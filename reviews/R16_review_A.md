AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

# R16_review_A

AI review report produced during this project; file names are internal working names.

- Internal source file: `out/R16_review_A.md`
- SHA-256: `1d6e6c9289cd0a15c13415ecd1313e42935a9088654cc9928529c1c364f13d1a`
- Report scope: R16 review A — the two theta inputs (`kThetaVector`, `StdOK`) and the Z4.2.04 unconditional candidate

## Internal report

The report below preserves its original verdict, scope and unresolved points. Source line numbers in other records count from its original title.

# R16 review A — the two theta inputs (`kThetaVector`, `StdOK`) and the Z4.2.04 unconditional candidate

Reviewed: `ch_P_r16.tex` (all of §§r16:stdok, r16:ktheta, r16:pair-candidate), `ch_P_r15.tex` 415–677 (§r15:translated, §r15:pair) and 691–760, 1285–1338, the register `R16_pending.json`, `status.json`, and the two R15 reviews. Lean was read at commit `40e56bab…` in original numbering (`git show`). Cone figures come from `graph_cache.bin` (the data behind `graphq.py`); a line count is the sum of inclusive ranges of distinct core declarations, written "lines / theorem lines".

Nothing here claims or implies that RH or GRH is proved. The review only compares hand proofs and bookkeeping with the Lean declarations they label. I did not write the blueprint. No human has signed off on any of this.

## 1. Verdicts

| Item | Verdict |
|---|---|
| 15 registered declarations (6 `kThetaVector`, 9 `StdOK`) | **13 CONFIRMED, 2 CONFIRMED WITH GAPS** (`Ker.kThetaVector`, `ThStd_proof`); 0 NOT CONFIRMED. The gaps are bookkeeping and one definitional sentence, not mathematics. |
| Deferral loop `algTAll` / `thM_spec` / `stdOK` | **Broken**, in the text and in the dependency graph (§4.1). |
| §r15:translated as a proof of `translate_entire_algebraic` and `algTAll` | **CONFIRMED WITH GAPS**: one location, complete, correct where I recomputed it. Two route deviations are marked at the head; three more are not (§4.3). |
| Z4.2.04, unconditional completion | **APPROVE AFTER MINOR EDITS** (list in §6). No edit needs new mathematics. The grade should not change until edits E1–E4 are made. |

The main finding outside the proofs: the Pair cone contains a **third Lean implementation** of the theta-vector theorem, `GlobalTheory.Mem.Col2.ThetaVec.thetaVector`, which the register does not list, while the listed "equivalent entry point" `Ker.Cd.kThetaVector` is not in the Pair cone at all (§3.1).

## 2. The fifteen declarations

All 16 register rows (15 plus the `Cd` entry point) reproduce: name, file, line range, inclusive cone size and theorem lines agree with the graph and the pinned source. All nine proof labels exist in `ch_P_r16.tex`.

### 2.1 `kThetaVector` group

| # | Declaration (Lean lines) | Label | Statement | Proof | Verdict |
|---|---|---|---|---|---|
| 1 | `Ker.kThetaVector` (`IsAdmissibleFlagPair…lean:27–29`) | r16:ktheta | match | correct | CONFIRMED WITH GAPS (G1, G2) |
| 2 | `Th1.H.product_theta_mem` (`Th0CharMulOpUTh0HalfPeriodEq.lean:199–212`) | r16:ktheta-line | match | correct | CONFIRMED |
| 3 | `Th1.H.ThStd_proof` (282–309) | r16:ktheta-line | match | correct | CONFIRMED WITH GAPS (G2) |
| 4 | `Th1.H.InterInv_of` (`LogarithmEquivalence.lean:201–241`) | r16:ktheta-transport | match | correct | CONFIRMED |
| 5 | `Th1.H.FourthRoot_of` (`MatrixFormFourfoldBlockFirstBlockEmb.lean:102–158`) | r16:ktheta-root | match | correct | CONFIRMED |
| 6 | `Th1.H.ThetaVector_of` (250–302) | r16:ktheta | match | correct | CONFIRMED |

