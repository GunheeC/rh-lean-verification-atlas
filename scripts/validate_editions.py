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
    paper = catalog["paper2_v8"]
    blueprint = catalog["blueprint_v13c"]
    original = catalog["blueprint_v13"]
    preceding = catalog["blueprint_v13a"]
    release_dir = root / "editions/v0.1.0"
    checksums = {}
    for key, filename in (("paper2_v8", "paper_v8.pdf"), ("blueprint_v13c", "blueprint_v13c.pdf")):
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
    expected_files = {"SHA256SUMS", "paper_v8.pdf", "blueprint_v13c.pdf"}
    if not release_dir.is_dir() or {p.name for p in release_dir.iterdir()} != expected_files:
        errors.append("Unexpected release-edition inventory")
    if catalog != read("data/notes.json")["editions"]:
        errors.append("Reading index and edition register disagree")
    v13a_text = read(preceding["page_text_comparison"])
    old_hashes = v13a_text["common_text_sha256_by_v13_physical_page"]
    count = original["pages"]
    if (fingerprint(root / preceding["page_text_comparison"]) != preceding["page_text_comparison_sha256"]
            or v13a_text["source_sha256"] != original["sha256"]
            or v13a_text["target_sha256"] != preceding["sha256"]
            or preceding["retained_v13_pages"] != count or len(old_hashes) != count):
        errors.append("Historical v13a per-sheet comparison is inconsistent")
    comparison = read(blueprint["page_comparison"])
    rows = comparison["pages"]
    exceptions = {row["old_physical"]: row for row in comparison["exceptions"]}
    expected_sheets = set(range(1, count + 1))
    if (fingerprint(root / blueprint["page_comparison"]) != blueprint["page_comparison_sha256"]
            or comparison["source_sha256"] != original["sha256"]
            or comparison["target_sha256"] != blueprint["sha256"]
            or comparison["front_pages"] != blueprint["new_front_pages"]
            or comparison["old_physical_pages"] != count or blueprint["retained_v13_pages"] != count
            or blueprint_page(blueprint, count) != blueprint["pages"]
            or len(rows) != count or {row["old_physical"] for row in rows} != expected_sheets
            or set(exceptions) != {1, 2} or len(comparison["exceptions"]) != len(exceptions)
            or comparison["identical_pages"] != count - len(exceptions)):
        errors.append("Blueprint v13c sheet inventory or recorded exception set differs")
    for row in rows:
        n = row["old_physical"]
        if n not in expected_sheets:
            continue
        changed = n in exceptions
        if row["new_physical"] != blueprint_page(blueprint, n) or row["source_text_sha256"] != old_hashes[n - 1]:
            errors.append(f"Blueprint v13 sheet {n}: inconsistent page or source text")
        for kind in ("text", "stream", "raster"):
            source = row[f"source_{kind}_sha256"]
            target = row.get(f"target_{kind}_sha256", source)
            if (not all(re.fullmatch("[0-9a-f]{64}", h) for h in (source, target))
                    or (source != target) != changed):
                errors.append(f"Blueprint v13 sheet {n}: unexpected {kind} comparison")
    if any(not row["reason"] or not row["text_diff"] or
           row["new_physical"] != blueprint_page(blueprint, n) for n, row in exceptions.items()):
        errors.append("Missing description of the two revised blueprint sheets")
    parent = catalog["blueprint_v13b"]
    parent_rows = read(parent["page_comparison"])["pages"]
    preceding_comparison = blueprint["comparison_with_preceding"]
    front_rows = preceding_comparison["unchanged_front_sheets"]
    revised_front = preceding_comparison["changed_front_sheets"]
    front_ids = {r["physical_sheet"] for r in front_rows}
    revised_ids = {r["sheet"] for r in revised_front}
    if (fingerprint(root / parent["page_comparison"]) != parent["page_comparison_sha256"]
            or blueprint["revised_from"] != "blueprint_v13b" or len(parent_rows) != len(rows)
            or preceding_comparison["source_edition"] != "blueprint_v13b"
            or preceding_comparison["source_sha256"] != parent["sha256"]
            or preceding_comparison["target_sha256"] != blueprint["sha256"]
            or preceding_comparison["retained_sheets_with_identical_text_content_streams_and_rasters"] != count
            or front_ids & revised_ids or len(front_ids) != len(front_rows) or len(revised_ids) != len(revised_front)
            or front_ids | revised_ids != set(range(1, blueprint["new_front_pages"]+1))
            or not {1,2} <= revised_ids):
        errors.append("The v13b–v13c sheet comparison refers to the wrong editions or length")
    for kind in ("text_sha256", "stream_sha256", "raster_sha256"):
        if (any(not re.fullmatch("[0-9a-f]{64}", r[kind]) for r in front_rows)
                or any(r["source"][kind] == r["target"][kind] or
                       not all(re.fullmatch("[0-9a-f]{64}", r[key][kind]) for key in ("source","target"))
                       for r in revised_front)):
            errors.append(f"The revised and retained blueprint front matter has invalid {kind} evidence")
    for row, previous_row in zip(rows, parent_rows):
        if row["old_physical"] != previous_row["old_physical"] or any(
                row.get("target_" + kind + "_sha256", row["source_" + kind + "_sha256"]) !=
                previous_row.get("target_" + kind + "_sha256", previous_row["source_" + kind + "_sha256"])
                for kind in ("text", "stream", "raster")):
            errors.append(f"Retained sheet {row['old_physical']} differs between v13b and v13c")
    packets = read("data/notes_starters.json")["starters"]
    note_index = (root / "notes/README.md").read_text()
    for track, packet in packets.items():
        if packet_page_links(blueprint, packet) not in note_index:
            errors.append(f"{track}: packet index lacks a current blueprint page link")
    if any(set(packet["pdf_pages"]) & exceptions.keys() for packet in packets.values()):
        errors.append("A packet cites a revised original blueprint sheet")
    previous = catalog["paper2_v7"]["unit_locators"]
    labels = read(paper["label_index"])
    if (fingerprint(root / paper["label_index"]) != paper["label_index_sha256"]
            or labels["source_pdf_sha256"] != paper["sha256"] or paper["review_status"] != "pending_review"):
        errors.append("Paper label register is stale or the new edition's review status has changed")
    math = paper["source_math_comparison"]
    if (math["source_edition"] != "paper2_v7"
            or math["source_pdf_sha256"] != catalog["paper2_v7"]["sha256"]
            or math["target_pdf_sha256"] != paper["sha256"]
            or math["target_aux_sha256"] != labels["latex_aux_sha256"]
            or not math["compilation_inputs_verified"]):
        errors.append("Mathematical source comparison is attached to a different edition")
    for name, count in (("four", 111), ("all", 966)):
        entry = math["comparisons"][name]
        if (entry["count"] != count or sum(entry["by_type"].values()) != count or entry["diff_bytes"] != 0
                or not re.fullmatch("[0-9a-f]{64}", entry["common_ordered_bytes_sha256"])):
            errors.append(f"Unexpected {name} environment comparison")
    offset = paper["arabic_page_one_pdf_page"] - 1
    guide = paper["new_reader_exposition"]
    locations = guide["locations"]
    if (guide["review_status"] != "pending_review" or guide["section"] != "2"
            or set(locations) != {"start", "end", "figure", "table"}
            or locations["end"]["pdf_page"] < locations["start"]["pdf_page"]):
        errors.append("The new reader account has an unexpected extent, figure, table or review status")
    for loc in locations.values():
        if (not loc["label"] or not loc["destination"] or loc["pdf_page"] != loc["printed_page"] + offset
                or not locations["start"]["pdf_page"] <= loc["pdf_page"] <= locations["end"]["pdf_page"] <= paper["pages"]):
            errors.append("The proof-guide register refers to an incorrect PDF page")
    coverage = read(paper["coverage_label_index"])
    if (fingerprint(root / paper["coverage_label_index"]) != paper["coverage_label_index_sha256"]
            or coverage["source_pdf_sha256"] != paper["sha256"]
            or coverage["latex_aux_sha256"] != labels["latex_aux_sha256"]):
        errors.append("Coverage and reading-task labels refer to a different AUX or PDF")
    for name, folio in coverage["printed_pages"].items():
        destination = coverage["named_destinations"][name]
        if not destination["name"] or not 1 <= folio + offset == destination["pdf_page"] <= paper["pages"]:
            errors.append(f"Coverage reference {name}: invalid folio or physical page")
    scope = paper["new_coverage_programme"]
    locs = scope["locations"]
    if (scope["section"] != "3" or scope["review_status"] != "pending_review"
            or set(locs) != {"start","end","map","table","figure","tasks","gaps","programme"}):
        errors.append("Section 3 coverage register is incomplete")
    for loc in locs.values():
        target = coverage["named_destinations"].get(loc["label"], {})
        if (coverage["printed_pages"].get(loc["label"]) != loc["printed_page"]
                or loc["pdf_page"] != target.get("pdf_page") or loc["destination"] != target.get("name")
                or not locs["start"]["pdf_page"] <= loc["pdf_page"] <= locs["end"]["pdf_page"]):
            errors.append(f"Section 3 coverage location {loc['label']} differs from the resolved destination")
    for uid, entries in paper["unit_locators"].items():
        if uid not in units:
            errors.append(f"{uid}: unknown unit in paper-v8 page register")
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
    if set(previous) != set(paper["unit_locators"]):
        errors.append("Current and preceding paper locators cover different units")
    for uid, entries in previous.items():
        expected = {(e["start_label"], e["end_label"]) for e in entries}
        actual = {(e["start_label"], e["end_label"]) for e in paper["unit_locators"].get(uid, [])}
        if expected != actual or len(entries) != len(paper["unit_locators"].get(uid, [])):
            errors.append(f"{uid}: v8 passage list differs from the v7 edition")
    return errors


if __name__ == "__main__":
    from atlas_files import unit_files

    root = Path(__file__).resolve().parents[1]
    units = {p.stem: json.loads(p.read_bytes()) for p in unit_files(root)}
    failures = check(root, units)
    for failure in failures:
        print(failure)
    raise SystemExit(bool(failures))
