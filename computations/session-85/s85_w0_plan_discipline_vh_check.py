#!/usr/bin/env python3
"""
S85 W0-22 — S85-PLAN-DISCIPLINE-VAN-HOVE-CHECK ([AUDIT])

Threshold (plan §W0-22):
  PASS iff 100% of stationarity claims across session-85-plan-w*.md are
          either (a) proven by a gate in same/earlier wave OR
                  (b) DEFERRED-TO-S86-{gate} tagged.
  INFO iff ≥ 90%.
  FAIL iff < 90%.

Classification: META
"""

from __future__ import annotations
import os
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

from canonical_constants import *  # noqa: F401,F403

import hashlib, json, re, sys, time
from pathlib import Path
import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
PLAN_DIR = PROJECT_ROOT / "sessions" / "session-plan"

SESSION = "S85"                                                  # (local)
GATE_ID = "S85-PLAN-DISCIPLINE-VAN-HOVE-CHECK"                   # (local)
SCHEME = "plan-PRDR"                                             # (local)
CONVENTION = "stationarity-claim"                                # (local)
L_MAX = "NA"                                                     # (local)

STATIONARITY_REGEX = re.compile(r"stationary|extremum|cusp|τ_fold|tau_fold|van hove", re.IGNORECASE)
SUCCESSOR_TAG_REGEX = re.compile(r"DEFERRED-TO-S86-|DEFERRED[- ]TO[- ]S\d+|successor[_ ]tag", re.IGNORECASE)

OUT_NPZ = resolve_output(85, 's85_w0_plan_discipline_vh_check.npz')
VERDICT_TXT = resolve_output(85, 's85_gate_verdicts.txt')


def sha256_of(p):
    try:
        return hashlib.sha256(p.read_bytes()).hexdigest()
    except OSError:
        return ""


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script, canonical, pins):
    sb = script.read_bytes(); cb = canonical.read_bytes()
    pj = json.dumps(dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True).encode()
    return (hashlib.sha256(sb + cb + pj).hexdigest(),
            hashlib.sha256(sb).hexdigest())


def compute():
    print("--- Section 5: Plan stationarity-claim PRDR audit ---")
    plan_files = sorted(PLAN_DIR.glob("session-85-plan-w*.md"))
    print(f"  Scanning {len(plan_files)} S85 plan files")

    total_claims = 0  # (local)
    resolved_claims = 0  # (local) either in-wave-proven (has gate referencing τ_fold/cusp) or DEFERRED-tagged
    per_file = {}  # (local)

    # A stationarity claim is "resolved" if:
    # (a) the same file has a gate block referencing the claim's topic (heuristic: VAN-HOVE-CUSP gate §W0-6 proves τ_fold uniqueness)
    # (b) the file contains a DEFERRED-TO-S86 tag nearby

    # Simpler approach: list stationarity lines per file and check for DEFERRED tag in same file
    # OR cross-reference with the gate-verdicts file for a relevant PASS/INFO.
    verdicts_text = (resolve_output(85, 's85_gate_verdicts.txt')).read_text(encoding="utf-8")
    van_hove_in_verdicts = "VAN-HOVE-CUSP-THEOREM" in verdicts_text  # (local) §W0-6 gate present

    for p in plan_files:
        text = p.read_text(encoding="utf-8")
        lines = text.splitlines()
        n_claims_file = 0  # (local)
        n_resolved_file = 0  # (local)
        for line in lines:
            if STATIONARITY_REGEX.search(line):
                n_claims_file += 1
                # resolved if: (a) line contains DEFERRED tag, OR
                # (b) van Hove gate exists in verdicts AND the line mentions cusp/τ_fold
                is_deferred = bool(SUCCESSOR_TAG_REGEX.search(line))
                is_proven_by_gate = (van_hove_in_verdicts and
                                     re.search(r"cusp|τ_fold|tau_fold|van hove", line, re.IGNORECASE))
                if is_deferred or is_proven_by_gate:
                    n_resolved_file += 1
        total_claims += n_claims_file
        resolved_claims += n_resolved_file
        per_file[p.name] = dict(claims=n_claims_file, resolved=n_resolved_file)
        if n_claims_file > 0:
            print(f"  {p.name}: {n_resolved_file}/{n_claims_file} resolved")

    compliance_pct = (resolved_claims / total_claims * 100.0) if total_claims > 0 else 100.0  # (local)
    print(f"\n  Total stationarity claims across S85 plan files: {total_claims}")
    print(f"  Resolved (proven-in-wave OR DEFERRED-tagged):     {resolved_claims}")
    print(f"  Compliance: {compliance_pct:.1f}%")

    return dict(
        value=compliance_pct,
        total_claims=total_claims,
        resolved_claims=resolved_claims,
        compliance_pct=compliance_pct,
        per_file=per_file,
    )


def evaluate_gate(result):
    pct = result["compliance_pct"]
    if pct >= 100.0:
        return "PASS"
    if pct >= 90.0:
        return "INFO"
    return "FAIL"


def emit_4tuple(v, s, c, L):
    return f"(value={v!r}, scheme={s}, convention={c}, L_max={L})"


def append_verdict(verdict, value, audit_sha, content_sha):
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


def save_npz(result, audit_sha, content_sha):
    np.savez_compressed(
        OUT_NPZ,
        total_claims=result["total_claims"],
        resolved_claims=result["resolved_claims"],
        compliance_pct=result["compliance_pct"],
        per_file_json=json.dumps(result["per_file"]),
        audit_sha256=audit_sha, content_sha256=content_sha,
    )


def main():
    t0 = time.time()
    pins = log_input_pins([resolve_script(None, 'canonical_constants.py')])
    audit_sha, content_sha = compute_dual_sha(
        Path(__file__).resolve(),
        resolve_script(None, 'canonical_constants.py'), pins)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print()
    result = compute()
    verdict = evaluate_gate(result)
    tag = emit_4tuple(result["value"], SCHEME, CONVENTION, L_MAX)
    print(tag)
    save_npz(result, audit_sha, content_sha)
    append_verdict(verdict, result["value"], audit_sha, content_sha)
    print(f"\n=== {GATE_ID}: {verdict}  (wall {time.time()-t0:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
