# D014 · Inertia and Frobenius for the arithmetic of a fixed host

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**Full · pending_review.** This proof concerns the local arithmetic of an axial host already given on a frame. The [unit statement](../../units/D014.md) is in manuscript v3, Appendix G.16, p. 160. The [v4 proof of Lemma 3.7](D014_v4.md), §3.1, pp. 15–16, gives the same eight fields. Its consumers include the [host window estimate](../../units/B08.md). All source locators below use the Lean commit in the unit record.

## The conductor and the sign

Write $Q$ for the host’s positive integer $\mathrm{QS}$, $q$ for its distinguished prime and $d$ for its other distinguished prime. The conductor is $N=Qqd$, with $d$ prime to $Qq$ and $d\equiv3\bmod 4$. Write $S$ for the prime factors of $Qq$. The arithmetic record is obtained by sending a unit modulo $N$ through the host Artin map and then into the additive group of the frame. Call this composite $r$. Its sign coordinate determines the predicate $\mathrm{InPhi}$. A multiplicative sign of $+1$ corresponds to additive sign zero. The required exceptional inertia element is the particular frame element $\mathrm{sgc0}$. The eight fields of the conclusion specify both the prime set and the local images. See the definition of **HostFactsS** in `SplitInertia.lean:14-22` and the construction **hostFactsS_pf** in `hostFactsS.lean:44-57`.

Here is the sign test used twice below. If a unit $u$ is congruent to $k$ modulo $d$, its sign in the host is the Jacobi symbol $(k/d)$. Indeed the host’s Artin-character identity gives the symbol of a residue representative of $u$, and congruence modulo $d$ replaces that representative by $k$. Hence $(k/d)=1$ implies $\mathrm{InPhi}(r(u))$. The arithmetic sign is a unit, so equality of its underlying integers suffices before passing to additive notation. This proves **inPhi_of_jac**, `hostFactsS.lean:7-15`.

## Away from the distinguished prime

The elementary fields hold at once. The host makes $d$ prime, $2\mid Q$, $q$ prime and $d\nmid Qq$. Positivity gives $Qq\ne0$, so $2,q\in S$ and $d\notin S$. If $p$ is prime, $p\notin S$ and $p\ne d$, then $p\nmid N$. Indeed a divisor of $Qqd$ divides $Qq$ or the prime $d$. At an unramified prime the local unit subgroup used to define inertia is trivial. Membership in inertia means being $r(u)$ for a unit in this subgroup. Thus $u=1$ and $r(u)=0$. This proves triviality of the whole additive inertia subgroup. The relevant calls are **unramified_spec** and **mem_inertia_iff** in `hostFactsS.lean:49-70`.

Now let $p\in S$. The prime $d$ divides the prime-to-$p$ part of $N$, since $d\mid N$ and $p\ne d$. A $p$-local unit is $1$ modulo this part and hence modulo $d$. The sign test with $k=1$ puts its inertia image in $\mathrm{InPhi}$. The chosen Frobenius unit is congruent to $p$ modulo the same part. For $p=2$ the congruence $d\equiv7\bmod16$ gives $(2/d)=1$ by the supplementary law, the use of **jac_two_d**. For an odd $p\mid Q$, quadratic reciprocity gives $(p/d)=(-d/p)$ since $d\equiv3\bmod4$: the sign from interchanging $d,p$ is exactly $(-1/p)$. The host splitting law at $p$ gives $(-d/p)=1$. For $p=q$, the congruence $q\equiv3\bmod8$ makes $q$ odd and the stipulated $(-d/q)=1$ gives the same conclusion. These are all the primes dividing $Qq$. The sign test with $k=p$ gives the Frobenius assertion. See **jac_of_dvd**, **d_dvd_ordCompl** and **frobUnit_modEq** in `hostFactsS.lean:17-38` and `hostFactsS.lean:71-82`.

## Equality of the inertia image at $d$

A $d$-local unit is $1$ modulo $Qq$. The host condition **art_d** restricts its Artin image to the identity or the distinguished involution. Passing through the frame identification sends these to $0$ and $\mathrm{sgc0}$ respectively. This proves one inclusion. The identity local unit realizes $0$. To obtain the other element, choose by the Chinese remainder theorem a unit $u$ satisfying

$$
u\equiv 1\pmod{Qq},\qquad u\equiv-1\pmod d.
$$

Both residues are units and the moduli are coprime. The first congruence gives local membership. The second gives Artin sign $(-1/d)=-1$, since $d\equiv3\bmod4$. Thus the identity possibility in **art_d** is excluded, and the resulting image is exactly $\mathrm{sgc0}$. This proves the reverse inclusion. See **toE_iod'** and **hostFactsS_pf** in `hostFactsS.lean:40-42`, `hostFactsS.lean:83-105` and `hostFactsS.lean:106-125`.

Finally the small primes are the prime factors of $Q$. As $Qq\ne0$ and $q$ is prime, adjoining $q$ to that set gives exactly $S$. Replacing $S$ by this equal finite set in the eight proven fields proves **UpperTheory.Comparison₂.hostFactsS**, `hostFactsS.lean:127-136`.

**Referee check.** Trace the two different uses of congruence. The $p$-Frobenius unit for $p\mid Qq$ reduces to $p$ at $d$. The witness for exceptional inertia instead reduces to $-1$ there. Interchanging the witnesses would lose the proof that the prescribed involution actually occurs.

## Status of literature-named inputs

- `Formalism.HC.jacobi_neg_recip` — in-repo constant (`Formalism/SharpRestriction/RamificationFrobenius/TotientGaloisClasses/HostFacts.lean:15–23`); not compared.
- `Formalism.HC.HostDer.art_ch` — record field (`Formalism/SharpRestriction/RamificationFrobenius/TotientGaloisClasses/ConjEMemHostFIff.lean:99`); not compared.
