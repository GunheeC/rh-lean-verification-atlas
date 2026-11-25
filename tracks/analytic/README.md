# Analytic number theory

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

The written deduction assumes [V](../../pillars/V.md), [F](../../pillars/F.md), Green’s finite-field character input, 31 local implications and the intermediate results listed in paper v8. No complete human-readable proof of V or F exists in this atlas. The Lean source supplies both with in-repository terms. No human has checked this material.

Standard background includes Dirichlet characters, zeros and the Mellin transform. On this route “host”, “level” and “window” denote Lean identifiers or terminology introduced by these drafts. Read them with the linked project definitions. [Glossary](../../lookup/glossary.md)

Gunhee Cho is the paper’s author and the blueprint’s editor. Both were drafted with AI assistance. No human, the author included, has yet checked the arguments. Levent Alpöge is the author of the Lean development. The repository includes both PDFs. The edition register preserves the earlier sources used in reviews. [Blueprint v13c · printed pp. 7–14](../../editions/v0.1.0/blueprint_v13c.pdf#page=43) · [Conditional paper v8](../../editions/v0.1.0/paper_v8.pdf) · [Edition register](../../data/editions.json)

[Starter packet](../../notes/analytic/README.md) · [Open questions](../../questions/analytic.md) · [Unit inventory](units.md) · [Korean](../../docs/ko/analytic.md)

## Start here

**The Landau window criterion.** Blueprint v13, printed pp. 7–14 (8 pages). Prove the abstract implication in P022 with the pole and window data fixed. Locate the positive-residue condition for a real pole. P023 explains the application to a smoothed sum. [Read the packet](../../notes/analytic/README.md)

**Starter prerequisites.** Complex analysis through residues, holomorphic power series, Mellin/Laplace transforms, and elementary bounds for the von Mangoldt function. [P022](../../units/P022.md) · [P023](../../units/P023.md)

## Where this field enters

The analytic argument begins with an unusual constraint. An upper bound for the prime sum is available on long intervals of the logarithmic variable, with gaps between them. In P022, Taylor coefficients of the transform detect a pole despite those gaps. To read the proof, mark the integration window, the half-plane of continuation and the point at which the sign of a real residue enters.

A separate arithmetic argument supplies the windows. At one scale B10 translates a lattice budget into a gap between finite sums. B09 averages over a subgroup, retaining precisely the characters trivial on it. B08 transfers the surviving sum to the prescribed level. When passing to a family in P017, track which thresholds have already been chosen before the host and scale vary. An AI review of v3 recorded gaps in the lower inputs to P017.

## Reading path

Follow these units in order. Each card identifies the assumptions, the Lean declaration and the available exposition.

### First reading

1. [P003](../../units/P003.md) · State the half-plane target and principal exception.
2. [P022](../../units/P022.md) · Read the abstract window lemma.
3. [P023](../../units/P023.md) · Apply it to a smoothed character family.
4. [P018](../../units/P018.md) · Track the level and the family quantifiers.

### Core argument

1. [B10](../../units/B10.md) · Identify the lattice gap.
2. [B09](../../units/B09.md) · Average the surviving characters.
3. [B08](../../units/B08.md) · Identify the level sum.
4. [P017](../../units/P017.md) · Pass from a single scale to a family.

### Open inputs and scope

1. [B07](../../units/B07.md) · Test simultaneous host and character supply.
2. [N415](../../units/N415.md) · Check the range and exceptional term in a relative prime count.

## Literature and the scope of the comparison

An AI review (R19, original line 64, public copy line 78) reports comparing Landau’s theorem on p. 1, Theorem 15.1 of the UBC Math 539 handout of 2 April 2020. No human has checked that comparison. The stronger moving-window criterion used here is a separate argument under pole and window hypotheses. [R19](../../reviews/R19_review.md) · [R20](../../reviews/R20_review.md) · [R23](../../reviews/R23_review.md)

## Questions for a specialist

Where does the contradiction use positivity of the residue at a real pole? Identify the corresponding datum in P023. [All three questions and units to check](../../questions/analytic.md)
