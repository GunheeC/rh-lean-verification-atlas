# W08 · Summing the Case I Selmer lengths over primes and characters

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**Outlined · pending_review.** For a primitive $\chi$ the bound chooses $C$ and two prime thresholds $r_1,r_2$ before the host. Fix a sufficiently large host $h$ of character $\chi$ with $q_1,d$ exceeding both primes, modulus $N$, and $0<e<t$. Let $T$ be any finite set of odd primes satisfying Case I ($\ell\notin B_\chi$ and $\ell-1\nmid2e$). At each prime choose its permitted coefficient ring $O_\ell$. The target includes finiteness of every localization length and the collective bound
$$
  \sum_{\ell\in T}\log\ell\sum_{\psi\in X_h(O_\ell,e)}v_\ell(\psi,e)\le(Nt)^C .
$$
Here $v_\ell$ denotes the normalized real length, after ruling out infinite length. The independence of $C$ from the size of $T$ is essential for [W13](../../units/W13.md). See paper v3 §5.44, p. 51, and v4 §5.44, p. 68. [Original statement](W08.tex). `CountI` (`Development/AutomorphicArithmetic/AutomorphicVarieties/HeightAndVanishing/Counts.lean:53-58`).

## Produce the one-character estimate

Start with the automorphic package $H'$, one witness for [W05](../../units/W05.md), the two-twist Kato vanishing of [W07](../../units/W07.md), and the rank-three automorphy input for unramified coefficients. The cohomological package is specialized to the rank-$n$ field of $H'$ with that very cohomology witness. The linked unramified endpoint, adjoint lifting, first and second rigidity and even-level admissibility are then applied to compatible data. The three algebraic inputs are the two graded length comparisons and the additional algebraic lemma supplied by this route. [P027](../../units/P027.md), [P028](../../units/P028.md). `count_i_of_printed_bound_k_kato_automorphy` (`Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/LinkedUnlE.lean:49-54`).

For one eligible character the finite-length and trace-difference bound is first proved in an unramified coefficient model. The prime-to-$\ell$ order allows a representative there with the same values inside $\overline{\mathbb Q}_\ell$. The pinned proof compares the good-data predicate, the normalized lengths and the twisted character values at the chosen Galois element and its inverse. This permits application of the unramified automorphy input. The integer used later in the sum must control characters in all the coefficient models selected by the reader. [D528](../../units/D528.md). `oneCharU_of_katoTwoW_rig_admI_automorphy` (`Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/FOneCharU.lean:75-95`).

## Turn local trace comparisons into a simultaneous orbit bound

Fix the imaginary quadratic field chosen from $\chi$, a kernel $H\subset(\mathbb Z/N)^\times$, and a good test prime $p$. The rank-three automorphic counting input is applied to all complex characters with that kernel. Their root-of-unity values and stability under coefficient conjugation supply the hypotheses of the counting input. It produces a nonzero integer with controlled logarithmic size and divisibility at the good coefficient primes. The proof chooses a place over $p$ and a Frobenius there and compares the complex and $\ell$-adic character orbits by an actual bijection. The one-character valuation inequalities can consequently be summed against the valuation of this same integer. `propGK_of_numberU3U_of_oneCharU` (`Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/FPropGKU.lean:118-145`). `propGK_of_numberU3U_of_oneCharU` (`Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/FPropGKU.lean:146-172`).

There are two test primes because the comparison at $p$ excludes $\ell=p$. Apply it at $r_1$ and $r_2$ to obtain nonzero integers $n_1,n_2$. For every admitted $\ell$, one of the primes differs from $\ell$; nonnegativity allows the orbit bound $2v_\ell(n_1)+2v_\ell(n_2)$ uniformly. Factorization of a nonzero integer gives $\sum_{\ell\in T}v_\ell(n_i)\log\ell\le\log|n_i|$. Thus the weighted orbit sum has cost at most
$$
  2c_5\,\varphi([(\mathbb Z/N)^\times:H])\,[N(e+1)]^A
           (\log r_1+\log r_2).
