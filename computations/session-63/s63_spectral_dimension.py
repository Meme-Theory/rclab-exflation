#!/usr/bin/env python3
"""
S63 W3-02: SPECTRAL-DIMENSION-63 -- d_s Flow from 992 Eigenvalues

Computes the spectral dimension d_s(t) from the heat kernel of D_K^2 spectrum
on Jensen-deformed SU(3) at the fold (tau=0.19).

Physics:
  K(t) = sum_n d_n exp(-lambda_n^2 t)
  d_s(t) = -2 d(ln K) / d(ln t)

Key structural finding: ALL 992 eigenvalues lie in a NARROW BAND
  omega in [0.82, 2.06] M_KK (omega^2 in [0.67, 4.24])
This is NOT like CDT where eigenvalues span many decades. The narrow band
is a PHYSICAL PROPERTY of the truncated KK spectrum at L_max = 6.

For the heat kernel:
  - t << 1/omega_max^2 ~ 0.24: K(t) -> sum(d_n) = const, d_s -> 0
  - t >> 1/omega_min^2 ~ 1.49: K(t) -> 0 exponentially, d_s -> 2*omega_min^2*t
  - Transition window: 0.2 < t < 2 (less than 1 decade)

The spectral dimension is meaningful ONLY in the transition window.
There is no zero eigenvalue (omega_min > 0), so no constant-K regime at large t.

Inputs:
  computations/session-44/s44_dos_tau.npz (992 KK eigenvalues at fold)
  computations/session-61/s61_trace_formula_geometric.npz (Weyl counting, Seeley-DeWitt)
  computations/session-62/s62_phonon_dispersion_full.npz (coupled spectrum)

Output:
  computations/session-63/s63_spectral_dimension.npz

Gate: SPECTRAL-DIMENSION-63 (INFO: report d_s flow)

Author: phonon-first-cosmologist
Session: S63 W3-02
"""

import sys
import os
import numpy as np
from scipy.optimize import curve_fit

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from canonical_constants import *

# ============================================================
# 1. LOAD DATA
# ============================================================
print("=" * 70)
print("S63 W3-02: SPECTRAL-DIMENSION-63 -- d_s Flow from 992 Eigenvalues")
print("=" * 70)

base = os.path.dirname(__file__)

d44 = np.load(os.path.join(base, 's44_dos_tau.npz'), allow_pickle=True)
omega_fold = d44['tau0.19_all_omega']       # 992 eigenvalues (M_KK units)
dim2_fold = d44['tau0.19_all_dim2']         # Plancherel weight per mode
omega_bi = d44['tau0.00_all_omega']
dim2_bi = d44['tau0.00_all_dim2']

d61 = np.load(os.path.join(base, 's61_trace_formula_geometric.npz'), allow_pickle=True)
a0_gilkey = float(d61['a0_gilkey'])
a2_gilkey_fold = float(d61['a2_gilkey_fold'])
alpha_N_S61 = float(d61['alpha_N'])
alpha_N_PW_S61 = float(d61['alpha_Npw'])

d62 = np.load(os.path.join(base, 's62_phonon_dispersion_full.npz'), allow_pickle=True)
lambda_n_cg = d62['lambda_n']

print(f"\nData loaded:")
print(f"  992-mode fold spectrum: omega in [{omega_fold.min():.6f}, {omega_fold.max():.6f}] M_KK")
print(f"  omega^2 in [{omega_fold.min()**2:.4f}, {omega_fold.max()**2:.4f}] M_KK^2")
print(f"  Bandwidth ratio: {omega_fold.max()**2 / omega_fold.min()**2:.2f}")
print(f"  Plancherel weights: dim^2 in [{dim2_fold.min():.0f}, {dim2_fold.max():.0f}]")
print(f"  Total modes: {len(omega_fold)}, Total Plancherel: {dim2_fold.sum():.0f}")

# ============================================================
# 2. CONSTRUCT HEAT KERNELS
# ============================================================
# Two counting methods:
# (A) Plancherel-weighted: K_PW(t) = sum_i d_i exp(-omega_i^2 t)
#     This is Tr[exp(-D_K^2 t)] on L^2(SU(3)), probes GEOMETRY of SU(3).
# (B) Mode-counted: K_MC(t) = sum_i exp(-omega_i^2 t)
#     Each of the 992 spinor modes counted once.

# Focus the diffusion time on the PHYSICALLY MEANINGFUL region
# where the heat kernel is transitioning (not saturated, not dead)
omega_max = omega_fold.max()
omega_min = omega_fold.min()
t_UV = 1.0 / omega_max**2    # Below: K ~ const (all modes contribute equally)
t_IR = 1.0 / omega_min**2    # Above: K ~ exp(-omega_min^2 t) (exponential decay)

# Extend range for context but focus resolution on the transition
t_arr = np.logspace(-4, 4, 400)

omega2_fold = omega_fold**2
omega2_bi = omega_bi**2

print(f"\nComputing heat kernels over {len(t_arr)} points, t in [1e-4, 1e4]...")
print(f"  Transition window: [{t_UV:.4f}, {t_IR:.4f}] M_KK^{{-2}}")

K_PW_fold = np.array([np.sum(dim2_fold * np.exp(-omega2_fold * t)) for t in t_arr])
K_PW_bi   = np.array([np.sum(dim2_bi   * np.exp(-omega2_bi   * t)) for t in t_arr])
K_MC_fold = np.array([np.sum(np.exp(-omega2_fold * t)) for t in t_arr])
K_MC_bi   = np.array([np.sum(np.exp(-omega2_bi   * t)) for t in t_arr])

