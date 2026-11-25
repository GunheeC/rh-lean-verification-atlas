# D025 · A nonzero Bessel period

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 21,500 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**Outlined · pending_review.** For a fixed discrete-series representation, a finite-dimensional comparison representation and a lowest-weight unit vector, two translates make the specified Bessel integral nonzero. The result supplies a detecting test even though a particular choice of translates could give zero.

## Statement and hypotheses

For admissible discrete-series parameters with even $k\ge2$, interlacing and half-integral difference in the two-unitary-group setup, for every admissible discrete-series representation, comparison representation, lowest-weight unit vector and pair of Haar measures, two group translates give a nonzero matrix-coefficient Bessel integral.

$$
\exists x,x_0\in U(H_{p_k}),\quad \int \langle\sigma(x_0)w,\sigma(uv)\sigma(x)w\rangle\,\overline{\psi_{\rm gen}(v)}\,\pi(u^{-1})\,d(\mu_W\otimes\mu_N)(u,v)\ne0.
$$

[`besselNVG` · `Closed.lean:10-10`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/ReciprocityTheory/ReductiveGroups/DiscreteSeries/LaplaceOperators/BesselVectors/Closed.lean#L10-L10)

**Read alongside** [N076 · Bessel period in the wave grid](../../units/N076.md) · [T09 · Separation on the evaluation grid](../../units/T09.md).

## Fix the test vector before moving it

Choose an even integer $k\ge2$ and an arbitrary $r$. Keep the admissible $z$, nonzero entries of $c$, the Harish–Chandra conditions on both weights, interlacing, half-integral difference and the large-gap condition. The assertion quantifies over the two representations, then over the lowest unit vector and the two Haar measures. Only now may one choose the two group elements. The output is an operator on the finite-dimensional representation. A nonzero matrix coefficient of the original representation at a single point would give no conclusion about this integral. [`BesselNVG` · `BesselNV.lean:39-57`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/ReciprocityTheory/ReductiveGroups/DiscreteSeries/LaplaceOperators/BesselVectors/BesselNV.lean#L39-L57)

## Obtain the model test

The first input is the integration statement obtained from a finite-integral assertion under the multiplicity-one hypotheses. The nonvanishing construction combines it with the base step, the induction step and a decay/derivative input. When passed an admissible target, the specialization retains the rank, parameter, interlacing, half-integrality and gap information required by that construction. The conversion to the group version separately supplies the signature-zero coefficient statement. These are substantive inputs even though the last theorem on the unit card consists of a single application. [`intS` · `NVHTop.lean:25-26`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/ReciprocityTheory/ReductiveGroups/DiscreteSeries/LaplaceOperators/SpectralGap/NVHTop.lean#L25-L26) · [`nv` · `Imports.lean:10-11`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/ReciprocityTheory/ReductiveGroups/DiscreteSeries/LaplaceOperators/Imports.lean#L10-L11) · [`bAtTarget_of` · `BesselNVGOfNv.lean:10-16`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/ReciprocityTheory/ReductiveGroups/DiscreteSeries/LaplaceOperators/BesselVectors/BesselNVGOfNv.lean#L10-L16)

## Move the coefficient and test the operator

Transport the discrete-series coefficient through the change of Hermitian model. The transported lowest vector has the same coefficient on the unitary group. The model's expression for it supplies a nonzero scalar, while the Bessel test supplies a vector and two translates. In the shifted integral the scalar multiplies a nonzero vector; this gives the nonzero evaluation that will detect the operator. The Haar hypotheses ensure that almost every integration point lies in each required subgroup. Their product therefore lies in the unitary group where the coefficient identity holds. Rewrite the integrand there, evaluate the operator integral on the detecting vector, and deduce nonvanishing. This last implication is linear algebra; construction of the model test and the coefficient identity carry the burden. [`besselNVG_of` · `BesselNV.lean:118-147`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/ReciprocityTheory/ReductiveGroups/DiscreteSeries/LaplaceOperators/BesselVectors/BesselNV.lean#L118-L147) · [`besselNVG_of` · `BesselNV.lean:148-171`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/ReciprocityTheory/ReductiveGroups/DiscreteSeries/LaplaceOperators/BesselVectors/BesselNV.lean#L148-L171)

**First step to challenge.** Check the comparison of the given lowest-weight coefficient with the model coefficient on the entire unitary group, including the nonzero scalar used to transfer nonvanishing.

[Unit record and exact statement](../../units/D025.md)
