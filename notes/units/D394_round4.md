# D394 · Tying period entries to level valuations

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 43,650 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**Outlined · pending_review.** For good constructed slots, six eventual assertions control reference and twisted evaluations, their periods, the real-row tie and the level-prime valuations. All six are read from the over-column description and carried to the linked bundle points.

## Statement and hypotheses

For every slot system and bundle linkage, six conditions hold eventually on built and good members: evaluation on the reference chain, twisted points, periods at zero and after twisting, compatibility of the two evaluations, and the level-prime column valuations.

$$
\bigwedge_{j=1}^{6}\mathrm{Lg1}(\mathrm{KPx},\,\mathrm{IsBuiltE},\,\mathrm{IsGoodE},\,P_j).
$$

[`period_entries_tie_and_level_valuations_at_built` · `SixRowsAtMemberStatement.lean:12-13`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SixRowsAtMemberStatement.lean#L12-L13)

**Read alongside** [P048 · One twisted period with simultaneous local bounds](../../units/P048.md) · [P096 · Equality of localized class lattices](../../units/P096.md) · [Z4.4 · Twisted periods on the selected chain](../../units/Z4.4.md) · [T04 · All 26 large-slot conditions from the open conditions](../../units/T04.md).

## Understand the six large-slot assertions

Fix the slot system and bundle linkage. The first two predicates concern evaluation on the reference chain and on the twisted point. The next two concern the periods at zero and at the twisted point. The fifth is a tie of the real-side columns, and the sixth concerns level-prime valuations of the columns. In the statement each of these predicates has its own eventual large-slot quantifier. In the proof all six can use the same elementary auxiliary slot. The objects within each predicate still have to be transported to the correct linked bundle point. [`six_rows_at_member_alt` · `SixRowsAtMember.lean:11-17`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SixRowsAtMember.lean#L11-L17)

## Choose the common column view

Intersect the good slot with the predicate that is always true. The good-twist-core result gives the over-columns property there. The constantly true predicate is itself a large-base condition on built slots, furnishing a witness that can be reused. At this stage the argument has produced a way to read columns at good points. It has yet to deduce any one of the six period or valuation assertions, which are supplied by separate conversions. [`six_rows_at_member_alt` · `SixRowsAtMember.lean:18-24`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SixRowsAtMember.lean#L18-L24)

## Example of one conversion

For the untwisted period, first prove a row property for the period class sum on constructed points. At the underlying point the true-column description identifies a row, with its integral input, lattice, parameters and pins. Apply the period-class-sum result to those data. The constructor for eventual working classes transfers this statement to the row on the specified slot. Only then apply the row-to-bundle operation with the given linkage. This shows where the integrality hypothesis enters; the eventual quantifier alone does not give an integral value. [`row_aPer0_of_overCols` · `ReferencePeriodIntegralBundlePointsOfOverColumns.lean:9-16`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/ReferencePeriodIntegralBundlePointsOfOverColumns.lean#L9-L16)

## Return each field to the row constructor

The other conversions use the same over-column witness for reference evaluation, twisted-point integrality, twisted-period integrality, real-side compatibility and the level-prime valuations. In the all-row constructor their projections have different positions: the sharp valuation field is selected before the point and period fields, and the tie follows these. A comparison of two periods on different linked points would not fill the projected row field. Checking the fixed linkage at each conversion is the mathematical part of this bookkeeping. [`six_rows_at_member_alt` · `SixRowsAtMember.lean:22-24`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SixRowsAtMember.lean#L22-L24) · [`allRows_of_open0_alt` · `LinkROfIsLinked.lean:52-66`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkROfIsLinked.lean#L52-L66)

**Scope of the hypotheses.** The note retains the source’s named predicates and records. For the exact quantified assumptions at this head, read `GlobalTheory.T.period_entries_tie_and_level_valuations_at_built` (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SixRowsAtMemberStatement.lean:12–13`). Their internal definitions are separate reading tasks.

**First step to challenge.** Check the passage from integrality of a constructed row to the reference period assertion at the linked bundle point, retaining its pins and its lattice.

[Unit record and exact statement](../../units/D394.md)
