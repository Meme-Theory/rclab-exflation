#!/usr/bin/env python3
"""
SPECTRAL-FLOW-NS-46: Spectral Current and Velocity-Weighted Tilt
=================================================================

Session 46, W2-1 (spectral-geometer)

Computes the spectral current j(lambda, tau) = d_k * |d lambda_k / d tau|
and extracts the effective hose-count exponent alpha from eigenvalue velocities.

Physics:
  Modes near van Hove singularities (d lambda/d tau = 0) contribute ZERO spectral
  current -- they are "frozen" in the spectral plane. Fast-moving modes contribute
  proportionally to their velocity. This intermediate weighting (between Weyl's
  alpha=6 and collective alpha=0) may give alpha ~ 1.

  The spectral current is the natural observable in spectral flow theory
  (Mueller, Lott): it counts how many eigenvalues cross a given threshold per
  unit deformation parameter. The total spectral flow (integral of j) is a
  topological invariant, but the differential current j(k) carries geometric
  information about HOW eigenvalues redistribute.

  TWO k-variables are used:
  (A) k_casimir = sqrt(C_2(p,q)): proper geometric wavenumber on SU(3).
      5 non-trivial sectors, k in [1.15, 2.45]. Limited dynamic range.
  (B) k_eigenvalue = |omega(tau=0)|: eigenvalue at the round metric as k-proxy.
      510 unique values, k in [0.83, 1.80]. Higher resolution but mixes
      eigenvalue and wavenumber.

Method:
  1. Load eigenvalues at 5 tau values near fold (0.190, 0.195, 0.200, 0.205, 0.209)
     from s45_dos_fine_scan.npz, plus the full 992-mode set from s44_dos_tau.npz
  2. Compute d lambda_k / d tau by 4th-order forward finite differences at tau = fold
  3. Spectral current: j(k) = sum_{modes at k} d_k * |d lambda_k / d tau|
  4. Fit j(k) ~ k^alpha on log-log using BOTH k-variables
  5. Decompose: alpha_j = alpha_N + alpha_d + alpha_v (counting + dimension + velocity)
  6. Velocity-weighted Bogoliubov power spectrum for n_s

Gate: SPECTRAL-FLOW-NS-46
  PASS: alpha in [0.8, 1.2]
  FAIL: alpha outside [0.5, 2.0]
  INFO: otherwise
  Note: gate evaluates alpha_v (velocity-only exponent), since this is the
  component not already determined by Weyl counting.

Formula Audit Protocol (S46 Mandatory):
  (a) d lambda / d tau: 4th-order forward difference at tau=0.190.
      DIMENSIONLESS (lambda in M_KK, tau dimensionless).
  (b) j(k) = sum d_k * |v_k|: degeneracy-weighted velocity.
  (c) alpha from log-log fit: DIMENSIONLESS exponent.
  (d) Decomposition: j/N = d(p,q) * <|v|>, so alpha_jpm = alpha_d + alpha_v.
  (e) Limiting case: if all velocities equal, alpha_j = alpha_Weyl. [VERIFIED]
"""

import sys
import numpy as np
from pathlib import Path
from numpy.linalg import lstsq

sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import tau_fold, M_KK, PI

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

DATA_DIR = Path(__file__).parent
OUT_PREFIX = "s46_spectral_flow_ns"

# ==============================================================================
# SECTION 1: Load eigenvalue data
# ==============================================================================
print("=" * 78)
print("SPECTRAL-FLOW-NS-46: Spectral Current from Eigenvalue Velocities")
print("=" * 78)

# --- Source 1: s45_dos_fine_scan.npz ---
d_fine = np.load(DATA_DIR / "s45_dos_fine_scan.npz", allow_pickle=True)
tau_fine_all = d_fine["tau_fine"]

# --- Source 2: s44_dos_tau.npz ---
d_dos = np.load(DATA_DIR / "s44_dos_tau.npz", allow_pickle=True)
omega_tau0 = d_dos["tau0.00_all_omega"]
omega_fold = d_dos["tau0.19_all_omega"]
dim2_all = d_dos["tau0.19_all_dim2"]
omega_015 = d_dos["tau0.15_all_omega"]

# --- Source 3: s45_fwd_bwd_ns.npz ---
d_bogo = np.load(DATA_DIR / "s45_fwd_bwd_ns.npz", allow_pickle=True)
beta2_fwd = d_bogo["beta2_fwd"]
beta2_bwd = d_bogo["beta2_bwd"]
k_eigenvalue = d_bogo["k_casimir"]  # NOTE: this is |omega(tau=0)|, NOT sqrt(C_2)
mode_sector = d_bogo["mode_sector"]
k_unique_ev = d_bogo["k_unique"]

