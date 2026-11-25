AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

# R4_review_Z1Z3

AI review report produced during this project; file names are internal working names.

- Internal source file: `out/R4_review_Z1Z3.md`
- SHA-256: `df0e87d509f8162576a007f109e7d292a226540a1366649c8fd9fc7fed15c804`
- Report scope: Round-4 independent review: Z1.4 and Z3.2

## Internal report

The report below preserves its original verdict, scope and unresolved points. Historical review-machine home prefixes are displayed as `${REVIEW_HOME}`; the source checksum above identifies the original report. Source line numbers in other records count from its original title.

# Round-4 independent review: Z1.4 and Z3.2

Reviewed text: `${REVIEW_HOME}/work/prev4/ch_P.tex`, Z1.4 at lines 9945-10463 (`sec:P-z14-full`, plus the earlier statement material at 9313-9431, 9682-9697, 9856-9888) and Z3.2 at lines 8513-8757 (`sec:P-r4-Z32`, plus 7551-7627). Summary rows: `P_notes.md` lines 27-28.

Checked against: cleaned Lean copy `${REVIEW_HOME}/src/rh/src/`, the original tree (via the device shell, for files missing from the cleaned copy), and the dependency graph (`graphq.py`, plus cone/reachability scripts in `${REVIEW_TMP}/r4z1z3/`).

What "checked" means here: I compared every Lean statement named below with the text, read the top-level proofs (`main_holds`, `core_holds`, `low_holds`, `up_holds`, `mprime_holds`, `model_lower`, `rowTie_disp`, `dimLx_of`, `count_eq`, `rowCup`, `open_inputs_at_normalized`, `SelmerBoundAtPoint.main`, the two downstream sites), recomputed the constants, and tested the labels by graph reachability. I did not read the full cones line by line (Z1.4 upper cone is 1,266 declarations, Z3.2 is 4,605).

---

## Z1.4 - graded model and the factor two

### Verdict: COMPLETE WITH GAPS

The statements match Lean, the constants follow, and I found no mathematical error. The gap is in criterion 1: several steps that carry real weight are asserted in a phrase, with no proof, no earlier blueprint item, and no "Proved in Lean, not reproduced" label.

### 1. Is "complete" earned? Steps asserted without proof or label

1. **The multigraded Euler-characteristic calculus.** The intersection calculation uses these as one-line facts:
   - eventual nonnegativity of chi ("the remaining Euler term is eventually nonnegative", "nonnegativity of the kernel module");
   - additivity on short exact sequences;
   - independence of the order of sections ("by additivity, or by taking the two orders of homology");
   - "the eventual Euler upper-bound rule for quotient by sections";
   - chi equals the alternating difference of Hilbert functions for small annihilator (used inside "peeling").

   In Lean these are `rulePos`, `euler_additivity_of_rules`, `euler_rule_two_of_graded_finite_iso`, `ruleUB`, `ruleSmall`, with `ruleGr`, `ruleFin`, `ruleIso`, `ruleDev`, `ruleIrr`, `ruleShift`: about 3,600 lines in `Formalism/SharpRestriction/.../NoetherianQuotientCalc/`. They appear nowhere else in the chapter (the only other `HidaSetting` hit, line 2799, is unrelated). The text cites only the definition of `chi`. This is the largest unlabelled block.
2. **The Herbrand-type formula** (`th_holds`, 10383-10393): cokernel minus kernel length of multiplication by `a` equals the sum of localized length times `v(sigma a)`. It is given as a four-line filtration sketch; the finiteness of the kernel and cokernel lengths and the norm-valuation identity for a horizontal prime are asserted.
3. **The support check** (10254-10302, `zi/zii/ct/zm/zp/admissibility_holds`, `eventually_mQ_gr_finite_annihilator`). The use of M3 is correct as far as I can follow, but the construction of the two one-sided points from a relevant prime ("retain a surviving section, kill the opposite weights and pass to a geometric point of the localization") and the passage from radical containment to a power are not written out.
4. **Representability of the local and global deformation functors** (9958-9982). The text proves the finiteness hypothesis but asserts the representing ring ("one represents the unconstrained local lift"). `exists_uLoc`, `exists_ring`, `exists_model` have cones of 962, 6,860 and 7,892 declarations.
5. **The framed presentation** (`lemmaP`, `boxPres`; 9984-10007): successive lifting and the obstruction-dimension bound are sketched in outline only.
6. **Point and tangent convergence** (10029-10056): "as in the cited proof" for the comparison on degree-zero integral values.
7. **Two-sided classification** (`twoPt_shape`): only its isomorphism clause is argued (10129-10144). The type I / type II dichotomy used at 9461 is cited, not proved.
8. **Published theorems used without a label or reference:**
   - class field theory ("factor through the class group by class field theory", 10068-10070, and the additive version at 10086-10088); Lean proves this as `Kum.artKer`, cone of 6,010 declarations;
   - "the weight-zero finite local condition gives an unramified class at ell" (10083-10085); Lean takes this from `CohInp.loc` via `Loc.z1fUnr`, and the text does not say so (the negative-weight case does say "by the character clause of the local input");
   - crystalline period-ring facts: the cones of `pt_fixed`, `bloch_kato_nonpositive_weight`, `exists_ring`, `exists_model`, `vlen_le` all reach `GlobalTheory.T.fontaineBcrisBasicTheorems_proof` (filed on the literature side of the graph) through `exists_crystalline_period_matrix_bcris_of_isCrys`. The section never mentions it.