**Statement (row 1).** Lean's `ThetaVector` quantifies over an arbitrary matrix `h`, subgroup `Λ`, functions `α, β` and equivalence `g` with `StdData`, and any `κ ≠ 0`. It asserts existence of `θ ∈ Th(matH h, α, Λ)` with `tens4 θ = κ • kernel4`, and for every such `θ`: `θ ≠ 0`, any other solution is `ζθ` with `ζ⁴ = 1`, and `θ` spans the theta space. The text (258–282) has all four clauses and all ten `StdData` fields. `kernel4` is `inter stdH β stdLat (g(Λ⁴)) F0 ∘ g`, summed over `M/(A∩M)` with factor `[M : A∩M]^{-1/2}`; this is the text's `I_AM`.

**One-dimensionality of the standard theta space (rows 2, 3).** I recomputed:

- `f = σ·exp(−s₂z²/2)` with `η(ω) = s₂ω + π ω̄/A`: the quasi-period factor becomes `s(ω)·exp(πH(z,ω) + πH(ω,ω)/2)`. With `opU` as in `IsSemiChar.lean:21–22` this is `s(ω)·U_ω f = f`, which is Lean's `SgStarFixed`.
- Legendre gives `c = π/A` for either orientation of the generators, because `area` is an absolute value. The text's "use a positive ordering" is enough.
- `e_t = U_t f / (U_t f)(0)`, `t = ω₀/2 ∉ L`: multiplier `s(ω)·exp(πi E(ω, ω₀))`, which is Lean's `thetaZeroCharacter`. The sign of the exponent is immaterial since `E(ω, ω₀) ∈ ℤ`, as the text says.
- Uniqueness: `F/e_t` is elliptic with at most one simple pole per cell, so its residue vanishes and it is constant. Lean (`even_theta_line`, `EvenThetaSecond.lean:10–89`) first translates `F` by `−ω₀/2` and applies `thetaLine` for `σ*`. The text says the half-period translation is "already made in the denominator". Same argument.
- Product: `th_split` (214–280) plus induction over a finset is the text's "fix all coordinates but `i`" and "iteration". The empty product is covered.
- Semicharacter on the standard lattice: the parity of the cross terms of `m + n + mn` is `mn′ + m′n ≡ det (mod 2)`. Self-duality: test on the two coordinate periods (`mem_lattice_of_dual`).

**Line transport (row 4).** Recomputed with `U_xU_y = e^{−πiE(x,y)}U_{x+y}`: `D_xD_y = β(x+y)·e^{−2πiE(x,y)}·U_{x+y}`, so `D_xD_y = D_{x+y}` needs `E(x,y) ∈ ℤ` on the lattice. That follows from the semicharacter taking values `±1`; the text states integrality two sentences later. The pairing `A/K × M/K → S¹` has trivial kernels by the two self-dualities; both quotients are finite by the index hypotheses; the double sum collapses to `d·F`. Lean proves the equal orders by a double character sum (`IndexEq_of`) instead of the injection into the dual group. Same content. Spanning of `I_AM F₀` uses `InterTh` (the intertwiner preserves entireness) and the inverse on `M`-fixed functions; both are stated.

**Fourth root (row 5).** `q(z) = P(z, u₁, u₂, u₃)` lies in the one-block space by testing at `(x,0,0,0)` and `α(0) = 1`; `q^{⊗4} = cP` by the line; `c ≠ 0` at `(u₀,u₀,u₀,u₀)`; `θ = rq` with `r⁴ = c⁻¹`. Uniqueness: `G ⊗ v^{⊗3} = bP` evaluated at `(z,w,w,w)`. This is `FourthRoot_of` step for step (`restrict_mem`, `fourfoldTensorMem`, `key_line`). No hermiticity of `h` is needed, and none is used.

**Assembly (rows 1, 6).** `ThetaVector_of` is: `β` is a semicharacter on the standard lattice by `betaStd`; `F₀` is a nonzero member; `LineTransport`; pullback by the isometry `g` with `betaAlpha`; `FourthRoot`. The text follows this order (351–415). The last paragraph (417–432) correctly derives `thM_spec`, `isThM_ne_zero` and `κ ≠ 0` (`KapChoice.kappa_ne_zero`, 176–193, including the `finprod` convention).

**Gaps.**

- **G1 (labelling).** See §3.1: the register names the wrong second implementation.
- **G2 (definitions).** Lean defines `wSigma` as `z·∏'` over all of `L.lattice`, `wZeta` as a `∑'` over all of `L.lattice`, `wEta` as the real-linear extension of `2ζ(ωᵢ/2)`, and `s2` by an explicit quotient (`SemiChar.lean:8–23`). The text uses the DLMF objects without saying these are the same: the `l = 0` terms are harmless under Lean's `x/0 = 0`, `η(ωᵢ) = 2ζ(ωᵢ/2)` is DLMF (23.2.11)–(23.2.12), and `s2` is what the decomposition `η(ω) = s₂ω + πω̄/A` forces. One sentence is needed. The Lean cone under `sgStarQuasi ∪ sgStarBasic` (1,371 / 1,324 residual lines) is covered only by this citation.

