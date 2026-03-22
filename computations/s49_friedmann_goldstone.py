#!/usr/bin/env python3
"""
s49_friedmann_goldstone.py — Friedmann-Goldstone Coupling
==========================================================

Session 49, Wave 1-A (Volovik agent)
Gate: FRIEDMANN-GOLDSTONE-49

Computes the effective Goldstone mass when the fabric phase field is
coupled to 4D Friedmann dynamics through the superfluid density tensor.

Physics:
  The Goldstone mode phi of the spontaneously broken U(1)_7 propagates
  on the 32-cell Josephson network. In the absence of Friedmann coupling,
  the dispersion is omega^2 = (J/rho_s) K^2 (massless, S47 PASS).

  When coupled to an expanding FRW universe:
    d^2 phi/dt^2 + 3H dphi/dt + (J/rho_s) nabla^2 phi = 0

  The Hubble friction 3H damps long-wavelength modes, creating an
  effective mass m_eff^2 = (9/4) H^2 in de Sitter (exact result).

  The 84-order scale crisis (S48 Volovik review):
    J * K_pivot^2 ~ 3.7 M_KK^2  (Josephson coupling at CMB pivot)
    m_G^2 ~ H_0^2 ~ 10^{-116} M_KK^2  (required)
    Ratio: 10^{-120}

  This script computes:
  1. The exact Goldstone EOM on 32-cell network + FRW background
  2. The late-time de Sitter effective mass m_eff = (3/2)H
  3. The CMB-epoch effective mass (matter-dominated H(z))
  4. The scale crisis: ratio of Hubble mass to Josephson mass
  5. Non-equilibrium routes: GGE-modified stiffness, running J
  6. The q-theory perspective: m_eff from vacuum relaxation rate

Inputs:
  - s47_rhos_tensor.npz (superfluid stiffness tensor)
  - s47_texture_corr.npz (Josephson couplings, T_acoustic)
  - s39_richardson_gaudin.npz (GGE conserved quantities)
  - s39_gge_lambdas.npz (GGE occupations and temperatures)

Gate criteria:
  PASS: m_G/M_KK in [10^{-60}, 10^{-30}] with no free parameters
  INFO: computable but outside range or requires tuning
  FAIL: m_G = 0 or computation breaks down
"""

import sys
sys.path.insert(0, '.')
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from canonical_constants import (
    E_cond, tau_fold, M_KK, M_KK_gravity, M_KK_kerner,
    Delta_0_GL, Delta_B3, N_cells, xi_GL, xi_BCS,
    a0_fold, a2_fold, a4_fold, S_fold,
    rho_Lambda_obs, M_Pl_reduced, M_Pl_unreduced, PI,
    hbar_c_GeV_m, Mpc_to_m, omega_PV,
    E_B1, E_B2_mean, E_B3_mean,
    rho_B2_per_mode, M_max_thouless,
    N_dof_BCS, E_cond_ED_8mode,
    H_0_GeV, H_0_inv_s, H_0_km_s_Mpc,
    G_N, c_light, hbar_SI, Omega_Lambda, Omega_m,
    rho_crit_GeV4, rho_Lambda_obs, Lambda_obs_MP4,
    Mpc_to_GeV_inv, GeV_inv_to_Mpc,
    T_CMB, k_B, t_universe_s,
    H_fold, v_terminal, dt_transit,
    Z_fold, G_DeWitt, M_ATDHFB,
    Gamma_Langer_BCS, S_inst, omega_att,
    c_fabric,
)

# ============================================================
# Load upstream data
# ============================================================

d_rhos = np.load('s47_rhos_tensor.npz', allow_pickle=True)
d_tex = np.load('s47_texture_corr.npz', allow_pickle=True)
d_rg = np.load('s39_richardson_gaudin.npz', allow_pickle=True)
d_gge = np.load('s39_gge_lambdas.npz', allow_pickle=True)

# Superfluid stiffness at fold
rho_s_eigs = d_rhos['rho_s_eigs_fold']     # shape (8,)
rho_s_diag = d_rhos['rho_s_diag_fold']     # shape (8,)
anisotropy = float(d_rhos['anisotropy_fold'])

# Josephson couplings
J_C2 = float(d_tex['J_C2'])                # 0.933 M_KK
J_su2 = float(d_tex['J_su2'])              # 0.059 M_KK
J_u1 = float(d_tex['J_u1'])                # 0.038 M_KK
T_acoustic = float(d_tex['T_acoustic'])     # 0.112 M_KK
l_cell = float(d_tex['l_cell'])             # 0.152 M_KK^{-1}
xi_phase_C2 = float(d_tex['xi_phase_C2_acoustic'])  # 532 cells
phi_rms_C2 = float(d_tex['phi_rms_C2_acoustic'])    # 0.566 rad

# GGE data
lambda_k = d_gge['lambda_k']   # 8 conserved integrals
T_eff = d_gge['T_eff']         # 8 effective temperatures
p_k = d_gge['p_k']             # 8 occupation probabilities
S_gge = float(d_gge['S_gge'])  # GGE entropy

# Richardson-Gaudin data
V_phys_fold = d_rg['V_phys_fold']   # 8x8 pairing interaction
Delta_k_fold = d_rg['Delta_k_fold'] # 8 BCS gaps

# Derived stiffness components
rho_s_C2 = float(np.mean(rho_s_eigs[4:8]))   # C^2 block: ~7.96 M_KK
rho_s_su2 = float(np.mean(rho_s_eigs[1:4]))  # su(2) block: ~0.505 M_KK
rho_s_u1 = float(rho_s_eigs[0])              # u(1): ~0.327 M_KK

# Fabric parameters
L_fabric = N_cells * l_cell  # total fabric extent in M_KK^{-1}

print("=" * 78)
print("FRIEDMANN-GOLDSTONE COUPLING — S49 W1-A")
print("=" * 78)

print("\n=== INPUT PARAMETERS ===")
print(f"  rho_s(C^2) = {rho_s_C2:.6f}  M_KK")
print(f"  rho_s(su2) = {rho_s_su2:.6f}  M_KK")
print(f"  rho_s(u1)  = {rho_s_u1:.6f}  M_KK")
print(f"  anisotropy = {anisotropy:.2f}")
print(f"  J_C2 = {J_C2:.6f}  M_KK")
print(f"  T_acoustic = {T_acoustic:.6f}  M_KK")
print(f"  l_cell = {l_cell:.6f}  M_KK^{{-1}}")
print(f"  L_fabric = {L_fabric:.6f}  M_KK^{{-1}}")
print(f"  xi_phase(C^2) = {xi_phase_C2:.1f}  cells")
print(f"  phi_rms(C^2) = {phi_rms_C2:.4f}  rad")
print(f"  |E_cond| = {abs(E_cond):.6f}  M_KK")
print(f"  M_KK = {M_KK:.4e}  GeV")
print(f"  H_0 = {H_0_GeV:.4e}  GeV")
print(f"  H_0 / M_KK = {H_0_GeV / M_KK:.4e}")
print(f"  S_gge = {S_gge:.4f} nats")


# ============================================================
# SECTION 1: Scale Conversion — M_KK Units to Physical Units
# ============================================================
# The 32-cell tessellation spans L_fabric = 4.864 M_KK^{-1}.
# The physical size of the fabric is the horizon: L_H = c/H_0.
# This defines the mapping:
#   L_fabric (M_KK^{-1}) <-> L_H (physical m)
#   K_fabric (M_KK) <-> k_physical (m^{-1})
#
# The mapping is determined by the spectral action / Sakharov
# induced gravity: M_Pl^2 = (a_2 / 4*pi) * M_KK^2
# This is not a free parameter; it's computed from the spectrum.

print("\n" + "=" * 78)
print("SECTION 1: Scale Hierarchy")
print("=" * 78)

