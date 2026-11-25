# V-BC · proof checklist

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

[Unit and hypotheses](V-BC.md) · [Step manifest](V-BC.steps.yaml)

Sign-off edition SHA-256 `8e0d5578ecbd4ddc7ebed095ed382572bef537601a09df08fdc26eb9687d2474`. This identifies the exact statement, source files and ordered step text. The whole note SHA-256 is `7b68b3795360f059732b9e0081427e1255006b0a55ceba0e05b6adbdf92ea195`. Each check covers the stated claim under its listed inputs.

| Edition source | SHA-256 |
|---|---|
| [notes/units/V-BC_round4.md](../notes/units/V-BC_round4.md) | `7b68b3795360f059732b9e0081427e1255006b0a55ceba0e05b6adbdf92ea195` |

| Step | Claim | Uses | Pinned Lean source | AI step review | Human checks |
|---|---|---|---|---|---|
| <a id="S1"></a>**S1** | Finite candidate data and the stated local, spectral and Hecke inputs give a frame on which to make the comparisons. ([source](../notes/units/V-BC_round4.md), lines 13–13, appeal-to-input) | [W16](W16.md) · input: unitary-side and trace comparison data | [`UpperTheory.BaseChangeIdentities.baseChangeN_of` 7–9](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/Foundations/BaseChangeIdentities/FillPre.lean#L7-L9) · [`UpperTheory.HeckeLevelFrameExistence.frameEx_of_fin` 43–48](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/Foundations/BaseChangeIdentities/FrameMatching/HeckeEigenvalueFiniteness/FrameExOfFin.lean#L43-L48) | No step-specific verdict | awaiting human check |
| <a id="S2"></a>**S2** | Frame existence, the word bound and frame reading provide a finite run with the generation and limiting-read inputs. ([source](../notes/units/V-BC_round4.md), lines 15–15, assembly) | [S1](#S1) · input: frame bound and frame reading | [`PositivityTheory.Rg.BcB.Plug2.bci_of` 22–26](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/SatakeExponents/BciOf.lean#L22-L26) · [`PositivityTheory.Rg.BcB.F.Rig.fieldN_of_run` 31–32](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/SatakeExponents/SatakeRigidity/FullThetaHolds.lean#L31-L32) · [`PositivityTheory.Rg.BcB.One.RunFin` 25–28](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/FieldNOf.lean#L25-L28) | No step-specific verdict | awaiting human check |
| <a id="S3"></a>**S3** | Fullness for the empty split-test set gives one global datum. The split-place comparison transports the tests to that datum through the matching permutation. ([source](../notes/units/V-BC_round4.md), lines 21–21, assembly) | [S2](#S2) · input: simultaneous full read | [`PositivityTheory.Rg.BcB.One.fieldN_of` 52–81](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/FieldNOf.lean#L52-L81) · [`PositivityTheory.Rg.BcB.One.full_of` 37–49](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/FieldNOf.lean#L37-L49) · [`PositivityTheory.Rg.BcB.F.Rig.fieldN_of_run` 31–32](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/RepresentationTheoryGL/ArchimedeanBaseChange/ArchimedeanBaseChangeProof/SatakeExponents/SatakeRigidity/FullThetaHolds.lean#L31-L32) | No step-specific verdict | awaiting human check |

## Statement comparison and unit decision

Statement against Lean · **awaiting human check**. Current edition meets L4 · **no**. All steps and statement checked by at least two independent readers · **no**.

## How to record your check

Choose the edition and step IDs you actually read. Report your method, verdict and any reservations. The form accepts partial and negative findings. [Sign-off guide and form](../signoffs/README.md)
