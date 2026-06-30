#!/usr/bin/env python3
"""
s75_ec_observable_mapping.py -- A_s as function of E_C (condensation energy)
===========================================================================

Gate: S75-A7-EC-MAP  (Session 75 Wave 2, W2-G)
  PASS: Monotone AND |delta_A_s| < 0.05 OOM for +/- 5% E_C shift
  INFO: Monotone but |delta_A_s| in [0.05, 0.20] OOM
  FAIL: Non-monotone OR |delta_A_s| > 0.20 OOM

PHYSICS (substrate framing):
    E_C = Delta_BCS = 0.4643 M_KK is the canonical BCS gap (Method A,
    S74 W1-D: pair-addition energy from exact diagonalization).

    The A_s chain (W1-G) depends on E_C through:
      1. BCS coherence factors u_k, v_k via:
            xi_k = eps_k - mu
            E_k = sqrt(xi_k^2 + Delta^2)
            v_k^2 = (1/2)(1 - xi_k/E_k)
            u_k^2 = (1/2)(1 + xi_k/E_k)
      2. Squeeze parameters r_k:
         - B2 flat band (xi~0): regularized via van Hove averaged cosh(2r)
           over bandwidth W_B2 with cutoff |xi| >= 0.01*Delta
         - B1, B3: r_k = arctanh(v_k/u_k) or arctanh(min/max sqrt ratio)
      3. Squeezed vacuum variance:
            sigma_k^2 = (1/(2*omega_k))(cosh(2r_k) - sinh(2r_k)*cos(phi_k))
      4. Peter-Weyl filter + BLV dilution -> A_s

    This script parameterizes E_C in [0.4, 0.5] M_KK (20% range around
    canonical 0.4643), recomputes the full chain for each value, and
    reports A_s(E_C) and dA_s/dE_C.

Session: S75 W2-G
Author: landau-condensed-matter-theorist
Depends on: s74_as_from_bogoliubov.npz (W1-G chain),
            s69_squeeze_reconciled.npz (van Hove regularization),
            s65_ab_mode_as.npz (H_phys, M_Pl, eps_H),
            s74_transfer_function.npz (omega_Bi),
            canonical_constants (Delta_BCS, A_s_CMB, etc.)
"""

import sys
import os
import time
import numpy as np
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPT_DIR))

from canonical_constants import (
    tau_fold, a2_fold, A_s_CMB, PI, M_KK,
    c_Gold, c_fabric, c_Gold_over_c_fabric,
    Delta_BCS, E_cond, E_B1, E_B2_mean, E_B3_mean,
)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

OUT_NPZ = SCRIPT_DIR / "s75_ec_observable_mapping.npz"
OUT_PNG = SCRIPT_DIR / "s75_ec_observable_mapping.png"

t_start = time.time()

print("=" * 78)
print("S75 W2-G  S75-A7-EC-MAP: A_s as Function of E_C (Method A)")
print("=" * 78)

# =============================================================================
# SECTION 1: Load reference data from S74 W1-G chain
# =============================================================================
print("\n--- Section 1: Load reference data ---")

# S65 physical parameters (H, M_Pl, eps_H -- independent of Delta)
d_s65 = np.load(SCRIPT_DIR / "s65_ab_mode_as.npz", allow_pickle=True)
c_BLV = float(d_s65['c_BLV'])            # 0.485
eps_H_fold = float(d_s65['eps_H_fold'])   # (local)
H_phys_sq = float(d_s65['H_phys_sq'])    # (local)
M_Pl_sq = float(d_s65['M_Pl_sq'])        # (local)

# S74 W1-A transfer function (omega_Bi -- mode frequencies at fold)
d_s74_tf = np.load(SCRIPT_DIR / "s74_transfer_function.npz", allow_pickle=True)
omega_B1 = float(d_s74_tf['omega_B1'])    # (local)
omega_B2 = float(d_s74_tf['omega_B2'])    # (local)
omega_B3 = float(d_s74_tf['omega_B3'])    # (local)

# S69 reconciled squeeze data (for band structure, mu, xi)
d_s69 = np.load(SCRIPT_DIR / "s69_squeeze_reconciled.npz", allow_pickle=True)
mu_BCS_canonical = float(d_s69['mu_BCS'])  # (local) = 0.845 M_KK

