"""Validate the local atlas without network access. Unit files use the JSON subset of YAML 1.2."""
from atlas_files import unit_files
import argparse
from collections import Counter
from datetime import date
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
BANNER = "AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved"
TRACKS = ("analytic", "arakelov", "theta", "galois", "local", "ktheory", "formal")
GRADES = ("L0", "L1", "L2", "L3", "L4")
STATUSES = ("Full", "Outlined", "Statement only")
REQUIRED = set("id title track statement assumptions lean expositions status grade reviews prerequisites size_pages open_questions last_checked".split())
DIGEST = re.compile(r"[0-9a-f]{64}\Z")


def distinct_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError(f"duplicate key {key!r}")
        result[key] = value
    return result


def read(path):
    return json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=distinct_keys)


def safe_file(root, name):
    if not isinstance(name, str) or not name:
        return False
    path = Path(name.split("#", 1)[0])
    return not path.is_absolute() and (root / path).resolve().is_relative_to(root.resolve()) and (root / path).is_file()


def validate(root, lean_src=None):
    root = root.resolve()
    errors = []
    def require(test, message):
        if not test:
            errors.append(message)
        return test

    units = {}
    for path in sorted(unit_files(root)):
        u = read(path)
        uid = u.get("id")
        require(isinstance(uid, str) and uid == path.stem, f"{path.name}: filename/id mismatch")
        if not require(uid not in units, f"duplicate unit {uid}"):
            continue
        units[uid] = u
    require(bool(units), "empty unit inventory")
    editions = read(root / "data/editions.json")["editions"]
    evidence = read(root / "data/grade_evidence.json")["records"]
    independent = read(root / "data/independent_confirmations.json")
    sources = read(root / "sources/registry.json")
    entries = sources["sources"] if isinstance(sources, dict) else sources
    source_ids = {s["id"] for s in entries}
    pin_registry = read(root / "data/pins.json")
    expected_pins = pin_registry["anchors"]
    require(pin_registry["source_commit"] == "40e56bab026552e089d7afcfeff08d2defb9c005", "unexpected Lean commit")
    require(pin_registry["archive_sha256"] == "9631b4f020199e580ba86178cb56c6e9b09f690c2369a80dc4334aa93f49c7fc", "unexpected Lean archive")
    review_index = {r["file"]:r for r in read(root / "reviews/index.json")["records"]}
    pins = {}
    total_anchors = 0
    from signoff_records import load_records
    record_list = load_records(root)
    for uid, u in units.items():
        result = lambda condition, msg: require(condition, f"{uid}: {msg}")
        if not result(REQUIRED <= u.keys(), f"missing {sorted(REQUIRED-u.keys())}"):
            continue
        result(u.get("notice") == BANNER, "missing evidence notice")
        for field in ("title", "statement"):
            result(isinstance(u[field], str) and u[field].strip(), f"empty {field}")
        for field in ("assumptions", "prerequisites", "open_questions", "expositions", "lean", "reviews"):
            result(isinstance(u[field], list), f"{field} must be a list")
        primary = u["track"]["primary"]
        secondary = u["track"]["secondary"]
        result(primary in TRACKS and isinstance(secondary, list) and set(secondary) <= set(TRACKS) and primary not in secondary and len(secondary)==len(set(secondary)), "invalid track assignments")
        result(u["status"] in STATUSES and u["grade"] in GRADES, "unknown status or grade")
        result(u["size_pages"] is None or type(u["size_pages"]) is int and u["size_pages"] > 0, "invalid page count")
        try:
            date.fromisoformat(u["last_checked"])
        except (TypeError, ValueError):
            result(False, "invalid check date")
        for dep in u["prerequisites"]:
            result(dep in units and dep != uid, f"unknown or self prerequisite {dep}")
        for assumption in u["assumptions"]:
            result(isinstance(assumption, str) and (assumption in units and assumption != uid or assumption.startswith("source:") and assumption[7:] in (source_ids | set(editions))), f"invalid assumption {assumption}")
        result(u["expositions"], "missing exposition or statement locator")
        for exp in u["expositions"]:
            doc = exp["document"]
            pages = exp["pages"]
            result(doc in editions or safe_file(root,doc), f"unknown document {doc}")
            result(isinstance(exp["section"],str) and exp["section"].strip(), "missing section")
            result(isinstance(pages,list) and (not pages or len(pages)==2 and all(type(n) is int for n in pages) and 0<pages[0]<=pages[1]), f"invalid page interval {pages}")
            if pages and doc in editions and editions[doc].get("pages"):
                result(pages[-1] <= editions[doc]["pages"], "interval beyond edition")
        result(u["lean"], "no pinned declaration")
        names = set()
        for a in u["lean"]:
            if not result(set("name file line0 line1 sha256 dominated".split())<=a.keys(), "incomplete declaration pin"):
                continue
            name, file, first, last, sha = (a[k] for k in ("name","file","line0","line1","sha256"))
            result(name not in names and isinstance(name,str) and name.strip(), f"empty or repeated declaration {name}")
            names.add(name)
            result(isinstance(file,str) and file.endswith(".lean") and not Path(file).is_absolute() and ".." not in Path(file).parts, "invalid Lean path")
            if not result(type(first) is int and type(last) is int and 0<first<=last, "invalid source interval"):
                continue
            result(bool(DIGEST.fullmatch(sha)), "invalid SHA-256")
            result(type(a["dominated"]) is int and a["dominated"]>=0 or a["dominated"] is None and bool(a.get("graph") or a.get("scope")), "invalid dominated-line metric")
            identity = (file,first,last,sha,a["dominated"])
            pin = expected_pins.get(name)
            result(pin and all(pin[k] == a[k] for k in ("file","line0","line1","sha256","dominated")), f"mismatch with independently verified declaration {name}")
            if pin and a.get("graph"):
                result(pin["graph"] == a["graph"], f"graph scope does not match {name}")
            if name in pins:
                result(pins[name] == identity, f"inconsistent pin for {name}")
            pins[name] = identity
            total_anchors += 1
        for rev in u["reviews"]:
            result(safe_file(root, rev) and rev.startswith("reviews/"), f"invalid review pointer {rev}")
        if u["grade"] == "L4":
            result(u.get("grade_before_human_check") in GRADES[:-1], "L4 requires a restorable prior grade")
        else:
            result("grade_before_human_check" not in u, "a superseded human grade must restore the prior grade")
        grade = u.get("grade_before_human_check", u["grade"])
        targets = set(u.get("statement_declarations", [u["lean"][0]["name"]] if u["lean"] else []))
        if grade in ("L1", "L2"):
            aligned = {n for r in evidence if r["review"] in u["reviews"] for n in r["declarations"]}
            result(targets and targets <= names and targets <= aligned, "missing evidence for one or more statement declarations")
        if grade == "L2":
            result(u["status"] == "Full" and bool(u["reviews"]), f"{grade} requires a written proof and a review")
            certifications = {n for r in evidence
                              if r["grade"] == "L2" and r["review"] in u["reviews"]
                              for n in r["declarations"]}
            result(targets and targets <= names and targets <= certifications, "missing matching declaration-specific L2 review")
        if grade == "L3":
            ids = independent.get(uid, [])
            result(len(set(ids)) >= 2 and set(ids)<=source_ids, "L3 requires two independent registered sources")
        from signoff_records import human_state, load_records
        step_file = root / "units" / (uid + ".steps.yaml")
        if u["grade"] == "L4" or step_file.is_file() and record_list:
            state = human_state(root, uid, read(step_file), record_list) if step_file.is_file() else {}
            result((u["grade"] == "L4") == bool(state.get("l4")), "L4 requires a Full unit, a derivation, and positive checks for the current statement and every active step")
    note_index = read(root / "data/notes.json")["units"]
    require(set(note_index) == set(units), "unit/excerpt coverage mismatch")
    for uid, note in note_index.items():
        require(safe_file(root, note["path"]), f"{uid}: missing indexed excerpt")
    for tex in (root / "notes").rglob("*.tex"):
        require(BANNER in tex.read_text(encoding="utf-8"), f"{tex.name}: excerpt notice")
    if lean_src is not None:
        source_lines = {}
        glossary = read(root / "data/glossary_sources.json")
        glossary_pins = [a for term in glossary["terms"]
                         for a in (term["definition"], *term["additional_definitions"])]
        for a in [*expected_pins.values(), *glossary_pins]:
            name, file, first, last = (a[k] for k in ("name", "file", "line0", "line1"))
            path = lean_src / file
            if not require(path.is_file(), f"{name}: missing source {file}"):
                continue
            if file not in source_lines:
                source_lines[file] = path.read_text(encoding="utf-8").splitlines()
            lines = source_lines[file]
            actual = hashlib.sha256("\n".join(lines[first-1:last]).encode()).hexdigest()
            require(0 < first <= last <= len(lines) and actual == a["sha256"], f"{name}: pinned source bytes disagree")
    for r in evidence:
        rec = review_index.get(r["review"])
        require(rec and safe_file(root,r["review"]), f"missing grade evidence {r['review']}")
        require(rec and rec["sha256"] == r["source_sha256"] and rec["source_path"] == r["source_review"], f"grade review identity {r['review']}")
        require(len(r["lines"]) == 2 and 0 < r["lines"][0] <= r["lines"][1], "invalid review line range")
    require(len(read(root / "data/blueprint_membership.json")) == 55, "blueprint membership cardinality")
    for key, uid in read(root / "data/blueprint_membership.json").items():
        require(uid in units, f"{key}: missing blueprint unit {uid}")
    graph = read(root / "data/graph.json")
    nodes = {n["id"]:n for n in graph["nodes"]}
    require(len(nodes)==len(graph["nodes"])==775, "paper graph must contain 775 distinct source entries")
    edges = {(e["from"],e["to"]) for e in graph["edges"]}
    require(all(a in nodes and b in nodes for a,b in edges), "unresolved graph edge")
    for node in nodes.values():
        path = node["reading_path"]
        require(node["unit_id"] in units and path and path[0]==node["unit_id"] and path[-1]==node["id"], f"{node['id']}: broken reading path")
        require(all((a,b) in edges for a,b in zip(path,path[1:])), f"{node['id']}: reading path absent from graph")
        require(expected_pins.get(node["name"])==node["source"], f"{node['id']}: graph declaration pin mismatch")
    starters = read(root / "data/notes_starters.json")["starters"]
    require(set(starters)==set(TRACKS), "seven distinct starter packets required")
    for track, packet in starters.items():
        require(packet["unit_id"] in units and safe_file(root,packet["path"]) and safe_file(root,packet["tex"]), f"{track}: missing starter unit or text")
        require(packet["lean_decl"] in expected_pins and packet.get("checkable_target"), f"{track}: starter declaration or scope missing")
        size=packet["size_pages"]
        pages=packet["printed_pages"]
        require(5<=size<=15 and size==len(pages)==len(packet["pdf_pages"]) and pages==list(range(pages[0], pages[-1]+1)), f"{track}: invalid starter interval")
        for page in pages:
            img=(root/packet["path"]).parent/"pages"/f"{page}.webp"
            require(img.is_file() and hashlib.sha256(img.read_bytes()).hexdigest()==packet["page_image_hashes"].get(str(page)), f"{track}: starter image differs on p. {page}")
    crosswalk = read(root/"crosswalk/adriazola.json")
    require(crosswalk["source_id"] in source_ids and crosswalk["lean_commit"]==pin_registry["source_commit"], "invalid crosswalk source revision")
    from resolve_crosswalk import render_text
    manuscript = next(entry for entry in entries if entry["id"] == crosswalk["source_id"])
    require(crosswalk["matching_source_revision"] == manuscript["revision"] and
            crosswalk["matching_pdf_sha256"] == manuscript["edition_evidence"]["pdf_sha256"],
            "crosswalk manuscript edition differs from the registered source")
    mappings = crosswalk["mappings"]
    routes = crosswalk["dependency_routes"]
    require((root / "crosswalk/adriazola.md").read_text() == render_text(crosswalk),
            "manuscript correspondence page differs from neutral source data")
    require(len(mappings) == 91 and "not contacted" in crosswalk["notice"]
            and "not reviewed" in crosswalk["notice"], "manuscript correspondence scope")
    for target, route in routes.items():
        uid=route["unit_id"]
        chain=route["path"]
        require(chain and chain[-1]==target and uid in units and chain[0] in {a["name"] for a in units[uid]["lean"]}, f"{target}: bad reading route endpoints")
    require(len({m["id"] for m in mappings}) == len(mappings), "duplicate crosswalk ID")
    require(sum(m["kind"]=="numbered_hypothesis" for m in mappings)==43, "incomplete numbered hypothesis inventory")
    for m in mappings:
        key=m["id"]
        matched=set(m.get("matched_propositions",[]))
        refs={a["name"] for a in m["lean_declarations"]}
        require(matched <= refs, f"{key}: target missing from compared source")
        for src in m["lean_declarations"]:
            pin=expected_pins.get(src["name"])
            require(pin and (src["file"],src["line_start"],src["line_end"],src["sha256"]) == (pin["file"],pin["line0"],pin["line1"],pin["sha256"]), f"{key}: invalid compared declaration")
        for target, uid in m.get("reading_routes",{}).items():
            require(target in routes and routes[target]["unit_id"]==uid, f"{key}: unregistered reading route")
        require(set(m["unit_ids"]+m.get("contextual_unit_ids",[]))<=units.keys(), f"{key}: missing mapped unit")
        allowed_fields = {"id", "external_id", "kind", "section", "page", "relation",
                          "unit_ids", "contextual_unit_ids", "reading_routes", "lean_declarations",
                          "matched_propositions", "matches"}
        relation = m["relation"]
        require(m.keys() <= allowed_fields and relation in {"exact", "partial", "none"},
                f"{key}: unexpected correspondence field or match type")
        require(relation == "none" or bool(refs), f"{key}: mapped item has no declaration")
        require((relation == "exact") == bool(matched), f"{key}: exact proposition locator")
        for match in m["matches"]:
            uid=match["unit_id"]
            name=match["lean_declaration"]
            if match.get("node_id"):
                n=nodes.get(match["node_id"])
                require(n and n["unit_id"]==uid and n["name"]==name, f"{key}: graph/unit/name mismatch")
            else:
                require(uid in units and name in {a["name"] for a in units[uid]["lean"]}, f"{key}: declaration not on named card")
    for track in TRACKS:
        require(safe_file(root,f"tracks/{track}/README.md"),f"missing track {track}")
    from validate_round3 import check as validate_round3
    errors.extend(validate_round3(root, units, lean_src))
    from signoff_records import validate as validate_signoffs
    errors.extend(validate_signoffs(root))
    from snapshot import check as validate_progress
    errors.extend(validate_progress(root))
    from validate_round4 import check as validate_round4
    errors.extend(validate_round4(root, units, lean_src))
    from validate_round5 import check as validate_round5
    errors.extend(validate_round5(root, units))
    from validate_round6 import check as validate_round6
    errors.extend(validate_round6(root, units, lean_src))
    from validate_reader import check as validate_reader
    errors.extend(validate_reader(root, units, sources, expected_pins, BANNER))
    return errors, {"units":len(units),"indexed_declarations":len(expected_pins),"distinct_unit_declarations":len(pins),"declaration_entries":total_anchors,
                    "grades":dict(sorted(Counter(u["grade"] for u in units.values()).items()))}


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root",type=Path,default=ROOT)
    parser.add_argument("--lean-src",type=Path,help="add exact source-span byte checks against a local Lean src tree")
    args=parser.parse_args()
    try:
        errors, summary=validate(args.root.resolve(),args.lean_src)
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(f"Invalid atlas: {exc}",file=sys.stderr)
        return 1
    print(json.dumps({**summary,"errors":len(errors)},ensure_ascii=False))
    for error in errors:
        print(error,file=sys.stderr)
    return bool(errors)


if __name__ == "__main__":
    sys.exit(main())