# The fundamental scale ratios (no free parameters):
H_0_over_MKK = H_0_GeV / M_KK
M_Pl_over_MKK = M_Pl_reduced / M_KK

print(f"\n  H_0 / M_KK = {H_0_over_MKK:.4e}")
print(f"  M_Pl / M_KK = {M_Pl_over_MKK:.4f}")
print(f"  H_0 / M_Pl = {H_0_GeV / M_Pl_reduced:.4e}")
print(f"  (H_0/M_KK)^2 = {H_0_over_MKK**2:.4e}")

# Hubble length in M_KK^{-1}
L_H_MKK = 1.0 / H_0_over_MKK  # ~ 5.2e58 M_KK^{-1}
print(f"\n  L_Hubble / M_KK^{{-1}} = {L_H_MKK:.4e}")
print(f"  L_fabric / M_KK^{{-1}} = {L_fabric:.4f}")
print(f"  L_fabric / L_Hubble = {L_fabric / L_H_MKK:.4e}")

# Physical fabric size
L_fabric_m = L_fabric * hbar_c_GeV_m / M_KK  # in meters
L_H_m = c_light / (H_0_inv_s)
print(f"\n  L_fabric (physical) = {L_fabric_m:.4e} m")
print(f"  L_Hubble (physical) = {L_H_m:.4e} m")
print(f"  L_fabric / L_Hubble = {L_fabric_m / L_H_m:.4e}")

# CMB pivot scale
k_pivot_Mpc = 0.05  # Mpc^{-1} (Planck 2018)
k_pivot_GeV = k_pivot_Mpc * Mpc_to_GeV_inv  # GeV^{-1} -> GeV (actually k has dim 1/length)
# k_pivot in natural units: k_pivot = 0.05 Mpc^{-1} * (Mpc in GeV^{-1})
# k_pivot = 0.05 / (Mpc_to_m / hbar_c_GeV_m) GeV = 0.05 * hbar_c_GeV_m / Mpc_to_m
k_pivot_GeV_proper = k_pivot_Mpc * hbar_c_GeV_m / Mpc_to_m  # GeV
k_pivot_MKK = k_pivot_GeV_proper / M_KK

print(f"\n  k_pivot = {k_pivot_Mpc} Mpc^{{-1}}")
print(f"  k_pivot = {k_pivot_GeV_proper:.4e} GeV")
print(f"  k_pivot / M_KK = {k_pivot_MKK:.4e}")


# ============================================================
# SECTION 2: Goldstone Dispersion on 32-Cell Josephson Network
# ============================================================
# The Goldstone mode phi_i on cell i obeys:
#   rho_s_i * d^2 phi_i / dt^2 = J_{ij} * sum_j (phi_j - phi_i)
#
# On a 1D ring with N_cells cells, the eigenvalues are:
#   omega_n^2 = (2J / rho_s) * [1 - cos(2*pi*n/N_cells)]
#             ~ (J / rho_s) * K_n^2  for K_n << 1
#   where K_n = 2*pi*n / (N_cells * l_cell)
#
# The C^2 subspace has ordered phase correlations (xi = 532 cells >> N_cells = 32).
# The Goldstone propagates coherently on this subspace.

print("\n" + "=" * 78)
print("SECTION 2: Goldstone Dispersion on Josephson Network")
print("=" * 78)

# Normal modes of 1D ring (N_cells)
n_modes_ring = np.arange(1, N_cells)  # 1 to 31
K_n_ring = 2 * PI * n_modes_ring / (N_cells * l_cell)  # M_KK units

# Exact lattice dispersion (J-model)
omega_sq_ring = (2 * J_C2 / rho_s_C2) * (1 - np.cos(2 * PI * n_modes_ring / N_cells))

# Continuum limit: omega^2 = (J/rho_s) * K^2
c_goldstone_sq = J_C2 / rho_s_C2  # Goldstone "sound velocity" squared
c_goldstone = np.sqrt(c_goldstone_sq)

print(f"\n  Goldstone velocity: c_G^2 = J_C2/rho_s_C2 = {c_goldstone_sq:.6f} M_KK^2")
print(f"  c_G = {c_goldstone:.6f} M_KK")
print(f"  c_G / c_fabric = {c_goldstone / c_fabric:.6f}")

# Mode spectrum
K_min_fabric = 2 * PI / (N_cells * l_cell)
K_max_fabric = PI / l_cell
omega_min = np.sqrt(omega_sq_ring[0])
omega_max = np.sqrt(omega_sq_ring[-1])

print(f"\n  K_min = {K_min_fabric:.4f} M_KK  (n=1, longest mode)")
print(f"  K_max = {K_max_fabric:.4f} M_KK  (n=N/2, zone boundary)")
print(f"  omega_min = {omega_min:.6f} M_KK")
print(f"  omega_max = {omega_max:.6f} M_KK")

# The PHYSICAL mode wavenumbers (in GeV, not M_KK)
K_min_phys = K_min_fabric * M_KK   # GeV
K_max_phys = K_max_fabric * M_KK   # GeV

print(f"\n  K_min (physical) = {K_min_phys:.4e} GeV")
print(f"  K_max (physical) = {K_max_phys:.4e} GeV")


# ============================================================
# SECTION 3: Friedmann Coupling — Exact de Sitter Mass
# ============================================================
# A massless scalar in FRW obeys:
#   phi'' + 3H phi' + (k^2/a^2) phi = 0
#
# In de Sitter (H = const), the late-time attractor gives:
#   omega^2 = k^2/a^2 + (9/4)H^2 - (m_bare)^2 * corrections
#
# For a MASSLESS Goldstone (m_bare = 0), the de Sitter background
# provides an effective mass:
#   m_eff^2 = (9/4) H^2
#
# This is the Hubble-scale mass from conformal coupling of a
# minimally-coupled scalar in de Sitter. It is:
#   - Parameter-free (H is cosmological, not tuned)
#   - Generated by expansion (non-equilibrium physics)
#   - The 3He analog: second sound in an expanding container
#
# From Volovik's perspective (Paper 05, eq 4.4): this is the
# mass of the Goldstone of the broken Lorentz symmetry in
# the superfluid vacuum, where H plays the role of the
# departure from equilibrium.

print("\n" + "=" * 78)
print("SECTION 3: Friedmann-Coupled Effective Mass")
print("=" * 78)

# Late-time de Sitter: H = H_0 * sqrt(Omega_Lambda)
H_dS = H_0_GeV * np.sqrt(Omega_Lambda)
H_dS_MKK = H_dS / M_KK

# De Sitter effective mass
m_dS_sq = (9.0 / 4.0) * H_dS**2  # GeV^2
m_dS = np.sqrt(m_dS_sq)           # GeV
m_dS_MKK = m_dS / M_KK

print(f"\n  H_dS = H_0 * sqrt(Omega_Lambda) = {H_dS:.4e} GeV")
print(f"  H_dS / M_KK = {H_dS_MKK:.4e}")
print(f"  m_dS = (3/2)*H_dS = {m_dS:.4e} GeV")
print(f"  m_dS / M_KK = {m_dS_MKK:.4e}")
print(f"  log10(m_dS / M_KK) = {np.log10(m_dS_MKK):.4f}")

# Is this in the gate window?
gate_lo, gate_hi = -60, -30
log_m_dS = np.log10(m_dS_MKK)
in_gate_dS = gate_lo <= log_m_dS <= gate_hi
print(f"  Gate window: [{gate_lo}, {gate_hi}]")
print(f"  log10(m_dS/M_KK) = {log_m_dS:.2f}  -> {'IN GATE' if in_gate_dS else 'OUTSIDE'}")


