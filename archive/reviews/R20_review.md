AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

# R20_review

AI review report produced during this project; file names are internal working names.

- Internal source file: `out/R20_review.md`
- SHA-256: `944006e694afcc9d99ca8f0174fa3d08d7fe3f3bb80eeac91f3c58fed2523bff`
- Report scope: R20 manuscript v0 — independent review

## Archived report · [English summary](../../reviews/R20_review.md)

The report below preserves its original verdict, scope and unresolved points. Superseded graph percentages have been removed from this public edition. Source line numbers in other records count from its original title.

# R20 manuscript v0 — independent review

Object reviewed: `main.pdf` (88 pp., "From the Selmer window to Dirichlet zero-free statements", manuscript v0), with `R20_report.md`, `R20_dispositions.json`, the R19 skeleton and audit, the pinned Lean tree `40e56bab`, and the dependency graph cache.
Reviewer: an AI model reading cold. Nothing here is a human or specialist check.

Method. Statements were compared with the pinned source through `git show 40e56bab:src/...`. Proof terms were read for P011–P023 and for the helpers named in Section 3. Cone sizes were recomputed from `graph_cache.bin` (1,155,391 declarations, 9,567,047 core lines reachable from `allChi`; `*_of_literature` wrappers are `lit` leaves and are not expanded). Two numbers are given per declaration: **ex** = core lines that become unreachable from `allChi` when the declaration is deleted (dominated cone), **inc** = core lines reachable from it. These are not the manuscript's "exclusive core lines", which subtract nested heads; the two agree where no head is nested (P010: 761,324 in the PDF, 761,322 here).

## 0. Verdict

- **No sentence claims RH is proved**, and the first page says so. The overclaim risk is elsewhere: status vocabulary ("Proved here", "approved", "confirmed", "complete", "expert assignments", "Independent review"), the uniform `Theorem` environment for Goal and Lean-only entries, and the "what remains" total.
- **The analytic chain P018, P019, P021, P022, P023 is written out in full and I found no error.** The Landau-type window theorem (Theorem 4.23, pp. 19–23) is a complete, correct proof and matches `Deduction.landau_window` hypothesis for hypothesis.
- **"Proved here" does not have one meaning.** Of 24 entries sampled: 14 are complete derivations under their stated hypotheses, 8 are compressed outlines that defer the substance to the unpublished Blueprint, and 2 (P015, P017) are pointers: their PDF proofs invoke Lean lemmas that are neither hypotheses of the theorem nor proved in the PDF.
- **Statement fidelity is good** where it can be checked: 27 statements compared, 27 faithful, with three small remarks.
- **The "remaining work" figure (69 propositions, 5,994,382 lines) understates what has no written derivation** by at least 0.97M lines: P010's 761,324 (labelled Goal), P015's 185,028 and P020's 21,873 (labelled Proved here) are excluded.
- **Section 3 is accurate** against the proof terms, with two omissions that matter (§5.1).
- **A number theorist could not follow the architecture from this manuscript alone.** The mechanism linking Selmer-kernel bounds to prime sums is never stated in mathematical terms, about 40 project predicates are used undefined, there is no bibliography, and the formalization's author is never named.

## 1. Overclaim audit

No sentence asserts that RH or GRH holds. The items below either let a cold reader infer more verification than exists, or present a formal statement as an established theorem.

