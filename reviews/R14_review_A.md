AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

# R14_review_A

AI review report produced during this project; file names are internal working names.

- Internal source file: `out/R14_review_A.md`
- SHA-256: `de9371122d85257a3871435c76082b2dd702e905ad9c64d430fa005eae7d31be`
- Report scope: R14 review A — Z4.2.13 `GlobalTheory.TieBase.base_data` and Z4.3 step (i)

## Internal report

The report below preserves its original verdict, scope and unresolved points. Source line numbers in other records count from its original title.

# R14 review A — Z4.2.13 `GlobalTheory.TieBase.base_data` and Z4.3 step (i)

Reviewed: `ch_P_r14.tex` lines 1–943 against the Lean source at commit `40e56bab…` (original numbering), the register `R14_pending.json` (37 Z4.2.13 rows) and the dependency graph.
Nothing here claims or implies that RH is proved. The review only compares hand proofs with the Lean statements they label.

## 1. Verdicts

**Z4.2.13 closure: DO NOT CLOSE.** Keep the unit `partial`.

- The root assembly is correct and the four conclusions match Lean exactly.
- The lattice law `LatAll` and the period nonvanishing are fully hand-proved. That is the only conjunct I would accept as closed.
- `VecP` and `EqP` are reduced to suppliers, and most of the cone sits behind suppliers that are not hand-proved here:
  - 5,366 theorem lines are reachable only through the inputs the author declares (three CM laws, four local Weil inputs).
  - 5,355 more are reachable only through the "operator inputs" (`exists_weil`, `vacuum_inert`, `vacuum_exact`), which are labelled but only sketched.
  - **18,877 more are reachable only through suppliers that are neither proved nor labelled as inputs** (list in §3.3).
- The eight literature leaves of the cone (Hasse norm theorem, Landherr-type statements) are never cited at their points of use.

**Z4.3 (i): statement covered, proof conditional.** §r14:equivariance targets exactly the conjunct that `transOne` and `vac_leftE` consume, for every base and every `IsChi` character, so the χ-tracking is sound (and in fact unnecessary). The proof inherits the same unproved suppliers as `EqP` (§4).

**Per-declaration count:** 24 CONFIRMED, 13 CONFIRMED WITH GAPS, 0 NOT CONFIRMED. All 37 Lean declarations were read individually, including the eight one-line wrappers. Register rows (file, lines, cone size) all agree with the graph.

### Verdict table

"Minor" = a routine or standard step is asserted. "Major" = the hand proof is an assembly whose substantive suppliers are not proved here.

