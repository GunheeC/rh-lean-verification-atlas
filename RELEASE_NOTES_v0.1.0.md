# RH Lean Verification Atlas · v0.1.0

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

This atlas groups statements and implications from the pinned Lean development into 217 reading units. It contains 55 Full arguments under stated inputs, 127 outlines and 35 statement-only entries. The 182 written units have 739 active steps. [Reading orders](docs/reading-orders.md) · [Progress](PROGRESS.md)

**Evidence.** A third-party audit reports kernel acceptance of the formal development. The atlas records edition-matched AI reviews of 20 written units and step-specific AI review of 6 active steps. Human-checked steps: 0. The conditional argument assumes the Selmer window V, a common definite-side witness F, Green’s input and 31 local implications. The hypothesis table in paper v7 lists the supplementary inputs used in the deduction. The Lean source supplies both V and F. No human-readable derivation of either is available in the atlas. [Open questions](questions/README.md) · [Assumptions and scope](OVERVIEW.md)

**Editions.** The repository snapshot and its convenience attachments contain the same two PDFs. Gunhee Cho’s paper follows the conditional argument from its inputs to its conclusions. The companion blueprint explains the 20 original inputs. The atlas records the sources and the checks on each step across editions.

| Repository PDF | Physical pages | SHA-256 |
|---|---:|---|
| [Toward a human verification of Alpöge’s Lean proof of the Riemann hypothesis, I: the conditional chain from Selmer windows to zero-free regions](editions/v0.1.0/paper_v7.pdf) · v7 | 432 | `9ea2256176c7b28156a683dee9c4ad76138777246811ce99aca14eb1ec015b9d` |
| [The Alpöge formalization of RH and GRH: an informal blueprint](editions/v0.1.0/blueprint_v13b.pdf) · v13b | 955 | `6108e2468ad4284ca3012dd7f91cfd983b7d791809c0f6b523eb8b53f5bb211e` |

The new [Section 2, *The proof at a glance*](editions/v0.1.0/paper_v7.pdf#page=5) explains the argument for nonspecialists on printed pp. 5–8. It awaits independent review. The theorem, lemma, proposition and proof environments of paper v7 have the same mathematical text as v6. The new prose and the earlier mathematical arguments were drafted with AI assistance. No independent human referee has checked them. [Read the guide](docs/proof-at-a-glance.md) · [Korean guide](docs/ko/proof-at-a-glance.md)

The new [Section 3, *Scope, coverage and the verification programme*](editions/v0.1.0/paper_v7.pdf#page=9) covers printed pp. 9–22. It separates index placement from direct citations, identifies the available reading tasks and records open inputs. Its new prose awaits independent review. [Coverage and verification tasks](docs/coverage.md) · [Korean coverage guide](docs/ko/coverage.md)

Paper v7 · [conditional theorem, printed p. 2](editions/v0.1.0/paper_v7.pdf#page=2) · [hypothesis table, printed pp. 51–52](editions/v0.1.0/paper_v7.pdf#page=51) · [closing deduction, printed pp. 52–53](editions/v0.1.0/paper_v7.pdf#page=52). Blueprint v13b preserves the 944 original sheet positions after its 11 new front sheets. A Korean disclaimer was removed from original sheets 1 and 2 (v13b physical pages 12 and 13). Extracted text, decoded content streams and renders agree on original sheets 3–944. The packet index retains the original printed folios. Reviews remain attached to the editions examined. [Packet index](notes/README.md) · [Sheet comparison](data/blueprint_v13b_page_comparison.json) · [Edition register](data/editions.json) · [PDF checksums](editions/v0.1.0/SHA256SUMS)

**Citation.** *RH Lean Verification Atlas (AI-drafted; maintained by Gunhee Cho)*, v0.1.0 (2026). Cite the Git commit selected by tag `v0.1.0`, the unit and step IDs, and the PDF digest where relevant. The release entry supplies the full Git hash. [Citation metadata](CITATION.cff) · [Attribution](AUTHORS.md)
