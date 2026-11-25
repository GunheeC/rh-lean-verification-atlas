# DB3 review A — independent referee report on fourteen round-3 notes
AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved
Scope: `${ATLAS}/notes/units/` — B08_v4, B09_v4, B10_v4, P017_v4, D014_round3, D014_v4, D547_v4, D548_v4, D549_v4, D550_v4, D562_v4, D567_v4, D561_v4, V4-COND_round3.
Lean source: pinned commit 40e56bab at `${LEAN_PROJECT}/src` (paths below are relative to `src/`). Read only; nothing was built, and no Lean proof was machine-checked by me.

Nothing in this report says, or should be read as saying, that the Riemann hypothesis is proved. The report checks (a) whether each note states what the cited Lean declaration states and (b) whether the note's written argument is mathematically sound and follows the Lean term. `Main.lean:4–12` contains declarations with the five public statements as their types; I did not audit the chain behind them and take no position on it.

Abbreviations for long paths:
- `PC/` = `Development/AutomorphicArithmetic/PrimitiveCosets/`
- `LT/` = `Development/AutomorphicArithmetic/DedekindLFunctions/LandauTheorems/`
- `CB/` = `Development/AutomorphicArithmetic/CharacterBoxes/`
- `TPS/` = `Development/AutomorphicArithmetic/ThetaCorrespondence/ThetaPairLifts/ThirdPlaceSeries/`
- `SWB/` = `Formalism/SizeWindowBrackets/`, `CSW/` = `Formalism/SizeWindowBrackets/ChainSlopeWindows/`
- `TGC/` = `Formalism/SharpRestriction/RamificationFrobenius/TotientGaloisClasses/`

## 1. Summary table

| Note | Verdict | Gaps | Most serious issue |
|---|---|---|---|
| B08_v4 | CONFIRMED WITH GAPS | 1 (minor) | Five inputs to B09 (`b>0`, `a≥0`, `k>0`, `m≤x^{1/2+ε/2}`, `xm≤k`) come from the error windows, not from the "sizes" the note names |
| B09_v4 | CONFIRMED WITH GAPS | 3 (minor) | The thick-place cost `3(x+1)(η+1)` uses the width-Lipschitz bound with constant 3 (D562/A9), which the note never states or cites at that step |
| B10_v4 | CONFIRMED | 0 | None; rests on P021 (`each_unit_bound_statement`), which the note states as an input |
| P017_v4 | CONFIRMED | 0 | None; two definitional identifications are silent (remarks only) |
| D014_round3 | CONFIRMED | 0 | None |
| D014_v4 | CONFIRMED | 0 | None |
| D547_v4 | CONFIRMED | 0 | Carries an unused hypothesis `x>0` that Lean `gmA_eq` does not have (harmless) |
| D548_v4 | CONFIRMED (light check) | 0 | None |
| D549_v4 | CONFIRMED (light check) | 0 | None |
| D550_v4 | CONFIRMED (light check) | 0 | Proof is a different (explicit-threshold) argument from Lean's; it is correct |
| D562_v4 | CONFIRMED | 0 | ψ(t)≤3t is proved by a different route from Lean; one cited line range stops short of the theorem actually used |
| D567_v4 | CONFIRMED | 0 | None; constants 20, 14, 112, 2, 200 all check |
| D561_v4 | CONFIRMED WITH GAPS (as an outline) | 2 | The unit card pins `CharacterBalanceMoves.core`, but the note states and derives `ch_balance` and only the reindexing step of `th_le` |
| V4-COND_round3 | CONFIRMED WITH GAPS; "Full" is an overclaim | 5 | The proof uses results that are neither among the 34 tabulated hypotheses nor derived in the note (P018/`formB`, P021, `divinN_of_hypV`, `linkMu_of_linkDIV`, a rank bound), and steps 1–2 are outlines of units the atlas itself rates "Outlined" (B07, B05) |

No note is NOT CONFIRMED, and I found no sign error, wrong constant or wrong quantifier order in any of the fourteen. The only statement-level mismatch is the D561 card/note mismatch.

## 2. Per-note findings

### B08_v4 — one-scale bound (`core_gm`, `PC/CoreGm.lean:12–74`)

Statement. Lean: `∀ Λ eD eL K cHH eK C eps, 0<eps → ∃ x1, ∀ x≥x1, ∀ φ (H : HostAx φ) TT, EAtH … C → CoreAtH … → Λ.Gm x ≤ x^(1/2+(eD+eL+7)eps)`. The note's quantifier order (constants, then threshold, then frame/host/TT) matches. Only `eps>0` is assumed; the other constants are arbitrary reals. Match.

Steps checked against Lean:
- Three thresholds: B09 threshold with `C=max(eD+eL,0)+3`, `c=(3o+1)⁻¹`, `M=4o`, `Ko=koOf Λ` (`CoreGm.lean:21`); `large_x_eventually eps K cHH eK` (line 23); `1+4o ≤ x^eps` (lines 24–25). Match.
- `|c|≤1` from `o≥0` (lines 18–20). Correct.
- Internal constants nonnegative: `ConstsBound` gives `0≤eDiv`, `0≤eLoss`, `0≤cHH` (`SWB/ErrorFormsWeakWindowsFalse.lean:23–26`); hence `0≤eD+eL` (`CoreGm.lean:46`) and `max` collapses (line 47). Correct.
- LargeX transfers from `cHH` to the internal `C.cHH ≤ cHH` because `200(1+K)²≥0` and `1+eK≥0` (line 41). Correct.
- Exponent monotonicity `x^(CErr·ε) ≤ x^((eD+eL+3)ε)` needs `x≥1` (line 51–54) and bracket `≥0` (lines 48–50). Both stated in the note.
- Final arithmetic: `Gm ≤ x^(1/2+(eD+eL+6)ε) + 4o·x^(1/2+ε)`, `1/2+ε ≤ 1/2+(eD+eL+6)ε` since `eD+eL≥0`, then `(1+4o) ≤ x^ε` (lines 61–74). I redid it; correct, exponent `eD+eL+7` is right.
- Coverage: `∀ u∈A0 ∃ v, tr v = u` used at lines 57–60. Stated.

