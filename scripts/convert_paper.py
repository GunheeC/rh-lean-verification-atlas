#!/usr/bin/env python3
"""Import the reviewed paper map. Pass the project manuscript archive with --notes.

--capture-aux and --capture-overrides import the saved v3 build labels and v3
sources before the paused v4 edits. Normal runs use the frozen in-atlas extract.
The graph combines typed editorial relations; only edges marked proof_route
carry a dependency assertion. Dominator weights come from data/pins.json.
"""
import argparse
import collections
import hashlib
import json
from pathlib import Path
import re

from paper_formulas import FORMULAS

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
NOTICE = "AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved"
STAMP = "2026-11-24"
SHA = "40e56bab026552e089d7afcfeff08d2defb9c005"
V3 = "83af020c6a19b7ddba22d72bd6b27145cf957b0cb4eadc0e643ebff476b25898"

def read(p):
    return json.loads(p.read_text())

def save(p, data):
    p.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def index(rows):
    return {r["id"]: r for r in rows}

# These names are catalogue titles. The statements are imported separately.
DEEP = """002 galois | A global lattice index from local lengths
004 local | Norm bounds for the Wach lattice
006 local | Local Bloch–Kato, Tate and Euler identities
014 analytic | Inertia and Frobenius at exceptional host primes
024 theta | Unfolding a twisted theta integral
025 theta | A nonzero Bessel period
033 theta | Uniform row bounds from convergent Siegel–Weil
044 theta | Agreement of the square-model theta integrals
077 galois | Ordinary Eisenstein lifts at split primes
082 local | Restriction and the Bloch–Kato finite condition
097 local | The crystalline locus in the ordinary local deformation space
108 galois | Residual nonvanishing from a Bernoulli unit
123 arakelov | Arakelov degree of the normalized flat generator
128 theta | Integrality of the theta scalar on the integral models
154 arakelov | Hyperplane sections of the Chow form
155 arakelov | Fubini–Study normalization of Chow height
174 local | Characteristic polynomials in de Rham and étale realizations
193 local | The normalized flat model and universal isogeny
203 local | Fixed vectors over the de Rham period ring
230 local | Crystalline invariants over the maximal unramified extension
245 local | The period span of the positive Frobenius vector
302 local | Graded pieces of the crystalline filtration
309 local | The Hodge–Tate sequence from the Fargues exact sequence
317 arakelov | The intersection identity along the tower
331 arakelov | Integrability of the cusp weight
340 arakelov | Comparison of the period Gram matrices
351 arakelov | The Poincaré–Lelong identity
379 theta | Counting constants from Siegel–Weil
394 theta | Tying period entries to level valuations
415 theta | Injectivity of the adjoint theta scalar formula
421 galois | Uniform hub estimates for twist-good families
427 galois | The Selmer contribution to the lattice link
443 local | Flat degree and the Scholze–Weinstein input
479 arakelov | Global lattice compatibility of a family
481 arakelov | Divisibility of the closed bridge kernel
484 theta | The spectral link from the tuple-size bound
486 theta | Joined row counts and the irreducibility link
506 galois | The Borel injection in the cohomological comparison
510 analytic | A common quadratic host on a window
511 analytic | Host data from the chosen field
513 analytic | Choice of even column rank in a prescribed frame
528 galois | A single character from the Kato and rigidity inputs
532 galois | The first Selmer character count
536 galois | The pointwise window from a joint count
547 analytic | Identifying the host and level prime sums
548 analytic | Character shares on the retained cosets
549 analytic | The omitted-frequency correction
550 analytic | A common scale for logarithms and fixed constants
551 galois | Annihilation of the minus kernel
558 galois | Cyclotomic restriction on locally trivial Selmer classes
561 analytic | Orthogonality under the translate average
562 analytic | Increment bounds for smoothed character sums
563 analytic | Absorbing the four size-window errors
564 analytic | The bound for one character on the selected set
566 analytic | The equivalent clauses of a size window
567 arakelov | The per-unit lattice error and the arithmetic bracket
568 arakelov | A slope bound for the Gaussian term
569 arakelov | Transport of the main term across the finite bijections
570 arakelov | Upper bound for the weighted mean of lower slopes
575 galois | Green's parameterization of finite cuspidal characters"""
SUBJECT, EXTRA_TITLE = {}, {}
for row in DEEP.splitlines():
    tag, field, _, title = row.split(" ", 3)
    key = "D" + tag
    SUBJECT[key], EXTRA_TITLE[key] = field, title
