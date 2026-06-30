#!/usr/bin/env python3
"""
OCC-SPEC-64: Occupied-State Spectral Action at tau = 0.190
============================================================

Computes S_occ = sum_{(p,q)} dim(p,q)^2 * sum_j v^2(lambda_j) * |lambda_j|

where v^2(lambda) is the BCS occupation number:
    v_k^2 = (1/2)(1 - xi_k / E_k)
    xi_k  = |lambda_k| - mu
    E_k   = sqrt(xi_k^2 + Delta^2)

The full spectral action S_fold = 250,361 sums ALL eigenvalues equally.
Only occupied modes contribute to physical observables. The BCS occupation
numbers v_k^2 weight each mode by its pair correlation.

Gate: OCC-SPEC-64
  INFO: Report S_occ and revised A_s gap
  Notable: S_occ < 100 => A_s problem significantly reduced

Input: D_K eigenvalues from s36_sfull_tau_stabilization.npz
       Delta = Delta_0_OES = 0.464 M_KK (canonical)
       mu = E_B1 = 0.819 M_KK (BCS chemical potential)  # (local)
Output: s64_occ_spec.{npz,png}

Session 64, Gen-Physicist agent
"""

import numpy as np
import matplotlib.pyplot as plt
import os
import sys
import time

t_start = time.time()

# --- Setup paths ---
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)
ARCHIVE_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), 'computations/_shared')

from canonical_constants import (
    tau_fold, Delta_0_OES, E_B1, S_fold, A_s_CMB,
    E_B2_mean, E_B3_mean, rho_B2_per_mode,
    E_cond, n_pairs
)

print("=" * 70)
print("OCC-SPEC-64: Occupied-State Spectral Action")
print("=" * 70)

# =========================================================================
# 1. LOAD EIGENVALUE DATA
# =========================================================================
print("\n--- 1. Loading eigenvalue data from S36 ---")

data_path = os.path.join(ARCHIVE_DIR, 's36_sfull_tau_stabilization.npz')
d = np.load(data_path, allow_pickle=True)

sectors = [(0,0), (1,0), (0,1), (1,1), (2,0), (0,2), (3,0), (0,3), (2,1), (1,2)]

def dim_pq(p, q):
    return (p + 1) * (q + 1) * (p + q + 2) // 2

# Extract eigenvalues at tau = 0.190
eigenvalue_data = {}
total_evals = 0  # (local)
for p, q in sectors:
    key = f'evals_tau0.190_{p}_{q}'
    evals = d[key]
    eigenvalue_data[(p, q)] = evals
    total_evals += len(evals) * dim_pq(p, q)  # with PW degeneracy
    dpq = dim_pq(p, q)
    print(f"  ({p},{q}): dim={dpq}, n_block_evals={len(evals)}, "
          f"|lambda| range = [{np.min(np.abs(evals)):.6f}, {np.max(np.abs(evals)):.6f}]")

# Verify S_fold reproduction
S_full_check = 0.0  # (local)
for p, q in sectors:
    evals = eigenvalue_data[(p, q)]
    dpq = dim_pq(p, q)
    S_full_check += dpq**2 * np.sum(np.abs(evals))

print(f"\n  S_fold (reproduced) = {S_full_check:.2f}")
print(f"  S_fold (canonical)  = {S_fold:.2f}")
print(f"  Match: {abs(S_full_check - S_fold) / S_fold:.2e}")

# =========================================================================
# 2. BCS PARAMETERS
# =========================================================================
print("\n--- 2. BCS parameters ---")

Delta = Delta_0_OES   # 0.464 M_KK (OES/pair-addition gap)
mu = E_B1             # 0.819 M_KK (BCS chemical potential = B1 mode energy)

print(f"  Delta (BCS gap)       = {Delta:.6f} M_KK")
print(f"  mu (chemical pot)     = {mu:.6f} M_KK")
print(f"  E_B2_mean             = {E_B2_mean:.6f} M_KK")
print(f"  E_B3_mean             = {E_B3_mean:.6f} M_KK")

# =========================================================================
# 3. COMPUTE BCS OCCUPATION NUMBERS
# =========================================================================
print("\n--- 3. BCS occupation numbers v_k^2 ---")

