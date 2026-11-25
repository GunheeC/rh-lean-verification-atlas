AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

# R6_review

AI review report produced during this project; file names are internal working names.

- Internal source file: `out/R6_review.md`
- SHA-256: `120684e5a02afcba6c4942f8a82606125930c6a833a3705c226f395dc4273841`
- Report scope: Round-6 independent review — Z1.5.02, Z4.2.08, re-check of Z1.5.07 and Z2.K4, status audit

## Archived report · [English summary](../../reviews/R6_review.md)

The report below preserves its original verdict, scope and unresolved points. Historical review-machine home prefixes are displayed as `${REVIEW_HOME}`; the source checksum above identifies the original report. Source line numbers in other records count from its original title.

# Round-6 independent review — Z1.5.02, Z4.2.08, re-check of Z1.5.07 and Z2.K4, status audit

Scope. This review checks whether the hand proofs in the blueprint faithfully and rigorously cover the Lean statements they label. It says nothing about whether RH is proved; every unit below is an internal implication with stated hypotheses.

Sources read: `${REVIEW_HOME}/work/prev6/ch_P.tex`, `ch_Z.tex`, `P_notes.md`; the cleaned Lean copy under `${REVIEW_HOME}/src/rh/src`; `graphq.py` (`callers`, `deps`, `path`, `find`); `${REVIEW_HOME}/work/prev5/R5_review_A.md`.

Line-number convention. Lean ranges are quoted in the original numbering used by the blueprint and by `graphq.py`. The cleaned copy carries a 4–5 line header shift (for example `TCardK.lean` theorem at 22–40 in the cleaned copy, 18–36 in the original). Blueprint references are `ch_P.tex:LINE`.

## Verdict table

| Unit | Lean root | Verdict |
|---|---|---|
| Z1.5.02 | `UpperTheory.V.Af.card_k_of_printed_results`, `TCardK.lean:18–36` | **COMPLETE WITH GAPS** — statement faithful, argument correct; one unproved and unlabelled standard input (class-number finiteness for GL_n over the finite adeles), hypothesis label names no real discharge site, one stale sentence |
| Z4.2.08 | `GlobalTheory.TwV.scal_at_site`, `KernelSiteSeriesScalarPowIntegral.lean:14–16` | **COMPLETE WITH GAPS** — statement faithful, argument follows the Lean decomposition and is correct where checked; no hypothesis label for the dictionary, dependence on site-law fields and on one clause of the partial unit Z4.2.04 not stated as such, several one-sentence steps, one wrong file name |
| Z1.5.07 (R5 gap) | — | **Fixed** (p-adic Hodge step now reproduced, and it matches the Lean proof) |
| Z2.K4 (R5 gaps) | — | **Mostly fixed** — 7 of 9 items fixed, 2 fixed in substance but not in the requested form (see table in that section) |
| Status audit | — | `ch_Z.tex` and the v8 section of `P_notes.md` agree on all 54 units (26 / 19 / 9). All disagreements sit in tables under archive headings (v7, v6, v4–v5); those tables are stale but labelled as archives. Two stale sentences remain in `ch_P.tex` itself |

---

## Z1.5.02 — Counting a finite family at principal level

Blueprint: `ch_P.tex:12518–12527` (statement and assembly, label `r5:small:Z1.5.02`), `ch_P.tex:12657–12692` (label `r6:Z1.5.02`), map item `ch_P.tex:11646`, unit row `ch_Z.tex:707`.

### Statement vs Lean — matches

- `CardK` (`AutomorphicForms/IsoOfFrob.lean:19–23`): for every CM field `K` and `n ≥ 2` there exist `c, A` such that for all strictly decreasing `m`, all `H` with `|m_i| ≤ H`, all `M ≥ 1`, and every finite `S ⊂ SigK K m M` in which isomorphism implies equality, `|S| ≤ c (M(H+1))^A`. The blueprint has the same quantifier order: `K, n` fixed first, constants before `m, H, M, S` (`ch_P.tex:12520`, `12662`).
- `SigK` (`IsoOfFrob.lean:13–14`): infinitesimal character `infOf m` at every embedding, conjugate duality, nonzero `KLev K n M`-fixed vector. All three clauses are quoted. Conjugate duality is unused in the proof (also unused in Lean).
- Constants: Lean returns `c₂·c₁` and `A₁ + A₂` with `A₂ = [K:ℚ]·n²` and `c₂ = c·3^{A₂}` (`CohBoundFree.lean:69–91`). The blueprint gives `c₁c₂[M(H+1)]^{A₁+A₂}` with `A₂ = [K:ℚ]n²` and "absorbing the fixed power of three" (`ch_P.tex:12524`, `12691`). Correct.
- The record `Hypotheses'` is used only through its fields `cohC` and `borelC` (`TCardK.lean:26–29` original numbering; `graphq deps` confirms). The blueprint says exactly this (`ch_P.tex:12526`, `12691`).

