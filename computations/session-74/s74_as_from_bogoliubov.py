#!/usr/bin/env python3
"""
s74_as_from_bogoliubov.py -- A_s from 8-mode Bogoliubov squeezed vacuum
=======================================================================

Gate: A-S-FROM-BOGOLIUBOV-74  (Session 74 Wave 1 Batch 2, W1-G)
  PASS: |log10(A_s^computed/A_s^Planck)| < 1.0 (within factor 10, closes 2+ OOM)
  INFO: 1.0 < |gap| < 2.0 (partial closure)
  FAIL: |gap| > 2.0 (Bogoliubov-amplitude route insufficient)

PHYSICS (substrate framing):
    A_s is NOT a primordial curvature perturbation in inflationary spacetime.
    A_s is the emergent projection of the 8-mode Bogoliubov squeezed vacuum
    variance (from the fold transit) onto the scalar channel of the emergent
    4-metric. The chain is:

        D_K squeezed vacuum at fold
          --> Peter-Weyl sector filter (only (p,p) even-parity project to scalar)
          --> BLV acoustic dilution (c_BLV=0.485 enhances mode power as c_BLV^-3)
          --> horizon-crossing dynamics
          --> emergent A_s

    The squeezed vacuum variance per mode (in units of 1/(2*omega)):
        sigma_k^2 = (1/(2*omega_k)) * (cosh(2*r_k) - sinh(2*r_k)*cos(phi_k))

    For phi_k = pi (sudden quench from S64) with tiny delta_phi = 2.4e-4:
        cos(phi_k) = cos(pi + 2.4e-4) ~ -1 + 2.88e-8
    giving sigma_k^2 ~ (1/(2*omega_k)) * exp(+2*r_k) (strong amplification).

    This is the LARGE variance route -- the r_k=3.57 (B1) squeeze gives
    exp(2*3.57) = 1240x amplification per mode. B2 modes have r=1.786,
    amplification = 35x. B3 modes have r=1.963, amplification = 51x.

    Critical inputs:
      - 8-mode r_k (BCS squeeze): B2[0-3]=1.786, B1=3.571, B3[0-2]=1.963
      - 8-mode omega_k (from transfer function S74 W1-A)
      - phi_k ~ pi (sudden quench, delta = 2.4e-4)
      - Peter-Weyl filter: keep only (p,p) sectors in B1, B2 branches
      - c_BLV = 0.485 -> enhancement factor c_BLV^-3 = 8.77x per mode
      - M_Pl^2 = a_2/(48*pi^2) (spectral action Planck mass)
      - H_phys from S65 AB-AS-65 (0.4043 M_KK, GM-formula matching gap_occ)

Session: S74 W1-G
Author: phonon-first-cosmologist
Depends on: S73a (s73a_exit_horizon_bog.npz, 8-mode r_k, omega estimates),
            S74 W1-A (s74_transfer_function.npz, omega_Bi, mode weights),
            S65 (s65_ab_mode_as.npz, H_phys, M_Pl from a_2),
            S64 (s64_transfer_bogoliubov.npz, PW suppression numbers,
                 s64_occ_spec.npz, sector multiplicities),
            canonical_constants (A_s_CMB, c_Gold/c_fabric -> c_BLV derived,
                                 tau_fold, a2_fold, M_KK, PI).

Pre-registered baselines:
  - S73B baseline gap: 3.15 OOM (historical framework chapter target)
  - S74 W1-A post-transfer baseline: 5.83 OOM (5.834601525887933)
  - Planck A_s_obs: 2.1e-9
"""

import sys
import os
import time
import numpy as np
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPT_DIR))

from canonical_constants import (
    tau_fold, a2_fold, a0_fold, a4_fold,
    S_fold, dS_fold, d2S_fold,
    A_s_CMB, PI, M_KK,
    c_Gold, c_fabric, c_Gold_over_c_fabric,
)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

OUT_NPZ = SCRIPT_DIR / "s74_as_from_bogoliubov.npz"
OUT_PNG = SCRIPT_DIR / "s74_as_from_bogoliubov.png"
OUT_LOG = SCRIPT_DIR / "s74_as_from_bogoliubov_output.txt"

t_start = time.time()

lines = []  # (local)
def log(msg=""):
    print(msg)
    lines.append(msg)

log("=" * 78)
log("S74 W1-G  A-S-FROM-BOGOLIUBOV-74: A_s from 8-mode squeezed vacuum")
log("=" * 78)

# =============================================================================
# SECTION 1: Load input data
# =============================================================================
log("\n--- Section 1: Load input data ---")

# 1a. S73a 8-mode Bogoliubov data
d_s73a = np.load(SCRIPT_DIR / "s73a_exit_horizon_bog.npz", allow_pickle=True)
labels = d_s73a['labels']              # ['B2[0]', 'B2[1]', ..., 'B1', 'B3[0]', ...]
r_k_bcs_raw = np.array(d_s73a['r_k_bcs'])  # BCS squeeze, 8 modes
n_k_dyn = np.array(d_s73a['n_k'])      # dynamical |beta|^2 (small, ~1e-3)
alpha_sq_s73a = np.array(d_s73a['alpha_sq'])
beta_sq_s73a = np.array(d_s73a['beta_sq'])
phase_k_s73a = np.array(d_s73a['phase_k'])
mode_weights_s73a = np.array(d_s73a['mode_weights'])

