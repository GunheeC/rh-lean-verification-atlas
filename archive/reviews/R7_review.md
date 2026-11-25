AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

# R7_review

AI review report produced during this project; file names are internal working names.

- Internal source file: `out/R7_review.md`
- SHA-256: `2d65c55fd3ed203cf7c1a96dd5301f607647293c45a1cf956e1c503f109090d0`
- Report scope: Round-7 independent review — Z4.2.06, Z4.2.07, Z4.2.10, Z4.2.11; Z1.3 publication comparison; four Z4.2 partials; trust ledger

## Archived report · [English summary](../../reviews/R7_review.md)

The report below preserves its original verdict, scope and unresolved points. Historical review-machine home prefixes are displayed as `${REVIEW_HOME}`; the source checksum above identifies the original report. Superseded graph percentages have been removed from this public edition. Source line numbers in other records count from its original title.

# Round-7 independent review — Z4.2.06, Z4.2.07, Z4.2.10, Z4.2.11; Z1.3 publication comparison; four Z4.2 partials; trust ledger

Scope. This review checks whether the hand proofs in the blueprint faithfully and rigorously cover the Lean statements they label, and whether the bookkeeping is honest. It says nothing about whether RH is proved. Every unit below is an internal implication with stated hypotheses.

Sources read: `${REVIEW_HOME}/work/prev7/ch_P.tex`, `ch_P_r7.tex`, `status.json`, `ch_trust.tex`, `trust_tables.tex`, `omission_summary.tex`, `blueprint_v9.pdf` (via `all.txt` and a fresh `pdftotext` of pp. 1–16); the Lean tree under `${REVIEW_HOME}/src/rh/src`; the dependency graph behind `graphq.py`; `prev6/R6_review.md`, `prev5/R5_review_{A,B,C}.md`.

Conventions.

- Lean line ranges are in the original numbering used by the blueprint and `graphq.py`. The cleaned copy on disk is shifted by about +5 lines.
- "Theorem lines" below is my own measure: core theorem declarations with a source range, weighted `l1 − l0 + 1`, summed over a dependency cone. It is not the ledger's weighting (which also counts definitions).
- "Never named" means the declaration's short name does not occur anywhere in `ch_P.tex` or `ch_P_r7.tex`. It is a proxy for "not reproduced", not a proof of it: an argument can be reproduced without naming the lemma. I use it only to locate candidates and then check the text.

## Verdict table

| Item | Lean root | Verdict |
|---|---|---|
| Z4.2.06 | `GlobalTheory.TwV.move_at_site`, `KernelSiteArithmeticGroupMovesFrames.lean:13–15` | **COMPLETE WITH GAPS** — statement faithful; the new eigenvalue and scalar computations are correct and match Lean; no bracketed hypothesis or not-reproduced labels; the existence of the move `(g, κ)` is still the v8 sketch; algebraicity of the datum scalar is not stated |
| Z4.2.07 | `GlobalTheory.TwV.away_of_dict`, `KernelSiteSeriesIndependentAwayFromPlaceOverP.lean:13–16` | **COMPLETE WITH GAPS** — statement faithful; the coefficient-field descent of both units is correct where checked; several one-sentence steps cover Lean lemmas that are never named; no bracketed labels |
| Z4.2.10 | `GlobalTheory.TwV.StepZero.del_zero`, `KernelSiteFrameValuesStepZero.lean:10–13` | **NOT COMPLETE** — the site-series formula rests on an unproved, unnamed, unlabelled Lean theorem (`kerTh_eq_pull`) whose inputs are not among the unit's hypotheses; four further Lean inputs are asserted in one sentence each |
| Z4.2.11 | `GlobalTheory.TwV.StepDel.del_of_pos`, `KernelSiteFrameValuesPositiveSteps.lean:10–12` | **NOT COMPLETE** — same Lean theorem (`tieDel_all_steps`) and same gaps as Z4.2.10 |
| Z1.3: Tate citation (A01) | `GlobalTheory.T.integral_tate_inertia_cyclotomic_twist_torsion` | **Citation real and says what is used** (checked against a scan, see below); the work is not in the bibliography |
| Z1.3: hand proofs C01, C02, C03 | `exists_pres_smoothed`, `hilbert_ninety`, `pDiv` | **Correct where checked**; C02 fully checked, C01 and C03 checked at the level of every displayed identity |
| Z1.3 count | — | 13 = 1 (a) + 9 (b) + 3 (c) agrees with `status.json` (`kato_gaps`) and with the text |
| Z4.2.02 partial | `joint_at_nonempty` | Remaining statement **matches a Lean declaration** (`topLawQ_midTop`); it is **not the only missing piece** |
| Z4.2.04 partial | `pairOK_allSites` | Remaining statement matches a local `have` in `ta_thMoved` (supplied by `coefIn_translate` and `thZero_coefIn`); **not the only missing piece** |
| Z4.2.09 partial | `site_law_xiIn` | Remaining statement is a paraphrase of two Lean theorems; **a much larger input (`TieBase.base_data`) is missing and not listed** |
| Z4.2.12 partial | `site_cmpLite_siteAdm` | Remaining statement is a conjunction of the three above, **not one Lean declaration**; inherits their gaps and the Z4.2.10–11 gap |
| Trust ledger numbers | — | `trust_tables.tex` agrees with `status.json` and with an independent recomputation from the graph (30/15/9, 24 open, 13/7, all line counts) |
| Trust ledger wording | — | Disclaimer present. Two sentences need repair (sign-off sentence; "complete" for Z4.2.10–11) |
| PDF vs sources | — | **PDF is stale in the trust ledger**: five numbers and two sentences differ from the current sources. Unit statuses and open-unit tables agree |

---

## Z4.2.06 — Arithmetic translation of the frames

Blueprint: `ch_P_r7.tex:36–50` (common frame), `ch_P_r7.tex:52–70` (label `r7:Z4.2.06`), v8 text `ch_P.tex:13189–13199` (label `r6:Z4.2.06`), map item `ch_P.tex:11685`.

### Statement vs Lean — matches

- Root: `move_at_site : AllSites (… S => J.Dict std → S.Move)`. `S.Move` is `MoveTie` (`Definitions/GaloisGeometry/NatCastMemOfPlace.lean:75`, cleaned numbering): for `j < mm`, a component `c`, a valid source `L`, a valid target `La'` and `γ ∈ Γ`, there exist a matrix `e` over `E` and `cΞ ∈ ℂ` with `e·e* = 1`, the frame relation at every `v`, `kerN(γL) = e·kerN(L)`, `cΞ ∈ Q̄`, the datum relation, and the scalar identity `pPow(γL)·λ(scal0(γL)/chiFac(γL)·cΞ) = kapG(γ)⁻¹·pPow(L)·λ(scal0(L)/chiFac(L))`.
- The `status.json` statement is an informal but faithful summary. Quantifier order is harmless: Lean allows `e, cΞ` to depend on the target; the blueprint builds them from the source alone.
- Constants: `A = ⌊j(t+1)/2⌋`, `B = ⌊(m_{j+1}+1)/2⌋` (`ch_P_r7.tex:53`) are exactly the two shifts in Lean `FillAt` (`IsUnifAt.lean`, `FillAt`) and in `kapG_at_site`.

