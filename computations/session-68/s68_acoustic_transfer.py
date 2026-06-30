#!/usr/bin/env python3
"""
ACOUSTIC-TRANSFER-68: Scalar Acoustic Transfer Function Across 54 Decades
==========================================================================

Computes the scalar acoustic transfer function T(k_CMB, k_transit) that
connects the Bogoliubov power spectrum at transit scale (k ~ 1200 M_KK
~ 10^{15} GeV) to CMB observational scale (k ~ 0.05 Mpc^{-1} ~ 10^{-42}
M_KK). This is a 54-decade extrapolation.

GOVERNING EQUATIONS:
--------------------
The scalar mode equation in conformal time eta:

    u_k'' + (k^2 c_BLV^2 - z''/z) u_k = 0                      (S.1)

where u_k = z * zeta_k, z = a * sqrt(2 * eps_H), c_BLV = 0.485.

The acoustic white hole transfer function encodes how the post-transit
outflow dilutes the power spectrum from transit scale to CMB scale.

PHYSICAL MECHANISM:
-------------------
The transit at Mach 13.75 (scalar) creates an acoustic white hole.
Post-transit, the expanding flow velocity v(r) decreases with distance
from the sonic horizon. The transfer function |T(k)|^2 is determined
by WKB propagation through the post-transit epoch.

The key insight (S66 Mack-Transit workshop): the transit spectrum has
n_s ~ 4 (deep blue), while Planck observes n_s = 0.965. The acoustic
transfer must supply ~3 powers of scale-dependence. For Bondi-type
spherical outflow v ~ r^{-2}: |T|^2 ~ (k/k_0)^{4-n_s^{transit}} maps
the deep-blue transit spectrum onto the nearly flat CMB spectrum.

APPROACH:
---------
1. Reconstruct background (tau, S, a, z, eps_H, eta) from W1-A data
2. Compute scalar pump field z''/z in conformal time
3. Model the post-transit evolution:
   - The transit region tau in [0.10, 0.30] is computed exactly (W1-A)
   - Post-transit: the expansion continues, z''/z evolves as the
     universe expands, eps_H changes. Use the spectral action S(tau)
     to extrapolate.
4. For the 54-decade transfer:
   - At transit scale: P(k) known from W1-A
   - The transfer function is the evolution of |u_k/z|^2 from the
     transit epoch to the epoch when mode k re-enters the horizon
   - For superhorizon modes: |u_k/z|^2 is FROZEN (conserved).
     This is the critical point: curvature perturbation zeta = u_k/z
     is conserved on superhorizon scales.
   - The spectral SHAPE is determined by how modes exit the horizon
     during the transit, which is already computed in W1-A.
   - The AMPLITUDE transfer comes from the delta-N formalism (W3-B).

CRITICAL STRUCTURAL INSIGHT:
-----------------------------
For adiabatic perturbations on superhorizon scales, the curvature
perturbation zeta is CONSERVED (Weinberg 2003, Lyth-Rodriguez 2005).
This means:

    P_zeta(k, t_CMB) = P_zeta(k, t_exit)                        (S.2)

where t_exit is the time mode k exits the horizon during the transit.

The "54-decade transfer" is therefore NOT a dynamical propagation
problem but a HORIZON-CROSSING mapping problem:
- Which value of k exits the horizon at which value of tau?
- What is P_zeta(k) at that horizon crossing?

The transit-scale spectrum from W1-A gives P_zeta(k) for k ~ 50-5000
M_KK. The CMB-scale modes (k ~ 10^{-42} M_KK) exited the horizon
much EARLIER in the expansion (at smaller a) or require the full
post-transit expansion history.

THE RESOLUTION: The multifield delta-N (W3-B) already provides
A_s = 3.29e-10 at CMB scale. The acoustic transfer's role is to
determine the SPECTRAL SHAPE (n_s, alpha_s) at CMB scale, and to
provide the remaining ~0.80 OOM amplitude correction.

Gate: ACOUSTIC-TRANSFER-68
  PASS: alpha_s(k_CMB) in [-0.015, +0.015] AND A_s gap < 0.3 OOM
  FAIL: |alpha_s(k_CMB)| > 0.019 OR A_s gap > 1.0 OOM
  INFO: intermediate values
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))

import numpy as np
from scipy.interpolate import CubicSpline, interp1d
from scipy.integrate import solve_ivp, cumulative_trapezoid
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    tau_fold, M_KK, M_Pl_reduced,
    S_fold, dS_fold, d2S_fold, H_fold as H_fold_canon,
    dt_transit, v_terminal,
    a0_fold, a2_fold, a4_fold,
    A_s_CMB, PI,
    H_0_GeV, Mpc_to_GeV_inv,
)

# ============================================================================
#  SECTION 1: Load all input data
# ============================================================================

print("=" * 72)
print("ACOUSTIC-TRANSFER-68: Scalar Acoustic Transfer Across 54 Decades")
print("=" * 72)

script_dir = os.path.dirname(os.path.abspath(__file__))

# Load W1-A transit power spectrum
w1a = np.load(os.path.join(script_dir, 's67_transit_ps.npz'), allow_pickle=True)

# Load tensor transfer for comparison
tensor = np.load(os.path.join(script_dir, 's67_acoustic_tensor.npz'), allow_pickle=True)

# Load multifield delta-N
delta_n = np.load(os.path.join(script_dir, 's67_multifield_delta_n.npz'), allow_pickle=True)

# Load spectral action data
zeta_data = np.load(os.path.join(script_dir, 's66_zeta_sa.npz'), allow_pickle=True)

# Load running ns data
running_data = np.load(os.path.join(script_dir, 's66_running_ns.npz'), allow_pickle=True)

# Key constants
c_BLV = 0.485  # scalar sound speed (M_KK units)  # (local)
c_tensor = 1.0  # tensor propagation speed  # (local)
eps_H_fold = 0.022  # slow-roll parameter at fold  # (local)

print(f"\n  Data files loaded successfully.")

# ============================================================================
#  SECTION 2: Reconstruct background from W1-A
# ============================================================================

print(f"\n{'='*72}")
print("SECTION 2: BACKGROUND RECONSTRUCTION")
print(f"{'='*72}")

# Background arrays from W1-A
tau_fine = w1a['tau_fine']       # shape (8000,)
eta_fine = w1a['eta_fine']       # conformal time
a_fine = w1a['a_fine']           # scale factor
z_fine = w1a['z_fine']           # z = a * sqrt(2*eps_H)
eps_H_fine = w1a['eps_H_fine']   # slow-roll parameter
zpp_z = w1a['zpp_z']            # z''/z pump field
zpp_z_fold_val = float(w1a['zpp_z_fold'])  # z''/z at fold

# Transit parameters
k_transit = float(w1a['k_transit'])  # = H_fold / c_BLV = 1209.3 M_KK
H_fold = H_fold_canon

# Tensor data for comparison
app_a_fold = float(tensor['app_a_fold'])  # a''/a at fold
k_tach_tensor = float(tensor['k_tach_tensor'])  # tensor tachyonic threshold
k_tach_scalar = float(tensor['k_tach_scalar'])  # scalar tachyonic threshold

# Scalar mode data
k_grid_rk = w1a['k_grid_rk']    # k values for RK4/5
P_zeta_rk = w1a['P_zeta_rk']    # P_zeta from RK4/5
ns_rk = w1a['ns_rk']            # n_s from RK4/5
alpha_rk = w1a['alpha_rk']      # alpha_s from RK4/5
beta_sq_rk = w1a['beta_sq_rk']  # |beta_k|^2 from RK4/5

valid_mask = np.isfinite(P_zeta_rk) & (P_zeta_rk > 0)
k_valid = k_grid_rk[valid_mask]
P_valid = P_zeta_rk[valid_mask]
ns_valid = ns_rk[valid_mask]

print(f"\n  Transit spectrum: {np.sum(valid_mask)} valid modes")
print(f"  k range: [{k_valid[0]:.1f}, {k_valid[-1]:.1f}] M_KK")
print(f"  P_zeta range: [{P_valid.min():.4e}, {P_valid.max():.4e}]")
print(f"  k_transit = {k_transit:.1f} M_KK")
print(f"  k_tach^S = {k_tach_scalar:.1f} M_KK")
print(f"  z''/z at fold = {zpp_z_fold_val:.4e} M_KK^2")
print(f"  a''/a at fold = {app_a_fold:.4e} M_KK^2")

# ============================================================================
#  SECTION 3: Spectral action S(tau) for extended tau range
# ============================================================================

print(f"\n{'='*72}")
print("SECTION 3: SPECTRAL ACTION AND EXPANSION HISTORY")
print(f"{'='*72}")

# Reconstruct S(tau) exactly as in tensor script
tau_16 = zeta_data['tau_all']
a2_16 = zeta_data['a2']
a4_16 = zeta_data['a4']
a0_const = 6440.0  # (local)

S_bare_L3 = running_data['S_bare_L3']

a2_cal = np.array([np.interp(t, tau_16, a2_16) for t in [0.05, 0.19, 0.22]])
a4_cal = np.array([np.interp(t, tau_16, a4_16) for t in [0.05, 0.19, 0.22]])
A_mat = np.array([[a0_const, a2_cal[0], a4_cal[0]],
                   [a0_const, a2_cal[1], a4_cal[1]],
                   [a0_const, a2_cal[2], a4_cal[2]]])
f0, f2, f4 = np.linalg.solve(A_mat, S_bare_L3[[0, 4, 6]])
S_tau_16 = f0 * a0_const + f2 * a2_16 + f4 * a4_16
cs_S = CubicSpline(tau_16, S_tau_16)

print(f"  S(tau_fold) = {cs_S(tau_fold):.2f} (canon: {S_fold:.2f})")

# Kinetic normalization
dlnS_fold = dS_fold / S_fold
K_norm = dlnS_fold**2 / (2.0 * eps_H_fold)

# Expansion history: how many e-folds of expansion?
tau_lo, tau_hi = 0.10, 0.30
N_fine = 8000  # (local)

# Total e-folds during transit window
a_start = a_fine[0]
a_end = a_fine[-1]
N_transit = np.log(a_end / a_start)

print(f"\n  Transit window: tau in [{tau_lo}, {tau_hi}]")
print(f"  a(start)/a(fold) = {a_start:.6e}")
print(f"  a(end)/a(fold) = {a_end:.6e}")
print(f"  N_transit = {N_transit:.4f} e-folds in transit window")

# ============================================================================
#  SECTION 4: Extended expansion history for 54-decade extrapolation
# ============================================================================

print(f"\n{'='*72}")
print("SECTION 4: EXTENDED EXPANSION HISTORY")
print(f"{'='*72}")

# The transit window covers tau in [0.10, 0.30], giving N ~ 0.17 e-folds.
# To reach CMB scales, we need to cover the full expansion from fold to today.
#
# k_CMB = 0.05 Mpc^{-1}. Convert to M_KK:
# k_CMB = 0.05 * Mpc_to_GeV_inv * M_KK_gravity (in GeV) / M_KK_gravity
# = 0.05 * 1.563e38 / 7.43e16 = 1.05e20 ... no.
# k has dimensions of inverse length. k = 0.05 Mpc^{-1}.
# In natural units: k_CMB = 0.05 / Mpc * (1 Mpc = 1.563e38 GeV^{-1})
# So k_CMB = 0.05 / (1.563e38 GeV^{-1}) = 3.20e-41 GeV
# In M_KK units: k_CMB / M_KK = 3.20e-41 / 7.43e16 = 4.31e-58 M_KK

k_CMB_GeV = 0.05 / Mpc_to_GeV_inv  # GeV
k_CMB_MKK = k_CMB_GeV / M_KK       # dimensionless

print(f"\n  k_CMB = 0.05 Mpc^{{-1}} = {k_CMB_GeV:.4e} GeV = {k_CMB_MKK:.4e} M_KK")
print(f"  k_transit = {k_transit:.1f} M_KK = {k_transit * M_KK:.4e} GeV")
print(f"  Scale ratio: k_transit / k_CMB = {k_transit / k_CMB_MKK:.4e}")
print(f"  Log10 ratio: {np.log10(k_transit / k_CMB_MKK):.1f} decades")

# For the CMB mode to have been superhorizon at the fold, we need:
# k_CMB * c_BLV < sqrt(z''/z) at the fold
# k_CMB * c_BLV = 4.31e-58 * 0.485 = 2.09e-58 << sqrt(z''/z) = 958
# YES: CMB modes are deeply superhorizon throughout the entire transit.

k_CMB_cs = k_CMB_MKK * c_BLV
sqrt_zppz = np.sqrt(zpp_z_fold_val)
print(f"\n  k_CMB * c_BLV = {k_CMB_cs:.4e} M_KK")
print(f"  sqrt(z''/z)   = {sqrt_zppz:.1f} M_KK")
print(f"  Ratio: {k_CMB_cs / sqrt_zppz:.4e}")
print(f"  --> CMB modes are DEEPLY superhorizon. k_CMB << k_tach by 60+ decades.")

# ============================================================================
#  SECTION 5: Superhorizon conservation and the transfer function structure
# ============================================================================

print(f"\n{'='*72}")
print("SECTION 5: SUPERHORIZON CONSERVATION -- THE CENTRAL ARGUMENT")
print(f"{'='*72}")

# THE CRITICAL PHYSICS:
# For adiabatic perturbations, the curvature perturbation zeta = u_k / z
# is CONSERVED on superhorizon scales. This is the Weinberg (2003) theorem.
#
# The mode equation u_k'' + (k^2 c_s^2 - z''/z) u_k = 0 has two solutions:
#   - Growing mode: u_k ~ z (=> zeta = const)
#   - Decaying mode: u_k ~ z * integral(d_eta / z^2) (=> zeta decays)
#
# After horizon exit, the growing mode dominates and zeta freezes.
# The frozen zeta is what we observe at the CMB.
#
# Therefore, the "transfer function" for SCALAR adiabatic modes is:
#   |T(k)|^2 = 1 for all superhorizon modes.
#
# This is NOT an approximation -- it's exact for single-field adiabatic modes.
# The spectral index at the CMB is determined entirely by the k-dependence
# of P_zeta at the time each mode exits the horizon.
#
# The AMPLITUDE, however, depends on WHEN each mode exits the horizon,
# which depends on the expansion history. This is where the delta-N
# formalism enters.

print(f"""
  WEINBERG THEOREM (2003):
  For single-clock adiabatic perturbations, zeta is conserved outside
  the horizon. The curvature perturbation at horizon crossing equals
  the curvature perturbation at any later time:

      zeta(k, t_CMB) = zeta(k, t_exit(k))                       (5.1)

  The power spectrum therefore transfers as:

      P_zeta(k, t_CMB) = P_zeta(k, t_exit(k))                   (5.2)

  The "transfer function" is:

      |T(k)|^2 = P_zeta(k, CMB) / P_zeta(k, transit)
               = [P at horizon exit] / [P at transit computation]

  For modes that are ALREADY superhorizon at the transit computation
  epoch (all modes below k_tach ~ 1975 M_KK), zeta is ALREADY frozen.
  Therefore |T(k)|^2 = 1 for these modes, and P_zeta(k, CMB) is
  simply the P_zeta(k) computed in W1-A.

  HOWEVER: The W1-A computation extracted P_zeta in M_KK units.
  The conversion to dimensionless P_zeta involves:

      P_zeta(k) = (k^3 / 2*pi^2) * |u_k/z|^2                   (5.3)

  This is already dimensionless. The question is whether the P_zeta
  computed in W1-A at transit scale can be directly compared to Planck.
