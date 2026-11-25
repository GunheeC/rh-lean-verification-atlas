AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

# R4_review_Z2

AI review report produced during this project; file names are internal working names.

- Internal source file: `out/R4_review_Z2.md`
- SHA-256: `286e910f2743565d62dab15bf7f254eeeaeb16b481c1daf480526250d8cb7221`
- Report scope: Round-4 review: Z2.K2 and Z2.K7 (Chapter P, blueprint v6)

## Internal report

The report below preserves its original verdict, scope and unresolved points. Historical review-machine home prefixes are displayed as `${REVIEW_HOME}`; the source checksum above identifies the original report. Source line numbers in other records count from its original title.

# Round-4 review: Z2.K2 and Z2.K7 (Chapter P, blueprint v6)

Reviewed text: `${REVIEW_HOME}/work/prev4/ch_P.tex`

- K2: Proposition `prop:P-k-few` (lines 207-316), the two K2 paragraphs (lines 1110-1438).
- K7: paragraph "K7. The class number and exponent 24" (lines 1493-1546), Proposition `prop:P-r4-k7` (lines 1548-1806), and the use site in `prop:P-k-num` (lines 660-676).

Checked against the cleaned Lean copy `${REVIEW_HOME}/src/rh/src/` and the dependency graph (`graphq.py find/deps/callers/path`). Line numbers quoted in the chapter agree with the graph (original tree); the cleaned copy is shifted by a few lines. The original read-only tree was not opened separately. Nothing here says or implies that RH is proved; both items are conditional pieces of the Z2 bound.

---

## Z2.K2 (`UpperTheory.V.ZK.sClassOf`, with `sCoc`, `sTrans`, `sThetaOf`, `sPhi`, `sEta`, `SRel_of`, `SStein_of`)

### Verdict: COMPLETE WITH GAPS

The gaps are expository (sketched or silently used standard steps). I found no mathematical error and no mismatch with the Lean statements.

### 1. Is "complete" earned?

Steps I re-derived and found fully written and correct:

- `zc` is a cycle (face pairing (1,2),...,(2E-1,2E); first face killed by q = 0).
- Prism boundary identity (`SPrism`).
- Trivial-group clause of `SChain` (differentials alternate 0, 1).
- The 2-cocycle U, its symmetry, the cochain t = U^E cup v, cancellation of insertions in pairs, and the telescoping sum giving x^E v(g) (`SCoc`).
- Projective-line transfer: cocycle c(g,x), compatibility with faces, direct-sum additivity with multiplicity |W| = 1 in Z/q, dimension one (`STrans`).
- Integral interpolation: (T - kappa^j) J^j f divisible by J^{j+1}, hence ([w]-1)^m | B; [t0-t]-1 | [w]-1; the product with [(-t,1)]-1 (`SEta`).
- Steinitz step I + J = O + IJ and the determinant correction (`SStein`).
- Divisor of beta: ord_P beta = sum A_i D(gamma^i P), and S(beta) = p(a) S(alpha) = P_E v(r(N_a(alpha))) (`cBetaDiv`, `cBetaVal`).
- Order of kappa mod q equals |gamma|, so the twist s_j = gamma^{-i} is well defined (`cGtEq`).
- The integral cycle sigma_* b - rho_* b + sum n_t prism_{k_t}((sigma d_t)_* z) and its identification in the ambient group (`cChain`).
- One localization b chosen before the reduction r; splitting of k tensor O_F (`cSplit`, `cSupp`, `cLatLoc`).

Steps asserted without a written proof, an earlier item, a citation, or a "Proved in Lean, not reproduced" label:

