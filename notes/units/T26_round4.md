# T26 · The arithmetic inputs behind the deep estimate

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 481,067 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**Outlined · pending_review.** The deep component estimate needs one constant chosen before the core, cover and weight vary. This reduction obtains it from a tower and a volume theorem and translates the hypotheses on each deep datum into the numerical restrictions required by the volume estimate.

## Claim and hypotheses

Assume an arithmetic intersection system, the three Hilbert--Samuel
consequences T18, the bigness bound T17, the resolution statement
`ResKStatement`, extension of homomorphisms of semiabelian
schemes, the Fargues Hodge--Tate input, GAGA for sections, quotients by
finite flat subgroups, the Zarhin splitting T22 and nef Riemann--Roch T23.
Then the uniform component-slope estimate in T14 holds with the same
restrictions on $D,T,j,Y,e,o$ and the number of prime factors.

[`GlobalTheory.CompanionTheory.Ar.Plug.deepStR_of_use` · `DeepStROfUse.lean:12–23`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/AutomorphicKernels/MoriwakiBigness/HilbertSamuelApplications/DeepStROfUse.lean#L12-L23)

## Build the large-degree line

The first four inputs are the intersection system, the three Hilbert–Samuel consequences, arithmetic bigness and resolution. The proof extracts a successive-minima upper bound from the Hilbert–Samuel and bigness pair. Intersection existence and generic degree come from the system; resolution supplies point integrability. The remaining construction includes a change of chart coordinates, a dual lattice index, metric energy and a change of model. These are used together to produce a line of large degree. This step is a substantial geometric input to the rest of the argument. [`GlobalTheory.CompanionTheory.Ar.Giv.lineOfLargeDegree_of_use` · `LineOfLargeDegreeOfUse.lean:10–29`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/AutomorphicKernels/MoriwakiBigness/HilbertSamuelApplications/LineOfLargeDegreeOfUse.lean#L10-L29) [`GlobalTheory.CompanionTheory.Ar.Giv.lineOfLargeDegree_of_use` · `LineOfLargeDegreeOfUse.lean:72–88`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/AutomorphicKernels/MoriwakiBigness/HilbertSamuelApplications/LineOfLargeDegreeOfUse.lean#L72-L88)

## Supply one compatible tower and volume comparison

Extension of semiabelian homomorphisms, the Fargues Hodge–Tate input and GAGA for sections join the large-degree line to give the record called `Given`. The same data, supplemented by finite flat quotients and the Zarhin splitting, give a pair consisting of good-tower existence and the volume theorem. The tower construction extracts its model, geometric and analytic components from the same record. The last line invokes the final comparison, adding the point integrability obtained from resolution. The step pairs two propositions; later code must still specialize them to the relevant datum. [`GlobalTheory.CompanionTheory.Ar.Plug.deepStR_of_use` · `DeepStROfUse.lean:12–23`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/AutomorphicKernels/MoriwakiBigness/HilbertSamuelApplications/DeepStROfUse.lean#L12-L23) [`GlobalTheory.CompanionTheory.Ar.Link.good_tower_volume_theorem_bis` · `GoodTowerVolumeTheoremBis.lean:9–19`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/AutomorphicKernels/MoriwakiBigness/HilbertSamuelApplications/GoodTowerVolumeTheoremBis.lean#L9-L19)

## Choose the uniform constant first

The Hilbert–Samuel component of `Given` supplies the birational pullback/pushforward identity. Use that identity, nef Riemann–Roch, the intersection system and the tower/volume pair in the abelian CM component estimate. Its output gives $C\ge 0$ before any choice of core, index, deep datum or good pair of parameters. Only then does the proof introduce the particular data and recover the compatible parameters of the good datum. In particular the resolution and the arithmetic inputs alone are not presented here as a direct numerical bound. [`GlobalTheory.CompanionTheory.Ar.Plug.deepStR_of_use` · `DeepStROfUse.lean:16–23`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/AutomorphicKernels/MoriwakiBigness/HilbertSamuelApplications/DeepStROfUse.lean#L16-L23) [`GlobalTheory.CompanionTheory.Ar.Plug.deepStR_of_volume` · `DeepStROfVolume.lean:21–38`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicSpectrum/Proofs/GeometryProofs/DeepStROfVolume.lean#L21-L38)

## Check the finite exceptional set

The volume estimate bounds the cardinality of the union of primes dividing twice the absolute discriminant with those dividing the level integer. The target supplies a restriction on the latter set. Split the union at the host threshold $n$. The small-prime part embeds in the first $n+1$ natural numbers. For the other part the host bad-prime estimate applies. The CM-type cardinality and the lower bound for the square of the signature sum absorb these estimates in the required bound. Apply the constant to this datum, using its geometric and level conditions, then substitute its root-discriminant and scale identities. The finite-set arithmetic is visible here. The uniform arithmetic volume theorem remains an input. [`GlobalTheory.CompanionTheory.Ar.Plug.deepStR_of_volume` · `DeepStROfVolume.lean:39–58`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicSpectrum/Proofs/GeometryProofs/DeepStROfVolume.lean#L39-L58)

## First step to challenge

Check that the constant in the abelian CM component estimate is chosen before the datum and its bad primes. Verify the union-of-primes bound for the same level as the selected tower.

The target with its quantifiers is in [T14](../../units/T14.md). The detachable geometric inputs include [T17](../../units/T17.md), [T18](../../units/T18.md), [T22](../../units/T22.md) and [T23](../../units/T23.md).

## Literature-named inputs

`ReciprocityTheory.ChartRestriction.G.ArakelovGeometry.MoriwakiBigStatement` — hypothesis at this head (`ReciprocityTheory/ReductiveGroups/ArithmeticGeometry/ArakelovGeometry/MoriwakiSt.lean:29–36`); not compared.

`GlobalTheory.Published.SemiAbelianHomExtension` — hypothesis at this head (`Development/AbelianVarietyTheory/PublishedTheorems/SemiabelianTori/GeometricallyConnectedSplitTorusAff.lean:15–20`); not compared.

`GlobalTheory.CompanionTheory.Ar.HT.FarguesHodgeTate` — hypothesis at this head (`Development/AutomorphicSpectrum/PublishedTheorems/Algebra₂/FarguesHodgeTate.lean:10–20`); not compared.
