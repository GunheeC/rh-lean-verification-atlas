# W04 · Weak unitary descent in ranks two through four

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 9 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**Outlined · pending_review.** An eligible conjugate-self-dual cuspidal representation in ranks two through four has a weak descent to the specified unitary group. The descent is unramified at nonsplit places and matches the given Satake parameters at all but finitely many split places.

## Statement and hypotheses

Let $E/E^+$ be CM and unramified at finite places. Fix a prime $p$ and a
finite set $S$ of finite places of $E^+$ containing those above $p$,
all split in $E$. Let $2\le n\le4$ and let $\pi$ be a regular algebraic
cuspidal representation of $\mathrm{GL}_n(\mathbb A_E)$ with
$\pi^\vee\simeq\pi^c$ and Satake parameters at all places above the
complement of $S$. There exists an automorphic representation $\sigma$ of
the specified unitary group, unramified at every nonsplit finite place.
At all but finitely many split $w$ the component of $\sigma$, read
on $\mathrm{GL}_n(E_w)$, has the same Satake multiset as $\pi_w$. [`descWeak` · `HasOfSplit.lean:29-30`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/TraceFormula/SplitRigidity/HasOfSplit.lean#L29-L30)

**Read alongside** [W02 · Isobaric base change for the definite unitary group](../../units/W02.md) · [T03 · Building the definite-side family from unramified row data](../../units/T03.md).

## Use the right set of local hypotheses

Fix the CM extension, unramified at finite places, the split exceptional set and regular algebraic cuspidal representation as in the unit statement. The internal descent assertion takes positive rank and asks for Satake parameters at every nonsplit place. A nonsplit place cannot lie above the specified exceptional set since all places in that set are split. Use the supplied Satake condition there. The lower rank restriction in the public result implies positive rank. This specialization does not enlarge the exceptional set in the conclusion, which states cofinite matching at split places. [`DescWeakAll` · `HasOfSplit.lean:20-30`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/TraceFormula/SplitRigidity/HasOfSplit.lean#L20-L30)

## Obtain a trace-formula alternative

The all-ranks internal deduction uses the trace-comparison alternative with the regularity, duality and nonsplit information just described. The formal source builds that alternative from a trace identity, finiteness, admissibility, a twisted trace sum and a spectral growth estimate. In the failure branch there is candidate decomposition data excluding the original representation, together with regularity and equality of Satake data almost everywhere on split places. To remove this branch it suffices to show that the candidate does contain the original representation. The construction of the alternative is an input to this outline. [`runTh` · `DescWeak.lean:9-9`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/TraceFormula/GaloisFromTraceFormula/DescWeak.lean#L9-L9) · [`descWeakAll` · `HasOfSplit.lean:26-27`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/TraceFormula/SplitRigidity/HasOfSplit.lean#L26-L27)

## Rule out the failure branch

Apply split rigidity to the cuspidal representation and the candidate list, indexed by its finitely many constituents and their positive ranks. Conjugate self-duality supplies the unitarity input for the original representation. For each constituent the part-normalization calculation uses the regularity and cofinite split agreement to identify a unitary representation to which it is equal. Transfer unitarity across that identification. At a split place in the cofinite set, unpack the candidate Satake multiset into its underlying tuple and apply equality with the cuspidal Satake parameters. These are the hypotheses used by rigidity. Its conclusion contradicts the exclusion in the trace alternative. [`has_of_split` · `HasOfSplit.lean:11-18`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/TraceFormula/SplitRigidity/HasOfSplit.lean#L11-L18) · [`splitRigid` · `SplitRigid.lean:12-13`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/TraceFormula/SplitRigidity/SplitRigid.lean#L12-L13)

## Scope of the surviving alternative

The surviving witness is an automorphic subrepresentation on the unitary group, unramified at every nonsplit place. At cofinally many split places it supplies a local irreducible representation and one Satake multiset read on both sides. The exceptional split places may still be exceptional. This is a weak comparison at the specified places, so any later application needing a specified component at every place must supply that stronger conclusion independently. [`DescWeakAll` · `HasOfSplit.lean:20-30`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/TraceFormula/SplitRigidity/HasOfSplit.lean#L20-L30)

**First step to challenge.** Check the split rigidity argument for a candidate decomposition with matched Satake multisets. It must identify the original cuspidal representation after obtaining unitarity for every constituent.

[Unit record and exact statement](../../units/W04.md)
