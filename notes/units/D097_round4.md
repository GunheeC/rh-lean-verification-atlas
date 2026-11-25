# D097 · The two tests for a saturated ordinary ideal

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 2,452 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**pending_review** · [Unit card](../../units/D097.md) · [Track guide](../../tracks/local/README.md)

The rank-three ordinary deformation datum has a specific saturated ideal in its universal coefficient ring. One assertion identifies a crystalline consequence of killing the ideal. A second says that a prescribed class of crystalline infinitesimal tests kills it. `GlobalTheory.T.saturatedOrdinaryIdeal_cuts_out_crystalline_locus` ([SaturatedOrdinaryIdealCutsOutCrystallineLocusStatement.lean:6–7](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/CrystallineOrdinaryIdeals/SaturatedOrdinaryIdealCutsOutCrystallineLocusStatement.lean#L6-L7)).

## Fix the ideal before choosing a point

Choose a prime $\ell$ and a characteristic-zero complete discrete valuation ring $O$ finite over the $\ell$-adic integers with the specified algebra structure. Fix the rank-three datum $D$ and its universal object $U$. The ordinary ideal is saturated at the element called del: an element belongs to $I_Y$ precisely if multiplication by some nonnegative power of del puts it in the ordinary ideal. The exponent is existential for each element. Both conclusions concern this very $I_Y$ in $U.R$ under the local published-theorem hypothesis. `GlobalTheory.T.saturatedOrdinaryIdeal_cuts_out_crystalline_locus` ([SaturatedOrdinaryIdealCutsOutCrystallineLocusStatement.lean:6–7](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/CrystallineOrdinaryIdeals/SaturatedOrdinaryIdealCutsOutCrystallineLocusStatement.lean#L6-L7)). `UpperTheory.V.Loc.Dat3.IY` ([IsInertiaInfiniteCyclotomic.lean:112–126](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/PadicHodgeTheory/IsInertiaInfiniteCyclotomic.lean#L112-L126)).

## Go from the ideal to a crystalline point

Take a compatible finite algebra $B$ over the $\ell$-adic rationals and an $O$-algebra map from the universal ring annihilating the ideal. The desired conclusion concerns the pushed representation. The source extracts its linear-group component on the specified subgroup, checks the auxiliary conditions, and tests it after further scalar extension. For an extension $B'$ the composite map still kills the ideal since the original map did. The specialized crystalline point theorem supplies a representation over $B'$; an entrywise comparison identifies it with the scalar extension of the component already selected. This identification is essential for applying the local crystalline criterion. `UpperTheory.V.Loc.Dat3.PtsCr` ([IsInertiaInfiniteCyclotomic.lean:140–143](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/PadicHodgeTheory/IsInertiaInfiniteCyclotomic.lean#L140-L143)). `GlobalTheory.OrdLoc.ptsCr_IY` ([SaturatedOrdIdealPointsIsLCrystalline.lean:17–50](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/CrystallineOrdinaryIdeals/SaturatedOrdIdealPointsIsLCrystalline.lean#L17-L50)).

## Go from an admissible test to the ideal

In this direction the target data include a finite extension $E$, an algebra $B$ finite over the $\ell$-adic rationals, and a projection to $E$ whose kernel elements are nilpotent. Assume the designated deformation condition on the pushed representation relative to that projection. The proof constructs the compatible fraction-field tower for $O,E,B$, using injectivity of the coefficient maps, and applies the reduction for this particular test to conclude $I_Y\subseteq\ker f$. The two implications have different input predicates and target algebras, so treating the second as a reversal of the first would miss a substantive comparison. The wrapper simply supplies this pair; a related local comparison involving finite cocycles is [D082](../../units/D082.md). `UpperTheory.V.Loc.Dat3.CrPts` ([IsInertiaInfiniteCyclotomic.lean:145–151](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/PadicHodgeTheory/IsInertiaInfiniteCyclotomic.lean#L145-L151)). `GlobalTheory.OrdLoc.crPts_IY` ([CrystallinePointsSaturatedOrdinaryIdealArtinian.lean:116–164](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/CrystallineOrdinaryIdeals/CrystallinePointsSaturatedOrdinaryIdealArtinian.lean#L116-L164)). `GlobalTheory.OrdLoc.ideal_cuts_crystalline_locus` ([SaturatedOrdinaryIdealCutsOutCrystallineLocus.lean:9–14](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/CrystallineOrdinaryIdeals/SaturatedOrdinaryIdealCutsOutCrystallineLocus.lean#L9-L14)).

The seven fields of `LocalPublishedTheorems` are `lfK`, `ltK`, `leK` (local finiteness, Tate duality and the Euler characteristic in the K formulation), `lf`, `lt`, `le` (the reciprocity formulations), and `bk` (local Bloch–Kato). `UpperTheory.V.Loc.LocalPublishedTheorems` (`Development/AutomorphicArithmetic/AutomorphicVarieties/PadicHodgeTheory/LocalPublishedTheorems.lean:12–19`).

The descent in `reduce` is the substantive reverse implication. Choose the integral specialization by `univEx`. Uniqueness in `unramified_lift_deformation` identifies its extension with the reduced test. Take the subalgebra of $B$ consisting of elements reducing into the image of the fraction field of $O$. The original map lands there. The retraction to that fraction field has nilpotent kernel, and `dcr_pair` transfers the deformation condition to the restricted test. Apply `crystallineDeformation_points_saturatedOrdinaryIdeal_fracO` to the restricted map and then include its zero values back into $B$. `GlobalTheory.OrdLoc.CriticalPoints.reduce` (`Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/CrystallineOrdinaryIdeals/CrystallinePointsSaturatedOrdinaryIdealArtinian.lean:35–110`). `GlobalTheory.T.crystallineDeformation_points_saturatedOrdinaryIdeal_fracO` (`Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/CrystallineOrdinaryIdeals/CrystallineDeformationPointsSaturatedOrdinaryIdeStatement.lean:6–7`).

## Literature-named inputs

`UpperTheory.V.Loc.LocalPublishedTheorems.lfK` — record field (`Development/AutomorphicArithmetic/AutomorphicVarieties/PadicHodgeTheory/LocalPublishedTheorems.lean:13`); not compared.

`UpperTheory.V.Loc.LocalPublishedTheorems.ltK` — record field (`Development/AutomorphicArithmetic/AutomorphicVarieties/PadicHodgeTheory/LocalPublishedTheorems.lean:14`); not compared.

`UpperTheory.V.Loc.LocalPublishedTheorems.leK` — record field (`Development/AutomorphicArithmetic/AutomorphicVarieties/PadicHodgeTheory/LocalPublishedTheorems.lean:15`); not compared.

`UpperTheory.V.Loc.LocalPublishedTheorems.lf` — record field (`Development/AutomorphicArithmetic/AutomorphicVarieties/PadicHodgeTheory/LocalPublishedTheorems.lean:16`); not compared.

`UpperTheory.V.Loc.LocalPublishedTheorems.lt` — record field (`Development/AutomorphicArithmetic/AutomorphicVarieties/PadicHodgeTheory/LocalPublishedTheorems.lean:17`); not compared.

`UpperTheory.V.Loc.LocalPublishedTheorems.le` — record field (`Development/AutomorphicArithmetic/AutomorphicVarieties/PadicHodgeTheory/LocalPublishedTheorems.lean:18`); not compared.

`UpperTheory.V.Loc.LocalPublishedTheorems.bk` — record field (`Development/AutomorphicArithmetic/AutomorphicVarieties/PadicHodgeTheory/LocalPublishedTheorems.lean:19`); not compared.

**First step to challenge.** Check the reverse implication on a finite test algebra with nilpotent kernel over its residue target. Testing only field-valued points omits the infinitesimal condition.