$$
The argument also treats the empty prime set, with zero cost. `corGK` (`Development/AutomorphicArithmetic/AutomorphicVarieties/UnitaryThreeGroups/CorGSumLog.lean:37-73`). `countI` (`Development/AutomorphicArithmetic/AutomorphicVarieties/UnitaryThreeGroups/CountI.lean:61-75`).

## Sum over kernels and absorb the constants

Choose $r_1\ge30N_\chi p_K+1$ and $r_2>r_1$. The host conditions imply that both avoid $30N|\operatorname{disc}K|$. Form the finite collection of distinct kernels of the characters that occur, across all $\ell\in T$. For any such kernel the quotient of $(\mathbb Z/N)^\times$ is cyclic. It has exactly $\varphi([(\mathbb Z/N)^\times:H])$ faithful complex characters. Inflating them gives disjoint sets for distinct kernels. The sum of these cardinalities is therefore at most the number of characters of the ambient group, hence at most $N$. The source proves this estimate before exchanging the two finite sums. `countI` (`Development/AutomorphicArithmetic/AutomorphicVarieties/UnitaryThreeGroups/CountI.lean:22-62`). `countI` (`Development/AutomorphicArithmetic/AutomorphicVarieties/UnitaryThreeGroups/CountI.lean:76-102`).

Set $A_0=2c_5(\log r_1+\log r_2)$ and choose $k$ with $A_0\le16^k$. The host gives $N\ge16$ and $e+1\le t$. The resulting bound $A_0N[N(e+1)]^A$ is at most $(Nt)^{k+1+A}$. Every finite length was already supplied by the orbit estimate, including when distinct coefficient rings realize the same kernel. [D532](../../units/D532.md). `countI` (`Development/AutomorphicArithmetic/AutomorphicVarieties/UnitaryThreeGroups/CountI.lean:103-136`). `absorb` (`Development/AutomorphicArithmetic/AutomorphicVarieties/UnitaryThreeGroups/CountI.lean:12-20`).

**First referee check.** Follow the fixed-kernel bijection into the simultaneous trace estimate. Choosing a new test integer for each coefficient prime or each character would lose the collective bound.

## Round 4 source comparison

The head assumes `HypothesesH′`, one witness of ∃ CK, LemmaK CK, `KatoTwoW` and `AutomorphyUnramifiedCoefficientsAlt`. In particular the Kato vanishing package is a premise here. In the endpoint generated from the first premise, the call to the projected forms system has fourteen top-level arguments: global Artin reciprocity, local class field theory, `modU_of_printsH`, `modularity_n_of_printed_mult_comp`, `levEx`, `lamEx`, `b0Ex`, `unitary_three_automorphy_dense_of_prints`, `seed2_alt`, `twist_of_printed_results`, `alg_cyclotomic_of_printed_results`, `alg_restriction_of_printed_results`, `tanA` and `core_alt_bis`. These constructions reuse fields and intermediate results of the supplied record. The numerical count in the review omitted one argument. The names of the source inputs identify repository interfaces; equivalence with a published package is unchecked.

[`UpperTheory.V.Z.J.linkedUnlE_alt` · `LinkedUnlE.lean:43–48`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/LinkedUnlE.lean#L43-L48) · [`UpperTheory.V.Z.J.count_i_of_printed_bound_k_kato_automorphy` · `LinkedUnlE.lean:49–54`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/LinkedUnlE.lean#L49-L54)

## Status of literature-named inputs

- `UpperTheory.V.Z.J.count_i_of_printed_bound_k_kato_automorphy` — in-repo constant (`Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/LinkedUnlE.lean:49–54`); not compared.
- `UpperTheory.V.Z.Kato.WeilSphericalRecords.KatoTwoW` — hypothesis at this head (`Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/KatoQuadraticCharacters/SphericalDecomposition/KatoTwoW.lean:10–14`); not compared.
- `UpperTheory.V.Z.J.oneCharU_of_katoTwoW_rig_admI_automorphy` — in-repo constant (`Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/FOneCharU.lean:75–95`); not compared.
