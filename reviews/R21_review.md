AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

# R21_review

AI review report produced during this project; file names are internal working names.

- Internal source file: `out/R21_review.md`
- SHA-256: `9e241d4b6e07b744eaa2c025e6c6ef9e8567170923b4f9a928dc4a1d5b08b7fc`
- Report scope: R21 manuscript v1 — independent review

## Internal report

The report below preserves its original verdict, scope and unresolved points. Superseded graph percentages have been removed from this public edition. Source line numbers in other records count from its original title.

# R21 manuscript v1 — independent review

Object reviewed: `main.pdf` (127 pp., "From the Selmer window to Dirichlet zero-free statements", manuscript v1), with `R21_report.md`, `R21_split_nodes.json`, `R21_pending.json`, the previous review `R20_review.md`, the pinned Lean tree `40e56bab`, and the dependency graph cache.
Reviewer: an AI model reading cold. Nothing here is a human or specialist check.

Method.
- Lean statements were read through `git show 40e56bab:src/...`, so line numbers are the original ones.
- Weights were recomputed from `graph_cache.bin` with my own dominator-tree computation (root `allChi`, traversal stopped at `lit`, weight = source span of `core` declarations). It gives 9,567,045 core lines, and it reproduces the `dominated` value of all 52 split nodes exactly (0 mismatches), the 32 Lean-only disjoint shares (sum 6,472,125), and the Related sum 505,202.
- References were checked by fetching the cited URL where one opens; each row in §3 says "online", "memory" or "unverified".
- Pages 5, 6 and 19 were rendered and read as images to resolve formulas that `pdftotext` flattens.

## 0. Verdict

- **No sentence claims RH is proved.** Page 1 says so, and the ten goal statements are typeset "Formal statement (Goal: …)".
- **All six R20 must-fix items are fixed** (§1). One R20 minor item (P128 wording) is only half fixed.
- **§2 is accurate.** Every displayed formula matches Lean. It is a correct map, and from "How does the lattice inequality detect primes?" onward a number theorist can follow it. The first half still does not say what the lattice is, where the Selmer sum enters it, or where the exponent 1/2 comes from (§2.3).
- **The 52 split statements are faithful** where I unfolded them (31 looked at, 17 unfolded to the definitions). All three Cited entries match their sources. No fabricated reference among the 13 distinct works cited for the Cited and Related nodes: 8 confirmed online, 5 from memory or unverified.
- **The next split will not work the same way.** The dominator tree under the big Lean-only nodes is flat: T02 has 53,280 immediate dominator children in the historical 1,847,425-line index region. T01 has a similarly flat tree. These two nodes are shared libraries, not theorem trees (§4).
- **Citation cannot close most of the gap.** Declarations I can name as "published theory re-proved" jointly dominate about 0.36M lines. My best guess for the cite side of the 6.47M Lean-only lines is about 0.9M (range 0.4–0.9M); about 5.6M is project-specific (§4.3).
- **Both pending hand proofs (P096, P134) are correct as far as I can check**, and their statements match Lean (§5).
- **Glossary: 16 of 30 entries checked, all agree with Lean**; 13 line locators checked, all exact (§6).

## 1. R20 must-fix items

| Item | Status | Evidence |
|---|---|---|
| Status vocabulary | **FIXED** | "approved", "confirmed", "expert", "discharges" occur 0 times. "Independent review" on p. 1 is now "AI skeleton cross-review (R19)" and "AI manuscript cross-review (R20)", with "No human sign-off is recorded in these files". The six labels are defined on p. 4 and called "editorial judgments by AI". |
| Formal statement vs Theorem | **FIXED** | 113 "Formal statement" headings and 32 "Theorem" headings. RH is "Formal statement 5.1 (Goal: The Riemann hypothesis in Mathlib's formulation)". The `Theorem` environment is used only where the status line is "Proved here (full)". |
| "What remains" totals | **FIXED** | §10 (p. 92) counts 110 parents and 7,026,361 exclusive lines without a full derivation or exact citation, names the ten goals, P015, P017, P020, P027, P034 and P041–P044 as included, and lists 5,193 lines as an index weight. It says the weights "do not count independently verified lines". |
| Attribution | **FIXED** | L. Alpöge is named on p. 1 and as reference [1], with the commit. The PDF link goes to `github.com/leanprover-community/riemann-hypothesis/tree/40e56bab…`. The Blueprint is one numbered reference [3]; there is a 42-item bibliography. |
| Audit citation | **FIXED** | Reference [2] links `https://math.mit.edu/~drew/grh/`. I fetched it: the page is titled "RH Lean proof: verification files", by Andrew Sutherland, last updated 2026-11-23 23:45 UTC. It reports module replay passed, nanoda and con-leche accepting, both kernel modes accepting, standalone Comparator v4.33.0 passed, and `lake comparator` v4.36.0 still running. The paragraph on p. 4 says exactly this and adds that the manuscript did not repeat the checks. |
| P015 / P017 demotion | **FIXED** | Both are "Lean only" (p. 37–38) with a "Route in the formalization" paragraph in place of a proof, and both are split (B05–B07, B08–B10). |

Other R20 items, checked in passing.
- Fixed: the indicative mood in the introduction; the P020 wording ("The Lean proof uses five intermediate results beyond the displayed hypotheses … outside this outline"); the positivity counterexample g(u) = −e^{βu} (p. 46); one weight metric with a comparison table; depth 4–7 moved to appendices; the literature record described as closed Lean terms whose bodies lie outside the counted cone.
- Half fixed: P128 (p. 113) still says the Dummigan–Schönnenbeck reference "gives the lattice action and its stabilizer". Formula (8) there is the factorisation of the stabiliser only. Delete "the lattice action and".
- Residual: internal codes N003 and N478 appear four times in §10.2 without definition.
- Residual: two totals, 9,567,245 (five-root graph) and 9,567,045 (`allChi`), sit a page apart. Both are right, but say in one clause that the difference is the five wrappers.

## 2. §2 "Mechanism of the Selmer-to-zero-free implication" (pp. 5–6)

### 2.1 Formula-by-formula check

