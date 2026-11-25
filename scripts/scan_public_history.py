#!/usr/bin/env python3
"""Audit only the trees, paths and commit metadata that publishing one ref would send."""
from collections import Counter
import argparse
import json
import platform
from pathlib import Path
import re
import subprocess

from scan_privacy import PUBLIC_EMAIL_CATEGORIES, count_tokens, git, name_hits, tree_listing, TOKEN_PATTERNS

LOCAL_PATH = re.compile(rb"[/](?:Users|home|sessions|mnt|tmp|private/(?:tmp|var)|var/folders|Volumes|workspace|root)[/]", re.I)
HOST = re.compile(rb"(?i)(?<![a-z0-9_.-])(?:[a-z0-9-]+[.](?:lan|internal|home[.]arpa)(?![.a-z0-9_-])|[a-z0-9-]*(?:macbook|imac|workstation|desktop-)[a-z0-9-]+(?:[.]local)?|ip-\d+-\d+-\d+-\d+|[a-z0-9-]+[.]local(?=[:/\s]|$)(?<![.]lean))")
PRIVATE_IP = re.compile(rb"(?<![\w.])(?:10[.]\d{1,3}|192[.]168|172[.](?:1[6-9]|2\d|3[01]))[.]\d{1,3}[.]\d{1,3}(?![\w.])")
LOCAL_HOST = platform.node().split(".")[0].encode().lower()
PROMPT = re.compile(rb"(?im)^\s*(?:\[(?:user|assistant)\]|(?:user|assistant)\s*:|<\|(?:im_start|im_end)\|>)")
# Dot-local is also used as a namespace in Lean. A reviewer must resolve
# bare candidates; a qualified Lean name with further components isn't a hostname.
OWNER = b"Gunhee Cho <GunheeC" + b"@users.noreply.github.com>"

def matches(raw):
    hits = count_tokens(raw)
    for key, pattern in [('absolute_local_path', LOCAL_PATH), ('host_candidate', HOST), ('private_network_address', PRIVATE_IP), ('transcript_marker', PROMPT)]:
        hits[key] += len(pattern.findall(raw))
    if len(LOCAL_HOST) >= 5 and LOCAL_HOST != b"localhost":
        hits["local_host_identity"] += len(re.findall(rb"(?<![\w-])" + re.escape(LOCAL_HOST) + rb"(?![\w-])", raw, re.I))
    return +hits

def scan(root, ref):
    commits = git(root, "rev-list", "--reverse", ref).decode().splitlines()
    blobs = {}
    rows = []
    candidates = {}
    with subprocess.Popen(["git", "-C", str(root), "cat-file", "--batch"],
                          stdin=subprocess.PIPE, stdout=subprocess.PIPE) as proc:
        for commit in commits:
            raw = git(root, "cat-file", "commit", commit)
            meta = matches(raw)
            for role in (b"author", b"committer"):
                ident = next(line for line in raw.splitlines() if line.startswith(role + b" "))
                if ident.split(b" ", 1)[1].rsplit(b" ", 2)[0] != OWNER:
                    meta["unexpected_git_identity"] += 1
            files = tree_listing(root, commit)
            totals = Counter()
            for mode, name, oid in files:
                if oid not in blobs:
                    proc.stdin.write(oid.encode() + b"\n")
                    proc.stdin.flush()
                    _, typ, size = proc.stdout.readline().split()
                    if typ != b'blob':
                        raise ValueError(f'Non-blob tree leaf: {name}')
                    data = proc.stdout.read(int(size))
                    if proc.stdout.read(1) != b"\n":
                        raise ValueError("Invalid batch framing")
                    blobs[oid] = matches(data)
                path_hits = name_hits(name, mode)
                path_hits.update(matches(name.encode()) - count_tokens(name.encode()))
                flags = blobs[oid] + path_hits
                totals.update(flags)
                unsafe = {k:v for k,v in flags.items() if k not in PUBLIC_EMAIL_CATEGORIES}
                if unsafe:
                    candidates[name] = unsafe
            rows.append(dict(commit=commit, paths=len(files), occurrences=totals, metadata=meta))
        proc.stdin.close()
    categories = [*TOKEN_PATTERNS, *sorted(PUBLIC_EMAIL_CATEGORIES), 'personal_or_unclassified_home', 'review_service_home',
                  'email_candidate','reserved_machine_email','absolute_local_path','host_candidate',
                  'transcript_marker','private_network_address','local_host_identity','unexpected_git_identity','credential_or_transcript_filename',
                  'outside_tree_path','symlink_to_review','external_gitlink']
    return dict(ref=ref, unique_blobs=len(blobs), categories=categories, commits=rows, flagged_files=candidates)

if __name__ == "__main__":
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('ref', nargs='?', default='main')
    ap.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    args=ap.parse_args()
    record=scan(args.root, args.ref)
    print(json.dumps(record, indent=2))
    raise SystemExit(bool(record['flagged_files']) or any(set(c['metadata']) - PUBLIC_EMAIL_CATEGORIES for c in record['commits']))
