#!/usr/bin/env python3
"""Build the six-stage public progress ledger from checked-in evidence."""
import argparse
from collections import defaultdict
from datetime import date, datetime, timezone
import hashlib
import json
from pathlib import Path
from index_position import nearest_positions, supplier_weights, scope_text
from atlas_labels import TRACK_NAMES
from reading_coverage import KINDS, MEASURES, citations, cited_totals
import re

ROOT = Path(__file__).resolve().parents[1]
NOTICE = "AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved"
TRACKS = ("analytic", "arakelov", "formal", "galois", "ktheory", "local", "theta")
STAGES = ("Pinned", "Compared", "Written", "Steps", "AI review", "Human")
TOTAL = 9567045


def read(path):
    return json.loads(path.read_bytes())


def digest(data):
    return hashlib.sha256(data).hexdigest()


def statement_heads(unit):
    if "statement_declarations" in unit:
        return unit["statement_declarations"]
    if unit.get("kind") == "paper_composite":
        return []  # This paper theorem has no single matching Lean statement.
    if unit.get("kind") in {"pillar_component", "reading_composite"}:
        return [entry["name"] for entry in unit["lean"]]
    return [unit["lean"][0]["name"]]


def source_fingerprint(root, path):
    return digest((root / path).read_bytes())


def certificate(root, pins):
    cert = read(root / "progress/dominators.json")
    anchors = cert["anchors"]
    if (cert["graph_sha256"] != pins["graph_sha256"] or cert["source_commit"] != pins["source_commit"]
            or anchors["allChi"] != {"parent": None, "weight": TOTAL} or cert["total"] != TOTAL):
        raise ValueError("Dominator graph pin differs from the source inventory")
    expected = {n: p["dominated"] for n, p in pins["anchors"].items() if p["graph"] == "allChi"}
    if set(expected) != set(anchors):
        raise ValueError("Dominator certificate and pinned allChi anchor sets differ")
    if any(n not in anchors or anchors[n]["weight"] != v for n, v in expected.items()):
        raise ValueError("Dominator certificate weight differs from a source pin")
    children = defaultdict(list)
    for n, a in anchors.items():
        if n == "allChi":
            continue
        if a["parent"] not in anchors or type(a["weight"]) != int or a["weight"] < 0:
            raise ValueError("Invalid compressed dominator parent or weight: " + n)
        children[a["parent"]].append(n)
    visited = set()
    todo = ["allChi"]
    while todo:
        n = todo.pop()
        if n in visited or sum(anchors[c]["weight"] for c in children[n]) > anchors[n]["weight"]:
            raise ValueError("Invalid or overlapping dominator branches under " + n)
        visited.add(n)
        todo.extend(children[n])
    if visited != set(anchors):
        raise ValueError("Disconnected compressed dominator tree")
    return anchors


def edition_reviews(root, unit, manifest, old, recent):
    uid = unit["id"]
    archived = old.get(uid, {})
    compared = digest(unit["statement"].encode()) in archived.get("statement_sha256", [])
    proof = False
    reviewed_sources = set()
    prose = {e["document"] for e in unit["expositions"] if e["document"].startswith("notes/")}
    # Archived certificates cover the exact local excerpts which supported the original proof review.
    if unit.get("review_status") != "pending_review":
        for version in archived.get("proof_versions", []):
            files = version["sources"]
            if set(files) == prose and all(source_fingerprint(root, p) == h for p, h in files.items()):
                reviewed_sources.update(files)
                proof = True
                break

    records = recent.get(uid, [])
    current = {record["note"]: record for record in records if record.get("current_sha256")
               and (root / record["note"]).is_file()
               and source_fingerprint(root, record["note"]) == record["current_sha256"]}
    statement_hash = digest(unit["statement"].encode())
    compared |= any(record.get("statement_compared") and record.get("statement_sha256") == statement_hash
                    for record in current.values())
    if current:
        # Current prose may contain separate partial notes. Every current proof note must be covered.
        active = {p for p in prose if p.endswith(".md") and p.startswith("notes/units/")}
        if manifest:
            active.update(s["path"] for s in manifest["sources"]
                          if s["path"].startswith("notes/units/") and s["path"].endswith(".md"))
        def covered(record):
            return (record.get("accepted_whole_note") or
                    (record.get("reviewed_sha256") == record.get("current_sha256")
                     and record.get("original_verdict") in {"CONFIRMED", "FAITHFUL OUTLINE"}))
        reviewed_sources.update(path for path, rec in current.items() if covered(rec)
                                and rec["reviewed_sha256"] == rec["current_sha256"])
        proof |= bool(active) and active <= current.keys() and all(covered(current[p]) for p in active)
    return bool(compared), bool(proof), reviewed_sources