### Proof check

The Lean root is two lines: it applies `site_move` (`KernelSiteArithmeticGroupMove.lean:18–35`) to `Dict`, the split pair `⟨J.alg0, J.alg⟩`, `pos_at_site S` (Z4.2.05) and `kernelSite_latticeTuplePairs_admissible S hD` (the root theorem of Z4.2.04, partial).

| Blueprint step | Lean step | Check |
|---|---|---|
| `det γ_v = ρ_v(det g)`; `ℓ_v(γL) − ℓ_v(L) = −ord_v ρ_v(det g)` (`ch_P_r7.tex:37–42`) | `kapG_at_site` (`hdet`, `hlen`), `len_smul_tup` | Correct. Cancelling `det F_v` uses `isUnit_det_frameMatrix_ofCharts`, as in Lean |
| `ā = a⁻¹`; even/odd slot; factor `λ(τ(a)^{w_vs})` (`:46`) | `kapG_eq_char_inf` (`KapGEqCharInf.lean:19–64`) | Correct. The odd-slot sign reversal is the `inv_zpow'` step in Lean |
| `w_vs = e_{pos(v,s)} − A − B` (`:53`) | `fillAt_of_comp`, `wG_succ_eq_shift` | Correct. I re-derived the two halves `j(b₀+1)` and `a₀+(j+1)(b₀+1)`. Needs a component at level `j+1`; the target supplies it |
| `kapG(γ) = λ(χ_lev(κ) μ(d) P^{−A−B})·p^{Σ V_v(ℓ_v(γL) − ℓ_v(L))}` (`:55–56`) | conclusion of `kapG_at_site` | Matches |
| `Q'·(μ(det κ)/χ_lev(κ))·(χ_lev(κ) μ(d) P^{−A−B}) = Q` (`:63–66`) | `scal_core`, `hcore` in `moveBy_scal` (`LatticeTupleMoveScalarPowerOfP.lean:34–52, 55–116`) | Correct. I checked the exponents: `x^{−A}` gives `P^A`, `1/x^B` gives `P^B`, target factors cancel |
| "Apply λ … old p-power is the new one times the length correction" (`:67`) | `hpp`, final `field_simp` | Correct. `Q'·cΞ` is algebraic because `Q` and the bracket are; this is `hAγQ` in Lean |

I found no mathematical error in the v9 text.

### Problems

1. **No "[Hypothesis, discharged at …]" label** in `ch_P_r7.tex:52–70`. The text says only "this proves complete under the dictionary" (`:67`). Discharge site, verified with the graph: `move_at_site` ← `GlobalTheory.T.kernelSite_arithmeticGroup_moves_frames` (a pass-through wrapper) ← `admissible_at_each_site` (`JointSiteChainComparedCarriesAdmittedSystem.lean:29–75`), where `hDict := latticeTuple_joint_dictionary` (Z4.2.03, complete). The ledger paragraph "A premise at a use site" (`ch_trust.tex:258–267`) names this site; the unit itself does not.
2. **No "[Proved in Lean, not reproduced: …]" label anywhere in the unit**, although the existence of `(g, κ)` with `MoveBy` is still the six-sentence v8 sketch (`ch_P.tex:13191`). The Lean content behind it that the blueprint never names:
   - `isPt_move_eq` (`IsPtMoveEq.lean:14–27`): point representatives of `L` and `γL` differ by the rational element on the left and a level element on the right, with `χ(κ)·χ(κ_a) = 1`;
   - `awayEx_of` and the tie field `lev0AtOf_compatible.chi` (source of the coefficient `r` with `embLL r = χ_lev(κ)`);
   - `movedDatum_pair_eq_adelicDatum_two_points`, `latK_rat_mul_lev`, `latticeTuple_chart_eq_of_same_component`, `latticeTuple_frameMatrices_eq_of_same_component`;
   - `chi_detId_smulLat` (`CharDeterminantIdealUnitarySmulSelfDual.lean:14`): "its new value is `P⁻¹x`" (`ch_P_r7.tex:62`) is this lemma, stated in one sentence;
   - `eMat_unitary_det`.
   
   Size: outside the cones of Z4.2.01, .03, .04, .05, .08 the root reaches 1,045 theorem lines, 677 of them in theorems never named. The gap is small, but it is unlabelled.
3. **Algebraicity of `cΞ` is not stated.** `MoveTie` requires `cΞ ∈ Q̄` for `cΞ = μ(det κ)/χ_lev(κ)`. Lean gets it from the site-law field `mu_alg` and from `χ_lev(κ) = embLL r` (`xiM_smul_moveBy`). The blueprint proves only that `Q'·cΞ` is algebraic (`ch_P_r7.tex:67`).
4. **Dependence on the partial unit Z4.2.04.** The Lean root consumes the whole Pair theorem. `moveBy_scal` reads only three fields of it: admitted lattices, `scal0 ∈ Q̄`, `chiFac ∈ Q̄` (cleaned line 65, `obtain ⟨hA1, -, -, -, hs1, hf1, -, -⟩`). The blueprint says "It uses the lattice and scalar fields established on page r6:Z4.2.04" (`:67`). That is accurate. But those fields are themselves asserted on that page by citation (`ch_P.tex:13184`, "supplied by the determinant-character calculation on this same pair"), not proved there. Same recurring issue as R6, Z4.2.08, problem 2.
5. **Site-law fields used as givens** (`mu_mul`, `mu_ne`, `mu_rat`, `S.hK`) are not flagged as hypotheses carried by the site record `J.At`, whose existence is Z4.2.02 (partial). Recurring from R6, Z4.2.08, problem 3.
6. **Stale label.** `ch_P.tex:13199` still reads "A. Proved in Lean, not reproduced" for the `kapG` identity that v9 now reproduces. The header says "(v8)" and line 13190 points forward, so a careful reader is not misled, but the two pages contradict each other.

Uncited standard facts: none of substance.

---

## Z4.2.07 — Comparison away from a split prime

Blueprint: `ch_P_r7.tex:72–95` (label `r7:Z4.2.07`), v8 text `ch_P.tex:13233–13242`, map item `ch_P.tex:11688`.

### Statement vs Lean — matches

