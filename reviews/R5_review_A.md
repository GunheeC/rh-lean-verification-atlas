AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

# R5_review_A

AI review report produced during this project; file names are internal working names.

- Internal source file: `out/R5_review_A.md`
- SHA-256: `7d564bd168c4bc30caaff4fb8fc1f75797ffb5eed672fcb9f2ae46b8d19e23df`
- Report scope: Round-5 independent review A — Z1.5.01, Z1.5.06, Z1.5.07, Z2.K4

## Internal report

The report below preserves its original verdict, scope and unresolved points. Historical review-machine home prefixes are displayed as `${REVIEW_HOME}`; the source checksum above identifies the original report. Source line numbers in other records count from its original title.

# Round-5 independent review A — Z1.5.01, Z1.5.06, Z1.5.07, Z2.K4

Sources checked: `ch_P.tex` (sec:P-r5-k4 lines 11737–11963; r5 small units lines 12406–12526; earlier K4 text lines 375–400 and 1585–1637), unit rows in `ch_Z.tex` (555, 560, 561, 634), `P_notes.md`, the cleaned Lean copy `${REVIEW_HOME}/src/rh/src/`, the original tree through the device shell (line ranges), and `graphq.py` (callers/deps). Two literature citations were checked by fetching the cited PDFs (machine summary of the fetched text, not a page-by-page reading).

| Unit | Verdict |
|---|---|
| Z1.5.01 | COMPLETE CONFIRMED (three compressed steps, none wrong) |
| Z1.5.06 | COMPLETE CONFIRMED (conditional on CountQAlt, NewAdmAlt as stated) |
| Z1.5.07 | COMPLETE WITH GAPS (one unlabelled p-adic Hodge step; conditional on CountKAlt) |
| Z2.K4 | COMPLETE WITH GAPS (complete only as a literature proof of SSurj; standard comparison theorems uncited; Lean route under-labelled) |

No statement/Lean mismatch and no mathematical error was found in any of the four. Nothing here bears on whether RH is proved; all four are internal implications.

---

## Z1.5.01 — Coefficient representations and the Weyl bound

**Verdict: COMPLETE CONFIRMED.**

### Findings

1. **Statement vs Lean.** Matches `UpperTheory.V.Af.WeylC` (`LocIsotypic.lean`) and `weyl_complex_of_printed_results` (`TWeylC.lean:10–44`): for totally complex `E` and every `n`, `∃ c A, ∀ m StrictAnti, ∀ H, (∀ i, |m i| ≤ H) → ∃ Ξ : AlgRep E n, (∀ τ, AlgInfChar Ξ τ ((infOf m).map Neg.neg)) ∧ Ξ.d ≤ c (H+1)^A`. The text's constants `A = n²d`, `c = ((n+1)²)^A`, `d = |Hom(E,ℂ)|` are literally the Lean witnesses. `AlgRep` carries irreducibility (`irred` field), as the text says. "Infinitesimal character" is, in Lean, *by definition* the identity `qdet(eOf Ξ τ, u+(n−1)/2) = ∏(u + m)·1` (`algInfChar_iff` is `Iff.rfl`); the text proves exactly that identity, so nothing is lost.
2. **Numerics verified.** `ν_k = k+1+H−m_{rev k} ≥ 0`; antitone because `m_{rev(k+1)} > m_{rev k}`; `ν_k ≤ n+2H`. Degree of the product of leading minors is `Σν_k ≤ n(n+2H)`; monomial count `≤ (N+1)^{n²}`; `n(n+2H)+1 ≤ (n+1)²(H+1)`. Scalar after the `det^{-(n+H)}` twist: `u−(n+H)−k+ν_k = u−n+1−m_{rev k}`, and at `u+(n−1)/2` this is `u−((n−1)/2+m_{rev k})`, i.e. the negated `infOf` multiset. `n=0` gives `c=1, A=0`, dimension 1. All correct.
3. **Highest-weight evaluation verified** against `Formalism.REAL.qdet` (`StatementE.lean`: product in list order `k=0..n−1` of `Tm(u−k)_{σ(k),k}`) and `quantumDetHighestWeight_holds`: the rightmost factors act first, the largest moved column `j` has `σ(j)<j`, and `E_{σ(j),j}` is a raising operator. Direction is right.
4. **Conjugation invariance verified** against `qdet_conj` (`QminorSwapAdjacent.lean`, hypothesis `Q*P=1`), `qdetComm` and `commAll`. The text's two-sum expansion (row selection of `P` ⇒ `det P`·quantum minor; column permutations ⇒ `det Q`) is the Lean proof.
5. **Label.** "[Hypothesis, discharged at the use]": confirmed. The proof begins `intro _` (the `Hypotheses'` argument is unused), and `card_k_of_printed_results` (`TCardK.lean:18–24`) passes its own record. `graphq callers` shows a **second** caller, `UpperTheory.V.Br.cardP_of_prints` (`BrCardP.lean:18–36`), not mentioned in the text; harmless.
6. Line ranges agree with the original tree (`TWeylC.lean` theorem at 10; `Scalar.lean:12`; `ExistsTens.lean:14,31`).