| Claim in §2 | Lean | Result |
|---|---|---|
| h_ℓ(E,k) is the Z_ℓ-length of the kernel of localisation on H¹ with coefficients (Q_ℓ/Z_ℓ)(−k) | `shaLen D e = Module.length ℤ_[l] (Sha D e)`, `Sha = Sha1 (qzTw D e) (locFam D.S D.A)`, `qzTw = scalRep (QZ l) (D.chi ^ (-e))` (`Statement.lean:67–78`) | exact |
| h_ℓ(E,k) < ∞ for 1 ≤ k < t, and Σ_{ℓ∈T} log ℓ Σ_{1≤k<t} h_ℓ(E,k) ≤ exp(x^ε/2), t = ⌊x^401⌋, for all local data and all finite T | `VVle E ⌊x^401⌋₊ (√exp(x^ε))` in `VAt`, `VWin = ∀ψ, VWinAt ψ 401` (`ExistsPageN.lean:12–49`) | exact |
| 0 < ε < 1/52; 2^{e(x)} ∈ [x^{2+8ε}, 2x^{2+8ε}]; ∃ J ≥ 1, X₀; for X ≥ X₀ and each admissible (q,d) at X^{1/J} some [Y,Y²] ⊂ [X^{1/J}, X]; the interval may depend on the pair | `VWinAt`, `PageN`, `WinPair` | exact, including the quantifier order |
| Host on windows of exponent 3/2; request = Selmer bound at rank t with budget √b plus explicit-formula condition for the cyclic level | `supplyChi : VWinAt ψ 401 → HostExW (3/2) (GChi ψ).req`; `GChi ψ = EAtH (Level.cyc ψ) … 4 ∧ VVle H.E t (√s.b)` | exact |
| Connectedness fixes e_D, e_L, ε₁ > 0 before ε; for each 0 < ε < ε₁ a family tied at every large scale of its windows | `FamilyClassConnected` (`DivinNOfHypV.lean:13–15`), `TopG` (`ZeroFreeAllOfTopG.lean:12–14`) | exact |
| Ga + μ_CC − K5 − Lo ≤ s | `s_lower5`: `D.Ga u0 + D.muCC u0 - K5v5 D C u0 - wmean (D.d u0) (Lo5 …) ≤ D.s u0` | exact |
| s ≤ μ_CC + log\|W(u)\| + Φ | `SlopeIneq`, with Φ = (1−δ)^{-1}(4u_F log(1+HH/u_F) + (η+4√e)HH) | exact; see omission 5 |
| ASK(u) ≤ MAIN(u) + Err(u) under eleven lattice hypotheses | `PointwiseBoundVariant`: eleven hypotheses (`hS hDIV hE hH hCount hSl hSN hLoss hSI hHH hFP`), conclusion `D.ASK u0 ≤ D.Main u0 + ErrX5at D C Xpp u0` (`LevelOfCongruence.lean:175`) | exact |
| ASK term at an inert prime: 2 log p (a/p^i − w)₊; at d a sum over an inertia coset with coefficient log d | `askP`, `askD`, `ASK` (`FirstPrimeNeSecondPrime.lean`) | exact; the sum is over those i with i·Frob_p ∉ Φ, which §2 leaves out |
| MAIN = a(log a − 1 − γ + Re ℓ(χ_C) − (1/f) Σ_{ρ∈Γ_Φ} log w(ρ)) | `MAIN ell a w` | exact (rendered formula on p. 6 has the outer parentheses) |
| Γ_Φ is the index-two subgroup, χ_C its quadratic character | `InPhi g := g.1.1 = 0` on (Z/2 × Z/2) × H; `chC` | exact |
| gap(u) ≤ x^{(e_Div+e_Loss+3)ε}·Br | `ch_top` gives x^{CErr·ε}·Br; `core_gm` relaxes with CErr ≤ e_D + e_L + 3 | correct; write e_D, e_L (the upper bounds), which is what the next display uses |
| G_L(x) = G_1(x) + Σ_{χ∈K∖{1}} a_χ Re G_χ(x) ≤ x^{1/2+(e_D+e_L+7)ε} on [Y, Y^{3/2}] | `core_gm` conclusion `Λ.Gm x ≤ x^(1/2 + (eD+eL+7)·eps)`; `ch_core` gives x^{1/2+(C+3)ε} + Σ\|G_ξ\| with C = e_D+e_L+3, and the discarded sum is absorbed by one factor x^ε | exact |
| G_χ(x) = Σ_{n≤x} Λ(n)χ(n)(x/n − 1) + x(L′/L)(1,χ); principal term with −x log x + (1+γ)x | `GPsi`, `Gz` (`StatementOC.lean:17`) | exact |
| Residue −(1/(ρ(ρ−1))) Σ a_χ (m_χ(ρ)+m_χ(ρ̄))/2; real poles positive | Mellin transform of Σ Λ(n)χ(n)(x/n−1) is −(L′/L)(s)/(s(s−1)); Re G_χ = (G_χ + G_χ̄)/2 and the zeros of L(s,χ̄) are the conjugates. For 0 < β < 1, −1/(β(β−1)) > 0 | correct (recomputed) |
| Windows in u = log x are [log Y, (3/2) log Y]; Landau window excludes poles in Re s > θ | `landau_window` (`landauWindow.lean:83`), `zeroFree_of_rpow_window` (`ZeroFreeOfRpowWindow.lean:11`) | exact |

All twelve file locators in §2 open the stated declaration at the stated line.

### 2.2 Errors

None found. Two imprecisions.
1. "Cancelling μ_CC and identifying the arithmetic part of K5 gives ASK(u) ≤ MAIN(u) + Err(u)". The cancellation gives Ga ≤ MAIN + … (`Ga_bound5`). The step from Ga to ASK uses the loss hypothesis ASK − Ga ≤ LoP (`LossBounds`, used as `h4` in the proof). Add one clause.
2. The gap display uses e_Div, e_Loss, and the next display uses e_D, e_L. Say that the first are bounded by the second.

### 2.3 Omissions that stop a number theorist

1. **Where the Selmer sum enters the lattice.** The section asks "How does the bound enter a lattice?" and answers with hosts and requests. The actual entry point is `LinkN_at` (`GlobalTheoremInputs.lean:32–35`): η_j ≤ d_{Z0,j}·[C(f·m·b·L² + (log x)²·N_c) + Σ_ℓ v_ℓ], where Σ_ℓ v_ℓ is the weighted Selmer sum (`vvRecord` in `DivinNOfHypV.lean` turns `VVle` into `Σ' vvTerm ≤ B`). The manuscript prints this inequality on p. 18 under B05. §2 should quote it: it is the one line where h_ℓ(E,k) touches the slope data.
2. **What the lattice is.** "Global lattice", "lattice word", "quotient slopes minus heights" and "comparison slope μ_CC" are used without saying which lattice (of what rank, over which ring, attached to which automorphic or geometric object) or why its slopes see primes of E. One sentence on the object and one on why its Arakelov-type degree has a prime-by-prime expansion with terms (a/p^i − w)₊ would do.
3. **Where 1/2 comes from.** The exponent is stated, not explained. In Lean it is the rank numerology: `RankVal` fixes m between √(x^{1−ε/8}) and twice that, `ch_core` assumes x^{1/2−ε} ≤ m ≤ x^{1/2+ε/2} and x·m ≤ k, and the gap bound is divided by m·b·δ₂/2 (`ChCore.lean:322–338`). Say that the number of columns is about √x and that this is the source of the critical exponent.
4. **The host is a field.** §2 says a host "fixes a finite abelian group, Frobenius and inertia data and a set of test translates". In Lean a host carries the Galois number field E itself (`HostRaw.E`, with √−d, √−q, a cyclotomic embedding and an Artin map). The Selmer request is `VVle H.E t √b` on that field. Without this the "field of type (ψ, e, q, d)" of the first paragraph and the host of the second are not visibly the same object.
5. **Which side is assumed.** The lower slope estimate is derived (`s_lower5`, from the DIV, slope, count and quotient-slope hypotheses). The upper one is itself one of the eleven hypotheses (`SlopeIneq`). §2 presents them symmetrically.
6. **b = exp(x^ε).** The budget is exp(x^ε/2) in the first paragraph and √b in the second. `Scale.b := exp(x^ε)` is never stated.
7. The localisation in h_ℓ is at the places above ℓ only, and the cohomology is that of the Galois group unramified outside those places (`LData.S = Above F l`). "For the prescribed local data" hides this.

Is it an accurate two-page account a number theorist could follow? Accurate: yes. Followable: the analytic half yes; the arithmetic half only as a list of names until items 1–4 are added. They need about fifteen lines.

## 3. The 52 split statements

