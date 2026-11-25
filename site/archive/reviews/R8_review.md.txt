AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

# R8_review

AI review report produced during this project; file names are internal working names.

- Internal source file: `out/R8_review.md`
- SHA-256: `6f2fe9757efaf77cb523bc756595405c38a3b270dad9f6515744b96cb463ae0c`
- Report scope: Round-8 independent review — depth-2 sub-theorems, Z4.2.06/.07, Z4.2.10/.11/.13, Kato questions B01–B09, Korean summary, build stamp

## Archived report · [English summary](../../reviews/R8_review.md)

The report below preserves its original verdict, scope and unresolved points. Historical review-machine home prefixes are displayed as `${REVIEW_HOME}`; the source checksum above identifies the original report. Source line numbers in other records count from its original title.

# Round-8 independent review — depth-2 sub-theorems, Z4.2.06/.07, Z4.2.10/.11/.13, Kato questions B01–B09, Korean summary, build stamp

Reviewer role: independent check of an AI-written blueprint against the Lean source. Nothing here asserts that RH is proved; the only questions are whether the hand proofs cover the Lean statements they label and whether the bookkeeping is honest.

Lean paths are relative to `${REVIEW_HOME}/src/rh/src` (the cleaned copy). Line numbers given as "Lean" are those of the cleaned copy, which run about 4–5 lines later than the numbers printed in the blueprint. Blueprint files are in `${REVIEW_HOME}/work/prev8/`.

## Verdict table

| # | Item | Verdict |
|---|---|---|
| 1 | 15 hand-proved sub-theorems (`ch_P_r8_small.tex`) | All 15 theorems checked (S01, S02, S04, S05, S06, S10, S11, S12, S14, S16, S18, S19, S20, S21, S22): **all CORRECT**. One statement-level mismatch (S01/S02 omit `IsTotallyComplex E`), harmless. No parent unit was closed on their basis. |
| 2 | Z4.2.06, Z4.2.07 | **R7 gaps fixed.** "Complete" is justified in the conditional sense the ledger defines, with one caveat that should be printed next to the status: the Lean roots have no Pair hypothesis and their cones contain the whole of Z4.2.04 (partial). |
| 3 | Z4.2.10/.11 downgrade, Z4.2.13 registration | **Accurate.** No complete unit reaches `TieBase.base_data`. Remaining-input lists are nearly full; a few direct suppliers are unnamed. |
| 4 | B01–B09 | Every question cites a real work. Both Coleman references exist as cited. Kato Lemma 1.7, Prop. 2.4, Thm 12.5(1), 12.6(2), 16.6(1),(2) checked against the Numdam text and match the use made of them. **`status.json` `kato_gaps[].comparison` is stale** for B04, B05, B07, B08, B09. |
| 5 | Korean summary | Statements, window argument, exponent and all counts agree with `status.json` and Lean. Disclaimer present. Two points need attention: `Main.lean` line numbers / `rhOfAll` cannot be confirmed from the cleaned copy, and the definition of *complete* is slightly stronger than what .06–.08 deliver. |
| 6 | SHA-256 stamp | **Match.** |

---

## 1. Sub-theorems in `ch_P_r8_small.tex`

Count check (`ch_P_r8_small.tex:2–5`, `status.json` `round8_subtheorems.counts`): 27 slots, Satake uniqueness ×4 and cardinality ×3 give 22 distinct declarations; 15 theorems + 2 instances + 5 record fields = 22. Correct.

