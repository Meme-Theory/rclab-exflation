"""Bulk text-file scrub for tier0-computation / tier0-archive path strings.

Companion to `_npz_stale_path_scanner.py` (which handles binary npz string
content). This script handles every text artifact in the project — `.json`,
`.txt`, `.md`, `.py`, `.jsonl`, `.log` — applying the same verified
`substitute_stale_paths` substitution.

Excludes immutable historical archives (`*_archive_harvested_edges.txt`),
backup files, virtual environments, bytecode caches, and the
self-modifying-data hazards from npz/SHA-remap report files.

Default: dry-run. Use --apply to write changes (creates `.text_scrub.bak`).
"""
import sys
import json
import argparse
import shutil
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import *  # noqa: F401, F403 — rule compliance (S34+)
from _npz_stale_path_scanner import substitute_stale_paths, STALE_PREFIX_RE

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SCAN_EXTENSIONS = {".json", ".txt", ".md", ".py", ".jsonl", ".log", ".js"}

EXCLUDE_PATH_FRAGMENTS = [
    # Immutable historical archives (project rule: don't touch)
    "_archive_harvested_edges.txt",
    # Backup files (don't scrub backups; they're recovery copies)
    ".pre_scrub.bak",
    ".sha_remap.bak",
    ".text_scrub.bak",
    # Virtual envs / caches
    ".venv",
    "__pycache__",
    # Self-modifying-data hazards: scan/patch/remap report files
    "_npz_sha_remap_dryrun.json",
    "_npz_sha_remap_apply.json",
    "_npz_sha_remap_verify.json",
    "_npz_stale_path_scan_report.json",
    "_npz_stale_path_patch_report.json",
    "_npz_stale_path_scan_post_patch.json",
    "_text_stale_path_scrub_dryrun.json",
    "_text_stale_path_scrub_apply.json",
    "_text_stale_path_scrub_verify.json",
    # The scrubber sources themselves contain the regex pattern in code
    "_npz_stale_path_scanner.py",
    "_npz_sha_remap.py",
    "_text_stale_path_scrubber.py",
    # Knowledge DB binary
    "knowledge.db",
    # Tagged immutable snapshots (mechanical-closure-discipline.md):
    # filename embeds content_sha256 prefix -- editing breaks identity contract
    ".frozen-",
]


def is_excluded(path):
    s = str(path).replace("\\", "/")
    return any(frag in s for frag in EXCLUDE_PATH_FRAGMENTS)


def scan_text_files():
    for ext in SCAN_EXTENSIONS:
        for p in PROJECT_ROOT.rglob(f"*{ext}"):
            if is_excluded(p):
                continue
            yield p


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true",
                        help="Write changes (default: dry-run)")
    parser.add_argument("--json", default=None, help="JSON report path")
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args()

    n_scanned = 0           # (local)
    n_files_hit = 0         # (local)
    n_files_modified = 0    # (local)
    n_total_subs = 0        # (local)
    file_log = []

    for path in scan_text_files():
        n_scanned += 1
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        # Quick bail if no stale prefix appears anywhere
        if not STALE_PREFIX_RE.search(text):
            continue
        # Apply substitution; count actual replacements
        new_text = substitute_stale_paths(text)
        if new_text == text:
            continue  # all matches had wildcard suffixes; defensive non-replace
        # Count substitutions (number of stale-prefix occurrences that were replaced)
        n_subs = len(STALE_PREFIX_RE.findall(text)) - len(STALE_PREFIX_RE.findall(new_text))
        if n_subs <= 0:
            continue
        n_files_hit += 1
        n_total_subs += n_subs
        rel = str(path.relative_to(PROJECT_ROOT)).replace("\\", "/")
        if not args.quiet:
            print(f"  HIT: {rel}  --  {n_subs} substitution(s)")
        if args.apply:
            backup = path.with_suffix(path.suffix + ".text_scrub.bak")
            if not backup.exists():
                shutil.copy2(path, backup)
            path.write_text(new_text, encoding="utf-8")
            n_files_modified += 1
        file_log.append({"file": rel, "n_subs": n_subs})

    print()
    print("=" * 60)
    print(f"Text files scanned:       {n_scanned}")
    print(f"Files with stale paths:   {n_files_hit}")
    print(f"Total substitutions:      {n_total_subs}")
    if args.apply:
        print(f"Files modified:           {n_files_modified}")
    else:
        print("[dry-run -- pass --apply to write changes]")

    if args.json:
        report = {
            "mode": "apply" if args.apply else "dry-run",
            "n_scanned": n_scanned,
            "n_files_hit": n_files_hit,
            "n_files_modified": n_files_modified,
            "n_total_subs": n_total_subs,
            "files": file_log,
        }
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump(report, f, indent=2)
        print(f"Report: {args.json}")


if __name__ == "__main__":
    main()
