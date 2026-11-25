"""Render the paper and both reader guides from the same coverage records."""
import argparse
import html
import json
import re
import zlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTICE = "AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved"
LEVELS = ("full", "outline", "top_level_map", "statement_only", "not_covered")
SHADES = ("#262626", "#555555", "#888888", "#aaaaaa", "#dddddd")
NAMES = {
    "en": ("Full at nearest head", "Outline at head", "Map as head grade", "Statement only at head", "No indexed head"),
    "ko": ("가장 가까운 선언에 전체 논증", "색인 선언에 개요", "선언 등급이 지도뿐", "색인 선언에 진술만", "색인 선언 없음"),
}
LOCAL_LEVEL = {"en": {"full":"Full under stated inputs", "outline":"Outline", "top_level_map":"Top-level map only", "mixed":"Mixed local levels"}, "ko": {"full":"명시한 전제 아래 전체 논증", "outline":"개요", "top_level_map":"최상위 지도만", "mixed":"국소 서술 수준이 섞임"}}
URL = "https://github.com/GunheeC/rh-lean-verification-atlas/blob/v0.1.0/"


def read(path):
    return json.loads(path.read_bytes())


def text(value, lang):
    return value[lang] if isinstance(value, dict) else value


def tex(value):
    replacements = {"\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#",
                    "_": r"\_", "{": r"\{", "}": r"\}", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}"}
    return "".join(replacements.get(c, c) for c in str(value))


def words(value, lang, latex):
    raw = text(value, lang)
    if latex:
        return tex(raw)
    return raw.replace("|", r"\|").replace("\n", " ")


def code(raw, latex):
    if latex:
        return r"\nolinkurl{" + raw + "}"
    return "`" + raw + "`"


def link(label, target, latex):
    if latex:
        return r"\href{" + target.replace("#", r"\#") + "}{" + label + "}"
    return f"[{label}]({target})"


def page_range(first, last):
    return str(first) if first == last else f"{first}–{last}"


def tex_pages(a, b):
    pages = r"\pageref{" + a + "}"
    if a != b:
        pages += r"--\pageref{" + b + "}"
    return pages


def paper_ref(locator, lang, latex, catalog, page_index):
    a, b = locator["start_label"], locator["end_label"]
    sec = locator.get("section_label")
    if latex:
        section = r"\S\ref{" + sec + "}, " if sec else ""
        pages = tex_pages(a, b)
        n = r"\number\numexpr\getpagerefnumber{" + b + r"}-\getpagerefnumber{" + a + r"}+1\relax"
        return r"Paper " + section + r"pp.\ " + pages + " (" + n + " pp.)"
    pages = page_index["printed_pages"]
    first, last = pages[a], pages[b]
    extent = page_range(first, last)
    physical = page_index["named_destinations"][a]["pdf_page"]
    section = page_index.get("section_numbers", {}).get(sec)
    label = ("Paper " if lang == "en" else "논문 ") + ("§" + section + ", " if section else "")
    label += f"pp. {extent} ({last - first + 1} pp.)" if lang == "en" else f"{extent}쪽 ({last - first + 1}쪽)"
    prefix = "../" if lang == "en" else "../../"
    return link(label, prefix + catalog["paper2_v7"]["repository_file"] + f"#page={physical}", False)


def reading_ref(row, lang, latex, catalog, page_index):
    kind = row["document"]
    if kind == "paper":
        return paper_ref(row, lang, latex, catalog, page_index)
    title = words(row["title"], lang, latex)
    a, b = row["pages"]
    extent = page_range(a, b)
    label = title + (f", pp. {extent}" if lang == "en" else f", {extent}쪽")
    prefix = URL if latex else ("../" if lang == "en" else "../../")
    if kind == "blueprint":
        bp = catalog.get("blueprint_v13b")
        if latex:
            return label
        physical = bp["first_original_arabic_folio_pdf_page"] + a - 1
        return link(label, prefix + bp["repository_file"] + f"#page={physical}", latex)
    return link(label, prefix + row["path"], latex)


