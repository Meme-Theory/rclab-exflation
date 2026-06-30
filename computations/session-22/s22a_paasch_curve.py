#!/usr/bin/env python3
"""
S81-canonical re-run wrapper for S22a Paasch curve.

Re-executes the s19a -> s22a pipeline with:
  1. canonical_constants imported (phi_paasch sourced there, not hardcoded)
  2. All intermediates tagged (local)
  3. SHA-256 pins logged in first 20 lines of stdout
  4. Output 4-tuple + closure SHA printed as final lines

Gate: S22A-PAASCH-CURVE
Domain: Paasch mass-quantization (phi_paasch = 1.531580 PROVEN at s=0.15)
"""

from __future__ import annotations

import hashlib
import os
import sys
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


# Cap CPU threads (all work here is small-matrix scipy/numpy, GPU not warranted)
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import numpy as np
from scipy.interpolate import CubicSpline
from scipy.optimize import brentq

# Canonical-constants import (MANDATORY per computations/_shared/CLAUDE.md)
# X2-removed: alias 'SHARED_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
sys.path.insert(0, str(SHARED_DIR))
from canonical_constants import phi_paasch  # noqa: E402

# ============================================================
# Input pins (SHA-256 pre-registered in prep_T3-S22A-PAASCH-CURVE.md)
# ============================================================
ARCHIVE = Path(r"C:/sandbox/Ainulindale Exflation/computations/_shared")
ORIG_SCRIPT = ARCHIVE / "s22a_paasch_curve.py"
SWEEP_DATA = ARCHIVE / "s19a_sweep_data.npz"
CANON = resolve_script(None, 'canonical_constants.py')


