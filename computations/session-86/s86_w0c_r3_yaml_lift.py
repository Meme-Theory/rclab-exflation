#!/usr/bin/env python3
"""
S86 W0c-5 — S86-R3-YAML-LIFT
=============================

Gate: S86-R3-YAML-LIFT ([AUDIT])
Classification: META

Pre-registered threshold (plan §W0c-5.9):
  PASS iff sig_4_coverage >= 0.90 post-lift.
  FAIL iff sig_4_coverage < 0.90 post-lift.
  INFO iff parser fails on any S85 plan file (script exits 2).

The lift inserts `schema_version: R3` as the first sub-key of every
machinery_pin: block in S85 plan files. Per .claude/rules/v3-closure-recovery.md
the sig_4 metric is the fraction of gate blocks declaring R3 schema; per
the validator (_yaml_gate_validator.py:73-82) compliance also requires an
8-item PRDR checklist (operator, strict_PASS_boundary,
boundary_reachable_analytically, reachable_rationals, machinery_pin_map,
audit_discriminators, substitution_chain, input_files). The literal
plan instruction (insert schema_version: R3) will not by itself raise
the validator's compliance score above the 8-item checklist coverage,
so this gate's PASS path requires the gate blocks to ALREADY carry
the 8-item content — `schema_version: R3` is the labelling layer.

Inputs (S84+ dual-SHA):
  - sessions/session-plan/archive/session-85-plan-w*.md (16 files;
    located in archive/ post-S85-close, NOT directly under session-plan/)
  - computations/_shared/_yaml_gate_validator.py (canonical sig_4 audit tool)
  - script bytes (this file)

Output 4-tuple:
  (value=<sig_4_coverage_post_lift>, scheme=R3_yaml_lift,
   convention=schema_version_R3, L_max=N/A)
"""
from __future__ import annotations

from canonical_constants import M_KK  # noqa: F401 — framework-import discipline

import hashlib
import json
import re
import subprocess
import sys
import time
import os
from pathlib import Path
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===


os.environ.setdefault("OMP_NUM_THREADS", "8")

PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S86"
GATE_ID = "S86-R3-YAML-LIFT"
SCHEME = "R3_yaml_lift"
CONVENTION = "schema_version_R3"
L_MAX = "N/A"

# Plan-canonical glob path (returns 0 in current state — files archived)
PLAN_GLOB_CANONICAL = "sessions/session-plan/session-85-plan-w*.md"  # (local)
# Archive fallback (where S85 plans actually live post-S85-close)
PLAN_GLOB_ARCHIVE = "sessions/session-plan/archive/session-85-plan-w*.md"  # (local)

VALIDATOR = resolve_script(None, '_yaml_gate_validator.py')
DIFF_PATCH = resolve_script(86, 's86_w0c_5_r3_lift_diff.patch')
VERDICT_TXT = resolve_output(86, 's86_gate_verdicts.txt')

