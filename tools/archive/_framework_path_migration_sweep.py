"""
Project-wide path-string find-and-replace sweep after the
sessions/framework/ reorganization (S86 housekeeping).

34 files moved:
  - 31 to sessions/framework/registry/
  -  3 to sessions/framework/correspondence/

Replaces literal substrings `sessions/framework/<name>.md` with the
new path. Operates ONLY on the in-scope file list documented in the
spawn prompt. Does NOT touch closed sessions, archived plans, or
auto-rebuilt indexes.

Usage:
    python tools/_framework_path_migration_sweep.py [--dry-run]
"""

from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent  # project root

# ---------------------------------------------------------------------------
# Mapping table (old basename -> new basename with subfolder prefix)
# ---------------------------------------------------------------------------

REGISTRY_FILES = [
    "21cm-science-case.md",
    "_registry-template.md",
    "baseline-findings-s66.md",
    "branch-iv-canonical.md",
    "canonical-source-architecture.md",
    "CGWB-alpha-s-joint-flagship-pre-registration.md",
    "closed-gw-channels.md",
    "cmb-hd-alpha-s-poll-log.md",
    "constraint-mega-matrix.md",
    "cutoff-sqrt-adjudication.md",
    "detector-readiness-9-cell.md",
    "dr3-3row-7cell-subtree.md",
    "elimination-bulletins.md",
    "external-clock-scaffold.md",
    "falsifier-master-inventory.md",
    "falsifier-rigor-registry.md",
    "falsifier-watchlist.md",
    "fisher-pdf-registry.md",
    "f-nl-folded-pathway-registry.md",
    "layer1-layer2-retroactive-audit.md",
    "lizzi-finite-infinite-vector-classification.md",
    "lrd-observational-constraints.md",
    "path-b-d2-workshop.md",
    "path-b-rq1-inner-fluctuation-simulator.md",
    "path-b-rq1-rq3-combined-full-cycle-simulator.md",
    "path-b-rq2-cc-dilaton-lambda-running.md",
    "path-b-rq3-phase-transition-simulator.md",
    "pre-registered-observations.md",
    "spectral-moment-identities.md",
    "spectral-post-mortem.md",
    "w0-primary-decision-rule.md",
]

CORRESPONDENCE_FILES = [
    "correspondence-table-registry.md",
    "cross-channel-correlation-matrix.md",
    "3HeB-inheritance-canonical.md",
]

# Build the (old, new) substring pairs.  Order: longest old-path-prefix first,
# but since all olds share "sessions/framework/" + bare-basename, ordering by
# basename length (descending) avoids accidental partial-substring overlap
# (e.g., "falsifier-watchlist.md" vs "falsifier-master-inventory.md").
PAIRS: list[tuple[str, str]] = []
for fname in REGISTRY_FILES:
    PAIRS.append((f"sessions/framework/{fname}", f"sessions/framework/registry/{fname}"))
for fname in CORRESPONDENCE_FILES:
    PAIRS.append((f"sessions/framework/{fname}", f"sessions/framework/correspondence/{fname}"))

# Sort by length of the old-string descending so longer/more-specific patterns
# replace before shorter ones (defensive; not strictly necessary here since all
# are full filenames with `.md` suffix, but it's the safe convention).
PAIRS.sort(key=lambda p: -len(p[0]))

# ---------------------------------------------------------------------------
# In-scope file collection
# ---------------------------------------------------------------------------