| # | Page | Quote | Problem | Replacement |
|---|---|---|---|---|
| 1 | 1 | "Independent review / SHA-256" and "the approved and editorial registers" | "Independent" and "approved" read as third-party human review. Both are AI-produced files. | "AI audit of the skeleton (R19) / SHA-256"; "AI-maintained status register and editorial register". Add: "No file named here records a human check." |
| 2 | 4 | "The two zeta declarations locate every nontrivial zero on the line Re s = 1/2." | Indicative mood about the conclusion. | "The two zeta declarations assert that every nontrivial zero lies on Re s = 1/2." Same change for "The first excludes zeros…", "The next locates…". |
| 3 | 4 | "A finite-window estimate supplies primitive nonvanishing" | Reads as an accomplished step. | "In the formal development, primitive nonvanishing is deduced from a finite-window estimate". |
| 4 | 4 | "In the archived MIT audit dated 23 November 2026, 23:45 UTC, module replay passed. … These are published checks." | Third-party verification asserted with no citation a reader can open; this is the only place where the PDF says something external was checked, and the report states that no rebuild was done in this round. | Give the URL or drop the paragraph to one sentence: "A third-party kernel replay is reported at [reference]; we did not rerun it and rely on it only for the identity of the five statements." |
| 5 | 4 | "The approved register lists 14 complete original inputs out of 20, and 30 complete expert assignments out of 55" | "approved", "complete", "expert" imply specialist sign-off. The next sentence ("zero human sign-offs") contradicts the impression instead of preventing it. | "The project's AI-maintained register marks 14 of 20 inputs and 30 of 55 review tasks as having a written derivation that passed AI review. No human has signed off on any of them." |
| 6 | 5 | "Proved here points to a deduction reproduced or summarized from an existing written proof." | The label says "proved"; the definition says "summarized". For P015 and P017 the entry is neither. | Rename to "Written derivation (AI-reviewed)", split off "Outline (Blueprint)", and define: "a derivation under the stated hypotheses, written and reviewed by AI, not checked by a human". |
| 7 | 13–15 | "Theorem 4.1 (The Riemann hypothesis in Mathlib's formulation). For every s ∈ C, if ζ(s) = 0, … then Re s = 1/2." and Theorems 4.2–4.10 | A `Theorem` environment stating RH. The status line "Goal" is in small type below. | Use "Formal statement 4.1 (Goal, not proved here)". Apply to all 10 Goal and 57 Lean-only entries. |
| 8 | 16 | "Thus the exported application discharges all three fields in Lean." and "the proved declaration galoisLocalGlobalStrong_recParameter" | "discharges", "proved" without qualifier. | "In the Lean source the three fields are filled by Lean declarations (761k exclusive lines for the first and third); no written proof is given here." |
| 9 | 27 | "This proves the reduction given the intermediate bounds in blueprint Chapter S" | The proof of P020 depends on five Lean lemmas outside the hypotheses (`thmBab_of_lemmaK`, `ferreroWashington`, `thmBcFree_of`, `ML.iv`, `countZ X.propZ`). | "This outlines the reduction. The five intermediate results listed are not hypotheses of the theorem and are not proved here." |
| 10 | 47 | "The approval recorded in r14:z44-approved applies to Z4.4 under its stated assumptions." | "approval" by whom is not said. | "An AI review round (r14) accepted the Z4.4 derivation under its stated assumptions." |
| 11 | 32–60 | "Register: Z4.4 (confirmed)" (11 times), "Register: Z… (complete)" (26 times) | Same vocabulary problem in every status line. | "Register: Z4.4 (AI-reviewed)". |
| 12 | 85 | "Together these two disjoint lists contain 69 propositions and own 5,994,382 exclusive core lines. The goals themselves are excluded from both lists." | Presented under "What remains". P010 (Goal) owns 761,324 lines of Galois-representation construction; P015 and P020 (Proved here) own 206,901 lines used through unproved lemmas. | Add a third row "Heads whose own cone is not covered by the written text" with P010, P015, P020, P034, P027, P041–P044, and state the complement: complete written derivations cover on the order of 3–4 thousand of 9.57M core lines. |
| 13 | 23 | "the hypothesis c_ρ > 0 at real poles cannot be dropped" | True, but asserted without support. | Add the example g(u) = −e^{βu}: Φ(s) = −1/(s−β), g ≤ 0 on every window, pole at β > θ. |

Items 6, 7 and 12 are the ones I would not let through.

## 2. "Proved here" audit (24 of 48)

Classes: **F** = complete derivation in the PDF under the stated hypotheses; **O** = outline whose decisive steps are deferred to the Blueprint or to unnamed lemmas; **P** = pointer.

