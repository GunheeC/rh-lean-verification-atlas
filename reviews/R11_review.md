AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

# R11_review

AI review report produced during this project; file names are internal working names.

- Internal source file: `out/R11_review.md`
- SHA-256: `c2566a64ed8165e09bd775e866534a1ff0c6d0c1823e8de78186161e39aeb3ac`
- Report scope: Round-11 independent review: `rankTwo` (Z1.2 queue) and Z4.4 suppliers 2, 3, 5, 6

## Internal report

The report below preserves its original verdict, scope and unresolved points. Historical review-machine home prefixes are displayed as `${REVIEW_HOME}`; the source checksum above identifies the original report. Source line numbers in other records count from its original title.

# Round-11 independent review: `rankTwo` (Z1.2 queue) and Z4.4 suppliers 2, 3, 5, 6

Reviewed text: `${REVIEW_HOME}/work/prev11/ch_P_r11.tex` (1,172 lines) and the `round11` block of `status.json`.
Lean source: cleaned copy `${REVIEW_HOME}/src/rh/src`; line numbers below are the original (commit `40e56bab`) numbering used by the blueprint and by `graphq.py`. The cleaned copy is shifted by +4 to +7 lines in the files I read.
Graph: `graphq.py` plus a reachability pass over the same `graph_cache.bin`.

Nothing in this review, in the chapter, or in the Lean development is treated here as establishing RH or GRH. The review only compares hand proofs with the Lean statements they label.

## 1. Verdict table

| # | Candidate | Lean declaration | Verdict |
|---|---|---|---|
| 1 | Z1.2 queue: `rankTwo` | `UpperTheory.V.Z.J.rankTwo`, `.../LinkedUnramifiedChains/CrystallineCardinalities/RankTwo.lean:177-229` | **CONFIRMED WITH GAPS** (proof complete and faithful; gaps are statement edge cases and labelling, see 2.1) |
| 2 | Z4.4 supplier 2 | `GlobalTheory.T.hermitianColumnChoices_of_formsLevelsClasses`, `HermitianColumnChoicesOfFormsLevelsClassesStatement.lean:8-9` (= `TC.hermColsCh_of_forms`, `HermitianColumnChoicesOfFormsLevelsClasses.lean:68-82`) | **CONFIRMED WITH GAPS** (statement exact; decisive calculations correct; several sub-lemmas are one-line sketches) |
| 3 | Z4.4 supplier 3 | `GlobalTheory.T.stepZeroHermitianLevel_uniformiser_kills_values_alt`, `StepZeroHermitianLevelUniformiserKillsValuesStatement.lean:9-10` | **CONFIRMED WITH GAPS** (statement exact; main argument complete; local-basis and adelic-to-local inputs sketched and uncited) |
| 4 | Z4.4 supplier 5 | `GlobalTheory.T.hermitianColumns_generators_baseLattices_functionals`, `HermitianColumnsGeneratorsBaseLatticesFunctionalStatement.lean:8-9` (= `TC.herm_rest_tied`, `HermitianColumnsGeneratorsBaseLatticesFunctional.lean:16-33`) | **CONFIRMED** (minor remarks only) |
| 5 | Z4.4 supplier 6 | `GlobalTheory.Mem.Col2.TC.spaces_in_coordinates`, `TrueColumnSpacesStandardInFrameCoords.lean:90-101` | **CONFIRMED** (minor remarks only) |

No candidate is NOT CONFIRMED. All five are conditional implications; none closes an original input, and the chapter and `status.json` say so correctly (section 4).

Two findings outside the per-candidate verdicts matter more than any gap inside them:

- **`rankTwo` is not in the cone of the Z1.2 root.** It lies in the cone of the Z1.1 root `UpperTheory.V.Z.Win.Dn.ends0_alt`, as do `tan`, `selLow`, `locHigh`, `cupUnr`, `b1absO`, `dualNO` and `core_alt_bis`. Confirming it removes nothing from the 38,519-line Z1.2 root cone (section 3.1).
- **The Z1.2 "remaining open" list is accurate in what it names but incomplete** for the two hypotheses of the root, and the Z4.4 list omits the Weyl-duality boundary that the chapter itself describes (sections 3.1, 3.2).

## 2. Per-candidate review

### 2.1 `UpperTheory.V.Z.J.rankTwo`

Text: `ch_P_r11.tex:373-395`. Lean: `RankTwo.lean:177-229`, helpers `tors_card` 9-39, `hom_alt` 41-96, `rel`/`rel_le` 98-116, `rel_fin` 118-166, `finite_linearMap_of_finite_module_finite` 170-175; `okFin`, `OkFin.lean:5-80`.

**Statement comparison.**