9. **Delegated, and said so:** that tangent classes at the base satisfy the finite local condition (`tanCoc_isBK`, needed for `PtHyp.rigid0`) is left to Z1.2 (9667-9670). This is consistent with "complete under the common arithmetic input", but the reader of Z1.4 alone would not see that M1 depends on it.

Steps that are written out and that I checked: the lower lemma `mprime_holds` (9856-9888, complete and correct); the Smith normalisation; the `phi(a) != 0` modification; the slice argument and finiteness of the cover; cyclicity and reducedness of the localized weight pieces; the squaring factor; the leading-term count; the final cancellation.

### 2. Statements versus Lean

- `LemmaM` (`OrbitVanishingLocal.lean`): three conclusions (a cover exists; `cotLen != top`; bound for every cover `T`), with `2 * sum v(xi a)`. The text agrees, including "for every cover" and the empty cover.
- `M1`-`M5`, `Covers`, `Eqns`, `mDims`: agree with the prose at 9354-9406 and 10015-10020. Parameters `(r,s,r',s',m) = (u(-1)+2, u(-2)+1, u(1)+3, u(2)+1, u(0)+3)` match `ModelOfPres.lean` exactly; list sizes `r+1, s, r', s', m` and chart multiplicities `r, s, r'+1, s'+1, m` match.
- `LemmaM'` and `mprime_holds`: agree.
- `model_lower`, `model_upper`, `soBar`, `bloch_kato_nonpositive_weight` (all `j <= 0`), `pt_fixed`, `sha_inj` (modulus exactly `b`): agree.
- Rees data: `N_2 = B F_*^2 + N_0^2 N_1` and the section list match `mN`, `tsF`, `tsR`.
- Minor: the section has no theorem environment or `\lean{}` tag for `main_holds`; the statement lives in prose at 9688-9695. The ambient hypotheses of `LemmaM` (complete DVR of characteristic zero, `IsWRing`: generation in weights +-1, +-2 over `A_0`, `x` zero on nonzero weights, `IsCO` for `A_0`) are used but not restated; "group monomials into weight +-2 factors" silently needs the weight restriction.

No mismatch in hypotheses, quantifier order or constants.

### 3. Proofs

No error found. Constants recomputed independently:

- Hilbert series `1/((1-X)^r (1-X^2)^s (1-Y)^{r'+1} (1-Y^2)^{s'+1})` at `(u,w) = (2d_0+4d_2, 2d_1+2d_2)`: matches `hf_holds` / `cnt`.
- Mixed difference: `(1+X)^{r-1}(1+Y)^{r'}(1-X^4Y^2)/((1-X)(1-Y)(1-Y^2))`, eventual value `2^{r-1+r'}`; times `sum 2c_i` gives `2^{r+r'} sum c_i`. Matches `num_holds`, `low_holds`.
- Upper side `2^{r+1+r'}` from `r+1` squares `F_i^2` and `r'` squares `E_i^2`: matches `locLen_aPiece_ideal2_le_two_pow`, `up_holds`.
- Chain in `core_holds`: Nzd, then permutation, then `ruleUB`, then the quotient isomorphism. The inequality direction in the text (10377) is the Lean one.
- `F_*` in the saturated square gives negative total at least 4 for `F_*^2`: correct, and it needs the cut chart (no weight-zero variables), which the text does use.
- Weight-zero cocycle argument, the `-c(cc)/2` primitive, the diagonal intertwiner and the square-root case, the degree derivation `D(f) = -2`: all correct.

### 4. Labels

The section itself carries no "[Hypothesis, discharged at ...]" label. The related ones at 9620-9637 and in the notes row:

- `Alg.M.main_holds`, `Alg.M.mprime_holds`, `Alg.lemmaP` consumed at `SmallClassNumbers/CorGKOf.lean:15-18`, and `cohInp_alt` at line 13: **correct in the original tree** (I read the file).
- That file does not exist in the cleaned copy, and the graph lists the callers as `count_i_of_printed_bound_k_kato_automorphy` (`LinkedUnlE.lean`, same expression at cleaned lines 333-336), `count_v_of_printed_bound_k_reduced_unitary_lift`, and `countII_and_countIII_of_printsH_of_sp4In`. So `graphq callers` will not confirm the cited path; the citation and the graph refer to different layouts of the same code.
- `main_holds` (1,266 declarations) and `mprime_holds` (33) have no literature node in their cones: they are unconditional theorems, as claimed.
- `cohInp_alt` needs `LiteratureRankNHypothesis` and `exists CK, LemmaK CK`; the text's "bounded LemmaK of Z2, normalized Poitou-Tate, local finiteness and duality" matches the hypotheses of `soBar`.
- `PtHyp` (M1, M3, M4) is supplied by `ptHyp_of_autB_of_lemW_of_isBase`, which calls `pt_fixed` and `bloch_kato_nonpositive_weight` and takes `KatoTwoW` and both rigidity cases. "Under the rigidity supplied in Z1.2-Z1.3" is accurate.

### 5. Understanding

The text does explain why the result holds. The cotangent length at the base is turned into an intersection number on a three-graded Rees algebra, which is then computed twice. From below, the Smith exponents of the weight -1 equations appear because squaring `pi^{c_i} y_i` lets one peel `2c_i` copies of a reduction whose Hilbert function is an explicit monomial count. From above, adding the trace element `a` leaves only the finitely many two-sided orbits, where each weight piece is cyclic and reduced, so each squared equation costs at most a factor two. The two powers of two differ by exactly one factor, which is the 2 in the theorem. The remark that the bound holds for every cover, and why that matters for irredundant representatives, is a real explanation. What a reader does not get is why the Euler characteristic behaves as claimed (positivity, order independence), since that machinery is invoked rather than explained, and the arithmetic half (9948-10190) reads as a dense list of checks rather than an argument with a visible shape.

### Most important problems (Z1.4)

1. The Euler-characteristic calculus (about 3,600 lines of Lean, five rules) is used unproved and unlabelled; it should be recorded as "Proved in Lean, not reproduced" and is missing from column A of the notes row.
2. `th_holds`, the support check, deformation-ring representability, `lemmaP`/`boxPres` and `twoPt_shape`'s dichotomy are sketches, not proofs, and are not labelled either.
3. Unlabelled published inputs: class field theory, the unramifiedness of weight-zero finite classes at ell (from `CohInp.loc`), and the crystalline period-ring theorem reached by `pt_fixed` and `bloch_kato_nonpositive_weight`.
4. The cited consumer path `CorGKOf.lean` cannot be confirmed with the graph or the cleaned copy (it is correct in the original tree).
5. No formal statement of the lemma in the section; ambient `IsWRing` hypotheses are implicit.

---

## Z3.2 - local arithmetic comparisons

### Verdict: COMPLETE WITH GAPS

The five comparisons are stated correctly and track the Lean proofs closely; I found no mathematical error. The result is conditional on the public hypotheses of `SelmerBoundAtPoint.main`, which the text says. The gaps are a headline declaration that is not on the proof path, a label that overstates what is discharged, and a few one-sentence steps.

### 1. Is "complete" earned? Steps asserted without proof or label

1. **Identification of the row quotient with the public colength** (8549-8551): "the same calculation applies to the image of f, so the two isomorphisms identify the quotient". In Lean this is `len_eq_col` (used inside `rowLenD_eq`), a separate lemma with continuity and bijectivity hypotheses. Asserted.
2. **Induced surjection of lattices** (8530-8531): "finite freeness, spanning and equivariance give the induced surjection" is `latHom_onto`. Asserted.
3. **Integral annihilator step** (8572-8577): that the strict condition on the torsion image is the annihilator of the integral `F_{s,w}` is one sentence ("integral Tate duality detects the kernel"). This is the content of `bk_a_of_admitted_bk_a` / `bka_gen`.
4. **Natural invariant isomorphisms on H^2** (8571, 8593-8596). These come from `Fact T2.Core`, which `SelmerBoundAtPoint.main` builds from its three global hypotheses through `local_duality_class_field_facts_of_artin_tate_euler`. That derivation is neither reproduced nor labelled in this section (line 8052 mentions only its class-number clause).
5. **Crystallinity of the extension on `Y + O`** (8620-8623): "the assumed Fontaine subobject and filtration statements and the crystalline family then make the extension crystalline with jumps among those of the family" compresses `ytEmbW_of`, `jump_pi`, `ytTarget_of`.

