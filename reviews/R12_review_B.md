AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

# R12_review_B

AI review report produced during this project; file names are internal working names.

- Internal source file: `out/R12_review_B.md`
- SHA-256: `4f2f73d8ab62283127c95358bf89d17a3e19be0345b6a6f9ce57632178f7137b`
- Report scope: Round-12 independent review B: Z4.4 suppliers 1 and 7, the assembly, and the Z4.4 closure question

## Internal report

The report below preserves its original verdict, scope and unresolved points. Historical review-machine home prefixes are displayed as `${REVIEW_HOME}`; the source checksum above identifies the original report. Superseded graph percentages have been removed from this public edition. Source line numbers in other records count from its original title.

# Round-12 independent review B: Z4.4 suppliers 1 and 7, the assembly, and the Z4.4 closure question

Reviewed text: `${REVIEW_HOME}/work/prev12/ch_P_r12.tex`, lines 1773-3616 (supplier 1, supplier 7, `r12:assembly`, `r12:outcome`), and the `round12` block of `status.json`.
Lean source: cleaned copy `${REVIEW_HOME}/src/rh/src`. Line numbers below are the original-mirror numbering (commit `40e56bab`), the numbering used by the chapter and by `graphq.py`; the cleaned copy is shifted by a few lines.
Graph: `graphq.py` plus reachability and dominator passes over the same `graph_cache.bin`.

Nothing in this review, in the chapter, or in the Lean development is treated here as establishing RH or GRH. The review only compares hand proofs with the Lean statements they label.

## 0. What was and was not checked

- **Statements.** All 33 declarations in scope (16 for supplier 1, 15 for supplier 7, the two assembly theorems) were compared with their Lean signatures, hypothesis by hypothesis and conclusion by conclusion.
- **Proofs.** Read against the Lean proof body or the Lean definitions: both assembly theorems, the root, `perDecTwT_of_std`, `exists_gLoc_idG_chiTied`, `ipV_norm_tie`, `exists_conj_referenceChartIndex`, `furtherPlace_penultimateChart_character_inverseValue`, `charts_tuple_trivQ`, `charts_funKilled`/`swapLaws`, `step_gam_mem_UJ`, and the definitions `InJSym`, `JSymG`, `lamSym`, `InJ`, `lamJ`, `Loc.om`, `Loc.E1`, `ChIdx.Ok`, `ChiFin`, `NearSet`, `valV`, `TwLevJ`, `StdF`, `StdLvC`, `StdW`, `CarH`, `CharacterCompatible`, `FunKilled`. The remaining paragraphs were checked for internal mathematical correctness and for agreement with the Lean statement and with the dependency list of the Lean proof, not line by line against the Lean body. `til_ties` (about 1,100 Lean lines) and the reference-chart paragraph are in this second group.
- **Dependencies assumed from the other reviewer.** Listed in section 3.3. My verdicts are conditional on them.
- **Line-count convention.** The chapter's figures (root 88,646; supplier 1 53,609; supplier 7 62,711) are reproduced exactly by counting distinct core source lines of cone members with a nonzero start line. All figures below use that convention. "Dominated" means: lines that leave the root cone when the named declaration is removed.

## 1. Verdict table

### Supplier 1 (`ch_P_r12.tex:1773-2601`)

| # | Lean declaration | File:lines | Text | Verdict |
|---|---|---|---|---|
| 1 | `GlobalTheory.Mem.TypePrimes.exists_gLoc_idG_chiTied` | `ExistsGLocIdGChiTied.lean:194-211` | 1783-1835 | **CONFIRMED** |
| 2 | `GlobalTheory.Mem.Col2.MemChart.cls_bij` | `ExistsMemberStepCharts.lean:310-348` | 1837-1866 | **CONFIRMED** |
| 3 | `GlobalTheory.Mem.Col2.MemChart.stM_range` | same, 355-366 | 1868-1876 | **CONFIRMED** |
| 4 | `GlobalTheory.T.columnPoint_eq_of_deco_and_cosetReduction` | `...Statement.lean:6-7` | 1895-1919 | **CONFIRMED** |
| 5 | `GlobalTheory.T.exists_couplingCoset_with_given_reduction` | `...Statement.lean:6-7` | 1921-1938 | **CONFIRMED** |
| 6 | `GlobalTheory.Mem.Col2.MemChart.exists_charts` | `ExistsMemberStepCharts.lean:521-566` | 1940-2046 | **CONFIRMED WITH GAPS** |
| 7 | `GlobalTheory.Mem.Col2.TC.clsP_tie` | `ExistsEmbFIff.lean:209-293` | 2048-2088 | **CONFIRMED WITH GAPS** |
| 8 | `GlobalTheory.Mem.Col2.TC.val_tied` | `HermitianChartComplexRationalIntegralForms.lean:394-510` | 2090-2118 | **CONFIRMED WITH GAPS** |
| 9 | `GlobalTheory.Mem.Col2.MetricTie.ipV_norm_tie` | `UnitaryOfIsON.lean:195-205` | 2119-2129 | **CONFIRMED WITH GAPS** |
| 10 | `GlobalTheory.Mem.Col2.DiaChart.dilTied` | `DiamondOperatorsOnCharts.lean:176-231` | 2131-2172 | **CONFIRMED WITH GAPS** |
| 11 | `GlobalTheory.Mem.Col2.TC.til_ties` | `HermitianFormLastCoordinateUniformizerVectorSelf.lean:1086-1143` | 2174-2264 | **CONFIRMED** |
| 12 | `GlobalTheory.Mem.Col2.OneLevel.stepBefore_oneLevel` | `ChartTiedTopLevelChain.lean:369-484` | 2266-2401 | **CONFIRMED** |
| 13 | `GlobalTheory.Mem.Col2.TC.GLev0.glev_zero` | `LevelTwistPrimesStepZeroCharacterEqOne.lean:571-573` | 2403-2456 | **CONFIRMED** |
| 14 | `GlobalTheory.Mem.Col2.TC.levels_top_row_sym` | `LevelsTopRowSym.lean:217-224` | 2458-2506 | **CONFIRMED** |
| 15 | `GlobalTheory.Mem.Col2.ChartLevel.chart_gLevH` | `ValLtOfRedM.lean:478-487` | 2508-2541 | **CONFIRMED** |
| 16 | `GlobalTheory.T.exists_standardFormComparison_symmetricLevel_members` (= `FormSym.formsTiedSym_std`, `ExistsStandardFormComparisonSymmetricLevelMember.lean:52-243`) | `...Statement.lean:8-9` | 1773-1781, 2543-2600 | **CONFIRMED WITH GAPS** |

