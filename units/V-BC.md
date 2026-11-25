# V-BC · Isobaric base change from finite frame candidates

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

Assume finite control of candidates in the specified comparison frames. This reduction uses frame existence, bounds and reading to obtain the global isobaric datum that the Selmer window’s automorphic input requires.

`isobaric-base-change-from-finite-frame-candidates` · [Theta correspondence and automorphic representations of unitary groups](../tracks/theta/README.md) · [Galois representations, automorphy lifting, Iwasawa theory and Euler systems](../tracks/galois/README.md)

**Outlined** · **L0** Declaration pinned; no review of this unit · Record generated 2026-11-25 (no human check).

**First-pass outline of the head proof term** · 1,279 dominated core lines. In scope, this note describes what the top-level term calls; it does not explain the dependency cone beneath it.

| 1 · Lean pinned | 2 · Statement compared | 3 · Prose | 4 · Steps | 5 · AI review | 6 · Human |
|---|---|---|---|---|---|
| ✓ | – | Outlined | 3 | – | 0 of 3 steps |

[Numbered proof and check records](V-BC.check.md) · [Progress and counting rules](../PROGRESS.md)

## Statement

Assume the finite-candidate property CandFin for the specified local comparison frames. Then the definite isobaric base-change assertion BaseChangeIsobaricN holds.

## Assumptions

- Assume the candidate finiteness statement for the specified comparison frames, test data and auxiliary places.

Sources for the assumptions · [W16 · Finiteness of the candidates in a base-change frame](W16.md)

**New exposition · pending_review.** This edition has no independent review of the new argument. Earlier verdicts below retain their stated scopes.

## Where to read

Gunhee Cho is the paper’s author and the blueprint’s editor. Both were drafted with AI assistance. No independent human referee has checked the arguments. Levent Alpöge is the author of the Lean development. [Blueprint v13b](../editions/v0.1.0/blueprint_v13b.pdf) · [Conditional paper v7](../editions/v0.1.0/paper_v7.pdf) · [Edition register](../data/editions.json)

- [V-BC · Conditional base change from finite comparison candidates](../notes/units/V-BC_round4.md), pp. 1–2 in the atlas print layout. Round-4 outline under the named inputs; pending_review.

### Declaration-name matches

- [jae-63/rh-alpoge-blueprint](../crosswalk/jae-63.md) · 1 matching declaration.

## Evidence

The pinned declaration is recorded in the formal source. No higher-level verdict is assigned to this unit.

## Lean declarations

- `UpperTheory.BaseChangeIdentities.baseChangeN_of`  
  [`FillPre.lean`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/Foundations/BaseChangeIdentities/FillPre.lean#L7-L9), lines 7–9 · 1,279 dominated lines · SHA-256 `1931e1038512`.

[Machine record and full declaration hashes](V-BC.yaml) · [Declaration lookup](../lookup/declarations.md)

## Reading prerequisites

Background · Isobaric base change · Local components of automorphic representations.

- [W16 · Finiteness of the candidates in a base-change frame](W16.md) · statement-reading

[Pillar dependencies and pinned source ranges](../data/round4_changes.json)

## Open questions

- Check that the finite family for a fixed split test is selected before the finite set of inert places varies, then check the permutation that transfers a singleton split-place match to the original global datum.

[Pillar call tree and source witnesses](../pillars/V.md)

## Graph connections

Arrows may connect either a unit’s main declaration or an indexed member.

**Uses** · No recorded edge.

**Used by** · No recorded edge.

[Declaration witnesses and graph scope](../data/unit_graph.json)

Lookup aliases · `baseChangeN_of`, `V-BC Assume finite control of candidates in the specified comparison frames`

<!-- Unit metadata SHA-256 844eb19dfeeac0cba135c2f067617f961baecb52436a6778f68244fa26a7fca4 -->