Written out and checked: the decreasing-kernel argument; finite classes map to finite classes; the cochain calculation for `J_w`; the Baer extension; the transport to `U_e`; the compact-image denominator argument; the stable lattice; the telescoping dimension count.

### 2. Statements versus Lean

- **Row bound.** `RowAt` gives `F.ColLe PD lenw`; `rowTie_disp` concludes `rowLen n != top` and `rowLen n <= b * lenOl`. Text: "integers m, k with colength m, k = length_O(O/lO), m <= b_w k". Agrees.
- **`TBAt`.** Three clauses: `p^{cB}` times the orbit cocycle lies in `HfD`; for `e > 0` the finite locally constant cocycles are coboundaries, for `e = 0` they equal unramified plus coboundaries; length bound `(finrank Qp K + 1) * cB * lenOl`. Text: `l^{c_B}`, zero / unramified, `([E_w:Q_l]+1) c_B a`. Agrees. `U_e` is `divisibleCocycles` (locally constant torsion cocycles). Agrees.
- **`finrank_Ff`.** Lean: `finrank_O (F_f / torsion) = finrank H^1_f`. Text: "rank_O F_f = j_w". Same thing, but the text does not say rank is taken modulo torsion.
- **`DimLx`.** Lean target is an inequality, `rank(L_x / im D) <= j_w + dim ker D`. The text derives an equality and then says "upper bound". Consistent.
- **Hypothesis status slightly misdescribed** (8717-8718): "the coefficient-splitting and Bloch-Kato dimension hypotheses". `BlochKatoDim` is a hypothesis (`admBK`), but `Splits` is proved (`LargeLevelLemmas.splits_coef`).
- `H^0(W) = 0` "by the local gain assumption" is a clause of `admG2`. Agrees.
- `bkAAt` (annihilator hypothesis) requires `IsDR` and `IsDual1`; the text's "de Rham representation and its paired dual" agrees.

Notation: `e = c-1` in 8610 against `k = c-1` in the table at 7529; `P` in the text is `E` in Lean. Harmless.

### 3. Proofs

No error found. Specific checks:

- Off-Z dimension (8706-8726) follows `negdim_eq`, `count_eq`, `rank_le_count`, `dimLx_of` step for step: common lower index (Lean uses `min loV loW`), equality of negative multiplicities, Bloch-Kato formula on both sides, `H^0(W) = 0`.
- Character jumps nonnegative: `GainBoundAt` gives jump `c-1 >= 0`. Correct.
- `rowCup`: the pairing `T_1 x Y -> Y(1)`, equivariance by `key_mul`, `y_g` as coboundary of the projector in `A`, injectivity on H^2 via `h2Map_injective_statement`, `Y` finite as a submodule of `A` (`clause4`). All as in the text.
- Rank computation: kernel of `F_f -> H^1_f(W)` is torsion (clear a denominator of the primitive), image is everything after inverting (compact image, one denominator). Correct.

### 4. Labels

Label under test (8727-8728): "[Hypothesis, discharged at `open_inputs_at_normalized` and `theorem_n5_of_open_b` for the normalized Selmer calculation.]"

1. **`tieRow_disp` is not on the proof path.** The notes row and the text (8559) name `tieRow_disp`. It exists in the original tree (`FiniteClassesRowEqGeneric.lean:161-171`, a wrapper over `rowTie_disp`) but has **0 hits in the dependency graph** and is absent from the cleaned copy. The path actually used is `rowTie_disp` (102-157) -> `rowTie_S` -> `row_match_from_comparison` -> `plugOpen3_B` -> `theorem_n5_of_open_b`. The cited range "139-171" starts in the middle of the proof of `rowTie_disp`.
2. **Each lemma reaches only one of the two sites.** By graph reachability:
   - from `open_inputs_at_normalized` only: `finFf_of`, `rankFf_normAt` (via `hRho_rN`), `tbTarget_row`, `tbLen_w`, `lenMap_of`, `ytTarget_of`, `rowSub_at`, `rowMat_SN`;
   - from `theorem_n5_of_open_b` only: `rowTie_disp`, `rowCup`/`bridgeRho`/`cupKillAdm`, `cup_iff`, `bk_a_of_admitted_bk_a`, `im_le_Fs`, `liftCol_eve_Dd`, `liftCol_evE_Dd`, `dimLx_of_font`, `negX_of`, `finX_of`.

   Together they cover everything, and both feed `theorem_n5_from_inputs`, so the label is right as a pair. But it is attached to the dimension statement, which is consumed only at `theorem_n5_of_open_b` (via `colLx_of_ringDef` -> `colLx` -> `plugOpen3_B`).
