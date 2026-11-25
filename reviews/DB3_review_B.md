# DB3 review B: round-3 outline notes, OVERVIEW, track READMEs, procedures
AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved
Independent referee report. Scope: 17 `*_round3.md` outline notes, `OVERVIEW.md`, seven `tracks/*/README.md`, `notes/formal/procedures.md`, checked by reading against the pinned Lean source (commit `40e56bab`, `${LEAN_PROJECT}/src`). Nothing was built or run in Lean; no network. All Lean paths below are relative to `src/`. This report does not assert, and nothing in it should be read as asserting, that RH is proved.

Abbreviations for long paths:
- `GR/` = `Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/`
- `TPS/` = `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/`
- `DTC/` = `Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/`
- `AV/` = `Development/AutomorphicArithmetic/AutomorphicVarieties/`
- `SWF/` = `Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/`

## 0. Cross-cutting finding (affects every note that names a classical theorem)

The pinned Lean development has **no hypotheses at the top** (`Main.lean:4`, `riemannHypothesis : RiemannHypothesis := rhOfAll`) and I found no `axiom`/`sorry` by grep. Every literature-named statement is a `Prop` *defined inside the repository* (namespace `GlobalTheory.Published.*`, `UpperTheory.V.Published.*`, ...) and is *inhabited by an in-repository proof term*. Concretely:

- `TPS/EveryCharacterOfLiteratureOfVWin.lean:219-809` contains 176 theorems named `..._of_literature (O : OpenLiteratureStatements)`. Almost all ignore `O` and return a closed constant, e.g. `howe_duality_real_of_literature O := GlobalTheory.howeDualityReal_holds` (line 437-438), `kawamata_viehweg_of_literature` (447-448), `green_regular_characters_of_literature O := PositivityTheory.Stage1.PM.greenRegularCharacters` (399-400), `siegel_weil_std_of_literature O := PositivityTheory.SiegelWeilFormula.Fin.siegelWeilStd` (563-564). `O`'s three fields are used only at lines 284, 286, 618.
- The same pattern holds for `OpenImageCondition` (`DTC/TemperedProductOfSquareIntegrable.lean:207-208`, one field) and its `..._of_open` theorems (e.g. `jacquet_shalika_of_open`, 297-298; `clozel_purity_of_open`, 279-280; `global_artin_reciprocity_of_open`, 225-226).

Consequence for the notes: at a *unit head* a classical result is often a hypothesis or a structure field (so "assumed input at this head" is right), but on the route to `allChi` it is discharged by a Lean constant, not assumed. Whether each in-repo `Prop` faithfully states the classical theorem is a separate, unchecked question, and in at least three cases examined here the Lean statement is demonstrably a variant (B04 local parameter; P010 local-global compatibility; W11 class-group rank). No note states this two-level status uniformly. This is the single most important systematic gap.

## 1. Summary table

