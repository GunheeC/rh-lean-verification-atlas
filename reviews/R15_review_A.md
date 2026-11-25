AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

# R15_review_A

AI review report produced during this project; file names are internal working names.

- Internal source file: `out/R15_review_A.md`
- SHA-256: `5b787a5d05d1e8388d5a01f8a2d426eec614cd95e91b37523d9006cac6b16d6f`
- Report scope: R15 review A — Z4.2.04 completion candidate (`GlobalTheory.pairOK_allSites`)

## Internal report

The report below preserves its original verdict, scope and unresolved points. Source line numbers in other records count from its original title.

# R15 review A — Z4.2.04 completion candidate (`GlobalTheory.pairOK_allSites`)

Reviewed: `ch_P_r15.tex` lines 1–540 against the Lean source at commit `40e56bab…` (original numbering, `git show`), the register `R15_pending.json` (26 Z4.2.04 rows and the unit candidate), `status.json`, the revised `ch_P_r14.tex` (Z4.2.04 text at 1112–1331), the two R14 reviews, and the earlier translate texts `prev7/ch_P_r7.tex:97–127` and `prev8/ch_P_r8_frames.tex:53–144`. Cone figures come from `graph_cache.bin` (the data behind `graphq.py`); a line count is the sum of inclusive ranges of distinct core declarations with a valid range.

Nothing here claims or implies that RH or GRH is proved. The review only compares hand proofs and bookkeeping with the Lean declarations they label.

## 1. Verdicts

| Item | Verdict |
|---|---|
| 26 registered sub-declarations | **26 CONFIRMED** (statement and proof), 0 with gaps, 0 not confirmed. Labelling and citation slips are listed in §2.6; none affects a proof. |
| Unit candidate `pairOK_allSites` (assembly) | **CONFIRMED WITH GAPS**: the assembly is correct field by field, but one supplier (`translate_entire_algebraic`) rests on inputs that are not hand-proved. |
| `translate_entire_algebraic` (task 2) | **CONFIRMED WITH GAPS**: the hand argument is sound as far as it goes, but it starts from two inputs the text itself leaves open, and it has no single location. |
| Z4.2.04 unit | **DO NOT APPROVE** as an unconditional completion. Reasons and sizes in §5. |

Review B's four fixes:

| Fix | Status |
|---|---|
| F1 (`r14:lat` verdict for `Base.latAll`, first clause) | Closed. Review A row 1 confirmed `Base.latAll`; `ch_P_r14.tex:1154–1156` now cites it. |
| F2 (hand proofs of the two site lemmas) | Closed by `r15:site` and `r15:span`; confirmed below. |
| F3 (generic integrality step) | Closed. `ch_P_r14.tex:1171–1180`: `exp(πi q(x)) = ±1`, squaring gives `q(x) ∈ ℤ`. |
| F4 (Osgood) | Closed. `ch_P_r14.tex:1282–1286` names Osgood's lemma and `analyticOnNhd_of_differentiable_vc`; entireness of `e` is stated at 1276–1281. |

So everything review B asked for is done. What blocks approval is the item B explicitly did not audit: the translated-coefficient input.

## 2. The 26 declarations

All 26 rows of `R15_pending.json` reproduce: name, file, line range and inclusive cone size agree with the graph and with the pinned source.

### 2.1 Recovering the lattice and its adelic span (`r15:site-glob`)

| # | Declaration (Lean lines) | Statement | Proof | Verdict |
|---|---|---|---|---|
| 1 | `Comp.glob_one` (`EqGlobOfHat.lean:39–40`) | match: `IsLat Λ → globLat 1 Λ = Λ` | correct | CONFIRMED |
| 2 | `Comp.mem_hat_glob` (42–44) | match: `u ∈ hat(globLat g Λ) ↔ g⁻¹u ∈ hat Λ` | correct | CONFIRMED |

Checked against `csGlob_one` (`CsGlob.lean:175–241`), `csGlob_N_fg`, `csGlob_int` (52–101), `csSpan_approx`, `csSpan_fwd`, `csSpan_back` (`CsSpan.lean:21–150`).

