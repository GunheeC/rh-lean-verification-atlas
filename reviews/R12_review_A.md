AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

# R12_review_A

AI review report produced during this project; file names are internal working names.

- Internal source file: `out/R12_review_A.md`
- SHA-256: `ce0beaa9b665080b6f21da3c25242bccbaff64b46044daa790ab5268fc58e4df`
- Report scope: Round-12 independent review, part A: `ch_P_r12.tex` lines 1-1772

## Internal report

The report below preserves its original verdict, scope and unresolved points. Historical review-machine home prefixes are displayed as `${REVIEW_HOME}`; the source checksum above identifies the original report. Source line numbers in other records count from its original title.

# Round-12 independent review, part A: `ch_P_r12.tex` lines 1-1772

Scope: R11 corrections (2-106), Z1.2 trust ledger (107-162), `r12:weyl` (163-415), `r12:point` (416-576), suppliers 4 (577-807), 9 (808-1311) and 8 (1312-1772) of the Z4.4 root `twistedPeriodAdmissible_of_rowInt`. A second reviewer covers lines 1773-3616 (suppliers 1 and 7, assembly, outcome).

Sources: cleaned copy `${REVIEW_HOME}/src/rh/src`; all line numbers below are the original numbering (commit `40e56bab`), read with `git show`. Graph: `graphq.py` and a reachability pass over the same `graph_cache.bin`.

Nothing here, in the chapter, or in the Lean development is treated as establishing RH or GRH. This review only compares hand proofs with the Lean statements they label.

## 1. Verdicts

26 declarations are registered `pending_review` in my scope (`round12.subtheorems`, groups `weyl`, `point`, `4`, `9`, `8`). For all 26 the file, line range and inclusive cone size in `status.json` reproduce exactly from the graph (cones counted as distinct core source lines, ignoring auto-generated `:0-0` declarations).

"Depth" column: **S** = Lean statement compared clause by clause; **P** = Lean proof term read and compared step by step with the hand proof; **M** = hand argument checked mathematically on its own, without reading the full Lean proof.

| Group | Declaration | Lean location | Depth | Verdict |
|---|---|---|---|---|
| weyl | `GlobalTheory.T.standard_weyl_lattices_fock_dual` | `StandardWeylLatticesFockDualStatement.lean:14-15` (= `StdDual.std_dual`, `StandardWeylLatticesFockDual.lean:237-307`) | S, P, M | **CONFIRMED** |
| weyl | `GlobalTheory.T.transportedLattice_localization_free_le_coefficientSpace` | `...LeCoefficientSStatement.lean:14-15` (= `nabDelLoc_free_leVV`, `...LeCoefficientS.lean:217-234`) | S, P, M | **CONFIRMED** (two labelling gaps, 3.3) |
| point | `PtExist.exists_modify` | `ValuedLtOfMem.lean:219-295` | S, P | **CONFIRMED** |
| point | `PtExist.exists_isPtOf_cm` | `ValuedLtOfMem.lean:299-337` | S, P | **CONFIRMED** |
| point | `T.exists_adelicPoint_decoratedLattice_allTwists` | `...AllTwistsStatement.lean:7-8` (= `exists_ptOf_twists`, `:11-60`) | S, P | **CONFIRMED** |
| point | `Formalism.L2.Col.decoPtSurj_of` | `AdelicLemmas.lean:1245-1401` | S, P (first 60 and last 20 lines), M | **CONFIRMED WITH GAPS** |
| point | `PtExist.unimodGenus` | `ValuedLtOfMem.lean:102-123` | S, M | **CONFIRMED WITH GAPS** (hand route differs from Lean; 4.1) |
| 4 | `T.exists_hermitian_data_carT_of_std` | `HermitianDataAtLevelPrimeStatement.lean:8-9` (= `TC.hermitian_data_at_level_prime`, `:18-62`) | S, P (assembly), M (sub-suppliers) | **CONFIRMED WITH GAPS** |
| 9 | `T.decoratedPointClasses_bijective_doubleCosets` | `...DoubleCosetsStatement.lean:8-9` (= `classes_bijective`, `:34-83`) | S, P | **CONFIRMED** |
| 9 | `Mem.Col2.mem_locW_hlat_iff` | `MemLocWHlatIff.lean:14-30` | S, P | **CONFIRMED** |
| 9 | `T.exists_K1_point_congruent` | `ExistsK1PointCongruentStatement.lean:8-9` (= `exists_K1_isPtOf`, `:11-52`) | S, P (top level), M | **CONFIRMED** |
| 9 | `T.mem_framedLevel_iff_two_adelic_points` | `...TwoAdelicPointsStatement.lean:8-9` | S, M | **CONFIRMED WITH GAPS** |
| 9 | `TwP.til_tw` | `ExtMMulVecFix.lean:253-377` | S, M | **CONFIRMED WITH GAPS** |
| 9 | `T.tuple_integralForms_row_place_by_place` | `...RowPlaceByPlaceStatement.lean:11-12` | S, M | **CONFIRMED WITH GAPS** (dependency mislabelled, 3.3) |
| 9 | `T.tuplePrimedSpaceClasses_level_and_comparison` | `...LevelAndComparisonStatement.lean:9-10` | S, M | **CONFIRMED WITH GAPS** |
| 9 | `T.tupleLayerCompatibilities_of_X_prime` (supplier 9) | `...OfXPrimeStatement.lean:9-16` (= `TC.tupleLayer_compatibility`, `:17-46`) | S, P (assembly) | **CONFIRMED WITH GAPS** |
| 8 | `TC.exists_level_projections` | `ReductionModPrimeLevelPrimeSmulEq.lean:197-231` | S, P, M | **CONFIRMED** |
| 8 | `LevFun.fvTieG` | `ChartTiedLevelChain.lean:300-330` | M | **CONFIRMED WITH GAPS** |
| 8 | `TC.dn_locP_lat`, `TC.dn_level_functional`, `TC.dn_keeps_chart` | `DownMoveLocalDualLatticeEqLevelPrime.lean:88-120`, `MoveDownLevelFunctionalEq.lean:100-130`, `MoveDownLevelPrimeKeepsChart.lean:198-202` | S, M | **CONFIRMED WITH GAPS** (group) |
| 8 | `TC.bw_tie` | `IsBasisAtOfIsLocBasis.lean:180-266` | S, M | **CONFIRMED WITH GAPS** (dependency mislabelled, 3.3) |
| 8 | `DnMove.dnNatTieG_cols`, `UpChart.upNatTie` | `ChartTiedLevelChainHost.lean:48-58`, `InvSmulMem.lean:281-329` | M (outline only) | **CONFIRMED WITH GAPS** (group; lowest depth of this review) |
| 8 | `TC.StepZero.lvSame_zero` | `LvSameZero.lean:335-371` | M (outline only) | **CONFIRMED WITH GAPS** |
| 8 | `T.tupleChains_levelStructure_compatible_at_levelPrime` (supplier 8) | `...AtLevelPrimeStatement.lean:8-9` (= `tw_lv_tied_and_same`, `:94-134`) | S, P (assembly, incl. `exists_lvTied_of_std` 17-40 and `lvSameMu0` 44-90) | **CONFIRMED WITH GAPS** |