def pipeline(root=ROOT):
    root = Path(root)
    pins = read(root / "data/pins.json")
    anchors = certificate(root, pins)
    from source_inventory import load_inventory
    inventory = load_inventory(root)
    if inventory["source_commit"] != pins["source_commit"] or inventory["weighted_core_lines"] != TOTAL:
        raise ValueError("Coverage denominators and unit pins refer to different sources")
    old = read(root / "progress/legacy_reviews.json")["units"]
    ledger = read(root / "data/grade_evidence.json")
    # Check the archived evidence against the contemporaneous record, allowing a
    # grouped unit to use the specific declaration targets covered by each entry.
    index = defaultdict(set)
    for item in ledger["records"]:
        key = (item["review"], tuple(item["lines"]), item["verdict"])
        index[key].update(item["declarations"])
    for entry in old.values():
        for row in [*entry["statement_evidence"], *(r for version in entry["proof_versions"] for r in version["evidence"])]:
            key = (row["review"], tuple(row["lines"]), row["verdict"])
            if not set(row["targets"]).issubset(index[key]) or not (root/row["review"]).is_file():
                raise ValueError("Unmatched archived review evidence: " + row["review"])
    recent = defaultdict(list)
    for record in ledger.get("round3_note_reviews", []):
        recent[record["unit"]].append(record)
    comparisons = read(root/"data/statement_comparisons.json")
    if comparisons["source_commit"] != pins["source_commit"]:
        raise ValueError("Supplemental statement comparisons use another source edition")
    current_statements = {}
    for record in comparisons["records"]:
        uid = record["unit"]
        pin = pins["anchors"].get(record["declaration"])
        if uid in current_statements or not pin or record["result"] != "statement compared" or not record["scope"]:
            raise ValueError("Incomplete or duplicate statement comparison for " + uid)
        if [record["file"],record["line0"],record["line1"],record["lean_sha256"]] != [pin[k] for k in ("file","line0","line1","sha256")]:
            raise ValueError("Statement comparison source differs for " + uid)
        lo, hi = record["published_review_lines"]
        review = (root/record["original_review"]).read_text().splitlines()
        if not 1 <= lo <= hi <= len(review) or record["declaration"].rsplit(".",1)[-1] not in "\n".join(review[lo-1:hi]):
            raise ValueError("Earlier statement-comparison locator differs for " + uid)
        current_statements[uid] = record
    units = {}
    from signoff_records import human_state, load_records
    from proof_steps import build
    human_records = load_records(root)
    for path in sorted((root / "units").glob("*.yaml")):
        if path.name.endswith(".steps.yaml"):
            continue
        u = read(path)
        uid = u["id"]
        stage1 = bool(u["lean"]) and all(pins["anchors"].get(a["name"], {}).get("sha256") == a["sha256"] for a in u["lean"])
        written = u["status"] in ("Full", "Outlined")
        step_path = root / "units" / (uid + ".steps.yaml")
        manifest = read(step_path) if step_path.is_file() else {}
        if manifest:
            observed = build(root, uid, [src["path"] for src in manifest["sources"]], manifest["steps"])
            if any(manifest.get(key) != value for key, value in observed.items()):
                raise ValueError(f"{uid}: citations do not match the current prose and step edition")
        steps = [s for s in manifest.get("steps", []) if s["status"] == "active"]
        ai_steps = sum(bool(s.get("ai_review")) for s in steps)
        st2, st5, reviewed_sources = edition_reviews(root, u, manifest, old, recent)
        supplemental = current_statements.get(uid)
        if supplemental:
            if (supplemental["statement_sha256"] != digest(u["statement"].encode())
                    or supplemental["declaration"] not in statement_heads(u)):
                raise ValueError("Current statement differs from the registered comparison: " + uid)
            st2 = True
        state = human_state(root, uid, manifest, human_records) if manifest else {}
        checked = sum(s["state"] == "human-checked" for s in state.get("steps", {}).values())
        full_human = bool(state.get("l4"))
        st5 = written and (st5 or (bool(steps) and ai_steps == len(steps)))
        units[uid] = dict(stages=[stage1, st2 or bool(state.get("statement_checked")), written,
                                  bool(steps), st5, full_human],
                          written_steps=len(steps), ai_reviewed_steps=ai_steps, human_checked_steps=checked,
                          disputed_steps=sum(s["state"] == "disputed" for s in state.get("steps", {}).values()),
                          independent_steps=sum(bool(s.get("independent_pair")) for s in state.get("steps", {}).values()),
                          two_independent=bool(state.get("two_independent")),
                          track=u["track"]["primary"], status=u["status"], heads=statement_heads(u),
                          citations=citations(u, manifest, state, reviewed_sources),
                          uid=uid, grade=u["grade"], l4_evidence=state.get("l4_evidence", {
                              "reader_count": 0, "includes_maintainer": False, "ai_assistance_levels": []}))
    if current_statements.keys() - units.keys():
        raise ValueError("Statement comparison refers to an unknown unit")
    def aggregate(rows):
        return dict(units=len(rows), stages=[sum(row["stages"][i] for row in rows) for i in range(6)],
                    full=sum(row["status"] == "Full" for row in rows),
                    outlined=sum(row["status"] == "Outlined" for row in rows),
                    independent_units=sum(row["two_independent"] for row in rows),
                    statement_only=sum(row["status"] == "Statement only" for row in rows),
                    **{key: sum(row[key] for row in rows) for key in
                       ("written_steps", "ai_reviewed_steps", "human_checked_steps", "disputed_steps", "independent_steps")},
                    cited_lines=cited_totals(rows, inventory))
    groups = {t: aggregate([r for r in units.values() if r["track"] == t]) for t in TRACKS}
    denominators = dict(weighted_core_lines=TOTAL, raw_files=inventory["file_count"], raw_lines=inventory["raw_lines"],
                        source_files=inventory["source_files"], source_lines=inventory["source_lines"])
    return dict(units=units, counts=dict(denominators=denominators, all=aggregate(list(units.values())), tracks=groups),
                index_position=nearest_positions(units, anchors), suppliers=supplier_weights(units, anchors))


