#!/usr/bin/env python3
"""
IMPEDANCE-55: Impedance Mismatch at Cutoff Edge
=================================================

Computes acoustic impedance Z(tau) at sharp cutoff Lambda=1.0.
Tests whether the S_occ barrier height is impedance-controlled or DOS-controlled.

Physics:
  In acoustic/phononic systems, a sharp boundary between a propagating medium
  (Z != 0) and vacuum (Z = 0) gives total reflection R = 1. A graded impedance
  profile (Fermi-Dirac cutoff with finite steepness alpha) creates partial
  transmission T(alpha) = 1 - R(alpha).

  The Fermi-Dirac family of cutoff functions:
      f_alpha(x) = 1 / (exp(alpha*(x - 1)) + 1)
  interpolates between:
      alpha -> 0:   f -> 1/2  (flat, no cutoff)
      alpha -> inf: f -> Theta(1 - x)  (sharp cutoff)

  Acoustic impedance Z = rho * c_s where:
      rho = DOS (density of states near cutoff)
      c_s = group velocity = d(omega)/dk ~ d(eigenvalue)/d(index) near cutoff

  At the cutoff edge, the reflection coefficient is:
      R = |Z_below - Z_above|^2 / |Z_below + Z_above|^2

  For sharp cutoff: Z_above = 0, so R = 1 (total reflection).
  For Fermi-Dirac: the cutoff function acts as an impedance-matching layer,
  reducing R and transmitting spectral weight across the boundary.

  If barriers are IMPEDANCE-CONTROLLED: barrier height ~ R(alpha)
  If barriers are DOS-CONTROLLED: barrier height ~ N_modes(Lambda, tau)

Gate: IMPEDANCE-55 (INFO): impedance-controlled vs DOS-controlled classification.

Author: Tesla-Resonance (S55 W3-4)
"""

import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import numpy as np
from scipy.optimize import brentq
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

from canonical_constants import (
    tau_fold, Delta_0_GL, Delta_0_OES, E_cond, E_B1, E_B2_mean, E_B3_mean
)

# =============================================================================
# 0. Load data
# =============================================================================
data_dir = os.path.dirname(os.path.abspath(__file__))
sa_data = np.load(os.path.join(data_dir, 's54_sa_latt_occ.npz'), allow_pickle=True)
tb_data = np.load(os.path.join(data_dir, 's54_tb_hamiltonian.npz'), allow_pickle=True)

tau_values = sa_data['tau_values']         # (50,)
eigenvalues = tb_data['eigenvalues']       # (50, 32)
bandwidths = tb_data['bandwidths']         # (50,)
S_occ = sa_data['S_occ']                  # (3, 3, 50) [cutoff, Lambda, tau]
S_vac = sa_data['S_vac']                  # (3, 3, 50)
occupations = sa_data['occupations']       # (50, 32) BCS(OES) primary
Lambda_values = sa_data['Lambda_values']   # [1.0, 2.0, 5.0]
cutoff_names = sa_data['cutoff_names']     # ['Exponential', 'Sharp', 'Polynomial']
has_minimum = sa_data['has_minimum']       # (3, 3) bool
barrier_heights = sa_data['barrier_heights']  # (3, 3)

N_tau = len(tau_values)
N_cells = eigenvalues.shape[1]  # 32
dtau = tau_values[1] - tau_values[0]

print(f"Loaded: {N_tau} tau values, {N_cells} cells")
print(f"tau range: [{tau_values[0]:.3f}, {tau_values[-1]:.3f}], dtau = {dtau:.6f}")
print(f"Lambda values: {Lambda_values}")
print(f"Cutoff names: {cutoff_names}")

# =============================================================================
# 1. BCS occupation (re-derive for Fermi-Dirac family)
# =============================================================================
Delta_primary = Delta_0_OES  # 0.464 M_KK

def bcs_occupation(energies, delta, n_target=2.0):
    """BCS occupation n_k = v_k^2 with mu adjusted for particle number."""
    e_min, e_max = energies.min(), energies.max()
    def occupation_sum(mu):
        eps = energies - mu
        Ek = np.sqrt(eps**2 + delta**2)
        vk2 = 0.5 * (1.0 - eps / Ek)
        return np.sum(vk2) - n_target
    mu_lo = e_min - 10.0 * abs(delta) - 10.0 * (e_max - e_min)
    mu_hi = e_max + 10.0 * abs(delta) + 10.0 * (e_max - e_min)
    mu = brentq(occupation_sum, mu_lo, mu_hi, xtol=1e-14, maxiter=200)
    eps = energies - mu
    Ek = np.sqrt(eps**2 + delta**2)
    n_k = 0.5 * (1.0 - eps / Ek)
    return n_k, mu

# =============================================================================
# 2. Fermi-Dirac cutoff family
# =============================================================================
def f_fermi_dirac(x, alpha):
    """
    Fermi-Dirac cutoff: f_alpha(x) = 1 / (exp(alpha*(x - 1)) + 1).

    Limits:
      alpha -> inf: f -> Theta(1 - x)  (sharp cutoff)
      alpha -> 0:   f -> 1/2           (no cutoff)
      alpha = 1:    smooth transition width ~ 4/alpha around x=1  # (local)
    """
    arg = alpha * (x - 1.0)
    # Numerically stable
    return np.where(arg > 500, 0.0, np.where(arg < -500, 1.0, 1.0 / (np.exp(arg) + 1.0)))

# Reference cutoffs from S54
def f_exp(x):
    return np.exp(-x)

def f_sharp(x):
    return np.where(x <= 1.0, 1.0, 0.0)

def f_poly(x):
    return np.where(x <= 1.0, (1.0 - x)**2, 0.0)

# =============================================================================
# 3. Compute acoustic impedance Z(tau) at cutoff edge
# =============================================================================
# For each tau, define:
#   rho(tau) = local DOS near Lambda = 1.0
#   c_s(tau) = local group velocity near Lambda = 1.0
#   Z(tau) = rho * c_s
#
# The eigenvalues are ordered: lam_0 < lam_1 < ... < lam_{31}.
# Near the cutoff lam = Lambda, the DOS is approximately the number of modes
# per unit energy, and c_s is the spacing between consecutive eigenvalues.

Lambda_test = 1.0  # Primary cutoff scale (local)