- Root: `away_of_dict : AllSites (… S => J.Dict std → S.Away)`. `S.Away` is `∀ v, ∀ j < m, AwayTie …`: a split prime `P` with trivial localized half-different, `P` and its conjugate outside the bad set and prime to the reader level, the two approximation clauses, and `u, u'` of valuation zero such that tuples with equal away data have equal off-prime lattices, equal frames, equal data and the scalar identity with `u^{len}`, `u'^{len}`.
- `u, u'` are chosen before the tuples in Lean. The blueprint's two elements `p^{−V}embW(r_μ r_j)`, `p^{V}embW(r_μ⁻¹ r_{j+1}⁻¹)` (`ch_P_r7.tex:87–91`) depend only on `v, j` and the chosen `π`. Correct order.

### Proof check

The Lean root applies `away_of_pos_pair` (`KernelSiteAwayOfPositivePair.lean:21–73`) to `Dict`, the split pair, `J.kin`, `pos_at_site` and the Pair theorem.

| Blueprint step | Lean step | Check |
|---|---|---|
| `x' = (s,1)`, `x'/x̄' = π`; transport; `b_P = 1` away from `p` by infinite divisibility (`:73`) | `exists_h90_oneOff_preimage_at_splitPlace`, `transfer_eq_zero` | Correct. `D₀z/l^h` integral for all `h` forces the `P`-component to vanish |
| `μ₀` unramified over `p`; value is a product of uniformizer values in the pinning's field; `KIn` gives `r_μ ∈ LL` (`:77`) | `mu_mem_LL` (`StepCharacterUniformizingIdeleMemCoeffField.lean:89–175`) | Plausible and consistent with the Lean statement; I did not trace the pinning identities |
| `C⁻¹ diag(π,1,…,1) C` preserves the Gram matrix, determinant `π`; decomposition into rational × class × level; `r_i` (`:80–83`) | `exists_upts_det`, `tw_ch_rat`, `chiI_pow_rat` (`…CharPowValuesInCoeffField.lean:21–128`) | The matrix computation is correct (`D*D = 1` since `ππ̄ = 1`). The decomposition is the class-representative bijection of the joint |
| Both elements have embedded norm one (`:92`) | `two_units` (`TwoUnitsAtPlaceUniformizingIdele.lean:38–81`) | Correct: `‖λ(μ(π))‖ = ‖p‖^V` by Z4.2.08, `‖λ(χ_I(π))‖ = 1` by the inert-prime computation |
| Scalar identity for equal away data (`ch_P.tex:13238–13240`) | `key`, `final`, `scal_away` | I re-derived it: with `n, n'` the length differences, `p^{V(n−n')}·u^n·u'^{n'}` equals the ratio of the two `scal0`. The powers of `p`, `M`, `C` cancel as claimed |

The claim "These were obtained before the open Taylor clause in Z4.2.04" (`ch_P_r7.tex:92`) is accurate: `scal_away` reads only `.1` (self-duality) and `.2.2.2.2.1` (`scal0 ∈ Q̄`) of Pair.

### Problems

1. **No bracketed "[Hypothesis, discharged at …]" label.** The discharge is given in prose (`:92`: "At the call in `admissible_at_each_site` the site is fixed, Z4.2.03 gives its dictionary and Z4.2.05 its position comparison"). The site is correct and is the real one (verified: `away_of_dict` ← wrapper `kernelSite_series_independent_away_from_place_over_p` ← `admissible_at_each_site`). The cited range `29–38` covers it.
2. **`KIn t` is a hypothesis of `away_of_pos_pair` and `two_units`**, supplied by the joint field `J.kin`. The blueprint uses it (`:77`) without saying where it comes from.
3. **No "[Proved in Lean, not reproduced]" label**, although several steps are one sentence over Lean lemmas that are never named:
   - `eqOff_kerN_of_sameAway` is cited, but its inputs are not: `AdelicLatticeSmulMemOfAgreeAwayFromPlace` (228 lines), `KernelLatticeEqAwayFromPrimeOfAgreeOffPlace` (143), `AdelicPointsAgreeAwayOfLatticeTuplesAgreeAway` (65). The blueprint's whole argument is "The dictionary then identifies the lattices off the split prime pair" (`ch_P.tex:13239`);
   - `movedDatum_eq_of_latticeTuples_agreeAway` (equality of the finite data) is not mentioned at all; the blueprint states the conclusion only;
   - `det_latticeTuples_agreeing_away_from_place` (the determinants differ by a power of `π` times an integral norm-one unit) is the step that makes the scalar comparison work; it is implicit in "the powers of M, C, p cancel";
   - `exists_normOne_idele_order_one_trivial_elsewhere`, `level_badPrimes_coprime_residueChar`.
   
   Size: outside the cones of Z4.2.01, .03, .05, .08 the root reaches 3,053 theorem lines, 2,400 of them in theorems never named. Part of this is the Pair cone.
4. **Line references.** `away_of_pos_pair` is at `21–73`, cited as `25–73`. Minor.
5. **Stale label.** `ch_P.tex:13242` still reads "A. Proved in Lean, not reproduced" for the coefficient-field realization that v9 reproduces.

Uncited standard facts: none of substance.

---

## Z4.2.10 and Z4.2.11 — Change of kernel at level zero and at positive levels

Blueprint: `ch_P_r7.tex:162–343` (common contraction, label `r7:z42-common-operator`), `ch_P_r7.tex:451–513` (specializations, labels `r7:Z4.2.10`, `r7:Z4.2.11`), v8 text `ch_P.tex:13263–13282`, map items `ch_P.tex:11697`, `11700`.

Both Lean roots are one-line specializations of `tieDel_all_steps` (`KernelSiteFrameValuesAllStepsLtM.lean:23–94`), so they stand or fall together.

### Statement vs Lean — matches

- `del_zero : AllSites (… S => J.Dict std → S.Pair → S.Pos → S.Law → S.Del 0)`; `del_of_pos : … → ∀ j, 1 ≤ j → j < m → S.Del j`.
- `S.Del j` (`JointCmpEmbeddingY.lean`): for every `ι : ℂ →+* ℂ_p` extending `S.lam` there is `c_K` with `‖c_K‖ = 1` and `KernelDifferenceAtLevel … j c_K`. Order `∀ ι ∃ c_K` is kept in the blueprint (`ch_P_r7.tex:489`, `:501–502`).
- The four hypotheses are printed (`:491`, `:503–504`).

### What is correct

