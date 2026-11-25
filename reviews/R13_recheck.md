AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

# R13_recheck

AI review report produced during this project; file names are internal working names.

- Internal source file: `out/R13_recheck.md`
- SHA-256: `e1823ce0f3a387cc55ba7182ab50068e020ef90da3203f8d5a667da42be3f9b9`
- Report scope: Round-13 recheck of Z4.4 (`twistedPeriodAdmissible_of_rowInt`): fixes A1-A7

## Internal report

The report below preserves its original verdict, scope and unresolved points. Historical review-machine home prefixes are displayed as `${REVIEW_HOME}`; the source checksum above identifies the original report. Source line numbers in other records count from its original title.

# Round-13 recheck of Z4.4 (`twistedPeriodAdmissible_of_rowInt`): fixes A1-A7

Scope: a focused recheck of the seven required fixes A1-A7 (`BP_round13.md`, section A) against `ch_P_r12.tex` (4,354 lines) and `status.json` in `${REVIEW_HOME}/work/prev13`. It is not a new full review. Lean line numbers are the original numbering of commit `40e56bab`, read with `git show`. Graph figures come from `graphq.py` and a reachability/dominator pass over the same `graph_cache.bin`.

Nothing here, in the chapter, or in the Lean development is treated as establishing RH or GRH. This report only compares hand proofs and bookkeeping with the Lean declarations they label.

## 1. Verdict

**APPROVE AFTER MINOR EDITS.**

All seven fixes are FIXED. I found no mathematical error and no statement mismatch. The edits in section 5 are clerical (one line reference, a few helper names in the class-sum paragraph, one notation clash). They need no further review round. Once they are made, the original input Z4.4 can be raised to complete (14 of 20).

| Fix | Subject | Result |
|---|---|---|
| A1 | `TransDual.nabDelDual` registered and fully hand-proved | **FIXED** |
| A2 | `NabDelLoc` dependency labels for suppliers 8 and 9 | **FIXED** |
| A3 | `locPrints_of_litN` as pass-through of `hH.litN` | **FIXED** |
| A4 | `upNatTie`, `dnNatTieG_cols`, `lvSame_zero` hand proofs; `fvTieG` statement | **FIXED** |
| A5 | Stage and base-law block in the ledger, `.unit` observation | **FIXED** |
| A6 | Two deviation lemmas stated, marked, and correct | **FIXED** |
| A7 | Pinpoint references at the four places | **FIXED** |

## 2. The seven fixes

### A1. Transported Hermitian duality: FIXED

Text: `ch_P_r12.tex:472-584` (`r13:weyl-dual`). Lean: `TransportedWeylLatticeHermitianDuality.lean:29-309`; statement `NabDelDual`, `CoefModLemmas.lean:143-148`. Registration: `status.json` `round13.new_subtheorems[0]` (lines 278-309, cone 7,581; both reproduce from the graph).

Statement. Lean: for `G τ` Hermitian with unit determinant and `M τ` lattices, `dual (pairK lam G) (nabK lam M) = delK lam (hdualFr G M)` and `dual (pairK lam G) (delK lam M) = nabK lam (hdualFr G M)`, where `dual` tests the first argument (`dual_of_local`, `h1`, 229-241) and `hdualFr G M = {x | ∀ y ∈ M, star y ⬝ᵥ (G *ᵥ x) ∈ 𝓞 K}` (`CoefMod.lean:228-242`). The display at 482-487 states exactly this. The Hermitian hypothesis is carried but unused in Lean (`intro ... _ hG hM`, 279), and the hand proof does not use it either.

Proof, step by step against Lean.

