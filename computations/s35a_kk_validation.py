#!/usr/bin/env python3
"""
Session 35a: KK Independent Validation — M_max with Correct Spinor Pairing Kernel
==================================================================================
Cross-check of M_max using K_a_matrix (spinor, CORRECT) vs A_antisym (frame, WRONG)
across 4 DOS scenarios x 2 V-matrix choices = 8 M_max values.

Author: kk (kaluza-klein-theorist), Session 35a
Date: 2026-03-06
"""

import os
import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA = np.load(os.path.join(SCRIPT_DIR, 's23a_kosmann_singlet.npz'), allow_pickle=True)

# ==============================================================================
#  tau_idx = 3  =>  tau = 0.20
# ==============================================================================
ti = 3
tau = float(DATA['tau_values'][ti])

# --- Sorted eigenvalues & branch identification ---
evals_raw = DATA[f'eigenvalues_singlet_{ti}']
si = np.argsort(evals_raw)
evals_sorted = evals_raw[si]

pos_idx = np.where(evals_sorted > 0)[0]  # indices [8..15]
# Ascending positive: B1(1) + B2(4) + B3(3)
B1_full = pos_idx[0:1]    # [8]
B2_full = pos_idx[1:5]    # [9,10,11,12]
B3_full = pos_idx[5:8]    # [13,14,15]

E_B1 = evals_sorted[B1_full]  # [0.81914]
E_B2 = evals_sorted[B2_full]  # [0.84527 x4]
E_B3 = evals_sorted[B3_full]  # [0.97822 x3]

# B2+B1 subspace (5 modes), B2 first then B1
idx_5 = np.concatenate([B2_full, B1_full])  # [9,10,11,12,8]
E_5 = evals_sorted[idx_5]

# ==============================================================================
#  Build V_spinor (16x16) from K_a_matrix — already in eigenbasis
# ==============================================================================
V_spinor_full = np.zeros((16, 16))
for a in range(8):
    K = DATA[f'K_a_matrix_{ti}_{a}']
    V_spinor_full += np.abs(K)**2

V_spinor_5x5 = V_spinor_full[np.ix_(idx_5, idx_5)]

# ==============================================================================
#  Build V_frame (8x8) from A_antisym
# ==============================================================================
V_frame_full = np.zeros((8, 8))
for a in range(8):
    A = DATA[f'A_antisym_{ti}_{a}']
    V_frame_full += np.abs(A)**2

# Frame ordering: B3=[0,1,2], B2=[3,4,5,6], B1=[7]
frame_idx_5 = np.array([3, 4, 5, 6, 7])  # B2 + B1

# Frame eigenvalues in branch order: B3(top 3), B2(middle 4), B1(bottom 1)
pos_ev_sorted = np.sort(evals_sorted[evals_sorted > 0])
E_branch_8 = np.zeros(8)
E_branch_8[0:3] = pos_ev_sorted[5:8]   # B3
E_branch_8[3:7] = pos_ev_sorted[1:5]   # B2
E_branch_8[7]   = pos_ev_sorted[0]     # B1
E_frame_5 = E_branch_8[frame_idx_5]

V_frame_5x5 = V_frame_full[np.ix_(frame_idx_5, frame_idx_5)]

# ==============================================================================
#  Verify discrepancy
# ==============================================================================
V_B2B2_spinor = V_spinor_full[np.ix_(B2_full, B2_full)]
V_B2B2_spinor_offdiag = V_B2B2_spinor.copy()
np.fill_diagonal(V_B2B2_spinor_offdiag, 0)

V_B2B2_frame = V_frame_full[np.ix_([3,4,5,6], [3,4,5,6])]
V_B2B2_frame_offdiag = V_B2B2_frame.copy()
np.fill_diagonal(V_B2B2_frame_offdiag, 0)

print("=" * 72)
print(f"KK VALIDATION: tau = {tau}")
print("=" * 72)
print(f"\n  V(B2,B2) max off-diag  SPINOR (K_a_matrix): {np.max(V_B2B2_spinor_offdiag):.6f}")
print(f"  V(B2,B2) max off-diag  FRAME  (A_antisym):  {np.max(V_B2B2_frame_offdiag):.6f}")
print(f"  Ratio frame/spinor: {np.max(V_B2B2_frame_offdiag)/np.max(V_B2B2_spinor_offdiag):.2f}x")