| Item | Lean | Blueprint | Match |
|---|---|---|---|
| Ring `O` | domain, DVR, `[IsCoef l O]`, `[Algebra ℤ_[l] O]`, `(l : O) ≠ 0` | "coefficient DVR with (ℓ:O) ≠ 0" | yes, but see gap (b) |
| `R` | commutative Noetherian `O`-algebra | same | yes |
| `ξ`, `T` | `ξ : R →ₐ[O] O`, `T : Set R` arbitrary | same | yes |
| Target | `Ok l O k = O ⧸ (l^k)` (`UnitStep.lean:48`) | `A_k = O/(ℓ^k)` | yes |
| Count | `∀ k > 0, ∀ X, X = {δ ...} → X.Finite → card(A_k)^2 ≤ C * X.ncard`, `C : ℕ` | "at least `|A_k|^2/C` for all k>0, with C>0 fixed" | see gaps (a), (c) |
| Quantifier order | `C` before `k` | `C` fixed, then all `k` | yes |
| Conclusion | two `O`-linear ξ-derivations `R → O` killing `T`, `LinearIndependent O ![δ, δ']` | same | yes |

**Proof check.** Every step of the hand proof matches a Lean step and is correct.

1. `M = R/⟨T, ab − ξ(a)b − ξ(b)a⟩_O`; derivations to any `O`-module are exactly linear maps from `M` (`rel_le`, 101-116; used at 187-189 and 208-215).
2. `1 ≡ 0` from `a=b=1` (`rel_fin`, 145-150); products of two elements of `ker ξ` vanish (124-127); hence the finitely many ideal generators of `ker ξ` span `M` over `O` (128-166). The hand argument "replace each coefficient r by ξ(r)" is exactly lines 134-143. Noetherianity is used only here.
3. Structure theorem over the PID, free rank `s` plus `O/(a_i)` (`hom_alt`, 47, via `Module.equiv_free_prod_directSum`).
4. Kernel and cokernel of multiplication by `a_i` on `A_k` have equal order, and the cokernel is a quotient of `O/(a_i)` (`tors_card`, 9-39). Correct.
5. If `s ≤ 1`: at most `C'·|A_k|` maps (56-96). With the hypothesis, `|A_k| ≤ C·C'`; Lean takes `k = C·C'+1` and `2^k ≤ |A_k|` (`okFin`, 201-229). The hand "since |A_k| tends to infinity" is the same step.
6. If `s ≥ 2`: two coordinate projections; independence by evaluating at the two basis vectors (49-55, 191-199).

The remark "takes no inverse limit of choices" is accurate.

**Gaps.**

(a) *`C = 0`.* Lean allows `C = 0`; the blueprint assumes `C > 0`. The Lean statement is still covered (the hypothesis is then contradictory at `k = 1` because the set is finite and `|A_1| > 0`), but the text should say so or state `C ≥ 0`.

(b) *What "coefficient DVR" supplies.* The proof needs two facts that the text uses silently: `O/(c)` is finite for `c ≠ 0` (finite residue field, `IsCoef.fin`), and `ℓ` is a non-unit (residue characteristic ℓ, `IsCoef.char`), which with `ℓ ≠ 0` gives `|A_k| → ∞`. Both are in `okFin` (`OkFin.lean:5-80`), which the text does not cite.

(c) *Finiteness of the derivation set.* The Lean hypothesis is conditional on `X.Finite` and uses `ncard`. The hand version states an unconditional count. They agree only because the set is always finite (`M` finitely generated, `A_k` finite; Lean line 205). One sentence is missing.

(d) *Discharge site not labelled.* The single caller is `UpperTheory.V.Z.J.tan`, `BoxUnit.lean:128-160`. There `R = S.R`, `T` is the set of inertia values of the diagonal characters, the lower bound comes from `selLow` (`SelLow.lean:60-98`) and the injection of `ZN B k` into the derivation set comes from `derOf` (`LiftOfBar.lean:214-281`) and the private `zn_ext`. The paragraph names none of `tan`, `derOf`, `zn_ext`, and does not say where Noetherianity of `S.R` is supplied.

(e) *Uncited standard fact.* Structure theorem for finitely generated modules over a PID.

(f) *Unit attribution.* See section 3.1: the declaration is registered under Z1.2 but lies outside the Z1.2 root cone. Its cone is 304 core lines (RankTwo 213, OkFin 76, three definitions), with no literature leaves.

### 2.2 Supplier 6: `TC.spaces_in_coordinates`

Text: `ch_P_r11.tex:481-503`. Lean: `TrueColumnSpacesStandardInFrameCoords.lean:90-101`; helpers `Crd.Ortho`, `ortho_pos`, `Ortho.gram`, `Ortho.mem_standardLattice_iff_integral_coords`, `map_symm_map`, `incl_co` at 14-80.

**Statement comparison.** Hypotheses `I.Ok`, `TC.Pins B X`, `l`, `Z`: match. Conclusions in Lean order: `StdTied D`; `gramP D = 1`; `iXc` extends by a zero last coordinate; for every `i ≤ m`: `gramN = 1`, lattice coordinates integral iff in `O_E`, and for all `u, a`: (for all `c`, `latCrd (latAt u a i c)` is the decorated representative lattice) and there is `eY` with `IdY` and `de_i(z,τ) = det((eY z)_τ)`. The blueprint lists all of these.

