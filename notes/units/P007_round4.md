# P007 · Using the primitive functional equation in the strip

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 24 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**pending_review** · [Unit card](../../units/P007.md) · [Track guide](../../tracks/formal/README.md)

For a primitive character, the functional equation turns a zero left of the middle of the strip into a zero of the inverse character to the right. The all-character input rules out that reflected zero. `critAll` ([MainTheorems.lean:11–13](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Supplements/Kernels/MainTheorems.lean#L11-L13)).

## Separate primitive from arbitrary characters

Choose the nonzero modulus, then a primitive character, then the point in the open strip. The target is an equality of its real part with one half. Both end inequalities are strict. The reduction fixes the original modulus throughout. In the unrestricted all-character export [P004](../../units/P004.md) one must first pass to the conductor. Here primitivity is already supplied at the point where the functional equation is invoked. `critAll` ([MainTheorems.lean:11–13](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Supplements/Kernels/MainTheorems.lean#L11-L13)). `PrimitiveDirichletLZerosOnLine` ([Statements.lean:14–16](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Statements.lean#L14-L16)).

## Remove the gamma factor at the zero

Positive real part gives a nonzero real gamma factor in the even case. In the odd case its argument has been shifted by one and still has positive real part. The equality between ordinary L and completed L divided by this factor transfers the zero to the numerator. The point $s=0$ is excluded by the strict lower bound on its real part. This explicit denominator check matters because the division operation in Lean is total. `Formalism.VW.gammaFactor_ne_zero` ([CritLine.lean:6–9](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/GammaFactorNonvanishing/CritLine.lean#L6-L9)). `Formalism.VW.critLine` ([CritLine.lean:11–27](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/GammaFactorNonvanishing/CritLine.lean#L11-L27)).

## Apply the all-character input on the proper side

For $\Re s<1/2$, invariance of the conductor under inversion supplies primitivity of $\chi^{-1}$. Apply its functional equation at $s$, substitute the completed zero, and rewrite its double inverse as $\chi$. The ordinary L-function for $\chi^{-1}$ then vanishes at $1-s$. Both exclusions used here have witnesses: $1-s\ne0$ follows from $s\ne1$, and $1-s\ne1$ follows from $s\ne0$. Since $\Re(1-s)>1/2$, [P009](../../units/P009.md) contradicts the reflected zero. A point on the right gives a contradiction directly with $s\ne1$. The middle equality remains. `Formalism.VW.critLine` ([CritLine.lean:11–27](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Formalism/GammaFactorNonvanishing/CritLine.lean#L11-L27)). `critAll` ([MainTheorems.lean:11–13](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Supplements/Kernels/MainTheorems.lean#L11-L13)).

## Reproduce the export check

Run from the atlas checkout. Set `ALPOGE_RH_SRC` to the absolute path of the `src` directory of a separately obtained Lean checkout at the commit in [sources](../../sources/README.md). The following command was executed on 25 November 2026. It compares the full inclusive source span to the atlas digest, then tests the specific supplier or projection used by this export.

```sh
python3 - <<'PY'
from pathlib import Path
from hashlib import sha256
import json
unit = json.loads(Path('units/P007.yaml').read_text())
pin = unit['lean'][0]
from os import environ
source = Path(environ['ALPOGE_RH_SRC']) / pin['file']
lines = source.read_text().splitlines()
span = '\n'.join(lines[pin['line0'] - 1:pin['line1']])
assert sha256(span.encode()).hexdigest() == pin['sha256']
assert 'Formalism.VW.critLine allChi N χ hχ s h0 h1 hz' in span
print(unit['id'], pin['name'], pin['sha256'])
PY
```

Observed output

```text
P007 critAll 0d978db013e5eba6fa1d430c3cbd57ba979648c7e28481d8ee74be0150b7b823
```

The digest identifies the exact source text used above. The string assertion tests the spelling of the application. Its mathematical domain and exceptional cases come from the cited predicates and proof steps.

**First step to challenge.** Check which inverse character is primitive and why the exceptional argument one is excluded after reflection, even for a principal character of modulus one.