| Item | Lean declaration (cleaned copy) | Statement | Proof | Verdict |
|---|---|---|---|---|
| S01 `HasSat.card` | `PublishedTheorems/GaloisCohomology₂/StrongMultiplicityOne.lean:78–81`; `HasSatGL.card`, `IsSatVecUOfIsSphericalU.lean:146–148` | Matches, except the Lean section carries `[IsTotallyComplex E]` (`StrongMultiplicityOne.lean:16`); blueprint says "number field" (`small.tex:38`) | Cardinality is the third conjunct of `IsSatVecGL` (`IsSatVecUOfIsSphericalU.lean:115–117`); correct | CORRECT |
| S02 `HasSat.unique` | same file `:73–76`; `eq_of_satEig_eq`, `IsSatVecUOfIsSphericalU.lean:93–109` | Same remark | Same vector, one uniformizer, cancel `q^{j(a−j)/2}`, compare `∏(X+b)`; this is the Lean route (`:139–142`). Quotient invariance via `Iso.hasSatGL` (`:22–33`) is stated | CORRECT |
| S04 `frob_unr` | `ExistsUniqueHcharOfFiniteOrder.lean:296–301` | Hypotheses (`v∤ℓ ∨ n=0`, unramified, `A` over `v`, Frobenius at exponent `Nv`) and conclusion `(ι⁻¹χ.val v)⁻¹` match | Uses the `frob` clause with `σ⁻¹` (`:35–37`), local identity, unit-independence. Sign is right. The "no continuous embedding `E_v→Q̄_ℓ`" argument (`small.tex:92–95`) is correct | CORRECT |
| S05 `ine_image` | same file `:263–273` | Matches, both directions, any `z` | Two uses of the `ine` field at `g=σ̄` and `g=a(i_v u)`; exactly the Lean proof | CORRECT |
| S06 `inv` | same file `:311–315` | Matches | `infPow_neg`, `lPow_neg` (`:210–215`, `:231–236`); correct | CORRECT |
| S10 `mem_of_isIntegral` | `Proofs/GlobalInterpolation/IneLeFixingSubgroup.lean:14–18` | Matches (any field, any valuation subring) | Standard "divide the monic equation by `x^d`"; Lean uses integral closedness instead. Correct | CORRECT |
| S11 `one_lt_normV` | `Definitions/AutomorphicMembership/ExistsNotCongPow.lean:146–149` | Matches | Finite quotient + `0≠1`; correct | CORRECT |
| S12 `Sep.hasFixed` | `AutomorphicForms/ConjSep.lean:20–21, 79–82` | Matches the pointwise definition of `Sep` (a `p` for each nonzero `x`) | Choose `x` first, then `p`; correct, and the remark that no common `p` is needed is accurate | CORRECT |
| S14 `cls_spec` | `CharacterLevelBounds/ShaFamMono.lean:112–121` | Matches (`N>0`, `ζ^N=1`, exponent is `val` of the class) | Cyclicity of `μ_N` by counting, then definition of the modular cyclotomic character; correct | CORRECT |
| S16 `phiAll` | `WeilCharactersModular/PhiAll.lean:12–17`; `PhiAll`, `LocCFTAll.lean:18–21`; `PhiCond`, `ResMapBijective.lean:333–336` | Matches: three `PhiCond` clauses for `Γ`, `G₀`, each `G_v` | The cocycle `d_φ(g)(x)=φ(s_x⁻¹ g s_{g⁻¹x})` is the Lean one (`PhiDec.lean:18–22`, `PhiGS.lean:136`). I rechecked membership in `H`, the cocycle identity, continuity and injectivity on classes: all correct. Global finiteness is used at `r=1` with `ContainsAbove` from `V.sub` (`PhiGS.lean:146–162`; `GalCoh.lean:92–96`). `G₀` step is `Det.phiSub` | CORRECT |
| S18 `norm_natCast_lt_one` | `Proofs/DivisorProofs/ExistsFiniteAdeleEmbeddingExtension.lean:21–25` | Matches | Norm extension twice; correct | CORRECT |
| S19 `away_ae`, S20 `eventually_natCast_notMem` | `InertialOrderFifteenCharAuxiliaryPrimeSpec.lean:78–82`; `AutomorphicForms/CountSys.lean:103–114` | Match (nonzero natural number, not necessarily prime; cofinite filter) | Finite quotient / prime factors of `(t)`; correct | CORRECT |
| S21 `IsConjOm.cyc` | `AutomorphicVarieties/PartsSign.lean:17–36` | Matches (`σ : Ω ≃+* Ω`, any `ℓ`) | `|j ζ|=1 ⇒ σζ·ζ=1`, then congruences mod `ℓ^m` for all `m`; correct including `ℓ=2` | CORRECT |
| S22 `levEx` | `WeilCharactersModular/SgnEqOne.lean:17–100`; `LevEx`, `ArithmeticPointClassicality.lean:135–138`; `Lev`, `ContinuousResP.lean:108–121` | Matches: `S'` finite, `s.S ⊆ S'`, decomposition groups in `H`; conclusion `∃ V, V.S'=S'` | All eleven fields of `Lev` are accounted for (`hη`, `η_open`, `η_c`, `hε`, `ε_cont`). Index two, `c∉H` via total complexity, inertia in `ker χ_ℓ` away from `ℓ` (distinct reductions of `ℓ^m`-th roots) are all correct. Closedness of `H` silently uses continuity of restriction (`continuous_resP`) | CORRECT |