1. **Relation `SRel` (lines 1125-1137).** The text computes H_{2E}(C^2, Z/q) = R^{2E+1} from the tensor product of two periodic resolutions, but the relation is needed as a boundary in the unnormalized bar complex `Ch`. The comparison between bar homology and the homology computed from another free resolution is used silently, with no citation. The Lean proof goes a different way (`gen_two`: generation by 2E+1 elements via coinduced modules and long exact sequences; `d_eq_bd`, `rel_bd`), so this is an unlabelled alternative argument.
2. **Prism composition `SPrismMul` (lines 1241-1249).** Only a triangulation sketch, with signs "up to overall sign" and the three side faces asserted. The Lean proof (`SPrismMul.lean`, cone/homogeneous calculation, about 200 lines) is not reproduced, and the step is not labelled as such.
3. **Change of homogeneous section in the transfer (lines 1292-1300).** The insertion prism is described "up to orientation"; its boundary identity is asserted (`tr_cob`).
4. **Block evaluation (`cBlockVal`, lines 1203-1216 and 1407-1410).** `IsAdd.add` is stated for pushforwards cm(sumRep rho sigma) z of a cycle z of an abstract group. The text applies additivity to prism_g(rho_* z) with g block diagonal and commuting, without saying why this chain is such a pushforward (one needs an auxiliary group such as C x Z, or the Lean device in `CBlockVal.lean:34-69`). Same remark for "Additivity on direct sums then reduces the evaluation to the one-dimensional character" in the determinant step.
5. **Edge case q = 1 in `STheta`.** The transvection argument needs a in k with a not 0, 1, supplied by "a primitive q-th root ... here". For q = 1 (allowed by the Lean statement, `[NeZero q]`) and k = F_2 there is no such a; the statement is then trivial because Z/1 = 0, but the text does not say so. Irrelevant for the application (q = l^nu, nu >= c >= 1).
6. **Split coordinates (lines 1399-1406).** The identity s_j((g_t w)_j) = (A_x (s_i w_i))_j and "applying r tau gives exactly these entries" are one-line assertions standing for `cVal` (`BlkEquiv.lean`), `cMu`, `cInt`. The lemmas `cMu` (230 lines), `cInt` (160 lines), `cAct`, `cRep`, `cUnit`, `cSupp` are arguments of `cJoin` but are not named in the text; their content is covered only in prose.

### 2. Statements

All match. Details checked:

- `SClass`: hypotheses `Lay l c nu zeta gamma`, `2*e+3 < l^c`, `DivDel gamma ((1+l^c)^(e+1)) alpha d`; conclusion exists N, y, b with `Cyc y`, `b != 0`, and for every finite field k, r surjective on O_L with r b != 0, every theta with `IsAdd` and `HasVal` (root only required to satisfy zeta^q = 1), the value `pe (1+l^c) (2e+3) (e+1) * v u` with `Res r (nrm ...) u`. The text has the same quantifier order (cycle and b before r, k, v, theta), the same range (E = e+1 >= 1, 2E+1 < l^c) and P_E = prod_{i < 2E+1, i != E}(kappa^E - kappa^i).
- `SCoc`: degree 2e+3 = 2E+1, primitive root required, value x^(e+1) v(g). Matches.
- `STrans`: hypothesis (card k : A) = 1 appears in the text as |W| = 1 in R. Matches.
- `SEta`: M < l^c, c <= nu, Fin (M+1), coefficients of prod_{j<M}(X - kappa^j). Matches with M = m.
- `SStein`: `Nonempty J or beta = 1`; text treats rank zero. Matches.
- `SRel`: Fin (2e+4) = m+1 maps d_t, unit coefficient at some t0. Matches.
- `SPhi` / `IsPrimFam`: boundary, stabilization, d-fold repetition. Matches.
- Conventions `DivDel`, `nrm`, `polAct` (uses gamma^{-i}), `Carries` (determinant beta on the block x = 1, 1 elsewhere), `CVal` formula sum_sigma sum_x (kap(sigma) x)^E f(sigma delta_x): all as in the text.

Minor: the Lean b is in O_L (= O_M) inside `cJoin` and is exported as an element of O_F; the text says b in O_M. Harmless.

### 3. Proofs

No wrong inequality, missing case or out-of-range step found. Points verified numerically or by hand:

- v_l(t0 - t) < c because |t0 - t| <= m < l^c, so w = l^c is a multiple of t0 - t in Z/q.
- Coincident powers kappa^i mod q (when l^{nu-c} < m+1) are handled ("coincident powers contribute the sum of their coefficients").
- Empty weight blocks: determinant 1; the weight-1 block contains (1,0), matching the `exists j, chi j = 1` hypothesis of `CGtEq`.
- The scaling by n_{t0}^{-1} is on Z/q-chains and does not depend on r, although the sentence places it "after reducing"; ordering of choices is otherwise respected.
- l = 2 uses c >= 2 (`Lay.c_two`) where the binomial valuation is used.

### 4. Labels

There are no "Hypothesis, discharged at" brackets in the K2 text. The supply claims are correct:

- `graphq callers` gives `UpperTheory.V.ZK.lemmaK` (`LemmaKOfLitN.lean:28-31`) as the only caller of `sClassOf`, `sCoc`, `sTrans`, `sThetaOf`, `sPhi`, `sEta`.
- `SRel` and `SStein` are supplied there by `LateralTheory.Fin.SRel.intersectionNumber_baseChange` and `LateralTheory.Fin.SStein.intersectionNumber_baseChange`, which are `SRel_of` and `SStein_of` with no extra hypotheses.
- `sClassOf` = `cJoin cChain cFree cTriv cAct cSplit cSupp cLatLoc cMu cInt cVal cGtNe cGtEq cBetaDiv cBetaVal cRep cUnit`; no hypothesis left open. `lemmaK` itself still carries `BOdd`, Poitou-Tate, `LocalFinitenessK`, `LocalTateDualityK`, none of which belongs to K2.
- Citation nits: `sPhi` is `PiRepApply.lean:82-154` (text and notes stop at 116); `SStein_of` is `SSteinTPf.lean:203-228` (text: 191-227).