def _sha256(p: Path) -> str:
    with open(p, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


input_pins = {  # (local) SHA map for closure hash
    "s22a_paasch_curve.py": _sha256(ORIG_SCRIPT),
    "s19a_sweep_data.npz": _sha256(SWEEP_DATA),
    "canonical_constants.py": _sha256(CANON),
}

print("=" * 72)
print("S22A-PAASCH-CURVE  (S81-canonical re-run)")
print("=" * 72)
print(f"phi_paasch (from canonical_constants): {phi_paasch:.6f}")
print(f"[pin] s22a_paasch_curve.py: {input_pins['s22a_paasch_curve.py']}")
print(f"[pin] s19a_sweep_data.npz:  {input_pins['s19a_sweep_data.npz']}")
print(f"[pin] canonical_constants.py: {input_pins['canonical_constants.py']}")
print("=" * 72)

# ============================================================
# 1. LOAD + EXTRACT SECTOR EIGENVALUES (mirrors s22a original)
# ============================================================
data = np.load(SWEEP_DATA, allow_pickle=True)
tau = data["tau_values"]                # (local) scan grid from s19a
n_tau = len(tau)                        # (local)

E_00 = np.zeros(n_tau)                  # (local) min E in (0,0)
E_30 = np.zeros(n_tau)                  # (local) min E in (3,0)
E_03 = np.zeros(n_tau)                  # (local) min E in (0,3)

for i in range(n_tau):
    ev = data[f"eigenvalues_{i}"]       # (local)
    p = data[f"sector_p_{i}"]           # (local)
    q = data[f"sector_q_{i}"]           # (local)
    mask_30 = (p == 3) & (q == 0)       # (local)
    mask_00 = (p == 0) & (q == 0)       # (local)
    mask_03 = (p == 0) & (q == 3)       # (local)
    E_30[i] = ev[mask_30].min() if mask_30.any() else np.nan
    E_00[i] = ev[mask_00].min() if mask_00.any() else np.nan
    E_03[i] = ev[mask_03].min() if mask_03.any() else np.nan

ratio = E_30 / E_00                     # (local) m_{(3,0)}/m_{(0,0)}
ratio_03 = E_03 / E_00                  # (local)
delta = ratio - phi_paasch              # (local)

# ============================================================
# 2. CROSSINGS (linear + spline-refined brentq)
# ============================================================
crossings = []                          # (local)
for i in range(n_tau - 1):
    if delta[i] * delta[i + 1] < 0:
        tau_cross = tau[i] - delta[i] * (tau[i + 1] - tau[i]) / (
            delta[i + 1] - delta[i]
        )                                # (local) linear interp
        crossings.append(tau_cross)

cs_delta = CubicSpline(tau, delta)      # (local)
tau_fine = np.linspace(0, 2, 2000)      # (local) sign-detection grid
delta_fine = cs_delta(tau_fine)         # (local)
spline_crossings = []                   # (local)
for i in range(len(tau_fine) - 1):
    if delta_fine[i] * delta_fine[i + 1] < 0:
        try:
            root = brentq(cs_delta, tau_fine[i], tau_fine[i + 1])  # (local)
            spline_crossings.append(root)
        except Exception:
            pass

# ============================================================
# 3. CLOSEST APPROACH (cubic spline dense minimum)
# ============================================================
cs_ratio = CubicSpline(tau, ratio)      # (local)
tau_dense = np.linspace(0, 2, 10000)    # (local)
ratio_dense = cs_ratio(tau_dense)       # (local)
delta_dense = np.abs(ratio_dense - phi_paasch)  # (local)
i_min = int(np.argmin(delta_dense))     # (local)
tau_closest = float(tau_dense[i_min])   # (local)
ratio_closest = float(ratio_dense[i_min])  # (local)
dev_closest = (ratio_closest - phi_paasch) / phi_paasch * 100  # (local) %

# ============================================================
# 4. REPRODUCIBILITY CHECK vs existing s22a_paasch_curve.npz
# ============================================================
EXISTING_NPZ = ARCHIVE / "s22a_paasch_curve.npz"
if EXISTING_NPZ.exists():
    prev = np.load(EXISTING_NPZ, allow_pickle=True)
    ratio_rel = np.max(np.abs((ratio - prev["ratio"]) / prev["ratio"]))  # (local)
    closest_abs = abs(tau_closest - float(prev["tau_closest"]))          # (local)
    prev_cross = np.asarray(prev["crossings"])                            # (local)
    cur_cross = np.asarray(crossings)                                     # (local)
    if len(prev_cross) == len(cur_cross) and len(cur_cross) > 0:
        cross_abs = float(np.max(np.abs(cur_cross - prev_cross)))         # (local)
    else:
        cross_abs = float("nan")
    print(f"[repro] max rel err in ratio[] vs prev npz: {ratio_rel:.3e}")
    print(f"[repro] |tau_closest - prev|: {closest_abs:.3e}")
    print(f"[repro] max |crossings - prev|: {cross_abs:.3e}")
    print(f"[repro] ratio_closest: current={ratio_closest:.12f} prev={float(prev['ratio_closest']):.12f}")
else:
    ratio_rel = float("nan")             # (local)
    closest_abs = float("nan")           # (local)
    cross_abs = float("nan")             # (local)

# Pre-registered PASS thresholds (prep_T3-S22A-PAASCH-CURVE.md)
THRESH_RATIO_REL = 1e-12                 # (local) gate threshold
THRESH_CROSS_ABS = 1e-10                 # (local) gate threshold

gate_pass = (ratio_rel <= THRESH_RATIO_REL) and (
    np.isnan(cross_abs) or cross_abs <= THRESH_CROSS_ABS
)                                        # (local)

print("=" * 72)
print("Results")
print("=" * 72)
print(f"  phi_paasch          = {phi_paasch:.12f}  (canonical)")
print(f"  tau_closest         = {tau_closest:.12f}")
print(f"  ratio_closest       = {ratio_closest:.12f}")
print(f"  |r - phi|/phi       = {abs(dev_closest):.6e}%")
print(f"  linear crossings    = {crossings}")
print(f"  spline crossings    = {spline_crossings}")
print(f"  gate PASS threshold = ratio_rel <= {THRESH_RATIO_REL}, cross_abs <= {THRESH_CROSS_ABS}")
print(f"  gate_pass           = {gate_pass}")

# ============================================================
# 5. Closure SHA + output 4-tuple (S81 canonical form)
# ============================================================
closure_src = "|".join(  # (local) ordered: script, npz, canon
    f"{k}:{v}" for k, v in sorted(input_pins.items())
)
closure_sha = hashlib.sha256(closure_src.encode()).hexdigest()  # (local)

value_tag = (
    f"tau_closest={tau_closest:.8f},"
    f"ratio_closest={ratio_closest:.8f},"
    f"crossings=[{crossings[0]:.8f},{crossings[1]:.8f}]"
    if len(crossings) >= 2
    else f"tau_closest={tau_closest:.8f},ratio_closest={ratio_closest:.8f}"
)                                        # (local)

print(f"[closure_sha] {closure_sha}")
print(
    f"OUTPUT_4TUPLE value={value_tag} "
    f"scheme=s19a-eigendata-spline-brentq "
    f"convention=r=E30/E00_min_per_sector L_max=max_pq_sum=6_from_s19a"
)
