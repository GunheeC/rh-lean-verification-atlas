#!/usr/bin/env python3
"""Read-only local Git object/worktree audit; diagnostics never print matched values."""
import argparse
from collections import Counter
from datetime import datetime, timezone
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess


def git(root, *args):
    return subprocess.check_output(["git", "-C", str(root), *args])


def count_tokens(data):
    hits = Counter()
    for category, pattern in TOKEN_PATTERNS.items():
        hits[category] += sum(1 for _ in pattern.finditer(data))
    for m in HOME.finditer(data):
        owner = m[1].lower()
        kind = "review_service_home" if owner in SERVICE_ACCOUNTS else "personal_or_unclassified_home"
        hits[kind] += 1
    for m in EMAIL.finditer(data):
        host = m[1].lower()
        if m[0] in PUBLIC_EMAILS and whole_contact(data, m):
            category = PUBLIC_EMAILS[m[0]]
        elif host.endswith((b".invalid", b".localhost", b".test", b".example", b".local")) or host == b"localhost":
            category = "reserved_machine_email"
        else:
            category = "email_candidate"
        hits[category] += 1
    # An address with an internationalized letter or domain separator can
    # disappear entirely from the ASCII scan. Classify the full UTF-8 token.
    if b"@" in data and not data.isascii():
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError:
            text = ""
        for match in INTERNATIONAL_EMAIL.finditer(text):
            token = match[0]
            if token.isascii():
                continue
            raw = token.encode()
            partial = EMAIL.search(raw)
            if partial is not None:
                permitted = PUBLIC_EMAILS.get(partial[0])
                if not permitted or not whole_contact(raw, partial):
                    continue  # Already counted as an unlisted ASCII candidate.
                hits[permitted] -= 1
            hits["email_candidate"] += 1
    return +hits


HOME = re.compile(rb"(?:[/](?:Users|home)[/]|[A-Za-z]:[\\/]+Users[\\/]+)([A-Za-z0-9_.-]+)", re.I)
SERVICE_ACCOUNTS = {b"agent", b"oai", b"claude", b"runner", b"ubuntu"}
OWNER_NOREPLY = b"GunheeC" + b"@users.noreply.github.com"
PUBLIC_EMAILS = {
    OWNER_NOREPLY: "authorized_owner_noreply",
    b"wvx17" + b"@txstate.edu": "authorized_academic_email",
    b"geonhee" + b"@transcendq.com": "authorized_company_email",
}
PUBLIC_EMAIL_CATEGORIES = frozenset(PUBLIC_EMAILS.values())
# A period ending a sentence is a delimiter. A further domain label belongs
# to the candidate, so a domain suffix cannot turn a lookalike into a match.
EMAIL = re.compile(rb"(?<![A-Za-z0-9_.+-])[A-Za-z0-9_.%+-]+@([A-Za-z0-9.-]+\.[A-Za-z]{2,}|localhost)(?![A-Za-z0-9_-]|\.[A-Za-z0-9_-])")
INTERNATIONAL_EMAIL = re.compile(r"(?<![\w.%+-])[\w.%+-]+@[\w-]+(?:[.。．｡][\w-]+)+")
def whole_contact(data, match):
    """A known address embedded in another mailbox is not an approved contact."""
    before = data[max(0, match.start()-4):match.start()].decode("utf-8", errors="ignore")
    after = data[match.end():match.end()+4].decode("utf-8", errors="ignore")
    # An internationalized letter immediately adjoining a recognized ASCII
    # mailbox extends that mailbox. Quotation marks and prose delimiters do not.
    if (before and not before[-1].isascii() and before[-1].isalnum()) or (
            after and not after[0].isascii() and after[0].isalnum()):
        return False
    # Common RFC local-part separators may connect another word to the left.
    # Quoted standalone addresses in prose retain their exact identity.
    return not re.search(rb"[A-Za-z0-9][!#$&'*=?^|`~]+$", data[max(0, match.start()-16):match.start()])


