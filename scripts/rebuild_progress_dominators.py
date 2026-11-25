#!/usr/bin/env python3
"""Replay the compact progress certificate from the pinned external extraction."""
import argparse
from hashlib import file_digest
import json
from pathlib import Path
import sys
from tempfile import TemporaryDirectory


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("--notes",type=Path,required=True,help="Read-only RH notes extraction containing out/graph_cache.bin and its dominator tools")
    p.add_argument("--root",type=Path,default=Path(__file__).resolve().parents[1])
    p.add_argument("--write",action="store_true",help="Replace the certificate after checking all source pin weights")
    args=p.parse_args()
    cert_path=args.root/"progress/dominators.json"
    pins=json.loads((args.root/"data/pins.json").read_bytes())
    graph_path=args.notes/"out/graph_cache.bin"
    with graph_path.open("rb") as f:
        if file_digest(f,"sha256").hexdigest()!=pins["graph_sha256"]:
            raise ValueError("Unexpected source graph digest")
    sys.path.insert(0,str(args.notes/"scripts"))
    from blueprint_cones import Graph
    from r22_graph import dominator_tree
    graph=Graph(graph_path)
    with TemporaryDirectory() as t:
        parent,weight=dominator_tree(graph,Path(t))
    selected={name:graph.index[name] for name,pin in pins["anchors"].items() if pin["graph"]=="allChi"}
    indices=set(selected.values())
    anchors={}
    for name,i in selected.items():
        if parent[i]<0 or weight[i]!=pins["anchors"][name]["dominated"]:
            raise ValueError("Mismatch at "+name)
        j=parent[i]
        while j!=parent[j] and j not in indices:
            j=parent[j]
        anchors[name]={"parent":None if i==j else graph.names[j],"weight":weight[i]}
    candidate=dict(source_commit=pins["source_commit"],graph_sha256=pins["graph_sha256"],root="allChi",
                   total=weight[graph.index["allChi"]],rule="Nearest strictly dominating selected anchor. A subtree has the inclusive core-span weight in the pinned mixed allChi graph with literature stops. Roots outside allChi contribute no lines.",anchors=anchors)
    if args.write:
        cert_path.write_text(json.dumps(candidate,ensure_ascii=False,sort_keys=True,indent=2)+"\n")
    elif json.loads(cert_path.read_bytes())!=candidate:
        raise SystemExit("Dominator certificate differs from graph replay")
    print(f"{len(anchors)} allChi anchor weights and nearest selected dominators matched")


if __name__=="__main__":
    main()
