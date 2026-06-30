#!/usr/bin/env python3
"""
S56 W1-4: MU-JOSEPHSON-56 — Chemical Potential Shift from Inter-Cell Coupling

The S34 mu=0 theorem requires particle-hole (PH) symmetry of the single-cell
Dirac spectrum. Josephson coupling broadens each level into a BAND across the
32-cell fabric. If the band structure breaks PH symmetry, an effective mu_eff != 0
is generated, potentially reopening the S_f non-monotonicity channel (SF-SIGN-55).

Method:
1. Load the 32x32 TB Hamiltonian H(tau) from s54_tb_hamiltonian.npz
2. At each tau, diagonalize H(tau) to get 32 eigenvalues
3. Compute mu_half = (E[15] + E[16]) / 2 at half-filling (16 particles)
4. Compute mu_PH = (E_max + E_min) / 2 (spectral midpoint)
5. mu_eff = mu_half - mu_PH measures PH asymmetry
6. Compute cumulative PH asymmetry A_PH

Gate: MU-SHIFT-56
  PASS: |mu_eff| > 0.1 M_KK at any tau in [0.10, 0.30]
  FAIL: |mu_eff| < 0.01 M_KK everywhere

Author: Spectral-Geometer
Session: S56, Wave 1, Task 4
"""

import sys
import os
sys.path.insert(0, 'computations')
from canonical_constants import *
import numpy as np
import matplotlib.pyplot as plt

# ============================================================================
# 1. Load TB Hamiltonian data
# ============================================================================
data = np.load('computations/session-54/s54_tb_hamiltonian.npz', allow_pickle=True)

tau_values = data['tau_values']       # (50,)
eigenvalues = data['eigenvalues']     # (50, 32)
hamiltonians = data['hamiltonians']   # (50, 32, 32)
bandwidths = data['bandwidths']       # (50,)
N_cells = int(data['N_cells'])        # 32
J_C2_tau = data['J_C2_tau']           # (50,)
cell_casimirs = data['cell_casimirs'] # (32,)
cell_dims = data['cell_dims']         # (32,)

n_tau = len(tau_values)
N = N_cells  # 32

print(f"Loaded: {n_tau} tau values, {N} cells")
print(f"Eigenvalue shape: {eigenvalues.shape}")
print(f"tau range: [{tau_values[0]:.4f}, {tau_values[-1]:.4f}]")

# ============================================================================
# 2. Verify eigenvalues by re-diagonalizing (cross-check)
# ============================================================================
idx_check = 25  # middle tau
H_check = hamiltonians[idx_check]
eigs_check = np.linalg.eigvalsh(H_check)
eigs_stored = eigenvalues[idx_check]
max_diff = np.max(np.abs(np.sort(eigs_check) - np.sort(eigs_stored)))
print(f"\nCross-check at tau={tau_values[idx_check]:.4f}: max |E_recomputed - E_stored| = {max_diff:.2e}")
assert max_diff < 1e-10, f"Eigenvalue cross-check FAILED: {max_diff}"

# ============================================================================
# 3. Compute chemical potential quantities at each tau
# ============================================================================

# Arrays to store results
mu_half = np.zeros(n_tau)       # Chemical potential at half-filling
mu_PH = np.zeros(n_tau)         # PH-symmetric midpoint
mu_eff = np.zeros(n_tau)        # Effective PH-breaking shift
A_PH = np.zeros(n_tau)          # PH asymmetry measure
E_min_arr = np.zeros(n_tau)     # Lowest eigenvalue
E_max_arr = np.zeros(n_tau)     # Highest eigenvalue
BW = np.zeros(n_tau)            # Bandwidth
gap_half = np.zeros(n_tau)      # Gap at half-filling E[16] - E[15]