**Proof check.** `Ok.spaces` gives the standard positive models (93-95); orthonormality from `stdSpace_gram_apply` (`ortho_pos`, 22-23); integrality criterion by expansion in the frame (36-50); `Pins.iX` sends frame vector `a` to frame vector `a`, giving the zero-extension formula (`incl_co`, 53-80); `latAt` is a pullback whose forward image recovers the lattice (`map_symm_map`, 47-51, used at 98-100); `eY := Equiv.refl` with both properties by `rfl` (101). All as described.

**Remarks.**

- `StdTied` is the first conjunct of the Lean conclusion but appears only inside the proof ("provides the witnesses to `StdTied`"). It should be in the statement sentence, because it is the only component used at the assembly call (`ExistsStandardColumnComparisonsTrueColumns.lean:20-72` takes `.1`).
- "There is a frame equivalence `e_Y`" follows "for each `u,a,i,c`". In Lean `eY` depends on `u,a,i` but not on `c`.
- "The two frame types now coincide definitionally" is certified in Lean by `rfl`; the text does not exhibit the unfolding of `(I.chain l u a).Y i` and `Forms.Fr`. Acceptable, but it is an appeal to the Lean definitions, not a hand argument.
- The hypothesis that conjugation preserves integrality (`hs` from `Ok.spaces`) is used in `ortho_pos` and not mentioned.
- The 14,238-line cone is almost entirely the definitional infrastructure of `rec7`; the theorem's own proof term is covered in full.

### 2.3 Supplier 3: `stepZeroHermitianLevel_uniformiser_kills_values_alt`

Text: `ch_P_r11.tex:505-564`. Lean: statement file 9-10; proof in `StepZeroHermitianLevelUniformiserKillsValues.lean`: `fun_transport` 29-54, `smul_eq_zero_of_prime_card` 60-65, `pi_kills` 69-114, `stepZeroHermitianLevel_with_formsFunctional` 123-162; `MovePair.ld_loc`, `ClassPairMovedOfMultipliesLocalFunctional.lean:96-105`; `UnitaryCompletionMapsDualLattices.lean:52-188`.

**Statement comparison.** Hypotheses: `Ok`, `Pins`, `l`, `Z`, word `u`, `F : FormsTiedSym` with `StdF`, level `L` with `SameCar` against the step-zero forms level. Conclusion: one `L'` with seven equalities (`Lb`, `Uloc`, `U`, `y`, `stabI`, `splitG`, `frG`) and, for every `w | T` and `a ∈ intV E w` whose image is the image of `F.atT.piU`, `a • m = 0` on `L'.fM w`. The blueprint has the same hypotheses, the same seven retained items, and the correct order (`L'` chosen before `w, a`). Match.

`Ok`, `Pins` and `StdF` are unused in the Lean proof (line 170 binds them to `_`). The blueprint lists them as hypotheses, which is faithful; it could note they are not needed.

**Proof check.**

1. Choice of `v` with `eV v = w` (158-160): matches "choose v corresponding to w".
2. `pi_kills` (69-114): class `c`; `fv_ne` gives an input with nonzero value; `pr_surj` lifts it to `z`; `ld_loc` puts `y_c^{-1} z_w` in the local base dual; the tie `FvTie` gives `f_T(t) ≠ 0`; `pr_smul` and `res_pi` give `f_T(y_c^{-1}(πz)_w) = 0`; that vector is `a·t`; prime order finishes. The hand proof follows this line by line and is correct. The phrase "a class c above the identity double coset" is harmless: Lean discards that property (`obtain ⟨c, -⟩`, line 75).
3. Transport to the rank indexing of `L` (`fun_transport`, 29-54) and replacement of `fM`, `fT` and their five certificates only (146-156): matches "replace only the value module, functional and their certificates". The four transported properties (nonvanishing, vanishing on the base lattice, scalar annihilation, stabilizer identity) are `k1`-`k4`.
4. Local dual calculation (`isLocBasis_dual` 75-113, `mem_latS_dualL` 115-159, `dual_move` 161-188): the identity `h(v, y^{-1}z) = h(yv, z)` and the description of the dual by the columns of `(B^*J)^{-1}` are correct and match.

**Gaps.**

(a) `LocB.exists_isLocBasis` (`PBwLocGen.lean:248-289`) is sketched as "semilocal Dedekind ring is a PID, so a full lattice has a local basis matrix". The second half needs "finitely generated torsion-free over a PID is free, of rank n because the lattice is full". Standard, uncited.

(b) `latS_of_locBasis` (`LatSOfLocBasis.lean:117-127`) is described in one clause ("after extending to S the columns still generate"). No argument is given that the `S`-span of the lattice equals the `S`-span of the local basis columns.