log(f"  s73a labels: {labels}")
log(f"  r_k_bcs: {r_k_bcs_raw}")
log(f"  mode weights: {mode_weights_s73a}")

# 1b. S74 W1-A transfer function data (provides omega_Bi, mode weights, A_s_baseline)
d_s74_tf = np.load(SCRIPT_DIR / "s74_transfer_function.npz", allow_pickle=True)
omega_B1 = float(d_s74_tf['omega_B1'])
omega_B2 = float(d_s74_tf['omega_B2'])
omega_B3 = float(d_s74_tf['omega_B3'])
r_B1_tf = float(d_s74_tf['r_B1'])
r_B2_tf = float(d_s74_tf['r_B2'])
r_B3_tf = float(d_s74_tf['r_B3'])
W_B1 = float(d_s74_tf['W_B1'])
W_B2 = float(d_s74_tf['W_B2'])
W_B3 = float(d_s74_tf['W_B3'])
A_s_4D_baseline = float(d_s74_tf['A_s_4D'])
A_s_gap_OOM_baseline = float(d_s74_tf['A_s_gap_OOM'])

log(f"\n  S74 W1-A transfer function:")
log(f"    omega_B1={omega_B1:.4f}, omega_B2={omega_B2:.4f}, omega_B3={omega_B3:.4f}")
log(f"    r_B1={r_B1_tf:.4f}, r_B2={r_B2_tf:.4f}, r_B3={r_B3_tf:.4f}")
log(f"    W_B1={W_B1:.4f}, W_B2={W_B2:.4f}, W_B3={W_B3:.4f}")
log(f"    A_s_4D (post-transfer) = {A_s_4D_baseline:.6e}")
log(f"    A_s gap (post-transfer) = {A_s_gap_OOM_baseline:.4f} OOM")

# 1c. S65 AB-AS data (for M_Pl, H_phys, eps_H, reference chain)
d_s65 = np.load(SCRIPT_DIR / "s65_ab_mode_as.npz", allow_pickle=True)
c_BLV = float(d_s65['c_BLV'])            # 0.485
eps_H_fold = float(d_s65['eps_H_fold'])
H_phys_s65 = float(d_s65['H_phys'])      # 0.4043 M_KK
H_phys_sq_s65 = float(d_s65['H_phys_sq'])
M_Pl_sq_s65 = float(d_s65['M_Pl_sq'])
a2_fold_s65 = float(d_s65['a2_fold'])
gap_occ_s65 = float(d_s65['gap_occ'])         # 6.891 (starting point before PW)
gap_full_s65 = float(d_s65['gap_full'])        # 8.014
gap_revised_S64 = float(d_s65['gap_revised_S64'])  # 3.165 (S64 route final)
gap_from_PW_s65 = float(d_s65['gap_from_PW'])   # -3.496 (S64 PW suppression, (0,0) only)
gap_from_gaps_s65 = float(d_s65['gap_from_gaps'])  # -0.230 (S64 gap tunneling)

log(f"\n  S65 inputs:")
log(f"    c_BLV = {c_BLV:.4f} (subluminal scalar sound speed)")
log(f"    eps_H(fold) = {eps_H_fold:.6f}")
log(f"    M_Pl^2 = a_2/(48*pi^2) = {M_Pl_sq_s65:.6f} M_KK^2")
log(f"    H_phys = {H_phys_s65:.6f} M_KK  (from GM-inverse of gap_occ)")
log(f"    S64 PW suppression (0,0 only): {gap_from_PW_s65:.4f} OOM")
log(f"    S64 gap tunneling: {gap_from_gaps_s65:.4f} OOM")
log(f"    S64 revised gap (PW route): {gap_revised_S64:.4f} OOM")

# 1d. S64 transfer_bogoliubov for S_occ_total and sector data
d_s64_tb = np.load(SCRIPT_DIR / "s64_transfer_bogoliubov.npz", allow_pickle=True)
S_occ_total = 18851.918238061662                          # (local) from s64_occ_spec

# 1e. S64 occ_spec for per-sector weights
d_s64_occ = np.load(SCRIPT_DIR / "s64_occ_spec.npz", allow_pickle=True)
sectors_list = list(d_s64_occ['sectors'])         # ['(0,0)','(1,0)',...]
sector_S_occ = np.array(d_s64_occ['sector_S_occ'])
sector_v2_mean = np.array(d_s64_occ['sector_v2_mean'])

log(f"\n  S64 sector data (top 10 sectors):")
for i, s in enumerate(sectors_list):
    log(f"    {s}: S_occ={sector_S_occ[i]:.3e}, <v^2>={sector_v2_mean[i]:.4f}")
