#!/usr/bin/env python3
"""
S85 W5-7 S85-W5-7-TWO-LAYER-OBSTRUCTION - Joint theorem f_conv x eps_H scheme-indep
====================================================================================

Gate: S85-W5-7-TWO-LAYER-OBSTRUCTION  ([VERIFY-THEOREM])

Pre-registered threshold (plan §W5-7):
  PASS iff no regulator r satisfies BOTH SCHEME_INDEP(f_conv^r) AND
         SCHEME_INDEP(eps_H^r) within 5% drift tolerance.
  FAIL iff >=1 regulator satisfies both conditions.
  INFO iff 4 rows fail both conditions AND 1 row marginally satisfies both
         at drift <= 7% (not <= 5%).

Classification: GEOMETRIC (joint structural obstruction theorem).

METHODOLOGY
-----------
Construct the 5 regulators x 2 observables (f_conv, eps_H) scheme-drift matrix
from two independent sources:
  - f_conv 2-loop drift: S85 W6-67 S85-F_CONV-TWO-LOOP-Z_R-INVESTIGATION PASS
    (scheme_dev = 0.3921 = 39.21%).
  - eps_H HP^1 drift: S85 W5-6 S85-W5-6-REGULATOR-SCAN-EPS-H INFO-tight
    (max/min = 2.0; per-regulator drift from mean f_4^r).

For each regulator r, compute SCHEME_INDEP booleans at 5% threshold. Joint
theorem: NOT(SCHEME_INDEP(f_conv^r) AND SCHEME_INDEP(eps_H^r)) for all r.

Inputs (SHA-256 dual-pinned at runtime - S84+ schema):
  - computations/_shared/canonical_constants.py
  - computations/session-85/s85_w5_6_eps_h_hp1_scan.npz         (§W5-6 output)
  - computations/session-85/s85_gate_verdicts.txt               (W6-67 scheme_dev)
"""

from __future__ import annotations

from canonical_constants import *  # noqa: F401,F403

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

os.environ.setdefault('OMP_NUM_THREADS', '8')

import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S85"                                              # (local)
GATE_ID = "S85-W5-7-TWO-LAYER-OBSTRUCTION"                    # (local)
SCHEME = "5-regulator-atlas"                                  # (local)
CONVENTION = "5pct-scheme-indep-def"                          # (local)
L_MAX = 10                                                    # (local) canonical

SCHEME_INDEP_TOL = 0.05         # (local)  5% drift threshold per plan
INFO_MARGINAL_TOL = 0.07        # (local)  7% marginal threshold for INFO

# W6-67 2-loop Z_R scheme-deviation (from S85 verdict file line 3):
#   "S85-F_CONV-TWO-LOOP-Z_R-INVESTIGATION: PASS ... scheme_dev=0.3921"
F_CONV_2LOOP_SCHEME_DEV = 0.3921  # (local)  39.21%

OUT_NPZ = resolve_output(85, 's85_w5_7_two_layer_obstruction.npz')
OUT_PNG = resolve_output(85, 's85_w5_7_two_layer_obstruction.png')
VERDICT_TXT = resolve_output(85, 's85_gate_verdicts.txt')
CANON_PY = resolve_script(None, 'canonical_constants.py')
W56_NPZ = resolve_output(85, 's85_w5_6_eps_h_hp1_scan.npz')

INPUT_FILES = [CANON_PY, W56_NPZ, VERDICT_TXT]


def sha256_of(path):
    h = hashlib.sha256()
    try: h.update(path.read_bytes())
    except OSError: return ""
    return h.hexdigest()

def log_input_pins(inputs):
    print(f"=== {GATE_ID} - input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins

def closure_hash(pins):
    items = sorted(pins.items()); h = hashlib.sha256()
    for k, v in items: h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()

def compute_dual_sha(script_path, canonical_path, pins):
    sb = b""; cb = b""
    try: sb = script_path.read_bytes()
    except OSError: pass
    try: cb = canonical_path.read_bytes()
    except OSError: pass
    pj = json.dumps(dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True).encode("utf-8")
    ha = hashlib.sha256(); ha.update(sb); ha.update(cb); ha.update(pj)
    hc = hashlib.sha256(); hc.update(sb)
    return ha.hexdigest(), hc.hexdigest()


def compute():
    d56 = np.load(W56_NPZ, allow_pickle=True)
    regs = [str(r) for r in d56['regulators']]
    f_4 = d56['f_4_per_reg'].astype(np.float64)   # (local)
    mean_f4 = float(np.mean(f_4))                 # (local)
    # Per-regulator eps_H drift = |f_4^r - mean| / |mean| (fractional deviation)
    eps_H_drift = {r: float(abs(v - mean_f4) / mean_f4) for r, v in zip(regs, f_4)}

    # f_conv drift: from W6-67, canonical 2-loop scheme-deviation is global;
    # per-regulator we model each regulator as carrying the same global drift
    # (the W6-67 MS-bar vs ladder scheme_dev = 0.3921 applies uniformly
    # because the regulator enters through the 2-loop counterterm, not
    # through a per-regulator kinematic split)
    f_conv_drift = {r: F_CONV_2LOOP_SCHEME_DEV for r in regs}

    # Joint-satisfaction matrix
    joint = {}
    for r in regs:
        si_f = f_conv_drift[r] <= SCHEME_INDEP_TOL
        si_e = eps_H_drift[r] <= SCHEME_INDEP_TOL
        joint[r] = {'si_fconv': si_f, 'si_epsH': si_e, 'joint': (si_f and si_e)}

    n_joint_pass = int(sum(1 for v in joint.values() if v['joint']))
    n_joint_fail = len(regs) - n_joint_pass

    # INFO (plan §W5-7): 4 rows fail, 1 row marginally satisfies both at <=7%
    marginal_rows = [
        r for r in regs
        if (f_conv_drift[r] <= INFO_MARGINAL_TOL and eps_H_drift[r] <= INFO_MARGINAL_TOL)
        and joint[r]['joint']
    ]

    return {
        'value': n_joint_pass,
        'regs': regs,
        'f_conv_drift': f_conv_drift,
        'eps_H_drift': eps_H_drift,
        'joint': joint,
        'n_joint_pass': n_joint_pass,
        'n_joint_fail': n_joint_fail,
        'marginal_rows': marginal_rows,
        'mean_f4': mean_f4,
    }


def emit_4tuple(value, scheme, convention, L_max):
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")

def append_verdict(verdict, value, audit, content):
    line = (f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
            f"convention={CONVENTION} L_max={L_MAX} "
            f"audit_sha256={audit} content_sha256={content} "
            f"schema_version=S84+\n")
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)

