"""Cross-check the revised reader editions and the three release attachments offline."""
from hashlib import sha256
import json
from pathlib import Path
import re


def check(root, units, asset_dir=None):
    def read(name):
        return json.loads((root / name).read_bytes())

    errors = []
    catalog = read('data/editions.json')['editions']
    paper = catalog['paper2_v5']
    release = read('data/round5_release.json')
    current_pillars = read('data/round6_review_corrections.json')['pillar_editions']
    for path, edition in current_pillars.items():
        note = root / path
        if not note.is_file() or sha256(note.read_bytes()).hexdigest() != edition['sha256']:
            errors.append(f'{path}: revised pillar edition differs')
        lower, upper = (1, 1) if path.startswith('docs/ko/') else (6, 12)
        if not lower <= edition['pages'] <= upper:
            errors.append(f'{path}: revised pillar print length differs')
    expected_pillars = {prefix + name + '.md' for prefix in ('pillars/', 'docs/ko/pillars/') for name in ('V', 'F')}
    if set(current_pillars) != expected_pillars or set(release['pillar_editions']) != expected_pillars:
        errors.append('Incomplete revised pillar inventory')
    original_rows = read('data/round3_v4.json')['list_a']
    expected = {r['row']: r['unit_id'] for r in original_rows}
    if {row['row']: row['unit'] for row in paper['list_a']} != expected or len(paper['list_a']) != 10:
        errors.append('The v5 list-A assignments differ from the ten pinned statements')
    required = set(expected.values()) | {'V4-COND'}
    pages = paper['pages']
    for uid in required:
        locators = paper['unit_locators'].get(uid, [])
        unit_rows = [e for e in units[uid]['expositions'] if e['document'] == 'paper2_v5']
        actual = [(e['section'], e['pages']) for e in unit_rows]
        if (not locators or actual != [(e['section'], e['pages']) for e in locators]
                or any(e.get('review_status') != 'pending_review' for e in unit_rows)):
            errors.append(f'{uid}: missing, stale or promoted v5 exposition')
    for uid, locators in paper['unit_locators'].items():
        for loc in locators:
            start, end = loc['pages']
            if uid not in units or not 1 <= start <= end <= pages:
                errors.append(f'{uid}: invalid v5 page extent')
    if paper['review_status'] != 'pending_review' or paper['lean_commit'] != read('data/pins.json')['source_commit']:
        errors.append('Incorrect v5 review status or Lean source')
    assets = release['attachments']
    expected_assets = {'paper_v5.pdf': 'paper2_v5', 'blueprint_v13.pdf': 'blueprint_v13',
                       'blueprint_v13_cover.pdf': 'blueprint_v13_cover'}
    if set(assets) != set(expected_assets):
        errors.append('Release attachment inventory differs')
    for filename, key in expected_assets.items():
        edition = catalog[key]
        digest = edition['sha256']
        if assets.get(filename) != digest or not re.fullmatch('[0-9a-f]{64}', digest):
            errors.append(f'{filename}: checksum missing or inconsistent')
        if asset_dir is not None:
            p = asset_dir / filename
            if not p.is_file() or sha256(p.read_bytes()).hexdigest() != digest:
                errors.append(f'{filename}: release attachment bytes differ')
    return errors


if __name__ == '__main__':
    import argparse
    from atlas_files import unit_files
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--assets', type=Path)
    args = ap.parse_args()
    root = Path(__file__).resolve().parents[1]
    units = {p.stem: json.loads(p.read_bytes()) for p in unit_files(root)}
    problems = check(root, units, args.assets)
    for problem in problems:
        print(problem)
    raise SystemExit(bool(problems))
