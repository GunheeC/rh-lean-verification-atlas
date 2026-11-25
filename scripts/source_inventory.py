#!/usr/bin/env python3
"""Replay the fixed Round 1 raw-source denominator and physical allChi membership."""
import argparse
from collections import defaultdict
from hashlib import file_digest, sha256
from itertools import groupby
import json
from pathlib import Path
import tarfile

ROOT = Path(__file__).resolve().parents[1]
SOURCE = '40e56bab026552e089d7afcfeff08d2defb9c005'
ARCHIVE = '9631b4f020199e580ba86178cb56c6e9b09f690c2369a80dc4334aa93f49c7fc'
GRAPH = 'be8105049e470b3ef224a2b234a0cac6395f8fb1d983c8200416f116ba15abf6'
DB1_PATHS = '9b5802b937fd1df3415791f399100f31757def705e1e2e7976c0adb7d770220d'
DB1_FILE_ROWS = '1fd01df5f6f9a445afa4157922d3989c653c8072c921ca9cf96a6da4f789ad78'


def compact(data):
    return json.dumps(data, sort_keys=True, ensure_ascii=False, separators=(',', ':'))


def fingerprint(data):
    return sha256(compact(data).encode()).hexdigest()


def serialize(data):
    # One file per line for human inspection and stable, compact diffs.
    fields = []
    for key, value in data.items():
        if isinstance(value, dict) and value:
            rows = ['    '+compact(k)+': '+compact(value[k]) for k in sorted(value)]
            body = '{\n'+',\n'.join(rows)+'\n  }'
        else:
            body = compact(value)
        fields.append('  '+compact(key)+': '+body)
    return '{\n'+',\n'.join(fields)+'\n}\n'


def load_inventory(root):
    inventory = json.loads((Path(root)/'progress/source_inventory.json').read_bytes())
    expected = inventory.pop('certificate_sha256')
    if fingerprint(inventory) != expected:
        raise ValueError('Source inventory certificate has changed')
    fixed = {'source_commit': SOURCE, 'archive_sha256': ARCHIVE, 'graph_sha256': GRAPH,
             'historical_path_list_sha256': DB1_PATHS, 'source_files': 175187, 'source_lines': 17374215,
             'source_unterminated': 0, 'archive_regular_files': 175190,
             'weighted_core_lines': 9567045, 'distinct_core_physical_lines': 9567045,
             'file_count': 855, 'raw_lines': 101765}
    if any(inventory.get(k) != v for k, v in fixed.items()):
        raise ValueError('Source inventory differs from the fixed extraction or historical file count')
    if fingerprint(inventory['files']) != DB1_FILE_ROWS:
        raise ValueError('Historical physical-line counts, file paths or hashes differ')
    files, outside = inventory['files'], inventory['outside_files']
    if set(files) & set(outside) or set(inventory['core_ranges']) != set(files) | set(outside):
        raise ValueError('Source inventory must cover all certified files exactly once')
    if set(inventory['core_overlaps']) or not cited_files(root).issubset(set(files)|set(outside)):
        raise ValueError('Invalid core interval multiplicity or uncatalogued active source file')
    for name, runs in inventory['core_ranges'].items():
        entry = (files if name in files else outside)[name]
        lines = entry['lines']
        last = -1
        for a, b in runs:
            if not last+1 < a <= b <= lines:
                raise ValueError(f'Invalid disjoint core runs in {name}')
            last = b
    inventory['certificate_sha256'] = expected
    return inventory


def check_digest(path, expected):
    with path.open('rb') as file:
        if file_digest(file, 'sha256').hexdigest() != expected:
            raise ValueError(f'Unexpected digest: {path.name}')


def cited_files(root):
    return {r['file'] for path in (root/'units').glob('*.steps.yaml')
            for s in json.loads(path.read_bytes())['steps'] if s['status'] == 'active'
            for r in s['lean']}


def source_rows(archive, selected, local_src):
    check_digest(archive, ARCHIVE)
    rows = {}
    census = dict(source_files=0, source_lines=0, source_unterminated=0, archive_regular_files=0)
    with tarfile.open(archive, 'r|gz') as tar:
        for member in tar:
            if not member.isfile():
                continue
            census['archive_regular_files'] += 1
            if not member.name.startswith('lean/src/') or not member.name.endswith('.lean'):
                continue
            name = member.name[len('lean/src/'):]
            raw = tar.extractfile(member).read()
            census['source_files'] += 1
            census['source_lines'] += raw.count(b'\n')
            census['source_unterminated'] += bool(raw) and not raw.endswith(b'\n')
            if name not in selected:
                continue
            if name in rows or not member.isfile():
                raise ValueError(f'Ambiguous source file {name}')
            if local_src and (local_src/name).read_bytes() != raw:
                raise ValueError(f'Source checkout differs from archive at {name}')
            lines = raw.count(b'\n') + int(bool(raw) and not raw.endswith(b'\n'))
            # All existing note citations and the extraction use UTF-8, 1-based inclusive lines.
            if lines != len(raw.decode('utf-8').splitlines()):
                raise ValueError(f'Incompatible Unicode and physical line counts in {name}')
            rows[name] = {'lines': lines, 'sha256': sha256(raw).hexdigest()}
    if set(rows) != selected:
        raise ValueError('Missing pinned source file: '+str(sorted(selected-set(rows))))
    return rows, census


