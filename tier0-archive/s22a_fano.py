#!/usr/bin/env python3
"""
Session 22a QA-2: Fano Parameter q(tau) at Monopole Locations

Extracts the Fano resonance parameter from the avoided crossing lineshapes
at M1 (tau ~ 0.11) and M2 (tau ~ 1.58).

The Fano profile characterizes the interference between a discrete state
(the gap-edge mode switching sector identity) and a continuum background
(the bulk spectral density). The lineshape asymmetry encodes the coupling
strength — |q| >> 1 means strong coupling (Fano-dominated), |q| ~ 0 means
pure Lorentzian (weak coupling).

Method: Fit the gap-edge eigenvalue trajectory near the avoided crossing
to the standard Fano lineshape in tau-space:

  delta_E(tau) = delta_min * |epsilon + q|^2 / (epsilon^2 + 1)

where epsilon = (tau - tau_0) / (Gamma/2) is the reduced deformation parameter,
delta_min is the minimum splitting, and Gamma is the width.

Data:
  M1: s19a_sweep_data.npz (coarse grid, tau step = 0.1)
  M2: s21c_neutrino_fine_grid.npz (fine grid, tau step = 0.02)

Author: quantum-acoustics-theorist
Date: 2026-02-20
"""

import numpy as np
from scipy.optimize import curve_fit
from pathlib import Path

data_dir = Path(__file__).parent

# ============================================================
# 1. FANO LINESHAPE FUNCTIONS
# ============================================================

def fano_profile(epsilon, q):
    """Standard Fano lineshape: sigma = (epsilon + q)^2 / (epsilon^2 + 1)"""
    return (epsilon + q)**2 / (epsilon**2 + 1)

def fano_delta_E(tau, tau_0, Gamma, delta_min, q, offset):
    """
    Gap splitting as a function of tau, modeled as Fano lineshape.
    delta_E(tau) = offset + delta_min * |(epsilon + q)|^2 / (epsilon^2 + 1)
    where epsilon = (tau - tau_0) / (Gamma/2)
    """
    epsilon = (tau - tau_0) / (Gamma / 2)
    return offset + delta_min * (epsilon + q)**2 / (epsilon**2 + 1)


# ============================================================
# 2. M2 ANALYSIS (FINE GRID, tau step = 0.02)
# ============================================================

print("=" * 70)
print("SESSION 22a QA-2: FANO PARAMETER AT MONOPOLE LOCATIONS")
print("=" * 70)
print()

# Load fine-grid data near M2
d_fine = np.load(data_dir / 's21c_neutrino_fine_grid.npz', allow_pickle=True)
tau_fine = d_fine['tau_fine']
L1 = d_fine['pq6_lambda1']  # lowest eigenvalue
L2 = d_fine['pq6_lambda2']  # second lowest
L3 = d_fine['pq6_lambda3']  # third lowest

# The "gap splitting" is delta = L2 - L1 (the avoided crossing gap)
delta_M2 = L2 - L1
print("--- M2 Fine-Grid Data (tau_fine, 11 points) ---")
print(f"{'tau':>6s} {'L1':>12s} {'L2':>12s} {'delta':>12s}")
for i in range(len(tau_fine)):
    print(f"{tau_fine[i]:6.2f} {L1[i]:12.6f} {L2[i]:12.6f} {delta_M2[i]:12.6f}")

# Find the minimum splitting
i_min = np.argmin(delta_M2)
delta_min_M2 = delta_M2[i_min]
tau_0_M2 = tau_fine[i_min]
print(f"\nMinimum splitting: delta_min = {delta_min_M2:.8f} at tau_0 = {tau_0_M2:.2f}")

# The Fano parameter can be extracted from the ASYMMETRY of the
# splitting profile around the minimum.
# Key diagnostic: ratio of delta at equal distances on either side
# of the minimum. For a symmetric (Breit-Wigner/Lorentzian) profile,
# this ratio = 1. For Fano, it deviates.