| # | Declaration (Lean lines) | Label | Statement | Verdict | Main remark |
|---|---|---|---|---|---|
| 1 | `Base.latAll` (`IsAdmissibleFlagPair…:623–644`) | lat-indices | match | CONFIRMED | `hδ` is a pure pass-through (never used below) |
| 2 | `hermitian_form_integral_values` (`PThIndep:11`) | lat-integral | match | CONFIRMED | wrapper |
| 3 | `hermitian_pairing_integral` (`PHfInt:203–207`) | lat-integral | match | CONFIRMED | |
| 4 | `arithmetic_hermitian_form` (`PHfInt:209`) | lat-integral | match | CONFIRMED | wrapper |
| 5 | `AR.div_okc` (`PHfArith:321–389`) | lat-integral | match | CONFIRMED | hand proof gives m = index, stronger than Lean |
| 6 | `curve_lattice_self_dual` (`PSelfDual:563–622`) | lat-dual | match | CONFIRMED | ℤ-basis of the ideal assumed |
| 7 | `SD.coord` (`PSelfDual:184–261`) | lat-dual | match | CONFIRMED | different but valid route (Dedekind independence) |
| 8 | `SD.alg_step` (`PSelfDual:117–180`) | lat-dual | match | CONFIRMED | |
| 9 | `SelfDualRec_of_curve` (`PSelfDual:310–393`) | lat-dual | match | CONFIRMED | |
| 10 | `self_dual_lattice` (`PSelfDual:624`) | lat-dual | match | CONFIRMED | wrapper |
| 11 | `IO.semiChar_of_HfInt` (`PIopIso:240–267`) | lat-indices | match | CONFIRMED | |
| 12 | `IO.La_index_finite` (`PIopIso:315–330`) | lat-indices | match | CONFIRMED | |
| 13 | `IO.La_index_ne_zero` (`PIopIso:332–338`) | lat-indices | match | CONFIRMED | wrapper |
| 14 | `Base.thMoved_ne_zero` (`…:251–262`) | vec-transport | hypotheses not displayed | WITH GAPS (major) | θ_M ≠ 0 rests on the unnamed "fourfold kernel theorem" |
| 15 | `Base.vec_mem_ne` (`…:656–660`) | vec-transport | match | WITH GAPS (major) | `StdOK` supplier is one sentence |
| 16 | `chiFac_mem` (`TranslateMoments…:337–339`) | vec-transport | match | WITH GAPS (minor) | "determinant ideals are norm one" asserted |
| 17 | `exists_field` (`ExistsMovesOfSelfDual:407–420`) | vec-fixed | match | CONFIRMED | infinite Galois correspondence uncited |
| 18 | `exists_coef_field` (`…:442–515`) | vec-fixed | match | WITH GAPS (major) | three CM laws are inputs; two further facts unlabelled |
| 19 | `ColNorms.familyVectors` (`NormalisedFamilyNonzero…:15–50`) | vec-descent | match | WITH GAPS (major) | `algTAll` only sketched |
| 20 | `ExponentsFinite.yFinite` (`KernelConstantExponentsFinite:85–126`) | vec | match | CONFIRMED | unused by its only consumer here |
| 21 | `exists_chi` (`ExistsMovesOfSelfDual:659–695`) | eq-reference | match | WITH GAPS (minor) | `mem_detId_iff` asserted |
| 22 | `exists_family_of_curve` (`ExistsThetaVectorFamily…:15–108`) | eq-reference | match | WITH GAPS (major) | assembly only; see §2.5 |
| 23 | `WeilInter.om_iop` (`WeilRepresentationComm…:88–125`) | eq-transport | not displayed | WITH GAPS (major) | correspondence and membership suppliers unnamed |
| 24 | `exists_norm_eq_neg_one` (`ExistsDvdMulInvolutionAddOne:81–127`) | eq-rational | match | CONFIRMED | |
| 25 | `exists_mul_involution_add_one_mem_pow` (`…:41–106`) | eq-rational | match | CONFIRMED | |
| 26 | `RatEqui.exists_root` (`OddEqOfEven:26–40`) | eq-rational | match | CONFIRMED | |
| 27 | `RatEqui.exists_factor` (`OddEqOfEven:82–109`) | eq-rational | match | WITH GAPS (minor) | existence of the avoiding norm-one scalar not justified |
| 28 | `RatEqui.oddEq_of_even` (`OddEqOfEven:176–180`) | eq-rational | narrower than Lean | WITH GAPS (major) | hand proof treats only exponents a = a′ = 0 |
| 29 | `NatEqui.chi_smulLat` (`NormalisedFamilySatisfies…:17–33`) | eq-normalize | match | CONFIRMED | |
| 30 | `NatEqui.chiFac_ne_zero` (`…:42–45`) | eq-normalize | match | CONFIRMED | |
| 31 | `NatEqui.chiFac_right` (`…:47–51`) | eq-normalize | match | CONFIRMED | |
| 32 | `NatEqui.chiFac_left` (`…:53–57`) | eq-normalize | match | CONFIRMED | |
| 33 | `NatEqui.eqP` (`…:59–117`) | equivariance | match | WITH GAPS (major) | normalisation step correct; inherits #22 |
| 34 | `base_linkage_nonempty` (`PFamily:80–86`) | period | match | CONFIRMED | |
| 35 | `ThetaCoordLine.exists_eq_smul` (`ThetaFunctionSelfDual…:54–93`) | line | match | WITH GAPS (minor) | real spanning and symplectic basis asserted |
| 36 | `TieBase.base_data` (`KernelEntryPeriodNeZero…:14–19`) | base-assembly | match | WITH GAPS (major) | assembly correct; unit not closed |
| 37 | `NormGauss.sum_norm_neg` (`FinsumNormNeg:57–183`) | weil-sign | match | CONFIRMED | hand proof gives −q exactly |

## 2. Findings by section

### 2.1 Root statement and assembly (tex 12–43, 893–911)