# For each tau, find the modes near Lambda and compute local DOS and velocity
Z_below = np.zeros(N_tau)
dos_below = np.zeros(N_tau)
c_s_below = np.zeros(N_tau)
n_below = np.zeros(N_tau, dtype=int)  # number of modes below cutoff
edge_gap = np.zeros(N_tau)  # gap between last mode below and first mode above cutoff

for it in range(N_tau):
    lam = eigenvalues[it]  # sorted eigenvalues
    x = lam**2 / Lambda_test**2
    mask_below = x <= 1.0  # modes with lam^2/Lambda^2 <= 1
    n_b = mask_below.sum()
    n_below[it] = n_b

    if n_b == 0 or n_b >= N_cells:
        # Degenerate: all modes above or below cutoff
        Z_below[it] = 0.0
        dos_below[it] = 0.0
        c_s_below[it] = 0.0
        edge_gap[it] = 0.0
        continue

    # Modes below and above cutoff
    lam_below = lam[mask_below]
    lam_above = lam[~mask_below]

    # Local DOS: number of modes per unit energy near Lambda
    # Use the modes closest to the cutoff edge
    if n_b >= 2:
        # Spacing near the edge
        spacing_below = lam_below[-1] - lam_below[-2]  # spacing of last two below
        dos_below[it] = 1.0 / max(spacing_below, 1e-12)
    else:
        # Only one mode below -- use mode-to-cutoff distance
        dos_below[it] = 1.0 / max(Lambda_test - lam_below[0], 1e-12)

    # Group velocity: d(omega)/dk approximated as spacing / (1 mode)
    # In a lattice, c_s ~ Delta_lam * N / L ~ spacing between modes
    if n_b >= 2:
        c_s_below[it] = lam_below[-1] - lam_below[-2]  # eigenvalue spacing near edge
    else:
        c_s_below[it] = lam_below[0]  # the single mode energy

    # Impedance = rho * c_s
    # In acoustic analogy: Z = sqrt(K * rho_mass) or Z = rho_DOS * c_group
    # Here: Z = dos * c_s = 1 (dimensional analysis check)
    # More physically: Z measures the spectral weight density at the edge
    # Z_below = n_modes_near_edge * weight_per_mode
    Z_below[it] = dos_below[it] * c_s_below[it]

    # Gap between last mode below and first mode above
    edge_gap[it] = lam_above[0] - lam_below[-1]

print(f"\n{'='*70}")
print(f"Section 3: Acoustic impedance at Lambda = {Lambda_test}")
print(f"{'='*70}")
print(f"{'tau':>6} {'n_below':>8} {'DOS':>12} {'c_s':>12} {'Z':>12} {'edge_gap':>12}")
for it in [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 49]:
    print(f"{tau_values[it]:6.3f} {n_below[it]:8d} {dos_below[it]:12.4f} "
          f"{c_s_below[it]:12.6f} {Z_below[it]:12.4f} {edge_gap[it]:12.6f}")

# =============================================================================
# 4. Reflection coefficient for Fermi-Dirac family
# =============================================================================
# The key insight: for a cutoff function f(x), the "effective impedance" at the
# edge is not just Z_below vs 0 -- the cutoff function itself acts as an
# impedance-matching taper.
#
# For the Fermi-Dirac cutoff f_alpha(x) = 1/(exp(alpha*(x-1)) + 1):
# - The cutoff has width ~ 4/alpha centered at x=1
# - Modes within this transition region contribute with partial weight
# - The effective reflection depends on how many modes fall in the transition
#
# Transmission through a graded impedance profile:
#   T(alpha) = 1 - R(alpha)
# where R depends on the number of modes within the transition region [1 - 2/alpha, 1 + 2/alpha]
#
# For an acoustic quarter-wave matching layer: T = 4*Z1*Z2/(Z1+Z2)^2
# Here Z1 = Z_below, Z2 = 0 for sharp cutoff.
# With Fermi-Dirac: Z2 != 0 because modes above cutoff have finite (exponentially small) weight.

alpha_values = np.array([0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 50.0, 100.0, 500.0, 1000.0])
N_alpha = len(alpha_values)

# Compute S_occ for Fermi-Dirac family at Lambda=1.0
S_occ_fd = np.zeros((N_alpha, N_tau))
S_vac_fd = np.zeros((N_alpha, N_tau))

for ia, alpha in enumerate(alpha_values):
    for it in range(N_tau):
        lam = eigenvalues[it]
        x = lam**2 / Lambda_test**2
        f_vals = f_fermi_dirac(x, alpha)
        S_occ_fd[ia, it] = np.sum(occupations[it] * f_vals)
        S_vac_fd[ia, it] = np.sum(f_vals)

print(f"\n{'='*70}")
print(f"Section 4: Fermi-Dirac cutoff family at Lambda = {Lambda_test}")
print(f"{'='*70}")

# For each alpha, find minima in [0.10, 0.30]
tau_lo_idx = np.argmin(np.abs(tau_values - 0.10))
tau_hi_idx = np.argmin(np.abs(tau_values - 0.30))

fd_has_min = np.zeros(N_alpha, dtype=bool)
fd_min_tau = np.full(N_alpha, np.nan)
fd_min_val = np.full(N_alpha, np.nan)
fd_barrier = np.full(N_alpha, np.nan)
fd_barrier_abs = np.full(N_alpha, np.nan)

for ia in range(N_alpha):
    S = S_occ_fd[ia]
    S_search = S[tau_lo_idx:tau_hi_idx+1]
    tau_search = tau_values[tau_lo_idx:tau_hi_idx+1]

    # Search for local minima
    for j in range(1, len(S_search) - 1):
        if S_search[j] < S_search[j-1] and S_search[j] < S_search[j+1]:
            S_min = S_search[j]
            tau_min = tau_search[j]
            S_left_max = S_search[:j].max()
            S_right_max = S_search[j+1:].max()
            barrier = min(S_left_max - S_min, S_right_max - S_min)
            barrier_rel = barrier / abs(S_min) if abs(S_min) > 1e-15 else barrier

            if not fd_has_min[ia] or barrier > fd_barrier_abs[ia]:
                fd_has_min[ia] = True
                fd_min_tau[ia] = tau_min
                fd_min_val[ia] = S_min
                fd_barrier[ia] = barrier_rel
                fd_barrier_abs[ia] = barrier