def bcs_occupation(omega, mu, Delta):
    """
    BCS occupation number v_k^2 for a mode at frequency omega.

    v_k^2 = (1/2)(1 - xi_k / E_k)

    xi_k = |omega| - mu  (single-particle energy relative to Fermi level)
    E_k = sqrt(xi_k^2 + Delta^2)  (Bogoliubov quasiparticle energy)

    For xi >> Delta: v_k^2 -> 0 (unoccupied, above Fermi surface)
    For xi << -Delta: v_k^2 -> 1 (fully occupied, deep below Fermi surface)
    For xi = 0: v_k^2 = 1/2 (at Fermi surface)

    Args:
        omega: eigenvalue frequencies |lambda| (array or scalar)
        mu: chemical potential (scalar)
        Delta: BCS gap (scalar)

    Returns:
        v_sq: occupation numbers v_k^2 (same shape as omega)
    """
    xi = np.abs(omega) - mu
    E_k = np.sqrt(xi**2 + Delta**2)
    v_sq = 0.5 * (1.0 - xi / E_k)
    return v_sq

# Show v_k^2 for the 8 BCS modes in (0,0) sector
evals_00 = eigenvalue_data[(0, 0)]
omega_00 = np.abs(evals_00)
# Sort by magnitude for display
omega_sorted = np.sort(omega_00)
v2_00 = bcs_occupation(omega_sorted, mu, Delta)

# The 8 BCS modes are: 4 B2 (degenerate) + 1 B1 + 3 B3 (degenerate)
# From canonical_constants: E_B1=0.819, E_B2_mean=0.845, E_B3_mean=0.978
# The (0,0) sector has 16 eigenvalues (dim=1, block size=1*16=16)
# These come in +/- pairs due to chirality

unique_omega_00 = np.unique(np.round(omega_sorted, 6))
print(f"\n  (0,0) sector: {len(omega_sorted)} eigenvalues, {len(unique_omega_00)} unique |lambda|")
print(f"  Unique |lambda| values and BCS occupations:")
for om in unique_omega_00:
    v2 = bcs_occupation(om, mu, Delta)
    xi = om - mu
    print(f"    |lambda| = {om:.6f}, xi = {xi:+.6f}, v^2 = {v2:.6f}")

# =========================================================================
# 4. COMPUTE S_occ (OCCUPIED-STATE SPECTRAL ACTION)
# =========================================================================
print("\n--- 4. Occupied-state spectral action ---")

S_occ_total = 0.0  # (local)
S_full_total = 0.0  # (local)
sector_results = {}

print(f"\n  {'Sector':>8} {'dim':>4} {'dim^2':>6} {'S_bare':>10} {'S_occ_bare':>12} "
      f"{'<v^2>':>8} {'S_occ':>12} {'S_full':>12} {'frac':>8}")
print("  " + "-" * 95)

for p, q in sectors:
    evals = eigenvalue_data[(p, q)]
    dpq = dim_pq(p, q)
    mult = dpq**2
    omega = np.abs(evals)

    # Full spectral action contribution
    S_bare_full = np.sum(omega)
    S_full_sector = mult * S_bare_full
    S_full_total += S_full_sector

    # BCS occupation
    v2 = bcs_occupation(omega, mu, Delta)

    # Occupied-state spectral action
    S_bare_occ = np.sum(v2 * omega)
    S_occ_sector = mult * S_bare_occ
    S_occ_total += S_occ_sector

    # Mean occupation
    v2_mean = np.mean(v2)

    # Fraction of full
    frac = S_occ_sector / S_full_sector if S_full_sector > 0 else 0

    sector_results[(p, q)] = {
        'S_full': S_full_sector,
        'S_occ': S_occ_sector,
        'v2_mean': v2_mean,
        'n_evals': len(evals),
        'omega_range': (omega.min(), omega.max()),
        'frac': frac
    }

    print(f"  ({p},{q}):  {dpq:4d} {mult:6d} {S_bare_full:10.4f} {S_bare_occ:12.6f} "
          f"{v2_mean:8.4f} {S_occ_sector:12.4f} {S_full_sector:12.2f} {frac:8.4f}")

print(f"\n  {'TOTAL':>8} {'':>4} {'':>6} {'':>10} {'':>12} "
      f"{'':>8} {S_occ_total:12.4f} {S_full_total:12.2f} {S_occ_total/S_full_total:8.6f}")

# =========================================================================
# 5. KEY RESULTS
# =========================================================================
print("\n--- 5. Key results ---")

