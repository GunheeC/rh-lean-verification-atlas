# D575 · Green's parameterization of finite cuspidal characters

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 280 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**Outlined · pending_review.** A classification indexed by regular multiplicative characters can be read using monic irreducible polynomial labels. The argument identifies Frobenius orbits on the two sides, including the value on a matrix with irreducible characteristic polynomial and the uniqueness and exhaustion of the labels.

## Claim and hypotheses

Assume the regular-character classification for finite general linear groups. For every prime field size g, permitted character pairing L and degree d>0, index the cuspidal characters by monic irreducible polynomials of degree d with nonzero constant coefficient. The characters have the prescribed degrees and Frobenius-orbit value formula; the labels identify equal characters and exhaust the cuspidal ones.
$$
\mathrm{GreenRegularCharacters}\ \Longrightarrow\ \mathrm{GLq.Green}.
$$

[`GlobalTheory.GreenBridge.green_of_regular` · `SumRangeEqRoots.lean:225–304`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/SumRangeEqRoots.lean#L225-L304)

## Read the input on regular orbits

Fix the prime $g$, degree $d>0$ and the permitted label datum $L$. Apply the hypothesis to the chosen degree-$d$ finite field. It supplies a function $\tau$ on multiplicative characters, an orbit criterion for equality and exhaustion of cuspidals. On regular characters it gives the degree $\prod_{1\le i<d}(g^i-1)$ and a signed Frobenius sum on each matrix with irreducible characteristic polynomial. The pairing in $L$ translates root parameters into characters. These classification facts are assumptions for this conversion. [`GlobalTheory.Published.GreenRegularCharacters` · `GreenRegularCharacters.lean:13–20`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/PublishedTheorems/GaloisCohomology₂/GreenRegularCharacters.lean#L13-L20) [`GlobalTheory.GreenBridge.green_of_regular` · `SumRangeEqRoots.lean:225–234`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/SumRangeEqRoots.lean#L225-L234)

## Build a regular label and compute its value

Choose one root $x_0$ of the monic irreducible polynomial $P$. Its nonzero constant term gives a unit parameter. The first $d$ Frobenius powers are distinct, so the character associated to $x_0$ by the chosen pairing is regular and the input classification applies. For a test matrix $y$, its determinant is nonzero, hence its characteristic polynomial has nonzero constant term. A chosen root $z$ of that polynomial can therefore be lifted to a unit in the fixed degree-$d$ finite field. It is at that unit that the character formula evaluates. [`GlobalTheory.GreenBridge.regular_iff` · `SumRangeEqRoots.lean:207–212`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/SumRangeEqRoots.lean#L207-L212) [`GlobalTheory.GreenBridge.green_of_regular` · `SumRangeEqRoots.lean:228–258`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/SumRangeEqRoots.lean#L228-L258)

## Remove the arbitrary choices of roots

Any permissible root of $P$ is $x_0^{g^j}$. Replacing the characteristic root $z$ by $z^{g^j}$ permutes the root sum. The compatibility of the pairing with powers moves that factor over to the label $x_0$. Thus the original formula gives the same test value for every choice required by the conclusion. Conversely, equality of assigned characters puts their regular parameters in the same Frobenius orbit. The injectivity of the pairing recovers the same orbit of roots, and their monic irreducible minimal polynomials agree. [`GlobalTheory.GreenBridge.green_of_regular` · `SumRangeEqRoots.lean:256–280`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/SumRangeEqRoots.lean#L256-L280)

## Recover a polynomial for every cuspidal character

Write the given cuspidal character as $\tau(\theta)$ with $\theta$ regular. Surjectivity of the parameterization writes $\theta$ using a root parameter $x$. Its minimal polynomial has positive degree dividing $d$, since $x$ is fixed by the $d$th Frobenius iterate. If that degree were smaller, Frobenius at that exponent would fix $x$, contradicting regularity by comparison with exponent zero. As $x$ is nonzero, this minimal polynomial is an allowed label. Its chosen root lies in the orbit of $x$; the orbit criterion returns the original character. The final reassignment is routine only after recovering degree $d$. [`GlobalTheory.GreenBridge.green_of_regular` · `SumRangeEqRoots.lean:281–304`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/SumRangeEqRoots.lean#L281-L304)

## First step to challenge

For an arbitrary regular character, prove that the minimal polynomial of its root parameter has degree exactly $d$. A degree dividing $d$ would allow labels of the wrong size.

For the use of the Green input in the family construction see [B05](../../units/B05.md) and the complete list of conditional inputs in [V4-COND](../../units/V4-COND.md).

The main route supplies the regular-character hypothesis inside Lean. Its wrapper takes an open-literature argument but returns `PositivityTheory.Stage1.PM.greenRegularCharacters` directly. The parameter field here has prime cardinality. `UpperTheory.LiteratureTheorems.green_regular_characters_of_literature` (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean:399–400`). `GlobalTheory.GreenBridge.green_of_regular` (`Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/SumRangeEqRoots.lean:225–229`).

## Literature-named inputs

`GlobalTheory.Published.GreenRegularCharacters` — hypothesis at this head (`Development/AbelianVarietyTheory/PublishedTheorems/GaloisCohomology₂/GreenRegularCharacters.lean:13–20`); variant.

`UpperTheory.LiteratureTheorems.green_regular_characters_of_literature` — in-repo constant (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean:399–400`); variant.

`GlobalTheory.GreenBridge.green_of_regular` — in-repo constant (`Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/SumRangeEqRoots.lean:225–304`); not compared.