Counts confirmed: Cited 3 / 6,445, Related 17 / 505,202, Lean only 32 / 6,472,125, union 6,983,772.

### 3.1 Cited (3)

| Node | Statement vs Lean | Reference | How checked |
|---|---|---|---|
| T19 `resolution_char_zero_of_literature` | exact against `ResolutionCharZero`: k of characteristic 0; X locally of finite type, quasi-compact, separated, reduced; blow-up sequence; X′ smooth; isomorphism over the smooth locus; reduced preimage of the complement is SNC | Kollár, *Resolution of singularities — Seattle lecture*, Thm 36(1)–(3) | **online** (arXiv math/0508332, machine-read): Theorem 36 defines a blow-up sequence functor on all schemes of finite type over a characteristic-zero field with conclusions (1) smooth, (2) isomorphism over the smooth locus, (3) preimage of Sing X is an SNC divisor. Matches; Lean adds "reduced" and "separated", so it is a special case. |
| T20 `principalisation_char_zero_of_literature` | exact against `PrincipalisationCharZero`: X smooth of relative dimension d; I vanishing on no component; boundary E with SNC at each point; centres compatible with the boundary; pullback of I effective Cartier with SNC support; isomorphism off the cosupport | Kollár, Thm 35(1)–(3) | **online** (same source): hypotheses and conclusions (1)–(3) match. |
| W11 `ferreroWashington` | exact against `Published.FerreroWashington`: K abelian over Q containing μ_ℓ (μ_4 for ℓ = 2); ∃ r, for all n and all K′ with `IsCyclotomicExtension {ℓ^n} K K′`, \|Cl(K′)/Cl(K′)^ℓ\| ≤ ℓ^r | Washington, 2nd ed., Thm 7.15 and Prop. 13.23; Ferrero–Washington 1979 | **memory**: Thm 7.15 is μ = 0 for abelian fields, Prop. 13.23 is "μ = 0 iff the p-rank of A_n is bounded". Springer text not re-fetched. The deduction on p. 32 (the root-of-unity hypothesis puts every K′ in the cyclotomic Z_ℓ-tower) is correct. |

Disposition "Cited" is right for all three. Two remarks.
- `IsBlowupSeq`, `IsSncBlowupSeq` and `FinalTheorems.Snc` are project definitions. I did not compare them with Kollár's. A Cited entry should say that this comparison was made, or say that it was not.
- These three statements have dominated weights 35, 1,572 and 4,838 but inclusive weights 121,633, 100,762 and 54,293. The Lean development contains closed terms for them. The manuscript says so for T19 and T20 ("uses a closed resolution term independently of its record argument"); say it for W11 too.

### 3.2 Related reference, proof in Lean only (17)

| Node | Statement vs Lean | Reference | How checked | Disposition |
|---|---|---|---|---|
| B01 `galoisRepresentations_of_thetaLift` | structure exact: `TLiftK → Row0b recT`, proof term = B03 applied to B02. Clauses of `Row0b` not unfolded | BLGGT Thm 2.1.1 | memory (confirmed real in R20) | right |
| B03 `galoisLocalGlobalStrong_of_geometry_lift` | exact: `GeoOne → TLiftK → Row0b recT` | BLGGT Thm 2.1.1 | memory | right |
| B04 `recTExists` | clause list on p. 17 consistent with the name `RecTExists`; not unfolded | Scholze, LLC for GL_n, Thm 1.2 | **online**: (a) characterisation by traces, (b) parabolic induction, (c) bijection on supercuspidals, (d) twists, central characters, duals, L- and ε-factors. The note on p. 17 is accurate | right. The JSON says "1.2(a)–(d)", the PDF "1.2(c,d)"; align |
| T09 `functionalsSeparate_of_howeUnram_of_siegelWeil` | hypotheses exact (`ThetaLocalInputs`, `HoweUnram`, `SiegelWeilUnitaryConvergent`); conclusion not unfolded | Yamana, Pacific J. Math. 264, Thm 2 | **online**: paper and Theorem 2 exist | right |
| T11 `theoremK_head2` | exact at the level of names: `EisBL → SiegelWeilStd → ThetaIntegralsAgree ∧ LocalMatching` | Yamana Thm 2 | online | right |
| T12 `siegelWeilStd` | **exact against `SiegelWeilStd`**: good base, m, n ≥ 1, opposite Hermitian/skew signs, min(r,s) = 0, Hecke character restricting as η^m, doubling model, frame, standard K, height, Haar measure with fundamental domain, K-finite Schwartz vector; value at s₀ = (m−n)/2 is (1 if n < m, else 2) × the theta average | Yamana Thm 2 | **online**: value at s₀ equals κ·I(g;φ), κ = 2 if m ≤ n, κ = 1 if m − r > n, r the Witt index. With min(r,s) = 0 the space is anisotropic and both cases are covered. "The printed identity has the same two multipliers" is accurate | right; the closest of the 17 to Cited |
| T16 `chow_form_height_comparison` | **exact**, including the leading hypothesis `PublishedHodgeBundleTheorems` and the bound a ≤ `[K:Q](D+1)`·d·(imageHeight + t) | Bost–Gillet–Soulé, JAMS 7, Thm 4.3.8 | **unverified** (paper is real; item number not fetched) | right |
| T17 `moriwakiBig_outright` | closed term for `MoriwakiBigStatement`; statement not unfolded | Moriwaki, *Continuity of volumes on arithmetic varieties*, Cor. 5.5 | **online**: the introduction's Theorem A is marked "cf. Corollary 5.5": for nef L̄, log #{small sections of mL+N} = (deg ĉ₁(L̄)^d / d!)·m^d + o(m^d), hence vol = deg. Section 5 itself lay beyond the fetched part | right |
| T18 `hsUse_outright` | closed term for `HSUse`; three clauses not unfolded | Moriwaki Cor. 5.5 | online, as above | right |
| T21 `poincare_lelong_inv_of_literature` | not unfolded | Demailly, *Complex analytic and differential geometry*, III (2.15) | **memory** (Lelong–Poincaré equation); the site refused automated access | right. The JSON gives a different URL (ime.usp.br) from the PDF (www-fourier.ujf-grenoble.fr); align |
| T22 `zarhin_statement` | consistent: abelian scheme over a valuation ring R with relatively ample sheaf; i, r with r∘i = 1; P abelian with a rigidified symmetric relatively ample sheaf with trivial polarisation kernel | Milne, *Abelian Varieties* v2.00, Thm 13.12 | **online**: "Theorem 13.12 (Zarhin's trick). For any abelian variety A, (A × A^∨)^4 is principally polarized", in a section assuming k algebraically closed | right; the stated difference (field vs valuation ring) is the real one |
| T23 `nef_rr_of_literature` | not unfolded | Lazarsfeld, *Positivity I*, Cor. 1.4.41 | **memory** (asymptotic Riemann–Roch for nef divisors) | right |
| T24 `fargues_exact_of_literature` | not unfolded | Fargues, *La filtration canonique…*, §5.3 | **unverified** | right |
| W02 `baseChangeN` | **exact against `BaseChangeIsobaricN`**: E CM, unramified over E⁺ at every finite prime, n ≥ 1, any automorphic π of the definite unitary group; partition, constituents, local components, infinitesimal characters | Labesse, *Changement de base CM et séries discrètes*, Cor. 5.3 | **online**: weak base change for σ in the discrete spectrum with property (∗) and discrete series at infinity; partition n = n₁+…+n_r | right, with one more difference to record (below) |
| W04 `descWeak` | **exact against `DescWeak`**: 2 ≤ n ≤ 4; S finite, containing the places above p, all split; π regular algebraic cuspidal, conjugate self-dual, Satake data outside S; σ unramified at every nonsplit place, same Satake multiset at cofinitely many split places | Labesse Thm 5.4 | **online**: descent of θ-invariant cohomological cuspidal π; E/F unramified at finite places and U quasi-split at inert places are assumed | right; the note on p. 30 is accurate |
| W05 `lemmaK_litN_alt` | **exact against `LemmaK`**: L totally complex with μ_ℓ (μ_4 for ℓ = 2), e ≥ 1, H²(Z_ℓ(e+1)) finite, log # ≤ exp((2e[L:Q])^{C_K}·log(2D)) | Soulé, Doc. Math. Extra Vol. Kato, §4.3 Thm 3 and §4.4 Prop. 4(i) | **online**: Theorem 3 bounds a product over primes p ≥ 4n−1 and p ≥ r+2; Prop. 4(i) is log log k(m) ≤ 220·m⁴ log(m)·r^{4r}·√D·log(D)^{r−1}. The note on p. 31 (with n = e+1 the needed prime ℓ ≤ r+1 is outside the product; different discriminant dependence) is accurate | right |
| W07 `katoTwoW_of_printsH` | hypothesis list on p. 31 plausible; `KatoTwoW` not unfolded | Kato, Astérisque 295, Thm 14.2(1) | **unverified** (item number not fetched) | right |

