"""Compute the least set of Full written units closed under their named inputs."""
import json
import re

from atlas_files import unit_files


LOCAL_STEP = re.compile(r"S[1-9][0-9]*[a-z]*")


def closed_units(root):
    """Return closed unit IDs. An unresolved external input or cycle cannot seed closure."""
    inputs = {}
    for path in unit_files(root):
        unit = json.loads(path.read_bytes())
        if unit["status"] != "Full":
            continue
        manifest = path.with_suffix(".steps.yaml")
        if not manifest.is_file():
            continue
        steps = [s for s in json.loads(manifest.read_bytes())["steps"] if s["status"] == "active"]
        if not steps:
            continue
        names = set(unit["prerequisites"])
        names.update(ref for ref in unit["assumptions"] if not ref.startswith("source:"))
        for step in steps:
            names.update(ref for ref in step["uses"] if not LOCAL_STEP.fullmatch(ref))
        inputs[unit["id"]] = names

    closed = set()
    while True:
        qualified = {uid for uid, names in inputs.items() if names <= closed}
        if qualified == closed:
            return sorted(closed)
        closed = qualified