(c) `ld_loc` needs four inputs that the text does not name: the Gram determinant is a unit (`bwB_gramN_det`), the class lattice is full (`clsLat_lat`, `bwB_clsCrd_lat`), the dual is finitely generated (`LocB.dual_le_bnd`, `fg_of_le_bnd`, in `ld_lattice` 86-94), and the adelic lattice criterion for `y_c` localizes to `w` (`rlv_yloc`, `afsplit_bc_mem`). The text starts from "a unitary local map y carrying the base lattice to the representative lattice", which is the output of that localization.

(d) Discharge of `SameCar`: at `colsTiedSym_std` (`ExistsStandardColumnComparisonsTrueColumns.lean:20-72`) from `CarH.car0` of supplier 2. The Assembly paragraph (`ch_P_r11.tex:1050-1062`) says this correctly.

### 2.4 Supplier 5: `hermitianColumns_generators_baseLattices_functionals`

Text: `ch_P_r11.tex:566-666`. Lean: `herm_rest_tied`, 16-33, which dispatches to five theorems.

**Statement comparison.** Hypotheses: `H`, `F_u`, `A_u`, `StdF ∧ StdLvC` for every word, `CarH H F`, `CarT H F A`, and for every `u`, `w | T`, `a` with image `(A u).piU`: `a` kills `(H.lev0 u).fM w`. Conclusions: `SymmetricCofactorCompatibility`, `SymmetricBaseCompatibility`, `Nonempty SymmetricResidueFieldLevels`, and `∃ X0, ∀ u, (X0 u).piG = X.piG` (`SymAll.lean:17, 43, 62, 71`). The blueprint states exactly these four. Match.

**Proof check.**

| Part | Lean | Hand proof | Result |
|---|---|---|---|
| Cofactor | `CarT.piU`, `StdF.piU`, `Pins.cof` (lines 19-23) | "π = X.piT(u) by the two standard comparisons; pinned identity" | correct |
| Base, step zero | `base_sup_dual_eq` 12-113, `base_step_zero_tied` 121-168 | `L = O^{n-1} ⊕ πO`, `L^∨ = O^{n-1} ⊕ π̄^{-1}O`, `L + π̄L^∨ = O^n`; rank zero immediate | correct |
| Base, charts | `ChartBase.sup_dual_eq` 22-106, `chart_base_sup_dual` 158-211 | same computation with `StdF.mid`/`carC`, `StdF.ends`/`carM` | correct (statement-level check) |
| Residue levels, `1 ≤ i < m` | `FvChart.fvTie_of_car` 90-124 (`reGL_solve`, `crdN_mem_LdG`, `exists_reindex_hom`) | reindex, apply `f_T`, compose with `fMeC`; `prC` and `fvC` | correct |
| Residue levels, `i = m` | `fvTie_top` 91-115 | unique chart, `CarT.pr`, `fv` | correct |
| Level-zero data | `colLevel_functional` 118-182, `stepZeroLevel_functional_residueField` 187-251, `intV_coe_eq_inclE_of_T_mem` 255-302, `exists_equiv_of_cyclic` 52-80, `localDual_eq_add_span` 9-144, `acts_by_same_integer` 180-253 | `M = L_w + S·e`, `e = e_n/π̄`; both targets killed by π; common integer action; equal kernels; quotient isomorphism; `piG := X.piG` | correct |

I checked the "common scalar action" paragraph in detail, because it is the one non-routine step. For `d = π + π̄` and `c = bπ̄ + b̄π` one has `db − c = π(b − b̄)`, which acts as zero on both modules; `d ∉ w` because the residue map kills `π` but not `π̄` (`res_conj`, lines 233-242); so `b` acts by the same integer mod `T` on both. For scalars from the completed base integers, `k_1 − k_2` lies in the maximal ideal and is an integer, hence divisible by `T` (`same_int_of_local`, 71-100; `int_dvd_of_mem`). The two subrings generate `intV E w` by definition (`DataLevel.lean`, `intV := tensInt ...`). The argument is complete, and the text's remark that equal orders alone do not identify the actions is the right point.

**Remarks.**

