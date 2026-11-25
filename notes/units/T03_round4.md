# T03 · Building the definite-side family from unramified row data

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 1,232,133 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**Outlined · pending_review.** A definite-side witness can be assembled if rational rows, an eventually available retwisting grid and three linked bounds are supplied. The small-prime bound begins on the dependence parameters. The functional and covolume bounds already live on the stronger extension.

## Statement and hypotheses

Assume $P$ and row rationality: every datum in the starting row test with the
prescribed group, geometric, weight and residue-characteristic conditions passes
the rational row test. Fix a proof $h$ of `RecTExists`, $c\in\mathbb R$, and an
eventually large retwisting predicate $A$. Suppose the small-prime norm bound
is linked at $p(c)$, and the functional inequality of T10 and covolume
inequality of T13 are linked in their row versions at $p_A(c)$.
Then the definite-side family, selection and certificates of T02 exist.
The two types of parameter have distinct roles in this implication. [`hypotheses_nonempty_of_unramified_exponents_alt` · `HypothesesNonemptyOfUnramifiedExponents.lean:41-61`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/HypothesesNonemptyOfUnramifiedExponents.lean#L41-L61)

**Read alongside** [T06 · Lattice masses, automorphic membership and existence of linked bundles](../../units/T06.md) · [T08 · The twelve linked conditions at dependence parameters](../../units/T08.md) · [T04 · All 26 large-slot conditions from the open conditions](../../units/T04.md) · [T05 · Two uniform bounds on indefinite rows](../../units/T05.md) · [T13 · Arithmetic inputs for the covolume bound](../../units/T13.md).

## Keep the two parameter spaces separate

Fix the proof of reciprocity existence, dependence parameter and retwisting predicate. The last must be eventually available. The extension is constructed with this predicate, the indicated origin, no extra series extension and the closure of unrestricted geometry. The small-prime estimate starts at the original dependence point. The functional and third-place-series covolume conditions refer directly to the constructed extension. First use row rationality and the unitary hypothesis to obtain the mass ratio, membership and bundle existence. The geometric Galois inputs supply the third-layer records, while the unitary input supplies surjectivity and the lower bound. [`hypotheses_nonempty_of_unramified_exponents_alt` · `HypothesesNonemptyOfUnramifiedExponents.lean:41-48`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/HypothesesNonemptyOfUnramifiedExponents.lean#L41-L48)

## Strengthen a linked norm estimate

Use local finiteness, local Tate duality, the Euler-characteristic input, depth-zero support and the small-prime estimate with the proof of `RecTExists`. This yields the required preliminary norm rows. The projection from data on the stronger extension to the earlier extension exhibits nonemptiness of the latter. Apply the two consequences of extension monotonicity separately: one transports the open conditions, and one transports the norm rows after specializing the family predicate. This is the delicate compatibility step. It is also the reason the proof cannot simply hand the original small-prime estimate to the last constructor. [`hypotheses_nonempty_of_unramified_exponents_alt` · `HypothesesNonemptyOfUnramifiedExponents.lean:44-53`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/HypothesesNonemptyOfUnramifiedExponents.lean#L44-L53)

## Build the rows and assemble

Now all four row inputs refer to the strengthened extension: the transported open data, the supplied covolume and functional statements, and the new norm rows. Apply the all-row theorem using global Artin reciprocity, the convergent Siegel–Weil input, the listed discrete-series and harmonic-analysis assumptions, and both surjectivity/lower-bound outputs. What remains is a constructor for nonemptiness. Its independent inputs include thin-scale estimates, decay, finite dimensionality, the type and main-term/row-error assertions, and the volume and mass constants. Supply those with the earlier mass, membership and bundle data and the all-row record. This packages compatible data for one definite-side witness. [`hypotheses_nonempty_of_unramified_exponents_alt` · `HypothesesNonemptyOfUnramifiedExponents.lean:54-61`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/HypothesesNonemptyOfUnramifiedExponents.lean#L54-L61)

## Extent of this outline

The mass and membership branch has its own substantial input on rational weights, saturated weight one and a nonempty Weil block. The present implication uses its three conclusions. A specialist tracing existence can isolate that branch from the independent problem of transporting norms and obtaining the covolume estimate. The construction retains all three branches as conditions when read in this direction. [`hypotheses_nonempty_of_unramified_exponents_alt` · `HypothesesNonemptyOfUnramifiedExponents.lean:43-48`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/HypothesesNonemptyOfUnramifiedExponents.lean#L43-L48) · [`member_bundles_large_unramified_exponents_alt` · `MemberBundlesLargeUnramifiedExponents.lean:54-63`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/MemberBundlesLargeUnramifiedExponents.lean#L54-L63)

The parameter `hL` is a proof of the existence statement `RecTExists`. Its local witness is under an existential quantifier. `UpperTheory.Zero.LLC.RecTExists` (`Development/AutomorphicArithmetic/Foundations/LocalLanglands/IsRecTOfIsRec.lean:78–80`). `GlobalTheory.Fc.S0.StageU.hypotheses_nonempty_of_unramified_exponents_alt` (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/HypothesesNonemptyOfUnramifiedExponents.lean:41–61`).

**Scope of the hypotheses.** The note retains the source’s named predicates and records. For the exact quantified assumptions at this head, read `GlobalTheory.Fc.S0.StageU.hypotheses_nonempty_of_unramified_exponents_alt` (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/HypothesesNonemptyOfUnramifiedExponents.lean:41–61`). Their internal definitions are separate reading tasks.

## Literature-named inputs

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.localTateDuality` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:81`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.globalArtinReciprocity` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:46`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.siegelWeilUnitaryConvergent2` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:64`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.discreteSeriesCover` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:57`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.harishChandraModules` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:58`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.cuspRapidDecay` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:31`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.casselmanWallach` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:59`); not compared.

`GlobalTheory.Fc.S0.UnitaryGroupThirdPlaceHypotheses.discreteSeriesClassification` — record field (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/BernsteinUnitaryProductIrreducible.lean:62`); not compared.

`GlobalTheory.rowNGP_of_siegelWeil` — in-repo constant (`Development/AbelianVarietyTheory/Proofs/FlagMeasures/RowPositivityOfSiegelWeil.lean:10–15`); not compared.

`GlobalTheory.rowMainEqP_of_siegelWeil` — in-repo constant (`Development/AbelianVarietyTheory/Proofs/FlagMeasures/RowMainEqPOfSiegelWeil.lean:10–16`); not compared.

**First step to challenge.** Check that the reciprocity and norm bound survives strengthening the extension and has the exact norm predicate used by the all-row theorem.

[Unit record and exact statement](../../units/T03.md)
