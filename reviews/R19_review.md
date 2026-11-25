AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

# R19_review

AI review report produced during this project; file names are internal working names.

- Internal source file: `out/R19_review.md`
- SHA-256: `aa51dd3702189be9696cf747ee1de47d3e4c15330dfe2a1834797c9fd8fa3ea7`
- Report scope: R19 skeleton — independent review

## Internal report

The report below preserves its original verdict, scope and unresolved points. Superseded graph percentages have been removed from this public edition. Source line numbers in other records count from its original title.

# R19 skeleton — independent review

Reviewed: `R19_skeleton.md` / `R19_skeleton.json` (140 nodes P001–P140; grades L 0, S 35, A 14, N 0, R 20, U 71), against the Lean source at commit `40e56bab…c005`.

**Scope and limits.** This review compares written statements with Lean statements, checks citations and grades, and checks graph edges. It does not assess whether any proof is mathematically correct, and nothing here is a claim that RH or GRH is proved. The grades I give are statement-level judgments by a non-specialist reader. Literature marked *[memory]* comes from my recollection and was not checked against the text; literature marked *[checked]* was opened and read during this review.

## 0. Verdict

- **Fidelity is good.** All 140 Lean locations and statement texts match the original commit (140/140 span hashes). In about 50 nodes read against the Lean definitions I found no substantive mismatch of hypotheses, quantifiers or constants, only compressions (§1).
- **The DAG is correct as far as it goes.** All 155 distinct witness hops and all 123 direct dependencies check out (§4).
- **The A grades hold up.** Every cited source exists and says roughly what is claimed; two bases are loose and two A nodes are over-graded (§2).
- **Most U nodes can be settled.** Of 71, I can give a grade to about 64. Four are N-candidates, two need an expert, and one (P010) is the target itself (§3).
- **As a table of contents it is not yet sound.** The skeleton resolves the 20 inputs well but leaves about 6.9M of the 7.03M exclusively-owned lines inside four undivided U nodes (P010, P012, P013, P015). The theorems where the argument actually turns are not nodes (§5).

## 1. Statement fidelity

**Mechanical checks, all 140 nodes.**
- Each `source.file:line0–line1` span at the pinned commit hashes to the recorded `sha256_source_span`: 140/140.
- Each `lean_statement` is found in its span: 140/140.
- MD headings and paragraphs agree with the JSON: 140/140.
- The cleaned tree in `src/` differs from the pinned commit for P001–P008 (line numbers and proof terms, e.g. `rhOfAll := Claim.zeta allChi`). The skeleton consistently uses the original commit.

**Nodes read against the unfolded Lean definitions.**
- Top chain: P001–P023.
- A nodes: P018, P022, P023, P026, P034, P038, P039, P042, P063, P066, P084, P086, P128, P129.
- S nodes: P028, P035, P040, P049, P050, P051, P052.
- R nodes: P019, P047, P053, P059, P068, P135, P136 (proof bodies also read).
- U nodes: P025, P027, P029, P031, P036, P037, P064, P139, P140.

**Result: no substantive mismatch.** Constants that I checked exactly:

