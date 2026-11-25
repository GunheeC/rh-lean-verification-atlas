"""Regenerate public products after an explicitly accepted local submission."""
import json
from pathlib import Path
import subprocess
import sys

from atlas_files import unit_files
from signoff_records import disputes, human_state, load_records

ROOT = Path(__file__).resolve().parents[1]


def main():
    records = load_records(ROOT)
    (ROOT/'questions/disputes.md').write_text(disputes(ROOT, records), encoding='utf-8')
    for p in unit_files(ROOT):
        unit = json.loads(p.read_bytes())
        manifest = p.with_suffix('.steps.yaml')
        if not manifest.is_file():
            continue
        state = human_state(ROOT, unit['id'], json.loads(manifest.read_bytes()), records)
        if state['l4'] and unit['grade'] != 'L4':
            unit['grade_before_human_check'] = unit['grade']
            unit['grade'] = 'L4'
        elif not state['l4'] and unit['grade'] == 'L4':
            unit['grade'] = unit.pop('grade_before_human_check')
        else:
            continue
        p.write_text(json.dumps(unit, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')
    commands = [['signoff_authors.py'], ['build_navigation.py'], ['proof_steps.py'], ['unit_pages.py'], ['dashboard.py'],
                ['front_counts.py'], ['roadmap.py'], ['snapshot.py', '--render'], ['build_site.py']]
    for script, *args in commands:
        subprocess.run([sys.executable, str(ROOT/'scripts'/script), *args], cwd=ROOT, check=True)
    print('If counters changed, run scripts/snapshot.py --append --round "Edition label", then regenerate the local site.')


if __name__ == '__main__':
    main()
