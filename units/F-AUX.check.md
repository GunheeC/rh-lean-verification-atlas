# F-AUX · proof checklist

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

[Unit and hypotheses](F-AUX.md) · [Step manifest](F-AUX.steps.yaml)

Sign-off edition SHA-256 `ec642113bd2c5560ade193a7d295422245913ed890493d0a74dc1d5a5ea3a977`. This identifies the exact statement, source files and ordered step text. The whole note SHA-256 is `2016c71155261499864c38f0e646dbf74e06f48a330728a9d3da1835d4d58b0d`. Each check covers the stated claim under its listed inputs.

| Edition source | SHA-256 |
|---|---|
| [notes/units/F-AUX_round4.md](../notes/units/F-AUX_round4.md) | `2016c71155261499864c38f0e646dbf74e06f48a330728a9d3da1835d4d58b0d` |

| Step | Claim | Uses | Pinned Lean source | AI step review | Human checks |
|---|---|---|---|---|---|
| <a id="S1"></a>**S1** | For the unramified pair, invariance of the span and separation of orbit heights put a vector fixed by the second integral subgroup in the span of the first group’s vacuum translates. ([source](../notes/units/F-AUX_round4.md), lines 15–16, appeal-to-input) | standard: orbit-height induction | [`GlobalTheory.Hk3.HoweDuality.fixed_mem_span` 145–240](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/RhoMemOfMkEq.lean#L145-L240) | No step-specific verdict | awaiting human check |
| <a id="S2"></a>**S2** | Applying the fixed-span result to the Hermitian-adjoint swap gives the other compact-fixed inclusion. ([source](../notes/units/F-AUX_round4.md), lines 15–16, assembly) | [S1](#S1) | [`GlobalTheory.Hk3.howeUnram_holds` 250–256](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/RhoMemOfMkEq.lean#L250-L256) | No step-specific verdict | awaiting human check |
| <a id="S3"></a>**S3** | The matching hypotheses give a common quotient. Evaluation on the two spaces of finite Fock functions spans the target on each side. ([source](../notes/units/F-AUX_round4.md), lines 22–23, appeal-to-input) | standard: irreducibility and scalar commutant | [`GlobalTheory.SquareLM.twisted_square_local_matching` 18–81](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/TwistedSquareLocalMatching.lean#L18-L81) | No step-specific verdict | awaiting human check |
| <a id="S4"></a>**S4** | The product form on those subspaces extends to the ambient function spaces with its values on finite functions unchanged, which gives square-model local matching. ([source](../notes/units/F-AUX_round4.md), lines 22–23, assembly) | [S3](#S3) | [`GlobalTheory.SquareLM.twisted_square_local_matching` 18–81](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/TwistedSquareLocalMatching.lean#L18-L81) · [`GlobalTheory.T.twisted_local_factors_match` 88–89](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/TwistedSquareLocalMatching.lean#L88-L89) | No step-specific verdict | awaiting human check |
| <a id="S5"></a>**S5** | The step from Start to Pinned, the at-datum row test and universal specialization compose to yield RowRatW. ([source](../notes/units/F-AUX_round4.md), lines 27–27, assembly) | standard: composition of implications | [`GlobalTheory.Mem.LiteralAutomorphy.rowRatW_of_rowTest` 9–12](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/RowRatWOfRowTest.lean#L9-L12) | No step-specific verdict | awaiting human check |

## Statement comparison and unit decision

Statement against Lean · **awaiting human check**. Current edition meets L4 · **no**. All steps and statement checked by at least two independent readers · **no**.

## How to record your check

Choose the edition and step IDs you actually read. Report your method, verdict and any reservations. The form accepts partial and negative findings. [Sign-off guide and form](../signoffs/README.md)
