# P090 · The full adelic law for the specified kernel

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 10,997 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**Outlined · pending_review.** One kernel and one determinant character satisfy the transformation, support and integrality requirements along the entire chosen chain. The statement lets adjacent stages use the same class representatives and character when a matrix step changes to a coupled step.

## Statement and hypotheses

For every chain and adelic datum $A$, determinant map $d$ and exponent $a$ satisfying the given adelic pin and tie conditions, the functions $\Xi=\Xi_{\rm ad}(A,a)$ and $\mu_T=\mu_{\rm of}(t,u,\mu,d)$ satisfy the entire $\mathrm{AdLawAt}$. The first function reads the prescribed adjacent kernels after change of frame, transforms under rational and level actions, depends only on the specified bad-place components, satisfies the local congruence condition, is supported on the prescribed denominator lattice and is integral off the designated primes. The second reads both rank-one determinants and class representatives, is algebraic and multiplicative on norm-one ideles, is trivial on the prescribed integral ideles, and on norm-one rational points is the product of the prescribed integral embedding powers. [`adLawAt_xiAd` · `AdelicChainDatumCharacterLawsJointKernel.lean:62-116`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/AdelicChainDatumCharacterLawsJointKernel.lean#L62-L116)

**Read alongside** [P134 · Depth-zero congruence in a represented base frame](../../units/P134.md) · [Z4.2.02 · Local realization of the tagged kernel](../../units/Z4.2.02.md).

## Fix the two functions

Work under the pin and tie for the given chain, finite adelic data, determinant map and exponent. Choose the functions appearing in the claim itself. Existence of chart representatives holds at each step, and the distinguished representative of each class is one such point. At the coupling step the coset of this representative is prescribed. Independently obtain the norm-one character laws from the given pin and tie. A local comparison for the kernel alone would leave the class character unidentified. [`adLawAt_xiAd` · `AdelicChainDatumCharacterLawsJointKernel.lean:62-69`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/AdelicChainDatumCharacterLawsJointKernel.lean#L62-L69) · [`xiAd_eq_of_isPtAd` · `AdelicChainDatumCharacterLawsJointKernel.lean:33-42`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/AdelicChainDatumCharacterLawsJointKernel.lean#L33-L42)

## Check independence before checking level transformations

Split the index according as it is less than, equal to, or greater than the index of first coupling. The first region uses matrix-step independence, the second uses the first coupled calculation, and the last uses terminal independence. This supplies invariance under changes away from the specified bad components for every step. Repeat the partition for level equivariance, now using the corresponding independence result along with the character law and existence of points. Rational invariance uses the all-step independence result. The separate size and integrality inputs supply the local constancy/congruence and support fields and the value in the off-bad integral ring. [`adLawAt_xiAd` · `AdelicChainDatumCharacterLawsJointKernel.lean:70-84`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/AdelicChainDatumCharacterLawsJointKernel.lean#L70-L84)

## Identify the actual values

Rewrite the chosen kernel using the point-reading lemma for actual chart representatives at the two consecutive stages. On a matrix step, apply the first chain identity. On the first coupled step the formula takes the coupling coset of the second representative; at the final step it takes that of the first. Independence for the function of the kernel argument follows by choosing representatives for both pairs and applying the already established point independence. These checks compare values of the particular global function defined by choosing representatives. They justify using it even with a different valid choice of representatives. [`adLawAt_xiAd` · `AdelicChainDatumCharacterLawsJointKernel.lean:85-106`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/AdelicChainDatumCharacterLawsJointKernel.lean#L85-L106) · [`adLawAt_xiAd` · `AdelicChainDatumCharacterLawsJointKernel.lean:107-113`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/AdelicChainDatumCharacterLawsJointKernel.lean#L107-L113)

## Read the character on classes

For a unitary matrix in the specified finite adelic group, the determinant has norm one. Insert it in a one-dimensional scalar matrix. The norm-one identity verifies that the new matrix belongs to the rank-one unitary group, and the determinant of a one-dimensional matrix gives back the original determinant. Apply this to the representative for the class in question. The determinant part of the tie identifies the character with the prescribed class value; the remaining multiplicativity, algebraicity, unramified and rational-point properties are projections of the same character law. [`exists_u1Af_det` · `AdelicChainDatumCharacterLawsJointKernel.lean:44-58`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/AdelicChainDatumCharacterLawsJointKernel.lean#L44-L58) · [`adLawAt_xiAd` · `AdelicChainDatumCharacterLawsJointKernel.lean:114-116`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/AdelicChainDatumCharacterLawsJointKernel.lean#L114-L116)

**First step to challenge.** Check the two uses of the coupling-coset identity, on opposite sides of the transition. Reversing the adjacent representative in one use changes the kernel being read.

[Unit record and exact statement](../../units/P090.md)