def snapshot_digest(row):
    payload = {key: row[key] for key in ("label", "date", "counts")}
    return digest(json.dumps(payload, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode())


def validate_counts(counts, inventory):
    expected_den = dict(weighted_core_lines=TOTAL, raw_files=inventory["file_count"], raw_lines=inventory["raw_lines"],
                        source_files=inventory["source_files"], source_lines=inventory["source_lines"])
    if set(counts) != {"denominators", "all", "tracks"} or counts["denominators"] != expected_den or set(counts["tracks"]) != set(TRACKS):
        raise ValueError("Historical coverage has unknown fields, denominator, or tracks")
    ceiling = inventory["raw_lines"] + sum(meta["lines"] for meta in inventory["outside_files"].values())
    for loc, row in [("all", counts["all"]), *counts["tracks"].items()]:
        keys = {"units", "stages", "full", "outlined", "independent_units", "statement_only", "written_steps", "ai_reviewed_steps",
                "human_checked_steps", "disputed_steps", "independent_steps", "cited_lines"}
        if set(row) != keys or set(row["cited_lines"]) != set(KINDS):
            raise ValueError("Unknown historical headline (obsolete graph-cone fields are forbidden): " + loc)
        pool = row["cited_lines"]
        for kind, values in pool.items():
            if set(values) != set(MEASURES) or any(type(v) is not int or v < 0 for v in values.values()):
                raise ValueError("Invalid historical line metric for " + loc + "/" + kind)
            if (values["all_files"] > ceiling or values["in_raw_files"] > min(values["all_files"], inventory["raw_lines"])
                    or values["in_weighted_core"] > values["all_files"] or values["weighted_core_weight"] < values["in_weighted_core"]
                    or values["weighted_core_weight"] > TOTAL
                    or not inventory["core_overlaps"] and values["weighted_core_weight"] != values["in_weighted_core"]
                    or not row["written_steps"] and any(values.values())
                    or kind == "ai_reviewed" and not row["ai_reviewed_steps"] and any(values.values())
                    or kind == "human_checked" and not row["human_checked_steps"] and any(values.values())):
                raise ValueError("Historical line count exceeds its source or step evidence: " + loc + "/" + kind)
        for key in MEASURES:
            all_value = pool["written"][key]
            if any(x[key] > all_value for x in pool.values()) or all_value > pool["full"][key] + pool["outlined"][key]:
                raise ValueError("Historical coverage is not a possible citation union")


def headline_guard(root):
    """Detect the retired cone as a reading percentage on live entry pages, including rendered HTML."""
    from html import unescape
    sources = ["README.md", "README.ko.md", "STATUS.md", "PROGRESS.md", "dashboard/README.md",
               "progress/README.md", "progress/by-field.md", "docs/ko/README.md", "docs/ko/STATUS.md"]
    # Check the corresponding published pages in both languages.
    targets = [root/p for p in sources]
    targets += [root/"site"/p for p in ("index.html", "README.ko.html", "STATUS.html", "PROGRESS.html",
               "dashboard/index.html", "progress/index.html", "progress/by-field.html", "docs/ko/index.html", "docs/ko/STATUS.html")]
    for path in targets:
        if not path.is_file():
            continue
        raw = path.read_text(encoding="utf-8")
        text = re.sub(r"<[^>]+>", " ", raw)
        text = re.sub(r"[, *_`]", "", unescape(text))
        # The exact graph total may legitimately identify the denominator beside a small fraction.
        obsolete = r"(?:9567045\s*\(\s*100(?:\.0+)?\s*%|197509\s*\(\s*2\.0[67]\s*%|7383745\s*\(\s*77\.18\s*%)"
        retired = r"(?:9567045|7383745|197509)"
        reading_label = r"(?:written|AI.reviewed|in prose|stages? [356]|작성|AI 검토)"
        bare_value = re.search(reading_label + r"\s*(?:[·-]\s*stage [356]\s*)?[:|=→–-]\s*" + retired + r"(?!\d)", text, re.I)
        table_value = re.search(r"\|\s*" + retired + r"\s*\|", text)
        html_value = re.search(r"<td[^>]*>\s*" + retired + r"\s*</td>", raw.replace(",", ""), re.I)
        if re.search(obsolete, text, re.I) or bare_value or table_value or html_value:
            raise ValueError("Retired graph-footprint percentage on a reading page: " + path.relative_to(root).as_posix())
        if re.search(r"(?:written|outlined|human.checked|AI.reviewed|stage [356])[^|]{0,55}\b(?:100(?:\.0+)?|2\.06)\s*%\s*(?:of (?:the )?(?:proof|source|lines)|complete|coverage)", text, re.I):
            raise ValueError("A reading headline attributes an old graph percentage to proof completion")


def read_history(root):
    path = root / "progress/history.jsonl"
    rows = [json.loads(line) for line in path.read_text().splitlines() if line.strip()] if path.exists() else []
    from source_inventory import load_inventory
    inventory = load_inventory(root)
    seen = set()
    for row in rows:
        if set(row) != {"label", "date", "counts", "snapshot_sha256"} or row["label"] in seen:
            raise ValueError("Unrecognized or repeated historical snapshot")
        validate_counts(row["counts"], inventory)
        date.fromisoformat(row["date"])
        if snapshot_digest(row) != row["snapshot_sha256"]:
            raise ValueError("Snapshot content digest differs from its registered value")
        seen.add(row["label"])
    return rows


def history_chart(rows):
    # Both lines are unit counts; axes use a shared scale.
    w, h, left, right, top, bottom = 720, 240, 58, 27, 18, 47
    last = len(rows) - 1
    peak = max([1, *(max(r["counts"]["all"]["stages"][2],r["counts"]["all"]["stages"][5]) for r in rows)])
    ceiling = max(25, 25 * ((peak + 24) // 25))
    def xx(i):
        return left + i * (w-left-right) / max(last, 1)
    def yy(n):
        return top + (ceiling-n) / ceiling * (h-top-bottom)
    segments = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc">',
                '<title id="title">Units with written arguments and units fully human-checked</title>',
                '<desc id="desc">Counts by snapshot in chronological order. Exact values appear in the adjacent history table.</desc>',
                '<rect width="100%" height="100%" fill="white"/>','<g font-family="sans-serif" font-size="13" fill="#172b38">']
    for value in sorted({0, ceiling//2, ceiling}):
        y=yy(value)
        segments.extend([f'<path d="M{left},{y:.1f} H{w-right}" stroke="#cbd5db"/>',
                         f'<text x="{left-8}" y="{y+5:.1f}" text-anchor="end">{value}</text>'])
    for i in range(len(rows)):
        if i in (0,last) or len(rows)<=14:
            segments.append(f'<text x="{xx(i):.1f}" y="{h-23}" text-anchor="middle">{i+1}</text>')
    for j,color in [(2,"#185d85"),(5,"#913d18")]:
        points=" ".join(f"{xx(i):.1f},{yy(r['counts']['all']['stages'][j]):.1f}" for i,r in enumerate(rows))
        segments.append(f'<polyline fill="none" stroke="{color}" stroke-width="3" points="{points}"/>')
        for i,r in enumerate(rows):
            segments.append(f'<circle cx="{xx(i):.1f}" cy="{yy(r["counts"]["all"]["stages"][j]):.1f}" r="3.5" fill="{color}"/>')
    return "\n".join(segments+['</g></svg>',''])


LINE_NOTICE = ("A cited line locates a written step in the pinned Lean source and by itself establishes "
               "neither a line-by-line check nor a complete proof.")
LABELS = {"written": "Any written unit", "full": "Full", "outlined": "Outlined",
          "ai_reviewed": "Current AI review of the specific step",
          "ai_reviewed_prose": "Current AI review of the containing prose",
          "human_checked": "Current human check of the specific step"}


def table(lines, headers, rows):
    lines.append("| " + " | ".join(headers) + " |")
    lines.append("|---" + "|---:" * (len(headers) - 1) + "|")
    for row in rows:
        lines.append("| " + " | ".join(map(str, row)) + " |")
    lines.append("")


def share(value, total):
    return f"{value:,} ({value / total:.4%})"


def coverage_table(lines, counts, denominators):
    weighted = denominators["weighted_core_lines"]
    raw = denominators["raw_lines"]
    physical = denominators["source_lines"]
    table(lines, ["Evidence or exposition", f"Distinct cited lines / {physical:,} full-source lines",
                  f"Within {weighted:,} core lines", f"Within {raw:,} lines of the original file sample"],
          ([LABELS[k], share(v["all_files"], physical), share(v["weighted_core_weight"], weighted), share(v["in_raw_files"], raw)]
           for k, v in counts["cited_lines"].items()))


def render(root, data, rows):
    counts = data["counts"]
    all_units = counts["all"]
    den = counts["denominators"]
    cited = all_units["cited_lines"]
    written = cited["written"]
    shared = cited["full"]["all_files"] + cited["outlined"]["all_files"] - written["all_files"]
    groups = [("**All**", all_units)] + [(f"[{t}](tracks/{t}/README.md)", counts["tracks"][t]) for t in TRACKS]
    lines = ["# Writing and reading progress", "", NOTICE, "",
             f"Of {all_units['units']} units, **{all_units['full']} have a Full argument under stated inputs**, "
             f"**{all_units['outlined']} have an outline**, and **{all_units['statement_only']} give the statement only**.", "",
             f"The notes contain **{all_units['written_steps']} active proof steps**. "
             f"**{all_units['ai_reviewed_steps']}** have a current step-specific AI review. "
             f"**{all_units['human_checked_steps']}** have a current human check.", "",
             "## Source lines cited by active steps", "", LINE_NOTICE, "",
             f"The steps cite **{written['all_files']:,} distinct physical lines**. "
             f"Of these, {written['in_weighted_core']:,} are in the dependency graph of the all-character statement `allChi`. "
             f"The original {den['raw_files']} indexed files contain {written['in_raw_files']:,} of the cited lines. "
             f"The remaining {written['all_files'] - written['in_raw_files']:,} appear in other files at the same Lean commit.", ""]
    coverage_table(lines, all_units, den)
    lines.extend([f"Full and Outlined notes cite {shared:,} of the same physical lines. "
                  "The first row takes their union. The two AI rows distinguish a verdict on the named step from a review of its enclosing prose. "
                  "A whole-note review does not supply a verdict on a step added later. Each evidence row counts its own union.", "",
                  "## Position in the declaration index", "",
                  "This table shows where a line sits in the index. It gives no evidence that the line was explained or read.", ""])
    index = data["index_position"]
    table(lines, ["Writing status of nearest indexed statement", "Core lines at this index position"],
          [(status, share(n, den["weighted_core_lines"])) for status,n in index["status"].items()]
          + [("Of Full, also at evidence level L2", share(index["full_l2"], den["weighted_core_lines"]))])
    lines.extend([f"Each line belongs to the nearest indexed unit statement at or above it in the dominator tree. "
                  f"{index['shared_heads']} statement declarations have more than one primary unit. "
                  "For a shared statement, the earliest unit ID in ordinary character order owns the position. "
                  "This deterministic tie-break ignores grades. The Full-and-L2 row is part of Full.", ""])
    shared = next((a for a in index["heads"] if {"P034", "Z2.K4"} <= set(a["primary_units"])), None)
    if shared:
        lines.extend([f"For example, P034 and Z2.K4 share the head `{shared['name'].rsplit('.',1)[-1]}`. "
                      f"The tie rule assigns its {shared['weight']:,} lines to {shared['owner']}. "
                      "Choosing the other card would move those positions between the two writing-status rows without changing a single note.", ""])
    for sentence in scope_text(den, data["suppliers"]):
        lines.extend([sentence, ""])
    lines.extend(["[Per-field citation unions](progress/by-field.md) · [Counting rules](progress/README.md) · "
                  "[Reproduce the index assignment](progress/index_position.json)", "",
                  "## Units with evidence at each stage", "",
                  "The first two stages concern the unit’s statement. Written includes Full arguments and Outlined derivations. "
                  "A human check of a whole unit requires a positive current record for every active step and the statement comparison.", ""])
    table(lines, ["Primary field", "Units", "1 · Pinned", "2 · Compared", "3 · Written", "4 · Steps", "5 · AI review", "6 · Human"],
          ([name, row["units"], *row["stages"]] for name, row in groups))
    lines.extend(["## Checks on individual steps", ""])
    table(lines, ["Primary field", "Active steps", "AI-reviewed steps", "Human-checked steps", "Steps with two independent readers",
                  "Units with two independent readers", "Disputed"],
          ([name, *(row[k] for k in ("written_steps", "ai_reviewed_steps", "human_checked_steps", "independent_steps", "independent_units", "disputed_steps"))]
           for name, row in groups))
    proof_grade = {uid for uid, unit in data["units"].items() if unit["grade"] == "L2"}
    all_prose = {uid for uid, unit in data["units"].items() if unit["stages"][4]}
    def linked(ids):
        return ", ".join(f"[{uid}](units/{uid}.md)" for uid in sorted(ids)) or "none"
    lines.extend([f"Among {len(proof_grade)} units at L2 and {len(all_prose)} at stage 5, "
                  f"L2 without stage 5: {linked(proof_grade-all_prose)}. Stage 5 without L2: {linked(all_prose-proof_grade)}.", ""])
    if "D014" in proof_grade-all_prose:
        lines.extend(["D014’s L2 concerns one written proof. Its separate companion note has no current whole-note review.", ""])
    if "D550" in all_prose-proof_grade:
        lines.extend(["D550’s current individual checkpoints have scoped AI reviews. The light check does not approve its entire argument at L2.", ""])
    outlines = (all_prose-proof_grade) & {uid for uid,u in data["units"].items() if u["status"]=="Outlined"}
    if outlines:
        lines.extend([f"The AI evidence for these outline units concerns outline fidelity: {linked(outlines)}.", ""])
    lines.extend(["Stage 2 uses a recorded comparison of the named statement, including earlier comparisons of the same transcription. "
                  "Stage 5 accepts an edition-matched review of the written argument or a review of every active step. "
                  "An earlier unit-level review remains unit-level. A proof can have a review before it has a step checklist.", "",
                  "## Recorded history", "",
                  "Blue shows units with written arguments. Rust shows units with a complete human check for the recorded edition. "
                  "The horizontal axis numbers the snapshots. The source-line column uses the checklist available in each round.", "",
                  "![Written and human-checked units through the recorded snapshots](progress/history.svg)", ""])
    table(lines, ["Snapshot", "Date (UTC)", "Units", "Compared", "Written", "With steps", "AI review", "Human", "Distinct lines cited"],
          ([f"{i} · {r['label']}", r["date"], r["counts"]["all"]["units"], *r["counts"]["all"]["stages"][1:],
            f"{r['counts']['all']['cited_lines']['written']['all_files']:,}"]
           for i, r in enumerate(rows, 1)))
    lines.extend(["The early records summarize editorial editions predating the public release. Their identifiers are digests of the recorded counts. "
                  "The first three editions contain prose but predate step checklists. Zero cited lines there means zero recorded step citations.", "",
                  "Round 6 counted only reviews covering the current argument, reducing the unit count from 26 to 20, and set aside earlier verdicts on D014 S7 and D548 S2–S3, reducing the number of steps with a specific review from 9 to 6.", "",
                  "[Machine-readable history](progress/history.jsonl) · [Dashboard](dashboard/README.md) · "
                  "[Submit a human check](signoffs/README.md)", ""])
    fields = ["# Source lines cited by field", "", NOTICE, "", LINE_NOTICE, "",
              "Each field includes units whose primary subject is that field. Within a row, count each physical line once, "
              "even when several notes cite it. The core column uses the pinned declaration weights. "
              f"The raw-file column counts only citations in the original {den['raw_files']} complete source files. "
              "A line can occur in several fields, so adding field totals can count it twice.", ""]
    for track in TRACKS:
        row = counts["tracks"][track]
        fields.extend([f"## {TRACK_NAMES[track]}", ""])
        coverage_table(fields, row, den)
    fields.extend(["[Project-wide unions and definitions](../PROGRESS.md)", ""])
    source_lines = ["# What the source counts measure", "", NOTICE, "",
                    "The atlas counts each reading unit once, under its primary field. Its writing status concerns the argument available under stated inputs. "
                    "Its evidence level belongs to the edition and statement named on its card.", ""]
    for paragraph in scope_text(den, data["suppliers"]):
        source_lines.extend([paragraph, ""])
    table(source_lines, ["Role in the conditional deduction", "Source statement", "Dominated core lines"],
          ([name, f"[{uid}](../units/{uid}.md)", f"{data['suppliers'][uid]:,}"] for uid,name in [
              ("P013","V, the uniform Selmer window"), ("T02","F, one definite-side record with a closed link"),
              ("D575","Green’s finite-field character input"), ("P017","List A, host character and error bounds"),
              ("B07","List B, the auxiliary pair and host"), ("B05","List C, a common design and closed comparisons")]))
    source_lines.extend(["The table locates the six statements in the graph. A dominated weight gives no count of prose, source lines cited or human checks. "
                         "The figure for a list is the enclosing unit’s weight. [Source-line citations and index positions](../PROGRESS.md) · "
                         "[Input lists and exact declarations](../MAP.md) · [AI review of the conditional reduction](../reviews/R23_review.md)", ""])
    return {root/"PROGRESS.md": "\n".join(lines), root/"progress/by-field.md": "\n".join(fields),
            root/"sources/coverage.md": "\n".join(source_lines),
            root/"progress/index_position.json": json.dumps(index, ensure_ascii=False, indent=2)+"\n",
            root/"progress/history.svg": history_chart(rows)}


def append(root, label, counts, rows, as_of=None):
    label = label or "Update " + str(len(rows)+1)
    if rows and rows[-1]["counts"] == counts and rows[-1]["label"] == label:
        return rows
    if any(row["label"] == label for row in rows):
        raise ValueError("Each recorded edition needs a distinct label")
    stamp = date.fromisoformat(as_of) if as_of else datetime.now(timezone.utc).date()
    row = dict(label=label, date=stamp.isoformat(), counts=counts)
    row["snapshot_sha256"] = snapshot_digest(row)
    with (root/"progress/history.jsonl").open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False, separators=(",", ":"))+"\n")
    return rows+[row]


def check(root=ROOT):
    try:
        root=Path(root)
        data=pipeline(root)
        stale_grades = [uid for uid, row in data["units"].items()
                        if row["grade"] in {"L1", "L2"} and not row["stages"][1]]
        if stale_grades:
            raise ValueError("Statement evidence needs a comparison for the current transcription: " + ", ".join(stale_grades))
        rows=read_history(root)
        headline_guard(root)
        if not rows or rows[-1]["counts"] != data["counts"]:
            raise ValueError("Latest progress snapshot differs from current counters")
        for path, content in render(root,data,rows).items():
            if not path.is_file() or path.read_text() != content:
                raise ValueError("Regenerate "+path.name)
    except (ValueError, OSError, KeyError, TypeError) as exc:
        return [str(exc)]
    return []


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root",type=Path,default=ROOT)
    ops=parser.add_mutually_exclusive_group(required=True)
    for flag in ("--check","--render","--append","--counts"):
        ops.add_argument(flag,action="store_true")
    parser.add_argument("--date", help="UTC edition date (YYYY-MM-DD); defaults to the current UTC date")
    parser.add_argument("--round",dest="label")
    args=parser.parse_args()
    if args.check:
        errors=check(args.root)
        if errors:
            raise SystemExit("\n".join(errors))
        return
    data=pipeline(args.root)
    if args.counts:
        print(json.dumps(data["counts"],indent=2))
        return
    rows=read_history(args.root)
    if args.append:
        rows=append(args.root,args.label,data["counts"],rows,args.date)
    for path,content in render(args.root,data,rows).items():
        path.write_text(content,encoding="utf-8")


if __name__ == "__main__":
    main()
