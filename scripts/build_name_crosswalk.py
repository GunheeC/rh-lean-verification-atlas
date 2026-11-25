#!/usr/bin/env python3
"""Index exact pinned declaration references in three external reading projects.

Use --fetch to read the recorded public snapshots; or pass --cache DIR containing
SOURCE.tree.json and SOURCE.tar.gz for each registered source. No files from the
snapshots are extracted. Only identifiers, locations and hashes enter the atlas.
"""
from atlas_files import unit_files
import argparse
from bisect import bisect_left
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
import hashlib
import html
import io
import json
from pathlib import Path
import re
import subprocess
import tarfile
from urllib.parse import quote

BANNER = 'AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved'
SOURCES = ('naskrecki','jae-63','josebrox')
FORMATS = {'.md','.tex','.json','.lean','.dot','.mmd','.html','.txt','.tsv','.csv','.org','.rst','.bib'}
PIN_TREES = {
    'naskrecki': '9940cf4def7ab66186edd5584eadee737fc6aa7d',
    'jae-63': '694ddba91026222ddf4d34722c9742d93457ff0e',
    'josebrox': 'a410b7c343a726c6afc409467164a590d0532f97',
}
MD_HEAD = re.compile(r'^ {0,3}#{1,6}\s+(.*)')
TEX_HEAD = re.compile(r'^\s*\\(?:part|chapter|section|subsection|subsubsection)\*?\{')
TEX_LABEL = re.compile(r'\\label\{([\w:./-]+)\}')
JSON_STRING = re.compile(r'"(?:\\.|[^"\\])*"')


def read(path):
    return json.loads(path.read_bytes())


def fetch(url):
    return subprocess.check_output(['curl','-fsSL','--retry','1','--max-time','120',url])


def stable_json(data):
    return json.dumps(data, ensure_ascii=False, indent=2)+'\n'


def write(path, text, check):
    if check:
        if not path.exists() or path.read_text()!=text:
            raise ValueError('Stale: '+str(path))
    else:
        path.write_text(text)


def binary_hash(content):
    return hashlib.sha1(b'blob '+str(len(content)).encode()+b'\0'+content).hexdigest()


def eligible(path):
    p=Path(path)
    return p.suffix.lower() in FORMATS and not any(piece in {'.github','scripts','node_modules'} for piece in p.parts)


def validate_tree(tree, tree_sha, revision):
    if tree['truncated'] or tree['sha'] not in (tree_sha,revision):
        raise ValueError('Incomplete or changed upstream tree')
    groups=defaultdict(list)
    for entry in tree['tree']:
        dirname,_,tail=entry['path'].rpartition('/')
        groups[dirname].append((tail,entry['type'],entry['mode'],entry['sha']))
    expected={e['path']:e['sha'] for e in tree['tree'] if e['type']=='tree'}
    expected['']=tree_sha
    for dirname,members in groups.items():
        buf=bytearray()
        for name,kind,mode,sha in sorted(members,key=lambda v:(v[0]+('/' if v[1]=='tree' else '')).encode()):
            buf.extend(mode.lstrip('0').encode()+b' '+name.encode()+b'\0'+bytes.fromhex(sha))
        if hashlib.sha1(b'tree '+str(len(buf)).encode()+b'\0'+buf).hexdigest()!=expected[dirname]:
            raise ValueError('Changed tree entries: '+dirname)


