#!/usr/bin/env python3
"""
SAKHAROV-GN-48: Curvature-weighted Sakharov induced gravity using S47 anatomy.

Physics:
  Sakharov (1967): G_N arises from one-loop quantum fluctuations of matter fields.
  The Einstein-Hilbert term R/(16piG) is INDUCED in the effective action.

  Standard (S45):
    1/(16piG) = (1/(48pi^2)) * sum_k d_k [Lambda^2 - m_k^2 ln(1 + Lambda^2/m_k^2)]
    Result: G_Sak/G_obs = 0.436, monotone, 0.36 OOM discrepancy. Gate: INFO.

  S48 upgrade — curvature-weighted spectral sum:
    On a curved internal manifold, the Lichnerowicz formula gives:
      D^2 = nabla^2 + R/4
    so the effective mass of each mode receives a curvature correction:
      m_k^2(eff) = lambda_k^2 * M_KK^2 + R(tau) * M_KK^2 / 4

    S47 gives R(tau), Ric^2(tau), K^2(tau) at 26 tau points [0, 0.25].
    The Seeley-DeWitt a_4 coefficient provides additional corrections
    from R^2, Ric^2, Riem^2 terms (suppressed by 1/Lambda^2).

  Condensed matter analog (Volovik):
    In 3He-A, the induced Newton's constant is:
      1/G_eff ~ N_F * p_F^2 / m*
    The anisotropy of the gap structure (Fermi point geometry) changes
    the effective G. The Jensen deformation of SU(3) is the analog of
    changing the gap anisotropy.

DATA SOURCE CONSISTENCY NOTE:
  s42_crystal_spec.npz (tau=0.01-0.15) and s36_sfull (tau=0.05, 0.16-0.22)
  have a 0.55% Sakharov discrepancy at their overlap tau=0.05 (different
  eigenvalue normalizations). To avoid data-splicing artifacts, this script
  uses ONLY the s36 + s45_occ consistent data set (the same 9 tau points
  as S45), and interpolates to the curvature anatomy grid.

Gate: SAKHAROV-GN-48
  PASS if discrepancy < 0.2 OOM
  INFO if computed but unchanged
  FAIL if S(tau) monotone

Data sources:
  - s47_curvature_anatomy.npz: K_ab(tau), R(tau), Ric(tau) at 26 tau
  - s36_sfull_tau_stabilization.npz: sector eigenvalues at 7 tau (0.05, 0.16-0.22)
  - s45_occ_spectral.npz: eigenvalues at tau=0, 0.19, 0.5
  - s45_running_gn.npz: S45 baseline for comparison
  - canonical_constants.py: M_KK, M_Pl, G_N, a0_fold, etc.

Output: s48_sakharov_gn.{npz, png}
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import (
    M_KK_gravity as M_KK, M_Pl_reduced as M_PL,
    G_N as G_N_OBS, a0_fold, a2_fold, a4_fold, tau_fold,
    Vol_SU3_Haar, PI
)

DATA_DIR = Path(__file__).parent

# ============================================================
#  Physical scales
# ============================================================
inv_16piG_obs = M_PL**2 / 2.0       # GeV^2 (observed target)
LAMBDA_UV = 10.0 * M_KK             # UV cutoff (S44/S45)
prefactor = 1.0 / (48.0 * np.pi**2)

print("=" * 78)
print("SAKHAROV-GN-48: Curvature-Weighted Sakharov G_N Using S47 Anatomy")
print("=" * 78)
print(f"  M_KK             = {M_KK:.4e} GeV")
print(f"  M_Pl (reduced)   = {M_PL:.4e} GeV")
print(f"  Lambda_UV        = {LAMBDA_UV:.4e} GeV  (10 * M_KK)")
print(f"  1/(16piG_obs)    = {inv_16piG_obs:.6e} GeV^2")

# ============================================================
#  SU(3) sector definitions
# ============================================================
SECTORS = [(0,0), (1,0), (0,1), (1,1), (2,0), (0,2), (3,0), (0,3), (2,1), (1,2)]
SECTOR_SIZES = [16, 48, 48, 128, 96, 96, 160, 160, 240, 240]

def dim_pq(p, q):
    """Peter-Weyl degeneracy: dimension of SU(3) irrep (p,q)."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2

# Flat degeneracy array for 1232-mode ordering
degs_flat = []
for i, (p, q) in enumerate(SECTORS):
    degs_flat.extend([dim_pq(p, q)] * SECTOR_SIZES[i])
degs_flat = np.array(degs_flat, dtype=float)

# ============================================================
#  STEP 1: Load curvature anatomy (S47)
# ============================================================
print(f"\n{'='*78}")
print("STEP 1: Load S47 Curvature Anatomy")
print("=" * 78)

