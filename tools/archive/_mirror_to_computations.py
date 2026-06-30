"""tools/_mirror_to_computations.py — Phase 2a of the parallel-mirror plan.

BYTE-IDENTICAL mirror copy from computations/ + computations/ into
the new computations/ tree. No content transformation in this phase; every
copied file's SHA-256 matches its source byte-for-byte.

This is Phase 2a only. Phase 2b (the X2 transformation that makes scripts
runnable from their new location) is a separate authoring task that
operates on the output of this script.

Source trees:
    computations/    (live, S5-S88, ~4805 files; flat layout)
    computations/        (frozen, S19-S51, ~1673 files; flat layout)

Destination tree:
    computations/
        session-N/        (per-session subfolders; N in {5..88})
        _shared/          (shared infra: canonical_constants.py, audit
                           scripts, archive helpers, R2 overrides)
        README.md         (created by --execute)

Routing rules (classify():
    1. R2 overrides (s23a_kosmann_singlet.py, s35_pfaffian_corrected_j.py)
       → computations/_shared/ regardless of session prefix
    2. Debug stubs in computations/_shared (_inspect_*, _tmp_*, check_*, etc.)
       → SKIP
    3. Archive non-session orphans (a5_*, b2_*, AUDIT_*.md, phase25_*, etc.)
       → SKIP
    4. Files matching s{N}_* pattern → computations/session-N/
    5. Archive helper allowlist (dirac_spectrum.py, etc.)
       → computations/_shared/
    6. computations/_shared orphans (non-session, non-stub) → computations/_shared/
    7. Anything else (uncategorized archive) → SKIP

Collision policy: computations/_shared wins (C1). When a basename exists in
both source trees AND both classify to the same destination, the
computations/_shared source is selected; the archive copy is logged as
LOSER but not mirrored.

Modes:
    --dry-run (default): build plan; emit plan log; no filesystem changes
                         in computations/.
    --execute:           do the copies; verify post-copy SHA-256.

Idempotency: --execute is safe to re-run. Files already at destination
with matching SHA are skipped; mismatches overwrite.

Plan log: tools/_mirror_plan.jsonl (overwritten each run). The audit
script tools/_mirror_audit.py reads this log to verify post-copy state.

Usage:
    python tools/_mirror_to_computations.py            # dry-run (default)
    python tools/_mirror_to_computations.py --execute  # actual copy
    python tools/_mirror_to_computations.py --dry-run --verbose  # full plan
"""

from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import re
import shutil
import sys
from typing import Optional


# ----------------------------------------------------------------------------
# Configuration
# ----------------------------------------------------------------------------

PROJECT_ROOT = pathlib.Path(__file__).resolve().parent.parent
SOURCE_TREES = ("computations/_shared", "computation-archive")
DEST_TREE = PROJECT_ROOT / "computations"
PLAN_LOG_PATH = PROJECT_ROOT / "tools" / "_mirror_plan.jsonl"

# Subdirectories never traversed in either source tree.
# Note: subdirs NOT in this set ARE recursed into. computations/t3-intake/
# is recursed in (its files mostly route to session-N via the t3 secondary
# patterns below). computations/artifacts/ is recursed in (s85_w12_*
# outputs that mostly C1-dedupe with top-level twins). Subdirs listed in
# PRESERVE_DIR_ROUTING are recursed in with their internal structure preserved.
SKIP_SUBDIRS = {
    "__pycache__",
    ".claude",
    "a5_output",          # archive: pre-S52 dev branch outputs
    "_fisher_pdf_cache",  # computations/_shared: memoization cache (per user "scrap")
    "_artifacts",         # computations/_shared: agent debris (per user "scrap")
    "_tmp",               # computations/_shared: scratch dir (per user "scrap")
}

