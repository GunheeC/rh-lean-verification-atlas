#!/usr/bin/env python3
"""Export blueprint assignments, readable excerpts and field-specific entry points."""
import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path
import re

BANNER = "AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved"
LABEL = re.compile(r"\\label\{([^{}]+)\}")
HEADING = re.compile(r"^\s*\\(section|subsection|subsubsection|paragraph|subparagraph)\*?\{")
LEVEL = {"section": 0, "subsection": 1, "subsubsection": 2, "paragraph": 3, "subparagraph": 4}
ENV = re.compile(r"^\s*\\begin\{(lemma|theorem|proposition|corollary)\}")
GROUPS = {
    "Z42-SITES": "Served-site parameters and the lattice dictionary",
    "Z42-FRAMES": "Translation, away comparison and arithmetic scalars",
    "Z42-KERNEL": "Transformation and level changes of the kernel",
}
TRACKS = {
    "Analytic number theory": "analytic", "Arakelov geometry": "arakelov",
    "Automorphic forms and theta": "theta", "Galois deformation theory": "galois",
    "Algebraic K-theory": "ktheory",
}
LOCAL = {"Z4.1", "Z42-SITES", "Z4.2.02", "Z42-FRAMES"}
EXTRA_LABELS = {
    "Z4.2.04": ["r15:translated", "r15:pair", "r16:stdok", "r16:ktheta"],
    "Z4.4": ["r11:z44", "r11:fock", "r12:assembly", "r13:recheck"],
    "Z4.1": ["sec:P-r4-z41-kernel"],
    "Z1.2": ["r11:adj"],
    "Z2.K4": ["sec:P-r5-k4"],
    "Z1.4": ["sec:P-z14-full"],
    "Z2.K2": ["prop:P-k-few"],
    "Z2.K7": ["prop:P-k-num"],
}
# Pedagogical reading order. Formal antecedents and open suppliers are separate fields.
READ_BEFORE = {
    "Z1.5.02": ["Z1.5.01"], "Z1.5.03": ["Z1.5.02"], "Z1.5.04": ["Z1.5.02"],
    "Z1.5.05": ["Z1.5.04"], "Z5.2": ["Z5.1"], "Z4.2.02": ["Z42-SITES"],
    "Z4.2.04": ["Z42-SITES"], "Z42-FRAMES": ["Z4.2.02", "Z4.2.04"],
    "Z42-KERNEL": ["Z4.2.02", "Z4.2.04", "Z4.2.13", "Z42-FRAMES"],
    "Z4.3": ["Z4.1", "Z42-KERNEL"], "Z4.4": ["Z42-SITES"],
    "Z1.1.02": ["Z1.1.01"], "Z1.1.03": ["Z1.1.02"], "Z1.1.05": ["Z1.1.04"],
    "Z1.1.06": ["Z1.1.05"], "Z1.1.07": ["Z1.1.05", "Z1.1.06"],
    "Z1.3.04": ["Z1.3.01", "Z1.3.02", "Z1.3.03"], "Z1.3.05": ["Z1.3.04"],
    "Z1.3.07": ["Z1.3.06"], "Z1.3.08": ["Z1.3.04", "Z1.3.05", "Z1.3.07"],
    "Z2.K6": ["Z2.K1", "Z2.K5"], "Z3.2": ["Z3.1"],
}
REVIEW_CONTEXT = {
    "Z4.2.04": ["R14_review_B", "R15_review_A", "R16_review_A", "R17_review"],
    "Z4.4": ["R11_review", "R12_review_A", "R12_review_B", "R13_recheck", "R14_review_B"],
    "Z4.2.13": ["R14_review_A", "R15_review_A"], "Z4.3": ["R4_review_Z4", "R14_review_B", "R15_review_B"],
    "Z4.1": ["R4_review_Z4"], "Z4.2.02": ["R7_review", "R8_review"], "Z42-KERNEL": ["R7_review", "R8_review"],
    "Z1.2": ["R5_review_C", "R11_review"], "Z1.4": ["R4_review_Z1Z3"], "Z3.2": ["R4_review_Z1Z3"],
    "Z2.K2": ["R4_review_Z2"], "Z2.K4": ["R5_review_A", "R6_review"],
    "Z1.5.07": ["R5_review_A", "R6_review"], "Z42-FRAMES": ["R6_review", "R7_review", "R8_review"],
}
DIRECT_INPUTS = {
    "Z42-FRAMES": ["Z4.2.04"],
    "Z1.1.06": ["Z1.1.05"],
    "Z1.3.04": ["Z1.3.01", "Z1.3.02", "Z1.3.03"],
    "Z1.3.07": ["Z1.3.06"],
}
STATEMENTS = {
    "Z1.5.04": r"Assume the automorphic hypotheses and $\mathrm{LevelPNAlt}$. For each imaginary quadratic field $K$ and $n\ge2$ there are $c,A$ such that for all strictly decreasing weights $m$ with $|m_i|\le H$ and $m_i+m_{\mathrm{rev}(i)}=\mathrm{wt}$, levels $M\ge1$ and places $w\mid p$ with $p\nmid M\,\mathrm{disc}(K)$, there is a single Frobenius classifier $D$ over $w$ of size at most $c[M(H+1)]^A$ for every allowed $\mathrm{AdmPNAlt}$ system at every odd coefficient prime $\ell\ne p$.",
    "Z1.3.05": r"Fix the coefficient ring, cocycle $y$, exceptional primes, twist, test characters and cyclotomic layers of an ordinary normal form. If the same tuple satisfies $\mathrm{Sys}$, $\mathrm{IwSys2}$, $\mathrm{SpLink}$ and $\mathrm{Pin7}$, some inertia element with trivial cyclotomic action and lower diagonal entry $1$ has nonzero second coordinate under $y$.",
}
SECONDARY = {
    "Z2.K5": ["ktheory", "galois"], "Z2.K1": ["ktheory"], "Z2.K6": ["ktheory"], "Z2.K8": ["ktheory"],
    "N188": ["arakelov"], "N318": ["local"], "Z4.2.13": ["local"], "Z4.2.04": ["local"],
    "Z4.3": ["local"], "Z4.4": ["local"], "Z42-KERNEL": ["local"], "Z1.2": ["local"],
    "Z1.3.02": ["local"], "Z1.3.05": ["local"], "Z3.2": ["local"],
}

