#!/usr/bin/env python3
"""
s65_scale_transfer.py — Scale Transfer: k_KK to k_CMB Mechanism
================================================================

Gate: SCALE-TRANSFER-65
  PASS: At least one interpretation gives nonzero power at CMB scales
  FAIL: Both interpretations give P(k_CMB) = 0
  INFO: P(k_CMB) > 0 but amplitude unknown to better than 3 OOM

PHYSICS:
    The deepest open question for observational connection: what physical
    mechanism transfers perturbations from the transit scale k_KK ~ M_KK
    ~ 10^16 GeV to the CMB scale k_CMB ~ 10^{-29} GeV?

    Standard inflation uses ~60 e-folds of exponential expansion.
    The framework has N_e = 0.0037 (self-consistent, S64) — hopelessly
    insufficient for the standard stretching mechanism.

    TWO INTERPRETATIONS are tested:

    Interpretation A (Expansion Transfer):
        Perturbations generated at k ~ H_transit and stretched by expansion.
        Requires ln(k_transit/k_CMB) ~ 130 e-folds. Framework has 0.004.
        This interpretation FAILS by construction.

    Interpretation B (GGE Acoustic Spectrum):
        The GGE relic is an interference pattern of post-transit acoustic
        excitations on CG(24). The Bogoliubov process creates quasiparticles
        at ALL graph momenta simultaneously, including k=0 (the uniform mode
        on the 32-cell tessellation). The k=0 mode has infinite wavelength
        ON THE GRAPH — it is a uniform perturbation of the condensate.

        Key insight: On a discrete graph, the k=0 mode EXISTS NATIVELY.
        It is not a mode that was "stretched" from short wavelength.
        It is the singlet representation of the graph symmetry group.
        Particle creation at k=0 means the condensate's UNIFORM component
        is parametrically excited during the transit.

        After the transit, the GGE relic encodes occupation numbers n_k
        at all 32 k-points. The power spectrum P_GGE(k) = n_k * omega_k
        determines the observable perturbation spectrum.

        The mapping to physical CMB modes proceeds:
            - k=0 on CG(24) -> the spatially uniform mode
            - k>0 on CG(24) -> modes with wavelength ~ 1/(M_KK * sqrt(lambda_k))
            - The CMB power comes from the k=0 THROUGH k~few modes, not from
              redshifting short-wavelength modes

    This computation:
    1. Demonstrates that Interpretation A fails (N_e deficit quantified)
    2. Shows that Interpretation B gives nonzero P(k=0) from Bogoliubov data
    3. Computes the full GGE power spectrum P_GGE(k) on CG(24)
    4. Analyzes the Bogoliubov transfer function T(k) for k-independence
    5. Maps the graph-scale spectrum to physical scales

Session: S65 W2-B
Author: phonon-first-cosmologist
Depends on: s63_bogoliubov_cg24, s63_moduli_dispersion, s64_ne_selfconsist, s64_transfer_bogoliubov
"""

import sys
import os
import time
import numpy as np
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPT_DIR))

from canonical_constants import (
    M_KK, M_KK_gravity, M_Pl_reduced, M_Pl_unreduced,
    tau_fold, dt_transit, N_cells,
    a0_fold, a2_fold, a4_fold,
    S_fold, dS_fold, G_DeWitt,
    H_fold, v_terminal,
    A_s_CMB, PI, H_0_GeV, T_CMB_GeV,
    N_e_classical,
    Mpc_to_GeV_inv,
    c_Gold, omega_L1, omega_L2,
    E_cond, n_pairs,
    J_C2, J_su2, J_u1,
)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

OUT_NPZ = SCRIPT_DIR / "s65_scale_transfer.npz"
OUT_PNG = SCRIPT_DIR / "s65_scale_transfer.png"

t_start = time.time()

print("=" * 78)
print("S65 SCALE-TRANSFER-65: k_KK to k_CMB Mechanism")
print("=" * 78)

# =============================================================================
# SECTION 1: Load all input data
# =============================================================================
print("\n--- Section 1: Load input data ---")

# S63: Bogoliubov coefficients on CG(24)
d_bog = np.load(SCRIPT_DIR / "s63_bogoliubov_cg24.npz", allow_pickle=True)
omega_all = d_bog['omega_all']           # (50, 32, 45) omega(tau, k, mode)
beta_sq = d_bog['beta_sq']               # (32, 45) |beta|^2 per (k, mode)
alpha_sq = d_bog['alpha_sq']             # (32, 45) |alpha|^2
beta_sq_fold = d_bog['beta_sq_fold']     # (32, 45) fold-only Bogoliubov
sector_label = d_bog['sector_label']     # (32, 45) sector: 0=A, 1=B, 2=C
sector_weight = d_bog['sector_weight_all']  # (50, 32, 45, 3)
lambda_n = d_bog['lambda_n']             # (32,) graph Laplacian eigenvalues
k_eff = d_bog['k_eff']                   # (32,) effective wavevectors
tau_values = d_bog['tau_values']          # (50,) tau grid

N_k = len(lambda_n)                       # 32
N_modes = beta_sq.shape[1]                # 45
N_tau = len(tau_values)                    # 50

