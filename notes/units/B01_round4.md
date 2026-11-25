# B01 · Theta lifting and the polarised Galois row

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 720,478 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**Outlined · pending_review.** Assume the specified stable-range theta lift. The resulting Galois representation for each regular algebraic polarized cuspidal pair has the stated Hodge–Tate symmetry and local comparisons, with stronger conclusions only at places satisfying their extra conditions.

## Statement and hypotheses

Assume the following stable-range lift. Fix good CM base data, $n\ge1$ and
the Hermitian space with matrix $1$ and signature $(n,0)$. There is $d_0$
such that for every $d\ge d_0$, skew space with matrix $\delta I_d$ and
signature as in the lift, and splitting Hecke characters $\chi_X,\chi_W$
with the prescribed quadratic restrictions and infinity exponents $m_X,m_W$,
each automorphic $U$ with weights $\lambda_v$ satisfying
$d+m_W(v)\le2\lambda_v(k)$ for every $v,k$ has a target $U'$ satisfying
the specified theta-lift relation. Under this assumption every regular
algebraic polarised cuspidal pair as above admits $r$, $w_\pi\in\mathbb Z$
and Hodge--Tate multisets $H_\tau$ satisfying the whole row below.

The representation $r$ is continuous and semisimple. The multiset
$H_\tau$ is $(a-1)/2$ minus the infinitesimal character at $\iota\tau$,
and $H_{\tau c}=w_\pi-H_\tau$. At each $w\nmid\ell$ and for
*every* parameter map satisfying the local laws in
[B04](../../units/B04.md), compare $\mathrm{WD}(r|_{E_w})$ with the parameter
of the algebraically normalised local component. They have equal dimension.
A toral target with zero monodromy gives equality; under the source's
`IsQpBig`, tame and squarefree conditions, a target with
zero monodromy gives zero monodromy and equality of characteristic polynomials
on degree-zero Weil elements. For every tied local comparison datum and
inducing bridge above $\ell$, a spherical component gives crystallinity,
the de Rham property and jumps $H_\tau$ at every induced embedding.
A zero-monodromy toral target, or a zero-monodromy target satisfying the
three tame-range conditions, gives the de Rham and potentially semistable
properties, the same jumps and the preceding Weil--Deligne comparison. [`galoisRepresentations_of_thetaLift` · `GaloisRepresentationsOfThetaLift.lean:6-6`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GaloisRepresentationsOfThetaLift.lean#L6-L6)

In both tame clauses, `IsQpBig` requires a prime $g$ and a continuous ring isomorphism from $\mathbb Q_g$ to the completion at $w$, with $n=1$ or $16n^2<g$ for the relevant rank $n$. `UpperTheory.GalStar.IsQpBig` (`Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/TypeConditions/WeightsConjBis.lean:15–16`). `UpperTheory.GalStar.AwayB` (`Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/TypeConditions/WeightsConjBis.lean:26–31`). `UpperTheory.GalStar.AboveB` (`Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/TypeConditions/WeightsConjBis.lean:48–52`).

**Read alongside** [B02 · Weight-one geometric realisation in odd rank](../../units/B02.md) · [B03 · Local–global compatibility from geometric realization and theta lifting](../../units/B03.md) · [B04 · A local parameter with the tame type law](../../units/B04.md).

## Insert the geometric seed

The top statement takes stable-range lifting as an input. The other argument of the geometry-to-row theorem is the weight-one geometric realization. Its supplier unfolds the specified holomorphic Lefschetz statement and uses the fixed-point formula for the finite étale correspondence. The weight-one realization theorem takes that formula as its premise. This explains which part of the geometric hypothesis is obtained internally on this route and which theta-lift existence statement is still assumed. A formula for a different correspondence would not supply this seed. [`weight_one_geometric_realization` · `WeightOneGeometricRealization.lean:7-9`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/WeightOneGeometricRealization.lean#L7-L9) · [`geoOne_holds` · `WeightOneGeometricRealization.lean:11-11`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GeometricFlagBases/WeightOneGeometricRealization.lean#L11-L11) · [`galoisRepresentations_of_thetaLift` · `GaloisRepresentationsOfThetaLift.lean:6-6`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GaloisRepresentationsOfThetaLift.lean#L6-L6)

## Build the core before making local comparisons

From the geometric realization obtain a seed at finite odd level. A weight-existence input supplies the congruence condition. Take the finite odd-level limit using both. The construction then combines that limit with the assumed lift, compatibility of the closed trace and descent off the exceptional set to obtain the core used by the global row. The local reciprocity predicate in this construction is the one defining the parameter maps in the unit statement. The successive calls are recorded at the pin; the analytic and arithmetic constructions establishing the limit are lower inputs here. [`recT` · `Development.lean:18-22`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/Development.lean#L18-L22) · [`galoisLocalGlobal_of_geometry_lift` · `Development.lean:27-28`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/Development.lean#L27-L28)

## Obtain the local comparisons

Given the core, obtain compatibility on the unlinked support from spherical information. Use it a second time for the Iwahori-fixed local comparison. Combine the two specialized compatibilities with the original core to obtain the local/global row. The final operation weakens `Row0` to `Row0b` for the same reciprocity predicate. Despite the Lean name `galoisLocalGlobalStrong_of_geometry_lift`, `Props.big` drops part of the tame comparison by passing from `IsQpBig` to `IsQp`. `UpperTheory.GalStar.Row0.row0b` (`Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/TypeConditions/WeightsConjBis.lean:84–86`). `UpperTheory.GalStar.Props.big` (`Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/TypeConditions/WeightsConjBis.lean:75–82`). In reading the long statement, keep distinct the spherical hypothesis above the coefficient prime, the toral zero-monodromy cases and the extra large-residue, tame and squarefree conditions in the other zero-monodromy cases. [`rest` · `Development.lean:24-25`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/Development.lean#L24-L25) · [`galoisLocalGlobalStrong_of_geometry_lift` · `Development.lean:30-31`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/Development.lean#L30-L31)

## Range of the conditional statement

The assumed lift has a threshold in the target dimension and conditions at every infinity place on the splitting characters and source weights. The comparison away from the coefficient prime quantifies over maps satisfying the local reciprocity laws of B04. Thus neither a single constructed comparison map nor a lift in one dimension would meet these inputs. The core and both row conversions use the specified predicates throughout; the resulting local conclusions retain their case distinctions. [`galoisRepresentations_of_thetaLift` · `GaloisRepresentationsOfThetaLift.lean:6-6`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/GaloisRepresentationsOfThetaLift.lean#L6-L6) · [`recT` · `Development.lean:18-22`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/Development.lean#L18-L22)

## Literature-named inputs

`UpperTheory.TP.TLiftK` — hypothesis at this head (`Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/ThetaParseval/HalfIndexLattices/TLiftK.lean:12–23`); not compared.

`UpperTheory.Cb.lefschetz_fixedPoint_finite_etale_correspondence` — in-repo constant (`Development/AutomorphicArithmetic/Foundations/EtaleClopenDescent/LefschetzFixedPointFiniteEtaleCorrespondence.lean:255–358`); not compared.

`GlobalTheory.T.lefschetz_fixedPoint_finite_etale_correspondence` — in-repo constant (`Development/AbelianVarietyTheory/Proofs/SatakeParameters/LefschetzFixedPointFiniteEtaleCorrespondence.lean:8–15`); not compared.

**First step to challenge.** Check the passage from finite odd-level seeds and congruences to the global core using the assumed stable-range lift. The final row projections alone supply no such passage.

[Unit record and exact statement](../../units/B01.md)