### 2.2 `StdOK` group

| # | Declaration (Lean lines) | Label | Statement | Proof | Verdict |
|---|---|---|---|---|---|
| 7 | `SO.stdOK` (`PStdOK.lean:338–339`) | r16:stdok | match | correct | CONFIRMED |
| 8 | `FourthRootStd.stdOK` (`SpanRangeEmb4EqTop.lean:700–701`) | r16:stdok | match | correct | CONFIRMED |
| 9 | `Th1.H.quadMultiplierSemicharacter` (`MatrixFormFourfoldBlockFirstBlockEmb.lean:178–232`) | r16:std-char | match | correct | CONFIRMED |
| 10 | `SC.char_eq` (`PStdChar.lean:310–352`) | r16:std-char | match | correct | CONFIRMED |
| 11 | `FourthRootStd.span_range_emb4_eq_top` (256–295) | r16:std-isom | match | correct | CONFIRMED |
| 12 | `Base.isomOK` (`IsAdmissibleFlagPair…lean:773–798`) | r16:std-isom | match | correct | CONFIRMED |
| 13 | `Base.lat0OK` (438–439) | r16:std-dual | match | correct | CONFIRMED |
| 14 | `SO.up` (`PStdOK.lean:251–301`) | r16:std-indices | match | correct | CONFIRMED |
| 15 | `SO.down` (303–325) | r16:std-indices | match | correct | CONFIRMED |

- **Rows 7, 8.** Both assert `B.StdOK` for any base over a curve ideal and a discriminant twelfth root. The ten fields are derived in the text in the order `per`, `half`, `betaStd`, `isom`, `alpha0`, `betaAlpha`, `selfDual`, `betaSemi`, `idx₁`, `idx₂`. `SO.stdOK` goes through `Base.stdOK_of'` and `Base.latAll`; `FourthRootStd.stdOK` calls `selfDual_La` directly with the same two ingredients (`self_dual_lattice`, `hermitian_form_integral_values`). The text says so (244–256, 187–192).
- **Row 9.** With `w_b = (b + i√d)/2`: `Im(w_b H) = (b/2)·e + (√d/2)·Re H`, so `√d·Re H(x,y) = 2k − be`. At `x = y`, `e = 0` and `q(x) = k`. The cross term of `q(x+y)` is `2k − be ≡ e (mod 2)` for odd `b`. This is the Lean `key`, `hq`, `hadd`.
- **Row 10.** Hypotheses match: stability under `cmTheta 1 d`, `ω₀ ∈ L`, the two torsion exclusions, `d % 8 = 7`. I recomputed: `ω, wω` are a basis of `P/2P`; `q(ω) = E(wω, ω)` is odd; `q(wω) = ((1+d)/4)·q(ω)` is even; both multipliers are `−1` at `ω` and `+1` at `wω`; the quotient of two semicharacters for the same `E` is a `±1` character, trivial on `2P`. Lean runs the same four-coset check (`gen`, `q_odd`, `r0`, `ru`, `rall`).
- **Row 11.** Lean: `FL.linInd_embP` (discriminant of the integral basis is nonzero, complementary embeddings by conjugation) and `FL.span_embP` (`[E:ℚ] = 2|Tau|` vectors in a real space of that dimension). The text has both steps (99–116).
- **Row 12.** `gC_spec`, the `K`-isometry field `IsoKG.isom`, `FL.sum_tau_trace`, then sesquilinear extension from the spanning set, first in `x`, then in `y`. As in the text (118–139). `blk4 (hOne) = hOne` on `Fin 4 × n` is the "diagonal blocks" sentence.
- **Row 13.** `homL(S_N, S_N′)` is the integral matrices, `YYl` is the matrices with entries in `I = AA0`, and single-entry generators give the reverse inclusion. The text (142–154) matches `homL_std_entry`, `YYl_std_entry`, `single_mem_homL`, `Lat0`, including empty matrices. `areaOK` is the least-positive-determinant argument (155–158).
- **Self-duality and `betaSemi`.** The standard pair `(2,2)` is admitted (`Adm_std`, `stdL_isSD`); `δ ≠ 0` from the period basis (`base_linkage_nonempty`); the self-duality clause of `Base.latAll` (confirmed in R14 review A); transport by `areaOK`, `lat0OK`, the reindexing `reix`, then `g`. `betaSemi` is row 9 at `b = 1` on `A′`, with `w`-stability from `lamMM_smul`. All in 164–192.
- **Rows 14, 15.** `mk·A′ ⊆ A`: `k` clears `I` into `𝒪_E`, `m` clears the finitely many additive maps `t ↦ (γ₀(e_a t))_v` on an integral basis. `hA ⊆ A′`: `h` clears `γ₀⁻¹(e_v)` and `𝒪_E ⊆ 𝔟⁻¹` (`one_mem_inverse_halfDifferent`). Index convention checked: `relIdx(A, A′) = A.relIndex A′ = [A′ : A∩A′]` is `idx₁`.

