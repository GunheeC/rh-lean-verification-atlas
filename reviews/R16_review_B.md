AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

# R16_review_B

AI review report produced during this project; file names are internal working names.

- Internal source file: `out/R16_review_B.md`
- SHA-256: `ac60e0255aabdadb178405bc52036c13ac4e75229e959941ea347559be340080`
- Report scope: R16 review B — audit of the L/S/R/N triage pilot on Z1.5

## Internal report

The report below preserves its original verdict, scope and unresolved points. Superseded graph percentages have been removed from this public edition. Source line numbers in other records count from its original title.

# R16 review B — audit of the L/S/R/N triage pilot on Z1.5

Reviewer B, independent. Pin `40e56bab026552e089d7afcfeff08d2defb9c005`. Nothing in this review claims, or depends on, RH being proved; it concerns only how a Lean development is partitioned for a human-readable blueprint.

Inputs audited: `triage.py`, `R16_Z1_5_inputs.json`, `R16_Z1_5_triage.json`, `R16_Z1_5_triage.md`, `status.json`, the graph cache used by `graphq.py`, and the Lean source at the pin (original numbering, extracted with `git archive`).

## 0. Verdict

- **The tool is a correct and deterministic accountant.** I reproduced the shipped JSON and Markdown byte for byte, and all 41 row sizes with an independent reimplementation.
- **It is not yet a classifier, and the default N label is not a measurement of new mathematics.** In this register N is the default bucket for everything nobody argued into L, S or R; the register's own `scope` field says so ("not a claim of novelty for every line").
- **The reviewer estimated the mix of material in 25,578 lines assigned to N.** The examples include project-specific adaptations, textbook-citable results, definitions and glue. The author marked these as judgments from statements.
- **Not ready for the remaining ~2.1M lines.** Run unchanged it would return N by default across the remaining material and reduce nothing. Seven changes are listed in §3.1; the first three are blocking.

Limits of this audit: all 7 R, 11 S and 1 L rows were read in full against Lean. For N rows I read module inventories, principal statements and the Prop definitions behind them for 12 rows whose historical index weight was 22,413 lines, but not the proof bodies. The novelty estimates are statement-level judgments, not line counts.

## 1. Tool audit

### 1.1 Reproduction

`triage.py` imports `blueprint_cones.Graph`, which is not in `prev16/` or in the project scripts directory. The tool therefore cannot be run from the delivered inputs alone. I wrote a 15-line shim over the same pickle that `graphq.py` loads (weight = `line1 − line0 + 1` when `line0 > 0`, else 0) and ran the unmodified tool.

| Check | Result |
|---|---|
| Output JSON, `PYTHONHASHSEED` = 0, 1, 77 | identical to each other and to the shipped `R16_Z1_5_triage.json` (sha256 `c42d36d2…`) |
| Output Markdown, same seeds | identical to the shipped `.md` (sha256 `399122ff…`) |
| `register_sha256` | matches the inputs file (`4be8bda4…`) |
| Scope | 2,527 declarations, 442 modules, 26,532 lines: confirmed |
| Independent recomputation of residuals | 41/41 rows match on declarations, core lines and theorem lines |
| Unowned / multiply owned declarations | 0 / 0 |
| Overlapping source ranges inside scope | none; sum of ranges equals distinct covered lines (26,532) |
| `graphq.py deps/callers/find` spot checks | consistent with the same pins |

Sample of reproduced rows (declarations, core lines, theorem lines):

| Row | Class | Mine | Shipped |
|---|---|---|---|
| z15-local-reps | N | 334 / 3,400 / 3,011 | same |
| z15-eigenspaces | N | 249 / 3,372 / 3,318 | same |
| z15-regular-fibres | N | 260 / 2,651 / 2,398 | same |
| z15-cohomology | N | 302 / 2,550 / 2,241 | same |
| z15-global-trace | N | 159 / 2,234 / 2,053 | same |
| z15-integrality | N | 214 / 1,960 / 1,825 | same |
| z15-convolution | N | 165 / 1,676 / 1,455 | same |
| z15-counts | N | 98 / 812 / 775 | same |
| z15-quadratic-local | S | 6 / 139 / 139 | same |
| z15-eigenline | L | 3 / 90 / 90 | same |
| z15-exports | R | 22 / 44 / 44 | same |
| z15-consumer-predicates | R | 25 / 54 / 0 | same |

