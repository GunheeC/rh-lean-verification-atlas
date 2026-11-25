AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

# R17_review

AI review report produced during this project; file names are internal working names.

- Internal source file: `out/R17_review.md`
- SHA-256: `288b9592687eb74b507031c5d8740bc11b9f8487be45d09c113a754d6546a6bc`
- Report scope: R17 independent review: E1–E7 recheck, tier audit, and the unclassified material

## Internal report

The report below preserves its original verdict, scope and unresolved points. Superseded graph percentages have been removed from this public edition. Source line numbers in other records count from its original title.

# R17 independent review: E1–E7 recheck, tier audit, and the unclassified material

Reviewer: independent AI pass, 2026-11-24. Source pin `40e56bab026552e089d7afcfeff08d2defb9c005`, original line numbering throughout. No Lean build was run and nothing here is a human sign-off. Nothing in this review, or in the material reviewed, establishes RH or GRH; the subject is the internal structure of a Lean development and a blueprint that describes it.

## 0. Verdict

- **Z4.2.04:** E1–E6 are fixed in the two chapter files. E7 is fixed in `status.json`; the register `R16_pending.json` was not in the package, and the only copy I could reach is still the pre-edit one. I **confirm** the unconditional completion on review A's own condition (E1–E4), with the register left as an open bookkeeping item.
- **Counts:** I rebuilt the cones from the graph without the author's reader. Every headline total reproduces exactly: 1,604,500 / 758,973 / 780,265 / 7,007 / 726,539, and D = 23,230.
- **Classified tiers:** no block is graded too low. The only errors I found are A blocks that would pass as S (3 of 16). About 40% of A blocks (28 of 71) cite a chapter or section where a statement is needed.
- **Unclassified material.** From a seeded, line-weighted sample of 66 declarations, the reviewer judged most sampled items routine or standard. One N candidate and four borderline A items were identified at statement level.
- **Limits of that estimate:** n = 66, one reader, statement plus skim. The N estimate is especially sensitive to how four borderline items are classified. Novelty that lives in short top-level statements or in the overall architecture is invisible to a line-weighted sample.
- **Package gap:** `R17_triage.json` lists 11 of the 40,612 U blocks. The block ledger, owner table, tools zip and Z4.2.13 comparison that the report links to were not delivered, so the claimed byte-identical rerun could not be checked and U blocks could not be sampled as blocks.

## 1. E1–E7 recheck

| Edit | Status | Evidence |
|---|---|---|
| E1 | FIXED | `ch_P_r16.tex:442–449` registers `GlobalTheory.Mem.Col2.ThetaVec.thetaVector` (`PeriodLatticeSesquilinearFormIsHerm.lean:437–498`) as the second implementation and states that `Ker.Cd.kThetaVector` is outside the Pair cone. `ch_P_r15.tex:712–720` carries the new figures. Graph check: the head is at 437–498 and in the Pair cone; `Ker.Cd.kThetaVector` is not in it. |
| E2 | FIXED | `ch_P_r15.tex:434–441` and `:598` cite `WeilVac.thMM_spec` (`ExistsWeilOThZeroTriv.lean:33–36`) for the four-copy identity and route `Base.thMM_spec` / `Ker.kThetaVector` through the entireness clause. Same at `ch_P_r16.tex:459–463`. Graph: `WeilVac.thMM_spec` is at 33–36. |
| E3 | FIXED | `ch_P_r15.tex:449–466`: `vector_bound_link` 270 / 247, `theta_line` 2,046 / 2,015, and `Base.latAll` for integrality on the standard lattice. The file cites `latAll` at 623–644 (and 623–634 at `:621`), which is correct in original numbering. Review A's "583–585" does not point at `latAll` in the pinned file. |
| E4 | FIXED | `ch_P_r15.tex:469–478` identifies the ε-chosen `TaylorLogMetric.sgStar` with σ·exp(−s₂z²/2), with uniqueness by the one-pole argument. `ch_P_r16.tex:298–305` maps `wSigma`, `wZeta`, `wEta`, `s2` to the DLMF objects under Lean's `z/0 = 0` convention. |
| E5 | FIXED | `ch_P_r16.tex:364–367`: integrality of E on each self-dual lattice is stated before `D_xD_y = D_{x+y}`. |
| E6 | FIXED, one nit | Ranges now match the graph: `FourthRootStd.stdOK` 700–701 (`ch_P_r16.tex:18, 258`), `FL.lam_mem` 528–540 (`:36`), `StdData` 52–64 (`:41`), `quadMultiplierRules` 234–242 (`:142`). `MF110.pdf` no longer appears. A number-field reference is added at `ch_P_r16.tex:113–115` (Milne ANT v3.01, Prop. 2.26; I fetched it and the statement is the discriminant identity). The `chiFac` sentence points to §r8:Z4.2.04 (`ch_P_r15.tex:633–636`). Nit: Milne's ANT is cited as `ANT301.pdf` in r16 and as the unversioned `ANT.pdf` at `ch_P_r15.tex:101`. |
| E7 | PARTLY VERIFIED | `status.json`: Z4.2.04 is `complete`, `remaining_input` is empty, `basis` is replaced, `completion_review.status` is `reviewed`, and `round17.chapters_after_edits` hashes equal the SHA-256 of the two tex files I was given. **Not verified:** `R16_pending.json` is absent from `prev17/`. The copy under `out/` (older timestamp than the R17 files) still has all 15 rows at `pending_review`, still lists `Cd.kThetaVector`, and has no `ThetaVec.thetaVector`. |

