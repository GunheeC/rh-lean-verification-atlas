# W01 · The rank record that supplies a common Selmer window

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 884,497 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**Outlined · pending_review.** Assume three inputs: the one-field open-image condition $O$, the isobaric base-change assertion for the specified definite groups, and the polarized Galois row. The output puts a single interval around a bound for the localization lengths of all the fields that the chosen character and prime pair prescribe. Thus the mathematical content of W01 is the compatibility of the three starting inputs with that particular arithmetic conclusion. [The complete window statement](../../pillars/V.md) · [W02](../../units/W02.md) · [V-OPEN](../../units/V-OPEN.md). `automorphic_window_of_inputs` (`TopMainZj.lean:71–74`) `VWin` (`ExistsPageN.lean:49–49`) `VWinAt` (`ExistsPageN.lean:44–47`) `VVle` (`ExistsPageN.lean:12–17`)

## Assemble one rank record

1. **Supply the CM field of the record.** Starting with $O$, form the eleven components required by the CM hypothesis. In particular the dual-crystal assertion combines a dual-abelian-scheme result with a smooth-lift comparison. Period comparison, the Gauss–Manin statement and the Serre–Tate assertion have their own suppliers. The elliptic CM, Hilbert class field, Deligne–Ribet, partial zeta and Hecke–Tate assertions occupy separate slots. The caller in W01 passes this one CM record, as a fourth argument, to its conditional subtheorem. This is the indexed sub-statement D118. `cm_abelian_inputs_from_literature` (`TopMainZj.lean:59–70`) `LiteratureCMHypothesis` (`LitAut.lean:47–58`) `automorphic_window_of_inputs` (`TopMainZj.lean:71–74`)
2. **Keep the automorphic row and base change in their designated slots.** The local package uses eighteen assignments from $O$. The automorphic package has a field `bc` for base change and a field `gal` for the row. It also uses separately named suppliers for finiteness, purity, reciprocity and the remaining slots. A Galois-cohomology package is constructed from $O$. Together with the first step, these give exactly the local, automorphic, cohomological and CM fields of the rank record. The implication from these inputs to the window is the indexed sub-statement D114. `local_inputs_from_literature` (`TopMainZj.lean:18–37`) `automorphic_inputs_from_literature` (`TopMainZj.lean:38–54`) `LiteratureRankNHypothesis` (`LitAut.lean:59–63`) `v_window_of_depth_zero_residual_bc_cm` (`TopMainZj.lean:55–58`)
3. **Follow the same record through the arithmetic reduction.** The rank record is augmented by the patching supplier with its fixed descent argument. Its projected rank input gives a single witness to the existence of the cohomology-bound constant. Its pair of end conclusions is used twice. One projection enters the unramified automorphy input to count I, and the other enters count V. Counts II and III are the two projections of another joint result. At that point the four-count theorem accepts the original rank input, the constant witness, and counts I, II, III and V. [P024](../../units/P024.md) · [P020](../../units/P020.md). `v_window_of_literal_automorphy_n` (`WindowBoundOfLiteratureLevel.lean:33–34`) `v_window_of_automorphy_csd_ss_mono_odd` (`WindowBoundOfLiteratureLevel.lean:30–31`) `vwin_of_hypotheses_H_E_alt` (`WindowBoundOfLiteratureLevel.lean:25–29`) `of_four_alt` (`HVCore.lean:18–22`)

## What the assembly has to preserve

Consider a single test of the output: fix a primitive character, an allowed exponent and a page function before choosing an outer scale and its prime pair. The test allows its field to vary with a point $x$ of the returned interval and allows a new finite set of primes for every evaluation. Consequently a hypothetical argument that only returned an interval separately for each cohomological datum would leave a logical gap even if the same numerical upper bound occurred each time. In the source the same four-count implication supplies the quantified `VWin` as a whole. The proof of its last passage chooses the window before the field and the local data. [W08](../../units/W08.md) · [W09](../../units/W09.md). `of_four_alt` (`HVCore.lean:18–22`) `VWinAt` (`ExistsPageN.lean:44–47`) `VAt` (`ExistsPageN.lean:41–42`) `VVle` (`ExistsPageN.lean:12–17`) `vwinAt_of_joint` (`AdmissibleOfPageN.lean:41–129`)

The routine step here is applying D114 after giving it D118. The arithmetic step remains the construction and use of the count and end records with their common witnesses. A CM record field whose mathematical name is familiar still has the exact type specified by the local development. A reader can grant the whole record conditionally or open each available assignment; those are different levels of the same reading task. The cited supplier fixes which record is in use. `automorphic_window_of_inputs` (`TopMainZj.lean:71–74`) `LiteratureCMHypothesis` (`LitAut.lean:47–58`) `vwin_of_hypotheses_H_E_alt` (`WindowBoundOfLiteratureLevel.lean:25–29`)

The head passes `O` to the CM and automorphic adapters. Its sole field is never projected on this route; the map also receives the row argument `gal` separately. See the source search and the three separate arguments in [pillar V](../../pillars/V.md). `UpperTheory.One.Join.automorphic_window_of_inputs` (`Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/TopMainZj.lean:71–74`).

## Literature-named inputs

`UpperTheory.Lit.serreTateGoodReduction` — in-repo constant (`Development/AutomorphicArithmetic/ThetaCorrespondence/GoodReduction/SerreTate.lean:15–16`); not compared.

`UpperTheory.LiteratureTheorems.siegel_klingen_deligne_ribet_of_open` — in-repo constant (`Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/TemperedProductOfSquareIntegrable.lean:219–220`); not compared.

`UpperTheory.LiteratureTheorems.harish_chandra_finite_of_open` — in-repo constant (`Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/TemperedProductOfSquareIntegrable.lean:291–292`); not compared.

`UpperTheory.LiteratureTheorems.jacquet_shalika_of_open` — in-repo constant (`Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/TemperedProductOfSquareIntegrable.lean:297–298`); not compared.

`UpperTheory.LiteratureTheorems.clozel_purity_of_open` — in-repo constant (`Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/TemperedProductOfSquareIntegrable.lean:279–280`); not compared.

`UpperTheory.LiteratureTheorems.clozel_cohomological_of_open` — in-repo constant (`Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/TemperedProductOfSquareIntegrable.lean:277–278`); not compared.

`UpperTheory.LiteratureTheorems.global_artin_reciprocity_of_open` — in-repo constant (`Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/TemperedProductOfSquareIntegrable.lean:225–226`); not compared.

`UpperTheory.V.Z.J.count_i_of_printed_bound_k_kato_automorphy` — in-repo constant (`Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/LinkedUnlE.lean:49–54`); not compared.

`UpperTheory.V.Z.Kato.WeilSphericalRecords.katoTwoW_of_printsH` — in-repo constant (`Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/KatoTwoWOfPublishedH.lean:48–49`); not compared.

**First step to challenge.** Trace the two end projections and the common cohomology constant through counts I, II, III and V, then verify that the four-count result has the field-independent interval required by W01. `vwin_of_hypotheses_H_E_alt` (`WindowBoundOfLiteratureLevel.lean:25–29`) `of_four_alt` (`HVCore.lean:18–22`) `VWinAt` (`ExistsPageN.lean:44–47`)
