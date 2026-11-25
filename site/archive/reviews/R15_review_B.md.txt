AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

# R15_review_B

AI review report produced during this project; file names are internal working names.

- Internal source file: `out/R15_review_B.md`
- SHA-256: `4fa6720c78f5bdc8654139141afe86ff3b43b59e71ee10d44d49376109240e0b`
- Report scope: R15 review B — L/R/N triage of the Z4.2.13 suppliers, four N hand proofs, Z4.3(i) vacuum-free route, Z4.3 premise table

## Archived report · [English summary](../../reviews/R15_review_B.md)

The report below preserves its original verdict, scope and unresolved points. Superseded graph percentages have been removed from this public edition. Source line numbers in other records count from its original title.

# R15 review B — L/R/N triage of the Z4.2.13 suppliers, four N hand proofs, Z4.3(i) vacuum-free route, Z4.3 premise table

Reviewed: `ch_P_r15.tex` lines 531–1080, `R15_pending.json`, `status.json` (unit Z4.3), `ch_P_r14.tex` §`r15:z43-premises` (lines 1511–1583, where the premise table actually lives), against the Lean source at commit `40e56bab…` (original numbering) and the dependency graph.
Nothing here claims or implies that RH is proved. The review compares an AI-written blueprint with the Lean declarations it labels.

Line references of the form `File.lean:a–b` are in original numbering; `tex N` means `ch_P_r15.tex` line N.

## 0. Summary

- **Triage (task 1).** The N labels are safe. The R label is not yet safe: 3 of the 12 supplier rows labelled R are clearly misclassified, and 2 more are R only at the head while their unproved content is deferred to inputs that no row owns. The two L rows and the six boundary R rows are correct.
- **Root cause.** A row is classified by reading its *head* declaration (often a 1–3 line wrapper), while the "Lines" column reports the *whole cone*. The 12 R heads total 215 lines; their cones total 13,893 theorem lines.
- **Hand proofs (task 2).** All six statements match Lean. All six are CONFIRMED WITH GAPS; none is NOT CONFIRMED. The gaps are inherited inputs, not errors.
- **Z4.3(i) (task 3).** The vacuum-free route is correct and proves exactly the conjunct both callers use. The cone figures reproduce (39,278 vs 50,356). Two caveats: the union is not a sub-cone of `eqP`, and one of the 26 suppliers is unnecessary.
- **Premise table (task 4).** Every number reproduces exactly. The framing of the "CM2 row service" row is misleading: that declaration is the enclosing row-level assembly, not an input of the inert calculation.

## 1. Classification audit

### 1.1 Audit table

"Head" = lines of the named declaration. "Cone" = the table's size (theorem lines outside the `D7` cone). "Excl." = theorem lines of that cone not contained in the cone of any N-classified row, so reachable only through R rows. All 30 register rows (file, lines, three sizes) agree with the graph; `D7` = 602 theorem lines reproduces.

**Supplier rows labelled R (12)**