### Supplier 7 (`ch_P_r12.tex:2602-3510`)

| # | Lean declaration | File:lines | Text | Verdict |
|---|---|---|---|---|
| 17 | `GlobalTheory.T.exists_unitaryAdelic_twist_diagonal_at_primes` | `...Statement.lean:8-9` | 2619-2647 | **CONFIRMED** |
| 18 | `GlobalTheory.T.pointOverX_has_adelicPoint_blockExtend_mul` | `...Statement.lean:8-9` | 2649-2682 | **CONFIRMED** |
| 19 | `GlobalTheory.T.chart_lastStep_twistBasePoint` | `...Statement.lean:8-9` | 2684-2722 | **CONFIRMED WITH GAPS** |
| 20 | `GlobalTheory.T.exists_unitaryAdelic_lift_typePrime_reductions` | `...Statement.lean:7-13` | 2724-2756 | **CONFIRMED** |
| 21 | `GlobalTheory.T.exists_reference_class_matching_coupling_coset` | `...Statement.lean:7-14` | 2758-2796 | **CONFIRMED** |
| 22 | `GlobalTheory.T.exists_conj_referenceChartIndex` | `...Statement.lean:7-16` | 2798-2919 | **CONFIRMED WITH GAPS** (hand proof is a different route from Lean; see 4.2.4) |
| 23 | `GlobalTheory.Mem.Col2.ChExM.chart_of` | `ExistsFiniteOrderChartsMiddleSteps.lean:314-396` | 2921-3065 | **CONFIRMED WITH GAPS** |
| 24 | `GlobalTheory.Mem.Col2.ChExM.exists_charts` | same, 450-499 | 3067-3083 | **CONFIRMED WITH GAPS** |
| 25 | `GlobalTheory.T.exists_levelJ_character_eq_member_off_places` | `...Statement.lean:7-8` | 3144-3189 | **CONFIRMED** |
| 26 | `GlobalTheory.T.furtherPlace_penultimateChart_character_inverseValue` | `...Statement.lean:12-13` | 3191-3269 | **CONFIRMED WITH GAPS** (direct proof, different route from Lean; see 4.2.7) |
| 27 | `GlobalTheory.T.exists_character_allCharts_furtherPlaces` | `...Statement.lean:9-10` | 3271-3287 | **CONFIRMED** |
| 28 | `GlobalTheory.Mem.Col2.FinAtQ.chartLoc_finiteIndex` | `ChartLocalGroupFiniteIndexAtFurtherPlace.lean:195-209` | 3289-3322 | **CONFIRMED** |
| 29 | `GlobalTheory.T.furtherPlaces_group_contains_chart_levels` | `...Statement.lean:9-10` | 3324-3330 | **CONFIRMED** |
| 30 | `GlobalTheory.T.exists_penultimateLevel_couplingCosets` | `...Statement.lean:8-9` | 3332-3411 | **CONFIRMED WITH GAPS** |
| 31 | `GlobalTheory.T.trueColumnChoice_exists_chainData_with_basePoints` (= `TC.tw_ties_with_points`, `TrueColumnChoiceExistsChainDataWithBasePoints.lean:13-23`) | `...Statement.lean:10-18` | 2602-2617, 3413-3509 | **CONFIRMED WITH GAPS** |

### Assembly and root (`ch_P_r12.tex:3511-3577`)

| # | Lean declaration | File:lines | Verdict |
|---|---|---|---|
| 32 | `GlobalTheory.Mem.Col2.TC.colsTiedSym_std` | `ExistsStandardColumnComparisonsTrueColumns.lean:20-72` | **CONFIRMED** |
| 33 | `GlobalTheory.Mem.Col2.TC.colsTwPTiedS_std` (with `underQ_iff` 19-32, `carH_of_cols` 34-43) | `TrueColumnChoiceExistsStandardChainData.lean:45-56` | **CONFIRMED** |
| 34 | `GlobalTheory.PerTwClose.twistedPeriodAdmissible_of_rowInt` (derivation from the two records) | `AdmissiblePeriodTwistOfIntegralRows.lean:14-21` | **CONFIRMED** as an implication from suppliers 1-9; closure verdict in section 2 |

No declaration in scope is NOT CONFIRMED. I found no false statement and no step that fails. Every gap is one of three kinds: a sub-argument given as an outline, a delegation to a generic argument in the other reviewer's scope, or missing accounting.

## 2. Z4.4 closure verdict

