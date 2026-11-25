AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

# R5_review_C

AI review report produced during this project; file names are internal working names.

- Internal source file: `out/R5_review_C.md`
- SHA-256: `db28c39baf686e374f8f28cd6d16d59a4da59d2d7c7456ed0a8b7323e3de9789`
- Report scope: Round-5 independent review C: Z1.1.04, Z1.2, Z1.3.06, Z1.3.07

## Internal report

The report below preserves its original verdict, scope and unresolved points. Historical review-machine home prefixes are displayed as `${REVIEW_HOME}`; the source checksum above identifies the original report. Source line numbers in other records count from its original title.

# Round-5 independent review C: Z1.1.04, Z1.2, Z1.3.06, Z1.3.07

Checked against the cleaned Lean copy `${REVIEW_HOME}/src/rh/src/`, with line ranges spot-checked against the read-only original (`${LEAN_SRC}/`) and callers checked with `graphq.py`. Blueprint text reviewed: `ch_P.tex` lines 11964-12020 (Z1.2), 12362-12389 (Z1.3.06, Z1.3.07), 12448-12477 (Z1.1.04), the map entries at 11604, 11637, 11640, and the unit rows in `ch_Z.tex` 607, 611, 617, 618.

| Unit | Verdict |
|---|---|
| Z1.3.06 | COMPLETE CONFIRMED |
| Z1.3.07 | COMPLETE CONFIRMED |
| Z1.1.04 | COMPLETE CONFIRMED (minor wording and reference gaps) |
| Z1.2 | NOT COMPLETE in the scope the text claims; the narrow Lean implication (part 2) is COMPLETE WITH GAPS |

Line numbers quoted from the Lean source are those of the original tree unless marked "cleaned"; the cleaned copy is offset by a few header lines in some files.

---

## Z1.3.06 Specialize the local test to the global cocycle

**Verdict: COMPLETE CONFIRMED**

Lean: `GlobalTheory.KZ.zetaSysU_of_halves2`, `ZetaElementsUnramifiedOrdinaryOfEulerSystemInert.lean:36-41`.

1. **Complete earned?** Yes. The Lean proof is three lines (introduce the data, destructure the global existential, apply the local universal statement to the same witnesses). The text writes out exactly this. No step is asserted without proof.
2. **Statement.** Matches. `ExistsZetaEulerSystemIwasawaData Pin` gives `∃ c y S' ν χ Z, Sys W c y S' ∧ IwSys2 c A ν Z ∧ SpLink A e χ Z y ∧ Pin e A W c ν χ Z`; `ZetaEulerSystemNonvanishing Pin` quantifies over all six and concludes `NzAt W A y`; the conclusion `ZetaSysUr2` is `∃ c y S', Sys W c y S' ∧ NzAt W A y`. Quantifier order (`∀ l Ω ι e S A W g, Nf → SrcUr → …`) is as in the text. `NzAt` is `∃ s ∈ Ine A, cycBar s = 1 ∧ mat W s 1 1 = 1 ∧ y s 1 ≠ 0`, as the text says with indices 0,1.
3. **Proof.** Correct. The remark that the dependence on `y` enters through `SpLink` although `y` is not an argument of `Pin` is accurate.
4. **Label.** "Hypothesis, discharged at the application" is correct. The only caller of `zetaUr_of_halves2` (hence of this unit) is `UpperTheory.V.Z.Kato.Final.zetaUr`, `UnramifiedZeta/ZetaUr.lean:9-12`. There the global half is `Kato.Joint.kato_global_unit_law_of_smoothed_classes` applied to `Kd.K4.kato_eulerSystem_integrality`, `Kato.K5.smoothedZetaClass_hodgeTateLaw` and `GlobalTheory.T.exists_admissible_hecke_projection_nonvanishing`, whose result type is `ExistsZetaEulerSystemIwasawaData Pin7`; the local half is `Kd.C7.pLocu`. This is what the text states.
5. **Understanding.** The text explains the one point that matters: the local nonvanishing must be applied to the very cocycle produced globally, and this is possible because the local statement is universal over the tuple while the global one is existential. That is the whole content.