- The coefficient identity `⟨P, f(Uz)⟩ = ⟨trSub_U P, f⟩` (`ch_P_r7.tex:214–223`). I verified it on monomials: both sides equal `Σ_d n! m! Π U_ik^{d_ik}/d_ik!` over matrices `d` with row sums `n` and column sums `m`.
- The reduction to one polynomial `V_{d₀}` by injectivity of `ι` on coefficients (`:477–479`) is exactly `MvPolynomial.map_injective` in `tieDel_all_steps`.
- The empty-component case with `c_K = 1` (`:453–454`).
- The generic-vanishing argument for polynomial identities (`:309–312`).
- The scalar bookkeeping `c_K(e_S/e_T)c_A(B)s_O s_H = s_cT ι(ρ_S ρ_T)` (`:327–334`) is consistent with the Lean hypotheses `hsc`, `hChi` and `eFac_mul_pPow`.

### Why "complete" is not earned

1. **The site-series formula `srOf = (e_S/e_T)·f(V L_B z)` rests on an unproved theorem.** The blueprint's entire argument is (`ch_P_r7.tex:197–199`): "To see the last equality, take the site law on representatives. The two unitary decomposition matrices give a linear pullback of the class kernel with nonzero scalar." In Lean this sentence is
   - `serAt_all` (`ThetaSeriesSiteEqChangedFrameClassSeries.lean:11–19`, cited), which calls
   - `pullAt_of_dict` (`LatticeTupleKernelEqSmulPullbackClassKernel.lean:21–49`), which calls
   - `GlobalTheory.TwV.SPull.kerTh_eq_pull` (`ThetaKernelFunctionAdelicPointsEqPullbackClassKe.lean:65–79`): for adelic points `x = γ·y_c·κ`, `x' = γ'·y_{c'}·κ'`, the kernel theta function of the two transported lattices equals an explicit scalar times the pullback by `(γ, γ')` of the class kernel `Th(c, c')`.
   
   `kerTh_eq_pull` in turn uses
   - `kernelEntry_period_ne_zero_and_lattice_laws` = `TieBase.base_data` (`KernelEntryPeriodNeZeroAndLatticeLaws.lean:14–19`): `δ ≠ 0`, `LatAll`, `VecP`, `EqP` for the tied base, proved from `NatEqui.eqP` (`NormalisedFamilySatisfiesEquivarianceLaws.lean:59–117`) and `ColNorms.familyVectors` (`NormalisedFamilyNonzeroThetaVectorsNumberField.lean:15–50`);
   - `KerMove.kerTh_move` (`KernelThetaAdmissibleLattices.lean`): the kernel theta function of unitarily moved lattices is the pullback of the kernel theta function;
   - `th_eq_kerTh` (`ConsecutiveClassesKernelEqKernelFunctionTranspor.lean:14–20`): the class kernel equals the kernel theta function of the class lattices.
   
   None of `pullAt_of_dict`, `kerTh_eq_pull`, `base_data`, `eqP`, `familyVectors`, `kerTh_move`, `th_eq_kerTh` occurs anywhere in `ch_P.tex`, `ch_P_r7.tex` or the 826-page PDF text. `base_data` has a cone of 51,268 theorem lines. These facts are **not consequences of Dict, Pair, Pos, Law**: Law concerns arithmetic-group moves of site tuples, not rational isometries carrying class representatives to tuple points. So this is a missing proof inside the unit, not a hypothesis. It has no "[Proved in Lean, not reproduced]" label.
2. **Four further Lean inputs are asserted in one sentence each**, each with a cone of several thousand theorem lines outside Z4.2.01–.09:
   - `cKs_unit_indep` (3,313 theorem lines outside Z4.2.01–.09). The blueprint (`:456–462`) says the factors are "powers of the norm-one site scale and the derivation generators". That the Lubin–Tate scale `ltC` and the derivation generators have norm one is where the Lean cone goes (`DatumCurveIntegralUnitDiscModel`, `HasRationalTorsionIffMemRange`, `FirstOrderRigid`, `DetOrthonormalCoordsMulBasisLocalUnit`); the blueprint gives no argument;
   - `unit_mul_scal_eq_scT` (3,985). The blueprint (`:330`) writes "The equality `c_K c_A(B) s_O ι(u_S) ι(u_T) = s_cT` now gives …" and cites the Lean lines. The equality itself is not derived;
   - `moved_forms_at_source` (3,549; includes `SharpPoly`, `RealisingPolynomialBlockwiseHomogeneous`). One paragraph (`:302–321`);
   - `transported_frame_realAt` (2,453). Five sentences (`:466–474`).
3. **Smaller unnamed inputs**: `exists_adelic_latticeTuple_decomposition` ("The dictionary gives a decomposition `d₀`", `:477`), `operatorOnFrame_and_classSummand_polynomial` (the reading `φ κ y = (Π de^{sDiv})⁻¹·frPoly P y`), `rdJ_eq_of_realAt` (named only in the v8 text), `frames_invertible`, `wt_polDY_framePol`, `kernelScalar_of_sourceTarget_parts_product` (cited as `tieChiH_of_parts`, not derived).
4. **Size.** Outside the cones of Z4.2.01–.09, `del_zero` reaches 9,913 theorem lines; 8,461 are in theorems never named. Outside the completed units only (.01, .03, .05, .08) it reaches 41,987, of which 39,262 are never named. A 180-line prose section cannot be a reproduction of this; it is an accurate road map with correct central identities.
5. **Hypotheses discharged by open units.** `admissible_at_each_site` supplies Pair from Z4.2.04 (partial) and Law from Z4.2.09 (partial). The blueprint lists the four suppliers (`:509–513`) but does not say that two of them are open. There is no bracketed label. The discharge site itself is correct (verified with the graph; `61–71` covers the two calls).
6. **Stale labels.** `ch_P.tex:13275` and `13282` still read "A. Proved in Lean, not reproduced … The mixed chain-rule and coefficient-pairing identity in these coordinates is the outstanding hand check."

This is the same pattern for which R5 withdrew "complete" from Z4.4 and Z1.2.

### What would make the status accurate

Mark both units partial with remaining inputs stated as Lean declarations: (A) `kerTh_eq_pull` together with `TieBase.base_data`; (B) `cKs_unit_indep`; (C) `unit_mul_scal_eq_scT`; (D) `moved_forms_at_source`; (E) `transported_frame_realAt`. Alternatively, reproduce (B)–(E) and state (A) as the one remaining proposition, shared with Z4.2.09.

Uncited standard fact: existence of a ring homomorphism `ι : ℂ → ℂ_p` extending a given embedding of `Q̄` (used at `ch_P.tex:13288`, `ch_P_r7.tex:550`; Lean `place_extends_to_iso`). It needs equal transcendence degree and choice. It belongs to Z4.2.12 but both units quantify over such `ι`.

---

## Z1.3 — publication comparison (13 gaps)

Blueprint: `ch_P_r7.tex:566–863`. Register: `status.json`, key `kato_gaps`.

