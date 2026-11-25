"""Validate edition-specific human reading records and compute their public state."""
from collections import defaultdict
from datetime import date
from hashlib import sha256
from html import escape
import json
import math
from pathlib import Path
import re
import unicodedata

from signoff_yaml import read_yaml

ATTESTATION = "I read the edition identified above myself."
NOTICE = "AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved"
INDEPENDENCE = "I checked independently of other readers."
INDEPENDENCE_SENTENCE = re.compile(
    r"(?:^|(?<=[.!?])[ \t]+)[ \t]*(?:[-*][ \t]+)?" + re.escape(INDEPENDENCE) + r"(?=\s|$)",
    re.IGNORECASE | re.MULTILINE)
VERDICTS = {"checked-correct", "correct-with-reservation", "gap-found", "error-found",
            "could-not-follow", "not-attempted"}
OBJECTIONS = {"gap-found", "error-found"}
FINGERPRINT = re.compile(r"[0-9a-f]{64}\Z")
STEP = re.compile(r"S[1-9][0-9]*[a-z]*\Z")
REQUIRED = {"reader", "unit", "edition_sha256", "scope", "verdict", "what_i_did",
            "time_spent_hours", "reservations", "conflicts_of_interest", "ai_assistance_used",
            "ai_assistance_description", "date", "attestation"}
ROOT = Path(__file__).resolve().parents[1]


def require(condition, message):
    if not condition:
        raise ValueError(message)


def string(value):
    return isinstance(value, str) and bool(value.strip())


def folded(value):
    return " ".join(unicodedata.normalize("NFKC", value).casefold().split())


def slug(name):
    value = unicodedata.normalize("NFKD", folded(name))
    latin = re.sub(r"[^a-z0-9]+", "-", value.encode("ascii", "ignore").decode()).strip("-")
    return latin[:64].rstrip("-") or "reader-" + sha256(value.encode()).hexdigest()[:10]


def is_maintainer(reader):
    return folded(reader["name"]) == "gunhee cho"


def is_orcid(value):
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{4}-\d{4}-\d{3}[\dX]", value):
        return False
    compact = value.replace("-", "")
    checksum = 0
    for char in compact[:-1]:
        checksum = (checksum + int(char)) * 2
    last = (12 - checksum % 11) % 11
    return compact[-1] == ("X" if last == 10 else str(last))


def known_editions(manifest):
    current = manifest["edition_sha256"]
    editions = {item["edition_sha256"]: item["steps"] for item in manifest.get("history", [])}
    editions[current] = {s["id"]: s["sha256"] for s in manifest["steps"] if s.get("status") != "withdrawn"}
    return editions


def read_manifest(root, uid):
    require(isinstance(uid, str) and re.fullmatch(r"[A-Za-z0-9]+(?:[.-][A-Za-z0-9]+)*", uid), "Invalid unit ID")
    path = root / "units" / (uid + ".steps.yaml")
    require(path.is_file(), f"{uid} has no identified checklist edition")
    return json.loads(path.read_text())


def record_prefix(r):
    return f'{r["date"]}_{r["unit"]}_{slug(r["reader"]["name"])}_'