No declaration is NOT CONFIRMED. I found no mathematical error in any hand proof I checked. "With gaps" means sketched sub-lemmas, unlabelled Lean inputs or a divergent route, as itemised below. For `dnNatTieG_cols`, `upNatTie` and `lvSame_zero` I did not compare the Lean statements clause by clause and did not read the proofs; the verdict rests on the hand argument being coherent and on the assembly consuming them as described.

The sections outside the registered declarations:

| Section | Verdict |
|---|---|
| R11 corrections (2-106) | Applied correctly; three small R11 items not taken up (2.1) |
| Z1.2 trust ledger (107-162) | Accurate; one pass-through described as a discharge (2.2) |

## 2. Corrections queue and trust ledger

### 2.1 Corrections to the R11 queue (`ch_P_r12.tex:2-106`)

I checked each of the eight requested corrections in `R11_review.md` section 5.

| R11 item | Applied at | Result |
|---|---|---|
| 1. `rankTwo` belongs to Z1.1 | 19-51; `round12.trust_ledger.Z1.1.reassigned_from_Z1.2`; `round11.subtheorems[0].unit = Z1.1` | Correct. I re-ran the traversal: none of `rankTwo`, `tan`, `selLow`, `locHigh`, `cupUnr`, `b1absO`, `dualNO`, `core_alt_bis` is reachable from `adjointLiftingTheorem_of_locPrints_of_core`; all eight are reachable from `ends0_alt`. |
| 2. Z1.2 remaining list | 107-162 | Applied, see 2.2. |
| 3. Z4.4: Weyl boundary, assembly conditional | 163-415; `original_inputs.Z4.4.assembly.status = pending_review` | Applied. |
| 4. `rankTwo` edge cases and labels | 19-46 | All five sub-items present: finite residue field and non-unit `ℓ` (27-30, `okFin`), `C = 0` (31), finiteness of `X` (24-27), discharge site `tan` with `selLow`, `derOf`, `zn_ext` (39-46), structure theorem cited (32-36). |
| 5. Supplier 2 | 54-75 | `GLevH` named, `T ≠ g_i`, positive rank, `cmUnram` route stated, local-global inputs cited, Iwahori lemmas labelled "proved in Lean and sketched". |
| 6. Supplier 3 | 77-92 | Inputs labelled "Lean inputs to the hand proof", with the missing sentences added. |
| 7. Supplier 6 | 98-103 | `StdTied` is now the first conclusion; `e_Y` independent of `c`. |
| 8. `til_tw` range | 104-105 | `ExtMMulVecFix.lean:253-377`, correct. |

Not taken up (all minor, from R11 section 3.1 items 3, 5, 6):

- `tanA` and its two callers (`linkedUnlE_alt`, `linkedUnlE_holds_alt`) and co-suppliers `unitOf`, `linkOf`, `gwlOf`, `leOf2` are still not named.
- `DAmitsur.lean`, `IrrIffSpan.lean`, `CycInertia.lean`, `LocStab.lean`, `GlobalB.lean` (shared root-cone lines used as standard facts) are still uncited.
- Of the direct suppliers of `ordinary_vanishing_two_of_printed_hida`, the text table omits `count` (it is in `status.json`), and `b0Ex`, `lamEx`, `phiAll`, `nmAbs` appear in neither.

Line-reference slips in this subsection: `LeAdicClosure.lean:157-168` (`Space` is 157-165); `ClassPairMovedOfMultipliesLocalFunctional.lean:86-105` (`ld_lattice` 88-91, `ld_loc` 96-105); `PBwLocGen.lean:311-325, 344-384` (declarations end at 324 and 383). Immaterial.

### 2.2 Trust ledger, Z1.2 at stage C (`ch_P_r12.tex:107-162`)