def scan_source(record, pins, pattern, owner, support, cache):
    sid=record['id']
    repo=record['url'].removeprefix('https://github.com/')
    rev=record['revision']
    if cache:
        tree=read(cache/(sid+'.tree.json'))
        archive=(cache/(sid+'.tar.gz')).read_bytes()
    else:
        tree=json.loads(fetch(f'https://api.github.com/repos/{repo}/git/trees/{rev}?recursive=1'))
        archive=fetch(f'https://codeload.github.com/{repo}/tar.gz/{rev}')
    validate_tree(tree,PIN_TREES[sid],rev)
    files={e['path']:e for e in tree['tree'] if e['type']=='blob' and e['mode'] in ('100644','100755') and eligible(e['path'])}
    hits=defaultdict(list)
    file_records={}
    atlas_ids=defaultdict(dict)
    seen=set()
    with tarfile.open(fileobj=io.BytesIO(archive),mode='r:gz') as tf:
        for member in tf:
            path=member.name.partition('/')[2]
            if path not in files or not member.isfile():
                continue
            raw=tf.extractfile(member).read()
            if path in seen or binary_hash(raw)!=files[path]['sha']:
                raise ValueError(f'{sid}: changed or duplicate file {path}')
            seen.add(path)
            text=raw.decode('utf8')
            suffix=Path(path).suffix.lower()
            matches=defaultdict(lambda:defaultdict(set))
            section='file';heading_line=1
            for lineno,line in enumerate(text.splitlines(),1):
                if suffix=='.tex':
                    if TEX_HEAD.match(line):
                        section='section';heading_line=lineno
                    if lineno-heading_line<=1 and (label:=TEX_LABEL.search(line)):
                        section=label[1]
                    line=line.replace(r'\_', '_').replace(r'\allowbreak{}','').replace(r'\-', '')
                elif suffix in ('.md','.txt'):
                    heading=MD_HEAD.match(line)
                    if heading:
                        section_number=re.match(r'([0-9]+(?:\.[0-9]+)*)\b',heading[1])
                        section='§'+section_number[1] if section_number else 'heading'
                        heading_line=lineno
                elif suffix=='.html':
                    line=html.unescape(line)
                elif suffix=='.json' and '\\' in line:
                    # Decode individual JSON strings on this physical source line.
                    line=JSON_STRING.sub(lambda m:'"'+json.loads(m[0])+'"',line)
                for m in pattern.finditer(line):
                    name=m[1]
                    if name in pins:
                        matches[name][(section,heading_line)].add(lineno)
            if not matches:
                continue
            file_records[path]={'git_blob_sha1':files[path]['sha'],'line_count':len(text.splitlines())}
            if sid=='naskrecki' and path=='data/model.json':
                # Match the declaration field of a node, never an incidental name
                # in its description. Retain the node ID and JSON Pointer.
                array_start=min(re.finditer(r'^([ \t]*)"nodes"\s*:\s*\[',text,re.MULTILINE),key=lambda m:len(m[1]),default=None)
                if not array_start:
                    raise ValueError('Cannot locate upstream node array')
                cursor=array_start.end()
                line_ends=[m.start() for m in re.finditer('\n',text)]
                decoder=json.JSONDecoder()
                for i,recorded in enumerate(json.loads(text)['nodes']):
                    while text[cursor].isspace() or text[cursor]==',':
                        cursor+=1
                    node,end=decoder.raw_decode(text,cursor)
                    if node!=recorded:
                        raise ValueError('JSON pointer drifted')
                    name=node.get('declaration')
                    if name in pins:
                        raw_key=re.search(r'"declaration"\s*:\s*'+re.escape(json.dumps(name,ensure_ascii=False)),text[cursor:end])
                        if name not in matches or raw_key is None:
                            raise ValueError('Missing lexical evidence for '+name)
                        line=bisect_left(line_ends,cursor+raw_key.start())+1
                        atlas_ids[name][node['id']]={'id':node['id'],'component':node.get('component'),'path':path,
                            'line':line,'pointer':f'/nodes/{i}/declaration'}
                    cursor=end
            for name,sections in matches.items():
                evidence=[]
                for (section,hline),line_nums in sorted(sections.items(),key=lambda pair:pair[0][1]):
                    block={'lines':sorted(line_nums)}
                    if section!='file':
                        block['section']=section;block['heading_line']=hline
                    evidence.append(block)
                hits[name].append({'path':path,'locations':evidence})
    if seen!=set(files):
        raise ValueError(f'{sid}: archive omitted eligible paths: {sorted(set(files)-seen)}')
    rows=[]
    for name in sorted(hits):
        rows.append({'declaration':name,'level':'name-level','unit_ids':owner.get(name,[]),
                     'dependency_unit':support.get(name) if not owner.get(name) else None,
                     'external_nodes':sorted(atlas_ids[name].values(), key=lambda v:v['id']),
                     'occurrences':sorted(hits[name],key=lambda f:f['path'])})
    manifest=''.join(f'{path}\t{files[path]["sha"]}\n' for path in sorted(files)).encode()
    return {'source_id':sid,'repository':record['url'],'commit':rev,'git_tree_sha1':PIN_TREES[sid],
            'eligible_files':len(files),'matched_files':len(file_records),
            'eligible_path_and_blob_sha256':hashlib.sha256(manifest).hexdigest(),
            'distinct_declarations':len(rows),'declaration_file_pairs':sum(len(r['occurrences']) for r in rows),
            'files':dict(sorted(file_records.items())),'rows':rows}


