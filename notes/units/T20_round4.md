# T20 · Principalisation with a prescribed boundary

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 1,572 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**Outlined · pending_review.** Principalisation must transform an ideal while tracking an already specified normal-crossings boundary through every blowup. The argument first represents the boundary by a compatible list of divisors, then combines the resulting sequence with three distinct assertions about its endpoint.

## Claim and hypotheses

Let $X/k$ be smooth of relative
dimension $d$, quasi-compact and separated over a characteristic-zero
field. Let $I$ be an ideal whose cosupport contains no irreducible
component of $X$, and $E$ a closed boundary that has simple normal
crossings at every point of $E$. There is a sequence of blowups in
smooth centres with normal crossings with the current boundary,
updating that boundary by total transform at every step. The resulting
$X'$ is smooth, $I\mathcal O_{X'}$ defines an effective Cartier divisor
with simple normal crossings reduced support, and $X'\to X$ is an
isomorphism off the cosupport of $I$. This wrapper also uses a closed term.

[`UpperTheory.LiteratureTheorems.principalisation_char_zero_of_literature` · `EveryCharacterOfLiteratureOfVWin.lean:555–556`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean#L555-L556)

## Translate the closed boundary into a list

The top-level record argument is present in the statement, while its proof takes a closed principalisation supplier. The supplier combines a theorem for a general boundary with `gBoundary`. Using noetherianity, this latter theorem obtains a finite family of components of $E$, maps each component to its vanishing ideal, and records their union. A mere finite cover of the boundary would be too weak: the principalisation rule requires a list with the normal-crossings property at every point. [`UpperTheory.LiteratureTheorems.principalisation_char_zero_of_literature` · `EveryCharacterOfLiteratureOfVWin.lean:555–556`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean#L555-L556) [`PositivityTheory.ResPlug.WeightsCompactStabilizer.principalisationCharZero_closed` · `PrincipalisationCharZeroClosed.lean:7–8`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/ResolutionCharZero/PrincipalisationCharZeroClosed.lean#L7-L8) [`PositivityTheory.ResPlug.GBnd.gBoundary` · `RqGbnd.lean:777–790`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/ResolutionCharZero/RqGbnd.lean#L777-L790)

## Compare the components on every chart

For a point of $X$, choose the local étale chart and the subset of its coordinate hyperplanes that cuts out $E$. On a refinement assign each relevant component of the finite list its local label. Distinct list indices with the same active label must coincide, since the list has no repeated components. The remaining chart comparisons handle labels that are absent and the equations for those that are present. The equality of the supports follows by taking the union of the vanishing ideals of the components. These checks turn a chartwise hypothesis on the closed set into the required compatible list. [`PositivityTheory.ResPlug.GBnd.gBoundary` · `RqGbnd.lean:782–818`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/ResolutionCharZero/RqGbnd.lean#L782-L818)

## Distinguish the three endpoint properties

For a principalizing sequence the endpoint criterion has three inputs. One asserts an isomorphism on the complement of the original cosupport. One gives strict normal crossings for the reduced inverse image of the cosupport. The third gives effective Cartierness of the actual pulled-back ideal, using that the original ideal is nonzero on components. To express the middle conclusion in the target vocabulary, compare the support of the pulled-back ideal with the inverse image of the original support pointwise, and take the vanishing ideal. Cartierness alone would retain neither this crossing information nor the isomorphism on the complement. [`PositivityTheory.ResPlug.WeightsCompactStabilizer.gEnd_of` · `PrincipalisationCharZeroBotOfEff.lean:236–246`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/ResolutionCharZero/PrincipalisationCharZeroBotOfEff.lean#L236-L246)

## Put the prescribed boundary and endpoint together

The complement isomorphism and strict normal crossings are extracted from the same principalizing sequence; the latter also receives the normal-crossings condition on the input boundary list. Effective Cartierness comes from the separate endpoint supplier. Together with the compatible boundary and center data this gives the full statement. The empty-boundary theorem appears separately in the source and does not supply a proof for a prescribed nonempty $E$. This outline leaves the rule constructing the principalizing sequence and the effective-Cartier supplier as inputs. [`PositivityTheory.ResPlug.WeightsCompactStabilizer.principalisationCharZero_of_eff` · `PrincipalisationCharZeroBotOfEff.lean:263–264`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/ResolutionCharZero/PrincipalisationCharZeroBotOfEff.lean#L263-L264) [`PositivityTheory.ResPlug.WeightsCompactStabilizer.principalisationCharZero_of_boundary` · `PrincipalisationCharZeroOfBoundary.lean:14–15`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/ResolutionCharZero/PrincipalisationCharZeroOfBoundary.lean#L14-L15) [`PositivityTheory.ResPlug.WeightsCompactStabilizer.principalisationCharZero_bot_closed` · `PrincipalisationCharZeroOfBoundary.lean:17–25`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/ResolutionCharZero/PrincipalisationCharZeroOfBoundary.lean#L17-L25)

## First step to challenge

Verify that the finite boundary list describes exactly the original boundary on each chart, and that the final reduced divisor is the support of the pulled-back ideal on that very sequence.

See [T19](../../units/T19.md) for resolution of a reduced singular scheme and [T13](../../units/T13.md) for the family of covolume hypotheses that includes both inputs.

The Lean head takes the open-literature record and does not use it. `UpperTheory.LiteratureTheorems.principalisation_char_zero_of_literature` (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean:555–556`).

## Literature-named inputs

`PositivityTheory.ResPlug.WeightsCompactStabilizer.principalisationCharZero_closed` — in-repo constant (`Development/WeilBound/CoreStatements/ResolutionCharZero/PrincipalisationCharZeroClosed.lean:7–8`); not compared.
