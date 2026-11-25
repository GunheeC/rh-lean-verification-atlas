# D484 · The spectral link from the tuple-size bound

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 1,314 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**Outlined · pending_review.** A tuple-size estimate implies the spectral-link inequalities with constant three on the specified family class. The implication also needs the chosen spectral rows, their local ties, counting, volume and main-term estimates.

## Statement and hypotheses

For the supplied spectral and real-family selections, decay and transport data, type and volume records, uniform constant c30 and large-scale hypotheses, the tuple-size bound implies the spectral link with C0=3 on D3(3,A). This controls off-diagonal Hilbert–Schmidt norms, diagonal deviation and total dimension under the prescribed dimension-ratio window.

$$
\mathrm{TuSize}(F)\ \Longrightarrow\ \mathrm{LinkS}(F,3).
$$

[`link_alt_alt_bis` · `LinkAltAltBis.lean:16-48`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkAltAltBis.lean#L16-L48)

**Read alongside** [D033 · Uniform row bounds from convergent Siegel–Weil](../../units/D033.md) · [D379 · Counting constants from Siegel–Weil](../../units/D379.md) · [B05 · Connected families from Green and the closed link](../../units/B05.md).

## Fix the selected rows and their constants

Start with a twist selection on the family class and a spectral condition for that selection. Restrict to the stated enriched class, with frame bound, decay, row finite-dimensionality, row type, nongeneric estimate, main term, loop and selected spectral estimates. The counting function depends on the output list and satisfies its given exponent and nonnegativity conditions. At each later index require volume-sign independence and the class items at the specified rank. These are inputs even though the last displayed arrow itself says only that the tuple-size estimate implies a spectral link. [`link_alt_alt_bis` · `LinkAltAltBis.lean:16-34`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkAltAltBis.lean#L16-L34)

## Construct the instance tie

Specialize the spectral constant to three and take the universally available residual-evaluation condition. Restrict the original selection by the projection from the enriched class. Its threshold is unchanged, and its later ties come from the given spectral record. At each selected row use the local tie, the instance field, the real tie from the original twist, volume-sign and class data, and the family scale tie. These supply the instance tie and the lower bound of one on the local quantity required by transport. This is where two superficially compatible selections would fail to compose if they did not pick the same row. [`link_alt_alt_bis` · `LinkAltAltBis.lean:35-47`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkAltAltBis.lean#L35-L47)

## Transport the estimates through concrete rows

Finite dimensionality and decay supply finite row data. The selection and frame estimate give valid selections and hence concrete evaluation. For every sufficiently large scale construct the tied automorphic row from the selected record at that very scale and index, using the instance tie and local lower bound. The selection threshold is the eventual threshold used in this construction. No fresh extremizing row is chosen for the purpose of the estimate. [`theoremS_transport_link_zero` · `LinkSPos.lean:131-157`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/LinkSPos.lean#L131-L157)

## Combine diagonal and nondiagonal estimates

The concrete spectral-link theorem combines evaluation and selected off-diagonal estimates with diagonal positivity. In the diagonal terms the row type and the pair consisting of nongeneric bound and main-term identity are used at different stages. The counting bound is passed on the same family, with the same function of output lists. This gives the required closed implication at constant three. The final specialization is routine; the interface between the numerical row estimates and the tied automorphic row is where the information about the actual selection enters. [`theoremS_transport_link_zero` · `LinkSPos.lean:158-161`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/LocalToGlobal/SiegelLatticeTheory/FlagStabilizerTensors/LinkSPos.lean#L158-L161) · [`link_alt_alt_bis` · `LinkAltAltBis.lean:41-48`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkAltAltBis.lean#L41-L48)

**Scope of the hypotheses.** The note retains the source’s named predicates and records. For the exact quantified assumptions at this head, read `GlobalTheory.Top.link_alt_alt_bis` (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/LinkAltAltBis.lean:16–48`). Their internal definitions are separate reading tasks.

**First step to challenge.** Verify that the real volume, class data and spectral instance refer to the row picked by the original selection at that family index.

[Unit record and exact statement](../../units/D484.md)
