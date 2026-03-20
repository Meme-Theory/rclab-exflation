#!/usr/bin/env python3
"""
s48_qtheory_goldstone.py — Q-Theory Goldstone Self-Tuning Mass
==============================================================

Session 48, Wave 2-C (Volovik agent)
Gate: Q-THEORY-GOLD-48

Computes the Goldstone boson mass from THREE independent routes:
  A: Q-theory self-tuning (BCS gap modulation by phase fluctuations)
  B: Disordered-direction effective mass (Ising-like correlation length)
  C: Dimensional crossover (finite-size mass from transverse confinement)

Each route is grounded in Volovik's q-theory framework (Papers 15-16, 35):
  - The equilibrium condition d(rho_vac)/dq = 0 determines masses
  - The microscopic Hamiltonian is BCS on SU(3) with known spectrum
  - Topological classification: 3He-B class, N_3 = 0, fully gapped

Inputs:
  - s46_qtheory_selfconsistent.npz (q-theory crossing data)
  - s47_rhos_tensor.npz (superfluid stiffness tensor)
  - s47_texture_corr.npz (Josephson couplings, T_acoustic)
  - canonical_constants.py (all constants)
"""

import sys
sys.path.insert(0, '.')
import numpy as np
from canonical_constants import (
    E_cond, tau_fold, M_KK, M_KK_gravity, M_KK_kerner,
    Delta_0_GL, Delta_B3, N_cells, xi_GL, xi_BCS,
    a0_fold, a2_fold, a4_fold, S_fold,
    rho_Lambda_obs, M_Pl_reduced, PI,
    hbar_c_GeV_m, Mpc_to_m, omega_PV,
    E_B1, E_B2_mean, E_B3_mean,
    rho_B2_per_mode, M_max_thouless,
    N_dof_BCS, E_cond_ED_8mode,
)

# ============================================================
# Load upstream data
# ============================================================

d_s46 = np.load('s46_qtheory_selfconsistent.npz', allow_pickle=True)
d_rhos = np.load('s47_rhos_tensor.npz', allow_pickle=True)
d_tex = np.load('s47_texture_corr.npz', allow_pickle=True)

# Q-theory data
V_mat_raw = d_s46['V_mat_raw']
V_mat_constrained = d_s46['V_mat_constrained']
alpha_star = float(d_s46['alpha_star'])
tau_star_flatband = float(d_s46['tau_star_flatband_s46'])
Delta_B2_fold = float(d_s46['Delta_B2_fold'])
Delta_B1_fold = float(d_s46['Delta_B1_fold'])
Delta_B3_fold = float(d_s46['Delta_B3_fold'])

# Superfluid stiffness (diagonal at fold)
rho_s_diag = d_rhos['rho_s_diag_fold']  # shape (8,)
rho_s_eigs = d_rhos['rho_s_eigs_fold']  # shape (8,)
anisotropy = float(d_rhos['anisotropy_fold'])

# Texture/Josephson data
J_C2 = float(d_tex['J_C2'])         # 0.933
J_su2 = float(d_tex['J_su2'])       # 0.059
J_u1 = float(d_tex['J_u1'])         # 0.038
T_acoustic = float(d_tex['T_acoustic'])  # 0.112
l_cell = float(d_tex['l_cell'])      # 0.152 M_KK^{-1}
phi_rms_C2 = float(d_tex['phi_rms_C2_acoustic'])

# Derived quantities
rho_s_C2 = float(np.mean(rho_s_diag[3:7]))  # C^2 block: 7.962
rho_s_su2 = float(np.mean(rho_s_diag[0:3]))  # su(2) block: ~0.505
rho_s_u1 = float(rho_s_diag[7])              # u(1): 0.327
rho_s_avg = float(np.mean(rho_s_diag))

print("=" * 78)
print("Q-THEORY GOLDSTONE SELF-TUNING MASS — S48 W2-C")
print("=" * 78)

print("\n=== INPUT PARAMETERS ===")
print(f"  J_C2 = {J_C2:.6f}  (M_KK)")
print(f"  J_su2 = {J_su2:.6f}  (M_KK)")
print(f"  J_u1 = {J_u1:.6f}  (M_KK)")
print(f"  T_acoustic = {T_acoustic:.6f}  (M_KK)")
print(f"  rho_s(C^2) = {rho_s_C2:.6f}  (M_KK)")
print(f"  rho_s(su2) = {rho_s_su2:.6f}  (M_KK)")
print(f"  rho_s(u1) = {rho_s_u1:.6f}  (M_KK)")
print(f"  |E_cond| = {abs(E_cond):.6f}  (M_KK)")
print(f"  Delta_B2 = {Delta_B2_fold:.6f}  (M_KK)")
print(f"  Delta_B1 = {Delta_B1_fold:.6f}  (M_KK)")
print(f"  Delta_B3 = {Delta_B3_fold:.6f}  (M_KK)")
print(f"  l_cell = {l_cell:.6f}  (M_KK^{{-1}})")
print(f"  N_cells = {N_cells}")
print(f"  phi_rms(C^2) = {phi_rms_C2:.6f}  rad")
print(f"  M_KK(gravity) = {M_KK_gravity:.4e}  GeV")
print(f"  M_KK(Kerner) = {M_KK_kerner:.4e}  GeV")