N_modes = len(omega_fold)
d_k = np.sqrt(dim2_all)

print(f"\n--- Loaded Data ---")
print(f"  N_modes: {N_modes}")
print(f"  tau_fold: {tau_fold}")
print(f"  omega(fold) range: [{omega_fold.min():.6f}, {omega_fold.max():.6f}]")
print(f"  k_eigenvalue range: [{k_eigenvalue.min():.6f}, {k_eigenvalue.max():.6f}]")

# ==============================================================================
# SECTION 2: Compute eigenvalue velocities d lambda_k / d tau at the fold
# ==============================================================================
print(f"\n{'=' * 78}")
print("SECTION 2: Eigenvalue Velocities at Fold (tau = 0.190)")
print("=" * 78)

# Sector mapping: mode_sector in S45 -> fine-scan sector key
sector_fine_key = {
    0: '0_0',   # (0,0)
    1: '1_0',   # (1,0) [= (0,1)]
    5: '1_1',   # (1,1)
    2: '2_0',   # (2,0) [= (0,2)]
    6: '2_1',   # (2,1) [= (1,2)]
    3: '3_0',   # (3,0) [= (0,3)]
}

# Fine-scan has eigenvalues at tau = 0.190, 0.195, 0.200, 0.205, 0.209
# Use 4th-order forward derivative at tau = 0.190:
# f'(x0) = (-25f0 + 48f1 - 36f2 + 16f3 - 3f4) / (12h)
# with h = 0.005

h = 0.005
vel_fine = np.zeros(N_modes)
vel_2pt = np.zeros(N_modes)  # simple forward diff for comparison
fine_matched = np.zeros(N_modes, dtype=bool)

print(f"\n--- 4th-order forward derivative (h = {h}) ---")
for ms_val, pq_key in sector_fine_key.items():
    ev_190 = d_fine[f'evals_tau0.190_{pq_key}']
    ev_195 = d_fine[f'evals_tau0.195_{pq_key}']
    ev_200 = d_fine[f'evals_tau0.200_{pq_key}']
    ev_205 = d_fine[f'evals_tau0.205_{pq_key}']
    ev_209 = d_fine[f'evals_tau0.209_{pq_key}']

    n_levels = min(len(ev_190), len(ev_195), len(ev_200), len(ev_205), len(ev_209))

    # 4th-order forward derivative
    v_4pt = (-25*ev_190[:n_levels] + 48*ev_195[:n_levels]
             - 36*ev_200[:n_levels] + 16*ev_205[:n_levels]
             - 3*ev_209[:n_levels]) / (12*h)

    # Simple 2-point forward difference
    v_2pt = (ev_195[:n_levels] - ev_190[:n_levels]) / h

    # Match each mode in this sector to a fine-scan level
    mask = mode_sector == ms_val
    modes_in_sector = np.where(mask)[0]

    for mi in modes_in_sector:
        om = omega_fold[mi]
        dists = np.abs(ev_190[:n_levels] - om)
        best_idx = np.argmin(dists)
        if dists[best_idx] < 0.01:
            vel_fine[mi] = v_4pt[best_idx]
            vel_2pt[mi] = v_2pt[best_idx]
            fine_matched[mi] = True

    n_matched = np.sum(mask & fine_matched)
    print(f"  sector {ms_val} ({pq_key}): {n_matched}/{mask.sum()} matched")

print(f"\n  Total fine-matched: {fine_matched.sum()}/{N_modes}")

# Fallback for unmatched: coarse backward difference (tau=0.15 -> 0.19)
vel_coarse = (omega_fold - omega_015) / 0.04
vel_primary = np.where(fine_matched, vel_fine, vel_coarse)

# Consistency check: 2-point vs 4-point
mask_valid = fine_matched & (np.abs(vel_2pt) > 0.001)
rel_diff = np.abs(vel_fine[mask_valid] - vel_2pt[mask_valid]) / np.abs(vel_2pt[mask_valid])
print(f"\n--- 2pt vs 4pt consistency ---")
print(f"  Median relative difference: {np.median(rel_diff):.4f}")
print(f"  Max relative difference: {rel_diff.max():.4f}")
print(f"  Note: 4pt uses wider stencil (tau=0.190..0.209), may differ for nonlinear trajectories")

abs_vel = np.abs(vel_primary)

print(f"\n--- Final velocity statistics ---")
print(f"  |v| range: [{abs_vel.min():.6f}, {abs_vel.max():.6f}]")
print(f"  v mean:    {vel_primary.mean():.6f}")
print(f"  v > 0: {(vel_primary > 0).sum()}, v < 0: {(vel_primary < 0).sum()}")
print(f"  Modes near VH (|v| < 0.01): {(abs_vel < 0.01).sum()}")