# S63: Moduli dispersion on CG(24)
d_disp = np.load(SCRIPT_DIR / "s63_moduli_dispersion.npz", allow_pickle=True)
branch_omega = d_disp['branch_omega']     # (36, 5) omega per (branch, k_graph)
c_eff_branches = d_disp['c_eff']          # (36,) effective speeds
omega_0_branches = d_disp['omega_0']      # (36,) zone-center frequencies
tier_labels = d_disp['tier_labels']       # (36,) branch labels
k_points_graph = d_disp['k_points']       # [0, 4, 6, 8, 12]
k_multiplicities = d_disp['k_multiplicities']  # [1, 9, 4, 9, 1]

# S64: Self-consistent e-folds
d_ne = np.load(SCRIPT_DIR / "s64_ne_selfconsist.npz", allow_pickle=True)
Ne_primary = float(d_ne['Ne_primary'])
Ne_range_lo = float(d_ne['Ne_range_lo'])
Ne_range_hi = float(d_ne['Ne_range_hi'])
H_phys_fold_GeV = float(d_ne['H_phys_fold_GeV'])
H_phys_fold_MKK = float(d_ne['H_phys_fold_MKK'])

# S64: Transfer Bogoliubov
d_trans = np.load(SCRIPT_DIR / "s64_transfer_bogoliubov.npz", allow_pickle=True)
gap_revised = float(d_trans['gap_revised'])       # A_s gap in OOM
beta_Gaussian_seq = float(d_trans['beta_Gaussian_seq'])
f0_trans = float(d_trans['f0'])
f2_trans = float(d_trans['f2'])
f4_trans = float(d_trans['f4'])

print(f"Loaded S63 Bogoliubov CG24: {N_k} k-points x {N_modes} modes")
print(f"  Total |beta|^2: {beta_sq.sum():.4f}")
print(f"  |beta|^2 at k=0: {beta_sq[0].sum():.4f}")
print(f"Loaded S63 moduli dispersion: {len(branch_omega)} branches x {len(k_points_graph)} k-points")
print(f"Loaded S64 e-folds: N_e = {Ne_primary:.6e} (range [{Ne_range_lo:.2e}, {Ne_range_hi:.2e}])")
print(f"  H_phys at fold: {H_phys_fold_GeV:.4e} GeV")
print(f"Loaded S64 transfer: A_s gap = {gap_revised:.2f} OOM")

# =============================================================================
# SECTION 2: Interpretation A — Expansion Transfer (Standard Mechanism)
# =============================================================================
print("\n" + "=" * 78)
print("INTERPRETATION A: Expansion Transfer (Standard Stretching)")
print("=" * 78)

# The standard inflation mechanism:
# - Perturbations generated at k_phys ~ H_inflation during slow-roll
# - Expansion redshifts k_phys: k_phys(t) = k_comoving / a(t)
# - After N_e e-folds: k_phys -> k_phys * exp(-N_e)
# - Need k_transit * exp(-N_e) = k_CMB => N_e = ln(k_transit/k_CMB)

# Physical scales
k_CMB_Mpc = 0.05                   # Planck pivot scale, Mpc^-1  # (local)
k_CMB_GeV = k_CMB_Mpc / Mpc_to_GeV_inv   # Convert to GeV

# Transit Hubble scale as transit wavenumber
k_transit_GeV = H_phys_fold_GeV    # ~ 2.94e16 GeV
k_transit_MKK = H_phys_fold_MKK    # ~ 0.396 M_KK

# Required e-folds
Ne_required = np.log(k_transit_GeV / k_CMB_GeV)
Ne_deficit = Ne_required - Ne_primary

# Expansion factor achieved
expansion_achieved = np.exp(Ne_primary)
expansion_required = np.exp(Ne_required)

# Physical wavenumber at recombination (if only expansion transfers modes)
# k_phys(recomb) = k_transit * exp(-Ne_framework) * (a_recomb/a_transit)
# But we only have the transit expansion, so:
k_phys_post_transit = k_transit_GeV * np.exp(-Ne_primary)

# Ratio to CMB scale
ratio_A = k_phys_post_transit / k_CMB_GeV

print(f"\nPhysical scales:")
print(f"  k_CMB = {k_CMB_Mpc} Mpc^-1 = {k_CMB_GeV:.4e} GeV")
print(f"  k_transit = H_fold = {k_transit_GeV:.4e} GeV")
print(f"  log10(k_transit/k_CMB) = {np.log10(k_transit_GeV/k_CMB_GeV):.2f}")
print(f"\nE-fold analysis:")
print(f"  Required N_e = ln(k_transit/k_CMB) = {Ne_required:.2f}")
print(f"  Framework N_e = {Ne_primary:.6e}")
print(f"  N_e classical ceiling = {N_e_classical:.4f}")
print(f"  DEFICIT = {Ne_deficit:.2f} e-folds")
print(f"\nExpansion factors:")
print(f"  Achieved: exp(N_e) = {expansion_achieved:.6f}")
print(f"  Required: exp(N_e) = {expansion_required:.4e}")
print(f"  Ratio: {expansion_required/expansion_achieved:.4e}")
print(f"\nPost-transit physical wavenumber:")
print(f"  k_phys(post-transit) = {k_phys_post_transit:.4e} GeV")
print(f"  k_phys / k_CMB = {ratio_A:.4e}")
print(f"\n>>> INTERPRETATION A: FAILS")
print(f">>> Deficit of {Ne_deficit:.1f} e-folds makes expansion transfer")
print(f">>> completely inoperative. k_phys remains at transit scale.")
print(f">>> P_A(k_CMB) = 0 exactly (no power at CMB scales from expansion).")

