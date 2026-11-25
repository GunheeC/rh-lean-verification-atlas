"""Paths to canonical unit cards; checklists and step manifests share their directory."""
def unit_files(root):
    return sorted(path for path in (root / "units").glob("*.yaml")
                  if not path.name.endswith(".steps.yaml"))
