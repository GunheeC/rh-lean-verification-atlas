AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

# R14_review_B

AI review report produced during this project; file names are internal working names.

- Internal source file: `out/R14_review_B.md`
- SHA-256: `60856cf048b48ffbb71f7c7faca762efe865e425a6b66db34e144f23468f5713`
- Report scope: Round-14 review B: Z4.2.04 kernel coefficients, Z4.3(ii) `comb_of_tied`, and the nine round-13 proof checks

## Internal report

The report below preserves its original verdict, scope and unresolved points. The scope of one reference to section 3 has been clarified in this public edition. Source line numbers in other records count from its original title.

# Round-14 review B: Z4.2.04 kernel coefficients, Z4.3(ii) `comb_of_tied`, and the nine round-13 proof checks

Scope. (a) `ch_P_r14.tex:944-1298` (15 declarations registered in `R14_pending.json` for Z4.2.04 and Z4.3). (b) The nine round-13 registrations in `status.json` (`round13.new_subtheorems`, status `pending_review`) whose hand proofs are in `ch_P_r12.tex` and `ch_P_r11.tex:961-1001`. Lean was read in the original numbering of commit `40e56bab` (`git show`). Graph figures come from `graph_cache.bin` (same data as `graphq.py`); a line count is the sum of inclusive ranges of core declarations with a valid range.

Nothing here, in the chapters, or in the Lean development is treated as establishing RH or GRH. This report only compares hand proofs and bookkeeping with the Lean declarations they label.

Not in scope and not checked: `ch_P_r14.tex:1-943` (Z4.2.13: `LatAll`, vectors, equivariance), the round-7 and round-8 texts for the translated vacuum, and the round-4 Z4.3 text. Where a declaration below depends on them, that is stated.

## 1. Verdicts

### 1.1 Closure verdicts

| Item | Verdict |
|---|---|
| Z4.2.04 (`GlobalTheory.pairOK_allSites`) | **CLOSE AFTER LISTED FIXES** (fixes F1-F4 in section 6; F1 and F2 are substantive, not clerical) |
| Z4.3(ii) (`comb_of_tied`) | **Hand-derived** as the stated implication `AlgTAll -> t.Hyp -> LevFree -> admitted /\ IsComb`. Z4.3 as a unit stays partial |
| Nine round-13 registrations | All nine pass at proof level (5 confirmed, 4 confirmed with labelling gaps). No mathematical error found |

### 1.2 Round 14, fifteen declarations

All 15 names, files, line ranges and cone sizes in `R14_pending.json` reproduce from the graph.

| # | Declaration (Lean lines) | Text (`ch_P_r14.tex`) | Statement | Proof | Verdict |
|---|---|---|---|---|---|
| 1 | `RepComb.lamK_eq` (`RepComb.lean:331-333`) | 965-984 | match | both inclusions correct | **CONFIRMED** |
| 2 | `RepComb.laFacts_of_adm` (341-362) | 986-1007 | match | correct; depends on `Base.latAll` clause 1 | **CONFIRMED WITH GAPS** (G1) |
| 3 | `Ker.lattice_integral_of_facts` (`PeriodLatticeFinitelyGenerated.lean:1524-1529`) | 986-1002 | Lean statement is generic; text proves the CM instance | correct at the instance | **CONFIRMED WITH GAPS** (G2) |
| 4 | `Ker.finite_index_of_fg` (1703-1708) | 1017-1039 | match | correct | **CONFIRMED** |
| 5 | `Ker.twist_lattice_kernel` (179-196) | 1041-1081 | match, incl. the abstract form (1070-1074) | weights and phases recomputed | **CONFIRMED** |
| 6 | `Ker.theta_coset_kernel` (276-290) | 1010-1081 | match | correct | **CONFIRMED** |
| 7 | `GlobalTheory.kerTh_entire_algCoef` (`KerThEntireAlgCoef.lean:22-40`) | 1083-1111 | match | assembly correct; rests on rounds 7-8 and `LatAll` | **CONFIRMED WITH GAPS** (G3, G4) |
| 8 | `GlobalTheory.pairOK_allSites` (`KernelSiteLatticeTuplePairsAdmissible.lean:23-47`) | 946-962, 1113-1134 | match, all Pair fields | assembly correct; six site suppliers only cited | **CONFIRMED WITH GAPS** (G5) |
| 9 | `Ker.push_opU` (309-318) | 1187-1193 | match | correct | **CONFIRMED** |
| 10 | `Ker.reading_is_kernel` (320-333) | 1160-1205 | match (seven fields of `KerRead.Hyp`) | correct | **CONFIRMED** |
| 11 | `Ker.taylor_sum` (1457-1464) | 1237-1242 | match | correct | **CONFIRMED** |
| 12 | `Ker.transcendence_algebraic_eigen` (1826-1831) | 1219-1235 | match | correct; one uncited standard fact | **CONFIRMED WITH GAPS** (G4) |
| 13 | `Ker.kernel_combination_form` (1476-1498) | 1237-1264 | match | correct | **CONFIRMED** |
| 14 | `Ker.first_kernel_law_reading` (1520-1522) | 1259-1261 | match | composition | **CONFIRMED** |
| 15 | `Ggeo.KerComb.comb_of_tied` (`CombOfTied.lean:14-33`) | 1139-1156, 1209-1264 | match | correct | **CONFIRMED WITH GAPS** (G6, G7) |

### 1.3 Round 13, nine declarations (proof level)

All nine lie in the Z4.4 root cone; ranges and cone sizes reproduce.