def first_evidence(sid, row):
    def weight(e):
        path=e['path']
        if row['external_nodes'] and path=='data/model.json':return 0
        if sid=='jae-63' and path=='BLUEPRINT.md':return 0
        if sid=='josebrox':
            if path.startswith('paper/') and path.endswith('.tex'):return 0
            if path.startswith('notes/') and path.endswith('.md'):return 1
            if path.startswith('blueprint/') and path.endswith('.md'):return 2
        return 3 if path.endswith(('.md','.tex')) else 4
    return min(row['occurrences'], key=lambda e:(weight(e),e['path']))


def render(src):
    names={'naskrecki':'Naskręcki’s reading project','jae-63':'jae-63/rh-alpoge-blueprint','josebrox':'JoseBrox/GRH_distillation'}
    sid=src['source_id'];urls=set()
    out=[BANNER,'',f'# {names[sid]} declaration references','',
         f'The scan found **{src["distinct_declarations"]} distinct pinned Lean names** across {src["matched_files"]} of {src["eligible_files"]} eligible files in revision `{src["commit"]}`. Every row is a name-level match. A name appearing in prose, an example, a diagram or an imported index records a reference only.','',
         'The table gives one reading location per name. The [full index](name_matches.json) retains all matched files, sections and line numbers. Units listed here own the declaration in the atlas graph or include it on the unit card. A unit marked *dependency* reaches the named declaration through a checked path in the original graph. All names also appear in the [declaration lookup](../lookup/declarations.md).','',
         '| Lean declaration | External source location | Atlas unit |','|---|---|---|']
    for row in src['rows']:
        e=first_evidence(sid,row)
        block=e['locations'][0]
        path=e['path'];line=block['lines'][0]
        external_ids=', '.join(x['id'] for x in row['external_nodes'])
        if external_ids:
            # Text hits in this file can precede a node's declaration key. Link
            # the exact line of the node value, separately from prose mentions.
            line=row['external_nodes'][0]['line']
        label=external_ids or block.get('section','')
        if label in ('section','heading'):
            label=f'{label} at L{block["heading_line"]}'
        url=f'{src["repository"]}/blob/{src["commit"]}/{quote(path,safe="/")}#L{line}'
        urls.add(url)
        location=(label+' · ' if label else '')+f'{path} L{line}'
        links=', '.join(f'[{uid}](../units/{uid}.md)' for uid in row['unit_ids'])
        if not links and row['dependency_unit']:
            uid=row['dependency_unit'];links=f'dependency [{uid}](../units/{uid}.md)'
        if not links:
            links='—'
        out.append(f'| `{row["declaration"]}` | [{location}]({url}) | {links} |')
    out.extend(['','[Landscape](../LANDSCAPE.md) · [Crosswalk guide](README.md).'])
    return '\n'.join(out)+'\n',urls