print(f"\n{'alpha':>8} {'has_min':>8} {'tau_min':>8} {'S_min':>12} {'barrier_rel':>12} {'barrier_abs':>12}")
print("-" * 68)
for ia in range(N_alpha):
    if fd_has_min[ia]:
        print(f"{alpha_values[ia]:8.1f} {'YES':>8} {fd_min_tau[ia]:8.4f} "
              f"{fd_min_val[ia]:12.6f} {fd_barrier[ia]:12.6f} {fd_barrier_abs[ia]:12.6f}")
    else:
        print(f"{alpha_values[ia]:8.1f} {'NO':>8} {'---':>8} {'---':>12} {'---':>12} {'---':>12}")

# =============================================================================
# 5. Effective impedance via cutoff-weighted spectral moments
# =============================================================================
# Instead of the naive Z = rho * c_s, define the effective impedance through
# the cutoff function directly.
#
# The cutoff f(x) defines a "transmission window". The spectral action is:
#   S_occ(tau) = sum_k n_k(tau) * f(lam_k^2 / Lambda^2)
#
# The impedance mismatch at the edge is captured by the spectral weight
# in the transition region of the cutoff. Define:
#
#   W_edge(tau, alpha) = sum_k n_k * |df/dx|_{x=lam_k^2/Lambda^2}
#
# This measures how much spectral weight sits in the "impedance matching" zone.
# Large W_edge => many modes in transition => good matching => small R
# Small W_edge => few modes in transition => poor matching => large R
#
# The derivative of the Fermi-Dirac cutoff:
#   df/dx = -alpha * exp(alpha*(x-1)) / (exp(alpha*(x-1)) + 1)^2
#           = -alpha * f(x) * (1 - f(x))

W_edge_occ = np.zeros((N_alpha, N_tau))
W_edge_vac = np.zeros((N_alpha, N_tau))

for ia, alpha in enumerate(alpha_values):
    for it in range(N_tau):
        lam = eigenvalues[it]
        x = lam**2 / Lambda_test**2
        f_vals = f_fermi_dirac(x, alpha)
        # |df/dx| = alpha * f * (1-f)
        df_abs = alpha * f_vals * (1.0 - f_vals)
        W_edge_occ[ia, it] = np.sum(occupations[it] * df_abs)
        W_edge_vac[ia, it] = np.sum(df_abs)

# Effective reflection: R_eff(alpha, tau) = 1 when W_edge -> 0 (sharp, no modes in transition)
# R_eff -> 0 when many modes densely fill the transition region.
# Model: R_eff = exp(-W_edge / W_scale) where W_scale is a characteristic scale.
# Or from transfer matrix theory: R = tanh^2(pi * delta_n / (2 * n_transition))
# where delta_n = refractive index contrast, n_transition = modes in transition.

# Simpler: define the effective transmission through the occupied spectral measure:
#   T_eff(alpha, tau) = 1 - [S_occ(alpha->inf) - S_occ(alpha)] / S_occ(alpha)
# This measures how much the barrier CHANGES as we soften the cutoff.

# Use the sharpest Fermi-Dirac (alpha=1000) as proxy for sharp cutoff
S_sharp_fd = S_occ_fd[-1]  # alpha=1000 ~ sharp

# Effective transmission relative to sharp cutoff
T_eff = np.zeros((N_alpha, N_tau))
for ia in range(N_alpha):
    for it in range(N_tau):
        if abs(S_sharp_fd[it]) > 1e-15:
            T_eff[ia, it] = 1.0 - abs(S_occ_fd[ia, it] - S_sharp_fd[it]) / abs(S_sharp_fd[it])
        else:
            T_eff[ia, it] = 0.0

print(f"\n{'='*70}")
print(f"Section 5: Edge spectral weight W_edge")
print(f"{'='*70}")
print(f"{'alpha':>8} {'W_edge_mean':>12} {'W_edge_fold':>12} {'T_eff_fold':>12}")
fold_idx = np.argmin(np.abs(tau_values - tau_fold))
for ia in range(N_alpha):
    print(f"{alpha_values[ia]:8.1f} {W_edge_occ[ia].mean():12.6f} "
          f"{W_edge_occ[ia, fold_idx]:12.6f} {T_eff[ia, fold_idx]:12.6f}")

# =============================================================================
# 6. Test: Impedance-controlled vs DOS-controlled barrier scaling
# =============================================================================
# Hypothesis A (impedance-controlled): barrier height ~ R_eff(alpha)
#   barrier_abs(alpha) propto (1 - T_eff(alpha))
# Hypothesis B (DOS-controlled): barrier height ~ n_modes_below(Lambda, tau_min)
#   barrier_abs(alpha) ~ constant for alpha > alpha_critical
#   (once the cutoff is sharp enough to count modes, further sharpening doesn't help)
#
# Discriminant: plot barrier_abs vs alpha and fit to:
#   Model A: barrier = A * (1 - exp(-alpha/alpha_0))  [impedance saturation]
#   Model B: barrier = B * (1 - exp(-alpha/alpha_1)) + C * alpha  [linear growth from DOS]
#
# If barrier saturates => DOS-controlled (counting modes dominates)
# If barrier grows with alpha => impedance-controlled (R increases with sharpness)

print(f"\n{'='*70}")
print(f"Section 6: Barrier scaling test")
print(f"{'='*70}")

# Compute S_occ derivative (barrier proxy) at the minimum location
# For each alpha, measure the barrier near the fold
# Use the full search approach from Section 4

# Also compute: at the tau where Sharp has its minimum,
# how does S_occ(alpha) behave?
# Sharp minimum is at tau ~ 0.194 for Lambda=1.0
sharp_min_idx = np.argmin(np.abs(tau_values - 0.194))