d_curv = np.load(DATA_DIR / 's47_curvature_anatomy.npz', allow_pickle=True)
tau_curv = d_curv['tau_values']           # (26,): 0, 0.01, ..., 0.25
K_all = d_curv['K_all']                   # (26, 28): 28 sectional curvatures
R_scalar = d_curv['R_scalar_all']         # (26,): scalar curvature
Ric_eigs = d_curv['Ric_eigs_all']        # (26, 8): Ricci eigenvalues
pair_types = d_curv['pair_types']         # (28,): type labels

print(f"  Curvature grid: {len(tau_curv)} tau points, [{tau_curv[0]:.2f}, {tau_curv[-1]:.2f}]")

# Curvature invariants at each tau
R_tau = R_scalar.copy()
Ric_sq_tau = np.sum(Ric_eigs**2, axis=1)
Ric_tf_sq_tau = np.sum((Ric_eigs - R_scalar[:, None]/8)**2, axis=1)
K_sq_tau = np.sum(K_all**2, axis=1)

# Curvature anisotropy: K_max / K_min (nonzero)
K_aniso = np.zeros(len(tau_curv))
for i in range(len(tau_curv)):
    K_nonzero = K_all[i][K_all[i] > 1e-10]
    if len(K_nonzero) > 0:
        K_aniso[i] = K_nonzero.max() / K_nonzero.min()

fold_ci = np.argmin(np.abs(tau_curv - tau_fold))
print(f"\n  At fold (tau={tau_fold}):")
print(f"    R            = {R_tau[fold_ci]:.8f}")
print(f"    Ric^2        = {Ric_sq_tau[fold_ci]:.8f}")
print(f"    Ric_tf^2     = {Ric_tf_sq_tau[fold_ci]:.8f}")
print(f"    sum(K^2)     = {K_sq_tau[fold_ci]:.8f}")
print(f"    K_anisotropy = {K_aniso[fold_ci]:.4f}")

# ============================================================
#  STEP 2: Load eigenvalue data (CONSISTENT sources only)
# ============================================================
print(f"\n{'='*78}")
print("STEP 2: Assemble Dirac Eigenvalues (s36 + s45_occ only)")
print("  NOTE: s42_crystal_spec excluded due to 0.55% normalization offset")
print("=" * 78)

tau_eigen_data = {}

# --- Source 1: s45_occ_spectral (tau=0.000, 0.190, 0.500) ---
d_occ = np.load(DATA_DIR / 's45_occ_spectral.npz', allow_pickle=True)
for tau_val, key in [(0.000, 'evals_tau0.000'), (0.190, 'evals_tau0.190'),
                      (0.500, 'evals_tau0.500')]:
    if key in d_occ.files:
        abs_evals = d_occ[key]
        tau_eigen_data[tau_val] = (abs_evals, degs_flat / 2.0)

# --- Source 2: s36_sfull_tau_stabilization (sector-resolved at 7 tau) ---
d36 = np.load(DATA_DIR / 's36_sfull_tau_stabilization.npz', allow_pickle=True)
s36_taus = [0.050, 0.160, 0.170, 0.180, 0.190, 0.210, 0.220]
for tau_val in s36_taus:
    tau_round = round(tau_val, 2)
    if tau_round in tau_eigen_data:
        continue
    tau_str = f"{tau_val:.3f}"
    pos_evals = []
    pos_degs = []
    for (p, q) in SECTORS:
        key = f'evals_tau{tau_str}_{p}_{q}'
        if key not in d36.files:
            continue
        evals = d36[key]
        pos = evals[evals > 0.01]
        deg = dim_pq(p, q)
        pos_evals.extend(pos.tolist())
        pos_degs.extend([deg] * len(pos))
    if len(pos_evals) > 0:
        tau_eigen_data[tau_round] = (np.array(pos_evals), np.array(pos_degs, dtype=float))

# Sort and keep only [0, 0.5]
tau_eigen_sorted = np.array(sorted(tau_eigen_data.keys()))
n_eigen = len(tau_eigen_sorted)
print(f"\n  {n_eigen} tau points:")
for tau_val in tau_eigen_sorted:
    pe, pd = tau_eigen_data[tau_val]
    a0 = np.sum(pd)
    print(f"    tau={tau_val:.3f}: {len(pe)} modes, a_0={a0:.0f}")

# ============================================================
#  STEP 3: Standard Sakharov at all tau (baseline)
# ============================================================
print(f"\n{'='*78}")
print("STEP 3: Standard Sakharov G_N (Baseline)")
print("=" * 78)

inv_16piG_standard = np.zeros(n_eigen)
a0_arr = np.zeros(n_eigen)
s2_arr = np.zeros(n_eigen)
leading_arr = np.zeros(n_eigen)
subleading_arr = np.zeros(n_eigen)