### Proof check — correct

I checked each step against the Lean lemma it cites.

1. **Passage from level `M` to `3M`** (`klev_three`, `TCardK.lean:10–17`): `(3M) ⊂ (M)`, so the kernel mod `3M` lies in the kernel mod `M`. Correct.
2. **Projective resolution and per-degree bound** (`bddArith_cx`, `BddArith.lean:38–49`): `ℂ[G/S]` is projective for finite `S` by averaging; `Hom_G(ℂ[X_q], V)` embeds in `V^{|G\X_q|}`. Correct, including for infinite-dimensional `V` (Lean `totCoh` and `Bdd` are cardinal-valued, `RankHomology.lean:14–17`).
3. **Degree cutoff `D`** (`adelic_rep_dimension_bounded`, Lean `DimBdd`): the injection of distinct vertices of a tuple into `∐_r G_{v_r}` via `(r_j, g_j k_{r_j}^{-1})` is well defined and injective; `D = Σ_r |G_{v_r}|` does not depend on the tuple. Matches the Lean statement "for `p ≥ D` no tuple is injective".
4. **Alternation** (`rep_hom_alternating_sum_eq_zero`, `altChain_of_permSplit`, `ext_vanishing_of_resolution_endo`): the normalized signed symmetrizer is a chain map, is the identity in degree 0, and vanishes on tuples with a repeated entry; a chain endomorphism of a projective resolution lifting the identity is homotopic to the identity, so `H^q = 0` for `q ≥ D`. Correct. The Lean `AltZero` and `PermSplit` statements are the ones described.
5. **Finite-index transfer** (`adelic_rep_bounded_of_subgroup_bounded`, `coind_retract_of_finite_index`, `…_comm_of_bounded_equiv`): I verified the retraction `F ↦ d^{-1} Σ_{gS} g F(g^{-1})` is well defined on cosets, equivariant, and left inverse to `w ↦ (g ↦ gw)`. Shapiro in both directions gives the bound for every subgroup commensurable with the image of `GL_n(𝒪_K)`. Correct.
6. **Coinduction comparison** (`toCo`, `RankHomology.lean:33–60`): `(Tf)(g)(z) = ξ(g) f(g^{-1}z)` is literally the Lean map; equivariance and the inverse formula check out. Fibre size `[K(3):K(3M)]` is `FibCard`.
7. **Stabilizers** (`arith`, `mem_arith`): the stabilizer of `gK(3)` is `{γ : g^{-1}γg ∈ K(3)}`; commensurable with the preimage of `K(1)`, which is `GL_n(𝒪_K)` (`ArithOne`, `ArithComm`). Correct.
8. **Index bound**: Lean uses `relIndex(K(3M), K(3)) ≤ relIndex(K(3M), K(1)) ≤ (3M)^{[K:ℚ]n²}`; the blueprint's "embedding the congruence quotient at level one" is the same route.
9. **Assembly** (`TCardK.lean:30–36`): `|S| ≤ cohDim ⊤ K(3M) (ratC Ξ) ≤ c₂ M^{A₂} dim Ξ`, then exponents raised using `M ≥ 1`, `H+1 ≥ 1`. Correct.

The K7 inputs (exactness of the augmented tuple complex in every degree, finitely many orbits in each degree, finite vertex stabilizers; Lean `sx_exact`, `KT.orb`, `KT.stabfin`, used in `BoundedComplexOfBoundedSimplicialComplex.lean:8–28`) are taken from Proposition `prop:P-r4-k7` (`ch_P.tex:1697 ff.`), whose proof does contain paragraphs on exactness, orbit counting and stabilizers (`ch_P.tex:1712–1890`). I did not re-review that proposition; Z2.K7 is marked complete in `ch_Z.tex:786`.