Recomputed from the graph, cutting at literature leaves and removing the cones of Z4.2.01, .03 and .05:

| Quantity | Report | Mine |
|---|---:|---:|
| Pair cone, core / theorem lines | 54,386 / 42,543 | 54,386 / 42,543 |
| Pair residual | 24,978 / 23,600 | 24,978 / 23,600 |
| Union below the four implementation heads | 8,373 / 7,887 | 8,373 / 7,887 |
| With the two selection wrappers | 8,379 / 7,893 | 8,379 / 7,893 |
| Reachable only through the five cut heads | 3,654 / 3,477 | 3,654 / 3,477 |
| Old three-head union (theorem lines) | 6,539 | 6,539 |

**Decision.** Review A made the grade change conditional on E1–E4. Those are in the text, at the right Lean locations, with figures that reproduce. I confirm unconditional completion of Z4.2.04. Before the next release, deliver the updated `R16_pending.json` or correct the report's statement that the register was updated. The approval remains AI-only, as the report itself says.

Review B's three blocking changes are also met: the shared core has owners (758,973 lines), U is the default and is never summed into N, and D and A exist as tiers.

## 2. Audit of the classified tiers

Samples used `random.Random(20261124).sample` over the curated blocks of each tier in `R17_triage.json`. For the automatic D and R rules I re-implemented `auto_class` and drew line-weighted samples from the result. My re-implementation gives D = 23,230 lines, equal to the report.

| Tier | Checked | Misgraded | Direction | Notes |
|---|---:|---:|---|---|
| A | 16 blocks (13 random, 3 from the table head) | 3 (19%) | A where S suffices | Stated difference matched the Lean statement in 7 of 7 compared |
| R | 15 (9 curated, 6 automatic) | 0 | — | All are `rfl`, `Iff.rfl` or single delegations |
| S | 8 | 0, with 2 borderline S/A | — | `levels_closed`, `coords_of_orthonormal_basis` are project-normalised |
| D | 9 (2 curated, 7 automatic) | 0 | — | 1–2 of 7 are theorem statements packaged as `def … : Prop` |
| L | all 10 blocks (12 declarations) | 0 | — | 4 theorem numbers not verified |

### A blocks

| Block | Base literature | Real and apt? | Difference vs. Lean | My tier |
|---|---|---|---|---|
| `z15-matchpow-cf16e7` | Arthur–Clozel, Ch. 1 §§1–4 | Real; apt | Accurate against `MatchPow` (`MatchPowAlt.lean:68–74`): unique place above v, constant c kept | A |
| `shared-geometric-lemma-cell` | Bernstein–Zelevinsky 1977, 2.12 | Real; apt | Accurate: only surjectivity of one cell map | A |
| `z15-cellstep-38dc78` | Bernstein–Zelevinsky 1976, 6.9–6.10 | Real; apt (invariant distributions orbit by orbit) | Accurate against `CellStep` (`TracePow.lean:17–26`): character, p-periodic s, zero cyclic sum | A |
| `z15-jacquet-borel-nontrivial-…-6ba51c` | BZ 1977 §2; Zelevinsky 1980 | Real; apt | Accurate: both published inputs are explicit hypotheses | A |
| `z4213-096` (`exists_pt_of_mem_La_moved`) | Weil, Basic Number Theory, Chs. II, IV | Real; framework only | Plausible; not checked line by line | A, weak basis |
| `z4213-099` (`exists_coprime_small`) | same | Real; framework only | Accurate | **S** (denominator clearing with a coprimality condition) |
| `z15-kerkill-e967b7` | Casselman, "The Jacquet module" | Real (fetched). Its three sections are the Jacquet module, admissibility, the canonical pairing; "contracting elements" is not its wording | Accurate against `KerKill` (`TraceQuot.lean:40–42`) | A |
| `z4213-078` (`fourthRoot`) | Mumford, Tata III §§3, 6 | Real; section-level, no URL | Consistent with `FourthRoot` (`ProductThetaMem.lean:43–50`) | A, weak basis |
| `z15-twexp-c2b58f` | Horn–Johnson, Lemma 1.3.19 | Real; apt for the common eigenvector only | Accurate (`ExistsCommonEigenvector.lean:16–144`: joint generalised weight spaces permuted by s, trace selects a fixed one) | **S** (finite-dimensional linear algebra) |
| `z4213-065` (`even_theta_line`) | DLMF §23.2; Mumford §3 | Real; apt | Consistent | A |
| `z4213-073` (`char_eq`) | DLMF §23.2; Mumford §6 | Real; apt | Accurate: `d % 8 = 7` is in the statement (`PStdChar.lean:310–352`) | A |
| `z4213-021` (`exists_isModel`) | Mumford, Tata III §§1–4 | Real; section-level; page range not verified | Not checked beyond the statement | A |
| `z15-isotypic-multiplicity-…-611c0a` | Etingof et al., Ch. 3 | Real; chapter-level | Consistent | A, weak basis |
| `z15-cosetsum-d24f4c` | Deitmar–Echterhoff, Thm 1.5.2 | Real; theorem number not verified | Accurate against `CosetSum` (`MatchSmulAlt.lean:44–51`): output #R·μ(K)/ν(V) | **S** |
| `shared-hilbert90` | Milne FT v5.00, Cor. 5.25 | Real (fetched; it is Hilbert 90 for cyclic extensions) | Accurate: S-unit witness is the project step | A |
| `shared-restricted-product` | Flath 1979 | Real; apt | Accurate; the statement is close to Flath's theorem itself | A (L/A boundary) |