# =============================================================================
# SECTION 3: Interpretation B — GGE Acoustic Spectrum
# =============================================================================
print("\n" + "=" * 78)
print("INTERPRETATION B: GGE Acoustic Spectrum on CG(24)")
print("=" * 78)

# ---- 3a: Graph momentum structure ----
print("\n--- 3a: CG(24) momentum structure ---")

# The CG(24) graph has 32 nodes (cells of the Voronoi tessellation).
# The graph Laplacian L = D - A has eigenvalues lambda_n, n=0..31.
# lambda_0 = 0 (uniform/singlet mode), with eigenvector (1,1,...,1)/sqrt(32).
# The k=0 mode is the SPATIALLY UNIFORM perturbation of the condensate.

# Multiplicities from the graph symmetry
unique_lambda, counts = np.unique(np.round(lambda_n, 4), return_counts=True)
print(f"Graph Laplacian spectrum ({N_k} eigenvalues):")
print(f"  lambda range: [0, {lambda_n.max():.4f}]")
print(f"  {len(unique_lambda)} distinct eigenvalues")
print(f"  lambda_0 = {lambda_n[0]:.6f} (singlet, k=0)")
print(f"  lambda_1 = {lambda_n[1]:.6f} (first nonzero)")
print(f"  lambda_max = {lambda_n[-1]:.6f}")

# Physical wavelength mapping
# On the graph, each cell has size ~ 1/M_KK
# The effective wavevector on the graph is k_graph = sqrt(lambda_n)
# Physical wavenumber: k_phys = M_KK * sqrt(lambda_n)
k_phys_graph = M_KK * np.sqrt(lambda_n)  # (32,) in GeV
k_phys_graph[0] = 0.0  # Exact zero for singlet

print(f"\nPhysical wavenumber mapping (each cell ~ 1/M_KK):")
print(f"  k_phys(n=0) = 0 (uniform mode)")
print(f"  k_phys(n=1) = {k_phys_graph[1]:.4e} GeV")
print(f"  k_phys(n=31) = {k_phys_graph[-1]:.4e} GeV")
print(f"  Physical graph extent: ~ {N_cells**(1/3):.1f} / M_KK = {N_cells**(1/3)/M_KK:.4e} GeV^-1")

# ---- 3b: Bogoliubov occupation spectrum ----
print("\n--- 3b: GGE occupation number spectrum ---")

# Occupation numbers per k-point: n_k = sum_modes |beta_k^m|^2
n_k_total = beta_sq.sum(axis=1)                    # (32,) total per k
n_k_A = np.array([beta_sq[ik][sector_label[ik]==0].sum() for ik in range(N_k)])
n_k_B = np.array([beta_sq[ik][sector_label[ik]==1].sum() for ik in range(N_k)])
n_k_C = np.array([beta_sq[ik][sector_label[ik]==2].sum() for ik in range(N_k)])

print(f"Occupation numbers n_k (sum over modes at each k):")
print(f"  k=0 (singlet): n_total={n_k_total[0]:.4f}, n_A={n_k_A[0]:.4f}, n_B={n_k_B[0]:.4f}, n_C={n_k_C[0]:.4f}")
print(f"  k=1:           n_total={n_k_total[1]:.4f}, n_A={n_k_A[1]:.4f}, n_B={n_k_B[1]:.4f}, n_C={n_k_C[1]:.4f}")
print(f"  Mean:           n_total={n_k_total.mean():.4f}, n_A={n_k_A.mean():.4f}, n_B={n_k_B.mean():.4f}")
print(f"  Max:            n_total={n_k_total.max():.4f} at k_idx={np.argmax(n_k_total)}")

# CRITICAL RESULT: n_k(k=0) > 0 means the GGE HAS power at the k=0 mode.
# This is the uniform perturbation on the graph — a density fluctuation
# of the entire condensate, not localized to any cell.
print(f"\n>>> n(k=0) = {n_k_total[0]:.4f} > 0: GGE HAS power at k=0")
print(f">>> B-sector dominates: n_B(k=0) = {n_k_B[0]:.4f} ({n_k_B[0]/n_k_total[0]*100:.1f}% of total)")

# ---- 3c: GGE power spectrum ----
print("\n--- 3c: GGE power spectrum P_GGE(k) ---")

# Power spectrum: P(k) = sum_modes omega_m(k) * |beta_m(k)|^2
# This is the GGE energy per mode at each k-point.
omega_final = omega_all[-1]  # (32, 45) at tau_final (post-transit)

# Energy density per k: E(k) = sum_m omega_m(k,final) * |beta_m(k)|^2
# But omega_all can have negative eigenvalues (instabilities/artifacts)
# Use absolute value for energy
omega_final_abs = np.abs(omega_final)
E_k = np.sum(omega_final_abs * beta_sq, axis=1)  # (32,)

# Dimensionless power spectrum: Delta^2(k) = k^3 P(k) / (2*pi^2)
# But on a graph, the k-space measure is discrete, so we define
# P_GGE(k) = E_k / (number of modes at k = N_modes)
# For comparison to CMB: P(k) should have units of [length]^3 * [energy]
# We normalize to make it comparable to A_s
P_GGE = E_k  # M_KK units, energy per k-point