### 5. Understanding

The text does explain why the result holds. A fixed integral bar cycle z of the cyclic group is pushed into the lattice stabilizer along m+1 diagonal maps; a linear relation among the pushforwards (available because H_{2E}(C^2, Z/q) has only 2E+1 generators) is turned into a degree-(2E+1) cycle by conjugating with lattice transports g_t. The scalar cochain U^E cup v, transferred over projective lines, reads off x^E v(det) on each scalar-character block, so the value of the class is governed entirely by the block determinants of the g_t. The interpolation multiplicities eta are designed so that all determinants are 1 except beta on one block, and the polynomial p turns beta into P_E times the twisted norm. Choosing one denominator b before any reduction is what makes a single integral class work at every allowed prime. The reader can follow the mechanism; what is thin is the homological bookkeeping listed in section 1.

### Most important problems (K2)

1. `SRel`: bar-complex versus resolution comparison used without statement or citation; the hand argument differs from the Lean route and is not marked as an alternative.
2. `SPrismMul` and the transfer change-of-section prism are sketches with unverified signs, not labelled "Proved in Lean, not reproduced".
3. Additivity is applied to prism chains of block-diagonal commuting elements without the reduction to a pushforward of a cycle (`cBlockVal`).
4. Split-coordinate identification (`cVal`, `cMu`, `cInt`) is asserted in two sentences; several `cJoin` inputs are never named.
5. q = 1 not covered in the determinant step for `STheta` (trivial, but unstated).

---

## Z2.K7 (`UpperTheory.V.KT.tors_le`, `UpperTheory.V.ZK.torsAll`, `sTors`)

### Verdict: COMPLETE CONFIRMED

Two minor remarks below; neither affects the bound or the exponent 24.

### 1. Is "complete" earned?

Every step is written out or is a cited published theorem:

- Class number: Minkowski bound (Milne, ANT, Theorem 4.3, checked: integral representative of norm at most (4/pi)^{r2} (n!/n^n) sqrt D); constant at most 1; slot encoding of ideals; tuple count X(1+log X)^{n-1}; log h <= n log D / 2; floor(log_2 h) <= 4n log(2D).
- Geometry: covolume (2^{-n/2} sqrt D)^N; elements of P are positive definite; local finiteness; vertices, normal cones, cover of U and finiteness over compacta; existence of extreme minimizers with spanning active set.
- Exactness of the ordered nerve complex: hand proof via thickened finite convex cover and a double complex.
- Orbit count: common minimal vectors at the barycentre span M^N; det H identity and packing bound; Hadamard; I <= I_0; eigenvalue bound; B' = I B^{-1} integral; residue of B' mod I determines B up to G; conjugate bound R and separation mod 2R+1; exponent 12(p+1)d^3 N.
- Stabilizers: finiteness, injectivity of reduction mod 3 on finite subgroups, s = 3^{dN}.
- Homology: Shapiro, |H| kills positive-degree homology, order |H|^{|H|^j}, dimension shifting through M_{i+1} = ker(C_i -> M_i), cokernel torsion bounded by a minor and Hadamard.
- Numerics: 1,920,300 u^5 L_0, 7,681,212 < 2^24, exponent (2En)^24 log(2D).

Remarks:

1. **Exactness (lines 1643-1671).** The hand proof is explicitly announced as different from the Lean route (`nerve_compact`, hyperplane cuts), which is correct practice, but it relies on two textbook facts without a reference: chains subordinate to an open cover compute singular homology (barycentric subdivision), and the two-way computation of a first-quadrant double complex with exact rows/columns. The sketch is correct (the thickening to open convex sets is exactly what the subdivision theorem needs, and ordered tuples with repetition match `simp`/`nerve`). A citation would close it.
2. **Statement form.** See item 2.

### 2. Statements