| # | Declaration (Lean lines) | Text | Verdict |
|---|---|---|---|
| 16 | `TC.ChTw.charts_tuple_trivQ` (`ChartsTupleTrivQ.lean:86-101`) | `ch_P_r12.tex:3734-3813` | **CONFIRMED WITH GAPS** (H1) |
| 17 | `T.localMove_classRep_iff_localConditions` (`...Statement.lean:7-12`; proof `LocalMoveClassRepIffLocalConditions.lean:218-339`) | 3771-3803 | **CONFIRMED WITH GAPS** (H2) |
| 18 | `TC.twPack_ex` (`TrueColumnChoiceTwistedChainsFormsClasses.lean:272-319`) | 4126-4182 | **CONFIRMED** |
| 19 | `TC.tw_chains` (464-484) | 4184-4241 | **CONFIRMED WITH GAPS** (H3) |
| 20 | `TwAtStd.twAtT_exists` (`DecoStabTrivial.lean:146-176`) | 4184-4201 | **CONFIRMED WITH GAPS** (H4) |
| 21 | `TC.charts_funKilled` (`InclMulInvMul.lean:422-439`) | 2527-2540, 4141-4157 | **CONFIRMED** |
| 22 | `PerConj.period_conj` (`CevInjective.lean:219-225`) | `ch_P_r11.tex:952-1001`; cited at `ch_P_r12.tex:1236-1241` | **CONFIRMED** |
| 23 | `FormSym.readsK_one` (`MemFiCComp.lean:147-159`) | 2340-2347 | **CONFIRMED** |
| 24 | `T.nonempty_classMap_above_lastStep` (`...Statement.lean:7-8`; `NonemptyClassMapAboveLastStep.lean:7-16`) | 4166-4172 | **CONFIRMED** |

## 2. Round 14: Z4.2.04 declarations

### 2.1 `lamK_eq`: CONFIRMED

Lean: `lamK cc δ N N' = La D (tor0 D cc δ) N N'`, by `lambda_in_lattice_pair` (210-254) and `la_le_lamK` (290-329). The text's `Λ = δ·emb(aaOf·Hom(L,L'))` is `LamC` (`XiIndCClass.lean:216`), and the analytic group is `La` (`IsDiscriminantTwelfthRootOfIdealLattice.lean:74-76`).

- Forward: the generator `b₀t₀X` maps to `δφ₀(b₀)·emb(t₀·mat X)`, which is a generator of `La`. This uses that every `embT τ` restricts to `φ₀` on `K` (`FL.embT_K`, line 226); the text says "the same embeddings over φ₀|K" (971). Lean's two inductions over `O_E`-spans are the text's "multiplying an `O_E`-coefficient into `X` preserves its lattice condition" (977-978).
- Converse: `matH_toLin`, `toLin_mem`, and stability of `lamK` under `O_E` (`lamK_stable`, 265-269). The text's "expand and distribute" (980-982) is this.

Callers: `laFacts_of_adm`, `eNat_fixed`, `eNat_fixed_of_vec`, `thetaSpace_std_line`. No hypothesis to discharge.

### 2.2 `laFacts_of_adm`: CONFIRMED WITH GAPS

Lean: from `(B.latAll hcc hδ _).1` take self-duality and the semicharacter for the sign `al = (-1)^round(q)`; `KS.Lat.al_eq_La` (`SelfDualComap.lean:211-216`) converts `al` to `alphaQ = exp(πi q)` on the lattice; `lamK_eq` transports the lattice.

The text argues the same, with one honest difference of route for `q(x) ∈ ℤ`:

- Text (988-995): `ω = (1+i√d)/2 = φ₀(ω_K)` with `ω_K ∈ O_K`, `ωΛ ⊂ Λ`, `H(x,x)` real, hence `q(x) = (√d/2)·H(x,x) = Im(ω)·H(x,x) = E_H(ωx,x) ∈ ℤ` by self-duality. I checked this: `H` is linear in the first variable (`Sesq`, `IsSemiChar.lean:13`), `ωΛ ⊂ Λ` is `La_theta` (`SelfDualComap.lean:174-182`) with `theta_eq`, `lam_mul` (`PStdOK.lean:121-135`), and `d ≡ 7 mod 8` makes `ω_K` integral. Correct.
- Lean: `rational_integrality_link` (`LinkThetaStatementFamily.lean:82-105`) through `hermitian_form_integral_values`. The text says so at 1001-1002.

Then `exp(πi q) = (-1)^{round q}` for integer `q`, and both `IsSemiChar` clauses transport (996-1000). Correct.

**G1.** `Base.latAll` is a theorem (cone 6,055 lines), not a hypothesis of this declaration. Its hand proof is `r14:lat` (`ch_P_r14.tex:45-173`), registered for Z4.2.13 in this same round and outside my assignment. Lines 986 and 998 use it without a `\ref`. The verdict for rows 2, 3, 7, 12 is conditional on the `r14:lat` verdict.

### 2.3 `lattice_integral_of_facts`: CONFIRMED WITH GAPS

Lean statement (`LatIntOfFacts`): for **arbitrary** `E, emb, δ, d, sc, AA0, N, N'`, `LaFacts → LatInt (HV sc) (√d/2) LamC`. Proof: Hermitian by `herm_HV`; `E_H ∈ ℤ` on `Λ²` from `dualLat = Λ`; the diagonal from the sign clause, `alV x = ±1 ⟹ q(x) ∈ ℤ` (`int_of_sign`, line 1529).

**G2.** The text obtains the diagonal from the CM multiplication `ω` (previous subsection). That argument is valid for the instance used in `kerTh_entire_algCoef`, but it does not prove the Lean statement, which has no CM structure. The one-line generic step is missing: `exp(πi q(x)) ∈ {1,-1}` forces `q(x) ∈ ℤ`. Add it; the label then covers the declaration as stated. The other two fields are covered as written (986-987).

Callers: `kerTh_entire_algCoef`, `combined_kernel_twisted`; in both `LaFacts` is supplied by `laFacts_of_adm` or a hypothesis.

### 2.4 `finite_index_of_fg`: CONFIRMED

Lean (`IdxOfFG`): `0 < c`, `LamC.FG` give three nonzero relative indices, by `half_periods_torsion` (248-256), `fg_of_nsmul`, `fg_of_le_fg`, `relIdx_ne_zero_of_tor` (1660-1699).

Text 1010-1033. Checked:

- `twist₂ M c e = {x : x ∈ c^{e_Q} M_Q ∀Q}` (`XiIndCClass.lean:180-182`); `halfAO` uses `-expS`, `halfBO` uses `expS` (187-191). The text's `A ↔ c^{-e_Q}M_Q`, `B ↔ c^{e_Q}M_Q` (1012-1013) is right, and `cA, cB ⊂ Λ`, `cΛ ⊂ B` follow because `e_Q ∈ {-1,0,1}` and `M = ⋂ M_Q` (`tw_nsmul_mem`, `nsmul_mem_tw`).
- `A, B ⊂ c⁻¹Λ` are finitely generated; `Λ ∩ A ⊂ Λ` likewise. A finitely generated group killed by `c > 0` is finite. Correct.
- The three quotients at 1029-1033 are `repsOf Λ AC`, `repsOf BC (Λ ⊓ AC)`, `repsOf Λ BC` of `xiV` (`XiIndCClass.lean:224-228`), in that order.