def source_line(pin, latex):
    name = pin.get("name", pin.get("decl"))
    path = pin["file"]
    a = pin.get("line0", pin.get("lo"))
    b = pin.get("line1", pin.get("hi"))
    return code(name, latex) + " · " + code(f"{path}:{a}–{b}", latex)


def plot_svg(levels, total, lang):
    width = 840
    labels = NAMES[lang]
    out = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} 260" role="img" aria-labelledby="t">',
           '<title id="t">' + ("Nearest indexed statement by exposition" if lang == "en" else "가장 가까운 색인 명제의 서술 수준") + '</title>',
           '<rect width="840" height="260" fill="white"/>',
           '<g font-family="sans-serif" font-size="16" fill="#222">']
    for i, (key, shade) in enumerate(zip(LEVELS, SHADES)):
        y = 35 + 46*i
        count = levels[key]
        length = 330 * count / total
        out.extend([f'<text x="8" y="{y}">{html.escape(labels[i])}</text>',
                    f'<rect x="260" y="{y-16}" width="330" height="18" fill="#f3f3f3"/>',
                    f'<rect x="260" y="{y-16}" width="{length:.4f}" height="18" fill="{shade}"/>',
                    f'<text x="607" y="{y}">{count:,} ({100*count/total:.4f}%)</text>'])
    return "\n".join(out + ["</g></svg>", ""])