Gap B08-1 (minor). The note says "The sizes, thinness, costs and containment T₂⊂A₀ are fields of the same core package. … Hence B09 applies." B09 also needs `0<b`, `0≤a_E`, `0<k`, `m ≤ x^(1/2+ε/2)` and `x·m ≤ k`. These are not in `SizesA`/`RestSize`; Lean takes them from `ErrWindows0` (`w4`, `w5`, `w10`, `w7`, `w8`; `CoreGm.lean:42–45, 55–56`; definition at `SWB/ErrorFormsWeakWindowsFalse.lean:28–41`).

Language: "This establishes B08 for all eligible frames and hosts simultaneously" is acceptable for a conditional one-scale implication.

### B09_v4 — finite character average (`ch_core`, `LT/ChCore.lean:343–442`)

Statement. Lean: `∀ C ε CE Ko c M, 0≤C → 0<ε → |c|≤1 → ∃ x1, ∀ x≥x1, ∀ H m D S ell N TT T2 a w b b' k aE η X' θ A0 Kp, HostFactsS → 0<b → 0≤aE → 0<k → m≤x^(1/2+ε/2) → x·m≤k → SizesA → ThinScales → CostWindows → RestSize → T2⊆A0 → CharsA → (gap bound on A0) → GmA ≤ x^(1/2+(C+3)ε) + SigA`. The unit card B09.yaml matches this. The note itself does not restate the theorem; see gap B09-2.

Independent re-derivation (all agree with the note and with Lean):
- Principal frequency: cost `C_d` per term (`one_char`, lines 214–227).
- Kept nonzero ξ: per-term move cost `log(x+1)+C_d+K_o` (`move`, 154–165); coefficient error `M·x^(−1+ε)·n_T · x(log x+C_d+K_o)` using `|G_ξ(x)| ≤ x(log x+C_d+|ℓ|)` from `G_ξ(1)=ℓ(ξ)` (`triv`, 167–179); zero when ξ is trivial on H (lines 231–236). `ξ(e₁(t))=ξ(0,t)` needs `ξ(s₀)=1` (lines 238–241). Signs correct: lower bounds throughout.
- Discarded ξ: `Re(ξ(e₁t)G_ξ(y_t)) ≥ −|G_ξ(x)| − (log(x+1)+C_d+|C_E|log x)` (lines 270–281).
- Threshold: `log x ≤ 4x^{1/4}` (line 384–386), `log(x+1) ≤ 1+4s ≤ 5s` (387–391), `x^(−1+ε)·x = x^ε` (379–382). With `A₁ = 5+C_d+|K_o|+|M|(4+C_d+|K_o|)+4|C_E|` each cost is `≤ A₁·s·e` (r1–r3, lines 403–418), and `|𝒜|·A₁·s·e ≤ |M|A₁·s·e ≤ s²e = x^(1/2+ε)` once `|M|A₁ ≤ x^{1/4}`. So the factor 4 is slack, as the note says (line 439 only needs `≤4`). `A₁` depends on `C_d, K_o, M, C_E` only, so the threshold precedes `H, TT, T₂, w, m`. Correct.
- Thin place: `a_t ≥ (x−1)b`, `w ≤ 2b'`, `b'X' ≤ xb`, `x≥3` give `X'w/3 ≤ 2xb/3 ≤ (x−1)b ≤ a_t` (lines 126–130). Correct. Then `w|G(a/w)| ≤ aθ ≤ (x+1)bθ` (133–138).
- Count: `(1/f)·(#places ≤ f)·(#characters = 2f)·K = 2fK` (`CR.norm_avg_le`, `CSW/LipschitzWeightAndMinimum.lean:188–`; `card_char` line 170; `card_S_le` line 182). `2f[3(x+1)(η+1)+(x+1)bθ] ≤ b/x + b/x` from `CostWindows` (`SWB/SChain.lean:50–51`; `ChCore.lean:296–301`). Correct.
- Subgroup average: `−e₁(s+u−t) = e₁(t)+(0,−s)+(0,−u)` in `(ℤ/2)²×H` (`sum_A`, 28–54); vanishing off `𝒜`; factor `b·n₂/f = b·δ₂/2` with `f=2n` (`sum_Th`, 56–73; `phiSet_card`, `Formalism/ThickAverageLoss/ThickAverageProofs/ThickAverage.lean:39`). Correct.
- Size lemma (`proposition_size_bound`, `CSW/LipschitzWeightAndMinimum.lean:507–592`; `SizeWindows` at `SWB/GrowthBoundGivesRiemannHypothesis.lean:109–116`). I recomputed the four quotients: `a_E/(mb) ≤ 2x/m ≤ 2X ≤ 2Y`; `a_E m/(bk) ≤ 2xm/k ≤ 2 ≤ 2Y`; `2(n/t)m x^ε ≤ 4x^(1/2+13ε/8) = 4Y`; `r k x^{2ε}/(n²t) ≤ (n/t)x^(1/2+ε) ≤ 2x^(1/2+9ε/8) ≤ 2Y`. Sum 10. Then `δ(G−4X) ≤ 2(10PY+2/x) ≤ 22PY`, `G ≤ 4X+22PYx^ε ≤ 26Z` with `Z=x^(1/2+(C+21/8)ε)`, and `26 ≤ x^(3ε/8)` gives exponent `C+3`. Lean has the same 22, 26 and 21/8 (lines 580–592). Correct.

Gap B09-1. "At a thick place b≤w≤b+η+1 and a_t≤(x+1)b, so replacing its weighted value by the frozen one costs at most 3(x+1)(η+1)." This is the width-Lipschitz estimate `‖wG(A/w) − bG(A/b)‖ ≤ 3A/min(w,b)·|w−b|` (`LipW`, `SWB/GrowthBoundGivesRiemannHypothesis.lean:58–60`), supplied by `lipschitz_weight_all` (`CSW/LipschitzWeightAndMinimum.lean:957–964`) and used at `ChCore.lean:117–123` and `:308`. The note's input paragraph lists only the increment half of D562 (A4), not the width half (A9). The constant 3 in the note is therefore unexplained at that point.