for i, tau_val in enumerate(tau_eigen_sorted):
    pos_evals, pos_degs = tau_eigen_data[tau_val]
    m_k = np.abs(pos_evals) * M_KK

    a0_arr[i] = np.sum(pos_degs)
    s2_arr[i] = np.sum(pos_degs * pos_evals**2)

    term = LAMBDA_UV**2 - m_k**2 * np.log(1.0 + LAMBDA_UV**2 / m_k**2)
    inv_16piG_standard[i] = prefactor * np.sum(pos_degs * term)

    leading_arr[i] = prefactor * a0_arr[i] * LAMBDA_UV**2
    subleading_arr[i] = prefactor * np.sum(-pos_degs * m_k**2 * np.log(1.0 + LAMBDA_UV**2 / m_k**2))

ratio_standard = inv_16piG_obs / inv_16piG_standard
log10_ratio_std = np.log10(ratio_standard)

print(f"\n{'tau':>6s}  {'a_0':>8s}  {'1/(16piG_std)':>16s}  {'G/G_obs':>12s}  {'log10':>10s}")
for i, tau_val in enumerate(tau_eigen_sorted):
    print(f"{tau_val:6.3f}  {a0_arr[i]:8.0f}  {inv_16piG_standard[i]:16.6e}  "
          f"{ratio_standard[i]:12.6f}  {log10_ratio_std[i]:+10.4f}")

# Cross-check with S45
d45 = np.load(DATA_DIR / 's45_running_gn.npz', allow_pickle=True)
s45_tau = d45['tau_values']
s45_ratio = d45['ratio_sak']
print(f"\n  S45 cross-check at fold: G/G_obs = {s45_ratio[np.argmin(np.abs(s45_tau-0.19))]:.6f}")
fold_eigen_idx = np.argmin(np.abs(tau_eigen_sorted - 0.19))
print(f"  This computation at fold:  G/G_obs = {ratio_standard[fold_eigen_idx]:.6f}")

# ============================================================
#  STEP 4: Curvature-corrected Sakharov (Lichnerowicz + a_4)
# ============================================================
print(f"\n{'='*78}")
print("STEP 4: Curvature Corrections — Two Channels")
print("  Channel 1 (Lichnerowicz): m_k^2(eff) = m_k^2 + R(tau)*M_KK^2/4")
print("  Channel 2 (a_4):         O(R^2/Lambda^2) correction from heat kernel")
print("=" * 78)

from scipy.interpolate import interp1d

# Interpolate curvature to eigenvalue tau grid
R_interp = interp1d(tau_curv, R_tau, kind='cubic', fill_value='extrapolate')
Ric_tf_sq_interp = interp1d(tau_curv, Ric_tf_sq_tau, kind='cubic', fill_value='extrapolate')

R_at_eigen = R_interp(tau_eigen_sorted)
Ric_tf_sq_at_eigen = Ric_tf_sq_interp(tau_eigen_sorted)

# --- Channel 1: Lichnerowicz mass correction ---
inv_16piG_lich = np.zeros(n_eigen)
delta_mass_frac = np.zeros(n_eigen)

for i, tau_val in enumerate(tau_eigen_sorted):
    pos_evals, pos_degs = tau_eigen_data[tau_val]
    m_k_sq = pos_evals**2 * M_KK**2
    R_val = R_at_eigen[i]
    m_k_sq_eff = m_k_sq + R_val * M_KK**2 / 4.0

    delta_mass_frac[i] = np.mean(R_val / 4.0 / pos_evals**2)

    term_eff = LAMBDA_UV**2 - m_k_sq_eff * np.log(1.0 + LAMBDA_UV**2 / m_k_sq_eff)
    inv_16piG_lich[i] = prefactor * np.sum(pos_degs * term_eff)

ratio_lich = inv_16piG_obs / inv_16piG_lich
log10_ratio_lich = np.log10(ratio_lich)

print(f"\n--- Channel 1: Lichnerowicz ---")
print(f"{'tau':>6s}  {'R(tau)':>8s}  {'dm^2/m^2':>10s}  {'G/G_obs':>12s}  {'log10':>10s}  {'delta':>10s}")
for i, tau_val in enumerate(tau_eigen_sorted):
    delta_log = log10_ratio_lich[i] - log10_ratio_std[i]
    print(f"{tau_val:6.3f}  {R_at_eigen[i]:8.5f}  {delta_mass_frac[i]:10.6f}  "
          f"{ratio_lich[i]:12.6f}  {log10_ratio_lich[i]:+10.4f}  {delta_log:+10.6f}")

# --- Channel 2: a_4 correction ---
# From Seeley-DeWitt: delta(1/(16piG))_a4 / (1/(16piG)) ~ R/(24 * (Lambda/M_KK)^2)
# Plus tracefree Ricci contribution
a4_correction = np.zeros(n_eigen)
for i in range(n_eigen):
    R_val = R_at_eigen[i]
    Ric_tf_val = Ric_tf_sq_at_eigen[i]
    a4_correction[i] = R_val / (24.0 * (LAMBDA_UV/M_KK)**2) + \
                        Ric_tf_val / (R_val * (LAMBDA_UV/M_KK)**2 * 6.0)

