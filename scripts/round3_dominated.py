"""Recompute one allChi dominator weight by removing the named declaration."""
import argparse
from array import array
import hashlib
import json
from pathlib import Path
import pickle


def reachable_weight(root, excluded, records, starts, targets):
    seen = bytearray(len(records))
    todo = array("i")
    if root != excluded:
        todo.append(root)
        seen[root] = 1
    total = 0
    while todo:
        node = todo.pop()
        _, _, classification, first, last, _ = records[node]
        if classification == "lit":
            continue
        if classification == "core" and 1 <= first <= last:
            total += last - first + 1
        for child in targets[starts[node]:starts[node+1]]:
            if child != excluded and not seen[child]:
                seen[child] = 1
                todo.append(child)
    return total


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("graph", type=Path)
    parser.add_argument("name")
    parser.add_argument("--pins", type=Path, default=Path("data/pins.json"))
    args = parser.parse_args()
    pins = json.loads(args.pins.read_text())
    pin = pins["anchors"][args.name]
    if pin["graph"] != "allChi":
        parser.error("Select a declaration measured from allChi.")
    with args.graph.open("rb") as f:
        if hashlib.file_digest(f, "sha256").hexdigest() != pins["graph_sha256"]:
            parser.error("The graph file differs from the pinned export.")
        f.seek(0)
        names, records, starts, targets = pickle.load(f)
    root = names.index("allChi")
    excluded = names.index(args.name)
    before = reachable_weight(root, -1, records, starts, targets)
    after = reachable_weight(root, excluded, records, starts, targets)
    print(f"root: {before}\nwithout {args.name}: {after}\ndominated: {before-after}")
    if before != pins["allChi_total"] or before - after != pin["dominated"]:
        raise SystemExit("The recomputed weights differ from the pin ledger.")


if __name__ == "__main__":
    main()
