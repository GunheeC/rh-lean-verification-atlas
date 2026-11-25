AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

# R22_review_crosswalk

AI review report produced during this project; file names are internal working names.

- Internal source file: `out/R22_review_crosswalk.json`
- SHA-256: `db87baaed581e8d4cc082b79657a6167218dc6d9ade5d4e43f6b3151467315c6`
- Report scope: R21 review-to-revision crosswalk

## Scope and result

A structured working ledger used to implement the R21 review. Its entries track individual claims or measurements. The independently readable [round report](R22_report.md) records the resulting corrections and preserved manuscript state.

Selected ledger fields, as recorded in the local source:

```json
{
  "basis": "Original source spans under the pinned formal development. Hashes use UTF-8 source lines joined by LF with no final newline. Source names with a review prefix or a private kernel module have been resolved to their exact graph key. All weights use one allChi dominator tree. Before-R22 net subtracts the nearest 52 retained R21 boundaries. Each extra reading anchor is within the reported retained cut; its hypothetical single-cut weight is informative and is not added. The 87 suggestions that were not retained do not introduce dispositions or exact citations and do not change the 623-entry inventory. Source signatures are included in full.",
  "review_sha256": "9e241d4b6e07b744eaa2c025e6c6ef9e8567170923b4f9a928dc4a1d5b08b7fc",
  "review_section": "4.2"
}
```
