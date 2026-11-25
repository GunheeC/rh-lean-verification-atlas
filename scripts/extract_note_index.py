"""Index unit expositions and seven source-facsimile reading packets."""
from atlas_files import unit_files
from atlas_labels import TRACK_NAMES
from edition_links import packet_page_links
import argparse
import hashlib
import json
from collections import defaultdict
from pathlib import Path

NOTICE = 'AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved'


def read(path):
    return json.loads(path.read_bytes())


def digest(data):
    return hashlib.sha256(data).hexdigest()


def main(atlas, project):
    metadata = atlas / 'data'
    paper = read(metadata / 'notes_units.json')['units']
    blueprint = read(metadata / 'blueprint_excerpt_index.json')
    editions = read(metadata / 'editions.json')['editions']
    revised = read(metadata / 'round6_review_corrections.json')['note_editions']
    original_notes = {note['path']: note['sha256'] for change in read(metadata / 'round3_changes.json')['changes']
                      for note in change['notes']}
    starters = read(metadata / 'notes_starters.json')['starters']
    anchors = read(metadata / 'pins.json')['anchors']
    units = {}
    by_decl = defaultdict(set)
    for f in sorted(unit_files(atlas)):
        row = read(f)
        uid = row['id']
        if row.get('kind') == 'paper_composite':
            argument = next(e['document'] for e in row['expositions'] if e['document'].endswith('.md'))
            entry = dict(path=argument, origin='Conditional argument from the pinned paper v4; formal references identify components.')
        elif uid in paper:
            original = paper[uid]
            entry = {k: v for k, v in original.items() if k != 'lean_declarations'}
        elif uid not in blueprint:
            argument = next(e["document"] for e in row["expositions"] if e["document"].startswith("notes/") and e["document"].endswith(".md"))
            entry = dict(path=argument)
        else:
            ranges = []
            for r in blueprint[uid]:
                raw = (project / r['source']).read_bytes()
                excerpt = b''.join(raw.splitlines(keepends=True)[r['start']-1:r['end']])
                ranges.append(dict(r, file_sha256=digest(raw), fragment_sha256=digest(excerpt)))
            entry = dict(path=f'notes/blueprint/{uid}.tex', origin='Local blueprint working source, identified by the file hash at each range. V13 page locators apply only to passages labelled in that edition.', source_ranges=ranges)
        essays = [e['document'] for e in row['expositions'] if e['document'].endswith('.md') and e['document'].startswith('notes/')]
        for round_name in ("round3", "round4"):
            paths = [p for p in essays if p.startswith("notes/units/") and
                     (p.endswith("_round4.md") == (round_name == "round4"))]
            if paths:
                entry[round_name + "_readings"] = paths
        entry['file_sha256'] = digest((atlas / entry['path']).read_bytes())
        entry['lean_declarations'] = [pin['name'] for pin in row['lean']]
        for name in entry['lean_declarations']:
            by_decl[name].add(uid)
        entry['starters'] = []
        # Preserve the source fingerprint from before the editorial annotation.
        path = entry['path']
        if path in revised and revised[path].get('previous_sha256'):
            entry['previous_file_sha256'] = original_notes.get(path, revised[path]['previous_sha256'])
            entry['edition_note'] = ('The original excerpt provenance is given in source_ranges. '
                                     'The current file includes a separately marked atlas reading annotation.')
        units[uid] = entry
    if not (set(paper) | set(blueprint)) <= units.keys():
        raise ValueError('Unit file set differs from source exposition set')
    graph_members = {}
    for row in read(metadata / 'graph.json')['nodes']:
        uid = row['unit_id']
        if uid not in units:
            raise ValueError(f"No exposition for graph member {row['id']}")
        by_decl[row['name']].add(uid)
        graph_members[row['id']] = dict(unit_id=uid, lean_decl=row['name'],
                              assignment=row['assignment'], unit_note=units[uid]['path'],
                              statement_pdf_page=row['start_page'])
    for track, packet in starters.items():
        for uid in [packet['unit_id'], *packet['companions']]:
            units[uid]['starters'].append(track)
        name = packet['lean_decl']
        by_decl[name].add(packet['unit_id'])
        packet['lean_pin'] = anchors[name]
        packet['pdf_sha256'] = editions[packet['edition']]['sha256']
    notes = dict(notice=NOTICE, editions=editions, counts=dict(units=len(units),
                    paper=len(paper), blueprint=len(blueprint), paper_composites=sum(read(p).get("kind") == "paper_composite" for p in unit_files(atlas)), pillar_interfaces=sum(uid not in paper and uid not in blueprint and row.get("round4_readings") is not None for uid, row in units.items()), packets=len(starters),
                    printed_page_facsimiles=sum(s['size_pages'] for s in starters.values())),
                 extent='Page totals count printed facsimiles per packet, including shared boundaries. Unit heading pages and TeX line counts do not measure proof or reading length.',
                 units=units, lean_declarations={k: sorted(v) for k,v in sorted(by_decl.items())},
                 paper_graph_members=graph_members,
                 grouping='Each of the 775 paper nodes points to its containing unit. Group assignments locate related reading and do not assert that the unit excerpt includes a separate proof of every member.',
                 starters=starters)
    index = metadata / 'notes.json'
    if not index.exists() or read(index) != notes:
        index.write_text(json.dumps(notes, ensure_ascii=False, indent=2)+'\n')
    lines = [NOTICE, '', '# Reading notes', '',
             'Gunhee Cho is the paper’s author and the blueprint’s editor. Both were drafted with AI assistance. No human, the author included, has yet checked the arguments. Levent Alpöge is the author of the Lean development. The repository includes both PDFs. The edition register preserves the earlier sources used in reviews. [Blueprint v13c](../editions/v0.1.0/blueprint_v13c.pdf) · [Conditional paper v8](../editions/v0.1.0/paper_v8.pdf) · [Edition register](../data/editions.json)', '',
             f'The atlas indexes {len(units)} units, with source excerpts, round-3 mathematical reading notes and seven graduate reading packets. Each packet includes its TeX source and full typeset pages from blueprint v13. Read the target and its premises before assigning the rest of a companion unit.', '',
             '| Track and packet | Unit | Printed pages in blueprint v13c | What to check |',
             '|---|---|---|---|']
    for track, p in starters.items():
        uid = p['unit_id']
        page_links = packet_page_links(editions['blueprint_v13c'], p)
        lines.append(f"| [{TRACK_NAMES[track]}]({track}/README.md) | [{uid}](../units/{uid}.md) | {page_links} | {p['checkable_target']} |")
    lines.extend(['', 'The 47 facsimiles include the printed boundary pages of each assignment. The marked TeX ranges delimit material when a boundary page is shared. Each packet records the entry prerequisites and the point at which a further arithmetic or representation-theoretic input is needed.', '',
        f'The [paper2 v3 extracts](units/) cover {len(paper)} units, with separate argument files where the manuscript writes out the proof later. The [blueprint extracts](blueprint/) cover {len(blueprint)} units. They retain the earlier reports’ wording. Consult each unit’s current review field for its status.', '',
        'The [note index](../data/notes.json) maps canonical IDs and Lean declaration names to excerpts, packet companions, and exact source ranges. The [edition register](../data/editions.json) gives the PDF fingerprints for the current and earlier editions. Some blueprint unit extracts reflect later local revisions and have their own source-file fingerprints.', ''])
    (atlas / 'notes/README.md').write_text('\n'.join(lines))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--atlas', required=True, type=Path)
    parser.add_argument('--project-archive', '--rh-notes', dest='project_archive', required=True, type=Path)
    args = parser.parse_args()
    main(args.atlas, args.project_archive)