# Full corrected
inv_16piG_corr = inv_16piG_lich * (1.0 + a4_correction)
ratio_corr = inv_16piG_obs / inv_16piG_corr
log10_ratio_corr = np.log10(ratio_corr)

print(f"\n--- Channel 2: a_4 correction ---")
print(f"{'tau':>6s}  {'a4_corr(%)':>10s}  {'G_corr/G_obs':>14s}  {'log10':>10s}  "
      f"{'vs_std':>10s}  {'vs_S45':>10s}")
for i, tau_val in enumerate(tau_eigen_sorted):
    delta_vs_std = log10_ratio_corr[i] - log10_ratio_std[i]
    # Find nearest S45 point for comparison
    s45_idx = np.argmin(np.abs(s45_tau - tau_val))
    if abs(s45_tau[s45_idx] - tau_val) < 0.005:
        delta_vs_s45 = log10_ratio_corr[i] - np.log10(s45_ratio[s45_idx])
        s45_str = f"{delta_vs_s45:+10.6f}"
    else:
        s45_str = "     N/A  "
    print(f"{tau_val:6.3f}  {a4_correction[i]*100:10.4f}  {ratio_corr[i]:14.6f}  "
          f"{log10_ratio_corr[i]:+10.4f}  {delta_vs_std:+10.6f}  {s45_str}")

# ============================================================
#  STEP 5: Monotonicity analysis
# ============================================================
print(f"\n{'='*78}")
print("STEP 5: Monotonicity Analysis")
print("=" * 78)

# Standard
d_std = np.diff(inv_16piG_standard)
std_monotone = np.all(d_std > 0) or np.all(d_std < 0)
std_dir = "DECREASING" if np.all(d_std < 0) else ("INCREASING" if np.all(d_std > 0) else "NON-MONOTONE")

# Corrected
d_corr = np.diff(inv_16piG_corr)
corr_monotone = np.all(d_corr > 0) or np.all(d_corr < 0)
corr_dir = "DECREASING" if np.all(d_corr < 0) else ("INCREASING" if np.all(d_corr > 0) else "NON-MONOTONE")

print(f"\n  Standard Sakharov: {std_dir} (monotone={std_monotone})")
print(f"  Full corrected:    {corr_dir} (monotone={corr_monotone})")

# Search for extrema in corrected ratio
ratio_diffs = np.diff(ratio_corr)
sign_changes = np.where(np.diff(np.sign(ratio_diffs)) != 0)[0]
print(f"\n  Sign changes in d(G/G_obs)/dtau: {len(sign_changes)}")
for sc in sign_changes:
    tau_sc = tau_eigen_sorted[sc+1]
    print(f"    At tau ~ {tau_sc:.3f}: G/G_obs = {ratio_corr[sc+1]:.6f}")

# Min/max
idx_min = np.argmin(np.abs(ratio_corr - 1.0))
best_tau = tau_eigen_sorted[idx_min]
best_ratio = ratio_corr[idx_min]
best_log10 = log10_ratio_corr[idx_min]

print(f"\n  Closest to G_obs: tau={best_tau:.3f}, G/G_obs={best_ratio:.6f} ({best_log10:+.4f} OOM)")

# ============================================================
#  STEP 6: Curvature anatomy at the fold
# ============================================================
print(f"\n{'='*78}")
print("STEP 6: Curvature Anatomy at the Fold")
print("=" * 78)

unique_types = sorted(set(pair_types))
type_indices = {t: np.where(pair_types == t)[0] for t in unique_types}

# Type-resolved curvature evolution
K_type_avg = np.zeros((len(tau_curv), len(unique_types)))
for j, t in enumerate(unique_types):
    K_type_avg[:, j] = np.mean(K_all[:, type_indices[t]], axis=1)

print(f"\n  Curvature type evolution (tau=0 -> fold -> 0.25):")
print(f"  {'Type':>8s}  {'Count':>5s}  {'K(0)':>10s}  {'K(fold)':>10s}  {'K(0.25)':>10s}  {'dK/K':>8s}")
for j, t in enumerate(unique_types):
    K0 = K_type_avg[0, j]
    Kf = K_type_avg[fold_ci, j]
    K25 = K_type_avg[-1, j]
    if K0 > 1e-10:
        frac = (Kf - K0) / K0 * 100
    else:
        frac = 0
    print(f"  {t:>8s}  {len(type_indices[t]):>5d}  {K0:10.6f}  {Kf:10.6f}  {K25:10.6f}  {frac:+7.1f}%")

