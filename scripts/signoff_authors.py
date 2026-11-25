"""Render the named human contribution row from the submitted sign-off records."""
import argparse
from pathlib import Path
import re

from signoff_records import ROOT, is_maintainer, load_records, safe_text


def render(root):
    path = root / "AUTHORS.md"
    records = load_records(root)
    if records:
        entries = []
        for filename, record in records:
            reader = record["reader"]
            name = safe_text(reader["name"])
            role = " (maintainer)" if is_maintainer(reader) else ""
            label = f"{name}{role} · {record['unit']} · {record['date']}"
            entries.append(f"[{label}](signoffs/records/{filename})")
        credit = "Self-declared reader names and submitted scopes: " + " · ".join(entries) + "."
    else:
        credit = "The human-check register currently contains no submissions."
    row = ("| Named human checks | " + credit
           + " The progress table and checklists derive their counts from the register. "
           + "[Human check records and intake](signoffs/README.md) · [Progress](PROGRESS.md) |")
    body = path.read_text(encoding="utf-8")
    updated, count = re.subn(r"^\| Named human checks \|[^\n]*$", lambda _: row, body, flags=re.M)
    if count != 1:
        raise ValueError("AUTHORS.md must contain one named human checks row")
    return path, updated


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    path, updated = render(args.root)
    if path.read_text(encoding="utf-8") != updated:
        if args.check:
            raise SystemExit("The reader attributions in AUTHORS.md are stale")
        path.write_text(updated, encoding="utf-8")


if __name__ == "__main__":
    main()
