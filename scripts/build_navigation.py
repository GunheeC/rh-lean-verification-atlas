#!/usr/bin/env python3
"""Generate the declaration finder and the unit dependency projection from portable atlas data."""
from atlas_files import unit_files
import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path
from urllib.parse import quote
from navigation_text import glossary, proof_map

ROOT = Path(__file__).resolve().parents[1]
NOTICE = "AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved"
PROOF = {"compiled_direct", "compiled_proof_route", "skeleton_proof_dependency"}


def read(rel):
    return json.loads((ROOT / rel).read_text())


def source_url(commit, pin):
    file = quote(pin["file"], safe="/")
    return f"https://github.com/leanprover-community/riemann-hypothesis/blob/{commit}/src/{file}#L{pin['line0']}-L{pin['line1']}"


def anchor(name):
    return "decl-" + hashlib.sha256(name.encode()).hexdigest()[:16]


def memberships(graph, units):
    index = defaultdict(lambda: defaultdict(set))
    def add(name, unit, role, why):
        index[name][unit, role].add(why)
    for node in graph["nodes"]:
        role = {"primary":"primary", "indexed_under_unit":"attached", "attached_assembly":"attached"}[node["assignment"]]
        add(node["name"], node["unit_id"], role, "paper:" + node["id"])
    for i,u in units.items():
        for a in u["lean"]:
            if a.get("role") == "component":
                add(a["name"], i, "support", "component of a paper implication")
                continue
            role = "secondary" if a.get("role") == "chart supplier" else "primary"
            add(a["name"],i,role,"blueprint chart" if role == "secondary" else "unit statement")
    return index


def unit_graph(graph, units, index, raw):
    nodes = {v["id"]: v["name"] for v in graph["nodes"]}
    by_pair = defaultdict(dict)
    def edge(a,b,kind,path):
        # No same-declaration aliases, ownership or editorial grouping links become proof edges.
        for (s,ar) in index.get(a, {}):
            for (t,br) in index.get(b, {}):
                if s == t or a == b or "support" in (ar, br):
                    continue
                k = (a,b,ar,br)
                values = by_pair[s,t]
                item = values.setdefault(k,dict(consumer=a,supplier=b,consumer_role=ar,supplier_role=br,kind=kind))
                if path and ("path" not in item or (len(path),path) < (len(item["path"]),item["path"])):
                    item.update(kind=kind,path=path)
    for e in graph["edges"]:
        if e["relation"] in PROOF:
            edge(nodes[e["from"]],nodes[e["to"]],e["relation"],e.get("lean_route"))
    for path in raw["routes"]:
        edge(path[0],path[-1],"compiled_value_"+str(len(path)-1)+"_hop",path)
    us = {i: dict(uses=[],used_by=[]) for i in sorted(units) if units[i].get("kind") != "paper_composite"}
    edges = []
    for (s,t),w in sorted(by_pair.items()):
        us[s]["uses"].append(t)
        us[t]["used_by"].append(s)
        edges.append({"from":s,"to":t,"witnesses":[w[k] for k in sorted(w)]})
    return {"notice":NOTICE,"source_commit":graph["source_commit"],"inputs":["data/graph.json","data/unit_value_routes.json"],
            "direction":"from (consumer) uses to (supplier). Only compiled-value routes and identified skeleton proof dependencies enter. An edge between reading units may connect attached or chart declarations rather than the two unit statements. Memberships that share a declaration produce no alias edge. Scope is the indexed evidence; absent edges do not establish independence.",
            "units":us,"edges":edges}


def direct_reading(u):
    local = [e["document"] for e in u["expositions"] if e["document"].startswith("notes/")]
    return {"status":u["status"],"scope":"unit statement under its stated hypotheses","notes":list(dict.fromkeys(local))}


