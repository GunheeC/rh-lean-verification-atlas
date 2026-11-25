# F-AUX · Three theta inputs for the definite-side grid and row test

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

Three inputs connect theta theory to the tests used to choose the definite-side witness. They supply the unramified fixed-vector comparison for separation, transfer local matching to the square model for the evaluation grid, and turn tests at individual data into the required rationality of the rows. Each has its own hypotheses.

`three-theta-inputs-for-the-definite-side-grid` · [Theta correspondence and automorphic representations of unitary groups](../tracks/theta/README.md) · [Local p-adic theory](../tracks/local/README.md)

**Outlined** · **L0** Declaration pinned; no review of this unit · Record generated 2026-11-25 (no human check).

**First-pass outline of the head proof term** · 6,499 dominated core lines. In scope, this note describes what the top-level term calls; it does not explain the dependency cone beneath it.

| 1 · Lean pinned | 2 · Statement compared | 3 · Prose | 4 · Steps | 5 · AI review | 6 · Human |
|---|---|---|---|---|---|
| ✓ | – | Outlined | 5 | – | 0 of 5 steps |

[Numbered proof and check records](F-AUX.check.md) · [Progress and counting rules](../PROGRESS.md)

## Statement

The unramified dual-pair assertion HoweUnram holds. Real Howe duality, the theta-local inputs, tensor-model integral agreement and tensor-model local matching imply local matching in the twisted square model. A row test at every datum implies RowRatW. These are three separate implications used in the definite-side supplier.

## Assumptions

- For the unramified assertion use the valued field, involution, local pair and nonzero invariant generating test vector of HoweUnram.
- For the local transfer supply real Howe duality and the full theta-local record, theta-integral agreement and local matching in the original model.
- For row rationality supply AtDat of the row test on the complex realization at each datum.

Sources for the assumptions · [Lean source mirror](../sources/README.md)

**New exposition · pending_review.** This edition has no independent review of the new argument. Earlier verdicts below retain their stated scopes.

## Where to read

The blueprint and conditional paper are AI-written, unpublished manuscripts prepared under the direction of Gunhee Cho. They have no human review. Levent Alpöge is the author of the Lean development. [Blueprint v13a](../editions/v0.1.0/blueprint_v13a.pdf) · [Conditional paper v6](../editions/v0.1.0/paper_v6.pdf) · [Edition register](../data/editions.json)

- [F-AUX · Three inputs to the definite-side evaluation grid and row test](../notes/units/F-AUX_round4.md), pp. 1–3 in the atlas print layout. Round-4 outline under the named inputs; pending_review.

## Evidence

The pinned declaration is recorded in the formal source. No higher-level verdict is assigned to this unit.

L0 records the three pinned head declarations; the atlas groups their uses at T02.

## Lean declarations

- `GlobalTheory.Hk3.howeUnram_holds`  
  [`RhoMemOfMkEq.lean`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/RhoMemOfMkEq.lean#L250-L256), lines 250–256 · 6,499 dominated lines · SHA-256 `0c79aadc5113`.

<details>
<summary>2 additional indexed declarations</summary>

- `GlobalTheory.T.twisted_local_factors_match`  
  [`TwistedSquareLocalMatching.lean`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/TwistedSquareLocalMatching.lean#L88-L89), lines 88–89 · 2 dominated lines · SHA-256 `dfa1b9c76215`.
- `GlobalTheory.Mem.LiteralAutomorphy.rowRatW_of_rowTest`  
  [`RowRatWOfRowTest.lean`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/IwasawaDecomposition/RowRatWOfRowTest.lean#L9-L12), lines 9–12 · 4 dominated lines · SHA-256 `cab25bc2ec91`.

</details>

[Machine record and full declaration hashes](F-AUX.yaml) · [Declaration lookup](../lookup/declarations.md)

## Reading prerequisites

Background · Unramified dual pairs · Finite Fock subspaces and local matching · Dependent row predicates.

No prior atlas unit is specified.

[Pillar dependencies and pinned source ranges](../data/round4_changes.json)

## Open questions

- Track the same quotient and both spanning conditions through the finite Fock subspaces and the product-form argument.

[Pillar call tree and source witnesses](../pillars/F.md)

## Graph connections

Arrows may connect either a unit’s main declaration or an indexed member.

**Uses** · No recorded edge.

**Used by** · No recorded edge.

[Declaration witnesses and graph scope](../data/unit_graph.json)

Lookup aliases · `unramified fixed-vector comparison`, `square-model local matching`, `row rationality transition`

<!-- Unit metadata SHA-256 f0d434324f6e8232de5bf70ff16a102003fb76a69d4bb3f1cb84da24b10b0def -->