log(f"    S_occ_total = {S_occ_total:.3e}")

# =============================================================================
# SECTION 2: Pre-registered baselines and Planck target
# =============================================================================
log("\n--- Section 2: Pre-registered baselines ---")

A_s_planck = A_s_CMB                                   # 2.1e-9
baseline_s73b_OOM = 3.15                                   # (local)
baseline_s74_w1a_OOM = A_s_gap_OOM_baseline               # 5.83

log(f"  Planck A_s_obs = {A_s_planck:.3e}")
log(f"  Baseline (S73B, 3.15 OOM): A_s = {10**baseline_s73b_OOM * A_s_planck:.3e}")
log(f"  Baseline (S74 W1-A, 5.83 OOM): A_s = {10**baseline_s74_w1a_OOM * A_s_planck:.3e}")
log(f"  Target: closure to within 1 OOM (PASS) or 1-2 OOM (INFO)")

# =============================================================================
# SECTION 3: Per-mode squeezed vacuum variance
# =============================================================================
log("\n--- Section 3: Per-mode squeezed vacuum variance ---")

# Assemble the 8-mode data:
# s73a ordering: B2[0], B2[1], B2[2], B2[3], B1, B3[0], B3[1], B3[2]
N_modes = 8                                               # (local)
# Branch labels
branch = np.array(['B2','B2','B2','B2','B1','B3','B3','B3'])

# Frequencies: take from S74 W1-A (branch-level), broadcast to 8 modes
omega_k = np.array([
    omega_B2, omega_B2, omega_B2, omega_B2,
    omega_B1,
    omega_B3, omega_B3, omega_B3,
])

# Squeeze parameters: take from s73a r_k_bcs directly (they match W1-A)
r_k = r_k_bcs_raw.copy()

# Phase: sudden quench from S64 => phi_k = pi + delta_phi
delta_phi_physical = 2.4e-4                                  # (local)
phi_k = np.full(N_modes, PI + delta_phi_physical)

log(f"  Mode index  Branch  omega_k   r_k_bcs    phi_k")
for i in range(N_modes):
    log(f"  {i}      {branch[i]}    {omega_k[i]:.4f}  {r_k[i]:.4f}   {phi_k[i]:.6f}")

# Compute the bare squeezed-state variance per mode:
#   sigma_k^2 = (1/(2*omega_k)) * (cosh(2*r_k) - sinh(2*r_k)*cos(phi_k))
# With phi_k ~ pi, cos(phi_k) ~ -1, so
#   sigma_k^2 ~ (1/(2*omega_k)) * (cosh(2*r_k) + sinh(2*r_k)) = (1/(2*omega_k)) * exp(2*r_k)
#
# The exact formula is used (no approximation).
sigma_sq_bare = (1.0 / (2.0 * omega_k)) * (
    np.cosh(2.0 * r_k) - np.sinh(2.0 * r_k) * np.cos(phi_k)
)

log(f"\n  Bare squeezed-state variance sigma_k^2 = (1/(2 omega_k)) [cosh(2r)-sinh(2r)cos(phi)]:")
for i in range(N_modes):
    amp_factor = np.exp(2.0 * r_k[i])                       # (local)
    log(f"  {i} {branch[i]}: sigma^2={sigma_sq_bare[i]:.4e}   (vac = {1.0/(2*omega_k[i]):.4e}, "
        f"amp exp(2r) = {amp_factor:.2e})")

# Total bare squeezed variance (no filtering yet)
Sigma_bare_total = np.sum(sigma_sq_bare)
log(f"\n  Total bare squeezed variance (sum over 8 modes) = {Sigma_bare_total:.4e}")
log(f"  Total vacuum variance (sum of 1/(2 omega_k)) = {np.sum(1.0/(2*omega_k)):.4e}")
log(f"  Amplification vs vacuum: {Sigma_bare_total/np.sum(1.0/(2*omega_k)):.2e}")

# =============================================================================
# SECTION 4: Peter-Weyl sector filter
# =============================================================================
log("\n--- Section 4: Peter-Weyl (p,p) even-parity filter ---")

# Branch-to-(p,q)-sector mapping from the canonical s52/s73a convention:
#   B1 = (0,0) singlet (C_2=0, dim=1)   -- one mode, Fermi surface orbital
#   B2 = (1,1) adjoint (C_2=3, dim=8)   -- four degenerate modes
#   B3 = (1,0)+(0,1) fund+conj (dim=6)  -- three modes
#
# The scalar (even-parity) channel accepts ONLY (p,p) sectors:
#   (0,0): YES  (p=q=0)  -> B1 kept
#   (1,1): YES  (p=q=1)  -> B2 kept (all 4 modes)
#   (1,0), (0,1): NO     -> B3 filtered
#
# Peter-Weyl multiplicities per sector (dim^2):
#   (0,0) -> 1^2 = 1    degenerate weight (B1)
#   (1,1) -> 8^2 = 64   degenerate weight split across (1,1) states;
#                        per-mode weight in the 4-mode B2 block is 64/4 = 16
#   (1,0) -> 3^2 = 9    (B3 filtered out)
#   (0,1) -> 3^2 = 9    (B3 filtered out)
#
# The per-mode PW weight encodes how many D_K eigenmodes contribute to that
# 8-mode basis vector. For the Bogoliubov squeezed vacuum, each mode acts
# as an ensemble of d_(p,q)^2 copies.