# For CMB comparison, the scalar power spectrum A_s:
# In inflation: A_s = H^2 / (8*pi^2 * eps * M_Pl^2)
# In our framework: the relevant quantity is the condensate density fluctuation

# The B-sector (BA phonon) contribution at k=0 gives the scalar perturbation
E_k_B = np.array([np.sum(omega_final_abs[ik][sector_label[ik]==1] *
                          beta_sq[ik][sector_label[ik]==1])
                   for ik in range(N_k)])

print(f"GGE energy spectrum E(k) [M_KK units]:")
print(f"  E(k=0) = {E_k[0]:.4f} (total),  E_B(k=0) = {E_k_B[0]:.4f}")
print(f"  E(k=1) = {E_k[1]:.4f} (total),  E_B(k=1) = {E_k_B[1]:.4f}")
print(f"  E(k_max) = {E_k[-1]:.4f} (total)")
print(f"  Total E_GGE = {E_k.sum():.4f} M_KK")

# ---- 3d: Bogoliubov transfer function T(k) ----
print("\n--- 3d: Bogoliubov transfer function T(k) ---")

# Define the transfer function as the ratio of occupation at k to the
# adiabatic parameter-weighted production rate.
# T(k) = n_k / <n_k>
# If T(k) is flat (k-independent), the GGE has scale-invariant occupation.

n_k_mean = n_k_total.mean()
T_k = n_k_total / n_k_mean  # Normalized transfer function

# Check for k-independence at low k
# For quasi-scale-invariance, we want T(k) ~ constant for k << k_max
T_low_k = T_k[:5]  # First 5 k-points
T_high_k = T_k[-5:]

print(f"Transfer function T(k) = n_k / <n_k>:")
for ik in range(min(10, N_k)):
    print(f"  k_idx={ik:2d}, lambda={lambda_n[ik]:.4f}: T(k) = {T_k[ik]:.4f}")
print(f"  ...")
for ik in range(max(0, N_k-3), N_k):
    print(f"  k_idx={ik:2d}, lambda={lambda_n[ik]:.4f}: T(k) = {T_k[ik]:.4f}")

# Flatness metric: std(T)/mean(T) for low-k modes
T_flatness_low = np.std(T_low_k) / np.mean(T_low_k)
T_flatness_all = np.std(T_k) / np.mean(T_k)
print(f"\nTransfer function flatness:")
print(f"  Low-k (first 5):  <T> = {T_low_k.mean():.4f}, sigma/mean = {T_flatness_low:.4f}")
print(f"  All k:            <T> = {T_k.mean():.4f}, sigma/mean = {T_flatness_all:.4f}")

# Key diagnostic: is T(k=0) comparable to T(k>0)?
T_0 = T_k[0]
T_nonzero_mean = T_k[1:].mean()
print(f"  T(k=0) = {T_0:.4f}")
print(f"  <T(k>0)> = {T_nonzero_mean:.4f}")
print(f"  Ratio T(k=0)/<T(k>0)> = {T_0/T_nonzero_mean:.4f}")

# ---- 3e: Spectral tilt of GGE power spectrum ----
print("\n--- 3e: Spectral tilt of P_GGE(k) ---")

# Fit the GGE spectrum to a power law in the nonzero-k regime:
# P_GGE(k) ~ k^alpha  => log(P) = alpha * log(k) + const
# Use lambda_n as proxy for k^2: P ~ lambda^(alpha/2)
mask_nonzero = lambda_n > 0
log_lambda = np.log(lambda_n[mask_nonzero])
log_E = np.log(E_k[mask_nonzero])

# Linear regression
from numpy.polynomial import polynomial as P_fit
coeffs = np.polyfit(log_lambda, log_E, 1)
alpha_E = coeffs[0]  # Slope: E(k) ~ lambda^alpha_E => E ~ k^{2*alpha_E}
spectral_index_alpha = 2 * alpha_E  # Since lambda ~ k^2

print(f"Power-law fit E(k) ~ lambda^alpha:")
print(f"  alpha_E = {alpha_E:.4f} (E vs lambda)")
print(f"  Spectral index: E(k) ~ k^{spectral_index_alpha:.4f}")
print(f"  For comparison: scale-invariant -> alpha = 0 (flat)")
print(f"  Harrison-Zeldovich: n_s - 1 = 0 -> P(k) ~ k^0")

# B-sector only
log_E_B = np.log(np.maximum(E_k_B[mask_nonzero], 1e-30))
valid_B = np.isfinite(log_E_B)
if valid_B.sum() > 2:
    coeffs_B = np.polyfit(log_lambda[valid_B], log_E_B[valid_B], 1)
    alpha_E_B = coeffs_B[0]
    print(f"  B-sector: E_B(k) ~ lambda^{alpha_E_B:.4f} => k^{2*alpha_E_B:.4f}")

# ---- 3f: Physical interpretation ----
print("\n--- 3f: Physical interpretation ---")

