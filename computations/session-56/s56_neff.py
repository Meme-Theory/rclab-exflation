#!/usr/bin/env python3
"""
s56_neff.py — Effective Mode Count in Z_fabric vs Z_cell^N
============================================================

Session 56, W0-2 (NEFF-56)

Physics:
  In a superfluid Josephson array on the 32-cell tessellation, phase coherence
  rigidifies the global phase degree of freedom.  The 31 Bogoliubov-Anderson (BA)
  phonon modes replace 31 independent single-cell phase modes.  This computation
  quantifies the thermodynamic effective mode count N_eff and compares to the
  naive independent-cell prediction of 32 * 8 = 256 (or 32 * 31 = 992 for the
  continuum).

  The Landau approach: identify the order parameter (superfluid phase phi_i on
  each cell), write the most general free energy consistent with U(1) symmetry
  and the graph topology, then derive the partition function from the normal
  modes of the Gaussian fluctuation operator (the graph Laplacian dressed by
  E_J and E_c).

Method:
  1. Compute BA phonon frequencies omega_n(tau) = sqrt(E_c * E_J * lambda_n)
  2. Compute single-cell fermionic entropy S_cell from 8 BCS-active modes
  3. Compute BA phonon entropy S_BA from 31 bosonic modes
  4. N_eff = S_BA / (S_independent / 256)

Gate: NEFF-56 — INFO: N_eff(tau). If N_eff < 100 at fold, "mode count wins" invalidated.

Author: Landau-Condensed-Matter-Theorist (opus)
"""

import sys
import os
import numpy as np

sys.path.insert(0, 'computations')
from canonical_constants import (
    tau_fold, Delta_0_OES, N_cells, PI
)

# =============================================================================
#  Load data
# =============================================================================

data_tb = np.load('computations/session-54/s54_tb_hamiltonian.npz')
data_sf = np.load('computations/session-54/s54_scale_factor.npz')

tau_vals = data_tb['tau_values']       # (50,)
eigenvalues = data_tb['eigenvalues']   # (50, 32)
J_C2_tau = data_tb['J_C2_tau']         # (50,)

tau_sf = data_sf['tau']                # (10,)
H_sf = data_sf['H']                   # (10,)

N = int(data_tb['N_cells'])            # 32
N_modes_per_cell = 8                   # BCS-active modes
Delta = Delta_0_OES                    # 0.4643 M_KK (canonical gap)

print(f"Loaded: {len(tau_vals)} tau values, N_cells = {N}")
print(f"Delta (OES) = {Delta:.4f} M_KK")

# =============================================================================
#  Interpolate H(tau) -> T_GH(tau)
# =============================================================================

# H is given at 10 tau points; interpolate to 50
H_interp = np.interp(tau_vals, tau_sf, H_sf)
T_GH = H_interp / (2.0 * PI)  # Gibbons-Hawking temperature

print(f"\nT_GH range: [{T_GH.min():.4f}, {T_GH.max():.4f}] M_KK")
print(f"T_GH at tau=0: {T_GH[0]:.4f}, T_GH at tau_fold~0.19: {T_GH[np.argmin(np.abs(tau_vals - tau_fold))]:.4f}")

# =============================================================================
#  At each tau: compute E_J, E_c, BA phonon spectrum, entropies
# =============================================================================

# Storage
E_c_arr = np.zeros(len(tau_vals))
E_J_arr = np.zeros(len(tau_vals))
F_anom_arr = np.zeros(len(tau_vals))
S_cell_arr = np.zeros(len(tau_vals))
S_indep_arr = np.zeros(len(tau_vals))
S_BA_arr = np.zeros(len(tau_vals))
N_eff_arr = np.zeros(len(tau_vals))
omega_min_arr = np.zeros(len(tau_vals))
omega_max_arr = np.zeros(len(tau_vals))
Z_ratio_arr = np.zeros(len(tau_vals))

# Graph Laplacian eigenvalues: lambda_n = E_n / J_C2 (from tight-binding)
# The zero eigenvalue corresponds to the uniform mode (global phase).
# We need the 31 nonzero eigenvalues.

