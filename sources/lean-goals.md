# What Main.lean exports

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

These are the five declaration signatures in the pinned submission. The linked definitions give the Lean quantifiers and exceptional points. [Main.lean, lines 4–12](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Main.lean#L4-L12) · [Statements.lean, lines 3–16](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Statements.lean#L3-L16)

## P001

```lean
theorem riemannHypothesis : RiemannHypothesis
```

The first target is the Mathlib predicate. The source identifies it definitionally with the explicit zeta formulation in P002. Both exclude negative even integers and the conventional value at the pole. [Challenge and definition](https://math.mit.edu/~drew/grh/)

[Unit P001](../units/P001.md) · [Source signature](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Main.lean#L4-L4)

## P002

```lean
theorem riemannZeta_eq_zero_re : RiemannZetaZerosOnLine
```

```lean
def RiemannZetaZerosOnLine : Prop :=
  ∀ s : ℂ, riemannZeta s = 0 → (¬∃ n : ℕ, s = -2 * ((n : ℂ) + 1)) → s ≠ 1 → s.re = 1 / 2
```

[Unit P002](../units/P002.md) · [Source signature](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Main.lean#L6-L6)

## P003

```lean
theorem LFunction_ne_zero_of_half_lt_re : DirichletLNonvanishingRightOfHalf
```

```lean
def DirichletLNonvanishingRightOfHalf : Prop :=
  ∀ (N : ℕ) [NeZero N] (χ : DirichletCharacter ℂ N) (s : ℂ),
    1 / 2 < s.re → (χ ≠ 1 ∨ s ≠ 1) → DirichletCharacter.LFunction χ s ≠ 0
```

[Unit P003](../units/P003.md) · [Source signature](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Main.lean#L8-L8)

## P004

```lean
theorem LFunction_eq_zero_re : DirichletLZerosOnLine
```

```lean
def DirichletLZerosOnLine : Prop :=
  ∀ (N : ℕ) [NeZero N] (χ : DirichletCharacter ℂ N) (s : ℂ),
    0 < s.re → s.re < 1 → DirichletCharacter.LFunction χ s = 0 → s.re = 1 / 2
```

[Unit P004](../units/P004.md) · [Source signature](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Main.lean#L10-L10)

## P005

```lean
theorem LFunction_eq_zero_re_of_isPrimitive : PrimitiveDirichletLZerosOnLine
```

```lean
def PrimitiveDirichletLZerosOnLine : Prop :=
  ∀ (N : ℕ) [NeZero N] (χ : DirichletCharacter ℂ N), χ.IsPrimitive →
    ∀ s : ℂ, 0 < s.re → s.re < 1 → DirichletCharacter.LFunction χ s = 0 → s.re = 1 / 2
```

[Unit P005](../units/P005.md) · [Source signature](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Main.lean#L12-L12)

For each of these five conclusions the reported axiom set is `propext`, `Classical.choice`, `Quot.sound`. [Pinned checker record](kernel-audit.md)