- Lean: `∀ t : KerEntTied ex, t.δ ≠ 0 ∧ t.B.LatAll ∧ t.B.VecP t.χ ∧ t.B.EqP t.χ`. The text states the same four conclusions with the same `B` and `χ` (tex 27–30). `Base.tor`, `eNat`, `chiFac`, `LatAll`, `VecP`, `EqP`, `vec22`, `eq22`, `pull`, `Iop` were compared field by field; exponents `N′/2`, `−N/2` and the placement of the conjugate transpose in `pull` agree.
- The Lean proof is five lines and the text reproduces it: `base_linkage_nonempty`, `latAll`, `familyVectors`, `eqP`. "Neither `t.Hyp` nor a second character is a premise" (tex 910–911) is correct.
- Pass-throughs at this call:
  - `cm_field_facts_hold`, `induced_cm_type`, `yFinite` are passed to `familyVectors` (`…:18–19`) and discarded on entry (`intro D cc δ B χ _ _ hc hδ hχ _`, `NormalisedFamilyNonzero…:16`). The text says so (tex 470–473). Proving `yFinite` is therefore not needed for this unit.
  - `t.δ_ok` is passed to `latAll` and never used in the lattice records (`SelfDualRec_of_curve:311` binds it as `_`; the `HfIntRec` chain only forwards it). The text uses only δ ≠ 0, which is right.
- Callers of the root: `TwV.site_law_xiIn` (`KernelSiteLaw…:20–48`) and `T.kernelEntry_period_ne_zero_and_lattice_laws` (then `kerTh_eq_pull`). Matches tex 913–921.
- The size paragraph (tex 931–942) reproduces: 9,400 core declarations, 60,733 lines, 8 literature leaves; 3,766 ranged theorems with 51,444 lines; 176 singletons; `eqP` 50,356.

### 2.2 Period and lattice law (tex 34–173) — sound

Checked step by step against rows 1–13 and 34.

- `H(x,y) = a/√d + ib` with `a ≡ b (mod 2)` matches `HfInt` (`PIopIso:187–189`). The divisibility `v/m`, `(u+v)/(2m) ∈ ℤ` is exactly `hyZ`, `hxZ` in `div_okc:371–383`.
- The dual-lattice recovery follows `SelfDualRec_of_curve` line for line: ℓ(T) ∈ C from the plane, coordinates from `SD.coord`, then `alg_step`.
- Self-duality of `I = 𝔟⁻¹` is the host field `HostDer.unimodular` (`ConjEMemHostFIff:159–162`), a hypothesis carried by `D7`. The text's label "the fixed host supplies" is accurate.
- `d` prime and `d ≡ 3 (mod 4)` follow from `HostHyp` (`d % 16 = 7`).
- Small points, none affecting the verdict:
  - The existence of a ℤ-basis of the ideal (`CS.cc_basis`, 50 lines) is assumed at tex 93 and 114.
  - Integrality of the trace of `Q*P` (tex 71–73) is given by a localisation argument; fine.
  - The index bound uses `IsCurveIdeal` only through `cc ≠ ⊥`, and holds also for δ = 0.

### 2.3 Theta line (tex 175–242) — sound, minor gaps

- `exists_eq_smul` assumes positive area, discreteness and Im-self-duality, and no semicharacter law. The text's automorphy factor (tex 199) matches `ThSp`/`U`.
- Asserted without proof: that a discrete self-dual `A` spans over ℝ and has rank 2g (tex 205–206); existence of a symplectic basis for a perfect alternating form; that the normalising exponential can absorb the unit-modulus values of α on the first half.
- For frame lattices `LaB` (first disjunct of `KLat`), self-duality is referred to "the lattice argument above", which was written for `La(L,L′)`. `of_dual_families` covers both; one sentence is missing.

### 2.4 Natural vector and coefficient field (tex 244–493)

- **Nonvanishing (rows 14–15).** The inverse-intertwiner argument is right, but "cancels the two normalizations" (tex 305–306) needs `[Λ₁:Λ₁∩Λ₂] = [Λ₂:Λ₁∩Λ₂]`, which follows from self-duality and is not said.
  - `B.thZero ≠ 0` comes from `thM_spec`/`isThM_ne_zero` (3,001 theorem lines beyond the baseline). The text calls this "the fourfold kernel theorem" (tex 292) with no Lean name. An argument exists in the earlier paragraph `par:r4-z43-iso`, inside a unit still graded partial; it is not cross-referenced here.
  - `B.StdOK` comes from `SO.stdOK` (`PStdOK:338–339`, 3,161 lines): one sentence (tex 286–289).
  - `ThZeroMem` silently uses `lat0OK` (`La(S,S′) = powLat lamM`) and `areaOK`.