ratio = S_occ_total / S_full_total
print(f"\n  S_fold (full spectral action)      = {S_full_total:.2f}")
print(f"  S_occ (occupied-state SA)          = {S_occ_total:.6f}")
print(f"  Ratio S_occ / S_fold               = {ratio:.6e}")

# Revised A_s gap
# A_s = S_occ * M_KK^4 / (normalization)
# The original gap uses S_fold:
#   gap_original = log10(S_fold * M_KK^4 / A_s_obs)
# With M_KK = M_KK_gravity in GeV, but the spectral action is in M_KK units
# So S * M_KK^4 is just S (in M_KK^4 units)
#
# The A_s comparison: A_s^{pred} ~ S * M_KK^4 / M_Pl^4
# gap = log10(A_s^{pred} / A_s^{obs})
# With M_KK in natural units (=1), we need the ratio M_KK/M_Pl
# But the task says: gap = log10(S_occ * M_KK^4 / A_s_obs)
# The "7.6 OOM gap" uses S_fold directly.

# A_s ~ S * (M_KK/M_Pl)^4 is the prediction
# The original gap: log10(S_fold / A_s_obs) where S_fold is already in M_KK units
# But that doesn't give 7.6 OOM. Let me compute properly.

# From the task: "If S_occ ~ 5, the A_s gap drops from 7.6 OOM to 2.93 OOM"
# gap_original = log10(S_fold) - log10(A_s_obs) ??? No, that gives:
# log10(250361) = 5.40, log10(2.1e-9) = -8.68 => difference = 14.08 OOM. Not 7.6.
#
# The 7.6 OOM gap must be: log10(A_s^pred / A_s^obs) where A_s^pred includes the
# (M_KK/M_Pl)^4 suppression. Let's check:
# A_s = c * S * (M_KK/M_Pl)^4 where c is some O(1) factor
# log10(S_fold * (M_KK/M_Pl)^4 / A_s_obs)
# (M_KK/M_Pl)^4 = (7.43e16/2.435e18)^4 = (0.0305)^4 = 8.65e-7
# log10(250361 * 8.65e-7 / 2.1e-9) = log10(250361 * 8.65e-7) - log10(2.1e-9)
# = log10(0.2166) + 8.678 = -0.664 + 8.678 = 8.01. Close to 7.6.
#
# Actually the task says the gap is 7.6 OOM when using S_fold.
# Let me just compute the RATIO and report it. The key is S_occ vs S_fold.

from canonical_constants import M_KK_gravity, M_Pl_reduced

MKK_over_MPl = M_KK_gravity / M_Pl_reduced
ratio_4 = MKK_over_MPl**4

A_s_pred_full = S_fold * ratio_4
A_s_pred_occ = S_occ_total * ratio_4

gap_full = np.log10(A_s_pred_full / A_s_CMB)
gap_occ = np.log10(A_s_pred_occ / A_s_CMB)

print(f"\n  M_KK / M_Pl                        = {MKK_over_MPl:.6e}")
print(f"  (M_KK / M_Pl)^4                    = {ratio_4:.6e}")
print(f"  A_s^pred (full)   = S_fold * R^4   = {A_s_pred_full:.6e}")
print(f"  A_s^pred (occ)    = S_occ * R^4    = {A_s_pred_occ:.6e}")
print(f"  A_s^obs (CMB)                      = {A_s_CMB:.1e}")
print(f"  gap_full = log10(A_s^pred / A_s^obs) = {gap_full:.3f} OOM")
print(f"  gap_occ  = log10(A_s^pred / A_s^obs) = {gap_occ:.3f} OOM")
print(f"  Gap reduction:  {gap_full:.3f} - ({gap_occ:.3f}) = {gap_full - gap_occ:.3f} OOM")

# =========================================================================
# 6. EFFECTIVE NUMBER OF CONTRIBUTING MODES
# =========================================================================
print("\n--- 6. Effective number of contributing modes ---")

# N_eff = (sum v_k^2 * d_k)^2 / sum (v_k^2 * d_k)^2
# where d_k = dim(p,q) is the PW weight per eigenvalue
# But actually we should use dim(p,q)^2 * v_k^2 * |lambda_k| for the spectral action weighting.
# Let me compute a few different definitions:

# Definition 1: Participation ratio on v_k^2 * dim^2 * |lambda|
weights_full = []  # v^2 * dim^2 * |lambda| per eigenvalue
weights_v2 = []    # v^2 * dim^2 per eigenvalue

