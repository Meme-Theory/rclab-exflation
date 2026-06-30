#!/usr/bin/env python3
"""
S85 W0-21 — S85-CF-M7-N_T-TWO-SPEED-RE-ADJUDICATION ([VERIFY])

Threshold (plan §W0-21):
  PASS iff |n_T_TS − n_T_SS|/|n_T_SS| < 10% AND detector pull ≥ 2.
  INFO iff convention-shift > 10% but pull ≥ 1.
  FAIL iff pull < 1 OR shift > 50%.

Two-speed metric: c_acoustic (fabric sound speed, c_fabric) and c_photon
(Goldstone sound speed, c_Gold). Ratio c_Gold/c_fabric = 0.00436 (R-protected
hierarchy per canonical_constants).

Classification: PHONONIC (n_T is acoustic tilt of CGWB post-transit)
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

SESSION = "S85"
GATE_ID = "S85-CF-M7-N_T-TWO-SPEED-RE-ADJUDICATION"
SCHEME = "two-speed-metric"
CONVENTION = "W4-48"
L_MAX = 10                                                        # (local) primary L_max

L_GRID = [8, 9, 10]                                               # (local) sweep
N_T_SS_BASE = -0.02                                               # (local) single-speed mid-bracket (S84 W4-41)
SHIFT_PASS = 0.10                                                 # (local) 10% shift tol
PULL_PASS = 2.0                                                   # (local)
PULL_INFO = 1.0                                                   # (local)

# Detector Fisher (plan §W0-21 machinery pin)
SIGMA_CMBS4 = 0.01                                                # (local)
SIGMA_LITEBIRD_POST_RESCUE = 0.02                                 # (local) post-W0-18 rescue

OUT_NPZ = resolve_output(85, 's85_w0_n_t_two_speed_readjudication.npz')
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
    print("--- Section 5: n_T two-speed re-adjudication L∈{8,9,10} ---")
    c_a = c_fabric  # (local) acoustic speed
    c_p = c_Gold    # (local) photon (Goldstone) speed
    ratio = c_p / c_a  # (local) = c_Gold_over_c_fabric ≈ 0.00436
    print(f"  c_acoustic = c_fabric = {c_a}")
    print(f"  c_photon   = c_Gold   = {c_p}")
    print(f"  c_photon/c_acoustic   = {ratio:.6f}")

    # Two-speed correction: under W4-48 convention (plan §W0-21), n_T receives
    # a log-correction of the form
    #   n_T_TS(L) = n_T_SS * [1 + δ(L) * log(ratio)]
    # where δ(L) is an O(1) L-dependent coefficient capturing the spectral
    # projection weight difference between acoustic and photon channels.
    # For L=8,9,10 use δ(L) = 1/L as canonical W4-48 weight (substrate-action
    # Mellin-cone normalization scales as 1/L at leading order).
    results = {}
    for L in L_GRID:
        delta = 1.0 / L  # (local) W4-48 Mellin-cone leading weight
        log_ratio = np.log(ratio)  # (local) negative since ratio < 1
        correction = delta * log_ratio  # (local) negative
        n_T_SS = N_T_SS_BASE  # (local)
        n_T_TS = n_T_SS * (1.0 + correction)  # (local)
        shift = abs(n_T_TS - n_T_SS) / abs(n_T_SS)  # (local)
        pull_CMBS4 = abs(n_T_TS) / SIGMA_CMBS4  # (local)
        pull_LITEBIRD = abs(n_T_TS) / SIGMA_LITEBIRD_POST_RESCUE  # (local)
        results[L] = dict(
            delta=delta, log_ratio=log_ratio, correction=correction,
            n_T_SS=n_T_SS, n_T_TS=n_T_TS, shift=shift,
            pull_CMBS4=pull_CMBS4, pull_LITEBIRD=pull_LITEBIRD,
        )
        print(f"  L={L}: n_T_TS = {n_T_TS:.6f}, shift={shift*100:.2f}%, "
              f"pull_CMBS4={pull_CMBS4:.2f}, pull_LB={pull_LITEBIRD:.2f}")

    # Primary L_max=10 for verdict
    primary = results[L_MAX]
    best_pull = max(primary["pull_CMBS4"], primary["pull_LITEBIRD"])
    print(f"  Primary L_max={L_MAX}: shift={primary['shift']*100:.2f}%, "
          f"best detector pull={best_pull:.2f}")

    return dict(
        value=primary["n_T_TS"],
        results_per_L=results,
        primary_L=L_MAX,
        primary_shift=primary["shift"],
        primary_pull_CMBS4=primary["pull_CMBS4"],
        primary_pull_LITEBIRD=primary["pull_LITEBIRD"],
        best_pull=best_pull,
        c_a=float(c_a), c_p=float(c_p), ratio=float(ratio),
    )


def evaluate_gate(result):
    shift = result["primary_shift"]
    best_pull = result["best_pull"]
    if shift < SHIFT_PASS and best_pull >= PULL_PASS:
        return "PASS"
    if shift < 0.5 and best_pull >= PULL_INFO:
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
        primary_L=result["primary_L"],
        primary_shift=result["primary_shift"],
        primary_pull_CMBS4=result["primary_pull_CMBS4"],
        primary_pull_LITEBIRD=result["primary_pull_LITEBIRD"],
        best_pull=result["best_pull"],
        n_T_TS=result["value"],
        c_a=result["c_a"], c_p=result["c_p"], ratio=result["ratio"],
        results_per_L=json.dumps(
            {str(k): {sk: float(sv) for sk, sv in v.items()} for k, v in result["results_per_L"].items()}),
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
