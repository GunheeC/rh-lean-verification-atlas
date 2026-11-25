# V-OPEN · The polarized row in the open-image condition

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

The open-image condition used by the window theorem stores a single polarized Galois row. Its constructor lets the same row serve both the record argument and the explicit Galois input in the Selmer-window supplier.

`polarized-row-in-the-open-image-condition` · [Galois representations, automorphy lifting, Iwasawa theory and Euler systems](../tracks/galois/README.md)

**Outlined** · **L0** Declaration pinned; no review of this unit · Record generated 2026-11-25 (no human check).

**First-pass outline of the head proof term** · 2 dominated core lines. In scope, this note describes what the top-level term calls; it does not explain the dependency cone beneath it.

| 1 · Lean pinned | 2 · Statement compared | 3 · Prose | 4 · Steps | 5 · AI review | 6 · Human |
|---|---|---|---|---|---|
| ✓ | – | Outlined | 2 | – | 0 of 2 steps |

[Numbered proof and check records](V-OPEN.check.md) · [Progress and counting rules](../PROGRESS.md)

## Statement

The open-image condition has one field, the polarized Galois row RowT specialized to IsRecT. A witness of that row supplies the record used in the window theorem.

## Assumptions

- The head defines a one-field structure. To construct the record, supply the polarized-pair Galois row for the specified reciprocity predicate. `UpperTheory.LiteratureTheorems.OpenImageCondition` (`Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/TemperedProductOfSquareIntegrable.lean:207–208`).

Sources for the assumptions · [Lean source mirror](../sources/README.md)

**New exposition · pending_review.** This edition has no independent review of the new argument. Earlier verdicts below retain their stated scopes.

## Where to read

The blueprint and conditional paper are AI-written, unpublished manuscripts prepared under the direction of Gunhee Cho. They have no human review. Levent Alpöge is the author of the Lean development. [Blueprint v13a](../editions/v0.1.0/blueprint_v13a.pdf) · [Conditional paper v6](../editions/v0.1.0/paper_v6.pdf) · [Edition register](../data/editions.json)

- [V-OPEN · Which Galois row the open-image record contains](../notes/units/V-OPEN_round4.md), pp. 1–3 in the atlas print layout. Round-4 outline under the named inputs; pending_review.

### Declaration-name matches

- [Naskręcki’s reading project](../crosswalk/naskrecki.md) · 1 matching declaration.
- [jae-63/rh-alpoge-blueprint](../crosswalk/jae-63.md) · 1 matching declaration.

## Evidence

The pinned declaration is recorded in the formal source. No higher-level verdict is assigned to this unit.

## Lean declarations

- `UpperTheory.LiteratureTheorems.OpenImageCondition`  
  [`TemperedProductOfSquareIntegrable.lean`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/TemperedProductOfSquareIntegrable.lean#L207-L208), lines 207–208 · 2 dominated lines · SHA-256 `da9aea23711a`.

[Machine record and full declaration hashes](V-OPEN.yaml) · [Declaration lookup](../lookup/declarations.md)

## Reading prerequisites

Background · Galois representations of polarized pairs · Local reciprocity data.

No prior atlas unit is specified.

[Pillar dependencies and pinned source ranges](../data/round4_changes.json)

## Open questions

- Compare the exact reciprocity specialization in `RowT` with the hypothesis of P013, including the above-prime alternatives, before reusing the same witness in the two argument positions.

[Pillar call tree and source witnesses](../pillars/V.md)

## Graph connections

Arrows may connect either a unit’s main declaration or an indexed member.

**Uses** · No recorded edge.

**Used by** · No recorded edge.

[Declaration witnesses and graph scope](../data/unit_graph.json)

Lookup aliases · `OpenImageCondition`, `V-OPEN The open-image condition used by the window theorem stores a single polarized Galois row`

<!-- Unit metadata SHA-256 a3c3e4a906c8f9cde92b84d36d753ab80c122277c708c5db672aefdf1c390350 -->