Accurate in every named item. Checked against the graph: all 26 ledger entries (`local_crystalline` 7, `vanishing` 8, `uniform_count_inputs` 11) have correct files and line ranges; the seven crystalline comparisons are in the Z1.2 root cone and the other 19 are not; all 26 are in the Z1.1 root cone. `FontaineBcris` (`OneSubPhiOntoOfFilZero.lean:18-20`), `fontaineBcrisBasicTheorems_proof` and `SmGL.IrrRep` are literature-class leaves of the root cone, as stated. Assigning stage C on the ground that the second premise is supplied only through the Z1.1 Hida/automorphy work is justified.

Findings:

1. **`locPrints_of_litN` is a pass-through, not a discharge** (`ch_P_r12.tex:111-114`; `status.json` key `local_record_discharge`). The declaration is

   `theorem locPrints_of_litN (hN : LiteratureRankNHypothesis) : Loc.LocalPublishedTheorems := ⟨hN.coh.lfK, hN.coh.ltK, hN.coh.leK, hN.coh.lf, hN.coh.lt, hN.coh.le, hN.coh.bk⟩`

   (`HVFinalU.lean:12-13`), called at `ThFinal.lean:18` with `hH.litN`, where `hH : HypothesesH'` is itself a hypothesis of `adjoint_lifting_of_cohomology`. The seven fields (local finiteness, local Tate duality, local Euler characteristic in two versions each, and `BlochKatoLocal`) are therefore published statements carried as hypotheses up the call chain. The text's "the first premise comes from `locPrints_of_litN`" and the JSON key name suggest the premise is discharged there. It should say: projected from `LiteratureRankNHypothesis.coh`, which enters as the hypothesis `HypothesesH'.litN`. I did not trace where `HypothesesH'` is finally supplied; the ledger should name that site. The sentence at 120-122 ("identifies a formal input; it does not verify a printed comparison theorem") is the right caveat and should be attached to these seven fields as well.

2. **Cone table, "Local" column** (129-137). With the same graph I get 374,411 and 341,282 for the first two rows (and 375,725 for `core_alt_bis`, 16,175 for `crWt0`), that is, the "R11 review" column, not the "Local" column. The other rows agree. The 3-4 line difference is immaterial, but the claim "recomputed with the local pinned graph" does not reproduce for those entries; `status.json` carries the same four values.

3. Discharge sites for the `b1absO`/`b1O` constants (147-161) are named correctly and match the graph ranges.

## 3. `r12:weyl` (`ch_P_r12.tex:163-415`)

### 3.1 Statement comparison

`standard_weyl_lattices_fock_dual`: for `K` a number field with `[StarRing K]`, `ι` a fintype, `n : ℕ`, `lam : ι → DomWeight n`, and `x ∈ VV K lam`:
`(∀ y ∈ delStd, pairP lam 1 y x ∈ range(𝓞 K → K)) ↔ x ∈ nabStd` and `(∀ y ∈ nabStd, ...) ↔ x ∈ delStd`. The display at 169-172 states exactly this, with `x ∈ VV` as a standing hypothesis (174), identity Gram matrices, and `R = 𝓞 K`. Match.

`transportedLattice_localization_free_le_coefficientSpace : NabDelLoc ∧ NabDelFree ∧ NabLeVV` (`CoefModLemmas.lean:100-118`). Localization is `localization₂ w N = {x | ∃ s ∉ w, s • x ∈ N}`. The three assertions at 378-394 are: `(P_T)_w = act(B_w)(T_w)` for any family of full lattices and any local basis family (both `∇` and `Δ`); with a global frame `P_T = act(B) T`; and `nabP ⊆ VV`. Match, including quantifier order (lattices, then `w`, then `B`).

### 3.2 Proof check: the two dualities

This is the direction R11 recorded as open. I checked the argument in full; it is correct and complete.