for p, q in sectors:
    evals = eigenvalue_data[(p, q)]
    dpq = dim_pq(p, q)
    mult = dpq**2
    omega = np.abs(evals)
    v2 = bcs_occupation(omega, mu, Delta)

    for j in range(len(evals)):
        weights_full.append(mult * v2[j] * omega[j])
        weights_v2.append(mult * v2[j])

weights_full = np.array(weights_full)
weights_v2 = np.array(weights_v2)

# Participation ratio
N_eff_SA = np.sum(weights_full)**2 / np.sum(weights_full**2)
N_eff_v2 = np.sum(weights_v2)**2 / np.sum(weights_v2**2)

# Total number of base eigenvalues (without PW expansion)
N_base = sum(len(eigenvalue_data[(p,q)]) for p,q in sectors)

# Total eigenvalues with PW multiplicity
N_total_PW = sum(dim_pq(p,q) * len(eigenvalue_data[(p,q)]) for p,q in sectors)

# Number with v^2 > 0.01
n_significant = np.sum(weights_v2 > 0.01 * np.max(weights_v2))

print(f"  N_base (distinct eigenvalues)       = {N_base}")
print(f"  N_total (with PW x block)           = {N_total_PW}")
print(f"  N_eff (spectral action PR)          = {N_eff_SA:.2f}")
print(f"  N_eff (occupation PR)               = {N_eff_v2:.2f}")
print(f"  N_significant (w > 1% of max)       = {n_significant}")

# =========================================================================
# 7. SECTOR DECOMPOSITION OF S_occ
# =========================================================================
print("\n--- 7. Sector decomposition ---")

print(f"\n  {'Sector':>8} {'S_occ':>12} {'frac_S_occ':>12} {'frac_S_full':>12} {'<v^2>':>8}")
print("  " + "-" * 55)

for p, q in sectors:
    r = sector_results[(p, q)]
    frac_occ = r['S_occ'] / S_occ_total if S_occ_total > 0 else 0
    frac_full = r['S_full'] / S_full_total
    print(f"  ({p},{q}):  {r['S_occ']:12.6f} {frac_occ:12.4f} {frac_full:12.4f} {r['v2_mean']:8.4f}")

print(f"\n  (0,0) sector fraction of S_occ: {sector_results[(0,0)]['S_occ'] / S_occ_total:.4f}")
print(f"  (0,0) sector fraction of S_full: {sector_results[(0,0)]['S_full'] / S_full_total:.6f}")

# =========================================================================
# 8. PHYSICAL INTERPRETATION AND CROSS-CHECKS
# =========================================================================
print("\n--- 8. Physical interpretation ---")

# The BCS coherence length is xi_BCS = 0.808 M_KK^{-1}
# Modes with |lambda| > mu + Delta ~ 1.28 M_KK are in the "normal" band
# (v^2 exponentially small). These are ALL the higher PW sectors.
omega_above = mu + Delta  # above this, modes are essentially unoccupied

print(f"\n  Critical frequency |lambda| = mu + Delta = {omega_above:.4f} M_KK")
print(f"  Modes with |lambda| > {omega_above:.4f} have v^2 -> 0")

# For each sector, what fraction of modes are above critical?
for p, q in sectors:
    evals = eigenvalue_data[(p, q)]
    omega = np.abs(evals)
    n_above = np.sum(omega > omega_above)
    frac_above = n_above / len(evals)
    v2_max = np.max(bcs_occupation(omega, mu, Delta))
    v2_min = np.min(bcs_occupation(omega, mu, Delta))
    print(f"  ({p},{q}): {frac_above*100:5.1f}% above critical, "
          f"v^2 range = [{v2_min:.6f}, {v2_max:.6f}]")

# Analytic estimate: for modes far above Fermi surface (xi >> Delta):
# v^2 ~ Delta^2 / (4 * xi^2)
# This gives the leading correction.
print(f"\n  Analytic asymptotic: for |lambda| >> mu + Delta:")
print(f"    v^2 ~ Delta^2 / (4 * (|lambda| - mu)^2)")
print(f"    At |lambda| = 2.0: v^2 ~ {Delta**2 / (4 * (2.0 - mu)**2):.6f}")