| Step | Text | Lean | Check |
|---|---|---|---|
| Localized dual test `x ∈ D_w ⟺ h(T_{w̄}, x) ⊂ R_w` | 489-503 | `conj_not_mem` 52-58, `pair_locP` 70-77, `pair_denom` 79-99, `mem_localization_dual` 101-117 | Both directions correct. Forward: `h(ty, sx) = t̄ s h(y,x)`, `t̄ s ∉ w`. Converse: product of denominators over a finite generating set; finite generation is used only here. `sx ∈ V` is used so that the characterization of `D` applies. |
| `A = ⋂_w A_w`, global test equals all local tests | 504-510 | `mem_of_forall_locP` 29-44, `pair_integral_iff` 119-123 | Correct; the text notes that this half needs no finite generation, as in Lean. |
| `M^#` is a full finitely generated lattice | 514-522 | `isLattice_hdualFr`, `dualFr_lattice_and_hdual` (`DualLatticeIsLatticeAndHermitianDual.lean:92-147, 173-175`); used at 282-283 | Correct: the rows `ȳᵗG` span; sandwich between `dR^n` and `d^{-1}R^n`; Noetherian. |
| Dual frame `B' = (B^*G)^{-1}` is a basis of `(M^#)_w` when `B` is a basis of `M_{w̄}` | 523-531 | `mem_colLat_dual` 162-190, `isBasisAt_hdual` 192-201, `exists_dual_frame` 204-210 | Correct. The text compresses two applications of the localized test (to `M` and to `colLat B`) into one sentence; the argument is the same. |
| Standard lattices finitely generated; `A ⊂ V` | 533-545 | `std_fg_span` (296, 303); `hnab` 292 by the third part of the registered localization theorem; `hdel` 293-294 by `transLat_mono`, `delStd_le_nabStd` | Correct. All three inputs are named. |
| Localization formulas at `w̄` for `M` and at `w` for `M^#` | 547-550 | 302, 309: `NabDelLoc` at `conjPl w` with `B`, and at `w` with `hM'` and `B'` | Correct, including which component (`.1` or `.2`) is used in each equality. |
| Covariance `P_G(act(B)y, x) = P_1(y, x_0)`, `x = act(B')x_0` | 550-562 | `pairTransport` (`CoefModLemmas.lean:477-500`), `ht` 249-253 | Correct; the determinant-twist bookkeeping matches `hs` (479-485). |
| Local equivalence and intersection | 563-570 | `h2`, `h3` 242-271; 272-274 | Correct. `x_0 ∈ V` is `polyAction_mem_VV` (263). |
| Both choices `(T,T') = (∇,Δ), (Δ,∇)` | 533, 568-569 | 296-302 uses `.2` of standard duality; 303-309 uses `.1` | Correct: the first equality needs "`x ∈ Δ_std ⟺ P_1(∇_std, x) ⊂ R`", the second the other one. |

Every direct theorem dependency of `nabDelDual` in the graph (ten declarations) is named in the text.

Period-numerator path (572-584). Verified in Lean: `PeriodClassSum.pairBDualK` (`IsClassSumPairingFormsLat.lean:181-194`) installs the trivial star (`starRingOfComm`), takes `G = 1`, rewrites `hdualFr 1 M = dualFr M` (`hdualFr_triv`) and uses symmetry of the bilinear pairing (`pairingBSymm_holds`); `pairBDual` (196-197) applies it to `tauLat` extensions with `tauLatLattice`; `PairAtClass.pair_integral` (`ClassPairingIntegralFormRowIsIntegral.lean:55-56`) uses the first equivalence, forward direction. The text says exactly this. The remark R12-A left unverified ("trivial star and `G = 1` at the period numerator") is confirmed.

Graph: `nabDelDual` is the only caller of `standard_weyl_lattices_fock_dual` and of the registered localization theorem inside the root cone; its callers in the root cone are `pairBDualK` only (`ColPeriod.pairBK_mem_one` and the public alias are outside the root cone, as `status.json` records for the alias).

### A2. Localization path for suppliers 8 and 9: FIXED

Text: new paragraph `r13:nabdelloc` at 1244-1260, and corrected statements at 1177-1181, 1292-1293, 1577-1579, 1997-1998, 2024-2026, 2222-2223, 2627-2629. JSON: `round13.localization_paths`.

Lean and graph: `ValLat.mem_localization_delAtr` (`MemClosureIff.lean:141-150`) calls `Formalism.L2.DIV.nabDelLoc` at line 149 (`CoefficientsModP.lean:24`), which is `nablaDeltaLocal_holds` (`NablaIndependenceHolds.lean:578-580`). The cones of `bw_tie`, `tuple_integralForms_row_place_by_place`, suppliers 8, 9 and 1 contain `mem_localization_delAtr` and do not contain the registered `T.transportedLattice_localization_free_le_coefficientSpace`, whose only caller in the root cone is `nabDelDual`. The text now says this, says that both theorems prove the same proposition `NabDelLoc`, and names `tauLatLattice`, `du_dualFr_lattice`, `basisAtEx`. No remaining passage attributes the integral tests to the registered theorem.

