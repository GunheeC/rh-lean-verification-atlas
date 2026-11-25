AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

# R23_review

AI review report produced during this project; file names are internal working names.

- Internal source file: `out/R23_review.md`
- SHA-256: `b4255492226a35974a296a52c921ecd647e89d563e56363af91a4239b7c2b82c`
- Report scope: R23 manuscript v3, §3 "The chain in detail" — independent referee report

## Internal report

The report below preserves its original verdict, scope and unresolved points. Superseded graph percentages have been removed from this public edition. Source line numbers in other records count from its original title.

# R23 manuscript v3, §3 "The chain in detail" — independent referee report

Object reviewed: `main.pdf` (341 pp., manuscript v3), §3 on pp. 9–23, with `chain.txt`, `r23_p017.tex`, `R23_pending.json`, `R23_report.md`, the pinned Lean tree `40e56bab` and the dependency graph cache.
Reviewer: an AI model reading cold; I did not write the manuscript. Nothing here is a human or specialist check.
Nothing in this report, and nothing in the manuscript, claims that the Riemann hypothesis is proved. Page 1 of the manuscript says so explicitly, and §11.1 lists all five steps as `pending_review`.

Method.
- Every Lean statement was read through `git show 40e56bab:src/...`, so line numbers are the original ones.
- Every inequality in steps 1 and 2 was recomputed by hand from the Lean definitions, not from the manuscript's wording.
- Sizes were recomputed with my own dominator-tree pass over `graph_cache.bin` (root `allChi`, stop at `lit`, weight = source span of `core` declarations). It gives 9,567,045 core lines and reproduces every "Dominated" figure I compared (B05, B07, B08–B10, T02, D510, D511, D547, D548, D561, D562, D567). "Inclusive" means all core lines reachable from the declaration.
- I did not re-run Lean, and I did not open `r23_budget.tex`, `r23_link.tex`, `r23_host.tex`, `r23_selmer.tex` or `r23_p012.tex` (not supplied); for those steps I read the PDF text.

## 0. Verdict

| Step | Claimed extent | My verdict |
|---|---|---|
| 1. P017 window inequality (pp. 9–13) | full | **CORRECT WITH GAPS.** No error found. Every constant and exponent recomputes. Three inputs are used but neither proved nor displayed as numbered Formal statements (§1.4). |
| 2. LinkN_at and the per-unit bound (pp. 13–16) | full, local | **CORRECT AND COMPLETE as three local implications** (Prop. 3.6 parts 1 and 2, and P021). **WITH GAPS as "Selmer sum into lattice error"**: the inequality that makes a Selmer length bound a local error is a hypothesis, and the bridge from Prop. 3.6 to the `DIV` hypothesis of P021 is narrated, not stated (§2.4). |
| 3. P015 supplyChi / TopG (pp. 17–19) | top-level only | Correct and faithful to the proof terms. Inputs are displayed only as two bundles; at least four suppliers have no statement anywhere (§3.3). |
| 4. P013 Selmer window (pp. 20–22) | top-level only | Correct and faithful. W08–W10 are displayed; six lower inputs are named by locator only (§4.3). |
| 5. P012 definite side and covolume (pp. 22–23) | outline | Accurate. Quantifier order and the max of two thresholds match Lean. Several hypotheses used at each stage are not mentioned (§5). |

- I found **no mathematical error** in §3 and no Lean locator that points to the wrong place (about 70 locators checked while reading; all exact).
- The chapter now answers the three questions R21 said a number theorist could not answer: what the lattice inequality is, where the Selmer sum is carried, and where the exponent 1/2 comes from.
- What the manuscript proves is a **conditional** statement. The precise form is in §6: three large hypotheses (V, F, B) and about twenty Formal statements imply the five goals. The graph places V and the F supplier at 886,201 and 3,679,692 dominated lines respectively. The manuscript supplies a conditional deduction.

## 1. Step 1 — P017, Proposition 3.1

### 1.1 Statement against Lean

| Manuscript (Prop. 3.1) | Lean (`ChebyshevInequalityOnWindows`, `TopWin.lean:26–28`; `level_gm_le_on_family_scales`, `LevelGmLeOnFamilyScales.lean:28–30`) | Match |
|---|---|---|
| level Λ, real e_D, e_L, ε > 0 | `∀ eD eL eps, 0 < eps` | yes |
| family F at ε | `Fm : FamP eps`, core `Fm.toFamCore` | yes; the type `FamP` is not named |
| EFamC(Λ, F) | `∃ C x0, ∀ x ≥ x0, ∀ i, EAtH Λ host TT x eps C` (`TopDefs.lean:13–16`) | yes |
| ∃ K, c_HH, e_K, C_L, x_0: ChainTied at every x ≥ x_0 in Win(F) | `ChebyshevInequalityOnFamilyWindows` (`TopWin.lean:23–24`) | yes |
| ∃ X, ∀ x ≥ X in Win(F): G_Λ(x) ≤ x^{1/2+(e_D+e_L+7)ε} | same, real exponent `1/2 + (eD+eL+7)*eps` | yes |
| X = max(x_0, x_E, B08 threshold) | `max x1 (max x0 xE)` (`WindowInequalityOfArtinInputs.lean:22`) | yes |

