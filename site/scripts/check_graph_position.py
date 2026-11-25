"""Replay a deletion from a separately reconstructed allChi graph. All numbers are little-endian uint32."""
import argparse
from array import array
from hashlib import file_digest
import json
import lzma
from pathlib import Path
import struct
import sys

ROOT = Path(__file__).resolve().parents[1]
MAGIC = b"RHGRAPH1"
HEADER = struct.Struct("<II")

def read_array(stream, count):
    a = array("I")
    data = stream.read(4*count)
    if len(data) != 4*count or a.itemsize != 4:
        raise ValueError("Unexpected traversal array length or integer size")
    a.frombytes(data)
    if sys.byteorder != "little":
        a.byteswap()
    return a

def reachable(root, removed, weights, ends, edges):
    seen = bytearray(len(weights))
    todo = array("I", [root]) if removed != root else array("I")
    seen[root] = 1
    total = 0
    while todo:
        node = todo.pop()
        total += weights[node]
        for child in edges[ends[node]:ends[node+1]]:
            if child != removed and not seen[child]:
                seen[child] = 1
                todo.append(child)
    return total

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("name", nargs="?", default="UpperTheory.FinalTheorems.everyCharacter_of_row")
    parser.add_argument("--graph", required=True, type=Path, help="Authenticated output of pack_position_graph.py")
    args = parser.parse_args()
    meta = json.loads((ROOT/"progress/position_graph.json").read_text())
    pins = json.loads((ROOT/"data/pins.json").read_text())
    if meta["source_graph_sha256"] != pins["graph_sha256"]:
        parser.error("The source graph differs from the pin register.")
    with args.graph.open("rb") as stream:
        if file_digest(stream,"sha256").hexdigest() != meta["sha256"]:
            parser.error("The traversal graph digest differs.")
        stream.seek(0)
        with lzma.open(stream) as graph:
            if graph.read(8) != MAGIC:
                parser.error("Unknown traversal graph format")
            n, m = HEADER.unpack(graph.read(HEADER.size))
            if (n, m) != (meta["nodes"], meta["edges"]):
                parser.error("Graph and name index dimensions differ")
            weights = read_array(graph,n)
            ends = read_array(graph,n+1)
            edges = read_array(graph,m)
            if graph.read(1) or ends[0] != 0 or ends[-1] != m:
                parser.error("Traversal graph dimensions differ")
    try:
        remove = meta["named_nodes"][args.name]
        expected = pins["anchors"][args.name]["dominated"]
    except KeyError:
        parser.error("Choose a named allChi anchor in progress/position_graph.json")
    before = reachable(meta["root"], -1, weights, ends, edges)
    after = reachable(meta["root"], remove, weights, ends, edges)
    if before != pins["allChi_total"] or before - after != expected:
        raise SystemExit("Computed weight does not agree with its source pin")
    print(f"root: {before}\nwithout {args.name}: {after}\ndominated: {before-after}")

if __name__ == "__main__":
    main()