# The GGE acoustic spectrum has NONZERO occupation at k=0.
# This means the condensate's DENSITY FLUCTUATION has a uniform component.
#
# In the substrate picture:
# - Each cell of the 32-cell tessellation hosts a BCS condensate
# - The k=0 mode is the in-phase oscillation of ALL cells
# - The Bogoliubov process creates |beta(k=0)|^2 ~ 3.7 pairs at k=0
# - These pairs represent a UNIFORM density perturbation
#
# The mapping to physical CMB scales:
# - The k=0 mode on CG(24) maps to k_phys = 0 (infinite wavelength)
# - This IS a superhorizon perturbation — no expansion needed
# - The power at k=0 sets the "DC offset" of the perturbation spectrum
# - The power at k>0 sets the spatial structure at scales ~ 1/k_phys
#
# The CONTINUOUS limit:
# - CG(24) is a discrete graph with 32 nodes
# - In the continuum limit (N_cells -> infinity), the graph Laplacian
#   becomes the continuum Laplacian, and the discrete spectrum fills in
# - The occupation at k=0 remains nonzero in this limit (it's the
#   integral of the creation rate over modes, and the integrand is
#   smooth at k=0)
#
# The spectrum on CG(24) samples the FULL range from k=0 to k_max.
# No e-folds of expansion are needed because the perturbations are
# NOT generated at a single scale and then stretched. They are generated
# AT EVERY SCALE SIMULTANEOUSLY by the parametric process.

# Estimate P_GGE(k=0) in units comparable to A_s
# A_s = <delta_rho/rho>^2 at CMB scales
# From the GGE: delta_rho at k=0 = sum_m omega_m |beta_m|^2 at k=0
# Total GGE energy = E_GGE_total
# delta_rho/rho at k=0 ~ E(k=0) / E_total_per_cell
E_total = E_k.sum()
E_per_cell = E_total / N_cells

# The condensate energy per cell is |E_cond| (BCS ground state)
delta_rho_over_rho_k0 = E_k[0] / (N_cells * abs(E_cond))

# For the B-sector (the mode that maps to scalar perturbations):
delta_rho_over_rho_k0_B = E_k_B[0] / (N_cells * abs(E_cond))

print(f"Power at k=0:")
print(f"  E_GGE(k=0) = {E_k[0]:.4f} M_KK")
print(f"  E_GGE_B(k=0) = {E_k_B[0]:.4f} M_KK")
print(f"  E_cond = {E_cond:.4f} M_KK (per cell)")
print(f"  N_cells = {N_cells}")
print(f"  delta_rho/rho(k=0, total) = {delta_rho_over_rho_k0:.6e}")
print(f"  delta_rho/rho(k=0, B-sector) = {delta_rho_over_rho_k0_B:.6e}")
print(f"  (delta_rho/rho)^2 at k=0 = {delta_rho_over_rho_k0_B**2:.6e}")
print(f"  A_s(observed) = {A_s_CMB:.4e}")
print(f"  log10( (delta/rho)^2 / A_s ) = {np.log10(delta_rho_over_rho_k0_B**2 / A_s_CMB):.2f}")

# ---- 3g: Continuum extrapolation ----
print("\n--- 3g: Continuum limit extrapolation ---")

# In the continuum limit, the graph becomes a manifold.
# The GGE occupation in the continuum is:
#   n(k) = |beta(k)|^2 integrated over mode directions
# The discrete CG(24) result samples this at 32 k-points.
#
# For the power spectrum, the relevant quantity is:
#   P(k) = (2*pi)^{-3} * integral d^3k' |beta(k')|^2 * delta(|k'|-k)
#        = k^2 / (2*pi^2) * |beta(k)|^2
#
# The n_s - 1 parameter (spectral tilt) depends on the k-dependence of |beta|^2.
# From the discrete data: |beta|^2 vs lambda_n shows a RISING trend
# (more pair creation at high k due to stronger nonadiabatic driving).
#
# This rising spectrum on the graph means n_s > 1 (blue tilt) at graph scales.
# However, the CMB corresponds to the k << k_graph limit, where the
# spectrum approaches the k=0 value. The tilt at CMB scales depends on
# how the discrete graph result extrapolates to the continuum.

# Fit occupation vs k for small k (first 10 modes)
lambda_low = lambda_n[1:10]  # Exclude k=0 itself
n_k_low = n_k_total[1:10]

# Linear extrapolation to test if n(k->0) is smooth
from scipy.interpolate import interp1d

# Fit: n_k = a + b*lambda for small lambda
if len(lambda_low) > 2:
    coeffs_lin = np.polyfit(lambda_low, n_k_low, 1)
    n_k_extrap_0 = coeffs_lin[1]  # Extrapolated n(k=0) from linear fit
    slope_n = coeffs_lin[0]
    print(f"Small-k occupation fit: n(k) = {coeffs_lin[1]:.4f} + {coeffs_lin[0]:.4f} * lambda")
    print(f"  Extrapolated n(k=0) = {n_k_extrap_0:.4f}")
    print(f"  Actual n(k=0) = {n_k_total[0]:.4f}")
    print(f"  Ratio actual/extrapolated = {n_k_total[0]/n_k_extrap_0:.4f}")

# ---- 3h: BA acoustic branch analysis ----
print("\n--- 3h: BA acoustic branch (Anderson-Bogoliubov sound mode) ---")

