#!/usr/bin/env python3
"""Build the English unit pages, or compare them with their sources using --check."""
from atlas_files import unit_files
from edition_links import blueprint_page
import argparse
from collections import defaultdict
import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
NOTICE = "AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved"
from atlas_labels import TRACK_NAMES as TRACKS
from signoff_records import l4_summary, load_records
GRADES = {"L0": "Declaration pinned; no review of this unit", "L1": "Statement matched to Lean",
          "L2": "Written proof accepted in AI cross-review", "L3": "Independent expositions agree",
          "L4": "Named human sign-off"}
MATH = re.compile(r"\\\[(.*?)\\\]|\\\((.*?)\\\)|\$\$(.*?)\$\$|(?<!\\)\$((?:\\.|[^$])*)\$", re.S)
INLINE_MACRO = re.compile(r"\\(nolinkurl|code|texttt|emph|textbf|ensuremath|nodeid)\{([^{}]*)\}")
PIN_PREFIX = "https://github.com/leanprover-community/riemann-hypothesis/blob/"

def load(file):
    return json.loads(file.read_text(encoding="utf-8"))

def pageref(pages):
    return "p. "+str(pages[0]) if len(set(pages))==1 else f"pp. {pages[0]}–{pages[-1]}"

def link(name, path):
    return f"[{name}]({path})"

def interval(lines):
    return str(lines[0]) if lines[0]==lines[-1] else f"{lines[0]}–{lines[-1]}"

# Spellings emitted by the v3 TeX-to-text conversion. Each maps to the same
# formula in the adjacent display; other prose is copied from the unit YAML.
LEGACY_EXPRESSIONS = {
    r"Gal(Q̄\ensuremath{\ell}/K)": r"\operatorname{Gal}(\overline{\mathbb Q}_\ell/K)",
    r"(p−q)/2": r"(p-q)/2", r"exp(−x^(ez/7))": r"\exp(-x^{e_z/7})",
    r"floor(Y^(epsilon/5))": r"\lfloor Y^{\varepsilon/5}\rfloor",
    r"x^(−1+epsilon)": r"x^{-1+\varepsilon}",
    r"0<epsilon<1/52": r"0<\varepsilon<1/52",
    r"[x^(2+8epsilon),2x^(2+8epsilon)]": r"[x^{2+8\varepsilon},2x^{2+8\varepsilon}]",
    r"|Gpsi(y)−Gpsi(z)| \ensuremath{\le} |y−z|(log(max(y,z))+Cd+|ell(psi)|)": r"|G_\psi(y)-G_\psi(z)|\le |y-z|(\log(\max\{y,z\})+C_d+|\ell(\psi)|)",
    r"|Gz(y)−Gz(z)| \ensuremath{\le} Cd|y−z|": r"|G_z(y)-G_z(z)|\le C_d|y-z|",
    r"|TT| times (vv(psi)−R)": r"|TT|(\operatorname{vv}(\psi)-R)",
    r"psi(e1(t))": r"\psi(e_1t)", r"y(t)":r"y_t",
    r"Err \ensuremath{\le} x^(C·epsilon)": r"\mathrm{Err}\le x^{C\varepsilon}",
    r"x\ensuremath{\ge}3": r"x\ge3", r"x^(3epsilon/8)\ensuremath{\ge}26": r"x^{3\varepsilon/8}\ge26",
    r"m \ensuremath{\le} x^(1/2+epsilon/2)": r"m\le x^{1/2+\varepsilon/2}",
    r"xm \ensuremath{\le} k": r"xm\le k", r"Ga(u)":r"\mathrm{Ga}(u)",
    r"Main(u)+log|W(u)|+K0v5+M":r"\mathrm{Main}(u)+\log|W(u)|+K_{0,v5}+M",
    r"(1−delBar) inverse":r"(1-\bar\delta)^{-1}",
    r"[4 log(1+x^cHH)(K3+M+b)+(etaBar+4sqrt(eBar))x^cHH b]":
        r"\left[4\log(1+x^{c_{HH}})(K_3+M+b)+(\bar\eta+4\sqrt{\bar e})x^{c_{HH}}b\right]",
}
def tex_prose(text, ids, labels):
    """Translate the blueprint's presentation macros without changing mathematical delimiters."""
    text = re.sub(r"\\par\\noindent\{\\footnotesize\s+(?:\\nolinkurl\{[^{}]+\}(?:,\s*)?)+\.\}\\par\s*", "", text)
    text = re.sub(r"\\textasciicircum(?:\{\})?", "^", text)
    text = text.replace(r"\ensuremath{-}", "−")
    for old, rendered in LEGACY_EXPRESSIONS.items():
        if old in text:
            text=text.replace(old,"$"+rendered+"$")
    text = re.sub(r"\\begin\{(itemize|enumerate)\}", "\n\n", text)
    text = re.sub(r"\\end\{(itemize|enumerate)\}", "\n\n", text)
    text = re.sub(r"\\item\b\s*", "\n\n- ", text)
    text = text.replace("~", " ").replace("---", "—").replace("--","–")
    text = text.replace(r"\_", "_").replace(r"\%", "%").replace(r"\&", "&")
    def inline(m):
        cmd, body = m.groups()
        if cmd == "nodeid":
            return link(body, body+".md") if body in ids else body
        if cmd in ("nolinkurl","texttt","code"):
            return "\x60"+body+"\x60"
        if cmd == "ensuremath":
            return "$"+body+"$"
        if cmd == "emph":
            return "*"+body+"*"
        return "**"+body+"**"
    text = INLINE_MACRO.sub(inline, text)
    def hyper(m):
        label, caption = m.groups()
        if caption in ids:
            return link(caption,caption+".md")
        dest = labels.get(label)
        return caption + (f" (manuscript §{dest['section']}, p. {dest['page']})" if dest else "")
    text = re.sub(r"\\hyperref\[([^\]]+)\]\{([^{}]+)\}", hyper, text)
    def ref(m):
        dest=labels[m[1]]
        return f"{dest['section']} (manuscript p. {dest['page']})"
    text = re.sub(r"\\ref\{([^{}]+)\}",ref,text)
    return text

