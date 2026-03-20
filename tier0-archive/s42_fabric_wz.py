#!/usr/bin/env python3
"""
s42_fabric_wz.py — Fabric-Collective Dark Energy w(z) (W-Z-42 REDO)

Einstein-Theorist, Session 42 (Redo).

CRITICAL ERROR IN OLD CALCULATION: s42_dark_energy_wz.py treated tau as a
single homogeneous scalar field, giving w = -1 trivially. That was the energy
of ONE ATOM. This script computes the thermodynamics of the CRYSTAL.

THE FABRIC HAS SPATIAL STRUCTURE:
- 32 Voronoi cells (from W1-2 giant_voronoi)
- Domain walls at cell boundaries where nabla(tau) != 0
- Gradient stiffness Z = 74,731 (from W1-1)
- Modulus mass m_tau = 2.062 M_KK (from W2-1)

THE TOTAL ENERGY DENSITY:
  rho_fabric = rho_bulk + rho_gradient + rho_walls

THE EQUATION OF STATE (each component):
  w_bulk = -1 (cosmological constant from frozen V_eff)
  w_gradient = -1/3 (gradient energy = curvature-like, p = -(1/3)*rho)
  w_walls = -2/3 (domain wall network in 3D)

  w_eff = -1 + (2/3)*f_gradient + (1/3)*f_walls

where f_gradient = rho_gradient/rho_total, f_walls = rho_walls/rho_total.

RESULT: The wall thickness (1/m_tau ~ 0.49 M_KK^{-1}) and BCS coherence
length (xi_BCS ~ 1.1 M_KK^{-1}) are at the KK scale: 10^{-49} to 10^{-59} Mpc.
The cell radius is ~4500 Mpc. The volume fraction is 10^{-52} to 10^{-63}.
The fabric correction to w is STRUCTURALLY NEGLIGIBLE:

  |w + 1| ~ 10^{-53} to 10^{-63}

This is a STRUCTURAL result: it follows from the scale hierarchy M_KK >> H_0.
The fabric IS there. It just cannot be seen in w(z).
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ========================================================================
# 1. LOAD UPSTREAM DATA
# ========================================================================
gs = np.load('tier0-computation/s42_gradient_stiffness.npz', allow_pickle=True)
fd = np.load('tier0-computation/s42_fabric_dispersion.npz', allow_pickle=True)
vor = np.load('tier0-computation/s42_giant_voronoi.npz', allow_pickle=True)
td = np.load('tier0-computation/s42_tau_dyn_reopening.npz', allow_pickle=True)
sf = np.load('tier0-computation/s36_sfull_tau_stabilization.npz', allow_pickle=True)
sd = np.load('tier0-computation/s41_constants_vs_tau.npz', allow_pickle=True)

# Extract quantities
tau_fold = 0.190
Z_fold = float(gs['Z_fold'].flat[0])
dV_fold = float(gs['dS_fold'].flat[0])
d2V_fold = float(gs['d2S_fold'].flat[0])
V_fold = float(gs['S_fold'].flat[0])   # S_full(0.190)

m_tau = float(fd['m_tau'].flat[0])
v_B2 = float(fd['v_th_B2'].flat[0])   # B2 thermal velocity

N_cells = int(vor['N_cells'])
R_obs_Mpc = float(vor['R_obs'])  # 14250 Mpc comoving

tau_Sfull = sf['tau_combined']
S_full = sf['S_full']

# Seeley-DeWitt at fold (from S41)
tau_vals = sd['tau_values']
idx_fold = np.argmin(np.abs(tau_vals - tau_fold))
a0_fold = float(sd['a0_cutoff0'][idx_fold])
a2_fold = float(sd['a2_cutoff0'][idx_fold])
a4_fold = float(sd['a4_cutoff0'][idx_fold])

# BCS data from S35/S38
from canonical_constants import E_cond, E_exc as E_exc_total, n_pairs, M_Pl_unreduced as M_Planck_GeV
Delta_B3 = 0.176  # BCS gap in B3 sector (M_KK, from S38)

# Physical constants
from canonical_constants import H_0_inv_s as H_0  # s^{-1} (67.4 km/s/Mpc)
## M_Planck_GeV imported from canonical_constants above
from canonical_constants import GeV_to_inv_s as GeV_to_invs  # 1 GeV -> s^{-1}
hbar_c_GeV_fm = 0.1973269804  # GeV*fm
Mpc_to_fm = 3.0857e38    # fm per Mpc
Lambda_obs_MP4 = 2.888e-122  # observed CC in M_P^4

# M_KK conventions
MKK_dict = {
    'M_KK = 10^9 GeV (Conv A)': 1e9,
    'M_KK = 10^{13} GeV (Conv C)': 1e13,
    'M_KK = 10^{16} GeV (GUT)': 1e16,
    'M_KK = M_Planck': M_Planck_GeV,
}

print("=" * 76)
print("W-Z-42 (REDO): FABRIC-COLLECTIVE DARK ENERGY w(z)")
print("Einstein-Theorist, Session 42")
print("REPLACES: single-tau computation that gave w = -1 trivially.")
print("=" * 76)

# ========================================================================
# 2. VORONOI CELL GEOMETRY
# ========================================================================
print("\n--- 32-CELL VORONOI GEOMETRY ---")

V_obs = (4.0 / 3.0) * np.pi * R_obs_Mpc**3  # Mpc^3
V_cell = V_obs / N_cells
R_cell = (3.0 * V_cell / (4.0 * np.pi))**(1.0/3.0)

# For a Voronoi tessellation, each cell has ~14 faces (Kelvin/Weaire-Phelan)
# Each face shared between 2 cells
# Total wall area: A = N * n_faces * <A_face> / 2
# For roughly spherical cells: sum of face areas ~ 4*pi*R_cell^2
# So A_total ~ N * 4*pi*R_cell^2 / 2 = 2*pi*N*R_cell^2
n_faces_eff = 14  # typical Voronoi
A_cell = 4.0 * np.pi * R_cell**2  # surface area of equivalent sphere
A_total = N_cells * A_cell / 2.0   # total wall area (shared faces counted once)

print(f"  N_cells = {N_cells}")
print(f"  R_obs = {R_obs_Mpc:.0f} Mpc (comoving)")
print(f"  V_obs = {V_obs:.4e} Mpc^3")
print(f"  V_cell = {V_cell:.4e} Mpc^3")
print(f"  R_cell = {R_cell:.1f} Mpc")
print(f"  A_total = 2*pi*N*R_cell^2 = {A_total:.4e} Mpc^2")

# ========================================================================
# 3. WALL THICKNESS: THREE ESTIMATES
# ========================================================================
print("\n--- DOMAIN WALL THICKNESS ---")

# Estimate A: Bare mass scale (1/m_tau in M_KK^{-1})
delta_wall_A_MKK = 1.0 / m_tau  # M_KK^{-1}

# Estimate B: BCS coherence length (xi_BCS = v_F / (pi * Delta))
xi_BCS = v_B2 / (np.pi * Delta_B3)  # M_KK^{-1}

# Estimate C: Kibble-Zurek correlation length at freeze-out
# BCS: nu=1/2, z_KZ=2. tau_Q ~ 0.12, tau_0 ~ 1.27 M_KK^{-1} (from S38)
tau_Q = 0.12
tau_0_BCS = 1.27
nu_BCS = 0.5
z_KZ = 2.0
xi_0 = 1.0 / m_tau
xi_ratio = (tau_Q / tau_0_BCS)**(nu_BCS / (1 + nu_BCS * z_KZ))
xi_KZ = xi_0 * xi_ratio

print(f"  Estimate A (bare mass): delta_wall = 1/m_tau = {delta_wall_A_MKK:.4f} M_KK^{{-1}}")
print(f"  Estimate B (BCS coherence): xi_BCS = v_B2/(pi*Delta) = {xi_BCS:.4f} M_KK^{{-1}}")
print(f"  Estimate C (Kibble-Zurek): xi_KZ = xi_0*(tau_Q/tau_0)^{{nu/(1+nu*z)}} = {xi_KZ:.4f} M_KK^{{-1}}")
print()

# Use the LARGEST estimate (BCS coherence) as the physical wall thickness
# This is the most favorable case for a detectable w correction
delta_wall_MKK = max(delta_wall_A_MKK, xi_BCS, xi_KZ)
print(f"  Using LARGEST estimate: delta_wall = {delta_wall_MKK:.4f} M_KK^{{-1}}")
print(f"    (most favorable for detecting w != -1)")

# ========================================================================
# 4. delta_tau BETWEEN CELLS: THREE ESTIMATES
# ========================================================================
print("\n--- TAU VARIATION BETWEEN CELLS ---")

# Estimate 1: Quantum fluctuations during BCS transit
# H_BCS ~ 0.014 M_KK (Session 29)
H_BCS = 0.014  # M_KK
delta_tau_quantum = H_BCS / (2.0 * np.pi * np.sqrt(Z_fold))
print(f"  Estimate 1 (quantum): delta_tau = H_BCS/(2*pi*sqrt(Z)) = {delta_tau_quantum:.6e}")
print(f"    delta_tau/tau = {delta_tau_quantum/tau_fold:.6e}")

# Estimate 2: Kibble-Zurek freeze-out
# Each causal domain of size xi_KZ gets a random tau value.
# The RMS variation between neighboring domains:
# delta_tau_KZ ~ 1/sqrt(Z * xi_KZ^3)  (from thermal fluctuation in 3D)
# At T_BCS (the transition temperature), the field fluctuation per domain:
T_BCS = 0.004  # Approximate BCS T_c in M_KK (from S38 instanton, T at Delta minimum)
delta_tau_KZ = np.sqrt(T_BCS / (Z_fold * xi_KZ**3))
print(f"  Estimate 2 (Kibble-Zurek): delta_tau_KZ = sqrt(T/Z*xi^3) = {delta_tau_KZ:.6e}")
print(f"    delta_tau/tau = {delta_tau_KZ/tau_fold:.6e}")

# Estimate 3: FIRAS upper bound
delta_tau_FIRAS = 3e-6 * tau_fold
print(f"  Estimate 3 (FIRAS bound): delta_tau < 3e-6 * tau = {delta_tau_FIRAS:.6e}")
print(f"    delta_tau/tau = 3e-6")

# Use the LARGEST physical estimate and the FIRAS bound separately
delta_tau_phys = max(delta_tau_quantum, delta_tau_KZ)
print(f"\n  Physical estimate: delta_tau = {delta_tau_phys:.6e}")
print(f"  FIRAS upper bound: delta_tau = {delta_tau_FIRAS:.6e}")
print(f"  FIRAS / physical = {delta_tau_FIRAS / delta_tau_phys:.1f}x")

# ========================================================================
# 5. ENERGY BUDGET: WALL + GRADIENT vs BULK
# ========================================================================
print("\n" + "=" * 76)
print("ENERGY BUDGET OF THE FABRIC")
print("=" * 76)

results = {}

for label, MKK_GeV in MKK_dict.items():
    print(f"\n  --- {label} ---")

    MKK_inv_fm = MKK_GeV / hbar_c_GeV_fm  # M_KK in fm^{-1}

    # Convert wall thickness to Mpc
    delta_wall_fm = delta_wall_MKK / MKK_inv_fm
    delta_wall_Mpc = delta_wall_fm / Mpc_to_fm

    # Wall volume fraction
    V_walls_Mpc3 = A_total * delta_wall_Mpc
    f_walls = V_walls_Mpc3 / V_obs

    # Gradient energy at the wall:
    # rho_gradient_wall = (1/2) * Z * (delta_tau / delta_wall)^2  in M_KK^4
    # Use BOTH delta_tau estimates
    for dtau_label, delta_tau in [("Physical", delta_tau_phys), ("FIRAS", delta_tau_FIRAS)]:
        grad_tau = delta_tau / delta_wall_MKK  # gradient in M_KK units
        rho_grad_wall = 0.5 * Z_fold * grad_tau**2  # M_KK^4

        # The gradient energy is concentrated in the wall volume
        # Average over full volume: rho_gradient_avg = rho_grad_wall * f_walls
        rho_grad_avg = rho_grad_wall * f_walls

        # Wall energy density:
        # The wall has surface tension sigma = int dz [Z/2 (d tau/dz)^2 + V(tau) - V_fold]
        # For a kink profile: sigma ~ (2/3) * delta_tau * sqrt(Z * V'') ~ delta_tau * m_tau * Z
        # sigma has units M_KK^3
        sigma_wall = delta_tau * m_tau * Z_fold  # rough: M_KK^3

        # Wall energy density averaged: rho_walls_avg = sigma * A_total / V_obs (per physical volume)
        # But sigma is in M_KK^3 and A/V is in Mpc^{-1}
        # Need to be careful with units.
        # Actually: rho_walls = sigma_wall * delta(x_wall) integrated over wall width = sigma_wall
        # Averaged over cell volume: rho_walls_avg = sigma_wall * A_cell / V_cell (in M_KK^4 * Mpc^{-1})
        # This is a units mismatch. Let me be more careful.
        #
        # The correct approach: EVERYTHING in M_KK^4 units, compute fractional contributions.
        #
        # rho_bulk = V_fold [M_KK^4], filling the whole volume.
        # rho_gradient (at wall) = (1/2) Z (grad tau)^2 [M_KK^4], in wall volume only.
        # rho_walls (domain wall tension) = surface tension sigma [M_KK^3] / delta_wall [M_KK^{-1}]
        #   = sigma * m_tau [M_KK^4], in wall volume.
        # Actually, for a domain wall of thickness delta_wall, the integrated energy per unit area
        # is sigma [M_KK^3], and the volume energy density within the wall is sigma/delta_wall [M_KK^4].

        # The energy FRACTIONS are:
        # f_gradient = (rho_grad_wall / V_fold) * f_walls  (gradient energy fraction)
        # f_wall_tension = (sigma_wall / (delta_wall_MKK * V_fold)) * f_walls

        f_gradient = (rho_grad_wall / V_fold) * f_walls
        sigma_vol = sigma_wall / delta_wall_MKK  # energy density in wall [M_KK^4]
        f_wall_tension = (sigma_vol / V_fold) * f_walls

        if dtau_label == "Physical":
            print(f"    [{dtau_label} delta_tau = {delta_tau:.3e}]")
            print(f"      delta_wall = {delta_wall_Mpc:.3e} Mpc")
            print(f"      f_walls (volume) = {f_walls:.3e}")
            print(f"      rho_grad (at wall) = {rho_grad_wall:.3e} M_KK^4")
            print(f"      rho_grad / V_fold = {rho_grad_wall/V_fold:.3e}")
            print(f"      f_gradient = {f_gradient:.3e}")
            print(f"      sigma_wall = {sigma_wall:.3e} M_KK^3")
            print(f"      f_wall_tension = {f_wall_tension:.3e}")

        if dtau_label == "FIRAS":
            print(f"    [{dtau_label} delta_tau = {delta_tau:.3e}]")
            print(f"      f_gradient = {f_gradient:.3e}")
            print(f"      f_wall_tension = {f_wall_tension:.3e}")

        if label == 'M_KK = 10^9 GeV (Conv A)' and dtau_label == 'FIRAS':
            results['f_gradient_best'] = f_gradient
            results['f_walls_best'] = f_wall_tension
            results['f_walls_vol_best'] = f_walls
            results['delta_wall_Mpc_best'] = delta_wall_Mpc

    results[label] = {
        'delta_wall_Mpc': delta_wall_Mpc,
        'f_walls': f_walls,
    }

# ========================================================================
# 6. EFFECTIVE EQUATION OF STATE w_eff
# ========================================================================
print("\n" + "=" * 76)
print("EFFECTIVE EQUATION OF STATE w_eff")
print("=" * 76)

# w_eff = -1 + (2/3)*f_gradient + (1/3)*f_walls
# where f's are energy fractions in the total rho

print("\nw = w_bulk*(1-f_g-f_w) + w_g*f_g + w_w*f_w")
print("  = -1*(1-f_g-f_w) + (-1/3)*f_g + (-2/3)*f_w")
print("  = -1 + (2/3)*f_g + (1/3)*f_w")
print()

# Compute for EACH M_KK, using FIRAS bound (most favorable)
w_results = {}

for label, MKK_GeV in MKK_dict.items():
    MKK_inv_fm = MKK_GeV / hbar_c_GeV_fm
    delta_wall_fm = delta_wall_MKK / MKK_inv_fm
    delta_wall_Mpc = delta_wall_fm / Mpc_to_fm

    V_walls_Mpc3 = A_total * delta_wall_Mpc
    f_walls_vol = V_walls_Mpc3 / V_obs

    # Gradient energy fraction (using FIRAS, most favorable)
    grad_tau = delta_tau_FIRAS / delta_wall_MKK
    rho_grad_wall = 0.5 * Z_fold * grad_tau**2
    f_grad = (rho_grad_wall / V_fold) * f_walls_vol

    # Wall tension fraction
    sigma_wall = delta_tau_FIRAS * m_tau * Z_fold
    sigma_vol = sigma_wall / delta_wall_MKK
    f_wall = (sigma_vol / V_fold) * f_walls_vol

    # Total correction
    w_correction = (2.0/3.0) * f_grad + (1.0/3.0) * f_wall
    w_eff = -1.0 + w_correction

    log10_corr = np.log10(max(w_correction, 1e-300))

    print(f"  {label}:")
    print(f"    f_gradient = {f_grad:.3e}")
    print(f"    f_walls = {f_wall:.3e}")
    print(f"    |w + 1| = (2/3)*{f_grad:.2e} + (1/3)*{f_wall:.2e} = {w_correction:.3e}")
    print(f"    log10|w+1| = {log10_corr:.1f}")
    print(f"    w_eff = {w_eff:.15f}")
    print()

    w_results[label] = {
        'w_eff': w_eff,
        'w_correction': w_correction,
        'f_grad': f_grad,
        'f_wall': f_wall,
        'f_walls_vol': f_walls_vol,
        'delta_wall_Mpc': delta_wall_Mpc,
        'log10_corr': log10_corr,
    }

# ========================================================================
# 7. WHY THE CORRECTION IS STRUCTURALLY NEGLIGIBLE
# ========================================================================
print("=" * 76)
print("WHY |w+1| ~ 10^{-53} IS A STRUCTURAL RESULT")
print("=" * 76)

print("""
The fabric correction to w is controlled by a SINGLE dimensionless ratio:

  f_walls ~ (delta_wall / R_cell) * (N_cells * A_cell / V_obs)
          ~ delta_wall / R_cell   (geometric factor ~ O(1))

