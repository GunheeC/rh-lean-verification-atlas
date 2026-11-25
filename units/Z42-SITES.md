# Z42-SITES · Served-site parameters and the lattice dictionary

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

The served-site hypotheses fix the actual local ranks and parameters. The selected chart identifies the relevant double coset, lattice and determinant, and local evaluation matches the prescribed global embedding with conjugation at odd positions. These identifications specify the data on which the kernel calculations run.

`served-site-parameters-and-the-lattice-dictionary` · [Local p-adic theory](../tracks/local/README.md) · [Theta correspondence and automorphic representations of unitary groups](../tracks/theta/README.md)

**Full** · **L2** Written proof accepted in AI cross-review · Record generated 2026-11-25 (no human check).

| 1 · Lean pinned | 2 · Statement compared | 3 · Prose | 4 · Steps | 5 · AI review | 6 · Human |
|---|---|---|---|---|---|
| ✓ | ✓ | Full | 4 | Current argument (AI) | 0 of 4 steps |

[Numbered proof and check records](Z42-SITES.check.md) · [Progress and counting rules](../PROGRESS.md)

## Statement

**Z4.2.01.** At a served site with the host tie `GatTies` and its tied lattice data and $2r_G\le k$, every position $v$ of the selected local model satisfies Std with its actual ranks, weights, marked subset and parameters. **Z4.2.03.** For $j\le m$ and an actual lattice tuple, the selected chart point satisfies the point condition and represents the prescribed rational-unitary/level double coset, the kernel lattice agrees after reindexing with the adelic lattice at that point, and its determinant is the prescribed one. **Z4.2.05.** At every site the $p$-adic evaluation of the global embedding at position $(v,s)$ agrees with the local twist of the place embedding, applied to the conjugate exactly at odd positions.

## Assumptions

- The served site has its host tie and tied lattice, with $2r_G\le k$.
- Supply the joint and its actual tuple at a stage $j\le m$. For the position calculation fix the site embeddings and position $(v,s)$.

Sources for the assumptions · [RH verification blueprint, release v13](../data/editions.json)

## Where to read

Gunhee Cho is the paper’s author and the blueprint’s editor. Both were drafted with AI assistance. No independent human referee has checked the arguments. Levent Alpöge is the author of the Lean development. [Blueprint v13b](../editions/v0.1.0/blueprint_v13b.pdf) · [Conditional paper v7](../editions/v0.1.0/paper_v7.pdf) · [Edition register](../data/editions.json)

- [Blueprint source excerpt](../notes/blueprint/Z42-SITES.tex)
- [Blueprint v13b](../editions/v0.1.0/blueprint_v13b.pdf#page=360), printed p. 324, section label `r5:Z4.2.01`.
- [RH verification blueprint, release v13](../data/editions.json), section label `r5:Z4.2.01`, PDF p. 349 (printed p. 324)
- [Blueprint v13b](../editions/v0.1.0/blueprint_v13b.pdf#page=375), printed p. 339, section label `r6:review:Z4.2.01`.
- [RH verification blueprint, release v13](../data/editions.json), section label `r6:review:Z4.2.01`, PDF p. 364 (printed p. 339)
- [Blueprint v13b](../editions/v0.1.0/blueprint_v13b.pdf#page=370), printed p. 334, section label `r5:small:Z4.2.03`.
- [RH verification blueprint, release v13](../data/editions.json), section label `r5:small:Z4.2.03`, PDF p. 359 (printed p. 334)
- [Blueprint v13b](../editions/v0.1.0/blueprint_v13b.pdf#page=375), printed p. 339, section label `r6:review:Z4.2.03`.
- [RH verification blueprint, release v13](../data/editions.json), section label `r6:review:Z4.2.03`, PDF p. 364 (printed p. 339)
- [Blueprint v13b](../editions/v0.1.0/blueprint_v13b.pdf#page=371), printed p. 335, section label `r5:small:Z4.2.05`.
- [RH verification blueprint, release v13](../data/editions.json), section label `r5:small:Z4.2.05`, PDF p. 360 (printed p. 335)
- [Blueprint v13b](../editions/v0.1.0/blueprint_v13b.pdf#page=375), printed p. 339, section label `r6:review:Z4.2.05`.
- [RH verification blueprint, release v13](../data/editions.json), section label `r6:review:Z4.2.05`, PDF p. 364 (printed p. 339)

## Evidence

- [R5 review B](../reviews/R5_review_B.md), original line 7 — COMPLETE CONFIRMED. Exactly the named unit at the hypotheses reviewed in the cited row.
- [R5 review B](../reviews/R5_review_B.md), original line 8 — COMPLETE CONFIRMED. Exactly the named unit at the hypotheses reviewed in the cited row.
- [R5 review B](../reviews/R5_review_B.md), original line 9 — COMPLETE CONFIRMED. Exactly the named unit at the hypotheses reviewed in the cited row.

Named statement declarations with the hypotheses above. Chart supplier records have their own review scopes.

Review records · [R5 review B](../reviews/R5_review_B.md)

## Lean declarations

- `GlobalTheory.TwU.std_at_served`  
  [`StdAtServed.lean`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/StdAtServed.lean#L9-L22), lines 9–22 · 14 dominated lines · SHA-256 `ade5997ef2f3`.
- `GlobalTheory.TwV.joint_dict`  
  [`LatticeTupleJointDictionary.lean`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/LatticeTupleJointDictionary.lean#L16-L25), lines 16–25 · 189 dominated lines · SHA-256 `33f8072b907e`.
- `GlobalTheory.TwV.pos_at_site`  
  [`SitePlaceInducesPositionEmbeddings.lean`](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AbelianVarietyTheory/Proofs/SatakeParameters/SitePlaceInducesPositionEmbeddings.lean#L11-L13), lines 11–13 · 32 dominated lines · SHA-256 `8bb9bf841002`.

[Machine record and full declaration hashes](Z42-SITES.yaml) · [Declaration lookup](../lookup/declarations.md)

## Reading prerequisites

Background · Local lattice parameters · Unitary theta kernels.

- [D513 · Choice of even column rank in a prescribed frame](D513.md) · statement-reading

[Evidence and definitions of reading links](../data/round3_prerequisites.json)

## Open questions

None recorded.

## Graph connections

Arrows may connect either a unit’s main declaration or an indexed member.

**Uses** · No recorded edge.

**Used by** · [P046](P046.md) · [Z42-FRAMES](Z42-FRAMES.md) · [Z42-KERNEL](Z42-KERNEL.md)

[Declaration witnesses and graph scope](../data/unit_graph.json)

Lookup aliases · `std_at_served`, `Z42-SITES Served-site parameters and the lattice dictionary`

<!-- Unit metadata SHA-256 e17be5471b74911f0840af1816651ca99cb3c40c24447500a5a25ba81b9bc881 -->
