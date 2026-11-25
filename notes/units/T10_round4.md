# T10 · The constant-function fit from theta and Hecke functionals

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 62,323 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**Outlined · pending_review.** The theta comparisons, separating tests and lower-weight estimate help turn the automorphic join and functional equation into one functional bound. A threshold for the field grid works before the later family, point and numerical parameter are specified.

## Statement and hypotheses

Assume $F$, the automorphic join, the Hecke--Tate functional equation, both
theta comparisons of T11, separation as in T09, and the lower-weight
assertion of T05. Then some $C_{F,0}$ works for every $C_F\ge C_{F,0}$.
In each admissible family with `DIVinN`, eventually every point
having the prescribed field grid of size $C_F$ satisfies, for every $C$,
the false-side functional bound
$\mu_{\max,RR}\le h_h-\operatorname{meanLog}(\kappa)$
for its numerical data $N(C)$. [`fourier_coefficient_fit_of_join_alt` · `FourierCoefficientFitOfJoin.lean:12-17`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FourierCoefficientFitOfJoin.lean#L12-L17)

**Read alongside** [T09 · Separation on the evaluation grid](../../units/T09.md) · [T11 · Simultaneous global theta-integral comparison and local matching](../../units/T11.md) · [T05 · Two uniform bounds on indefinite rows](../../units/T05.md) · [D024 · Unfolding a twisted theta integral](../../units/D024.md) · [D044 · Agreement of the square-model theta integrals](../../units/D044.md).

## Unpack the join

Keep the local theta inputs, the ordinary integral and matching assertions, separation and the lower-weight bound. Split the automorphic join into its toric denominator, lattice-norm transport, twisted transport, zeta-denominator and reflection data. From Hecke–Tate take the absolute functional equation. The intermediate fit theorem consumes these particular components, so listing only the availability of an automorphic representation would suppress part of the hypothesis. The square leading-term bound gives a collection of estimates and existence data, including smallness and nonvanishing at the bottom, field data and a tower. [`fourier_coefficient_fit_of_join_alt` · `FourierCoefficientFitOfJoin.lean:12-17`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FourierCoefficientFitOfJoin.lean#L12-L17) · [`fittedFunction_at_zero_close_alt` · `FittedFunctionAtZeroClose.lean:42-48`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FittedFunctionAtZeroClose.lean#L42-L48)

## Tie local and global tests

The local theta input alone gives the finite-place, away and infinity estimates. Use the local theta input together with both theta comparisons for the joined local-sum relations. Separation gives injectivity of the tested row map only after combining it with convergence at the real places for cuspidal lifts. Size gives the eligible set of points. The logarithmic derivative bound, denominator bound for the class sum and archimedean bound enter separately. Use twisted transport for a toric ratio estimate. Then deduce that the square ratio belongs to the embedded coefficient field, using the constant relation, nonvanishing input, triple and tower data. [`fittedFunction_at_zero_close_alt` · `FittedFunctionAtZeroClose.lean:49-59`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FittedFunctionAtZeroClose.lean#L49-L59)

## Fit the specified functional

The closure step collects a bundle built from rows and a scaling estimate. The embedded-field result and denominator data provide the function that is to be fitted. Linearity and injectivity with the constant and two-term relations give the map and kernel tie. Finite and away estimates yield the fixed-point input; the infinity and lower-weight estimates supply height and infinite-place bounds. The same aggregation also requires density, integrality, the archimedean tie, theta and weight bounds and final rank, ramified-sum and descent estimates. The lower-weight bound alone controls just one part of this list. [`fittedFunction_at_zero_close_alt` · `FittedFunctionAtZeroClose.lean:60-67`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FittedFunctionAtZeroClose.lean#L60-L67)

## Use the resulting threshold

The next argument obtains a grid threshold for the functional condition and another for the existence of evaluations. Choosing their maximum makes the same grid admissible for both. This illustrates why T10 chooses a threshold before all larger grid sizes and before specializing the family. A fit depending on each individual point would be too weak for that choice. [`nonempty_hyps_definite_side_of_closed_bound` · `SiegelEisensteinSecondTermHypotheses.lean:49-58`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SiegelEisensteinSecondTermHypotheses.lean#L49-L58)

**Scope of the hypotheses.** The note retains the source’s named predicates and records. For the exact quantified assumptions at this head, read `GlobalTheory.BigTop.Fun.Close.fourier_coefficient_fit_of_join_alt` (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FourierCoefficientFitOfJoin.lean:12–17`). Their internal definitions are separate reading tasks.

## Literature-named inputs

`GlobalTheory.Published.HeckeTateFunctionalEquation` — hypothesis at this head (`Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/HeckeTateFunctionalEquationCM.lean:244–249`); not compared.

`GlobalTheory.FunPr.ThetaLocalInputs.howeDualityReal` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/BernsteinUnitaryProductIrreducible.lean:57`); not compared.

**First step to challenge.** Check the production of a function with values in the embedded coefficient field. It uses both the square-ratio assertion and the denominator estimate for that same family.

[Unit record and exact statement](../../units/T10.md)
