#!/usr/bin/env python3
"""Apply the DB2 reading fields and compare with --check.
 
Edit the item in data/round2_reading_inputs.json to correct an imported
title, alias, background topic, hypothesis or source-backed open question.
An explicit entry in a unit's reader_overrides map takes precedence for
those fields and for prerequisites. Rebuild unit Markdown after any edit.
Grades, statements, pins, source references and expositions are read from
the current YAML and pass through unchanged. The historical DB1 grade and
hash are solely for provenance. New units outside this snapshot pass through.
"""
from atlas_files import unit_files
import argparse
from collections import Counter, defaultdict
import hashlib
import json
from pathlib import Path
import re
import sys
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
NOTICE = "AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved"


def read(path):
    return json.loads(path.read_bytes())


def serialize(document):
    return json.dumps(document, indent=2, ensure_ascii=False) + "\n"


def slugify(value):
    normalized = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", normalized).strip("-")


def reachable(edges, start, goal):
    pending = [start]
    visited = set()
    while pending:
        current = pending.pop()
        if current == goal:
            return True
        if current not in visited:
            visited.add(current)
            pending.extend(edges[current])
    return False


def project_prerequisites(records, graph):
    # Edition-specific reading input and named-head evidence can refer to the
    # same pair. Preserve both kinds of evidence without creating two links.
    candidates = defaultdict(set)
    for uid, record in records.items():
        for supplier in record["baseline"]["prerequisites"]:
            candidates[uid, supplier].add("DB1 reading prerequisite")
    navigation = defaultdict(set)
    for edge in graph["edges"]:
        uid, supplier = edge["from"], edge["to"]
        navigation[uid].add(supplier)
        for witness in edge["witnesses"]:
            if witness["consumer_role"] == witness["supplier_role"] == "primary":
                candidates[uid, supplier].add(witness["kind"])
    def priority(pair):
        reasons = candidates[pair]
        # An existing reading sequence is retained if several editions of
        # shared declarations give competing reading directions.
        return ("DB1 reading prerequisite" not in reasons, len(reasons) == 1, pair)
    wanted = defaultdict(set)
    accepted = defaultdict(dict)
    excluded = []
    for uid, supplier in sorted(candidates, key=priority):
        if reachable(wanted, supplier, uid):
            excluded.append({"from":uid, "to":supplier, "reasons":sorted(candidates[uid,supplier]),
                             "why":"Adding this edge would create a cycle in the reading order."})
            continue
        wanted[uid].add(supplier)
        accepted[uid][supplier] = sorted(candidates[uid, supplier])
    return accepted, navigation, excluded


