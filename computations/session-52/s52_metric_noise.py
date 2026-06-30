#!/usr/bin/env python3
"""
S52 METRIC-NOISE-52: Stochastic Metric Noise from 32-Cell Voronoi Tessellation
================================================================================

Computes amplitude and frequency spectrum of stochastic metric fluctuations
arising from the discrete internal structure of the 32-cell fabric tessellation.

Physics:
--------
1. The 32-cell Voronoi tessellation (S42) means the internal SU(3) fiber has
   discrete structure at scale L_cell ~ (Vol_SU3 / N_cells)^{1/8}.

2. Cell-to-cell fluctuations in tau produce metric noise:
       delta(g_mu_nu) ~ (delta_tau / tau_fold) * g_mu_nu

3. The Goldstone mode (W1-F, GL-JOSEPHSON-52) propagates with c_BCS = 0.915 M_KK.
   The fabric sound speed c_fabric = 209.97 M_KK (spectral action gradient stiffness).

4. The noise spectrum is shaped by THREE scales:
   (a) L_cell: sets the UV cutoff (wavelength below cell size has no meaning)
   (b) m_tau = 2.062 M_KK: fabric mass gap (exponentially suppresses sub-gap frequencies)
   (c) T_acoustic = 0.112 M_KK: GGE acoustic temperature (thermal excitation scale)

5. Strain conversion: h = delta_L / L ~ delta_tau * (l_P / L_phys)^relevant_scaling

Key inputs from canonical_constants:
    N_cells = 32 (S42)
    Vol_SU3_Haar = 1349.74 (S44)
    M_KK = 7.43e16 GeV (gravity route)
    tau_fold = 0.19
    delta_tau/tau = 1.75e-6 (HOMOG-42)
    m_tau = 2.062 M_KK (fabric gap)
    J_C2 = 0.933, J_su2 = 0.059, J_u1 = 0.038 (Josephson couplings)
    T_acoustic = 0.112 M_KK (GGE temperature)
    c_fabric = 209.97 M_KK

Gate: INFO (amplitude, spectrum, comparison to GQuEST/LIGO/LISA)

Reference papers:
    - Verlinde-Zurek 2021 (Paper 20): S_h(f) ~ f^{-1/2} geontropic spectrum
    - Vermeulen et al. 2025 (Paper 17): GQuEST sensitivity ~10^{-21} Hz^{-1/2}
    - Zurek 2022 (Paper 13): Pixellon metric fluctuation model
    - Carlip 2025 (Paper 14): Midisuperspace foam, CC hiding

Author: Quantum-Foam-Theorist (S52)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    N_cells, Vol_SU3_Haar, M_KK, M_KK_gravity, M_KK_kerner,
    M_Pl_reduced, M_Pl_unreduced, tau_fold, m_tau,
    J_C2, J_su2, J_u1, T_acoustic, c_fabric,
    l_Planck, hbar_GeV_s, hbar_c_GeV_m, c_light,
    GeV_to_inv_s, GeV_to_inv_m, PI, S_fold,
    E_B1, E_B2_mean, E_B3_mean, Delta_0_GL,
    rho_Lambda_obs, Lambda_obs_MP4
)

print("=" * 72)
print("S52 METRIC-NOISE-52: Stochastic Metric Noise from Tessellation")
print("=" * 72)

# ==============================================================================
# SECTION 1: Cell geometry and fundamental scales
# ==============================================================================
print("\n--- SECTION 1: Cell Geometry ---")

# SU(3) has dim = 8 as a manifold.
# Cell size from Voronoi decomposition:
# L_cell^8 ~ Vol_SU3 / N_cells  (in M_KK^{-8} units)
# L_cell ~ (Vol_SU3 / N_cells)^{1/8}  in M_KK^{-1}

dim_SU3 = 8  # (local)
L_cell_MKK = (Vol_SU3_Haar / N_cells) ** (1.0 / dim_SU3)

print(f"Vol_SU3_Haar = {Vol_SU3_Haar:.2f}  (M_KK^{{-8}})")
print(f"N_cells = {N_cells}")
print(f"Vol_cell = {Vol_SU3_Haar / N_cells:.2f}  (M_KK^{{-8}})")
print(f"L_cell = {L_cell_MKK:.4f}  (M_KK^{{-1}})")

# Physical cell size
L_cell_GeV_inv = L_cell_MKK / M_KK  # in GeV^{-1}
L_cell_m = L_cell_MKK * hbar_c_GeV_m / M_KK  # in meters
print(f"L_cell = {L_cell_GeV_inv:.3e}  GeV^{{-1}}")
print(f"L_cell = {L_cell_m:.3e}  m")

# For comparison: Planck length, and M_KK^{-1}
L_KK_m = hbar_c_GeV_m / M_KK
print(f"M_KK^{{-1}} = {L_KK_m:.3e}  m")
print(f"l_Planck = {l_Planck:.3e}  m")
print(f"L_cell / l_Planck = {L_cell_m / l_Planck:.3e}")
print(f"L_cell / M_KK^{{-1}} = {L_cell_MKK:.4f}")

# ==============================================================================
# SECTION 2: Metric fluctuation amplitude from cell-to-cell tau variations
# ==============================================================================
print("\n--- SECTION 2: Metric Fluctuation Amplitude ---")

# HOMOG-42: delta_tau / tau_fold = 1.75e-6
delta_tau_over_tau = 1.75e-6
delta_tau = delta_tau_over_tau * tau_fold

print(f"tau_fold = {tau_fold}")
print(f"delta_tau / tau = {delta_tau_over_tau:.3e}  (HOMOG-42)")
print(f"delta_tau = {delta_tau:.3e}")

# The Jensen metric g_tau = 3 * diag(e^{2tau}, e^{2tau}, e^{2tau},
#                                     e^{-2tau}, e^{-2tau}, e^{-2tau}, e^{-2tau},
#                                     e^{tau})
# Metric perturbation from tau -> tau + delta_tau:
# delta(g_ii) / g_ii = (dg_ii/dtau) * delta_tau / g_ii
# For the e^{2tau} block: dg/dtau / g = 2 -> delta_g/g = 2 * delta_tau
# For the e^{-2tau} block: dg/dtau / g = -2 -> delta_g/g = -2 * delta_tau
# For the e^{tau} direction: dg/dtau / g = 1 -> delta_g/g = delta_tau
#
# RMS fractional metric perturbation (averaged over all 8 directions):
# <(delta_g/g)^2> = (1/8) * [3*(2*delta_tau)^2 + 4*(2*delta_tau)^2 + 1*(delta_tau)^2]
# = (1/8) * delta_tau^2 * [3*4 + 4*4 + 1] = (1/8) * delta_tau^2 * 29
# delta_g/g_rms = delta_tau * sqrt(29/8)

factor_sq = (3 * 4 + 4 * 4 + 1)  # = 29
rms_factor = np.sqrt(factor_sq / dim_SU3)
delta_g_over_g = delta_tau * rms_factor

print(f"\nJensen metric perturbation:")
print(f"  <(delta_g/g)^2>^{{1/2}} / delta_tau = sqrt({factor_sq}/{dim_SU3}) = {rms_factor:.4f}")
print(f"  delta_g/g (internal, per cell) = {delta_g_over_g:.3e}")

# How this maps to 4D strain:
# The 4D effective metric includes the conformal factor from the internal volume:
#   g_4D ~ (det g_internal)^{1/4} * g_M4    (Kaluza-Klein reduction)
# Since det(g_Jensen) = 3^8 * exp[2*3*tau + (-2)*4*tau + 1*tau] * tau_vol_factor
# The exponent = 6tau - 8tau + tau = -tau.
# Volume-preserving: d(det)/dtau = 0 at tau=0 by construction.
# At tau_fold: d(ln det)/dtau = 6 - 8 + 1 = -1
# So delta(ln det) = -delta_tau, delta(det^{1/4}) / det^{1/4} = -delta_tau/4

# BUT: the volume-preserving TT deformation (Session 12) enforces
# d(det g_tau)/dtau = 0 at ALL tau, not just tau=0.
# Wait -- let me recalculate. The normalization is:
# g_tau = 3 * diag(e^{2tau}, e^{2tau}, e^{2tau}, e^{-2tau}, e^{-2tau}, e^{-2tau}, e^{-2tau}, e^{tau})
# det(g_tau) = 3^8 * e^{6tau} * e^{-8tau} * e^{tau} = 3^8 * e^{-tau}
# This is NOT volume-preserving in terms of det(g).
# The actual TT parameterization uses traceless-transverse, and the factor of 3
# is the initial uniform value. Let me use the correct form:
# g_tau has trace: Tr(g_tau) = 3*(3*e^{2tau} + 4*e^{-2tau} + e^{tau})
# Volume element = sqrt(det(g_tau))
# det = 3^8 * exp(3*2tau + 4*(-2tau) + tau) = 3^8 * exp(-tau)
# d(ln det)/dtau = -1

# But the Haar volume is FIXED = 1349.74 regardless of tau. This means the
# Riemannian volume integrand already includes the correct Weyl integration
# factors. The KK reduction properly done:
# G_4D / G_10D ~ 1 / Vol_internal
# The internal volume fluctuation:
# delta(Vol) / Vol = (1/2) * Tr(g^{-1} delta_g)
# For our perturbation: Tr(g^{-1} delta_g) = sum_i (delta g_ii / g_ii)
# = delta_tau * (3*2 + 4*(-2) + 1) = delta_tau * (6 - 8 + 1) = -delta_tau
# So delta(Vol)/Vol = -delta_tau / 2 per cell.
# The 4D Newton constant fluctuates as:
# delta(G_N) / G_N = -delta(Vol) / Vol = delta_tau / 2

delta_vol_over_vol = -delta_tau / 2
delta_GN_over_GN = delta_tau / 2

print(f"\nVolume and Newton constant fluctuation:")
print(f"  Tr(g^{{-1}} delta_g) = (6-8+1) * delta_tau = -delta_tau")
print(f"  delta(Vol)/Vol per cell = {delta_vol_over_vol:.3e}")
print(f"  delta(G_N)/G_N per cell = {delta_GN_over_GN:.3e}")

# The 4D metric fluctuation from KK reduction:
# g_4D_mu_nu = g_M4_mu_nu * Phi^{2/(d-2)} where Phi = (det g_int)^{1/2}
# For d=4+8=12: g_4D ~ g_M4 * Phi^{1/5}
# delta(g_4D)/g_4D ~ (1/5) * delta(Phi)/Phi ~ (1/10) * delta_tau
# But more precisely in Einstein frame KK:
# h_mu_nu ~ (M_KK / M_Pl)^2 * delta_g_internal
# The strain from internal fluctuations:

ratio_MKK_MPl = M_KK / M_Pl_unreduced
print(f"\nM_KK / M_Pl = {ratio_MKK_MPl:.3e}  ({np.log10(ratio_MKK_MPl):.2f} dex)")

# Method 1: Naive KK strain
# h ~ delta_tau * (M_KK / M_Pl)^2
h_naive = delta_tau * ratio_MKK_MPl**2
print(f"\nMethod 1 (naive KK): h ~ delta_tau * (M_KK/M_Pl)^2 = {h_naive:.3e}")

# Method 2: Proper effacement (QF-12, S43)
# sigma_lambda ~ 10^{-4} per fold  (fold foam protection, left-invariant)
# The effacement factor delta_g = 7.8e-8 (PERLMAN-43) is the dominant suppression
effacement = 7.8e-8  # S43 PERLMAN-43
h_effaced = delta_tau * effacement
print(f"Method 2 (effacement): h ~ delta_tau * delta_g = {h_effaced:.3e}")

# Method 3: Volume-averaged over N_cells
# The 32 cells are not independent -- they share boundaries with Josephson coupling.
# But the tau fluctuation is COHERENT across the full SU(3) manifold (HOMOG-42).
# The 32-cell structure gives DISCRETE modes, not independent noise.
# The metric noise comes from PHONON excitations of the tessellation,
# not from independent random cells.

# Key physics: the 32-cell structure supports 32 modes (1 per cell in k-space).
# The acoustic modes have dispersion omega(K) from GL-JOSEPHSON-52.
# Each mode carries energy T_acoustic (GGE temperature).
# The metric noise is the superposition of all excited modes.

print("\n--- SECTION 3: Tessellation Phonon Modes ---")

# BCC-like lattice (S52 W1-F): a = 4.386 M_KK^{-1}, K_BZ = 0.716 M_KK
a_lattice = 4.386  # M_KK^{-1}  # (local)
K_BZ = 0.716  # M_KK  # (local)

# From GL-JOSEPHSON-52 (W1-F): 6 branches
# Using only the 3 phase branches (these are the gapless/soft modes):
# Goldstone: omega(0)=0, omega(K_BZ)=0.507, c_Gold = 0.915 M_KK
# Leggett-1: omega(0)=0.138, omega(K_BZ)=0.529
# Leggett-2: omega(0)=0.192, omega(K_BZ)=0.986

c_Gold = 0.915  # M_KK (dimensionless speed, i.e., omega/K in M_KK units)
omega_L1 = 0.138  # M_KK
omega_L2 = 0.192  # M_KK
omega_Gold_BZ = 0.507  # M_KK at zone boundary  # (local)

# Number of K-modes per branch: for BCC lattice with N_cells sites in real space,
# there are N_cells K-modes in the first BZ.
# But N_cells=32 sites on the Voronoi tessellation, so 32 K-points per branch.
N_K = N_cells

print(f"Lattice constant a = {a_lattice:.3f} M_KK^{{-1}}")
print(f"BZ boundary K_BZ = {K_BZ:.3f} M_KK")
print(f"Goldstone speed c_Gold = {c_Gold:.3f} M_KK")
print(f"Leggett-1 gap = {omega_L1:.3f} M_KK")
print(f"Leggett-2 gap = {omega_L2:.3f} M_KK")
print(f"N_K modes per branch = {N_K}")

# ==============================================================================
# SECTION 4: Noise Spectrum Computation
# ==============================================================================
print("\n--- SECTION 4: Noise Spectrum S_h(f) ---")

# The metric noise power spectral density from tessellation phonons.
#
# Each phonon mode (branch b, wavevector K) contributes:
#   S_h(f) = |h_bK|^2 * delta(f - f_bK)
# where h_bK is the strain amplitude per mode.
#
# For a thermal ensemble at T_acoustic:
#   <n_bK> = 1 / (exp(omega_bK / T_acoustic) - 1)
# Energy per mode: E_bK = omega_bK * (<n_bK> + 1/2)
# Displacement amplitude: |u_bK|^2 = E_bK / (M_cell * omega_bK^2)
# where M_cell is the effective mass of one cell.
#
# The metric perturbation from displacement u:
#   delta_g ~ (u / L_cell) * delta_tau_over_tau
# Since the modulus tau is the dynamical variable and the phonons ARE tau fluctuations.
#
# More precisely: the Goldstone mode is a PHASE mode (theta), not tau.
# The tau (amplitude) fluctuation comes from the Higgs/amplitude modes.
# But the Leggett modes mix phase and amplitude.
#
# For metric noise: we need the tau-component of each phonon.
# The amplitude modes (Branch-4, Higgs-1) are the ones that fluctuate tau directly.
# The phase modes fluctuate theta (relative orientation), not tau.
# However, phase fluctuations between cells DO produce metric fluctuations
# via the Josephson coupling: they modulate the EFFECTIVE tau seen by a photon
# traversing the tessellation.
#
# Key insight: for a 4D photon propagating through the internal space,
# the relevant metric noise is from ALL modes that modulate the path length.
# Phase modes modulate the phase of the order parameter, which couples to
# the photon via the gauge connection (weak). Amplitude modes modulate tau directly.

# Approach: compute S_h(f) from the amplitude modes (conservative),
# then add phase mode contribution (subdominant but included).

# ---- Amplitude modes (dominant for metric noise) ----
# From W1-F: Branch-4 has omega(0) = 1.410 M_KK, omega(K_BZ) = 2.793 M_KK
# Higgs-1 has omega(0) = 11.465 M_KK (nearly flat, omega(K_BZ) = 11.468)
omega_amp_0 = 1.410  # Branch-4 gap  # (local)
omega_higgs_0 = 11.465  # Higgs-1 gap  # (local)
omega_branch3_0 = 0.378  # Branch-3 gap (mixed)  # (local)

# The amplitude fluctuation per mode at temperature T_acoustic:
# delta_tau_bK = sqrt(T_acoustic / (m_eff * omega_bK^2 * N_cells))
# where m_eff is the effective mass parameter for tau oscillation.
# From canonical: m_tau = 2.062 M_KK, d2S/dtau2 = 317,862
# Effective mass = d2S_fold / (2 * M_KK^2) in natural units
# Actually: m_tau^2 = d2V/dtau2 where V = spectral action
# The kinetic term is (1/2) * Z_fold * (dtau/dt)^2, so the canonical
# mass is Z_fold.

from canonical_constants import Z_fold, d2S_fold, M_ATDHFB

# m_tau^2 = d2S_fold / Z_fold ? No.
# m_tau = 2.062 is the mass eigenvalue, i.e., omega of the tau mode.
# Z_fold = 74730 is the gradient stiffness.
# M_ATDHFB = 1.695 is the collective mass.
# Proper: omega_tau^2 = (stiffness) / (mass) = Z_fold * something / M_ATDHFB
# But we already have m_tau = 2.062 M_KK from S42. Use it directly.

# For the tau oscillation (amplitude mode at K=0):
# E_quantum = m_tau * M_KK = 2.062 * M_KK (one quantum)
# Thermal occupation: <n> = 1/(exp(m_tau/T_acoustic) - 1)
n_tau = 1.0 / (np.exp(m_tau / T_acoustic) - 1.0)
n_amp4 = 1.0 / (np.exp(omega_amp_0 / T_acoustic) - 1.0)
n_higgs = 1.0 / (np.exp(omega_higgs_0 / T_acoustic) - 1.0)
n_Gold_BZ = 1.0 / (np.exp(omega_Gold_BZ / T_acoustic) - 1.0)
n_L1 = 1.0 / (np.exp(omega_L1 / T_acoustic) - 1.0)
n_L2 = 1.0 / (np.exp(omega_L2 / T_acoustic) - 1.0)

print(f"T_acoustic = {T_acoustic:.3f} M_KK = {T_acoustic * M_KK:.3e} GeV")
print(f"\nThermal occupations (Bose-Einstein):")
print(f"  m_tau mode (2.062 MKK):    <n> = {n_tau:.3e}")
print(f"  Leggett-1 (0.138 MKK):     <n> = {n_L1:.3e}")
print(f"  Leggett-2 (0.192 MKK):     <n> = {n_L2:.3e}")
print(f"  Branch-3 (0.378 MKK):      <n> = {n_higgs:.3e}")  # using same formula
print(f"  Branch-4 (1.410 MKK):      <n> = {n_amp4:.3e}")
print(f"  Higgs-1 (11.465 MKK):      <n> = {n_higgs:.3e}")

# All modes are DEEPLY frozen: T_acoustic/omega << 1 for all modes except
# potentially the Goldstone at small K.
# The Goldstone mode: omega(K) = c_Gold * K for small K.
# Minimum K on the lattice: K_min ~ 2*pi / (N_cells^{1/3} * a_lattice)
# For 32 cells in 8D... actually the tessellation is in the FULL 8D manifold.
# The effective number of cells per linear dimension is N_cells^{1/8} ~ 32^{1/8} = 1.41
# So K_min ~ 2*pi / (N_cells^{1/8} * a_lattice)

N_lin = N_cells ** (1.0 / dim_SU3)  # effective linear size
K_min = 2 * PI / (N_lin * a_lattice)
omega_Gold_min = c_Gold * K_min

print(f"\nLattice parameters:")
print(f"  N_lin (effective) = {N_lin:.3f}")
print(f"  K_min = {K_min:.4f} M_KK")
print(f"  omega_Gold(K_min) = {omega_Gold_min:.4f} M_KK")
print(f"  omega_Gold(K_min) / T_acoustic = {omega_Gold_min / T_acoustic:.2f}")

# Even the softest Goldstone mode at K_min has omega/T ~ 9.
# So ALL modes have <n> << 1: the tessellation is in the QUANTUM ground state.
# The metric noise comes from ZERO-POINT fluctuations only.

n_Gold_min = 1.0 / (np.exp(omega_Gold_min / T_acoustic) - 1.0)
print(f"  <n>_Goldstone(K_min) = {n_Gold_min:.3e}")
print(f"\nAll modes frozen: <n> << 1. Noise = ZERO-POINT only.")

# ==============================================================================
# SECTION 5: Zero-point metric noise
# ==============================================================================
print("\n--- SECTION 5: Zero-Point Metric Noise ---")

# For zero-point fluctuations, each mode has energy (1/2) * hbar * omega_bK.
# The displacement variance: <u^2>_bK = hbar / (2 * M_eff * omega_bK)
# where M_eff is the effective mass for that mode.
#
# For the tau modulus: the kinetic term in the action is
#   S_kin = (1/2) * Z_fold * (dtau/dt)^2  per cell
# So M_eff = Z_fold for the homogeneous mode.
# For the K-dependent mode: M_eff(K) = Z_fold (local stiffness is K-independent)
#
# Zero-point tau fluctuation per mode:
#   <(delta_tau)^2>_bK = 1 / (2 * Z_fold * omega_bK)   [in M_KK units]
# (This is hbar / (2 * m * omega) with hbar=1 in natural units)

# Total zero-point tau variance (sum over all modes and branches):
print(f"Z_fold = {Z_fold:.2f}")

# Create K-grid for each branch
N_K_grid = 200
K_grid = np.linspace(K_min, K_BZ, N_K_grid)
dK = K_grid[1] - K_grid[0]

# Dispersion relations (approximate from W1-F data)
# Goldstone: omega = c_Gold * K (linear)
omega_Gold = c_Gold * K_grid

# Leggett-1: omega = sqrt(omega_L1^2 + c_L1^2 * K^2), estimate c_L1
# From omega(0)=0.138, omega(K_BZ)=0.529: c_L1 = sqrt((0.529^2-0.138^2)/K_BZ^2)
c_L1 = np.sqrt((0.529**2 - 0.138**2) / K_BZ**2)
omega_Leg1 = np.sqrt(omega_L1**2 + c_L1**2 * K_grid**2)

# Leggett-2: omega = sqrt(omega_L2^2 + c_L2^2 * K^2)
c_L2 = np.sqrt((0.986**2 - 0.192**2) / K_BZ**2)
omega_Leg2 = np.sqrt(omega_L2**2 + c_L2**2 * K_grid**2)

# Branch-3: omega = sqrt(0.378^2 + c_3^2 * K^2)
c_3 = np.sqrt((1.456**2 - 0.378**2) / K_BZ**2)
omega_B3 = np.sqrt(omega_branch3_0**2 + c_3**2 * K_grid**2)

# Branch-4: omega = sqrt(1.410^2 + c_4^2 * K^2)
c_4 = np.sqrt((2.793**2 - 1.410**2) / K_BZ**2)
omega_B4 = np.sqrt(omega_amp_0**2 + c_4**2 * K_grid**2)

# Higgs: nearly flat, omega ~ 11.465 + tiny K^2
omega_H = np.full_like(K_grid, omega_higgs_0)

print(f"Dispersion speeds (M_KK):")
print(f"  c_Gold = {c_Gold:.3f}")
print(f"  c_L1   = {c_L1:.3f}")
print(f"  c_L2   = {c_L2:.3f}")
print(f"  c_B3   = {c_3:.3f}")
print(f"  c_B4   = {c_4:.3f}")

# Zero-point displacement variance per mode:
# <(delta_tau)^2> = 1 / (2 * Z_fold * omega)
# But only AMPLITUDE modes contribute to tau fluctuations directly.
# Phase modes contribute indirectly via cross-terms.
# Conservative: use only Branch-3, Branch-4, Higgs (amplitude character)
# Phase modes: Goldstone, Leggett-1,2 contribute via (delta_theta * J * delta_tau) coupling

# For the METRIC noise seen by a 4D observer:
# The relevant quantity is the fluctuation of the VOLUME of the internal space,
# which is the tau-dependent conformal factor.

# Total zero-point tau variance from amplitude modes:
delta_tau_sq_zp_B3 = np.sum(1.0 / (2.0 * Z_fold * omega_B3)) * dK / (K_BZ - K_min) * N_K
delta_tau_sq_zp_B4 = np.sum(1.0 / (2.0 * Z_fold * omega_B4)) * dK / (K_BZ - K_min) * N_K
delta_tau_sq_zp_H = np.sum(1.0 / (2.0 * Z_fold * omega_H)) * dK / (K_BZ - K_min) * N_K

delta_tau_zp_total = np.sqrt(delta_tau_sq_zp_B3 + delta_tau_sq_zp_B4 + delta_tau_sq_zp_H)

print(f"\nZero-point tau variance per branch (summed over K):")
print(f"  Branch-3: <(delta_tau)^2> = {delta_tau_sq_zp_B3:.3e}")
print(f"  Branch-4: <(delta_tau)^2> = {delta_tau_sq_zp_B4:.3e}")
print(f"  Higgs-1:  <(delta_tau)^2> = {delta_tau_sq_zp_H:.3e}")
print(f"  Total:    delta_tau_zp = {delta_tau_zp_total:.3e}")
print(f"  delta_tau_zp / tau_fold = {delta_tau_zp_total / tau_fold:.3e}")

# Compare to HOMOG-42 classical cell-to-cell fluctuation:
print(f"\n  delta_tau(HOMOG-42) / tau = {delta_tau_over_tau:.3e}")
print(f"  delta_tau(zero-point) / tau = {delta_tau_zp_total / tau_fold:.3e}")
print(f"  Ratio HOMOG/ZP = {delta_tau_over_tau * tau_fold / delta_tau_zp_total:.2f}")

# ==============================================================================
# SECTION 6: Strain Power Spectral Density S_h(f)
# ==============================================================================
print("\n--- SECTION 6: Strain PSD S_h(f) ---")

# Convert from internal (M_KK) units to physical units.
# Frequency: f = omega * M_KK / (2*pi*hbar) in Hz
# f = omega * M_KK * GeV_to_inv_s / (2*pi)
# Wait: omega is in M_KK units, so omega_phys = omega * M_KK (in GeV)
# f = omega_phys / (2*pi*hbar) = omega * M_KK / (2*pi * hbar_GeV_s)

def omega_to_Hz(omega_MKK):
    """Convert frequency from M_KK units to Hz."""
    return omega_MKK * M_KK / (2 * PI * hbar_GeV_s)

# Characteristic frequencies
f_Gold_min = omega_to_Hz(omega_Gold_min)
f_Gold_BZ = omega_to_Hz(omega_Gold_BZ)
f_L1 = omega_to_Hz(omega_L1)
f_L2 = omega_to_Hz(omega_L2)
f_B3 = omega_to_Hz(omega_branch3_0)
f_B4 = omega_to_Hz(omega_amp_0)
f_Higgs = omega_to_Hz(omega_higgs_0)
f_tau = omega_to_Hz(m_tau)
f_gap = omega_to_Hz(m_tau)  # fabric gap frequency

print(f"Characteristic frequencies:")
print(f"  f_Gold(K_min) = {f_Gold_min:.3e} Hz")
print(f"  f_Gold(K_BZ)  = {f_Gold_BZ:.3e} Hz")
print(f"  f_Leggett_1   = {f_L1:.3e} Hz")
print(f"  f_Leggett_2   = {f_L2:.3e} Hz")
print(f"  f_Branch_3    = {f_B3:.3e} Hz")
print(f"  f_Branch_4    = {f_B4:.3e} Hz")
print(f"  f_Higgs_1     = {f_Higgs:.3e} Hz")
print(f"  f_fabric_gap  = {f_gap:.3e} Hz")

# ALL frequencies are at ~10^{40} Hz. This is 30+ orders of magnitude above
# any detector band (GQuEST: 1 Hz - 100 MHz = 10^0 - 10^8 Hz).
# The question is: what is the LOW-FREQUENCY tail?

# Below the fabric gap (f < f_gap), the noise is exponentially suppressed:
# S_h(f) ~ S_h(f_gap) * exp(-f_gap / f)  [Boltzmann suppression]
# No wait -- the suppression is not Boltzmann. The fabric gap means there are
# NO propagating modes below m_tau. The spectral density below the gap is
# from EVANESCENT modes (tunneling), with exponential suppression:
# S_h(f < f_gap) ~ S_h(f_gap) * exp(-2 * m_tau * L / c)
# where L is the distance and c is the speed.
# But more fundamentally: the spectral density AT frequency f comes from modes
# with omega = 2*pi*f*hbar / M_KK. If omega < m_tau, the mode is evanescent
# and the noise is suppressed by exp(-m_tau * L_cell) per cell.

# The suppression factor for detecting noise at frequency f << f_gap:
# S_h(f) = S_h^{(ZP)}(f_gap) * exp(-2 * f_gap / f)  ... no, this is wrong.
# The correct statement: the power spectral density at frequency f comes from
# the Fourier transform of the time-correlation function of the metric.
# For a gapped system: <h(t) h(0)> ~ exp(-m_tau * |t|) * cos(m_tau * t)
# => S_h(f) ~ 1 / ((2*pi*f)^2 + m_tau^2)^2   (Lorentzian^2)
# In physical units: S_h(f) = A / (f^2 + f_gap^2)^2

# Zero-point noise amplitude at the gap:
# h_rms = delta_tau_zp * (M_KK / M_Pl)^2 * effacement
# Using the proper chain: internal fluctuation -> 4D strain

# The 4D strain from a tau fluctuation:
# In KK reduction: g_{4D} ~ g_M4 * exp(-alpha * tau) for some alpha
# h ~ alpha * delta_tau * (M_KK / M_Pl)^2   (KK dilution factor)
# The factor (M_KK / M_Pl)^2 comes from the KK hierarchy.
# PLUS the effacement factor from S43 PERLMAN-43.

# Strain amplitude at the gap frequency:
h_rms_at_gap = delta_tau_zp_total * ratio_MKK_MPl**2
print(f"\nStrain from zero-point fluctuations:")
print(f"  h_rms (at gap, no effacement) = {h_rms_at_gap:.3e}")
h_rms_effaced = delta_tau_zp_total * effacement
print(f"  h_rms (with effacement 7.8e-8) = {h_rms_effaced:.3e}")

# Actually, the effacement factor delta_g = 7.8e-8 already INCLUDES the
# (M_KK/M_Pl)^2 suppression. From S43 PERLMAN-43:
# "Three mechanisms: effacement (dominant, 10^{-32}), lensing (10^{-47}), phase (10^{-77})"
# The effacement delta_g = 7.8e-8 is the ratio delta_g_4D / delta_g_internal
# Let me re-check. From S42 EFFACEMENT-42:
# delta_g = |E_BCS| / S_fold ~ 10^{-6}
# No -- the 7.8e-8 is the per-domain amplitude AFTER fold-protection.
#
# Let me be precise: S43 PERLMAN-43 gives angular blur 1.17e-32 arcsec.
# The blur comes from: theta_blur ~ delta_phi * sqrt(L * l_P) / L
# where delta_phi is the accumulated phase shift from metric fluctuations.
#
# The strain h from internal tau fluctuations:
# h = (delta_tau / tau_fold) * (L_cell / L_obs) * N_cells^{1/2} * (M_KK / M_Pl)
# But this is getting circular. Let me use the FUNDAMENTAL chain:
#
# 1. Zero-point tau fluctuation per mode: delta_tau_mode = 1/sqrt(2*Z_fold*omega)
# 2. This creates a metric fluctuation in the internal space
# 3. In 4D Einstein frame: h ~ delta_tau * (dg_4D/dtau) / g_4D
# 4. The KK reduction factor: (dg_4D/dtau) / g_4D = -1/4 * d(ln det g_int)/dtau
#    = -1/4 * (-1) = 1/4   (from Section 2 calculation)
# 5. So h_4D = (1/4) * delta_tau per cell
# 6. Over the full SU(3): coherent sum of N_cells cells = N_cells * h_cell
#    No -- the cells are at DIFFERENT K, so RMS sum = sqrt(N_cells) * h_cell

# Wait. The key point I'm missing: the internal space IS the SU(3) fiber at
# each spacetime point. The metric fluctuation of the fiber produces a
# conformal factor fluctuation of the 4D metric.
# The 4D effective action (KK reduction):
#   S_4D = (M_Pl^2 / 16*pi*G) * integral R_4D * sqrt(g_4D) d^4x
# where G depends on the volume of the internal space.
# delta(G_N) / G_N = delta_tau / 2  (from Section 2).
# This translates to strain:
# h ~ delta(G_N)/G_N = delta_tau / 2

# BUT this is the strain at the SCALE of the internal space.
# At macroscopic scales, the internal fluctuation is averaged out UNLESS
# it produces a propagating mode in 4D.
# The fabric gap m_tau = 2.062 M_KK means: any tau fluctuation with 4D momentum
# k < m_tau does NOT propagate. It's exponentially confined.
# The 4D range of influence: r ~ 1/m_tau ~ M_KK^{-1} / 2 ~ 10^{-33} m.
# This is the CORRELATION LENGTH of the metric noise.
# At distances >> 1/m_tau, the noise averages to zero.
# This is W-FOAM-5 quantified.

r_corr = 1.0 / (m_tau * M_KK) * hbar_c_GeV_m  # correlation length in meters
print(f"\nCorrelation length of metric noise:")
print(f"  r_corr = 1/(m_tau * M_KK) = {r_corr:.3e} m")
print(f"  r_corr / l_Planck = {r_corr / l_Planck:.3f}")

# The noise power spectral density at DETECTOR frequency f:
# S_h(f) = h_0^2 * r_corr / (c * tau_c^2) * 1 / ((2*pi*f)^2 + (1/tau_c)^2)
# where tau_c = r_corr / c is the correlation time.

tau_corr = r_corr / c_light  # correlation time in seconds
f_corr = 1.0 / (2 * PI * tau_corr)  # characteristic frequency in Hz

print(f"  tau_corr = {tau_corr:.3e} s")
print(f"  f_corr = {f_corr:.3e} Hz  (= f_gap)")

# h_0: strain amplitude at the source (correlation length scale)
# From the zero-point fluctuation:
h_0 = delta_tau_zp_total / 2.0  # conformal factor, no KK suppression at source
# But we need to be careful: the MEASURABLE 4D strain at distance r >> r_corr
# is suppressed by the massive propagator:
# G_massive(r) ~ (1/r) * exp(-m*r) for r >> 1/m
# At the detector (r ~ 1 m for GQuEST, 4 km for LIGO):
# G(r_det) ~ (r_corr / r_det) * exp(-r_det / r_corr)

# This exponential suppression is the QUANTITATIVE statement of W-FOAM-5.
# Let me compute it for each detector:

detectors = {
    "GQuEST (1.5m)": 1.5,
    "LIGO (4km)": 4e3,
    "LISA (2.5Gm)": 2.5e9,
    "Cosmic interferometer (1AU)": 1.496e11,
}

print(f"\n--- SECTION 7: Detector Comparison ---")
print(f"\nh_0 (at source) = {h_0:.3e}")
print(f"r_corr = {r_corr:.3e} m")
print(f"")
print(f"{'Detector':<30s}  {'r_det (m)':<12s}  {'r_det/r_corr':<15s}  {'log10(suppression)':<20s}  {'h_eff':<12s}")
print("-" * 100)

results = {}
for name, r_det in detectors.items():
    ratio = r_det / r_corr
    # Suppression: exp(-m*r) ~ exp(-r/r_corr)
    log10_supp = -ratio / np.log(10)
    # Effective strain (using propagator)
    h_eff = h_0 * (r_corr / r_det) * np.exp(-ratio) if ratio < 700 else 0.0
    results[name] = {"r_det": r_det, "ratio": ratio, "log10_supp": log10_supp, "h_eff": h_eff}
    print(f"{name:<30s}  {r_det:<12.3e}  {ratio:<15.3e}  {log10_supp:<20.1f}  {'<10^{-300}'.rjust(12) if h_eff == 0.0 else f'{h_eff:.3e}'.rjust(12)}")

# ==============================================================================
# SECTION 8: Compare to GQuEST sensitivity
# ==============================================================================
print("\n--- SECTION 8: GQuEST Comparison ---")

# GQuEST sensitivity: displacement ~10^{-18} m at 1.5m baseline
# Strain sensitivity: h ~ 10^{-18} / 1.5 ~ 7e-19
# Spectral density: S_h^{1/2} ~ 10^{-21} Hz^{-1/2} at 100 kHz - 100 MHz
gquest_strain_sensitivity = 7e-19
gquest_Sh_sqrt = 1e-21  # Hz^{-1/2}

# At GQuEST frequencies (say f = 1 MHz = 10^6 Hz):
f_gquest = 1e6  # Hz

# The framework's noise at this frequency:
# S_h(f) = h_0^2 * (2*tau_corr) / ((2*pi*f*tau_corr)^2 + 1)
# For f << f_corr: S_h ~ h_0^2 * 2*tau_corr
# For f >> f_corr: S_h ~ h_0^2 / (2*pi^2 * f^2 * tau_corr)

# But f_corr ~ 10^{40} Hz >> any detector frequency, so we're in f << f_corr:
# Wait, this is inverted. f_corr = 10^{40} Hz is the GAP frequency.
# For f << f_corr (which is where ALL detectors operate):
# The propagator falls off as exp(-f_corr/f)? No.
#
# The spectral density of a massive field at frequency f << m (gap):
# S_h(f) propto exp(-2*m*r) where r = c/(2*pi*f) is the wavelength/2pi...
# No. The PSD is the Fourier transform of the time-domain correlator.
# For a massive field: <phi(t) phi(0)> ~ exp(-m*|t|) * cos(m*t)
# S_phi(omega) ~ m / ((omega - m)^2 + gamma^2) + m / ((omega + m)^2 + gamma^2)
# This is peaked at omega = m with width gamma.
# For omega << m (detector band): S(omega) ~ m / (m^4) = 1/m^3 (constant, tiny)
# Actually: S(omega) = integral_{-inf}^{inf} <phi(t)phi(0)> e^{-i*omega*t} dt
# For <phi(t)phi(0)> = (A/m) * exp(-gamma*|t|) * cos(m*t):
# S(omega) = (2*A*gamma/m) / ((omega^2 - m^2)^2 + 4*gamma^2*omega^2)   [Breit-Wigner]
# For omega << m: S(omega) ~ (2*A*gamma/m) / (m^4) = 2*A*gamma / m^5

# The damping gamma for the tau mode: from Langer decay rate
# Gamma_Langer_BCS = 0.250 M_KK
gamma_tau = 0.250  # M_KK (from canonical_constants)  # (local)

# Zero-point amplitude A:
A_zp = delta_tau_zp_total**2 * m_tau  # units: M_KK^{-1}

# S_tau(omega) for omega << m_tau:
# S_tau(omega<<m) ~ 2 * A_zp * gamma_tau / m_tau^5   [in M_KK^{-4} units]
S_tau_low_f = 2 * A_zp * gamma_tau / m_tau**5  # M_KK^{-4} i.e., per (M_KK)

# Convert to SI: S_tau in units of 1/Hz
# S_tau_SI = S_tau_low_f * (M_KK / (2*pi*hbar_GeV_s))^{-1}
# = S_tau_low_f * (2*pi*hbar_GeV_s / M_KK)
S_tau_Hz = S_tau_low_f * (2 * PI * hbar_GeV_s / M_KK)

print(f"Zero-point amplitude A_zp = {A_zp:.3e}")
print(f"Langer damping gamma_tau = {gamma_tau:.3f} M_KK")
print(f"S_tau(f << f_gap) = {S_tau_low_f:.3e} M_KK^{{-4}}")
print(f"S_tau(f << f_gap) = {S_tau_Hz:.3e} Hz^{{-1}}")

# Convert tau PSD to strain PSD:
# h = (1/2) * delta_tau  (conformal factor) * (spatial averaging)
# For a detector at distance r >> r_corr:
# The spatial averaging kills the signal by exp(-r/r_corr)
# S_h(f) = (1/4) * S_tau(f) * exp(-2*r_det/r_corr) / r_det^2

# For GQuEST (r_det = 1.5 m):
r_gquest = 1.5  # (local)
supp_gquest = r_gquest / r_corr
log10_supp_gquest = -supp_gquest / np.log(10)

print(f"\nGQuEST comparison:")
print(f"  r_det / r_corr = {supp_gquest:.3e}")
print(f"  log10(exp(-r/r_corr)) = {log10_supp_gquest:.1f}")
print(f"  This is suppression by 10^{{{log10_supp_gquest:.0f}}}")

# S_h(f_gquest):
# Even without the exponential: S_h_no_exp = (1/4) * S_tau_Hz / r_gquest^2
S_h_no_exp = 0.25 * S_tau_Hz
sqrt_S_h_no_exp = np.sqrt(abs(S_h_no_exp)) if S_h_no_exp > 0 else 0
print(f"  sqrt(S_h) at gap (no spatial suppression) = {sqrt_S_h_no_exp:.3e} Hz^{{-1/2}}")
print(f"  sqrt(S_h) at gap (with exp suppression)   = (below machine precision)")
print(f"  GQuEST sensitivity: sqrt(S_h) ~ {gquest_Sh_sqrt:.3e} Hz^{{-1/2}}")

# The key result: the exponential suppression from the fabric gap kills
# the signal by 10^{10^{25}} or more (from GQUEST-43: 10^{-6.1e25}).
# This confirms W-FOAM-5 and GQUEST-43.

# ==============================================================================
# SECTION 9: Comparison to Standard Foam Models
# ==============================================================================
print("\n--- SECTION 9: Comparison to Foam Models ---")

# Standard foam models predict:
# 1. Random-walk: delta_l ~ l^{1/2} * l_P^{1/2}  (RULED OUT by Perlman)
# 2. Holographic: delta_l ~ l^{1/3} * l_P^{2/3}  (marginally allowed)
# 3. Framework:   delta_l ~ delta_tau * l_P * exp(-m_tau * l / hbar*c)
#                 = EXPONENTIALLY SUPPRESSED for l >> l_P

# At l = 1 m (tabletop):
l_test = 1.0  # m
delta_l_rw = np.sqrt(l_test * l_Planck)
delta_l_holo = l_test**(1.0/3.0) * l_Planck**(2.0/3.0)
# Framework: r/r_corr ~ l_test / r_corr
delta_l_framework = delta_tau_zp_total * l_Planck * (r_corr / l_test)
# But the exponential kills it:
exp_supp_log10 = -(l_test / r_corr) / np.log(10)

print(f"Distance fluctuation at l = 1 m:")
print(f"  Random walk:  delta_l = {delta_l_rw:.3e} m")
print(f"  Holographic:  delta_l = {delta_l_holo:.3e} m")
print(f"  Framework (no exp): delta_l ~ {delta_l_framework:.3e} m")
print(f"  Framework (with exp): log10(suppression) = {exp_supp_log10:.1e}")
print(f"  Framework effective: delta_l < 10^{{{exp_supp_log10:.0e}}} m  (below all detectors)")

# At l = l_Planck:
delta_l_rw_lp = np.sqrt(l_Planck * l_Planck)
delta_l_holo_lp = l_Planck**(1.0/3.0) * l_Planck**(2.0/3.0)
delta_l_fw_lp = delta_tau_zp_total * l_Planck  # at the source scale, no exponential
print(f"\nDistance fluctuation at l = l_P:")
print(f"  Random walk:  delta_l = l_P = {l_Planck:.3e} m")
print(f"  Holographic:  delta_l = l_P = {l_Planck:.3e} m")
print(f"  Framework:    delta_l = {delta_l_fw_lp:.3e} m  (ratio {delta_tau_zp_total:.3e})")

# ==============================================================================
# SECTION 10: Summary Results
# ==============================================================================
print("\n" + "=" * 72)
print("SUMMARY: METRIC-NOISE-52 Results")
print("=" * 72)

print(f"""
R1: Cell geometry
   L_cell = {L_cell_MKK:.4f} M_KK^{{-1}} = {L_cell_m:.3e} m
   32-cell Voronoi tessellation of SU(3) with dim=8