# ============================================================
# SECTION 4: Matter-Dominated Mass (CMB Epoch)
# ============================================================
# At CMB decoupling (z ~ 1100), H(z) is larger:
#   H(z) = H_0 * sqrt(Omega_m * (1+z)^3 + Omega_Lambda)
# The effective Goldstone mass at this epoch:
#   m_eff(z) = (3/2) * H(z)
#
# For the primordial power spectrum, what matters is the
# INFLATIONARY Hubble parameter, not today's. But in this
# framework, there is no separate inflaton — the transit IS
# the expansion. So H during transit is the relevant quantity.

print("\n" + "=" * 78)
print("SECTION 4: Epoch-Dependent Effective Mass")
print("=" * 78)

# CMB decoupling
z_CMB = 1100
H_CMB = H_0_GeV * np.sqrt(Omega_m * (1 + z_CMB)**3 + Omega_Lambda)
m_CMB = 1.5 * H_CMB
m_CMB_MKK = m_CMB / M_KK
print(f"\n  z_CMB = {z_CMB}")
print(f"  H(z_CMB) = {H_CMB:.4e} GeV")
print(f"  m_eff(z_CMB) = (3/2)*H = {m_CMB:.4e} GeV")
print(f"  m_eff(z_CMB) / M_KK = {m_CMB_MKK:.4e}")
print(f"  log10(m_CMB/M_KK) = {np.log10(m_CMB_MKK):.4f}")

# BBN epoch
z_BBN = 4e8
H_BBN = H_0_GeV * np.sqrt(Omega_m * (1 + z_BBN)**3 + Omega_Lambda)
m_BBN = 1.5 * H_BBN
m_BBN_MKK = m_BBN / M_KK
print(f"\n  z_BBN = {z_BBN:.0e}")
print(f"  H(z_BBN) = {H_BBN:.4e} GeV")
print(f"  m_eff(z_BBN) = {m_BBN:.4e} GeV")
print(f"  m_eff(z_BBN) / M_KK = {m_BBN_MKK:.4e}")
print(f"  log10(m_BBN/M_KK) = {np.log10(m_BBN_MKK):.4f}")

# Transit epoch (framework-specific)
# H_fold is in M_KK units (S38: H_fold = 586.5 M_KK)
# This is the Hubble parameter DURING transit
H_transit_GeV = H_fold * M_KK  # GeV
m_transit = 1.5 * H_transit_GeV
m_transit_MKK = 1.5 * H_fold  # In M_KK units

print(f"\n  H_fold = {H_fold:.2f} M_KK = {H_transit_GeV:.4e} GeV")
print(f"  m_eff(transit) = {m_transit_MKK:.2f} M_KK = {m_transit:.4e} GeV")
print(f"  log10(m_transit/M_KK) = {np.log10(m_transit_MKK):.4f}")

# The transit Hubble is HUGE — m_eff ~ 880 M_KK during transit.
# This means the Goldstone is FROZEN during transit (m >> omega_max).
# It only becomes dynamical when H drops below the Josephson scale.

# Scan: m_eff(z) vs z
z_scan = np.logspace(-1, 10, 1000)
H_scan = H_0_GeV * np.sqrt(Omega_m * (1 + z_scan)**3 + Omega_Lambda)
m_scan = 1.5 * H_scan
m_scan_MKK = m_scan / M_KK


# ============================================================
# SECTION 5: The 84-Order Scale Crisis — Quantitative
# ============================================================
# The Ornstein-Zernike power spectrum is:
#   P(K) ~ 1 / (K^2 + m^2/J)
#
# For n_s != 1, we need m != 0. The required mass gap:
#   m_OZ^2 / J = K_pivot^2 * (2 - n_s - 2) / (n_s - 1)  [near-HZ]
#   Actually: P(K) ~ K^{n_s-1} => n_s - 1 = -2 + 2 = 0 for massless
#   With mass: P(K) ~ 1/(K^2 + mu^2) where mu^2 = m^2/(rho_s * c_G^2)
#   This gives n_s = 1 for massless (confirmed S47).
#   For n_s = 0.965: the tilt is 1 - n_s = 0.035.
#
# In O-Z with K^{-(2-alpha)}: alpha = 2(1-n_s)/(1+n_s) ~ 0.036
# This requires mu^2 comparable to K_pivot^2.
#
# mu^2 = m^2 / (rho_s * c_G^2 * a^2)   [dimensionless]
# K_pivot on the fabric is K_pivot_MKK ~ 10^{-58} M_KK
#
# For mu^2 ~ K_pivot^2: m^2 ~ rho_s * c_G^2 * a^2 * K_pivot_MKK^2
# This is the target mass.

print("\n" + "=" * 78)
print("SECTION 5: Scale Crisis Analysis")
print("=" * 78)

# The Josephson energy scale at CMB pivot
# K_pivot in M_KK units (fabric wavenumber)
# The CMB pivot probes scales ~ 1/k_pivot ~ 20 Mpc ~ 6e23 m
# In M_KK^{-1} units: k_pivot_MKK computed above

E_Josephson_pivot = J_C2 * k_pivot_MKK**2  # M_KK^2 (energy of mode at pivot)
m_Hubble_now_sq = (9.0 / 4.0) * H_0_over_MKK**2  # M_KK^2

print(f"\n  K_pivot / M_KK = {k_pivot_MKK:.4e}")
print(f"  K_pivot^2 / M_KK^2 = {k_pivot_MKK**2:.4e}")
print(f"  J_C2 * K_pivot^2 = {E_Josephson_pivot:.4e} M_KK^2")
print(f"  m_Hubble^2 = (9/4)*H_0^2 = {m_Hubble_now_sq:.4e} M_KK^2")
print(f"  Ratio m_H^2 / (J*K^2) = {m_Hubble_now_sq / E_Josephson_pivot:.4e}")

# The scale crisis:
log_ratio = np.log10(m_Hubble_now_sq / E_Josephson_pivot)
print(f"  log10 ratio = {log_ratio:.1f}")
print(f"  SCALE CRISIS: {abs(log_ratio):.0f} orders between Hubble mass and Josephson energy at pivot")

# But wait — the CMB pivot is NOT at the fabric scale.
# The fabric has only 32 cells. K_min = 2*pi/(32*0.152) = 1.29 M_KK.
# The CMB pivot at k_pivot_MKK ~ 10^{-58} M_KK is 58 orders below the LOWEST
# fabric mode. The Goldstone dispersion simply does not extend to CMB scales.
#
# This is the REAL scale crisis: the 32-cell fabric has O(30) modes, all
# at M_KK scale. CMB modes require K ~ 10^{-58} M_KK. There is no connection.
#
# UNLESS: the fabric IS the universe (each cell is ~ 450 Mpc comoving).
# In that case, K_fabric maps directly to CMB scales.

print(f"\n  --- Scale mapping test ---")
print(f"  K_min(fabric) = {K_min_fabric:.4f} M_KK")
print(f"  K_max(fabric) = {K_max_fabric:.4f} M_KK")
print(f"  These are ALL at M_KK scale (O(1) to O(10) M_KK).")
print(f"  CMB pivot: K_pivot ~ {k_pivot_MKK:.4e} M_KK")
print(f"  Separation: {np.log10(K_min_fabric / k_pivot_MKK):.0f} orders")

# However, S47 texture correlation established a DIFFERENT mapping:
# l_cell_fabric_Mpc = 450 Mpc (from S47 s47_texture_corr.npz)
l_cell_Mpc = float(d_tex['l_cell_fabric_Mpc'])  # 450 Mpc
L_fabric_Mpc = N_cells * l_cell_Mpc

K_min_fabric_Mpc = 2 * PI / L_fabric_Mpc  # Mpc^{-1}
K_max_fabric_Mpc = PI / l_cell_Mpc         # Mpc^{-1}

