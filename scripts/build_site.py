#!/usr/bin/env python3
"""Build a local HTML edition of the atlas. Uses only the Python standard library."""
from atlas_files import unit_files
from edition_links import blueprint_page
import argparse
from collections import defaultdict
import hashlib
from html import escape
import json
import os
from pathlib import Path
import re
import sys
import textwrap
from urllib.parse import quote, unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
NOTICE = "AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved"
MATHJAX = "https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-mml-chtml.js"
MENU = [("Home", "index.html"), ("Status", "STATUS.html"), ("Map", "MAP.html"),
        ("Tracks", "dashboard/index.html"), ("Search declarations", "lookup/search.html")]
CSS = """
:root{color-scheme:light;--ink:#182e35;--muted:#485d64;--line:#cbd5d3;--link:#005d69;--paper:#fdfdf9}
*{box-sizing:border-box}html{background:var(--paper);color:var(--ink)}
body{margin:0;font:17px/1.62 'STIX Two Text',Georgia,serif}
header,footer,nav,th,.notice,label,.search-state,small{font-family:'Source Sans 3',system-ui,sans-serif}
header{background:#14383d;color:white;border-bottom:4px solid #c89b58}
.bar{max-width:78rem;margin:auto;padding:.8rem 5%;display:flex;flex-wrap:wrap;align-items:center;gap:.45rem 2rem}
.brand{font:600 1.15rem/1.45 'STIX Two Text',Georgia,serif;color:white}
nav{display:flex;gap:.3rem 1.25rem;flex-wrap:wrap;font-size:.92rem}
header a{color:#f1f7f6;text-decoration:none}header a:hover,header a:focus{text-decoration:underline}
main{width:90%;max-width:69rem;margin:2.8rem auto 5rem;min-height:55vh}
h1,h2,h3{line-height:1.18;letter-spacing:-.02em;text-wrap:balance}
h1{font-size:2.8rem;margin:.6em 0 .45em}h2{font-size:1.6rem;margin:1.9em 0 .5em}h3{font-size:1.2rem;margin:1.4em 0 .4em}
p,ol,ul,blockquote{max-width:78ch}p{margin:.7em 0 1em}li{margin:.34em 0}li p{margin:0}
a{color:var(--link);text-underline-offset:.16em;overflow-wrap:anywhere}a:hover{color:#873f16}a:focus-visible,input:focus-visible{outline:3px solid #b76a22;outline-offset:2px}
.notice{color:var(--muted);padding:.55em .9em;border-left:3px solid #b48e57;background:#f0f2ed;font-size:.89rem}
table{width:100%;border-collapse:collapse;text-align:left;font-size:.95rem}th{font-size:.84rem;color:#264c50;background:#e7eeea}th,td{vertical-align:top;padding:.52rem .65rem;border-bottom:1px solid var(--line)}
tr:nth-child(even) td{background:#f5f7f3}.scroll{overflow:auto;margin:1.1rem 0}
code,pre{font: .85em/1.5 'IBM Plex Mono',ui-monospace,monospace}code{overflow-wrap:anywhere;background:#eef1ed;padding:.1em .2em;border-radius:2px}
pre{padding:1em;background:#eef1ed;overflow:auto}pre code{font-size:1em;padding:0}.math{overflow-wrap:anywhere}.display{overflow:auto;margin:1em 0}
img{display:block;max-width:100%;height:auto;margin:1rem auto}.diagram{max-width:100%;overflow:auto;border:1px solid var(--line);background:#fff}.diagram svg{display:block;width:100%;min-width:42rem;height:auto}.diagram rect{fill:#edf4ef;stroke:#678483}.diagram text{font:14px system-ui,sans-serif;fill:#172e34}
.search-input{display:block;width:min(100%,47rem);font:inherit;padding:.65rem .8rem;border:1px solid #738d89;border-radius:4px;background:white;margin:.3rem 0 .8rem}
.search-state,small{color:var(--muted);font-size:.89rem}#results{padding-left:1.4rem}#results li{margin:.7em 0}
footer{border-top:1px solid var(--line);font-size:.85rem;padding:1rem 5%;color:var(--muted)}details{margin:.6rem 0}
@media(max-width:42rem){h1{font-size:2.1rem}main{margin-top:1.35rem}.bar{gap:.25rem .8rem}nav{font-size:.82rem;gap:.25rem .8rem}th,td{padding:.4rem}.scroll table{min-width:28rem}}
@media print{header,footer,form{display:none}main{width:100%;max-width:none;margin:0}.scroll,.display,.diagram{overflow:visible}.diagram svg{min-width:0}}
"""
SEARCH = """
const catalog = JSON.parse(document.getElementById('catalog').textContent);
const query = document.getElementById('query');
const results = document.getElementById('results');
const count = document.getElementById('result-count');

function link(label, href) {
  const anchor = document.createElement('a');
  anchor.textContent = label;
  anchor.href = href;
  return anchor;
}

function showMatches() {
  const term = query.value.trim().toLowerCase();
  const matches = catalog.filter(([name, , unitIds]) =>
    name.toLowerCase().includes(term) || unitIds.some(id => id.toLowerCase() === term)
  );
  results.replaceChildren();
  const limit = 50;
  const countLabel = matches.length === 1 ? ' declaration' : ' declarations';
  count.textContent = matches.length.toLocaleString('en-US') + countLabel
    + (matches.length > limit ? ' · showing the first ' + limit : '');

  for (const [name, location, unitIds, range, dominated] of matches.slice(0, limit)) {
    const item = document.createElement('li');
    const code = document.createElement('code');
    code.textContent = name;
    const nameLink = link('', location);
    nameLink.append(code);
    item.append(nameLink, document.createElement('br'));
    const detail = document.createElement('small');
    detail.textContent = range + ' · ' + dominated.toLocaleString('en-US') + ' dominated lines · ';
    item.append(detail);
    unitIds.forEach((id, index) => {
      if (index) item.append(', ');
      item.append(link(id, '../units/' + encodeURIComponent(id) + '.html'));
    });
    results.append(item);
  }
}

query.addEventListener('input', showMatches);
query.value = new URLSearchParams(location.search).get('q') || '';
showMatches();
"""


