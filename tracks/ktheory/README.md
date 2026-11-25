# Algebraic K-theory and cohomology of arithmetic groups

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

The written deduction assumes [V](../../pillars/V.md), [F](../../pillars/F.md), Green’s finite-field character input, 31 local implications and the intermediate results listed in paper v6. No complete human-readable proof of V or F exists in this atlas. The Lean source supplies both with in-repository terms. No human has checked this material.

Standard background includes group homology, regulator ranks and torsion in algebraic K-groups. On this route “layer”, “divisor-character packet” and “finite count” in the linked notes denote Lean identifiers or terminology introduced by these drafts. Read them with the linked project definitions. [Glossary](../../lookup/glossary.md)

The blueprint and conditional paper are AI-written, unpublished manuscripts prepared under the direction of Gunhee Cho. They have no human review. Levent Alpöge is the author of the Lean development. The repository includes both PDFs. The edition register preserves the earlier sources used in reviews. [Blueprint v13a · printed pp. 149–155](../../editions/v0.1.0/blueprint_v13a.pdf#page=176) · [Conditional paper v6](../../editions/v0.1.0/paper_v6.pdf) · [Edition register](../../data/editions.json)

[Starter packet](../../notes/ktheory/README.md) · [Open questions](../../questions/ktheory.md) · [Unit inventory](units.md) · [Korean](../../docs/ko/ktheory.md)

## Start here

**Counting finite sets of divisor classes.** Blueprint v13, printed pp. 149–155 (7 pages). Track the cardinality bound once evaluations separate the finite set. Inspect the numerical cap and both consecutive integral homology torsion groups that enter it. The elementary last implication assumes that cap. [Read the packet](../../notes/ktheory/README.md)

**Starter prerequisites.** Finite abelian groups and their primary parts, valuations, units and ideal classes. The Selmer application also uses cohomology and congruence-group homology. [P036](../../units/P036.md) · [Z2.K5](../../units/Z2.K5.md)

## Where this field enters

W05 asks for a quantitative second-cohomology estimate with the field, prime and Tate twist all specified. Finiteness over a single field gives no control on how its order grows with degree and discriminant. Write the range of primes next to each estimate.

The route through arithmetic-group homology separates rational rank from integral torsion. P034 treats odd homology under the specified block operations. P035 handles stabilization. P038 brings in an integral torsion bound. At the finite level, Z2.K2 evaluates cycles on integral matrices after reduction and P036 counts the distinguished classes. These arguments supply bounds to W12, where the prime two and exceptional layers reappear. When comparing this route with a published product bound, list every prime omitted from that product.

## Reading path

Follow these units in order. Each card identifies the assumptions, the Lean declaration and the available exposition.

### First reading

1. [Z2.K2](../../units/Z2.K2.md) · Read how reductions evaluate integral cycles.
2. [Z2.K5](../../units/Z2.K5.md) · Count the equivariant characters.
3. [Z2.K8](../../units/Z2.K8.md) · Translate finite duality into a length.
4. [P034](../../units/P034.md) · Check the rank range in odd degree.

### Core argument

1. [Z2.K1](../../units/Z2.K1.md) · Inspect the localization kernel along the tower.
2. [P035](../../units/P035.md) · Track stabilization of torsion.
3. [P038](../../units/P038.md) · Identify the quantitative torsion bound.

### Open inputs and scope

1. [W05](../../units/W05.md) · Compare the allowed primes in the second-cohomology bound.
2. [W12](../../units/W12.md) · Read the common interval for exceptional layers.

## Literature and the scope of the comparison

An AI review (R19) reports looking up the rational ranks in Borel’s *Stable real cohomology of arithmetic groups*. AI reviews R19 and R21 report comparing the torsion estimate in Soulé’s *A bound for the torsion in the K-theory of algebraic integers*. The reported locators (Borel §12, Proposition 12.2 and Soulé §4.1, Theorem 1, §§4.3–4.4) are not verified here. The coefficient rings, excluded primes and discriminant dependence require separate checks. [R19](../../reviews/R19_review.md) · [R21](../../reviews/R21_review.md)

## Why the 11 primary units have these grades

Each of the 11 primary units has a recorded comparison at its named declaration. Ten carry L1 and one carries L2. The line numbers refer to the original reviews, whose prefatory atlas notices are excluded from that numbering. [Declaration-level evidence](../../data/grade_evidence.json)

| Unit | Grade | Review and original lines | Reason for grade |
|---|---|---|---|
| [P032](../../units/P032.md) | L1 | [R20](../../reviews/R20_review.md) 58, 110 | The AI review (R20) reports checking the uniform evaluation statement for the integral cycle. Its construction has an outline. |
| [P033](../../units/P033.md) | L1 | [R20](../../reviews/R20_review.md) 59, 110 | The AI review (R20) reports checking the determinant evaluation on scalar prisms. Its comparison gives statement-level evidence. |
| [P034](../../units/P034.md) | L1 | [R5 A](../../reviews/R5_review_A.md) 10–12 | The AI review identifies the odd homology and rank statement and records qualifications about its proof. |
| [P035](../../units/P035.md) | L1 | [R20](../../reviews/R20_review.md) 111 | The AI review (R20) reports checking the assertion about stable torsion orders. R5 A also qualifies the proof in this block. |
| [P036](../../units/P036.md) | L1 | [R20](../../reviews/R20_review.md) 112 | The AI review (R20) reports checking the finite count and exponent loss under the stated separation hypotheses. |
| [P037](../../units/P037.md) | L1 | [R20](../../reviews/R20_review.md) 113 | The AI review (R20) reports checking the layer-to-kernel implication, with the layer bound supplied as an input. |
| [P038](../../units/P038.md) | L1 | [R20](../../reviews/R20_review.md) 114 | The AI review (R20) reports checking the all-prime torsion statement. R4 reviews the shared blueprint conclusion. The v3 manuscript gives an outline for P038. |
| [P039](../../units/P039.md) | L1 | [R4 Z2](../../reviews/R4_review_Z2.md) 91–123 | The AI review (R4) reports checking the shared torsion declaration in the blueprint. The v3 manuscript outlines its use with one discriminant exponent. |
| [Z2.K2](../../units/Z2.K2.md) | L1 | [R4 Z2](../../reviews/R4_review_Z2.md) 12–16 | The AI review (R4) reports checking the integral-cycle evaluation statement and records gaps in its homological bookkeeping. |
| [Z2.K4](../../units/Z2.K4.md) | L1 | [R5 A](../../reviews/R5_review_A.md) 10–12 | The AI review (R5 A) reports checking the stable odd homology and torsion claim, with qualifications on the proof. |
| [Z2.K7](../../units/Z2.K7.md) | L2 | [R4 Z2](../../reviews/R4_review_Z2.md) 91–123 | The AI review (R4) reports checking the blueprint’s full integral torsion bound under its inputs, including its exponent. |

## Questions for a specialist

For which twists and degrees does the needed prime fall outside Soulé’s product? Identify a supplier for the remaining small-prime term. [All three questions and units to check](../../questions/ktheory.md)