| Node | Page | Class | Proof correct? | Statement vs Lean |
|---|---|---|---|---|
| P014 | 16 | F | Yes. Uses the change-of-level product written on p. 14. | exact |
| P015 | 16–17 | **P** | The four lines restate the proof term. `shape_closed_link_n_of_green` (ex 146,214), `supplyChi` (ex 31,622) and `forall_goal_of_shape_of_hyps` are invoked, not proved, and are not hypotheses. The entry owns 185,028 exclusive lines. | exact (B, V, F; λ = 3/2) |
| P016 | 17 | F | Yes. Threshold x₁+1 and C = 4 match `eFamC_of_cls`, `hypV_of_cls`. | exact |
| P017 | 17–18 | **P** | The proof says "The one-scale inequality core_gm applies." `core_gm` (ex 3,303), with `Deduction.ch_core` (ex 1,886) and `ch_top`, is the content of the theorem: it is where tied lattice data become a bound on G_L. It is not proved in the PDF. | exact (exponent 1/2 + (e_D+e_L+7)ε, quantifier order) |
| P018 | 25 | F | Yes. δ = λ−1, C = 1. | exact (`FormB`) |
| P019 | 26 | F | Yes. Δ = min(Re s − 1/2, 1/2), θ = 1/2 + Δ/2, as in `level_of_tiedWin`. | exact |
| P020 | 26–27 | O | The size bookkeeping at the end is plausible. The five intermediate inputs of item 9 above are assumed. | exact (`LiteratureRankNHypothesis`, ∃C_K, Counts I, II, III, V; exponent 401) |
| P021 | 27–29 | F | Yes; Steps 1–5 rechecked line by line, including the key identity and u·log(1+H/u) ≤ log(1+X)(U+b). | exact (`ErrX5at`, `UBar5`, `MLo5`, `Count5` compared term by term) |
| P022 | 19–23 | F | Yes, in full; see §2.1. | exact |
| P023 | 24–25 | F | Yes; see §2.1. | exact |
| P027 | 32 | O | Not checkable from the PDF. The Hilbert-series step and "nonnegativity of the remaining Euler characteristic" are stated, not derived. 8,903 exclusive lines. | not unfolded (`LemmaM`) |
| P028 | 33 | F | Yes. Matches the Lean proof step for step (saturation, injectivity of ψ, length of Hom(k, O/c) ≤ 1, cardinality comparison). | consistent with the proof term |
| P032 | 35–36 | O | Consistent with `SClass`; the prism and Steinitz steps are named, not shown. | exact (m = 2E+1 = 2e+3 < ℓ^c, product over j ≠ E) |
| P033 | 36 | F− | Follows the Lean proof (homomorphism, vanishing on transvections, reduction to diagonal). Adequate as a proof given the six hypotheses. | exact (degree 2e+3, value x^{e+1}·v(det g)) |
| P040 | 40–41 | O+ | Standard finite-to-compact limit argument; correct in outline. | exact |
| P048 | 47 | O | Summary of four comparisons P054–P057; final sum y = Σ b_c/h_c and the ultrametric step are fine. | not unfolded |
| P049 | 48 | F | Yes (covolume 2^{−f}√Δ, Gram determinant, index by Smith form). | exact (`HtGram`) |
| P051 | 49 | F | Yes, given P050 and P052. | exact (`DualMu`: μ = lcv/D) |
| P052 | 49 | F | Yes. C(A^∨)C(A) = 2^{−nD}Δ^D and the height normalisation 2^{fD}Δ^{−D/2} give product 1. | exact |
| P053 | 50 | F | Yes (three-line deduction from Theorem 7.2). | consistent |
| P059 | 52–53 | F | Yes (bookkeeping). | not unfolded (`Std`) |
| P068 | 59 | F | Yes (instantiation of two hypotheses with the same witnesses). | consistent |
| P069 | 59 | O | Assembly of Theorems 8.1–8.8, two of which (P084, P086) are "Adapted, proof in Lean only". | not unfolded |
| P082 | 65 | O | Construction of the idempotent and the unitary scalar is sketched; the lift to the adelic relation is asserted. | not unfolded |

Totals in the sample: F 14, O 8, P 2. The two pointers are exactly the nodes the R19 audit singled out as carrying the new mathematics.

### 2.1 Theorem 4.23 (Landau-type window theorem), checked in full

Statement. `PoleData` has seven fields (measurability; |g(u)| ≤ C₀e^{2u} for u ≥ 0; Laplace identity for Re s > 2; Z ⊂ {Re > 0}; differentiability on {Re > 0} \ Z; no accumulation in {Re > 0}; simple poles with c ≠ 0 and c real positive at real ρ). (P1)–(P4) reproduce all seven. `WindowHypU` is Definition 4.22 verbatim. `landau_window` takes 0 < θ, θ < 1, 0 < δ and concludes ∀ρ ∈ Z, Re ρ ≤ θ. Match.

Proof.
- Lemma 4.24: (1) t^k/k! ≤ e^t; (2) Gamma integral; (3) the pointwise bound e^{−su} ≤ e^{lU}e^{−(s+l)u} + e^{−lV}e^{−(s−l)u} off [U, V]. Correct.
- Lemma 4.25: with l = 2 + 6/δ, M = l(1+δ), σ = M(2+l) I recomputed (1+δ/2)(l−2) = l+1, σ−2−l = (M−1)(2+l), (1+δ/2)(2+l) = M−1, hence (1+δ/2)σ = M(M−1); both tail exponents are ≤ 0 and ≤ 1 as claimed. Correct, C = e/(σ−2−l) + 1/(σ−2+l).
- Proposition 4.26: |g|+g ≤ 2R on the window; off the window (P1) and Lemma 4.25; the step 1/σ^k ≤ 1/(σ−θ)^k uses θ > 0. Correct.
- Lemma 4.27 (dichotomy) and Lemma 4.28 (generic γ on Re s = σ): both correct; the equidistance equation has at most one solution in γ, and none when Im a = Im b.
- Case (A): |c|/d^{k+1} ≤ |c_k(z)| + M/r′^k, Re c_k(σ) ≥ −M′/r′^k on the pole-free disc B(σ, D), then (r′/d)^{k/2} ≤ (C₁+M+M′)d/|c| for arbitrarily large k. Correct; C₁, M, M′ do not depend on k or η.
- Case (B): real pole, positive residue, γ = 0. Correct.

