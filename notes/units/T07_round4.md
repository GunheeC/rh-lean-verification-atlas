# T07 · Keeping the linked row when passing from two primes to the Selmer bound

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 222,063 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**pending_review** · [Unit card](../../units/T07.md) · [Track guide](../../tracks/local/README.md)

At the same reciprocity and dependence parameters, the local bound at two and three combines with memberwise Galois and tie data to give the linked Selmer norm condition. The combination requires compatible witnesses on a strengthened row. `UpperTheory.GalC.final_alt_alt` ([CFinal.lean:19–22](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/CFinal.lean#L19-L22)).

## Identify the common parameter and the two suppliers

Start with the two-layer linkage hypotheses, the third-layer inputs, geometric Galois compatibility, the series assumption, depth-zero support, local finiteness, local Tate duality and the Euler characteristic. Fix a proof of `RecTExists` and the dependence constant. The premise and the conclusion use the same parameter built from them. The premise is the linked family bound at two and three, as in [T25](../../units/T25.md). The exported proof first produces the required good-cut facts for a supplied tie using the Chebotarev component and the local inputs. It separately supplies Galois preconditions at a member from the geometric, series, support and local data. These are obligations concerning the actual member. `UpperTheory.GalC.final_alt_alt` ([CFinal.lean:19–22](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/CFinal.lean#L19-L22)). `UpperTheory.GalC.final_of_alt` ([LinkNFam.lean:75–86](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkNFam.lean#L75-L86)). `UpperTheory.GalC.exists_good_cut_facts_tie4` ([CFacts.lean:58–62](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/CFacts.lean#L58-L62)).

## Transport memberwise facts to the selected witness

The intermediate theorem chooses witness transport along the specified list extension with the geometric closure. The depth-zero and geometric assumptions supply the tie condition at members. Pair this with the Galois preconditions before applying the transport from members to witnesses. The resulting assertion at the selected place carries both conditions on the same datum. If one transported two independently existential witnesses, each could satisfy only one of these conditions, and the next invocation would have no common input. `UpperTheory.GalS.galois_preconditions_at_mem` ([PreAtMem.lean:86–103](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/PreAtMem.lean#L86-L103)). `UpperTheory.GalC.final_of_alt` ([LinkNFam.lean:75–86](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkNFam.lean#L75-L86)).

## Intersect the two linked rows

One premise now gives the Galois preconditions and the tie on a linked row. The other is the closed two-prime condition on a possibly differently described row at the identical parameter. Decompose the two linked proofs, form the conjunction of their rows and use monotonicity for the first premise and strengthening for the second. Projection in each case returns the relevant condition at a point on the conjunction. The local-to-Selmer implication applies inside that common row. This is the step connecting the arithmetic suppliers to the compatibility condition; the final wrapping in a linked assertion is formal. [D427](../../units/D427.md) gives the Selmer contribution in the atlas, while [N188](../../units/N188.md) locates a related linkage assumption. Neither individual input yields the output linkage without the common parameter and row. `UpperTheory.GalC.linkedAt_linkN_of_boundAtTwoThree` ([LinkNFam.lean:64–73](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkNFam.lean#L64-L73)). `UpperTheory.GalC.final_of_alt` ([LinkNFam.lean:75–86](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkNFam.lean#L75-L86)).

The parameter `hL` is a proof of the existence statement `RecTExists`. Its local witness is under an existential quantifier. `UpperTheory.Zero.LLC.RecTExists` (`Development/AutomorphicArithmetic/Foundations/LocalLanglands/IsRecTOfIsRec.lean:78–80`). `UpperTheory.GalC.final_alt_alt` (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/CFinal.lean:19–22`).

**Scope of the hypotheses.** The note retains the source’s named predicates and records. For the exact quantified assumptions at this head, read `UpperTheory.GalC.final_alt_alt` (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/CFinal.lean:19–22`). Their internal definitions are separate reading tasks.

## Literature-named inputs

`ReciprocityTheory.Gal.LocalTateDuality` — hypothesis at this head (`ReciprocityTheory/Hypotheses/GalCoh.lean:201–205`); not compared.

`GlobalTheory.HeightCounting.Up.PublishedInputsThirdLayerAlt.cheb` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/PublishedInputsThirdLayer.lean:27`); not compared.

**First step to challenge.** Check that the transport of Galois preconditions and the two-prime estimate survives passage to the same strengthened row and hence the same family.
