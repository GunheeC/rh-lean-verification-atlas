"""Render the mathematical map and the glossary using the frozen evidence tables."""
from collections import Counter


def unit(i, prefix=""):
    return f"[{i}]({prefix}units/{i}.md)"


def mermaid(lines):
    return "\n".join(["```mermaid", "flowchart TD", *lines, "```"])


def glossary(source, units, notice, source_url):
    text=["# Glossary","",notice,"","Terms such as “host”, “polarized row”, “page function”, “closed link”, “tied family” and “definite-side witness” name Lean identifiers or constructions in this project’s drafts. They are not standard names for these particular definitions in the literature. Each source link opens the exact Lean definition or theorem. The unit column identifies the statement owner when one exists and otherwise gives the place to read its construction or use. A shared short name may have other meanings elsewhere in the development.","",
          "| Term | Meaning on this route | Lean source | Atlas context |","|---|---|---|---|"]
    for r in sorted(source["terms"],key=lambda x:x["term"].casefold()):
        d = r["definition"]
        owners={i for i,u in units.items() if d["name"] in u.get("statement_declarations",[u["lean"][0]["name"]])}
        all_defs=[d,*r["additional_definitions"]]
        src=" · ".join(f'[`{h["name"]}`]({source_url(source["source_commit"],h)})' for h in all_defs)
        context=", ".join(unit(i,"../") for i in r["unit_ids"])
        if owners:
            context="Statement "+", ".join(unit(i,"../") for i in sorted(owners)) + (". Read with "+", ".join(unit(i,"../") for i in r["unit_ids"] if i not in owners) if set(r["unit_ids"])-owners else "")
        else:
            context="Construction or use in "+context
        text.append(f'| **{r["term"]}** | {r["meaning"]} | {src} | {context} |')
    text+=["","[Declaration lookup](declarations.md) · [Source spans and SHA-256 hashes](../data/glossary_sources.json) · [Map](../MAP.md)"]
    return "\n".join(text)+"\n"


