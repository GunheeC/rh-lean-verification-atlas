# D486 · Joined row counts and the irreducibility link

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 773 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**Outlined · pending_review.** Joined, injectively labelled and counted rows give the eventual small irreducibility error for every sufficiently large family index. Green's finite-group input supplies admissibility of the label weights used in this deduction.

## Statement and hypotheses

Assume Green’s finite-group character input and the closed existence of injectively labelled, joined and counted rows with cIc positive. Eventually at every index the row deviations are nonnegative and their delta statistic is at most exp(-x^(ez/7)).

$$
\delta\le\exp(-x^{e_z/7}).
$$

[`closed_linkIRR_of_join_count` · `LinkIrr.lean:22-43`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkIrr.lean#L22-L43)

**Read alongside** [D379 · Counting constants from Siegel–Weil](../../units/D379.md) · [B05 · Connected families from Green and the closed link](../../units/B05.md) · [T04 · All 26 large-slot conditions from the open conditions](../../units/T04.md).

## Fix one counted row

Fix a twist selection and a positive real constant. On the specified enriched family class assume that beyond one family threshold, every index has a row record with injective label counting, a join and the count at the indicated rank-dependent tolerance. The existential row occurs outside the conjunction of those three conditions. Keep this order: three rows, each satisfying one of the clauses, would be insufficient. The output will apply to all sufficiently large indices and imposes the stated small error on the family. [`closed_linkIRR_of_join_count` · `LinkIrr.lean:22-33`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkIrr.lean#L22-L33)

## Supply the missing constraints at the same index

Enlarge the threshold to the maximum of the original threshold, the selection threshold, the starting scale plus one, and four. The strict family scale condition and eligibility for selection then hold together. Keep the previously obtained row. Green's cuspidal parametrization applies to the selected type record to supply admissible label weights for the datum. The family size lemma at the same point gives the size bounds with exponent six. Return the original injectivity, join and count with these two new fields; the row witness itself has not been changed. [`closed_linkIRR_of_join_count` · `LinkIrr.lean:34-43`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkIrr.lean#L34-L43)

## Pass from joining to weights

Apply the bound for a family of permitted positive exponent at most one. The derived exponent is positive. Raise the threshold further to include $(3/2)^{1/e_z}$. Then $x^{e_z}\ge3/2$, giving the weight range required by the size estimates. Combine that range, the admissible label weights, the tie and the existing join to obtain the weight condition for the counted row. This conversion permits the all-rows irreducibility estimate to act on the injective labelling, count, weights and sizes together. [`linkIRR_of_join_ex` · `LinkIRROfJoinEx.lean:17-32`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/LinkIRROfJoinEx.lean#L17-L32)

## Where the powers come from

The size lemma extracts the family scale, its positive exponent and its upper restrictions, and compares the ranks and prime parameters against powers of that very scale. The constant six in the application belongs to these size bounds, whereas the final delta estimate has $e_z/7$ in its exponent. These play distinct roles. Intersection with the closed exponent bound finishes the application. A useful check is to follow a single index through the chain of threshold increases and verify that the label weight tolerance still uses the fixed counting constant. [`sizesRec_at` · `LinkIRROfJoinEx.lean:39-53`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/LinkIRROfJoinEx.lean#L39-L53) · [`sizesRec_at` · `LinkIRROfJoinEx.lean:64-99`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/LinkIRROfJoinEx.lean#L64-L99) · [`closed_linkIRR_of_join_count` · `LinkIrr.lean:39-43`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkIrr.lean#L39-L43)

**Scope of the hypotheses.** The note retains the source’s named predicates and records. For the exact quantified assumptions at this head, read `GlobalTheory.Top.Irr.closed_linkIRR_of_join_count` (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkIrr.lean:22–43`). Their internal definitions are separate reading tasks.

## Literature-named inputs

`GlobalTheory.Top.Lq.admissibleLabelWeights_of_greenCuspidalParametrisation` — in-repo constant (`Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/AdmissibleLabelWeightsOfGreenCuspidalParametrisa.lean:255–299`); not compared.

**First step to challenge.** Check the passage from the joined-row count to the weighted estimate with the row's own labels and the fixed positive counting constant.

[Unit record and exact statement](../../units/D486.md)
