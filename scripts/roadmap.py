#!/usr/bin/env python3
"""Regenerate the writing queue and volunteer reading queue from the current atlas."""
import argparse
import json
from pathlib import Path
import re
from snapshot import statement_heads
from signoff_records import human_state, load_records

ROOT = Path(__file__).resolve().parents[1]
NOTICE = "AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved"
START = "<!-- roadmap:volunteers:start -->"
END = "<!-- roadmap:volunteers:end -->"
UNIT_LINK = re.compile(r"\]\((?:\.\./)+units/([^/#)]+)\.md\)")


def read(path):
    return json.loads(path.read_text())


def route_members(root):
    routes = set()
    for path in (root / "tracks").glob("*/README.md"):
        passage = re.search(r"^## Reading path\s*(.*?)(?=^## (?!#)|\Z)", path.read_text(), re.M | re.S)
        if passage:
            routes.update(UNIT_LINK.findall(passage[1]))
    pillars = set()
    for path in (root / "pillars").glob("*.md"):
        in_level = False
        for line in path.read_text().splitlines():
            if line.startswith("#"):
                in_level = bool(re.match(r"### Level [12] ", line))
            if (in_level and line.startswith("|")) or re.match(r"\|\s*[12](?:\s*[/.·]|\s*\|)", line):
                pillars.update(UNIT_LINK.findall(line))
    return routes, pillars


def size(unit):
    heads = statement_heads(unit)
    pins = [row for row in unit["lean"] if row["name"] in heads]
    measured = [row for row in pins if isinstance(row.get("dominated"), int)]
    if not measured:
        return None, None
    largest = max(measured, key=lambda row: row["dominated"])
    return largest["dominated"], largest.get("graph", "allChi")


def queues(root):
    units = [read(p) for p in (root / "units").glob("*.yaml") if not p.name.endswith(".steps.yaml")]
    primary, pillars = route_members(root)
    writing, reading = [], []
    records = load_records(root)
    for unit in units:
        uid = unit["id"]
        lines, graph = size(unit)
        group = 0 if uid in primary else 1 if uid in pillars else 2
        if unit["status"] != "Full":
            writing.append(dict(id=uid, title=unit["title"], status=unit["status"], group=group, lines=lines, graph=graph))
        manifest = root / "units" / f"{uid}.steps.yaml"
        if not manifest.exists():
            continue
        mf = read(manifest)
        state = human_state(root, uid, mf, records)
        active = [s for s in mf["steps"] if s["status"] != "withdrawn"]
        if not active or state["l4"]:
            continue
        checked = sum(state["steps"][s["id"]]["state"] == "human-checked" for s in active)
        disputed = sum(state["steps"][s["id"]]["state"] == "disputed" for s in active)
        pages = unit.get("size_pages")
        reading.append(dict(id=uid, title=unit["title"], track=unit["track"]["primary"],
                            steps=len(active), pages=pages, prerequisites=len(unit["prerequisites"]),
                            checked=checked, disputed=disputed, statement_checked=state["statement_checked"]))
    writing.sort(key=lambda r: (r["status"] != "Statement only", r["group"], r["lines"] is None, -(r["lines"] or 0), r["id"]))
    reading.sort(key=lambda r: (r["steps"], r["pages"] is None, r["pages"] or 0, r["prerequisites"], r["id"]))
    return writing[:40], reading


def render(root):
    writing, reading = queues(root)
    reasons = ("track reading path", "V/F level 1 or 2", "dominated source size")
    guide = ["# Writing queue and volunteer reading opportunities", "", NOTICE, "",
             "[What is covered and what readers can check](docs/coverage.md)", "",
             "## Next writing assignments", "",
             "Statement-only units come first. Within this group, priority goes to the published track routes, then to either pillar’s first two levels, then to the remaining units. Each group runs from largest to smallest measured source size. If fewer than 40 statements remain, the same order fills the list with outlines to extend. The size is the largest dominated core-line count among the unit’s named statement pins in its recorded graph. Counts from different rows can overlap. A dash means the measurement is unavailable.", "",
             "| Order | Unit | Next writing task | Priority | Core lines · graph |", "|---:|---|---|---|---:|"]
    for i, row in enumerate(writing, 1):
        lines = "—" if row["lines"] is None else f'{row["lines"]:,} · {row["graph"]}'
        task = "First outline" if row["status"] == "Statement only" else "Extend outline"
        guide.append(f'| {i} | [{row["id"]} · {row["title"]}](units/{row["id"]}.md) | {task} | {reasons[row["group"]]} | {lines} |')
    guide += ["", "## Units waiting for a human reader", "",
              "Choose a checklist, follow the cited passages, and record the steps you actually read. Rows are sorted by active step count, then known note length, then number of direct unit prerequisites. An unmeasured length sorts after known lengths with the same step count. These measures describe the size of the reading assignment. They do not measure mathematical difficulty. Partial and disputed units remain available. [Record a check](signoffs/README.md)", "",
              "| Unit checklist | Field | Steps | Pages | Direct prerequisites | Current checks |", "|---|---|---:|---:|---:|---|"]
    for r in reading:
        detail = f'{r["checked"]}/{r["steps"]} steps'
        if r["disputed"]:
            detail += f' · {r["disputed"]} disputed'
        if r["statement_checked"]:
            detail += ' · statement checked'
        guide.append(f'| [{r["id"]} · {r["title"]}](units/{r["id"]}.check.md) | {r["track"]} | {r["steps"]} | {r["pages"] or "—"} | {r["prerequisites"]} | {detail} |')
    guide += ["", "## Correcting or retiring a unit", "", "Report the unit ID, edition digest, step ID and a source interval or counterexample through the contribution form. The maintainer records the disposition and publishes the corrected edition. An inserted step takes a new suffix; a removed step keeps its ID with status `withdrawn`. A contradictory or negative record stays in the ledger with its edition. The new checklist distinguishes current and superseded records. A replacement unit or retired claim should be identified in the change log, with a link to the earlier record and the reason. [Contribution route](CONTRIBUTING.md) · [Check records](signoffs/README.md) · [Change log](CHANGELOG.md)", ""]
    top = [START, "### Ten short checklists awaiting readers", "", "Sorted by steps, note length and prerequisites. [Full volunteer queue and writing plan](ROADMAP.md)", ""]
    for i,r in enumerate(reading[:10], 1):
        pages = f' · {r["pages"]} pp.' if r["pages"] else ""
        top.append(f'{i}. [{r["id"]} · {r["title"]}](units/{r["id"]}.check.md) · {r["steps"]} steps{pages}')
    top.extend(["", END])
    readme = (root / "README.md").read_text()
    block = "\n".join(top)
    if START in readme and END in readme:
        readme = readme[:readme.index(START)] + block + readme[readme.index(END) + len(END):]
    else:
        pos = readme.index("## Seven tracks")
        readme = readme[:pos] + block + "\n\n" + readme[pos:]
    return {"ROADMAP.md": "\n".join(guide), "README.md": readme}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--check", action="store_true")
    args = p.parse_args()
    for name, content in render(ROOT).items():
        path = ROOT / name
        if args.check:
            if not path.exists() or content != path.read_text():
                raise SystemExit(f"roadmap output is stale: {name}")
        else:
            path.write_text(content)


if __name__ == "__main__":
    main()
