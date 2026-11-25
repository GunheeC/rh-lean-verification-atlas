# D415 · Injectivity of the adjoint theta scalar formula

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 17,210 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**Outlined · pending_review.** For a specified real datum and admissible system of scalar forms, the theta map and its adjoint satisfy a scalar formula on the parts of the row. Positivity on the nonzero parts makes the adjoint injective. This supplies the injectivity input for the construction of automorphic rows.

## Statement and hypotheses

For the given real datum and face, assume the comparison hypotheses, unit conductor ideal, agreement of the indicated place sets and the fixed-point condition at conjugation-invariant good places. Every admitted scalar form then satisfies the bilinear formula, and each theta operator has injective adjoint.

$$
\forall S_F,\ \mathrm{IsSF}(R,S_F)\ \Longrightarrow\ \mathrm{BForm}(R,S_F)\wedge\mathrm{UpInj}(R).
$$

[`thetaLift_adjoint_scalarFormula_injective` · `ThetaLiftAdjointScalarFormulaInjectiveStatement.lean:26-27`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ThetaLiftAdjointScalarFormulaInjectiveStatement.lean#L26-L27)

**Read alongside** [T06 · Lattice masses, automorphic membership and existence of linked bundles](../../units/T06.md) · [T09 · Separation on the evaluation grid](../../units/T09.md).

## Inputs to the scalar calculation

Use the discrete-series cover, Harish–Chandra finiteness and modules, Casselman–Wallach and rapid decay, unramified Howe, the Weil–Siegel input, the Hecke-form condition at every datum, continuation and unramified doubling. The real datum and face carry the specified comparison hypotheses. Include the unit-conductor ideal, the equality of the two place sets and the fixed-point property at self-conjugate good places. The equality of place sets is an argument of the published interface even though this proof does not use its binder. The other fields furnish positive chain-step scalars, preservation of the spherical parts off the tuple, and the Schur condition. [`upInj` · `ThetaLiftAdjointScalarFormulaInjective.lean:32-38`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ThetaLiftAdjointScalarFormulaInjective.lean#L32-L38)

## One scalar for each part

For the chosen admissible scalar form the adjoint calculation uses the core datum, the Schur condition, positive scalars and the assertion about spherical parts. This yields a positive common factor and the scalar formula. On a nonzero row part, choose a single model furnishing both the internal step values and the top value. Select the relevant positive real number at every index and check that it has the required local-value property there. Choosing each number from an unrelated model would leave the hypotheses of the scalar formula to be checked again. [`upInj` · `ThetaLiftAdjointScalarFormulaInjective.lean:34-38`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ThetaLiftAdjointScalarFormulaInjective.lean#L34-L38) · [`exists_lvals` · `UpInjOfBForm.lean:29-46`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/UpInjOfBForm.lean#L29-L46)

## Separate the zero and nonzero cases

On a zero row part, any vector in the corresponding test eigenspace maps into zero; the model comparison shows that the vector vanishes, so taking scalar one satisfies the identity. On a nonzero part take the positive common factor times the product of the selected positive step values. The product is positive and the scalar formula identifies the theta map composed with its adjoint on that part with multiplication by this real scalar, viewed in the complex field. [`upInj_of_bForm` · `UpInjOfBForm.lean:54-69`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/UpInjOfBForm.lean#L54-L69)

## Pass from parts to the whole space

For each part the scalar is nonzero. Choose these scalars for the fixed theta map, and use the operator-row result that identifies the span of the parts. The criterion for injectivity of the adjoint now applies to the family of subspaces and their scalar identities. Applying the composite to a kernel vector on this spanning calculation forces the vector to vanish. The linear algebra at this last step is short; the positivity and spanning requirements give a specialist a much sharper place to test the argument. [`upInj_of_bForm` · `UpInjOfBForm.lean:70-76`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/UpInjOfBForm.lean#L70-L76)

**Scope of the hypotheses.** The note retains the source’s named predicates and records. For the exact quantified assumptions at this head, read `GlobalTheory.T.thetaLift_adjoint_scalarFormula_injective` (`Development/AbelianVarietyTheory/Proofs/DecoratedLatticeProofs/ThetaLiftAdjointScalarFormulaInjectiveStatement.lean:26–27`). Their internal definitions are separate reading tasks.

## Literature-named inputs

`GlobalTheory.Published.DiscreteSeriesCover` — hypothesis at this head (`Development/AbelianVarietyTheory/PublishedTheorems/TwistedTraceFormula/AdmissibleDiscreteSeriesOfHasParam.lean:35–38`); not compared.

`GlobalTheory.Published.HarishChandraFinite` — hypothesis at this head (`Development/AbelianVarietyTheory/PublishedTheorems/AutomorphicForms₂/HarishChandraFinite.lean:50–58`); not compared.

`GlobalTheory.Published.HarishChandraModules` — hypothesis at this head (`Development/AbelianVarietyTheory/PublishedTheorems/TwistedTraceFormula/HarishChandraModulesOn.lean:43–44`); not compared.

`GlobalTheory.Published.CasselmanWallach` — hypothesis at this head (`Development/AbelianVarietyTheory/PublishedTheorems/AutomorphicForms₂/HasDRepIffHasDerivAt.lean:98–111`); not compared.

`GlobalTheory.Published.CuspRapidDecay` — hypothesis at this head (`Development/AbelianVarietyTheory/PublishedTheorems/AutomorphicForms₂/ExistsNormLeHeightPow.lean:28–32`); not compared.

`GlobalTheory.Hk3.HoweUnram` — hypothesis at this head (`Development/AbelianVarietyTheory/PublishedTheorems/GaloisGeometry₂/HoweUnram.lean:8–19`); not compared.

`GlobalTheory.Published.WeilSiegelFormulaUnitary` — hypothesis at this head (`Development/AbelianVarietyTheory/PublishedTheorems/TwistedTraceFormula/WeilSiegelFormulaUnitary.lean:56–69`); not compared.

`GlobalTheory.Published.SiegelEisensteinContinuation` — hypothesis at this head (`Development/AbelianVarietyTheory/PublishedTheorems/SiegelWeil₂/SiegelEisensteinContinuationOfDoublingMethod.lean:14–19`); not compared.

`GlobalTheory.Published.UnramifiedDoublingGL` — hypothesis at this head (`Development/AbelianVarietyTheory/PublishedTheorems/TwistedTraceFormula/PairwiseDisjointCell.lean:314–324`); not compared.

**First step to challenge.** Check positivity of each step scalar on a common model of a nonzero row part and the assertion that the resulting parts span the tested space.

[Unit record and exact statement](../../units/D415.md)