# S74 W1-G data (for cross-check)
d_s74 = np.load(SCRIPT_DIR / "s74_as_from_bogoliubov.npz", allow_pickle=True)
A_s_s74 = float(d_s74['A_s_computed'])     # (local) = 6.22
gap_s74 = float(d_s74['gap_OOM_vs_planck'])  # (local) = 9.47

print(f"  H_phys^2 = {H_phys_sq:.6f} M_KK^2")
print(f"  M_Pl^2 = {M_Pl_sq:.6f} M_KK^2")
print(f"  eps_H = {eps_H_fold:.6f}")
print(f"  c_BLV = {c_BLV:.4f}")
print(f"  omega_B1 = {omega_B1:.4f}, omega_B2 = {omega_B2:.4f}, omega_B3 = {omega_B3:.4f}")
print(f"  mu_BCS = {mu_BCS_canonical:.4f} M_KK")
print(f"  Delta_BCS (canonical) = {Delta_BCS:.6f} M_KK")
print(f"  A_s(S74 W1-G) = {A_s_s74:.4e} (gap = {gap_s74:.4f} OOM)")

# =============================================================================
# SECTION 2: Define the A_s(E_C) computation chain
# =============================================================================
print("\n--- Section 2: Define A_s(E_C) chain ---")

# Mode structure (8 modes: 4 B2 + 1 B1 + 3 B3)
N_modes = 8  # (local)
labels = ['B2[0]', 'B2[1]', 'B2[2]', 'B2[3]', 'B1', 'B3[0]', 'B3[1]', 'B3[2]']  # (local)
branch = np.array(['B2','B2','B2','B2','B1','B3','B3','B3'])  # (local)

# Single-particle energies at fold (from canonical constants)
eps_fold = np.array([  # (local) M_KK units
    E_B2_mean, E_B2_mean, E_B2_mean, E_B2_mean,  # B2 degenerate
    E_B1,                                           # B1
    E_B3_mean, E_B3_mean, E_B3_mean,               # B3 degenerate
])

# Chemical potential = mu_BCS (sets the Fermi surface at B2)
mu = mu_BCS_canonical  # (local)
xi_fold = eps_fold - mu  # (local) xi_k = eps_k - mu

print(f"  Single-particle energies (M_KK):")
for i in range(N_modes):
    print(f"    {labels[i]}: eps = {eps_fold[i]:.6f}, xi = {xi_fold[i]:.6f}")

# Frequencies (independent of Delta -- set by spectral geometry)
omega_k = np.array([  # (local)
    omega_B2, omega_B2, omega_B2, omega_B2,
    omega_B1,
    omega_B3, omega_B3, omega_B3,
])

# Peter-Weyl sector filter (from S74 W1-G: B1, B2 kept; B3 filtered)
def dim_pq(p, q):
    return (p + 1) * (q + 1) * (p + q + 2) // 2

mult_00 = dim_pq(0, 0) ** 2  # (local) = 1
mult_11 = dim_pq(1, 1) ** 2  # (local) = 64
mult_10 = dim_pq(1, 0) ** 2  # (local) = 9
mult_01 = dim_pq(0, 1) ** 2  # (local) = 9

d_pq_sq = np.array([  # (local) PW multiplicity per mode
    mult_11 / 4.0, mult_11 / 4.0, mult_11 / 4.0, mult_11 / 4.0,  # B2
    mult_00,                                                         # B1
    (mult_10 + mult_01) / 3.0, (mult_10 + mult_01) / 3.0, (mult_10 + mult_01) / 3.0,  # B3
])

Theta_pp = np.array([  # (local) (p,p) filter
    1.0, 1.0, 1.0, 1.0,   # B2 = (1,1) kept
    1.0,                    # B1 = (0,0) kept
    0.0, 0.0, 0.0,         # B3 filtered
])

# Phase: phi_k = pi + 2.4e-4 (sudden quench)
delta_phi = 2.4e-4  # (local)
phi_k = np.full(N_modes, PI + delta_phi)  # (local)

# BLV factor
blv_factor = c_BLV ** (-3.0)  # (local)

# GM template (independent of Delta)
P_0_GM = H_phys_sq / (8.0 * PI**2 * eps_H_fold * M_Pl_sq)  # (local)

