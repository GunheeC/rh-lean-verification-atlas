# Three checks on a pinned Lean export

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**pending_review** · The examples use Python 3.11 or later. The axiom query and graph extraction also use Lean 4.33.1. Start in the atlas checkout. For the source-slice check, use a separate checkout of the public Lean source. The following shell commands acquire its pinned revision and create a temporary working directory. The third check uses this checkout and its separately obtained compiled objects. [Unit P001](../../units/P001.md) · [Pin ledger](../../data/pins.json)

```sh
WORK_DIR=$(mktemp -d)
git clone --no-checkout https://github.com/leanprover-community/riemann-hypothesis "$WORK_DIR/source"
git -C "$WORK_DIR/source" checkout --detach 40e56bab026552e089d7afcfeff08d2defb9c005
export LEAN_SRC="$WORK_DIR/source/src"
```

## 1. Extract a declaration and check its hash

Look up the qualified name, source file and inclusive line range in the pin ledger. For the public zeta export the source is `Main.lean:4–4` at commit `40e56bab026552e089d7afcfeff08d2defb9c005`. Python indexes the first line as zero. Slice from `line0 - 1` up to the exclusive Python endpoint `line1`. Joining with LF puts one newline *between* neighboring source lines and none at the end. Run the following command in the atlas directory.

```sh
python3 - <<'PY'
import hashlib, json, os
from pathlib import Path
pin = json.loads(Path('data/pins.json').read_text())['anchors']['riemannHypothesis']
source = Path(os.environ['LEAN_SRC']) / pin['file']
lines = source.read_text(encoding='utf-8').splitlines()
span = '\n'.join(lines[pin['line0'] - 1 : pin['line1']])
digest = hashlib.sha256(span.encode('utf-8')).hexdigest()
assert digest == pin['sha256']
print(span, digest, sep='\n')
PY
```

The command printed the declaration and `71b3d50605ddda7c0c74fbbf5cca47165a4cfa2ad72f50f36b907ecac7ff505a`. A terminal newline in this one-line input would yield a different digest. The result identifies the exact source slice. Its mathematical deduction uses the modulus-one character and the zeta functional equation. [Read the deduction](../units/P001_round3.md)

## 2. Ask which axioms an export uses

The compiled-object reader below requires the public object archive. Its manifest and archive are available at the pinned dataset revision shown below. The archive is 28,638,044,751 bytes; allow about 99 GB for the extracted tree. The manifest and the named object are checked separately below. The full `#print axioms` query also needs the compiled packages pinned in the source checkout’s `lake-manifest.json`. Use an independently prepared checkout with those packages or populate its standard dependency cache in the temporary checkout. Python and Lean’s core libraries suffice for the object-reader alternative.

```sh
export OLEAN_DIR="$WORK_DIR/objects"
export LEAN_PACKAGES="$WORK_DIR/source/.lake/packages"
mkdir -p "$OLEAN_DIR/extract"
BASE=https://huggingface.co/datasets/JackMcCarthy/riemann-hypothesis-build/resolve/9036e64326acf4acfae159b96664e9708445c1d1
curl -fL "$BASE/olean-manifest.sha256" -o "$OLEAN_DIR/olean-manifest.sha256"
curl -fL "$BASE/oleans.tar.zst" -o "$OLEAN_DIR/oleans.tar.zst"
python3 - <<'PYCODE'
import hashlib, os
from pathlib import Path
with (Path(os.environ['OLEAN_DIR']) / 'oleans.tar.zst').open('rb') as f:
    assert hashlib.file_digest(f, 'sha256').hexdigest() == '953bab5386a7849527a11960f80a2fab427c49c637d6e94cc75788dd8f40196b'
PYCODE
zstd -dc "$OLEAN_DIR/oleans.tar.zst" | tar -xf - -C "$OLEAN_DIR/extract"
(cd "$WORK_DIR/source" && lake exe cache get)
```

The ordinary command is `#print axioms <qualified-name>` after importing the module. The launcher below sets the search path to the existing published and package objects, then sends two lines to Lean. For an export directly used in the public zeta reduction, run

```sh
python3 scripts/round3_print_axioms.py Formalism.GammaFactorNonvanishing.RhOfRight Formalism.VW.rh_of_right --objects "$OLEAN_DIR/extract/.lake/build/lib/lean" --packages "$LEAN_PACKAGES"
```

This imports `Formalism.GammaFactorNonvanishing.RhOfRight` and executes `#print axioms Formalism.VW.rh_of_right`. The observed output was `'Formalism.VW.rh_of_right' depends on axioms: [propext, Classical.choice, Quot.sound]`. That theorem is the reflection implication with a right-half-plane premise. The public export `riemannHypothesis` lies in `Main` and is a different declaration. The equivalent command for the full public module is

