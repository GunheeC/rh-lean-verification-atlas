# P006 · One input and three output predicates

AI-written, AI cross-reviewed; no human sign-off; not a claim that RH is proved

**First-pass outline of the head proof term** · 91 dominated core lines (index size).

this note describes what the top-level term calls; it does not explain the dependency cone beneath it

**pending_review** · [Unit card](../../units/P006.md) · [Track guide](../../tracks/formal/README.md)

A single right-half-plane assertion is inserted directly into the first slot and used twice more to obtain the strip and zeta slots. The three components have different domains and exclusions. `claimAll` ([MainTheorems.lean:15–16](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Supplements/Kernels/MainTheorems.lean#L15-L16)).

## Fix the type of the shared input

The first proposition is nonvanishing for every character strictly to the right of one half, subject to the disjunction on character and argument. The second is an equality of real parts for any character with a zero in the open strip. The third concerns zeta, allows zeros anywhere and explicitly excludes $1$ and the negative even integers. The outer conjunction is right associated. In particular [P004](../../units/P004.md) can recover the strip statement without any projection on the individual complex arguments. `Claim.HalfPlane` ([HalfPlane.lean:3–4](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/CharacterBoxes/HalfPlane.lean#L3-L4)). `Claim.Strip` ([HalfPlane.lean:6–7](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/CharacterBoxes/HalfPlane.lean#L6-L7)). `Claim.Zeta` ([HalfPlane.lean:9–10](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/CharacterBoxes/HalfPlane.lean#L9-L10)). `claimAll` ([MainTheorems.lean:15–16](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Supplements/Kernels/MainTheorems.lean#L15-L16)).

## Use the same half-plane witness in two branches

The first slot is literally [P009](../../units/P009.md). In the strip branch the case on the right contradicts that same input. On the left the proof passes to the conductor, removes the finite Euler factors, and reflects the resulting primitive zero to the inverse character. The modulus has changed along this branch. The original universal quantifier over the modulus is what makes a second application to the reflected character available. `Claim.strip` ([ClaimStrip.lean:59–73](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/CharacterBoxes/ClaimStrip.lean#L59-L73)). `Claim.prim_zero` ([ClaimStrip.lean:23–33](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/CharacterBoxes/ClaimStrip.lean#L23-L33)). `Claim.prim_reflect` ([ClaimStrip.lean:42–57](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/CharacterBoxes/ClaimStrip.lean#L42-L57)).

## Close the zeta branch with the proper range

For a zero with positive real part below one the modulus-one character and the strip result give the desired equality. For real part at least one the known nonvanishing invoked in the source rules out the zero. In the nonpositive half-plane the argument first excludes zero itself; the gamma-factor zeros that remain would correspond to an excluded negative even integer. Reflect the resulting completed zero to $1-s$ and use nonvanishing for real part at least one. This branch uses its own completed-zeta argument. Identifying it with the separate modulus-one route in [P008](../../units/P008.md) would obscure which analytic reductions actually occur in the proof term. `Claim.zeta` ([ClaimStrip.lean:75–100](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Development/AutomorphicArithmetic/CharacterBoxes/ClaimStrip.lean#L75-L100)). `claimAll` ([MainTheorems.lean:15–16](https://github.com/leanprover-community/riemann-hypothesis/blob/40e56bab026552e089d7afcfeff08d2defb9c005/src/Supplements/Kernels/MainTheorems.lean#L15-L16)).

## Reproduce the export check

Run from the atlas checkout. Set `ALPOGE_RH_SRC` to the absolute path of the `src` directory of a separately obtained Lean checkout at the commit in [sources](../../sources/README.md). The following command was executed on 25 November 2026. It compares the full inclusive source span to the atlas digest, then tests the specific supplier or projection used by this export.

```sh
python3 - <<'PY'
from pathlib import Path
from hashlib import sha256
import json
unit = json.loads(Path('units/P006.yaml').read_text())
pin = unit['lean'][0]
from os import environ
source = Path(environ['ALPOGE_RH_SRC']) / pin['file']
lines = source.read_text().splitlines()
span = '\n'.join(lines[pin['line0'] - 1:pin['line1']])
assert sha256(span.encode()).hexdigest() == pin['sha256']
assert '⟨allChi, Claim.strip allChi, Claim.zeta allChi⟩' in span
print(unit['id'], pin['name'], pin['sha256'])
PY
```

Observed output

```text
P006 claimAll ed1f716842f8ede8864c2da8b1ba7bef252f4af1ef68f6775a487aa17e90270c
```

The digest identifies the exact source text used above. The string assertion tests the spelling of the application. Its mathematical domain and exceptional cases come from the cited predicates and proof steps.

**First step to challenge.** Check that the zeta branch really covers zeros of nonpositive real part. The strip implication alone only covers the open strip.