| Node | What was checked | Result |
| --- | --- | --- |
| P013 / P020 | `VWinAt ψ 401`; ε < 1/52; `PageN` as x^{2+8ε} ≤ 2^e ≤ 2x^{2+8ε}; window Y ≤ x ≤ Y²; bound `sqrt(exp(x^ε))` written as exp(x^ε/2) | exact |
| P017 | exponent 1/2 + (e_D + e_L + 7)ε | exact |
| P018 | `FormB`: ∀λ>1, ∀θ∈(0,1), windows [Y, Y^λ] | exact |
| P022 | `PoleData` (growth e^{2u}, simple poles, positive real residue at real poles); `WindowHypU` (∀η, arbitrarily far [U,(1+δ)U], majorant R ≥ 0, ∫R e^{−θu} ≤ e^{ηU}) | exact |
| P023 | window [Y, Y^{1+δ}], G_F(y) ≤ C·y^θ, arbitrary real C | exact |
| P034 | k even, k+1 < r₂, n ≥ 2(k+1)+4, rank ≤ r₂ | exact |
| P035 | card of torsion of H_m(GL_{n'}) equals `tc L n m`, which is the card of torsion of H_m(GL_n) | exact |
| P038 | bound b^A·s^{mAs^m} with A = `orbBound`, s = 3^{dd·N}, b = m+2 | exact |
| P039 | log\|T\| ≤ exp((2e[L:Q])^C·log(2\|disc\|)); ranges 1 ≤ N ≤ 4e+6, m ≤ 2e+1 | exact |
| P042 | valuation scaling e, generator count g, evaluation maps for all Z ⊆ X, length identity per block | exact |
| P036 | g = 2[L:Q] + ⌊log₂ h_L⌋ + 2 (`gens`) | exact |
| P051 | "= 2·log ht(R)/([K:Q]·D)" is the unfolding of `lcv` | definitional, correct |
| P052 | totally-complex hypothesis is in scope through the section `variable` | correct |
| P084 / P086 | ∃γ sits outside the implication | reproduced correctly |
| P129 | q and k_P are hypotheses, not conclusions | note is accurate |

**Compressions worth fixing.** None changes the meaning, but a reader of a paper would need them.
1. **P019.** `ChebyshevInequalityAtWindowScale` chooses e_D, e_L, ε₁ before ε (∃ e_D e_L ε₁, ∀ ε < ε₁, ∃ family). The paragraph says only "for all sufficiently small ε a tied family can be supplied". The uniformity of e_D, e_L in ε is what lets the exponent tend to 1/2, so it should be stated. The first hypothesis is also an implication (tied ⇒ bound), not a bound.
2. **P013 / P020.** `WinPair` is never unfolded. Its conditions are: q ≡ 3 mod 8; d ≡ 7 mod 16; q | d+1; every odd prime p ≤ Y^{ε/5} divides d+1; and log-size windows for q and d. It is taken at scale X^{1/J}. `IsChiField` is also not unfolded: E is the subfield of Q(ζ_N) fixed by a ≡ ±1 mod 2^{e+2}, ψ(a) = 1, (a/q) = (a/d) = 1. These define which fields the Selmer window ranges over, and the paper's main definition needs them.
3. **P022.** The growth bound is only for u ≥ 0, and the Laplace identity only for Re s > 2.
4. **P034.** The hypothesis k+1 < r₂(L) is reproduced but not explained, and the "difference" text does not mention it. It is unusual relative to Borel and should be a listed difference.
5. **P012.** The paragraph is correct. The structure name `OpenLiteratureStatements` is misleading, because P010/P011 discharge all three fields with proved theorems. A sentence saying so would prevent a reader from thinking these are open assumptions.
6. **P026, P063, P066.** `SrcUr`, `AdmWn`, `IsZWc`, `Sys`, `IwSys2`, `SpLink` and `Pin7` are named, not unfolded. I could confirm the paragraph only at the level of the visible binder structure.

## 2. Grades

### 2.1 The 14 A nodes

| Node | Base literature | Stated difference | Comment |
| --- | --- | --- | --- |
| P018 | Real. Martin's notes p. 1 use "Theorem 15.1" as the integral form of Landau's theorem *[checked]*. In the printed Montgomery–Vaughan I recall it as "Lemma 15.1" *[memory]*; verify the label. | Accurate | The proof is a 12-line reduction to P023 through `level_family`, so its proof role is R. |
| P022 | Same | Accurate | The proof uses k-th derivatives at σ > 2 with k ≈ U, so the kernel u^k·e^{−σu} concentrates in the window. A closer base is the localised oscillation theorems of Turán, Pintz and Kaczorowski *[memory]*. Keep A. This is a self-contained new lemma (863 lines) and deserves a full proof in the paper. |
| P023 | Same | Accurate | `CharFamily` needs positive weights and "N=1 or χ≠1"; `Gchi` includes the −y·log y and L′/L(1) corrections. The paragraph says "finite weighted character family", which is acceptable. |
| P026 | Kato, Astérisque 295: (8.1.3) is the p-adic zeta element of a newform *[checked]*. The norm relation for (8.1.3) is Prop. 8.12 *[checked]*; cite it instead of "the norm relations of §8". | Plausible | The proof role is R (it assembles P053, P058, P062, P063, P065, P066). |
| P034 | Borel 1974: Thm 7.5, Thm 11.1, §§11.2–11.4 exist and match the description *[checked]*. | Accurate, incomplete | The directly relevant statement is Borel's §12, Prop. 12.2 (ranks of K_i) *[checked]*; add it. Add k+1 < r₂ as a difference. |
| P038 | Soulé 2003, §4.1 Thm 1, p. 778: N ≥ 2, primes p ≤ 1+sup(r,N) excluded *[checked]*. | Accurate | s = 3^{[L:Q]N²} is consistent with bounding finite subgroups by reduction mod 3, which is how small primes can be kept. |
| P039 | Same | Accurate | — |
| P042 | Stacks 02M1 is Lemma 10.52.13 with the stated formula *[checked]*. CRing Prop. 4.9 is flat base change of Hom *[checked]*. | Accurate | The real mathematical setting is generalized matrix algebras; see P041–P044 in §3. |
| P063 | Kato §8 | Plausible | Not unfolded far enough to confirm. |
| P066 | Kato Thm 9.7 exists and concerns the dual exponential of the element (8.1.3) *[checked]*. | Plausible | — |
| P084, P086 | Dummigan–Schönnenbeck Props 3.4–3.5 exist *[checked]*, but they are about matrices of Hecke operators T_p through neighbour counts. | Plausible | The base is loose. The Lean statements are existence of a unitary element realising one up or down neighbour step with adelic compatibility. Kneser's neighbour method for Hermitian lattices and strong approximation are closer *[memory]*. |
| P128 | Dummigan–Schönnenbeck §2.2 (adelic action, stabiliser, double cosets) *[checked]* | Accurate | Generic background; A is generous. S or A. |
| P129 | Same | Accurate (it says itself that no existence is concluded) | Over-graded. It verifies that a given point represents x·κ. Regrade to S. |

### 2.2 S nodes checked (12)

- **Agree:** P040 (Poitou–Tate length formula under the three assumed dualities), P049, P050, P051, P052 (covolume, Gram determinant and dual lattice), P076, P098, P110, P111, P112 (algebraic Hecke characters), P137 (I re-derived H\*H = I), P138.
- **P035, change to A or L.** Homological stability for GL_n(O_L) in the range n ≥ 2m+4, together with finite generation, is a named published theorem (van der Kallen 1980 *[memory]*), not folklore. The range needs checking against it.
- **P033, S or R.** `SThetaOf` is an implication from six step-premises (`SChain → SPrism → SPrismMul → SZc → STrans → SCoc → STheta`), proved in about 80 lines. "Standard computation" is not evidenced.
- **P028, P070, P083, P085, P088, P089.** These are routine statements about project-specific objects. S is acceptable, but see the note on project-internal lemmas in §3.3.

### 2.3 R nodes checked (10)

- **Agree, proof bodies read:** P019, P047 (case split over four premises), P053, P068 (witness plugging), P059, P080 (one-line existential packaging), P125, P135 (`AdTie.levMid` does supply the local existence and the character identity, as the rationale says), P136 (uses `UlocAlt` and `U_eq`, as the rationale says).
- **P065, questionable.** The statement looks like assembly, but the proof is `glue2` applied to about 20 further lemmas (`meas3`, `smNz`, `explSmul`, `avgEq`, and others), and the exclusive cone is 3,308 lines. That is content, not packaging. Regrade to A (Kato §§8–9 plus an Eisenstein measure), or split it.

## 3. The 71 U nodes

### 3.1 Top chain (19 nodes)

The skeleton declines to give R to thin wrappers. For a table of contents the proof role is what matters, so I give both where they differ.

| Node | My grade | Reason |
| --- | --- | --- |
| P001, P002, P003, P009 | R | Pure wrappers. The statement is the classical conjecture, which is a published conjecture and not a published theorem, so L/S/A do not apply. |
| P004, P006, P007, P008 | R | Other forms of the target from P009 by the functional equation and the reduction to primitive characters (`Claim.strip`, `Claim.zeta`, `critLine`, `rh_of_every`); S-level content. |
| P005 | R | Specialisation of P004. |
| P010 | Target | The claimed result itself. No grade on the scale is meaningful. Its 761,324-line exclusive cone is not about this statement: it is the proof of `Row0b` (see §5). |
| P011 | R | Assembles P012, P013 and `recTExists`. The statement "Row0b ⇒ target" has no published analogue by construction. |
| P012 | N-candidate | Selmer windows plus literature ⇒ target. This is the theta and Arakelov half; it is not one statement but a 5.67M-line subtree. |
| P013 | N-candidate | Row0b ⇒ `VWin`: a subexponential bound for Σ_ℓ log ℓ · Σ_{e<x^401} (length of the localisation kernel of Z_ℓ(e)), uniform over the fields cut out by `IsChiField`. The nearest published results are Mazur–Wiles and Rubin for abelian fields and Soulé 1999/2003 *[memory]*; none gives this uniform statement. Needs an Iwasawa-theory expert. |
| P014 | R | P015 plus `imprimitive` (primitive ⇒ all characters; standard). |
| P015 | N-candidate | Green + `VWin` + `HypsAlt` ⇒ zero-free. `Green` itself is Green 1955 on cuspidal characters of GL_d(F_q), which is L *[memory]*. |
| P016 | R | The proof assembles P017, P018, P019. The hypothesis `TopG` (Selmer bound ⇒ family connectedness) carries the novelty. |
| P017 | **N-candidate** | Lattice-chain data (`ChainTied`) ⇒ G_Λ(x) ≤ x^{1/2+(e_D+e_L+7)ε} on windows. I know of no published statement that derives square-root cancellation in a character-weighted prime sum from lattice or slope data. |
| P020 | R | `VWin` from `LemmaK` plus four count bounds plus a literature bundle; every ingredient is a named hypothesis. The 21,873-line cone means the assembly is heavy. |
| P021 | R (medium confidence) | A pointwise inequality ASK ≤ Main + Err under 11 named hypotheses; weighted-average bookkeeping. |

### 3.2 Input side (52 nodes)

| Node | Grade | Closest published result or reason |
| --- | --- | --- |
| P024 | A (low confidence) | Ordinary automorphy lifting and propagation along families: Geraghty; Barnet-Lamb–Gee–Geraghty–Taylor; Newton–Thorne *[memory]*. An expert must pin the exact theorem. |
| P025 | A | Ordinary versus Bloch–Kato local conditions for the polarised adjoint, n ≤ 4: Newton–Thorne on adjoint Selmer groups; Allen 2016 *[memory]*. |
| P027 | Expert needed | Graded-algebra cotangent length ≤ 2·Σ v(ξ(a)). The nearest analogy is the Wiles–Lenstra numerical criterion *[memory]*, but I see no published match. Lemma-level N-candidate. |
| P029, P030, P061 | A | Polynomial bound on Hecke or Frobenius eigensystems of bounded weight and level, independent of ℓ: compatible systems plus the trivial bound on cuspidal cohomology. P030 adds descent from an imaginary quadratic field. |
| P031 | A | Iwasawa descent: the Sha of Z_ℓ(e) at layer m equals the cokernel of the twisted γ^{ℓ^m} − 1. Iwasawa; Schneider 1979 *[memory]*. |
| P032 | A | Homology classes of GL_N(O_L) with Z/q coefficients, evaluated at residue fields: Soulé 1979; Quillen 1972 *[memory]*. |
| P036 | A (low to medium) | Kummer-theoretic count of equivariant characters with a generator bound from units and class number. |
| P037 | A | Sha length bounded through equivariant divisor-class characters over all layers; same family as P031. |
| P041, P043, P044 | A | **Generalized matrix algebras and the lattice construction**: idempotents, distinct eigenvalues, reducibility ideal, Ext groups landing in Selmer groups. Bellaïche–Chenevier (Astérisque 324, ch. 1); Ribet 1976; Urban 2001 *[memory]*. The explicit error terms in P044 are the adaptation. The skeleton missed this identification, which also covers P042. |
| P045 | Expert needed | Valuation bounds for coefficients of weighted derivatives of theta series under a formal-group integrality hypothesis. Possibly Katz 1978 on p-adic interpolation and Lubin–Tate integrality *[memory]*. |
| P046 | R | Assembles P059 and P060. |
| P048 | R | Assembles P054–P057. |
| P058 | A | Integral Hecke projection to an eigencomponent with a bounded denominator ℓ^a: Kato §6; Hida's ordinary projector *[memory]*. |
| P060 | R | Existential packaging over P080 and the Lubin–Tate curve hypothesis. |
| P062 | A (low) | Local non-triviality of the Euler-system class from non-vanishing of power-series moments (Kato §§12–13 type). The 6,815-line cone shows real content. |
| P064 | A, near S | Trivial polynomial bound on the number of cuspidal representations of fixed weight and level; uses P081. |
| P067 | A (low) | Choice of auxiliary level, characters and an ordinary Eisenstein eigenfunctional with non-vanishing smoothing factor (Kato §§3–4 type). |
| P069, P082, P090, P091, P099, P101, P103, P104, P107, P108, P126 | R | Each assembles listed children (P082–P089; P087, P093–P095; P091–P106; P107–P108; P109 and P113; P110–P112; P114, P115, P119; P117 and P120; P121–P123 and P128; P126, P129, P130, P135; P115). |
| P071, P078, P079 | R | Existence of twisted level, chain and point data compatible with data already fixed. |
| P072 | R (low) | Construction of channels and symmetric form data; the 3,113-line cone is large for an R. |
| P074, P077, P139, P140 | S | Lattice arithmetic at one prime: uniformiser relations, a level killed by a uniformiser, frame image equals the localised companion lattice, integrality of a scaled coset representative. |
| P075 | S | Elementary ultrametric transfer of non-vanishing between two power series with congruent character sums. |
| P092, P100, P105 | S | The kernel depends only on components at bad places; support and periodicity of the kernel. |
| P095 | S | Local existence of a unitary element that is the identity away from v. |
| P106 | S (low) | Algebraicity and integrality of kernel values away from a finite set of primes. |
| P113, P114, P115, P122, P123 | S | Value of an algebraic Hecke character of U(1) on a level determinant as a product of local tame characters; class-field-theory bookkeeping in project normalisation. |
| P130 | S (low) | Existence of a chart point with frames moved by a level element; companion of P127 (S) and P128. |

### 3.3 Summary

| My grade | Count | Nodes |
| --- | --- | --- |
| R | 32 | 14 top + 18 input-side |
| S | 16 | all input-side, mostly Z4.2 |
| A | 16 | 12 with a base I am fairly confident of; 4 (P024, P036, P062, P067) clearly "adaptation, not new" but needing an expert to pin the theorem |
| N-candidate | 4 | P012, P013, P015, P017 |
| Expert needed | 2 | P027, P045 |
| Target | 1 | P010 |

- **Settled:** 64 of 71 (R 32, S 16, A 16). With the four N-candidates counted as a verdict, 68 of 71 leave U.
- **Caveat on project-internal lemmas.** About 30 of the S and R grades sit in Z4.2 and Z4.4 and concern bespoke objects (Ξ_ad, chart points, `AdPins`, `AdTie`). Their statements are routine *given the definitions*; any novelty lies in the definitions of the kernel chain, which the skeleton does not grade. A grade such as "routine, definition-dependent" would be more honest than S.

**Best candidates for the new mathematics of this proof**, in order:
1. **P017**, with the unlisted `core_gm` and `windowInequality_of_artinInputs` under it, and P021: the prime-sum bound from lattice-chain data.
2. **The proof of `TopG` and the host supply**: `shape_closed_link_n_of_green`, `forall_goal_of_shape_of_hyps`, and `supplyChi : VWinAt ψ 401 → HostExW (3/2) …`. These sit in P015's 185,028-line exclusive cone and are not nodes.
3. **P013**: the Selmer window, with the count bounds `CountI`–`CountV` that appear only as hypotheses of P020.
4. **Inside P012**: `nonempty_hyps_definite_side_of_closed_bound` (the `HypsAlt` data) and `topCovolSlim2_use_alt_alt` (the covolume bound).
5. **P022 / P023**: the windowed Landau criterion. Small, self-contained, and checkable by hand.
6. Lemma level: P027, P045, and the quantitative form of P044.

## 4. DAG

- **Witness paths.** All 43 paths (320 hops, 155 distinct) were checked two ways. Every hop is an edge of the independent dependency cache used by `graphq.py`: 320/320. For every distinct hop, the target's name occurs in the source declaration's proof body (text after `:=`) at the pinned commit: 155/155. The text check is by short name, so it is weaker than the cache check; together they are strong.
- **Direct dependencies.** 115/115 edges between cone nodes are present in the cache once wrapper aliases are folded (for example `K4.top` through `kato_eulerSystem_integrality`, `P090` through `adelicChainDatum_characterLaws_jointKernel`). The 8 edges out of the five `Main` declarations are outside the cache's cone and were confirmed by reading `Main.lean` and `MainTheorems.lean`.
- **Proof terms read by eye (about 25 edges):** P001–P005 → P006–P009; P009 → P010; P010 → P011; P011 → P012, P013; P012 → (helper) → P014; P014 → P015; P015 → P016; P016 → P017, P018, P019; P018 → P023; P026 → P053, P058, P062, P063, P065, P066; P053 → P068; P065 → P067; P080 → P090.
- **Bookkeeping.** Input distances are consistent with the edges (no node has a parent contradicting its distance), the 140-node subgraph is acyclic, and the longest path from an input root is 7 edges, as stated.
- **What the DAG leaves out.** Edges to theorems outside the R18 catalogue are dropped, and at the top these are the largest branches:
  - P010 also uses `galoisLocalGlobalStrong_recParameter` (the proof of `Row0b`).
  - P011 also uses `recTExists` (local Langlands for GL_n).
  - P013 also uses `baseChangeN`.
  - P015 also uses `supplyChi`, `shape_closed_link_n_of_green`, `forall_goal_of_shape_of_hyps`.
  - P012 records no direct subordinate at all, although its proof term names about 25 theorems.

  These are not errors under the stated edge convention, but the picture drawn in the document omits most of the proof.

## 5. Is this a sound table of contents for a 100–150 page main paper?

**Not yet.** It is a sound and well-verified *index of the 20 inputs*, and its top spine (P009 → P010 → P011 → {P012, P013}; P012 → P014 → P015 → P016 → {P017, P018, P019}; P018 → P023 → P022) is the right opening chapter. What is missing is the middle.

**The numbers.**
- The cone has 9.57M core lines: 2.09M shared, 7.03M exclusively owned by the 140 nodes.
- Of that 7.03M, four U nodes own 6.90M: P012 5,666,153; P010 761,324; P013 285,082; P015 185,028.
- The other 136 nodes together own about 134K lines in the historical graph index.
- An earlier backward dominator tree (`backward_tree.md`) lists 1,099 theorems that each dominate at least 5,000 lines. Only 17 of them are skeleton nodes, and only 27 are in the R18 catalogue at all. The skeleton and the bulk of the proof are nearly disjoint.
- Coverage is uneven: Z4.2 has 50 nodes and Z4.4 has 27, while Z1.1, Z1.2, Z2.K1, Z2.K5, Z2.K6, Z2.K8, Z4.1 and Z4.3 have one each.

**What must be added before this can organise a paper.**
1. **Split P012** along its own proof term. At minimum:
   - `every_character_of_theta_integrals_local_matching` (dominates about 3.69M lines) and under it `nonempty_hyps_definite_side_of_closed_bound` (about 2.96M) and `hypotheses_nonempty_of_unramified_exponents_alt` (about 1.69M);
   - `topCovolSlim2_use_alt_alt` (about 0.57M), the covolume bound;
   - `published_results_eigen`, `published_results_first`, `published_results_arithmetic`, each a bundle of dozens of literature statements.

   These are the chapter headings of the theta and Arakelov side. The literature bundles need a table of their own with L grades and citations, since P012's cone is where the literature side lives.
2. **Split P010.** Its cone is the proof of `Row0b` by `galoisRepresentations_of_thetaLift`. The statement is published (Galois representations for polarised regular algebraic cuspidal representations over CM fields, with local-global compatibility: Harris–Taylor, Shin, Chenevier–Harris, Caraiani *[memory]*) and should be an L node. Whether the theta-lift route is itself new is a separate question that an expert must answer. `recTExists` and `baseChangeN` need the same treatment.
3. **Split P013 and P015** at `automorphic_window_of_inputs`, `vwin_of_hypotheses_H_E_alt`, `supplyChi`, and the `TopG` proof. These are candidates 2 and 3 of §3.3 and currently have no statement paragraph.
4. **Add the definitions as first-class entries.** `VWin`, `WinPair`, `IsChiField`, `TopG`, `HostExW`, `ChainTied`, `HypsAlt`, `LinkN`, `Closed`, `Level.Gm`, `LemmaK`, `CountI`–`CountV`. A reader cannot judge P013–P017 without them, and several are where the novelty sits.
5. **Go below depth 7 only where it pays.** The strict catalogue graph ends at depth 7, so "depth 8 costs nothing" is true but uninformative. The 112 unread helper lemmas on the witness paths (for example `core_gm`, `lemmaK`, `glue2`, `theorem_n5_of_ring_inputs`) matter more than further catalogue depth, and the document's own estimate is about 25 minutes of reading.
6. **Prune for the paper.** Most of Z4.2 and Z4.4 (about 75 nodes of equivariance and lattice bookkeeping) belongs in an appendix as one proposition each ("the adelic kernel Ξ_ad satisfies the laws `AdLawAt`"; "standard column data exist"), not as 75 contents entries.
7. **Fix the grading scheme.** Give proof-role R to wrappers; add a "target" grade for P010; add "routine, definition-dependent" for project-internal lemmas; apply the regrades of §2 and §3.

**A workable outline** from what exists plus the additions above:
1. Statements and the windowed Landau criterion (P001–P009, P018–P023).
2. From lattice chains to prime sums (P016, P017, P019, P021, `core_gm`).
3. Family connectedness from Selmer bounds (`TopG`, `supplyChi`, P015).
4. Selmer windows (P013, P020, Z1 and Z2).
5. The theta and period side (P012, Z3 and Z4).
6. Heights and covolume (Z5, `topCovolSlim2`).
7. Literature inputs, with `Row0b` and local Langlands.

Chapters 2–4 are where a reader would look for the new mathematics, and they are the thinnest part of the current skeleton.