PASS_THRESHOLD = 0.90  # (local) — sig_4 PIN per .claude/rules/v3-closure-recovery.md


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def compute_dual_sha(script_path: Path, validator_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    sb = b""  # (local)
    try:
        sb = script_path.read_bytes()
    except OSError:
        pass
    vb = b""  # (local)
    try:
        vb = validator_path.read_bytes()
    except OSError:
        pass
    pj = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")  # (local)
    h_a = hashlib.sha256(); h_a.update(sb); h_a.update(vb); h_a.update(pj)
    h_c = hashlib.sha256(); h_c.update(sb)
    return h_a.hexdigest(), h_c.hexdigest()


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


def run_validator_on_files(files: list[Path]) -> dict:
    """Run _yaml_gate_validator.py with --json on the given files; parse output."""
    cmd = [
        sys.executable,
        str(VALIDATOR),
        "--json",
    ] + [str(f) for f in files]  # (local)
    proc = subprocess.run(cmd, capture_output=True, text=True, cwd=str(PROJECT_ROOT))  # (local)
    try:
        data = json.loads(proc.stdout)  # (local)
    except json.JSONDecodeError:
        return {
            "error": "JSON decode failed",
            "stdout": proc.stdout[:500],
            "stderr": proc.stderr[:500],
            "returncode": proc.returncode,
        }
    return data


def coverage_from_report(report: dict) -> tuple[int, int, float]:
    """Return (compliant, total, fraction)."""
    total = 0  # (local)
    compliant = 0  # (local)
    for r in report.get("reports", []):
        for g in r.get("gates", []):
            total += 1
            if g.get("r3_compliant"):
                compliant += 1
    return compliant, total, (compliant / total if total else 0.0)


def insert_schema_version_in_pin_blocks(text: str) -> tuple[str, int]:
    """Insert `schema_version: R3` as first sub-key under each machinery_pin: block.

    Strategy: locate every line that matches `^(\\s+)machinery_pin:\\s*$` (a
    YAML key-only declaration) and insert `<indent>  schema_version: R3` on
    the next line if not already present.

    Idempotent: skips blocks that already have schema_version present in the
    next 4 lines.

    Returns (new_text, n_inserted).
    """
    lines = text.split("\n")  # (local)
    out: list[str] = []  # (local)
    n_inserted = 0  # (local)
    i = 0  # (local)
    while i < len(lines):
        out.append(lines[i])
        m = re.match(r"^(\s+)machinery_pin:\s*$", lines[i])
        if m:
            indent = m.group(1)  # (local)
            # Look ahead 4 lines for existing schema_version: R3
            window = "\n".join(lines[i + 1:i + 5])  # (local)
            if "schema_version" not in window:
                out.append(f"{indent}  schema_version: R3")
                n_inserted += 1
        i += 1
    return "\n".join(out), n_inserted


def main() -> int:
    t0 = time.time()  # (local)
    print(f"=== {GATE_ID} — pre-edit phase ===")

    # Glob canonical path first; fall back to archive
    canonical_files = sorted(PROJECT_ROOT.glob(PLAN_GLOB_CANONICAL))  # (local)
    archive_files = sorted(PROJECT_ROOT.glob(PLAN_GLOB_ARCHIVE))  # (local)
    print(f"  Canonical path '{PLAN_GLOB_CANONICAL}': {len(canonical_files)} files")
    print(f"  Archive  path '{PLAN_GLOB_ARCHIVE}': {len(archive_files)} files")
    if not canonical_files and archive_files:
        print(f"  S85 plans archived; proceeding with archive set "
              f"(post-S85-close housekeeping, not convention-shopping).")
        plan_files = archive_files  # (local)
    elif canonical_files:
        plan_files = canonical_files
    else:
        print(f"  FAIL: no S85 plan files found at either path")
        return 0  # exit 0 (script ran; verdict captured below)

    # Log SHAs and pin map
    pins: dict[str, str] = {}  # (local)
    print(f"\n=== {GATE_ID} — input SHA-256 pins (pre-edit) ===")
    for p in plan_files:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    pins[
        "computations/_shared/_yaml_gate_validator.py"
    ] = sha256_of(VALIDATOR)
    print()

    # Pre-edit baseline: run validator
    pre_report = run_validator_on_files(plan_files)  # (local)
    if "error" in pre_report:
        print(f"  Validator ERROR: {pre_report['error']}")
        print(f"  stderr: {pre_report.get('stderr', '')[:200]}")
        verdict = "INFO"
        value = "validator_parse_error"
        audit_sha, content_sha = compute_dual_sha(
            Path(__file__).resolve(), VALIDATOR, pins
        )
        append_verdict(verdict, value, audit_sha, content_sha)
        return 0
    pre_compliant, pre_total, pre_fraction = coverage_from_report(pre_report)  # (local)
    print(f"  Pre-lift coverage: {pre_compliant}/{pre_total} = {pre_fraction:.4f}")

    # Apply lift
    print(f"\n=== {GATE_ID} — applying schema_version: R3 lift ===")
    n_inserted_per_file: dict[str, int] = {}  # (local)
    diff_lines: list[str] = []  # (local) — for the .patch artifact
    for p in plan_files:
        text = p.read_text(encoding="utf-8")  # (local)
        new_text, n_inserted = insert_schema_version_in_pin_blocks(text)  # (local)
        if n_inserted > 0:
            p.write_text(new_text, encoding="utf-8")
            diff_lines.append(
                f"### {p.relative_to(PROJECT_ROOT).as_posix()}: +{n_inserted} schema_version: R3 lines\n"
            )
        n_inserted_per_file[str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")] = n_inserted
    total_inserted = sum(n_inserted_per_file.values())  # (local)
    print(f"  Total schema_version: R3 insertions: {total_inserted}")
    for rel, n in n_inserted_per_file.items():
        if n > 0:
            print(f"    {rel}: +{n}")

    # Write diff patch
    DIFF_PATCH.write_text(
        "# S86 W0c-5 R3 YAML lift diff (per-file insert counts)\n" + "".join(diff_lines),
        encoding="utf-8",
    )

    # Post-edit: re-run validator
    print(f"\n=== {GATE_ID} — post-lift validator re-run ===")
    post_report = run_validator_on_files(plan_files)  # (local)
    if "error" in post_report:
        print(f"  Validator ERROR post-lift: {post_report['error']}")
        verdict = "INFO"
        value = "validator_parse_error_post_lift"
        audit_sha, content_sha = compute_dual_sha(
            Path(__file__).resolve(), VALIDATOR, pins
        )
        append_verdict(verdict, value, audit_sha, content_sha)
        return 0
    post_compliant, post_total, post_fraction = coverage_from_report(post_report)  # (local)
    print(f"  Post-lift coverage: {post_compliant}/{post_total} = {post_fraction:.4f}")
    delta_fraction = post_fraction - pre_fraction  # (local)
    print(f"  Delta: {delta_fraction:+.4f}")

    # Pin post-edit SHAs
    for p in plan_files:
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        pins[rel] = sha256_of(p)

    # Compute dual-SHA against post-edit pin map
    audit_sha, content_sha = compute_dual_sha(
        Path(__file__).resolve(), VALIDATOR, pins
    )
    print(f"\n  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")

    # Verdict (substitution chain per plan §W0c-5.10)
    verdict = "PASS" if post_fraction >= PASS_THRESHOLD else "FAIL"  # (local)
    value = f"{post_fraction:.4f}"  # (local)

    print(f"\n(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")

    append_verdict(verdict, value, audit_sha, content_sha)

    # Diagnostic JSON
    diag = {
        "gate_id": GATE_ID,
        "verdict": verdict,
        "session": SESSION,
        "wave": "W0c",
        "pre_lift_coverage_compliant": pre_compliant,
        "pre_lift_coverage_total": pre_total,
        "pre_lift_coverage_fraction": pre_fraction,
        "post_lift_coverage_compliant": post_compliant,
        "post_lift_coverage_total": post_total,
        "post_lift_coverage_fraction": post_fraction,
        "delta_coverage_fraction": delta_fraction,
        "pass_threshold": PASS_THRESHOLD,
        "n_files_processed": len(plan_files),
        "n_inserted_per_file": n_inserted_per_file,
        "total_schema_version_R3_insertions": total_inserted,
        "canonical_path_returned_zero": len(canonical_files) == 0,
        "archive_path_used": True,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
    }  # (local)
    diag_path = resolve_output(86, 's86_w0c_5_r3_yaml_lift.json')  # (local)
    diag_path.write_text(json.dumps(diag, indent=2), encoding="utf-8")
    print(f"\nDiagnostic JSON: {diag_path.name}")
    print(f"Diff patch:      {DIFF_PATCH.name}")

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