Citation slips in this group, all minor: `FourthRootStd.stdOK` is 700–701 (the text's 700–707 includes `stdOK_of_crv`; review B flagged this in R15); `FL.lam_mem` is 528–540; `StdData` is 52–64; `quadMultiplierRules` is 234–242.

### 2.3 Citations

| Citation in the text | Checked against the source | Result |
|---|---|---|
| DLMF §23.2(ii): σ entire, odd, simple zeros at lattice points | dlmf.nist.gov/23.2 | correct; it is the paragraph after (23.2.8) |
| DLMF (23.2.14): Legendre relation | same page | correct: `η₁ω₃ − η₃ω₁ = πi/2` and cyclic forms |
| DLMF (23.2.17): `σ(z+2mω_j+2nω_k)/σ(z) = (−1)^{m+n+mn} exp(…)` | same page | correct |
| DLMF (23.10.3): `σ(u+v)σ(u−v)/(σ²(u)σ²(v)) = ℘(v) − ℘(u)` | dlmf.nist.gov/23.10 | correct |
| Milne, *Modular Functions and Modular Forms*, Corollary 12.16 | jmilne.org MF.pdf | correct: `j(z)` is an algebraic integer for `ℚ[z]` imaginary quadratic |
| Milne, *Fields and Galois Theory*, Theorem 9.29 | jmilne.org FT.pdf | correct: `Ω^{Aut(Ω/F)} = F` for `Ω` algebraically closed, `F` perfect |
| Silverman, AEC III.6.4 and VI.3.6; DLMF §23.3(i) | not fetched | from memory the Silverman numbers are right (torsion structure; `ℂ/Λ ≅ E(ℂ)`); I did not verify them here |

The tex cites `MF110.pdf` and the register cites `MF.pdf`; use one.

Standard facts used without a reference in r16: the residue theorem on a period parallelogram and Liouville on the torus; nonvanishing of the discriminant of a basis of a separable extension; duality of finite abelian groups; existence of an integer denominator for a fractional ideal. These are textbook and each is argued in a line. One reference for the number-field facts would be enough. I do not supply theorem numbers I have not checked.

## 3. Labelling and discharge sites

### 3.1 The third implementation (G1)

`GlobalTheory.Mem.Col2.ThetaVec.thetaVector : ThetaVector` (`IwasawaDecomposition/PeriodLatticeSesquilinearFormIsHerm.lean:437–498`) proves the same proposition as `Ker.kThetaVector`, with its own lemmas (`std_line`, `fourthRoot`, `inter_inter`, `inter_mem_fixedBy`, `evenTheta_spans_thetaSpace`) and a second Weierstrass development.

| Head | In the Pair cone | Called by | Residual cone |
|---|---|---|---|
| `Ker.kThetaVector` | yes | `thM_spec`, `isThM_ne_zero` → `Base.thMM_spec` → … → `vector_bound_link` (the **entireness** clause only) | 3,259 / 2,998 |
| `ThetaVec.thetaVector` | yes | `WeilVac.thMM_spec` → `thetaVector_fourthPower_algebraicGerm`, `WeilVac.thZero_mem` (the **coefficient** clause, `algTAll`) | 1,449 / 1,348, of which 1,389 / 1,348 lie outside the cones of the 15 registered declarations |
| `Ker.Cd.kThetaVector` (registered "equivalent entry point") | **no**; it is in no registered unit cone | — | 0 |

Consequences:

- The hand proof r16:ktheta proves the proposition `ThetaVector`, so it covers all three Lean proofs mathematically. I confirmed the statement identity by reading 437–498.
- The register and `status.json` figures "6,539 theorem lines" (union of the three registered heads) and "2,906 reachable only through them" omit this head. With it the union is **8,373 / 7,887**.
- §r15:translated cites `Base.thMM_spec` (`IsAdmissibleFlagPair…lean:218–220`) for the four-copy identity. Lean's coefficient route uses `WeilVac.thMM_spec` (`ExistsWeilOThZeroTriv.lean:33–36`). `SO.stdOK` is likewise called only by `vector_bound_link`, and `FourthRootStd.stdOK` only by `ta_thMoved` and `thetaVector_fourthPower_algebraicGerm`.

### 3.2 The ε-defined `sgStar`

The translate section works with `f = sgStar(Λ)` for `Λ = lamOf`. In Lean this `TaylorLogMetric.sgStar` is a `Classical.epsilon` choice of an entire odd function with `G′(0) = 1` and the Hermitian multiplier (`IsDiscriminantTwelfthRootOfIdealLattice.lean:238–240`). The kernel's `F₀` uses the explicit `F.th0 B.L`. Lean identifies the two by `OddTheta.sgStar_eq` and `thetaZero_periodLattice_eq` (existence from the canonical σ, uniqueness by the one-pole argument, plus `areaOK`). The text treats them as one function and never says why. The argument needed is exactly the uniqueness paragraph of r16:ktheta-line applied to `σ*`. One sentence closes it.

## 4. Task 2

### 4.1 Is the deferral loop broken?

Yes.

- **Text.** §r15:translated (433–441) states that `thMM` is an epsilon choice and points to §r16:ktheta and §r16:stdok for the two supplies. The supplier-table rows for `thM_spec`, `isThM_ne_zero`, `SO.stdOK`, `FourthRootStd.stdOK` are now class N with a section reference, and the `algTAll` row describes the hand route. §r16:stdok ends in base fields, `Base.latAll` (confirmed) and elementary algebra. §r16:ktheta ends in `StdData` hypotheses and the DLMF citations. Neither refers back to translated coefficients.
- **Graph.** The cone of `Ker.kThetaVector` contains none of `algTAll`, `translate_entire_algebraic`, either `stdOK`, `latAll`, `coefIn_translate`, `theta_line`. The same holds for `ThetaVec.thetaVector`. The cones of the two `stdOK` contain neither theta-vector head nor `algTAll`; `SO.stdOK` contains `latAll`, whose cone contains none of the others.

### 4.2 Is §r15:translated a single, complete, correct hand proof?

It is one location (415–604), and the statement at 417–423 matches `TranslateEntireAlgebraic.lean:15–18` (`m > 0`, `m·x ∈ La(L,L′)`, entire, coefficients in `Q̄`). I recomputed each paragraph.

- **Elliptic germ.** `Δ = 1` gives `j = 1728·g₂³`, so `g₂, g₃ ∈ k`. `f^ρ = f·exp(cz²)` with `2c = s − ρ(s)`: the constant is fixed by `f′(0) = 1`, the linear term by oddness. `f(αz)²/f(z)^{2d}` is elliptic because `αᾱ = d` and squaring removes the signs; it is even with poles only on `Λ`, hence `P(℘)`. Conjugation fixes `α ∈ k` and gives `exp(2c(α² − d)z²) = P^ρ(℘)/P(℘)`; the logarithmic derivative `4c(α² − d)z` must be periodic, so `c = 0`. Correct.
- **Torsion translates.** `Ψ₂ = −℘′(z+u)` and the quadratic exponential cancels (`4 = 2²`). `(log Ψ_l)″ = l²(℘(v) − ℘(lv))` and (23.10.3) give the recurrence; the exponents `(l+1)² + (l−1)² − 2l² = 2` match. `(U_uf)^{h²}·Ψ_h = U_{hu}f(hz) = f(hz)` for `h = 2m`. The coefficient induction is right, and `c₀ ≠ 0` because `u ∉ Λ`.
- **Four variables.** Translation by `(a,a,a,a)` splits on the left by block orthogonality and passes through `γ` on the right by the isometry; the phase `exp(−πiE(γ𝐚, b))` is a root of unity by the `up` bound; `γ` has algebraic entries by `alg_of_span`; the coefficient at `(β,β,β,β)` is a fourth power. `thZero` is a product over disjoint matrix entries and `lat0OK` places each entry of a shift in `(L_M)_ℚ`.
- **Intertwiners and character.** `La(L,L′) ⊆ sat(La(S,S′))`: every generator is `δ·embV(M)` and `n·Nm(𝔠)·δ·embV(M) = δφ₀(Nm 𝔠)·embV(nM)` with `nM` integral. I checked this against `klat_rat` and `klat_mul_mem` (`ThetaTranslationIntertwinerUnitary.lean:94–160`). `Iop` is a finite sum with coefficients `±[A₂ : A₁∩A₂]^{-1/2}`, or zero at index zero. `eNat = chiFac·thMoved`.

Gaps:

1. **Route deviations.** Marked at the head: `coefIn_translate` and `cmTheta_taylorCoeff_algebraic_and_conjugate`. Not marked:
   - Entireness. Lean takes it from `vector_bound_link` (`ProvisionExtensionLink.lean:38–39`, through `vec_mem_ne`, `thMoved_mem`, `thZeroMem_of`). The hand proof gets it directly from finite sums of translates of an entire function.
   - Rational phases. Lean's `rational_points` (`RationalPoints.lean:18–43`) takes integrality of `Im H` on the lattice from conjuncts 3 and 7 of `ThetaLine.theta_line`, a seven-part theorem whose first part (the theta space of a self-dual pair is at most a line) is not used. The hand proof needs only integrality of `E_H` on the standard period lattice. The sentence at 583–585 asserts it without a source; it is `Base.latAll` at the standard pair (§r14:lat-integral).
   - The identity source, §3.1.
2. **`sgStar`**, §3.2.
3. **`chiFac`.** The three lines at 593–597 are a summary. The argument is in §r8:Z4.2.04 and was confirmed at argument level in R8; §r15:pair cites that section, this paragraph does not.
4. **Depth of my reading.** I checked `integral_j_and_algebraic_data` only as a literature substitution (citation numbers verified, hypotheses stated at 445–449), and I did not compare `galSg_all` or `chiFac_mem` with Lean line by line. R15 review A read the same argument once; this is its second reading.

## 5. Root cone

### 5.1 Recomputation

Cone of `pairOK_allSites`: 10,648 declarations, **54,386 / 42,543**, no literature leaf. After removing the cones of Z4.2.01, .03, .05: residual **24,978 / 23,600**. Every R15 figure reproduces.

| Part of the residual | Lines / theorem lines | Status |
|---|---|---|
| 26 site declarations (union) | 2,386 / 2,239 | Confirmed, R15 review A |
| `kerTh_entire_algCoef` outside translate | 1,552 / 1,408 | Confirmed, R14 review B |
| Everything else (assembly, `scal0`, `chiFac`, `detId`, frames) | 653 / 605 | As in R15 review A §4.1 |
| `translate_entire_algebraic` | 20,441 / 19,402 | Below |

The four parts overlap in 54 lines. The translate block splits exactly:

| Piece | Lines / theorem lines | Status after this review |
|---|---|---|
| Cones of the 15 registered declarations (= `Ker.kThetaVector` ∪ the two `stdOK`) | 6,984 / 6,539 | Hand-proved in r16; confirmed in §2. Contains `Base.latAll` (2,145 / 2,008, confirmed in R14) and the σ-theory heads `sgStarQuasi ∪ sgStarBasic` (1,371 / 1,324, cited to DLMF). |
| Reachable only through `coefIn_translate` or `cmTheta_taylorCoeff_algebraic_and_conjugate` | 6,950 / 6,599 | Bypassed by the hand route; marked at the head of §r15:translated |
| Reachable only through `vector_bound_link` | 270 / 247 | Bypassed (entireness); **not marked** |
| Hand-route remainder | 6,237 / 6,017 | Next table |

Hand-route remainder, attributed in this order:

| Head | Lines / theorem lines | Status |
|---|---|---|
| `ThetaVec.thetaVector` (third implementation) | 1,389 / 1,348 | Same proposition as r16:ktheta; **not registered** |
| `integral_j_and_algebraic_data` | 486 / 465 (751 / 730 reachable only through it) | Replaced by Milne 12.16 and Silverman; class L+R in the table |
| `galSg_all` | 381 / 359 | Hand-proved (elliptic germ) |
| `algebraicTaylor_torsionTranslate_evenTheta_alt` | 98 / 91 | Hand-proved (torsion translates) |
| `rational_points` | 2,522 / 2,460 | Hand-proved for what is used; **2,046 / 2,015 are reachable only through `ThetaLine.theta_line`**, whose unused conjuncts are neither proved here nor marked |
| `klat_rat` | 28 / 28 | Hand-proved |
| `chiFac_mem` | 507 / 486 | Argument of §r8:Z4.2.04 |
| Remaining glue (`TA.*`, `Cl`/`Gen` closure, several-variable Taylor support, `WeilVac.thZero_mem`, `algTAll`) | 826 / 780 | Routine; covered by the text's closure statements |

### 5.2 Project-specific pieces neither hand-proved, nor confirmed, nor labelled

| Piece | Lean | Size | What is missing |
|---|---|---|---|
| Third theta-vector implementation | `Mem.Col2.ThetaVec.thetaVector`, `WeilVac.thMM_spec`, `WeilVac.thZero_mem` | 1,389 / 1,348 | A register row and a sentence. The mathematics is r16:ktheta. |
| Theta-line theorem behind the rational phase | `ThetaLine.theta_line` via `rational_points` | 2,046 / 2,015 exclusive | A statement that only integrality of `E_H` is used and that it comes from `Base.latAll`. No proof label for `theta_line` appears in `ch_P_r15.tex`, `ch_P_r16.tex` or the register; if a confirmed proof exists elsewhere, cite it instead. |
| Entireness through the vector link | `vector_bound_link`, `vec_mem_ne`, `thMoved_mem`, `thZeroMem_of`, `qInt_of_stdOK` | 270 / 247 exclusive | A statement that the hand route proves entireness directly. |
| Identification of the two `sgStar` | `OddTheta.sgStar_eq`, `thetaZero_periodLattice_eq`, `WeilVac.areaOK` | inside the pieces above | One sentence (§3.2). |

Together 3,705 / 3,610. None of it is new mathematics for the hand proof: the first row is a duplicate proof of a proposition proved in r16, and the next two are Lean detours the hand route does not take. I found no project-specific step of the Pair statement that the hand route needs and that lacks a hand proof.

Covered only by citation, for the record: σ-theory under `sgStarQuasi ∪ sgStarBasic` (1,371 / 1,324), the second Weierstrass development under `ThetaVec.thetaVector` and `galSg_all` (about 950 lines in `HasSumLocallyUniformlyWeierstrassZetaExcept`), and CM integrality of `j` (751 / 730).

## 6. Unit verdict for Z4.2.04

**APPROVE AFTER MINOR EDITS** as an unconditional completion.

Both conditions of the R15 conditional grade are now discharged by hand proofs that match their Lean statements and that I could recompute: `B.StdOK` for every base (§r16:stdok, 9 declarations) and the fourth-root theta law (§r16:ktheta, 6 declarations). The translate argument has a single location, states its epsilon choice and its two largest route deviations up front, and no longer defers to an unowned input. The three citations R15 review A could not verify are correct.

Required edits (the grade should change only after E1–E4):

- **E1.** Register `GlobalTheory.Mem.Col2.ThetaVec.thetaVector` (`PeriodLatticeSesquilinearFormIsHerm.lean:437–498`) as an entry point of r16:ktheta. Mark `Ker.Cd.kThetaVector` as outside the Pair cone or drop it. Correct the figures that depend on the union: 6,539 → 7,887 theorem lines with the third head, and recompute "2,906 reachable only through them".
- **E2.** In §r15:translated, cite `WeilVac.thMM_spec` (`ExistsWeilOThZeroTriv.lean:33–36`) for the four-copy identity used by `algTAll`, and say that `Base.thMM_spec` / `Ker.kThetaVector` enter the Pair cone through the entireness clause.
- **E3.** Add to the head of §r15:translated the three unmarked deviations with their sizes: entireness (`vector_bound_link`, 270 / 247), the rational phase (`theta_line`, 2,046 / 2,015), and cite `Base.latAll` at 583–585 for integrality of `E_H` on the standard period lattice.
- **E4.** Add one sentence identifying the ε-defined `sgStar(Λ)` with `σ·exp(−s₂z²/2)` (existence, and uniqueness by the one-pole argument of r16:ktheta-line), and one sentence in r16:ktheta-line that Lean's `wSigma`, `wZeta`, `wEta`, `s2` are the DLMF objects under Lean's division convention.
- **E5.** In r16:ktheta-transport, say that `E` is integral on each lattice before `D_xD_y = D_{x+y}`.
- **E6.** Fix the line ranges in §2.2; use one URL for Milne's notes; add one reference for the number-field facts; point the `chiFac` sentence at §r8:Z4.2.04.
- **E7.** After the edits, set the 15 rows and the unit candidate to reviewed in `R16_pending.json` and `status.json`, and replace the Z4.2.04 `remaining_input` and `basis` strings.

Limits of this approval:

- It rests on earlier confirmations I did not redo: the 26 site declarations (R15 A), the finite expansion and `Base.latAll` (R14 A and B), `chiFac` (R8).
- The CM integrality step is a literature substitution for a Lean theorem proved from `q`-expansions; I verified the citation, not the Lean proof.
- All reviews so far are by AI reviewers; `status.json` records zero human sign-offs.

## 7. What was and was not read

Read in Lean (original numbering): `IsSemiChar.lean`, `ProductThetaMem.lean`, `LineTransport.lean` (definitions); `Th0CharMulOpUTh0HalfPeriodEq.lean:1–310`; `LogarithmEquivalence.lean` in full; `MatrixFormFourfoldBlockFirstBlockEmb.lean` in full; `SemiChar.lean`, `QuasiPeriodConstUnique.lean`, `ThetaZeroLogDerivative.lean:1–90`, `ThetaZeroTranslateProduct.lean:1–65`, `EvenThetaSecond.lean`, `HermHalfRight.lean:83–129`; `LateralTheory.lean:1–215`; `IsAdmissibleFlagPair…lean:1–110, 176–225, 300–445, 615–650, 730–816`; `PStdOK.lean` in full; `PStdChar.lean:100–360`; `SpanRangeEmb4EqTop.lean:1–35, 250–300, 345–400, 586–709`; `PLinkThU.lean:205–270, 385–415, 520–545`; `DataHost.lean:147–160`; `TranslateEntireAlgebraic.lean`, `GaloisGeometry/AlgTAll.lean`, `VacuumEntireAndNormalizedJetsAlgebraic.lean:60–320`; `ExistsWeilOThZeroTriv.lean:20–105`; `PeriodLatticeSesquilinearFormIsHerm.lean:215–320, 436–500`; `RationalPoints.lean`; `ThetaSpaceSelfDualPairAtMostLine.lean:252–296`; `ThetaTranslationIntertwinerUnitary.lean:94–160`; `IdealPeriodLatticeOfCurveDatum.lean:130–160`; `OddThetaFunctionExistenceUniqueness.lean:100–150`; statements of `InterReps`, `InterFixed`, `InterTh`, `ThIsom`, `induced_type`.

Not read: the Lean proofs of the σ-theory (`SigmaQuasi.lean`, `SigmaBasic.lean`, `Legendre.lean`, `EllipticOnePole.lean`), the bodies of `InterReps_of`, `InterFixed_of`, `InterTh_of`, `ThIsom_of`, `galSg_all`, `integral_j_and_algebraic_data`, `coefIn_translate`, `chiFac_mem`, `of_dual_families`, `hermitian_form_integral_values`, `self_dual_lattice`; `ch_P_r15.tex` outside the ranges named at the top; §r16:pilot and the Z1.5 triage files (out of scope); Silverman and DLMF §23.3.

## Short summary

- All 15 registered declarations match their Lean statements and their hand proofs are correct: 13 CONFIRMED, 2 CONFIRMED WITH GAPS (a missing definitional sentence and a register error). The DLMF, Milne MF 12.16 and Milne FT 9.29 citations are accurate.
- The deferral loop is broken, in the text and in the graph. §r15:translated is now one complete, correct hand proof of `translate_entire_algebraic` and `algTAll`, with two of its five route deviations marked.
- Root cone 54,386 lines, residual 24,978 / 23,600, translate block 20,441 / 19,402; all prior figures reproduce. New: a third Lean proof of the theta-vector theorem (`ThetaVec.thetaVector`, 1,389 / 1,348) sits in the cone unregistered, while the registered `Cd` entry point is not in the cone; 2,046 / 2,015 lines hang only on `theta_line` and 270 / 247 only on `vector_bound_link`, both bypassed by the hand route but unmarked. Total unlabelled: 3,705 / 3,610, none of it mathematics the hand proof lacks.
- Unit verdict: **APPROVE AFTER MINOR EDITS** for unconditional completion of Z4.2.04, with edits E1–E4 required before the grade changes. The approval rests on earlier AI confirmations and has no human sign-off.