**CLOSE AFTER LISTED FIXES**, conditional on the other reviewer confirming suppliers 4, 8, 9, the Weyl duality and the adelic point.

Reasons for closing:

1. **The round-5 objection is answered.** R5 found that existence of `C` and `t` rested on nine supplier theorems named nowhere. All nine are now named, stated and given a hand derivation; the two assembly theorems are reproduced exactly as Lean composes them (4.3).
2. **The top-level structure is the Lean structure.** The root calls `exists_standardColumnComparisons_trueColumns` (62,010 lines inclusive), `trueColumnChoice_exists_standardChainData` (73,759), `perDecTwT_of_std`, `admissiblePeriodTwists_reduction_placeTuples` and `twistedPeriodDecomposition_of_classwiseTwistedPairingIntegral`. The first two are the assemblies of suppliers 1-6 and 7-9. The last three are the class-sum part that R5 already found correct; `ch_P_r12.tex:3546-3576` restates it faithfully.
3. **No circularity.** No supplier root lies in the cone of another, except supplier 6, which lies in all. The supplier 1 cone contains eight chart-level supplier 8 results and no supplier 7, 8 or 9 root. So the reference charts and forms are built before the twisted chain, as `r12:outcome` claims. The order "C, then t over that C, then the class sum" is the order of the Lean proof.
4. **One top point, one character.** `tw_ties_with_points` extracts the top frame from `StdW.topk` of the `W` it has just built; the remark at 2610-2612 is correct. `exists_character_allCharts_furtherPlaces` gives a single character on the product of the generated groups, and the text handles the choice inside `valV` correctly (all near-pair values agree, 3250-3256).
5. **Hypotheses are labelled.** `I.Ok`, `Pins`, `l`, `l0`, `Z`, `RowInt`, `tp.xi = I.xi` are stated as hypotheses. `RowInt` is discharged at the caller, as recorded in `prev5/ch_P.tex:12327-12334`. The three literature leaves in the cone (`Published.herm_col`, `exists_cc_eq_neg`, `exists_basis_one_imaginary`) enter only through the adelic point construction, which is the other reviewer's.

Reasons it cannot close as it stands (details in sections 3 and 5):

- **A. Unlabelled Lean prerequisite of 4,485 dominated lines.** The stage and base law derivations from `I.Ok` and `Base` are in the root cone, are named in no chapter, and are neither reproduced nor labelled (3.2). The hand proof needs one definitional field of them, so a two-sentence fix suffices, but by the blueprint's own convention an unlabelled prerequisite keeps a unit partial.
- **B. Two hand proofs replace the Lean route.** `exists_conj_referenceChartIndex` and the further-place character identity are proved by arguments that are not the Lean proofs. Both arguments are correct as far as I can check. The first uses a tuple-independence lemma that exists nowhere in Lean, and the text omits two of the facts it needs (4.2.4). The bypassed Lean blocks are 5,045 and 2,846 dominated lines; only the first is flagged as bypassed in the text.
- **C. Outline-level sub-arguments** in items 6-10, 19, 23, 24, 30 (section 4), several of which delegate to "the generic arguments of supplier 9" without a pinpoint.
- **D. Registration.** Hand-proved intermediate theorems carrying most of supplier 7's exclusive content are not review entries (3.4).

If the other reviewer returns NOT CONFIRMED on any of the items in 3.3, the verdict becomes DO NOT CLOSE regardless of the above.

Status of that condition when this report was finished: `R12_review_A.md` was already in this directory. Its verdict table has no NOT CONFIRMED among its 26 declarations (8 CONFIRMED, the rest CONFIRMED WITH GAPS), so the condition is met as reported there. I read only its verdict table and did not check its findings. One point from it bears on my scope: review A records `upNatTie`, `dnNatTieG_cols` and `lvSame_zero` as checked at outline depth only, without a clause-by-clause statement comparison. `upNatTie` and `dnNatTieG_cols` are direct dependencies of the supplier 1 proof (`formsTiedSym_std`), and `upNatTie` is where the stage law block of 3.2 enters. So the shallowest-reviewed part of the whole Z4.4 derivation sits inside supplier 1's cone.

## 3. Cone analysis

### 3.1 Decomposition of the root cone

Root cone: 15,659 declarations, 88,646 core lines, three literature leaves.

| Piece | Inclusive lines |
|---|---|
| Supplier 1 | 53,609 |
| Supplier 2 (confirmed R11) | 19,383 |
| Supplier 3 (confirmed R11) | 16,899 |
| Supplier 4 | 22,116 |
| Supplier 5 (confirmed R11) | 17,437 |
| Supplier 6 (confirmed R11) | 14,396 |
| Supplier 7 | 62,711 |
| Supplier 8 | 39,826 |
| Supplier 9 | 34,914 |
| Outside all nine suppliers | about 4,500 |

Figures for suppliers 2-6, 8, 9 and the last row use all core lines, a different line-count convention from the chapter. The part outside the nine suppliers is the Weyl duality used by `pair_integral` (`StandardWeylLatticesFockDual`, `TransportedWeylLatticeHermitianDuality`, `ApplyWordMemDualWeyl`, `LowerTriOfInterlaced` and neighbours, other reviewer) and the class-sum files (`PerDecTwTOfStd`, `ClassPairingIntegralFormRowIsIntegral`, `TwistedPeriodDecompositionOfClasswiseTwistedPair`, `AdmissiblePeriodTwistsReductionPlaceTuples`). Supplier 1 dominates 5,944 lines and supplier 7 dominates 19,637.