# CG(24) base: 32 graph eigenvalues
lambda2_cg = lambda_n_cg**2
K_base = np.array([np.sum(np.exp(-lambda2_cg * t)) for t in t_arr])

print(f"  K_PW_fold: [{K_PW_fold.min():.4e}, {K_PW_fold.max():.4e}]")
print(f"  K_MC_fold: [{K_MC_fold.min():.4e}, {K_MC_fold.max():.4e}]")

# ============================================================
# 3. COMPUTE SPECTRAL DIMENSION
# ============================================================
# d_s(t) = -2 d(ln K)/d(ln t)
# Use central differences on the log-log scale.
# CRITICAL: avoid log(0) and handle the exponential decay regime.

def compute_ds(K, t):
    """Compute spectral dimension, handling zero K values."""
    ln_t = np.log(t)
    # Mask out regions where K is effectively zero
    valid = K > 1e-300
    ds = np.full(len(t), np.nan)
    # Use numpy gradient for smooth derivative
    if valid.sum() > 3:
        ln_K = np.log(np.maximum(K, 1e-300))
        dln_K = np.gradient(ln_K, ln_t)
        ds = -2.0 * dln_K
        ds[~valid] = np.nan
    return ds

ds_PW_fold = compute_ds(K_PW_fold, t_arr)
ds_PW_bi   = compute_ds(K_PW_bi, t_arr)
ds_MC_fold = compute_ds(K_MC_fold, t_arr)
ds_MC_bi   = compute_ds(K_MC_bi, t_arr)
ds_base    = compute_ds(K_base, t_arr)

# Clip extreme values in the asymptotic regime (these are not physical)
# The true behavior at large t is d_s -> 2 omega_min^2 t (linear growth),
# which is the artifact of a gapped spectrum with no zero mode.
# This is NOT a dimensional flow but simple exponential decay of K.

print(f"\nSpectral dimension computed.")
# Report in the trustworthy window
mask_trust = (t_arr > t_UV) & (t_arr < t_IR * 2)
if mask_trust.sum() > 0:
    ds_trust = ds_PW_fold[mask_trust]
    t_trust = t_arr[mask_trust]
    valid_trust = np.isfinite(ds_trust)
    if valid_trust.sum() > 0:
        print(f"  d_s(PW fold) in trustworthy window [{t_UV:.3f}, {t_IR*2:.3f}]:")
        print(f"    range: [{ds_trust[valid_trust].min():.4f}, {ds_trust[valid_trust].max():.4f}]")
        print(f"    mean:  {ds_trust[valid_trust].mean():.4f}")

# ============================================================
# 4. SHIFTED HEAT KERNEL: SUBTRACT MINIMUM EIGENVALUE
# ============================================================
# The standard spectral dimension formula assumes the Laplacian has a
# zero mode. On a compact manifold without boundary, the Laplacian
# DOES have zero mode, but our TRUNCATED spectrum has omega_min > 0.
#
# For the FULL D_K^2 on SU(3): there is no zero mode because D_K is
# the internal Dirac operator with a mass gap (omega_min = C2(0,0)/R^2 > 0).
#
# The physically correct heat kernel for spectral dimension should
# use the SHIFTED operator: D_K^2 - omega_min^2.
# This gives: K_shifted(t) = exp(omega_min^2 t) * K(t) = sum d_n exp(-(omega_n^2 - omega_min^2)*t)
#
# The shifted spectrum has eigenvalue 0 for the lowest mode, and
# the spectral dimension of the shifted operator probes the actual
# geometry of the eigenvalue distribution above the gap.

print(f"\n{'='*70}")
print("4. SHIFTED HEAT KERNEL (subtract gap)")
print("=" * 70)

omega2_min_fold = omega_fold.min()**2
omega2_min_bi = omega_bi.min()**2

# Shifted eigenvalues
omega2_shift_fold = omega2_fold - omega2_min_fold
omega2_shift_bi = omega2_bi - omega2_min_bi

print(f"  Gap subtracted: omega_min^2(fold) = {omega2_min_fold:.6f}")
print(f"  Gap subtracted: omega_min^2(bi)   = {omega2_min_bi:.6f}")
print(f"  Shifted omega^2 range (fold): [0, {omega2_shift_fold.max():.4f}]")

# Compute shifted heat kernels
K_PW_shift = np.array([np.sum(dim2_fold * np.exp(-omega2_shift_fold * t)) for t in t_arr])
K_MC_shift = np.array([np.sum(np.exp(-omega2_shift_fold * t)) for t in t_arr])
K_PW_shift_bi = np.array([np.sum(dim2_bi * np.exp(-omega2_shift_bi * t)) for t in t_arr])

# Shifted spectral dimension
ds_PW_shift = compute_ds(K_PW_shift, t_arr)
ds_MC_shift = compute_ds(K_MC_shift, t_arr)
ds_PW_shift_bi = compute_ds(K_PW_shift_bi, t_arr)

# Now at large t, K_shifted -> d_0 (degeneracy of lowest mode) = const
# so d_s -> 0 (correct for compact manifold)
# At small t, K_shifted -> sum(d_n) (all modes), d_s -> 0
# In between, d_s shows the actual spectral dimension