print(f"\n  P_0 (GM template) = {P_0_GM:.4e}")
print(f"  BLV factor = {blv_factor:.4f}")
print(f"  PW weights: {d_pq_sq}")
print(f"  Theta filter: {Theta_pp}")

# Bandwidth parameters (from S69, fixed by spectral geometry, NOT Delta)
W_B2 = 0.001  # (local) B2 flat band width ~ negligible (degeneracy lifting)
W_B1 = 0.15   # (local) B1 bandwidth
W_B3 = 0.20   # (local) B3 bandwidth
N_quad = 2000  # (local) quadrature points for van Hove integral


# =============================================================================
# SECTION 3: Van Hove regularized cosh(2r) function
# =============================================================================
print("\n--- Section 3: Van Hove regularized squeeze ---")

def vH_cosh2r_band(xi_center, bandwidth, Delta_val, n_quad=2000):
    """
    Compute van Hove averaged cosh(2r) = <E_k/|xi_k|> over a band
    centered at xi_center with width bandwidth.

    For the BCS Bogoliubov transformation:
        cosh(2r_k) = E_k / |xi_k| = sqrt(xi_k^2 + Delta^2) / |xi_k|

    This diverges logarithmically when the band crosses the Fermi surface
    (xi=0). Regularized with cutoff at |xi| >= 0.01*Delta.

    Returns: (cosh2r_avg, crosses_fermi)
    """
    xi_min = xi_center - bandwidth / 2.0  # (local)
    xi_max = xi_center + bandwidth / 2.0  # (local)

    crosses_fermi = (xi_min < 0 and xi_max > 0) or abs(xi_center) < 1e-10  # (local)

    if crosses_fermi:
        eps_cutoff = Delta_val * 0.01  # (local)
        n_half = n_quad // 2  # (local)
        xi_pos = np.linspace(eps_cutoff, max(bandwidth / 2, eps_cutoff * 2), n_half)  # (local)
        xi_neg = np.linspace(-max(bandwidth / 2, eps_cutoff * 2), -eps_cutoff, n_half)  # (local)
        xi_arr = np.concatenate([xi_neg, xi_pos])  # (local)
        E_arr = np.sqrt(xi_arr**2 + Delta_val**2)  # (local)
        cosh2r_arr = E_arr / np.abs(xi_arr)  # (local)
        return np.mean(cosh2r_arr), crosses_fermi

    # Band does not cross Fermi surface
    if abs(xi_center) < 1e-15:
        return np.sqrt(Delta_val**2) / max(abs(xi_center), 1e-15), crosses_fermi

    if xi_center > 0:
        xi_bottom = max(xi_min, 0.001 * Delta_val)  # (local)
        xi_top = xi_max  # (local)
    else:
        xi_bottom = max(abs(xi_max), 0.001 * Delta_val)  # (local)
        xi_top = abs(xi_min)  # (local)

    W_eff = xi_top - xi_bottom  # (local)
    if W_eff <= 0:
        E_c = np.sqrt(xi_center**2 + Delta_val**2)  # (local)
        return E_c / abs(xi_center), crosses_fermi

    t_max = np.sqrt(W_eff)  # (local)
    t = np.linspace(1e-10, t_max, n_quad)  # (local)
    xi_arr = xi_bottom + t**2  # (local)
    E_arr = np.sqrt(xi_arr**2 + Delta_val**2)  # (local)
    cosh2r_arr = E_arr / xi_arr  # (local)
    return np.mean(cosh2r_arr), crosses_fermi