### A3. `locPrints_of_litN`: FIXED

Text 121-129: the argument at `ThFinal.lean:18` is `hH.litN` with `hH : Af.HypothesesH'` a hypothesis; `locPrints_of_litN` (`HVFinalU.lean:12-13`) projects `lfK, ltK, leK, lf, lt, le, bk` from `coh`; "passes all seven results through as hypotheses". Lines 131-142 trace the supply (`published_hypotheses_from_patching_alt`, `litN := hN`, `PublishedHypothesesFromPatching.lean:98-103`; `v_window_of_automorphy_csd_ss_mono_odd`, `WindowBoundOfLiteratureLevel.lean:30-31`; `v_window_of_depth_zero_residual_bc_cm`, `TopMainZj.lean:55-58`; `LitAut.lean:59-63`). I read each of these in Lean; all are as described. The caveat that this is a formal supply, not a verification of printed hypotheses, is attached (141-142).

JSON: the key is now `local_record_pass_through` (`status.json:25445-25469`) with `incoming_hypothesis`, `argument`, `projects_from`, the seven fields and `enclosing_supply`. The old key `local_record_discharge` no longer occurs.

### A4. `upNatTie`, `dnNatTieG_cols`, `lvSame_zero`, `fvTieG`: FIXED

Statements, clause by clause.

- `UpNatTieG` (`TiedTwLv.lean:68-87`) against text 1711-1727: for every `v, β, c` and `z ∈ LdG(lat c)` with `fv(pr z) = 1` there are a label equality, `γ ∈ UJ`, adelic `η`, `κ ∈ (K β).lev.U` with (1) `η_{v'} = 1` for `v' ≠ eV v`; (2) `γ y_{c'} = y_c η κ`; (3) `loc_P(γ·lat c') = loc_P(LdG(lat c))`; (4) `loc_P(γ·LdG(lat c')) = loc_P(LdG(lat c) ⊔ span{T^{-1}z})`; (5) for `x ∈ LdG(lat c')` with `T·γx ∈ LdG(lat c)`, `fv(pr x) = fv(pr(Tγx))`; (6) the frame clause with multiplier `χ(κ)^{-1}`. All six are in the text, with `D_c = lat c`, `D_c^♯ = LdG`. Match.
- `DnNatTieG` (91-106) against 1711-1730: `g ≠ 0` a residue-linear functional on `lk`; same (1), (2), (6); one lattice identity `loc_P(γ·LdG(lat c')) = loc_P(lat c)`; functional clause for `γx ∈ LkG`, value `g(prk(γx))`. Match.
- Hypotheses of `upNatTie` (`InvSmulMem.lean:281`) and `dnNatTieG_cols` (`ChartTiedLevelChainHost.lean:48`): `I.Ok`, `Pins`, `l`, `Z`, `u`, `a`, `i ≤ m`, `bad`, `Ch`, `chOf`, `K`, `eY`, `eV`, `L`, `ReadsK`, `IdY`, `IdV`, `IdL`. Text 1696-1700: all present.
- `lvSame_zero` (`LvSameZero.lean:335`): any `A : TwAtT`, `A.eVT = refl`, `(A.eFv v).symm (resT μ₀ (A.eVT v) r) = resT a v r`; conclusion `Nonempty (LvSame A 0 (I.eCls0 l u a) (Equiv.refl _) ((I.tw l l0 Z).e0 u a))`. Text 2101-2109: match, including `l0`.
- `fvTieG` (`ChartTiedLevelChain.lean:300`): no `eY`; hypotheses `ReadsK`, `IdV`, `IdL` and the kill condition `t' = π·t ⇒ fT t' = 0` with `π = X.piT u`; conclusion `∃ fMe, FvTieG L eV K fMe ∧ (∀ β v x j r t, j last → t = x_v → r = π̄ x_j → fMe β v (fT t) = resT v r)`. Text 2033-2049: match, both clauses.