Finite generation of `Λ` itself (1017-1023) is `perO_fg`, `period_lattice_finitely_generated` (1714-1753): not registered, but derived in the text and in round 8 (`ch_P_r8_frames.tex:142`). The inputs "`N'` finitely generated, `N` spans" are fields of `IsSDLat` (`KerThEntireAlgCoef.lean:26-27`).

### 2.5 `twist_lattice_kernel` and `theta_coset_kernel`: CONFIRMED

I recomputed the weight from the definitions.

- `opU H x F z = F(z+x)·exp(-πH(z,x) - πH(x,x)/2)` (`IsSemiChar.lean:21-22`). Then `U_xU_y = exp(-πH(x,y) + (π/2)(H(x,y)+H(y,x)))·U_{x+y} = exp(-πi E_H(x,y))·U_{x+y}`. This is line 1049-1051 and Lean `opU_xiS` (168-177).
- `hatS H 1 SA Φ y = |SA|⁻¹ Σ_t Φ(t)·brk(y,t)⁻¹`, `brk(y,t)⁻¹ = exp(2πi E_H(t,y))` (`XiIndCClass.lean:18-21`). At volume one the two volume factors are 1. This is 1044-1048.
- `xiL` inserts `α(x)` and `Φ(·-x)` (26-27). So `r_{x,y} = α(x)α(y)e^{-πiE_H(x,y)}|S_A|⁻¹ Σ_t Φ(t-x)e^{2πiE_H(t,y)}`. The display at 1054-1057 equals the Lean term at 181-183 factor by factor.
- Integrality (1060-1069): with `cx, cy, ct ∈ Λ` and `LatInt`, `c²q`, `c²E_H` are integers; each phase has `2c²`-th power one; a root of unity has norm one at every `p` (`IntOff.of_pow`, 58-70); `|S_A|⁻¹` is a `p`-unit for `p ∉ S` (`IntOff.inv_nat`); the ultrametric inequality closes it. `Φ = onV Ξ` is `Ξ` at a chosen preimage or zero (`XiIndCClass.lean:210-211`); the text states this faithfully (1041-1043).
- `SNum S |S_A|`: the middle index is positive and the quotient is killed by `c` (`cΛ ⊂ B`). The text bounds the order by `c^h`; Lean uses Cauchy's theorem (`snum_relIdx`, 260-274). Both are correct.
- The abstract `XiLKer` takes `TorS` for each transversal element, `SNum S |SA|`, and integrality of `Φ(s-x)` as hypotheses. The text states exactly these (1070-1074).

Callers of `theta_coset_kernel`: `kerTh_entire_algCoef`, `reading_is_kernel`, `combined_kernel_twisted`. The hypotheses `LatInt` and the three indices are supplied by rows 3 and 4 in the first, and by `KerRead.Hyp` in the second (pass-through, labelled as `t.Hyp`).

### 2.6 `kerTh_entire_algCoef`: CONFIRMED WITH GAPS

Lean (22-40): `lattice_integral_of_facts ∘ laFacts_of_adm`, `period_lattice_finitely_generated`, `finite_index_of_fg`, `theta_coset_kernel`, then `entire_algCoef_comb` with `translate_entire_algebraic` at each shift, using `lambda_in_lattice_pair` to place `m·t_k` in `La`.

Text 1083-1111 follows this. The statement matches: `Differentiable ℂ (kerTh …) ∧ CoefIn … Qbar` under `admitted`, `SNum S cl`, `∀x, IntOff S (Ξ x)`. The caveat at 1105-1107 (norm bounds concern the weights, not the jets) is correct and worth keeping.

**G3.** The algebraicity of `[z^β] U_{x+y} e` is `translate_entire_algebraic = ThLoc.algTAll`, residual cone 20,441 lines. Lines 1084-1097 summarise rounds 7 and 8 (`r7:Z4.2.04`, `r8:Z4.2.04`); they do not reprove it. I did not re-audit those texts. `status.json` records the round-8 sublemma as established; this row inherits that. Two small points inside the summary: entireness of `e` itself is used at 1098-1100 but not stated (it is a finite sum of translates of the entire standard vacuum times a constant; Lean `vector_bound_link … h1.1`); and `Base.latAll` is again inside this cone (G1).

**G4 (uncited standard fact).** Termwise differentiation (1101-1103) needs each summand to be `C^∞`. Lean gets this from Osgood's lemma: a Fréchet `ℂ`-differentiable function on `ℂⁿ` is analytic (`analyticOnNhd_of_differentiable_vc`, `AnalyticOnNhdOfDifferentiableVc.lean:20-32`, using `AnForm.Osgood.osgood`; 185 theorem lines in `Osgood`, `OsgoodA`). The text cites lines 34-41 only and does not name the fact. The same fact is used silently at 1223-1225 ("holomorphic and smooth") for row 12. Name it once (Osgood, or Cauchy's formula on polydiscs).

### 2.7 `pairOK_allSites`: CONFIRMED WITH GAPS

Lean (23-47) and text (946-962, 1113-1134) agree field by field with `PairOK` (`NatCastMemOfPlace.lean:57-62`): admitted; `DatLoc` for `xiM`; differentiable; `CoefIn`; `scal0 ∈ Q̄`; the two `chiFac` clauses; for each place two unit determinants and two local spans (case split on the index, as at 1124-1126). The inputs to row 7 are right: the level is `SNum` by `site_finite_data_level_pos_bad_prime_factors` (= `level_structure_counting`), and `IntOff` for `xiM` follows from `S.law.int` on the defining branch and zero otherwise (`SiteBaseDatumIntegralOffBadPrimes.lean:13-18`), since `xiM` only re-indexes `xi0` (956-958).

Caller: `T.kernelSite_latticeTuplePairs_admissible` (wrapper). The hypothesis `J.Dict std` is a pass-through; its supplier `joint_dict` is Z4.2.03 (complete).

**G5.** Nine suppliers are cited by name at 1118-1126 and 949-953, "as in the earlier Z4.2.04 work". Their status:

| Supplier | Residual outside Z4.2.01/.03/.05 (lines / theorem lines) | Hand text |
|---|---|---|
| `kernelLattice_selfDual_even_rank_at_site` → `isSDLat_latK_of_stdL` (`IsSDLatLatKOfStdL.lean:19-34`) | 1,525 / 1,434 | one sentence, `ch_P.tex:13182`; R8 recorded it as not checked |
| `frame_localLattice_span_kernelLattice_zero`, `_succ` → `KerSp.locSp_latK_isPt` | 2,047 / 1,915 and 2,068 / 1,936 (shared core 1,885 / 1,753) | four sentences, `ch_P.tex:13182` |
| `latticeTuplePairScalar_mem_algebraicClosure` | 2,567 / 2,417 (mostly the two rows above and the next) | `ch_P_r8_frames.tex:122-126` |
| `chi_detId_and_chiFac_alg` | 1,021 / 972 | `ch_P_r8_frames.tex:122-126` (hand proof) |
| `site_finite_data_level_pos_bad_prime_factors` | 63 / 59 | `ch_P_r8_frames.tex:142` |
| `movedPairDatum_congr` (`xiM_datLoc`) | 54 / 39 | one sentence, `ch_P.tex:13184` |
| `intOff_xi0_of_joint` | 26 / 17 | `ch_P_r14.tex:955-958` (complete) |
| `isUnit_det_frameMatrix_ofCharts` | 11 / 11 | trivial (`det` of a unit matrix product) |

The first two rows are project-specific mathematics (self-duality of the adelic lattice at a unitary point; the local span of that lattice as a frame image). Their union is 2,136 lines (2,004 theorem lines). They have a few sentences of text from round 6 and no proof-level review on record. The paragraph at 1130-1132 should not present them as established without saying so.

## 3. Round 14: Z4.3(ii) declarations

### 3.1 `push_opU`, `reading_is_kernel`: CONFIRMED

- `push_opU`: `opU (HV A⁻¹) t F (z∘iT) = opU (formV A) (s.pt t) (s.push F) z` with `s.pt t = t∘iT⁻¹`. The text's `s_*(U_vF) = U_{P_s v}(s_*F)` (1187-1193) is this; the proof by re-indexing the sum over `τ` is `HV_push` (298-304) and `pt_iT`.
- `reading_is_kernel`: `KerRead.Hyp` (`FirstKernelLawReading.lean:114-123`) has exactly the seven items listed at 1160-1167: `A.sc = area⁻¹`, `SNum S lev`, pushed vacuum, `LatTie`, `LatInt`, three indices, `IntOff` of `Ξ`. Lean applies `theta_coset_kernel`, pushes each term (`hsc, push_opU, he`), and transports the torsion with `hlat` (`s.pt (a•t) = a•s.pt t`). The text does the same (1194-1197). `kernel_comparison_holds` only repackages `IsKerG` as `IsKer` (200-208), as said at 1201-1202.

Caller: `first_kernel_law_reading` only. `KerRead.Hyp` is a pass-through of `t.Hyp`.

### 3.2 `taylor_sum`, `kernel_combination_form`, `first_kernel_law_reading`: CONFIRMED

- `taylor` is the iterated Fréchet derivative at 0 on coordinate vectors divided by `∏α_k!` (`IsDiscriminant….lean:115-118`); linearity for `C^∞` summands is `taylor_sum`. Text 1237-1242.
- `kernel_combination_form` (`KerCombOf`): from `TransAlg` and `IsKer` build `IsComb` with weights `lamC λ (r_k)`, the same shifts, the **same** lattices `L, L'`, `EqAt` with multiplier 1, `admitted` from the hypothesis, torsion multiplier prime to `p` because it is `S`-supported and `p ∉ S`. Coefficientwise: `lamC` is additive and multiplicative on `Q̄` (`lamC_sum`, `lamC_mul`). All of this is in the text (1243-1258), including the remark that no infinite sum is exchanged and that the general `IsKer` has a separate annihilator per shift. Smoothness of `U_v e` is `contDiff_opU` (`ThDistC.lean:435-441`).
- `first_kernel_law_reading` composes the two (1520-1522).

### 3.3 `transcendence_algebraic_eigen`: CONFIRMED WITH GAPS

Lean (`TransAlgENat`): under `IsCurveIdeal`, the discriminant root, `δ ≠ 0`, `B.StdOK`, `B.AlgT χ`, conclude `TransAlg D B.tor (B.eNat χ)`. Smoothness: `thMoved_mem (latAll) (thZeroMem StdOK) hAdm` gives differentiability, hence `ContDiff`; `eNat = chiFac·thMoved`. Algebraicity: the hypothesis `B.AlgT χ`, passed through.

Text 1219-1231 matches, including that `AlgTAll` is a supplied law. Gaps: G4 (differentiable implies smooth in several variables is uncited), and the dependence on `thMoved_mem`, `LatAll`, `StdOK`, whose hand proofs are `r14:vec-transport` and `r14:lat` (outside my scope).

### 3.4 `comb_of_tied`: CONFIRMED WITH GAPS

Lean (14-33), step by step against the text:

| Step | Lean | Text | Check |
|---|---|---|---|
| Even ranks | `k_even.add (t_odd.add_one.mul_left j)` | 1209-1210 | `N_j = k + j(t₀+1)`, correct |
| Self-duality | `((t.O u μ).lat i c).2` | 1210-1212 | fields of the lattice object |
| `TransAlg` | `transcendence_algebraic_eigen` with `delta_ne`, `stdOK`, `hAlg … t.χ_ok` | 1219-1231 | correct |
| `p ∉ S` | `t.O_S`: `S = insert T ({g₀,g₁} ∪ Y.Qp μ)`; three clauses of `LevFree` | 1212-1215 | matches `FirstKernelLawReading.lean:432`, `DataKerI.lean:65-67` |
| Identify lattices and kernel | `rw [t.O_lat, t.O_Th]` | 1198-1199 | correct |
| Conclude | `first_kernel_law_reading … (hH u μ i hi) hTA … hS` | 1259-1261 | correct |

Hypotheses and discharge sites (graph):

