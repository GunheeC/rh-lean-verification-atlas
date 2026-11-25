#!/usr/bin/env python3
"""Regenerate the entry-page census and the two status tables from the step records."""
import argparse
from collections import Counter
from pathlib import Path
import posixpath
import re
from snapshot import ROOT, pipeline, read

from atlas_labels import TRACK_NAMES

KOREAN_NAMES = {
    "analytic": "해석적 수론",
    "arakelov": "Arakelov 기하·수의 기하",
    "theta": "세타 대응·유니타리 군의 보형 표현",
    "galois": "갈루아 표현·보형성 올림·Iwasawa 이론과 오일러 계",
    "local": "국소 p진 이론",
    "ktheory": "대수적 K이론·산술군 코호몰로지",
    "formal": "형식화·재현",
}
METRICS = {
    "written": ("Any written step", "서술된 모든 단계"),
    "full": ("Steps in full arguments", "전체 논증의 단계"),
    "outlined": ("Steps in outlines", "개요의 단계"),
    "ai_reviewed": ("Steps reviewed by AI on this edition", "이 판본에서 AI가 해당 단계를 검토"),
    "ai_reviewed_prose": ("Steps in prose with a whole-argument AI review", "전체 논증의 AI 검토가 있는 판본의 단계"),
    "human_checked": ("Steps with a current qualifying human check", "현 판본에서 실명 확인된 단계"),
}


def replace_once(text, pattern, replacement, flags=0):
    result, count = re.subn(pattern, lambda _: replacement, text, flags=flags)
    if count != 1:
        raise ValueError("Expected exactly one census block matching " + pattern)
    return result


def entry(text, a, grades, ko):
    if ko:
        box = ["**서술과 검토 현황** · [검증 범위](docs/ko/STATUS.md) · [진척 추이](PROGRESS.md)",
               f"전체 {a['units']}개 단위 중 명시한 가정 아래 전체 논증이 있는 단위는 {a['full']}개, 개요는 {a['outlined']}개, 명제만 있는 단위는 {a['statement_only']}개다.",
               f"AI의 서면 논증 검토를 근거로 L2 등급을 받은 단위는 {grades['L2']}개다. 현 판본의 {a['written_steps']}단계 중 {a['ai_reviewed_steps']}단계에 그 추론을 특정한 AI 검토 기록이 있다.",
               f"실명 독자가 확인한 단계는 {a['human_checked_steps']}개다. 모든 단계와 명제 대조의 실명 확인이 갖춰진 단위는 {a['stages'][5]}개다. [읽기 대기열](ROADMAP.md)"]
    else:
        box = ["**Writing and review** · [Evidence and limits](STATUS.md) · [Progress over time](PROGRESS.md)",
               f"Of {a['units']} units, {a['full']} give full arguments under their stated inputs, {a['outlined']} give outlines and {a['statement_only']} give statements only.",
               f"{grades['L2']} units hold L2 for an AI review of a written argument. Of {a['written_steps']} current steps, {a['ai_reviewed_steps']} have an AI review identifying that specific inference.",
               f"Named readers have checked {a['human_checked_steps']} current steps. {a['stages'][5]} units have named checks for all steps and the statement comparison. [Reader queue](ROADMAP.md)"]
    text = replace_once(text, r"^>[^\n]*(?:\n>[^\n]*)*", "  \n".join("> "+s for s in box), re.M)
    for field, label in (KOREAN_NAMES if ko else TRACK_NAMES).items():
        text = re.sub(r"\[[^]\n]+\]\((tracks/" + field + r"/README\.md|docs/ko/" + field + r"\.md)\)", lambda m: "[" + label + "](" + m[1] + ")", text)
    for i in range(5):
        g = f"L{i}"
        text, n = re.subn(r"^(\| "+g+r" \| .*? \| )[\d,]+( \|)$",
                          lambda m: m[1]+str(grades[g])+m[2], text, flags=re.M)
        if n != 1:
            raise ValueError("Missing grade row "+g)
    return text


def share(n, d):
    return f"{n:,} ({n/d:.4%})"


