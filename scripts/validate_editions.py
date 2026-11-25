"""Verify the two repository PDFs, page evidence, packet links and current paper locators."""
import hashlib
import json
from pathlib import Path
import re

from edition_links import blueprint_page, packet_page_links


def fingerprint(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def check(root, units):
    def read(path):
        return json.loads((root / path).read_bytes())

    errors = []
    catalog = read("data/editions.json")["editions"]
    paper = catalog["paper2_v6"]
    blueprint = catalog["blueprint_v13a"]
    release_dir = root / "editions/v0.1.0"
    checksums = {}
    for key, filename in (("paper2_v6", "paper_v6.pdf"), ("blueprint_v13a", "blueprint_v13a.pdf")):
        ed = catalog[key]
        path = release_dir / filename
        if ed["repository_file"] != path.relative_to(root).as_posix() or not path.is_file():
            errors.append(f"{key}: repository PDF is missing or incorrectly named")
            continue
        checksums[filename] = fingerprint(path)
        if checksums[filename] != ed["sha256"] or ed["sha256"] not in (root / "RELEASE_NOTES_v0.1.0.md").read_text():
            errors.append(f"{key}: PDF checksum differs from edition register or release notes")
    checksum_file = release_dir / "SHA256SUMS"
    entries = checksum_file.read_text().splitlines() if checksum_file.is_file() else []
    if sorted(entries) != sorted(f"{h}  {f}" for f, h in checksums.items()):
        errors.append("Repository PDF checksum manifest differs from registered documents")
    expected_files = {"SHA256SUMS", "paper_v6.pdf", "blueprint_v13a.pdf"}
    if not release_dir.is_dir() or {p.name for p in release_dir.iterdir()} != expected_files:
        errors.append("Unexpected release-edition inventory")
    if catalog != read("data/notes.json")["editions"]:
        errors.append("Reading index and edition register disagree")
    evidence = read(blueprint["page_text_comparison"])
    sheets = evidence["common_text_sha256_by_v13_physical_page"]
    count = blueprint["retained_v13_pages"]
    if (fingerprint(root / blueprint["page_text_comparison"]) != blueprint["page_text_comparison_sha256"]
            or evidence["source_sha256"] != catalog["blueprint_v13"]["sha256"]
            or evidence["target_sha256"] != blueprint["sha256"]
            or evidence["new_front_pages"] != blueprint["new_front_pages"]
            or len(sheets) != count or count != catalog["blueprint_v13"]["pages"]
            or blueprint_page(blueprint, count) != blueprint["pages"]
            or not all(re.fullmatch("[0-9a-f]{64}", h) for h in sheets)):
        errors.append("Blueprint PDF or per-sheet text comparison is inconsistent")
    packets = read("data/notes_starters.json")["starters"]
    note_index = (root / "notes/README.md").read_text()
    for track, packet in packets.items():
        if packet_page_links(blueprint, packet) not in note_index:
            errors.append(f"{track}: packet index lacks a current blueprint page link")
    previous = catalog["paper2_v5"]["unit_locators"]
    labels = read(paper["label_index"])
    if (fingerprint(root / paper["label_index"]) != paper["label_index_sha256"]
            or labels["source_pdf_sha256"] != paper["sha256"] or paper["review_status"] != "pending_review"):
        errors.append("Paper label register is stale or the new edition's review status has changed")
    offset = paper["arabic_page_one_pdf_page"] - 1
    for uid, entries in paper["unit_locators"].items():
        if uid not in units:
            errors.append(f"{uid}: unknown unit in paper-v6 page register")
            continue
        for e in entries:
            first, last = e["printed_pages"]
            if (labels["printed_pages"].get(e["start_label"]) != first
                    or labels["printed_pages"].get(e["end_label"]) != last
                    or e["pdf_pages"] != [labels["named_destinations"].get(k, {}).get("pdf_page")
                                          for k in (e["start_label"], e["end_label"])]
                    or e["pdf_pages"] != [offset + first, offset + last]
                    or not 1 <= first <= last <= paper["pages"] - offset):
                errors.append(f"{uid}: invalid paper PDF pages for {e['start_label']}")
    for uid, entries in previous.items():
        expected = {(e["start_label"], e["end_label"]) for e in entries}
        actual = {(e["start_label"], e["end_label"]) for e in paper["unit_locators"].get(uid, [])}
        if not expected <= actual:
            errors.append(f"{uid}: missing a current counterpart for a v5 conditional or List A passage")
    return errors


if __name__ == "__main__":
    from atlas_files import unit_files

    root = Path(__file__).resolve().parents[1]
    units = {p.stem: json.loads(p.read_bytes()) for p in unit_files(root)}
    failures = check(root, units)
    for failure in failures:
        print(failure)
    raise SystemExit(bool(failures))
