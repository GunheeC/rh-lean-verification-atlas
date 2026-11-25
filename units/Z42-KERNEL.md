# Z42-KERNEL · Transformation and level changes of the kernel

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

Under the specified site conditions the frame series transforms with the prescribed character, and level changes admit norm-one scalar corrections. With the additional admission and stabilizer assumptions, the same selected chain carries both the comparison and the bounded local system.

`transformation-and-level-changes-of-the-kernel` · [Theta correspondence and automorphic representations of unitary groups](../tracks/theta/README.md) · [Local p-adic theory](../tracks/local/README.md)

**Outlined** · **L0** Declaration pinned; no review of this unit · Record generated 2026-11-25 (no human check).

| 1 · Lean pinned | 2 · Statement compared | 3 · Prose | 4 · Steps | 5 · AI review | 6 · Human |
|---|---|---|---|---|---|
| ✓ | – | Outlined | 4 | – | 0 of 4 steps |

[Numbered proof and check records](Z42-KERNEL.check.md) · [Progress and counting rules](../PROGRESS.md)

## Statement

**Z4.2.09.** For a site satisfying Pair, Pos, Move and Away, obtain the inverse-$\kappa$ transformation identity for the frame series under the arithmetic group, together with the LawInLt and XiIn conditions for this same local system. **Z4.2.10.** At a site with dictionary, Pair, Pos and Law, for every extension of the chosen algebraic embedding there exists a $p$-adic norm-one scalar giving KernelDifferenceAtLevel at $j=0$ for these comparison maps and series. **Z4.2.11.** With the same dictionary, Pair, Pos and Law and for each $1\le j<m$, every extension of the chosen algebraic embedding admits a norm-one scalar giving KernelDifferenceAtLevel at that $j$. **Z4.2.12.** With AdmAtEnt2, CurveEx, a joint $J$, a used tuple, trivial level-zero stabilizers and $2r_G\le k$, the very chain $\mathrm{chainAt}(H,h_T)$ carries both the comparison data and an admitted site system with $d_G(0)=0$ and $d_G(j)$ bounded by the stabilizer valuation.

## Assumptions

- The transformation branch requires Pair, Pos, Move and Away.
- At level zero assume the dictionary, Pair, Pos and Law, and fix the algebraic embedding and its extension. A positive stage satisfies $0<j<m$.
- For the final comparison assume AdmAtEnt2 and CurveEx with a joint, a used tuple, trivial level-zero stabilizers and twice the rank at most $k$.

Sources for the assumptions · [RH verification blueprint, release v13](../data/editions.json)

## Where to read

The blueprint and conditional paper are AI-written, unpublished manuscripts prepared under the direction of Gunhee Cho. They have no human review. Levent Alpöge is the author of the Lean development. [Blueprint v13a](../editions/v0.1.0/blueprint_v13a.pdf) · [Conditional paper v6](../editions/v0.1.0/paper_v6.pdf) · [Edition register](../data/editions.json)