# Target mass from S47 texture-framework analysis
# n_s = 0.965 requires m such that K^2/(K^2 + m^2/rho_s) = K^{-2+alpha}
# with alpha = 2(1 - n_s) = 0.070, giving m^2/rho_s that maps to particular m
# The S47 estimate: m ~ 3.2e-56 M_KK
# More careful: from ANISO-OZ-48 (Wave 2-A), n_s = 0.965 requires
# m_required such that P(K) ~ K^{-(2-alpha)} with alpha from mass gap
m_required_MKK = 3.2e-56  # M_KK units (S47 W5 estimate)
m_required_GeV = m_required_MKK * M_KK  # GeV

print(f"\n=== TARGET MASS ===")
print(f"  m_required / M_KK = {m_required_MKK:.2e}")
print(f"  m_required (GeV) = {m_required_GeV:.2e}")


# ============================================================
# ROUTE A: Q-Theory Self-Tuning (Volovik Mechanism)
# ============================================================
#
# The vacuum energy includes the Goldstone sector:
#   rho_vac(tau, m) = E_spectral(tau) + E_BCS(tau; m) + E_Goldstone(m)
#
# E_BCS depends on m because phase fluctuations modulate the BCS gap:
#   Delta_eff = Delta_0 * <cos(phi)> ~ Delta_0 * (1 - <phi^2>/2)
#   E_BCS(m) = E_cond * [1 - <phi^2>/2 + ...]^2
#            ~ E_cond * [1 - <phi^2> + ...]
#
# The phase fluctuations in 3D with mass m and stiffness rho_s:
#   <phi^2> = (T / rho_s) * sum_K 1/(K^2 + m^2/rho_s)
#           = (T / (4*pi^2 * rho_s)) * integral d^3K / (K^2 + m^2/rho_s)
#
# For a lattice with d ordered directions and N_cells cells:
#   <phi^2> = (T / rho_s) * sum_{n=1}^{N_max} g_n / (K_n^2 + m^2/rho_s)
#
# The Goldstone kinetic energy:
#   E_Gold = (1/2) * rho_s * <(grad phi)^2> = (T/2) * N_ordered_modes
#           (equipartition)
#
# The self-tuning condition (q-theory):
#   d(rho_vac)/d(m^2) = 0
#
# d/d(m^2) [E_BCS(m) + E_Gold(m)] = 0
# d/d(m^2) [E_cond * (1 - <phi^2>) + (1/2) rho_s m^2 <phi^2>] = 0
#
# Note: <phi^2> depends on m through the infrared regulator.
# For the continuum limit in d=4 (4 ordered C^2 directions):
#   <phi^2>_3D = (T/(4*pi^2*rho_s)) * integral_0^{K_max} 4*pi*K^2 dK / (K^2 + mu^2)
#   where mu^2 = m^2/rho_s
#
# But we are NOT in the continuum. The fabric is a 4x4x2 lattice with
# 4 ordered (C^2) and 4 disordered (su2+u1) directions.
# The ordered subspace: d_eff = 4, with L_C2 = 4 cells in each C^2 direction.
#
# For a d-dimensional lattice with L cells per direction:
#   <phi^2> = (T / rho_s) * (1/L^d) * sum_{n != 0} 1/(K_n^2 + mu^2)
#   K_n = 2*pi*n / (L*a), n = (n1,...,nd), not all zero

print("\n" + "=" * 78)
print("ROUTE A: Q-Theory Self-Tuning (BCS Gap Modulation)")
print("=" * 78)

# Lattice parameters for C^2 ordered subspace
d_ordered = 4  # C^2 directions (from rho_s_diag: 4 directions with rho_s ~ 7.96)
L_C2 = 4       # 4 cells in C^2 directions (from 4x4x2 tessellation)
L_dis = 2      # 2 cells in each disordered direction
a = l_cell     # lattice spacing = cell size (M_KK^{-1})

# Generate lattice momenta for d_ordered = 4 dimensions, L = 4
# K_n = 2*pi*n / (L*a), with n_i in {-L/2+1, ..., L/2}
n_max = L_C2 // 2
n_range = np.arange(-n_max + 1, n_max + 1)  # [-1, 0, 1, 2] for L=4
K_unit = 2 * PI / (L_C2 * a)

# Build d-dimensional mode list
from itertools import product
modes_4d = list(product(n_range, repeat=d_ordered))
K_sq_list = []
for mode in modes_4d:
    if all(n == 0 for n in mode):
        continue  # skip zero mode
    K_sq = sum(n**2 for n in mode) * K_unit**2
    K_sq_list.append(K_sq)

K_sq_arr = np.array(K_sq_list)
N_modes = len(K_sq_arr)
print(f"\n  Lattice: d={d_ordered}, L={L_C2}, a={a:.4f} M_KK^{{-1}}")
print(f"  K_unit = 2*pi/(L*a) = {K_unit:.4f} M_KK")
print(f"  N_modes (excluding zero) = {N_modes}")
print(f"  K_sq range: [{K_sq_arr.min():.4f}, {K_sq_arr.max():.4f}] M_KK^2")

# Phase fluctuation as function of mass parameter mu^2 = m^2/rho_s
def phi_sq(mu_sq, K_sq=K_sq_arr, T=T_acoustic, rho_s=rho_s_C2, N_m=N_modes):
    """Mean-square phase fluctuation <phi^2> on the lattice."""
    return (T / rho_s) * (1.0 / (N_m + 1)) * np.sum(1.0 / (K_sq + mu_sq))

def d_phi_sq_d_mu(mu_sq, K_sq=K_sq_arr, T=T_acoustic, rho_s=rho_s_C2, N_m=N_modes):
    """d<phi^2>/d(mu^2) on the lattice."""
    return -(T / rho_s) * (1.0 / (N_m + 1)) * np.sum(1.0 / (K_sq + mu_sq)**2)