### Problems

1. **Class-number finiteness for `GL_n` is asserted, not proved, not cited, not labelled** (`ch_P.tex:12682`, sentence "At level one the upper triangular decomposition and approximation for its unipotent factor reduce to diagonal matrices…"). In Lean this is `PIW.ClassFinD.borelKGL_of` (`BorelGL.lean:83–102`) fed by three separate theorems in `FiniteAdelicDoubleCosets.lean:13–21`:
   - `GlobalTheory.T.iwasawaDecomposition_finiteAdeles_GL` (`IwasawaDecompositionFiniteAdelesGLStatement.lean:14–15`),
   - `GlobalTheory.T.strongApproximation_upperUnitriangular_finiteAdeles` (`StrongApproximationUpperUnitriangularFiniteAdeleStatement.lean:14–15`),
   - `PIW.ClassFinD.idele_class_finite` (`LatticeIdealNonzero.lean:43–108`).
   
   All three are `[thm, core]` in the graph. The blueprint names none of the three and cites only `borelKGL_of`. This needs either a "[Proved in Lean, not reproduced: …]" label naming them or literature references. It is the only step of the unit that is neither reproduced nor labelled.
2. **The hypothesis label names no discharge site** (`ch_P.tex:12526`: "[Hypothesis, discharged at the use:] … Z1.5.03 supplies that record unchanged"). `graphq callers` confirms the only caller is `countK_alt` (`FrobeniusTraceCountBoundOfCmEigensystemCount.lean:63–125`), which passes `hP` through — that is a pass-through, not a discharge. The record is actually built in `published_hypotheses_from_patching_alt` (`PublishedHypothesesFromPatching.lean:98–103`; `graphq callers Hypotheses'.mk`), where `cohC := clozelCohC_alt hN` (`TPCohC.lean:10–30`, derived from `LiteratureRankNHypothesis`) and `borelC := Z.Coh.borelInjC` (`ClozelCohomology/ClozelConjC.lean:31`, a proved core theorem). The blueprint cites this site elsewhere (`ch_P.tex:10289–10293`) but not here.
3. **Unexplained shorthand** (`ch_P.tex:12691`): "The fields `cohC` and `borelC` are B at the counting theorem." "B" is the notes' private code for "hypothesis supplied by the caller" (`P_notes.md:74`); it is not defined in the chapter.
4. **Stale sentence in the map entry** (`ch_P.tex:11646`): "A literal combined bound remains to be identified." This contradicts the unit's complete status.
5. **Open and compact** — `borelC` requires `K(3M)` to be open and compact (`isOpen_KLev`, `isCompact_KLev`, `KLevTop.lean:66–91`). The blueprint does not mention this. Trivial, but it is a Lean theorem the proof uses.
6. **Unit row is vague** (`ch_Z.tex:707`): "Under the stated automorphic inputs" does not say which inputs; only `cohC` and `borelC` are used.
7. **Line ranges**: `Hypotheses'` is cited as `AutomorphicFormHyp.lean:12–17`; the graph gives 12–22. `countK_alt` is cited as 63–68; the theorem spans 63–125. Cosmetic.

### Labels

- "[Proved in Lean, not reproduced: …]": **none appears in the unit.** Everything else is reproduced or referred to an earlier proposition, so the only missing label is item 1.
- "[Hypothesis, discharged at …]": present, site incomplete (item 2).

**Verdict: COMPLETE WITH GAPS.** No statement mismatch and no mathematical error.

---

## Z4.2.08 — Integrality of the normalized scalar

Blueprint: `ch_P.tex:13197–13214` (label `r6:Z4.2.08`), map item `ch_P.tex:11691`, unit row `ch_Z.tex:741`.

### Statement vs Lean — matches