def compute_r_k(Delta_val, xi_k_arr, mu_val, bandwidths, n_quad=2000):
    """
    Compute per-mode BCS squeeze parameters r_k for given Delta.

    For each mode:
    - If |xi_k| < bandwidth/2 (near Fermi surface): use van Hove regularized
    - Otherwise: standard r_k = arctanh(v_k/u_k)

    The van Hove regularization computes <cosh(2r)> over the band,
    then converts to r = 0.5 * arccosh(<cosh(2r)>).

    Returns: array of r_k values (shape N_modes)
    """
    N = len(xi_k_arr)  # (local)
    r_out = np.zeros(N)  # (local)
    cosh2r_out = np.zeros(N)  # (local)

    for i in range(N):
        xi = xi_k_arr[i]  # (local)
        E_qp = np.sqrt(xi**2 + Delta_val**2)  # (local)

        # BCS coherence factors
        if E_qp > 1e-15:
            v2 = 0.5 * (1.0 - xi / E_qp)  # (local)
            u2 = 0.5 * (1.0 + xi / E_qp)  # (local)
        else:
            v2 = 0.5  # (local)
            u2 = 0.5  # (local)

        # Determine which bandwidth applies
        bw = bandwidths[i]  # (local)

        # For near-degenerate modes (|xi| < bw/2 or flat band):
        if abs(xi) < bw / 2.0 or abs(u2 - v2) < 1e-8:
            # Van Hove regularized
            c2r, _ = vH_cosh2r_band(xi, bw, Delta_val, n_quad)  # (local)
            cosh2r_out[i] = c2r
            r_out[i] = 0.5 * np.arccosh(max(c2r, 1.0))
        else:
            # Standard BCS: r_k = arctanh(min/max ratio)
            ratio = np.sqrt(min(u2, v2) / max(u2, v2))  # (local)
            r_out[i] = np.arctanh(min(ratio, 0.9999))
            cosh2r_out[i] = np.cosh(2.0 * r_out[i])

    return r_out, cosh2r_out


def compute_As(Delta_val, r_k_arr, omega_k_arr, phi_k_arr, d_pq_arr,
               Theta_arr, blv, P_0):
    """
    Full A_s computation from r_k array, following W1-G chain.

    Returns: A_s, gap_OOM, sigma_sq_bare, sigma_sq_filtered
    """
    # Squeezed vacuum variance per mode
    sigma_sq = (1.0 / (2.0 * omega_k_arr)) * (  # (local)
        np.cosh(2.0 * r_k_arr) - np.sinh(2.0 * r_k_arr) * np.cos(phi_k_arr)
    )

    # PW filter
    sigma_sq_filt = sigma_sq * Theta_arr  # (local)

    # Bare vacuum (r=0) PW-weighted sum for normalization
    bare_vac_weighted = np.sum(d_pq_arr / (2.0 * omega_k_arr))  # (local)

    # Squeeze factor
    F_squeeze = np.sum(sigma_sq * d_pq_arr) / bare_vac_weighted  # (local)

    # Filter factor
    filt_total = np.sum(sigma_sq_filt * d_pq_arr)  # (local)
    bare_total = np.sum(sigma_sq * d_pq_arr)  # (local)
    F_filter = filt_total / bare_total if bare_total > 0 else 0.0  # (local)

    # Combined
    F_total = F_squeeze * F_filter * blv  # (local)
    A_s_val = P_0 * F_total  # (local)
    gap = np.log10(A_s_val / A_s_CMB) if A_s_val > 0 else -999.0  # (local)

    return A_s_val, gap, sigma_sq, sigma_sq_filt, F_squeeze, F_filter


# Per-mode bandwidths
bw_per_mode = np.array([  # (local)
    W_B2, W_B2, W_B2, W_B2,  # B2 flat band
    W_B1,                      # B1
    W_B3, W_B3, W_B3,          # B3
])

# =============================================================================
# SECTION 4: Cross-check at canonical Delta
# =============================================================================
print("\n--- Section 4: Cross-check at canonical Delta ---")

r_k_check, cosh2r_check = compute_r_k(Delta_BCS, xi_fold, mu, bw_per_mode, N_quad)
A_s_check, gap_check, _, _, F_sq_check, F_filt_check = compute_As(
    Delta_BCS, r_k_check, omega_k, phi_k, d_pq_sq, Theta_pp, blv_factor, P_0_GM
)

print(f"  Delta = {Delta_BCS:.6f} M_KK (canonical)")
print(f"  r_k (recomputed):")
for i in range(N_modes):
    print(f"    {labels[i]}: r = {r_k_check[i]:.6f}, cosh(2r) = {cosh2r_check[i]:.4f}")

# Compare with S74 values
r_k_s74 = np.array(d_s74['r_k'])  # (local)
print(f"\n  Comparison with S74 W1-G r_k:")
print(f"  {'Mode':<8} {'This':>10} {'S74':>10} {'Ratio':>10}")
for i in range(N_modes):
    ratio = r_k_check[i] / r_k_s74[i] if r_k_s74[i] > 0 else float('inf')  # (local)
    print(f"  {labels[i]:<8} {r_k_check[i]:>10.6f} {r_k_s74[i]:>10.6f} {ratio:>10.4f}")