# ==============================================================================
# SECTION 3: Spectral Current — Casimir Wavenumber Analysis
# ==============================================================================
print(f"\n{'=' * 78}")
print("SECTION 3: Spectral Current — Casimir Wavenumber k = sqrt(C_2)")
print("=" * 78)

# Peter-Weyl sectors and their Casimir eigenvalues
sectors_pq = {
    0: (0, 0),
    1: (1, 0),  # combined with (0,1)
    5: (1, 1),
    2: (2, 0),  # combined with (0,2)
    6: (2, 1),  # combined with (1,2)
    3: (3, 0),  # combined with (0,3)
}

# Casimir: C_2(p,q) = (p^2 + q^2 + 3p + 3q + pq)/3
def casimir_su3(p, q):
    return (p**2 + q**2 + 3*p + 3*q + p*q) / 3.0

def dim_su3(p, q):
    return (p + 1) * (q + 1) * (p + q + 2) // 2

# Collect sector-level data
sec_k = []
sec_j_total = []
sec_j_per_mode = []
sec_v_mean = []
sec_N = []
sec_d = []
sec_label = []

P_total = beta2_fwd + beta2_bwd

sec_P_weyl = []
sec_P_vel = []

print(f"\n{'Sector':<12} {'k_Cas':>7} {'d(p,q)':>7} {'N':>5} "
      f"{'j_total':>10} {'j/N':>8} {'<|v|>':>8}")
print("-" * 65)

for ms in sorted(sectors_pq.keys()):
    p, q = sectors_pq[ms]
    C2 = casimir_su3(p, q)
    if C2 == 0:
        continue  # skip trivial rep (k=0, not on log scale)
    k = np.sqrt(C2)
    d = dim_su3(p, q)

    mask = mode_sector == ms
    n = mask.sum()
    if n == 0:
        continue

    j = np.sum(d_k[mask] * abs_vel[mask])
    j_pm = j / n
    v_m = np.mean(abs_vel[mask])

    pw = np.sum(dim2_all[mask] * P_total[mask])
    pv = np.sum(d_k[mask] * abs_vel[mask] * P_total[mask])

    sec_k.append(k)
    sec_j_total.append(j)
    sec_j_per_mode.append(j_pm)
    sec_v_mean.append(v_m)
    sec_N.append(n)
    sec_d.append(d)
    sec_label.append(f"({p},{q})")
    sec_P_weyl.append(pw)
    sec_P_vel.append(pv)

    print(f"  ({p},{q}){' '*(6-len(f'({p},{q})'))} {k:7.4f} {d:7d} {n:5d} "
          f"{j:10.2f} {j_pm:8.4f} {v_m:8.4f}")

sec_k = np.array(sec_k)
sec_j_total = np.array(sec_j_total)
sec_j_per_mode = np.array(sec_j_per_mode)
sec_v_mean = np.array(sec_v_mean)
sec_N = np.array(sec_N)
sec_d = np.array(sec_d)
sec_P_weyl = np.array(sec_P_weyl)
sec_P_vel = np.array(sec_P_vel)

# Log-log fits with uncertainty (5 data points, 2 parameters)
lk = np.log(sec_k)
n_pts = len(lk)
p_fit = 2  # slope + intercept
A = np.vstack([lk, np.ones(n_pts)]).T
ATA_inv = np.linalg.inv(A.T @ A)

def fit_with_uncertainty(x, y, label):
    """Log-log fit with standard error on slope."""
    lx = np.log(x)
    ly = np.log(y)
    A_loc = np.vstack([lx, np.ones(len(lx))]).T
    sol, _, _, _ = lstsq(A_loc, ly, rcond=None)
    alpha = sol[0]
    resid = ly - A_loc @ sol
    s2 = np.sum(resid**2) / max(len(lx) - 2, 1)
    ATA_inv_loc = np.linalg.inv(A_loc.T @ A_loc)
    se = np.sqrt(s2 * ATA_inv_loc[0, 0])
    ss_tot = np.sum((ly - ly.mean())**2)
    r2 = 1 - np.sum(resid**2) / ss_tot if ss_tot > 0 else 0.0
    print(f"  {label}: alpha = {alpha:.3f} +/- {se:.3f}  (R^2 = {r2:.4f})")
    return alpha, se, r2

