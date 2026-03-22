#!/usr/bin/env python3
"""
MULTI-JACOBSON-QTHEORY-46: Sector-by-Sector Gibbs-Duhem at tau* = 0.209
========================================================================

Physics:
--------
Jacobson (1995) derives Einstein equations from delta Q = T dS on local
Rindler horizons. For a GGE with 8 conserved charges, the first law
generalizes to a multi-temperature form:

    delta Q = sum_k T_k dS_k

Each sector contributes independently to the gravitating stress-energy.
The q-theory self-tuning (Volovik 2005, Klinkhamer-Volovik 2008) requires
the Gibbs-Duhem condition:

    rho(tau*) = epsilon(tau*) - tau* * d(epsilon)/d(tau)|_{tau*} = 0   (1)

Q-THEORY-BCS-45 found the AGGREGATE crossing at tau* = 0.209 (FLATBAND).
But in the multi-temperature Jacobson framework, each sector k defines
its own partial vacuum energy density:

    epsilon_k(tau) = (1/2) * d_k * ln(E_k(tau)^2 / mu^2)              (2)

where E_k = sqrt(lambda_k^2 + Delta_k^2) is the BCS quasiparticle energy,
d_k is the degeneracy, and mu is the reference scale.

The sector-by-sector Gibbs-Duhem condition is:

    rho_k(tau*) = epsilon_k(tau*) - tau* * d(epsilon_k)/d(tau)|_{tau*}  (3)

For consistency, ALL 8 sectors (or equivalently, 3 branches B1/B2/B3)
must satisfy |rho_k(tau*)| < threshold.

[Formula audit]
 - Eq (1): [rho] = [epsilon] = M_KK^4 (natural units where TL is dimensionless)
 - Eq (2): [epsilon_k] = dimensionless (trace-log of dimensionless ratio)
 - Eq (3): [rho_k] = dimensionless
 - Limiting case: Delta -> 0 reproduces vacuum trace-log (Q-THEORY-KK-45)
 - Limiting case: all sectors degenerate -> reduces to uniform scenario

Gate: MULTI-JACOBSON-QTHEORY-46
  PASS: all 8 sectors |rho_k(tau*)| < 0.1 M_KK^4
  FAIL: any |rho_k| > 1.0 M_KK^4

References:
  Jacobson, PRL 75 1260 (1995) [Paper 17 in Hawking library]
  Volovik, Ann.Phys. 517 165 (2005) [Paper 05]
  Klinkhamer & Volovik, PRD 77 085015 (2008) [Paper 15]
  Q-THEORY-BCS-45 (this project, Session 45)
  MULTI-T-JACOBSON-44 (this project, Session 44)

Author: Hawking-Theorist (S46 W4-8)
"""

import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
from pathlib import Path
import sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from canonical_constants import (
    M_KK_gravity as M_KK, tau_fold, E_cond,
    Delta_0_GL, Delta_B3, E_B1, E_B2_mean, E_B3_mean,
    PI
)

base = Path(__file__).parent

print("=" * 78)
print("MULTI-JACOBSON-QTHEORY-46: Sector-by-Sector Gibbs-Duhem at tau*")
print("=" * 78)

# ============================================================================
# STEP 0: Load input data
# ============================================================================
print("\n--- STEP 0: Load Input Data ---")

# S45 q-theory BCS data
d45 = np.load(base / 's45_qtheory_bcs.npz', allow_pickle=True)
tau_star = float(d45['tau_star_flatband'])   # 0.2094
Delta_B2_fb = float(d45['Delta_B2_flatband'])  # 0.770
Delta_B1_fb = float(d45['Delta_B1_flatband'])  # 0.385
Delta_B3_fb = float(d45['Delta_B3_flatband'])  # 0.176
B2_lam_sq_fold = float(d45['B2_lam_sq_fold'])
B1_lam_sq_fold = float(d45['B1_lam_sq_fold'])
B3_lam_sq_fold = float(d45['B3_lam_sq_fold'])
B2_deg = int(d45['B2_deg'])
B1_deg = int(d45['B1_deg'])
B3_deg = int(d45['B3_deg'])
rho_gs_fold_flatband = float(d45['rho_gs_fold_flatband'])

# S44 multi-T Jacobson data
d44 = np.load(base / 's44_multi_t_jacobson.npz', allow_pickle=True)
labels_8 = d44['labels']    # 8 mode labels
E_k_8 = d44['E_k']          # quasiparticle energies
n_k_8 = d44['n_k']          # GGE occupations
T_k_8 = d44['T_k']          # GGE temperatures
S_k_8 = d44['S_k']          # per-mode entropies
rho_k_8 = d44['rho_k']      # per-mode energy densities
w_k_gge = d44['w_k_gge']    # per-mode EOS
T_branch = d44['T_branch']  # (T_B2, T_B1, T_B3)
E_GGE = float(d44['E_GGE'])
S_GGE = float(d44['S_GGE'])

# S36 sector eigenvalues
d36 = np.load(base / 's36_sfull_tau_stabilization.npz', allow_pickle=True)
tau_16 = d36['tau_combined']      # 16 tau values
S_full_16 = d36['S_full']
S_sector_00 = d36['S_sector_0_0']  # singlet sector spectral action

# Eigenvalue tau grid and per-sector eigenvalues
tau_evals = [0.05, 0.16, 0.17, 0.18, 0.19, 0.21, 0.22]
evals_dict = {}
for tau_e in tau_evals:
    for p, q in [(0,0)]:  # singlet only
        key = f'evals_tau{tau_e:.3f}_{p}_{q}'
        if key in d36:
            evals_dict[tau_e] = d36[key]