Not sampled as proofs: S15, S17 (one-line instances), and the five field projections S03, S07, S08, S09, S13, which the text correctly counts separately and does not present as theorems proved (`small.tex:5`, `:145–157`).

Spot checks in the parent paragraphs: the adjoint-ratio argument for Z1.1.01 (`small.tex:373–382`) and the determinant identity for Z1.1.02 (`small.tex:395–407`) are arithmetically correct.

**Parents.** All nine parents remain `partial` in `status.json` (Z1.1.01, .02, .03, .05, .06, .07; Z1.5.03, .04, .05). Each parent paragraph ends by naming what is still open (`small.tex:387–390, 411–414, 428–434, 448–453, 470–476, 489–493, 505–511, 524–528, 543–549`). No closure is claimed.

**Requested fix.** `small.tex:38`: write "totally complex number field" or say that the hypothesis is present in Lean and unused.

---

## 2. Z4.2.06 and Z4.2.07 (`ch_P_r8_move_review.tex`)

R7 listed four gaps (`prev7/R7_review.md:343–344`). Status of each:

| R7 gap | Now | Evidence |
|---|---|---|
| No bracketed hypothesis label | Fixed | `move_review.tex:3–17` and `:122–136`: "[Hypothesis, discharged at `admissible_at_each_site`]", plus a "[Proved in Lean, not reproduced]" label for the site construction and for the general-pair kernel calculation |
| Existence of the move over unnamed lemmas | Fixed | `move_review.tex:19–63` constructs `κ_a`, `κ_1`, `κ=κ_a⁻¹κ_1`, `x'=(rat g)xκ` and names `awayEx_of`, `ptOne_of`, `isPt_move_eq`, `eMat_unitary_det`, `latK_rat_mul_lev`, `chi_detId_smulLat`, `xiM_smul_moveBy`. I located each: `TiedFamilies/EqOneOfPh.lean:156`, `TiedFamilies/TiePtOne.lean:59`, `SatakeParameters/IsPtMoveEq.lean:18`, `ToMatrixCoMulSymm.lean:98`, `LatKRatMulLev.lean:18`, `CharDeterminantIdealUnitarySmulSelfDual.lean:14`, `MovedDatumMovedLatticeTuple.lean:45` |
| `cΞ ∈ Q̄` not stated | Fixed | `move_review.tex:91–98`: `cΞ=μ_{j+1}(det κ)χ_lev(κ)⁻¹`, algebraic by `mu_alg` on the norm-one determinant and `χ_lev(κ)=embLL(r_a⁻¹)`. This is the `cΞ ∈ TaylorLogMetric.Qbar` conjunct of `MoveTie` (`Definitions/GaloisGeometry/NatCastMemOfPlace.lean:75–88`) |
| Source of `KIn` | Fixed | `move_review.tex:125–130`: `KIn(t)` is the joint field `J.kin`. Confirmed: `away_of_dict` passes `J.kin` (`KernelSiteSeriesIndependentAwayFromPlaceOverP.lean:19`); field at `JointCmpEmbeddingY.lean:81`; definition `IsUnifAt.lean:25` |