One difference the manuscript does not record: by the fetched text, Labesse's §5 has the standing hypothesis that F is totally real of degree at least 2. `BaseChangeIsobaricN` and `DescWeak` quantify over every CM field, including imaginary quadratic ones. Add this to the notes for W02 and W04, after checking the source.

### 3.3 Lean only: the eleven I compared

| Node | Result |
|---|---|
| T01 `every_character_of_theta_integrals_local_matching` | exact: seven inputs (P, F, theta agreement, local matching, covolume bound, `RecTExists`, `VWin`) → `EveryCharacter` |
| T02 `nonempty_hyps_definite_side_of_closed_bound` | exact: five inputs, `RecTExists`, the linked bound at two and three for every real c → `Nonempty (HypsAlt S0.NL DefiniteSideCondition)` |
| T03 `hypotheses_nonempty_of_unramified_exponents_alt` | exact: P, `RowRat`, h, c, A with `EvLgG A`, three linked conditions |
| T13 `topCovolSlim2_use_alt_alt` | exact: fifteen inputs (eight of T17–T24 kind, seven published geometric) → `CovolumeBoundOfX` |
| T14 `deep_slim_use` | exact: the eight statements → `DeepStR` |
| T26 `deepStR_of_use` | exact: ten inputs, listed in the same order on p. 29 |
| W01 `automorphic_window_of_inputs` | exact: `OpenImageCondition`, `BaseChangeIsobaricN`, `RowT` → `VWin` |
| B05 `shape_closed_link_n_of_green` | exact in shape: `Green → TopShapeAlt True True (Closed … LinkN) TopG`; the displayed inequality on p. 18 is `LinkN_at` term for term |
| B07 `supplyChi` | exact |
| B08 `core_gm` | exact: quantifier order (x₁ before frame, host and TT), exponent 1/2 + (e_D+e_L+7)ε, and the `EAtH` and `CoreAtH` fields as paraphrased |
| B09 `ch_core` | **exact, checked field by field**: C ≥ 0, ε > 0, \|c\| ≤ 1; m ≤ x^{1/2+ε/2}, x·m ≤ k; `SizesA`, `ThinScales` (\|G_ξ(y)\| ≤ y·θ for y ≥ X′/3: a product, confirmed on the rendered page), `CostWindows`, `RestSize`, `CharsA`; bracket Br = n_T·a_E(1+m²/k) + m(2nmb·x^ε + n₂kb·x^ε/(n²x^{−ε})); conclusion with exponent 1/2 + (C+3)ε |

B02, B06, B10 and the remaining Lean-only nodes were read but not unfolded. For B02 the statement on p. 16 is a paraphrase of `GeoOne` that I could not check from the PDF alone.

## 4. Next-level split of the twelve largest Lean-only nodes

Sizes: **net** = dominated core lines with the already selected sub-nodes removed. "Disjoint" is the R21 share of the node. Dispositions are guesses from declaration names and statement heads, not from a literature search. Candidate sources named in the last column are unverified pointers for whoever does that search; none is a checked locator.

### 4.1 A structural finding first

Dominance does not split the two largest nodes.

| Node | Disjoint | Immediate dominator children |
|---|---:|---:|
| T02 | 1,847,425 | 53,280 |
| T01 | 548,334 | 21,000 |
| T15 | 205,928 | 2,465 |
| T03 | 274,375 | 5,615 |
| B02 | 625,495 | 169 (one wrapper, then flat) |
| W01 | 480,551 | 4 (one wrapper, then flat) |
| T26, T04, T05, T06, T07, T08 | 169,776–481,067 | 1–2,678 |

T02's direct proof-term dependencies are T03, T05, T08, T09 and T10, which are already nodes. Its own 1.85M lines are declarations that two or more of those branches share, so only T02 dominates them. They are a library, spread over about 9,000 two-level namespaces. The fourteen largest namespaces are listed below. T01 is the same one level up.

Consequence: for T02 and T01 the next manuscript layer cannot be "ten sub-theorems". It has to be chapters of a shared library, cut by subject. The largest subject blocks in T02's region are:

| Namespace | Lines in T02's region | Largest declaration (dominated) | Guess |
|---|---:|---|---|
| `Formalism.FourierDecayAlt` | 234,852 | `…P.CutSE.actual_compact_theorem` (16,589) | project-specific analytic estimate |
| `Formalism.L2` | 152,144 | `…SG.Pf.NcAllC.ncTieC_of_closed` (44,532) | project-specific |
| `ReciprocityTheory.ChartRestriction` (mostly `.DS`) | 68,969 | `…DS.Lap.TopClosed.besselNVG` (21,500) | related: discrete series, Bessel asymptotics |
| `GlobalTheory.Mem` | 42,418 | `…Col2.TC.colsTiedSym_std` (6,985) | project-specific |
| `Formalism.MainNotions` | 40,564 | `…BridgeLemma.word_theorem_a_admissible` (3,424) | project-specific |
| `GlobalTheory.HL` | 32,632 | `…AbstractBound.ngAt` (7,946) | project-specific |
| `PI.UnitaryGroupMassFormula`, `PI.VolStabS`, `PI.AprimeInfW` | 43,660 | `…CntFormula.RowsMassW.row_lattice_mass` (3,207) | related: mass formula for unitary groups |

Module directory names in the cleaned tree are not a reliable subject guide (`Development.AbelianVarietyTheory.Proofs` holds 2.55M of the 6.47M lines and is not about abelian varieties), so I used declaration namespaces.

### 4.2 Proposed sub-theorems

**T02** `UpperTheory.Lit.nonempty_hyps_definite_side_of_closed_bound` — disjoint 1,847,425

