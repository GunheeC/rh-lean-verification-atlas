"""Extract bounded manuscript entries from paper2 v3, recording their origin and PDF heading page."""
from pathlib import Path
import argparse, json, hashlib, re
from collections import defaultdict
NOTICE='AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved'
D='002 004 006 014 024 025 033 044 077 082 097 108 123 128 154 155 174 193 203 230 245 302 309 317 331 340 351 379 394 415 421 427 443 479 481 484 486 506 510 511 513 528 532 536 547 548 549 550 551 558 561 562 563 564 566 567 568 569 570 575'
IDS=[f'P{i:03d}' for i in [*range(1,51),90,96,134]]+[f'{k}{i:02d}' for k,size in [('T',26),('B',10),('W',16)] for i in range(1,size+1)]+['D'+s for s in D.split()]
def sha(b):return hashlib.sha256(b).hexdigest()
def lines(p):return p.read_text().splitlines(keepends=True)
def main(args):
    atlas=args.atlas; notes=atlas/'notes'; root=args.project_archive; v3=args.v3_before_v4
    paper=root/'paper2'; folder=notes/'units'; folder.mkdir(exist_ok=True)
    labels={k:(n,int(p)) for k,n,p in re.findall(r'\\newlabel\{([^{}]*)\}\{\{([^{}]*)\}\{(\d+)\}',args.aux.read_text())}
    pdf_hash=sha(args.pdf.read_bytes())
    ed=json.loads((atlas/'data/editions.json').read_text())['editions']['paper2_v3']
    if pdf_hash!=ed['sha256']:raise ValueError('wrong v3 PDF')
    sources={p.name:p for p in paper.glob('*.tex')}
    for name in ['upper.tex','split_status.tex','node_status.tex','architecture.tex']:
        sources[name]=v3/name
    linecache={n:lines(p) for n,p in sources.items()}
    status={}
    for n in ['split_status.tex','node_status.tex']:
        for ln in linecache[n]:
            m=re.search(r'\\csname (?:node|split)([PTBW]\d+)\\endcsname\{(.*)\}\s*$',ln)
            if m:status[m[1]]=re.search(r'\\nolinkurl\{([^}]+)',m[2])[1]
    anchors={}
    for name,ll in linecache.items():
        for i,line in enumerate(ll):
            for key in re.findall(r'\\label\{((?:pn:P|sub:[BTW]|decomp:D)\d+)\}',line):
                if key.split(':')[1] in IDS:anchors[key]=name,i
    note_index={}
    groups=defaultdict(list)
    for unit in IDS:
        key=('pn:' if unit.startswith('P') else 'decomp:' if unit.startswith('D') else 'sub:')+unit
        name,i=anchors[key]; ll=linecache[name]; start=i
        while start>=0 and not re.search(r'\\begin\{(?:formalstatement|definition|theorem|lemma|proposition|corollary)\}',ll[start]):start-=1
        if start<0 or i-start>6:raise ValueError((key,'missing statement opener'))
        end=start+1
        while end<len(ll) and not re.search(r'^\s*\\(?:begin\{(?:formalstatement|definition|theorem|lemma|proposition|corollary)\}|(?:sub)*section\*?\{|clearpage|end\{document\}|Needspace\{)',ll[end]):end+=1
        if unit == 'P022':
            start = next(j for j in range(start) if r'\subsubsection{The abstract statement}' in ll[j])
            proof = next(j for j in range(i,len(ll)) if r'\begin{proof}[Proof of \nodeid{P022}]' in ll[j])
            end = next(j+1 for j in range(proof,len(ll)) if r'\end{proof}' in ll[j])
        while end>start and not ll[end-1].strip():end-=1
        segment=''.join(ll[start:end]); num,page=labels[key]
        decl=status.get(unit)
        if unit.startswith('D'):
            m=re.search(r'\\bfseries [^{}]*\}\\quad \\nolinkurl\{([^}]+)',segment)
            if not m:raise ValueError((unit,'decomposition source declaration missing'))
            decl=m[1]
        if not decl:raise ValueError(unit)
        r={'file':f'paper2/{name}','line0':start+1,'line1':end,'fragment_sha256':sha(segment.encode()),'file_sha256':sha(sources[name].read_bytes())}
        note_index[unit]={'path':f'notes/units/{unit}.tex','edition':'paper2_v3','label':key,'number':num,'heading_page':page,'lean_declarations':[decl],'source_ranges':[r]}
        groups[decl].append(unit)
        intro=[f'% {NOTICE}',f'% Atlas unit {unit}. Local manuscript v3, item {num}, heading on printed PDF p. {page}.',f'% {decl}',f'% {r["file"]}:{start+1}–{end}. Verbatim excerpt; SHA-256 {r["fragment_sha256"]}.','% Original TeX uses the macros and cross-reference keys of the source manuscript.']
        (folder/(unit+'.tex')).write_text('\n'.join(intro)+'\n\n'+segment)
    # Additional separately paginated arguments in v3, rather than reporting an old
    # catalogue front as the long derivation. These are distinct from reviewed grades.
    sup={'P017':('r23_p017','r23:p017'),'P021':('r23_link','r23:link'),'P015':('r23_host','r23:host'),'P012':('r23_p012','sec:r23-p012'),'P013':('r23_selmer','sec:r23-selmer'),'P096':('pending_p096','sec:pending-p096'),'P134':('pending_proof','sec:pending-p134')}
    sup['D563'] = ('r23_budget', 'r23:budget')
    for k,(base,key) in sup.items():
        filename=base+'.tex'; p=v3/filename if (v3/filename).is_file() else (root/'out'/filename if base.startswith('r23') else paper/filename)
        orig=('out/' if base.startswith('r23') else 'paper2/')+filename
        if key not in labels:raise ValueError(key)
        dst=folder/f'{k}-argument.tex'; page=labels[key][1]
        dst.write_text(f'% {NOTICE}\n% Manuscript v3, heading p. {page}; original {orig}, SHA-256 {sha(p.read_bytes())}.\n'+p.read_text())
        note_index[k]['additional_exposition']={'path':dst.relative_to(atlas).as_posix(),'heading_page':page,'source':orig,'source_sha256':sha(p.read_bytes())}
    data={'notice':NOTICE, 'edition':'paper2_v3','pdf_sha256':pdf_hash,'page_rule':'Heading pages come from the aux file of the hash-matched edition. They locate the entry; they are not a statement of its proof length. Reading lengths for packets use actual page images.', 'units':note_index, 'lean_declarations':dict(groups)}
    (atlas/'data/notes_units.json').write_text(json.dumps(data,indent=2,ensure_ascii=False)+'\n')
if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--project-archive','--rh-notes',dest='project_archive',required=True,type=Path)
    for k in ['atlas','v3-before-v4','pdf','aux']:p.add_argument('--'+k,required=True,type=Path)
    main(p.parse_args())
