# Local p-adic theory

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

The written deduction assumes [V](../../pillars/V.md), [F](../../pillars/F.md), Green’s finite-field character input, 31 local implications and the intermediate results listed in paper v5. No complete human-readable proof of V or F exists in this atlas. The Lean source supplies both with in-repository terms. No human has checked this material.

Standard background includes crystalline representations, inertia and local reciprocity. On this route “good class”, “row” and “local defect” denote Lean identifiers or terminology introduced by these drafts. Read them with the linked project definitions. [Glossary](../../lookup/glossary.md)

The blueprint and paper versions cited here are this project’s own AI-written, unpublished and human-unreviewed drafts. They are not by the Lean development’s author. Blueprint v13, its separate cover, and paper v5 are distributed as assets of release v0.1.0. For v3 and v4 the atlas supplies selected excerpts and notes. [Edition register](../../data/editions.json)

[Starter packet](../../notes/local/README.md) · [Open questions](../../questions/local.md) · [Unit inventory](units.md) · [Korean](../../docs/ko/local.md)

## Start here

**An elementary defect bound at an inert prime.** Blueprint v13, printed pp. 58–64 (7 pages). Check Lemma 4.6 (FactLpF) for a nonzero cycle length, an integer parameter $\ell \ge 2$ and nonnegative row sizes. The nearby coefficient model explains the application. The full Hecke-place assertion P045 has additional formal-group hypotheses. [Read the packet](../../notes/local/README.md)

**Starter prerequisites.** Finite cyclic groups, finite sums, a supremum and the elementary notion of a valuation. Knowledge of formal groups is useful for the final application only. [P045](../../units/P045.md)

## Where this field enters

Fix a place before fixing a lattice. P041–P044 compare data over a normalized ring with the original local conditions. Write down the coefficient ring, ramification index and integral lattice. Agreement after extension of scalars need not preserve the original integral index.

Height-two formal-group coordinates enter the reading of the kernel. Z42-SITES identifies the allowed places and the lattice dictionary, while Z4.2.02 asks for a local model realizing a kernel that has already been specified. In P045 the valuation bound for expansion coefficients is passed to a Hecke calculation. A second local question concerns the host itself. D014 identifies its exceptional primes, inertia images and Frobenius signs under explicit host axioms. These local gains have to be evaluated at the places supplied by the global construction.

## Reading path

Follow these units in order. Each card identifies the assumptions, the Lean declaration and the available exposition.

### First reading

1. [Z3.1](../../units/Z3.1.md) · Fix the normalized matrix algebra.
2. [Z3.2](../../units/Z3.2.md) · Pass from local comparisons to a global index.
3. [D014](../../units/D014.md) · Identify exceptional primes and inertia.
4. [Z42-SITES](../../units/Z42-SITES.md) · Read the parameters at the served places.

### Core argument

1. [P045](../../units/P045.md) · Inspect the Hecke-place coefficient bound.
2. [B04](../../units/B04.md) · Isolate the tame type condition.
3. [Z42-FRAMES](../../units/Z42-FRAMES.md) · Compare scalars after changing frames.

### Open inputs and scope

1. [Z4.2.02](../../units/Z4.2.02.md) · Realize the fixed tagged kernel locally.
2. [T24](../../units/T24.md) · Locate the integral Hodge–Tate kernel comparison.

## Literature and the scope of the comparison

An AI review (R21) reports comparing the trace, induction, supercuspidal and twisting clauses with Scholze’s *The local Langlands correspondence for GLₙ over p-adic fields* (Theorem 1.2(a)–(d), locator not verified here). The repository’s B04 weakens the assignment off the good cuspidal classes. [R21](../../reviews/R21_review.md) · [R18](../../reviews/R18_review.md)

## Questions for a specialist

After a coordinate change, which integrality and valuation bounds remain valid on the original coefficient ring? [All three questions and units to check](../../questions/local.md)
