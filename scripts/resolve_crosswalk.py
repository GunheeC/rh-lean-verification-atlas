#!/usr/bin/env python3
"""Resolve named Lean declarations against reading units. Optional verified raw-graph path rebuild."""
from atlas_files import unit_files
import argparse
from array import array
from collections import defaultdict, deque
import hashlib
import json
from pathlib import Path
import pickle

BANNER = 'AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved'


def load(file):
    return json.loads(file.read_text())


def make_paths(cache, pins, units, requested):
    with cache.open('rb') as stream:
        digest = hashlib.file_digest(stream, 'sha256').hexdigest()
    if digest != pins['graph_sha256']:
        raise ValueError('The raw dependency graph differs from the atlas pin.')
    with cache.open('rb') as stream:
        names, info, starts, targets = pickle.load(stream)
    index = {n:i for i,n in enumerate(names)}
    parent = array('i', [-1]) * len(names)
    owners = {}
    search = deque()
    for uid, unit in sorted(units.items()):
        for anchor in unit['lean']:
            v = index.get(anchor['name'])
            if v is None or anchor.get('role','statement') != 'statement' or v in owners:
                continue
            owners[v] = uid
            parent[v] = v
            search.append(v)
    remaining = {index[n] for n in requested if n in index}
    paths = {}
    while search and remaining:
        v = search.popleft()
        if v in remaining:
            path = [names[v]]
            r = v
            while r not in owners:
                r = parent[r]
                path.append(names[r])
            paths[names[v]] = {'unit_id':owners[r], 'path':list(reversed(path))}
            remaining.remove(v)
        if info[v][2] == 'lit':
            continue
        for w in targets[starts[v]:starts[v+1]]:
            if parent[w] == -1:
                parent[w] = v
                search.append(w)
    return paths


def resolve(root, cache):
    book = root / 'crosswalk/adriazola.json'
    doc = load(book)
    units = {p.stem:load(p) for p in sorted(unit_files(root))}
    graph = load(root/'data/graph.json')
    pins = load(root/'data/pins.json')
    byname = defaultdict(list)
    for n in graph['nodes']:
        kind = 'unit_statement' if n['id'] == n['unit_id'] else 'graph_member'
        byname[n['name']].append((n['unit_id'], n['id'], kind))
    for uid,unit in units.items():
        for d in unit['lean']:
            if d.get('role') == 'component' or any(entry[0]==uid for entry in byname[d['name']]):
                continue
            kind = 'unit_statement' if d.get('role','statement') == 'statement' else 'chart_supplier'
            byname[d['name']].append((uid, None, kind))
    requested = {d['name'] for row in doc['mappings'] for d in row['lean_declarations']}
    if cache:
        doc['dependency_routes'] = make_paths(cache, pins, units, requested)
        doc['dependency_graph_sha256'] = pins['graph_sha256']
    routes = doc.get('dependency_routes', {})
    for row in doc['mappings']:
        direct=[]
        for d in row['lean_declarations']:
            name = d['name']
            d['role'] = 'corresponding_proposition' if name in row.get('matched_propositions',[]) else 'related_declaration'
            if name in pins['anchors']:
                pin = pins['anchors'][name]
                if (pin['file'],pin['line0'],pin['line1']) != (d['file'],d['line_start'],d['line_end']):
                    raise ValueError('Source span mismatch for '+name)
                d['sha256'] = pin['sha256']
            for uid,node,kind in byname.get(name,[]):
                direct.append({'unit_id':uid,'node_id':node,'lean_declaration':name,'match_kind':kind})
        row['matches'] = direct
        row['unit_ids'] = sorted({m['unit_id'] for m in direct})
        row['reading_routes'] = {d['name']:routes[d['name']]['unit_id'] for d in row['lean_declarations']
                                 if d['name'] in routes and len(routes[d['name']]['path'])>1}
        unknown = (set(row['contextual_unit_ids']) | set(row['unit_ids']))-set(units)
        if unknown:
            raise ValueError(f"Unknown unit IDs in {row['id']}: {unknown}")
    book.write_text(json.dumps(doc,ensure_ascii=False,indent=2)+'\n')
    return doc


def render_text(doc):
    rows = doc['mappings']
    out = ['# Adriazola’s reconstruction', '', doc['notice'], '', BANNER, '',
           'This table relates numbered passages in the 287-page manuscript dated 24 November 2026 to Lean declarations and atlas units. The two source editions are pinned in the [register](../sources/registry.json).', '',
           '“Exact” denotes a correspondence with the identified proposition at its stated hypotheses. “Partial” denotes a related statement or declaration. “None” means the table identifies no statement-level counterpart. A contextual unit or a related declaration is a reading pointer. The table supplies no review or grade for an atlas unit.', '']
    unitlink = lambda uid: f'[{uid}](../units/{uid}.md)'
    for heading, kind in [('Numbered hypotheses', 'numbered_hypothesis'), ('Other numbered passages', 'comparison')]:
        out += ['## '+heading, '', '| Manuscript item | Match | Lean declaration | Atlas unit |', '|---|---|---|---|']
        for row in rows:
            if row['kind'] != kind:
                continue
            refs = row['lean_declarations']
            pins = ', '.join('`'+r['name']+'`' for r in refs) or '—'
            links = [unitlink(uid) for uid in row['unit_ids']]
            seen = set(row['unit_ids'])
            for label, uids in (('dependency', row['reading_routes'].values()), ('context', row['contextual_unit_ids'])):
                extra = sorted(set(uids) - seen)
                if extra:
                    links.append(label+' '+', '.join(map(unitlink,extra)))
                    seen.update(extra)
            page = ', p. '+str(row['page']) if row.get('page') else ''
            out.append(f"| {row['external_id']}{page} | {row['relation']} | {pins} | {' · '.join(links) or '—'} |")
        out.append('')
    out += ['', '[Full correspondence table, source spans and navigation paths](adriazola.json).']
    return '\n'.join(out)+'\n'


def render(root, doc):
    (root/'crosswalk/adriazola.md').write_text(render_text(doc), encoding='utf8')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--graph-cache', type=Path, help='trusted graph cache from the project archive; SHA-256 must agree')
    options = parser.parse_args()
    render(options.root, resolve(options.root, options.graph_cache))
