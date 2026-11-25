"""Extract local reading packets from the released v13 blueprint, preserving page witnesses."""
import argparse, hashlib, json, re, subprocess, tempfile
from pathlib import Path
from PIL import Image

BANNER="AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved"
RELEASE_HASH="d9dcb73f10a5829865f9246409d886c16cb1d2087717adf7758f154257a28af4"
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def label(x): return re.sub(r'(?<!^)([A-Z])', r' \1', x)
# Each span below has its two original printed boundary pages included. Facsimiles
# may show adjoining text on a shared boundary page; source excerpts stop exactly.
spec={
'analytic':('One-sided power windows and simple poles','P022','Deduction.landau_window',(7,14),'§§2.2–2.3',[('ch_E',237,738)],
'Complex analysis through residues, holomorphic power series, Mellin/Laplace transforms, and elementary bounds for the von Mangoldt function.',
'Follow the abstract Landau implication for given pole data and a moving upper window. Identify where positivity at a real pole is needed and why the analytic radius forces a contradiction.',
'Start at the definitions of PoleData and WindowHypU. Follow the Taylor coefficient inequality, the real/nonreal pole alternatives and the nearest-pole argument. Only then pass to the positive character family.',
'The local theorem assumes exactly the displayed pole and window hypotheses. The chapter derives the contradiction under them. The arithmetic supply of such windows, the explicit formula for an actual family, and global zero-freeness are separate tasks.'),
'arakelov':('A Gram determinant in a complex frame','P049','Formalism.HN.htGram_of',(173,178),'§§8.2.1–8.2.4',[('ch_P',1984,2417)],
'Linear algebra over a number field, its real Minkowski embedding, covolumes of lattices and the trace pairing.',
'Calculate the covolume of a lattice with a chosen basis in its span. Identify the discriminant factor, the square of the complex determinant and the normalization that gives a height.',
'Compare the two notions of dual in §8.2.1. In §8.2.2 track the determinant of the realification, then compare the archimedean product with the trace dual. §§8.2.3–4 explain what changes when the chart varies.',
'The fixed-frame calculation has an explicit full-rank basis in its span and invertible frames. These are the data of the theorem. The downstream bound for the actual family of rows needs the indicated project comparison records.'),
'theta':('Testing the two integral Weyl lattices by Fock duality','Z4.4','GlobalTheory.T.standard_weyl_lattices_fock_dual',(473,478),'§8.21.3',[('ch_P_r12',224,585)],
'Integral lattices, polynomials, partitions and tableaux, factorial pairings and change of basis over a number field with involution.',
'Check the two integrality tests for a vector in the specified Weyl space at the identity Gram matrix. The membership in that space is essential to the coefficient test.',
'Begin with the normalized pairing and the two standard lattices. Follow how tests on Weyl words recover coefficients, then trace the triangular straightening and passage to integral coefficients. Finish with the limits of the transport argument.',
'The standard-lattice test is a local result with the normalized pairing, fixed dominant weights and a vector in the specified Weyl space. The surrounding Z4.4 theorem also needs a common site, transported lattices and period suppliers. The packet does not certify all of Z4.4.'),
'galois':('Recovering a full Selmer length from two eigenspaces','P020','UpperTheory.V.vvle_of_parts',(76,81),'§§5.1–5.3',[('ch_S',50,392)],
'Finite-length modules over a discrete valuation ring, involutions and their projectors. Cohomology is needed to recognize the localization kernel in the application.',
'For odd primes, recover the two summands with the signs prescribed by the twist; account for the single factor log 2 when recombining the prime budgets.',
'Read the finite-prime-set window statement, then the general involution lemma, the plus/minus convention and the weighted sum. The next section identifies the separate two-adic and tower inputs.',
'For the splitting argument the operator squares to the identity, the submodule is stable under it, and 2 is a unit. For the sum, finite bounds on the two parts and the two-adic part are explicit inputs. The packet does not derive a VWin or a uniform tower estimate.'),
'local':('An elementary bound inside the inert-prime gain','P045','Formalism.BasicNotions.factLpF',(58,64),'§§4.1–4.3',[('ch_G',25,359)],
'Finite cyclic groups, finite sums, a supremum and the elementary notion of a valuation. Knowledge of formal groups is useful for the final application only.',
'Verify the upper and lower bounds for the linear-programming defect lpF for a nonzero cycle length d, an integer parameter ℓ ≥ 2 and nonnegative row sizes Dₛ.',
'Start with the orbit and column sizes, then isolate the feasible arrays of §4.2. Check the cyclic reindexing and the contribution of each allowed odd index. Read §4.3 for the local formal group in which the loss occurs.',
'The finite-array inequality is closed under the displayed numerical data. The application to weighted jets (P045) also needs the integral formal-group comparison and the local projection and rank conditions described on p. 64. This packet supplies background for P045 rather than a proof of its full statement.'),
'ktheory':('Finite divisor counts and the loss in the exponent','P036','UpperTheory.V.ZK.sCount',(149,155),'§§8.1.2–8.1.4',[('ch_P',178,649)],
'Finite abelian groups and their primary parts, valuations, units and ideal classes. The Selmer application also uses cohomology and congruence-group homology.',
'Track the finite-subset count after evaluation separates the characters. Locate the class-number term, the exponent loss, and both consecutive homological torsion orders.',
'Read separation by evaluations in §8.1.2, identify the integral-cycle input in §8.1.3 and track the quotient of the divisor group in §8.1.4. Check why a bound for every finite subset bounds the cardinality of the image.',
'The final finite-subset implication is elementary with a stated finite cap. The arithmetic estimate for that cap uses the explicitly named separation and integral-cycle/homology statements. Those inputs are not closed by this excerpt; LemmaK and its global Selmer bound need more.'),
'formal':('Audit one export and distinguish three verification questions','P001','riemannHypothesis',(1,7),'Ch. 1 and §2.1',[('ch_O',1,133),('ch_E',1,236)],
'Directory navigation, SHA-256, and the distinction between the type of a Lean declaration, its dependencies, and a compiled object. No mathematical background beyond the statement being inspected is required.',
'Check the name and normalized range hash of one public export, then compare the exact scope of its statement with the dated evidence for replay and comparison.',
'Read the chapter overview and the five declarations. Trace P001 to its single source line and use the local check below. Compare the recorded results for dependencies and proof exports with the source claim you have actually checked.',
'The byte comparison is fully repeatable from the fixed source checkout. A kernel replay and an independent mathematical proof are outside this exercise. The blueprint describes prior replay results, not a replay performed by the atlas.')
}
# A supporting declaration can be a standalone reading target without matching the
# root of its contextual atlas unit. Multiple units can also share a formal head.
roles = {
    'analytic': ('exact head', 'P022 states the window lemma. P023 applies it to a positive character family.', ['P023']),
    'arakelov': ('supporting declaration', 'The fixed-frame Gram calculation is a tool in the height identity headed by Formalism.HN.height_gram_determinant (P049 and Z5.1).', ['Z5.1']),
    'theta': ('supporting declaration', 'The standard-lattice theorem is one named input to the larger twisted-period argument in Z4.4.', []),
    'galois': ('supporting declaration', 'Proposition 5.10 recombines the two sign parts. P020 packages the five counting inputs and the window statement.', []),
    'local': ('supporting declaration', 'Lemma 4.6 bounds the finite-array loss that appears in the inert-place estimate. P045 is the formal-group bound for weighted jets.', []),
    'ktheory': ('exact head', 'P036 and Z2.K5 share the formal head sCount. The elementary last step assumes the numerical cap derived from the arithmetic inputs.', ['Z2.K5']),
    'formal': ('exact head', 'P001 is the public export inspected in this byte audit.', []),
}
def public_excerpt(chunk):
    """Use a portable source-root label in the published formal packet."""
    chunk = re.sub(rb"(?<=Revision checked against the original )[\w.-]+/lean/src(?= tree)", b"pinned Lean source", chunk)
    return re.sub(rb"(?<=Paths begin at )\\nolinkurl\{[^}]+/lean/src/\}", lambda _: br"\texttt{LEAN\_SRC}", chunk)