Statements still match Lean: `move_at_site : J.Dict std → S.Move` (`KernelSiteArithmeticGroupMovesFrames.lean:17–19`), `away_of_dict : J.Dict std → S.Away` (`KernelSiteSeriesIndependentAwayFromPlaceOverP.lean:16–19`).

Mathematics rechecked in the new text:
- `.06`: `y=(rat g)xκ_a⁻¹`, `κ_1=y⁻¹x'` gives `x'=(rat g)xκ` and `χ_lev(κ)=χ_lev(κ_a)⁻¹`; correct. `e=CgC⁻¹` unitary with `det e=det g`; correct.
- `.07`: `P` = preimage of `pW_v`; `p∉P²`; hence unramified and the half-different is a unit at `P`; `π=(p,p⁻¹)`; common denominator `D` and `c=aā∈w^m`; dual inclusion by `H(z,cy)=H(cz,y)`. Each step is correct, and the conclusion is literally `GL3Theta.EqOff` (`Formalism/SharpRestriction/GlobalSchurBounds/GL3Theta.lean:419–422`). The remaining conjuncts of `AwayTie` (`NatCastMemOfPlace.lean:89–102`) are each addressed.

**Is "complete" justified?** Yes, as a conditional completion, with one caveat.

The Lean proofs of both roots call `kernelSite_latticeTuplePairs_admissible S hD`, that is, the full Pair theorem of Z4.2.04, which is `partial`. Reachability in the dependency graph confirms that the cones of `move_at_site`, `away_of_dict` and `scal_at_site` all contain `GlobalTheory.pairOK_allSites`. Pair is not a hypothesis of these Lean statements. The hand proofs avoid the open part of Pair by using only three of its conjuncts:
- `admitted` (even ranks, self-dual lattices),
- `scal0 ∈ Q̄`,
- `chiFac ∈ Q̄`.

I checked that Lean reads exactly these: `LatticeTupleMoveScalarPowerOfP.lean:65` destructures `⟨hA1, -, -, -, hs1, hf1, -, -⟩`; `ThetaSeriesScalarBoundedOfPosPair.lean:42` reads only the first conjunct. The blueprint derives the two scalar fields in `ch_P_r8_frames.tex:122–126` (the argument `I_L·Ī_L=1`, `χ(I_L)^{2h}` algebraic is correct) and refers to the v10 text for self-duality (PDF text around "IsSDLatLatKOfStdL.lean"; I confirmed the passage exists but did not recheck it line by line).

So the claim "only the even self-dual lattice and the two scalar fields enter" (`move_review.tex:104–106`, `:133–136`) is true, and the completions stand on it.

**Requested fixes.**
1. `status.json` `round8_review.conditional_complete` lists `Z4.2.06`, `Z4.2.07` only. Z4.2.08 is in the same position (the ledger says so at `ch_trust.tex:270–276`). Add it.
2. The `basis` strings of .06/.07 say "Complete for a supplied site and dictionary". Add "and for the three Pair conjuncts derived at `r8:Z4.2.04`", since Pair is not a premise of the Lean statement.
3. The hypothesis label says "discharged at `admissible_at_each_site`". That lemma constructs the dictionary (`JointSiteChainComparedCarriesAdmittedSystem.lean:36`) but is itself quantified over sites; the site is chosen in `site_cmpLite_siteAdm` through Z4.2.02. The body text says this correctly (`move_review.tex:13–17`); the label alone is slightly too short.
4. The ultimate supplier of `J.kin` (`kernelCoefficientField_le_coefficientField`, `TrueColumnExistsChainChartsKernelDataForms.lean:77`) is not named.