def validate_one(r, manifest, filename=None):
    require(isinstance(r, dict) and REQUIRED <= r.keys(), "Missing one or more required reader record fields")
    require(set(r) <= REQUIRED | {"step_sha256", "resolves"}, "Unknown field in record (examples cannot be submitted)")
    rd = r["reader"]
    require(isinstance(rd, dict) and {"name","field","level"} <= rd.keys() <= {"name","field","level","affiliation","orcid"}, "Invalid reader fields")
    require(string(rd["name"]) and string(rd["field"]), "Reader name and field are required")
    require(rd["level"] in {"faculty","postdoc","phd-student","other"}, "Invalid reader level")
    require("affiliation" not in rd or string(rd["affiliation"]), "Empty affiliation")
    require("orcid" not in rd or is_orcid(rd["orcid"]), "Invalid ORCID or checksum")
    require(r["unit"] == manifest["unit"], "Record unit and checklist differ")
    try:
        require(date.fromisoformat(r["date"]).isoformat() == r["date"], "Use an ISO calendar date")
    except (TypeError, ValueError) as error:
        raise ValueError("Use YYYY-MM-DD for the date") from error
    require(r["attestation"] == ATTESTATION, "Missing or changed personal attestation")
    require(all(string(r[k]) for k in ("what_i_did", "reservations", "conflicts_of_interest")), "Describe the work, reservations and conflicts (or say none)")
    require(type(r["time_spent_hours"]) in (int, float) and math.isfinite(r["time_spent_hours"]) and r["time_spent_hours"] >= 0, "Invalid hours")
    require(r["ai_assistance_used"] in ("none","some","substantial"), "Invalid AI-assistance level")
    require(isinstance(r["ai_assistance_description"], str) and (r["ai_assistance_used"] == "none" or string(r["ai_assistance_description"])), "Describe the AI assistance used")
    ed = r["edition_sha256"]
    require(isinstance(ed, str) and FINGERPRINT.fullmatch(ed), "Invalid edition SHA-256")
    editions = known_editions(manifest)
    require(ed in editions, "Unknown edition; the cited checklist and its hashes must be archived first")
    original = editions[ed]
    if "step_sha256" in r:
        stored = r["step_sha256"]
        require(isinstance(stored, dict), "Invalid step fingerprints")
        candidates = [original] + [item["steps"] for item in manifest.get("history", []) if item["edition_sha256"]==ed]
        matching = [old for old in candidates if all(old.get(k)==v for k,v in stored.items()) and
                    (r["scope"] != "whole-note" or set(old)==set(stored))]
        require(matching, "Unknown historical step fingerprints")
        original = matching[0]
    scope = r["scope"]
    if isinstance(scope, dict):
        require(set(scope) == {"steps"} and isinstance(scope["steps"], list) and bool(scope["steps"]), "List the checked steps")
        steps = scope["steps"]
        require(all(isinstance(s, str) and STEP.fullmatch(s) and s in original for s in steps), "Unknown, withdrawn, or invalid step on that edition")
        require(len(set(steps)) == len(steps), "Duplicate step")
        targets = set(steps)
    else:
        require(scope in ("whole-note", "statement-vs-lean"), "Invalid scope")
        targets = set(original) if scope == "whole-note" else {"statement-vs-lean"}
    verdicts = r["verdict"]
    require(isinstance(verdicts, dict) and targets and set(verdicts) == targets, "Supply one verdict for every target in scope")
    require(all(v in VERDICTS for v in verdicts.values()), "Unknown verdict")
    if any(v in OBJECTIONS | {"correct-with-reservation"} for v in verdicts.values()):
        require(folded(r["reservations"]) not in {"none", "n/a", "-"}, "Describe the objection or reservation")
    hashes = {k: original[k] for k in sorted(targets) if k != "statement-vs-lean"}
    if filename is not None or "step_sha256" in r:
        require(r.get("step_sha256") == hashes, "Step fingerprints do not match the identified checklist")
    if filename is not None:
        require(re.fullmatch(re.escape(record_prefix(r)) + r"[1-9]\d*\.yaml", filename), "Filename disagrees with reader, unit or date")
    refs = r.get("resolves", {})
    require(isinstance(refs, dict), "resolves must map each target to a list of prior record filenames")
    for key, names in refs.items():
        require(verdicts.get(key) == "checked-correct" and isinstance(names, list) and names and all(string(n) and Path(n).name == n for n in names) and len(set(names))==len(names), "Resolution needs a positive target and named earlier objections")
    return hashes


def reader_groups(records):
    """Treat matching self-declared names or ORCIDs as one identity across this record set."""
    aliases = {}
    groups = {}
    for name, record in records:
        reader = record["reader"]
        keys = {("name", folded(reader["name"]))}
        if reader.get("orcid"):
            keys.add(("orcid", reader["orcid"]))
        members = set(keys)
        for key in keys:
            members.update(aliases.get(key, ()))
        for key in members:
            aliases[key] = members
        groups[name] = next(iter(keys))
    return {name:min(aliases[key]) for name,key in groups.items()}


def target_hash(record, target, manifest):
    if target != "statement-vs-lean":
        return record["step_sha256"].get(target)
    if record["edition_sha256"] == manifest.get("edition_sha256"):
        return manifest.get("statement_sha256")
    return next((e.get("statement_sha256") for e in manifest.get("history", [])
                 if e["edition_sha256"] == record["edition_sha256"]), None)


def step_prose(record, target, manifest):
    expected = record["step_sha256"].get(target)
    for step in manifest.get("steps", []):
        if step["id"] == target and step["sha256"] == expected:
            return step.get("claim"), step.get("passage_sha256")
    for edition in manifest.get("history", []):
        if edition["edition_sha256"] == record["edition_sha256"] and edition["steps"].get(target) == expected:
            return (edition.get("step_texts", {}).get(target), edition.get("step_passages", {}).get(target))
    return None, None