| Item | Verdict | Most serious issue |
|---|---|---|
| B04 | FAITHFUL WITH GAPS | "Good cuspidal" is never defined (`GoodCusp`: rank 1, or twist of a depth-zero class over a field isomorphic to Q_p); note does not say outright that `RecTExists` is not the local Langlands correspondence. |
| P010 | FAITHFUL WITH GAPS (statement description weakened in a misleading direction) | Local compatibility field described as "compares the local Weil-Deligne data"; Lean `AwayB` gives only equal dimension, equality in the toral monodromy-free case, and inertial char. polys in a tame squarefree large-p case. |
| P011 | FAITHFUL WITH GAPS | The ~590-line, 176-theorem "literature" layer and the ~45 literature-named inputs inside the window supplier are presented as a one-sentence hand-off. |
| P026 | FAITHFUL WITH GAPS | Two `Nf` hypotheses mis-stated/omitted (`wt` holds only up to a power m; `ne` omitted); 19 further named inputs of `glue2` glossed as "remaining compatibilities". |
| W08 | FAITHFUL WITH GAPS | `linkedUnlE_alt` (13 inputs) presented as one routine item; Kato vanishing is a hypothesis at this head, not labelled. |
| W09 | FAITHFUL OUTLINE | Minor: `main_big` internals not verifiable from the outline. |
| W11 | FAITHFUL WITH GAPS | The deep input `memZ` (group-ring containment, the mu=0 content) is not named or located; note never says Lean proves, rather than assumes, the statement, nor that the root-of-unity hypothesis is entirely unused. |
| W13 | FAITHFUL OUTLINE | Minor: `countIV`, `countVs` unnamed; two numerical constants unverified by me. |
| T09 | FAITHFUL WITH GAPS | Record fields (Casselman-Wallach, Harish-Chandra, doubling, ...) not labelled as assumed fields; two cited names are not the ones in the head term (wrappers). |
| T11 | FAITHFUL OUTLINE | Minor: "inert Howe duality" etc. are Lean constants, status not stated. |
| T12 | FAITHFUL WITH GAPS | Continuation (`EisBL`), `HolLead`, `AbsThm`, Siegel densities and Siegel-set inputs are substantial and unnamed; literature status absent. |
| T15 | FAITHFUL OUTLINE | Minor: head calls wrapper `uniform_lower_bound_of_sums'`; flat-degree supplier is `flatDeg_of_scholzeWeinstein_of_prints`, name omitted. |
| T17 | FAITHFUL WITH GAPS | No statement that the Lean `MoriwakiBigStatement` is a bespoke formulation proved in-repo (`moriwakiBig_outright`), nor that resolution and Poincare-Lelong are in-repo constants. |
| P001 | FAITHFUL OUTLINE | None of substance. |
| P003 | FAITHFUL WITH GAPS | Primitive predicate `ZeroFreeAll` has no pole exception (it includes N=1, s=1, relying on Mathlib's totalized value); not disclosed. |
| P005 | FAITHFUL OUTLINE | None of substance. |
| P009 | FAITHFUL WITH GAPS | `formB` (Landau window criterion) mislabelled "slope bound"; `allChi` is an alias, not an "application". |
| OVERVIEW.md | NEEDS CORRECTION | Does not say V has no human-readable proof; later paragraphs read as an unconditional proof narrative; the 31 list A-C implications are not quantified; no sentence on the Lean/paper distinction. |
| tracks/local | NEEDS CORRECTION | Cites Scholze's LLC against B04 without saying B04 is far weaker than, and not, the LLC. |
| tracks/theta | NEEDS CORRECTION (minor) | Calls T12 "the doubling formula"; it is a Siegel-Weil statement. |
| tracks/galois | NEEDS CORRECTION (minor) | W11 called "the classical bound"; no literature line for it; P011 (galois primary) missing from path. |
| tracks/analytic, arakelov, formal, ktheory | ACCEPTABLE WITH IMPROVEMENTS | None says in-page that the main deduction is conditional and V, F unproved on paper. |
| notes/formal/procedures.md | COHERENT | Commands and numbers consistent; paths assume a private directory layout. |

## 2. Per-note sections

### P010 (priority)

Lean: `UpperTheory.FinalTheorems.everyCharacter`, `Development/AutomorphicArithmetic/CharacterBoxes/MainConclusion.lean:10-11`.

1. Statement. The Lean declaration is hypothesis-free: `everyCharacter : EveryCharacter := everyCharacter_of_row Gal.Int.galoisLocalGlobalStrong_recParameter`. The note describes the conclusion correctly but never says in one plain sentence that the Lean theorem has no premises. Add it.
2. Row type (`GR/TypeConditions/WeightsConjBis.lean:69-73`): binders and order are reported correctly (E CM, Omega, l, iota, a >= 1, pi, chi over the maximal real subfield, `IsRegAlg`, `PolarizedPair`, then one existential triple `r, wt, HT` with `PropsB`). Six fields of `PropsB` (54-67): correct count and names.
3. **Weakened description.** The note says the `away` field "compares the local Weil-Deligne data of the representation with the parameter of the local component". The actual content is `AwayB` (same file, 26-31):
   - `dim`: equal dimensions;
   - `tor : Tor y -> y.mono0 -> x = y`: equality only when the target parameter is toral and has zero monodromy;
   - `tame0 : IsQpBig w y.lpDim -> TmW y -> Sqf y -> y.mono0 -> x.mono0 ∧ (char. polys agree on degree-0 Weil elements)`, where `IsQpBig` (15-16) needs the completion to be Q_g with `n = 1 ∨ 16 n^2 < g`.
   This is much less than local-global compatibility. A reader in the field will assume the Caraiani-type statement; the note must spell out the three clauses. In addition `rc` ranges over *every* map satisfying `IsRecT` (line 58-59), and `IsRecT` does not pin the map outside "good" classes (see B04).
4. Row0 -> Row0b (`Props.big`, 75-82; `Row0.row0b`, 84-86). The note says the operation "forgets some of the stronger conditions and restricts the remaining tests". Nothing is forgotten: `Away` and `AwayB` have the same three fields (`WeightsConjAlt.lean:35-40`); the only change is strengthening a hypothesis from `IsQp` to `IsQpBig` in `tame0` and in `AboveB.nice`. Reword.
5. Outline fidelity. The term chain is reproduced accurately and in order: `RowSrc.lean:6` -> `GaloisRepresentationsOfThetaLift.lean:6` (with `Geo.geoOne_holds`) -> `Development.lean:30-31` -> `27-28` (`seedFinOdd_of_geoOne geo`, `congFinOdd_of_ex Wt.wtLacEx_holds`) -> `coreAll_of` (20-22: `toCoreK up congPhi_holds descOffT (limFinOdd_of seed cong)`) -> `rest` (24-25: Iwahori input derived from the spherical one on the same core). I confirm each of these.
6. Unnamed inputs. The note says "weight result", "descent, closed-trace and limiting steps" without the Lean names: `UpperTheory.Gal.Wt.wtLacEx_holds`, `UpperTheory.Gal.ClosedPhiFromClosedTrace.congPhi_holds`, `UpperTheory.Gal.Desc.descOffT`, `UpperTheory.Gal.Lim.limFinOdd_of`, `UpperTheory.Gal.Int.Geo.geoOne_holds` (`.../GeometricFlagBases/WeightOneGeometricRealization.lean:11`), `UpperTheory.TP.tLift_holds_k`. All six are closed Lean constants; the unit card records 9,567,042 dominated lines under this two-line head, so none of them is routine.
7. Literature. The row is the in-repo analogue of "Galois representations attached to regular algebraic polarized cuspidal representations over CM fields, with local-global compatibility"; the receiving record even names its fields `caraianiLocalGlobalDual` and `galoisRepOfPolarizedPairLit` (`EveryCharacterOfLiteratureOfVWin.lean:215-218`). The note names no classical theorem. It must say: (a) Lean does not assume this; it claims to construct it from `GeoOne` (`HodgeTrAt.lean:79-`, odd rank, weight-one geometric realization) and a theta-lift statement `TLiftK` (`ThetaParseval/HalfIndexLattices/TLiftK.lean:12-`); (b) the Lean statement is the weak variant of item 3.
8. Not checked: definitions of `CuspSub`, `PolarizedPair`, `IsRegAlg`, `IsLocComp`, `wdOf`, `LocTied`, `AboveB` semantics; the `.tex` excerpt and paper page.

Verdict: FAITHFUL WITH GAPS; item 3 borders on misleading and must be fixed.

### P011 (priority)

Lean: `everyCharacter_of_row`, `MainConclusion.lean:7-8`: `every_character_of_literature_of_vWin ⟨h, recTExists, h⟩ (vwin_of_row h)`.

1. Statement: one explicit premise `h : Row0b (fun h rc => IsRecT h rc)`, conclusion `EveryCharacter`. Correct in the note. `One.M.Row` is definitionally that row (`.../SatakeParameters/RecT.lean:6`); the note's claim that fields 1 and 3 share a type is correct.
2. VWin quantifiers (`CharacterBoxes/ExistsPageN.lean:12-17, 41-49`): the note's order (eps, page selector e, then J >= 1, X0, then X, pair (q,d) at scale X^{1/J}, then Y with X^{1/J} <= Y, Y^2 <= X, then all x in [Y,Y^2], all fields E with `IsChiField`, all closures and local data, finiteness for 0 < e < t and the sum bound over every finite S) is correct. The note omits the budget itself, `sqrt(exp(x^eps))` (line 42), and the content of `WinPair` (27-37: q ≡ 3 mod 8, d ≡ 7 mod 16, q | d+1, every odd prime p <= Y^{eps/5} divides d+1, size windows for log q, log d). Since V is vacuous at any X with no such pair, the note should say where pairs are produced.
3. Steps presented as routine that are substantial:
   - `every_character_of_literature_of_vWin` (`...OfVWin.lean:810-813`) is described in one sentence. It calls `UpperTheory.Lit.every_character_of_theta_integrals_local_matching` (`TPS/SiegelEisensteinSecondTermHypotheses.lean:69-74`) with seven arguments built in lines 219-809 of the same file (176 theorems). That callee in turn calls `Top.every_character_of_green_v_win` with Green supplied by `GreenBridge.green_of_regular P.greenRegularCharacters` and the geometric witness by `nonempty_hyps_definite_side_of_closed_bound` (same file, 43-68, about 25 lines combining ~20 named results). The note does not name this callee or Green at all.
   - `vwin_of_row` (`DTC/VwinOfRow.lean:4-5`) -> `automorphic_window_of_inputs` (`DTC/TopMainZj.lean:71-74`) -> `v_window_of_depth_zero_residual_bc_cm` (55-58) -> `UpperTheory.V.v_window_of_literal_automorphy_n` with four bundles assembled at 18-70 (18 local, 15 automorphic, Galois-cohomology, 11 CM fields: Bernstein-Zelevinsky, Jacquet-Shalika, Clozel purity, global Artin reciprocity, de Rham => potentially semistable, Siegel-Klingen/Deligne-Ribet, Hecke-Tate, Grothendieck deformation, ...). The note says only "That theorem supplies the CM abelian inputs".
4. Unnamed input: "the named base-change result" is `UpperTheory.BaseChangeIdentities.baseChangeN : BaseChangeIsobaricN` (`Foundations/BaseChangeIdentities/DefiniteNHolds.lean:5`), a closed constant.
5. Literature: see section 0. The record name `OpenLiteratureStatements` suggests assumed literature; in `everyCharacter_of_row` its three fields are filled by `h`, `recTExists`, `h`, and the other ~170 named results are in-repo constants. The note should say so. The middle field `localLanglandsExists` is filled by B04's weak statement (see B04).
6. The closing caution ("the source claims to derive that full window from the row through P013") is accurate and appropriately worded.

Verdict: FAITHFUL WITH GAPS.

### P026 (priority)

Lean: `UpperTheory.V.Z.Kato.Final.zetaUr`, `AV/ModularityArgument/KatoQuadraticCharacters/UnramifiedZeta/ZetaUr.lean:9-12`; statement `GlobalTheory.Ord2.ZetaUr`, `Development/AbelianVarietyTheory/Statements/CuspidalUnitaryTwists/ZetaUr.lean:18-20`.

1. Statement. Binders and conclusion `ES W A` are right; the conclusion's "no scalar a with y_2(s) = (W_22(s) - 1) a on the decomposition group" matches `Gr` (`.../Definitions/Foundations/FinalTheorems.lean:72-73`) and `es_of_sys` (`IsLocallyConstantCycMod.lean:46-48`). Hypothesis discrepancies against `Nf` (`FinalTheorems.lean:53-66`):
   - `wt : ∃ m ≥ 1, ∀ s ∈ inertia, (W_11 s)^m = eps(s)^(e m)`. The note says "the specified first inertia character"; the Lean condition holds only up to a power m. Weakened in Lean, strengthened in the note.
   - `ne : ∃ s ∈ Dec, W_11 s ≠ eps s` is omitted from the note.
   - `SrcUr` (lines 13-16): the auxiliary character must satisfy `KillsMu l chi`; the note's "finite-character twist" should state this condition.
2. Outline fidelity. Top term: `zetaUr_of_halves2 _ (kato_global_unit_law_of_smoothed_classes K4.kato_eulerSystem_integrality K5.smoothedZetaClass_hodgeTateLaw exists_admissible_hecke_projection_nonvanishing) C7.pLocu`. The note's "three principal inputs" are exactly these three. Tuple `(c, y, S', nu, chi, Z)` and the four properties `Sys ∧ IwSys2 ∧ SpLink ∧ Pin7` match `ZetaElementsUnramifiedOrdinaryOfEulerSystemInert.lean:20-26`; the universal local half matches 28-34; assembly 36-46 is as described.
3. Local half (`Foundations/IwahoriReduction/LangPolynomials/NormFactorLeOne.lean:99-157`): I followed the proof line by line and the note's sequence is correct: contradiction hypothesis; `h50` gives W_22 = 1 on cyclotomically trivial inertia; `SpLink` gives `SpZero`; restriction to inertia (`hI`); Frobenius conjugation law via `conj_law` (76-98) and `pFrobEx`; `pCore` yields the series and relations; `h48` gives the nonzero test; `hint` the vanishing; evaluation at `max r₂ r₃` and the same primitive root.
4. Substantial inputs not named:
   - `h48 = GlobalTheory.T.nonvanishing_transfer_characterSums_powerSeries` and `h50 = GlobalTheory.T.quotient_char_trivial_inertia_cyclotomic_tower` (`NormFactorLeOne.lean:162-164`); `pCore`, `pFrobEx`, `norm_factor_le_one`. The note says "the transfer theorem" and "the pinned local power-series comparison".
   - In `kato_global_unit_law_of_smoothed_classes` (`.../FrobeniusHodgeTateLaws/KatoGlobalUnitLawOfSmoothedClasses.lean:8-10`) the term is `glue2 h4 h5 (...) towerEx ordinaryEisensteinEigenfunctional_exists meas3 jEx coefUb mono psiEx frobU detIne hatW pinOf smNz gmEx explSmul avgEq avgMF rhsEq smSys chiFix`: 19 further named inputs beyond the three principal ones. The note calls them "the remaining tower, coefficient, Frobenius and averaging compatibilities". At least `pinOf` and `smNz` produce the `Pin7` nonvanishing clause that the whole local argument consumes (`HTPresNuOfPolys.lean:24-36`, last clause), so they are not bookkeeping. The directory holding them has 3,698 lines. Name them and say which one yields the final clause of `Pin7`.
5. Literature. "Kato" appears only via Lean identifiers. `KatoEulerSystemIwasawaClassStatement` (`.../SmoothedZetaClassHodgeTateLawStatement.lean:11-`) is a bespoke cocycle-level statement (towers, `AdmWn`, coefficient rings), not a published theorem verbatim, and it is *proved in-repo* (`UpperTheory.Kd.K4.kato_eulerSystem_integrality`), not assumed. The note must say both. I do not vouch for any Kato numbering.
6. Not checked: `Tame`, `Unr`, `Z1 (Loc.colRep W)`, `Newform.Att`, `HTLawCsOfCoef`, `Layer2`, internals of `glue2`.

Verdict: FAITHFUL WITH GAPS.

### W13 (priority)

Lean: `UpperTheory.V.HV.vwin_of_counts`, `AV/HeightAndVanishing/JointWinOfCounts.lean:30-33`.

1. Statement. Hypotheses in Lean: `PoitouTateDuality`, `LocalFinitenessK`, `LocalTateDualityK`, `LemmaK CK`, `ThmBab K 401`, `ThmBcFree`, `CountI`, `CountII`, `CountIII`, `CountV`, `CountZ`; conclusion `VWin`. The note lists exactly these eleven. Correct.
2. Outline fidelity, confirmed against source:
   - `pointHV_of_counts` (16-18): `point (sumIn h2 h5 (countVs hP hF hT CK hK) countIV) (sumOut h1 hZ h2 h3)`. The note's split (outside B_chi: I, Z, II, III; exceptional primes: II, IV, V) is right. `PointHV` budget `(N t)^C + C B` (`LayerLe.lean:39-44`) is right.
   - `thmHV` (`ThmHV.lean:6-40`): B = exp(x^{4 eps/5}) at line 37, correct.
   - `jointWin_of` (`AV/PrimeSetBoundDataOfPrimitiveChar.lean:145-156`): Y is obtained once from `ThmBab` (line 152 in file) and passed into the `ThmHV` implication (153-154); the threshold is the sum of the list `[psi.N, ordC, pK, hStar, pOne, r1, r2]`. The note's central claim ("binds Y once") is correct.
   - `vwinAt_of_joint` (`AV/CMFieldExponentialBounds/AdmissibleOfPageN.lean:41-129`): J' = max(J,1) (line 51), thresholds combined by maxima (55-60), `vvle_of_parts` with budget `B2 log 2 + Bm + Bp` (`AV/LengthEqAddEigen.lean:127-128`). Correct.
   - `thmBc_iff` (112-134): used in direction `.2 hc`. Correct.
3. Minor gaps: `countIV` and `countVs` are closed/derived Lean results not named in the note; the specific constants "log(N t) <= 2 x^{eps/4}" and "K exp(8 x^{eps/4})" come from `log_conductor_mul_height_le_of_pageN` and `minusBound_le_exp_of_log_le`, whose statements I did not open. Not verified.
4. Literature: Poitou-Tate, local finiteness, local Tate duality are genuine hypotheses at this head. The note's "Fix..." is acceptable; "assumed at this head" would be clearer.

Verdict: FAITHFUL OUTLINE.

### T12 (priority)

Lean: `PositivityTheory.SiegelWeilFormula.Fin.siegelWeilStd`, `SWF/SiegelWeilStandard/SiegelWeilStd.lean:8`; statement `GlobalTheory.ThK.Dbl.SiegelWeilStd`, `Development/WeilBound/ThetaLifts/LatticeBasics/HypothesesS.lean:11-21`.

1. Statement. All hypotheses are reported: good base, m, n >= 1, `min r s = 0` for A, opposite Hermitian/skew types, Hecke character with `ResEtaPow ... m`, `IsDbl` (fields `rat, weil, lin, adm, kill, fix, theta`, `Hypotheses2.lean:62-74`), frame/standard K/height, Haar measure and fundamental domain, Schwartz and K-finite Phi. Conclusion: `EisValueAt` at s0 = (m-n)/2 with multiplier `if n < m then 1 else 2` times the normalized average of the theta sum. The note's display and its reading of the four clauses of `EisValueAt` (76-78) are correct.
2. Outline fidelity. Chain confirmed: `siegelWeilStd := siegelWeilStd_of_ct (Act.ctSplit_of kfour.auxEx kfour.coefEx)`; `ctSplit_of` discards both arguments (`SWF/SiegelWeilActions/CtSplitOf.lean:10-11`), as the note says; `ctSplit_of_parts` takes the max of three bounds and splits the coset sum on the Lagrangian condition (`CtSplitOfParts.lean:137-158`), as described; `siegelWeilStd_of_ct` supplies `TW.Twp.poisson`; `_pre`, `_mid`, `_of` and `Atop.siegelWeilStd_of` (`SWF/FockVacuumBounds/SiegelWeilStdLeaves.lean:40-58`) and `Atop.fieldOf` (`FieldOf.lean:50-63`: case n < m via `Khead.siegelWeilStd_lt`, else multiplier 2 via `hLe`) are as described.
3. Substantial inputs the note does not name (all closed Lean constants):
   - `PositivityTheory.RgEis.Hd.eisBL : EisBL` (`SiegelWeilStdLeaves.lean:44`): meromorphic continuation with growth bounds of the Eisenstein series (structure at `Hypotheses2.lean:55-60`). The note says "separate continuation ... inputs" without name or location. This is a major theorem in its own right.
   - `HSt.holLeadB : HolLead` (`SiegelWeilStdMid.lean:19`), `AbsSt.absThm : AbsThm`, `AbsSt.vacuum_generates_polynomials` (`SiegelWeilStdOf.lean:66-67`).
   - `PositivityTheory.PfSWUS.HMass.siegelDensitiesLowA`, `PositivityTheory.Rg.Base1.densEq` (local density inputs in `whitGenLt`/`whitGenEq`, `SiegelWeilStdOf.lean:43-47`), `GlobalTheory.T.siegel_set_unitary` (39-41), `kunf.unfold`, `Aeis.eisWk`, `Krd.rdEx`, `kfour.lamBd`, `kfour.fourierZero`.
   The "Step" (rank change), built at `SiegelWeilStdOf.lean:63-65` from about 25 arguments, is correctly singled out by the note as the place to challenge.
4. Literature. The note never states the relation to the classical Siegel-Weil formula. Required: Lean proves `SiegelWeilStd` in-repo with no hypothesis; it is the anisotropic case (A definite at the listed signature) in a Darboux/Weil-splitting formalism with a probability-normalized average; whether it coincides with the published theorem (and in which range of m, n the published statement is unconditional) is not established here. The track README attributes the multiplier comparison to "Yamana, Theorem 2" via R21; I cannot see that source and do not vouch for the number.
5. Not checked: `IsGood`, `IsUWeilSplit`, `flat`, `eisTerm`, `thetaSum` definitions; internals of `KWhit`, `AStep`.

Verdict: FAITHFUL WITH GAPS.

### T15 (priority)

Lean: `SelfIntersectionVolumeEstimates.topCovolG_alt_alt`, `TPS/TopCovolG.lean:39-58`.

1. Statement. Seven inputs in the stated order: confirmed (line 39). Table rows checked against the structures: `HypothesesX` five fields `ks, lie, green, sep, fsch` (`Development/AbelianVarietyTheory/Definitions/Divisors/HypothesesX.lean:10-20`); `HypothesesH` four fields `sieg, fan, charts, deg` (`.../SemiposAtOfPositive.lean:216-220`); `Quoted` eight fields (`.../WellChosen.lean:22-30`); `DeepStR` (`Development/AutomorphicSpectrum/Definitions/GlobalGeometry/ModelSmall.lean:63-66`: C >= 0, `m^2 <= k`, `1 <= j < m`, at most 15 prime factors); `VolumeEstimateHypotheses` is the conjunction of `SelfIntersectionBound` and `SmallSectionsInject` (`.../VolumeEstimateHypotheses.lean:11`). All correct.
2. Conclusion. `CovolumeBoundOfX` (`TPS/LiftLambdaBound.lean:60-61`) with `Closed` (`Formalism/SharpRestriction/ParamsHeightRankConstant.lean:159-161`: ∃ eps1 > 0, ∀ eps <= eps1, ∃ K, ∀ Fm CH, class and largeness imply P) and `EventuallyAtAllPoints` (18-19). The note's quantifier order (threshold, transported data, family and H, then C0 >= 0, then scale threshold, then points satisfying `RowsTAlt`, then all C >= C0) is correct.
3. Outline fidelity. The body (42-58) is reproduced step for step: extraction of `sieg, ks, lie`; `covering_gram_of_prints`, `cov_size_bound`, `covering_meas_of_prints`, `anchor_bound`, `covering_deepEx_of_prints`; `deepGood_of_toroidal_and_semiabelian`; flat degree; cover degree; share; `height_lower_bound_general_alt`; `coverHeightSum_...`; uniform lower bound with `sum_c_of_deep_good`; `liftLowBound_of_cover_estimates` with seven suppliers; final `covolX_of_truncation_badSet_lambda_lowBound` with eight lift conditions. The dependence order degree -> share -> height sum is as the note says.
4. Minor corrections:
   - Step 4 attributes the step to `u_low_of_cover_hyps` (`ULowOf.lean:16-24`). The head calls `GlobalTheory.T.uniform_lower_bound_of_sums'` (`TPS/ULowOfStatement.lean:11-12`), a wrapper that closes by `first | exact ... u_low_of_cover_hyps | ...`. Cite the wrapper too.
   - The flat-degree supplier is `GlobalTheory.T.flatDeg_of_scholzeWeinstein_of_prints` (line 50). The note says only "obtained from the Hodge record"; the literature name carried by the identifier should appear, with the usual caveat.
   - `cov_size_bound` and `anchor_bound` are closed constants with no hypotheses ("supplied separately" in the note); name them.
