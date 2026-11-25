# T19 · Resolution over a characteristic-zero field

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 35 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**Outlined · pending_review.** Resolution is used in a form that keeps the original smooth locus and controls the inverse image of its complement. This note traces how a functorial resolution supplies those properties and how its tower of blowups becomes a single composite in the target statement.

## Claim and hypotheses

For every characteristic-zero field $k$
and reduced separated finite-type $k$-scheme $X$, there is a sequence of
blowups $f:X'\to X$ with $X'$ smooth. Its restriction over the smooth
locus is an isomorphism. The reduced inverse image of the complement
is a simple normal crossings divisor. The formal wrapper uses a closed
resolution term independently of its record argument.

[`UpperTheory.LiteratureTheorems.resolution_char_zero_of_literature` · `EveryCharacterOfLiteratureOfVWin.lean:557–558`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean#L557-L558)

## What the wrapper really consumes

The outer declaration accepts an open-literature record. Its body names a resolution supplier directly, independently of this argument. That supplier invokes a functorial characteristic-zero resolution at the relevant universe. Its adapter extracts a rule $R$ and the proof that the selected resolution data satisfy the required conditions. The original morphism, its characteristic-zero field, reducedness and geometric finiteness assumptions stay in the scope of the rule. No bibliographic identification follows just from the name of the outer wrapper. [`UpperTheory.LiteratureTheorems.resolution_char_zero_of_literature` · `EveryCharacterOfLiteratureOfVWin.lean:557–558`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean#L557-L558) [`PositivityTheory.Resplug.ResolutionBlowup.resolutionCharZero` · `ResolutionCharZero.lean:6–7`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/ResolutionCharZero/ResolutionCharZero.lean#L6-L7) [`PositivityTheory.Resplug.ResolutionBlowup.resolutionCharZero_of_top` · `ResolutionCharZeroOfTop.lean:40–46`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/ResolutionCharZero/ResolutionCharZeroOfTop.lean#L40-L46)

## Start the induction even for a tower of length zero

The initial object of the tower is isomorphic to the original scheme. Consequently its structural map is the chosen isomorphism, which in the target formulation needs a blowup witness. Take the unit ideal. For a map into the original scheme, composing with the inverse isomorphism gives its unique factorization through this blowup. The pullback unit ideal has the local unit generator. This lets the base case fit the target constructor for one blowup even when the original tower has zero nontrivial stages. [`PositivityTheory.Resplug.ResolutionBlowup.blowup_top_of_iso` · `ResolutionCharZeroOfTop.lean:13–19`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/ResolutionCharZero/ResolutionCharZeroOfTop.lean#L13-L19) [`PositivityTheory.Resplug.ResolutionBlowup.structMap_zero` · `ResolutionCharZeroOfTop.lean:21–23`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/ResolutionCharZero/ResolutionCharZeroOfTop.lean#L21-L23)

## Compose one actual blowup at each successor

At stage $i+1$, the bound $i+1\leq\text{length}$ puts $i$ strictly below the terminal index. The structural map to the original scheme factors as the downward map at that index followed by the previous structural map. Apply the step constructor with the actual center recorded at $i$, the proof that the downward map is its blowup, and the induction hypothesis on the previous composite. This establishes the blowup-sequence predicate for all admissible stages, including the terminal one. [`PositivityTheory.Resplug.ResolutionBlowup.isBlowupSeq_structMap` · `ResolutionCharZeroOfTop.lean:25–34`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/ResolutionCharZero/ResolutionCharZeroOfTop.lean#L25-L34) [`PositivityTheory.Resplug.ResolutionBlowup.isBlowupSeq_topMap` · `ResolutionCharZeroOfTop.lean:36–38`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/ResolutionCharZero/ResolutionCharZeroOfTop.lean#L36-L38)

## Recover the three geometric conclusions from one tower

Specialize $R$ to the given $k$-scheme and structural morphism. The selected terminal object and top map now carry four pieces of evidence: the composite blowup proof just constructed, terminal smoothness, the isomorphism over the smooth locus, and the normal-crossings condition on the indicated reduced inverse image. They belong to a single choice of tower. The transfer of evidence into the target tuple is routine. Construction and termination of the functorial resolution used as input are outside this outline. [`PositivityTheory.Resplug.ResolutionBlowup.resolutionCharZero_of_top` · `ResolutionCharZeroOfTop.lean:40–46`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/ResolutionCharZero/ResolutionCharZeroOfTop.lean#L40-L46)

## First step to challenge

Check the terminal resolution data for the reduced inverse image of the exceptional locus; recording smoothness of the resolved scheme alone loses that divisor condition.

The related input [T20](../../units/T20.md) starts with a smooth scheme and principalizes an ideal with a prescribed boundary. The two statements have different outputs.

The Lean head takes the open-literature record and does not use it. `UpperTheory.LiteratureTheorems.resolution_char_zero_of_literature` (`Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean:557–558`).

## Literature-named inputs

`PositivityTheory.Resplug.ResolutionBlowup.resolutionCharZero` — in-repo constant (`Development/WeilBound/CoreStatements/ResolutionCharZero/ResolutionCharZero.lean:6–7`); not compared.