# Compute asymmetry ratio at several distances
print("\n--- Asymmetry Analysis (M2) ---")
for offset in [1, 2, 3, 4]:
    i_lo = i_min - offset
    i_hi = i_min + offset
    if 0 <= i_lo and i_hi < len(tau_fine):
        ratio = delta_M2[i_hi] / delta_M2[i_lo]
        print(f"  offset={offset} steps: delta(tau_0-{offset*0.02:.2f})={delta_M2[i_lo]:.6f}, "
              f"delta(tau_0+{offset*0.02:.2f})={delta_M2[i_hi]:.6f}, ratio={ratio:.4f}")

# Fit Fano profile to delta_M2
# Use epsilon = (tau - tau_0) / (Gamma/2) parametrization
# delta_E = delta_min * (epsilon + q)^2 / (epsilon^2 + 1)
try:
    # Initial guess: tau_0 from minimum, Gamma ~ 0.1, q ~ 1
    p0 = [tau_0_M2, 0.10, delta_min_M2, 1.0, 0.0]
    bounds = ([1.50, 0.01, 0.0, -10, -0.001], [1.68, 0.50, 0.01, 10, 0.001])
    popt, pcov = curve_fit(fano_delta_E, tau_fine, delta_M2, p0=p0, bounds=bounds, maxfev=10000)
    tau_0_fit, Gamma_fit, dmin_fit, q_fit, offset_fit = popt
    perr = np.sqrt(np.diag(pcov))

    print(f"\n--- Fano Fit (M2) ---")
    print(f"  tau_0  = {tau_0_fit:.4f} +/- {perr[0]:.4f}")
    print(f"  Gamma  = {Gamma_fit:.4f} +/- {perr[1]:.4f}")
    print(f"  d_min  = {dmin_fit:.6f} +/- {perr[2]:.6f}")
    print(f"  q      = {q_fit:.4f} +/- {perr[3]:.4f}")
    print(f"  offset = {offset_fit:.6f} +/- {perr[4]:.6f}")
    print(f"  |q|    = {abs(q_fit):.4f}")

    # Compute residuals
    delta_fit = fano_delta_E(tau_fine, *popt)
    rms = np.sqrt(np.mean((delta_M2 - delta_fit)**2))
    print(f"  RMS residual = {rms:.8f}")
    print(f"  Relative RMS = {rms/delta_min_M2:.4f}")
    q_M2 = q_fit
    Gamma_M2 = Gamma_fit
except Exception as e:
    print(f"\nFano fit failed for M2: {e}")
    q_M2 = None
    Gamma_M2 = None

# Alternative: direct asymmetry-based q estimate
# For Fano: delta(epsilon) = (epsilon + q)^2 / (epsilon^2 + 1) * delta_min
# At epsilon = +1 and -1:
# delta(+1) = (1+q)^2 / 2 * delta_min
# delta(-1) = (-1+q)^2 / 2 * delta_min
# Ratio: delta(+1)/delta(-1) = (1+q)^2/(q-1)^2
# => q = (1+r^(1/2)) / (r^(1/2) - 1) where r = delta(+1)/delta(-1)
# This works when we know the width Gamma

print("\n--- Direct Asymmetry q Estimate (M2) ---")
# Use the splitting at symmetric offsets from minimum
# as epsilon ~ +/- n
for n_steps in [1, 2, 3]:
    i_lo = i_min - n_steps
    i_hi = i_min + n_steps
    if 0 <= i_lo and i_hi < len(tau_fine):
        r = delta_M2[i_hi] / delta_M2[i_lo]
        if r > 0 and r != 1:
            sqrt_r = np.sqrt(r)
            if sqrt_r > 1:
                q_est = (1 + sqrt_r) / (sqrt_r - 1)
            else:
                q_est = -(1 + sqrt_r) / (1 - sqrt_r)
            print(f"  n={n_steps}: ratio={r:.4f}, |q_est| = {abs(q_est):.4f}")


# ============================================================
# 3. M1 ANALYSIS (COARSE GRID, tau step = 0.1)
# ============================================================

print()
print("=" * 70)
print("M1 ANALYSIS (COARSE GRID)")
print("=" * 70)
print()