1. *Setup* (184-195) matches `dualWeyl`, `rowGen`/`rowDiv`, `hw`, `applyWord`, `weyl` (`StatementA.lean:24-73`) and `bDual` (`StatementE.lean:21-45`; the text says 20-44).
2. *`B(h,H) = H(I)` on `V_ν`* (201-207). The row-weight argument is right: a product of initial-column minors with the row weight of `h` must use row 1 in every minor, then row 2 in every minor of size at least 2, and so on, so it is `±h`; other row weights are orthogonal to `h` and vanish at `I`. The spanning statement it needs is obtained from the leading-term elimination over `ℚ`, which is derived from column invariance alone, so there is no circularity.
3. *`∇_ℤ ⊆ Δ_ℤ^#`* (208-211): `B(A^t h, F) = (AF)(I)`. Matches `nablaEqDualWeylOf`, forward half (`ApplyWordMemDualWeyl.lean:110-135`).
4. *Coefficient extraction* (213-234). On lower unitriangular matrices the strictly lower exponents determine the diagonal ones through the column totals, so the coefficient is `[X^e]F`. The right-to-left installation order is justified correctly: when position `(a,s)` is installed, every earlier entry has column at least `s` and lies strictly below the diagonal, so row `s` is still `e_s`.
5. *Leading exponent is interlaced* (236-273). I re-derived the induction. With allowance `s`: `G(X,Y+tX) = (Y+tX)^e L`, `L ≠ 0`, so `e ≤ s` and `deg_t L ≤ s-e`; `L(1,-t) = w_K(t)`, and `L` is homogeneous of degree `K` in `(X,Y)`, so `deg_t w_K(t) ≤ s-e+K`; the leading term of `G` is `X^K Y^e` times that of `w_K`; induction gives `Σ_{2≤b≤a} e_b ≤ s-e+K + Σ_{2≤b<a} K_b`, which is (*) with allowance `s`. Correct, and it is the definition `InterlacedAt` (`StatementC.lean:34-35`). The restriction to the graded component (244-248) is valid because the substitution preserves the grading and the component contains the leading monomial.
6. *Tableau and monic bideterminant* (275-294). (*) with `a = L_s[k]` gives `L_{s-1}[k] < L_s[k]`; columns form an initial segment because `ν` is antitone; the diagonal term is the unique lex-leading monomial. Correct. Lower triangularity of `m` follows.
7. *Integral straightening* (296-305). `[X^m]F ∈ ℤ` because `m` is lower triangular (step 4); subtracting `[X^m]F · D_m` keeps all lower triangular coefficients integral and lowers the leading exponent. Correct.
8. *The other dual* (307-323). `Δ_ℤ` is a full lattice in `V_ν` (orthogonal complement is zero by steps 4 and 6 and positivity), so `Δ^{##} = Δ`. Matches `weyl_isLattice`, `dual_dual_of_isLattice`, `weylEqDualNablaOf` (`ApplyWordMemDualWeyl.lean:182-196, 261-321`).
9. *Number field and tensor step* (325-348). Compared line by line with `exists_dual_bases` (145-235) and `std_dual` (237-307): dual bases over `ℚ`, base change of both lattices (`weyl_toK`, `dualWeyl_toK`, `span_image_eq`), factorisation of the Fock form over blocks with the `extNorm` denominator (`hpair`, 281-299), conjugation preserving `𝓞 K` (`hc`, 300-302), and the coordinate test `dual_span_iff` (25-54) applied in both orders.

Route difference, harmless: Lean takes `b` to be the integral standard-monomial basis `sSBasis ℤ` of `∇_ℤ` and defines `d = N·Q^{-1} b`; the text takes an abstract `ℤ`-basis `d_i` of `Δ_ℤ` and its dual `b_i`. The hand route avoids the linear-independence half of the standard monomial theorem and is valid.

### 3.3 Proof check: transported lattices

`locP_transLat` (`...LeCoefficientS.lean:157-215`) is reproduced faithfully at 378-388, including the choice `s_v ∈ v^{k_v} \ w` (Lean: `exists_dvd_mul`, 67-85) and the two finiteness reductions. `transLat_colLat` and `mem_of_forall_locP` are at 389-391, `mem_VV_of_locP` at 392-394. Correct.

Gaps:

(a) **The two stability theorems are argued but not cited.** Frame independence is `indep_of_stable` applied to `GlobalTheory.T.polyAction_mem_locP_nabStd_of_isBasisAt` and `..._delStd_of_isBasisAt` (`NabIndepAndDelIndepLocalConditions.lean:39-43`; statements at `ActPMem...Statement.lean:14-15`, cones 410 and 675 lines). The paragraph at 353-368 proves both by hand (generation of `GL_n(R_w)` by elementary and diagonal matrices; divided row operations prepend letters; diagonal units scale words), and the argument is correct, but it cites only `isBasisAt_inv_mul`, `indep_of_stable`, `nabIndep_and_delIndep`. The substance is in the two uncited theorems.

(b) **Uncited standard facts**: `GL_n` of a local ring is generated by elementary and invertible diagonal matrices; a submodule of a finitely generated free `ℤ`-module is free; a finitely generated torsion-free module over a DVR is free (this is `LatBasisAt.basisAtEx`, also not named at 373-375).

(c) **The localization identity reaches suppliers 8 and 9 through a different Lean theorem.** The text says the integral tests "depend on this round's transported-localization candidate" (1008-1011, 1041, 1607, 1633, 1769-1770, 1309-1310). In the graph, `ValLat.mem_localization_delAtr` (`MemClosureIff.lean:141-150`) calls `Formalism.L2.DIV.nabDelLoc` (`CoefficientsModP.lean:24`) `= nablaDeltaLocal_holds` (`NablaIndependenceHolds.lean:578-580`, cone 5,665). The registered `GlobalTheory.T.transportedLattice_localization_free_le_coefficientSpace` is **not** in the cone of `bw_tie`, `tuple_integralForms_row_place_by_place`, supplier 8 or supplier 9. Its only callers are `TransDual.nabDelDual` and `TransLattice.nabDelLattice`. Both Lean theorems prove the same proposition `NabDelLoc`, so the hand proof of 3.3 does cover what suppliers 8 and 9 need; nothing is mathematically missing. The labelling is wrong, and the correct discharge site (`Formalism.L2.DIV.nabDelLoc`, with `basisAtEx`, `tauLatLattice`, `du_dualFr_lattice`) should be named.

(d) **`TransDual.nabDelDual` is not registered.** It is the only caller of `standard_weyl_lattices_fock_dual` and the only route by which either Weyl result enters the Z4.4 root cone (`TransportedWeylLatticeHermitianDuality.lean:278-309`, cone 7,581; callers `ColPeriod.pairBK_mem_one`, `PeriodClassSum.pairBDualK`, and the wrapper `T.transported_weylLattice_hermitianDuality`). It appears in the chapter only in the twelve-line sketch at 403-414 and nowhere in `status.json`. The sketch is accurate as far as it goes (dual frame `B^* G B' = 1`, conjugate place in the first argument, simultaneous denominators on a finite generating set, intersection over `w`; these are `exists_dual_frame`, `isBasisAt_hdual`, `mem_localization_dual`, `dual_of_local`). It does not mention `pairTransport`, `dualFr_lattice_and_hdual`, or `delStd_le_nabStd` (used at line 294 for `delP ⊆ VV`). For a completion claim on Z4.4 this theorem should be registered and given a full proof. I did not verify the remark "used with trivial star and `G = 1` at the period numerator".

