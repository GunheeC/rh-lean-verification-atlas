#!/usr/bin/env python3
"""Extract declaration-scoped AI verdicts from the archived review text and registers."""
import argparse
import hashlib
import json
import re
from pathlib import Path


def load(path):
    return json.loads(path.read_text())


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--notes", required=True, type=Path)
    p.add_argument("--data", type=Path, default=Path(__file__).resolve().parents[1] / "data")
    a = p.parse_args()
    out = a.notes / "out"
    status = load(a.notes / "blueprint/status.json")
    pins = load(a.data / "pins.json")["anchors"]
    paper = {r["id"]:r["name"] for r in load(out/"R21_parent_status.json")["nodes"]}
    records = []
    def add(names,unit,grade,review,start,end,verdict,scope):
        path = out / (review+".md")
        assert 1 <= start <= end <= len(path.read_text().splitlines())
        assert all(n in pins for n in names), names
        records.append(dict(declarations=names,legacy_unit=unit,grade=grade,
            review="reviews/"+path.name,source_review="out/"+path.name,lines=[start,end],
            source_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),verdict=verdict,scope=scope))
    for name in ("R5_review_A","R5_review_B","R5_review_C","R6_review","R7_review"):
        for i,line in enumerate((out/(name+".md")).read_text().splitlines(),1):
            m = re.match(r"^\| (Z[\d.K]+) \|",line)
            if not m or m[1] not in status["units"]:
                continue
            unit=m[1]
            good="COMPLETE CONFIRMED" in line
            match="statement faithful" in line or good
            if not match:
                continue
            ns=[r["name"] for r in status["units"][unit]["roots"]]
            add(ns,unit,"L2" if good else "L1",name,i,i,
                "COMPLETE CONFIRMED" if good else "Statement faithful; gaps in proof",
                "Exactly the named unit at the hypotheses reviewed in the cited row.")
    for u,rev,lo,hi in [("Z2.K7","R4_review_Z2",91,123),("Z4.2.04","R17_review",34,38)]:
        add([r["name"] for r in status["units"][u]["roots"]],u,"L2",rev,lo,hi,
            "COMPLETE CONFIRMED" if u=="Z2.K7" else "An AI review reports: unconditional completion confirmed",
            "Named unit conclusion. Its lower suppliers keep their own individual verdicts.")
    add([r["name"] for r in status["units"]["Z1.5.07"]["roots"]],"Z1.5.07","L2","R6_review",218,218,
        "Only R5 gap explicitly fixed and independently rechecked","At the pre-existing CountKAlt hypothesis; the closure concerns the B_cris step named in R5_review_A.")
    assert status["round14"]["approval"]["after_edits"]=="approved"
    add([r["name"] for r in status["units"]["Z4.4"]["roots"]],"Z4.4","L2","R14_review_B",348,353,
        "R13 conditional approval followed by applied edits and R14 independent acceptance of the recorded grade",
        "Root hand proof under its stated inputs, per R13_recheck.md:188, blueprint/status.json round14.approval and this recheck; individual suppliers evaluated separately.")
    def labels_in_text(row,review):
        n=row["name"]; name=n.split(".")[-1]
        lines=(out/(review+".md")).read_text().splitlines()
        verdict=row.get("independent_verdict",row.get("original_review_verdict",""))
        if not verdict.startswith("CONFIRMED"):
            return
        pat=re.compile(r"(?<![a-zA-Z0-9_'])"+re.escape(name)+r"(?![a-zA-Z0-9_'])")
        candidates=[i for i,l in enumerate(lines,1) if l.startswith("|") and pat.search(l) and verdict in l]
        if not candidates:
            return
        # A matching table row, not acceptance of the complete enclosing unit.
        spellings=[".".join(n.split(".")[j:]) for j in range(len(n.split(".")))]
        ranks={i:max((len(s) for s in spellings if s in lines[i-1]),default=0) for i in candidates}
        winners=[i for i in candidates if ranks[i]==max(ranks.values())]
        if len(winners)>1 and not ranks[winners[0]]>len(name):
            return
        i=winners[0]
        if n not in pins:
            return
        strong=verdict=="CONFIRMED" and "CONFIRMED WITH GAP" not in lines[i-1]
        add([n],row.get("unit"),"L2" if strong else "L1",review,i,i,verdict,
            "Only this declaration's hand derivation under the reviewed hypotheses."
            if strong else "Declaration-level statement comparison only; proof qualifications remain.")
    for row in status["round11"]["subtheorems"]:
        labels_in_text(row,"R11_review")
    for row in status["round12"]["subtheorems"]:
        labels_in_text(row,"R12_review_"+row["review"])
    for round_num in (14,15,16):
        for row in load(out/("R%d_pending.json"%round_num))["new_declarations"]:
            review=row.get("review",{}).get("source")
            if review:
                labels_in_text(row,Path(review).stem)
    add(["GlobalTheory.TransDual.nabDelDual"],"Z4.4","L2","R13_recheck",168,168,
        "A1 checked in full","Transported Hermitian duality only; no other new R13 entry is included.")
    for i,line in enumerate((out/"R20_review.md").read_text().splitlines(),1):
        cells=[x.strip() for x in line.strip("|").split("|")]
        if 45<i<73 and re.fullmatch("P[0-9]{3}",cells[0]) and len(cells)>=5:
            key=cells[0]
            strong=cells[2]=="F" and "Yes" in cells[3] and "not unfolded" not in cells[4]
            if strong or "exact" in cells[4]:
                add([paper[key]],key,"L2" if strong else "L1","R20_review",i,i,
                    "F: full derivation; yes" if strong else "Statement exact",
                    "R20 local implication under its stated premises, not its prerequisite cones.")
        if 96<=i<=117 and "exact" in cells[-1] and line.startswith("|"):
            ids=re.findall(r"P\d{3}",cells[0])
            if "P014–P016" in cells[0]:
                ids=["P014","P015","P016"]
            for key in ids:
                add([paper[key]],key,"L1","R20_review",i,i,"Exact statement comparison","Named theorem at the specified hypotheses in the R20 manuscript.")
    add([paper["P021"]],"P021","L2","R23_review",120,136,
        "CORRECT AND COMPLETE under displayed hypotheses",
        "Only the per-unit ASK inequality from all eleven hypotheses.")
    add([paper["P017"]],"P017","L1","R23_review",27,88,
        "CORRECT WITH GAPS","R23 window theorem; exact conditional statement, no approval of its lower proof suppliers.")
    for key,lo,hi in [("P096",417,432),("P134",433,448)]:
        add([paper[key]],key,"L1","R21_review",lo,hi,"Statement compared; later candidate recheck reserved",
            "Statement-level verdict only; no completion of other segments in the same legacy unit.")
    splits={r["id"]:r["name"] for r in load(out/"R21_split_nodes.json")["nodes"]}
    checked = [91,92,93,104,108,109,116,117,118,127,128,129,130,131,132,133,135,136,137]
    r21=(out/"R21_review.md").read_text().splitlines()
    for number in checked:
        key=r21[number-1].split("|")[1].split()[0]
        assert "exact" in r21[number-1].lower()
        add([splits[key]],key,"L1","R21_review",number,number,
            "Exact statement comparison","Lean interface as specified in the review row; no equivalence with a published result inferred.")
    add(["Formalism.LFunctionChainParameters.ThickSetMeanBounds.proposition_size_bound"],"D563","L2",
        "R23_review",61,67,"Seven steps rederived, each marked correct",
        "Only the numerical size bound of v3 Lemma 3.4, at its stated inequalities; use with its hand exposition and not as approval of P017.")
    for u,rev,lo,hi in [("Z2.K4","R5_review_A",10,12),("Z2.K2","R4_review_Z2",12,16),("Z4.1","R4_review_Z4",149,159),("Z1.4","R4_review_Z1Z3",43,50)]:
        add([r["name"] for r in status["units"][u]["roots"]],u,"L1",rev,lo,hi,"No statement mismatch reported","Statement comparison; the proof has qualifications.")
    data=dict(method="Each record cites lines in source_review (relative to the historical notes), available via the local provenance card in review. Verdict applies only to the listed declaration(s) and stated scope. L2 requires a corresponding full exposition. No grade propagates along a dependency edge or to other anchors. Absence is not a negative verdict.",
        external_correspondence_policy="Crosswalk rows are bibliographic or statement locators and confer no unit grade.",
        records=records)
    f=a.data/"grade_evidence.json"
    # Source rebuilds of the pre-atlas ledger preserve later edition-specific referee records.
    if f.is_file():
        current = load(f)
        data.update({k:v for k,v in current.items() if k not in {"method", "records"}})
        data["records"].extend(r for r in current.get("records", []) if r.get("note") and r.get("reviewed_sha256"))
    tmp=f.with_suffix(".partial");tmp.write_text(json.dumps(data,ensure_ascii=False,indent=2)+"\n");tmp.replace(f)
    from collections import Counter
    print(Counter(x["grade"] for x in records),"records for",len({n for x in records for n in x["declarations"]}),"declarations")

if __name__=="__main__":
    main()
