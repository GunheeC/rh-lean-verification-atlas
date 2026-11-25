# D082 · Comparing two restrictions of a finite cocycle

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 6,375 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**pending_review** · [Unit card](../../units/D082.md) · [Track guide](../../tracks/local/README.md)

A continuous cocycle satisfying the finite condition on the chosen local group satisfies it on the decomposition subgroup, and conversely. Extending a witness from a subgroup requires division by a finite index in the rational coefficient field. `UpperTheory.V.Loc.bkAbove` ([BkAbove.lean:47–79](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/PadicHodgeTheory/BkAbove.lean#L47-L79)).

## Identify the two local actions

Take a number field $F$, an algebraic closure and an embedding $j$ into the local algebraic closure at a prime $\ell$. The topological group $H$ maps to the global Galois group by $\psi$ and by an open embedding $\varphi$ to the local group. Their actions agree after $j$. Thus the map $h\mapsto(\psi(h),\varphi(h))$ lands in the indicated decomposition subgroup. Its second projection is an open embedding; its first projection gives the action on the original representation. The cocycle is taken for the specified coefficient algebra and continuous representation over the $\ell$-adic rationals. `UpperTheory.V.Loc.bkAbove` ([BkAbove.lean:47–79](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/PadicHodgeTheory/BkAbove.lean#L47-L79)).

## Restrict a witness, or locate the finite-index subgroup

A crystalline-period coboundary witness on the decomposition subgroup pulls back along the paired map. In the other direction the witness initially works only over $H$. Compactness of the local Galois group and openness of $\varphi(H)$ make its index finite. Pull this subgroup back along the second projection. Its elements come from $H$ because that projection is injective and the two maps have the stated agreement. Thus the period-valued cocycle is already a coboundary on this finite-index subgroup. Continuity of the cocycle under the two restrictions follows from the projection and embedding properties. `UpperTheory.V.Loc.bkAbove` ([BkAbove.lean:47–79](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/PadicHodgeTheory/BkAbove.lean#L47-L79)).

## Average with the right sign

For a cocycle $f$ and an existing witness $x$, subtract $g x-x$ to obtain $f'$, which vanishes on the subgroup. Now $f'(gh)=f'(g)$ for $h$ in the subgroup, so $f'$ descends to the cosets. Write $S$ for the sum of those values and $d$ for the index. The cocycle law and permutation of the cosets give $S=d f'(g)+gS$. It follows that $x-d^{-1}S$ is a coboundary witness for the original cocycle. This argument requires only a finite-index subgroup, without a normality assumption, and makes its division in characteristic zero. An integral claim with the same index would require further justification. [D006](../../units/D006.md) gives a related use of the local finite condition in the torsion package. `bkAbove_avg` ([BkAbove.lean:5–45](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/PadicHodgeTheory/BkAbove.lean#L5-L45)). `UpperTheory.V.Loc.bkAbove` ([BkAbove.lean:47–79](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/PadicHodgeTheory/BkAbove.lean#L47-L79)).

## Test the two directions on a period vector

The tensor supplied to the averaging calculation is $c(p(g))\otimes1$ over the $\ell$-adic rationals, with $p$ here denoting the global projection of the decomposition group. The code verifies that the induced period action is multiplicative by induction on tensors, then uses the cocycle identity on the projected elements to obtain the period-valued cocycle identity. These are the hypotheses of the finite-index calculation. In the other direction no average is needed: evaluate the existing identity at the image of each $h$ under the paired map. Thus even though finite membership is an equivalence at the two groups, its two proofs require different data. A proposed integral version should first account for the inverse of the coset cardinality appearing only on the extension side. `UpperTheory.V.Loc.bkAbove` ([BkAbove.lean:47–79](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/PadicHodgeTheory/BkAbove.lean#L47-L79)). `bkAbove_avg` ([BkAbove.lean:5–45](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/PadicHodgeTheory/BkAbove.lean#L5-L45)).

**First step to challenge.** Check why the subgroup on which a witness is known has finite index and why its index is invertible in the coefficient field used for averaging.