Lower declarations.
- `core_gm` (`CoreGm.lean:12–15`): threshold `x1` is chosen from (Λ, e_D, e_L, K, c_HH, e_K, C, ε) before the frame, host and TT. The text says this ("All three thresholds depend only on the fixed constants"). C_L is not an argument of `core_gm`; the manuscript correctly carries it only inside ChainTied.
- `HostAx` is not a hypothesis of Prop. 3.1 in Lean. It is a field of each family member (`host.toHostAx`). Formal statement 3.3 words it as an assumption on the host, which is harmless.
- `tiedCore_of_chainTied` (`LevelGmLeOnFamilyScales.lean:13–26`): translation map `id`, word fibres of `pt(u)`, TT identified by injectivity of the frame coordinate, T2 ⊂ A0 from the digit description at translate 0. The paragraph "Family quantifiers" describes exactly this. One small imprecision: the coverage clause is satisfied on all of the frame group, not only on A0.
- `RankVal` (`PairRowIffQdRows.lean:28–32`): n ∈ [x^{2+8ε}, 2x^{2+8ε}], m ∈ [√(xδ1), 2√(xδ1)], k ∈ [x^{9/2+10ε}, 2x^{9/2+10ε}], and r + t = 8fr + 4 + TOv·nWv. The text quotes the n and m clauses only.
- ASK and MAIN (`FirstPrimeNeSecondPrime.lean:84–91`): the prose in §2 matches. §3 uses both without restating them.

### 1.2 Line-by-line recomputation

| Claim in the text | Recomputed | Lean |
|---|---|---|
| A = √(xδ1) = x^{1/2−ε/16}, m = 2⌈A/2⌉, A ≤ m < A+2 ≤ 2A for A ≥ 2 | Correct. For x ≥ 16 and ε < 1/52, A ≥ 16^{0.498} > 3.9. | `exists_even_between`, `ExistsRanksRankValFrame.lean:10–15, 63–75` |
| x^{1/2−ε} ≤ m ≤ x^{1/2+ε/2} once x^{9ε/16} ≥ 2 | 2x^{1/2−ε/16} ≤ x^{1/2+ε/2} ⇔ 2 ≤ x^{9ε/16}. Correct. | used as `w7` (ErrWindows) and RestSize clause 4 |
| \|G_ξ(x)\| ≤ x(log x + C_d + \|ℓ(ξ)\|) | From G_ξ(1) = ℓ(ξ): (x−1)(log x + C_d + \|ℓ\|) + \|ℓ\| ≤ x(…). Correct. | `triv`, `ChCore.lean:167–179` |
| three per-character costs ≤ A_1·s·e with s = x^{1/4}, e = x^ε | log x ≤ 4s; log(x+1) ≤ log 2 + log x ≤ 5s; x^{−1+ε}·x = e. Kept: 5s + C_d + \|K_o\| + \|M\|(4 + C_d + \|K_o\|)se. Discarded: 5s + C_d + 4\|C_E\|s. Principal: C_d. All ≤ A_1 se. Correct. | `r1, r2, r3`, `ChCore.lean:403–418` |
| band cost ≤ n_T s²e, "hence also at most 4n_T x^{1/2+ε}" | \|A\| ≤ M and \|M\|A_1 ≤ s give \|A\|·A_1 se ≤ s²e = x^{1/2+ε}. The factor 4 is slack; 1 suffices. Correct. | `hY`, `ChCore.lean:427–439` |
| thick place cost ≤ 3(x+1)(η+1) | 3a_t/min(w,b)·\|w−b\| = (3a_t/b)(w−b) ≤ 3(x+1)(η+1). Correct. | `th_le`, `ChCore.lean:114–123` |
| thin place: a_t/w ≥ X′/3 | (X′/3)·w ≤ (2/3)X′b′ ≤ (2/3)xb ≤ (x−1)b ≤ a_t ⇔ x ≥ 3. Correct. | `ChCore.lean:126–130` |
| 2f[3(x+1)(η+1) + (x+1)bθ] ≤ 2b/x | CostWindows: 6f(x+1)(η+1) ≤ b/x and 2f(x+1)θ ≤ 1/x. Sum is 2b/x. Correct. The count "f places, 2f characters, normalisation 1/f" is right because \|E_0 × H\| = 4n = 2f. | `hK`, `ChCore.lean:296–301`; `SChain.lean:50–51` |
| −e_1(s+u−t) = e_1(t) + (0,−s) + (0,−u); average over A_0 gives b(δ_2/2)Σ_{ξ∈A} | In (Z/2)², −(1,0) = (1,0). Factor b·n_2/f = b·n_2/(2n). Correct. | `sum_A`, `sum_Th`, `ChCore.lean:28–73` |
| n_T m b (δ_2/2)(G − 4x^{1/2+ε}) ≤ E + 2n_T m b/x | Correct. | `core`, `ChCore.lean:283–338` |
| Lemma 3.4, term 1: a_E/(mb) ≤ 2x/m ≤ 2Y | a_E ≤ 2xb, x/m ≤ x^{1/2+ε} = X ≤ Y. Correct. Only use of the lower bound on m. | `SZ.T1` |
| term 2: a_E m/(bk) ≤ 2xm/k ≤ 2Y | xm ≤ k gives ≤ 2, and 2 ≤ 2Y. Correct, with large slack. | `SZ.T2` |
| term 3: 2(n/t)m x^ε ≤ 4Y | n/t ≤ 2x^{ε/8}; exponent ε/8 + 1/2 + ε/2 + ε = 1/2 + 13ε/8. Correct. Only use of the upper bound on m. | `SZ.T3` |
| term 4: r k x^{2ε}/(n²t) ≤ 2x^{1/2+9ε/8} ≤ 2Y | k ≤ n²x^{1/2−ε} and r ≤ n give (n/t)x^{1/2+ε}. Correct. | `SZ.T4`, `LipschitzWeightAndMinimum.lean:84–113` |
| Err/Q ≤ 10PY; δ(G − 4X) ≤ 22PY | 2(10PY + 2/x) = 20PY + 4/x and 4/x ≤ 2 ≤ 2PY for x ≥ 3. Correct. | `LipschitzWeightAndMinimum.lean:561–569` |
| G ≤ 4X + 22PYx^ε ≤ 26Z, Z = x^{1/2+(C+21/8)ε} | PYx^ε = x^{Cε + 1/2 + 13ε/8 + ε} = Z; X ≤ Z. Correct, including the case G − 4X ≤ 0. | lines 570–589 |
| 26Z ≤ x^{3ε/8}Z = x^{1/2+(C+3)ε} | 21/8 + 3/8 = 3. Correct. | lines 584–592 |
| C = max(e_D+e_L, 0) + 3 becomes e_D + e_L + 3 | 0 ≤ e_Div ≤ e_D and 0 ≤ e_Loss ≤ e_L hold whenever a host exists. Correct, and the text handles this point. | `CoreGm.lean:46–47` |
| G_Λ ≤ x^{1/2+(e_D+e_L+6)ε} + 4o·x^{1/2+ε} ≤ x^{1/2+(e_D+e_L+7)ε} | (C+3) = e_D+e_L+6; omitted characters: at most 4o of them, each ≤ x^{1/2+ε}; 1 + 4o ≤ x^ε. Correct. | `CoreGm.lean:61–74`, `sigA_le` |
| thresholds | B09: max(3, [26 ≤ x^{3ε/8}], [\|M\|A_1 ≤ x^{1/4}]). B08: that, plus LargeX, plus 1 + 4o ≤ x^ε. Proposition: max with x_0, x_E. All independent of the host because C_d is absolute. Correct. | `ChCore.lean:352–359`, `CoreGm.lean:21–26` |