def unchanged_objection(record, target, manifest, active):
    """A new edition or a changed citation alone cannot supersede an objection."""
    if target == "statement-vs-lean":
        before = target_hash(record, target, manifest)
        return before is None or before == manifest.get("statement_sha256")
    if target not in active:
        return False
    old_hash = record["step_sha256"][target]
    step = active[target]
    if old_hash == step["sha256"]:
        return True
    claim, passage = step_prose(record, target, manifest)
    # Without evidence of a change, keep the objection open on the surviving target.
    return ((claim is None or claim == step.get("claim")) and
            (passage is None or passage == step.get("passage_sha256")))


def validate_resolutions(records, manifests):
    lookup = dict(records)
    identities = reader_groups(records)
    maintainers = {identities[n] for n,r in records if is_maintainer(r["reader"])}
    for name, r in records:
        for target, refs in r.get("resolves", {}).items():
            require(identities[name] not in maintainers, "A maintainer cannot close a dispute on unchanged text")
            for prev in refs:
                old = lookup.get(prev, {})
                require(old.get("unit") == r["unit"] and old.get("verdict", {}).get(target) in OBJECTIONS,
                        "A resolution must identify an objection on this unit and target")
                require(identities[prev] != identities[name], "The resolving reader must differ from the objector")
                manifest = manifests[r["unit"]]
                same_edition = old["edition_sha256"] == r["edition_sha256"]
                before = target_hash(old, target, manifest)
                after = target_hash(r, target, manifest)
                same_target = before == after and (bool(after) or same_edition)
                if not same_target and target != "statement-vs-lean":
                    original = step_prose(old, target, manifest)
                    same_target = all(original) and original == step_prose(r, target, manifest)
                require(same_target, "A resolution must address the same target text")
                require(old["date"] <= r["date"], "A resolution predates its objection")


def load_records(root=ROOT):
    root = Path(root)
    records = []
    cache = {}
    directory = root / "signoffs/records"
    for p in sorted(directory.glob("*")):
        if p.name == ".gitkeep":
            continue
        require(p.is_file() and not p.is_symlink() and p.suffix == ".yaml", f"Unexpected record entry: {p.name}")
        try:
            r = read_yaml(p.read_text())
            uid = r.get("unit")
            if uid not in cache:
                cache[uid] = read_manifest(root, uid)
            validate_one(r, cache[uid], p.name)
        except (ValueError, KeyError, TypeError) as exc:
            raise ValueError(f"{p.name}: {exc}") from exc
        records.append((p.name, r))
    validate_resolutions(records, cache)
    return records


def independent(checks):
    qualifying = [c for c in checks if c["independent"]]
    return len({c["identity"] for c in qualifying}) >= 2


def human_state(root, uid, manifest, records=None):
    if records is None:
        records = load_records(root)
    identities = reader_groups(records)
    maintainers = {identities[n] for n,r in records if is_maintainer(r["reader"])}
    records = [(n,r) for n,r in records if r["unit"]==uid]
    ed = manifest.get("edition_sha256")
    active_steps = {s["id"]: s for s in manifest.get("steps",[]) if s.get("status") == "active"}
    cells = {s["id"]: {"state": "withdrawn" if s.get("status") == "withdrawn" else "awaiting human check", "checks":[], "independent_pair":False}
             for s in manifest.get("steps",[])}
    cells["statement-vs-lean"] = {"state":"awaiting human check", "checks":[], "independent_pair":False}
    resolved = {(old, sid) for _,r in records for sid, refs in r.get("resolves",{}).items() for old in refs}
    whole_note = []
    for n,r in sorted(records, key=lambda pair:(pair[1]["date"], int(pair[0].rsplit("_",1)[1][:-5]), pair[0])):
        current = r["edition_sha256"] == ed
        rd = r["reader"]
        for sid,v in r["verdict"].items():
            cell = cells.setdefault(sid, {"state":"withdrawn", "checks":[], "independent_pair":False})
            same_text = unchanged_objection(r, sid, manifest, active_steps)
            hash_matches = sid == "statement-vs-lean" or (
                sid in active_steps and active_steps[sid]["sha256"] == r["step_sha256"].get(sid))
            check = dict(name=rd["name"], date=r["date"], verdict=v, edition_sha256=r["edition_sha256"],
                         status="current" if current and hash_matches else "superseded", maintainer=identities[n] in maintainers, record=n,
                         identity=identities[n], same_text=same_text, ai_assistance=r["ai_assistance_used"],
                         resolved=(n,sid) in resolved, orcid=rd.get("orcid"),
                         independent=bool(INDEPENDENCE_SENTENCE.search(r["what_i_did"]))
                         and folded(r["conflicts_of_interest"]) == "none" and r["ai_assistance_used"] != "substantial")
            cell["checks"].append(check)
        if r["scope"] == "whole-note":
            whole_note.append(n)
    positive_records = []
    for cell in cells.values():
        if cell["state"] == "withdrawn":
            continue
        live = [c for c in cell["checks"] if c["status"]=="current"]
        if any(c["same_text"] and c["verdict"] in OBJECTIONS and not c["resolved"] for c in cell["checks"]):
            cell["state"] = "disputed"
            continue
        latest = {}
        for c in live:
            latest[c["identity"]] = c
        positive = [c for c in latest.values() if c["verdict"]=="checked-correct"]
        if positive:
            positive_records.extend(positive)
            cell["state"]="human-checked"
            cell["independent_pair"]=independent(positive)
    statement = cells.pop("statement-vs-lean")
    active = [c for c in cells.values() if c["state"]!="withdrawn"]
    checked = statement["state"] == "human-checked"
    unit = json.loads((Path(root)/"units"/(uid+".yaml")).read_bytes())
    kinds = {s.get("kind") for s in manifest.get("steps", []) if s.get("status") == "active"}
    derivation = bool(kinds & {"assembly", "case-split", "computation", "definition-unfolding", "inequality"})
    complete = bool(active) and checked and all(c["state"] == "human-checked" for c in active)
    l4 = unit["status"] == "Full" and derivation and complete
    evidence = dict(reader_count=len({c["identity"] for c in positive_records}),
                    includes_maintainer=any(c["maintainer"] for c in positive_records),
                    ai_assistance_levels=sorted({c["ai_assistance"] for c in positive_records}))
    return dict(steps=cells, statement_checked=checked, statement=statement["checks"], statement_state=statement["state"],
                whole_note=whole_note, records=[n for n,_ in records],
                l4=l4, l4_evidence=evidence,
                two_independent=bool(active) and statement["independent_pair"] and all(c["independent_pair"] for c in active))