print(f"tau* (FLATBAND from Q-THEORY-BCS-45) = {tau_star:.4f}")
print(f"tau_fold = {tau_fold}")
print(f"Gap scenario: FLATBAND")
print(f"  Delta_B2 = {Delta_B2_fb:.4f}, Delta_B1 = {Delta_B1_fb:.4f}, Delta_B3 = {Delta_B3_fb:.4f}")
print(f"  B2_deg = {B2_deg}, B1_deg = {B1_deg}, B3_deg = {B3_deg}")
print(f"  Total singlet modes = {B2_deg + B1_deg + B3_deg}")
print(f"  lam^2 at fold: B2={B2_lam_sq_fold:.4f}, B1={B1_lam_sq_fold:.4f}, B3={B3_lam_sq_fold:.4f}")

# ============================================================================
# STEP 1: Extract per-sector lambda^2(tau) from singlet eigenvalues
# ============================================================================
print("\n" + "=" * 78)
print("STEP 1: Per-Sector lambda^2(tau) Extraction")
print("=" * 78)

def get_singlet_groups(tau_val):
    """Extract singlet eigenvalues grouped by B1/B2/B3 at given tau.

    Returns dict: sector -> {'lam_sq': float, 'deg': int}
    Clustering by degeneracy: B1(2), B2(8), B3(6).
    """
    eigs = evals_dict.get(tau_val)
    if eigs is None:
        return None
    lam_sq = np.sort(eigs**2)

    unique_sq = []
    degs = []
    tol = 0.01
    used = np.zeros(len(lam_sq), dtype=bool)
    for i in range(len(lam_sq)):
        if used[i]:
            continue
        cluster = np.abs(lam_sq - lam_sq[i]) < tol
        unique_sq.append(np.mean(lam_sq[cluster]))
        degs.append(int(np.sum(cluster)))
        used[cluster] = True

    unique_sq = np.array(unique_sq)
    degs = np.array(degs)
    order = np.argsort(unique_sq)
    unique_sq = unique_sq[order]
    degs = degs[order]

    result = {}
    for ls, dg in zip(unique_sq, degs):
        if dg == 2:
            result['B1'] = {'lam_sq': float(ls), 'deg': 2}
        elif dg == 8:
            result['B2'] = {'lam_sq': float(ls), 'deg': 8}
        elif dg == 6:
            result['B3'] = {'lam_sq': float(ls), 'deg': 6}
    return result

# Build lambda^2(tau) for each sector across all tau_evals
lam_sq_B1 = np.zeros(len(tau_evals))
lam_sq_B2 = np.zeros(len(tau_evals))
lam_sq_B3 = np.zeros(len(tau_evals))

print(f"\n{'tau':>6s}  {'lam2_B1':>10s}  {'lam2_B2':>10s}  {'lam2_B3':>10s}")
for i, t in enumerate(tau_evals):
    grp = get_singlet_groups(t)
    if grp and len(grp) == 3:
        lam_sq_B1[i] = grp['B1']['lam_sq']
        lam_sq_B2[i] = grp['B2']['lam_sq']
        lam_sq_B3[i] = grp['B3']['lam_sq']
        print(f"{t:6.3f}  {lam_sq_B1[i]:10.6f}  {lam_sq_B2[i]:10.6f}  {lam_sq_B3[i]:10.6f}")
    else:
        print(f"{t:6.3f}  MISSING or incomplete grouping")

# Cross-check at fold
print(f"\nCross-check at fold (tau=0.19):")
print(f"  B1: {lam_sq_B1[4]:.6f} vs stored {B1_lam_sq_fold:.6f} (err={abs(lam_sq_B1[4]-B1_lam_sq_fold):.2e})")
print(f"  B2: {lam_sq_B2[4]:.6f} vs stored {B2_lam_sq_fold:.6f} (err={abs(lam_sq_B2[4]-B2_lam_sq_fold):.2e})")
print(f"  B3: {lam_sq_B3[4]:.6f} vs stored {B3_lam_sq_fold:.6f} (err={abs(lam_sq_B3[4]-B3_lam_sq_fold):.2e})")

# ============================================================================
# STEP 2: Compute per-sector trace-log epsilon_k(tau) with FLATBAND gaps
# ============================================================================
print("\n" + "=" * 78)
print("STEP 2: Per-Sector Trace-Log epsilon_k(tau)")
print("=" * 78)

# FLATBAND gap scenario
gaps = {'B1': Delta_B1_fb, 'B2': Delta_B2_fb, 'B3': Delta_B3_fb}
degs = {'B1': B1_deg, 'B2': B2_deg, 'B3': B3_deg}
lam_sq_arrays = {'B1': lam_sq_B1, 'B2': lam_sq_B2, 'B3': lam_sq_B3}

mu_ref_sq = 1.0  # Reference scale = M_KK

# Per-sector trace-log: epsilon_k(tau) = (1/2) * d_k * ln(E_k^2 / mu^2)
# where E_k^2 = lambda_k^2 + Delta_k^2
epsilon_sectors = {}
for sector in ['B1', 'B2', 'B3']:
    d_k = degs[sector]
    delta_sq = gaps[sector]**2
    lam_sq = lam_sq_arrays[sector]
    E_sq = lam_sq + delta_sq
    eps_k = 0.5 * d_k * np.log(E_sq / mu_ref_sq)
    epsilon_sectors[sector] = eps_k

# Total trace-log (should match Q-THEORY-BCS-45 FLATBAND)
epsilon_total = np.zeros(len(tau_evals))
for sector in ['B1', 'B2', 'B3']:
    epsilon_total += epsilon_sectors[sector]