- `E ∩ S = O_E`. The text takes the trace of `xb`, uses integrality of the trace on `S`, embeds `E ∩ S` in the `O_F`-span of a scaled trace-dual basis, and applies the determinant trick. This is `adelstab_tr_mem`, `adelstab_dual`, `csGlob_N_fg`, `csGlob_int` step for step. "Contains 1 and is stable under multiplication by `x`" is exactly what `isIntegral_of_smul_mem_submodule` needs.
- Congruence modulo `dS`. Lean has two versions (`csGlob_approx` by a ℤ-basis of `O_E`, `csSpan_approx` by closure induction). The text's "generators, hence `S`" is the second; it is valid because `dS` is an ideal of `S`.
- `G_1(M) = M`. I recomputed: `x = Σ s_k m_k`, `s_k ≡ b_k (mod bc₀S)`, `y = Σ b_k m_k ∈ M`, `x − y ∈ bc₀ Σ S m_k ⊆ bSⁿ` because `c₀m_k ∈ O_Eⁿ`; then `E ∩ S = O_E` gives `x − y ∈ bO_Eⁿ ⊆ M`. Lean runs the same computation as a span induction with `c₁ = m`, `c₂`.
- Span recovery. The bounds `bdSⁿ ⊆ gM̂ ⊆ (dc₀)⁻¹Sⁿ` are right (`d` clears `g` and `g⁻¹`). The decomposition `z = x + Σ w_k·(bd e_k)` is `csSpan_back` with `α = dc₂`, `β = c₁d`. The reverse inclusion is `csSpan_fwd`.
- `latAd = globLat` is `Submodule.span_eq` (`SDCompan.latAd_eq`), as the text says.

Asserted in one clause, standard, no argument: a common denominator `d ∈ O_F` for the entries of `g` and `g⁻¹` (`levelaf_exists_denom`, via `levelaf_denom`).

### 2.2 Dual and companion (`r15:site-dual`)

| # | Declaration | Statement | Proof | Verdict |
|---|---|---|---|---|
| 3 | `isLat_dl_of_isOrthCo` (`IsLatDlOfIsOrthCo.lean:139–141`) | match | correct | CONFIRMED |
| 4 | `Comp.glob_dl` (`EqGlobOfHat.lean:197–205`) | match | correct | CONFIRMED |
| 5 | `Comp.glob_companion` (`ExistsUnitaryOneDetEq.lean:18–23`) | match (`a ≠ 0`) | correct | CONFIRMED |

- Row 3 (`OrthDual.isLat_dl`, 55–135). With `v_r = c⁻¹e_r` and `n_r v_r ∈ M`: `h_J(n_r v_r, z) = n_r (cz)_r`, so `M^# ⊆ Σ O_E·v_r/n_r`. With `m` clearing the `c`-coordinates of generators: `h_J(x, m v_r) = σ((cx)_r)·m ∈ O_E`. Both computations match Lean (`hle`, `hmem`). The case `n = 0` is covered.
- Row 4. Forward inclusion is `glob_dl_le`: pairing in `S` by `hform_hat` / `csDual_span`, the involution preserves `S` (`csDual_sig_mem`), unitarity of `g⁻¹`, then `E ∩ S = O_E`. Lean gets the last step from `glob_one` on a rank-one lattice; the text uses the scalar fact directly. Same content. The reverse inclusion needs `IsLat(dl(G_gΛ))` for inverse transport; the text says so ("valid for the full dual lattice just proved"), Lean passes `hJ`.
- Row 5. `glob_sup` is the order-isomorphism argument; `glob_smul` in the text is direct (divide by `a`, which is a unit of `E ⊗ 𝔸`, and use `hat(aM) = a·hat(M)`); Lean proves one inclusion and inverts. Both are correct. The case `a = 0` is handled separately in the text and in `isSD_core`.

### 2.3 From the identity chart to the kernel lattice (`r15:site-standard`)

| # | Declaration | Statement | Proof | Verdict |
|---|---|---|---|---|
| 6 | `OrthSelfDual.isLat_and_dl_eq_of_isSDLat_mvL` (`IsLatAndDlEqOfIsSDLatMvL.lean:28–71`) | match | correct | CONFIRMED |
| 7 | `SDCompan.isSD_toStd` (`IsSDLatLatK.lean:44–70`) | match | correct | CONFIRMED |
| 8 | `SDCompan.isSDLat_latK` (98–100) | match, incl. `a = 0` | correct | CONFIRMED |
| 9 | `KerSelfDual.isSDLat_latK_of_stdL` (`IsSDLatLatKOfStdL.lean:19–34`) | match | correct | CONFIRMED |
| 10 | `KerSiteSelfDual.even_and_isSDLat_kerN` (`KernelLatticeSelfDualEvenRankAtSite.lean:22–27`) | match | correct | CONFIRMED |