- The text derives `π ≠ 0` from the norm equation; `base_sup_dual_eq` derives it from the lattice spanning (67-80), while `stepZeroLevel_functional_residueField` does use the norm equation (228-232). Both are valid; the norm equation `piU_norm` is available in both places.
- "Both targets are killed by π ... the second by the nonzero-value argument of supplier 3" is right, but the Lean proof re-runs that argument through `unitary_maps_latS_dual` (line 162), not through `ld_loc`. The same remarks as 2.3(c) apply to that input.
- Discharge sites, all at `colsTiedSym_std:20-72`: `CarH` from supplier 2 after substituting supplier 3's `L'` (the seven equalities); `CarT` and `A` from supplier 4 (open); the annihilation hypothesis from supplier 3 after rewriting `CarT.piU`. The Assembly paragraph states each of these correctly.
- Supplier 5 calls supplier 6 through `trueColumn_spaces_standard_in_frameCoords` (`...Statement.lean:7-8`). The text says "in the frame of supplier 6", which is adequate.

### 2.5 Supplier 2: `hermitianColumnChoices_of_formsLevelsClasses`

Text: `ch_P_r11.tex:668-785`. Lean: `hermColsCh_of_forms` 68-82, `level_classes_of` 42-65 (with `chart_level_classes`, `top_level_classes` 13-40), and four imported theorems.

**Statement comparison.** Hypotheses: `Ok`, `Pins`, `l`, `Z`, `Ch`, `chOf`, `F`, finiteness of every `Ch u i`, `Nonempty (Unique (Ch u m))`, `StdF` for every `u`. Conclusion: `∃ lev0 lev cls vT Fv, CarH {...} F`, seven fields (`StdLvPr.lean:19-42`: `eV`, `fv`, `car0`, `carC`, `carM`, `sp`, `fr0`). The blueprint has the same data and says "all seven fields". Match. `vT := (F u).atT.eV` (line 74) is stated.

**Proof check.**

1. *Residue fields* (`ResidueFieldEquivRealSubfieldQuotientTrueColumns.lean:19-57`). `r_v(y) = r_v(yq + ȳp)/r_v(p + q)` with both elements fixed and integral. Correct.
2. *Chart level* (`level_of_chart` 136-169, `exists_herm_level` 35-69, `baseL_eq` 98-130). Gram = 1 from supplier 6 (line 138); base lattice `O^{n-1} ⊕ pO`; the three obligations are away-from-bad hyperspecial, `mem_Uloc_of_cong` at generator primes, and `uloc_T_iff` at `T`. Matches. The rank is positive (`m_add_three_le_k`, line 139), so `L = A^{n-1} ⊕ pA` makes sense; the text does not say why `n ≥ 1`.
3. *Splitting at `T`* (`LevelPrimeUnramifiedUniformizer.lean:35-110`, `LevelPrimeDvdOfAdicValuationLtOne.lean:21-86`). The count "2f distinct primes of norm T, `N((T)) = T^{2f}`, so exponent one each" is correct and is what `notMem_sq`/`unram` do, using `card_vT` and `finrank_E`.
4. *Discriminant-group calculation* (`uloc_T_iff` 78-94, `uloc_acts_trivially_on_dual_quotient` 50-186, `eq_one_add_of_fixes` 13-68, `uloc_of_triv_disc` 10-70). I checked every line of the hand computation: `L^# = A^{n-1} ⊕ q^{-1}A`; `x_{jn} ∈ qA` for `j < n`; `(d−1)m = 0`; `d̄d ≡ 1 (mod T)` from the last diagonal entry because `conj(x_{jn}) x_{jn} ∈ pqA`; the scalar action on a group of prime order factors through one residue projection; hence `d_1 ≡ 1`, then `d_2 ≡ 1` from the product; `(d−1)/q ∈ pA`; `(x−1)L^# ⊂ L`. All correct, and the converse direction is correct. This is `InLocalDiscriminantKernel` (`InLocalDiscriminantKernel.lean:62-66`).
5. *Class identifications* (`HermitianClassConditionOfChartClasses.lean:29-81`): transport by rank equality; fibre over a chart label for `i < m`, bijection onto all classes at `i = m` by uniqueness. Matches lines 13-65.
6. *Step zero* (`ColumnLevelOfStepZeroFormsLevelTrueColumns.lean`: `exists_reindex` 32-67, `mem_Uloc_iff_iwU` 108-139, `stab_class_lattice` 143-178, `exists_colLevel` 201-256). Every `ColLevel` field is the reindexed endpoint field except `Uloc_g` (Iwahori criterion), `w1` (lying over) and `stabI_lat` (lattice stability). The text names exactly these three.

**Gaps.**

(a) `mem_Uloc_of_cong` (`ValNatCastLtOne.lean:41-83`) gets four sentences. The hypothesis it consumes, `GLevH K.lev F.gl Hs lam` (supplied by `F.glevC` / `F.glevM`, lines 21 and 36 of the supplier file), is not named, and "the resulting matrix reduces to the identity, which belongs to the given residue subgroup" is the whole argument.

(b) The Iwahori criterion rests on `G.splitStabL_of`, `G.split_integral_completion` and `G.self_dual_lattice_at` (cited inside `mem_Uloc_iff_iwU`, 110-115). The text compresses these to "the two local factors are dual, and a unitary element acts by inverse transpose on the second". "T is a unit there" needs `T ≠ g_i` (`D.T_ne_g`, used at line 229); not stated.

(c) Local-global lattice principle (`latLocGlob_main`, `mem_levelAfL_iff`): "a full finite lattice is the intersection of its localizations (test the annihilator...)". Standard, uncited, sketched in a parenthesis.

(d) The Lean route to the splitting of `intV E v` at `T` is different from the hand route. Lean's `eq_one_add_of_fixes` uses the standing hypothesis `cmUnram` of `CMData` through `exists_splitting_of_character` (line 23) together with the uniformizer statement `hunif`. The hand proof derives splitting from the prime count alone. The hand route is valid and self-contained, but the text cites `eq_one_add_of_fixes` as its source without noting that the Lean proof uses `cmUnram`. The step "its integral algebra is `R × R`" (the subring generated by `O_E` and `O_v` is the maximal order) is asserted with a one-clause CRT justification.