- `AlgTAll`: pass-through in `comb_of_tied` and in all four callers; discharged by `ThLoc.algTAll` inside `CurveThetaInert.torsionTaylorAlgebraic_latticeExists_of_cm` (`TorsionTaylorAlgebraicLatticeExistsOfCm.lean:15-19`), called from `Svd.servH_row_of_artin` (`BundleBoth…ArtinReci.lean:15-24`). The text cites `servH_row_of_artin` and `AlgTAll.lean:12-26` but does not name the discharging declaration.
- `t.Hyp`: pass-through; discharged in `PdvClose.at_of_true_columns` (`AtOfTrueColumns.lean:30-47`) by `kernelEntries_hyp_of_columnSideProperties _ … hDuty.col hTop`. The text says this correctly (1284-1286).

**G6.** `comb_of_tied` has four callers. The text names one (`exists_beFam_evenConditionsInert_of_kerEnt`, 1267-1281; I checked that paragraph against `AdmissibleKernelSeriesInertPrimeNonConjugateFrob.lean:24-65` and it is accurate, including the order of choices and the `(1,0)` default). The other three are not named: `Ggeo.frobeniusConjugation_conditions_adaptedKernelDatum_alt` (`…AdaptedKernelDatum.lean:23-62`), `Ggeo.AdmEntInt.kernelDatum_entries_integral_away_from_d` (`KernelDatumEntriesIntegralAwayFromD.lean:25-41`), `Ggeo.KerShapeD.thetaKernelShapeAtD_ofKer_of_hyp_adapted` (`KernelDatumThetaSeriesShapeAtDAdaptedBases.lean:16-42`). All three pass `AlgTAll` (as `hIn.algT` in two of them) and `t.Hyp` through, and all are consumed in `at_of_true_columns`.

**G7.** `\pageref{r10:z43-register}` (1289) points to a label that is defined in no chapter of the blueprint directory. The register it refers to exists only in `status.json` (`units.Z4.3.application_premises`).

## 4. Round 13: the nine proof checks

### 4.1 `charts_tuple_trivQ`: CONFIRMED WITH GAPS

Lean chain: `match_idx` (`MatchTupleChartMemberChart.lean:17-110`) → `match_base_trivQ` (23-40) → `charts_match_trivQ` (44-82) → `charts_tuple_trivQ` (86-101), with `ChExM.exists_charts`.

I read `match_idx` in full against 3754-3770 and 3787-3797:

- `exists_conj_referenceChartIndex` gives `x'` with the group identification and equal characters, and `x' = 1` when `i+1 = m`. `exists_reference_class_matching_coupling_coset` gives `c₀` and `y` in the reference type group. With `x = y x'`: conjugation by `x` still identifies the groups because `y` normalises the reference group (`hxg`, 43-51); the character is unchanged because the target is abelian (`hxc`, 52-58). At `i = m-1`, `x = y` and the coset clause of `y` applies (`hx1`, `hcos`). All as in the text.
- `exists_unitaryAdelic_lift_typePrime_reductions` gives `t`. Forward direction (61-84): the local-move criterion, conjugation invariance of the lattice conditions, `θ = 1` from `twistLocalCondition_conj_iff_frameChange_trivial`, the reference move `(1, x h x⁻¹, 1)`, vacuous twist condition for `μ₀`, equal characters. Converse (85-108) by the inverse conjugation. This is 3762-3767 and 3787-3797.
- `θ = 1`: at `P ∈ Q`, `t_P = 1` and `s_P = 1`, so the embedded `θ_P⁻¹` is the identity, and `E → E_P` is injective. Correct (3793-3795).

`charts_match_trivQ`: membership gives a move (`locMv_of_mem`, `ChartLevelTwistTrivialLocalMove.lean:86-115`: `s = 1` at twist places, so the rational twist frames still represent the new point; disjointness of generator and twist places by `levOk_twists`), and a move gives membership and the character (`reads_of_locMv`). This is 3797-3803. `charts_tuple_trivQ` then takes `K` from `exists_charts`, gets `Uloc` equality off `Q` by inserting a single local element (`stepLevel_uloc_eq_of_agree`, 3768-3770), finite order from `exists_charts`, and the character clause from `charts_match_trivQ`. Correct.

**H1 (labelling).** Seven helper declarations in the Z4.4 root cone are used but not named; some are covered only by a file range: `locMv_of_mem` (cone 13,330), `reads_of_locMv` (6,187), `admissibleBasePoint_chart_mul_twist` (5,042), `underQ_prime_to_bad` (8,344), `stepLevel_uloc_eq_of_agree` (380), and the two conjugation statements `localConditions_conj_unitary_keepsStdLattice`, `twistLocalCondition_conj_iff_frameChange_trivial` (file ranges at 3804-3806, no names). I read the statements of the last two and the proof of `locMv_of_mem`; I did not read `exists_pt_of_agree`, `conj_unitary_preserves_stdLat_of_ptOf`, or the proofs of the three large suppliers (reference coset, adelic lift, `exists_charts`), which have their own paragraphs.

Caller: `twStep_mid` only, for `a ≠ μ₀`, with the reference reading from `(hF u).mid`.

### 4.2 `localMove_classRep_iff_localConditions`: CONFIRMED WITH GAPS

Lean `locMv_iff` (314-337) with `conds_of_pts` (218-272) and `pt_of_conds` (274-304). `LocMv` is: rational component one, coset preserved, and for every `g` representing the class representative, `g·s` represents the moved decoration.

Text 3771-3786 against Lean: lattice preserved after cancelling `g` (`carries_cancel`); pullback coordinates of `gs` are `s⁻¹` times those of `g` (`hasRes_pullV`); rational lattice vectors lifting a residue basis (`exists_single`); last row of `s⁻¹` at level primes and full reduction `h_w` at generators; exact twist frame gives `s_P = ι_P(θ_P⁻¹)` (255-272); conversely five fields (`uni`, `lat`, `f`, `be`, `fr`) for every representing `g`. All correct; unitarity of `s` is `s = g⁻¹(gs)`.

**H2.** The forward implication needs one representing `g` to exist; Lean takes it from `hI.exists_isPtOf` (329). The paragraph starts "for a represented point" and never says a representative exists. One clause with that name closes it.

Caller: `match_idx` only (four uses).

### 4.3 `twPack_ex`: CONFIRMED

Lean 272-319 against 4126-4182:

