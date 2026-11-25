#!/usr/bin/env python3
"""Bind proof checkpoints to exact note editions and regenerate their public checklists."""
import argparse
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[1]
NOTICE = 'AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved'
KINDS = {'definition-unfolding', 'computation', 'inequality', 'case-split',
         'appeal-to-input', 'literature', 'assembly'}
BASE = 'https://github.com/leanprover-community/riemann-hypothesis/blob/'
STEP_ID = re.compile(r'S[1-9][0-9]*[a-z]*$')


def read(path):
    return json.loads(path.read_text(encoding='utf-8'))


def digest(data):
    return hashlib.sha256(data).hexdigest()


def canonical(obj):
    return json.dumps(obj, ensure_ascii=False, separators=(',', ':'), sort_keys=True).encode()


def note_path(root, rel):
    path = Path(rel)
    if path.is_absolute() or '..' in path.parts or path.parts[:1] != ('notes',):
        raise ValueError(f'invalid edition source {rel}')
    return root / path


def edition(root, names):
    if not names or len(names) != len(set(names)):
        raise ValueError('an edition needs distinct note sources')
    files = [{'path': p, 'sha256': digest(note_path(root, p).read_bytes())} for p in names]
    return files, files[0]['sha256'] if len(files) == 1 else digest(canonical(files))


def passage(text, anchor, end_anchor=None):
    if not anchor or anchor not in text:
        raise ValueError(f'passage anchor missing: {anchor!r}')
    if text.count(anchor) != 1:
        raise ValueError(f'passage anchor ambiguous: {anchor!r}')
    start = text.index(anchor)
    # Bind each step to the complete source paragraph, retaining TeX and equations.
    lo = text.rfind('\n\n', 0, start) + 2 if '\n\n' in text[:start] else 0
    end = start + len(anchor)
    if end_anchor:
        if end_anchor not in text[end:]:
            raise ValueError(f'end of passage missing: {end_anchor!r}')
        end = text.index(end_anchor, end) + len(end_anchor)
    hi = text.find('\n\n', end)
    hi = len(text) if hi < 0 else hi
    return text[lo:hi], [text.count('\n', 0, lo) + 1, text.count('\n', 0, hi) + 1]


def normalize_pin(root, unit, pin):
    if isinstance(pin, int):
        pin = unit['lean'][pin]
    elif isinstance(pin, str):
        pin = read(root/'units'/f'{pin}.yaml')['lean'][0]
    fields = {'name': pin.get('name', pin.get('decl')), 'file': pin['file'],
              'line0': pin.get('line0', pin.get('start')), 'line1': pin.get('line1', pin.get('end'))}
    a, b = fields['line0'], fields['line1']
    p = Path(fields['file'])
    if not fields['name'] or p.is_absolute() or '..' in p.parts or p.suffix != '.lean' or not isinstance(a, int) or not isinstance(b, int) or not 1 <= a <= b:
        raise ValueError(f'invalid named Lean interval {fields}')
    return fields


def build(root, uid, sources, rows):
    unit = read(root/'units'/f'{uid}.yaml')
    files, note_hash = edition(root, sources)
    texts = {s: note_path(root, s).read_text(encoding='utf-8') for s in sources}
    active = set()
    ids = set()
    steps = []
    for row in rows:
        key = row['id']
        if not STEP_ID.fullmatch(key) or key in ids:
            raise ValueError(f'{uid}: invalid or duplicate step {key}')
        ids.add(key)
        if row.get('status') == 'withdrawn':
            steps.append(dict(row))
            continue
        try:
            source = row.get('source', sources[0])
            anchor = row['anchor']
            excerpt, lines = passage(texts[source], anchor, row.get('end_anchor'))
            claim = row['claim'].strip()
            kind, uses = row['kind'], row['uses']
            if len(claim.split()) < 4 or kind not in KINDS or not isinstance(uses, list):
                raise ValueError('invalid claim, kind, or uses')
            for ref in uses:
                if STEP_ID.fullmatch(ref):
                    if ref not in active:
                        raise ValueError(f'unavailable prior step {ref}')
                elif not (ref.startswith(('standard: ', 'input: ')) or
                          re.fullmatch(r'[A-Za-z0-9.\-]+', ref) and (root/'units'/f'{ref}.yaml').is_file()):
                    raise ValueError(f'unknown input {ref!r}')
            lean = [normalize_pin(root, unit, p) for p in row['lean']]
            if not lean:
                raise ValueError('each step needs a pinned declaration')
            step = {'id':key,'status':'active','claim':claim,'kind':kind,'uses':uses,
                    'lean':lean,'source':source,'anchor':anchor}
            if row.get('end_anchor'):
                step['end_anchor'] = row['end_anchor']
            step['source_lines'] = lines
            step['claim_sha256'] = digest(claim.encode('utf-8'))
            step['passage_sha256'] = digest(excerpt.encode())
            step['sha256'] = digest(canonical({s:step[s] for s in ('claim','kind','uses','lean','source','passage_sha256')}))
            step['ai_review'] = row.get('ai_review', [])
            active.add(key)
            steps.append(step)
        except (ValueError, KeyError, IndexError) as exc:
            raise ValueError(f'{uid}/{key}: {exc}') from exc
    if not active:
        raise ValueError(f'{uid}: no active checkpoints')
    statement_hash = digest(canonical({'statement': unit['statement'], 'lean': [
        normalize_pin(root,unit,p) for p in unit['lean']]}))
    ed = digest(canonical({'unit':uid, 'sources':files, 'statement_sha256':statement_hash,
                           'steps':[(s['id'],s['sha256']) for s in steps if s['status']=='active']}))
    for step in steps:
        if step['status'] != 'active':
            continue
        for review in step['ai_review']:
            if (review['step_sha256'] != step['sha256'] or review['edition_sha256'] != ed
                    or not review.get('verdict') or not review.get('scope')):
                raise ValueError(f'{uid}: AI evidence must identify this step and edition')
            path = Path(review['file'])
            if path.is_absolute() or '..' in path.parts or not (root/path).is_file():
                raise ValueError('AI review file missing')
            bounds = review['lines']
            if len(bounds)!=2 or not 1 <= bounds[0] <= bounds[1] <= len((root/path).read_text().splitlines()):
                raise ValueError(f'{uid}: invalid AI evidence lines')
    return {'notice':NOTICE,'unit':uid,'edition_sha256':ed,'note_sha256':note_hash,
            'statement_sha256':statement_hash,'sources':files,'steps':steps}