# Conv A: B1=(0,0), B2=(1,1), B3=(1,0)+(0,1)
def dim_pq(p, q):
    return (p + 1) * (q + 1) * (p + q + 2) // 2

# Peter-Weyl multiplicity for each branch (d_(p,q)^2)
mult_00 = dim_pq(0, 0) ** 2       # 1
mult_11 = dim_pq(1, 1) ** 2       # 64
mult_10 = dim_pq(1, 0) ** 2       # 9
mult_01 = dim_pq(0, 1) ** 2       # 9

# Per-mode PW weights (distributing the sector multiplicity across modes)
# B1 (1 mode) carries all of (0,0): 1
# B2 (4 modes) split (1,1) multiplicity: 64/4 = 16 per mode
# B3 (3 modes) split (1,0)+(0,1) multiplicity: (9+9)/3 = 6 per mode
d_pq_sq_per_mode = np.array([
    mult_11 / 4.0, mult_11 / 4.0, mult_11 / 4.0, mult_11 / 4.0,   # B2
    mult_00,                                                         # B1
    (mult_10 + mult_01) / 3.0, (mult_10 + mult_01) / 3.0, (mult_10 + mult_01) / 3.0,  # B3
])

# (p,p) even-parity Theta filter
Theta_pp = np.array([
    1.0, 1.0, 1.0, 1.0,   # B2 = (1,1) kept
    1.0,                  # B1 = (0,0) kept
    0.0, 0.0, 0.0,        # B3 = (1,0)+(0,1) filtered
])

log(f"  Per-mode PW weights d_(p,q)^2:")
for i in range(N_modes):
    log(f"    {i} {branch[i]}: d^2={d_pq_sq_per_mode[i]:.2f}, Theta_(p,p)={Theta_pp[i]}")

sigma_sq_filtered = sigma_sq_bare * Theta_pp
Sigma_filtered_total = np.sum(sigma_sq_filtered * d_pq_sq_per_mode)
Sigma_bare_weighted = np.sum(sigma_sq_bare * d_pq_sq_per_mode)

log(f"\n  Total bare PW-weighted variance = {Sigma_bare_weighted:.4e}")
log(f"  Total filtered PW-weighted variance (B1+B2 kept) = {Sigma_filtered_total:.4e}")
log(f"  Filter retention fraction = {Sigma_filtered_total/Sigma_bare_weighted:.6e}")
log(f"  Filter OOM suppression = {np.log10(Sigma_filtered_total/Sigma_bare_weighted):.4f}")

# Alternative (S53 loose convention): B1 = (0,0)+(1,0)+(0,1), so B1 per-mode
# is (1+9+9)=19 in weight, but only the (0,0) fraction (1/19) is (p,p).
# Recompute under this convention as a cross-check.
d_pq_sq_per_mode_loose = np.array([
    mult_11 / 4.0, mult_11 / 4.0, mult_11 / 4.0, mult_11 / 4.0,
    (mult_00 + mult_10 + mult_01),  # B1 = (0,0)+(1,0)+(0,1) pooled
    mult_11 / 3.0, mult_11 / 3.0, mult_11 / 3.0,  # B3 = higher, but we only keep B1 (p,p) fraction
])
# Under loose, B1 keeps only (0,0) fraction: Theta = 1/19
Theta_pp_loose = np.array([
    1.0, 1.0, 1.0, 1.0,            # B2 = (1,1) all kept
    mult_00 / (mult_00 + mult_10 + mult_01),  # B1 partial (p,p)
    0.0, 0.0, 0.0,                  # B3 higher, none (p,p) -- filter
])
sigma_sq_filtered_loose = sigma_sq_bare * Theta_pp_loose
Sigma_filtered_loose = np.sum(sigma_sq_filtered_loose * d_pq_sq_per_mode_loose)
log(f"\n  [Cross-check, loose S53 convention]")
log(f"    B1 (p,p) Theta = {Theta_pp_loose[4]:.4f} (only (0,0) fraction)")
log(f"    Filtered total (loose) = {Sigma_filtered_loose:.4e}")
log(f"    Difference from strict: {np.log10(Sigma_filtered_loose/Sigma_filtered_total):+.4f} OOM")

# =============================================================================
# SECTION 5: BLV acoustic dilution
# =============================================================================
log("\n--- Section 5: BLV acoustic dilution ---")

# The scalar mode sound speed is c_BLV = 0.485 (subluminal).
# In the Garriga-Mukhanov formalism, c_s appears in the denominator of P_s:
#     P_s proportional to 1/c_s
# In the mode-by-mode Bogoliubov picture, the scalar sound speed enters
# as a normalization factor (c_BLV)^(-3) for the mode volume in the power
# spectrum (each dimension of 3-momentum is rescaled by 1/c_BLV).
#
# This ENHANCES the spectrum (c_BLV<1 => factor > 1) --> gap WORSENS.