Proofs.

- Up, lattices (1785-1812). Checked: at `P`, `D_P = ker f_P ⊂ N_P = D_P^♯`. With `x_0 ∈ N` lifting the projection of `z`, the neighbour is `N_P + R_P q^{-1}x_0`, its functional is `y ↦ f_P(qy)` with kernel `N_P`. Hence (3) and (4); `q^{-1}(z - x_0) ∈ D^♯_P` gives the form with `z` (Lean `loc_sup_le`, 66-75).
- Up, functional (1814-1830). Checked: `qγ D^♯_{c'} ⊂ N_{c,P}`, so `qγx_1 - x_2 ∈ P N_{c,P}`, and `f_{c'}[x_1] = f_P(qγx_1) = f_P(x_2)`. This is the use of `sub_mem` and `d3` at `InvSmulMem.lean:317-325`.
- Up, splice and character (1837-1898). Matches `isPt_up` (224-258: `Splice.exists_splice`, `δ = k ε k^{-1}`, support at the base prime) and `exists_level` (167-207: `y_c δ = γ y_{c'} z`, `z ∈ U_β` from the level reading applied to `(1,κ)`, coset equality from `cosetIn_upP`, `cosetIn_smul_unitary`, and the chart key). `upNatTie` takes `κ = z^{-1}` (307-310, 327-329). I multiplied out `γ y_{c'} = y_c δ z^{-1}`: correct.
- Down (1740-1783, 1900-1937). `dnNatTieG_cols` (49-58) assembles `dn_keeps_chart`, the adelic factorisation, `dn_locP_lat`, `dn_level_functional`, `tr_eq_of_isTr`. The Lean factorisation statement fixes `γ` as the rational part of the chosen move and gives `χ(κ)^{-1}` as the embedded character of the move; the text uses that same `γ` in all three places and says so (1928-1931). I multiplied out `y_c η κ = h_m b^{-1} = γ y_{c'}` with the displayed `η, κ`: correct; `η` is supported at the one base prime.
- `fvTieG` (2051-2098). Follows `exists_equiv_level` (211-250) and the final lines 321-330: `ψ(t) = ρ_P(π̄ t_n)`; `ker ρ_P = π O_v`; factorisation through `ψ`; `fT_ne`, `vT_norm`, `fM_card`; then `f(sz) = [s]ψ(t)` from the last row of `b^{-1}` (`hR.k_T`) and cancellation of `[s]` (`fv_of_smul`). Correct. The source of `|M| = q` (`fM_card`) is now named.
- `lvSame_zero` (2116-2204). The thirteen fields of `LvSame` (`TiedTwSame.lean:17-44`) are all addressed. Equal preferred decorations: `stepZero_corresponding_representatives_same_deco` via `canon`, `orb_iff`, `stepZero_preferred_iff_canonicalRep` (`StepZeroClassesBijectiveSameDeco.lean`), as sketched at 2116-2133. Quotient maps as casts along that equality (`redN`, `redK`, 19-69). Moves: `upA_deco`, `dnA_deco`, `diaA_deco`, including the inadmissible branch (`up_deco_of`, `dn_deco_of`). Transports: `tr_of_deco` (131-149) with `exists_lift` and `mv_unique`, where freeness is `(l.lev u μ₀).free0`, a field of the law hypothesis; the text names it (2168-2170) and is right that only reference freeness is used. `bw`: `bwA` (300-333) with the second clause of `l0 u a`. `eFv` fixes every residue (`hE`, 340-343). Correct.

Depth: for the three formerly outline-level entries I compared the Lean statements clause by clause and read the top-level Lean proofs (`upNatTie`, `exists_level`, `isPt_up`, `sub_mem`, `dnNatTieG_cols`, `lvSame_zero`, the `LvSameZero` field lemmas, `fvTieG`, `exists_equiv_level`). I did not read `deco_up`, `lattices_at_up`, `Splice.exists_splice`, `dn_locP_lat`, `dn_level_functional` or `move_down_adelic` line by line; for those I checked the hand argument mathematically and against the Lean statements.

### A5. Stage and base-law block: FIXED

Text 1596-1632 (`r13:stage-unit`); JSON `round13.stage_and_base_laws`.

