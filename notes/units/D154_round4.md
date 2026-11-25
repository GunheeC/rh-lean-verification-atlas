# D154 · Hyperplane sections of the Chow form

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 0 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**Outlined · pending_review.** A hyperplane cuts the original cycle into components with multiplicities. Specializing one block of the Chow form records exactly those components as factors. The scalar ambiguity is harmless for this factorization, but the multiplicities and the requirement that the hyperplane avoid the original prime are essential.

## Claim and hypotheses

Slicing the first block of the Chow form by a hyperplane gives, up to a nonzero scalar, the product of the component Chow forms raised to the intersection multiplicities.
$$
\exists c\in k^\times,\qquad f(u,-)=c\prod_{Q\in\operatorname{supp}(P\cap H_u)}g_Q^{m_Q}.
$$

[`ChowFormCompatibility.chow_form_hyperplane_section` · `ChowFormHyperplaneSection.lean:12–38`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/NefModelVolumes/ChowFormHyperplaneSection.lean#L12-L38)

## Which polynomial is specialized?

Take a characteristic-zero field and a homogeneous prime $P$ in a polynomial ring on $N$ variables. Its quotient has Krull dimension $e+2$. Choose a linear form with coefficient vector $u$ outside $P$. The input $f$ is a Chow form in $e+2$ blocks, and a component form $g_Q$ uses $e+1$ blocks. The choice of $g_Q$ is arbitrary subject to the Chow condition on every component in the section cycle. The output concerns a polynomial in the remaining blocks, with one nonzero scalar allowed for the entire identity. [`GlobalTheory.Published.ChowFormHyperplaneSection` · `IsMultiHomogeneousFixFirstBlock.lean:122–132`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/PublishedTheorems/Divisors₂/IsMultiHomogeneousFixFirstBlock.lean#L122-L132)

## Pass from incidence to the geometric section formula

First prove relevance. If every variable lay in $P$, then multiplying each variable by its hyperplane coefficient and summing would put the linear form in $P$, contrary to hypothesis. This combines with primeness and homogeneity to give a projective prime. The integral Chow predicate supplies a nonzero polynomial with the required divisibility characterization on incidence tuples: divisibility implies vanishing there by multiplication, and universal vanishing gives divisibility by the input predicate. The geometric section theorem can now return some component forms $g'_Q$ and a scalar $c$. Its proof of that section identity is an input here. [`ChowFormCompatibility.chow_form_hyperplane_section` · `ChowFormHyperplaneSection.lean:12–24`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/NefModelVolumes/ChowFormHyperplaneSection.lean#L12-L24) [`ChowFormCompatibility.chow_form_of_integral_version` · `ChowFormOfIntegralVersion.lean:8–13`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/NefModelVolumes/ChowFormOfIntegralVersion.lean#L8-L13)

## Transfer the multiplicities and the specialization

There are two definitions of the cycle. On a relevant component compare the multiplicity in the projective cycle with the locally computed multiplicity, applying the natural-number realization of the extended value. Away from the component support both coefficients vanish. This proves equality of the finitely supported functions, including their exponents. There are also two first-block substitutions. The variable in block zero is sent to the constant coefficient $u_j$, and a variable in a successor block is reindexed unchanged. Agreement on variables gives equality of the polynomial substitutions. [`ChowFormCompatibility.projCycle_eq_fundCycle` · `HyperplaneSectionDivCycle.lean:8–20`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/NefModelVolumes/HyperplaneSectionDivCycle.lean#L8-L20) [`ChowFormCompatibility.hyperplane_section_divCycle` · `HyperplaneSectionDivCycle.lean:22–34`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/NefModelVolumes/HyperplaneSectionDivCycle.lean#L22-L34)

## Change each representative only once

For each component the two candidate Chow forms divide one another. They are associated, and a polynomial unit over a field is a nonzero constant. Write $g'_Q=a_Qg_Q$. If its multiplicity is $m_Q$, the replacement contributes $a_Q^{m_Q}$ to the scalar. Multiplication over the finite support produces $c\prod_Q a_Q^{m_Q}$, nonzero since each factor is nonzero. Rearranging finite products finishes the statement. The scalar can depend on the chosen representatives. The multiplicity exponent cannot be absorbed by rescaling the polynomial. [`ChowFormCompatibility.chow_form_unique_up_to_constant` · `ChowFormUniqueUpToConstant.lean:8–15`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/NefModelVolumes/ChowFormUniqueUpToConstant.lean#L8-L15) [`ChowFormCompatibility.chow_form_hyperplane_section` · `ChowFormHyperplaneSection.lean:25–38`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/WeilBound/CoreStatements/NefModelVolumes/ChowFormHyperplaneSection.lean#L25-L38)

## First step to challenge

Check the equality of the section cycle and the divisor cycle component by component, including the local multiplicity. Equality of their underlying supports does not suffice.

The height normalization is treated in [D155](../../units/D155.md), and the resulting image-height comparison in [T16](../../units/T16.md).