- **Two-torsion point (tex 332–336).** The trace argument proves the conjunct of `exists_point` that is used. Correct.
- **θ₀ and the vacuum (tex 337–366).** Existence and zero set of the modified sigma function (`sgStar` is an ε-choice; `OddTheta.sgStar_laws`, 980 lines) are used as standard facts without citation.
  - `Vacuum.exists_vacuum` (`NormSqMul…:276–355`, 16,557 lines beyond baseline) is cited with "the construction uses" (tex 362–366). `oddE0` has five conjuncts (`StandardLatticesGL3:496–500`); none is derived. It is not listed among the stated inputs.
- **Coefficient field (row 18).** The descent matches Lean: same adjoined set, `a = 1` from the fixed coefficient.
  - Labelled inputs: `integral_j_and_algebraic_data`, `taylor_algebraic`, `useConj_all` (tex 396–406). Good.
  - Unlabelled: a lattice is determined by `(g₂,g₃)` (`lamConj_eq_self`; `lamConj` is an ε-choice, so this is needed for "the torus is therefore T", tex 417–419); convergence of the conjugated series before reading its coefficients (`taylor_fnConj`).
  - Without a base, δ ≠ 0 comes from `InertSign.delta_ne_zero` (discriminant of a lattice is nonzero). Rows 18 and 22 are stated without a base; the text only derives δ ≠ 0 from the base (tex 34–43).
- **Natural side (row 19).** The final step `F = b·e`, `b = a_α(F)/a_α(e)`, `M = M₀(b)` is correct.
  - `ThLoc.algTAll` (15,462 lines) is described in tex 434–454 and introduced by "Equivalently". The key step is imprecise: "four directional derivatives control the fourth power" does not by itself give all coefficients. The correct argument is short (take a lowest nonzero coefficient `a_β`; then `a_β⁴` and `a_α a_β³` are coefficients of the tensor) and should be written.
  - Its two suppliers are unnamed: the fourfold identity again, and `AlgTranslate.coefIn_translate` ("the rational-translate theorem", 10,897 lines).
- **`yFinite` (row 20).** Proof correct, matches Lean. See §2.1 on its being unused.

### 2.5 Equivariance (tex 495–752)

- **Statement.** The three displayed laws match `eq22` (`TaylorLogMetric:37–50`), including which rank appears in which exponent.
- **Reference character (row 21).** Matches `exists_chi`. `mem_detId_iff` (membership in `detId(L₁,L₂)` equals integrality after dividing by `det(g₁⁻¹g₂)`) is asserted (tex 528–531).
- **κ itself is not constructed.** `exists_kappa` (`ExistsMovesOfSelfDual:570–657`) is used wholesale. The text labels as inputs "the split and inert vacuum identities and the construction of W" (tex 548–549). That label does not cover:
  - `InertTrivial.character_trivial_at_inert` (`CharacterTrivialAtInertPrimes:255–309`, 6,020 lines). It is what makes `κ∘P` take the value `∏τ(z)⁻¹` on rational norm-one `z` (`htriv`, `…:603–607`), i.e. the second clause of `IsChi` for the reference character, which `eqP` uses through `chi_smulLat hχ′`. **It is not mentioned anywhere in lines 1–943.**
  - `exists_base` (existence of the unitary extension, with `infChar_eq_one`), and `HeckeVal.hecke_values` (algebraicity of the scalar, "algebraic by the vacuum scalar comparison", tex 373–374).