(e) `StepLevel` fields `Lb_fin`, `Lb_span`, `Lb_dual`, `Lb_index` (`InLocalDiscriminantKernel.lean:75-93`) are covered only by "use these same lattices"; only `Lb_int` gets an explicit sentence. They are transported verbatim in Lean (`exists_herm_level`), so this is a wording gap.

(f) Discharge sites. The chart sets, `chOf`, the forms and `StdF` come from supplier 1 (open) at `colsTiedSym_std:20-72`. The text's "this proves supplier 2 from its stated premises" is the right scope.

None of (a)-(f) is an error. The verdict is "with gaps" because several non-trivial local statements (items a, b, c) are represented by one-sentence sketches. I did not measure what fraction of the supplier's theorem lines they cover.

**Cross-check.** The four supplier cones contain no literature leaves and no axioms beyond the three standard ones. The cone sizes and theorem-only counts in the numbered list (`ch_P_r11.tex:453-472`) reproduce exactly: 19,178 (10,327); 16,725 (7,960); 17,252 (8,398); 14,238 (6,767). All line ranges cited in the four paragraphs agree with the graph's original numbering; I found no wrong reference among about fifty checked.

## 3. Audit of the "remaining open" lists

### 3.1 Z1.2, root `UpperTheory.V.Th.adjointLiftingTheorem_of_locPrints_of_core` (`AdLOf.lean:104-150`)

**What the root cone contains.** I recomputed 38,521 core lines (blueprint: 38,519). The seven comparison roots are all inside it, with cones 18,598 / 20,759 / 11,421 / 16,908 / 16,175 / 13,208 / 16,296 and union 26,407 (blueprint: 16,171 for `crWt0`, union 26,405; differences of at most 4 lines, immaterial). Of the other 12,114 lines, 7,531 are the recorded exclusive read ranges and 4,583 are shared lines.

**Accuracy of what is named.**

- Seven local comparisons (`crExt`, `prF`, `bkDim`, `charFil`, `crWt0`, `isCrys_isDR_sub_quot`, `isCrys_isDR_internalHom`): correct, in the root cone, correctly labelled "proved in Lean, not reproduced" (`ch_P_r11.tex:242-256`).
- Uniform dual bound `dualNO` (`DualNO.lean:50-144`, cone 2,410): correct, labelled "statement only".
- Flag exclusion `UnlPt` / `linkedUnlE_alt` (cone 1,111,251; blueprint 1,111,243): correct, labelled as remaining.

**What is missing or understated.**