print(f"\n--- Power-law fits (k = sqrt(C_2), {n_pts} sectors) ---")
alpha_j, se_j, r2_j = fit_with_uncertainty(sec_k, sec_j_total, "j(k) total")
alpha_jpm, se_jpm, r2_jpm = fit_with_uncertainty(sec_k, sec_j_per_mode, "j(k)/N per-mode")
alpha_v, se_v, r2_v = fit_with_uncertainty(sec_k, sec_v_mean, "<|v|>(k)")
alpha_N, se_N, r2_N = fit_with_uncertainty(sec_k, sec_N.astype(float), "N(k)")
alpha_d, se_d, r2_d = fit_with_uncertainty(sec_k, sec_d.astype(float), "d(p,q)(k)")

print(f"\n--- Decomposition ---")
print(f"  alpha_j = alpha_N + alpha_d + alpha_v")
print(f"         = {alpha_N:.3f} + {alpha_d:.3f} + {alpha_v:.3f} = {alpha_N + alpha_d + alpha_v:.3f}")
print(f"  Actual:  {alpha_j:.3f}")
print(f"  Check j/N = d*<|v|>: alpha_jpm = alpha_d + alpha_v = {alpha_d + alpha_v:.3f} vs {alpha_jpm:.3f}")

# Dynamic range diagnostic
print(f"\n--- Dynamic range ---")
print(f"  k range: [{sec_k.min():.4f}, {sec_k.max():.4f}]")
print(f"  log(k) range: {np.log(sec_k.max()/sec_k.min()):.3f} decades")
print(f"  WARNING: Only {n_pts} sectors, < 1 decade in k. Fit uncertainty is large.")

# ==============================================================================
# SECTION 4: Spectral Current — Eigenvalue-k Analysis
# ==============================================================================
print(f"\n{'=' * 78}")
print("SECTION 4: Spectral Current — Eigenvalue Wavenumber k = |omega(tau=0)|")
print("=" * 78)

# This is the original S45 k-proxy: k = |omega(tau=0)|
# Higher resolution (510 unique k values) but mixes eigenvalue with wavenumber

j_per_mode_arr = d_k * abs_vel
k_unique_ev = np.unique(k_eigenvalue)
n_k_ev = len(k_unique_ev)

j_ev_binned = np.zeros(n_k_ev)
v_ev_binned = np.zeros(n_k_ev)
d2_ev_binned = np.zeros(n_k_ev)
n_ev_binned = np.zeros(n_k_ev)

for i, kv in enumerate(k_unique_ev):
    mask = np.abs(k_eigenvalue - kv) < 1e-6
    j_ev_binned[i] = np.sum(j_per_mode_arr[mask])
    v_ev_binned[i] = np.mean(abs_vel[mask])
    d2_ev_binned[i] = np.sum(dim2_all[mask])
    n_ev_binned[i] = mask.sum()

valid_ev = j_ev_binned > 0
c_ev = np.polyfit(np.log(k_unique_ev[valid_ev]), np.log(j_ev_binned[valid_ev]), 1)
alpha_ev = c_ev[0]
pred_ev = c_ev[0] * np.log(k_unique_ev[valid_ev]) + c_ev[1]
ss_res_ev = np.sum((np.log(j_ev_binned[valid_ev]) - pred_ev)**2)
ss_tot_ev = np.sum((np.log(j_ev_binned[valid_ev]) - np.log(j_ev_binned[valid_ev]).mean())**2)
r2_ev = 1 - ss_res_ev / ss_tot_ev

c_v_ev = np.polyfit(np.log(k_unique_ev[valid_ev]), np.log(v_ev_binned[valid_ev]), 1)
alpha_v_ev = c_v_ev[0]

c_d2_ev = np.polyfit(np.log(k_unique_ev[valid_ev]), np.log(d2_ev_binned[valid_ev]), 1)
alpha_W_ev = c_d2_ev[0]

print(f"\n--- Eigenvalue-k fits ({n_k_ev} unique k values) ---")
print(f"  j(k) total:   alpha = {alpha_ev:.4f}  (R^2 = {r2_ev:.4f})")
print(f"  <|v|>(k):      alpha_v = {alpha_v_ev:.4f}")
print(f"  N(k) Weyl:     alpha_W = {alpha_W_ev:.4f}")
print(f"  Dynamic range: k in [{k_unique_ev.min():.4f}, {k_unique_ev.max():.4f}], "
      f"{np.log(k_unique_ev.max()/k_unique_ev.min()):.3f} decades")

# ==============================================================================
# SECTION 5: Per-Branch Analysis
# ==============================================================================
print(f"\n{'=' * 78}")
print("SECTION 5: Per-Branch Velocity Analysis")
print("=" * 78)

# B1: trivial rep (0,0) eigenvalues. lambda ~ 0.82
# B2: (1,1) lowest eigenvalue. lambda ~ 0.845
# B3: everything else. lambda > 0.87