- Root: `scal_at_site : AllSites (… S => J.Dict std → S.Scal)`. `S.Scal` unfolds (`JointCmpEmbeddingY.lean:165`, `DefsRepLt.lean:177–181`) to: for all `j < mm`, every representative `L0 ∈ repOf`, every `La'` at `j+1` that is a lattice tuple, `scalG ∈ Qbar` and `‖p^{expG} · λ(scalG)‖ ≤ 1`.
- `expG = Σ_v vm_{v,j+1}·(len_v(L') − len_v(L))` (`ScalG.lean:19–21`). The blueprint's `e` is the same (`ch_P.tex:13198`).
- The blueprint states the hypothesis as "(B) is `J.Dict(std)`" and proves norm exactly one, which implies `≤ 1`. Faithful.
- The unit row (`ch_Z.tex:741`) omits the dictionary hypothesis; the map item (`ch_P.tex:11691`) has it.

### Proof check — follows the Lean proof

The Lean root is three lines: it applies `thetaSeries_scalar_bounded_of_pos_pair` (= `scal_of_pos_pair`, `ThetaSeriesScalarBoundedOfPosPair.lean:22–87`) to `Dict`, the split-chart pair `⟨J.alg0, J.alg⟩`, `pos_at_site S` (Z4.2.05) and `kernelSite_latticeTuplePairs_admissible S hd` (the root theorem of Z4.2.04). The blueprint paragraphs map onto the Lean steps as follows.

| Blueprint paragraph | Lean step | Check |
|---|---|---|
| "Both determinants belong to the norm-one group… first-factor orders are −ℓ_v" | `lattice_det_mem_U1_and_ordA_eq_neg_len` | Matches statement; argument is two sentences |
| "Determinant ideals have norm one… a positive power is generated by a norm-one element z… χ(𝔞)^k = (∏τ(z))^{-1}" | `determinantIdeal_normOne_char_unitary_smul`, `chi_alg_unit_inert` (`ChiAlgUnitInert.lean:21–58`) | Matches the Lean proof line by line |
| "At the odd inert prime the CM product is a unit…" | `normUnit_of_inert` → `frobOut_of_inertK`, `normUnitK_of_frobOut`, `prod_embT` | Matches. `InertK` is `jacobiSym(−d, p) = −1`; the type norm `nPsi z ∈ E` satisfies `y·ȳ = 1` (`nPsi_conj`); a Frobenius acting by −1 on `√−d` fixes every prime over `p` and inverts `(y)` |
| "For a norm-one idele d… d^{2h} = (a/ā)(k/k̄)… ‖λ(μ(d))‖ = ‖p‖^{Σ w_v ord_v(d)}" | `lambdaCharacter_norm_eq_p_pow_of_pos` (`NormLambdaCharacterNormOneIdeleEqPPow.lean:19–84`) | Matches: `x^m = z·k`, `mu_mul`, `mu_rat`, finite order of `μ(k)`, `norm_lamC_type_normOne`, `vm_shift_cancels`, additivity of `ordA` |
| "lift it to a one-dimensional unitary matrix y… z/z̄ = z²… finite image" | `mt_finite_order` (`MtFiniteOrder.lean:14–59`), `circle_pow`, `finite_order` (`HeckeCharFiniteOrderUnitIdele.lean`) | Matches in outline. The no-small-subgroups argument is correct. I did not trace the "tie" reading of `y²` in detail |
| "read the last added block… lifted highest weight… two constant shifts" | `fillAt_of_comp` (`SystemWeightsEqShiftedCharacterExponents.lean:30–65`), Lean `FillAt` | Matches the two shifts in `FillAt` |
| "remaining factor is μ(d_{L'})/μ(d_L)… exponent −e… norm exactly one" | `scal_of_pos_pair`, final `calc` | Verified: `−len(L') + len(L)` weighted by `vm` cancels `expG` |

I found no mathematical error. The sign conventions (orders are minus lengths; `μ` evaluated at index `j+1` on both determinants) agree with `scalG` (`ScalG.lean:22–28`).

### Problems

