"""Check the reader edition, Markdown navigation and reproducible products offline."""
from collections import Counter
from functools import lru_cache
import json
from pathlib import Path
import re
import subprocess
import sys
from urllib.parse import unquote


FENCES = re.compile(r"^\s*(\x60{3,}|~{3,})[^\n]*\n.*?^\s*\1[ \t]*$", re.M | re.S)
INLINE = re.compile(r"(\x60+)[^\n]*?\1")
LINK = re.compile(r"\]\(\s*(?:<([^>\n]+)>|([^\s)]+))(?:\s+\"[^\"]*\")?\s*\)")
EXTERNAL = re.compile(r"https?://[^\s<>)\]\"\x60]+")
HTML_TARGET = re.compile(r"""(?:href|src)\s*=\s*["']([^"']+)["']""", re.I)
HANGUL = re.compile(r"[가-힣]")
FRONT = ("README.md", "STATUS.md", "MAP.md", "LANDSCAPE.md", "FAQ.md", "CHANGELOG.md",
         "CONTRIBUTING.md", "NOTICE.md",
         "lookup/declarations.md", "lookup/glossary.md", "signoffs/README.md", "OVERVIEW.md",
         "RELEASE_NOTES_v0.1.0.md", "PROGRESS.md", "AUTHORS.md", "ROADMAP.md", "docs/reading-orders.md", "pillars/V.md", "pillars/F.md")


def strings(value):
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for item in value:
            yield from strings(item)
    elif isinstance(value, dict):
        yield from strings(list(value.values()))


@lru_cache(maxsize=1024)
def anchors(path):
    content = FENCES.sub("", path.read_text(encoding="utf-8"))
    found = set(re.findall(r"""(?:id|name)=["']([^"']+)["']""", content))
    headings = Counter()
    for heading in re.findall(r"^#{1,6}\s+(.+?)\s*#*\s*$", content, re.M):
        label = re.sub(r"\[([^]]+)\]\([^)]*\)", r"\1", heading).lower()
        base = re.sub(r"[^\w\s-]", "", label).replace(" ", "-")
        n = headings[base]
        found.add(f"{base}-{n}" if n else base)
        headings[base] += 1
    return found


def registered_external_checker(root, registry=None, pins=None):
    def read(name):
        return json.loads((root / name).read_text(encoding="utf-8"))
    if registry is None:
        registry = read("sources/registry.json")
    if pins is None:
        pins = read("data/pins.json")["anchors"]
    known = {s for s in strings(registry) if s.startswith(("http://", "https://"))}
    known.update(read(registry["crosswalk_evidence_urls"])["urls"])
    editions = read("data/editions.json")["editions"]
    for edition in editions.values():
        asset = edition.get("release_asset")
        if asset:
            starts = {span["pages"][0] for spans in edition.get("unit_locators", {}).values() for span in spans}
            known.update(asset + "#page=" + str(page) for page in starts)
    lean = next(s for s in registry["sources"] if s["id"] == "lean-repository")
    prefix = lean["source_blob_prefix"]
    registered = list(pins.values())
    for term in read("data/glossary_sources.json")["terms"]:
        registered += [term["definition"], *term.get("additional_definitions", [])]
    spans = {(a["file"], a["line0"], a["line1"]) for a in registered}
    for a in read("data/round4_changes.json")["citations"]:
        spans.add((a["file"], a["line0"], a["line1"]))
    for row in read("data/round6_review_corrections.json")["citations"]:
        spans.add((row["file"], row["line0"], row["line1"]))
    # These are the exact public-export signature groups on the primary evidence page.
    spans.update({("Main.lean", 4, 12), ("Statements.lean", 3, 16)})

    def external_ok(url):
        if url in known and url != prefix:
            return True
        if not url.startswith(prefix):
            return False
        m = re.fullmatch(r"([^#?]+)#L([1-9]\d*)(?:-L([1-9]\d*))?", unquote(url[len(prefix):]))
        return m and (m[1], int(m[2]), int(m[3] or m[2])) in spans

    return external_ok