- All eight declarations are named with correct files and ranges (checked in the graph): `ColIn.Ok.stp_ok` (50), `unrepresented_step_conditions` (35-48), `StepOk.stepY_ok` (65-103), `FramedForms.main` (145-152), `base_fields_primes_ok` (18-22), `FieldsLaws.fields_ok` (114-165), `BasePrimes.primes_ok` (148-182), `base_fOk` (15-16).
- Figures reproduce: inclusive 12,289; joint cut 4,485; `stp_ok` alone 3,832; difference 653.
- `.unit` observation: `step_gam_mem_UJ` (`StepGamMemUJ.lean:10-16`) is the only caller of `stp_ok` in the root cone and uses only `(hI.stp_ok u a i).unit b g` after the Gram identity of supplier 6. In `stepY_ok` that field is `ufGL_conjTranspose_mul g.1` (line 89); `GStep.Ok.reRep` copies it (18-20). `upNatTie` is the only caller of `step_gam_mem_UJ`. The text gives the two-line proof of `M^*M = 1` and states that the other record fields are proved in Lean and not needed by the hand proof.
- `fields_ok` and `primes_ok` are labelled as base-data facts used elsewhere (for example `InvSmulMem.lean:301`). That is the form review B asked for.

One slip: the call to `step_gam_mem_UJ` inside `upNatTie` is at `InvSmulMem.lean:307`, not 311 (text 1597).

### A6. The two deviation lemmas: FIXED

(a) Tuple independence (`r13:tuple-independence`, 3427-3465; context 3403-3425, 3467-3554). JSON `round13.deviations[0]`.

- Stated as a lemma with hypotheses: one generator prime `P`; common ranks and residue characters; `j < m₂`; `a, h` lattice stabilizers; both tuples under `ChIdx.Ok`, in particular `psi0`; both sharp flags true by `ColIn.Ok.sharp` (`TrueColumnChoicesHeckeCharReferenceEqOne.lean:242`, verified); the same depths `A', B'`; the witness `X` may depend on the depths. It is declared a hand lemma that is not a Lean declaration. The three facts review B asked for (same `A', B'`; `sharp = true`; determinants are `P`-units, so the `muq` and `sq` exponents vanish) are all present, and the `none` index is handled (3415-3417).
- Proof against the definitions (`FiniteSumNonzeroLargeDepth.lean:927-944, 988-989, 1012-1037`; `Loc.om`, `Loc.E1`, `TwistedEisensteinNonvanishing.lean:181-207`): at a generator prime with `sharp = true`, `PhiAt` is `PhiGS(q, psi0P Ch, chiP Ch, ranks)` and does not depend on the tuple. The tuple enters `E1at` only through `cst.psi`, `cst.muq`, `cst.sq`, `A`, `B`. With unit determinants the `om` prefactor is a nonzero constant. `sclLat` makes the adjacent marked entries lie in `q^{-1}O_P` on the support, so `q·chArg` is integral and `psi0` identifies the phases. Hence the normalized sums agree for every `X, A', B'`, and `FiniteSumNonzeroLargeDepth` transfers. The induction (3505-3521) uses the tuple's `nonvan`, the invariance under the source double coset (Lean `unfoldedDatum_ne_zero_of_doubleCoset_source`), and the reference `surj` once with `stabG`; the non-generator clause is empty for `μ₀`. Correct.
- Marked in JSON with `hand_lemma`, three `hypotheses`, `hand_route`, `lean_route` (`cosetOne` 34-56, `idx_nonempty` 58-79, `twSurjG` 18-25, `twNonVanG` 27-34; ranges verified), `cut_roots`, and 5,045 dominated lines (reproduced).

(b) Supported character at a further place (`r13:near-character`, 3840-3935). JSON `round13.deviations[1]`.

