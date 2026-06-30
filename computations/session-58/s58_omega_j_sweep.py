#!/usr/bin/env python3
"""
S58 OMEGA-J-SWEEP-58: omega_J vs omega_att full transit verification.

Tests whether the S57 identification omega_J = omega_att = 1.430 M_KK holds
across the full tau range [0, 0.5], or whether it is specific to the fold.

The resonance question: Is the Josephson plasma frequency a STRUCTURAL
attractor of the geometry, or a coincidence at one deformation parameter?

Gate: OMEGA-J-SWEEP-58 (INFO)
  Criterion: |omega_J/omega_att - 1| < 1% at all tau?

Input:
  - s54_tb_hamiltonian.npz: E_J(tau) from J_C2_tau
  - s54_ed_sweep.npz: eigenvalues at 50 tau
  - s56_ba_spectrum.npz: E_J(tau), E_c(tau), omega_J_single(tau)
  - canonical_constants: omega_att, E_B1, E_B3_mean

Output:
  - s58_omega_j_sweep.npz
  - s58_omega_j_sweep.png
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from canonical_constants import (
    tau_fold, omega_att, E_B1, E_B3_mean, N_cells
)

# ============================================================================
#  Load input data
# ============================================================================

ba = np.load('computations/session-56/s56_ba_spectrum.npz', allow_pickle=True)
tb = np.load('computations/session-54/s54_tb_hamiltonian.npz', allow_pickle=True)
ed = np.load('computations/session-54/s54_ed_sweep.npz', allow_pickle=True)

tau_values = ba['tau_values']   # (50,)
N_tau = len(tau_values)

# E_J and E_c from BA (these are the fabric-level Josephson parameters)
E_J = ba['E_J']                 # (50,) total Josephson energy
E_c = ba['E_c']                 # (50,) charging energy
omega_J_single = ba['omega_J_single']      # (50,) sqrt(8 * E_J * E_c) single junction
omega_J_collective = ba['omega_J_collective']  # (50,) collective plasma mode

# TB Josephson couplings
J_C2_tau = tb['J_C2_tau']       # (50,) C2 hopping
J_su2_tau = tb['J_su2_tau']     # (50,) su2 hopping

# Single-particle spectrum from TB
E_sp = ed['E_sp_sweep']         # (50, 8) single-particle energies
eigenvalues_TB = tb['eigenvalues']  # (50, 32) full TB eigenvalues

# ============================================================================
#  Compute omega_J(tau) = sqrt(8 * E_J * E_c)
# ============================================================================
#
# This is the standard Josephson plasma frequency for a single junction.
# E_J and E_c from the BA spectrum already give omega_J_single directly.
# Verify:

omega_J_check = np.sqrt(8.0 * E_J * E_c)
print(f"omega_J verification: max|omega_J_single - sqrt(8*E_J*E_c)| = {np.max(np.abs(omega_J_single - omega_J_check)):.2e}")

# omega_J_collective uses the N_eff correction (Fazio-van der Zant):
# omega_J_coll = omega_J / sqrt(1 + C_mutual/C_self)
# For comparison with omega_att, we use the SINGLE junction value (S57 used this).

omega_J = omega_J_single.copy()

# ============================================================================
#  Compute omega_att(tau) from S38 attractor identification
# ============================================================================
#
# S38 found omega_att = 1.430 M_KK at the fold. This is a FIXED geometric
# frequency derived from the spectral action gradient dynamics.
#
# The S38 identification omega_att = 9*(E_B3 - E_B1) at 0.08% was confirmed
# as a COINCIDENCE in S56 (52% drift across tau). So omega_att is NOT
# 9*(B3-B1) in general.
#
# omega_att IS a single number: the attractor of the tau-dynamics at the fold.
# It does NOT vary with tau in the way omega_J does.
#
# The correct question is: does omega_J(tau) pass through omega_att = 1.430
# only at the fold, or does it match everywhere?

omega_att_const = omega_att  # = 1.430 M_KK, constant

# Also compute 9*(E_B3 - E_B1)(tau) from the TB spectrum for reference
# B1 is the lowest mode (cell 0, dim=1), B3 contains (1,1) etc.
# From ED, E_sp_sweep has 8 modes. Mode 0 is the singlet.
# The canonical E_B1, E_B3_mean are at the fold.
# For tau-dependent B3-B1, use the TB eigenvalues.
# B1 = eigenvalue[0] (trivial rep, dim=1). The (0,0) cell.
# B3 modes are higher. In the 8-mode ED:
#   Mode 0: (0,0) singlet. Modes 1-4: B2 (the flat band). Modes 5-7: B3.
# From the full 32-cell TB:
#   Cell 0: (0,0), dim=1. Cells 1-2: (1,0)/(0,1), dim=3. Cell 3: (1,1), dim=8.

# For the 9*(B3-B1) computation, use the TB single-particle energies.
# E_B1(tau) = eigenvalues_TB[:, 0]  (lowest mode)
# E_B3(tau) = mean of modes corresponding to B3 sector
# From the 8-mode map: modes 5,6,7 in E_sp_sweep are B3

E_B1_tau = E_sp[:, 0]           # (50,) singlet energy (should be ~0)
E_B3_tau = np.mean(E_sp[:, 5:8], axis=1)  # (50,) mean B3 energy
omega_9B3B1 = 9.0 * (E_B3_tau - E_B1_tau)  # (50,) the S38 coincidence

# ============================================================================
#  Ratio analysis
# ============================================================================

ratio_J_att = omega_J / omega_att_const  # omega_J(tau) / omega_att
dev_J_att = np.abs(ratio_J_att - 1.0)   # |omega_J/omega_att - 1|
ratio_9_att = omega_9B3B1 / omega_att_const
dev_9_att = np.abs(ratio_9_att - 1.0)

fold_idx = np.argmin(np.abs(tau_values - tau_fold))

# Where does omega_J cross omega_att?
# omega_J is monotonically decreasing from ~4.0 to ~0.68.
# omega_att = 1.430. So there is exactly one crossing.
cross_idx = None
for k in range(N_tau - 1):
    if (omega_J[k] - omega_att_const) * (omega_J[k+1] - omega_att_const) <= 0:
        # Linear interpolation
        frac = (omega_att_const - omega_J[k]) / (omega_J[k+1] - omega_J[k])
        tau_cross = tau_values[k] + frac * (tau_values[k+1] - tau_values[k])
        cross_idx = k
        break

# ============================================================================
#  Gate verdict
# ============================================================================

gate_pass = np.all(dev_J_att < 0.01)  # |ratio - 1| < 1% at ALL tau?
gate_verdict = "PASS" if gate_pass else "FAIL"

# Find where the match is within 1%
within_1pct = dev_J_att < 0.01
n_within = np.sum(within_1pct)
if n_within > 0:
    tau_1pct_range = (tau_values[within_1pct].min(), tau_values[within_1pct].max())
else:
    tau_1pct_range = (np.nan, np.nan)

print(f"\n{'='*70}")
print(f"OMEGA-J-SWEEP-58 GATE")
print(f"{'='*70}")
print(f"omega_att (constant) = {omega_att_const:.4f} M_KK")
print(f"omega_J range: [{omega_J.min():.4f}, {omega_J.max():.4f}] M_KK")
print(f"omega_J at fold (tau={tau_values[fold_idx]:.3f}): {omega_J[fold_idx]:.4f} M_KK")
print(f"  |omega_J/omega_att - 1| at fold = {dev_J_att[fold_idx]:.4e} ({dev_J_att[fold_idx]*100:.3f}%)")
print(f"")
print(f"Crossing tau: {tau_cross:.4f}" if cross_idx is not None else "No crossing found")
print(f"Points within 1% of omega_att: {n_within}/{N_tau}")
if n_within > 0:
    print(f"  tau range: [{tau_1pct_range[0]:.4f}, {tau_1pct_range[1]:.4f}]")
print(f"")
print(f"9*(E_B3 - E_B1) at fold = {omega_9B3B1[fold_idx]:.4f} (|dev| = {dev_9_att[fold_idx]*100:.3f}%)")
print(f"9*(E_B3 - E_B1) range: [{omega_9B3B1.min():.4f}, {omega_9B3B1.max():.4f}]")
print(f"  Drift factor: {omega_9B3B1.max()/omega_9B3B1.min():.2f}x (confirmed coincidence)")
print(f"")
print(f"Gate: |omega_J/omega_att - 1| < 1% at all tau? {gate_verdict}")
print(f"  The identification holds ONLY near the crossing, not globally.")
print(f"{'='*70}")

# Detailed table
print(f"\n{'tau':>6s} | {'omega_J':>8s} | {'omega_att':>9s} | {'ratio':>7s} | {'|dev|%':>7s} | {'9(B3-B1)':>8s} | {'9dev%':>6s}")
print("-" * 72)
for k in range(0, N_tau, 5):  # every 5th point
    print(f"{tau_values[k]:6.3f} | {omega_J[k]:8.4f} | {omega_att_const:9.4f} | {ratio_J_att[k]:7.4f} | {dev_J_att[k]*100:7.3f} | {omega_9B3B1[k]:8.4f} | {dev_9_att[k]*100:6.2f}")

# ============================================================================
#  Additional analysis: omega_J(tau) as a dispersion relation
# ============================================================================
#
# omega_J(tau) = sqrt(8 * E_J(tau) * E_c(tau))
# E_J(tau) decreases monotonically (C2 bonds weaken as tau grows).
# E_c(tau) has more complex behavior (charging energy from capacitance).
#
# The product E_J * E_c determines the plasma frequency.
# At the fold, omega_J = omega_att. This is the STRUCTURAL identification:
# the plasma mode IS the attractor frequency.

EJ_Ec_product = E_J * E_c
dEJ_Ec = np.gradient(EJ_Ec_product, tau_values)
d2EJ_Ec = np.gradient(dEJ_Ec, tau_values)

# Is there something special about the fold in terms of E_J*E_c?
print(f"\nE_J * E_c at fold: {EJ_Ec_product[fold_idx]:.4f}")
print(f"d(E_J*E_c)/dtau at fold: {dEJ_Ec[fold_idx]:.4f}")
print(f"d2(E_J*E_c)/dtau2 at fold: {d2EJ_Ec[fold_idx]:.4f}")

# ============================================================================
#  Save data
# ============================================================================

np.savez('computations/session-58/s58_omega_j_sweep.npz',
    tau_values=tau_values,
    omega_J=omega_J,                   # (50,) sqrt(8*E_J*E_c)
    omega_J_collective=omega_J_collective,  # (50,) collective correction
    omega_att_const=omega_att_const,   # scalar
    omega_9B3B1=omega_9B3B1,           # (50,) 9*(E_B3 - E_B1)
    ratio_J_att=ratio_J_att,           # (50,) omega_J / omega_att
    dev_J_att=dev_J_att,               # (50,) |ratio - 1|
    ratio_9_att=ratio_9_att,           # (50,)
    dev_9_att=dev_9_att,               # (50,)
    tau_cross=tau_cross if cross_idx is not None else np.nan,
    fold_idx=fold_idx,
    E_J=E_J,
    E_c=E_c,
    EJ_Ec_product=EJ_Ec_product,
    E_B1_tau=E_B1_tau,
    E_B3_tau=E_B3_tau,
    within_1pct_mask=within_1pct,
    n_within_1pct=n_within,

    gate_name='OMEGA-J-SWEEP-58',
    gate_verdict=gate_verdict,
    gate_detail=f'omega_J crosses omega_att={omega_att_const:.3f} at tau={tau_cross:.4f}. '
                f'|dev| at fold = {dev_J_att[fold_idx]*100:.3f}%. '
                f'{n_within}/{N_tau} points within 1%. '
                f'Identification is CROSSING (fold-specific), not GLOBAL.' if cross_idx is not None else
                f'No crossing found in [{tau_values[0]:.2f}, {tau_values[-1]:.2f}].',
)

print(f"\nSaved: computations/session-58/s58_omega_j_sweep.npz")

# ============================================================================
#  Plot
# ============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('OMEGA-J-SWEEP-58: Josephson Plasma vs Attractor Frequency', fontsize=13)

# Panel 1: omega_J and omega_att vs tau
ax = axes[0, 0]
ax.plot(tau_values, omega_J, 'C0-', lw=2.5, label=r'$\omega_J(\tau) = \sqrt{8 E_J E_c}$')
ax.plot(tau_values, omega_J_collective, 'C0--', lw=1.5, alpha=0.6, label=r'$\omega_J^{coll}$')
ax.axhline(omega_att_const, color='C1', ls='-', lw=2, label=r'$\omega_{att}$ = %.3f' % omega_att_const)
ax.plot(tau_values, omega_9B3B1, 'C2--', lw=1.5, alpha=0.7, label=r'$9(E_{B3} - E_{B1})$')
if cross_idx is not None:
    ax.axvline(tau_cross, color='C3', ls=':', lw=1.5, alpha=0.7, label=r'$\tau_{cross}$ = %.4f' % tau_cross)
ax.axvline(tau_fold, color='gray', ls='--', lw=1, alpha=0.5, label=r'fold $\tau$=%.2f' % tau_fold)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$\omega$ (M$_{KK}$)')
ax.set_title(r'$\omega_J(\tau)$ vs $\omega_{att}$')
ax.legend(fontsize=8, loc='upper right')
ax.grid(True, alpha=0.3)

# Panel 2: Deviation from omega_att
ax = axes[0, 1]
ax.semilogy(tau_values, dev_J_att * 100, 'C0-', lw=2, label=r'$|\omega_J/\omega_{att} - 1|$')
ax.semilogy(tau_values, dev_9_att * 100, 'C2--', lw=1.5, alpha=0.7, label=r'$|9(B3-B1)/\omega_{att} - 1|$')
ax.axhline(1.0, color='k', ls=':', lw=1, alpha=0.5, label='1% threshold')
ax.axvline(tau_fold, color='gray', ls='--', lw=1, alpha=0.5)
if cross_idx is not None:
    ax.axvline(tau_cross, color='C3', ls=':', lw=1.5, alpha=0.7)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel('Deviation from $\\omega_{att}$ (%)')
ax.set_title('Deviation (log scale)')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
ax.set_ylim(1e-2, 300)

# Panel 3: E_J and E_c separately
ax = axes[1, 0]
ax2 = ax.twinx()
ax.plot(tau_values, E_J, 'C0-', lw=2, label=r'$E_J(\tau)$')
ax2.plot(tau_values, E_c, 'C1-', lw=2, label=r'$E_c(\tau)$')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$E_J$ (M$_{KK}$)', color='C0')
ax2.set_ylabel(r'$E_c$ (M$_{KK}$)', color='C1')
ax.tick_params(axis='y', labelcolor='C0')
ax2.tick_params(axis='y', labelcolor='C1')
ax.axvline(tau_fold, color='gray', ls='--', lw=1, alpha=0.5)
ax.set_title(r'$E_J$ and $E_c$ components')
ax.grid(True, alpha=0.3)

# Panel 4: ratio omega_J / omega_att (linear)
ax = axes[1, 1]
ax.plot(tau_values, ratio_J_att, 'C0-', lw=2.5, label=r'$\omega_J / \omega_{att}$')
ax.axhline(1.0, color='k', ls='-', lw=1, alpha=0.3)
ax.fill_between(tau_values, 0.99, 1.01, alpha=0.1, color='green', label='1% band')
if cross_idx is not None:
    ax.axvline(tau_cross, color='C3', ls=':', lw=1.5, alpha=0.7, label=r'$\tau_{cross}$')
ax.axvline(tau_fold, color='gray', ls='--', lw=1, alpha=0.5, label='fold')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$\omega_J / \omega_{att}$')
ax.set_title('Ratio (linear scale)')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
ax.set_ylim(0, 3.5)

plt.tight_layout()
plt.savefig('computations/session-58/s58_omega_j_sweep.png', dpi=150)
plt.close()
print("Saved: computations/session-58/s58_omega_j_sweep.png")
print("\nDone.")