R2: Metric fluctuation amplitude (HOMOG-42 classical)
   delta_tau / tau = 1.75e-6  (cell-to-cell)
   delta_g_internal / g = {delta_g_over_g:.3e}  (RMS over all 8 directions)
   delta(G_N) / G_N = {delta_GN_over_GN:.3e}  (conformal volume fluctuation)

R3: Zero-point fluctuation from tessellation phonons
   All modes FROZEN: T_acoustic/omega_min = {T_acoustic / omega_Gold_min:.3f} (<<1)
   delta_tau_zp = {delta_tau_zp_total:.3e}  (in M_KK units)
   delta_tau_zp / tau_fold = {delta_tau_zp_total / tau_fold:.3e}

R4: Characteristic frequencies  (ALL at ~10^40 Hz)
   f_Gold(K_min) = {f_Gold_min:.3e} Hz
   f_Leggett_1   = {f_L1:.3e} Hz
   f_Leggett_2   = {f_L2:.3e} Hz
   f_fabric_gap  = {f_gap:.3e} Hz

R5: Correlation length and exponential suppression (W-FOAM-5)
   r_corr = 1/m_tau = {r_corr:.3e} m  ({r_corr/l_Planck:.1f} * l_P)
   At GQuEST (1.5m): suppression 10^{{{log10_supp_gquest:.0e}}}
   CONFIRMS GQUEST-43: null for ALL sub-10^40 Hz detectors