def rendered(root, tex_only=False):
    d = root / "data"
    blocks = read(d / "coverage_blocks.json")
    tasks = read(d / "coverage_tasks.json")
    gaps = read(d / "coverage_gaps.json")
    catalog = read(d / "editions.json")["editions"]
    page_index = {} if tex_only else read(root / catalog["paper2_v7"]["coverage_label_index"])
    total = blocks["total"]
    levels = {k: sum(b["by_exposition"][k] for b in blocks["blocks"]) for k in LEVELS}
    if sum(b["lines"] for b in blocks["blocks"]) != total or total != 9567045 or sum(levels.values()) != total:
        raise ValueError("Coverage rows do not partition the fixed allChi inventory")
    if any(sum(b["by_exposition"].values()) != b["lines"] for b in blocks["blocks"]):
        raise ValueError("Block size differs from its exposition breakdown")
    if [t["order"] for t in tasks["tasks"]] != list(range(1, len(tasks["tasks"])+1)):
        raise ValueError("Verification task order is not consecutive")
    for task in tasks["tasks"]:
        uid = task["unit"]
        if task["checklist"] != f"units/{uid}.check.md" or not (root / task["checklist"]).is_file():
            raise ValueError(f"{uid}: invalid reader checklist")
        manifest = read(root / f"units/{uid}.steps.yaml")
        active = {s["id"] for s in manifest["steps"] if s["status"] == "active"}
        if (task["unit_step_count"] != len(active) or task["edition_sha256"] != manifest["edition_sha256"] or
                task["selected_step_count"] != len(task["steps"]) or (task["scope"] == "statement" and task["steps"])):
            raise ValueError(f"{uid}: stale checklist edition or reported task count")
        if not set(task["steps"]) <= active or len(set(task["steps"])) != len(task["steps"]):
            raise ValueError(f"{uid}: task cites an inactive or duplicated numbered step")
    out = {}
    for lang, latex in ([("en", True)] if tex_only else [("en", True), ("en", False), ("ko", False)]):
        en = lang == "en"
        prefix = URL if latex else ("../" if en else "../../")
        def w(v):
            return words(v, lang, latex)
        body = [] if latex else [("# Scope, coverage and verification tasks" if en else "# 서술 범위와 검증 과제"), "", NOTICE, ""]
        def heading(en_title, ko_title, label):
            body.extend([r"\subsection{" + en_title + r"}\label{" + label + "}" if latex else "## " + (en_title if en else ko_title), ""])
        heading("Coverage map", "서술 범위", "v7:q1")
        body.extend([w(blocks["scope"]), "", w(blocks["method"]["description"]), ""])
        if latex:
            body.extend([r"\begingroup\scriptsize\setlength{\tabcolsep}{2pt}\setlength{\emergencystretch}{2em}",
                         r"\begin{longtable}{@{}>{\raggedright\arraybackslash}p{.14\linewidth}>{\raggedright\arraybackslash}p{.15\linewidth}>{\raggedright\arraybackslash}p{.18\linewidth}>{\raggedright\arraybackslash}p{.10\linewidth}>{\raggedright\arraybackslash}p{.34\linewidth}@{}}",
                         r"\caption{Scope of the indexed blocks}\label{tab:v7-coverage}\\",
                         r"\toprule Block / role & Lean entries & Exposition level & Core lines & Written locations / AI review / human check \\ \midrule\endfirsthead",
                         r"\toprule Block / role & Lean entries & Exposition level & Core lines & Written locations / AI review / human check \\ \midrule\endhead"])
        else:
            headers = ["Block", "Role", "Lean entries", "Core lines", "Written locations", "Exposition levels", "AI review", "Human checks"] if en else ["부분","역할","Lean 선언","코어 줄","서술 위치","서술 수준","AI 검토","사람 확인"]
            body.extend(["| " + " | ".join(headers) + " |", "|" + "---|" * len(headers)])
        for row in blocks["blocks"]:
            locations = [reading_ref(loc, lang, latex, catalog, page_index) for loc in row["readings"]]
            reading = w(row["writing"]) + (" · " + " · ".join(locations) if locations else "")
            names = [code(x["name"], latex) for x in row["entries"]]
            review = w(row["review"])
            expo = [(NAMES[lang][i],row["by_exposition"][k]) for i,k in enumerate(LEVELS) if row["by_exposition"][k]]
            breakdown = LOCAL_LEVEL[lang][row["level"]] + (r"\par " if latex else " · ") + (r"\par " if latex else " · ").join(f"{a} {n:,}" for a,n in expo)
            if latex:
                cells = [r"\textbf{" + w(row["title"]) + r"}\par " + w(row["role"]), r"\par ".join(names) or "—", breakdown, f'{row["lines"]:,}', reading + r"\par AI review: " + review + r"\par Human checks: " + str(row["human_checks"])]
                body.append(" & ".join(cells) + r" \\ \midrule")
            else:
                body.append("| " + " | ".join([w(row["title"]), w(row["role"]), " · ".join(names) or "—", f'{row["lines"]:,}', reading, breakdown, review, str(row["human_checks"])]) + " |")
        if latex:
            body += [r"\textbf{Total} & & & " + f"{total:,}" + r" & \\", r"\bottomrule\end{longtable}\endgroup"]
        else:
            body += ["| " + ("**Total**" if en else "**합계**") + f" | | | **{total:,}** | | | | |"]
        body.extend(["",w(blocks["summary"]),""])
        if latex:
            body += [r"\begin{figure}[htbp]\centering\footnotesize",r"\begin{tabular}{@{}l l r@{}}"]
            for i,k in enumerate(LEVELS):
                n=levels[k]
                body.append(f'{NAMES[lang][i]} & '+r"\textcolor{black!"+str(90-12*i)+r"}{\rule{"+f'{.32*n/total:.6f}'+r"\linewidth}{1.1ex}} & "+f"{n:,} ({100*n/total:.4f}"+r"\%) \\")
            body += [r"\end{tabular}\caption{Index positions by exposition of their nearest indexed statement.}\label{fig:v7-coverage}\end{figure}",""]
        else:
            body += ["![" + ("Index positions by exposition level" if en else "가장 가까운 색인 명제의 서술 수준별 위치") + f"]({prefix}data/coverage_levels_{lang}.svg)", ""]
        citation = blocks["citations"]
        keys = ("core_full","core_outline_only","core_uncited")
        if sum(citation[key] for key in keys) != total:
            raise ValueError("Direct citations do not partition the core inventory")
        citations_head = ["Active step citations", "Core lines", "Share"] if en else ["유효한 단계의 직접 인용", "코어 줄", "비율"]
        citations_label = (["Cited by a Full step", "Additional lines cited only by Outline steps", "No active step cites this line"]
                           if en else ["전체 논증 단계가 인용한 줄", "개요 단계만 인용한 추가 줄", "유효한 단계가 인용하지 않은 줄"])
        if latex:
            body += [r"\begin{center}\small\begin{tabular}{@{}lrr@{}}\toprule",
                     " & ".join(citations_head) + r" \\ \midrule"]
        else:
            body += ["| " + " | ".join(citations_head) + " |", "|---|---:|---:|"]
        for label, key in zip(citations_label, keys):
            lines = citation[key]
            percent = f"{100*lines/total:.4f}" + (r"\%" if latex else "%")
            body.append((f"{label} & {lines:,} & {percent}" + r" \\") if latex else f"| {label} | {lines:,} | {percent} |")
        if latex:
            body += [r"\bottomrule\end{tabular}\end{center}"]
        closed = citation["all_prerequisites_full"]
        full = citation["full_units"]
        body += ["", w(blocks["citation_interpretation"]), "",
                 (f"Direct citations do not establish a line-by-line proof. The share of the interior with a complete written derivation has not been measured. Of {full} locally Full units, {closed} have a recursively closed set of Full prerequisites."
                  if en else f"직접 인용이 각 줄의 증명을 확인해 주지는 않는다. 내부에서 완전한 서면 유도가 있는 비율은 측정되지 않았다. 국소 전체 논증이 있는 {full}개 중 모든 전제가 재귀적으로 전체 논증까지 닫히는 단위는 {closed}개다."), ""]
        heading("What a reader can check", "독자가 확인할 수 있는 과제", "v7:q2")
        body.extend([w(tasks["step_scope"]), ""])
        for t in tasks["tasks"]:
            title = w(t["title"])
            task_id = f" ({t['id']})" if re.fullmatch(r"A[0-9]+", t["id"]) else ""
            task_name = f"{t['order']}{task_id}. {title}"
            body += [r"\paragraph{Task " + task_name + r"}\label{v7:task-" + str(t["order"]) + "}" if latex else "### " + task_name, ""]
            labels = [("check","Check","확인할 내용"),("assume","Inputs","가정"),("background","Background","선수 지식"),("positive","A positive check establishes","확인되는 범위"),("limit","Outside this check","남는 부분")]
            for k,eng,kor in labels:
                body += [(r"\textbf{"+eng+r".} " if latex else "**"+(eng if en else kor)+".** ")+w(t[k]),""]
            refs=[paper_ref(t["paper"],lang,latex,catalog,page_index)] if t.get("paper") else []
            refs.extend(reading_ref(loc,lang,latex,catalog,page_index) for loc in t.get("readings",[]))
            ids = t["steps"]
            steptext = (f"{len(ids)} of {t['unit_step_count']} numbered checklist steps" if en else f"확인표의 전체 {t['unit_step_count']}단계 중 {len(ids)}단계")
            if ids:
                steptext += " (" + ", ".join(ids) + ")"

            body += [(" · ".join(refs+[steptext,link(tex(t["unit"])+" checklist" if latex else (t["unit"]+(" checklist" if en else " 확인표")),prefix+t["checklist"],latex)]))+".",""]
            for pin in t["lean"]:
                body += [source_line(pin, latex) + ("." if latex else ""), ""]
        intake=link("Reader sign-off instructions" if en else "사람 검토 기록 제출 안내",prefix+("signoffs/README.md" if en else "docs/ko/signoffs/README.md"),latex)
        body += [(("Record the edition, step IDs, assumptions and verdict. Report a failed inference or limitation through the same form. " if en else "판본과 단계 번호, 가정, 판정을 적는다. 추론이 성립하지 않거나 범위가 제한되는 경우에도 같은 양식으로 제출한다. ")+intake+"."),""]
        heading("What the written documents leave open", "서면 자료에서 아직 확인할 수 없는 부분", "v7:q3")
        body += [w(gaps["size_rule"]),""]
        for x in gaps["rows"]:
            title=w(x["title"])
            body += [r"\paragraph{"+title+"}" if latex else "### "+title,"",w(x["gap"]),"",
                     ("Field: " if en else "전문 분야: ")+w(x["field"])+". "+("Further document needed: " if en else "필요한 자료: ")+w(x["next"]),""]
            for pin in x["lean"]:
                size=pin["dominated"]
                count=(f"{size:,} dominated core lines" if en else f"지배하는 코어 줄 {size:,}개") if size is not None else ("separate size not registered" if en else "별도 크기 미등록")
                body += [source_line(pin,latex)+" · "+count+".",""]
        if latex:
            body += [r"\noindent\textattachfile[color=0.15 0.15 0.15,mimetype=text/plain,description={Coverage tables and reading tasks}]{v7_coverage_data.tex}{\textcolor{inkblue}{Source for the coverage tables and reading tasks (TeX).}}",""]
            out["data/v7_coverage_data.tex"] = "\n".join(body)
        else:
            body += ["## How further work is recorded" if en else "## 후속 작업의 기록 방법", "",
                     (f"Each written step has a source and edition. Human checks identify both. A revised edition requires a fresh check. Part II on V and Part III on F are tentative plans. [Programme]({prefix}ROADMAP.md) · [Edition register]({prefix}data/editions.json) · [Review register]({prefix}reviews/index.json)"
                      if en else f"서면 단계마다 소스와 판본이 있다. 사람 검토는 두 항목을 지정하고, 판본이 바뀌면 새로 확인한다. V를 다룰 제2부와 F를 다룰 제3부는 잠정 계획이다. [작업 계획]({prefix}ROADMAP.md) · [판본 기록]({prefix}data/editions.json) · [검토 기록]({prefix}reviews/index.json)"), ""]
            out["docs/coverage.md" if en else "docs/ko/coverage.md"] = "\n".join(body)
            out[f"data/coverage_levels_{lang}.svg"] = plot_svg(levels,total,lang)
    return out


