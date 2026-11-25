# T15 · Turning a height lower bound into a common covolume estimate

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**Outlined · pending_review.** Follow one column of one point in an admissible family. The arithmetic height estimate first applies to quotients on a good cover. One must turn it into a lower bound on the original lift, then combine it with the Gram recursion and an upper bound for the core. The last step chooses a coefficient that works for every column of every sufficiently large family member. [Unit T15](../../units/T15.md) · [Paper v3, Formal statement 5.25, p. 44](T15.tex) · [The v3 covolume application, pp. 22–23](P012-argument.tex)

## Hypotheses and conclusion

The formal head `SelfIntersectionVolumeEstimates.topCovolG_alt_alt` takes seven inputs in this order. Its local source is `ThirdPlaceSeries/TopCovolG.lean:39–41`. Short file references below are relative to the pinned Lean source. The exact paths and ranges are collected in the [source manifest](../../data/round3_arakelov.json).

| Input | What is supplied |
|---|---|
| Volume estimates | A self-intersection bound and injectivity on small sections. Both components are needed in the height argument. `VolumeEstimateHypotheses.lean:11` |
| Geometry of the model | Toroidal Kodaira–Spencer, seminegativity of the semiabelian Lie bundle, Green cuspidality, separation of pairs of points and a Fubini–Study Chow-height comparison. `HypothesesX.lean:10–20` |
| Hodge-bundle record | The full named record, including compactification, arithmetic volume, reduction and local comparison fields used by the cover suppliers. `ToKnownTheoremsOf.lean:7–35` |
| Toroidal and degree data | An integral Siegel toroidal model, toroidal charts for the fan, toroidal charts, and an arithmetic degree formula. `SemiposAtOfPositive.lean:216–220` |
| Grothendieck deformation | For a surjective ring map with a nilpotent divided-power kernel, the Grothendieck–Messing comparison at that thickening. `GrothendieckDeformation.lean:12–15` |
| Eight quoted assertions | Kawamata–Viehweg vanishing, log-canonical extension, comparison for holomorphic sections, nef numerics, existence of a Chow form, its integral form, hyperplane-section compatibility and proper-intersection length. `WellChosen.lean:22–30` |
| Uniform estimate on deep components | One nonnegative constant for the mean estimate on each eligible deep good datum, including the rank condition, interior index and at most fifteen distinct prime factors. This is the conclusion supplied by T14. `ModelSmall.lean:63–66`. [T14](../../units/T14.md) |

The conclusion is `CovolumeBoundOfX`. There is an epsilon threshold. For each allowed positive epsilon there is transported largeness data. For each family satisfying the family condition and that largeness requirement at height $H$, there is $C_0\ge0$ and then an eventual scale threshold. At every admissible point $p$ above that threshold and the family's own strict threshold, put $S=p.S(\mathrm{false})$. For every $C\ge C_0$ and every column $i$, the normalized log covolume satisfies

$$
\frac{\operatorname{lcv}(S.XW_i,S.M_i)}{S.D}\le (p.N(C,H)).\mathrm{l3}_i .
$$

The point must satisfy both `PointConditions'` and `RecTied`. The choice of $C_0$ precedes the choice of the point, the scale and the column. The base family and $H$ are already fixed at that stage. The definitions are `Closed` in `ParamsHeightRankConstant.lean:159–161`, `RowsTAlt` and `EventuallyAtAllPoints` in `LiftLambdaBound.lean:17–19`, `CovolumeBoundOfX` in the same file at lines 60–61 and `L3` in `IndefSide.lean:315–316`.

## From the point to its covers

1. **Fix the geometry in which the estimates agree.** From the toroidal record take the integral Siegel model, and from the model-geometry record take the Kodaira–Spencer and Lie assertions. The Hodge-bundle record gives the Gram comparison, measure comparison and existence of the deep covering datum. The size and anchor estimates are supplied separately. These are quantified statements for the same family and index. When cover hypotheses are specialized one also fixes an interior index and one good cover at that index. `topCovolG_alt_alt`, `TopCovolG.lean:42–50`. The two quantifier patterns are `LiftsCondition` and `CoversCondition` in `LiftLambdaBound.lean:26–32`.

2. **Compute degree before using the height.** Deep goodness uses the Hodge, deformation and quoted inputs with the three geometric fields just extracted. The flat-degree assertion is a separate comparison obtained from the Hodge record. With deep goodness, size and flat degree one obtains the covering degree. The cover degree is an argument of the next step, which bounds the share for each permitted quotient. In particular one cannot choose a new quotient after using its degree to estimate its share. The source makes this order explicit in `TopCovolG.lean:50–53`; the quantifiers over the same quotient appear in `LiftLambdaBound.lean:56–59`. [D443, the flat-degree supplier](../../units/D443.md)