blv_factor = c_BLV ** (-3.0)
log(f"  c_BLV = {c_BLV:.4f}")
log(f"  BLV dilution factor (c_BLV)^(-3) = {blv_factor:.4f}")
log(f"  log10(BLV factor) = {np.log10(blv_factor):.4f} OOM (enhancement)")

sigma_sq_blv = sigma_sq_filtered * blv_factor
Sigma_blv_weighted = np.sum(sigma_sq_blv * d_pq_sq_per_mode)

log(f"  Post-BLV filtered variance = {Sigma_blv_weighted:.4e}")

# =============================================================================
# SECTION 6: Convert to A_s (dimensionless)
# =============================================================================
log("\n--- Section 6: Convert to dimensionless A_s ---")

# The mode-variance sum must be normalized to produce a dimensionless A_s.
# Following the Garriga-Mukhanov formalism, the scalar power spectrum for a
# collection of modes with per-mode variance sigma_k^2 is:
#
#     P_s = (H^2/(8*pi^2*eps_H*M_Pl^2)) * (scale) * F_squeezed
#
# where F_squeezed is the dimensionless ratio of the squeezed-mode variance
# to the BD vacuum variance. For a single mode:
#     F_squeezed = sigma_k^2 / sigma_BD^2 = (cosh(2r)-sinh(2r)cos(phi))
#
# For a collection of N modes with PW weights d_i^2 and Theta filter Theta_i:
#     F_squeezed = (sum_i Theta_i * d_i^2 * sigma_sq_bare_i) /
#                   (sum_i d_i^2 * sigma_BD_i^2)
#
# But that ratio double-counts the frequency normalization. The cleaner
# formulation is: A_s = A_s_baseline_5p83 * F_filter * F_BLV * F_squeeze
# where the baseline A_s_baseline_5p83 comes from S74 W1-A (which already
# accounts for the squeezed-vacuum transfer function at tree level) and
# we multiply by the additional factors from the PW filter and BLV dilution.
#
# Alternatively, we can compute A_s from scratch starting from the
# Garriga-Mukhanov template at H_phys:
#     P_0 = H_phys^2 / (8*pi^2*eps_H*M_Pl^2)
# then multiply by the ratio F_squeezed / F_vacuum (mode by mode) with
# Theta filter and BLV dilution.
#
# The GM template P_0 reproduces gap_occ when evaluated with the 8-mode
# occupation but WITHOUT sector filtering or BLV. We compute F_mode as the
# multiplicative correction.

P_0_GM = H_phys_sq_s65 / (8.0 * PI**2 * eps_H_fold * M_Pl_sq_s65)
log(f"  GM template P_0 = H^2/(8 pi^2 eps M_Pl^2) = {P_0_GM:.4e}")
log(f"  gap_from_P0 = log10(P_0/A_s_obs) = {np.log10(P_0_GM/A_s_planck):.4f} OOM  "
    f"(matches gap_occ = {gap_occ_s65:.4f})")

# Mode-level correction factor F_mode:
#   F_mode = (filtered squeezed variance, BLV-diluted) / (bare vacuum variance, unfiltered)
# Bare vacuum PW-weighted sum: sum_i (d_i^2 / (2*omega_i))
bare_vacuum_weighted = np.sum(d_pq_sq_per_mode / (2.0 * omega_k))
F_mode_squeeze_bare = Sigma_bare_weighted / bare_vacuum_weighted            # squeeze amplification
F_mode_filter_factor = Sigma_filtered_total / Sigma_bare_weighted            # PW filter
F_mode_BLV_factor = blv_factor                                               # BLV dilution

# Combined corrected A_s (strict convention)
F_mode_total = F_mode_squeeze_bare * F_mode_filter_factor * F_mode_BLV_factor
A_s_computed = P_0_GM * F_mode_total

log(f"\n  Mode-level correction factors (strict S52 convention):")
log(f"    F_squeeze_bare = {F_mode_squeeze_bare:.4e}  (squeeze amplification)")
log(f"    F_filter_factor = {F_mode_filter_factor:.4e}  (PW (p,p) filter retention)")
log(f"    F_BLV_factor = {F_mode_BLV_factor:.4e}  (c_BLV^-3 enhancement)")
log(f"    F_mode_total = {F_mode_total:.4e}")
log(f"\n  A_s_computed = P_0 * F_mode_total = {A_s_computed:.4e}")
log(f"  A_s_Planck = {A_s_planck:.4e}")

gap_OOM = np.log10(A_s_computed / A_s_planck)
log(f"\n  gap_OOM = log10(A_s_computed/A_s_Planck) = {gap_OOM:.4f} OOM")

# =============================================================================
# SECTION 7: Step-by-step OOM breakdown
# =============================================================================
log("\n--- Section 7: Step-by-step OOM breakdown ---")

