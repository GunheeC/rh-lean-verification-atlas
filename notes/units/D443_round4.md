# D443 · Passing the global flat-degree statement to one good cover

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 3,808 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**pending_review** · [Unit card](../../units/D443.md) · [Track guide](../../tracks/local/README.md)

The flat-degree package is evaluated on the actual good cover by matching the host period to a character period. Its source accepts Hodge-bundle hypotheses and builds the required degree statement through a residue comparison. `GlobalTheory.T.flatDeg_of_scholzeWeinstein_of_prints` ([ThirdPlaceSeries/FlatDegreeStatement.lean:22–23](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FlatDegreeStatement.lean#L22-L23)).

## Identify the actual supplier

The Lean head takes the Hodge-bundle record and does not use it in its result. Its intermediate term passes the record, `q2` and `q4` to `flat_tensor_swap_isIso`, which discards all three. The accessor `q2` itself ignores the record. No Scholze–Weinstein or prismatic Dieudonné input occurs in this route. The actual supplier is `flatDegreeSt_of_resK` applied to the in-repo constant `PositivityTheory.ResPlug.FromRes.resK`. `UpperTheory.Lit.Flat.flat_tensor_swap_isIso` (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/FlatTensorSwapIsIso.lean:7–8`). `GlobalTheory.CovTop.PublishedHodgeBundleTheorems.q2` (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/ToKnownTheoremsOf.lean:37–37`). `PositivityTheory.ResPlug.FromRes.resK` (`Development/WeilBound/CoreStatements/ResolutionCharZero/PlugResK.lean:7–8`). This reading records the route through the source and makes no literature equivalence assertion. [D123](../../units/D123.md) is the related reading unit indicated by the atlas. `GlobalTheory.T.flatDeg_of_scholzeWeinstein_of_prints` ([ThirdPlaceSeries/FlatDegreeStatement.lean:22–23](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FlatDegreeStatement.lean#L22-L23)). `GlobalTheory.CovTop.FlatDegProof.flatDeg_alt_alt` ([ThirdPlaceSeries/FlatDegreeStatement.lean:12–16](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FlatDegreeStatement.lean#L12-L16)). `UpperTheory.Lit.Flat.flat_tensor_swap_isIso` ([FlatTensorSwapIsIso.lean:7–8](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/FlatTensorSwapIsIso.lean#L7-L8)).

## Put the global assertion at the chosen good cover

Fix the size and host data, the selected point $p$, the index $i$ and its good cover $Y$. The deep-law theorem uses the range condition for the shifted index $i+1$ together with the relevant component of goodness for $Y$. This gives the laws on $Y.U$ for the fixed parameter $\xi_R(D)$. The log-period theorem then produces a character and the equality identifying its period with that of the actual host. The proof must use the same character and its host conditions when specializing the global statement. Replacing it by a character with matching local degree only would leave the period identity unaccounted for. `GlobalTheory.CovTop.FlatDegProof.flatDegAt_of_st` ([DivisorProofs/FlatDegreeStatement.lean:15–23](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/FlatDegreeStatement.lean#L15-L23)).

## Assemble the family witnesses

Specialize the global flat-degree theorem to the field, Hodge data, shifted weight, level, moduli object, cover, and deep laws above. Unfold the local target and rewrite by the period identity. In the enclosing family statement the source gives the outer positive witness one and the displayed auxiliary zero data, then waits for the actual family, point and good cover before invoking the just-described result. This explains the apparent disparity between the fixed auxiliary constants and the geometric content: the estimate is already available in the statement specialized on the individual cover. The proof of the residue-based global statement and the host period comparison remain distinct inputs. `GlobalTheory.CovTop.FlatDegProof.flatDegAt_of_st` ([DivisorProofs/FlatDegreeStatement.lean:15–23](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/DivisorProofs/FlatDegreeStatement.lean#L15-L23)). `GlobalTheory.CovTop.FlatDegProof.flatDeg_alt_alt` ([ThirdPlaceSeries/FlatDegreeStatement.lean:12–16](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FlatDegreeStatement.lean#L12-L16)). `FlatDegreeResidue.flatDegreeSt_of_resK` ([FlatSlim.lean:5–6](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/ComplexPeriods/FlatDegreeResidues/FlatSlim.lean#L5-L6)).

`FlatDegreeCondition` applies `CoversCondition` to the predicate `FlatDegAt p i Y` on the chosen point, index and good cover. `GlobalTheory.CovTop.FlatDegreeCondition` (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LiftLambdaBound.lean:52–52`).

## Literature-named inputs

`FlatDegreeResidue.flatDegreeSt_of_resK` — in-repo constant (`Development/WeilBound/CoreStatements/ComplexPeriods/FlatDegreeResidues/FlatSlim.lean:5–6`); not compared.

`PositivityTheory.ResPlug.FromRes.resK` — in-repo constant (`Development/WeilBound/CoreStatements/ResolutionCharZero/PlugResK.lean:7–8`); not compared.

`GlobalTheory.T.flatDeg_of_scholzeWeinstein_of_prints` — in-repo constant (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/FlatDegreeStatement.lean:22–23`); not compared.

`GlobalTheory.CompanionTheory.Ar.Br.flatDegreeSt_of_resK_gaga` — in-repo constant (`Development/AutomorphicSpectrum/Proofs/DivisibilityProofs/FlatDegreeStOfResKGaga.lean:18–30`); not compared.

`GlobalTheory.CompanionTheory.Gaga.gagaSections` — in-repo constant (`Development/AutomorphicSpectrum/Proofs/GlobalProofs/GagaSections.lean:104–138`); not compared.

**First step to challenge.** Check that the period identity and the deep-cover law refer to the same host, index and character as the specialization of the flat-degree theorem.