print(f"\n  A_s (this) = {A_s_check:.4e}, gap = {gap_check:.4f} OOM")
print(f"  A_s (S74)  = {A_s_s74:.4e}, gap = {gap_s74:.4f} OOM")
print(f"  Difference = {gap_check - gap_s74:+.4f} OOM")

# NOTE: The r_k values may differ from S74 because S74 used pre-computed
# r_k_bcs from S72/S70 which had a specific compound squeeze treatment.
# This script uses the BCS-only squeeze from first principles.
# The absolute gap values may differ, but the SENSITIVITY (dA_s/dE_C)
# is what matters for the gate.

# =============================================================================
# SECTION 5: E_C scan
# =============================================================================
print("\n--- Section 5: E_C scan over [0.4, 0.5] M_KK ---")

N_scan = 101  # (local) fine grid for smooth derivatives
E_C_range = np.linspace(0.4, 0.5, N_scan)  # (local)
E_C_canonical = Delta_BCS  # (local) = 0.4643

A_s_scan = np.zeros(N_scan)     # (local)
gap_scan = np.zeros(N_scan)     # (local)
r_k_scan = np.zeros((N_scan, N_modes))  # (local)
F_sq_scan = np.zeros(N_scan)    # (local)
F_filt_scan = np.zeros(N_scan)  # (local)

for j in range(N_scan):
    Delta_j = E_C_range[j]  # (local)

    # Recompute r_k for this Delta
    r_j, c2r_j = compute_r_k(Delta_j, xi_fold, mu, bw_per_mode, N_quad)  # (local)

    # Compute A_s
    As_j, gap_j, _, _, Fsq_j, Ffilt_j = compute_As(  # (local)
        Delta_j, r_j, omega_k, phi_k, d_pq_sq, Theta_pp, blv_factor, P_0_GM
    )

    A_s_scan[j] = As_j
    gap_scan[j] = gap_j
    r_k_scan[j, :] = r_j
    F_sq_scan[j] = Fsq_j
    F_filt_scan[j] = Ffilt_j

# Report key values
print(f"\n  E_C scan results (selected values):")
print(f"  {'E_C':>8} {'A_s':>12} {'gap_OOM':>10} {'r_B2[0]':>10} {'r_B1':>10} {'r_B3[0]':>10}")
for idx in [0, 25, 50, 75, 100]:
    if idx < N_scan:
        print(f"  {E_C_range[idx]:8.4f} {A_s_scan[idx]:12.4e} {gap_scan[idx]:10.4f} "
              f"{r_k_scan[idx, 0]:10.6f} {r_k_scan[idx, 4]:10.6f} {r_k_scan[idx, 5]:10.6f}")

# =============================================================================
# SECTION 6: Monotonicity and sensitivity analysis
# =============================================================================
print("\n--- Section 6: Monotonicity and sensitivity ---")

# Check monotonicity: is A_s monotonically increasing or decreasing in E_C?
dAs = np.diff(A_s_scan)  # (local) length N_scan - 1
all_positive = np.all(dAs > 0)  # (local)
all_negative = np.all(dAs < 0)  # (local)
monotone = all_positive or all_negative  # (local)

if monotone:
    direction = "increasing" if all_positive else "decreasing"  # (local)
    print(f"  A_s is MONOTONE {direction} in E_C over [0.4, 0.5] M_KK")
else:
    # Find sign changes
    sign_changes = np.where(np.diff(np.sign(dAs)) != 0)[0]  # (local)
    print(f"  A_s is NON-MONOTONE: {len(sign_changes)} sign change(s) in dA_s/dE_C")
    for sc in sign_changes:
        print(f"    Sign change near E_C = {E_C_range[sc+1]:.4f} M_KK")

# Derivative dA_s/dE_C at canonical value
# Use central difference at the nearest grid point
idx_canon = np.argmin(np.abs(E_C_range - E_C_canonical))  # (local)
if 0 < idx_canon < N_scan - 1:
    dE = E_C_range[idx_canon + 1] - E_C_range[idx_canon - 1]  # (local)
    dAs_dEc = (A_s_scan[idx_canon + 1] - A_s_scan[idx_canon - 1]) / dE  # (local)
    # In OOM: d(log10(A_s))/dE_C
    dgap_dEc = (gap_scan[idx_canon + 1] - gap_scan[idx_canon - 1]) / dE  # (local)
