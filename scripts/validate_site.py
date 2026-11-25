"""Check links, search results and source registrations in the local HTML edition."""
from collections import Counter
from html.parser import HTMLParser
import json
import re
from pathlib import Path
from urllib.parse import unquote, urlsplit


class PageLinks(HTMLParser):
    def __init__(self, html):
        super().__init__()
        self.ids = set()
        self.links = []
        self.search_rows = []
        self.is_catalog = False
        self.notice_parts = None
        self.notices = []
        self.feed(html)
        self.close()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        for key in ("href", "src"):
            if attrs.get(key):
                self.links.append(attrs[key])
        if tag == "p" and "notice" in attrs.get("class", "").split():
            self.notice_parts = []
        self.is_catalog = tag == "script" and attrs.get("id") == "catalog"

    def handle_endtag(self, tag):
        if tag == "script":
            self.is_catalog = False
        if tag == "p" and self.notice_parts is not None:
            self.notices.append("".join(self.notice_parts).strip())
            self.notice_parts = None

    def handle_data(self, text):
        if self.notice_parts is not None:
            self.notice_parts.append(text)
        if self.is_catalog:
            self.search_rows = json.loads(text)
            for _, location, units, _, _ in self.search_rows:
                self.links.append(location)
                self.links.extend(f"../units/{unit}.html" for unit in units)


def validate(root, site):
    from validate import BANNER
    from validate_reader import registered_external_checker
    read = lambda p: json.loads((root / p).read_text())
    external_ok = registered_external_checker(root)
    # The in-checkout site shares the signed repository PDF bytes. A portable
    # export resolves the same documents under its own editions directory.
    in_checkout = site.resolve() == (root / "site").resolve()
    document_root = root if in_checkout else site
    documents = {(document_root / e["repository_file"]).resolve(): e["pages"]
                 for e in read("data/editions.json")["editions"].values() if "repository_file" in e}
    receipts = set(documents) | {(document_root / "editions/v0.1.0/SHA256SUMS").resolve()}
    errors = []
    counts = Counter()
    pages = {file.resolve(): PageLinks(file.read_text()) for file in sorted(site.rglob("*.html"))}
    search = pages.get((site / "lookup/search.html").resolve())
    expected = read("data/declarations.json")["declarations"]
    if search is None or [r[0] for r in search.search_rows] != [r["name"] for r in expected]:
        errors.append("The search catalog differs from data/declarations.json.")
    for file, page in pages.items():
        if page.notices != [BANNER]:
            errors.append(f"{file.relative_to(site)}: expected one visible AI review notice")
        for href in page.links:
            parts = urlsplit(href)
            if parts.scheme or parts.netloc:
                counts["external"] += 1
                if not external_ok(href):
                    errors.append(f"{file.relative_to(site)}: unregistered URL {href}")
                continue
            location = (file.parent / unquote(parts.path)).resolve() if parts.path else file
            counts["local"] += 1
            if (not location.is_relative_to(site) and location not in receipts) or not location.is_file():
                errors.append(f"{file.relative_to(site)}: broken destination {href}")
            elif parts.fragment and location in documents:
                match = re.fullmatch(r"page=([1-9]\d*)", parts.fragment)
                if not match or int(match[1]) > documents[location]:
                    errors.append(f"{file.relative_to(site)}: invalid physical PDF page {href}")
            elif parts.fragment and location in pages:
                counts["fragments"] += 1
                if unquote(parts.fragment) not in pages[location].ids:
                    errors.append(f"{file.relative_to(site)}: missing fragment {href}")
    return counts, errors