Because all nine supplier roots are now either confirmed or submitted, registration covers the cone mechanically. The useful question is which parts of the cone the hand proofs do not reach. Those are listed next.

### 3.2 Unreproduced and unlabelled pieces

| Piece | Location | Inclusive | Dominated | Status in the text |
|---|---|---|---|---|
| Stage and base laws: `ColIn.Ok.stp_ok`, `Ok.unrepresented_step_conditions`, `StepOk.stepY_ok`, `FramedForms.main`, `base_fields_primes_ok`, `FieldsLaws.fields_ok`, `BasePrimes.primes_ok`, `base_fOk` | `TrueColumnChainsSatisfyConditions.lean:35-50`, `FiniteOrbitsOfFiniteFibres.lean:65-103`, `ExistsSmulOfDecoEq.lean:83-152`, `BaseFieldsDefiniteLaws.lean:114-165`, `ProdAbsNormDivsDvd.lean:148-182` | 12,289 | 4,485 | not named in any chapter |
| of which `stp_ok` alone | | 12,289 | 3,832 | not named |
| `nabDelLoc` / `nablaDeltaLocal_holds` under `mem_localization_delAtr` (used by `val_tied`, `bw_tie`, `clsP_tie`) | `CoefficientsModP.lean:24`, `NablaIndependenceHolds.lean:578-580` | 5,665 | 861 | not named in my scope; Weyl section to confirm |
| `LevTwist.levOk_twists` (used by `val_tied`, `isPt_up`) | `LevOkTwists.lean:48-85` | 4,698 | 503 | named once, at line 572, outside my scope |
| `LatGood.hasRatBasis`, `LatGood.step_gram_posDef`, `majAt_classSum` (used by `ipV_norm_tie`) | `WeightLawGoodOfFieldEmbedding.lean:180-193` | 3,542 | 458 | not named |
| `PerConj.period_conj` | `CevInjective.lean:219-225` | 16,088 | 188 | hand proof at `ch_P_r11.tex:961-1001` and `ch_P_r12.tex:1003, 1297`; not a review entry |
| Twist-place disjointness: `twistPlaces_prime_to_levelAndTypePrimes`, `not_twistPlace_referenceTuple`, `twistPrimes_reference_tuple_eq_empty`, four more | `...Statement.lean` files, `TrueColumnChoicesHeckeCharReferenceEqOne.lean:273-279` | 10,069 | 160 | used as facts ("the reference twist set is empty", "Q avoids T and the generators"); not named |
| `eCls0_mu0_eq_self` and the `ClsZero` lemmas | `StepZeroClassEquivReferenceTupleEqSelf.lean:9-15`, `StepZeroClassesBijectiveSameDeco.lean` | 8,464 | 156 | one sentence at 3499-3500 |

On the first row. `stp_ok` has exactly one caller in the root cone, `TC.step_gam_mem_UJ` (`StepGamMemUJ.lean:10-16`), which is used by `UpChart.upNatTie` (`InvSmulMem.lean:311`). The only field used is `.unit`: the rational component of a stage move is unitary. In `stepY_ok` that field is proved by the one-line `ufGL_conjTranspose_mul`. The rest of the record (finiteness of orbits and stabilizers, hence class-set finiteness for Hermitian lattices through `classSetFinite_core`, successive minima, `autFinite`) is built by Lean and discarded. So this is an accounting gap, not a mathematical one: a hand proof needs one definitional fact and should say so. `upNatTie` is a supplier 8 entry, so the sentence belongs in that section; it is listed here because it sits in the supplier 1 cone and in the root cone. Elsewhere in my scope the "stage law" is a genuine hypothesis, the field `l.ch` of `I.Laws`, and the text's wording at 1876, 2021, 2040 is correct.

### 3.3 Dependencies on the other reviewer's scope

My verdicts assume the following are correct.

- **Adelic point.** `exists_adelicPoint_decoratedLattice_allTwists` is used for `yStd` (1957-1960), for the primed chart through `exists_isPtOf_cm` (2057-2059), and for `g_c` in the top and middle twisted charts (2701-2702, 3069-3071). All five point entries lie in both supplier cones.
- **Supplier 8 chart-level results inside supplier 1.** `upNatTie`, `dnNatTieG_cols`, `bw_tie`, `fvTieG`, `exists_level_projections`, `dn_keeps_chart`, `dn_level_functional`, `dn_locP_lat`. The supplier 1 assembly takes them in one sentence (2576-2579). The diamond paragraph uses "the factorization in supplier 8" (2133-2135).
- **Supplier 9 results inside supplier 7.** `decoratedPointClasses_bijective_doubleCosets`, `exists_K1_point_congruent`, `mem_framedLevel_iff_two_adelic_points`, used at 2703-2709 and 3038-3041.
- **Supplier 9 generic arguments inside supplier 1.** `clsP_tie` applies "the value and metric arguments under supplier 9" (2073-2074); the corresponding Lean lemmas are the `RowTie` family, `ExistsEmbFIff.lean:29-142` and `UfGLRatHom.lean:43-108`.
- **Weyl duality.** The transported-lattice localization formula in `val_tied` (2111-2113), wrongly attributed there to supplier 8.
- **Suppliers 2, 3, 5, 6** as confirmed in R11. Supplier 6 is used throughout (Gram matrix 1, `IdY`, class lattice equals decorated lattice).

### 3.4 Hand-proved but unregistered declarations

These carry real content, are proved in my scope, and are not among the 57 entries.

