#!/usr/bin/env python3
"""Rebuild the DB1 anchor census from the RH notes extraction and pinned source archive."""
import argparse
import hashlib
import json
import sys
import tarfile
import tempfile
from collections import defaultdict
from pathlib import Path

COMMIT = "40e56bab026552e089d7afcfeff08d2defb9c005"
ARCHIVE = "9631b4f020199e580ba86178cb56c6e9b09f690c2369a80dc4334aa93f49c7fc"


def read(path):
    return json.loads(path.read_bytes())


def write(path, data):
    tmp = path.with_suffix(".partial")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
    tmp.replace(path)


def digest(path):
    with path.open("rb") as f:
        return hashlib.file_digest(f, "sha256").hexdigest()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--notes", required=True, type=Path)
    p.add_argument("--source-project", required=True, type=Path)
    p.add_argument("--data", type=Path, default=Path(__file__).resolve().parents[1] / "data")
    args = p.parse_args()
    repo = args.notes.resolve()
    src = args.source_project.resolve() / "lean/src"
    archive = args.source_project.resolve() / "lean.tar.gz"
    sys.path.insert(0, str(repo / "scripts"))
    from blueprint_cones import Graph
    from r19_cones import SHA_CACHE, PUBLIC
    from r22_graph import dominator_tree
    cache = repo / "out/graph_cache.bin"
    if digest(cache) != SHA_CACHE or digest(archive) != ARCHIVE:
        raise ValueError("Changed source or graph pin")
    skeleton = read(repo / "out/R19_skeleton.json")
    extra = skeleton["cones"]["supplement"]["project_nodes"]
    all_nodes = {}
    for fn in ("R21_parent_status","R21_split_nodes","R22_decomposition"):
        for row in read(repo / ("out/" + fn + ".json"))["nodes"]:
            all_nodes[row["name"]] = row["source"]
    assert len(all_nodes) == 775
    status = read(repo / "blueprint/status.json")
    for unit in status["units"].values():
        for r in unit["roots"]:
            all_nodes.setdefault(r["name"],r)
    for unit in status["recursive_inputs"].values():
        for n in unit["roots"]:
            all_nodes.setdefault(n,{})
    for f in args.data.glob("*anchor_requests.json"):
        for n in read(f):
            all_nodes.setdefault(n,{})
    starters = read(args.data / "notes_starters.json")["starters"]
    for starter in starters.values():
        for key in ("lean_decl","support_declarations","supporting_declarations","lean_declarations"):
            names = starter.get(key,[])
            if isinstance(names,str):
                names = [names]
            for item in names:
                n = item if isinstance(item,str) else item["name"]
                all_nodes.setdefault(n,{})
    print("Building",len(all_nodes),"pins",flush=True)
    graph = Graph(cache)
    with tempfile.TemporaryDirectory() as temp:
        temp = Path(temp)
        parent,dom = dominator_tree(graph,temp)
        assert dom[graph.index["allChi"]] == 9567045
        known_weights = read(repo / "out/R22_graph_weights.json")["weights"]
        for n, old in known_weights.items():
            i = graph.index[n]
            assert (parent[i] >= 0) == old["reached"] and dom[i] == old["dominated"], n
        five_extra = set(extra)
        for n, row in extra.items():
            assert n not in graph.index
            graph.index[n] = len(graph.names)
            graph.names.append(n)
            a,b = row["line0"], row["line1"]
            graph.info.append((row["module"],"thm","core",a,b,False))
            graph.lines.append(b-a+1 if a else 0)
        graph.lit += bytes(len(extra))
        for n,row in extra.items():
            graph.target.extend(graph.index[c] for c in row["project_dependencies"])
            graph.start.append(len(graph.target))
        synthetic = len(graph.names)
        graph.names.append("DB1 synthetic public root")
        graph.lines.append(0)
        graph.lit += bytes(1)
        graph.target.extend(graph.index[n] for n in PUBLIC)
        graph.start.append(len(graph.target))
        original = graph.index["allChi"]
        # R22's routine reads its entrypoint from this one index.
        graph.index["allChi"] = synthetic
        try:
            five_parent, five_dom = dominator_tree(graph,temp)
        finally:
            graph.index["allChi"] = original
        assert five_dom[synthetic] == 9567245
    anchors = {}
    files = defaultdict(list)
    for n, expected in sorted(all_nodes.items()):
        v = graph.index.get(n)
        if v is None:
            raise ValueError("Missing declaration metadata: "+n)
        mod,kind,cls,a,b,_ = graph.info[v]
        fn = mod.replace(".","/")+".lean"
        if a < 1 or a > b:
            raise ValueError("Missing source interval: "+n)
        if v < len(parent) and parent[v] >= 0:
            weight, scope = dom[v],"allChi"
        elif five_parent[v] >= 0:
            weight, scope = five_dom[v],"five_public_heads"
        else:
            weight, scope = None,"outside_both_roots"
        anchors[n] = dict(name=n,file=fn,line0=a,line1=b,sha256=None,dominated=weight,graph=scope)
        if expected:
            assert (expected["file"],expected["line0"],expected["line1"]) == (fn,a,b), n
        files[fn].append(n)
    matched = set()
    with tarfile.open(archive, "r|gz") as tf:
        for item in tf:
            fn = item.name.removeprefix("lean/src/")
            if fn not in files:
                continue
            if fn in matched or not item.isfile():
                raise ValueError("Duplicate/nonfile member: "+fn)
            raw = tf.extractfile(item).read()
            if raw != (src/fn).read_bytes():
                raise ValueError("Working file differs from archive: "+fn)
            lines = raw.decode().splitlines()
            for n in files[fn]:
                row = anchors[n]; expected = all_nodes[n]
                if row["line1"] > len(lines):
                    raise ValueError("Out-of-range declaration: "+n)
                span = "\n".join(lines[row["line0"]-1:row["line1"]]).encode()
                row["sha256"] = hashlib.sha256(span).hexdigest()
                previous_hash = expected.get("sha256",expected.get("sha256_source_span"))
                if previous_hash and previous_hash != row["sha256"]:
                    raise ValueError("Stored span differs: "+n)
            matched.add(fn)
    assert matched == files.keys(), set(files)-matched
    pins = dict(source_commit=COMMIT,archive_sha256=ARCHIVE,graph_sha256=SHA_CACHE,
                span_rule="1-based inclusive. UTF-8 source lines joined by LF, without a final LF.",
                graph_rule="allChi, stop at lit, mixed type/value/constructor edges, weight inclusive core declaration span, literature weight zero. Dominator subtree weight, not additive across overlapping anchors. For exterior nodes only, five_public_heads adds the 29 pinned R19 project nodes and an unweighted synthetic root over the five conclusions. null means unreachable in both universes.",
                allChi_total=dom[original],five_public_heads_total=five_dom[synthetic],
                archive_files_compared=len(matched),checked_anchors=len(anchors),anchors=anchors)
    write(args.data/"pins.json",pins)
    print("Verified",len(matched),"complete source files and",len(anchors),"declaration spans",flush=True)


if __name__ == "__main__":
    main()
