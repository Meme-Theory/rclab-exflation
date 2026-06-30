"""Bulk-remap stale content_sha256 strings after the npz string-patch run.

Every npz patched by `_npz_stale_path_scanner.py --patch` has a NEW
content_sha256 because the embedded strings (and therefore the file bytes)
changed. Any audit-trail entry pinning the OLD SHA is now stale.

This script:
  1. Walks `*.pre_scrub.bak` files (exact pre-patch byte-copies) and the
     corresponding live npz files. Computes (old_sha, new_sha) pairs.
  2. Filters to where old != new.
  3. Bulk-substitutes old_sha -> new_sha in text files across the project,
     excluding historical archives + migration logs + binary npz/db.
  4. Writes a JSON report and creates `.sha_remap.bak` per modified text file.

Default: dry-run (report what WOULD change). Use --apply to write changes.
"""
import sys
import json
import argparse
import hashlib
import shutil
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import *  # noqa: F401, F403 — rule compliance (S34+)

PROJECT_ROOT = Path(__file__).resolve().parents[2]
COMPUTATIONS_ROOT = PROJECT_ROOT / "computations"

# Text-file extensions to scan for SHA references
SCAN_EXTENSIONS = {".json", ".txt", ".md", ".py", ".jsonl", ".log"}

# Path-fragment exclusions: do NOT modify these (immutable historical record
# OR self-modifying-data hazards from this tool's own report files)
EXCLUDE_PATH_FRAGMENTS = [
    "_archive_harvested_edges.txt",          # frozen historical edge dumps per session
    "tools/_phase3_string_migration_log.jsonl",  # rename audit trail
    "tools/_x2_transform_log.jsonl",         # rename audit trail
    "tools/_mirror_plan.jsonl",              # mirror migration trail
    ".pre_scrub.bak",                         # the backups themselves
    ".sha_remap.bak",                         # this script's backups
    ".venv",                                  # virtual environments
    "__pycache__",                            # bytecode
    # Self-corruption guards — these report files contain (old_sha, new_sha)
    # pairs as JSON fields; substituting old->new in them destroys the audit
    # trail. Excluded to make the script idempotent across re-runs.
    "_npz_sha_remap_dryrun.json",
    "_npz_sha_remap_apply.json",
    "_npz_stale_path_scan_report.json",
    "_npz_stale_path_patch_report.json",
    "_npz_stale_path_scan_post_patch.json",
]


def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def build_sha_mapping():
    """Walk *.pre_scrub.bak files; return list of (file_path, old_sha, new_sha)."""
    pairs = []
    for bak in sorted(COMPUTATIONS_ROOT.rglob("*.pre_scrub.bak")):
        live = bak.with_name(bak.name[:-len(".pre_scrub.bak")])
        if not live.exists():
            print(f"  WARN: backup has no live file: {bak.relative_to(PROJECT_ROOT)}")
            continue
        old_sha = sha256_of(bak)
        new_sha = sha256_of(live)
        pairs.append({
            "file": str(live.relative_to(PROJECT_ROOT)).replace("\\", "/"),
            "backup": str(bak.relative_to(PROJECT_ROOT)).replace("\\", "/"),
            "old_sha": old_sha,
            "new_sha": new_sha,
            "changed": old_sha != new_sha,
        })
    return pairs


def is_excluded(path):
    s = str(path).replace("\\", "/")
    return any(frag in s for frag in EXCLUDE_PATH_FRAGMENTS)


def scan_text_files():
    """Yield text files under PROJECT_ROOT, respecting exclusions."""
    for ext in SCAN_EXTENSIONS:
        for p in PROJECT_ROOT.rglob(f"*{ext}"):
            if is_excluded(p):
                continue
            yield p


def find_and_replace(text, sha_map):
    """Apply all old->new SHA substitutions to text. Returns (new_text, n_subs)."""
    n_subs = 0       # (local)
    for old, new in sha_map.items():
        count = text.count(old)
        if count > 0:
            text = text.replace(old, new)
            n_subs += count
    return text, n_subs


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true",
                        help="Write changes (default: dry-run report only)")
    parser.add_argument("--json", default=None, help="Path for JSON report")
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    print("Step 1: Building SHA mapping from .pre_scrub.bak files...")
    pairs = build_sha_mapping()
    changed_pairs = [p for p in pairs if p["changed"]]
    print(f"  Found {len(pairs)} backup pairs; {len(changed_pairs)} have SHA change.")
    if len(changed_pairs) == 0:
        print("Nothing to remap.")
        return

    sha_map = {p["old_sha"]: p["new_sha"] for p in changed_pairs}
    if len(sha_map) != len(changed_pairs):
        print(f"  WARN: SHA collision — {len(changed_pairs)} pairs map to "
              f"only {len(sha_map)} unique old SHAs.")

    print()
    print("Step 2: Scanning text files for old-SHA occurrences...")
    n_files = 0          # (local)
    n_files_hit = 0      # (local)
    n_files_modified = 0 # (local)
    n_total_subs = 0     # (local)
    file_log = []

    for path in scan_text_files():
        n_files += 1
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except Exception as e:
            continue
        # Quick bail if NONE of the old SHAs appear
        if not any(old in text for old in sha_map):
            continue
        new_text, n_subs = find_and_replace(text, sha_map)
        if n_subs == 0:
            continue
        n_files_hit += 1
        n_total_subs += n_subs
        rel = str(path.relative_to(PROJECT_ROOT)).replace("\\", "/")
        if not args.quiet:
            print(f"  HIT: {rel}  --  {n_subs} SHA replacement(s)")
        if args.apply:
            backup = path.with_suffix(path.suffix + ".sha_remap.bak")
            if not backup.exists():
                shutil.copy2(path, backup)
            path.write_text(new_text, encoding="utf-8")
            n_files_modified += 1
        file_log.append({"file": rel, "n_subs": n_subs})

    print()
    print("=" * 60)
    print(f"Backup pairs:           {len(pairs)}")
    print(f"With SHA change:        {len(changed_pairs)}")
    print(f"Unique old SHAs:        {len(sha_map)}")
    print(f"Text files scanned:     {n_files}")
    print(f"Text files with hits:   {n_files_hit}")
    print(f"Total SHA substitutions: {n_total_subs}")
    if args.apply:
        print(f"Text files modified:    {n_files_modified}")
    else:
        print("[dry-run -- pass --apply to write changes]")

    if args.json:
        report = {
            "mode": "apply" if args.apply else "dry-run",
            "n_backup_pairs": len(pairs),
            "n_changed_pairs": len(changed_pairs),
            "n_unique_old_shas": len(sha_map),
            "n_text_files_scanned": n_files,
            "n_text_files_hit": n_files_hit,
            "n_text_files_modified": n_files_modified,
            "n_total_substitutions": n_total_subs,
            "sha_pairs": changed_pairs,
            "files_modified": file_log,
        }
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)
        print(f"Report written to: {args.json}")


if __name__ == "__main__":
    main()