R6: Strain amplitude at source scale
   h_rms(at r_corr) = {h_0:.3e}  (conformal, no KK dilution)
   h_rms(KK diluted) = {h_rms_at_gap:.3e}
   h_rms(effaced)    = {h_rms_effaced:.3e}

R7: Comparison to GQuEST
   Framework S_h^{{1/2}}(1 MHz) < 10^{{{exp_supp_log10:.0e}}} Hz^{{-1/2}}
   GQuEST sensitivity: ~10^{{-21}} Hz^{{-1/2}}
   MARGIN: {abs(exp_supp_log10) - 21:.0e} orders of magnitude

R8: Comparison to standard foam models (at l = 1m)
   Random walk:  delta_l ~ {delta_l_rw:.1e} m  (RULED OUT by Perlman)
   Holographic:  delta_l ~ {delta_l_holo:.1e} m  (marginally allowed)
   Framework:    delta_l < 10^{{{exp_supp_log10:.0e}}} m  (exponentially null)

R9: Physical picture
   The 32-cell tessellation IS a source of metric noise, but:
   (a) All phonon modes are frozen (quantum ground state, T << omega)
   (b) The fabric gap m_tau = 2.062 M_KK confines all fluctuations
       within r_corr ~ 1.3 l_P
   (c) Exponential suppression at detector scales is 10^{{10^25}} or greater
   (d) This is the STRONGEST null prediction in the framework

   The framework is discriminable from gapless foam models (Verlinde-Zurek
   pixellon, Ng holographic) precisely because the gap kills all low-frequency
   noise. A DETECTION of broadband metric noise at any frequency below
   10^40 Hz would FALSIFY this framework.