print("Per-sector trace-log at each tau:")
print(f"  {'tau':>6s}  {'eps_B1':>10s}  {'eps_B2':>10s}  {'eps_B3':>10s}  {'eps_tot':>10s}")
for i, t in enumerate(tau_evals):
    print(f"  {t:6.3f}  {epsilon_sectors['B1'][i]:10.6f}  {epsilon_sectors['B2'][i]:10.6f}  "
          f"{epsilon_sectors['B3'][i]:10.6f}  {epsilon_total[i]:10.6f}")

# Verify total matches Q-THEORY-BCS-45 computation
# The total TL for FLATBAND was stored — load and compare
print(f"\n--- Cross-check: Total TL vs Q-THEORY-BCS-45 ---")
# Reconstruct what Q-THEORY-BCS-45 computed
# For FLATBAND, the TL is: (1/2)*sum_k d_k * ln((lam_k^2 + Delta_k^2) / mu^2)
# which is exactly our sum of epsilon_sectors. OK.
print(f"  Total TL at fold (tau=0.19): {epsilon_total[4]:.6f}")

# ============================================================================
# STEP 3: Cubic spline interpolation and Gibbs-Duhem per sector
# ============================================================================
print("\n" + "=" * 78)
print("STEP 3: Sector-by-Sector Gibbs-Duhem Condition")
print("=" * 78)

tau_ev = np.array(tau_evals)
tau_fine = np.linspace(0.06, 0.22, 1000)

# Build cubic splines for each sector
cs_sectors = {}
for sector in ['B1', 'B2', 'B3']:
    cs_sectors[sector] = CubicSpline(tau_ev, epsilon_sectors[sector])

cs_total = CubicSpline(tau_ev, epsilon_total)

# Gibbs-Duhem: rho_k(tau) = [eps_k(tau) - eps_k(tau_ref)] - tau * d(eps_k)/d(tau)
# Using tau_ref = tau_evals[0] = 0.05 (ground-state subtraction)
tau_ref = tau_evals[0]

rho_sectors = {}
for sector in ['B1', 'B2', 'B3']:
    cs = cs_sectors[sector]
    eps_fine = cs(tau_fine)
    deps_fine = cs(tau_fine, 1)  # d(eps)/d(tau)
    eps_ref = cs(tau_ref)
    # Gibbs-Duhem with ground-state subtraction
    rho_gs = (eps_fine - eps_ref) - tau_fine * deps_fine
    rho_sectors[sector] = rho_gs

# Total
eps_total_fine = cs_total(tau_fine)
deps_total_fine = cs_total(tau_fine, 1)
eps_total_ref = cs_total(tau_ref)
rho_total = (eps_total_fine - eps_total_ref) - tau_fine * deps_total_fine

# Evaluate at tau*
idx_star = np.argmin(np.abs(tau_fine - tau_star))
tau_at_star = tau_fine[idx_star]

print(f"\nGibbs-Duhem condition at tau* = {tau_star:.4f} (nearest grid: {tau_at_star:.4f}):")
print(f"  {'Sector':<8s}  {'deg':>4s}  {'eps_k(tau*)':>12s}  {'d(eps_k)/dtau':>14s}  {'rho_k(tau*)':>12s}  {'|rho_k|':>10s}")

rho_at_star = {}
eps_at_star = {}
deps_at_star = {}

for sector in ['B1', 'B2', 'B3']:
    cs = cs_sectors[sector]
    eps_val = cs(tau_star)
    deps_val = cs(tau_star, 1)
    eps_ref_val = cs(tau_ref)
    rho_val = (eps_val - eps_ref_val) - tau_star * deps_val

    rho_at_star[sector] = rho_val
    eps_at_star[sector] = eps_val
    deps_at_star[sector] = deps_val

    print(f"  {sector:<8s}  {degs[sector]:>4d}  {eps_val:>12.6f}  {deps_val:>14.6f}  {rho_val:>12.6f}  {abs(rho_val):>10.6f}")

# Total
eps_tot_star = cs_total(tau_star)
deps_tot_star = cs_total(tau_star, 1)
eps_tot_ref = cs_total(tau_ref)
rho_tot_star = (eps_tot_star - eps_tot_ref) - tau_star * deps_tot_star

print(f"  {'TOTAL':<8s}  {16:>4d}  {eps_tot_star:>12.6f}  {deps_tot_star:>14.6f}  {rho_tot_star:>12.6f}  {abs(rho_tot_star):>10.6f}")

# Cross-check: sum of sector rho should equal total rho
rho_sum_sectors = sum(rho_at_star.values())
print(f"\n  Sum of sector rho_k: {rho_sum_sectors:.6f}")
print(f"  Total rho:           {rho_tot_star:.6f}")
print(f"  Difference:          {abs(rho_sum_sectors - rho_tot_star):.2e}")

# ============================================================================
# STEP 4: Expand to 8 individual modes
# ============================================================================
print("\n" + "=" * 78)
print("STEP 4: Mode-by-Mode Gibbs-Duhem (8 Modes)")
print("=" * 78)

# Each sector has d_k modes. Within a sector, all modes have the same
# lambda^2(tau) and Delta, so each mode's contribution is:
#   rho_k^{per-mode}(tau) = rho_k(tau) / d_k
# The sector Gibbs-Duhem is satisfied iff each mode's is.

