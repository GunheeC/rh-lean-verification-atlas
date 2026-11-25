# W09 · The two individual symplectic Selmer bounds

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**Outlined · pending_review.** For each primitive $\chi$, W09 gives exponents for Cases II and III. Fix a large host of character $\chi$ and modulus $N$, an odd prime $\ell$, $0<e<t$, a coefficient ring $O$, and an allowed $\psi\in X_h(O,e)$. Let $\theta_0$ be the prime-to-$\ell$ part of $\psi$. The case predicate uses $\chi_P=\theta_0\,\mathrm{comp}_{\ell}(\theta_0)^{-1}$, removing its local $\ell$-component. `chiP` (`Development/AutomorphicArithmetic/AutomorphicVarieties/HeightAndVanishing/DirichletPrimeToLPartMulLPowerPart.lean:86-86`). Case II requires $e\ge2$, even order of $\chi_P$, and either $\ell\in B_\chi$ or $\ell-1\mid2e$. Case III requires $\ell\notin B_\chi$, $\ell-1\mid2e$, and $\psi$ nontrivial of odd order. Each conclusion comprises finiteness and
$$
      (\log\ell)\,v_\ell(\psi,e)\le(\ell N e)^C .
$$
Each use is at one character and prime. The prime-set summation belongs to [W13](../../units/W13.md). See paper v3 §5.45, p. 51, and v4 §5.45, p. 68. [Original statement](W09.tex). `CountShape` (`Development/AutomorphicArithmetic/AutomorphicVarieties/HeightAndVanishing/Counts.lean:60-63`). `CaseII` (`Development/AutomorphicArithmetic/AutomorphicVarieties/HeightAndVanishing/DirichletPrimeToLPartMulLPowerPart.lean:212-212`). `CaseIII` (`Development/AutomorphicArithmetic/AutomorphicVarieties/HeightAndVanishing/DirichletPrimeToLPartMulLPowerPart.lean:214-215`). `VLe` (`Development/AutomorphicArithmetic/AutomorphicVarieties/HeightAndVanishing/DirichletPrimeToLPartMulLPowerPart.lean:120-120`).

## Fix the cohomology witness before the coefficient field varies

Assume $H'$, the uniform cohomology inequality of [W05](../../units/W05.md), and the rank-four symplectic automorphy and density record of [W06](../../units/W06.md). Choose one $C_K$ from W05. The cohomological data and the unramified adjoint-lifting data are obtained from the same $H'$. Together with the three graded-algebra lemmas they give the matrix and rigidity inputs. The rank-four counting input comes from the classical part of $H'$. A separate residual argument uses the Bernoulli-unit result underlying [D108](../../units/D108.md). `countII_and_countIII_of_printsH_of_sp4In` (`Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/AdjointLiftingOfCohomology.lean:33-39`).

The final symplectic theorem needs two cohomological controls for every closure and prime. The first turns a continuous locally trivial cocycle with algebraic $\ell$-adic coefficients into a global coboundary under its character hypotheses. Its proof descends the character and then the cocycle to a finite coefficient field before applying its finite-dimensional criterion. The second controls finiteness of the localization length over each admissible integral coefficient ring. Here one passes to the abelian field cut out by the character together with the required cyclotomic roots. Both uses specialize the same $C_K$, Poitou–Tate, local finiteness and local duality to $\mathbb Q$. The binders in the second use still quantify over $O$. `soBar` (`Development/AutomorphicArithmetic/AutomorphicVarieties/LevelCohomology/FdAdjoinRange.lean:78-96`). `soFin` (`Development/AutomorphicArithmetic/AutomorphicVarieties/LevelCohomology/ExistsAb.lean:43-99`).

## Prove one estimate when enough roots are available

Work temporarily over a coefficient ring containing roots of the two prescribed $2$-power orders for this character. The auxiliary rank-four argument constructs good symplectic data and identifies their localization length on the Case II or Case III branch. Its deformation-model construction uses the cohomology inputs just supplied. The two branches choose different level parameters. In Case II the auxiliary multiplier is $1$; in Case III it is the fixed test parameter attached to $\chi$. The conductor exponent and divisibility relations are established before using the common comparison theorem. `main_big` (`Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/ConductorAtMapInjectiveCoeff.lean:68-102`).

The level calculation supplies the weights and positive level. A test prime chosen outside this level and the bad places gives a Frobenius comparison. Applied with rank-four automorphy and rigidity, the matrix inequality for that Frobenius gives finite length and a numerical upper bound. Its arithmetic estimate absorbs the level parameters into a power of $\ell Ne$ with exponent chosen from $\chi$. Finiteness is needed at this point to transport the normalized length through the comparison; the order-theoretic statement about a possible infinite length is checked first. `main_big` (`Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/ConductorAtMapInjectiveCoeff.lean:102-130`).

## Return to the requested ring

Given the reader's $O$, enlarge it inside the fixed closure to a common coefficient ring containing the $2^{n_{\rm II}+n_{\rm III}}$ roots required by the two procedures. Map $\psi$ along the inclusion. Injectivity preserves its kernel and its order, and the local conductor and parity agree after extension. Hence both $n_{\rm II}$ and $n_{\rm III}$ keep their values, the mapped character belongs to the same host set and the same case applies. Each separate required root order divides the chosen one. The preceding estimate is therefore available with its original exponent. `sp4Main_alt` (`Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/ConductorAtMapInjectiveCoeff.lean:131-164`).

The coefficient-independence theorem transports finiteness and the **normalized** numerical estimate back to $O$. A raw length over an enlarged discrete valuation ring would need a ramification normalization, so a bare comparison of two dimensions would leave a missing factor. The construction actually establishes a bound on the disjunction of Cases II and III, then gives the left and right restrictions to obtain the stated pair of results. [Related adjoint comparison](../../units/P025.md). `sp4Main_alt` (`Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/ConductorAtMapInjectiveCoeff.lean:162-171`).

**First referee check.** Verify that the coefficient change preserves the conductor and the order of the prime-to-$\ell$ part and that the length comparison refers to the same normalized invariant on both sides. All three are needed to descend the estimate.

## Round 4 source comparison

The symplectic argument called through `main_big` remains an input to this outline. The review followed the passage to a larger coefficient ring and the descent but left that inner construction open. The cohomological and automorphy bundles used at the head are explicit premises; source names alone do not establish equivalence with published formulations.

[`countII_and_countIII_of_printsH_of_sp4In` · `AdjointLiftingOfCohomology.lean:33–39`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/AdjointLiftingOfCohomology.lean#L33-L39)

## Status of literature-named inputs

- `UpperTheory.V.HV.U.pt_s` — in-repo constant (`Development/AutomorphicArithmetic/AutomorphicVarieties/ModularityArgument/ThresholdArguments/DenseThresholdCases/HVFinalU.lean:11`); not compared.
- `GlobalTheory.Mem.LiteralAutomorphy.LitCoh.pt` — record field (`Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/Brauer.lean:105–106`); not compared.