Minor points
- The text says "an integer $e\ge0$"; `Nf` contains `e_pos : 1 ≤ e`. Harmless, since `Nf` is retained as a hypothesis.
- Map entry 5 (line 11634) writes the nonvanishing coordinate as $y(s)_2$ (1-indexed) while the unit text uses indices 0,1. Notation only.

---

## Z1.3.07 The inertia witness excludes the Greenberg condition

**Verdict: COMPLETE CONFIRMED**

Lean: `GlobalTheory.KZ.zetaUr_of_halves2`, same file `:43-46`, via `zetaElementsUnramifiedOrdinary_of_eulerSystem_inertia` (`:18`), `es_of_sys` and `not_gr_of_nzAt` (`IsLocallyConstantCycMod.lean:40-48`).

1. **Complete earned?** Yes. Every step is written out.
2. **Statement.** Matches `ZetaUr`: `∀ … Nf e S A W → SrcUr ι e A W g → ES W A`. `Gr W A c` is `∃ x, ∀ s ∈ Dec A, c s 1 = mat W s 1 1 * x - x`, exactly the displayed equation. `ES` is `Sys` with `¬ Gr W A y` inserted between `Unr W y` and the tame clause; the text's count of "five other pieces" (integral matrices, cocycle, integral coordinates, `Unr`, tame clause with the same quantifiers) is correct.
3. **Proof.** Correct. `not_gr_of_nzAt` uses `Ine_le_Dec`, `mat W s 1 1 = 1`, and `y s 1 ≠ 0`; the cyclotomic clause of the witness is discarded (`-` in the `obtain`), as the text notes.
4. **Label.** Correct; same single caller `Kato.Final.zetaUr` as above.
5. **Understanding.** Adequate: a Greenberg primitive $x$ gives $y(s)_1=(W(s)_{11}-1)x$ on the decomposition group, which is zero at an inertia element where the quotient character is 1, while the Euler-system class was built to be nonzero there.

No problems found.

---

## Z1.1.04 Building the rank-three seed in a specified weight class

**Verdict: COMPLETE CONFIRMED** (with the minor items below)

Lean: `UpperTheory.V.Z.Sym.W.adjoint_lift_from_eisenstein_of_propagation : PropEGW → SeedInW → AdAutW → UnitaryThreeAutomorphyDense`, `AdjointLiftFromEisensteinSeedOfHyps.lean:184-281`.