| Row | Head | Cone | Excl. | What the Lean actually contains | Audit |
|---|---|---|---|---|---|
| `TrueTheta.exists_base` | 46 | 402 | 181 | Extension of a unitary character by divisibility of ℂˣ (Baer), plus Kronecker's theorem (integral, all conjugates of modulus 1 ⇒ root of unity) and the host fact that the CM-type product kills roots of unity | R acceptable. Standard argument, not bookkeeping; the description omits Kronecker |
| `HeckeVal.hecke_values` | 47 | 879 | 222 | Finiteness of the class group (`x^h` = principal · unit), finite order on integral units, algebraicity with all conjugates of modulus 1, p-adic unit bound | R acceptable, borderline. Textbook argument; description accurate |
| `Ker.thM_spec` | 3 | 3,001 | 2,804 | Head is ε-specification. Cone is `kThetaVector`: one-dimensionality of the standard theta space, product-theta membership, line transport by intertwiners, holomorphic fourth root, all resting on Weierstrass σ theory | **MISCLASSIFIED** (hidden N/L content) |
| `Ker.isThM_ne_zero` | 3 | 3,001 | 2,804 | Same cone as the previous row | **MISCLASSIFIED** (same content) |
| `SO.stdOK` | 2 | 3,161 | 890 (585 after `latAll`) | Head assembles seven facts. Inputs: `latAll` (confirmed in R14), plus explicit computations: quadratic multiplier is a semicharacter, standard character identity, span of `emb4`, isometry `isomOK`, two denominator bounds | R at the head only. Inputs are stated to "remain an input" and are owned by no row |
| `FourthRootStd.stdOK` | 2 | 2,853 | 0 | Verbatim copy of the previous row in another namespace | Same as above; lies inside the `algTAll` cone |
| `ThetaConj.lamConj_eq_self` | 6 | 552 | 0 | Head is ε-specification. Content (540 lines) is the classical theorem that a lattice is determined by (g₂, g₃) | **MISCLASSIFIED**: should be L with a citation |
| `ConjSeries.taylor_fnConj` | 17 | 610 | 0 | Taylor coefficients of a convergent several-variable power series are its coefficients; termwise conjugation of a finite sum | R acceptable (standard analysis) |
| `ThetaLevels.levels_closed` | 40 | 4,010 | 0 | Heisenberg commutation and level arithmetic; inputs are N rows | R correct |
| `VacuumScalar.lattice_facts` | 37 | 4,615 | 0 | Collects line, intertwiner and index facts; inputs are N rows and the theta line | R correct |
| `RelDetIdeal.detId_normOne_mul` | 11 | 548 | 540 | Head applies two lemmas. Content: local generators of relative determinant ideals, multiplicativity, norm one from dual bases (`normOne_relDet`, `relDet_mul`) | R borderline. Standard algebra, but the paragraph describes only the 11-line head |
| `relative_determinant_norm_one` | 1 | 362 | 0 | Volume-ideal sandwich argument and `unitDisc` (109 lines) | R acceptable; same remark |

**Literature boundary (8)**

| Row | Class | Audit |
|---|---|---|
| `Published.HasseNormSt` (statement) | L | Correct. Hypotheses match; see §1.3 |
| `QNorm.hasseNormSt` (proof) | L | Correct, with a note: it is fully proved in Lean; see §1.3 |
| `HasseNormSt.of_isSquare` | R | Correct. `(a,b) = ((x+1)/2, (x−1)/(2r))` checked |
| `Published.herm_col`, `det_map_cc`, `cc_ne_zero`, `exists_cc_eq_neg`, `exists_basis_one_imaginary` | R | Correct. All five are elementary (2–19 lines); they are marked `lit` only because of the directory they sit in |

**N rows spot-checked (7 of 18)**

| Row | Audit |
|---|---|
| `RepEqAt.repExS` | N correct (two integral trivialisations compared; denominator control) |
| `InertTrivial.character_trivial_at_inert` | N correct (half-idempotent argument specific to this project) |
| `CurveAlgebraic.integral_j_and_algebraic_data` | Over-classified. Content is integrality of singular moduli (`CMCurves.isIntegral_latticeJ`) and algebraicity of ℘, ℘′ at torsion points, plus bookkeeping: L + R would do. Safe direction |
| `T.exists_thetaLattice_correspondence_weilOperator` | N correct. Head is a 2-line statement wrapper around `WeilCorr.exists_corr`, and the row says so |
| `NormSum.exists_lattice_of_adelic_point` | N defensible (idele–lattice dictionary; standard, could be R with a paragraph). Safe direction |
| `theta_translation_intertwiner_unitary` | N correct (torus means, reverse intertwiner) |
| `FinWeil.Vacuum.vacuum_fixed_span` | N correct |

### 1.2 Misclassifications, with sizes

1. **`Ker.thM_spec` and `Ker.isThM_ne_zero` (3,001 lines each, one cone; 2,804 reachable only through R rows).**
   - Lean: `IsAdmissibleFlagPair…lean:75–77` and `79–81` are three lines each, applying `kThetaVector` (`:27–29`).
   - `kThetaVector` is assembled from `ThStd_proof` (`Th0CharMulOpUTh0HalfPeriodEq.lean:282–309`, cone 1,992), `product_theta_mem` (`:199–212`), `kLineTransport` (`:26`), `ThIsom_of`, and `fourth_root` (`MatrixFormFourfoldBlockFirstBlockEmb.lean:160`, via `FourthRoot_of :102–158`).
   - The largest residual theorems are analysis: `ellipticOnePole_of` (`OnePole.lean:84–217`), `even_theta_line` (`EvenThetaSecond.lean:10–89`), `th_split`, σ quasi-periodicity and convergence.
   - The table's paragraph ("apply the existence clause … the fourth-root existence theorem is an inherited input", tex 573–574) tells a reader nothing about these 2,800 lines, and no other row classifies them.
   - Correct label: N for `kThetaVector` (or L for the σ/theta-line part plus N for the fourth root), with the two heads as R wrappers of size 3.