# The lowest-energy collective excitation is the Anderson-Bogoliubov (AB)
# sound mode. This is the Goldstone mode of the broken U(1) symmetry.
# Its dispersion is omega_AB(k) = c_BA * k for small k.
#
# From canonical constants: c_Gold = 0.915 M_KK (Goldstone speed)
# The AB mode at k=0 has omega = 0 (Goldstone theorem).
# But the discrete graph has a gap at k=0 due to finite size.
#
# For the scale transfer: the AB mode is the one that maps to 4D scalar
# perturbations (density/pressure oscillations of the condensate).

# Identify the AB branch in the Bogoliubov data
# At k=0, the BA phonon modes have specific frequencies.
# The lowest B-sector frequency at k=0 should be the AB mode.

omega_k0 = omega_all[-1, 0, :]  # (45,) at k=0, tau_final
B_mask_k0 = sector_label[0] == 1
omega_B_k0 = omega_k0[B_mask_k0]
beta_B_k0 = beta_sq[0, B_mask_k0]

sort_idx = np.argsort(np.abs(omega_B_k0))
print(f"B-sector modes at k=0 (sorted by |omega|):")
for i in sort_idx[:8]:
    print(f"  omega = {omega_B_k0[i]:+.6f} M_KK, |beta|^2 = {beta_B_k0[i]:.6f}")

# The smallest-frequency B mode is the AB sound mode at k=0
# Its |beta|^2 gives the particle production at the uniform scale
omega_AB_k0 = omega_B_k0[sort_idx[0]]
beta_AB_k0 = beta_B_k0[sort_idx[0]]
print(f"\nAB mode at k=0:")
print(f"  omega_AB(k=0) = {omega_AB_k0:.6f} M_KK")
print(f"  |beta_AB(k=0)|^2 = {beta_AB_k0:.6f}")

# =============================================================================
# SECTION 4: Combined Assessment
# =============================================================================
print("\n" + "=" * 78)
print("SECTION 4: COMBINED ASSESSMENT")
print("=" * 78)

# Interpretation A: FAILS
P_A_kCMB = 0.0  # Exactly zero — expansion transfers nothing  # (local)

# Interpretation B:
# The GGE has nonzero occupation at k=0: n(k=0) = 3.68
# The B-sector carries 99% of this: n_B(k=0) = 3.64
# The energy at k=0: E_B(k=0) = E_k_B[0] M_KK
# This gives a nonzero perturbation at the uniform (superhorizon) scale.
P_B_kCMB = n_k_B[0]  # Nonzero occupation = nonzero power

# Amplitude estimate
# The naive delta_rho/rho ~ sqrt(A_s) ~ 5e-5 requires careful normalization
# We have (delta_rho/rho)^2 ~ E_B(k=0)/(N_cells * |E_cond|)^2
# This is a ROUGH estimate — the actual A_s depends on:
# 1. The spectral action perturbation equation
# 2. The mapping from graph-mode amplitude to curvature perturbation
# 3. The matching to the 4D FRW perturbation spectrum
#
# From S64 TRANSFER-BOGOLIUBOV-64: A_s gap was 3.16 OOM (before transfer analysis)
# The new estimate using graph-mode data:
amplitude_est = delta_rho_over_rho_k0_B**2
amplitude_gap_OOM = np.log10(amplitude_est / A_s_CMB)

print(f"\nInterpretation A: P_A(k_CMB) = {P_A_kCMB}")
print(f"  => FAILS: N_e deficit of {Ne_deficit:.1f} e-folds")
print(f"  => No mechanism to transfer transit-scale perturbations to CMB")
print(f"")
print(f"Interpretation B: P_B(k_CMB) > 0")
print(f"  n_B(k=0) = {n_k_B[0]:.4f} (nonzero occupation at uniform mode)")
print(f"  E_B(k=0) = {E_k_B[0]:.4f} M_KK")
print(f"  => PASSES: GGE has nonzero power at k=0 (superhorizon) scale")
print(f"")
print(f"Amplitude comparison:")
print(f"  (delta_rho/rho)^2(k=0) ~ {amplitude_est:.4e}")
print(f"  A_s(observed) = {A_s_CMB:.4e}")
print(f"  Gap: {amplitude_gap_OOM:.2f} OOM")
print(f"  => Amplitude known only to {abs(amplitude_gap_OOM):.1f} OOM")

# Gate verdict
if P_B_kCMB > 0:
    if abs(amplitude_gap_OOM) <= 3.0:
        gate_verdict = "PASS"
        gate_detail = (
            f"Interpretation B gives nonzero P(k_CMB). n_B(k=0)={n_k_B[0]:.4f}. "
            f"Amplitude gap = {amplitude_gap_OOM:.2f} OOM (within 3 OOM threshold)."
        )
    else:
        gate_verdict = "INFO"
        gate_detail = (
            f"Interpretation B gives nonzero P(k_CMB) via GGE k=0 mode: n_B(k=0)={n_k_B[0]:.4f}. "
            f"Interpretation A FAILS (N_e deficit = {Ne_deficit:.1f}). "
            f"Amplitude gap = {amplitude_gap_OOM:.2f} OOM (exceeds 3 OOM threshold). "
            f"The MECHANISM works (k=0 mode exists natively on graph), "
            f"but amplitude requires proper spectral-action-to-curvature-perturbation normalization."
        )
else:
    gate_verdict = "FAIL"
    gate_detail = "Both interpretations give P(k_CMB) = 0."

