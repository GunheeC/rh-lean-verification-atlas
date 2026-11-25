# D044 · Agreement of the square-model theta integrals

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 2 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**Outlined · pending_review.** Agreement of theta integrals and local matching for the original Weil models transfer to the square models. The scalar depends on the matched data. For each second-space test vector the comparison chooses an integrable representative in its coinvariant class.

## Statement and hypotheses

From the local theta inputs and ordinary agreement and local matching obtain square-model integral agreement. Each matched datum has a nonzero scalar such that each second-space vector has an integrable representative modulo finite coinvariant relations, and matching first-space vectors have integrals related by that scalar.

$$
\mathrm{ThetaLocalInputs}\wedge\mathrm{ThetaIntegralsAgree}_{\rm Weil}\wedge\mathrm{LocalMatching}\ \Longrightarrow\ \mathrm{ThetaIntegralsAgree}_{\rm square}.
$$

[`twisted_square_theta_integrals_eq` · `TwistedSquareThetaIntegralsEq.lean:48-49`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/TwistedSquareThetaIntegralsEq.lean#L48-L49)

**Read alongside** [T11 · Simultaneous global theta-integral comparison and local matching](../../units/T11.md) · [T10 · The constant-function fit from theta and Hecke functionals](../../units/T10.md).

## Two comparisons enter at different stages

Fix the matched Hermitian spaces, characters, measures, Weil data and maps in the square-model assertion. Construct a placewise seesaw model over these data using both specified Weil realizations. Invoke local matching in that model to obtain comparison maps, then evaluate the ordinary integral-agreement hypothesis on those very maps. This gives an ordinary comparison scalar and the coinvariant assertion, with a nonzero scalar for the applicable comparison. The integral-agreement and local-matching assumptions therefore supply different objects. Knowing that some local maps exist would be insufficient if ordinary agreement applied only to some other pair. [`twisted_theta_integrals_agree` · `TwistedSquareThetaIntegralsEq.lean:17-27`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/TwistedSquareThetaIntegralsEq.lean#L17-L27)

## Choose the scalar before the representative

The transferred square kernels agree up to a second nonzero scalar, obtained using the real Howe part of the local input and the compatible seesaw data. Multiply this by the ordinary scalar. Their product is nonzero and is now fixed. For each allowed vector on the second side, the coinvariant passage supplies a representative, its relation to the given vector, and a vector in the model with which to compute. This order matters: the scalar is common to the subsequent test vectors, while the representative may vary. [`twisted_theta_integrals_agree` · `TwistedSquareThetaIntegralsEq.lean:23-30`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/TwistedSquareThetaIntegralsEq.lean#L23-L30)

## Transfer convergence and the equality

Apply the decay and convergence assertion to the model representative. Its bounded-kernel estimate at derivative index zero and the accompanying convergence data give the moderate-growth/integral condition requested in the square model. For a matching first-space vector, obtain a model lift and apply kernel matching with the same representative on the second side. Rewrite each square-model theta integral as the corresponding model integral, using the measure and domain identities for its own space. Ordinary agreement applies with the second vector multiplied by the kernel scalar. Linearity of the model integral then produces the product of scalars fixed above. The last scalar manipulation is routine; controlling the representative modulo relations while retaining convergence is essential. [`twisted_theta_integrals_agree` · `TwistedSquareThetaIntegralsEq.lean:28-41`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/TwistedSquareThetaIntegralsEq.lean#L28-L41)

## Where this comparison is used

The fit argument uses theta agreement and local matching together to obtain the estimates for sums and the square leading term. The unit card gives the exact original predicates and the target square predicate. Treating them as interchangeable at the outset would hide the coinvariant and normalization steps. [`fittedFunction_at_zero_close_alt` · `FittedFunctionAtZeroClose.lean:46-51`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FittedFunctionAtZeroClose.lean#L46-L51)

**Scope of the hypotheses.** The note retains the source’s named predicates and records. For the exact quantified assumptions at this head, read `GlobalTheory.T.twisted_square_theta_integrals_eq` (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/TwistedSquareThetaIntegralsEq.lean:48–49`). Their internal definitions are separate reading tasks.

## Literature-named inputs

`GlobalTheory.FunPr.ThetaLocalInputs.howeDualityReal` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/BernsteinUnitaryProductIrreducible.lean:57`); not compared.

**First step to challenge.** Check that the change of representative preserves the local matching relation after the kernel comparison scalar is inserted, with the same measures on both model integrals.

[Unit record and exact statement](../../units/D044.md)