### Count

`kato_gaps` has 13 entries: A01 (closed), B01–B09 (open), C01–C03 (closed). This agrees with `ch_P_r7.tex:567–570` and with the open-unit rows in `trust_tables.tex` (B01, B02; C01, B03; A01, C02, B04, B05; B06, B07; C03, B08, B09). All six units Z1.3.01–.05 and .08 remain partial in `status.json`. The bookkeeping is consistent.

### A01 — the Tate citation

- **Which work.** J. Tate, *p-Divisible Groups*, in *Proceedings of a Conference on Local Fields* (Driebergen 1966), Springer 1967. It is cited inline only (`ch_P_r7.tex:662–668`). It is **not a bibliography record**: `status.json` lists it under `literature_works` with `origin: "separately cited"` and empty `bib_keys`; the PDF bibliography has no entry for it; the only bib file on disk (`${REVIEW_HOME}/work/blueprint/bib.tex`, an older 24-item file) has Lubin–Tate 1965 but not this paper.
- **How I checked.** I did not use the link printed in the blueprint. I fetched an OCR scan of the paper hosted at the University of Rochester (`https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/tate-pdiv-ocr.pdf`) through a web-fetch tool that returns an extraction of the page text, not the raw PDF. The extraction reports:
  - §3 standing hypotheses (p. 170): `R` a complete discrete valuation ring of characteristic 0 with perfect residue field of characteristic `p`; `K` its fraction field; `C` the completion of `K̄`;
  - §3.3 (p. 176): `χ : G → K*` a continuous homomorphism, `K_∞` the extension determined by `Ker χ`;
  - Theorem 2 (p. 176): if there is a finite extension `K₀` of `K` inside `K_∞` such that `K_∞/K₀` is totally ramified with Galois group `Z_p`, then `H⁰(G, C(χ)) = 0` and `H¹(G, C(χ)) = 0`.
  
  The OCR garbles some symbols; the section number, theorem number, page and the two vanishing statements are unambiguous. I regard the citation as **verified at the level of statement and hypotheses**. I did not read Tate's proof.
- **Does it say what is used?** Yes. The blueprint uses "vanishing of both continuous `H⁰` and `H¹` for a one-dimensional twist … whose character cuts out, after finite base extension, a totally ramified `Z_ℓ`-extension" (`:663–667`). That is Theorem 2.
- **Hypothesis check in the blueprint** (`:669–692`). `K` = completion of `Q_ℓ^ur` with `F` and `μ_ℓ` (and `μ₄` if `ℓ = 2`) adjoined: complete, discretely valued, characteristic 0, algebraically closed residue field. Correct. The character `χ^{−j}` has values in `Z_ℓ^× ⊂ K^×`; its image on `G_K` is a closed infinite subgroup of the principal units, hence `≅ Z_ℓ`; every finite layer is totally ramified. Correct, with `K₀ = K`. One wording slip: "still has infinite image because `j > 0`" (`:689`) — the reason is `j ≠ 0` and torsion-freeness of the principal units.
- **Integral consequence** (`:693–708`). `D x(s) = χ(s)^{−j}s(x) − x` is a continuous bijection `V → Z¹_cts(G_K, V)` of `Q_ℓ`-Banach spaces; the open mapping argument via Baire is given and is correct; hence `|x| ≤ ℓ^c sup_s |Dx(s)|`. For integral `x`, the Lean hypothesis `s x ≡ (χ_n(s).val)^j x mod ℓ^n` gives `|Dx(s)| ≤ ℓ^{−n}`, so `ℓ^c x ≡ 0 mod ℓ^n`. This matches the Lean statement (`IntegralTateInertiaCyclotomicTwistTorsionStatement.lean:7–11`): `∃ c, ∀ n x`, with `c` depending on `A, j, F` only.
- **Remarks.**
  - The Lean proof (`IntegralTateInertiaCyclotomicTwistTorsion.lean`, 610 lines) does not cite Tate; it proves the estimate directly. The blueprint's route is an alternative proof. The register says so ("discrete-base comparison and bounded inverse proved here"). Honest.
  - Two unproved standard steps: that a valuation subring `A ⊂ Q̄` with `v(ℓ) < 1` comes from an embedding `Q̄ → Q̄_ℓ` ("Embed Ω at A", `:669–670`), and that every `s ∈ G_K` restricts to an element of the inertia group `Ine A` fixing `F` (`:679–682`, stated with a one-line reason). Both are standard.
  - The Kato page and theorem numbers (12.5(1) p. 221, 12.6(2) p. 222, 13.5, 14.2(1)) I did **not** verify.

### C02 — `hilbert_ninety` (`ch_P_r7.tex:714–729`) — correct

Lean (`ExistsInvariantLift.lean:13–55`): `ρ : Γ → Aut_Ω(K)`, `Δ ≤ Γ` of finite index, `c : Γ → K` nowhere zero with `c(γγ') = ρ(γ)(c(γ'))·c(γ)` and `c(γ) = 1` whenever `γ` fixes every `Δ`-fixed element; conclusion `∃ y ≠ 0, c(γ)·ρ(γ)(y) = y`.

The hand proof takes `L` = `Δ`-fixed elements, `D` = pointwise stabilizer of `L`, proves independence of the distinct restrictions by the shortest-relation argument, sets `y = Σ_t c(t)t(x)` over `Γ/D`, and checks well-definedness and invariance. I verified: `c(gd)·(gd)(x) = c(g)·g(x)` for `d ∈ D`; `c(s)·s(y) = Σ c(st)(st)(x) = y`. One omission: finiteness of `Γ/D` needs `Δ ≤ D` (immediate); not stated.

### C01 — `exists_pres_smoothed` (`ch_P_r7.tex:598–648`) — correct where checked

Lean (`SmoothedPresOfShCoc.lean:197–224`): `m₀ = 0`, `c₀' = 0`; for every `m` and primitive `ζ` of order `ℓ^m` a finite family `(P_i, o_i)` with `HTPresNuOfPolys A cf m 0 (Y − d₀·Y(·d₀)) ζ P o`: coefficients of `P_i` in `A` and inertia-fixed, `P_i(ζ)` a unit, `o_i` integral, and Kummer exponents `k_i(s)` with `Z_m(s,1) ≡ Σ o_i k_i(s) mod ℓ^m` for `s` in inertia with `χ_m(s) = 1`.