1. **No "[Hypothesis, discharged at …]" label for the dictionary** (`ch_P.tex:13198`). The text says only "The hypothesis (B) is `J.Dict(std)`". The discharge site, verified with `graphq callers`: `scal_at_site` ← `kernelSite_seriesScalar_pow_integral` ← `admissible_at_each_site` (`JointSiteChainComparedCarriesAdmittedSystem.lean:29–75`), where `hDict := latticeTuple_joint_dictionary t std J` (= `joint_dict`, Z4.2.03, complete). Z4.2.04 mentions `joint_dict` (`ch_P.tex:13182`); Z4.2.08 does not.
2. **Dependence on the partial unit Z4.2.04 is understated.** The Lean root calls the Z4.2.04 theorem (`pairOK_allSites`, `KernelSiteLatticeTuplePairsAdmissible.lean:23–47`) and uses only its first conjunct (even rank and self-duality of the two kernel lattices). The blueprint says "as in Z4.2.04" and "without using the theta-coefficient assertion left open in Z4.2.04" (`ch_P.tex:13200`, `13214`). That is accurate, and the clause used is the one Z4.2.04 does reconstruct (`ch_P.tex:13178`, `even_and_isSDLat_kerN`). But "the rank at the site is even" is itself asserted there in half a sentence. The complete status of Z4.2.08 therefore rests on that sentence.
3. **Site-law fields are used as givens without being flagged.** The Lean proof uses `S.law.mu_mul`, `S.law.mu_rat`, `S.law.mu_read`, `S.law.mu_alg` and `S.curve` (which supplies `p ≥ 5`, inertness and `IsChi`). These are fields of the site record `J.At`, whose existence is Z4.2.02 (`joint_at_nonempty`, **partial**, `ch_Z.tex:735`). The blueprint refers to "the site character law" and "the odd inert prime" without saying these are hypotheses carried by the site. The header "complete under the site dictionary" (`ch_P.tex:13141`) should read "for a given site, under the dictionary".
4. **No "[Proved in Lean, not reproduced]" label anywhere in the unit**, although several steps are stated in one or two sentences rather than proved:
   - determinant order equals minus the length (`latticeTuplePoint_det_normOne_order_eq_neg_length`, `…:111–125`, plus `len_bases`);
   - why the Frobenius acts on the type norm as complex conjugation (needs `c^{-1}g ∈ Ψ` and `nPsi_inv`, `NormProdCmEmbeddingsEqOneOfInert.lean:265–353`); the text says only "It acts on the type norm by conjugation";
   - the tie reading in `mt_finite_order`;
   - properties of `ordA` (`OrdA.ordA_props`) and `vm_shift_cancels`.
   
   Each is plausible and consistent with the Lean statement, but a reader cannot reconstruct them from the text. Either expand or label.
5. **Wrong file name** (`ch_P.tex:13200`): `NormProdCMEmbeddingsEqOneOfInert.lean` does not exist; the file is `NormProdCmEmbeddingsEqOneOfInert.lean` (graph module `…NormProdCmEmbeddingsEqOneOfInert`).
6. **Line ranges off by a few lines** against the graph: `chi_alg_unit_inert` 21–59 (graph 21–58); `lambdaCharacter_norm_eq_p_pow_of_pos` 19–88 (19–84); `latticeTuplePoint_…` 111–128 (111–125); `norm_lamC_type_normOne` 58–100 (58–97). Cosmetic.
7. **Stale sentence in the map entry** (`ch_P.tex:11691`): "A character-value comparison must also account for the length exponent and determinant factors" reads as an open task for a unit now marked complete.

**Verdict: COMPLETE WITH GAPS.** The implication `Dict → Scal` for a given site is correctly and recognisably reconstructed; the gaps are labelling, scoping and compression.

---

## Z1.5.07 — were the R5 gaps fixed?

| R5 item | Round 6 | Evidence |
|---|---|---|
| Potentially crystalline branch of the twisted level condition unlabelled and unreproduced (`potCrys_twistBy`, crystallinity of `χ_cyc^j`) | **Fixed — by reproduction, not by label** | New section `ch_P.tex:12583–12589` (`r6:review:Z1.5.07`). Multiplication by `t^j` on the period factor intertwines the twisted and untwisted actions and identifies the invariants. This is the Lean proof: `isCrys_mul_cyc` (`BlockCharactersCrystallineOfRules.lean:28–72`) uses `PD.t_unit`, `PD.t_act` and `mulLeftLinearEquiv`. The compositum step matches `potCrys_twistBy` (`GaloisHodgeOfCuspidal.lean:188–234`, `supExt`). The main text points to it (`ch_P.tex:12512`) |
| Continuity of the twisted representation not mentioned | **Fixed** | `ch_P.tex:12588` |
| Misleading sentence about inverses of matrices | **Fixed** | Sentence removed; `ch_P.tex:12512` and `12588` now say the classifier gives the roots `b^{-1}` at `σ^{-1}` directly |
| Unit conditional on `CountKAlt` (Z1.5.03, structure only) | Unchanged, correctly stated | `ch_P.tex:12588` last sentence; `P_notes.md:50` |

