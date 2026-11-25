# P003 · The half-plane export and its conductor reduction

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**pending_review** · Reading outline against Lean commit `40e56bab026552e089d7afcfeff08d2defb9c005`. [Unit card](../../units/P003.md)

## The exact assertion exported

Take a positive modulus $N$, a complex Dirichlet character $\chi$ modulo $N$ and a point $s$ with $\Re s>1/2$. The extra hypothesis is $\chi\ne1$ or $s\ne1$, where $1$ denotes the principal character at modulus $N$. Thus a nonprincipal character may be tested at $s=1$, and the principal character may be tested at every point allowed by the real-part condition except $s=1$. Either alternative is sufficient. The definition including the order of these binders is `DirichletLNonvanishingRightOfHalf` (`Statements.lean:6–8`). The manuscript identifies this whole assertion with $H$. [Manuscript v3, §6.3, p. 55](P003.tex)

On the public line `LFunction_ne_zero_of_half_lt_re` (`Main.lean:8–8`), Lean uses the constant supplied at [P009](../../units/P009.md). Unfolding `UpperTheory.EveryCharacter` (`Development/AutomorphicArithmetic/CharacterBoxes/EveryCharacter.lean:13–14`) gives the same positive-modulus instance, universal character and complex variable, the same two implications and the same function value in the conclusion. Therefore a term proving the internal predicate has exactly the type required by the public predicate after unfolding. This conversion explains the short proof term. The arithmetic entering its supplier can be seen in the following more detailed conditional reduction.

## Lift nonvanishing from the conductor

Unfold the primitive input `Formalism.HC.ZeroFreeAll`: for every packaged primitive character $\psi$, the premise True gives $L(s,\psi)\ne0$ at every complex $s$ with $\Re s>1/2$. Its type has no pole-exclusion disjunction. At modulus one and $s=1$ it concerns Mathlib’s totalized L-function value. The public predicate has its own exception there. See `Formalism.HC.PChar.ZeroFreeAbove`, `Formalism.HC.ZeroFreeOn` and `Formalism.HC.ZeroFreeAll` (`Formalism/SharpRestriction/RamificationFrobenius/TotientGaloisClasses/ExplicitFormulaErrorOfHostConditions.lean:11–18`). Assume this primitive input. Let $M$ be the conductor of $\chi$ and let $\psi$ be the primitive character of modulus $M$ inducing $\chi$. The construction supplies a nonzero conductor, and applying the primitive hypothesis to the packaged character at $s$ gives $L(s,\psi)\ne0$. To use the change-of-level relation we must also have $\psi\ne1$ or $s\ne1$. If the public disjunction gives $s\ne1$, retain it. Otherwise use $\chi\ne1$. Were $\psi$ principal, changing it to level $N$ would again give the principal character. The change-of-level identity for $\psi$ would identify that character with $\chi$, a contradiction. These are the operations in lines 8–19 of `UpperTheory.Top.imprimitive` (`Development/AutomorphicArithmetic/CharacterBoxes/Imprimitive.lean:5–35`).

The change-of-level formula now expresses $L(s,\chi)$ as $L(s,\psi)$ times a finite product of local factors of the form $1-\psi(p)p^{-s}$. Consider a prime appearing in this product. We have $p>1$ and $\Re s>0$. In particular,

$$
|\psi(p)p^{-s}|\le p^{-\Re s}<1 .
$$

The inequality uses the norm bound for a Dirichlet character, which also allows a zero character value at a nonunit. It uses the real-valued positive base $p$ in the norm formula for the complex power. If the local factor vanished, the product inside the absolute value would equal one, contradicting the strict inequality. Each factor is nonzero, so its finite product times $L(s,\psi)$ is nonzero. The pinned proof performs this argument prime by prime in lines 20–35 of `UpperTheory.Top.imprimitive` (`Development/AutomorphicArithmetic/CharacterBoxes/Imprimitive.lean:5–35`). An empty prime set contributes the multiplicative identity and already fits the product proof.

## What supplies the primitive input

The passage to arbitrary characters is explicitly the last operation in `UpperTheory.Top.every_character_of_green_v_win` (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TopPlug.lean:16–18`). Its input comes from `UpperTheory.Top.zero_free_all_of_green_v_win` (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TopPlug.lean:12–15`), which consumes Green's character statement, the Selmer window and a common geometric witness. The use of $\Re s>1/2$ belongs to this upstream primitive result. The local Euler factors only require positivity of $\Re s$. This difference identifies which part of the calculation carries the difficult half-plane bound. [Primitive input P015](../../units/P015.md) · [Conditional passage P014](../../units/P014.md)

Finally `allChi` (`Supplements/Kernels/MainTheorems.lean:7–7`) supplies the internal assertion for the one-line public conversion. This outline explains both the conversion and the removal of the primitivity restriction under the indicated input. A complete derivation of the common window and its geometric datum is a separate task at their supplying units.

**First point for review.** Passing from the primitive character to its lift must preserve the disjunction at the pole before the change-of-level identity can be invoked.

## Status of literature-named inputs

- `UpperTheory.Top.imprimitive` — in-repo constant (`Development/AutomorphicArithmetic/CharacterBoxes/Imprimitive.lean:5–35`); not compared.
- `UpperTheory.Top.zero_free_all_of_green_v_win` — in-repo constant (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TopPlug.lean:12–15`); not compared.