P_FIELDS = {
    "formal": [1,2,3,4,5,6,7,8,9,10],
    "galois": [11,13,20,24,25,26,27,28,29,30,31],
    "analytic": [14,15,16,17,18,19,22,23],
    "arakelov": [21,49,50],
    "ktheory": [32,33,34,35,36,37,38,39],
    "local": [40,41,42,43,44,45],
    "theta": [12,46,47,48,90,96,134],
}
for field, ids in P_FIELDS.items():
    for num in ids:
        SUBJECT[f"P{num:03d}"] = field
for pre, fields in {
    "B": "theta galois galois local arakelov theta analytic analytic analytic arakelov",
    "T": "theta arakelov theta theta analytic theta local theta theta theta theta theta arakelov arakelov arakelov arakelov arakelov arakelov arakelov arakelov arakelov arakelov arakelov local local arakelov",
    "W": "galois theta galois theta galois galois galois galois galois galois galois galois galois galois galois galois",
}.items():
    for i, field in enumerate(fields.split(), 1):
        SUBJECT[f"{pre}{i:02d}"] = field
assert len(SUBJECT) == 165
SECONDARY = {
    "analytic": "P001 P002 P003 P004 P005 P007 P008 P009 P010 P013 P020 B10 W12 D033 D486",
    "galois": "P012 P014 P015 P016 P017 B05 B07 T01 T02 T24 D002 D004 D006 D014 D097 D510 D511",
    "arakelov": "P017 B08 B09 P046 P047 T03 T09 T10 D128 D561 D563",
    "local": "P025 P026 P027 W05 W06 W07 W11 D077 D108 D421 D427 D551",
    "theta": "P011 B02 B05 D123 D155 D331 D340 T13 T14",
    "ktheory": "P031 P040 W11",
}
def tex_body(tex_root, overrides, aux):
    labels = {m[1]: {"number": m[2], "page": int(m[3])}
              for m in re.finditer(r"\\newlabel\{(?:pn|sub|decomp):([PTBWD]\d+)\}\{\{([^}]+)\}\{(\d+)\}", aux.read_text())}
    entries = {}
    for src in sorted(tex_root.glob("*.tex")):
        origin = overrides/src.name if (overrides/src.name).exists() else src
        tex = origin.read_text()
        for m in re.finditer(r"\\begin\{(formalstatement|proposition|theorem|lemma|corollary)\}(.*?)\\end\{\1\}", tex,re.S):
            loc = re.search(r"\\label\{(pn|sub|decomp):([A-Z]\d+)\}",m[2])
            if not loc: continue
            key=loc[2]
            if loc[1]=="decomp" and key in entries: continue
            body = m[2][loc.end():].strip()
            body = re.sub(r"\\label\{[^}]+\}", "", body).strip()
            if not body: raise ValueError(key)
            # Start page is for the label in the chosen statement, not another
            # appearance of the same ID in the decomposition appendix.
            l = re.search(r"\\newlabel\{"+loc[1]+":"+key+r"\}\{\{([^}]+)\}\{(\d+)\}", aux.read_text())
            if not l: raise ValueError((key,origin))
            entries[key]={"source_file": "paper2/"+src.name, "tex_label":loc[1]+":"+key,
                          "number":l[1],"page":int(l[2]),"statement":body}
    if len(entries) != 775:
        raise ValueError(("v3 label count",len(entries),sorted(set(labels)-set(entries))))
    return entries

