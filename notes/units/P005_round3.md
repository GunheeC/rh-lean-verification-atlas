# P005 · Reflect a primitive zero across the middle of the strip

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**pending_review** · Reading outline against Lean commit `40e56bab026552e089d7afcfeff08d2defb9c005`. [Unit card](../../units/P005.md)

## Fix the character and isolate the input

Let $N>0$ and let $\chi$ be a primitive complex Dirichlet character of modulus $N$. We are given $0<\Re s<1$ and $L(s,\chi)=0$. The target is $\Re s=1/2$. The public definition places primitivity before the universal quantifier over $s$ in `PrimitiveDirichletLZerosOnLine` (`Statements.lean:14–16`). The export `LFunction_eq_zero_re_of_isPrimitive` (`Main.lean:12–12`) uses `critAll` (`Supplements/Kernels/MainTheorems.lean:11–13`), the primitive reflection wrapper [P007](../../units/P007.md). The following argument explains the wrapper's exact use of the all-character half-plane statement $H$, supplied by [P009](../../units/P009.md). [Manuscript v3, §6.5, p. 55](P005.tex)

The strict strip bounds exclude $s=0$ and $s=1$. Suppose the real part differs from $1/2$. If $\Re s>1/2$, apply $H$ to $N,\chi,s$ using $s\ne1$ for the disjunction permitting nonvanishing. This contradicts the zero. When $\Re s<1/2$ we have to transport the zero to the other half of the strip. The strict alternatives and direct contradiction appear in lines 11–16 and 27 of `Formalism.VW.critLine` (`Formalism/GammaFactorNonvanishing/CritLine.lean:11–27`).

## Pass to the completed function at the original point

Write $\Lambda(\chi,s)$ for the completed $L$-function. The source form of the identity at $s\ne0$ is $L(s,\chi)=\Lambda(\chi,s)/\gamma(\chi,s)$. In totalized field division a quotient can vanish if its denominator vanishes. To conclude that the numerator is zero, the proof checks the denominator. For an even character the gamma factor is $\Gamma_{\mathbb R}(s)$, and for an odd character it is $\Gamma_{\mathbb R}(s+1)$. The first argument has positive real part by the strip hypothesis. In the second case adding one keeps the real part positive. The respective gamma factors are therefore nonzero. These two cases are `Formalism.VW.gammaFactor_ne_zero` (`Formalism/GammaFactorNonvanishing/CritLine.lean:6–9`), and lines 19–21 of `Formalism.VW.critLine` (`Formalism/GammaFactorNonvanishing/CritLine.lean:11–27`) use the result to infer $\Lambda(\chi,s)=0$.

## Apply the functional equation in the needed direction

The inverse character is primitive because inversion preserves the conductor. Apply the primitive functional equation to $\chi^{-1}$ at $s$. Its left side is the completed function for the inverse character at $1-s$. Its right side contains the completed function for $(\chi^{-1})^{-1}=\chi$ at $s$, which has just been shown to vanish. Thus $\Lambda(\chi^{-1},1-s)=0$. The proof uses multiplication by a zero here and does not divide by a root number. The choice of inverse character and the simplification are in lines 17–23 of `Formalism.VW.critLine` (`Formalism/GammaFactorNonvanishing/CritLine.lean:11–27`).

Set $t=1-s$. The original bound $\Re s<1$ gives $t\ne0$, so the ordinary-to-completed formula is available there as well. Its numerator is zero, which suffices to give $L(t,\chi^{-1})=0$. On the other hand $\Re t=1-\Re s>1/2$. We also have $t\ne1$ because $s\ne0$. Apply $H$ to $N,\chi^{-1},t$ with this latter alternative in its disjunction. The two conclusions contradict one another. The argument at $t$ is in lines 24–26 of `Formalism.VW.critLine` (`Formalism/GammaFactorNonvanishing/CritLine.lean:11–27`).

Both strict inequalities have been eliminated, so equality follows under $H$. The public Lean term uses the same $N$, character, point and strip hypotheses throughout the wrapper. No change to an inducing primitive character occurs on this path, since primitivity was supplied at the start. Obtaining $H$ uniformly in the modulus remains the separate arithmetic input to this local reflection argument. [Half-plane statement](../../units/P003.md)

**First point for review.** Check that the functional equation is used for the inverse character, and that the ordinary-to-completed quotient at the original point has nonzero denominator.

## Status of literature-named inputs

- `Formalism.VW.critLine` — in-repo constant (`Formalism/GammaFactorNonvanishing/CritLine.lean:11–27`); not compared.
- `Formalism.VW.gammaFactor_ne_zero` — in-repo constant (`Formalism/GammaFactorNonvanishing/CritLine.lean:6–9`); not compared.
