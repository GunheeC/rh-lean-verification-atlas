"""Count the union of physical citations in active, edition-bound steps."""
from collections import defaultdict

KINDS = ("written", "full", "outlined", "ai_reviewed", "ai_reviewed_prose", "human_checked")
MEASURES = ("all_files", "in_raw_files", "in_weighted_core", "weighted_core_weight")


def merged(intervals):
    """Sorted disjoint closed integer ranges; adjacent intervals may be joined."""
    out = []
    for lo, hi in sorted(intervals):
        if out and lo <= out[-1][1] + 1:
            out[-1] = (out[-1][0], max(out[-1][1], hi))
        else:
            out.append((lo, hi))
    return out


def weighted_intersection(citations, runs):
    """Mass of a union intersected with sorted disjoint runs [lo,hi,(mass)]."""
    i = j = total = 0
    while i < len(citations) and j < len(runs):
        a, b = citations[i]
        x, y, *weight = runs[j]
        total += max(0, min(b, y) - max(a, x) + 1) * (weight[0] if weight else 1)
        if b <= y:
            i += 1
        else:
            j += 1
    return total


def cited_totals(rows, inventory):
    raw = inventory["files"]
    known = {**inventory["outside_files"], **raw}
    result = {}
    for kind in KINDS:
        refs = defaultdict(set)
        for row in rows:
            for ref in row["citations"][kind]:
                path, lo, hi = ref
                if path not in known or not 1 <= lo <= hi <= known[path]["lines"]:
                    raise ValueError(f"Coverage range outside pinned source inventory: {path}:{lo}-{hi}")
                refs[path].add((lo, hi))
        values = dict.fromkeys(MEASURES, 0)
        for path, intervals in refs.items():
            spans = merged(intervals)
            size = sum(hi - lo + 1 for lo, hi in spans)
            values["all_files"] += size
            if path in raw:
                values["in_raw_files"] += size
            core = weighted_intersection(spans, inventory["core_ranges"][path])
            values["in_weighted_core"] += core
            values["weighted_core_weight"] += core + weighted_intersection(spans, inventory["core_overlaps"].get(path, []))
        result[kind] = values
    return result


def citations(unit, manifest, human, reviewed_sources):
    """Keep specific step review and review of the encompassing prose distinct."""
    pools = {key: set() for key in KINDS}
    if unit["status"] not in ("Full", "Outlined"):
        return pools
    for s in manifest.get("steps", []):
        if s["status"] != "active":
            continue
        spans = {(pin["file"], pin["line0"], pin["line1"]) for pin in s["lean"]}
        pools["written"].update(spans)
        pools[unit["status"].lower()].update(spans)
        if s["source"] in reviewed_sources:
            pools["ai_reviewed_prose"].update(spans)
        for verdict in s["ai_review"]:
            if verdict["edition_sha256"] != manifest["edition_sha256"] or verdict["step_sha256"] != s["sha256"]:
                raise ValueError(f"{unit['id']}/{s['id']}: AI verdict belongs to another edition or step")
            pools["ai_reviewed"].update(spans)
        if human.get("steps", {}).get(s["id"], {}).get("state") == "human-checked":
            pools["human_checked"].update(spans)
    return pools
