# T24 · Why the orthogonal kernel is an integral assertion

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 1,613 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**pending_review** · [Unit card](../../units/T24.md) · [Track guide](../../tracks/local/README.md)

A bilinear form on the two extended Tate modules, normalized by the Weil pairing, detects the Hodge–Tate kernel by testing against the kernel of the dual logarithmic differential. The theorem handed to the reader accepts a literature record. Its implementation uses a separately constructed prismatic comparison. `UpperTheory.LiteratureTheorems.fargues_exact_of_literature` ([EveryCharacterOfLiteratureOfVWin.lean:549–550](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean#L549-L550)).

## Fix the two integral modules and the form

Take a prime $p$, an algebraically closed field $C$ of characteristic zero with valuation $v$, and a valuation ring $O$ over the $p$-adic integers, complete for $(p)$, with $v(p)<1$. Fix the $p$-divisible group $G/O$ and roots $\zeta_0=1$, $\zeta_{n+1}^p=\zeta_n$, $\zeta_1\ne1$. For each pair of Tate vectors there must exist one $p$-adic integer giving both the exponent of the Weil pairing and the value of $B$ after applying the coefficient map. This compatibility fixes the scaling of the bilinear form. The test variable $y$ belongs to the extended Tate module on the dual side. The assertion ranges over all such $y$ killed by its differential. `GlobalTheory.CompanionTheory.Ar.HT.FarguesExact` ([FarguesExact.lean:10–18](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicSpectrum/PublishedTheorems/Algebra₂/FarguesExact.lean#L10-L18)).

## Identify the supplier behind the interface

Read the body of the wrapper. The named open-literature argument does not occur in it. The closed term uses a prismatic Hodge statement constructed from a primitive system, connected and dual-connected group data, and matrices lifted to the Fontaine ring. Following those calls identifies the additional proof obligations a specialist would need to inspect for an independent derivation. No identification of those obligations with a particular published theorem is used here. `UpperTheory.LiteratureTheorems.fargues_exact_of_literature` ([EveryCharacterOfLiteratureOfVWin.lean:549–550](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean#L549-L550)). `UpperTheory.Lit.farguesExact` ([PrismaticDieudonneHodge.lean:27–28](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/PrismaticDieudonne/PrismaticDieudonneHodge.lean#L27-L28)). `UpperTheory.Lit.prismaticDieudonneHodge` ([PrismaticDieudonneHodge.lean:19–25](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/PrismaticDieudonne/PrismaticDieudonneHodge.lean#L19-L25)).

## Move from pure Tate vectors to the desired functional

The source obtains a primitive system for the comparison and a Hodge–Tate sandwich. Multiplication by the distinguished Tate root identifies the exponent uniquely; comparing the two pairings on pure tensors and extending by tensor induction identifies the form used in the kernel description with the given $B$. In the forward direction that description gives a nonzero scalar $c$ and a functional $l$ such that $cB(x,y)=l(\mathrm{dlog}(y))$. Setting the differential to zero and cancelling $c$ in the domain gives orthogonality. `PositivityTheory.Tls2.Jfarg.farguesExact_of_hodge` ([FarguesExactOfPrismatic.lean:56–107](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/TemperedRepresentationTheory/FarguesExactness/FarguesExactOfPrismatic.lean#L56-L107)).

## Recover the converse over the original ring

Suppose $B(x,-)$ vanishes on the differential kernel. The proof uses the inclusion of $p^2$ times the target in the span of the logarithmic differentials. The span lies in the range of the linearized differential by evaluating on pure tensors. Factorization therefore supplies a functional after multiplication by $p^2$. This multiplier is nonzero in $O$, exactly the witness needed for the integral kernel description. [D309](../../units/D309.md) adds a separate annihilator bound when assembling the larger Hodge–Tate package. The construction and bounds underlying the sandwich and the $p^2$ span remain separate inputs to this outline. `PositivityTheory.Tls2.Jfarg.farguesExact_of_hodge` ([FarguesExactOfPrismatic.lean:56–107](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/TemperedRepresentationTheory/FarguesExactness/FarguesExactOfPrismatic.lean#L56-L107)). `GlobalTheory.CompanionTheory.Relay.hodge_tate_of_fargues_exact` ([HodgeTateOfFarguesExact.lean:36–37](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicSpectrum/Proofs/AlgebraProofs/HodgeTateOfFarguesExact.lean#L36-L37)).

The Lean head takes the open-literature record and does not use it. `UpperTheory.LiteratureTheorems.fargues_exact_of_literature` (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean:549–550`).

## Literature-named inputs

`UpperTheory.Lit.farguesExact` — in-repo constant (`Development/AutomorphicArithmetic/ThetaCorrespondence/PrismaticDieudonne/PrismaticDieudonneHodge.lean:27–28`); not compared.

`UpperTheory.LiteratureTheorems.fargues_exact_of_literature` — in-repo constant (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean:549–550`); not compared.

`PositivityTheory.Tls2.Jfarg.farguesExact_of_hodge` — in-repo constant (`Development/WeilBound/CoreStatements/TemperedRepresentationTheory/FarguesExactness/FarguesExactOfPrismatic.lean:56–107`); not compared.

`GlobalTheory.CompanionTheory.Relay.hodge_tate_of_fargues_exact` — in-repo constant (`Development/AutomorphicSpectrum/Proofs/AlgebraProofs/HodgeTateOfFarguesExact.lean:36–37`); not compared.

`PositivityTheory.Xgn.farguesHodgeTate_of_farguesExact` — in-repo constant (`Development/WeilBound/CoreStatements/TorusUniformisation/ChowMahlerFamilies/XXgzFarOfExact.lean:50–60`); not compared.

**First step to challenge.** In the reverse implication, check that the image of the differential contains every $p^2w$ in the original module, so factorization over the valuation ring yields the required functional.