else:
    dAs_dEc = 0.0  # (local)
    dgap_dEc = 0.0  # (local)

print(f"\n  At canonical E_C = {E_C_canonical:.4f} M_KK:")
print(f"    dA_s/dE_C = {dAs_dEc:.4e}")
print(f"    d(gap_OOM)/dE_C = {dgap_dEc:.4f} OOM / M_KK")

# Gate criterion: +/- 5% shift in E_C
E_C_plus5 = E_C_canonical * 1.05   # (local)
E_C_minus5 = E_C_canonical * 0.95  # (local)

# Interpolate gap at +/- 5%
gap_at_canon = np.interp(E_C_canonical, E_C_range, gap_scan)  # (local)
gap_at_plus5 = np.interp(E_C_plus5, E_C_range, gap_scan)      # (local)
gap_at_minus5 = np.interp(E_C_minus5, E_C_range, gap_scan)    # (local)

delta_gap_plus5 = gap_at_plus5 - gap_at_canon    # (local)
delta_gap_minus5 = gap_at_minus5 - gap_at_canon   # (local)
max_delta_gap_5pct = max(abs(delta_gap_plus5), abs(delta_gap_minus5))  # (local)

print(f"\n  +/- 5% E_C shift sensitivity:")
print(f"    E_C - 5% = {E_C_minus5:.4f}: gap = {gap_at_minus5:.4f}, delta = {delta_gap_minus5:+.6f} OOM")
print(f"    E_C (canon) = {E_C_canonical:.4f}: gap = {gap_at_canon:.4f}")
print(f"    E_C + 5% = {E_C_plus5:.4f}: gap = {gap_at_plus5:.4f}, delta = {delta_gap_plus5:+.6f} OOM")
print(f"    Max |delta_gap| for +/- 5% = {max_delta_gap_5pct:.6f} OOM")

# Also check +/- 10% for context
E_C_plus10 = E_C_canonical * 1.10  # (local)
E_C_minus10 = E_C_canonical * 0.90  # (local)
gap_at_plus10 = np.interp(E_C_plus10, E_C_range, gap_scan)   # (local)
gap_at_minus10 = np.interp(E_C_minus10, E_C_range, gap_scan)  # (local)
delta_gap_plus10 = gap_at_plus10 - gap_at_canon   # (local)
delta_gap_minus10 = gap_at_minus10 - gap_at_canon  # (local)
max_delta_gap_10pct = max(abs(delta_gap_plus10), abs(delta_gap_minus10))  # (local)

print(f"\n  +/- 10% E_C shift sensitivity:")
print(f"    E_C - 10% = {E_C_minus10:.4f}: gap = {gap_at_minus10:.4f}, delta = {delta_gap_minus10:+.6f} OOM")
print(f"    E_C + 10% = {E_C_plus10:.4f}: gap = {gap_at_plus10:.4f}, delta = {delta_gap_plus10:+.6f} OOM")
print(f"    Max |delta_gap| for +/- 10% = {max_delta_gap_10pct:.6f} OOM")

# Elasticity: % change in A_s per % change in E_C
As_at_canon = np.interp(E_C_canonical, E_C_range, A_s_scan)  # (local)
As_at_plus5 = np.interp(E_C_plus5, E_C_range, A_s_scan)      # (local)
As_at_minus5 = np.interp(E_C_minus5, E_C_range, A_s_scan)    # (local)

elasticity_plus = ((As_at_plus5 - As_at_canon) / As_at_canon) / 0.05  # (local)
elasticity_minus = ((As_at_minus5 - As_at_canon) / As_at_canon) / (-0.05)  # (local)
elasticity = (elasticity_plus + elasticity_minus) / 2.0  # (local)

print(f"\n  Elasticity (d ln A_s / d ln E_C):")
print(f"    From +5%: {elasticity_plus:.4f}")
print(f"    From -5%: {elasticity_minus:.4f}")
print(f"    Average: {elasticity:.4f}")

# =============================================================================
# SECTION 7: Physical interpretation
# =============================================================================
print("\n--- Section 7: Physical interpretation ---")

