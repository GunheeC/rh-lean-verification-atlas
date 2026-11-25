AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

# R5_review_B

AI review report produced during this project; file names are internal working names.

- Internal source file: `out/R5_review_B.md`
- SHA-256: `05c90c433f3b62c8976a82e7d18a6bc7204db9c0ed522890fc74383cffebf6e9`
- Report scope: Round-5 independent review B: Z4.2.01, Z4.2.03, Z4.2.05, Z4.4

## Internal report

The report below preserves its original verdict, scope and unresolved points. Historical review-machine home prefixes are displayed as `${REVIEW_HOME}`; the source checksum above identifies the original report. Source line numbers in other records count from its original title.

# Round-5 independent review B: Z4.2.01, Z4.2.03, Z4.2.05, Z4.4

Checked against the cleaned Lean copy `${REVIEW_HOME}/src/rh/src/` and the dependency graph (`graphq.py`, plus reachability scripts in `${REVIEW_TMP}/r5B/`). Line ranges quoted from the text were compared with the graph's ranges (original numbering), not with the cleaned copy. The original read-only tree was not consulted.

| Unit | Verdict |
|---|---|
| Z4.2.01 | COMPLETE CONFIRMED |
| Z4.2.03 | COMPLETE CONFIRMED (conditional on the joint, as the text says) |
| Z4.2.05 | COMPLETE CONFIRMED |
| Z4.4 | NOT COMPLETE (the class-sum argument is correct; the existence of the column and chain data it runs on is asserted, unlabelled) |

---

## Z4.2.01 — Standard local-model parameters

**Verdict: COMPLETE CONFIRMED.**

Text: `ch_P.tex` §"Z4.2.01. The parameters at a served site" (label `r5:Z4.2.01`). Lean: `GlobalTheory.TwU.std_at_served`, `StdAtServed.lean:9–22`.

1. **Complete earned?** Yes. All eleven fields of `Std` are accounted for and each matches the Lean term:
   - `prime`, `five_le` from `hg : GIdx` (`hg.1`, `hg.2.1`).
   - `two_le`, `even` from the local setting `P.setting v`.
   - `r_pos`, `two_r` from the `LatTied` rank clause plus `gat_k` and `2·rG ≤ D.R.k`, with both branches of the `if`.
   - `m_pos` from `mm = D.R.m` and `D.R.two_le_m`.
   - `base` from `Fills.base`, `dom` from `P.dom`.
   - `w_low` from the two halves of `Fills.w_ge` (a bound on a max).
   - `w_mono` from `Fills.w_mono`, which holds for all `j ≥ 1`, so the `l < m` restriction is simply dropped.
2. **Statement.** Matches. The quantifier order in Lean is `LatTied → 2·rG ≤ D.R.k → ∀ v, Std …`; the text fixes `v` after the hypotheses.
3. **Proof.** Correct. In the branch `r = 1`, `2r ≤ k₁+1` needs `2 ≤ D.R.k`, which follows from `2·rG ≤ D.R.k` and `rG = KG+1 ≥ 1`; the text's "both branches … by the explicit hypothesis" covers this.
4. **Labels.** "Hypothesis, discharged at the application" is accurate. The only caller is `GlobalTheory.TwV.site_cmpLite_siteAdm` (`JointSiteChainComparedCarriesAdmittedSystem.lean:77–89`), which passes `J.tied` and its own hypothesis `hk : 2 * rG L.sc ≤ D.R.k`, and then uses this `std` in `jointData_at_p_and_adelicDatum_nonempty` and `admissible_at_each_site`. The rank inequality is not discharged there; it stays an explicit hypothesis one level up (`modelsOK_of_joints`). The text says exactly that.
5. **Understanding.** Adequate for what is a bookkeeping lemma: the reader sees that `Std` is a list of size and weight conditions, each read off from the served-site index, the lattice tie or the fill, and that the one non-trivial point is the two-branch rank.