Checked: the identity `z(s, d₀) = z(ρ⁻¹sρ, 1)` follows from the lower-coordinate cocycle law with multiplier one on inertia (I expanded `Z(ρ⁻¹sρ, 1)` and used `Z(ρ⁻¹ρ, 1) = 0`); the Kummer exponent of `v_i/ρv_i` is `a_i(s) − d₀a_i(ρ⁻¹sρ)`; `w_i = u_i/ρu_i` is `H`-fixed because `H` is normal in `I_A`; the basis argument with `v(ζ − 1) = 1/φ(M)` gives integral coefficients because the valuations `i/h + ℤ` are distinct and `0 ≤ i/h < 1`. The case split "all weights vanish / otherwise" matches the Lean `by_cases hcw`.

Remark: "the stipulated ordinary shape" (`:638`) is the Lean theorem `RhoAdm.rho_ordinary_shape`, a deduction from `Nf`, `SrcUr` and one field of `AdmWn`. It is used without name.

### C03 — `pDiv` (`ch_P_r7.tex:771–833`) — correct where checked

Lean (`SDiv`, `FixedIntegersIsUnitOfNotMemPrimeSpan.lean:112`; proof `DivEqZeroOfCg.lean:49–207`, with `pCob`, `pDivAlg`, `pGenEx`): for `ℓ ≠ 2`, an integral continuous system `Z` with vanishing specialization, there are `g`, `c₂` and an integral continuous `Z'` with `ℓ^{c₂}Z_m(s,x) = tr_g Z'_m(s,x) − φ(g)g^k Z'_m(s,x)` for `s ∈ I_A ∩ ker χ_m`.

Checked identities:
- `τS(xγ) − S(x) = (τ^N − 1)μ_r(x)` for `S(x) = Σ_{i<N} τ^i μ_r(xγ^i)`;
- `q = τS/(τ^N − 1)` satisfies `q(xγ) − θq(x) = μ_r(x)`;
- `|S(1)| ≤ a = |τ^N − 1|` from the three comparisons (pullback vs `τ^j`, `η_s` vs `τ^j`, moment `→ 0`), then `|S(x)| ≤ a` for all `x` by the recurrence;
- `θ^N ≠ 1`;
- the telescoping bound `|1 − θ^N|·‖q‖ ≤ ‖(T_g − θ)q‖`;
- `(β − 1)M_s = (η(s) − 1)M_t` from `M_{ts} = M_{st}` (commutator has trivial cyclotomic character), `β = (1+ℓ)^{−k} ≠ 1`;
- the corrected `μ_r(s) = ℓ^{c₂}Z_r(s) − w(δ_{χ_r(s)} − δ_1)` has moments tending to zero, and the Dirac terms cancel on `ker χ_r ∩ I_A`.

Compressed steps (not wrong): that `w(δ_{χ(s)} − δ_1)` is a coboundary for the translation action, so the corrected system still satisfies the cocycle law (the text says only "remains integral and push-compatible", `:824`); surjectivity of the cyclotomic character on inertia ("total ramification at each finite level and compactness", `:816–817`).

---

## The four Z4.2 partials

Question asked: is the stated remaining proposition really the only missing piece, and does it match a Lean declaration?

### Z4.2.02 — `joint_at_nonempty`

- **Remaining (A)** (`ch_P_r7.tex:152–159`): the twist-prime law `z'·F((g')⁻¹Wg, g⁻¹y₁)·ρ_S(det g)·ρ_T(det g') = z·F(W, y₂)` under `q^{−M}(y₁ − y₂) ∈ Λ`, `q^M y₂ ∈ Λ`, `ChIdx.Ok`, `QUnif`, a middle-level pair and a top-level pair, `P` outside the type-prime set.
- **Matches a Lean declaration: yes.** `GlobalTheory.TwTopLaw.topLawQ_midTop` (`TopLevelDatumTransformAtTwistPrimeUnderLevels.lean:108–253`). I compared hypotheses and conclusion with the Lean statement; they agree, including the direction of each action and both uniformizer conditions. The graph confirms the path `topLawQ_midTop → locq_twist → locAt → levAt_top → adLawAt_xiAd → joint_at_nonempty`.
- **(B) CurveEx** is a hypothesis of the Lean root itself, not a missing proof. Listing it as "remaining input" is defensible but should be worded as a premise.
- **Only missing piece: no.** The cone of `topLawQ_midTop` is 1,018 theorem lines. Outside the completed units (.01, .03, .05, .08) the root reaches 25,508 theorem lines; removing the `topLawQ_midTop` cone leaves 24,723, of which 22,550 are in theorems never named. The four paragraphs `ch_P_r7.tex:121–150` are sketches of `ratLaw_of_tie`, `sizeLaw_of_tie'`, `xiAd_intOff`, `levAt_mat`, `levAt_coupled` and the type-prime half of `levAt_top`. Examples of content covered by a clause: "On replacing … the determinant products by the pinned tame determinant characters" (`:137`) is `MuCharacterDetLevelEqLocalTameProduct` (401 lines); `PhiMapsAndOmegaLaw` (549), `IntegralHilbert90FiniteIdelesTrivialWhereTrivial` (327), `ExistsMoveRight` (241), `WeakApprox` (156) are never named.
- The v8 section (`ch_P.tex:13223–13230`) still lists three level identities as "A. Proved in Lean, not reproduced" and has no pointer to the v9 text.

### Z4.2.04 — `pairOK_allSites`

- **Remaining (A)** (`ch_P_r7.tex:110–118`): for the standard pair, `Taylor_α(U_x·B.thZero_{N,N'})(0) ∈ Q̄` for all `x ∈ sat(Λ₀)` and all `α`.
- **Matches a Lean declaration: not a standalone one.** It is the coefficient clause of the local `have h0` in `ta_thMoved` (`VacuumEntireAndNormalizedJetsAlgebraic.lean:311–316`), as the blueprint says. `h0` is supplied by `GlobalTheory.AlgTranslate.coefIn_translate` (`CoefInTranslate.lean:53–85`) applied to `thZero`, with `thZero_coefIn` (`…:236–258`) and `WeilVac.thZero_mem`. The remaining statement should name these three declarations.
- **Only missing piece: no.** Outside Z4.2.01, .03, .05 the root reaches 23,483 theorem lines; removing the cones of `coefIn_translate` and `thZero_coefIn` leaves 8,888, of which 8,374 are in theorems never named. Unlabelled one-sentence steps include: the period lattice is finitely generated and the kernel is a finite sum (`period_lattice_finitely_generated`, `level_structure_counting`; `ch_P.tex:13184`); `chi_detId_and_chiFac_alg` (the scalar and character fields used by Z4.2.06–.08); `la_le_sat` via `rational_points` and `klat_rat` ("their vectors are CM images of rational coordinate matrices", `ch_P_r7.tex:101`); `thZero_mem` (the standard vacuum lies in the theta space).

### Z4.2.09 — `site_law_xiIn`