def catalog(graph, units, index, pins):
    rows = {n:{**p,"units":[],"paper_entries":[],"reading":[],"crosswalk":[],"name_references":[],"anchor":anchor(n)}
            for n,p in sorted(pins["anchors"].items(),key=lambda item:(item[0].casefold(),item[0]))}
    for n,groups in index.items():
        for (i,role),origins in sorted(groups.items()):
            rows[n]["units"].append({"id":i,"role":role,"evidence":sorted(origins)})
            if role == "primary":
                rows[n]["reading"].append(dict(unit=i,**direct_reading(units[i])))
    for node in graph["nodes"]:
        rows[node["name"]]["paper_entries"].append({k:node[k] for k in ("id","unit_id","assignment","source_disposition","edition_locator","start_page")})
    for track, starter in read("data/notes_starters.json")["starters"].items():
        n, i = starter["lean_decl"], starter["unit_id"]
        rows[n]["reading"].append({"starter":track,"unit":i,"section":starter["section"],"printed_pages":starter["printed_pages"],"path":starter["path"],"relation":starter["unit_relation"]})
        if not any(x["id"]==i for x in rows[n]["units"]):
            rows[n]["units"].append(dict(id=i,role="support",evidence=["starter target"]))
    cross = read("crosswalk/adriazola.json")
    for m in cross["mappings"]:
        for a in m["lean_declarations"]:
            n = a["name"]
            record = {"external_id":m["external_id"],"page":m.get("page"),"section":m.get("section"),"relation":m["relation"]}
            rows[n]["crosswalk"].append(record)
            i = m.get("reading_routes",{}).get(n)
            if i and not any(x["id"] == i for x in rows[n]["units"]):
                rows[n]["units"].append(dict(id=i,role="support",evidence=["crosswalk reading route"]))
    for source in read("crosswalk/name_matches.json")["sources"]:
        for match in source["rows"]:
            rows[match["declaration"]]["name_references"].append(source["source_id"])
    # Some parent roots are distinct from their specialist assignments. The relationship is contextual.
    for reg in read("data/map_inputs.json")["inputs"]:
        for n in reg["roots"]:
            if not rows[n]["units"]:
                rows[n]["units"].extend(dict(id=v,role="support",evidence=["original input "+reg["id"]]) for v in reg["unit_ids"])
    for ent in rows.values():
        ent["units"].sort(key=lambda x:(x["id"],x["role"]))
        if not ent["units"]:
            raise ValueError("Unclassified source pin: "+ent["name"])
    return {"notice":NOTICE,"source_commit":pins["source_commit"],"span_rule":pins["span_rule"],"graph_rule":pins["graph_rule"],
            "roles":{"primary":"Unit statement or one of the explicit joint statements.","attached":"Paper entry attached to the indexed reading unit.","secondary":"A named supplier on the unit’s historical blueprint chart.","support":"Reading pointer for an external name, a packet or an original input. No unit-level proof claim."},
            "declarations":list(rows.values())}


def links(entry):
    return ", ".join(f'[{x["id"]}](../units/{x["id"]}.md) ({x["role"]})' for x in entry["units"])


def where(entry, names):
    locations = []
    for r in entry["reading"]:
        if "starter" in r:
            pp=r["printed_pages"]
            locations.append(f'[starter, pp. {pp[0]}–{pp[-1]}](../{r["path"]})')
        else:
            locations.append(f'[{r["status"]}](../units/{r["unit"]}.md)')
    for p in entry["paper_entries"]:
        if p["assignment"] != "primary":
            locations.append(f'v3 {p["edition_locator"]}, p. {p["start_page"]} ({p["source_disposition"]})')
    if entry["crosswalk"]:
        labels = ", ".join(dict.fromkeys(str(x["external_id"]) for x in entry["crosswalk"]))
        locations.append(f"[{names['adriazola']}, {labels}](../crosswalk/adriazola.md)")
    if entry["name_references"]:
        locations.append("Name references: "+", ".join(f'[{names[k]}](../crosswalk/{k}.md)' for k in entry["name_references"]))
    if not any("status" in r or "starter" in r for r in entry["reading"]):
        if not entry["paper_entries"]:
            locations.insert(0,"No separate atlas proof indexed")
    return "; ".join(locations)


