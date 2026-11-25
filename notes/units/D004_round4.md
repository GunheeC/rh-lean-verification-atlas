# D004 · Reading the Wach norm package by its individual clauses

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 12,168 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**pending_review** · [Unit card](../../units/D004.md) · [Track guide](../../tracks/local/README.md)

A fixed local Wach datum, its Fontaine data and a compatible comparison determine a whole collection of lattice and cohomological assertions. This unit gathers them on the same input so later estimates can select the clauses they need. `GlobalTheory.T.wachLattice_laterClauses_hold` ([WachLatticeLaterClausesHoldStatement.lean:8–9](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/WachLatticeLaterClausesHoldStatement.lean#L8-L9)).

## Write the dependent inputs in order

Fix the host $D$, then Wach data $HW$ for its local theory, Fontaine data $F$ for that particular $HW$, and finally comparison data $C_m$ for all three. The conclusion is a nested conjunction. It contains global freeness, predicates P2 through P9, a characterization of the Wach lattice, a semisimple quotient condition, Pr2a through Pr2d, a third lemma and Conclusion E. The comparison datum occurs in the types of particular conjuncts. Erasing it globally because some clauses do not mention it would change the question. The local family applications, including [T25](../../units/T25.md), need propositions about a single compatible choice. `GlobalTheory.T.wachLattice_laterClauses_hold` ([WachLatticeLaterClausesHoldStatement.lean:8–9](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/WachLatticeLaterClausesHoldStatement.lean#L8-L9)). `Formalism.MainNotions.DeltaInvariantLattices.DeltaInvariantNormBound` ([UsedLocalConclusion.lean:9–13](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SharpRestriction/LevelLetterCocycles/UsedLocalConclusion.lean#L9-L13)).

## Trace the Wach block

Unfolding the conjunction in order gives a useful checklist. The freeness witness uses $D,HW,F$. The trivial-mod-uniformizer and crystalline-comparison suppliers take $C_m$ as well. For the next group the source calls the low-level expansion, height from Hodge jumps, saturated exactness, cocycle-pole, P8 and tame-descent theorems. Compare the actual arguments at each call. For example, the P8 supplier takes comparison data even though the P8 predicate in the assembled conjunction has no explicit comparison argument. The distinction is between what the result states and what its constructor needs. `GlobalTheory.NL.wach_used_clauses` ([WachLatticeLaterClausesHold.lean:28–38](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/WachLatticeLaterClausesHold.lean#L28-L38)). `Formalism.MainNotions.DeltaInvariantLattices.DeltaInvariantNormBound` ([UsedLocalConclusion.lean:9–13](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SharpRestriction/LevelLetterCocycles/UsedLocalConclusion.lean#L9-L13)).

## Trace the cohomology block and the last pair

After the characterization and the semisimple quotient, the constructors use the Herr first-cohomology description, the finite-condition restriction test, the finite cocycle-class result, and a second-cohomology torsion kernel. The next component is the crystalline-surjection cokernel killed by a power of the lattice variable. Finally the source opens Conclusion E and pairs a Nygaard-extension statement with the local-comparison result. This last use again takes the same $C_m$. The assembly itself consists of placing these proofs into their corresponding fields; each individual bound or exactness statement retains its own proof obligation. For comparison with another local use of these data see [D006](../../units/D006.md). `GlobalTheory.NL.wach_used_clauses` ([WachLatticeLaterClausesHold.lean:28–38](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/WachLatticeLaterClausesHold.lean#L28-L38)).

**Scope of the hypotheses.** The note retains the source’s named predicates and records. For the exact quantified assumptions at this head, read `GlobalTheory.T.wachLattice_laterClauses_hold` (`Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/WachLatticeLaterClausesHoldStatement.lean:8–9`). Their internal definitions are separate reading tasks.

**First step to challenge.** Trace the passage from a rational crystalline comparison to the specific integral cokernel clause. The last constructor requires an explicit power of the lattice parameter killing the cokernel.