Two points beyond the per-block grades:

- **Chapter-level bases.** Across all 71 A blocks, 20 lead with Mumford's Tata III by section, 5 cite Weil by chapter and 3 cite Etingof by chapter. That is enough to place the result in a theory and not enough for the A requirement of "state the adapted result and cite the model". These rows should carry a marker so the writer knows the hand proof is still wholly to be written.
- **Unnamed members.** A blocks hold 235 declarations but the JSON names only 73 heads; S holds 395 with 198 named. A reviewer cannot see which helpers a judgment covers.

### L blocks

All ten are statements of the kind the cited source proves, and the hypothesis comparisons read correctly against the Lean statements.

- **Verified or known to me:** Horn–Johnson 1.3.19 (two blocks, correctly cross-linked as one family), Milne MF Cor. 12.16 (two blocks), DLMF (23.2.14) and (23.10.3).
- **Theorem number not verified:** Milne ANT Thm 5.11, Lam VI.2.12, Voight 14.6.9, and the DLMF §23.3(i) location. For Lam, confirm that the cited theorem covers residue characteristic 2, since the Lean statement does.
- **DLMF as a source for existence of a lattice with given invariants:** it is a handbook statement without proof. Add a proof source.
- **`isotropic_of_locally_isotropic`** takes the Hasse norm statement as a hypothesis and needs four variables. The comparison says so; the grade stands.

L, S and R grades cover the head only. 169 of 197 S blocks and 3,391 of 3,469 R blocks depend directly on U. Only 1,456 U lines sit exclusively beneath L heads and 16,748 beneath A heads, so the registered tiers do not yet discharge much of the cone by domination.

### D and R

- **D** is correct by construction. Many `def … : Prop` entries are packaged theorem statements (`LocDesc`, `MatchPow`, `CellStep`, `BCMem`, `StatColumnJ`). The definition dictionary should separate vocabulary from statement packages.
- **Non-Prop definitions are left in U:** 40,072 lines in the pilots. They are D by the report's own definition.
- **R** is correct, and narrower than it could be (see §4).

## 3. The unclassified material

### 3.1 Method

- **Why declarations, not blocks.** The JSON does not contain the U blocks, so I rebuilt the population: pilot-union core declarations with positive weight that are not registered non-U heads, not `ind`, not Prop definitions, and not forwarding theorems. This gives 59,060 declarations and 744,029 lines against the report's 735,290. The difference between the two index totals is unnamed helper members of registered blocks, plus forwarders caught only by the tool's `first | exact` pattern.
- **Sampling.** Probability proportional to line count, without replacement, within strata, so the share of sampled declarations in a tier estimates the share of lines directly.
- **Seeds.** `random.Random(20261124)` for the first six strata (candidates sorted by graph index, `choices` with line weights, duplicates redrawn); `random.Random(20261125)` for the seventh.
- **Reading level.** Full statement, first 12–22 proof lines and the last few, plus the definitions of project predicates for seven doubtful items.

| Stratum | U lines | Sampled |
|---|---:|---:|
| Z1.5 only, shared among the 20 | 672,499 | 28 |
| Z1.5 exclusive | 20,569 | 6 |
| Z4.2.13 only, not shared among the 20 | 39,052 | 8 |
| Both pilots (shared) | 6,445 | 3 |
| Z4.2.13 only, shared among the 20 | 5,464 | 3 |
| Shared core outside both pilots | 49,761 | 4 |
| Exclusive cones of the other 18 inputs | 774,474 | 14 |