Minor points:
- "The lattice tie gives $m_f=D.R.m\ge2$ … $k_1+1=D.R.k$" merges three sources. `mm = D.R.m` and the `r` formula are from `LatTied`; `≥ 2` is `D.R.two_le_m` (rank data); `k₁+1 = D.R.k` is `GatTies.gat_k`, not the lattice tie. `GatTies` is cited in the footnote, so this is an attribution blur, not a gap.
- The `ch_Z` row does not mention `GatTies` as a hypothesis ("tied lattice data" has to be read as covering both `hT` and `LatTied`).

---

## Z4.2.03 — Adelic lattice dictionary

**Verdict: COMPLETE CONFIRMED** (for a given standard joint `J`; the joint's fields are hypotheses).

Text: `ch_P.tex` label `r5:small:Z4.2.03`. Lean: `GlobalTheory.TwV.joint_dict`, `LatticeTupleJointDictionary.lean:16–25`; `Joint.Dict`, `JointCmpEmbeddingY.lean:123–129`.

1. **Complete earned?** Yes. The Lean proof splits `j = 0` / `j+1` and assembles four conjuncts from seven lemmas. I read all seven and their main inputs; each step in the text corresponds to one:
   - Point condition: `basesAt_span` (basis from `latAt_isLattice`, chosen by `epsilon`), `exists_unitary_pt` (`yG · sec`), `isPt_pt_zero`, `pt_succ_isPt`. The "inverse reindexing gives back the same matrix" step is the local `hre` lemma.
   - Double coset: `ptEx_of` (surjectivity of representatives), `ptOne_of` (ratio is 1 off `p`, in the standard-lattice stabiliser at `p`, then `LocHyp` puts it in `U`), `IsCG1.pt`, `kaAt_pt`, `pt_zero_eq_rat_mul_rep_mul` (the `κ'⁻¹κ` correction via `J.y0` and `J.lev0`), `pt_succ_coset` (via `chart_succ_eq`, `Equiv.apply_symm_apply`).
   - Kernel lattice: `kerN_zero_eq_latK_pt`, `kerN_succ_heq` with `gram_succ`, `base_succ`, `latK_of_renamed`, all reducing to `reindex_rename_point_det_latK` after `subst`.
   - Determinant: `joint_dt_eq_det_of_isPt` (`dt` is by definition `det` of the chart matrix; reindexing preserves `det`).
2. **Statement.** Matches `Joint.Dict`: `∀ j ≤ m, ∀ La, IsLatTup La.2 → IsPt ∧ (∃ γ ∈ UJ, ∃ κ ∈ U, pt = rat γ · y · κ) ∧ HEq kerN latK ∧ dt = det pt`. The `ch_Z` row lists three assertions and omits the first (the point condition); the `ch_P` text lists all four.
3. **Proof.** Correct. Spot checks:
   - The ratio argument uses `x⁻¹x'` (right ratio), consistent with `κ` multiplying on the right.
   - The level-zero correction is `κ'⁻¹ * κ`, as in Lean.
   - The kernel-lattice equality is a heterogeneous equality after rank transport, which the text describes correctly as "the same submodule" once equal ranks are substituted.
4. **Labels.** "Hypothesis, discharged at the use" is accurate in what it claims. `joint_dict` has one caller, the alias `GlobalTheory.T.latticeTuple_joint_dictionary`, used in `admissible_at_each_site` (`…AdmittedSystem.lean:29–34`), which `site_cmpLite_siteAdm` invokes after building `std` from `J.tied`. The joint itself remains an argument of `site_cmpLite_siteAdm`; the text does not claim otherwise.
5. **Understanding.** Good. The text explains why one point serves all four clauses: the point is defined as the chart matrix up to reindexing, so the determinant and kernel-lattice clauses are transport identities, and the coset clause is "two bases of one lattice differ by a level-group element". That is the actual reason.

Minor points:
- The level-zero coset step also uses `J.cls0` (the label class equals `e0` of the level-zero class). The text mentions only the representative comparison `J.y0`.
- The integrality inputs to the ratio argument (`LocInt`, `LocHyp`, `bad_p` inside `OneHyp` / `H.core`) are joint and chart hypotheses. The text's phrase "satisfy the chart's local condition for the level group" covers them but does not name them as hypotheses.
- The level-zero kernel-lattice clause is given one sentence ("`J.lev0` identifies the base lattice"); the transport argument is spelled out only for the successor. It is the same lemma, so this is acceptable.
- The citation `site_cmpLite_siteAdm … :77–83` for "uses this dictionary" is indirect; the direct use is at `:29–34`, which is also cited.

---

## Z4.2.05 — Embedding and parity at each position

**Verdict: COMPLETE CONFIRMED.**

Text: `ch_P.tex` label `r5:small:Z4.2.05`. Lean: `GlobalTheory.TwV.pos_at_site`, `SitePlaceInducesPositionEmbeddings.lean:11–13`; `GlobalTheory.TwU.lamPos_of_posEmb`, `LamPosOfPosEmb.lean:39–54`.

1. **Complete earned?** Yes. Every step of the 15-line Lean proof is written out:
   - specialise the position identity at `x_s`;
   - `posArg_eq_self` (even: nothing; odd: `sigD(conj x) = x` via `involution_conj`);
   - `embLL_mem_alg` (image of a number-field element is algebraic);
   - `tEL_emb` (`embLL ∘ tEL = embT`);
   - unfold `lamC` on an algebraic argument;
   - apply `S.hK`; finish by definitional unfolding of `twG = iK ∘ ι ∘ σ^s`.
2. **Statement.** Matches `LamPos`: `∀ v s x, lamC lam (embT (pos ⟨v,s⟩) x) = twG X E v s (ρ v (if IsOddPos s then conj x else x))`, with `IsOddPos s` meaning `s.val % 2 = 1`. The `ch_Z` row is accurate.
3. **Proof.** Correct. The displayed intermediate `e(tEL_τ(x)) = ι_v σ_v^s ρ_v(x_s)` is exactly `h1` after the rewrite.
4. **Labels.** Accurate. `pos_at_site` passes `S.hK` (site field) and `(J.Gd.cmp.tie u w hg).pos_emb` (comparison tie of the joint). The consumer `admissible_at_each_site` obtains `hPos` from the alias and feeds it to `allSites_k1_of_dict_pair_pos_scal`, `kernelSite_law_and_fixedCoordinateStabiliserLaw` and both `frameValues` lemmas.
5. **Understanding.** Good. The reader sees that the statement is a compatibility of two embeddings of the same number-field element, and that the parity twist exists only because the tie's position identity is stated with the host conjugation on odd inputs, which is an involution.

Minor point: cited ranges differ slightly from the graph (`Joint.At.Pos` cited `157–160`, graph `159`; `tEL_emb` cited `18–26`, graph `21–26`; `Joint.At` cited `134–138`, graph `134–145`). Harmless.

---

## Z4.4 — Twisted periods on the selected chain

**Verdict: NOT COMPLETE.** The part of the proof that the text writes out for this declaration (per-class numerator, class sum, valuation bound) is correct and matches Lean. The step it rests on, existence of the standard column comparison `C` and the twisted chain data `t`, is asserted in one paragraph without proof and without a "Proved in Lean, not reproduced" label. That step is most of the Lean proof. By the blueprint's own convention (Z1.3.05 is "partial" because of an unreproduced Lean prerequisite), Z4.4 is partial.

Text: `ch_P.tex` §"Z4.4. A period on the chosen column system" (`sec:r5-z44`, lines 12022–12358). Lean: `GlobalTheory.PerTwClose.twistedPeriodAdmissible_of_rowInt`, `AdmissiblePeriodTwistOfIntegralRows.lean:14–21`.

### What the Lean proof is

Five steps:
1. `T.exists_standardColumnComparisons_trueColumns` (`colsTiedSym_std`) gives `C : ColsTiedSym` with `StdC`, `StdLvC`.
2. `T.trueColumnChoice_exists_standardChainData` (`colsTwPTiedS_std`) gives `t : SymmetricTwistedColumnsAtPrimes tp C (I.tw …)` with `I.StdTw`.
3. `perDecTwT_of_std`: per class `c`, an integer `b_c ∈ 𝓞_K` with `σ(b_c) = h_c · ⟨r_c j_M G, r_c z⟩`.
4. `perDecTw_of_at`: class decomposition of the period.
5. `perTwAt_of_perDecTw`: `y = Σ b_c / h_c` and the bound from `h_c ∣ DΓ_u`.

Dependency cone of the declaration: 15,659 nodes, 11,651 core theorems, about 74,700 theorem lines. Cones of the individual steps (overlapping): step 1 about 50,200 theorem lines, step 2 about 60,600, step 3 about 11,900, step 4 about 4,500, step 5 about 800.

### 1. Is "complete" earned? Steps asserted without proof or label

(a) **Existence of `C` and `t` (steps 1–2).** The text's second paragraph ("Construct the reference form comparison … always over $C$") is a 13-line description of the order of choices, citing only `colsTiedSym_std`, `underQ_iff`, `colsTwPTiedS_std`. Those two theorems are assemblies of nine suppliers, none of which is named anywhere in `ch_P`, `ch_T`, `ch_Z` or `P_notes.md` (grep count 0 for each name and for each module name):
   - `T.exists_standardFormComparison_symmetricLevel_members` (cone about 43,200 theorem lines)
   - `T.hermitianColumnChoices_of_formsLevelsClasses` (about 10,300)
   - `T.stepZeroHermitianLevel_uniformiser_kills_values_alt` (about 8,000)
   - `T.exists_hermitian_data_carT_of_std` (about 12,400)
   - `T.hermitianColumns_generators_baseLattices_functionals` (about 8,400)
   - `TC.spaces_in_coordinates` (about 6,800)
   - `T.trueColumnChoice_exists_chainData_with_basePoints` (about 51,000)
   - `T.tupleChains_levelStructure_compatible_at_levelPrime` (about 29,200)
   - `T.tupleLayerCompatibilities_of_X_prime` (about 24,500)

   These are not bookkeeping. `t` carries exactly the facts the later paragraphs use as given:
   - the period law `period z G = ipP (jM G) z` (`t.ptE.per`);
   - the Petersson expansion in an orthonormal frame (`t.pt.val.ipP`);
   - the point-space and rationality identifications (`t.pt.val.ptC`, `.rat`);
   - the `StdTw` coordinate identity `hS.2.2.eW` used to compute `r_c`.

   The sentences "The period law gives $P(w,G)=\langle j_MG,w\rangle_P$" and "In that frame the Petersson expansion … is a finite sum of class contributions" are therefore assertions about an object whose existence is not proved in the text. The only "Proved in Lean, not reproduced" label in the section covers "shared inputs outside the Z4.4 period comparison" (interlacing lowering, split theta), which is a different thing.

(b) **Δ/∇ duality.** "Their rational contraction lies in $\mathcal O_K$. Indeed dual frames pair by the identity, localization gives the standard dual lattices at each prime, and intersection gives the ring of integers." The localisation and intersection part is a fair sketch of `nabDelDual` / `dual_of_local`. The base fact, that the standard Weyl lattice and its dual pair integrally under the polynomial pairing (`T.standard_weyl_lattices_fock_dual`; cone of `pairBDualK` about 7,000 theorem lines), is used as known. It is not proved here, not cited as an earlier blueprint item and not labelled. (`ch_T` N354 lists "integral Fock lattice duality" as a hypothesis, so the blueprint elsewhere treats it as a named input.)

(c) **Literature leaves.** The cone contains three `lit` nodes, `GlobalTheory.Published.herm_col`, `exists_cc_eq_neg`, `exists_basis_one_imaginary`, entering through step 1–2 suppliers (`SelfDualGenus.*`, `LandherrStd.main`, `HermAdelicNorm.congr_of_signature_of_adelic_norm`). The three leaves themselves are elementary, but the callers indicate that the existence step passes through a Landherr-type classification and self-dual genus arguments. The Z4.4 text does not mention this.

### 2. Statement

Matches the Lean target `TwistedPeriodAdmissible`: `DGamDef D → ∀ u μ, UsedT μ → μ ≠ μ₀ → ∀ x ∈ ptLat, ∀ F ∈ M̃_μ, F ∈ V⁰_μ → ∃ y, embLL y = period (ptEmb x) (eMtTw⁻¹ F) ∧ ∀ w, resChar w ∉ Y.Qp μ → y = 0 ∨ −e_w·v_p(DΓ_u) ≤ v_w(y)`. One `y` for all `w`; sign and ramification index are correct (`ur D w (vDG D u w)`, `vDG = padicValNat p (D.mem u).C.DGam`). Hypotheses `Ok`, `Pins`, laws `l`, `l0`, `Later Z`, `RowInt`, `nch`, `tp` with `tp.xi = I.xi`, all `Y`: all present.

Minor: the `ch_Z` row says "admits the twisted-period decomposition"; the Lean conclusion is the admissibility bound, and the decomposition (`PerDecTw`) is an intermediate.

### 3. Proofs

In-scope paragraphs ("The numerator at one class", "One algebraic period at every good place"): correct and faithful.
- `pair_integral`: restricting both entries to `c` gives weight `wt c = 1/h_c` once (`petersson_single_left/right`); `period_single` gives the same weight; multiplying by `h_c` leaves the polynomial pairing of a Δ-vector with a ∇-vector at the same representative (`Lsh_eq_N`); integrality by `pairBDual`. The text's remark that taking `P(r_c z, G)` alone would insert the denominator twice is right.
- `perDecTw_of_at`: the extension outside the point space (whole period times `h_{c₀}` at one class; `z = 0` if no classes) matches `pcTw`.
- `perTwAt_of_perDecTw`: `y = Σ h_c⁻¹ b_c`; `h_c ∣ DΓ_u` via `stabMap_inj`, `dvd_DGam`, `DGamDef.one`; `v_w(h_c) = e_w·k ≤ e_w·v_p(DΓ_u)` (`vAdd_dvd_le`); ultrametric sum including zero terms. Lean proves the numerator integral at every `w`, slightly more than needed.
- No wrong inequality direction or missing case found.

Out-of-scope paragraphs. Three of the six proof paragraphs argue for other declarations. Reachability check: every lemma cited in them is outside the cone of `twistedPeriodAdmissible_of_rowInt`.
- "Evaluation and branching on these lattices" (`isLocBasis_snoc`, `rhoVr_brAt_eq_brStd`, `brStd_mem_delStd`, `coP_PtT_eq_blk`, `ptT_forms_built`, `mem_locW_delAtr_iff`, `latCo_one/gen`, `blk_IntSpan_of`, `lowerTieTwAt_integral`, `exists_mem_SP_of_coP_mem`, `desc`) belongs to twisted *point* integrality (`twistedPointIntegral_of_TC_ok` → `row_aPtTw_of_overCols`), a sibling theorem.
- "Comparison at a level prime" and "Comparison at a generator prime" (`levelChainSharpColumnValuation_of_stability`, `eventually_level_prime_coprime_stabiliser_of_design`, `pair0U`, `pairTwU`, `period_geTU`, `admissible_at_twist_places`, `tiesAt_true`, `jetAtSplit_of`, `jetLossAll_of_jetSplitAmb`, `colMu_bound_all`, `sizeAt_of_params`, `boundAt_of_chainTie`, `not_dvd_card_of_injective`, `vG_loss_le`, `row_atG_of_jetSplitAmb`, `atG_coreU`, `admissible_at_generator_places`, `admissible_off_twist_places`) are consumers of `TwistedPeriodAdmissible` inside `admissible_level_two`, or parallel inputs to it.
- The reference-tuple sentences (`perDec0At_std`, `admissiblePeriodZero_of_classPeriodDecomposition`) are also outside the cone.

These paragraphs may be useful for the parent input, but they do not contribute to this unit's declaration and should not count toward its completeness. I did not verify them line by line. Arithmetic spot checks passed:
- the accumulated exponent `m·d + s₀|V|·m(m+1)/2 = m·E_T` agrees with `loss_eq` and `EatT`;
- the cyclotomic-degree argument for `p`-unit stabilisers is sound;
- the case split for `6A²N_m + 2 < Y` holds under `A ≥ 10`, `N_m ≥ 2`, `A⁸, N_m¹⁶ ≤ Y`.

### 4. Labels

- "[Hypothesis, discharged at the constructed point]": accurate. The only caller is `row_aPerTw_of_overCols` (`TwistedPeriodsIntegralAtBundlePoints.lean:11–19`), which supplies `w.ok`, `w.pins`, `cv.rowInt`, `cv.tup` (the tuple with `tp.xi = I.xi`) and rewrites by `cv.tw_eq`. `rowInt_over` feeds `T.periodRowLatticesIntegral_provisionalRows`.
- `famU` / `admissible_level_two` take `TwistedPeriodAdmissible` as a hypothesis (`AdmissibleAtGeneratorPlaces.lean:214–245, 263–300`): accurate as a description of the consumer.
- "[Proved in Lean, not reproduced: shared inputs outside the Z4.4 period comparison]" names `branching_interlacing_pairs`, `split_place_scaled_bound`, `jetAtSplit`. All three are outside this declaration's cone, so the label is true but irrelevant to this unit. `P_notes.md` "A. … No residual within the Z4.4 period statement" is therefore not correct: the residual is items (a)–(b) above.
- `P_notes.md` is internally inconsistent: line 28 says "Z4.4 — complete", while the tables at lines 159 and 1123 still read "partial" for Z4.4.

### 5. Understanding

For the class sum itself the text does explain why the result holds, and well: the period is a Petersson pairing; the Petersson form is a sum over classes weighted by inverse stabiliser orders; at each class the two polynomial values lie in dual lattices and so pair to an integer; hence the period is `Σ b_c/h_c` and its only denominators are stabiliser orders, which divide `DΓ_u`. The "denominator twice" remark shows the normalisation is understood. What the reader does not learn is why the twisted column admits a model in which all this is true: why the period of the twisted system is the Petersson pairing against `j_M G` on those lattices, with those class representatives and stabilisers. That is the content of `C` and `t`, and the text describes it only as an order of choices. The three extra paragraphs make the section look more complete than it is for this declaration, and make it harder to see where the actual proof ends.

---

## Most important problems

1. **Z4.4: existence of the column comparison and chain data is unproved and unlabelled.** `colsTiedSym_std` and `colsTwPTiedS_std` are cited as if they were choices; they rest on nine supplier theorems (cones of 7k to 51k theorem lines each, the bulk of the 74.7k-line cone) that appear nowhere in the blueprint. The period law, Petersson expansion and point-lattice identification used in the class-sum argument are fields of the object whose existence is skipped. Status should be "partial" until this is either reproduced or labelled "Proved in Lean, not reproduced" with the nine names.
2. **Z4.4: half the section proves other theorems.** "Evaluation and branching", "level prime" and "generator prime" cite only lemmas outside the cone of `twistedPeriodAdmissible_of_rowInt` (they belong to `twistedPointIntegral_of_TC_ok` and to the `admissible_level_two` consumers). The `P_notes` summary "What was reconstructed" lists mostly these. They should not be counted as closing this unit.
3. **Z4.4: Δ/∇ lattice duality is used as known.** The standard-lattice duality (`standard_weyl_lattices_fock_dual`) behind `pairBDual` needs a proof, a reference to an earlier item, or a label.
4. **Z4.4: `P_notes.md` residual line and tables.** "No residual within the Z4.4 period statement" is not right; the lines 159 and 1123 still say "partial".
5. **Z4.2.01 / Z4.2.03 / Z4.2.05: no substantive problems.** Only attribution details: `k₁+1 = D.R.k` and `m ≥ 2` are not from the lattice tie; the `ch_Z` row for Z4.2.03 omits the point-condition clause; `J.cls0` and the `OneHyp` integrality fields are used but not named; a few cited line ranges are off by a few lines.