# ==============================================================================
#  Thouless M_max computation
# ==============================================================================
def thouless_Mmax(V_5x5, E_5, rho_B2, rho_B1=1.0, eta_frac=0.001):
    """Linearized BdG Thouless criterion at mu=0.
    M_nm = V_nm * rho_m / (2 * |xi_m|), xi_m = E_m (mu=0).
    Returns max Re(eigenvalue of M).
    """
    xi = E_5.copy()
    lam_min = np.min(np.abs(xi))
    eta = max(eta_frac * lam_min, 1e-15)
    abs_xi = np.maximum(np.abs(xi), eta)
    rho = np.array([rho_B2]*4 + [rho_B1])
    M = np.zeros((5, 5))
    for m in range(5):
        M[:, m] = V_5x5[:, m] * rho[m] / (2.0 * abs_xi[m])
    return np.max(np.real(np.linalg.eigvals(M)))

# ==============================================================================
#  4 scenarios x 2 V-matrices
# ==============================================================================
scenarios = {
    "Step + old impedance":       5.40 * 1.046 * 1.56,
    "Step + corrected impedance": 5.40 * 1.046 * 1.00,
    "Smooth + old impedance":     14.02 * 1.046 * 1.56,
    "Smooth + corrected imp":     14.02 * 1.046 * 1.00,
}

results = {}
print(f"\n{'':>30s}  {'rho_B2':>8s}  {'M_max(spinor)':>14s}  {'M_max(frame)':>14s}")
print(f"  {'-'*70}")

for name, rho_B2 in scenarios.items():
    M_spinor = thouless_Mmax(V_spinor_5x5, E_5, rho_B2)
    M_frame  = thouless_Mmax(V_frame_5x5, E_frame_5, rho_B2)
    results[name] = {'rho': rho_B2, 'M_spinor': M_spinor, 'M_frame': M_frame}
    tag_s = "PASS" if M_spinor >= 1.0 else "FAIL"
    tag_f = "PASS" if M_frame >= 1.0 else "FAIL"
    print(f"  {name:>28s}  {rho_B2:8.2f}  {M_spinor:10.6f} {tag_s:>4s}  {M_frame:10.6f} {tag_f:>4s}")

# ==============================================================================
#  The answer: M_max at (rho=14.67, K_a_matrix)
# ==============================================================================
rho_answer = 14.02 * 1.046 * 1.00  # = 14.665
M_answer = thouless_Mmax(V_spinor_5x5, E_5, rho_answer)

print(f"\n{'=' * 72}")
print(f"  ANSWER: M_max = {M_answer:.6f}  at rho_B2 = {rho_answer:.2f}")
print(f"          (smooth VH DOS + corrected impedance + K_a_matrix spinor V)")
print(f"          Verdict: {'PASS' if M_answer >= 1.0 else 'FAIL'}")
print(f"{'=' * 72}")

# ==============================================================================
#  Save
# ==============================================================================
save = {
    'tau': tau,
    'V_B2B2_spinor_max_offdiag': np.max(V_B2B2_spinor_offdiag),
    'V_B2B2_frame_max_offdiag': np.max(V_B2B2_frame_offdiag),
    'E_5_spinor': E_5,
    'E_5_frame': E_frame_5,
    'V_spinor_5x5': V_spinor_5x5,
    'V_frame_5x5': V_frame_5x5,
}
for name, r in results.items():
    key = name.replace(' ', '_').replace('+', 'p').lower()
    save[f'rho_{key}'] = r['rho']
    save[f'M_spinor_{key}'] = r['M_spinor']
    save[f'M_frame_{key}'] = r['M_frame']
save['M_answer'] = M_answer
save['rho_answer'] = rho_answer

out = os.path.join(SCRIPT_DIR, 's35a_kk_validation.npz')
np.savez_compressed(out, **save)
print(f"\nSaved: {out}")
print(f"Size: {os.path.getsize(out) / 1024:.1f} KB")