### 1.3 Where the exponent 1/2 comes from

The text's account (a cost of order x divided by m columns, against a cost proportional to m) is right for terms 1 and 3. It is incomplete for term 4, whose x^{1/2} comes from the separate size hypothesis k ≤ n²x^{1/2−ε} in RestSize. With k ≈ x^{9/2+10ε} and n ≈ x^{2+8ε} this holds with room, but it is a third, independent source of the exponent and the "column scale" paragraph does not mention it.

### 1.4 Gaps

1. **The balance identity ASK − MAIN = De** (`ch_balance`, `ChBalance.lean:200–260`; dominated 582, inclusive 670 lines). It is displayed in one sentence under "Averaging over the translates", with a locator, and then used. It is not proved and is not a numbered Formal statement. This is the step where primes enter the lattice inequality. I checked informally that it is the expected finite Fourier computation (orthogonality gives 2·[i·Frob_p = g]; the ℓ(ξ) terms survive only for ξ ∈ {0, χ_C}), so I expect it to be fillable in under a page.
2. **The weight increment bound** \|wG_ξ(A/w) − bG_ξ(A/b)\| ≤ 3A\|w−b\|/min(w,b) (`lipschitz_weight_all`; dominated 177). Same status: displayed inline, not proved, not numbered. I did not verify the constant 3.
3. **The identification of T(u,t) with the thick part of De.** "Write both sums on the same translated complement of Φ. A thick place there is indexed once by s ∈ T_2" is an assertion. The maps `partner`, `thickPl`, `topPl` and the predicate `IsThickAt` are never defined in §3, so a reader cannot check it. In Lean this is `hTh` and `CR.De_re` inside `th_le` (dominated 276).
4. **Formal statement 3.3** (D547 242 lines, D548 203, D549 51, D562 270) is supported by a five-line sketch. D547 is the dictionary between host characters and the level's primitive characters; the sketch is plausible and matches `charsA`, `gmA_eq`, `sigA_le`, but it is not a proof.
5. **D567** (`errX5at_le`, 289 lines) and **D014** (`hostFactsS`, 130 lines) are inputs. D567 is displayed in 3.2. D014 is cited by label only; its statement is in Appendix G.16.
6. **The bracket B is never displayed in §3.** Lemma 3.4 says "Expand Br". The reader must go to Formal statement 5.9 on p. 39.
7. The manuscript's entry for P017 on p. 59 still reads "Lean only", and B08–B10 on pp. 38–39 read "Lean only", while §11.1 says "Full". The "Round 23 candidate" note explains this, but the two labels disagree on the page.

Is every hypothesis either a displayed Formal statement with a Lean location, or proved? Almost. Items 1–3 are neither.

Verdict: **CORRECT WITH GAPS** (items 1–5).

## 2. Step 2 — LinkN_at, Proposition 3.6 and P021

### 2.1 Statement against Lean

| Manuscript | Lean (`GlobalTheoremInputs.lean:31–47, 59–63`) | Match |
|---|---|---|
| v_ℓ = log ℓ · Σ_{1≤e<t} shaLen_D(ℓ, e) at primes, 0 otherwise | `vvTerm`: rational lengths over `Finset.Ico 1 D.R.t`, times `Real.log l` | yes |
| E_j = Σ_{w∈S_w} λ_w e_w η_j(w), S_w = support places with μ(w) ≠ μ_0 | `etaSum` | yes |
| LinkN_at: (v_ℓ) summable ⇒ E_j ≤ d_j(C·A_x + Σ v_ℓ), A_x = f m b L² + (log x)² N_c | `LinkN_at` | yes |
| L = x^ε, b = exp L | `Scale.L`, `Scale.b` (`DataParams₂.lean:31–33`) | yes |
| family version: one C, one threshold, finiteness assumed before quantifying over lifts | `LinkN`: `∃ C x0, ∀ x ≥ x0, ∀ i, ShaFinOdd → ∀ j ∈ lifts` | yes |
| conclusion E_j ≤ D_0(\|C\|+1)x^ε(B_0 + N_c) | `DIVinN_at L j (|C|+1)` | yes |
| P021: eleven hypotheses ⇒ ASK(u_0) ≤ Main(u_0) + ErrX5at(u_0) | `PointwiseBoundVariant` (`QuotientSlopeBoundsWith.lean:72–75`): HidaSetting, DIV, EComp5, HComp, Count5, Slopes, QuotientSlopeBoundsWith, LossBounds, SlopeIneq, HHBound, FParams | yes, eleven and in this order |