### Steps asserted in compressed form (not wrong; an expert can fill each in a few lines)

- **Column skew-symmetry of quantum minors** ("The 𝔤𝔩_n commutator with the consecutive shifts gives skew-symmetry under adjacent exchanges"). This is the technical core (Lean `two_rel`, `prod_ofFn_adjacent`, `qminor_swap_adjacent`, about 120 lines). The text gives the reason but not the computation. I checked the two-factor identity `T_ab(x)T_cd(x−1) − T_cb(x)T_ad(x−1) + T_ad(x)T_cb(x−1) − T_cd(x)T_ab(x−1) = 0` from `[E_ab,E_cd] = δ_bc E_ad − δ_da E_cb`; it holds. The passage from adjacent to arbitrary repeated columns is also left to the reader.
- **The differentiated polynomial action satisfies the 𝔤𝔩_n relations** (`Weyl.glRel`, `GlRel.lean:5–18`) and **`Ad`-compatibility** `Ξ(y)E_ab = (Σ y_ca Q_bd E_cd)Ξ(y)` (`adEq`) are used without being stated.
- **"The derivative at a given embedding sees only its own factor."** True, but the reason is not given: `eOf` is the Wirtinger derivative `(1/2)(d(X) − i·d(iX))` and the factor at `τ' ≠ τ` (in particular at `τ̄`) is not holomorphic in the `τ`-coordinate (`eOf_fac`, `coord_hol`). This is also the only place "totally complex" is used, which the text does not say.

### Understanding

The text does explain why the result holds: a product of leading minors is an explicit highest-weight vector of weight `ν` in a polynomial space whose dimension is trivially polynomial in `H`; the Capelli (quantum) determinant acts on it by the scalar read off from the diagonal term, is central, hence acts by that scalar on the generated submodule; tensoring over embeddings and shrinking to a minimal invariant subspace keeps both the scalar and the bound. The route deliberately avoids the Weyl dimension formula (the `P_notes` remark "Weyl's dimension formula is a candidate" is superseded). A reader gets the idea and the exponents.

### Most important problems

1. Column antisymmetry of quantum minors is asserted with a one-line reason rather than written out (minor).
2. The role of total complexity / holomorphic coordinates in the tensor step is not explained (minor).
3. Second consumer `cardP_of_prints` missing from the discharge note (cosmetic).

---

## Z1.5.06 — Rational Frobenius trace bound

**Verdict: COMPLETE CONFIRMED** (as an implication from `CountQAlt` and `NewAdmAlt`).

### Findings

