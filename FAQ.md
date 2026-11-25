# Frequently asked questions

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

### Does this atlas settle the Riemann hypothesis?

No. The formal audit and the reading of the mathematical argument answer different questions. The audit concerns the formal declarations at one Lean revision. Two major assumptions in the written deduction still lack a complete derivation in the atlas. The status page gives the current count of signed human checks. [Status](STATUS.md) · [한국어](docs/ko/FAQ.md)

### The kernel accepted it. Why does this atlas not say “proved”?

Kernel acceptance establishes that the proof terms have their declared types relative to the checker, definitions and axioms. The atlas cites the third-party run and helps a reader compare those types with mathematical statements. It adds conditional written arguments for selected steps. No human has checked those arguments or matched the repository’s literature-named propositions to published theorems. [Formal statements](sources/lean-goals.md) · [Checker record](sources/kernel-audit.md)

### What did the kernel check?

The kernel checks that each proof term has its declared type under the recorded definitions and axioms. The frozen MIT record gives the results for external checkers and the status of the separate end-to-end comparator. For all five exports, Lean’s axiom inspection lists propositional extensionality, classical choice and quotient soundness. [Checker record](sources/kernel-audit.md) · [Exact conclusions](sources/lean-goals.md)

### Where do the written derivations stop?

V asks for one interval on which all the indicated Selmer bounds hold. F asks for one record containing a class of families and a compatible selection. The required comparisons must use that same selection. Even a complete local argument may assume results from elsewhere. No complete human-readable derivation of V or F exists in this atlas. The pinned Lean repository supplies both. <!-- front:faq -->Of 217 units, 55 have full arguments, 127 have outlines and 35 have statements only.<!-- /front:faq --> [V](pillars/V.md) · [F](pillars/F.md) · [Current counts](STATUS.md) · [Open questions](questions/README.md)

### What do the line counts measure?

A written step cites a range of lines in a particular Lean file. The counts take the union of those ranges within each category. A citation identifies the source for an inference. It says nothing about how many lines a person has checked or how much proof lies behind the cited result. The status page gives the two denominators and links to the separate table locating each source line in the index. [Definitions and counts](STATUS.md) · [History](PROGRESS.md)

### What does an AI review cover?

An AI system wrote the exposition. A separate AI review can compare a statement, inspect a particular step or assess an entire specified edition. A review of one passage applies only within its recorded scope. [Review archive](reviews/README.md) · [Authorship](AUTHORS.md)

### How can I check a single assertion?

Choose a unit and compare its quantifiers, hypotheses and exceptional cases with the linked Lean statement. Read an individual numbered step and follow each input it uses. Record the edition identifier, the step number and your verdict. You can record a gap or a step you could not follow. [Starter packets](notes/README.md) · [How to submit](signoffs/README.md)

### What do the grades mean?

L0 identifies the formal source. L1 records a comparison of the statement and its assumptions. L2 records an AI review of the written argument under the stated inputs. L3 requires matching evidence from at least two independent sources. L4 applies only to a Full unit and requires a derivation beyond an appeal to an input. Every current step and a separate statement comparison must have a qualifying personal check. An unresolved objection prevents that target from qualifying. A second reader other than the maintainer can resolve a dispute, or a new edition can supersede its target. Names are self-declared. Partial and negative assessments stay visible. [Grade rules](sources/coverage.md) · [Dashboard](dashboard/README.md)

### Where can I find other readings?

Use the source mirror for Lean code and the MIT record for checker runs. To compare an author’s notation or proposition numbers, choose the identified edition of that exposition. [Public reading projects and comparisons](LANDSCAPE.md)
