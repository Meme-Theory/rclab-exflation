#!/usr/bin/env python3
"""
Session 32a -- FLAT-1: B2-mediated effective interaction B1<->B3.

Compute the effective B1-B3 interaction mediated by virtual B2 excitations
using second-order perturbation theory in the singlet eigenvector basis.

Physics:
  V_eff(B1,B3) = sum_{k in B2} |<B1|dD/dtau|B2_k>|^2 * |<B2_k|dD/dtau|B3>|^2
                  / (E_B1 - E_B2_k)^2

  This measures the indirect coupling between the acoustic singlet (B1) and the
  optical triplet (B3) mediated by virtual excitations of the flat-band quartet (B2).
  If attractive (negative): extra collective instability reinforces RPA.
  If repulsive (positive) or zero: standard RPA sufficient.

  The off-diagonal matrix elements <m|dD/dtau|n> are extracted from the
  eigenvector evolution: since D(tau)|psi_n(tau)> = lambda_n(tau)|psi_n(tau)>,
  differentiating gives for m != n:
    <psi_m|dD/dtau|psi_n> = (dlambda_n/dtau * delta_{mn}) + (lambda_n - lambda_m) * <psi_m|dpsi_n/dtau>
  Therefore for m != n:
    <psi_m|dD/dtau|psi_n> = (lambda_n - lambda_m) * <psi_m|dpsi_n/dtau>

Input: tier0-computation/s23a_kosmann_singlet.npz, s32a_umklapp_vertex.npz
Output: tier0-computation/s32a_flat_b2_interaction.npz, .png
Gate: FL-32a (V_eff sign)

Author: phonon-exflation-sim agent, Session 32a
Date: 2026-03-02
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

# ============================================================
# 0. LOAD DATA
# ============================================================

data_dir = Path(__file__).parent
kosmann_data = np.load(data_dir / 's23a_kosmann_singlet.npz', allow_pickle=True)
umklapp_data = np.load(data_dir / 's32a_umklapp_vertex.npz', allow_pickle=True)

tau_values = kosmann_data['tau_values']
n_tau = len(tau_values)

print(f"tau_values = {tau_values}")

# Eigenvalue ordering in stored data:
# Columns 0-2: -B3 (3 negative optical)
# Columns 3-6: -B2 (4 negative flat)
# Column 7:    -B1 (1 negative acoustic)
# Column 8:    +B1 (1 positive acoustic)
# Columns 9-12: +B2 (4 positive flat)
# Columns 13-15: +B3 (3 positive optical)

# For the FLAT-1 computation, we work with the POSITIVE eigenvalue sector (columns 8-15).
# B1 = column 8
# B2 = columns 9-12
# B3 = columns 13-15

B1_col = 8
B2_cols = [9, 10, 11, 12]
B3_cols = [13, 14, 15]

# Verify eigenvalue assignments
print("\n=== EIGENVALUE VERIFICATION ===")
for i in range(n_tau):
    evals = kosmann_data[f'eigenvalues_{i}']
    print(f"  tau={tau_values[i]:.2f}: B1(col8)={evals[B1_col]:.6f}  "
          f"B2(cols9-12)={evals[B2_cols[0]]:.6f}  B3(col13)={evals[B3_cols[0]]:.6f}")

# ============================================================
# 1. COMPUTE dD/dtau MATRIX ELEMENTS VIA EIGENVECTOR DERIVATIVES
# ============================================================
# Using: <psi_m|dD/dtau|psi_n> = (lambda_n - lambda_m) * <psi_m|dpsi_n/dtau>
# for m != n.
#
# dpsi_n/dtau is approximated by finite difference of the eigenvectors at
# neighboring tau values. We need to handle the gauge freedom (arbitrary phase
# of each eigenvector) by aligning phases between consecutive tau values.

def align_phases(U_ref, U_new):
    """Align eigenvector phases between consecutive tau values.

    For each column (eigenvector), multiply by a phase factor that maximizes
    overlap with the reference eigenvectors. This handles the arbitrary phase
    choice in degenerate subspaces.

    For degenerate subspaces, we use a more careful alignment:
    project the new subspace onto the reference and use SVD to find the
    optimal rotation within the degenerate manifold.
    """
    n = U_ref.shape[1]
    U_aligned = U_new.copy()

    # Group by eigenvalue (degenerate subspaces)
    # For this problem, the structure is fixed: B3(3) + B2(4) + B1(1) + B1(1) + B2(4) + B3(3)
    # Process each group separately

    # Non-degenerate groups first (B1 positive, B1 negative: single columns)
    for col in [7, 8]:  # -B1, +B1
        overlap = np.dot(U_ref[:, col].conj(), U_new[:, col])
        phase = overlap / abs(overlap) if abs(overlap) > 1e-10 else 1.0
        U_aligned[:, col] = U_new[:, col] / phase

    # Degenerate groups: B2 (4-fold) and B3 (3-fold)
    for cols in [[0, 1, 2], [3, 4, 5, 6], [9, 10, 11, 12], [13, 14, 15]]:
        # Project new subspace onto reference using SVD
        overlap_matrix = U_ref[:, cols].conj().T @ U_new[:, cols]
        U_svd, S_svd, Vh_svd = np.linalg.svd(overlap_matrix)
        # Optimal rotation within degenerate subspace
        rotation = U_svd @ Vh_svd
        U_aligned[:, cols] = U_new[:, cols] @ rotation.conj().T

    return U_aligned

# Load and align eigenvectors at all tau values
eigvecs = []
for i in range(n_tau):
    U = kosmann_data[f'eigenvectors_{i}']
    eigvecs.append(U.copy())

# Align phases relative to tau=0 reference
eigvecs_aligned = [eigvecs[0].copy()]
for i in range(1, n_tau):
    U_aligned = align_phases(eigvecs_aligned[i-1], eigvecs[i])
    eigvecs_aligned.append(U_aligned)

# Verify alignment quality
print("\n=== PHASE ALIGNMENT QUALITY ===")
for i in range(1, n_tau):
    # Check overlap of each eigenvector with its aligned neighbor
    overlap = np.abs(np.diag(eigvecs_aligned[i-1].conj().T @ eigvecs_aligned[i]))
    print(f"  tau={tau_values[i-1]:.2f}->{tau_values[i]:.2f}: min|overlap| = {np.min(overlap):.6f}  "
          f"max|overlap| = {np.max(overlap):.6f}")

# ============================================================
# 2. COMPUTE OFF-DIAGONAL MATRIX ELEMENTS AT KEY TAU VALUES
# ============================================================
# We evaluate at tau=0.15 (idx=2), 0.20 (idx=3), 0.25 (idx=4)
# using centered finite differences where possible.

results = {}

for idx in [1, 2, 3, 4, 5, 6, 7]:  # tau = 0.10 through 0.40
    tau = tau_values[idx]
    evals = kosmann_data[f'eigenvalues_{idx}']
    U = eigvecs_aligned[idx]

    # Compute dpsi/dtau by centered finite difference
    if idx > 0 and idx < n_tau - 1:
        h_l = tau_values[idx] - tau_values[idx-1]
        h_r = tau_values[idx+1] - tau_values[idx]
        U_prev = eigvecs_aligned[idx-1]
        U_next = eigvecs_aligned[idx+1]
        # Non-uniform centered difference
        dU = (-h_r / (h_l * (h_l + h_r))) * U_prev + \
             ((h_r - h_l) / (h_l * h_r)) * U + \
             (h_l / (h_r * (h_l + h_r))) * U_next
    elif idx == 0:
        h = tau_values[1] - tau_values[0]
        dU = (eigvecs_aligned[1] - U) / h
    else:
        h = tau_values[-1] - tau_values[-2]
        dU = (U - eigvecs_aligned[-2]) / h

    # Matrix elements: <psi_m|dD/dtau|psi_n> = (lambda_n - lambda_m) * <psi_m|dpsi_n/dtau>
    # Compute overlap <psi_m|dpsi_n/dtau>
    overlap_dU = U.conj().T @ dU  # (16, 16) matrix

    # dD/dtau matrix elements
    dD_matrix = np.zeros((16, 16), dtype=complex)
    for m in range(16):
        for n in range(16):
            if m == n:
                # Diagonal: dlambda/dtau (from Hellmann-Feynman)
                dD_matrix[m, n] = overlap_dU[m, n].real  # Should match finite-diff eigenvalue derivative
            else:
                dD_matrix[m, n] = (evals[n] - evals[m]) * overlap_dU[m, n]

    # Extract B1-B2, B2-B3, and B1-B3 couplings
    # B1 = col 8, B2 = cols 9-12, B3 = cols 13-15

    # <B1|dD/dtau|B2_k> for each B2 mode k
    V_B1_B2 = np.array([dD_matrix[B1_col, k] for k in B2_cols])

    # <B2_k|dD/dtau|B3_j> for each B2 mode k and B3 mode j
    V_B2_B3 = np.array([[dD_matrix[k, j] for j in B3_cols] for k in B2_cols])

    # Direct <B1|dD/dtau|B3_j>
    V_B1_B3_direct = np.array([dD_matrix[B1_col, j] for j in B3_cols])

    # Energy differences
    E_B1 = evals[B1_col]
    E_B2 = np.array([evals[k] for k in B2_cols])
    E_B3 = np.array([evals[j] for j in B3_cols])

    # V_eff(B1,B3) = sum_{k in B2} |<B1|dD/dtau|B2_k>|^2 * |<B2_k|dD/dtau|B3_j>|^2 / (E_B1 - E_B2_k)^2
    # Sum over B2 modes and average over B3 modes
    V_eff_per_B3 = np.zeros(3)
    for j_idx, j in enumerate(B3_cols):
        for k_idx, k in enumerate(B2_cols):
            dE = E_B1 - E_B2[k_idx]
            if abs(dE) > 1e-12:
                V_eff_per_B3[j_idx] += np.abs(V_B1_B2[k_idx])**2 * np.abs(V_B2_B3[k_idx, j_idx])**2 / dE**2

    V_eff_total = np.sum(V_eff_per_B3)
    V_eff_avg = np.mean(V_eff_per_B3)

    # Sign determination: is the interaction attractive or repulsive?
    # In second-order perturbation theory with intermediate virtual states,
    # the sign depends on the energy ordering:
    # E_B1 < E_B2 < E_B3 (at tau=0.15-0.20)
    # => (E_B1 - E_B2) < 0 => the denominator squared is positive
    # The sign of V_eff itself is ALWAYS POSITIVE (it's a sum of |...|^2 / (...)^2)
    #
    # For the PHYSICAL effective interaction, we need the sign of the
    # second-order energy shift: Delta E ~ -|V|^2 / Delta_E
    # where Delta_E = E_intermediate - E_initial > 0 for virtual excitation.
    #
    # For B1-B3 mediated by B2:
    #   Delta E_{B1} = -sum_k |<B1|V|B2_k>|^2 / (E_B2_k - E_B1) < 0 (attractive, B2 > B1)
    #   But combined B1-B3 interaction through B2:
    #   V_eff = -sum_k <B1|V|B2_k><B2_k|V|B3> / [(E_B2 - E_B1)(E_B2 - E_B3)]
    #   Since E_B2 > E_B1 and E_B2 < E_B3:
    #   (E_B2 - E_B1) > 0 and (E_B2 - E_B3) < 0
    #   => denominator < 0 => V_eff has OPPOSITE sign from the numerator product

    # Proper effective interaction (second-order perturbation, off-diagonal):
    V_eff_proper = np.zeros(3, dtype=complex)
    for j_idx, j in enumerate(B3_cols):
        for k_idx, k in enumerate(B2_cols):
            dE_B1_B2 = E_B2[k_idx] - E_B1   # > 0
            dE_B3_B2 = E_B2[k_idx] - E_B3[j_idx]  # < 0 (B3 > B2)
            if abs(dE_B1_B2) > 1e-12 and abs(dE_B3_B2) > 1e-12:
                V_eff_proper[j_idx] += (V_B1_B2[k_idx] * np.conj(V_B2_B3[k_idx, j_idx])) / (dE_B1_B2 * dE_B3_B2)

    V_eff_proper_total = np.sum(V_eff_proper)

    results[tau] = {
        'V_B1_B2': V_B1_B2,
        'V_B2_B3': V_B2_B3,
        'V_B1_B3_direct': V_B1_B3_direct,
        'E_B1': E_B1,
        'E_B2': E_B2,
        'E_B3': E_B3,
        'V_eff_total': V_eff_total,
        'V_eff_avg': V_eff_avg,
        'V_eff_proper': V_eff_proper,
        'V_eff_proper_total': V_eff_proper_total,
    }

    print(f"\n=== tau = {tau:.2f} ===")
    print(f"  E_B1 = {E_B1:.6f}")
    print(f"  E_B2 = {E_B2}")
    print(f"  E_B3 = {E_B3}")
    print(f"  gap(B2-B1) = {E_B2[0]-E_B1:.6f}")
    print(f"  gap(B3-B2) = {E_B3[0]-E_B2[0]:.6f}")
    print(f"\n  |<B1|dD/dtau|B2_k>|:")
    for k_idx in range(4):
        print(f"    k={k_idx}: {np.abs(V_B1_B2[k_idx]):.6f}")
    print(f"\n  |<B2_k|dD/dtau|B3_j>| matrix:")
    for k_idx in range(4):
        row = '  '.join(f'{np.abs(V_B2_B3[k_idx, j_idx]):.6f}' for j_idx in range(3))
        print(f"    B2_{k_idx}: [{row}]")
    print(f"\n  |<B1|dD/dtau|B3_j>| (direct):")
    for j_idx in range(3):
        print(f"    j={j_idx}: {np.abs(V_B1_B3_direct[j_idx]):.6f}")
    print(f"\n  V_eff (|.|^2/E^2 form, always positive): {V_eff_total:.8f}")
    print(f"  V_eff (proper sign, per B3 mode): {V_eff_proper}")
    print(f"  V_eff (proper sign, total): {V_eff_proper_total:.8f}")
    sign_str = "ATTRACTIVE" if V_eff_proper_total.real < 0 else "REPULSIVE" if V_eff_proper_total.real > 0 else "ZERO"
    print(f"  Sign: {sign_str} (Re = {V_eff_proper_total.real:+.8f})")

# ============================================================
# 3. GATE CLASSIFICATION
# ============================================================

# Evaluate at tau=0.15 and 0.20 (gradient-balance region)
V_eff_15 = results[0.15]['V_eff_proper_total']
V_eff_20 = results[0.20]['V_eff_proper_total']

# Use both for classification
if V_eff_15.real < 0 and V_eff_20.real < 0:
    fl32a_verdict = "ATTRACTIVE"
    fl32a_detail = (f"V_eff(B1,B3) = {V_eff_15.real:+.6f} (tau=0.15), "
                    f"{V_eff_20.real:+.6f} (tau=0.20). Both attractive. "
                    f"Extra collective instability reinforces RPA.")
elif V_eff_15.real > 0 and V_eff_20.real > 0:
    fl32a_verdict = "REPULSIVE"
    fl32a_detail = (f"V_eff(B1,B3) = {V_eff_15.real:+.6f} (tau=0.15), "
                    f"{V_eff_20.real:+.6f} (tau=0.20). Both repulsive. "
                    f"Standard RPA sufficient.")
elif abs(V_eff_15.real) < 1e-10 and abs(V_eff_20.real) < 1e-10:
    fl32a_verdict = "ZERO"
    fl32a_detail = (f"V_eff(B1,B3) = {V_eff_15.real:+.6e} (tau=0.15), "
                    f"{V_eff_20.real:+.6e} (tau=0.20). Effectively zero. "
                    f"Standard RPA sufficient.")
else:
    fl32a_verdict = "SIGN-CHANGING"
    fl32a_detail = (f"V_eff(B1,B3) = {V_eff_15.real:+.6f} (tau=0.15), "
                    f"{V_eff_20.real:+.6f} (tau=0.20). Sign changes between tau values.")

print(f"\n{'='*60}")
print(f"GATE FL-32a: {fl32a_verdict} -- {fl32a_detail}")
print(f"{'='*60}")

# ============================================================
# 4. COMPARISON: DIRECT VS B2-MEDIATED COUPLING
# ============================================================

print(f"\n=== DIRECT vs B2-MEDIATED COUPLING ===")
for tau in [0.15, 0.20, 0.25]:
    r = results[tau]
    V_direct = np.mean(np.abs(r['V_B1_B3_direct'])**2)
    V_mediated = r['V_eff_total']
    ratio = V_mediated / V_direct if V_direct > 1e-15 else float('inf')
    print(f"  tau={tau:.2f}: |V_direct|^2 = {V_direct:.8f}  V_mediated = {V_mediated:.8f}  ratio = {ratio:.4f}")

# ============================================================
# 5. SAVE RESULTS
# ============================================================

# Collect tau-dependent arrays
taus_computed = sorted(results.keys())
V_eff_proper_vs_tau = np.array([results[t]['V_eff_proper_total'] for t in taus_computed])
V_eff_total_vs_tau = np.array([results[t]['V_eff_total'] for t in taus_computed])
V_B1_B2_norms = np.array([np.mean(np.abs(results[t]['V_B1_B2'])**2) for t in taus_computed])
V_B2_B3_norms = np.array([np.mean(np.abs(results[t]['V_B2_B3'])**2) for t in taus_computed])
V_direct_norms = np.array([np.mean(np.abs(results[t]['V_B1_B3_direct'])**2) for t in taus_computed])

np.savez(data_dir / 's32a_flat_b2_interaction.npz',
    taus_computed=np.array(taus_computed),
    V_eff_proper_vs_tau=V_eff_proper_vs_tau,
    V_eff_total_vs_tau=V_eff_total_vs_tau,
    V_B1_B2_norms=V_B1_B2_norms,
    V_B2_B3_norms=V_B2_B3_norms,
    V_direct_norms=V_direct_norms,
    fl32a_verdict=fl32a_verdict,
)

print(f"\nSaved: s32a_flat_b2_interaction.npz")

# ============================================================
# 6. PLOTS
# ============================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Session 32a: FLAT-1 -- B2-Mediated Effective Interaction', fontsize=14)

# Panel (a): V_eff (proper sign) vs tau
ax = axes[0, 0]
ax.plot(taus_computed, np.real(V_eff_proper_vs_tau), 'rs-',
        label=r'Re[$V_{\rm eff}$] (proper)', markersize=6, linewidth=2)
ax.plot(taus_computed, np.imag(V_eff_proper_vs_tau), 'b^--',
        label=r'Im[$V_{\rm eff}$]', markersize=5, alpha=0.7)
ax.axhline(y=0, color='gray', linestyle='-', alpha=0.5)
ax.axvspan(0.10, 0.31, alpha=0.1, color='green', label='Instanton orbit')
ax.fill_between(taus_computed, 0, np.real(V_eff_proper_vs_tau),
                where=(np.real(V_eff_proper_vs_tau) < 0),
                alpha=0.2, color='blue', label='ATTRACTIVE')
ax.fill_between(taus_computed, 0, np.real(V_eff_proper_vs_tau),
                where=(np.real(V_eff_proper_vs_tau) > 0),
                alpha=0.2, color='red', label='REPULSIVE')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$V_{\rm eff}(B1, B3)$')
ax.set_title(f'(a) Effective B1-B3 Interaction [FL-32a: {fl32a_verdict}]')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel (b): Coupling magnitudes
ax = axes[0, 1]
ax.semilogy(taus_computed, V_B1_B2_norms, 'bo-', label=r'$\langle |V_{B1,B2}|^2 \rangle$', markersize=5)
ax.semilogy(taus_computed, V_B2_B3_norms, 'r^-', label=r'$\langle |V_{B2,B3}|^2 \rangle$', markersize=5)
ax.semilogy(taus_computed, V_direct_norms, 'ks--', label=r'$\langle |V_{B1,B3}|^2 \rangle$ (direct)', markersize=5)
ax.axvspan(0.10, 0.31, alpha=0.1, color='green')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'Mean $|V|^2$')
ax.set_title('(b) Coupling Matrix Element Magnitudes')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel (c): V_eff magnitude vs tau
ax = axes[1, 0]
ax.plot(taus_computed, V_eff_total_vs_tau, 'gs-',
        label=r'$\sum |V|^2/\Delta E^2$ (magnitude)', markersize=6, linewidth=2)
ax.axvspan(0.10, 0.31, alpha=0.1, color='green')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$V_{\rm eff}$ (unsigned)')
ax.set_title('(c) V_eff Magnitude')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel (d): Direct vs mediated ratio
ax = axes[1, 1]
ratios = V_eff_total_vs_tau / np.maximum(V_direct_norms, 1e-15)
ax.plot(taus_computed, ratios, 'mo-', markersize=6, linewidth=2,
        label=r'$V_{\rm mediated}/|V_{\rm direct}|^2$')
ax.axhline(y=1, color='gray', linestyle='--', alpha=0.5, label='Equal')
ax.axvspan(0.10, 0.31, alpha=0.1, color='green')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel('Ratio')
ax.set_title('(d) Mediated / Direct Coupling Ratio')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)
ax.set_yscale('log')

plt.tight_layout()
plt.savefig(data_dir / 's32a_flat_b2_interaction.png', dpi=150, bbox_inches='tight')
print(f"Saved: s32a_flat_b2_interaction.png")

print("\n=== COMPUTATION COMPLETE ===")