3. **`unramified_input_of_admitted` is consumed at neither site.** Its only caller is `SelmerBoundAtPoint.main` itself (`SelmerLengthBoundAtPoint.lean:23-28`), one level above `theorem_n5_from_inputs`. The text at 8743-8746 describes it correctly as a public hypothesis, but the citation at 8686 sits inside the "integral columns" list as if it were part of that calculation.
4. **"Hypothesis, discharged" overstates.** What happens at those two sites is consumption of proved lemmas. The real hypotheses are those of `SelmerBoundAtPoint.main`. At the two downstream sites named in the notes:
   - `boundAtPoint_all_localisations_of_objectConditions` derives only `BlochKatoAnnihilators` (from `BlochKatoLocal`, local Tate duality, local Euler characteristic), Tate H^1 finiteness, `UnramifiedTrivialH1f` and `adm51`. Everything else (`admG1`-`admG6`, `admBK`, `admTB`, `LengthBoundAtPlaces`, `LiftExponentAtPlaces`, `FamilyContinuous`, `SemisimpleDecomposition`, `FontaineAtPlacesOverL`, `LocalCoefficientCompatibility`) is taken by destructuring its own `admitted` hypothesis.
   - `splitCase_bound_at_point_of_admitted_items` takes all of them, including the annihilator, finiteness and unramified clauses, from `EmbeddingTypes.admitted`.

   So `RowAt`, `TBAt`, the Fontaine clauses and the Bloch-Kato dimension formula, which this section calls "assumed", are still hypotheses after both sites. Lines 7612-7627 say this honestly ("come from the admissible instance quantified in its statement"); the notes row ("premises are given at ...") reads stronger than that.
5. Both sites are the only two callers of `globalLatticeIndexTheorem_of_lengthBoundAtPlaces`, hence of `SelmerBoundAtPoint.main`: confirmed. `globalArtinReciprocity_holds`, `Gcoh.top_tate`, `Gcoh.top_euler` exist; the first is on the literature side of the graph.
6. Line ranges otherwise check out (`rowCup` 20-59, `finFf_of` 894-904, `rankFf_normAt` 58-63, `dimLx_of_font` 582-589, `open_inputs_at_normalized` 74-93, `theorem_n5_of_open_b` 351-363).

### 5. Understanding

The section explains what each comparison is for and mostly why it holds. The common idea is stated and visible: every local condition is defined in a period model, and a group isomorphism plus a coefficient isomorphism carry cocycles, coboundaries and witnesses back and forth, so each public hypothesis can be applied to the concrete lattices of the determinant argument. On top of that there are three real arguments, each understandable from the text: the row error pairs to zero with `J_w` because `g -> (u(g)-1)P` is the coboundary of `P` in the ambient algebra and the map on H^2 is injective; the character blocks are handled by building an explicit extension on `Y + O` and feeding its orbit difference to the trivial-bound hypothesis; the off-Z dimension equals `dim ker D + j_w` because the extra characters have only nonnegative jumps, so they do not change the negative part of the filtration. What stays opaque is the first block: the reader is told that two isomorphisms identify the quotient with the public colength, but not why the identification respects the finite conditions on both sides in the integral setting.

### Most important problems (Z3.2)

1. The headline declaration `tieRow_disp` is outside the dependency cone; the proof path goes through `rowTie_disp` -> `rowTie_S`. The notes row and line 8559 should not present it as the closing theorem.
2. The label "Hypothesis, discharged at ..." marks consumption of lemmas, not discharge of hypotheses. `RowAt`, `TBAt`, Fontaine and Bloch-Kato dimension remain hypotheses at both downstream sites (taken from `admitted`); only the annihilator, Tate finiteness, unramified H^1_f and `adm51` are derived, and only in the all-localisations branch.
3. `unramified_input_of_admitted` is applied in `SelmerBoundAtPoint.main`, not at either labelled site.
4. Unproved one-line steps: `len_eq_col`, `latHom_onto`, the integral annihilator identification, and the existence of natural H^2 invariant isomorphisms (`T2.Core`, derived in Lean from the three global hypotheses, not labelled here).
5. Small inaccuracies: `Splits` is called a hypothesis but is proved; "rank_O F_f" is rank modulo torsion; the range "139-171" for `tieRow_disp`.