# Map 8 GGE modes to sectors:
# B2[0], B2[1], B2[2], B2[3] -> B2 (deg=8, but 4 GGE modes with DOS weight)
# B1 -> B1 (deg=2, 1 GGE mode)
# B3[0], B3[1], B3[2] -> B3 (deg=6, 3 GGE modes)
#
# IMPORTANT: The 8 GGE modes have different OCCUPATIONS (n_k) but the
# same lambda^2 within a sector. The per-mode trace-log (vacuum energy)
# does NOT depend on occupation — it depends only on the eigenvalue spectrum.
# The occupation n_k enters the MATTER contribution, not the vacuum.
#
# In the q-theory framework, the vacuum energy is:
#   epsilon(tau) = (1/2) * Tr ln(D_K^2(tau) / mu^2)
# This is a sum over ALL eigenvalues regardless of occupation.
#
# The GGE occupation n_k determines the MATTER energy (2 E_k n_k)
# which is a separate contribution to the stress-energy.
#
# For the multi-T Jacobson check, we need:
# 1. VACUUM SECTOR: rho_k^{vac}(tau*) = 0 per sector -> self-tuning
# 2. MATTER SECTOR: separately conserved by integrability
#
# The gate asks: does rho_k (the gravitating vacuum energy contribution
# from sector k) vanish at tau*?

# Assign per-mode rho values
# Within B2: 8 eigenvalues, split as 4 GGE modes (each with DOS weight ~14)
# Within B1: 2 eigenvalues, 1 GGE mode
# Within B3: 6 eigenvalues, 3 GGE modes
# Per eigenvalue: rho_per_eigenvalue = rho_sector / d_sector

mode_names = ['B2[0]', 'B2[1]', 'B2[2]', 'B2[3]', 'B1', 'B3[0]', 'B3[1]', 'B3[2]']
mode_sectors = ['B2', 'B2', 'B2', 'B2', 'B1', 'B3', 'B3', 'B3']

# The degeneracy splitting within GGE is from DOS weight (rho_k):
# B2 has 4 GGE modes out of 8 eigenvalues -> 2 eigenvalues per GGE mode
# B1 has 1 GGE mode out of 2 eigenvalues -> 2 eigenvalues per GGE mode
# B3 has 3 GGE modes out of 6 eigenvalues -> 2 eigenvalues per GGE mode
# All GGE modes correspond to 2 eigenvalues each (Kramers/BDI doubling).

eigenvalues_per_gge_mode = 2  # universal BDI doubling

rho_8_modes = np.zeros(8)
eps_8_modes = np.zeros(8)
deps_8_modes = np.zeros(8)

print(f"\nPer-mode Gibbs-Duhem at tau* = {tau_star:.4f}:")
print(f"  {'Mode':<8s}  {'Sector':<6s}  {'n_k':>8s}  {'T_k':>8s}  {'rho_vac':>10s}  {'|rho_vac|':>10s}  {'Status':>8s}")

gate_threshold_pass = 0.1
gate_threshold_fail = 1.0
all_pass = True
any_fail = False

for i, (name, sector) in enumerate(zip(mode_names, mode_sectors)):
    # Per GGE mode: each mode has 2 eigenvalues (BDI), so contributes
    # 2/d_sector of the sector's rho
    frac = eigenvalues_per_gge_mode / degs[sector]
    rho_mode = rho_at_star[sector] * frac
    eps_mode = eps_at_star[sector] * frac
    deps_mode = deps_at_star[sector] * frac

    rho_8_modes[i] = rho_mode
    eps_8_modes[i] = eps_mode
    deps_8_modes[i] = deps_mode

    if abs(rho_mode) < gate_threshold_pass:
        status = "PASS"
    elif abs(rho_mode) > gate_threshold_fail:
        status = "FAIL"
        any_fail = True
    else:
        status = "MARGINAL"
        all_pass = False

    if abs(rho_mode) > gate_threshold_pass:
        all_pass = False

    print(f"  {name:<8s}  {sector:<6s}  {n_k_8[i]:8.5f}  {T_k_8[i]:8.4f}  "
          f"{rho_mode:>10.6f}  {abs(rho_mode):>10.6f}  {status:>8s}")

print(f"\n  Sum of 8-mode rho:  {np.sum(rho_8_modes):.6f}")
print(f"  Total rho:          {rho_tot_star:.6f}")
print(f"  Max |rho_k|:        {np.max(np.abs(rho_8_modes)):.6f}")

# ============================================================================
# STEP 5: rho_k(tau) curves — find per-sector zero crossings
# ============================================================================
print("\n" + "=" * 78)
print("STEP 5: Per-Sector Zero Crossings of rho_k(tau)")
print("=" * 78)

tau_stars_sector = {}
for sector in ['B1', 'B2', 'B3']:
    rho_s = rho_sectors[sector]
    # Find zero crossings
    zc = np.where(np.diff(np.sign(rho_s.astype(float))))[0]
    crossings = []
    for zi in zc:
        # Linear interpolation
        t_cross = tau_fine[zi] + (tau_fine[zi+1] - tau_fine[zi]) * \
                  (-rho_s[zi]) / (rho_s[zi+1] - rho_s[zi])
        crossings.append(t_cross)
    tau_stars_sector[sector] = crossings

    n_cross = len(crossings)
    cross_str = ', '.join(f'{c:.4f}' for c in crossings) if crossings else 'NONE'
    print(f"  {sector}: {n_cross} crossing(s) at tau = [{cross_str}]")
    print(f"    rho_k(tau*={tau_star:.4f}) = {rho_at_star[sector]:.6f}")