```sh
python3 scripts/round3_print_axioms.py Main riemannHypothesis riemannZeta_eq_zero_re LFunction_ne_zero_of_half_lt_re LFunction_eq_zero_re LFunction_eq_zero_re_of_isPrimitive --objects "$OLEAN_DIR/extract/.lake/build/lib/lean" --packages "$LEAN_PACKAGES"
```

On 25 November 2026 we ran this `import Main` and all five `#print axioms` commands with Lean 4.33.1. The process exited successfully. For each of the five names Lean reported `propext`, `Classical.choice` and `Quot.sound`. This imports the compiled environment and queries its axiom collector. It uses the existing module objects and performs no source rebuild.

Lean 4.33.1 stores the axiom set computed for an exported declaration in its module object. The following checks identify the manifest and `Main.olean` before reading the five named entries. This is a smaller local procedure for the public targets when importing the whole development is impractical.

```sh
python3 - <<'PY'
import os
from hashlib import file_digest, sha256
from pathlib import Path
manifest = Path(os.environ['OLEAN_DIR']) / 'olean-manifest.sha256'
with manifest.open('rb') as handle:
    assert file_digest(handle, 'sha256').hexdigest() == 'fb3609ad73a17102e6e3e2346c5358a9c0957bcf5945442a7e5ffaa00c441ff5'
relative = '.lake/build/lib/lean/Main.olean'
matches = [line.split()[0] for line in manifest.read_text().splitlines() if line.endswith('  ' + relative)]
obj = Path(os.environ['OLEAN_DIR']) / 'extract' / relative
assert matches == [sha256(obj.read_bytes()).hexdigest()]
print(matches[0])
PY
lean +leanprover/lean4:v4.33.1 --run scripts/round3_axiom_entries.lean "$OLEAN_DIR/extract/.lake/build/lib/lean/Main.olean"
```

The first command printed `ce9a2006adda570c7404866ff3ceb4a7341c6c5d8ae7b56b6d8600b4c312d1ab`. The second returned entries for all five public names listed above. Each entry contained `propext`, `Classical.choice` and `Quot.sound`. The reader selects the `exportedAxiomsExt` entry array. In this toolchain the serialization is defined at `Lean/Util/CollectAxioms.lean:120–146`, and the lookup at lines 149–153. The native print command calls the collector at `Lean/Elab/Print.lean:240–251`. This checks the metadata carried by the specified compiled object. Rechecking proof terms in a kernel is a different operation documented under the dated external audit. [Lean launcher](../../scripts/round3_print_axioms.py) · [Object reader](../../scripts/round3_axiom_entries.lean) · [Kernel audit](../../sources/kernel-audit.md)

## 3. Recompute dominated lines for one node

In the graph rooted at `allChi`, a declaration $v$ dominates a reached declaration $w$ if *every* directed path from the root to $w$ contains $v$. Delete $v$, traverse again and subtract the surviving weight. A supplier with an alternative path survives, even if it lies below $v$ in the original traversal.

For a concrete example take the row-to-half-plane declaration in [P011](../../units/P011.md). The atlas records the fingerprint and declaration-name index in `progress/position_graph.json`. Follow the [graph regeneration procedure](../../progress/README.md#rebuild-the-optional-traversal-graph) to reconstruct the traversal arrays outside the atlas. The deletion program verifies the resulting bytes before traversing. The arrays retain every vertex, its weight and every distinct outgoing dependency, except that nodes tagged `lit` have no outgoing edges. This stopping convention defines its literature frontier. The tag says where traversal stops; it establishes no equivalence with a published result. Each reachable core declaration with a valid source span contributes its inclusive line count exactly once. This choice counts overlapping spans of different declarations independently.

```sh
python3 scripts/check_graph_position.py --graph "$GRAPH_WORK/position_graph.xz" UpperTheory.FinalTheorems.everyCharacter_of_row
```

The command printed

```text
root: 9567045
without UpperTheory.FinalTheorems.everyCharacter_of_row: 2137853
dominated: 7429192
```

The subtraction agrees with the P011 pin. To replay a different target, pass one of the declaration names listed in the graph’s JSON name index. The reconstructed arrays omit duplicate edges and retain all vertex weights. The [packer](../../scripts/pack_position_graph.py) checks their fingerprint against the published index. The graph includes dependencies arising in types, values and constructor data. Its weight describes reachability for this root and this frontier. A high weight can belong to a two-line theorem that gathers many suppliers. Adding parent and child weights double-counts their shared dominated region. The separate `five_public_heads` weights for the public exports use a different root convention. [Traversal implementation](../../scripts/check_graph_position.py) · [P011 deduction](../units/P011_round3.md)