Gap B09-2. The paragraph "Character inputs at the same host" assumes `HostAx`, `EAtH` and fixes `c=(3o+1)⁻¹`, `M=4o`, `K_o=koOf Λ`, and quotes D547 and D549. None of this belongs to B09: `ch_core` takes `CharsA` abstractly for arbitrary real `c, M, K_o, C_E` and never mentions a level. The proof in the note is nevertheless general (it uses `|M|`, `|K_o|`, `|C_E|`). The effect is that the note does not contain a self-contained statement of the theorem it proves and blurs B09 with B08.

Gap B09-3. The balance identity needs `a_t>0` and the cutoff `a_t/w ≤ N` on Φ. The note does not say where `a_t>0` comes from; Lean derives it from `|a_t/b − x| ≤ 1`, `x≥3`, `b>0` (`ChCore.lean:292–295`).

Observation (not a defect of the note). The hypothesis `|c|≤1` of `ch_core` (line 343, `hc`) is not used anywhere in the Lean proof body (lines 352–442).

### B10_v4 — lattice bound to gap bound (`ch_top`, `LT/ChTop.lean:37–72`)

Statement matches (card B10.yaml and Lean): under `IdentU`, `SizeData₂` (the eleven hypotheses), `ErrWindows`, `BNBoundsU`, `LargeX`, for every unit `u`: `gapA(tr u) ≤ x^(CErr·ε)·errorBracketSizeWindows` with `a_E = a`.

Steps: main-term transport under the two bijections (`ch_top_main_eq`, lines 11–35) and `gap = ASK − Main` (lines 47–52); `ASK ≤ Main + ErrX5at` (`each_unit_bound_statement`, `CSW/LevelOfCongruence.lean:175–197`, line 54); `ErrX5at ≤ x^(CErr ε)·ErrText` (D567, line 55); `ErrText ≤ Br` from `BNBoundsU` with `m≥0` (lines 61–67; `BNBoundsU` at `Development/AutomorphicArithmetic/DedekindLFunctions/SplitInertia.lean:74–77`). The `N_c` bound in the note, `n₂kbx^ε/(n²x^{−ε})`, matches. All correct. The transfer to all of `A₀` by coverage is done in `CoreGm.lean:57–60`, as the note says.

No gaps. Dependency to keep visible: the pointwise lattice inequality P021 is an input here and is not among lists A–C of V4-COND (see V4-COND gap 1).

### P017_v4 — family threshold (`level_gm_le_on_family_scales`, `PC/LevelGmLeOnFamilyScales.lean:28–30`)

Statement. `ChebyshevInequalityOnWindows` (`TGC/TopWin.lean:26–28`): `∀ eD eL eps, 0<eps → ∀ Fm, EFamC Λ Fm → (∃ K cHH eK CL x0, ∀ x≥x0, x∈Win → Tied …) → ∃ x1, ∀ x≥x1, x∈Win → Λ.Gm x ≤ x^(1/2+(eD+eL+7)eps)`. The note's statement matches, including "on this same set".

First step to challenge (threshold before the scale-dependent member; same translates):
- `windowInequality_of_artinInputs` (`PC/WindowInequalityOfArtinInputs.lean:17–25`): `C, xE` from `EFamC` and `K, cHH, eK, CL, x0` are unpacked first (line 20), `core_gm` is applied to those constants (line 21), threshold `max x1 (max x0 xE)` (line 22), and only then is the member `i` obtained at the given `x` (line 24). The explicit-formula bound is evaluated at that same `i` (line 25). Order is correct.
- `tiedCore_of_chainTied` (`LevelGmLeOnFamilyScales.lean:13–26`): `tr = id`, word fibres `(Fm.D x (pt u0)).what₂.Word` (line 22); coverage `fun s _ => ⟨s, rfl⟩` (line 23); `TT = host.TT` from the membership equation, `Fm.TT_eq` and injectivity of `Frame.A.val` (lines 17–21); `T₂ ⊆ A₀` from the digit description at translate 0 (lines 25–26); size clauses restricted from all translates to `A₀` (line 24). All as the note describes. `EAt` is by definition `EAtH … D.host.TT …` (`TGC/TopDefs.lean:13`), so the same `TT` is used on both sides.

Remarks (no gap counted): (i) the passage from `Ident`/`BNBounds`/`arithOf`/`GlobalTheoryTheory.logDerivativeAtOne` to `IdentU`/`BNBoundsU`/`arith`/`An.logDerivativeAtOne` is definitional (`LevelGmLeOnFamilyScales.lean:11`, `TopDefs.lean:11`) and silent in the note; (ii) the `ValuesAtX` clause of `ChainTied`, the only place `C_L` enters, is discarded (`LevelGmLeOnFamilyScales.lean:16`, last `-`), so `C_L` is a dummy in P017. The note could say so.

Not checked: the paper page references (pp. 10–21, Definition 6.19 p. 77).

### D014_round3 and D014_v4 — host prime facts (`hostFactsS`, `PC/hostFactsS.lean:127–136`)

Statement: `HostFactsS (arith H) (insert H.q H.small)` for every frame and `HostAx` host. Fields at `Development/AutomorphicArithmetic/DedekindLFunctions/SplitInertia.lean:14–22`. Both notes state all eight fields correctly (`unram` for primes `p∉S`, `p≠d`).

First step to challenge: the CRT unit `u≡1 (mod Qq)`, `u≡−1 (mod d)` (`hostFactsS.lean:99–100`) is `d`-local since `ordCompl[d] N = Qq` (lines 84–85, 104–105); its sign is `(−1/d) = −1` because `d≡3 (mod 4)` (lines 114–118); `art_d` then forces `art u = iod` (lines 119–125), and `toE iod = sgc0` (lines 40–42). Correct. Coordinate exchange: `toE` sends `((a,b),m)` to `((σ(b),σ(a)),ι⁻¹m)` (`PC/RecH.lean:10–11`) and `InPhi g := g.1.1 = 0` (`Formalism/ThickAverageLoss/PartnersToFactorsAt.lean:20`), so `InPhi` tests the second multiplicative sign, which `art_ch` equates with the Jacobi symbol at `d` (`hostFactsS.lean:10–15`). Both notes have this right.