print(f"\nS_occ(tau={tau_values[sharp_min_idx]:.3f}) vs alpha:")
print(f"{'alpha':>8} {'S_occ':>12} {'S_occ/S_sharp':>14} {'n_modes_trans':>14}")
for ia in range(N_alpha):
    alpha = alpha_values[ia]
    # Count modes in transition region [1 - 2/alpha, 1 + 2/alpha] (in x-space)
    x_lo = max(0, 1.0 - 2.0/max(alpha, 0.01))
    x_hi = 1.0 + 2.0/max(alpha, 0.01)
    lam = eigenvalues[sharp_min_idx]
    x = lam**2 / Lambda_test**2
    n_trans = np.sum((x >= x_lo) & (x <= x_hi))

    ratio = S_occ_fd[ia, sharp_min_idx] / S_occ_fd[-1, sharp_min_idx] if abs(S_occ_fd[-1, sharp_min_idx]) > 1e-15 else 0.0
    print(f"{alpha:8.1f} {S_occ_fd[ia, sharp_min_idx]:12.6f} {ratio:14.6f} {n_trans:14d}")

# =============================================================================
# 7. Quantitative comparison: barrier height vs alpha
# =============================================================================
# More refined: compute barrier height as function of alpha
# by finding min and surrounding max in the search window

print(f"\n{'='*70}")
print(f"Section 7: Barrier height vs alpha (quantitative)")
print(f"{'='*70}")

# Also compute for the S54 cutoff functions at Lambda=1.0
# S_occ[0,0,:] = Exponential, Lambda=1.0
# S_occ[1,0,:] = Sharp, Lambda=1.0
# S_occ[2,0,:] = Polynomial, Lambda=1.0

S_ref = {
    'Exponential': S_occ[0, 0, :],
    'Sharp': S_occ[1, 0, :],
    'Polynomial': S_occ[2, 0, :],
}

# Compute derivative of S_occ_fd with respect to tau at each alpha
dS_fd = np.zeros((N_alpha, N_tau))
for ia in range(N_alpha):
    dS_fd[ia] = np.gradient(S_occ_fd[ia], dtau)

# Compute the "curvature" at the minimum -- second derivative
d2S_fd = np.zeros((N_alpha, N_tau))
for ia in range(N_alpha):
    d2S_fd[ia] = np.gradient(dS_fd[ia], dtau)

# For the test: compute the barrier as max(dS) in the search region
# The barrier is the integral of |dS/dtau| from the max before minimum to the minimum
# More directly: barrier = S(tau_max_left) - S(tau_min)

barrier_vs_alpha = np.full(N_alpha, np.nan)
curvature_vs_alpha = np.full(N_alpha, np.nan)
min_tau_vs_alpha = np.full(N_alpha, np.nan)

for ia in range(N_alpha):
    S = S_occ_fd[ia]
    S_search = S[tau_lo_idx:tau_hi_idx+1]
    tau_search = tau_values[tau_lo_idx:tau_hi_idx+1]

    # Find all local minima
    best_barrier = -1.0  # (local)
    for j in range(1, len(S_search) - 1):
        if S_search[j] < S_search[j-1] and S_search[j] < S_search[j+1]:
            S_min = S_search[j]
            S_left_max = S_search[:j].max()
            S_right_max = S_search[j+1:].max()
            barrier = min(S_left_max - S_min, S_right_max - S_min)
            if barrier > best_barrier:
                best_barrier = barrier
                barrier_vs_alpha[ia] = barrier
                min_tau_vs_alpha[ia] = tau_search[j]
                # Curvature at minimum (in global indices)
                global_j = tau_lo_idx + j
                curvature_vs_alpha[ia] = d2S_fd[ia, global_j]

print(f"\n{'alpha':>8} {'barrier':>12} {'curvature':>12} {'tau_min':>10}")
print("-" * 50)
for ia in range(N_alpha):
    if not np.isnan(barrier_vs_alpha[ia]):
        print(f"{alpha_values[ia]:8.1f} {barrier_vs_alpha[ia]:12.6f} "
              f"{curvature_vs_alpha[ia]:12.6f} {min_tau_vs_alpha[ia]:10.4f}")
    else:
        print(f"{alpha_values[ia]:8.1f} {'no min':>12} {'---':>12} {'---':>10}")

# =============================================================================
# 8. The decisive comparison: scaling law
# =============================================================================
# If impedance-controlled: barrier ~ 1 - exp(-alpha/alpha_0)  (saturates)
# If DOS-controlled: barrier ~ n_below(tau_min) which is alpha-independent past threshold
#
# The barrier for the SHARP cutoff from S54 is 0.05348 (at Lambda=1.0)
# Let's see how the Fermi-Dirac barrier approaches this value

print(f"\n{'='*70}")
print(f"Section 8: Scaling law analysis")
print(f"{'='*70}")

# S54 sharp barrier at Lambda=1.0
barrier_sharp_s54 = barrier_heights[1, 0]  # Sharp cutoff, Lambda=1.0
print(f"S54 Sharp barrier (Lambda=1.0): {barrier_sharp_s54:.6f}")

# Compute relative approach to sharp limit
valid_mask = ~np.isnan(barrier_vs_alpha)
alpha_valid = alpha_values[valid_mask]
barrier_valid = barrier_vs_alpha[valid_mask]

if len(barrier_valid) > 0:
    barrier_inf = barrier_valid[-1]  # highest alpha approximates sharp
    print(f"FD barrier at alpha={alpha_valid[-1]:.0f}: {barrier_inf:.6f}")

    # Fractional approach to saturation
    print(f"\nFractional approach to saturation:")
    print(f"{'alpha':>8} {'barrier':>12} {'frac_of_max':>14} {'delta':>12}")
    for i in range(len(barrier_valid)):
        frac = barrier_valid[i] / barrier_inf if barrier_inf > 1e-15 else 0.0
        delta = barrier_inf - barrier_valid[i]
        print(f"{alpha_valid[i]:8.1f} {barrier_valid[i]:12.6f} {frac:14.6f} {delta:12.6f}")

# =============================================================================
# 9. DOS analysis: mode counting at the cutoff edge
# =============================================================================
print(f"\n{'='*70}")
print(f"Section 9: DOS at cutoff edge (mode counting)")
print(f"{'='*70}")

# For each tau, count modes with lam^2/Lambda^2 <= 1 and compute occupied weight
n_modes_below = np.zeros(N_tau, dtype=int)
occ_weight_below = np.zeros(N_tau)
occ_weight_above = np.zeros(N_tau)
n_occ_effective = np.zeros(N_tau)  # sum of n_k for modes below cutoff