- Lean: `tors_le (L) [IsTotallyComplex L] (N m) : TorsLe (HGL L N m) (bound m (orbBound L N m) (3^(dd L N * N)) (m+2))`, with `bound m A s b = b^A * s^(m*A*s^m)`, `orbBound = I0^(1+dN) * ((2R+1)^d + 1)^(dN(p+1))`, `I0 = D^N d^d`, `RR = N^N I0^2`, `dd = n N`.
- Text: order at most (m+2)^A s^{m A s^m} with s = 3^{dN} and A = (2Dd)^{12(m+1)d^3 N}, for N >= 1.
- These agree after `orbnum` (`orbBound L N p <= (2 D d)^(12(p+1)d^3 N)` under `1 <= N`), which is how `torsAll` combines them. The text's I_0, R, Z are literally the Lean `I0`, `RR`, `(2R+1)^d`. The Lean `tors_le` has no N >= 1 hypothesis; the text's proposition adds it because it states the simplified A. No real mismatch.
- `torsAll`: C = 24, hypotheses totally complex, 1 <= e, 1 <= N <= 4e+6, m <= 2e+1; conclusion finiteness and log card <= kBound 24 e n D = exp((2en)^24 log(2D)). Text: same range ("1 <= N <= 4E+6, m <= 2E+1", endpoint m = 2E+1 included) and same bound.
- `STors` uses only N = 4E+6 and only the logarithmic conjunct; the text says so (lines 668-671).
- `log_classNumber_le` in Lean is log h <= log D / 2 + n log(1 + log D / 2); the text's log h <= n log D / 2 is a correct consequence of its own (slightly sharper) count. `gens_le` gives floor(log_2 h) <= 4n log(2D) as stated.

### 3. Proofs

Checked by hand; all constants follow:

- log of bound <= A s^{m+1}(2m+1) (`TorsLe.log_le_exp`), then exponent (m+1){12 d^3 N log(2Dd) + 2dN} + 2m, exactly the left side of `exponent_le`.
- log(2Dd) <= L_0 + d - 1 <= 16 u L_0 uses L_0 > 0.69; 12 * 10^4 * 16 = 1,920,000; 200 u^2 <= 300 u^5 L_0; 4u * 1,920,300 + 12 = 7,681,212 < 16,777,216.
- det H >= d^{-d} from the open cube of side 1/sqrt d; prod det h'_v >= 1/I_0 with slack.
- I^{nN^2} residue matrices, sum over I <= I_0 gives I_0^{1+dN}; dim_R V = nN^2/2 <= dN.
- Exponent split 2d(1+dN) <= 4(p+1)d^3N and ((5d+2)d+1) dN(p+1) <= 8(p+1)d^3N.
- Minkowski mod 3: for p = 3 the terms after 3^{a+1}Y are divisible by 3^{a+2} since a >= 1.
- Dimension shift: exactness is needed at C_0,...,C_m (this is `FaceExactTo ... m`), kernel of H_j(G,M_i) -> H_{j-1}(G,M_{i+1}) is an image of H_j(G,C_i), product s^{A sum_{j=1}^m s^j} <= s^{A m s^m}; final cokernel torsion <= (m+2)^A; m = 0 is covered.

No wrong direction, missing case, or out-of-range step found.

### 4. Labels

No "Hypothesis, discharged at" brackets. Supply claims verified with graphq:

- `tors_le` is called by `torsAll` (and by `Up.torsStab`, the K4 finiteness use mentioned in the text).
- `torsAll` is called only by `sTors` (`ExponentLe.lean:122-125`).
- `sTors` is called only by `lemmaK` (`LemmaKOfLitN.lean:28-31`), where it is the `STors` argument of `lemmaK_of_steps`.
- `tors_le` depends on `mainFace`, `sx_exact` (from `acyc_simp` and `tupExact`), `orb`, `orbBound_mono`, `stab`; none carries an undischarged hypothesis.

### 5. Understanding

Yes. The text makes clear why an all-prime torsion bound exists: GL_N(O_M) acts on the vertices of the polyhedron of Hermitian forms with minimum at least 1, the ordered nerve of the normal cones is exact because the cones form a locally finite convex cover of a convex set, and reduction theory (common minimal vectors, a bounded index I, bounded conjugates) bounds the number of orbits while Minkowski's mod-3 lemma bounds the stabilizers. Equivariant homology then splits the torsion into stabilizer contributions (killed by |H|, bounded rank) and one integer matrix with small columns whose cokernel torsion is bounded by a minor. The final numerical step shows transparently where 24 comes from (u^6 with a constant below 2^24). The class-number estimate is likewise explained from first principles.

### Most important problems (K7)

1. Exactness of the ordered nerve complex uses the subordinate-chains theorem and a double-complex comparison without a reference; the argument is sound but is an uncited alternative to the Lean proof.
2. The proposition states the simplified orbit constant A and N >= 1, whereas `tors_le` is stated with `orbBound` and no restriction on N; the link (`orbnum`) is cited but the proposition's `\lean{}` tag points at `tors_le` alone.
3. No other issue found.