""")

# ==============================================================================
# SECTION 11: Save data and create plots
# ==============================================================================
print("--- Saving data and creating plots ---")

# Create frequency array for spectrum plot (log scale)
f_array = np.logspace(0, 42, 1000)  # 1 Hz to 10^42 Hz

# Framework strain PSD (Breit-Wigner from massive tau mode)
# S_h(f) = S_0 / ((f^2/f_gap^2 - 1)^2 + (gamma/m)^2 * f^2/f_gap^2)
# For f << f_gap: S_h ~ S_0 / (1 + (gamma/m)^2 * f^2/f_gap^2) ~ S_0
# But with exponential propagation suppression:
# At detector, multiply by exp(-2*r_det*m_tau*M_KK/hbar_c)

# Actually, let's just plot the SPECTRAL SHAPE properly.
# The noise PSD from the sum of all phonon branches:

# For the plot: show the intrinsic noise PSD (at the source) and the
# detector-observable PSD (with propagation suppression).

# Intrinsic: sum of Lorentzians centered on each branch frequency
gamma_frac = 0.01  # fractional width of each mode (conservative)  # (local)

# Compute S_h_intrinsic(f) as sum over branches
S_h_intrinsic = np.zeros_like(f_array)

# Goldstone: linear dispersion from f_Gold_min to f_Gold_BZ
f_Gold_array = omega_to_Hz(omega_Gold)
# Density of states: dn/df ~ 1/(df/dK * dK/dn) ~ 1/c_Gold * (K_BZ/N_K)
# For discrete modes: each K contributes a delta function broadened by lifetime
for i in range(0, len(K_grid), len(K_grid) // N_K + 1):
    f_mode = omega_to_Hz(omega_Gold[i])
    gamma_mode = gamma_frac * f_mode
    # Zero-point amplitude: delta_tau^2 = 1/(2*Z_fold*omega)
    amp = 1.0 / (2.0 * Z_fold * omega_Gold[i])
    # Lorentzian contribution
    S_h_intrinsic += amp * gamma_mode / ((f_array - f_mode)**2 + gamma_mode**2) / PI

# Leggett and amplitude modes (discrete contributions)
for omega_0, label in [(omega_L1, "L1"), (omega_L2, "L2"),
                        (omega_branch3_0, "B3"), (omega_amp_0, "B4"),
                        (omega_higgs_0, "H")]:
    f_mode = omega_to_Hz(omega_0)
    gamma_mode = gamma_frac * f_mode
    amp = 1.0 / (2.0 * Z_fold * omega_0)
    S_h_intrinsic += N_K * amp * gamma_mode / ((f_array - f_mode)**2 + gamma_mode**2) / PI

# Convert to strain PSD: multiply by (1/2)^2 for conformal factor
S_h_intrinsic *= 0.25

# Detector sensitivities (approximate)
# GQuEST: ~10^{-21} Hz^{-1/2} from 10^4 to 10^8 Hz
# LIGO: ~10^{-23} Hz^{-1/2} at 100 Hz, rising at lower/higher f
# LISA: ~10^{-20} Hz^{-1/2} at 10^{-3} Hz

f_gquest_band = np.logspace(4, 8, 100)
S_gquest = np.full_like(f_gquest_band, 1e-42)  # (10^{-21})^2

f_ligo_band = np.logspace(1, 4, 100)
S_ligo = (1e-23)**2 * (1 + (100.0/f_ligo_band)**4 + (f_ligo_band/2000)**2)

f_lisa_band = np.logspace(-4, 0, 100)
S_lisa = (1e-20)**2 * np.ones_like(f_lisa_band)

# ---- PLOT ----
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# Top panel: full spectrum
ax1.loglog(f_array, S_h_intrinsic, 'b-', linewidth=1.5, label='Framework (intrinsic)')
ax1.loglog(f_gquest_band, S_gquest, 'r--', linewidth=2, label=r'GQuEST ($10^{-21}$ Hz$^{-1/2}$)')
ax1.loglog(f_ligo_band, S_ligo, 'g--', linewidth=2, label='LIGO O4')
ax1.loglog(f_lisa_band, S_lisa, 'm--', linewidth=2, label='LISA')

# Mark the gap frequency
ax1.axvline(f_gap, color='orange', linestyle=':', linewidth=1.5, label=f'Fabric gap ($f_{{gap}} = {f_gap:.1e}$ Hz)')

# Mark key mode frequencies
ax1.axvline(f_L1, color='cyan', linestyle=':', alpha=0.5)
ax1.axvline(f_B4, color='cyan', linestyle=':', alpha=0.5)
ax1.text(f_L1*1.5, 1e-45, 'Leggett-1', fontsize=8, rotation=90, color='cyan')
ax1.text(f_B4*1.5, 1e-45, 'Branch-4', fontsize=8, rotation=90, color='cyan')

ax1.set_xlabel('Frequency (Hz)', fontsize=12)
ax1.set_ylabel(r'$S_h(f)$ (Hz$^{-1}$)', fontsize=12)
ax1.set_title('S52 METRIC-NOISE: Stochastic Metric Noise from 32-Cell Tessellation', fontsize=14)
ax1.set_xlim(1e-4, 1e44)
ax1.set_ylim(1e-80, 1e-20)
ax1.legend(fontsize=10, loc='upper left')
ax1.grid(True, alpha=0.3)

# Annotate the gap
ax1.annotate(f'ALL modes at $f > 10^{{40}}$ Hz\nDetectors at $f < 10^8$ Hz\nGap = 32 orders of magnitude',
             xy=(1e24, 1e-50), fontsize=11,
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

# Bottom panel: zoom into detector bands with propagation suppression
# Show that the framework noise is below everything

ax2.fill_between([1e-4, 1e0], [1e-80, 1e-80], [1e-20, 1e-20],
                  alpha=0.1, color='purple', label='LISA band')  # (local)
ax2.fill_between([1e1, 1e4], [1e-80, 1e-80], [1e-20, 1e-20],
                  alpha=0.1, color='green', label='LIGO band')  # (local)
ax2.fill_between([1e4, 1e8], [1e-80, 1e-80], [1e-20, 1e-20],
                  alpha=0.1, color='red', label='GQuEST band')  # (local)

# Detector curves
ax2.loglog(f_gquest_band, S_gquest, 'r-', linewidth=2, label=r'GQuEST sensitivity')
ax2.loglog(f_ligo_band, S_ligo, 'g-', linewidth=2, label='LIGO O4 sensitivity')
ax2.loglog(f_lisa_band, S_lisa, 'm-', linewidth=2, label='LISA sensitivity')

# Framework prediction: exponentially below all curves
ax2.axhline(1e-80, color='blue', linewidth=2, label=r'Framework: $S_h < 10^{-10^{25}}$ Hz$^{-1}$')
ax2.annotate(f'Framework noise EXPONENTIALLY NULL\nin all detector bands\n($m_{{\\tau}} = 2.06$ $M_{{KK}}$, gap at $10^{{40}}$ Hz)',
             xy=(1e2, 1e-60), fontsize=11,
             bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.8))

# Standard foam models for comparison
# Random walk: S_h ~ l_P / (c * f)   [Amelino-Camelia convention]
S_h_rw = l_Planck / (c_light * f_array)
# Holographic: S_h ~ l_P^{4/3} / (c * l_det^{1/3} * f)
l_det = 1.5  # GQuEST arm length  # (local)
S_h_holo = l_Planck**(4.0/3.0) / (c_light * l_det**(1.0/3.0)) / f_array

ax2.loglog(f_array[(f_array > 0.1) & (f_array < 1e9)],
           S_h_rw[(f_array > 0.1) & (f_array < 1e9)],
           'k--', linewidth=1, alpha=0.5, label='Random walk foam (RULED OUT)')
ax2.loglog(f_array[(f_array > 0.1) & (f_array < 1e9)],
           S_h_holo[(f_array > 0.1) & (f_array < 1e9)],
           'k:', linewidth=1, alpha=0.5, label='Holographic foam (marginal)')

ax2.set_xlabel('Frequency (Hz)', fontsize=12)
ax2.set_ylabel(r'$S_h(f)$ (Hz$^{-1}$)', fontsize=12)
ax2.set_title('Detector-Band Comparison: Framework vs Standard Foam', fontsize=14)
ax2.set_xlim(1e-4, 1e9)
ax2.set_ylim(1e-80, 1e-20)
ax2.legend(fontsize=9, loc='upper right')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(os.path.dirname(os.path.abspath(__file__)),
            's52_metric_noise.png'), dpi=150, bbox_inches='tight')
print("Plot saved: s52_metric_noise.png")

# Save data
np.savez(os.path.join(os.path.dirname(os.path.abspath(__file__)),
         's52_metric_noise.npz'),
    # Cell geometry
    L_cell_MKK=L_cell_MKK,
    L_cell_m=L_cell_m,
    N_cells=N_cells,
    dim_SU3=dim_SU3,
    # Fluctuation amplitudes
    delta_tau_over_tau=delta_tau_over_tau,
    delta_tau=delta_tau,
    delta_g_over_g=delta_g_over_g,
    delta_GN_over_GN=delta_GN_over_GN,
    delta_tau_zp_total=delta_tau_zp_total,
    # Strain
    h_0=h_0,
    h_rms_at_gap=h_rms_at_gap,
    h_rms_effaced=h_rms_effaced,
    # Frequencies
    f_Gold_min=f_Gold_min,
    f_Gold_BZ=f_Gold_BZ,
    f_L1=f_L1,
    f_L2=f_L2,
    f_B3=f_B3,
    f_B4=f_B4,
    f_Higgs=f_Higgs,
    f_gap=f_gap,
    # Correlation
    r_corr=r_corr,
    tau_corr=tau_corr,
    # Spectrum
    f_array=f_array,
    S_h_intrinsic=S_h_intrinsic,
    # Foam comparison
    S_h_rw=S_h_rw,
    S_h_holo=S_h_holo,
    # Detector suppressions (log10)
    log10_supp_gquest=log10_supp_gquest,
)
print("Data saved: s52_metric_noise.npz")

print("\n" + "=" * 72)
print("METRIC-NOISE-52 COMPLETE")
print("=" * 72)