- Row 9 is the first site lemma review B asked for (residual 1,508 / 1,417). Lean: `isOrthCo_toLE_of_cT_mul_self`, `isLat_dl_of_isOrthCo`, `glob_one` to turn `latCo(c,a,1,L_b)` into `c·C_a(L_b)`, `stdL_isSD`, row 6, row 8. The text has the same six steps in the same order (155–171). The displayed statement (22–29) has the hypotheses `c^*c = J` and `latCo(c,a,1,L_b) = O_Eⁿ`, every unitary adelic `g`, and the three fields of `IsSDLat`.
- `latK = toStd(compan(latAd))` and `stdCo = Classical.epsilon (IsOrthCo σ J)`: the text's "chosen using the existence witnessed by `c`" is `Classical.epsilon_spec hco` in `isSD_toStd`.
- Row 10. `Dict` gives the rank equality and the `HEq` with `latK`; `J.pins.crd_orth` and `J.base` discharge the two hypotheses of row 9; `N_even` is `k_even.add (t_odd.add_one.mul_left j)`. All in the text (179–188). Both hypotheses are fields of `Joint`, so they are pass-throughs at this root.

### 2.4 Local span (`r15:span-place`, `r15:span-frame`, `r15:span-steps`)

| # | Declaration | Statement | Proof | Verdict |
|---|---|---|---|---|
| 11 | `ph_tensInt_onto` (`TensorFirstFactorIntegersOntoLocalIntegers.lean:14–49`) | match | correct | CONFIRMED |
| 12 | `locSp_eq_image` (`LocSpEqImage.lean:16–66`) | match | correct | CONFIRMED |
| 13 | `LocCarry.mem_latS_latAd_iff` (`MemLatSLatAdIff.lean:37–72`) | match | correct | CONFIRMED |
| 14 | `latAdLoc_of` (`LatAdLocOf.lean:17–60`) | match | correct | CONFIRMED |
| 15 | `smul_dualSet_latAd_mem` (`SmulDualSetLatAdMem.lean:17–55`) | match | correct | CONFIRMED |
| 16 | `CompSp.locSp_compan_eq` (`LocSpCompanEq.lean:17–59`) | match | correct | CONFIRMED |
| 17 | `FacQPt.facQ_isPt` (`FacQIsPt.lean:19–33`) | match | correct | CONFIRMED |
| 18 | `SpanPt.locSp_latAd_isPt` (`LocSpLatAdIsPt.lean:25–29`) | match | correct | CONFIRMED |
| 19 | `KerSp.locSp_latK_isPt` (`KernelLatticeFirstFactorLatticeTuplePoint.lean:21–30`) | match | correct | CONFIRMED |
| 20 | `Joint.basesAt_span` (`LatticeTupleBasesSpanAtPlaces.lean:10–16`) | match | correct | CONFIRMED |
| 21 | `locSp_reindex` (`ColSpanMapMulVecLin.lean:21–26`) | match | correct | CONFIRMED |
| 22 | `Joint.locSp_kerN_zero` (`FrameLocalLatticeSpanKernelLatticeZero.lean:19–34`) | match | correct | CONFIRMED |
| 23 | `Joint.locSp_kerN_succ` (`FrameLocalLatticeSpanKernelLatticeSucc.lean:18–54`) | match | correct | CONFIRMED |

- Row 19 is the second site lemma (residual 1,885 / 1,753). Lean: `smul_dualSet_latAd_mem`, `latAdLoc_of`, then `locSp_map`, `locSp_compan_eq`, `locSp_latAd_isPt`, `colSpan_map`. The text follows this chain (285–309). The displayed formula `span ρ_v(latK) = colSpan(ρ_v(CB)·g_v)` is the Lean right-hand side `((toMatrix'(stdCo) * A.B).map (A.iw v)) * castGL A.rk (g v)`. Hypotheses match: an orthogonal coordinate exists, `SplAlg`, `LocInt`, `LbAtB`, `0 < T`, `IsPt`, `T` a unit of `W_v`; the level supplies `Lb_fin`, `Lb_span`, `Lb_dual`.
- Row 11. Integral image of `a ⊗ 1` by its monic equation and integral closedness; `1 ⊗ z ↦ z` by `SplAlg`. As in the text (265–271).
- Row 13. Both directions are present: extend by zero (`IE_latS`), apply the global span identity (row 2 with `integral_adele_approximation_holds`), project (`prV_latS`). The paragraph at 250–258 is correct but hard to follow, because it announces "the reverse inclusion" and then gives both.
- Row 15. `T L_b^# ⊆ L_b` transports to `T M^# ⊆ M` by `glob_dl`, `smul_glob_le`, `glob_mono`. Correct; needs `T > 0` so that `a = T ≠ 0`.
- Row 16. `M ⊆ M_a`, `T·M_a ⊆ M`, `T` a unit in `W_v`. Correct for every `a`.
- Rows 17–18. `f_v(x_v) = B_v g_v B_v⁻¹` from the place clause of `IsPt`; then `B_v g_v B_v⁻¹·colSpan(B_v) = colSpan(B_v g_v)`.
- Rows 22–23. I read both Lean proofs against 319–367: `Dict` for the lattice `HEq`; `J.lev0` or `chart_succ_eq` (`hTT`, `hLb`) for level and base lattice; coprimality from `gidx_facts`, hence `0 < T` and `T` a unit in the local ring (`natCast_isUnit_localRing`); `crd_orth`; the chart hypotheses `J.alg0, J.one.int, J.lb0` and `J.alg, H.core.int, J.lbB`; the point from `isPt_pt_zero` / `pt_succ_isPt`; `basesAt_span`; `locSp_reindex`; in the successor case the valid branch of `chAt` and `J.iw`. All are named in the text.
- Row 20 has zero residual lines: it lies wholly inside the Z4.2.03 cone. Its one external input, `Pend.latAt_isLattice`, is described but not named.

