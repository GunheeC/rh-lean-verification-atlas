# Z42-FRAMES · Translation, away comparison and arithmetic scalars

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

In the specified dictionary, arithmetic translation acts on the chosen frames and kernel by controlled rational and algebraic data. Away comparisons match off-prime lattices and bound the adjacent scalar after normalization. These controls track what changes when representatives or places change.

`translation-away-comparison-and-arithmetic-scalars` · [Local p-adic theory](../tracks/local/README.md) · [Theta correspondence and automorphic representations of unitary groups](../tracks/theta/README.md)

**Full** · **L1** Statement matched to Lean · Record generated 2026-11-25 (no human check).

| 1 · Lean pinned | 2 · Statement compared | 3 · Prose | 4 · Steps | 5 · AI review | 6 · Human |
|---|---|---|---|---|---|
| ✓ | ✓ | Full | 4 | – | 0 of 4 steps |

[Numbered proof and check records](Z42-FRAMES.check.md) · [Progress and counting rules](../PROGRESS.md)

## Statement

**Z4.2.06.** The dictionary implies MoveTie: an arithmetic group translate at a source tuple is implemented by a rational unitary matrix on its frames and kernel lattice and by an algebraic scalar on the kernel datum, with the prescribed $\kappa$ factor after normalization. **Z4.2.07.** For each local place $v$ and $j<m$, the dictionary supplies a split prime with the specified integral approximation and excluded-support conditions. Tuples with identical away data have matching off-prime lattices, frames and kernel datum, with the scalar ratio given by two valuation-zero factors and the two lengths. **Z4.2.08.** For a given site $S$ and dictionary $J.\mathrm{Dict}(\mathrm{std})$, the scalar for each source representative and adjacent valid target at $j<m$ is algebraic and its $p$-adic image times $p^{\mathrm{exp}_G}$ has norm at most one.

## Assumptions

- For the translation law assume a site dictionary with the pair-admission and algebraicity data for the scalar and character factors.
- For the away comparison use the actual joint with self-dual, coefficient-compatible adjacent data. The scalar law also requires the indicated even ranks.

Sources for the assumptions · [Z4.2.02 · Local realization of the tagged kernel](Z4.2.02.md) · [Z4.2.04 · Theta kernels for adjacent pairs](Z4.2.04.md) · [RH verification blueprint, release v13](../data/editions.json)

## Where to read

Gunhee Cho is the paper’s author and the blueprint’s editor. Both were drafted with AI assistance. No human, the author included, has yet checked the arguments. Levent Alpöge is the author of the Lean development. [Blueprint v13c](../editions/v0.1.0/blueprint_v13c.pdf) · [Conditional paper v8](../editions/v0.1.0/paper_v8.pdf) · [Edition register](../data/editions.json)

- [Blueprint source excerpt](../notes/blueprint/Z42-FRAMES.tex)
- [Blueprint v13c](../editions/v0.1.0/blueprint_v13c.pdf#page=391), printed p. 355, section label `r6:Z4.2.06`.
- [RH verification blueprint, release v13](../data/editions.json), section label `r6:Z4.2.06`, PDF p. 380 (printed p. 355)
- [Blueprint v13c](../editions/v0.1.0/blueprint_v13c.pdf#page=466), printed p. 430, section label `r8:Z4.2.06`.
- [RH verification blueprint, release v13](../data/editions.json), section label `r8:Z4.2.06`, PDF p. 455 (printed p. 430)
- [Blueprint v13c](../editions/v0.1.0/blueprint_v13c.pdf#page=394), printed p. 358, section label `r6:Z4.2.07`.
- [RH verification blueprint, release v13](../data/editions.json), section label `r6:Z4.2.07`, PDF p. 383 (printed p. 358)
- [Blueprint v13c](../editions/v0.1.0/blueprint_v13c.pdf#page=468), printed p. 432, section label `r8:Z4.2.07`.
- [RH verification blueprint, release v13](../data/editions.json), section label `r8:Z4.2.07`, PDF p. 457 (printed p. 432)
- [Blueprint v13c](../editions/v0.1.0/blueprint_v13c.pdf#page=392), printed p. 356, section label `r6:Z4.2.08`.
- [RH verification blueprint, release v13](../data/editions.json), section label `r6:Z4.2.08`, PDF p. 381 (printed p. 356)
- [Blueprint v13c](../editions/v0.1.0/blueprint_v13c.pdf#page=400), printed p. 364, section label `r7:review:Z4.2.08`.
- [RH verification blueprint, release v13](../data/editions.json), section label `r7:review:Z4.2.08`, PDF p. 389 (printed p. 364)

## Evidence

- [R6 review](../reviews/R6_review.md), original line 14 — Statement faithful; gaps in proof. Exactly the named unit at the hypotheses reviewed in the cited row.
- [R7 review](../reviews/R7_review.md), original line 17 — Statement faithful; gaps in proof. Exactly the named unit at the hypotheses reviewed in the cited row.
- [R7 review](../reviews/R7_review.md), original line 18 — Statement faithful; gaps in proof. Exactly the named unit at the hypotheses reviewed in the cited row.

Named statement declarations with the hypotheses above. Chart supplier records have their own review scopes.

Review records · [R6 review](../reviews/R6_review.md) · [R7 review](../reviews/R7_review.md) · [R8 review](../reviews/R8_review.md)

## Lean declarations

- `GlobalTheory.TwV.move_at_site`  
  [`KernelSiteArithmeticGroupMovesFrames.lean`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/KernelSiteArithmeticGroupMovesFrames.lean#L13-L15), lines 13–15 · 563 dominated lines · SHA-256 `2e6f46eeeb5f`.
- `GlobalTheory.TwV.away_of_dict`  
  [`KernelSiteSeriesIndependentAwayFromPlaceOverP.lean`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/KernelSiteSeriesIndependentAwayFromPlaceOverP.lean#L13-L16), lines 13–16 · 2,349 dominated lines · SHA-256 `4e95c2131df9`.
- `GlobalTheory.TwV.scal_at_site`  
  [`KernelSiteSeriesScalarPowIntegral.lean`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/KernelSiteSeriesScalarPowIntegral.lean#L14-L16), lines 14–16 · 103 dominated lines · SHA-256 `4c7d3c8f69e3`.

[Machine record and full declaration hashes](Z42-FRAMES.yaml) · [Declaration lookup](../lookup/declarations.md)

## Reading prerequisites

Background · Local frames · Unitary translations · Adelic scalar factors.

- [Z4.2.02 · Local realization of the tagged kernel](Z4.2.02.md) · statement-reading
- [Z4.2.04 · Theta kernels for adjacent pairs](Z4.2.04.md) · graph
- [Z42-SITES · Served-site parameters and the lattice dictionary](Z42-SITES.md) · graph

[Evidence and definitions of reading links](../data/round3_prerequisites.json)

## Open questions

None recorded.

## Graph connections

Arrows may connect either a unit’s main declaration or an indexed member.

**Uses** · [Z4.2.04](Z4.2.04.md) · [Z42-SITES](Z42-SITES.md)

**Used by** · No recorded edge.

[Declaration witnesses and graph scope](../data/unit_graph.json)

Lookup aliases · `move_at_site`, `Z42-FRAMES Translation, away comparison and arithmetic scalars`

<!-- Unit metadata SHA-256 6a7fecc97779560f860824538e851ae7af706d109734fa43e1de34952badcb6e -->