Line-reference slips: `StatementE.lean:20-44` (21-45); `UnitriMonomialOfLowerTri.lean:35-141` (`coeff_single` 36-58, `wordOf_eq` 141-156); `StandardWeylLatticesFockDual.lean:129-151, 167-235` for `exists_dual_bases` (145-235).

## 4. `r12:point` (`ch_P_r12.tex:416-576`)

### 4.1 `unimodGenus` (418-480)

Statement: for `n > 0` and every full lattice `N` unimodular for `hStd`, there is `x ∈ UAd` with `globLat x stdLat = N` (`Inputs.lean:51-53`). Match.

Lean proof: `Genus.exists_globLat_eq` applied to `SelfDualPoint.mem_genus` with `hc.cmUnram` (`ValuedLtOfMem.lean:121-123`). `mem_genus` (cone 2,024) rests on `Mass.UnimodLoc.exists_isom_of_isUnimodularAt` (`ExistsIsometryOfUnimodularLatticesAtPlace.lean:229-245`), which works with semilocal rings inside `E` and produces a rational unitary directly (`exists_unitary`).

The hand proof takes a different route: classify self-dual lattices over the completion (split pair, or unramified field with an orthonormal basis by norm surjectivity), then approximate the local unitary by a rational one through the Cayley transform. I checked it: ramification is excluded by `cmUnram` (a ramified prime has trivial conjugation on the residue field); the diagonal-nonvanishing argument via the trace form is right, including characteristic 2; unit norms are surjective by successive approximation; `λ = (t+δ)/(t+δ̄)` gives infinitely many norm-one scalars, so `1+λu` can be made invertible in each factor; skew-adjoint matrices have a rational structure; stabilisers are open. The argument is valid.

Gaps:

- The text presents this as a reading of the Lean source ("See `ExistsIsometryOfUnimodularLatticesAtPlace.lean:186-245`"). It is an alternative proof and should be labelled as one, as was done for the splitting argument in supplier 2.
- "Duality commutes with completion" (431-436) and "equality of full lattices is detected at all finite primes" (479-480) are stated with one-clause justifications.
- **Literature-class nodes in the cone.** The cones of `unimodGenus`, `exists_isPtOf_cm`, `exists_adelicPoint_decoratedLattice_allTwists`, `tuplePrimedSpaceClasses_level_and_comparison`, supplier 9, `upNatTie` and supplier 8 contain three nodes the graph classifies `lit`: `GlobalTheory.Published.herm_col`, `.exists_cc_eq_neg`, `.exists_basis_one_imaginary` (`PublishedTheorems/AdelicLattices₂/AlgebraMapNormOfBasisOneSqrt.lean:33-36, 252-257, 259-277`). I read them: all three are fully proved elementary lemmas (a matrix identity, existence of a purely imaginary element, a basis `{1, θ}`); they are not the `Landherr` or `HasseNorm` propositions defined in the same file, and they are not hypotheses. So `new_publication_citations = 0` is substantively right. The chapter and `status.json` should still record them, because a reader of the graph will see `lit` leaves under seven "no new publication" candidates.

### 4.2 `decoPtSurj_of` (482-508)

Statement: `UnimodGenus → RedSurj → IsSplitSet (ST ∪ SG) → Disjoint ST SG → DecoPtSurj`. Match. The Lean proof (1249-1300, 1385-1401) is the one described: `r_P = red_P ∘ pullV x0`; `lin_factor` in both directions gives `Y_P ∈ GL_n(k_P)` at `S_G`; a matrix with the functional as last row at `S_T`; one integral unitary `k`; `x = x_0 k^{-1}`; denominators cleared on `N_P`; zero off `N_P`.

`RedSurj` is a hypothesis, discharged at `ValuedLtOfMem.lean:309` by `reduction_surjective_bis`. The text labels this correctly and proves by hand only the identity-Gram, standard-frame instance that is used. That scope is stated (498-500). The hand proof of the instance is correct. Verdict "with gaps" only because I did not read lines 1300-1385 of the Lean proof.

### 4.3 `exists_modify`, `exists_isPtOf_cm`, all twists (510-575)

Compared with the Lean proofs line by line.

- `exists_modify`: glue matrix `G` and inverse `G'` (226-237), unitarity via `sig_glue` (251-256), integrality at `P` by `valued_pullV_le` and `valued_symm_le` with `carries_globLat` (258-284), at `P̄` by `int_of_uni` (285-286), three conclusions (287-295). The text follows this exactly. The frames are rational (`Sp E n ≃ₗ[E] Sp E n`); the text's "matrix of the prescribed frame" should say so.
- `exists_isPtOf_cm`: rank zero by the identity; otherwise `decoPtSurj_of` then `exists_modify`, with `c3` preserving the residue data because `S_T`, `S_G` are disjoint from `Q ∪ Q̄`. The warning at 549-554 that frame modification alone does not give existence is correct.
- `exists_ptOf_twists`: the four conjugate-exclusion cases (48-60) are the ones at 556-566, using `piT_cop`, `T_notMem_vGs`, `good_of_mem`, `levOk_twists`.