# Ricci eigenvalue splitting
print(f"\n  Ricci eigenvalue splitting:")
for tau_show in [0.00, 0.05, 0.10, 0.15, 0.19, 0.25]:
    idx = np.argmin(np.abs(tau_curv - tau_show))
    eigs = Ric_eigs[idx]
    spread = eigs.max() - eigs.min()
    print(f"    tau={tau_show:.2f}: [{eigs.min():.5f}, {eigs.max():.5f}], spread={spread:.5f}")

# ============================================================
#  STEP 7: Directional Sakharov stiffness
# ============================================================
print(f"\n{'='*78}")
print("STEP 7: Directional Stiffness & F(tau) Functional")
print("=" * 78)

# Interpolate Sakharov sums to full curvature grid
f_std_interp = interp1d(tau_eigen_sorted, inv_16piG_standard, kind='cubic',
                         fill_value='extrapolate')
f_corr_interp = interp1d(tau_eigen_sorted, inv_16piG_corr, kind='cubic',
                           fill_value='extrapolate')

# Restrict interpolation to [0, 0.25] (within curvature data)
tau_interp = tau_curv[tau_curv <= 0.25]
inv_std_interp = f_std_interp(tau_interp)
inv_corr_interp = f_corr_interp(tau_interp)

# F(tau) = R(tau) * 1/(16piG(tau)) — gravitational self-energy functional
R_interp_vals = R_tau[:len(tau_interp)]
F_std = R_interp_vals * inv_std_interp
F_corr = R_interp_vals * inv_corr_interp

# F monotonicity
dF = np.diff(F_corr)
F_monotone = np.all(dF > 0) or np.all(dF < 0)
F_dir = "DECREASING" if np.all(dF < 0) else ("INCREASING" if np.all(dF > 0) else "NON-MONOTONE")

# F sign changes
F_sign_changes = np.where(np.diff(np.sign(dF)) != 0)[0]

print(f"\n  F(tau) = R(tau) * 1/(16piG_corr(tau)):")
print(f"    Monotone: {F_monotone} ({F_dir})")
print(f"    Sign changes in dF/dtau: {len(F_sign_changes)}")
for sc in F_sign_changes:
    print(f"      tau ~ {(tau_interp[sc]+tau_interp[sc+1])/2:.3f}")

print(f"\n  F at key tau:")
for tau_show in [0.00, 0.05, 0.10, 0.15, 0.19, 0.25]:
    idx = np.argmin(np.abs(tau_interp - tau_show))
    print(f"    tau={tau_show:.2f}: F_corr = {F_corr[idx]:.6e}, F_std = {F_std[idx]:.6e}")

# Curvature-response function
# d(1/(16piG))/dtau from curvature alone: -(M_KK^2/4) * (dR/dtau) * response
dR_dtau = np.gradient(R_tau, tau_curv)
response_arr = np.zeros(n_eigen)
for i in range(n_eigen):
    pos_evals, pos_degs = tau_eigen_data[tau_eigen_sorted[i]]
    m_k_sq_eff = pos_evals**2 * M_KK**2 + R_at_eigen[i] * M_KK**2 / 4.0
    resp = np.log(1.0 + LAMBDA_UV**2 / m_k_sq_eff) - LAMBDA_UV**2 / (m_k_sq_eff + LAMBDA_UV**2)
    response_arr[i] = prefactor * np.sum(pos_degs * resp)

f_resp_interp = interp1d(tau_eigen_sorted, response_arr, kind='cubic', fill_value='extrapolate')
response_full = f_resp_interp(tau_interp)
d_inv_curv = -(M_KK**2 / 4.0) * dR_dtau[:len(tau_interp)] * response_full

print(f"\n  Curvature-driven d(1/(16piG))/dtau:")
for tau_show in [0.00, 0.10, 0.19, 0.25]:
    idx = np.argmin(np.abs(tau_interp - tau_show))
    print(f"    tau={tau_show:.2f}: dR/dtau={dR_dtau[idx]:.4f}, "
          f"d_inv_curv={d_inv_curv[idx]:.4e} GeV^2")

# ============================================================
#  STEP 8: Comparison with S45
# ============================================================
print(f"\n{'='*78}")
print("STEP 8: S45 Comparison & Gate")
print("=" * 78)

s45_fold_idx = np.argmin(np.abs(s45_tau - 0.19))
s45_ratio_fold = s45_ratio[s45_fold_idx]
s45_log10_fold = np.log10(s45_ratio_fold)

s48_ratio_fold = ratio_corr[fold_eigen_idx]
s48_log10_fold = log10_ratio_corr[fold_eigen_idx]

improvement = abs(s45_log10_fold) - abs(s48_log10_fold)  # positive = S48 better

print(f"\n  At fold (tau={tau_fold}):")
print(f"    S45 standard:   G/G_obs = {s45_ratio_fold:.6f}  (|log10| = {abs(s45_log10_fold):.4f} OOM)")
print(f"    S48 corrected:  G/G_obs = {s48_ratio_fold:.6f}  (|log10| = {abs(s48_log10_fold):.4f} OOM)")
print(f"    Improvement:    {improvement:+.4f} OOM (positive = S48 closer to G_obs)")