1. **Statement vs Lean** (`FrobeniusTraceCountBoundOfCmEigensystemCount.lean:348–398`, original numbering). Quantifier order matches: `CountQAlt → NewAdmAlt → ∃ c A, ∀ K e≥1 M≥1 p h w (p prime, p ∈ w, p ∤ M), ∃ D : TrData (p^h) e, card ≤ c(M(e+1))^A ∧ ∀ l odd ≠ p, Ω, ι, B over w, σ with IsFrob B (p^h) σ, D.Classifies ι σ⁻¹ (Adm2B ι e M)`. The text's "one finite index set … for each odd ℓ≠p, allowed closure, ι and place over w" is the correct order (`D` before `l`). `TrData` fields (conjugation-stable, `‖t‖ ≤ √q+2`, `q^e t` integral, `q = p^h`) are quoted correctly. `c, A` are obtained from `CountQAlt 2` before `K` is introduced, so they are absolute, as claimed.
2. **Proof checked line by line.**
   - Rank-two instance at weight `(e,−e)`, `wt = 0`, `H = e`: strict decrease needs `e ≥ 1`; reversed sums vanish; bound `c(M(e+1))^A`. Correct.
   - Bound: `Win p 0` gives `p^{-1/2} < |b_i| < p^{1/2}` and `|b_1 b_2| = 1`, so `0 < u_i ≤ R`, `u_1u_2 = 1`, `(R−u_1)(R−u_2) ≥ 0 ⇒ u_1+u_2 ≤ R+1/R ≤ R+1`, hence `|t| ≤ R+2`. Inequality directions correct; `h = 0` included (`R = 1`).
   - Integrality: `intInv` with `a = e` gives `p^e b^{-1}` integral; `h`-th power and `p^{he}·1`. Correct.
   - Frobenius: `frobenius_pow_resDeg_place_norm` gives `B` over `v`, a rational Frobenius `τ` and `(τ^h)^{-1}·σ|_ℚ ∈ I_B`; the classifier's unramifiedness (first clause of `FrobEig`) kills it, so `W(σ^{-1}|_ℚ) = W(τ^{-1})^h`. Roots of `W(τ^{-1})` are `b_i^{-1}` after `ι` (the `FrobEig` convention with `β.map (·⁻¹)`), and the power-trace recurrence is `map_trace_eq_sum_roots_of_charpoly_map.2`. Trace of the block form is `1 + tr W`. All as in the text.
   - Injectivity of labels: `block_conjugate_rank_three_rep`. Correct.
3. **Labels.** "[Hypothesis, discharged at the application]" confirmed with `graphq callers`: the only caller is `numberU3U_of_adm2A_imp_adm2B` (`KeepNumU.lean:25–78`), which feeds `countQ_alt hP hLP hA` and `hN`; `numberU3U_of_prints` (`KeepNumU.lean:79–80`) supplies `newAdmS_alt P` (its only caller). Line ranges `25–32, 79–80` are right in the original tree. Note the consumer applies the bound with level `N·|disc K|` and `p^h = Nw`, which is consistent with the statement.

### Steps asserted without proof or citation

- "the stabilizer of the prime maps onto its residue automorphism group" (for the integral closure in an *infinite* algebraic extension). In Lean this is Mathlib's `Ideal.Quotient.stabilizerHom_surjective_of_profinite` inside `ReciprocityTheory.Gal.exists_frob_over` (`GlobalB.lean:238–310`). It is a standard theorem, but the text neither cites a reference nor marks it as taken from Mathlib.
- The meaning of an eigenvalue classifier (`EigData.Classifies`: unramified at every place over `v` and the inverse-root convention at inverse Frobenius) is used but not restated in this subsection; the phrase "Unramifiedness kills this inertia quotient" relies on it.

### Understanding

Yes. The text makes clear that nothing new is counted: the rank-three representations in `Adm2B` are `W ⊕ 1` for a rational rank-two `W`, so the rational eigenvalue classifier is reused with the same labels, and the only work is (a) converting eigenvalues at a rational Frobenius into the trace at a Frobenius of residue degree `h` over `K`, and (b) checking the two numerical side conditions. The reason the bound is `√(p^h)+2` and the integrality exponent is `he` is visible.

### Most important problems

1. Surjectivity of the decomposition group onto residue automorphisms is used without citation or a "Mathlib" label (minor).
2. `CountQAlt` and `NewAdmAlt` remain genuine hypotheses of this unit (correctly labelled; their own units are not closed by this proof).

---

## Z1.5.07 — CM Frobenius trace bound

**Verdict: COMPLETE WITH GAPS** (one unlabelled step; otherwise correct, conditional on `CountKAlt`).

### Findings