# The total vacuum energy from Goldstone + BCS sectors:
# rho_vac(m) = E_cond * (1 - <phi^2>) + (1/2) * rho_s * m^2 * <phi^2>
#
# NOTE: E_cond < 0, so (1 - <phi^2>) REDUCES the magnitude of E_cond.
# The sign matters: rho_vac = E_cond * (1 - <phi^2>) + (1/2)*rho_s*m^2*<phi^2>
#                            = E_cond - E_cond*<phi^2> + (1/2)*rho_s*m^2*<phi^2>
#
# Using mu^2 = m^2/rho_s:
# rho_vac(mu) = E_cond - E_cond * phi_sq(mu) + (1/2) * rho_s^2 * mu^2 * phi_sq(mu)
#
# Self-tuning: d(rho_vac)/d(mu^2) = 0
# => -E_cond * d_phi_sq/d_mu^2 + (1/2)*rho_s^2 * [phi_sq + mu^2 * d_phi_sq/d_mu^2] = 0
# => [-E_cond + (1/2)*rho_s^2*mu^2] * d_phi_sq/d_mu^2 + (1/2)*rho_s^2 * phi_sq = 0
#
# Since d_phi_sq/d_mu^2 < 0 always, and E_cond < 0, we have:
# [|E_cond| + (1/2)*rho_s^2*mu^2] * |d_phi_sq/d_mu^2| = (1/2)*rho_s^2 * phi_sq
#
# Solve for mu^2:
# mu^2 = (rho_s^2 * phi_sq / |d_phi_sq/d_mu^2| - 2*|E_cond|) / rho_s^2
#       = phi_sq / |d_phi_sq/d_mu^2| - 2*|E_cond| / rho_s^2

# Solve self-consistently via iteration
print("\n  --- Self-consistent iteration ---")
mu_sq = 1e-6  # initial guess
E_c = abs(E_cond)
rs = rho_s_C2

converged = False
diverged_4d = False
for iteration in range(200):
    ps = phi_sq(mu_sq)
    dps = d_phi_sq_d_mu(mu_sq)

    mu_sq_new = ps / abs(dps) - 2 * E_c / rs**2

    if mu_sq_new < 0:
        print(f"  iter {iteration}: mu^2_new = {mu_sq_new:.6e} < 0 => NO self-tuning solution")
        break

    if mu_sq_new > 1e10:
        diverged_4d = True
        print(f"  DIVERGES at iteration {iteration}: mu^2 = {mu_sq_new:.6e} (runaway)")
        break

    rel_change = abs(mu_sq_new - mu_sq) / max(abs(mu_sq_new), 1e-30)
    mu_sq = mu_sq_new

    if rel_change < 1e-12:
        converged = True
        print(f"  Converged at iteration {iteration}: mu^2 = {mu_sq:.6e}")
        break

if converged:
    m_sq_A = mu_sq * rs  # m^2 = mu^2 * rho_s
    m_A_MKK = np.sqrt(abs(m_sq_A))
    m_A_GeV = m_A_MKK * M_KK
    ps_final = phi_sq(mu_sq)

    print(f"\n  ROUTE A RESULT:")
    print(f"    mu^2 = m^2/rho_s = {mu_sq:.6e} M_KK^2")
    print(f"    m^2 = {m_sq_A:.6e} M_KK^2")
    print(f"    m = {m_A_MKK:.6e} M_KK")
    print(f"    m = {m_A_GeV:.6e} GeV")
    print(f"    <phi^2> at self-tuning = {ps_final:.6e}")
    print(f"    m / m_required = {m_A_MKK / m_required_MKK:.4e}")
    print(f"    log10(m/M_KK) = {np.log10(m_A_MKK):.4f}")
