#!/usr/bin/env python3
"""
S84 W4-39: N_T-CMB-TRANSFER
============================

Gate: S84-N_T-CMB-TRANSFER
Trigger: [SIGN]
Classification: GEOMETRIC (tensor transfer through emergent g_M)

Hypothesis: n_T(k_CMB) under the G46 eps_H-flow transfer is -3e-3 (RED),
confirming the substrate-scale BLUE tilt does NOT propagate to CMB scales.

Method:
  1. Load S83 G46 transfer kernel (T^2, eps_H_CMB, eps_H_transit, r_CMB).
  2. Evaluate n_T(k_CMB) = -2 * eps_H(k_CMB) in pure slow-roll limit.
  3. Quote the suppression factor vs naive -2*eps_H(fold).
  4. Cross-check against modified consistency relation n_T = -r/8 * (c_T/c_S).
  5. Plot n_T(k) across 54 decades from k_CMB = 0.05 Mpc^-1 to k_transit.

Substrate-framing: the BLUE +0.468 at transit and -3e-3 at CMB are the
SAME physics at different scales. Transit-scale tilt = where relay patterns
are born (GEOMETRIC, Jensen-curvature steepening). CMB-scale n_T = what a
c-bounded observer infers after propagation through emergent g_M (single
e-fold of transit is discarded by c-bounded flatness of transfer kernel).

PRDR machinery pin:
  - k range: [k_CMB=0.05 Mpc^-1, k_transit=5.53e52 Mpc^-1] (54 decades)
  - eps_H scheme: canonical single-field, constant at k_CMB
  - Convention: Planck 2018 sign convention P_t ~ k^{n_T}
  - Numerical tolerance: 1e-5 relative on transfer kernel
  - GPU path: not required (low-cost transfer kernel eval)

Input SHA-256 pins (computed at runtime):
  - canonical_constants.py
  - s83_w3_g46_tensor_transfer.npz
  - s65_blue_tensor_tilt.npz
  - s66_tensor_transfer.npz
"""

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import sys
import hashlib
import json
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from canonical_constants import M_KK, tau_fold  # noqa: E402


# --------------------------------------------------------------------------- #
# SHA-256 input pins (printed in first 20 lines of stdout)
# --------------------------------------------------------------------------- #
def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


INPUT_CANON = SCRIPT_DIR / "canonical_constants.py"
INPUT_S83_G46 = SCRIPT_DIR / "s83_w3_g46_tensor_transfer.npz"
INPUT_S65_BLUE = SCRIPT_DIR / "s65_blue_tensor_tilt.npz"
INPUT_S66_TRANSFER = SCRIPT_DIR / "s66_tensor_transfer.npz"

sha_canon = sha256_file(INPUT_CANON)
sha_s83_g46 = sha256_file(INPUT_S83_G46)
sha_s65_blue = sha256_file(INPUT_S65_BLUE)
sha_s66_transfer = sha256_file(INPUT_S66_TRANSFER)

print(f"[S84 W4-39 N_T-CMB-TRANSFER] input-pin SHA-256:")
print(f"  canonical_constants.py          : {sha_canon}")
print(f"  s83_w3_g46_tensor_transfer.npz  : {sha_s83_g46}")
print(f"  s65_blue_tensor_tilt.npz        : {sha_s65_blue}")
print(f"  s66_tensor_transfer.npz         : {sha_s66_transfer}")


# --------------------------------------------------------------------------- #
# Step 1: load G46 pins from S83
# --------------------------------------------------------------------------- #
g46 = np.load(INPUT_S83_G46, allow_pickle=True)

eps_H_CMB = float(g46["eps_H_CMB"])          # (local) far-field value at k_CMB
eps_H_transit = float(g46["eps_H_transit"])  # (local) fold value
c_T_canon = float(g46["c_T_canon"])          # (local) tensor speed
c_S_canon = float(g46["c_S_canon"])          # (local) scalar speed
T_sq = float(g46["T_sq"])                    # (local) transfer kernel T^2
T_factor = float(g46["T_factor"])            # (local) T = sqrt(T_sq)
r_CMB_G46 = float(g46["r_CMB"])              # (local) framework r at CMB
r_transit_G46 = float(g46["r_transit_formula"])  # (local) framework r at transit
k_transit_T = float(g46["k_transit_T"])      # (local) k_transit / M_KK
tau_CMB_exit = float(g46["tau_CMB_exit"])    # (local) tau at CMB exit
tau_transit_exit = float(g46["tau_transit_exit"])  # (local) tau at transit exit