- [Blueprint source excerpt](../notes/blueprint/Z42-KERNEL.tex)
- [Blueprint v13a](../editions/v0.1.0/blueprint_v13a.pdf#page=386), printed p. 359, section label `r6:Z4.2.09`.
- [RH verification blueprint, release v13](../data/editions.json), section label `r6:Z4.2.09`, PDF p. 384 (printed p. 359)
- [Blueprint v13a](../editions/v0.1.0/blueprint_v13a.pdf#page=451), printed p. 424, section label `r8:Z4.2.09`.
- [RH verification blueprint, release v13](../data/editions.json), section label `r8:Z4.2.09`, PDF p. 449 (printed p. 424)
- [Blueprint v13a](../editions/v0.1.0/blueprint_v13a.pdf#page=388), printed p. 361, section label `r6:Z4.2.10`.
- [RH verification blueprint, release v13](../data/editions.json), section label `r6:Z4.2.10`, PDF p. 386 (printed p. 361)
- [Blueprint v13a](../editions/v0.1.0/blueprint_v13a.pdf#page=460), printed p. 433, section label `r8:Z4.2.10`.
- [RH verification blueprint, release v13](../data/editions.json), section label `r8:Z4.2.10`, PDF p. 458 (printed p. 433)
- [Blueprint v13a](../editions/v0.1.0/blueprint_v13a.pdf#page=387), printed p. 360, section label `r6:Z4.2.11`.
- [RH verification blueprint, release v13](../data/editions.json), section label `r6:Z4.2.11`, PDF p. 385 (printed p. 360)
- [Blueprint v13a](../editions/v0.1.0/blueprint_v13a.pdf#page=460), printed p. 433, section label `r8:Z4.2.11`.
- [RH verification blueprint, release v13](../data/editions.json), section label `r8:Z4.2.11`, PDF p. 458 (printed p. 433)
- [Blueprint v13a](../editions/v0.1.0/blueprint_v13a.pdf#page=388), printed p. 361, section label `r6:Z4.2.12`.
- [RH verification blueprint, release v13](../data/editions.json), section label `r6:Z4.2.12`, PDF p. 386 (printed p. 361)
- [Blueprint v13a](../editions/v0.1.0/blueprint_v13a.pdf#page=455), printed p. 428, section label `r8:Z4.2.12`.
- [RH verification blueprint, release v13](../data/editions.json), section label `r8:Z4.2.12`, PDF p. 453 (printed p. 428)

## Evidence

The pinned declaration is recorded in the formal source. No higher-level verdict is assigned to this unit.

Named statement declarations with the hypotheses above. Chart supplier records have their own review scopes.

Review records · [R7 review](../reviews/R7_review.md) · [R8 review](../reviews/R8_review.md)

## Lean declarations

- `GlobalTheory.TwV.site_law_xiIn`  
  [`KernelSiteLawAndFixedCoordinateStabiliserLaw.lean`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/KernelSiteLawAndFixedCoordinateStabiliserLaw.lean#L20-L48), lines 20–48 · 5,250 dominated lines · SHA-256 `0f49034d5bea`.
- `GlobalTheory.TwV.StepZero.del_zero`  
  [`KernelSiteFrameValuesStepZero.lean`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/KernelSiteFrameValuesStepZero.lean#L10-L13), lines 10–13 · 4 dominated lines · SHA-256 `9076055eef78`.
- `GlobalTheory.TwV.StepDel.del_of_pos`  
  [`KernelSiteFrameValuesPositiveSteps.lean`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/KernelSiteFrameValuesPositiveSteps.lean#L10-L12), lines 10–12 · 3 dominated lines · SHA-256 `39824bef51b8`.
- `GlobalTheory.TwV.site_cmpLite_siteAdm`  
  [`JointSiteChainComparedCarriesAdmittedSystem.lean`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/JointSiteChainComparedCarriesAdmittedSystem.lean#L77-L89), lines 77–89 · 30,579 dominated lines · SHA-256 `08d9eab7a3e5`.

[Machine record and full declaration hashes](Z42-KERNEL.yaml) · [Declaration lookup](../lookup/declarations.md)

## Reading prerequisites

Background · Theta transformations · Congruence levels · Lubin–Tate coordinates.

- [Z4.2.02 · Local realization of the tagged kernel](Z4.2.02.md) · graph
- [Z4.2.04 · Theta kernels for adjacent pairs](Z4.2.04.md) · statement-reading
- [Z4.2.13 · Period, lattice and theta-vector laws of the tied base](Z4.2.13.md) · graph
- [Z42-FRAMES · Translation, away comparison and arithmetic scalars](Z42-FRAMES.md) · statement-reading
- [Z42-SITES · Served-site parameters and the lattice dictionary](Z42-SITES.md) · graph

[Evidence and definitions of reading links](../data/round3_prerequisites.json)

## Open questions

- Supply `TieBase.base_data` (Z4.2.13), `KerMove.kerTh_move` and the bad-prime exclusion in `lev_pos_and_noConj`. For the full modelXi and movesCompose interfaces derive the geometric half-lattice comparisons for arbitrary curve bases and the simultaneous split-supported changes of a triple.
- Class-kernel pullback under rational isometries, including the tied base in Z4.2.13 and kernel covariance; component-independent unit; source factor identity; moved source operator and degrees; target frame realization. Supporting inputs are tuple decomposition, the class entry polynomial, its extended weight, frame invertibility, character product and reading from all realizations. Direct suppliers in the all-step argument include `sysS_ranks`, `rk_le`, `ltC_ne`, `equiv_frame_b` and `kernelSite_contractionIdentity_operatorHalf`.
- Supply `joint_at_nonempty` (.02), `pairOK_allSites` (.04), `site_law_xiIn` (.09) with `TieBase.base_data` (.13), and the five common inputs of the differential changes (.10 and .11). In the assembly prove the remaining fields of `kernelSite_seriesData_below_lastStep`, the stabilizer comparison `tieStab_kaAtAny`, and the realizing-polynomial comparison in `series_reading_entries`.

## Graph connections

Arrows may connect either a unit’s main declaration or an indexed member.

**Uses** · [P046](P046.md) · [Z4.2.02](Z4.2.02.md) · [Z4.2.13](Z4.2.13.md) · [Z42-SITES](Z42-SITES.md)

**Used by** · [P012](P012.md) · [T04](T04.md)

[Declaration witnesses and graph scope](../data/unit_graph.json)

Lookup aliases · `site_law_xiIn`, `Z42-KERNEL Transformation and level changes of the kernel`

<!-- Unit metadata SHA-256 88f46a8de34f8698e8e76a89163bc9913a9dd69ae6c2db34a6f206d471113039 -->