### 2.2 Proposition 3.6

Part 1 (pointwise link, C = 2000(\|c\|+1)³).
- Per-prime bound d_j log ℓ·(ν_ℓ + 2/ℓ² + λ^G_ℓ + VVr(ℓ) + ord_ℓ H + ord_ℓ M): matches `hper` in `etaSum_le` (`MemPrimesOverOfMem.lean:578–603`).
- Table sums 2T, 8cX, 4cX, 1000(c+1)³X, 1164000T with T = (c+1)²U^18, U = x^{c+2}exp(x^{ε/4}): match `sum_g`, `sum_23`, `sum_qd`, `sum_small`, `sum_exc`. 20T matches `glob_le`; 4·10⁶T ≤ b matches `big_le_b`.
- (20 + 2 + 1164000)T ≤ 4·10⁶T ≤ b ≤ X, then X + 12cX + 1000(c+1)³X ≤ 2000(c+1)³X because 1 + 12c ≤ 1000(c+1)³ for c > 0. Correct, and identical to `point_bound` lines 965–996.
- "The first applicable branch is bounded by the sum of the nonnegative envelopes" is exactly `hpt`.

Part 2 (family error).
- Partial sums of v_ℓ are bounded by √b after filtering non-primes; so the series is summable with total ≤ √b. Matches `vvRecord`.
- √b ≤ b ≤ B_0 = f m b y with y = x^ε ≥ 1; f m b L² = y·B_0; (log x)²N_c ≤ y·N_c. So E_j ≤ D_0{\|C\|y(B_0+N_c) + B_0} ≤ D_0(\|C\|+1)y(B_0+N_c). Correct; matches `divinN_at`.
- Threshold: max of the three family thresholds, x_1 + 1, and a point beyond which (log x)² ≤ x^ε. Matches `divinN_of_hypV`.

Transfer from the cut family: the extra d_j log M with log M ≤ C_1 x^{C_1} L ≤ C_1 A_x, constant C + C_1. Matches `linkN_of_gd` (`LinkNOfGd.lean:46, 59–93`).

### 2.3 P021 (Formal statement 3.7 and its proof)

I re-derived every line from the Lean definitions.
- Lower quotient slope plus DIV, F_o cancels: μ_N − h ≥ μ_M + G_a + μ_CC − E_e − Lo − S_Div + A log T − E_Div. Correct.
- Main-term identity S_Div − AΛ + mA·lg = Main + A·c_Count(L_a + m²L_a/k): the two terms ∓mA log(π/v) cancel. Correct; it needs f > 0, which is in HidaSetting and not mentioned.
- K_0 and the averaged lower bound G_a + μ_CC − Main − K_0 − ⟨Lo⟩ ≤ s. Correct.
- Spread: μ^max_M(u) − μ_M(u′) ≤ c_S n_T a L_a(2 + m/k); the two E_e errors 2m c_E B_0; height comparison c_H(n_T a L_a + m B_0); A·c_Count log k; upper quotient error c_Sl1 m B_0. So 0 ≤ u_F ≤ K_3 + ⟨Lo⟩. Correct; matches `Vvar_bound5`, `u_function_le_mean`.
- z log(1 + H′/z) ≤ z log(1+X) + (H′ − zX)/(1+X) ≤ (z + b) log(1+X): from log t ≤ t − 1 at t = (1 + H′/z)/(1+X), then H′ ≤ Xb and X/(1+X) ≤ log(1+X). Correct; matches `phi_bound`.
- Final error K_0 + log\|W(u_0)\| + LoP + M + (1−δ̄)^{-1}[4 log(1+X)(K_3 + M + b) + (η̄ + 4√ē)Xb] equals `ErrX5at` term by term, with UBar5 = K_3 + MLo5.

### 2.4 Gaps

1. **The Selmer term enters through a hypothesis.** The per-prime inequality that carries VVr(ℓ) is clause 4 (`ArchimedeanSignatureMatching`) and clause 16 (`GeneratorPrimeEtaBound`) of the 17-clause table predicate `AdmT` (`ResidueCharacters/TwistedPlaces.lean:239–242`). §3.2 shows how that term is carried, summed over primes and absorbed. It does not show why a localisation-kernel length bounds η_j. That content sits under D427 (dominated 205,214; inclusive 393,278) and D421 (150,531). The section title "From the Selmer sum to the lattice error" promises more than this.
2. **Formal statement 3.5 is a bundle** of ten Lean lemmas (`etaAt_le_g`, `etaAt_le`, `loc_le_lamB`, five sums, `glob_le`, `big_le_b`). `AdmT` is named but its 17 clauses are not listed. `gset` ("designated set"), `lStar` ("cutoff"), η_j(w), λ_w and "retained lift" are not defined in §3.
3. **The bridge from Prop. 3.6 to P021 is prose.** DIVinN becomes the `DIV` hypothesis of the lattice record through LinkDIVt (D481, dominated 5,437; inclusive 42,336) and LinkGLOBAL (D479, dominated 11,198; inclusive 191,128). The paragraph "Which assumptions pass to the slopes?" names them. Neither is displayed in §3, and the text does not say how x^ε(B_0+N_c) becomes c_Div·m(B_0+N_c)x^{e_Div ε}.
4. `sha_eq` (the record equality identifying extended lengths with rational summands) is used and cited, not stated.