def tex_math(formula):
    formula = formula.strip().replace(r"\Sha",r"\operatorname{Sha}").replace("](",r"]\,(")
    formula = re.sub(r"\\(code|nolinkurl|texttt)\{([^{}]*)\}",
                     lambda m: r"\texttt{"+m[2].replace("_",r"\_")+"}", formula)
    # 'split' is an AMS equation wrapper. 'aligned' works directly inside a GitHub display.
    formula = formula.replace(r"\begin{split}",r"\begin{aligned}").replace(r"\end{split}",r"\end{aligned}")
    return re.sub(r"\s+", " ", formula)

def markdown(text, ids, labels):
    # GitHub-style parsers require delimiters at word boundaries.
    text=text.replace("I$_2$",r"$\mathrm{I}_2$")
    text=re.sub(r"(\$(?:\\[A-Za-z]+|[A-Za-z])\$)th\b",r"\1-th",text)
    pieces=[]
    i=0
    for m in MATH.finditer(text):
        pieces.append(tex_prose(text[i:m.start()],ids,labels))
        if m[1] is not None or m[3] is not None:
            pieces.append("\n\n$$\n"+tex_math(m[1] if m[1] is not None else m[3])+"\n$$\n\n")
        else:
            pieces.append("$"+tex_math(m[2] if m[2] is not None else m[4])+"$")
        i=m.end()
    pieces.append(tex_prose(text[i:],ids,labels))
    text="".join(pieces)
    parts=[]
    for part in re.split(r"\n\s*\n",text):
        part=part.strip()
        if not part:
            continue
        if part.startswith("$$\n"):
            parts.append(part)
        else:
            parts.append(re.sub(r"\s+"," ",part))
    return "\n\n".join(parts)