# --------------------------------------------------------------------------- #
# Step 2: load S65 substrate BLUE tilt and S66 transfer structure
# --------------------------------------------------------------------------- #
s65 = np.load(INPUT_S65_BLUE, allow_pickle=True)
n_T_transit_S65 = float(s65["n_T"])           # (local) +0.4676 BLUE

s66 = np.load(INPUT_S66_TRANSFER, allow_pickle=True)
k_transit_Mpc = float(s66["k_transit_Mpc"])   # (local) ~5.5e52 Mpc^-1
k_CMB_pivot = float(s66["k_CMB_pivot"])       # (local) 0.05 Mpc^-1
decades_separation = float(s66["decades_separation"])  # (local) 54.04
T_h = np.array(s66["T_h"])                    # (local) transfer across CMB range
k_grid = np.array(s66["k_grid"])              # (local) k-grid for plotting
n_T_CMB_scenario_A_S66 = float(s66["n_T_CMB_scenario_A"])  # (local) reference

# --------------------------------------------------------------------------- #
# Step 3: Execute substitution chain [SIGN]
# --------------------------------------------------------------------------- #
# Definitions:
#   n_T^slow-roll(k) = -2 * eps_H(k)          (single-field inflationary identity)
#   eps_H(k_CMB)     = 0.00151  (c-bounded far-field value)
#   eps_H(k_transit) = 0.02160  (van Hove fold value)
#
# Substitution at k_CMB:
n_T_slow_roll_fold = -2.0 * eps_H_transit    # (local) naive pre-transit value
n_T_CMB_predicted = -2.0 * eps_H_CMB         # (local) framework value

# Simplification: suppression factor vs fold slow-roll
suppression_factor = n_T_slow_roll_fold / n_T_CMB_predicted  # (local) should be ~14

# Direction: eps_H_CMB > 0 => n_T < 0 => RED
assert eps_H_CMB > 0, "eps_H_CMB must be positive; slow-roll sign convention broken"
direction = "RED" if n_T_CMB_predicted < 0 else "BLUE"  # (local)

# --------------------------------------------------------------------------- #
# Step 4: Consistency-relation cross-checks
# --------------------------------------------------------------------------- #
# Standard single-field (c_T = c_S = 1): n_T = -r/8
n_T_via_r_over_8 = -r_CMB_G46 / 8.0          # (local) naive -r/8

# Generalized (c_T != c_S): r = -8 * n_T * (c_S / c_T)  =>  n_T = -r * c_T / (8 * c_S)
n_T_via_modified_consistency = -r_CMB_G46 * c_T_canon / (8.0 * c_S_canon)  # (local)

# Deviation from naive -r/8
deviation_from_standard = n_T_CMB_predicted / n_T_via_r_over_8  # (local) ~2.06
# Match to modified consistency:
reconciliation_residual = abs(n_T_CMB_predicted - n_T_via_modified_consistency)  # (local)

# --------------------------------------------------------------------------- #
# Step 5: build n_T(k) across 54 decades for plotting
# --------------------------------------------------------------------------- #
# eps_H runs logarithmically between k_CMB and k_transit (single-field flow)
# Interpolate: ln eps_H vs ln k, linear flow
log_k_CMB = np.log10(k_CMB_pivot)           # (local)
log_k_transit = np.log10(k_transit_Mpc)     # (local)
log_k_arr = np.linspace(log_k_CMB, log_k_transit, 300)  # (local)
k_arr = 10 ** log_k_arr                     # (local)

# Linear-in-log interpolation of eps_H between the two pinned endpoints
eps_H_arr = np.exp(
    np.log(eps_H_CMB)
    + (np.log(eps_H_transit) - np.log(eps_H_CMB))
    * (log_k_arr - log_k_CMB)
    / (log_k_transit - log_k_CMB)
)  # (local)

# Slow-roll tilt at each k, except at the transit-locked endpoint where
# Jensen-curvature BLUE dominates (piecewise). Below a threshold near k_transit,
# n_T = -2 * eps_H; at k_transit the tilt is set by the spectral-action gradient.
n_T_arr = -2.0 * eps_H_arr  # (local) slow-roll everywhere except transit window

# Transit-window BLUE (last two decades of k, conservatively):
k_transit_window_lo = 10 ** (log_k_transit - 2.0)  # (local)
mask_transit = k_arr > k_transit_window_lo  # (local)
n_T_arr_with_blue = n_T_arr.copy()  # (local)
# linear ramp from slow-roll value to +0.468 at the fold
for i, k in enumerate(k_arr):
    if mask_transit[i]:
        frac = (np.log10(k) - (log_k_transit - 2.0)) / 2.0  # (local) in [0,1]
        n_T_arr_with_blue[i] = (1 - frac) * (-2.0 * eps_H_arr[i]) + frac * n_T_transit_S65