def gather_in_scope_files(root: Path) -> list[Path]:
    """Walk the in-scope tree and return every file we should consider."""
    files: list[Path] = []

    # 1. .claude/rules/*.md
    files.extend((root / ".claude" / "rules").glob("*.md"))

    # 2. .claude/agent-memory/**/*.md (active memory)
    am = root / ".claude" / "agent-memory"
    if am.exists():
        files.extend(am.rglob("*.md"))

    # 3. computations/_shared/*.py and *.json and *.txt and *.md
    # (The .md files are active audit/landing reports per S82+ pattern;
    # see amri_audit_report.md, s84_w*_*.md landing blocks, etc.)
    t0 = root / "computations"
    if t0.exists():
        files.extend(t0.glob("*.py"))
        files.extend(t0.glob("*.json"))
        files.extend(t0.glob("*.txt"))
        files.extend(t0.glob("*.md"))

    # 4. CLAUDE.md, team-lead-behavior.md, no-technical-debt.md (project root)
    for name in ("CLAUDE.md", "team-lead-behavior.md", "no-technical-debt.md"):
        p = root / name
        if p.exists():
            files.append(p)

    # 5. tools/*.py and *.json and *.md
    tools = root / "tools"
    if tools.exists():
        files.extend(tools.glob("*.py"))
        files.extend(tools.glob("*.json"))
        files.extend(tools.glob("*.md"))

    # 6. tools/viz/console/*
    viz_console = root / "tools" / "viz" / "console"
    if viz_console.exists():
        for p in viz_console.iterdir():
            if p.is_file():
                files.append(p)

    # 7. sessions/permanent-results-registry.md and sessions/evoi-framework.md
    for name in ("permanent-results-registry.md", "evoi-framework.md"):
        p = root / "sessions" / name
        if p.exists():
            files.append(p)

    # 8. sessions/session-86/**
    s86 = root / "sessions" / "session-86"
    if s86.exists():
        for ext in ("*.md", "*.json", "*.txt"):
            files.extend(s86.rglob(ext))

    # 9. sessions/session-plan/session-86-* (active plans)
    plan_dir = root / "sessions" / "session-plan"
    if plan_dir.exists():
        for p in plan_dir.glob("session-86-*"):
            if p.is_file():
                files.append(p)

    # 10. sessions/framework/registry/*.md and correspondence/*.md (newly installed; cite each other)
    for sub in ("registry", "correspondence"):
        d = root / "sessions" / "framework" / sub
        if d.exists():
            files.extend(d.glob("*.md"))

    # 11. sessions/framework/*.md root files (the 13 that stayed)
    fw = root / "sessions" / "framework"
    if fw.exists():
        for p in fw.glob("*.md"):
            files.append(p)

    # 12. summary/session-86-final.md (if exists)
    s86final = root / "summary" / "session-86-final.md"
    if s86final.exists():
        files.append(s86final)

    # Dedup and stable sort
    files = sorted({f.resolve() for f in files})
    return files


# Out-of-scope safety: explicit forbid-list checked per file at edit time.
def is_out_of_scope(path: Path, root: Path) -> bool:
    rel = path.resolve().relative_to(root)
    parts = rel.parts
    # Closed sessions: sessions/session-NN/ for NN < 86
    if len(parts) >= 2 and parts[0] == "sessions" and parts[1].startswith("session-"):
        sub = parts[1]
        if sub == "session-plan":
            # session-plan handled separately; only session-86-* allowed
            if len(parts) >= 3 and not parts[2].startswith("session-86"):
                return True
            return False
        if sub.startswith("session-"):
            # Extract numeric portion
            try:
                num = int(sub.split("-", 1)[1])
                if num < 86:
                    return True
            except ValueError:
                pass
    # sessions/archive
    if len(parts) >= 2 and parts[0] == "sessions" and parts[1] == "archive":
        return True
    # sessions/session-plan/archive
    if len(parts) >= 3 and parts[0] == "sessions" and parts[1] == "session-plan" and parts[2] == "archive":
        return True
    # summary/session-NN-final.md for N < 86
    if len(parts) >= 2 and parts[0] == "summary":
        nm = parts[1]
        if nm.startswith("session-") and nm.endswith("-final.md"):
            try:
                num = int(nm.split("-", 1)[1].split("-")[0])
                if num < 86:
                    return True
            except ValueError:
                pass
        if nm == "Archives" or (len(parts) >= 3 and parts[1] == "Archives"):
            return True
    # tools/knowledge-index.json
    if len(parts) == 2 and parts[0] == "tools" and parts[1] == "knowledge-index.json":
        return True
    return False


# ---------------------------------------------------------------------------
# Per-file replacement
# ---------------------------------------------------------------------------

