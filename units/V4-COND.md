# V4-COND · Conditional passage from Selmer and definite-side data to the five public goals

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

The v4 conditional theorem takes a uniform Selmer window, one compatible definite-side witness, Green’s character assertion and the local implications in three explicit lists as premises. Under those assumptions it derives the five public zeta and Dirichlet conclusions. The note lets a reader trace the deduction while keeping each unproved input visible.

`conditional-passage-to-the-five-goals` · [Analytic number theory](../tracks/analytic/README.md) · [Galois representations, automorphy lifting, Iwasawa theory and Euler systems](../tracks/galois/README.md) · [Theta correspondence and automorphic representations of unitary groups](../tracks/theta/README.md) · [Arakelov geometry and geometry of numbers](../tracks/arakelov/README.md) · [Formalization and reproducibility](../tracks/formal/README.md)

**Outlined** · **L0** Pinned Lean components of the paper argument · Record generated 2026-11-25 (no human check).

| 1 · Lean pinned | 2 · Statement compared | 3 · Prose | 4 · Steps | 5 · AI review | 6 · Human |
|---|---|---|---|---|---|
| ✓ | – | Outlined | 7 | – | 0 of 7 steps |

[Numbered proof and check records](V4-COND.check.md) · [Progress and counting rules](../PROGRESS.md)

## Statement

Assume the Selmer window $V$, a compatible definite-side witness $F$, the finite-field Green assertion $B$, and the universally quantified local implications in lists A, B and C of v4 Table 1. Then the conclusions of P001–P005 follow. The quantified premises, the five individual conclusions and the proof are given in the accompanying note.

## Assumptions

- For every primitive character assume VWinAt at cutoff exponent 401 and the square-root exponential budget, on the selected square windows.
- Assume one witness of HypsAlt for DefiniteSideCondition and the class predicate Closed(LinkN), with one common family class and compatible choices.
- Assume the Green parametrization with its regular-elliptic character formula and degree for every prime, label datum and positive degree.
- Grant the ten local prime-sum implications A1–A10, the eight host implications B1–B8 and the thirteen closed family/design implications C1–C13 at their respective pinned types.
- The written outline also calls the Landau level criterion (P018), the per-lattice estimate (P021), division and slope lemmas, the eventual rank bound and the classical Dirichlet nonvanishing, change-of-level and functional-equation results. See the named sources in the conditional note.

Sources for the assumptions · [From the Selmer window to Dirichlet zero-free statements, v4](../data/editions.json)

**New exposition · pending_review.** This edition has no independent review of the new argument. Earlier verdicts below retain their stated scopes.

## Where to read

Gunhee Cho is the paper’s author and the blueprint’s editor. Both were drafted with AI assistance. No independent human referee has checked the arguments. Levent Alpöge is the author of the Lean development. [Blueprint v13b](../editions/v0.1.0/blueprint_v13b.pdf) · [Conditional paper v7](../editions/v0.1.0/paper_v7.pdf) · [Edition register](../data/editions.json)