def status(data, grades, units, rows, suppliers, ko):
    a, den = data["all"], data["denominators"]
    wc, physical = den["weighted_core_lines"], den["source_lines"]
    nfiles = den["source_files"]
    text = ["| 분야 | 단위 | 전체 논증 | 개요 | 명제만 |" if ko else
            "| Primary field | Units | Full | Outlined | Statement only |", "|---|---:|---:|---:|---:|"]
    for k, label in (KOREAN_NAMES if ko else TRACK_NAMES).items():
        r = data["tracks"][k]
        text.append(f"| {label} | {r['units']} | {r['full']} | {r['outlined']} | {r['statement_only']} |")
    total = "전체" if ko else "All units"
    text.append(f"| **{total}** | **{a['units']}** | **{a['full']}** | **{a['outlined']}** | **{a['statement_only']}** |")
    gl = ", ".join(f"L{i} {grades['L'+str(i)]}" for i in range(5))
    l2 = {u["id"] for u in units if u["grade"] == "L2"}
    assessed = {uid for uid, row in rows.items() if row["stages"][4]}
    prefix = "../../" if ko else ""
    def link_units(ids):
        return ", ".join(f"[{uid}]({prefix}units/{uid}.md)" for uid in sorted(ids)) or ("없음" if ko else "none")
    if ko:
        text += ["", f"최고 근거 등급별 단위 수는 {gl}이다. Full은 해당 단위의 가정을 받아들였을 때 논증을 모두 썼다는 뜻이다. 개요를 포함해 현 판본의 서술 전체에 AI 검토가 있는 단위는 {a['stages'][4]}개다. L2에만 속하는 단위는 {link_units(l2-assessed)}이며 현 판본 전체 검토에만 속하는 단위는 {link_units(assessed-l2)}이다. 단위 등급은 한정된 논증의 검토도 기록하고, 현 판본 검토 수는 개요의 판정도 센다. 현 판본 {a['written_steps']}단계 중 특정 추론에 대한 AI 검토는 {a['ai_reviewed_steps']}단계, 독자의 확인은 {a['human_checked_steps']}단계다. [등급](FAQ.md) · [실명 검토](signoffs/README.md)",
                 "", "### 서술에서 인용한 Lean 줄", "",
                 "범주마다 현재 단계가 인용한 원문 줄의 합집합을 센다. 같은 범주 안에서 겹치는 줄은 한 번만 센다. 물리적 분모는 고정된 src 아래 모든 Lean 파일의 줄바꿈 문자 수(wc -l 합계)다. 코어 줄은 고정 그래프의 프로젝트 선언에 지정된 양 끝 포함 구간의 한 줄이다. 문헌 노드는 의존 탐색을 멈추도록 표시한 선언이다. 명칭과 출판된 정리가 일치하는지 여부는 따로 대조해야 한다.", "",
                 f"| 범주 | 고정 원문 {nfiles:,}개 파일의 {physical:,}줄 중 | 가중 코어 {wc:,}줄 중 |"]
    else:
        text += ["", f"The highest evidence grades are {gl}. Full means the argument is written under the unit’s stated inputs. {a['stages'][4]} units have an AI assessment of their entire current prose, including outlines. L2 alone includes {link_units(l2-assessed)}. Current-prose review alone includes {link_units(assessed-l2)}. The grade can cover a scoped argument, and a current-prose review can cover an outline. Of {a['written_steps']} current steps, {a['ai_reviewed_steps']} have a step-specific AI review and {a['human_checked_steps']} have a qualifying personal check. [Evidence levels](FAQ.md) · [Named checks](signoffs/README.md)",
                 "", "### Lean lines cited in the writing", "",
                 "Each row counts the union of the Lean ranges cited by current steps in that category. Overlapping lines count once within a row. The physical denominator sums newline characters (wc -l) across every Lean file in the pinned src directory. A core line is one line of a project declaration’s inclusive source range in the pinned graph. A literature node is a declaration where the dependency traversal stops. Its agreement with a published result requires a separate comparison.", "",
                 f"| Scope | Of {physical:,} physical lines in all {nfiles:,} pinned source files | Of {wc:,} weighted core lines |"]
    text.append("|---|---:|---:|")
    for key, labels in METRICS.items():
        c = a["cited_lines"][key]
        text.append(f"| {labels[int(ko)]} | {share(c['all_files'],physical)} | {share(c['weighted_core_weight'],wc)} |")
    if ko:
        text += ["", f"서로 다른 범주의 인용 줄은 겹칠 수 있다. 별도의 색인 위치 표는 코어 줄을 지배 트리에서 가장 가까운 상위 단위에 배정한다. 위치는 그 줄을 설명했거나 읽었다는 뜻이 아니다. V와 F 공급자의 지배 영역은 서로 겹치지 않으며 합계는 코어 {suppliers['vf']:,}줄이다. [색인 위치·분모·추이](../../PROGRESS.md) · [분야별 표](../../dashboard/README.md)"]
    else:
        text += ["", f"Citations can overlap across categories. The separate index-position table assigns each core line to its nearest unit above it in the dominator tree. Position says where a line sits in the index. It provides no evidence that anyone explained or read that line. The V and F suppliers dominate disjoint regions totaling {suppliers['vf']:,} core lines. [Index position, denominators and history](PROGRESS.md) · [Field breakdown](dashboard/README.md)"]
    return "\n".join(text)


def mirror(text):
    def target(match):
        dest = match[1]
        if dest.startswith(("#", "https:", "http:")):
            return match[0]
        path, sep, anchor = dest.partition("#")
        return "]("+posixpath.relpath(path, "docs/ko")+sep+anchor+")"
    return re.sub(r"\]\(([^)\n]+)\)", target, text)


