# Galois representations, automorphy lifting, Iwasawa theory and Euler systems

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

The written deduction assumes [V](../../pillars/V.md), [F](../../pillars/F.md), Green’s finite-field character input, 31 local implications and the intermediate results listed in paper v7. No complete human-readable proof of V or F exists in this atlas. The Lean source supplies both with in-repository terms. No human has checked this material.

Standard background includes Galois representations, Selmer groups and Euler systems. On this route “polarized row”, “host” and “page function” denote Lean identifiers or terminology introduced by these drafts. Read them with the linked project definitions. [Glossary](../../lookup/glossary.md)

Gunhee Cho is the paper’s author and the blueprint’s editor. Both were drafted with AI assistance. No independent human referee has checked the arguments. Levent Alpöge is the author of the Lean development. The repository includes both PDFs. The edition register preserves the earlier sources used in reviews. [Blueprint v13b · printed pp. 76–81](../../editions/v0.1.0/blueprint_v13b.pdf#page=112) · [Conditional paper v7](../../editions/v0.1.0/paper_v7.pdf) · [Edition register](../../data/editions.json)

[Starter packet](../../notes/galois/README.md) · [Open questions](../../questions/galois.md) · [Unit inventory](units.md) · [Korean](../../docs/ko/galois.md)

## Start here

**Splitting a Selmer length into two eigenspaces.** Blueprint v13, printed pp. 76–81 (6 pages). In Lemma 5.8, check stability of the submodule and invertibility of 2 before forming the two projectors. In Proposition 5.10 combine the odd-prime lengths with the separate 2-adic budget. [Read the packet](../../notes/galois/README.md)

**Starter prerequisites.** Finite-length modules over a discrete valuation ring, involutions and their projectors. Cohomology is needed to recognize the localization kernel in the application. [P020](../../units/P020.md)

## Where this field enters

The Selmer window in P013 bounds a weighted sum over primes and layers for varying CM fields. Start by fixing the primitive character. For every constant that appears later, write down whether it may depend on the field, the twist or the layer. A representation-by-representation vanishing result has different quantifiers from this window.

The positive and negative parts of the length bring together several inputs. W08 and W09 distinguish collective from individual bounds. In P026, norm compatibility of the layers has to survive passage to integral coefficients, including denominators in the Hecke projector. P025 compares ordinary and Bloch–Kato conditions for an adjoint representation. W13 assembles the counting estimates. P013 also needs the constructions supplying them. In the application to a lattice inequality the separate common definite-side witness F supplies the geometric link consuming the lengths.

## Reading path

Follow these units in order. Each card identifies the assumptions, the Lean declaration and the available exposition.

### First reading

1. [W11](../../units/W11.md) · Read the repository’s bounded-rank formulation named after Ferrero–Washington.
2. [P040](../../units/P040.md) · Read the compact-coefficient length formula.
3. [W08](../../units/W08.md) · Find the aggregate estimate in Case I.
4. [W09](../../units/W09.md) · Compare the individual estimates in Cases II and III.

### Core argument

1. [P026](../../units/P026.md) · Track integrality and local conditions in the Euler system.
2. [W13](../../units/W13.md) · Combine the case bounds.
3. [P013](../../units/P013.md) · Restore the field and scale quantifiers in the Selmer window.

### Open inputs and scope

1. [Z1.2](../../units/Z1.2.md) · Compare ordinary and adjoint rigidity.
2. [W07](../../units/W07.md) · Inspect the two vanishing inputs.
3. [P024](../../units/P024.md) · Track markings at the endpoints and descent.

After these routes, [P011](../../units/P011.md) combines the representation row, the local parameter existence record and the window.

## Literature and the scope of the comparison

[W11](../../units/W11.md) proves a bounded-rank assertion in the Lean development. No human has compared that assertion with the published μ-invariant theorem.

An AI review (R19) reports consulting Kato’s *p-adic Hodge theory and values of zeta functions of modular forms* for the zeta element, its norm relation and the dual exponential. The reported locators (8.1.3), Proposition 8.12 and Theorem 9.7 are not verified here. P026 additionally uses uniform projectors and local conditions. [R19](../../reviews/R19_review.md) · [R23](../../reviews/R23_review.md)

## Questions for a specialist

Where is a denominator chosen that works for the integral Hecke projector at every layer? [All three questions and units to check](../../questions/galois.md)

## The two open inputs

[V · uniform Selmer window](../../pillars/V.md) · [F · compatible definite-side witness](../../pillars/F.md)