def output_name(source):
    if source.name == "README.md":
        return source.with_name("index.html")
    return source.with_suffix(".html")


def relative(path, output):
    return quote(os.path.relpath(path, output.parent), safe="/#-._~")


def slug(text):
    return re.sub(r"[^\w\s-]", "", text.lower()).replace(" ", "-")


def diagram(lines, lang="en"):
    """Lay out the atlas's labelled acyclic Mermaid arrows as a local SVG."""
    names, edges = {}, []
    styles, classes = {}, {}
    color = r"(#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})?)"
    token = r'(\w+)(?:\["([^"]+)"\])?'
    for raw in lines[1:]:
        line = raw.strip().rstrip(";")
        style = re.fullmatch(r"classDef\s+(\w+)\s+fill:" + color + r",\s*stroke:" + color, line)
        if style:
            styles[style[1]] = f"fill:{style[2]};stroke:{style[3]}"
            continue
        group = re.fullmatch(r"class\s+(\w+(?:,\s*\w+)*)\s+(\w+)", line)
        if group:
            for node in group[1].split(","):
                classes[node.strip()] = group[2]
            continue
        row = re.fullmatch(r'\s*'+token+r'\s*-->\s*'+token+r'\s*', line)
        if not row:
            raise ValueError("Unsupported Mermaid edge: " + raw)
        a, alabel, b, blabel = row.groups()
        names[a] = alabel or names.get(a, a)
        names[b] = blabel or names.get(b, b)
        edges.append((a,b))
    if set(classes) - set(names) or set(classes.values()) - set(styles):
        raise ValueError("Unknown node or style in Mermaid class directive")
    parents = defaultdict(list)
    for a,b in edges:
        parents[b].append(a)
    ranks = {}
    while len(ranks) < len(names):
        step = {n: max((ranks[p]+1 for p in parents[n]), default=0)
                for n in names if n not in ranks and all(p in ranks for p in parents[n])}
        if not step:
            raise ValueError("Cycle in atlas map")
        ranks.update(step)
    layers = [[n for n in names if ranks[n] == i] for i in range(max(ranks.values())+1)]
    width = max(map(len,layers))*176 + 12
    pos = {n:(width/2+(j-(len(layer)-1)/2)*176, 40+i*104)
           for i, layer in enumerate(layers) for j,n in enumerate(layer)}
    height = 80+(len(layers)-1)*104
    key = hashlib.sha256("\n".join(lines).encode()).hexdigest()[:12]
    figure_title = "의존 관계도" if lang == "ko" else "Dependency diagram"
    text_label = "연결 관계를 글로 읽기" if lang == "ko" else "Read the connections as text"
    out = [f'<figure class="diagram"><svg role="img" viewBox="0 0 {width} {height}" aria-labelledby="title-{key}"><title id="title-{key}">{figure_title}</title>',
           f'<defs><marker id="arrow-{key}" viewBox="0 0 10 10" markerWidth="7" markerHeight="7" refX="9" refY="5" orient="auto"><path d="M 0 0 L 10 5 L 0 10 z" fill="#4b686c"/></marker></defs>']
    for a,b in edges:
        x, y = pos[a]
        xx, yy = pos[b]
        mid = (y + yy) / 2
        out.append(f'<path d="M{x},{y+29} C{x},{mid} {xx},{mid} {xx},{yy-30}" fill="none" stroke="#526e72" stroke-width="1.5" marker-end="url(#arrow-{key})"/>')
    for n,(x,y) in pos.items():
        label=textwrap.wrap(names[n], 11 if lang == "ko" else 21, break_long_words=False)
        style = f' style="{styles[classes[n]]}"' if n in classes else ""
        out.append(f'<rect x="{x-82}" y="{y-28}" width="164" height="56" rx="5" fill="#edf4ef" stroke="#678483"{style}/>')
        for j, line in enumerate(label):
            out.append(f'<text x="{x}" y="{y+5+(j-(len(label)-1)/2)*15}" text-anchor="middle" font-family="sans-serif" font-size="14" fill="#172e34">{escape(line)}</text>')
    out.append(f'</svg></figure><details><summary>{text_label}</summary><ul>')
    out += [f'<li>{escape(names[a])} → {escape(names[b])}</li>' for a,b in edges]
    return ''.join(out)+'</ul></details>'