5. Literature. All "Published.*" items are hypotheses *at this head* (correctly presented as inputs). On the main route they are discharged by constants in `EveryCharacterOfLiteratureOfVWin.lean` (e.g. `kawamata_viehweg_of_literature`, 447-448, itself derived from Nadel vanishing and nef numerics). The note should add one sentence on that.
6. Not checked: `data/round3_arakelov.json` contents; `CovolXOfSteps.lean:16-40` arithmetic (C0 = C1 + C2 + 1); `PtAt`, `Cov`, `GoodCov`, `Quo` definitions.

Verdict: FAITHFUL OUTLINE (with the minor corrections above).

### B04

Lean: `UpperTheory.Zero.LLC.recTExists`, `Development/AutomorphicArithmetic/Foundations/LocalLanglands/LocalCentralUnits/RecTExists.lean:20-66`; statement `RecTExists`/`LawsT`, `Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/RecTExists.lean:54-79`.

1. Statement. The note's field-by-field account is accurate, including which laws are restricted to `Good` classes (`twist`, `central`, `dual`, `inj`, `depth`) and which are unconditional (`dim`, `one`, `langlands`, `cusp`, `nu`, `absCentral`), and the `TypeLaw` hypotheses (34-52).
2. Outline fidelity. The proof term is followed accurately: `artEx` (uniqueness discarded by `-`, line 23), `cuspEx`, `exists_isLExt Pr.exh Pr.multi`, `hcusp`, `extDim`, `extTw`, record at 31-44, type clause 58-66 via `typeIff ... .2`, `isCuspidal_of_inflates`. The description of `cuspEx` (`CuspEx.lean:168-193`): `r x = if GoodCusp x then r₀ x else (J x.1).lpTw (e x)` with `J` from `junkEx`: correct, and commendably explicit.
3. Gaps:
   - `GoodCusp` (`NonGaloisDescent/RecTExists.lean:19-21`) is never defined in the note: rank 1, or (the field is continuously isomorphic to some Q_g and the class is a character twist of a class with a nonzero `KOne`-fixed vector). Without this the reader cannot tell how small the "good" locus is.
   - The note should say in one sentence: this is *not* the local Langlands correspondence of Harris-Taylor/Henniart/Scholze. Outside good cuspidal support the assignment is an arbitrary irreducible parameter of the right dimension. The record field that receives it is nevertheless called `localLanglandsExists`.
   - `Pr.exh`, `Pr.multi` (exhaustion and multisegment uniqueness, i.e. Bernstein-Zelevinsky/Langlands classification) and `goodMap`, `junkEx`, `expo`, `parUniq` are closed Lean constants; say so.