# Total variation
total_var = (ratio_corr.max() - ratio_corr.min()) / np.mean(ratio_corr)

print(f"\n  Running statistics:")
print(f"    Range: [{ratio_corr.min():.6f}, {ratio_corr.max():.6f}]")
print(f"    Total variation: {total_var*100:.2f}%")
print(f"    Best: tau={best_tau:.3f}, G/G_obs={best_ratio:.6f} ({best_log10:+.4f} OOM)")

# --- Gate verdict ---
discrepancy_oom = abs(s48_log10_fold)

# S(tau) = 1/(16piG_corr) is what the gate checks for monotonicity.
# The corrected sum has the same monotonicity as the standard (same underlying spectrum).
if discrepancy_oom < 0.2:
    gate_verdict = "PASS"
    gate_reason = f"Discrepancy {discrepancy_oom:.4f} OOM < 0.2 threshold"
elif corr_monotone:
    gate_verdict = "FAIL"
    gate_reason = f"S(tau) monotone ({corr_dir}). Discrepancy {discrepancy_oom:.4f} OOM"
else:
    if abs(improvement) < 0.01:
        gate_verdict = "INFO"
        gate_reason = (f"Curvature corrections computed. Discrepancy {discrepancy_oom:.4f} OOM "
                       f"(improvement {improvement:+.4f} OOM over S45)")
    else:
        gate_verdict = "INFO"
        gate_reason = f"Discrepancy {discrepancy_oom:.4f} OOM"

print(f"\n  GATE: SAKHAROV-GN-48 = {gate_verdict}")
print(f"  Reason: {gate_reason}")

# ============================================================
#  Physical interpretation
# ============================================================
print(f"\n{'='*78}")
print("PHYSICAL INTERPRETATION")
print("=" * 78)

print(f"""
  The Sakharov induced G_N receives two curvature corrections from S47 anatomy:

  1. LICHNEROWICZ MASS SHIFT (Channel 1):
     D^2 = nabla^2 + R/4 shifts every mode's effective mass by R*M_KK^2/4.
     Fractional shift: dm^2/m^2 ~ R/(4*lambda^2) ~ {delta_mass_frac[fold_eigen_idx]*100:.1f}% at fold.
     Effect on G/G_obs: +{abs(log10_ratio_lich[fold_eigen_idx]-log10_ratio_std[fold_eigen_idx])*1000:.1f} milli-OOM
     (REDUCES the discrepancy — the mass shift increases 1/(16piG), pushing G toward G_obs)

  2. a_4 SEELEY-DEWITT CORRECTION (Channel 2):
     Higher-order heat kernel: R^2, Ric^2 at O(1/Lambda^2).
     Size: {a4_correction[fold_eigen_idx]*100:.4f}% at fold.
     Effect: {abs(a4_correction[fold_eigen_idx]*log10_ratio_lich[fold_eigen_idx])*1000:.2f} milli-OOM
     (NEGLIGIBLE — suppressed by (M_KK/Lambda)^2 = 1/100)

  Combined improvement over S45: {improvement*1000:+.1f} milli-OOM = {improvement:+.4f} OOM.
  The curvature corrections HELP (push G toward G_obs) but are quantitatively
  tiny compared to the 0.36 OOM baseline discrepancy.

  RESONANCE STRUCTURE:
  - The SU(3) cavity has 28 sectional curvature directions
  - 3 directions (U1-SU2) are FLAT — zero-modes, nodal lines
  - 3 directions (SU2-SU2) STIFFEN under Jensen: K rises from 0.083 to 0.122
  - 12 directions (SU2-C2) SOFTEN: K drops from 0.021 to 0.010
  - 6 directions (C2-C2) MIX: some rise, some fall
  - Net: R increases by 1% over [0, 0.25]
  - The anisotropy ratio K_max/K_min grows from 1 to 12.5

  CONDENSED MATTER ANALOG (Volovik):
  - In 3He-A, induced G_N ~ N_F * p_F^2 / m* where m* is the effective mass
  - The Jensen deformation changes m* (the Dirac eigenvalues shift)
  - The Lichnerowicz correction is the analog of the BCS gap equation
    modifying quasiparticle masses near a Fermi surface
  - The 0.36 OOM discrepancy survives because the species count a_0=6440
    (number of resonant modes in the cavity) does not change with tau
  - Only the mass-dependent correction (subleading term) varies, and it
    contributes ~9% of the total""")

# ============================================================
#  STEP 9: Save data
# ============================================================
print(f"\n{'='*78}")
print("STEP 9: Save Data")
print("=" * 78)

