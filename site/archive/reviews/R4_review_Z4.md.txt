AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

# R4_review_Z4

AI review report produced during this project; file names are internal working names.

- Internal source file: `out/R4_review_Z4.md`
- SHA-256: `e3e5f72145063e2f4e3021703997dcdfa83db51095279b592b6717e9d6dd7806`
- Report scope: Round-4 independent review: Z4.3 and Z4.1 (Chapter P, blueprint v6)

## Archived report · [English summary](../../reviews/R4_review_Z4.md)

The report below preserves its original verdict, scope and unresolved points. Historical review-machine home prefixes are displayed as `${REVIEW_HOME}`; the source checksum above identifies the original report. Source line numbers in other records count from its original title.

# Round-4 independent review: Z4.3 and Z4.1 (Chapter P, blueprint v6)

Reviewed text: `${REVIEW_HOME}/work/prev4/ch_P.tex`

- Z4.1: lines 3910–4472 (`sec:P-r4-z41`, `sec:P-r4-z41-kernel`), with its statement and bridge in lines 3801–3908 and its consumer, Proposition `prop:P4-columns` / Lemma `lem:P4-select`, lines 3196–3477.
- Z4.3: lines 4535–7402, with the reduction paragraphs at 4510–4533 and 3604–3660.

Checked against the cleaned Lean copy `${REVIEW_HOME}/src/rh/src/` and the dependency graph (`graphq.py`, plus a transitive-cone script in `${REVIEW_TMP}/z4scratch`). Cone sizes below count core lines reachable from a declaration; every cone contains a shared base of roughly 1,900 declarations / 4,200 lines of data definitions, so small cones are mostly that base.

How far the checking went: Z4.1 was read in full and its arguments re-derived by hand. Z4.3 was read in full, but it compresses cones of 10k–60k Lean lines into a page each, so only the paragraphs named in the Z4.3 findings were re-derived; the rest was checked for statement match, existence of the cited declarations, and labels.

| Sub-input | Verdict |
|---|---|
| Z4.3 | **NOT COMPLETE** (as labelled). The local analytic estimates are reconstructed and the sampled ones are correct, but several steps on the direct path to the premises of `first_clause_cases` are neither written out nor labelled. |
| Z4.1 | **COMPLETE WITH GAPS**. The three entry estimates, the kernel normal form, the expansions and the Hecke integrality are written out and correct; the bridge from the entry estimates to the three place bounds is asserted without proof or label. |

---

## Z4.3 — Off-level bounds on the actual kernel

### Verdict: NOT COMPLETE

The notes say "complete, under the common arithmetic/geometric premises of the standard tie". That would be acceptable if every premise carried a label and everything else were proved. It is not: three groups of steps (items 1.1–1.3 below) sit on the direct path and have neither a proof nor a label. One of them (the odd-order inert class) is an analytic estimate, not bookkeeping.

### 1. Is "complete" earned? Steps asserted without proof or label

**1.1 The numerical "Core" between the letter bounds and the four premises is named but not derived.**
In Lean the four premises of `first_clause_cases` come from `OrbitPlaces.lift_bounds_of_essential`, fed by `DIV.Lemmas.OrbitEntryBounds.orbit_entry_bounds_hold` (`ChainOperators/OrbitEntryBounds.lean:49–52`; called at `SumOverPrimesHypotheses.lean:225–226`). That theorem supplies the eight components of `OrbitPlaces.Core`. The text never names `orbit_entry_bounds_hold`, `lift_bounds_of_essential` or any of the `PI.*` suppliers. What it does with each component:

| Core component | Lean supplier | Treatment in the text |
|---|---|---|
| `OrbitValuationBound` (exponent `g0Pl + FOrb − errF`) | `PI.OrbBoundF` | Line 4666–4667 quotes the exponent. No derivation from the split corollary. |
| `ValuationSumBound` | `PI.SumOrbC` | Line 4656: "The valuation-sum inequality bounds…". No derivation. |
| `ScaledGeneratorsInSup` (both clauses) | `UpperTheory.kvalGe_theta_of_shape`, `fInert_sub_eatI_le_orbit_average_sub_errors` | Line 4662–4664: one sentence. See 1.2. |
| `OrbitsAddLowerBound`, `OrbitsAddAtConjugate`, `OrbitRestriction`, `OrbitRestrictionAtConjugate` | `PI.OrbAddUp`, `OrbAddOne`, `OrbRestr`, `OrbRestrOne` | "The orbit-addition inequality adds these exponents"; "Add over the f positions". Not proved. |
| `OrbitSumBound` | `OrbitPlaces.sumI` | Cited by name. Not proved. |
| `EntriesAtDiscriminant` | `jet_bound_ramified_prime` | Item 2 of the enumerate (4624–4649) gives a real argument. |