def page_layout(path,title,body,lang="en",math=False):
    nav = ' '.join(f'<a href="{relative(Path(url),path)}">{label}</a>' for label,url in MENU)
    head = ''
    if math:
        head = ('<script>window.MathJax={tex:{inlineMath:[["$","$"]],displayMath:[["$$","$$"]],'
                'processEscapes:true},options:{ignoreHtmlClass:"no-math"}};</script>'
                f'<script defer src="{MATHJAX}"></script>')
    return (f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" '
            f'content="width=device-width,initial-scale=1"><title>{escape(title)} · RH verification atlas</title>'
            f'<link rel="stylesheet" href="{relative(Path("atlas.css"),path)}">{head}</head><body>'
            f'<header><div class="bar"><a class="brand" href="{relative(Path("index.html"),path)}">RH verification atlas</a>'
            f'<nav aria-label="Atlas navigation">{nav}</nav></div></header><main>{body}</main>'
            f'<footer><a href="{relative(Path("help.html"),path)}">Using the local edition</a></footer></body></html>\n')

INLINE = re.compile(
    r'(?P<code>`[^`\n]+`)'
    r'|(?P<anchor><a (?:id|name)="[\w.-]+"></a>)'
    r'|(?P<image>!?)\[(?P<label>(?:[^\[\]]|\[[^\[\]]*\])*)\]\((?P<href>[^\s)]+)\)'
    r'|(?P<math>\$\$(?:.|\n)+?\$\$|(?<!\\)\$(?:\\\$|[^$\n])+?(?<!\\)\$)'
    r'|(?P<strong>\*\*[^*\n]+\*\*)|(?P<em>\*(?!\s)[^*\n]+?\*)'
)
HEADING = re.compile(r'^(#{1,6})\s+(.+)')
LIST = re.compile(r'^\s*([-*]|\d+\.)\s+(.+)')
COLUMN_RULE = re.compile(r'^\s*\|?\s*:?-{3,}:?\s*\|')
TABLE_CELL = re.compile(r'(`[^`]*`|\$[^$]*\$|\\\||[^|`$\\]+|\\.|[`$])+')


