# P001 · From a right-half-plane bound to the zeta zero line

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**pending_review** · Reading outline against Lean commit `40e56bab026552e089d7afcfeff08d2defb9c005`. [Unit card](../../units/P001.md)

## The input to the reduction

Fix a zero $s$ of the Riemann zeta function. The public predicate also assumes $s\ne1$ and excludes $s=-2(n+1)$ for each natural number $n$. Its conclusion is $\Re s=1/2$. The two zeta exports share the same proof term. The route for P001 uses the Mathlib predicate itself, whereas P002 spells the predicate out. The public declaration is `riemannHypothesis` (`Main.lean:4–4`), its immediate supplier is `rhOfAll` (`Supplements/Kernels/MainTheorems.lean:9–9`), and the explicit quantifiers appear in `RiemannZetaZerosOnLine` (`Statements.lean:3–4`). The manuscript places the two formulations side by side on p. 54. [v3 statement](P001.tex) · [Companion P002](../../units/P002.md)

Write $H$ for nonvanishing of every Dirichlet $L$-function in $\Re s>1/2$ subject to the principal-character exception. The substantive analytic argument at this export is an implication from $H$. The separate supplier of $H$ is [P009](../../units/P009.md). Keeping $H$ as an input isolates exactly what the reflection calculation needs.

## Specialize the character and choose the point of reflection

Take the character of modulus one. Every point in the right half-plane other than $1$ satisfies the second disjunct of $H$. The modulus-one identity equates its $L$-function with $\zeta$. We obtain a function assigning $\zeta(t)\ne0$ to every $t$ with $\Re t>1/2$ and $t\ne1$. No simplicity or isolation hypothesis on the zero enters this specialization. This is the entire call to $H$ in `Formalism.VW.rh_of_every` (`Formalism/GammaFactorNonvanishing/CritLine.lean:29–32`).

Compare $\Re s$ with $1/2$. Equality gives the desired relation. A value strictly larger than $1/2$ contradicts $\zeta(s)=0$ directly. In the remaining case put $t=1-s$, so $\Re t>1/2$. The value $s=0$ would contradict $\zeta(0)=-1/2$. Consequently $t\ne1$. Also $t$ cannot be a nonpositive integer because it has positive real part. These observations both permit the functional equation at $t$ and place $t$ in the domain of the nonvanishing input. The case division and side conditions occur in lines 5–30 of `Formalism.VW.rh_of_right` (`Formalism/GammaFactorNonvanishing/RhOfRight.lean:5–62`).

## Exclude the vanishing of every factor

The functional equation at $t$ expresses $\zeta(1-t)=\zeta(s)$ as the product

$$
2(2\pi)^{-t}\,\Gamma(t)\,\cos(\pi t/2)\,\zeta(t).
$$

The base $2\pi$ of the complex power is nonzero. The gamma factor is nonzero because $\Re t>0$, and the modulus-one specialization already gives $\zeta(t)\ne0$. For the cosine, vanishing would give $t=2k+1$ for some integer $k$, and hence $s=-2k$. If $k<0$, this makes $s$ a positive even integer, contradicting $\Re s<1/2$. If $k=0$, it gives the zero argument already excluded. If $k>0$, then $k-1$ is nonnegative and $s=-2((k-1)+1)$ violates the public hypothesis. The pinned term converts $k-1$ to a natural number explicitly before invoking that hypothesis. These factors occupy lines 31–59 of `Formalism.VW.rh_of_right` (`Formalism/GammaFactorNonvanishing/RhOfRight.lean:5–62`). Their nonzero product contradicts the original zero in its line 60.

Thus the displayed implication from $H$ supplies the zeta predicate, and the export reuses that implication with the particular term supplied by `allChi` (`Supplements/Kernels/MainTheorems.lean:7–7`). The outline leaves the construction of that term at its own card. A check of these lines can cover the modulus-one reduction, reflection and exceptional zeros while leaving the arithmetic source of the half-plane bound as a separate review obligation.

**First point for review.** The reflection step divides the cases at a negative even integer and at zero. Check the precise exclusion of each against the predicate passed to the public export.

## Status of literature-named inputs

- `Formalism.VW.rh_of_right` — in-repo constant (`Formalism/GammaFactorNonvanishing/RhOfRight.lean:5–62`); not compared.