1. **Statement vs Lean** (`…CmEigensystemCount.lean:418–461`). Matches: `CountKAlt → ∀ K CM, ∃ c A, ∀ e≥1, N≥1, p, w | p, p ∤ N, p ∤ disc K, ∃ D : TrData (Nw) e, card ≤ c(N(e+1))^A ∧ ∀ l odd ≠ p, Ω, ι, B over w, σ Frobenius of norm Nw, D.Classifies ι σ⁻¹ (Adm3NAlt ι e N)`. Constants depend on `K` (text: "Fix a CM field"), `D` is chosen before `ℓ` (text says so explicitly). The Lean constant is `c·2^A`, the text's `c'`.
2. **Proof checked.**
   - Weight `(e−1,−1,−e−1)`: strictly decreasing, paired sums `−2 = 1−3`, `H = e+1`. Correct.
   - Window: `Win q (−2)` gives `q^{-3/2} < |b| < q^{-1/2}`, hence `a^{-1} < |(qb)^{-1}| < a` with `a = √q`; product clause gives `xyz = 1`. The three-number inequality: two of `x,y,z` on the same side of 1 give `x+y ≤ 1+xy = 1+1/z`; `(a−z)(az−1) ≥ 0 ⇒ z+1/z ≤ a+1/a ≤ a+1`; total `≤ a+2`. Correct, and it is the content of `add_add_le_add_two_of_mul_eq_one_…` used at `FrobeniusTraceCountBoundOfRatEigensystemCount.lean:78–145`.
   - Integrality: all weights `≤ e−1`, so `q^{e−1}b^{-1}` is integral and `q^e(qb)^{-1} = q^{e−1}b^{-1}`. Correct (including `e = 1`).
   - Cardinality: `c(N(e+2))^A ≤ c·2^A(N(e+1))^A`. Correct.
   - Untwisting: `ρ' = ρ ⊗ χ^{-1}`, `ρ'(σ^{-1}) = χ(σ)ρ(σ^{-1}) = q·ρ(σ^{-1})` since `χ(σ) = q` at a Frobenius of norm `q` with `ℓ ∉ w` (`cycZ_of_isFrob`, Bézout for `p, ℓ`); so `q·ι tr ρ(σ^{-1}) = Σ b^{-1}`. Correct.
   - `Adm3NAlt → AdmKNAlt` for the twist (`admissible_twist_cyclotomic`, 409–417): irreducibility, the automorphy clause (already stated for the twist in `Adm3NAlt.aut`), level, oddness. The oddness step (`oddTw'` via `unl_tw`, `pot_tw` in `FlagLaws.lean`) is the two-line cancellation the text describes.
3. **Labels.** "[Hypothesis, discharged at the use]: CountKAlt is Z1.5.03" — confirmed: the only caller is `numberU3U_of_adm2A_imp_adm2B`, which passes `countK_alt hP hLK` (`countK_alt` at 63 in the original; Z1.5.03 row in `ch_Z.tex`). Note Z1.5.03 itself is marked "structure only", so the unit is complete only as a conditional conversion, exactly as its header "Complete under CountKAlt" says.
4. A small wording point: "The inverse of an invertible matrix has eigenvalues the inverse roots" is not what is used. The classifier (`EigData.Classifies` → `FrobEig`) already gives the characteristic polynomial of `ρ'(σ^{-1})` with roots `b^{-1}`; no inversion of a matrix is needed. The displayed identity is nevertheless correct.

### Steps asserted without proof, citation or label

- **Potentially crystalline branch of the level condition.** `Level` (`BlochKatoSelmerVanishes.lean`) has, above `ℓ`, the alternative "`κ_i ≠ κ_j·χ_cyc` for all `i,j`" **or** `PotCrysAt r A`. In the second branch `level_twist_cyclotomic_pow` (`LevelTwistCyclotomicPow.lean:19–59`) invokes `GlobalTheory.HodgeOfTrue.potCrys_twistBy` (`GaloisHodgeOfCuspidal.lean:188–234`) and `UpperTheory.isCrysAt_cyclotomic_zpow_restrict_decompositionGroup`, i.e. (a) integral powers of the cyclotomic character are crystalline and (b) a potentially crystalline representation tensored with a crystalline character is potentially crystalline. These are genuine `B_cris` statements in this formalization (they go through `CrysRules.isCrys_iff`, `isCrys_cyc_zpow`, the tied period data `LocTied`). The text only says "tensor the potentially crystalline representation with the crystalline cyclotomic power on the same local bridge". It is neither written out, nor cited to the literature, nor marked "Proved in Lean, not reproduced".
- Continuity of the twisted representation (first field of `Level`) is not mentioned (trivial).