- **Movers (tex 558–565).** "A rational unitary change puts a multiple sL in standard coordinates, with s coprime to m₀" is the whole content of `RepEqAt.repExS` (5,038 lines) and is where five literature leaves enter (`Published.herm_col`, `cc_ne_zero`, `det_map_cc`, `exists_basis_one_imaginary`, `exists_cc_eq_neg`). It is asserted, with no citation.
- **Transport (row 23).** The idea is right. The statement of `om_iop` (eight `Moves` hypotheses, δ ≠ 0, `F ∈ Th`) is not displayed. Its suppliers are unnamed: `exists_thetaLattice_correspondence_weilOperator` (the coset bijection, 1,341 lines), `WeilTheta.om_mem_Th_moved` (5,583), `ThetaLevels.levels_closed` (4,010).
- **Rational movers (rows 24–28).**
  - Rows 24–26 are complete and correct; I rechecked the lifting identity and `b̄ = b`.
  - The determinant identities are right: `det g · conj det(1−g) = det(1−g)` for even n, hence `|wᵐ|/wᵐ = τ(det g)^{−m/2}`; likewise `τ(det h)^{n/2}` on the target.
  - The scalar "|D₀|/D₀ times the normalized Gauss phase" is taken from `par:r4-z43-iso`, a paragraph of the earlier chapter in a partial unit. Say so, and say whether it has been reviewed.
  - Row 28: Lean's `oddEq` holds for every `WeilO` and every exponents `a, a′` with `2a′ = ε·n_τ + N`, `2a = ε′·n′_τ − N′` (`StandardLatticesGL3:487–494`). The text proves the case `a = a′ = 0` of the specific W. This is the case used at `ExistsThetaVectorFamily…:89`, but it is narrower than the labelled statement. The general case is the same computation with the factor `∏τ(det γ)^{−a}`.
  - Row 27: the scalar `z` with `z z̄ = 1`, `z ≠ 1`, `z⁻¹` outside the spectrum needs infinitely many norm-one elements; one line is missing.
  - `VacuumExact.vacuum_exact` (14,337 lines), `ThetaSpan.theta_span`, `RatExtend.om_eq_pull_of_vacuum` are argued in one paragraph each (tex 686–706).
- **Normalisation (rows 29–33).** Fully checked and correct: `B.thZero = a·E(S,S′)` with `a` depending only on the ranks; the ratio `C_χ/C_η` is invariant under both moves because χ and η pick up the same `∏τ(det g)⁻¹`; the two single-lattice laws follow by cancellation. No division by `a`. This agrees with `eqP:65–117`.
  - Multiplicativity of `detId` along a chain of self-dual lattices (`RelDetIdeal.detId_normOne_mul`, 548 lines) is asserted at tex 727–728.

### 2.6 Finite Weil action and inert sign (tex 808–891)

- Row 37 is complete: the fibre count and `−q` are correct, and the hypothesis `∃a, ψ(a+s(a)) ≠ 1` is the one the text derives.
- The λ normalisation gives `λ(p^{f_p}) = −√(p^{f_p})` as stated.
- The rest is a sketch with declared inputs (adjacent-lattice composition, local transvection, triangle coordinates, eighth-root property). Asserted without proof and not declared: that translates of the vacuum span the all-level theta space (`vacuum_fixed_span`, 5,620 lines in cone), the adelic model (`exists_isModel`), and the identification of the adelic sum with the theta average (`iop_eq_sumOp`).

## 3. Root closure

### 3.1 Method

Cone of `base_data`, type and value edges, stopping at literature leaves: 9,400 core declarations, 60,733 lines, 8 leaves. Core theorems with ranges: 3,766, 51,444 lines. All figures below are theorem lines out of 51,444.

No earlier round confirms anything inside this cone at declaration level. The only cone members that appear in `status.json` are the root itself, `eqP` (as a route), two pool samples and three "elementary literature leaves". Complete units Z4.2.06–.08 overlap the cone by about 22k lines, but they are conditional completions, not hand proofs of the shared declarations.

Coverage in the text: 175 theorems (4,545 lines) are identified by name or by a cited line range; 3,591 theorems (46,899 lines) are not.

### 3.2 Partition

The cone was cut at the head of every supplier that the text does not prove, then the cuts were released in order.

| Layer | Theorem lines | Cumulative |
|---|---|---|
| Hand-proof territory (reachable without any unproved supplier) | 21,846 | 21,846 |
| + author-declared inputs (3 CM laws, 4 local Weil inputs) | 5,366 | 27,212 |
| + "operator inputs" `exists_weil`, `vacuum_inert`, `vacuum_exact` | 5,355 | 32,567 |
| + suppliers neither proved nor labelled (§3.3) | 18,877 | 51,444 |

- Inside the hand-proof territory, 137 theorems (3,241 lines) are identified in the text; the other 18,605 lines are support lemmas the hand argument must absorb. Most are routine, but they include uncited standard theory: Weierstrass σ/ζ (about 1,300 lines), discriminant nonvanishing, uniqueness of a lattice from `(g₂,g₃)`, Taylor expansion of entire functions in several variables.
- Declared inputs, inclusive cones beyond the 602-line `D7` baseline: CM laws 13,646 (`useConj_all` 13,139 alone); local Weil inputs 3,100. The four local Weil inputs have zero exclusive lines: everything under them is also reachable elsewhere.
- The order of release matters because the cone is heavily shared. Releasing the unlabelled suppliers before the operator inputs gives 21,072 instead of 18,877.