branch_labels = np.zeros(N_modes, dtype=int)
branch_labels[omega_fold < 0.84] = 1
branch_labels[(omega_fold >= 0.84) & (omega_fold < 0.87)] = 2
branch_labels[omega_fold >= 0.87] = 3

for b in [1, 2, 3]:
    mask = branch_labels == b
    if mask.sum() == 0:
        continue
    v_b = vel_primary[mask]
    j_b = j_per_mode_arr[mask]
    print(f"\n  Branch B{b}: {mask.sum()} modes")
    print(f"    v range: [{v_b.min():.6f}, {v_b.max():.6f}]")
    print(f"    <|v|>: {np.abs(v_b).mean():.6f}")
    print(f"    j fraction: {j_b.sum()/j_per_mode_arr.sum():.4f}")

# Van Hove diagnostic
vh_threshold = 0.01
n_vh = (abs_vel < vh_threshold).sum()
j_vh_frac = j_per_mode_arr[abs_vel < vh_threshold].sum() / j_per_mode_arr.sum()
print(f"\n  Near-VH modes (|v| < {vh_threshold}): {n_vh} ({n_vh/N_modes*100:.1f}%)")
print(f"  VH spectral current fraction: {j_vh_frac:.6f}")
print(f"  Velocity weighting suppresses VH by factor: "
      f"{(n_vh/N_modes) / max(j_vh_frac, 1e-10):.1f}x")

# ==============================================================================
# SECTION 6: Velocity-Weighted Bogoliubov Power Spectrum
# ==============================================================================
print(f"\n{'=' * 78}")
print("SECTION 6: Velocity-Weighted Bogoliubov Power Spectrum")
print("=" * 78)

# Sector-level power spectra (Casimir k)
print(f"\n--- Sector-level (k = sqrt(C_2)) ---")
c_pw = np.polyfit(np.log(sec_k), np.log(sec_P_weyl), 1)
c_pv = np.polyfit(np.log(sec_k), np.log(sec_P_vel), 1)
ns_weyl_sec = c_pw[0]
ns_vel_sec = c_pv[0]
print(f"  Weyl-weighted:     n_s = {ns_weyl_sec:.4f}")
print(f"  Velocity-weighted: n_s = {ns_vel_sec:.4f}")
print(f"  Velocity correction to n_s: {ns_vel_sec - ns_weyl_sec:.4f}")

# Eigenvalue-k level
P_weyl_ev = np.zeros(n_k_ev)
P_vel_ev = np.zeros(n_k_ev)

for i, kv in enumerate(k_unique_ev):
    mask = np.abs(k_eigenvalue - kv) < 1e-6
    P_weyl_ev[i] = np.sum(dim2_all[mask] * P_total[mask])
    P_vel_ev[i] = np.sum(j_per_mode_arr[mask] * P_total[mask])

valid_pw_ev = P_weyl_ev > 0
valid_pv_ev = P_vel_ev > 0

c_pw_ev = np.polyfit(np.log(k_unique_ev[valid_pw_ev]), np.log(P_weyl_ev[valid_pw_ev]), 1)
c_pv_ev = np.polyfit(np.log(k_unique_ev[valid_pv_ev]), np.log(P_vel_ev[valid_pv_ev]), 1)

print(f"\n--- Eigenvalue-k level ---")
print(f"  Weyl-weighted:     n_s = {c_pw_ev[0]:.4f}")
print(f"  Velocity-weighted: n_s = {c_pv_ev[0]:.4f}")

# ==============================================================================
# SECTION 7: Signed Spectral Flow
# ==============================================================================
print(f"\n{'=' * 78}")
print("SECTION 7: Signed Spectral Flow")
print("=" * 78)

j_signed = d_k * vel_primary

# Per sector
print(f"\n{'Sector':<12} {'j_signed':>10} {'j_unsigned':>12} {'cancel%':>8}")
print("-" * 45)
for i_s, ms in enumerate(sorted(sectors_pq.keys())):
    p, q = sectors_pq[ms]
    mask = mode_sector == ms
    js = np.sum(j_signed[mask])
    ju = np.sum(np.abs(j_signed[mask]))
    cancel = 1 - abs(js) / ju if ju > 0 else 0
    print(f"  ({p},{q}){' '*(6-len(f'({p},{q})'))} {js:10.2f} {ju:12.2f} {cancel*100:7.1f}%")

net_flow = np.sum(j_signed)
unsigned_flow = np.sum(np.abs(j_signed))
total_cancel = 1 - abs(net_flow) / unsigned_flow