### Understanding

Yes. The explanation is clear: specialize the eigenvalue count to the weight that the inverse cyclotomic twist of an `Adm3NAlt` representation has, keep the labels, and observe that undoing the twist at inverse Frobenius divides by `q`, which is exactly why the trace datum is `Σ(qb)^{-1}`, why the window is centred so that the three numbers have product one, and why `q^e` clears denominators. What a reader does not learn from this subsection is what the potentially-crystalline alternative in the level condition is for.

### Most important problems

1. The pot-crystalline twist stability (`potCrys_twistBy` + crystallinity of `χ_cyc^j`) is an unlabelled, unreproduced p-adic Hodge step. It should carry a "Proved in Lean, not reproduced" label or a literature citation.
2. The unit is conditional on `CountKAlt` (Z1.5.03, "structure only"); the "complete" status must be read with that qualifier.
3. Misleading sentence about inverses of matrices (cosmetic).

---

## Z2.K4 — Odd stable homology and torsion

**Verdict: COMPLETE WITH GAPS.** The rank bound and the torsion statement follow correctly from what is written plus published theorems, and the second comparison (`SWtOdd`) is genuinely reconstructed. The first comparison (`SSurj`) is closed by a literature argument that is *different from the Lean proof*; that argument is sound as far as I can check, but several textbook comparison facts are used without citation, and the Lean route is only partly labelled.

### Findings

1. **Statements vs Lean.**
   - `BOdd`/`BStarOdd` (`LemmaKOfSteps.lean`, `SBStarOdd.lean:18`): `L` totally complex, `Even k`, `k+1 < r_2`, `0 < ℓ`, `2(k+1)+4 ≤ n` ⇒ `rank_ℤ span{zSeq(x,k) : x ∈ H_{k+1}(GL_n O_L)} ≤ r_2`. Matches the `ch_Z.tex` row. `zSeq` step: `ψ_ℓ − ℓ^{t+2}·stab` (`SBStar.lean:30`), matching "minus `ℓ^{j+2}` times its stabilized image".
   - `TorsStab` (`RankCount.lean`): totally complex, `2m+4 ≤ n ≤ n'` ⇒ torsion of `H_m(GL_{n'})` finite with the cardinality at rank `n`. Matches.
   - `SSurj` (`SBStar.lean:20–24`): `∃ N ≥ n₀` working for **every** invariant cocycle `c`, with `ω` invariant under all of `∏_w GL_N(ℂ)`. The text states exactly this ("one `N` … for every `c`"). `SWtOdd` (`SBStarOdd.lean:9–16`): `τ` chosen before `N, ω`; coefficients `c_w` and the systems `a_j` may depend on `N, ω`. The text has the same dependence.
   - `ev`, `intS`, `intP`, `FInv`, the action `h ↦ (g^{-1})^* h g^{-1}` (`ActLPos.lean`) are as described; `FInv` and `intP` indeed only test positive points, so extending a form by zero off the cone is legitimate.
2. **Assembly (`sBStarOdd_of`, `SBStarOddOf.lean:13–78`) verified.** Weight-`j` value on a terminal cycle is `∏_{t<k}(ℓ^j − ℓ^{t+2})·a_j(z_0)`, zero for `2 ≤ j ≤ k+1` at `t = j−2`; weight-one values persist under `stab`; `SStab` injectivity is used at rank `ℓ^k n ≥ 2(k+1)+4`; `rank_span_le` is flatness of `ℝ` over `ℤ`. The text's "Passage back" paragraph (with lines 1600–1637) follows this exactly.
3. **Second comparison verified against the Lean route** (`sWtOdd_of`, `swtOdd`, `wOneOdd`, `fft_of`): 
   - The double-commutant argument is correct as written (Hilbert–Schmidt projection onto a unital `*`-closed algebra commutes with left multiplication; blocks lie in `𝒜'`; apply to the identity).
   - Span of block-unitary tensor powers: vanishing on diagonal unitaries ⇒ a degree-`q` polynomial vanishing on a torus ⇒ zero; unitary conjugation ⇒ all Hermitian blocks; `H+tK` at `t = i` ⇒ all block matrices; polarization ⇒ symmetric tensors. Correct.
   - Weight systems: padding by identity pads tangent vectors by zero (every cycle is a nonempty word, so traces are unchanged); `d` diagonal copies multiply each cycle trace by `d`; closedness from `[𝔭,𝔭] ⊂ 𝔨`; Stokes. Matches the three clauses of `WSys` (`SBStar.lean:9–12`).
   - One-cycle term: conjugate to the rotation, single place, reversal conjugates the trace, so exactly one of the alternated real/imaginary parts can survive; `τ_v` := their sum. This is `wOneOdd` (`OddWeightCycles/Weights.lean:144–198`), including the case split on the sign of the reversal.
