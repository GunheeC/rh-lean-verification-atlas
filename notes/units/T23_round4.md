# T23 · Nef growth of the chart lattice

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 769 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**Outlined · pending_review.** For a nef multidegree, the ranks of the normed chart lattices have a leading term determined by the generic degree. The argument sandwiches those ranks between ordinary section ranks with two fixed twists, preserving the particular chart lattice needed for the volume comparison.

## Claim and hypotheses

Let $y$ be a birational
multihomogeneous presentation in a characteristic-zero field with
arithmetic variety $P$ of dimension $D+1$, and let the integral
multidegree $a$ be nef on the generic fibre. Put
$V_n=\operatorname{span}_{\mathbb Q}(\mathrm{chartLatNm}(y,a,n))$.
Each $V_n$ is finite-dimensional and
$$
 \lim_{n\to\infty} \frac{D!\,\dim_{\mathbb Q}V_n}{n^D}
       =\mathrm{genDeg}(P,D,a).
$$

[`UpperTheory.LiteratureTheorems.nef_rr_of_literature` · `EveryCharacterOfLiteratureOfVWin.lean:551–552`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean#L551-L552)

## Identify the normalized sequence

Fix a finite multihomogeneous coordinate presentation $y$ over a characteristic-zero field, a birationality witness and the nef multidegree $a$. Write $V_\tau$ for the rational span of its normed chart lattice. The claim gives finite dimension for every $\tau$ and the indicated real limit after multiplying by $D!$ and dividing by $\tau^D$. This is a rank asymptotic for fixed data. The degree-zero-dimensional case is dispatched by a separate model lemma before any positive-dimensional estimates are invoked. The record argument of the outer wrapper is unused. [`GlobalTheory.CompanionTheory.Ar.Pub.NefRR` · `NefRR.lean:8–14`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicSpectrum/PublishedTheorems/Geometry₂/NefRR.lean#L8-L14) [`PositivityTheory.Tls2.Nef.nefRR` · `NefRR.lean:14–20`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/TemperedRepresentationTheory/NefDivisors/NefRR.lean#L14-L20)

## Inject the normed chart into an ordinary chart with fixed twist

When $D>0$ the twist-shift theorem returns a multidegree $e$ and a nonzero scalar $c$. Multiplication by $c$ is an injective rational linear map on the field. Its image on $V_\tau$ lies in the ordinary chart space in multidegree $\tau a+e$. This comparison is simultaneous over powers, so the same twist is available for the asymptotic theorem. The ordinary chart space is finite-dimensional. Its subspace containing the injected image therefore proves that $V_\tau$ is finite-dimensional, via its isomorphism to that image. [`PositivityTheory.Tls2.Nef.nefRR` · `NefRR.lean:18–30`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/TemperedRepresentationTheory/NefDivisors/NefRR.lean#L18-L30)

## Bound the rank in both directions

For the upper bound use invariance of rank under this injection onto its image, followed by monotonicity of finite-dimensional rank under inclusion. For the lower bound no multiplication is needed. The ordinary chart at the unshifted multidegree $\tau a$ is a subspace of the rational span of the normed chart. Rank monotonicity in this other inclusion gives the opposite inequality. The lower and upper spaces thus use the twists zero and $e$, respectively. Their comparison does not identify them with one another at individual degrees. [`PositivityTheory.Tls2.Nef.nefRR` · `NefRR.lean:31–44`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/TemperedRepresentationTheory/NefDivisors/NefRR.lean#L31-L44)

## Squeeze only after normalization

For a prescribed positive tolerance use the nef sections lower estimate with twist zero and the chart dimension upper estimate with twist $e$. Each eventually bounds the appropriate endpoint in the rank sandwich. Transitivity gives both eventual bounds for the real rank of $V_\tau$ itself, and the asymptotic-bounds lemma yields the limit with the required normalization. The rank comparisons and the squeeze are elementary parts of the deduction. The source of the nef lower estimate, the fixed-twist upper estimate and the dimension-zero model remain separate inputs to this outline. [`PositivityTheory.Tls2.Nef.nefRR` · `NefRR.lean:45–52`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/TemperedRepresentationTheory/NefDivisors/NefRR.lean#L45-L52)

## First step to challenge

Check that one twist and one nonzero multiplier control the entire upper inclusion for every power. A choice depending on the power would prevent direct application of the fixed-twist asymptotic bound.

Compare [T18](../../units/T18.md), where the objects being counted are small sections, and [T26](../../units/T26.md), which uses the rank asymptotic for nef data.

The Lean head takes the open-literature record and does not use it. `UpperTheory.LiteratureTheorems.nef_rr_of_literature` (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean:551–552`).

## Literature-named inputs

`PositivityTheory.Tls2.Nef.nefRR` — in-repo constant (`Development/WeilBound/CoreStatements/TemperedRepresentationTheory/NefDivisors/NefRR.lean:14–52`); not compared.

`GlobalTheory.CompanionTheory.Ar.Pub.NefRRModel.nefRR_dimZero` — in-repo constant (`Development/AutomorphicSpectrum/PublishedTheorems/Geometry₂/ProjLineLimit.lean:93–116`); not compared.
