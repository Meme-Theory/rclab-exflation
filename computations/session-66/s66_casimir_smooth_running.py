#!/usr/bin/env python3
"""
CASIMIR-SMOOTH-RUNNING-66 (W4-F) -- Alpha_s with Casimir-Averaged Smoothing
=============================================================================

W3-A found alpha_s = -0.038, persisting at 5.0 sigma from Planck (-0.0045 +/- 0.0067),
with negligible change from L_max=3 to L_max=4.

Hypothesis: The spectral action is a sum over Peter-Weyl sectors labeled by
Casimir eigenvalue C_2(p,q). The "wavenumber" on the fiber is k_{(p,q)} = sqrt(C_2(p,q)),
which forms a DISCRETE lattice, not a continuum. The running alpha_s = dn_s/d(ln k)
is a finite-difference derivative over this discrete Casimir ladder.
If we smooth in Casimir space with a Gaussian kernel, the effective derivatives
may decrease, reducing the tension with Planck.

Method:
-------
1. Load the D_K eigenvalues from S36 (L_max=3) and W3-A (L_max=4 new sectors).
2. Compute S_{(p,q)}(tau) = dim(p,q)^2 * sum_j |lambda_j^{(p,q)}(tau)| for each sector.
3. Assign k_{(p,q)} = sqrt(C_2(p,q)) to each sector.
4. For each Gaussian width sigma_C, compute the smoothed spectral action:
     S_smooth(tau) = sum_{(p,q)} w_{(p,q)}(sigma_C) * S_{(p,q)}(tau)
   where w_{(p,q)} is a Gaussian weight that redistributes spectral weight.
5. Compute eps_H and alpha_s from S_smooth.
6. Scan sigma_C from minimal (C_2(1,0) = 4/3) to maximal (all sectors equal weight).

Gate: CASIMIR-SMOOTH-RUNNING-66
  PASS: |alpha_s^{smoothed}| < 0.015 for sigma_C >= C_2(1,0)
  FAIL: |alpha_s^{smoothed}| > 0.030 even at maximal smoothing
  INFO: 0.015 < |alpha_s^{smoothed}| < 0.030 (partial improvement)

Agent: gen-physicist (Session 66, Wave 4)
"""

import numpy as np
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVE_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), 'computations/_shared')
sys.path.insert(0, SCRIPT_DIR)
sys.path.insert(0, ARCHIVE_DIR)

os.chdir(SCRIPT_DIR)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from scipy.interpolate import CubicSpline

from canonical_constants import (
    tau_fold, Delta_0_OES, G_DeWitt, PI
)

# =============================================================================
# CONFIGURATION
# =============================================================================
print("=" * 78)
print("CASIMIR-SMOOTH-RUNNING-66 (W4-F): Alpha_s with Casimir-Averaged Smoothing")
print("=" * 78)

Delta = Delta_0_OES   # 0.464 M_KK (BCS gap)
G = G_DeWitt          # 5.0 (DeWitt moduli kinetic coefficient)
tau_f = tau_fold       # 0.19
planck_alpha_s = -0.0045  # (local)
planck_alpha_s_sigma = 0.0067  # (local)

print(f"\n  tau_fold        = {tau_f}")
print(f"  Delta (BCS)     = {Delta:.6f} M_KK")
print(f"  G_DeWitt        = {G:.1f}")
print(f"  Planck alpha_s  = {planck_alpha_s} +/- {planck_alpha_s_sigma}")

# =============================================================================
# STEP 0: LOAD EIGENVALUES FROM S36 (L<=3) AND W3-A (L=4 NEW)
# =============================================================================
print("\n" + "=" * 78)
print("STEP 0: Load Eigenvalues")
print("=" * 78)

# Load S36 archive
d_s36 = np.load(os.path.join(ARCHIVE_DIR, 's36_sfull_tau_stabilization.npz'),
                allow_pickle=True)

# Load W3-A data (contains L4 eigenvalues)
d_w3a = np.load(os.path.join(SCRIPT_DIR, 's66_running_ns.npz'), allow_pickle=True)

tau_evals = np.array([0.05, 0.16, 0.17, 0.18, 0.19, 0.21, 0.22])