else:
    # Analyze the failure/divergence
    ps_0 = phi_sq(0.0)
    dps_0 = d_phi_sq_d_mu(0.0)
    ratio_0 = ps_0 / abs(dps_0)
    threshold = 2 * E_c / rs**2

    if diverged_4d:
        print(f"\n  DIVERGENT self-tuning (4D lattice):")
        print(f"    ps/|dps| at mu=0: {ratio_0:.6e}")
        print(f"    2|E_cond|/rho_s^2: {threshold:.6e}")
        print(f"    Ratio: {ratio_0 / threshold:.6e} >> 1 => iteration diverges")
        print(f"    <phi^2> at mu=0: {ps_0:.6e}")
        print(f"    Physical: ps/|dps| grows with mu for discrete lattice.")
        print(f"    The self-tuning equation has NO finite fixed point.")
        print(f"    Solutions: m=0 (Goldstone theorem) or m=inf (frozen phase).")
    else:
        print(f"\n  NO self-tuning solution (4D lattice):")
        print(f"    ps/|dps| at mu=0: {ratio_0:.6e}")
        print(f"    2|E_cond|/rho_s^2: {threshold:.6e}")
        print(f"    <phi^2> at mu=0: {ps_0:.6e}")

    # However, the FABRIC (32 cells) extends the lattice.
    # Recalculate with extended lattice: 32 cells along each ordered direction
    print(f"\n  --- Extended fabric: L={N_cells} cells per C^2 direction ---")
    L_fabric = N_cells  # 32
    K_unit_fab = 2 * PI / (L_fabric * a)
    n_max_fab = L_fabric // 2
    n_range_fab = np.arange(-n_max_fab + 1, n_max_fab + 1)

    # For d=4, L=32: total modes = 32^4 - 1 = 1,048,575
    # Too many to enumerate directly; use a cutoff
    # Actually, the anisotropic tessellation is 4x4x2, not 32^4
    # The 32 cells form a Voronoi tessellation in 8D with N_cells = 32
    # Let's treat it as effectively N_cells modes in 1D for the Goldstone
    # because the fabric connectivity is the relevant topology

    # 1D chain of N_cells:
    print(f"  Using 1D chain model (N_cells = {N_cells}):")
    n_1d = np.arange(1, N_cells)  # modes 1 to N_cells-1
    K_1d = 2 * PI * n_1d / (N_cells * a)
    K_sq_1d = K_1d**2
    N_modes_1d = len(K_sq_1d)

    def phi_sq_1d(mu_sq_1d):
        return (T_acoustic / rho_s_C2) * (1.0 / N_cells) * np.sum(1.0 / (K_sq_1d + mu_sq_1d))

    def d_phi_sq_1d(mu_sq_1d):
        return -(T_acoustic / rho_s_C2) * (1.0 / N_cells) * np.sum(1.0 / (K_sq_1d + mu_sq_1d)**2)

    ps_0_1d = phi_sq_1d(0.0)
    dps_0_1d = d_phi_sq_1d(0.0)
    ratio_0_1d = ps_0_1d / abs(dps_0_1d)

    print(f"    K_min = {K_1d[0]:.6e} M_KK")
    print(f"    K_max = {K_1d[-1]:.6e} M_KK")
    print(f"    N_modes = {N_modes_1d}")
    print(f"    <phi^2>(mu=0) = {ps_0_1d:.6e}")
    print(f"    ps/|dps| at mu=0: {ratio_0_1d:.6e}")
    print(f"    threshold: {threshold:.6e}")
    print(f"    ratio/threshold = {ratio_0_1d / threshold:.6e}")

    # Try self-consistent for 1D chain
    mu_sq_1d_val = 1e-6
    converged_1d = False
    diverged_1d = False
    m_sq_A = 0.0
    m_A_MKK = 0.0
    m_A_GeV = 0.0
    for iteration in range(200):
        ps_v = phi_sq_1d(mu_sq_1d_val)
        dps_v = d_phi_sq_1d(mu_sq_1d_val)
        mu_sq_new_1d = ps_v / abs(dps_v) - 2 * E_c / rs**2

        if mu_sq_new_1d < 0:
            print(f"  1D chain: NO self-tuning at iter {iteration}")
            print(f"    ps/|dps| = {ps_v/abs(dps_v):.6e} < threshold {threshold:.6e}")
            break

        if mu_sq_new_1d > 1e10:
            diverged_1d = True
            print(f"  1D chain: DIVERGES at iter {iteration}, mu^2 = {mu_sq_new_1d:.6e}")
            break

        rel_change = abs(mu_sq_new_1d - mu_sq_1d_val) / max(abs(mu_sq_new_1d), 1e-30)
        mu_sq_1d_val = mu_sq_new_1d
        if rel_change < 1e-12:
            converged_1d = True
            break

    if converged_1d:
        m_sq_A = mu_sq_1d_val * rs
        m_A_MKK = np.sqrt(abs(m_sq_A))
        m_A_GeV = m_A_MKK * M_KK
        ps_final_1d = phi_sq_1d(mu_sq_1d_val)
        print(f"\n  1D CHAIN ROUTE A RESULT:")
        print(f"    mu^2 = {mu_sq_1d_val:.6e} M_KK^2")
        print(f"    m = {m_A_MKK:.6e} M_KK")
        print(f"    m = {m_A_GeV:.6e} GeV")
        print(f"    <phi^2> = {ps_final_1d:.6e}")
        print(f"    m / m_required = {m_A_MKK / m_required_MKK:.4e}")
    elif diverged_1d:
        print(f"\n  ROUTE A: DIVERGES — ps/|dps| > threshold at all mu^2 > 0")
        print(f"  Physical: increasing mass INCREASES BCS energy gain (fewer fluctuations")
        print(f"  deplete the condensate), creating a runaway. No finite self-tuning point.")
        print(f"  The self-tuning condition has solution only at m -> infinity (trivial: frozen phase).")
    else:
        print(f"\n  ROUTE A: FAIL — self-tuning gives m = 0 (both 4D lattice and 1D chain)")

    # Route A alternate: ANALYTIC estimate from Volovik Paper 05
    # In equilibrium, the vacuum energy response to perturbation is:
    #   delta_rho ~ T^2/rho_s (thermal fluctuations)
    # The Goldstone mass squared from equipartition + BCS:
    #   m^2 ~ |E_cond| * T / (rho_s^2 * a^2)
    # (This comes from balancing BCS energy gain from order vs. thermal disruption)

    m_sq_A_analytic = abs(E_cond) * T_acoustic / (rs**2 * a**2)
    m_A_analytic_MKK = np.sqrt(m_sq_A_analytic)
    m_A_analytic_GeV = m_A_analytic_MKK * M_KK

    print(f"\n  --- Route A analytic estimate (Volovik Paper 05) ---")
    print(f"    m^2 ~ |E_cond| * T / (rho_s^2 * a^2)")
    print(f"    m^2 = {m_sq_A_analytic:.6e} M_KK^2")
    print(f"    m = {m_A_analytic_MKK:.6e} M_KK")
    print(f"    m = {m_A_analytic_GeV:.6e} GeV")
    print(f"    log10(m/M_KK) = {np.log10(m_A_analytic_MKK):.4f}")
    print(f"    m / m_required = {m_A_analytic_MKK / m_required_MKK:.4e}")