# Detailed PH violation per eigenvalue pair
PH_violation = np.zeros((n_tau, N//2))  # |E_k + E_{N-1-k} - 2*mu_PH|

for i in range(n_tau):
    E = np.sort(eigenvalues[i])  # sorted ascending

    E_min_arr[i] = E[0]
    E_max_arr[i] = E[-1]
    BW[i] = E[-1] - E[0]

    # Half-filling: 16 particles fill levels 0..15
    # Chemical potential at half-filling = midpoint of Fermi gap
    mu_half[i] = (E[15] + E[16]) / 2.0

    # PH-symmetric midpoint
    mu_PH[i] = (E[-1] + E[0]) / 2.0

    # Effective chemical potential shift
    mu_eff[i] = mu_half[i] - mu_PH[i]

    # Gap at half-filling
    gap_half[i] = E[16] - E[15]

    # PH asymmetry measure: average violation of E_k + E_{N-1-k} = 2*mu_PH
    for k in range(N//2):
        PH_violation[i, k] = abs(E[k] + E[N-1-k] - 2*mu_PH[i])

    A_PH[i] = np.sum(PH_violation[i]) / (2.0 * BW[i]) if BW[i] > 0 else 0.0

# ============================================================================
# 4. Additional measure: Hermitian PH symmetry check
# ============================================================================
# A PH-symmetric Hamiltonian satisfies C H C^{-1} = -H + const
# For the TB Hamiltonian, check if the spectrum is symmetric about mu_PH
# by computing the spectral skewness

spectral_skewness = np.zeros(n_tau)
spectral_asymmetry_max = np.zeros(n_tau)

for i in range(n_tau):
    E = np.sort(eigenvalues[i])
    E_centered = E - mu_PH[i]

    # Skewness of centered spectrum
    sigma = np.std(E_centered)
    if sigma > 0:
        spectral_skewness[i] = np.mean(E_centered**3) / sigma**3

    # Maximum asymmetry in paired eigenvalues
    asym = np.zeros(N//2)
    for k in range(N//2):
        asym[k] = abs(E_centered[k] + E_centered[N-1-k])
    spectral_asymmetry_max[i] = np.max(asym)

# ============================================================================
# 5. Focus on gate window [0.10, 0.30]
# ============================================================================
mask_gate = (tau_values >= 0.10) & (tau_values <= 0.30)
tau_gate = tau_values[mask_gate]
mu_eff_gate = mu_eff[mask_gate]
A_PH_gate = A_PH[mask_gate]

max_mu_eff_gate = np.max(np.abs(mu_eff_gate))
max_A_PH_gate = np.max(A_PH_gate)

# Gate evaluation (in M_KK units — eigenvalues are already in M_KK units)
# The eigenvalues from TB Hamiltonian are dimensionless ratios of M_KK
PASS_threshold = 0.1   # |mu_eff| > 0.1 M_KK  # (local)
FAIL_threshold = 0.01  # |mu_eff| < 0.01 M_KK everywhere  # (local)

if max_mu_eff_gate > PASS_threshold:
    gate_verdict = "PASS"
elif max_mu_eff_gate < FAIL_threshold:
    gate_verdict = "FAIL"
else:
    gate_verdict = "INFO"

# ============================================================================
# 6. Ratio mu_eff / bandwidth for physical interpretation
# ============================================================================
mu_eff_over_BW = np.zeros(n_tau)
for i in range(n_tau):
    if BW[i] > 0:
        mu_eff_over_BW[i] = mu_eff[i] / BW[i]

# ============================================================================
# 7. Check: is PH violation from graph topology or from Casimir disorder?
# ============================================================================
# The cells have different Casimirs (on-site energies).
# Check if the Hamiltonian is bipartite (which would enforce PH symmetry)
adj = data['adjacency']  # 32x32
# Bipartite check via eigenvalues of adjacency
adj_eigs = np.linalg.eigvalsh(adj.astype(float))
adj_eigs_sorted = np.sort(adj_eigs)
# Bipartite graph has spectrum symmetric about 0
adj_skewness = np.mean(adj_eigs_sorted**3) / (np.std(adj_eigs_sorted)**3 + 1e-30)

# On-site energies (Casimirs) break PH if non-uniform
casimir_std = np.std(cell_casimirs)
casimir_mean = np.mean(cell_casimirs)

print(f"\n{'='*70}")
print(f"GRAPH TOPOLOGY ANALYSIS")
print(f"{'='*70}")
print(f"Adjacency eigenvalue skewness: {adj_skewness:.6f}")
print(f"  (0 = bipartite/PH-symmetric graph)")
print(f"Casimir disorder: mean={casimir_mean:.4f}, std={casimir_std:.4f}")
print(f"  std/mean = {casimir_std/casimir_mean:.4f}" if casimir_mean > 0 else "")

# ============================================================================
# 8. Print results table
# ============================================================================
print(f"\n{'='*70}")
print(f"MU-JOSEPHSON-56: Chemical Potential Shift Results")
print(f"{'='*70}")
print(f"\n{'tau':>8s} {'mu_half':>10s} {'mu_PH':>10s} {'mu_eff':>10s} {'|mu_eff|/BW':>12s} {'A_PH':>10s} {'gap_half':>10s} {'BW':>10s}")
print("-" * 82)

for i in range(n_tau):
    marker = " *" if mask_gate[i] else ""
    print(f"{tau_values[i]:8.4f} {mu_half[i]:10.6f} {mu_PH[i]:10.6f} {mu_eff[i]:10.6f} "
          f"{abs(mu_eff_over_BW[i]):12.8f} {A_PH[i]:10.6f} {gap_half[i]:10.6f} {BW[i]:10.4f}{marker}")

print(f"\n{'='*70}")
print(f"GATE WINDOW [0.10, 0.30]")
print(f"{'='*70}")
print(f"max |mu_eff| in gate window: {max_mu_eff_gate:.8f} M_KK")
print(f"max A_PH in gate window:     {max_A_PH_gate:.8f}")
print(f"PASS threshold:              {PASS_threshold:.2f} M_KK")
print(f"FAIL threshold:              {FAIL_threshold:.2f} M_KK")
print(f"\nGATE VERDICT: MU-SHIFT-56 = {gate_verdict}")

# Fold region details
fold_idx = np.argmin(np.abs(tau_values - tau_fold))
print(f"\nAt fold (tau={tau_values[fold_idx]:.4f}):")
print(f"  mu_half  = {mu_half[fold_idx]:.8f}")
print(f"  mu_PH    = {mu_PH[fold_idx]:.8f}")
print(f"  mu_eff   = {mu_eff[fold_idx]:.8f}")
print(f"  |mu_eff|/BW = {abs(mu_eff_over_BW[fold_idx]):.8f}")
print(f"  A_PH     = {A_PH[fold_idx]:.8f}")
print(f"  gap_half = {gap_half[fold_idx]:.6f}")
print(f"  BW       = {BW[fold_idx]:.6f}")
print(f"  spectral skewness = {spectral_skewness[fold_idx]:.8f}")
print(f"  max spectral asymmetry = {spectral_asymmetry_max[fold_idx]:.8f}")

# Full-range statistics
print(f"\nFull range statistics:")
print(f"  max |mu_eff| overall:    {np.max(np.abs(mu_eff)):.8f} M_KK at tau={tau_values[np.argmax(np.abs(mu_eff))]:.4f}")
print(f"  max A_PH overall:        {np.max(A_PH):.8f} at tau={tau_values[np.argmax(A_PH)]:.4f}")
print(f"  max |skewness| overall:  {np.max(np.abs(spectral_skewness)):.8f} at tau={tau_values[np.argmax(np.abs(spectral_skewness))]:.4f}")

# ============================================================================
# 9. Detailed eigenvalue pair analysis at fold
# ============================================================================
print(f"\n{'='*70}")
print(f"EIGENVALUE PAIR ANALYSIS AT FOLD (tau={tau_values[fold_idx]:.4f})")
print(f"{'='*70}")
E_fold = np.sort(eigenvalues[fold_idx])
print(f"{'k':>3s} {'E_k':>10s} {'E_{31-k}':>10s} {'E_k+E_{31-k}':>12s} {'2*mu_PH':>10s} {'violation':>10s}")
print("-" * 58)
for k in range(N//2):
    Ek = E_fold[k]
    Em = E_fold[N-1-k]
    violation = abs(Ek + Em - 2*mu_PH[fold_idx])
    print(f"{k:3d} {Ek:10.6f} {Em:10.6f} {Ek+Em:12.6f} {2*mu_PH[fold_idx]:10.6f} {violation:10.6f}")

# ============================================================================
# 10. Physical interpretation: relation to SF-SIGN-55
# ============================================================================
print(f"\n{'='*70}")
print(f"PHYSICAL INTERPRETATION")
print(f"{'='*70}")

# The S34 mu=0 theorem applies to single-cell BCS.
# For the fabric, mu_eff measures how far the fabric half-filling deviates
# from the PH-symmetric point.
print(f"""
S34 mu=0 theorem: Single-cell Dirac spectrum is PH-symmetric => mu=0 forced.
SF-SIGN-55 PASS: dS_f/dtau > 0 at mu=median (half-filling), BUT mu=0 forced.
TRUNC-RATIO-55: At mu=0, S_f monotonically decreasing (strengthens with truncation).

MU-JOSEPHSON-56 tests: does inter-cell coupling generate mu_eff != 0?
  max |mu_eff| = {max_mu_eff_gate:.8f} M_KK in gate window [0.10, 0.30]
  This is {'ABOVE' if max_mu_eff_gate > PASS_threshold else 'BELOW'} the PASS threshold of {PASS_threshold} M_KK.
  This is {'ABOVE' if max_mu_eff_gate > FAIL_threshold else 'BELOW'} the FAIL threshold of {FAIL_threshold} M_KK.
""")

if gate_verdict == "FAIL":
    print("CONCLUSION: The fabric TB Hamiltonian preserves PH symmetry to high precision.")
    print("mu_eff ~ 0 even with inter-cell coupling. The S34 mu=0 theorem extends to the fabric.")
    print("The SF-SIGN-55 non-monotonicity at mu=median remains unphysical.")
    print("The S_f non-monotonicity channel is CLOSED at the fabric level.")
elif gate_verdict == "PASS":
    print("CONCLUSION: Inter-cell coupling generates significant PH asymmetry!")
    print(f"mu_eff up to {max_mu_eff_gate:.4f} M_KK in the gate window.")
    print("The S34 mu=0 theorem does NOT extend to the fabric.")
    print("The SF-SIGN-55 non-monotonicity at finite mu becomes physical.")
    print("The S_f non-monotonicity channel is REOPENED.")
else:
    print(f"CONCLUSION: Intermediate regime. |mu_eff| = {max_mu_eff_gate:.6f} M_KK.")
    print("PH symmetry is weakly broken. Gate is INFO — downstream test decisive.")

# ============================================================================
# 11. Save data
# ============================================================================
np.savez('computations/session-56/s56_mu_josephson.npz',
    tau_values=tau_values,
    mu_half=mu_half,
    mu_PH=mu_PH,
    mu_eff=mu_eff,
    mu_eff_over_BW=mu_eff_over_BW,
    A_PH=A_PH,
    gap_half=gap_half,
    BW=BW,
    spectral_skewness=spectral_skewness,
    spectral_asymmetry_max=spectral_asymmetry_max,
    PH_violation=PH_violation,
    E_min=E_min_arr,
    E_max=E_max_arr,
    adj_skewness=np.array([adj_skewness]),
    casimir_mean=np.array([casimir_mean]),
    casimir_std=np.array([casimir_std]),
    # Gate metadata
    gate_name=np.array(['MU-SHIFT-56']),
    gate_verdict=np.array([gate_verdict]),
    gate_detail=np.array([f'max |mu_eff|={max_mu_eff_gate:.8f} in [0.10,0.30]. '
                          f'PASS>{PASS_threshold}, FAIL<{FAIL_threshold}. '
                          f'A_PH_max={max_A_PH_gate:.8f}. adj_skew={adj_skewness:.4f}']),
    PASS_threshold=np.array([PASS_threshold]),
    FAIL_threshold=np.array([FAIL_threshold]),
)
print(f"\nData saved to computations/session-56/s56_mu_josephson.npz")

# ============================================================================
# 12. Plot
# ============================================================================
fig, axes = plt.subplots(2, 3, figsize=(16, 10))
fig.suptitle('MU-JOSEPHSON-56: Chemical Potential Shift from Inter-Cell Coupling',
             fontsize=14, fontweight='bold')

# Panel 1: mu_eff vs tau
ax = axes[0, 0]
ax.plot(tau_values, mu_eff, 'b-', linewidth=2, label=r'$\mu_{\rm eff}$')
ax.axhline(y=PASS_threshold, color='g', linestyle='--', alpha=0.5, label=f'PASS threshold ({PASS_threshold})')
ax.axhline(y=-PASS_threshold, color='g', linestyle='--', alpha=0.5)
ax.axhline(y=FAIL_threshold, color='r', linestyle=':', alpha=0.5, label=f'FAIL threshold ({FAIL_threshold})')
ax.axhline(y=-FAIL_threshold, color='r', linestyle=':', alpha=0.5)
ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
ax.axvline(x=tau_fold, color='orange', linestyle='--', alpha=0.5, label=f'fold ({tau_fold:.3f})')
ax.axvspan(0.10, 0.30, alpha=0.1, color='yellow', label='gate window')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$\mu_{\rm eff}$ ($M_{\rm KK}$ units)')
ax.set_title(r'Effective chemical potential shift')
ax.legend(fontsize=7, loc='best')
ax.grid(True, alpha=0.3)

# Panel 2: |mu_eff| / BW ratio
ax = axes[0, 1]
ax.plot(tau_values, np.abs(mu_eff_over_BW), 'r-', linewidth=2)
ax.axvline(x=tau_fold, color='orange', linestyle='--', alpha=0.5, label=f'fold')
ax.axvspan(0.10, 0.30, alpha=0.1, color='yellow')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$|\mu_{\rm eff}| / \mathrm{BW}$')
ax.set_title(r'PH asymmetry relative to bandwidth')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 3: A_PH (cumulative asymmetry)
ax = axes[0, 2]
ax.plot(tau_values, A_PH, 'g-', linewidth=2)
ax.axvline(x=tau_fold, color='orange', linestyle='--', alpha=0.5, label=f'fold')
ax.axvspan(0.10, 0.30, alpha=0.1, color='yellow')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$A_{\rm PH}$')
ax.set_title(r'Cumulative PH asymmetry')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 4: Spectral skewness
ax = axes[1, 0]
ax.plot(tau_values, spectral_skewness, 'm-', linewidth=2)
ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
ax.axvline(x=tau_fold, color='orange', linestyle='--', alpha=0.5, label=f'fold')
ax.axvspan(0.10, 0.30, alpha=0.1, color='yellow')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel('Spectral skewness')
ax.set_title(r'Third moment asymmetry')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 5: Eigenvalue pair violations at fold
ax = axes[1, 1]
ax.bar(range(N//2), PH_violation[fold_idx], color='steelblue', alpha=0.7)
ax.set_xlabel('Pair index k')
ax.set_ylabel(r'$|E_k + E_{31-k} - 2\mu_{\rm PH}|$')
ax.set_title(f'PH violation per pair at fold (tau={tau_values[fold_idx]:.3f})')
ax.grid(True, alpha=0.3, axis='y')

# Panel 6: mu_half, mu_PH, and band edges vs tau
ax = axes[1, 2]
ax.fill_between(tau_values, E_min_arr, E_max_arr, alpha=0.15, color='blue', label='band')
ax.plot(tau_values, mu_half, 'r-', linewidth=2, label=r'$\mu_{\rm half}$')
ax.plot(tau_values, mu_PH, 'b--', linewidth=2, label=r'$\mu_{\rm PH}$')
ax.axvline(x=tau_fold, color='orange', linestyle='--', alpha=0.5, label=f'fold')
ax.axvspan(0.10, 0.30, alpha=0.1, color='yellow')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'Energy ($M_{\rm KK}$ units)')
ax.set_title(r'Band edges and chemical potentials')
ax.legend(fontsize=7, loc='best')
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('computations/session-56/s56_mu_josephson.png', dpi=150, bbox_inches='tight')
print(f"Plot saved to computations/session-56/s56_mu_josephson.png")
plt.close()

print(f"\n{'='*70}")
print(f"FINAL GATE VERDICT: MU-SHIFT-56 = {gate_verdict}")
print(f"max |mu_eff| in [0.10, 0.30] = {max_mu_eff_gate:.8f} M_KK")
print(f"{'='*70}")