2. **`ThetaConj.lamConj_eq_self` (552 lines, 540 in the input).**
   - Lean: `CmThetaTaylorCoeffAlgebraicAndConjugate.lean:54–59` is ε-specification plus one clause of `invariants_dictionary` (`LatticeInvariantsPeriodPairDictionary.lean:191–203`): `g2 Λ′ = g2 Λ → g3 Λ′ = g3 Λ → Λ′ = Λ`.
   - That is a published classical theorem re-proved in Lean. The row states it in one clause ("uniqueness of the lattice with these invariants", tex 590) without citation or proof.
   - Correct label: L, with a citation and a hypothesis check (nonzero discriminant).

3. **Head-only R with un-owned inputs.**
   - `SO.stdOK` (`PStdOK.lean:338–339`): after removing `latAll`, 585 theorem lines remain that only this row reaches, among them `quadMultiplierSemicharacter` (`MatrixFormFourfoldBlockFirstBlockEmb.lean:178–232`), `SC.char_eq` (`PStdChar.lean:310–352`), `SO.up`/`SO.down` (`PStdOK.lean:251–325`), `isomOK` (`IsAdmissibleFlagPair…lean:773–798`).
   - `detId_normOne_mul` (`DetIdNormOneMul.lean:156–166`): 540 lines sit in `normOne_relDet` (`:135–144`), `relDet_mul` (`:123–133`) and their local-generator lemmas.
   - These are computations a paragraph could cover, so R is defensible, but the paragraphs given describe only the heads.

### 1.3 The L items