- Stage `0`: `twStep_out` with labels transported by `e₀`. Stages `1 ≤ i < m`: `twStep_mid`, which for `μ₀` widens the reference chart to the larger bad set (`chartWiden`) and otherwise calls `charts_tuple_trivQ`. Stage `m`: `twStep_top`, with the singleton reference chart or `chart_lastStep_twistBasePoint`. Stages `> m`: `nonempty_classMap_above_lastStep`. The family is updated at `m` to the distinguished top entry. All as in the text.
- `twStep_mk` (111-138): replaces each functional (`killK`, `swap_ex`, same `swapLaws` as row 21) and builds the Hermitian level by `chartTie_toQ` (`StepQOfReindex.lean:56-63`). I read `stepQ_of_reindex`: off `Q` the local groups come from `H` (through `CarH`), at `Q` from an open-subgroup lemma. Matches 4158-4164.
- Finite exponent at `m-1` (293-302): for `μ₀` exponent 1 by `chi_triv` because `Q = ∅` (`not_twistPlace_referenceTuple`); otherwise `chiFin`. Matches 4175-4178.
- Coupled level, equal base lattice (`twBefore_cl_nonempty`, `reads_lb_eq`), corrected character (`exists_levelJ_character_eq_member_off_places`), and `{J with chiJ := χ}`. Matches 4178-4181 and the paragraph at 3815-3860.

Minor: "by openness" (4161) is `T.open_congruence_subgroup_preserves_principal_lattice` (dominates 249 lines), not named. Caller: `tw_chains`.

### 4.4 `tw_chains`: CONFIRMED WITH GAPS

Lean 464-484 with `twT` (338-380), `twJ` (384-396), `twW` (413-445), `twJS` (447-458). The displayed statement (4203-4213) matches the Lean statement. Checked: `Q a` is the image of `I.Q a` under contraction; `twT` uses `e₀` and the trivial stabilizer isomorphism from `free0`; `twJ` uses `offU`, `offL`; `twW` takes `val` from `hermitianChart_complex_rational_integral_forms` (= `TC.val_tied`), `dil` from `diamondOperators_on_charts` (= `DiaChart.dilTied`) with the killed functional and `eVT = refl`, `ipV`/`norm` from `ipV_norm_tie`, all with the identity-on-matrices frame from `StdF` (`idY_twYS`). `StdW`: three `rfl`, `eVT = refl`, the residue clause from `twAtT_exists` and `(hF u).res`, readings, the two top clauses, `fk`. `TwChMu0` by `eCls0_mu0_eq_self`. Matches 4214-4236.

**H3.** (a) The `W` field `twisted_e0_at_mu0_eq_eMu0` is supplied by `T.stepZeroFormsIdentification_referenceTuple_eq_self` (`law0_choose_mu0_eq_self`, 30 dominated lines), not named; it follows from `eCls0_mu0_eq_self` and injectivity of the stage-zero embedding. (b) The Lean hypothesis `StdF ∧ StdLvC` is displayed, but only `StdF` is used in `tw_chains`; `StdLvC` is used in `tw_chains_std` (488-489) to supply the `glevJ.fr = 1` hypothesis. Say so. (c) The direct caller `T.trueColumnChoice_twistedChains_formsClasses` is not named (the text names `tw_ties_with_points`).

### 4.5 `twAtT_exists`: CONFIRMED WITH GAPS

Lean 146-176: `eVT`, `eFv` identities; `rhoT` from `dil_eCls0` (23-33) and `dilT_eCls0` (88-128); `Mu0` from `mem_Fi_of_free` (130-142); the rest `rfl`.

Text 4190-4201: the diamond changes only the residue functional, so it commutes with `e₀` (classes at zero are read from the canonical decoration); two moves agreeing on the decoration differ by an integral twist factor, the twist group at zero is the full group with trivial character (`chrQ_top`), freeness makes the stabilizer trivial, so rational and generator components agree (`deco_stab_trivial`, 35-73); under freeness the form space is the classwise polynomial condition. All correct.

**H4.** `deco_stab_trivial` also needs the marked coset set at stage zero to be empty (`hp0`, line 62, from `ClsZero.ys0`), so that the action fixes the whole decorated point and freeness applies. The text omits this.

Caller: `tw_chains`.

### 4.6 `charts_funKilled`: CONFIRMED

Lean 422-439: `Lb = baseLb` from the reading, `Reside.swapLaws` (383-397), new chart `{K β with lev := swap …}`; `Lb, Uloc, U, y, stabI` are definitionally retained, and the character on equal underlying elements. Statement retained exactly (R13).

Proof content is `stab_eq` (312-344). I checked the mathematics: at a split level place `E_v = E_P × E_{P̄}`; dual/base is the sum of two lines of order `T`; a nonzero `O_v`-linear functional to a module of prime order `T` vanishing on the base lattice is killed by `π` or by `π̄` (`kill_or`, since `ππ̄ = T`). If by `π`, it and the canonical functional factor through each other (`fLoc_of_fT`, `fT_of_fLoc`), so the stabilizers agree. If by `π̄`, a unitary `g = (g_P, (g_P^*)⁻¹)` acts on the two lines by `a` and `ā⁻¹`, so fixing either line pointwise is the same condition (`row_inv`, `rll_mem_stabFun`, `fixes_of_row`). The text says this at 4144-4153 and 2530-2533. The canonical functional has order `T`, is killed by `π_T` (`fLoc_killed`), is nonzero and vanishes on the base lattice.

Callers in the root cone: `formsTiedSym_std` (named at 2539). `charts_funKilled_one` is outside the Z4.4 root cone.

### 4.7 `period_conj`: CONFIRMED

Lean 219-225 assembles `jM`, `jM_injective`, `jM_onto`, `jM_mem`, `period_eq`, `re_petersson_self_pos`. Against `ch_P_r11.tex:952-1001`:

- `E^* = cev`; injective by vanishing on invertible frames; conjugate-linear preimages (`exists_cev`, 24-39). Correct.
- Intertwining (`cev_act`, 74-97): a finite-order character value has absolute value 1, so the conjugate of `σ(χ(g))⁻¹` is `σ(χ(g))`; `γ⁻¹ = γ^*`. Lean also uses that the embeddings commute with conjugation (`fields_ok.conjE`, line 222); the text uses this silently in "substitution in the frame action". Worth one clause.
- Onto: lift `P_c`, fixed by the stabilizer by injectivity, extend by the action, independence of the choice (`key`, 161-171). Injective because the source law holds for the full group (`H = ⊤`). Correct.
- Period identity from `polOf_cev`, `nfAll_conj`, `ipVal_cev`; weights `1/|Stab|` on both sides; positivity from `ps_fockF_pos` and finite stabilizers. Correct.