def build(root):
    data = root / "data"
    records = read(data / "round2_reading_inputs.json")["units"]
    graph = read(data / "unit_graph.json")
    prerequisites, navigation, excluded = project_prerequisites(records, graph)
    units = {p.stem:read(p) for p in sorted(unit_files(root))}
    missing = records.keys() - units.keys()
    if missing:
        raise ValueError("Missing enrolled DB2 unit(s): "+", ".join(sorted(missing)))
    units = {k:units[k] for k in records}
    titles = {k:r.get("title",r["baseline"]["title"]).replace("--","–") for k,r in records.items()}
    slugs = {k:r.get("slug",slugify(titles[k])) for k,r in records.items()}
    if len(set(slugs.values())) != len(units):
        raise ValueError("Friendly slugs must be distinct")
    # Declarations shared between two editions remain searchable in the
    # declaration index. They are not assigned as ambiguous standalone aliases.
    aliases = {}
    potential = defaultdict(set)
    for k, u in units.items():
        r = records[k]
        terms = r.get("aliases",[]) + [r["baseline"]["title"], u["lean"][0]["name"].rsplit(".",1)[-1]]
        terms += [k + " " + titles[k]]
        for term in terms:
            potential[term.casefold()].add(k)
        aliases[k] = list(dict.fromkeys(terms))
    reserved = defaultdict(set)
    for k in units:
        for label in (k,titles[k],slugs[k]):
            reserved[label.casefold()].add(k)
    counts = Counter()
    outcome = {}
    outputs = {}
    for k, u in units.items():
        r = records[k]
        old = r["baseline"]
        q = r.get("questions", [])
        hypotheses = r["hypotheses"]
        if not hypotheses or any(h == u["statement"] for h in hypotheses):
            raise ValueError(f"{k}: invalid reading hypotheses")
        exp = next(x for x in u["expositions"] if x["document"] in ("paper2_v3","blueprint_v13"))
        u["title"], u["slug"] = titles[k], slugs[k]
        u["aliases"] = [term for term in aliases[k] if term not in (k,titles[k],slugs[k]) and
                        len(reserved[term.casefold()] | potential[term.casefold()]) == 1]
        u["background"] = r["background"]
        u["hypothesis_details"] = hypotheses
        u["hypothesis_source"] = {"document":exp["document"],"section":exp["section"],"pages":exp["pages"]}
        u["prerequisites"] = sorted(prerequisites[k])
        u["open_questions"] = [v["text"] for v in q] or ["none-recorded"]
        u["question_sources"] = sorted({v["source"] for v in q})
        u.setdefault("reader_metadata_checked", "2026-11-24")
        overrides = u.get("reader_overrides", {})
        for field, value in overrides.items():
            if field not in {"title","slug","aliases","background","hypothesis_details","open_questions","question_sources","prerequisites"}:
                raise ValueError(f"{k}: unsupported editorial override {field}")
            u[field] = value
        outputs[root / "units" / (k+".yaml")] = u
        before = old["prerequisites"]
        after = u["prerequisites"]
        counts["empty_prerequisites_before"] += not before
        counts["empty_prerequisites_after"] += not after
        counts["previously_empty_prerequisites_populated"] += bool(after) and not before
        counts["empty_open_questions_before"] += not old["open_question_count"]
        counts["unspecified_open_questions_after"] += not u["open_questions"]
        counts["none_recorded_questions_after"] += u["open_questions"] == ["none-recorded"]
        counts["explicit_questions_after"] += u["open_questions"] != ["none-recorded"]
        counts["units_with_background"] += bool(u["background"])
        counts["full_statement_in_hypotheses_before"] += old["full_statement_in_hypotheses"]
        counts["units_with_itemized_hypotheses_after"] += bool(hypotheses)
        counts["changed_titles"] += u["title"] != old["title"]
        counts["new_reading_links"] += len(set(after)-set(before))
        cone = ("selected prerequisite" if after else
                "related indexed branches only" if navigation[k] else
                "no distinct indexed supplier found")
        outcome[k] = {"baseline_sha256":old["sha256"],"prior_prerequisites":before,
                      "reading_prerequisite_evidence":{key:prerequisites[k].get(key,["Unit editorial override"]) for key in sorted(after)},
                      "reading_scope":cone, "question_state":"none-recorded" if u["open_questions"] == ["none-recorded"] else "recorded"}
    final_units = list(outputs.values())
    if len({u["slug"] for u in final_units}) != len(final_units):
        raise ValueError("A reader override introduced a duplicate slug")
    effective_graph = defaultdict(set, {u["id"]:set(u["prerequisites"]) for u in final_units})
    for uid, targets in list(effective_graph.items()):
        for target in targets:
            if reachable(effective_graph, target, uid):
                raise ValueError(f"Reading prerequisite cycle from {uid} to {target}")
    summary = {"notice":NOTICE,"units":len(units),"source_graph":"data/unit_graph.json",
               "graph_sha256":hashlib.sha256((data/"unit_graph.json").read_bytes()).hexdigest(),
               "reading_inputs":"data/round2_reading_inputs.json",
               "policy":"A new reading prerequisite needs a witnessed path between named unit statements. Component/owner links remain in Uses and Used by. Empty means no eligible distinct atlas prerequisite was selected in the captured graph; the statement may still depend on other Lean or literature inputs.",
               "counts":dict(sorted(counts.items())),
               "scope_counts":dict(sorted(Counter(r["reading_scope"] for r in outcome.values()).items())),
               "cycle_exclusions":excluded, "units_by_id":outcome}
    outputs[data/"round2_units.json"] = summary
    # DB2 remains a dated census. Apply the later statement readings to the live unit records.
    later = data / "round3_prerequisites.json"
    if later.exists():
        audited = read(later)["units"]
        for u in final_units:
            row = audited[u["id"]]
            u["prerequisites"] = row["prerequisites"]
            u["prerequisite_sources"] = {target: row["links"][target]["source"] for target in u["prerequisites"]}
    return outputs, summary


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    outputs, summary = build(args.root)
    stale = []
    for path, output in outputs.items():
        rendered = serialize(output)
        if path.is_file() and path.read_text() == rendered:
            continue
        stale.append(path.relative_to(args.root).as_posix())
        if not args.check:
            path.write_text(rendered)
    if args.check and stale:
        print("Stale enrichment: "+", ".join(stale[:12]), file=sys.stderr)
        return 1
    print(json.dumps({"units":summary["units"],"changed":len(stale),**summary["counts"]},sort_keys=True))
    return 0


if __name__ == "__main__":
    sys.exit(main())