- `HasseNormSt` (`ExistsNormTensor.lean:12`): for a number field F and δ, x ≠ 0, local representability `x = a² − δb²` at every real embedding and every finite completion implies it over F.
- This is the quadratic case of the Hasse norm theorem. The norm form of `F_v[t]/(t²−δ)` in the basis `1, t` is `a² − δb²`, so the Lean local hypotheses are exactly "x is a local norm" at finite and real places; complex places impose nothing. The comparison at tex 607–626 is right.
- Lean does not assume δ nonsquare. The proof (`HasseNormTheoremQuadraticExtension.lean:13–32`) splits on `IsSquare δ` and uses `of_isSquare` in the split case, as the text says.
- Note for the register: `QNorm.hasseNormSt` is not an assumption. It is proved in Lean through S-units, the first inequality and Kummer theory (`sUnit_mem_globalNorm_of_mem_localNorms`). The graph marks it `lit` and records no proof dependencies for it, so that proof cone is invisible to every size in this chapter. "Published theorem re-proved in Lean" is the accurate description.
- Point of use: in this cone the theorem is reached only from `Vacuum.exists_vacuum`, through `SqDet.exists_rat_sum_norm_forms_eq_one` and `LocalQuad.isotropic_of_locally_isotropic`. The chapter checks the statement, not that those two calls supply the local hypotheses. That check belongs with `exists_vacuum`.
- Citations: the Macedo–Newton paper exists under the stated title and DOI ([Cambridge Core](https://cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/explicit-methods-for-the-hasse-norm-principle-and-applications-to-an-and-sn-extensions/8BDD93B63766C00382E598622B32CFCA), [arXiv 1906.03730](https://arxiv.org/pdf/1906.03730)). I did not verify the "§1(I)" locator or the page range of Hasse 1931.

### 1.4 Estimated misclassification rate

| Measure | Rate |
|---|---|
| Supplier R rows clearly misclassified | 3 of 12 (25%); 2 distinct pieces of content |
| Supplier R rows clear or head-only with un-owned inputs | 5 of 12 (42%) |
| All R and L rows audited (20) | 3 clear (15%); 5 with head-only rows (25%) |
| All 38 classified items | 3 clear (8%); 5 with head-only rows (13%) |
| Theorem lines reachable only through R rows (4,640) that are not routine | at least 2,804; about 3,900 if the `stdOK` and `detId` inputs are counted |
| N rows sampled (7) classified too low | 0 |
| N rows sampled classified too high | 1 clear, 1 arguable |

The errors are one-directional. Nothing new was mislabelled as routine by reading it wrongly; in every case the head really is routine and the content sits one call below.

## 2. Verdicts on the hand proofs

| Item | Label | Statement vs Lean | Verdict |
|---|---|---|---|
| `FinWeil.exists_weil` | `r15:weil` | match | CONFIRMED WITH GAPS |
| `InertSign.vacuum_inert` | `r15:vacuum-inert` | match | CONFIRMED WITH GAPS |
| `VacuumExact.vacuum_exact` | `r15:vacuum-exact` | match | CONFIRMED WITH GAPS |
| `ThLoc.algTAll` | `r15:jets` | match | CONFIRMED WITH GAPS (route differs from Lean) |
| `RatEqui.isPull_row` | `r15:rational-weights` | match | CONFIRMED WITH GAPS (minor) |
| `RatEqui.isPull_col` | `r15:rational-weights` | match | CONFIRMED WITH GAPS (minor) |

All cited Lean names resolve in the graph. Labels are present and unique.

### 2.1 `exists_weil` (tex 811–898)

- Statement: Lean (`ExistsWeilOfVacuum.lean:82–83`) gives, for even N, N′, every `e0 ∈ Th(std)`, `e0 ≠ 0` and every pair of Hecke characters, a `WeilO` with `chV = χ`, `chV′ = χ′`, `ep = ep′ = 1`. The text states this, and correctly notes that evenness is unused (`exists_weil_of_vacuum :22–80`).
- The proof follows Lean step for step:
  - model, fixedness and spanning (`exists_isModel`, `vacuum_fixed_span`, `span_translates_vacuum`);
  - `normOp = λ(idx)⁻¹ · sumOp` and composition by strong induction on the index (`NormalizedHeisenbergIntertwinerComp.lean:14–45`);
  - the representation with `Om g e = normOp A (ρ g A) e` (`exists_weil_rep`);
  - the twist `c′(g′)·c(g)`, extension by zero, and the eight fields of `WeilO`.
- `GoodNorm` (`IsHeisTrivial.lean:38–41`) is as described: λ² = cardinality on residue fields, and λ = −√ on conjugation-stable primes. The construction λ(q) = √q·exp(πi/f) at non-split q gives λ(q^f) = −√(q^f) as stated.
- The twist identity was checked against `exists_split_character` (`ExistsSplitCharacterUnitaryGroup.lean:76–116`): `cut_ε(det g) · (b · σ(b)) = x` with `b = cut_{σε}(x)`, hence `c(g) = χ(x)` by the norm law.
- Gaps:
  - `Model.exists_isModel`, `Vacuum.vacuum_fixed_span` and `iop_eq_sumOp` are three N rows of the table with no proof of their own. The spanning argument (character components under A/lA) is sketched convincingly; the model and the adelic/analytic comparison are used.
  - The equal-intersection adjacent case rests on the signed Gauss factor (confirmed as R14 row 37) and on `exists_adj_selfDual_step`, which is cited, not proved.
  - "Inert" in `InertQ` means non-split. That it never means ramified here uses the host's unramifiedness (`exists_goodNorm`, last clause, `D.host.der.unramEF`); one sentence would say so.

### 2.2 `vacuum_inert` (tex 900–966)

- Statement: `odd3` (`StandardLatticesGL3.lean:515–522`). Exponent `N·lenQ(std N′, L₁′) + N′·lenQ(std N, L₁)` with `lenQ L₀ L₁ = length(L₀/(L₀∩L₁))`; the text's `nℓ(S′,L′) + mℓ(S,L)` agrees. `Even (N·N′)` is a hypothesis Lean never uses; the text carries it harmlessly.
- `InertSign.core` (`…VacuumSignInertPlaces.lean:126–236`) was compared line by line:
  - independence of the mover (`hwd`) and nonvanishing (`hne`);
  - the step `E_B = c·I_{AB}E_A`, `E_C = c·I_{AC}E_A`, `I_{BC}E_B = σE_C` (`hstep`);
  - the inertness of q by Bézout on `s` and `q` (`:209–223`);
  - induction on the length with the between-lattice identity.
- The final assembly (`:293–327`) is as described: first coordinate, intertwiner equivariance, second coordinate, then the mixed distributive triple with scalar one.
- The residue computation `1 + (Q+1)(−1) = −Q` is correct, and `−Q/√(Q²) = −1` per coordinate gives `(−1)^r`.
- Gaps:
  - `WeilTheta.om_mem_Th_moved` (an N row, 5,583 lines) supplies `W(h)v ∈ Th(Λ_L)`, which is what allows "write E_B on the line". It is used silently; the paragraph names the line, the intertwiners and equivariance only.
  - Also used without name: `kernelLattices_form_selfDual_triples` (existence of the triple constant) and `exists_traceOne_integer_conj_diff_prime_to` (`∃a, a − σa ∉ P`).
  - The triangle sign (`mu_eq_sign`), distributivity (`dist_La`, `const_eq_one`), the nearer neighbour and the transvection mover are cited inputs.

### 2.3 `vacuum_exact` (tex 968–1029)

- Statement matches `WeilOperatorVacuumExactConstantEvenRank.lean:79`: both ranks even, `x = det g·σx`, `x′ = det g′·σx′`, multiplier `chV(x′)^ep · chV′(x)^ep′`.
- `exists_scalar` (`:17–52`): the level bookkeeping in the text (level of `W(g,h)v` times the index) is what Lean does at `:37–46`.
- The scalar identity `c = c_s·c_i` was rechecked independently: with `Hv = √d_f·G`, `HG = d_f G`, `H_iG = d_iG`, `H_sG = d_sG` and `d_f = d_s d_i`, one gets `c·d_f = c_s c_i √d_f·√(d_i d_s) = c_s c_i d_f`. Correct.
- The even-rank steps are right: the inert sign is `+1` because both ranks are even (`:102`), and `χ(y) = χ(x)` needs the character's own rank even (`split_part`, `:71–77`), applied to `chV′` with N′ and to `chV` with N.
- Gaps:
  - `T.weilOperator_conj_heisenberg_moved_lattice` ("transport of rational Weyl operators") is used at `:47` and not named.
  - `VacuumScalar.lattice_facts` (an R row), `La_agree_of_trivAt` and `index_mul` are cited inputs.
  - The proof depends on `vacuum_inert` and on `character_trivial_at_inert` (an N row with no proof here).

### 2.4 `algTAll` (tex 1031–1067)

- Statement matches `Base.AlgT` (`FirstKernelLawReading.lean:452–454`) under `IsCurveIdeal`, the discriminant root and `IsChi`.
- The reduction is right: `eNat = chiFac · thMoved`, `chiFac` algebraic at an admitted pair, clear the multiple into the saturation, finish by linearity (`Definitions/GaloisGeometry/AlgTAll.lean:12–26`).
- **Route divergence, not flagged as such.** Lean's `ta_thMoved` (`VacuumEntireAndNormalizedJetsAlgebraic.lean:311–316`) gets translates of `thZero` from `AlgTranslate.coefIn_translate`, which is 10,897 of this row's 15,462 lines. The hand proof (§`r15:translated`, step 2) instead translates the four variables of the fourfold identity and reads the coefficient at `(β,β,β,β)`, which is `a_β⁴`.
  - That argument is valid, and it fixes the imprecision R14 review A found.
  - But the table row (tex 579) says "follow `ThLoc.Alg.algTAll`", and tex 1065 says the argument "uses its own four-copy theta input". A reader would conclude that the Lean declaration does not depend on `coefIn_translate`. It does.
- Gaps:
  - The whole content is in §`r15:translated`, whose step 1 (genus-one torsion translates) cites `ch_P_r8_frames.tex`, outside this review's inputs.
  - Step 2 closes with "their proof locations are recorded under the R15 supplier names". Those names are `thM_spec` and `stdOK`, R rows that in turn call the same facts "inherited inputs". This is a deferral loop: nobody owns the fourfold identity (§1.2, item 1).
- The sketch for `coefIn_translate` itself (k-linear retraction π, Taylor uniqueness) is correct and matches `exists_alg_comb` (`CoefInTranslate.lean:28–51`); that row is not among the four submitted.

### 2.5 The two covariance laws (tex 661–724)

- Statements match `OddEqOfEven.lean:126–149` and `151–174`: any `WeilO` on a vector that is only assumed to lie in `Th(std)`, with `2a_τ = ε′n_{ψ′,τ} − N′` for rows and `2a′_τ = εn_{ψ,τ} + N` for columns; conclusion `Om = ∏τ(det γ)^{−a_τ} · pull` on all of `TT`. `pull` matches the displayed `P_{γ,γ′}`.
- Exponent bookkeeping checked against Lean:
  - row: Weil multiplier `τ(u)^{−(a_τ+N′/2)}` (`char_value` with `k = a + N′/2`), pullback multiplier `τ(u)^{−N′/2}` (`pull_eq_smul_iop`), quotient `−a_τ`;
  - column: `−(a′_τ − N/2)` and `+N/2` (`pull_right_eq_det_smul`), quotient `−a′_τ`.
- `(τ(d)/|τ(d)|)² = τ(u)` for `d = u·d̄` is correct, with `d = 1+u` or `d = √(−d_host)`.
- The factorisation `γ = (zγ)(z̄·1)` matches `exists_factor`. The count of norm-one scalars via `(r+ξ)/(r−ξ)` is correct and closes R14 row 27.
- Together the two laws give every exponent in `oddEq_of_even` (`:176–180`), which closes the "narrower than Lean" remark on R14 row 28.
- Gaps (minor): the two pullback multipliers come from the phase computation of `r14:eq-rational`; spanning (`theta_span`) and extension (`om_eq_pull_of_vacuum`) are cited; both laws depend on `vacuum_exact`.

## 3. Z4.3(i): the vacuum-free route

**Does it prove the right statement?** Yes.

- The first conjunct of `eq22` (`ColumnData.lean:412–419`) is: for even N, N′, self-dual L, L′ and rational unitaries γ, γ′, `pull γ γ′ (eNat χ L L′) = eNat χ (γL) (γ′L′)`.
- `transOne` uses only this (`IntAsm.lean:55–77`: `obtain ⟨h1, -, -⟩ := hEq`), at the weak-approximation pair.
- `vac_leftE` uses only this (`ThCLeftStab.lean:368–397`: `hE.1 … 1 ⟨matOf s γ.1, …⟩`), with γ = 1 and γ′ a stabiliser.
- The route proves it for every base, every `IsChi` character and all even ranks, zero included.

**Is the argument correct?** Yes. Each step was checked.

- `exists_kappa` (`ExistsMovesOfSelfDual.lean:570–657`) is quantified over every nonzero `e0 ∈ Th(std)` and yields W with both weight conditions at `a = a′ = 0` and `W(g,h)e0 = scal κ g h · I e0`. So "use it with the chosen v" is legitimate.
- With `exists_chi`, `scal κ g h = η(detId(S,L))^{N′/2} · η(detId(S′,M))^{−N/2} = C_η(L,M)`.
- The two successive transports (first L with S′ fixed, then M) follow from `W.mul`, `W.smul` and `om_iop`, and reproduce the two intertwiners in `B.thMoved`. Hence `eNat χ (L,M) = b·(C_χ/C_η)(L,M)·E(L,M)`.
- At zero weights the two laws of §2.5 give `W(γ_A, γ′_A) = P` on `TT`; `moves_smulLat` and the group law give `P·E(L,M) = E(γL, γ′M)`.
- `chi_smulLat` gives the same factor for χ and η, so `C_χ/C_η` is invariant; `C_η ≠ 0` by `chiFac_ne_zero`. `b = 0` is allowed.

**Do the cone figures reproduce?** Yes.

| Quantity | Register | Recomputed |
|---|---|---|
| Union of the 26 suppliers, core lines | 39,278 | 39,278 (34,246 theorem lines) |
| Literature leaves of the union | 5 | 5 (the Hermitian linear-algebra ones) |
| `NatEqui.eqP`, core lines | 50,356 | 50,356 (44,844 theorem lines; 8 leaves) |
| Absent from the union: `exists_vacuum`, three CM laws, three Hasse declarations | stated | confirmed |
| 26 supplier pins (file, lines) | — | all agree with the graph |

**Caveats.**

1. **The union is not a sub-cone of `eqP`.** It contains 3,025 core lines (2,834 theorem lines) that `eqP` does not reach. The honest decomposition is 14,103 lines removed and 3,025 added, net 11,078.
   - The added lines are the `kThetaVector` chain, pulled in by `Base.thZero_ne_zero` (`IsAdmissibleFlagPair…lean:222`). They are exactly the content §1.2 finds mislabelled as R.
2. **`thZero_ne_zero` is unnecessary.** The proof needs some nonzero v in `Th(S,S′)` and `thZero ∈ Th(S,S′)`. If no nonzero v exists then `thZero = 0`, `eNat ≡ 0` by linearity of the two intertwiners, and the conjunct is trivial. With that case split the union drops to 36,253 core lines and the `kThetaVector` dependency disappears.
3. **The reduction leaves outstanding inputs.** The union still contains `exists_weil`, `vacuum_inert`, `vacuum_exact`, `character_trivial_at_inert` and `repExS`, all N rows that are unproved or proved only with gaps. The text says the remaining inputs "include" these; the status should stay `partial`.
4. `eqP` itself obtains membership from `thZero_mem` under `stdOK_of_crv` (`NormalisedFamily…lean:71–72`), so `StdOK` is common to both routes and is not a saving.

Minor: tex 649 cites `SpanRangeEmb4EqTop.lean:700–707` for `stdOK_of_crv`; the declaration is `705–707`.

## 4. Z4.3 premise table

**Numbers: accurate.** All ten supplier rows reproduce exactly in all three columns, as do the row count (ten theorems plus the hypothesis `t.Adapted`), the first-six union (47,437 core; 35,046 theorem; 26,246 outside the three cones), the bridge `isStandardBasesLatticeAtPlace_of_adapted_bases` (4,540 / 650), and both CM2 traversals (380,456 at the first literature leaf; 380,460 through the 23 leaves, the difference being the four-line `TwSys.Cheb`).

**Framing: three problems.**

1. **The "CM2 row service" row is the enclosing assembly, not a premise.**
   - `Svd.servH_row_of_artin` (`BundleBothParts…ArtinReci.lean:15–24`) proves `Row Q Lk (ServH ker)` from global Artin reciprocity and the standard tie.
   - Its cone contains the entire Z4.2.04 cone (54,386) and Z4.2.13 cone (60,733), the roots of nine of the other ten premise rows, `at_of_true_columns` (190,558) and the inert calculation `exists_beFam_evenConditionsInert_of_kerEnt` (36,055).
   - So tex 535–536, "the inert calculation uses the CM2 service", has the dependency backwards: the row service calls the inert calculation.
   - After removing the three cones, `comb_of_tied` and the other ten rows, 244,171 core lines remain. CM2 proper (`cmGoodModel_of_globalArtinReciprocity`) is 10,869 lines with 12 literature leaves.
   - "Rows overlap" is stated, but a reader will still read 380k as the cost of a CM input to Z4.3.
2. **The host row is conditional, and its conditions are not rows.**
   - `hostAt_inert` (`JacobiOfClass.lean:63–81`) takes `GenusOneModelExistsLattice`, `CurveDict` and `IntInert` as hypotheses.
   - Their suppliers are `torsionTaylorAlgebraic_latticeExists_of_cm` (55,619), `Rep.curve_dictionary` (33,771) and `intInert_of_complexMultiplication_condition` (91,446). Together with CM2 proper their union is 114,570 core lines, 88,999 outside the three cones.
   - This is the CM cost the inert application actually incurs. It is reachable only through the 380k row and is not shown.
   - `transOne`, the first call site of Z4.3(i), lies inside the `IntInert` supplier.
3. **Two rows are consumed elsewhere.** `theta_isometry_facts_hold` (SB) is not in the row-service cone at all; its only caller is `Pk.sum_over_primes_service` (`SumOverPrimesHypotheses.lean:187–221`). The text says so for SB and orbit parity, but the table presents all eleven as premises of one application.

Also: `atLin_adaptedCoef_eq_standardSeries`, used in the inert calculation at `AdmissibleKernelSeries…lean:62`, is not named; its cone is covered by the listed rows, so no size changes. And tex 534 refers to `r15:z43-premises`, which is defined in `ch_P_r14.tex:1512`, not in the chapter that cites it.

## 5. Other findings

- **5,355 not reproduced.** Tex 558 says releasing the three operator cones "at their place in the R14 ordered partition" adds 5,355 theorem lines. The unordered measure (lines of the `base_data` cone reachable only through the three operator rows) is 5,132. The register does not record the ordering, so the figure cannot be checked from R15 inputs alone; it was attested by R14 review A.
- **Duplicated mathematics is classified more than once.** `SO.stdOK` / `FourthRootStd.stdOK`, `Ker.kThetaVector` / `Ker.Cd.kThetaVector`, and `detId_normOne_mul` / `relative_determinant_norm_one` are copies or two proofs of one fact. Row counts and "exclusive" sizes depend on which copy a caller happens to use.
- **Pointer ranges narrower than the declaration** (low priority): `theta_span` 143–176 (declaration 143–195), `om_eq_pull_of_vacuum` 207–227 (207–250), `sumOp_comp_of_adj_of_inf_eq` 22–57 (22–192), `lattice_of_curve` 136–147 (136–157).
- **Coverage.** All 30 rows lie in the `base_data` cone; 4,361 theorem lines of that cone outside `D7` are reached by none of them. I assume these are the parts confirmed in R14; the chapter should say so.

## 6. Prioritised fixes

1. **Reclassify `kThetaVector`.** Give it its own row as N (or L for the σ/theta-line part plus N for the fourth root), reduce `thM_spec` and `isThM_ne_zero` to 3-line R wrappers, and write or cross-reference the proof. This also breaks the deferral loop from `algTAll`.
2. **Reclassify `lamConj_eq_self` as L**, cite the theorem that (g₂, g₃) determine the lattice, and check the nonzero-discriminant hypothesis at the call (`ExistsMovesOfSelfDual.lean:482–485`).
3. **Give `stdOK` and `detId_normOne_mul` real paragraphs** covering their inputs (semicharacter identity, `emb4` span, isometry, denominators; local generators and dual bases), or split those inputs into rows.
4. **Change the size column for R rows** to head lines plus exclusive residual. Keep the inclusive cone only as a secondary figure.
5. **Flag the `algTAll` route as a hand substitution** that bypasses `coefIn_translate` (10,897 lines), in the same terms used for Z4.3(i), and correct the table row.
6. **Z4.3(i):** add the trivial-case split, drop `thZero_ne_zero` from the supplier list (39,278 → 36,253), and state the reduction as 14,103 removed, 3,025 added.
7. **Premise table:** replace the CM2 row by the CM inputs the application uses (CM2 proper; genus-one lattice; curve dictionary; `IntInert`), or relabel it "enclosing row assembly". Correct tex 535–536.
8. **Name the silent inputs** in §2: `om_mem_Th_moved` in `vacuum_inert`; `weilOperator_conj_heisenberg_moved_lattice` in `vacuum_exact`.
9. Record the R14 ordering behind 5,355, or replace it by the unordered 5,132.
10. Optionally downgrade `integral_j_and_algebraic_data` to L + R, which saves a hand proof of 2,225 lines.

## 7. Is the triage reliable enough to scale?

**Not yet for R; yes for N and L, with one mechanical change.**

- The N direction is safe: no sampled N row was under-classified, and the only errors found there cost effort, not correctness.
- L was applied carefully, with a real hypothesis comparison, and the six elementary declarations in the literature directory were correctly not promoted to L.
- R failed in one specific, repeatable way: the head was read, the cone was counted. This codebase is built from thin `…Statement` wrappers and one-line specialisations over large cones, so the failure will recur at the same rate or higher across the remaining ~2.1M lines. In three of the twelve supplier R rows, involving at least 2,804 R-only index lines in this pilot, "trusted to the kernel with a paragraph" would silently absorb most of the mathematics that a reader needs explained.

Guardrails, in order of value:

1. **Classify closed cuts, not heads.** A row may be R only if every theorem line in its exclusive residual (its cone minus the cones of all other L/N/R rows) is routine. Otherwise split it into a head row and named input rows. This is a graph computation and can gate the register automatically.
2. **No un-owned inputs and no deferral loops.** Every phrase "inherited input" must resolve to a row with a class and a proof label. Check mechanically that the deferral graph is acyclic and ends in a citation (L), a hand proof (N) or an R leaf with a small residual.
3. **Automatic escalation of R rows.** Flag for a human-style read any R row whose exclusive residual exceeds about 300 theorem lines, contains a single theorem over about 40 lines, or involves analysis (`tsum`, `HasSum`, `Differentiable`, measure) or an ε-choice whose existence clause is proved elsewhere.
4. **Report head and residual sizes** for every R row, so the paragraph is visibly proportionate to what it covers.
5. **Add a class for standard arguments** (or widen L to "classical theory re-proved in Lean"). `hecke_values`, `exists_base`, the determinant-ideal lemmas, the (g₂, g₃) theorem, σ-function theory and singular moduli fit neither "published theorem with matching hypotheses" nor "bookkeeping". They need a reference and a three-line sketch, not a full hand proof.
6. **Deduplicate before classifying**, so one piece of mathematics gets one class.
7. **Record hand-route substitutions in the register**, with the bypassed Lean suppliers and their sizes.
8. **Check L at the point of use**, not only at the statement, and note when a `lit` node carries a Lean proof the graph hides.
9. **Sample-audit every round.** Have an independent reviewer read the Lean for a fixed fraction of R rows (20% is enough to detect a 25% error rate quickly); if more than about 5% are clearly wrong, re-audit the round.

With guardrails 1–4 in place the triage becomes a sound way to spend hand-proof effort on the N rows. Without them, the R count overstates progress.