---

## 3. Z4.2.10, Z4.2.11, Z4.2.13

**Downgrade.** Accurate. `status.json` has .10 and .11 `partial` with `remaining_input` naming the class-kernel pullback, the tied base, and suppliers B–E. `ch_P_r8_kernel_review.tex:49–174` labels A–E each as "[Proved in Lean, not reproduced]" and `:216–222` states plainly that the conclusion is conditional on them. The R7 objection (the site law had been substituted for the rational-isometry identity) is acknowledged at `kernel_review.tex:92–94`.

**Z4.2.13.** Statement matches `GlobalTheory.TieBase.base_data` (`KernelEntryPeriodNeZeroAndLatticeLaws.lean:19–24`): `t.δ≠0 ∧ LatAll ∧ VecP χ ∧ EqP χ` for every tied entry. The nonvanishing argument and the one-coefficient-field descent in `ch_P_r8_base.tex:8–16` are correct and correctly labelled as partial. I reproduced the figures in `base.tex:29` from the graph: 60,733 core lines, 8 literature-boundary declarations, 6,438 core theorems, 3,766 with valid ranges, 51,444 lines, 176 one-line ranges, 51,444−176=51,268.

**Remaining inputs — nearly full.**
- Z4.2.13 lists `Base.latAll`, `ColNorms.familyVectors`, `NatEqui.eqP`. The Lean proof also passes `cm_field_facts_hold`, `induced_cm_type` (`InducedCmType.lean:10–17`) and `ExponentsFinite.yFinite` (`KernelConstantExponentsFinite.lean:85–126`) into `familyVectors`. None of the three is named in `base.tex` or in the unit's `remaining_input`. Their cones are about 4,000 core lines each.
- Z4.2.10/.11: direct theorem dependencies of `tieDel_all_steps` (`KernelSiteFrameValuesAllStepsLtM.lean:23–94`) that are not named in `kernel_review.tex`: `FrameB.equiv_frame_b` and `FrameB.ltC_ne` (`EquivFrameBTheta.lean:470–487`), `DelA.rk_le`, `DelB.sysS_ranks`, and `kernelSite_contractionIdentity_operatorHalf`. The last is the largest direct supplier (89,475 core lines) and is where input A and `base_data` enter; it is cited elsewhere in v10 but should be named in this section.
- Z4.2.09: `base_data`, `KerMove.kerTh_move`, `lev_pos_and_noConj` match the Lean proof (`KernelSiteLawAndFixedCoordinateStabiliserLaw.lean:20–31`).

**Silent dependence on Z4.2.13.** None. Reachability from every unit root to `TieBase.base_data`: only Z4.2.09, .10, .11, .12, .13 reach it, all `partial`. It has two direct callers, `site_law_xiIn` and `kernelEntry_period_ne_zero_and_lattice_laws` (the latter feeds `kerTh_eq_pull`). The ledger's site table says this for .09 and .10/.11 (`ch_trust.tex:277–283`). The .12 row (`:284–286`) does not mention .13, but `status.json` and `base.tex:27` do; add three words to the row.

The only complete-over-partial dependency in the whole register is .06/.07/.08 over .04, discussed in section 2 and disclosed at `ch_trust.tex:270–276`.

---

## 4. B01–B09 (`r8_kato_questions.tex`)