# Subdirs whose internal directory structure is PRESERVED in the mirror,
# rather than flattened. Each key is the subdir name in the source tree;
# each value is the destination relpath under computations/. Files within
# these subdirs route to <dest_prefix>/<relpath_within_preserve_dir>.
#
# Example: computations/tests/foo.py -> computations/tests/foo.py
# Example: computations/_source_reconciliation_fixture/site_1/inner.py
#          -> computations/_shared/_source_reconciliation_fixture/site_1/inner.py
PRESERVE_DIR_ROUTING = {
    "tests":                            "tests",
    "_source_reconciliation_fixture":   "_shared/_source_reconciliation_fixture",
}

# Debug stubs in computations/_shared: leave behind.
DEBUG_STUB_BASENAMES = {
    "_minimal_test.py", "_test_basic.py", "test_minimal.py",
    "_find_gge.py", "_find_gge2.py",
    "_npz_inspect_out.txt", "_linecount.txt",
    "_verify_s59_npz.py", "verify_a2.py",
    "run_timescape.py",
}
DEBUG_STUB_PATTERNS = (
    r"^_inspect_.*\.py$",
    r"^inspect_.*\.py$",
    r"^check_.*\.py$",
    r"^_tmp_.*\.(py|txt)$",
    r"^_.*_inspect\.txt$",
    r"^_cc_(keys|sweep_inspect)\.txt$",
    r"^_dprov_inspect\.txt$",
    r"^_gates_(inspect.*|post.*)\.txt$",
    r"^_gge_keys_.*\.txt$",
    r"^_gge_found.*\.txt$",
    r"^_s\d+\w*_(tier3_)?(verdict|done|out|out2)\.txt$",
    r"^_s\d+_.*\.log$",
    r"^_pru_k_disambiguation_rerun\.csv$",
)

# Archive non-session orphans: leave behind.
ARCHIVE_LEAVE_BEHIND_BASENAMES = {
    "canonical_constants.py",  # collision; live wins (C1)
    "CLAUDE.md",                # collision; live wins (C1)
    "extended_phi_analysis.py",
    "mc_phi_significance.py",
    "phi_significance.py",
    "paasch_phi_analysis.py",
    "feynman_actual_predictions.py",
    "feynman_predictions_compute.py",
    "gauge_coupling_derivation.py",
    "rge33a_reanalysis.py",
    "run_diff_audit.py",
    "branching_computation_32dim.py",      # variant; canonical wins
    "branching_computation_phase2b.py",    # variant; canonical wins
    "coleman_weinberg_sweep.png",
    "cw_regularized.png",
    "heat_kernel_analysis.png",
    "CONSTANTS_CORRECTION_REPORT.md",
}
ARCHIVE_LEAVE_BEHIND_PATTERNS = (
    r"^a5_",
    r"^b\d+_",
    r"^c\d+_",
    r"^d\d+",                # d1_, d2_, d4_, d19_
    r"^debug_jcompat",
    r"^phase25_",
    r"^h\d+_",               # h2_, h4_, h5_
    r"^kk1_",
    r"^l\d+_(?!lichnerowicz)",  # l20_lichnerowicz allowlisted; others left behind
    r"^AUDIT_.*\.md$",
)

# Archive helpers explicitly mirrored (in addition to s{N}_-prefixed scripts).
ARCHIVE_HELPER_ALLOWLIST = {
    "dirac_spectrum.py",
    "spectral_action.py",
    "branching_computation.py",
    "r20a_riemann_tensor.py",
    "l20_lichnerowicz.py",
    # coleman_weinberg.py / cw_regularized.py /
    # phi_analysis.py / spectral_free_energy.py — exist in BOTH
    # trees; collision per C1 → computations/_shared source wins.
}

# R2 overrides: helper-shaped despite session prefix → _shared/ in mirror.
R2_SHARED_OVERRIDES = {
    "s23a_kosmann_singlet.py",
    "s35_pfaffian_corrected_j.py",
}

# Compile patterns once.
_DEBUG_STUB_RE = tuple(re.compile(p) for p in DEBUG_STUB_PATTERNS)
_ARCHIVE_LEAVE_RE = tuple(re.compile(p) for p in ARCHIVE_LEAVE_BEHIND_PATTERNS)
_SESSION_PREFIX_RE = re.compile(r"^s(\d+)[_a-zA-Z]")

