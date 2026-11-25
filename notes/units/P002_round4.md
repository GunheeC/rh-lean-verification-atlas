# P002 · Which zeta zeros the explicit export quantifies over

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 3 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**pending_review** · [Unit card](../../units/P002.md) · [Track guide](../../tracks/formal/README.md)

The public zeta export spells out the exclusions on a zero and passes the resulting predicate to the same supplier used for the Mathlib formulation. The exclusions matter when the argument reflects a zero across the critical line. `riemannZeta_eq_zero_re` ([Main.lean:6–6](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Main.lean#L6-L6)).

## Read the binders before the alias

Take any complex number $s$. The first premise is the equality $\zeta(s)=0$. The second denies the existence of a natural number $n$ for which $s=-2(n+1)$, so it starts with $-2$. The last premise is $s\ne1$. The output is an equality of real numbers. The public source passes a term of type RiemannHypothesis directly across this boundary. [P001](../../units/P001.md) is the parallel export with the Mathlib name. A comparison which checked the real-part equation alone could miss the entire exclusion at the negative even integers. `RiemannZetaZerosOnLine` ([Statements.lean:3–4](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Statements.lean#L3-L4)). `riemannZeta_eq_zero_re` ([Main.lean:6–6](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Main.lean#L6-L6)).

## Identify the input used at modulus one

The actual supplier is [P008](../../units/P008.md). Given the all-character assertion [P009](../../units/P009.md), its proof fixes the character of modulus one. The hypothesis there admits either a nonprincipal character or an argument different from one. Only the latter choice applies. Rewriting the modulus-one L-function gives zeta nonvanishing on the required right half-plane with the same excluded point. `rhOfAll` ([MainTheorems.lean:9–9](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Supplements/Kernels/MainTheorems.lean#L9-L9)). `Formalism.VW.rh_of_every` ([CritLine.lean:29–32](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/GammaFactorNonvanishing/CritLine.lean#L29-L32)).

## Inspect the difficult case of the reduction

A zero to the right gives an immediate contradiction. For a zero to the left put $t=1-s$. The special value at zero gives $s\ne0$, so $t\ne1$, and its positive real part allows the gamma-factor calculation. A zero of the cosine factor would give $s=-2k$ with $k$ integral. Negative $k$ conflicts with the assumed real part, $k=0$ is already excluded by the special value, and positive $k$ supplies the natural witness $k-1$. Thus each factor in the functional equation at $t$ is nonzero. This is the place to compare the explicit quantifier with the value used in the analytic reduction. Reading the one-line public alias covers none of the arithmetic behind [P009](../../units/P009.md). `Formalism.VW.rh_of_right` ([RhOfRight.lean:5–62](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/GammaFactorNonvanishing/RhOfRight.lean#L5-L62)).

## Reproduce the export check

Run from the atlas checkout. Set `ALPOGE_RH_SRC` to the absolute path of the `src` directory of a separately obtained Lean checkout at the commit in [sources](../../sources/README.md). The following command was executed on 25 November 2026. It compares the full inclusive source span to the atlas digest, then tests the specific supplier or projection used by this export.

```sh
python3 - <<'PY'
from pathlib import Path
from hashlib import sha256
import json
unit = json.loads(Path('units/P002.yaml').read_text())
pin = unit['lean'][0]
from os import environ
source = Path(environ['ALPOGE_RH_SRC']) / pin['file']
lines = source.read_text().splitlines()
span = '\n'.join(lines[pin['line0'] - 1:pin['line1']])
assert sha256(span.encode()).hexdigest() == pin['sha256']
assert ':= rhOfAll' in span
print(unit['id'], pin['name'], pin['sha256'])
PY
```

Observed output

```text
P002 riemannZeta_eq_zero_re b76ddf651dfdaa35aa759391bf660be25e1a3d4299cf9b6fd89926313aac2ae7
```

The digest identifies the exact source text used above. The string assertion tests the spelling of the application. Its mathematical domain and exceptional cases come from the cited predicates and proof steps.

**First step to challenge.** Check the enumeration of the excluded zeros when the cosine vanishes. In particular, zero itself is disposed of by its zeta value, while the first excluded negative even integer corresponds to the natural index zero.