### 2.5 Moved datum (`r15:datum`)

| # | Declaration | Statement | Proof | Verdict |
|---|---|---|---|---|
| 24 | `moved_pair_datum_eq_adelic_datum_alt` (`MovedPairDatumEqAdelicDatum.lean:21–24`) | match | correct | CONFIRMED |
| 25 | `datLoc_homRe` (`DatLocHomRe.lean:14–23`) | match | correct | CONFIRMED |
| 26 | `xiM_datLoc` (`MovedPairDatumDependsOnlyOnLevel.lean:13–28`) | match | correct | CONFIRMED |

`xiM = movD(Ξ₀, trG_j, trG_{j+1})` applies `inFr g g'`; `xi0` applies `inFr g.symm g'.symm` on its positive branch; they cancel (`inFr_symm_inFr_cancel`). `DatLoc` then comes from `S.law.loc` after substituting the two rank equalities and the two `HEq`s. The text (371–388) says exactly this, including `homRe(refl, refl, z) = z`.

### 2.6 Labelling and citation slips (all minor)

1. `ch_P_r15.tex:439–440`: `thetaTranslate_canonicalOddTheta_of_half_mem` is at `GaloisConjTaylorThetaTranslate.lean:42–49`. Lines 51–75 hold `thetaTranslate_natCast_mul` and `thetaTranslate_zero_at_shifted_point`. Cite 42–64 and name the dilation lemma.
2. Line 104: `levelaf_exists_denom` is `Levelaf.lean:423–442`, not 423–430.
3. Line 261: `IE_latS` ends at `PNeatB.lean:72`; the cited range stops at 71.
4. Line 185: `N_even` has no path (`ProductZerothFirstParts.lean:303–305`).
5. Line 362: `lattice_tuple_chart_succ_eq_component_chart` is the wrapper in `…Statement.lean:9–10`; the declaration at the cited `…ComponentChart.lean:22–27` is `chart_succ_eq`.
6. The root calls `T.*` wrappers (`kernelLattice_selfDual_even_rank_at_site`, `frame_localLattice_span_kernelLattice_zero/_succ`, `movedPairDatum_congr`, `kernelLatticeFirstFactor_latticeTuplePoint`, `lattice_tuple_bases_span_at_places`). The chapter uses the implementation names only. One sentence mapping wrappers to implementations would let a reader match `KernelSiteLatticeTuplePairsAdmissible.lean:29–45`.
7. Name `Pend.latAt_isLattice` at 321–324 and `bwB_gramN_det` (determinant of a unitary adelic point has norm one because `det J ≠ 0`) where `scal0` is discussed.
8. Standard facts used by name without a reference: Chinese remainder theorem and approximation in a Dedekind domain; an element of `F` with all finite valuations `≤ 1` is integral; nondegeneracy of the trace form; the determinant trick; integral closedness of a discrete valuation ring; existence of a common denominator for finitely many finite adeles. These are textbook algebra; one citation (for example Neukirch or Cassels–Fröhlich) would cover them.
9. `gidx_facts` (`GidxFacts.lean:16–24`) is cited for coprimality only. Its other conjuncts pull `Served.served_facts` into the cone (99 lines reachable only this way). The hand proof needs only the projection `¬ p ∣ T`, which is a field of `GIdx`. Say so, so that the 99 lines are accounted for as unused.

## 3. Proof-level review of `translate_entire_algebraic`

### 3.1 Where the hand proof is

Lean (`TranslateEntireAlgebraic.lean:15–18`): for a curve ideal, a discriminant root, `IsChi χ`, an admitted pair and a shift `s` with `m·s ∈ La`, `U_s(B.eNat χ)` is entire and has normalized Taylor coefficients in `Q̄`. Entireness is `vector_bound_link … .1` with `IO.U_diff`; the coefficients are `ThLoc.algTAll` = `ThLoc.Alg.algTAll` (`AlgTAll.lean:12–26`), which is `ta_thMoved`, `TA.comb`, `chiFac_mem`, `sat_of_nsmul`, `la_le_sat`.

There is no single hand proof. `r15:translated` (396–485) is a three-item digest that points to:

| Step | Text | Lean it tracks |
|---|---|---|
| Genus-one germ and torsion translates | `ch_P_r8_frames.tex:56–101` | `galSg_all`, `divQuot_rec`, `coef_translate_mem`, `algebraicTaylor_torsionTranslate_evenTheta_alt` |
| Four copies with one torsion shift | `ch_P_r8_frames.tex:103–118` | no Lean counterpart; Lean uses `thetaVector_fourthPower_algebraicGerm` (unshifted) and then `AlgTranslate.coefIn_translate` |
| Saturation of period lattices | `ch_P_r8_frames.tex:120` | `la_le_sat`, `klat_rat`, `rational_points` |
| Translations and intertwiners | `ch_P_r7.tex:97–104` | `TA.transl`, `TA.iop`, `ta_thMoved` |
| Character factor | `ch_P_r8_frames.tex:122–126` | `chiFac_mem`, `relative_determinant_norm_one` |
| Self-duality, integrality of `E_H` | `r14:lat` | `Base.latAll` (confirmed, R14 review A) |

No earlier review checked this argument: R8 did not sample it, R14 review A called `algTAll` "sketch", R14 review B left it out of scope. This section is its first proof-level reading.

### 3.2 What I checked

I recomputed each step from the Lean definitions (`U1`/`opU`, `sgStar_laws`, `IsThM`, `kernel4`, `StdData`, `thZero`, `thMoved`, `eNat`, `chiFac`, `TA`).

- **Germ of `f = sgStar(Λ)`.** `(log f)'' = −(℘ + s)`; coefficientwise conjugation gives `f^σ = f·exp(cz²)` with `2c = s − σ(s)` (constant term by `f'(0) = 1`, linear term by oddness). `f(αz)²/f(z)^{2d}` is elliptic because `|α|² = d` makes the two multipliers equal; it is even with poles only on `Λ`, hence a polynomial in `℘`. Conjugating gives `exp(2c(α² − d)z²) = P^σ(℘)/P(℘)`, so the left side is elliptic and entire, hence constant; `α² = −d ≠ d` gives `c = 0`. Correct.
- **Recurrence.** `Ψ_{l+1}Ψ_{l−1}/Ψ_l² = ℘(v) − ℘(lv) = l⁻²(log Ψ_l)''`, which is `(n+1)²Ψ_nΨ_{n+2} = Wr(Ψ_{n+1})`. The modification of `σ` by `exp(−sz²/2)` cancels in both identities. `Ψ_2 = −℘'(z+u)`. Correct; division is in the Laurent field, so a zero value at `0` is harmless.
- **Power identity.** From `U_uf(z) = f(z+u)·exp(−πH(z,u) − πH(u,u)/2)`: `(U_uf)^{h²}·Ψ_h = U_{hu}f(hz)`, and `U_{hu}f = f` because `hu/2 = mu ∈ Λ` (sign clause of `sgStar_laws`). Then `c_0^{h²} ∈ Q̄`, `c_0 = f(u)·(unit) ≠ 0`, and the degree-`j` coefficient of `v^{h²}` is `h²c_0^{h²−1}c_j` plus earlier terms. Correct.
- **Four copies.** With `θ^{⊗4} = κ·K` and `K(z) = (J F_0)(γz)`: translation by `(a,a,a,a)` gives `⊗⁴U_aθ` on the left (orthogonal sum) and `(U_{γ𝐚}J F_0)(γz)` on the right (`γ` an isometry). Each term is a root of unity times a product of genus-one translates at points of `Λ_ℚ`, composed with the algebraic matrix `γ`. The coefficient at `(β,β,β,β)` is `([z^β]U_aθ)⁴`. Then `thZero` is a product over matrix entries in disjoint variables. Correct, given the inputs in §3.3.
- **Moving the pair.** `U_xU_t = (root of unity)·U_{x+t}` on the saturation uses integrality of `E_H` on the standard period lattice (from `LatAll`). `Iop` is a finite sum with coefficients `±[A₂ : A₁∩A₂]^{−1/2}`, or zero at index zero. `chiFac ∈ Q̄` by `I_L·Ī_L = 1` (argument confirmed in the R8 review). Correct.
- **Entireness.** `thMM` entire (first clause of `IsThM`), products, translates, finite sums. Correct, given §3.3.

### 3.3 Why it is not complete

**(a) Two inputs are left open by the text itself.** `thMM` is `Classical.epsilon (IsThM …)` (`LateralTheory.lean:28–29, 155`). Unless a witness exists, `thMM` is an arbitrary function: it need not be entire and need not satisfy `θ^{⊗4} = κ·K`. Everything in §3.2 from "four copies" onward starts from