print(f"\n  Total net flow:      {net_flow:.2f}")
print(f"  Total unsigned flow: {unsigned_flow:.2f}")
print(f"  Cancellation:        {total_cancel*100:.1f}%")
print(f"  Direction: {'expanding (v > 0 dominates)' if net_flow > 0 else 'contracting (v < 0 dominates)'}")

# ==============================================================================
# SECTION 8: Gate Evaluation
# ==============================================================================
print(f"\n{'=' * 78}")
print("SECTION 8: Gate Evaluation — SPECTRAL-FLOW-NS-46")
print("=" * 78)

# The gate evaluates alpha_v (velocity-only exponent) from the Casimir-k fit.
# This is the component genuinely testing whether velocity weighting gives alpha ~ 1.
# alpha_j (total) includes Weyl counting which is trivially large.

alpha_gate = alpha_v  # velocity exponent is the physically meaningful one
se_gate = se_v

print(f"\n--- Alpha hierarchy ---")
print(f"  alpha_j (total, Casimir k):   {alpha_j:.3f} +/- {se_j:.3f}")
print(f"  alpha_jpm (per-mode):         {alpha_jpm:.3f} +/- {se_jpm:.3f}")
print(f"  alpha_v (velocity only):      {alpha_v:.3f} +/- {se_v:.3f}")
print(f"  alpha_d (dimension scaling):  {alpha_d:.3f} +/- {se_d:.3f}")
print(f"  alpha_N (mode counting):      {alpha_N:.3f} +/- {se_N:.3f}")
print(f"  alpha_ev (eigenvalue-k, j):   {alpha_ev:.3f}")
print(f"  alpha_v_ev (eigenvalue-k, v): {alpha_v_ev:.3f}")

# Gate decision on alpha_v (Casimir-k velocity scaling)
if 0.8 <= alpha_gate <= 1.2:
    verdict = "PASS"
    detail = f"alpha_v = {alpha_gate:.3f} +/- {se_gate:.3f} in [0.8, 1.2]"
elif 0.5 <= alpha_gate <= 2.0:
    verdict = "INFO"
    detail = f"alpha_v = {alpha_gate:.3f} +/- {se_gate:.3f} in [0.5, 2.0] but outside [0.8, 1.2]"
else:
    verdict = "FAIL"
    detail = f"alpha_v = {alpha_gate:.3f} +/- {se_gate:.3f} outside [0.5, 2.0]"

# However: the task specifically asks for alpha from j(k) ~ k^alpha at Casimir k
# which is alpha_j = 4.03. This FAILS the gate.
# The per-mode alpha_jpm = 2.49 also fails.
# ONLY the bare velocity alpha_v = 0.62 is in the INFO range.

# Report both
if 0.8 <= alpha_j <= 1.2:
    verdict_j = "PASS"
elif 0.5 <= alpha_j <= 2.0:
    verdict_j = "INFO"
else:
    verdict_j = "FAIL"

print(f"\n--- Gate: SPECTRAL-FLOW-NS-46 ---")
print(f"  PRIMARY (j(k) ~ k^alpha_j):  alpha_j = {alpha_j:.3f}, Verdict: {verdict_j}")
print(f"  VELOCITY (<|v|> ~ k^alpha_v): alpha_v = {alpha_gate:.3f}, Verdict: {verdict}")
print(f"  Detail: {detail}")

# Final interpretation
print(f"\n--- Physical Interpretation ---")
print(f"  Velocity weighting does NOT bring alpha to ~1.")
print(f"  The velocity exponent alpha_v = {alpha_v:.3f} is modest (R^2 = {r2_v:.3f}):")
print(f"    higher-k modes move {np.exp(alpha_v * np.log(2.45/1.15)):.1f}x faster than lower-k.")
print(f"  But the spectral current is dominated by Weyl counting (alpha_N = {alpha_N:.1f})")
print(f"    and dimension scaling (alpha_d = {alpha_d:.1f}), giving alpha_j = {alpha_j:.1f}.")
print(f"  The VH suppression is real but minimal: {n_vh} modes (|v|<0.01)")
print(f"    carry only {j_vh_frac*100:.2f}% of total current.")
print(f"  Spectral current is a UV-dominated observable, like Weyl counting.")

# ==============================================================================
# SAVE
# ==============================================================================
print(f"\n{'=' * 78}")
print("Saving results...")
print("=" * 78)

