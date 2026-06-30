#!/usr/bin/env python3
"""
Tag remaining potential hardcodes with # (local) comments.

Reads the extract_entities.py audit output, finds every POTENTIAL_HARDCODE,
and appends '  # (local)' to the flagged line in each script.

Usage:
    python tag_local_constants.py [--dry-run]

Scans computations/_shared/ and computations/ for S34+ scripts.
"""

import sys
import re
from pathlib import Path

DRY_RUN = "--dry-run" in sys.argv

# Directories to scan
ROOT = Path(__file__).parent.parent
COMPUTATIONS = ROOT / "computations"
SHARED = COMPUTATIONS / "_shared"
# computation-archive deleted at Phase 5 cutover (2026-05-03). Sentinel makes scan
# a graceful no-op; archive content is now under computations/session-N/.
ARCHIVE = ROOT / "_deleted_computations_archive_sentinel_"

# Import the audit machinery
sys.path.insert(0, str(SHARED))   # canonical_constants + audit helpers
sys.path.insert(0, str(COMPUTATIONS))
sys.path.insert(0, str(ROOT / "tools"))

from extract_entities import audit_canonical_constants

def main():
    print("Running canonical constants audit...")
    results = audit_canonical_constants(COMPUTATIONS) + audit_canonical_constants(ARCHIVE)

    potentials = [r for r in results if r["pattern"] == "POTENTIAL_HARDCODE"]
    print(f"Found {len(potentials)} potential hardcodes to tag.\n")

    # Group by script path
    by_script = {}
    for r in potentials:
        script = r["script"]
        line = r["line"]
        # Find the actual file
        for d in [COMPUTATIONS, ARCHIVE]:
            p = d / script
            if p.exists():
                by_script.setdefault(str(p), []).append(line)
                break

    total_tagged = 0
    total_skipped = 0
    files_modified = 0

    for filepath, lines_to_tag in sorted(by_script.items()):
        p = Path(filepath)
        content = p.read_text(encoding="utf-8")
        file_lines = content.split("\n")
        modified = False

        for line_no in sorted(set(lines_to_tag)):
            idx = line_no - 1  # 0-indexed
            if idx < 0 or idx >= len(file_lines):
                continue

            line = file_lines[idx]

            # Skip if already tagged
            if "# (local)" in line:
                total_skipped += 1
                continue

            # Skip if line has other S72 annotations (already handled)
            if "# S72:" in line:
                total_skipped += 1
                continue

            # Append the tag
            # Preserve existing inline comments
            if "#" in line:
                # Has an existing comment — append (local) to it
                file_lines[idx] = line.rstrip() + "  # (local)"
            else:
                file_lines[idx] = line.rstrip() + "  # (local)"

            total_tagged += 1
            modified = True

        if modified:
            files_modified += 1
            if not DRY_RUN:
                p.write_text("\n".join(file_lines), encoding="utf-8")
                print(f"  Tagged {filepath}: {len([l for l in lines_to_tag if l-1 < len(file_lines)])} lines")
            else:
                print(f"  [DRY RUN] Would tag {filepath}: {len(lines_to_tag)} lines")

    print(f"\n{'='*60}")
    print(f"Tagged:   {total_tagged} lines across {files_modified} files")
    print(f"Skipped:  {total_skipped} (already tagged or S72-annotated)")
    if DRY_RUN:
        print("(DRY RUN — no files modified)")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