def build(notes, frozen, grades):
    origin = notes/"out"
    files = ["R19_skeleton","R20_dispositions","R21_parent_status","R21_split_nodes",
             "R22_decomposition","R22_graph_weights","R23_pending"]
    src = {k:read(origin/f"{k}.json") for k in files}
    parents=index(src["R21_parent_status"]["nodes"])
    prose=index(src["R20_dispositions"]["nodes"])
    splits=index(src["R21_split_nodes"]["nodes"])
    leaves=index(src["R22_decomposition"]["nodes"])
    original={**parents,**splits,**leaves}
    byname={r["name"]:k for k,r in original.items()}
    pins=read(DATA/"pins.json")["anchors"]
    if len(original)!=len(byname) or len(original)!=775 or set(original)!=set(frozen):
        raise ValueError("Nonunique paper IDs or mismatched v3 corpus")
    note_index = read(DATA/"notes_units.json")["units"]
    rows={}
    direct=collections.defaultdict(set)
    nav=collections.defaultdict(set)
    edges=[]
    unique=set()
    def edge(a,b,kind,path=()):
        if a==b or (a,b,kind) in unique: return
        if a not in original or b not in original: raise ValueError((a,b))
        unique.add((a,b,kind))
        e={"from":a,"to":b,"relation":kind}
        if path: e["lean_route"]=path
        edges.append(e)
        nav[a].add(b)
        if kind in ("skeleton_proof_dependency","compiled_proof_route","compiled_direct"):
            direct[a].add(b)
    for key, r in parents.items():
        for sub in r["indexed_proof_dependencies"]:
            edge(key,sub,"skeleton_proof_dependency")
    for row in src["R19_skeleton"]["graph"]["witness_paths"]:
        if row["from"] in byname and row["to"] in byname:
            edge(byname[row["from"]],byname[row["to"]],"compiled_proof_route",row["path"])
    for key,r in splits.items():
        edge(r["parent"],key,"first_layer_reading_group")
    for row in src["R22_decomposition"]["edges"]:
        # These are separately checked compiled value paths. Preserve intermediate names.
        edge(byname[row["from"]],byname[row["to"]],
             "compiled_direct" if len(row["path"])==2 else "compiled_proof_route",row["path"])
    for k,r in leaves.items():
        for p in r["presentation_parents"]: edge(byname[p],k,"decomposition_reading_group")
    # Map omitted subdeclarations to the nearest primary along an actual inventory
    # edge. A path is labelled editorial whenever it crosses an editorial edge.
    owner={k:k for k in SUBJECT}
    routes={k:[k] for k in SUBJECT}
    queue=collections.deque(sorted(SUBJECT))
    while queue:
        p=queue.popleft()
        for k in sorted(nav[p]):
            if k not in owner:
                owner[k]=owner[p];routes[k]=routes[p]+[k];queue.append(k)
    for k,r in original.items():
        pin=pins[r["name"]]
        paper=frozen[k]
        source=r["source"]
        if (pin["file"],pin["line0"],pin["line1"],pin["sha256"])!=(source['file'],source['line0'],source['line1'],source.get('sha256',source.get('sha256_source_span'))):
            raise ValueError(("pin mismatch",k))
        disp=leaves.get(k,{}).get("disposition",parents.get(k,splits.get(k,{})).get("status"))
        unit=owner.get(k)
        if k in SUBJECT: role="primary"
        elif unit and disp=="Routine assembly": role="attached_assembly"
        elif unit: role="indexed_under_unit"
        else: role="cross_index_only"
        rows[k]={"id":k,"name":r["name"],"unit_id":unit,"assignment":role,
                 "reading_path":routes.get(k,[]),"edition_label":paper['tex_label'],
                 "edition_locator":paper['number'],"start_page":paper['page'],
                 "source_disposition":disp,"source":pin}
        if k not in owner:rows[k]['mapping_reason']="Outside the indexed paths from the selected stations; preserved for independent lookup."
        if k in leaves: rows[k]["round22_accounting"]= {key:v for key,v in leaves[k]["weights"].items() if key in ("inclusive","assigned","dominated","owner","residual_all","reached")}
    graph={"notice":NOTICE,"source_commit":SHA,"paper_edition":"paper2_v3",
           "paper_pdf_sha256":V3,"anchors":"data/pins.json",
           "roots":{"r19_public_ids":[f"P{i:03d}" for i in range(1,6)],"r22_dominator_root":"allChi","r22_root_id":"P009"},
           "sources":{f"out/{f}.json":sha(origin/f"{f}.json") for f in files},
           "accounting":"All 775 distinct paper IDs are retained. Global dominators and graph roots in the pin registry are not wrapper charges or disjoint reading costs. Reading paths are editorial assignments, not logical implication chains. A chapter grade applies only to its primary declaration.",
           "assembly_policy":"Project-specific claims are indexed under the nearest selected station. An omitted node is tagged attached_assembly only when its R22 disposition is Routine assembly. Ties between equally short indexed paths use stable ID order.",
           "nodes":[rows[k] for k in sorted(rows)],"edges":edges}
    save(DATA/"graph.json",graph)
    lookup=collections.defaultdict(list)
    for r in grades:
        for decl in r["declarations"]: lookup[decl].append(r)
    for k,primary in SUBJECT.items():
        r=original[k]; p=frozen[k]; declaration=r["name"]
        title=EXTRA_TITLE.get(k) or prose.get(k,{}).get('title_tex') or splits[k]["title"]
        status={"Proved here (full)":"Full","Outlined (proof in Blueprint/Lean)":"Outlined"}.get(parents.get(k,{}).get("status"),"Statement only")
        if k in ("P012","P013","P015","P017","B05","B07","B08","B09","B10","T02","T13","T14","D561"):status="Outlined"
        if k in ("D563","D564","P096","P134"):status="Full"
        reviews=sorted(lookup[declaration],key=lambda r:int(r["grade"][1]),reverse=True)
        grade="L0"
        for record in reviews:
            level = min(int(record["grade"][1]),2 if status=="Full" else 1)
            if level>int(grade[1]):grade=f"L{level}"
        secondary=[t for t,keys in SECONDARY.items() if k in keys.split() and t!=primary]
        paper={"document":"paper2_v3","section":p['number']+" ("+p['tex_label']+")",
               "pages":[p['page'],p['page']],"coverage":"Statement starts on the cited page."}
        notespath=f"notes/units/{k}.tex"
        expositions=[paper,{"document":notespath,"section":p["tex_label"],"pages":[]}]
        size=None
        for round_key, ids in {"P017":"P017 B08 B09 B10 D561 D563 D564 D567 D569", "LinkN_at":"P021 D427","P015":"P015 B05 B07 D510 D511 D513", "P013":"P013 W01 W08 W09 W10", "P012":"P012 T02 T13 T14"}.items():
            if k not in ids.split(): continue
            candidate=next((row for row in src["R23_pending"].get("chain",src["R23_pending"].get("stages",[])) if row.get("stage")==round_key),None)
            if candidate:
                expositions.append({"document":"paper2_v3","section":"The chain in detail: "+round_key,"pages":candidate["pages"],"coverage":"Shared subsection for this station, including subordinate inputs."})
                if k==round_key or (k=="P021" and round_key=="LinkN_at"):
                    size=candidate["pages"][1]-candidate["pages"][0]+1
        if k == "P022":
            expositions.append({"document":"paper2_v3","section":"Theorem 6.23 and its proof after Lemma 6.28","pages":[61,65],"coverage":"Statement, analytic lemmas and conclusion in the abstract-statement subsection."})
            size=5
        if k == "D563":
            expositions.append({"document":"paper2_v3","section":"Lemma 3.4 (r23:budget)","pages":[13,13],"coverage":"Complete four-term division and absorption argument."})
            size=1
        supplement = note_index[k].get("additional_exposition")
        if supplement:
            supplement_label = {"D563":"r23:budget","P017":"r23:p017","P021":"r23:link","P015":"r23:host"}.get(k)
            expositions.append({"document":supplement["path"],"section":supplement_label or "Written argument for "+k,"pages":[]})
        partial_crosswalks = {"T14":"H15.69 · Hypothesis 15.69 (target DeepStR only)",
                              "W05":"B-effective · §17.4.3, tw:effectiveK (target LemmaK only)"}
        if k in partial_crosswalks:
            expositions.append({"document":"crosswalk/adriazola.json","section":partial_crosswalks[k],"pages":[],
                                "coverage":"Target predicate only. The local implication has additional hypotheses."})
        statement=p["statement"]
        if k in FORMULAS:
            statement += "\n\\[\n"+FORMULAS[k]+"\n\\]"
        hypothesis_details={"document":"paper2_v3","label":p["tex_label"],"number":p["number"],"page":p["page"],
                            "statement_with_quantifiers":p["statement"],"formal_declaration":declaration,
                            "reference_index":"data/paper_v3_labels.json"}
        evidence=[{"grade":e["grade"],"review":e["review"],"lines":e["lines"],"scope":e["scope"],
                   "verdict":e["verdict"]} for e in reviews]
        refs=sorted(set(e["review"] for e in reviews))
        d=[sub for sub in sorted(direct[k]) if sub in SUBJECT]
        # Direct proof suppliers are navigation prerequisites, not automatically
        # antecedents of the mathematical implication.
        if grade=="L0": question="Compare the displayed statement and its quantified hypotheses with the pinned declaration."
        elif status=="Full" and grade=="L2": question="Independently check the written derivation at the stated hypotheses and record the scope of any human review."
        elif status=="Full": question="Check the complete written argument independently, including the local hypotheses at each use."
        elif status=="Outlined": question="Check the outlined steps against the named lower inputs and identify which still require a written proof."
        else: question="Determine whether the pinned statement has a written derivation under exactly these hypotheses."
        if k=="P017":question="Supply the balance identity, the width Lipschitz estimate and the thick-place identification identified in the v3 referee report §1.4."
        attached=[nk for nk in sorted(rows) if nk!=k and rows[nk]["unit_id"]==k]
        unit={"notice":NOTICE,"id":k,"title":title,"track":{"primary":primary,"secondary":secondary},"statement":statement,
              "assumptions":["source:paper2_v3"],"hypothesis_details":hypothesis_details,"lean":[pins[declaration]],"expositions":expositions,
              "status":status,"grade":grade,"reviews":refs,"prerequisites":d,"size_pages":size,"open_questions":[question],
              "last_checked":STAMP,"grade_evidence":evidence,"paper_id":k,"indexed_members":attached,
              "scope":"The exposition, grade and proof status cover the anchor at its own hypotheses. Indexed members have their own pins and retain their source dispositions."}
        save(ROOT/"units"/f"{k}.yaml",unit)
    print("165 paper stations",collections.Counter(r["assignment"] for r in rows.values()),"edges",len(edges))

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--notes",type=Path,required=True)
    parser.add_argument("--capture-aux",type=Path)
    parser.add_argument("--capture-overrides",type=Path)
    args=parser.parse_args()
    frozen=DATA/"paper_v3_statements.json"
    if args.capture_aux:
        pdf=args.capture_aux.with_suffix(".pdf")
        if sha(pdf)!=V3: raise ValueError("Auxiliary does not sit beside verified v3 PDF")
        aux=args.capture_aux.read_text()
        refs = {m[1]:{"section":m[2],"page":int(m[3])} for m in re.finditer(
            r"(?m)^\\newlabel\{([^}]+)\}\{\{([^}]+)\}\{(\d+)\}", aux)}
        save(DATA/"paper_v3_labels.json",{"notice":NOTICE,"edition":"paper2_v3","aux_sha256":sha(args.capture_aux),"labels":refs})
        entries=tex_body(args.notes/"paper2",args.capture_overrides,args.capture_aux)
        save(frozen,{"notice":NOTICE,"edition":"paper2_v3","source_pdf_sha256":V3,
                     "aux_sha256":sha(args.capture_aux),"entries":entries})
    pages=read(frozen)["entries"]
    build(args.notes,pages,read(DATA/"grade_evidence.json")["records"])
if __name__=="__main__":
    main()