class Edition:
    def __init__(self, root, output=None):
        self.root = root.resolve()
        # In the checkout, link to the sole repository copy. A site written to any other directory
        # keeps its own PDFs so it can be moved as a unit.
        self.in_checkout = (output or self.root / "site").resolve() == self.root / "site"
        editions = json.loads((self.root / "data/editions.json").read_bytes())["editions"]
        blueprint = editions["blueprint_v13b"]
        starters = json.loads((self.root / "data/notes_starters.json").read_bytes())["starters"]
        self.packet_pages = {}
        for packet in starters.values():
            src = Path(packet["path"])
            for folio, physical in zip(packet["printed_pages"], packet["pdf_pages"], strict=True):
                page = blueprint_page(blueprint, physical)
                self.packet_pages[src, f"pages/{folio}.webp"] = (
                    f"../../{blueprint['repository_file']}#page={page}",
                    f"Open printed page {folio} in blueprint v13b",
                )
        self.pages = {}
        self.assets = {}
        self.directories = set()
        self.files = {}

    def href(self, src, url):
        parts = urlsplit(url)
        if parts.scheme or parts.netloc:
            if parts.scheme not in {"https", "http", "mailto"}:
                raise ValueError(f"Unsupported URL in {src}: {url}")
            return url
        if not parts.path:
            return url
        target = (self.root / src.parent / unquote(parts.path)).resolve()
        local = target.relative_to(self.root)
        if local.parts and local.parts[0] in {".git", "site"}:
            if local == Path("site/index.html"):
                return relative(Path("index.html"), self.pages[src])
            raise ValueError(f"Unexpected target in {src}: {url}")
        if target.is_dir():
            index = local / "README.md"
            dest = self.pages.get(index)
            if not dest:
                dest = local / "index.html"
                self.directories.add(local)
        elif local in self.pages:
            dest = self.pages[local]
        elif target.is_file() and self.in_checkout and local.parts[:1] == ("editions",):
            dest = Path("..") / local
        elif target.is_file():
            # Verbatim archived Markdown is a text download, distinct from the new reading pages.
            dest = local.with_suffix(".md.txt") if local.suffix == ".md" else local
            self.assets[dest] = target
        else:
            raise ValueError(f"Missing local target in {src}: {url}")
        out = relative(dest, self.pages[src])
        if parts.query:
            out += "?" + parts.query
        if parts.fragment:
            out += "#" + parts.fragment
        return out

    def inline(self, src, s):
        result, start = [], 0
        for m in INLINE.finditer(s):
            result.append(escape(s[start:m.start()].replace(r"\|","|")))
            if m.group('href'):
                href=escape(self.href(src,m['href']),quote=True)
                if m['image']:
                    img = f'<img src="{href}" alt="{escape(m["label"],quote=True)}" loading="lazy">'
                    packet = self.packet_pages.get((src, m["href"]))
                    if packet:
                        pdf, label = packet
                        dest = escape(self.href(src, pdf), quote=True)
                        img = f'<a href="{dest}" aria-label="{label}">{img}</a>'
                    result.append(img)
                else:
                    result.append(f'<a href="{href}">{self.inline(src,m["label"])}</a>')
            elif m.group('code'):
                result.append('<code>'+escape(m['code'][1:-1])+'</code>')
            elif m.group('anchor'):
                result.append(m['anchor'])
            elif m.group('math'):
                result.append('<span class="math">'+escape(m['math'])+'</span>')
            elif m.group('strong'):
                result.append('<strong>'+self.inline(src,m['strong'][2:-2])+'</strong>')
            else:
                result.append('<em>'+escape(m['em'][1:-1])+'</em>')
            start=m.end()
        return ''.join(result)+escape(s[start:].replace(r"\|","|"))

    def markdown(self, src):
        text=(self.root/src).read_text()
        lines=text.splitlines()
        out=[]
        counts=defaultdict(int)
        title=next((s[2:] for s in lines if s.startswith('# ')),src.stem)
        i=0
        def table(j):
            return j+1<len(lines) and lines[j].startswith('|') and COLUMN_RULE.match(lines[j+1])
        def block(j):
            line=lines[j]
            return (not line.strip() or HEADING.match(line) or LIST.match(line) or line.startswith(('> ','```','$$')) or table(j))
        while i<len(lines):
            line=lines[i]
            i+=1
            if not line.strip():
                continue
            if line == NOTICE:
                out.append('<p class="notice">'+NOTICE+'</p>')
            elif (match:=HEADING.match(line)):
                level=len(match[1])
                anchor=slug(match[2])
                counts[anchor] += 1
                if counts[anchor]>1:
                    anchor+='-'+str(counts[anchor]-1)
                out.append(f'<h{level} id="{escape(anchor)}">{self.inline(src,match[2])}</h{level}>')
            elif line.startswith('```'):
                start=i
                while i<len(lines) and not lines[i].startswith('```'):
                    i+=1
                if i==len(lines):
                    raise ValueError(f"Unclosed code fence in {src}")
                content=lines[start:i]
                i += 1
                if line.strip()=='```mermaid':
                    out.append(diagram(content, lang="ko" if "ko" in src.parts else "en"))
                else:
                    out.append('<pre><code>'+escape('\n'.join(content))+'</code></pre>')
            elif line.strip()=='$$':
                start=i
                while i<len(lines) and lines[i].strip()!='$$':
                    i+=1
                if i==len(lines):
                    raise ValueError(f"Unclosed display in {src}")
                out.append('<div class="math display">$$'+escape('\n'.join(lines[start:i]))+'$$</div>')
                i += 1
            elif table(i-1):
                rows=[line]
                i += 1
                while i<len(lines) and lines[i].startswith('|'):
                    rows.append(lines[i])
                    i += 1
                out.append('<div class="scroll"><table>')
                for j,row in enumerate(rows):
                    tag='td' if j else 'th'
                    cells=[m.group().strip() for m in TABLE_CELL.finditer(row.strip().strip('|'))]
                    out.append(('<tbody>' if j==1 else '<thead>' if j==0 else '')+'<tr>'+
                               ''.join(f'<{tag}>{self.inline(src,c)}</{tag}>' for c in cells)+'</tr>'+
                               ('</thead>' if j==0 else ''))
                out.append(('</tbody>' if len(rows)>1 else '')+'</table></div>')
            elif (match:=LIST.match(line)):
                tag='ol' if match[1][0].isdigit() else 'ul'
                items=[match[2]]
                while i<len(lines):
                    next_item=LIST.match(lines[i])
                    if next_item:
                        if next_item[1][0].isdigit()!=(tag=='ol'):
                            break
                        items.append(next_item[2])
                        i += 1
                    elif lines[i].startswith(('  ','\t')):
                        items[-1]+='\n'+lines[i].lstrip()
                        i += 1
                    elif not lines[i].strip() and i+1<len(lines) and LIST.match(lines[i+1]):
                        i+=1
                    else:
                        break
                out.append(f'<{tag}>'+''.join('<li>'+self.inline(src,s).replace('\n','<br>')+'</li>' for s in items)+f'</{tag}>')
            elif line.startswith('> '):
                quotes=[line[2:]]
                while i<len(lines) and lines[i].startswith('> '):
                    quotes.append(lines[i][2:])
                    i += 1
                out.append('<blockquote>' + '<br>'.join(self.inline(src, row.rstrip()) for row in quotes) + '</blockquote>')
            elif line.strip() in {'---','***'}:
                out.append('<hr>')
            else:
                para=[line]
                while i<len(lines) and not block(i):
                    para.append(lines[i])
                    i += 1
                out.append('<p>'+self.inline(src,' '.join(para))+'</p>')
        body='\n'.join(out)
        if src==Path('lookup/declarations.md'):
            first=body.index('</h1>')+5
            body=body[:first]+'<p><a href="search.html">Search all pinned declarations by name or unit</a></p>'+body[first:]
        return page_layout(self.pages[src], title, body, lang='ko' if src.name=='README.ko.md' or 'ko' in src.parts else 'en', math='class="math' in body)

    def build(self):
        index = self.root/'data/declarations.json'
        records=json.loads(index.read_text())['declarations']
        units=sorted(unit_files(self.root))
        missing=[p.stem for p in units if not p.with_suffix('.md').is_file()]
        if missing:
            raise ValueError(f"Generate the {len(missing)} missing unit pages with scripts/unit_pages.py first.")
        selected=set()
        for pattern in ('*.md','units/*.md','tracks/*/*.md','dashboard/*.md','questions/*.md','notes/README.md',
                        'notes/*/README.md','notes/formal/procedures.md','notes/units/*.md','lookup/*.md','crosswalk/*.md','sources/*.md','progress/*.md','signoffs/examples/*.md','signoffs/*.md','docs/*.md','pillars/*.md','docs/ko/*.md','docs/ko/pillars/*.md','docs/ko/signoffs/*.md','reviews/*.md'):
            selected.update(p.relative_to(self.root) for p in self.root.glob(pattern))
        self.pages={p:output_name(p) for p in sorted(selected)}
        for src, dest in self.pages.items():
            self.files[dest]=self.markdown(src).encode()
        self.files[Path('lookup/search.html')]=self.search(records).encode()
        self.files[Path('atlas.css')]=CSS.strip().encode()+b'\n'
        help_body='<h1>Using the local edition</h1><p class="notice">'+NOTICE+'</p><p>Open <code>site/index.html</code> with a browser. The reading pages, diagrams, declaration search, page images and linked local evidence are available from disk. Formula typesetting uses a pinned MathJax release when the browser can reach its CDN. Offline, the original TeX remains readable.</p><h2>Rebuild</h2><p>From the atlas directory, run <code>python3 scripts/build_site.py</code>. Use <code>python3 scripts/build_site.py --check</code> to check that the edition matches the source files. The builder uses the Python standard library.</p>'
        self.files[Path('help.html')]=page_layout(Path('help.html'),'Using the local edition',help_body).encode()
        for folder in sorted(self.directories):
            items=[]
            for original in sorted((self.root/folder).iterdir()):
                if not original.is_file() or original.name.startswith('.'):
                    continue
                local=original.relative_to(self.root)
                target=self.pages.get(local)
                if not target:
                    target=local.with_suffix('.md.txt') if local.suffix=='.md' else local
                    self.assets[target]=original
                items.append(f'<li><a href="{relative(target,folder/"index.html")}">{escape(original.name)}</a></li>')
            body=f'<h1>{escape(str(folder))}</h1><p class="notice">{NOTICE}</p><ul>'+''.join(items)+'</ul>'
            self.files[folder/'index.html']=page_layout(folder/'index.html',str(folder),body).encode()
        for dest,src in self.assets.items():
            self.files[dest]=src.read_bytes()
        return self.files

    def search(self,records):
        groups={}
        for source in sorted(self.root.glob('lookup/declarations-*.md')):
            groups.update((a,source.with_suffix('.html').name) for a in re.findall(r'<a id="(decl-[0-9a-f]+)"',source.read_text()))
        catalog=[[r['name'],groups[r['anchor']]+'#'+r['anchor'],list(dict.fromkeys(u['id'] for u in r['units'])),
                  r['file']+f":{r['line0']}–{r['line1']}",r['dominated']] for r in records]
        data=json.dumps(catalog,ensure_ascii=False,separators=(',',':')).replace('<',r'\u003c')
        body=(f'<h1>Search Lean declarations</h1><p class="notice">{NOTICE}</p><label for="query">Declaration name, namespace or unit ID</label>'
              '<input type="search" id="query" class="search-input" placeholder="e.g. Deduction.landau_window" autocomplete="off">'
              '<p id="result-count" role="status" class="search-state" aria-live="polite"></p><ol id="results"></ol>'
              '<p><a href="declarations.html">Browse the alphabetical index</a></p><noscript><p>Open the alphabetical index above to browse without JavaScript.</p></noscript>'
              f'<script type="application/json" id="catalog">{data}</script><script>{SEARCH}</script>')
        return page_layout(Path('lookup/search.html'),'Search Lean declarations',body)


