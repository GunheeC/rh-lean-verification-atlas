# D570 · Upper bound for the weighted mean of lower slopes

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 12 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**Outlined · pending_review.** The lower-slope correction varies over a finite set of lattice indices. A common count bound at a single unit gives an upper bound for each correction, so the same bound holds after taking its weighted mean.

## Claim and hypotheses

Under the Hida size setting and Count5, the d(u)-weighted mean of the lower quantities Lo5 at any unit u is at most cSl1·IO(u)+K7v5.
$$
\mathrm{wmean}\bigl(d(u),\mathrm{Lo5}(u)\bigr)\le c_{\rm Sl1}\mathrm{IO}(u)+K_{7,v5}.
$$

[`Formalism.LFunctionChainParameters.WeightedSlopeBounds.weighted_mean_lower_bound_le` · `LevelOfCongruence.lean:162–171`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SizeWindowBrackets/ChainSlopeWindows/LevelOfCongruence.lean#L162-L171)

## Isolate the only varying term

Fix $u_0$ and an index $u$ in its nonempty finite set $W(u_0)$. Set $A=c_{\rm Sl1} n_T m(a/k+b')$. In the lower-slope correction the dependence on $u$ is entirely through $\log T(u_0,u)$. The other summands are $c_{\rm Sl1}\,\mathrm{IO}(u_0)$ and $c_{\rm Sl1}X''+1$. The variable $u_0$ stays fixed: the mean runs over $u$, with no outer mean over units. [`Formalism.LFunctionChainParameters.WeightedSlopeBounds.Lo5` · `QuotientSlopeBoundsWith.lean:15–17`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SizeWindowBrackets/QuotientSlopeBoundsWith.lean#L15-L17) [`Formalism.LFunctionChainParameters.WeightedSlopeBounds.weighted_mean_lower_bound_le` · `LevelOfCongruence.lean:162–171`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SizeWindowBrackets/ChainSlopeWindows/LevelOfCongruence.lean#L162-L171)

## Choose the relevant count

The count hypothesis has a lower bound for the log count, an upper bound, and a bound on its difference for two indices. Use its middle clause, $\log T(u_0,u)\leq c_{\rm Count}mL$. The setting gives $a\ge0$, $b'\ge0$, $k>0$ and $c_{\rm Sl1}\ge0$. Together with $n_T\ge0$ and $m\ge0$ these imply $A\ge0$. Multiply the count inequality by $A$ and add the other two summands. The resulting upper bound is $c_{\rm Sl1}\mathrm{IO}(u_0)+K_{7,v5}$, with $K_{7,v5}=A(c_{\rm Count}mL)+c_{\rm Sl1}X''+1$. The term $X''$ occurs additively on both sides. [`Formalism.LFunctionChainParameters.WeightedSlopeBounds.Count5` · `QuotientSlopeBoundsWith.lean:27–32`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SizeWindowBrackets/QuotientSlopeBoundsWith.lean#L27-L32) [`Formalism.LFunctionChainParameters.WeightedSlopeBounds.K7v5` · `LevelOfCongruence.lean:29–30`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SizeWindowBrackets/ChainSlopeWindows/LevelOfCongruence.lean#L29-L30) [`Formalism.LFunctionChainParameters.WeightedSlopeBounds.weighted_mean_lower_bound_le` · `LevelOfCongruence.lean:164–171`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SizeWindowBrackets/ChainSlopeWindows/LevelOfCongruence.lean#L164-L171)

## Average without changing the constant

At this unit each $u$ has a strictly positive weight. Multiply the pointwise inequality by that weight and sum over $W(u_0)$. Division by the positive total weight preserves the inequality. The weighted mean of the constant on the right equals the constant because the same total weight occurs in numerator and denominator. The implementation separates order preservation from the identity for a constant mean, using nonemptiness for strict positivity in the second step. [`Formalism.RankGapBounds.WeightedMeanData.wmean_mono` · `WeightedMeanData.lean:16–22`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/RankGapBounds/RankGapProofs/WeightedMeanData.lean#L16-L22) [`Formalism.RankGapBounds.WeightedMeanData.wmean_const` · `WeightedMeanData.lean:27–32`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/RankGapBounds/RankGapProofs/WeightedMeanData.lean#L27-L32) [`Formalism.RankGapBounds.WeightedMeanData.wmean_le_const` · `WeightedMeanData.lean:34–38`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/RankGapBounds/RankGapProofs/WeightedMeanData.lean#L34-L38)

## Identify the remaining loss (downstream application)

The result still contains the unit-dependent $\mathrm{IO}(u_0)$. Replacing it by a uniform loss bound belongs to a later application and requires a separate loss hypothesis. In that application $c_{\rm Sl1}\ge0$ permits the comparison after multiplication. Thus the calculation fits the longer slope estimate without importing a uniform bound on $\mathrm{IO}$ into its own hypotheses. [`Formalism.LFunctionChainParameters.WeightedSlopeBounds.each_unit_bound_statement` · `LevelOfCongruence.lean:175–192`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SizeWindowBrackets/ChainSlopeWindows/LevelOfCongruence.lean#L175-L192)

## First step to challenge

Check the sign of the coefficient of the logarithmic count before multiplying the upper counting inequality. Check positivity of the total weight before cancelling it.

See [D568](../../units/D568.md) for the two occurrences of this mean in the Gaussian estimate and [P021](../../units/P021.md) for its pointwise role.
