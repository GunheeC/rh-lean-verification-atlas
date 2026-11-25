# T16 · The Chow height of an image model

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 30,511 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**Outlined · pending_review.** For an integral image model with its specified sections and conjugation-compatible metrics, one controls a shifted self-intersection by the image degree and image height. This turns arithmetic information on the model into a bound expressed in the coordinates of the image.

## Claim and hypotheses

Assume the Hodge-bundle record. Let $K$ be a number field with no real
embeddings, $V$ a $K$-module compatibly acted on by $\mathcal O_K$, and
$\Omega/K$ a field. Let $N_\sigma$ on $V$ have Gram data and be invariant
under conjugating $\sigma$. Let $W\subset V$ be a finitely generated
$\mathcal O_K$-module spanning $V$ over $K$, and
$\mathrm{ev}:V\to\Omega$ linear with generating ratios. For degree index
$D\ge0$ suppose $d=\mathrm{imageDeg}(\mathrm{ev},D)>0$.
Let $(X,L)$ be its integral image model over $\mathcal O_K$ with the
specified embedding $\Omega\to K(X)$ and sections indexed by $W$ for
$N_\sigma,W,\mathrm{ev},D$. If the constant metric shift $L(t)$ has
self-intersection $a$, then
$$
 a\le [K:\mathbb Q]\,(D+1)d\,
       \bigl(\mathrm{imageHeight}(N,W,\mathrm{ev},D)+t\bigr).
$$

[`ChowFormHeightComparison₂.chow_form_height_comparison` · `ChowFormHeightComparison.lean:11–12`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/ChowFormHeightComparison.lean#L11-L12)

## What the bound measures

Fix the shift $t$ before making comparisons. The target keeps the same evaluation map, positive image degree and finitely generated spanning lattice all the way to the image height. In particular the multiplier is the absolute degree times $D+1$ times the image degree. The witness $a$ is a self-intersection for this shift on the supplied model. The construction must recover that value after changing the presentation of the model and its sections. [`ChowFormHeightComparison₂.chow_form_height_comparison` · `ChowFormHeightComparison.lean:11–12`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/ChowFormHeightComparison.lean#L11-L12)

## Supply the height comparison and the rational model

The first input is a height bound from the archimedean computation on points and charts, the Mahler section statement, and arithmetic existence from the Hodge-bundle record. The proof then extracts a point of the given model from its generic identification and base compatibility. Its projectivity supplies properness. The point, its residue-field data and the structural morphism define the rational model used in the next comparison. The underlying integral scheme stays fixed; the new data identify its generic sections with the field of values. [`ChowFormHeightComparison₂.chow_form_height_bound` · `ChowFormHeightComparison.lean:9–10`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/ChowFormHeightComparison.lean#L9-L10) [`PositivityTheory.UnitarySelfGeneration.weil_height_inequality` · `WeilHeightInequality.lean:10–18`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/WeilHeightInequality.lean#L10-L18)

## Carry the sections across the identification

Take the frame, coordinate generators and comparison data supplied by the Fubini–Study part of the image-model hypothesis. The matrix estimate supplies determinant and conjugation compatibility for the chosen frame. To generate the model line, check the ratio for two indexed sections at a general point. A local generator at that point lets the image-model ratio condition be read in the chosen field. Base-point freeness, the original spanning condition and the frame spanning identity give the generating family to which the intersection comparison applies. [`PositivityTheory.UnitarySelfGeneration.weil_height_inequality` · `WeilHeightInequality.lean:17–26`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/WeilHeightInequality.lean#L17-L26)

## Read the last equality at the correct shift

The volume/self-intersection comparison now receives the Chow height input, the model, its divisor relation, the chosen family of sections and their metric matrices. An isometry to the relevant Fubini–Study model is constructed with the same $t$. It transports the resulting intersection back to the original line. Uniqueness of self-intersection on the arithmetic model identifies it with $a$. The terminal ring identity rearranges the factors in the displayed bound. The outline uses the earlier height and volume comparisons as inputs and does not derive them from an arbitrary projective embedding. [`PositivityTheory.UnitarySelfGeneration.weil_height_inequality` · `WeilHeightInequality.lean:26–31`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/WeilHeightInequality.lean#L26-L31)

## First step to challenge

Check the identification of section ratios in the constructed rational model with the original evaluation ratios. The isometry and uniqueness comparison must concern the same shifted metrized line.

Read [D155](../../units/D155.md) on Fubini–Study normalization and [T13](../../units/T13.md) for the surrounding covolume input.

## Literature-named inputs

`GlobalTheory.CovTop.PublishedHodgeBundleTheorems.p4` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/HodgeBundleWeights/ToKnownTheoremsOf.lean:11`); not compared.