**Bibliography — verified by fetching the publisher or author pages.**
- R. F. Coleman, *Division values in local fields*, Invent. Math. 53 (1979), 91–116, DOI 10.1007/BF01390028. Confirmed on the Springer page for that DOI.
- P. Schneider, O. Venjakob, *Coates–Wiles homomorphisms and Iwasawa cohomology for Lubin–Tate extensions*, in *Elliptic Curves, Modular Forms and Iwasawa Theory*, Springer Proc. Math. Stat. 188 (2016), 401–468. Confirmed on Venjakob's publication page. Theorem 2.2 of the arXiv version (1511.04922, Section 2 "Coleman power series") is headed "(Coleman)" and states existence of a unique Laurent series in the norm-invariant units interpolating a norm-coherent sequence; the paper's own proof line is "See [Col] Thm. A and Cor. 17". I did not check that the numbering in the published volume equals the arXiv numbering.
- K. Kato, Astérisque 295 (2004), 117–290. Confirmed on Numdam.

**Kato theorem numbers — read from the Numdam PDF text (OCR is poor; content checked, not symbols).**

| Cited | What the text says | Blueprint's use | OK? |
|---|---|---|---|
| Lemma 1.7 | (1) compatibility under `GL₂(Z/N)`, (2) distribution relation for Siegel units | B04, B05 (`:203–204`, `:236–237`) | Yes |
| Prop. 2.4 | Norm from `K₂(Y(Mℓ,Nℓ))` to `K₂(Y(M,N))` with a factor in `T'(ℓ)` | B02 (`:101–102`) | Yes |
| Thm 12.5(1) | Map `γ↦z_γ^{(p)}`; `exp*` image tied to `L`-values with sign `(−1)^{k−r−1}χ(−1)` | B03 (`:161–163`) | Yes |
| Thm 12.6(2) | For `T=V_{O_λ}(f)`, generators `_{c,d}z` with `ξ∈SL₂(Z)`, `(cd,6pN)=1`, `c≡d≡1 mod N`, lying in `H¹(T)` | B01, B02, B06 (`:59–61`, `:103`, `:283–285`) | Yes |
| Thm 16.6(1),(2) | (1) eigenvector `η` with `φη=αη`, normalized against `ω`; (2) Perrin-Riou map of the zeta element equals the `p`-adic `L`-function | B06, B07 (`:280–281`, `:343–345`) | Yes |

Not verified: the page numbers "p. 221", "p. 222" and "Kato 13.5" that appear only in `status.json`.

The observation in B06 that `D≡1 mod N` contradicts the smoothing inequality at `e=1, i=1, j=0` is correct: the inequality `D²≠D^{e+1}(θχ^{±1})(D)^i ψ(D)^j` (`CuspidalUnitaryTwists/CuspidalUnitaryTwistsClaim.lean:16–26`) becomes `D²≠D²`.

**Stale register.** `status.json` `kato_gaps[].comparison` disagrees with the questions file:

| Gap | `status.json` | `r8_kato_questions.tex` |
|---|---|---|
| B04 | Kato 12.5(1) | Lemma 1.7 and 12.5(1) |
| B05 | Kato 12.5(1) | Lemma 1.7(2) |
| B07 | Kato 12.5(1) | Theorem 16.6(2) |
| B08 | Kato 13.5(1),(2) | Coleman; Schneider–Venjakob 2.2 |
| B09 | Kato 13.5(2) | Schneider–Venjakob 2.2 |

The questions file is the better comparison; the JSON should be regenerated from it. The two Coleman works are registered in `literature_works` as "separately cited" and counted in the 55.

**Statements vs Lean (spot checks).** B01 matches `UpperTheory.Kd.K4.ml` (`NormProducts/Ml.lean:26–36`). B05 matches `cgA_coeff_of_isThB_succ` (`IsThBSuccCoeffCongStatement.lean:13–14`). B06 matches `CuspidalUnitaryTwistsClaim`. B08 matches `SExact` with `FrobLift` unfolded (`Definitions/Foundations/CyclotomicDvdExpandOfCoprime.lean:81–85`; `FixedIntegersIsUnitOfNotMemPrimeSpan.lean:73–74`); the stated "Frobenius on `R/pR` surjective" is a consequence of `σ` being an automorphism, not a separate Lean hypothesis. B09 matches `powerSeries_eq_of_congruent_values_at_primitiveRoots` including the precision `⌊m/2⌋−c₀` and truncation `ℓ^{3m}`. B02, B03, B04, B07 were read but not compared clause by clause.