- Stated as a lemma: `χ_β(e_v(x)) = val_v(x)^{-1}` for `x ∈ K_β.U_v`, under "the exact hypotheses of `T.furtherPlace_penultimateChart_character_inverseValue`". The Lean statement (`...Statement.lean:12`) concludes `χ(embU x) · valV x = 1` under `StdF`, frame one, the reading with `k_v = 1` on `UnderQ`, `ChiFin`, local agreement off `Q` and chart-character agreement; the text lists the reading, identity-frame and finite-exponent hypotheses on top of "the chart and reference data above". Match.
- The text now says that the proof is direct and names the four bypassed declarations (`AdT.lev_mid` 71-98 and the three statement wrappers). The figure 2,848 reproduces, and the reconciliation with review B's 2,846 is explained correctly.
- Radii: `log` on `v_p(C) > 0`, `exp` on `v_p(Z) > 1/(p-1)`, with `s > 1/(p-1)` and `v_p(C) > s + v_p(e)`. I checked the estimates: `v(C^k/k) - v(C) ≥ (k-1)(v(C) - 1/(p-1)) > 0`, so `v(e^{-1} log B) > s`; likewise for `exp`; `A^e = B` by the one-variable identities. This covers `p = 2` and `p | e`. The rest (rational `d` by density, the reading applied to `b`, `θ_P = d^{-1}`, depth invariance) is as review B found it.
- Marked in JSON with `hypotheses`, `hand_route`, `lean_route`, `cut_roots`, both counts and the `count_method`.

The third entry of `deviations` (`unimodGenus`, completion plus Cayley transform in place of the semilocal route) is a section-B item and is also recorded.

### A7. Pinpoint references: FIXED

The phrase "generic argument(s) of supplier 9" no longer occurs. Five labelled targets exist in supplier 9: `r13:s9-cosets` (1295), `r13:s9-congruence` (1358), `r13:s9-twopoints` (1389), `r13:s9-shrink` (1435), `r13:s9-values` (1494). The four passages:

| Old lines | Now | Reference given |
|---|---|---|
| 2073-2074 (`clsP_tie`) | 2568 | `r13:s9-values` |
| 2703-2709 (top chart) | 3296-3306 | `r13:s9-twopoints` with `mem_framedLevel_iff_two_adelic_points`; `r13:s9-congruence` with `exists_K1_point_congruent`; `r13:s9-cosets` with `decoratedPointClasses_bijective_doubleCosets`; file ranges for all three |
| 3031 (middle fibre level) | 3656-3659 | `r13:s9-shrink` with `exists_stepLevel_shrink` (`ExistsStepLevelSmallerAtFinitePlaces.lean:38-132`) |
| 3038-3041 (middle fibre classes) | 3674-3682 | the same three labels and declarations as the top chart, with file ranges |

Also 2651 (`ipV_norm_tie`) now points to `r13:s9-values`.

## 3. Root-cone coverage (graph)

Root cone of `GlobalTheory.PerTwClose.twistedPeriodAdmissible_of_rowInt`: 15,659 declarations, 88,646 core lines, three `lit` leaves. These reproduce.

Registered for Z4.4: 73 declarations (4 from round 11, 57 from round 12, 2 assembly, 10 from round 13). All 73 lie in the root cone.

1. **Outside every registered cone**: 237 declarations and 1,347 core lines, of which 81 are theorems. This is exactly the class-sum derivation: the root, `perDecTwT_of_std`, `pair_integral`, `pairBDual`, `pairBDualK`, `petersson_eq_sum_restrict_twist`, `perDecTw_of_at`, `perTwAt_of_perDecTw`, with their definitions (416 of the lines are the `DataDIV` structures). That part was confirmed in round 5, was reconfirmed as an implication by R12-B (row 34), and is restated at 4242-4272 with those eight declarations named. No declaration outside the registered cones is unconnected to it.

2. **The three `lit` leaves** (`Published.herm_col`, `exists_cc_eq_neg`, `exists_basis_one_imaginary`) are recorded in `round13.elementary_literature_leaves` as fully proved elementary lemmas, with the seven cones that contain them.

3. **Pieces that review B listed as unlabelled inside registered cones**: stage and base laws (A5, now labelled); `nabDelLoc` path (A2, now labelled); `levOk_twists` (named at four places); `LatGood.hasRatBasis`, `LatGood.step_gram_posDef` and `majAt_classSum` (named at 2666-2686); `period_conj` (registered); twist-place disjointness (`twistPrimes_reference_tuple_eq_empty` named at 3207, 3278).

