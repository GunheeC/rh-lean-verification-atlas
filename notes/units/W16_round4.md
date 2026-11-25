# W16 · Three finiteness statements for a two-block comparison

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 418 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**Outlined · pending_review.** Fix a CM field in the finite-unramified setting, a positive rank, the given automorphic representation, a local reading rule, and its comparison frame. The frame includes an initial set of places, a finite index set of block sizes and the local data for candidate products. Choose an admissible finite auxiliary set $T'$ and the prescribed test data. The problem is to control many candidates simultaneously while the frame and tests stay fixed. The conclusion has three separate finite outputs. This is the hypothesis used by [V-BC](../../units/V-BC.md) and hence by [W02](../../units/W02.md). `candFin` (`FrameEx.lean:15–17`) `candFin_of` (`CandOf.lean:36–40`) `all_parts` (`CandOf.lean:22–34`) `baseChangeN_of` (`FillPre.lean:7–9`)

## First obtain finite lists in each block

For a partition index $i$ write $a_i$ and $n-a_i$ for its two degrees. Apply the level-openness input to the two groups for the actual frame. The reading rule supplies their permitted levels and their compact-type conditions. The strict-finiteness input, applied separately on the left and right with the stated character parameter, supplies two finite lists of model data. A candidate's component conditions and its sum conditions give a model for each side of that candidate. The lists can depend on $i$ and the frame. They are chosen before a particular candidate pair is tested. `candFin_of` (`CandOf.lean:36–40`) `cls_fin` (`ClsFin.lean:31–45`)

## Eigenvalues at auxiliary places

Fix $i$ and $w$. For the finite lists of the two block types, the eigenvalue comparison produces a finite set $Z_{iw}$ of **ordered pairs** of eigenvalue tuples, together with a dimension bound $m_{iw}$. A given candidate's two strict models allow the comparison theorem to place its joint eigenvalue tuple in $Z_{iw}$. Since the index set and $T'$ are finite, the dimension bounds can be combined to give
$$
 m_0=\sup_i\;\sup_{w\in T'}m_{iw}.
$$
The proof takes these suprema in the natural numbers. For a place belonging to $T'$, each relevant $m_{iw}$ is bounded by $m_0$. The bound works simultaneously over all candidates and $w\in T'$ once the frame and auxiliary set are fixed. This step does not ask that the same $m_0$ work after either changes. `part1` (`Imports.lean:21–36`) `all_parts` (`CandOf.lean:22–34`)

## Products at initial places

For $w$ in the initial set the output is a finite list of full local-product models. The strict-join result gives a finite list of joins of the two block models. For any candidate join, choose the resulting strict full product. A second comparison transfers strictness to the relation `Same` at the prescribed subgroup. This relation requires an equivalence for membership of every irreducible subquotient, equality of the two dimensions of the fixed spaces and finite dimensionality of the model fixed space. These three conclusions permit the same model to serve the local tests that the comparison frame actually requests. `part2` (`ImportsAlt.lean:26–38`) `Same` (`ImportsAlt.lean:21–24`)

## Assemble the three conclusions

Combine the finite eigenvalue sets from the first comparison, the finite product list just constructed, and the single dimension bound from the double supremum. The top-level supplier invokes seven inputs: finiteness of strict types, strict product and join, the candidate component conditions, openness of the levels, invariance under isomorphism, and admissibility of the product. Its last step is an application of the three-part theorem with precisely those inputs, so this outline leaves their separate derivations exposed. [Conditional base change](../../units/V-BC.md). `candFin` (`FrameEx.lean:15–17`) `candFin_of` (`CandOf.lean:36–40`) `all_parts` (`CandOf.lean:22–34`)

**Scope of the hypotheses.** The note retains the source’s named predicates and records. For the exact quantified assumptions at this head, read `UpperTheory.HeckeLevelFrameExistence.candFin` (`Development/AutomorphicArithmetic/Foundations/BaseChangeIdentities/FrameMatching/HeckeEigenvalueFiniteness/FrameEx.lean:15–17`). Their internal definitions are separate reading tasks.

**First step to challenge.** In the transfer from two finite block lists to one finite product list, check the actual level subgroup and verify that strict comparison preserves both subquotients and fixed-space dimensions for every candidate. `part2` (`ImportsAlt.lean:26–38`) `Same` (`ImportsAlt.lean:21–24`)