Callers (graph): `exists_isPtOf_cm` is used by `exists_ptOf_twists`, `ColIn.Ok.exists_isPtOf`, `RowTie.exists_cls`, `Splice.exists_splice`, `tuplePrimedSpace_classes`; `exists_modify` also by `exists_K1_isPtOf`, `TwUnit.exists_tw`, `UnitaryLift.exists_lift`, `ApproxZero.exists_K1_element_local_support`. The text's "used by several of the column constructions" is right; the list could be given.

Slips: `ValuedLtOfMem.lean:219-296` (295); `LevOkTwists.lean:24-80` (`levOk_twists` ends at 85); `...AllTwists.lean:11-59` (60).

## 5. Supplier 4 (`ch_P_r12.tex:577-807`)

Statement: exact (hypotheses `Ok`, `Pins`, `l`, `Z`, `H`, `F`, `StdF ∧ StdLvC` for all `u`, `CarH H F`; conclusion one `A` with `CarT`, `SymmetricAdelicCompatibility`, `SymmetricStabilizerMapCompatibility`). The assembly at 783-800 matches `hermitian_data_at_level_prime:19-62` field by field: eight calls; `CarT` = two `rfl`, `hcar`, `hlat`, two coordinate projections, the middle cancellation, final vector, move matrix; six adelic conditions from up/down/diamond at `i = 0` and `i > 0`; `hstab A hT`.

Sole caller: `colsTiedSym_std` (`ExistsStandardColumnComparisonsTrueColumns.lean:20-72`), where `F` comes from supplier 1 and `CarH` from supplier 2 after supplier 3. The text's closing sentence ("with `F_u` and `CarH` as hypotheses") is the right scope.

Sub-suppliers, compared with the definitions `SeenCl`, `DiscCl`, `UpCl`, `DnCl`, `DilCl` (`MemSmulLk.lean:209-253`):

| Step | Text | Check |
|---|---|---|
| Seen prime | 592-606 | Fully checked. `ν(π+π̄) = 0`, `ν(yπ̄ + ȳπ) > 0`, hence `P ⊆ {ν > 0}` and equality by maximality. Gives both alternatives of `SeenCl`. Correct. |
| Discriminant quotient | 608-633 | Fully checked. `N/L ≅ 𝓞/(π)`, `L^♯/N ≅ 𝓞/(π̄)`, coprime supports, so `L^♯/L ≅ 𝓞/(T)`. Matches `DiscCl`. Correct. |
| Middle projections | 635-656 | `L + P L^♯` identity and cancellation of `res_v(π̄)` checked. Correct. |
| Transport | 658-694 | Statement-level. The displayed relation and the three consequences match `SameOff` and the off-place clauses of `UpCl`/`DnCl`/`DilCl`. |
| Up, down | 696-727 | The displayed lattice equalities and functional identities are exactly the clauses of `UpCl` and `DnCl`. Proofs not read. |
| Diamond | 729-763 | Fully checked: `e = (1+α/d)/2` is idempotent with `ē = 1-e`; `μ = k^{-1}e + k(1-e)` has `μμ̄ = 1`; `kμ` acts as the identity once `e` is oriented. Correct. |
| Classes | 765-781 | Statement-level. |
| Stabiliser map | 792-801 | Deferred to the supplier-4 paragraph of the round-11 chapter; not re-checked here. |

Gaps:

- "Since `T ≠ 2`" (734): the source is the data field `D.T_ne_two u` (`PSplitT.lean:272`); not named.
- Hensel's lemma is used without citation; the text gives the Newton iteration in a sentence, which is adequate.
- The transport, up and down paragraphs compress about 600 Lean lines into statements of what is transported; they are outlines, not proofs. They should be labelled "proved in Lean, outlined" unless expanded.
- The stabiliser comparison depends on a cross-reference to another chapter.

Slips: `DualModClassLatticeEquivQuotient.lean:18-33` (18-32); `HostPrimesOverLevelPlace.lean:20-37` (20-36); `AdelicConjugateCharacterStandardForms.lean:133-159, 213-237` (133-158, 213-235); `HermitianUpMoveAtLevelPrimePlace.lean:19-77` (19-72); `DiamondOperatorHermitianSideLevelPrime.lean:219-251` (219-249); `AdmissibleOfSplitAndRoundTrips.lean:86-189` for `local_diamond_of_split_idempotent` (151-178).

## 6. Supplier 9 (`ch_P_r12.tex:808-1311`)

Statement: exact. The text's statement paragraph (810-820) omits two details that are in Lean: the law `l0 : I.Law0 l`, and that the top-reading hypothesis is required only for `a ≠ μ_0` and `1 ≤ m`. The assembly (1291-1310) matches `tupleLayer_compatibility:24-46` field by field: `cls`, `Lb`, `chi_fin`, `val`, `norm`, `til`; `eWz = refl`, `evz`, `jM`, `per`; the two generator conditions; the four `StdP` fields.

