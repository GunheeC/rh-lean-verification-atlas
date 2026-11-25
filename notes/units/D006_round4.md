# D006 · Putting local duality and Euler inputs on the specified tie

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 8,424 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**pending_review** · [Unit card](../../units/D006.md) · [Track guide](../../tracks/local/README.md)

Given the Bloch–Kato local, Tate-duality and Euler-characteristic inputs, the local construction returns both torsion assertions on every good set of field data. The first assertion refers to the tie already specified by the Fontaine datum. `GlobalTheory.T.theorem_tb_of_local_blochKato_duality_euler` ([TheoremTbOfLocalBlochKatoDualityEulerStatement.lean:8–9](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/TheoremTbOfLocalBlochKatoDualityEulerStatement.lean#L8-L9)).

## Unpack the local conclusion at a test prime

Fix the three cohomological statements, a host, its Wach data and Fontaine data, and a compatible comparison. To test the conclusion choose a prime $\ell$, two finite extensions $K,LL$, an index $s$, and a proof of the condition called Good for these choices. The first output is TBat for the induced situation and the tie on the indicated component of $F$. The second is TBeAt on the same situation. This joint quantification means that replacing one of the good field extensions after producing the first part changes the object on which the second part is needed. `Formalism.MainNotions.LocalSituation.Conclusion4` ([LocalSituation.lean:590–593](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SharpRestriction/LevelLetterCocycles/LocalSituation.lean#L590-L593)). `GlobalTheory.T.theorem_tb_of_local_blochKato_duality_euler` ([TheoremTbOfLocalBlochKatoDualityEulerStatement.lean:8–9](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/TheoremTbOfLocalBlochKatoDualityEulerStatement.lean#L8-L9)).

## Create the admitted local input

Apply the local Tate-duality and Euler statements to $D,HW,F$. The source chooses ties from local nonemptiness and assembles an admitted input record. Its components include an $H^2$ assertion obtained from duality, the Euler formula itself, filtered quotient data, continuity of the fundamental exact sequence and Fontaine bounds. The first remaining surjectivity clause is produced from a local core and a one-minus-Frobenius assertion. The last clause produces a pair of local comparison and decompletion inputs. The consumer retains the admitted part of the output. The comparison argument of the exported implication stays in its type even though this particular constructor names it with an unused binder. `GlobalTheory.LocInputs.ties_and_inputs_of_duality_euler` ([TiesAndInputsOfDualityEuler.lean:19–34](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/TiesAndInputsOfDualityEuler.lean#L19-L34)). `GlobalTheory.TheoremTBRecords.aux_of_blochKato_tateDuality_eulerChar` ([TheoremTbOfLocalBlochKatoDualityEuler.lean:12–18](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/TheoremTbOfLocalBlochKatoDualityEuler.lean#L12-L18)).

## Supply Bloch–Kato on all tested local fields

The Bloch–Kato input together with duality and Euler gives Conclusion5 for the same host. This quantifies over primes and finite extensions and supplies the Bloch–Kato condition on their local period data. The good-case torsion theorem now takes the admitted record and Conclusion5 and produces Conclusion4. This is the step converting a statement on the period data into the two torsion statements for the chosen good situation. The separate derivations of the admitted record entries and the good-case theorem remain inputs here. [D004](../../units/D004.md) gives the companion inventory for the Wach norm assertions; [T25](../../units/T25.md) records their local-bound setting. `GlobalTheory.T.blochKatoLocal_all_of_tateDuality_eulerChar` ([BlochKatoLocalAllOfTateDualityEulerCharStatement.lean:8–9](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/BlochKatoLocalAllOfTateDualityEulerCharStatement.lean#L8-L9)). `Formalism.MainNotions.LocalSituation.Conclusion5` ([LocalSituation.lean:595–596](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/SharpRestriction/LevelLetterCocycles/LocalSituation.lean#L595-L596)). `GlobalTheory.T.twistedTorsionClassTheorem_goodCase` ([TwistedTorsionClassTheoremGoodCaseStatement.lean:9–10](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/TwistedTorsionClassTheoremGoodCaseStatement.lean#L9-L10)).

In the construction of the ties, the dual filtration is supplied by `TateDualFil.main`. `GlobalTheory.LocInputs.ties_and_inputs_of_duality_euler` (`Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/TiesAndInputsOfDualityEuler.lean:24–31`).

## Literature-named inputs

`GlobalTheory.Published.BlochKatoLocal` — hypothesis at this head (`Development/AbelianVarietyTheory/PublishedTheorems/GaloisCohomology₂/RationalDualityOfAllCoefficients.lean:60–62`); not compared.

`Formalism.GaloisCohomology.LocalTateDualityK` — hypothesis at this head (`Formalism/GaloisCohomology/LocalTateDualityK.lean:47–55`); not compared.

`Formalism.GaloisCohomology.LocalEulerCharK` — hypothesis at this head (`Formalism/GaloisCohomology/LocalTateDualityK.lean:57–61`); not compared.

`GlobalTheory.T.theorem_tb_of_local_blochKato_duality_euler` — in-repo constant (`Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/TheoremTbOfLocalBlochKatoDualityEulerStatement.lean:8–9`); not compared.

`GlobalTheory.TheoremTBRecords.aux_of_blochKato_tateDuality_eulerChar` — in-repo constant (`Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/TheoremTbOfLocalBlochKatoDualityEuler.lean:12–18`); not compared.

`GlobalTheory.T.blochKatoLocal_all_of_tateDuality_eulerChar` — in-repo constant (`Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/BlochKatoLocalAllOfTateDualityEulerCharStatement.lean:8–9`); not compared.

`GlobalTheory.BlochKatoLocalAllOfTateDualityEulerChar₂.aux_of_blochKato_tateDuality_eulerChar₂` — in-repo constant (`Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/BlochKatoLocalAllOfTateDualityEulerChar.lean:10–13`); not compared.

**First step to challenge.** Follow the tie in the first output back to the Fontaine datum at the same prime, fields and index. Existence of an unrelated tie would not give that output.
