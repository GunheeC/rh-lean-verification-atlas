# D568 · A slope bound for the Gaussian term

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 233 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**Outlined · pending_review.** This estimate controls a Gaussian term at a fixed lattice unit by its main term and explicit losses. The varying slope quantity left on the right is a weighted mean on that unit. A later estimate bounds this mean using counts.

## Claim and hypotheses

Under the ten size, division, comparison, counting, slope, height and finite-parameter assumptions, Ga(u) is at most Main(u)+log|W(u)|+K0v5+M plus (1−delBar) inverse times [4 log(1+x\textasciicircum{}cHH)(K3+M+b)+(etaBar+4sqrt(eBar))x\textasciicircum{}cHH b], where M is the weighted mean of Lo5.
$$
\mathrm{Ga}(u)\le \mathrm{Main}(u)+\log|W_u|+K_{0,v5}+M+\frac{4\log(1+x^{c_{HH}})(K_3+M+b)+(\bar\eta+4\sqrt{\bar e})\,x^{c_{HH}}b}{1-\bar\delta}.
$$

[`Formalism.LFunctionChainParameters.WeightedSlopeBounds.Ga_bound5` · `LevelOfCongruence.lean:113–160`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SizeWindowBrackets/ChainSlopeWindows/LevelOfCongruence.lean#L113-L160)

## Keep the two intermediate estimates distinct

Fix the unit $u_0$ and put $M=\operatorname{wmean}(d(u_0),\mathrm{Lo5}(u_0,-))$. The division and quotient-slope inequalities, counting and exponent estimates bound the mean slope $s$ below in terms of $\mathrm{Ga}$, a comparison slope, $K_5$ and $M$. In this step the lower count bound on the logarithm of $T$ is multiplied by a nonnegative sum of coefficients. Separately compare the maximal slope at one index to the average at the same unit. Exponent variation, height comparison and pairwise count control give $u_F\le K_3+M$. These are different uses of the input estimates. [`Formalism.LFunctionChainParameters.WeightedSlopeBounds.s_lower5` · `LevelOfCongruence.lean:50–66`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SizeWindowBrackets/ChainSlopeWindows/LevelOfCongruence.lean#L50-L66) [`Formalism.LFunctionChainParameters.WeightedSlopeBounds.u_function_le_mean` · `LevelOfCongruence.lean:81–103`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SizeWindowBrackets/ChainSlopeWindows/LevelOfCongruence.lean#L81-L103)

## Insert the main term and compare the losses

The exact identity rewrites the relevant division expression as the main term plus an explicit counting cost. It needs positive $v$, positive $f$ and positive individual weights from the setting. The finite-parameter and height bounds license the slope inequality. The logarithmic loss uses $u_F\ge 0$, the bound on $u_F$, and a positive $x^{c_{HH}}$. A second loss is the product of the height with $\eta+4\sqrt e$. Its coefficient and the height are nonnegative. Replace first the coefficient by its uniform upper bound and then the height by $x^{c_{HH}}b$. [`Formalism.LFunctionChainParameters.WeightedSlopeBounds.key_identity5` · `LevelOfCongruence.lean:105–111`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SizeWindowBrackets/ChainSlopeWindows/LevelOfCongruence.lean#L105-L111) [`Formalism.LFunctionChainParameters.WeightedSlopeBounds.Ga_bound5` · `LevelOfCongruence.lean:121–145`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SizeWindowBrackets/ChainSlopeWindows/LevelOfCongruence.lean#L121-L145)

## Preserve the direction of reciprocal comparison

The hypotheses give positive denominators $1-\delta(u_0)$ and $1-\bar\delta$, with the latter no larger. Taking reciprocals bounds the local reciprocal above by the uniform one. Both original losses are nonnegative, so multiplying their sum by the larger reciprocal preserves an upper bound. The uniform reciprocal is also nonnegative, allowing replacement of the terms inside the brackets. Expanding $K_5$ and $K_0$ gives the claimed bound by collecting terms. [`Formalism.LFunctionChainParameters.WeightedSlopeBounds.Ga_bound5` · `LevelOfCongruence.lean:130–160`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SizeWindowBrackets/ChainSlopeWindows/LevelOfCongruence.lean#L130-L160)

## What remains to use the estimate

The inputs include division, exponent and height comparisons, a count estimate, two kinds of slope bounds, the slope inequality, the height bound and finite-parameter bounds, for the same data. The result still contains $M$ both additively and inside the bracket. Downstream the coefficient multiplying $M$ is checked to be nonnegative before inserting the mean bound. This outline traces substitutions subject to the listed hypotheses; their supply is a separate question for an arithmetic family. [`Formalism.LFunctionChainParameters.WeightedSlopeBounds.each_unit_bound_statement` · `LevelOfCongruence.lean:175–192`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SizeWindowBrackets/ChainSlopeWindows/LevelOfCongruence.lean#L175-L192)

## First step to challenge

Check nonnegativity of the entire error before replacing its inverse denominator by the uniform upper bound. Comparing the denominators alone does not justify multiplication.

Use [D570](../../units/D570.md) for the weighted mean and [P021](../../units/P021.md) for the pointwise lattice application.

The final three lines place the pointwise reciprocal estimate inside the error bracket and use `linarith` to collect the remaining terms. `Formalism.LFunctionChainParameters.WeightedSlopeBounds.Ga_bound5` (`Formalism/SizeWindowBrackets/ChainSlopeWindows/LevelOfCongruence.lean:158–160`).