TOKEN_PATTERNS = {
    "private_key": re.compile(rb"-{5}BEGIN (?:[A-Z0-9 ]+ )?PRIVATE KEY-{5}|PuTTY-User-Key-File-[23]:"),
    "provider_token": re.compile(rb"(?<![A-Za-z0-9])(?:gh[pousr]_[A-Za-z0-9]{25,}|github_pat_[A-Za-z0-9_]{40,}|glpat-[A-Za-z0-9_-]{20,}|xox[baprs]-[A-Za-z0-9-]{15,}|sk-(?:proj-|live_|test_)?[A-Za-z0-9_-]{22,}|(?:AKIA|ASIA)[A-Z0-9]{16}|AIza[A-Za-z0-9_-]{35}|npm_[A-Za-z0-9]{32,}|pypi-[A-Za-z0-9_-]{36,})"),
    "long_credential_assignment": re.compile(rb"""(?im)\b(?:api[_-]?key|access[_-]?token|auth[_-]?token|password|client[_-]?secret)\b\s*["']?\s*[:=]\s*["']?([A-Za-z0-9+/=_-]{18,})"""),
    "authorization_header": re.compile(rb"(?i)\bauthorization\s*:\s*(?:basic|bearer)\s+[a-z0-9_./+=-]{14,}"),
    "credential_in_url": re.compile(rb"(?i)\b(?:https?|ssh)://[^/?\s:'\"]+:[^/?\s@'\"]+@"),
    "chat_transcript_structure": re.compile(rb"""(?im)^\s*\{\s*["'](?:role|author)["']\s*:\s*["'](?:user|assistant)["']\s*,\s*["'](?:content|text)["']\s*:"""),
}
SENSITIVE_NAME = re.compile(r"(?:^|/)(?:\.env(?:\..*)?|id_(?:rsa|ed25519|ecdsa|dsa)(?:\.pub)?|\.netrc|\.npmrc|credentials(?:\.[^/]*)?|secrets?\.(?:json|yml|yaml)|[^/]+\.(?:pem|pfx|p12|key)|(?:chat|conversation|transcript)[-_]?(?:log|export|history)?\.(?:jsonl?|txt|md|log))$", re.I)


def name_hits(path, mode):
    hits = Counter()
    if SENSITIVE_NAME.search(path):
        hits["credential_or_transcript_filename"] += 1
    parts = PurePosixPath(path)
    if parts.is_absolute() or ".." in parts.parts:
        hits["outside_tree_path"] += 1
    if mode == "120000":
        hits["symlink_to_review"] += 1
    if mode == "160000":
        hits["external_gitlink"] += 1
    hits.update(count_tokens(os.fsencode(path)))
    return hits


def tree_listing(root, commit):
    result = []
    for rec in git(root, "ls-tree", "-rz", commit).split(b"\0"):
        if rec:
            header, name = rec.split(b"\t", 1)
            mode, _, oid = header.split()
            result.append((mode.decode(), os.fsdecode(name), oid.decode()))
    return result


def scan_tree_entries(data, hash_bytes):
    """Scan each stored entry, including trees outside any commit."""
    cursor = 0
    findings = Counter()
    while cursor < len(data):
        split = data.index(b" ", cursor)
        end = data.index(b"\0", split + 1)
        mode = data[cursor:split].decode("ascii")
        findings.update(name_hits(os.fsdecode(data[split + 1:end]), mode))
        cursor = end + 1 + hash_bytes
    if cursor != len(data):
        raise ValueError("Truncated Git tree")
    return findings


def reachable_objects(root, *rev):
    output = git(root, "rev-list", "--objects", "--no-object-names", *rev)
    return set(output.decode("ascii").split())


def classify_reflog(root):
    fields = "%gD%x00%gn%x00%ge%x00%gs"
    records = git(root, "reflog", "show", "--all", "--format=" + fields).splitlines()
    totals, remote_updates = Counter(), Counter()
    for line in records:
        ref, _, email, subject = line.split(b"\0", 3)
        totals.update(count_tokens(line))
        if ref.startswith(b"refs/remotes/") and subject == b"update by push":
            remote_updates.update(count_tokens(email))
    return {"occurrence_counts": dict(totals), "remote_tracking_push_actor_subset": dict(remote_updates)}