| Lean name | Net | Guess |
|---|---:|---|
| `GlobalTheory.RowClaim.Join.thetaLift_row_properties_conj` | 67,993 | project-specific |
| `UpperTheory.Lit.I5.unitary_theory_of_harishChandra_langlands_alt` | 47,081 | project glue over ten named published hypotheses (Harish-Chandra, Langlands classification, Flath, Dixmier–Malliavin, Bernstein–Zelevinsky, Green) |
| `Formalism.L2.SG.Pf.NcAllC.ncTieC_of_closed` | 44,532 | project-specific |
| `GlobalTheory.TypeAsm.TopGap.typeBound_of_gap` | 36,947 | related: discrete series and Bessel models |
| `GlobalTheory.SqTower.tower_alt_bis` | 31,772 | project-specific |
| `GlobalTheory.BpEigen.pointwise_bound_eigenfunction` | 17,357 | related: pointwise bounds for Capelli eigenfunctions |
| `CompanionTheory.WaveGrid.wave_bessel_period_threshold` | 16,122 | related: Zuckerman translation, matrix-coefficient asymptotics |
| `GlobalTheory.FamilyNormRational.squaredGroupSum_classDoubleCoset_eq_rowWeight` | 14,208 | project-specific |
| `Formalism.FourierDecayAlt.P.CutSE.thmPActualCpt_of_spec` | 12,434 | project-specific |
| `ReciprocityTheory.ChartRestriction.DS.Lap.step` | 11,877 | cite or related: Laplace-method step for discrete series |

Use the namespace table in §4.1 for the rest.

**B02** `UpperTheory.Gal.Int.Geo.geoOne_holds` — disjoint 625,495 (one wrapper `geometric_realization_of_weight_one`, 595,445)

| Lean name | Net | Guess |
|---|---:|---|
| `UpperTheory.Gal.LocalSmoothExtension.ksHodge_of_geo` | 30,291 | project-specific (holomorphic Lefschetz plus definite-unitary counts) |
| `UpperTheory.Gal.W2.fixedPoints_int_base_holds` | 28,109 | related: Hecke fixed points and CM cycles via uniformisation |
| `UpperTheory.Gal.Int.Geo.Pl.planEx_holds` | 25,753 | project-specific |
| `UpperTheory.Gal.Seam.HT.htBij` | 23,528 | cite: Hodge–Tate comparison for smooth projective varieties |
| `UpperTheory.Et.EtaleTopology.top` | 21,764 | cite: étale topology foundations (SGA 4) |
| `UpperTheory.Et.purAll` | 16,006 | cite: cohomological purity and Gysin |
| `UpperTheory.Et.E2.main` | 12,772 | cite: étale cohomology foundations |
| `GlobalTheory.UPel.HT.RepFam.smoothOfRelativeDimension`, `GlobalTheory.T.harrisTaylor_typeTj_isogenies_representable` | 11,694; 7,372 | cite: Harris–Taylor moduli of isogenies |
| `UpperTheory.Pbf.pbf_all` (private), `UpperTheory.Et.etale_finiteness_of_duality` | 8,569; 8,566 | cite: projective bundle formula, finiteness and duality |
| `UpperTheory.Ru.crystallineComparison.finAll` | 8,000 | cite: crystalline comparison |
| `GlobalTheory.T.potentialSemiAbelianReduction_of_isogeny` | 8,087 | cite: potential semi-abelian reduction under isogeny |

This is the most citeable node of the twelve: it is the construction of Galois representations in the cohomology of unitary Shimura varieties, with its étale and p-adic Hodge foundations re-proved. The ten "cite" rows jointly dominate 129,126 lines. Name-matched étale, purity and Lefschetz declarations in the region total about 183k and p-adic Hodge about 34k.

**T01** `UpperTheory.Lit.every_character_of_theta_integrals_local_matching` — disjoint 548,334

| Lean name | Net | Guess |
|---|---:|---|
| `Formalism.InvariantFactorPaths.MC.theoremMV7` | 23,098 | not inspected |
| `UpperTheory.Top.zero_free_all_of_green_v_win` (P015 outside B05–B10) | 13,212 | project-specific |
| `Formalism.InvariantFactorPaths.MC.theoremMXB` | 12,984 | related: highest-weight dimension monotonicity |
| `GlobalTheory.NL.wach_used_clauses` | 12,166 | related: Wach modules |
| `Formalism.MainNotions.N.K.normalized_ring_data` | 8,205 | project-specific |
| `Formalism.MainNotions.flipOneThree.Pf.theorem_I_of_finer_open_statements` | 7,530 | project-specific |
| `Formalism.MainNotions.LiftingTheory.local_theory_of_admitted` | 7,135 | project-specific |
| `GlobalTheory.langRecCore_of_artinReciprocity` | 6,696 | cite side: class field theory, local duality |
| `GlobalTheory.Hk.normPrimes_short_interval_lower` | 6,100 | cite or related: prime ideals with norm in short intervals, explicit in the conductor |
| `Formalism.MainNotions.G.ColumnFamilies.splitting_package_holds` | 5,104 | project-specific |

Largest namespaces: `ReciprocityTheory.ChartRestriction.DS` 46,167, `Formalism.MainNotions.G` 40,404, `Formalism.L2.SG` 37,081, `Formalism.HermitianLattices.Ext` 25,024.

**T26** `GlobalTheory.CompanionTheory.Ar.Plug.deepStR_of_use` — disjoint 481,067 (wrapper `Ar.Top.goodTower_and_volume`, 294,784)

| Lean name (prefix `GlobalTheory.CompanionTheory.Ar.`) | Net | Guess |
|---|---:|---|
| `Cusp.volumeTheoremX_of_inputs` | 140,077 | project-specific |
| `Num.TopRel.relations` | 38,845 | project-specific |
| `Plug.SlopeVolM.slope_sub_cost_le_compVolSlope` | 18,932 | project-specific (uses nef Riemann–Roch) |
| `Num.FamEx.TestPt.testFacts` | 18,696 | related: Fargues, Zarhin, quotients by finite flat subgroups |
| `Giv.lineOfLargeDegree_of_use` | 15,650 | related: arithmetic Hilbert–Samuel and bigness |
| `Link.given_of_use` | 13,412 | project-specific |
| `Sl.LineProof.line_of_key` | 11,435 | project-specific |
| `Cusp.TopHt.htU_of_given` | 9,642 | project-specific |
| `TopTower.comp_data` | 7,780 | project-specific |
| `GroundTheory.Heights₂.Heights.NumbersDVR.NumericalSegre.full` | 2,923 | cite: heights and Segre numbers |

The namespace `GroundTheory.Heights₂.Heights` holds 91,083 lines of this region (heights machinery; candidate source Bost–Gillet–Soulé).

**W01** `UpperTheory.One.Join.automorphic_window_of_inputs` — disjoint 480,551 (wrapper `…vwin_of_hypotheses_H_E_alt`, 438,086 net)

| Lean name (prefix `UpperTheory.`) | Net | Guess |
|---|---:|---|
| `V.Pa.core` | 24,255 | related: Taylor–Wiles–Kisin patching |
| `V.HV.Core.of_four_alt` (= P020; W12–W15 may be nested) | 21,873 gross | already a parent |
| `V.Z.Sym.Glob.sideG` | 16,727 | related: symmetric power transfer |
| `V.Z.Desc.V0.numJEDenseThresholdCases` | 10,479 | project-specific |
| `Reformulated.B.Gr34.mem_UC` | 8,016 | project-specific; one declaration with an 8,001-line span |
| `V.Th.core_o_of_literal_automorphy_n` | 7,860 | related: ordinary automorphy lifting |
| `V.Alg.M.core_holds` | 7,506 | project-specific |
| `V.Z.Sym.Unl.half_of_printed_hida` | 6,586 | related: Hida theory |
| `ConvolutionTheory.Sph.ramSph` | 6,201 | project-specific |
| `V.Pa.B2.obstructionBound_of_duality` | 4,198 | related: duality bound for the obstruction group |