The last stratum is outside the report's ownership universe. I added it so the extrapolation would not rest on the pilots alone. It is dominated by Z1.1 (431,233 lines) and Z1.3 (133,992).

**Working definitions.**

- **R:** unfolding, reindexing, casts, one-step consequences.
- **S:** a fact or argument a specialist accepts as standard, including bespoke elementary lemmas proved by direct computation.
- **A:** a recognisable step of a known theory whose statement is shaped by the project's models, so a hand proof with stated differences is needed.
- **N:** no base literature identifiable and an argument that is more than computation.
- **"A?"** means A with N arguable; **"N?"** means N at statement level, not confirmed.

### 3.2 The sample

| # | Stratum | Declaration | Location | Lines | Tier | Reason |
|---:|---|---|---|---:|---|---|
| 1 | Z1.5/shared20 | `BW.zt_zero` | `SliceShift.lean:25–27` | 3 | R | unfolds a project definition at 0 |
| 2 | Z1.5/shared20 | `REAL.prod_ofFn_apply_of_eigen` | `QuantumDetHighestWeightHolds.lean:39–49` | 11 | R | product of operators on a common eigenvector; induction |
| 3 | Z1.5/shared20 | `Parabolic.diagPow_mem_center` | `CuspidalAdmissible.lean:86–99` | 14 | S | block-scalar diagonal matrices are central in the Levi |
| 4 | Z1.5/shared20 | `LadicPlace.norm_embedding_integer_le_one` | `NormEmbeddingIntegerLeOne.lean:7–35` | 29 | S | integral elements have norm ≤ 1 in a non-archimedean field |
| 5 | Z1.5/shared20 | `Ram.vdField_eq_avg` | `CondDisc.lean:41–86` | 46 | S | l-adic conductor–discriminant formula for subfields of a cyclotomic field (Washington, Thm 3.11 type) |
| 6 | Z1.5/shared20 | `T.gelfand_operator_pairing_adjoint` | `GelfandOperatorPairingAdjointStatement.lean:12–13` | 2 | R | `first | exact …` forwarder; the tool itself grades this R (contamination of my reconstruction, excluded from the estimate) |
| 7 | Z1.5/shared20 | `FinDisc.bessel_lintegral_le` | `KernelSumBoundUniform.lean:154–286` | 133 | S | Bessel-inequality bound for orthonormal eigenfunctions of a compactly supported convolution kernel (Godement/GGPS finiteness argument) |
| 8 | Z1.5/shared20 | `GelFlagPf.gelFlag_of` | `ContDiffMulRight.lean:218–300` | 83 | A | derives project predicate GelFlag from GelComm, GelN; Gelfand-type operator on an adapted flag |
| 9 | Z1.5/shared20 | `GradedWeylDivisibility.le_and_degreeOf_top_le_of_degreeOf_sum_le` | `PeelDegBound.lean:30–117` | 88 | A? | bespoke degree bound for a column-addition substitution in MvPolynomial; no base literature identified (N-possible) |
| 10 | Z1.5/shared20 | `LocalField.algEquiv_ext_sup` | `LubinTateUnramified.lean:17–31` | 15 | S | automorphism of a compositum is determined by its two restrictions |
| 11 | Z1.5/shared20 | `RightCosetSpace.automorphicKernel_smul_left` | `QuotientKernel.lean:21–28` | 8 | R | Γ-invariance of the automorphic kernel by reindexing |
| 12 | Z1.5/shared20 | `ParabolicProjection.exists_slice_ne` | `PProjA.lean:102–112` | 11 | R | nonzero function has a nonzero slice, from the Iwasawa-type decomposition |
| 13 | Z1.5/shared20 | `OpenCoinv.translate_mem` | `OpenCellJacquetMapSurjectiveWhittaker.lean:25–31` | 7 | R | stability of an open-cell function space under unipotent translation |
| 14 | Z1.5/shared20 | `CIndGlue.average_cut` | `SmoothSubrepCompactInductionSpan.lean:67–157` | 91 | A | averaging step inside compact induction (cut to one double coset); BZ/Bushnell–Henniart technique in the project model |
| 15 | Z1.5/shared20 | `CellA.blk_two` | `BlockIndexOfWeylShuffle.lean:12–20` | 9 | R | block index of a two-block partition |
| 16 | Z1.5/shared20 | `Asm.hint_of_rinv` | `HintTranslate.lean:17–22` | 6 | R | rewrites an index-normalised sum for a right-invariant function |
| 17 | Z1.5/shared20 | `FMul.fRaw_mul` | `InducedFunctionParabolicEquivariant.lean:84–109` | 26 | S | explicit highest-weight function is multiplicative under the parabolic; direct computation |
| 18 | Z1.5/shared20 | `FilLaws.σDp_xi` | `BdRFiltrationLaws.lean:76–92` | 17 | S | Galois group multiplies Fontaine’s ξ by a unit of B_dR^+ |
| 19 | Z1.5/shared20 | `PTop.bgen_adj` | `FrameBoundOf.lean:101–109` | 9 | R | adjoint of a generator from an earlier lemma |
| 20 | Z1.5/shared20 | `Parabolic.cellJacquetFun` | `GeometricLemmaJacquetCell.lean:512–514` | 3 | D | data definition |
| 21 | Z1.5/shared20 | `H.sandId` | `SandId.lean:107–186` | 80 | A? | identity in the spherical Hecke algebra of GL_n with Macdonald-type denominator polynomial (N-possible only as to normalisation) |
| 22 | Z1.5/shared20 | `Asm.term_eq` | `GlZeroEqOne.lean:377–398` | 22 | R | exponent bookkeeping for |det|^{1/2} |
| 23 | Z1.5/shared20 | `IsExpLieAlgebra.exists_prodExp_coord` | `DixmierMalliavinHaarCoord.lean:145–192` | 48 | S | coordinates of the second kind near 1 by the inverse function theorem |
| 24 | Z1.5/shared20 | `archExp_single` | `ArchExpSingleUnipotentEmbedding.lean:10–48` | 39 | R | matrix unit exponential is a unipotent embedding |
| 25 | Z1.5/shared20 | `BlockHomomorphism.blkGL` | `BlockHomomorphism.lean:409–540` | 132 | D | generated definition (132 lines of elaborated term) |
| 26 | Z1.5/shared20 | `Whittaker.prod_bottomRows_eq_prodFrom` | `WhittakerCells.lean:491–504` | 14 | R | finite product reindexing |
| 27 | Z1.5/shared20 | `SatakeVectors.isSatVecGL_of_ind` | `PSatCore.lean:42–131` | 90 | A | Satake multiset of a parabolically induced vector from the blocks’ Satake data, with modulus shifts |
| 28 | Z1.5/shared20 | `FX.piece_size` | `IntMvPolynomialCoeffAbsSumAddLe.lean:30–82` | 53 | S | ℓ¹ bound K^{k+1}/k! for homogeneous pieces; bespoke but elementary |
| 29 | Z1.5/excl | `Int.F_ne` | `OpBound.lean:246–264` | 19 | R | nonvanishing transferred through a basis |
| 30 | Z1.5/excl | `cmp_homeo` | `EigenspaceFactorizationOverNonsplitPlacesCMDatum.lean:107–127` | 21 | R | homeomorphism for a place with a unique prime above |
| 31 | Z1.5/excl | `conj_locGL` | `SatOfPol.lean:106–123` | 18 | R | conjugation commutes with local embedding |
| 32 | Z1.5/excl | `Sph.powSat` | `PowSat.lean:36–47` | 12 | R | unramified power character: Satake value |
| 33 | Z1.5/excl | `EigenLatticeOffDiagonal.oloc_comm` | `HeckeOperatorSummandWeightCMDatum.lean:32–44` | 13 | R | operator commuting with the regular representation commutes with an integrated operator |
| 34 | Z1.5/excl | `HeckeLevel.exists_level_nat` | `ExistsNatHeckeCharacterTrivialCongruentUnits.lean:17–52` | 36 | S | a Hecke character has a level |
| 35 | Z4.2.13/excl | `Inh.stdLat_fg` | `CayleyGaussianIntegralsCongrFact.lean:39–48` | 10 | R | finite generation instance |
| 36 | Z4.2.13/excl | `InertSign.vacuum_inert` | `WeilRepresentationVacuumSignInertPlaces.lean:254–327` | 74 | A? | sign of the Weil operator on the vacuum at inert places, assembled from literature leaves; lattice-model Weil representation (N-possible) |
| 37 | Z4.2.13/excl | `Constant.const_eq` | `PullEqGaussSmulIntertwiner.lean:24–155` | 132 | A? | explicit constant of a theta intertwiner as det(1−a)^{-1} times a Gauss sum (Weil 1964/Mumford type; N-possible as stated) |
| 38 | Z4.2.13/excl | `UnRep.exists_inverse_one_add_preserving_hat` | `ExistsInverseOneAddPreservingAdelicCompletion.lean:111–311` | 201 | S | 1 + eN·X is invertible on an adelic lattice; local Neumann-series argument |
| 39 | Z4.2.13/excl | `GlobalTheory.exists_isSymplecticFamily_span_eq` | `DualRestrictSurjectiveOfIsTorsionFreeQuotient.lean:163–260` | 98 | S | symplectic elementary-divisor basis over a PID for a nondegenerate submodule |
| 40 | Z4.2.13/excl | `ThetaConj.embeddingConj_evenTheta_coeff_of_fixes_field` | `CmThetaTaylorCoeffAlgebraicAndConjugate.lean:316–355` | 40 | A | Galois conjugation of Taylor coefficients of CM theta (Shimura reciprocity in project normalisation) |
| 41 | Z4.2.13/excl | `TA.transl` | `VacuumEntireAndNormalizedJetsAlgebraic.lean:281–288` | 8 | R | closure step using rational_points |
| 42 | Z4.2.13/excl | `Graph.term_shift` | `PhDetMulIntegral.lean:51–85` | 35 | S | semicharacter shift identity; direct computation |
| 43 | both/shared20 | `QNorm.exists_place_isSquare_and_not_isSquare` | `ExistsPlaceIsSquareAndNotIsSquare.lean:16–70` | 55 | S | a place where δ is a square and u is not; quadratic-extension/S-unit argument |
| 44 | both/shared20 | `QNorm.eq_one_of_mul_self_eq_one_withZero` | `SUnitMemGlobalNormOfMemLocalNorms.lean:39–49` | 11 | R | a·a=1 ⇒ a=1 in ℤ-valued group with zero |
| 45 | both/shared20 | `QNorm.isSquare_of_mem_locSq` | `IsSquareOfSUnitLocalSquareFiniteRealPlaces.lean:27–45` | 19 | R | contrapositive of a literature leaf plus subgroup bookkeeping |
| 46 | Z4.2.13/shared20 | `LocalLattice.mem_frameLattice_iff` | `MemIffForallMemLocalizeRingOfIntegers.lean:300–309` | 10 | R | membership in a frame lattice |
| 47 | Z4.2.13/shared20 | `Fills.Pj` | `DataGChain.lean:44–47` | 4 | D | recursive data definition |
| 48 | Z4.2.13/shared20 | `LegendreModelEllipticTorsion.e2Summand_succ` | `Legendre.lean:10–37` | 28 | S | q-expansion of the weight-2 Eisenstein summand |
| 49 | outside/shared20 | `NG.columnJ` | `CupKillAdm.lean:121–252` | 132 | N? | existence of a nonzero A-linear map out of a bespoke presented module (StatColumnJ); no base literature identified; elementary linear algebra |
| 50 | outside/shared20 | `FIN.InChiFixReal` | `RealClassMapSecondPlace.lean:72–81` | 10 | D | Prop definition |
| 51 | outside/shared20 | `core` | `CrystallinePeriodMatrixMemFilZeroOfWeightZero.lean:57–155` | 99 | A | period matrix lies in Fil⁰ at weight zero; standard p-adic Hodge successive approximation in project axiomatics |
| 52 | outside/shared20 | `exists_int_basis` | `ExistsIntBasis.lean:12–72` | 61 | S | continuous representation of a compact group over ℚ_l stabilises a lattice |
| 53 | other-excl Z4.1 | `ParitySumsOverFilteredPairs.sum_iN_tops` | `EntryATwoAndB.lean:164–168` | 5 | R | sum reindexing |
| 54 | other-excl Z1.1 | `urIndex_avg` | `HcUrIndex.lean:25–60` | 36 | S | cocycle trivial on a finite-index subgroup with invertible index is a coboundary |
| 55 | other-excl Z1.1 | `exists_max` | `CaCotOfQuot.lean:15–61` | 47 | S | maximal cotangent-independent family inside an ideal of a regular local ring |
| 56 | other-excl Z1.1 | `W.exists_determinantPair_map_of_algHom` | `ExistsDeterminantPairMapOfAlgHom.lean:45–90` | 46 | R | push-forward of a determinant pair along an algebra map |
| 57 | other-excl Z1.1 | `Hyp.lintegral_weight_mul` | `GJGlobalUnfoldCount.lean:216–228` | 13 | S | unfolding against a fundamental domain |
| 58 | other-excl Z1.1 | `RSq.map_inv_up_mem` | `NewformLiftLocalType.lean:189–196` | 8 | R | integrality of an explicit matrix away from p |
| 59 | other-excl Z1.3 | `UniformCoboundary.coboundary_of_approx` | `CoboundaryOfPadicAlgClUniformApprox.lean:51–128` | 78 | S | p-adic limit of coboundaries is a coboundary (finite-dimensional closedness); bespoke but elementary |
| 60 | other-excl Z2.K4 | `SmoothMinimalSupport.chi_lip` | `GSmMin.lean:22–33` | 12 | R | smooth transition is Lipschitz |
| 61 | other-excl Z1.1 | `PadicRank.finite_ker_padicLog` | `PrincipalUnitsRank.lean:224–234` | 11 | S | kernel of the p-adic logarithm on principal units is finite |
| 62 | other-excl Z4.4 | `Col.ResidueFieldUnfoldingNonzero` | `ChainOneB.lean:61–64` | 4 | D | Prop definition (statement package) |
| 63 | other-excl Z1.1 | `height_sub` | `CaCotLoc.lean:39–55` | 17 | S | height ≥ cardinality for part of a regular system of parameters |
| 64 | other-excl Z2.K4 | `SplitStd.extLast_mulVec_single_last` | `ExistsGLSplitSeqStandardOfStableRangeLe.lean:23–27` | 5 | R | matrix times last basis vector |
| 65 | other-excl Z4.2 | `SeamKer.seam_kerTh` | `ColumnFieldKernelPushforwardEqHostKernelFunction.lean:38–67` | 30 | A | transport of the kernel theta along a field identification (“seam”), assembled from literature leaves |
| 66 | other-excl Z4.2 | `TopStep.entB_zero` | `RedPDivOfUnit.lean:92–116` | 25 | R | entry formula at c′=0 |
Item 6 is graded R by the tool itself and is dropped from the estimates.