The first row is the step where the constants (11, 1) actually enter the error terms. Lean needs `CLarge 11 1` with `ce.c6 = 12`, `ce.dig = 3`, `K.dl1 = 5` (`cLarge_of_fixed`, cleaned `OrbitPlaces.lean:266`). The text never says how 11 and 1 are absorbed into `errF`, `E_atI`, `E_atC`. The quantities `F_inert`, `F_orb`, `errF`, `E_atI`, `E_atC`, `lowCs`, `g0^Pl` are also not defined in the subsection.

**1.2 The odd-order inert class C_s has no estimate.**
For `IsCs` the Lean bound is `KvalGe … (lowCs L (i+1) p)` for every series with the all-real product form, where

`lowCs = (Σ FOrb)/nP − (k−1)(Σ w)/p³ − 8(Σ w)/p − 3 f Nm² log_p a`.

This is `UpperTheory.kvalGe_theta_of_shape` (`KvalGeThetaOfShape.lean:155–204`, cone 8,196 lines). The text's only statement is "The former uses the all-real expansion and a lower bound lowCs ≥ F_inert − E_atI; here g0^S = 0" (4662–4664). Paragraph `par:r4-z43-odd` (5887–6004) proves the factorization for odd h. It does not prove any valuation bound for the factored series. One sub-branch of the fourth estimate is therefore missing.

**1.3 The properties the tie supplies to `kform_of_ker` are used but not proved and not labelled.**
Line 4551–4554 and 4596–4599 say the tied datum "gives" the unit, the rational class-pair maps, `F_i`-preservation and the level-zero stabilizers. In `at_of_true_columns` (`AtOfTrueColumns.lean:30–47`) these are separate theorems, none of which appears anywhere in `ch_P.tex`:

| Property | Lean supplier | Cone (core lines) |
|---|---|---|
| `UnUnit` | `T.kernelPairScalars_isUnit_trueColumns` | 18,953 |
| `KmapRat` | `PdvKm.kmapRat_kerEntC'` | 11,626 |
| `KFi` | `T.kernelClassSums_carry_chainComplexForms` | 76,105, with 8 published-theorem inputs |
| `Stab0` | `T.stab0_rec7_of_levelData` | 16,041 |
| `Duty` | `T.conditions_at_standardKernelComparison_trueColumns` | 42,176 |
| `t.Hyp` | `T.kernelEntries_hyp_of_columnSideProperties` | 14,039 |

The notes (Z4.3 bullet "실제 사용 위치") treat these as hypotheses with a supply site. The text has neither a "Hypothesis, discharged at `at_of_true_columns`" tag nor a "Proved in Lean, not reproduced" tag for them.

Two further inputs used at `SumOverPrimesHypotheses.lean:214–216` are not mentioned at all:
- `OrbitPlaces.SB`, from `DIV.Lemmas.theta_isometry_facts_hold` (cone 6,647 lines);
- `OrbitParityCond`, from `DIV.Inh.orbit_admissible_of_split_bound` (cone 3,910 lines).

**1.4 Published theorems in the supply cone are not named.**
The cone of `at_of_true_columns` is 190,558 core lines and reaches these `lit` declarations: `Published.HasseNormSt` / `QNorm.hasseNormSt` (Hasse norm theorem for a quadratic extension), `exists_basis_one_imaginary`, `det_map_cc`, `herm_col`, `cc_ne_zero`, `exists_cc_eq_neg`. They enter through the `KFi` supplier. The Z4.3 text does not mention them. The label at 5573 covers CM2 only; its supplier additionally rests on `Published.GlobalArtinReciprocity`, `Published.cheb_holds` (Chebotarev, degree one) and the `IsGoodCMCurve` premises, which the label does not state.