for it in range(N_tau):
    lam = eigenvalues[it]
    x = lam**2 / Lambda_test**2
    mask = x <= 1.0
    n_modes_below[it] = mask.sum()
    occ_weight_below[it] = np.sum(occupations[it][mask])
    occ_weight_above[it] = np.sum(occupations[it][~mask])
    n_occ_effective[it] = np.sum(occupations[it] * mask.astype(float))

# The key question: does the barrier in S_occ come from
# (A) mode crossings through the cutoff edge (DOS mechanism), or
# (B) impedance mismatch at the edge (reflection mechanism)?
#
# If (A): the barrier appears when a mode crosses Lambda, and the barrier height
# is proportional to the occupation weight of that mode.
# If (B): the barrier comes from the discontinuous reflection at the cutoff edge,
# and its height scales with the impedance contrast.

# Find where mode count changes (a mode crosses the cutoff)
mode_crossing_taus = []
mode_crossing_occ = []
for it in range(1, N_tau):
    if n_modes_below[it] != n_modes_below[it-1]:
        mode_crossing_taus.append(tau_values[it])
        # Weight of the crossing mode
        if n_modes_below[it] > n_modes_below[it-1]:
            # A mode entered: its index is n_modes_below[it]-1
            idx = n_modes_below[it] - 1
            mode_crossing_occ.append(occupations[it, idx])
        else:
            # A mode left: its index is n_modes_below[it]
            idx = n_modes_below[it]
            mode_crossing_occ.append(occupations[it-1, idx])

print(f"\nMode crossings through Lambda={Lambda_test}:")
print(f"{'tau':>8} {'n_below(after)':>14} {'occ_crossing':>14}")
for i in range(len(mode_crossing_taus)):
    it = np.argmin(np.abs(tau_values - mode_crossing_taus[i]))
    print(f"{mode_crossing_taus[i]:8.4f} {n_modes_below[it]:14d} "
          f"{mode_crossing_occ[i]:14.6f}")

print(f"\nMode count vs tau (selected points):")
print(f"{'tau':>8} {'n_below':>8} {'occ_below':>12} {'occ_above':>12}")
for it in [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 49]:
    print(f"{tau_values[it]:8.4f} {n_modes_below[it]:8d} "
          f"{occ_weight_below[it]:12.6f} {occ_weight_above[it]:12.6f}")

# =============================================================================
# 10. Decisive test: correlate barrier with mode crossings vs impedance
# =============================================================================
print(f"\n{'='*70}")
print(f"Section 10: DECISIVE TEST — impedance vs DOS control")
print(f"{'='*70}")

# Compute the derivative of n_modes_below with respect to tau
# At mode crossings, this is a delta function
# The S_occ derivative should correlate with EITHER:
#   (A) mode crossing events (delta functions in dn/dtau), or
#   (B) smooth impedance variation (gradual Z changes)

# For the sharp cutoff, S_occ = sum_k n_k * Theta(1 - lam_k^2/Lambda^2)
# = sum_{k: lam_k < Lambda} n_k(tau)
# So dS_occ/dtau = sum_{k: lam_k < Lambda} dn_k/dtau + n_k_crossing * delta(tau - tau_crossing)
#
# The first term is the smooth BCS occupation change (DOS-controlled).
# The second term is the discrete mode crossing (impedance-controlled in the sense
# that it's a sudden change in the number of contributing modes).

# Compute the smooth part: sum of dn_k/dtau for modes below cutoff
# The barrier is the TOTAL change, which includes both terms.

# Compute the smooth contribution to dS/dtau
dS_smooth = np.zeros(N_tau)
for it in range(1, N_tau-1):
    lam = eigenvalues[it]
    mask = lam**2 / Lambda_test**2 <= 1.0
    # Smooth part: change in occupation of FIXED set of modes
    if it > 0 and it < N_tau - 1:
        dn_occ = (occupations[it+1] - occupations[it-1]) / (2.0 * dtau)
        dS_smooth[it] = np.sum(dn_occ[mask])

# The total dS/dtau for sharp cutoff (from S54 data)
dS_sharp = np.gradient(S_occ[1, 0, :], dtau)  # Sharp cutoff, Lambda=1.0

# The discrete part: jumps at mode crossings
dS_discrete = dS_sharp - dS_smooth

# Compare magnitudes
print(f"\nDerivative decomposition at key tau points:")
print(f"{'tau':>8} {'dS_total':>12} {'dS_smooth':>12} {'dS_discrete':>12} {'ratio(d/s)':>12}")
for it in [5, 10, 15, 20, 25, 30, 35, 40, 45]:
    denom = abs(dS_smooth[it]) if abs(dS_smooth[it]) > 1e-15 else 1e-15
    ratio = abs(dS_discrete[it]) / denom
    print(f"{tau_values[it]:8.4f} {dS_sharp[it]:12.6f} {dS_smooth[it]:12.6f} "
          f"{dS_discrete[it]:12.6f} {ratio:12.4f}")

# =============================================================================
# 11. Summary statistics for gate verdict
# =============================================================================
print(f"\n{'='*70}")
print(f"Section 11: GATE SUMMARY — IMPEDANCE-55")
print(f"{'='*70}")

# Compute correlation between barrier and mode-count discontinuity
# At the sharp minimum (tau ~ 0.194), is there a mode crossing?
if len(mode_crossing_taus) > 0:
    nearest_crossing = min(mode_crossing_taus, key=lambda t: abs(t - 0.194))
    print(f"Nearest mode crossing to Sharp minimum (tau=0.194): tau={nearest_crossing:.4f}")
    print(f"  Distance: {abs(nearest_crossing - 0.194):.4f}")
else:
    print("No mode crossings found near Sharp minimum")

# Compute: fraction of S_occ change attributable to mode crossings vs smooth occupation
# In the search window [0.10, 0.30]
search_slice = slice(tau_lo_idx, tau_hi_idx+1)
total_variation_sharp = np.sum(np.abs(np.diff(S_occ[1, 0, search_slice])))
smooth_variation = np.sum(np.abs(dS_smooth[search_slice] * dtau))
discrete_variation = total_variation_sharp - smooth_variation

print(f"\nTotal variation of S_occ(Sharp, Lambda=1) in [0.10, 0.30]:")
print(f"  Total:    {total_variation_sharp:.6f}")
print(f"  Smooth:   {smooth_variation:.6f} ({100*smooth_variation/total_variation_sharp:.1f}%)")
print(f"  Discrete: {discrete_variation:.6f} ({100*discrete_variation/total_variation_sharp:.1f}%)")