print(f"\n  --- Physical fabric mapping (S47) ---")
print(f"  l_cell = {l_cell_Mpc:.0f} Mpc")
print(f"  L_fabric = {L_fabric_Mpc:.0f} Mpc")
print(f"  K_min(fabric) = {K_min_fabric_Mpc:.6f} Mpc^{{-1}}")
print(f"  K_max(fabric) = {K_max_fabric_Mpc:.6f} Mpc^{{-1}}")
print(f"  k_pivot(CMB) = {k_pivot_Mpc} Mpc^{{-1}}")

# Check if CMB pivot is within fabric mode range
if K_min_fabric_Mpc <= k_pivot_Mpc <= K_max_fabric_Mpc:
    print(f"  CMB PIVOT IS WITHIN FABRIC RANGE")
    pivot_in_fabric = True
else:
    print(f"  CMB PIVOT IS OUTSIDE FABRIC RANGE")
    pivot_in_fabric = False
    if k_pivot_Mpc > K_max_fabric_Mpc:
        print(f"    k_pivot > K_max: above Brillouin zone by {k_pivot_Mpc/K_max_fabric_Mpc:.2f}x")
    else:
        print(f"    k_pivot < K_min: below lowest mode by {K_min_fabric_Mpc/k_pivot_Mpc:.2f}x")


# ============================================================
# SECTION 6: Friedmann EOM on the Josephson Network
# ============================================================
# With the S47 physical mapping (l_cell = 450 Mpc), the fabric
# modes are at physical wavelengths 900-14400 Mpc.
#
# The Friedmann equation couples to the Goldstone via the
# effective potential:
#   V_eff(phi) = (1/2) * m_eff^2(H) * phi^2
#
# where m_eff^2(H) = (9/4)*H^2 for de Sitter.
#
# The linearized EOM for mode n on the Josephson network:
#   d^2 phi_n / dt^2 + 3*H*dphi_n/dt + [omega_n^2 + m_eff^2]*phi_n = 0
#
# where omega_n^2 = (2*J/rho_s)*(1 - cos(2*pi*n/N))
#
# The ratio that matters for the power spectrum tilt:
#   R_n = m_eff^2 / omega_n^2
#
# For massless Goldstone + Hubble mass:
#   R_n = (9/4)*H^2 / [(2J/rho_s)*(1-cos(2*pi*n/N))]

print("\n" + "=" * 78)
print("SECTION 6: Friedmann EOM — Mode-by-Mode Analysis")
print("=" * 78)

# The Goldstone frequency omega_n and Hubble mass must be in the SAME units.
# Option A: Everything in M_KK units (if modes oscillate at M_KK frequency)
# Option B: Everything in physical units via the S47 mapping

# The key insight: rho_s and J are in M_KK units because they come from
# the spectral action. But the PHYSICAL time coordinate is t_physical
# (cosmic time), not t_MKK. The relationship:
# omega_physical = omega_MKK * M_KK / hbar
#
# For the Friedmann equation in PHYSICAL units:
# d^2 phi / dt_phys^2 + 3H dphi/dt_phys + (J_phys/rho_s_phys)*nabla^2 phi = 0
#
# J_phys = J_C2 * M_KK (in GeV, since J is dimensionless in M_KK units)
# rho_s_phys = rho_s * M_KK (same)
# c_G_phys = c_G * c_light (if M_KK is the natural unit for speeds)

# Actually, c_G is a dimensionless ratio in M_KK units.
# In physical units, the Goldstone frequency:
#   omega_n_phys = omega_n_MKK * (M_KK / hbar)  [rad/s]
#   where omega_n_MKK has dimensions of M_KK
#
# The Hubble parameter in natural units:
#   H_0 = 1.438e-42 GeV = 1.438e-42 / M_KK * M_KK = 1.94e-59 M_KK
#
# So: m_Hubble / omega_min_fabric =
# = (3/2)*H_0_MKK / omega_min_MKK

R_Hubble_modes = np.zeros(len(n_modes_ring))
for i, n in enumerate(n_modes_ring):
    R_Hubble_modes[i] = m_Hubble_now_sq / omega_sq_ring[i]

print(f"\n  m_Hubble^2 (de Sitter) = {m_Hubble_now_sq:.4e} M_KK^2")
print(f"  omega_min^2 (n=1) = {omega_sq_ring[0]:.6f} M_KK^2")
print(f"  omega_max^2 (n=15) = {omega_sq_ring[14]:.6f} M_KK^2")
print(f"  R(n=1) = m_H^2/omega_1^2 = {R_Hubble_modes[0]:.4e}")
print(f"  R(n=15) = m_H^2/omega_15^2 = {R_Hubble_modes[14]:.4e}")
print(f"\n  R << 1 for ALL modes: Hubble mass is NEGLIGIBLE on the fabric.")
print(f"  The fabric modes oscillate {1/np.sqrt(R_Hubble_modes[0]):.0e}x faster than Hubble.")


# ============================================================
# SECTION 7: Non-Equilibrium Routes
# ============================================================
# Given that m_Hubble << omega_fabric, the Hubble friction does NOT
# generate a mass term visible at the fabric scale. The modes are
# over-damped only when omega < H, which never happens.
#
# Route 7a: Horizon-size mass (m ~ pi*c/L_Hubble)
# Route 7b: Running stiffness rho_s(a) (non-equilibrium GGE)
# Route 7c: GGE-modified Josephson coupling
# Route 7d: Finite-temperature phase transition (T_acoustic near T_c)
# Route 7e: q-theory vacuum relaxation rate
# Route 7f: Conformal mass from Friedmann coupling
#            (m^2 = -R/6 where R is the Ricci scalar)

print("\n" + "=" * 78)
print("SECTION 7: Non-Equilibrium Routes")
print("=" * 78)

# === Route 7a: Horizon Finite-Size Mass ===
# The longest wavelength mode that fits in the Hubble volume:
# K_H = 2*pi / L_H, giving m_H = c_G * K_H
# This is NOT the de Sitter mass — it's the IR cutoff of the Goldstone.

K_H = 2 * PI / L_H_MKK  # M_KK units
m_horizon_sq = c_goldstone_sq * K_H**2
m_horizon = np.sqrt(m_horizon_sq) * M_KK  # GeV
m_horizon_MKK = np.sqrt(m_horizon_sq)

print(f"\n  7a: Horizon finite-size mass")
print(f"    K_H = 2*pi/L_H = {K_H:.4e} M_KK")
print(f"    m_horizon = c_G * K_H = {m_horizon_MKK:.4e} M_KK")
print(f"    m_horizon = {m_horizon:.4e} GeV")
print(f"    log10(m/M_KK) = {np.log10(m_horizon_MKK):.2f}")
log_m_7a = np.log10(m_horizon_MKK)

# === Route 7b: GGE-Modified Stiffness ===
# The GGE has non-thermal occupations. The superfluid density at
# finite temperature is reduced: rho_s(T) = rho_s(0) * (1 - (T/T_c)^alpha)
# For GGE with 8 temperatures, the reduction is:
# rho_s_GGE = rho_s_0 * product_k (1 - p_k_GGE)
# where p_k is the occupation of mode k.
# If p_k is large (mode excited), that mode's contribution to rho_s is reduced.

# GGE occupations from S39
p_B2 = float(d_gge['p_B2'])  # 0.930
p_B1 = float(d_gge['p_B1'])  # 0.063
p_B3 = float(d_gge['p_B3'])  # 0.007

# The GGE depletion of superfluid density (Landau two-fluid model):
# rho_n / rho = sum_k p_k * (rho contribution of mode k)
# For the BCS system: each mode k with occupation p_k contributes
# p_k to the normal component.
rho_n_fraction = float(np.sum(p_k))  # Total normal fraction
rho_s_GGE_fraction = 1.0 - rho_n_fraction  # Superfluid fraction remaining

print(f"\n  7b: GGE-modified superfluid density")
print(f"    p_k occupations: {p_k}")
print(f"    Total normal fraction: sum(p_k) = {rho_n_fraction:.4f}")
print(f"    rho_s_GGE / rho_s_0 = {rho_s_GGE_fraction:.4f}")

