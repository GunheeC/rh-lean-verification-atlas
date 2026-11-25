"""Regenerate the optional allChi traversal graph from pinned Lean compiler output."""
import argparse
from array import array
from collections import defaultdict
from hashlib import sha256
from itertools import groupby
import json
import lzma
import os
from pathlib import Path
import struct
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[1]
TOOLCHAIN = "leanprover/lean4:v4.33.1"


def read_declarations(trace, objects):
    node_ids = {}
    by_module = defaultdict(list)
    literature = bytearray()
    with (trace / "decls.jsonl").open(encoding="utf-8") as stream:
        for line in stream:
            row = json.loads(line)
            if row["cls"] not in {"core", "lit"}:
                continue
            name = row["name"]
            if name in node_ids:
                raise ValueError(f"Duplicate declaration {name}")
            node = len(node_ids)
            node_ids[name] = node
            literature.append(row["cls"] == "lit")
            if row["cls"] == "core":
                by_module[row["module"]].append((node, name))

    weights = array("I", [0]) * len(node_ids)
    for module, declarations in by_module.items():
        index = objects / (module.replace(".", "/") + ".ilean")
        spans = json.loads(index.read_bytes())["decls"]
        for node, name in declarations:
            if name in spans:
                first, _, last, *_ = spans[name]
                weights[node] = last - first + 1
    return node_ids, literature, weights


def edge_records(stream):
    # The Lean writer emits compact two-field JSON. Most names need no JSON unescaping.
    for line in stream:
        if "\\" in line:
            record = json.loads(line)
            yield record["src"], record["dst"]
        else:
            src, dst = line[8:-3].split('","dst":"')
            yield src, dst


def graph_edges(trace, node_ids, literature):
    offsets, targets = array("I", [0]), array("I")
    with (trace / "edges.jsonl").open(encoding="utf-8") as stream:
        for source, edges in groupby(edge_records(stream), key=lambda edge: edge[0]):
            node = node_ids[source]
            if node < len(offsets) - 1:
                raise ValueError("Trace edge groups differ from declaration visit order")
            while len(offsets) < node + 1:
                offsets.append(len(targets))
            if not literature[node]:
                children = {node_ids.get(target) for _, target in edges}
                children.discard(node)
                children.discard(None)
                targets.extend(sorted(children))
            offsets.append(len(targets))
    while len(offsets) <= len(node_ids):
        offsets.append(len(targets))
    return offsets, targets


def check_source(checkout):
    if (checkout / "lean-toolchain").read_text().strip() != TOOLCHAIN:
        raise ValueError(f"Expected {TOOLCHAIN} in project's lean-toolchain")
    inventory = json.loads((ROOT / "progress/source_inventory.json").read_bytes())
    for path, row in inventory["files"].items():
        if sha256((checkout / "src" / path).read_bytes()).hexdigest() != row["sha256"]:
            raise ValueError(f"Source file differs from the pinned sample: {path}")


def pack(trace, objects, output):
    meta = json.loads((ROOT / "progress/position_graph.json").read_bytes())
    node_ids, literature, weights = read_declarations(trace, objects)
    if len(weights) != meta["nodes"] or any(node_ids.get(name) != pos for name, pos in meta["named_nodes"].items()):
        raise ValueError("The declaration order differs from the pinned graph")
    offsets, targets = graph_edges(trace, node_ids, literature)
    if len(targets) != meta["edges"]:
        raise ValueError("The edge count differs from the pinned graph")
    with tempfile.NamedTemporaryFile(dir=output.parent) as tmp:
        with lzma.open(tmp, "wb", preset=4) as graph:
            graph.write(b"RHGRAPH1" + struct.pack("<II", len(weights), len(targets)))
            for column in (weights, offsets, targets):
                if column.itemsize != 4:
                    raise ValueError("Packing requires 32-bit unsigned integers")
                if sys.byteorder != "little":
                    column.byteswap()
                graph.write(column)
        tmp.seek(0)
        digest = sha256(tmp.read()).hexdigest()
        if digest != meta["sha256"]:
            raise ValueError(f"Packed graph differs from its pinned SHA-256: {digest}")
        # Publish the verified file atomically, without replacing any existing path.
        tmp.flush()
        os.link(tmp.name, output)
    print(f"{digest}  {output} ({len(weights):,} nodes, {len(targets):,} edges)")


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--checkout", required=True, type=Path, help="Lean project containing src/ and lean-toolchain")
    p.add_argument("--objects", type=Path, help="Project .olean and .ilean tree (default: CHECKOUT/.lake/build/lib/lean)")
    p.add_argument("--output", required=True, type=Path, help="New path for the authenticated position_graph.xz")
    p.add_argument("--trace-dir", type=Path, help="Reuse complete decls.jsonl and edges.jsonl from this extractor")
    p.add_argument("--lean", default="lean", help="Lean 4.33.1 executable (default: lean on PATH)")
    args = p.parse_args()
    checkout = args.checkout.resolve()
    objects = (args.objects or checkout / ".lake/build/lib/lean").resolve()
    output = args.output.resolve()
    if output.is_relative_to(checkout) or output.is_relative_to(objects) or output.is_relative_to(ROOT):
        p.error("Choose an output outside the atlas, the source checkout and the compiled objects")
    if output.exists():
        p.error("Output already exists. Choose a new path.")
    output.parent.mkdir(parents=True, exist_ok=True)
    check_source(checkout)
    if not all((objects / ("Main." + ext)).is_file() for ext in ("olean", "ilean")):
        p.error("Supply the project object directory containing Main.olean and Main.ilean")
    if args.trace_dir:
        pack(args.trace_dir, objects, output)
        return
    version = subprocess.check_output([args.lean, "--version"], cwd=checkout, text=True)
    if "version 4.33.1," not in version:
        p.error(f"Expected Lean 4.33.1, found {version.strip()}")
    with tempfile.TemporaryDirectory(dir=output.parent) as work:
        subprocess.run([args.lean, "--run", str(ROOT / "scripts/trace_position_graph.lean"), str(objects), work],
                       cwd=checkout, check=True)
        pack(Path(work), objects, output)


if __name__ == "__main__":
    main()