def build(args):
    atlas=Path(args.atlas).resolve(); bundle=Path(args.edition_sources); pdf=Path(args.pdf)
    if sha(pdf)!=RELEASE_HASH:raise ValueError('wrong blueprint v13 PDF')
    ship={int(k):int(v) for k,v in re.findall(r'\\BPshipout\{(\d+)\}\{(\d+)\}',Path(args.aux).read_text())}
    output={}
    with tempfile.TemporaryDirectory() as tmp:
        scratch=Path(tmp); executable=scratch/'pages'
        if not args.reuse_pages: subprocess.run(['swiftc','-module-cache-path',str(scratch/'module-cache'),str(atlas/'scripts/extract_pages.swift'),'-o',str(executable)],check=True)
        for track,(title,unit,decl,(start,end),section,ranges,bg,goal,order,limit) in spec.items():
            dest=atlas/'notes'/track; pages=dest/'pages';pages.mkdir(parents=True,exist_ok=True)
            physical=[ship[n] for n in range(start,end+1)]
            if not args.reuse_pages: subprocess.run([str(executable),str(pdf),str(scratch),*map(str,physical)],check=True)
            description = ("Sections of blueprint v13 with local source-root references normalized. Selected-source hashes identify the original fragments."
                           if track == "formal" else "Verbatim sections of local blueprint v13. See README.md for macros, edition and source spans.")
            orig=[]; out=[f'% {BANNER}\n% {description}\n'.encode()]
            for name,i,j in ranges:
                f=bundle/(name+'.tex'); source=f.read_bytes().splitlines(keepends=True)
                if len(source)<j: raise ValueError(f'Short source {f}')
                b=b''.join(source[i-1:j])
                exported = public_excerpt(b) if track == "formal" else b
                out.extend([f'\n% blueprint/{f.name}:{i}-{j}\n'.encode(), exported])
                orig.append({'file':f'blueprint/{f.name}','line0':i,'line1':j,'file_sha256':sha(f),'excerpt_sha256':hashlib.sha256(b).hexdigest()})
            (dest/'excerpt.tex').write_bytes(b''.join(out))
            hashes={}
            for n,k in enumerate(physical,start):
                f=pages/f'{n}.webp'
                if args.reuse_pages:
                    old = json.loads((atlas/'data/notes_starters.json').read_text())['starters'][track]
                    if sha(f) != old['page_image_hashes'][str(n)]:raise ValueError(f'Changed cached page: {f}')
                else:
                    with Image.open(scratch/f'p{k}.png') as im: im.convert('RGB').save(f,lossless=True,method=4)
                hashes[str(n)]=sha(f)
            role, relation, companions = roles[track]
            companion_links = ' · '.join(f'[{k}](../../units/{k}.md)' for k in companions)
            unit_note = f'[{unit}](../../units/{unit}.md)' + (' · '+companion_links if companions else '')
            s=[BANNER,'',f'# {title}','',f'**Starter for the {track} track.** Atlas units {unit_note}. The local reading target is `{decl}` ({role}). {relation}','',f'**Background.** {bg}','',f'**Reading target.** {goal}','',f'**Reading order.** {order}','',f'**Scope and prerequisites.** {limit}','',f'**Edition.** Blueprint v13, {section}, printed pp. {start}–{end} ({len(physical)} actual pages; PDF pages {physical[0]}–{physical[-1]}). The page images preserve the typeset formulas. On a shared boundary page, adjoining material may be visible; the TeX selection below marks the exact span.','', '[Original local TeX excerpt](excerpt.tex) · [Edition register](../../data/editions.json)','',f'Original PDF SHA-256 `{RELEASE_HASH}`.','']
            pin = json.loads((atlas/'data/pins.json').read_text())['anchors'][decl]
            s.extend([f"**Pinned Lean source.** `{pin['file']}:{pin['line0']}–{pin['line1']}`, range SHA-256 `{pin['sha256']}`. The [pin register](../../data/pins.json) records the graph and dominated line count.", ''])
            for record in orig:s.append(f"- `{record['file']}:{record['line0']}–{record['line1']}`, selected source bytes SHA-256 `{record['excerpt_sha256']}`.")
            if track=='formal':
                s = [line.replace('[Original local TeX excerpt](excerpt.tex)', '[TeX excerpt with portable source-root references](excerpt.tex)') for line in s]
                s += ['', 'The selected-source fingerprints above identify the original manuscript fragments. The distributed TeX uses `LEAN_SRC` for the local source root.']
                s+=['','### Repeat the local export check','','From the atlas root, with `LEAN_SRC` set as in the [procedures](procedures.md), run this read-only check. The hash excludes a final newline, matching the atlas range convention.','', '''```python
import hashlib, json, os
from pathlib import Path

entry = json.loads(Path("data/pins.json").read_text())["anchors"]["riemannHypothesis"]
source = Path(os.environ["LEAN_SRC"]) / entry["file"]
lines = source.read_text().splitlines()[entry["line0"] - 1:entry["line1"]]
assert hashlib.sha256("\\n".join(lines).encode()).hexdigest() == entry["sha256"]
print(entry["file"], entry["line0"], entry["line1"], *lines, sep="\\n")
```''']
            s+=['','## Typeset pages','']
            for n in range(start,end+1): s.extend([f'![Blueprint v13, printed page {n}](pages/{n}.webp)',''])
            (dest/'README.md').write_text('\n'.join(s)+'\n')
            output[track]=dict(title=title,unit_id=unit,lean_decl=decl,path=f'notes/{track}/README.md',tex=f'notes/{track}/excerpt.tex',edition='blueprint_v13',printed_pages=list(range(start,end+1)),pdf_pages=physical,size_pages=len(physical),section=section,source_ranges=orig,page_image_hashes=hashes,scope=limit,prerequisites=bg,unit_relation=role,relation_detail=relation,companions=companions,checkable_target=goal,lean_pin=pin)
            if track == "formal":
                output[track]["public_excerpt_sha256"] = sha(dest / "excerpt.tex")
    (atlas/'data/notes_starters.json').write_text(json.dumps({'notice':BANNER,'starters':output},ensure_ascii=False,indent=2)+'\n')
if __name__=='__main__':
    p=argparse.ArgumentParser()
    for key in ['atlas','edition-sources','pdf','aux']:p.add_argument('--'+key,required=True)
    p.add_argument('--reuse-pages',action='store_true',help='Verify existing facsimile hashes instead of rasterizing the same edition again.')
    build(p.parse_args())