def embedded_source(pdf, source):
    """Look for the exact self-attached TeX bytes in a raw or Flate PDF stream."""
    for marker in re.finditer(rb"(?<![a-z])stream(?:\r\n|[\r\n])", pdf):
        pos = marker.end()
        if pdf.startswith(source, pos):
            return True
        if pos >= len(pdf) or pdf[pos] & 15 != 8:
            continue
        try:
            d = zlib.decompressobj()
            # The bound prevents a malicious stream from filling memory.
            data = d.decompress(memoryview(pdf)[pos:], max_length=len(source)+1)
            if d.eof and data == source:
                return True
        except zlib.error:
            continue
    return False


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=ROOT)
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--tex-output", type=Path, help="Write the manuscript fragment before running LaTeX")
    a = ap.parse_args()
    out = rendered(a.root, tex_only=a.tex_output is not None)
    fragment = out["data/v7_coverage_data.tex"]
    if a.tex_output:
        a.tex_output.write_text(fragment, encoding="utf-8")
        return
    for name, content in out.items():
        p = a.root / name
        if a.check:
            if not p.is_file() or p.read_text(encoding="utf-8") != content:
                raise SystemExit("Stale coverage output: " + name)
        else:
            p.write_text(content, encoding="utf-8")
    if a.check:
        paper = read(a.root / "data/editions.json")["editions"]["paper2_v7"]
        if not embedded_source((a.root / paper["repository_file"]).read_bytes(), fragment.encode()):
            raise SystemExit("Paper v7 does not contain the exact coverage-table source generated by this checkout.")
        citations = read(a.root / "data/coverage_blocks.json")["citations"]
        from check_coverage_blocks import verify
        verify(a.root)
        from coverage_closure import closed_units
        from snapshot import pipeline
        counts = pipeline(a.root)["counts"]["all"]
        actual = {"all_prerequisites_full":len(closed_units(a.root)), "full_units":counts["full"],
                  "steps":counts["written_steps"], "human_checked_steps":counts["human_checked_steps"],
                  "distinct_physical":counts["cited_lines"]["written"]["all_files"],
                  "core":counts["cited_lines"]["written"]["in_weighted_core"]}
        for name, value in actual.items():
            if citations[name] != value:
                raise SystemExit("Coverage snapshot differs from the source evidence: " + name)


if __name__ == "__main__":
    main()
