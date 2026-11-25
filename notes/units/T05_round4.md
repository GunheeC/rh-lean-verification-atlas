# T05 · Two estimates on different sides of the same row problem

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 303,161 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**Outlined · pending_review.** A fit for the Fourier coefficient will use just the lower-weight component of this pair. The later construction of the definite-side record will use both components. Keeping the two estimates apart also keeps their hypotheses apart. [T05](../../units/T05.md) · [The F construction](../../pillars/F.md)

## Read the two assertions separately

Fix the third-place hypothesis record $P$. Call a point admissible when it satisfies the row's `PointConditions'`. At fixed family $F_m$ the phrase “eventually at points” requires one $x_0$ that works at every $x\ge x_0$ with $x>F_m.x_1$, every index there and every admissible point $p$ at that index. A statement is closed on a family class when some $\varepsilon_1>0$ works as follows. For each $0<\varepsilon\le\varepsilon_1$ there is a largeness datum $K$ which works for every family and height $H$ satisfying the class membership and largeness conditions. The choices of the two outer closed thresholds for the two assertions may differ. `GlobalTheory.BigTop.EventuallyAtPoints`, `Realised.lean:117–118`; `Formalism.MainNotions.Closed`, `ParamsHeightRankConstant.lean:159–161`; `GlobalTheory.Fc.S0.ontoX_and_lamLow_of_unitaryGroupHypotheses'`, `SurjectiveAndLowWeightOfUnramifiedExponents.lean:16–29`.

- On the false side, assume the family's division inequality `DIVinN`. Some $C_0\ge0$ works eventually at points. At each such point satisfying `More`, for every $C\ge C_0$ the row `p.S false` satisfies `ON` with the numerical record `p.N C H`. The family and $H$ precede $C_0$, which precedes the eventual point. `GlobalTheory.BigOn.SurjectiveOntoX`, `ExportSt.lean:47–48`.
- On the true side, eventually at points, every real $C$ gives the condition `L6` for `p.S true` with that point's `p.N C H`. This clause has neither the extra division premise nor the restriction $C\ge C_0$. `GlobalTheory.BigTop.LambdaLowerBound₂`, `Realised.lean:126`.

## From the inputs to the pair

1. **Identify the proof of `RecTExists`.** On the false branch the supplied fields concern cuspidal data, cohomological and character comparisons, base change, crystalline lattices, decay, the discrete-series cover and Casselman–Wallach. The reciprocity argument passed alongside these is worth opening. The application lists local converse, depth-zero, Brauer, units, reciprocity, exhaustion and segment hypotheses. The body of the selected `UpperTheory.One.M.New.llOf_alt` returns its first input, already of type `RecTExists`. The next comparison receives the proof `P.litN.loc.llc` that a suitable local map exists at each place. `SurjectiveAndLowWeightOfUnramifiedExponents.lean:19–26`; `LlOf.lean:18–21`.

2. **Put the local estimates on the same row.** The first supplier extracts global Artin reciprocity from its character input, gets the ray-field and series data and constructs the export. Its page and geometry control the rank comparison on the selected runs. Together with the export this gives the twisted-place bound. A model supplies the share estimate and, with the cuspidal input, the bad-place bound. The cohomological/base-change/crystalline inputs and the proof of `RecTExists` give the exponent bound. The terminal call puts these estimates on the prescribed records. The terminal function discards its export argument; it reconstructs the page, geometry and rank assertions from primed suppliers before combining them with the twist, share, bad-place and exponent arguments. `GlobalTheory.BigOn.ontoX_of_hypotheses_alt_alt`, `OntoXOfPrints.lean:28–45`; `GlobalTheory.BigOn.ontoX_of_twist_shares_exp_alt`, `OntoXOfTwistSharesExp.lean:21–25`.

3. **Fix the family before the lower-weight estimate.** On the other branch the actual inputs are cusp decay, the unitary Weil–Siegel and convergent Siegel–Weil assertions, the doubling and unramified inputs, Bernstein–Zelevinsky finiteness and the compact-dual formal-degree assertion. The supplier restricts by a closed lower bound of eight on the size parameter. For the resulting family it obtains an eventual size estimate, fixes its $x_0$, and then takes the scale, point, index and $C$. The size control is available for every column at that scale. `GlobalTheory.BigTop.lamLow_of_hypotheses_alt_alt`, `LamLowOfPublished.lean:17–26`.

4. **Apply the real-data estimate at this point.** The finiteness supplier takes the point's own maps and phases, the primitiveness, separation and column-size data. One numerical side condition is the hook-log-sum estimate with the size term removed. The second simplifies by $C\cdot0=0$ to reflexivity. This yields the asserted lower bound for the chosen $C$. 

The two named suppliers now give a conjunction. At the call in T02 it is the second projection that feeds the Fourier fit. In T03 both projections enter the all-rows supplier. `lamLow_of_hypotheses_alt_alt`, `LamLowOfPublished.lean:25–35`; `UpperTheory.Lit.nonempty_hyps_definite_side_of_closed_bound`, `SiegelEisensteinSecondTermHypotheses.lean:51`; `GlobalTheory.Fc.S0.StageU.hypotheses_nonempty_of_unramified_exponents_alt`, `HypothesesNonemptyOfUnramifiedExponents.lean:54–56`. [T10](../../units/T10.md) · [T03](../../units/T03.md)

## Literature-named inputs

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.greenCuspidal` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:24`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.clozelCohomological` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:23`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.heckeLAdicCharacter` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:25`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.chebotarevDegreeOne` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:26`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.baseChangeDefiniteUnitary` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:28`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.bhattScholzeCrystallineLattices` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:29`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.heckeLAdicCharacterAbove` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:30`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.cuspRapidDecay` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:31`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.globalArtinReciprocity` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:46`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.discreteSeriesCover` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:57`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.casselmanWallach` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:59`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.weilSiegelFormulaUnitary` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:32`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.siegelWeilUnitaryConvergent` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:33`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.doublingMethod` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:34`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.unramifiedDoublingGL` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:35`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.bernsteinZelevinskyFiniteness` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:36`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.formalDegreeCompactDual` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:37`); not compared.

`GlobalTheory.T.exportSt_of_reciprocity_and_casselman_wallach` — in-repo constant (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ExportStOfReadingStatement.lean:11–12`); not compared.

`GlobalTheory.BadWOn.badWSt_of_greenCuspidal_of_modelSt` — in-repo constant (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BadWStOf.lean:205–214`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.harishChandraModules` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:58`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.rayClassFieldSt` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:52`); not compared.

`GlobalTheory.FunPr.ThetaLocalInputs.siegelSetUnitary` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/BernsteinUnitaryProductIrreducible.lean:58`); not compared.

`GlobalTheory.FunPr.ThetaLocalInputs.howeDualityReal` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/BernsteinUnitaryProductIrreducible.lean:57`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.localTateDuality` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:81`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.siegelWeilUnitaryConvergent2` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:64`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.discreteSeriesClassification` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:62`); not compared.

**First step to challenge.** On the false side, track one twisted place from the rank comparison through the five estimates. Check that the chosen record in the exponent bound and its numerical parameters coincide with those used for the share and bad-place inequalities. On the true side, check that the scale threshold is selected before $p$ and $C$. The conjunction is routine once those estimates have the stated scopes. The atlas has not supplied internal hand derivations for all their inputs. `ontoX_of_hypotheses_alt_alt`, `OntoXOfPrints.lean:35–45`; `lamLow_of_hypotheses_alt_alt`, `LamLowOfPublished.lean:21–30`.