Remarks, none affecting validity.
1. The sentence inside the statement ("In the pole-data hypotheses the growth bound holds for u ≥ 0, and the Laplace identity is required for Re s > 2") repeats Definition 4.21; delete.
2. θ < 1 is used only for σ − θ > 0, which already follows from θ < σ. Say so, or the reader will look for where 1 enters.
3. Proposition 4.32 defines Φ by a formula that is 0/0 at s = 1. State that Φ is the holomorphic extension there; (P3) needs Φ differentiable at 1.
4. Lemma 4.31 and Proposition 4.32: transform, residues −m/(ρ(ρ−1)), positivity for 0 < β < 1 all recomputed. Correct. The identity −1/(s−1)² = −(1/(s(s−1)))(1/(s−1) + 1) holds.
5. Theorem 4.33: the choice R(u) = |C|e^{θu} and |C|δU ≤ e^{ηU} is right.

## 3. Statement fidelity (27 statements)

| Entry | Lean object compared | Result |
|---|---|---|
| Thm 4.1, 4.2 (P001, P002) | `RiemannHypothesis`, `RiemannZetaZerosOnLine` | exact |
| Thm 4.3 (P003) | `DirichletLNonvanishingRightOfHalf` (χ ≠ 1 ∨ s ≠ 1) | exact |
| Thm 4.4, 4.5 (P004, P005) | `DirichletLZerosOnLine`, `PrimitiveDirichletLZerosOnLine` | exact |
| Thm 4.11 (P011) | `everyCharacter_of_row`; proof term ⟨h, recTExists, h⟩, `vwin_of_row h` | exact, and the text on p. 16 describes the term correctly |
| Window predicate V (p. 15) | `VWin`, `VWinAt`, `VAt`, `VVle`, `WinPair`, `IsChiField`, `PageN` | exact: ε < 1/52; x^{2+8ε} ≤ 2^{e(x)} ≤ 2x^{2+8ε}; q ≡ 3 (8), d ≡ 7 (16); both log ranges; q ∣ d+1; odd p ≤ B^{ε/5}; t = ⌊x^{401}⌋; bound √exp(x^ε). Remark: the PDF prints "exp(x^ε/2)"; write exp(x^ε/2) as exp(½x^ε) to avoid reading it as exp((x/2)^ε). Remark: "twist −k" is a convention not visible in `shaLen (ld p) (e : ℤ)`; say where the sign comes from. |
| Thm 4.12 (P012) | `OpenLiteratureStatements` (3 fields), `VWin` | exact |
| Thm 4.13 (P013) | `vwin_of_row` | exact |
| Thm 4.14–4.16 (P014–P016) | `TopPlug.lean`, `ZeroFreeAllOfTopG.lean` | exact |
| Thm 4.17 (P017) | `ChebyshevInequalityOnWindows` | exact |
| Def 4.18–4.20 | `Gchi`, `G`, `Level`, `wt`, `Level.Gm`, `cyc`, `HasWindows` | exact, including weight 1/(3o+1) and the remark on principal characters of modulus > 1 |
| Thm 4.23 (P022), 4.33 (P023), 4.34 (P018), 4.35 (P019) | see §2 | exact |
| Thm 4.36 (P020) | `of_four_alt`, `LemmaK`, `kBound`, `CountI`, `CountShape` | exact: log|H²| ≤ exp((2e·n)^{C_K}·log(2D)) |
| Thm 4.40 (P021) | `PointwiseBoundVariant`, `ErrX5at` | exact |
| Thm 5.8 (P031) | `exists_descends` | exact |
| Thm 5.9, 5.10 (P032, P033) | `SClass`, `SThetaOf` | exact |
| Thm 5.12 (P035) | `TorsStab` (2m+4 ≤ n ≤ n′) | exact |
| Thm 5.13 (P036) | `SCount`, `Few`, `gens` | exact: g = 2[L:Q] + ⌊log₂ h_L⌋ + 2, exponent (b+v)g + c + v |
| Thm 5.14 (P037) | `SSha`, `TopRoot` | exact |
| Thm 5.15 (P038) | `KH.bound m A s b = b^A·s^{mAs^m}`, s = 3^{dN}, b = m+2 | exact |
| Thm 5.17 (P040) | `vFormula_of_classicalTheorems` | exact |
| Thm 5.26, 5.28, 5.29 (P049, P051, P052) | `HtGram`, `DualMu`, `ht_dual` | exact |
| Thm 9.8 (P098) | `host_primes_over_level_place` | faithful paraphrase; the seven structural hypotheses are compressed to "standard column data" |

No mismatch found. Entries from depth 2 downward (P054–P140) state their hypotheses through project predicates (`Std`, `CarT`, `StdC`, "tied", "pinned") that the PDF does not define, so they cannot be compared with Lean from the PDF alone; I did not count those.

## 4. "Adapted" (24) and "Cited" (1): 14 sampled

Existence of the base reference and accuracy of the stated difference.