def object_scan(root):
    catalog = git(root, "cat-file", "--batch-all-objects", "--batch-check=%(objectname) %(objecttype)").splitlines()
    objects = dict(x.decode().split() for x in catalog)
    proc = subprocess.Popen(["git","-C",str(root),"cat-file","--batch"], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    findings = {}
    all_tree_names = Counter()
    tree_findings = {}
    try:
        for oid, kind in objects.items():
            proc.stdin.write(oid.encode() + b"\n")
            proc.stdin.flush()
            fields = proc.stdout.readline().split()
            data = proc.stdout.read(int(fields[2]))
            if proc.stdout.read(1) != b"\n":
                raise ValueError("Malformed cat-file output")
            if kind == "tree":
                entry_hits = scan_tree_entries(data, len(oid) // 2)
                if entry_hits:
                    tree_findings[oid] = entry_hits
                    all_tree_names.update(entry_hits)
                continue
            hits = count_tokens(data)
            if hits:
                findings[oid] = hits
    finally:
        proc.stdin.close()
        proc.stdout.close()
        if proc.wait():
            raise RuntimeError("Git object inspection failed")
    all_commits = [oid for oid, kind in objects.items() if kind == "commit"]
    head_set = reachable_objects(root, "HEAD")
    ref_set = reachable_objects(root, "--all")
    git_group = {
        "reachable_from_HEAD": head_set,
        "reachable_from_other_refs_only": ref_set - head_set,
        "stored_outside_current_refs": set(objects) - ref_set,
    }
    partitions = {}
    for name, identifiers in git_group.items():
        grouped = {"blobs": Counter(), "commit_tag_metadata": Counter(), "tree_entry_names": Counter()}
        for oid in identifiers:
            if oid in tree_findings:
                grouped["tree_entry_names"].update(tree_findings[oid])
            if oid in findings:
                category = "blobs" if objects[oid] == "blob" else "commit_tag_metadata"
                grouped[category].update(findings[oid])
        partitions[name] = {
            "object_counts": dict(Counter(objects[oid] for oid in identifiers)),
            "occurrence_counts": {key: dict(value) for key,value in grouped.items()},
        }
    histories = []
    blob_sums, metadata = Counter(), Counter()
    tree_names = Counter()
    for oid, hits in findings.items():
        (blob_sums if objects[oid] == "blob" else metadata).update(hits)
    for commit in sorted(all_commits):
        entries = tree_listing(root, commit)
        by_path = Counter()
        flagged = 0
        for mode, path, oid in entries:
            flags = name_hits(path, mode)
            tree_names.update(flags)
            flags.update(findings.get(oid, {}))
            by_path.update(flags)
            flagged += bool(flags.keys() - PUBLIC_EMAIL_CATEGORIES)
        histories.append(dict(commit=commit,reachable_from_ref=commit in ref_set,reachable_from_HEAD=commit in head_set,paths=len(entries),
                              flagged_paths=flagged,path_occurrence_counts=dict(by_path),
                              commit_metadata_counts=dict(findings.get(commit, {}))))
    refs = git(root,"for-each-ref","--format=%(refname)").splitlines()
    return {"object_counts":dict(Counter(objects.values())),"all_stored_commits":histories,
            "object_partitions":partitions,
            "unique_blob_occurrences":dict(blob_sums),"unique_tag_and_commit_metadata_occurrences":dict(metadata),
            "all_stored_tree_entry_occurrences":dict(all_tree_names),
            "tree_path_occurrences_across_commits":dict(tree_names),
            "local_reflog_metadata":classify_reflog(root),
            "ref_name_occurrences":dict(count_tokens(b"\n".join(refs)))}


def paths_from_git(root, *args):
    return {os.fsdecode(x) for x in git(root,"ls-files","-z",*args).split(b"\0") if x}


def work_scan(root):
    tracked = paths_from_git(root)
    ignored = paths_from_git(root,"--others","--ignored","--exclude-standard")
    files = {"tracked":Counter(), "untracked":Counter(), "ignored":Counter()}
    counts = Counter()
    for folder, dirs, names in os.walk(root,followlinks=False):
        dirs[:] = [d for d in dirs if d != ".git"]
        linked_dirs = [d for d in dirs if (Path(folder)/d).is_symlink()]
        dirs[:] = [d for d in dirs if d not in linked_dirs]
        for part in names + linked_dirs:
            f = Path(folder) / part
            rel = f.relative_to(root).as_posix()
            kind = "tracked" if rel in tracked else "ignored" if rel in ignored else "untracked"
            counts[kind] += 1
            symlink = f.is_symlink()
            flags = name_hits(rel, "120000" if symlink else "")
            if symlink or f.is_file():
                content = os.fsencode(os.readlink(f)) if symlink else f.read_bytes()
                flags.update(count_tokens(content))
            else:
                flags["special_file_to_review"] += 1
            files[kind].update(flags)
    return {"file_counts":dict(counts),"occurrence_counts":{k:dict(v) for k,v in files.items()}}


def main():
    argv = argparse.ArgumentParser(description=__doc__)
    argv.add_argument("--root",type=Path,default=Path(__file__).resolve().parents[1])
    argv.add_argument("--output",type=Path)
    argv.add_argument("--phase",choices=("live","pre-final-commit"), default="live")
    args=argv.parse_args()
    root=args.root.resolve()
    report={"capture":{"at_utc":datetime.now(timezone.utc).isoformat(timespec="seconds"), "phase":args.phase,
                       "scope":"This tracked preparation record measures the worktree, object store and local reflogs at the time shown. The final commit and restored bundle are inspected afterward. Their results belong in the enclosing project's out/LOG.md and are not observations in this snapshot." if args.phase=="pre-final-commit" else "A live scan of the checkout in which the command ran."},
            "method":"Local Git object database, every stored tree entry, commit snapshot, ref name and local reflog, and actual working tree including ignored files. Match values are withheld. No credential store or remote is read.",
            "scope":"Counts per commit expand paths. Unique-blob totals count shared objects once. HEAD history, other refs only, and objects outside the current refs are disjoint sets. Remote-tracking push actors are a subset of the local reflog counts. Reflogs and unreferenced objects are local and their counts can differ in a fresh clone or restoration. Reader notes and page-image origins are independently recorded in NOTICE.md.",
            "categories_checked":list(TOKEN_PATTERNS)+sorted(PUBLIC_EMAIL_CATEGORIES)+["email_candidate","reserved_machine_email","review_service_home","personal_or_unclassified_home","credential_or_transcript_filename","outside_tree_path","external_gitlink","symlink_to_review","special_file_to_review"],
            "public_contacts":"Three exact, case-sensitive addresses are reported separately: the owner's GitHub no-reply identity and the academic and company contact addresses supplied for publication.",
            "limitations":"Pattern detection covers recognizable secret formats and transcript markers. Linked files and gitlinks are reported without dereferencing them. No Git history is rewritten.",
            "round3_disposition":{
                "previous_commits":"The two original DB1/DB2 trees contain 24 and 48 occurrences of absolute paths for shared review-service accounts. The owner authorized rewriting Git identities with those first two tree snapshots preserved. These machine paths therefore persist wherever those snapshots are included. The owner decides public visibility.",
                "authorized_identity":"The owner authorized one exact GitHub no-reply identity for attribution, authorship and committer fields. The scanner counts its exact spelling separately. Other ordinary-format addresses remain candidates, with values withheld.",
                "current_documents":"Fourteen review or archival source copies replace review-machine home prefixes with an environment placeholder. Original report hashes remain historical source references. The static copies are regenerated from the sanitized files.",
                "scope_of_ignored_files":"Ignored Python bytecode is local-only. Before final compilation cleanup, eight machine-path strings occurred there. No prior commit contains those bytecode files.",
                "binary_origin":"The notes/ edition index and NOTICE account for indigenous image/TeX sources. The scanner reads binary bytes for ASCII secret signatures; no OCR claim is made."},
            "git":object_scan(root),"working_tree":work_scan(root)}
    text=json.dumps(report,indent=2,sort_keys=True)+"\n"
    if args.output:
        args.output.write_text(text)
    else:
        print(text,end="")


if __name__=="__main__":
    main()