print(f"\n  Shifted d_s(PW fold):")
# Report at key t values
key_t = [1e-3, 1e-2, 5e-2, 0.1, 0.2, 0.3, 0.5, 0.7, 1.0, 1.5, 2.0, 3.0, 5.0, 10.0, 50.0]
print(f"  {'t':>10s}  {'d_s(PW)':>10s}  {'d_s(MC)':>10s}  {'d_s(PW,bi)':>10s}")
print(f"  {'-'*50}")
for tk in key_t:
    idx = np.argmin(np.abs(t_arr - tk))
    v_pw = ds_PW_shift[idx] if np.isfinite(ds_PW_shift[idx]) else 0
    v_mc = ds_MC_shift[idx] if np.isfinite(ds_MC_shift[idx]) else 0
    v_bi = ds_PW_shift_bi[idx] if np.isfinite(ds_PW_shift_bi[idx]) else 0
    print(f"  {t_arr[idx]:10.4e}  {v_pw:10.4f}  {v_mc:10.4f}  {v_bi:10.4f}")

# Find peak d_s in the shifted spectrum
valid_shift = np.isfinite(ds_PW_shift)
if valid_shift.sum() > 0:
    idx_peak_shift = np.argmax(ds_PW_shift[valid_shift])
    # Map back to original indices
    valid_indices = np.where(valid_shift)[0]
    idx_peak_shift = valid_indices[idx_peak_shift]
    print(f"\n  Peak d_s(PW, shifted, fold) = {ds_PW_shift[idx_peak_shift]:.4f} at t = {t_arr[idx_peak_shift]:.4e}")

    idx_peak_mc_shift = np.where(np.isfinite(ds_MC_shift))[0]
    if len(idx_peak_mc_shift) > 0:
        imax = idx_peak_mc_shift[np.argmax(ds_MC_shift[idx_peak_mc_shift])]
        print(f"  Peak d_s(MC, shifted, fold) = {ds_MC_shift[imax]:.4f} at t = {t_arr[imax]:.4e}")

    idx_peak_bi_shift = np.where(np.isfinite(ds_PW_shift_bi))[0]
    if len(idx_peak_bi_shift) > 0:
        imax = idx_peak_bi_shift[np.argmax(ds_PW_shift_bi[idx_peak_bi_shift])]
        print(f"  Peak d_s(PW, shifted, bi)   = {ds_PW_shift_bi[imax]:.4f} at t = {t_arr[imax]:.4e}")

# ============================================================
# 5. PLATEAU IDENTIFICATION IN SHIFTED SPECTRUM
# ============================================================
print(f"\n{'='*70}")
print("5. PLATEAU IDENTIFICATION (shifted spectrum)")
print("=" * 70)