### 3.3 Estimate for the pilot union

Counts by stratum (item 6 removed):

| Stratum | n | D | S | A | R | N |
|---|---:|---:|---:|---:|---:|---:|
| Z1.5 shared | 27 | 2 | 9 | 5 | 11 | 0 |
| Z1.5 exclusive | 6 | 0 | 1 | 0 | 5 | 0 |
| Z4.2.13 not shared | 8 | 0 | 3 | 3 | 2 | 0 |
| Both pilots | 3 | 0 | 1 | 0 | 2 | 0 |
| Z4.2.13 shared | 3 | 1 | 1 | 0 | 1 | 0 |

Weighted by stratum size and scaled to the report's 735,290 U lines:

| Tier | Historical estimate of indexed lines |
|---|---:|
| R | ≈ 303,000 |
| S | ≈ 243,000 |
| A | ≈ 138,000 |
| D | ≈ 51,000 |
| L | — |
| N | 0 |

- The ranges are driven by the 27 draws in the stratum with the greatest indexed weight (Wilson intervals on that stratum).
- **D** has an independent check: non-Prop `def` declarations are 40,072 U lines, so D is pinned much more tightly than the sample alone would allow.
- **L vs. S.** I graded nothing L, but about two thirds of my S items are statements of known results that could be closed by citation (items 4, 5, 10, 18, 23, 34, 39, 43, 48, 52). The rest are bespoke elementary lemmas that need a short written proof (17, 28, 38, 42).
- **N.** Four of the 47 are "A?" (9, 21, 36, 37). If all four were N, that would be about 58,000 lines of pilot U. I do not think all four are; 21 and 37 are classical computations in an unusual normalisation.
- **Where A sits.** A is concentrated in the Z4.2.13 theta material (3 of 8) and in the automorphic machinery of the Z1.5 shared core (5 of 27). For the Z1.5 exclusive region, which R16 had placed largely in its default N bucket, the six sampled declarations received five R and one S.