def read(path):
    return json.loads(path.read_text(encoding="utf-8"))

def save(path, obj):
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

def unique(values):
    return list(dict.fromkeys(values))

class SourceIndex:
    def __init__(self, project):
        self.project = project
        self.files = {}
        self.labels = {}
        self.pages = {}
        for file in sorted((project / "blueprint").glob("*.tex")):
            if file.name.startswith("handoff"):
                continue
            lines = file.read_text(encoding="utf-8").splitlines()
            self.files[file] = lines
            for index, line in enumerate(lines):
                for label in LABEL.findall(line):
                    self.labels[label] = file, index
        page_map = (project / "blueprint/handoff_pages.tex").read_text(encoding="utf-8")
        for lab, printed, physical in re.findall(r"BPpage:(.*?)\\endcsname\{\\bp\{(\d+)\}\{(\d+)\}\}", page_map):
            self.pages[lab] = int(printed), int(physical)

    def block(self, lab):
        """Return a whole heading, or one stated theorem and its following proof."""
        file, index = self.labels[lab]
        lines = self.files[file]
        start = index
        # Source labels often follow a heading or a one-line theorem opener.
        if start and (HEADING.match(lines[start - 1]) or ENV.match(lines[start - 1])) and not (HEADING.match(lines[start]) or ENV.match(lines[start])):
            start -= 1
        env = ENV.match(lines[start])
        heading = HEADING.match(lines[start])
        if env:
            for j in range(index + 1, len(lines)):
                if r"\end{proof}" in lines[j]:
                    return file, start, j + 1
                if HEADING.match(lines[j]) or ENV.match(lines[j]):
                    return file, start, j
        end = len(lines)
        for j in range(index+1, len(lines)):
            nxt = HEADING.match(lines[j])
            if nxt and (heading is None or LEVEL[nxt[1]] <= LEVEL[heading[1]]):
                end = j
                break
            if lines[j].startswith(r"\phantomsection\label{r6:review:") and not nxt:
                end = j
                break
            if lines[j].lstrip().startswith((r"\input{", r"\end{document}")):
                end = j
                break
        while end > start+1 and not lines[end-1].strip():
            end -= 1
        return file, start, end

def passage_labels(uid, experts, ledger, charts, index):
    labels = []
    for member in experts:
        canonical = ledger[member]["proof_label"]
        for candidate in ("r5:"+member, "r5:small:"+member, "r6:"+member, "r6:review:"+member):
            if candidate in index.labels:
                labels.append(candidate)
        labels.extend(EXTRA_LABELS.get(member, []))
        for c in charts.get(member, {}).values():
            if c["proof_label"]:
                labels.append(c["proof_label"])
        labels.append(canonical)
    return unique(labels)

