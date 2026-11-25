# T01 · From matched theta data to the half-plane

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 4,409,174 dominated core lines (index size). **top-level map only**.

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**Outlined · pending_review.** Matching and agreement of the theta integrals, together with the third-place, reciprocity, covolume and Selmer-window hypotheses, imply the stated half-plane nonvanishing for Dirichlet characters. The theta side supplies a definite-side witness, while the window enters the final implication separately.

## Statement and hypotheses

Assume $P,F$, local matching, agreement of theta integrals, the closed
covolume bound of T13, the reciprocity existence assertion $h$, and the
primitive-character window with constant $401$. Then for every $N\ge1$,
every complex Dirichlet character $\chi$ modulo $N$, and every $s$ with
$\Re s>1/2$, one has $L(s,\chi)\ne0$ whenever $\chi\ne\chi_0$ or $s\ne1$.
Here $h$ proves that a compatible reciprocity map exists for each place in the quantified setting. The two theta assumptions
are the two conclusions stated in T11. [`every_character_of_theta_integrals_local_matching` · `SiegelEisensteinSecondTermHypotheses.lean:69-73`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SiegelEisensteinSecondTermHypotheses.lean#L69-L73)

The third-place record $P$ has 60 fields including assertions named for Clozel, Green and Casselman–Wallach. The local theta record $F$ has 53 fields including real Howe duality and Kudla splitting. Their definitions give the individual types. `GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses` (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:22–82`). `GlobalTheory.FunPr.ThetaLocalInputs` (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/BernsteinUnitaryProductIrreducible.lean:6–59`).

**Read alongside** [T09 · Separation on the evaluation grid](../../units/T09.md) · [T10 · The constant-function fit from theta and Hecke functionals](../../units/T10.md) · [T11 · Simultaneous global theta-integral comparison and local matching](../../units/T11.md) · [T13 · Arithmetic inputs for the covolume bound](../../units/T13.md) · [T03 · Building the definite-side family from unramified row data](../../units/T03.md) · [V4-COND · Conditional passage from Selmer and definite-side data to the five public goals](../../units/V4-COND.md).

## Extract the two row tests

Fix the third-place input $P$, the local theta input, the two Weil-model comparison hypotheses, the closed covolume bound and a proof of `RecTExists`. Separation uses `GlobalTheory.Hk3.howeUnram_holds`, an in-repo constant, and the field `P.siegelWeilUnitaryConvergent`. `GlobalTheory.Hk3.howeUnram_holds` (`Development/AbelianVarietyTheory/Proofs/SatakeParameters/RhoMemOfMkEq.lean:250–256`). `UpperTheory.Lit.nonempty_hyps_definite_side_of_closed_bound` (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SiegelEisensteinSecondTermHypotheses.lean:46–49`). These support the construction of a rational row test with finite-group, join and functional-equation inputs from $P$. Use the same comparisons and separation, together with the lower-weight part of the third-place input, for the constant-function fit. One branch concerns rationality of the tested rows; the other controls a numerical functional. [`nonempty_hyps_definite_side_of_closed_bound` · `SiegelEisensteinSecondTermHypotheses.lean:44-54`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SiegelEisensteinSecondTermHypotheses.lean#L44-L54)

## Choose the grid once

Grid existence uses convergence of the twisted Weil model, matching of its local factors, square-integral agreement and the separating functionals. The row functional independently gives a grid threshold of its own. Choose the maximum of the two thresholds and establish eventual grid availability there. Build the open conditions at that dependence parameter. Project the stronger extension down to the earlier one and transport the open conditions. The row-functional assertion applies on the stronger extension with the very same grid threshold. The maximum has to be taken before the later family data enter. [`nonempty_hyps_definite_side_of_closed_bound` · `SiegelEisensteinSecondTermHypotheses.lean:52-64`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SiegelEisensteinSecondTermHypotheses.lean#L52-L64)

## Obtain the definite-side input

Use the closed covolume bound, the harmonic-analysis and ray-class fields of $P$, and the transported open conditions to construct the third-layer linkage. The small-prime norm condition is available at the chosen dependence parameter from the reciprocity theorem and the norm-link field of $P$. These fit the rational row, grid, functional and covolume arguments of the witness constructor. The result says that the definite-side record is inhabited. It keeps the shared family and selection needed in the subsequent deduction. [`nonempty_hyps_definite_side_of_closed_bound` · `SiegelEisensteinSecondTermHypotheses.lean:63-68`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SiegelEisensteinSecondTermHypotheses.lean#L63-L68) · [`every_character_of_theta_integrals_local_matching` · `SiegelEisensteinSecondTermHypotheses.lean:69-73`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SiegelEisensteinSecondTermHypotheses.lean#L69-L73)

## Apply the character implication

Finally extract Green's finite-group input from the regular-character hypothesis. Combine it with the separately assumed primitive-character window and the definite-side witness. This produces the stated conditional character conclusion, including the exception at the principal pole. The symbol for the local theta hypotheses in the initial comparison and the definite-side nonemptiness obtained much later designate different inputs. The two pillar pages track the window and the definite-side witness at the interface with the final implication. [`every_character_of_theta_integrals_local_matching` · `SiegelEisensteinSecondTermHypotheses.lean:69-73`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SiegelEisensteinSecondTermHypotheses.lean#L69-L73)

The final application `every_character_of_green_v_win` takes the entire V window as a premise together with Green and the definite-side package. Its construction belongs to the separate [pillar V](../../pillars/V.md) reading map. `UpperTheory.Top.every_character_of_green_v_win` (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TopPlug.lean:16–18`). `UpperTheory.Lit.every_character_of_theta_integrals_local_matching` (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SiegelEisensteinSecondTermHypotheses.lean:69–73`).

The parameter `hL` is a proof of the existence statement `RecTExists`. Its local witness is under an existential quantifier. `UpperTheory.Zero.LLC.RecTExists` (`Development/AutomorphicArithmetic/Foundations/LocalLanglands/IsRecTOfIsRec.lean:78–80`). `UpperTheory.Lit.every_character_of_theta_integrals_local_matching` (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/SiegelEisensteinSecondTermHypotheses.lean:69–73`).

## Literature-named inputs

`GlobalTheory.Hk3.howeUnram_holds` — in-repo constant (`Development/AbelianVarietyTheory/Proofs/SatakeParameters/RhoMemOfMkEq.lean:250–256`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.siegelWeilUnitaryConvergent` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:33`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.greenRegularCharacters` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:50`); not compared.

`GlobalTheory.GreenBridge.green_of_regular` — in-repo constant (`Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/SumRangeEqRoots.lean:225–304`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.greenCuspidal` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:24`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.discreteSeriesCover` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:57`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.harishChandraModules` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:58`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.cuspRapidDecay` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:31`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.casselmanWallach` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:59`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.rayClassFieldSt` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:52`); not compared.

`GlobalTheory.FunPr.ThetaLocalInputs.siegelSetUnitary` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/BernsteinUnitaryProductIrreducible.lean:58`); not compared.

`GlobalTheory.FunPr.ThetaLocalInputs.howeDualityReal` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/BernsteinUnitaryProductIrreducible.lean:57`); not compared.

`UpperTheory.Lit.functionalsSeparate_of_howeUnram_of_siegelWeil` — in-repo constant (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/FunctionalsSeparateOfHoweUnramOfSiegelWeil.lean:17–19`); not compared.

**First step to challenge.** At the common grid threshold, check that the open, functional, small-prime and covolume assertions refer to the same strengthened extension.

[Unit record and exact statement](../../units/T01.md)
