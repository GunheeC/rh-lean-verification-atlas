# T08 · The twelve linked conditions at dependence parameters

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 169,776 dominated core lines (index size). **top-level map only**.

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**Outlined · pending_review.** At any chosen dependence parameter, the third-place unitary hypotheses yield twelve open conditions on linked rows. Their shared parameter lets the all-row construction use geometric compatibility, type labels, multiplicities and the other row fields together.

## Statement and hypotheses

Given $P$, every proof $h$ of `RecTExists` and every real $c$, the following
twelve conditions are linked at $p(c)$: primitivity, lambda-prime bounds,
divisors, decomposition points, selection jumps, ties, labels, goodness,
weak geometric compatibility, multiplicities, kappa and defect. In
particular the geometric field supplies a comparison with the prescribed
point summands, class-sum normalization, point compatibility and the
additional point condition `More`. [`open0_of_unitary_group_hypotheses` · `OpenOrbitOfUnramifiedExponents.lean:75-76`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/OpenOrbitOfUnramifiedExponents.lean#L75-L76)

**Read alongside** [T03 · Building the definite-side family from unramified row data](../../units/T03.md) · [T04 · All 26 large-slot conditions from the open conditions](../../units/T04.md) · [T09 · Separation on the evaluation grid](../../units/T09.md).

## Set up the common extension

Fix the proof of reciprocity existence and a real dependence parameter. Every element of the extension with list projects to an inhabitant of the extension with law. At each of its points there is also a recorded bookkeeping law. Obtain the primitive and decomposition-point conditions by their two direct constructions. The real tie uses the extension-with-law witness together with discrete-series, Harish–Chandra, Weil and globalization inputs. Combine the primitive and decomposition data with the tie to obtain the jumps. The presence of the common extension in these calls matters more than the final ordering of the twelve fields. [`open_orbit_of_unramified_exponents_alt` · `OpenOrbitOfUnramifiedExponents.lean:39-49`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/OpenOrbitOfUnramifiedExponents.lean#L39-L49)

## Multiplicity, divisor and prime data

The third-place multiplicity calculation applies the in-repo constant `GlobalTheory.Hk3.howeUnram_holds` and fields of $P$ for the Weil and Siegel–Weil formulas, doubling, classification and strong approximation. Its two components have distinct uses. Combine its first component with the bookkeeping law to obtain the divisor entry. The real-group calculation gives the lambda-prime entry, using both local representation theory and the finite-group input. Feed that entry into the Harish–Chandra calculation giving kappa. The second component from the multiplicity input remains available for the final tuple. The two uses need not be deduced from one another. [`open_orbit_of_unramified_exponents_alt` · `OpenOrbitOfUnramifiedExponents.lean:50-63`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/OpenOrbitOfUnramifiedExponents.lean#L50-L63)

## Tie goodness to geometry

The goodness supplier combines the inhabited extension with the finite-group result from Green regular characters and the Zelevinsky field. `GlobalTheory.Fc.S0.Open0ProofU.open_orbit_of_unramified_exponents_alt` (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/OpenOrbitOfUnramifiedExponents.lean:64–64`).

The label supplier takes the first component of goodness on this same extension. `GlobalTheory.Fc.S0.Open0ProofU.open_orbit_of_unramified_exponents_alt` (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/OpenOrbitOfUnramifiedExponents.lean:65–65`).

The ray-class-field input, divisor assertion and tie supply the weak geometric field. `GlobalTheory.Fc.S0.Open0ProofU.open_orbit_of_unramified_exponents_alt` (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/OpenOrbitOfUnramifiedExponents.lean:66–66`).

The defect field comes from the Weil-unitary calculation on the fixed extension. `GlobalTheory.Fc.S0.Open0ProofU.open_orbit_of_unramified_exponents_alt` (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/OpenOrbitOfUnramifiedExponents.lean:67–68`).

The lambda-prime assertion is passed to the Harish–Chandra calculation to obtain kappa. `GlobalTheory.Fc.S0.Open0ProofU.open_orbit_of_unramified_exponents_alt` (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/OpenOrbitOfUnramifiedExponents.lean:56–63`).

The assembled tuple takes the second components of goodness and multiplicity and the already constructed labels, geometry, kappa and defect. `GlobalTheory.Fc.S0.Open0ProofU.open_orbit_of_unramified_exponents_alt` (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/OpenOrbitOfUnramifiedExponents.lean:69–69`).

## Downstream use

The definite-side construction first gets these fields at the dependence parameters. It then uses extension monotonicity before applying the all-row constructor. A check on a particular open field belongs here if it concerns the initial construction; compatibility with a retwisting extension belongs to the subsequent transport. [`hypotheses_nonempty_of_unramified_exponents_alt` · `HypothesesNonemptyOfUnramifiedExponents.lean:45-56`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/HypothesesNonemptyOfUnramifiedExponents.lean#L45-L56)

The parameter `hL` is a proof of the existence statement `RecTExists`. Its local witness is under an existential quantifier. `UpperTheory.Zero.LLC.RecTExists` (`Development/AutomorphicArithmetic/Foundations/LocalLanglands/IsRecTOfIsRec.lean:78–80`). `GlobalTheory.T.open0_of_unitary_group_hypotheses` (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/OpenOrbitOfUnramifiedExponents.lean:75–76`).

## Literature-named inputs

`GlobalTheory.Hk3.howeUnram_holds` — in-repo constant (`Development/AbelianVarietyTheory/Proofs/SatakeParameters/RhoMemOfMkEq.lean:250–256`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.discreteSeriesCover` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:57`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.harishChandraModules` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:58`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.casselmanWallach` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:59`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.weilRepresentationUnitaryPair` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:60`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.discreteSeriesExists` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:61`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.harishChandraFinite` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:49`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.cuspRapidDecay` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:31`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.weilSiegelFormulaUnitary` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:32`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.siegelWeilUnitaryConvergent` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:33`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.doublingMethod` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:34`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.unramifiedDoublingGL` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:35`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.discreteSeriesClassification` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:62`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.strongApproxSU` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:63`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.siegelWeilUnitaryConvergent2` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:64`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.harishChandraAnalyticity` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:65`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.cuspTraceClass` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:66`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.dixmierMalliavinFactorisation` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:67`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.flathFactorisation` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:68`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.zelevinskyPolynomialRing` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:51`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.greenCuspidal` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:24`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.greenRegularCharacters` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:50`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.rayClassFieldSt` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:52`); not compared.

`GlobalTheory.T.harish_chandra_inputs_combined_alt_alt` — in-repo constant (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/HarishChandraInputsCombined.lean:56–57`); not compared.

`GlobalTheory.T.linked_bundles_good_of_local_langlands_alt_alt` — in-repo constant (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkedBundlesGoodOfLocalLanglands.lean:96–97`); not compared.

`GlobalTheory.GreenBridge.green_of_regular` — in-repo constant (`Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/SumRangeEqRoots.lean:225–304`); not compared.

**First step to challenge.** Check the geometric-tie field on the actual dependence extension. It needs the previously obtained divisor and tie records for the same reciprocity choice.

[Unit record and exact statement](../../units/T08.md)