The wall thickness delta_wall is at the KK scale: 1/(m_tau * M_KK)
The cell radius R_cell is at the cosmological scale: ~4500 Mpc

  delta_wall / R_cell = 1 / (m_tau * M_KK * R_cell_phys)

This ratio is:""")

for label, MKK_GeV in MKK_dict.items():
    MKK_inv_fm = MKK_GeV / hbar_c_GeV_fm
    delta_wall_fm = delta_wall_MKK / MKK_inv_fm
    delta_wall_Mpc = delta_wall_fm / Mpc_to_fm
    ratio = delta_wall_Mpc / R_cell
    print(f"  {label}: {ratio:.3e}")

print("""
This is the ratio (KK scale) / (Hubble scale) ~ (M_KK)^{-1} / (H_0)^{-1}
                                                ~ H_0 / M_KK
                                                ~ 10^{-52} to 10^{-62}

The fabric STRUCTURE is real (32 cells, domain walls, gradient energy).
But the walls are thinner than an atom is to the observable universe.
The correction to w is:

  |w + 1| ~ delta_tau^2 * Z * f_walls / V_fold ~ 10^{-53} (best case)

This is NOT a failure of the fabric picture. It is the PREDICTION:
the fabric is cosmologically invisible in w(z).
""")

# ========================================================================
# 8. w(z) EVOLUTION (wall fraction scales with redshift)
# ========================================================================
print("=" * 76)
print("w(z) EVOLUTION")
print("=" * 76)

# The wall fraction f_walls(z) evolves because:
# - Wall thickness delta_wall = const (set by m_tau, independent of a)
# - Cell PHYSICAL size R_cell(a) = R_cell_0 * a = R_cell_0 / (1+z)
# - So f_walls ~ delta_wall / R_cell ~ (1+z) * f_walls_0
# This gives: w(z) = -1 + correction_0 * (1+z)
# In CPL form: w(a) = w_0 + w_a * (1-a) where:
#   w_0 = -1 + correction_0
#   w_a = -correction_0  (i.e., w was further from -1 in the past)
# So w_a < 0, which IS the DESI trend sign.

z_eval = np.array([0.0, 0.295, 0.510, 0.706, 1.0, 1.317, 2.0, 3.0, 5.0, 10.0])

# Use M_KK = 10^9 GeV (most favorable = smallest M_KK = largest walls)
MKK_best = 1e9
wr = w_results['M_KK = 10^9 GeV (Conv A)']
correction_0 = wr['w_correction']
w_0_fabric = wr['w_eff']
w_a_fabric = -correction_0  # From scaling f_walls ~ (1+z)

print(f"\n  Using M_KK = 10^9 GeV (most favorable case, FIRAS delta_tau):")
print(f"  correction_0 = {correction_0:.3e}")
print(f"  w_0 = -1 + correction_0 = {w_0_fabric:.15f}")
print(f"  w_a = -correction_0 = {w_a_fabric:.3e}")
print()

# w(z) = w_0 + w_a * z/(1+z)  [CPL convention: w(a) = w_0 + w_a*(1-a)]
w_z_eval = w_0_fabric + w_a_fabric * z_eval / (1.0 + z_eval)

print("  z       w(z) [fabric]           |w+1|")
print("  " + "-" * 55)
for z, w in zip(z_eval, w_z_eval):
    print(f"  {z:5.3f}   {w:22.15f}   {abs(w+1):.3e}")

print(f"\n  w_a sign: NEGATIVE (correct DESI trend)")
print(f"  But |w_a| = {abs(w_a_fabric):.3e}: invisible at ANY precision")

# ========================================================================
# 9. ALTERNATIVE CC: CONDENSATION ENERGY
# ========================================================================
print("\n" + "=" * 76)
print("ALTERNATIVE CC: CONDENSATION ENERGY vs SPECTRAL ACTION")
print("=" * 76)

print(f"""
  Two candidates for the physical CC:
  (A) V_eff(tau_fold) = {V_fold:.0f} M_KK^4  (full spectral action at fold)
  (B) |E_cond| = {abs(E_cond):.3f} M_KK    (BCS condensation energy per pair)
      Total BCS: |E_cond| * n_crystal, where n_crystal is the crystal density

  For the BCS condensate:
  - E_cond = {E_cond} M_KK (from S35)
  - The condensation energy DENSITY in the BCS ground state is:
    rho_BCS ~ (1/2) * N(0) * Delta^2 where N(0) is DOS at Fermi level
  - From S35: E_cond per unit cell = -0.115 M_KK
  - In M_KK^4 units (energy per KK-volume): rho_BCS ~ |E_cond| * M_KK^3 ~ 0.115 M_KK^4
  - This is ~2.2 million times SMALLER than V_fold = 250,361 M_KK^4