# Load coarse grid data
d_coarse = np.load(data_dir / 's19a_sweep_data.npz', allow_pickle=True)
tau = d_coarse['tau_values']

# Track the (0,0) singlet and (0,1)/(1,0) fundamental eigenvalues
E_singlet = np.zeros(21)
E_fund = np.zeros(21)

for i in range(21):
    ev = d_coarse[f'eigenvalues_{i}']
    p = d_coarse[f'sector_p_{i}']
    q = d_coarse[f'sector_q_{i}']

    mask_00 = (p == 0) & (q == 0)
    mask_01 = (p == 0) & (q == 1)
    mask_10 = (p == 1) & (q == 0)

    E_singlet[i] = ev[mask_00].min()
    E_fund[i] = min(ev[mask_01].min(), ev[mask_10].min())

delta_M1 = np.abs(E_singlet - E_fund)

print("--- M1 Coarse-Grid Data ---")
print(f"{'tau':>6s} {'E_singlet':>12s} {'E_fund':>12s} {'delta':>12s} {'who_leads':>12s}")
for i in range(6):  # first 6 points span M1
    leader = "(0,1)" if E_fund[i] < E_singlet[i] else "(0,0)"
    print(f"{tau[i]:6.2f} {E_singlet[i]:12.6f} {E_fund[i]:12.6f} {delta_M1[i]:12.6f} {leader:>12s}")

# The crossing is between tau=0.10 and tau=0.20
# At tau=0.10: delta = 0.001623 (near-degenerate)
# At tau=0.00: delta = 0.032692 (well separated)
# At tau=0.20: delta = 0.017636

# The minimum delta is at tau=0.10
i_min_M1 = np.argmin(delta_M1[:6])
print(f"\nMinimum splitting: delta = {delta_M1[i_min_M1]:.6f} at tau = {tau[i_min_M1]:.2f}")

# Asymmetry around the minimum (only 1 point on each side available)
if i_min_M1 > 0 and i_min_M1 < 5:
    ratio_M1 = delta_M1[i_min_M1 + 1] / delta_M1[i_min_M1 - 1]
    sqrt_r_M1 = np.sqrt(ratio_M1)
    if sqrt_r_M1 > 1:
        q_est_M1 = (1 + sqrt_r_M1) / (sqrt_r_M1 - 1)
    else:
        q_est_M1 = -(1 + sqrt_r_M1) / (1 - sqrt_r_M1)
    print(f"\nAsymmetry: delta(tau=0.20)/delta(tau=0.00) = {ratio_M1:.4f}")
    print(f"|q_est| (M1) = {abs(q_est_M1):.4f}")
else:
    q_est_M1 = None
    print("\nCannot estimate q at M1 (minimum at boundary)")

# Fit Fano to M1 coarse data (limited: only ~5 relevant points)
try:
    # Use first 6 points
    tau_M1 = tau[:6]
    delta_M1_data = delta_M1[:6]
    p0_M1 = [0.10, 0.10, 0.001, 2.0, 0.0]
    bounds_M1 = ([0.05, 0.02, 0.0, -20, -0.01], [0.20, 0.50, 0.05, 20, 0.01])
    popt_M1, pcov_M1 = curve_fit(fano_delta_E, tau_M1, delta_M1_data,
                                  p0=p0_M1, bounds=bounds_M1, maxfev=10000)
    tau0_M1, G_M1, dmin_M1, q_M1_fit, off_M1 = popt_M1
    perr_M1 = np.sqrt(np.diag(pcov_M1))
    print(f"\n--- Fano Fit (M1, coarse) ---")
    print(f"  tau_0 = {tau0_M1:.4f} +/- {perr_M1[0]:.4f}")
    print(f"  Gamma = {G_M1:.4f} +/- {perr_M1[1]:.4f}")
    print(f"  d_min = {dmin_M1:.6f} +/- {perr_M1[2]:.6f}")
    print(f"  q     = {q_M1_fit:.4f} +/- {perr_M1[3]:.4f}")
    print(f"  |q|   = {abs(q_M1_fit):.4f}")

    delta_fit_M1 = fano_delta_E(tau_M1, *popt_M1)
    rms_M1 = np.sqrt(np.mean((delta_M1_data - delta_fit_M1)**2))
    print(f"  RMS residual = {rms_M1:.8f}")