### 1.2 Claimed features against the code

| Claim | Implemented? | Comment |
|---|---|---|
| Residual (single-owner exclusive) classification | Yes in code (`walk_cut`), vacuous in this register | See 1.3 |
| Ownership and duplication checks | Yes, sound | A declaration in two seed sets raises; any scope declaration reached by two walks or by none raises; class totals must equal the scope |
| Cycle detection | Yes, at row level only | `TopologicalSorter` over row-to-row inheritance. It does not detect blueprint-level loops between proof labels, which was the R15 concern |
| Auto-escalation | Partly | Only rows proposed R are scanned. S and L rows are never scanned. Signals are lexical |
| L-citation check | Presence only | `citation` and `hypothesis_comparison` must be non-empty strings; nothing checks them against the Lean statement |
| Deterministic | Yes | No timestamps; outputs sorted; only the text of a cycle error could vary with hash seed |

### 1.3 Findings

**F1 (major). The residual walk does nothing here; classification is by module list.** 40 of 41 rows carry a `modules` field (433 modules in total), and for every row the residual equals its seed set exactly. The `roots` are "representative" heads only. A row such as z15-local-reps is 50 modules and 334 declarations, shown in the Markdown by one head of 129 lines out of 3,400. This is the R15 problem inverted: rows are no longer judged by a wrapper head, but nobody judged them at all. They were bucketed by directory.

Evidence that rows are directory buckets rather than mathematical units:
- The three `z15-satake*` rows, three `z15-convolution*` rows and two each of cohomology, regular-fibres, global-trace and weyl share one rationale sentence verbatim.
- The `-2`/`-3` splits exist to make the row graph acyclic, not because the mathematics divides there.
- `exclusive_before_cuts` is 0 for 40 of 41 rows, so no row is a self-contained cone.

**F2 (major). N is a default, and the tool can only move rows into it.** `final = 'N' if flags else proposed`. There is no gate on proposing N, no rationale requirement beyond a non-empty string, and no signal that would move a row out of N. The large N bucket is therefore a consequence of default assignments.

**F3 (major). The pilot assigns only the exclusive Z1.5 core.** The Z1.5 cone is 726,539 lines; the exclusive core classified here is 26,532. The other 700,007 lines are "excluded baseline" with no owner in this pilot. Across all 20 recursive inputs the exclusive cores sum to 845,527 lines, against 1,604,506 core lines in their union by my count (range weights from the same cache). About 759,000 lines are shared between inputs and have no owner under the exclusive-portfolio design. The tool lists them in `shared_core_boundary` but raises nothing. One R-row wrapper already dispatches into this unowned region: `cuspidal_traceMatrixUnits_acts_by_sum_infinitesimalCharacter` → `trace_Eop_of_hasInfChar` (53 lines, in the Z1.1 cone).

**F4 (medium). No check that the source tree matches the pin.** I pointed `--lean-root` at the cleaned tree (different numbering). The tool exited 0 and silently returned a different escalation set: `choice_source` disappeared from z15-exports-analytic. Class totals were unchanged only by luck. The default `--lean-root` is a relative path, so this is easy to hit.

**F5 (medium). Escalation signals are lexical and both hits in this run are false positives.** z15-exports-analytic (two 2-line wrappers) was escalated R→N because one statement contains a variable named `ε` (the CHOICE regex matches `ε`) and the other contains the type `Measure`. The CHOICE regex also matches `Nat.choose`. Cost here is 4 lines, but at 2.1M lines every wrapper mentioning a measure or an epsilon will inflate N. Conversely, a 36-line induction (z15-finite-product) passes because the threshold is 40.

**F6 (medium). Definitions are classed R.** z15-consumer-predicates is 54 lines with 0 theorem lines: `EigData`, `EigData.Classifies`, `CountKAlt`, `CountQAlt`, `Win`, `AdmKNAlt`, `AdmRNAlt`. These are the statement of the Z1.5 input. "Trusted to the kernel" is the wrong warrant for them: the kernel checks proofs, not whether a definition means what the blueprint says. Inside N there are a further 1,833 definition lines with the same issue in the other direction. Definitions need their own class routed to the definitions dictionary.