# ============================================================
# ROUTE B: Disordered-Direction Effective Mass
# ============================================================
#
# The su(2) and u(1) directions are DISORDERED (T/J > 1).
# Phase fluctuations in these directions are massive:
#   xi_dis = a / sqrt(T/J - 1) (correlation length)
#   m_dis = 1/xi_dis
#
# For the C^2 Goldstone, coupling to disordered directions
# introduces an effective mass:
#   m_eff^2 = sum_{dis} (J_dis / a^2) * (T/J_dis - 1)
#           = sum_{dis} (T - J_dis) / a^2

print("\n" + "=" * 78)
print("ROUTE B: Disordered-Direction Effective Mass")
print("=" * 78)

# Temperature-to-coupling ratios
ratio_su2 = T_acoustic / J_su2
ratio_u1 = T_acoustic / J_u1
ratio_C2 = T_acoustic / J_C2

print(f"\n  T/J ratios:")
print(f"    T/J_C2 = {ratio_C2:.4f}  (< 1: ORDERED)")
print(f"    T/J_su2 = {ratio_su2:.4f}  (> 1: DISORDERED)")
print(f"    T/J_u1 = {ratio_u1:.4f}  (> 1: DISORDERED)")

# Correlation lengths in disordered directions
# Ising model: xi = a / sqrt(T/J - 1) for T > J (paramagnetic phase)
xi_su2 = a / np.sqrt(ratio_su2 - 1)
xi_u1 = a / np.sqrt(ratio_u1 - 1)

print(f"\n  Correlation lengths:")
print(f"    xi_su2 = {xi_su2:.6f} M_KK^{{-1}}  ({xi_su2/a:.4f} lattice spacings)")
print(f"    xi_u1 = {xi_u1:.6f} M_KK^{{-1}}  ({xi_u1/a:.4f} lattice spacings)")

# Effective mass from disordered directions
# The C^2 Goldstone sees disordered directions as a mass gap:
# m_B^2 = sum_i (T - J_i) / a^2  for disordered directions i
# There are 3 su(2) directions and 1 u(1) direction (4 total disordered)
n_su2_dirs = 3  # from rho_s_diag: 3 directions with rho_s ~ 0.505
n_u1_dirs = 1   # 1 direction with rho_s ~ 0.327

m_sq_B_su2 = n_su2_dirs * (T_acoustic - J_su2) / a**2
m_sq_B_u1 = n_u1_dirs * (T_acoustic - J_u1) / a**2
m_sq_B = m_sq_B_su2 + m_sq_B_u1

m_B_MKK = np.sqrt(m_sq_B)
m_B_GeV = m_B_MKK * M_KK

print(f"\n  Effective mass from disorder:")
print(f"    m^2_su2 = {n_su2_dirs} * (T - J_su2) / a^2 = {m_sq_B_su2:.6e} M_KK^2")
print(f"    m^2_u1 = {n_u1_dirs} * (T - J_u1) / a^2 = {m_sq_B_u1:.6e} M_KK^2")
print(f"    m^2_total = {m_sq_B:.6e} M_KK^2")
print(f"    m_B = {m_B_MKK:.6e} M_KK")
print(f"    m_B = {m_B_GeV:.6e} GeV")
print(f"    log10(m_B/M_KK) = {np.log10(m_B_MKK):.4f}")
print(f"    m_B / m_required = {m_B_MKK / m_required_MKK:.4e}")

# Cross-check: inverse correlation length
m_B_from_xi = np.sqrt(1.0/xi_su2**2 * n_su2_dirs + 1.0/xi_u1**2 * n_u1_dirs)
print(f"\n  Cross-check (1/xi method):")
print(f"    m = sqrt(3/xi_su2^2 + 1/xi_u1^2) = {m_B_from_xi:.6e} M_KK")
print(f"    Agreement: {m_B_from_xi/m_B_MKK:.6f}")


# ============================================================
# ROUTE C: Dimensional Crossover (Finite-Size Mass)
# ============================================================
#
# The tessellation has different extent in ordered vs. disordered
# directions. In the disordered directions, the effective size is
# L_perp ~ 2 cells (the "2" in the 4x4x2 interpretation).
#
# Below K_cross ~ pi / L_perp, the system crosses over from
# d_eff = 4+4 = 8 dimensions to d_eff = 4 (ordered only).
# This crossover introduces an effective mass:
#   m_C = pi / L_perp = pi / (2*a)

print("\n" + "=" * 78)
print("ROUTE C: Dimensional Crossover (Finite-Size Mass)")
print("=" * 78)

# Two interpretations of "transverse size":
# (1) Physical: 2 cells in each disordered direction
L_perp_2 = 2 * a
m_C1_MKK = PI / L_perp_2
m_C1_GeV = m_C1_MKK * M_KK

# (2) Correlation-length limited: the disordered directions have
# xi_dis << L_eff, so the effective transverse size is xi_dis
# m_C2 ~ pi / xi_dis (the larger mass, from smaller xi)
m_C2_MKK = PI / xi_u1  # u(1) has shortest correlation length
m_C2_GeV = m_C2_MKK * M_KK

# (3) Full extent: all 32 cells form the transverse size
L_full = N_cells * a
m_C3_MKK = PI / L_full
m_C3_GeV = m_C3_MKK * M_KK