**Precision for an expert.** B05, B06, B08, B09 are self-contained and can be answered from the page. B01–B04 and B07 are precise but lean on project names that are not defined in the file: `IsZetaSystemFixedExponent`, `IsZWc`, `Nf`, `χ_K`, `IsLamFR2`, `lamv`, `FixIc`, `toQ(pieceT)`, `IsThB`, `tval`, `mass`, `Pin7`. A reader without the Lean tree cannot evaluate those five. A half-page glossary would fix this. For B08 it would help to cite Coleman's own theorem number; per Schneider–Venjakob it is Theorem A with Corollary 17 (I did not read Coleman's text).

---

## 5. Korean summary (`summary.tex`, `blueprint_summary.pdf`, 6 pages)

**Disclaimer.** Present on page 1: "AI-written draft awaiting human review" and "RH 증명 주장 아님" (`summary.tex:31–32`), with the build stamp.

**Five statements** (`summary.tex:39–43`) against `Statements.lean` (definitions at lines 7–20 of the cleaned file) and `Main.lean`:
- `riemannZeta_eq_zero_re`: zero, `s≠1`, not of the form `−2(n+1)` ⇒ `Re s=1/2`. Matches.
- `LFunction_ne_zero_of_half_lt_re`: `N≠0`, `Re s>1/2`, `χ≠1 ∨ s≠1`. Matches.
- `LFunction_eq_zero_re` and the primitive version. Match.

Two things cannot be confirmed here:
- The summary cites `Main.lean:4, 6, 8, 10, 12` in the order RH, zeta, half-plane, strip, primitive. In the cleaned copy the theorems sit at lines 10, 13, 16, 18, 21 and the half-plane statement comes first. This is not a uniform +5 shift, so the cleaned `Main.lean` differs in layout from whatever the summary was written against.
- "앞의 두 줄은 같은 `rhOfAll`을 사용한다" (`summary.tex:46`). In the cleaned copy `riemannHypothesis := Claim.zeta LFunction_ne_zero_of_half_lt_re` and `riemannZeta_eq_zero_re := riemannHypothesis`; `rhOfAll` exists (`Supplements/Kernels/MainTheorems.lean:12`) with the same body but is not what `Main.lean` calls. Mathematically equivalent; please recheck both points against the original file.

**Window argument** (`summary.tex:52–60`). Matches `Deduction.CharFamily` (`a_i>0`, `N_i=1 ∨ χ_i≠1`), `Gm`, and `zeroFree_of_rpow_window` (`0<θ<1`, `δ>0`, some `C`, arbitrarily large `Y`, bound on `[Y, Y^{1+δ}]`, conclusion nonvanishing for `Re s>θ`): `DedekindLFunctions/CharFamily.lean:28–41`, `ZeroFreeOfRpowWindow.lean:14–17`. The second paragraph is a fair description of `landau_window` (`landauWindow.lean:87–`); I did not check the Mellin-derivative sentence against the proof body.

**Exponent** (`summary.tex:66`). Matches `ChebyshevInequalityOnWindows`: `Λ.Gm x ≤ x^(1/2+(eD+eL+7)·eps)` for `x≥x₁` in the windows (`Formalism/SharpRestriction/RamificationFrobenius/TotientGaloisClasses/TopWin.lean:24–26`), and the choice of small `ε` is `exists_small_eps` (`:36`). The sentence "열의 수 m을 √x 규모로 택하면" was not checked.

**Counts** (page 6 and the two tables). All agree with `status.json`, and I recomputed the graph figures independently:

| Figure | Summary | Recomputed |
|---|---|---|
| complete / partial / structure only | 28 / 27 / 0 | 28 / 27 / 0 |
| original inputs complete | 13 of 20 | 13 (Z1.4; Z2.K1, K2, K4–K8; Z3.1, Z3.2; Z4.1; Z5.1, Z5.2) |
| Z1.1, Z1.3, Z1.5, Z4.2 | 1/7, 2/8, 4/7, 6/13 | same |
| open-union lines | 2,217,882 | 2,217,882 |
| reached by exactly one unit, which is open | 815,888 | 815,888 |
| open only (not reached from any complete unit) | 2,068,365 | 2,068,365 |
| literature boundary declarations / theorems | 2,653 / 1,860 | 2,653 / 1,860 |
| four-register union | 6,324,998 | `status.json` value; not recomputed |
| modules, headlines, sign-offs, works | 175,187 / 5 / 0 / 55 | `status.json` values |

**Overstatement check.** One sentence: "판정 complete는 해당 선언에 적힌 가정에서 그 결론까지의 손유도가 문서에 있다는 뜻이다" (`summary.tex:48`). For Z4.2.06–.08 the hand derivation additionally rests on Pair conjuncts derived elsewhere and on the site carrying its fields, which is the looser definition in `ch_trust.tex:27–28` ("under its specified premises"). The summary sentence should be aligned with the ledger's. Nothing else in the six pages overstates; the Z4.2 paragraph (`summary.tex:103`) says explicitly that the theta-vector covariance and class-kernel transformation are still open.

Minor, outside the six pages: `ch_trust.tex:124–126` says the last two Dirichlet wrappers "take a projection and a primitive-character reduction, respectively". In Lean the strip statement comes from `Claim.strip` and the primitive one simply drops the primitivity hypothesis; "reduction" is the wrong word.

---

## 6. Build stamp

`sha256sum status.json` = `ed9d42a913c273a21bedb55e5d727f0bd7a0a0236e7bfc34e1253e96f648b725`.

`blueprint_v10.pdf` title page: "Built 2026-11-23 20:49:11 UTC status.json SHA-256 ed9d42a913c273a21bedb55e5d727f0bd7a0a0236e7bfc34e1253e96f648b725". **Equal.** `blueprint_summary.pdf` page 1 carries the same stamp. The PDF's embedded creation time (14:49:11 CST) agrees with the stamp. The PDF's status table (28 / 27 / 0; "13 original inputs … 7 remain open") agrees with `status.json`.

---

## Short summary

- The sampled depth-2 proofs are correct and faithful; the only statement slip is the missing "totally complex" in S01/S02. No parent was closed.
- Z4.2.06 and .07 now have hypothesis labels, named lemmas, `cΞ∈Q̄` and the `KIn` source. Their "complete" is a sound conditional completion. It depends on three Pair conjuncts that the blueprint derives separately while the full Pair theorem (Z4.2.04) stays partial; this should be written into the status basis, and Z4.2.08 added to `conditional_complete`.
- The downgrade of .10/.11 and the new unit .13 are accurate. No complete unit reaches `base_data`. A handful of direct suppliers are unnamed (`cm_field_facts_hold`, `induced_cm_type`, `yFinite`; `equiv_frame_b`, `ltC_ne`, `rk_le`, `sysS_ranks`, `kernelSite_contractionIdentity_operatorHalf`).
- B01–B09 cite real works with theorem numbers that match the sources where I could read them. Both Coleman references exist. `status.json` `kato_gaps[].comparison` is out of date for five of the nine.
- The Korean summary is accurate on statements, window argument, exponent and counts, and carries the disclaimer. Recheck the `Main.lean` line numbers and the `rhOfAll` sentence against the original file, and soften the definition of *complete*.
- The SHA-256 stamp matches.

Not checked: the self-duality derivation on the v10 page referenced as `r6:Z4.2.04` (existence only), B02/B03/B04/B07 clause by clause, the "√x columns" sentence, Coleman's own theorem numbers, and the published-volume numbering of Schneider–Venjakob Theorem 2.2.