print(f"""
  The A_s(E_C) mapping reveals the sensitivity of the scalar amplitude
  to the BCS condensation energy.

  Chain: E_C = Delta -> u_k, v_k -> r_k -> sigma_sq -> PW filter -> BLV -> A_s

  The key physics:
  - B2 flat band (xi ~ 0): cosh(2r) = Delta/|xi| >> 1. The van Hove
    regularized <cosh(2r)> depends on Delta through the infrared cutoff
    and the integrand sqrt(xi^2 + Delta^2)/|xi|. When Delta changes by
    5%, the cutoff at 0.01*Delta shifts proportionally.
  - B1 mode (xi = {xi_fold[4]:.4f}): E_k = sqrt(xi^2 + Delta^2). Since
    |xi| << Delta, E_k ~ Delta and cosh(2r) ~ Delta/|xi| ~ Delta.
    Direct proportionality expected.
  - B3 modes (xi = {xi_fold[5]:.4f}): xi/Delta ~ {abs(xi_fold[5])/Delta_BCS:.3f}.
    In the intermediate regime where both xi and Delta matter.
  - Peter-Weyl filter kills B3 contributions (Theta=0), so only B1+B2
    matter for A_s.

  The overall sensitivity is:
    d(log10(A_s)) / d(E_C) = {dgap_dEc:.4f} OOM per M_KK
    At +/- 5%: max shift = {max_delta_gap_5pct:.6f} OOM

  For comparison, the A_s gap is {gap_at_canon:.2f} OOM -- the 5% shift
  is {max_delta_gap_5pct/abs(gap_at_canon)*100:.4f}% of the total gap.
""")

# =============================================================================
# SECTION 8: Gate verdict
# =============================================================================
print("\n--- Section 8: Gate verdict ---")

if monotone and max_delta_gap_5pct < 0.05:
    verdict = "PASS"  # (local)
    verdict_msg = (f"A_s(E_C) is monotone ({direction}) AND |delta_gap| = "  # (local)
                   f"{max_delta_gap_5pct:.6f} OOM < 0.05 OOM for +/- 5% E_C shift. "
                   f"A_s is robust to E_C uncertainty.")
elif monotone and max_delta_gap_5pct < 0.20:
    verdict = "INFO"  # (local)
    verdict_msg = (f"A_s(E_C) is monotone ({direction}) but |delta_gap| = "  # (local)
                   f"{max_delta_gap_5pct:.6f} OOM is in [0.05, 0.20] OOM range. "
                   f"Moderate sensitivity to E_C.")
elif not monotone:
    verdict = "FAIL"  # (local)
    verdict_msg = (f"A_s(E_C) is NON-MONOTONE over [0.4, 0.5] M_KK. "  # (local)
                   f"E_C does not have a unique mapping to A_s.")
else:
    verdict = "FAIL"  # (local)
    verdict_msg = (f"|delta_gap| = {max_delta_gap_5pct:.6f} OOM > 0.20 OOM for "  # (local)
                   f"+/- 5% E_C shift. A_s is too sensitive to E_C uncertainty.")

print(f"\n  Gate S75-A7-EC-MAP: {verdict}")
print(f"  {verdict_msg}")

# =============================================================================
# SECTION 9: Save results
# =============================================================================
print("\n--- Section 9: Save results ---")

save_dict = {
    'gate_name': 'S75-A7-EC-MAP',
    'gate_verdict': verdict,
    'gate_detail': verdict_msg,
    # Scan data
    'E_C_range': E_C_range,
    'A_s_scan': A_s_scan,
    'gap_scan': gap_scan,
    'r_k_scan': r_k_scan,
    'F_sq_scan': F_sq_scan,
    'F_filt_scan': F_filt_scan,
    # Key values
    'E_C_canonical': E_C_canonical,
    'A_s_canonical': As_at_canon,
    'gap_canonical': gap_at_canon,
    'monotone': monotone,
    'max_delta_gap_5pct': max_delta_gap_5pct,
    'max_delta_gap_10pct': max_delta_gap_10pct,
    'delta_gap_plus5': delta_gap_plus5,
    'delta_gap_minus5': delta_gap_minus5,
    'dgap_dEc': dgap_dEc,
    'elasticity': elasticity,
    # Cross-check
    'r_k_check': r_k_check,
    'A_s_check': A_s_check,
    'gap_check': gap_check,
    'A_s_s74_reference': A_s_s74,
    'gap_s74_reference': gap_s74,
}