# Barrier saturation test
if len(barrier_valid) >= 3:
    # Does the barrier saturate as alpha -> inf?
    # Compare ratio of last two barriers
    ratio_last = barrier_valid[-1] / barrier_valid[-2] if barrier_valid[-2] > 1e-15 else 999
    ratio_first = barrier_valid[1] / barrier_valid[0] if barrier_valid[0] > 1e-15 else 999
    print(f"\nBarrier saturation test:")
    print(f"  barrier[alpha={alpha_valid[-1]:.0f}] / barrier[alpha={alpha_valid[-2]:.0f}] = {ratio_last:.6f}")
    print(f"  barrier[alpha={alpha_valid[1]:.0f}] / barrier[alpha={alpha_valid[0]:.0f}] = {ratio_first:.6f}")
    if abs(ratio_last - 1.0) < 0.01:
        print(f"  SATURATED: barrier converges for alpha > {alpha_valid[-2]:.0f}")
        saturation_verdict = "SATURATED"
    else:
        print(f"  NOT SATURATED: barrier still changing at alpha = {alpha_valid[-1]:.0f}")
        saturation_verdict = "NOT_SATURATED"
else:
    saturation_verdict = "INSUFFICIENT_DATA"
    print(f"  Insufficient data for saturation test")

# The final classification
# DOS-controlled: barrier exists because mode count changes discretely with tau.
#   The occupation weights of the modes that cross the cutoff determine the barrier.
# Impedance-controlled: barrier exists because of the Z discontinuity at the edge.
#   The barrier scales with the reflection coefficient R(alpha).

# The physical distinction:
# - If DOS-controlled: the barrier survives for ANY cutoff that counts modes (even smooth ones)
# - If impedance-controlled: the barrier requires a sharp enough cutoff (alpha > alpha_crit)
#   to create sufficient reflection

# Compute alpha_crit: smallest alpha for which a barrier exists
alpha_crit = np.nan
for ia in range(N_alpha):
    if fd_has_min[ia]:
        alpha_crit = alpha_values[ia]
        break

print(f"\nalpha_crit (smallest alpha with barrier): {alpha_crit}")

# Compare barrier at alpha_crit with sharp-limit barrier
if not np.isnan(alpha_crit) and len(barrier_valid) > 0:
    ia_crit = np.where(alpha_values == alpha_crit)[0][0]
    if fd_has_min[ia_crit]:
        ratio_crit = barrier_vs_alpha[ia_crit] / barrier_valid[-1]
        print(f"barrier(alpha_crit) / barrier(alpha->inf) = {ratio_crit:.6f}")

    # If barrier exists even at alpha_crit << inf, it's DOS-controlled
    # If barrier only appears at alpha >> 1, it's impedance-controlled
    if alpha_crit <= 5.0:
        classification = "DOS-CONTROLLED"
        print(f"\nCLASSIFICATION: DOS-CONTROLLED")
        print(f"  Barrier appears at alpha = {alpha_crit:.1f} << sharp limit.")
        print(f"  Mode counting drives the barrier, not impedance mismatch.")
    elif alpha_crit <= 20.0:
        classification = "MIXED"
        print(f"\nCLASSIFICATION: MIXED (DOS + IMPEDANCE)")
        print(f"  Barrier appears at intermediate alpha = {alpha_crit:.1f}.")
        print(f"  Both mode counting and impedance contribute.")
    else:
        classification = "IMPEDANCE-CONTROLLED"
        print(f"\nCLASSIFICATION: IMPEDANCE-CONTROLLED")
        print(f"  Barrier requires sharp cutoff (alpha = {alpha_crit:.1f}).")
        print(f"  Impedance mismatch at cutoff edge is essential.")
else:
    classification = "NO_BARRIER"
    print(f"\nCLASSIFICATION: NO BARRIER FOUND")

# =============================================================================
# 12. Cross-check: compare with S54 Polynomial and Exponential
# =============================================================================
print(f"\n{'='*70}")
print(f"Section 12: Cross-check against S54 cutoff functions")
print(f"{'='*70}")

# The polynomial (1-x)^2 is a smooth cutoff with "impedance matching"
# The exponential exp(-x) is ultra-smooth
# Their barrier heights at Lambda=1.0:
print(f"Cutoff function barriers at Lambda=1.0:")
print(f"  Exponential: has_min={has_minimum[0,0]}, barrier={barrier_heights[0,0]:.6f}")
print(f"  Sharp:       has_min={has_minimum[1,0]}, barrier={barrier_heights[1,0]:.6f}")
print(f"  Polynomial:  has_min={has_minimum[2,0]}, barrier={barrier_heights[2,0]:.6f}")

# Compare: Exponential has NO barrier at Lambda=1.0
# Sharp has the LARGEST barrier (0.053)
# This is consistent with impedance theory: smooth cutoff = better matching = smaller barrier

# But the Polynomial also has NO barrier at Lambda=1.0...
# and the Sharp HAS a barrier. So the question is whether the barrier APPEARS
# because of the discontinuity (impedance) or because mode counting changes (DOS).

# Since Poly(1-x)^2 is C^0 at x=1 (f=0, df/dx = -2(1-x) -> 0 at x=1),
# it's smooth at the cutoff edge. So it provides impedance matching.
# The Exponential is C^inf everywhere -- ultimate matching.
# The Sharp is C^{-1} (discontinuous) -- zero matching.

# Check: does the Fermi-Dirac barrier track the S54 cutoffs?
# FD(alpha=1000) should approximate Sharp
# FD(alpha=2) should approximate Polynomial
# FD(alpha=0.5) should approximate Exponential

print(f"\nFermi-Dirac vs S54 cutoff comparison at tau=0.194 (fold region):")
for alpha_test in [0.5, 2.0, 1000.0]:
    ia_test = np.argmin(np.abs(alpha_values - alpha_test))
    print(f"  FD(alpha={alpha_test:.1f}): S_occ = {S_occ_fd[ia_test, sharp_min_idx]:.6f}")