| Node | Base reference in the PDF | Real? | Difference stated accurately? |
|---|---|---|---|
| P098 (Cited) | Stacks Project, Lemma 15.112.10(1), tag 0BRK | Yes, confirmed online: Galois group acts transitively on primes of the integral closure over a given prime ([tag 0BRK](https://stacks.math.columbia.edu/tag/0BRK)). | Yes. The citation covers the disjunction once P_v is known to lie over v_F; the PDF says where that comes from. Correctly "Cited". |
| P026, P063, P065, P066, P067 | Kato, Astérisque 295: (8.1.3), Prop. 8.12, Thm 9.7, Thm 12.5–12.6, §4.2, Thm 6.6 | Yes (numbering as I know it; not re-fetched). | Yes, and candidly: norm relation is published, the integral model and local non-coboundary are "Lean only". P026 has 4 exclusive lines because all weight sits in P058–P066; say so. |
| P029 | BLGGT, Thm 2.1.1 | Yes. "End of §5.1" not verified. | Yes. |
| P030 | Arthur–Clozel, Ch. III, Thm 4.2 | Yes. | Yes. |
| P031 | Sharifi, *Group and Galois Cohomology*, §2.2 | §2.2 exists ("Cohomology of profinite groups"); the page was too long to confirm Prop. 2.2.18 ([notes](https://www.math.ucla.edu/~sharifi/notes/groupcoh-ch02.html)). | Yes. The written proof on p. 35 is a real argument. |
| P034 | Borel, Ann. Sci. ENS 1974, Thm 7.5, 11.1, Prop. 12.2 | Yes. | Yes: the PDF notes Borel has no k+1 < r₂ restriction and does not cover i = 1. The "proof" is a three-paragraph outline for 23,135 exclusive lines. |
| P035 | van der Kallen, Invent. Math. 60, Thm 4.11 | Yes. | Yes. Lean uses n ≥ 2m+4, weaker than the n ≥ 2m+1 the citation gives; the PDF says this. |
| P036 | Milne CFT II Cor. 1.23; ANT Thm 4.4, 5.1 | Notes exist; item numbers not re-fetched. | Yes. |
| P038, P039 | Soulé, Doc. Math. Extra Vol. Kato (2003) 761–788, Thm 1 | Yes ([Documenta listing](https://www.maths.tcd.ie/EMIS/journals/DMJDMV/vol-kato/soule.dm.html)); the clause "removes p ≤ 1 + max(r, N)" not verified. | Plausible. I rechecked the arithmetic of P039 (C = 24, 7,681,212 < 2²⁴): correct. |
| P041–P044 | Bellaïche–Chenevier, Thm 1.4.4(i), 1.5.5; Ribet 1976 Prop. 2.1; Stacks 10.52.13 (tag 02M1) | Yes; tag 02M1 confirmed online as the flat local length formula ([tag 02M1](https://stacks.math.columbia.edu/tag/02M1)). | Yes. |
| P084, P086 | Greenberg–Voight, Prop. 5.4, Thm 5.8, Cor. 5.10; Dummigan–Schönnenbeck, Prop. 3.3–3.5 | Yes, all six confirmed online ([Greenberg–Voight](https://jvoight.github.io/articles/orthohecke-240123.pdf), [Dummigan–Schönnenbeck](https://eprints.whiterose.ac.uk/145797/1/Hecke8.pdf)). | Yes. Note Greenberg–Voight give only a proof sketch of Thm 5.8. |
| P128 | Dummigan–Schönnenbeck §2.2 (8) | Formula (8) exists but is the factorisation K_L = ∏_p K_{L,p}, not a "lattice action". | Wording off: cite it as the adelic stabiliser, or drop the base reference; this entry is in substance Lean only. |

Also confirmed in passing for §3.3: Stacks Prop. 39.9.11(7), tag 03RP ([tag 03RP](https://stacks.math.columbia.edu/tag/03RP)).

Finding. No fabricated reference in the sample. Three locators are unverified (Sharifi 2.2.18, Soulé's small-prime clause, HLTT "Corollary 7.14" for P061). One description is inaccurate (P128). The label "Adapted" covers two different situations and should be split: 12 entries carry a written comparison, 12 say "proof in Lean only"; the second group is Lean only with a related reference.

## 5. Section 3 and the split of P012 and P013

### 5.1 Accuracy of Section 3 against the proof terms

| § | Claim | Check |
|---|---|---|
| 3.1 | P010 = P011 applied to `galoisLocalGlobalStrong_recParameter`; route through `galoisRepresentations_of_thetaLift` | Correct. ex 761,322 and 720,478. Under it `Geo.geoOne_holds` (ex 625,495) is the bulk and is not mentioned. |
| 3.1 | P011 uses the row twice and `recTExists` | Correct (`⟨h, recTExists, h⟩`). |
| 3.2 | `every_character_of_theta_integrals_local_matching` has seven inputs | Correct (P, F, hA, hM, hX, hL, hV). |
| 3.2 | `nonempty_hyps_definite_side_of_closed_bound` inputs; `hypotheses_nonempty_of_unramified_exponents_alt` inside it | Correct. |
| 3.2 | `topCovolSlim2_use_alt_alt` takes fifteen inputs | Correct (counted). |
| 3.3 | Three constructors with 60, 53, 28 assignments | Correct (lines 667–726, 728–780, 782–809). |
| 3.4 | `vwin_of_row` → `automorphic_window_of_inputs` with `OpenImageCondition.mk h`, `baseChangeN`, `h`; `baseChangeN` uses `candFin` | Correct. |
| 3.4 | `vwin_of_hypotheses_H_E_alt` obtains ends, K-bound and counts, then P020 | Correct. |
| 3.5 | `supplyChi : VWinAt ψ 401 → HostExW (3/2) (GChi ψ).req`; route P017 → `windowInequality_of_artinInputs` → `core_gm` → `ch_top` → P021 | Correct. |

Omissions and defects.
1. **The literature record is not an assumption, and the PDF never says what fills it.** In the pinned file only four lines use a field of `O`. Every other `*_of_literature` wrapper ignores `O` and returns a named Lean declaration (for example `casselman_wallach_of_literature := PositivityTheory.CWB.casselmanWallach`). The graph treats these wrappers as `lit` leaves, so their proofs lie outside the 9.57M core lines. A reader of §3.3 will think 141 published theorems are hypotheses. State: (a) they are closed terms in Lean, (b) their proofs are outside the weights quoted, (c) how many were compared with the literature (6 fields, 2 direct).
2. **Three weight systems are mixed.** §3.2 quotes 3,690,545 / 2,957,291 / 1,693,945 / 567,883 from "the earlier backward map". On the current graph the dominated cones are 4,409,173 / 3,679,693 / 1,232,134 / 836,896. Neither set is wrong, but a reader cannot reconcile them with the 5,666,153 of P012. Use one metric in §3 and relegate the other to a footnote.
3. §3.4 skips the step between `LiteratureRankNHypothesis` and `HypothesesH'`: `published_hypotheses_from_patching_alt` (ex 46,525) and `descWeak` (inc 350,186). That is where patching and descent to the unitary group enter.
4. §3.5 describes `TopG` and `ChainTied` by listing their fields. It does not say what "connectedness of a family class" is or why it yields a tied chain. This is the hinge of the argument.

### 5.2 Proposed sub-nodes

Label: **cite** = statement looks like a published theorem and should become a Cited or Adapted entry with a locator; **proj** = project-specific. My labels are from names and types, not from a literature search.

**P012** (PDF: 5,666,153 exclusive; dominated cone 6,497,541)

| # | Lean name | ex | inc | Label |
|---|---|---:|---:|---|
| 1 | `UpperTheory.Lit.every_character_of_theta_integrals_local_matching` | 4,409,173 | 5,846,517 | proj (N003) |
| 2 | `UpperTheory.Lit.nonempty_hyps_definite_side_of_closed_bound` | 3,679,693 | 5,646,413 | proj |
| 3 | `GlobalTheory.Fc.S0.StageU.hypotheses_nonempty_of_unramified_exponents_alt` | 1,232,134 | 5,189,760 | proj |
| 4 | `GlobalTheory.Fc.AllAtMemberStage0.allRows_of_open0_alt` | 455,025 | 2,638,235 | proj |
| 5 | `GlobalTheory.Fc.S0.ontoX_and_lamLow_of_unitaryGroupHypotheses'` | 303,161 | 1,786,849 | proj |
| 6 | `GlobalTheory.T.large_unramified_exponent_bundles_exist_alt` | 280,672 | 2,637,180 | proj |
| 7 | `UpperTheory.GalC.final_alt_alt` (`NLink.Final.mainTheorem`) | 222,062 | 1,261,229 | proj |
| 8 | `GlobalTheory.T.open0_of_unitary_group_hypotheses` | 169,776 | 2,025,830 | proj |
| 9 | `UpperTheory.Lit.functionalsSeparate_of_howeUnram_of_siegelWeil` | 64,874 | 514,201 | adapted (unramified Howe duality, Siegel–Weil) |
| 10 | `GlobalTheory.BigTop.Fun.Close.fourier_coefficient_fit_of_join_alt` | 62,323 | 909,674 | proj |
| 11 | `PositivityTheory.ThKR.theoremK_head2` (gives `ThetaIntegralsAgree ∧ LocalMatching`) | 97,419 | 292,506 | adapted (doubling, Siegel–Weil) |
| 12 | `PositivityTheory.SiegelWeilFormula.Fin.siegelWeilStd` | 20,986 | 242,886 | cite (Siegel–Weil for unitary groups) |
| 13 | `SelfIntersectionVolumeEstimates.topCovolSlim2_use_alt_alt` | 836,896 | 2,171,515 | proj (N478) |
| 14 | `PositivityTheory.HtPt.Ah.deep_slim_use` (via `Ar.Plug.deepStR_of_use`, ex 481,067) | 486,193 | 1,311,853 | proj |
| 15 | `SelfIntersectionVolumeEstimates.topCovolG_alt_alt` | 205,928 | 1,498,191 | proj |
| 16 | `ChowFormHeightComparison₂.chow_form_height_comparison` | 30,511 | 62,496 | cite or adapted (heights of Chow forms) |
| 17 | `PositivityTheory.Pf1.HilbertSamuelMoriwaki.moriwakiBig_outright`, `hsUse_outright` | 13, 9 | 366,806 | cite (arithmetic Hilbert–Samuel, arithmetic bigness) |
| 18 | `resolution_char_zero_of_literature`, `principalisation_char_zero_of_literature`, `poincare_lelong_inv_of_literature`, `zarhin_statement`, `nef_rr_of_literature`, `fargues_exact_of_literature` | 35; 1,572; 18; 3,757; 769; 1,613 | 121,633; 100,762; 84,844; 82,432; 59,206; 9,481 | cite, six separate entries; these are `core`, so their proofs are inside the cone |
| 19 | `UpperTheory.N.boundAtTwoThree_linked_of_recT` | 9 | 213,953 | proj |
| 20 | The 141 record fields (`published_results_eigen` 60, `_first` 53, `_arithmetic` 28) | 0 | leaves | cite, one table row per field with a locator; today 6 have one |

Rows 1–3 are nested and rows 4–8 sit under row 3: this is the spine a reader needs, in that order.

**P013** (PDF: 285,082 exclusive; dominated cone 886,201)

| # | Lean name | ex | inc | Label |
|---|---|---:|---:|---|
| 1 | `UpperTheory.One.Join.automorphic_window_of_inputs` | 884,497 | 1,723,135 | proj wrapper (N624) |
| 2 | `UpperTheory.BaseChangeIdentities.baseChangeN` (with `HeckeLevelFrameExistence.candFin`, ex 418) | 1,699 | 444,452 | cite or adapted (isobaric base change from unitary groups) |
| 3 | `UpperTheory.V.HV.DescentVanishingReductions.published_hypotheses_from_patching_alt` | 46,525 | 397,974 | adapted (patching) |
| 4 | `UpperTheory.V.Z.Tf.SR.descWeak` | 9 | 350,186 | cite or adapted (descent from GL_n over a CM field) |
| 5 | `UpperTheory.V.ZK.lemmaK_litN_alt` | 38,725 | 105,973 | adapted; root of the Z2.K inputs P031–P040 |
| 6 | `UpperTheory.V.HV.DescentVanishingReductions.sp4In0_alt` | 111,950 | 845,977 | proj |
| 7 | `UpperTheory.V.Z.Kato.WeilSphericalRecords.katoTwoW_of_printsH` | 145,398 | 421,793 | adapted (Kato); parent of P026 |
| 8 | `UpperTheory.V.Z.J.count_i_of_printed_bound_k_kato_automorphy` | 12,061 | 1,241,070 | proj (Count I) |
| 9 | `…DescentVanishingReductions.countII_and_countIII_of_printsH_of_sp4In` | 15,582 | 1,055,606 | proj (Counts II, III) |
| 10 | `UpperTheory.V.Z.J.count_v_of_printed_bound_k_reduced_unitary_lift` | 15,145 | 1,223,685 | proj (Count V) |
| 11 | `UpperTheory.V.FW.ferreroWashington` | 4,838 | 54,293 | cite (Ferrero–Washington) |
| 12 | `UpperTheory.V.Win.thmBab_of_lemmaK`, `UpperTheory.V.HV.vwin_of_counts`, `UpperTheory.V.Odd.thmBcFree_of`, `UpperTheory.V.X.propZ` | 4,107; 4,677; 2,871; 2,058 | 50,537; 15,583; 47,736; 55,134 | proj; these are the lemmas P020's proof assumes |

`ends0_alt` (P024, inc 1,154,962) and `of_four_alt` (P020) are already nodes and belong in this list as children.

The same treatment is needed for two heads the task did not name:
- **P010**: `Gal.Int.galoisRepresentations_of_thetaLift` (720,478 / 1,844,742), `Gal.Int.Geo.geoOne_holds` (625,495 / 1,026,091), `galoisLocalGlobalStrong_of_geometry_lift` (93,354 / 890,837), `Zero.LLC.recTExists` (4,837 / 29,083). The statement is a published theorem; the Lean route (theta lift, weight-one geometric realization) is not the published one. Enter the statement as Cited and the route as project-specific.
- **P015**: `Top.shape_closed_link_n_of_green` (146,214 / 616,449), `GlobalTheory.Top.closed_family_admissible_twist_link_alt` (21,017 / 65,731), `Top.supplyChi` (31,622 / 66,017). **P017**: `Comparison₂.core_gm` (3,303 / 4,492), `Deduction.ch_core` (1,886 / 2,047), `Deduction.ch_top` (675 / 876).

## 6. Readability: can a number theorist follow the architecture?

Not from this manuscript alone. The upper analytic part (§4.3–4.5) can be read and checked. Everything that connects it to arithmetic cannot.

Top 10 improvements, in order of effect.

1. **Write the mechanism in two pages before any entry.** Why would bounds on Σ_ℓ log ℓ · Σ_k h_ℓ(E, k) over fields E of type (ψ, j, q, d) give G_L(x) ≤ x^{1/2+ε} on [Y, Y^{3/2}]? The PDF names hosts, tied chains and "connectedness" but never says what object is being bounded by what. One paragraph each for: host and frame; the lattice chain and its slopes; what P021's ASK and Main are in the application; what TopG asserts.
2. **Define the project predicates mathematically or do not use them in statements.** Undefined in the PDF: `EFamC`, `EAtH`, `ChainTied`, `HostExW` (partly), `HypV`, `FamilyClassConnected`, `HypsAlt`, `LinkN`, `Closed`, `DefiniteSideCondition`, `PropsB`, `IsRecT`, `LiteratureRankNHypothesis`, `H′`, `Std`, `CarT`, `StdC`, "tied", "pinned", "served". Add a glossary with one mathematical sentence and one Lean locator each.
3. **Split the four heavy heads as in §5.2** and give each new node a statement paragraph. The existing contents list locates only the named heads.
4. **Fix the status system** (§1 items 6, 7, 11): five honest labels (Goal / Complete written derivation / Outline, details in Blueprint / Related reference, proof in Lean only / Lean only), `Formal statement` instead of `Theorem` for anything not proved in the text, and "AI-reviewed" wherever "approved", "confirmed" or "complete" now stands.
5. **Make the document self-contained or cite properly.** 134 pointers to an unpublished "Blueprint". No bibliography; references are inline with URLs. The formalization's author and source are never named. Add a numbered reference list, cite the Blueprint as one item with a stable identifier, and say in the first paragraph whose Lean development this is and where it was obtained.
6. **One weight metric, explained once.** Say that `lit` wrappers are cut, that "exclusive" subtracts nested heads, and give for each heavy head both the nested-exclusive and the dominated figure. Remove the backward-map numbers from §3.2 and §13.2 or put them in one comparison table.
7. **Redo "What remains" (§13).** List every head whose cone is not covered by a complete written derivation, whatever its label, and state the covered fraction. Add P010, P015, P017, P020, P027, P034, P041–P044.
8. **Move depths 4–7 (§§9–12, about 16 pages, 50 Lean-only entries) to an appendix table.** They are chart bookkeeping with undefined terms and hide the architecture.
9. **Notation.** L is a level, a number field, an L-function, a length and a constant; G is a function, a requirement and a group; χ is a Dirichlet character and the cyclotomic character; e is a function, a twist and a ramification index. Two numbering systems (Theorem m.n and Pnnn) run in parallel. The cross-reference on p. 4 ("See Theorems 4.13, 4.16–4.34 and 4.33") is garbled.
10. **§4.4 polish.** State Theorem 4.23 first in Mellin form for G_F, then abstractly; apply remarks 1–3 of §2.1; add the one-line counterexample for positivity; say explicitly that this section, with P018, P019 and P021, is the part of the manuscript that is complete.

## 7. Limits of this review

- AI review only. I did not build Lean and did not rerun any kernel check.
- "Correct" for a class-F proof means I followed every step. For class O it means I found no contradiction with the Lean statement, not that the outline is a proof.
- Literature: six locators were confirmed online; the rest are from memory of the standard references or marked unverified. Labels "cite" in §5.2 are proposals to be confirmed by a search and a specialist.
- Deep-layer statements (P054–P140) were not unfolded against Lean.
- Page numbers are those printed in the PDF.

## Summary

The manuscript does not claim RH. Its analytic core (Landau window theorem, level criterion, window combination, weighted-slope bound) is fully written, correct as far as I can check, and faithful to Lean. Its status vocabulary and its "what remains" total overstate coverage: P015 and P017 are labelled "Proved here" but their proofs point to unproved lemmas, P010's 761k lines are hidden under "Goal", and words such as "approved", "confirmed" and "expert" describe AI bookkeeping. All 27 statements compared are faithful and no sampled reference is fabricated. Section 3 is accurate but must say that the literature record is filled by Lean terms outside the counted cone. P012 and P013 should be split into about 20 and 12 sub-nodes (lists with cone sizes in §5.2), and P010 and P015 likewise. For a number theorist the architecture remains opaque until the Selmer-to-prime-sum mechanism and some forty project predicates are stated in mathematical language.
