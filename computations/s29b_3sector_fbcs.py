#!/usr/bin/env python3
"""
s29b_3sector_fbcs.py — 3-Sector BCS Free Energy Restriction + Gradient Balance

Session 29Ba computations:
  29B-1: Restrict F_BCS to permanently supercritical sectors (3,0), (0,3), (0,0).
  29B-6: Gradient balance S_b'(tau) + F_BCS^{3-sector}'(tau) = 0.

Permanently supercritical sectors (from L-9 first-order transition + LZ retraction):
  (3,0): idx=6, Peter-Weyl mult = dim_rho^2 = 100, first-order (c = 0.00552)
  (0,3): idx=7, Peter-Weyl mult = dim_rho^2 = 100, first-order (c = 0.00723)
  (0,0): idx=0, Peter-Weyl mult = dim_rho^2 = 1, always supercritical at mu = lambda_min

NOTE on (0,0) multiplicity: The s27 code (and data) uses Peter-Weyl mult=1 for the
singlet. The 16 Dirac eigenvalues are INTERNAL to the BCS gap equation; F_cond[0,:,:]
already integrates over all 16 modes. The prompt says "mult=16 (Spin(8) spinor)" which
conflates the spinor dimension with the Peter-Weyl multiplicity. We compute BOTH:
  - F_3sect_pw: using actual Peter-Weyl mult (100, 100, 1) — consistent with s27 F_total
  - F_3sect_16: using (100, 100, 16) — per prompt specification
The primary result uses Peter-Weyl multiplicities for consistency with s27/s28 data.

Gate B-29a: |F_BCS^{3-sector}| > 0.1 at minimum → PASS (stabilization by load-bearing sectors)
Gate P-29a: genuine minimum with both Hessian eigenvalues > 0 → PASS

Inputs:
  - s27_multisector_bcs.npz (F_cond, sectors, tau_values, mu_ratios, lambda_min)
  - s28b_hessian.npz (reference full-sector Hessian)
  - s24a_vspec.npz (S_b(tau) for gradient balance)

Output:
  - s29b_3sector_fbcs.npz
  - s29b_3sector_fbcs.png (3-panel diagnostic)

Author: phonon-exflation-sim agent
Date: 2026-02-28
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

# ============================================================================
# Configuration
# ============================================================================
DATA_DIR = Path(r"C:\sandbox\Ainulindale Exflation\tier0-computation")
OUT_NPZ = DATA_DIR / "s29b_3sector_fbcs.npz"
OUT_PNG = DATA_DIR / "s29b_3sector_fbcs.png"
GATE_FILE = DATA_DIR / "s29b_gate_verdicts.txt"

# 3 permanently supercritical sector indices in s27 data
SECT_IDX = [0, 6, 7]  # (0,0), (3,0), (0,3)
SECT_NAMES = ["(0,0)", "(3,0)", "(0,3)"]

# Peter-Weyl multiplicities (from s27 SECTORS: dim_rho^2)
PW_MULT = np.array([1, 100, 100])

# Prompt-specified multiplicities (prompt says 16 for singlet)
PROMPT_MULT = np.array([16, 100, 100])

# Gate thresholds
F_THRESHOLD = 0.1  # |F_3sect| must exceed this

# ============================================================================
# Load data
# ============================================================================
print("=" * 70)
print("29B-1: 3-SECTOR BCS FREE ENERGY RESTRICTION")
print("=" * 70)

# s27 multi-sector BCS
d27 = np.load(DATA_DIR / "s27_multisector_bcs.npz", allow_pickle=True)
F_cond = d27['F_cond']          # (N_sectors=9, N_tau=9, N_mu=12)
sectors = d27['sectors']         # (9, 4): p, q, dim_rho, dim_rho^2
tau_values = d27['tau_values']   # (9,)
mu_ratios = d27['mu_ratios']    # (12,)
lambda_min_all = d27['lambda_min']  # (9, 9): tau_idx x sector_idx? Need to check
F_total_full = d27['F_total']   # (N_tau=9, N_mu=12)

N_TAU = len(tau_values)
N_MU = len(mu_ratios)

print(f"Loaded s27_multisector_bcs.npz: F_cond shape = {F_cond.shape}")
print(f"tau_values = {tau_values}")
print(f"mu_ratios = {mu_ratios}")
print(f"\nTarget sectors:")
for i, (si, name) in enumerate(zip(SECT_IDX, SECT_NAMES)):
    p, q, dim_rho, mult = sectors[si]
    print(f"  {name}: idx={si}, dim_rho={dim_rho}, PW_mult={mult}, "
          f"prompt_mult={PROMPT_MULT[i]}")

# s28b Hessian (reference)
d28 = np.load(DATA_DIR / "s28b_hessian.npz", allow_pickle=True)
print(f"\nLoaded s28b_hessian.npz (reference Hessian)")

# s24a V_spec (for gradient balance)
d24 = np.load(DATA_DIR / "s24a_vspec.npz", allow_pickle=True)
tau_vspec = d24['tau']           # (21,) — finer grid than BCS tau
print(f"Loaded s24a_vspec.npz: tau grid shape = {tau_vspec.shape}")

# ============================================================================
# 29B-1: Compute F_BCS^{3-sector}
# ============================================================================
print(f"\n{'='*70}")
print("COMPUTING F_BCS^{3-sector}(tau, mu)")
print(f"{'='*70}")

# Extract F_cond for 3 sectors: shape (3, N_tau, N_mu)
F_3 = np.array([F_cond[si, :, :] for si in SECT_IDX])

# Weighted sum with Peter-Weyl multiplicities
# F_3sect_pw[tau, mu] = sum_i PW_MULT[i] * F_3[i, tau, mu]
F_3sect_pw = np.zeros((N_TAU, N_MU))
for i in range(3):
    F_3sect_pw += PW_MULT[i] * F_3[i, :, :]

# Weighted sum with prompt multiplicities (16 for singlet)
F_3sect_16 = np.zeros((N_TAU, N_MU))
for i in range(3):
    F_3sect_16 += PROMPT_MULT[i] * F_3[i, :, :]

# Report tables
for label, F_3s, mults in [("Peter-Weyl mult (1,100,100)", F_3sect_pw, PW_MULT),
                            ("Prompt mult (16,100,100)", F_3sect_16, PROMPT_MULT)]:
    print(f"\nF_3sect with {label}:")
    header = f"{'tau':>6s}"
    for ratio in mu_ratios:
        header += f"  {ratio:>8.2f}"
    print(header)
    for ti in range(N_TAU):
        row = f"{tau_values[ti]:6.2f}"
        for mi in range(N_MU):
            val = F_3s[ti, mi]
            if np.isnan(val):
                row += f"  {'NaN':>8s}"
            elif val == 0.0:
                row += f"  {'0':>8s}"
            else:
                row += f"  {val:8.3f}"
        print(row)

# Fraction of full-sector F_total at each point
print(f"\nF_3sect_pw / F_total_full (fraction of full-sector value):")
header = f"{'tau':>6s}"
for ratio in mu_ratios:
    header += f"  {ratio:>8.2f}"
print(header)
for ti in range(N_TAU):
    row = f"{tau_values[ti]:6.2f}"
    for mi in range(N_MU):
        f3 = F_3sect_pw[ti, mi]
        ft = F_total_full[ti, mi]
        if ft == 0 or np.isnan(ft) or np.isnan(f3):
            row += f"  {'---':>8s}"
        else:
            frac = f3 / ft
            row += f"  {frac:8.3f}"
    print(row)

# ============================================================================
# Locate minimum of F_3sect_pw on (tau, mu) grid
# ============================================================================
print(f"\n{'='*70}")
print("LOCATING MINIMUM OF F_BCS^{3-sector}")
print(f"{'='*70}")

# Only consider mu > 0 (mu=0 is always zero condensate)
mu_mask = mu_ratios > 0
F_search = F_3sect_pw[:, mu_mask].copy()
mu_search = mu_ratios[mu_mask]

# Find global minimum
min_val = np.nanmin(F_search)
min_pos = np.unravel_index(np.nanargmin(F_search), F_search.shape)
tau_min = tau_values[min_pos[0]]
mu_min_ratio = mu_search[min_pos[1]]
tau_min_idx = min_pos[0]
mu_min_idx_full = np.where(mu_ratios == mu_min_ratio)[0][0]

print(f"Global minimum: F_3sect = {min_val:.6f}")
print(f"  at tau = {tau_min}, mu/lambda_min = {mu_min_ratio}")
print(f"  tau_idx = {tau_min_idx}, mu_idx = {mu_min_idx_full}")

# Also find minimum for each mu value (to identify landscape)
print(f"\nMinimum per mu:")
for mi in range(N_MU):
    if mu_ratios[mi] == 0:
        continue
    F_col = F_3sect_pw[:, mi]
    valid = np.isfinite(F_col)
    if not np.any(valid):
        print(f"  mu/lmin={mu_ratios[mi]:.2f}: all NaN")
        continue
    best_ti = np.nanargmin(F_col)
    print(f"  mu/lmin={mu_ratios[mi]:.2f}: F_min={F_col[best_ti]:.6f} at tau={tau_values[best_ti]:.2f}")

# Also find interior minimum (not at boundary tau=0 or tau=0.5)
print(f"\nInterior minimum search (excluding tau boundaries):")
interior_mask = (tau_values > 0) & (tau_values < 0.5)
for mi in range(N_MU):
    if mu_ratios[mi] == 0:
        continue
    F_col = F_3sect_pw[:, mi]
    F_interior = F_col.copy()
    F_interior[~interior_mask] = np.nan
    valid = np.isfinite(F_interior)
    if not np.any(valid):
        continue
    best_ti = np.nanargmin(F_interior)
    if best_ti > 0 and best_ti < N_TAU - 1:
        # Check it's a local minimum
        if F_col[best_ti] < F_col[best_ti - 1] and F_col[best_ti] < F_col[best_ti + 1]:
            print(f"  mu/lmin={mu_ratios[mi]:.2f}: INTERIOR MIN at tau={tau_values[best_ti]:.2f}, "
                  f"F={F_col[best_ti]:.6f}")
        else:
            print(f"  mu/lmin={mu_ratios[mi]:.2f}: best interior at tau={tau_values[best_ti]:.2f}, "
                  f"F={F_col[best_ti]:.6f} (NOT a local minimum)")

# ============================================================================
# Compute 2D Hessian at the minimum
# ============================================================================
print(f"\n{'='*70}")
print("COMPUTING 2D HESSIAN AT MINIMUM")
print(f"{'='*70}")

def compute_hessian_2d(F, tau_arr, mu_arr, ti, mi):
    """
    Compute 2D Hessian of F(tau, mu) at grid point (ti, mi) via finite differences.

    Uses central differences where possible, one-sided at boundaries.
    F has shape (N_tau, N_mu).

    Returns:
        H: 2x2 Hessian matrix [[d2F/dtau2, d2F/dtaudmu], [d2F/dtaudmu, d2F/dmu2]]
        eigvals: eigenvalues of H
    """
    nt, nm = F.shape

    # d2F/dtau2
    if 0 < ti < nt - 1:
        dt = tau_arr[ti + 1] - tau_arr[ti]
        dt_m = tau_arr[ti] - tau_arr[ti - 1]
        d2F_dtau2 = 2.0 * (F[ti + 1, mi] / (dt * (dt + dt_m))
                          - F[ti, mi] / (dt * dt_m)
                          + F[ti - 1, mi] / (dt_m * (dt + dt_m)))
    elif ti == 0:
        dt = tau_arr[1] - tau_arr[0]
        dt2 = tau_arr[2] - tau_arr[0]
        d2F_dtau2 = 2.0 * (F[0, mi] * dt2 - F[1, mi] * (dt + dt2) + F[2, mi] * dt) / (dt * dt2 * (dt2 - dt))
        # Simpler: forward difference
        if nt >= 3:
            h1 = tau_arr[1] - tau_arr[0]
            h2 = tau_arr[2] - tau_arr[1]
            d2F_dtau2 = 2.0 * ((F[2, mi] - F[1, mi]) / h2 - (F[1, mi] - F[0, mi]) / h1) / (h1 + h2)
    else:  # ti == nt - 1
        h1 = tau_arr[-1] - tau_arr[-2]
        h2 = tau_arr[-2] - tau_arr[-3]
        d2F_dtau2 = 2.0 * ((F[-1, mi] - F[-2, mi]) / h1 - (F[-2, mi] - F[-3, mi]) / h2) / (h1 + h2)

    # d2F/dmu2
    # mu_ratios are not uniformly spaced; use non-uniform central diff
    if 0 < mi < nm - 1:
        hm_p = mu_arr[mi + 1] - mu_arr[mi]
        hm_m = mu_arr[mi] - mu_arr[mi - 1]
        d2F_dmu2 = 2.0 * (F[ti, mi + 1] / (hm_p * (hm_p + hm_m))
                         - F[ti, mi] / (hm_p * hm_m)
                         + F[ti, mi - 1] / (hm_m * (hm_p + hm_m)))
    elif mi == 0 and nm >= 3:
        hm1 = mu_arr[1] - mu_arr[0]
        hm2 = mu_arr[2] - mu_arr[1]
        d2F_dmu2 = 2.0 * ((F[ti, 2] - F[ti, 1]) / hm2 - (F[ti, 1] - F[ti, 0]) / hm1) / (hm1 + hm2)
    else:
        hm1 = mu_arr[-1] - mu_arr[-2]
        hm2 = mu_arr[-2] - mu_arr[-3]
        d2F_dmu2 = 2.0 * ((F[ti, -1] - F[ti, -2]) / hm1 - (F[ti, -2] - F[ti, -3]) / hm2) / (hm1 + hm2)

    # d2F/dtau*dmu (mixed partial)
    if 0 < ti < nt - 1 and 0 < mi < nm - 1:
        dt_p = tau_arr[ti + 1] - tau_arr[ti]
        dt_m = tau_arr[ti] - tau_arr[ti - 1]
        hm_p = mu_arr[mi + 1] - mu_arr[mi]
        hm_m = mu_arr[mi] - mu_arr[mi - 1]
        d2F_dtaudmu = ((F[ti + 1, mi + 1] - F[ti + 1, mi - 1]) / (hm_p + hm_m)
                      - (F[ti - 1, mi + 1] - F[ti - 1, mi - 1]) / (hm_p + hm_m)) / (dt_p + dt_m)
    else:
        d2F_dtaudmu = 0.0  # boundary fallback

    H = np.array([[d2F_dtau2, d2F_dtaudmu],
                   [d2F_dtaudmu, d2F_dmu2]])
    eigvals = np.linalg.eigvalsh(H)
    return H, eigvals

# Compute Hessian at global minimum
# Need mu in physical units for the Hessian: mu = mu_ratio * lambda_min
# But for the purpose of checking positive-definiteness, we can work in grid coordinates
# Actually, the gradient balance uses tau, so we need physical-unit Hessian

# For the grid minimum, compute Hessian in (tau, mu_ratio) space
H_min, eigvals_min = compute_hessian_2d(F_3sect_pw, tau_values, mu_ratios,
                                         tau_min_idx, mu_min_idx_full)

print(f"Hessian at global minimum (tau={tau_min}, mu/lmin={mu_min_ratio}):")
print(f"  H = [[{H_min[0,0]:.4f}, {H_min[0,1]:.4f}],")
print(f"       [{H_min[1,0]:.4f}, {H_min[1,1]:.4f}]]")
print(f"  Eigenvalues: {eigvals_min}")
genuine_min_global = np.all(eigvals_min > 0)
print(f"  Genuine minimum: {genuine_min_global}")

# Also compute Hessians at the best point for each promising mu value
print(f"\nHessian survey across mu values:")
hessian_results = {}
for mi in range(N_MU):
    if mu_ratios[mi] == 0:
        continue
    F_col = F_3sect_pw[:, mi]
    best_ti = np.nanargmin(F_col)
    F_best = F_col[best_ti]
    if F_best >= 0 or np.isnan(F_best):
        continue

    H, ev = compute_hessian_2d(F_3sect_pw, tau_values, mu_ratios, best_ti, mi)
    is_min = np.all(ev > 0)
    print(f"  mu/lmin={mu_ratios[mi]:.2f}: tau={tau_values[best_ti]:.2f}, "
          f"F={F_best:.4f}, eigvals=[{ev[0]:.2f}, {ev[1]:.2f}], "
          f"genuine={'YES' if is_min else 'NO'}")
    hessian_results[mu_ratios[mi]] = {
        'tau': tau_values[best_ti],
        'F': F_best,
        'H': H,
        'eigvals': ev,
        'genuine': is_min,
        'tau_idx': best_ti,
        'mu_idx': mi,
    }

# ============================================================================
# Gate verdict: B-29a and P-29a
# ============================================================================
print(f"\n{'='*70}")
print("GATE VERDICTS")
print(f"{'='*70}")

# Check if any (tau, mu) has |F_3sect| > threshold with genuine minimum
passes_threshold = np.abs(F_3sect_pw) > F_THRESHOLD
has_condensate = F_3sect_pw < -F_THRESHOLD

# Find the best genuine minimum
best_genuine = None
for mu_ratio, result in sorted(hessian_results.items()):
    if result['genuine'] and result['F'] < -F_THRESHOLD:
        if best_genuine is None or result['F'] < best_genuine['F']:
            best_genuine = result
            best_genuine['mu_ratio'] = mu_ratio

# Also check global minimum even if Hessian is indefinite
print(f"\nB-29a check: |F_3sect| > {F_THRESHOLD} at any (tau, mu)?")
print(f"  Global min F_3sect = {min_val:.6f} at tau={tau_min}, mu/lmin={mu_min_ratio}")
print(f"  |F_3sect| = {abs(min_val):.6f} {'>' if abs(min_val) > F_THRESHOLD else '<='} {F_THRESHOLD}")

b29a_pass = abs(min_val) > F_THRESHOLD
print(f"  B-29a: {'PASS — load-bearing sectors can stabilize' if b29a_pass else 'FAIL — 3-sector depth insufficient'}")

if best_genuine is not None:
    print(f"\nP-29a check: genuine minimum with |F| > {F_THRESHOLD}?")
    print(f"  Best genuine minimum: F={best_genuine['F']:.6f} at tau={best_genuine['tau']:.2f}, "
          f"mu/lmin={best_genuine['mu_ratio']:.2f}")
    print(f"  Hessian eigenvalues: {best_genuine['eigvals']}")
    p29a_pass = True
    print(f"  P-29a: PASS — genuine minimum confirmed")
else:
    print(f"\nP-29a check: no genuine minimum found with |F| > {F_THRESHOLD}")
    # Check if global minimum passes threshold but Hessian is indefinite
    if b29a_pass:
        print(f"  Global minimum has |F| > threshold but Hessian eigenvalues = {eigvals_min}")
        print(f"  P-29a: CONDITIONAL — depth sufficient but minimum not confirmed genuine")
        p29a_pass = False
    else:
        print(f"  P-29a: FAIL")
        p29a_pass = False

# Comparison to full-sector
print(f"\nComparison to full-sector:")
full_min = np.nanmin(F_total_full[:, mu_mask])
full_pos = np.unravel_index(np.nanargmin(F_total_full[:, mu_mask]),
                            F_total_full[:, mu_mask].shape)
print(f"  Full-sector min: F={full_min:.4f} at tau={tau_values[full_pos[0]]:.2f}, "
      f"mu/lmin={mu_search[full_pos[1]]:.2f}")
print(f"  3-sector min: F={min_val:.4f} at tau={tau_min:.2f}, mu/lmin={mu_min_ratio:.2f}")
if full_min != 0:
    print(f"  Fraction: F_3sect/F_full = {min_val/full_min:.4f}")

# ============================================================================
# 29B-6: Gradient Balance
# ============================================================================
print(f"\n{'='*70}")
print("29B-6: 3-SECTOR GRADIENT BALANCE S_b'(tau) + F_BCS^{3-sect}'(tau) = 0")
print(f"{'='*70}")

# We need S_b(tau) on the same tau grid as the BCS data.
# s24a_vspec has tau on a 21-point grid. Interpolate to the 9-point BCS grid.
# Use rho=0.1 as the primary cutoff (standard choice from sessions 24a).
V_spec = d24['V_spec_rho_0p100']  # (21,) at rho=0.1
tau_fine = d24['tau']              # (21,)

print(f"V_spec(rho=0.1) grid: {len(tau_fine)} points, tau in [{tau_fine[0]:.3f}, {tau_fine[-1]:.3f}]")

# S_b(tau) = spectral bosonic action = V_spec in the notation of the gradient balance
# Interpolate to BCS tau grid
from scipy.interpolate import interp1d
S_b_interp = interp1d(tau_fine, V_spec, kind='cubic', fill_value='extrapolate')
S_b = S_b_interp(tau_values)

print(f"S_b(tau) at BCS grid points:")
for ti in range(N_TAU):
    print(f"  tau={tau_values[ti]:.2f}: S_b={S_b[ti]:.6f}")

# For each mu with F_3sect < 0, compute gradients and find balance point
print(f"\nGradient balance at selected mu values:")

# Compute dS_b/dtau via finite differences on the BCS grid
def finite_diff_deriv(f, x):
    """Central finite differences for non-uniform grid."""
    n = len(f)
    df = np.zeros(n)
    for i in range(n):
        if i == 0:
            df[i] = (f[1] - f[0]) / (x[1] - x[0])
        elif i == n - 1:
            df[i] = (f[-1] - f[-2]) / (x[-1] - x[-2])
        else:
            h_p = x[i + 1] - x[i]
            h_m = x[i] - x[i - 1]
            df[i] = (f[i + 1] * h_m**2 + f[i] * (h_p**2 - h_m**2) - f[i - 1] * h_p**2) / (h_p * h_m * (h_p + h_m))
    return df

dSb_dtau = finite_diff_deriv(S_b, tau_values)
print(f"\ndS_b/dtau:")
for ti in range(N_TAU):
    print(f"  tau={tau_values[ti]:.2f}: dS_b/dtau = {dSb_dtau[ti]:.6f}")

gradient_balance_results = {}
mu_candidates = [mi for mi in range(N_MU) if mu_ratios[mi] > 0
                 and np.any(F_3sect_pw[:, mi] < -F_THRESHOLD)]

for mi in mu_candidates:
    mu_r = mu_ratios[mi]
    F_tau = F_3sect_pw[:, mi]
    dF_dtau = finite_diff_deriv(F_tau, tau_values)

    # Total gradient: dS_b/dtau + Lambda * dF_BCS/dtau = 0
    # => Lambda_crit = -dS_b/dtau / dF_dtau at each tau
    # We want the balance point where the ratio is O(1)

    # Also direct: find tau where dS_b/dtau + dF_dtau = 0 (Lambda=1)
    # Or more generally where they have opposite signs

    residual = dSb_dtau + dF_dtau  # balance at Lambda=1

    # Lambda_crit(tau) = -dS_b(tau) / dF(tau)
    Lambda_crit = np.where(np.abs(dF_dtau) > 1e-10,
                           -dSb_dtau / dF_dtau,
                           np.inf)

    # Find sign changes in residual (zero crossings)
    zero_crossings = []
    for ti in range(N_TAU - 1):
        if residual[ti] * residual[ti + 1] < 0:
            # Linear interpolation for crossing
            frac = residual[ti] / (residual[ti] - residual[ti + 1])
            tau_cross = tau_values[ti] + frac * (tau_values[ti + 1] - tau_values[ti])
            zero_crossings.append(tau_cross)

    print(f"\n  mu/lmin={mu_r:.2f}:")
    print(f"    dF_BCS/dtau: {dF_dtau}")
    print(f"    residual (dSb + dF): {residual}")
    print(f"    Lambda_crit: {Lambda_crit}")
    if zero_crossings:
        print(f"    Balance tau_0 (at Lambda=1): {zero_crossings}")
    else:
        print(f"    No zero crossing at Lambda=1")

    # Find tau where Lambda_crit is in [0.1, 10] (O(1))
    reasonable = (Lambda_crit > 0.1) & (Lambda_crit < 10.0) & np.isfinite(Lambda_crit)
    if np.any(reasonable):
        for ti in np.where(reasonable)[0]:
            print(f"    tau={tau_values[ti]:.2f}: Lambda_crit={Lambda_crit[ti]:.4f} (O(1))")

    gradient_balance_results[mu_r] = {
        'dF_dtau': dF_dtau,
        'Lambda_crit': Lambda_crit,
        'residual': residual,
        'zero_crossings': zero_crossings,
    }

# ============================================================================
# Summary
# ============================================================================
print(f"\n{'='*70}")
print("SUMMARY")
print(f"{'='*70}")

print(f"\n29B-1 Results:")
print(f"  F_BCS^{{3-sector}} global minimum = {min_val:.6f}")
print(f"    at tau = {tau_min}, mu/lambda_min = {mu_min_ratio}")
print(f"  Hessian at minimum: eigenvalues = [{eigvals_min[0]:.4f}, {eigvals_min[1]:.4f}]")
print(f"  Genuine minimum: {genuine_min_global}")
if best_genuine is not None:
    print(f"  Best GENUINE minimum: F={best_genuine['F']:.6f} at tau={best_genuine['tau']:.2f}, "
          f"mu/lmin={best_genuine['mu_ratio']:.2f}")
print(f"  Fraction of full-sector: {min_val/full_min:.4f}" if full_min != 0 else "")

print(f"\n29B-6 Results:")
for mu_r, gr in sorted(gradient_balance_results.items()):
    lc = gr['Lambda_crit']
    reasonable = (lc > 0.1) & (lc < 10.0) & np.isfinite(lc)
    if np.any(reasonable):
        for ti in np.where(reasonable)[0]:
            print(f"  mu/lmin={mu_r:.2f}: tau_0={tau_values[ti]:.2f}, Lambda_crit={lc[ti]:.4f}")

print(f"\nGate Verdicts:")
print(f"  B-29a: {'PASS' if b29a_pass else 'FAIL'}")
print(f"  P-29a: {'PASS' if p29a_pass else 'CONDITIONAL' if b29a_pass else 'FAIL'}")

# ============================================================================
# Save outputs
# ============================================================================
print(f"\nSaving to {OUT_NPZ}")

save_dict = {
    # 29B-1: 3-sector F_BCS
    'F_3sect_pw': F_3sect_pw,
    'F_3sect_16': F_3sect_16,
    'tau_values': tau_values,
    'mu_ratios': mu_ratios,
    'sector_indices': np.array(SECT_IDX),
    'pw_multiplicities': PW_MULT,
    'prompt_multiplicities': PROMPT_MULT,
    'global_min_F': np.float64(min_val),
    'global_min_tau': np.float64(tau_min),
    'global_min_mu_ratio': np.float64(mu_min_ratio),
    'H_min': H_min,
    'eigvals_min': eigvals_min,
    'genuine_min_global': np.bool_(genuine_min_global),
    # Full-sector comparison
    'full_min_F': np.float64(full_min),
    'fraction_of_full': np.float64(min_val / full_min) if full_min != 0 else np.float64(np.nan),
    # 29B-6: Gradient balance
    'S_b': S_b,
    'dSb_dtau': dSb_dtau,
    # Gate verdicts
    'B_29a': np.bool_(b29a_pass),
    'P_29a': np.bool_(p29a_pass),
}

# Add Hessian survey
for mu_r, result in hessian_results.items():
    key = f"H_mu{mu_r:.2f}".replace('.', 'p')
    save_dict[f'{key}_H'] = result['H']
    save_dict[f'{key}_eigvals'] = result['eigvals']
    save_dict[f'{key}_F'] = np.float64(result['F'])
    save_dict[f'{key}_tau'] = np.float64(result['tau'])
    save_dict[f'{key}_genuine'] = np.bool_(result['genuine'])

# Add gradient balance per mu
for mu_r, gr in gradient_balance_results.items():
    key = f"grad_mu{mu_r:.2f}".replace('.', 'p')
    save_dict[f'{key}_dF'] = gr['dF_dtau']
    save_dict[f'{key}_Lambda_crit'] = gr['Lambda_crit']
    save_dict[f'{key}_residual'] = gr['residual']

np.savez_compressed(OUT_NPZ, **save_dict)
print(f"Saved {OUT_NPZ.name}")

# ============================================================================
# Plot
# ============================================================================
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Panel 1: F_3sect_pw vs tau for selected mu values
ax = axes[0]
for mi in [5, 7, 8, 9, 10]:  # mu = 1.0, 1.1, 1.2, 1.5, 2.0
    if mi < N_MU:
        F_tau = F_3sect_pw[:, mi]
        valid = np.isfinite(F_tau) & (F_tau != 0)
        if np.any(valid):
            ax.plot(tau_values[valid], F_tau[valid], 'o-',
                    label=f'mu/lmin={mu_ratios[mi]:.2f}')
ax.axhline(-F_THRESHOLD, color='red', linestyle='--', alpha=0.5, label=f'threshold = -{F_THRESHOLD}')
ax.set_xlabel('tau')
ax.set_ylabel('F_BCS^{3-sector}')
ax.set_title('29B-1: 3-Sector BCS Free Energy')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 2: Fraction F_3sect/F_full
ax = axes[1]
for mi in [5, 7, 8, 9, 10]:
    if mi < N_MU:
        f3 = F_3sect_pw[:, mi]
        ff = F_total_full[:, mi]
        frac = np.where((ff != 0) & np.isfinite(ff) & np.isfinite(f3), f3 / ff, np.nan)
        valid = np.isfinite(frac)
        if np.any(valid):
            ax.plot(tau_values[valid], frac[valid], 'o-',
                    label=f'mu/lmin={mu_ratios[mi]:.2f}')
ax.axhline(1.0, color='gray', linestyle=':', alpha=0.5)
ax.axhline(0.5, color='red', linestyle='--', alpha=0.5, label='50%')
ax.set_xlabel('tau')
ax.set_ylabel('F_3sect / F_full')
ax.set_title('3-Sector Fraction of Full-Sector')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 3: Gradient balance
ax = axes[2]
ax.plot(tau_values, dSb_dtau, 'k-o', label="dS_b/dtau", linewidth=2)
for mu_r, gr in sorted(gradient_balance_results.items()):
    if mu_r in [1.0, 1.1, 1.2, 1.5]:
        ax.plot(tau_values, -gr['dF_dtau'], 's--',
                label=f'-dF_3sect/dtau (mu/lmin={mu_r:.1f})', markersize=4)
ax.set_xlabel('tau')
ax.set_ylabel('Gradient')
ax.set_title('29B-6: Gradient Balance')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(OUT_PNG, dpi=150, bbox_inches='tight')
print(f"Saved {OUT_PNG.name}")

# ============================================================================
# Write gate verdicts
# ============================================================================
verdict_lines = [
    "\n--- 29B-1: 3-Sector F_BCS ---",
    f"B-29a: {'PASS' if b29a_pass else 'FAIL'}",
    f"  F_3sect global min = {min_val:.6f} at tau={tau_min}, mu/lmin={mu_min_ratio}",
    f"  Threshold = {F_THRESHOLD}",
    f"  Hessian eigenvalues = [{eigvals_min[0]:.4f}, {eigvals_min[1]:.4f}]",
    f"  Genuine minimum: {genuine_min_global}",
]
if best_genuine is not None:
    verdict_lines.append(
        f"P-29a: PASS (best genuine min F={best_genuine['F']:.6f} at "
        f"tau={best_genuine['tau']:.2f}, mu/lmin={best_genuine['mu_ratio']:.2f})")
else:
    verdict_lines.append(f"P-29a: {'CONDITIONAL' if b29a_pass else 'FAIL'}")

verdict_lines.append(f"  F_3sect/F_full at global min = {min_val/full_min:.4f}" if full_min != 0 else "")

verdict_lines.append("\n--- 29B-6: Gradient Balance ---")
found_balance = False
for mu_r, gr in sorted(gradient_balance_results.items()):
    lc = gr['Lambda_crit']
    reasonable = (lc > 0.1) & (lc < 10.0) & np.isfinite(lc)
    if np.any(reasonable):
        for ti in np.where(reasonable)[0]:
            verdict_lines.append(
                f"  Balance at mu/lmin={mu_r:.2f}: tau_0={tau_values[ti]:.2f}, "
                f"Lambda_crit={lc[ti]:.4f}")
            found_balance = True
if not found_balance:
    verdict_lines.append("  No gradient balance with Lambda_crit = O(1)")

with open(GATE_FILE, 'a') as f:
    for line in verdict_lines:
        f.write(line + "\n")
print(f"Appended gate verdicts to {GATE_FILE.name}")

print(f"\n{'='*70}")
print("DONE")
print(f"{'='*70}")