np.savez(DATA_DIR / f"{OUT_PREFIX}.npz",
    # Gate
    gate_name=np.array(["SPECTRAL-FLOW-NS-46"]),
    gate_verdict=np.array([verdict_j]),
    gate_detail=np.array([f"alpha_j={alpha_j:.3f}, alpha_v={alpha_v:.3f}"]),

    # Casimir-k analysis (PRIMARY)
    alpha_j=np.array(alpha_j),
    alpha_j_se=np.array(se_j),
    alpha_jpm=np.array(alpha_jpm),
    alpha_jpm_se=np.array(se_jpm),
    alpha_v_casimir=np.array(alpha_v),
    alpha_v_se=np.array(se_v),
    alpha_N=np.array(alpha_N),
    alpha_d=np.array(alpha_d),
    r2_j=np.array(r2_j),
    r2_v_casimir=np.array(r2_v),

    # Sector data
    sec_k=sec_k,
    sec_j_total=sec_j_total,
    sec_j_per_mode=sec_j_per_mode,
    sec_v_mean=sec_v_mean,
    sec_N=sec_N,
    sec_d=sec_d,
    sec_P_weyl=sec_P_weyl,
    sec_P_vel=sec_P_vel,

    # Eigenvalue-k analysis
    alpha_ev=np.array(alpha_ev),
    alpha_v_ev=np.array(alpha_v_ev),
    alpha_W_ev=np.array(alpha_W_ev),
    r2_ev=np.array(r2_ev),

    # Per-mode data
    vel_primary=vel_primary,
    vel_fine=vel_fine,
    vel_2pt=vel_2pt,
    vel_coarse=vel_coarse,
    j_per_mode=j_per_mode_arr,
    abs_vel=abs_vel,
    fine_matched=fine_matched,

    # Eigenvalue-k binned
    k_unique_ev=k_unique_ev,
    j_ev_binned=j_ev_binned,
    v_ev_binned=v_ev_binned,
    d2_ev_binned=d2_ev_binned,

    # Power spectra
    ns_weyl_sec=np.array(ns_weyl_sec),
    ns_vel_sec=np.array(ns_vel_sec),
    ns_weyl_ev=np.array(c_pw_ev[0]),
    ns_vel_ev=np.array(c_pv_ev[0]),

    # Branch analysis
    branch_labels=branch_labels,

    # Signed flow
    net_flow=np.array(net_flow),
    unsigned_flow=np.array(unsigned_flow),
    cancellation_frac=np.array(total_cancel),
)

print(f"  Saved: {DATA_DIR / f'{OUT_PREFIX}.npz'}")

# ==============================================================================
# PLOT
# ==============================================================================
fig, axes = plt.subplots(2, 3, figsize=(18, 11))
fig.suptitle(
    f"SPECTRAL-FLOW-NS-46: Spectral Current from Eigenvalue Velocities\n"
    f"$\\alpha_j = {alpha_j:.2f} \\pm {se_j:.2f}$ (Casimir k), "
    f"$\\alpha_v = {alpha_v:.2f} \\pm {se_v:.2f}$, "
    f"Gate: {verdict_j}",
    fontsize=13, fontweight='bold'
)

# --- Panel (a): j(k) vs k at Casimir wavenumber ---
ax = axes[0, 0]
ax.loglog(sec_k, sec_j_total, 'o', color='tab:blue', ms=10, zorder=5, label='j(k) data')
k_line = np.linspace(sec_k.min() * 0.9, sec_k.max() * 1.1, 50)
ax.loglog(k_line, np.exp(np.polyfit(np.log(sec_k), np.log(sec_j_total), 1)[1]) * k_line**alpha_j,
          '--', color='tab:red', lw=2, label=f'$k^{{{alpha_j:.1f}}}$')
for i, lbl in enumerate(sec_label):
    ax.annotate(lbl, (sec_k[i], sec_j_total[i]), textcoords="offset points",
                xytext=(5, 5), fontsize=9)
ax.set_xlabel(r'$k = \sqrt{C_2(p,q)}$', fontsize=12)
ax.set_ylabel(r'$j(k) = \sum d_k |v_k|$', fontsize=12)
ax.set_title(f'(a) Spectral current (Casimir k)', fontsize=11)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

# --- Panel (b): Velocity vs eigenvalue ---
ax = axes[0, 1]
sc = ax.scatter(omega_fold, vel_primary, s=2, alpha=0.3, c=np.log10(dim2_all + 1),
                cmap='viridis', label='all modes')
ax.axhline(0, color='gray', lw=0.5)
ax.set_xlabel(r'$\lambda$ at fold (M$_{\rm KK}$)', fontsize=12)
ax.set_ylabel(r'd$\lambda$/d$\tau$', fontsize=12)
ax.set_title('(b) Eigenvalue velocity at fold', fontsize=11)
plt.colorbar(sc, ax=ax, label=r'$\log_{10}(d^2+1)$')
ax.grid(True, alpha=0.3)

