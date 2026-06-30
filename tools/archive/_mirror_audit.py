"""tools/_mirror_audit.py — post-copy verification of the parallel mirror.

Reads the mirror plan log (tools/_mirror_plan.jsonl) and verifies, for every
recorded "copy" action:

  1. Destination file exists.
  2. Destination SHA-256 matches source SHA-256 (byte-identical mirror).

Reports any divergence: missing destinations, SHA mismatches.

This script is the audit canary for Phase 2a's byte-identical invariant. It
should report ALL PASS immediately after `_mirror_to_computations.py --execute`.
After Phase 2b's X2 transformation runs, the mirror will INTENTIONALLY diverge
from sources (path-resolution lines rewritten to use tools.computation_root);
running this script post-Phase-2b will report SHA mismatches on transformed
.py files and that's expected.

Usage:
    python tools/_mirror_audit.py                    # default plan log
    python tools/_mirror_audit.py --plan custom.jsonl
    python tools/_mirror_audit.py --quiet             # only failures + summary
    python tools/_mirror_audit.py --show-only-failures

Exit codes:
    0  all matches; mirror is byte-equivalent to sources
    1  drift detected (missing dst OR SHA mismatch)
    2  plan log missing or unparseable
"""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import sys
from typing import Iterable


PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
DEFAULT_PLAN_LOG = PROJECT_ROOT / "tools" / "_mirror_plan.jsonl"


def sha256_file(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def iter_plan(plan_path: pathlib.Path) -> Iterable[dict]:
    if not plan_path.exists():
        print(f"[error] plan log not found at {plan_path}", file=sys.stderr)
        sys.exit(2)
    with open(plan_path, "r", encoding="utf-8") as f:
        for ln, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                yield json.loads(line)
            except json.JSONDecodeError as e:
                print(f"[error] malformed JSONL at {plan_path}:{ln}: {e}",
                      file=sys.stderr)
                sys.exit(2)


def audit_one(entry: dict) -> tuple[str, str]:
    """Return (status, detail). status in {'PASS', 'MISSING', 'SHA_MISMATCH', 'IO_ERROR'}."""
    src = PROJECT_ROOT / entry["src"]
    dst = PROJECT_ROOT / entry["dst"]
    if not dst.exists():
        return ("MISSING", f"dst does not exist: {dst.relative_to(PROJECT_ROOT)}")
    if not src.exists():
        return ("IO_ERROR",
                f"src no longer exists at audit time: {src.relative_to(PROJECT_ROOT)}")
    try:
        src_sha = sha256_file(src)
        dst_sha = sha256_file(dst)
    except OSError as e:
        return ("IO_ERROR", f"sha256 read error: {e}")
    if src_sha == dst_sha:
        return ("PASS", f"sha={src_sha[:16]}")
    return ("SHA_MISMATCH",
            f"src={src_sha[:16]} dst={dst_sha[:16]}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Phase 2a mirror audit: verify byte-identical SHA equivalence."
    )
    parser.add_argument("--plan", default=str(DEFAULT_PLAN_LOG),
                        help="Path to mirror plan log JSONL "
                             "(default: tools/_mirror_plan.jsonl)")
    parser.add_argument("--quiet", action="store_true",
                        help="Suppress per-file PASS lines; only show summary + failures")
    parser.add_argument("--show-only-failures", action="store_true",
                        help="Same as --quiet")
    args = parser.parse_args()

    plan_path = pathlib.Path(args.plan).resolve()
    quiet = args.quiet or args.show_only_failures

    print("=" * 72)
    print(f"Mirror audit (reads {plan_path.relative_to(PROJECT_ROOT)})")
    print("=" * 72)

    counts = {"PASS": 0, "MISSING": 0, "SHA_MISMATCH": 0, "IO_ERROR": 0}
    failures: list[dict] = []
    header_seen = False

    for entry in iter_plan(plan_path):
        etype = entry.get("type")
        if etype == "header":
            header_seen = True
            print(f"  Plan header: phase={entry.get('phase')}, "
                  f"n_planned={entry.get('n_planned_copies')}, "
                  f"n_skipped={entry.get('n_skipped')}, "
                  f"n_collisions={entry.get('n_collisions')}")
            continue
        if etype != "copy":
            # collision_resolved / skip rows: not in audit scope
            continue

        status, detail = audit_one(entry)
        counts[status] = counts.get(status, 0) + 1
        if status != "PASS":
            failures.append({
                "src": entry["src"],
                "dst": entry["dst"],
                "status": status,
                "detail": detail,
            })
            print(f"  [{status}] {entry['dst']} -- {detail}")
        elif not quiet:
            print(f"  [PASS] {entry['dst']}")

    if not header_seen:
        print(f"[warn] no header row in plan log; "
              f"plan structure may not match expected schema_version=1",
              file=sys.stderr)

    print()
    print("=" * 72)
    print("Audit summary")
    print("=" * 72)
    total = sum(counts.values())
    for status, count in counts.items():
        print(f"  {status:14s} {count:6d}")
    print(f"  {'TOTAL':14s} {total:6d}")

    if failures:
        print()
        print(f"  [FAIL] {len(failures)} mismatch(es) detected. "
              f"Mirror is NOT byte-equivalent to sources.")
        return 1
    print()
    print("  [PASS] mirror is byte-equivalent to sources for all planned copies.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