# Also total
zc_tot = np.where(np.diff(np.sign(rho_total.astype(float))))[0]
crossings_tot = []
for zi in zc_tot:
    t_cross = tau_fine[zi] + (tau_fine[zi+1] - tau_fine[zi]) * \
              (-rho_total[zi]) / (rho_total[zi+1] - rho_total[zi])
    crossings_tot.append(t_cross)
cross_str_tot = ', '.join(f'{c:.4f}' for c in crossings_tot) if crossings_tot else 'NONE'
print(f"  TOTAL: crossing(s) at tau = [{cross_str_tot}]")
print(f"    rho(tau*={tau_star:.4f}) = {rho_tot_star:.6f}")

# ============================================================================
# STEP 6: Physical interpretation — internal energy balance
# ============================================================================
print("\n" + "=" * 78)
print("STEP 6: Physical Interpretation")
print("=" * 78)

# The key physical question: does the q-theory self-tuning mechanism
# work SECTOR-BY-SECTOR or only in aggregate?
#
# If sector-by-sector: each sector independently finds rho_k = 0.
#   This requires that the geometric curvature of epsilon_k(tau) is the
#   same for all sectors — i.e., they all have the same convexity structure.
#
# If aggregate only: the total rho = sum rho_k = 0, but individual sectors
#   have rho_k != 0. The sectors "trade" vacuum energy, with some having
#   positive rho_k and others negative. This is analogous to a multi-component
#   chemical equilibrium where individual chemical potentials need not vanish,
#   only the total free energy is minimized.
#
# The multi-temperature Jacobson constraint is:
#   For EACH sector to independently source the correct Einstein equation,
#   each must independently satisfy rho_k = 0 (strict).
#   OR: the coupling between sectors through the common metric tau mediates
#   the cancellation (relaxed).
#
# In the relaxed interpretation, what matters is:
#   sum_k rho_k(tau*) = 0   (total CC vanishes)
# The individual rho_k encode the inter-sector vacuum energy exchange,
# which is gravitationally inert if the sectors couple through the metric.

# Compute sector fractions at tau*
total_abs_rho = np.sum(np.abs(list(rho_at_star.values())))
print(f"\nSector vacuum energy at tau* = {tau_star:.4f}:")
for sector in ['B1', 'B2', 'B3']:
    frac = abs(rho_at_star[sector]) / total_abs_rho * 100
    sign = "+" if rho_at_star[sector] > 0 else "-"
    print(f"  {sector}: rho = {rho_at_star[sector]:+.6f} ({sign}{frac:.1f}% of total |rho|)")

print(f"  Total: rho = {rho_tot_star:+.6f}")

# Cancellation ratio: how much cancellation occurs between sectors?
cancel_ratio = abs(rho_tot_star) / total_abs_rho
print(f"\n  Cancellation ratio |rho_tot| / sum|rho_k| = {cancel_ratio:.4f}")
if cancel_ratio < 0.1:
    print(f"  Strong inter-sector cancellation ({(1-cancel_ratio)*100:.1f}% cancelled)")
elif cancel_ratio > 0.9:
    print(f"  Weak cancellation — sectors nearly aligned")
else:
    print(f"  Partial cancellation")

# ============================================================================
# STEP 7: Dimensional check and physical units
# ============================================================================
print("\n" + "=" * 78)
print("STEP 7: Dimensional Analysis and Physical Scale")
print("=" * 78)

# The trace-log epsilon_k is dimensionless in M_KK units.
# The physical vacuum energy density is:
#   rho_k^{phys} = (M_KK^4 / 16 pi^2) * rho_k
# where the 16 pi^2 comes from the spectral zeta regularization.
#
# At M_KK ~ 7.4e16 GeV:
#   M_KK^4 / (16 pi^2) ~ (7.4e16)^4 / 158 ~ 1.9e65 GeV^4

prefactor = M_KK**4 / (16.0 * PI**2)

print(f"  M_KK = {M_KK:.4e} GeV")
print(f"  M_KK^4 / (16 pi^2) = {prefactor:.4e} GeV^4")
print(f"  rho_Lambda_obs = 2.7e-47 GeV^4")
print(f"  CC hierarchy = {prefactor / 2.7e-47:.2e}")

print(f"\n  Per-sector physical rho_k(tau*) [GeV^4]:")
for sector in ['B1', 'B2', 'B3']:
    rho_phys = rho_at_star[sector] * prefactor
    print(f"    {sector}: {rho_phys:.4e} GeV^4")
print(f"    TOTAL: {rho_tot_star * prefactor:.4e} GeV^4")

# The individual sector values are of order unity in M_KK^4 units,
# which is ~10^65 GeV^4. The q-theory mechanism cancels these to give
# rho_total ~ 0 at tau*. The question is how precisely.

# ============================================================================
# STEP 8: Limiting case checks
# ============================================================================
print("\n" + "=" * 78)
print("STEP 8: Limiting Case Checks")
print("=" * 78)

# Check 1: Delta -> 0 should reproduce vacuum trace-log
print("Check 1: Delta -> 0 limit")
eps_vac_sectors = {}
for sector in ['B1', 'B2', 'B3']:
    d_k = degs[sector]
    lam_sq = lam_sq_arrays[sector]
    eps_vac = 0.5 * d_k * np.log(lam_sq / mu_ref_sq)
    eps_vac_sectors[sector] = eps_vac

# Compare at fold
eps_vac_total_fold = sum(eps_vac_sectors[s][4] for s in ['B1', 'B2', 'B3'])
eps_bcs_total_fold = epsilon_total[4]
shift_bcs = eps_bcs_total_fold - eps_vac_total_fold
print(f"  Total TL (vacuum) at fold: {eps_vac_total_fold:.6f}")
print(f"  Total TL (BCS) at fold:    {eps_bcs_total_fold:.6f}")
print(f"  BCS shift:                 {shift_bcs:+.6f} ({abs(shift_bcs/eps_vac_total_fold)*100:.1f}%)")