| Declaration | File:lines | Inclusive | Dominated | Text |
|---|---|---|---|---|
| `TC.ChTw.charts_tuple_trivQ` (with `match_base_trivQ`, `charts_match_trivQ`, `Match.match_idx`) | `ChartsTupleTrivQ.lean:23-101`, `MatchTupleChartMemberChart.lean:17-110` | 40,570 | 10,838 | 3085-3142 |
| `TC.twPack_ex`, `twStep_mid`, `twStep_top`, `twStep_out`, `tw_chains` | `TrueColumnChoiceTwistedChainsFormsClasses.lean:62-484` | 63,176 | n/a | 3413-3509 |
| `TwAtStd.twAtT_exists` | `DecoStabTrivial.lean:146-176` | 14,624 | 158 | 3467-3485 |
| `TC.charts_funKilled`, `Reside.swapLaws`, `Reside.stab_eq` | `InclMulInvMul.lean:227-439` | 17,056 | small | 1985-1989, 3428-3444 |
| `T.localMove_classRep_iff_localConditions` and the two conjugation statements | `LocalMoveClassRepIffLocalConditions.lean:218-339` and neighbours | 14,322 | small | 3103-3132 |
| `FormSym.readsK_one` | `MemFiCComp.lean:147-159` | 13,772 | 13 | 1886-1893 |
| `nonempty_classMap_above_lastStep` | `NonemptyClassMapAboveLastStep.lean:14-16` | 4,362 | small | 3453-3457 |

`charts_tuple_trivQ` is the largest single block of supplier 7. I read its Lean proof; the paragraph at 3085-3142 follows it (index match, supported lift `t`, frame `k_0 t`, local-move criterion, conjugation, single-place insertion for `Uloc`). It should be a review entry.

## 4. Per-section findings

### 4.1 Supplier 1

**Statement (1773-1781).** Exact. Hypotheses `I.Ok`, `Pins`, `l`, `Z`. Conclusions: `Ch`, `chOf`, `F`; `StdF` and `StdLvC` for every `u`; finiteness; unique label at `m`; equality of `(F u).gl`; `CharacterCompatible` at `u₀`. All eight appear.

**4.1.1 Generator datum (1783-1835).** Matches `exists_gLoc` and `exists_gLoc_idG_chiTied`. The exponent `2(a+1)`, the use of `chi_om` and `chi_inj`, and `orderOf = p-1` from injectivity agree with `ExistsGLocIdGChiTied.lean:132-191` and with the three fields of `CharacterCompatible` (`DefsChi.lean:16-24`). The trace-unit argument at 1794-1796 is correct but compressed: the reason is that the conjugate of `a` lies in the second prime and `a` does not. Complete.

**4.1.2 Fibre of the class map (1837-1893).** `cls_bij` has two explicit hypotheses (`hsur`, `hnorm`) and the section variable `hinj` (`ExistsMemberStepCharts.lean:301`); the text's "three hypotheses" is right. Both directions are proved. `stM_range` correct. The text cites 350-366 for `stM_range`; 350-353 is the definition `stM`.

**4.1.3 Reduction fibre (1895-1938).** Both statements exact, including `QE = ∅` and `q_w ∉ w²`. The CRT construction is correct: the conditions defining the coset lattice are at generator places only, so integrality of `e_w/q_w` is needed only there, which is what is arranged.

**4.1.4 Reference chart, `exists_charts` (1940-2046).** Statement exact (`ReadsK`, equality with `yStd`, uniqueness at `i = 0` and `i = m`). Gaps:

- (a) The level `U` is asserted to be a `StepLevel` by a list of properties ("compact open", "product of local levels", "prime-order quotient", stabilizer identification) followed by "These are the fields of `stepOf`" (1977-2001). The Lean record is built in `RecLevelStep`, `RecLevelLocF`, `RecLevelLocK`, `RecLevelLoc`, `RecLevelLocT`, `RecLevelCls`, `RecLevelAsm`, about 2,500 lines, cited only by range. The calculations given are right (`L_0^∨`, index `T^{2f}`, the last-row congruence), but the field list of `StepLevel` is not enumerated, so completeness cannot be read off.
- (b) "Completion of the global lattice detects the local matrices ... by clearing denominators and applying CRT" (2012-2015) is one sentence for the local-global lattice principle.
- (c) `FunKilled` (2045). In Lean `exists_charts` does not return `FunKilled`; `formsTiedSym_std` passes the charts through `charts_funKilled`, which replaces each chart by one with the canonical functional and the same `Lb`, `Uloc`, `U`. The hand route (build the chart with the canonical functional from the start) is legitimate, but the text should say that the Lean chart of `exists_charts` is replaced and that `yStd` equality and `ReadsK` survive. The stabilizer argument that justifies the replacement is at 3428-3444, in the supplier 7 section; it is correct (the functional is linear over the split local algebra, so it factors through one of the two residue lines, and unitarity pairs the two lines).

**4.1.5 Primed chart, `clsP_tie` (2048-2088).** Statement exact. The chart, class bijection and reading are argued directly. The value, rationality, integrality and norm clauses are obtained by "apply the value and metric arguments under supplier 9" with no pinpoint. The weight bookkeeping (2077-2082) is right. Gap: delegation.

**4.1.6 `val_tied` (2090-2118).** Statement exact (arbitrary tuple, `ReadsK` and `IdY`). The complex and rational parts are complete. The integral part is an outline in ten lines: semilocal basis, transported Weyl formula, basis independence, one denominator. The formula is attributed to supplier 8 (2111) but is the Weyl section's `transportedLattice_localization_free_le_coefficientSpace`. `levOk_twists` and `IsPtOf.of_extTo`, both direct dependencies, are not mentioned.