def su3_dim(p, q):
    """Dimension of SU(3) irrep (p,q)."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def casimir_su3(p, q):
    """Quadratic Casimir C_2(p,q) for SU(3) irrep (p,q).
    C_2 = (p^2 + pq + q^2 + 3p + 3q) / 3
    Convention: generators normalized so C_2(1,0) = 4/3 (fundamental).
    """
    return (p**2 + p*q + q**2 + 3*p + 3*q) / 3.0


# Build sector list for L_max = 4
sectors_L3 = []
for p in range(4):
    for q in range(4):
        if p + q <= 3:
            sectors_L3.append((p, q))

sectors_L4_new = []
for p in range(5):
    for q in range(5):
        if p + q == 4:
            sectors_L4_new.append((p, q))

sectors_all = sectors_L3 + sectors_L4_new

print(f"\n  L_max=3 sectors:  {len(sectors_L3)} -> {sectors_L3}")
print(f"  L_max=4 new:      {len(sectors_L4_new)} -> {sectors_L4_new}")
print(f"  Total sectors:    {len(sectors_all)}")

# Print Casimir values
print(f"\n  Casimir eigenvalues C_2(p,q):")
for (p, q) in sectors_all:
    c2 = casimir_su3(p, q)
    k_pq = np.sqrt(c2)
    d = su3_dim(p, q)
    print(f"    ({p},{q}): C_2 = {c2:.4f}, k = sqrt(C_2) = {k_pq:.4f}, "
          f"dim = {d}, weight dim^2 = {d**2}")

# =============================================================================
# STEP 1: COMPUTE PER-SECTOR SPECTRAL ACTION S_{(p,q)}(tau)
# =============================================================================
print("\n" + "=" * 78)
print("STEP 1: Per-Sector Spectral Action S_{(p,q)}(tau)")
print("=" * 78)

print("""
  S_{(p,q)}(tau) = dim(p,q)^2 * sum_j |lambda_j^{(p,q)}(tau)|
  BCS-dressed: S_{(p,q)}^BCS(tau) = dim(p,q)^2 * sum_j sqrt(|lambda_j|^2 + Delta^2)
  One-loop:    S_{(p,q)}^1L(tau) = (1/2) * dim(p,q) * sum_j log(|lambda_j|^2 + Delta^2)
""")

# sector_S_bcs[i][(p,q)] = BCS effective spectral action for sector (p,q) at tau_evals[i]
sector_S_eff = {}  # effective = tree BCS + 1-loop BCS

for i, tau in enumerate(tau_evals):
    # L_max = 3 sectors from S36
    for (p, q) in sectors_L3:
        key_s36 = f'evals_tau{tau:.3f}_{p}_{q}'
        if key_s36 not in d_s36:
            print(f"  WARNING: {key_s36} not found in S36 archive")
            sector_S_eff[(i, p, q)] = 0.0
            continue

        evals = d_s36[key_s36]
        dim_pq = su3_dim(p, q)
        pw_tree = dim_pq ** 2
        pw_1loop = dim_pq

        omega = np.abs(evals)
        omega_sq = omega ** 2
        E_bdg = np.sqrt(omega_sq + Delta ** 2)

        S_tree = pw_tree * np.sum(E_bdg)
        S_1loop = 0.5 * pw_1loop * np.sum(np.log(omega_sq + Delta ** 2))

        sector_S_eff[(i, p, q)] = S_tree + S_1loop

    # L_max = 4 new sectors from W3-A
    for (p, q) in sectors_L4_new:
        key_w3a = f'evals_L4_tau{tau:.3f}_{p}_{q}'
        if key_w3a not in d_w3a:
            print(f"  WARNING: {key_w3a} not found in W3-A data")
            sector_S_eff[(i, p, q)] = 0.0
            continue

        evals = d_w3a[key_w3a]
        dim_pq = su3_dim(p, q)
        pw_tree = dim_pq ** 2
        pw_1loop = dim_pq

        omega = np.abs(evals)  # complex -> magnitude
        omega_sq = omega ** 2
        E_bdg = np.sqrt(omega_sq + Delta ** 2)

        S_tree = pw_tree * np.sum(E_bdg)
        S_1loop = 0.5 * pw_1loop * np.sum(np.log(omega_sq + Delta ** 2))

        sector_S_eff[(i, p, q)] = S_tree + S_1loop

# Verify total matches W3-A
S_total_check = np.zeros(len(tau_evals))
for i in range(len(tau_evals)):
    for (p, q) in sectors_all:
        S_total_check[i] += sector_S_eff[(i, p, q)]

S_eff_bcs_L4_ref = d_w3a['S_eff_bcs_L4']
print(f"\n  Cross-check: S_total vs W3-A S_eff_bcs_L4 at fold:")
idx_fold = np.argmin(np.abs(tau_evals - 0.19))
dev = abs(S_total_check[idx_fold] - S_eff_bcs_L4_ref[idx_fold]) / S_eff_bcs_L4_ref[idx_fold]
print(f"    S_total(fold)     = {S_total_check[idx_fold]:.2f}")
print(f"    W3-A S_eff(fold)  = {S_eff_bcs_L4_ref[idx_fold]:.2f}")
print(f"    Fractional dev    = {dev:.2e}")
assert dev < 1e-8, f"Cross-check FAILED: dev = {dev:.2e}"
print(f"    PASS (dev < 1e-8)")

# Print sector contributions at fold
print(f"\n  Sector contributions at fold (tau = {tau_evals[idx_fold]:.2f}):")
print(f"  {'(p,q)':>6s}  {'C_2':>8s}  {'k=sqrt(C2)':>10s}  {'S_eff':>14s}  {'frac':>8s}")
for (p, q) in sectors_all:
    c2 = casimir_su3(p, q)
    k_pq = np.sqrt(c2)
    s_pq = sector_S_eff[(idx_fold, p, q)]
    frac = s_pq / S_total_check[idx_fold]
    print(f"  ({p},{q}):  {c2:8.4f}  {k_pq:10.4f}  {s_pq:14.2f}  {frac:8.4f}")


# =============================================================================
# STEP 2: DEFINE CASIMIR SMOOTHING
# =============================================================================
print("\n" + "=" * 78)
print("STEP 2: Casimir Smoothing Methodology")
print("=" * 78)

print("""
  The spectral action S(tau) = sum_{(p,q)} S_{(p,q)}(tau) can be rewritten as:

    S(tau) = sum_{(p,q)} S_{(p,q)}(tau)

  Each sector has fiber wavenumber k_{(p,q)} = sqrt(C_2(p,q)).
  The hypothesis is that the physical CMB wavenumber maps to a SMOOTH function
  of the fiber wavenumber, so the correct derivative dn_s/d(ln k_phys) should
  use a smoothed version of S(tau):

    S_smooth(tau; sigma) = sum_{(p,q)} w_{(p,q)}(sigma) * S_{(p,q)}(tau)

  where w_{(p,q)} is the row-normalized Gaussian kernel:

    K_{(p,q),(r,s)} = exp(-(C_2(p,q) - C_2(r,s))^2 / (2 sigma^2))
    w_{(p,q)}(sigma) = sum_{(r,s)} K_{(p,q),(r,s)} * S_{(r,s)} / S_total

  This preserves S_total (the weights sum to 1) while redistributing
  sector contributions.

  PHYSICAL ARGUMENT: Sectors with nearby Casimir values have similar
  representation-theoretic content and hence similar eigenvalue spectra.
  The discrete jump between adjacent sectors is an artifact of the Peter-Weyl
  decomposition at finite L_max, not a physical feature.

  ALTERNATIVE INTERPRETATION: We directly smooth the sector-resolved S(tau)
  as a function of C_2, then sum. This avoids modifying individual sectors.
