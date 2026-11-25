"""Check the live reader edition against the round-4 source and coverage ledger."""
from collections import Counter
import hashlib
import json
from pathlib import Path
import re


def check(root, units, lean_src=None):
    ledger = json.loads((root / 'data/round4_changes.json').read_bytes())
    changes = {r['id']: r for r in ledger['changes']}
    errors = []
    if len(changes) != len(ledger['changes']):
        errors.append('Duplicated round-4 change')
    grades = json.loads((root / 'data/round2_reading_inputs.json').read_bytes())['units']
    for uid, u in units.items():
        if uid in grades and u.get('grade_before_human_check', u['grade']) != grades[uid]['baseline']['grade'] and uid not in ledger['review_grade_changes']:
            errors.append(f'{uid}: grade change without an independent review')
        if u['status'] != 'Statement only':
            summary = u.get('summary', '')
            if not 1 <= len(summary.split()) <= 90 or '\n' in summary:
                errors.append(f'{uid}: missing or overlong plain-language paragraph')
        if u['status'] == 'Statement only' and uid not in ledger['statement_only_remaining']:
            errors.append(f'{uid}: absent from the remaining work list')
    remaining = sorted(uid for uid,u in units.items() if u['status'] == 'Statement only')
    if remaining != sorted(ledger['statement_only_remaining']) or len(remaining) > 60:
        errors.append('Remaining statement-only inventory or target differs')
    if dict(Counter(u['status'] for u in units.values())) != ledger['status_counts']:
        errors.append('Current written coverage differs from dashboard ledger')
    def edition(doc):
        file = root/doc['path']
        if (not file.resolve().is_relative_to(root.resolve()) or not file.is_file()
                or hashlib.sha256(file.read_bytes()).hexdigest() != doc['sha256']):
            errors.append(f"Changed or missing written edition: {doc['path']}")
    revisions = json.loads((root/'data/round6_review_corrections.json').read_bytes())['note_editions']
    for uid,r in changes.items():
        u = units[uid]
        if u['status'] != r['status'] or not r['first_step_to_challenge'] or not r['lean_ranges']:
            errors.append(f'{uid}: incomplete change record')
        doc = r['note']
        current = revisions.get(doc['path'], doc)
        edition(current)
        if current is not doc and current["previous_sha256"] != doc["sha256"]:
            errors.append(f'{uid}: incorrect earlier edition digest')
        if not any(e['document']==doc['path'] and e['pages']==[1,current['pages']] for e in u['expositions']):
            errors.append(f'{uid}: unregistered exposition or page extent')
        lower, upper = (1, 12) if r['old_status'] == 'Full' else (2, 4)
        if not lower <= doc['pages'] <= upper or u.get('review_status') != 'pending_review':
            errors.append(f'{uid}: check print extent or review state')
    for key, p in ledger['pillars'].items():
        if not 6 <= p['edition']['pages'] <= 12 or p['korean_opening']['pages'] != 1:
            errors.append(f'{key}: print length differs from the required extent')
        for row in p['table']:
            uid = row['unit']
            if uid not in units or units[uid]['status'] == 'Statement only':
                errors.append(f'{key}: missing outline for {uid}')
            if row['level'] == 2 and row.get('classification') not in ('a','b','c','unclassified'):
                errors.append(f'{key}: unclassified row needs an explicit disposition')
            if not isinstance(row['dominated'],int) or row['dominated'] < 0 or not row.get('evidence'):
                errors.append(f'{key}: missing graph weight or source evidence')
    cache = {}
    for pin in ledger['citations']:
        f,lo,hi,sha = (pin[k] for k in ('file','line0','line1','sha256'))
        if Path(f).is_absolute() or '..' in Path(f).parts or not (1<=lo<=hi and re.fullmatch('[0-9a-f]{64}',sha)):
            errors.append(f'{f}: invalid round-4 source locator')
            continue
        if lean_src:
            if f not in cache:
                raw = (lean_src/f).read_bytes()
                if hashlib.sha256(raw).hexdigest() != ledger['source_file_sha256'][f]:
                    errors.append(f'{f}: differs from the source archive')
                cache[f] = raw.decode().splitlines()
            if hi > len(cache[f]) or hashlib.sha256('\n'.join(cache[f][lo-1:hi]).encode()).hexdigest()!=sha:
                errors.append(f'{f}: source lines {lo}–{hi} differ')
    return errors