Other checks: `HostHyp` is `q≡3 (8)`, `d≡7 (16)`, `(−d/q)=1` (`Formalism/FrobeniusOrbits/Statement.lean:13–14`); `(2/d)=1` from `d≡7 (8)` (`CSW/GaloisMapComplexConjugation.lean:290–294`); `(p/d)=(−d/p)` for odd `p` when `d≡3 (4)` (`TGC/HostFacts.lean:15–24`); `QS_split` for odd `l | QS` (`TGC/ConjEMemHostFIff.lean:21`). Correct.

Both CONFIRMED. Quadratic reciprocity and the supplementary law are used as standard facts (Mathlib in Lean); neither note lists them as inputs, which is acceptable but could be said in one clause.

### D547_v4 — kept character sums (`gmA_eq`, `PC/GmAEq.lean:61–149`)

Statement: `EAtH → HostAddCharCompatible → ∀ y, GmA (arith H) ell (keptA Λ H) (3o+1)⁻¹ y = Λ.Gm y`. The note's preamble adds `x>0`, which this Lean theorem does not assume (it is needed only by `charsA` and `sigA_le`). Harmless, but it is a hypothesis the Lean statement does not have.

Checks: `Level.Gm = Gz + Σ_{Nt} wt·Re gChi` with `wt = 1` at `psK`, else `(3o+1)⁻¹` (`TGC/ExplicitFormulaErrorOfHostConditions.lean:36, 38`); `wtA` (`SplitInertia.lean:30`). Weight match in the three cases (lines 94–128): trivial character; `psC` kept forces `psK = some` with weight one, and `psK = none` forbids keeping `psC` (`ExceptionalCharacterKept`, `TGC/Analytic.lean:158–159`); all other kept characters get `c`. Correct. Bijection `keptA → KEPT` from `chr_bij` and `prim_inj` (lines 67–93; `PC/ChrBij.lean:21–24`, `PC/PrimInj.lean:6–27`).

First step to challenge (zero branch at primes dividing the modulus): `cosetMean_eq_primitive` (`CSW/GaloisMapComplexConjugation.lean:209–231`) treats both branches: trivial on inertia ⇒ conductor divides `ordCompl[p] N` and the value is `χ_prim(p)^i` via `frobUnit ≡ p`; nontrivial ⇒ `p | conductor` and both sides vanish (lines 225–231, using `inertia_conductor`). The note's argument matches. `(y/n−1)₊ = y/n−1` on `n ≤ ⌊y⌋` (`PC/PrimRead.lean:25–33`). CONFIRMED.

### D548_v4, D549_v4, D550_v4 (lighter checks)

D548 (`charsA`, `PC/charsA.lean:80–125`): six clauses of `CharsA` (`SplitInertia.lean:56–62`) match. `|𝒜| = 4·[H:A₀] = 4o` (`PC/CardPsiA.lean:26–`, `o_eq`). Shares: `lam γ = (4 if γ∈A₀ else 3)/(3o+1)`, error `≤ δ·n_T` per coset (`TGC/ExplicitFormulaErrorOfHostConditions.lean:135–140`); the note's `n_v = (3+1_{v=0})c·n_T + e_v` and `Σ_v α(v)n_v − c·n_T = Σ α(v)e_v`, modulus `≤ o·x^(−1+ε)n_T ≤ 4o·…`, agree with `tops_sum_gen` (`PC/TopsSum.lean:26–30`) and `charsA.lean:105–112`. Both signs at `iod`: `chr_bounded` (lines 40–51) gives `(Xp ∧ ¬Kept) ∨ Xm`, exactly `HostRaw.Bounded` (`TGC/Analytic.lean:136`). CONFIRMED. I did not read the bodies of `tops_sum_gen` beyond line 50 or `card_PsiA_index`.

D549 (`sigA_le`, `PC/SigALe.lean:38–60`): statement and proof match (`bdG` on the bounded set, then card `≤ 4o`). CONFIRMED.

D550 (`large_x_eventually`, `CSW/SubThreeMulLogTwoLe.lean:319–329`): statement matches. The note proves it with an explicit `x₀ = exp(max{0, 2/ε², log(max{1,K_*})/ε})`; Lean uses `isLittleO_log_rpow_atTop` and `tendsto_rpow_atTop`. I checked the note's argument: for `u = log x ≥ 2/ε²`, `e^{εu} ≥ (εu)²/2 ≥ u`; and `e^{εu} ≥ max{1,K_*}`. It works for `K_*<1` (including negative `K_*`) and for small ε. CONFIRMED. The header block about the bracket `E` is irrelevant to this lemma.

### D562_v4 — increments and width (`derivative_integral_all` :966–981, `lipschitz_weight_all` :957–964 in `CSW/LipschitzWeightAndMinimum.lean`)

Statements match `LipW` and `DerivInt` (`SWB/GrowthBoundGivesRiemannHypothesis.lean:58–65`), with `C_d` absolute and chosen before `H, D, ℓ` (`DerivIntAll`, lines 161–163).

First step to challenge (principal character, constant three): with `w ≤ b`, `wG₀(A/w) − bG₀(A/b) = U − V`, `U = Σ Λ(n)[(A/n−w)₊ − (A/n−b)₊] ∈ [0, 3A(b−w)/w]`, `V = A log(b/w) ∈ [0, A(b−w)/w]`. Same sign, so `|U−V| ≤ max(U,V) ≤ 3A(b−w)/w`. This is exactly `lip_triv_le` (lines 901–944). Correct; constant 3 preserved.

Other checks I redid:
- ψ(N) ≤ 3N by the binomial induction: `Ψ(N) − Ψ(⌈N/2⌉) ≤ log C(N,⌊N/2⌋) ≤ N log 2`; `N ≤ 3⌊N/2⌋` for `N≥2`; so `Ψ(N) ≤ 3⌈N/2⌉ + N log 2 ≤ 3N`. Correct. Lean proves the same bound differently, from Mathlib's `Chebyshev.psi_le` (`psi_le_three`, lines 668–690). The note says its argument is "an elementary derivation of the estimate in `AN.psi_le_three`"; it should say plainly that it is not the Lean proof.
- `log N − 1 ≤ L(N) ≤ log N + 3`; non-principal increment `≤ |y−z|(L(⌊M⌋)+|ℓ|)`; principal derivative `L(N) − log t + γ` on `(N,N+1)` with `−1−log 2 ≤ L(N) − log t ≤ 3`. Hence `C_d = 3+|γ|` works for both. Correct. Lean's constant is `|K| + log 4 + 4` (line 968); only existence matters, as the note says.

