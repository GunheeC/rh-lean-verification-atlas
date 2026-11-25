# Formalization and reproducibility

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

The written deduction assumes [V](../../pillars/V.md), [F](../../pillars/F.md), Green’s finite-field character input, 31 local implications and the intermediate results listed in paper v7. No complete human-readable proof of V or F exists in this atlas. The Lean source supplies both with in-repository terms. No human has checked this material.

Standard background includes proof terms, axioms and directed graph dominators. On this route “core line”, “literature node” and “reading unit” denote Lean identifiers or terminology introduced by these drafts. Read them with the linked project definitions. [Glossary](../../lookup/glossary.md)

Gunhee Cho is the paper’s author and the blueprint’s editor. Both were drafted with AI assistance. No independent human referee has checked the arguments. Levent Alpöge is the author of the Lean development. The repository includes both PDFs. The edition register preserves the earlier sources used in reviews. [Blueprint v13b · printed pp. 1–7](../../editions/v0.1.0/blueprint_v13b.pdf#page=37) · [Conditional paper v7](../../editions/v0.1.0/paper_v7.pdf) · [Edition register](../../data/editions.json)

[Starter packet](../../notes/formal/README.md) · [Open questions](../../questions/formal.md) · [Unit inventory](units.md) · [Korean](../../docs/ko/formal.md)

## Start here

**A public declaration, its source bytes and the audit record.** Blueprint v13, printed pp. 1–7 (7 pages). Locate P001 and reproduce its normalized source-span hash. Compare the public statement with the scope of the dated audit. This exercise does not rerun a kernel. [Read the packet](../../notes/formal/README.md)

**Starter prerequisites.** Directory navigation, SHA-256, and the distinction between the type of a Lean declaration, its dependencies, and a compiled object. No mathematical background beyond the statement being inspected is required. [P001](../../units/P001.md)

[Run the three local checks: source hash, axiom list and dominated lines](../../notes/formal/procedures.md)

## Where this field enters

The five exports in `Main.lean:4–12` have no external hypothesis argument. The written implication in [V4-COND](../../units/V4-COND.md) retains its premises. From the `allChi` root, [P010](../../units/P010.md) dominates 9,567,042 core lines and [P011](../../units/P011.md) dominates 7,429,192; the latter region lies inside the former. [Counting procedure](../../notes/formal/procedures.md)

Start by pinning what is being compared. The five public declarations differ in their domains, primitive-character conditions and treatment of the principal character. A shared name or a matching summary is insufficient to identify a theorem. The unit pages give the exact declaration, source range and hash rule.

Next choose a graph question. Inclusive weight counts the reachable core below a declaration. Dominated weight counts the core that becomes unreachable from the root if the declaration is removed. A shared supplier can belong to several inclusive cones. Types and proof values can also lead to different edges. Finally keep the evidence layers separate. Object-file integrity, kernel acceptance, the translation of a statement and an independent reading of a written proof answer different questions. Their dates and scopes are recorded individually.

## Reading path

Follow these units in order. Each card identifies the assumptions, the Lean declaration and the available exposition.

### First reading

1. [P001](../../units/P001.md) · Read the exact zeta declaration.
2. [P003](../../units/P003.md) · Locate the principal character exception.
3. [P005](../../units/P005.md) · State the primitive-character target.
4. [P009](../../units/P009.md) · Locate the assertion over all characters.

### Core argument

1. [P010](../../units/P010.md) · Follow the upper declaration to its suppliers.
2. [P011](../../units/P011.md) · Track the row used in the upper argument.
3. [P012](../../units/P012.md) · Check reuse of a common input.

### Open inputs and scope

1. [T02](../../units/T02.md) · Distinguish a common witness from separately supplied fields.
2. [P013](../../units/P013.md) · Separate the checked assembly from the inputs it consumes.

## Literature and the scope of the comparison

The source commit for the Lean development and the dated MIT verification snapshot are separate primary records. The checker verdicts refer to specific files and runs. [Source register](../../sources/README.md) · [Dated status](../../STATUS.md) · [R19](../../reviews/R19_review.md) · [R23](../../reviews/R23_review.md)

## Questions for a specialist

What bytes are hashed for a declaration, the full archive and the compiled object? Reproduce one digest with its stated convention. [All three questions and units to check](../../questions/formal.md)