Verdict: the three implications are **CORRECT AND COMPLETE** under their displayed hypotheses. As a derivation of the lattice error from the Selmer bound the step is **CORRECT WITH GAPS** (items 1 and 3).

## 3. Step 3 — P015: Propositions 3.8 and 3.10

### 3.1 Proposition 3.8 (supplyChi)

Statement: matches `HostExW (3/2) (GChi ψ).req` (`SupplyChi.lean:8–9`, `ThinScalesIffHostBound.lean:120–123`, `Supply.lean:42–43`), including C_5 = 4, C_8 ≥ 1, c_6, C_b > 0, and the budget √(exp(x^ε)).

Proof, against `winPairs` and `supplyOfAdmOf`:
- a = 2 + 8ε, k = c^{1/a}, W ≥ max(1, k³, k^400), Z = kW; for Z ≤ x ≤ Z^{3/2}, x ≤ W² because k³ ≤ W; u = x/k ∈ [W, W²]. Correct (`WinPairs.lean:23–57`).
- x^a ≤ c·2^{e(u)} ≤ 2x^a; x^400 = k^400 u^400 ≤ u^401 because k^400 ≤ W ≤ u; exp(u^ε) ≤ exp(x^ε). Correct (lines 64–81).
- C_0 ≥ max(1, J, Λ.o, 8M); threshold with x > c·2^{e_0} and Y^{ε/5} ≥ max(5, 4M). Correct (`supplyOfAdmOf.lean:30–50`).
- Q_S ≤ 4M·c·2^e ≤ 8M x^a ≤ C_0·R.n. Correct (lines 100–109).
- q ≠ 3 from log q > Y^{ε/5}/2 ≥ 5/2 > log 3. Correct.
- EAtH assembled from o-equality, kept data, exceptional character, shares, and the two bounded-character estimates. Correct (line 128).

The "at least half" step: `pair_share` is applied with exceptional fraction η = 1/2, modulus 8M and tolerance ε/2 (`pairEx.lean:116`, `PairExists.lean:15`). (1 − η)\|P\| ≤ \|G\| with \|P\| > 0 gives a nonempty G_1, then a nonempty G_2(q) for the chosen q. The pools are as described: primes q ≡ 3 (mod 8) in (e^{z/2}, e^z]; primes d ≡ 7 (mod 16) in (e^{z′/2}, e^{z′}] with q·∏_{3≤p≤z} p dividing d + 1. The positivity of the pools is part of `pair_share`'s conclusion and the text displays it.

The share constants λ_γ = 4/(3o+1) on A_0 and 3/(3o+1) elsewhere match `Frame.lam`; they sum to 1 over the o cosets and give the coefficient c = 1/(3o+1) used in step 1.

### 3.2 Proposition 3.10 (TopG)

- Statement matches `TopG` and `FamilyClassConnected` (`ZeroFreeAllOfTopG.lean:12–14`, `DivinNOfHypV.lean:13–15`).
- Constants (C_abs, C_0, e_D, e_L) = (2, 3, 2, 0): matches `topDesWin … 2 3 2 0` (`TopShape.lean:52`). So the exponent delivered to step 1 is 1/2 + 9ε.
- The nine conditions are `hN, hDIV, hEta, hIRR, hZ, hRk, hG, hS, hGL` (`DesWin.lean:14–22`), intersected as `hN.and (hDIV.and (hEta.and …))`. `Closed.and` takes the minimum of the ε-thresholds and the componentwise supremum of the largeness parameters; the text says exactly this.
- Order of use: design at the common largeness parameter; HypV from the request; DIVinN from HypV, N and the rank equality; LinkDIV from LinkDIVt with LinkEta and DIVinN; LinkMu from the two rank statements with the size bounds and LinkDIV; then the global implication with (LinkG, LinkS, LinkIRR, LinkDIV, LinkMu). Matches lines 23–31.
- The application at λ = 3/2 with G_ψ: HypV after x_1 + 1 and EFamC with constant 4 match `hypV_of_cls`, `eFamC_of_cls`.

### 3.3 Are the inputs displayed?

Only as two bundles (Formal statements 3.9 and 3.11).
- In 3.9, `pairEx` (dominated 17,613; inclusive 26,640), `fieldChi` (3,104; 6,384), `boundedTw`, `isChiField` and `pairHyp` are described in prose "inside D510" and have no statement of their own. `hostOfField` is D511 (10,024; 41,613); the text refers the reader to the source for "the precise divisibility and positivity conditions".
- 3.9 hides the main analytic content of the host: for the selected primes, every character induced by a nontrivial twist satisfies \|G_χ(y)\| ≤ y^{1/2+ε/2} for Y ≤ y ≤ X. The text mentions this in half a sentence ("the primitive inducing characters' bounds").
- In 3.11, the supplier of `hZ`, `link_alt_alt_alt` (dominated 122; inclusive 45,303), has no D-label and no statement in the manuscript. The same holds for `selection_closed_of_wu_decay_alt` (347; 128,020) and for `goal_of_shape_of_hyps`, which maps the fields of the HypsAlt record to about sixty arguments of the shape theorem (9; 63,925). B05's disjoint share is 125,197 of its 146,214 dominated lines, so most of B05 is not allocated to any listed entry.

