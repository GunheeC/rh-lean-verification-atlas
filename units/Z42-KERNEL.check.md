# Z42-KERNEL · proof checklist

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

[Unit and hypotheses](Z42-KERNEL.md) · [Step manifest](Z42-KERNEL.steps.yaml)

Sign-off edition SHA-256 `b2d698fb25d56e15fcea09076895229e0a37b4e204c10df3f193ec3bd36a99f2`. This identifies the exact statement, source files and ordered step text. The whole note SHA-256 is `45d3eb80504f2943b01ddabf4abff2ad4fc39e78e9e4ea408868af0fc6796a64`. Each check covers the stated claim under its listed inputs.

| Edition source | SHA-256 |
|---|---|
| [notes/blueprint/Z42-KERNEL.tex](../notes/blueprint/Z42-KERNEL.tex) | `45d3eb80504f2943b01ddabf4abff2ad4fc39e78e9e4ea408868af0fc6796a64` |

| Step | Claim | Uses | Pinned Lean source | AI step review | Human checks |
|---|---|---|---|---|---|
| <a id="S1"></a>**S1** | The common indicator relations give the stabilizer law for the selected kernel. ([source](../notes/blueprint/Z42-KERNEL.tex), lines 7–11, assembly) | input: simultaneous indicator relations and fixed-coordinate stabilizer | [`GlobalTheory.TwV.site_law_xiIn` 20–48](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/KernelSiteLawAndFixedCoordinateStabiliserLaw.lean#L20-L48) | No step-specific verdict | awaiting human check |
| <a id="S2"></a>**S2** | One polynomial and one determinant constant give the positive-step frame differences. ([source](../notes/blueprint/Z42-KERNEL.tex), lines 17–20, computation) | input: positive-step frame comparison | [`GlobalTheory.TwV.StepDel.del_of_pos` 10–12](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/KernelSiteFrameValuesPositiveSteps.lean#L10-L12) | No step-specific verdict | awaiting human check |
| <a id="S3"></a>**S3** | The zero-step difference is obtained from its own contraction identity. ([source](../notes/blueprint/Z42-KERNEL.tex), lines 32–35, case-split) | input: initial-level frame comparison | [`GlobalTheory.TwV.StepZero.del_zero` 10–13](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/KernelSiteFrameValuesStepZero.lean#L10-L13) | No step-specific verdict | awaiting human check |
| <a id="S4"></a>**S4** | The chain carrying the comparisons also carries the admitted site system under the entry and curve inputs. ([source](../notes/blueprint/Z42-KERNEL.tex), lines 39–42, assembly) | [S1](#S1) · [S2](#S2) · [S3](#S3) · [P046](P046.md) | [`GlobalTheory.TwV.site_cmpLite_siteAdm` 77–89](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/JointSiteChainComparedCarriesAdmittedSystem.lean#L77-L89) | No step-specific verdict | awaiting human check |

## Statement comparison and unit decision

Statement against Lean · **awaiting human check**. Current edition meets L4 · **no**. All steps and statement checked by at least two independent readers · **no**.

## How to record your check

Choose the edition and step IDs you actually read. Report your method, verdict and any reservations. The form accepts partial and negative findings. [Sign-off guide and form](../signoffs/README.md)