**1.5 What is written out and checks.** I re-derived these and found them correct:
- Constant 11 (4811–4875): strong duality, complementary slackness on H = {σ_s ≥ 2/p}, the incoming-flow bound Σ_H w ≤ Σ w / p, the losses 8/p and 2γ ≤ 3/p.
- Digit-loss constant 1 (4877–4927): 1/(p−1) − R = ρ with R = ρ + 1/(p+1).
- The exceptional coefficient bound `lemmaS` (4930–5001): weight quantization in (p−1)⁻¹ℤ, the binomial extraction, the exact loss of 1.
- The general even-orbit frame bound (5050–5198): all three pair types are paid by the chosen radii; the top-row optimisation with q and u_s = p^(−q) gives ≤ γA_s − topTerm_s.
- The dyadic model (5231–5313): I checked (D′+16D)³ = 1728 g₂³ D′D symbolically from the stated g₂′, g₃′, and Δ = a³ − 27, c₄ = a(a³ − 24) for y² + axy + y = x³.
- The first-level coboundary (5585–5713) and the cube identity.
- The low jets (6134–6159): J₁, J₂ and the integral expression for a(a−b)J₂ are algebraically correct.
- The reference scalar (6798–6851): |M| = I|D|², D̄ = (−1)^dim det(u) D, hence c₀⁸ = det(u)⁴.
- The Hurwitz-integrality zero bound (7241–7317) and the word comparison (7352–7383): losses 2Λ and 3Λ digits give 5hM²Λ + 4|T|Λ².

### 2. Statements against Lean

No mismatch found in the declarations I compared:
- `first_clause_cases` (`StatementsOfRemainingBound.lean:25–95`): four hypotheses `OrbitsWithoutOperator`, `MediumInertPrimeLengthBound`, `LossAtDiscriminant`, `DGamDef → RestElse`; the case split in the text (4524–4533, 3636–3653) matches, including discarding the nonnegative Σ g0S.
- `local_bound_eleven_comparison` and `lpF` (`DataParams₂.lean:55–63`): k ≥ 3, w > 0, 0 ≤ E ≤ 4w, D = (k−1)w + E − 2w·1_T.
- `LemmaS`, `BHyp`, `IsBiPower`, `torus` (`GaussJetBounds/Statement.lean`): weight ρ, thresholds 1/(p−1) and 1/(p−1) − 1, torus exponent (−l)^s.
- `ThmAGauss` (`StatementP.lean:33`): ε = ±1, 1 ≤ a, size ≤ a, 2 log_l a + 2 ≤ N₀ − 1, exponent Σ_T(topTerm − γ·Wcap) + Fnum(Dl) − d N₀ N₁ (log_l a + 1). `topTerm` agrees with the text's H_j description.
- `orbit_bound_rec` (`OrbitBoundStandardSeriesInertPlaces.lean:22–42`): row gap ≤ 2a, 5 ≤ dl1, 4 ≤ dl2, sign −1, conclusion max(g0, 0).
- `at_of_true_columns`, `at_of_stdTie`: the hypothesis list at 4688–4693 matches.

All cited Lean names I looked up exist with the cited line ranges. The cleaned copy of `OrbitPlaces.lean` is shifted by about 175 lines relative to the citations, which follow the original numbering used by the graph.

### 3. Proofs

No mathematical error found in the paragraphs listed in 1.5. Defects that are not errors of substance:
- **Broken LaTeX at 4978–4979 and 5183–5184.** `{\rm even}` and `{\rm marked}` have become `{` + newline + `m even}` / `m marked}`. Both displayed formulas are damaged.
- Line 4913 says "a+b odd" for the one-letter exceptional pair without saying why (it follows from s even, s′ odd, s + a ≡ s′ + b′ mod even h).
- Line 7354 asserts Λ = log_p(2a) ≥ 1 without citing `Shape.xa` (p ≤ X″ ≤ a).
- Item 1 of the enumerate (4605–4623), items 3–4 (4650–4676), "Reduction of translates to one copy" (5470–5530) and "the theta space is a line" (6775–6796) are outlines. I could not confirm them step by step; they read as correct summaries of the cited declarations.