except Exception as e:
    print(f"\nFano fit failed for M1: {e}")
    q_M1_fit = None


# ============================================================
# 4. COUPLING STRENGTH ESTIMATE FROM FANO
# ============================================================

print()
print("=" * 70)
print("COUPLING STRENGTH ANALYSIS")
print("=" * 70)
print()

# The Fano parameter q = V_coupling / (pi * rho_background * Gamma)
# where V is the off-diagonal coupling matrix element between the
# discrete (gap-edge) and continuum (bulk) channels.

# At M2 (fine grid):
if q_M2 is not None and Gamma_M2 is not None:
    # The minimum splitting delta_min is related to the coupling:
    # delta_min ~ 2 * V^2 / (typical level spacing of background)
    # Or equivalently, from the avoided crossing:
    # delta_min = 2 * |V_coupling| in the 2-level model
    V_coupling_M2 = delta_min_M2 / 2
    print(f"M2 coupling estimates:")
    print(f"  Minimum splitting: {delta_min_M2:.8f}")
    print(f"  V_coupling (2-level): {V_coupling_M2:.8f}")
    print(f"  Fano |q|: {abs(q_M2):.4f}")
    print(f"  Width Gamma: {Gamma_M2:.4f}")

# At M1 (coarse grid, less reliable):
print(f"\nM1 estimates (COARSE GRID - less reliable):")
delta_min_M1_val = delta_M1[i_min_M1]
V_coupling_M1 = delta_min_M1_val / 2
print(f"  Minimum splitting: {delta_min_M1_val:.6f}")
print(f"  V_coupling (2-level): {V_coupling_M1:.6f}")

# Coupling/gap ratio (the Session 21b diagnostic)
# gap at M1 ~ 0.832, coupling ~ 0.001/2 = 0.0005 -> ratio ~ 0.0006
# gap at M2 ~ 2.12, coupling ~ 0.000008/2 = 0.000004 -> ratio ~ 0.000002
# These are MUCH smaller than the 4-5x ratio claimed from block-diagonal analysis
# because these are the gap-edge crossings, not the full off-diagonal coupling
print(f"\nCoupling/gap ratios at avoided crossings:")
print(f"  M1: V/E_gap = {V_coupling_M1/E_fund[i_min_M1]:.6f}")
print(f"  M2: V/E_gap = {V_coupling_M2/L1[i_min]:.8f}")
print(f"  NOTE: These are gap-edge 2-level couplings, not the full off-diagonal.")
print(f"  The 4-5x ratio from Session 21b is the coupling between DIFFERENT sectors")
print(f"  through the Kosmann-Lichnerowicz operator, not the avoided crossing width.")


# ============================================================
# 5. Constraint Gate ASSESSMENT
# ============================================================

print()
print("=" * 70)
print("Constraint Gate ASSESSMENT (QA-2)")
print("=" * 70)
print()

if q_M2 is not None:
    q_abs = abs(q_M2)
    if q_abs > 2:
        verdict = f"COMPELLING: |q| = {q_abs:.2f} > 2 at M2 (strong Fano asymmetry)"
        bf = 5
        pp = "+2-4 pp"
    elif q_abs >= 1:
        verdict = f"INTERESTING: |q| = {q_abs:.2f} in [1,2] at M2 (mixed profile)"
        bf = 3
        pp = "+1-2 pp"
    else:
        verdict = f"NEUTRAL: |q| = {q_abs:.2f} < 1 at M2 (Lorentzian-dominated)"
        bf = 1
        pp = "0 pp"
    print(f"  M2 result: {verdict}")
    print(f"  BF = {bf}, shift: {pp}")
else:
    print("  M2: Fano fit failed, cannot assess.")

if q_M1_fit is not None:
    q_abs_M1 = abs(q_M1_fit)
    print(f"  M1 result: |q| = {q_abs_M1:.2f} (coarse grid, lower confidence)")

print()
print("Done.")