def proof_map(register, graph, lookup, notice):
    nodes={r["id"]:r for r in graph["nodes"]}
    catalog={r["name"]:r for r in lookup["declarations"]}
    def paper(i):
        n=nodes[i]
        if n["unit_id"]==i:
            return unit(i)
        e=catalog[n["name"]]
        f=shard(e["name"])
        return f"[{i}](lookup/declarations-{f}.md#{e['anchor']})"
    text=["# Map of the argument","",notice,"",
      "Trace the two open inputs in the [Selmer window map](pillars/V.md) and the [definite-side witness map](pillars/F.md). Each table gives the assumptions, source calls and first steps to challenge.","",
      "## 1. Five goals and the common window","",
      "The five exported statements reduce through the common every-character assertion. The written argument uses a one-sided Chebyshev bound on arbitrarily distant intervals of fixed power length. For a zero with real part greater than one half, the exponent can be chosen strictly below that real part. The Landau argument then excludes the corresponding pole. The arithmetic and geometric inputs below supply the hypotheses of this conditional deduction.","",
      mermaid(['    v["V: Selmer window"] --> host["Character hosts on a 3/2 window"]',
               '    lb["List B: host construction"] --> host',
               '    f["F: simultaneous geometric data"] --> top["TopG: connected families"]',
               '    green["B: Green character input"] --> top',
               '    lc["List C: closed comparisons"] --> top',
               '    la["List A: local estimates"] --> gm["P017: Chebyshev bound on tied scales"]',
               '    host --> win["One-sided power-window inequality"]',
               '    top --> win','    gm --> win',
               '    win --> primitive["Primitive nonvanishing via Landau"]',
               '    primitive --> every["Every character"]','    every --> goals["Five public goals"]']),
      "", "Arrows in this diagram run from an input to the deduction it supports. The last step includes passage to the inducing primitive character and the functional equation. The five targets are the Mathlib zeta statement, the explicit zeta zero-line statement, Dirichlet nonvanishing on the right half-plane, and the open-strip zero-line statements for all and for primitive characters. "+ " · ".join(unit(i) for i in graph["roots"]["r19_public_ids"])+". [Exact signatures and exceptions](sources/lean-goals.md)","",
      "| Input | What the implication assumes | Dominated core lines at the supplying theorem |","|---|---|---:|",
      f"| V | A common Selmer length budget on windows for each primitive character (exponent 401). {unit('P013')} | {nodes['P013']['source']['dominated']:,} |",
      f"| F | One inhabitant of the HypsAlt record for closed LinkN and the definite-side condition. {unit('T02')} | {nodes['T02']['source']['dominated']:,} |",
      f"| B | Green’s character-theoretic input for finite general linear groups. {unit('D575')} | {nodes['D575']['source']['dominated']:,} |","",
      "The Selmer budget concerns a localization kernel. The comparison also needs LinkN on the chosen geometric data and the same family index. After the local and slope estimates, P017 bounds the weighted prime sum by $x^{1/2+(e_D+e_L+7)\\varepsilon}$. The chosen exponents give $1/2+9\\varepsilon$. ["+"Geometric estimate](units/D427.md) · [Slope bound](units/P021.md) · [Window inequality](units/P017.md) · [Landau theorem](units/P022.md)",
      "", "The following lists are the remaining formal premises in the review of paper v3, §6.2. The single-letter input B and the list labelled B are separate entries. Paper v4 writes out list A and states the conditional deduction at two locations. [Conditional unit and table](units/V4-COND.md) · [Edition-specific review](reviews/R23_review.md)","",
      "| List | What it supplies | Components in the v3 review |","|---|---|---|",
      f"| A | The lattice and error estimates for {unit('P017')}. | {', '.join(paper(i) for i in ['D547','D548','D549','D562','D567','D014','D550'])}, the character balance identity, the Lipschitz weight estimate and the thick-place rewrite. |",
      f"| B | Combining the Selmer window with a host, as required by {unit('B07')}. | The prime pair and its share and existence, the character field, the bounded twist and its field/pair identifications inside {paper('D510')}, then {paper('D511')}, {paper('D513')} and {paper('D515')}. |",
      f"| C | The closed geometric and arithmetic comparisons assembled in {unit('B05')}. | {', '.join(paper(i) for i in ['D483','D479','D481','D480','D482','B06','D484','D485','D486','D489'])}, including the D516–D518 subentries of B06, plus the small-level rank equality, decay selection and final shape-to-goal assembly. |",
      "", "## 2. The original twenty recursive inputs","",
      "The blueprint ledger grouped twenty recursive inputs, each with one or more exact Lean entry declarations. The paper identified twenty-nine entry declarations in total. Its predecessor column gives the upper paper declaration and the length of each checked proof path, in the same order as the entry IDs. Each specialist link opens the current atlas unit for that original assignment. [Ledger transcription with source hashes](data/map_inputs.json) · [Blueprint assignment crosswalk](data/blueprint_groups.json)","",
      mermaid(['    orig["20 original recursive inputs"] --> trace["Trace and Selmer counts"]',
               '    orig --> loc["Local divisibility"]','    orig --> slope["Global lattice slopes"]',
               '    trace --> z1["Z1: arithmetic points, 5"]','    trace --> z2["Z2: cohomology bounds, 7"]',
               '    trace --> z3["Z3: congruence index, 2"]','    loc --> z4["Z4: local rank and periods, 4"]',
               '    slope --> z5["Z5: determinants, 2"]']),
      "", "This diagram groups obligations by subject. Z2.K3 had already been discharged when the historical ledger opened. The ledger records local completion under the stated premises for fourteen of these twenty groups. These historical dispositions and current unit grades have different scopes.","",
      "| Original input | Mathematical question | Entry declarations | From / proof hops | Specialist units |","|---|---|---|---|---|"]
    all_paths={(e["from"],e["to"],len(e["lean_route"])-1) for e in graph["edges"] if e.get("lean_route")}
    for r in register["inputs"]:
        if [nodes[i]["name"] for i in r["root_ids"]]!=r["roots"] or any((r["via"],i,h) not in all_paths for i,h in zip(r["root_ids"],r["proof_hops"])):
            raise ValueError("Original input crosswalk does not match the paper graph: "+r["id"])
        text.append(f'| {r["id"]} | {r["title"]} | {", ".join(paper(i) for i in r["root_ids"])} | {paper(r["via"])} / {", ".join(map(str,r["proof_hops"]))} | {", ".join(unit(i) for i in r["unit_ids"])} |')
    kinds=Counter(e["relation"] for e in graph["edges"])
    text+=["","## 3. Inside the 775-node graph","",
      "The 140 P entries are the original paper skeleton. A first expansion adds the 10 B, 26 T and 16 W entries. The D register adds 583 further entries. The graph retains all 775 identities, including entries attached to another reading unit. The namespace lookup also covers blueprint chart suppliers, crosswalk support and starter packets. [775-node graph and paths](data/graph.json) · [Unit projection](data/unit_graph.json) · [Declaration lookup](lookup/declarations.md)","",
      mermaid(['    names["Original P declarations"] --> paperIndex["775-node paper index"]',
               '    split["B, T and W declarations"] --> paperIndex','    deep["D declarations"] --> paperIndex',
               '    paperIndex --> proof["Proof dependencies and compiled paths"]',
               '    paperIndex --> reading["Editorial reading groups"]',
               '    proof --> projection["Unit uses and used by"]']),
      "", f"Of the {len(graph['edges']):,} stored relations, {kinds['compiled_direct']} give direct compiled calls, {kinds['compiled_proof_route']} record compiled paths, and {kinds['skeleton_proof_dependency']} record identified skeleton dependencies. The other {kinds['decomposition_reading_group']+kinds['first_layer_reading_group']} group entries for reading. Multiple records can describe one pair. The separate unit survey includes longer paths between statement heads, with each hop checked against the compiled value. Its paths and object hashes are available in the [compiled-value evidence](data/unit_value_routes.json).",
      "", "For a concrete route, P023 reaches P022 through `Deduction.lemmaL`. The graph gives the intermediate Lean name. The unit page gives the hypotheses, proof location and review level. Dominated lines measure a different property of a larger graph that also follows types and constructors. [P023](units/P023.md) · [P022](units/P022.md) · [Dominator conventions](data/pins.json)"]
    return "\n".join(text)+"\n"


def shard(name):
    first=name.split(".",1)[0].casefold()
    return "a-f" if first<"g" else "g-l" if first<"m" else "m-t" if first<"u" else "u-z"