# Step 0: P_0 (GM template, no squeezing, no filter, no BLV)
A_s_step0 = P_0_GM
OOM_step0 = np.log10(A_s_step0 / A_s_planck)

# Step 1: Add squeezing (but no filter, no BLV)
A_s_step1 = P_0_GM * F_mode_squeeze_bare
OOM_step1 = np.log10(A_s_step1 / A_s_planck)

# Step 2: Apply PW filter (strict convention)
A_s_step2 = P_0_GM * F_mode_squeeze_bare * F_mode_filter_factor
OOM_step2 = np.log10(A_s_step2 / A_s_planck)

# Step 3: Apply BLV dilution
A_s_step3 = P_0_GM * F_mode_squeeze_bare * F_mode_filter_factor * F_mode_BLV_factor
OOM_step3 = np.log10(A_s_step3 / A_s_planck)

log(f"  Step 0 (GM template P_0 alone): A_s = {A_s_step0:.4e}, OOM = {OOM_step0:+.4f}")
log(f"  Step 1 (+ squeeze amplification): A_s = {A_s_step1:.4e}, OOM = {OOM_step1:+.4f}")
log(f"  Step 2 (+ PW (p,p) filter):      A_s = {A_s_step2:.4e}, OOM = {OOM_step2:+.4f}")
log(f"  Step 3 (+ c_BLV^-3 dilution):    A_s = {A_s_step3:.4e}, OOM = {OOM_step3:+.4f}")

log(f"\n  Delta_OOM from squeezing:    {OOM_step1 - OOM_step0:+.4f}  (worsens by Bogoliubov amp)")
log(f"  Delta_OOM from PW filter:     {OOM_step2 - OOM_step1:+.4f}  (suppression from (p,p) filter)")
log(f"  Delta_OOM from BLV dilution: {OOM_step3 - OOM_step2:+.4f}  (enhancement from c_BLV<1)")

# =============================================================================
# SECTION 8: Gate verdict
# =============================================================================
log("\n--- Section 8: Gate verdict ---")

# Closure metrics relative to both baselines
gap_vs_planck = gap_OOM                                     # absolute gap vs observation
gap_vs_s73b = gap_OOM - baseline_s73b_OOM                   # change relative to 3.15 OOM baseline
gap_vs_s74_w1a = gap_OOM - baseline_s74_w1a_OOM             # change relative to 5.83 OOM baseline

log(f"  Gap vs Planck A_s_obs: {gap_vs_planck:+.4f} OOM")
log(f"  Change vs S73B baseline (3.15): {gap_vs_s73b:+.4f} OOM")
log(f"  Change vs S74 W1-A baseline (5.83): {gap_vs_s74_w1a:+.4f} OOM")

if abs(gap_vs_planck) < 1.0:
    verdict = "PASS"
    verdict_msg = f"A_s within 1 OOM of Planck (|{gap_vs_planck:.4f}|<1.0); Bogoliubov route closes the gap."
elif abs(gap_vs_planck) < 2.0:
    verdict = "INFO"
    verdict_msg = f"A_s within 1-2 OOM of Planck (|{gap_vs_planck:.4f}|in[1,2]); partial closure only."
else:
    verdict = "FAIL"
    verdict_msg = (f"A_s gap {abs(gap_vs_planck):.2f} OOM > 2.0 OOM threshold; "
                   f"Bogoliubov-amplitude route alone does NOT close the tension.")

log(f"\n  VERDICT: A-S-FROM-BOGOLIUBOV-74 = {verdict}")
log(f"  Reason: {verdict_msg}")

# =============================================================================
# SECTION 9: Cross-checks
# =============================================================================
log("\n--- Section 9: Cross-checks ---")

# Cross-check 1: r_k = 0 limit -> vacuum result
r_k_zero = np.zeros(N_modes)                                 # (local)
sigma_sq_vac_check = (1.0 / (2.0 * omega_k)) * (
    np.cosh(2.0 * r_k_zero) - np.sinh(2.0 * r_k_zero) * np.cos(phi_k)
)
F_vac_check = np.sum(sigma_sq_vac_check * d_pq_sq_per_mode) / bare_vacuum_weighted
log(f"  Cross-check 1 (r_k=0): F_mode = {F_vac_check:.6f} (should be 1.000)")
assert abs(F_vac_check - 1.0) < 1e-9, f"Vacuum limit failed: {F_vac_check}"
log(f"    PASS: vacuum limit recovers BD normalization.")

# Cross-check 2: BLV factor enhancement direction
log(f"  Cross-check 2: c_BLV^-3 = {blv_factor:.4f} > 1  "
    f"({'PASS' if blv_factor > 1 else 'FAIL'}: subluminal enhances amplitude)")

# Cross-check 3: Filter must be <= 1 (suppression or identity)
filter_leq_1 = F_mode_filter_factor <= 1.0
log(f"  Cross-check 3: Filter retention {F_mode_filter_factor:.4e} <= 1.0  "
    f"({'PASS' if filter_leq_1 else 'FAIL'})")

