#!/usr/bin/env python3
"""
S53 ACOUSTIC-CASIMIR-GL-53: Lattice Casimir Energy from Tight-Binding Bands
============================================================================

Physics:
  The 32-cell Voronoi tessellation of SU(3) with 6 GL phonon branches
  (Goldstone, 2 Leggett, 3 Higgs) has 6 x N_K = 192 modes (at N_K=32,
  one K-point per cell). The zero-point energy is:

    E_Casimir = (1/2) * sum_i sum_K  omega_i(K)

  This is a FINITE sum — the discrete lattice provides a natural UV
  cutoff at K_BZ = pi/a_BCC. No regularization is needed.

  We compute E_Casimir(tau) at the 15 tau values from s53_gl_sweep.npz
  and ask: is it monotone or non-monotone? Non-monotonicity would
  indicate a potential stabilization mechanism for the modulus tau.

  The Goldstone branch contributes the acoustic zero-point energy:
    E_Gold = (1/2) * sum_K  omega_Gold(K)

  which for a linear branch omega ~ c_Gold * |K| is dominated by
  modes near the BZ boundary.

Comparisons:
  (a) E_cond = -0.137 M_KK  (BCS condensation energy)
  (b) V_KK at fold            (Kaluza-Klein potential)
  (c) a0_fold = 6440           (spectral action volume term)

Gate: ACOUSTIC-CASIMIR-GL-53 — INFO
Author: Quantum-Acoustics-Theorist (S53)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from numpy import pi, sqrt
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    E_cond, tau_fold, a0_fold, N_cells,
    c_Gold, omega_L1, omega_L2, omega_H1, omega_H2, omega_H3,
    S_fold, Vol_SU3_Haar,
)

print("=" * 70)
print("S53 ACOUSTIC-CASIMIR-GL-53: Lattice Casimir from Tight-Binding Bands")
print("=" * 70)

# ============================================================
# Section 1: Load upstream data
# ============================================================
print("\n--- Section 1: Load upstream data ---")

# S52 GL Josephson: single tau (fold) dispersion
d52 = np.load(os.path.join(os.path.dirname(__file__),
              "s52_gl_josephson.npz"), allow_pickle=True)
K_array = d52['K_array']       # shape (51,), uniform grid [0, K_BZ]
K_BZ = float(d52['K_BZ'])
a_BCC = float(d52['a_BCC'])
N_K_grid = int(d52['N_K'])     # = 50 (51 points including K=0)
omega_fold = d52['omega_branches']  # shape (51, 6)
branch_labels = d52['branch_labels']

print(f"  K_BZ = {K_BZ:.6f} M_KK")
print(f"  a_BCC = {a_BCC:.4f} M_KK^{{-1}}")
print(f"  N_K grid points = {len(K_array)} (K=0 to K_BZ)")
print(f"  Branches: {list(branch_labels)}")

# S53 GL sweep: dispersion at 15 tau values
d53 = np.load(os.path.join(os.path.dirname(__file__),
              "s53_gl_sweep.npz"), allow_pickle=True)
tau_values = d53['tau_values']     # shape (15,)
omega_full = d53['omega_full']     # shape (15, 51, 6)
N_tau = int(d53['N_tau'])
K_plot = d53['K_plot']             # shape (51,), same as K_array
c_Gold_vs_tau = d53['c_Gold_vs_tau']  # shape (15,)
Delta_all = d53['Delta_all']       # shape (15, 3)
omega_BZ_all = d53['omega_BZ_all']   # shape (15, 6)

print(f"  Tau values ({N_tau}): {tau_values}")
print(f"  omega_full shape: {omega_full.shape}")

# ============================================================
# Section 2: Physical K-point sampling for 32-cell lattice
# ============================================================
print("\n--- Section 2: Physical K-point sampling ---")

# The physical lattice has N_cells = 32 cells in the BCC arrangement.
# For a 1D BCC chain analogy (which is what the dispersion uses —
# single K direction), the allowed K values in the first BZ are:
#   K_n = (2*pi*n) / (N_cells * a_BCC)  for n = 0, 1, ..., N_cells/2
# But we have the dispersion tabulated on a fine grid (51 points).
#
# Two approaches:
#   A) Use all 51 grid points as a fine approximation to the
#      continuous 1D BZ integral (trapezoidal rule).
#   B) Sample only the 32 physical K-points (discrete sum).
#
# We do BOTH and compare.

# Method A: Trapezoidal integration over continuous BZ
# In 1D, the density of states per unit K is L/(2*pi) = N_cells*a_BCC/(2*pi)
# E_Casimir = (1/2) * sum_branches integral_0^{K_BZ} omega(K) * [L/(2*pi)] dK
#           = (1/2) * N_cells * a_BCC/(2*pi) * sum_i integral omega_i(K) dK
#
# But since we want the total zero-point energy of the 32-cell system,
# we integrate over the BZ with density N_cells * a_BCC / (2*pi):

L_system = N_cells * a_BCC   # total system size in M_KK^{-1}
dos_1d = L_system / (2 * pi) # 1D density of states factor

print(f"  N_cells = {N_cells}")
print(f"  L_system = N_cells * a_BCC = {L_system:.4f} M_KK^{{-1}}")
print(f"  1D DOS factor = L/(2*pi) = {dos_1d:.4f}")
print(f"  K_BZ = pi/a = {K_BZ:.6f}")

# Method B: Physical K-points for N=32 cell chain
# K_n = n * 2*pi/(N*a) for n = 0, 1, ..., N/2
# Only N/2 + 1 = 17 distinct K-points (0 to K_BZ)
# but K=0 and K=K_BZ are special (each counted once, not twice)
# Total distinct modes = N per branch (counting +K and -K)

N_phys = N_cells  # = 32
K_phys = np.array([n * 2 * pi / (N_phys * a_BCC) for n in range(N_phys // 2 + 1)])
# K_phys has 17 points from K=0 to K_BZ

print(f"\n  Physical K-points (N={N_phys}, {len(K_phys)} unique):")
print(f"    K_phys = {K_phys[:5]}...{K_phys[-3:]}")
print(f"    K_phys[-1] = {K_phys[-1]:.6f} vs K_BZ = {K_BZ:.6f}")
print(f"    Match: {abs(K_phys[-1] - K_BZ) < 1e-10}")

# ============================================================
# Section 3: Interpolate dispersion to physical K-points
# ============================================================
print("\n--- Section 3: Interpolation to physical K-points ---")

from scipy.interpolate import interp1d

def get_omega_at_physical_K(omega_vs_K, K_grid, K_physical):
    """Interpolate 6-branch dispersion from fine grid to physical K-points."""
    n_branches = omega_vs_K.shape[1]
    omega_phys = np.zeros((len(K_physical), n_branches))
    for b in range(n_branches):
        f_interp = interp1d(K_grid, omega_vs_K[:, b], kind='cubic',
                           fill_value='extrapolate')
        omega_phys[:, b] = f_interp(K_physical)
    # Ensure non-negative (numerical)
    omega_phys = np.maximum(omega_phys, 0.0)
    return omega_phys

# Test at fold
omega_phys_fold = get_omega_at_physical_K(omega_fold, K_array, K_phys)

print(f"  Interpolated dispersion at fold (tau={tau_fold}):")
for b, label in enumerate(branch_labels):
    print(f"    {label:12s}: omega_min={omega_phys_fold[0,b]:.6f}, "
          f"omega_max={omega_phys_fold[-1,b]:.6f}")

# ============================================================
# Section 4: Compute Casimir energy (both methods)
# ============================================================
print("\n--- Section 4: Casimir energy computation ---")

def casimir_energy_trapz(omega_vs_K, K_grid, L_sys):
    """Method A: Trapezoidal integration over full BZ.

    E = (1/2) * (L/(2*pi)) * integral_{-K_BZ}^{K_BZ} omega(K) dK
      = (L/(2*pi)) * integral_0^{K_BZ} omega(K) dK    [using omega(K)=omega(-K)]

    The factor of 2 from the full BZ cancels the 1/2 from zero-point energy
    when integrating only over half-BZ with symmetry.
    """
    n_branches = omega_vs_K.shape[1]
    E_per_branch = np.zeros(n_branches)
    dos = L_sys / (2 * pi)
    _trapz = getattr(np, 'trapezoid', getattr(np, 'trapz', None))
    for b in range(n_branches):
        # Full BZ = 2 * half-BZ integral, times 1/2 zero-point = dos * int_0^KBZ
        E_per_branch[b] = dos * _trapz(omega_vs_K[:, b], K_grid)
    return E_per_branch

def casimir_energy_discrete(omega_phys, N_cells_val):
    """Method B: Discrete sum over physical K-points.

    For N cells, there are N allowed K-values per branch.
    K_n = n * 2*pi/(N*a) for n = 0, ..., N-1
    Using symmetry, K and -K give same omega, so:
    E = (1/2) * [omega(K=0) + omega(K_BZ) + 2 * sum_{n=1}^{N/2-1} omega(K_n)]
    per branch. This is for even N.
    """
    n_branches = omega_phys.shape[1]
    N_half = N_cells_val // 2  # = 16
    E_per_branch = np.zeros(n_branches)
    for b in range(n_branches):
        # omega_phys has N/2+1 = 17 points (K=0 through K_BZ)
        # K=0 and K=K_BZ each counted once (no partner)
        # K=1..N/2-1 each counted twice (K and -K)
        E_b = omega_phys[0, b]          # K=0 (once)
        E_b += omega_phys[-1, b]        # K=K_BZ (once)
        E_b += 2 * np.sum(omega_phys[1:-1, b])  # interior (twice)
        E_per_branch[b] = 0.5 * E_b
    return E_per_branch

# Fold computation
E_trapz_fold = casimir_energy_trapz(omega_fold, K_array, L_system)
E_disc_fold = casimir_energy_discrete(omega_phys_fold, N_cells)

E_total_trapz = np.sum(E_trapz_fold)
E_total_disc = np.sum(E_disc_fold)

print(f"\n  Method A (trapezoidal, continuous BZ):")
print(f"    Per branch:")
for b, label in enumerate(branch_labels):
    print(f"      {label:12s}: E_zp = {E_trapz_fold[b]:.6f} M_KK")
print(f"    Total E_Casimir = {E_total_trapz:.6f} M_KK")

print(f"\n  Method B (discrete, {N_cells} physical K-points):")
print(f"    Per branch:")
for b, label in enumerate(branch_labels):
    print(f"      {label:12s}: E_zp = {E_disc_fold[b]:.6f} M_KK")
print(f"    Total E_Casimir = {E_total_disc:.6f} M_KK")

print(f"\n  Agreement: {abs(E_total_trapz - E_total_disc)/abs(E_total_disc)*100:.2f}%")

# Per-mode average
E_per_mode_disc = E_total_disc / (6 * N_cells)
print(f"\n  E_Casimir / (6 * N_cells) = {E_per_mode_disc:.6f} M_KK per mode")

# Goldstone (acoustic) contribution
E_Gold_disc = E_disc_fold[0]
E_Gold_trapz = E_trapz_fold[0]
print(f"\n  Goldstone (acoustic) zero-point energy:")
print(f"    Discrete:     E_Gold = {E_Gold_disc:.6f} M_KK")
print(f"    Trapezoidal:  E_Gold = {E_Gold_trapz:.6f} M_KK")
print(f"    Fraction:     E_Gold/E_total = {E_Gold_disc/E_total_disc:.4f}")

# ============================================================
# Section 5: Comparison to energy scales
# ============================================================
print("\n--- Section 5: Energy scale comparison ---")

# Use discrete method (physical K-points)
E_Cas = E_total_disc

print(f"  E_Casimir = {E_Cas:.6f} M_KK")
print(f"  E_cond    = {E_cond:.6f} M_KK")
print(f"  |E_Cas/E_cond| = {abs(E_Cas/E_cond):.4f}")
print(f"  a0_fold   = {a0_fold:.1f} (spectral action volume term)")
print(f"  E_Cas/a0_fold = {E_Cas/a0_fold:.6e}")
print(f"  S_fold    = {S_fold:.2f} (full spectral action)")
print(f"  E_Cas/S_fold = {E_Cas/S_fold:.6e}")

# V_KK at fold: the spectral action gradient gives dS/dtau
# The "potential" is V = -S_fold in appropriate normalization
# More physically: the relevant energy scale is a0 * M_KK^4 in natural units
# Since everything is in M_KK units, the spectral action a0 itself is the scale
V_KK_fold = a0_fold  # order of magnitude
print(f"\n  V_KK scale ~ a0_fold = {V_KK_fold:.1f}")
print(f"  E_Cas / V_KK = {E_Cas / V_KK_fold:.6e}")

# ============================================================
# Section 6: E_Casimir(tau) across transit — monotonicity test
# ============================================================
print("\n--- Section 6: E_Casimir(tau) — tau sweep ---")

E_Cas_vs_tau_trapz = np.zeros((N_tau, 6))
E_Cas_vs_tau_disc = np.zeros((N_tau, 6))
E_total_vs_tau_trapz = np.zeros(N_tau)
E_total_vs_tau_disc = np.zeros(N_tau)
E_Gold_vs_tau = np.zeros(N_tau)

for t_idx in range(N_tau):
    tau = tau_values[t_idx]
    omega_t = omega_full[t_idx]  # shape (51, 6)

    # Method A
    E_Cas_vs_tau_trapz[t_idx] = casimir_energy_trapz(omega_t, K_plot, L_system)
    E_total_vs_tau_trapz[t_idx] = np.sum(E_Cas_vs_tau_trapz[t_idx])

    # Method B
    omega_phys_t = get_omega_at_physical_K(omega_t, K_plot, K_phys)
    E_Cas_vs_tau_disc[t_idx] = casimir_energy_discrete(omega_phys_t, N_cells)
    E_total_vs_tau_disc[t_idx] = np.sum(E_Cas_vs_tau_disc[t_idx])
    E_Gold_vs_tau[t_idx] = E_Cas_vs_tau_disc[t_idx, 0]

print(f"  {'tau':>6s}  {'E_total(disc)':>14s}  {'E_Gold':>10s}  {'E_total(trapz)':>14s}")
for t_idx in range(N_tau):
    print(f"  {tau_values[t_idx]:6.3f}  {E_total_vs_tau_disc[t_idx]:14.6f}  "
          f"{E_Gold_vs_tau[t_idx]:10.6f}  {E_total_vs_tau_trapz[t_idx]:14.6f}")

# ============================================================
# Section 7: Monotonicity analysis
# ============================================================
print("\n--- Section 7: Monotonicity analysis ---")

# Use discrete method
E_tot = E_total_vs_tau_disc

# Check monotonicity
dE = np.diff(E_tot)
dtau = np.diff(tau_values)
dEdtau = dE / dtau

monotone_increasing = np.all(dE > 0)
monotone_decreasing = np.all(dE < 0)
is_monotone = monotone_increasing or monotone_decreasing

print(f"  E_total range: [{E_tot.min():.6f}, {E_tot.max():.6f}] M_KK")
print(f"  Delta_E = E_max - E_min = {E_tot.max() - E_tot.min():.6f} M_KK")
print(f"  Relative variation: {(E_tot.max()-E_tot.min())/E_tot.mean()*100:.4f}%")
print(f"\n  dE/dtau values:")
for i in range(len(dEdtau)):
    tau_mid = (tau_values[i] + tau_values[i+1]) / 2
    sign = "+" if dEdtau[i] > 0 else "-"
    print(f"    tau ~ {tau_mid:.3f}: dE/dtau = {dEdtau[i]:+.6f} ({sign})")

if monotone_increasing:
    print(f"\n  MONOTONE INCREASING across [{tau_values[0]:.2f}, {tau_values[-1]:.2f}]")
elif monotone_decreasing:
    print(f"\n  MONOTONE DECREASING across [{tau_values[0]:.2f}, {tau_values[-1]:.2f}]")
else:
    # Find extrema
    extrema_idx = []
    for i in range(1, len(dE)):
        if dE[i] * dE[i-1] < 0:
            extrema_idx.append(i)
    print(f"\n  NON-MONOTONE: {len(extrema_idx)} sign change(s) in dE/dtau")
    for idx in extrema_idx:
        tau_ext = tau_values[idx]
        E_ext = E_tot[idx]
        ext_type = "MAXIMUM" if dE[idx-1] > 0 and dE[idx] < 0 else "MINIMUM"
        print(f"    {ext_type} near tau = {tau_ext:.3f}, E = {E_ext:.6f} M_KK")

# Per-branch monotonicity
print(f"\n  Per-branch monotonicity:")
branch_names = ['Goldstone', 'Leggett-1', 'Leggett-2', 'Branch-3', 'Branch-4', 'Higgs-1']
for b in range(6):
    E_b = E_Cas_vs_tau_disc[:, b]
    dE_b = np.diff(E_b)
    if np.all(dE_b > 0):
        mono = "INCREASING"
    elif np.all(dE_b < 0):
        mono = "DECREASING"
    else:
        n_sign = np.sum(np.diff(np.sign(dE_b)) != 0)
        mono = f"NON-MONOTONE ({n_sign} sign change(s))"
    print(f"    {branch_names[b]:12s}: E=[{E_b.min():.6f}, {E_b.max():.6f}], {mono}")

# ============================================================
# Section 8: Goldstone branch acoustic analysis
# ============================================================
print("\n--- Section 8: Goldstone (acoustic) zero-point energy ---")

# For a linear dispersion omega = c * |K|, the zero-point energy
# on a 1D lattice with N modes is:
#   E_Gold = (1/2) * c * sum_n |K_n|
# For K_n = n * delta_K, n=1..N/2 (counting +K and -K):
#   E_Gold = c * sum_{n=1}^{N/2-1} K_n + (c/2) * K_BZ
#          = c * delta_K * [sum_{n=1}^{N/2-1} n] + (c/2) * K_BZ
#          = c * delta_K * (N/2-1)*N/4 + (c/2)*K_BZ

# Compare analytic vs computed
for t_idx, tau in enumerate(tau_values):
    c_g = c_Gold_vs_tau[t_idx]
    # Analytic for linear dispersion
    delta_K = 2 * pi / (N_cells * a_BCC)
    E_analytic = 0.0  # (local)
    for n in range(1, N_cells // 2):
        E_analytic += c_g * n * delta_K  # two modes (K, -K) -> factor 2, but (1/2) cancels
    E_analytic += 0.5 * c_g * K_BZ  # BZ edge, counted once
    # K=0 contributes 0 for Goldstone

    E_computed = E_Gold_vs_tau[t_idx]

    if t_idx == 0 or t_idx == 9 or t_idx == N_tau-1:
        print(f"  tau={tau:.3f}: c_Gold={c_g:.6f}, "
              f"E_Gold(analytic)={E_analytic:.6f}, "
              f"E_Gold(computed)={E_computed:.6f}, "
              f"ratio={E_computed/E_analytic:.6f}")

# The ratio != 1 because the actual Goldstone branch is not exactly linear
# (it has alpha ~ 0.96, not 1.0)

# ============================================================
# Section 9: Stabilization assessment
# ============================================================
print("\n--- Section 9: Stabilization assessment ---")

# Find the extremum location if non-monotone
if not is_monotone:
    # Fit a polynomial to find precise extremum
    from numpy.polynomial import polynomial as P
    # Use quadratic fit near the extremum
    for idx in extrema_idx:
        # Use 5 points around the extremum
        i_lo = max(0, idx - 2)
        i_hi = min(N_tau, idx + 3)
        tau_fit = tau_values[i_lo:i_hi]
        E_fit = E_tot[i_lo:i_hi]

        # Quadratic fit
        coeffs = np.polyfit(tau_fit, E_fit, 2)
        tau_ext = -coeffs[1] / (2 * coeffs[0])
        E_ext = np.polyval(coeffs, tau_ext)
        curvature = 2 * coeffs[0]

        ext_type = "MAXIMUM" if coeffs[0] < 0 else "MINIMUM"
        print(f"  Fitted {ext_type} at tau = {tau_ext:.4f}")
        print(f"  E_Casimir at extremum = {E_ext:.6f} M_KK")
        print(f"  Curvature d^2E/dtau^2 = {curvature:.4f}")
        print(f"  Depth from boundary = {abs(E_ext - max(E_tot[0], E_tot[-1])):.6f} M_KK")

        # Compare curvature to spectral action
        print(f"\n  Curvature comparison:")
        print(f"    d^2 E_Cas / dtau^2 = {curvature:.4f}")
        print(f"    d^2 S_fold / dtau^2 = {317862.85:.2f} (from canonical)")
        print(f"    Ratio = {abs(curvature) / 317862.85:.6e}")

        # Effective modulus mass from curvature
        # In the Friedmann equation, the modulus obeys M * d^2 tau/dt^2 = -dV/dtau
        # The effective frequency is omega_mod^2 = |d^2V/dtau^2| / M
        # For M_ATDHFB = 1.695 (from canonical):
        M_ATDHFB = 1.695  # canonical
        omega_mod_sq = abs(curvature) / M_ATDHFB
        omega_mod = sqrt(omega_mod_sq) if omega_mod_sq > 0 else 0
        print(f"    omega_mod (from Casimir) = {omega_mod:.6f} M_KK")
        print(f"    omega_att (from spectral) = 1.430 M_KK")
        if omega_mod > 0:
            print(f"    omega_Cas / omega_att = {omega_mod / 1.430:.6e}")
else:
    print(f"  E_Casimir is MONOTONE across the tau range.")
    print(f"  No stabilization from lattice Casimir effect.")

    # Report the gradient
    dE_dtau_mean = (E_tot[-1] - E_tot[0]) / (tau_values[-1] - tau_values[0])
    print(f"\n  Mean gradient dE_Cas/dtau = {dE_dtau_mean:.4f} M_KK per unit tau")
    print(f"  Spectral action gradient dS/dtau|_fold = {58672.80:.2f}")
    print(f"  Ratio = {abs(dE_dtau_mean) / 58672.80:.6e}")

# ============================================================
# Section 10: Decomposition by mode type
# ============================================================
print("\n--- Section 10: Energy decomposition ---")

# At the fold (tau=0.19, index 9)
fold_idx = 9  # tau = 0.19 (local)
E_branches_fold = E_Cas_vs_tau_disc[fold_idx]
E_total_fold = E_total_vs_tau_disc[fold_idx]

print(f"\n  Energy decomposition at tau = {tau_values[fold_idx]:.2f} (fold):")
print(f"  {'Branch':12s}  {'E_zp (M_KK)':>12s}  {'Fraction':>10s}  {'Character':10s}")
for b in range(6):
    frac = E_branches_fold[b] / E_total_fold
    char = "acoustic" if b == 0 else ("optical" if b < 3 else "gapped")
    print(f"  {branch_names[b]:12s}  {E_branches_fold[b]:12.6f}  {frac:10.4f}  {char:10s}")
print(f"  {'TOTAL':12s}  {E_total_fold:12.6f}")

# Phase vs amplitude decomposition
# Branches 0-2 are primarily phase modes; 3-5 are amplitude-dominated at K=0
E_phase = np.sum(E_branches_fold[:3])
E_amp = np.sum(E_branches_fold[3:])
print(f"\n  Phase modes (0-2):     {E_phase:.6f} M_KK ({E_phase/E_total_fold:.4f})")
print(f"  Amplitude modes (3-5): {E_amp:.6f} M_KK ({E_amp/E_total_fold:.4f})")

# ============================================================
# Section 11: Gate verdict
# ============================================================
print("\n--- Section 11: Gate ACOUSTIC-CASIMIR-GL-53 ---")

gate_name = "ACOUSTIC-CASIMIR-GL-53"
gate_verdict = "INFO"

if is_monotone:
    mono_str = "MONOTONE"
    stab_str = "NO STABILIZATION"
else:
    mono_str = "NON-MONOTONE"
    stab_str = f"{len(extrema_idx)} extremum/a found"

gate_detail = (f"E_Casimir = {E_total_fold:.4f} M_KK at fold. "
               f"|E_Cas/E_cond| = {abs(E_total_fold/E_cond):.1f}. "
               f"E_Cas/a0 = {E_total_fold/a0_fold:.2e}. "
               f"E_Casimir(tau) is {mono_str}. {stab_str}. "
               f"Goldstone fraction = {E_Gold_vs_tau[fold_idx]/E_total_fold:.4f}.")

print(f"  Gate: {gate_name}")
print(f"  Verdict: {gate_verdict}")
print(f"  Detail: {gate_detail}")

# ============================================================
# Section 12: Plotting
# ============================================================
print("\n--- Section 12: Plotting ---")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("S53 ACOUSTIC-CASIMIR-GL-53: Lattice Casimir Energy", fontsize=14)

# Panel 1: E_Casimir(tau) total
ax = axes[0, 0]
ax.plot(tau_values, E_total_vs_tau_disc, 'ko-', lw=2, ms=5, label='Total (discrete)')
ax.plot(tau_values, E_total_vs_tau_trapz, 'b--', lw=1.5, alpha=0.7, label='Total (trapz)')
ax.axvline(tau_fold, color='r', ls=':', alpha=0.5, label=f'fold (tau={tau_fold})')
ax.set_xlabel('tau')
ax.set_ylabel('E_Casimir (M_KK)')
ax.set_title('Total zero-point energy')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 2: E_Casimir per branch vs tau
ax = axes[0, 1]
colors = ['blue', 'green', 'orange', 'red', 'purple', 'brown']
for b in range(6):
    ax.plot(tau_values, E_Cas_vs_tau_disc[:, b], 'o-', color=colors[b],
            lw=1.5, ms=3, label=branch_names[b])  # (local)
ax.axvline(tau_fold, color='r', ls=':', alpha=0.5)
ax.set_xlabel('tau')
ax.set_ylabel('E_zp per branch (M_KK)')
ax.set_title('Zero-point energy by branch')
ax.legend(fontsize=7, ncol=2)
ax.set_yscale('log')
ax.grid(True, alpha=0.3)

# Panel 3: Goldstone acoustic energy
ax = axes[1, 0]
ax.plot(tau_values, E_Gold_vs_tau, 'bo-', lw=2, ms=5)
ax.axvline(tau_fold, color='r', ls=':', alpha=0.5, label=f'fold')
ax.set_xlabel('tau')
ax.set_ylabel('E_Gold (M_KK)')
ax.set_title('Goldstone (acoustic) zero-point energy')
ax2 = ax.twinx()
ax2.plot(tau_values, c_Gold_vs_tau, 'g--', lw=1.5, alpha=0.7)
ax2.set_ylabel('c_Gold (M_KK units)', color='green')
ax2.tick_params(axis='y', labelcolor='green')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 4: dE/dtau
ax = axes[1, 1]
tau_mid = (tau_values[:-1] + tau_values[1:]) / 2
ax.plot(tau_mid, dEdtau, 'ko-', lw=2, ms=5)
ax.axhline(0, color='gray', ls='--', alpha=0.5)
ax.axvline(tau_fold, color='r', ls=':', alpha=0.5, label=f'fold')
ax.set_xlabel('tau')
ax.set_ylabel('dE_Casimir / dtau')
ax.set_title('Casimir energy gradient')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

plt.tight_layout()
outpng = os.path.join(os.path.dirname(__file__), "s53_acoustic_casimir.png")
plt.savefig(outpng, dpi=150)
print(f"  Saved: {outpng}")

# ============================================================
# Section 13: Save data
# ============================================================
print("\n--- Section 13: Saving data ---")

outnpz = os.path.join(os.path.dirname(__file__), "s53_acoustic_casimir.npz")
np.savez(outnpz,
    # Tau sweep
    tau_values=tau_values,
    E_total_vs_tau=E_total_vs_tau_disc,
    E_branches_vs_tau=E_Cas_vs_tau_disc,
    E_Gold_vs_tau=E_Gold_vs_tau,
    E_total_trapz=E_total_vs_tau_trapz,
    # Fold values
    E_Casimir_fold=E_total_fold,
    E_branches_fold=E_branches_fold,
    E_Gold_fold=E_Gold_vs_tau[fold_idx],
    # Physical K-points
    K_phys=K_phys,
    N_cells=N_cells,
    K_BZ=K_BZ,
    a_BCC=a_BCC,
    # Derived
    c_Gold_vs_tau=c_Gold_vs_tau,
    is_monotone=np.array([is_monotone]),
    # Gate
    gate_name=np.array([gate_name]),
    gate_verdict=np.array([gate_verdict]),
    gate_detail=np.array([gate_detail]),
)
print(f"  Saved: {outnpz}")

# ============================================================
# Summary
# ============================================================
print("\n" + "=" * 70)
print("SUMMARY: ACOUSTIC-CASIMIR-GL-53")
print("=" * 70)
print(f"  Lattice: BCC, a = {a_BCC:.4f}, K_BZ = {K_BZ:.4f}, N_cells = {N_cells}")
print(f"  6 branches, {6*N_cells} = {6*N_cells} physical modes")
print(f"  15 tau values: [{tau_values[0]:.2f}, {tau_values[-1]:.2f}]")
print(f"")
print(f"  E_Casimir at fold = {E_total_fold:.4f} M_KK")
print(f"    |E_Cas/E_cond| = {abs(E_total_fold/E_cond):.1f}")
print(f"    E_Cas/a0_fold = {E_total_fold/a0_fold:.2e}")
print(f"    Goldstone fraction: {E_Gold_vs_tau[fold_idx]/E_total_fold:.4f}")
print(f"    Higgs-1 fraction: {E_branches_fold[5]/E_total_fold:.4f}")
print(f"")
print(f"  E_Casimir(tau): {mono_str}")
if not is_monotone:
    print(f"    Extremum at tau ~ {tau_ext:.4f}, depth {abs(E_ext - max(E_tot[0], E_tot[-1])):.6f} M_KK")
else:
    print(f"    Variation: {E_tot.max()-E_tot.min():.4f} M_KK ({(E_tot.max()-E_tot.min())/E_tot.mean()*100:.2f}%)")
print(f"")
print(f"  Gate: {gate_name} — {gate_verdict}")
print(f"  {gate_detail}")
print("=" * 70)