### 3.4 Extrapolation to the 20-input union

Assumptions:

1. The other 18 exclusive cones are represented by my 14 draws from them (6 R, 6 S, 1 A, 1 D).
2. The shared core outside the pilots is represented by 4 draws (1 each of S, A, D, N?).
3. The 44,975 lines already classified in the pilots keep their grades.
4. My statement-level grading is as reliable outside the pilots as inside.

| Tier | Historical estimated lines in the 1,604,500 union |
|---|---:|
| R | ≈ 640,000 |
| S | ≈ 590,000 |
| A | ≈ 210,000 |
| D | ≈ 140,000 |
| L | < 1,000 as registered |
| N | ≈ 12,000 |

- **D floor:** definitions and inductives by kind alone are about 120,000 lines (23,230 graded, 40,072 in pilot U, 56,920 elsewhere).
- **N:** the point estimate rests on a single item, 49 (`NG.columnJ`, 132 lines), which is elementary linear algebra about a bespoke presented module. One firm candidate in 65 gives a rough upper estimate of 130,000 indexed lines. Counting the four "A?" items as well gives 5 of 65, an estimated range of 50,000–270,000 indexed lines.
- **Answer to the key question:** genuinely new mathematics at lemma level is most likely on the order of 10,000–60,000 lines, and I cannot exclude 130,000. Adaptations of known theory are most likely about 200,000 lines. In this sample, the N-leaning items are bespoke technical lemmas (a polynomial degree bound, a module presentation, a Weil-operator sign, an intertwiner constant), not new theorems of independent interest.