""")

# ============================================================================
#  SECTION 6: Computing the transfer function
# ============================================================================

print(f"{'='*72}")
print("SECTION 6: ACOUSTIC TRANSFER FUNCTION COMPUTATION")
print(f"{'='*72}")

# Strategy: The transfer function has TWO components:
#
# (A) SPECTRAL SHAPE TRANSFER: How does the spectral index change from
#     transit scale to CMB scale?
#
#     At the transit: n_s(k_transit) ~ 4 (deep blue, from k^3 superhorizon
#     scaling). But this is the spectral index of the RAW Bogoliubov
#     spectrum at a SINGLE epoch.
#
#     At the CMB: n_s(k_CMB) ~ 0.965 (nearly scale-invariant).
#
#     The reconciliation: different k-modes EXIT the horizon at DIFFERENT
#     epochs during the transit. Modes that exit earlier see a different
#     z(eta) than modes that exit later. The spectral index at CMB scale
#     is determined by the VARIATION of P_zeta with the exit time.
#
# (B) AMPLITUDE TRANSFER: The absolute amplitude of P_zeta involves
#     the Planck mass / M_KK ratio and the number of e-folds.
#     The multifield delta-N already provides A_s = 3.29e-10.

# The acoustic white hole picture:
# Post-transit, the "flow" (parametrized by the expanding a(eta))
# sets up an effective outward velocity. In the white hole analogy:
#   v(r) ~ H * r (Hubble flow)
#   c_s = c_BLV = 0.485
# The sonic horizon is at r_s where v = c_s, i.e., r_s = c_s / H.
# Modes with k < H/c_s are outside the sonic horizon (superhorizon).

# For the SPECTRAL SHAPE, we need to compute how P_zeta(k) evaluated
# at the FREEZING epoch varies with k. In slow-roll inflation:
#   P_zeta(k) = H^2 / (8*pi^2 * eps * c_s * M_Pl^2) at k = aH/c_s
#   n_s - 1 = -2*eps - eta - s (where s = c_s'/Hc_s)
#
# For the supersonic transit, this slow-roll formula is INAPPLICABLE.
# But the mode equation IS solved in W1-A. We need to interpret the
# W1-A results correctly.

# ============================================================================
#  SECTION 6A: The k^3 factor and its interpretation
# ============================================================================

print(f"\n  SECTION 6A: Interpreting the W1-A spectrum")
print(f"  {'-'*60}")

# In W1-A, P_zeta(k) = (k^3 / 2*pi^2) * |u_k/z|^2 was computed at
# the END of the transit window (tau = 0.30). For modes with k < k_tach,
# |u_k/z|^2 is approximately constant (frozen). The k^3 factor is
# the standard phase-space density of states.
#
# The deep superhorizon limit: u_k ~ z (growing mode), so |u_k/z|^2 = const.
# Then P_zeta ~ k^3 * const => n_s = 4 (deeply blue).
#
# But wait: the STANDARD inflation computation gives P_zeta ~ const
# (nearly scale-invariant) despite the same k^3 factor. Why?
# Because in slow-roll inflation, the mode function at horizon exit is:
#   u_k(exit) ~ H / (sqrt(2 k^3) * c_s)
# so |u_k|^2 ~ H^2 / (2 k^3 c_s^2)
# and P_zeta = k^3/(2pi^2) * H^2/(2 k^3 c_s^2 z_exit^2) ~ H^2/(8pi^2 eps c_s)
# The k^3 CANCELS between phase space and mode function normalization.
#
# In the transit, ALL modes are superhorizon simultaneously (impulsive event).
# They all see the SAME z''/z barrier. So u_k/z ~ const for all k < k_tach.
# The k^3 does NOT cancel.
#
# THIS is the P_zeta = k^3 * const spectrum that W1-A computed.
# And THIS is what the acoustic transfer must process.

# The question: what physical mechanism converts k^3 (n_s=4) to k^{-0.035}
# (n_s=0.965)?

# ============================================================================
#  SECTION 6B: The acoustic white hole transfer mechanism
# ============================================================================

print(f"  SECTION 6B: Acoustic white hole transfer mechanism")
print(f"  {'-'*60}")

# Physical picture from S66 Mack-Transit workshop:
#
# After the transit, the universe expands. Different modes re-enter the
# horizon at different epochs (different values of a(t)). The curvature
# perturbation zeta is conserved outside the horizon. But the OBSERVATION
# of zeta at the CMB requires modes to have been superhorizon for the
# entire post-transit expansion.
#
# The transit spectrum P_zeta(k) ~ k^3 is computed at the transit epoch.
# At that epoch, ALL modes with k < k_tach are superhorizon.
#
# Now, the crucial question: are the CMB modes (k ~ 10^{-58} M_KK)
# EVER sub-horizon during the transit?
#
# Answer: NO. They are superhorizon throughout. Their horizon exit
# happened BEFORE the transit (or rather, they were never sub-horizon
# after the onset of expansion).
#
# In the exflation picture, the expansion starts at the fold and continues.
# A mode with wavenumber k exits the horizon when k*c_BLV = aH.
# For the smallest k (CMB modes), this happens when a is very small,
# i.e., very early in the expansion.
#
# The transfer function is therefore determined by:
# 1. The spectrum of quantum fluctuations at the moment of horizon exit
# 2. Conservation of zeta outside the horizon
#
# For modes that exit the horizon during the transit itself:
# zeta(k) at exit = (H / (2*pi)) * (1 / sqrt(2*eps*c_s)) * (k/aH)^{...}
#
# The standard result for the power spectrum at horizon exit:
# P_zeta(k) = H^2 / (8*pi^2 * eps_H * c_s) evaluated at k*c_s = a*H.
#
# The key: eps_H, H, c_s all vary as the tau parameter evolves.
# Different k-modes have k*c_s = a*H at different values of tau.
# This tau-dependence of eps_H, H gives the spectral tilt.

# ============================================================================
#  SECTION 6C: Horizon crossing computation
# ============================================================================

print(f"  SECTION 6C: Horizon crossing analysis")
print(f"  {'-'*60}")

# At the transit epoch, the comoving Hubble scale is:
# k_H(tau) = a(tau) * H(tau) / c_BLV
#
# Modes exit the horizon when k = k_H(tau), i.e., k*c_BLV = a*H.
# The scale factor a(tau) = a_fold * exp(integral of H/v_tau dtau)

# Reconstruct S, eps_H, H over the extended tau range [0.0, 0.50]
tau_extended = tau_16  # [0.0, 0.05, ..., 0.50]
S_extended = S_tau_16
dS_extended = cs_S(tau_extended, 1)
dlnS_extended = dS_extended / S_extended
eps_H_extended = dlnS_extended**2 / (2.0 * K_norm)
H_extended = H_fold * np.sqrt(S_extended / cs_S(tau_fold))

# Scale factor: integrate d(ln a)/d(tau) = H/v_tau
v_tau = v_terminal
dlna_dtau_ext = H_extended / v_tau

# Cumulative integration for a(tau) -- need fine grid
tau_fine_ext = np.linspace(0.0, 0.50, 10000)
S_fine_ext = cs_S(tau_fine_ext)
H_fine_ext = H_fold * np.sqrt(S_fine_ext / cs_S(tau_fold))
dlna_dtau_fine = H_fine_ext / v_tau
lna_fine_ext = cumulative_trapezoid(dlna_dtau_fine, tau_fine_ext, initial=0.0)
# Normalize: a(fold) = 1
lna_at_fold = np.interp(tau_fold, tau_fine_ext, lna_fine_ext)
lna_fine_ext -= lna_at_fold
a_fine_ext = np.exp(lna_fine_ext)

# Comoving Hubble horizon
k_H_fine = a_fine_ext * H_fine_ext / c_BLV  # in M_KK

print(f"\n  Extended expansion history:")
for tau_val in [0.0, 0.05, 0.10, 0.15, 0.19, 0.25, 0.30, 0.40, 0.50]:
    idx = np.argmin(np.abs(tau_fine_ext - tau_val))
    print(f"    tau = {tau_val:.2f}: a = {a_fine_ext[idx]:.6e}, "
          f"H = {H_fine_ext[idx]:.2f}, k_H = {k_H_fine[idx]:.4e} M_KK")

# E-folds from tau=0 to tau=0.50
N_total_050 = lna_fine_ext[-1] - lna_fine_ext[0]
print(f"\n  Total e-folds (tau=0 to 0.50): {N_total_050:.4f}")
print(f"  Total e-folds (tau=0.10 to 0.30): {N_transit:.4f}")

# ============================================================================
#  SECTION 7: Spectral index from horizon crossing time variation
# ============================================================================

print(f"\n{'='*72}")
print("SECTION 7: SPECTRAL INDEX FROM HORIZON CROSSING")
print(f"{'='*72}")

# For a mode with wavenumber k that exits the horizon at tau_exit(k):
#   k * c_BLV = a(tau_exit) * H(tau_exit)
#
# The power spectrum at horizon exit (Mukhanov formula):
#   P_zeta(k) = 1 / (2 * eps_H * c_BLV) * (H / (2*pi))^2 / M_Pl^2     (7.1)
#
# where everything is evaluated at tau_exit(k), and M_Pl = M_Pl_reduced.
#
# But we must express this in M_KK units. H is already in M_KK units.
# M_Pl / M_KK = ?

M_Pl_over_MKK = M_Pl_reduced / M_KK
print(f"\n  M_Pl / M_KK = {M_Pl_over_MKK:.4f}")
print(f"  (M_Pl / M_KK)^2 = {M_Pl_over_MKK**2:.4f}")

# Standard slow-roll formula (for reference):
# P_zeta(k) = H^2 / (8*pi^2 * eps_H * c_s * M_Pl^2)
# All in GeV: H in GeV, M_Pl in GeV => P_zeta dimensionless
# In M_KK units: H in M_KK, M_Pl in M_KK => same formula

# Evaluate at the fold:
H_fold_MKK = H_fold  # already in M_KK units
eps_H_at_fold = eps_H_fold
c_s = c_BLV

# The standard formula
P_zeta_slowroll_fold = H_fold_MKK**2 / (8.0 * PI**2 * eps_H_at_fold * c_s * M_Pl_over_MKK**2)
print(f"\n  Slow-roll P_zeta at fold:")
print(f"    H_fold = {H_fold_MKK:.4f} M_KK")
print(f"    eps_H = {eps_H_at_fold:.4f}")
print(f"    c_s = {c_s:.4f}")
print(f"    P_zeta(SR) = {P_zeta_slowroll_fold:.4e}")
print(f"    A_s(Planck) = {A_s_CMB:.4e}")
print(f"    log10(P_zeta(SR) / A_s) = {np.log10(P_zeta_slowroll_fold / A_s_CMB):.2f}")

# Now: the spectral index
# n_s - 1 = d ln P_zeta / d ln k = -2*eps - eta - s
# where eta = deps/dlnk, s = dc_s/dlnk / c_s
#
# In the transit, these parameters vary with tau, not with k.
# The chain rule: d/dlnk = (dtau/dlnk) * d/dtau
#
# From k*c_BLV = a*H (horizon exit):
# dlnk = d ln(aH/c_s)
# At fixed c_s: dlnk = d ln(aH) = d(ln a + ln H)
#              = (H/v_tau + (1/2)*(dS/dtau)/S) dtau  [using H ~ sqrt(S)]
#
# So dtau/dlnk = v_tau / (H + v_tau * (dS/dtau)/(2S))

# Compute eps_H, dS/S, etc. on the fine grid
dS_fine_ext = cs_S(tau_fine_ext, 1)
dlnS_fine_ext = dS_fine_ext / S_fine_ext
eps_H_fine_ext = dlnS_fine_ext**2 / (2.0 * K_norm)

# dtau/dlnk at the fold
dS_at_fold = cs_S(tau_fold, 1)
dlnS_at_fold = dS_at_fold / cs_S(tau_fold)
dlnH_dtau = dlnS_at_fold / 2.0  # H ~ sqrt(S)
dlna_dtau_fold = H_fold / v_tau

dtau_dlnk_fold = 1.0 / (dlna_dtau_fold + dlnH_dtau)
print(f"\n  Spectral index ingredients at fold:")
print(f"    d(lnS)/d(tau) = {dlnS_at_fold:.4f}")
print(f"    d(lnH)/d(tau) = {dlnH_dtau:.4f}")
print(f"    d(lna)/d(tau) = {dlna_dtau_fold:.4f}")
print(f"    d(tau)/d(lnk) = {dtau_dlnk_fold:.6f}")

# deps_H/dtau at the fold (from running_ns data)
deps_dtau = float(running_data['deps_dtau_L3'])
print(f"    d(eps_H)/d(tau) = {deps_dtau:.6f}")

# eta parameter: eta = (deps_H/dtau) * (dtau/dlnk) / eps_H
# Actually: eta = d(ln eps_H)/d(lnk) = (deps_H/dtau) * (dtau/dlnk) / eps_H
# n_s - 1 = -2*eps_H - eta - s (standard slow-roll)
# But for impulsive transit, we use the full formula:
# n_s - 1 = d ln P_zeta / d ln k
# where P_zeta = H^2 / (8*pi^2 * eps_H * c_s * M_Pl^2)
# d ln P_zeta / d ln k = 2 * d ln H / d ln k - d ln eps_H / d ln k - d ln c_s / d ln k

# d ln H / d ln k = (d ln H / d tau) * (d tau / d ln k)
dlnH_dlnk = dlnH_dtau * dtau_dlnk_fold
# d ln eps_H / d ln k
dlneps_dlnk = (deps_dtau / eps_H_at_fold) * dtau_dlnk_fold
# c_BLV is constant: d ln c_s / d ln k = 0

n_s_analytic = 1.0 + 2.0 * dlnH_dlnk - dlneps_dlnk
print(f"\n  Analytic spectral index at fold:")
print(f"    2 * d(ln H)/d(ln k) = {2*dlnH_dlnk:.6f}")
print(f"    d(ln eps_H)/d(ln k) = {dlneps_dlnk:.6f}")
print(f"    n_s = 1 + 2*dlnH/dlnk - dlneps/dlnk = {n_s_analytic:.6f}")

# Compare with running ns data
ns_bare_L3 = float(running_data['ns_bare_L3'])
ns_bcs_L3 = float(running_data['ns_bcs_L3'])
print(f"    n_s (running_ns L3, bare) = {ns_bare_L3:.6f}")
print(f"    n_s (running_ns L3, BCS)  = {ns_bcs_L3:.6f}")

# ============================================================================
#  SECTION 8: Running of spectral index alpha_s
# ============================================================================

print(f"\n{'='*72}")
print("SECTION 8: RUNNING OF SPECTRAL INDEX")
print(f"{'='*72}")

# alpha_s = d(n_s)/d(ln k)
# From the running_ns computation:
alpha_s_L3 = float(running_data['alpha_s_L3'])
alpha_s_L4 = float(running_data['alpha_s_L4'])
alpha_s_bare_L3 = float(running_data['alpha_s_bare_L3'])
alpha_s_bare_L4 = float(running_data['alpha_s_bare_L4'])

print(f"\n  Running from S66 computation:")
print(f"    alpha_s (L3, 1-loop) = {alpha_s_L3:.6f}")
print(f"    alpha_s (L4, 1-loop) = {alpha_s_L4:.6f}")
print(f"    alpha_s (L3, bare)   = {alpha_s_bare_L3:.6f}")
print(f"    alpha_s (L4, bare)   = {alpha_s_bare_L4:.6f}")
print(f"    Planck alpha_s       = {-0.0045:.6f} +/- {0.0067:.6f}")

# The W1-A computation gave alpha_s = 0 in the superhorizon plateau.
# But that's because ALL modes were evaluated at the SAME epoch.
# The PHYSICAL alpha_s involves evaluating P_zeta at different tau_exit(k).

# ============================================================================
#  SECTION 9: Full acoustic transfer computation
# ============================================================================

print(f"\n{'='*72}")
print("SECTION 9: FULL ACOUSTIC TRANSFER COMPUTATION")
print(f"{'='*72}")

# The transfer function approach:
#
# We compute P_zeta(k) using the horizon-crossing formula:
#   P_zeta(k) = H(tau_exit)^2 / (8*pi^2 * eps_H(tau_exit) * c_BLV * (M_Pl/M_KK)^2)
#
# where tau_exit is determined by k*c_BLV = a(tau_exit) * H(tau_exit).
#
# This gives the PHYSICAL spectrum that is observed at the CMB.
# The transit Bogoliubov computation (W1-A) gives the spectrum at a fixed
# epoch. The transfer function converts between these.

# Step 1: For each k, find tau_exit where k*c_BLV = a(tau)*H(tau)
# k_H(tau) = a(tau) * H(tau) / c_BLV is the comoving Hubble scale

# We need k_H(tau) on the fine extended grid
# Already computed: k_H_fine = a_fine_ext * H_fine_ext / c_BLV

print(f"\n  Comoving Hubble scale k_H(tau) = a*H/c_BLV:")
print(f"    k_H(tau=0.00) = {k_H_fine[0]:.4e} M_KK")
print(f"    k_H(tau=0.19) = {np.interp(tau_fold, tau_fine_ext, k_H_fine):.4e} M_KK")
print(f"    k_H(tau=0.50) = {k_H_fine[-1]:.4e} M_KK")

# k_H is a MONOTONICALLY INCREASING function of tau (since a grows
# faster than H decreases). This means:
# - Smaller k exits the horizon at EARLIER tau
# - Larger k exits at LATER tau

# Step 2: The spectrum P_zeta(k) = H^2/(8*pi^2 * eps * c_s * M_Pl^2) at exit

# Create a fine grid of k values spanning from deeply superhorizon to
# near the transit scale
N_k_transfer = 1000
k_min_log = np.log10(k_H_fine[k_H_fine > 0].min()) - 1
k_max_log = np.log10(k_transit)
k_transfer = np.logspace(k_min_log, k_max_log, N_k_transfer)

print(f"\n  Transfer k-grid: [{k_transfer[0]:.4e}, {k_transfer[-1]:.4e}] M_KK ({N_k_transfer} points)")

# For each k, find tau_exit and compute P_zeta
tau_exit_arr = np.zeros(N_k_transfer)
P_zeta_transfer = np.zeros(N_k_transfer)
H_at_exit = np.zeros(N_k_transfer)
eps_at_exit = np.zeros(N_k_transfer)
a_at_exit = np.zeros(N_k_transfer)

# Splines for interpolation
cs_H_ext = CubicSpline(tau_fine_ext, H_fine_ext)
cs_eps_ext = CubicSpline(tau_fine_ext, eps_H_fine_ext)
cs_a_ext = CubicSpline(tau_fine_ext, a_fine_ext)
cs_kH = CubicSpline(tau_fine_ext, k_H_fine)

for ik, k in enumerate(k_transfer):
    # Find tau where k_H(tau) = k, i.e., a(tau)*H(tau)/c_BLV = k
    # k_H is monotonically increasing, so use interpolation
    if k < k_H_fine[0]:
        # Mode exits before tau=0: assign tau=0
        tau_exit_arr[ik] = 0.0
    elif k > k_H_fine[-1]:
        # Mode never exits: assign tau=0.50
        tau_exit_arr[ik] = 0.50
    else:
        # Invert k_H(tau) = k
        # Since k_H is increasing, find first crossing
        idx_cross = np.searchsorted(k_H_fine, k)
        if idx_cross == 0:
            tau_exit_arr[ik] = tau_fine_ext[0]
        elif idx_cross >= len(tau_fine_ext):
            tau_exit_arr[ik] = tau_fine_ext[-1]
        else:
            # Linear interpolation between idx_cross-1 and idx_cross
            t0 = tau_fine_ext[idx_cross - 1]
            t1 = tau_fine_ext[idx_cross]
            k0 = k_H_fine[idx_cross - 1]
            k1 = k_H_fine[idx_cross]
            tau_exit_arr[ik] = t0 + (t1 - t0) * (k - k0) / (k1 - k0)

    te = tau_exit_arr[ik]
    H_e = float(cs_H_ext(te))
    eps_e = float(cs_eps_ext(te))
    a_e = float(cs_a_ext(te))

    H_at_exit[ik] = H_e
    eps_at_exit[ik] = eps_e
    a_at_exit[ik] = a_e

    # Ensure eps_H > 0 for the formula
    if eps_e <= 0:
        eps_e = eps_H_fold  # fallback

    # P_zeta(k) = H^2 / (8*pi^2 * eps * c_s * M_Pl^2)
    # With H in M_KK, M_Pl in M_KK:
    P_zeta_transfer[ik] = H_e**2 / (8.0 * PI**2 * eps_e * c_BLV * M_Pl_over_MKK**2)

# Report
print(f"\n  Horizon crossing results:")
valid_transfer = P_zeta_transfer > 0
for k_val, label in [(k_transfer[0], "k_min"),
                      (k_transit, "k_transit"),
                      (k_transfer[-1], "k_max")]:
    idx = np.argmin(np.abs(k_transfer - k_val))
    print(f"    {label} = {k_transfer[idx]:.4e} M_KK:")
    print(f"      tau_exit = {tau_exit_arr[idx]:.4f}")
    print(f"      H = {H_at_exit[idx]:.4f} M_KK")
    print(f"      eps_H = {eps_at_exit[idx]:.6f}")
    print(f"      a = {a_at_exit[idx]:.6e}")
    print(f"      P_zeta = {P_zeta_transfer[idx]:.4e}")

# ============================================================================
#  SECTION 10: Spectral index and running from the transfer
# ============================================================================

print(f"\n{'='*72}")
print("SECTION 10: SPECTRAL INDEX AND RUNNING AT CMB SCALE")
print(f"{'='*72}")

# Compute n_s(k) and alpha_s(k) from the transferred spectrum
ln_k = np.log(k_transfer)
ln_P = np.log(np.maximum(P_zeta_transfer, 1e-300))

# Spectral index: n_s(k) = d ln P / d ln k
ns_transfer_arr = np.gradient(ln_P, ln_k)

# Smooth with a running average
smooth_win = 15
kernel = np.ones(smooth_win) / smooth_win
if len(ns_transfer_arr) > 2 * smooth_win:
    ns_transfer_arr_smooth = np.convolve(ns_transfer_arr, kernel, mode='same')
else:
    ns_transfer_arr_smooth = ns_transfer_arr

# Running: alpha_s(k) = d n_s / d ln k
alpha_s_transfer_arr = np.gradient(ns_transfer_arr_smooth, ln_k)
if len(alpha_s_transfer_arr) > 2 * smooth_win:
    alpha_s_transfer_smooth = np.convolve(alpha_s_transfer_arr, kernel, mode='same')
else:
    alpha_s_transfer_smooth = alpha_s_transfer_arr

# Report at several k scales within our computed range
print(f"\n  Spectral index across transfer k-range:")
print(f"  {'k (M_KK)':<20} {'tau_exit':<12} {'P_zeta':<14} {'n_s':<12} {'alpha_s':<12}")
print(f"  {'-'*70}")

# Report at geometrically spaced points
for ik in np.linspace(0, N_k_transfer - 1, 15, dtype=int):
    print(f"  {k_transfer[ik]:<20.4e} {tau_exit_arr[ik]:<12.4f} "
          f"{P_zeta_transfer[ik]:<14.4e} {ns_transfer_arr_smooth[ik]:<12.4f} "
          f"{alpha_s_transfer_smooth[ik]:<12.6f}")

# ============================================================================
#  SECTION 11: Extrapolation to CMB scale
# ============================================================================

print(f"\n{'='*72}")
print("SECTION 11: EXTRAPOLATION TO CMB SCALE")
print(f"{'='*72}")

# The CMB mode k_CMB ~ 10^{-58} M_KK exits the horizon at VERY early tau.
# Our tau grid starts at tau = 0. At tau = 0:
# a(0) = a_fold * exp(-integral of H/v_tau from 0 to fold)
# This is very small.
#
# k_H(tau=0) = a(0) * H(0) / c_BLV
# If k_CMB < k_H(0), the CMB mode exits even before our computation starts.
#
# Let's check:

k_H_at_0 = k_H_fine[0]
print(f"\n  k_H(tau=0) = {k_H_at_0:.4e} M_KK")
print(f"  k_CMB = {k_CMB_MKK:.4e} M_KK")
print(f"  k_CMB / k_H(0) = {k_CMB_MKK / k_H_at_0:.4e}")

if k_CMB_MKK < k_H_at_0:
    print(f"  --> CMB mode exits BEFORE tau = 0.")
    print(f"      Need to extend tau range backward.")
else:
    print(f"  --> CMB mode exits within tau = [0, 0.50] range.")

# Since k_CMB << k_H(0), the CMB mode exits the horizon before the
# spectral action description begins. We need to model the pre-transit
# epoch.
#
# PHYSICAL ARGUMENT:
# Before the transit, the Jensen deformation parameter tau is in the
# range [0, tau_fold]. The spectral action S(tau) and its derivatives
# determine H and eps_H. At very small tau:
# S(tau) ~ S(0) + S'(0)*tau + ... (Taylor expansion from the UV fixed point)
#
# The key insight: at tau = 0, S(0) = S_tau_16[0] and its derivatives
# determine the initial conditions for expansion.

# For the spectral index, what matters is the VARIATION of H^2/(eps*c_s)
# near the fold, because modes near the fold dominate the observation.
# The CMB mode is so deeply superhorizon that its precise exit time
# doesn't matter for n_s -- it's in the plateau.

# The spectral index at CMB scale is determined by the variation of the
# slow-roll parameters at the FOLD, because the CMB-relevant modes exit
# the horizon during the transit period (in a standard inflation picture)
# or, in the exflation picture, their spectral properties are set by the
# global expansion history.

# CRITICAL REALIZATION:
# In exflation, there is no separate "slow-roll era" with 60+ e-folds.
# The total expansion is N ~ 0.17 e-folds in the transit window.
# The CMB modes are superhorizon from the START. Their spectrum is set
# by the initial quantum state, not by horizon crossing during slow-roll.

# This means the P_zeta we observe at the CMB is:
# (a) The Bogoliubov spectrum from W1-A (for modes in the computed k range)
# (b) For modes outside the computed range, extrapolation using the
#     superhorizon scaling: P_zeta ~ k^3 * const (the "k^3 disaster").

# The delta-N formalism RESOLVES the amplitude by providing the
# correct conversion between the multi-field GGE fluctuations and zeta.
# A_s(multi) = 3.29e-10 from W3-B.

# ============================================================================
#  SECTION 12: The transfer function |T(k)|^2
# ============================================================================

print(f"\n{'='*72}")
print("SECTION 12: TRANSFER FUNCTION |T(k)|^2")
print(f"{'='*72}")

# The transfer function connects transit-scale P to CMB-scale P:
# P_zeta(k_CMB) = |T|^2 * P_zeta(k_transit)
#
# From the W1-A computation:
# P_zeta(k_transit) = 2.56e6 (at k = 1209 M_KK)
# From Planck: P_zeta(k_CMB) = A_s = 2.1e-9
#
# So |T|^2 = 2.1e-9 / 2.56e6 = 8.2e-16
# log10(|T|^2) = -15.1

P_transit = float(w1a['P_zeta_at_transit'])
T_sq_needed = A_s_CMB / P_transit
log10_T_sq = np.log10(T_sq_needed)

print(f"\n  Transit amplitude: P_zeta(k_transit) = {P_transit:.4e}")
print(f"  CMB amplitude:     A_s = {A_s_CMB:.4e}")
print(f"  Required |T|^2 = {T_sq_needed:.4e}")
print(f"  log10(|T|^2) = {log10_T_sq:.2f}")

# The multifield delta-N provides A_s = 3.29e-10 (gap = 0.80 OOM).
# This delta-N computation already accounts for the multi-field conversion.
A_s_multi = float(delta_n['A_s_multi_m1'])
gap_multi_OOM = float(delta_n['gap_m1_OOM'])
print(f"\n  Multifield delta-N: A_s = {A_s_multi:.4e}")
print(f"  Gap from Planck: {gap_multi_OOM:.2f} OOM")

# ============================================================================
#  SECTION 13: Decomposing the transfer into geometric + conversion
# ============================================================================

print(f"\n{'='*72}")
print("SECTION 13: TRANSFER DECOMPOSITION")
print(f"{'='*72}")

# The 15.1 OOM gap between P(transit) and A_s has two components:
#
# (A) GEOMETRIC DILUTION: The k^3 factor. The transit spectrum has
#     P ~ k^3 for k < k_tach. Going from k = k_transit to k = k_CMB:
#     (k_CMB / k_transit)^3 = (4.31e-58 / 1209)^3 = 10^{-183}
#     This is WAY too much. The k^3 scaling is for modes at the SAME
#     epoch, not for the physical spectrum across different exit times.
#
# (B) CONVERSION: The delta-N formalism converts from the single-field
#     Bogoliubov spectrum to the multi-field curvature perturbation.
#     This is what W3-B computes.
#
# The correct decomposition:
# P_zeta(k=k_transit, SR) = H^2/(8*pi^2*eps*c_s*M_Pl^2) = P_SR
# P_zeta(k=k_transit, W1A) = 2.56e6 (from mode equation)
#
# The ratio P_SR / P_W1A tells us the conversion factor.

print(f"\n  P_zeta(transit, slow-roll formula) = {P_zeta_slowroll_fold:.4e}")
print(f"  P_zeta(transit, W1-A Bogoliubov)   = {P_transit:.4e}")
print(f"  Ratio (SR / W1-A) = {P_zeta_slowroll_fold / P_transit:.4e}")
print(f"  log10 ratio = {np.log10(P_zeta_slowroll_fold / P_transit):.2f}")

# The slow-roll formula gives P_zeta ~ 10^{-9} directly when evaluated
# at the fold with the correct M_Pl/M_KK ratio. The W1-A computation
# gives P ~ 10^{6} because it uses M_KK-unit normalization.
#
# The difference is the (M_Pl/M_KK)^2 factor and the mode function
# normalization convention.

# Let's be precise about the transfer function structure.
# In the W1-A computation:
# P_zeta(k) = (k^3 / 2*pi^2) * |u_k/z|^2
# where u_k has dimensions of M_KK^{-1} (set by Bunch-Davies normalization
# in M_KK units), and z = a*sqrt(2*eps_H) is dimensionless.
# So P_zeta has dimensions of M_KK^3 * M_KK^{-2} = M_KK ... no.
# Actually, k is in M_KK, |u_k|^2 has dimensions of M_KK^{-2} (from
# u_k ~ 1/sqrt(2*omega_k) ~ M_KK^{-1}), and z is dimensionless.
# So P_zeta = k^3 * |u_k|^2 / z^2 / (2*pi^2) has dimensions of M_KK.
#
# Wait -- P_zeta should be dimensionless. Let me trace the units carefully.
#
# In natural units where everything is in M_KK:
# The mode function is v = z * zeta. The field zeta is dimensionless
# (curvature perturbation). z = a*sqrt(2*eps_H) is dimensionless
# (a is dimensionless, eps_H is dimensionless).
# So v is dimensionless. Then u_k'' + omega^2 u_k = 0, with eta
# having dimensions of M_KK^{-1}. For the mode function:
# u_k ~ 1/sqrt(2*omega) where omega has dimensions M_KK.
# So u_k ~ M_KK^{-1/2}.
# |u_k/z|^2 ~ M_KK^{-1}.
# k^3 ~ M_KK^3.
# P = k^3/(2*pi^2) * |u_k/z|^2 ~ M_KK^2.
#
# But the physical P_zeta is dimensionless!
# The issue: the PHYSICAL mode function includes hbar and the
# gravitational normalization.
# P_zeta = (1/(2*eps_H)) * (H/(2*pi*M_Pl))^2 at horizon crossing.
# This is dimensionless when H and M_Pl are in the same units.

# RESOLUTION: The W1-A P_zeta is in M_KK units and needs to be divided
# by M_Pl^2/M_KK^2 to become the physical dimensionless P_zeta.
# Actually, the Mukhanov variable v = z*zeta has canonical normalization
# [v, v'] = i*hbar. In natural units (hbar=1), v ~ M_KK^{-1/2}.
# P_zeta = (k^3/2pi^2)*|v/(az)|^2 where v is the PHYSICAL mode.
# But in W1-A, the mode function u_k is normalized in M_KK units.
# The physical P_zeta involves the gravitational coupling:
# P_zeta^{phys} = P_zeta^{W1A} / (2 * M_Pl^2 / M_KK^2)
#
# Let me just use the slow-roll formula as calibration:

# From the slow-roll formula: P_zeta = H^2 / (8*pi^2 * eps * c_s * M_Pl^2)
# Numerically: H_fold = 586.5 M_KK, eps = 0.022, c_s = 0.485
# M_Pl = 32.78 M_KK
# P_zeta(SR) = 586.5^2 / (8*pi^2 * 0.022 * 0.485 * 32.78^2)
#            = 343978 / (8 * 9.87 * 0.022 * 0.485 * 1074.5)
#            = 343978 / 89.81 = 3831

# Wait, let me recalculate more carefully
numer_SR = H_fold_MKK**2
denom_SR = 8.0 * PI**2 * eps_H_at_fold * c_BLV * M_Pl_over_MKK**2
P_SR_check = numer_SR / denom_SR
print(f"\n  Detailed slow-roll check:")
print(f"    H^2 = {numer_SR:.4e}")
print(f"    8*pi^2*eps*c_s*M_Pl^2 = {denom_SR:.4e}")
print(f"    P_zeta(SR) = {P_SR_check:.4e}")

# This P_SR is already dimensionless because H and M_Pl are in the same
# units (M_KK). The ratio H/M_Pl ~ 18 >> 1 (!) means we're at Planck
# scale... H = 586 M_KK, M_Pl = 32.8 M_KK => H/M_Pl = 17.9.
#
# This is a HUGE H/M_Pl ratio, completely outside slow-roll.
# In standard inflation, H/M_Pl ~ 10^{-5}. Here it's 18.
# This means the standard slow-roll formula is NOT reliable.

print(f"\n  H_fold / M_Pl = {H_fold_MKK / M_Pl_over_MKK:.4f}")
print(f"  --> H >> M_Pl (Planck scale physics!)")
print(f"  --> Standard slow-roll formula is UNRELIABLE.")
print(f"  --> Must use the Bogoliubov computation (W1-A) directly.")

# But the W1-A computation gives P in M_KK units with specific normalization.
# We need to convert.

# The proper conversion: in W1-A, the Mukhanov variable is normalized as
# u_k(eta_in) = 1/sqrt(2*omega_k) (Bunch-Davies).
# The physical curvature perturbation:
# P_zeta(k) = (k^3/(2*pi^2)) * |u_k/(a*sqrt(2*eps_H))|^2
# where u_k is in M_KK^{-1/2} units (from Bunch-Davies).
#
# The gravitational coupling enters through z = a*sqrt(2*eps_H)*(M_Pl/M_KK).
# But in the W1-A computation, z = a*sqrt(2*eps_H) WITHOUT the M_Pl factor.
# To get the PHYSICAL dimensionless P_zeta, we need to divide by (M_Pl/M_KK)^2.

P_phys_transit = P_transit / M_Pl_over_MKK**2
print(f"\n  PHYSICAL P_zeta at transit:")
print(f"    P_W1A = {P_transit:.4e} (M_KK units)")
print(f"    (M_Pl/M_KK)^2 = {M_Pl_over_MKK**2:.4e}")
print(f"    P_phys = P_W1A / (M_Pl/M_KK)^2 = {P_phys_transit:.4e}")
print(f"    A_s(Planck) = {A_s_CMB:.4e}")

gap_physical_OOM = np.log10(P_phys_transit / A_s_CMB)
print(f"    Physical gap: {gap_physical_OOM:.2f} OOM")

# The physical P_zeta at transit scale is P_transit / M_Pl_over_MKK^2.
# Compare this to what the delta-N gives:
print(f"\n  Comparison with delta-N (W3-B):")
print(f"    A_s (delta-N, M1) = {A_s_multi:.4e}")
print(f"    A_s (physical, direct) = {P_phys_transit:.4e}")
print(f"    A_s (Planck) = {A_s_CMB:.4e}")

# ============================================================================
#  SECTION 14: Physical transfer function with proper normalization
# ============================================================================

print(f"\n{'='*72}")
print("SECTION 14: PHYSICAL TRANSFER FUNCTION")
print(f"{'='*72}")

# The W1-A computed P_zeta(k) = (k^3/2pi^2) * |u_k/z|^2 in M_KK units.
# The physical P_zeta = P_W1A / M_{Pl,eff}^2 where M_{Pl,eff}^2 appears
# from the gravitational normalization of the Mukhanov variable.
#
# In the standard treatment: v = z*R where z = a*dot(phi)/H and
# R is the comoving curvature perturbation. The action for v is:
# S = (1/2) integral [v'^2 - c_s^2*(grad v)^2 + z''/z * v^2] d^3x deta
#
# The gravitational coupling is ALREADY in z through the relation
# z = a*sqrt(2*eps_H)*M_Pl. In the W1-A computation, M_Pl was not
# included in z (z = a*sqrt(2*eps_H)).
#
# Therefore: z_phys = z_W1A * M_Pl/M_KK
# P_zeta = (k^3/2pi^2) * |u_k/z_phys|^2 = P_W1A / (M_Pl/M_KK)^2

# Convert the ENTIRE W1-A spectrum to physical units
P_phys = P_valid / M_Pl_over_MKK**2

print(f"\n  Physical P_zeta spectrum:")
print(f"  {'k (M_KK)':<15} {'P_W1A':<15} {'P_phys':<15} {'n_s'}")
print(f"  {'-'*60}")
for ik in np.linspace(0, len(k_valid)-1, 12, dtype=int):
    print(f"  {k_valid[ik]:<15.2f} {P_valid[ik]:<15.4e} {P_phys[ik]:<15.4e} {ns_valid[ik]:<10.3f}")

# The physical spectrum SHAPE (n_s) is the same as W1-A: dividing by a
# constant doesn't change the spectral index.
#
# So: n_s(physical) = n_s(W1A) ~ 4 in the superhorizon plateau.
# alpha_s(physical) = alpha_s(W1A) ~ 0 in the superhorizon plateau.
#
# This is CORRECT at the transit scale. The question is whether the
# spectral index CHANGES as we go to CMB scale.

# ============================================================================
#  SECTION 15: The spectral index at CMB scale
# ============================================================================

print(f"\n{'='*72}")
print("SECTION 15: SPECTRAL INDEX AT CMB SCALE")
print(f"{'='*72}")

# The transfer function for the spectral SHAPE:
#
# In the horizon-crossing picture:
# P_zeta(k) = H(tau_exit(k))^2 / (8*pi^2 * eps(tau_exit(k)) * c_s * M_Pl^2)
#
# The spectral index is:
# n_s - 1 = d ln P / d ln k = d ln(H^2/(eps*c_s)) / d ln k
#         = 2*(dH/H) / dlnk - (deps/eps) / dlnk
#
# Using dlnk = d ln(aH/c_s) = (H/v_tau + dlnH/dtau) * dtau:
#
# n_s - 1 = (2*dlnH/dtau - dlneps/dtau) / (H/v_tau + dlnH/dtau)

# Compute this on the fine grid
dlnH_dtau_fine = cs_S(tau_fine_ext, 1) / (2.0 * S_fine_ext)
dlneps_dtau_fine = np.gradient(np.log(np.maximum(eps_H_fine_ext, 1e-30)), tau_fine_ext)
dlna_dtau_fine_2 = H_fine_ext / v_tau

# d ln k / d tau = d ln(aH/c_s) / d tau = d(lna)/dtau + d(lnH)/dtau
dlnk_dtau = dlna_dtau_fine_2 + dlnH_dtau_fine

# n_s - 1 = (2*dlnH/dtau - dlneps/dtau) / dlnk/dtau
ns_minus_1_fine = (2.0 * dlnH_dtau_fine - dlneps_dtau_fine) / dlnk_dtau

# Smooth
ns_fine_smooth = np.convolve(ns_minus_1_fine, np.ones(50)/50, mode='same') + 1.0

print(f"\n  Spectral index from horizon-crossing formula:")
print(f"  {'tau':<8} {'H':<12} {'eps_H':<12} {'n_s - 1':<12} {'n_s'}")
print(f"  {'-'*50}")
for tau_val in [0.00, 0.05, 0.10, 0.15, 0.19, 0.22, 0.25, 0.30, 0.40, 0.50]:
    idx = np.argmin(np.abs(tau_fine_ext - tau_val))
    # Avoid edge effects
    if idx < 50 or idx > len(ns_fine_smooth) - 50:
        continue
    print(f"  {tau_val:<8.2f} {H_fine_ext[idx]:<12.4f} {eps_H_fine_ext[idx]:<12.6f} "
          f"{ns_fine_smooth[idx]-1:<12.6f} {ns_fine_smooth[idx]:<12.6f}")

# The n_s AT THE FOLD (where the transit happens):
idx_fold = np.argmin(np.abs(tau_fine_ext - tau_fold))
ns_at_fold = ns_fine_smooth[idx_fold]
print(f"\n  n_s at fold (tau = {tau_fold}): {ns_at_fold:.6f}")
print(f"  n_s (S66 running_ns, bare L3): {ns_bare_L3:.6f}")
print(f"  n_s (S66 running_ns, BCS L3):  {ns_bcs_L3:.6f}")
print(f"  n_s (Planck 2018): 0.9649 +/- 0.0042")

# alpha_s from the variation of n_s with tau
dns_dtau = np.gradient(ns_fine_smooth, tau_fine_ext)
alpha_s_fine = dns_dtau * (1.0 / dlnk_dtau)

# Smooth
alpha_s_fine_smooth = np.convolve(alpha_s_fine, np.ones(50)/50, mode='same')

alpha_s_at_fold = alpha_s_fine_smooth[idx_fold]
print(f"\n  alpha_s at fold: {alpha_s_at_fold:.6f}")
print(f"  alpha_s (S66 running_ns, L3): {alpha_s_L3:.6f}")
print(f"  alpha_s (S66 running_ns, L4): {alpha_s_L4:.6f}")
print(f"  alpha_s (Planck 2018): -0.0045 +/- 0.0067")

# ============================================================================
#  SECTION 16: The delta-N acoustic transfer contribution
# ============================================================================

print(f"\n{'='*72}")
print("SECTION 16: DELTA-N ACOUSTIC TRANSFER")
print(f"{'='*72}")

# The multifield delta-N computation (W3-B) found:
# A_s(M1) = 3.29e-10 (0.80 OOM below Planck)
# This uses three GGE branches: acoustic (0.13%), Leggett (0.44%), optical (99.4%)
#
# The transfer function from W1-A to physical P_zeta:
# 1. Divide by (M_Pl/M_KK)^2: removes M_KK normalization -> P_phys ~ 2380
# 2. The delta-N factors: each branch contributes (dN/dsigma_i)^2 * sigma_i^2
#    Enhancement M1 = 1.786e-12 (from W3-B)

enhancement_m1 = float(delta_n['enhancement_m1'])
enhancement_m2 = float(delta_n['enhancement_m2'])

print(f"\n  Multifield enhancement factors:")
print(f"    M1 (optimal): {enhancement_m1:.4e}")
print(f"    M2 (minimal): {enhancement_m2:.4e}")

# The complete transfer:
# P_phys = P_W1A / (M_Pl/M_KK)^2 ~ 2380
# P_multi = P_phys * enhancement * (additional k-dep factors)
# A_s = P_multi at k_CMB

# Let's compute what the transfer function must accomplish:
# A_s(Planck) = 2.1e-9
# P_phys(transit) = 2380
# Required total suppression = 2.1e-9 / 2380 = 8.82e-13
# The delta-N gives enhancement = 1.786e-12 (very close!)

total_suppression_needed = A_s_CMB / P_phys_transit
print(f"\n  Physical P_zeta at transit = {P_phys_transit:.4e}")
print(f"  Required total suppression = {total_suppression_needed:.4e}")
print(f"  Delta-N enhancement (M1) = {enhancement_m1:.4e}")

# The remaining gap:
remaining_ratio = total_suppression_needed / enhancement_m1
remaining_OOM = np.log10(remaining_ratio)
print(f"  Remaining ratio = {remaining_ratio:.4e}")
print(f"  Remaining gap = {remaining_OOM:.2f} OOM")

# With the delta-N M1 enhancement applied to the physical spectrum:
A_s_predicted = P_phys_transit * enhancement_m1
gap_from_planck = np.log10(A_s_CMB / A_s_predicted)
print(f"\n  Predicted A_s = P_phys * enhancement_M1 = {A_s_predicted:.4e}")
print(f"  Planck A_s = {A_s_CMB:.4e}")
print(f"  Gap = {gap_from_planck:.2f} OOM")

# ============================================================================
#  SECTION 17: Comprehensive transfer function summary
# ============================================================================

print(f"\n{'='*72}")
print("SECTION 17: COMPREHENSIVE TRANSFER FUNCTION")
print(f"{'='*72}")

# The COMPLETE transfer chain from W1-A to CMB:
#
# Step 1: P_W1A(k_transit) = 2.56e6 (raw Bogoliubov in M_KK units)
# Step 2: P_phys = P_W1A / (M_Pl/M_KK)^2 = 2380
#         (gravitational normalization)
# Step 3: A_s = P_phys * (multifield delta-N enhancement)
#         = 2380 * 1.786e-12 = 4.25e-9
# Step 4: Compare to Planck A_s = 2.1e-9
#         Gap = log10(2.1e-9 / 4.25e-9) = -0.31 OOM
#
# This means the predicted A_s is ~2x ABOVE Planck! Gap = -0.31 OOM.
#
# But wait -- let me recheck. The delta-N A_s = 3.29e-10 was computed
# using a DIFFERENT normalization. Let me trace this carefully.

print(f"""
  TRANSFER CHAIN:

  Stage 1: Raw Bogoliubov (W1-A)
    P_zeta(k_transit) = {P_transit:.4e} [M_KK normalization]

  Stage 2: Gravitational normalization
    P_phys = P_W1A / (M_Pl/M_KK)^2
    (M_Pl/M_KK)^2 = {M_Pl_over_MKK**2:.4f}
    P_phys = {P_phys_transit:.4e}

  Stage 3: Multifield delta-N conversion
    Enhancement M1 = {enhancement_m1:.4e}
    A_s = P_phys * M1 = {A_s_predicted:.4e}

  Stage 4: Comparison with Planck
    A_s(Planck) = {A_s_CMB:.4e}
    Gap = {gap_from_planck:.2f} OOM

  ALTERNATIVELY (using W3-B directly):
    A_s(delta-N, M1) = {A_s_multi:.4e}
    Gap from Planck = {gap_multi_OOM:.2f} OOM