print(f"  S54 Exp:   S_occ = {S_occ[0, 0, sharp_min_idx]:.6f}")
print(f"  S54 Sharp: S_occ = {S_occ[1, 0, sharp_min_idx]:.6f}")
print(f"  S54 Poly:  S_occ = {S_occ[2, 0, sharp_min_idx]:.6f}")

# =============================================================================
# 13. Impedance reflection coefficient R(tau) for sharp cutoff
# =============================================================================
# For the sharp cutoff at Lambda=1.0:
# R = 1 identically (total reflection: Z_above = 0)
# T = 0 (no transmission past cutoff)
#
# But the physical question is about the INTERNAL impedance matching
# within the occupied spectrum. Define:
#   Z_occupied(tau) = sum_k n_k(tau) * f(lam_k^2/Lambda^2)  [= S_occ]
#   Z_vacant(tau) = sum_k (1 - n_k(tau)) * f(lam_k^2/Lambda^2)
#
# The "reflection" between occupied and vacant channels:
#   R_occ_vac = |Z_occ - Z_vac|^2 / |Z_occ + Z_vac|^2
#
# This tells us about spectral weight redistribution.

Z_occ_sharp = S_occ[1, 0, :]  # Sharp, Lambda=1.0
Z_vac_sharp = S_vac[1, 0, :] - S_occ[1, 0, :]  # Vacant weight

R_occ_vac = np.zeros(N_tau)
for it in range(N_tau):
    Z_o = Z_occ_sharp[it]
    Z_v = Z_vac_sharp[it]
    denom = (Z_o + Z_v)**2
    if denom > 1e-30:
        R_occ_vac[it] = (Z_o - Z_v)**2 / denom
    else:
        R_occ_vac[it] = 1.0

print(f"\n{'='*70}")
print(f"Section 13: Occupied-Vacant reflection coefficient")
print(f"{'='*70}")
print(f"{'tau':>8} {'Z_occ':>12} {'Z_vac':>12} {'R_ov':>12} {'n_below':>8}")
for it in [0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 49]:
    print(f"{tau_values[it]:8.4f} {Z_occ_sharp[it]:12.6f} {Z_vac_sharp[it]:12.6f} "
          f"{R_occ_vac[it]:12.6f} {n_below[it]:8d}")

# Does R_occ_vac have a minimum near the fold?
R_search = R_occ_vac[tau_lo_idx:tau_hi_idx+1]
tau_R_min = tau_values[tau_lo_idx + np.argmin(R_search)]
R_min = R_search.min()
print(f"\nR_occ_vac minimum in [0.10, 0.30]: R = {R_min:.6f} at tau = {tau_R_min:.4f}")

# Correlation between R_occ_vac and S_occ barrier?
# If the barrier in S_occ correlates with a maximum in R_occ_vac, that supports
# impedance control.
dR_occ_vac = np.gradient(R_occ_vac, dtau)
dS_occ_sharp = np.gradient(S_occ[1, 0, :], dtau)

# Pearson correlation in search window
from numpy import corrcoef
corr = corrcoef(dR_occ_vac[search_slice], dS_occ_sharp[search_slice])[0, 1]
print(f"Pearson correlation between dR_occ_vac/dtau and dS_occ/dtau: {corr:.4f}")

# =============================================================================
# 14. Final verdict
# =============================================================================
print(f"\n{'='*70}")
print(f"IMPEDANCE-55 FINAL VERDICT")
print(f"{'='*70}")

# Collect all evidence
print(f"\nEvidence summary:")
print(f"  1. Barrier exists for Sharp (alpha->inf): YES (0.053)")
print(f"  2. Barrier exists for Exponential (smooth): NO")
print(f"  3. Barrier exists for Polynomial (C^0 smooth): NO")
print(f"  4. alpha_crit (smallest FD alpha with barrier): {alpha_crit}")
print(f"  5. Barrier saturation: {saturation_verdict}")
print(f"  6. Classification: {classification}")
print(f"  7. dR/dS correlation: {corr:.4f}")
print(f"  8. Smooth vs discrete variation: {100*smooth_variation/total_variation_sharp:.1f}% / {100*discrete_variation/total_variation_sharp:.1f}%")

# Write final answer
if classification == "DOS-CONTROLLED":
    verdict = ("The S_occ barrier at Lambda=1.0 is DOS-CONTROLLED. "
               "Barrier appears even at mild alpha because eigenvalue compression "
               "pushes modes through the cutoff edge as tau increases. "
               "The barrier height is set by the occupation weight of crossing modes, "
               "not by the impedance contrast at the edge.")
elif classification == "IMPEDANCE-CONTROLLED":
    verdict = ("The S_occ barrier at Lambda=1.0 is IMPEDANCE-CONTROLLED. "
               "Barrier requires sharp cutoff (alpha > alpha_crit). "
               "The discontinuity in spectral weight at the cutoff edge "
               "creates a reflection that prevents smooth spectral flow.")
elif classification == "MIXED":
    verdict = ("The S_occ barrier at Lambda=1.0 has MIXED character: "
               "mode counting (DOS) provides the basic mechanism through eigenvalue "
               "compression, but the barrier height is modulated by the cutoff "
               "sharpness (impedance). Both effects contribute.")
else:
    verdict = "No barrier found for analysis."

print(f"\n{verdict}")

# =============================================================================
# 15. Plots
# =============================================================================
fig = plt.figure(figsize=(18, 14))
gs = GridSpec(3, 3, figure=fig, hspace=0.35, wspace=0.3)

# Plot 1: S_occ for Fermi-Dirac family
ax1 = fig.add_subplot(gs[0, 0])
colors_fd = plt.cm.viridis(np.linspace(0, 1, N_alpha))
for ia in range(N_alpha):
    ax1.plot(tau_values, S_occ_fd[ia], color=colors_fd[ia],
             label=f'a={alpha_values[ia]:.0f}' if ia in [0, 2, 4, 6, 8, 9] else None,
             linewidth=0.8)
ax1.axvline(tau_fold, color='red', linestyle='--', alpha=0.5, linewidth=0.5)
ax1.set_xlabel('tau')
ax1.set_ylabel('S_occ')
ax1.set_title('Fermi-Dirac family, Lambda=1.0')
ax1.legend(fontsize=6, ncol=2)

