# D155 · Fubini–Study normalization of Chow height

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 0 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**Outlined · pending_review.** A generic Chow form and the Fubini–Study metric on the projective coordinates give two descriptions of one self-intersection. The normalization includes the absolute degree of the number field and uses the same matrices that specified the metric at infinity.

## Claim and hypotheses

The published Hodge-bundle package gives the Fubini–Study expression for the height of the common Chow form.
$$
\mathrm{PublishedHodgeBundleTheorems}\ \Longrightarrow\ \mathrm{FubiniStudyChowHeight}.
$$

[`FubiniStudyChowHeightFormula₂.fubiniStudy_chowHeight_formula` · `FubiniStudyChowHeightFormula.lean:17–18`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/FubiniStudyChowHeightFormula.lean#L17-L18)

## Match the projective data

Let $Y$ be integral with the specified closed immersion into projective space over the integers of $K$, and assume the arithmetic variety dimension condition $e$. The matrices $A_\sigma$ are invertible. Over conjugate embeddings their values agree after complex conjugation and right multiplication by a unitary matrix. This is the compatibility required for the real norms. For a Chow form $f$ of block degree $\delta$ the target value is $[K:\mathbf Q]$ times its form height with identity finite matrix and frames $A$ at infinity. It is the self-intersection of the pulled-back metrized hyperplane line. [`GlobalTheory.Published.FubiniStudyChowHeight` · `FubiniStudyChowHeight.lean:17–30`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/FubiniStudyChowHeight.lean#L17-L30)

## Construct a common metrized line

The hypothesis record supplies its arithmetic-calculus field and hence the existence of arithmetic intersections. Construct the Fubini–Study line on projective space using the coordinate sections, which cover it. Pull the line back along the fixed immersion and use arithmetic existence to choose a self-intersection for it. The norm at each embedding is obtained from the given invertible matrix. The unitary right factor makes the associated norm compatible with conjugation. Pullback of coordinate sections preserves the Fubini–Study property for each embedding. [`FubiniStudyChowHeightFormula₂.fubiniStudy_chowHeight_formula` · `FubiniStudyChowHeightFormula.lean:17–18`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/FubiniStudyChowHeightFormula.lean#L17-L18) [`FubiniStudyChowHeightFormula₂.fubiniStudyChowHeight_of` · `FubiniStudyChowHeightOfArExists.lean:152–153`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/AbelianHeightsDuality/FubiniStudyChowHeight/FubiniStudyChowHeightOfArExists.lean#L152-L153) [`FubiniStudyChowHeightFormula₂.fubiniStudyChowHeight_of_arExists` · `FubiniStudyChowHeightOfArExists.lean:109–124`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/AbelianHeightsDuality/FubiniStudyChowHeight/FubiniStudyChowHeightOfArExists.lean#L109-L124)

## Identify the polynomial seen by the coordinate sections

The generic ideal of those sections is the scalar extension of the homogeneous ideal at the generic point of $Y$. Rewrite the ideal before using the incidence characterization of $f$. The forward implication uses divisibility from universal vanishing, and the converse uses vanishing of a multiple wherever its factor vanishes. The multihomogeneous degree condition is checked one block at a time on every monomial in the support. This ensures that the same $f$ and $\delta$ enter the intersection computation. [`FubiniStudyChowHeightFormula₂.fubiniStudyChowHeight_of_arExists` · `FubiniStudyChowHeightOfArExists.lean:125–142`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/AbelianHeightsDuality/FubiniStudyChowHeight/FubiniStudyChowHeightOfArExists.lean#L125-L142)

## Evaluate the recursive height with these frames

The comparison invoked here combines a vertical calculation, an archimedean chart calculation, the Chow-height recursion and the section and product formulas. These are the substantive geometric inputs retained in this outline. Applied to the metrized line and $f$, the comparison gives the chosen intersection in an auxiliary normalization. In the conversion to form height, the inverse matrix of the resulting local norm is the original $A_\sigma$, by invertibility. Rewriting by that equality and the comparison yields a witness for the claimed self-intersection. [`FubiniStudyChowHeightFormula₂.Fs.stMain` · `FubiniStudyChowHeightOfArExists.lean:92–95`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/AbelianHeightsDuality/FubiniStudyChowHeight/FubiniStudyChowHeightOfArExists.lean#L92-L95) [`FubiniStudyChowHeightFormula₂.fubiniStudyChowHeight_of_arExists` · `FubiniStudyChowHeightOfArExists.lean:143–150`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/AbelianHeightsDuality/FubiniStudyChowHeight/FubiniStudyChowHeightOfArExists.lean#L143-L150)

## First step to challenge

Check that the ideal detected by the pulled-back sections is the generic ideal in the Chow-form hypothesis. Then recover the original matrices from the inverse archimedean norms.

For the hyperplane section underlying the height recursion see [D154](../../units/D154.md). For the use of a height comparison on an image model see [T16](../../units/T16.md).

## Literature-named inputs

`GlobalTheory.CovTop.PublishedHodgeBundleTheorems.p4` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/ToKnownTheoremsOf.lean:11`); not compared.