Citation remark: for the principal increments Lean uses `Formalism.zetaPrimeSumErrorLipschitz` (`Formalism/ZetaNonvanishing/GzLipschitz.lean:220`), with `lip_upto` at line 185. The note cites `GzLipschitz.lean:55–106,127–184`, which stops before both.

### D567_v4 — per-unit error (`errX5at_le`, `CSW/PChain.lean:613–672`)

Statement matches: `ErrWindows D C Xpp eK K → LargeX D.x D.ε K C.cHH eK → ErrX5at u ≤ x^(CErr C·ε)·ErrText`, `CErr = eDiv+eLoss+3`, `KBig = 200(1+K)²(1+cHH)(1+eK)` (`SWB/ErrorFormsWeakWindowsFalse.lean:16–52`; `ErrX5at` at `SWB/QuotientSlopeBoundsWith.lean:45–54`). The note's list of window conditions agrees with `ErrWindows0` clause by clause.

I recomputed every term against `core_ineq` (`CSW/SubThreeMulLogTwoLe.lean:13–207`):
- Outside the fraction: `4Ky + 2Ky + Kd + K + 4Ky + 1 + Kz + (K²z+4K²y+K+1)`; in units of `ydz` this is `5K²+14K+2 ≤ 20(1+K)²` (Lean: same polynomial, line 197).
- `(Ū+b)/E ≤ 5K²+13K+2K·e_K+2` in units of `yz` (Lean `TU`, line 138, with `g=1+e_K`), `≤ 14(1+K)²(1+e_K)`.
- Fraction: `(1−δ̄)⁻¹ ≤ 2` from `δ̄ ≤ 1/2`; `4 log(1+x^{cHH}) ≤ 4(1+cHH)y`; product `2·4·14 = 112`. Mixed frame term: `2·K·y` from the last window clause. Correct.
- `20+112+2 = 134 ≤ 200`, then `K_* ≤ y` gives `y³dz = x^((eDiv+eLoss+3)ε)`. Correct.
The note uses `log k ≤ e_K·y` where Lean uses `(1+e_K)y`; both are valid.

CONFIRMED. No gaps.

### D561_v4 — balance identity and frozen-width reindexing

A8 (`ch_balance`, `LT/ChBalance.lean:200–260`). Statement matches: `HostFactsS D S`, `a>0`, `w>0` on Φ, `a/w ≤ N` on Φ ⇒ `ASK − MAIN = De` in ℂ. `ASK`, `MAIN`, `De`, `IsInert` in the note agree with `SWB/FirstPrimeNeSecondPrime.lean:72–96`.

Checked: orthogonality `(1/f)Σ_ξ ξ̄(g)v_ξ(p^i) = (2/|I_p|)·1[g−iF_p∈I_p]` (`|U| = 2f`; `orthogonality_ramified`, `CSW/StronglyIrreducible.lean:311–317`); three prime classes (`lsplit` 77–97, `lunram` 55–75, `ld` 99–120, `cardI` 34–40; `d>N` case 18–32); truncation `h(p^i,g)=0` for `p^i>N` (lines 146–152). Other order: `W·L_ξ(a/W)`, corrections `a log a − a log W − (1+γ)a` for ξ=0 and `−aℓ(ξ)` otherwise (lines 207–215); colour sum `(1/f)Σ_{g∉Φ} ξ̄(g) = 1[ξ=0] − 1[ξ=χ_C]`, giving `+aℓ(χ_C)` (lines 236–244); partner bijection (lines 245–255). Signs correct; result is `MAIN`. CONFIRMED.

A10 (`th_le`, `LT/ChCore.lean:75–152`). The note derives only the identity `hTh` (lines 90–104) together with `De_re` (`CSW/LipschitzWeightAndMinimum.lean:161–168`): `P_t(g)` is thick iff `g = e₁(s+u−t)` for a unique `s∈T₂`. Correct, and the note says explicitly that the thin terms and width change are elsewhere (they are in B09_v4).

Gap D561-1 (card/note mismatch). `units/D561.yaml` pins `Deduction.CharacterBalanceMoves.core` (`ChCore.lean:283–338`) and states the averaged inequality `|TT|·m·b·(δ₂/2)·Y ≤ Err + 2|TT|mb/x`. The note neither states nor proves that; it treats `ch_balance` and part of `th_le`. `data/round3_changes.json` lists `ch_balance` and `th_le` for D561. The three sources disagree about what D561 is.

Gap D561-2 (small). In "Hence J = ASK" the note does not say that a prime `p∈S` is never inert. It follows because inert requires `F_p∉Φ` while `split_frob` gives `F_p∈Φ` (`ChBalance.lean:163–167`), and this is needed since the inert condition only excludes `2, q₁, d`, not all of `S`.

### V4-COND_round3 — conditional theorem

What I compared: the Lean term `UpperTheory.Top.zero_free_all_of_green_v_win` (`TPS/TopPlug.lean:12–15`) and what it unfolds to: `zeroFreeAll_of_topG` (`CB/ZeroFreeAllOfTopG.lean:26–34`), `shape_closed_link_n_of_green` (`TPS/TopShape.lean:33–55`), `goal_of_shape_of_hyps` (`TPS/ShapeOf.lean:24–30`), `topDesWin` (`CB/DesWin.lean:11–31`), `supplyChi` (`CB/SupplyChi.lean:8–16`) with `supplyOfAdmOf` (`Development/AutomorphicArithmetic/ShortNorms/supplyOfAdmOf.lean:13–135`) and `winPairs` (`CB/WinPairs.lean:5–81`).