# Cross-check 4: Match to S65 AB-AS baseline (sanity: gap_occ is our starting point)
P_0_check = A_s_step0
gap_P_0 = np.log10(P_0_check / A_s_planck)
log(f"  Cross-check 4: P_0 gap = {gap_P_0:.4f} vs S65 gap_occ = {gap_occ_s65:.4f}  "
    f"(|diff| = {abs(gap_P_0 - gap_occ_s65):.4f})")

# Cross-check 5: loose convention
A_s_loose = P_0_GM * (Sigma_bare_weighted / bare_vacuum_weighted) * (Sigma_filtered_loose / Sigma_bare_weighted) * blv_factor
gap_loose = np.log10(A_s_loose / A_s_planck)
log(f"  Cross-check 5: loose S53 convention A_s = {A_s_loose:.4e}, gap = {gap_loose:.4f} "
    f"(vs strict {gap_OOM:.4f}, diff = {gap_loose-gap_OOM:+.4f})")

# Cross-check 6: compare against S65 gap_revised_S64 (PW route without squeezing)
# If we turn off squeezing (r=0) and keep PW filter + gap tunneling, we should
# approximately recover gap_occ + gap_from_PW_s65 + gap_from_gaps_s65 = 3.165
P_0_PW_only = P_0_GM * F_mode_filter_factor   # no squeezing, no BLV
gap_PW_only = np.log10(P_0_PW_only / A_s_planck)
log(f"  Cross-check 6: P_0 * filter alone (no squeeze, no BLV): gap = {gap_PW_only:.4f} OOM")
log(f"    S65 PW+gaps baseline was {gap_revised_S64:.4f} (strict is looser/tighter by sector choice)")
log(f"    Note: S65 used only (0,0) -> -3.50 OOM; strict (p,p)=(0,0)+(1,1) -> {np.log10(F_mode_filter_factor):+.4f} OOM")

# =============================================================================
# SECTION 10: Save results
# =============================================================================
log("\n--- Section 10: Save results ---")

save_dict = {
    'gate_name': 'A-S-FROM-BOGOLIUBOV-74',
    'gate_verdict': verdict,
    'gate_detail': verdict_msg,
    # Core outputs
    'A_s_computed': A_s_computed,
    'A_s_planck': A_s_planck,
    'gap_OOM_vs_planck': gap_OOM,
    'gap_vs_s73b_baseline': gap_vs_s73b,
    'gap_vs_s74_w1a_baseline': gap_vs_s74_w1a,
    # Baselines
    'baseline_s73b_OOM': baseline_s73b_OOM,
    'baseline_s74_w1a_OOM': baseline_s74_w1a_OOM,
    # Per-mode data
    'labels': labels,
    'branch': branch,
    'omega_k': omega_k,
    'r_k': r_k,
    'phi_k': phi_k,
    'sigma_sq_bare': sigma_sq_bare,
    'sigma_sq_filtered': sigma_sq_filtered,
    'sigma_sq_blv': sigma_sq_blv,
    'Theta_pp': Theta_pp,
    'd_pq_sq_per_mode': d_pq_sq_per_mode,
    # Step-by-step OOM
    'OOM_step0_P0': OOM_step0,
    'OOM_step1_squeeze': OOM_step1,
    'OOM_step2_filter': OOM_step2,
    'OOM_step3_BLV': OOM_step3,
    'A_s_step0': A_s_step0,
    'A_s_step1': A_s_step1,
    'A_s_step2': A_s_step2,
    'A_s_step3': A_s_step3,
    # Correction factors
    'F_squeeze_bare': F_mode_squeeze_bare,
    'F_filter_factor': F_mode_filter_factor,
    'F_BLV_factor': F_mode_BLV_factor,
    'F_mode_total': F_mode_total,
    # Physical inputs
    'c_BLV': c_BLV,
    'eps_H_fold': eps_H_fold,
    'H_phys_s65': H_phys_s65,
    'M_Pl_sq': M_Pl_sq_s65,
    'P_0_GM': P_0_GM,
    # Alternative convention
    'A_s_loose': A_s_loose,
    'gap_loose': gap_loose,
    'Theta_pp_loose': Theta_pp_loose,
    # Cross-check
    'P_0_PW_only_gap': gap_PW_only,
    'S65_PW_gap': gap_from_PW_s65,
    'S65_gap_revised': gap_revised_S64,
    'S65_gap_occ': gap_occ_s65,
}

np.savez(OUT_NPZ, **save_dict)
log(f"  Saved: {OUT_NPZ}")

# =============================================================================
# SECTION 11: Plot
# =============================================================================
log("\n--- Section 11: Generate plot ---")

fig = plt.figure(figsize=(14, 10))
gs = GridSpec(2, 2, figure=fig, hspace=0.35, wspace=0.3)