## 4. Step 4 — P013: Proposition 3.12

### 4.1 Statement

Matches `VWinAt ψ 401` (`ExistsPageN.lean:44–47`): 0 < ε < 1/52; any page function with x^{2+8ε} ≤ 2^{s(x)} ≤ 2x^{2+8ε}; J′ ≥ 1 and X_0; every `WinPair` at X^{1/J′}; Y with X^{1/J′} ≤ Y and Y² ≤ X; t = ⌊x^401⌋; all fields of type IsChiField; finiteness for 1 ≤ k < t; every finite prime set, including 2; bound √(exp(x^ε)) = exp(x^ε/2).

### 4.2 Proof

- The chain `vwin_of_row` → `automorphic_window_of_inputs` → `v_window_of_depth_zero_residual_bc_cm` → `v_window_of_literal_automorphy_n` → `vwin_of_hypotheses_H_E_alt` → `Core.of_four_alt` → `vwin_of_counts` is as described. The record patched with `descWeak`, the K-bound from its rank-n field, W08 with the two-twist Kato and unramified-automorphy fields, W09 for II and III, W10 with the second component of the end data: all match `WindowBoundOfLiteratureLevel.lean:25–31`.
- Counts I, II, III, V are the four hypotheses of `of_four_alt`. The auxiliary cases are Vs (`countVs`, from Poitou–Tate, local finiteness, local duality and C_K), IV (`countIV`, no hypotheses) and Z (`countZ X.propZ`). Matches `JointWinOfCounts.lean:16–18` and `HVCore.lean:18–22`.
- Case split: I, Z, II, III for odd ℓ ∉ B_χ; II, IV, V for ℓ ∈ B_χ. Matches `HV.cases` (`Cases.lean:8–12`), which I read in full.
- Uniformity in the prime set: C = C_0 + D + b + bD. For u ≥ 2, u^{C_0} + b·u^D ≤ (1+b)u^{C_0+D} ≤ 2^b u^{C_0+D} ≤ u^C, and bDB ≤ CB. Correct; matches `HV.point` (`PointArith.lean:47`).
- Interval: J′ = max(1, J); log(qd) ≤ z^{ε/4} = X^{ε/(4J′)} ≤ X^{ε/(4J)}; q, d > 2X^401 + 1 and above the fixed thresholds eventually; X_0 ≥ max(X_J, X_B, L^{J′}). Matches `vwinAt_of_joint` lines 51–94. The text omits X_B from the displayed maximum.
- Sum of budgets: B(x) log 2 + K exp(8x^{ε/4}) + u^C + C·B(x) with B(x) = exp(x^{4ε/5}) and log u ≤ 2x^{ε/4}. Each term is at most a constant times exp(max(1, 8, 2\|C\|)x^{4ε/5}), whose logarithm is o(x^ε). So the total is ≤ exp(x^ε/2) for large x. Correct; matches `vvle_of_parts` and `error_terms_le_sqrt_exp_rpow`.

### 4.3 Are the inputs displayed?

- W08, W09, W10 are displayed in Formal statement 3.13 and match `CountI`, `CountII`, `CountIII`, `CountV` (`Counts.lean:53–69`) and the case predicates. `VLe` includes the factor log ℓ, as the statement says.
- W12, W14, W15, W02, W03, W05 are cited by label; their statements are elsewhere in the manuscript.
- `countIV` (dominated 354; inclusive 7,205), `countVs` (306; 9,316), `sumIn` (1,250; 10,156), `sumOut` (265; 8,435), `ML.iv` and `vvle_of_parts` (161; 746) are named with locators and described in a sentence each. They are not displayed statements. The predicates `LayerLe`, `plusLen`, `minusBound`, `Big` are not defined in §3.
- `ends0_alt` (P024; dominated 4,505; inclusive 1,154,954) supplies both the unramified-automorphy input to Count I and the input to Count V. The proof mentions "the end-data bound" without saying this is P024.

## 5. Step 5 — P012: Formal statements 3.14 and 3.15

- **Quantifier order of the covolume bound.** `CovolumeBoundOfX := Closed FamHyp fun Fm CH => ∃ C0, 0 ≤ C0 ∧ EventuallyAtAllPoints Fm (… ∀ C, C0 ≤ C → (p.S false).L3 (p.N C CH))` (`LiftLambdaBound.lean:60–61, 17–19`). Unfolded: ∃ ε_1 > 0, ∀ 0 < ε ≤ ε_1, ∃ K, ∀ F, H with FamHyp(F) and F.Large(K, H), ∃ C_0 ≥ 0, ∃ x_0, ∀ x > x_1(F) with x ≥ x_0, ∀ ι, ∀ p with RowsTAlt, ∀ C ≥ C_0, ∀ j, lcv(S.XW_j, S.M_j)/S.D ≤ (p.N(C,H)).l3_j. Formal statement 3.14 has exactly this order, including "≤ ε_1" and S = p.S(false).
- **Fifteen inputs.** The list matches the fifteen arguments of `topCovolSlim2_use_alt_alt` (`TopCovolSlim2Use.lean:16–17`) in order. The first eight feed `deep_slim_use` (T14). The two geometric records, the six Hodge-record fields q6, q8, q13, q7, q10, q12, and the seven premises of T15 match lines 18–22 and `TopCovolG.lean:39`.
- **Max of two thresholds.** `CF1` from `evaluation_grid_of_join` and `CF0` from `rowFun_at_gridA_alt`; c = max(CF0, CF1); `hEv` uses c ≥ CF1, `hFun` uses c ≥ CF0; the same c enters `hOpen1`, `hL3` and `hN c` (`SiegelEisensteinSecondTermHypotheses.lean:52–68`). The outline's C_1, C_0 and "one c for all conditions" are right.
- Statement 3.15 matches line 44 argument by argument.