1. *None of the non-comparison items is in the Z1.2 root cone.* `rankTwo`, `tan`, `selLow`, `locHigh`, `cupUnr`, `b1absO`, `dualNO`, `core_alt_bis` and `ordinary_vanishing_two_of_printed_hida` are all outside it, and all are inside the cone of the Z1.1 root `ends0_alt`. The chapter says "this cone and the ordinary tangent input are at callers outside the declared root's 38,519-line cone" (`ch_P_r11.tex:427-428`), which is true, but the queue paragraph and `status.json` file `rankTwo` under unit Z1.2 without that qualification. A reader of `status.json` alone would take the candidate as progress on the Z1.2 root. It is progress on an "additional assignment" (the unit statement's own phrase), and in the 20-input partition it belongs to Z1.1.

2. *Discharge of `LocalPublishedTheorems` is not labelled.* The root's caller is `UpperTheory.V.Th.adjoint_lifting_of_cohomology` (`ThFinal.lean:18`), which supplies `LocalPublishedTheorems` from `UpperTheory.V.HV.U.locPrints_of_litN` (`HVFinalU.lean:12-13`, cone 5,243) and `DenseThresholdMainCase` from `core_alt_bis` (`ThFinal.lean:17`). The chapter names the second and not the first. The root cone also contains literature leaves (`GlobalTheory.Published.FontaineBcris` and its fields, `fontaineBcrisBasicTheorems_proof`, `SmGL.IrrRep`), on which the seven comparisons rest; they should appear in the remaining list as published inputs.

3. *"Uniform dual Selmer bound" understates the vanishing input by two orders of magnitude.* `core_alt_bis` has cone 375,725; almost all of it is `ordinary_vanishing_two_of_printed_hida` (`TOrdVan.lean:159-192`, 374,411). Its direct suppliers are `hida_x_of_printed_hida` (`THidaX.lean:17-23`, 341,282), `core_o_of_literal_automorphy_n` (`TCoreO.lean:129-159`, 132,810, of which `has_operator_statement` `THasOp.lean:18-45` is 94,762 and `count` is 5,982), `Nm.regular_arithmetic_hida_of_literal_automorphy` (37,088), `W.locCFT` (19,625), `b0Ex`, `lamEx`, `phiAll`, `nmAbs`. `dualNO` is 2,410 lines of this. The chapter does say that `core_alt_bis` "still requires the ordinary vanishing assertion" and gives the cone size, so the text is not wrong; but the summary lists ("uniform dual Selmer bound"; in `status.json` "uniform dual trace bound and same-level Hecke lower bound") name one small leaf and one vague item. The remaining list should name `ordinary_vanishing_two_of_printed_hida` with its four large suppliers.

4. *Inside `b1absO` the other constants are taken without a label.* `ch_P_r11.tex:281-300` takes `c_1`, `c_0`, `C_v`, `A_j` "before choosing m". These are Lean theorems `h0GO` (`RedSurj.lean:24-82`), `h0v0O` (`RedSmul.lean:19-81`), `h0qO` (`ExistsCyc.lean:40-86`), `locVO` (`PsiCont.lean:132-183`), with `phEqO` and `adExP` also used. Only `dualNO` and `oneLevelO` are cited. The "given global duality formula" in `oneLevelO` is a hypothesis carried in `Sys.counts`; its discharge (`presCnts`, `arPl`, `arPres`, `unrLoc` under `b1O`, `OrdinaryHeckeAlgebraIntegral.lean:31-53`, cone 12,194) is not named.

5. *Flag.* The stated remainder (annihilator, simple-root selection, local-to-global lower count) is fair. For completeness: `rankTwo` is consumed through `tan → tanA_of → tanA` (`TanAOf.lean:30-37`, `TanA.lean:7-8`, cone 35,705), whose other suppliers `unitOf` (29,874), `linkOf`, `gwlOf`, `leOf2` are not mentioned; and `tanA` is called from both `linkedUnlE_alt` (`LinkedUnlE.lean:43-48`) and `linkedUnlE_holds_alt` (`LinkedUnlEHolds.lean:24-29`, cone 871,819, the caller inside the Z1.1 root). The chapter cites only the first.

6. *Shared root-cone lines used as standard facts without citation.* "Irreducibility gives full matrix span" is `DAmitsur.lean` (208 lines in the cone) and `IrrIffSpan.lean`; "the cyclotomic character has an element of infinite order on this inertia" is `CycInertia.lean` (162 lines); `LocStab.lean` (253) and `GlobalB.lean` (182) are not cited at all. These are small, but they are in the cone and are neither reproduced nor labelled.

**Conclusion for Z1.2.** The three named items are accurate. The list is not complete: it should add the discharge site and literature record for `LocalPublishedTheorems`, replace "uniform dual Selmer bound" by the vanishing theorem with its main suppliers, label the remaining `b1absO` constants, and state that everything except the seven comparisons lies in the Z1.1 cone.

### 3.2 Z4.4, root `GlobalTheory.PerTwClose.twistedPeriodAdmissible_of_rowInt` (`AdmissiblePeriodTwistOfIntegralRows.lean:14-21`)

**Cone.** 88,646 core lines, reproduced exactly. The nine suppliers are all in the cone; their union is 84,181 lines, reproduced exactly. Direct theorem dependencies of the root: `exists_standardColumnComparisons_trueColumns` (61,582), `trueColumnChoice_exists_standardChainData` (73,211), `perDecTwT_of_std` (22,066), `admissiblePeriodTwists_reduction_placeTuples` (4,449), `twistedPeriodDecomposition_of_classwiseTwistedPairingIntegral` (10,484).

**Suppliers 1, 4, 7, 8, 9.** The descriptions of what stays open are accurate, and the cone sizes quoted for the open sub-suppliers reproduce: `exists_charts` 27,859; downward move 18,740; `chart_lastStep_twistBasePoint` 27,250; `charts_tuple_trivQ` 40,240; `exists_penultimateLevel_couplingCosets` 32,279; `upNatTie` 30,447; `dnNatTieG_cols` 20,761; `tuplePrimedSpaceClasses_level_and_comparison` 24,746; `tuple_integralForms_row_place_by_place` 19,117; `til_tw` 17,886. One wrong range: `til_tw` is `ExtMMulVecFix.lean:253-377`, not 253-274.

Supplier 4's eight sub-suppliers in `hermitian_data_at_level_prime` (`HermitianDataAtLevelPrime.lean:18-62`) are seen-prime, discriminant quotient, middle projection, stabilizer map, hyperplane classes, diamond, down, up; the text's list ("seen-prime condition, discriminant quotient, middle projections, three adelic moves and the comparison of hyperplane classes and lattices") matches, with the stabilizer map hand-proved.

Supplier 1 is described in prose only. `formsTiedSym_std` has at least fifteen sub-suppliers above 13,000 lines besides `exists_charts`: `exists_gLoc_idG_chiTied`, `charts_funKilled`, `val_tied`, `ipV_norm_tie`, `dilTied`, `upNatTie`, `dnNatTieG_cols`, `bw_tie`, `chart_gLevH`, `readsK_one`, `til_ties`, `levels_top_row_sym`, `glev_zero`, `clsP_tie`, `stepBefore_oneLevel`, `fvTieG`, `exists_level_projections`. The prose covers them by category; an itemized list would make the open set checkable.

**Missing from the queue paragraph and from `status.json`.**

1. *Weyl-lattice duality.* 4,465 lines of the root cone lie outside the nine suppliers, most of them in the duality files. `standard_weyl_lattices_fock_dual` (`StandardWeylLatticesFockDualStatement.lean:14-15`, cone 5,730) is used by `TransDual.nabDelDual` (`TransportedWeylLatticeHermitianDuality.lean:278-309`) in both directions of the iff. Section `r11:fock` proves one direction by hand and states its boundary honestly (integral straightening `lowerTriIntegral`, tableau existence for an interlaced leading exponent, `transportedLattice_localization_free_le_coefficientSpace`). The queue paragraph (`ch_P_r11.tex:1164-1172`) and `round11.original_inputs.Z4.4` list only supplier numbers. These three items should be in the remaining list.

2. *Simultaneous construction.* The task brief and the chapter both speak of the suppliers "and their simultaneous construction"; `status.json` records only `remaining_supplier_numbers`. The assembly (`colsTiedSym_std`, `colsTwPTiedS_std`) is conditional on all nine and should be recorded as conditional.

3. *Sketched sub-lemmas inside the pending suppliers* (2.3 a-c, 2.5 a-e) are not in any list. If the four candidates are accepted, these should be carried as "proved in Lean, sketched" items.

The other three direct dependencies of the root (`perDecTwT_of_std`, the class sum, the place-tuple reduction) are outside this round; the round-5 review found the class-sum argument correct. The chapter's phrase "the already checked class sum" is consistent with that.

**Conclusion for Z4.4.** The supplier-level list is accurate. It is incomplete by the Weyl-duality boundary and by the conditional status of the assembly.

## 4. Claims of closure

- `ch_P_r11.tex:2-4`: "Both original inputs remain partial ... None has been added to the accepted count of thirteen original inputs out of twenty." Correct and consistent with the rest of the chapter.
- `status.json`: `units.Z1.2.status = partial`, `units.Z4.4.status = partial`; `round11.accepted_grade_changes = []`; `round11.independent_review_received = false`; the five subtheorems are `pending_review`; no occurrence of "complete" or "confirmed" in the `round11` block.
- "No new published theorem is invoked in this round": true for the five candidates (no literature leaves in their cones).
- No original input is claimed closed.

## 5. Requested corrections, in order of importance

1. Record in `status.json` and in the queue paragraph that `rankTwo` lies in the Z1.1 root cone, not the Z1.2 root cone, and that its acceptance does not change the Z1.2 root's remaining set.
2. Z1.2 remaining list: add `locPrints_of_litN` and the `FontaineBcris` record; replace "uniform dual Selmer bound" by `ordinary_vanishing_two_of_printed_hida` with `hida_x_of_printed_hida`, `core_o_of_literal_automorphy_n` (`has_operator_statement`, `count`, `b1O`), `regular_arithmetic_hida_of_literal_automorphy`, `locCFT`; label `h0GO`, `h0v0O`, `h0qO`, `locVO`, `phEqO`, `adExP`.
3. Z4.4 remaining list: add the Weyl-duality converse inputs and mark the assembly as conditional.
4. `rankTwo`: state finite residue field and residue characteristic ℓ; cover `C = 0`; add the finiteness sentence; name the discharge site `tan` (`BoxUnit.lean:128-160`) with `selLow`, `derOf`, `zn_ext`; cite the structure theorem.
5. Supplier 2: name `GLevH` as the input of `mem_Uloc_of_cong`; state `T ≠ g_i` and `n ≥ 1`; note that Lean's splitting uses `cmUnram`; cite the local-global lattice principle; expand the Iwahori step or label `splitStabL_of`, `split_integral_completion`, `self_dual_lattice_at` as proved in Lean, not reproduced.
6. Supplier 3: label `exists_isLocBasis`, `latS_of_locBasis`, `bwB_gramN_det`, `dual_le_bnd`, `rlv_yloc` as proved in Lean, not reproduced, or supply the missing sentences.
7. Supplier 6: put `StdTied` in the statement; fix the scope of `e_Y`.
8. Correct `til_tw` to `ExtMMulVecFix.lean:253-377`.

## 6. Summary

All five candidates state their Lean declarations correctly, with the right hypotheses, quantifier order and coefficient rings, and I found no mathematical error in any hand proof. Suppliers 5 and 6 are confirmed. `rankTwo` and suppliers 2 and 3 are confirmed with gaps: for `rankTwo` the gaps are edge cases and labelling; for suppliers 2 and 3 several local lattice lemmas are sketched in a sentence and uncited. The supplier-level cone counts and all checked line references are exact.

The remaining-open lists are accurate in what they name and incomplete in what they leave out. For Z1.2 the main omissions are the size and content of the vanishing input behind `DenseThresholdMainCase`, the discharge of `LocalPublishedTheorems`, and the fact that `rankTwo` and every other non-comparison item sit in the Z1.1 cone. For Z4.4 the omission is the Weyl-duality boundary. No original input is claimed closed, and both remain partial.