3. **Bring the arithmetic estimate onto this cover.** The height lower bound and the bound for the cover-height sum are different assertions. The first combines the self-intersection and small-section input with short vectors, the geometry of the model, an integral carrying section in a controlled frame, the size budget and the deep mean estimate. The second uses the flat degree, the covering degree and the share on the chosen cover. In particular a lower bound for an average at an arbitrary deep component does not by itself identify the section, height, or measure in the chosen quotient. These two applications are `height_lower_bound_general_alt` in `HeightLowerBoundGeneral.lean:21–22` and `coverHeightSum_of_flatDeg_coverDegree_share` at its call in `TopCovolG.lean:54–55`. Deep goodness gives a further bound `sum_c_of_deep_good` on the component sum.

4. **Make the lower bound uniform and transport it off the cover.** Intersect the seven eventual conditions for goodness, size, degree, share, height, height sum and component sum. On the joint family, let $a,b\ge0$ be the constants for the height and height-sum bounds. The local covering comparison applies to all seven specializations at the same point and accepts the common lower-bound constant $2(3a+b+4)$. Its choice is independent of the point and cover. This is the content of `u_low_of_cover_hyps` in `ULowOf.lean:16–24`. To return to one lift, the source also requires the low defect from Gram and anchor data, deep existence, ring descent and compatible maps, cover rank, a generator bound and flatness. Their roles are explicit in `liftLowBound_of_cover_estimates` in `LowOfCoverHypothesesStatement.lean:11–12` and their suppliers are selected in `TopCovolG.lean:56–57`. The outline uses those comparison theorems as inputs to this step.

## Why one coefficient works for all columns

The final assembly simultaneously uses eight conditions on lifts. Four furnish Gram, recursion, truncation and the bad-set estimate. The other four give the lambda bound, size, an upper bound on the core and the lower bound just transported. The bad-set comparison uses the Green field along with the degree and share data. The rationality input is used together with Gram and measure to produce the core estimate. See the call to `covolX_of_truncation_badSet_lambda_lowBound` in `TopCovolG.lean:58`.

Write $C_1,C_2\ge0$ for the constants in the core and lower bounds. The family exponent is positive by evaluating its scale at an index over zero. Hence the loss inequality provides a scale threshold for the lambda and size constants and $C_1+C_2+1$. A second threshold makes the eight estimates available at once. Take the maximum of those thresholds. For any later point and column, identify its scale and exponent with the family's. The pointwise covolume comparison `lcv_le` gives the bound with coefficient $C_1+C_2+1$. The size estimate implies that its error factor `unitE p` is nonnegative, so replacing this coefficient by any greater $C$ preserves the inequality. Thus $C_0=C_1+C_2+1$ works uniformly for the points and columns quantified above. These steps occur in `covolX_of_lift_bounds_and_coreLe`, `CovolXOfSteps.lean:16–40`. The use of maxima to intersect eventual conditions appears in `EventuallyAtAllPoints.and`, `LiftLambdaBound.lean:20–25`.

**Point for independent review.** Trace the same deep cover, admissible quotient, integral carrying section and normalization from the deep mean estimate into `height_lower_bound_general_alt` and the cover-height sum. This is the substantive geometric passage behind the common lower constant. The last maximum only synchronizes thresholds after those estimates have been supplied. [Downstream use in T13](../../units/T13.md)

## Round 4 source comparison

In the first cover comparison the size and anchor suppliers are the closed constants `cov_size_bound` and `anchor_bound`. The flat degree in the following step is `flatDeg_of_scholzeWeinstein_of_prints hP`. For the uniform component estimate the head calls `uniform_lower_bound_of_sums'`, the wrapper of `u_low_of_cover_hyps`. The seven records and propositions are hypotheses at this head; the enclosing source route supplies them by repository terms. The flat-degree supplier's name identifies its local interface, without establishing equivalence to a published theorem.

[`SelfIntersectionVolumeEstimates.topCovolG_alt_alt` · `TopCovolG.lean:39–58`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TopCovolG.lean#L39-L58) · [`GlobalTheory.T.uniform_lower_bound_of_sums'` · `ULowOfStatement.lean:11–12`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ULowOfStatement.lean#L11-L12)

## Status of literature-named inputs

- `GlobalTheory.Published.GrothendieckDeformation` — hypothesis at this head (`Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/GrothendieckDeformation.lean:12–15`); not compared.
- `GlobalTheory.T.flatDeg_of_scholzeWeinstein_of_prints` — in-repo constant (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FlatDegreeStatement.lean:22–23`); not compared.