Remaining remark: the reproduced argument treats general `V` directly, while Lean reduces to the rank-one character and tensor closure; the text says so. No objection.

## Z2.K4 — were the R5 gaps fixed?

New section `ch_P.tex:12591–12608` (`r6:review:Z2.K4`); label paragraph in the main section `ch_P.tex:11832–11837`.

| R5 item | Round 6 | Evidence and residue |
|---|---|---|
| Reference for invariant form ↔ group cocycle comparison | **Fixed** | `ch_P.tex:12596`: explicit chain map from the homogeneous bar resolution to smooth singular simplices of the cone, both free resolutions for a torsion-free subgroup, de Rham integration, transfer back; cites Lee Thm 18.14 and Hatcher §3.G, plus Borel Thm 7.5 |
| Torsion-free finite-index subgroup uncited | **Fixed (now proved)** | `ch_P.tex:12593`: kernel mod 3. I checked the 3-adic valuation argument, including `p = 3` |
| Künneth, torus cohomology, transfer, cross product uncited | **Fixed** | `ch_P.tex:12601`, Hatcher §3.2 and §3.G |
| Real bar homology vs `ℝ ⊗ H_*(–;ℤ)` | **Fixed (now proved)** | `ch_P.tex:12607`, flatness; cites `SBridge`, `th_zc` |
| Missing "Proved in Lean, not reproduced" labels for `sWhit`, `sCen`, `sLoc`, `sMean_of`, `sHecke`, `sPU`, `sHt_of`, `sPrime_of` | **Fixed in substance, not by name** | `ch_P.tex:12604` lists "a suitable prime, a Hecke comparison, height and partition-of-unity bounds, a moment, Whitney reconstruction, central averaging, a spectral gap, localization, an invariant mean and an invariant-form input". All eight are covered descriptively. Only `JoinReconstruction.key`, `sGap_of`, `sMom_of` appear as Lean names (`ch_P.tex:11834–11837`, `12605`); `grep` finds none of the eight names in `ch_P.tex` |
| State plainly that the hand proof of `SSurj` is not the formalized proof | **Fixed** | `ch_P.tex:12604`: "The hand proof uses the preceding published comparison for the entire stable-realization input" |
| `torsStab` discharge note | **Fixed in substance, not in label form** | `ch_P.tex:12607–12608`: "The Selmer upper-bound assembly supplies precisely this torsion statement as its first input", citing `sUpperOf` (`SUpperOf.lean:64–66`). `graphq` (R5) confirmed `sUpperOf` is the only caller. No bracketed "[Hypothesis, discharged at …]" wording. Which stability theorem is relied on is now stated |
| Unused hypothesis `k+1 < r_2(L)` unexplained | **Fixed** | `ch_P.tex:12601`: "enters the formal Hecke proof through its Hecke input". Verified: `SHecke` carries `k + 1 < nrComplexPlaces L` (`SBridgeAlt.lean:66–72`) |
| `P-Milne-Mink` theorem number | **Fixed** | `%BIB` at `ch_P.tex:1657` now reads "Theorem 4.3 on integral ideal representatives and Theorem 5.1 on the lattice of logarithms of units"; the unit-theorem citation `[Theorem 5.1]` at `ch_P.tex:12601` agrees |

Not addressed (was an R5 "other observation", not on the task list): primary sources for homological stability (Maazen; van der Kallen) are still absent from the bibliography; `grep` finds neither name.

### Citation checks and how they were made

