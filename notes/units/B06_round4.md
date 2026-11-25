# B06 · Valuation of period columns in a selected family

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 21,017 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**Outlined · pending_review.** For the specified twist selection and enriched family, sufficiently large points have the required level-prime valuation bound on period columns. The point, period and size estimates used to obtain it must apply to the same family at the same scale.

## Statement and hypotheses

Fix $\mathcal A$ with a twist selection. On $D_3(3,\mathcal A)$ suppose
the following are closed: untwisted point and twisted-point integrality;
the untwisted period-class Weyl sum and twisted-period admissibility;
the sharp untwisted and twisted column bounds at the selected level;
and the existence of a common constant for the used tuples and the
family size at the type prime. Suppose the selection is served on this
class. Then the following too is closed: there is $x_0$ such that
for $x\ge x_0$, $x>x_1(F)$ and each index at $x$, for every unit $u$,
place $w$, lattice vector $\phi\in L.\mathrm{NuLat}(u)$ and form
$F'$ in the prescribed level module and the subspace $V_0$, there is
a coefficient-field element $y$ whose fixed embedding equals the period
column at $(u,w,\phi,F')$. It is zero or satisfies
$v_w(y)\ge\lfloor\operatorname{ur}(D,w,L.\mathrm{sg}(u,w))\rfloor$. [`closed_family_admissible_twist_link_alt` · `ClosedFamilyAdmissibleTwistLink.lean:12-31`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ClosedFamilyAdmissibleTwistLink.lean#L12-L31)

**Read alongside** [D394 · Tying period entries to level valuations](../../units/D394.md) · [P047 · Four cases for the first column bound](../../units/P047.md) · [Z4.3 · Off-level kernel valuations](../../units/Z4.3.md) · [Z4.4 · Twisted periods on the selected chain](../../units/Z4.4.md).

## Collect the period data

Restrict the original chosen twist to the enriched family class. The hypotheses give eventual estimates for untwisted and twisted points, for the reference period class sum and admissibility of the twisted period, and for sharp column bounds at the selected level. These concern the original datum or its specified twist, depending on the clause. Separately one common constant controls both the used tuples and the family size at the type prime. The final service hypothesis applies to the selected twist. Keep the quantifiers on these constants outside the subsequent pointwise variables. [`closed_family_admissible_twist_link_alt` · `ClosedFamilyAdmissibleTwistLink.lean:12-25`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ClosedFamilyAdmissibleTwistLink.lean#L12-L25)

## Turn service into a family assertion

From membership in the enriched class extract its size component for the discriminant parameter. Combine it with service of the chosen twist. The service summation over primes produces the family service needed in the admission record. The eventual stabilizer coprimality field is obtained separately on the family carrying the level character. Insert these two fields with the point, period, column and type-prime bounds into the input for level-two admissibility. This is the point at which the proof uses more than a collection of period inequalities. [`closed_family_admissible_twist_link_alt` · `ClosedFamilyAdmissibleTwistLink.lean:25-31`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ClosedFamilyAdmissibleTwistLink.lean#L25-L31) · [`closed_servF_of_servT_of_dGamSize` · `GServT.lean:31-33`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/GServT.lean#L31-L33)

## Get one large scale for all the local tests

For a fixed family take a maximum of the finitely many point, period, service, stabilizer and size thresholds and the auxiliary threshold $3^{5/e_z}$. At every scale above this maximum apply the local level-two result using the same index in each estimate. The family data give local compatibility and the parameters of the served model. Positivity of $e_z$ translates the auxiliary threshold into $3\le x^{e_z/5}$. Thus all quantities needed by the local calculation are present at once. This is the substantive step behind the eventual assertion. [`famU` · `AdmissibleAtGeneratorPlaces.lean:263-275`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/GroupLattices/AdmissibleAtGeneratorPlaces.lean#L263-L275) · [`famU` · `AdmissibleAtGeneratorPlaces.lean:276-300`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/GroupLattices/AdmissibleAtGeneratorPlaces.lean#L276-L300)

## Pass to a closed property

Closure of a finite conjunction takes the smaller exponent range and bounds its parameter functions by componentwise maxima. The admissibility implication gives two eventual conclusions. Project the first, which is the required level-two bound. Specializing its datum and lattice yields the alternative that the coefficient-field period is zero or its valuation has the stated lower bound. None of these choices asks for a scale adapted to an individual form or lattice vector. [`admissible_family_of_inclusion` · `AdmissibleAtGeneratorPlaces.lean:315-329`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/GroupLattices/AdmissibleAtGeneratorPlaces.lean#L315-L329) · [`closed_family_admissible_twist_link_alt` · `ClosedFamilyAdmissibleTwistLink.lean:27-31`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/ClosedFamilyAdmissibleTwistLink.lean#L27-L31)

**First step to challenge.** Check the common threshold in the level-two argument. It must control both the used tuples and the family size with the same constant at every eligible point.

[Unit record and exact statement](../../units/B06.md)
