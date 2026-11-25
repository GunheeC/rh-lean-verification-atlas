# T04 · All 26 large-slot conditions from the open conditions

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 455,025 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**Outlined · pending_review.** Open row conditions and three linked bounds furnish all 26 large-slot obligations for the chosen extension. Some fields come from a common period comparison; the definite-row field requires intersecting several eventual assertions on a single slot.

## Statement and hypotheses

Assume global Artin reciprocity, the convergent unitary Siegel--Weil formula,
the discrete-series cover, Harish--Chandra modules, rapid decay, the
Casselman--Wallach statement, discrete-series classification, and both estimates
of T05. For any proof of `RecTExists`, norm-choice extension, series extension,
geometry and family predicate $N$, let $p$ be their extension parameters.
Suppose T08's open conditions and the linked covolume, functional and
$N$-norm conditions hold at $p$. Then all 26 large-slot row conditions hold
for its built and good slots and its bundle linkage. They give class counts,
the $j$-invariant, rank, the second complement, prime column valuations,
arithmetic at bundle points, reference and twisted points and periods, the
row tie, row bounds, twists, primitivity, lambda primes, divisors,
decomposition points, selection jumps, the $L^p$ and order conditions,
service, zero locus, the frame condition, irreducibility counts, definite
rows and the $N$-norm condition. Each row condition has its own existential
large-slot quantifier. [`allRows_of_open0_alt` · `LinkROfIsLinked.lean:50-86`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkROfIsLinked.lean#L50-L86)

**Read alongside** [T08 · The twelve linked conditions at dependence parameters](../../units/T08.md) · [T05 · Two uniform bounds on indefinite rows](../../units/T05.md) · [D394 · Tying period entries to level valuations](../../units/D394.md) · [D379 · Counting constants from Siegel–Weil](../../units/D379.md).

## Fix the extension and the type of largeness

The statement fixes a proof of `RecTExists`, norm and series extensions, geometry and the family predicate for the norm. Open, functional, covolume and norm assertions are all linked at the resulting extension parameters. The output includes a separate eventually-large slot quantifier for each required field. When one field itself needs properties held by several slots, the helper combines two eventual row assertions using intersection. A second helper projects a bundle linkage down to reciprocity linkage by projecting the equality of the dependent bundle point. Both operations preserve which point carries the row. [`forall_linked_bundles_and_alt` · `LinkROfIsLinked.lean:40-43`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkROfIsLinked.lean#L40-L43) · [`linkR_of_isLinked'` · `LinkROfIsLinked.lean:45-49`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkROfIsLinked.lean#L45-L49) · [`allRows_of_open0_alt` · `LinkROfIsLinked.lean:50-55`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkROfIsLinked.lean#L50-L55)

## Populate the period, arithmetic and local entries

For the given slots and linkage, obtain the six period and level-column assertions together. These yield the reference and twisted points, both periods, their real tie and the sharp level-prime bounds. The convergent unitary formula gives a volume ratio and three separate local-row entries. Some open fields pass directly into the output, including prime and divisor information, the decomposition-point condition and selection jumps. Others change form: the primitive condition gives the $j$-field and the zero-locus condition, and the existing tie supplies the twist entry. Row counting uses the label field together with the convergent formula. Each projection refers to its designated input. [`allRows_of_open0_alt` · `LinkROfIsLinked.lean:52-79`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkROfIsLinked.lean#L52-L79)

## Intersect before using the definite row

The definite row needs primitivity, divisors, goodness and geometric compatibility on one side, and covolume, functional, multiplicity, kappa and defect data on the other. Build their conjunction by repeated use of the linked-row intersection helper. Only after that operation apply the stage-zero definite-row theorem with the discrete-series and harmonic-analysis inputs and both estimates on surjectivity and the lower weight. Read the projections of the conjunction in their actual order. The final norm field, in contrast, is exactly the supplied norm assertion. [`allRows_of_open0_alt` · `LinkROfIsLinked.lean:79-86`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkROfIsLinked.lean#L79-L86)

## Interface with the witness

The witness construction calls this result only after transporting the open conditions and norm rows to the stronger extension, where the functional and covolume bounds already reside. The collection of 26 outputs still needs bundle existence and membership for use in the witness constructor. Thus one can trace a failed row to its particular local, arithmetic or geometric source before inspecting the other inputs to existence. [`hypotheses_nonempty_of_unramified_exponents_alt` · `HypothesesNonemptyOfUnramifiedExponents.lean:49-61`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/HypothesesNonemptyOfUnramifiedExponents.lean#L49-L61)

The parameter `hL` is a proof of the existence statement `RecTExists`. Its local witness is under an existential quantifier. `UpperTheory.Zero.LLC.RecTExists` (`Development/AutomorphicArithmetic/Foundations/LocalLanglands/IsRecTOfIsRec.lean:78–80`). `GlobalTheory.Fc.AllAtMemberStage0.allRows_of_open0_alt` (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkROfIsLinked.lean:50–86`).

**Scope of the hypotheses.** The note retains the source’s named predicates and records. For the exact quantified assumptions at this head, read `GlobalTheory.Fc.AllAtMemberStage0.allRows_of_open0_alt` (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkROfIsLinked.lean:50–86`). Their internal definitions are separate reading tasks.

## Literature-named inputs

`GlobalTheory.Published.GlobalArtinReciprocity` — hypothesis at this head (`Development/AbelianVarietyTheory/PublishedTheorems/AutomorphicForms₂/ExistsUniqueHcharOfFiniteOrder.lean:70–72`); not compared.

`HeckeCharacterZeroLocus.SiegelWeilU.SiegelWeilUnitaryConvergent` — hypothesis at this head (`Formalism/UnipotentAdelicQuotients/SiegelWeilUnitaryConvergent.lean:46–49`); not compared.

`GlobalTheory.Published.DiscreteSeriesCover` — hypothesis at this head (`Development/AbelianVarietyTheory/PublishedTheorems/TwistedTraceFormula/AdmissibleDiscreteSeriesOfHasParam.lean:35–38`); not compared.

`GlobalTheory.Published.HarishChandraModules` — hypothesis at this head (`Development/AbelianVarietyTheory/PublishedTheorems/TwistedTraceFormula/HarishChandraModulesOn.lean:43–44`); not compared.

`GlobalTheory.Published.CuspRapidDecay` — hypothesis at this head (`Development/AbelianVarietyTheory/PublishedTheorems/AutomorphicForms₂/ExistsNormLeHeightPow.lean:28–32`); not compared.

`GlobalTheory.Published.CasselmanWallach` — hypothesis at this head (`Development/AbelianVarietyTheory/PublishedTheorems/AutomorphicForms₂/HasDRepIffHasDerivAt.lean:98–111`); not compared.

`GlobalTheory.Published.DiscreteSeriesClassification` — hypothesis at this head (`Development/AbelianVarietyTheory/PublishedTheorems/DiscreteSeriesUnitary₂/DiscreteSeriesClassificationIff.lean:11–36`); not compared.

**First step to challenge.** Check the construction of the definite-row field after intersecting all its eventual hypotheses. The functional and covolume records must apply to the selected row on that same slot.

[Unit record and exact statement](../../units/T04.md)