def reader_quotations(root):
    """The signed reader text may be in the reader's own language."""
    from collections import defaultdict
    from signoff_records import OBJECTIONS, load_records, safe_text
    allowed = defaultdict(set)
    for _, record in load_records(root):
        name = safe_text(record["reader"]["name"])
        allowed["AUTHORS.md"].add(name)
        allowed[f"units/{record['unit']}.check.md"].add(name)
        if set(record["verdict"].values()) & OBJECTIONS or record.get("resolves"):
            allowed["questions/disputes.md"].add(name)
        if set(record["verdict"].values()) & OBJECTIONS:
            allowed["questions/disputes.md"].add(safe_text(record["reservations"]))
    return allowed


def check(root, units, registry, pins, banner):
    errors = []
    for f in FRONT:
        if not (root / f).is_file():
            errors.append("missing reader page " + f)
    slugs = set()
    for uid, u in units.items():
        slug = u.get("slug", "")
        if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", slug) or slug in slugs:
            errors.append(f"{uid}: invalid or duplicate slug")
        slugs.add(slug)
        for field in ("aliases", "hypothesis_details", "background", "open_questions"):
            items = u.get(field)
            if not isinstance(items, list) or not items or not all(isinstance(s, str) and s.strip() for s in items):
                errors.append(f"{uid}: missing itemized {field}")
        if u["statement"] in u.get("hypothesis_details", []):
            errors.append(f"{uid}: hypothesis repeats statement")
    external_ok = registered_external_checker(root, registry, pins)
    personal_quotes = reader_quotations(root)
    korean = {"README.ko.md", "docs/ko/README.md", "docs/ko/STATUS.md", "docs/ko/FAQ.md", "docs/ko/signoffs/README.md", "docs/ko/OVERVIEW.md", "docs/ko/pillars/V.md", "docs/ko/pillars/F.md", *(f"docs/ko/{u['track']['primary']}.md" for u in units.values())}
    for path in sorted(korean):
        if not (root / path).is_file():
            errors.append(f"missing Korean mirror {path}")
    anchors.cache_clear()
    for path in sorted(root.rglob("*.md")):
        rel = path.relative_to(root)
        if any(x in rel.parts for x in (".git", "site")):
            continue
        body = path.read_text(encoding="utf-8")
        if banner not in body.splitlines():
            errors.append(f"{rel}: missing exact evidence notice line")
        content = FENCES.sub("", body)
        prose = INLINE.sub("", content)
        archival = rel.parts[0] == "archive"
        if not archival and rel.as_posix() not in korean:
            english = content
            for quote in sorted(personal_quotes.get(rel.as_posix(), ()), key=len, reverse=True):
                english = english.replace(quote, "")
            english = INLINE.sub("", english).replace("[한국어]", "").replace("[한국어판]", "")
            if HANGUL.search(english):
                errors.append(f"{rel}: unexpected Korean text on an English page")
            if not re.search(r"\b[A-Za-z]{3,}\b", english.replace(banner, "")):
                errors.append(f"{rel}: missing English text")
        targets = {a or b for a, b in LINK.findall(prose)} | set(HTML_TARGET.findall(prose))
        if not archival:
            for url in EXTERNAL.findall(prose):
                targets.add(url.rstrip(".,;"))
        for target in sorted(targets):
            if target.startswith(("http://", "https://")):
                if not archival and not external_ok(target):
                    errors.append(f"{rel}: unregistered external URL {target}")
                continue
            name, _, fragment = target.partition("#")
            loc = (path.parent / unquote(name)).resolve() if name else path
            if not loc.is_relative_to(root) or not loc.exists():
                errors.append(f"{rel}: broken local link {target}")
            elif fragment and loc.suffix.lower() == ".md" and unquote(fragment) not in anchors(loc):
                errors.append(f"{rel}: broken local anchor {target}")

    for script in ("proof_steps.py", "front_counts.py", "signoff_authors.py", "roadmap.py", "build_navigation.py", "enrich_units.py", "unit_pages.py", "dashboard.py", "build_site.py"):
        result = subprocess.run([sys.executable, str(root / "scripts" / script), "--check"], cwd=root,
                                capture_output=True, text=True)
        if result.returncode:
            errors.append((result.stderr or result.stdout or f"{script} failed").strip())
    packets = subprocess.run([sys.executable, str(root / "scripts/verify_page_provenance.py")],
                             cwd=root, capture_output=True, text=True)
    if packets.returncode:
        errors.append((packets.stderr or packets.stdout or "page provenance failed").strip())
    from validate_name_crosswalk import validate as validate_names
    errors.extend(validate_names(root))
    return errors