4. **First comparison, literature proof — checked.**
   - `Γ₀ = Δ × U` is `det^{-1}(U^N)`, of finite index; the splitting `X_N ≅ Y_N × ℝ^{r_2}`, the translation `−2N^{-1}log|det g_v|`, the equivariance of `h ↦ h/(\det h)^{1/N}` through `g ↦ g/δ` with `δ^N = det g`, and invariance of `dt_v` are all correct. The scalar-unit translations form a full lattice in `Σ t_v = 0` (normalized absolute values at complex places are squares). Borel is needed in **all** degrees `0..q`, and the text says so.
   - **Borel citation verified** (fetched Numdam PDF): Theorem 7.5 is injectivity for `q ≤ c(G)` and surjectivity for `q ≤ min(c(G), m(G(ℝ)))` of `I_G^q → H^q(Γ)` for a semisimple `ℚ`-group and arithmetic `Γ`; §9.5 bounds the minimum below by a function of `rk_ℚ G` (about a quarter of it) via restriction of scalars; §11 treats `R_{k/ℚ}` and `SL_n` over a number field. The use made of it is legitimate.
   - **Stability citation verified** (fetched EMS PDF of Soulé 2003): §4.2, p. 779 states `H_m(GL(A),ℤ) = H_m(GL_N(A),ℤ)` for `N ≥ 2m+1`, attributed to Maazen and van der Kallen. The project only needs `N ≥ 2m+4`. In Lean this is not an assumption: `isIso_stab`/`torsStab` use `PositivityTheory.v8.KStability.kStability`, a proved core theorem with range `n ≥ 2i+s+2`, `s = 2` for Dedekind rings.
5. **Labels.** "[Hypothesis, discharged at `UpperTheory.V.ZK.bOdd`, `BOdd.lean:3`]" confirmed: `bOdd := bOdd_zk`; its only caller is `lemmaK_litN_alt` (`KFinal.lean:11`; the cited range 9–11 contains it), which passes it to `lemmaK_of_litN_alt`. `bOdd_zk`'s only caller is `bOdd`. `torsStab`'s only caller is `UpperTheory.V.ZK.sUpperOf` (`SUpperOf.lean:64–66`); the r5 section gives **no** discharge note for this second declaration of the unit (the older text at line 390 only says "specialization of TorsStab").
6. The stale "partial" rows for Z2.K4 in `P_notes.md` (lines 157, 1109–1110, 1162) sit under the v6 / v5 archive headings; they are historical, not a contradiction.

### Steps asserted without proof, earlier item, citation or label

- **De Rham / bar-complex comparison.** "It induces the usual comparison with cohomology of the symmetric space … the affine map from the homogeneous bar realization to `X_N` is equivariant between contractible free spaces." This is the statement that integrating invariant forms over straight simplices computes `H^*(Γ;ℝ)` and agrees with the map `j` of Borel's theorem. Standard, but it is the hinge between Borel's theorem and the exact `ev … (intP ω)` identity that `SSurj` demands, and it is given neither a proof nor a reference (the only citation is "Borel, proof by passage to a torsion-free subgroup").
- **Existence of a torsion-free finite-index subgroup** of `GL_N(O_L)` (and of `Δ`), used twice, uncited.
- **Real Künneth formula** for `Δ × U`, **cohomology of a torus**, the **transfer** argument, and compatibility of wedge product of forms with the cross product of classes: all uncited textbook facts.
- **Bar homology with real coefficients vs `ℝ ⊗ H_*(–;ℤ)`** and its naturality (Lean `SBridge`, `th_zc`): used in "each integral terminal generator maps into this image after extension of scalars" without statement.
- **Lean route for `SSurj`.** The paragraph "The proof selected by the Lean source" lists Whitney forms, central averaging, the `(3/5)^r` Hecke contraction, the `(4/5)^r` lower bound (confirmed at `Assemble.lean:226–277`), stable surjectivity. Only `sGap_of` and `sMom_of` carry the "Proved in Lean, not reproduced" label, but none of `sWhit`, `sCen`, `sLoc`, `sMean_of`, `sHecke`, `sPU`, `sHt_of`, `sPrime_of` is reproduced either. Because the literature argument replaces the whole interface this does not break completeness, but the label understates what is not reproduced, and the reader should be told plainly that **the hand proof of `SSurj` is not the formalized proof**.

