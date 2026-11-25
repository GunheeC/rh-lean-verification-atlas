# How to read the counts

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

The [progress page](../PROGRESS.md) begins with units and steps. A Full note gives the argument under its stated inputs. An Outlined note sketches all or part of a derivation. A Statement only card identifies the proposition. Each primary field counts its own units.

## What a source citation records

A cited line locates a written step in the pinned Lean source and by itself establishes neither a line-by-line check nor a complete proof. The counter rebuilds each step’s edition digest from its note, statement, claims, input names and inclusive source ranges. It combines ranges within each file and counts each physical line once per category. A line can occur in both a Full and an Outlined note, or in more than one field.

The full-source column divides distinct citations by the number of newline characters in all Lean files under `lean/src/` in the pinned archive. Every nonempty source file ends with a newline. The core column uses the graph rooted at `allChi`. A core line contributes one unit of source-span weight for a reachable core declaration. A literature node is a declaration marked by the extraction’s name or module boundary, where traversal stops without inspecting its proof. The positive core spans in this extraction are disjoint. The optional smaller column counts only physical lines in the original fixed sample of 855 files, including comments and blanks. [Source file inventory](source_inventory.json)

The step-specific AI row requires a verdict on the exact step and edition. The prose-review row counts ranges cited by steps in a note whose exact text has a whole-note review. A human-checked line needs a current positive verdict on the active step that cites it. A superseded record, or a step with an unresolved dispute, gives no credit from that step. These unions may overlap when another step cites the same line. [Current human evidence rules](../signoffs/README.md)

## Position in the index

Each line belongs to the nearest registered unit statement at or above its declaration in the `allChi` dominator tree. This locates the line in the index and establishes neither explanation nor reading. Including only statement heads excludes sources used merely as contextual pointers. For a head shared by several primary units, the earliest unit ID in character order owns its position. This rule does not consult status or grade. Subtract each nearest descendant head’s full weight from its parent’s weight. The remaining weights partition the root and are added by owner status. The Full-and-L2 row is a subset of Full. [All owners, ties and assigned weights](index_position.json) · [Pinned dominator tree](dominators.json)

## Unit and step evidence

1. Pinned means every registered declaration has a matching source-span hash.
2. Compared means an AI or a signatory compared the current statement transcription with its Lean statement. The record identifies the target declaration and edition.
3. Written includes both Full arguments and outlines.
4. With steps means at least one current checkpoint is bound to the note.
5. AI review counts an edition-matched review of the current argument or positive coverage of every active step by an AI review. Outline-fidelity findings stay outline findings. A review of the enclosing prose supplies no individual step verdict.
6. A complete human check follows the Full-unit rule on the sign-off page. Partial findings and disputes appear on the unit checklist. [Reader evidence](../signoffs/README.md)

## Editions and reproducibility

[History](history.jsonl) preserves dated counter snapshots. They have content hashes independent of Git history. The first three editorial editions contained prose but had no step checklists. Their zero cited lines mean there were no recorded step citations at the time. The early rows were recomputed from their archived evidence before public release. Those archives are not part of the release. The current edition can be checked entirely from this checkout.

Run `python scripts/snapshot.py --check` to verify the latest counts, historical row identities and generated pages. For a future edition, run `python scripts/snapshot.py --append --round "Edition label"` after updating the evidence. An explicit `--date YYYY-MM-DD` supplies the edition’s UTC date. This command records the new snapshot and renders its pages. [Formal procedures and the graph](../notes/formal/procedures.md)

To reproduce the physical census using the separately obtained pinned source archive, run `python scripts/source_inventory.py --source-archive LEAN_TAR_GZ --graph-cache GRAPH_CACHE_BIN`. The optional `--lean-src LEAN_SRC` also compares the complete bytes of the indexed and cited files to your checkout. The source archive, the graph and the published list of included files are authenticated by their digests.

## Rebuild the optional traversal graph

The atlas records the expected graph fingerprint, dimensions and 1,003 named node IDs. Its normal offline validation checks this public index. Repeating a graph deletion also requires the dependency edges, which you can reconstruct separately. [Expected graph identity](position_graph.json)

Start with a separate copy of source revision `40e56bab026552e089d7afcfeff08d2defb9c005` and the matching project's compiled objects. The Lean source directory is `src/` inside that checkout. Lean 4.33.1 reads elaborated dependencies from the project’s `.olean` files. The Python 3.11+ packer gets inclusive source ranges from their companion `.ilean` files. A checkout containing only `.lean` files needs the matching build outputs first. The pinned public object archive and its verification commands are in section 2 of the formal procedures. This graph calculation requires no Mathlib package objects or new project build when using that archive. Allow about 99 GB for the unpacked object archive and 15 GB of temporary space for the trace. [Source and object archive instructions](../notes/formal/procedures.md)

Run the following in the atlas directory after setting `LEAN_SRC` to the separate checkout’s `src/` and `PROJECT_OBJECTS` to the directory containing the project’s `Main.olean` and `Main.ilean`. For the object archive extracted as in the formal procedures, set `PROJECT_OBJECTS="$OLEAN_DIR/extract/.lake/build/lib/lean"`. The output directory must be outside both checkouts.

```sh
GRAPH_WORK=$(mktemp -d)
python3 scripts/pack_position_graph.py --checkout "$(dirname "$LEAN_SRC")" \
  --objects "$PROJECT_OBJECTS" --output "$GRAPH_WORK/position_graph.xz"
python3 scripts/check_graph_position.py --graph "$GRAPH_WORK/position_graph.xz" \
  UpperTheory.FinalTheorems.everyCharacter_of_row
```

The packer checks 855 source-file digests against the inventory. The extractor indexes project constants, starts at `allChi`, and follows constants used in types, values and inductive constructors. Literature nodes retain only type dependencies in the intermediate trace and become terminal in the packed graph. Dependencies outside the project end the walk. Core declarations with a recorded compiler source span receive its inclusive line count. Each output node stores its weight and sorted unique successor IDs. The fingerprint must equal `d28c467b46f5039ae24bb26072bfa49c61bc0a0e6b54ca951df668ddc33371f8` before the packer installs the local output file. For P011 the expected root weight is 9,567,045, the surviving weight 2,137,853 and the difference 7,429,192. [Lean extractor](../scripts/trace_position_graph.lean) · [Packer](../scripts/pack_position_graph.py) · [Deletion and traversal](../scripts/check_graph_position.py)

To retain the intermediate trace for repeated runs, invoke the extractor directly in the pinned project with Lean 4.33.1. Its positional arguments are the project object directory and an empty output directory. Add `--trace-dir TRACE_DIRECTORY` to the packer command above to read the complete `decls.jsonl` and `edges.jsonl` from that extraction. This mode still reads the compiler’s original source ranges and verifies the same final graph fingerprint.
