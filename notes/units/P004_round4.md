# P004 · Extracting the all-character open-strip claim

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 101 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**pending_review** · [Unit card](../../units/P004.md) · [Track guide](../../tracks/formal/README.md)

The public assertion applies to every character of a positive modulus. Its proof selects the open-strip component of a conjunction. The analytic reduction behind that component must handle characters induced from smaller conductors. `LFunction_eq_zero_re` ([Main.lean:10–10](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Main.lean#L10-L10)).

## Select the middle component

In [P006](../../units/P006.md) the three components are grouped as $H\land(S\land Z)$. Taking the second projection and then the first gives $S$. Write down the domain of that component before applying it. The modulus is nonzero, the character is arbitrary, and the point is strictly between the vertical lines at zero and one. [P007](../../units/P007.md) has an extra primitivity hypothesis. Projection from that assertion would give a different public statement. `LFunction_eq_zero_re` ([Main.lean:10–10](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Main.lean#L10-L10)). `DirichletLZerosOnLine` ([Statements.lean:10–12](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Statements.lean#L10-L12)). `claimAll` ([MainTheorems.lean:15–16](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Supplements/Kernels/MainTheorems.lean#L15-L16)).

## Reduce the vanishing to a primitive character

For a character induced from conductor $M$, change of level expresses the old L-function as a primitive L-function times a finite product. If a prime factor in that product vanished, $\psi(p)p^{-s}$ would equal one. Its norm is bounded by $p^{-\Re s}<1$ since the character value has norm at most one. Thus the product cannot absorb the zero. The change-of-level identity also needs $s\ne1$, supplied by the upper strip inequality. `Claim.prim_zero` ([ClaimStrip.lean:23–33](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/CharacterBoxes/ClaimStrip.lean#L23-L33)). `Claim.factor_ne_zero` ([ClaimStrip.lean:7–21](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/CharacterBoxes/ClaimStrip.lean#L7-L21)).

## Follow the reflected character

When $\Re s<1/2$, nonvanishing of the archimedean gamma factor converts the primitive zero into a completed zero. Apply the functional equation for the inverse primitive character at $1-s$ and return to the ordinary L-function there. Now the half-plane statement applies at the conductor and to that inverse character. The exception is discharged by $1-s\ne1$, which follows from $s\ne0$. For $\Re s>1/2$ the half-plane statement applies directly at the original modulus using $s\ne1$. Equality is the remaining case. The proof here uses [P009](../../units/P009.md) as its arithmetic input. `Claim.prim_reflect` ([ClaimStrip.lean:42–57](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/CharacterBoxes/ClaimStrip.lean#L42-L57)). `Claim.strip` ([ClaimStrip.lean:59–73](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/CharacterBoxes/ClaimStrip.lean#L59-L73)).

## Reproduce the export check

Run from the atlas checkout. Set `ALPOGE_RH_SRC` to the absolute path of the `src` directory of a separately obtained Lean checkout at the commit in [sources](../../sources/README.md). The following command was executed on 25 November 2026. It compares the full inclusive source span to the atlas digest, then tests the specific supplier or projection used by this export.

```sh
python3 - <<'PY'
from pathlib import Path
from hashlib import sha256
import json
unit = json.loads(Path('units/P004.yaml').read_text())
pin = unit['lean'][0]
from os import environ
source = Path(environ['ALPOGE_RH_SRC']) / pin['file']
lines = source.read_text().splitlines()
span = '\n'.join(lines[pin['line0'] - 1:pin['line1']])
assert sha256(span.encode()).hexdigest() == pin['sha256']
assert ':= claimAll.2.1' in span
print(unit['id'], pin['name'], pin['sha256'])
PY
```

Observed output

```text
P004 LFunction_eq_zero_re 16e8622c29d633b78f0009d3ed16ed8cd13ece9122362aed0a4fb12646635409
```

The digest identifies the exact source text used above. The string assertion tests the spelling of the application. Its mathematical domain and exceptional cases come from the cited predicates and proof steps.

**First step to challenge.** Check the factors removed at imprimitive primes on the whole open strip, including points with real part below one half, before using primitive reflection.
