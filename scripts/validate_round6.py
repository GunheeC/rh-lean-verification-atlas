"""Verify the current public corrections, their source intervals and edition-specific checks."""
import hashlib
import json
from pathlib import Path
import re


def check(root, units, lean_src=None):
    ledger = json.loads((root / "data/round6_review_corrections.json").read_bytes())
    errors = []
    ids = [row["id"] for row in ledger["dispositions"]]
    expected = ({f"C-V{i}" for i in range(1, 9)} | {f"C-F{i}" for i in range(1, 10)}
                | {f"D{i}" for i in range(1, 14)} | {f"E{i}" for i in range(1, 21)}
                | {f"N{i}" for i in range(1, 14)})
    if expected - set(ids) or len(set(ids)) != len(ids):
        errors.append("Missing or duplicate numbered review disposition")
    for row in ledger["dispositions"]:
        if row["status"] not in {"applied", "applied with correction", "rejected with evidence", "not done"} or not row.get("decision") or not row.get("evidence"):
            errors.append(f"{row['id']}: incomplete disposition")
    from snapshot import pipeline
    metrics = pipeline(root)["counts"]["all"]
    current = {"stages": metrics["stages"], "steps": metrics["written_steps"],
               "ai_steps": metrics["ai_reviewed_steps"], "human_steps": metrics["human_checked_steps"]}
    if ledger.get("current_counts") != current or ledger["source_census"]["cited"] != metrics["cited_lines"]:
        errors.append("Review dispositions and live evidence counts differ")
    for p, ed in ledger["note_editions"].items():
        file = root / p
        if (not file.is_file() or not file.resolve().is_relative_to((root / "notes").resolve())
                or hashlib.sha256(file.read_bytes()).hexdigest() != ed["sha256"]):
            errors.append(f"{p}: current note digest differs")
    graph = json.loads((root / "progress/position_graph.json").read_bytes())
    pins = json.loads((root / "data/pins.json").read_bytes())
    nodes = graph["named_nodes"]
    index_bytes = json.dumps(nodes, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
    registered = {name for name, pin in pins["anchors"].items()
                  if pin["graph"] == "allChi" and pin["dominated"] is not None}
    if (graph["source_graph_sha256"] != pins["graph_sha256"]
            or graph["sha256"] != "d28c467b46f5039ae24bb26072bfa49c61bc0a0e6b54ca951df668ddc33371f8"
            or (graph["nodes"], graph["edges"]) != (1_155_391, 12_997_137)
            or set(nodes) != registered or len(nodes) != len(set(nodes.values()))
            or hashlib.sha256(index_bytes).hexdigest() != "d254ed2d6575c721b4d1864c98e72e9293cafdc2d80f617aa7bd92b6ccb0d00c"
            or nodes.get("allChi") != graph["root"]
            or any(not isinstance(i, int) or not 0 <= i < graph["nodes"] for i in nodes.values())):
        errors.append("Optional graph identity or declaration index differs from the pinned extraction")
    inspected = ledger["outlines"]["sampled"] + ledger["outlines"]["other"]
    expected_units = {p.name.split("_")[0] for p in (root / "notes/units").glob("*_round4.md")}
    if (len(ledger["outlines"]["sampled"]) != 21 or len(ledger["outlines"]["other"]) != 42
            or set(inspected) != expected_units):
        errors.append("Incomplete 21 + 42 outline census")
    for uid in inspected:
        path = root / "notes/units" / (uid + "_round4.md")
        card = root / "units" / (uid + ".md")
        for f in (path, card):
            body = f.read_text() if f.exists() else ""
            if ("First-pass outline of the head proof term" not in body or
                    "this note describes what the top-level term calls; it does not explain the dependency cone beneath it" not in body or
                    (uid in {"T01", "T08"} and "top-level map only" not in body)):
                errors.append(f"{f.name}: missing statement of scope")
    source_lines = {}
    for p in ledger["citations"]:
        file, start, end = p["file"], p["line0"], p["line1"]
        if (Path(file).is_absolute() or ".." in Path(file).parts or not end >= start > 0
                or not re.fullmatch(r"[0-9a-f]{64}", p["sha256"])):
            errors.append(f"{file}: invalid correction source")
            continue
        if lean_src:
            if file not in source_lines:
                source_lines[file] = (lean_src / file).read_text().splitlines()
            lines = source_lines[file]
            digest = hashlib.sha256("\n".join(lines[start-1:end]).encode()).hexdigest()
            if end > len(lines) or digest != p["sha256"]:
                errors.append(f"{file}:{start}-{end}: correction cites a different source")
    for uid, unit in units.items():
        if unit["grade"] == "L4" and unit["status"] != "Full":
            errors.append(f"{uid}: L4 requires a Full unit")
    return errors