**F7 (minor).**
- Comment stripping is `line.partition('--')`; block comments are not handled.
- 88 scope declarations have no source range and are not marked auxiliary (65 theorems, 16 constructors, 6 definitions, 1 recursor). They are structure projections, equation lemmas and `casesOn`, all weight 0; none hides content. The scanner reports `source_range_unavailable` only for R rows.
- A register author can keep an R row under the 300-line theorem threshold by splitting it; nothing aggregates R by directory.

**No bug that hides in-scope content.** The completeness assertion (every scope declaration has exactly one owner, class totals equal scope) is sound. Content can only escape through the scope definition (F3) or through module-level granularity (F1).

## 2. Classification audit

### 2.1 R rows (7 rows, 167 lines): all read in full

| Row | Lines | Finding |
|---|---:|---|
| z15-exports | 44 | 22 two-line `first \| exact …` wrappers. 20 targets owned by z15-satake (N), 1 by z15-embeddings (S), 1 external (F3). Correct as R |
| z15-exports-2 | 10 | 5 wrappers; all targets in z15-satake-2 (N). Correct |
| z15-exports-3 | 6 | 3 wrappers; all targets in z15-satake-3 (N). Correct |
| z15-cohom-interface | 15 | Swaps Γ∩Λ between two subgroup presentations and chains three hypotheses. Correct |
| z15-finite-product | 36 | Pull one factor out of a pairwise-commuting product, by induction. Acceptable as R; S would be equally defensible |
| z15-inversion | 2 | Two `rfl` lemmas. Correct |
| z15-consumer-predicates | 54 | Definitions, not bookkeeping. Wrong class (F6); no hidden proof content |

Result: 0 of 7 hide proof content. This is a real improvement on R15 (3 of 12). The wrapper/implementation separation works: each wrapper's target has a recorded owner. One row is in the wrong category.

### 2.2 S rows (11 rows, 697 lines) and the L row: all read in full

All 11 S rows are self-contained standard arguments, and each rationale matches the Lean proof. No hidden content.

| Row | Lines | Content | Could be L? |
|---|---:|---|---|
| z15-cm-generator | 76 | x − x̄ gives a totally negative square in a CM field | no need |
| z15-cohom-rank | 34 | rank H ≤ rank cycles ≤ rank chains; swap of finite and cardinal sums | no |
| z15-coinduction | 67 | A is a retract of Coind Res A for finite index (averaged transfer) | yes: Brown, *Cohomology of Groups*, III §9 |
| z15-degrees | 44 | monomial count; degree of a leading minor | no |
| z15-embeddings | 48 | embeddings of a CM field pair up over the real subfield | no |
| z15-finite-quotients | 63 | fibre cardinality of G/U → G/U′; double-coset representatives; N(w) = p^f | no |
| z15-finite-trace | 98 | trace under faithful restriction; twisted trace form on End(P) | no |
| z15-haar | 55 | Haar measure scales by the inverse modulus of det | yes: Weil, *Basic Number Theory*, I §2 |
| z15-quadratic-local | 139 | Hensel for x²+x = z; split ⇒ unramified; different criterion | partly |
| z15-subrepresentation | 54 | matrices of a restricted action | no |
| z15-valuation | 19 | det of an integral invertible matrix is a unit | no |

L row z15-eigenline (90 lines): the citation (Horn–Johnson, Lemma 1.3.19) is the right result and the hypothesis comparison is accurate, including the arbitrary index set. Two notes:
- The row holds two independent Lean proofs of the same lemma (strong induction on dimension, and a minimal invariant subspace).
- z15-local-reps (N) contains a third proof, `jointEig` (66 lines: a commuting family has a joint eigenvector in the intersection of generalized eigenspaces), plus two thin restatements. The same textbook lemma is L in one row and N in another.

### 2.3 N rows: 12 rows sampled (22,413 indexed lines in these rows)

Structure of the N lines:

| Slice | Lines |
|---|---:|
| Definitions, structures, constructors | 1,833 |
| Theorems of ≤ 5 lines (387 of them) | 1,261 |
| Theorems of 6–15 lines | 4,191 |
| Theorems of 16–40 lines | 6,161 |
| Theorems of 41–100 lines (140) | 8,331 |
| Theorems over 100 lines (27) | 3,801 |
| Theorems whose statement is only opaque Prop names (`A → B → C`) | 8,230 |

The last line matters for any head-based reading: the entries assigned 8,230 indexed lines require opening the defined propositions, because the statement is a named Prop defined elsewhere (`theorem twExp : TwExp`).

