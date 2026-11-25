# D123 · Arakelov degree of the normalized flat generator

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 9,501 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**Outlined · pending_review.** A flat generator in a particular CM frame carries prescribed norms at the infinite and finite places. The unit computes their normalized degree from a CM period and the root discriminant. This supplies an exact input to the tower calculation, including the finite contribution that an archimedean period alone would miss.

## Claim and hypotheses

Give an adelic norm to the flat generator. Its degree is (p−q)/2 times the real CM period logarithm plus q times twice the logarithm of the square root of d minus the logarithm of the root discriminant.
$$
N\ \text{adelic},\qquad \deg N=\tfrac{p-q}{2}\operatorname{Re}\log\Omega(E,\chi)+q\bigl(2\log\sqrt d-\log\operatorname{rd}(E)\bigr).
$$

[`GlobalTheory.T.FlatDegree_holds` · `FlatDegreeHoldsStatement.lean:5–6`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicSpectrum/Proofs/GeometryProofs/FlatDegreeHoldsStatement.lean#L5-L6)

## Which generator is being measured?

Fix the moduli datum, its chosen uniformized family and index, the open set, embedding and frame function. The hypotheses identify that frame function as a flat generator and identify its logarithmic norms with the given system $N$. In particular the choice of embedding sends the distinguished square root to the prescribed complex value. The character is the Kronecker character at the host modulus. The assertion concerns the assigned norms of this generator. A general choice of frame or unrelated family of local norms would lose the two comparisons that enter the calculation. [`GlobalTheory.CompanionTheory.Ar.Fl.FlatDegree` · `FlatDegree.lean:12–19`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicSpectrum/Statements/GeometryStatements/FlatDegree.lean#L12-L19)

## Match the two archimedean periods

The signs of the square root give two CM period data. Both logarithmic period parameters equal the same real number because their images in the complex numbers have the same expression. The CM value of the frame supplies a common finite extension $k$ containing the coefficient data and the period fields. The proof takes normalized sums over embeddings into the complex numbers. On extending a number field each base embedding is counted with its extension multiplicity. Division by the absolute degree cancels that factor, so both period means survive passage to $k$. [`GlobalTheory.CompanionTheory.Ar.Fl.flatDegree` · `FlatDegreeHolds.lean:60–89`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicSpectrum/Proofs/GeometryProofs/FlatDegreeHolds.lean#L60-L89) [`GlobalTheory.CompanionTheory.Ar.Fl.flatDegree_mean_ext` · `FlatDegreeHolds.lean:21–28`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicSpectrum/Proofs/GeometryProofs/FlatDegreeHolds.lean#L21-L28)

## Keep the finite correction

For each prime the frame-height comparison supplies a local factor. A local basis condition at all but finitely many primes forces its logarithmic norm to vanish there for every relevant embedding. Its exceptional set is therefore contained in the finite set from the Gram determinant calculation. Complex conjugation in the CM field permutes embeddings into the local coefficient field. The sum for the conjugate factor consequently equals the original sum. Both finite support and the conjugate identity are inputs to the Hermitian metric formula. [`GlobalTheory.CompanionTheory.Ar.Fl.flatDegree` · `FlatDegreeHolds.lean:74–113`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicSpectrum/Proofs/GeometryProofs/FlatDegreeHolds.lean#L74-L113) [`GlobalTheory.CompanionTheory.Ar.Fl.flatDegree_sum_conj` · `FlatDegreeHolds.lean:30–39`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicSpectrum/Proofs/GeometryProofs/FlatDegreeHolds.lean#L30-L39)

## Descend and identify the coefficient

Over $k$ the metric formula gives an adelic system together with its degree. The extension-of-norms result identifies degrees and gives the equivalence of adelicity needed to descend the conjunction. In rewriting the real part of the CM period, positivity of the root discriminant and of the square root of the modulus permits the logarithms of quotients to split. This last algebraic rewrite is routine once the local and archimedean comparisons have been supplied. The constructions of the CM period and the metric formula remain named inputs of this outline. [`GlobalTheory.CompanionTheory.Ar.Fl.flatDegree_logOm_re` · `FlatDegreeHolds.lean:41–58`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicSpectrum/Proofs/GeometryProofs/FlatDegreeHolds.lean#L41-L58) [`GlobalTheory.CompanionTheory.Ar.Fl.flatDegree` · `FlatDegreeHolds.lean:95–118`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicSpectrum/Proofs/GeometryProofs/FlatDegreeHolds.lean#L95-L118)

## First step to challenge

Trace the finite logarithms outside the exceptional Gram primes, then check the descent of both adelicity and degree from the common coefficient extension.

Read [T26](../../units/T26.md) for the tower that uses this degree and [P049](../../units/P049.md) for the separate determinant calculation in the span.