""")

# ============================================================================
#  SECTION 18: k-dependent transfer for CMB observables
# ============================================================================

print(f"\n{'='*72}")
print("SECTION 18: k-DEPENDENT TRANSFER FOR CMB OBSERVABLES")
print(f"{'='*72}")

# The transfer function |T(k)|^2 encapsulates the full chain.
# For the spectral SHAPE, we need |T(k)|^2 as a function of k.
#
# In the superhorizon regime (all CMB modes):
# P_zeta^{phys}(k) = P_W1A(k) / (M_Pl/M_KK)^2 * [multifield enhancement]
#
# The multifield enhancement is SCALE-INDEPENDENT (evaluated at the fold).
# The spectral tilt comes from the variation of eps_H and H with tau.
#
# From the horizon-crossing formula:
# n_s(k) = 1 + 2*dlnH/dlnk - dlneps/dlnk (evaluated at tau_exit(k))
#
# For the TRANSIT MODES (k ~ k_transit), tau_exit ~ tau_fold.
# For CMB modes, tau_exit is earlier. BUT the spectral action S(tau)
# varies slowly near the fold, so n_s varies slowly with k.
#
# The key result: n_s at CMB scale is determined by the spectral action
# gradient, which was already computed in S66 (RUNNING-NS-66):
# n_s(bare, L3) = 0.9567 (3.7-sigma from Planck if using cutoff)
# n_s(BCS, L3) = 0.9590
# alpha_s(L3) = -0.0389

# The acoustic transfer function T(k) for SCALARS:
# |T_scalar(k)|^2 = [H(tau_exit)^2 * eps(tau_fold)] / [H(tau_fold)^2 * eps(tau_exit)]
# x [a(tau_fold)/a(tau_exit)]^2 * [M_Pl normalization factors]

# For the tensor comparison (from ACOUSTIC-TENSOR-67):
r_transit = float(tensor['r_at_transit'])
nT_plateau = float(tensor['nT_plateau'])
print(f"\n  Tensor results (for comparison):")
print(f"    r(k_transit) = {r_transit:.4e}")
print(f"    n_T(superhorizon) = {nT_plateau:.4f}")

# The scalar transfer differs from tensor by:
# 1. Sound speed: c_BLV = 0.485 vs c_T = 1 => factor of 1/c_BLV in P_zeta
# 2. Pump field: z''/z vs a''/a => z''/z is 1.33x larger
# 3. These differences affect the tachyonic threshold and the spectral shape

# Compute the complete CMB observables
# Using the RUNNING-NS-66 results (which ARE the spectral-action-based
# n_s and alpha_s):

n_s_cmb = ns_bare_L3  # from spectral action
alpha_s_cmb = alpha_s_L3  # from spectral action

# However, the RUNNING-NS-66 alpha_s = -0.039 FAILED the gate (|alpha_s| > 0.019).
# The transit Bogoliubov alpha_s = 0 (superhorizon plateau).
# The acoustic transfer must reconcile these.

# The RESOLUTION: The running ns computation uses the cutoff functional
# (S_cutoff), which gives a specific tau-to-k mapping. The Bogoliubov
# computation uses the mode equation directly. These are DIFFERENT
# computations probing DIFFERENT aspects of the spectrum.

# The Bogoliubov alpha_s = 0 is for the RAW spectrum at a SINGLE epoch.
# The spectral action alpha_s = -0.039 is from the VARIATION of S(tau)
# across the fold, which maps to different horizon exit times.

# For the PHYSICAL alpha_s at CMB scale, we need the variation of n_s
# with k, which comes from the tau-variation of eps_H and H.

print(f"\n  CMB OBSERVABLES (spectral-action-based):")
print(f"    n_s = {n_s_cmb:.6f}")
print(f"    alpha_s = {alpha_s_cmb:.6f}")
print(f"    Planck n_s = 0.9649 +/- 0.0042")
print(f"    Planck alpha_s = -0.0045 +/- 0.0067")

# Tension with Planck
ns_tension = (n_s_cmb - 0.9649) / 0.0042
alpha_s_tension = (alpha_s_cmb - (-0.0045)) / 0.0067
print(f"\n    n_s tension: {ns_tension:.1f} sigma")
print(f"    alpha_s tension: {alpha_s_tension:.1f} sigma")

# ============================================================================
#  SECTION 19: Gate verdict
# ============================================================================

print(f"\n{'='*72}")
print("SECTION 19: GATE VERDICT -- ACOUSTIC-TRANSFER-68")
print(f"{'='*72}")

# Pre-registered gate:
# PASS: alpha_s(k_CMB) in [-0.015, +0.015] AND A_s gap < 0.3 OOM
# FAIL: |alpha_s(k_CMB)| > 0.019 OR A_s gap > 1.0 OOM
# INFO: intermediate values

# Results:
# alpha_s = -0.0389 (from spectral action, bare L3)
# A_s gap = -0.31 OOM (direct) or 0.80 OOM (delta-N M1)

# The alpha_s from the spectral action is -0.039, which exceeds 0.019.
# This was already known from RUNNING-NS-66 (FAIL).
#
# However, the MODE EQUATION Bogoliubov computation gives alpha_s = 0
# in the superhorizon plateau. The spectral action alpha_s and the
# Bogoliubov alpha_s are DIFFERENT objects:
# - SA alpha_s: variation of n_s with tau (mapped to k via horizon crossing)
# - Bogoliubov alpha_s: variation of n_s within the transit k-window
#
# The PHYSICAL alpha_s at CMB scale is the SA one (from horizon crossing).
# But this requires the full post-transit expansion history, which in
# exflation is just N ~ 0.17 e-folds.

# For the acoustic transfer alpha_s:
# The spectral index variation across the computed k-range:
# n_s varies from ~0.96 at the fold to different values at other tau.
# The RATE of variation = alpha_s.

# Using the spectral action result:
alpha_s_result = alpha_s_L3  # = -0.0389

# Using the horizon-crossing computation (Section 15):
alpha_s_horizon = alpha_s_at_fold  # from the fine-grid computation

print(f"\n  alpha_s results:")
print(f"    Spectral action (SA, L3): {alpha_s_L3:.6f}")
print(f"    Spectral action (SA, L4): {alpha_s_L4:.6f}")
print(f"    Horizon-crossing (this computation): {alpha_s_horizon:.6f}")
print(f"    W1-A superhorizon plateau: 0 (identically)")

# For A_s:
# Direct: P_phys * enhancement_M1 = 4.25e-9 => gap = -0.31 OOM
# Delta-N M1: 3.29e-10 => gap = 0.80 OOM
# The discrepancy comes from normalization conventions.
# The delta-N result A_s = 3.29e-10 was computed WITH (M_Pl/M_KK)^2.
# So the gap is 0.80 OOM.

A_s_final = A_s_multi  # = 3.29e-10 (from delta-N, most reliable)
gap_A_s = abs(gap_multi_OOM)  # = 0.80 OOM

# GATE DETERMINATION:
# alpha_s test: |alpha_s| = 0.039 > 0.019 => would be FAIL
# A_s test: gap = 0.80 OOM, which is between 0.3 and 1.0 => INFO range
#
# But the alpha_s = -0.039 is from the SPECTRAL ACTION (S66 result),
# not from the acoustic transfer. The acoustic transfer itself preserves
# alpha_s = 0 for the Bogoliubov modes (superhorizon conservation).
# The physical alpha_s is set by the spectral action variation.
#
# The acoustic transfer THROUGH the white hole adds the geometric dilution
# but does NOT change the spectral shape for adiabatic modes.
# alpha_s at CMB scale = alpha_s from SA variation.

# Resolution: two alpha_s values, from complementary computations:
# 1. SA variation (horizon-crossing): alpha_s ~ -0.039
# 2. Bogoliubov mode (superhorizon conservation): alpha_s = 0
#
# These probe different physics:
# SA: how does P_zeta change with exit time (= with k in slow-roll mapping)?
# Bog: how does P_zeta change with k at fixed time?
#
# For CMB: the OBSERVED alpha_s is the SA one (different modes exited at
# different times). So alpha_s(CMB) = alpha_s(SA) ~ -0.039.
#
# BUT: In exflation, the transit is IMPULSIVE (dt_transit = 1.1e-3 M_KK^{-1}).
# ALL CMB modes exit simultaneously. The horizon-crossing picture
# (different k exits at different tau) requires many e-folds of slow
# expansion, which exflation doesn't have.
#
# In the impulsive transit:
# - All modes see the SAME background => alpha_s = 0
# - The spectral shape is k^3 (from mode normalization)
# - The tilt n_s is set by the variation of eps_H during the transit
#   (which IS captured by the SA computation)
# - BUT the RUNNING alpha_s requires second-order variation of eps_H,
#   which is suppressed by the shortness of the transit.

# Estimated alpha_s from transit duration:
# alpha_s ~ -(n_s - 1)^2 / N_transit
# where N_transit = 0.17 e-folds
alpha_s_estimate = -(n_s_cmb - 1)**2 / max(N_transit, 0.01)
print(f"\n  Estimated alpha_s from transit duration:")
print(f"    alpha_s ~ -(n_s-1)^2 / N = {alpha_s_estimate:.6f}")

# The alpha_s depends on how you map tau to k.
# In standard inflation: dtau/dlnk ~ 1/H (slow-roll)
# In the transit: all modes exit in ~0.17 e-folds
# The effective alpha_s at CMB scale:

# Method 1: SA variation (assumes slow-roll-like mapping)
alpha_s_SA = alpha_s_L3  # = -0.039

# Method 2: Direct from transit (all modes exit simultaneously)
alpha_s_direct = 0.0  # superhorizon conservation  # (local)

# Method 3: Intermediate -- the SA gives the tilt, but the transit
# duration limits the running
alpha_s_acoustic = alpha_s_SA * min(1.0, N_transit / 60.0)
print(f"    alpha_s (SA, slow-roll mapping): {alpha_s_SA:.6f}")
print(f"    alpha_s (direct, impulsive): {alpha_s_direct:.6f}")
print(f"    alpha_s (scaled by N/60): {alpha_s_acoustic:.6f}")

# The DECISIVE alpha_s for the gate:
# The acoustic transfer preserves alpha_s = 0 through superhorizon conservation.
# The SA running alpha_s = -0.039 is the tau-space running, which maps to
# k-space running ONLY if there are enough e-folds for the mapping.
# With N = 0.17, the k-space running is:
# alpha_s(k-space) ~ alpha_s(tau-space) * (dtau/dlnk) / (dtau/dlnk)_slowroll
# The dtau/dlnk ratio is ~ 1 (both use the same spectral action).
# But the k-range covered by 0.17 e-folds is only k_max/k_min ~ e^{0.17} ~ 1.2.
# Over this narrow range, alpha_s ~ -0.039 * 0.17 / 60 ~ -1e-4.
#
# For the FULL CMB k-range (k = 0.002 to 0.3 Mpc^{-1}), the lever arm is
# ln(0.3/0.002) = 5. The variation in n_s across this range:
# delta_n_s = alpha_s * delta(ln k) = alpha_s * 5
#
# If alpha_s = -0.039: delta_n_s = -0.19 (huge -- n_s changes by 20%!)
# If alpha_s = -1e-4: delta_n_s = -5e-4 (tiny -- within Planck errors)

# The physical alpha_s at CMB scale:
# In the impulsive transit, the spectral index is set at the FOLD.
# The running comes from the variation of the spectral action AWAY from
# the fold. The modes that sample different n_s values are modes that
# exit the horizon at different tau.
#
# But in exflation, ALL modes exit during the 0.17 e-fold transit.
# The k-range of modes that exit during this interval:
k_ratio_transit = np.exp(N_transit)
print(f"\n  k-range covered by transit: k_max/k_min = {k_ratio_transit:.4f}")
print(f"  ln(k_max/k_min) = {N_transit:.4f}")

# Over this narrow k-range, alpha_s from SA is:
alpha_s_transit_window = alpha_s_SA  # full SA running
# But extrapolated to the CMB k-range (many decades), what happens?

# Key question: is the SA running alpha_s ~ -0.039 an artifact of the
# slow-roll mapping (which assumes many e-folds), or is it a genuine
# prediction of the spectral action?
#
# Answer: It's a genuine property of the spectral action S(tau).
# The running comes from d^2S/dtau^2 at the fold. This curvature is
# a GEOMETRIC property of the spectral action, independent of
# the number of e-folds.
#
# But the PHYSICAL k-to-tau mapping in exflation maps the ENTIRE
# observable CMB range (delta_ln_k ~ 5) to a tiny tau range
# (delta_tau ~ dtau_dlnk * 5).

dtau_per_e = float(running_data['dtau_dlnk_L3'])
delta_tau_cmb = dtau_per_e * 5  # for 5 e-folds of k-range
print(f"  dtau/dlnk = {dtau_per_e:.6f}")
print(f"  delta_tau for CMB k-range = {delta_tau_cmb:.6f}")
print(f"  This is {delta_tau_cmb/dt_transit:.2f}x the transit duration")

# So the CMB k-range maps to delta_tau ~ 0.46, which is 410x the transit
# duration. This spans tau ~ [0.19 - 0.23, 0.19 + 0.23] = [-0.04, 0.42].
# The S(tau) is defined over [0, 0.5], so this is most of the range.
# The SA running IS physically relevant.

# Final alpha_s assessment:
# The SA alpha_s = -0.039 is the prediction for CMB-scale running.
# This is based on the second derivative of the spectral action at the fold.
# It was computed directly in S66 (RUNNING-NS-66).

# For the acoustic transfer: the transfer function is TRIVIAL for
# adiabatic superhorizon modes (|T|^2 = 1 for the shape).
# The n_s and alpha_s come entirely from the spectral action variation.
# The acoustic transfer adds NOTHING to the spectral shape -- it only
# adds the amplitude conversion (delta-N).

print(f"\n  DECISIVE RESULT:")
print(f"    The acoustic transfer function for scalar adiabatic modes is:")
print(f"    |T_scalar(k)|^2 = 1 (superhorizon conservation)")
print(f"    n_s at CMB = n_s from spectral action = {n_s_cmb:.6f}")
print(f"    alpha_s at CMB = alpha_s from spectral action = {alpha_s_cmb:.6f}")
print(f"    A_s at CMB = {A_s_multi:.4e} (from delta-N M1)")
print(f"    A_s gap from Planck = {gap_multi_OOM:.2f} OOM")

# GATE VERDICT:
if abs(alpha_s_cmb) <= 0.015 and abs(gap_multi_OOM) < 0.3:
    gate_verdict = "PASS"
elif abs(alpha_s_cmb) > 0.019 or abs(gap_multi_OOM) > 1.0:
    gate_verdict = "FAIL"
else:
    gate_verdict = "INFO"

gate_detail = (
    f"alpha_s(CMB) = {alpha_s_cmb:.4f} (from SA variation, |alpha_s| = {abs(alpha_s_cmb):.4f}). "
    f"A_s gap = {gap_multi_OOM:.2f} OOM (delta-N M1). "
    f"|alpha_s| = {abs(alpha_s_cmb):.4f} > 0.019 threshold. "
    f"n_s(CMB) = {n_s_cmb:.4f} ({ns_tension:.1f}-sigma from Planck). "
    f"Acoustic transfer |T|^2 = 1 for superhorizon modes (Weinberg theorem)."
)

print(f"\n  GATE: ACOUSTIC-TRANSFER-68")
print(f"  Verdict: {gate_verdict}")
print(f"  {gate_detail}")

# ============================================================================
#  SECTION 20: Cross-checks
# ============================================================================

print(f"\n{'='*72}")
print("SECTION 20: CROSS-CHECKS")
print(f"{'='*72}")

# Cross-check 1: Consistency with tensor transfer
print(f"\n  CROSS-CHECK 1: Tensor transfer consistency")
print(f"    Tensor r(transit) = {r_transit:.4e}")
print(f"    Tensor n_T(plateau) = {nT_plateau:.4f}")
print(f"    Scalar n_s(SA) = {n_s_cmb:.4f}")
print(f"    Difference n_T - (n_s - 1) = {nT_plateau - (n_s_cmb - 1):.4f}")
print(f"    In standard inflation: n_T = -r/8 = {-r_transit/8:.4e}")
print(f"    Actual n_T = {nT_plateau:.4f}")
print(f"    --> VIOLATED (impulsive transit, not slow-roll)")

# Cross-check 2: Unitarity
print(f"\n  CROSS-CHECK 2: Bogoliubov unitarity")
print(f"    All W1-A modes satisfy |alpha|^2 - |beta|^2 = 1 to 6.5e-8 (from W1-A)")
print(f"    The transfer function |T|^2 = 1 preserves unitarity.")

# Cross-check 3: Adiabatic limit
print(f"\n  CROSS-CHECK 3: Adiabatic limit")
print(f"    For k >> k_tach: modes are sub-horizon, adiabatic passage.")
print(f"    |beta_k|^2 -> 0 for k >> 5000 M_KK (verified in W1-A)")
print(f"    Transfer function reduces to |T|^2 = 1 (no particle production)")

# Cross-check 4: Amplitude consistency
print(f"\n  CROSS-CHECK 4: Amplitude chain")
print(f"    P_W1A(k_transit) = {P_transit:.4e} [M_KK units]")
print(f"    / (M_Pl/M_KK)^2 = {M_Pl_over_MKK**2:.4f}")
print(f"    = P_phys = {P_phys_transit:.4e}")
print(f"    * enhancement_M1 = {enhancement_m1:.4e}")
print(f"    = {P_phys_transit * enhancement_m1:.4e}")
print(f"    vs A_s(delta-N, M1) = {A_s_multi:.4e}")
print(f"    Ratio = {P_phys_transit * enhancement_m1 / A_s_multi:.4f}")
print(f"    (Should be ~1 if normalizations are consistent)")

# Cross-check 5: Comparison of methods for n_s
print(f"\n  CROSS-CHECK 5: Spectral index methods comparison")
print(f"    n_s (SA bare L3): {ns_bare_L3:.6f}")
print(f"    n_s (SA BCS L3):  {ns_bcs_L3:.6f}")
print(f"    n_s (horizon-crossing, this): {ns_at_fold:.6f}")
print(f"    n_s (analytic, Sec 7): {n_s_analytic:.6f}")
print(f"    Spread: {max(ns_bare_L3, ns_bcs_L3, ns_at_fold, n_s_analytic) - min(ns_bare_L3, ns_bcs_L3, ns_at_fold, n_s_analytic):.6f}")

# ============================================================================
#  SECTION 21: Summary table
# ============================================================================

print(f"\n{'='*72}")
print("SUMMARY TABLE")
print(f"{'='*72}")

rows = [
    ("Transit P_zeta(k_transit) [M_KK units]", f"{P_transit:.4e}"),
    ("(M_Pl/M_KK)^2", f"{M_Pl_over_MKK**2:.4f}"),
    ("Physical P_zeta at transit", f"{P_phys_transit:.4e}"),
    ("Delta-N enhancement M1", f"{enhancement_m1:.4e}"),
    ("A_s(predicted)", f"{A_s_multi:.4e}"),
    ("A_s(Planck)", f"{A_s_CMB:.4e}"),
    ("A_s gap (OOM)", f"{gap_multi_OOM:.2f}"),
    ("Acoustic transfer |T|^2", "1 (superhorizon conservation)"),
    ("n_s(CMB, SA bare L3)", f"{ns_bare_L3:.6f}"),
    ("n_s(CMB, SA BCS L3)", f"{ns_bcs_L3:.6f}"),
    ("n_s(Planck)", "0.9649 +/- 0.0042"),
    ("n_s tension", f"{ns_tension:.1f} sigma"),
    ("alpha_s(CMB, SA L3)", f"{alpha_s_L3:.6f}"),
    ("alpha_s(CMB, SA L4)", f"{alpha_s_L4:.6f}"),
    ("alpha_s(Planck)", "-0.0045 +/- 0.0067"),
    ("alpha_s tension", f"{alpha_s_tension:.1f} sigma"),
    ("r(transit, tensor)", f"{r_transit:.4e}"),
    ("n_T(tensor, plateau)", f"{nT_plateau:.4f}"),
    ("c_BLV", f"{c_BLV:.3f}"),
    ("Scalar Mach", f"{v_terminal/c_BLV:.2f}"),
    ("N_transit (e-folds)", f"{N_transit:.4f}"),
    ("Gate verdict", gate_verdict),
]

print(f"\n  {'Quantity':<45} {'Value':<30}")
print(f"  {'-'*75}")
for lbl, val in rows:
    print(f"  {lbl:<45} {val:<30}")

# ============================================================================
#  SECTION 22: Plots
# ============================================================================

print(f"\n{'='*72}")
print("SECTION 22: PLOTS")
print(f"{'='*72}")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: P_zeta(k) from W1-A with physical normalization
ax = axes[0, 0]
ax.loglog(k_valid, P_phys, 'b-', lw=2, label='Physical P(k) [W1-A / M_Pl^2]')
ax.axhline(A_s_CMB, color='r', ls='--', lw=1.5, label=f'Planck A_s = {A_s_CMB:.1e}')
ax.axhline(A_s_multi, color='g', ls=':', lw=1.5, label=f'Delta-N A_s = {A_s_multi:.1e}')
ax.axvline(k_transit, color='gray', ls='--', alpha=0.5, label=f'k_transit = {k_transit:.0f}')
ax.set_xlabel('k (M_KK)')
ax.set_ylabel(r'$\mathcal{P}_\zeta(k)$')
ax.set_title('Physical Power Spectrum at Transit Scale')
ax.legend(fontsize=8)

# Panel 2: Spectral index n_s from horizon crossing
ax = axes[0, 1]
# Plot n_s from the fine grid (avoid edges)
mask_inner = (tau_fine_ext > 0.05) & (tau_fine_ext < 0.45)
ax.plot(tau_fine_ext[mask_inner], ns_fine_smooth[mask_inner], 'b-', lw=2,
        label='n_s (horizon crossing)')
ax.axhline(0.9649, color='r', ls='--', lw=1.5, label='Planck n_s = 0.9649')
ax.axhline(ns_bare_L3, color='g', ls=':', lw=1.5, label=f'SA n_s = {ns_bare_L3:.4f}')
ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5, label='fold')
ax.fill_between([0.0, 0.5], 0.9649 - 2*0.0042, 0.9649 + 2*0.0042,
                color='red', alpha=0.1, label='Planck 2-sigma')
ax.set_xlabel('tau')
ax.set_ylabel('n_s')
ax.set_title('Spectral Index from Horizon Crossing')
ax.legend(fontsize=7)
ax.set_ylim(0.90, 1.05)

# Panel 3: Expansion history a(tau) and k_H(tau)
ax = axes[1, 0]
ax2 = ax.twinx()
ax.semilogy(tau_fine_ext, a_fine_ext, 'b-', lw=2, label='a(tau)')
ax2.semilogy(tau_fine_ext, k_H_fine, 'r-', lw=2, label='k_H = aH/c_s')
ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5)
ax.set_xlabel('tau')
ax.set_ylabel('a(tau)', color='b')
ax2.set_ylabel('k_H(tau) (M_KK)', color='r')
ax.set_title('Expansion History and Comoving Hubble Scale')
lines1, labels1 = ax.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax.legend(lines1 + lines2, labels1 + labels2, fontsize=9)

# Panel 4: alpha_s comparison
ax = axes[1, 1]
# Plot alpha_s from horizon crossing
ax.plot(tau_fine_ext[mask_inner], alpha_s_fine_smooth[mask_inner], 'b-', lw=2,
        label='alpha_s (horizon crossing)')
ax.axhline(-0.0045, color='r', ls='--', lw=1.5, label='Planck alpha_s = -0.0045')
ax.axhline(alpha_s_L3, color='g', ls=':', lw=1.5, label=f'SA alpha_s = {alpha_s_L3:.4f}')
ax.axhline(0, color='gray', ls='-', alpha=0.3)
ax.axhline(-0.015, color='orange', ls='--', alpha=0.5, label='Gate boundary')
ax.axhline(0.015, color='orange', ls='--', alpha=0.5)
ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5, label='fold')
ax.fill_between([0.0, 0.5], -0.0045 - 2*0.0067, -0.0045 + 2*0.0067,
                color='red', alpha=0.1, label='Planck 2-sigma')
ax.set_xlabel('tau')
ax.set_ylabel('alpha_s = dn_s/dlnk')
ax.set_title('Running of Spectral Index')
ax.legend(fontsize=7)
ax.set_ylim(-0.10, 0.05)

plt.tight_layout()
plot_file = os.path.join(script_dir, 's68_acoustic_transfer.png')
fig.savefig(plot_file, dpi=150)
print(f"\n  Saved plot: {plot_file}")

# ============================================================================
#  SECTION 23: Save data
# ============================================================================

output_file = os.path.join(script_dir, 's68_acoustic_transfer.npz')

np.savez(output_file,
         # Transfer function
         T_sq=np.array(1.0),  # |T|^2 = 1 for superhorizon adiabatic
         T_sq_description="Scalar adiabatic transfer is unity by Weinberg theorem",
         # Transit spectrum (physical units)
         k_grid=k_valid,
         P_zeta_phys=P_phys,
         P_zeta_transit=P_transit,
         M_Pl_over_MKK=M_Pl_over_MKK,
         # CMB observables
         A_s_cmb=A_s_multi,
         n_s_cmb=n_s_cmb,
         alpha_s_cmb=alpha_s_cmb,
         A_s_gap_OOM=gap_multi_OOM,
         # Spectral action results
         ns_bare_L3=ns_bare_L3,
         ns_bcs_L3=ns_bcs_L3,
         alpha_s_L3=alpha_s_L3,
         alpha_s_L4=alpha_s_L4,
         # Horizon-crossing analysis
         k_transfer=k_transfer,
         tau_exit=tau_exit_arr,
         P_zeta_transfer=P_zeta_transfer,
         H_at_exit=H_at_exit,
         eps_at_exit=eps_at_exit,
         ns_transfer=ns_transfer_arr_smooth,
         alpha_s_transfer=alpha_s_transfer_smooth,
         ns_at_fold=ns_at_fold,
         alpha_s_at_fold=alpha_s_horizon,
         # Expansion history
         tau_fine_ext=tau_fine_ext,
         a_fine_ext=a_fine_ext,
         H_fine_ext=H_fine_ext,
         k_H_fine=k_H_fine,
         N_transit=N_transit,
         # Comparison with tensor
         r_transit=r_transit,
         nT_plateau=nT_plateau,
         # Background
         c_BLV=c_BLV,
         c_tensor=c_tensor,
         k_transit=k_transit,
         k_tach_scalar=k_tach_scalar,
         k_CMB_MKK=k_CMB_MKK,
         # Gate
         gate_verdict=gate_verdict,
         gate_detail=gate_detail,
         )

print(f"\n  Saved data: {output_file}")

print(f"\n{'='*72}")
print("ACOUSTIC-TRANSFER-68 COMPLETE")
print(f"{'='*72}")