print(f"\n  Interpretation 1 (L_perp = 2a):")
print(f"    L_perp = {L_perp_2:.6f} M_KK^{{-1}}")
print(f"    m_C1 = pi/L_perp = {m_C1_MKK:.6e} M_KK")
print(f"    m_C1 = {m_C1_GeV:.6e} GeV")
print(f"    log10(m_C1/M_KK) = {np.log10(m_C1_MKK):.4f}")

print(f"\n  Interpretation 2 (L_perp = xi_u1):")
print(f"    xi_u1 = {xi_u1:.6f} M_KK^{{-1}}")
print(f"    m_C2 = pi/xi_u1 = {m_C2_MKK:.6e} M_KK")
print(f"    m_C2 = {m_C2_GeV:.6e} GeV")
print(f"    log10(m_C2/M_KK) = {np.log10(m_C2_MKK):.4f}")

print(f"\n  Interpretation 3 (L_full = N_cells*a):")
print(f"    L_full = {L_full:.6f} M_KK^{{-1}}")
print(f"    m_C3 = pi/L_full = {m_C3_MKK:.6e} M_KK")
print(f"    m_C3 = {m_C3_GeV:.6e} GeV")
print(f"    log10(m_C3/M_KK) = {np.log10(m_C3_MKK):.4f}")


# ============================================================
# ROUTE A': Refined Analytic — Volovik q-theory with Hubble friction
# ============================================================
#
# From Paper 16 (Klinkhamer-Volovik 2009): the remnant CC in an
# expanding universe is Lambda ~ K^3 / E_Pl^2 where K is the
# characteristic scale of the vacuum sector.
#
# For the Goldstone sector, the characteristic scale is set by
# the BCS gap: K ~ Delta_0^2 (string tension analog).
# The Goldstone mass from q-theory relaxation in an expanding universe:
#   m^2 ~ Lambda / rho_s ~ (Delta_0^6 / M_Pl^2) / rho_s
#
# This is the PHYSICAL mass, not a lattice artifact.

print("\n" + "=" * 78)
print("ROUTE A': Q-Theory Hubble Relaxation (Paper 16 Analog)")
print("=" * 78)

# Using Delta_0 in M_KK units and M_Pl in M_KK units
M_Pl_in_MKK = M_Pl_reduced / M_KK  # = 2.435e18 / 7.43e16 = 32.77
print(f"  M_Pl / M_KK = {M_Pl_in_MKK:.4f}")

# Klinkhamer-Volovik scaling: Lambda ~ K_vac^3 / M_Pl^2
# For our system, K_vac ~ Delta_0^2 (pair condensation scale)
K_vac = Delta_B2_fold**2  # ~ 0.536
Lambda_KV = K_vac**3 / M_Pl_in_MKK**2
m_sq_Ap = Lambda_KV / rho_s_C2
m_Ap_MKK = np.sqrt(abs(m_sq_Ap))
m_Ap_GeV = m_Ap_MKK * M_KK

print(f"  K_vac = Delta_B2^2 = {K_vac:.6f} M_KK^2")
print(f"  Lambda_KV = K_vac^3 / M_Pl^2 = {Lambda_KV:.6e} M_KK^4")
print(f"  m^2 = Lambda_KV / rho_s = {m_sq_Ap:.6e} M_KK^2")
print(f"  m = {m_Ap_MKK:.6e} M_KK")
print(f"  m = {m_Ap_GeV:.6e} GeV")
print(f"  log10(m/M_KK) = {np.log10(m_Ap_MKK):.4f}")
print(f"  m / m_required = {m_Ap_MKK / m_required_MKK:.4e}")


# ============================================================
# ROUTE A'': Alternative analytic — thermal mass from condensed matter
# ============================================================
#
# In superfluid 3He, the Goldstone mass arises from dipolar coupling
# that weakly breaks the continuous symmetry. The analog here is
# the BCS gap modulation.
#
# The standard result for pseudo-Goldstone mass:
#   m_pG^2 = epsilon * f_pi^2 / rho_s
# where epsilon is the explicit symmetry breaking parameter and
# f_pi is the decay constant.
#
# For BCS: epsilon = Delta^2 / E_F^2 (ratio of gap to Fermi energy)
# f_pi ~ sqrt(rho_s) * v_F (pion decay constant analog)
# m_pG^2 ~ (Delta/E_F)^2 * rho_s
#
# But [iK_7, D_K] = 0, so epsilon = 0 at tree level.
# The ONLY symmetry breaking is at the BCS level:
# E_cond depends on |Delta|^2 but NOT on phase => epsilon_BCS = 0 too!
#
# The phase only enters when we couple cells:
# epsilon_Josephson = J_inter * (1 - cos(phi_i - phi_j))
# gives m^2 = J_inter / (a^2 * rho_s)

print("\n" + "=" * 78)
print("ROUTE A'': Pseudo-Goldstone from Josephson Coupling")
print("=" * 78)

# The inter-cell Josephson coupling J_inter is NOT J_C2 (which is
# the single-cell thermal coupling). The inter-cell coupling for
# the U(1)_7 phase is:
# J_inter = |E_cond| * overlap^2
# where overlap is the wavefunction overlap between neighboring cells.
# For cells of size a ~ 0.152 and coherence length xi_BCS ~ 0.808:
overlap = np.exp(-a / xi_BCS)
J_inter = abs(E_cond) * overlap**2
m_sq_J = J_inter / (a**2 * rho_s_C2)
m_J_MKK = np.sqrt(m_sq_J)
m_J_GeV = m_J_MKK * M_KK