**4.1.7 `ipV_norm_tie` (2119-2129).** Statement exact; note that Lean needs only `IdY`, not a read chart. The inner-product half is complete (`ipVal_step`: unitary change of orthonormal frame, determinants of absolute value 1). The norm half restates the skeleton of `norm_step` and `majAt_step` in three sentences. It rests on `majAt_classSum`, `LatGood.hasRatBasis` and `LatGood.step_gram_posDef`, none named or proved (458 dominated lines).

**4.1.8 `dilTied` (2131-2172).** Statement exact, including `FunKilled` and `IdV`. The point computation is complete. Depends on supplier 8 for the identification of the functional. "Rational transport leaves the framed coset in its own frame unchanged" (2163-2164) is `cosetIn_smul_unitary` (`CouplingCosetFramesInvariantRationalUnitary.lean:11-107`), not cited.

**4.1.9 `til_ties` (2174-2264).** Statement exact: five premises, conclusions `z0`, `TilBaseLat`, `EvzTie` with identity `e`. I checked the three decisive steps. (i) `s = π̄` works for either convention of the Hermitian form. (ii) The cancellation of `red_P(s)` is valid because `P` divides `π` and not `π̄`. (iii) The last column of any allowed extension is forced because `π` is a unit in the adele ring. No gap found. Not compared line by line with the Lean file.

**4.1.10 `stepBefore_oneLevel` (2266-2401).** Statement exact. The description of the symmetric group at 2347-2372 agrees entry for entry with `InJSym` (`DefsSym.lean:20-25`): order `p`, unit diagonal below `r = k+2r_S+1`, the exceptional zero at column `k+r_S`. The character at 2382-2389 agrees with `lamSym = lamJ ψ χ (rSym) t nb k` (sum over `x+1 = y < r`, `y ≠ k`; `i` determinant blocks). The orbit set `Y_b = ∐ J.U/K_β.U` gives all four orbit clauses. Complete.

**4.1.11 `glev_zero`, `levels_top_row_sym`, `chart_gLevH` (2403-2541).** Statements exact, including the `GLev` parameters `(k, t, 0, k, N(0), false)` and the flags `true`/`false` of `HSym`. Arguments complete. In `chart_gLevH` the hypothesis `IdG` is unused in Lean, as in the text.

**4.1.12 Assembly of supplier 1 (2543-2600).** Every direct dependency of `formsTiedSym_std` is addressed: the twelve entries above, supplier 6, the five supplier 8 results, `charts_funKilled`, `readsK_one`, `period_conj`. The period embedding is taken from `ch_P_r11.tex:961-1001`, a passage R11 did not review; the same construction is at `ch_P_r12.tex:1003, 1297` in the other reviewer's scope. `(F u).gl = G` literally for all `u`, so the equality clause is immediate.

### 4.2 Supplier 7

**Statement (2602-2617).** Hypotheses exact (`l0`, `inQ ↔ UnderQ`, `H`, `F`, `StdF ∧ StdLvC`, `CarH`). The opening sentence names only `T, J, W` and the top-point clause. The Lean conclusion also has `TwChMu0 T`, `I.StdW W` (nine fields: `eCls0`, `eY`, `lat`, `eVT`, `eFv`, `reads`, `top`, `topk`, `killed`) and `Nonempty (SymmetricTwistedJointForms T F)`. All are addressed later (3467-3502), but they should be in the statement.

**4.2.1 Diagonal twist (2619-2647).** Exact, including the degenerate case `Q = ∅`. Complete.

**4.2.2 Block extension and top chart (2649-2722).** `pointOverX_has_adelicPoint_blockExtend_mul`: the three hypotheses on `k`, the `K1` membership and the diagonal form of `t` match; the computation is complete. `chart_lastStep_twistBasePoint`: all six conclusions are named (reading with common `k_0 t`, extension property, `TopBase`, `Uloc` equality off `Q`, finite exponent, character agreement). The construction of the level and its double-coset bijection is delegated to "the generic two-point and congruence arguments of supplier 9" (2703-2709). The recovery of the old level in the `k_0` frame (2684-2693) is brief.

**4.2.3 Type-prime lift and coset matching (2724-2796).** Both statements exact. The coset argument is complete: `y = s_G^{-1}`, reduced set `y_w B_w`, equivalence under `h_0 = y h y^{-1}`, trivial twist factor.

**4.2.4 `exists_conj_referenceChartIndex` (2798-2919).** Statement exact. **The hand proof is not the Lean proof.** Lean (`ExistsConjReferenceChartIndex.lean:34-136`) shows that every index on either tuple has the identity double coset (`cosetOne`, through `twSurjG`) and that reference indices exist (`idx_nonempty`, through `twNonVanG`). Those use the first-unfolding classification (`ReductionExistsInLatticeStabilizerHolds`, `ResidueFieldUnfoldingClaimsHold`, `BlockTriangularMulVecMemPartialFlag`), 5,045 dominated lines. The text avoids all of it by an induction that transfers the tuple's `nonvan` witness to the reference tuple and calls the reference `surj` once. It says so at 2804-2811 and 2889-2891.

I checked the new argument against the definitions and find it correct:

- `E1at = Loc.E1 (cst.psi P) (valsQ q A B) (q^B)^{-1} (omPhi ...)` and `Loc.om μ v sq g₀ h Φ x = μ(det g₀) μ(det h)^{-1} sq^{...} Φ(h^{-1} x g₀)` (`TwistedEisensteinNonvanishing.lean:143-169`). The tuple enters at a generator prime only through `cst.psi`, `cst.muq`, `cst.sq`, `A`, `B`. The kernel `PhiGS` depends on `q`, `psi0P Ch`, `chiP Ch` and the ranks only.
- The prefactor is constant in the summation variable. It is nonzero because the determinants of lattice stabilizers are `P`-units, so the exponent of `muq` and of `sq` is zero.
- On the support, `q·chArg` is integral (`intAt_chArg_G`), so the law `psi0` makes the phase tuple-independent.
- Invariance under the source double coset is Lean's `unfoldedDatum_ne_zero_of_doubleCoset_source` (`UnfoldedDatumNeZeroIffDoubleCoset.lean:171-292`), stated for general `a₂ = r a₁ κ`, as the text needs.
- The induction closes: the hypotheses of `ChIdx.Ok.surj` are `stabG` at generator primes, an empty non-generator clause on the reference tuple, and a reference predecessor at every `P`.

Gaps: (i) the tuple-independence lemma is new mathematics relative to the Lean development and is not marked as such in `status.json`; (ii) the text says the prefactors are "constant in Y and nonzero" but should state that both sums are taken with the same `A', B'` and that `sharp = true` on both tuples (`Ok.sharp`); (iii) the degenerate index `none` of `Idx` at `i ≥ 1` is not mentioned (trivial).

**4.2.5 Middle chart on a fixed fibre (2921-3083).** `chart_of`: hypotheses `k1, k2, k3`, the fibre predicate with `bar` and `cqOf`, and all six conclusions match. The orbit and stabilizer arguments (2932-3001) are complete, and the CRT construction (2959-2976) is correct. The realization of the level as a `StepLevel` (3003-3045) is an outline that again invokes "the same componentwise argument as in supplier 9" and "the arbitrary-depth congruence correction of supplier 9". The conjugation by `k` (3047-3065) is complete. Hypothesis `k2` leaves `k` unconstrained at generator places when `a ≠ μ₀` and at `UnderQ` places; "off the exceptional places" at 3053 should say which places are meant. `exists_charts`: the text names the wrapper `GlobalTheory.T.exists_finiteOrder_charts_middle_steps`; the registered entry is `ChExM.exists_charts`, 450-499.

**4.2.6 Level character off the twist places (3144-3189).** Statement exact. The character `χ(x) = χ₀(ψ(x)) η(x) η(ρ(x))^{-1}` is a homomorphism, agrees with every chart character on common elements, and agrees with `χ₀` on elements trivial at `Q`. I re-derived both identities. Complete.

**4.2.7 Further-place character (3191-3287).** Statement exact: `ChiFin` is finite exponent on elements trivial at `badG` (`LiftsInvOne.lean:49-51`); `valV` is the `σ₀`-image of a product over marked primes of a chosen near-pair value (`NearPair.lean:36-38`). The proof is direct and differs from Lean, which goes through `AdT.lev_mid`, `exists_stepGroupElement_of_chartLevel`, `stepNearLifts_component_mem_localChartGroup` and `penultimateChart_localGroup_mem_nearLevelSet` (2,846 dominated lines; none is a review entry, and unlike 4.2.4 the text does not say the route differs). The argument is sound:

- the `e`-th root near the identity by `exp(e^{-1} log B)`;
- density of `GL_n(E)` in `GL_n(E_P)` for the rational `d`;
- the reading applied to `b` forces `h = 1`, `θ_{P'} = 1` for `P' ≠ P`, `θ_P = d^{-1}`;
- depth invariance of `λ_P` makes `valV` independent of the chosen near pair.

Gaps: convergence radii of `log` and `exp` are not stated; uniqueness of the marked prime over `v` relies on the disjointness statements of 3.2.

**4.2.8 Generated group, finite index (3271-3330).** Statements exact, including the empty-family case, which Lean needs because `W` must contain a principal congruence subgroup. The finite-index argument (action on `L/NL`, kernel inside the chart group, no normality) is correct.

**4.2.9 Penultimate coupling (3332-3411).** Conclusion `Nonempty (TwLevJ ...)`. The fields `levJ`, `Yb`, `yb_orbit`, `lb`, `le`, `stab`, `chiJ`, `chiJ_eq`, `J_g` (`ChartWiden.lean:51-79`) are all addressed, but the text does not enumerate them. The Hermitian level `H₀` is obtained from "the local calculations in confirmed supplier 2, applied to this level" (3338-3341). That is a re-use of an argument, not an application of the supplier 2 theorem, and should be marked as such. The joint injectivity of the two maps on `Y_b` (3391-3395) is correct.

**4.2.10 Assembly of supplier 7 (3413-3509).** Follows `twPack_ex` and `tw_chains`. The finite-exponent hypothesis is discharged correctly in both cases (3459-3462), consistent with the definition of `ChiFin`. `TwChMu0` gets one sentence (3499-3500) for `eCls0_mu0_eq_self`. `SymmetricTwistedJointForms` gets one sentence (3497-3499).

### 4.3 Assembly and root (3511-3577)

`colsTiedSym_std`. The text follows the Lean term step by step:

- supplier 1 gives `Ch, chOf, F`;
- supplier 2 takes those;
- supplier 3 is applied per word and rewrites `Lb, Uloc, U, y, stabI, splitG, frG`;
- `CarH` is rebuilt from `car0, sp, fr0` after substitution;
- supplier 4 acts on this `H, F`;
- `hT.piU` converts supplier 3's annihilation into supplier 5's hypothesis;
- supplier 6 gives `StdTied`;
- the two word-independence identities come from `StdF.fr0` and `StdF.frP` being 1;
- `gl_const` and `chi` come from supplier 1.