def guide(doc, sources, manuscript):
    """Build the reader census from the same records as the detailed pages."""
    mappings = manuscript["mappings"]
    hypotheses = sum(row["kind"] == "numbered_hypothesis" for row in mappings)
    title = sources["adriazola"]["short_title"]
    lines = ["# Correspondence with external reading projects", "", BANNER, "",
             "| Source | Rows | Recorded correspondence |", "|---|---:|---|",
             f"| [{title}](adriazola.md) | {len(mappings)} | Manuscript numbers, identified Lean propositions and atlas units. Includes {hypotheses} numbered hypotheses. |"]
    for scan in doc["sources"]:
        sid = scan["source_id"]
        title = sources[sid]["short_title"]
        lines.append(f"| [{title}]({sid}.md) | {scan['distinct_declarations']} | Exact occurrences of a Lean declaration name across {scan['matched_files']} source files at the pinned commit. |")
    lines += ["", f"The three name indexes scan all {doc['pin_count']:,} registered Lean names. They cover text, TeX, Markdown, Lean, JSON, diagram sources and the other formats listed in the index. They exclude binary renderings, software implementations and CI files. A name match supplies a locator and carries no mathematical grade. Each occurrence has a file, line and Git blob identifier. With local copies of the pinned archives and Git trees, run `python3 scripts/build_name_crosswalk.py --cache DIRECTORY --check`. [Name index and scan scope](name_matches.json) · [Source editions](../sources/registry.json)."]
    return "\n".join(lines) + "\n"


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1])
    ways=parser.add_mutually_exclusive_group(required=True)
    ways.add_argument('--fetch',action='store_true',help='Read only the named public snapshots.')
    ways.add_argument('--cache',type=Path,help='Use a directory containing pinned trees and tarballs.')
    parser.add_argument('--check',action='store_true',help='Compare generated files with existing ones.')
    opts=parser.parse_args();root=opts.root
    pins=read(root/'data/pins.json')['anchors']
    tops=sorted({n.split('.')[0] for n in pins},key=len,reverse=True)
    pattern=re.compile(r"(?<![\w.'])(?:_root_\.)?((?:"+'|'.join(map(re.escape,tops))+r")(?:\.[\w'!?]+)*)(?![\w'])")
    graph=read(root/'data/graph.json')
    owner=defaultdict(set)
    for n in graph['nodes']:
        owner[n['name']].add(n['unit_id'])
    for p in unit_files(root):
        for a in read(p)['lean']:
            if a.get('role') != 'component':
                owner[a['name']].add(p.stem)
    owner={name:sorted(ids) for name,ids in owner.items()}
    support={name:r['unit_id'] for name,r in read(root/'crosswalk/adriazola.json')['dependency_routes'].items()}
    registry={s['id']:s for s in read(root/'sources/registry.json')['sources']}
    with ThreadPoolExecutor(max_workers=3) as executor:
        futures=[executor.submit(scan_source,registry[s],pins,pattern,owner,support,opts.cache) for s in SOURCES]
        sources=[f.result() for f in futures]
    doc={'notice':BANNER,'relation':'name-level','lean_commit':graph['source_commit'],'pin_count':len(pins),
         'format_scope':sorted(FORMATS),'excluded_directories':['.github','scripts','node_modules'],
         'scope':'Source text, including structured data, imported indexes and text diagram sources. Binary renderings, compiled outputs and software implementations are outside the chosen reading corpus. An entry represents one source and one exact atlas declaration. Aliases, unqualified suffixes and thematic similarities are excluded. Registered root-namespace declarations are matched by their complete names.',
         'sources':sources}
    write(root/'crosswalk/name_matches.json',stable_json(doc),opts.check)
    source_file = root/'sources/registry.json'
    source_doc = read(source_file)
    for entry in source_doc['sources']:
        scan = next((s for s in sources if s['source_id'] == entry['id']), None)
        if scan is None:
            continue
        mapping = entry['atlas_mapping']
        mapping.update(matched_distinct_names=scan['distinct_declarations'],
                       name_file_pairs=scan['declaration_file_pairs'],
                       files_with_matches=scan['matched_files'],
                       eligible_files_scanned=scan['eligible_files'])
        if entry['id'] == 'naskrecki':
            mapping['upstream_atlas_node_ids_matched'] = sum(len(row['external_nodes']) for row in scan['rows'])
    write(source_file, stable_json(source_doc), opts.check)
    write(root/'crosswalk/README.md', guide(doc, registry, read(root/'crosswalk/adriazola.json')), opts.check)
    urls=set()
    for src in sources:
        md,links=render(src)
        urls.update(links)
        write(root/('crosswalk/'+src['source_id']+'.md'),md,opts.check)
    write(root/'sources/reader_urls.json',stable_json({'purpose':'Exact URLs displayed by the three source-name crosswalk pages. Each URL names an immutable commit, verified file and physical line.','urls':sorted(urls)}),opts.check)
    print(', '.join(f'{s["source_id"]}: {s["distinct_declarations"]} names, {s["declaration_file_pairs"]} name/file pairs' for s in sources))


if __name__=='__main__':
    main()