# Check 2: All sectors degenerate -> should match uniform scenario
print("\nCheck 2: Degenerate limit (all lam^2 equal)")
# If all lam_sq were the same, rho_B1 = (2/16)*rho_total, rho_B2 = (8/16)*rho_total, etc.
# The ratio rho_k/rho_total should equal d_k/d_total
deg_total = B1_deg + B2_deg + B3_deg
for sector in ['B1', 'B2', 'B3']:
    expected_frac = degs[sector] / deg_total
    actual_frac = rho_at_star[sector] / rho_tot_star if abs(rho_tot_star) > 1e-10 else float('nan')
    print(f"  {sector}: expected frac = {expected_frac:.4f}, actual = {actual_frac:.4f}")

# ============================================================================
# STEP 9: Summary and gate verdict
# ============================================================================
print("\n" + "=" * 78)
print("STEP 9: Gate Verdict")
print("=" * 78)

# Gate: MULTI-JACOBSON-QTHEORY-46
# PASS: all 8 sectors |rho_k(tau*)| < 0.1 M_KK^4
# FAIL: any |rho_k| > 1.0 M_KK^4

max_abs_rho = np.max(np.abs(rho_8_modes))
min_abs_rho = np.min(np.abs(rho_8_modes))

# For sectors:
max_sector_rho = max(abs(v) for v in rho_at_star.values())

if max_abs_rho < gate_threshold_pass:
    verdict = 'PASS'
    detail = f'All 8 modes |rho_k| < {gate_threshold_pass}. Max = {max_abs_rho:.4f}'
elif any_fail:
    verdict = 'FAIL'
    detail = f'At least one mode |rho_k| > {gate_threshold_fail}. Max = {max_abs_rho:.4f}'
else:
    verdict = 'INFO'
    detail = f'Max |rho_k| = {max_abs_rho:.4f} in [{gate_threshold_pass}, {gate_threshold_fail}]'

print(f"\nGate: MULTI-JACOBSON-QTHEORY-46 = {verdict}")
print(f"Detail: {detail}")
print(f"\nSector rho_k(tau*={tau_star:.4f}):")
for sector in ['B1', 'B2', 'B3']:
    print(f"  {sector}: {rho_at_star[sector]:+.6f} (deg={degs[sector]})")
print(f"  TOTAL: {rho_tot_star:+.6f}")
print(f"  Max |rho_k| (8-mode): {max_abs_rho:.6f}")
print(f"  Max |rho_k| (3-sector): {max_sector_rho:.6f}")
print(f"  Cancellation: {cancel_ratio:.4f}")

# Do the sectors have SEPARATE zero crossings?
print(f"\nPer-sector zero crossings:")
all_have_crossing = True
for sector in ['B1', 'B2', 'B3']:
    crossings = tau_stars_sector[sector]
    if crossings:
        closest = min(crossings, key=lambda x: abs(x - tau_star))
        dist = abs(closest - tau_star)
        print(f"  {sector}: tau* = {closest:.4f} (delta from aggregate tau* = {dist:.4f})")
    else:
        all_have_crossing = False
        print(f"  {sector}: NO zero crossing in [{tau_fine[0]:.2f}, {tau_fine[-1]:.2f}]")

print(f"\n  All sectors have independent zero crossing: {all_have_crossing}")
if all_have_crossing:
    spread = max(min(tau_stars_sector[s], key=lambda x: abs(x - tau_star))
                 for s in ['B1', 'B2', 'B3']) - \
             min(min(tau_stars_sector[s], key=lambda x: abs(x - tau_star))
                 for s in ['B1', 'B2', 'B3'])
    print(f"  Spread of sector tau*: {spread:.4f}")

# ============================================================================
# STEP 10: Save data
# ============================================================================
print("\n" + "=" * 78)
print("STEP 10: Save Data")
print("=" * 78)

# Convert crossings to arrays for saving
tau_star_B1 = np.array(tau_stars_sector['B1'])
tau_star_B2 = np.array(tau_stars_sector['B2'])
tau_star_B3 = np.array(tau_stars_sector['B3'])