def reading_orders(root, units):
    """Refresh assigned page counts using the linked edition rather than a unit-wide page total."""
    path = root / "docs/reading-orders.md"
    text = path.read_text()
    sizes = {}
    for unit in units:
        for edition in unit["expositions"]:
            doc = edition["document"]
            if doc.startswith("notes/") and doc.endswith(".md"):
                first, last = edition["pages"]
                sizes[doc] = last - first + 1
    for packet in read(root / "data/notes_starters.json")["starters"].values():
        sizes[packet["path"]] = packet["size_pages"]

    def assigned(cell):
        links = re.findall(r"\]\(\.\./([^)]+)\)", cell)
        if len(links) == 1 and links[0] in sizes:
            return sizes[links[0]]
        pages = re.search(r"pp\. (\d+)–(\d+)", cell)
        if pages is None:
            raise ValueError("Reading assignment has no registered extent: " + cell)
        return int(pages[2]) - int(pages[1]) + 1

    def week(row):
        cells = [c.strip() for c in row.group().strip("|").split("|")]
        if len(cells) != 6:
            raise ValueError("A field itinerary must have five assignments and one total")
        lengths = [assigned(cell) for cell in cells[:5]]
        for i, n in enumerate(lengths):
            cells[i] = replace_once(cells[i], r"\(\d+\)$", f"({n})")
        return "| " + " | ".join([*cells[:5], f"**{sum(lengths)}**"]) + " |"

    text, field_count = re.subn(r"^\| \*\*[^\n]+$", week, text, flags=re.M)
    if field_count != len(TRACK_NAMES):
        raise ValueError("A reading order is missing a primary field")
    lengths = []
    def conditional(row):
        cells = [c.strip() for c in row.group().strip("|").split("|")]
        docs = re.findall(r"\]\(\.\./(notes/units/[^)]+)\)", cells[1])
        if not docs:
            raise ValueError("A conditional assignment has no written note")
        group = [sizes[doc] for doc in docs]
        lengths.extend(group)
        cells[2] = " + ".join(map(str, group))
        return "| " + " | ".join(cells) + " |"

    text = re.sub(r"^\| \d+ \| [^\n]+$", conditional, text, flags=re.M)
    text = replace_once(text, r"(?:## The whole conditional deduction · )\d+ pages",
                        f"## The whole conditional deduction · {sum(lengths)} pages")
    overview = re.search(r"\(\.\./OVERVIEW\.md\), \*\*(\d+) pages\*\*", text)
    packet = sizes["notes/analytic/README.md"]
    text = re.sub(r"(\(\.\./notes/analytic/README\.md\), \*\*)\d+( pages\*\*)",
                  lambda m: m[1] + str(packet) + m[2], text)
    text = replace_once(text, r"## One afternoon · \d+ pages", f"## One afternoon · {int(overview[1]) + packet} pages")
    return path, text


def documents(root):
    units = [read(p) for p in (root/"units").glob("*.yaml") if not p.name.endswith(".steps.yaml")]
    grades = Counter(u["grade"] for u in units)
    snapshot = pipeline(root)
    data = snapshot["counts"]
    route, itinerary = reading_orders(root, units)
    result = {route: itinerary}
    for name in ["README.md", "README.ko.md"]:
        file = root/name
        result[file] = entry(file.read_text(), data["all"], grades, name.endswith(".ko.md"))
    result[root/"docs/ko/README.md"] = mirror(result[root/"README.ko.md"])
    for name in ["STATUS.md", "docs/ko/STATUS.md"]:
        path = root/name
        block = "<!-- front:status:start -->\n"+status(data, grades, units, snapshot["units"], snapshot["suppliers"], name.startswith("docs/"))+"\n<!-- front:status:end -->"
        result[path] = replace_once(path.read_text(), r"<!-- front:status:start -->.*?<!-- front:status:end -->", block, re.S)
    counts = data["all"]
    for name in ["FAQ.md", "docs/ko/FAQ.md"]:
        path = root / name
        if name.startswith("docs/"):
            census = f"현재 {counts['units']}개 중 전체 논증 {counts['full']}개, 개요 {counts['outlined']}개, 명제만 {counts['statement_only']}개다."
        else:
            census = f"Of {counts['units']} units, {counts['full']} have full arguments, {counts['outlined']} have outlines and {counts['statement_only']} have statements only."
        result[path] = replace_once(path.read_text(), r"<!-- front:faq -->.*?<!-- /front:faq -->", "<!-- front:faq -->" + census + "<!-- /front:faq -->", re.S)
    notes = root / "notes/README.md"
    result[notes] = replace_once(notes.read_text(), r"The atlas indexes [0-9,]+ units", f"The atlas indexes {counts['units']} units")
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    for path, text in documents(args.root).items():
        if path.read_text() != text:
            if args.check:
                raise SystemExit("Stale live census in "+str(path.relative_to(args.root)))
            path.write_text(text,encoding="utf-8")


if __name__=="__main__":
    main()