4. **Remaining unnamed helpers.** None blocks approval; each is a one-sentence labelling matter. Sizes are dominated core lines in the root cone.

| Helper | Location | Dominated | Where it enters |
|---|---|---|---|
| `PerRedTw.exists_orthonormal_frame_twisted` with `D7.X'_posDef`, `factXmDef`, `sig_family`, `sig_dim`, `pos_of_isomEmb` | `TwistedPeriodDecompositionOfClasswiseTwistedPair.lean:22-54`, `PosOfIsomEmb.lean`, `RankBoundMonotoneInDimension.lean` | 245 | "In an orthonormal frame" (4243): existence of the frame from positive definiteness of `X'` |
| `PerRedTw.eW_rep_o_tw` with `Forms.blkRow_mem`, `delSq_rowAct`, `weyl_eq_dual`, `bs_dual_le_weyl` | same file 68-86; `TiedBrRep.lean:33-46`; `BranchingNormalisedOfAdjoint.lean:119-121, 229-233` | 97 (inclusive 9,697, the rest shared with the registered Weyl cones) | restriction to one class stays in the complex span; uses Weyl = dual Weyl over `ℂ`, which the Weyl section proves over `ℚ` |
| `TauLat.tauLatLattice` helpers (`exists_dual_family` and others) | `LatticeExtensionAlongFieldEmbeddingDuals.lean:27-151` | 109 | `tauLatLattice` is named; its proof is not reproduced |
| `AdmPerTw.vAdd_dvd_le`, `card_stabilizer_dvd₂`, `WeightDegreeSizes.pair_add_ge`, `OrbitPlaces.vAdd_*` | `AdmPerTw.lean:14-47`, `WeightDegreeSizes.lean:737-763`, `OrbitPlaces.lean` | about 110 | the valuation bound "each `h_c` divides `D_{Γ,u}`" and the sum inequality (4261-4266); two of them were named in the round-5 chapter |
| `T.eCls0_mu0_eq_self` | `StepZeroClassEquivReferenceTupleEqSelfStatement.lean:7-8` | 156 | one sentence at 4196-4197 |

Inside registered cones there are further internal Lean lemmas that no chapter names (the largest by dominated lines: `FramedForms.frmGSD_ok`, 3,022, inside the A5 block; `Mass.UnimodLoc.exists_isom`, 1,459, inside the recorded `unimodGenus` deviation; `weylEqNablaQ`, 992, inside the hand-proved Weyl section). These sit under hand-proved or explicitly bypassed declarations and are covered by the convention that a registered hand proof replaces its Lean cone. I did not audit that convention entry by entry in this recheck.

So: no project-specific declaration of the root cone is at once outside the hand-proved registrations, outside the earlier-confirmed class-sum part, and unlabelled, except the small helpers in the table above.

## 4. The ten round-13 registrations (statement level only)

For all ten, the name, file, line range and inclusive cone in `round13.new_subtheorems` reproduce exactly from the graph, and all ten lie in the root cone. Status is `pending_review`, as it should be.

