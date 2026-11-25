#!/usr/bin/env python3
"""Check the round-3 reading links against their frozen paths, declarations and DB2 evidence.

Run without arguments for the in-atlas census. Add --lean-src /path/to/lean/src
to compare every declaration span to a local checkout of the pinned edition.
"""
import argparse
from collections import Counter, defaultdict
from graphlib import TopologicalSorter
import hashlib
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def read(path):
    return json.loads(path.read_bytes())


def verify(root, source=None):
    records = read(root / "data/round3_prerequisites.json")
    declarations = records["declarations"]
    units = records["units"]
    old = read(root / records["baseline"])["units_by_id"]
    graph = read(root / "data/unit_graph.json")
    if set(units) != set(old) or graph["source_commit"] != records["lean_commit"]:
        raise ValueError("Snapshot mismatch")
    lookup = {(e["from"], e["to"]): e["witnesses"] for e in graph["edges"]}
    list(TopologicalSorter({i: u["prerequisites"] for i, u in units.items()}).static_order())
    expected_places = defaultdict(list)
    regions = {"Start here":"starter", "First reading":"first",
               "Core argument":"core", "Open inputs and scope":"open"}
    for page in sorted(root.glob("tracks/*/README.md")):
        section = None
        for line_no, line in enumerate(page.read_text().splitlines(), 1):
            if line.startswith("#"):
                section = regions.get(line.strip("# "))
            if section:
                for i in re.findall(r"\[[^\]]+\]\(../../units/([^/)]+)\.md\)",line):
                    if i in units:
                        expected_places[i].append(dict(track=page.parent.name, path=page.relative_to(root).as_posix(),
                                                       section=section, line=line_no))
    kinds = Counter()
    new = 0
    for i, u in units.items():
        if u["path_locations"] != expected_places.get(i, []) or u["prerequisites"] != sorted(u["links"]):
            raise ValueError(f"{i}: path or prerequisite mismatch")
        previous = old[i]["reading_prerequisite_evidence"]
        if not previous.keys() <= u["links"].keys():
            raise ValueError(f"{i}: dropped inherited reading link")
        should_audit = i in expected_places and not previous
        if should_audit != bool(u["audit"]):
            raise ValueError(f"{i}: audit cohort mismatch")
        if should_audit and (not u["audit"]["reason"] or not u["audit"]["statement_declarations"]):
            raise ValueError(f"{i}: missing statement audit")
        for j, link in u["links"].items():
            if j not in units:
                raise ValueError(f"{i}: unknown reading unit {j}")
            kinds[link["source"]] += 1
            if j in previous and link.get("inherited_evidence") != previous[j]:
                raise ValueError(f"{i}->{j}: changed inherited evidence")
            if j not in previous:
                if not should_audit or link["origin"] != "DB3":
                    raise ValueError(f"{i}->{j}: unexpected new reading link")
                new += 1
            if link["source"] == "graph":
                if not any(w["consumer_role"] == w["supplier_role"] == "primary"
                           and w["consumer"] == link["consumer"] and w["supplier"] == link["preceding"]
                           and w["kind"] == link["basis"] for w in lookup.get((i,j), [])):
                    raise ValueError(f"{i}->{j}: unidentified primary graph edge")
                names = [link["consumer"], link["preceding"]]
            elif link["source"] == "statement-reading":
                paths = [link["consumer_type_path"], link["preceding_type_path"]]
                if not link["explanation"] or any(not (2 <= len(p) <= 4) or p[-1] != link["object"] for p in paths):
                    raise ValueError(f"{i}->{j}: incomplete common statement object")
                names = paths[0] + paths[1]
            else:
                raise ValueError(f"{i}->{j}: unknown reading source")
            if not set(names) <= declarations.keys():
                raise ValueError(f"{i}->{j}: unpinned source")
    if new != records["counts"]["new_links"]:
        raise ValueError("New link count mismatch")
    if source is not None:
        for name, pin in declarations.items():
            lines = (source / pin["file"]).read_text().splitlines()
            lo, hi = pin["line0"], pin["line1"]
            digest = hashlib.sha256("\n".join(lines[lo-1:hi]).encode()).hexdigest()
            if (not 1 <= lo <= hi <= len(lines) or digest != pin["sha256"] or pin["name"] != name):
                raise ValueError(f"{name}: source span mismatch")
    return dict(units=len(units), declarations=len(declarations), **kinds, newly_added=new)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--lean-src", type=Path)
    args = parser.parse_args()
    print(json.dumps(verify(args.root.resolve(),args.lean_src),sort_keys=True))