# =========================================================================
# 9. COMPARISON WITH TASK TARGETS
# =========================================================================
print("\n--- 9. Comparison with task targets ---")
print(f"\n  S_occ = {S_occ_total:.6f}")
print(f"  S_fold = {S_full_total:.2f}")
print(f"  Ratio = {S_occ_total / S_full_total:.6e}")

if S_occ_total < 100:
    print(f"\n  ** NOTABLE: S_occ < 100 -- A_s problem SIGNIFICANTLY reduced **")
if S_occ_total < 5:
    print(f"  ** S_occ < 5 -- only (0,0) sector contributes **")
    print(f"  ** Expected: A_s gap drops from {gap_full:.1f} to {gap_occ:.1f} OOM **")
if S_occ_total < 0.005:
    print(f"  ** S_occ < 0.005 -- A_s gap CLOSES entirely **")

# =========================================================================
# 10. ALTERNATIVE: GAUSSIAN CUTOFF VERSION
# =========================================================================
print("\n--- 10. Alternative cutoff functions ---")

# The standard SA uses f(D) = |D|. Try also:
# (a) Gaussian: f(x) = exp(-x^2/Lambda^2)
# (b) Sharp: f(x) = Theta(Lambda - |x|) (i.e., 1 if |x| < Lambda, 0 otherwise)

# For Gaussian: S = sum dim^2 * sum_j exp(-lambda_j^2)
S_gauss_full = 0.0  # (local)
S_gauss_occ = 0.0  # (local)
for p, q in sectors:
    evals = eigenvalue_data[(p, q)]
    dpq = dim_pq(p, q)
    mult = dpq**2
    omega = np.abs(evals)
    v2 = bcs_occupation(omega, mu, Delta)
    f_gauss = np.exp(-omega**2)
    S_gauss_full += mult * np.sum(f_gauss)
    S_gauss_occ += mult * np.sum(v2 * f_gauss)

# For sharp cutoff at Lambda = M_KK = 1:
S_sharp_full = 0.0  # (local)
S_sharp_occ = 0.0  # (local)
for p, q in sectors:
    evals = eigenvalue_data[(p, q)]
    dpq = dim_pq(p, q)
    mult = dpq**2
    omega = np.abs(evals)
    v2 = bcs_occupation(omega, mu, Delta)
    f_sharp = (omega <= 1.0).astype(float)
    S_sharp_full += mult * np.sum(f_sharp)
    S_sharp_occ += mult * np.sum(v2 * f_sharp)

print(f"\n  Cutoff function comparison (Lambda = M_KK = 1):")
print(f"  {'Cutoff':>12} {'S_full':>12} {'S_occ':>12} {'ratio':>12}")
print(f"  {'|D|':>12} {S_full_total:12.2f} {S_occ_total:12.6f} {S_occ_total/S_full_total:12.6e}")
print(f"  {'Gaussian':>12} {S_gauss_full:12.2f} {S_gauss_occ:12.6f} {S_gauss_occ/S_gauss_full:12.6e}")
if S_sharp_full > 0:
    print(f"  {'Sharp':>12} {S_sharp_full:12.2f} {S_sharp_occ:12.6f} {S_sharp_occ/S_sharp_full:12.6e}")
else:
    print(f"  {'Sharp':>12} {'0':>12} {'0':>12} {'N/A':>12} (all evals > 1 M_KK)")

# =========================================================================
# 11. V^2 PROFILE ACROSS FULL SPECTRUM
# =========================================================================
print("\n--- 11. v^2 profile across spectrum ---")

# Collect all eigenvalue magnitudes with their sector info
all_omega = []
all_v2 = []
all_sector = []
all_mult = []

for p, q in sectors:
    evals = eigenvalue_data[(p, q)]
    dpq = dim_pq(p, q)
    omega = np.abs(evals)
    v2 = bcs_occupation(omega, mu, Delta)
    for j in range(len(evals)):
        all_omega.append(omega[j])
        all_v2.append(v2[j])
        all_sector.append(f"({p},{q})")
        all_mult.append(dpq**2)

all_omega = np.array(all_omega)
all_v2 = np.array(all_v2)
all_mult = np.array(all_mult)

# Sort by omega
sort_idx = np.argsort(all_omega)
all_omega = all_omega[sort_idx]
all_v2 = all_v2[sort_idx]
all_mult = all_mult[sort_idx]