Omissions, acceptable in an outline but worth one sentence each:
- The functional condition (D036) and the row bound (D041) each also use five fields of P (discrete-series cover, Harish-Chandra modules, cusp rapid decay, Casselman–Wallach, ray class field).
- T10 also uses the lower bound λ_low from `ontoX_and_lamLow`.
- Row rationality also uses the Siegel-set, real Howe duality, Green-cuspidal, join and functional-equation fields.
- The evaluation grid also uses twisted Weil convergence, the twisted local-factor match and the twisted square theta identity.

## 6. End to end: what is now derivable by hand

### 6.1 Answer

Yes, with one qualification. §2, §3.1–§3.3 and the Landau window theorem of §6.4, together with P014, P016, P018, P019 and the reductions of §6.1 (all "Proved here (full)" and reviewed earlier), give a derivation a reader can follow of

> **V + F + B + the Formal statements listed in 6.2 ⇒ the five goals P001–P005.**

- V is the Selmer window `VWin` (every primitive ψ, exponent 401).
- F is `Nonempty (HypsAlt (Closed … LinkN) DefiniteSideCondition)`.
- B is Green's finite-field character input.

The qualification: "Selmer window + listed Formal statements" is not enough by itself. F is a second hypothesis of the same order of magnitude as V, and it is where LinkN (the statement that consumes the Selmer bound) is supplied. §3.4 and §3.5 do not reduce V or F to anything a reader can check; they describe the top of their Lean proofs.

The derivation runs:
1. Goals ⇐ H (every character) by change of level and the functional equation (§6.1, P006–P009).
2. H ⇐ zero-freeness for primitive characters (P014).
3. That ⇐ TopG and HostExW(3/2, G_ψ) for all ψ, using P017, formB and P019 (P016).
4. formB ⇐ the Landau window theorem (P018, P022, P023).
5. P017 ⇐ list A below (Prop. 3.1).
6. HostExW ⇐ V and list B (Prop. 3.8).
7. TopG ⇐ B, F and list C (Prop. 3.10).

The exponent reaching the Landau step is 1/2 + 9ε (e_D = 2, e_L = 0).

### 6.2 The Formal statements the derivation rests on

Sizes are core lines: dominated / inclusive. Dominated counts only what no other route reaches, so it understates shared material; inclusive counts everything reachable and overlaps between rows.

Hypotheses.

| | Declaration | Dominated | Inclusive |
|---|---|---|---|
| V | `VWin`, proved in Lean by P013 `vwin_of_row` from the polarised row | 886,201 | 1,724,828 |
| F | T02 `nonempty_hyps_definite_side_of_closed_bound` | 3,679,692 | 5,646,411 |
| B | `GreenBridge.green_of_regular` | 280 | 370 |

List A — for Proposition 3.1 (P017 itself: 3,365 / 11,483).

| Label | Declaration | Dominated | Inclusive | Status in §3 |
|---|---|---|---|---|
| D547 | `gmA_eq` | 242 | 1,045 | displayed (3.3), sketch |
| D548 | `charsA` | 203 | 919 | displayed (3.3), sketch |
| D549 | `sigA_le` | 51 | 700 | displayed (3.3), sketch |
| D562 | `derivative_integral_all` | 270 | 341 | displayed (3.3) |
| D567 | `errX5at_le` | 289 | 398 | displayed (3.2) |
| D014 | `hostFactsS` | 130 | 564 | label only |
| D550 | `large_x_eventually` | 13 | 15 | label only; elementary |
| — | `ch_balance` (ASK − MAIN = De) | 582 | 670 | inline sentence |
| — | `lipschitz_weight_all` | 177 | 244 | inline sentence |
| — | rewriting inside `th_le` | part of 276 | 343 | asserted |

Proved in the text and therefore not in the list: D561 `core` apart from the three rows above, D563 (Lemma 3.4), D564, D565, D566, D568–D570 and P021.

List B — for Proposition 3.8 (B07 `supplyChi`: 31,622 / 66,017).

| Label | Declaration | Dominated | Inclusive |
|---|---|---|---|
| in D510 | `QH.pairEx` (with `pair_share`, `pair_exists`) | 17,613 | 26,640 |
| in D510 | `fieldChi` | 3,104 | 6,384 |
| in D510 | `boundedTw`, `isChiField`, `pairHyp` | 51, 47, 29 | 253, 128, 42 |
| D511 | `hostOfField` | 10,024 | 41,613 |
| D513 | `exists_ranks_rankVal_frame` | 81 | — |
| D515 | `admissibleClassesTwistedChar` | 112 | 458 |

List C — for Proposition 3.10 (B05 `shape_closed_link_n_of_green`: 146,214 / 616,449).