Callers in the root cone: `formsTiedSym_std`, `tupleLayer_compatibility` (both named). `ipMt_tie` is outside the root cone.

### 4.8 `readsK_one`, `nonempty_classMap_above_lastStep`: CONFIRMED

- `readsK_one` (147-159): with all labels equal to `β`, take the witness `k(β)`; `onto` gives a class over `β`; the other clauses specialise. The text (2340-2346) is the Lean proof.
- `nonempty_classMap_above_lastStep`: `clDown` takes the class of the same decoration with the twist frame forgotten (`extTo (I.Q μ₀)`), empty marked set (allowed by `ysAt_ys_of_ne`), at `Idx.top`. Text 4166-4172. The hypothesis `I.Ok` of the statement is unused.

## 5. Unit status

### 5.1 Z4.2.04

Root cone of `pairOK_allSites`: 10,648 declarations, 54,386 core lines (42,543 theorem lines), no literature leaf. Inside the complete units Z4.2.01, .03, .05: 29,408 lines. Residual: **24,978 lines (23,600 theorem lines)**. (Z4.2.06-.08 are complete but contain this root, so they cannot be subtracted.)

| Part of the residual | Lines / theorem lines | Status |
|---|---|---|
| `translate_entire_algebraic` (= `ThLoc.algTAll`) | 20,441 / 19,402 | Hand proofs of rounds 7 and 8; accepted earlier; not re-audited here. Contains `Base.latAll` (cone 6,055; 2,145 residual) |
| `laFacts_of_adm` outside the previous row | 747 / 695 | Hand-proved this round (rows 1-3), given `LatAll` |
| Finite expansion, finite generation, Osgood (`kerTh_entire_algCoef` outside both rows above) | 805 / 713 | Hand-proved this round (rows 4-7); Osgood (185) is a standard fact to cite |
| Site suppliers outside the `kerTh` cone | 2,985 / 2,790 | See below |

Project-specific pieces that are neither hand-proved in detail, nor confirmed by a review, nor labelled as open:

| Piece | Lean | Lines / theorem lines |
|---|---|---|
| Self-duality of the kernel lattice at a site | `KerSelfDual.isSDLat_latK_of_stdL` with `SDCompan.isSDLat_latK` (1,160), `Comp.glob_one` (500), `isLat_dl_of_isOrthCo` (143) | 1,508 / 1,417 |
| Local span of the kernel lattice as a frame image | `KerSp.locSp_latK_isPt` (`KernelLatticeFirstFactorLatticeTuplePoint.lean`), used by `locSp_kerN_zero`, `locSp_kerN_succ` | 1,885 / 1,753 |
| Union of the two | | **2,136 / 2,004** |
| Own steps of `locSp_kerN_zero` / `_succ` beyond that | `lattice_tuple_bases_span_at_places`, `locSp_reindex`, `gidx_facts` | 146 and 167 theorem lines |
| Datum congruence | `xiM_datLoc`, `moved_pair_datum_eq_adelic_datum`, `datLoc_homRe` | 52 / 37 |

Named-theorem count for information: of the 1,975 theorems in the residual, 134 are named in some chapter (2,678 lines); 20,922 theorem lines are in theorems never named, almost all under the hand-proved `algTAll` block.

**Does the document now cover the root completely? No, not yet.** What stayed open through rounds 7-9 (integral forms on the actual pair, the three quotients, the weights with their Fourier denominator, `S`-integrality, `S`-torsion shifts) is now proved correctly, and the assembly is right. Two things stand between this and closure:

1. `Base.latAll` (and through it rows 2, 3, 7) depends on the `r14:lat` verdict, which is not mine.
2. The two site lemmas above (2,004 theorem lines) are cited, not proved.

**Verdict: CLOSE AFTER LISTED FIXES** (F1-F4). Do not change the grade before F1 and F2 are done.

### 5.2 Z4.3

**(ii) `comb_of_tied` is hand-derived.** Its cone is 15,441 lines; only 187 lie outside the Z4.2.04 cone (`stdOK`, `contDiff_opU`, `U_eq`, rows 9-15 and three small lemmas), and section 3 discusses those named declarations. It is an implication from `AlgTAll` and `t.Hyp`; it supplies neither.

What remains for Z4.3 as a whole:

- **(i) Covariance** (`r14:eq-z43`, `NatEqui.eqP`, 50,356 lines; direct route 24,010): submitted in the same chapter, outside my assignment.
- **Registered application premises** (sizes reproduce from the graph; "outside" excludes the cones of Z4.2.04, Z4.2.13 and the Z4.3 root; the last column also excludes the complete Z4.4):

| Premise | Lean supplier | Cone / theorem lines | Outside | Also outside Z4.4 |
|---|---|---|---|---|
| Duty | `conditions_at_standardKernelComparison_trueColumns` | 42,176 / 30,258 | 21,654 | 12,606 |
| UnUnit | `kernelPairScalars_isUnit_trueColumns` | 18,953 / 8,805 | 8,096 | 992 |
| Stab0 | `stab0_rec7_of_levelData` | 16,041 / 8,338 | 7,179 | 1,139 |
| t.Hyp | `kernelEntries_hyp_of_columnSideProperties` (= `colSide_hyp`) | 14,039 / 6,538 | 2,646 | 2,013 |
| SB | `theta_isometry_facts_hold` | 6,647 / 3,136 | 888 | 888 |
| OrbitParityCond | `orbit_admissible_of_split_bound` | 3,910 / 667 | 73 | 73 |
| Six together | | 47,437 / 35,046 | 26,246 | 16,936 |
| CM2 row service | `servH_row_of_artin` | 380,460 / 339,211 (recorded 380,456) | 295,105 | 247,005; 23 literature leaves |

- **Inputs of the inert-row application that are not on the registered list.** `exists_beFam_evenConditionsInert_of_kerEnt` (cone 36,055; 20,567 lines outside `comb_of_tied` and the three cones above) also consumes:

