# Verification status

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

This page separates the formal check from the reading of the mathematics. The Lean source is fixed at commit `40e56bab026552e089d7afcfeff08d2defb9c005`. The edition register identifies Blueprint v13, the paper manuscripts and the individual notes used below. [Coverage, open inputs and reader checks](docs/coverage.md) · [Source register](sources/README.md) · [Edition hashes](data/editions.json) · [한국어](docs/ko/STATUS.md)

## The documents

Gunhee Cho’s paper, *Toward a human verification of Alpöge's Lean proof of the Riemann hypothesis, I: the conditional chain from Selmer windows to zero-free regions*, maps 775 Lean statements and follows the conditional deduction from the Selmer window to zero-free regions. The companion blueprint builds up the 20 original inputs from definitions and lemmas. With each edition, the atlas links steps in both documents to Lean declarations and review records so readers can check them by hand. AI systems drafted the texts under Gunhee Cho’s direction and cross-checked passages against the Lean source. No step has a human check. [Paper v7](editions/v0.1.0/paper_v7.pdf) · [The Alpöge formalization of RH and GRH: an informal blueprint (Blueprint v13b)](editions/v0.1.0/blueprint_v13b.pdf) · [Editions and fingerprints](data/editions.json)

Paper v7 retains the mathematical text of the theorem, lemma, proposition and proof environments in v6, the typographic revision of v5. Blueprint v13a added two opening sheets to the 944 sheets of v13. Version v13b revises the front matter and removes disclaimers from the first two original sheets. Original sheets 3–944 match in extracted text, PDF content streams and rendering. The eleven opening sheets put original PDF sheet $n$ at physical sheet $n+11$ in v13b. Printed Arabic page 1 begins on physical sheet 37. Reviews and grades apply only to the editions and passages examined.

## What the formal development states