""")

# Casimir values and fiber wavenumbers for each sector
sector_C2 = {}
sector_k = {}
for (p, q) in sectors_all:
    sector_C2[(p, q)] = casimir_su3(p, q)
    sector_k[(p, q)] = np.sqrt(casimir_su3(p, q))

# Sort sectors by Casimir value
sectors_sorted = sorted(sectors_all, key=lambda pq: sector_C2[pq])
C2_values = np.array([sector_C2[pq] for pq in sectors_sorted])
k_values = np.array([sector_k[pq] for pq in sectors_sorted])

print(f"\n  Sectors sorted by C_2:")
print(f"  {'(p,q)':>6s}  {'C_2':>8s}  {'k':>8s}")
for pq in sectors_sorted:
    if pq == (0,0):
        print(f"  ({pq[0]},{pq[1]}):  {sector_C2[pq]:8.4f}  {sector_k[pq]:8.4f}  <- trivial rep (k=0)")
    else:
        print(f"  ({pq[0]},{pq[1]}):  {sector_C2[pq]:8.4f}  {sector_k[pq]:8.4f}")

# Unique Casimir values (some sectors are conjugates with same C_2)
C2_unique = np.unique(np.round(C2_values, 8))
print(f"\n  Unique C_2 values: {len(C2_unique)}")
print(f"  {C2_unique}")

# Minimal Casimir step
C2_sorted = np.sort(C2_unique)
C2_steps = np.diff(C2_sorted[C2_sorted > 0])  # exclude trivial (0,0) sector
print(f"\n  C_2 steps (excluding trivial): {C2_steps}")
C2_min_step = C2_steps[0] if len(C2_steps) > 0 else 1.0
print(f"  Minimal Casimir step: {C2_min_step:.4f}")
print(f"  C_2(1,0) = {casimir_su3(1,0):.4f} (fundamental)")
print(f"  C_2(1,1) = {casimir_su3(1,1):.4f} (adjoint)")


# =============================================================================
# STEP 3: COMPUTE SMOOTHED SPECTRAL ACTIONS
# =============================================================================
print("\n" + "=" * 78)
print("STEP 3: Compute Smoothed Spectral Actions for Scan of sigma_C")
print("=" * 78)

# Define smoothing widths to scan
sigma_values = np.array([
    0.0,                      # No smoothing (raw)
    casimir_su3(1, 0) / 2,    # Half the fundamental Casimir
    casimir_su3(1, 0),        # = 4/3, minimal Casimir step
    2.0,                      # Intermediate
    casimir_su3(1, 1),        # = 4, adjoint Casimir
    6.0,                      # Large
    casimir_su3(2, 1),        # = 10/3 ~ 3.33, next step
    8.0,                      # Larger
    12.0,                     # Very large
    20.0,                     # Near-uniform
    50.0,                     # Effectively uniform
    100.0,                    # Limit
])
sigma_values = np.sort(np.unique(sigma_values))

print(f"  Scanning {len(sigma_values)} sigma_C values: {sigma_values}")

# Build the Gaussian smoothing kernel for each sigma
# The smoothed action at each tau is:
#   S_smooth(tau; sigma) = sum_{(p,q)} [sum_{(r,s)} G(C2_pq - C2_rs; sigma) * S_{(r,s)}(tau)]
#                        / [sum_{(r,s)} G(C2_pq - C2_rs; sigma)]
# Then S_smooth_total = sum_{(p,q)} S_smooth_{(p,q)}
#
# But this doesn't change the total -- each sector gets redistributed but the sum is preserved.
# So the smoothed total = unsmoothed total. That means this approach can't change alpha_s!
#
# CORRECT APPROACH: Smoothing means we replace the per-sector contribution
# by a smoothed version before computing the total and its derivatives.
# The physical question is: does the spectral action "know" about the discrete
# Casimir labels, or does it only depend on C_2 as a smooth parameter?
#
# Formally: let f(C_2) be the spectral weight per unit Casimir (the "density").
# The discrete sum S = sum_a f(C_2^a) * delta_C_2^a can be replaced by
# a convolved version: S_smooth = sum_a [G * f](C_2^a) * delta_C_2^a.
#
# This is equivalent to: for each sector a, replace S_a(tau) by
#   S_a^smooth(tau) = sum_b G_{ab}(sigma) * S_b(tau)
# where G_{ab} = exp(-(C2_a - C2_b)^2 / (2 sigma^2)), then NORMALIZE each row.
# The smoothed total is S_smooth_total = sum_a S_a^smooth.
#
# CRITICAL: After row normalization, S_smooth_total != S_total in general!
# Each sector's contribution gets replaced by a weighted average of nearby sectors.
# This IS physically meaningful: it smooths the tau-derivatives.

N_sec = len(sectors_sorted)

# Precompute the Casimir distance matrix
C2_arr = np.array([sector_C2[pq] for pq in sectors_sorted])
C2_dist = np.abs(C2_arr[:, None] - C2_arr[None, :])

# Storage for smoothed spectral actions
S_smoothed = {}  # S_smoothed[sigma_idx] = array of shape (len(tau_evals),)

for sigma_idx, sigma in enumerate(sigma_values):
    if sigma < 1e-10:
        # No smoothing: identity kernel
        kernel = np.eye(N_sec)
    else:
        kernel = np.exp(-C2_dist**2 / (2.0 * sigma**2))

    # Row-normalize
    row_sums = kernel.sum(axis=1)
    kernel_norm = kernel / row_sums[:, None]

    # Compute smoothed total at each tau
    S_sm = np.zeros(len(tau_evals))
    for i in range(len(tau_evals)):
        # Per-sector contributions at this tau
        S_sectors = np.array([sector_S_eff[(i, pq[0], pq[1])] for pq in sectors_sorted])

        # Apply smoothing kernel
        S_sectors_smooth = kernel_norm @ S_sectors

        # Total smoothed action
        S_sm[i] = np.sum(S_sectors_smooth)

    S_smoothed[sigma_idx] = S_sm

# Verify sigma=0 matches raw total
dev_raw = np.max(np.abs(S_smoothed[0] - S_total_check) / S_total_check)
print(f"\n  Cross-check: sigma=0 vs raw total, max fractional dev = {dev_raw:.2e}")
assert dev_raw < 1e-12, f"sigma=0 should reproduce raw total, got dev = {dev_raw:.2e}"
print(f"  PASS")

# Print smoothed values at fold
print(f"\n  Smoothed S(fold) for each sigma_C:")
print(f"  {'sigma_C':>10s}  {'S_smooth(fold)':>16s}  {'delta_S/S':>12s}")
for sigma_idx, sigma in enumerate(sigma_values):
    s_sm = S_smoothed[sigma_idx][idx_fold]
    delta = (s_sm - S_total_check[idx_fold]) / S_total_check[idx_fold]
    print(f"  {sigma:10.4f}  {s_sm:16.2f}  {delta:+12.6f}")


# =============================================================================
# STEP 4: COMPUTE eps_H AND alpha_s FOR EACH SMOOTHING WIDTH
# =============================================================================
print("\n" + "=" * 78)
print("STEP 4: Slow-Roll Parameters and Running for Each Smoothing Width")
print("=" * 78)

print("""
  For each sigma_C:
  1. Fit cubic spline to S_smooth(tau) using near-fold points (tau >= 0.16)
  2. Compute eps_H = (1/2) * (S'/S)^2 / G at the fold
  3. Compute alpha_s = -2 * d(eps_H)/dtau * dtau/d(ln k) at the fold
     with dtau/d(ln k) = eps_H / (d(ln S)/dtau)
""")

idx_near = np.arange(1, len(tau_evals))  # tau = 0.16..0.22 (skip 0.05)
tau_near = tau_evals[idx_near]
dtau = 0.001  # numerical derivative stencil

results = {}

for sigma_idx, sigma in enumerate(sigma_values):
    S_arr = S_smoothed[sigma_idx][idx_near]

    # Cubic spline
    cs = CubicSpline(tau_near, S_arr)
    S_val = float(cs(tau_f))
    dS_val = float(cs(tau_f, 1))
    d2S_val = float(cs(tau_f, 2))

    # Hubble slow-roll
    if d2S_val > 0 and S_val > 0:
        eps_H = 0.5 * dS_val ** 2 / (S_val * d2S_val)
    else:
        eps_H = np.inf

    # Potential slow-roll
    eps_V = 0.5 * (dS_val / S_val) ** 2 / G
    eta_V = d2S_val / (S_val * G)
    eta_H = eta_V / (1.0 - eps_V / 3.0)
    ns = 1.0 - 2.0 * eps_H - eta_H

    # Running: d(eps_H)/dtau by central difference
    def eps_at_tau(t):
        S_t = float(cs(t))
        dS_t = float(cs(t, 1))
        d2S_t = float(cs(t, 2))
        if d2S_t > 0 and S_t > 0:
            return 0.5 * dS_t ** 2 / (S_t * d2S_t)
        return np.nan

    eps_plus = eps_at_tau(tau_f + dtau)
    eps_minus = eps_at_tau(tau_f - dtau)
    deps_dtau = (eps_plus - eps_minus) / (2 * dtau)

    # dtau/d(ln k)
    dln_S_dtau = dS_val / S_val
    dtau_dlnk = eps_H / dln_S_dtau if dln_S_dtau > 0 else 0.0

    # Running
    alpha_s = -2.0 * deps_dtau * dtau_dlnk

    results[sigma_idx] = {
        'sigma': sigma,
        'S': S_val, 'dS': dS_val, 'd2S': d2S_val,
        'eps_H': eps_H, 'eta_H': eta_H, 'ns': ns,
        'deps_dtau': deps_dtau, 'dtau_dlnk': dtau_dlnk,
        'alpha_s': alpha_s,
    }

# Print results table
print(f"\n  {'sigma_C':>8s}  {'eps_H':>10s}  {'n_s':>10s}  {'alpha_s':>12s}  "
      f"{'|alpha_s|':>10s}  {'Planck sigma':>12s}")
print(f"  {'-'*8}  {'-'*10}  {'-'*10}  {'-'*12}  {'-'*10}  {'-'*12}")
for sigma_idx, sigma in enumerate(sigma_values):
    r = results[sigma_idx]
    tension = abs(r['alpha_s'] - planck_alpha_s) / planck_alpha_s_sigma
    print(f"  {sigma:8.3f}  {r['eps_H']:10.6f}  {r['ns']:10.6f}  "
          f"{r['alpha_s']:12.6e}  {abs(r['alpha_s']):10.6f}  {tension:12.1f}")


# =============================================================================
# STEP 5: ANALYZE THE SMOOTHING MECHANISM
# =============================================================================
print("\n" + "=" * 78)
print("STEP 5: Analysis of Smoothing Mechanism")
print("=" * 78)

alpha_raw = results[0]['alpha_s']
print(f"\n  Raw alpha_s (sigma=0): {alpha_raw:.6e}")
print(f"  |alpha_s(raw)| = {abs(alpha_raw):.6f}")

# Find minimum |alpha_s|
min_abs_alpha = np.inf
min_sigma_idx = 0
for sigma_idx in range(len(sigma_values)):
    a = abs(results[sigma_idx]['alpha_s'])
    if a < min_abs_alpha:
        min_abs_alpha = a
        min_sigma_idx = sigma_idx

print(f"\n  Minimum |alpha_s| = {min_abs_alpha:.6f} at sigma_C = {sigma_values[min_sigma_idx]:.4f}")
print(f"  Reduction ratio: {min_abs_alpha / abs(alpha_raw):.4f}")

# Check whether the smoothing changes the DERIVATIVES or just the VALUES
print(f"\n  Derivative diagnostics at fold:")
for sigma_idx, sigma in enumerate(sigma_values):
    r = results[sigma_idx]
    dlnS = r['dS'] / r['S']
    d2lnS = r['d2S'] / r['S'] - (r['dS'] / r['S'])**2
    print(f"    sigma={sigma:8.3f}: d(ln S)/dtau = {dlnS:.6f}, "
          f"d^2(ln S)/dtau^2 = {d2lnS:.6f}, "
          f"eps_H = {r['eps_H']:.6f}")

# Understand why: the running comes from deps_dtau.
# If all sectors have the SAME eps_H profile, smoothing changes nothing.
# Running is large when different sectors have DIFFERENT curvature profiles.
print(f"\n  Per-sector eps_H analysis (without smoothing):")
for pq in sectors_sorted:
    if pq == (0, 0):
        continue  # Skip trivial rep
    S_sec = np.array([sector_S_eff[(i, pq[0], pq[1])] for i in range(len(tau_evals))])
    S_sec_near = S_sec[idx_near]
    if np.all(S_sec_near > 0):
        cs_sec = CubicSpline(tau_near, S_sec_near)
        S_v = float(cs_sec(tau_f))
        dS_v = float(cs_sec(tau_f, 1))
        d2S_v = float(cs_sec(tau_f, 2))
        if d2S_v > 0 and S_v > 0:
            eps_sec = 0.5 * dS_v**2 / (S_v * d2S_v)
            dlnS_sec = dS_v / S_v
            print(f"    ({pq[0]},{pq[1]}): C_2={sector_C2[pq]:.4f}, "
                  f"S(fold)={S_v:.2f}, d(ln S)/dtau={dlnS_sec:.4f}, "
                  f"eps_H_sector={eps_sec:.6f}")


# =============================================================================
# STEP 6: GATE VERDICT
# =============================================================================
print("\n" + "=" * 78)
print("STEP 6: GATE VERDICT -- CASIMIR-SMOOTH-RUNNING-66")
print("=" * 78)

# The gate threshold is on alpha_s at sigma_C >= C_2(1,0) = 4/3
sigma_threshold = casimir_su3(1, 0)  # = 4/3
print(f"\n  Gate threshold sigma_C >= C_2(1,0) = {sigma_threshold:.4f}")

# Find alpha_s at sigma = C_2(1,0)
idx_gate = None
for sigma_idx, sigma in enumerate(sigma_values):
    if abs(sigma - sigma_threshold) < 1e-8:
        idx_gate = sigma_idx
        break

if idx_gate is None:
    # Find nearest sigma >= threshold
    for sigma_idx, sigma in enumerate(sigma_values):
        if sigma >= sigma_threshold - 1e-8:
            idx_gate = sigma_idx
            break

alpha_s_gate = results[idx_gate]['alpha_s']
alpha_s_maxsmooth = results[len(sigma_values) - 1]['alpha_s']

print(f"  alpha_s at sigma_C = {sigma_values[idx_gate]:.4f}: {alpha_s_gate:.6e}")
print(f"  |alpha_s| at gate sigma: {abs(alpha_s_gate):.6f}")
print(f"  alpha_s at max smoothing: {alpha_s_maxsmooth:.6e}")
print(f"  |alpha_s| at max smoothing: {abs(alpha_s_maxsmooth):.6f}")

# Determine verdict
# PASS: |alpha_s^{smoothed}| < 0.015 for sigma_C >= C_2(1,0)
# FAIL: |alpha_s^{smoothed}| > 0.030 even at maximal smoothing
# INFO: 0.015 < |alpha_s^{smoothed}| < 0.030

# Check all sigma >= threshold
pass_any = False
fail_all_above_030 = True
alpha_s_at_threshold_sigmas = []

for sigma_idx, sigma in enumerate(sigma_values):
    if sigma >= sigma_threshold - 1e-8:
        a = abs(results[sigma_idx]['alpha_s'])
        alpha_s_at_threshold_sigmas.append((sigma, a))
        if a < 0.015:
            pass_any = True
        if a <= 0.030:
            fail_all_above_030 = False

# For the gate, use maximal smoothing as the decisive value
alpha_s_decisive = abs(alpha_s_maxsmooth)

if alpha_s_decisive < 0.015:
    verdict = "PASS"
    detail = (f"|alpha_s(sigma_C={sigma_values[-1]:.1f})| = {alpha_s_decisive:.6f} < 0.015 "
              f"(Casimir smoothing resolves the tension)")
elif alpha_s_decisive > 0.030:
    verdict = "FAIL"
    detail = (f"|alpha_s(sigma_C={sigma_values[-1]:.1f})| = {alpha_s_decisive:.6f} > 0.030 "
              f"(running is intrinsic, not a Casimir discreteness artifact)")
else:
    verdict = "INFO"
    detail = (f"|alpha_s(sigma_C={sigma_values[-1]:.1f})| = {alpha_s_decisive:.6f} in [0.015, 0.030] "
              f"(partial improvement from smoothing)")

print(f"\n  GATE: CASIMIR-SMOOTH-RUNNING-66")
print(f"  CRITERION:")
print(f"    PASS: |alpha_s^{{smoothed}}| < 0.015 for sigma_C >= C_2(1,0) = {sigma_threshold:.4f}")
print(f"    FAIL: |alpha_s^{{smoothed}}| > 0.030 even at maximal smoothing")
print(f"    INFO: 0.015 < |alpha_s^{{smoothed}}| < 0.030")
print(f"")
print(f"  COMPUTED:")
print(f"    |alpha_s(raw)|          = {abs(alpha_raw):.6f}")
print(f"    |alpha_s(sigma=4/3)|    = {abs(alpha_s_gate):.6f}")
print(f"    |alpha_s(max smooth)|   = {alpha_s_decisive:.6f}")
print(f"    Minimum |alpha_s|       = {min_abs_alpha:.6f} at sigma = {sigma_values[min_sigma_idx]:.4f}")
print(f"")
print(f"  VERDICT: {verdict}")
print(f"  {detail}")


# =============================================================================
# STEP 7: PHYSICAL INTERPRETATION
# =============================================================================
print("\n" + "=" * 78)
print("STEP 7: Physical Interpretation")
print("=" * 78)

print(f"""
  The Casimir smoothing hypothesis:
  ---------------------------------
  The spectral action S(tau) = sum_{{(p,q)}} S_{{(p,q)}}(tau) is built from discrete
  Peter-Weyl sectors. Each sector has Casimir C_2(p,q) serving as a fiber
  wavenumber squared. The derivative dn_s/d(ln k) computed from this discrete
  sum inherits the granularity of the Casimir ladder.

  If the mapping from fiber wavenumber to physical CMB wavenumber involves
  any coarse-graining (e.g., because the CMB mode couples to a range of fiber
  modes, not a single sector), then smoothing over adjacent Casimir values
  gives the physical running.

  Results:
  --------
  Raw alpha_s (no smoothing):     {alpha_raw:.6e}  (5.0 sigma from Planck)
  alpha_s at sigma = C_2(1,0):    {alpha_s_gate:.6e}
  alpha_s at max smoothing:       {alpha_s_maxsmooth:.6e}
  Minimum |alpha_s|:              {min_abs_alpha:.6e}
""")

# Check if the smoothing produces UNIFORM tau-dependence (all sectors have same shape)
print(f"  Diagnostic: sector-to-sector variation in d(ln S)/dtau at fold")
dlnS_sectors = []
for pq in sectors_sorted:
    if pq == (0, 0):
        continue
    S_sec = np.array([sector_S_eff[(i, pq[0], pq[1])] for i in range(len(tau_evals))])
    S_sec_near = S_sec[idx_near]
    if np.all(S_sec_near > 0):
        cs_sec = CubicSpline(tau_near, S_sec_near)
        S_v = float(cs_sec(tau_f))
        dS_v = float(cs_sec(tau_f, 1))
        dlnS_sectors.append((pq, dS_v / S_v))

dlnS_vals = np.array([x[1] for x in dlnS_sectors])
print(f"  d(ln S)/dtau range: [{np.min(dlnS_vals):.6f}, {np.max(dlnS_vals):.6f}]")
print(f"  d(ln S)/dtau mean:  {np.mean(dlnS_vals):.6f}")
print(f"  d(ln S)/dtau std:   {np.std(dlnS_vals):.6f}")
print(f"  Relative std/mean:  {np.std(dlnS_vals)/np.mean(dlnS_vals):.4f}")

if np.std(dlnS_vals) / np.mean(dlnS_vals) < 0.01:
    print(f"\n  CONCLUSION: All sectors have nearly identical d(ln S)/dtau profiles.")
    print(f"  Smoothing CANNOT change the running because the running comes from the")
    print(f"  UNIVERSAL tau-dependence, not from inter-sector variations.")
    print(f"  The large alpha_s is intrinsic to the spectral geometry, not an artifact")
    print(f"  of the discrete Casimir ladder.")
else:
    print(f"\n  Sectors have significant variation in d(ln S)/dtau profiles.")
    print(f"  Smoothing has physical content and can modify the effective running.")


# =============================================================================
# STEP 8: PLOT
# =============================================================================
print("\n" + "=" * 78)
print("STEP 8: Generate Plot")
print("=" * 78)

fig = plt.figure(figsize=(16, 12))
gs = GridSpec(2, 2, figure=fig, hspace=0.3, wspace=0.3)

# Panel 1: |alpha_s| vs smoothing width
ax1 = fig.add_subplot(gs[0, 0])
sigmas = [sigma_values[si] for si in range(len(sigma_values)) if sigma_values[si] > 0]
alphas = [abs(results[si]['alpha_s']) for si in range(len(sigma_values)) if sigma_values[si] > 0]
ax1.plot(sigmas, alphas, 'o-', color='#2196F3', linewidth=2, markersize=8, label='Smoothed')
ax1.axhline(y=abs(alpha_raw), color='black', linestyle='--', linewidth=1.5,
            label=f'Raw |alpha_s| = {abs(alpha_raw):.4f}')
ax1.axhline(y=0.015, color='green', linestyle=':', linewidth=1.5, label='PASS threshold (0.015)')
ax1.axhline(y=0.030, color='red', linestyle=':', linewidth=1.5, label='FAIL threshold (0.030)')
ax1.axhline(y=abs(planck_alpha_s), color='orange', linestyle='-.', linewidth=1.5,
            label=f'Planck |alpha_s| = {abs(planck_alpha_s)}')
ax1.axvspan(casimir_su3(1, 0), casimir_su3(1, 1), alpha=0.1, color='blue',
            label='C_2(1,0) to C_2(1,1)')
ax1.set_xlabel(r'$\sigma_C$ (Casimir smoothing width)', fontsize=12)
ax1.set_ylabel(r'$|\alpha_s|$', fontsize=12)
ax1.set_title(r'$|\alpha_s|$ vs Casimir Smoothing Width', fontsize=13)
ax1.set_xscale('log')
ax1.legend(fontsize=9, loc='upper right')
ax1.set_xlim(0.5, 150)
ax1.grid(True, alpha=0.3)

# Panel 2: eps_H vs smoothing width
ax2 = fig.add_subplot(gs[0, 1])
eps_vals = [results[si]['eps_H'] for si in range(len(sigma_values))]
ax2.plot(sigma_values, eps_vals, 's-', color='#FF5722', linewidth=2, markersize=6)
ax2.set_xlabel(r'$\sigma_C$ (Casimir smoothing width)', fontsize=12)
ax2.set_ylabel(r'$\epsilon_H$', fontsize=12)
ax2.set_title(r'$\epsilon_H$ vs Smoothing Width', fontsize=13)
ax2.grid(True, alpha=0.3)

# Panel 3: Per-sector d(ln S)/dtau vs C_2
ax3 = fig.add_subplot(gs[1, 0])
c2_plot = [sector_C2[x[0]] for x in dlnS_sectors]
dlnS_plot = [x[1] for x in dlnS_sectors]
labels_plot = [f"({x[0][0]},{x[0][1]})" for x in dlnS_sectors]
ax3.bar(range(len(c2_plot)), dlnS_plot, color='#4CAF50', alpha=0.7)
ax3.set_xticks(range(len(c2_plot)))
ax3.set_xticklabels(labels_plot, rotation=45, fontsize=9)
ax3.set_xlabel('Sector (p,q)', fontsize=12)
ax3.set_ylabel(r'$d(\ln S_{(p,q)})/d\tau$', fontsize=12)
ax3.set_title('Per-Sector Log Derivative at Fold', fontsize=13)
ax3.grid(True, alpha=0.3, axis='y')

# Panel 4: Smoothed S(tau) profiles for different sigma values
ax4 = fig.add_subplot(gs[1, 1])
colors = plt.cm.viridis(np.linspace(0, 1, len(sigma_values)))
for sigma_idx, sigma in enumerate(sigma_values):
    if sigma_idx % 2 == 0 or sigma_idx == len(sigma_values) - 1:
        S_arr = S_smoothed[sigma_idx]
        lbl = f'sigma={sigma:.1f}' if sigma > 0 else 'raw'
        ax4.plot(tau_evals, S_arr / S_arr[idx_fold], '-o', color=colors[sigma_idx],
                 label=lbl, markersize=4, linewidth=1.5)
ax4.axvline(x=tau_f, color='grey', linestyle='--', linewidth=1, alpha=0.5,
            label=f'tau_fold = {tau_f}')
ax4.set_xlabel(r'$\tau$', fontsize=12)
ax4.set_ylabel(r'$S(\tau) / S(\tau_{fold})$', fontsize=12)
ax4.set_title('Normalized Spectral Action Profiles', fontsize=13)
ax4.legend(fontsize=8, loc='upper left')
ax4.grid(True, alpha=0.3)

fig.suptitle(f'CASIMIR-SMOOTH-RUNNING-66: Verdict = {verdict}\n'
             f'Raw |alpha_s| = {abs(alpha_raw):.4f}, '
             f'Min smoothed |alpha_s| = {min_abs_alpha:.4f}',
             fontsize=14, fontweight='bold', y=0.98)

plt.savefig(os.path.join(SCRIPT_DIR, 's66_casimir_smooth_running.png'),
            dpi=150, bbox_inches='tight')
plt.close()
print(f"  Plot saved: s66_casimir_smooth_running.png")


# =============================================================================
# STEP 9: SAVE DATA
# =============================================================================
print("\n" + "=" * 78)
print("STEP 9: Save Data")
print("=" * 78)

outpath = os.path.join(SCRIPT_DIR, 's66_casimir_smooth_running.npz')

# Collect alpha_s values for each sigma
alpha_s_array = np.array([results[si]['alpha_s'] for si in range(len(sigma_values))])
eps_H_array = np.array([results[si]['eps_H'] for si in range(len(sigma_values))])
ns_array = np.array([results[si]['ns'] for si in range(len(sigma_values))])

np.savez(
    outpath,
    # Gate
    gate_name='CASIMIR-SMOOTH-RUNNING-66',
    gate_verdict=verdict,
    gate_detail=detail,

    # Scan results
    sigma_values=sigma_values,
    alpha_s_vs_sigma=alpha_s_array,
    eps_H_vs_sigma=eps_H_array,
    ns_vs_sigma=ns_array,

    # Key thresholds
    alpha_s_raw=alpha_raw,
    alpha_s_at_C2_10=alpha_s_gate,
    alpha_s_max_smooth=alpha_s_maxsmooth,
    alpha_s_min_abs=min_abs_alpha,
    sigma_at_min_abs=sigma_values[min_sigma_idx],

    # Per-sector data
    sectors=np.array(sectors_sorted),
    C2_values=C2_arr,
    sector_dlnS_dtau=dlnS_vals,
    dlnS_relative_std=np.std(dlnS_vals) / np.mean(dlnS_vals),

    # Smoothed actions at fold
    S_smoothed_at_fold=np.array([S_smoothed[si][idx_fold] for si in range(len(sigma_values))]),

    # Reference
    tau_evals=tau_evals,
    tau_fold=tau_f,
    Delta=Delta,
    G_DeWitt=G,
    planck_alpha_s=planck_alpha_s,
    planck_alpha_s_sigma=planck_alpha_s_sigma,
)

print(f"  Data saved: {outpath}")

# =============================================================================
# FINAL SUMMARY
# =============================================================================
print("\n" + "=" * 78)
print("FINAL SUMMARY")
print("=" * 78)
print(f"""
  Gate:           CASIMIR-SMOOTH-RUNNING-66
  Verdict:        {verdict}

  Raw alpha_s:             {alpha_raw:.6e}  (W3-A result)
  Min smoothed |alpha_s|:  {min_abs_alpha:.6e}  (at sigma_C = {sigma_values[min_sigma_idx]:.2f})
  alpha_s at C_2(1,0):     {alpha_s_gate:.6e}
  alpha_s at max smooth:   {alpha_s_maxsmooth:.6e}
  Reduction ratio:         {min_abs_alpha / abs(alpha_raw):.4f}

  {detail}
""")

print("=" * 78)
print("CASIMIR-SMOOTH-RUNNING-66 COMPLETE")
print("=" * 78)
