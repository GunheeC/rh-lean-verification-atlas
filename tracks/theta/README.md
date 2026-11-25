# Theta correspondence and automorphic representations of unitary groups

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

The written deduction assumes [V](../../pillars/V.md), [F](../../pillars/F.md), Green’s finite-field character input, 31 local implications and the intermediate results listed in paper v8. No complete human-readable proof of V or F exists in this atlas. The Lean source supplies both with in-repository terms. No human has checked this material.

Standard background includes the theta correspondence, Weil representations and Eisenstein series. On this route “definite-side witness”, “linked rows” and “grid” denote Lean identifiers or terminology introduced by these drafts. Read them with the linked project definitions. [Glossary](../../lookup/glossary.md)

Gunhee Cho is the paper’s author and the blueprint’s editor. Both were drafted with AI assistance. No human, the author included, has yet checked the arguments. Levent Alpöge is the author of the Lean development. The repository includes both PDFs. The edition register preserves the earlier sources used in reviews. [Blueprint v13c · printed pp. 473–478](../../editions/v0.1.0/blueprint_v13c.pdf#page=509) · [Conditional paper v8](../../editions/v0.1.0/paper_v8.pdf) · [Edition register](../../data/editions.json)

[Starter packet](../../notes/theta/README.md) · [Open questions](../../questions/theta.md) · [Unit inventory](units.md) · [Korean](../../docs/ko/theta.md)

## Start here

**Exact duality for the standard Weyl lattices.** Blueprint v13, printed pp. 473–478 (6 pages). At the identity Gram matrix, check the two integrality tests for a vector in the specified Weyl space. Then follow the change of basis in the transported test. The global twisted periods in Z4.4 require further inputs. [Read the packet](../../notes/theta/README.md)

**Starter prerequisites.** Integral lattices, polynomials, partitions and tableaux, factorial pairings and change of basis over a number field with involution. [Z4.4](../../units/Z4.4.md)

## Where this field enters

T12 gives a Siegel–Weil special-value formula for an Eisenstein series on the doubled group. The verification problem is to recognize the theta average, with its character, measure, test vector and normalization, inside the project’s evaluation on a selected lattice chain. In T12 write down the two dimension regimes and the factor in each. This prepares the comparison with both local readings in T11.

The Fock model provides local kernels. Z4.2.04 passes between kernels of adjacent lattices, and Z4.4 follows a twisted period along the selected chain. Record the base point as well as the scalar when comparing two readings. A period available at one point need not furnish the common witness used by every row. T09 asks whether the evaluation functionals separate. N076 bounds weighted minor moments on the wave grid under the stated thresholds. [N076 · statement and pinned source](../../units/N076.md)

## Reading path

Follow these units in order. Each card identifies the assumptions, the Lean declaration and the available exposition.

### First reading

1. [N188](../../units/N188.md) · Fix a nonsingular Hermitian Gram coefficient.
2. [Z4.2.04](../../units/Z4.2.04.md) · Compare kernels of adjacent lattices.
3. [P048](../../units/P048.md) · Read the simultaneous local bounds on one period.
4. [T12](../../units/T12.md) · Identify the two rank-dependent multipliers in the Siegel–Weil formula.

### Core argument

1. [Z4.4](../../units/Z4.4.md) · Track the period on the chosen chain.
2. [T11](../../units/T11.md) · Compare the specified integrals and local readings.
3. [T09](../../units/T09.md) · Locate separation on the evaluation grid.

### Open inputs and scope

1. [Z4.2.13](../../units/Z4.2.13.md) · Check that vector and period laws use the same base.
2. [Z4.3](../../units/Z4.3.md) · Inspect off-level valuations.
3. [N076](../../units/N076.md) · Check the weighted upper bound and the separated-parameter range.

## Literature and the scope of the comparison

An AI review (R21) reports comparing the anisotropic multiplier in T12 with Yamana’s *The Siegel–Weil formula for unitary groups* (Theorem 2, locator not verified here). T09 and T11 also use a separate evaluation grid and local matching data. [R21](../../reviews/R21_review.md) · [R16 A](../../reviews/R16_review_A.md)

## Questions for a specialist

At equal dimensions, which multiplier and measure enter the Siegel–Weil special-value formula, and which map transports them to T11? [All three questions and units to check](../../questions/theta.md)

## The two open inputs

[V · uniform Selmer window](../../pillars/V.md) · [F · compatible definite-side witness](../../pillars/F.md)