def declaration_pages(catalog):
    entries=catalog["declarations"]
    source_names = {s["id"]: s["short_title"] for s in read("sources/registry.json")["sources"]}
    # Namespace breaks give stable, searchable ranges; the large G and U families get their own pages.
    group=lambda n: n.split(".",1)[0].casefold()
    partitions = [
        ("a-f","A–F",lambda n: group(n) < "g"),
        ("g-l","G–L",lambda n: "g" <= group(n) < "m"),
        ("m-t","M–T",lambda n: "m" <= group(n) < "u"),
        ("u-z","U–Z",lambda n: group(n) >= "u"),
    ]
    pages = {}
    intro = ["# Lean declaration lookup","",NOTICE,"","Search by the full Lean name or by its namespace. Each entry links the inclusive source range at the pinned commit, the responsible reading unit and any recorded exposition.","","| Alphabetical range | First and last declarations | Entries |","|---|---|---:|"]
    for slug,title,select in partitions:
        chosen=[e for e in entries if select(e["name"])]
        if not chosen:
            continue
        file=f"lookup/declarations-{slug}.md"
        intro.append(f'| [{title}](declarations-{slug}.md) | `{chosen[0]["name"]}` through `{chosen[-1]["name"]}` | {len(chosen)} |')
        lines=[f"# Lean declarations {title}","",NOTICE,"","[All namespaces and role definitions](declarations.md) · [Glossary](glossary.md)","","| Qualified declaration | Location in pinned source | SHA-256 of span | Dominated lines (graph) | Units | Where to read |","|---|---|---|---:|---|---|"]
        for e in chosen:
            url=source_url(catalog["source_commit"],e)
            line=f'{e["line0"]}–{e["line1"]}'
            lines.append(f'| <a id="{e["anchor"]}"></a>`{e["name"]}` | [`{e["file"]}:{line}`]({url}) | `{e["sha256"]}` | {e["dominated"]:,} (`{e["graph"]}`) | {links(e)} | {where(e,source_names)} |')
        pages[file]="\n".join(lines)+"\n"
    intro += ["",f'**{len(entries):,} declarations.** A primary declaration states a unit or one of its jointly indexed statements. An attached declaration has its own paper entry. A secondary declaration belongs to a blueprint supplier chart. A support link identifies a packet, an original input or a crosswalk route. A unit’s proof status applies only to its own statement.','',
        'The “Where to read” column distinguishes written deductions from outlines, statements, cited results and Lean-only entries. A paper page locates the start of the indicated entry. The correspondence table links numbered passages to declarations.','',
        'The source hash is SHA-256 of the 1-based inclusive UTF-8 lines joined with LF and no final LF. Dominated lines count core declaration spans reachable only through this declaration from the named graph root, stopping at literature boundaries. Six reached declarations have zero weight. Pin weights can overlap across nested declarations.','',
        '[Machine-readable lookup](../data/declarations.json) · [Pin census](../data/pins.json) · [Map of the argument](../MAP.md)']
    from index_position import lookup_scope
    intro.extend(["", *[paragraph for text in lookup_scope(ROOT) for paragraph in (text, "")]])
    pages["lookup/declarations.md"]="\n".join(intro)+"\n"
    return pages


def save(products, check):
    stale = []
    for file, data in products.items():
        path=ROOT/file
        content=data if isinstance(data,str) else json.dumps(data,ensure_ascii=False,indent=2)+"\n"
        if check:
            if not path.exists() or path.read_text()!=content:
                stale.append(file)
        else:
            path.parent.mkdir(exist_ok=True,parents=True)
            if not path.exists() or path.read_text()!=content:
                path.write_text(content)
    if stale:
        raise SystemExit("Stale navigation: "+", ".join(stale))


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check",action="store_true")
    parser.add_argument("--graph-only",action="store_true")
    args=parser.parse_args()
    units={f.stem:json.loads(f.read_text()) for f in sorted(unit_files(ROOT))}
    graph=read("data/graph.json")
    index=memberships(graph,units)
    # The DB2 prerequisite census uses the original seven-track unit projection.
    # Pillar calls have separate evidence and do not change that frozen projection.
    original = read("data/round2_reading_inputs.json")["units"]
    graph_units = {i: units[i] for i in original}
    ug=unit_graph(graph, graph_units, memberships(graph, graph_units), read("data/unit_value_routes.json"))
    products={"data/unit_graph.json":ug}
    if not args.graph_only:
        decls=catalog(graph,units,index,read("data/pins.json"))
        products["data/declarations.json"]=decls
        products.update(declaration_pages(decls))
        products["lookup/glossary.md"] = glossary(read("data/glossary_sources.json"),units,NOTICE,source_url)
        products["MAP.md"] = proof_map(read("data/map_inputs.json"),graph,decls,NOTICE)
    save(products,args.check)
    print(f"{len(units)} units, {len(ug['edges'])} unit dependencies",end="")
    if not args.graph_only:
        print(f", {len(decls['declarations'])} declarations",end="")
    print()


if __name__=="__main__":
    main()