print(f"  overlap = exp(-a/xi_BCS) = exp(-{a:.4f}/{xi_BCS:.4f}) = {overlap:.6f}")
print(f"  J_inter = |E_cond| * overlap^2 = {J_inter:.6e} M_KK")
print(f"  m^2 = J_inter / (a^2 * rho_s) = {m_sq_J:.6e} M_KK^2")
print(f"  m = {m_J_MKK:.6e} M_KK")
print(f"  m = {m_J_GeV:.6e} GeV")
print(f"  log10(m/M_KK) = {np.log10(m_J_MKK):.4f}")
print(f"  m / m_required = {m_J_MKK / m_required_MKK:.4e}")

# Alternative: J_inter directly from the spectral action gradient stiffness
# The gradient stiffness Z_fold = 74730 gives an effective J
# J_spectral = Z_fold / (V * N_cells) where V = Vol_SU3 * a^8
# But this is the TAU stiffness, not the PHASE stiffness
# The phase stiffness IS rho_s, so J_phase_inter = rho_s * a^(d-2)
# For d=1 chain: J_phase = rho_s / a
m_sq_phase = rho_s_C2 / (N_cells * a)**2  # From phase stiffness over full chain
m_phase_MKK = np.sqrt(m_sq_phase)
m_phase_GeV = m_phase_MKK * M_KK

print(f"\n  Alternative (rho_s over full fabric):")
print(f"    m^2 = rho_s / (N_cells * a)^2 = {m_sq_phase:.6e} M_KK^2")
print(f"    m = {m_phase_MKK:.6e} M_KK")
print(f"    m = {m_phase_GeV:.6e} GeV")
print(f"    log10(m/M_KK) = {np.log10(m_phase_MKK):.4f}")


# ============================================================
# SUMMARY TABLE
# ============================================================

print("\n" + "=" * 78)
print("SUMMARY: ALL ROUTES")
print("=" * 78)

results = {}

# Route A: self-tuning
if m_A_MKK > 0:
    results['A_selftuning'] = (m_A_MKK, m_A_GeV)
else:
    results['A_selftuning'] = (0.0, 0.0)

# Route A analytic
if 'm_A_analytic_MKK' in dir():
    results['A_analytic'] = (m_A_analytic_MKK, m_A_analytic_GeV)

# Route A': Hubble relaxation
results['Ap_hubble'] = (m_Ap_MKK, m_Ap_GeV)

# Route A'': Josephson
results['App_josephson'] = (m_J_MKK, m_J_GeV)
results['App_phase_stiffness'] = (m_phase_MKK, m_phase_GeV)

# Route B: disorder
results['B_disorder'] = (m_B_MKK, m_B_GeV)

# Route C: dimensional crossover
results['C1_finite_2a'] = (m_C1_MKK, m_C1_GeV)
results['C2_finite_xi'] = (m_C2_MKK, m_C2_GeV)
results['C3_finite_32a'] = (m_C3_MKK, m_C3_GeV)

print(f"\n  {'Route':<25s} {'m/M_KK':>12s} {'m (GeV)':>14s} {'log10(m/MKK)':>14s} {'m/m_req':>12s} {'In gate?':>10s}")
print(f"  {'-'*25} {'-'*12} {'-'*14} {'-'*14} {'-'*12} {'-'*10}")

for name, (m_mkk, m_gev) in sorted(results.items()):
    if m_mkk > 0:
        log_m = np.log10(m_mkk)
        ratio = m_mkk / m_required_MKK
        in_gate = "YES" if -60 <= log_m <= -30 else "NO"
        print(f"  {name:<25s} {m_mkk:12.4e} {m_gev:14.4e} {log_m:14.4f} {ratio:12.4e} {in_gate:>10s}")
    else:
        print(f"  {name:<25s} {'0':>12s} {'0':>14s} {'---':>14s} {'---':>12s} {'FAIL':>10s}")


# ============================================================
# GATE VERDICT
# ============================================================

print("\n" + "=" * 78)
print("GATE VERDICT: Q-THEORY-GOLD-48")
print("=" * 78)

# Check if any route gives log10(m/M_KK) in [-60, -30]
any_in_gate = False
best_route = None
best_log = None

for name, (m_mkk, m_gev) in results.items():
    if m_mkk > 0:
        log_m = np.log10(m_mkk)
        if -60 <= log_m <= -30:
            any_in_gate = True
            if best_log is None or abs(log_m - np.log10(m_required_MKK)) < abs(best_log - np.log10(m_required_MKK)):
                best_log = log_m
                best_route = name

# Check if A' or A'' give masses in a useful range
all_m = [(name, m) for name, (m, _) in results.items() if m > 0]
all_logs = [(name, np.log10(m)) for name, m in all_m]

# Classify
if any_in_gate:
    verdict = "PASS"
    detail = f"Route {best_route}: log10(m/M_KK) = {best_log:.2f}, in [-60, -30]"
else:
    # Check if all are O(M_KK) or zero
    all_near_mkk = all(abs(lg) < 2 for _, lg in all_logs if lg is not None)
    all_zero = all(m == 0 for _, m in all_m)

    if all_zero:
        verdict = "FAIL"
        detail = "All routes give m = 0 (no self-tuning mass)"
    elif all_near_mkk:
        verdict = "FAIL"
        detail = f"All routes give m ~ M_KK (no hierarchy)"
    else:
        # Some routes give intermediate values
        min_log = min(lg for _, lg in all_logs)
        max_log = max(lg for _, lg in all_logs)
        if min_log > -30:
            verdict = "FAIL"
            detail = f"All routes: log10(m/M_KK) in [{min_log:.1f}, {max_log:.1f}] — all too heavy"
        else:
            verdict = "INFO"
            detail = f"Routes span log10(m/M_KK) in [{min_log:.1f}, {max_log:.1f}]"