`mem_UC` should be looked at: an 8,001-line single theorem is machine-generated and cannot be given a human statement as it stands.

**T04** `GlobalTheory.Fc.AllAtMemberStage0.allRows_of_open0_alt` — disjoint 455,025

| Lean name | Net | Guess |
|---|---:|---|
| `GlobalTheory.CarrierGap.offDiag` (contains `theoremS_leaves_of_carrierG`, 76,966) | 183,266 | project-specific |
| `GlobalTheory.Svd.servH_row_of_artin` (contains `servH_row`, 73,485) | 130,968 | project-specific |
| `Formalism.L2.SG.TheoremS.pbApplied` | 28,178 | project-specific |
| `GlobalTheory.FlagBase.OneClass.bound` | 19,123 | project-specific |
| `GlobalTheory.MomFin.moments_fin` | 18,803 | project-specific |
| `Formalism.FourierDecayAlt.P.built_bounds_compact_of_head_top` | 17,184 | project-specific |
| `Formalism.FourierDecayAlt.P.lemma_model` | 15,339 | project-specific |
| `Formalism.L2.KerInert.AdmLoc2.admissible_entries_small_chain` | 13,156 | project-specific |
| `Formalism.L2.KerInert.integral_inert_of_weakApprox` | 7,159 | related: weak approximation |

The first two rows nest the third to ninth in part. The ten selected antichain heads locate disjoint graph regions.

**T05** `GlobalTheory.Fc.S0.ontoX_and_lamLow_of_unitaryGroupHypotheses'` — disjoint 303,161 (wrapper `BigOn.ontoX_of_hypotheses_alt_alt`, 298,263)

| Lean name | Net | Guess |
|---|---:|---|
| `GlobalTheory.InputsAtRecord.inputsNet_recPlus` | 100,117 | project-specific |
| `GlobalTheory.BigOn.exponent_bound_of_unitaryThetaStandardTheorems_alt` | 45,114 | related: Clozel, ℓ-adic Hecke characters, Chebotarev as named hypotheses |
| `UpperTheory.labelSetGeo_of_even_of_rankOK_of_not_dvd_discr` | 25,046 | project-specific |
| `GlobalTheory.FinalJoin.inputs4_of_net` | 11,008 | project-specific |
| `GlobalTheory.BigOn.Exp.exportSt_of_hypotheses_alt` | 10,030 | project glue |
| `GlobalTheory.MinorShiftJet.window_letterDet` | 8,419 | project-specific |
| `GlobalTheory.CompareOff.compareOffOwn_run` | 6,757 | project-specific |
| `GlobalTheory.LowRow.lamLow_closing_alt` | 4,142 | project-specific |

The table gives the historical weights of the selected dominator heads.

**T06** `GlobalTheory.T.large_unramified_exponent_bundles_exist_alt` — disjoint 280,670 (wrapper `Mem.Top.Bl.exists_baseLattice_of_prime_alt`, 188,022)

| Lean name | Net | Guess |
|---|---:|---|
| `GlobalTheory.Mem.Top.Closing.memberE_closing_alt_alt` | 75,959 | project-specific |
| `GlobalTheory.HeightCounting.Up.all_stages_of_specializations_alt` | 31,788 | project glue over Casselman–Wallach, Weil representation, discrete series |
| `GlobalTheory.TwExportTop.twistAllPowers_of_galoisCohomology_classField` | 22,518 | related: Poitou–Tate, local duality, Bloch–Kato |
| `GlobalTheory.ChainTw.scalars_of_given_all` | 16,432 | project-specific |
| `GlobalTheory.Mem.Top.Bl.exBL_isLinked_prmR_alt` | 9,872 | project-specific |
| `GlobalTheory.LevCmp.stageCExists_of_harishChandra_serN` | 8,863 | project-specific |
| `GlobalTheory.TwInputs.exists_inputs_of_hkSup_galHodge` | 8,277 | project-specific |
| `GlobalTheory.Mem.R3.Rw.datExt_rest` | 7,706 | project-specific |

The table gives the historical weights of the selected dominator heads.

**T03** `GlobalTheory.Fc.S0.StageU.hypotheses_nonempty_of_unramified_exponents_alt` — disjoint 274,375

| Lean name | Net | Guess |
|---|---:|---|
| `PositivityTheory.Rg.Rsw.resCore` | 64,875 | related: regularised Siegel–Weil, residues |
| `GlobalTheory.HeckeMember.heckeInt_transform_readTie` | 20,949 | project-specific |
| `GlobalTheory.RowsAll.locComp_of_isRc_classMapD_cenLoc` | 12,218 | project-specific |
| `GlobalTheory.RawLift.rawLift_main` | 8,987 | project-specific |
| `GlobalTheory.DownLift.GenFinite.gen_of_type_clean` | 6,458 | related: unramified Howe duality |
| `UpperTheory.One.M.unitaryRead_true_alt` | 3,808 | project-specific |
| `GlobalTheory.RawLift.Assembled.rallisConv_of_siegelWeil` | 3,436 | related: Rallis inner product |
| `GlobalTheory.HoweIrrCompact.howe_irr` | 3,320 | cite: Howe duality for compact pairs |
| `GlobalTheory.LowestKType.lowestKType_irreducible` | 2,562 | cite: lowest K-type |

The table gives the historical weights of the selected dominator heads.

**T07** `UpperTheory.GalC.final_alt_alt` — disjoint 222,063 (wrapper `NLinkClose.main_alt_alt`, 150,531)

| Lean name | Net | Guess |
|---|---:|---|
| `GlobalTheory.TheoremT.liftF_of_isGood` | 33,297 | related: crystalline lattices (Bhatt–Scholze, Fontaine) as named hypotheses |
| `Formalism.MainNotions.N.Ln03.local_theorem_of_inputs` | 21,595 | project-specific |
| `GlobalTheory.TopBridge.twistedLatticeCohomology_theoremTOP` | 20,898 | project-specific |
| `Formalism.MainNotions.RamifiedCoefficientChains.Asm.theorem_of_local_lemmas` | 14,763 | project-specific |
| `GlobalTheory.TheoremBAdm.admissible_ranks_of_CMDatum` | 14,416 | related: Bloch–Kato local conditions, local Tate duality |
| `Formalism.MainNotions.N.Ln34.lifting_theorem_of_uniform_link` | 14,338 | project-specific |
| `Formalism.MainNotions.N.FrobeniusPowerSeries.arc_proposition_alternative` | 14,247 | project-specific (Wach lattices) |
| `GlobalTheory.PinClose.locComp_of_isRc_classMapD_cenLoc` | 5,958 | project-specific |
| `GlobalTheory.Pass.stepsNoCut_of_artin_alt` | 5,569 | project glue |

The table gives the historical weights of the selected dominator heads.

**T15** `SelfIntersectionVolumeEstimates.topCovolG_alt_alt` — disjoint 205,928