### 3.3 Suppliers neither proved nor labelled

Sizes are inclusive theorem cones beyond the baseline; "excl." is what becomes reachable only through that supplier.

| Supplier | Lean | Size | Excl. | Treatment in text |
|---|---|---|---|---|
| `Vacuum.exists_vacuum` | `NormSqMulGaussianLatticeTranslateEqShifted:276–355` | 16,557 | 3,935 | "the construction uses" (tex 362–366) |
| `ThLoc.algTAll` | `AlgTAll:6`, `12–26` | 15,462 | 3,460 | sketch, "Equivalently" (tex 434–454) |
| `InertTrivial.character_trivial_at_inert` | `CharacterTrivialAtInertPrimes:255–309` | 6,020 | 4,764 | absent |
| `RepEqAt.repExS` (under `exists_moves_of_selfDual`) | `ExistsTriv:54–91` | 5,038 | 4,906 | asserted (tex 558–565) |
| `SO.stdOK`, `FourthRootStd.stdOK` | `PStdOK:338–339`, `SpanRangeEmb4EqTop:700–701` | 3,161 / 2,853 | 952 / 1,120 | one sentence (tex 286–289) |
| `thM_spec`, `isThM_ne_zero` | `IsAdmissibleFlagPair…:75–81` | 3,001 | 2,532 | "the fourfold kernel theorem" (tex 292) |
| `HeckeVal.hecke_values` | `UnitaryHeckeCharacterValues:232–278` | 879 | 445 | "algebraic by the vacuum scalar comparison" |
| `TrueTheta.exists_base` | `ExistsMovesOfSelfDual:519–564` | 402 | 180 | absent |

Further unnamed suppliers inside the hand-proof territory, which the text relies on by assertion: `ThetaLevels.levels_closed` (4,010), `WeilTheta.om_mem_Th_moved` (5,583), `VacuumScalar.lattice_facts` (4,615), `theta_translation_intertwiner_unitary` (3,407), `exists_thetaLattice_correspondence_weilOperator` (1,341), `NormSum.exists_lattice_of_adelic_point` (1,105), `detId_normOne_mul` (548), `relative_determinant_norm_one` (362).

### 3.4 Literature leaves

All eight are unlabelled at their points of use in lines 1–943.

- Under `exists_moves_of_selfDual` → `repExS` → `SelfDualGenus.*`: `Published.herm_col`, `cc_ne_zero`, `det_map_cc`, `exists_basis_one_imaginary`, `exists_cc_eq_neg`.
- Under `exists_vacuum` → `OddGenus.odd_one` → `SqDet.*` / `LocalQuad.*`: `Published.HasseNormSt`, `HasseNormSt.of_isSquare`, `QNorm.hasseNormSt`.

### 3.5 Closure verdict

DO NOT CLOSE. What is missing, in theorem lines:

- 18,877 behind unlabelled, unproved suppliers;
- 5,355 behind operator inputs that are labelled but only sketched;
- 5,366 behind declared inputs (accepted as inputs, but they keep the unit partial);
- 8 literature leaves without citation.

`δ ≠ 0 ∧ LatAll` (2,615-line theorem cone for `latAll`, fully inside the hand-proof territory) can be recorded as proved.

## 4. Z4.3 step (i)

**Does §r14:equivariance prove the conjunct that both applications use?** At statement level, yes.

- `transOne` (`InertCoprimeLemmas/IntAsm.lean:55–77`) takes an arbitrary `B`, `hcc`, `hδ`, `χ`, `hχ`, obtains `eq22 D B.tor χ (B.eNat χ)` from `eulerProduct_eq_of_curve_ideal` (line 65), and uses only its first conjunct, at the self-dual pair `(M,M′)` and unitary `(γ,γ′)` from weak approximation (lines 64–71).
  - `eulerProduct_eq_of_curve_ideal` (`SplitPairEquations/FinalEq.lean:10–13`) and `NatEqui.eqP` have identical hypotheses and conclusion (`B.EqP χ`). Replacing one by the other is legitimate.