def make_note(uid, labels, index, notes, ranks):
    # Store each source interval once even when both a subsection and a nested lemma are cited.
    pieces = defaultdict(list)
    locators = []
    for label in labels:
        file, first, end = index.block(label)
        pieces[file].append((first, end, label))
        source_rel = file.relative_to(index.project).as_posix()
        passage = {"label": label, "source": source_rel, "start": first+1, "end": end}
        if label in index.pages:
            printed, physical = index.pages[label]
            passage.update(v13_printed_page=printed, v13_pdf_page=physical)
        locators.append(passage)
    out = ["% "+BANNER, "% RH Notes blueprint source excerpts for "+uid,
           "% Verbatim excerpts in the notation of the parent blueprint. The labelled editions and source ranges appear below.",
           "% See the unit YAML for the current proof status. Earlier-round passages retain their original wording.",
           r"\section*{"+uid+". "+ranks+"}", ""]
    for file, intervals in pieces.items():
        source_rel = file.relative_to(index.project).as_posix()
        out.append("% Parent source SHA-256: "+hashlib.sha256(file.read_bytes()).hexdigest())
        merged = []
        for first, end, label in sorted(intervals):
            if merged and first < merged[-1][1]:
                merged[-1][1] = max(end, merged[-1][1])
                merged[-1][2].append(label)
            else:
                merged.append([first,end,[label]])
        for first, end, labs in merged:
            out.extend(["% "+source_rel+" lines "+str(first+1)+" through "+str(end)+"; "+", ".join(labs)])
            out.extend(index.files[file][first:end])
            out.append("")
    (notes / (uid+".tex")).write_text("\n".join(out)+"\n", encoding="utf-8")
    return locators

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--notes",type=Path,required=True,help="project manuscript archive")
    parser.add_argument("--atlas",type=Path,default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    atlas, project = args.atlas.resolve(), args.notes.resolve()
    notes = atlas / "notes/blueprint"
    notes.mkdir(parents=True, exist_ok=True)
    data = atlas / "data"
    original = read(project / "blueprint/status.json")["units"]
    membership = read(data / "blueprint_membership.json")
    antecedents = read(data / "blueprint_reading_inputs.json")
    charts = read(data / "blueprint_chart_members.json")
    pins = read(data / "pins.json")["anchors"]
    reviewed = read(data / "grade_evidence.json")["records"]
    assert set(original) == set(membership) == set(antecedents) and len(original)==55
    groups = defaultdict(list)
    for member, group in membership.items():
        groups[group].append(member)
    index = SourceIndex(project)
    excerpts = {}
    for uid, members in groups.items():
        v = original[members[0]]
        title = GROUPS.get(uid, v["title"])
        names = unique(n["name"] for m in members for n in original[m]["roots"])
        chart_names = unique(n for m in members for n in charts.get(m, {}))
        lean = [{**pins[n], "role": "statement" if n in names else "chart supplier"} for n in unique(names+chart_names)]
        labels = passage_labels(uid, members, original, charts, index)
        excerpts[uid] = make_note(uid, labels, index, notes, title)
        conditional = [original[m]["conditional_completion"] for m in members if original[m].get("conditional_completion")]
        assumed = unique(membership[k] for c in conditional for k in c["open_units"] if membership[k]!=uid)
        assumed = unique(assumed + DIRECT_INPUTS.get(uid, []))
        hypotheses = [a for m in members for a in antecedents[m]]
        status = "Full" if all(original[m]["status"]=="complete" for m in members) else "Outlined"
        primary = "local" if uid in LOCAL else TRACKS[v["specialty"]]
        if uid.startswith("Z1.5"):
            secondary = ["galois"]
        elif uid in LOCAL:
            secondary = ["theta"]
        else:
            secondary = SECONDARY.get(uid, [])
        statements = [STATEMENTS.get(m, original[m]["statement"]) for m in members]
        if len(members)>1:
            statements = [r"\textbf{"+m+r".} "+s for m,s in zip(members, statements)]
        records = [r for r in reviewed if set(r["declarations"]) & set(names)]
        highest = []
        for n in names:
            allowed = [int(r["grade"][1:]) for r in records if n in r["declarations"] and r["legacy_unit"] in members]
            highest.append(max([0]+allowed))
        level = min([2 if status=="Full" else 1]+highest)
        reviews = unique(["reviews/"+s+".md" for s in REVIEW_CONTEXT.get(uid, [])]+[r["review"] for r in records])
        st = " ".join(statements)
        questions = unique(original[m]["remaining_input"].strip() for m in members if original[m]["remaining_input"].strip())
        expositions = [{"document":"notes/blueprint/"+uid+".tex","section":", ".join(labels),"pages":[]}]
        for row in excerpts[uid]:
            if "v13_pdf_page" in row:
                p = row["v13_pdf_page"]
                expositions.append({"document":"blueprint_v13","section":row["label"],"pages":[p,p],
                        "printed_page":row["v13_printed_page"],"scope":"First page of this named destination."})
        assert any(e["document"]=="blueprint_v13" for e in expositions)
        u = {
            "id":uid, "title":title,"track":{"primary":primary,"secondary":secondary},"statement":st,
            "assumptions":assumed+["source:blueprint_v13"],"hypothesis_details":hypotheses,"lean":lean,"expositions":expositions,
            "status":status,"grade":"L"+str(level),"reviews":reviews,
            "prerequisites":unique(READ_BEFORE.get(uid,[])+assumed),"size_pages":None,
            "open_questions":questions,"last_checked":"2026-11-24",
            "blueprint_members":members,"representative":names[0],"statement_declarations":names,
            "grade_scope":"Named statement declarations with the hypotheses above. Chart supplier records have their own review scopes.",
            "confirmation_basis":"Minimum across the statement declarations, using registry rows for the blueprint assignments listed here. Reviews of other expositions of a shared declaration are included as context.",
            "notice":BANNER,
        }
        save(atlas / "units" / (uid+".yaml"), u)
    save(data/"blueprint_excerpt_index.json",excerpts)
    print(f"{len(membership)} assignments, {len(groups)} units, {sum(len(v) for v in excerpts.values())} passage locators")

if __name__ == "__main__":
    main()
