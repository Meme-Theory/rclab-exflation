#!/usr/bin/env python3
"""
S86 W0c-7 — S86-W12-4-A_N-REGULATOR-PIN-DISCIPLINE
====================================================

Gate: S86-W12-4-A_N-REGULATOR-PIN-DISCIPLINE ([AUDIT])
Classification: META

Pre-registered threshold (plan §W0c-7.9):
  PASS iff post-pass `bare_a_n_count == 0` (every citation either auto-tagged
  via inference or manually tagged in the same pass).
  FAIL iff `bare_a_n_count > 0 AND manual_review_required > 0` (auto-inference
  failed and manual tagging deferred).
  INFO iff `bare_a_n_count == 0 pre-pass` (no violations existed; rule lands
  but retrofit was a no-op).

Strategy (per plan §W0c-7.6 + epistemic discipline):
  Step 1: confirm rule-file landed at .claude/rules/regulator-pin-discipline.md
  Step 2: confirm audit-script landed at computations/_shared/_a_n_regulator_pin_audit.py
  Step 3: run audit (no auto-retrofit — see PROHIBITED_ACTIONS rationale below)
  Step 4: record FAIL with diagnostic; queue Level-3 manual review for S87+

PROHIBITED_ACTIONS rationale: the audit's regex `\\ba_(\\d+)\\b(?!\\^)` matches
ANY `a_n` token, not just Seeley-DeWitt coefficients. Pre-existing computation
codebase contains ~20k bare-a_n hits across ~638 files; the majority are
NON-Seeley-DeWitt (lattice spacings, plain variable names, string literals,
generic indices). Auto-tagging all 20k as Seeley-DeWitt would be ansatz-
forced PASS via false-positive labeling. The honest path is FAIL +
forward-looking rule + queued semantic-review carry-forward.

Inputs (S84+ dual-SHA):
  - .claude/rules/regulator-pin-discipline.md (rule landing)
  - computations/_shared/_a_n_regulator_pin_audit.py (audit script)
  - computations/_shared/ + computations/_shared/ Python files (audit targets)
  - script bytes (this file)

Output 4-tuple:
  (value=<post_pass_bare_a_n_count>, scheme=regulator_pin_audit,
   convention=tagged_a_n, L_max=N/A)
"""
from __future__ import annotations

from canonical_constants import M_KK  # noqa: F401  # framework-import discipline

import hashlib
import json
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
GATE_ID = "S86-W12-4-A_N-REGULATOR-PIN-DISCIPLINE"
SCHEME = "regulator_pin_audit"
CONVENTION = "tagged_a_n"
L_MAX = "N/A"

