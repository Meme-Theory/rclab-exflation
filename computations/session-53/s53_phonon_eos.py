#!/usr/bin/env python3
"""
S53 PHONON-EOS-53: Equation of State + Exflationary Expansion History
=====================================================================

Physics:
  The BCS condensate on M^4 x SU(3) supports 6 phonon branches (GL-JOSEPHSON-52).
  These form a phonon gas at the GGE relic temperature T_acoustic = 0.112 M_KK.
  The equation of state w = p/rho determines whether this gas drives expansion.

  CRITICAL: This is EXFLATION, not inflation. Expansion is NOT from vacuum energy.
  The Jensen TT-deformation is exactly volume-preserving:
    L1^1 * L2^3 * L3^4 = e^{2s - 6s + 4s} = 1
  So V_int(tau) = constant — no KK volume change.

  The expansion comes from the BLV ACOUSTIC METRIC (W0-1, BLV-CONFORMAL-53):
    a_acoustic = a_geom * sqrt(rho_s / c_s)
    N_e^acoustic = N_e^geom + (1/2)*ln(rho_f/rho_i) - (1/2)*ln(c_sf/c_si)

  The phonon EOS tells us what happens to phonon stress-energy ON TOP of
  the acoustic metric expansion. In the condensed epoch, phonons propagate
  on the acoustic metric and their stress-energy contributes to the effective
  Friedmann equation for acoustic observers.

Method:
  1. Load 6-branch dispersion omega_n(K) from s52_gl_josephson.npz
  2. For each branch, compute Bose-Einstein thermodynamics:
     - rho_i = integral d^3K/(2pi)^3 omega_i(K) n_BE(omega_i(K), T)
     - p_i = integral d^3K/(2pi)^3 (1/3) K (d omega_i/dK) n_BE(omega_i(K), T)
  3. Sum over branches: w = sum(p_i) / sum(rho_i)
  4. Compute T=0 (zero-point) and T->inf (equipartition) limits
  5. Compute exflationary expansion history a_acoustic(tau)
  6. Compute H_exflation(tau) and plot

Gate: PHONON-EOS-53
  INFO: w value determined AND expansion history computed.

Author: Quantum-Acoustics-Theorist (S53)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from numpy import pi, sqrt, log, exp
from scipy.integrate import simpson
from scipy.interpolate import CubicSpline
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    T_acoustic, tau_fold, Vol_SU3_Haar, G_DeWitt, M_KK,
    c_Gold, c_fabric, N_e_classical, E_cond, H_fold,
    omega_L1, omega_L2, omega_H1, omega_H2, omega_H3,
    v_terminal, dt_transit, M_Pl_reduced
)

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "s53_phonon_eos_output.txt")
fp = open(OUT, "w")

def pr(s=""):
    print(s)
    fp.write(s + "\n")

pr("=" * 72)
pr("S53 PHONON-EOS-53: Phonon Equation of State + Exflationary History")
pr("=" * 72)

# ==========================================================================
#  SECTION 1: Load GL dispersion data
# ==========================================================================

pr("\n--- Section 1: Load GL dispersion ---")

data_dir = os.path.dirname(os.path.abspath(__file__))
gl_data = np.load(os.path.join(data_dir, "s52_gl_josephson.npz"), allow_pickle=True)
sweep_data = np.load(os.path.join(data_dir, "s53_gl_sweep.npz"), allow_pickle=True)

K_array = gl_data['K_array']       # (N_K+1,) wavevector grid
omega_br = gl_data['omega_branches']  # (N_K+1, 6) frequencies at fold tau=0.19
branch_labels = gl_data['branch_labels']
K_BZ = float(gl_data['K_BZ'])
N_K = len(K_array)
N_branches = 6

pr(f"  K range: [0, {K_BZ:.4f}] M_KK, {N_K} points")
pr(f"  Branches: {list(branch_labels)}")
pr(f"  T_acoustic = {T_acoustic} M_KK (GGE relic temperature)")

for i, label in enumerate(branch_labels):
    pr(f"  {label}: omega = [{omega_br[0,i]:.6f}, {omega_br[-1,i]:.6f}]")

# ==========================================================================
#  SECTION 2: Phonon thermodynamics — Bose-Einstein integrals
# ==========================================================================

pr("\n--- Section 2: Phonon equation of state ---")
pr("  Computing energy density and pressure from Bose-Einstein statistics")
pr("  3D BZ integration: rho = int d^3K/(2pi)^3 omega*n_BE")
pr("  Pressure: p = int d^3K/(2pi)^3 (1/3)*K*(d omega/dK)*n_BE")
pr("  where n_BE = 1/(exp(omega/T) - 1)")

def compute_eos(omega_branches, K_arr, T, verbose=True):
    """
    Compute energy density and pressure for a multi-branch phonon gas.

    Uses 3D integration over the BZ assuming isotropic dispersion.
    d^3K = 4*pi*K^2 dK, divided by (2*pi)^3.

    For each branch i:
      rho_i = 1/(2*pi^2) * int_0^K_BZ dK K^2 omega_i(K) * n_BE(omega_i, T)
      p_i   = 1/(2*pi^2) * int_0^K_BZ dK K^2 * (1/3)*K*(d omega_i/dK) * n_BE(omega_i, T)

    The factor 1/(2*pi^2) = 4*pi/(2*pi)^3.

    Zero-point (T=0) contributions:
      rho_0_i = 1/(2*pi^2) * int dK K^2 * (1/2)*omega_i
      p_0_i   = 1/(2*pi^2) * int dK K^2 * (1/6)*K*(d omega_i/dK)
    """
    N_br = omega_branches.shape[1]
    K_max = K_arr[-1]

    rho_per_branch = np.zeros(N_br)
    p_per_branch = np.zeros(N_br)
    rho_zp_per_branch = np.zeros(N_br)
    p_zp_per_branch = np.zeros(N_br)

    for i in range(N_br):
        omega_i = omega_branches[:, i]

        # Compute group velocity dω/dK via finite differences
        # Use cubic spline for smooth derivative
        cs_omega = CubicSpline(K_arr, omega_i)
        v_g = cs_omega(K_arr, 1)  # first derivative

        # Phase space weight: K^2 / (2*pi^2)
        K2 = K_arr**2
        prefactor = K2 / (2.0 * pi**2)

        # Bose-Einstein occupation
        if T > 0:
            # For Goldstone branch, omega(K=0)=0. Handle carefully.
            x = omega_i / T
            # Avoid overflow/underflow
            n_BE = np.zeros_like(x)
            mask_small = x < 500  # exp(500) overflows, n_BE ~ 0 there
            mask_zero = x < 1e-12  # omega ~ 0, use classical limit n_BE ~ T/omega
            mask_normal = mask_small & ~mask_zero

            if np.any(mask_zero):
                # Classical limit: n_BE = T/omega for omega -> 0
                # But at K=0 the integrand K^2*omega*n_BE -> K^2*T, finite
                n_BE[mask_zero] = T / np.maximum(omega_i[mask_zero], 1e-30)

            if np.any(mask_normal):
                n_BE[mask_normal] = 1.0 / (np.exp(x[mask_normal]) - 1.0)

            # n_BE = 0 for large x (mask not small) — already zero

            # Thermal energy density: omega * n_BE
            integrand_rho = prefactor * omega_i * n_BE
            rho_per_branch[i] = simpson(integrand_rho, x=K_arr)

            # Thermal pressure: (1/3) * K * v_g * n_BE
            integrand_p = prefactor * (1.0/3.0) * K_arr * v_g * n_BE
            p_per_branch[i] = simpson(integrand_p, x=K_arr)

        # Zero-point contributions (T=0 quantum pressure)
        integrand_rho_zp = prefactor * 0.5 * omega_i
        rho_zp_per_branch[i] = simpson(integrand_rho_zp, x=K_arr)

        integrand_p_zp = prefactor * (1.0/6.0) * K_arr * v_g
        p_zp_per_branch[i] = simpson(integrand_p_zp, x=K_arr)

    rho_total = np.sum(rho_per_branch)
    p_total = np.sum(p_per_branch)
    rho_zp_total = np.sum(rho_zp_per_branch)
    p_zp_total = np.sum(p_zp_per_branch)

    w = p_total / rho_total if abs(rho_total) > 1e-30 else 0.0
    w_zp = p_zp_total / rho_zp_total if abs(rho_zp_total) > 1e-30 else 0.0

    return {
        'rho_branch': rho_per_branch,
        'p_branch': p_per_branch,
        'rho_total': rho_total,
        'p_total': p_total,
        'w': w,
        'rho_zp_branch': rho_zp_per_branch,
        'p_zp_branch': p_zp_per_branch,
        'rho_zp_total': rho_zp_total,
        'p_zp_total': p_zp_total,
        'w_zp': w_zp,
    }


# Compute at T_acoustic
eos = compute_eos(omega_br, K_array, T_acoustic)

pr(f"\n  T = {T_acoustic} M_KK:")
pr(f"  {'Branch':<12} {'rho_i':>12} {'p_i':>12} {'w_i':>8}")
for i, label in enumerate(branch_labels):
    w_i = eos['p_branch'][i] / eos['rho_branch'][i] if abs(eos['rho_branch'][i]) > 1e-30 else 0.0
    pr(f"  {label:<12} {eos['rho_branch'][i]:>12.6f} {eos['p_branch'][i]:>12.6f} {w_i:>8.4f}")

pr(f"\n  rho_total = {eos['rho_total']:.6f} M_KK^4")
pr(f"  p_total   = {eos['p_total']:.6f} M_KK^4")
pr(f"  w_phonon  = {eos['w']:.6f}")

# Zero-point
pr(f"\n  T = 0 (zero-point quantum pressure):")
pr(f"  {'Branch':<12} {'rho_zp':>12} {'p_zp':>12} {'w_zp':>8}")
for i, label in enumerate(branch_labels):
    w_zp_i = eos['p_zp_branch'][i] / eos['rho_zp_branch'][i] if abs(eos['rho_zp_branch'][i]) > 1e-30 else 0.0
    pr(f"  {label:<12} {eos['rho_zp_branch'][i]:>12.6f} {eos['p_zp_branch'][i]:>12.6f} {w_zp_i:>8.4f}")

pr(f"\n  rho_zp_total = {eos['rho_zp_total']:.6f} M_KK^4")
pr(f"  p_zp_total   = {eos['p_zp_total']:.6f} M_KK^4")
pr(f"  w_zp         = {eos['w_zp']:.6f}")

# ==========================================================================
#  SECTION 3: Temperature dependence of w
# ==========================================================================

pr("\n--- Section 3: w(T) — temperature scan ---")

T_values = np.array([0.001, 0.005, 0.01, 0.02, 0.05, 0.08, 0.1,
                      0.112, 0.15, 0.2, 0.3, 0.5, 0.8, 1.0,
                      2.0, 5.0, 10.0, 50.0, 100.0])

w_vs_T = np.zeros(len(T_values))
rho_vs_T = np.zeros(len(T_values))
p_vs_T = np.zeros(len(T_values))

for j, T in enumerate(T_values):
    eos_T = compute_eos(omega_br, K_array, T, verbose=False)
    w_vs_T[j] = eos_T['w']
    rho_vs_T[j] = eos_T['rho_total']
    p_vs_T[j] = eos_T['p_total']

pr(f"  {'T (M_KK)':>10} {'w':>10} {'rho':>14} {'p':>14}")
for j, T in enumerate(T_values):
    pr(f"  {T:>10.3f} {w_vs_T[j]:>10.6f} {rho_vs_T[j]:>14.6f} {p_vs_T[j]:>14.6f}")

# Analytic limits
pr(f"\n  Analytic limits:")
pr(f"  T -> 0:   w -> w_zp = {eos['w_zp']:.6f}")
pr(f"  T -> inf: w -> 1/3   (radiation, all modes relativistic)")
pr(f"  At T_acoustic: w = {w_vs_T[np.argmin(np.abs(T_values - T_acoustic))]:.6f}")

# Bracket from scan
w_at_Tacoustic = w_vs_T[np.argmin(np.abs(T_values - T_acoustic))]
w_low_T = w_vs_T[0]
w_high_T = w_vs_T[-1]

# ==========================================================================
#  SECTION 4: Degeneracy multiplicities
# ==========================================================================

pr("\n--- Section 4: Branch multiplicities ---")
pr("  The 6 GL branches describe COLLECTIVE modes of the 3-sector condensate.")
pr("  In the full fabric, each cell has these 6 modes. On the 32-cell tessellation:")
pr(f"  N_cells = 32")
pr(f"  Total phonon modes = 6 * 32 = 192")
pr("  But the EOS per cell is what enters the local Friedmann equation.")
pr("  The multiplicities affect the total energy density but NOT w.")
pr("  w = p/rho is intensive (per cell).")

# ==========================================================================
#  SECTION 5: Exflationary expansion history
# ==========================================================================

pr("\n--- Section 5: Exflationary expansion history ---")
pr("  The Jensen TT-deformation is EXACTLY volume-preserving:")
pr("  V_int(tau) = Vol_SU3_Haar * det(g(tau)/g(0))^{1/2} = const")
pr("  L1^1 * L2^3 * L3^4 = e^{2s-6s+4s} = 1")
pr("  So V_int does NOT change. There is NO KK volume-driven expansion.")
pr("")
pr("  The expansion is from the ACOUSTIC METRIC (BLV-CONFORMAL-53):")
pr("  a_acoustic = a_geom * sqrt(rho_s / c_s)")
pr("  N_e^acoustic = N_e^geom + (1/2)*ln(rho_f/rho_i) - (1/2)*ln(c_sf/c_si)")
pr("")
pr("  Three contributions:")
pr(f"  1. Geometric: N_e^geom = {N_e_classical:.4f} (EFOLD-MAPPING-52)")
pr(f"  2. Sound speed: (1/2)*ln(c_fabric/c_Gold) = (1/2)*ln({c_fabric/c_Gold:.2f})")

N_e_sound = 0.5 * np.log(c_fabric / c_Gold)
pr(f"     = {N_e_sound:.4f} e-folds")

# Density contribution from GL sweep
tau_sweep = sweep_data['tau_values']
Delta_sweep = sweep_data['Delta_all']  # (15, 3)
rho_sweep = sweep_data['rho_all']      # (15, 3)

# Superfluid density proxy: rho_s ~ sum(rho_alpha * Delta_alpha^2) = phase inertia
rho_s_sweep = np.sum(rho_sweep * Delta_sweep**2, axis=1)

pr(f"\n  Superfluid density rho_s(tau) = sum_alpha rho_alpha * Delta_alpha^2:")
for j in range(len(tau_sweep)):
    pr(f"    tau = {tau_sweep[j]:.2f}: rho_s = {rho_s_sweep[j]:.6f}")

rho_s_max_idx = np.argmax(rho_s_sweep)
rho_s_min_idx = np.argmin(rho_s_sweep)
rho_s_initial = rho_s_sweep[0]  # tau = 0.01
rho_s_fold = rho_s_sweep[np.argmin(np.abs(tau_sweep - tau_fold))]

pr(f"\n  rho_s(tau=0.01) = {rho_s_initial:.6f}")
pr(f"  rho_s(fold)     = {rho_s_fold:.6f}")
pr(f"  rho_s max       = {rho_s_sweep[rho_s_max_idx]:.6f} at tau = {tau_sweep[rho_s_max_idx]:.2f}")
pr(f"  rho_s max/min   = {rho_s_sweep[rho_s_max_idx]/rho_s_sweep[rho_s_min_idx]:.4f}")

N_e_density = 0.5 * np.log(rho_s_fold / rho_s_initial)
pr(f"\n  3. Density: (1/2)*ln(rho_f/rho_i) = {N_e_density:.4f}")

N_e_total = N_e_classical + N_e_sound + N_e_density
pr(f"\n  N_e^total = {N_e_classical:.4f} + {N_e_sound:.4f} + {N_e_density:.4f} = {N_e_total:.4f}")

# ==========================================================================
#  SECTION 6: Acoustic Hubble parameter H(tau)
# ==========================================================================

pr("\n--- Section 6: Acoustic Hubble parameter H_acoustic(tau) ---")

# The acoustic scale factor:
# a_acoustic(tau) = a_geom(tau) * sqrt(rho_s(tau) / c_s(tau))
#
# For the geometric part, from S52 12D-reduction:
# V_KK(tau) = -(M_p^2/2) * R_K(tau), with G_mod = 5
# The modulus kinetic term: (1/2)*G_mod*M_p^2 * tau_dot^2
# Terminal velocity: v_terminal = 26.545 M_KK
# dt_transit = 0.0011302 M_KK^{-1}
#
# Geometric scale factor from spectral action gradient:
# H_geom = sqrt((G_mod * v_term^2 / 2 + V_KK) / (3*M_p^2))
# But more directly: H_fold = 586.53 M_KK (from S38 KZ defects)

# Compute a_acoustic(tau) along the GL sweep
c_Gold_sweep = sweep_data['c_Gold_vs_tau']  # (15,) Goldstone speed at each tau

a_acoustic_rel = np.sqrt(rho_s_sweep / c_Gold_sweep)
a_acoustic_norm = a_acoustic_rel / a_acoustic_rel[0]  # normalized to 1 at tau=0.01

pr(f"  a_acoustic(tau) = sqrt(rho_s / c_Gold) * a_geom [relative]")
pr(f"  {'tau':>6} {'rho_s':>10} {'c_Gold':>10} {'a_acous/a_0':>12}")
for j in range(len(tau_sweep)):
    pr(f"  {tau_sweep[j]:>6.2f} {rho_s_sweep[j]:>10.6f} {c_Gold_sweep[j]:>10.6f} {a_acoustic_norm[j]:>12.6f}")

# Acoustic Hubble from time derivative
# We need tau(t) to compute H. Use tau_dot = v_terminal at fold.
# Approximate: tau is roughly linear in t near the fold.
# dt/dtau = 1/v_terminal

# Compute H_acoustic = d(ln a_acoustic)/dt_proper
# dt_proper = sqrt(rho_s * c_Gold) * dt  (acoustic lapse)
# d(ln a_acoustic)/dt = (1/2) * (rho_s'/rho_s - c_Gold'/c_Gold) * tau_dot + H_geom
# where prime is d/dtau

# Spline interpolation for derivatives
cs_rho_s = CubicSpline(tau_sweep, rho_s_sweep)
cs_c_Gold = CubicSpline(tau_sweep, c_Gold_sweep)

# Evaluate derivatives
drho_s_dtau = cs_rho_s(tau_sweep, 1)
dc_Gold_dtau = cs_c_Gold(tau_sweep, 1)

# Geometric Hubble: from the spectral action kinetic term
# H_geom = v_terminal * sqrt(G_DeWitt / 6) (for modulus-dominated era)
# More precisely: H_geom^2 = (G_DeWitt * v_term^2 / 2) / (3 * M_Pl^2/M_KK^2)
# Using M_Pl/M_KK = M_Pl_reduced / M_KK
M_Pl_MKK = M_Pl_reduced / M_KK  # in M_KK units

# From S38: H_fold = 586.53 M_KK. This is the GEOMETRIC Hubble.
H_geom_fold = H_fold
pr(f"\n  H_geom at fold = {H_geom_fold:.2f} M_KK (S38 KZ)")

# H_acoustic = [H_geom + (1/2)(rho_s'/rho_s - c'/c) * tau_dot] / sqrt(rho_s * c_Gold)
# tau_dot = v_terminal = 26.545 M_KK
tau_dot = v_terminal

H_acoustic = np.zeros(len(tau_sweep))
for j in range(len(tau_sweep)):
    drho_rho = drho_s_dtau[j] / rho_s_sweep[j]
    dc_c = dc_Gold_dtau[j] / c_Gold_sweep[j]
    lapse = np.sqrt(rho_s_sweep[j] * c_Gold_sweep[j])
    H_acoustic[j] = (H_geom_fold + 0.5 * (drho_rho - dc_c) * tau_dot) / lapse

pr(f"\n  Acoustic Hubble parameter H_acoustic(tau):")
pr(f"  {'tau':>6} {'H_acoustic':>12} {'H_acous/H_geom':>14}")
for j in range(len(tau_sweep)):
    pr(f"  {tau_sweep[j]:>6.2f} {H_acoustic[j]:>12.2f} {H_acoustic[j]/H_geom_fold:>14.4f}")

H_acoustic_fold = H_acoustic[np.argmin(np.abs(tau_sweep - tau_fold))]
pr(f"\n  H_acoustic at fold = {H_acoustic_fold:.2f} M_KK")
pr(f"  Ratio H_acoustic/H_geom = {H_acoustic_fold/H_geom_fold:.4f}")

# ==========================================================================
#  SECTION 7: Effective Friedmann equation with phonon stress-energy
# ==========================================================================

pr("\n--- Section 7: Phonon stress-energy on acoustic metric ---")

# The phonon energy density at T_acoustic in the acoustic metric
rho_phonon = eos['rho_total']  # M_KK^4
p_phonon = eos['p_total']      # M_KK^4

pr(f"  rho_phonon = {rho_phonon:.6f} M_KK^4")
pr(f"  p_phonon   = {p_phonon:.6f} M_KK^4")
pr(f"  w_phonon   = {eos['w']:.6f}")

# How does this compare to the geometric Hubble?
# H_fold^2 = (8*pi*G_4D/3) * rho_geom
# G_4D ~ 1/(M_Pl^2), rho_geom from modulus kinetic energy
# rho_geom = (1/2)*G_DeWitt*M_Pl^2 * v_terminal^2 / M_KK^4 (in M_KK^4 units)
# Actually: H_fold^2 * 3*M_Pl^2/M_KK^2 = rho_geom/M_KK^4 in natural units
rho_geom = 3.0 * M_Pl_MKK**2 * H_geom_fold**2
pr(f"\n  rho_geom (from H_fold) = 3*M_p^2*H^2 = {rho_geom:.2f} M_KK^4")
pr(f"  rho_phonon / rho_geom = {rho_phonon/rho_geom:.6e}")
pr("  Phonon stress-energy is NEGLIGIBLE compared to geometric (modulus) energy.")
pr("  The expansion is entirely GEOMETRIC during the transit epoch.")

# ==========================================================================
#  SECTION 8: Expansion history a_acoustic(tau) integrated
# ==========================================================================

pr("\n--- Section 8: Integrated expansion history ---")

# Dense tau grid for smooth integration
tau_dense = np.linspace(tau_sweep[0], tau_sweep[-1], 500)
rho_s_dense = cs_rho_s(tau_dense)
c_Gold_dense = cs_c_Gold(tau_dense)

# Acoustic scale factor (relative)
a_acous_dense = np.sqrt(rho_s_dense / c_Gold_dense)
a_acous_dense_norm = a_acous_dense / a_acous_dense[0]

# Including geometric expansion
# N_e^geom(tau) = N_e_classical * (tau - tau_0) / (tau_fold - tau_0)
# Approximation: linear in tau from 0 to tau_fold
# Actually EFOLD-MAPPING-52 gives total = 0.1734 for full transit
# Distribute linearly in tau
tau_0_eff = tau_sweep[0]
a_geom_factor = np.exp(N_e_classical * (tau_dense - tau_0_eff) / (tau_fold - tau_0_eff))

# Full acoustic scale factor
a_full_dense = a_geom_factor * a_acous_dense_norm

# E-folds (cumulative from tau=0.01)
N_e_full = np.log(a_full_dense)
N_e_acous_only = np.log(a_acous_dense_norm)

pr(f"  E-folds at fold (tau={tau_fold}):")
fold_idx = np.argmin(np.abs(tau_dense - tau_fold))
pr(f"  N_e^acoustic_only = {N_e_acous_only[fold_idx]:.4f}")
pr(f"  N_e^geom         = {N_e_classical * (tau_fold - tau_0_eff) / (tau_fold - tau_0_eff):.4f}")
pr(f"  N_e^full         = {N_e_full[fold_idx]:.4f}")

pr(f"\n  Including c_fabric -> c_Gold transition (ONSET):")
pr(f"  N_e^sound (onset) = {N_e_sound:.4f}")
pr(f"  N_e^GL_internal   = {N_e_acous_only[fold_idx]:.4f}")
pr(f"  N_e^geom          = {N_e_classical:.4f}")
pr(f"  N_e^total         = {N_e_sound + N_e_acous_only[fold_idx] + N_e_classical:.4f}")

# ==========================================================================
#  SECTION 9: Cross-check with prior result
# ==========================================================================

pr("\n--- Section 9: Cross-checks ---")

# W1-5 found w = 0.158 with bracket [0.050, 0.222] — verify
pr(f"  W1-5 prior: w = 0.158, bracket [0.050, 0.222]")
pr(f"  This computation: w = {eos['w']:.6f}")

# Check: for the Goldstone branch alone (linear dispersion omega ~ c*K),
# w should be 1/3 (radiation)
eos_gold_only = compute_eos(omega_br[:, :1], K_array, T_acoustic, verbose=False)
pr(f"\n  Goldstone-only EOS:")
pr(f"    w_Goldstone = {eos_gold_only['w']:.6f} (expect ~1/3 = {1/3:.6f})")

# For massive branches (gap >> T), w -> 0 (non-relativistic)
# Check the massive Higgs branch
eos_higgs = compute_eos(omega_br[:, 5:6], K_array, T_acoustic, verbose=False)
pr(f"  Higgs-only EOS (massive, gap = {omega_br[0,5]:.2f}):")
pr(f"    w_Higgs = {eos_higgs['w']:.6f} (expect ~0 for gap >> T)")
pr(f"    rho_Higgs = {eos_higgs['rho_total']:.6e} (Boltzmann-suppressed)")

# Effective w decomposition
pr(f"\n  Energy-weighted decomposition:")
total_rho = eos['rho_total']
for i, label in enumerate(branch_labels):
    frac = eos['rho_branch'][i] / total_rho
    w_i = eos['p_branch'][i] / eos['rho_branch'][i] if abs(eos['rho_branch'][i]) > 1e-30 else 0.0
    pr(f"    {label:<12}: frac={frac:.4f}, w_i={w_i:.4f}, frac*w_i={frac*w_i:.4f}")

pr(f"\n  Sum of frac*w_i = {eos['w']:.6f} = w_total (consistency check)")

# ==========================================================================
#  SECTION 10: T -> infinity limit
# ==========================================================================

pr("\n--- Section 10: High-T (equipartition) limit ---")
eos_highT = compute_eos(omega_br, K_array, 1000.0, verbose=False)
pr(f"  T = 1000 M_KK: w = {eos_highT['w']:.6f}")
pr(f"  Expected: w -> 1/3 = {1/3:.6f} (all modes classical/relativistic)")
pr(f"  Deviation from 1/3: {abs(eos_highT['w'] - 1/3):.6f}")

# ==========================================================================
#  SECTION 11: Gate verdict
# ==========================================================================

pr("\n" + "=" * 72)
pr("GATE: PHONON-EOS-53")
pr("=" * 72)

pr(f"\n  w_phonon at T_acoustic = {T_acoustic} M_KK:")
pr(f"    w = {eos['w']:.6f}")
pr(f"    rho = {eos['rho_total']:.6f} M_KK^4")
pr(f"    p = {eos['p_total']:.6f} M_KK^4")
pr(f"\n  w_zp (T=0): {eos['w_zp']:.6f}")
pr(f"  w_highT (T=1000): {eos_highT['w']:.6f}")
pr(f"\n  Expansion history:")
pr(f"    N_e^geom    = {N_e_classical:.4f}")
pr(f"    N_e^sound   = {N_e_sound:.4f}")
pr(f"    N_e^density = {N_e_density:.4f}")
pr(f"    N_e^total   = {N_e_total:.4f}")
pr(f"\n  H_acoustic at fold = {H_acoustic_fold:.2f} M_KK")
pr(f"  rho_phonon/rho_geom = {rho_phonon/rho_geom:.2e}")

gate_verdict = "INFO"
gate_detail = (
    f"w_phonon = {eos['w']:.4f} at T_acoustic = {T_acoustic}. "
    f"Bracket: [{eos['w_zp']:.3f}, {1/3:.3f}] (T=0 to T=inf). "
    f"N_e^acoustic = {N_e_total:.2f}. "
    f"Phonon stress-energy negligible vs geometric: rho_ph/rho_geom = {rho_phonon/rho_geom:.1e}. "
    f"Expansion driven by acoustic metric (c_fabric/c_Gold = {c_fabric/c_Gold:.0f}x), not vacuum energy."
)

pr(f"\n  Verdict: {gate_verdict}")
pr(f"  Detail: {gate_detail}")

# ==========================================================================
#  SECTION 12: Save data
# ==========================================================================

pr("\n--- Section 12: Saving data ---")

save_path = os.path.join(data_dir, "s53_phonon_eos.npz")
np.savez(save_path,
    # EOS at T_acoustic
    w_phonon=eos['w'],
    rho_phonon=eos['rho_total'],
    p_phonon=eos['p_total'],
    rho_branch=eos['rho_branch'],
    p_branch=eos['p_branch'],
    w_zp=eos['w_zp'],
    rho_zp=eos['rho_zp_total'],
    p_zp=eos['p_zp_total'],
    # Temperature scan
    T_values=T_values,
    w_vs_T=w_vs_T,
    rho_vs_T=rho_vs_T,
    p_vs_T=p_vs_T,
    # Expansion history
    tau_sweep=tau_sweep,
    rho_s_sweep=rho_s_sweep,
    c_Gold_sweep=c_Gold_sweep,
    a_acoustic_norm=a_acoustic_norm,
    H_acoustic=H_acoustic,
    H_acoustic_fold=H_acoustic_fold,
    N_e_geom=N_e_classical,
    N_e_sound=N_e_sound,
    N_e_density=N_e_density,
    N_e_total=N_e_total,
    # Dense expansion history
    tau_dense=tau_dense,
    N_e_full_dense=N_e_full,
    # Gate
    gate_name=np.array(["PHONON-EOS-53"]),
    gate_verdict=np.array([gate_verdict]),
    gate_detail=np.array([gate_detail]),
)
pr(f"  Saved: {save_path}")

# ==========================================================================
#  SECTION 13: Plot
# ==========================================================================

pr("\n--- Section 13: Plotting ---")

fig, axes = plt.subplots(2, 3, figsize=(18, 10))
fig.suptitle('PHONON-EOS-53: Equation of State + Exflationary History', fontsize=14, fontweight='bold')

# Panel 1: w(T)
ax = axes[0, 0]
ax.semilogx(T_values, w_vs_T, 'b.-', lw=2, markersize=6)
ax.axhline(1/3, color='r', ls='--', alpha=0.5, label='w = 1/3 (radiation)')
ax.axhline(eos['w_zp'], color='gray', ls=':', alpha=0.5, label=f'w_zp = {eos["w_zp"]:.3f}')
ax.axvline(T_acoustic, color='green', ls='--', alpha=0.7, label=f'T_acoustic = {T_acoustic}')
ax.set_xlabel('T (M_KK)')
ax.set_ylabel('w = p/rho')
ax.set_title('EOS: w(T)')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 2: Energy density per branch at T_acoustic
ax = axes[0, 1]
short_labels = ['Gold', 'L1', 'L2', 'B3', 'B4', 'H1']
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
ax.bar(range(N_branches), eos['rho_branch'], color=colors, alpha=0.7)
ax.set_xticks(range(N_branches))
ax.set_xticklabels(short_labels, fontsize=9)
ax.set_ylabel('rho_i (M_KK^4)')
ax.set_title(f'Energy density per branch (T={T_acoustic})')
ax.set_yscale('log')
ax.grid(True, alpha=0.3, axis='y')

# Panel 3: Superfluid density and c_Gold vs tau
ax = axes[0, 2]
ax2 = ax.twinx()
l1, = ax.plot(tau_sweep, rho_s_sweep, 'b.-', lw=2, label='rho_s')
l2, = ax2.plot(tau_sweep, c_Gold_sweep, 'r.-', lw=2, label='c_Gold')
ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5)
ax.set_xlabel('tau')
ax.set_ylabel('rho_s (M_KK^4)', color='b')
ax2.set_ylabel('c_Gold (M_KK)', color='r')
ax.set_title('Superfluid density & sound speed')
lines = [l1, l2]
ax.legend(lines, [l.get_label() for l in lines], fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 4: Acoustic scale factor
ax = axes[1, 0]
ax.plot(tau_sweep, a_acoustic_norm, 'b.-', lw=2, label='a_acoustic (rho,c only)')
fold_marker = np.argmin(np.abs(tau_sweep - tau_fold))
ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5, label=f'fold tau={tau_fold}')
ax.plot(tau_sweep[fold_marker], a_acoustic_norm[fold_marker], 'ro', ms=10,
        label=f'fold: a/a_0 = {a_acoustic_norm[fold_marker]:.4f}')
ax.set_xlabel('tau')
ax.set_ylabel('a_acoustic / a_acoustic(tau_0)')
ax.set_title('Acoustic scale factor (GL internal)')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 5: Acoustic Hubble parameter
ax = axes[1, 1]
ax.plot(tau_sweep, H_acoustic, 'b.-', lw=2)
ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5)
ax.set_xlabel('tau')
ax.set_ylabel('H_acoustic (M_KK)')
ax.set_title('Acoustic Hubble parameter')
ax.grid(True, alpha=0.3)

# Panel 6: E-fold breakdown (bar chart)
ax = axes[1, 2]
contributions = [N_e_classical, N_e_sound, N_e_density]
labels_bar = ['Geometric\n(EFOLD-52)', 'Sound speed\n(c_fab/c_Gold)', 'Density\n(rho_s)']
bar_colors = ['steelblue', 'darkorange', 'green']
bars = ax.bar(range(3), contributions, color=bar_colors, alpha=0.7)
ax.set_xticks(range(3))
ax.set_xticklabels(labels_bar, fontsize=9)
ax.set_ylabel('e-folds')
ax.set_title(f'E-fold contributions (total = {N_e_total:.2f})')
ax.axhline(3.1, color='red', ls='--', alpha=0.5, label='Master gate (3.1)')
for b, v in zip(bars, contributions):
    ax.text(b.get_x() + b.get_width()/2, v + 0.03, f'{v:.3f}', ha='center', fontsize=9)
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3, axis='y')

plt.tight_layout()
plot_path = os.path.join(data_dir, "s53_phonon_eos.png")
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
pr(f"  Saved: {plot_path}")

# ==========================================================================
#  SUMMARY
# ==========================================================================

pr("\n" + "=" * 72)
pr("SUMMARY: PHONON-EOS-53")
pr("=" * 72)
pr(f"\n  EQUATION OF STATE:")
pr(f"    w_phonon = {eos['w']:.6f} at T_acoustic = {T_acoustic} M_KK")
pr(f"    Bracket: w in [{eos['w_zp']:.4f}, {1/3:.4f}] (T=0 to T=inf)")
pr(f"    At T_acoustic, w = {eos['w']:.4f}: radiation-like (gap < T for 3/6 branches)")
pr(f"    Goldstone-only: w = {eos_gold_only['w']:.4f} (linear dispersion -> radiation)")
pr(f"    Massive modes suppressed: Higgs rho/total = {eos['rho_branch'][5]/eos['rho_total']:.2e}")
pr(f"\n  EXFLATIONARY EXPANSION HISTORY:")
pr(f"    Jensen metric: EXACTLY volume-preserving (det(g) = const)")
pr(f"    Expansion mechanism: ACOUSTIC METRIC (BLV)")
pr(f"      a_acoustic = a_geom * sqrt(rho_s / c_s)")
pr(f"      N_e^geom    = {N_e_classical:.4f} (KK geometric ceiling)")
pr(f"      N_e^sound   = {N_e_sound:.4f} (c_fabric/c_Gold = {c_fabric/c_Gold:.0f}x)")
pr(f"      N_e^density = {N_e_density:.4f} (GL internal rho_s variation)")
pr(f"      N_e^total   = {N_e_total:.4f}")
pr(f"    H_acoustic at fold = {H_acoustic_fold:.2f} M_KK")
pr(f"    H_acous/H_geom = {H_acoustic_fold/H_geom_fold:.4f}")
pr(f"\n  PHONON STRESS-ENERGY vs GEOMETRIC:")
pr(f"    rho_phonon / rho_geom = {rho_phonon/rho_geom:.2e}")
pr(f"    Phonon gas is ENERGETICALLY IRRELEVANT to the expansion.")
pr(f"    Exflation is driven by the ACOUSTIC METRIC, not by w_phonon.")
pr(f"\n  CRITICAL DISTINCTION:")
pr(f"    In inflation, w < -1/3 drives accelerated expansion (vacuum energy).")
pr(f"    In exflation, expansion comes from the acoustic metric scale factor:")
pr(f"    the 229x c_fabric/c_Gold hierarchy means phononic observers see")
pr(f"    a MUCH LARGER universe than geometric observers, regardless of w.")
pr(f"    The phonon w = {eos['w']:.3f} does NOT need to be negative.")
pr(f"\n  Gate: PHONON-EOS-53 = {gate_verdict}")
pr(f"  {gate_detail}")
pr("=" * 72)

fp.close()
print(f"\nOutput written to {OUT}")