# T3-intake naming-convention secondary patterns. Each captures the session
# number N from a basename that emerged from the t3-intake workflow:
#   t3_S30B_FULL_SPECTRUM_verdict.txt  -> session-30
#   _t3_s35_pfaffian_corrected_j_rerun.py -> session-35
#   prep_T3-S22A-PAASCH-CURVE.md       -> session-22
# These extend the primary ^s(\d+) pattern; tried after it, before fallthrough.
_T3_SECONDARY_PATTERNS = (
    re.compile(r"^t3_S(\d+)[A-Z_]"),       # t3_S{N}_GATE_NAME_verdict.txt
    re.compile(r"^_t3_s(\d+)[_a-zA-Z]"),   # _t3_s{N}_*.{py,log}
    re.compile(r"^prep_T3-S(\d+)[A-Z-]"),  # prep_T3-S{N}-GATE-NAME.md
)


# ----------------------------------------------------------------------------
# Classification
# ----------------------------------------------------------------------------

def classify(source_tree: str, src_relpath: pathlib.Path) -> tuple[str, str]:
    """Return (classification, reason).

    Args:
        source_tree:  "computations/_shared" or "computation-archive"
        src_relpath:  path RELATIVE to the source tree root. For top-level
                      files this is just a filename; for nested files it
                      includes the subdir path (e.g.
                      'tests/test_foo.py' or
                      '_source_reconciliation_fixture/site_1/inner.py').

    classification is one of:
      - "skip"               — file is excluded; not mirrored
      - "shared"             — destination is computations/_shared/<basename>
      - "session-N"          — destination is computations/session-N/<basename>
      - "preserve:<relpath>" — destination is computations/<relpath>;
                               used when src is under a PRESERVE_DIR_ROUTING entry
    """
    parts = src_relpath.parts
    basename = parts[-1]

    # 0. Preserve-dir routing takes precedence: any file under a preserve-dir
    # gets directory-preserving placement, bypassing the flat classification
    # logic below.
    if len(parts) > 1 and parts[0] in PRESERVE_DIR_ROUTING:
        preserve_root = parts[0]
        dest_prefix = PRESERVE_DIR_ROUTING[preserve_root]
        relpath_within_preserve = "/".join(parts[1:])
        dest_relpath = f"{dest_prefix}/{relpath_within_preserve}"
        return (f"preserve:{dest_relpath}",
                f"preserve-dir:{preserve_root}")

    # 1. Debug stubs (computations/_shared only)
    if source_tree == "computations/_shared":
        if basename in DEBUG_STUB_BASENAMES:
            return ("skip", "debug-stub-literal")
        for pat in _DEBUG_STUB_RE:
            if pat.match(basename):
                return ("skip", f"debug-stub-pattern:{pat.pattern}")

    # 2. Archive leave-behinds (archive only)
    if source_tree == "computation-archive":
        if basename in ARCHIVE_LEAVE_BEHIND_BASENAMES:
            return ("skip", "archive-leave-behind-literal")
        for pat in _ARCHIVE_LEAVE_RE:
            if pat.match(basename):
                return ("skip", f"archive-leave-behind-pattern:{pat.pattern}")

    # 3. R2 override forces _shared/ regardless of session prefix
    if basename in R2_SHARED_OVERRIDES:
        return ("shared", "R2-override-helper-shaped")

    # 4. Primary session prefix (^s\d+_...)
    m = _SESSION_PREFIX_RE.match(basename)
    if m:
        n = int(m.group(1))
        return (f"session-{n}", "session-prefix")

    # 4b. T3-intake naming-convention secondary patterns. Tried after primary
    # session prefix; before fallthrough. Captures e.g. t3_S22A_*, _t3_s35_*,
    # prep_T3-S30B-*. Files matching these patterns route to session-N like
    # any other session-prefixed file, regardless of which subdir they live in.
    for pat in _T3_SECONDARY_PATTERNS:
        m = pat.match(basename)
        if m:
            n = int(m.group(1))
            return (f"session-{n}", f"t3-secondary:{pat.pattern}")

    # 5. Archive helper allowlist
    if source_tree == "computation-archive":
        if basename in ARCHIVE_HELPER_ALLOWLIST:
            return ("shared", "archive-helper-allowlisted")
        # Anything else in archive without session prefix and not on
        # allowlist: SKIP (default-deny for archive).
        return ("skip", "archive-uncategorized-default-deny")

    # 6. computations/_shared: non-session, non-stub → orphan → _shared/
    return ("shared", "computation-orphan")