for i, tau in enumerate(tau_vals):
    evals = eigenvalues[i]    # (32,) sorted ascending
    J_C2 = J_C2_tau[i]
    T = T_GH[i]
    beta = 1.0 / T if T > 1e-15 else 1e15

    # --- Charging energy: half the gap at Fermi surface ---
    # N=32 sites, half-filling: Fermi level between eigenvalue[15] and eigenvalue[16]
    E_c = (evals[16] - evals[15]) / 2.0
    E_c_arr[i] = E_c

    # --- Chemical potential (midpoint of Fermi gap) ---
    mu = (evals[15] + evals[16]) / 2.0

    # --- BCS anomalous density ---
    # F_anomalous = Sum_k Delta / (2 * E_qp_k^2)
    # where E_qp_k = sqrt((E_k - mu)^2 + Delta^2)
    xi_k = evals - mu
    E_qp_k = np.sqrt(xi_k**2 + Delta**2)
    uv_k = Delta / (2.0 * E_qp_k)
    F_anom = np.sum(Delta / (2.0 * E_qp_k**2))
    F_anom_arr[i] = F_anom

    # --- Josephson energy ---
    E_J = J_C2**2 * F_anom
    E_J_arr[i] = E_J

    # --- Graph Laplacian eigenvalues ---
    lambda_n = evals / J_C2  # normalized eigenvalues
    # The smallest eigenvalue should be ~0 (global mode)
    # Sort to be safe and take the 31 nonzero ones
    lambda_sorted = np.sort(lambda_n)
    lambda_nonzero = lambda_sorted[1:]  # skip the zero mode

    # --- BA phonon frequencies ---
    # omega_n = sqrt(E_c * E_J * lambda_n)
    # This is the Josephson plasma frequency formula for the graph
    omega_n = np.sqrt(E_c * E_J * lambda_nonzero)
    omega_min_arr[i] = omega_n[0]
    omega_max_arr[i] = omega_n[-1]

    # --- BA phonon entropy (bosonic) ---
    # S_bose = Sum_n [beta*omega_n/(exp(beta*omega_n)-1) - ln(1-exp(-beta*omega_n))]
    x_n = beta * omega_n
    # Avoid overflow: for large x, S_bose per mode ~ x*exp(-x)
    S_BA = 0.0  # (local)
    for x in x_n:
        if x > 500:
            S_BA += x * np.exp(-x)  # exponentially suppressed
        elif x < 1e-10:
            S_BA += 1.0 - np.log(x + 1e-300)  # classical limit
        else:
            S_BA += x / (np.exp(x) - 1.0) - np.log(1.0 - np.exp(-x))
    S_BA_arr[i] = S_BA

    # --- Single-cell fermionic entropy ---
    # Z_cell = Prod_{k=1}^{8} (1 + exp(-E_qp_k / T))
    # Use the 8 lowest quasiparticle energies as BCS-active modes
    E_qp_sorted = np.sort(E_qp_k)
    E_qp_8 = E_qp_sorted[:N_modes_per_cell]

    # Fermionic entropy: S = Sum_k [-f*ln(f) - (1-f)*ln(1-f)]
    # where f_k = 1/(1+exp(E_k/T))
    S_cell = 0.0  # (local)
    for E in E_qp_8:
        bE = E / T
        if bE > 500:
            S_cell += bE * np.exp(-bE)  # exponentially suppressed
        elif bE < 1e-10:
            S_cell += np.log(2.0)  # high-T limit: ln(2) per mode
        else:
            f = 1.0 / (1.0 + np.exp(bE))
            # Avoid log(0)
            if f > 1e-300 and (1-f) > 1e-300:
                S_cell += -f * np.log(f) - (1-f) * np.log(1-f)
    S_cell_arr[i] = S_cell

    # --- Independent cell estimate ---
    S_indep = N * S_cell  # 32 independent cells
    S_indep_arr[i] = S_indep

    # --- Effective mode count ---
    # N_eff = S_BA / (S_indep / (N * N_modes_per_cell))
    # = S_BA / (S_cell / N_modes_per_cell)
    # This is: how many "single-mode-equivalent" entropies does the BA sector contain
    S_per_mode = S_indep / (N * N_modes_per_cell)  # entropy per independent mode
    if S_per_mode > 1e-15:
        N_eff = S_BA / S_per_mode
    else:
        N_eff = 0.0  # (local)
    N_eff_arr[i] = N_eff

    # --- Partition function ratio (phase sector) ---
    # Z_fabric_phase = Prod_{n=1}^{31} [2 sinh(omega_n/(2T))]^{-1}
    # Z_cell_phase = [2 sinh(omega_uniform/(2T))]^{-32}
    # where omega_uniform = sqrt(E_c * E_J * mean(lambda_nonzero)) -- mean-field single-cell freq
    # Ratio = exp(ln Z_fabric - ln Z_cell)
    omega_uniform = np.sqrt(E_c * E_J * np.mean(lambda_nonzero))
    ln_Z_fabric = -np.sum(np.log(2.0 * np.sinh(np.clip(omega_n / (2.0 * T), 1e-10, 500))))
    ln_Z_cell = -N * np.log(2.0 * np.sinh(np.clip(omega_uniform / (2.0 * T), 1e-10, 500)))
    Z_ratio_arr[i] = np.exp(ln_Z_fabric - ln_Z_cell)

# =============================================================================
#  Find fold index and report key results
# =============================================================================

