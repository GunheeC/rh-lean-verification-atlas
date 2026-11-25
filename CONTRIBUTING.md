# Contribute a check

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

The Git author identifies Gunhee Cho as the repository owner. AI wrote the atlas content.

Start with the [unit page](lookup/declarations.md), the exact edition you read and the first step affected. A locally completed form is a draft until its author chooses to share it. If AI helped produce a submission, label that assistance and say which parts a person actually checked.

| Contribution | Evidence to include | Record |
|---|---|---|
| Check a unit | Unit, checklist edition, step IDs or statement comparison, individual verdicts and reservations, reader identity and personal attestation | [Sign-off form](.github/ISSUE_TEMPLATE/signoff.yml) · [How sign-offs are recorded](signoffs/README.md) |
| Correct an error or compare two stated hypotheses | Quote the smallest disputed claim, give the two source locations, identify a missing assumption or failed inference, and specify the affected conclusion. Include a counterexample if available. | [Error report](.github/ISSUE_TEMPLATE/error-report.yml) |
| Add an independent exposition | Give an immutable commit or document digest, author attribution, license evidence, stable theorem locator and the aligned Lean statement. Explain independence, differences in hypotheses, and which portions were read. | [Source form](.github/ISSUE_TEMPLATE/new-source.yml) |
| Add a crosswalk row | Identify the external section or theorem, pinned file and lines, qualified Lean name and unit. Distinguish a name occurrence, a partial correspondence and an exact proposition. Include affirmative evidence for any proposed change of grade. | [Existing rows](crosswalk/README.md) · [Source or mapping form](.github/ISSUE_TEMPLATE/new-source.yml) |
| Ask a question | Give the unit, the first unclear step, the background you used, and links to the sources already tried. | [Question form](.github/ISSUE_TEMPLATE/question.yml) |

## Recording a decision

Keep the original report and its scope. Check new source pins before changing the unit YAML. Record a correction or unresolved disagreement in the relevant review or question and retain both sides' locators. A name match supplies navigation. A positive whole-unit grade needs evidence for every principal statement in that unit. An AI-written report cannot fill the named-human field.

After an accepted edit, regenerate the pages, declaration lookup and dashboard with `python scripts/refresh_round4.py`. Run `python scripts/validate.py` from the atlas root. Changes to public claims, grades or source editions belong in the [change log](CHANGELOG.md). The [citation file](CITATION.cff) cites the atlas; mathematical claims should additionally cite their primary declarations and, when used, the outside author's edition.