- **Remaining (A)** (`ch_P_r7.tex:362–387`): finite split-place interpolation — one linear map on the span of the indicators `1_{Y_i}` sending each to `s_i·I·I·θ₀`.
- **Matches a Lean declaration: no, it is a paraphrase.** The Lean inputs are `model_at_split_places_holds : modelXi D` and `split_place_moves_compose : movesCompose D` (`HalvesRecursion/Outright.lean:8–12`), as consumed by `kerTh_relation_of_indicator`. The blueprint says its proposition is a restriction of what those two give ("Restricting the resulting map to this span suffices", `:380–381`). The remaining input should be stated as those two declarations, or the restriction should be proved equivalent.
- **Only missing piece: no — and this is the most serious bookkeeping error in the round.** `site_law_xiIn` begins with `obtain ⟨hδ, hLat, hVec, hEq⟩ := TieBase.base_data t` (`KernelSiteLawAndFixedCoordinateStabiliserLaw.lean`, first line of the proof) and passes `hLat, hVec, hEq` to both `kapLawLt_frecG` and `xiEx_theta_general`. The blueprint uses these as givens: "The two components of `B.EqP` give the moves" (`ch_P_r7.tex:390–391`); "Move identifies the kernels after the linear change of variables" (`:349–350`, which is `kerTh_move` and needs `EqP`, `VecP`, `LatAll`). `base_data` is a theorem, not a hypothesis of the unit. Sizes (theorem lines): root cone 77,934; cone of the declared proposition (A) 6,063; cone of `base_data` 51,268, of which 47,709 lie outside (A); remainder 24,162. So the declared remaining proposition accounts for under a tenth of the root's cone, and the largest undischarged input is not mentioned.
- `lev_pos_and_noConj` is also used and never named.

### Z4.2.12 — `site_cmpLite_siteAdm`

- **Remaining (A)** (`ch_P_r7.tex:516–532`): one site on the served standard structure satisfying Pair and admitting finite split-place interpolation.
- **Matches a Lean declaration: no.** It is the conjunction of `joint_at_nonempty` (Z4.2.02), `pairOK_allSites` (Z4.2.04) and the interpolation input of Z4.2.09. The text says so ("Its three source obligations are …", `:524–528`). Calling it "one exact remaining proposition" is a relabelling of three.
- **Only missing piece: no.** It inherits (i) everything listed above for .02, .04, .09, including `base_data`; (ii) the `kerTh_eq_pull` gap of Z4.2.10–.11, which the text now describes as "the two proved comparisons" (`:555`). Its own exclusive content is small (554 theorem lines outside the other eleven Z4.2 units, 457 never named): `kernelSite_seriesData_below_lastStep`, `tieStab_kaAtAny`, `series_reading_entries`, `series_compatibility_of`, `place_extends_to_iso`. Each gets one sentence. `place_extends_to_iso` is an uncited standard fact (see above).
- The v8 section (`ch_P.tex:13291`) still says "The unresolved … contraction in Z4.2.10–11".

---

## Trust ledger audit

### Numbers: `trust_tables.tex` vs `status.json`

| Quantity | `trust_tables.tex` | `status.json` / recomputed | Agree |
|---|---|---|---|
| Complete / partial / structure only | 30 / 15 / 9 | 30 / 15 / 9 (count of `units[*].status`) | yes |
| Open assignments | 24 | 15 + 9 | yes |
| Rows in the open tables | 24 | — | yes (N076, N318, Z1.1.01–.03, .05–.07, Z1.2, Z1.3.01–.05, .08, Z1.5.03–.05, Z4.2.02, .04, .09, .12, Z4.3, Z4.4) |
| Original inputs complete / open | 13 / 7 | 13 rows "complete", 7 "partial" in `TrustRecursiveRows` | yes |
| Exclusive lines by status | 166,682 / 772,858 / 43,030 | recomputed from the graph: identical | yes |
| Unique to open | 815,888 | 772,858 + 43,030 | yes |
| Open union, open only, overlap, closed only | 2,217,882; 2,024,679; 193,203; 182,655 | recomputed: identical | yes |
| Unit union, outside, scope | 2,400,537; 7,166,508; 9,567,045 | `graph.expert`; recomputed: identical | yes |
| Literature boundary | 2,653 declarations, 13,470 lines, 1,860 theorems | `graph.expert.universe`, `literature_boundary_kinds` (1,860 + 741 + 27 + 24 + 1 = 2,653) | yes |
| Boundary reached from experts | 987 | `graph.expert.union[2]` | yes |
| Parents union | 1,604,500 | `graph.recursive.union[1]` | yes |
| Cross-register union / shared / literature | 6,324,998; 2,658,315; 1,559 | `omission_union.union`, `.shared` | yes |
| Audit: headlines, modules, axioms, sign-offs | 5; 175,187; 3; 0 | `audit` | yes |
| Omission summary | 432,244; 1,461,602; 1,893,846 | `omission_graph` (1,893,846 − 1,461,602 = 432,244) | yes |

The recomputation used the same rule as `ch_trust.tex:177–183` (follow type and value edges from each root, stop at the literature boundary, weight `b − a + 1`) on the graph cache behind `graphq.py`. Every per-unit `exclusive_lines` value in `status.json` was reproduced.

The sources are internally consistent. The statuses they count are another matter: if Z4.2.10 and Z4.2.11 revert to partial, the headline becomes 28 / 17 / 9 with 26 open. The line partition would hardly move, because both cones lie inside the cone of the open unit Z4.2.12.

### Wording in `ch_trust.tex`

- **Disclaimer: present.** `ch_trust.tex:4–7`: "AI-written draft awaiting human review. This report does not claim a proof of the Riemann hypothesis." The PDF has it on the title page and at the head of the ledger.
- **Formal certificate: attributed, not overstated.** Lines 12–15 and 92–117 attribute every machine check to an external audit and say that the local axiom transcript "stops at the missing object" and that two checks "were still running at that timestamp". That is honest about what the project itself did. I could not verify the external audit's figures (5; 175,187; three axioms; kernels and comparators); a web search did not find the audit pages. They should be read as reported, not confirmed.
- **Literature: not overstated in the ledger.** `\TrustBibliographySummary` counts works and says they include "background and failed comparisons". The phrase "verified publication clauses" (`:172–173`) refers to the Kato register, where exactly one clause (A01) is closed by a publication; that one I confirmed above.
- **Misleading or unclear sentences.**
  1. `ch_trust.tex:33–34`: "The number of signed nodes in this project's backward dependency map is 0." This is opaque. The PDF has the clear sentence "The number of human sign-offs is 0." The clear sentence should be restored; `status.json` calls the field `human_signoffs`.
  2. `ch_trust.tex:28–29`: "*Complete* records an argument under its specified premises." For Z4.2.10 and Z4.2.11 the argument uses a Lean theorem that is neither a premise nor reproduced (see above). For Z4.2.06, .07, .08 the premises include fields of a site whose existence is open. The definition is fine; its application to .10 and .11 is not.
  3. `ch_trust.tex:211–212`: "Completed units can rely on explicit premises assigned to an open row." True and important, but nowhere does the ledger list which completed units do so. A two-line list (Z4.2.06, .07, .08, .10, .11 rely on Z4.2.02, .04, .09) would prevent misreading of "30 complete".
  4. Open-unit rows for Z4.2.02, .04, .09, .12 begin "A: …" as if (A) were the whole remaining input. As shown above it is not, most clearly for Z4.2.09.
  5. `ch_trust.tex:205–206`: "It includes intermediate arguments already reconstructed in a partial proof." Fair, but for the Z4.2 partials the reader has no way to tell how much is reconstructed; the proxy figures above suggest most of each cone is not.