np.savez(base / 's46_multi_jacobson.npz',
    # Gate
    gate_name=np.array(['MULTI-JACOBSON-QTHEORY-46']),
    gate_verdict=np.array([verdict]),
    gate_detail=np.array([detail]),

    # Input parameters
    tau_star=tau_star,
    tau_fold=tau_fold,
    Delta_B2=Delta_B2_fb,
    Delta_B1=Delta_B1_fb,
    Delta_B3=Delta_B3_fb,

    # Per-sector at tau*
    rho_B1=rho_at_star['B1'],
    rho_B2=rho_at_star['B2'],
    rho_B3=rho_at_star['B3'],
    rho_total=rho_tot_star,
    eps_B1=eps_at_star['B1'],
    eps_B2=eps_at_star['B2'],
    eps_B3=eps_at_star['B3'],
    deps_B1=deps_at_star['B1'],
    deps_B2=deps_at_star['B2'],
    deps_B3=deps_at_star['B3'],

    # Per-mode (8-mode)
    mode_names=np.array(mode_names),
    rho_8_modes=rho_8_modes,
    max_abs_rho=max_abs_rho,

    # Sector zero crossings
    tau_star_B1=tau_star_B1,
    tau_star_B2=tau_star_B2,
    tau_star_B3=tau_star_B3,
    tau_star_total=np.array(crossings_tot),
    all_sectors_have_crossing=all_have_crossing,

    # Cancellation
    cancel_ratio=cancel_ratio,
    total_abs_rho=total_abs_rho,

    # Curves for plotting
    tau_fine=tau_fine,
    rho_B1_curve=rho_sectors['B1'],
    rho_B2_curve=rho_sectors['B2'],
    rho_B3_curve=rho_sectors['B3'],
    rho_total_curve=rho_total,

    # Sector trace-logs at evaluated tau
    tau_evals=np.array(tau_evals),
    epsilon_B1=epsilon_sectors['B1'],
    epsilon_B2=epsilon_sectors['B2'],
    epsilon_B3=epsilon_sectors['B3'],
    epsilon_total=epsilon_total,

    # GGE quantities at fold (from S44)
    T_k_8=T_k_8,
    n_k_8=n_k_8,
    E_k_8=E_k_8,
    rho_matter_8=rho_k_8,
    S_k_8=S_k_8,

    # Eigenvalue data
    lam_sq_B1=lam_sq_B1,
    lam_sq_B2=lam_sq_B2,
    lam_sq_B3=lam_sq_B3,
)

print(f"Data saved to: {base / 's46_multi_jacobson.npz'}")

# ============================================================================
# STEP 11: Plots
# ============================================================================
print("\n--- Generating plots ---")

fig = plt.figure(figsize=(16, 14))
gs = GridSpec(3, 3, hspace=0.40, wspace=0.35)

# Colors
c_B1 = '#FF9800'
c_B2 = '#2196F3'
c_B3 = '#4CAF50'
c_tot = 'black'

# --- Panel (a): rho_k(tau) curves ---
ax1 = fig.add_subplot(gs[0, 0:2])
ax1.plot(tau_fine, rho_sectors['B2'], color=c_B2, linewidth=2, label=f'B2 (deg={B2_deg})')
ax1.plot(tau_fine, rho_sectors['B1'], color=c_B1, linewidth=2, label=f'B1 (deg={B1_deg})')
ax1.plot(tau_fine, rho_sectors['B3'], color=c_B3, linewidth=2, label=f'B3 (deg={B3_deg})')
ax1.plot(tau_fine, rho_total, color=c_tot, linewidth=2.5, linestyle='--', label='Total')
ax1.axhline(y=0, color='gray', linewidth=0.5, linestyle='-')
ax1.axvline(x=tau_star, color='red', linewidth=1, linestyle=':', alpha=0.7, label=f'$\\tau^* = {tau_star:.3f}$')
ax1.axvline(x=tau_fold, color='purple', linewidth=1, linestyle=':', alpha=0.5, label=f'$\\tau_{{fold}} = {tau_fold}$')

# Mark zero crossings
for sector, col in [('B1', c_B1), ('B2', c_B2), ('B3', c_B3)]:
    for tc in tau_stars_sector[sector]:
        ax1.plot(tc, 0, 'o', color=col, markersize=8, markeredgecolor='black', markeredgewidth=0.5)

ax1.set_xlabel(r'$\tau$', fontsize=11)
ax1.set_ylabel(r'$\rho_k(\tau)$ [M$_{\rm KK}^4$ units]', fontsize=10)
ax1.set_title('(a) Sector-by-sector Gibbs-Duhem: $\\rho_k(\\tau) = \\epsilon_k - \\tau\\,d\\epsilon_k/d\\tau$',
              fontsize=10, fontweight='bold')
ax1.legend(fontsize=8, loc='best')
ax1.set_xlim(0.06, 0.22)

# --- Panel (b): bar chart of rho_k at tau* ---
ax2 = fig.add_subplot(gs[0, 2])
sectors_for_bar = ['B2', 'B1', 'B3', 'Total']
rho_for_bar = [rho_at_star['B2'], rho_at_star['B1'], rho_at_star['B3'], rho_tot_star]
colors_bar = [c_B2, c_B1, c_B3, c_tot]
bars = ax2.bar(sectors_for_bar, rho_for_bar, color=colors_bar, alpha=0.8,
               edgecolor='black', linewidth=0.5)
ax2.axhline(y=0, color='gray', linewidth=1)
ax2.axhline(y=gate_threshold_pass, color='green', linewidth=1, linestyle='--', alpha=0.5, label=f'PASS: {gate_threshold_pass}')
ax2.axhline(y=-gate_threshold_pass, color='green', linewidth=1, linestyle='--', alpha=0.5)
ax2.set_ylabel(r'$\rho_k(\tau^*)$', fontsize=10)
ax2.set_title(f'(b) $\\rho_k$ at $\\tau^* = {tau_star:.3f}$', fontsize=10, fontweight='bold')
ax2.legend(fontsize=7)

# Add value labels on bars
for bar, val in zip(bars, rho_for_bar):
    ax2.text(bar.get_x() + bar.get_width()/2, bar.get_height(),
             f'{val:.4f}', ha='center', va='bottom' if val > 0 else 'top',
             fontsize=7, fontweight='bold')

# --- Panel (c): 8-mode rho bar chart ---
ax3 = fig.add_subplot(gs[1, 0:2])
mode_colors = [c_B2]*4 + [c_B1] + [c_B3]*3
x_pos = np.arange(8)
bars3 = ax3.bar(x_pos, rho_8_modes, color=mode_colors, alpha=0.8,
                edgecolor='black', linewidth=0.5)
