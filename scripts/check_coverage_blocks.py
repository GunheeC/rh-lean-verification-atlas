"""Replay the proof-block partition with the atlas's established nearest-head rule."""
from collections import Counter
import json
from pathlib import Path

from atlas_files import unit_files
from coverage_closure import closed_units


def verify(root):
    root = Path(root)

    def read(path):
        return json.loads((root / path).read_text(encoding="utf-8"))

    def check(condition, message):
        if not condition:
            raise ValueError(f"coverage blocks: {message}")

    dataset = read("data/coverage_blocks.json")
    anchors = read("progress/dominators.json")
    positions = read("progress/index_position.json")
    history = json.loads((root / "progress/history.jsonl").read_text().splitlines()[-1])["counts"]
    units = {p.stem: json.loads(p.read_text()) for p in unit_files(root)}
    source_heads = positions["heads"]
    named = anchors["anchors"]
    head_by_owner = {item["owner"]: item["name"] for item in source_heads}
    method = dataset["method"]
    roots = {head_by_owner[uid]: block for block, ids in method["explicit_subtree_roots"].items() for uid in ids}
    outer = set(method["assembly_residual_owner_ids"])
    status_key = {"Full": "full", "Outlined": "outline", "Statement only": "statement_only"}
    blocks = {item["id"]: item for item in dataset["blocks"]}
    expected = {key: [] for key in blocks}
    for head in source_heads:
        name, uid = head["name"], head["owner"]
        n = name
        while n is not None and n not in roots:
            n = named[n]["parent"]
        key = roots[n] if n is not None else ("assembly" if uid in outer else method["fallback"])
        expected[key].append({"name": name, "unit": uid, "lines": head["weight"], "level": status_key[units[uid]["status"]]})

    total = dataset["total"]
    levels = Counter()
    for key, rr in expected.items():
        item = blocks[key]
        check(rr == item["position_owners"], f"{key} assignment")
        counted = Counter()
        for row in rr:
            counted[row["level"]] += row["lines"]
        check(sum(counted.values()) == item["lines"], f"{key} weight")
        check(set(item["by_exposition"]) == {r["id"] for r in dataset["levels"]}, f"{key} categories")
        check(all(counted.get(k, 0) == n for k, n in item["by_exposition"].items()), f"{key} status")
        check(item["human_checks"] == 0, f"{key} current human stage")
        levels.update(counted)
        for pin in item["entries"]:
            candidates = units[pin["unit"]]["lean"]
            check(any(all(p[k] == pin[k] for k in ("name", "file", "line0", "line1")) for p in candidates), f"{key} Lean source")
        for evidence in item["review_evidence"]:
            for record in evidence["records"]:
                check(any(all(x.get(k) == v for k,v in record.items()) for x in units[evidence["unit"]]["grade_evidence"]), f"{key} review scope")
                check((root / record["review"]).is_file(), f"{key} review path")
        for reading in item["readings"]:
            if reading["document"] == "atlas":
                check((root / reading["path"]).is_file(), f"{key} reading")
                editions=read("data/round6_review_corrections.json")["pillar_editions"]
                if reading["path"] in editions:
                    import hashlib
                    published=editions[reading["path"]]
                    check(1 <= reading["pages"][0] <= reading["pages"][1] <= published["pages"], f"{key} pillar print folios")
                    check(hashlib.sha256((root/reading["path"]).read_bytes()).hexdigest()==published["sha256"],f"{key} pillar edition")
    check(sum(levels.values()) == anchors["total"] == total, "core total")
    check({status_key[k]: v for k,v in positions["status"].items()} == dict(levels), "local status replay")
    for row in dataset["levels"]:
        check(row["lines"] == levels[row["id"]] and row["percent"] == round(100*row["lines"]/total,4), "level bar")
    counts = history["all"]; evidence = counts["cited_lines"]; c = dataset["citations"]
    core = evidence["written"]["in_weighted_core"]
    check(core == evidence["written"]["weighted_core_weight"], "distinct cited core lines vs weighted intersection")
    facts = {"distinct_physical": evidence["written"]["all_files"], "core": core, "core_full": evidence["full"]["in_weighted_core"],
             "core_outline": evidence["outlined"]["in_weighted_core"], "core_outline_only": core-evidence["full"]["in_weighted_core"],
             "core_uncited":total-core, "full_source_physical_lines":history["denominators"]["source_lines"],
             "steps": counts["written_steps"], "full_units": counts["full"], "human_checked_steps": counts["human_checked_steps"],
             "all_prerequisites_full": len(closed_units(root))}
    check(all(c[k] == v for k,v in facts.items()), "active-step citation unions or closure evidence")
    check(c["core_percent"]==round(100*core/total,4) and c["core_uncited_percent"]==round(100*(total-core)/total,4),"citation percentages")
    check(method["source_graph_sha256"]==anchors["graph_sha256"],"source graph")
    supplier = dataset["supplier_boundaries"]
    for block in ("v","f"):
        entry = supplier[block]
        named_root=head_by_owner[entry["head"]]
        check(blocks[block]["lines"] == entry["whole_cone"] == named[named_root]["weight"], f"{block} entire supplier region")
        opposite=supplier["f" if block=="v" else "v"]["head"]
        ancestor=named_root
        while ancestor is not None:
            check(ancestor != head_by_owner[opposite], "supplier cones overlap")
            ancestor=named[ancestor]["parent"]
        pillar=(root/entry["first_two_levels"]).read_text()
        check(all(uid in units and ("/"+uid+".md") in pillar for uid in entry["first_level_units"]+entry["second_level_units"]),f"{block} two-level map entries")
    check(supplier["disjoint"] and supplier["union"] == blocks["v"]["lines"] + blocks["f"]["lines"], "V/F disjoint union")
    check(c["full_outline_overlap_in_core"]==c["core_full"]+c["core_outline"]-core,"Full/Outline citation overlap")
    check(supplier["percentage"]==round(100*supplier["union"]/total,4),"V/F percentage")
    return None


if __name__=="__main__":
    verify(Path(__file__).resolve().parents[1])
    print("Proof-block coverage partition, local writing status, citation and review payload agree.")