1. **Complete earned?** Essentially yes. I followed each paragraph against the Lean proof and its supporting lemmas:
   - Weight choice and characters: `hη2`, `hηc`, `hηL`, `hθL`, `hsp`, `hφ1`, `finOrder_of_kills`, $t=B+k_0+2$, $m=j+(\ell-1)t$, `hpar`, `hΦΨ`, square witness. All written out.
   - Open irreducibility of $\rho$: `Sd.sI` (`NormOneOfFin.lean`), `Sd.eisReg` (`EisReg.lean`), `core` and `Sd.sIabs` (`LineOfNotIrr.lean`). The text's argument (normal core; regular inertia element in $H$; translates of an $H$-line are eigenlines; non-preserving elements have trace zero so $\Phi\equiv-1$; preserving elements times an interchanger give $\Phi\equiv1$; hence $\Phi^2\equiv1$ everywhere) is the Lean argument.
   - Open irreducibility of the adjoint: `ad0Irr_factor`, `ad0Irr_core`, `Sd.ad0Irr` (`Ad0IrrMulVec.lean`). The Veronese vector $(x^2,2xy,y^2)$ is the right one for `symSquareMatrixHom`; the plane case and the line case (via the invariant pairing) are both treated, as in Lean.
   - Seed conditions: `ad0Facts` (continuity, form, away type, flag, residual sum), `exists_symmetric_pairing_adjoint_zero`, `order_at_adjoint_zero`, `ordAt_change`, `resFacts`, `shapeFacts`. The polarization identity $R(s)^tPR(c)R(csc^{-1})=PR(c)$ checks.
   - Automorphy: `hIn` (SeedInW) then `hadj` (AdAutW), `adjoint_zero_twist`, `mkCsdW'`, `AllW.witA`, `Birth.potOrd`, `potOfFlag` (`flag_exp`, `pow_fix`, `cyc_inf_over`). The text's exclusion of $\kappa_i^k=(\kappa_j\epsilon)^k$ matches.
   Steps stated without proof, reference or label (all standard, none affects correctness):
   - (a) "each finite cyclotomic level is totally ramified, every action on its primitive root lifts to absolute inertia" (surjectivity of the cyclotomic character on inertia above $\ell$; Lean `CycInertia.exists_mem_Ine_toZModPow`, `cycZ_Ine_surjective`). The compactness half is written; total ramification of $\mathbb Q(\mu_{\ell^r})/\mathbb Q$ at $\ell$ is assumed.
   - (b) "The image of $G_L$ in $G_{\mathbb Q}$ is open and the restriction is a homeomorphism onto that image" (Lean `resFacts`).
   - (c) Existence of an infinite-order $\ell$-adic unit and of a valuation subring above $\ell$ are used silently (`exists_unit_infinite_order`, `eisReg_place`).
