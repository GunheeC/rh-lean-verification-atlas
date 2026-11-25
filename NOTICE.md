AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

# Rights, attribution and provenance

Copyright © 2026 Gunhee Cho, to the extent copyright subsists in AI-generated text. CC BY 4.0 covers original atlas writing, editorial arrangement and original data to the extent of rights held. The grant does not cover material derived from the Lean source. No licence file found at the pinned commit. The matching archive contains 175,187 Lean files and three project files. Original scripts and workflow code use the MIT License. [License scope](LICENSE) · [Script license](LICENSE-MIT) · [Source editions](sources/README.md).

Gunhee Cho maintains the repository and decides what is released. AI systems drafted the text. The project’s own blueprint v13 and papers v3, v4 and v5 are AI-written, unpublished drafts with no human review. Levent Alpöge did not author these manuscripts. [Editions and available excerpts](data/editions.json) · [Release v0.1.0 assets](RELEASE_NOTES_v0.1.0.md).

| Referenced material | Source terms at the pin | Atlas use |
|---|---|---|
| Lean source mirror and Original Lean distribution | No licence file found at the pinned commit | Declaration names, locations, hashes, measurements and the public goal signatures. |
| MIT verification record, signed Andrew Sutherland (MIT) | Redistribution terms unverified | Dated outcomes, checker names and primary links. |
| Adriazola’s reconstruction | CC BY 4.0 at the root | Manuscript numbers, declaration names and corresponding unit IDs. |
| Naskręcki’s reading project | 0BSD at the root | Node IDs, names, locations and links. |
| JoseBrox/GRH_distillation | Root licence unverified | Names, locations and links. |
| jae-63/rh-alpoge-blueprint | Apache-2.0 at the root | Names, section numbers, locations and links. |
| Waterloo zeta draft and Alpöge’s announcement | Redistribution terms unverified | Bibliographic records, edition hashes and links. |

Root licences concern the identified repositories. Individual third-party contributions may have their own terms. [Source register](sources/registry.json) · [Goal signatures](sources/lean-goals.md).

The optional static site requests MathJax 3.2.2 for typesetting from the registered CDN. Its JavaScript is hosted externally. The site’s 47 WebP files have the same hashes as the reading packets. [MathJax 3.2.2 license, Apache-2.0](https://github.com/mathjax/MathJax/blob/3.2.2/LICENSE).

## The page images and local notes

All **47 WebP page images** in the seven reading packets come from the project’s own 944-page blueprint v13. The packets use 46 distinct physical PDF pages because two packets share a boundary page. Each image matched its recorded SHA-256. Every decoded RGB pixel also matched a fresh render of the corresponding page of the local release PDF, whose SHA-256 is `d9dcb73f10a5829865f9246409d886c16cb1d2087717adf7758f154257a28af4`. [Editions](data/editions.json) · [Packet page numbers and image hashes](data/notes_starters.json).

All **228 TeX files** under `notes/` trace to the project’s own manuscripts. The audit matched 165 paper-v3 extracts and 154 recorded fragments used by 48 blueprint notes, eight full supplementary arguments and eight source ranges used in seven starter extracts. Some blueprint working-source fragments postdate v13 and have no printed v13 page locator. [Unit excerpts](data/notes_units.json) · [Blueprint excerpt register](data/blueprint_excerpt_index.json).

## Reproduction check

The database round-2 audit compared atlas files by content hash against all 175,190 files in the original Lean archive, files in the four pinned reading-project repositories, and the MIT verification record, Waterloo zeta draft and Alpöge’s announcement. It found no complete file copied from those source editions. A separate 20-word comparison screened the local text, data and code against the available upstream prose and source-text formats. Candidate runs consisted of declaration names, dependency paths, digest or formula tokens, and the expressly quoted Lean goal signatures. The screen found no extended matching passage of expository prose in that corpus. Standard license text is excluded from the prose screen. The test detects literal overlap in the compared editions. Translations, paraphrases and unscreened literature require separate assessment.

Run `python3 scripts/verify_page_provenance.py` to check every image hash. Supplying `--pdf /path/to/blueprint_v13.pdf` also compares rendered pixels on macOS with PDFKit, Swift and Pillow. The audit method, input scope and qualification are recorded in the [reproduction audit](data/reproduction_audit.json).

[Contributors and division of work](AUTHORS.md)
