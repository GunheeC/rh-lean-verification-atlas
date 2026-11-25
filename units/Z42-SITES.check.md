# Z42-SITES · proof checklist

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

[Unit and hypotheses](Z42-SITES.md) · [Step manifest](Z42-SITES.steps.yaml)

Sign-off edition SHA-256 `cbebe867e453d1ce894fc53a14dc618303f2f8184db584d494eeffa1bc72bdc4`. This identifies the exact statement, source files and ordered step text. The whole note SHA-256 is `e26ce9b04d40cf3c3528953874dc9dd3516b0ae8a385da5f6a41a7d0b293c02f`. Each check covers the stated claim under its listed inputs.

| Edition source | SHA-256 |
|---|---|
| [notes/blueprint/Z42-SITES.tex](../notes/blueprint/Z42-SITES.tex) | `e26ce9b04d40cf3c3528953874dc9dd3516b0ae8a385da5f6a41a7d0b293c02f` |

| Step | Claim | Uses | Pinned Lean source | AI step review | Human checks |
|---|---|---|---|---|---|
| <a id="S1"></a>**S1** | The small-prime and large-prime rank choices both satisfy the two rank bounds in Std. ([source](../notes/blueprint/Z42-SITES.tex), lines 7–16, case-split) | input: served site, gate tie and rank bound | [`GlobalTheory.TwU.std_at_served` 9–22](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/StdAtServed.lean#L9-L22) | No step-specific verdict | awaiting human check |
| <a id="S2"></a>**S2** | The fill's maximum bound and monotonicity imply the remaining individual weight conditions for Std. ([source](../notes/blueprint/Z42-SITES.tex), lines 7–16, inequality) | input: bounds of the fixed fill | [`GlobalTheory.TwU.std_at_served` 9–22](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/StdAtServed.lean#L9-L22) | No step-specific verdict | awaiting human check |
| <a id="S3"></a>**S3** | At zero and at each successor the same point indexes the class, kernel lattice and determinant in the dictionary. ([source](../notes/blueprint/Z42-SITES.tex), lines 36–37, assembly) | input: joint and chosen tuple | [`GlobalTheory.TwV.joint_dict` 16–25](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/LatticeTupleJointDictionary.lean#L16-L25) | No step-specific verdict | awaiting human check |
| <a id="S4"></a>**S4** | The parity-adjusted conjugation of the embedding argument gives the required position embeddings at this site. ([source](../notes/blueprint/Z42-SITES.tex), lines 53–54, computation) | input: embedding compatibility and comparison tie | [`GlobalTheory.TwV.pos_at_site` 11–13](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/SitePlaceInducesPositionEmbeddings.lean#L11-L13) | No step-specific verdict | awaiting human check |

## Statement comparison and unit decision

Statement against Lean · **awaiting human check**. Current edition meets L4 · **no**. All steps and statement checked by at least two independent readers · **no**.

## How to record your check

Choose the edition and step IDs you actually read. Report your method, verdict and any reservations. The form accepts partial and negative findings. [Sign-off guide and form](../signoffs/README.md)