class Atlas:
    def __init__(self, root):
        self.root=root
        from snapshot import pipeline
        self.pipeline = pipeline(root)["units"]
        self.generated = load(root/"data/round6_review_corrections.json")["date"]
        self.units_with_records = {rec["unit"] for _, rec in load_records(root)}
        self.units={p.stem:load(p) for p in sorted(unit_files(root))}
        self.commit=load(root/"data/pins.json")["source_commit"]
        self.labels=load(root/"data/paper_v3_labels.json")["labels"]
        self.editions=load(root/"data/editions.json")["editions"]
        self.reviews=load(root/"data/grade_evidence.json")["records"]
        self.starters={v["unit_id"]:v for v in load(root/"data/notes_starters.json")["starters"].values()}
        self.graph=load(root/"data/unit_graph.json")["units"]
        self.reading_audit=load(root/"data/round3_prerequisites.json")["units"]
        self.new_pillar_units = {u["id"] for u in load(root/"data/round4_changes.json")["changes"]
                                 if u["old_status"] == "New"}
        self.external=defaultdict(list)
        for mapping in load(root/"crosswalk/adriazola.json")["mappings"]:
            for uid in mapping["unit_ids"]:
                self.external[uid].append(mapping)
        self.sources={v["id"]:v for v in load(root/"sources/registry.json")["sources"]}
        self.name_matches=defaultdict(lambda: defaultdict(list))
        for source in load(root/"crosswalk/name_matches.json")["sources"]:
            for r in source["rows"]:
                for uid in r["unit_ids"]:
                    self.name_matches[uid][source["source_id"]].append(r)

    def prose(self, text):
        return markdown(text, self.units, self.labels)

    def unit_link(self, uid):
        return link(uid+" · "+self.units[uid]["title"], uid+".md")

    def source_link(self, source):
        if source in self.editions:
            return link(self.editions[source]["title"], "../data/editions.json")
        return link(self.sources[source]["title"], "../sources/README.md")

    def readings(self, u):
        uid=u["id"]
        lines=[]
        if uid in self.starters:
            s=self.starters[uid]
            lines.append(f"- {link('Graduate reading packet · '+s['title'],'../'+s['path'])}")
        paper = self.editions["paper2_v7"]
        blueprint = self.editions["blueprint_v13b"]
        for entry in paper["unit_locators"].get(uid, []):
            physical = entry["pdf_pages"][0]
            ref = link(entry["section"], "../" + paper["repository_file"] + f"#page={physical}")
            lines.append("- Paper v7 · " + ref + ", printed " + pageref(entry["printed_pages"]))
        for e in u["expositions"]:
            doc=e["document"]
            if doc == "blueprint_v13":
                physical = blueprint_page(blueprint, e["pages"][0])
                ref = link("Blueprint v13b", "../" + blueprint["repository_file"] + f"#page={physical}")
                lines.append(f"- {ref}, printed p. {e['printed_page']}, section label `{e['section']}`.")
            if doc in self.editions:
                loc=e["section"]
                if doc=="blueprint_v13":
                    loc=f"section label \x60{loc}\x60"
                else:
                    loc=re.sub(r"\s*\(pn:[^)]+\)", "", loc)
                label=self.editions[doc]["title"]
                text=link(label, "../data/editions.json")+f", {loc}"
                if e["pages"]:
                    text+=", "+("PDF " if doc=="blueprint_v13" else "")+pageref(e["pages"])
                if e.get("printed_page"):
                    text+=f" (printed p. {e['printed_page']})"
                if e.get("coverage"):
                    text+=". "+self.prose(e["coverage"])
            elif doc.startswith("notes/") and doc.endswith(".md"):
                text = link(e["section"], "../" + doc)
                if e.get("pages"):
                    text += ", " + pageref(e["pages"]) + " in the atlas print layout"
                if e.get("coverage"):
                    text += ". " + self.prose(e["coverage"])
            elif doc.startswith("notes/"):
                if doc.startswith("notes/blueprint/"):
                    name="Blueprint source excerpt"
                elif doc.endswith("-argument.tex"):
                    name="Manuscript argument excerpt"
                else:
                    name="Manuscript source excerpt"
                text=link(name,"../"+doc)
                if "," not in e["section"]:
                    text+=" · section \x60"+e["section"]+"\x60"
            elif doc.startswith("crosswalk/"):
                text=link("Adriazola comparison", "../crosswalk/README.md")+" · "+e["section"]
                if e.get("coverage"):
                    text+=". "+self.prose(e["coverage"])
            else:
                text=link(e["section"], "../"+doc)
            lines.append("- "+text)
        return list(dict.fromkeys(lines))

    def evidence(self, u):
        grade=u["grade"]
        if grade == "L4":
            checklist = link("Current statement, steps and named sign-off records", u["id"] + ".check.md")
            return [f"- {checklist}. " + l4_summary(self.pipeline[u["id"]]["l4_evidence"])]
        records=u.get("grade_evidence", [])
        if u.get("blueprint_members"):
            names=set(u["statement_declarations"])
            records=[r for r in self.reviews if r.get("legacy_unit") in u["blueprint_members"]
                     and names.intersection(r["declarations"])]
        items=[]
        included=set()
        for r in records:
            if r["grade"]!=grade:
                continue
            path=r["review"]
            loc=r.get("lines")
            key=(path, tuple(loc or []), r["verdict"])
            if key in included:
                continue
            included.add(key)
            cite=link(Path(path).stem.replace("_"," "),"../"+path)
            if loc:
                cite+=", original "+("line " if len(set(loc))==1 else "lines ")+interval(loc)
            items.append(f"- {cite} — {r['verdict']}. {r['scope']}")
        if u.get("kind") == "paper_composite":
            return [u["grade_scope"]]
        if not items and grade=="L1":
            for r in records:
                if r["grade"]=="L2":
                    cite=link(Path(r["review"]).stem.replace("_"," "),"../"+r["review"])
                    items.append(f"- {cite}, original lines {interval(r['lines'])} — {r['verdict']}. This verdict covers the blueprint proof of the shared declaration. The atlas assigns L1 to the statement in this manuscript.")
        if not items:
            if grade=="L0":
                items=["The pinned declaration is recorded in the formal source. No higher-level verdict is assigned to this unit."]
            else:
                raise ValueError(f"{u['id']}: no evidence for {grade}")
        return items

    def declarations(self, u):
        primary=set(u.get("statement_declarations", [])) or {u["lean"][0]["name"]}
        def row(a):
            n=a["name"]
            destination=f"{PIN_PREFIX}{self.commit}/src/{quote(a['file'],safe='/')}#L{a['line0']}-L{a['line1']}"
            citation=link("\x60"+Path(a["file"]).name+"\x60",destination)
            nlines="outside the measured graph" if a["dominated"] is None else f"{a['dominated']:,} dominated lines"
            return f"- \x60{n}\x60  \n  {citation}, lines {interval([a['line0'],a['line1']])} · {nlines} · SHA-256 \x60{a['sha256'][:12]}\x60."
        if u.get("kind") == "paper_composite":
            return ["These are components of the paper implication. Its full hypothesis table has its own manuscript locator.", "",
                    *[row(a) for a in u["lean"]]]
        roots=[row(a) for a in u["lean"] if a["name"] in primary]
        other=[row(a) for a in u["lean"] if a["name"] not in primary]
        if other:
            roots+=["", "<details>", f"<summary>{len(other)} additional indexed declaration{'s' if len(other)!=1 else ''}</summary>", "", *other,"","</details>"]
        return roots

    def render(self, u):
        uid=u["id"]
        tr=u["track"]
        trackrefs=[link(TRACKS[t],"../tracks/"+t+"/README.md") for t in [tr["primary"]]+tr["secondary"]]
        evidence_label = "Pinned Lean components of the paper argument" if u.get("kind") == "paper_composite" and u["grade"] == "L0" else GRADES[u["grade"]]
        if u["grade"] == "L2" and not self.pipeline[uid]["stages"][4]:
            evidence_label = "AI proof verdict on an earlier or different exposition; current proof edition awaits review"
        out=[f"# {uid} · {u['title']}", "", NOTICE, "",
             *([self.prose(u["summary"]), ""] if u.get("summary") else []),
             f"\x60{u['slug']}\x60 · "+" · ".join(trackrefs), "",
             f"**{u['status']}** · **{u['grade']}** {evidence_label} · Record generated {self.generated}" +
             ("." if uid in self.units_with_records else " (no human check)."),
             "", "## Statement", "", self.prose(u["statement"]), "", "## Assumptions", ""]
        stages = self.pipeline[uid]
        marks = ["✓" if reached else "–" for reached in stages["stages"][:5]]
        reviewed = f"{stages['human_checked_steps']} of {stages['written_steps']} steps"
        check = (link("Numbered proof and check records", uid + ".check.md")
                 if stages["written_steps"] else "Awaiting numbered proof")
        marks[2] = u["status"]
        marks[3] = str(stages["written_steps"])
        if stages["stages"][4]:
            marks[4] = "Outline fidelity (AI)" if u["status"] == "Outlined" else "Current argument (AI)"
        statement = out.index("## Statement")
        if any(e["document"].endswith("_round4.md") for e in u["expositions"]):
            weight = u["lean"][0]["dominated"]
            size = f"{weight:,} dominated core lines" if weight is not None else "size outside the measured graph"
            label = "**First-pass outline of the head proof term**"
            if uid in ("T01", "T08"):
                label += " · **top-level map only**"
            out[statement:statement] = [label + " · " + size + ". In scope, this note describes what the top-level term calls; it does not explain the dependency cone beneath it.", ""]
        statement = out.index("## Statement")
        out[statement:statement] = [
            "| 1 · Lean pinned | 2 · Statement compared | 3 · Prose | 4 · Steps | 5 · AI review | 6 · Human |",
            "|---|---|---|---|---|---|", "| " + " | ".join(marks + [reviewed]) + " |", "",
            check + " · " + link("Progress and counting rules", "../PROGRESS.md"), ""]
        out+=["- "+self.prose(s) for s in u["hypothesis_details"]]
        cited=[]
        for a in u["assumptions"]:
            if a.startswith("source:"):
                cited.append(self.source_link(a[7:]))
            elif a in self.units:
                cited.append(self.unit_link(a))
            elif a.startswith("hyp:"):
                out.append("- "+self.prose(a[4:].strip()))
            else:
                raise ValueError(f"{uid}: unresolved assumption {a}")
        if cited:
            out+=["","Sources for the assumptions · "+" · ".join(cited)]
        if u.get("review_status") == "pending_review" and u["grade"] != "L4":
            out += ["", "**New exposition · pending_review.** This edition has no independent review of the new argument. Earlier verdicts below retain their stated scopes."]
        out += ["", "## Where to read", "",
                "Gunhee Cho is the paper’s author and the blueprint’s editor. Both were drafted with AI assistance. No independent human referee has checked the arguments. Levent Alpöge is the author of the Lean development. [Blueprint v13b](../editions/v0.1.0/blueprint_v13b.pdf) · [Conditional paper v7](../editions/v0.1.0/paper_v7.pdf) · [Edition register](../data/editions.json)", "",
                *self.readings(u)]
        if self.external[uid]:
            out+=["","### Other expositions and comparisons",""]
            for r in self.external[uid]:
                name="Adriazola, "+r["external_id"]
                if r.get("page"):
                    name+=f", p. {r['page']}"
                pdf=self.sources["adriazola"]["edition_evidence"]["pdf_url"]
                out.append("- "+link(name,pdf)+" · "+r["relation"]+". "+link("Correspondence table","../crosswalk/adriazola.md")+".")
        if self.name_matches[uid]:
            out+=["","### Declaration-name matches",""]
            for sid, rows in self.name_matches[uid].items():
                source=self.sources[sid]
                node_ids=sorted({n["id"] for r in rows for n in r["external_nodes"] if n.get("id")})
                count=len(rows)
                sep=" · indices "+", ".join("\x60"+n+"\x60" for n in node_ids) if node_ids else ""
                out.append("- "+link(source["short_title"],"../crosswalk/"+sid+".md")+f" · {count} matching declaration"+("s" if count!=1 else "")+sep+".")
        out+=["", "## Evidence", "", *self.evidence(u)]
        if u.get("grade_scope") and len(u["lean"])>1 and u.get("kind") != "paper_composite" and u["grade"] != "L4":
            out+=["",u["grade_scope"]]
        if u["reviews"]:
            cards=[link(Path(s).stem.replace("_"," "),"../"+s) for s in u["reviews"]]
            out+=["","Review records · "+" · ".join(cards)]
        out+=["","## Lean declarations","", *self.declarations(u), "",link("Machine record and full declaration hashes",uid+".yaml")+
              " · "+link("Declaration lookup","../lookup/declarations.md")]
        out+=["","## Reading prerequisites",""]
        if u["background"]:
            out+=["Background · "+" · ".join(self.prose(s) for s in u["background"])+".",""]
        if u["prerequisites"]:
            sources = u.get("prerequisite_sources", {})
            out+=["- "+self.unit_link(i)+(f" · {sources[i]}" if i in sources else "") for i in u["prerequisites"]]
            if sources and uid in self.reading_audit:
                out += ["", link("Evidence and definitions of reading links", "../data/round3_prerequisites.json")]
        else:
            audit = (self.reading_audit.get(uid) or {}).get("audit")
            if audit:
                out.append(audit["reason"] + " " + link("Statement evidence", "../data/round3_prerequisites.json"))
            else:
                out.append("No prior atlas unit is specified.")
        if uid in self.new_pillar_units:
            out += ["", link("Pillar dependencies and pinned source ranges", "../data/round4_changes.json")]
        out+=["","## Open questions",""]
        questions=u["open_questions"]
        if not questions or questions==["none-recorded"] or questions=="none-recorded":
            out.append("None recorded.")
        else:
            out+=["- "+self.prose(q) for q in questions]
        if u.get("pillar_map"):
            out += ["", link("Pillar call tree and source witnesses", "../" + u["pillar_map"])]
        out+=["","## Graph connections","","Arrows may connect either a unit’s main declaration or an indexed member.", ""]
        edges=self.graph.get(uid, {"uses": [], "used_by": []})
        for key,label in (("uses","Uses"),("used_by","Used by")):
            items=edges[key]
            out+=["**"+label+"** · "+(" · ".join(link(i,i+".md") for i in items) if items else "No recorded edge.") ,""]
        out.append(link("Declaration witnesses and graph scope","../data/unit_graph.json"))
        aliases=u.get("aliases", [])
        if aliases:
            out+=["","Lookup aliases · "+", ".join("\x60"+a+"\x60" for a in aliases)]
        canonical=json.dumps(u,ensure_ascii=False,sort_keys=True,separators=(",",":")).encode()
        out+=["","<!-- Unit metadata SHA-256 "+hashlib.sha256(canonical).hexdigest()+" -->"]
        return "\n".join(out)+"\n"

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root",type=Path,default=ROOT)
    parser.add_argument("--check",action="store_true",help="fail on a missing, stale or orphan unit page")
    args=parser.parse_args()
    atlas=Atlas(args.root)
    stale=[]
    for uid,u in atlas.units.items():
        page=args.root/"units"/(uid+".md")
        body=atlas.render(u)
        if not page.exists() or page.read_text(encoding="utf-8")!=body:
            if args.check:
                stale.append(uid)
            else:
                page.write_text(body,encoding="utf-8")
    for p in (args.root/"units").glob("*.md"):
        if not p.name.endswith(".check.md") and p.stem not in atlas.units:
            stale.append(p.name+" (no unit YAML)")
    if stale:
        print("Missing, stale or orphan unit pages: "+", ".join(stale),file=sys.stderr)
        return 1
    print(f"{len(atlas.units)} unit pages {'up to date' if args.check else 'generated'}.")
    return 0

if __name__=="__main__":
    sys.exit(main())
