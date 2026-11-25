#!/usr/bin/env python3
"""Import a human-authored YAML/JSON record or a filled GitHub issue body."""
import argparse
from contextlib import contextmanager
import json
import os
from pathlib import Path
import re
import subprocess
import sys
import tempfile

from signoff_records import ROOT, human_state, load_records, read_manifest, record_prefix, require, validate_one, validate_resolutions
from signoff_yaml import read_yaml

FIELDS = {"Reader name":"name", "Affiliation (optional)":"affiliation", "ORCID (optional)":"orcid",
          "Field":"field", "Reader level":"level", "Unit":"unit", "Edition SHA-256":"edition_sha256",
          "Scope":"scope", "Verdict for each target":"verdict", "What I did":"what_i_did",
          "Time spent in hours":"time_spent_hours", "Reservations":"reservations", "Conflicts of interest":"conflicts_of_interest",
          "AI assistance used":"ai_assistance_used", "AI assistance description":"ai_assistance_description",
          "Date":"date", "Attestation":"attestation"}


def form(text):
    body={}
    for label, value in re.findall(r"^### (.+?)\s*\n(.*?)(?=^### |\Z)",text,re.M|re.S):
        require(label in FIELDS and FIELDS[label] not in body, f"Unknown/repeated issue label {label}")
        value=value.strip()
        if value in {"_No response_", "No response", ""} and FIELDS[label] in {"orcid","affiliation"}:continue
        body[FIELDS[label]]=value
    rd={k:body.pop(k) for k in ("name","affiliation","orcid","field","level") if k in body}
    body["reader"]=rd
    require("scope" in body and "verdict" in body, "The issue needs the scope and verdict fields")
    scope=body["scope"]
    if scope.startswith("steps"):
        m=re.fullmatch(r"steps\s+\[([^\]]+)\]",scope)
        require(m, "Write the scope as steps [S1,S2], whole-note, or statement-vs-lean")
        body["scope"]={"steps":[x.strip() for x in m[1].split(",")]}
    verdicts={}
    resolves={}
    for line in body["verdict"].strip().splitlines():
        m=re.fullmatch(r"\s*(S[1-9]\d*[a-z]*|statement-vs-lean)\s*:\s*([a-z-]+)(?:\s+resolves\s+(.+))?\s*",line)
        require(m and m[1] not in verdicts, "Write one target: verdict per line; optional suffix: resolves RECORD.yaml")
        verdicts[m[1]]=m[2]
        if m[3]:
            resolves[m[1]]=[n.strip() for n in m[3].split(",")]
    body["verdict"]=verdicts
    if resolves:body["resolves"]=resolves
    body["time_spent_hours"]=float(body["time_spent_hours"])
    return body


def submission(text):
    return form(text) if re.search(r"^### Reader name\s*$",text,re.M) else read_yaml(text)


@contextmanager
def records_lock(path):
    # The directory is stable across atomic file installs; no lock file enters the atlas.
    import fcntl
    fd=os.open(path, os.O_RDONLY)
    try:
        fcntl.flock(fd,fcntl.LOCK_EX)
        yield
    finally:os.close(fd)


def import_record(root, record, dry_run=False):
    root=Path(root).resolve()
    manifest=read_manifest(root,record.get("unit"))
    record=dict(record)
    record["step_sha256"]=validate_one(record,manifest)
    directory=root/"signoffs/records"
    require(directory.is_dir(),"Missing records directory")
    with records_lock(directory):
        existing=load_records(root)
        for name, other in existing:
            if other==record:
                return name,False
        prefix=record_prefix(record)
        serial=1+max((int(n[len(prefix):-5]) for n,_ in existing if n.startswith(prefix)),default=0)
        name=f"{prefix}{serial}.yaml"
        validate_one(record,manifest,name)
        combined=existing+[(name,record)]
        resolving_units = {row["unit"] for _, row in combined if row.get("resolves")}
        validate_resolutions(combined, {uid: read_manifest(root, uid) for uid in resolving_units})
        human_state(root,record["unit"],manifest,combined)
        if dry_run:return name,False
        # The refresh runs only at the maintainer's explicit command. An interrupted refresh
        # can be replayed from the already-installed, complete record.
        target=directory/name
        with tempfile.NamedTemporaryFile("w",encoding="utf-8",dir=directory.parent,delete=False) as out:
            scratch=Path(out.name)
            try:
                json.dump(record,out,indent=2,ensure_ascii=False)
                out.write("\n");out.flush();os.fsync(out.fileno())
            except BaseException:
                scratch.unlink(missing_ok=True);raise
        try:os.link(scratch,target)
        finally:scratch.unlink(missing_ok=True)
        return name,True


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("input",help="filled GitHub Markdown, YAML/JSON file, or - for standard input")
    p.add_argument("--root",type=Path,default=ROOT)
    p.add_argument("--dry-run",action="store_true",help="check without storing or regenerating")
    a=p.parse_args()
    try:
        text=sys.stdin.read() if a.input=="-" else Path(a.input).read_text()
        r=submission(text)
        name,added=import_record(a.root,r,a.dry_run)
        print(("Validated" if a.dry_run else "Accepted" if added else "Already recorded"),name,flush=True)
        if not a.dry_run:
            subprocess.run([sys.executable,"scripts/refresh_round4.py"],cwd=a.root.resolve(),check=True)
    except (ValueError,KeyError,TypeError,AttributeError,OSError,subprocess.CalledProcessError) as e:
        p.exit(1,f"Sign-off intake: {e}\n")


if __name__=="__main__":
    main()