### PDF vs current sources

`pdfinfo` gives creation time Mon Nov 23 10:05:53 2026 CST. File times in `prev7/` are all copy times, so I compared content.

| Place | PDF (`blueprint_v9.pdf`) | Current source | Agree |
|---|---|---|---|
| Ledger p. i, sign-off sentence | "The number of human sign-offs is 0" | "The number of signed nodes in this project's backward dependency map is 0" (`ch_trust.tex:33`) | **no** |
| Ledger p. xiii, omission cones | 399,083 in exactly one cone; 1,460,766 in several; union 1,859,849 | 432,244; 1,461,602; 1,893,846 (`omission_summary.tex`) | **no** |
| Ledger p. xiii, cross-register union | 6,324,971; shared 2,625,071 | 6,324,998; 2,658,315 (`trust_tables.tex`) | **no** |
| Ledger p. xiii, sentence "For the two open literature comparisons the measured roots are the project interfaces …" | absent | present (`omission_summary.tex`) | **no** |
| 30 / 15 / 9, 24, 13 / 7 | same | same | yes |
| All other `\Trust…` macros (22 values) | same | same | yes |
| 24 open-unit rows (title, remaining input, basis) | same text | same text | yes (whitespace-insensitive match of all 72 fields) |
| 20 recursive rows | same | same | yes |
| Unit directory statuses (54 units) | same as `status.json` | — | yes |
| `ch_P_r7.tex` prose | 131 of 134 plain sentences found verbatim; the other three are extraction artefacts at page breaks or formulas | — | yes |

So the PDF predates the last regeneration of `trust_tables.tex`, `omission_summary.tex` and one edit of `ch_trust.tex`. The differences are confined to the trust ledger: one sentence reworded, one sentence added, five numbers changed. The PDF must be rebuilt before circulation.

### Other stale text

- `ch_P.tex:13199`, `13242`, `13275`, `13282`: v8 "A. Proved in Lean, not reproduced" paragraphs for units now marked complete. The headers carry "(v8)" and a forward pointer.
- `ch_P.tex:13181`, `13223`, `13255`, `13285`: v8 sections for Z4.2.04, .02, .09, .12 have **no** forward pointer, and their "A" statements differ from the v9 remaining statements.
- `ch_P.tex:11685–11703`: the map items for Z4.2.06, .07, .10, .11 still end with open-obligation sentences ("must also hold here", "is a separate obligation", "must produce the norm-one constant"). Same kind of stale sentence as R6 found at `11646` and `11691`.

---

## Recurring issues from earlier rounds

| Issue (first raised) | Round 7 state |
|---|---|
| No bracketed "[Hypothesis, discharged at …]" label (R6) | Still absent in all four new units. Prose discharge given for .07, .10, .11; none in the unit text for .06 |
| No "[Proved in Lean, not reproduced: …]" label on sketched steps (R5, R6) | Still absent. `ch_P_r7.tex:32–564` contains no such label at all |
| "Complete" resting on steps asserted without proof (R5: Z4.4, Z1.2) | Recurs for Z4.2.10, Z4.2.11 |
| Dependence on a partial unit understated (R6: Z4.2.08 on Z4.2.04) | Stated accurately for .06 and .07; not flagged for .10, .11 (Pair and Law come from open units) |
| Site-record fields used as givens (R6) | Unchanged |
| Pass-through discharge sites (R6) | Not repeated: `admissible_at_each_site` is the real site. The `GlobalTheory.T.*` wrappers in between are pass-throughs and are correctly not cited |
| Stale sentences in `ch_P.tex` (R6) | More of them (listed above) |

---

## Verdict summary

- **Z4.2.06 — COMPLETE WITH GAPS.** Statement matches. The v9 eigenvalue and scalar computations are correct and follow Lean. Gaps: no bracketed labels; existence of the move is still a sketch over unnamed lemmas (`isPt_move_eq`, `chi_detId_smulLat` and others, about 700 theorem lines); `cΞ ∈ Q̄` not stated; one stale paragraph.
- **Z4.2.07 — COMPLETE WITH GAPS.** Statement matches. The descent of both units to the coefficient field is correct where checked, and the scalar identity is right. Gaps: no bracketed labels; equality of off-prime lattices and of the finite data is asserted over unnamed Lean lemmas; `KIn` source not stated; one stale paragraph.
- **Z4.2.10 and Z4.2.11 — NOT COMPLETE.** The central coefficient identity is correct, but the site-series formula depends on `kerTh_eq_pull` and through it on `TieBase.base_data` (51k theorem lines), which are neither hypotheses nor reproduced nor labelled, and appear nowhere in the document. Four further inputs (`cKs_unit_indep`, `unit_mul_scal_eq_scT`, `moved_forms_at_source`, `transported_frame_realAt`) are asserted. Both should be partial.
- **Z1.3.** The Tate citation is real (§3.3, Theorem 2, p. 176) and its hypotheses are checked correctly in the blueprint; the work is missing from the bibliography. The three hand proofs C01–C03 are correct where checked. The 1 + 9 + 3 count is consistent. Kato page references were not verified.
- **Four partials.** Only Z4.2.02's remaining statement is a Lean declaration (`topLawQ_midTop`). In none of the four is the stated proposition the only missing piece. For Z4.2.09 the largest missing input, `TieBase.base_data`, is not listed at all.
- **Trust ledger.** The numbers in `trust_tables.tex` agree with `status.json` and with an independent recomputation. The disclaimer is present and the formal certificate is attributed rather than claimed. The sign-off sentence should be restored to the PDF's wording, and the ledger should list which completed units rely on open ones. With the verdicts above the honest headline is 28 complete / 17 partial / 9 structure only.
- **PDF.** `blueprint_v9.pdf` does not match the current sources in the trust ledger (one reworded sentence, one missing sentence, five numbers). Rebuild before use.