def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=ROOT)
    parser.add_argument('--output',type=Path,help='output directory (default: site/ in the atlas)')
    parser.add_argument('--check',action='store_true',help='compare the source-built files with the local edition')
    args=parser.parse_args()
    root=args.root.resolve()
    output=(args.output or root/'site').resolve()
    if output==root or output in root.parents:
        parser.error('Choose an output directory distinct from the source root and its parents.')
    files=Edition(root, output).build()
    # Only retire files that an earlier run created and whose bytes still match that run.
    manifest_path=output/'build-manifest.json'
    manifest={str(path): hashlib.sha256(data).hexdigest() for path,data in sorted(files.items())}
    previous=json.loads(manifest_path.read_text()) if manifest_path.exists() else {}
    bad=[]
    for former, digest in previous.items():
        if former in manifest:
            continue
        orphan=(output/former).resolve()
        if not orphan.is_relative_to(output) or not orphan.is_file():
            continue
        if args.check or hashlib.sha256(orphan.read_bytes()).hexdigest()!=digest:
            bad.append(former)
        else:
            orphan.unlink()
    files[Path('build-manifest.json')]=(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n').encode()
    for path, data in files.items():
        target=output/path
        if args.check:
            if not target.is_file() or target.read_bytes()!=data:
                bad.append(path)
        else:
            target.parent.mkdir(parents=True,exist_ok=True)
            if not target.is_file() or target.read_bytes()!=data:
                target.write_bytes(data)
    if args.check:
        from validate_site import validate as validate_site
        counts, errors = validate_site(root, output)
        print(f'{len(files)} expected output files checked; {len(bad)} stale or missing.')
        print(f'Checked {counts["local"]:,} local links including {counts["fragments"]:,} fragments, '
              f'and {counts["external"]:,} registered external URLs.')
        if bad or errors:
            print('\n'.join(str(p) for p in [*bad, *errors][:20]),file=sys.stderr)
        return bool(bad or errors)
    if bad:
        print('Preserved modified files from an older build: '+', '.join(map(str,bad[:20])),file=sys.stderr)
        return True
    print(f'Built {sum(p.suffix==".html" for p in files)} HTML pages and {len(files)} total files in {output}.')
    return False


if __name__=='__main__':
    sys.exit(main())