if rho_s_GGE_fraction > 0:
    rho_s_GGE = rho_s_C2 * rho_s_GGE_fraction
    c_G_GGE = np.sqrt(J_C2 / rho_s_GGE)
    print(f"    rho_s_GGE(C^2) = {rho_s_GGE:.4f} M_KK")
    print(f"    c_G(GGE) = {c_G_GGE:.4f} M_KK")
    print(f"    Enhancement of c_G: {c_G_GGE/c_goldstone:.4f}x")
    print(f"    But this does NOT generate a mass — it changes the SPEED, not the gap.")
else:
    print(f"    WARNING: rho_s_GGE <= 0 — superfluid is destroyed (normal state)")
    rho_s_GGE = 0

# === Route 7c: Curvature Coupling (Conformal Mass) ===
# A minimally-coupled scalar in FRW has effective mass:
#   m_conf^2 = -(1-6*xi_conf)*R/6
# For minimal coupling xi_conf = 0:
#   m_conf^2 = -R/6
# In FRW, R = 6(H_dot + 2H^2). In de Sitter, H_dot = 0:
#   R = 12 H^2
#   m_conf^2 = -2H^2  (tachyonic for minimal coupling)
#
# For conformal coupling xi_conf = 1/6: m_conf = 0
# The PHYSICAL coupling depends on how the Goldstone enters the
# gravitational action. From the Sakharov induced gravity perspective
# (Paper 05), the effective xi depends on the spectral geometry.
#
# Result: xi_conf is model-dependent. For ANY xi_conf:
#   m_conf^2 = (6*xi_conf - 1)*2*H^2
#   = (12*xi_conf - 2)*H^2

print(f"\n  7c: Curvature coupling (conformal mass)")
xi_conf_minimal = 0.0
xi_conf_conformal = 1.0/6.0

for xi_label, xi_val in [("minimal", xi_conf_minimal), ("conformal", xi_conf_conformal)]:
    m_conf_sq = (12 * xi_val - 2) * H_dS_MKK**2
    if m_conf_sq > 0:
        m_conf_MKK = np.sqrt(m_conf_sq)
        print(f"    xi = {xi_val:.4f} ({xi_label}): m^2 = {m_conf_sq:.4e} M_KK^2, m = {m_conf_MKK:.4e} M_KK")
    elif m_conf_sq == 0:
        print(f"    xi = {xi_val:.4f} ({xi_label}): m^2 = 0 (conformally coupled)")
    else:
        print(f"    xi = {xi_val:.4f} ({xi_label}): m^2 = {m_conf_sq:.4e} M_KK^2 (TACHYONIC)")

# For the de Sitter effective mass (the physically relevant one):
# m_dS^2 = (9/4)H^2 combines BOTH Hubble friction and curvature
# It is the mass that appears in the mode function after conformal rescaling.
# This result is independent of xi_conf (it comes from the a^3 measure).
print(f"    The de Sitter mass m^2 = (9/4)H^2 includes both Hubble friction")
print(f"    and curvature coupling. It is the physical mass in the mode equation.")

# === Route 7d: q-Theory Vacuum Relaxation Mass ===
# From Papers 15-16 (Klinkhamer-Volovik): the CC relaxation rate is
#   Gamma_q ~ H^3 / E_Planck^2 (for thermodynamic variables)
#
# The Goldstone mass from vacuum relaxation:
#   m_q^2 ~ Gamma_q / rho_s ~ H^3 / (M_Pl^2 * rho_s)
# This combines the q-theory idea with the superfluid stiffness.

print(f"\n  7d: q-theory vacuum relaxation mass")
Gamma_q = H_dS**3 / M_Pl_reduced**2  # GeV^3
m_q_sq = Gamma_q / (rho_s_C2 * M_KK)  # GeV^2 (rho_s in M_KK, need to convert)
m_q_sq_proper = H_dS_MKK**3 / (M_Pl_over_MKK**2 * rho_s_C2)  # M_KK^2
m_q = np.sqrt(abs(m_q_sq_proper))
log_m_7d = np.log10(m_q) if m_q > 0 else -999

print(f"    Gamma_q = H^3/M_Pl^2 = {Gamma_q:.4e} GeV^3")
print(f"    m_q^2 = Gamma_q / rho_s = {m_q_sq_proper:.4e} M_KK^2")
print(f"    m_q = {m_q:.4e} M_KK = {m_q * M_KK:.4e} GeV")
print(f"    log10(m_q/M_KK) = {log_m_7d:.2f}")

# === Route 7e: De Sitter Temperature Mass ===
# From Papers 35, 37: the de Sitter state has Gibbons-Hawking temperature
#   T_GH = H / (2*pi)
# The thermal mass of the Goldstone from Gibbons-Hawking radiation:
#   m_T^2 = lambda * T_GH^2 where lambda is the self-coupling
# For the Josephson model: lambda = J / (rho_s * a^2)

print(f"\n  7e: Gibbons-Hawking thermal mass")
T_GH = H_dS_MKK / (2 * PI)  # M_KK units
lambda_J = J_C2 / (rho_s_C2 * l_cell**2)
m_GH_sq = lambda_J * T_GH**2
m_GH = np.sqrt(m_GH_sq) if m_GH_sq > 0 else 0
log_m_7e = np.log10(m_GH) if m_GH > 0 else -999

print(f"    T_GH = H/(2*pi) = {T_GH:.4e} M_KK")
print(f"    lambda = J/(rho_s*a^2) = {lambda_J:.4f} M_KK^2")
print(f"    m_GH^2 = lambda * T_GH^2 = {m_GH_sq:.4e} M_KK^2")
print(f"    m_GH = {m_GH:.4e} M_KK = {m_GH * M_KK:.4e} GeV")
print(f"    log10(m_GH/M_KK) = {log_m_7e:.2f}")

# === Route 7f: Composite — de Sitter Effective Mass (the RESULT) ===
# The clean result combining all effects:
# In de Sitter, a minimally-coupled massless scalar has
# m_eff^2 = (9/4)*H^2 — THIS IS THE ANSWER.
#
# The 3He analog: in an expanding superfluid (Hubble-like flow),
# Goldstone modes develop an effective mass proportional to the
# expansion rate. Volovik Paper 05 eq (4.4):
#   Delta_Lambda / Lambda_0 ~ H/E_Planck * (E_Planck/Delta)^2
# The remnant from expansion is proportional to H, with the
# microscopic prefactor determined by the BCS parameters.

print(f"\n  7f: Composite de Sitter mass (final result)")
print(f"    m_eff = (3/2)*H_0*sqrt(Omega_Lambda)")
print(f"    = {m_dS:.4e} GeV")
print(f"    = {m_dS_MKK:.4e} M_KK")
print(f"    log10(m/M_KK) = {log_m_dS:.2f}")
print(f"    This is the PHYSICAL Goldstone mass on the Hubble horizon.")
print(f"    It is parameter-free: H and Omega_Lambda are observed.")


# ============================================================
# SECTION 8: Power Spectrum from Friedmann-Goldstone
# ============================================================
# The Goldstone power spectrum on the fabric, including Hubble mass:
#   P(K) ~ 1 / (K^2 + m_eff^2 / (rho_s * c_G^2))
#
# Using m_eff = (3/2)*H:
#   mu_eff^2 = m_eff^2 / (rho_s * c_G^2)
#            = (9/4)*H^2 / (rho_s * J/rho_s)
#            = (9/4)*H^2 / J
#
# The spectral tilt from this mass gap:
#   n_s - 1 = d ln P / d ln K |_{K=K_pivot}
#           = -2 * mu_eff^2 / (K_pivot^2 + mu_eff^2)
#
# For mu_eff << K_pivot: n_s - 1 ~ -2*mu_eff^2/K_pivot^2
# For mu_eff >> K_pivot: n_s - 1 ~ -2 (maximum red tilt)

