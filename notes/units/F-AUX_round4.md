# F-AUX · Three inputs to the definite-side evaluation grid and row test

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 6,499 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it The three anchors in this grouped unit carry separate index weights: `howeUnram_holds` 6,499, `twisted_local_factors_match` 2, `rowRatW_of_rowTest` 4.

**Outlined · pending_review.** Three short calls in the F supplier have different mathematical jobs. One gives the unramified assertion used for separation, one matches local factors in the square model used on the grid, and one converts a test at each datum into the stated row condition. The three results have separate hypotheses. Their exact positions are the separation, rationality and grid lines of `UpperTheory.Lit.nonempty_hyps_definite_side_of_closed_bound`, `SiegelEisensteinSecondTermHypotheses.lean:47–54`. [F](../../pillars/F.md) · [T02](../../units/T02.md)

## The unramified fixed-space assertion

The first call supplies `GlobalTheory.Hk3.HoweUnram`. Work with the valued field, involution, uniformizer, Hermitian matrices, additive character, actions on the complex module and hypotheses on the local dual pair in the theorem. The test vector $s$ is nonzero and satisfies the stipulated invariance and generating-span hypotheses. The construction must give the fixed-vector span conclusion for both sides of the pair. This input is used together with the theta-local record and the convergent Siegel–Weil field in [T09](../../units/T09.md). `GlobalTheory.Hk3.howeUnram_holds`, `RhoMemOfMkEq.lean:250–256`; `UpperTheory.Lit.functionalsSeparate_of_howeUnram_of_siegelWeil`, `FunctionalsSeparateOfHoweUnramOfSiegelWeil.lean:17–19`.

1. The one-sided calculation constructs an invariant span from translates of $s$. It tests its generators against the integral subgroup, commutes the two group actions and uses the prescribed fixed vector. For a nonzero invariant vector in an orbit component, the next step compares it with a vector of the generated span, modulo terms of smaller height. The two inclusions at a representative identify the orbit subspace with the span of the corresponding translates, so the passing to a quotient representative retains the same vector space. The orbit-height separation argument then proves membership. `GlobalTheory.Hk3.HoweDuality.fixed_mem_span`, `RhoMemOfMkEq.lean:198–240`.
2. One component of the final pair is this lemma applied directly. For the other, take the Hermitian-adjoint swap of the two factors, including the transformed invariance and spanning hypotheses on $s$, then apply the same lemma. This explicit swap is what makes the two one-sided conclusions comparable. `GlobalTheory.Hk3.howeUnram_holds`, `RhoMemOfMkEq.lean:250–256`.

## Moving to the square model

Here the assumptions are real Howe duality, the complete theta-local record, theta-integral agreement and local matching **in the original tensor model**. The desired target is local matching in the square model. These interfaces use different data. [D044](../../units/D044.md) supplies the companion assertion for agreement of integrals. `GlobalTheory.T.twisted_local_factors_match`, `TwistedSquareLocalMatching.lean:88–89`; `GlobalTheory.SquareLM.twisted_square_local_matching`, `TwistedSquareLocalMatching.lean:18–29`.

3. For the chosen characters, spaces, frames and indices, take the common quotient and its two maps supplied by the real quotient theorem. Its invariant subspaces are trivial, and the scalar commutant assertion applies to its action. For each side form the subspace of finite Fock functions. Evaluation after the given map is bilinear in the finite function and the polynomial. Surjectivity on the algebraic Fock span identifies the resulting images as a spanning set in the target. `GlobalTheory.SquareLM.twisted_square_local_matching`, `TwistedSquareLocalMatching.lean:20–56`.
4. The product-form theorem on these two subspaces returns a common factor, two functionals and their compatibility equations. Extend the functionals linearly to their ambient spaces. When evaluated on finite functions the extensions agree with the originals, so the spanning witnesses and matching identities required in the conclusion survive. It is the earlier common quotient and the prescribed test subspaces that supply the content behind this extension. `GlobalTheory.SquareLM.twisted_square_local_matching`, `TwistedSquareLocalMatching.lean:57–81`.

## From a test at a datum to row rationality

5. The input to this last implication is, at every datum, the test `Formalism.IndefR.Rat.RowTest (z.R.toCx3 z.F)`. The outer supplier obtains it through test-vector assembly with the same matching and separation data. The conversion composes a first step from `Start` to `Pinned`, the given test, and a last universally quantified specialization to the required parameters. No new test vector is chosen by the conversion. `GlobalTheory.T.test_vector_assembly_holds`, `TestVectorAtDatumOfJoin.lean:39–40`; `GlobalTheory.Mem.LiteralAutomorphy.rowRatW_of_rowTest`, `RowRatWOfRowTest.lean:9–12`; `UpperTheory.Lit.nonempty_hyps_definite_side_of_closed_bound`, `SiegelEisensteinSecondTermHypotheses.lean:49–50`.

**Scope of the hypotheses.** The note retains the source’s named predicates and records. For the exact quantified assumptions at this head, read `GlobalTheory.Hk3.howeUnram_holds` (`Development/AbelianVarietyTheory/Proofs/SatakeParameters/RhoMemOfMkEq.lean:250–256`). Their internal definitions are separate reading tasks.

## Literature-named inputs

`GlobalTheory.Hk3.howeUnram_holds` — in-repo constant (`Development/AbelianVarietyTheory/Proofs/SatakeParameters/RhoMemOfMkEq.lean:250–256`); not compared.

`GlobalTheory.Published.HoweDualityReal` — hypothesis at this head (`Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/HoweDualityReal.lean:21–31`); not compared.

`UpperTheory.Lit.functionalsSeparate_of_howeUnram_of_siegelWeil` — in-repo constant (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/LocalTypeDictionary/FunctionalsSeparateOfHoweUnramOfSiegelWeil.lean:17–19`); not compared.

**First step to challenge.** Inspect the real quotient and the passage to the two finite Fock spans. The later scalar-factor argument needs the same quotient and both projected spanning conditions. A quotient of the right dimension on each side separately would not establish that assertion. The fixed-space and row-test conclusions cannot supply a missing quotient. `GlobalTheory.SquareLM.twisted_square_local_matching`, `TwistedSquareLocalMatching.lean:20–30,47–72`.
