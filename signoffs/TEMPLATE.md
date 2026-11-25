# Human check field guide

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

Copy the [fictitious worked YAML example](examples/FICTITIOUS-EXAMPLE.yaml) into a new local file. Remove the example marker and replace all example values, including the fictitious non-attestation, with your own reading. Copy the edition from the unit checklist.

| Field | Content |
|---|---|
| `reader` | Your name, field and level (`faculty`, `postdoc`, `phd-student`, `other`). Affiliation and a checksum-valid ORCID are optional. |
| `unit`, `edition_sha256` | The unit ID and the full 64-character edition hash. |
| `scope`, `verdict` | The steps checked, whole-note, or statement-vs-lean, with one verdict per target as described in the [rules](README.md). |
| `what_i_did`, `time_spent_hours` | What you personally derived, followed or compared. Give hours as a nonnegative number. |
| `reservations`, `conflicts_of_interest` | Describe each limitation or conflict, or enter `none`. |
| `ai_assistance_used`, `ai_assistance_description` | One of `none`, `some`, `substantial`, and what the tool contributed. |
| `date`, `attestation` | Your reading date in YYYY-MM-DD format and the exact sentence “I read the edition identified above myself.” |

The importer adds `step_sha256` from the identified edition's checklist. Only a different reader other than the maintainer can use `resolves` to close an objection on unchanged text. Accepted input includes JSON and data-only YAML with nested mappings, simple lists, quoted or plain scalars and ordinary literal or folded blocks. [Issue form](../.github/ISSUE_TEMPLATE/signoff.yml)