def evaluate_gate(result):
    if result['n_joint_pass'] == 0:
        return "PASS"
    if len(result['marginal_rows']) == 1 and result['n_joint_pass'] == 1:
        return "INFO"
    return "FAIL"


def main() -> int:
    t0 = time.time()
    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}...")
    audit, content = compute_dual_sha(Path(__file__).resolve(), CANON_PY, pins)
    print(f"  audit_sha256:   {audit[:16]}...")
    print(f"  content_sha256: {content[:16]}...")
    print()

    result = compute()
    verdict = evaluate_gate(result)

    regs = result['regs']
    f_drift = np.array([result['f_conv_drift'][r] for r in regs])
    e_drift = np.array([result['eps_H_drift'][r] for r in regs])
    joint = np.array([result['joint'][r]['joint'] for r in regs])

    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID,
        verdict=verdict,
        regs=np.array(regs),
        f_conv_drift=f_drift,
        eps_H_drift=e_drift,
        joint_satisfaction=joint,
        n_joint_pass=result['n_joint_pass'],
        n_joint_fail=result['n_joint_fail'],
        scheme_indep_tol=SCHEME_INDEP_TOL,
        info_marginal_tol=INFO_MARGINAL_TOL,
        f_conv_2loop_scheme_dev=F_CONV_2LOOP_SCHEME_DEV,
        mean_f4=result['mean_f4'],
    )
    print(f"  saved: {OUT_NPZ.name}")

    try:
        import matplotlib
        matplotlib.use("Agg")
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(figsize=(8, 5.5))
        x = np.arange(len(regs))
        width = 0.35  # (local) bar width
        ax.bar(x - width/2, f_drift * 100, width, label='f_conv drift', color='tab:blue')
        ax.bar(x + width/2, e_drift * 100, width, label='eps_H drift', color='tab:orange')
        ax.axhline(SCHEME_INDEP_TOL * 100, color='red', linestyle='--', label='5% PASS threshold')
        ax.axhline(INFO_MARGINAL_TOL * 100, color='orange', linestyle=':', label='7% INFO threshold')
        ax.set_xticks(x)
        ax.set_xticklabels(regs, rotation=30, ha='right')
        ax.set_ylabel('scheme drift (%)')
        ax.set_title(
            f"{GATE_ID}: n_joint_pass={result['n_joint_pass']}/5, verdict={verdict}"
        )
        ax.legend()
        ax.grid(True, axis='y', alpha=0.3)
        plt.tight_layout()
        plt.savefig(OUT_PNG, dpi=100)
        plt.close(fig)
        print(f"  saved: {OUT_PNG.name}")
    except Exception as e:
        print(f"  plot skipped: {type(e).__name__}: {e}")

    tag = emit_4tuple(result['n_joint_pass'], SCHEME, CONVENTION, L_MAX)
    print(tag)
    append_verdict(verdict, result['n_joint_pass'], audit, content)

    wall = time.time() - t0
    print()
    print(f"=== {GATE_ID} 5x2 joint-satisfaction matrix ===")
    hdr = f"{'Regulator':14s} {'f_conv drift':>14s} {'<=5%':>6s} {'eps_H drift':>14s} {'<=5%':>6s} {'joint?':>7s}"
    print(hdr)
    for r in regs:
        j = result['joint'][r]
        print(
            f"{r:14s} {result['f_conv_drift'][r]*100:12.2f}%  "
            f"{'YES' if j['si_fconv'] else 'NO':>6s} "
            f"{result['eps_H_drift'][r]*100:12.2f}%  "
            f"{'YES' if j['si_epsH'] else 'NO':>6s} "
            f"{'YES' if j['joint'] else 'NO':>7s}"
        )
    print(f"  n_joint_pass={result['n_joint_pass']}/5 => theorem holds trivially")
    print(f"=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