def find_plateaus(ds, ln_t, threshold=0.08, min_width=8):
    """Find plateaus where |d(d_s)/d(ln_t)| < threshold."""
    valid = np.isfinite(ds)
    if valid.sum() < 10:
        return []
    dds = np.gradient(ds, ln_t)
    dds[~valid] = 999
    plateaus = []
    in_plateau = False
    start = 0
    for j in range(len(ds)):
        if valid[j] and abs(dds[j]) < threshold:
            if not in_plateau:
                start = j
                in_plateau = True
        else:
            if in_plateau and (j - start) >= min_width:
                mid = (start + j) // 2
                plateaus.append({
                    't_start': np.exp(ln_t[start]),
                    't_end': np.exp(ln_t[j-1]),
                    't_mid': np.exp(ln_t[mid]),
                    'd_s': np.nanmean(ds[start:j]),
                    'd_s_std': np.nanstd(ds[start:j]),
                    'width': ln_t[j-1] - ln_t[start],
                })
            in_plateau = False
    if in_plateau and (len(ds) - start) >= min_width:
        plateaus.append({
            't_start': np.exp(ln_t[start]),
            't_end': np.exp(ln_t[-1]),
            't_mid': np.exp(ln_t[(start + len(ds)) // 2]),
            'd_s': np.nanmean(ds[start:]),
            'd_s_std': np.nanstd(ds[start:]),
            'width': ln_t[-1] - ln_t[start],
        })
    return plateaus

ln_t = np.log(t_arr)
plateaus_shift = find_plateaus(ds_PW_shift, ln_t)
plateaus_mc_shift = find_plateaus(ds_MC_shift, ln_t)

print(f"\n--- PW shifted, fold ---")
for i, p in enumerate(plateaus_shift):
    print(f"  Plateau {i}: d_s = {p['d_s']:.4f} +/- {p['d_s_std']:.4f}, "
          f"t in [{p['t_start']:.2e}, {p['t_end']:.2e}], "
          f"width = {p['width']:.2f} ln-decades")

print(f"\n--- MC shifted, fold ---")
for i, p in enumerate(plateaus_mc_shift):
    print(f"  Plateau {i}: d_s = {p['d_s']:.4f} +/- {p['d_s_std']:.4f}, "
          f"t in [{p['t_start']:.2e}, {p['t_end']:.2e}], "
          f"width = {p['width']:.2f} ln-decades")

# ============================================================
# 6. WEYL-LAW SPECTRAL DIMENSION
# ============================================================
print(f"\n{'='*70}")
print("6. WEYL-LAW SPECTRAL DIMENSION")
print("=" * 70)

# The Weyl law approach: N(omega < Omega) ~ Omega^{d_s}
# gives the spectral dimension from eigenvalue counting.
# This is independent of the heat kernel and provides a cross-check.

# For D_K eigenvalues (Dirac operator):
# N(|D_K| < Lambda) ~ Lambda^d on d-dimensional manifold
# So alpha_N = d_s(Weyl)

# From S61: alpha_N = 2.977 from cum_N fit
# This is the Weyl spectral dimension of the TRUNCATED spectrum.

# Direct computation: sort eigenvalues and fit N(omega)
omega_sorted = np.sort(omega_fold)
N_cumulative = np.arange(1, len(omega_sorted) + 1)

# Fit ln N = d_W * ln omega + const
ln_omega = np.log(omega_sorted)
ln_N = np.log(N_cumulative)
# Use only middle 80% to avoid edge effects
n10 = len(omega_sorted) // 10
n90 = len(omega_sorted) * 9 // 10
coeffs_weyl = np.polyfit(ln_omega[n10:n90], ln_N[n10:n90], 1)
d_s_weyl = coeffs_weyl[0]

print(f"  Direct Weyl fit: d_s(Weyl) = {d_s_weyl:.4f}")
print(f"  S61 Weyl growth alpha_N = {alpha_N_S61:.4f}")
print(f"  PW-weighted Weyl growth alpha_N_PW = {alpha_N_PW_S61:.4f}")

# PW-weighted Weyl law: N_PW(omega < Omega) = sum_{omega_i < Omega} d_i
# Sort by omega and compute cumulative PW sum
sort_idx = np.argsort(omega_fold)
omega_sorted_pw = omega_fold[sort_idx]
dim2_sorted = dim2_fold[sort_idx]
N_PW_cumulative = np.cumsum(dim2_sorted)

coeffs_weyl_pw = np.polyfit(np.log(omega_sorted_pw[n10:n90]),
                             np.log(N_PW_cumulative[n10:n90]), 1)
d_s_weyl_pw = coeffs_weyl_pw[0]
print(f"  Direct PW Weyl fit: d_s(Weyl,PW) = {d_s_weyl_pw:.4f}")

# Corrected spectral dimension: for Dirac operator on d-dim manifold
# N(|D| < Lambda) ~ Lambda^d (mode-counted)
# N_PW(|D| < Lambda) ~ Lambda^{d+2rank} (PW adds dim^2 ~ Lambda^{2rank})
# For SU(3), rank = 2, so d_PW = d + 4
# But at truncation L=6, the asymptotic regime may not be reached.

# The difference between d_s(Weyl) and d_s(Weyl,PW) tells us the effective
# Plancherel growth rate, which is related to the rank of the group.
delta_weyl = d_s_weyl_pw - d_s_weyl
print(f"\n  Plancherel growth contribution: {delta_weyl:.4f}")
print(f"  Expected for rank-2 group: ~4 (2*rank)")
print(f"  Observed: {delta_weyl:.4f}")

# ============================================================
# 7. S57 ANOMALOUS EXPONENT CONNECTION
# ============================================================
print(f"\n{'='*70}")
print("7. S57 ANOMALOUS EXPONENT alpha = -1.84")
print("=" * 70)

alpha_S57 = -1.84  # (local)

# The anomalous exponent alpha = -1.84 describes the gap scaling
# Delta_N ~ N^alpha as a function of cell count N.
# This is the BCS gap on N cells of the CG(24) tessellation.
#
# On a d_s-dimensional discrete geometry:
# - Return probability: P(N) ~ N^{-d_s/d_w} with d_w = 2 (walk dimension)
#   Paper 19 confirms d_w = 2 universally for these geometries.
# - So P(N) ~ N^{-d_s/2}
# - The BCS gap depends on the DOS which goes as P(N)^{-1}:
#   Delta ~ exp(-1/(V * g(E_F))) where g ~ E_F^{d_s/2 - 1}
#
# More directly, from the Weyl counting on the CG(24) graph (N=32 vertices):
# The gap scales as Delta_N ~ N^alpha implies the eigenvalue density
# has an anomalous scaling. On a regular d-dim lattice, the gap at
# the N-th level scales as Delta ~ N^{-1/d_s}.
# So alpha = -1/d_s => d_s = -1/alpha = 1/1.84 = 0.543
# BUT: this is the spectral dimension of the GRAPH (base), not the fiber.
#
# Alternatively, if alpha refers to the return probability exponent:
# P(t) ~ t^{-d_s/2} => d_s = -2 alpha = 3.68
# This was the S57 interpretation.

# Compute the return probability exponent from the SHIFTED heat kernel
# P(t) = K_shift(t) / K_shift(0) (normalized)
K_shift_0 = K_PW_shift[0]
P_shift = K_PW_shift / K_shift_0

# Fit P(t) ~ t^{-beta} in the mid regime
mask_mid = (t_arr > 0.3) & (t_arr < 5.0) & (P_shift > 1e-10) & np.isfinite(P_shift)
if mask_mid.sum() > 5:
    ln_P = np.log(P_shift[mask_mid])
    ln_t_mid = np.log(t_arr[mask_mid])
    coeffs_P = np.polyfit(ln_t_mid, ln_P, 1)
    beta_return = -coeffs_P[0]
    d_s_return = 2 * beta_return
    print(f"  Return probability: P(t) ~ t^(-{beta_return:.4f}) for t in [0.3, 5]")
    print(f"  => d_s(return) = 2*beta = {d_s_return:.4f}")
else:
    beta_return = np.nan
    d_s_return = np.nan
    print(f"  Insufficient data for return probability fit")

print(f"\n  S57 alpha = {alpha_S57}:")
print(f"  Interpretation 1: alpha = -1/d_s => d_s = {-1/alpha_S57:.4f} (gap scaling)")
print(f"  Interpretation 2: alpha = -d_s/2 => d_s = {-2*alpha_S57:.4f} (return probability)")
print(f"  Our measured d_s(return) = {d_s_return:.4f}")

# ============================================================
# 8. TAU SWEEP: d_s ALONG THE TRANSIT
# ============================================================
print(f"\n{'='*70}")
print("8. TAU SWEEP: d_s(tau) AT FIXED t")
print("=" * 70)

# Compute d_s at a fixed diffusion time t* for each tau value
# This shows how the spectral dimension changes during the Jensen deformation
tau_values = [0.0, 0.05, 0.10, 0.15, 0.19]
t_star = 0.5  # Diffusion time in the middle of the transition window  # (local)

ds_vs_tau = []
peak_ds_vs_tau = []

for tau_val in tau_values:
    key_omega = f'tau{tau_val:.2f}_all_omega'
    key_dim2 = f'tau{tau_val:.2f}_all_dim2'
    omega_tau = d44[key_omega]
    dim2_tau = d44[key_dim2]

    # Shifted eigenvalues
    omega2_tau = omega_tau**2
    omega2_min_tau = omega2_tau.min()
    omega2_shift_tau = omega2_tau - omega2_min_tau

    # Heat kernel at t_star
    K_tau = np.array([np.sum(dim2_tau * np.exp(-omega2_shift_tau * t)) for t in t_arr])
    ds_tau = compute_ds(K_tau, t_arr)

    # Value at t_star
    idx_star = np.argmin(np.abs(t_arr - t_star))
    ds_at_star = ds_tau[idx_star] if np.isfinite(ds_tau[idx_star]) else 0
    ds_vs_tau.append(ds_at_star)

    # Peak value
    valid_tau = np.isfinite(ds_tau)
    peak_ds = ds_tau[valid_tau].max() if valid_tau.sum() > 0 else 0
    peak_ds_vs_tau.append(peak_ds)

    print(f"  tau = {tau_val:.2f}: d_s(t*={t_star}) = {ds_at_star:.4f}, peak d_s = {peak_ds:.4f}, "
          f"omega_min = {omega_tau.min():.6f}, BW = {omega_tau.max()-omega_tau.min():.4f}")

ds_vs_tau = np.array(ds_vs_tau)
peak_ds_vs_tau = np.array(peak_ds_vs_tau)
tau_sweep = np.array(tau_values)

# ============================================================
# 9. CG(24) BASE SPECTRAL DIMENSION
# ============================================================
print(f"\n{'='*70}")
print("9. CG(24) BASE SPECTRAL DIMENSION")
print("=" * 70)

# The CG(24) graph has 32 vertices. Its D_K eigenvalues from S62:
# lambda_n_cg = 32 values.
# The graph has a zero mode (lambda_0 = 0) so the heat kernel
# approaches d_0 = 1 at large t.

print(f"  CG(24) eigenvalues (32):")
print(f"    zero mode: lambda_0 = {lambda_n_cg[0]:.6f}")
print(f"    gap: lambda_1 = {lambda_n_cg[1]:.6f}")
print(f"    max: lambda_max = {lambda_n_cg[-1]:.6f}")

# For the graph, also compute with shifted spectrum (subtract zero mode)
lambda2_shift_cg = lambda_n_cg**2  # zero mode is already ~0
K_base_shift = np.array([np.sum(np.exp(-lambda2_shift_cg * t)) for t in t_arr])
ds_base_shift = compute_ds(K_base_shift, t_arr)

# Find peak of graph d_s
valid_base = np.isfinite(ds_base_shift)
if valid_base.sum() > 0:
    idx_peak_base = np.where(valid_base)[0][np.argmax(ds_base_shift[valid_base])]
    print(f"  Peak d_s(base) = {ds_base_shift[idx_peak_base]:.4f} at t = {t_arr[idx_peak_base]:.4e}")
    print(f"  For reference: a random 3D lattice has d_s = 3")
    print(f"  CG(24) is a quotient of S^3, expected d_s ~ 3")

# ============================================================
# 10. PRODUCT GEOMETRY d_s = FIBER + BASE
# ============================================================
print(f"\n{'='*70}")
print("10. PRODUCT GEOMETRY d_s")
print("=" * 70)

# On a product M = M_base x M_fiber:
# K_product(t) = K_base(t) * K_fiber(t)
# d_s^product = d_s^base + d_s^fiber
# This is exact when the spectra are independent.

ds_product = ds_PW_shift + ds_base_shift

valid_prod = np.isfinite(ds_product)
if valid_prod.sum() > 0:
    idx_peak_prod = np.where(valid_prod)[0][np.argmax(ds_product[valid_prod])]
    print(f"  Peak d_s(product) = {ds_product[idx_peak_prod]:.4f} at t = {t_arr[idx_peak_prod]:.4e}")
    print(f"  = d_s(fiber) + d_s(base)")
    print(f"  = {ds_PW_shift[idx_peak_prod]:.4f} + {ds_base_shift[idx_peak_prod]:.4f}")

# ============================================================
# 11. CDT FIT
# ============================================================
print(f"\n{'='*70}")
print("11. CDT FUNCTIONAL FORM FIT")
print("=" * 70)

# Try fitting d_s(t) = a - b/(t + c) to the shifted PW fold spectrum
# in the regime where d_s is varying

mask_fit = np.isfinite(ds_PW_shift) & (ds_PW_shift > 0.1) & (ds_PW_shift < 20)
cdt_a, cdt_b, cdt_c = np.nan, np.nan, np.nan
if mask_fit.sum() > 5:
    def cdt_func(x, a, b, c):
        return a - b / (np.exp(x) + c)
    try:
        popt, pcov = curve_fit(cdt_func, ln_t[mask_fit], ds_PW_shift[mask_fit],
                               p0=[4.0, 2.0, 0.5], maxfev=10000)
        cdt_a, cdt_b, cdt_c = popt
        resid = ds_PW_shift[mask_fit] - cdt_func(ln_t[mask_fit], *popt)
        rmse = np.sqrt(np.mean(resid**2))
        print(f"  d_s(t) = {cdt_a:.4f} - {cdt_b:.4f}/(t + {cdt_c:.4f})")
        print(f"  RMSE = {rmse:.4f}")
        print(f"  IR asymptote: d_s(t->inf) = {cdt_a:.4f}")
        print(f"  UV asymptote: d_s(t->0) = {cdt_a - cdt_b/cdt_c:.4f}")
        print(f"\n  CDT comparison (AJL, Paper 20):")
        print(f"    CDT: d_s = 4.02 - 119/(sigma + 54)")
        print(f"    CDT IR: d_s = 4.02, CDT UV: d_s = 1.80")
        print(f"    Ours: IR = {cdt_a:.2f}, UV = {cdt_a - cdt_b/cdt_c:.2f}")
    except Exception as e:
        print(f"  CDT fit failed: {e}")

# ============================================================
# 12. SEELEY-DEWITT PREDICTION
# ============================================================
print(f"\n{'='*70}")
print("12. SEELEY-DEWITT PREDICTION (d=8, continuum)")
print("=" * 70)

# On a smooth 8-dimensional manifold:
# K(t) = (4 pi t)^{-4} [a_0 + a_2 t + a_4 t^2 + ...]
# d_s(t) = 8 - 2t(a_2 + 2 a_4 t)/(a_0 + a_2 t + a_4 t^2)
#
# Using canonical constants: a0_fold, a2_fold, a4_fold
a0 = a0_fold  # from canonical_constants
a2 = a2_fold
a4 = a4_fold

t_SD = np.logspace(-3, 1, 200)
numer_SD = a0 + a2 * t_SD + a4 * t_SD**2
ds_SD = 8.0 - 2.0 * t_SD * (a2 + 2 * a4 * t_SD) / numer_SD

print(f"  Seeley-DeWitt coefficients (from canonical_constants):")
print(f"    a_0 = {a0:.2f}")
print(f"    a_2 = {a2:.2f}")
print(f"    a_4 = {a4:.2f}")
print(f"  d_s(SD, t=0) = 8.000 (by construction)")
print(f"  d_s(SD, t=0.01) = {ds_SD[np.argmin(np.abs(t_SD - 0.01))]:.4f}")
print(f"  d_s(SD, t=0.1) = {ds_SD[np.argmin(np.abs(t_SD - 0.1))]:.4f}")
print(f"  d_s(SD, t=1.0) = {ds_SD[np.argmin(np.abs(t_SD - 1.0))]:.4f}")

# The Seeley-DeWitt predicts d_s = 8 at small t, then drops as t grows
# Our TRUNCATED spectrum cannot reproduce this because:
# 1. Only 992 modes (finite, not continuous)
# 2. All eigenvalues in narrow band (no small eigenvalues below omega_min)
# 3. Weyl growth ~ Lambda^3, not Lambda^8

print(f"\n  WHY d_s != 8 in the discrete spectrum:")
print(f"  The Seeley-DeWitt expansion requires the heat kernel to resolve")
print(f"  ALL length scales, including scales much smaller than the lowest")
print(f"  eigenvalue spacing. At L_max = 6, we have {len(omega_fold)} modes with")
print(f"  max eigenvalue {omega_max:.4f}. The continuum limit needs L -> inf.")
print(f"  The Weyl exponent alpha_N = {alpha_N_S61:.3f} measures how FAST new modes")
print(f"  appear as L increases. For d_s = 8, we need alpha_N -> 8.")
print(f"  At L=6, alpha_N = {alpha_N_S61:.3f}: the approach is SLOW.")

# ============================================================
# 13. SAVE RESULTS
# ============================================================
print(f"\n{'='*70}")
print("13. SAVING RESULTS")
print("=" * 70)

outpath = os.path.join(base, 's63_spectral_dimension.npz')

# Key metrics for the verdict
idx_peak_pw_shift = np.where(np.isfinite(ds_PW_shift))[0]
peak_ds_pw_shift = ds_PW_shift[idx_peak_pw_shift].max() if len(idx_peak_pw_shift) > 0 else np.nan
peak_t_pw_shift = t_arr[idx_peak_pw_shift[np.argmax(ds_PW_shift[idx_peak_pw_shift])]] if len(idx_peak_pw_shift) > 0 else np.nan

idx_peak_mc_shift_arr = np.where(np.isfinite(ds_MC_shift))[0]
peak_ds_mc_shift = ds_MC_shift[idx_peak_mc_shift_arr].max() if len(idx_peak_mc_shift_arr) > 0 else np.nan

idx_peak_base_arr = np.where(np.isfinite(ds_base_shift))[0]
peak_ds_base = ds_base_shift[idx_peak_base_arr].max() if len(idx_peak_base_arr) > 0 else np.nan

idx_peak_prod_arr = np.where(np.isfinite(ds_product))[0]
peak_ds_prod = ds_product[idx_peak_prod_arr].max() if len(idx_peak_prod_arr) > 0 else np.nan

save_dict = {
    # Diffusion time
    't_arr': t_arr,
    'ln_t': ln_t,

    # Raw heat kernels
    'K_PW_fold': K_PW_fold,
    'K_PW_bi': K_PW_bi,
    'K_MC_fold': K_MC_fold,
    'K_base': K_base,

    # Shifted heat kernels
    'K_PW_shift': K_PW_shift,
    'K_MC_shift': K_MC_shift,
    'K_PW_shift_bi': K_PW_shift_bi,

    # Raw spectral dimensions
    'ds_PW_fold': ds_PW_fold,
    'ds_PW_bi': ds_PW_bi,
    'ds_MC_fold': ds_MC_fold,

    # Shifted spectral dimensions (PRIMARY RESULTS)
    'ds_PW_shift': ds_PW_shift,
    'ds_MC_shift': ds_MC_shift,
    'ds_PW_shift_bi': ds_PW_shift_bi,
    'ds_base': ds_base_shift,
    'ds_product': ds_product,

    # Seeley-DeWitt prediction
    't_SD': t_SD,
    'ds_SD': ds_SD,

    # Weyl spectral dimension
    'd_s_weyl': np.array(d_s_weyl),
    'd_s_weyl_pw': np.array(d_s_weyl_pw),
    'alpha_N_S61': np.array(alpha_N_S61),
    'alpha_N_PW_S61': np.array(alpha_N_PW_S61),

    # Return probability exponent
    'beta_return': np.array(beta_return),
    'd_s_return': np.array(d_s_return),

    # Tau sweep
    'tau_sweep': tau_sweep,
    'ds_vs_tau': ds_vs_tau,
    'peak_ds_vs_tau': peak_ds_vs_tau,

    # CDT fit
    'cdt_a': np.array(cdt_a),
    'cdt_b': np.array(cdt_b),
    'cdt_c': np.array(cdt_c),

    # Key numbers
    'peak_ds_PW_shift': np.array(peak_ds_pw_shift),
    'peak_t_PW_shift': np.array(peak_t_pw_shift),
    'peak_ds_MC_shift': np.array(peak_ds_mc_shift),
    'peak_ds_base': np.array(peak_ds_base),
    'peak_ds_product': np.array(peak_ds_prod),
    'omega_max_fold': np.array(omega_max),
    'omega_min_fold': np.array(omega_min),
    't_UV_cutoff': np.array(t_UV),
    't_IR_cutoff': np.array(t_IR),

    # Gate
    'gate_name': np.array('SPECTRAL-DIMENSION-63'),
    'gate_verdict': np.array('INFO'),
}

np.savez(outpath, **save_dict)
print(f"  Saved: {outpath}")

# ============================================================
# 14. PLOT
# ============================================================
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle('S63 W3-02: Spectral Dimension Flow from 992 KK Eigenvalues', fontsize=14, y=0.98)

# ---- Panel 1: Shifted d_s (primary result) ----
ax = axes[0, 0]
ax.semilogx(t_arr, ds_PW_shift, 'b-', lw=2, label='PW fold (shifted)')
ax.semilogx(t_arr, ds_MC_shift, 'b--', lw=1.5, label='MC fold (shifted)')
ax.semilogx(t_arr, ds_PW_shift_bi, 'r-', lw=1.5, label='PW bi-inv (shifted)')
ax.axhline(y=8, color='gray', ls=':', alpha=0.5, label='d=8 (SU(3))')
ax.axhline(y=4, color='green', ls=':', alpha=0.5, label='d=4 (CDT IR)')
ax.axhline(y=2, color='orange', ls=':', alpha=0.5, label='d=2 (CDT UV)')
ax.axhline(y=alpha_N_S61, color='purple', ls=':', alpha=0.5,
           label=f'd={alpha_N_S61:.2f} (Weyl)')
ax.set_xlabel('Diffusion time t [M_KK^{-2}]')
ax.set_ylabel('d_s(t)')
ax.set_title('Shifted Spectral Dimension (gap-subtracted)')
ax.legend(fontsize=7, loc='upper right')
ax.set_ylim(-0.5, 10)
ax.set_xlim(1e-3, 1e3)
ax.grid(True, alpha=0.3)

# ---- Panel 2: Raw d_s (shows truncation artifact) ----
ax = axes[0, 1]
# Clip raw d_s to reasonable range for display
ds_raw_clip = np.clip(ds_PW_fold, -1, 50)
ax.semilogx(t_arr, ds_raw_clip, 'b-', lw=2, label='PW fold (raw)')
ds_raw_bi_clip = np.clip(ds_PW_bi, -1, 50)
ax.semilogx(t_arr, ds_raw_bi_clip, 'r-', lw=1.5, label='PW bi-inv (raw)')
ax.axhline(y=8, color='gray', ls=':', alpha=0.5)
ax.axvline(x=t_UV, color='blue', ls='--', alpha=0.5, label=f't_UV={t_UV:.3f}')
ax.axvline(x=t_IR, color='red', ls='--', alpha=0.5, label=f't_IR={t_IR:.3f}')
ax.set_xlabel('Diffusion time t')
ax.set_ylabel('d_s(t) [raw, unshifted]')
ax.set_title('Raw d_s (shows gap artifact at large t)')
ax.legend(fontsize=7)
ax.set_ylim(-1, 20)
ax.grid(True, alpha=0.3)

# ---- Panel 3: Product geometry ----
ax = axes[0, 2]
ax.semilogx(t_arr, ds_PW_shift, 'b-', lw=1.5, label='d_s(fiber)')
ax.semilogx(t_arr, ds_base_shift, 'g-', lw=1.5, label='d_s(base, CG(24))')
ax.semilogx(t_arr, ds_product, 'k-', lw=2, label='d_s(product)')
ax.axhline(y=8, color='gray', ls=':', alpha=0.5, label='d=8')
ax.axhline(y=4, color='green', ls=':', alpha=0.5, label='d=4')
ax.set_xlabel('Diffusion time t')
ax.set_ylabel('d_s(t)')
ax.set_title('Product: Fiber + Base')
ax.legend(fontsize=7)
ax.set_ylim(-0.5, 14)
ax.set_xlim(1e-3, 1e3)
ax.grid(True, alpha=0.3)

# ---- Panel 4: Heat kernels ----
ax = axes[1, 0]
ax.loglog(t_arr, K_PW_fold, 'b-', lw=2, label='K_PW(fold)')
ax.loglog(t_arr, K_MC_fold, 'b--', lw=1.5, label='K_MC(fold)')
ax.loglog(t_arr, K_PW_shift, 'r-', lw=1.5, label='K_PW(shifted)')
ax.loglog(t_arr, K_base, 'g-', lw=1.5, label='K(base)')
ax.set_xlabel('t')
ax.set_ylabel('K(t)')
ax.set_title('Heat Kernels')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)

# ---- Panel 5: Seeley-DeWitt comparison ----
ax = axes[1, 1]
ax.semilogx(t_SD, ds_SD, 'k-', lw=2, label='Seeley-DeWitt (d=8)')
ax.semilogx(t_arr, ds_PW_shift, 'b-', lw=1.5, label='Discrete (shifted)')
ax.axhline(y=8, color='gray', ls=':', alpha=0.5)
ax.axhline(y=alpha_N_S61, color='purple', ls=':', alpha=0.5)
ax.set_xlabel('t')
ax.set_ylabel('d_s(t)')
ax.set_title('Seeley-DeWitt vs Discrete')
ax.legend(fontsize=7)
ax.set_ylim(-0.5, 10)
ax.set_xlim(1e-3, 1e2)
ax.grid(True, alpha=0.3)

# ---- Panel 6: Tau sweep ----
ax = axes[1, 2]
ax.plot(tau_sweep, ds_vs_tau, 'bo-', lw=2, label=f'd_s(t*={t_star})')
ax.plot(tau_sweep, peak_ds_vs_tau, 'rs-', lw=2, label='peak d_s')
ax.axhline(y=alpha_N_S61, color='purple', ls=':', alpha=0.5)
ax.set_xlabel('tau (Jensen deformation)')
ax.set_ylabel('d_s')
ax.set_title('d_s vs tau (transit sweep)')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plotpath = os.path.join(base, 's63_spectral_dimension.png')
plt.savefig(plotpath, dpi=150)
print(f"  Plot saved: {plotpath}")

# ============================================================
# 15. FINAL VERDICT
# ============================================================
print(f"\n{'='*70}")
print("GATE: SPECTRAL-DIMENSION-63 = INFO")
print("=" * 70)

print(f"""
VERDICT: INFO (d_s flow computed, structural findings reported)

KEY NUMBERS:
  1. Peak d_s(PW, shifted, fold) = {peak_ds_pw_shift:.4f} at t = {peak_t_pw_shift:.4e}
  2. Peak d_s(MC, shifted, fold) = {peak_ds_mc_shift:.4f}
  3. Peak d_s(base, CG(24))      = {peak_ds_base:.4f}
  4. Peak d_s(product)            = {peak_ds_prod:.4f}
  5. Weyl spectral dim (mode)     = {d_s_weyl:.4f}
  6. Weyl spectral dim (PW)       = {d_s_weyl_pw:.4f}
  7. Return probability exponent   = {d_s_return:.4f}
  8. S61 alpha_N (Weyl growth)     = {alpha_N_S61:.4f}

STRUCTURAL FINDINGS:
  A. NARROW-BAND SPECTRUM: All 992 eigenvalues lie in [0.82, 2.06] M_KK
     (bandwidth ratio 6.3:1). This confines the d_s signal to less than
     1 decade of diffusion time. NOT like CDT where eigenvalues span
     many decades.

  B. TRUNCATION DOMINANCE: The Weyl growth alpha_N = {alpha_N_S61:.3f} ~ 3 reflects
     the effective dimension of the TRUNCATED spectrum at L=6.
     The continuum value d_s = 8 requires L -> infinity.
     At L=6, the spectral dimension is locked to ~{peak_ds_pw_shift:.1f}, well below 8.

  C. JENSEN DEFORMATION EFFECT: d_s changes with tau across the transit:
     tau=0 (bi-inv): peak d_s ~ {peak_ds_vs_tau[0]:.2f}
     tau=0.19 (fold): peak d_s ~ {peak_ds_vs_tau[-1]:.2f}
     The deformation MODIFIES d_s but does not change its order.

  D. S57 ALPHA CONNECTION: The anomalous exponent alpha = -1.84 yields
     d_s = 3.68 under the return-probability interpretation, which is
     consistent with the Weyl dimension alpha_N ~ 3.

CDT COMPARISON:
  CDT (Paper 20): d_s: 4.02 -> 1.80 (4D spacetime, large Monte Carlo)
  This framework: d_s ~ {peak_ds_pw_shift:.1f} (truncated, 8D internal space)
  The comparison is NOT direct because:
    1. CDT uses millions of simplices; we have 992 modes
    2. CDT probes a 4D geometry; we probe 8D internal SU(3)
    3. CDT has a zero mode; our spectrum is gapped
  A meaningful CDT comparison requires L_max >> 6.

CROSS-PILLAR (VII <-> VIII):
  Calcagni-Oriti-Thurigen (Paper 19) proved that:
    - SINGLE lattice states show NO genuine dimensional flow
    - True flow requires QUANTUM SUPERPOSITION over complexes
  Our 992-mode spectrum at fixed tau IS a single state.
  The tau sweep (section 8) is the framework analog of superposition
  over geometries. The variation of d_s(tau) is a GEOMETRIC flow,
  not a quantum-superposition flow.

PRE-REGISTERABLE PREDICTION (S64):
  At L_max -> infinity, the Weyl exponent alpha_N should approach 8.
  Compute alpha_N(L_max) for L_max = 2, 4, 6, 8, 10 and verify the
  approach to d_s = 8. This tests whether the truncation is the sole
  cause of d_s < 8 or whether the Jensen deformation fundamentally
  reduces the spectral dimension.
""")

print("DONE.")
