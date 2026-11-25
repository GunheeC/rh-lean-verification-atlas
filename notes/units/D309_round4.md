# D309 · Two distinct inputs to the Hodge–Tate package

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 517 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**pending_review** · [Unit card](../../units/D309.md) · [Track guide](../../tracks/local/README.md)

The kernel criterion supplied by Fargues exactness gives one half of a Hodge–Tate package. The other half bounds the cokernel over the valuation ring and needs its own theorem, with a special inequality at two. `GlobalTheory.CompanionTheory.Relay.hodge_tate_of_fargues_exact` ([HodgeTateOfFarguesExact.lean:36–37](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicSpectrum/Proofs/AlgebraProofs/HodgeTateOfFarguesExact.lean#L36-L37)).

## Separate the two statements at a fixed group

Fix the prime $p$, algebraically closed characteristic-zero field, valuation ring over the $p$-adic integers and $p$-adically complete structure required by both definitions. Fix one $p$-divisible group $G$. The target has two conjuncts. Its first says that for an admissible $\kappa$ every vector $w$ in the dual invariant differentials has $\kappa w$ in the range of the Hodge–Tate map. Its second is an equivalence on vectors of the extended Tate module. It uses a chosen root system and a bilinear pairing normalized on pure Tate vectors. These last choices are quantified only in the kernel part. `GlobalTheory.CompanionTheory.Ar.HT.FarguesExact` ([FarguesExact.lean:10–18](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicSpectrum/PublishedTheorems/Algebra₂/FarguesExact.lean#L10-L18)). `GlobalTheory.CompanionTheory.Ar.HT.FarguesHodgeTate` ([FarguesHodgeTate.lean:10–20](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicSpectrum/PublishedTheorems/Algebra₂/FarguesHodgeTate.lean#L10-L20)).

## Read the kernel input in the correct direction

At this fixed $G$, specialize exactness to the same valued field, ring and group. Its remaining universal quantifiers are exactly the root system, bilinear pairing, compatibility predicate and test vector needed for the second conjunct. This implication does not obtain a cokernel estimate from orthogonality. [T24](../../units/T24.md) is where the argument producing that orthogonality condition can be inspected. The simple reuse of its statement here explains why no new duality or dimension count occurs in this component. `PositivityTheory.Xgn.farguesHodgeTate_of_farguesExact` ([XXgzFarOfExact.lean:50–60](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/TorusUniformisation/ChowMahlerFamilies/XXgzFarOfExact.lean#L50-L60)). `UpperTheory.LiteratureTheorems.fargues_exact_of_literature` ([EveryCharacterOfLiteratureOfVWin.lean:549–550](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean#L549-L550)).

## Read the scalar bound as an integral image condition

The additional sharp-cokernel theorem supplies membership in the actual integral range. For $p\ne2$, the target already requires $v(\kappa)^{p-1}\le v(p)$. At two the target requires $v(\kappa)\le v(4)$. Multiplicativity gives $v(4)=v(2)^2$, and $v(2)<1$ implies $v(2)^2\le v(2)$. Since $p-1=1$, this is the inequality needed by the uniform theorem. Dividing vectors by $\kappa$ over the fraction field would lose precisely the image statement being passed on. `GlobalTheory.CompanionTheory.Ar.HT.hodge_tate_cokernel_sharp` ([HodgeTateCokernelSharp.lean:7–8](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicSpectrum/Proofs/GeometryProofs/HodgeTateCokernelSharp.lean#L7-L8)). `GlobalTheory.CompanionTheory.Ar.HT.FarguesHodgeTate` ([FarguesHodgeTate.lean:10–20](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicSpectrum/PublishedTheorems/Algebra₂/FarguesHodgeTate.lean#L10-L20)). `PositivityTheory.Xgn.farguesHodgeTate_of_farguesExact` ([XXgzFarOfExact.lean:50–60](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/TorusUniformisation/ChowMahlerFamilies/XXgzFarOfExact.lean#L50-L60)).

## Record the interface consumed by subsequent uses

The exported implication forwards the two conclusions at the very same ring and group. Its short proof leaves the source of the separate sharp-cokernel theorem to the cited supplier. A check of the quantifier order should test any admissible $\kappa$ and then any $w$, without introducing a multiplier depending on $w$. This distinction allows a reader of [T13](../../units/T13.md) or [T14](../../units/T14.md) to locate exactly which input provides control of the integral discrepancy. `GlobalTheory.CompanionTheory.Relay.hodge_tate_of_fargues_exact` ([HodgeTateOfFarguesExact.lean:36–37](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicSpectrum/Proofs/AlgebraProofs/HodgeTateOfFarguesExact.lean#L36-L37)). `GlobalTheory.CompanionTheory.Ar.HT.hodge_tate_cokernel_sharp` ([HodgeTateCokernelSharp.lean:7–8](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicSpectrum/Proofs/GeometryProofs/HodgeTateCokernelSharp.lean#L7-L8)).

## Literature-named inputs

`GlobalTheory.CompanionTheory.Relay.hodge_tate_of_fargues_exact` — in-repo constant (`Development/AutomorphicSpectrum/Proofs/AlgebraProofs/HodgeTateOfFarguesExact.lean:36–37`); not compared.

`PositivityTheory.Xgn.farguesHodgeTate_of_farguesExact` — in-repo constant (`Development/WeilBound/CoreStatements/TorusUniformisation/ChowMahlerFamilies/XXgzFarOfExact.lean:50–60`); not compared.

`UpperTheory.LiteratureTheorems.fargues_exact_of_literature` — in-repo constant (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean:549–550`); not compared.

`UpperTheory.Lit.farguesExact` — in-repo constant (`Development/AutomorphicArithmetic/ThetaCorrespondence/PrismaticDieudonne/PrismaticDieudonneHodge.lean:27–28`); not compared.

**First step to challenge.** Check the threshold at $p=2$. The source first weakens the valuation bound involving four and only then applies the uniform sharp-cokernel input.