def compute_destination(classification: str, basename: str) -> Optional[pathlib.Path]:
    if classification == "skip":
        return None
    if classification.startswith("preserve:"):
        dest_relpath = classification[len("preserve:"):]
        # dest_relpath uses forward slashes per classify() construction;
        # split into parts so DEST_TREE / a / b / c works on Windows.
        parts = dest_relpath.split("/")
        dst = DEST_TREE
        for p in parts:
            dst = dst / p
        return dst
    if classification == "shared":
        return DEST_TREE / "_shared" / basename
    return DEST_TREE / classification / basename


# ----------------------------------------------------------------------------
# SHA-256
# ----------------------------------------------------------------------------

def sha256_file(path: pathlib.Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


# ----------------------------------------------------------------------------
# Plan building
# ----------------------------------------------------------------------------

def build_plan() -> tuple[dict, list, list]:
    """Build the mirror plan. Returns (plan, skipped, collisions).

    plan: dict[dst_path -> {src, src_tree, classification, reason}]
    skipped: list of {src, src_tree, basename, reason}
    collisions: list of {winner, loser, dst, policy}
    """
    plan: dict[pathlib.Path, dict] = {}
    skipped: list[dict] = []
    collisions: list[dict] = []

    for tree_name in SOURCE_TREES:
        tree_root = PROJECT_ROOT / tree_name
        if not tree_root.is_dir():
            print(f"[warn] source tree missing: {tree_root}", file=sys.stderr)
            continue

        # Enumerate sources: top-level files + recursive descent into any
        # non-skip subdir. SKIP_SUBDIRS is checked at every depth level.
        sources_to_process: list[pathlib.Path] = []
        for entry in tree_root.iterdir():
            if entry.is_dir():
                if entry.name in SKIP_SUBDIRS:
                    continue
                # Recurse into this non-skip subdir; respect SKIP_SUBDIRS at
                # any deeper level by checking parent.parts.
                for sub_entry in entry.rglob("*"):
                    if not sub_entry.is_file():
                        continue
                    rel_parents = set(sub_entry.relative_to(tree_root).parent.parts)
                    if rel_parents & SKIP_SUBDIRS:
                        continue
                    sources_to_process.append(sub_entry)
            elif entry.is_file():
                sources_to_process.append(entry)

        for src in sources_to_process:
            src_relpath = src.relative_to(tree_root)
            cls, reason = classify(tree_name, src_relpath)
            if cls == "skip":
                skipped.append({
                    "src": str(src),
                    "src_tree": tree_name,
                    "basename": src.name,
                    "reason": reason,
                })
                continue

            dst = compute_destination(cls, src.name)
            if dst is None:
                continue

            if dst in plan:
                existing = plan[dst]
                if existing["src_tree"] == "computations/_shared":
                    # computation-comp already won; archive copy is loser.
                    collisions.append({
                        "winner": str(existing["src"]),
                        "winner_tree": existing["src_tree"],
                        "loser": str(src),
                        "loser_tree": tree_name,
                        "dst": str(dst),
                        "policy": "C1-computation-wins",
                    })
                    continue
                else:
                    # Existing was archive; new is computation-comp; replace.
                    collisions.append({
                        "winner": str(src),
                        "winner_tree": tree_name,
                        "loser": str(existing["src"]),
                        "loser_tree": existing["src_tree"],
                        "dst": str(dst),
                        "policy": "C1-computation-wins",
                    })
                    plan[dst] = {
                        "src": src,
                        "src_tree": tree_name,
                        "classification": cls,
                        "reason": reason,
                    }
                    continue

            plan[dst] = {
                "src": src,
                "src_tree": tree_name,
                "classification": cls,
                "reason": reason,
            }

    return plan, skipped, collisions


# ----------------------------------------------------------------------------
# Plan log emission
# ----------------------------------------------------------------------------

def emit_plan_log(plan: dict, skipped: list, collisions: list,
                  with_shas: bool = False) -> None:
    """Emit a JSONL log of the plan."""
    with open(PLAN_LOG_PATH, "w", encoding="utf-8") as f:
        # Header / metadata row
        f.write(json.dumps({
            "type": "header",
            "schema_version": 1,
            "phase": "2a",
            "source_trees": list(SOURCE_TREES),
            "dest_tree": str(DEST_TREE.relative_to(PROJECT_ROOT)),
            "n_planned_copies": len(plan),
            "n_skipped": len(skipped),
            "n_collisions": len(collisions),
            "with_shas": with_shas,
        }) + "\n")

        # Copy entries
        for dst, entry in plan.items():
            row = {
                "type": "copy",
                "src": str(entry["src"].relative_to(PROJECT_ROOT)),
                "src_tree": entry["src_tree"],
                "dst": str(dst.relative_to(PROJECT_ROOT)),
                "classification": entry["classification"],
                "reason": entry["reason"],
            }
            if with_shas:
                row["src_sha256"] = sha256_file(entry["src"])
            f.write(json.dumps(row) + "\n")

        # Collisions
        for col in collisions:
            row = dict(col)
            row["type"] = "collision_resolved"
            f.write(json.dumps(row) + "\n")

        # Skipped
        for sk in skipped:
            row = dict(sk)
            row["type"] = "skip"
            f.write(json.dumps(row) + "\n")

    print(f"[plan] wrote {PLAN_LOG_PATH.relative_to(PROJECT_ROOT)}")


# ----------------------------------------------------------------------------
# Execute
# ----------------------------------------------------------------------------

README_BODY = """# computations/ — Parallel Mirror Tree (Phase 2a)

This directory is a **byte-identical mirror** of `computations/` plus
allowlisted helpers from `computations/`, established by Phase 2a of the
S88+ rigging plan.

## Status

- Phase 2a: byte-identical copy COMPLETE (this state).
- Phase 2b: X2 transformation pass (PENDING) — converts inlined path
  hardcodes in `session-N/*.py` to use `tools.computation_root.resolve_*`.
  Until Phase 2b runs, scripts here are NOT runnable from this location:
  their `T0 = PROJECT_ROOT / "computations/_shared"` references would resolve
  to `computations/computations/` which doesn't exist.
- Phase 3+: consumer refactor, cutover, eventual deletion of
  computations/.

## Layout

- `_shared/` — shared infrastructure
    - `canonical_constants.py` — copied from `computations/`
      (live wins on collision; archive copy was a 732-line stale snapshot)
    - `dirac_spectrum.py`, `spectral_action.py`,
      `branching_computation.py`, `r20a_riemann_tensor.py`,
      `l20_lichnerowicz.py` — archive-only helpers consumed by ~140 live
      scripts
    - `s23a_kosmann_singlet.py`, `s35_pfaffian_corrected_j.py` — R2
      overrides: helper-shaped despite session prefix
    - audit scripts, migration utilities, persistent state files copied
      from computations/_shared orphans
- `session-N/` — per-session subfolders for N in the union of session
  numbers found in computations/ and computations/

## Active root flag

The active computation root is determined by `tools/computation_root.json`
and the `tools.computation_root` module. Default: `computations/_shared`.
This mirror is queryable via the abstraction layer when the flag is
flipped to `computations` — but per Phase 2a status, scripts here are
not yet runnable. Don't flip the flag until Phase 2b transformation runs.

## Verifying mirror integrity

```
python tools/_mirror_audit.py
```

## Re-running the mirror copy

The mirror script is idempotent. Re-running with `--execute` will skip
files already at their destination with matching SHA-256.

```
python tools/_mirror_to_computations.py --execute
```
"""


def execute_plan(plan: dict, verbose: bool = False) -> tuple[int, int, list]:
    """Execute the plan: copy files; verify post-copy SHA. Returns
    (n_copied, n_skipped_idempotent, failures)."""
    n_copied = 0
    n_skipped = 0
    failures: list[dict] = []

    DEST_TREE.mkdir(exist_ok=True)
    (DEST_TREE / "_shared").mkdir(exist_ok=True)

    for dst, entry in sorted(plan.items()):
        src: pathlib.Path = entry["src"]

        # Ensure parent dir exists.
        dst.parent.mkdir(parents=True, exist_ok=True)

        # Idempotency: skip if dst exists with matching SHA.
        if dst.exists():
            try:
                src_sha = sha256_file(src)
                dst_sha = sha256_file(dst)
            except OSError as e:
                failures.append({"src": str(src), "dst": str(dst),
                                 "issue": f"sha256 read error: {e}"})
                continue
            if src_sha == dst_sha:
                n_skipped += 1
                if verbose:
                    print(f"[skip-idempotent] {dst.relative_to(PROJECT_ROOT)}")
                continue
            # else: SHA mismatch on existing dst; we'll overwrite
            if verbose:
                print(f"[overwrite] {dst.relative_to(PROJECT_ROOT)} "
                      f"(existing dst SHA != src SHA)")

        # Copy bytes + metadata; verify post-copy SHA.
        try:
            shutil.copy2(src, dst)
            src_sha = sha256_file(src)
            dst_sha = sha256_file(dst)
            if src_sha != dst_sha:
                failures.append({
                    "src": str(src),
                    "dst": str(dst),
                    "issue": "post-copy SHA mismatch",
                    "src_sha": src_sha,
                    "dst_sha": dst_sha,
                })
                continue
            n_copied += 1
            if verbose:
                print(f"[copy] {entry['classification']}/{src.name}")
        except (OSError, shutil.Error) as e:
            failures.append({"src": str(src), "dst": str(dst),
                             "issue": f"copy error: {e}"})

    # Emit README.md to mark the destination as a parallel-mirror tree.
    readme_path = DEST_TREE / "README.md"
    if not readme_path.exists():
        readme_path.write_text(README_BODY, encoding="utf-8")
        print(f"[readme] wrote {readme_path.relative_to(PROJECT_ROOT)}")

    return n_copied, n_skipped, failures


# ----------------------------------------------------------------------------
# Reporting
# ----------------------------------------------------------------------------

def print_summary(plan: dict, skipped: list, collisions: list) -> None:
    print("=" * 72)
    print("Mirror plan summary (Phase 2a: byte-identical copy)")
    print("=" * 72)

    # Aggregate plan by destination subdir.
    by_session: dict[str, int] = {}
    shared_count = 0
    preserve_dir_counts: dict[str, int] = {}
    for entry in plan.values():
        cls = entry["classification"]
        if cls == "shared":
            shared_count += 1
        elif cls.startswith("preserve:"):
            # Group preserve entries by the dest-prefix subdir name.
            dest_relpath = cls[len("preserve:"):]
            preserve_root = dest_relpath.split("/", 1)[0]
            preserve_dir_counts[preserve_root] = (
                preserve_dir_counts.get(preserve_root, 0) + 1
            )
        else:
            by_session[cls] = by_session.get(cls, 0) + 1

    print(f"  Source trees:        {list(SOURCE_TREES)}")
    print(f"  Destination tree:    {DEST_TREE.relative_to(PROJECT_ROOT)}")
    print(f"  Total to copy:       {len(plan)}")
    print(f"    -> _shared/        {shared_count}")
    print(f"    -> session-N/      {sum(by_session.values())} "
          f"across {len(by_session)} session subfolders")
    if preserve_dir_counts:
        total_preserve = sum(preserve_dir_counts.values())
        print(f"    -> preserve-dirs/  {total_preserve} "
              f"across {len(preserve_dir_counts)} preserve roots:")
        for root, count in sorted(preserve_dir_counts.items()):
            print(f"         {root}/  {count} files")
    print(f"  Skipped:             {len(skipped)}")
    print(f"  Collisions resolved: {len(collisions)} (all C1: computation-comp wins)")

    # Aggregate skip reasons.
    skip_reason_counts: dict[str, int] = {}
    for sk in skipped:
        skip_reason_counts[sk["reason"]] = skip_reason_counts.get(sk["reason"], 0) + 1
    if skip_reason_counts:
        print()
        print("  Skip reasons (top counts):")
        for reason, count in sorted(skip_reason_counts.items(),
                                    key=lambda x: -x[1])[:15]:
            print(f"    {count:5d}  {reason}")


def print_session_distribution(plan: dict) -> None:
    counts: dict[int, int] = {}
    for entry in plan.values():
        cls = entry["classification"]
        if cls.startswith("session-"):
            n = int(cls.split("-", 1)[1])
            counts[n] = counts.get(n, 0) + 1
    print()
    print("  Session distribution (post-mirror):")
    for n in sorted(counts.keys()):
        print(f"    session-{n:>2d}: {counts[n]} files")


def print_collisions(collisions: list, max_show: int = 15) -> None:
    if not collisions:
        return
    print()
    print(f"  Collisions resolved ({len(collisions)} total; showing first {max_show}):")
    for col in collisions[:max_show]:
        winner_rel = pathlib.Path(col["winner"]).relative_to(PROJECT_ROOT)
        loser_rel = pathlib.Path(col["loser"]).relative_to(PROJECT_ROOT)
        print(f"    WIN  {winner_rel}")
        print(f"    LOSE {loser_rel}")


# ----------------------------------------------------------------------------
# Main
# ----------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Phase 2a parallel-mirror copy "
                    "(computations/ + computations/ → computations/)"
    )
    parser.add_argument("--dry-run", action="store_true",
                        help="Build plan + emit log, but don't copy (default)")
    parser.add_argument("--execute", action="store_true",
                        help="Execute the plan (copy + post-copy SHA verify)")
    parser.add_argument("--verbose", action="store_true",
                        help="Per-file logging during execute")
    parser.add_argument("--with-shas", action="store_true",
                        help="Compute and log SHA-256 of every source in plan log "
                             "(slow on large trees; default off in dry-run)")
    parser.add_argument("--show-collisions", action="store_true",
                        help="List the resolved collisions in the summary output")
    parser.add_argument("--show-distribution", action="store_true",
                        help="Print per-session file count distribution")
    args = parser.parse_args()

    if args.execute and args.dry_run:
        print("[error] --execute and --dry-run are mutually exclusive",
              file=sys.stderr)
        return 2

    print(f"[setup] project_root = {PROJECT_ROOT}")
    print(f"[setup] dest_tree    = {DEST_TREE.relative_to(PROJECT_ROOT)}")

    plan, skipped, collisions = build_plan()

    print_summary(plan, skipped, collisions)
    if args.show_distribution:
        print_session_distribution(plan)
    if args.show_collisions:
        print_collisions(collisions)

    emit_plan_log(plan, skipped, collisions, with_shas=args.with_shas)

    if args.execute:
        print()
        print("=" * 72)
        print("Executing plan (this writes to computations/)")
        print("=" * 72)
        n_copied, n_skipped_idem, failures = execute_plan(plan, verbose=args.verbose)
        print()
        print(f"  Copied this run:           {n_copied}")
        print(f"  Skipped (already mirrored): {n_skipped_idem}")
        print(f"  Failures:                   {len(failures)}")
        if failures:
            print()
            print("  FAILURES:")
            for fail in failures[:10]:
                print(f"    {fail}")
            return 1
        print()
        print("[done] Phase 2a byte-identical mirror complete.")
        print("[next] Run tools/_mirror_audit.py to verify SHA-equivalence.")
        return 0
    else:
        print()
        print("[dry-run] no files copied. Re-run with --execute to perform the copy.")
        return 0


if __name__ == "__main__":
    sys.exit(main())