### 4. Labels

- `[Hypothesis, discharged at servH_row_of_artin]` (5573): **confirmed.** `GlobalTheory.Svd.servH_row_of_artin` (`BundleBothPartsOfStandardKernelOfGlobalArtinReci.lean:15–24`) obtains CM2 from `cmGoodModel_of_globalArtinReciprocity` and passes it on. It is on the path from `allChi`.
- **CM3, CM4, `AlgTAll`: used, discharged in Lean, but not labelled.** Inside `torsionTaylorAlgebraic_latticeExists_of_cm` (`TorsionTaylorAlgebraicLatticeExistsOfCm.lean:15–19`) they come from `ReciprocityTheory.ChartRestriction.L1.cmIntegralityThree` (`FgStatus.lean:5`, cone 20,848), `L1.cm4` (`TorStatus.lean:38`, cone 6,955) and `GlobalTheory.ThLoc.algTAll` (`AlgTAll.lean:6`, cone 20,296). The text says only "the available CM3 and CM4" (5575) and "the algebraicity … from `AlgTAll`" (5390).
- The paragraph at 3604–3610 (`[Hypothesis, discharged at statements_of_remaining_bound and … sum_over_primes_service]`): **confirmed** via `four_orbit_conditions_of_proof` (`GandSab.lean:11`) and the call at `SumOverPrimesHypotheses.lean:225`.
- `StdTie`, `Shape`, the row gap, `3 ≤ splitBound`, `5 ≤ dl1`, `4 ≤ dl2`: listed at 4688–4693 as hypotheses of `at_of_true_columns`, with no statement of where each is discharged. Only `three_le_split` and `cLarge_of_fixed` are visible in `sum_over_primes_service`.

### 5. Understanding

The text does explain why the bound holds. One tied kernel is expanded at every off-level place as an integral factor times an exponential of a biadditive curve term. Away from d the factor has integral jets because prime-to-p translates of the normalized theta are integral in the good formal parameter. At d a single quadratic term with |S| ≤ √p accounts for the loss. At inert and signal places the exponential is controlled by a coefficient test whose only exceptions are pairs of p-powers; these are paid for by a flow problem whose dual gives F(D), with constant 11 after comparison with the reference capacities. The explanations of the constant 11, the exceptional bipowers and the top-row optimisation are clear. What is weak is the last mile: how those letter bounds become the numbers `F − E_atC`, `F − E_atI`, `g0S` that `first_clause_cases` consumes is stated by name only, and a reader cannot reconstruct it from the text.

### Most important problems (Z4.3)

1. The numerical Core is not derived: `PI.OrbBoundF` (11, 1 → `g0Pl + FOrb − errF`), `PI.SumOrbC`, `sumI`, the orbit addition/restriction statements, and the second clause of `ScaledGeneratorsInSup`. The supplier `orbit_entry_bounds_hold` is never named.
2. No valuation estimate for the odd-order inert class C_s (`kvalGe_theta_of_shape`, bound `lowCs`).
3. `UnUnit`, `KmapRat`, `KFi`, `Stab0`, `Duty`, `t.Hyp`, `SB`, `OrbitParityCond` are used with neither proof nor label; the `KFi` cone alone is 76,105 lines and uses the Hasse norm theorem.
4. CM3, CM4 and `AlgTAll` lack "discharged at" labels although Lean discharges them; the published inputs behind CM2 (Artin reciprocity, Chebotarev) are not stated at the label.
5. Two displayed formulas are corrupted (lines 4978–4979, 5183–5184).

---

## Z4.1 — Integral jet estimates and normalized action

### Verdict: COMPLETE WITH GAPS

### 1. Is "complete" earned?

**Written out and correct** (re-derived by hand):
- The three entry inequalities `EntryExcessBound`, `EntryCappedBound`, `EntryB` (3926–4057): the four term types A_φ, B_k, Z, pY₀; the factorial bound (*); the three charging arguments.
- The one-place and all-place expansions (4059–4176).
- Integrality of the normalized Hecke operator (4178–4225); the numerical step agrees with `Ar_lift_le` (even part exact, odd part ≤ i·w(j+1, s)).
- The product entry and the single loss d_j (4227–4280).
- The classification of the biadditive kernel (4288–4471). Its six steps correspond one-to-one to `StepZero`, `StepI`, `StepII`, `StepH`, `StepIII`, `StepIV` in `BetaIsG_of` (`NormLiftLeOne.lean:32–60`).