print("\n" + "=" * 78)
print("SECTION 8: Power Spectrum Tilt from Friedmann-Goldstone")
print("=" * 78)

# mu_eff^2 in M_KK^2
mu_eff_sq = m_dS_MKK**2 / c_goldstone_sq  # dimensionless ratio

print(f"\n  mu_eff^2 = m_dS^2 / (J/rho_s) = {mu_eff_sq:.4e} M_KK^2")
print(f"  K_min(fabric)^2 = {K_min_fabric**2:.4f} M_KK^2")
print(f"  mu_eff / K_min = {np.sqrt(mu_eff_sq) / K_min_fabric:.4e}")

# n_s from O-Z with Hubble mass gap
# Using the PHYSICAL mapping (l_cell = 450 Mpc):
K_pivot_fabric = k_pivot_Mpc * l_cell_Mpc / (2 * PI)  # dimensionless mode number
# Actually K_pivot in fabric units:
# K_pivot_fabric = k_pivot_Mpc * (N_cells * l_cell_Mpc) / (2*pi) * (2*pi/N_cells/l_cell_MKK * l_cell_MKK)
# Simpler: K in Mpc^{-1} maps to K_MKK via K_MKK = K_Mpc * l_cell_Mpc * l_cell_MKK / l_cell_Mpc
# Wait — the mapping is: n = K_Mpc * L_Mpc / (2*pi)
# K_MKK = 2*pi*n / (N_cells * l_cell) = K_Mpc * (L_Mpc / (N_cells * l_cell))
# But this is just the ratio of physical to M_KK lengths:
# K_MKK / K_Mpc = L_fabric_Mpc / L_fabric_MKK * (M_KK^{-1} to Mpc conversion)

# Actually, the mode number n is what matters:
# n = k_Mpc * L_Mpc / (2*pi) = 0.05 * 14400 / (2*pi) = 114.6
# But N_cells = 32, so n_max = 16. The pivot is at n ~ 115, WAY above the zone boundary.
n_pivot = k_pivot_Mpc * L_fabric_Mpc / (2 * PI)
print(f"\n  Mode number at CMB pivot: n = {n_pivot:.1f}")
print(f"  Zone boundary: n_max = {N_cells//2}")

if n_pivot > N_cells // 2:
    print(f"  CMB PIVOT IS ABOVE BRILLOUIN ZONE by {n_pivot / (N_cells//2):.1f}x")
    print(f"  This means the 32-cell lattice CANNOT resolve the CMB pivot.")
    print(f"  The Goldstone power spectrum from the Josephson network does not")
    print(f"  extend to CMB scales. The O-Z correlation function describes")
    print(f"  SUPER-HUBBLE correlations, not sub-Hubble CMB modes.")
    pivot_resolved = False
else:
    pivot_resolved = True
    K_piv_fabric = 2 * PI * n_pivot / (N_cells * l_cell)  # M_KK
    ns_from_mass = 1 - 2 * mu_eff_sq / (K_piv_fabric**2 + mu_eff_sq)
    print(f"  n_s = 1 - 2*mu^2/(K^2+mu^2) = {ns_from_mass:.6f}")

# Even though pivot is outside BZ, the de Sitter mass still generates
# a universal tilt for ANY Goldstone mode:
print(f"\n  --- Universal tilt from de Sitter mass ---")
for n_mode in [1, 2, 4, 8, 16]:
    if n_mode >= N_cells:
        continue
    K_mode = 2 * PI * n_mode / (N_cells * l_cell)
    ns_mode = 1 - 2 * mu_eff_sq / (K_mode**2 + mu_eff_sq)
    print(f"    n={n_mode:3d}: K={K_mode:.4f}, n_s = {ns_mode:.12f}, (1-n_s) = {1-ns_mode:.4e}")


# ============================================================
# SECTION 9: The Structural Result
# ============================================================
# The de Sitter mass m = (3/2)*H gives:
#   log10(m/M_KK) ~ -58.8
# This is WITHIN the gate window [-60, -30].
#
# However, the tilt it produces is infinitesimal:
#   1 - n_s ~ 2 * (H/M_KK)^2 / J ~ 10^{-116}
# versus the observed 1 - n_s = 0.035.
#
# The structural reason: the fabric modes oscillate at M_KK frequency,
# while H ~ 10^{-58} M_KK. The Hubble mass is utterly negligible compared
# to the Josephson energy. The mode equation:
#   omega_n^2 + m_H^2 = omega_n^2 * (1 + 10^{-116})
#
# This is the 84-order crisis expressed as a spectral tilt:
# To get 1 - n_s = 0.035, we need m^2/J ~ K^2 at the pivot.
# The Hubble mass gives m^2/J ~ 10^{-116}, missing by 114 orders.

print("\n" + "=" * 78)
print("SECTION 9: Structural Result")
print("=" * 78)

# The n_s tilt from Hubble mass at the LOWEST fabric mode:
ns_tilt_lowest = 2 * mu_eff_sq / (K_min_fabric**2 + mu_eff_sq)
print(f"\n  Tilt at lowest fabric mode (n=1):")
print(f"    1 - n_s = {ns_tilt_lowest:.4e}")
print(f"    Observed: 1 - n_s = 0.035")
print(f"    Shortfall: {0.035 / ns_tilt_lowest:.4e}")
print(f"    log10 shortfall: {np.log10(0.035 / ns_tilt_lowest):.1f} orders")

# The required mass for n_s = 0.965 at the lowest fabric mode:
# 1 - n_s = 2*mu^2/(K^2+mu^2) => mu^2 = K^2*(1-n_s)/(2-(1-n_s)) = K^2*0.035/1.965
target_ns = 0.965
delta_ns = 1 - target_ns  # 0.035
mu_required_sq = K_min_fabric**2 * delta_ns / (2 - delta_ns)
m_required_from_ns = np.sqrt(mu_required_sq * c_goldstone_sq) * M_KK  # GeV
m_required_MKK_ns = np.sqrt(mu_required_sq * c_goldstone_sq)

print(f"\n  Required mass for n_s = {target_ns}:")
print(f"    mu_req^2 = K_min^2 * {delta_ns}/{2-delta_ns} = {mu_required_sq:.6f} M_KK^2")
print(f"    m_req = {m_required_MKK_ns:.4f} M_KK = {m_required_from_ns:.4e} GeV")
print(f"    log10(m_req/M_KK) = {np.log10(m_required_MKK_ns):.4f}")
print(f"    This is O(M_KK) — a LATTICE-SCALE mass, not cosmological.")
print(f"    The required mass for n_s from O-Z at fabric K is M_KK-scale.")
print(f"    But from S48, ALL equilibrium routes give m ~ M_KK (confirmed here).")


# ============================================================
# SECTION 10: Comprehensive Mass Table
# ============================================================

print("\n" + "=" * 78)
print("SECTION 10: Complete Mass Inventory")
print("=" * 78)

mass_table = {
    'de Sitter (3/2)H':     (m_dS_MKK, m_dS, 'parameter-free'),
    'Horizon c_G*K_H':      (m_horizon_MKK, m_horizon, 'parameter-free'),
    'q-theory relax':       (m_q, m_q * M_KK, 'parameter-free'),
    'GH thermal':           (m_GH, m_GH * M_KK, 'lambda from J/rho_s'),
    'O-Z req (n=1)':        (m_required_MKK_ns, m_required_from_ns, 'n_s = 0.965'),
    'CMB transit H_fold':   (m_transit_MKK, m_transit, 'S38 H_fold'),
    'CMB epoch H(1100)':    (m_CMB_MKK, m_CMB, 'LCDM H(z)'),
    'BBN epoch H(4e8)':     (m_BBN_MKK, m_BBN, 'LCDM H(z)'),
}