Hypotheses as stated in the note versus Lean:
- V = `VWin` (`CB/ExistsPageN.lean:12–49`). Every clause matches: `0<ε<1/52`; `e` with `PageN` for `x≥1`; `∃ J≥1, ∃ X₀, ∀ X≥X₀, ∀ q d, WinPair ε X^{1/J} q d → ∃ Y, X^{1/J} ≤ Y, Y² ≤ X, ∀ x∈[Y,Y²], VAt`; cutoff `⌊x^401⌋₊`; budget `√exp(x^ε) = exp(x^ε/2)`; finiteness for `0<a<t` at every prime; sum over every finite set of primes, ℓ=2 included; `WinPair` (lines 27–37) and `IsChiField` (lines 19–25) as described. Quantifier order correct.
- F = `Nonempty (HypsAlt (fun 𝒞 => Closed 𝒞 fun Fm _ => LinkN Fm) DefiniteSideCondition)` (`TopPlug.lean:13`; record at `TPS/Hyps.lean:22–90`, last field `nRest : N (D3 3 𝒜)`). `Closed` matches `Formalism/SharpRestriction/ParamsHeightRankConstant.lean:159–161`. Match.
- B = `GlobalTheory.GLq.Green` (`Development/AbelianVarietyTheory/Definitions/NonGaloisDescent/LabelDatum.lean:108–112`, with `IsCuspOf` 93–96, `IsPrimeLab` 91). Degree `∏_{1≤i<d}(g^i−1)`, the character formula with sign `(−1)^{d−1}`, injectivity and surjectivity onto cuspidal characters all match.
- Conclusions: `Statements.lean` definitions and `Main.lean:4–12` match the note's wording (`χ≠1 ∨ s≠1`; strip `0<Re s<1`; zeta zeros other than `s=1` and `−2(n+1)`).
- Table: 3+10+8+13 = 34 rows. All 34 named declarations exist at the cited files and starting lines (I grepped each). Role descriptions I compared with signatures: A1–A10, B2–B8, C2, C13 agree. I did not read the signatures of B1, C1, C3–C12 against their one-line descriptions beyond confirming how `TopShape.lean` calls them.

Same family / same selection (the "first step to challenge"):
- `goal_of_shape_of_hyps` feeds the shape with `h.𝒜` and selections all derived from the single `h.σ` (`ShapeOf.lean:25–30`). One witness, one class, one raw selection. Confirmed.
- `nRest : Closed (D3 3 𝒜) LinkN` is passed as `hN` to `topDesWin (WithChN 𝒜) … 3` (`TopShape.lean:52–53`); `D3 C0 𝒜` is by definition `Des (WithChN 𝒜) C0` (`Formalism/LocalToGlobal/ClassOfRecordOfChoice.lean:48`). Same class.
- In `topDesWin` the nine closed conditions are intersected (`DesWin.lean:23`), a single `(Fm, CH)` is drawn from the design class on `𝒜 ∧ G.cls la` (line 27), and all nine are instantiated at that `(Fm, CH)` (line 28). `divinN_of_hypV` uses `HypV` of the same `Fm` via the request class, with `LinkN` and `SmallLevelRankEq` (line 29); `LinkDIV` from the division implication with eta (line 29); `linkMu_of_linkDIV` with `NuFullF`, `MuRank`, `MuTu`, `MuDGam` (line 31); then `LinkGLOBAL` on `⟨LinkG, LinkS, LinkIRR, LinkDIV, LinkMu⟩` (line 30). This is exactly the note's step 2. Constants `Cabs=2, C0=3, eD=2, eL=0` (`TopShape.lean:52`; `link_gl`, `Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/LinkGl.lean:18`), so the exponent is `1/2+9ε`. Confirmed.
- The family returned by `FamilyClassConnected` (`CB/DivinNOfHypV.lean:13–15`) is the one for which `EFamC` is derived from the request class (`ZeroFreeAllOfTopG.lean:19–24, 30–33`), with explicit-formula constant 4 (`CB/Supply.lean:42–43`). Same `Fm` in P017. Confirmed.
- All thirteen C rows are consumed by the term: C2 line 35, C5 line 36, C6 line 40, C12 line 41, C4 line 46, C3 line 47, C1 line 50, C8 line 53, C9/C11/C10 line 54, C7 line 55 of `TopShape.lean`; C13 in `TopPlug.lean:15`. Rows B1–B6 are consumed in `supplyOfAdmOf.lean` (lines 28, 29, 68, 93–94, 110, 125, 129). B8 is consumed at `CB/SupplyChi.lean:13`, and B7 inside B8 (`Development/AutomorphicArithmetic/CoprimeRanks/AdmChi.lean:16`).

Step 1 arithmetic, redone: with `k^a = c`, `Z = kW`, `u = x/k`: `(kW)^{3/2} ≤ W²` iff `k³ ≤ W`; `x^a = c·u^a ≤ c·2^{e(u)} ≤ 2x^a`; `x^400 = k^400 u^400 ≤ u^401` since `k^400 ≤ W ≤ u`; `exp(u^ε/2) ≤ exp(x^ε/2)`. Agrees with `WinPairs.lean:40–51, 63–81`. The frame has `φ.e = e(u)` and `φ.ord = c·2^{e(u)}` (`CB/FieldChi.lean:20–25`), and `isChiField` is at `φ.e` (`CB/IsChiField.lean:5–6`), so V is applied to the right field type.

Step 4: matches `level_of_tiedWin` (`TGC/TopWin.lean:68–81`), `Imprimitive.lean:5–35`, `ClaimStrip.lean:59–102` (Euler factors nonzero for `Re s>0`; reflection with nonvanishing gamma factors; `ζ(0)≠0`; completed zeta for `Re s ≤ 0`).

So the statement matches and the term trace is faithful. The gaps concern what the note may call "Full" and what its hypothesis list omits.