4. Not checked: `ExtDepth.lean:11-34`, `TypeIff.lean:46-57`, `RcTwOfSegments.lean:36-57` internals.

Verdict: FAITHFUL WITH GAPS.

### W08

Lean: `count_i_of_printed_bound_k_kato_automorphy`, `DTC/LinkedUnlE.lean:49-54`; statement `CountI`, `AV/HeightAndVanishing/Counts.lean:53-58`.

1. Statement: correct, including choice of `C, r1, r2` before the host, primality of r1, r2, `h.Big t`, `0 < e < t`, per-prime coefficient rings, finiteness and bound `(N t)^C`. `CaseI` = `l ∉ Bchi ∧ ¬ (l - 1 ∣ 2e)` (`.../DirichletPrimeToLPartMulLPowerPart.lean`, def `CaseI`): correct.
2. Hypotheses at the head: `HypothesesH'`, `∃ CK, LemmaK CK`, `KatoTwoW`, `AutomorphyUnramifiedCoefficientsAlt`. Reported. Kato two-twist vanishing is therefore an *assumed input at this head*; label it so.
3. Term order confirmed: `cohInp_alt`; `unlEnd3E (linkedUnlE_alt hH)`; `numberU3U_of_prints`; `oneCharU_of_katoTwoW_rig_admI_automorphy` with `Alg.M.main_holds, Alg.M.mprime_holds, Alg.lemmaP`, `rigIUE_alt`, `rigII_a_alt`, `admissible_typeI_even_level_alt`; `propGK...`; `U3.corGK`; `U3.countI`. Constants checked in `AV/UnitaryThreeGroups/CountI.lean`: `30 * χ.N * pK χ + 1` (line 29), `16^k` absorption (12, 31), totient sum <= N (80-90), N >= 16 (95).
4. Gap: "the linked unramified endpoint" is `linkedUnlE_alt` (`LinkedUnlE.lean:43-48`), a term with 13 arguments (`modularity_n_of_printed_mult_comp`, `unitary_three_automorphy_dense_of_prints`, `seed2_alt`, three `Sd.*_of_printed_results`, `tanA`, `core_alt_bis`, ...). Presented as one routine item.
5. Not checked: `FPropGKU.lean:118-172`, `CorGSumLog.lean:37-73` beyond the log-factorization lines.

