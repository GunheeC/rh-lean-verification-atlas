"""Run Lean's #print axioms against already installed module objects without building them."""
import argparse
import os
from pathlib import Path
import re
import subprocess

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("module")
parser.add_argument("declaration", nargs="+")
parser.add_argument("--objects", type=Path, required=True)
parser.add_argument("--packages", type=Path, required=True)
args = parser.parse_args()
for name in [args.module, *args.declaration]:
    if not re.fullmatch(r"[\w']+(?:\.[\w']+)*", name):
        parser.error(f"Expected a qualified Lean name, got {name!r}")
if not (args.objects / (args.module.replace(".", "/") + ".olean")).is_file():
    parser.error("The selected module object is absent.")
paths = [args.objects, *sorted(args.packages.glob("*/.lake/build/lib/lean"))]
commands = ["import " + args.module, *["#print axioms " + name for name in args.declaration]]
env = {**os.environ, "LEAN_PATH": os.pathsep.join(str(p) for p in paths)}
result = subprocess.run(["lean", "+leanprover/lean4:v4.33.1", "--stdin"],
                        input="\n".join(commands) + "\n", text=True, env=env)
raise SystemExit(result.returncode)