""")

rho_BCS = abs(E_cond)  # M_KK^4 (energy density in natural units)
ratio_BCS_Vfold = rho_BCS / V_fold

print(f"  rho_BCS / V_fold = {ratio_BCS_Vfold:.3e}")
print(f"  If CC = rho_BCS: reduces hierarchy by {-np.log10(ratio_BCS_Vfold):.1f} orders")
print()

print("  Lambda_CC for each candidate:")
for label, MKK_GeV in MKK_dict.items():
    ratio_MKK = MKK_GeV / M_Planck_GeV
    r4 = ratio_MKK**4

    Lambda_A = V_fold * r4
    Lambda_B = rho_BCS * r4
    log_A = np.log10(Lambda_A / Lambda_obs_MP4) if Lambda_A > 0 else float('inf')
    log_B = np.log10(Lambda_B / Lambda_obs_MP4) if Lambda_B > 0 else float('inf')

    print(f"  {label}:")
    print(f"    (A) V_fold:  Lambda/Lambda_obs = 10^{{{log_A:.1f}}}")
    print(f"    (B) E_cond:  Lambda/Lambda_obs = 10^{{{log_B:.1f}}}")
    print(f"    BCS saves {log_A - log_B:.1f} orders (from V_fold/E_cond ratio)")

print("""
  NEITHER candidate solves the CC problem:
  - (A) overshoots by 87-127 orders
  - (B) overshoots by 81-121 orders
  The BCS condensation energy buys only ~6 orders. The fundamental
  hierarchy (M_KK/M_P)^4 remains.
