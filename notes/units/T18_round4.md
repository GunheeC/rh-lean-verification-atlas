# T18 · Three arithmetic Hilbert–Samuel consequences

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 9 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**Outlined · pending_review.** Three consequences of arithmetic Hilbert–Samuel theory enter the deep estimate. The first gives the sign of a top intersection. The other two bound small-section growth from above on two specified chart lattices. Their hypotheses and their lattices must be kept separate in applications.

## Claim and hypotheses

For each intersection system and finite multihomogeneous presentation as
above the following three statements hold.
(i) On an arithmetic variety of dimension $D+1$, relative semipositivity,
fibre nefness, conjugation invariance and nonnegative degree on every
arithmetic curve imply $I_P(A^{D+1})\ge0$.
(ii) For a birational characteristic-zero presentation with $D\ge1$,
small-generation data and conjugation invariance, the limsup of the
small-section count for `chartLat`, divided in degree $n$ by
$n^{D+1}/(D+1)!$, is at most $I_P(A^{D+1})$.
(iii) For a birational presentation over a field with $D\ge1$, nonnegative
multidegree, relative semipositivity at $P_0\subseteq P$, bounded monomials
and conjugation invariance, the same limsup bound holds for
`chartLatNm`.

[`PositivityTheory.Pf1.HilbertSamuelMoriwaki.hsUse_outright` · `Outright.lean:13–15`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/AutomorphicKernels/MoriwakiBigness/MoriwakiBigTheorem/Outright.lean#L13-L15)

## Three outputs from a single supply

The head has no hypotheses. It uses three in-repo constants for repo-defined propositions: `PositivityTheory.ResPlug.FromRes.resK`, `PositivityTheory.Tls2.Pl.poincareLelong` and `PositivityTheory.MbAis.DenseCurves.main`. Resolution and Poincaré–Lelong supply the arithmetic intersection system, and the third constant supplies density. `PositivityTheory.Pf1.HilbertSamuelMoriwaki.hsUse_outright` (`Development/WeilBound/CoreStatements/AutomorphicKernels/MoriwakiBigness/MoriwakiBigTheorem/Outright.lean:13–15`). Its first two outputs support the arithmetic bigness bound in T17. The final three are selected together here: arithmetic Kleiman positivity, the small-generated upper estimate called G7, and the upper estimate for the nef normed chart lattice. The outer supplier gets the intersection system from Poincaré–Lelong and resolution, and supplies density separately. A reference to a Hilbert–Samuel statement alone leaves the actual three requested conclusions unspecified. [`PositivityTheory.Pf1.HilbertSamuelMoriwaki.hsUse_of_hypotheses` · `HSChain.lean:376–378`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/AutomorphicKernels/MoriwakiBigness/MoriwakiBigTheorem/HSChain.lean#L376-L378) [`PositivityTheory.Pf1.HilbertSamuelMoriwaki.HSUse` · `HSChain.lean:372–374`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/AutomorphicKernels/MoriwakiBigness/MoriwakiBigTheorem/HSChain.lean#L372-L374) [`PositivityTheory.Pf1.HilbertSamuelMoriwaki.hsUse_outright` · `Outright.lean:13–15`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/AutomorphicKernels/MoriwakiBigness/MoriwakiBigTheorem/Outright.lean#L13-L15)

## Produce the sign of the intersection

For the first component the source assembles a mixed-section step using a small-section inequality and generic-degree information. A separate chain supplies positivity of the Fubini–Study geometric degree and then positivity after scaling. These inputs enter the mixed top-intersection calculation. From the resulting mixed Kleiman assertion the proof extracts the desired nonnegativity for the original top intersection. This branch uses the nonnegative curve-degree hypothesis and the semipositivity/fibre conditions of its own statement. A limsup comparison by itself would not give the required sign in this direction. [`PositivityTheory.Pf1.HilbertSamuelMoriwaki.hsChain` · `HSChain.lean:310–322`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/AutomorphicKernels/MoriwakiBigness/MoriwakiBigTheorem/HSChain.lean#L310-L322)

## Obtain the small-generated chart-lattice estimate

Power-block metric data and the point norms of sections feed the measure comparison in the power construction. The resulting power-block datum enters the tensor-power $L^2$ degree estimate along with the block covolume and Hilbert–Samuel input. Pass via Euclidean sections on powers to the ordinary Euclidean sections: the assembly uses the nonzero small-section result, a sublattice degree calculation and a successive-minima span statement. G7 is then applied to this last Euclidean-sections result. The upper estimate retains both the particular chart lattice and the small-generation hypothesis. [`PositivityTheory.Pf1.HilbertSamuelMoriwaki.hsChain` · `HSChain.lean:345–360`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/AutomorphicKernels/MoriwakiBigness/MoriwakiBigTheorem/HSChain.lean#L345-L360)

## Obtain the normed chart-lattice estimate

The third conclusion has its own normalization. A packing estimate controls the monomial shift. The small-generated result from the previous step enters an upper normalization together with packing and the previously constructed auxiliary bound. Combine that normalization, the shift and a perturbation of monomials to obtain the nef arithmetic volume statement. The three results are then returned in their specified order. Reading this as a purely formal projection is safe only after the two upper comparisons have been assigned to their respective lattices. The tensor-power and perturbation estimates themselves remain named inputs here. [`PositivityTheory.Pf1.HilbertSamuelMoriwaki.hsChain` · `HSChain.lean:359–365`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/AutomorphicKernels/MoriwakiBigness/MoriwakiBigTheorem/HSChain.lean#L359-L365)

## First step to challenge

Check the transition from the small-generated chart count to the normed chart count. The second bound needs the monomial shift and upper normalization for its own lattice.

Compare [T17](../../units/T17.md) for the opposed direction of the volume inequality and [T26](../../units/T26.md) for the simultaneous use of the three consequences.

The intermediate assertions `s1` through `s125` in `hsChain` are not outlined here. They precede the construction of the later inequalities quoted above. `PositivityTheory.Pf1.HilbertSamuelMoriwaki.hsChain` (`Development/WeilBound/CoreStatements/AutomorphicKernels/MoriwakiBigness/MoriwakiBigTheorem/HSChain.lean:185–309`). The third output uses `chartLatNm` with the stated bounded-monomial, conjugation and semipositivity hypotheses. `ReciprocityTheory.ChartRestriction.G.Geo.ArithmeticHilbertSamuelUpperBound` (`ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/BirationalGeometry/ArithmeticHilbertSamuelLowerBound.lean:135–145`).

## Literature-named inputs

`PositivityTheory.ResPlug.FromRes.resK` — in-repo constant (`Development/WeilBound/CoreStatements/ResolutionCharZero/PlugResK.lean:7–8`); not compared.

`PositivityTheory.Tls2.Pl.poincareLelong` — in-repo constant (`Development/WeilBound/CoreStatements/TemperedRepresentationTheory/PoincareLelong/PoincareLelongInv.lean:13–17`); not compared.

`PositivityTheory.MbAis.DenseCurves.main` — in-repo constant (`Development/WeilBound/CoreStatements/AutomorphicKernels/MoriwakiBigness/MoriwakiSymmetry/EqMapSymm.lean:23–119`); not compared.

`GlobalTheory.T.arith_intersection_system_of_poincare_lelong` — in-repo constant (`Development/AutomorphicSpectrum/Proofs/MetricProofs/ArithIntersectionSystemOfPoincareLelongStatement.lean:11–12`); not compared.