| Declaration | Lean | Cone | Statement in text | Check |
|---|---|---|---|---|
| `TransDual.nabDelDual` | `TransportedWeylLatticeHermitianDuality.lean:278-309` | 7,581 | 472-487 | Exact; fully checked under A1 |
| `TC.ChTw.charts_tuple_trivQ` | `ChartsTupleTrivQ.lean:86-101` | 40,240 | 3731-3789 | `1 ≤ i < m`, `Q ↔ UnderQ`, reference `ReadsK`; conclusion: finite `Ch`, reading with `k_v = 1` on `UnderQ`, `Uloc` equal off `Q`, finite exponent, equal characters on elements trivial at `Q`. All present, but spread over prose; no single displayed statement |
| `T.localMove_classRep_iff_localConditions` | `...Statement.lean:7-12` | 14,205 | 3748-3781 | Four-part equivalence (`γ = 1`, coset preserved, local move condition, `LocCQ`); both directions stated |
| `TC.twPack_ex` | `TrueColumnChoiceTwistedChainsFormsClasses.lean:272-319` | 54,944 | 4104-4160 | Hypotheses `Q ↔ UnderQ`, `StdF`, `glevJ.fr = 1`, `CarH`; conclusion one stage package. Match |
| `TC.tw_chains` | same file 464-484 | 62,689 | 4162-4203 | Conclusion `∃ T J W`, `TwChMu0 ∧ StdW ∧ Nonempty SymmetricTwistedJointForms`; all three mentioned (4194-4199). The hypothesis `StdF ∧ StdLvC` is not restated in this paragraph |
| `TwAtStd.twAtT_exists` | `DecoStabTrivial.lean:146-176` | 14,468 | 4166-4179 | `eVT = refl` and `eFv (res_a r) = res_{μ₀} r`; consistent with the hypothesis of `lvSame_zero` |
| `TC.charts_funKilled` | `InclMulInvMul.lean:422-439` | 16,880 | 2527-2540 | Retains `Lb`, `Uloc`, `U`, character on underlying elements, `y`, `stabI`, `ReadsK`; adds `FunKilled`. Exact |
| `PerConj.period_conj` | `CevInjective.lean:219-225` | 16,088 | `ch_P_r11.tex:961-1001` (recorded as `proof_source`) | Five conclusions (conjugate-linear `jM`, injective, onto `ptC`, values in `ptC`, period identity, positivity). Match |
| `FormSym.readsK_one` | `MemFiCComp.lean:147-159` | 13,620 | 2340-2347 | Singleton reading with the witness `k(β)`. Exact |
| `T.nonempty_classMap_above_lastStep` | `...Statement.lean:7-8` | 4,307 | 4144-4150 | `m < i`, a class map to the reference tuple. Exact |

No statement-level discrepancy. These ten remain to be confirmed at proof level by whoever closes the round-13 register; the A1 entry is already checked in full here.

## 5. Minor edits

1. `ch_P_r12.tex:1597`: `InvSmulMem.lean:311` should be `307` (the call to `step_gam_mem_UJ` inside `upNatTie`).
2. Class-sum paragraph (4242-4272): name `exists_orthonormal_frame_twisted` with `D7.X'_posDef` as the source of the orthonormal frame; name `eW_rep_o_tw` (with `blkRow_mem`, `weyl_eq_dual`) for "restricting to the `c`-th component stays in the form space", and say that Weyl = dual Weyl over `ℂ` follows from the Weyl section; name `vAdd_dvd_le`, `card_stabilizer_dvd₂`, `pair_add_ge` at the valuation bound.
3. Name `T.eCls0_mu0_eq_self` at 4196-4197.
4. `ch_P_r12.tex:1885`: the adelic element `z = y_{c'}^{-1}γ^{-1}y_cδ` reuses the letter of the dual vector `z` of the up move (1785); rename one.
5. `ch_P_r12.tex:1866-1867`: add the name `Splice.exists_splice` next to `ValuedInvMulLe.lean:146-272`.
6. Optional: give `charts_tuple_trivQ` and `tw_chains` one displayed statement each (hypotheses and conclusion together), as was done for the two deviation lemmas.

## 6. Bookkeeping and claims

- `status.json`: `round13.required_fixes` 1-7 are `addressed`; `original_inputs.Z4.4.accepted_status = partial`, `completion_candidate = pending_review`, `reconfirmation_received = false`; `accepted_grade_changes = []`; `grade_counts.original_complete = 13`; `build = deferred until approval`. Consistent with the chapter (4300-4312, 4351-4353).
- No statement in the chapter or in `status.json` claims that Z4.4 is already complete, and none claims that RH or GRH is proved.

## 7. Summary

All seven required fixes are in place and correct. The transported duality, the only link from the Weyl results to the root, is now registered and proved in full; I checked both equalities and the period-numerator specialization step by step against Lean. The three formerly outline-level supplier-8 entries now have real hand proofs whose statements match Lean clause by clause. The stage-law block, the two alternative arguments and the localization path are labelled correctly, with figures that reproduce from the graph. The root cone has no unaccounted project-specific declaration beyond a handful of small helpers in the class-sum paragraph (at most 245 dominated lines each) that should be named.

Verdict: **APPROVE AFTER MINOR EDITS** (section 5, items 1-5). With those made, Z4.4 may be recorded as complete; the ten new registrations stay `pending_review` at proof level except `nabDelDual`, which is confirmed here.