""")

# ========================================================================
# 10. COMPARISON WITH DESI
# ========================================================================
print("=" * 76)
print("DESI COMPARISON")
print("=" * 76)

desi_fits = {
    'DESI BAO + CMB (Planck)': {'w0': -0.55, 'w0_err': 0.21, 'wa': -1.30, 'wa_err': 0.70},
    'DESI + CMB + Pantheon+':  {'w0': -0.827, 'w0_err': 0.063, 'wa': -0.75, 'wa_err': 0.29},
    'DESI + CMB + DESY5':      {'w0': -0.752, 'w0_err': 0.067, 'wa': -1.05, 'wa_err': 0.31},
}

print(f"\n  Framework prediction (fabric-collective):")
print(f"    w_0 = {w_0_fabric:.15f}")
print(f"    w_a = {w_a_fabric:.3e}")
print(f"    These are INDISTINGUISHABLE from w_0 = -1, w_a = 0")
print()

for lab, fit in desi_fits.items():
    sigma_w0 = abs(w_0_fabric - fit['w0']) / fit['w0_err']
    sigma_wa = abs(w_a_fabric - fit['wa']) / fit['wa_err']
    print(f"  vs {lab}:")
    print(f"    w_0: {fit['w0']:.3f} +/- {fit['w0_err']:.3f} => {sigma_w0:.1f} sigma")
    print(f"    w_a: {fit['wa']:.2f}  +/- {fit['wa_err']:.2f}  => {sigma_wa:.1f} sigma")
    print()

print("  The fabric correction is 50+ orders below observational sensitivity.")
print("  The DESI comparison is IDENTICAL to the single-tau result.")
print("  The fabric IS there, but it is cosmologically silent.")

# ========================================================================
# 11. THE HONEST ANSWER: WHY FABRIC DOESN'T SAVE w(z)
# ========================================================================
print("\n" + "=" * 76)
print("STRUCTURAL ANALYSIS: WHY THE FABRIC CANNOT PRODUCE |w+1| ~ 0.1")
print("=" * 76)

print("""
  For w_0 ~ -0.55 (DESI central), we need:
    (2/3)*f_gradient + (1/3)*f_walls ~ 0.45

  This requires f_walls ~ O(1), i.e., the wall volume must be comparable
  to the total volume. But:

    f_walls = (wall area * wall thickness) / total volume
            ~ (N * R_cell^2 * delta_wall) / R_obs^3
            ~ (delta_wall / R_cell)   [since N * R_cell^3 ~ R_obs^3]

  For f_walls ~ O(1), we need delta_wall ~ R_cell.
  The wall thickness is 1/(m_tau * M_KK) in physical units.
  The cell radius is ~4500 Mpc.

  delta_wall / R_cell = 1 would require:
    m_tau * M_KK * R_cell = 1
    M_KK = 1 / (m_tau * R_cell) = 1 / (2.06 * 4500 Mpc)
    M_KK ~ 1 / (9270 Mpc) ~ 7e-29 eV

  This is BELOW the Hubble scale (H_0 ~ 10^{-33} eV).
  An M_KK this small is physically absurd:
  - Below the IR cutoff of the observable universe
  - Incompatible with having a Kaluza-Klein tower above the electroweak scale
  - Contradicts the framework's own structure (M_KK > 10^9 GeV from colliders)

  CONCLUSION: The fabric's spatial structure CANNOT produce observable w != -1
  for ANY physically meaningful M_KK. This is not a tuning failure. It is the
  dimensional analysis: (KK scale) / (Hubble scale) is always tiny.