| Export | Target in the pinned source |
|---|---|
| [P001](units/P001.md) · `riemannHypothesis : RiemannHypothesis` | Mathlib's zeta zero-line predicate. [Exact signature and definition](sources/lean-goals.md#p001) |
| [P002](units/P002.md) · `riemannZeta_eq_zero_re : RiemannZetaZerosOnLine` | A zeta zero outside the negative even integers, with $s\ne1$, has real part $1/2$. [Exact Lean statement](sources/lean-goals.md#p002) |
| [P003](units/P003.md) · `LFunction_ne_zero_of_half_lt_re : DirichletLNonvanishingRightOfHalf` | For every nonzero modulus and every character, $L(s,\chi)\ne0$ to the right of $1/2$, with the principal character at $s=1$ excepted. [Exact Lean statement](sources/lean-goals.md#p003) |
| [P004](units/P004.md) · `LFunction_eq_zero_re : DirichletLZerosOnLine` | For any Dirichlet character of nonzero modulus, a zero in $0<\Re s<1$ has real part $1/2$. [Exact Lean statement](sources/lean-goals.md#p004) |
| [P005](units/P005.md) · `LFunction_eq_zero_re_of_isPrimitive : PrimitiveDirichletLZerosOnLine` | The zero-line assertion in the open strip, restricted to primitive characters. [Exact Lean statement](sources/lean-goals.md#p005) |

All five exports depend on the three axioms `propext`, `Classical.choice` and `Quot.sound` according to the MIT inspection. [Axiom evidence](sources/kernel-audit.md)

## Freshness

The MIT page was captured at 05:25 UTC on 24 November 2026. The formal source, public reading projects and publisher documents have their own dated pins. To repeat a comparison, use the commit for a repository or the SHA-256 for a downloaded document. [Dates and recheck instructions for all nine entries](sources/freshness.md)

| External edition | Snapshot date |
|---|---|
| Lean source mirror | 20 November 2026 |
| Original Lean distribution | 20 November 2026 |
| MIT verification record | 24 November 2026 |
| Adriazola’s reconstruction | 24 November 2026 |
| Naskręcki’s reading project | 24 November 2026 |
| JoseBrox/GRH_distillation | 24 November 2026 |
| jae-63/rh-alpoge-blueprint | 20 November 2026 |
| Waterloo zeta draft | Version 2 dated 22 November 2026 |
| Alpöge’s announcement | 20 November 2026 |

For a Git source compare its full commit and tree. For the archive hash the fourteen parts joined in order. For a PDF or the MIT HTML page hash the downloaded bytes and compare the printed edition or timestamp. [Per-source evidence](sources/registry.json)

## Which checks have finished?

The MIT verification record, captured on **24 November 2026 at 05:25 UTC**, reports external checks of the compiled modules by Lean’s kernel and lean4lean. The default and paranoid Lean kernels, nanoda and con-leche from master accepted the full export. The challenge comparisons with con-leche and con-ron also passed. The standalone Comparator 4.33.0 passed. The final default-kernel stage of the separate 4.36.0 end-to-end lake comparator was still running. This atlas reports those external results and did not reproduce the runs. [Per-run results, incompatible versions and snapshot hash](sources/kernel-audit.md)

On 25 November an AI session for this atlas ran Lean 4.33.1’s `#print axioms` on all five public declarations after importing `Main`. Each listed `propext`, `Classical.choice` and `Quot.sound`. Reading the axiom metadata directly from the manifest-verified `Main.olean` gave the same five results. [Reproduce the local axiom lookup](notes/formal/procedures.md)

## What a reader can check here

<!-- front:status:start -->
| Primary field | Units | Full | Outlined | Statement only |
|---|---:|---:|---:|---:|
| Analytic number theory | 35 | 23 | 8 | 4 |
| Arakelov geometry and geometry of numbers | 33 | 7 | 20 | 6 |
| Theta correspondence and automorphic representations of unitary groups | 40 | 6 | 34 | 0 |
| Galois representations, automorphy lifting, Iwasawa theory and Euler systems | 62 | 11 | 26 | 25 |
| Local p-adic theory | 26 | 3 | 23 | 0 |
| Algebraic K-theory and cohomology of arithmetic groups | 11 | 5 | 6 | 0 |
| Formalization and reproducibility | 10 | 0 | 10 | 0 |
| **All units** | **217** | **55** | **127** | **35** |

The highest evidence grades are L0 138, L1 55, L2 24, L3 0, L4 0. Full means the argument is written under the unit’s stated inputs. 20 units have an AI assessment of their entire current prose, including outlines. L2 alone includes [D014](units/D014.md), [P014](units/P014.md), [Z1.3.06](units/Z1.3.06.md), [Z1.3.07](units/Z1.3.07.md), [Z4.2.04](units/Z4.2.04.md). Current-prose review alone includes [D550](units/D550.md). The grade can cover a scoped argument, and a current-prose review can cover an outline. Of 739 current steps, 6 have a step-specific AI review and 0 have a qualifying personal check. [Evidence levels](FAQ.md) · [Named checks](signoffs/README.md)

### Lean lines cited in the writing

Each row counts the union of the Lean ranges cited by current steps in that category. Overlapping lines count once within a row. The physical denominator sums newline characters (wc -l) across every Lean file in the pinned src directory. A core line is one line of a project declaration’s inclusive source range in the pinned graph. A literature node is a declaration where the dependency traversal stops. Its agreement with a published result requires a separate comparison.

| Scope | Of 17,374,215 physical lines in all 175,187 pinned source files | Of 9,567,045 weighted core lines |
|---|---:|---:|
| Any written step | 13,015 (0.0749%) | 12,584 (0.1315%) |
| Steps in full arguments | 5,863 (0.0337%) | 5,853 (0.0612%) |
| Steps in outlines | 7,928 (0.0456%) | 7,507 (0.0785%) |
| Steps reviewed by AI on this edition | 60 (0.0003%) | 60 (0.0006%) |
| Steps in prose with a whole-argument AI review | 1,686 (0.0097%) | 1,686 (0.0176%) |
| Steps with a current qualifying human check | 0 (0.0000%) | 0 (0.0000%) |

Citations can overlap across categories. The separate index-position table assigns each core line to its nearest unit above it in the dominator tree. Position says where a line sits in the index. It provides no evidence that anyone explained or read that line. The V and F suppliers dominate disjoint regions totaling 4,565,893 core lines. [Index position, denominators and history](PROGRESS.md) · [Field breakdown](dashboard/README.md)
<!-- front:status:end -->

Two global assumptions still lack a complete written derivation here. V supplies an interval on which bounds for Selmer localization kernels hold uniformly. F supplies one record containing a class of families and a compatible selection. Its norm estimate applies across the eligible families. The definite-side conditions must hold with the same selection. The conditional argument also assumes Green’s finite-field character assertion. Lists A, B and C cover the prime-sum estimates, construction of the arithmetic family and geometric comparisons, respectively. [V and its hypotheses](pillars/V.md) · [F and its hypotheses](pillars/F.md) · [Inputs and review scope](sources/coverage.md) · [Proof map](MAP.md)

## When a Lean result has a classical name

The Lean repository defines propositions under names taken from the literature and supplies them with its own terms. B04 restricts the stronger local parameter laws to specified classes. W11 gives a bounded-rank variant for a tower. T12 uses a particular special-value normalization. T17 uses this development’s arithmetic volume and intersection comparison. P010 has three restricted local comparison clauses away from the coefficient prime. No human has matched these formulations to their published counterparts. [B04](units/B04.md) · [W11](units/W11.md) · [T12](units/T12.md) · [T17](units/T17.md) · [P010](units/P010.md)

### What the conditional manuscript assumes

The v4 manuscript listed three global assumptions and 31 local inputs for Theorems 1.1 and 3.43. An AI review (A) identified further results used in the deduction. Paper v5 identifies the level/window criterion, the pointwise lattice estimate, the eventual rank bound and two comparison results. It also identifies the classical facts about L-functions used at the boundary and to transfer the conclusion. Paper v7 · [conditional theorem, printed p. 2](editions/v0.1.0/paper_v7.pdf#page=2) · [hypothesis table, printed pp. 51–52](editions/v0.1.0/paper_v7.pdf#page=51) · [closing deduction, printed pp. 52–53](editions/v0.1.0/paper_v7.pdf#page=52). This manuscript revision awaits independent review. The atlas labels the combined argument an outline. Each review of an individual calculation applies only to the edition and scope recorded for that calculation. [Conditional outline and hypotheses](units/V4-COND.md) · [Review dispositions](data/round4_review_corrections.json) · [Mathematical overview](OVERVIEW.md) · [Paper editions](data/editions.json)

## What would change this page?

| Event | Record and consequence |
|---|---|
| A named reader checks a specified statement | Record the edition, named steps or statement comparison, verdict and reservations. L4 requires a Full argument with a derivation beyond an appeal to an input, plus current personal checks for every active step and a separate comparison of the statement with Lean. A dispute can close through a second reader who is not the maintainer or a new text edition that supersedes its target. Partial checks retain their exact scope. [Sign-off records](signoffs/README.md) |
| A second independent exposition agrees | Register its edition, identify the matching proposition and resolve any differences in hypotheses. The ledger can then support a new L3 entry. [Source and review procedure](CONTRIBUTING.md) |
| A counterexample, missing hypothesis or incorrect derivation is identified | Link the first affected unit and evidence, revise the corresponding wording or grade, then regenerate the counts. The change log retains the prior assessment. [Correction procedure](CONTRIBUTING.md) · [Change log](CHANGELOG.md) |
