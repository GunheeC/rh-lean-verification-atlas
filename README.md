# RH Lean Verification Atlas

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

Levent Alpöge’s Lean development states the Riemann hypothesis for zeta and four further assertions about zeros of zeta or Dirichlet L-functions. A third-party audit records kernel acceptance, and this project did not reproduce that run. The written deduction assumes V, F, Green’s finite-field character input, 31 local implications and supplementary inputs S1–S6, including the Mathlib facts in S6. The Lean repository supplies terms for V and F. Their two disjoint regions account for 47.73% of the measured core lines. The atlas provides reading maps for both, and a complete hand derivation of either input remains open. [MainConclusion.lean:10–11](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/CharacterBoxes/MainConclusion.lean#L10-L11) · [RowSrc.lean:6–6](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/Foundations/GaloisRepresentations/IntegralStructures/RowSrc.lean#L6-L6) · [EveryCharacterOfLiteratureOfVWin.lean:810–813](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/EveryCharacterOfLiteratureOfVWin.lean#L810-L813)

[What is covered, what is not, what you can check](docs/coverage.md) · [Five formal statements](sources/lean-goals.md) · [External audit](sources/kernel-audit.md) · [V and its quantifiers](pillars/V.md) · [F and its common selection](pillars/F.md) · [한국어](README.ko.md)

## The documents

Gunhee Cho’s paper, *Toward a human verification of Alpöge's Lean proof of the Riemann hypothesis, I: the conditional chain from Selmer windows to zero-free regions*, maps 775 Lean statements and outlines the conditional deduction from Selmer windows to zero-free regions. It writes out selected steps in full. The companion blueprint builds up the 20 original inputs from definitions and lemmas. With each edition, the atlas links steps in both documents to Lean declarations and review records so readers can check them by hand. AI systems drafted the texts under Gunhee Cho’s direction and cross-checked passages against the Lean source. No human, the author included, has yet checked the arguments. [Paper v8](editions/v0.1.0/paper_v8.pdf) · [The Alpöge formalization of RH and GRH: an informal blueprint (Blueprint v13c)](editions/v0.1.0/blueprint_v13c.pdf) · [Editions and fingerprints](data/editions.json)

Pick a statement from Levent Alpöge’s Lean development. A reading unit covers one claim or several related claims. It lists their hypotheses and Lean declarations. It links to a written argument when one is available. A recorded review identifies the text and the claim it examined. The external kernel audit concerns the compiled Lean development. [Reading progress](PROGRESS.md) · [Next units and human reading queue](ROADMAP.md) · [Contributors](AUTHORS.md)

> **Writing and review** · [Evidence and limits](STATUS.md) · [Progress over time](PROGRESS.md)  
> Of 217 units, 55 give full arguments under their stated inputs, 127 give outlines and 35 give statements only.  
> 24 units hold L2 for an AI review of a written argument. Of 739 current steps, 6 have an AI review identifying that specific inference.  
> Named readers have checked 0 current steps. 0 units have named checks for all steps and the statement comparison. [Reader queue](ROADMAP.md)

## Choose your entry

| If you came here to… | Open |
|---|---|
| New here? | [Start with the proof at a glance](docs/proof-at-a-glance.md) |
| Understand the claim and what has been checked | [Verification status](STATUS.md) · [Mathematical overview](OVERVIEW.md) · [Frequently asked questions](FAQ.md) |
| See where the written derivation of the two main assumptions stops | [V · Selmer window](pillars/V.md) · [F · definite-side witness](pillars/F.md) |
| Choose a reading route and see its length | [Reading orders](docs/reading-orders.md) |
| Check something in your field | [Analytic number theory](tracks/analytic/README.md) · [Arakelov geometry and geometry of numbers](tracks/arakelov/README.md) · [Theta correspondence and automorphic representations of unitary groups](tracks/theta/README.md) · [Galois representations, automorphy lifting, Iwasawa theory and Euler systems](tracks/galois/README.md) · [Local p-adic theory](tracks/local/README.md) · [Algebraic K-theory and cohomology of arithmetic groups](tracks/ktheory/README.md) · [Formalization and reproducibility](tracks/formal/README.md) |
| Read a graduate-level argument with its prerequisites | [Choose a 6–8 page packet](notes/README.md) · [Start with a one-sided prime-sum window](notes/analytic/README.md) |
| Resolve a Lean name you already have | [Declaration lookup](lookup/declarations.md) · [Glossary](lookup/glossary.md) |
| Compare the public reading and checking projects | [Public landscape](LANDSCAPE.md) · [Statement and name crosswalks](crosswalk/README.md) |
| Report a problem or record a check | [Contribution forms and evidence](CONTRIBUTING.md) · [Named-reader form](signoffs/TEMPLATE.md) |

The [proof map](MAP.md) connects the five goals to their inputs in three views. Use the [dashboard](dashboard/README.md) to find a unit by its written coverage or review grade.

To browse a downloaded copy, open `site/index.html`. Its declaration search and diagrams work from disk.

<!-- roadmap:volunteers:start -->
### Ten short checklists awaiting readers

Sorted by steps, note length and prerequisites. [Full volunteer queue and writing plan](ROADMAP.md)

1. [D549 · The omitted-frequency correction](units/D549.check.md) · 2 steps · 1 pp.
2. [D550 · A common scale for logarithms and fixed constants](units/D550.check.md) · 2 steps · 1 pp.
3. [V-OPEN · The polarized row in the open-image condition](units/V-OPEN.check.md) · 2 steps · 3 pp.
4. [P014 · Nonvanishing for arbitrary characters from Green, the Selmer window and the family witness](units/P014.check.md) · 2 steps
5. [T14 · An averaged slope bound over deep components](units/T14.check.md) · 2 steps
6. [Z1.3.06 · Compatibility of the local and global cocycles](units/Z1.3.06.check.md) · 2 steps
7. [P016 · Zero-freeness from host existence and connectedness](units/P016.check.md) · 2 steps
8. [Z1.3.07 · Failure of the local Greenberg condition](units/Z1.3.07.check.md) · 2 steps
9. [B05 · Connected families from Green and the closed link](units/B05.check.md) · 2 steps
10. [T02 · A common definite-side witness](units/T02.check.md) · 2 steps

<!-- roadmap:volunteers:end -->

## Seven tracks

| Field | A first question | Starter unit |
|---|---|---|
| [Analytic number theory](tracks/analytic/README.md) | What window estimate excludes a pole? | [P022](units/P022.md) |
| [Arakelov geometry and geometry of numbers](tracks/arakelov/README.md) | Where does the discriminant enter a covolume? | [P049](units/P049.md) |
| [Theta correspondence and automorphic representations of unitary groups](tracks/theta/README.md) | Which integral lattices are dual in the Fock model? | [Z4.4](units/Z4.4.md) |
| [Galois representations, automorphy lifting, Iwasawa theory and Euler systems](tracks/galois/README.md) | How do the two Selmer length bounds combine? | [P020](units/P020.md) |
| [Local p-adic theory](tracks/local/README.md) | Which inert-prime estimate controls a row of the table? | [P045](units/P045.md) |
| [Algebraic K-theory and cohomology of arithmetic groups](tracks/ktheory/README.md) | Where does the exponent loss enter the finite count? | [P036](units/P036.md) |
| [Formalization and reproducibility](tracks/formal/README.md) | How do I check the identity of a public declaration? | [P001](units/P001.md) |

## Evidence levels

| Highest recorded level | What a reader can inspect | Units |
|---|---|---:|
| L0 | Declaration pinned; no review of this unit | 138 |
| L1 | Statement and assumptions compared with a pinned declaration | 55 |
| L2 | A written argument under its stated inputs passed the recorded AI cross-review | 24 |
| L3 | Matching evidence from at least two independent sources | 0 |
| L4 | Full argument with a derivation beyond an appeal to an input. Named current checks cover all steps and the statement comparison | 0 |

“Full” means the argument is written under the assumptions shown on its page. An outline still has intermediate reasoning to supply. A statement-only unit gives the claim and its source. Each grade records the evidence for that unit. The dashboard keeps AI review, independent corroboration and human checks in separate columns. These evidence levels are not cumulative prerequisites. L4 concerns the local written argument under its stated inputs. It gives no conclusion about V, F or RH. For each L4, read the number of readers, whether one is the maintainer and their declared AI assistance. Substantial assistance does not qualify as independent human reading. A second reader other than the maintainer or a text revision that supersedes the target can close a dispute. Reader names are self-declared and the repository does not verify identity. [Grade evidence](reviews/README.md) · [Named-check rules](signoffs/README.md)

## Who maintains this

Gunhee Cho maintains the atlas. His affiliations are the Department of Mathematics, Texas State University (`wvx17@txstate.edu`), and TranscendQ (`geonhee@transcendq.com`).
The views and any errors are the author's. [Author and background reading](AUTHORS.md)

Building on continuing discussions in the [EnjoyingMath](https://www.youtube.com/@enjoyingmath9346) channel community, Cho aims to work with mathematics students and mathematicians to check Alpöge’s Lean proof by hand, one step at a time. He intends to pursue that work for as long as it takes. He plans to publish progress updates in English and Korean through atlas editions, the progress dashboard and the channel. The atlas currently records zero human checks. [Progress](PROGRESS.md)

## How to cite

Gunhee Cho (maintainer), *RH Lean Verification Atlas*, v0.1.0, 25 November 2026. AI-drafted; maintained by Gunhee Cho. Give the exact atlas commit, unit ID and Lean declaration. When relying on an exposition, include its edition and pages. The DOI for this release will appear here after Zenodo assigns it. [Citation metadata](CITATION.cff) · [Edition hashes](data/editions.json) · [Release notes](RELEASE_NOTES_v0.1.0.md)

## How to contribute a check

Choose one unit. Identify the edition and exact inference you read, then record your verdict and any reservations. Partial checks, counterexamples and unresolved questions each have a place. [Contribution guide](CONTRIBUTING.md) · [Open questions](questions/README.md)

## License

Copyright © 2026 Gunhee Cho to the extent copyright subsists in AI-generated text. Original atlas writing and data are licensed under CC BY 4.0. Original scripts and workflow code are licensed under the MIT License. The grant excludes material derived from the Lean source and other third-party work. See the source register for the pinned repository’s licence record. [Pinned Lean licence record](sources/README.md) · [License scope](LICENSE) · [MIT License](LICENSE-MIT) · [Third-party notice](NOTICE.md)