""")

# ========================================================================
# 12. GATE VERDICT
# ========================================================================
print("=" * 76)
print("GATE VERDICT: W-Z-42 (REDO)")
print("=" * 76)

# Most favorable w
w_best = w_results['M_KK = 10^9 GeV (Conv A)']['w_eff']
correction_best = w_results['M_KK = 10^9 GeV (Conv A)']['w_correction']

print(f"""
  Pre-registered criterion:
    PASS: -1.2 < w_0 < -0.3 (dynamical DE consistent with DESI)
    FAIL: w_0 = -1.000 (exact Lambda) OR w_0 > 0

  COMPUTED (fabric-collective, most favorable case):
    w_0 = {w_best:.15f}
    |w_0 + 1| = {correction_best:.3e}
    w_a = {-correction_best:.3e}  (correct DESI sign, but ~50 orders too small)
""")

if abs(w_best + 1) < 1e-3:
    verdict = "FAIL"
    print(f"  VERDICT: **{verdict}** — w_0 = -1.000...{correction_best:.1e} (indistinguishable from -1)")
    print()
    print("  The fabric-collective calculation CONFIRMS the single-tau result.")
    print("  The spatial structure (32 cells, domain walls, gradient energy)")
    print("  exists but contributes at the 10^{-53} level to |w+1|.")
    print()
    print("  The framework IS geometric Lambda-CDM.")
    print("  The fabric correction has the RIGHT SIGN (w_a < 0, matching DESI trend)")
    print("  but is 50+ orders of magnitude below observational reach.")
else:
    verdict = "PASS"
    print(f"  VERDICT: **{verdict}** — dynamical dark energy")

# ========================================================================
# 13. SAVE DATA
# ========================================================================
np.savez('tier0-computation/s42_fabric_wz.npz',
    # Voronoi geometry
    N_cells=N_cells,
    R_obs_Mpc=R_obs_Mpc,
    R_cell_Mpc=R_cell,
    A_total_Mpc2=A_total,
    V_obs_Mpc3=V_obs,

    # Wall thickness estimates
    delta_wall_bare_MKK=delta_wall_A_MKK,
    xi_BCS_MKK=xi_BCS,
    xi_KZ_MKK=xi_KZ,
    delta_wall_used_MKK=delta_wall_MKK,

    # delta_tau estimates
    delta_tau_quantum=delta_tau_quantum,
    delta_tau_KZ=delta_tau_KZ,
    delta_tau_FIRAS=delta_tau_FIRAS,

    # w(z) prediction (most favorable: M_KK=10^9 GeV, FIRAS delta_tau)
    z_eval=z_eval,
    w_z_eval=w_z_eval,
    w0_fabric=w_0_fabric,
    wa_fabric=w_a_fabric,
    correction_0=correction_0,

    # Energy fractions (most favorable)
    f_gradient_best=w_results['M_KK = 10^9 GeV (Conv A)']['f_grad'],
    f_walls_best=w_results['M_KK = 10^9 GeV (Conv A)']['f_wall'],
    f_walls_vol_best=w_results['M_KK = 10^9 GeV (Conv A)']['f_walls_vol'],

    # Upstream data
    tau_fold=tau_fold,
    Z_fold=Z_fold,
    V_fold=V_fold,
    m_tau=m_tau,
    E_cond=E_cond,

    # CC comparison
    Lambda_obs_MP4=Lambda_obs_MP4,

    # S_full for plotting
    tau_Sfull=tau_Sfull,
    S_full=S_full,

    # Gate
    verdict=verdict,
    gate_name='W-Z-42-REDO',
)

print(f"\n  Data saved: tier0-computation/s42_fabric_wz.npz")

# ========================================================================
# 14. PLOT (3-panel: w(z), energy budget, wall fraction vs z)
# ========================================================================
fig, axes = plt.subplots(2, 2, figsize=(14, 11))
fig.suptitle('W-Z-42 (REDO): Fabric-Collective Dark Energy w(z)\n'
             r'$|w_0 + 1| \sim 10^{-53}$ — Fabric exists but is cosmologically silent',
             fontsize=13, fontweight='bold')

# --- Panel (a): w(z) with DESI ---
ax = axes[0, 0]
z_fine = np.linspace(0, 3, 200)
a_fine = 1.0 / (1.0 + z_fine)

# Framework prediction (indistinguishable from -1 at this scale)
w_framework = w_0_fabric + w_a_fabric * z_fine / (1.0 + z_fine)
ax.plot(z_fine, -1.0 * np.ones_like(z_fine), 'b-', lw=2.5,
        label=r'Framework: $w = -1 + O(10^{-53})$ (fabric)')

# DESI fits
w0_d, wa_d = -0.55, -1.30
w_desi = w0_d + wa_d * (1 - a_fine)
ax.plot(z_fine, w_desi, 'r--', lw=1.5, label=r'DESI Y1 (BAO+CMB): $w_0=-0.55$')
ax.fill_between(z_fine,
    (w0_d - 0.21) + (wa_d - 0.70) * (1 - a_fine),
    (w0_d + 0.21) + (wa_d + 0.70) * (1 - a_fine),
    color='red', alpha=0.1)

w0_p, wa_p = -0.827, -0.75
w_pan = w0_p + wa_p * (1 - a_fine)
ax.plot(z_fine, w_pan, 'g-.', lw=1.5, label=r'DESI+Pantheon+: $w_0=-0.83$')

ax.axhline(y=-1, color='gray', ls=':', alpha=0.5)
ax.set_xlabel('Redshift z', fontsize=12)
ax.set_ylabel('w(z)', fontsize=12)
ax.set_xlim(0, 3)
ax.set_ylim(-2.5, 0.5)
ax.legend(fontsize=8, loc='upper right')
ax.set_title('(a) Equation of State w(z)', fontsize=11)
ax.grid(True, alpha=0.3)

# --- Panel (b): Scale hierarchy (the WHY) ---
ax = axes[0, 1]
MKK_range = np.logspace(9, 20, 100)
f_walls_range = []
for MKK in MKK_range:
    MKK_inv_fm = MKK / hbar_c_GeV_fm
    dw_fm = delta_wall_MKK / MKK_inv_fm
    dw_Mpc = dw_fm / Mpc_to_fm
    Vw = A_total * dw_Mpc
    fw = Vw / V_obs
    f_walls_range.append(fw)
f_walls_range = np.array(f_walls_range)

ax.loglog(MKK_range, f_walls_range, 'b-', lw=2, label=r'$f_{walls}$ (volume fraction)')
ax.axhline(y=0.01, color='green', ls='--', lw=1.5, label=r'$f_{walls} = 0.01$ ($|w+1| \sim 0.003$)')
ax.axhline(y=1.0, color='red', ls='--', lw=1.5, label=r'$f_{walls} = 1$ ($|w+1| \sim 0.3$)')

for lbl, val in [('Conv A', 1e9), ('Conv C', 1e13), ('GUT', 1e16), (r'$M_P$', 1.22e19)]:
    idx = np.argmin(np.abs(MKK_range - val))
    ax.plot(val, f_walls_range[idx], 'o', ms=8, zorder=5)
    ax.annotate(lbl, xy=(val, f_walls_range[idx]),
                xytext=(val*3, f_walls_range[idx]*100),
                arrowprops=dict(arrowstyle='->', lw=0.8), fontsize=9)

ax.set_xlabel(r'$M_{KK}$ [GeV]', fontsize=12)
ax.set_ylabel(r'$f_{walls}$ = wall volume / total volume', fontsize=12)
ax.set_title('(b) Wall Volume Fraction vs M_KK', fontsize=11)
ax.set_ylim(1e-70, 1e5)
ax.legend(fontsize=9, loc='upper right')
ax.grid(True, alpha=0.3)

# --- Panel (c): Energy budget pie (at fold, most favorable) ---
ax = axes[1, 0]
f_g = w_results['M_KK = 10^9 GeV (Conv A)']['f_grad']
f_w = w_results['M_KK = 10^9 GeV (Conv A)']['f_wall']
f_bulk = 1.0 - f_g - f_w

# Since fractions are ~1e-53, pie chart is meaningless. Show log-scale bars instead.
categories = [r'Bulk $V_{eff}$' + '\n(w=-1)', r'Gradient' + '\n(w=-1/3)',
              r'Walls' + '\n(w=-2/3)']
values = [V_fold, V_fold * f_g, V_fold * f_w]
log_values = [np.log10(max(v, 1e-300)) for v in values]

colors = ['royalblue', 'darkorange', 'green']
bars = ax.barh(categories, log_values, color=colors, edgecolor='black', height=0.5)
ax.set_xlabel(r'$\log_{10}(\rho$ / $M_{KK}^4)$', fontsize=12)
ax.set_title(r'(c) Energy Density Budget ($M_{KK}=10^9$ GeV, FIRAS $\delta\tau$)', fontsize=11)

for bar, lv in zip(bars, log_values):
    ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height()/2,
            f'{lv:.1f}', va='center', fontsize=10)

ax.set_xlim(-60, 8)
ax.grid(True, alpha=0.3, axis='x')

# --- Panel (d): Wall fraction vs redshift ---
ax = axes[1, 1]
z_range = np.linspace(0, 10, 200)
# f_walls(z) = f_walls_0 * (1+z)  (wall thickness fixed, cells shrink)
f_walls_0 = w_results['M_KK = 10^9 GeV (Conv A)']['f_walls_vol']
f_walls_z = f_walls_0 * (1.0 + z_range)

ax.semilogy(z_range, f_walls_z, 'b-', lw=2, label=r'$f_{walls}(z) \propto (1+z)$')
ax.axhline(y=0.01, color='green', ls='--', alpha=0.7,
           label=r'Need $f_{walls} > 0.01$ for $|w+1| > 0.003$')
ax.set_xlabel('Redshift z', fontsize=12)
ax.set_ylabel(r'$f_{walls}(z)$', fontsize=12)
ax.set_title('(d) Wall Fraction Evolution (grows with z)', fontsize=11)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
ax.set_ylim(1e-55, 1e-48)

# Annotate the key message
ax.text(5, 1e-50, 'Wall fraction grows\nwith (1+z) but starts\n' +
        r'at $\sim 10^{-52}$' + '\nNever reaches O(1)',
        fontsize=10, ha='center', style='italic',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.tight_layout()
plt.savefig('tier0-computation/s42_fabric_wz.png', dpi=150, bbox_inches='tight')
print(f"  Plot saved: tier0-computation/s42_fabric_wz.png")

print("\n" + "=" * 76)
print("COMPUTATION COMPLETE")
print("=" * 76)
print("""
SUMMARY:
  The fabric-collective calculation CONFIRMS the single-tau result: w_0 = -1.
  The 32-cell Voronoi structure, domain walls, and gradient energy all exist
  but contribute at the 10^{-53} level. The reason is dimensional:
  wall thickness ~ 1/M_KK, cell size ~ 1/H_0, ratio ~ H_0/M_KK ~ 10^{-52}.

  The framework predicts:
    w_0 = -1 + O(10^{-53})    (indistinguishable from -1)
    w_a = -O(10^{-53})         (correct DESI sign, 50 orders too small)

  Gate W-Z-42: FAIL (w_0 = -1, exact Lambda-CDM)
  The fabric correction has the correct sign but is structurally negligible.
""")