| Lean name | Net | Guess |
|---|---:|---|
| `GlobalTheory.RefSum.refinedSum_weight_of_size_alt` | 18,240 | project-specific |
| `GlobalTheory.OrbitSep.separate_orbits_by_cusp` | 14,281 | project-specific |
| `GlobalTheory.PolFan.exists_smooth_refinement` | 9,721 | cite: smooth projective refinement of an invariant fan |
| `GlobalTheory.HSShort.geoBound_of_quoted'` | 9,202 | related: explicit arithmetic Hilbert–Samuel, Bertini |
| `MainStatements.Tam.Plug.comp` | 7,846 | related: volume comparison |
| `GlobalTheory.LogPole.exists_log_pole_along_boundary` | 6,806 | related: log poles along a toroidal boundary |
| `GlobalTheory.DetLine.exists_of_snc` | 5,497 | project-specific |
| `GlobalTheory.ValMultRun.valuation_multiplicity_of_consecutive_run_alt` | 4,558 | project-specific |
| `GlobalTheory.PeakThick.peak` | 4,261 | related: peak sections |
| `GlobalTheory.NefWt.weight_line_bundle_isNef` | 3,241 | related: nefness of the weight bundle |

The table gives the historical weights of the selected dominator heads.

**T08** `GlobalTheory.T.open0_of_unitary_group_hypotheses` — disjoint 169,776 (wrapper `MiTop.famAllQ_of_allTrue_alt`, 130,748)

| Lean name | Net | Guess |
|---|---:|---|
| `GlobalTheory.Fam.colSide_alt` | 43,853 | project-specific |
| `GlobalTheory.Fam.lawsLinks_of_geo_rows_cols_alt` | 36,634 | project-specific (uses strong approximation for SU as a hypothesis) |
| `GlobalTheory.MiTop.exists_botDat_pin_of_placed_of_framed` | 15,729 | project-specific |
| `GlobalTheory.KernelHalfS.kerSide_chainS` | 11,017 | project-specific |
| `GlobalTheory.Fam.LatShape.exists_shape_integral_in_normal_frames_alt` | 5,087 | project-specific |
| `GlobalTheory.Core.HypAt.hypL_at_points_alt` | 2,619 | project-specific |
| `GlobalTheory.LabPin.frameRed_exists` | 2,567 | project-specific |

Nothing here to cite.

### 4.3 "Cite and stop" versus project-specific

Computed, by deleting sets of declarations from the graph and measuring what becomes unreachable from `allChi`:

| Set deleted | Lines lost |
|---|---:|
| the 3 Cited nodes | 6,445 |
| the 17 Related nodes | 1,240,130 |
| all 20 | 1,246,697 |
| T17–T24 together (individually they dominate 7,786) | 108,935 |
| my 28 "cite" candidates from §4.2 | 357,209 |
| the 20 plus my 28 | 1,476,687 |

Two things follow.
- If every Related comparison were closed, 1.25M lines would leave the reading burden, not 0.51M: the disjoint shares understate it, because B01 contains B02. The manuscript's Related total is correct as a deduplicated share, but it is not the answer to "what does citing buy".
- Published results mostly enter this development as named hypotheses (`GlobalTheory.Published.*`, more than twenty in the statements above), filled upstream by `*_of_literature` wrappers that the graph cuts. Their re-proofs are already outside the 9.57M. What is left inside is mostly deduction from them.

Estimate for the 6,472,125 Lean-only lines (a guess; ±0.3M on the cite side):

| Node | Disjoint | Published theory re-proved (guess) | Project-specific |
|---|---:|---:|---:|
| T02 | 1,847,425 | 150,000 (discrete series, Bessel, mass formula) | 1,697,425 |
| B02 | 625,495 | 300,000 (étale, p-adic Hodge, Harris–Taylor moduli) | 325,495 |
| T01 | 548,334 | 60,000 | 488,334 |
| T26 | 481,067 | 100,000 (heights) | 381,067 |
| W01 | 480,551 | 60,000 (patching, Hida, symmetric powers) | 420,551 |
| T04 | 455,025 | 20,000 | 435,025 |
| T05 | 303,161 | 15,000 | 288,161 |
| T06 | 280,670 | 25,000 | 255,670 |
| T03 | 274,375 | 75,000 (regularised Siegel–Weil) | 199,375 |
| T07 | 222,063 | 30,000 | 192,063 |
| T15 | 205,928 | 25,000 | 180,928 |
| T08 | 169,776 | 0 | 169,776 |
| Twelve nodes | 5,893,870 | **860,000** | **5,033,870** |
| Other 20 Lean-only nodes | 578,255 | 30,000 | 548,255 |
| All 32 | 6,472,125 | **≈ 0.9M** | **≈ 5.6M** |

The floor for the cite side is the 0.36M I can attach to named declarations. Name-matched lines in the regions (étale and purity 204k, p-adic Hodge 147k, real representation theory 211k, heights 94k) support a figure of 0.6–0.7M. I do not see how it could exceed 1M.

Sub-trees that are essentially published theory re-proved, where the manuscript can cite and stop after a statement comparison: the étale and p-adic Hodge stack under B02; `GroundTheory.Heights₂` under T26; `ReciprocityTheory.ChartRestriction.DS` under T02 and T01; `PositivityTheory.Rg.Rsw` under T03; the eight statements T17–T24 taken together.

Sub-trees that are project-specific and need written proofs: `Formalism.FourierDecayAlt` (about 322k across regions), `Formalism.L2` (489k), `Formalism.MainNotions` (404k), `GlobalTheory.CompanionTheory.Ar` (223k), `GlobalTheory.Mem` (117k), all of T04, T05, T06 and T08, and the `UpperTheory.V` counting layer under W01.

## 5. Pending hand proofs

### 5.1 P096 `GlobalTheory.Mem.Col2.SameOff.use₆` (Appendix E.1, p. 118)

Statement. Lean: for standard column data, u, i ≤ m, v, classes c, c′, γ ∈ GL_{N_i}(E) with `AdC (F u) i hi c c′ γ v_F`, and every prime q of O_E with `q.under ≠ v_F`: `localization₂ q (mulLat γ (clsCrd c′)) = localization₂ q (clsCrd c)`. Formal statement A.6 says (γL_{c′})_Q = (L_c)_Q for Q whose contraction differs from v_F. **Match.** The structural hypotheses (`I.Ok`, `Pins`, `StdF`, `StdLvC`, `CarH`) are unused in the Lean proof, which is `sameoff_gen`.

Proof. Checked against `sameoff_gen`, `AdC`, `AdStep` and `locLat_of_adStep`.
- The two branches (i = 0 or i = m; 0 < i < m with `chOf c′ = chOf c`) are the two clauses of `AdC`. Correct.
- The relation γ_f·y′ = y·η·κ with κ ∈ U and η_w = 1 for w ≠ v₀ is `AdStep` verbatim. Correct.
- κ and κ^{-1} preserve the integral span of B: `stepLevel_stab`, from the local level inclusion. Correct.
- Evaluation at Q over w ≠ v₀ gives (γL_{c′})^∧_Q = γ·y′_Q·B^∧_Q = y_Q·κ_Q·B^∧_Q = L^∧_{c,Q}. Correct.
- Descent E^n ∩ L^∧_Q = L_Q for a full finitely generated lattice, via a basis over the DVR (O_E)_Q and E ∩ Ô_Q = (O_E)_Q. Correct, and it is what `mem_localization_of_mem_localLattice` does; γ preserves fullness and finite generation (`mulLat_fin`).

