AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

# R22_review_graph

AI review report produced during this project; file names are internal working names.

- Internal source file: `out/R22_review_graph.json`
- SHA-256: `7cedc22b78f70a4379b9ff76b3df844a1295bb7424f41ad2efc53dc5a1ddd4bc`
- Report scope: Graph and scope measurements for R21 integration

## Scope and result

A structured working ledger used to implement the R21 review. Its entries track individual claims or measurements. The independently readable [round report](R22_report.md) records the resulting corrections and preserved manuscript state.

Selected ledger fields, as recorded in the local source:

```json
{
  "source_graph_sha256": "be8105049e470b3ef224a2b234a0cac6395f8fb1d983c8200416f116ba15abf6",
  "review_sha256": "9e241d4b6e07b744eaa2c025e6c6ef9e8567170923b4f9a928dc4a1d5b08b7fc",
  "rule": "Delete the entire specified vertex set before walking allChi. Stop at lit and sum valid core source spans once per reachable declaration. Count losses inside/outside the original 32 using their nearest R21 dominator. This hypothetical graph saving neither establishes a citation nor classifies all affected lines.",
  "review_estimate": "0.4–0.9 million cite and about 5.6 million project-specific are reviewer estimates. The joint deletion results measure counterfactual dependency-graph reach, not the classification of the original six-million-line portfolio."
}
```
