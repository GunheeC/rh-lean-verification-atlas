# T17 · Why the small-section volume bounds the top intersection

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**Outlined · pending_review.** Read this alongside [the statement and v3 locator](../../units/T17.md). The argument has two dimension cases. In the arithmetic curve case one can see directly how an additive error in a count disappears. In higher dimensions the geometric step is a comparison with ample perturbations.

## Fix the actual inequality

Write $P$ for the multihomogeneous vanishing ideal of a finite collection of coordinate blocks $y$ in a field. Assume that $P$ presents an arithmetic variety of dimension $D+1$, the presentation by $y$ is birational, and $I$ satisfies the intersection-system axioms. Fix a Hermitian line $A$, invariant under complex conjugation and semipositive relative to an ideal $P_0\subseteq P$. Its multidegree is nef on fibres. Its generic nef condition tests nonnegativity of geometric degree on arithmetic subvarieties of dimension two. Define $Q$ to be the source's small-section predicate for $(P,y,A)$ and $L_k$ its degree-$k$ chart lattice. The target is

$$
T=I_P(A^{D+1})\ \le\ \operatorname{arVolP}(Q,L,1,D).
$$

The parameter $1$ means we take the normalized counts along all positive integer powers. The related Hilbert–Samuel convergence statement assumes nonnegative heights of arithmetic curves and asks for a limit. Here we need an upper bound on $T$ by a limsup, using the given lattice, for every admissible $I$. The two statements occur next to each other. Source: `MoriwakiBigStatement` (`MoriwakiSt.lean:29–36`) and `MoriwakiHSStatement` (`MoriwakiSt.lean:18–27`); the generic nef predicate is defined just above them.

## Positive relative dimension

For $D\ge1$, split according to the sign of the generic degree of the multidegree of $A$. If it is positive, the data form the nef-and-big tuple required by the small-section lower estimate: take in order $P_0\subseteq P$, relative semipositivity, conjugation invariance, fibre nefness, and positivity of generic degree. Its characteristic-zero hypothesis follows here from horizontality. Indeed, a natural number vanishing in the coefficient field would give a constant polynomial in $P$. The contraction of a horizontal ideal to the integers is zero, forcing that natural number to be zero. Applying the positive-degree estimate gives precisely the displayed inequality for the original $Q,L$. Source: `charZero_of_isHorizontal` (`CharZeroOfIsHorizontal.lean:12–21`), `G6.StatementB` (`StatementsArith.lean:395–400`) and `ArithmeticVolumeBig.proof` (`CharZeroOfIsHorizontal.lean:23–28`).

If the degree fails to be positive, the remaining comparison accepts the weak inequality “generic degree at most zero.” This alternative matters: applying the positive-degree estimate a second time would require a missing hypothesis. In the construction of the second estimate, the auxiliary nef-plus-ample degree bound enters the shift of the line, bounded-height points enter the separation of sections, and lattice finiteness is used in passing from separated sections to a count. Shifted volume control, the polynomial identities for the shifted intersection and shifted degree, and the ample counting result feed the nonpositive-degree argument. Its output has the original unshifted line and chart lattice, so either branch proves the same inequality. These are named geometric inputs to this outline. Source: `hsChain` (`HSChain.lean:258–274`), especially the construction of the two final estimates, and `ArithmeticVolumeBig.Statement` (`StatementsArith.lean:404–410`), `ArithmeticVolumeBig.proof` (`CharZeroOfIsHorizontal.lean:23–28`).

## Arithmetic dimension one

For $D=0$ set $c_k$ equal to the logarithmic small-section count in $L_k$. The curve counting result gives a constant $C$ with $kT-C\le c_k$ for all $k\ge1$. Here the underlying construction proceeds from control of the index of the integral lattice and a box count on its number-field realization. The chart lattice is shown full for that count; replacing it by all elements of the ambient field would lose the comparison. The proof also applies the packing estimate to the chart lattice through its inclusion in the normalized lattice. It gives an upper bound of the form $c_k\le C'(k+1)$. Nonnegativity of the count makes $C'\ge0$. Source: `CurveCountLower.Statement` (`StatementsCurveCountLower.lean:9–16`), `hsChain` (`HSChain.lean:293–303`), `MoriwakiBigCurve.proof` (`PMoriwakiBigCurve.lean:15–47`) and `chartLat_le_chartLatNm` (`PMoriwakiBigCurve.lean:11–13`).