# Plot 2: Barrier height vs alpha
ax2 = fig.add_subplot(gs[0, 1])
valid = ~np.isnan(barrier_vs_alpha)
if valid.any():
    ax2.semilogx(alpha_values[valid], barrier_vs_alpha[valid], 'ko-', markersize=4)
    ax2.axhline(barrier_heights[1, 0], color='red', linestyle='--',
                label=f'S54 Sharp={barrier_heights[1,0]:.4f}', linewidth=0.8)
    ax2.set_xlabel('alpha')
    ax2.set_ylabel('Barrier height')
    ax2.set_title('Barrier vs cutoff sharpness')
    ax2.legend(fontsize=7)

# Plot 3: Mode count vs tau
ax3 = fig.add_subplot(gs[0, 2])
ax3.step(tau_values, n_modes_below, where='mid', color='blue', linewidth=1)
ax3.set_xlabel('tau')
ax3.set_ylabel('N modes below Lambda=1')
ax3.set_title('Mode count at cutoff edge')
ax3.axvline(tau_fold, color='red', linestyle='--', alpha=0.5, linewidth=0.5)
# Mark mode crossings
for tc in mode_crossing_taus:
    ax3.axvline(tc, color='green', linestyle=':', alpha=0.3)

# Plot 4: Edge gap vs tau
ax4 = fig.add_subplot(gs[1, 0])
ax4.plot(tau_values, edge_gap, 'b-', linewidth=1)
ax4.set_xlabel('tau')
ax4.set_ylabel('Edge gap (lam_above - lam_below)')
ax4.set_title('Gap at cutoff edge')
ax4.axvline(tau_fold, color='red', linestyle='--', alpha=0.5, linewidth=0.5)

# Plot 5: Edge spectral weight W_edge
ax5 = fig.add_subplot(gs[1, 1])
for ia in [0, 2, 4, 6, 9]:
    ax5.plot(tau_values, W_edge_occ[ia], color=colors_fd[ia],
             label=f'a={alpha_values[ia]:.0f}', linewidth=0.8)
ax5.set_xlabel('tau')
ax5.set_ylabel('W_edge (occupied)')
ax5.set_title('Spectral weight at edge')
ax5.legend(fontsize=7)

# Plot 6: Occupied-Vacant reflection
ax6 = fig.add_subplot(gs[1, 2])
ax6.plot(tau_values, R_occ_vac, 'k-', linewidth=1)
ax6.set_xlabel('tau')
ax6.set_ylabel('R_occ_vac')
ax6.set_title('Occupied-Vacant reflection')
ax6.axvline(tau_fold, color='red', linestyle='--', alpha=0.5, linewidth=0.5)

# Plot 7: Derivative decomposition
ax7 = fig.add_subplot(gs[2, 0])
ax7.plot(tau_values, dS_sharp, 'k-', label='dS/dtau (total)', linewidth=1)
ax7.plot(tau_values, dS_smooth, 'b--', label='Smooth (occupation)', linewidth=0.8)
ax7.plot(tau_values, dS_discrete, 'r:', label='Discrete (crossings)', linewidth=0.8)
ax7.set_xlabel('tau')
ax7.set_ylabel('dS_occ/dtau')
ax7.set_title('Derivative decomposition (Sharp)')
ax7.legend(fontsize=7)
ax7.axvline(tau_fold, color='red', linestyle='--', alpha=0.5, linewidth=0.5)

# Plot 8: S_occ comparison (S54 vs FD sharp limit)
ax8 = fig.add_subplot(gs[2, 1])
ax8.plot(tau_values, S_occ[1, 0, :], 'k-', label='S54 Sharp', linewidth=1.5)
ax8.plot(tau_values, S_occ_fd[-1], 'r--', label=f'FD a={alpha_values[-1]:.0f}', linewidth=1)
ax8.plot(tau_values, S_occ_fd[4], 'b:', label=f'FD a={alpha_values[4]:.0f}', linewidth=1)
ax8.set_xlabel('tau')
ax8.set_ylabel('S_occ')
ax8.set_title('Sharp vs Fermi-Dirac')
ax8.legend(fontsize=7)
ax8.axvline(tau_fold, color='red', linestyle='--', alpha=0.5, linewidth=0.5)

# Plot 9: Occupation weight below cutoff
ax9 = fig.add_subplot(gs[2, 2])
ax9.plot(tau_values, occ_weight_below, 'b-', label='Below Lambda', linewidth=1)
ax9.plot(tau_values, occ_weight_above, 'r--', label='Above Lambda', linewidth=0.8)
ax9.set_xlabel('tau')
ax9.set_ylabel('Sum n_k')
ax9.set_title('Occupied weight below/above cutoff')
ax9.legend(fontsize=7)
ax9.axvline(tau_fold, color='red', linestyle='--', alpha=0.5, linewidth=0.5)

plt.suptitle('IMPEDANCE-55: Cutoff Edge Impedance Analysis', fontsize=14, fontweight='bold')
plt.savefig(os.path.join(data_dir, 's55_impedance.png'), dpi=150, bbox_inches='tight')
print(f"\nPlot saved: s55_impedance.png")

# =============================================================================
# 16. Save results
# =============================================================================
np.savez(os.path.join(data_dir, 's55_impedance.npz'),
    tau_values=tau_values,
    Lambda_test=Lambda_test,
    alpha_values=alpha_values,
    S_occ_fd=S_occ_fd,
    S_vac_fd=S_vac_fd,
    barrier_vs_alpha=barrier_vs_alpha,
    curvature_vs_alpha=curvature_vs_alpha,
    min_tau_vs_alpha=min_tau_vs_alpha,
    W_edge_occ=W_edge_occ,
    W_edge_vac=W_edge_vac,
    n_modes_below=n_modes_below,
    occ_weight_below=occ_weight_below,
    edge_gap=edge_gap,
    R_occ_vac=R_occ_vac,
    n_below=n_below,
    Z_below=Z_below,
    dos_below=dos_below,
    c_s_below=c_s_below,
    classification=np.array(classification),
    alpha_crit=np.array(alpha_crit),
    fd_has_min=fd_has_min,
    fd_barrier=fd_barrier,
)
print(f"Data saved: s55_impedance.npz")

print(f"\n{'='*70}")
print(f"IMPEDANCE-55 COMPLETE")
print(f"{'='*70}")