- `Ker.kThetaVector` through `thM_spec` / `isThM_ne_zero` (`IsAdmissibleFlagPairOfUnitriangularLeftAutomorph.lean:27–29, 75–81`): existence of the fourth-root theta vector, and
- `B.StdOK` through `FourthRootStd.stdOK` (`SpanRangeEmb4EqTop.lean:700–701`) and `SO.stdOK` (`PStdOK.lean:338–339`): isometry `g_C`, half-period, semicharacter identities, self-duality of the image lattice, two nonzero indices, and the inclusion `N·γ(L_M⁴) ⊆` standard lattice (`FourthRootStd.up`).

The chapter says this in so many words: "The inputs to the comparison are the stated fourfold theta identity and the standard isometry; their proof locations are recorded under the R15 supplier names for Z4.2.13" (455–457). The supplier table classifies them R with "The fourth-root existence theorem is an inherited input" and "Each of these lattice identities remains an input at this boundary" (573–576). `ch_P_r14.tex:316–327` adds "Z4.3 is partial, and review A treated this as a supplier". The only hand text is the round-4 paragraphs `par:r4-z43-iso` and `par:r4-z43-host-standard`; no review on record covers them, and `status.json` registers neither declaration.

**(b) The hand route is not the Lean route, and this is stated only at the end.** Lean proves the unshifted jets of `thZero` and transports them by `coefIn_translate` (class N, 10,889 theorem lines inclusive). The hand proof translates the four copies directly and never uses `coefIn_translate`. That is a legitimate proof of the same statement. But item 2 of `r15:translated` cites `thetaVector_fourthPower_algebraicGerm` and `thZero_coefIn` (unshifted in Lean) as if they carried the shift. The disclaimer is at 478–482; it should stand at the head of item 2. In genus one the same holds on a smaller scale: Lean's `coef_translate_mem` uses Galois conjugation of translates (`galois_conj_taylor_thetaTranslate`, `lamConj_eq_self`, `admJ_and_torsion_data_algebraic`); the hand proof uses the recurrence directly.

**(c) Uncited standard theory inside the cone.**

- Weierstrass `σ`, `ζ`, `℘`: existence of the Hermitian-normalized `σ` with its multiplier law, zeros exactly on `Λ`, the addition formula `σ(a+b)σ(a−b) = σ(a)²σ(b)²(℘(b) − ℘(a))`, and "an even elliptic function with poles only on `Λ` is a polynomial in `℘`". About 3,650 lines of the translate cone are analytic support for these. No reference is given in `r15:translated` or in the round-8 text.
- Algebraicity of `℘(u), ℘'(u)` at torsion points: stated with a one-line Galois-orbit argument, which presupposes the uniformization `ℂ/Λ ≅ E(ℂ)` as a group isomorphism. Cite it.
- Integrality of the CM `j`-invariant: cited as "Milne, Corollary 12.16" in round 8. In Lean this is a proved theorem (`integral_j_and_algebraic_data`, class N, 2,225 theorem lines, about 560 lines of `q`-expansion support), not a literature leaf. The citation is acceptable as a published comparison, but it should be recorded as such in the ledger, and I did not verify the numbering.
- `Δ(Λ) ≠ 0` (about 500 lines of elliptic identities under `discrNe`, outside the translate cone but inside `kerTh_entire_algCoef`).

**(d) Small asserted steps.** `Base.lat0OK` (the period lattice of the standard pair is entrywise `L_M`) is used at "its entry vectors are in `(L_M)_ℚ`" without argument. The saturation paragraph (`ch_P_r8_frames.tex:120`, trace-dual family for the half-different) reads correctly, but I did not compare it with `rational_points` line by line.

### 3.4 Verdict for task 2

`translate_entire_algebraic`: **CONFIRMED WITH GAPS**. Given `B.StdOK` and the existence clause of `kThetaVector`, the hand proof is correct and complete up to the standard facts in (c). Without those two inputs it is not a proof. The argument should be consolidated in one place, with the alternate-route statement first.

## 4. Root cone

### 4.1 Recomputation

Cone of `pairOK_allSites`: 10,648 declarations, **54,386** core lines (42,543 theorem lines), no literature leaf. After removing the cones of the complete units Z4.2.01, .03, .05: residual **24,978 lines (23,600 theorem lines)**. All figures in `ch_P_r15.tex:15–18, 523–525` and in `pair_review` of the register reproduce (1,508 / 1,417; 1,885 / 1,753; union 2,136 / 2,004; translate 20,441 / 19,402 residual, 24,503 / 20,015 inclusive).