print(f"\n  {'Route':<25s} {'m/M_KK':>14s} {'m (GeV)':>14s} {'log10(m/MKK)':>14s} {'In gate?':>10s} {'Notes'}")
print(f"  {'-'*25} {'-'*14} {'-'*14} {'-'*14} {'-'*10} {'-'*20}")

gate_pass_routes = []
for name, (m_mkk, m_gev, notes) in mass_table.items():
    if m_mkk > 0:
        log_m = np.log10(m_mkk)
        in_gate = gate_lo <= log_m <= gate_hi
        marker = "YES" if in_gate else "NO"
        if in_gate:
            gate_pass_routes.append((name, m_mkk, log_m))
        print(f"  {name:<25s} {m_mkk:14.4e} {m_gev:14.4e} {log_m:14.2f} {marker:>10s} {notes}")
    else:
        print(f"  {name:<25s} {'0':>14s} {'0':>14s} {'---':>14s} {'FAIL':>10s} {notes}")

print(f"\n  Routes in gate window [{gate_lo}, {gate_hi}]: {len(gate_pass_routes)}")
for name, m_val, log_val in gate_pass_routes:
    print(f"    {name}: log10 = {log_val:.2f}")


# ============================================================
# SECTION 11: GATE VERDICT
# ============================================================

print("\n" + "=" * 78)
print("GATE VERDICT: FRIEDMANN-GOLDSTONE-49")
print("=" * 78)

# Three masses fall in the gate window: de Sitter, horizon, q-theory relax
# All are parameter-free (computed from H_0, Omega_Lambda, J_C2, rho_s, M_Pl)
# The de Sitter mass is the cleanest: m = (3/2)*H * sqrt(Omega_Lambda)

if len(gate_pass_routes) > 0:
    best = gate_pass_routes[0]
    # Check if the mass produces the observed n_s tilt
    # Required: 1 - n_s ~ 2*m^2/(J*K_pivot^2) ~ O(0.035)
    ns_produced = 2 * (m_dS_MKK**2 / c_goldstone_sq) / K_min_fabric**2
    ns_shortfall = 0.035 / ns_produced if ns_produced > 0 else float('inf')

    print(f"\n  RESULT: {len(gate_pass_routes)} routes produce masses in the gate window.")
    print(f"  Best route: {best[0]}, log10(m/M_KK) = {best[2]:.2f}")
    print(f"\n  BUT: the mass is too small to produce the observed n_s tilt.")
    print(f"    1 - n_s produced: {ns_produced:.4e}")
    print(f"    1 - n_s observed: 0.035")
    print(f"    Shortfall: {ns_shortfall:.4e} ({np.log10(ns_shortfall):.0f} orders)")
    print(f"\n  The de Sitter mass IS in the gate window [{gate_lo}, {gate_hi}]")
    print(f"  but it is phenomenologically useless for the n_s tilt.")
    print(f"  The scale crisis is not a mass crisis — it is a COUPLING crisis:")
    print(f"  the Goldstone has a mass, but the fabric modes are too stiff")
    print(f"  for that mass to affect their dispersion.")

    # Verdict determination:
    # The gate says PASS if m/M_KK in [10^{-60}, 10^{-30}] with no free parameters.
    # The de Sitter mass satisfies this literally. It IS in the window.
    # But it's phenomenologically inert — the n_s shortfall is 114 orders.
    # This is an INFO: computable, in range, but cannot do what was hoped.

    verdict = "INFO"
    detail = (f"m_dS = (3/2)*H_dS = {m_dS:.2e} GeV = {m_dS_MKK:.2e} M_KK "
              f"(log10 = {log_m_dS:.2f}, IN gate). "
              f"But n_s tilt = {ns_produced:.2e}, shortfall {ns_shortfall:.2e} "
              f"({np.log10(ns_shortfall):.0f} OOM). "
              f"Mass exists but fabric too stiff for phenomenology.")

else:
    verdict = "FAIL"
    detail = "No route produces m/M_KK in gate window"

print(f"\n  VERDICT: {verdict}")
print(f"  Detail: {detail}")


# ============================================================
# SECTION 12: Volovik Interpretation
# ============================================================

print("\n" + "=" * 78)
print("SECTION 12: Volovik Interpretation")
print("=" * 78)

print("""
  The superfluid vacuum analogy illuminates the result:

  1. MASS EXISTS: In 3He superfluid, the Goldstone boson (second sound
     in 3He-B, orbital waves in 3He-A) acquires an effective mass from
     the expansion of the container. The analog here: m_dS = (3/2)*H.
     This is parameter-free and lands at log10(m/M_KK) = {:.1f}.

  2. MASS IS IRRELEVANT: The fabric modes oscillate at omega ~ sqrt(J/rho_s)
     ~ O(M_KK). The Hubble mass is H ~ 10^{{-58}} M_KK. The ratio
     m_H/omega ~ 10^{{-58}} is like adding 10^{{-58}} mK temperature
     to a superfluid at 1 mK — the perturbation is negligible.

  3. THE REAL DIAGNOSIS: The scale crisis is not "how to generate the mass"
     but "why the fabric stiffness J ~ M_KK is the wrong stiffness for CMB."
     In 3He, the superfluid stiffness rho_s is set by the gap Delta and
     the Fermi velocity v_F. Both are microscopic. To get a mass at the
     Hubble scale, one needs a stiffness at the Planck scale — but the
     fabric stiffness IS microscopic (M_KK scale). There is no mechanism
     in BCS theory or q-theory that makes J ~ H.

  4. Q-THEORY PERSPECTIVE: Volovik Papers 05, 15-16 show that the CC is
     zero in equilibrium and H-dependent out of equilibrium. The SAME logic
     applied to the Goldstone mass: m = 0 in equilibrium (Goldstone theorem),
     m ~ H out of equilibrium (de Sitter). Both are correct. Both are useless
     for the tilt: the CC is {:.0e} not {:.0e}, and the Goldstone mass
     is {:.0e} not {:.0e} (in M_KK^4 and M_KK units respectively).

  5. STRUCTURAL IDENTITY CONFIRMED: The mass problem IS the CC problem.
     Both require the M_KK / H_0 hierarchy. The de Sitter mass gives the
     RIGHT SCALE (10^{{-58}} M_KK ~ H_0) but the WRONG EFFECT (negligible
     compared to J). The CC gives the RIGHT SCALE (H^2*M_Pl^2) but the
     WRONG RESIDUAL (tiny compared to M_KK^4). Same crisis, same origin.

  6. WHAT BREAKS: The assumption that the Goldstone mass controls n_s
     through an Ornstein-Zernike spectrum P(K) ~ 1/(K^2 + m^2). The
     fabric modes are ALL at K ~ M_KK. The CMB modes at K ~ 10^{{-58}} M_KK
     are not Goldstone modes on the fabric — they are something else.
     The n_s tilt must come from a mechanism OUTSIDE the Josephson network.
""".format(log_m_dS, rho_Lambda_obs, Lambda_obs_MP4, m_dS_MKK, 3.2e-56))


# ============================================================
# Save results and plot
# ============================================================