**Verdict: correct.** Three small additions.
1. Say where L̂_c = y·B̂ comes from (`y_lat` of the endpoint level or of the chart).
2. Lean works in E ⊗_F F_w and the proof in E_Q. Add the sentence E ⊗_F F_w = ∏_{Q|w} E_Q.
3. State that B is finitely generated (`Lb_fin`); Lean uses it to pass between the adelic span and its local components.

### 5.2 P134 `GlobalTheory.TwV.congAt_fb_lev` (Appendix E.2, pp. 118–120)

Statement. Lean: under `UnderTie`, for i ≤ m, chart β, x, point p with `IsPtAd A a i hi β x p`, κ in the level group, and every P ∈ SB: `CongAt (seamP P) 0 (rat(fb_P)^{-1}·κ·rat(fb_P))` and the same for the inverse. Formal statement C.14 says Cong_{s(P),0}(k) and Cong_{s(P),0}(k^{-1}) with k = rat(b_P)^{-1}·κ·rat(b_P). **Match.**

Proof. Checked against `baseFrame_std_eq_compan`, `lev_stab_cong`, `globLat_compan_of_lev`, `int_conj`, `CongAt`, `NearAt`, `IsPtAd`, `IntAtA`, `qOf`.
- Local test: `IntAtA P z` (some s ∉ P with s·z integral) is equivalent to z_Q ∈ Ô_Q. The Chinese-remainder choice of s is right, and the identification of the integral tensor ring with ∏ Ô_w is right. `qOf P = Ideal.absNorm P`, so "depth d tests N(Q)^{-d}(k_Q − I)" is `CongAt`. Correct.
- C = L + aL^♯ is a full lattice, also for a = 0 (`compan_zero`, `compan_eq`). Correct.
- Duality commutes with transport by a unitary adele, so the completion at Q of the companion of the transported lattice is x_Q·C_Q. This is `companionLattice_adelicLattice_localization_eq`; Lean needs x unitary and det J a unit. Correct.
- R·V_Q = H·x_Q·C_Q from the lattice clause `IsPtAd.lat` and the transported-frame lemma with `frsF_mem` (two cases). Correct.
- The frame clause gives K = (H·x_Q·b)^{-1}·R ≡ I at depth d ≥ 1 (`NearAt`). Since N(Q) ∈ Q, K ≡ I modulo the maximal ideal, so det K is a unit and K·V_Q = V_Q. Hence b·V_Q = C_Q. Correct; this is `localisation_eq_stdAt_of_congruentOne_atPrime`.
- κ and κ^{-1} lie in the level, which stabilises L and is unitary, hence stabilises L^♯ and C. Conjugating by b gives integral matrices; subtracting I keeps integrality. Correct (`lev_stab_cong`, `int_conj`).

**Verdict: correct.** Three small additions.
1. Give the source of d ≥ 1: `(t.idx_ok μ).cst_ok.D_pos P`. The proof uses it and does not say where it is assumed.
2. "J its nonsingular Hermitian matrix": nonsingularity is derived in Lean from the pin hypothesis `crd_orth` (J is a conjugate-transpose product with the invertible `crd`). Say so, since the statement does not assume it.
3. Say that the first `UnderTie` hypothesis (the pins) is the one used.

Both candidates can go to cross-review as they are. Their weights are 227 and 175 exclusive lines.

## 6. Glossary (30 entries; 16 checked)

| Entry | Lean | Result |
|---|---|---|
| EFamC | `TopDefs.lean:15–16` | exact |
| EAtH | `ExplicitFormulaErrorOfHostConditions.lean:144–151`, six fields | exact |
| HostExW | `ThinScalesIffHostBound.lean:120–123` | exact |
| ChainTied | `TieGlobal.lean:97–114` | correct; omits the third bound `C.cHH ≤ cHH` |
| HypV | `DivinNOfHypV.lean:10–11` | exact |
| FamilyClassConnected | `DivinNOfHypV.lean:13–15` | exact |
| TopG | `ZeroFreeAllOfTopG.lean:12–14` | exact |
| Closed | `ParamsHeightRankConstant.lean:159–161` | exact (0 < ε ≤ ε₁, transported threshold, `Large K CH`) |
| LinkN | `GlobalTheoremInputs.lean:45–47` | exact; the entry would be more useful if it printed the inequality of `LinkN_at` |
| IsChiField | `ExistsPageN.lean:19–25` | exact |
| WinPair | `ExistsPageN.lean:27–37` | exact, all ten fields |
| VVle | `ExistsPageN.lean:12–17` | exact |
| VWin | `ExistsPageN.lean:49` | exact |
| LemmaK | `LemmaK.lean:13–17` | exact |
| CountI | `Counts.lean:53–58` | exact |
| CountII, CountIII, CountV | `Counts.lean:65, 67, 69` | shape exact (`CountShape`, bound (ℓNe)^C; `R1 ≤ 2^{c2}` and the complementary `CountVs`); the case predicates `CaseII`, `CaseIII`, `CaseV` were not unfolded |

No error in 16 entries. All 13 line locators I opened land on the named definition. Not checked: HypsAlt, PropsB, DefiniteSideCondition, IsRecT, H′, LiteratureRankNHypothesis, Std, StdF, StdC, StdLvC, CarT, CountIV.

Missing entries that §2 and §4 use: `Level` and `Level.Gm`, `Host` (as a field with structure), `Scale` (x, ε, b = exp(x^ε), a = x·b), `RankVal`, `CoreAtH`, `FamP` and `Win`.

## 7. Limits of this review

- AI review only. I did not build Lean or rerun any kernel check.
- §3: 17 of 52 statements were unfolded to their definitions; the others were compared at the level of hypothesis lists or not at all, as marked. "exact" for a paraphrased statement means I found every Lean hypothesis and the conclusion in the text.
- References: 8 works were confirmed by fetching the cited document, read through an automated summariser, so quotations there are second-hand. 5 are from memory or unverified, as marked. The Kollár and Scholze fetches covered the first part of the file only.
- §4: dispositions are guesses from names and statement heads. The cite/project line totals are estimates; only the "lines lost" table is computed.
- §5: "correct" means I followed each step and matched it to the Lean proof term; I did not re-derive the supporting Lean lemmas.
- Page numbers are those printed in the PDF.

## Summary

The manuscript does not claim RH, and all six R20 must-fix items are fixed. §2 is accurate formula by formula against Lean. Its analytic half is followable; its arithmetic half still omits the inequality where the Selmer sum enters (`LinkN_at`), what the lattice is, that a host is a number field, and that the exponent 1/2 comes from taking about √x columns. The 52 split statements are faithful where unfolded, the three Cited entries match Kollár and Washington, and no reference is fabricated (8 of 13 works confirmed online). One unrecorded difference: Labesse appears to assume [F:Q] ≥ 2, and W02 and W04 do not. The next split will not behave like this one: T02 (1.85M) and T01 (0.55M) are shared libraries with tens of thousands of immediate dominator children, so they need subject chapters, not sub-theorems; §4 gives 5–11 named sub-theorems with sizes for each of the twelve largest nodes. Citation can remove about 0.9M of the 6.47M Lean-only lines at best (0.36M attached to named declarations today); about 5.6M is project-specific. Both pending hand proofs, P096 and P134, match Lean and are correct as far as I can check. Sixteen glossary entries were checked with no error.
