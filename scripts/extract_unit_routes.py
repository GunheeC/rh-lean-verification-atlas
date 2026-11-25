#!/usr/bin/env python3
"""Capture checked compiled-value paths between unit statements and their supporting declarations.

Optional archival import. Ordinary builds use the portable data/unit_value_routes.json.
Inputs are the existing RH Notes metadata and Lean 4.33.1 objects. No modules are rebuilt.
"""
from atlas_files import unit_files
import argparse
from collections import defaultdict, deque
import hashlib
import json
from pathlib import Path
import subprocess
import tempfile
import sys

ROOT = Path(__file__).resolve().parents[1]


def sha(path):
    with path.open("rb") as stream:
        return hashlib.file_digest(stream, "sha256").hexdigest()


def capture(notes, lean):
    pins = json.loads((ROOT / "data/pins.json").read_text())["anchors"]
    heads = set()
    for path in sorted(unit_files(ROOT)):
        unit = json.loads(path.read_text())
        heads.update(unit.get("statement_declarations", [unit["lean"][0]["name"]]))
    graph = json.loads((ROOT / "data/graph.json").read_text())
    owned = {n["name"] for n in graph["nodes"]}
    for path in sorted(unit_files(ROOT)):
        owned.update(a["name"] for a in json.loads(path.read_text())["lean"])
    objects = notes / ".oleans/extract/.lake/build/lib/lean"
    manifest = notes / ".oleans/olean-manifest.sha256"
    prefix = ".lake/build/lib/lean/"
    hashes = {}
    for entry in manifest.read_text().splitlines():
        h, file = entry.split("  ", 1)
        if file.startswith(prefix) and file.endswith(".olean"):
            hashes[file[len(prefix):-6].replace("/", ".")] = h
    checked = set()
    reader = notes / "scripts/r19_value_edges.lean"
    modules = {n: a["file"][:-5].replace("/", ".") for n, a in pins.items()}
    with tempfile.TemporaryDirectory() as tmp:
        req, out = Path(tmp)/"requests", Path(tmp)/"terms"
        def fetch(names):
            group = defaultdict(list)
            for n in sorted(names):
                group[modules[n]].append(n)
            for mod in group.keys() - checked:
                if sha(objects / (mod.replace(".", "/") + ".olean")) != hashes[mod]:
                    raise ValueError("Object mismatch: " + mod)
            checked.update(group)
            req.write_text("".join("\t".join([mod, *names]) + "\n" for mod, names in sorted(group.items())))
            subprocess.run([lean, "--run", reader, objects, req, out], check=True)
            terms = {r["name"]: set(r["value"]) for r in map(json.loads,out.read_text().splitlines())}
            if set(names) != terms.keys():
                raise ValueError("Incomplete compiled-value response")
            return terms
        first = fetch(heads)
        wanted = set.union(*first.values()) - owned
        bridges = set()
        with (notes / "out/decls.jsonl").open() as stream:
            for line in stream:
                if not line.startswith('{"name":'):
                    raise ValueError("Unexpected declaration record")
                # The archive contains a million rows; only selected single-hop neighbours matter.
                row = json.loads(line)
                n = row["name"]
                if n in wanted and row["cls"] == "core" and row["kind"] == "thm" and not row["internal"]:
                    modules[n] = row["module"]
                    bridges.add(n)
        second = fetch(bridges)
        # Only propose paths through core theorems, then verify every individual step
        # in its compiled value. A type/constructor edge alone is never sufficient.
        sys.path.insert(0,str(notes/"scripts"))
        from blueprint_cones import Graph
        cache = notes/"out/graph_cache.bin"
        expected_hash = json.loads((ROOT/"data/pins.json").read_text())["graph_sha256"]
        if sha(cache) != expected_hash:
            raise ValueError("Changed original graph cache")
        graph_db = Graph(cache)
        head_idx = {graph_db.index[h] for h in heads if h in graph_db.index}
        is_theorem = bytes(k == "thm" and c == "core" and not hidden for _,k,c,_,_,hidden in graph_db.info)
        proposals = []
        for start in sorted(head_idx):
            seen = {start:None}
            queue = deque([start])
            targets = []
            while queue:
                curr = queue.popleft()
                for dest in graph_db.target[graph_db.start[curr]:graph_db.start[curr+1]]:
                    if dest in seen or not is_theorem[dest]:
                        continue
                    seen[dest] = curr
                    if dest in head_idx:
                        targets.append(dest)
                    else:
                        queue.append(dest)
            for dest in targets:
                chain = []
                while dest is not None:
                    chain.append(graph_db.names[dest])
                    dest = seen[dest]
                if len(chain) > 3:
                    proposals.append(list(reversed(chain)))
        proposed_names = {n for route in proposals for n in route[:-1]}
        modules.update({n:graph_db.info[graph_db.index[n]][0] for n in proposed_names})
        known = {**first, **second}
        missing = proposed_names - known.keys()
        if missing:
            known.update(fetch(missing))
        long_routes = [route for route in proposals if all(b in known[a] for a,b in zip(route,route[1:]))]
    paths = []
    used = set()
    for a, deps in sorted(first.items()):
        for b in sorted(deps & owned - {a}):
            paths.append([a,b])
            used.add(modules[a])
        for m in sorted(deps & bridges):
            for b in sorted(second[m] & owned - {a}):
                paths.append([a,m,b])
                used.update((modules[a], modules[m]))
    for path in long_routes:
        paths.append(path)
        used.update(modules[n] for n in path[:-1])
    return {"rule":"Every hop is a direct constant in the compiled value. The short survey stops at an owned declaration, directly or through one non-internal project theorem outside the owner index. For the head-to-head survey, propose shortest routes through core non-internal theorems, stopping at the next statement head on each branch. Keep a proposed route only after every hop is verified in the compiled value. Other routes may exist.", "long_verified":len(long_routes), "long_candidates":len(proposals), "lean":"4.33.1", "lean_commit":graph["source_commit"], "manifest_sha256":sha(manifest), "reader_sha256":sha(reader), "object_sha256":{m:hashes[m] for m in sorted(used)}, "routes":sorted(paths)}


if __name__ == "__main__":
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--notes",required=True,type=Path)
    p.add_argument("--lean",required=True,type=Path)
    args = p.parse_args()
    evidence = capture(args.notes.resolve(), args.lean.resolve())
    out = ROOT / "data/unit_value_routes.json"
    out.write_text(json.dumps(evidence, ensure_ascii=False,indent=2)+"\n")
    print(f"{len(evidence['routes'])} compiled-value paths in {len(evidence['object_sha256'])} source modules")