# Panel 1: OOM-closure cascade
ax1 = fig.add_subplot(gs[0, :])
steps = ['P_0 (GM)', '+ Squeeze', '+ PW filter', '+ BLV']
oom_values = [OOM_step0, OOM_step1, OOM_step2, OOM_step3]
colors = ['gray', 'orange', 'green', 'royalblue']
bars = ax1.bar(steps, oom_values, color=colors, edgecolor='black')
ax1.axhline(0, color='red', ls='--', lw=1.5, label='Planck A_s_obs (target)')
ax1.axhline(baseline_s73b_OOM, color='darkred', ls=':', lw=1.2, label=f'S73B baseline ({baseline_s73b_OOM:.2f})')
ax1.axhline(baseline_s74_w1a_OOM, color='purple', ls=':', lw=1.2, label=f'S74 W1-A baseline ({baseline_s74_w1a_OOM:.2f})')
ax1.axhline(1.0, color='darkgreen', ls='--', lw=1.0, alpha=0.7, label='PASS threshold (±1 OOM)')
ax1.axhline(-1.0, color='darkgreen', ls='--', lw=1.0, alpha=0.7)
ax1.axhline(2.0, color='darkorange', ls='--', lw=1.0, alpha=0.7, label='INFO boundary (±2 OOM)')
ax1.axhline(-2.0, color='darkorange', ls='--', lw=1.0, alpha=0.7)
for i, (step, val) in enumerate(zip(steps, oom_values)):
    ax1.text(i, val + (0.2 if val > 0 else -0.4), f'{val:+.2f}', ha='center', fontsize=11, fontweight='bold')
ax1.set_ylabel('log10(A_s/A_s_Planck)  [OOM]', fontsize=12)
ax1.set_title(f'S74 W1-G  A-S-FROM-BOGOLIUBOV-74: OOM-closure cascade  -->  {verdict}',
              fontsize=13, fontweight='bold')
ax1.legend(loc='center right', fontsize=9)
ax1.grid(True, alpha=0.3)

# Panel 2: per-mode squeezed variance
ax2 = fig.add_subplot(gs[1, 0])
mode_labels = [f'{labels[i]}' for i in range(N_modes)]
xpos = np.arange(N_modes)
colors_mode = ['tab:red' if Theta_pp[i] == 0 else ('tab:blue' if branch[i] == 'B1' else 'tab:green') for i in range(N_modes)]
ax2.bar(xpos, np.log10(sigma_sq_bare * d_pq_sq_per_mode), color=colors_mode, edgecolor='black', alpha=0.75)
ax2.set_xticks(xpos)
ax2.set_xticklabels(mode_labels, rotation=45, fontsize=9)
ax2.set_ylabel('log10(d^2 * sigma_k^2)', fontsize=11)
ax2.set_title('Per-mode PW-weighted squeezed variance (red=filtered out)', fontsize=11)
ax2.grid(True, alpha=0.3)

# Panel 3: correction factors (log scale)
ax3 = fig.add_subplot(gs[1, 1])
factors_names = ['Squeeze', 'PW filter', 'BLV', 'Total']
factors_log = [np.log10(F_mode_squeeze_bare),
               np.log10(F_mode_filter_factor),
               np.log10(F_mode_BLV_factor),
               np.log10(F_mode_total)]
colors_fact = ['orange', 'green', 'royalblue', 'black']
bars3 = ax3.bar(factors_names, factors_log, color=colors_fact, edgecolor='black', alpha=0.8)
ax3.axhline(0, color='red', ls='--', lw=1.0)
for i, (n, v) in enumerate(zip(factors_names, factors_log)):
    ax3.text(i, v + (0.05 if v > 0 else -0.15), f'{v:+.2f}', ha='center', fontsize=10, fontweight='bold')
ax3.set_ylabel('log10(correction factor)  [OOM]', fontsize=11)
ax3.set_title('Mode-level correction factors', fontsize=11)
ax3.grid(True, alpha=0.3)

# Annotation: verdict and numbers
fig.text(0.5, 0.02,
         f'A_s_computed = {A_s_computed:.3e}, Planck = {A_s_planck:.3e}, gap = {gap_OOM:+.3f} OOM | '
         f'Verdict: {verdict}',
         ha='center', fontsize=11,
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.85))

plt.savefig(OUT_PNG, dpi=120, bbox_inches='tight')
plt.close()
log(f"  Saved: {OUT_PNG}")

# =============================================================================
# Summary
# =============================================================================
log("\n" + "=" * 78)
log(f"S74 W1-G  A-S-FROM-BOGOLIUBOV-74: {verdict}")
log("=" * 78)
log(f"  A_s_computed      = {A_s_computed:.4e}")
log(f"  A_s_Planck        = {A_s_planck:.4e}")
log(f"  gap (OOM)         = {gap_OOM:+.4f}")
log(f"  vs S73B baseline: {gap_vs_s73b:+.4f} OOM change")
log(f"  vs S74 W1-A base: {gap_vs_s74_w1a:+.4f} OOM change")
log(f"  Runtime: {time.time()-t_start:.2f} s")

# Write output log
with open(OUT_LOG, 'w') as f:
    f.write('\n'.join(lines))