- **Milne, ANT v3.08, Thm 4.3 and Thm 5.1** — fetched `https://www.jmilne.org/math/CourseNotes/ANT.pdf` (machine summary of the text, characters 0–200,000 of the PDF). The version is v3.08 (July 19, 2020). Theorem 4.3 is the existence of integral ideal representatives under a bound, Theorem 4.4 is finiteness of the class number, Theorem 5.1 is the unit theorem, and the proof of 5.1 uses the logarithm map into the hyperplane. Both `P-Milne-Mink` (`ch_P.tex:1657`) and `P-R3-ANT` (`ch_P.tex:1101`, "Theorems 4.4 and 5.1") are correct.
- **Hatcher §3.2 and §3.G** — fetched the table of contents `https://pi.math.cornell.edu/~hatcher/AT/AT-toc.pdf`: §3.2 is "Cup Product" and contains "A Künneth Formula"; §3.G is "Transfer Homomorphisms". The descriptor "cross products and transfer" is consistent. I did not read the sections themselves.
- **Lee, Introduction to Smooth Manifolds, 2nd ed., Thm 18.14** — **not verified from the source.** A web search returned copies of the book, but I did not open the text of Chapter 18. The citation is plausible (Chapter 18 is the de Rham theorem chapter) and should be confirmed by someone with the book.
- **Borel Thm 7.5** — not re-checked; R5 review A checked it by fetching the Numdam PDF.

---

## Status consistency audit

### Method

Extracted the 54 `\textbf{ID} \emph{(status)}` rows of `ch_Z.tex` (lines 699–787) by regex; extracted every Markdown table row and every bold "ID — status" line in `P_notes.md` that names a unit; compared mechanically; then read the surrounding headings.

### Current tables agree

- `ch_Z.tex`: 26 complete, 19 partial, 9 structure only; the summary table at `ch_Z.tex:698` says 26 / 19 / 9 / 54 and the specialty rows sum correctly.
- `P_notes.md:5`: 26 / 19 / 9. The three v8 tables (`P_notes.md:11–18`, `24–38`, `46–59`) give 31 explicit statuses, and `P_notes.md:40` names the nine structure-only units. **All 40 agree with `ch_Z.tex`.**
- The other 14 units (N188, N415, Z1.4, Z2.K1, K2, K5, K6, K7, K8, Z3.1, Z3.2, Z4.1, Z5.1, Z5.2) have no row in any v8 table; they are complete in `ch_Z.tex` and complete by subtraction in the notes (26 − 12 listed).
- Arithmetic of the v7 → v8 change (`P_notes.md:5`): 26·6·22 → complete +2 (Z1.5.02, Z4.2.08) −2 (Z1.2, Z4.4) = 26; partial 6 − 1 + 12 + 2 = 19; structure 22 − 13 = 9. Consistent.
- "13 of 20 original inputs complete" appears in `P_notes.md:7` and `ch_P.tex:23`. Consistent.
- Status words in `ch_P.tex` section titles (`12611–12622`, `13177–13277`) and the status lines for Z4.4 (`12347`) agree with `ch_Z.tex`.

### Disagreements (all in archived tables)

| `P_notes.md` location | Heading | Unit | Says | `ch_Z.tex` / v8 | Note |
|---|---|---|---|---|---|
| 84 | v7 archive, prose | Z1.2 | complete | partial | Superseded; the archive note at line 68 says so |
| 93 | v7 archive, prose | Z4.4 | complete | partial | Same |
| 70 | v7 archive, prose | — | "15 of 20 complete" | 13 of 20 | Superseded |
| 118 | v7 ordering table | Z1.5.02 | partial | complete | Stale |
| 121, 122 | v7 ordering table | Z1.3.01, Z1.3.02 | structure only | partial | Stale |
| 123, 124 | v7 ordering table | Z4.2.04, Z4.2.06 | structure only | partial | Stale |
| 125 | v7 ordering table | Z4.2.08 | structure only | complete | Stale |
| 126, 127 | v7 ordering table | Z4.2.02, Z4.2.07 | structure only | partial | Stale |
| 128 | v7 ordering table | Z1.3.04 | structure only | partial | Stale |
| 129–132 | v7 ordering table | Z4.2.09, .11, .10, .12 | structure only | partial | Stale |
| 133 | v7 ordering table | Z1.3.08 | structure only | partial | Stale |
| 162 | v7 detail table | Z1.5.02 | partial | complete | Stale |
| 214 | v6 table | Z4.3 | complete | partial | Stale (already corrected at line 184) |
| 222 | v6 table | Z2.K4 | partial | complete | Stale |
| 1094–1096 | v4–v5 prose | K2, K4, K7 | open | complete | Stale |
| 1167–1168 | v5 table | Z1.4 | partial | complete | Stale |
| 1172–1173 | v5 table | Z2.K2 | partial | complete | Stale |
| 1174–1175 | v5 table | Z2.K4 | partial | complete | Stale |
| 1178–1179 | v5 table | Z2.K7 | partial | complete | Stale |
| 1183–1184 | v5 table | Z3.2 | partial | complete | Stale |
| 1185 | v5 table | Z4.1 | partial | complete | Stale |
| 1226–1229 | v5→v6 appendix | Z2.K2, K4, K7 | "theorem awaiting hand reconstruction" | complete | Stale |
| 358 | v6 per-unit map | Z1.5.02 | "No citation here for the combined bound" | complete | Stale remark |