Gap V-1 (dependencies outside the 34 rows, not derived in the note or in the reviewed companion notes). The argument as written needs:
 (a) the level window criterion `formB` (`PC/Imports.lean:8–19`, unit P018, resting on P022/P023 `Deduction.zeroFree_of_rpow_window`), consumed at `ZeroFreeAllOfTopG.lean:29`. Step 4 gives a four-sentence Mellin/Landau sketch and a paper reference; this is not a proof and `formB` is not in lists A–C.
 (b) the pointwise lattice bound `each_unit_bound_statement` (`CSW/LevelOfCongruence.lean:175–197`, unit P021), consumed at `LT/ChTop.lean:54`. List A has `errX5at_le` (A5) but not this. V4-COND does not mention P021 at all.
 (c) `divinN_of_hypV` (`CB/DivinNOfHypV.lean:76–131`), consumed at `DesWin.lean:29`. One sentence in step 2; it is elementary but not derived.
 (d) `J.linkMu_of_linkDIV` and `linkMu` (`Formalism/SharpRestriction/AdmissibleParameterJoins/SumLogPrimeFactorsLe.lean:728–784`), with `muTu_of_tuSize` and `J.muDGam_of_fact`, consumed at `DesWin.lean:31`. One sentence in step 2. I did not read `linkMu`'s body.
 (e) the rank bound `t ≤ x^400` (`UpperTheory.Top.eventually_rank_le_rpow_of_lt_one_div_fiftytwo`, used at `supplyOfAdmOf.lean:38, 134`). The note asserts "Its rank t is at most ⌊x^400⌋₊" with no source; B7 gives `RankVal`, not this bound.
 (f) classical facts used through Mathlib: nonvanishing on `Re s ≥ 1`, the functional equations, `LFunction_changeLevel`. The note mentions "classical nonvanishing" in passing but does not list these as inputs.
 The size lemma `proposition_size_bound` (D563) is also outside list A but is fully derived in B09_v4, so it is not a gap.

Gap V-2 (step 2 omits the kernel-bound wiring). `TopShape.lean:37–47` builds the hypothesis of C3 from C5, C12, C6, C4 together with `closed_Csz_ge_fn`, `Closed.of_class`, `cut_of_stable` (from `hMt`), `complement_two_of_items` (from `aC2`), the single-map condition from `hRB`, and `toRows_alt`. The note compresses all of this into "Apply Green and C1–C13 to its selections and to the request." A reader cannot reconstruct which F-fields feed which row.

Gap V-3 (step 1 quantifier wording). "V supplies the square window [W,W²] … Choose W ≥ max(1,k³,k^400)." `W` is produced by V and cannot be chosen. What is chosen is `X ≥ max(X₀, M^J)` with `M ≥ max(1, y, Y₁, k³, k^400)`, which forces `W ≥ X^{1/J} ≥ M` (`WinPairs.lean:23–37`). The note also omits the further lower bounds on the scale used to meet B2's premises: `4ψ.N ≤ ⌊Y^{ε/5}⌋`, `q≠3`, `e ≥ e₀` (`supplyOfAdmOf.lean:39–92`).

Gap V-4 (status). Steps 1 and 2 are prose outlines of `supplyChi` and `shape_closed_link_n_of_green`. The atlas rates exactly those units "Outlined" (B07, B05; `units/B07.yaml`, `units/B05.yaml`). A note whose two central steps are outlines of Outlined units, and which depends on V-1(a)–(e), is not "Full" in the sense used for B08–B10. It is an accurate, well-organised reduction map.

Gap V-5 (hypothesis list versus term). The note says the Lean implication "explicitly receive[s] Green, V and the nonempty record F" and that the manuscript "exposes A–C as separate assumptions". That is right, but the conditional theorem as stated ("V + F + B + lists A, B, C ⇒ five goals") is then weaker than what the note's own proof needs, by V-1. Either the list or the statement has to change.

Not checked for V4-COND: paper page numbers (pp. 6, 37–40, 83); `data/round3_v4.json` hashes; bodies of B1–B8 and C1–C13; `hostOfFieldOf`; `linkMu`; `formB`/`level_family`/`zeroFree_of_rpow_window`; `Supplements/Kernels/*` (how `Main.lean` obtains its terms).

## 3. Overclaiming language and unstated literature

- V4-COND_round3: "This is a Full exposition of a conditional paper theorem" — overclaim, see V-4 and V-1. No sentence in any of the fourteen notes claims RH; each carries the disclaimer line.
- V4-COND_round3 step 4: "The one-sided Landau window criterion excludes a level zero…" and "classical nonvanishing for Re s ≥ 1" — relied on, not listed as hypotheses (V-1 a, f).
- D562_v4: "This is an elementary derivation of the estimate in `AN.psi_le_three`" — true as mathematics, but Lean's proof goes through Mathlib `Chebyshev.psi_le`; say so.
- D014 (both): quadratic reciprocity and the supplementary law for 2 used as standard results; fine, but name them as background.
- B10_v4, P017_v4: cite paper lemma/proposition numbers ("v4 Lemma 3.5", "Proposition 3.1", "Definition 6.19") that I could not check against a PDF.
- B08_v4 "This establishes B08…", B09_v4 "Adding Σ_A proves B09": acceptable; both are conditional local implications and the notes say "under the assumptions of".

## 4. Required corrections

