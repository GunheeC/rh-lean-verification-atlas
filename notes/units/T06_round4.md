# T06 · Lattice masses, automorphic membership and existence of linked bundles

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 280,670 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**Outlined · pending_review.** The same extension supplies automorphic membership and eventual linked-bundle existence, and the third-place hypotheses also give the standard CM lattice mass ratio. The definite-side construction needs all three outputs, including the nonemptiness assertion at its selected slots.

## Statement and hypotheses

Assume $P$ and row rationality. For any $h,c,A$ as in T03 with $A$
eventually large, three conclusions hold. For every unramified CM datum and
$M\ge3$ the ratio of standard lattice masses in ranks $M$ and $M-1$ equals
the prescribed `massRatioRightSide`. At $p_A(c)$ one has the base,
first stage, export and second stage of automorphic membership. Finally, there
is a large-base slot $R$ such that eventually every constructed point of
the good slot intersected with $R$ admits, at every real scale, a bundle
with the specified linkage. [`large_unramified_exponent_bundles_exist_alt` · `MemberBundlesLargeUnramifiedExponents.lean:69-70`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MemberBundlesLargeUnramifiedExponents.lean#L69-L70)

**Read alongside** [T03 · Building the definite-side family from unramified row data](../../units/T03.md) · [T08 · The twelve linked conditions at dependence parameters](../../units/T08.md) · [D415 · Injectivity of the adjoint theta scalar formula](../../units/D415.md).

## Build membership hypotheses in two layers

Fix the third-place unitary input, rationality for the specified rows, a proof of `RecTExists`, a dependence parameter and an eventually large retwisting predicate. The first membership package comes from global reciprocity, CM-curve and Weber-field hypotheses, the discrete-series and harmonic-analysis fields, the compact-dual formal degree and the convergent formula. A second package gathers analyticity, cusp trace class, the two factorization results, Zelevinsky, the geometric lemma and Green's cuspidal input. At this point the mass-ratio datum is already present in the first package. It is read out separately from the automorphic assertions. [`member_bundles_large_unramified_exponents_alt` · `MemberBundlesLargeUnramifiedExponents.lean:34-49`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MemberBundlesLargeUnramifiedExponents.lean#L34-L49)

## Use rationality to control the weights

With the second package, combine row rationality with the Weil and Siegel–Weil formulas, continuation and pole inputs, unramified doubling, finiteness and orthogonality to get rational weights for membership. The saturation statement for weight one uses the first package together with this rational-weight result. Next obtain multiplicative closure of membership on the unstrengthened origin extension. This step uses the listed representation-theoretic fields and the same proof of `RecTExists`. It prepares passage from base-lattice existence to membership for the specified extension. [`member_bundles_large_unramified_exponents_alt` · `MemberBundlesLargeUnramifiedExponents.lean:47-58`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MemberBundlesLargeUnramifiedExponents.lean#L47-L58)

## Give the three witnesses

The third-layer Galois construction supplies the fields required for base-lattice membership. Project the mass-ratio field from the first package. For automorphic membership, first apply the base-lattice existence result with rationality, saturation and multiplicative closure. Its membership component passes to the extension with the added predicate by eventual availability. For linked-bundle existence apply the separate nonempty-Weil-block result with the same retwisting extension, the projection from its data, and the corresponding origin slot movement. The last result has its own large-base slot and asks for linked bundles at eligible built points and real scales. [`member_bundles_large_unramified_exponents_alt` · `MemberBundlesLargeUnramifiedExponents.lean:59-63`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MemberBundlesLargeUnramifiedExponents.lean#L59-L63)

## How the conclusions enter separately

The definite-side constructor takes the three projections in different positions. The mass identity participates in the global package, the membership projection provides the common membership predicate, and the existential bundle record supplies realizations. Replacing these with independent existence results would need a comparison between their slots and linkage. This outline exposes that compatibility requirement and leaves the lower automorphic existence and saturation results as named inputs. [`hypotheses_nonempty_of_unramified_exponents_alt` · `HypothesesNonemptyOfUnramifiedExponents.lean:41-46`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/HypothesesNonemptyOfUnramifiedExponents.lean#L41-L46) · [`hypotheses_nonempty_of_unramified_exponents_alt` · `HypothesesNonemptyOfUnramifiedExponents.lean:54-61`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/HypothesesNonemptyOfUnramifiedExponents.lean#L54-L61)

The parameter `hL` is a proof of the existence statement `RecTExists`. Its local witness is under an existential quantifier. `UpperTheory.Zero.LLC.RecTExists` (`Development/AutomorphicArithmetic/Foundations/LocalLanglands/IsRecTOfIsRec.lean:78–80`). `GlobalTheory.T.large_unramified_exponent_bundles_exist_alt` (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MemberBundlesLargeUnramifiedExponents.lean:69–70`).

**Scope of the hypotheses.** The note retains the source’s named predicates and records. For the exact quantified assumptions at this head, read `GlobalTheory.T.large_unramified_exponent_bundles_exist_alt` (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MemberBundlesLargeUnramifiedExponents.lean:69–70`). Their internal definitions are separate reading tasks.

## Literature-named inputs

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.siegelWeilUnitaryConvergent2` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:64`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.globalArtinReciprocity` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:46`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.cMCurveGoodOutsidePrimeSt` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:69`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.weberRayFieldSt` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:70`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.harishChandraModules` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:58`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.cuspRapidDecay` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:31`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.casselmanWallach` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:59`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.harishChandraFinite` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:49`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.discreteSeriesClassification` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:62`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.discreteSeriesCoverExists` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:71`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.formalDegreeCompactDual` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:37`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.harishChandraAnalyticity` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:65`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.cuspTraceClass` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:66`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.dixmierMalliavinFactorisation` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:67`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.flathFactorisation` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:68`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.zelevinskyPolynomialRing` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:51`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.greenCuspidal` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:24`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.discreteSeriesCover` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:57`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.weilSiegelFormulaUnitary` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:32`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.siegelWeilUnitarySchrodinger` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:72`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.siegelEisensteinContinuation` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:73`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.siegelEisensteinSimplePole` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:74`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.unramifiedDoublingGL` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:35`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.bernsteinZelevinskyFiniteness` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:36`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.schurOrthogonalitySquareIntegrable` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:75`); not compared.

**First step to challenge.** Check that the base membership theorem and the nonempty Weil block both apply with the same origin, geometry and retwisting predicate.

[Unit record and exact statement](../../units/T06.md)