def core_ranges(cache, source):
    # Only the known extraction may be deserialized.
    check_digest(cache, GRAPH)
    import pickle
    with cache.open('rb') as file:
        names, info, starts, edges = pickle.load(file)
    reached = bytearray(len(names))
    start = names.index('allChi')
    reached[start] = 1
    stack = [start]
    events = defaultdict(list)
    weighted_total = 0
    while stack:
        i = stack.pop()
        module, _, kind, a, b, _ = info[i]
        if kind == 'lit':
            continue
        if kind != 'core':
            raise ValueError(f'Unexpected non-library extraction class {kind}')
        if 1 <= a <= b:
            # Signed endpoints encode half-open [a,b+1), grouped by their absolute value below.
            events[module].extend([a, -(b+1)])
            weighted_total += b-a+1
        for j in edges[starts[i]:starts[i+1]]:
            if not reached[j]:
                reached[j] = 1
                stack.append(j)
    if weighted_total != 9567045:
        raise ValueError(f'Unexpected summed declaration weight {weighted_total}')
    physical_total = 0
    routed_weight = 0
    ranges = {name: [] for name in source}
    overlaps = {}
    for module, points in events.items():
        path = module.replace('.', '/')+'.lean'
        previous = 0
        count = 0
        for pos, changes in groupby(sorted(points, key=abs), key=abs):
            if count:
                length = pos-previous
                physical_total += length
                routed_weight += count*length
                if path in source:
                    if pos-1 > source[path]['lines']:
                        raise ValueError(f'Core source interval exceeds archive in {path}')
                    runs = ranges[path]
                    if runs and runs[-1][1]+1 == previous:
                        runs[-1][1] = pos-1
                    else:
                        runs.append([previous, pos-1])
                    if count > 1:
                        extra = overlaps.setdefault(path, [])
                        if extra and extra[-1][1]+1 == previous and extra[-1][2] == count-1:
                            extra[-1][1] = pos-1
                        else:
                            extra.append([previous, pos-1, count-1])
            count += sum(1 if x>0 else -1 for x in changes)
            if count < 0:
                raise ValueError(f'Negative multiplicity at {path}:{pos}')
            previous = pos
        if count:
            raise ValueError(f'Unbalanced endpoints in {path}')
    if routed_weight != weighted_total:
        raise ValueError('Physical intervals do not recover weighted spans')
    return dict(weighted_core_lines=weighted_total, distinct_core_physical_lines=physical_total,
                core_ranges=ranges, core_overlaps=overlaps)


def build(root, archive, cache, local_src=None):
    # The original subset is a pinned path list in this checkout. The archive provides its contents.
    inventory = json.loads((root/'progress/source_inventory.json').read_bytes())
    files = set(inventory['files'])
    paths_sha256 = sha256(('\n'.join(sorted(files))+'\n').encode()).hexdigest()
    if paths_sha256 != DB1_PATHS:
        raise ValueError('Unexpected historical source file set')
    outside = cited_files(root)-files
    source, census = source_rows(archive, files|outside, local_src)
    record = dict(source_commit=SOURCE, archive_sha256=ARCHIVE, graph_sha256=GRAPH,
                historical_path_list_sha256=DB1_PATHS, **census,
                line_rule='Count LF-terminated physical lines and a final unterminated line if present. Include comments and blank lines.',
                core_rule='Follow allChi edges, stopping at literature. Count 1-based inclusive source intervals of reachable core declarations; core_overlaps stores excess declaration multiplicity above one. Core endpoints are shipped for all files in this certificate.',
                file_count=len(files), raw_lines=sum(source[f]['lines'] for f in files),
                files={f: source[f] for f in files}, outside_files={f: source[f] for f in outside},
                **core_ranges(cache,source))
    record['certificate_sha256'] = fingerprint(record)
    return record


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--root', type=Path, default=ROOT)
    ap.add_argument('--source-archive', type=Path, required=True, help='pinned lean.tar.gz')
    ap.add_argument('--graph-cache', type=Path, required=True, help='pinned extraction graph_cache.bin')
    ap.add_argument('--lean-src', type=Path, help='also compare complete bytes with this read-only lean/src directory')
    ap.add_argument('--write', action='store_true')
    args = ap.parse_args()
    data = build(args.root, args.source_archive, args.graph_cache, args.lean_src)
    path = args.root/'progress/source_inventory.json'
    if args.write:
        path.write_text(serialize(data), encoding='utf-8')
    elif json.loads(path.read_bytes()) != data:
        raise SystemExit('Source inventory differs from archive or graph replay')
    load_inventory(args.root)
    print(f"{data['file_count']} original files, {data['raw_lines']:,} physical lines, {len(data['outside_files'])} additional cited files; {data['distinct_core_physical_lines']:,} distinct core source positions across the whole allChi graph.")


if __name__ == '__main__':
    main()