The normalization in dimension zero is $k^{0+1}/(0+1)!=k$. For $k\ge1$, $c_k/k\le2C'$, so the sequence is bounded above on the tail in the ordinary real line. Fix $\eta>0$ and take $k$ large enough that $C\le k\eta$. Division of the lower estimate by $k$ gives $T-\eta\le c_k/k$ for every such $k$. Thus the limsup is at least $T-\eta$ for every $\eta>0$, and letting $\eta$ decrease gives $T\le\operatorname{arVolP}(Q,L,1,0)$. This passes only to the limsup and uses the same $Q,L$ as the target. Source: `MoriwakiBigCurve.proof` (`PMoriwakiBigCurve.lean:15–47`), lines 24–47, and `MoriwakiBigCurve.Statement` (`StatementsMoriwakiBigCurve.lean:13–20`).

## Common inputs and review boundary

The dimension split now exhausts the natural numbers. The positive-dimensional comparison in this application does not consume the separately supplied generic-nef proof; the curve interface accepts it. The compiled assembly takes precisely the volume-big and curve components of a five-part package. It obtains resolution, an arithmetic intersection-system theorem from Poincaré–Lelong and that same resolution, and the dense bounded-height input. The resulting statement still quantifies over the particular admissible intersection system $I$ fixed at the outset. Source: `MoriwakiBig.of_found` (`MoriwakiBig.lean:11–16`), `moriwakiBig_of_classicalTheorems` (`HSChain.lean:365–370`), `arith_intersection_system_of_poincare_lelong` (`ArithIntersectionSystemOfPoincareLelongStatement.lean:11–12`) and `moriwakiBig_outright` (`Outright.lean:9–11`).

A referee should first examine the nonpositive-degree estimate and its use of dense bounded-height points to separate small sections on the shifted line. That is where a change of lattice or semipositivity hypothesis could invalidate transfer to the limit. The short wrapper alone does not establish this geometric estimate on paper. The surrounding covolume argument and its other inputs are indexed in [T15](../../units/T15.md).

## Round 4 source comparison

The hypothesis-free supplier `moriwakiBig_outright` proves the project's specific `MoriwakiBigStatement` from repository terms: resolution `resK`, the intersection-system theorem applied to `poincareLelong` and that resolution, and bounded-height density `DenseCurves.main`. The external formulation and proof have not been shown equivalent to the full statement with the source's chart lattice and intersection-system quantifiers.

[`PositivityTheory.Pf1.HilbertSamuelMoriwaki.moriwakiBig_outright` · `Outright.lean:9–11`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/AutomorphicKernels/MoriwakiBigness/MoriwakiBigTheorem/Outright.lean#L9-L11) · [`ReciprocityTheory.ChartRestriction.G.ArakelovGeometry.MoriwakiBigStatement` · `MoriwakiSt.lean:29–36`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/ArakelovGeometry/MoriwakiSt.lean#L29-L36)

## Status of literature-named inputs

- `PositivityTheory.Pf1.HilbertSamuelMoriwaki.moriwakiBig_outright` — in-repo constant (`Development/WeilBound/CoreStatements/AutomorphicKernels/MoriwakiBigness/MoriwakiBigTheorem/Outright.lean:9–11`); variant.
- `GlobalTheory.T.arith_intersection_system_of_poincare_lelong` — in-repo constant (`Development/AutomorphicSpectrum/Proofs/MetricProofs/ArithIntersectionSystemOfPoincareLelongStatement.lean:11–12`); not compared.
- `PositivityTheory.Tls2.Pl.poincareLelong` — in-repo constant (`Development/WeilBound/CoreStatements/TemperedRepresentationTheory/PoincareLelong/PoincareLelongInv.lean:13–17`); not compared.
