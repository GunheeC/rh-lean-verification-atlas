# W11 · A uniform class-group rank bound in every cyclotomic layer

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**Outlined · pending_review.** Fix a prime $\ell$ and a finite abelian extension $K/\mathbb Q$ containing a primitive $\ell$th root of unity for odd $\ell$, or a primitive fourth root for $\ell=2$. Write
$$
d_\ell(F)=\big|\mathrm{Cl}(F)/\mathrm{Cl}(F)^\ell\big|.
$$
W11 gives an integer $r$ depending on $\ell,K$ such that $d_\ell(K')\le\ell^r$ for every $n\ge0$ and every field model $K'$ of $K(\mu_{\ell^n})$ over $K$. Since the quotient has exponent dividing $\ell$, this bounds its dimension as an $\mathbb F_\ell$-vector space. The next consumer, [W12](../../units/W12.md), needs uniformity in the layer. See paper v3 §5.47, p. 52, and v4 §5.47, p. 69. [Original statement and commentary](W11.tex). `FerreroWashington` (`Development/AutomorphicArithmetic/AutomorphicVarieties/PublishedTheorems/FerreroWashington.lean:7-11`).

## Embed all layers with a controlled relative degree

Choose a cyclotomic field containing a copy of $K$, using the abelian-extension input of the source. Factor its conductor as $\ell^a f_0$ with $\ell\nmid f_0$. Set
$$
 f=f_0(\ell+1),\qquad D=f\ell^a .
$$
This harmless enlargement ensures $f>1$ and $(f,\ell)=1$. For a proposed tower threshold $n_0$ and any input layer $n$, put $m=n+a+n_0$. The embedding construction supplies $K'\subset L$ with $L$ a model of the cyclotomic field of conductor $f\ell^m$ over $\mathbb Q$. It works for the actual input model of $K'$, using its cyclotomic algebra structure. `embed` (`Development/AutomorphicArithmetic/AutomorphicVarieties/GaloisLibrary/FerreroWashingtonIndex/EmbedDeg.lean:16-53`).

Here is the degree comparison that makes this maneuver uniform. The absolute degree of $L$ is $\varphi(f\ell^m)$, while the primitive root in $K'$ gives $[K':\mathbb Q]\ge\varphi(\ell^n)$. By multiplicativity and the prime-power totient inequality,
$$
 \varphi(f\ell^m)\le f\ell^{a+n_0}\varphi(\ell^n).