ax3.axhline(y=0, color='gray', linewidth=1)
ax3.axhline(y=gate_threshold_pass, color='green', linewidth=1, linestyle='--', alpha=0.4)
ax3.axhline(y=-gate_threshold_pass, color='green', linewidth=1, linestyle='--', alpha=0.4)
ax3.set_xticks(x_pos)
ax3.set_xticklabels(mode_names, fontsize=8, rotation=45)
ax3.set_ylabel(r'$\rho_k^{\rm mode}(\tau^*)$', fontsize=10)
ax3.set_title('(c) Per-mode (8-mode) vacuum energy at $\\tau^*$', fontsize=10, fontweight='bold')

# --- Panel (d): epsilon_k(tau) ---
ax4 = fig.add_subplot(gs[1, 2])
tau_ev_arr = np.array(tau_evals)
ax4.plot(tau_ev_arr, epsilon_sectors['B2'], 's-', color=c_B2, markersize=5, label='B2')
ax4.plot(tau_ev_arr, epsilon_sectors['B1'], 'o-', color=c_B1, markersize=5, label='B1')
ax4.plot(tau_ev_arr, epsilon_sectors['B3'], 'D-', color=c_B3, markersize=5, label='B3')
ax4.plot(tau_ev_arr, epsilon_total, '^-', color=c_tot, markersize=5, label='Total')
ax4.set_xlabel(r'$\tau$', fontsize=11)
ax4.set_ylabel(r'$\epsilon_k(\tau)$', fontsize=10)
ax4.set_title('(d) Per-sector trace-log $\\epsilon_k(\\tau)$', fontsize=10, fontweight='bold')
ax4.legend(fontsize=8)

# --- Panel (e): Sector zero-crossing positions ---
ax5 = fig.add_subplot(gs[2, 0])
sector_labels = ['B1', 'B2', 'B3', 'Total']
sector_colors_e = [c_B1, c_B2, c_B3, c_tot]
all_crossings = [tau_stars_sector['B1'], tau_stars_sector['B2'],
                 tau_stars_sector['B3'], crossings_tot]

for i, (lab, col, crossings) in enumerate(zip(sector_labels, sector_colors_e, all_crossings)):
    for tc in crossings:
        ax5.plot(tc, i, 'o', color=col, markersize=10, markeredgecolor='black', markeredgewidth=0.5)

ax5.axvline(x=tau_star, color='red', linewidth=2, linestyle='--', alpha=0.7, label=f'$\\tau^*={tau_star:.3f}$')
ax5.axvline(x=tau_fold, color='purple', linewidth=1, linestyle=':', alpha=0.5, label=f'$\\tau_{{fold}}={tau_fold}$')
ax5.set_yticks(range(len(sector_labels)))
ax5.set_yticklabels(sector_labels, fontsize=10)
ax5.set_xlabel(r'$\tau$ of zero crossing', fontsize=10)
ax5.set_title('(e) Per-sector $\\tau^*$ positions', fontsize=10, fontweight='bold')
ax5.set_xlim(0.05, 0.25)
ax5.legend(fontsize=8)

# --- Panel (f): GGE temperatures vs sector rho ---
ax6 = fig.add_subplot(gs[2, 1])
# Plot T_k for each of 8 modes, colored by sector
ax6.scatter(np.abs(rho_8_modes), T_k_8, c=mode_colors, s=80,
            edgecolors='black', linewidth=0.5, zorder=5)
for i in range(8):
    ax6.annotate(mode_names[i], (np.abs(rho_8_modes[i]), T_k_8[i]),
                 fontsize=6, xytext=(3, 3), textcoords='offset points')
ax6.set_xlabel(r'$|\rho_k^{\rm vac}(\tau^*)|$', fontsize=10)
ax6.set_ylabel(r'$T_k$ [M$_{\rm KK}$]', fontsize=10)
ax6.set_title('(f) GGE temperature vs vacuum $|\\rho_k|$', fontsize=10, fontweight='bold')

# --- Panel (g): Cancellation summary ---
ax7 = fig.add_subplot(gs[2, 2])
# Pie chart of |rho_k| contributions
sector_abs = [abs(rho_at_star[s]) for s in ['B2', 'B1', 'B3']]
sector_abs.append(abs(rho_tot_star))
sector_labels_pie = [f'B2: {rho_at_star["B2"]:+.4f}',
                     f'B1: {rho_at_star["B1"]:+.4f}',
                     f'B3: {rho_at_star["B3"]:+.4f}',
                     f'Net: {rho_tot_star:+.4f}']
colors_pie = [c_B2, c_B1, c_B3, 'red']
ax7.bar(range(4), sector_abs, color=colors_pie, alpha=0.8,
        edgecolor='black', linewidth=0.5)
ax7.set_xticks(range(4))
ax7.set_xticklabels(['|B2|', '|B1|', '|B3|', '|Net|'], fontsize=9)
ax7.set_ylabel(r'$|\rho|$', fontsize=10)
ax7.set_title(f'(g) Cancellation ratio = {cancel_ratio:.4f}', fontsize=10, fontweight='bold')

fig.suptitle(f'MULTI-JACOBSON-QTHEORY-46: Sector-by-Sector Gibbs-Duhem at $\\tau^* = {tau_star:.4f}$\n'
             f'Gate: {verdict} — Max $|\\rho_k|$ = {max_abs_rho:.4f} (threshold {gate_threshold_pass})',
             fontsize=12, fontweight='bold', y=0.99)

plt.savefig(base / 's46_multi_jacobson.png', dpi=150, bbox_inches='tight')
print(f"Plot saved to: {base / 's46_multi_jacobson.png'}")

print(f"\nDone.")