| Label | Declaration | Dominated | Inclusive |
|---|---|---|---|
| D483 | `designExists_of_tuSize_aux4n_litThin` | 1,749 | 36,881 |
| D479 | `link_gl` (rank statements and global assembly) | 11,198 | 191,128 |
| D481 | `closed_linkDIVt_of_closed_bridge_kernel` | 5,437 | 42,336 |
| D480 | `wire_sel_alt` | 5,644 | 74,597 |
| D482 | `link_brest_alt` | 2,204 | 344,189 |
| B06 | `closed_family_admissible_twist_link_alt` (D516–D518) | 21,017 | 65,731 |
| D484 | `link_alt_alt_bis` (LinkS) | 1,314 | 130,614 |
| D485 | `closed_linkEta_of_duty` | 1,143 | 26,383 |
| D486 | `closed_linkIRR_of_join_count` (uses B) | 773 | 36,291 |
| D489 | `closed_linkG_of_duty` | 13 | 252,591 |
| none | `link_alt_alt_alt` (small-level rank equality) | 122 | 45,303 |
| none | `selection_closed_of_wu_decay_alt` | 347 | 128,020 |
| none | `goal_of_shape_of_hyps` | 9 | 63,925 |

Inside F, the statement that consumes the Selmer bound is D427 `linkN_of_twGood_galoisPreconditions` (205,214 / 393,278), with D421 (150,531) beneath it.

### 6.3 The honest statement

The manuscript proves, by hand and subject to review: if V, F and B hold, and the Formal statements of lists A, B and C hold, then L(s, χ) ≠ 0 for Re s > 1/2 (with the pole exception), and the five goals follow. Lists A–C are Lean theorems, not conjectures, but the manuscript gives no written proof of them. V and F are also Lean theorems (given the polarised row and the literature records); for them the manuscript gives a top-level description (V) or an outline (F). Nothing in the manuscript establishes V, F or the row by hand, and the manuscript says so.

## 7. Top 10 fixes

1. **Prove or number the balance identity.** Add a lemma "ASK − MAIN = De" with the half-page Fourier proof, or make it a numbered Formal statement with its 582 lines. It is the one place where primes enter and is currently a subordinate clause.
2. **Define the thick/thin apparatus in §3.1** (`partner`, `thickPl`, `topPl`, `IsThickAt`, De) and prove that T(u,t) is the thick part of De with frozen widths. Without it the "finite-group average" paragraph cannot be checked.
3. **Display the bracket Br in §3.1** next to Lemma 3.4, and restate ASK and MAIN there. Add to the "column scale" paragraph that term 4 takes its x^{1/2} from k ≤ n²x^{1/2−ε}, and quote the k clause of RankVal.
4. **Say in §3.2 where the Selmer length is actually used.** State clauses 4 and 16 of `AdmT` as displayed hypotheses and say that the inequality "localisation length bounds η" is assumed there and supplied under D427/D421. Retitle the section or add this sentence to its first paragraph.
5. **Display LinkDIVt and LinkGLOBAL as Formal statements in §3.2** (D481, D479), with the clause of `LinkDIV_at` that becomes `DIV`, so the passage from Prop. 3.6 to P021 is a stated implication.
6. **Split Formal statement 3.5** into the local inequalities and the table sums, list the 17 clauses of `AdmT`, and define `gset`, `lStar`, η_j(w), λ_w and "retained lift".
7. **Split Formal statement 3.9** and state `pairEx` separately, with its conclusion that twisted characters satisfy \|G_χ(y)\| ≤ y^{1/2+ε/2} on [Y, Y^J]. Give `fieldChi`, `boundedTw` and `isChiField` their own statements and sizes.
8. **Give entries to the unlabelled suppliers of TopG**: `link_alt_alt_alt`, `selection_closed_of_wu_decay_alt`, `goal_of_shape_of_hyps`. Say in 3.11 that B05 keeps a 125,197-line internal remainder.
9. **In §3.4, display Count IV, Count Vs, `sumIn`, `sumOut` and the minus bound** as statements, define `LayerLe`, `plusLen`, `Big`, name P024 as the source of the end data, and add X_B to the displayed threshold.
10. **State the conditional theorem of §6.1–6.2 of this report in the manuscript**, at the head of §3 or in §11.1, with V, F, B and the three lists. Reconcile the status labels: P017 and B08–B10 read "Lean only" in §5–§6 and "Full" in §11.1.

Smaller points.
- §3.1, "Family quantifiers": coverage holds on the whole frame group, not only A_0.
- §3.1: "at most 4n_T x^{1/2+ε}" — say the factor 4 is slack.
- §3.2, proof of 3.7: mention f > 0 in the main-term identity.
- §3.5: add the omitted hypotheses listed in §5 of this report.

## 8. Limits of this review

- I checked statements and top-level proof terms against Lean. I did not read the proofs of the Formal statements in lists A–C, and I did not re-run any Lean check.
- For `ch_balance` I checked the identity informally, not line by line. I did not verify the constant 3 in the weight increment bound.
- Steps 3–5 were checked for faithfulness to the Lean assembly. That says nothing about the correctness of what is assembled.
- Sizes come from my own pass over the supplied graph cache; they agree with the manuscript wherever both exist.
- This is an AI review. It is not a substitute for a specialist reading.

## Summary

- No error found in §3; every inequality, constant and exponent in steps 1 and 2 recomputes, and the theorem statements match Lean hypothesis by hypothesis.
- Step 1 is correct with gaps: the balance identity, the weight Lipschitz bound and the thick-place rewriting are used without proof or numbered statement.
- Step 2's three implications are correct and complete, but the Selmer length enters through an assumed table clause and the bridge to P021 is prose.
- Steps 3 and 4 are faithful top-level accounts; step 5 is an accurate outline with the right quantifier order and threshold choice. Their inputs are bundled, and several have no statement.
- The manuscript now supports a checkable derivation "V + F + B + lists A, B, C ⇒ five goals". V and F dominate 886,201 and 3,679,692 of 9,567,045 core lines and are not derived by hand.
