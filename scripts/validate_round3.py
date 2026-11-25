"""Check the round-3 written arguments, edition locators and reading paths."""
import hashlib
import json
from pathlib import Path
import re


def check(root, units, lean_src=None):
    def read(path):
        return json.loads((root / path).read_bytes())

    ledger = read("data/round3_changes.json")
    edition = read("data/editions.json")["editions"]["paper2_v4"]
    v4 = read("data/round3_v4.json")
    errors = []
    changes = {r["id"]: r for r in ledger["changes"]}
    later = read("data/round4_changes.json")
    changed_later = {r["id"] for r in later["changes"]}
    reviewed_later = set(later["review_grade_changes"])
    archive = read("archive/reviewed_editions/round3.json")["notes"]
    grade_ledger = read("data/grade_evidence.json")
    reports = grade_ledger["round3_review_reports"]
    reviews = {r["note"]: r for r in grade_ledger["round3_note_reviews"]}
    submitted = {d["path"] for u in ledger["changes"] for d in u["notes"]}
    if set(archive) != submitted or set(reviews) != submitted or len(reviews) != len(grade_ledger["round3_note_reviews"]):
        errors.append("DB3 reviewed-edition inventory differs from the submitted note set")
    if len(changes) != len(ledger["changes"]):
        errors.append("duplicated round-3 unit")
    # These are historical row counts in the printed v4 table.
    if len(v4["hypothesis_table"]) != 34 or len(v4["list_a"]) != 10:
        errors.append("incomplete v4 hypothesis table or list A")
    if edition["sha256"] != "a72979e4b067c41df977183b0a761f47b1e12ba8137a79d1136c06dc3ff1dab7" or edition["pages"] != 358:
        errors.append("v4 manuscript differs from the imported edition")
    baseline = read("data/round2_reading_inputs.json")["units"]
    for track, sections in ledger["reading_paths"].items():
        text = (root / "tracks" / track / "README.md").read_text()
        sequence = text.split("### First reading", 1)[1].split("### Open inputs and scope", 1)[0].split("### Core argument")
        for kind, body in zip(("first", "core"), sequence, strict=True):
            ids = re.findall(r"^\d+\. \[([^\]]+)\]\(../../units/[^)]+\)", body, flags=re.M)
            if ids != sections[kind]:
                errors.append(f"{track}: {kind} path differs from the audited list")
            for uid in ids:
                if units[uid]["status"] not in ("Full", "Outlined"):
                    errors.append(f"{track}: {uid} missing a written argument")
    all_spans = []
    for uid, original in baseline.items():
        unit = units[uid]
        prior_grade = unit.get("grade_before_human_check", unit["grade"])
        if unit["last_checked"] <= ledger["date"] and prior_grade != original["baseline"]["grade"] and uid not in reviewed_later:
            errors.append(f"{uid}: existing grade differs from the database-round baseline")
    for row in changes.values():
        uid = row["id"]
        u = units[uid]
        if row.get("review_status") != "pending_review" or not row["weakest_step"].strip():
            errors.append(f"{uid}: incomplete round-3 referee record")
        if uid in baseline and row["grade"] != baseline[uid]["baseline"]["grade"]:
            errors.append(f"{uid}: DB3 changed the prior verification grade")
        if uid not in changed_later | reviewed_later and (u.get("grade_before_human_check", u["grade"]) != row["grade"] or u["status"] != row["status"]):
            errors.append(f"{uid}: current status differs from its change record")
        if not row["notes"] or sum(doc["pages"] for doc in row["notes"]) != row["pages_written"]:
            errors.append(f"{uid}: missing argument or inconsistent pagination")
        for doc in row["notes"]:
            file = root / doc["path"]
            if not file.resolve().is_relative_to((root / "notes/units").resolve()) or not file.is_file():
                errors.append(f"{uid}: missing local argument {doc['path']}")
                continue
            raw = file.read_bytes()
            archive_text = archive.get(doc["path"], "")
            if hashlib.sha256(archive_text.encode()).hexdigest() != doc["sha256"] or "pending_review" not in archive_text:
                errors.append(f"{uid}: archived submitted note differs from the DB3 edition")
            review = reviews.get(doc["path"], {})
            if (review.get("unit") != uid or review.get("reviewed_sha256") != doc["sha256"]
                    or review.get("current_sha256") != hashlib.sha256(raw).hexdigest()
                    or review.get("same_edition") != (raw == archive_text.encode())):
                errors.append(f"{uid}: stale DB3 review attribution for the current or submitted note")
            if review.get("accepted_whole_note") and (not review.get("same_edition") or
                        review.get("original_verdict") not in {"CONFIRMED", "FAITHFUL OUTLINE"}):
                errors.append(f"{uid}: an altered edition or qualified verdict was treated as whole-note acceptance")
            report = next((v for v in reports.values() if v["path"] == review.get("review")), None)
            if report:
                report_bytes = (root / report["path"]).read_bytes()
                report_lines = report_bytes.decode().splitlines()
                line = review["summary_line"]
                lo, hi = review["review_range"]
                if (not 1 <= line <= len(report_lines) or not 1 <= lo <= hi <= len(report_lines)
                        or hashlib.sha256(report_bytes).hexdigest() != report["published_sha256"]
                        or report["original_sha256"] != review["original_review_sha256"]
                        or report["published_sha256"] != review["published_review_sha256"]):
                    errors.append(f"{uid}: invalid referee report, hash or lines")
                else:
                    cells = report_lines[line-1].split("|")
                    expected_key = Path(doc["path"]).stem if report["path"].endswith("_A.md") else uid
                    if len(cells)<4 or cells[1].strip()!=expected_key or cells[2].strip()!=review["original_verdict"]:
                        errors.append(f"{uid}: the saved original verdict differs from the referee's table")
            else:
                errors.append(f"{uid}: missing source report for the DB3 verdict")
            if not any(e["document"] == doc["path"] for e in u["expositions"]):
                errors.append(f"{uid}: local note absent from reading card")
        all_spans.extend(row["lean_ranges"])
    all_spans.extend(row["lean_range"] for row in v4["hypothesis_table"])
    prereqs = read("data/round3_prerequisites.json")
    all_spans.extend(prereqs["declarations"].values())
    for uid, u in units.items():
        origins = u.get("prerequisite_sources", {})
        if set(origins) != set(u["prerequisites"]) or set(origins.values()) - {"graph", "statement-reading"}:
            errors.append(f"{uid}: incomplete prerequisite evidence")
    file_hashes = ledger["source_file_sha256"]
    cache = {}
    for p in all_spans:
        f, a, b = p["file"], p["line0"], p["line1"]
        if Path(f).is_absolute() or ".." in Path(f).parts or not 0 < a <= b or not re.fullmatch("[0-9a-f]{64}", p["sha256"]):
            errors.append(f"{f}: invalid round-3 citation")
            continue
        if lean_src is None:
            continue
        if f not in cache:
            raw = (lean_src / f).read_bytes()
            if f in file_hashes and hashlib.sha256(raw).hexdigest() != file_hashes[f]:
                errors.append(f"{f}: whole source file differs from the pinned archive")
            cache[f] = raw.decode().splitlines()
        lines = cache[f]
        if b > len(lines) or hashlib.sha256("\n".join(lines[a-1:b]).encode()).hexdigest() != p["sha256"]:
            errors.append(f"{p['name']}: source lines {a}–{b} differ")
    from check_reading_prerequisites import verify
    verify(root)
    return errors