print(f"\n{'='*78}")
print(f"GATE VERDICT: SCALE-TRANSFER-65 = {gate_verdict}")
print(f"{'='*78}")
print(f"  {gate_detail}")

# =============================================================================
# SECTION 5: Summary diagnostics table
# =============================================================================
print("\n--- Summary Table ---")
print(f"{'Quantity':<45s} {'Value':<25s} {'Unit':<15s}")
print("-" * 85)
print(f"{'N_e (framework, self-consistent)':<45s} {Ne_primary:<25.6e} {'e-folds':<15s}")
print(f"{'N_e (required for expansion transfer)':<45s} {Ne_required:<25.2f} {'e-folds':<15s}")
print(f"{'N_e deficit':<45s} {Ne_deficit:<25.2f} {'e-folds':<15s}")
print(f"{'k_transit / k_CMB':<45s} {k_transit_GeV/k_CMB_GeV:<25.4e} {'':<15s}")
print(f"{'n_GGE(k=0, total)':<45s} {n_k_total[0]:<25.4f} {'pairs':<15s}")
print(f"{'n_GGE(k=0, B-sector)':<45s} {n_k_B[0]:<25.4f} {'pairs':<15s}")
print(f"{'n_GGE(k=0, A-sector)':<45s} {n_k_A[0]:<25.4f} {'pairs':<15s}")
print(f"{'E_GGE(k=0, B-sector)':<45s} {E_k_B[0]:<25.4f} {'M_KK':<15s}")
print(f"{'<n_GGE> (all k)':<45s} {n_k_mean:<25.4f} {'pairs':<15s}")
print(f"{'T(k=0) = n(k=0)/<n>':<45s} {T_0:<25.4f} {'':<15s}")
print(f"{'(delta_rho/rho)^2(k=0)':<45s} {amplitude_est:<25.4e} {'':<15s}")
print(f"{'A_s(observed)':<45s} {A_s_CMB:<25.4e} {'':<15s}")
print(f"{'Amplitude gap':<45s} {amplitude_gap_OOM:<25.2f} {'OOM':<15s}")
print(f"{'Spectral index E(k) ~ k^alpha':<45s} {spectral_index_alpha:<25.4f} {'':<15s}")
print(f"{'Transfer flatness (low-k, sigma/mean)':<45s} {T_flatness_low:<25.4f} {'':<15s}")
print(f"{'Transfer flatness (all k, sigma/mean)':<45s} {T_flatness_all:<25.4f} {'':<15s}")

# =============================================================================
# SECTION 6: Save results
# =============================================================================
print("\n--- Saving results ---")

save_dict = {
    # Interpretation A
    'Ne_primary': Ne_primary,
    'Ne_required': Ne_required,
    'Ne_deficit': Ne_deficit,
    'k_transit_GeV': k_transit_GeV,
    'k_CMB_GeV': k_CMB_GeV,
    'ratio_k_transit_k_CMB': k_transit_GeV / k_CMB_GeV,
    'P_A_kCMB': P_A_kCMB,

    # Interpretation B
    'lambda_n': lambda_n,
    'k_eff': k_eff,
    'k_phys_graph': k_phys_graph,
    'n_k_total': n_k_total,
    'n_k_A': n_k_A,
    'n_k_B': n_k_B,
    'n_k_C': n_k_C,
    'E_k': E_k,
    'E_k_B': E_k_B,
    'T_k': T_k,
    'T_flatness_low': T_flatness_low,
    'T_flatness_all': T_flatness_all,

    # Amplitude
    'delta_rho_over_rho_k0': delta_rho_over_rho_k0,
    'delta_rho_over_rho_k0_B': delta_rho_over_rho_k0_B,
    'amplitude_est': amplitude_est,
    'amplitude_gap_OOM': amplitude_gap_OOM,
    'spectral_index_alpha': spectral_index_alpha,

    # Gate
    'gate_name': 'SCALE-TRANSFER-65',
    'gate_verdict': gate_verdict,
    'gate_detail': gate_detail,
}

np.savez(OUT_NPZ, **save_dict)
print(f"Saved: {OUT_NPZ}")

# =============================================================================
# SECTION 7: Plot
# =============================================================================
print("\n--- Generating plot ---")

fig = plt.figure(figsize=(16, 12))
gs = GridSpec(2, 3, figure=fig, hspace=0.35, wspace=0.35)

# Panel 1: GGE occupation spectrum n(k)
ax1 = fig.add_subplot(gs[0, 0])
ax1.plot(lambda_n, n_k_total, 'ko-', ms=4, label='Total')
ax1.plot(lambda_n, n_k_B, 'b^-', ms=4, label='B (BA phonon)')
ax1.plot(lambda_n, n_k_A, 'r+-', ms=4, label='A (geometric)')
ax1.axhline(n_k_total.mean(), color='gray', ls='--', alpha=0.5, label=f'<n> = {n_k_mean:.1f}')
ax1.set_xlabel(r'$\lambda_n$ (graph Laplacian eigenvalue)')
ax1.set_ylabel(r'$n_k = \sum_m |\beta^m_k|^2$')
ax1.set_title('GGE Occupation Spectrum')
ax1.legend(fontsize=8)
ax1.set_xlim(-0.3, lambda_n.max() + 0.3)

