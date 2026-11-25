# D024 · Unfolding a twisted theta integral

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 25,645 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**Outlined · pending_review.** For a smooth cuspidal lift with the local theta inputs and existing row sums, the last-row integral agrees with its unfolded expression. The calculation must use the same large-depth cells, measures and test values throughout.

## Statement and hypotheses

The local theta inputs, smooth cuspidal lifts and existence of the row sums give the row unfolding identity at every admitted large-scale datum.

$$
\mathrm{ThetaLocalInputs}\wedge\mathrm{LiftsCuspidal}\wedge\mathrm{SumOKK}\ \Longrightarrow\ \mathrm{StepUnfold}.
$$

[`twisted_theta_integral_unfolds` · `TwistedThetaIntegralUnfolding.lean:37-38`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/TwistedThetaIntegralUnfolding.lean#L37-L38)

**Read alongside** [T10 · The constant-function fit from theta and Hecke functionals](../../units/T10.md) · [D044 · Agreement of the square-model theta integrals](../../units/D044.md).

## Choose a single large-depth regime

The hypotheses supply local theta data, cuspidality of smooth lifts and the row sum condition. The intermediate result first collects the relation between the real iterated integral and the finite expression, passage of cell-sum identities to integrals, and the real/finite splitting of period groups. The iteration along the chain uses the local theta and cuspidal inputs. Combine these eventually valid statements by conjunction and specialize them together. Running each step at a different depth would not yet produce the claimed identity for any one admissible datum. [`twisted_theta_integral_unfolding` · `TwistedThetaIntegralUnfolding.lean:10-19`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/TwistedThetaIntegralUnfolding.lean#L10-L19) · [`twisted_theta_integral_unfolding` · `TwistedThetaIntegralUnfolding.lean:25-30`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/TwistedThetaIntegralUnfolding.lean#L25-L30)

## Identify which cells contribute

At this depth the unfolded integrand is bi-invariant and a flat parameter is available. Use support on cells together with the single-coset description away from twist places, dependence of the definite period on the product function and the basic unfolding hypotheses. The support assertion produced in this way is for the parameter of the selected flat datum. The representation assertions at every place are specialized at the same parameter. This bridges a decomposition of the integration domain and an actual expression for the representative that the row test evaluates. [`twisted_theta_integral_unfolding` · `TwistedThetaIntegralUnfolding.lean:15-22`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/TwistedThetaIntegralUnfolding.lean#L15-L22) · [`twisted_theta_integral_unfolding` · `TwistedThetaIntegralUnfolding.lean:27-30`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/TwistedThetaIntegralUnfolding.lean#L27-L30)

## Evaluate the supported cells

The local cell-value theorem consumes flatness, product dependence, the change of measures for the definite period, the mass identities against level volumes and the reduction to Fock vectors. It also uses the staircase-coset description and existence of the sum. Thus identification of the support never licenses dropping the cell weights. Compute the values with those weights and use the real-line statement for the archimedean integration. Insert this package into the real iterated-integral relation, with its two chain conditions. Passage from the resulting large-depth implication to the unit's statement is direct. [`twisted_theta_integral_unfolding` · `TwistedThetaIntegralUnfolding.lean:19-30`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/TwistedThetaIntegralUnfolding.lean#L19-L30)

## Scope of the comparison

The two antecedents concerning smooth lifts and sums supply different parts of the calculation. Cuspidality is used in the iterated chain result; the sum hypothesis is still passed to the cell-value and final integral relations. The cited source leaves the local support, measure and Fock calculations as named inputs to this assembly. The conclusion gives one row unfolding identity, so comparing two models or proving that its value is nonzero requires additional information. [`twisted_theta_integral_unfolding` · `TwistedThetaIntegralUnfolding.lean:10-14`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/TwistedThetaIntegralUnfolding.lean#L10-L14) · [`twisted_theta_integral_unfolding` · `TwistedThetaIntegralUnfolding.lean:28-30`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/TwistedThetaIntegralUnfolding.lean#L28-L30) · [`twisted_theta_integral_unfolds` · `TwistedThetaIntegralUnfolding.lean:37-38`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/TwistedThetaIntegralUnfolding.lean#L37-L38)

**Scope of the hypotheses.** The note retains the source’s named predicates and records. For the exact quantified assumptions at this head, read `GlobalTheory.T.twisted_theta_integral_unfolds` (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/TwistedThetaIntegralUnfolding.lean:37–38`). Their internal definitions are separate reading tasks.

**First step to challenge.** Check that the cell masses and the change-of-measures factor refer to the very cells selected by support and bi-invariance. An untracked volume factor changes the unfolding identity.

[Unit record and exact statement](../../units/D024.md)