# Weighted statistics
total_weight = np.sum(all_mult)
weighted_v2_mean = np.sum(all_mult * all_v2) / total_weight
weighted_v2_rms = np.sqrt(np.sum(all_mult * all_v2**2) / total_weight)

print(f"  Total base eigenvalues:     {len(all_omega)}")
print(f"  Weighted <v^2>:             {weighted_v2_mean:.6e}")
print(f"  Weighted rms(v^2):          {weighted_v2_rms:.6e}")
print(f"  Max v^2:                    {np.max(all_v2):.6f}")
print(f"  Min v^2:                    {np.min(all_v2):.6e}")

# =========================================================================
# 12. GATE VERDICT
# =========================================================================
print("\n" + "=" * 70)
print("GATE VERDICT: OCC-SPEC-64")
print("=" * 70)

print(f"\n  S_fold = {S_full_total:.2f}")
print(f"  S_occ  = {S_occ_total:.6f}")
print(f"  Ratio  = {S_occ_total / S_full_total:.6e}")
print(f"  N_eff  = {N_eff_SA:.2f}")
print(f"\n  A_s gap (full): {gap_full:.3f} OOM")
print(f"  A_s gap (occ):  {gap_occ:.3f} OOM")
print(f"  Gap reduction:  {abs(gap_full - gap_occ):.3f} OOM")

if S_occ_total < 100:
    print(f"\n  NOTABLE: S_occ = {S_occ_total:.2f} < 100")
    print(f"  => A_s problem SIGNIFICANTLY reduced")

print(f"\n  Gate: INFO (reporting S_occ value and revised A_s gap)")

elapsed = time.time() - t_start
print(f"\n  Computation time: {elapsed:.2f}s")

# =========================================================================
# 13. SAVE DATA
# =========================================================================
print("\n--- 13. Saving data ---")

save_path = os.path.join(SCRIPT_DIR, 's64_occ_spec.npz')
np.savez(save_path,
    # Key results
    S_fold=S_full_total,
    S_occ=S_occ_total,
    ratio_occ_fold=S_occ_total / S_full_total,
    N_eff_SA=N_eff_SA,
    N_eff_v2=N_eff_v2,
    gap_full=gap_full,
    gap_occ=gap_occ,
    gap_reduction=abs(gap_full - gap_occ),

    # BCS parameters
    Delta_BCS=Delta,
    mu_BCS=mu,

    # Sector results
    sectors=np.array([f"({p},{q})" for p,q in sectors]),
    sector_S_occ=np.array([sector_results[(p,q)]['S_occ'] for p,q in sectors]),
    sector_S_full=np.array([sector_results[(p,q)]['S_full'] for p,q in sectors]),
    sector_v2_mean=np.array([sector_results[(p,q)]['v2_mean'] for p,q in sectors]),

    # Profile data
    all_omega=all_omega,
    all_v2=all_v2,
    all_mult=all_mult,

    # Alternative cutoffs
    S_gauss_full=S_gauss_full,
    S_gauss_occ=S_gauss_occ,
    S_sharp_full=S_sharp_full,
    S_sharp_occ=S_sharp_occ,
)
print(f"  Saved to {save_path}")

# =========================================================================
# 14. PLOT
# =========================================================================
print("\n--- 14. Generating plot ---")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: v^2 vs |lambda|
ax = axes[0, 0]
# Continuous curve
omega_fine = np.linspace(0.5, 2.2, 500)
v2_fine = bcs_occupation(omega_fine, mu, Delta)
ax.plot(omega_fine, v2_fine, 'b-', linewidth=2, label=r'$v_k^2(\omega)$')
ax.axhline(0.5, color='gray', linestyle='--', alpha=0.5, label=r'$v^2 = 0.5$')
ax.axvline(mu, color='r', linestyle='--', alpha=0.7, label=r'$\mu = E_{B1}$')
ax.axvline(mu - Delta, color='orange', linestyle=':', alpha=0.7, label=r'$\mu - \Delta$')
ax.axvline(mu + Delta, color='orange', linestyle=':', alpha=0.7, label=r'$\mu + \Delta$')

# Mark the eigenvalue positions
for p, q in sectors:
    evals = eigenvalue_data[(p, q)]
    omega = np.sort(np.unique(np.round(np.abs(evals), 4)))
    v2 = bcs_occupation(omega, mu, Delta)
    marker = 'o' if p+q <= 1 else ('s' if p+q == 2 else ('^' if p+q == 3 else 'D'))
    ax.scatter(omega, v2, s=15, alpha=0.5, marker=marker, label=f'({p},{q})')