**Asserted without proof or label — the bridge from the entry estimates to the place bounds** (3838–3890, and "The Gauss descent and removal of ρd above now transfer all three estimates to the place", 4056–4057). `first_theorem_place_bound`, `second_lemma_place_bound` and `hecke_place_bound` (`FirstTheoremPlaceBound.lean:20–30`) are obtained through `ea_A1U`, `ea_A2U`, `ea_BU`, which need:

| Step | Lean | Treatment in the text |
|---|---|---|
| Generic-frame reduction to `EntryHyp` data with `alN e = alG`, `capN = capG`, `lsN = lsG` | `EGaussK.reduce` (`EGaussK.lean:38`, cone 554 lines) | One sentence: "Reduction then gives an entry pairing z with data satisfying EntryHyp and matching degree, capacity and loss parameters." How minors of height one at tops become the top linear forms is not shown here (it is described only in Z4.3, 7203–7208). |
| b_J ≤ E_i for J = [0, i) | last clause of `EGaussK.reduce` | "the reduction gives b_J ≤ E_i" (3874–3875), no argument. The claim is true: I checked it block by block. |
| Identification of the system gains `g0v`, `gv`, `alEven` with `excessGain`, `gainG` at these data | `ea_brNum` (`GainOfCapacityLoss.lean:254`, cone 603) | Not addressed; "These steps explain the bounds g_A, g_B − alEven, and g_B". |
| Class under scaling | `ea_brClass` (`EaDegreeMapDomain.lean:167`, cone 372) | Not addressed. |
| Norm on the extension containing ϖ | `nm_restNorm_of_place` (`NmRestNormOfPlace.lean:25`, cone 684) | Not addressed. |
| Passage from norms in K′ to `LowAt` with the quantifier over U | `ea_lowN` (`EaGeCOfNorm.lean:93`) | Not addressed. |

Removing ρd by undoing X ↦ ϖX (`EGaussK.descend`) is explained (3876–3878).

**Labelled, outside Z4.1 proper.** Proposition `prop:P4-columns` keeps "[Proved in Lean, not reproduced: the full `FormalGroupSystem.Stmt` …]" and a status line that is still conditional on v(c_l) ≥ 0, v(c_r) ≥ a_v^ev, the neighbour count and the convolution inversion (`vGeK_cl`, `Cii`, `CountLoc`, `heckeCondition_of_adm`). Z4.1 does not supply those. This is consistent with the notes, which scope Z4.1 to the three place bounds, the expansions and the Hecke action, but "complete" for Z4.1 does not make that proposition unconditional.

### 2. Statements against Lean

No mismatch found.
- `EntryHyp` and the three `Entry*` definitions (`StatementE.lean:170–219`): p > 2, ‖p‖ = p⁻¹, integral u, ξ, T, e = 0 off TT, `InClass`; exponents G_A + ρd, G_B − Σ_{TT∖oddT} α + ρd, and G_B + ρd with the stated b_J.
- `deLoss` (`StatementAB.lean:77–78`) equals Δ; the hypotheses of `ExcessGainBound` and `BCore` (`ABArith`) are the ones the text derives.
- `RestBeta` (`DworkExponentialRestrictions.lean:15–17`), `BeProp` (`FormalGroupSystem.lean:147–158`), `Gser` (`OddLogRelation.lean:28`): c ∈ W with σ²c = c and exp(inParam β − (cA(X,Y) − σ(c)A(Y,X))) integral. `RestBeta` takes `DworkLemma p` as a hypothesis; that is clause `adm1` of `admitted`, and the text proves the lemma anyway (4330–4346).
- `RestGc`: p ≥ 5, n′ ≥ 2 even, ϖ^(p²−1) = p, μ inverse to λ_F.
- `admitted` (`FormalGroupSystem.lean:771–773`) has exactly thirteen conjuncts, as the notes say.

