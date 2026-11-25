"""Assign each allChi dominator-tree line to a single nearest indexed statement."""
from collections import defaultdict
import json

STATUS = ("Full", "Outlined", "Statement only")


def nearest_positions(units, anchors):
    owners = defaultdict(set)
    for uid, unit in units.items():
        for n in set(unit["heads"]) & anchors.keys():
            owners[n].add(uid)
    if "allChi" not in owners:
        raise ValueError("The root needs an indexed statement")
    weights = {n: anchors[n]["weight"] for n in owners}
    for n in owners:
        ancestor = anchors[n]["parent"]
        while ancestor is not None and ancestor not in owners:
            ancestor = anchors[ancestor]["parent"]
        if ancestor is not None:
            weights[ancestor] -= anchors[n]["weight"]
    totals = dict.fromkeys(STATUS, 0)
    full_l2 = 0
    assignment = []
    for n in sorted(owners):
        uid = min(owners[n])
        row = units[uid]
        weight = weights[n]
        if weight < 0:
            raise ValueError("Nearest-statement weights must be nonnegative")
        totals[row["status"]] += weight
        if row["status"] == "Full" and row["grade"] == "L2":
            full_l2 += weight
        assignment.append(dict(name=n, primary_units=sorted(owners[n]), owner=uid, weight=weight))
    if sum(totals.values()) != anchors["allChi"]["weight"]:
        raise ValueError("Nearest-statement regions do not partition the core")
    return dict(rule="Use scoped statement heads only, assign each residual region to its nearest head, and choose the least unit ID in Unicode code-point order among co-owners, independently of grade or status.",
                status=totals, full_l2=full_l2, shared_heads=sum(len(v)>1 for v in owners.values()), heads=assignment)


def has_ancestor(anchors, child, ancestor):
    while child is not None:
        if child == ancestor:
            return True
        child = anchors[child]["parent"]
    return False


def supplier_weights(units, anchors):
    names = {uid: units[uid]["heads"][0] for uid in ("P010", "P011", "P013", "T02", "D575", "P017", "B07", "B05")}
    v, f = names["P013"], names["T02"]
    if has_ancestor(anchors, v, f) or has_ancestor(anchors, f, v):
        raise ValueError("The V and F supplier subtrees overlap")
    if not has_ancestor(anchors, names["P011"], names["P010"]):
        raise ValueError("The row implication must lie under its closed parent")
    result = {uid: anchors[n]["weight"] for uid,n in names.items()}
    result.update(vf=result["P013"] + result["T02"], outside_row=result["P010"] - result["P011"])
    return result


def scope_text(den, supplier):
    return [
        f"A core line is one unit of weight for a physical source line of a reachable core declaration in the graph rooted at `allChi` ({den['weighted_core_lines']:,} in total). "
        "A literature node is a declaration marked as a stopping point by the extraction’s name or module rule, so the graph does not follow its proof or establish its relation to any publication.",
        f"The complete pinned source contains {den['source_lines']:,} physical lines in {den['source_files']:,} Lean files. "
        "This is the count of newline characters in every `.lean` file under `lean/src/` in the pinned archive. Every nonempty file ends with a newline.",
        f"The V and F supplier subtrees are disjoint. They contain {supplier['P013']:,} and {supplier['T02']:,} core lines, respectively, or {supplier['vf']:,} together. "
        f"The closed character statement P010 contains a further {supplier['outside_row']:,} core lines outside the subtree of its row implication P011. "
        "These are source-graph locations. The atlas contains no human-readable derivation of either supplier.",
    ]

def lookup_scope(root):
    inventory = json.loads((root/"progress/source_inventory.json").read_bytes())
    anchors = json.loads((root/"progress/dominators.json").read_bytes())["anchors"]
    ids = ("P010", "P011", "P013", "T02", "D575", "P017", "B07", "B05")
    units = {uid: {"heads": [json.loads((root/"units"/(uid+".yaml")).read_bytes())["lean"][0]["name"]]} for uid in ids}
    return scope_text(inventory, supplier_weights(units, anchors))
