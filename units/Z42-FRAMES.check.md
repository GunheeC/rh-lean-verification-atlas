# Z42-FRAMES · proof checklist

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

[Unit and hypotheses](Z42-FRAMES.md) · [Step manifest](Z42-FRAMES.steps.yaml)

Sign-off edition SHA-256 `072f3ce4aa89510ebd31b4f85778d90ca861da4853fd17700e704e8b1850c0cc`. This identifies the exact statement, source files and ordered step text. The whole note SHA-256 is `b391a2ae29a13bfe23f5bc1bd96fd686f1692c712f140dd1cb0ceaabf6189811`. Each check covers the stated claim under its listed inputs.

| Edition source | SHA-256 |
|---|---|
| [notes/blueprint/Z42-FRAMES.tex](../notes/blueprint/Z42-FRAMES.tex) | `b391a2ae29a13bfe23f5bc1bd96fd686f1692c712f140dd1cb0ceaabf6189811` |

| Step | Claim | Uses | Pinned Lean source | AI step review | Human checks |
|---|---|---|---|---|---|
| <a id="S1"></a>**S1** | Rational action and the level factor carry the chosen lattice tuple to the translated tuple in the same site. ([source](../notes/blueprint/Z42-FRAMES.tex), lines 7–11, computation) | [Z42-SITES](Z42-SITES.md) · input: admissible lattice pair | [`GlobalTheory.TwV.move_at_site` 13–15](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/KernelSiteArithmeticGroupMovesFrames.lean#L13-L15) | No step-specific verdict | awaiting human check |
| <a id="S2"></a>**S2** | The ratio of arithmetic scalars is computed from the moved exterior lattice and its character factor. ([source](../notes/blueprint/Z42-FRAMES.tex), lines 159–173, computation) | [S1](#S1) · input: determinant law at the site | [`GlobalTheory.TwV.move_at_site` 13–15](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/KernelSiteArithmeticGroupMovesFrames.lean#L13-L15) | No step-specific verdict | awaiting human check |
| <a id="S3"></a>**S3** | The cleared local lattice comparison yields the away identity at the prescribed place under the supplied dictionary. ([source](../notes/blueprint/Z42-FRAMES.tex), lines 237–256, appeal-to-input) | [Z42-SITES](Z42-SITES.md) · input: positive pair and comparison hypotheses | [`GlobalTheory.TwV.away_of_dict` 13–16](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/KernelSiteSeriesIndependentAwayFromPlaceOverP.lean#L13-L16) | No step-specific verdict | awaiting human check |
| <a id="S4"></a>**S4** | The class number clears the ideal class in the norm-one determinant comparison, giving the supplied bound on the normalized scalar. ([source](../notes/blueprint/Z42-FRAMES.tex), lines 29–34, inequality) | [Z42-SITES](Z42-SITES.md) · input: norm-one character and bounded scalar data | [`GlobalTheory.TwV.scal_at_site` 14–16](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/KernelSiteSeriesScalarPowIntegral.lean#L14-L16) | No step-specific verdict | awaiting human check |

## Statement comparison and unit decision

Statement against Lean · **awaiting human check**. Current edition meets L4 · **no**. All steps and statement checked by at least two independent readers · **no**.

## How to record your check

Choose the edition and step IDs you actually read. Report your method, verdict and any reservations. The form accepts partial and negative findings. [Sign-off guide and form](../signoffs/README.md)