def revise(root, uid, spec):
    path = root/'units'/f'{uid}.steps.yaml'
    old = read(path) if path.exists() else {}
    new = build(root, uid, spec['sources'], spec['steps'])
    by_id = {s['id']:s for s in new['steps']}
    old_ids = {s['sha256']:s['id'] for s in old.get('steps',[]) if s['status']=='active'}
    for s in new['steps']:
        if s['sha256'] in old_ids and s['id'] != old_ids[s['sha256']]:
            raise ValueError(f'{uid}: an unchanged claim cannot be renumbered')
    for row in old.get('steps', []):
        if row['id'] not in by_id:
            new['steps'].append(dict(row, status='withdrawn'))
        elif row.get('status') == 'withdrawn' and by_id[row['id']]['status'] != 'withdrawn':
            raise ValueError(f"{uid}: retired ID {row['id']} cannot be reused")
    new['history'] = list(old.get('history', []))
    if old and old['edition_sha256'] != new['edition_sha256']:
        snapshot = {'edition_sha256':old['edition_sha256'],'sources':old['sources'],
                    'statement_sha256':old['statement_sha256'],
                    'steps':{s['id']:s['sha256'] for s in old['steps'] if s['status']=='active'},
                    'step_texts':{s['id']:s['claim'] for s in old['steps'] if s['status']=='active'},
                    'step_passages':{s['id']:s['passage_sha256'] for s in old['steps'] if s['status']=='active'}}
        if snapshot not in new['history']:
            new['history'].append(snapshot)
    path.write_text(json.dumps(new, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')


def escape(value):
    return str(value).replace('|', r'\|').replace('\n',' ')


def starter_links(root, manifests, check):
    links = {}
    for track, packet in read(root/'data/notes_starters.json')['starters'].items():
        primary = packet['unit_id']
        entries = []
        for m in manifests:
            sources = {source['path'] for source in m['sources']}
            rows = [s['id'] for s in m['steps'] if s['status'] == 'active' and s['source'] == packet['tex']]
            if {packet['path'], packet['tex']} <= sources and rows:
                entries.append((m['unit'], rows[0]))
        if check and not entries:
            raise ValueError(f'{track}: starter edition lacks a bound excerpt and checklist')
        if entries:
            title = 'K-theory' if track == 'ktheory' else track.capitalize()
            links[primary] = ' · '.join(
                f"[{title} starter text and numbered checks]({uid}.check.md#{first})"
                for uid, first in entries)
    return links


def checklist(manifest, human, pin, starter=None):
    from signoff_records import safe_text
    uid = manifest['unit']
    lines = [f'# {uid} · proof checklist','',NOTICE,'',
             f"[Unit and hypotheses]({uid}.md) · [Step manifest]({uid}.steps.yaml)",'',
             f"Sign-off edition SHA-256 `{manifest['edition_sha256']}`. This identifies the exact statement, source files and ordered step text. The whole note SHA-256 is `{manifest['note_sha256']}`. Each check covers the stated claim under its listed inputs.",'', 
             '| Edition source | SHA-256 |','|---|---|']
    for s in manifest['sources']:
        lines.append(f"| [{s['path']}](../{s['path']}) | `{s['sha256']}` |")
    if starter:
        lines.extend(['', starter])
    lines.extend(['','| Step | Claim | Uses | Pinned Lean source | AI step review | Human checks |','|---|---|---|---|---|---|'])
    for row in manifest['steps']:
        k = row['id']
        url = '../'+row['source']
        anchor = f'<a id="{k}"></a>**{k}**'
        if row['status']=='withdrawn':
            anchor+=' · withdrawn'
        claim = f"{escape(row['claim'])} ([source]({url}), lines {row['source_lines'][0]}–{row['source_lines'][1]}, {row['kind']})"
        refs=[]
        for u in row['uses']:
            if STEP_ID.fullmatch(u): refs.append(f'[{u}](#{u})')
            elif u.startswith(('standard: ','input: ')): refs.append(escape(u))
            else: refs.append(f'[{u}]({u}.md)')
        lean=[]
        for p in row['lean']:
            target=BASE+pin+'/src/'+quote(p['file'],safe='/')+f"#L{p['line0']}-L{p['line1']}"
            lean.append(f"[`{escape(p['name'])}` {p['line0']}–{p['line1']}]({target})")
        reviews = []
        for a in row['ai_review']:
            review = f"[{escape(a['verdict'])}, ll. {a['lines'][0]}–{a['lines'][1]}](../{a['file']})"
            if a['scope'] != row['claim']:
                review += ' · ' + escape(a['scope'])
            reviews.append(review)
        ai = ' · '.join(reviews) or 'No step-specific verdict'
        state=human['steps'].get(k,{'state':'withdrawn','checks':[]})
        readers=[state['state']]
        if state.get('independent_pair'): readers.append('checked by at least two independent readers')
        for c in state['checks']:
            record = str(c['record']).split('/')[-1]
            label=f"{safe_text(c['name'])}, {c['date']}, {c['verdict']}"
            label+=f" · declared AI assistance {c['ai_assistance']}"
            if c.get('maintainer'):label+=' (maintainer)'
            if c['status']=='superseded':label+=f" · valid for edition `{c['edition_sha256']}`, superseded"
            readers.append(f"[{label}](../signoffs/records/{record})")
        lines.append(f"| {anchor} | {claim} | {' · '.join(refs) or '—'} | {' · '.join(lean)} | {ai} | {' · '.join(readers)} |")
    lines.extend(['','## Statement comparison and unit decision','',
        f"Statement against Lean · **{human['statement_state']}**. "
        f"Current edition meets L4 · **{'yes' if human['l4'] else 'no'}**. "
        f"All steps and statement checked by at least two independent readers · **{'yes' if human['two_independent'] else 'no'}**."])
    for c in human['statement']:
        record=str(c['record']).split('/')[-1]
        label=f"{safe_text(c['name'])}, {c['date']}, {c['verdict']} · declared AI assistance {c['ai_assistance']}" + (' (maintainer)' if c.get('maintainer') else '')
        if c['status']=='superseded':label+=f" · valid for edition `{c['edition_sha256']}`, superseded"
        lines.extend(['',f"[{label}](../signoffs/records/{record})"])
    if human['whole_note']:
        lines.extend(['','Whole-note submissions · '+' · '.join(f"[{n}](../signoffs/records/{n})" for n in human['whole_note'])])
    lines.extend(['','## How to record your check','',
        'Choose the edition and step IDs you actually read. Report your method, verdict and any reservations. The form accepts partial and negative findings. [Sign-off guide and form](../signoffs/README.md)',''])
    if human['l4']:
        from signoff_records import l4_summary
        lines.extend(['', l4_summary(human['l4_evidence'])])
    return '\n'.join(lines)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--check',action='store_true')
    parser.add_argument('--install',type=Path,help='explicitly install or revise unit→step specifications')
    parser.add_argument('--root',type=Path,default=ROOT)
    opts=parser.parse_args()
    root=opts.root
    if opts.install and opts.check:parser.error('--check cannot install an edition')
    if opts.install:
        for uid,spec in read(opts.install).items():revise(root,uid,spec)
    from signoff_records import human_state, load_records
    records=load_records(root)
    pin=read(root/'data/round3_changes.json')['lean_commit']
    count=0
    manifests = {path:read(path) for path in sorted((root/'units').glob('*.steps.yaml'))}
    starters = starter_links(root, manifests.values(), opts.check)
    for path, m in manifests.items():
        uid=m['unit']
        if path.name!=uid+'.steps.yaml':raise ValueError(f'{path.name}: unit mismatch')
        observed=build(root,uid,[s['path'] for s in m['sources']],m['steps'])
        if any(observed[k]!=m[k] for k in observed):raise ValueError(f'{uid}: step or edition hash mismatch; inspect and revise the edition')
        out=checklist(m,human_state(root,uid,m,records),pin,starters.get(uid))
        target=path.with_name(uid+'.check.md')
        if opts.check:
            if not target.exists() or target.read_text(encoding='utf-8')!=out:
                raise ValueError(f'{uid}: generated checklist out of date')
        else:target.write_text(out, encoding='utf-8')
        count+=len([s for s in m['steps'] if s['status']=='active'])
    if opts.check:
        for path in (root/'units').glob('*.yaml'):
            if not path.name.endswith('.steps.yaml') and read(path)['status'] in ('Full','Outlined') and not path.with_suffix('.steps.yaml').is_file():
                raise ValueError(f'{path.stem}: written unit lacks step manifest')
    print(f'{count} active proof steps')


if __name__=='__main__':
    main()