np.savez('s49_friedmann_goldstone.npz',
    # De Sitter effective mass
    m_dS_MKK=m_dS_MKK,
    m_dS_GeV=m_dS,
    H_dS_MKK=H_dS_MKK,
    H_dS_GeV=H_dS,
    log10_m_dS_MKK=log_m_dS,

    # Horizon mass
    m_horizon_MKK=m_horizon_MKK,
    m_horizon_GeV=m_horizon,

    # q-theory relaxation mass
    m_qtheory_MKK=m_q,
    m_qtheory_GeV=m_q * M_KK,

    # GH thermal mass
    m_GH_MKK=m_GH,
    m_GH_GeV=m_GH * M_KK,

    # Transit mass
    m_transit_MKK=m_transit_MKK,
    m_transit_GeV=m_transit,

    # CMB/BBN epoch masses
    m_CMB_MKK=m_CMB_MKK,
    m_CMB_GeV=m_CMB,
    m_BBN_MKK=m_BBN_MKK,
    m_BBN_GeV=m_BBN,

    # Required mass for n_s
    m_required_ns_MKK=m_required_MKK_ns,
    m_required_ns_GeV=m_required_from_ns,

    # Scale crisis
    ns_tilt_from_Hubble=ns_tilt_lowest,
    ns_shortfall_orders=np.log10(0.035 / ns_tilt_lowest) if ns_tilt_lowest > 0 else 999,

    # Goldstone parameters
    c_goldstone_sq=c_goldstone_sq,
    c_goldstone=c_goldstone,
    J_C2=J_C2,
    rho_s_C2=rho_s_C2,
    K_min_fabric=K_min_fabric,
    K_max_fabric=K_max_fabric,
    omega_min=omega_min,
    omega_max=omega_max,

    # Scale mapping
    L_fabric_Mpc=L_fabric_Mpc,
    l_cell_Mpc=l_cell_Mpc,
    K_min_fabric_Mpc=K_min_fabric_Mpc,
    K_max_fabric_Mpc=K_max_fabric_Mpc,
    n_pivot=n_pivot,
    pivot_in_BZ=pivot_resolved,

    # GGE data
    rho_s_GGE_fraction=rho_s_GGE_fraction,
    S_gge=S_gge,

    # Gate
    gate_name=np.array(['FRIEDMANN-GOLDSTONE-49']),
    gate_verdict=np.array([verdict]),
    gate_detail=np.array([detail]),
)

print(f"\n  Saved: s49_friedmann_goldstone.npz")


# ============================================================
# PLOT
# ============================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('FRIEDMANN-GOLDSTONE-49: De Sitter Effective Mass on Josephson Network',
             fontsize=13, fontweight='bold')

# Panel 1: Mass hierarchy
ax1 = axes[0, 0]
masses_log = {
    'H_fold\n(transit)': np.log10(m_transit_MKK),
    'O-Z req\n(n_s=0.965)': np.log10(m_required_MKK_ns),
    'H(BBN)': np.log10(m_BBN_MKK),
    'H(CMB)': np.log10(m_CMB_MKK),
    'GH thermal': log_m_7e,
    'q-theory': log_m_7d,
    'Horizon\nc_G*K_H': np.log10(m_horizon_MKK),
    'de Sitter\n(3/2)*H': log_m_dS,
}
names = list(masses_log.keys())
values = list(masses_log.values())
colors = ['red' if v > gate_hi else ('green' if gate_lo <= v <= gate_hi else 'blue') for v in values]

bars = ax1.barh(range(len(names)), values, color=colors, alpha=0.7, edgecolor='black')
ax1.axvline(x=gate_lo, color='green', linestyle='--', alpha=0.5, label=f'Gate: [{gate_lo},{gate_hi}]')
ax1.axvline(x=gate_hi, color='green', linestyle='--', alpha=0.5)
ax1.axvspan(gate_lo, gate_hi, alpha=0.1, color='green')
ax1.set_yticks(range(len(names)))
ax1.set_yticklabels(names, fontsize=8)
ax1.set_xlabel('log10(m / M_KK)')
ax1.set_title('Mass Hierarchy (green = in gate)')
ax1.set_xlim(-160, 10)
ax1.legend(fontsize=7)

# Panel 2: Goldstone dispersion with Hubble mass
ax2 = axes[0, 1]
K_cont = np.linspace(0.01, K_max_fabric, 500)
omega_cont = np.sqrt(c_goldstone_sq * K_cont**2)
omega_with_H = np.sqrt(c_goldstone_sq * K_cont**2 + m_dS_MKK**2)

ax2.plot(K_cont, omega_cont, 'b-', label=r'$\omega^2 = c_G^2 K^2$ (massless)', linewidth=2)
ax2.plot(K_cont, omega_with_H, 'r--', label=r'$\omega^2 = c_G^2 K^2 + m_{dS}^2$', linewidth=2)
ax2.scatter(K_n_ring, np.sqrt(omega_sq_ring), c='blue', s=20, zorder=5,
            label=f'Lattice modes (N={N_cells})')
ax2.set_xlabel('K (M_KK)')
ax2.set_ylabel(r'$\omega$ (M_KK)')
ax2.set_title('Goldstone Dispersion')
ax2.legend(fontsize=7)
ax2.set_xlim(0, K_max_fabric * 1.1)
# The Hubble mass is invisible at this scale — note it
ax2.text(0.5, 0.05, f'm_dS = {m_dS_MKK:.1e} M_KK\n(invisible at this scale)',
         transform=ax2.transAxes, fontsize=8, va='bottom', ha='center',
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.8))

# Panel 3: Effective mass vs redshift
ax3 = axes[1, 0]
ax3.loglog(1 + z_scan, m_scan_MKK, 'b-', linewidth=2, label=r'$m_{eff}(z) = \frac{3}{2}H(z)$')
ax3.axhline(y=omega_min, color='red', linestyle='--', label=r'$\omega_{min}$ (fabric)')
ax3.axhline(y=omega_max, color='red', linestyle='-.', label=r'$\omega_{max}$ (fabric)')
ax3.axhline(y=m_required_MKK_ns, color='green', linestyle=':', linewidth=2,
            label=f'Required for n_s=0.965')
ax3.axvline(x=1+z_CMB, color='gray', linestyle=':', alpha=0.5)
ax3.text(1+z_CMB, 1e-50, 'CMB', fontsize=8, rotation=90, va='bottom')
ax3.set_xlabel('1 + z')
ax3.set_ylabel('m_eff / M_KK')
ax3.set_title('Effective Mass vs Redshift')
ax3.legend(fontsize=7, loc='lower right')
ax3.set_ylim(1e-60, 1e5)
ax3.set_xlim(1, 1e11)

# Panel 4: Scale crisis diagram
ax4 = axes[1, 1]
# Show the O-Z spectrum P(K) for different mass scales
K_oz = np.logspace(-60, 2, 1000)  # M_KK units
P_massless = 1.0 / K_oz**2

# With de Sitter mass
mu_dS = m_dS_MKK**2 / c_goldstone_sq
P_dS = 1.0 / (K_oz**2 + mu_dS)

# With required mass
mu_req = m_required_MKK_ns**2 / c_goldstone_sq
P_req = 1.0 / (K_oz**2 + mu_req)

ax4.loglog(K_oz, P_massless / P_massless[0], 'b-', label='Massless: n_s = 1', linewidth=2)
ax4.loglog(K_oz, P_dS / P_dS[0], 'r--', label=f'de Sitter: m = {m_dS_MKK:.1e}', linewidth=1.5)
ax4.loglog(K_oz, P_req / P_req[0], 'g:', label=f'Required: m = {m_required_MKK_ns:.2f}', linewidth=2)

# Mark fabric mode range
ax4.axvspan(K_min_fabric, K_max_fabric, alpha=0.15, color='orange', label='Fabric modes')
ax4.axvline(x=k_pivot_MKK, color='purple', linestyle='--', alpha=0.5, label='CMB pivot')

ax4.set_xlabel('K (M_KK)')
ax4.set_ylabel('P(K) / P(K_min) [normalized]')
ax4.set_title('Scale Crisis: O-Z Spectrum')
ax4.legend(fontsize=7, loc='lower left')
ax4.set_xlim(1e-62, 1e3)
ax4.set_ylim(1e-10, 1e5)

plt.tight_layout()
plt.savefig('s49_friedmann_goldstone.png', dpi=150, bbox_inches='tight')
print(f"  Saved: s49_friedmann_goldstone.png")
print("=" * 78)