- `vac_leftE` (`ThCLeftStab.lean:368–397`) takes `hE : B.EqP χ` and uses `hE.1` with `γ = 1` and `γ′ = matOf s γ.1` at the fixed pair `(s.lat N, s.lat N′)` (line 372). Its only caller `thC_left_stab` discharges `hE` by `NatEqui.eqP D cc δ B χ hcc hδ hχ` (line 436).
  - The text's description (tex 786–792) matches: `g = 1`, both lattices fixed, the conjugate transpose is the inverse target action.
- **χ-tracking (tex 754–784) is correct.**
  - `at_of_true_columns` gives `t` to the inert supplier and the witness `t′` of `Duty(t).forms` to the forms supplier (`AtOfTrueColumns.lean:37–41`).
  - `duty_of_std` takes `t′` from `standardKernelData_with_standardBaseLevels`; `stdKer_stdRd` rebuilds the record keeping `cc, δ, B, χ, cD, O, ent` and replacing only the reader and its chain (`StandardKernelDataWithStandardBaseLevels.lean:35`).
  - Because `eqP` is universal in `B` and in every `χ` with `IsChi`, each witness supplies its own `χ_ok` and the law applies. The tracking is not needed for (i).

**Is it proved?** No, conditionally only. The `eqP` cone (44,844 theorem lines) splits as 17,641 hand-proof territory, 5,373 declared inputs, 5,355 operator inputs, 16,475 unlabelled. All eight literature leaves are in it.

**The route chosen for (i) carries inputs it does not need.**

- `eqP` uses only `q1, q2, q3` and membership/nonvanishing at the standard pair (`…:64, 70`). It never uses the coefficient field.
- The first `eq22` conjunct in `exists_family_of_curve` (lines 82–94) uses of the vacuum only `e0 ∈ Th(S,S′)` and `e0 ≠ 0`: `exists_kappa` asks for exactly that (`ExistsMovesOfSelfDual:574`), and `isPull_row/col` receive `he.1` (`OddEqOfEven:178`).
- A hand proof of (i) can therefore start from any nonzero theta vector at the standard pair. That removes `exists_vacuum` (16,557), the three CM laws (13,646) and three of the literature leaves from the dependency of (i). What remains is the Weil operator with its split and inert identities, κ with `character_trivial_at_inert`, the rational pullback, and the movers.

## 5. Prioritised fixes

1. **State the suppliers of §3.3 as inputs, with Lean names and sizes, or prove them.** In particular add `character_trivial_at_inert`, `exists_base` and `hecke_values` to the description of κ (tex 519–552), and `exists_vacuum`, `algTAll`, `repExS`, both `stdOK`, `thM_spec` where they are used. Update `deeper_review_inputs` in the register accordingly.
2. **Cite the eight literature leaves** at tex 355–366 (orthonormal frame at 2) and tex 558–565 (rational unitary change), with the published statements used.
3. **Rewrite the Z4.3 (i) route without the CM vacuum** (§4), or state explicitly that the CM laws and `exists_vacuum` are not needed for the first conjunct.
4. **Row 28:** prove `oddEq` for general exponents `a, a′`, or relabel the hand proof as the case used.
5. **Row 19:** replace the "four directional derivatives" sentence by the lowest-coefficient argument; name `coefIn_translate`.
6. **Rows 14–15:** cross-reference `par:r4-z43-iso` for the fourfold identity and state its review status; mention `lat0OK`, `areaOK` and the equality of the two indices in the inverse-intertwiner step.
7. **Rows 18, 22:** add δ ≠ 0 from the discriminant when no base is present; cite uniqueness of a lattice from `(g₂,g₃)` and the convergence step for the conjugated series.
8. **Row 23:** display the statement of `om_iop` and name its three suppliers.
9. **Standard facts to cite:** Weierstrass σ existence and zeros; symplectic basis of a perfect alternating form; infinite Galois correspondence (row 17); idele–ideal dictionary and `mem_detId_iff` (row 21); multiplicativity and norm-one property of `detId` (rows 16, 29–32); infinitely many norm-one elements (row 27).
10. **Editorial:** tex 577 cites `ExistsMovesOfSelfDual.lean:442--518`; the theorem ends at 515 (tex 430 has it right). Drop or footnote the proof of `yFinite`, since its consumer ignores it.
11. **Bookkeeping:** record `δ ≠ 0 ∧ LatAll` as proved inside the partial unit; keep `VecP` and `EqP` open.