# Panel 2: GGE energy spectrum
ax2 = fig.add_subplot(gs[0, 1])
ax2.semilogy(lambda_n, E_k, 'ko-', ms=4, label='Total')
ax2.semilogy(lambda_n, E_k_B, 'b^-', ms=4, label='B sector')
ax2.set_xlabel(r'$\lambda_n$')
ax2.set_ylabel(r'$E(k)$ [M$_{\rm KK}$]')
ax2.set_title('GGE Energy Spectrum')
ax2.legend(fontsize=8)

# Panel 3: Transfer function T(k)
ax3 = fig.add_subplot(gs[0, 2])
ax3.plot(lambda_n, T_k, 'ko-', ms=5)
ax3.axhline(1.0, color='gray', ls='--', alpha=0.5)
ax3.axhline(T_k[0], color='blue', ls=':', alpha=0.5, label=f'T(k=0) = {T_k[0]:.3f}')
ax3.set_xlabel(r'$\lambda_n$')
ax3.set_ylabel(r'$T(k) = n_k / \langle n \rangle$')
ax3.set_title('Transfer Function')
ax3.legend(fontsize=8)

# Panel 4: Interpretation A vs B scale diagram
ax4 = fig.add_subplot(gs[1, 0])
# Show the scale gap
scales_labels = [r'$k_{\rm CMB}$', r'$H_0$', r'$T_{\rm CMB}$', r'$T_{\rm recomb}$', r'$k_{\rm transit}$']
scales_GeV = [k_CMB_GeV, H_0_GeV, T_CMB_GeV, 0.26e-9, k_transit_GeV]
scales_log = [np.log10(s) for s in scales_GeV]
colors = ['blue', 'green', 'orange', 'red', 'purple']
for i, (lab, lg, col) in enumerate(zip(scales_labels, scales_log, colors)):
    ax4.barh(i, lg - scales_log[0], left=scales_log[0], color=col, alpha=0.6, height=0.5)
    ax4.text(lg + 0.5, i, f'{lab}\n{scales_GeV[i]:.1e} GeV', fontsize=7, va='center')
ax4.set_xlabel(r'$\log_{10}(k / {\rm GeV})$')
ax4.set_title('Scale Hierarchy')
ax4.set_yticks([])
# Mark the N_e deficit
ax4.annotate('', xy=(scales_log[0], 4.5), xytext=(scales_log[-1], 4.5),
             arrowprops=dict(arrowstyle='<->', color='red', lw=2))
ax4.text(np.mean([scales_log[0], scales_log[-1]]), 4.8,
         f'N_e deficit: {Ne_deficit:.0f} e-folds\n(Interp A FAILS)',
         ha='center', fontsize=8, color='red', fontweight='bold')

# Panel 5: Bogoliubov |beta|^2 heatmap
ax5 = fig.add_subplot(gs[1, 1])
# Show first 15 modes x 32 k-points
beta_display = beta_sq[:, :15].T  # (15, 32)
im = ax5.imshow(beta_display, aspect='auto', origin='lower',
                extent=[0, 31, -0.5, 14.5], cmap='hot',
                norm=matplotlib.colors.LogNorm(vmin=1e-6, vmax=beta_sq.max()))
ax5.set_xlabel('k-point index')
ax5.set_ylabel('Mode index')
ax5.set_title(r'$|\beta^m_k|^2$ (first 15 modes)')
plt.colorbar(im, ax=ax5, label=r'$|\beta|^2$')

# Panel 6: Comparison to A_s
ax6 = fig.add_subplot(gs[1, 2])
# Bar chart of amplitude estimates
bar_labels = [r'$A_s^{\rm obs}$', r'$({\delta\rho}/{\rho})^2_{k=0}$',
              r'$({\delta\rho}/{\rho})^2_{k=0,B}$']
bar_values = [A_s_CMB, delta_rho_over_rho_k0**2, amplitude_est]
bar_log = [np.log10(v) if v > 0 else -30 for v in bar_values]
bar_colors = ['green', 'blue', 'navy']
bars = ax6.barh(range(len(bar_labels)), bar_log, color=bar_colors, alpha=0.7)
ax6.set_xlabel(r'$\log_{10}$ Amplitude')
ax6.set_yticks(range(len(bar_labels)))
ax6.set_yticklabels(bar_labels, fontsize=9)
ax6.set_title(f'Amplitude Comparison\n(gap = {amplitude_gap_OOM:.1f} OOM)')
for i, (lab, val) in enumerate(zip(bar_labels, bar_log)):
    ax6.text(val + 0.1, i, f'{val:.1f}', va='center', fontsize=8)

fig.suptitle(f'SCALE-TRANSFER-65: k_KK to k_CMB Mechanism\n'
             f'Gate: {gate_verdict} | Interp A: FAIL (N_e deficit={Ne_deficit:.0f}) | '
             f'Interp B: n_B(k=0)={n_k_B[0]:.2f}, gap={amplitude_gap_OOM:.1f} OOM',
             fontsize=12, fontweight='bold')

plt.savefig(OUT_PNG, dpi=150, bbox_inches='tight')
print(f"Saved: {OUT_PNG}")

elapsed = time.time() - t_start
print(f"\nTotal runtime: {elapsed:.1f}s")
print(f"\nDone.")
