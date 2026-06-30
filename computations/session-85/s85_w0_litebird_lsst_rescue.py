#!/usr/bin/env python3
"""
S85 W0-18 — S85-LITEB-LSST-RESCUE-PRIOR ([VERIFY])

Threshold (plan §W0-18):
  Three rescue scenarios for LiteBIRD σ(n_T):
    A: LSST A_lens improvement 1.3×
    B: extended-mission 3-year baseline (×√(3/2))
    C: Simons Obs delensing (×0.7)
  PASS iff at least one scenario achieves pull ≥ 3.
  INFO iff at least one achieves 1 ≤ pull < 3.
  FAIL iff all scenarios have pull < 1.

Inputs (plan §W0-18):
  σ(n_T)_baseline = LiteBIRD Hazumi 2020 Table 5 ≈ 0.02 (typical forecast)
  n_T_framework   = S84 W4-41 anchor (using -0.02 as mid-bracket framework value
                    per §W0-21 re-adjudication; S84 original range -0.02 to -0.1)

Classification: PHONONIC — n_T is the acoustic tilt of CGWB post-transit.
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

import hashlib, json, sys, time
from pathlib import Path
import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S85"                                                    # (local)
GATE_ID = "S85-LITEB-LSST-RESCUE-PRIOR"                            # (local)
SCHEME = "Fisher-rescue"                                           # (local)
CONVENTION = "LiteBIRD-2020"                                       # (local)
L_MAX = 8                                                          # (local)

# Plan pins (§W0-18 machinery)
SIGMA_NT_BASELINE = 0.02                                           # (local) Hazumi 2020 Table 5
N_T_FRAMEWORK = -0.02                                              # (local) S84 W4-41 mid-bracket; absolute value used
LSST_A_LENS_IMPROVEMENT = 1.3                                      # (local) improvement factor
EXT_MISSION_FACTOR = np.sqrt(3.0 / 2.0)                            # (local) √(3/2)
DELENSING_FACTOR = 0.7                                             # (local) Simons Obs fiducial
PULL_PASS_THRESHOLD = 3.0                                          # (local)
PULL_INFO_THRESHOLD = 1.0                                          # (local)

OUT_NPZ = resolve_output(85, 's85_w0_litebird_lsst_rescue.npz')
VERDICT_TXT = resolve_output(85, 's85_gate_verdicts.txt')

INPUT_FILES = [resolve_script(None, 'canonical_constants.py')]


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
    print("--- Section 5: LiteBIRD σ(n_T) rescue scenarios ---")
    print(f"  σ(n_T)_baseline = {SIGMA_NT_BASELINE}  (Hazumi 2020 Table 5)")
    print(f"  n_T_framework   = {N_T_FRAMEWORK}  (S84 W4-41 mid-bracket)")
    print(f"  |n_T_framework| = {abs(N_T_FRAMEWORK)}")

    # Scenario A: LSST A_lens improvement (tightens σ by 1/1.3)
    sigma_A = SIGMA_NT_BASELINE / LSST_A_LENS_IMPROVEMENT  # (local)
    pull_A = abs(N_T_FRAMEWORK) / sigma_A  # (local)
    print(f"  Scenario A (LSST A_lens 1.3×): σ = {sigma_A:.5f}, pull = {pull_A:.3f}")

    # Scenario B: extended mission √(3/2) improvement in σ
    sigma_B = SIGMA_NT_BASELINE / EXT_MISSION_FACTOR  # (local)
    pull_B = abs(N_T_FRAMEWORK) / sigma_B  # (local)
    print(f"  Scenario B (extended mission √(3/2)): σ = {sigma_B:.5f}, pull = {pull_B:.3f}")

    # Scenario C: delensing 0.7×
    sigma_C = SIGMA_NT_BASELINE * DELENSING_FACTOR  # (local)
    pull_C = abs(N_T_FRAMEWORK) / sigma_C  # (local)
    print(f"  Scenario C (delensing 0.7×): σ = {sigma_C:.5f}, pull = {pull_C:.3f}")

    # Combined rescue (all 3 stacked)
    sigma_combined = sigma_A * (DELENSING_FACTOR / 1.0) / EXT_MISSION_FACTOR  # (local)
    pull_combined = abs(N_T_FRAMEWORK) / sigma_combined  # (local)
    print(f"  Combined (all 3 stacked): σ = {sigma_combined:.5f}, pull = {pull_combined:.3f}")

    max_pull = max(pull_A, pull_B, pull_C)  # (local) dominant scenario
    print(f"  max pull across 3 scenarios: {max_pull:.3f}")

    return dict(
        value=(pull_A, pull_B, pull_C),
        sigma_A=sigma_A, pull_A=pull_A,
        sigma_B=sigma_B, pull_B=pull_B,
        sigma_C=sigma_C, pull_C=pull_C,
        sigma_combined=sigma_combined, pull_combined=pull_combined,
        max_pull=max_pull,
        n_T_framework=N_T_FRAMEWORK,
        sigma_baseline=SIGMA_NT_BASELINE,
    )


def evaluate_gate(result):
    mp = result["max_pull"]
    if mp >= PULL_PASS_THRESHOLD:
        return "PASS"
    if mp >= PULL_INFO_THRESHOLD:
        return "INFO"
    return "FAIL"


def emit_4tuple(v, s, c, L):
    return f"(value={v!r}, scheme={s}, convention={c}, L_max={L})"


def append_verdict(verdict, value, audit_sha, content_sha):
    # serialize tuple compactly
    v_repr = f"({value[0]:.4f},{value[1]:.4f},{value[2]:.4f})"
    line = (
        f"{GATE_ID}: {verdict} -- value={v_repr} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


def save_npz(result, audit_sha, content_sha):
    np.savez_compressed(
        OUT_NPZ,
        pull_A=result["pull_A"], pull_B=result["pull_B"], pull_C=result["pull_C"],
        sigma_A=result["sigma_A"], sigma_B=result["sigma_B"], sigma_C=result["sigma_C"],
        sigma_combined=result["sigma_combined"], pull_combined=result["pull_combined"],
        max_pull=result["max_pull"],
        n_T_framework=result["n_T_framework"],
        sigma_baseline=result["sigma_baseline"],
        audit_sha256=audit_sha, content_sha256=content_sha,
    )


def main():
    t0 = time.time()
    pins = log_input_pins(INPUT_FILES)
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
