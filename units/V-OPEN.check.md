# V-OPEN · proof checklist

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

[Unit and hypotheses](V-OPEN.md) · [Step manifest](V-OPEN.steps.yaml)

Sign-off edition SHA-256 `97c2a00830d3d4783f24dd7d1b06f38cff8ce8dd260c4b4300b04128ab32039e`. This identifies the exact statement, source files and ordered step text. The whole note SHA-256 is `0c5be1aaedfca8f2581cc304eb292cc11cb71db45eaad041f6fa6371eba69256`. Each check covers the stated claim under its listed inputs.

| Edition source | SHA-256 |
|---|---|
| [notes/units/V-OPEN_round4.md](../notes/units/V-OPEN_round4.md) | `0c5be1aaedfca8f2581cc304eb292cc11cb71db45eaad041f6fa6371eba69256` |

| Step | Claim | Uses | Pinned Lean source | AI step review | Human checks |
|---|---|---|---|---|---|
| <a id="S1"></a>**S1** | The row witness has the polarized-pair row type specialized to the chosen local reciprocity relation. ([source](../notes/units/V-OPEN_round4.md), lines 13–13, definition-unfolding) | input: polarized-pair Galois row | [`UpperTheory.V.Z.Win.RowT` 47–47](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/AutomorphyLifting/WeakOfAtt.lean#L47-L47) · [`UpperTheory.GalStar.Row0b` 69–73](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/TypeConditions/WeightsConjBis.lean#L69-L73) | No step-specific verdict | awaiting human check |
| <a id="S2"></a>**S2** | The single row witness is the field required to construct the OpenImageCondition record. ([source](../notes/units/V-OPEN_round4.md), lines 21–21, definition-unfolding) | [S1](#S1) | [`UpperTheory.LiteratureTheorems.OpenImageCondition` 207–208](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/TemperedProductOfSquareIntegrable.lean#L207-L208) | No step-specific verdict | awaiting human check |
| <a id="S3"></a>**S3** · withdrawn | The window supplier can receive both the constructed record and its original row witness, with isobaric base change supplied separately. ([source](../notes/units/V-OPEN_round4.md), lines 17–17, assembly) | [S1](#S1) · [S2](#S2) · [W02](W02.md) | [`UpperTheory.One.vwin_of_row` 4–5](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/VwinOfRow.lean#L4-L5) · [`UpperTheory.One.Join.automorphic_window_of_inputs` 71–74](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/TopMainZj.lean#L71-L74) · [`UpperTheory.One.Join.automorphic_inputs_from_literature` 38–54](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/TopMainZj.lean#L38-L54) | No step-specific verdict | withdrawn |

## Statement comparison and unit decision

Statement against Lean · **awaiting human check**. Current edition meets L4 · **no**. All steps and statement checked by at least two independent readers · **no**.

## How to record your check

Choose the edition and step IDs you actually read. Report your method, verdict and any reservations. The form accepts partial and negative findings. [Sign-off guide and form](../signoffs/README.md)
