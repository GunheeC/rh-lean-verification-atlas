# Arakelov geometry and geometry of numbers

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

The written deduction assumes [V](../../pillars/V.md), [F](../../pillars/F.md), Green’s finite-field character input, 31 local implications and the intermediate results listed in paper v7. No complete human-readable proof of V or F exists in this atlas. The Lean source supplies both with in-repository terms. No human has checked this material.

Standard background includes metrized line bundles, covolumes and arithmetic intersection numbers. On this route “selected bundles” and “definite-side witness” denote Lean identifiers or terminology introduced by these drafts. Read them with the linked project definitions. [Glossary](../../lookup/glossary.md)

Gunhee Cho is the paper’s author and the blueprint’s editor. Both were drafted with AI assistance. No independent human referee has checked the arguments. Levent Alpöge is the author of the Lean development. The repository includes both PDFs. The edition register preserves the earlier sources used in reviews. [Blueprint v13b · printed pp. 173–178](../../editions/v0.1.0/blueprint_v13b.pdf#page=209) · [Conditional paper v7](../../editions/v0.1.0/paper_v7.pdf) · [Edition register](../../data/editions.json)

[Starter packet](../../notes/arakelov/README.md) · [Open questions](../../questions/arakelov.md) · [Unit inventory](units.md) · [Korean](../../docs/ko/arakelov.md)

## Start here

**Gram determinants and the evaluation dual.** Blueprint v13, printed pp. 173–178 (6 pages). Follow Lemmas 8.13–8.15 with a full-rank basis in its span and invertible frames. Recompute the determinant factor after changing basis. [Read the packet](../../notes/arakelov/README.md)

**Starter prerequisites.** Linear algebra over a number field, its real Minkowski embedding, covolumes of lattices and the trace pairing. [P049](../../units/P049.md) · [Z5.1](../../units/Z5.1.md)

## Where this field enters

The finite-place calculation measures lattice index. The archimedean calculation measures volume in a metric. In Z5.1 and P049 a complex change of basis contributes the square of an absolute determinant to the Gram determinant. Keep the places and the base field fixed while comparing the two expressions. Z5.2 then introduces the evaluation dual.

At the family level P021 bounds a lattice request by a main term and an error at one unit. To use it on varying members, record the order in which the uniform constant, the stage and the lattice are chosen. T13–T18 treat the geometric supply of covolume and height bounds. The published asymptotic counts small sections of one nef metrized line bundle. In T14–T15, locate an error bound common to all members of the varying tower.

## Reading path

Follow these units in order. Each card identifies the assumptions, the Lean declaration and the available exposition.

### First reading

1. [Z5.1](../../units/Z5.1.md) · Compare the Gram determinant with additive index.
2. [Z5.2](../../units/Z5.2.md) · Track height under evaluation duality.
3. [P050](../../units/P050.md) · Fix the local realizations of the lattice.
4. [P049](../../units/P049.md) · Apply the determinant formula in its span.

### Core argument

1. [P021](../../units/P021.md) · Read the bound at one lattice unit.
2. [T17](../../units/T17.md) · Read the small-section volume estimate.
3. [T15](../../units/T15.md) · Identify its use in the uniform covolume bound.

### Open inputs and scope

1. [T13](../../units/T13.md) · Trace the covolume hypotheses to their suppliers.
2. [T14](../../units/T14.md) · Check the constants over deep components.

## Literature and the scope of the comparison

An AI review (R21) reports comparing the introduction to Moriwaki’s *Continuity of volumes on arithmetic varieties*. The cited locator, Theorem A and §5, is not verified here. The report did not establish the proof or uniformity over the specific tower in T17–T18. [R21](../../reviews/R21_review.md)

## Questions for a specialist

Which discriminant, square and place weights appear before and after dualizing? Recover both sides after changing the basis. [All three questions and units to check](../../questions/arakelov.md)

## The two open inputs

[V · uniform Selmer window](../../pillars/V.md) · [F · compatible definite-side witness](../../pillars/F.md)
