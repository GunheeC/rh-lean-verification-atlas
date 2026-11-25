# T21 · Integrated Poincaré–Lelong identity

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 18 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**Outlined · pending_review.** An integral containing the logarithm of a section norm splits into a sum over horizontal divisor components and a curvature term. This identity is the input used when an arithmetic intersection computation replaces a section by its divisor, including its multiplicities.

## Claim and hypotheses

Let $P$ have arithmetic dimension $n+2$
in a finite multihomogeneous coordinate ring, and let
$L_1,\ldots,L_n,A,B$ be smooth conjugation-invariant Hermitian lines.
Assume $B$ has zero multidegree and $s$ is a section of $A$ on $P$.
Write $J_Z(\omega;f)$ for the project's point integral on $Z$ with
potential list $\omega$ and integrand $f$, and $\omega_L$ for the
potentials of the $L_i$. With $b=\log h_B$ and $a=\log h_A$,
$$
 J_P((b,\omega_L);\log\|s\|_A)=
   \sum_{W\ \mathrm{horizontal~in~div}(s)}^{\mathrm{fin}}
       \mathrm{mult}_{W}(P+(s))J_W(\omega_L;b)
     -J_P((a,\omega_L);b).
$$

[`UpperTheory.LiteratureTheorems.poincare_lelong_inv_of_literature` · `EveryCharacterOfLiteratureOfVWin.lean:553–554`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean#L553-L554)

## Identify the sign and the divisor being measured

There are two distinguished lines in addition to the $n$ smooth test lines. The log norm on the left belongs to the section $s$ of $A$. The first potential is the log metric on $B$, whose multidegree is zero. On the right the horizontal part of the divisor of $s$ integrates that latter function against the other potentials. Its coefficients are multiplicities of $P+(s)$. The last integral has potential from $A$ and the same log metric from $B$, and is subtracted. Conjugation invariance and smoothness are assumptions on the indicated lines in this version. [`GlobalTheory.CompanionTheory.Hypotheses₂.PoincareLelongInv` · `PoincareLelongInv.lean:9–18`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicSpectrum/PublishedTheorems/Metrics₂/PoincareLelongInv.lean#L9-L18)

## Control the singular locus before passing to a limit

The supplied analytic ingredients include a description of divisor branches at general points, a local order result and the Lelong limit along each branch. These give the required limit at good points. A second estimate controls regular mass near the smaller exceptional locus, together with the corresponding variety mass. Additivity of the integrals joins the estimates on and off the zero set. Stokes on the variety has its own tube-mass bound, using a rank-one contribution and an area/count bound. The limiting argument depends on these estimates; the mere pointwise formula away from zeros omits the divisor mass. [`PositivityTheory.Tls2.Pl.lelongLimit` · `Development.lean:48–58`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/TemperedRepresentationTheory/PoincareLelong/Development.lean#L48-L58) [`PositivityTheory.Tls2.Pl.stokesOnVariety` · `Development.lean:40–46`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/TemperedRepresentationTheory/PoincareLelong/Development.lean#L40-L46)

## Recover the algebraic weights and integrate on charts

A weighted polynomial version of the limit uses the local multiplicity comparison for comaps, the weight limit and Stokes. On the global side the proof gets integrability from absolute integrability and measurability. A Segre partition and the chart integral supply the Stokes identity in the arithmetic coordinates. The chart limit then combines the polynomial limit with the comparison of algebraic and chart divisors. Apply the regularized identity and its limit to recover the full formula. These steps explain the origin of the horizontal component coefficients; the geometric comparisons themselves remain named inputs. [`PositivityTheory.Tls2.Pl.lelongPolyLimit` · `Development.lean:60–64`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/TemperedRepresentationTheory/PoincareLelong/Development.lean#L60-L64) [`PositivityTheory.Tls2.Pl.poincareLelong_of` · `Development.lean:70–84`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/TemperedRepresentationTheory/PoincareLelong/Development.lean#L70-L84)

## Specialize to the invariant statement

The more general arithmetic formula receives the smoothness, arithmetic-variety, zero-multidegree and section conditions. The specialized conjugation-invariant statement supplies these directly; the adapter discards the three invariance hypotheses while applying the stronger result. The wrapper returns the in-repo constant `PositivityTheory.Tls2.Pl.poincareLelongInv` independently of the argument. Thus the final step is substitution, while the analytic content is already in the separate chart, branch and limit estimates. [`PositivityTheory.Tls2.Pl.poincareLelongInv_of_leaves` · `Development.lean:95–105`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/TemperedRepresentationTheory/PoincareLelong/Development.lean#L95-L105) [`PositivityTheory.Tls2.Pl.poincareLelongInv` · `PoincareLelongInv.lean:19–23`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/TemperedRepresentationTheory/PoincareLelong/PoincareLelongInv.lean#L19-L23)

## First step to challenge

Check the passage from branchwise Lelong limits to the full divisor integral. The estimate near the exceptional set must preserve the local orders that become horizontal multiplicities.

See [T18](../../units/T18.md) for the use of the resulting intersection system and [T17](../../units/T17.md) for its volume comparison.

The Lean head takes the open-literature record and does not use it. `UpperTheory.LiteratureTheorems.poincare_lelong_inv_of_literature` (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean:553–554`).

## Literature-named inputs

`PositivityTheory.Tls2.Pl.poincareLelongInv` — in-repo constant (`Development/WeilBound/CoreStatements/TemperedRepresentationTheory/PoincareLelong/PoincareLelongInv.lean:19–23`); not compared.

`UpperTheory.LiteratureTheorems.poincare_lelong_inv_of_literature` — in-repo constant (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean:553–554`); not compared.

`PositivityTheory.Tls2.Pl.poincareLelong_of` — in-repo constant (`Development/WeilBound/CoreStatements/TemperedRepresentationTheory/PoincareLelong/Development.lean:70–84`); not compared.

`PositivityTheory.Tls2.Pl.poincareLelongInv_of_leaves` — in-repo constant (`Development/WeilBound/CoreStatements/TemperedRepresentationTheory/PoincareLelong/Development.lean:95–105`); not compared.