Sole caller: `colsTwPTiedS_std` (`TrueColumnChoiceExistsStandardChainData.lean:45-56`). There `Lv` and `StdLv` come from supplier 8 (line 54) and the top-point hypothesis `hPt` from supplier 7 (line 53). The supplier-9 section says "already supplied top-point witness" without naming the site; the assembly paragraph at 3535-3542 (other reviewer's scope) does.

Sub-declarations:

- `mem_locW_hlat_iff` (918-932): proof is the common-denominator product, identical to Lean 20-30. Confirmed.
- `decoratedPointClasses_bijective_doubleCosets` (1043-1073): injectivity and surjectivity match `classes_bijective:36-83` step for step, including `v = y_c^{-1} γ_f^{-1} z u ∈ U`. Hypotheses `U ≤ UAd`, `k' ∈ UAd`, density for `g ∈ UAd` are stated. Confirmed.
- `exists_K1_point_congruent` (1100-1129): the approximation `|AM - 1| ≤ δ_{c+1}`, then `exists_modify`, then `mem_principal_of_same_decoration`; matches `exists_K1_isPtOf:17-52`. The avoidance hypothesis is the five-fold condition in the Lean statement. Confirmed.
- `mem_framedLevel_iff_two_adelic_points` (1131-1175): hypotheses (`d`, `N`, `val(d_P) ≤ exp(-N_P)`, principal subgroup inside `Θ_P.H` with trivial character, `ρ_P(k) = 1`, `t ∈ K_1`, the old-level equivalence, two point hypotheses) all appear. The argument is coherent. The step "recovery of the completed span ... Nakayama" (1146-1149) is a sketch of `carries_globLat`; I did not read `mem_topU_iff` (40-124).
- `til_tw` (822-916): statement matches (one `Tl` with `Tl.z0 = z0` and the evaluation identity for all `φ`, `c`, `s`, `s'`). Block uniqueness of the extension, the lattice `(N_c, 0) + 𝓞 z_0`, and the cancellation of `red_v(π̄)` are correct. `exists_ka_tw` and the stabiliser comparison are outlines.
- `tuple_integralForms_row_place_by_place` (934-957, 1007-1041): statement matches, including the quantifier "for every class and every local basis" and evaluation in `B^{-1}`. The both-directions argument is right. Dependency label wrong, see 3.3(c). "Zariski dense" (1026-1028) is used where the elementary argument given later at 1620-1623 (add `tI`) suffices; use the same argument in both places.
- `tuplePrimedSpaceClasses_level_and_comparison` (959-991, 1177-1234): the five conclusions match. The construction calls `exists_isPtOf_cm` with `S_T = ∅`, `S_G = v_Gs`, `Q = I.Q(a)`, which the graph confirms. Openness of `U'`, the six reading clauses and the character computation are outlines.

Gaps:

- `TopCh.exists_clsG_top` (cone 7,471), `topU_dense`, `topChi_finite_order_and_trivial`, `forms_tw`, `norm_tw`, `weightedInner_twisted`, `period_conj` are used and cited but are neither registered nor reproduced beyond a few sentences. `period_conj` is taken from the preceding round.
- Unitary invariance of the normalised Fock form (1268-1275) is asserted with a one-sentence reason.

Slips: `ExtMMulVecFix.lean:274-377` for `til_tw` (253-377; correct at 827); `HermitianFormLastCoordinateUniformizerVectorSelf.lean:692-704` (692-701); `LevelFrameCharacterMulMovedPoint.lean:32-94` (declarations span 25-93); `ExistsEmbFIff.lean:28-42` (29-41); `TupleChainComplexFormsEqAlgebraicModularForms.lean:38-83` (`ptC_tw` is 20-83); `IsPtOfMulJ0Decoration.lean:13-48` (13-50); `PolyFn.lean:264-287` (265-287).

## 7. Supplier 8 (`ch_P_r12.tex:1312-1772`)

Statement: exact (no `UnderQ` hypothesis; conclusion `(∃ Lv, StdLv Lv) ∧ Nonempty (TwLvSameS W)`). Assembly (1754-1771) matches `tw_lv_tied_and_same:95-134` and `exists_lvTied_of_std:34-40`: `exists_level_projections`, then `fvTieG`, `upNatTie`, `dnNatTieG_cols`, with `bw_tie` for the basis field; `lvSame_zero` per tuple and `lvSameMu0` at `μ_0` for every stage. Sole caller: `colsTwPTiedS_std:54`.

- `exists_level_projections` (1327-1387). Fully checked against 197-231 and mathematically. The neighbour is `N_- = K^0 + P (K^0)^♯`; `P̄ N_- ⊆ K^0` follows from `(K^0)^♯ ⊆ P̄^{-1} N`; hence `N_{-,P} = D_P`. The value-one test `p(qz) = [qe]` is right because `z - e ∈ D_P` and `q ∈ P`. All ten fields of the record and both `IdL` clauses are accounted for. Confirmed.
- `dn_locP_lat`, `dn_level_functional`, `dn_keeps_chart` (1389-1427, 1551-1587). Statements match. The key point, that `γ` is the rational part of the chosen move and the same `γ` serves both identities, is in the Lean statements and in the text. `dn_keeps_chart` reduces to `cosetIn_rep_cl_dn_eq`, as stated. The `SameG` invariance argument is coherent; proofs not read.
- `fvTieG` (1641-1683). Checked mathematically: `Λ = 𝓞^{n-1} ⊕ π̄^{-1}𝓞`, `ψ(t) = ρ_P(π̄ t_n)`, `ker ρ_P = π𝓞_v` because `π` is a uniformiser at `P` and a unit at `P̄`, the decomposition `t = π (w/π̄) e_n + t_0`, and bijectivity of `g` from prime order. Correct. The equality `|M| = q` is taken from the chart without naming the field.
- `bw_tie` (1589-1639). Statement matches (`IdY → BwTieG`). The argument is right; the "add `tI`" density argument is elementary and complete. Dependency label wrong, see 3.3(c).
- `upNatTie`, `dnNatTieG_cols` (1429-1549) and `lvSame_zero` (1685-1752). These are the longest outlines in my scope (cones 30,447, 20,761, 14,686). The displayed factorizations `γ y_{c'} = y_c δ κ` and `γ y_{c'} = y_c η κ` with the explicit `η`, `κ` are internally consistent (I multiplied them out). I did not compare with the Lean statements `UpNatTieG`/`DnNatTieG`/`LvSame` or read the proofs. The up splice calls `exists_isPtOf_cm` through `Splice.exists_splice` (`ValuedInvMulLe.lean:146-272`; the text cites 146-155), confirmed in the graph.

Gaps:

- For `upNatTie`, `dnNatTieG_cols`, `lvSame_zero` the text is a guided summary of the Lean proof rather than an independent hand proof. A second reader with time for these three should be assigned before supplier 8 is accepted.
- "Stage-zero freeness law" (1729), "preferred representative" (1576-1582), "simultaneous-translation comparison" are named without a source field.

Slips: `TupleChainsLevelStructureCompatibleAtLevelPrime.lean:94-132` (94-134; correct at 1767); `MoveDownLevelPrimeAdelicFactorisation.lean:75-120` (`pointGen` is 78-119); `UpKeepsChart.lean:17-66` (`up'` starts at 16); `MemClosureIff.lean:78-111` for `mem_closure_iff` (78-125); `ExistsForgetsFrames.lean:144-180` (`exists_lift` is 144-172).

## 8. Claims of closure and bookkeeping

- `ch_P_r12.tex:7-8`: both original inputs remain partial. `status.json`: `round12.review_status = pending_review`, `independent_review_received = false`, `accepted_grade_changes = []`, `grade_counts.original_complete = 13`. Z1.2 has `completion_candidate: null`. Consistent.
- `subtheorem_counts` (weyl 2, point 5, supplier 4: 1, supplier 9: 8, supplier 8: 10) agree with the list.
- No statement in lines 1-1772 claims that an original input, or RH, is proved.
- Of about 240 file/line citations in my scope, checked mechanically against the graph, none points to a wrong declaration; roughly 35 are off by one to five lines at an end point (listed per section above).

## 9. Corrections, in order of importance

1. Register `TransDual.nabDelDual` / `T.transported_weylLattice_hermitianDuality` as a Z4.4 subtheorem and give it a full hand proof; it is the only link from the two Weyl results to the root (3.3 d).
2. Fix the dependency statements for the integral tests in suppliers 8 and 9: the Lean path is `mem_localization_delAtr → Formalism.L2.DIV.nabDelLoc → nablaDeltaLocal_holds`, not the registered `T.transportedLattice_...`; say that the hand proof of `NabDelLoc` covers both (3.3 c).
3. Trust ledger: describe `locPrints_of_litN` as a projection from the hypothesis `LiteratureRankNHypothesis.coh` and name where `HypothesesH'` is supplied (2.2).
4. Supplier 8: obtain a statement-and-proof check of `upNatTie`, `dnNatTieG_cols`, `lvSame_zero`, or mark them "proved in Lean, outlined" (7).
5. Record the three `GlobalTheory.Published.*` lemmas in the cones of seven candidates as proved elementary lemmas (4.1).
6. `unimodGenus`: label the completion-plus-Cayley argument as an alternative to the Lean semilocal route (4.1).
7. `r12:weyl`: cite the two stability theorems and `basisAtEx`; cite the three standard facts (3.3 a, b).
8. Supplier 4: name `D.T_ne_two`; label the transport/up/down paragraphs as outlines or expand them; make the stabiliser argument self-contained (5).
9. Supplier 9: add `l0` and `1 ≤ m` to the statement paragraph; name `colsTwPTiedS_std:53-55` as the discharge site of the top-point and level hypotheses; register or label `exists_clsG_top`, `forms_tw`, `period_conj` (6).
10. Reconcile the "Local" cone column with the graph (2.2), take up the three leftover R11 items (2.1), and fix the end-point line references.

## 10. Summary

All 26 pending declarations in lines 1-1772 state their Lean counterparts correctly, with the right hypotheses, quantifier order and rings, and their files, ranges and cone sizes reproduce exactly. I found no mathematical error.

The Weyl section is the strongest part: the previously missing direction of `standard_weyl_lattices_fock_dual` is proved completely and correctly (coefficient extraction by Weyl words, interlacing of the leading exponent, integral straightening, double dual), and the transported-lattice localization is proved as in Lean. Both are confirmed. The point section is confirmed for the three constructions I read in full and confirmed with gaps for the genus step, where the hand proof is a valid alternative to the Lean route.

Suppliers 4, 9 and 8 are confirmed with gaps. Their statements and assemblies are exact and every calculation I re-derived is right, but a substantial share of each (transport and move laws in supplier 4; chart gluing and metric identities in supplier 9; the up/down splices and the stage-zero comparison in supplier 8) is an outline of the Lean proof. For `upNatTie`, `dnNatTieG_cols` and `lvSame_zero` my check did not go beyond coherence of the outline.

Two structural findings matter for the Z4.4 completion claim: `nabDelDual`, the sole consumer of the Weyl results in the root cone, is unregistered and only sketched; and the integral tests of suppliers 8 and 9 reach `NabDelLoc` through `Formalism.L2.DIV.nabDelLoc`, not through the registered theorem (same proposition, so no mathematical gap). In the Z1.2 ledger, the first premise of the root is forwarded from a literature hypothesis, not discharged. No original input is claimed closed, and nothing in this scope bears on the truth of RH.