Per-row observations. The public edition omits the historical estimates of class shares. T = textbook-citable (should be L or S). A = project-specific adaptation of known theory: bespoke statement, standard method, needs a written proof. G = glue or assembly. D = definitions. X = candidate for genuinely new mathematics.

| Row | Lines | What it is |
|---|---:|---|
| z15-local-reps | 3,400 | Distributions on orbit strata of totally disconnected spaces (`CellStep`, `DistZero`: the Bernstein–Zelevinsky localisation method); Jacquet modules and Casselman-type traces at Iwahori level; `DcosOp` (double-coset operator = vol · e π(x) e); torus eigencharacters |
| z15-eigenspaces | 3,372 | Isotypic decomposition over a restricted product (Flath-type), twisted Schur lemma on K-fixed vectors, finite-dimensionality of K-fixed eigenspaces, traces of products of commuting projections, then the CM-datum factorisations |
| z15-regular-fibres (+ -2) | 3,708 | Matching of orbital integrals for indicator "elementary" functions near strict diagonal elements under cyclic base change (`ElemLoc`, `VolRatio`, `CosetSum`, `MatchPow`, `Core`); Hilbert 90; openness of the norm. Labesse / Arthur–Clozel territory in an explicitly computable case |
| z15-cohomology | 2,550 | Uniform bound on total group cohomology via finite resolutions by permutation modules; passage along isomorphism, finite index and commensurability; minimal-vector stabilisers; existence of CM extensions; algebraicity of Hecke characters |
| z15-global-trace | 2,234 | `compress` (irreducibility under commuting idempotents and subalgebras), trace-comparison assembly theorems with 5–15 named hypotheses |
| z15-integrality | 1,960 | ℓ-adic bounds on Hecke eigenvalues of algebraic automorphic forms on a definite unitary group in terms of the weight (`AbsBound`, `OpBound`, `VecForm`) |
| z15-convolution | 1,676 | Spherical and twisted convolution operators, support and descent identities |
| z15-satake | 1,294 | Idele and Hecke-character bookkeeping, ramified twists, torus eigenforms; one Kronecker-type lemma |
| z15-arithmetic | 1,206 | Elementary algebraic number theory: split ⇔ local square, ramification index from inertia, integrality from a norm bound, CM criterion |
| z15-weyl | 888 | Highest weights, Capelli-type determinant identities, infinitesimal character of a coefficient representation |
| z15-counts | 812 | The five expert heads: assembly of count, Satake parameters, conjugation and integrality into `EigData` |
| z15-jacquet | 370 | Non-vanishing of Jacquet modules from character support; unipotent monodromy |

The clearest sign of over-classification is internal inconsistency. z15-arithmetic (N, 1,206 lines) contains `isSplitAt_of_isSquare`, `sqrt_fixed_of_isSquare_padic`, `ramificationIdx_eq_one` and `isIntegral_of_norm_le`. These are the same kind of statement, at the same depth, as the three theorems of z15-quadratic-local, which is S. The difference is only that the S ones were pulled into their own row.

### 2.4 Estimate for the 25,578 N lines

Weighting the table by row size:

| Category | Estimated lines (historical extrapolation) | Proper tier |
|---|---:|---|
| Genuinely new mathematics (X) | 0–2,500 | N |
| Project-specific adaptation of known theory (A) | 13,000–15,500 | a new tier: short proof plus reference for the method |
| Textbook-citable results (T) | 6,500–9,000 | L or S |
| Glue and assembly (G) | 1,300–2,000 | R |
| Definitions (D) | 1,833 | definitions dictionary |

The reviewer identified defaults that over-classify N and distinguished adaptation requiring exposition from a novelty claim.

Reasoning for the low X figure. The mathematical content of Z1.5 is a polynomial bound, in level and weight, on the number of regular algebraic cuspidal eigensystems, with Frobenius data classifying the attached Galois representations. Every ingredient I could identify from statements has a known method: bounded cohomology of arithmetic groups, Flath-type factorisation, base-change matching for elementary functions, weight bounds on Hecke eigenvalues, Capelli-type identities. I found no statement whose method looked unfamiliar. The candidates for novelty are in how the pieces are combined (z15-counts, the assembly theorems of z15-global-trace, the specific matching statement `Core`).

What would change this estimate: reading the proofs of the 27 theorems over 100 lines, and comparing the assembly statements against the source paper. I did neither.