Rows that agree but only by coincidence: Z1.2, Z4.3, Z4.4 are "partial" in the v5 table (`1165`, `1187`, `1188`) and partial now, after having been complete in between.

Rows that are not unit statuses: parent packages Z1.1, Z1.3, Z1.5, Z4.2 (`218–223`, `1164–1186`) are not rows of `ch_Z.tex`; "closed" in the v5 table is the old word for complete and agrees for Z2.K1, K5, K6, K8, Z3.1, Z5.1, Z5.2.

### Which tables are stale

- **Stale, but under an explicit archive heading:** everything from `P_notes.md:66` on — "v7 판정 기록 (보관)" (66–189), "v6 당시 판정" (191–762), "v3 보관 기록" (764–1070), "v4–v5 보관 기록" (1072–1216), "v5에서 v6로 넘어갈 때의 부록" (1218–end). The three examples in the task (line 76 vs 222 and 1174 for Z2.K4; lines 118, 125, 162 for Z1.5.02 and Z4.2.08) are all of this kind. They are historical records, not contradictions, **provided the reader notices the heading**. The v7 archive carries a supersession note (line 68) that mentions only Z1.2, Z4.4 and "the open-unit list"; it does not warn that the 36-row ordering table (107–144) is out of date for 14 rows. The v6 heading (191) and the v4–v5 heading (1072) carry no supersession note at all.
- **Current and consistent:** `P_notes.md:1–64` and `ch_Z.tex`.
- **Stale text inside `ch_P.tex` (not archived):** `ch_P.tex:11646` (Z1.5.02, "A literal combined bound remains to be identified") and `ch_P.tex:11691` (Z4.2.08, "A character-value comparison must also account for…"). These sit in the specialist-map section, which a reader will take as current.

Suggested repair: add a one-line "superseded by v8; statuses below are historical" note under the headings at lines 103, 146, 191 and 1072, or add a "v8" column to the 36-row table; and edit the two map sentences in `ch_P.tex`.

---

## Summary of verdicts

- **Z1.5.02 — COMPLETE WITH GAPS.** Statement and constants match Lean; the cohomology-bound argument is correct step by step. Gaps: GL_n class-number finiteness (three Lean theorems) is asserted without proof, citation or label; the hypothesis label gives a pass-through, not the real discharge site (`published_hypotheses_from_patching_alt`, `PublishedHypothesesFromPatching.lean:98–103`); one stale sentence.
- **Z4.2.08 — COMPLETE WITH GAPS.** Statement matches; the proof mirrors `scal_of_pos_pair` and its inputs. Gaps: no discharge label for `J.Dict` (site: `admissible_at_each_site`, `JointSiteChainComparedCarriesAdmittedSystem.lean:29–75`); reliance on site-law fields (Z4.2.02, partial) and on the even-rank/self-dual clause of Z4.2.04 (partial) should be stated as scope; four steps are one-sentence assertions with no label; one wrong file name.
- **Z1.5.07 — R5 gap fixed.** The `B_cris` twist is now reproduced and agrees with the Lean proof.
- **Z2.K4 — R5 gaps mostly fixed.** Comparison reference, torsion-free subgroup, Künneth/transfer, scalar extension, `r_2` hypothesis and the Milne theorem number are fixed. The eight Hecke-route inputs are labelled descriptively but not by Lean name; the `torsStab` consumer is named but not in the bracketed label form. Lee Thm 18.14 was not verified from the source.
- **Status audit.** `ch_Z.tex` and the v8 section of `P_notes.md` agree on all 54 units. Every disagreement is in an archived table (v7, v6, v4–v5); those need a clearer "superseded" marker. Two stale sentences remain in `ch_P.tex` (lines 11646, 11691).