- Paper v7 · [Theorem 1.1 · conditional statement](../editions/v0.1.0/paper_v7.pdf#page=2), printed p. 2
- Paper v7 · [Table 3 · global, local and supplementary inputs](../editions/v0.1.0/paper_v7.pdf#page=51), printed pp. 51–52
- Paper v7 · [Theorem 5.43 · conditional deduction](../editions/v0.1.0/paper_v7.pdf#page=52), printed pp. 52–53
- [From the Selmer window to Dirichlet zero-free statements, v5](../data/editions.json), Theorem 1.1 · conditional statement, p. 6. Revised paper v5 exposition, pending independent review.
- [From the Selmer window to Dirichlet zero-free statements, v5](../data/editions.json), Table 1 · global, local and supplementary inputs, pp. 38–41. Revised paper v5 exposition, pending independent review.
- [From the Selmer window to Dirichlet zero-free statements, v5](../data/editions.json), Theorem 3.43 · conditional deduction, pp. 41–42. Revised paper v5 exposition, pending independent review.
- [From a common Selmer window and a definite-side witness to five zero statements](../notes/units/V4-COND_round3.md), pp. 1–7 in the atlas print layout. Round-3 written exposition, pending independent review.
- [From the Selmer window to Dirichlet zero-free statements, v4](../data/editions.json), Theorem 1.1 (r24:intro), p. 6
- [From the Selmer window to Dirichlet zero-free statements, v4](../data/editions.json), Table 1 and Theorem 3.43 (r24:conclusion), pp. 37–40

## Evidence

L0 refers only to the linked declarations in the pinned development. The finite-premise presentation and its proof are paper theorems pending independent review. No single Lean declaration asserts this assembled paper theorem.

Review records · [DB3 review A](../reviews/DB3_review_A.md)

## Lean declarations

These are components of the paper implication. Its full hypothesis table has its own manuscript locator.

- `UpperTheory.Top.zero_free_all_of_green_v_win`  
  [`TopPlug.lean`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/TopPlug.lean#L12-L15), lines 12–15 · 194,351 dominated lines · SHA-256 `5e975b246227`.
- `UpperTheory.Comparison₂.level_gm_le_on_family_scales`  
  [`LevelGmLeOnFamilyScales.lean`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/PrimitiveCosets/LevelGmLeOnFamilyScales.lean#L28-L30), lines 28–30 · 3,365 dominated lines · SHA-256 `3ccafb3b79c9`.
- `UpperTheory.Comparison₂.formB`  
  [`Imports.lean`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/PrimitiveCosets/Imports.lean#L8-L19), lines 8–19 · 2,057 dominated lines · SHA-256 `7e428d22efce`.
- `riemannHypothesis`  
  [`Main.lean`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Main.lean#L4-L4), lines 4 · 1 dominated lines · SHA-256 `71b3d50605dd`.
- `riemannZeta_eq_zero_re`  
  [`Main.lean`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Main.lean#L6-L6), lines 6 · 3 dominated lines · SHA-256 `b76ddf651dfd`.
- `LFunction_ne_zero_of_half_lt_re`  
  [`Main.lean`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Main.lean#L8-L8), lines 8 · 4 dominated lines · SHA-256 `5b0ee8859337`.
- `LFunction_eq_zero_re`  
  [`Main.lean`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Main.lean#L10-L10), lines 10 · 101 dominated lines · SHA-256 `16e8622c29d6`.
- `LFunction_eq_zero_re_of_isPrimitive`  
  [`Main.lean`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Main.lean#L12-L12), lines 12 · 28 dominated lines · SHA-256 `0401b524ca29`.

[Machine record and full declaration hashes](V4-COND.yaml) · [Declaration lookup](../lookup/declarations.md)

## Reading prerequisites

Background · Finite Fourier analysis and smoothed character sums · Selmer groups and logarithmic length bounds · Functional equations for Dirichlet L-functions.

- [P013 · The Selmer window from the polarised row](P013.md) · statement-reading
- [T02 · A common definite-side witness](T02.md) · statement-reading
- [D575 · Green's parameterization of finite cuspidal characters](D575.md) · statement-reading
- [B07 · Character hosts on power windows](B07.md) · statement-reading
- [B05 · Connected families from Green and the closed link](B05.md) · statement-reading
- [D479 · Global lattice compatibility of a family](D479.md) · statement-reading
- [P017 · Chebyshev control on a chain-tied family](P017.md) · statement-reading
- [P018 · The level window criterion](P018.md) · statement-reading
- [P022 · Landau’s criterion on logarithmic windows](P022.md) · statement-reading
- [P023 · Power windows for a positive character family](P023.md) · statement-reading

## Open questions

- At the passage from the common definite-side witness and the host request to a tied family, can a referee track the very same selection through every closed implication, especially the independent slope comparison required by D479?

## Graph connections

Arrows may connect either a unit’s main declaration or an indexed member.

**Uses** · No recorded edge.

**Used by** · No recorded edge.

[Declaration witnesses and graph scope](../data/unit_graph.json)

Lookup aliases · `Theorem 1.1 (v4)`, `Theorem 3.43 (v4)`, `V + F + Green and lists A–C`

<!-- Unit metadata SHA-256 df5db871495344e7577deac719bacaa134917f795da946395182fc16867e9f8f -->