print(f"\n  VERDICT: {verdict}")
print(f"  Detail: {detail}")

# Structural analysis
print(f"\n  STRUCTURAL ANALYSIS:")
print(f"  ---")
print(f"  Routes B and C give m ~ O(M_KK): these are lattice-scale masses,")
print(f"  not the cosmological Goldstone mass. They represent the UV cutoff")
print(f"  for Goldstone propagation, not the IR mass needed for n_s.")
print(f"  ---")
if m_A_MKK == 0:
    print(f"  Route A (self-tuning) gives m = 0: the lattice infrared cutoff is")
    print(f"  too harsh — the Goldstone IR fluctuations are too small to generate")
    print(f"  a self-consistent mass from BCS gap modulation on a 4^4 lattice.")
    print(f"  On a fabric of 32 cells, the 1D chain also fails.")
print(f"  ---")
print(f"  Route A' (Hubble relaxation) gives m ~ {m_Ap_MKK:.2e} M_KK:")
print(f"  log10 = {np.log10(m_Ap_MKK):.2f}. This is the Klinkhamer-Volovik")
print(f"  estimate applied to the BCS vacuum. It requires the full cosmological")
print(f"  Hubble expansion to be relevant (not just lattice dynamics).")
print(f"  ---")
print(f"  Route A'' (Josephson) gives m ~ {m_J_MKK:.2e} M_KK:")
print(f"  This is the inter-cell phase coupling mass, O(M_KK). Too heavy.")

# The key physics: the tiny mass m ~ 10^{-56} M_KK requires a hierarchy
# between the microscopic scale (M_KK) and the cosmological Goldstone mass.
# None of the routes produce this hierarchy from microscopic parameters alone.
# The ONLY route that could is A' (Hubble relaxation), which imports M_Pl.

print(f"\n  KEY CONCLUSION:")
print(f"  The q-theory self-tuning does NOT produce the required mass")
print(f"  hierarchy m/M_KK ~ 10^{{-56}} from microscopic parameters alone.")
print(f"  All routes give m ~ O(M_KK) or m = 0.")
print(f"  Route A' imports M_Pl and gives m ~ 10^{{-2}} M_KK, still 54 orders")
print(f"  above target. The mass problem IS the CC problem: the same")
print(f"  M_KK/M_Pl hierarchy that fails for Lambda also fails for m_Goldstone.")
print(f"  ---")
print(f"  From Volovik's perspective: the Goldstone mass, like the CC,")
print(f"  is determined by the FULL microscopic theory — not by an effective")
print(f"  field theory estimate. The q-theory equilibrium condition d(rho)/dq = 0")
print(f"  sets Lambda = 0 in exact equilibrium. The Goldstone mass is similarly")
print(f"  zero in exact equilibrium (massless Goldstone theorem). The observed")
print(f"  n_s - 1 = -0.035 thus requires a non-equilibrium mechanism — the same")
print(f"  class of physics that gives the observed small Lambda.")


# ============================================================
# Save results
# ============================================================

np.savez('s48_qtheory_goldstone.npz',
    # Route A
    m_A_selftuning_MKK=m_A_MKK,
    m_A_selftuning_GeV=m_A_GeV,
    m_A_analytic_MKK=m_A_analytic_MKK if 'm_A_analytic_MKK' in dir() else 0.0,
    m_A_analytic_GeV=m_A_analytic_GeV if 'm_A_analytic_GeV' in dir() else 0.0,

    # Route A'
    m_Ap_hubble_MKK=m_Ap_MKK,
    m_Ap_hubble_GeV=m_Ap_GeV,
    Lambda_KV=Lambda_KV,
    K_vac=K_vac,

    # Route A''
    m_App_josephson_MKK=m_J_MKK,
    m_App_josephson_GeV=m_J_GeV,
    J_inter=J_inter,
    overlap=overlap,
    m_App_phase_MKK=m_phase_MKK,
    m_App_phase_GeV=m_phase_GeV,

    # Route B
    m_B_disorder_MKK=m_B_MKK,
    m_B_disorder_GeV=m_B_GeV,
    xi_su2=xi_su2,
    xi_u1=xi_u1,
    ratio_T_J_su2=ratio_su2,
    ratio_T_J_u1=ratio_u1,
    ratio_T_J_C2=ratio_C2,

    # Route C
    m_C1_finite_2a_MKK=m_C1_MKK,
    m_C1_finite_2a_GeV=m_C1_GeV,
    m_C2_finite_xi_MKK=m_C2_MKK,
    m_C2_finite_xi_GeV=m_C2_GeV,
    m_C3_finite_32a_MKK=m_C3_MKK,
    m_C3_finite_32a_GeV=m_C3_GeV,

    # Inputs used
    J_C2=J_C2,
    J_su2=J_su2,
    J_u1=J_u1,
    T_acoustic=T_acoustic,
    rho_s_C2=rho_s_C2,
    rho_s_su2=rho_s_su2,
    rho_s_u1=rho_s_u1,
    E_cond_used=E_cond,
    l_cell=l_cell,
    N_cells=N_cells,

    # Target
    m_required_MKK=m_required_MKK,
    m_required_GeV=m_required_GeV,

    # Gate
    gate_name=np.array(['Q-THEORY-GOLD-48']),
    gate_verdict=np.array([verdict]),
    gate_detail=np.array([detail]),
)

print(f"\n  Saved: s48_qtheory_goldstone.npz")
print("=" * 78)