| Input | Lean | Cone | Outside |
|---|---|---|---|
| Standard-basis integrality | `T.normalisedFamily_standardBases_integrality_alt` (no literature leaf; in no expert unit) | 24,181 | 19,746 |
| Local host `HostAt` | hypothesis; supplied by `KerStd.HostInert.hostAt_inert` in `at_of_true_columns` | 12,188 | 7,317 |
| Standard series conditions | `T.standard_series_b_conditions_large_prime` | 4,536 | 4,536 |
| Standard bases from adapted bases | `T.isStandardBasesLatticeAtPlace_of_adapted_bases` | 4,540 | 650 |
| `t.Adapted` | hypothesis of `at_of_true_columns` | n/a | n/a |

The text mentions these in prose (1267-1281, 1286-1288) and `ch_P.tex:5003-5040` discusses the first; none is in `application_premises`. I did not review that older text. Until they are registered, "seven application premises" understates what the selected-row application assumes.

- The three further callers of `comb_of_tied` (G6) each carry their own cone outside `comb_of_tied` and the base cones: 21,493, 27,565 and 26,985 lines.

## 6. Prioritized fixes

Required before Z4.2.04 is closed:

- **F1.** Obtain the verdict on `r14:lat` (`Base.latAll`) and add `\ref{r14:lat-indices}` at `ch_P_r14.tex:986` and `998`. Rows 2, 3, 7, 12 depend on it.
- **F2.** Give hand proofs, or register as open inputs with sizes, for `isSDLat_latK_of_stdL` and `locSp_latK_isPt` (2,004 theorem lines together). Change 1130-1132 so that it does not read as "established earlier".
- **F3.** Row 3: add the generic step `exp(πi q(x)) = ±1 ⟹ q(x) ∈ ℤ`, so that the text proves `LatIntOfFacts` as stated and not only its CM instance (`ch_P_r14.tex:996-1002`).
- **F4.** Cite Osgood's lemma (or Cauchy's formula on polydiscs) at 1101-1103 and 1223-1225, with `AnalyticOnNhdOfDifferentiableVc.lean:20-32`. State at 1098 that `e` is entire.

For Z4.3:

- **F5.** Define the label `r10:z43-register` or replace the reference at 1289.
- **F6.** Extend the registered premise list with the standard-basis integrality theorem, `HostAt`/`hostAt_inert`, `standard_series_b_conditions_large_prime` and `t.Adapted`, with the sizes above.
- **F7.** Name the three other callers of `comb_of_tied` and the discharging declaration of `AlgTAll` (`torsionTaylorAlgebraic_latticeExists_of_cm`).

Round 13 (labelling only; none blocks the recorded Z4.4 grade):

- **F8.** Name `locMv_of_mem`, `reads_of_locMv`, `admissibleBasePoint_chart_mul_twist`, `underQ_prime_to_bad`, `stepLevel_uloc_eq_of_agree` and the two conjugation statements in 3734-3813.
- **F9.** 3771: say that a representing point exists (`Ok.exists_isPtOf`). 4195: say that the marked set at stage zero is empty (`ClsZero.ys0`). `ch_P_r11.tex:969-972`: name the compatibility of the embeddings with conjugation (`fields_ok.conjE`).
- **F10.** 4214-4236: name `stepZeroFormsIdentification_referenceTuple_eq_self`; say that `tw_chains` uses only `StdF` and that `StdLvC` enters through `tw_chains_std`; name `open_congruence_subgroup_preserves_principal_lattice` at 4161.
- **F11.** Set `proof_recheck` for the nine entries in `status.json` according to section 1.3.

## 7. What was and was not read

Read in Lean (original numbering): `PeriodLatticeFinitelyGenerated.lean` 1-340, 1395-1530, 1640-1831; `XiIndCClass.lean` 10-245; `FirstKernelLawReading.lean` 10-135, 376-480, 560-575; `RepComb.lean` 150-365; `IsSemiChar.lean`; `IsDiscriminantTwelfthRootOfIdealLattice.lean` 60-300; the three top-level files; `SelfDualComap.lean` 140-220; `PStdOK.lean` 100-137; `LinkThetaStatementFamily.lean` 78-106; `AdmissibleKernelSeriesInertPrimeNonConjugateFrob.lean`; `AtOfTrueColumns.lean`; for round 13: `ChartsTupleTrivQ.lean`, `MatchTupleChartMemberChart.lean`, `LocalMoveClassRepIffLocalConditions.lean` 195-339, `ChartLevelTwistTrivialLocalMove.lean` 84-116, `TrueColumnChoiceTwistedChainsFormsClasses.lean` 20-490, `StepQOfReindex.lean`, `DecoStabTrivial.lean`, `InclMulInvMul.lean` 180-440, `CevInjective.lean`, `MemFiCComp.lean` 140-160, `NonemptyClassMapAboveLastStep.lean`.

Not read line by line: the Lean proofs under `translate_entire_algebraic`, `Base.latAll`, `thMoved_mem`, `stdOK`; the six site suppliers of `pairOK_allSites` beyond their top-level proofs; `exists_charts`, `chart_of`, `exists_reference_class_matching_coupling_coset`, `exists_unitaryAdelic_lift_typePrime_reductions`, `exists_penultimateLevel_couplingCosets`, `exists_levelJ_character_eq_member_off_places`, `chart_lastStep_twistBasePoint`, `exists_pt_of_agree`, `conj_unitary_preserves_stdLat_of_ptOf`, `row_inv`. For these I checked the hand argument against the Lean statements only.

## Short summary

- All 15 round-14 declarations match their Lean statements and their hand proofs are mathematically correct. I recomputed the weight `r_{x,y}`, the Heisenberg phase, the three quotients and the integrality argument from the definitions. Nine are confirmed outright; six carry gaps (dependence on `LatAll`, a generic statement proved only at its CM instance, an uncited Osgood step, cited-only site suppliers, unnamed callers, one dangling label).
- All nine round-13 declarations pass at proof level; four need labelling additions only.
- Z4.2.04: **close after listed fixes**. The long-open finite expansion is done. Still needed: the `r14:lat` verdict, and proofs or open-input registration for site self-duality and the frame span (2,004 theorem lines).
- Z4.3(ii): `comb_of_tied` is hand-derived as a conditional implication. Z4.3 stays partial: covariance (i), the seven registered premises (six of them 47,437 lines together, CM2 380,460), and four application inputs that are not yet on the registered list (largest: standard-basis integrality, 24,181 lines).