1. `notes/units/V4-COND_round3.md`, header line "This is a Full exposition…" and `units/V4-COND.yaml` field `status`: change "Full" to "Outlined", or scope it explicitly as "Full relative to P017, P018, P021, B05, B07". Same change in `data/round3_changes.json` entry `V4-COND`.
2. `notes/units/V4-COND_round3.md`, section "Quantified hypotheses" (after the three tables) and `units/V4-COND.yaml` `hypothesis_details`: add the inputs the proof uses beyond the 34 rows — `UpperTheory.Comparison₂.formB` (`PC/Imports.lean:8–19`, P018/P022/P023), `each_unit_bound_statement` (`CSW/LevelOfCongruence.lean:175–197`, P021), `divinN_of_hypV` (`CB/DivinNOfHypV.lean:117–131`), `J.linkMu_of_linkDIV` (`…/SumLogPrimeFactorsLe.lean:775–784`), `eventually_rank_le_rpow_of_lt_one_div_fiftytwo` (used at `ShortNorms/supplyOfAdmOf.lean:38,134`), and the Mathlib facts (nonvanishing on `Re s ≥ 1`, functional equations, change of level). Alternatively prove them in the note.
3. `notes/units/V4-COND_round3.md`, step 1, sentence "Choose W ≥ max(1,k³,k^400)": replace by the actual choice — take `X ≥ max(X₀, M^J)` with `M ≥ max(1, k³, k^400)` and the B1 threshold, so that the window start `W ≥ X^{1/J} ≥ M` (`CB/WinPairs.lean:23–37`). Add the lower bounds needed for B2 (`4ψ.N ≤ ⌊Y^{ε/5}⌋`, `q≠3`, `e ≥ e₀`; `supplyOfAdmOf.lean:39–92`).
4. `notes/units/V4-COND_round3.md`, step 1, sentence "Its rank t is at most ⌊x^400⌋₊": give the source (item in correction 2) instead of asserting it.
5. `notes/units/V4-COND_round3.md`, step 2, sentence "Apply Green and C1–C13 to its selections and to the request": spell out the construction of the C3 hypothesis from C5, C12, C6, C4 and the F-fields `hMt`, `hRB`, `aC2`, `rRows` (`TPS/TopShape.lean:37–47`), or mark the step as outlined and point to B05.
6. `notes/units/V4-COND_round3.md`, step 4: label the Mellin/Landau paragraph as a sketch and cite `formB` (P018) as the result being used.
7. `notes/units/V4-COND_round3.md`, step 3: add P021 to the list of what "P017 with list A" needs (through B10).
8. `notes/units/B09_v4.md`, paragraph "Finite-group average and B09", sentence "At a thick place … costs at most 3(x+1)(η+1)": state the width-Lipschitz bound `|wG_ξ(A/w) − bG_ξ(A/b)| ≤ 3A|w−b|/min(w,b)` and cite D562 (A9), `lipschitz_weight_all` (`CSW/LipschitzWeightAndMinimum.lean:957–964`; used at `LT/ChCore.lean:117, 308`). Add it to the input paragraph as well.
9. `notes/units/B09_v4.md`, paragraph "Character inputs at the same host": replace by (or precede with) a self-contained statement of B09 with abstract `c, M, K_o, C_E` and the `CharsA` clauses as hypotheses; move `HostAx`/`EAtH`, D547 and D549 to B08, where they are used.
10. `notes/units/B09_v4.md`, before "The balance identity now gives": add that `a_t>0` follows from `|a_t/b − x| ≤ 1`, `x≥3`, `b>0` (`LT/ChCore.lean:292–295`).
11. `notes/units/B08_v4.md`, sentence "The sizes, thinness, costs and containment T₂⊂A₀ are fields of the same core package": add that `b≥1`, `xb ≤ a` (so `a≥0`), `k≥1`, `m ≤ x^{1/2+ε/2}` and `xm ≤ k` are taken from the error windows (`PC/CoreGm.lean:42–45, 55–56`).
12. `units/D561.yaml` (fields `lean`, `statement`) versus `notes/units/D561_v4.md` versus `data/round3_changes.json` entry `D561`: make them agree. Either the card pins `ch_balance` and `th_le` (what the note covers), or the note adds the statement and derivation of `CharacterBalanceMoves.core` (`LT/ChCore.lean:283–338`), which currently lives in B09_v4.
13. `notes/units/D561_v4.md`, bullet "For p∈S": add that such `p` is never inert because `F_p∈Φ`, so the first term of ASK has no `p∈S` (`LT/ChBalance.lean:163–167`).
14. `notes/units/D562_v4.md`, sentence "This is an elementary derivation of the estimate in `AN.psi_le_three`": add that Lean obtains it from Mathlib `Chebyshev.psi_le`. Extend the citation `GzLipschitz.lean:127–184` to include `lip_upto` (185) and `zetaPrimeSumErrorLipschitz` (220), the theorem `derivative_integral_all` actually calls (`CSW/LipschitzWeightAndMinimum.lean:967`).
15. `notes/units/D547_v4.md`, preamble "Assume … x>0": note that `gmA_eq` does not need `x>0` (`PC/GmAEq.lean:61–64`), or drop it from this note.

## 5. Optional improvements

1. P017_v4: say that `C_L` is a dummy (the `ValuesAtX` clause is discarded, `PC/LevelGmLeOnFamilyScales.lean:16`) and that `Ident→IdentU`, `BNBounds→BNBoundsU`, `arithOf=arith` are definitional (line 11).
2. B09_v4 / units/B09.yaml: record that `|c|≤1` is not used in the Lean proof of `ch_core`.
3. D550_v4: remove the unrelated definition of the bracket `E` from the header; state that the proof differs from Lean's little-o argument.
4. D567_v4: note that Lean uses `log k ≤ (1+e_K)y` (`CSW/SubThreeMulLogTwoLe.lean:236–242`) where the note uses `e_K·y`.
5. D014: keep one of the two notes as canonical; they are consistent but duplicate each other. Name quadratic reciprocity and the supplementary law as background.
6. V4-COND table row C2: the remark "The surrounding comparison must still supply the slope hypotheses used by the second-layer conditions" is unclear; `link_gl` takes `tie`, `hU`, `hG`, `hduty` only (`LinkGl.lean:14–18`).
7. V4-COND: state that `TopShapeAlt` is instantiated with `V := True`, `NR := True` (`TopShape.lean:33`, `TopPlug.lean:15`), so the two "proofs of P, Q" in row C13 are trivial.
8. B10_v4: D569 is linked as a separate unit ("Statement only") although the note proves it inline; update the card.

## 6. What was not checked

- No Lean build; no `#print axioms`; no check of `sorry`/axiom use anywhere.
- Paper v4/v3 page and lemma references in every note.
- Checksums in `data/round3_changes.json`, `data/round3_v4.json`, `data/editions.json`.
- Bodies of: `each_unit_bound_statement` dependencies, `formB` chain, `linkMu`, `hostOfFieldOf`, B1–B8 and C1–C13 proofs, `tops_sum_gen` after line 50, `card_PsiA_index`, `toE_bij`, `GzLipschitz.lean` proofs, `Supplements/Kernels/*`.
- `proposition_size_bound` was checked by redoing the mathematics and comparing statement and final constants, not line by line.