# --------------------------------------------------------------------------- #
# PASS/INFO/FAIL verdict
# --------------------------------------------------------------------------- #
# PASS: |n_T(k_CMB) + 3e-3| < 1e-3 AND |n_T(k_CMB)| < 0.01
target_CMB = -3.0e-3  # (local) G46 benchmark
PASS_TOL = 1.0e-3     # (local) plan criterion
INFO_LO, INFO_HI = 0.01, 0.05  # (local) LiteBIRD marginal band

dist_to_benchmark = abs(n_T_CMB_predicted - target_CMB)  # (local)
abs_n_T = abs(n_T_CMB_predicted)                         # (local)

if (dist_to_benchmark < PASS_TOL) and (abs_n_T < INFO_LO):
    verdict = "PASS"
elif INFO_LO <= abs_n_T <= INFO_HI:
    verdict = "INFO"
elif (abs_n_T > INFO_HI) or (n_T_CMB_predicted > 0):
    verdict = "FAIL"
else:
    # |n_T| < 0.01 but far from -3e-3 benchmark => INFO (sub-LiteBIRD but off-target)
    verdict = "INFO"

print()
print(f"[STEP] n_T(k_transit) substrate BLUE (S65 G50) = {n_T_transit_S65:+.6f}")
print(f"[STEP] eps_H(k_transit) = {eps_H_transit:.6e}")
print(f"[STEP] eps_H(k_CMB)     = {eps_H_CMB:.6e}")
print(f"[STEP] eps_H_transit / eps_H_CMB = {eps_H_transit/eps_H_CMB:.4f}")
print(f"[STEP] Naive -2*eps_H(fold)     = {n_T_slow_roll_fold:+.6e}")
print(f"[STEP] Framework n_T(k_CMB)     = {n_T_CMB_predicted:+.6e}")
print(f"[STEP] Suppression factor       = {suppression_factor:.4f} x")
print(f"[STEP] Reference (S66 Sc.A)     = {n_T_CMB_scenario_A_S66:+.6e}")
print(f"[STEP] Match to S66 scenario A  = {abs(n_T_CMB_predicted - n_T_CMB_scenario_A_S66):.3e}")
print()
print(f"[CONSISTENCY] Standard -r/8 (c_T=c_S=1) = {n_T_via_r_over_8:+.6e}")
print(f"[CONSISTENCY] Modified -r*c_T/(8*c_S)   = {n_T_via_modified_consistency:+.6e}")
print(f"[CONSISTENCY] c_T / c_S                 = {c_T_canon/c_S_canon:.6f}")
print(f"[CONSISTENCY] Framework / standard -r/8 = {deviation_from_standard:.4f}")
print(f"[CONSISTENCY] Match to modified ident.  = {reconciliation_residual:.3e}")
print()
print(f"[TRANSFER] k-separation   = {decades_separation:.4f} decades")
print(f"[TRANSFER] T^2 (G46)      = {T_sq:.6e}")
print(f"[TRANSFER] T (G46)        = {T_factor:.6e}")
print(f"[TRANSFER] T_h CMB range  = [{T_h.min():.6e}, {T_h.max():.6e}] (flat=1)")
print()
print(f"[DIRECTION] n_T(k_CMB) sign = {direction}")
print(f"[DIRECTION] |n_T(k_CMB)|    = {abs_n_T:.6e}")
print(f"[DIRECTION] dist to -3e-3   = {dist_to_benchmark:.6e}")
print(f"[VERDICT]  {verdict}")

# --------------------------------------------------------------------------- #
# Plot
# --------------------------------------------------------------------------- #
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(k_arr, n_T_arr_with_blue, lw=2, color='C0',
        label="Framework n_T(k) (slow-roll + transit BLUE ramp)")
ax.axhline(0, color='grey', lw=0.6, ls='-')
ax.axhline(-3e-3, color='C3', lw=1, ls='--', label="G46 benchmark -3e-3")
ax.axhline(n_T_transit_S65, color='C2', lw=1, ls=':',
           label=f"Transit BLUE (S65): +{n_T_transit_S65:.4f}")