def replace_in_file(path: Path, dry_run: bool) -> tuple[int, list[str]]:
    """Apply all PAIRS to file content. Returns (n_replacements, hits_per_pair)."""
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        # Skip binary or encoding-incompatible files
        return (0, [])
    except OSError as exc:
        print(f"[ERROR] read {path}: {exc}", file=sys.stderr)
        return (0, [])

    original = text
    total = 0
    hits_log: list[str] = []
    for old, new in PAIRS:
        if old in text:
            count = text.count(old)
            text = text.replace(old, new)
            total += count
            hits_log.append(f"  {old} -> {new}: {count}")

    if total > 0 and not dry_run:
        path.write_text(text, encoding="utf-8")
    return (total, hits_log)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def directory_bucket(path: Path, root: Path) -> str:
    """Return a coarse directory label for reporting."""
    rel = path.resolve().relative_to(root)
    parts = rel.parts
    if parts[0] == ".claude":
        if len(parts) >= 2 and parts[1] == "rules":
            return ".claude/rules/"
        if len(parts) >= 2 and parts[1] == "agent-memory":
            return ".claude/agent-memory/"
        return ".claude/"
    if parts[0] == "computations":
        return "computations/_shared/"
    if parts[0] == "tools":
        if len(parts) >= 3 and parts[1] == "viz":
            return "tools/viz/"
        return "tools/"
    if parts[0] == "sessions":
        if len(parts) >= 2 and parts[1] == "framework":
            if len(parts) >= 3 and parts[2] in ("registry", "correspondence"):
                return f"sessions/framework/{parts[2]}/"
            return "sessions/framework/"
        if len(parts) >= 2 and parts[1] == "session-86":
            return "sessions/session-86/"
        if len(parts) >= 2 and parts[1] == "session-plan":
            return "sessions/session-plan/"
        return "sessions/"
    if parts[0] == "summary":
        return "summary/"
    return parts[0] + "/"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true",
                    help="Report what would change without writing.")
    ap.add_argument("--verbose", action="store_true",
                    help="Print per-file replacement counts.")
    args = ap.parse_args()

    files = gather_in_scope_files(ROOT)
    # Filter out-of-scope (defensive; gather_in_scope_files should not have
    # included them, but safeguard).
    files = [f for f in files if not is_out_of_scope(f, ROOT)]

    print(f"Total in-scope files: {len(files)}")
    print(f"Pair count: {len(PAIRS)}")
    print(f"Mode: {'DRY RUN' if args.dry_run else 'WRITE'}")
    print()

    bucket_files: dict[str, int] = {}
    bucket_hits: dict[str, int] = {}
    files_modified = 0
    total_replacements = 0
    failed: list[str] = []

    for f in files:
        try:
            n, log_lines = replace_in_file(f, args.dry_run)
        except Exception as exc:  # pragma: no cover
            failed.append(f"{f}: {exc}")
            continue
        bucket = directory_bucket(f, ROOT)
        bucket_files[bucket] = bucket_files.get(bucket, 0) + 1
        if n > 0:
            files_modified += 1
            total_replacements += n
            bucket_hits[bucket] = bucket_hits.get(bucket, 0) + n
            if args.verbose:
                rel = f.resolve().relative_to(ROOT)
                print(f"[+{n}] {rel}")
                for line in log_lines:
                    print(line)

    print()
    print("=" * 60)
    print("Summary by directory bucket:")
    print(f"{'bucket':<35} {'files_scanned':>14} {'files_modified':>16} {'replacements':>14}")
    all_buckets = sorted(set(bucket_files) | set(bucket_hits))
    for b in all_buckets:
        nf = bucket_files.get(b, 0)
        # files_modified per bucket: count by re-walking is unnecessary; we did
        # not track per-bucket modified count. Approximate via hits>0 detection.
        # To get accurate per-bucket mods, we'd need a second pass; instead,
        # just report scanned and replacement counts.
        nh = bucket_hits.get(b, 0)
        print(f"{b:<35} {nf:>14} {'-':>16} {nh:>14}")
    print()
    print(f"TOTAL files scanned:    {len(files)}")
    print(f"TOTAL files modified:   {files_modified}")
    print(f"TOTAL replacements:     {total_replacements}")
    if failed:
        print()
        print(f"FAILED ({len(failed)}):")
        for line in failed:
            print(f"  {line}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