np.savez(DATA_DIR / 's48_sakharov_gn.npz',
    # Eigenvalue tau grid
    tau_eigen=tau_eigen_sorted,
    n_eigen=n_eigen,

    # Standard Sakharov
    inv_16piG_standard=inv_16piG_standard,
    ratio_standard=ratio_standard,
    log10_ratio_standard=log10_ratio_std,

    # Lichnerowicz-corrected
    inv_16piG_lich=inv_16piG_lich,
    ratio_lich=ratio_lich,
    log10_ratio_lich=log10_ratio_lich,
    delta_mass_frac=delta_mass_frac,

    # Full corrected (Lich + a_4)
    inv_16piG_corr=inv_16piG_corr,
    ratio_corr=ratio_corr,
    log10_ratio_corr=log10_ratio_corr,
    a4_correction=a4_correction,

    # Curvature data at eigenvalue grid
    R_at_eigen=R_at_eigen,
    Ric_tf_sq_at_eigen=Ric_tf_sq_at_eigen,

    # Curvature anatomy (full S47 grid, for reference)
    tau_curv=tau_curv,
    R_tau=R_tau,
    Ric_sq_tau=Ric_sq_tau,
    Ric_tf_sq_tau=Ric_tf_sq_tau,
    K_sq_tau=K_sq_tau,
    K_aniso_tau=K_aniso,

    # Curvature type averages
    K_type_avg=K_type_avg,
    unique_types=np.array(unique_types),

    # F functional (on interpolated grid)
    tau_interp=tau_interp,
    F_corr=F_corr,
    F_std=F_std,

    # Response and curvature-driven derivative
    response_function=response_arr,
    dR_dtau=dR_dtau,

    # Key scalars
    inv_16piG_obs=inv_16piG_obs,
    Lambda_UV=LAMBDA_UV,
    M_KK=M_KK,
    tau_fold=tau_fold,

    # Gate
    gate_name=np.array(['SAKHAROV-GN-48']),
    gate_verdict=np.array([gate_verdict]),
    gate_reason=np.array([gate_reason]),
    discrepancy_oom_fold=discrepancy_oom,
    improvement_over_s45=improvement,
    s45_discrepancy_oom=abs(s45_log10_fold),
    corr_monotone=corr_monotone,
    std_monotone=std_monotone,
    best_tau=best_tau,
    best_ratio=best_ratio,
    total_variation=total_var,

    # Data quality flag
    data_consistency_note=np.array([
        's42_crystal_spec excluded: 0.55% Sakharov offset vs s36 at tau=0.05. '
        'Using only s36+s45_occ (consistent, same as S45).'
    ]),
)
print(f"  Saved: tier0-computation/s48_sakharov_gn.npz")

# ============================================================
#  STEP 10: Plot
# ============================================================
fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle('SAKHAROV-GN-48: Curvature-Weighted Sakharov $G_N$ — S47 Anatomy',
             fontsize=14, fontweight='bold')

# --- Panel 1: G/G_obs vs tau ---
ax = axes[0, 0]
ax.plot(tau_eigen_sorted, ratio_standard, 'b-o', lw=2, ms=5, label='Standard', alpha=0.7)
ax.plot(tau_eigen_sorted, ratio_lich, 'r--s', lw=2, ms=5, label='Lichnerowicz')
ax.plot(tau_eigen_sorted, ratio_corr, 'k-^', lw=2, ms=5, label='Full corrected')
ax.axhline(1.0, color='green', ls=':', lw=1.5, label='$G_{obs}$')
ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5, label=f'Fold')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$G_{Sak}/G_{obs}$')
ax.set_title(r'$G_N(\tau)$ — Three Formulas')
ax.legend(fontsize=7, loc='upper left')
ax.set_xlim(-0.02, 0.55)
ax.grid(alpha=0.3)

# --- Panel 2: log10 discrepancy ---
ax = axes[0, 1]
ax.plot(tau_eigen_sorted, log10_ratio_std, 'b-o', lw=2, ms=5, alpha=0.7, label='Standard')
ax.plot(tau_eigen_sorted, log10_ratio_lich, 'r--s', lw=2, ms=5, label='Lichnerowicz')
ax.plot(tau_eigen_sorted, log10_ratio_corr, 'k-^', lw=2, ms=5, label='Full corrected')
ax.axhline(0, color='green', ls=':', lw=1.5)
ax.axhline(-0.2, color='orange', ls=':', lw=1, alpha=0.7, label='0.2 OOM')
ax.axhline(0.2, color='orange', ls=':', lw=1, alpha=0.7)
ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$\log_{10}(G/G_{obs})$')
ax.set_title(r'Discrepancy (OOM)')
ax.legend(fontsize=7)
ax.set_xlim(-0.02, 0.55)
ax.grid(alpha=0.3)