idx_fold = np.argmin(np.abs(tau_vals - tau_fold))
print(f"\n{'='*70}")
print(f"  NEFF-56 RESULTS")
print(f"{'='*70}")
print(f"\nFold index: {idx_fold}, tau_fold = {tau_vals[idx_fold]:.4f}")
print(f"\nAt the fold (tau = {tau_vals[idx_fold]:.4f}):")
print(f"  T_GH       = {T_GH[idx_fold]:.6f} M_KK")
print(f"  E_c        = {E_c_arr[idx_fold]:.6f} M_KK")
print(f"  E_J        = {E_J_arr[idx_fold]:.6f} M_KK")
print(f"  F_anom     = {F_anom_arr[idx_fold]:.6f}")
print(f"  E_J/E_c    = {E_J_arr[idx_fold]/E_c_arr[idx_fold]:.2f}")
print(f"  omega_min  = {omega_min_arr[idx_fold]:.6f} M_KK")
print(f"  omega_max  = {omega_max_arr[idx_fold]:.6f} M_KK")
print(f"  S_BA       = {S_BA_arr[idx_fold]:.6f}")
print(f"  S_cell     = {S_cell_arr[idx_fold]:.6f}")
print(f"  S_indep    = {S_indep_arr[idx_fold]:.6f}")
print(f"  S_per_mode = {S_indep_arr[idx_fold]/(N*N_modes_per_cell):.6f}")
print(f"  N_eff      = {N_eff_arr[idx_fold]:.2f}")
print(f"  Z_ratio    = {Z_ratio_arr[idx_fold]:.6e}")

print(f"\nN_eff range over all tau: [{N_eff_arr.min():.2f}, {N_eff_arr.max():.2f}]")
print(f"N_eff at tau=0: {N_eff_arr[0]:.2f}")
print(f"N_eff at fold:  {N_eff_arr[idx_fold]:.2f}")
print(f"N_eff at tau=0.5: {N_eff_arr[-1]:.2f}")

# Gate verdict
if N_eff_arr[idx_fold] < 100:
    verdict = "N_eff < 100 at fold: 'mode count wins' INVALIDATED for Z_fabric"
    gate_status = "FLAGGED"
else:
    verdict = f"N_eff = {N_eff_arr[idx_fold]:.1f} >= 100 at fold: 'mode count wins' not invalidated"
    gate_status = "INFO"

print(f"\n{'='*70}")
print(f"  GATE NEFF-56: {gate_status}")
print(f"  {verdict}")
print(f"{'='*70}")

# --- Detailed table ---
print(f"\n{'tau':>8} {'T_GH':>10} {'E_c':>10} {'E_J':>10} {'S_BA':>10} {'S_indep':>10} {'N_eff':>10} {'Z_ratio':>12}")
print("-" * 82)
for j in range(0, len(tau_vals), 5):
    print(f"{tau_vals[j]:8.4f} {T_GH[j]:10.6f} {E_c_arr[j]:10.6f} {E_J_arr[j]:10.4f} "
          f"{S_BA_arr[j]:10.6f} {S_indep_arr[j]:10.4f} {N_eff_arr[j]:10.2f} {Z_ratio_arr[j]:12.4e}")

# =============================================================================
#  Additional diagnostics: temperature ratios
# =============================================================================

print(f"\n{'='*70}")
print(f"  TEMPERATURE RATIOS")
print(f"{'='*70}")
print(f"\nCompare omega_n to T_GH (Boltzmann suppression diagnostic):")
print(f"  At fold: omega_min/T_GH = {omega_min_arr[idx_fold]/T_GH[idx_fold]:.4f}")
print(f"  At fold: omega_max/T_GH = {omega_max_arr[idx_fold]/T_GH[idx_fold]:.4f}")

# If omega >> T, phonon modes are frozen (S_BA -> 0, N_eff -> 0)
# If omega << T, phonon modes are classical (S_BA ~ 31, N_eff ~ 31)
# If omega ~ T, intermediate regime
regime_fold = omega_min_arr[idx_fold] / T_GH[idx_fold]
if regime_fold > 10:
    regime_str = "FROZEN (omega >> T_GH): BA modes exponentially suppressed"
elif regime_fold < 0.1:
    regime_str = "CLASSICAL (omega << T_GH): BA modes carry full entropy"
else:
    regime_str = "INTERMEDIATE (omega ~ T_GH): partial occupation"
print(f"  Regime at fold: {regime_str}")

# Phase stiffness diagnostic
print(f"\n  E_J/T_GH at fold = {E_J_arr[idx_fold]/T_GH[idx_fold]:.2f} (>> 1 = superfluid)")

# =============================================================================
#  Save results
# =============================================================================

