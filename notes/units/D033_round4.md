# D033 · Uniform row bounds from convergent Siegel–Weil

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 1,500 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**Outlined · pending_review.** The convergent unitary Siegel–Weil input supplies a uniform bound on the contribution from nonzero nongeneric terms in the same row for tied two-word data. Its constants are chosen before the row and test data, so later row estimates can use the same error scale.

## Statement and hypotheses

The convergent unitary Siegel–Weil input supplies a common nonnegative row-error constant and two largeness thresholds for each set of admissible parameters. Every tied, standard two-word datum satisfying Hyp0 and absolute convergence has the required bound for the normalized sum of real inner products over pairs of nonzero nongeneric terms in the same row with $s_0=1$ with that error scale.

$$
\mathrm{SiegelWeilUnitaryConvergent}\ \Longrightarrow\ \mathrm{RowNGP}.
$$

[`rowNGP_of_siegelWeil` · `RowPositivityOfSiegelWeil.lean:10-15`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/FlagMeasures/RowPositivityOfSiegelWeil.lean#L10-L15)

**Read alongside** [N076 · Bessel period in the wave grid](../../units/N076.md) · [T03 · Building the definite-side family from unramified row data](../../units/T03.md).

## Identify the nongeneric pairs

Let $Q$ consist of pairs $(t,t')$ with nonzero $G$ on both terms, both terms nongeneric, equal rows and $s_0(t,t')=1$. The estimated quantity is $\Gamma_1\sum_{(t,t')\in Q}\operatorname{Re}\langle v_t,v_{t'}\rangle$. The pair definition imposes no distinctness requirement. Its upper bound is the row-error scale multiplied by the prescribed row normalization. [`ngSet` · `StatementPB.lean:49-49`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/HermitianCurvature/StatementPB.lean#L49-L49) · [`allPairs` · `StatementPB.lean:65-65`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/HermitianCurvature/StatementPB.lean#L65-L65) · [`one` · `StatementPB.lean:69-69`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/HermitianCurvature/StatementPB.lean#L69-L69) · [`pairSum` · `StatementPB.lean:75-76`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/HermitianCurvature/StatementPB.lean#L75-L76) · [`RowNG` · `StatementPB.lean:109-109`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/HermitianCurvature/StatementPB.lean#L109-L109)

## Write down the order of choice

Fix the external row parameters subject to the stated size assumptions. The row assertion supplies a nonnegative error constant and two thresholds. They precede the free scale choices, datum, the two words and the concrete row tests. Standardness, the local row hypotheses and absolute convergence restrict the tests to which the estimate applies. In particular, one cannot choose a convenient error bound from an individual row and then reuse it for another one. The cited definition is the place to compare these quantifiers to the uniform theorem used below. [`RowNGP` · `RowsPos.lean:37-41`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RowsPos.lean#L37-L41) · [`rowNGP_of_siegelWeil` · `RowPositivityOfSiegelWeil.lean:10-15`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/FlagMeasures/RowPositivityOfSiegelWeil.lean#L10-L15)

## Construct the uniform step data

Siegel–Weil provides a choice of mass data. To turn these into the required step choices, use convergence of the product cutoff on tied data and the archimedean assertion at scale one. For the latter specialization the wrapper supplies the concrete real-object result under the gap hypothesis, using the uniqueness-of-gap input and positivity of one. The scale in this application is already fixed, before the row estimate is specialized. Mass data and an archimedean estimate enter this step in different ways. [`stepChoiceDataC_of_siegelWeil_inInfinity` · `StepChoiceConstantsCOfSiegelWeilAtInfinity.lean:9-15`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/FlagMeasures/StepChoiceConstantsCOfSiegelWeilAtInfinity.lean#L9-L15) · [`rowNGP_of_siegelWeil` · `RowPositivityOfSiegelWeil.lean:10-15`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/FlagMeasures/RowPositivityOfSiegelWeil.lean#L10-L15)

## Use the pinned bound on those choices

Apply the closed corank-one nongeneric row bound to the Siegel–Weil data, the uniform step-choice input and the two fields giving the pin and the nongeneric form. Its remaining hypothesis asks for uniform constants in the pinned analytic theorem. Specialize that theorem to the external parameters, obtaining the error constant and thresholds together with their bound. Return these same constants, then pass all the subsequently supplied datum and word variables to the bound. The only weakening in this passage is that the final application needs fewer hypotheses than the row supplied. No maximization over a family of row-specific constants appears. [`rowNGP_of_siegelWeil_of_stepChoice` · `RowPositivityOfSiegelWeilConstants.lean:11-18`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/FlagMeasures/RowPositivityOfSiegelWeilConstants.lean#L11-L18)

## How it enters the row assembly

In the definite-side construction the result enters alongside a distinct assertion for the row main term, a volume ratio, finite-dimensionality and the large-slot rows. An upper error estimate alone cannot supply the whole row condition. To audit the construction, one can check the nongeneric estimate and the main-term identity independently at this interface, then verify that both are specialized with the same convergent formula. [`hypotheses_nonempty_of_unramified_exponents_alt` · `HypothesesNonemptyOfUnramifiedExponents.lean:54-61`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/HypothesesNonemptyOfUnramifiedExponents.lean#L54-L61)

The row bound requires $0<c_b$ and $0<c_T$ before choosing constants. It uses the concrete relation `ConcTie X Y` together with absolute convergence of the very row being estimated. `Formalism.L2.SG.RowsPos.RowNGP` (`Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/RowsPos.lean:37–41`).

## Literature-named inputs

`HeckeCharacterZeroLocus.SiegelWeilU.SiegelWeilUnitaryConvergent` — hypothesis at this head (`Formalism/UnipotentAdelicQuotients/SiegelWeilUnitaryConvergent.lean:46–49`); not compared.

`GlobalTheory.rowNGP_of_siegelWeil` — in-repo constant (`Development/AbelianVarietyTheory/Proofs/FlagMeasures/RowPositivityOfSiegelWeil.lean:10–15`); not compared.

`GlobalTheory.rowNGP_of_siegelWeil_of_stepChoice` — in-repo constant (`Development/AbelianVarietyTheory/Proofs/FlagMeasures/RowPositivityOfSiegelWeilConstants.lean:11–18`); not compared.

`GlobalTheory.St.stepChoiceDataC_of_siegelWeil_inInfinity` — in-repo constant (`Development/AbelianVarietyTheory/Proofs/FlagMeasures/StepChoiceConstantsCOfSiegelWeilAtInfinity.lean:9–15`); not compared.

`GlobalTheory.St.swxs_of_siegelWeil` — in-repo constant (`Development/AbelianVarietyTheory/Proofs/FlagMeasures/SwxsOfSiegelWeil.lean:8–10`); not compared.

**First step to challenge.** Check uniformity of the step-choice bound for all eligible word pairs. A bound obtained after choosing the two words would have the wrong quantifier order.

[Unit record and exact statement](../../units/D033.md)