| Part of the residual | Lines / theorem lines | Status after this review |
|---|---|---|
| Residual cones of the 26 registered declarations (union) | 2,386 / 2,239 | Hand-proved in `r15:site`, `r15:span`, `r15:datum`; confirmed in §2. Includes 108 lines under `gidx_facts` of which 99 serve unused conjuncts. |
| `kerTh_entire_algCoef` outside `translate_entire_algebraic` | 1,552 / 1,408 | Hand-proved in `r14:kernel-lattice`, `-finite`, `-jets`; confirmed by R14 review B rows 1–7; F3, F4 now closed. Contains Osgood (226 lines, named) and `Δ ≠ 0` support (about 500 lines, uncited). |
| `translate_entire_algebraic` | 20,441 / 19,402 | §3: conditional on two open inputs. |
| Everything else | 653 / 605 | Assembly; `scal0` and `chiFac` (argument of `ch_P_r8_frames.tex:122–126`, confirmed at argument level in R8; `chiFac_ne_zero` confirmed in R14 A row 30); `detId_normOne_mul` chain (390 / 366, class R in the supplier table); `level_structure_counting` (I read `PeriodLatticeFinitelyGenerated.lean:1774–1804` against `ch_P_r8_frames.tex:142`; correct); `isUnit_det_frameMatrix_ofCharts`; `site_base_datum_integral_off_bad_primes`. |

The four parts overlap in 54 lines and sum to the residual.

Inside the translate block, cutting at the supplier heads:

| Head | Inclusive in residual | Reachable from the root only through it |
|---|---|---|
| `thM_spec`, `isThM_ne_zero` (`kThetaVector`) | 3,264 / 3,001 | 1,700 / 1,596 |
| `FourthRootStd.stdOK`, `SO.stdOK` | 3,043 / 2,848 and 3,376 / 3,156 | 1,180 / 1,140 |
| The four together | 6,984 / 6,539 (union) | **3,062 / 2,906** |
| `AlgTranslate.coefIn_translate` | 11,409 / 10,889 | 2,054 / 1,958 |
| `integral_j_and_algebraic_data` | 2,295 / 2,225 | 751 / 730 |

### 4.2 Project-specific pieces neither hand-proved, nor confirmed, nor registered for this unit

| Piece | Lean | Size | Treatment |
|---|---|---|---|
| Existence of the fourth-root theta vector and the fourfold identity | `Ker.kThetaVector` via `thM_spec`, `isThM_ne_zero` | 3,001 theorem lines inclusive; 1,596 exclusive | Called an input (455–457, 573–574). Round-4 text only; never reviewed. Not in `status.json`, not in the Z4.2.04 register. |
| `B.StdOK` for every base over a curve datum | `FourthRootStd.stdOK`, `SO.stdOK`, with `FourthRootStd.up`, `Base.lat0OK`, `Base.areaOK` | 2,848 and 3,156 inclusive; 1,140 exclusive | "Remains an input" (575–576). Round-4 text only. |
| General translation of algebraic jets | `AlgTranslate.coefIn_translate` | 10,889 inclusive; 1,958 exclusive | Class N; sketched in `r15:jets`. Bypassed by the hand route, so not needed for the statement, but the bypass must be stated up front. |
| CM integrality and torsion coordinates in the project's period model | `CurveAlgebraic.integral_j_and_algebraic_data` | 2,225 inclusive; 730 exclusive | Class N. Round-8 text with a literature citation; first read here at argument level only. |
| Galois conjugation of translated genus-one jets | `cmTheta_taylorCoeff_algebraic_and_conjugate` and below | 6,554 theorem lines in the residual | Replaced by the recurrence argument in the hand route; say so. |
| Unused conjuncts of `gidx_facts` | `Served.served_facts` and below | 99 lines | Not mentioned. |

The first two rows are substantive and block closure. The third and fifth are a labelling matter. The fourth needs the ledger entry and a second reader. The last is clerical.

## 5. Unit verdict for Z4.2.04

**DO NOT APPROVE** (as an unconditional completion). Keep the unit `partial`.

What is established:

- The Pair assembly is correct and matches `PairOK` field by field.
- The two site lemmas that review B found unproved are now hand-proved correctly, with all their suppliers (26 of 26 confirmed).
- The finite expansion, the integral forms, `LatAll`, the scalar and character fields, the level, the moved datum and the frames are hand-proved and confirmed.

Why not approve:

1. **The cone contains two project theorems that the document itself declares to be inputs**: the fourth-root existence theorem (`kThetaVector`, 3,001 theorem lines) and `B.StdOK` (2,848 and 3,156). Together 2,906 theorem lines are reachable from the root only through them. `pairOK_allSites` has no such hypotheses, so they cannot be treated as pass-throughs. Their only hand text is from round 4 and has no review. The translated-coefficient argument, and with it the fields `Differentiable` and `CoefIn` of `PairOK`, depend on them.
2. **The translate argument has no single reviewed location** and follows a different route from Lean at its largest step (`coefIn_translate`, 10,889 theorem lines inclusive). This review read it once at argument level; `integral_j_and_algebraic_data` (2,225) and the saturation lemma were not compared with Lean line by line.
3. **Uncited standard theory** carries about 3,650 lines of the cone (Weierstrass functions), plus the CM `j` citation and torsion coordinates.