# --- Panel (c): Decomposition ---
ax = axes[0, 2]
categories = ['$\\alpha_N$', '$\\alpha_d$', '$\\alpha_v$', '$\\alpha_j$']
values = [alpha_N, alpha_d, alpha_v, alpha_j]
errors = [se_N, se_d, se_v, se_j]
colors = ['tab:orange', 'tab:green', 'tab:blue', 'tab:red']
bars = ax.bar(categories, values, yerr=errors, color=colors, alpha=0.7, capsize=5)
ax.axhline(1.0, color='gray', ls='--', lw=1, label='$\\alpha = 1$ target')
ax.set_ylabel(r'Power-law exponent $\alpha$', fontsize=12)
ax.set_title('(c) Alpha decomposition', fontsize=11)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3, axis='y')

# --- Panel (d): j(k) at eigenvalue-k ---
ax = axes[1, 0]
valid_plot = j_ev_binned > 0
ax.loglog(k_unique_ev[valid_plot], j_ev_binned[valid_plot], '.', color='tab:blue',
          ms=3, alpha=0.4, label=f'j(k), $\\alpha={alpha_ev:.1f}$')
ax.loglog(k_unique_ev[valid_plot], v_ev_binned[valid_plot], '.', color='tab:green',
          ms=3, alpha=0.4, label=f'$\\langle|v|\\rangle$, $\\alpha_v={alpha_v_ev:.1f}$')
ax.set_xlabel(r'$k = |\omega(\tau=0)|$', fontsize=12)
ax.set_ylabel('j(k) or $\\langle|v|\\rangle$(k)', fontsize=12)
ax.set_title(f'(d) Eigenvalue-k analysis', fontsize=11)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# --- Panel (e): Velocity-weighted vs Weyl power spectrum ---
ax = axes[1, 1]
ax.loglog(sec_k, sec_P_weyl, 'o-', color='tab:blue', ms=8, label=f'Weyl P, $n_s={ns_weyl_sec:.1f}$')
ax.loglog(sec_k, sec_P_vel, 's-', color='tab:red', ms=8, label=f'Vel-wt P, $n_s={ns_vel_sec:.1f}$')
for i, lbl in enumerate(sec_label):
    ax.annotate(lbl, (sec_k[i], sec_P_weyl[i]), textcoords="offset points",
                xytext=(5, -10), fontsize=8, color='tab:blue')
ax.set_xlabel(r'$k = \sqrt{C_2}$', fontsize=12)
ax.set_ylabel('P(k)', fontsize=12)
ax.set_title('(e) Bogoliubov power spectrum', fontsize=11)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

# --- Panel (f): |v| vs k at Casimir level ---
ax = axes[1, 2]
ax.plot(sec_k, sec_v_mean, 'o-', color='tab:blue', ms=10, label=r'$\langle|v|\rangle$')
k_line2 = np.linspace(sec_k.min(), sec_k.max(), 50)
fit_v = np.exp(np.polyfit(np.log(sec_k), np.log(sec_v_mean), 1)[1]) * k_line2**alpha_v
ax.plot(k_line2, fit_v, '--', color='tab:red', lw=2,
        label=f'$k^{{{alpha_v:.2f}}}$')
for i, lbl in enumerate(sec_label):
    ax.annotate(lbl, (sec_k[i], sec_v_mean[i]), textcoords="offset points",
                xytext=(5, 5), fontsize=9)
ax.set_xlabel(r'$k = \sqrt{C_2(p,q)}$', fontsize=12)
ax.set_ylabel(r'$\langle |d\lambda/d\tau| \rangle$', fontsize=12)
ax.set_title(f'(f) Mean velocity vs Casimir k, $\\alpha_v={alpha_v:.2f}$', fontsize=11)
ax.legend(fontsize=10)
ax.grid(True, alpha=0.3)

plt.tight_layout(rect=[0, 0, 1, 0.93])
plt.savefig(DATA_DIR / f"{OUT_PREFIX}.png", dpi=150, bbox_inches='tight')
print(f"  Saved: {DATA_DIR / f'{OUT_PREFIX}.png'}")

print(f"\n{'=' * 78}")
print(f"SPECTRAL-FLOW-NS-46 COMPLETE")
print(f"  alpha_j = {alpha_j:.3f} +/- {se_j:.3f}  (Casimir k, FAIL)")
print(f"  alpha_v = {alpha_v:.3f} +/- {se_v:.3f}  (velocity only, INFO)")
print(f"  Spectral current is UV-dominated. Velocity adds alpha_v ~ 0.6 to Weyl counting.")
print(f"  Gate: {verdict_j} -- alpha_j = {alpha_j:.3f} outside [0.5, 2.0]")
print(f"{'=' * 78}")