RULE_FILE = PROJECT_ROOT / ".claude" / "rules" / "regulator-pin-discipline.md"
AUDIT_SCRIPT = resolve_script(None, '_a_n_regulator_pin_audit.py')
VERDICT_TXT = resolve_output(86, 's86_gate_verdicts.txt')


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def compute_dual_sha(script_path: Path, audit_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    sb = b""  # (local)
    try:
        sb = script_path.read_bytes()
    except OSError:
        pass
    ab = b""  # (local)
    try:
        ab = audit_path.read_bytes()
    except OSError:
        pass
    pj = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")  # (local)
    h_a = hashlib.sha256(); h_a.update(sb); h_a.update(ab); h_a.update(pj)
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


def run_audit_json() -> dict:
    """Invoke _a_n_regulator_pin_audit.py --json."""
    cmd = [sys.executable, str(AUDIT_SCRIPT), "--json"]  # (local)
    proc = subprocess.run(
        cmd, capture_output=True, text=True, cwd=str(PROJECT_ROOT)
    )  # (local)
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError:
        return {
            "error": "JSON decode failed",
            "stdout": proc.stdout[:500],
            "stderr": proc.stderr[:500],
            "returncode": proc.returncode,
        }


def main() -> int:
    t0 = time.time()  # (local)

    print(f"=== {GATE_ID} — pre-conditions check ===")
    rule_exists = RULE_FILE.exists()  # (local)
    audit_exists = AUDIT_SCRIPT.exists()  # (local)
    print(f"  Rule file:   {RULE_FILE.relative_to(PROJECT_ROOT)} → "
          f"{'EXISTS' if rule_exists else 'ABSENT'}")
    print(f"  Audit script: {AUDIT_SCRIPT.relative_to(PROJECT_ROOT)} → "
          f"{'EXISTS' if audit_exists else 'ABSENT'}")
    if not (rule_exists and audit_exists):
        print(f"  PRE-CONDITIONS FAIL")
        return 0

    # Pin SHAs
    pins: dict[str, str] = {  # (local)
        ".claude/rules/regulator-pin-discipline.md": sha256_of(RULE_FILE),
        "computations/_shared/_a_n_regulator_pin_audit.py": sha256_of(AUDIT_SCRIPT),
    }
    print(f"\n=== {GATE_ID} — input SHA-256 pins ===")
    for k, v in pins.items():
        print(f"  {k}: {v[:16]}...")
    print()

    # Run the audit
    print(f"=== {GATE_ID} — running bare-a_n audit ===")
    audit_result = run_audit_json()  # (local)
    if "error" in audit_result:
        print(f"  Audit ERROR: {audit_result['error']}")
        verdict = "FAIL"
        value = "audit_subprocess_error"
        audit_sha, content_sha = compute_dual_sha(
            Path(__file__).resolve(), AUDIT_SCRIPT, pins
        )
        append_verdict(verdict, value, audit_sha, content_sha)
        return 0

    n_files = audit_result.get("n_files_scanned", 0)  # (local)
    n_files_with_violations = audit_result.get("files_with_violations", 0)  # (local)
    bare_count = audit_result.get("total_violations", 0)  # (local)
    print(f"  Files scanned:           {n_files}")
    print(f"  Files with violations:   {n_files_with_violations}")
    print(f"  Total bare a_n hits:     {bare_count}")
    print()

    # Compute dual SHA
    audit_sha, content_sha = compute_dual_sha(
        Path(__file__).resolve(), AUDIT_SCRIPT, pins
    )
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    # Verdict logic
    # PASS iff bare_count == 0 (rule preventative; no retrofit needed → INFO sub-tag)
    # FAIL iff bare_count > 0 (any pre-existing or new bare a_n)
    if bare_count == 0:
        verdict = "INFO"  # plan §W0c-7.9 INFO sub-tag NO_VIOLATIONS_FOUND
        value = "no_violations_pre_pass_INFO"
        print(f"  INFO: pre-pass bare_a_n_count == 0; rule lands as preventative.")
    else:
        verdict = "FAIL"
        value = f"bare_a_n_count={bare_count}_in_{n_files_with_violations}_files"
        print(f"  FAIL: bare_a_n_count = {bare_count} > 0 across "
              f"{n_files_with_violations} files; auto-retrofit deferred to S87+ "
              f"(semantic review required to avoid false-positive Seeley-DeWitt tagging).")

    print(f"\n(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    append_verdict(verdict, value, audit_sha, content_sha)

    # Diagnostic JSON
    diag = {
        "gate_id": GATE_ID,
        "verdict": verdict,
        "session": SESSION,
        "wave": "W0c",
        "rule_file_landed": rule_exists,
        "audit_script_landed": audit_exists,
        "n_files_scanned": n_files,
        "files_with_violations": n_files_with_violations,
        "bare_a_n_count": bare_count,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "remediation_route": (
            "Level-3 carry-forward to S87+: queue gate `S87-A-N-SEELEY-DEWITT-RETROFIT` "
            "for manual semantic review of pre-existing a_n citations. The audit "
            "regex `\\ba_(\\d+)\\b(?!\\^)` matches non-Seeley-DeWitt patterns "
            "(lattice spacings, plain variable names) and auto-tagging all 20k "
            "violations as Seeley-DeWitt would be ansatz-forced PASS. The "
            "regulator-pin-discipline rule applies forward-looking from S86 "
            "W0c-7 (any NEW file post-2026-04-26 must comply); use "
            "`_a_n_regulator_pin_audit.py --new-only` to enforce on new files."
        ),
    }  # (local)
    diag_path = resolve_output(86, 's86_w0c_7_a_n_regulator_pin_discipline.json')  # (local)
    diag_path.write_text(json.dumps(diag, indent=2), encoding="utf-8")
    print(f"\nDiagnostic JSON: {diag_path.name}")

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
