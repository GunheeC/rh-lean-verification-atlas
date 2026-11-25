# D128 · Integrality of the theta scalar on the integral models

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 3,199 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**Outlined · pending_review.** At a valued point of an admissible integral model, a theta key computed from a generating section comes from a unit of the valuation ring. The formula also tracks how a change of section affects tensor powers. This supplies the unit information needed when comparing integral frames.

## Statement and hypotheses

At the eligible valued points of the specified integral model, a generating section gives a unit representing its theta key. If its $N$-fold box is $a$ times a generator and $8\mid N$, then $a\kappa^{N/8}$ is represented by a unit.

$$
\mathrm{KeyUnitOnModels}.
$$

[`thetaKeyScalar_isUnit_on_integralModels` · `ThetaKeyScalarIsUnitOnIntegralModelsStatement.lean:5-6`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ThetaKeyScalarIsUnitOnIntegralModelsStatement.lean#L5-L6)

**Read alongside** [T13 · Arithmetic inputs for the covolume bound](../../units/T13.md) · [T14 · An averaged slope bound over deep components](../../units/T14.md).

## What a unit means at a valued point

Fix a CM host, positive signature sum, a base ring as specified, prime level, and a model with the level, N3, N4 and split-fibre conditions. Fix a compatible point and its lift, a Lie basis, a section and its generic fibre. A generating section gives a valuation-ring unit representing the key and generating box sections in degrees divisible by eight. More generally, if the box section is $a$ times another generator in degree $N$, the required unit represents $a\kappa^{N/8}$. The second clause keeps track of the scale even when the original section is not a generator. [`UnitAt` · `FibreFramesOnModels.lean:114-129`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/BlockTheory/DivisorBase/FibreFramesOnModels.lean#L114-L129) · [`KeyUnitOnModels` · `FibreFramesOnModels.lean:136-141`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/BlockTheory/DivisorBase/FibreFramesOnModels.lean#L136-L141)

## Extend the unit on a chart

Begin on the open generic chart where the key has an invertible representative. The argument uses density of the generic part, normality, countability and the extension criterion at discrete valuations to move from that open to the chosen chart on the model. Apply the criterion twice to obtain extensions of the representative and of its inverse. Their product restricts to one. Injectivity of restriction makes the product one on the model chart. This explains the arithmetic strength of the conclusion: a regular function with the right generic value would only control one inequality on its valuation. [`exists_chart_unit` · `ThetaKeyScalarIsUnitOnIntegralModels.lean:73-107`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ThetaKeyScalarIsUnitOnIntegralModels.lean#L73-L107) · [`exists_chart_unit` · `ThetaKeyScalarIsUnitOnIntegralModels.lean:107-135`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ThetaKeyScalarIsUnitOnIntegralModels.lean#L107-L135)

## Normalize the section at the lifted point

Choose the chart at the closed point, so the map from the local base factors through it. The chart unit gives the desired value for a generating section. For a general section, choose a generator nonzero on the closed fibre and express the section as its scalar multiple $b$. On the box power the multiple becomes $b^N$. Compare the chosen generator on that product with the box of the original generator; their comparison coefficient is a unit. Compatibility of the key rule with rescaling makes the combination in the conclusion a product of units. Here the divisibility by eight enters through the exponent of the key. [`unitAt_local` · `ThetaKeyScalarIsUnitOnIntegralModels.lean:145-176`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ThetaKeyScalarIsUnitOnIntegralModels.lean#L145-L176) · [`unitAt_local` · `ThetaKeyScalarIsUnitOnIntegralModels.lean:177-193`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ThetaKeyScalarIsUnitOnIntegralModels.lean#L177-L193)

## Pass to both kinds of valued point

Pull the valuation ring back to the coefficient field by the generic-point map. Its factorization through the base induces a localized model, with the old valued point and family lifted to it. The local argument applies after transport of the model conditions. The concluding packaging covers both the complete discrete valuation case and the complete algebraically closed ultrametric case with its unit ball. Establishing the valuation-ring description in the second case precedes use of the same argument. [`unitAt_valuation` · `ThetaKeyScalarIsUnitOnIntegralModels.lean:196-229`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ThetaKeyScalarIsUnitOnIntegralModels.lean#L196-L229) · [`keyUnitOnModels` · `ThetaKeyScalarIsUnitOnIntegralModels.lean:233-237`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/ThetaKeyScalarIsUnitOnIntegralModels.lean#L233-L237)

**First step to challenge.** Check why both a chart section and its inverse extend over the model chart. Extending the first alone leaves a possible zero along the boundary.

[Unit record and exact statement](../../units/D128.md)