np.savez(OUT_NPZ, **save_dict)
print(f"  Saved: {OUT_NPZ}")

# =============================================================================
# SECTION 10: Plot
# =============================================================================
print("\n--- Section 10: Plot ---")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('S75 W2-G: A_s as Function of E_C (Method A)', fontsize=14)

# (a) A_s vs E_C
ax = axes[0, 0]
ax.semilogy(E_C_range, A_s_scan, 'b-', lw=2)
ax.axvline(E_C_canonical, color='red', ls='--', lw=1.5, label=f'E_C canonical = {E_C_canonical:.4f}')
ax.axvline(E_C_minus5, color='orange', ls=':', lw=1, label='-5%')
ax.axvline(E_C_plus5, color='orange', ls=':', lw=1, label='+5%')
ax.axhline(A_s_CMB, color='green', ls='--', lw=1.5, alpha=0.7, label=f'Planck A_s = {A_s_CMB:.1e}')
ax.set_xlabel('E_C (M_KK)')
ax.set_ylabel('A_s')
ax.set_title('(a) A_s vs E_C')
ax.legend(fontsize=8)

# (b) gap_OOM vs E_C
ax = axes[0, 1]
ax.plot(E_C_range, gap_scan, 'b-', lw=2)
ax.axvline(E_C_canonical, color='red', ls='--', lw=1.5)
ax.axvline(E_C_minus5, color='orange', ls=':', lw=1)
ax.axvline(E_C_plus5, color='orange', ls=':', lw=1)
ax.axhline(0, color='green', ls='--', lw=1, alpha=0.5, label='Planck (0 OOM)')
ax.set_xlabel('E_C (M_KK)')
ax.set_ylabel('gap_OOM = log10(A_s/A_s_Planck)')
ax.set_title('(b) OOM gap vs E_C')
ax.legend(fontsize=8)

# (c) r_k vs E_C for each branch
ax = axes[1, 0]
ax.plot(E_C_range, r_k_scan[:, 0], 'b-', lw=2, label='B2[0]')
ax.plot(E_C_range, r_k_scan[:, 4], 'r-', lw=2, label='B1')
ax.plot(E_C_range, r_k_scan[:, 5], 'g-', lw=2, label='B3[0]')
ax.axvline(E_C_canonical, color='gray', ls='--', lw=1)
ax.set_xlabel('E_C (M_KK)')
ax.set_ylabel('r_k (squeeze parameter)')
ax.set_title('(c) Squeeze parameters vs E_C')
ax.legend(fontsize=8)

# (d) Sensitivity: delta_gap relative to canonical
ax = axes[1, 1]
delta_gaps = gap_scan - gap_at_canon  # (local)
ax.plot(E_C_range, delta_gaps, 'b-', lw=2)
ax.axvline(E_C_canonical, color='red', ls='--', lw=1.5)
ax.axhline(0.05, color='green', ls='--', lw=1, alpha=0.7, label='PASS threshold (+/- 0.05)')
ax.axhline(-0.05, color='green', ls='--', lw=1, alpha=0.7)
ax.axhline(0.20, color='orange', ls='--', lw=1, alpha=0.7, label='INFO boundary (+/- 0.20)')
ax.axhline(-0.20, color='orange', ls='--', lw=1, alpha=0.7)
ax.fill_between([E_C_minus5, E_C_plus5], -0.3, 0.3, alpha=0.1, color='red', label='+/- 5% range')
ax.set_xlabel('E_C (M_KK)')
ax.set_ylabel('delta_gap_OOM (vs canonical)')
ax.set_title('(d) Sensitivity: delta_gap vs E_C')
ax.legend(fontsize=8)
ax.set_ylim(-0.3, 0.3)

plt.tight_layout()
plt.savefig(OUT_PNG, dpi=150, bbox_inches='tight')
print(f"  Saved: {OUT_PNG}")

elapsed = time.time() - t_start  # (local)
print(f"\n  Elapsed: {elapsed:.2f} s")
print(f"\n{'='*78}")
print(f"FINAL: Gate S75-A7-EC-MAP = {verdict}")
print(f"  {verdict_msg}")
print(f"{'='*78}")
