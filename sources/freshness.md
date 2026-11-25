# Snapshot dates and how to recheck them

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

The register uses UTC. A Git commit fixes a source tree and a SHA-256 digest identifies the downloaded bytes. [Full source register](registry.json).

| Resource | Edition date, UTC | Identifier |
|---|---|---|
| [Lean source mirror](https://github.com/leanprover-community/riemann-hypothesis/tree/40e56bab026552e089d7afcfeff08d2defb9c005) | 2026-11-20T14:36:09Z | Git commit `40e56bab0265` |
| [Original Lean distribution](https://alpo.ge/lean.tar.gz.part01) | 20 November 2026 distribution | SHA-256 `9631b4f02019` |
| [MIT verification record](https://math.mit.edu/~drew/grh/) | 24 November 2026 at 05:25 UTC | SHA-256 `51d1d86aa983` |
| [Adriazola’s reconstruction](https://github.com/jimjamzola/RH-Alpoge-Reconstruction/tree/aa9c86bf2a7d29b08575641fecea19a2a603e87c) | 2026-11-24T16:27:32Z | Git commit `aa9c86bf2a7d` |
| [Naskręcki’s reading project](https://github.com/nasqret/riemann-rev/tree/6ccea03b21e96b70356c07afb85a88d581b61e86) | 2026-11-24T05:14:02Z | Git commit `6ccea03b21e9` |
| [JoseBrox/GRH_distillation](https://github.com/JoseBrox/GRH_distillation/tree/a6e7aa8f8694c2cbc330671ea34512f024927d28) | 2026-11-24T23:57:05Z | Git commit `a6e7aa8f8694` |
| [jae-63/rh-alpoge-blueprint](https://github.com/jae-63/rh-alpoge-blueprint/tree/0434143d80c94d491e2228e234507d38dfcb57d7) | 2026-11-20T22:15:51Z | Git commit `0434143d80c9` |
| [Waterloo zeta draft](https://www.math.uwaterloo.ca/~mrubinst/alpoge_claude_grh/zeta-paper_v2.pdf) | 22 November 2026 (date printed in version 2) | SHA-256 `b49de5037af5` |
| [Alpöge’s announcement](https://alpo.ge/remark.pdf) | 20 November 2026 (printed date) | SHA-256 `3fc97784b71d` |

Recheck each local file with a SHA-256 utility. For the multipart archive, hash all fourteen pieces concatenated in order. Compare complete commit identifiers and tree hashes for repository editions. [Verification status](../STATUS.md).
