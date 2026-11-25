# RH Lean Verification Atlas · v0.1.0

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

This atlas groups statements and implications from the pinned Lean development into 217 reading units. It contains 55 Full arguments under stated inputs, 127 outlines and 35 statement-only entries. The 182 written units have 739 active steps. [Reading orders](docs/reading-orders.md) · [Progress](PROGRESS.md)

**Evidence.** A third-party audit reports kernel acceptance of the formal development. The atlas records edition-matched AI reviews of 20 written units and step-specific AI review of 6 active steps. Human-checked steps: 0. The conditional argument assumes the Selmer window V, a common definite-side witness F, Green’s input and 31 local implications. The hypothesis table in paper v8 lists the supplementary inputs used in the deduction. The Lean source supplies both V and F. No human-readable derivation of either is available in the atlas. [Open questions](questions/README.md) · [Assumptions and scope](OVERVIEW.md)

**Editions.** Gunhee Cho’s paper states a conditional theorem and outlines its deduction within Levent Alpöge’s formal development. The companion blueprint works through 20 original inputs. AI systems helped draft the texts. No human, the author included, has yet checked the arguments.

| Repository PDF | Physical pages | SHA-256 |
|---|---:|---|
| [Toward a human verification of Alpöge’s Lean proof of the Riemann hypothesis, I: the conditional chain from Selmer windows to zero-free regions](editions/v0.1.0/paper_v8.pdf) · v8 | 432 | `3f920d59446741c0ce2a81252525336e5831c95a315879d4b410b86234726bd1` |
| [The Alpöge formalization of RH and GRH: an informal blueprint](editions/v0.1.0/blueprint_v13c.pdf) · v13c | 955 | `834038cc53f42f9254c075238d3a154592d356c34ba5afe78e7a1da2ccf70b82` |

Paper v8 introduces the author and the project, rewrites the abstract and introduction, and revises [Section 2, *The proof at a glance*](editions/v0.1.0/paper_v8.pdf#page=5) on printed pp. 5–8. The eight steps distinguish the conditional deduction from the two major inputs that still need written derivations. The 111 theorem, lemma, proposition and proof environments retain their exact mathematical text from v7. [English guide](docs/proof-at-a-glance.md) · [Korean guide](docs/ko/proof-at-a-glance.md)

[Section 3, *Scope, coverage and the verification programme*](editions/v0.1.0/paper_v8.pdf#page=9) occupies printed pp. 9–22. Its tables distinguish locations in the index from lines cited by written steps. The 20 tasks state what each check would establish. [Coverage and verification tasks](docs/coverage.md) · [Korean coverage guide](docs/ko/coverage.md)

Paper v8 · [conditional theorem, printed p. 2](editions/v0.1.0/paper_v8.pdf#page=2) · [hypothesis table, printed pp. 51–52](editions/v0.1.0/paper_v8.pdf#page=51) · [closing deduction, printed pp. 52–53](editions/v0.1.0/paper_v8.pdf#page=52). Blueprint v13c updates the editor and project information and explains that AI systems drafted and graded the 55 specialist reading units. The front matter also distinguishes the questions a reader can check from the earlier AI grades. The 11 introductory sheets precede the 944 original sheet positions. Those 944 sheets have the same text, decoded content streams and rendered images as in v13b. Each review remains attached to its edition and scope. [Round 10 review record](data/round10_review_corrections.json) · [Packet index](notes/README.md) · [Sheet comparison](data/blueprint_v13c_page_comparison.json) · [Edition register](data/editions.json) · [PDF checksums](editions/v0.1.0/SHA256SUMS)

**Citation.** *RH Lean Verification Atlas (AI-drafted; maintained by Gunhee Cho)*, v0.1.0 (2026). Cite the Git commit selected by tag `v0.1.0`, the unit and step IDs, and the PDF digest where relevant. The release entry supplies the full Git hash. [Citation metadata](CITATION.cff) · [Attribution](AUTHORS.md)