What this does not measure:

- **Short novel statements.** A two-line theorem with a new statement and a delegated proof has almost no line weight. The top-level reductions (the Z-inputs themselves and the ~2,850 `T.*` statement wrappers, 16,502 lines) need a separate statement-level pass.
- **Composite novelty.** Whether the combination of known pieces is new is a question about the blueprint, not about lemmas.
- **Depth.** I skimmed proofs. An item I graded S from its statement could hide a non-standard argument, and a 100-line A item could turn out to be routine.

## 4. Classifying the remaining U at scale

### 4.1 What the sample says about cheap signals

| Signal | In my sample | Proposed action |
|---|---|---|
| `def` / `ind` | 5 of 5 are D | Automatic D; flag those over 30 lines for a look |
| Theorem, 1–9 lines | 11 of 11 are R | Automatic R after a 100-item validation sample |
| Theorem, 10–29 lines | 24 of 24 are R (15) or S (9); no A, no N | One merged "R/S short" grade, confirmed from the statement alone |
| Theorem, 30+ lines | 26 items: 11 A or N, 13 S, 2 R | Must be read |

- **Every A and N item in the sample is at least 30 lines long.** Length is the single most useful filter. The reviewer proposed testing provisional R, S or D labels from kind, length and statement. That procedure reads no proof. The sample sizes behind this are 11 and 24, so validate before relying on it.
- **Top-level namespace.** `GroundTheory.*` (107,126 U lines in the pilots) reads as library-style formalisation of textbook theory. All 8 of my draws from it were R, S or D. A module-level grade of "L/S, cite the textbook" with a 50-item validation sample is reasonable there.
- **Directory names are unreliable.** A smooth-partition-of-unity lemma sits under `KTheoryStability`, and a p-adic integrality lemma under `IwasawaDecomposition`. File names and namespaces are descriptive and usable; directories are not.
- **Other automatic steps:**
  - Extend the forwarding rule to `Iff.rfl`, `by simp`/`simpa`, `unfold … ; simp`, and proofs made only of `omega`, `ring`, `norm_num`, `group`.
  - Grade one representative of each repeated statement (3,402 U candidates, plus the `Cd.*` copies of `Ker.*`).
  - Historical proposal: register heads for the Weierstrass functions, modular j and local class field theory developments. The current atlas grants citation evidence only at its compared declaration.