## 3. Assessment

### 3.1 Is the tool ready for the remaining ~2.1M lines?

No. The accounting layer is ready; the classification layer is not. In order:

1. **Give the shared core an owner (blocking).** Exclusive portfolios cover 0.85M of about 1.6M lines in the union of the 20 inputs. Use a dominator-based or lowest-common-consumer rule, or run the shared region as its own portfolio. Without this, half the material is never classified and R wrappers can dispatch into it unseen.
2. **Stop using N as the default (blocking).** Add an explicit "unclassified" state that is reported separately and never summed into N. Require a per-row statement of what is new for N, with the same strictness L has for citations.
3. **Split the tiers (blocking).** Add D (definitions) and a tier for project-specific adaptations of known theory. With only L/S/R/N, everything bespoke lands in N regardless of difficulty.
4. **Cap row size and drop `modules` as the normal mechanism.** A row should be one statement-level head and its true residual, for example at most 300 theorem lines or one module. Allow module lists only for R. Report head and residual line weights separately and flag unusually small heads for inspection.
5. **Resolve opaque statements.** For a head whose statement is a named Prop, print the Prop's definition in the report. A third of N is unreadable otherwise.
6. **Fix the scanner.** Verify the source tree against the pin (git tree hash, or per-file hash) and fail on mismatch. Remove `ε` and bare `choose` from the CHOICE regex. Scan S rows as well. Add a duplicate-statement check so the same lemma cannot be L in one row and N in another.
7. **Ship `blueprint_cones.py` with the tool** so the run is reproducible from the delivered files.

Items 1–3 change the headline number; 4–7 make it trustworthy.

### 3.2 What Z1.5 implies for the size of the N tier

Base: about 2.1M remaining Lean lines.

| Reading of "N" | Assumption | Hypothetical index weight |
|---|---|---:|
| As the tool computes it today | Registers written the same way as Z1.5 (module buckets, N by default) | 1.9–2.05M |
| Needs a written proof (A + X) | Z1.5 mix transfers; T, G, D reclassified | 1.05–1.4M |
| Genuinely new mathematics (X) | Z1.5 mix transfers | 0–210k, point ~60k |

Assumptions, each of which could move the range:

- **Z1.5 is representative.** It may not be. Its exclusive core has 26,532 indexed lines and is the counting-specific layer. Shared infrastructure is likely to be more textbook-heavy, which would lower both A and X. Inputs with large exclusive cores (Z1.1 at 431k, Z1.3 at 134k, Z4.2 at 107k) were not sampled and could differ in either direction.
- **Statement-level judgment is adequate.** I did not read proofs of N rows. A standard-looking statement can hide a non-standard proof; this pushes X up, not down.
- **Line share is not page share.** The A tier is long in Lean because of measure-theoretic and topological bookkeeping. I have no measured Lean-to-prose ratio for this project and do not offer a page count.

Practical consequence: the pilot does not show that the blueprint needs full hand proofs throughout the material assigned the default N label. It shows that the L/S/R/N scheme, applied at module granularity with N as default, cannot separate "new" from "bespoke but standard". With the tier split in §3.1, the full-proof obligation should fall to a small fraction, and the dominant cost becomes the A tier.

## 4. Summary

- Tool output reproduced byte for byte under three hash seeds; 41/41 row sizes reproduced independently; no unowned or doubly owned declaration; no bug that hides in-scope content.
- The residual walk is vacuous in this register: rows are module lists, and N is the default bucket. The pilot assigns 26,532 exclusive Z1.5 lines, and the shared region in the 20-input union has no owner under the exclusive design.
- The tool silently accepts a source tree that does not match the pin. Both auto-escalations in this run are regex false positives.
- R rows: 0 of 7 hide proof content (R15 had 3 of 12); one is definitions and belongs in a D class. S rows: 11 of 11 correct. L row: correct, but the same lemma is re-proved inside an N row.
- The 25,578 indexed N lines contain examples of project-specific adaptation, textbook-citable results, glue and definitions. The reviewer treats suspected novelty as a separate question.
- Not ready for the full run. First changes: own the shared core, stop defaulting to N, add D and an adaptation tier.
- Projected over 2.1M lines: 1.9–2.05M "N" as currently computed; 1.05–1.4M needing a written proof; 0–210k (point ~60k) genuinely new, subject to the stated assumptions.