# Inset: zoom on the correction
ax_ins = ax.inset_axes([0.5, 0.1, 0.45, 0.35])
delta = log10_ratio_corr - log10_ratio_std
ax_ins.plot(tau_eigen_sorted, delta * 1000, 'k-^', ms=4, lw=1.5)
ax_ins.set_xlabel(r'$\tau$', fontsize=7)
ax_ins.set_ylabel(r'$\Delta$ (milli-OOM)', fontsize=7)
ax_ins.tick_params(labelsize=6)
ax_ins.axvline(tau_fold, color='gray', ls='--', alpha=0.3)
ax_ins.set_title('Correction', fontsize=7)
ax_ins.grid(alpha=0.3)

# --- Panel 3: Curvature anatomy ---
ax = axes[0, 2]
ax.plot(tau_curv, R_tau, 'b-', lw=2, label=r'$R(\tau)$')
ax2 = ax.twinx()
ax2.plot(tau_curv, Ric_tf_sq_tau * 1e3, 'r-', lw=2, label=r'$|Ric_{tf}|^2 \times 10^3$')
ax2.plot(tau_curv, K_sq_tau, 'g--', lw=1.5, label=r'$\sum K^2$')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$R(\tau)$', color='blue')
ax2.set_ylabel(r'Curvature invariants', color='red')
ax.set_title('S47 Curvature Anatomy')
ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5)
lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines1 + lines2, labels1 + labels2, fontsize=7)
ax.grid(alpha=0.3)

# --- Panel 4: Sectional curvature by type ---
ax = axes[1, 0]
for j, t in enumerate(unique_types):
    ax.plot(tau_curv, K_type_avg[:, j], '-o', ms=2, label=t, lw=1.5)
ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$\langle K \rangle$ per type')
ax.set_title('Sectional Curvature Types')
ax.legend(fontsize=7)
ax.grid(alpha=0.3)

# --- Panel 5: Corrections decomposition ---
ax = axes[1, 1]
lich_corr_milli = (log10_ratio_lich - log10_ratio_std) * 1000
a4_corr_milli = (log10_ratio_corr - log10_ratio_lich) * 1000
total_corr_milli = (log10_ratio_corr - log10_ratio_std) * 1000

ax.plot(tau_eigen_sorted, total_corr_milli, 'k-^', lw=2, ms=5, label='Total')
ax.plot(tau_eigen_sorted, lich_corr_milli, 'r--s', lw=1.5, ms=4, label='Lichnerowicz')
ax.plot(tau_eigen_sorted, a4_corr_milli, 'b:o', lw=1, ms=3, label='$a_4$')
ax.axhline(0, color='gray', ls=':', alpha=0.5)
ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$\Delta \log_{10}(G/G_{obs})$ (milli-OOM)')
ax.set_title('Correction Decomposition')
ax.legend(fontsize=7)
ax.grid(alpha=0.3)

# --- Panel 6: Summary ---
ax = axes[1, 2]
ax.axis('off')
summary_text = (
    f"SAKHAROV-GN-48: {gate_verdict}\n"
    f"{'='*42}\n\n"
    f"Lambda = 10 * M_KK = {LAMBDA_UV:.2e} GeV\n"
    f"a_0 = {int(a0_arr[0])} (constant at all tau)\n\n"
    f"At fold (tau={tau_fold}):\n"
    f"  S45 standard: {s45_log10_fold:+.4f} OOM\n"
    f"  S48 corrected: {s48_log10_fold:+.4f} OOM\n"
    f"  Improvement: {improvement:+.4f} OOM\n\n"
    f"Corrections at fold:\n"
    f"  Lichnerowicz: {lich_corr_milli[fold_eigen_idx]:+.1f} milli-OOM\n"
    f"  a_4 heat kernel: {a4_corr_milli[fold_eigen_idx]:+.2f} milli-OOM\n"
    f"  Mass shift dm^2/m^2: {delta_mass_frac[fold_eigen_idx]*100:.1f}%\n\n"
    f"Monotone: {corr_dir}\n"
    f"Total variation: {total_var*100:.1f}%\n"
    f"Best: tau={best_tau:.2f} ({best_log10:+.4f} OOM)\n\n"
    f"Curvature (S47):\n"
    f"  R(fold)={R_tau[fold_ci]:.4f}\n"
    f"  K_aniso={K_aniso[fold_ci]:.1f}\n"
    f"  3 flat U1-SU2 (K=0)\n"
    f"  SU2-SU2: 0.083->0.122\n"
    f"  SU2-C2: 0.021->0.010\n\n"
    f"DATA: s36+s45_occ only\n"
    f"  (s42_crystal_spec excluded:\n"
    f"   0.55% normalization offset)"
)
ax.text(0.05, 0.95, summary_text, transform=ax.transAxes, fontsize=7.5,
        verticalalignment='top', fontfamily='monospace',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.tight_layout()
plt.savefig(DATA_DIR / 's48_sakharov_gn.png', dpi=150, bbox_inches='tight')
print(f"  Saved: tier0-computation/s48_sakharov_gn.png")

print(f"\n{'='*78}")
print("COMPUTATION COMPLETE")
print("=" * 78)
