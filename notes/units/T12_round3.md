# T12 · The two rank ranges in the doubled Siegel–Weil value

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**Outlined · pending_review.** The [unit statement](../../units/T12.md) is manuscript v3, §5.22, p. 43. The equality supplies the special-value input in the [global integral comparison](../../units/T11.md). This outline tracks how the constant-term and Fourier-coefficient calculations reach that equality for the original Haar measure and section.

## Section, continuation and normalization

Let $A,Y$ have positive ranks $m,n$ and opposite Hermitian signs over the good base, with $\min(r,s)=0$ for $A$. Take the character with the stipulated restriction $\eta^m$. The Darboux presentation must carry the rational-lattice law, compatible Weil splittings, invariance of the coefficient functional $l$ under the indicated translations and $A$-action, and the theta summation law. These hypotheses allow one to start with the section defined by $\Phi\mapsto l(\omega(x)\Phi)$ and compare its Fourier data to an actual theta sum in the same model. The test vector is Schwartz and its compact translates span a finite-dimensional complex space. See **IsDbl** in `LatticeBasics/Hypotheses2.lean:62-74` and **SiegelWeilStd** in `HypothesesS.lean:11-21`.

Put $s_0=(m-n)/2$ using subtraction in $\mathbb C$. At each fixed $x$ the conclusion requires a meromorphic function on the whole complex plane. On a sufficiently far right half-plane the Eisenstein terms must sum to this function. It must be analytic at $s_0$, where its value is the required multiple of the average on the prescribed fundamental domain. Thus calculating a matching formal Fourier coefficient at $s_0$ alone does not settle the assertion. The four requirements on the same function are the fields of **EisValueAt**, `LatticeBasics/Hypotheses2.lean:76-78`.

## What the constant-term splitting contributes

Start in the half-plane of absolute convergence. For the section and data in the splitting theorem there are three real bounds: one for convergence, one for the first-orbit identity and one for the transformation law of the second term. Their maximum puts all three statements at the same complex parameter. Choose compact representatives of the integration domains for the coefficient and the unipotent variables. Independence of the domains transports the integral on these representatives back to the original choices. Absolute summability now allows the sum over cosets to be partitioned into those satisfying the Lagrangian condition and their complement. The first sum is the designated first term, and the other contributes the section with its prescribed dilation law. This is **ctSplit_of_parts**, `CtSplitOfParts.lean:137-158`. In **ctSplit_of** the two formal arguments are discarded; independence, compact domains, absolute convergence and the two orbit laws supply the split. See `CtSplitOf.lean:10-11`.

Apply Poisson summation to the Weyl operation, supplementing it by the bijectivity, theta and uniqueness properties of the chosen model. The result joins the parabolic action to give the full operator identities. The proof then obtains a polynomial description of compact-finite vectors and the required lower-rank Lagrangian data. The reverse inclusion from polynomial vectors to compact-finite vectors and the local dilation identities are also used. These transitions let the coefficient calculation on explicit test vectors reach the stated class of $\Phi$. See **tWeyl_of**, **siegelWeilStd_pre** and **siegelWeilStd_mid** in `SiegelWeilStdPre.lean:16-23` and `SiegelWeilStdMid.lean:14-20`.

## Why the multiplier changes

The finite local, unramified and real coefficient formulas feed distinct Whittaker comparisons in the strict, equal and lower-rank cases. The proof combines them with the theta coefficient identity and unfolding. It also forms a rank-change step using the holomorphic leading term, singular Fourier coefficients, the vacuum and the constant-term split above. See **whitGenLt**, **whitGenEq**, **whitGenLow** and **siegelWeilStd_of** in `SiegelWeilStdOf.lean:37-50` and `SiegelWeilStdOf.lean:52-67`. The equal-rank comparison has multiplier two. Together with the rank step and the generation result for vacuum vectors it gives the comparison for all $m\le n$. The strict branch $n<m$ has its own comparison. The actual combination of these inputs is **Atop.siegelWeilStd_of**, `SiegelWeilStdLeaves.lean:40-58`.

Return to the original section at $x$. **Atop.fieldOf** tests $n<m$. In that case the strict branch directly returns the special value with multiplier one. Otherwise it packages the original spaces, splitting, frame, compact, height, Haar measure and domain into one datum and applies the $m\le n$ comparison with multiplier two. Equality of the ranks therefore belongs to the second case. The result is

$$
E_\Phi(x,s_0)=
\begin{cases}
1,&n<m,\\
2,&m\le n
\end{cases}
\ \operatorname{avg}_{g\in D}\theta_F\bigl(\omega(x)S(g)\Phi\bigr).
$$

The normalized average uses the measure fixed at the start. See `FockVacuumBounds/FieldOf.lean:50-63` and the actual specialization by Poisson summation and the constant-term split in **siegelWeilStd_of_ct** and **siegelWeilStd**, `SiegelWeilStdOfCt.lean:8` and `SiegelWeilStd.lean:8`.

The continuation with growth bounds is **PositivityTheory.RgEis.Hd.eisBL**, read in **Atop.siegelWeilStd_of** (`SiegelWeilStdLeaves.lean:40-54` and type **EisBL**, `Hypotheses2.lean:55-60`). The intermediate step supplies **HSt.holLeadB** for the holomorphic leading term (`SiegelWeilStdMid.lean:16-20`). **tAll_of** and **thetaCoef** use **GlobalTheory.T.siegel_set_unitary**. In the strict and equal branches the local density suppliers are **PositivityTheory.PfSWUS.HMass.siegelDensitiesLowA** and **PositivityTheory.Rg.Base1.densEq** (`SiegelWeilStdOf.lean:39-47`). The Whittaker and rank-change calculations use **kunf.unfold**, **Aeis.eisWk**, **Krd.rdEx**, **kfour.lamBd** and **kfour.fourierZero**. The assembly appeals to both **AbsSt.absThm** and **AbsSt.vacuum_generates_polynomials** (`SiegelWeilStdOf.lean:59-67`). These substantial inputs are supplied by Lean constants in this development. The exported **siegelWeilStd** has no additional theorem premise (`SiegelWeilStd.lean:8`). Its anisotropic statement specifies the doubling model, splitting and probability-normalized theta average. This outline establishes no comparison of all these conditions, or of their full rank range, with a published Siegel–Weil theorem.

**Referee check.** Follow the equal-to-lower-rank step from its singular Whittaker term to analyticity at $s_0$. The bounded half-plane splitting permits rearrangement there. The special-value assertion still needs the separate continuation and holomorphic-leading-term inputs.

## Status of literature-named inputs

- `PositivityTheory.SiegelWeilFormula.Fin.siegelWeilStd` — in-repo constant (`Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/SiegelWeilStandard/SiegelWeilStd.lean:8`); variant.
- `PositivityTheory.SiegelWeilFormula.Fin.siegelWeilStd_mid` — in-repo constant (`Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/SiegelWeilStandard/SiegelWeilStdMid.lean:16–20`); not compared.
- `PositivityTheory.SiegelWeilFormula.Fin.siegelWeilStd_of` — in-repo constant (`Development/WeilBound/CoreStatements/AutomorphicKernels/SiegelWeilFormula/SiegelWeilStandard/SiegelWeilStdOf.lean:52–67`); not compared.
