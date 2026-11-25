# Recording a human check

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

Start with one numbered inference you can derive or compare with its source. Copy its step number and the SHA-256 edition identifier from the checklist. The identifier fixes the exact text under review. Record what you did and what you found. A gap, a reservation or a step you could not follow can be submitted on its own. [Choose a checklist](../ROADMAP.md) · [Fictitious example](examples/FICTITIOUS-EXAMPLE.yaml) · [Reader-reported disputes](../questions/disputes.md) · [한국어](../docs/ko/signoffs/README.md)

## Submitting your reading

Use the named-check issue form or submit a pull request with a record prepared using the command below. [Issue form fields](../.github/ISSUE_TEMPLATE/signoff.yml) All submitted fields are public. Names, affiliations and ORCIDs are self-declared. The repository checks the format of an optional ORCID but does not verify anyone’s identity or qualifications. The attestation must come from the named reader. Maintainers transcribe the reader's submitted text and identify Gunhee Cho's own records as maintainer readings.

| Scope | What to enter in the verdict field |
|---|---|
| `steps [S1,S3]` | One verdict per listed step. For a YAML file use `scope: {steps: [S1, S3]}`. |
| `whole-note` | One verdict for **every** active step in that edition. Use `not-attempted` for steps you skipped. A whole-note reading can therefore be partial. |
| `statement-vs-lean` | A verdict on the separate target `statement-vs-lean`. Compare the quantifiers, hypotheses and conclusion with the pinned declaration or component declarations. |

Each verdict is one of `checked-correct`, `correct-with-reservation`, `gap-found`, `error-found`, `could-not-follow` or `not-attempted`. In `what_i_did`, identify the calculations you repeated, argument you followed, source you compared, and any assumptions you accepted. Include a description when reporting some or substantial AI assistance. A named reader can attest after assisted work; an AI review by itself cannot enter the human counts.

## When a step or unit qualifies

- A step is **human-checked** when a reader’s latest current-edition verdict is `checked-correct` and the target has no unresolved objection. `correct-with-reservation`, `could-not-follow` and `not-attempted` give no positive credit. The record shows the declared AI assistance (`none`, `some` or `substantial`).
- **L4 is local to a Full unit under its stated inputs.** The checklist must contain a derivation step, and readers must mark every active step and the separate statement comparison `checked-correct` for the current edition. An appeal to an input or a literature citation alone cannot carry the unit. Different people can cover different steps. L4 describes the written argument only. It establishes nothing about the truth of its inputs, its dependency graph, V, F or RH.
- Evidence levels are **not cumulative**. L1 records a statement comparison. L2 records an AI review of an argument. L3 requires agreement between independent sources. Personal checks can support L4 without any earlier AI grade or two independent sources. One self-declared reader, including the maintainer, can satisfy L4. The displayed result includes the number of contributing readers, whether any is the maintainer and the declared levels of AI assistance.
- **Two independent readers** is a separate designation. Both readers must mark the target `checked-correct`, report `none` under conflicts of interest and write “I checked independently of other readers.” under `what_i_did`. A reading marked `substantial` AI assistance is displayed and cannot count toward this designation. Matching names or ORCIDs identify a single reader for counting purposes. Every active step and the statement comparison need their own qualifying pair for the unit designation.
- `gap-found` or `error-found` opens a [dispute](../questions/disputes.md). A new vote alone cannot close it. On the same target text a **different reader who is not the maintainer** must give a `checked-correct` verdict, explain the resolution and identify the original record. In the issue form write `S2: checked-correct resolves PRIOR_RECORD.yaml`. In YAML use `resolves: {S2: [PRIOR_RECORD.yaml]}`. The original objection remains visible. The same rule applies to a statement comparison.
- A new edition needs new positive checks. An unresolved objection stays open across editions if the disputed step or statement is unchanged. When that target is changed or withdrawn, the old objection is marked superseded. It remains visible with its original verdict, and any replacement target needs its own check.

## Maintainer intake and pull requests

Copy the filled issue body to a text file or prepare a YAML/JSON file using the [field guide](TEMPLATE.md). The command accepts pasted Markdown through standard input with `-`. The command validates the date, reader, attestation, edition, step hashes, scope and verdicts. It appends a numbered record and refreshes the pages. Reimporting the same signed content reruns generation and keeps the original record. Review the changes locally before committing.

```sh
python scripts/add_signoff.py --dry-run my-check.yaml
python scripts/add_signoff.py my-check.yaml
```

For a pull request include the resulting `signoffs/records/YYYY-MM-DD_UNIT_reader-slug_n.yaml` and regenerated files. A later correction to a submitted check is another record. Never modify or delete the original submission. If the counts change, record an edition with `python scripts/snapshot.py --append --round 'Edition label'`. Its optional `--date` is a UTC date. [Progress history](../progress/README.md) Intake and publication are manual; there is no repository-writing issue bot.

When editing the proof, prepare an update keyed by unit ID with a `sources` list of note paths and a `steps` list in the format of the unit's `*.steps.yaml`. Keep stable step IDs and retain only AI evidence tied to the new edition. Run `python3 scripts/proof_steps.py --install updated_specs.json`, then `python3 scripts/refresh_round4.py`. These commands retain withdrawn IDs, archive the previous edition, regenerate its checklist and update grades. Every surviving step in a revised edition needs a fresh personal check.