### 4.2 Procedure

1. **Rules pass (no model).** Apply the D, R and short-theorem rules and the namespace rule. These rules proposed candidates for a later reading.
2. **Validation.** Draw 100 line-weighted items from each rule's output and grade them at statement level. Accept a rule if at most 3 are wrong and none is A or N.
3. **Reading pass on long theorems.** About 6,020 declarations in the pilots and 7,150 elsewhere, in about 8,900 files.
   - Work by file: a file is named after its main theorem and has a median of about 45 lines of U.
   - Batch 25–30 files, or 40–60 long declarations, per agent call. Supply each statement with its Prop expansions, the first 15 proof lines and the callers.
   - Ask for a tier, a base reference at statement level or an explicit "none found", and one sentence on the difference.
   - That is about 250–330 batches in total.
4. **Second opinion.** Send every item returned as N, as A with "none found", or as A with a chapter-level basis to a second, independent pass that reads the whole proof. Expect a quarter or less of the long theorems.
5. **Statement pass.** Separately grade the top-level statements and the `T.*` wrappers by statement alone, since they carry the novelty that line weighting misses.

### 4.3 Reasoning effort

- **Lower effort is safe** for steps 1–2 and for the short-theorem confirmations. These are recognition tasks, the sample shows no A or N below 30 lines, and errors between R and S cost nothing downstream.
- **Lower effort is not safe** for step 3 where it decides A against N or supplies a reference. Twenty-eight of the 71 existing A rows already cite a chapter or section instead of a statement, and four L theorem numbers could not be confirmed. A weaker pass will produce more of both, and fabricated theorem numbers are the costliest error here.
- **A workable split:** low effort proposes a tier for every long theorem; high effort handles only what comes back as A or N. On the sample's proportions that puts high effort on the long theorems flagged by those two sample categories.

## 5. Items for the author

1. Deliver `R16_pending.json` as updated, or correct the report's E7 line.
2. Deliver the U block ledger and owner table, or put the U blocks in the JSON. Name all members of curated blocks.
3. Route non-Prop definitions to D (about 40,000 lines in the pilots).
4. Regrade `z15-twexp-c2b58f`, `z15-cosetsum-d24f4c` and `z4213-099` to S, or record why they are A.
5. Mark A rows whose basis is a chapter or section, and replace those bases with statements where one exists.
6. Verify Milne ANT 5.11, Lam VI.2.12, Voight 14.6.9, Deitmar–Echterhoff 1.5.2 and the Mumford and Weil page ranges; use one versioned URL per Milne text.
7. In the D dictionary, separate vocabulary from `def … : Prop` statement packages.
8. Explain or remove the 6-line difference between 1,604,500 and review B's 1,604,506. My rebuild gives 1,604,500.
