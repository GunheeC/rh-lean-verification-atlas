# W02 · From a finite comparison frame to definite isobaric base change

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 1,699 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**Outlined · pending_review.** Take a CM number field unramified at all finite places over its maximal real subfield, positive rank $n$ and an automorphic representation of the indicated definite unitary group. The output is one partition of $n$ and one global family of isobaric constituent data, with compatible split and inert local conclusions and with the required infinitesimal character. [W16](../../units/W16.md) supplies candidate finiteness. [V-BC](../../units/V-BC.md) supplies the implication from candidate finiteness to this result. `baseChangeN` (`DefiniteNHolds.lean:5–6`) `baseChangeN_of` (`FillPre.lean:7–9`) `fieldN_of` (`FieldNOf.lean:52–81`)

## Choose finite families relative to the frame

Fix a reading rule and a comparison frame. For each permitted pair of block sizes, strict equivalence to finitely many candidates is obtained by applying the strict finiteness statement to each block separately. The candidate-component statement shows that a given candidate belongs to both lists. Local level openness supplies the level hypotheses. Local product compatibility and the comparison of invariant spaces then turn those lists into the three outputs needed for the entire frame: finitely many joint eigenvalue tuples at auxiliary places, finite local-product models at the initial places and a single bound for certain invariant dimensions. The finiteness is relative to the chosen frame. [W16](../../units/W16.md). `cls_fin` (`ClsFin.lean:31–45`) `all_parts` (`CandOf.lean:22–34`) `candFin_of` (`CandOf.lean:36–40`) `candFin` (`FrameEx.lean:15–17`)

## Use the finite input in the comparison

The conditional base-change supplier takes exactly that candidate finiteness as its argument. With the unitary-side input it forms a completed comparison frame. Integral Hecke, local matching, spherical and spectral inputs enter this step alongside candidate finiteness. The frame, the global Hecke-word bound and Gelfand reading are passed together to the final comparison. The latter calls a finite-family construction and then a result giving the desired isobaric datum. Reliance on these frame and reading inputs is part of the route; the elementary fact that a finite set of candidate pairs exists does not establish their compatibility. `frameEx_of_fin` (`FrameExOfFin.lean:43–48`) `baseChangeN_of` (`FillPre.lean:7–9`) `bci_of` (`BciOf.lean:22–26`)

## What one global datum must satisfy

A single global datum handles the compatible split and inert requirements. The finite-intersection argument with one failure chosen per candidate and the cofinite Satake permutation are given in [V-BC](../../units/V-BC.md). `full_of` (`FieldNOf.lean:37–49`), `fieldN_of` (`FieldNOf.lean:52–81`).

There are three final local cases. At a split place, choose the subquotient given by split compatibility and use spherical compatibility if needed. At a nonsplit unramified place, use the returned Satake tuple to obtain a spherical local subquotient with the required parameters. At a nonsplit place where the unitary datum is ramified, the local condition allows a subquotient without the special unramified conclusion. The local choices can then be made for every place with a fixed global partition and its fixed archimedean weight data. The common datum is the issue a hand reconstruction must account for. `fieldN_of` (`FieldNOf.lean:52–81`)

At the surface, W02 applies a conditional theorem to W16. The steps above identify what was supplied and what the global conclusion demands. The frame-matching results and their analytic input remain separate proof obligations for a self-contained reconstruction. [Role in the Selmer window](../../pillars/V.md). `baseChangeN` (`DefiniteNHolds.lean:5–6`) `bci_of` (`BciOf.lean:22–26`)

The head has no hypotheses. Its target is the in-repo formulation `BaseChangeIsobaricN`, inhabited by passing the closed finite-candidate construction to the conditional base-change theorem. `UpperTheory.BaseChangeIdentities.baseChangeN` (`Development/AutomorphicArithmetic/Foundations/BaseChangeIdentities/DefiniteNHolds.lean:5–6`). The [V-BC outline](../../units/V-BC.md) follows the finite-intersection argument for common split and inert data.

## Literature-named inputs

`UpperTheory.BaseChangeIdentities.baseChangeN` — in-repo constant (`Development/AutomorphicArithmetic/Foundations/BaseChangeIdentities/DefiniteNHolds.lean:5–6`); not compared.

**First step to challenge.** Check that the split and inert comparisons can be moved to a single global datum, with both the required subquotients and the inert Satake conclusion still belonging to the original datum. `full_of` (`FieldNOf.lean:37–49`) `fieldN_of` (`FieldNOf.lean:52–81`)