`colsTwPTiedS_std`. `underQ_iff` and `hxi` give `InQ' ↔ UnderQ`. Supplier 7 takes `C.herm.base`, `C.forms`, `carH_of_cols C`. Supplier 8 takes `T, J, W`. Supplier 9 takes `Lv` and the top-point clause `hPt`. The record is assembled without reselection. Exact.

Root. `perDecTwT_of_std` (`PerDecTwTOfStd.lean:11-44`) gives, for each class, a field element with the classwise pairing as image and non-negative valuation at allowed places, from `RowInt.tw`, `Lsh_eq_N` and `classPairing_integral_form_row_isIntegral`. The paragraph at 3546-3569 is the same argument followed by the class sum, as in R5. One remark: `pair_integral` is where the Weyl duality enters, so the root depends on the Weyl section even outside the nine suppliers.

### 4.4 Disposition (3578-3616)

The table is accurate: 57 entries, counts 1+8+10+16+15+5+2. The text does not claim closure and keeps 13 of 20 complete, consistent with `status.json`. The sentence at 3606-3613 about the reference witness is confirmed by the graph (section 2, reason 3).

## 5. Prioritized corrections

1. **Label the stage and base law block.** State where `stp_ok` enters (`step_gam_mem_UJ`, inside `upNatTie`), that only `.unit` is used, and that it is `ufGL_conjTranspose_mul`. Record the remaining 3,832 dominated lines as "in the Lean cone, not needed by the hand proof". State that `fields_ok` and `primes_ok` (about 650 dominated lines) are used as known facts about the base data, or prove them.
2. **`exists_conj_referenceChartIndex`.** Mark in `status.json` that the hand proof replaces `cosetOne`/`idx_nonempty` and does not reproduce `twSurjG`, `twNonVanG` (5,045 dominated lines). State the tuple-independence lemma as a separate lemma with its hypotheses: same `A', B'`; `sharp = true` on both tuples; determinants are `P`-units, so the `muq` and `sq` exponents vanish.
3. **Further-place character.** Say that the proof is direct and does not follow `lev_mid`. Either register `exists_stepGroupElement_of_chartLevel`, `stepNearLifts_component_mem_localChartGroup` and `penultimateChart_localGroup_mem_nearLevelSet` as bypassed (2,846 dominated lines), or prove them. State the radius on which `log` and `exp` are used.
4. **Replace "by the generic argument of supplier 9" with pinpoint references** at 2073-2074, 2703-2709, 3031, 3038-3041, naming the declaration and the label of the paragraph applied.
5. **`ipV_norm_tie`, norm half.** Prove or label `majAt_classSum`, `LatGood.hasRatBasis`, `LatGood.step_gram_posDef`.
6. **`val_tied`, integral half.** Correct the attribution at 2111 from supplier 8 to the Weyl section. Name `levOk_twists` and `IsPtOf.of_extTo`. Write the basis-change step.
7. **`exists_charts`.** Enumerate the `StepLevel` fields and check them off. Say explicitly that the chart is rebuilt with the canonical functional (Lean: `charts_funKilled`) and that `ReadsK` and the `yStd` equality are unchanged.
8. **Register the unlisted hand-proved theorems** of 3.4, at least `charts_tuple_trivQ`, `twPack_ex`/`tw_chains`, `twAtT_exists`, `charts_funKilled`, and `period_conj`.
9. **Supplier 7 statement.** Add `TwChMu0`, `StdW` with its nine fields, and `SymmetricTwistedJointForms` to the opening statement. Enumerate the `TwLevJ` fields in 3332-3411.
10. **Twist-place disjointness.** Cite `twistPlaces_prime_to_levelAndTypePrimes`, `not_twistPlace_referenceTuple`, `twistPrimes_reference_tuple_eq_empty` where the text assumes them (2620-2621, 2685, 3200-3203).
11. **Minor.**
    - `stM_range` range is 355-366.
    - `exists_conj_referenceChartIndex` statement range is 7-16.
    - `ipV_norm_tie` needs no read chart.
    - "Three hypotheses of `cls_bij`": say that the third is a section variable.
    - 3338-3341: say that supplier 2's argument is re-used, not its theorem.

## 6. Summary

- All 33 declarations in scope have statements that match Lean. 19 are CONFIRMED, 14 are CONFIRMED WITH GAPS (two of those are the supplier roots), none is NOT CONFIRMED. Both assembly theorems and the derivation of the root from the nine suppliers are CONFIRMED.
- The text is faithful to the Lean development in every place I compared directly, down to index conventions and character exponents. I found no incorrect step.
- Two hand proofs take a route different from Lean: the reference chart index (a new tuple-independence argument replacing the first-unfolding classification) and the further-place character identity. Both check out against the Lean definitions; the first needs to be stated as a lemma and marked as a deviation.
- The largest unlabelled piece of the root cone is the stage and base law block, 4,485 dominated lines. The hand proof needs one definitional field of it.
- Several paragraphs are outlines that delegate to supplier 9 or supplier 8 arguments without a pinpoint. My verdicts depend on the other reviewer for the adelic point, eight supplier 8 results, three supplier 9 results, the `RowTie` arguments, and the Weyl localization formula.
- **Z4.4: CLOSE AFTER LISTED FIXES**, provided the other reviewer confirms suppliers 4, 8, 9, the Weyl duality and the adelic point. Fixes 1-4 are required before closing; 5-11 are improvements of the same kind R11 accepted under "confirmed with gaps".