Paths to closure, either of which I would accept:

- **Conditional completion**, in the sense already used for Z4.2.06–.08: record the unit as complete given `B.StdOK` and the existence clause of `kThetaVector`, name both in the `basis` and `remaining_input` strings with the sizes above, and keep them open under Z4.2.13 / Z4.3. With the edits below this would be APPROVE AFTER MINOR EDITS.
- **Full completion**: write hand proofs of `kThetaVector` and of `stdOK` at the level of `r15:site`, register them, and have them reviewed together with a consolidated translate section.

Edits required in either case:

1. Consolidate the translate proof in one section; put "the hand route translates the four copies directly and does not use `coefIn_translate` or the Galois conjugation of translates" at its head.
2. State at the start of that section that `thMM` is an epsilon choice and that entireness and the fourfold identity both come from `thM_spec` under `StdOK`.
3. Add references for the Weierstrass facts, torsion coordinates and the fixed field of `Aut(ℂ/Q̄)`; record the CM `j` citation in the literature ledger and check its numbering.
4. Prove or cite `Base.lat0OK` where entry vectors are placed in `(L_M)_ℚ`.
5. Fix the citation slips of §2.6 (items 1–5), add the wrapper map (item 6) and the `gidx_facts` remark (item 9).
6. Update `status.json`: `remaining_input` of Z4.2.04 should name the two inputs instead of "independent proof review of …"; set the 26 rows to confirmed.

## 6. What was and was not read

Read in Lean (original numbering): all files of the 26 declarations in full; `EqGlobOfHat.lean`, `ExistsUnitaryOneDetEq.lean`, `CsGlob.lean`, `CsSpan.lean` in full; `Adelstab.lean:20–90`; `CsDual.lean:36–100`; `Levelaf.lean:423–442`; `IsOrthCo.lean`, `ExistsMidLevIff.lean:50–62`, `ToLEInvApply.lean:110–125`, `LocSpBot.lean`, `JointCmpEmbeddingY.lean:30–190`, `NatCastMemOfPlace.lean:10–70`; the root; `KerThEntireAlgCoef.lean`, `TranslateEntireAlgebraic.lean`, `AlgTAll.lean`, `VacuumEntireAndNormalizedJetsAlgebraic.lean:60–316`, `LateralTheory.lean:14–200`, `IsAdmissibleFlagPairOfUnitriangularLeftAutomorph.lean:40–100`, `GaloisConjTaylorThetaTranslate.lean:14–80`, `CmThetaTaylorCoeffAlgebraicAndConjugate.lean:255–345`, `ChiDetIdAndChiFacAlg.lean`, `LatticeTuplePairScalarMemAlgebraicClosure.lean`, `PeriodLatticeFinitelyGenerated.lean:1755–1806`; statements of `sgStar_laws`, `StdData`, `kernel4`, `IntAdApprox`, `adelstabL_lower/upper`, `IE_latS`, `prV_latS`, `latAt_isLattice`.

Not read: the Lean proofs under `kThetaVector`, the two `stdOK`, `coefIn_translate`, `integral_j_and_algebraic_data`, `vector_bound_link`, `rational_points`, the Weierstrass files, `CsGlobApprox`/`CsApprox` (statement only), `levelaf_denom`, `PNeatB` (statements only); the round-4 paragraphs beyond locating them; `ch_P_r15.tex:541–1080`, except the supplier table and `r15:jets`, which I read for the status of the translate inputs.

## Short summary

- All 26 registered declarations match their Lean statements and their hand proofs are correct. The two site lemmas review B asked for (self-duality of the kernel lattice at a unitary point; the local span as a frame image) are now properly proved. F1–F4 are closed.
- The Pair assembly is correct. Root cone 54,386 lines; residual 24,978 (23,600 theorem lines); every figure in the chapter and register reproduces.
- `translate_entire_algebraic` (20,441 residual lines): the hand argument is mathematically sound where I checked it, but it is spread over rounds 7, 8 and 15, takes a different route from Lean, and starts from two inputs the chapter itself leaves open: the fourth-root theta existence (`kThetaVector`, 3,001 theorem lines) and `B.StdOK` (2,848 and 3,156). 2,906 theorem lines of the cone are reachable only through them.
- Unit verdict: **DO NOT APPROVE** as an unconditional completion. A conditional completion on those two named inputs would be acceptable after minor edits; a full completion needs reviewed hand proofs of both.
