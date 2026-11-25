# Checker evidence for the five Main declarations

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

The MIT verification record is signed Andrew Sutherland (MIT). The snapshot used here is dated **24 November 2026, 05:25 UTC**. Its SHA-256 is `51d1d86aa983ffa794708767f07b90e7abe4ff0f9ef340936b8c0fc693b6728a`. The rows below transcribe the status of the **main submission** at that time. The arithmetic reformulations further down the original page are separate runs. [MIT primary record](https://math.mit.edu/~drew/grh/) · [Snapshot register](registry.json)

| Object checked | Result recorded in the snapshot |
|---|---|
| Original Lean 4.33.1 build and module-by-module Lean kernel replay | All 175,187 modules built and passed replay. |
| Sandboxed rebuild and export comparison | The export matched byte for byte. Of the 175,187 compiled module files, one differed; the audit describes its nondeterminism. |
| Full export, Lean 4.36.0 default and paranoid kernels | Both accepted, under both the default and adjusted allocator settings. |
| Full export, nanoda | Accepted. |
| Full export, con-leche from master; challenge comparisons with con-leche and con-ron | Accepted at the revisions named in the audit. The bundled 4.36.0 versions declined an unsupported inductive type. |
| Compiled modules, lean4lean built against 4.33.1 | Passed all modules. Five required reruns with a higher step limit. The 4.36.0 bundled checker was incompatible with this library. |
| Standalone Comparator 4.33.0 | End-to-end pass with the submission's comparator configuration. |
| Lean 4.36.0 lake comparator, end-to-end challenge vs. solution | **In progress.** Its paranoid and nanoda stages had accepted. Its last, default-kernel stage was running. The separately completed default-kernel run above used the same full export. |
| Axiom inspection of all five exports | Each used only `propext`, `Classical.choice` and `Quot.sound`. The audit separately found 15 axioms in the environment, all in Lean core. |

An AI session compared the snapshot digest and read the entries. This project did not reproduce those checker runs. The named-reader register currently contains zero signed mathematical assessments. [Sign-off register](../signoffs/README.md) [Scope and status](../STATUS.md)