Verdict: FAITHFUL WITH GAPS.

### W09

Lean: `countII_and_countIII_of_printsH_of_sp4In`, `DTC/AdjointLiftingOfCohomology.lean:33-39`.

Statement and case predicates (`CaseII`, `CaseIII`, `chiP`, `VLe`, `CountShape`) confirmed. Head term confirmed: `sp4Main_alt hS (...).coh Alg.M.main_holds Alg.M.mprime_holds Alg.lemmaP numberSp4_n_alt rigSp4_alt (X.corX X.lemmaX X.residual_bernoulli_nonvanishing)` plus `X.soBar` / `X.soFin` with the same `CK`, `pt_s`, `lfK`, `ltK` at Q. `sp4Main_alt` (`DTC/ConductorAtMapInjectiveCoeff.lean:131-171`): coefficient enlargement to `2^(nII+nIII)` roots, invariance of `nII`, `nIII`, membership and case under `chHom f`, `coefIndep` transport, disjunction then two restrictions: all as described. Not checked: `main_big` (68-130), `soBar`, `soFin` bodies.

Verdict: FAITHFUL OUTLINE.

### W11

Lean: `UpperTheory.V.FW.ferreroWashington`, `AV/GaloisLibrary/FerreroWashingtonIndex/FerreroWashington.lean:104-119`; statement `AV/PublishedTheorems/FerreroWashington.lean:7-11`.

