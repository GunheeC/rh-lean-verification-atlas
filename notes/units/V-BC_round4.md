# V-BC · Conditional base change from finite comparison candidates

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 1,279 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**Outlined · pending_review.** Assume `CandFin`, the finite joint-eigenvalue sets, finite local model lists and common invariant-space bounds for the specified comparison frames of [W16](../../units/W16.md). The conclusion is the definite unitary isobaric base-change assertion of [W02](../../units/W02.md). This note follows the conditional arrow and identifies the other suppliers built into its proof. Thus a reader can check whether a proposed replacement for `CandFin` has the strength this application needs. `baseChangeN_of` (`FillPre.lean:7–9`) `candFin` (`FrameEx.lean:15–17`) `fieldN_of` (`FieldNOf.lean:52–81`)

## Form a frame and run the comparisons

**Frame existence.** Supply the independently constructed unitary-side input and the hypothesized finite candidate data to the frame existence theorem. The proof also uses a local spherical algebra, its spectral trace comparison, inert data, independence of the candidate list, and Hecke and power identities. The hypothesis is consumed at the point where the comparison requires uniform finite candidate information for the frame under consideration. It does not claim all the other ingredients of a frame as consequences of finiteness. `frameEx_of_fin` (`FrameExOfFin.lean:43–48`) `baseChangeN_of` (`FillPre.lean:7–9`)

**Frame bounds and reading.** Adjoin the word bound and frame reading supplied by the source. The joining theorem takes three arguments: frame existence, a frame bound and a frame reading. In its proof these enter the construction of a finite run through the generation theorem; the latter also uses a limiting read rule and a diagonal-algebra input. The result passed to the next stage is one `RunFin` assertion. One must keep the frame tests used by the existence, bound and reading statements compatible. `baseChangeN_of` (`FillPre.lean:7–9`) `bci_of` (`BciOf.lean:22–26`) `fieldN_of_run` (`FullThetaHolds.lean:31–32`)

## Select one candidate for every inert test

Fix the field, positive rank and automorphic representation. For a prescribed set containing at most one split-place test, the finite run gives a family of candidates. Every finite list of inert test places is handled by some member of this one family. Suppose every candidate fails somewhere. For each member choose a failing inert place and collect the choices into a finite set. The finite-list property supplies a member that succeeds on that set, including its own chosen failure. This contradiction gives a candidate satisfying all unramified nonsplit places at once and retaining the initial split test. This is the mathematically informative use of a **finite** candidate list. `RunFin` (`FieldNOf.lean:25–28`) `full_of` (`FieldNOf.lean:37–49`)

**Use a fixed global datum.** Begin with the empty split-test set. The previous choice gives a full datum $D$, so all its inert tests already hold. For a split place $w$, the same argument with the singleton set gives a possibly different $D_w$ satisfying the requested local match. The two full data have the required regularity and cofinite Satake comparison. Local rigidity gives a permutation matching their pieces, and permutation compatibility transfers the local subquotient to $D$. At an unramified nonsplit place the spherical subquotient comes directly from $D$'s own inert property. At the remaining places one uses existence of a local subquotient with the applicable weaker conditions. `fieldN_of` (`FieldNOf.lean:52–81`) `fieldN_of_run` (`FullThetaHolds.lean:31–32`)

These choices supply local components compatible with one partition and its archimedean weights. The passage from finite-intersection tests to a simultaneous inert conclusion above is elementary once `RunFin` is granted. Construction of the finite run, the cofinite Satake comparison and local rigidity remain named mathematical inputs. [Role of the result in V](../../pillars/V.md). `fieldN_of` (`FieldNOf.lean:52–81`) `full_of` (`FieldNOf.lean:37–49`) `bci_of` (`BciOf.lean:22–26`)

The unconditional head and the three final local cases are described separately in [W02](../../units/W02.md). There candidate finiteness comes from `candFin`, while this head receives `hCF` and passes it to `frameEx_of_fin` with `uSide`. `UpperTheory.BaseChangeIdentities.baseChangeN_of` (`Development/AutomorphicArithmetic/Foundations/BaseChangeIdentities/FillPre.lean:7–9`). `UpperTheory.HeckeLevelFrameExistence.candFin` (`Development/AutomorphicArithmetic/Foundations/BaseChangeIdentities/FrameMatching/HeckeEigenvalueFiniteness/FrameEx.lean:15–17`).

**First step to challenge.** Check that the finite family for a fixed split test is selected before the finite set of inert places varies, then check the permutation that transfers a singleton split-place match to the original global datum. `RunFin` (`FieldNOf.lean:25–28`) `full_of` (`FieldNOf.lean:37–49`) `fieldN_of` (`FieldNOf.lean:52–81`)