np.savez('computations/session-56/s56_neff.npz',
         tau_values=tau_vals,
         T_GH=T_GH,
         E_c=E_c_arr,
         E_J=E_J_arr,
         F_anomalous=F_anom_arr,
         S_BA=S_BA_arr,
         S_cell=S_cell_arr,
         S_independent=S_indep_arr,
         N_eff=N_eff_arr,
         omega_min=omega_min_arr,
         omega_max=omega_max_arr,
         Z_ratio=Z_ratio_arr,
         idx_fold=idx_fold,
         gate_status=gate_status,
         verdict=verdict)

print(f"\nData saved: computations/session-56/s56_neff.npz")

# =============================================================================
#  Plot
# =============================================================================

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('NEFF-56: Effective Mode Count in Z_fabric vs Z_cell$^N$',
             fontsize=14, fontweight='bold')

# --- Panel (a): N_eff(tau) ---
ax = axes[0, 0]
ax.plot(tau_vals, N_eff_arr, 'b-', linewidth=2, label=r'$N_{\rm eff}(\tau)$')
ax.axhline(y=992, color='r', linestyle='--', alpha=0.7, label='992 (independent cells)')
ax.axhline(y=256, color='orange', linestyle='--', alpha=0.7, label='256 (8 modes $\\times$ 32)')
ax.axhline(y=100, color='green', linestyle=':', alpha=0.7, label='100 (gate threshold)')
ax.axhline(y=31, color='gray', linestyle=':', alpha=0.5, label='31 (BA modes)')
ax.axvline(x=tau_fold, color='k', linestyle=':', alpha=0.5, label=r'$\tau_{\rm fold}$')
ax.set_xlabel(r'$\tau$', fontsize=12)
ax.set_ylabel(r'$N_{\rm eff}$', fontsize=12)
ax.set_title(r'(a) Effective mode count $N_{\rm eff}(\tau)$', fontsize=12)
ax.legend(fontsize=8, loc='upper right')
ax.set_yscale('log')
ax.set_ylim(0.1, 2000)
ax.grid(True, alpha=0.3)

# --- Panel (b): BA phonon entropy vs independent cell entropy ---
ax = axes[0, 1]
ax.plot(tau_vals, S_BA_arr, 'b-', linewidth=2, label=r'$S_{\rm BA}$ (31 phonon modes)')
ax.plot(tau_vals, S_indep_arr, 'r-', linewidth=2, label=r'$S_{\rm indep}$ (32 indep. cells)')
ax.plot(tau_vals, S_cell_arr, 'g--', linewidth=1.5, label=r'$S_{\rm cell}$ (single cell)')
ax.axvline(x=tau_fold, color='k', linestyle=':', alpha=0.5)
ax.set_xlabel(r'$\tau$', fontsize=12)
ax.set_ylabel(r'Entropy (dimensionless)', fontsize=12)
ax.set_title(r'(b) Entropy comparison', fontsize=12)
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# --- Panel (c): BA phonon frequencies ---
ax = axes[1, 0]
# Plot omega_min and omega_max as envelope
ax.fill_between(tau_vals, omega_min_arr, omega_max_arr, alpha=0.3, color='blue',
                label='BA band')
ax.plot(tau_vals, omega_min_arr, 'b-', linewidth=1.5, label=r'$\omega_1$ (min)')
ax.plot(tau_vals, omega_max_arr, 'b--', linewidth=1.5, label=r'$\omega_{31}$ (max)')
ax.plot(tau_vals, T_GH, 'r-', linewidth=2, label=r'$T_{\rm GH}$')
ax.axvline(x=tau_fold, color='k', linestyle=':', alpha=0.5)
ax.set_xlabel(r'$\tau$', fontsize=12)
ax.set_ylabel(r'Energy (M$_{\rm KK}$)', fontsize=12)
ax.set_title(r'(c) BA phonon band vs $T_{\rm GH}$', fontsize=12)
ax.legend(fontsize=9)
ax.set_yscale('log')
ax.grid(True, alpha=0.3)

# --- Panel (d): Partition function ratio ---
ax = axes[1, 1]
ax.plot(tau_vals, Z_ratio_arr, 'b-', linewidth=2)
ax.axhline(y=1.0, color='k', linestyle=':', alpha=0.5)
ax.axvline(x=tau_fold, color='k', linestyle=':', alpha=0.5, label=r'$\tau_{\rm fold}$')
ax.set_xlabel(r'$\tau$', fontsize=12)
ax.set_ylabel(r'$Z_{\rm fabric,phase} / Z_{\rm cell,phase}$', fontsize=12)
ax.set_title(r'(d) Phase-sector partition function ratio', fontsize=12)
ax.legend(fontsize=9)
ax.set_yscale('log')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('computations/session-56/s56_neff.png', dpi=150, bbox_inches='tight')
print(f"Plot saved: computations/session-56/s56_neff.png")
print("\nDone.")
