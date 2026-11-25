# Sources and editions

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

Gunhee Cho is the paper’s author and the blueprint’s editor. Both were drafted with AI assistance. No independent human referee has checked the arguments. Levent Alpöge is the author of the Lean development. The repository includes both PDFs. The edition register preserves the earlier sources used in reviews. [Blueprint v13b](../editions/v0.1.0/blueprint_v13b.pdf) · [Conditional paper v7](../editions/v0.1.0/paper_v7.pdf) · [Release notes](../RELEASE_NOTES_v0.1.0.md) · [Manuscript editions](../data/editions.json).

## Source, audit and reading projects

| Resource | Fixed edition | Source terms | Index or use |
|---|---|---|---|
| [Lean source mirror](https://github.com/leanprover-community/riemann-hypothesis/tree/40e56bab026552e089d7afcfeff08d2defb9c005) | Git commit `40e56bab0265` | No licence file found at the pinned commit. | [Reference source for every unit.](../data/pins.json) |
| [Original Lean distribution](https://alpo.ge/lean.tar.gz.part01) | SHA-256 `9631b4f02019` | No licence file found at the pinned commit. | [The archive checksum and root tree identify the baseline for every source span.](../data/pins.json) |
| [MIT verification record](https://math.mit.edu/~drew/grh/) | SHA-256 `51d1d86aa983` | Redistribution terms unverified. | [The status page cites the dated checker outcomes.](../sources/kernel-audit.md) |
| [Adriazola’s reconstruction](https://github.com/jimjamzola/RH-Alpoge-Reconstruction/tree/aa9c86bf2a7d29b08575641fecea19a2a603e87c) | Git commit `aa9c86bf2a7d` | [CC-BY-4.0](https://github.com/jimjamzola/RH-Alpoge-Reconstruction/blob/aa9c86bf2a7d29b08575641fecea19a2a603e87c/LICENSE) | [Manuscript numbers, Lean declarations and atlas units.](../crosswalk/adriazola.md) |
| [Naskręcki’s reading project](https://github.com/nasqret/riemann-rev/tree/6ccea03b21e96b70356c07afb85a88d581b61e86) | Git commit `6ccea03b21e9` | [0BSD](https://github.com/nasqret/riemann-rev/blob/6ccea03b21e96b70356c07afb85a88d581b61e86/LICENSE) | [Index of exact Lean declaration names.](../crosswalk/naskrecki.md) |
| [JoseBrox/GRH_distillation](https://github.com/JoseBrox/GRH_distillation/tree/a6e7aa8f8694c2cbc330671ea34512f024927d28) | Git commit `a6e7aa8f8694` | Redistribution terms unverified. | [Index of exact Lean declaration names.](../crosswalk/josebrox.md) |
| [jae-63/rh-alpoge-blueprint](https://github.com/jae-63/rh-alpoge-blueprint/tree/0434143d80c94d491e2228e234507d38dfcb57d7) | Git commit `0434143d80c9` | [Apache-2.0](https://github.com/jae-63/rh-alpoge-blueprint/blob/0434143d80c94d491e2228e234507d38dfcb57d7/LICENSE) | [Index of exact Lean declaration names.](../crosswalk/jae-63.md) |
| [Waterloo zeta draft](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf) | SHA-256 `b49de5037af5` | Redistribution terms unverified. | Not yet mapped. |
| [Alpöge’s announcement](https://alpo.ge/remark.pdf) | SHA-256 `3fc97784b71d` | Redistribution terms unverified. | Announcement and date identified here. There is no declaration-level index for this document. |

The MIT verification record was updated on 24 November 2026 at 05:25 UTC. Its SHA-256 is `51d1d86aa983ffa794708767f07b90e7abe4ff0f9ef340936b8c0fc693b6728a`. Its 175,187 figure counts compiled modules. The original archive contains 175,190 regular files, including the three non-source project files. [Checker results](kernel-audit.md) · [Declaration and graph pins](../data/pins.json).

## Background reading

| Published source | Reading scope |
|---|---|
| [UBC Math 539 handout, 2 April 2020](https://personal.math.ubc.ca/~gerg/teaching/539-Winter2020/Apr2.pdf) | Analytic track. AI review R19, public line 78, reports comparing Landau’s theorem in the Math 539 handout of 2 April 2020, p. 1, Theorem 15.1. No human check is recorded. |
| [A. Moriwaki, Continuity of volumes on arithmetic varieties](https://arxiv.org/pdf/math/0612269) | Arakelov track. Arithmetic volumes and the introduction’s Theorem A. Locator not independently verified in this release. |
| [S. Yamana, The Siegel–Weil formula for unitary groups](https://msp.org/pjm/2013/264-1/pjm-v264-n1-p11-p.pdf) | Theta track. Theorem 2. Locator not independently verified in this release. |
| [K. Kato, p-adic Hodge theory and values of zeta functions of modular forms](https://archive.numdam.org/item/AST_2004__295__117_0.pdf) | Galois track. Sections 8 and 9. Locator not independently verified in this release. |
| [Scholze, The local Langlands correspondence for GL_n over p-adic fields](https://people.mpim-bonn.mpg.de/scholze/LocalLanglands.pdf) | Local track. Theorem 1.2. Locator not independently verified in this release. |
| [Stable real cohomology of arithmetic groups](https://doi.org/10.24033/asens.1269) | K-theory track. Proposition 12.2. Locator not independently verified in this release. |
| [A bound for the torsion in the K-theory of algebraic integers](https://ems.press/content/book-chapter-files/27335) | K-theory track. Sections on the torsion estimate. The earlier AI report R19 gives §4.1, Theorem 1, p. 778 (2003). No human check of the published statement is recorded. |

[All source revisions, licensing locations and background references](registry.json) · [External resource guide](../LANDSCAPE.md).
