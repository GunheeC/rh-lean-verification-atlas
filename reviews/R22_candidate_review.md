AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

# R22_candidate_review

AI review report produced during this project; file names are internal working names.

- Internal source file: `out/R22_candidate_review.json`
- SHA-256: `cb03136ac5829e89c7c7c9afe9aaa999859d062a55873a84562e57331bf87e34`
- Report scope: Candidate disposition ledger from the R21 review integration

## Scope and result

A structured working ledger used to implement the R21 review. Its entries track individual claims or measurements. The independently readable [round report](R22_report.md) records the resulting corrections and preserved manuscript state.

Selected ledger fields, as recorded in the local source:

```json
{
  "round": 22,
  "source_commit": "40e56bab026552e089d7afcfeff08d2defb9c005",
  "review": "out/R21_review.md",
  "review_sha256": "9e241d4b6e07b744eaa2c025e6c6ef9e8567170923b4f9a928dc4a1d5b08b7fc",
  "baseline": "out/R21_pending.json",
  "baseline_spans_rechecked": 17,
  "baseline_changed": false,
  "new_hand_proofs": 0,
  "hash_convention": "UTF-8 inclusive lines joined by newline, without an appended newline."
}
```