### Other observations

- The hypothesis `k+1 < r_2(L)` is recorded ("Here … `q < r_2(L)`") but never used in the literature proof of `SSurj`; it is an input of the Lean Hecke route only. The text does not say this, which leaves a reader wondering where it enters.
- "For `q` positive and odd" (i.e. `k` even) is likewise not what makes the one-cycle argument work as written (it works for any `q`, possibly with `τ_v = 0`); oddness is what makes the rotation an even permutation so that `τ_v` can be nonzero. Not an error.
- Bibliography: the unit theorem is cited as `P-Milne-Mink`, Theorem 5.1, while the `%BIB` line for that key describes Theorem 4.3 (bounded-norm ideal representatives). Same book, wrong descriptor.
- The stability reference is a secondary one ("as used by Soulé"); the primary sources (Maazen; van der Kallen) are not in the bibliography.

### Understanding

Largely yes, and better than for most units of this size. The text explains the mechanism: real cohomology of `GL_N(O_L)` in the stable range is carried by invariant forms; invariant forms are polynomials in traces of words, one trace per cycle; under `ℓ` diagonal copies a `j`-cycle form scales by `ℓ^j`; the `z`-sequence is built to annihilate every weight `2,…,k+1`, so only the single-trace forms, one per infinite place, can detect a terminal class; hence rank `≤ r_2`. The torsion statement is a direct consequence of integral stability plus the K7 finiteness. What is less well explained is the first comparison: the reader is given two proofs (a literature one and a sketch of the formalized Hecke one) without a clear statement of which is being relied on for "complete" and why the hypothesis `q < r_2` appears.

### Most important problems

1. `SSurj` is closed by a literature proof (Borel 7.5 + central factor + transfer) that is not the Lean proof; the comparison "invariant form integrated over straight simplices = group cocycle class" is the hinge and is asserted as "the usual comparison" with no reference.
2. Several further standard facts (torsion-free finite-index subgroup, Künneth, transfer, torus cohomology, real bar homology = `ℝ ⊗` integral homology) are used without citation.
3. The "Proved in Lean, not reproduced" label on the Hecke route names only the spectral gap and the moment bound; the Whitney-form, averaging, localization, mean and Hecke-vanishing inputs are equally unreproduced.
4. No discharge note for `torsStab` (consumer `sUpperOf`), and homological stability is cited only through Soulé although Lean proves it (`kStability_main`); the text should say which of the two it relies on.
5. The unused hypothesis `k+1 < r_2(L)` is not explained.

---

## Cross-unit summary of the most important problems

1. **Z2.K4:** complete only via a literature argument for stable realization; its key comparison step and several textbook facts are uncited, and the Lean route is under-labelled.
2. **Z1.5.07:** the potentially crystalline branch of the twisted level condition rests on unreproduced, unlabelled Lean theorems (`potCrys_twistBy`, crystallinity of cyclotomic powers).
3. **Z1.5.06 / Z1.5.07:** both are conditional conversions (`CountQAlt`+`NewAdmAlt`; `CountKAlt` = Z1.5.03, still "structure only"); correctly labelled, but "complete" does not extend to those inputs.
4. **Z1.5.01:** the column antisymmetry of quantum minors and the holomorphic-coordinate reason in the tensor step are compressed to single sentences.
5. **Z1.5.06:** decomposition-group surjectivity onto residue automorphisms (infinite extension) is used without a reference.