ax.set_xlabel(r'$|\lambda|$ (M$_{\rm KK}$)', fontsize=12)
ax.set_ylabel(r'$v_k^2$', fontsize=12)
ax.set_title(r'BCS occupation number $v_k^2$ vs eigenvalue', fontsize=13)
ax.legend(fontsize=7, ncol=3, loc='upper right')
ax.set_ylim(-0.05, 1.05)

# Panel 2: Sector contributions to S_occ
ax = axes[0, 1]
sector_names = [f"({p},{q})" for p,q in sectors]
S_occ_vals = [sector_results[(p,q)]['S_occ'] for p,q in sectors]
S_full_vals = [sector_results[(p,q)]['S_full'] for p,q in sectors]

x = np.arange(len(sectors))
width = 0.35  # (local)
bars1 = ax.bar(x - width/2, S_occ_vals, width, label=r'$S_{\rm occ}$', color='steelblue')
# S_full is much larger, use log scale
ax.set_yscale('log')
bars2 = ax.bar(x + width/2, S_full_vals, width, label=r'$S_{\rm full}$', color='salmon', alpha=0.7)
ax.set_xticks(x)
ax.set_xticklabels(sector_names, fontsize=9, rotation=45)
ax.set_ylabel('Spectral action contribution', fontsize=11)
ax.set_title('Sector contributions: full vs occupied', fontsize=13)
ax.legend(fontsize=10)

# Panel 3: Cumulative spectral action
ax = axes[1, 0]
# Sort all eigenvalues by magnitude and compute cumulative S_occ and S_full
omega_sorted = np.sort(all_omega)
cum_S_full = np.cumsum(all_mult[np.argsort(all_omega)] * all_omega[np.argsort(all_omega)])
cum_S_occ = np.cumsum(all_mult[np.argsort(all_omega)] * all_v2[np.argsort(all_omega)] * all_omega[np.argsort(all_omega)])

ax.plot(omega_sorted, cum_S_full / S_full_total, 'r-', linewidth=2, label=r'$S_{\rm full}$ (cumulative)')
ax.plot(omega_sorted, cum_S_occ / S_occ_total, 'b-', linewidth=2, label=r'$S_{\rm occ}$ (cumulative)')
ax.axvline(mu, color='gray', linestyle='--', alpha=0.5, label=r'$\mu$')
ax.axvline(mu + Delta, color='orange', linestyle=':', alpha=0.5, label=r'$\mu + \Delta$')
ax.set_xlabel(r'$|\lambda|$ (M$_{\rm KK}$)', fontsize=12)
ax.set_ylabel('Cumulative fraction', fontsize=12)
ax.set_title('Cumulative spectral action', fontsize=13)
ax.legend(fontsize=10)

# Panel 4: Summary text
ax = axes[1, 1]
ax.axis('off')
text = (
    f"OCC-SPEC-64: Occupied-State Spectral Action\n"
    f"{'='*42}\n\n"
    f"BCS parameters:\n"
    f"  $\\Delta$ = {Delta:.4f} M$_{{KK}}$\n"
    f"  $\\mu$ = {mu:.4f} M$_{{KK}}$\n\n"
    f"Results:\n"
    f"  $S_{{fold}}$ = {S_full_total:.2f}\n"
    f"  $S_{{occ}}$  = {S_occ_total:.4f}\n"
    f"  Ratio = {S_occ_total/S_full_total:.4e}\n\n"
    f"A$_s$ gap:\n"
    f"  Full: {gap_full:.3f} OOM\n"
    f"  Occ:  {gap_occ:.3f} OOM\n"
    f"  Reduction: {abs(gap_full - gap_occ):.3f} OOM\n\n"
    f"$N_{{eff}}$ = {N_eff_SA:.1f}\n\n"
    f"Gate: INFO"
)
ax.text(0.05, 0.95, text, transform=ax.transAxes, fontsize=11,
        verticalalignment='top', fontfamily='monospace',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.tight_layout()
plot_path = os.path.join(SCRIPT_DIR, 's64_occ_spec.png')
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"  Saved plot to {plot_path}")

print(f"\n  Total elapsed: {time.time() - t_start:.2f}s")
print("\nDONE.")