### 3. Proofs

No error found. Points I verified:
- (*) follows from 1/(p−1) = γ + ρ and i₂ ≤ Σ L_s / p ≤ γ Σ L_s.
- The charge orientation gives δ ≤ max exponent index, so each charge consumes at least p^δ letters; Σ_f p^(−(2f+1)) = γ.
- hhS: the dual-basis contraction yields u_s = c for s odd and −σc for s even.
- The excess (p−2)(q−1) at (i, j) = (0, 1) and the two increments.
- Kernel classification: the Frobenius-correction identity; the slice argument (b′_{pq^k} = 0, then a_j = 0, then b_j = 0, using 1 ≢ p mod p²−1); c + σ(c′) = 0 and c′ + σ(c) = 0 give σ²c = c; DA_c = σ(c)U(X)L(Y) − cL(X)U(Y) by direct coefficient comparison.

Two terse places: the definition of the normalizing exponent N′ is not displayed in the Hecke paragraph, and the sentence at 4019–4022 defining the cyclic distance is hard to parse (it means the least positive residue of the difference of the two exponent indices).

### 4. Labels

Z4.1 itself carries no "Hypothesis, discharged at" tag; its status line (4282–4285) defers admission on the chain to Z4.2. The notes' supply claims check out:
- `admissible_at_each_site` and `site_cmpLite_siteAdm` (`JointSiteChainComparedCarriesAdmittedSystem.lean:29, 77–89`) depend on `FormalGroupSystem.admitted` and are on the path from `allChi` through `modelsOK_of_joints`.
- `rests` (`PrvAndKernelCommutationUpToUnitsOfRests.lean:97–102`) takes `admitted` and calls the three place bounds, `theta_kernel_expansion`, `expansions_multiply`, `restEnt_of`.
- `stmt_proved` has a single caller, `sum_over_primes_service`.

### 5. Understanding

The text explains the result. After the substitution that splits top and low variables, the scaled kernel is a series in h/p whose terms are of four kinds. Each power of 1/p must be bought with factorials of the consumed letters, at the rate γ per top letter and ρ per degree. Paired terms and mixed terms are then charged against top letters or against the number of minors a rank-one direction can hit, which is exactly what distinguishes the excess gain, the capped gain and the weighted Hecke version. The kernel classification is a self-contained proof that additivity up to integral exponentials, plus the Teichmüller conjugacy, forces the normal form cA(X,Y) − σ(c)A(Y,X) with σ²c = c. The weak spot for a reader is the same as the gap above: how the Weyl-type frame polynomial of an actual system becomes the pair (e, minors) to which the entry estimates apply.

### Most important problems (Z4.1)

1. The bridge from `EntryExcessBound` / `EntryCappedBound` / `EntryB` to the three place bounds is asserted: `EGaussK.reduce` (including b_J ≤ E_i), `ea_brNum`, `ea_brClass`, `nm_restNorm_of_place`, `ea_lowN`. It needs either a written argument or a "Proved in Lean, not reproduced" tag.
2. Proposition `prop:P4-columns` remains conditional on items Z4.1 does not cover (`vGeK_cl`, `Cii`, `CountLoc`, convolution inversion). The label there is honest, but the Z4.1 "complete" should not be read as closing that proposition.
3. Minor presentation: N′ undefined in the Hecke paragraph; the cyclic-distance sentence at 4019–4022.

---

## References checked

- Milne, *Modular Functions and Modular Forms*, Corollary 12.16, p. 120: fetched; it states that j(z) is an algebraic integer when ℚ[z] is imaginary quadratic. Matches the use at 5278–5282.
- Deloup, Trans. AMS 351 (1999), p. 1896, equation (1) and Lemma 1.1: fetched (the URL redirects to `webhomes.maths.ed.ac.uk`); the normalized Gauss sum is 0 or an eighth root of unity, with the vanishing criterion. Matches the use at 6815–6821.
- DLMF 23.10.3: fetched; it is the sigma addition formula used at 5635–5654. DLMF 23.3(i) was not re-fetched.

Nothing in this review claims that the Riemann hypothesis is proved; the review concerns only whether two sub-inputs of the blueprint are reconstructed as labelled.
