"""Render the dashboard and track inventories from the unit records."""
from atlas_files import unit_files
import argparse
from collections import Counter
from pathlib import Path
import sys

from validate import BANNER, GRADES, ROOT, STATUSES, TRACKS, read


from atlas_labels import TRACK_NAMES as LABELS


def inventory(track, primary, secondary):
    lines = [
        f"# {LABELS[track]} · unit inventory", "", BANNER, "",
        f"[Track guide](README.md) · [Starter packet](../../notes/{track}/README.md) · "
        f"[Open questions](../../questions/{track}.md) · [Dashboard](../../dashboard/README.md)", "",
    ]
    for label, entries in [("Primary units", primary), ("Related units from other tracks", secondary)]:
        lines.extend([f"## {label} ({len(entries)})", "",
                      "| Unit | Title | Exposition | Grade | Reading material |", "|---|---|---|---|---|"])
        for unit in entries:
            uid = unit["id"]
            title = unit["title"].replace("|", r"\|").replace("\n", " ")
            docs = dict.fromkeys(e["document"] for e in unit["expositions"] if e["document"].startswith("notes/"))
            links = [f"[Extract {i}](../../{doc})" for i, doc in enumerate(docs, 1)]
            links.extend(f"[{Path(review).stem}](../../{review})" for review in unit["reviews"][:1])
            lines.append(f"| [{uid}](../../units/{uid}.md) | {title} | {unit['status']} | {unit['grade']} | "
                         f"{' · '.join(links) or 'See unit card'} |")
        lines.append("")
    return "\n".join(lines)


def documents(root):
    units = sorted((read(path) for path in unit_files(root)), key=lambda unit: unit["id"])
    lines = [
        "# Verification dashboard", "", BANNER, "",
        "Every unit appears once in the totals, under its primary track. The grade records the "
        "highest level supported for that unit and edition. The final three columns count the extent of "
        "the available human-readable exposition. A single declaration can appear in several units.", "",
        "| Primary track | Units | L0 | L1 | L2 | L3 | L4 · named human | Full | Outlined | Statement only |",
        "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|",
    ]
    results = {}
    groups = {key: [unit for unit in units if unit["track"]["primary"] == key] for key in TRACKS}
    for key, group in [*groups.items(), (None, units)]:
        grades = Counter(unit["grade"] for unit in group)
        statuses = Counter(unit["status"] for unit in group)
        name = f"[{LABELS[key]}](../tracks/{key}/README.md)" if key else "**All units**"
        row = [name, len(group), *(grades[grade] for grade in GRADES), *(statuses[s] for s in STATUSES)]
        lines.append("| " + " | ".join(map(str, row)) + " |")
        if key:
            secondary = [unit for unit in units if key in unit["track"]["secondary"]]
            results[root / "tracks" / key / "units.md"] = inventory(key, group, secondary)
    lines += ["", "“Full” means the exposition supplies a proof under its stated assumptions. "
              "Open questions, review scope and hypotheses appear on each unit card. "
              "[Status and evidence](../STATUS.md) · [Open questions](../questions/README.md)", ""]
    from snapshot import pipeline
    aggregate = pipeline(root)["counts"]
    total = aggregate["all"]
    lines[4:4] = [f"**{total['units']} units:** {total['full']} Full arguments under stated inputs, {total['outlined']} outlines and "
                  f"{total['statement_only']} statements only. **{total['written_steps']} active steps:** "
                  f"{total['ai_reviewed_steps']} with a step-specific AI review and {total['human_checked_steps']} with a human check.", ""]
    lines += ["## Six stages", "", "| Field | Lean pinned | Statement compared | In prose | In steps | AI-reviewed | Human-checked |",
              "|---|---:|---:|---:|---:|---:|---:|"]
    for key, row in [*aggregate["tracks"].items(), ("All", aggregate["all"])]:
        lines.append("| " + " | ".join([LABELS.get(key, key), *map(str, row["stages"])]) + " |")
    lines += ["", "[Cited Lean lines, checked steps and historical counts](../PROGRESS.md)", ""]
    results[root / "dashboard/README.md"] = "\n".join(lines)
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if a generated file differs")
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args()
    stale = []
    for path, content in documents(args.root).items():
        if args.check:
            if not path.is_file() or path.read_text(encoding="utf-8") != content:
                stale.append(str(path))
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")
    if stale:
        print("Stale generated files:\n" + "\n".join(stale), file=sys.stderr)
    return bool(stale)


if __name__ == "__main__":
    sys.exit(main())
