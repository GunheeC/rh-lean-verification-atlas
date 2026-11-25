# T22 · Splitting off an abelian scheme

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 3,757 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**Outlined · pending_review.** A polarized abelian scheme can be recovered as a direct factor of an abelian scheme equipped with stronger polarization data. The construction has to produce both the desired line bundle and explicit inclusion and retraction maps over the original valuation ring.

## Claim and hypotheses

Let $C$ be algebraically closed with a
nonnegative-real-valued valuation and let $R\to C$ identify $R$ as its
valuation ring. Every abelian scheme $A/R$ with a relatively ample
invertible sheaf admits group homomorphisms $i:A\to P$, $r:P\to A$
with $r i=1_A$. The scheme $P/R$ is abelian, smooth of a specified
relative dimension and carries a rigidified symmetric relatively ample
invertible sheaf with trivial polarization kernel.

[`UpperTheory.LiteratureTheorems.zarhin_statement` · `EveryCharacterOfLiteratureOfVWin.lean:547–548`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean#L547-L548)

## Produce the dual and the polarization morphism

The wrapper passes a dual abelian scheme theorem to the Zarhin supplier. The former is itself a fixed term at the open-literature interface. The latter also calls a cube theorem. For the given relatively ample line on $A$, use the cube theorem to prove the additivity conditions for the associated line on the square. The universal property of the dual abelian scheme $B$ then gives a classifying map $A\to B$ and the required homomorphism property. Relative ampleness of the original line makes this map a polarization in the source's sense. [`UpperTheory.LiteratureTheorems.dual_abelian_scheme_of_literature` · `EveryCharacterOfLiteratureOfVWin.lean:545–546`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean#L545-L546) [`PositivityTheory.HtPt.Narrow.zarhin` · `ZarTop.lean:6–7`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/HodgeTatePoints/ZarTop.lean#L6-L7) [`PositivityTheory.PrwZar.zarhinStatement_of_dual_cube_qiR` · `ZarhinStatementOfDualCubeQiR.lean:45–57`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/AbelianHeightsDuality/ZarhinTrick/ZarhinStatementOfDualCubeQiR.lean#L45-L57)

## Use the two quasi-inverse equations

A named supplier gives an integer $m\ge1$ and a return homomorphism $B\to A$ whose two composites are multiplication by $m$ on their respective schemes. Both equations enter the construction on four copies of $A\times B$. The proof chooses quaternion data for $4m^2-1$, constructs the polarization class and proves its rigidification. On a geometric fibre three separate calls establish relative ampleness, the trivial kernel and the required polarization map. The trivial kernel is the extra property that makes the resulting polarization principal. None of this follows just from inserting a copy of $A$ into a product. [`PositivityTheory.PrwZar.principal_of_quasiInverse` · `ZarhinStatementOfDualCubeQiR.lean:27–41`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/AbelianHeightsDuality/ZarhinTrick/ZarhinStatementOfDualCubeQiR.lean#L27-L41) [`PositivityTheory.PrwZar.zarhinStatement_of_dual_cube` · `ZarhinStatementOfDualCubeQiR.lean:68–70`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/AbelianHeightsDuality/ZarhinTrick/ZarhinStatementOfDualCubeQiR.lean#L68-L70)

## Choose the scheme and its symmetric bundle

The repeated product used in the polarization construction is abelian over the original base because products of the input abelian schemes are abelian. The symmetric-bundle comparison uses the dual and cube inputs again and returns a representative with the required properties. Choose the relative dimension of the resulting abelian scheme. At this point the proof has enough data for the scheme and its line bundle in the target without choosing any new ambient base. The relative-dimension and polarization checks refer to that particular product. [`PositivityTheory.PrwZar.zarhinStatement_of_dual_cube_qiR` · `ZarhinStatementOfDualCubeQiR.lean:56–65`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/AbelianHeightsDuality/ZarhinTrick/ZarhinStatementOfDualCubeQiR.lean#L56-L65)

## Exhibit the retraction

Insert $A$ in the first factor and take identities in the other factors. Project the repeated product back to its first factor and then to $A$. Product identities show that the composite is the identity homomorphism of $A$. This final computation is routine once the common polarized product has been supplied. The difficult ingredients left to check separately are the quasi-inverse on the valuation-ring data and the passage to the ample symmetric representative with the prescribed fibre kernel. [`PositivityTheory.PrwZar.zarhinStatement_of_dual_cube_qiR` · `ZarhinStatementOfDualCubeQiR.lean:58–66`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/AbelianHeightsDuality/ZarhinTrick/ZarhinStatementOfDualCubeQiR.lean#L58-L66)

## First step to challenge

Check the two quasi-inverse equations for the polarization and its return map, then verify triviality of the kernel on the constructed product. The existence of a retraction alone gives no such polarization.

The surrounding tower/volume construction uses this input together with quotients by finite flat subgroups. See [T26](../../units/T26.md) and [T14](../../units/T14.md).

The Lean head passes the open-literature record to `dual_abelian_scheme_of_literature`, whose body ignores it. `UpperTheory.LiteratureTheorems.zarhin_statement` (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean:547–548`).

## Literature-named inputs

`PositivityTheory.HtPt.Narrow.zarhin` — in-repo constant (`Development/WeilBound/CoreStatements/HodgeTatePoints/ZarTop.lean:6–7`); not compared.

`UpperTheory.LiteratureTheorems.zarhin_statement` — in-repo constant (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean:547–548`); not compared.

`PositivityTheory.PrwZar.zarhinStatement_of_dual_cube` — in-repo constant (`Development/WeilBound/CoreStatements/AbelianHeightsDuality/ZarhinTrick/ZarhinStatementOfDualCubeQiR.lean:68–70`); not compared.

`PositivityTheory.PrwZar.zarhinStatement_of_dual_cube_qiR` — in-repo constant (`Development/WeilBound/CoreStatements/AbelianHeightsDuality/ZarhinTrick/ZarhinStatementOfDualCubeQiR.lean:45–66`); not compared.
