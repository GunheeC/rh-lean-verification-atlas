#!/usr/bin/env python3
"""Check the external name index and its reader pages without network access."""
from atlas_files import unit_files
import argparse
from collections import defaultdict
from pathlib import Path
import re
from build_name_crosswalk import PIN_TREES, SOURCES, read, render, guide


def validate(root):
    doc=read(root/'crosswalk/name_matches.json')
    pins=read(root/'data/pins.json')
    registry={r['id']:r for r in read(root/'sources/registry.json')['sources']}
    graph=read(root/'data/graph.json')
    routes=read(root/'crosswalk/adriazola.json')['dependency_routes']
    owners=defaultdict(set)
    for node in graph['nodes']:
        owners[node['name']].add(node['unit_id'])
    for file in unit_files(root):
        for decl in read(file)['lean']:
            if decl.get('role') != 'component':
                owners[decl['name']].add(file.stem)
    errors=[]
    def require(condition, message):
        if not condition:
            errors.append(message)
    require(doc['lean_commit'] == pins['source_commit'] and doc['pin_count'] == len(pins['anchors']),
            'name crosswalk: current pinned declaration census differs')
    require((root/'crosswalk/README.md').read_text() == guide(doc, registry, read(root/'crosswalk/adriazola.json')),
            'name crosswalk: reader census differs from current source data')
    require([s['source_id'] for s in doc['sources']]==list(SOURCES),'name crosswalk: missing or duplicate source')
    urls=set()
    for src in doc['sources']:
        sid=src['source_id']; reg=registry[sid]
        require(src['commit']==reg['revision'] and src['repository']==reg['url'] and src['git_tree_sha1']==PIN_TREES[sid],f'{sid}: source pin mismatch')
        mapping=reg['atlas_mapping']
        pairs={'matched_distinct_names':'distinct_declarations','name_file_pairs':'declaration_file_pairs',
               'files_with_matches':'matched_files','eligible_files_scanned':'eligible_files'}
        require(all(mapping.get(key)==src[field] for key,field in pairs.items()),f'{sid}: registry crosswalk counts are stale')
        require(mapping['target']=='crosswalk/'+sid+'.md',f'{sid}: registry reading destination is stale')
        if sid=='naskrecki':
            require(mapping['upstream_atlas_node_ids_matched']==sum(len(r['external_nodes']) for r in src['rows']),f'{sid}: invalid upstream node count')
        rows=src['rows'];files=src['files']
        require(src['distinct_declarations']==len(rows)==len({r['declaration'] for r in rows}),f'{sid}: invalid distinct name count')
        require(src['declaration_file_pairs']==sum(len(r['occurrences']) for r in rows),f'{sid}: invalid occurrence count')
        require(src['eligible_files']>=src['matched_files']==len(files),f'{sid}: invalid file count')
        require(all(re.fullmatch('[0-9a-f]{40}',f['git_blob_sha1']) and f['line_count']>0 for f in files.values()),f'{sid}: invalid file hash or line count')
        for row in rows:
            name=row['declaration'];where=f'{sid}/{name}'
            require(name in pins['anchors'] and row['level']=='name-level' and 'grade' not in row,f'{where}: unverified or graded declaration')
            require(row['unit_ids']==sorted(owners[name]),f'{where}: incorrect directly associated unit')
            support=routes.get(name,{}).get('unit_id') if not owners[name] else None
            require(row['dependency_unit']==support,f'{where}: incorrect graph reading route')
            locations=set()
            for hit in row['occurrences']:
                path=hit['path']
                require(path in files,f'{where}: missing file metadata')
                for section in hit['locations']:
                    nums=section['lines']
                    require(nums==sorted(set(nums)) and all(1<=n<=files[path]['line_count'] for n in nums),f'{where}: invalid source line')
                    if 'heading_line' in section:
                        require(section['heading_line']<=nums[0],f'{where}: heading after occurrence')
                    locations.update((path,n) for n in nums)
            require(bool(locations),f'{where}: missing source occurrence')
            for node in row['external_nodes']:
                require(sid=='naskrecki' and node['path']=='data/model.json' and re.fullmatch('/nodes/[0-9]+/declaration',node['pointer']) and (node['path'],node['line']) in locations,f'{where}: invalid atlas node pointer')
        page,links=render(src)
        require((root/('crosswalk/'+sid+'.md')).read_text()==page,f'{sid}: stale crosswalk page')
        urls.update(links)
    require(sorted(urls)==read(root/'sources/reader_urls.json')['urls'],'crosswalk: stale exact reader URL register')
    return errors


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1])
    args=parser.parse_args()
    findings=validate(args.root)
    if findings:
        raise SystemExit('\n'.join(findings))
    print('External source names, unit routes, occurrence locators, rendered pages and URLs verified.')