2. **Statement.** Matches `UnitaryThreeAutomorphyDense`: field-pair conditions, `χ' ≠ η`, `M ≠ 0`, `2*l ∣ M`, `UnrSplit L M`, inertia condition on $\chi'|_{G_L}$ away from $M$, then `∀ B, ∃ m ≥ B, m ≡ j [MOD l-1] ∧ ∃ r, IrrOpen r ∧ IsSeedAlt ι c (ψ) (τ) ![m,0,-m] (cycBar L Ω l)⁻¹ r` with $\psi=(\epsilon^j\chi',1,(\epsilon^j\chi')^{-1})|_{G_L}$ and $\tau=(\chi',1,\chi'^{-1})|_{G_L}$. Quantifier order is right. The `IsSeedAlt` fields `cont`, `irr`, `pair` are not listed in the opening statement but are proved in "The remaining seed conditions".
3. **Proof.** Correct. Checks: $m\ge t\ge B$, $m+1\ge k_0$, $m\ge2$; parity $(\chi'\eta)(c)=(-1)^j\cdot(-1)=(-1)^{m+1}$ because $\ell-1$ is even; $\Phi(s)^2\not\equiv1$ at the witness; `PotOrd` needs $m_i\ne m_j+1$ for all $i,j$, true for $(m,0,-m)$ with $m\ge2$.
4. **Label.** Correct. Sole caller is `unitary_three_automorphy_dense_of_prints_and_row` (`UnitaryThreeInputsOfLiterature.lean:29`), which supplies `prop_eg_w_of_printed_hida hH` (Z1.1.01), `seedInW_alt hH` (Z1.1.02) and `adjoint_automorphy_w_of_printed_hida_window hH hR` (Z1.1.03). "Complete for the propagation implication" is the right scope.
5. **Understanding.** Good. The reader learns why a single residual square witness forces open irreducibility (dihedral argument with a regular inertia element), why irreducibility passes to the adjoint (an invariant plane or line produces a root of a binary quadratic, hence a line stable under an open subgroup), and why the auxiliary twist from the window hypothesis is harmless (it cancels in $\mathrm{Sym}^2\otimes\det^{-1}$).

Most important problems (all minor)
1. Second paragraph: "The quadratic character $\eta$ has kernel the subgroup for $K$, since $K$ has degree two." The kernel is the hypothesis `η_ker`; the degree-two hypothesis is what gives $\eta^2=1$ (Lean `sq_mem_galOf`). As written the deduction is the wrong way round, and $\eta^2=1$, needed for $\eta(c)=-1$ and for $\chi'\eta\ne1$, is used before it is stated.
2. "Oddness of $\ell$ gives the required parity for weight $m+1$" omits the two facts it uses, `par` ($\chi'(c)=(-1)^j$) and $\eta(c)=-1$.
3. The third clause of `OrdAt` (congruence $\kappa_i\equiv\psi_i$ on the decomposition group) after replacing $\Phi$ by $\Psi$ is not mentioned for the flag above $\ell$; the text only says "exactly the three inertial weights". Lean handles it by `ordAt_change` with `hψ`.
4. Items (a)-(c) above have no reference.
5. Stale status elsewhere: `ch_P.tex` 10421-10426 (older Z1 section) still says "the irreducibility and local-shape criteria … remain inputs", which this unit now proves.

---

## Z1.2 Ordinary adjoint rigidity and the flag at even level

**Verdict: NOT COMPLETE** for the scope the text claims ("Status: complete for Z1.2 under these inputs", covering parts 1-4). For the narrow Lean declaration named in the unit row (part 2 only) the verdict is **COMPLETE WITH GAPS**.

Lean root in the unit row: `UpperTheory.V.Th.adjointLiftingTheorem_of_locPrints_of_core : Loc.LocalPublishedTheorems → DenseThresholdMainCase → AdjointLiftingTheorem`, `AdLOf.lean:104-150`. Note that this root takes ordinary vanishing (`DenseThresholdMainCase`) as a hypothesis. The section additionally claims to prove `DenseThresholdMainCase` (part 1, Lean `core_alt_bis` = `core_of_ord_vanishing_two_phi_all (ordinary_vanishing_two_of_printed_hida hH) (W.phiAll hC)`) and `UnlEndLogNorm` (parts 3-4, Lean `linkedUnlE_alt` then `unlEnd3E`). Neither lies in the cone of the named root.

### 1. Is "complete" earned?

No. The section contains no "Proved in Lean, not reproduced" label at all and one collective "Hypothesis, discharged at the following callers" paragraph. Many load-bearing steps are stated in one sentence with a Lean pointer and no proof, earlier blueprint item, published reference, or label. List:

Part 2 (the named root; text matches Lean `adL_away`, `adL_above`, `adL_triv`, `bkOrd`, `OrdinaryBlock.fin/entry/crOn_ad/desc/bar`):
- P2-a. "The local ordinary crystallinity result applies to the column representation on $U$." This is `Loc.prC` (`PadicHodgeTheory/SnocZeroLastCoordinateLast.lean`, cleaned 345-352): upper-triangular, strictly decreasing inertial weights, no pair differing by cyclotomic implies crystalline. It is a core Lean theorem derived from `LocalPublishedTheorems`, not a field of that record. Not proved, not cited, not labelled; it does not appear anywhere else in `ch_P.tex`.
- P2-b. "its endomorphism representation is crystalline there by the internal-Hom comparison" (`Loc.isCrys_isDR_internalHom`, `AdmHom.lean`). Same situation.
- P2-c. "the finite rank-one character comparison supplies a scalar primitive" (`Loc.z1fChar`, weight $<0$ gives finite cocycles = coboundaries) and "vanishes on inertia by the unramified comparison" (`Loc.z1fUnr`). Derived in Lean from the Bloch-Kato record; asserted here.
- P2-d. "using crystallinity on $U$ to preserve the finite condition under this injection" (`Th.z1fSub`): asserted.
- P2-e. "The prescribed inertia acts trivially by the determinant relations" (`Ws.Eb.relKill`): the reason given in part 1 ("irreducibility implies the matrix span is the whole matrix algebra and the determinant of the given point represents $\rho$") does not say why a determinant trivial on a subgroup forces the irreducible representation to be trivial there.
- P2-f. "compactness puts the representation matrices in a finite field": no argument or reference (Lean `OrdinaryBlock.desc`).
- P2-g. Existence of the open embedding of the decomposition group into the local Galois group with matching inertia and cyclotomic character (`Loc.decEmb`) and the transport of the crystalline-period primitive (`Loc.bkAbove`) are used as facts.
These P2 items are where almost all of the 38,519-line cone sits; the 47 lines of the root and the corner induction are the part actually reproduced.

Part 1 (ordinary vanishing; Lean `nmAbs`, `ordinary_vanishing_two_of_printed_hida`, `core_o_of_literal_automorphy_n`, `count`):
- P1-a. Upper bound $|S_{m,N}|\le Q^{mb+C}$ (`B1`, `b1O`, `oneLevelO`, `dualNO`, `b1absO`). The bullet lists ingredients (local exponents $m(n+\binom n2)(1+d_v)$, auxiliary contribution $\le mn$, "Global duality … cancels the excess terms") but gives no computation, no proof that $C$ is independent of $m$, and no proof of the dual-Selmer statement ("dual classes normalized at complex conjugation descend after killing auxiliary inertia … zero pairing with every power").
- P1-b. Existence and choice of the auxiliary data (Lean `arPl hC`: Taylor-Wiles-type places with Frobenius conjugate to $s_j$ modulo the precision) is not stated as a step at all.
- P1-c. The Hida ideal $J$: "The universal determinant and diagonal characters map to the ordinary Hecke algebra by their relations on dense arithmetic points; the Frobenius coefficients and weight generators give surjectivity"; "the control and norm-compatible module come from this same Hecke datum" (`nonempty_unitaryHeckeData`, `exists_hecke_ideal`, `hecke_ideal_point_properties`, `levelX_of_isJ_unitaryHeckeData`, all taking `HypothesesH'`). Asserted. The text does not say which fields of `HypothesesH'` are consumed here.
- P1-d. Lower bound: "The weight-fibre annihilator provides $t_0$ with $x'(t_0)\ne0$, and the support of the module gives an eigenfunctional nonzero on some $m_0$" (`etOf`, `has_operator_statement`): asserted.
- P1-e. Existence of the universal ordinary determinant ring for the enlarged residual datum (`b0Ex (phiAll hC)`), of the weight algebra object (`lamEx`), and regularity of the arithmetic point (`regular_arithmetic_hida_of_literal_automorphy`, supplying `hreg`) are used in Lean and not mentioned.
- P1-f. "the space of cocycles for the cyclotomic twist of the adjoint is finite dimensional by the Galois finiteness condition … supplies finitely many $s_j$" (`core_of_ord_vanishing_two_phi_all` with `W.phiAll hC`): sketch only.
- P1-g. "Enlarge the coefficient order after choosing a self-dual lattice and conjugating the form" (`selfDual`, `conjAll`, `model`): asserted.

Part 3 (Lean `unitOf`, `cupUnr`, `selLow`, `tan`, `rankTwo`, `red2_alt`, `redAbs`, `unramified_at_of_dense_purity_num_e_power_series`, `derZero`, `endJ`, `exists_mon`, `der_zero`, `tor`):
- P3-a. "The local cup-product calculation provides a nonzero additive unramified $u$ and a cochain $\beta$": asserted.
- P3-b. Local counts "at least $q_k^{9+3d_w}$" and "$q_k^{10+3d_v}/C$" (`locLow`, `locHigh`), triviality of the dual invariant group (`dualZero`), archimedean bound $q_k^3$ (`archUp`), normalization cost $q_k^8$ (`normCnt`), and the global inequality itself (hypothesis `GWL` of `selLow`): all asserted. Only the final arithmetic is reproduced.
- P3-c. "The good-component condition, dimension bound, dense arithmetic points and the ordinary vanishing of part 1 give, for every $a\in J$, some $s$ with $\xi(s)\ne0$ and $s\phi(a)=0$ … tangent dimension at most $1+3d$; the height bound there gives a regular local domain … associated-prime criterion": a list of ingredients, not a proof.
- P3-d. "density and purity give a good arithmetic point in an open irreducibility locus; the multiplicity bound selects a simple root in the action polynomial": asserted.
- P3-e. "the type-I condition supplies entries of both signs and an odd-weight entry": asserted.

Part 4 (Lean `flag_match`, `move_all`, `unlEnd3E`): closer to a proof, but "Potential crystallinity is preserved by restriction, isomorphism and duality" and "the splitting condition lifts the local frame elements through $G_L$" are asserted.

### 2. Statements

The statements agree with Lean in substance.
- `DenseThresholdMainCase` / `AdjointLiftingTheorem` (`AutomorphicPointGalois.lean`): `V.S' = s.S`, no primitive $\ell$th root in $L$, `Large L c`, `2 ≤ n ≤ 4`, `r.V0ok`, `AutomorphicPointLocallyGeneric ι x ρ` (fields `cont, rep, arith, aut, unr0, flag, free, irr, n3`), conclusion `OrdZero` resp. `Par x → AdZero V ρ`. The text lists all of these.
- `Par`: Lean `StrictAnti m ∧ 0 < k ∧ (ψ_i g / ψ_j g * cycBar g ^ (m j - m i)) ^ k = 1` on inertia. Matches.
- `UnlEndLogNorm` (`LinkedUnlEOf.lean`): `LinkHyp`, `Even N`, `Psi σ = 1`, `HasFrame`, `OrdPt`, `MatIrr` on every open $U\le\ker\eta$, $K$ with `finrank = 2` and `η.ker = galOf ℚ K Ω`, $\rho$ on $G_K$ equal to the pushed matrices, `∀ N' ≥ 1, LevelAt l N' ![e,0,-e] ρ → Unl l N' ![e,0,-e] ρ`. Matches; `Unl` is `∀ w ∣ ℓ, ∃ A over w, ∃ κ, FlagAt … ∧ ∀ i j, κ i ≠ κ j * cyc`.
Small mismatches:
- `OrdZero` requires `V.frame.IsForm c.O n ρ P` whereas `AdZero` requires `V.frame.IsForm ℤ_[l] n ρ P`. The text says "every allowed form $P$" for both; the Lean root bridges the two with `he : V.frame.eps c.O (Qbar l) = V.frame.eps ℤ_[l] (Qbar l)`. Not mentioned.
- `Free` in Lean is `∃ g : F.Gv v, F.φ v g ∈ F.G' ∧ Pr.FreeRatios (ψ v i g)`. The text's "cyclotomic-kernel element" presupposes that $G'$ is the kernel of the cyclotomic character (used in Lean through `V.hε`); it should say so.
- The unit row and the heading name the conditional implication as the declaration, while the section's status sentence covers three theorems. The scope of the word "complete" is therefore ambiguous.

### 3. Proofs: what I could check, and whether it is correct

No mathematical error found in the parts that are written out. Verified by hand and against Lean:
- Normalization at $c_0$: $R(c_0)z(c_0)=-z(c_0)$, $X_0=-z(c_0)/2$ kills $z(c_0)$; averaging $Y$ with $R(c_0)Y$ gives a primitive on both cosets. Correct.
- Dual-number lift $(1+\epsilon y_0(g))\rho_0(g)$ and $\delta(\mathrm{tr}(g))=\mathrm{tr}(y_0(g)\rho_0(g))$ (Lean `pairF`: `(p.D.tr (single g 1)).snd = (z g * mat ρ₀ g).trace`). Correct.
- Counting contradiction: with $v=\operatorname{ord}(c_1c_2c_3d)$, $k=vb+C+1$, $m=v+k$ one has $k(b+1)=mb+C+1>mb+C$. Correct, and consistent with `B1` (`ncard ≤ card(ResidueField O)^(m*D0+C)`, eventually in $N$ for each $m$).
- `trZero`: well-definedness of $D(\rho(g))=y(g)\rho(g)$ from trace vanishing and full span; $Y=-\sum_iD(E_{io})E_{oi}$ gives $D(A)=AY-YA$. Correct.
- Conjugation formula $z(g)=R(\gamma)z(\gamma^{-1}g\gamma)+z(\gamma)-R(g)z(\gamma)$ and new primitive $R(\gamma)X-z(\gamma)$ (`adL_conj`, `adL_away`). Correct.
- Corner induction in `OrdinaryBlock.fin`: pairs $i>j$ ordered so that the rectangle $a\ge i$, $b\le j$ is cleared first; entry transforms by $\kappa_i/\kappa_j$ of weight $w_i-w_j<0$; `z1fChar` is applied in its `w < 0` branch; diagonal entries by `z1fUnr`. Inequality directions are right, and `StrictAnti` is used in the correct direction.
- Freeness on $U$ via $g_0^{[G:U]}$ and the "small" subgroup killing nontrivial $k$th roots: as in `bkOrd`.
- Part 3 arithmetic: $(x^ey)^{w_i-w_j}=x$ forces $e(w_i-w_j)=1$; `sel_arith` gives $q^2\le CN$ from the four displayed bounds, with one factor $q^3$ per infinite place and $\#\{\infty\}=\sum d_w$. Correct.
- Derivation algebra at the end of part 3 ($D'(p)D-D(p)D'$ kills $p$ and $S.B$, hence is zero): logically sound given the asserted inputs.
Wording error: "compactness puts the representation matrices in a finite field" and "the resulting finite-field cocycle" should read "finite extension of $\mathbf Q_\ell$"; as written it says something false.
Everything listed under item 1 is unverified from the text alone; I confirmed only that the corresponding Lean declarations exist with compatible statements, not their proofs.

### 4. Labels

The closing paragraph's discharge claims check out, but it is incomplete.
- Root: sole caller is `UpperTheory.V.Th.adjoint_lifting_of_cohomology` (`ThFinal.lean:18`), which passes `locPrints_of_litN hH.litN` (`HVFinalU.lean:12`; builds the record from `hN.coh.lfK, ltK, leK, lf, lt, le, bk`, as the text says) and `core_alt_bis hH hC` (`ThFinal.lean:17`). The wrapper in `AdjointLiftingOfCohomology.lean:31` supplies `hC = cohP_alt hH.litN`. Correct.
- `linkedUnlE_alt` (`LinkedUnlE.lean:43-48`) does call `unitary_three_automorphy_dense_of_prints hH` and `Birth.seed2_alt hH` (the two Z1.1 inputs), `tanA (…) (locPrints_of_litN hN)` and `core_alt_bis hH (cohP_alt hN)`. Correct.
- Not mentioned in the label paragraph although passed at the same call: `hN.aut.art`, `local_class_field_theory_all_of_literal_automorphy hN`, `HV.Core.modU_of_printsH hH`, `Z.J.D.modularity_n_of_printed_mult_comp hH Z.Mult.mult_free Z.Mult.compOf_free`, `levEx`, `lamEx`, `b0Ex (phiAll …)`, `Sd.twist_of_printed_results`, `Sd.alg_cyclotomic_of_printed_results`, `Sd.alg_restriction_of_printed_results`, `global_compat_printed_of_literal_automorphy_n`. In particular the modularity input is a substantial theorem and belongs in the list of inputs.
- "The common arithmetic record is `HypothesesH'`" is true but too coarse to count as a discharge label: part 1 uses it through `hida_x_of_printed_hida`, `regular_arithmetic_hida_of_literal_automorphy` and `core_o_of_literal_automorphy_n` (which needs only `LiteratureRankNHypothesis`), and the text does not attach any of these to a step.
- The consumers of `UnlEndLogNorm` are `rigIUE_alt`, `admissible_typeI_even_level_alt`, `hostRigidUE_alt` and `hostNumberUE_alt`; the text cites only the second.
- Cross-reference `\S\ref{sec:P-z1-round3}` resolves (`ch_P.tex:10381`).

### 5. Understanding

The section does convey the architecture: a non-coboundary ordinary cocycle yields a derivation of the universal ordinary ring whose trace derivative is one coordinate more than the $D+nq$ weight and auxiliary coordinates that the duality count allows at a common auxiliary level; a Bloch-Kato finite cocycle is made ordinary by clearing negative-weight lower entries and then the unramified diagonal; a cyclotomic link between adjacent diagonal characters would create a second independent weight-fixed derivation at a point where the graded structure allows none. Part 2 really is explained and a reader can reconstruct it. Parts 1 and 3 read as an annotated index to the Lean development: the reader is told which estimate is used at each point but not why the estimate holds, and the two estimates on which the contradiction rests (the Selmer upper bound with constant independent of precision, and the existence of the $b$ independent derivations at auxiliary level) are exactly the ones left unproved. So the text explains why the theorem follows from its main lemmas, not why those lemmas hold.

### Most important problems for Z1.2

1. "Complete" is claimed for three theorems (`DenseThresholdMainCase`, the finite-to-ordinary implication, `UnlEndLogNorm`) while the unit's declared root is only the second. For the first and third the text is an outline: items P1-a to P1-g and P3-a to P3-e are unproved and unlabelled.
2. Even for the declared root, the bulk of its cone (ordinary implies crystalline `Loc.prC`, internal Hom `isCrys_isDR_internalHom`, `z1fChar`, `z1fUnr`, `z1fSub`, `decEmb`, `bkAbove`, `relKill`) is invoked by name-like phrases with no proof and no "Proved in Lean, not reproduced" label. These are core Lean theorems derived from the published local record, not fields of it, so the closing hypothesis label does not cover them.
3. The upper bound $|S_{m,N}|\le Q^{mb+C}$ with $C$ independent of $m$, and the choice of auxiliary places behind it, is the heart of part 1 and has no proof in the text.
4. The discharge paragraph omits about ten inputs actually passed at `linkedUnlE_alt`, including `modularity_n_of_printed_mult_comp`.
5. "finite field" should be "finite extension of $\mathbf Q_\ell$" (two occurrences in part 2).
6. The `IsForm c.O` versus `IsForm ℤ_[l]` difference between `OrdZero` and `AdZero`, and the identification of $G'$ with the cyclotomic kernel, are silently assumed.
7. Status bookkeeping: `P_notes.md` line 19 says complete, while the v6 and v5 tables at lines 154 and 1100 still show Z1.2 as partial. If those tables are meant as history this is fine, but nothing marks them as superseded.

---

## Summary of the most important problems across the four units

1. **Z1.2 should not be marked complete.** A fair status is: part 2 complete modulo eight named local lemmas that need "Proved in Lean, not reproduced" labels; parts 1 and 3 are a proof map with Lean pointers; part 4 nearly complete.
2. **Z1.2 labels**: add per-step labels and complete the list of suppliers at `linkedUnlE_alt`.
3. **Z1.1.04**: fix the sentence deriving the kernel of $\eta$ from the degree of $K$; state $\eta^2=1$ and the parity inputs; add references for surjectivity of the cyclotomic character on inertia and for openness of $G_L$.
4. **Z1.3.06 and Z1.3.07**: no substantive problems.

No claim is made here about the truth of the hypotheses consumed (`HypothesesH'`, `LocalPublishedTheorems`, `RowT`, the Kato inputs), and nothing in this review bears on whether RH is proved.
