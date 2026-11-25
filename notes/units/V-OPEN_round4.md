# V-OPEN · Which Galois row the open-image record contains

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 2 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**Outlined · pending_review.** Fix a witness $h$ of the polarized-pair Galois row specialized to the local reciprocity relation `IsRecT`. The structure called `OpenImageCondition` in the Selmer-window supplier has one field of precisely this row type. Giving the witness to its constructor produces the record needed by [W01](../../units/W01.md). This step of [P013](../../units/P013.md) neither constructs the Galois representation from automorphy nor gives an independent open-image estimate. `vwin_of_row` (`VwinOfRow.lean:4–5`) `OpenImageCondition` (`TemperedProductOfSquareIntegrable.lean:207–208`) `RowT` (`WeakOfAtt.lean:47–47`)

## Identify the argument supplied to the constructor

The definition `RowT` specializes `Row0b` to the relation `fun h rc => IsRecT h rc`. Unfolding this abbreviation at the site of P013 identifies its input with the type required by the sole field. In particular the local reciprocity rule has been fixed. A row establishing compatibility for some other reading rule cannot be substituted by changing the notation for the field. `RowT` (`WeakOfAtt.lean:47–47`) `OpenImageCondition` (`TemperedProductOfSquareIntegrable.lean:207–208`) `vwin_of_row` (`VwinOfRow.lean:4–5`)

To see what is being carried, fix a CM field and its algebraic closure, a prime, an identification of the algebraic coefficient closure with the complex numbers, and a positive rank. For every regular algebraic cusp datum and character of the maximal real subfield satisfying the polarized-pair condition, the row supplies a representation, an integral weight and Hodge–Tate multiset data for each embedding. Its `PropsB` includes continuity and semisimplicity, a local compatibility quantified at primes away from the coefficient prime, and the weight and conjugation identities. The local condition above the coefficient prime quantifies over the compatible comparison objects that appear explicitly in its type. `Row0b` (`WeightsConjBis.lean:69–73`) `PropsB` (`WeightsConjBis.lean:54–67`)

For example, the `above` clause takes a local prime and auxiliary comparison data with a nonemptiness condition for a tied object, then a place, a valuation extension and a period bridge over the coefficient ring. Its conclusion distinguishes the crystalline condition for a spherical component from the potentially semistable conclusion under the separate local parameter hypotheses. Consequently quoting a representation with the correct traces at almost every prime would not supply the recorded field by itself. No one needs to prove these local conclusions during the constructor application: they are included in the assumed witness. `PropsB` (`WeightsConjBis.lean:54–67`) `AboveB` (`WeightsConjBis.lean:39–52`)

## Follow both uses of the witness

The constructor stores $h$ as `galoisRepOfPolarizedPairLit`. The complete source-level operation is visible in the call in P013; the compiler-generated constructor has no separate line span. W01 uses $O$ as one argument and takes the polarized row as another. The latter supplies the automorphic package's `gal` field. Both uses can therefore draw on exactly the same representation row. The isobaric base-change field of the automorphic package instead comes from [W02](../../units/W02.md). `OpenImageCondition` (`TemperedProductOfSquareIntegrable.lean:207–208`) `vwin_of_row` (`VwinOfRow.lean:4–5`) `automorphic_window_of_inputs` (`TopMainZj.lean:71–74`) `automorphic_inputs_from_literature` (`TopMainZj.lean:38–54`)

A reader granting the row can check the repackaging by matching the field type, its single constructor argument and the actual use on the call line. A reader reconstructing the row itself must instead account for all the above local and global assertions. This difference in scope explains how a structure can have a two-line declaration and still carry a difficult assumption. [The surrounding supplier](../../pillars/V.md). `OpenImageCondition` (`TemperedProductOfSquareIntegrable.lean:207–208`) `RowT` (`WeakOfAtt.lean:47–47`) `Row0b` (`WeightsConjBis.lean:69–73`) `vwin_of_row` (`VwinOfRow.lean:4–5`)

This head is a structure declaration. Its single projected value has type `RowT`. The uses of a constructed record by the V supplier are downstream reading directions. `UpperTheory.LiteratureTheorems.OpenImageCondition` (`Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/TemperedProductOfSquareIntegrable.lean:207–208`).

**Scope of the hypotheses.** The note retains the source’s named predicates and records. For the exact quantified assumptions at this head, read `UpperTheory.LiteratureTheorems.OpenImageCondition` (`Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/TemperedProductOfSquareIntegrable.lean:207–208`). Their internal definitions are separate reading tasks.

## Literature-named inputs

`UpperTheory.LiteratureTheorems.harish_chandra_finite_of_open` — in-repo constant (`Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/TemperedProductOfSquareIntegrable.lean:291–292`); not compared.

`UpperTheory.LiteratureTheorems.jacquet_shalika_of_open` — in-repo constant (`Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/TemperedProductOfSquareIntegrable.lean:297–298`); not compared.

`UpperTheory.LiteratureTheorems.clozel_purity_of_open` — in-repo constant (`Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/TemperedProductOfSquareIntegrable.lean:279–280`); not compared.

`UpperTheory.LiteratureTheorems.clozel_cohomological_of_open` — in-repo constant (`Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/TemperedProductOfSquareIntegrable.lean:277–278`); not compared.

`UpperTheory.LiteratureTheorems.global_artin_reciprocity_of_open` — in-repo constant (`Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/TemperedProductOfSquareIntegrable.lean:225–226`); not compared.

**First step to challenge.** Compare the exact reciprocity specialization in `RowT` with the hypothesis of P013, including the above-prime alternatives, before reusing the same witness in the two argument positions. `RowT` (`WeakOfAtt.lean:47–47`) `AboveB` (`WeightsConjBis.lean:39–52`) `vwin_of_row` (`VwinOfRow.lean:4–5`)