1. Statement: correct (any prime l; K abelian over Q with a primitive root of order l, or 4 when l = 2; ∃ r, ∀ n and every cyclotomic model K', |Cl(K')/l| <= l^r).
2. The hypothesis on roots of unity is **not used at all**: the proof opens `intro l _ K _ _ _ _` (line 106) and the anonymous hypothesis is never referenced; `embed` and `cyc` do not take it. The note's last paragraph hints at this ("already hold in the displayed wider abelian setting"). Say it plainly.
3. Outline fidelity: `embed` (f, D with `Module.finrank K' L <= D * l^n0`), `cyc` (B, n0; totally complex and index <= B), `desc` (index over K' <= degree times index over L), final bound `D * l^n0 * B` and `Nat.lt_pow_self`: confirmed.
4. Unnamed substantial input. Inside `cyc` (lines 18-33) the two inputs are `memZ` (`.../FerreroWashingtonIndex/ToKOf.lean:13-14`: for all n >= n0, `(γ - 1)^N ∈ span{thetaH(f l^n) c, 1 + [-1], l}` in the integral group ring) and `ambCyc` (`.../AmbCyc.lean:9-10`). `memZ` is precisely a uniform "Stickelberger element is not divisible by l, with bounded lambda" statement, i.e. where the mu = 0 content lives. The note calls this "the group-ring containment" and does not name or locate it. The directory totals 4,672 lines.
5. Literature. The Lean `Prop` is called `FerreroWashington` but is the bounded-rank formulation, not the statement mu = 0; and Lean proves it in-repo rather than assuming it. The note's prose never mentions the classical theorem; the track README calls it "the classical bound". Both should state the relation and that equivalence with the published theorem was not established (the unit card already says "no equivalence with a published result inferred").
6. Not checked: the l = 2 bound `((2^φ(f·2^{ee 2}))^N · B^N)^2` beyond matching line 34; `pOdd`, reflection inequality.

Verdict: FAITHFUL WITH GAPS.

### T09

Lean: `functionalsSeparate_of_howeUnram_of_siegelWeil`, `.../ThetaPairLifts/LocalTypeDictionary/FunctionalsSeparateOfHoweUnramOfSiegelWeil.lean:17-19`; `real_functionals_separate_of_hypothesis`, `.../RealFunctionalsSeparateOfHypothesis.lean:15-30`.

1. Statement `FunctionalsSeparate` (`Development/AbelianVarietyTheory/BlockTheory/DivisorBase/LevelPlusSubgroup.lean:83-91`) and `Separates` (65-67): the note's quantifier order (eps, CF >= 6510, x0, then data, w ≠ 0, then one (ρ, ξ), then ∀ t ≠ 0 ∃ Ψ, Φ) is correct.
2. Hypotheses at the head: `ThetaLocalInputs`, `HoweUnram`, `SiegelWeilUnitaryConvergent`: correct, and these are genuine assumed inputs at this head. On the main route `HoweUnram` is discharged by `GlobalTheory.Hk3.howeUnram_holds` and the Siegel-Weil statement by `UpperTheory.Lit.Sw47.convergent` (`TPS/SiegelEisensteinSecondTermHypotheses.lean:46`, `...OfVWin.lean:481-482`). Add that.
3. Term order confirmed: models, seesaw + twist step, row tower, convergence, `periodNe_of_eigen P.harishChandraModules P.casselmanWallach P.cuspRapidDecay realIn`, `twist_core_surjective` with twelve arguments, `rowSeparation_by_realFunctionals_of_chain_steps`, `bessel_separate_of_step_gap`.
4. Gaps: the head calls `GlobalTheory.T.convergence_of_separating_family` and `GlobalTheory.T.twist_core_surjective`; the note cites `separating_family_converges` and `twist_core_surjective_of_local_components` (presumably what the wrappers resolve to; not verified). "Globalization" is the field `casselmanWallach`; use the name. The fields of `P` consumed here (`harishChandraFinite`, `discreteSeriesCover`, `weilRepresentationUnitaryPair`, `weilSiegelFormulaUnitary`, `doublingMethod`, `unramifiedDoublingGL`) should be listed as assumed record fields.
5. Not checked: `SepGap.lean:222-256` (`factor_gap`), "even rank" claim, `RealBranch.lean:231-235`.

Verdict: FAITHFUL WITH GAPS.

### T11

Lean: `PositivityTheory.ThKR.theoremK_head2`, `Development/WeilBound/ThetaLifts/Reductions/FiniteClosure/TheoremKOfMod.lean:26-27`.

Two antecedents `EisBL`, `SiegelWeilStd`; conclusion `ThetaIntegralsAgree ∧ LocalMatching`: correct. `ModSt` filled by `modSt2`; the neighbouring variant takes an unused `_P` (lines 22-24): correct. The `closeSph` argument list (15-20) matches the note's place-by-place description. Minor: `howeInert`, `localLift_holds`, `siegelCore_holds`, `weilEx`, `locRepEx`, the four `BernsteinRamification.Close.*` are closed constants; say so, and say that the two antecedents are themselves discharged in-repo on the main route (`eisBL`, `siegelWeilStd`). Not checked: `CloseSph.lean` ranges, `WeilTensorModels.lean:491-592` clause-by-clause (StepAlpha/StepBeta formulas).

Verdict: FAITHFUL OUTLINE.

### T17

Lean: `moriwakiBig_outright`, `.../MoriwakiBigness/MoriwakiBigTheorem/Outright.lean:9-11`; statement `ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/ArakelovGeometry/MoriwakiSt.lean:29-36`.

Statement: all eight hypotheses and the inequality `II(A^{D+1}) <= arVolP ... 1 D` reported correctly; the contrast with `MoriwakiHSStatement` (18-27, extra `HeightsNonneg`, a limit) is correct. `MoriwakiBig.of_found` (`GroundTheory/HeightsAndTheta/Heights/OrbitLimits/MoriwakiBig.lean:11-16`): D = 0 goes to the curve statement, D > 0 to `hG6` without `hgen`: as the note says. `moriwakiBig_of_classicalTheorems` takes components `.1` and `.2.1` of the five-part `hsChain` (`HSChain.lean:365-370`): correct. Gaps: (a) no sentence that this is a bespoke formalization (multihomogeneous coordinate ideals, an axiomatized `IntersectionSystem`, limsup volume) proved in-repo with no hypotheses, whose agreement with the published arithmetic-bigness theorem is not established; (b) the three "classical" inputs are in-repo constants: `PositivityTheory.ResPlug.FromRes.resK` (a resolution statement), `Tls2.Pl.poincareLelong`, `MbAis.DenseCurves.main`. I did not open `ResKStatement`; what form of resolution Lean claims to prove is unchecked. Not checked: `hsChain` body (about 180 chained steps), `PMoriwakiBigCurve.lean:15-47` arithmetic.

Verdict: FAITHFUL WITH GAPS.

### P001

`Main.lean:4`; `Formalism/GammaFactorNonvanishing/CritLine.lean:29-32`; `RhOfRight.lean:5-62`. Statement, modulus-one specialization (`LFunction_modOne_eq`), trichotomy, side conditions (s ≠ 0 from `riemannZeta_zero`, `hnat`, `h1`), four nonvanishing factors, cosine case split on k < 0, k = 0, k > 0 with `(k-1).toNat`: all confirmed, including the internal line ranges 5-30, 31-59, 60. Not checked: manuscript page.

Verdict: FAITHFUL OUTLINE.

### P003

`Statements.lean:6-8`, `Main.lean:8`, `CharacterBoxes/Imprimitive.lean:5-35`, `TPS/TopPlug.lean:12-18`. Statement and definitional identity with `EveryCharacter` (`EveryCharacter.lean:13-14`) correct. Conductor reduction confirmed step by step (disjunction transfer 11-17; `LFunction_changeLevel` 18-19; Euler factor norm argument 20-35). `every_character_of_green_v_win` is on the actual route (called from `SiegelEisensteinSecondTermHypotheses.lean:72`). Gap: the primitive predicate is `ZeroFreeAll := ∀ ψ : PChar, True → ∀ s, 1/2 < re s → L(ψ, s) ≠ 0` (`Formalism/SharpRestriction/RamificationFrobenius/TotientGaloisClasses/ExplicitFormulaErrorOfHostConditions.lean:11-18`) with **no pole exception**; at N = 1, s = 1 it asserts nonvanishing of Mathlib's totalized value. `imprimitive` uses it at line 10 without any disjunction. The note should state the exact predicate and this convention.

Verdict: FAITHFUL WITH GAPS.

### P005

`Statements.lean:14-16`, `Main.lean:12`, `MainTheorems.lean:11-13`, `CritLine.lean:6-27`. Every step and internal line reference (11-16 and 27; 19-21; 17-23; 24-26) confirmed; functional equation applied to the inverse character via `hinv.completedLFunction_one_sub s` and `inv_inv`; no division by the root number. Correct.

Verdict: FAITHFUL OUTLINE.

### P009

`EveryCharacter.lean:13-14`, `MainTheorems.lean:7-16`, `TPS/TopPlug.lean:12-18`, `CharacterBoxes/SupplyChi.lean:8-16`, `CharacterBoxes/ZeroFreeAllOfTopG.lean:26-34`. Corrections: (a) `allChi := everyCharacter` is an alias, not "a direct application of P010"; (b) in `zeroFreeAll_of_topG` the two analytic inputs are `level_gm_le_on_family_scales` (P017) and `UpperTheory.Comparison₂.formB`, i.e. `Level.FormB` = the window criterion `HasWindows {x | Gm x <= x^θ} la → ZeroFreeAbove θ` (`.../TotientGaloisClasses/Window.lean:30-33`); the note calls the second a "slope bound", which is wrong; (c) the note should say that Green and the geometric witness are *not* hypotheses of the Lean P009 route but are supplied in `SiegelEisensteinSecondTermHypotheses.lean:69-74` (it says "P009's full statement has no hypothesis binder", which is right but leaves the reader guessing where they come from). The three "uses" paragraph is correct.

Verdict: FAITHFUL WITH GAPS.

## 3. OVERVIEW.md (priority)

Claims checked against Lean:
- eps < 1/52, cutoff t = floor(x^401), interval [Y, Y^2] with X^{1/J} <= Y, Y^2 <= X, J >= 1, finiteness plus sum bound exp(x^eps / 2) = sqrt(exp(x^eps)) over every finite S: correct (`CharacterBoxes/ExistsPageN.lean:12-49`).
- 3/2-window: correct (`SupplyChi.lean:8-9`, `TopPlug.lean:14`).
- Exponent 1/2 + (e_D + e_L + 7) eps: correct (`.../TotientGaloisClasses/TopDefs.lean:23-26`, `TopWin.lean:28`).
- e_D = 2, e_L = 0: consistent with `Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/LinkGl.lean:29` (`LinkGLOBAL Fm 2 CH 3 2 0`).
- Choice of theta and "9 eps < theta - 1/2": consistent with `TopWin.lean:69-81` (theta = 1/2 + min(beta - 1/2, 1/2)/2 and `exists_small_eps (eD + eL + 7)`). Note Lean fixes theta by a formula; the overview's "choose" is fine.
- Not checked: the "half power" paragraph (2/|I_p|, ASK - MAIN = De, the four error terms and the bounds on m, k/n^2), the Landau paragraph beyond the shape of `FormBAt`, and "For Re s >= 1 the level criterion uses classical nonvanishing".

Sentences that overstate or under-disclose:
1. **V.** The page says for F that its constructions "remain open as complete written derivations", but says nothing comparable for V. `STATUS.md:58` and `FAQ.md:7` do. The section "V supplies the numerical budget" reads as if V were available. Required: an explicit sentence that V has no human-readable proof.
2. **Mood.** From "The host construction chooses..." through "This contradicts the putative zero." the text is in the indicative. The first paragraph is conditional, but a reader landing on the last section sees an unconditional proof narrative. "The host construction ... supplies the bound at the chosen host's actual rank together with its explicit-formula estimate" is itself list B, i.e. assumed.
3. **Size of the assumption set.** "the local implications in lists A-C" hides that these are 10 + 8 + 13 = 31 universally quantified implications granted at their Lean types (`units/V4-COND.md`, Assumptions). Say the number and that they are not proved in the paper.
4. **Lean versus paper.** The overview never says that the pinned Lean development states the five goals without hypotheses and that the *written* argument is the conditional one. A specialist needs that sentence on this page, not only in STATUS.
5. **Green.** "Green's finite-field character assertion" is assumed in the paper theorem; in Lean it is produced by a constant (`PositivityTheory.Stage1.PM.greenRegularCharacters`). Either is fine, but say which layer is being described.
6. "The Landau window theorem bounds..." and "P017 bounds the prime sum..." are stated as established; P017 is "Full, L1, pending_review" and the analytic README says "The v3 review recorded gaps in the lower inputs to P017". Add "pending review" inline or soften.
7. The banner "AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved" is present. Good. "AI cross-reviewed" should not be read as review by a human; "no human sign-off" covers it.

Reader test: an analytic number theorist can tell where to start (P023 then P022, P018). A Galois or Arakelov specialist cannot: the V paragraph links P013 and B07 but not W13/P026/W08-W11, and the F paragraph links T02, T13, B05, P021 but not T15/T17/T12. The half-power paragraph uses m, n, k, "tied family", "column normalization", "error bracket" without definitions and is not checkable from the page.

## 4. Track READMEs

Common to all seven: banner present; each gives a starter packet, prerequisites, a reading path and one specialist question, which is good. None states on the page that the main deduction is conditional and that V and F lack written proofs (galois and formal mention V/F in passing). None explains the status vocabulary ("Open inputs and scope", grades L0/L1/L2) in place.

- **analytic.** Accurate as far as checked. P003 as first item is a formal re-export; fine as orientation. "The v3 review recorded gaps in the lower inputs to P017" is a useful disclosure; link the review line.
- **arakelov.** "The published asymptotic counts small sections of one nef metrized line bundle" is fair. It should add that T17 in Lean is a bespoke statement proved in-repo and that T15's seven inputs are hypotheses at that head. R21's check of "Theorem A" is reported with scope; I do not vouch for the numbering.
- **formal.** Accurate. Missing: one sentence that `Main.lean` exports have no hypotheses while the written deduction (V4-COND) is conditional; P010/P011 one-line descriptions ("Follow the upper declaration to its suppliers") do not tell the reader these two-line terms dominate 9.57M and 7.43M lines.
- **galois.** "W11 · Identify the classical bound in a cyclotomic tower": see W11; it is a Lean-proved bounded-rank variant whose root-of-unity hypothesis is unused. No literature entry for it. P011 has primary track galois (unit card) but is absent from this reading path. The Kato paragraph is appropriately scoped ("go beyond those comparisons"); it should add that in Lean the Euler-system integrality is an in-repo theorem in a bespoke form, and at W08 Kato vanishing is an assumed input.
- **local.** "P. Scholze, The local Langlands correspondence for GLn ... R21 compared the statements on traces, parabolic induction, supercuspidals and twists at B04." Without qualification this suggests B04 is, or rests on, the LLC. In Lean, B04 asserts existence of some assignment that is arbitrary on cuspidals outside `GoodCusp` and whose strong laws hold only on `Good` support. "The tame type law ... require additional input" does not convey this. Must be corrected.
- **theta.** "The doubling formula controls the value of an Eisenstein series" and "Identify the two multipliers in the doubling formula": T12 is a Siegel-Weil statement for the Eisenstein series on the doubled group; "doubling formula" will mislead a specialist (doubling method = zeta integral). The Yamana citation is scoped to the multiplier; I do not vouch for "Theorem 2".
- **ktheory.** The grade table is clear and scoped. Not checked against Lean (no ktheory note in my list). The Borel/Soulé numbering is not vouched for.

## 5. notes/formal/procedures.md

- Section 1: I recomputed the SHA-256 of `Main.lean` line 4 with the stated convention (LF-joined, no trailing newline): `71b3d50605ddda7c0c74fbbf5cca47165a4cfa2ad72f50f36b907ecac7ff505a`, equal to `data/pins.json` and to the value printed in the note. Coherent. The field name `line0` is 1-based, which the prose explains; the sentence "Python indexes the first line as zero" is fine.
- Section 2: script interfaces match the commands (`scripts/round3_print_axioms.py`: positional module then one or more declarations; `scripts/round3_axiom_entries.lean`: one `.olean` path). The axiom list `propext, Classical.choice, Quot.sound` agrees with `STATUS.md:41`. Lean 4.33.1 agrees with `${LEAN_PROJECT}/lean-toolchain`. I did not run Lean; the reported outputs are unverified by me. The note correctly distinguishes metadata lookup from kernel re-checking.
- Section 3: `scripts/round3_dominated.py` takes `graph name [--pins]` and checks `pins["graph_sha256"]`; matches. Numbers: root 9,567,045; without `everyCharacter_of_row` 2,137,853; dominated 7,429,192 = P011 card. P010 card 9,567,042 = root minus 3 lines (the one-line `allChi` plus the two-line `EveryCharacter` definition), consistent. I did not have `graph_cache.bin` and did not rerun.
- Issues: all commands depend on a private layout (`atlas checkout`, `Lean source checkout`, `../../.oleans`, `../../out/graph_cache.bin`) that is not part of the repository; an outside reader cannot run any of the three checks as written. "Both traversals stop at the literature frontier" uses an undefined term on this page (and, given section 0, "literature" nodes are ordinary proved declarations). `hashlib.file_digest` needs Python >= 3.11; stated version 3.11.9 is consistent.

Verdict: COHERENT; numbers consistent across files.

## 6. Required corrections

1. `notes/units/P010_round3.md`, paragraph 3 ("That record requires..."): replace "compares the local Weil-Deligne data ... with the parameter" by the three clauses of `AwayB` (`GR/TypeConditions/WeightsConjBis.lean:26-31`) and the definition of `IsQpBig` (15-16); state that `rc` ranges over all maps satisfying `IsRecT`.
2. `notes/units/P010_round3.md`, section "Weaken the row": replace "forgets some of the stronger conditions" by "strengthens the hypothesis `IsQp` to `IsQpBig` in `tame0` and in `AboveB.nice`; no field is dropped" (`WeightsConjBis.lean:75-82`, `WeightsConjAlt.lean:35-40`).
3. `notes/units/P010_round3.md`: add (a) one sentence that the Lean declaration has no premises; (b) the Lean names `geoOne_holds`, `tLift_holds_k`, `wtLacEx_holds`, `congPhi_holds`, `descOffT`, `limFinOdd_of`; (c) a literature sentence: in-repo construction, not an assumed theorem, and a weak variant of local-global compatibility.
4. `notes/units/P011_round3.md`, section "Apply the two-input theorem": name the callee `UpperTheory.Lit.every_character_of_theta_integrals_local_matching` (`TPS/SiegelEisensteinSecondTermHypotheses.lean:69-74`), state that Green is supplied there via `green_of_regular P.greenRegularCharacters`, and state that lines 219-809 of `EveryCharacterOfLiteratureOfVWin.lean` (176 theorems) are in-repo derivations of which only lines 284, 286, 618 use the record.
5. `notes/units/P011_round3.md`, section "Produce the right kind of window": list the four bundles built in `DTC/TopMainZj.lean:18-70` and say they are in-repo constants; name `baseChangeN`; add the budget `sqrt(exp(x^eps))` and the `WinPair` conditions (`ExistsPageN.lean:27-37, 42`).
6. `notes/units/P026_round3.md`, section "Fix the modular source...": correct the first-diagonal condition to "some power m >= 1" (`FinalTheorems.lean:65`), add the omitted hypothesis `ne` (line 66) and the `KillsMu l` condition on the twisting character (`Statements/.../ZetaUr.lean:14`).
7. `notes/units/P026_round3.md`, section "Produce a single global tuple": list the 19 additional `glue2` arguments (`KatoGlobalUnitLawOfSmoothedClasses.lean:9-10`) and identify which produce the nonvanishing clause of `Pin7`; name `nonvanishing_transfer_characterSums_powerSeries`, `quotient_char_trivial_inertia_cyclotomic_tower`, `pCore`, `pFrobEx` in the local section; add the literature sentence (Kato-named statements are bespoke and proved in-repo; no theorem number vouched).
8. `notes/units/B04_round3.md`: define `GoodCusp`/`Good` (`NonGaloisDescent/RecTExists.lean:19-23`) in the opening section; add "this is not the local Langlands correspondence; outside good cuspidal support the assignment is an arbitrary parameter"; mark `Pr.exh`, `Pr.multi`, `goodMap`, `junkEx` as in-repo constants.
9. `notes/units/W11_round3.md`: (a) name and locate `memZ` (`ToKOf.lean:13-14`) and `ambCyc` (`AmbCyc.lean:9-10`) and say `memZ` carries the mu = 0 content; (b) state plainly that the root-of-unity hypothesis is unused (`FerreroWashington.lean:106`); (c) add the literature sentence (bounded-rank formulation, proved in-repo, equivalence with the published theorem not established).
10. `notes/units/W08_round3.md`: expand "the linked unramified endpoint" into the 13 inputs of `linkedUnlE_alt` (`DTC/LinkedUnlE.lean:43-48`); label `KatoTwoW`, `HypothesesH'`, `AutomorphyUnramifiedCoefficientsAlt` and `∃ CK, LemmaK CK` as assumed at this head.
11. `notes/units/T12_round3.md`: name and locate `eisBL` (`SiegelWeilStdLeaves.lean:44`), `holLeadB` (`SiegelWeilStdMid.lean:19`), `absThm`, `vacuum_generates_polynomials` (`SiegelWeilStdOf.lean:66-67`), `siegelDensitiesLowA`, `densEq` (43-47), `siegel_set_unitary` (39-41); add the literature sentence (proved in-repo, anisotropic case, relation to the published formula not established).
12. `notes/units/T15_round3.md`, step 4: cite `uniform_lower_bound_of_sums'` (`TPS/ULowOfStatement.lean:11-12`) as the declaration actually called; step 2: name `flatDeg_of_scholzeWeinstein_of_prints`; step 1: name `cov_size_bound`, `anchor_bound`; add one sentence that the seven inputs are hypotheses here and are discharged in-repo upstream.
13. `notes/units/T17_round3.md`, last section: state that `MoriwakiBigStatement` is a bespoke formulation proved by `moriwakiBig_outright` with no hypotheses, that `resK`, `poincareLelong`, `DenseCurves.main` are in-repo constants, and that agreement with the published theorem is not established.
14. `notes/units/T09_round3.md`: use the names in the head term (`convergence_of_separating_family`, `twist_core_surjective`) or state the wrapper relation; replace "globalization" by the field `casselmanWallach`; list the consumed fields of `ThetaLocalInputs` as assumed at this head and say what discharges `HoweUnram` and `SiegelWeilUnitaryConvergent` upstream.
15. `notes/units/T11_round3.md`: add one sentence that `howeInert`, `localLift_holds`, `siegelCore_holds`, `weilEx` and the `BernsteinRamification.Close.*` inputs are in-repo constants.
16. `notes/units/P003_round3.md`, section "Lift nonvanishing from the conductor": state the exact predicate `ZeroFreeAll` and that it has no pole exception (`ExplicitFormulaErrorOfHostConditions.lean:11-18`), relying at (N = 1, s = 1) on Mathlib's totalized value.
17. `notes/units/P009_round3.md`: change "slope bound" to "the window (Landau) criterion `formB`" (`ZeroFreeAllOfTopG.lean:28`; `Window.lean:30-33`); change "direct application of P010" to "alias of P010"; say where Green and the geometric witness are supplied in Lean.
18. `OVERVIEW.md`, section "Why two arithmetic inputs are needed", V paragraph: add an explicit sentence that V has no human-readable proof in this atlas (mirror `STATUS.md:58`).
19. `OVERVIEW.md`, first paragraph: give the count 10 + 8 + 13 = 31 for lists A-C and say they are granted, not proved in the paper; add one sentence distinguishing the hypothesis-free Lean exports from the conditional written deduction.
20. `OVERVIEW.md`, final two paragraphs: put the host-construction sentence and the final deduction in conditional mood ("under V, F, Green and lists A-C ..."); mark P017/P022 as pending review inline.
21. `tracks/local/README.md`, "Literature" paragraph: state that B04 is not the LLC and is canonical only on good (rank-one or depth-zero-twist over Q_p) cuspidal support.
22. `tracks/theta/README.md`: replace "doubling formula" (two occurrences) by "Siegel-Weil formula for the doubled Eisenstein series".
23. `tracks/galois/README.md`: reword the W11 line (not "the classical bound"; "a Lean-proved bounded-rank statement named after Ferrero-Washington"), add a literature line for it with scope, and add P011 to the reading path.
24. All seven `tracks/*/README.md`: add one standard line under the banner: the written deduction is conditional on V, F, Green and 31 local implications; V and F have no human-readable proof; all text is AI-written without human review.
25. `notes/formal/procedures.md`: replace hard-coded private paths by variables (e.g. `LEAN_SRC`, `OLEAN_DIR`, `GRAPH`) with the present values as examples, and define "literature frontier" or remove the phrase.
26. All 17 notes: adopt one fixed sentence pattern for each named classical result: "hypothesis at this head / record field / in-repo constant `X` at `file:line`; classical statement or variant; equivalence not checked".

## 7. Reader-experience improvements

- Each note: open with a three-line box: Lean name and range; premises of the Lean declaration (or "none"); what is assumed at this head versus discharged upstream.
- Each note: add a small table "named inputs" with columns Lean constant, file:line, approximate size (file or dominated lines), kind (routine / substantial). The current prose buries names in bold mid-paragraph and omits sizes entirely.
- P010/P011: a five-row call chain diagram (`allChi` -> `everyCharacter` -> `everyCharacter_of_row` -> `every_character_of_literature_of_vWin` -> `every_character_of_theta_integrals_local_matching` -> `every_character_of_green_v_win` -> `imprimitive ∘ zero_free_all_of_green_v_win`) would replace several paragraphs and make clear where Green, V and F enter in Lean.
- OVERVIEW: add a "which unit first" line per field at the end of the V and F paragraphs (Galois: W13 then P026 then W08/W09/W11; Arakelov: T15 then T17; theta: T12 then T11 then T09; local: B04). Define or drop m, n, k in the half-power paragraph, or link one worked note.
- OVERVIEW and READMEs: a four-word status legend (Full / Outlined / Statement only; L0-L2) on the page.
- READMEs: under "Literature", separate three columns: published statement; Lean `Prop` name; relation (assumed here / proved in-repo / variant).
- B04, W11, T12, T17: a "how this differs from the textbook theorem" paragraph. These are the four places where a specialist is most likely to be misled by a name.
- Notes cite internal line sub-ranges (e.g. "`cyc` 42-55", "`countI` 76-102") without saying what happens there; either drop them or attach a five-word label to each range.
- Paper page references and `.tex` excerpts could not be checked from the repository alone; say in each note whether the excerpt is verbatim.

## 8. What was not checked

- No Lean build, no `#print axioms`, no graph recomputation; only the `Main.lean:4` hash was recomputed.
- Definitions below the statements: `CuspSub`, `PolarizedPair`, `IsRegAlg`, `IsLocComp`, `WD`, `wdOf`, `Newform`, `Att`, `Tame`, `Unr`, `Z1`, `Layer2`, `HTLawCsOfCoef`, `Host`, `Bchi`, `Vlen`, `shaLen`, `LData`, `IsArithVar`, `IntersectionSystem`, `arVolP`, `Darboux`, `IsUWeilSplit`, `PtAt`, `Cov`, `FamP`, `ResKStatement`.
- Proof bodies: `main_big`, `soBar`, `soFin`, `propGK...`, `hsChain`, `CloseSph`, `SepGap`, `CovolXOfSteps`, `glue2`, `pCore`, `memZ`, `ambCyc`, `goodMap`, everything under `geoOne_holds` and `tLift_holds_k`.
- OVERVIEW "half power" paragraph and the Re s >= 1 remark.
- All external theorem numbers (Kato 8.1.3/8.12/9.7, Scholze 1.2, Yamana Thm 2, Moriwaki Thm A, Borel 12.2, Soulé 4.1) and all manuscript page references.
- ktheory units; SHA-256 values of cited ranges other than `riemannHypothesis`.
