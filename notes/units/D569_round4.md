# D569 · Transport of the main term across the finite bijections

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 25 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**Outlined · pending_review.** Two finite bijections identify the lattice indices with the arithmetic indices. They transport the main term exactly, including its averaging factor. This lets the gap computation subtract the same main term on both sides.

## Claim and hypotheses

Assume the per-unit arithmetic/lattice identifications, including the chosen bijections onto TT and the character set. Then for every u, Main(u) equals the sum over t in TT and j<m of the real part of MAIN(ell,a(t),w(tr(u),j)).
$$
\mathrm{Main}(u)=\sum_{t\in TT}\sum_{j<m}\operatorname{Re}\mathrm{MAIN}(\ell,a(t),w(\mathrm{tr}(u),j)).
$$

[`Deduction.ch_top_main_eq` · `ChTop.lean:11–35`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/ChTop.lean#L11-L35)

## Name the two changes of index

Fix the unit $u_0$. The first equivalence carries the lattice top-index type to the subtype of elements of the finite set $TT$. The second carries the $f$ coefficient indices to the subtype of the arithmetic set $\Phi$. They come with more than cardinality data. The identification predicate matches the first coordinate parameter, every individual width, the constant and the real part of the selected character value; it also has a separate request identity. Only the first four clauses are needed for this main-term calculation. [`Deduction.CH.IdentU` · `SplitInertia.lean:67–72`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/DedekindLFunctions/SplitInertia.lean#L67-L72) [`Deduction.ch_top_main_eq` · `ChTop.lean:11–21`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/ChTop.lean#L11-L21)

## Transport the coefficient average

The second equivalence gives $f=\#\Phi$, first as a natural-number cardinality and then in the real denominator for the average. For every real function $G$ on the ambient product group it also gives $\sum_{\rho<f}G(e_P(\rho))=\sum_{x\in\Phi}G(x)$. Regard the right-hand sum as a sum over the finite subtype; the equivalence reindexes it term by term. Keeping the denominator avoids changing a mean into an unnormalized sum. No estimate of the individual terms is involved. [`Deduction.ch_top_main_eq` · `ChTop.lean:17–25`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/ChTop.lean#L17-L25)

## Transport the top indices and the real part

Expand the lattice main term, replace the four matched quantities, and use the coefficient sum and cardinality identities. Interchange the two remaining finite sums, then use the first equivalence on the top index. For a fixed $t,j$ expand the arithmetic expression MAIN and take its real part. Its width term contains exactly the real function $x\mapsto\log w(\mathrm{tr}(u_0),j,x)$, so the same coefficient identity applies again. This proves equality with the same weights and the same translated unit. [`Deduction.ch_top_main_eq` · `ChTop.lean:22–35`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/ChTop.lean#L22-L35)

## Where the request identity enters (downstream application)

The arithmetic gap involves a difference between a request and a main term. In the enclosing argument the unused request clause rewrites the request, while this unit rewrites the main term. Subtracting the finite sums produces the exact arithmetic gap at $\mathrm{tr}(u_0)$; the pointwise lattice bound then applies. The reindexing is routine given the equivalences and identifications. Constructing them from arithmetic comparison data is outside the present equality. [`Deduction.ch_top` · `ChTop.lean:37–55`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/ChTop.lean#L37-L55)

## First step to challenge

Verify the character-set cardinality in the averaging factor and the logarithmic width at each image index. Equal cardinalities without pointwise identification cannot transport the main term.

The equality is used in [B10](../../units/B10.md). The Gaussian estimate at the same unit is in [D568](../../units/D568.md).
