# P008 · Specializing the all-character bound to zeta

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 63 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**pending_review** · [Unit card](../../units/P008.md) · [Track guide](../../tracks/formal/README.md)

Specializing the half-plane input to the character of modulus one gives right-half-plane nonvanishing for zeta away from one. A separate reflection argument turns that into the zeta predicate consumed by the public exports. `rhOfAll` ([MainTheorems.lean:9–9](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Supplements/Kernels/MainTheorems.lean#L9-L9)).

## Specialize the disjunction correctly

Write $h$ for [P009](../../units/P009.md). With modulus one and character one the disjunction in $h$ must use the argument different from one. Thus for every $t$ with $\Re t>1/2$ and $t\ne1$ the ordinary zeta value at $t$ is nonzero. The rewrite uses the modulus-one identity for the L-function. This single specialization supplies the function needed in the reflection lemma. The potentially much larger obligation of supplying $h$ remains at its own unit. `rhOfAll` ([MainTheorems.lean:9–9](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Supplements/Kernels/MainTheorems.lean#L9-L9)). `Formalism.VW.rh_of_every` ([CritLine.lean:29–32](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/GammaFactorNonvanishing/CritLine.lean#L29-L32)).

## Locate the forbidden factors

Given a nontrivial zero with $\Re s<1/2$, write $t=1-s$. Positivity of $\Re t$ rules out all the nonpositive integers at $t$ and gives a nonzero gamma factor. Also $\zeta(0)$ rules out $s=0$, so $t\ne1$. The functional equation now writes the alleged zero as a product involving $\zeta(t)$, the gamma factor, a complex power with nonzero base, and $\cos(\pi t/2)$. Each factor needs a reason for nonvanishing. In particular, a cosine zero would make $t$ an odd integer, so $s$ would be an even integer. In the present range a negative even value is explicitly excluded and zero has already been treated. `Formalism.VW.rh_of_right` ([RhOfRight.lean:5–62](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/GammaFactorNonvanishing/RhOfRight.lean#L5-L62)).

## Return the predicate expected at the public interface

On the right of one half the specialized nonvanishing contradicts the proposed zero immediately; equality is the conclusion in the middle case. The resulting term has the Mathlib predicate as its type. Both [P001](../../units/P001.md) and [P002](../../units/P002.md) name it as their supplier and the latter spells the excluded values out explicitly. These source uses explain why a check of this theorem should combine a check of the analytic side conditions with an identification of the public predicate. `Formalism.VW.rh_of_right` ([RhOfRight.lean:5–62](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/GammaFactorNonvanishing/RhOfRight.lean#L5-L62)). `riemannHypothesis` ([Main.lean:4–4](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Main.lean#L4-L4)). `riemannZeta_eq_zero_re` ([Main.lean:6–6](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Main.lean#L6-L6)).

## Reproduce the export check

Run from the atlas checkout. Set `ALPOGE_RH_SRC` to the absolute path of the `src` directory of a separately obtained Lean checkout at the commit in [sources](../../sources/README.md). The following command was executed on 25 November 2026. It compares the full inclusive source span to the atlas digest, then tests the specific supplier or projection used by this export.

```sh
python3 - <<'PY'
from pathlib import Path
from hashlib import sha256
import json
unit = json.loads(Path('units/P008.yaml').read_text())
pin = unit['lean'][0]
from os import environ
source = Path(environ['ALPOGE_RH_SRC']) / pin['file']
lines = source.read_text().splitlines()
span = '\n'.join(lines[pin['line0'] - 1:pin['line1']])
assert sha256(span.encode()).hexdigest() == pin['sha256']
assert 'Formalism.VW.rh_of_every allChi' in span
print(unit['id'], pin['name'], pin['sha256'])
PY
```

Observed output

```text
P008 rhOfAll 0411e5a9dfb3386efa1d19f21b4f48f3061578663df27aa2e1537c899cf946d9
```

The digest identifies the exact source text used above. The string assertion tests the spelling of the application. Its mathematical domain and exceptional cases come from the cited predicates and proof steps.

**First step to challenge.** In the reflected case check simultaneously that the functional equation applies at $1-s$, the half-plane input applies there, and the cosine factor has no admissible zero.