$$
Dividing the tower-degree identity by the positive number $\varphi(\ell^n)$ gives $[L:K']\le D\ell^{n_0}$. Even $n=0$ is covered. Thus the degree cost of moving to a layer above a fixed threshold is independent of the moving layer. `embed` (`Development/AutomorphicArithmetic/AutomorphicVarieties/GaloisLibrary/FerreroWashingtonIndex/EmbedDeg.lean:54-78`).

## Bound the cyclotomic quotient at a fixed tame conductor

For this one $f$, the intermediate theorem supplies $B,n_0$ before it sees $m$ or $L$. On the tail, $L$ is totally complex and $d_\ell(L)\le B$. The construction chooses an auxiliary odd integer $2f\ell+1$, prime to $f\ell$, and obtains uniform parameters from the group-ring containment and ambiguous-class estimates. The containment acts on the class group through the cyclotomic action. In particular the intersection of the difference subgroup for complex conjugation with the $\ell$-torsion is bounded by $B_0^N$, with $B_0,N$ independent of the layer. `cyc` (`Development/AutomorphicArithmetic/AutomorphicVarieties/GaloisLibrary/FerreroWashingtonIndex/FerreroWashington.lean:18-33`). `cyc` (`Development/AutomorphicArithmetic/AutomorphicVarieties/GaloisLibrary/FerreroWashingtonIndex/FerreroWashington.lean:42-55`). `cyc` (`Development/AutomorphicArithmetic/AutomorphicVarieties/GaloisLibrary/FerreroWashingtonIndex/FerreroWashington.lean:77-90`).

For odd $\ell$, the field on the chosen tail contains a primitive $\ell$th root. The reflection inequality and the odd-prime group estimate then turn the bound on that intersection into a quotient bound $\ell(B_0^N)^2$. At two the proof uses separate sign information for the conjugation involution and the two-primary group estimate. Writing $a_2$ for the source’s fixed base-layer exponent at two, the resulting cardinality bound is $[(2^{\varphi(f2^{a_2})})^N B_0^N]^2$. A bound on only the difference subgroup would omit that factor. Both branches produce the same *kind* of output, one constant for every large $m$. These uniform group-ring, sign and reflection estimates are substantive lower inputs. `cyc` (`Development/AutomorphicArithmetic/AutomorphicVarieties/GaloisLibrary/FerreroWashingtonIndex/FerreroWashington.lean:54-66`). `cyc` (`Development/AutomorphicArithmetic/AutomorphicVarieties/GaloisLibrary/FerreroWashingtonIndex/FerreroWashington.lean:89-102`).

## Descend and choose the exponent

For totally complex $L$, class-field descent gives $d_\ell(K')\le [L:K']d_\ell(L)$. The proof counts characters to $\mathbb Z/\ell$. Restriction via the Artin map has kernel of cardinality at most the subgroup index $[L:K']$. Its image is accounted for by unramified class-group characters over $L$. Counting that kernel and image gives the product bound. This argument avoids assuming injectivity of extension on ideal classes. `desc` (`Development/AutomorphicArithmetic/AutomorphicVarieties/GaloisLibrary/FerreroWashingtonIndex/CardClDualOne.lean:10-39`). `desc` (`Development/AutomorphicArithmetic/AutomorphicVarieties/GaloisLibrary/FerreroWashingtonIndex/CardClDualOne.lean:40-94`).

Apply the tail bound at the *lifted* index $m$ and multiply the two bounds. The fixed integer $R=D\ell^{n_0}B$ bounds $d_\ell(K')$ for every original $n$. Taking $r=R$ suffices since $R\le\ell^R$ for $\ell>1$. The proof introduces the root-of-unity premise of W11, while the embedding and descent estimates used at its outermost step already hold in the displayed wider abelian setting. `ferreroWashington` (`Development/AutomorphicArithmetic/AutomorphicVarieties/GaloisLibrary/FerreroWashingtonIndex/FerreroWashington.lean:104-119`).

**First referee check.** In the two-primary branch, trace the sign bound through conjugation and the square in the final index estimate. A layer-dependent sign bound here would invalidate the subsequent choice of one $r$.

## Round 4 source comparison

The containment in the integral group ring is `memZ`: a single power of $\gamma-1$ lies in the ideal generated by the theta element, $1+[-1]$ and $\ell$, throughout the indicated tail. This carries the μ=0-type content of this construction. The distinct input `ambCyc` bounds a class-group index. Both are proved by terms in the repository. At the root the primitive-root hypothesis in the published predicate is introduced anonymously and unused. The result indexed here bounds the rank of the class-group quotient in a tower. The note has not established equivalence with the published Ferrero–Washington theorem.

[`UpperTheory.V.FW.memZ` · `ToKOf.lean:13–14`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/GaloisLibrary/FerreroWashingtonIndex/ToKOf.lean#L13-L14) · [`UpperTheory.V.FW.ambCyc` · `AmbCyc.lean:9–10`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/GaloisLibrary/FerreroWashingtonIndex/AmbCyc.lean#L9-L10) · [`UpperTheory.V.FW.ferreroWashington` · `FerreroWashington.lean:104–119`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/AutomorphicVarieties/GaloisLibrary/FerreroWashingtonIndex/FerreroWashington.lean#L104-L119)

## Status of literature-named inputs

- `UpperTheory.V.FW.ferreroWashington` — in-repo constant (`Development/AutomorphicArithmetic/AutomorphicVarieties/GaloisLibrary/FerreroWashingtonIndex/FerreroWashington.lean:104–119`); variant.