ax.axvline(k_CMB_pivot, color='k', lw=0.8, ls=':')
ax.axvline(k_transit_Mpc, color='k', lw=0.8, ls=':')
ax.scatter([k_CMB_pivot], [n_T_CMB_predicted], color='C0', zorder=5, s=80,
           edgecolor='k', label=f"n_T(k_CMB)={n_T_CMB_predicted:+.3e}")
ax.scatter([k_transit_Mpc], [n_T_transit_S65], color='C2', zorder=5, s=80,
           edgecolor='k', label="n_T(k_transit) BLUE")
ax.set_xscale('log')
ax.set_xlabel("k [Mpc^-1]")
ax.set_ylabel("n_T(k)")
ax.set_title(f"S84 W4-39: n_T(k) across {decades_separation:.1f} decades -- verdict {verdict}")
ax.legend(loc='center left', fontsize=9)
ax.grid(True, which='both', alpha=0.3)
plt.tight_layout()

OUT_NPZ = SCRIPT_DIR / "s84_w4_nt_cmb_transfer.npz"
OUT_PNG = SCRIPT_DIR / "s84_w4_nt_cmb_transfer.png"
VERDICT_TXT = SCRIPT_DIR / "s84_gate_verdicts.txt"

plt.savefig(OUT_PNG, dpi=140)
plt.close()

np.savez(
    OUT_NPZ,
    gate_id="S84-N_T-CMB-TRANSFER",
    verdict=verdict,
    n_T_CMB_predicted=n_T_CMB_predicted,
    n_T_slow_roll_fold=n_T_slow_roll_fold,
    n_T_transit_S65=n_T_transit_S65,
    n_T_CMB_scenario_A_S66=n_T_CMB_scenario_A_S66,
    eps_H_CMB=eps_H_CMB,
    eps_H_transit=eps_H_transit,
    suppression_factor=suppression_factor,
    target_CMB=target_CMB,
    dist_to_benchmark=dist_to_benchmark,
    n_T_via_r_over_8=n_T_via_r_over_8,
    n_T_via_modified_consistency=n_T_via_modified_consistency,
    deviation_from_standard=deviation_from_standard,
    reconciliation_residual=reconciliation_residual,
    c_T_canon=c_T_canon,
    c_S_canon=c_S_canon,
    T_sq=T_sq,
    T_factor=T_factor,
    r_CMB_G46=r_CMB_G46,
    k_CMB_pivot=k_CMB_pivot,
    k_transit_Mpc=k_transit_Mpc,
    decades_separation=decades_separation,
    k_arr=k_arr,
    n_T_arr=n_T_arr_with_blue,
    eps_H_arr=eps_H_arr,
    sha_canon=sha_canon,
    sha_s83_g46=sha_s83_g46,
    sha_s65_blue=sha_s65_blue,
    sha_s66_transfer=sha_s66_transfer,
)

# --------------------------------------------------------------------------- #
# Closure SHA (S81+ canonical form: SHA-256 of ordered input-pin map)
# --------------------------------------------------------------------------- #
pin_map = {
    "gate_id": "S84-N_T-CMB-TRANSFER",
    "canonical_constants.py": sha_canon,
    "s83_w3_g46_tensor_transfer.npz": sha_s83_g46,
    "s65_blue_tensor_tilt.npz": sha_s65_blue,
    "s66_tensor_transfer.npz": sha_s66_transfer,
    "value": f"{n_T_CMB_predicted:+.12e}",
    "scheme": "eps_H-flow-transfer-G46",
    "convention": "Planck 2018 P_t ~ k^{n_T}",
    "L_max": "5",
}
pin_str = json.dumps(pin_map, sort_keys=True, separators=(",", ":"))  # (local)
closure_sha = hashlib.sha256(pin_str.encode()).hexdigest()  # (local)

# 4-tuple output tag (final non-verdict line)
print()
print(f"(value={n_T_CMB_predicted:+.6e}, scheme=eps_H-flow-transfer-G46, "
      f"convention=Planck 2018, L_max=5)")
print(f"closure={closure_sha}")

# Append verdict line (S81+ canonical form)
verdict_line = (
    f"S84-N_T-CMB-TRANSFER: {verdict} -- "
    f"value={n_T_CMB_predicted:+.6e} "
    f"scheme=eps_H-flow-transfer-G46 "
    f"convention=Planck-2018 "
    f"L_max=5 "
    f"sha256={closure_sha}\n"
)
with open(VERDICT_TXT, "a") as f:
    f.write(verdict_line)

print(f"[S84 W4-39] verdict appended to {VERDICT_TXT.name}")
print(f"[S84 W4-39] closure SHA: {closure_sha}")
