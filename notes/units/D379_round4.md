# D379 · Counting constants from Siegel–Weil

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 40,441 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**Outlined · pending_review.** The convergent unitary Siegel–Weil formula gives counting constants that depend on the family's output list. Their exponent and positive lower bound are fixed before a later test predicate is chosen. The same constants can therefore be used when counting on all points of a family.

## Statement and hypotheses

Under the convergent unitary Siegel-Weil formula, one can choose counting constants as a function of the output list and a positive constant bounded by its c-component, with nonnegative C-component and exponent at least 2(CYL+1). The same choices give the counting estimate for every family and test predicate.

$$
\exists c_{30},\ \exists c_{\rm Ic}>0:\ \forall F,P,\quad C_F\ge0,\quad A_F\ge2(\mathrm{CYL}_F+1),\quad c_F\ge c_{\rm Ic},\quad\operatorname{CountAllPointsClass}(P,F,n_{0,F},A_F,C_F,c_F,cb_F).
$$

[`count_constants_of_siegelWeil` · `CountConstantsOfSiegelWeil.lean:11-24`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/FlagMeasures/CountConstantsOfSiegelWeil.lean#L11-L24)

**Read alongside** [T04 · All 26 large-slot conditions from the open conditions](../../units/T04.md) · [D484 · The spectral link from the tuple-size bound](../../units/D484.md).

## Extract a volume estimate

Start with the convergent unitary Siegel–Weil statement. The volume argument passes through a one-vector compactly supported mean, a compactly supported Siegel mean and then a limit statement for the mean. It uses the latter for the volume step in the counting theorem. This sequence distinguishes the formula assumed by D379 from the uniform family of counting inequalities that D379 must supply. The limiting argument and the conversion of a mean into a compact-dual volume estimate are input calculations for the present outline. [`volumeStep_of_siegelWeil` · `VolumeStepOfSiegelWeil.lean:13-18`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/FlagMeasures/VolumeStepOfSiegelWeil.lean#L13-L18)

## Obtain an entire family indexed by the exponent

At an arbitrary exponent $A$, unbundle the unitary automorphic counting result supplied by the compact-dual volume ratio. It gives a threshold $n_0$, a nonnegative $C_0$, and a points estimate for every larger eligible choice. Both of the small fractions in this estimate are $1/16$. The typed points assertion is filled by passing in the actual group, test, tensors, measures, fundamental domain and count data. This is where uniformity in the data must be available; the numbers for one selected test would not give the packaged theorem. [`count_typed_of_volumeStep` · `CountTypedOfVolumeStep.lean:12-19`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/FlagMeasures/CountTypedOfVolumeStep.lean#L12-L19)

## Read the family exponent from its list

Choose the functions $n_0(A)$ and $C_0(A)$ from the preceding result. At a list $l$, set the exponent equal to twice one plus the entry with zero-based index six, using zero as the default. For a family's own output list that entry is its cylinder parameter. Thus the selected exponent is exactly $2(\mathrm{CYL}+1)$. Fill the counting record using $n_0$ and $C_0$ evaluated at that exponent. Choose both small fractions, and the independent common lower bound, to be $1/16$. The nonnegativity of the large constant is inherited from the uniform count. [`count_constants_of_siegelWeil` · `CountConstantsOfSiegelWeil.lean:11-22`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/FlagMeasures/CountConstantsOfSiegelWeil.lean#L11-L22)

## Specialize last

A test predicate and a family now determine the class of points to count, without altering the earlier record. For each scale and index the class-counting implication converts the typed bound into the requested assertion. Choose the threshold and the large constant at equality in the typed estimate. The final numerical inequalities in the package are immediate. This order of specialization is what allows the spectral-link argument to take one function of output lists as its counting input. [`count_constants_of_siegelWeil` · `CountConstantsOfSiegelWeil.lean:15-24`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/FlagMeasures/CountConstantsOfSiegelWeil.lean#L15-L24)

## Literature-named inputs

`HeckeCharacterZeroLocus.SiegelWeilU.SiegelWeilUnitaryConvergent` — hypothesis at this head (`Formalism/UnipotentAdelicQuotients/SiegelWeilUnitaryConvergent.lean:46–49`); not compared.

`GlobalTheory.CountConstants.count_constants_of_siegelWeil` — in-repo constant (`Development/AbelianVarietyTheory/Proofs/FlagMeasures/CountConstantsOfSiegelWeil.lean:11–24`); not compared.

`GlobalTheory.GaussMean.volumeStep_of_siegelWeil` — in-repo constant (`Development/AbelianVarietyTheory/Proofs/FlagMeasures/VolumeStepOfSiegelWeil.lean:13–18`); not compared.

`GlobalTheory.GaussMean.oneVectorCc_of_siegelWeil` — in-repo constant (`Development/AbelianVarietyTheory/Proofs/FlagMeasures/OneVectorCcOfSiegelWeil.lean:379–426`); not compared.

**First step to challenge.** Check the compact-dual volume-to-count implication at the exponent determined by the output list. The two fixed fractions must survive specialization to the test predicate.

[Unit record and exact statement](../../units/D379.md)