def l4_summary(evidence):
    count = evidence["reader_count"]
    readers = "reader" if count == 1 else "readers"
    maintainer = "The maintainer contributed." if evidence["includes_maintainer"] else "The maintainer did not contribute."
    levels = ", ".join(evidence["ai_assistance_levels"])
    return (f"{count} self-declared {readers} contributed. {maintainer} "
            f"The declared AI assistance levels were {levels}. L4 covers this Full argument under its stated inputs. "
            "It establishes no claim about the inputs, V, F or RH.")


def safe_text(s):
    return re.sub(r"([\\`*_\[\]|])", r"\\\1", escape(" ".join(s.split()), quote=False))


def disputes(root, records):
    lines=["# Reader-reported gaps and errors","",NOTICE,"",
           "Each entry retains its original verdict and edition. To close an objection on the same text, a different reader other than the maintainer must address it explicitly. A change to the disputed target supersedes the old objection.",""]
    found=False
    states={}
    for n,r in records:
        for sid,v in r["verdict"].items():
            if v not in OBJECTIONS:
                continue
            if r["unit"] not in states:
                states[r["unit"]] = human_state(root,r["unit"],read_manifest(root,r["unit"]),records)
            st=states[r["unit"]]
            checks=st["statement"] if sid=="statement-vs-lean" else st["steps"][sid]["checks"]
            check=next(x for x in checks if x["record"]==n)
            status="resolved" if check["resolved"] else "open"
            if not check["resolved"] and not check["same_text"]:
                status = "superseded by changed or withdrawn target"
            elif check["status"] == "superseded":
                status += " on unchanged target in a later edition"
            unit=r["unit"]
            lines.extend([f"## {unit} · {sid} · {v}","",f"**{status.capitalize()}.** {safe_text(r['reader']['name'])}, {r['date']}. Edition `{r['edition_sha256']}`.","",
                          safe_text(r['reservations']),"",f"[Original record](../signoffs/records/{n}) · [Checklist](../units/{unit}.check.md)",""])
            for newer, rr in records:
                if n in rr.get("resolves",{}).get(sid,[]):
                    lines.extend([f"[Resolution by {safe_text(rr['reader']['name'])}](../signoffs/records/{newer})",""])
            found=True
    if not found:lines.extend(["There are no submitted gap or error records.",""])
    return "\n".join(lines)


def validate(root=ROOT):
    try:
        records=load_records(root)
        path=Path(root)/"questions/disputes.md"
        require(path.is_file() and path.read_text()==disputes(root,records), "Regenerate questions/disputes.md")
        return []
    except (ValueError,KeyError,TypeError,OSError) as exc:
        return [str(exc)]
