#!/usr/bin/env python3
"""
Session 35 K7-DPHYS-35: [iK_7, D_phys] Commutator at tau=0.190
===============================================================================

CONTEXT:
--------
Session 34 proved [iK_7, D_K] = 0 at ALL tau -- the bare Dirac operator commutes
with the K_7 Kosmann derivative EXACTLY. But the physical Dirac operator
D_phys = D_K + phi*[D_K, H_j] + J*phi*[D_K, H_j]*J^{-1} includes inner
fluctuations from the finite algebra A_F = C + H + M_3(C).

This task checks whether the U(1)_7 symmetry survives the inner fluctuation
in the H_j direction at gap-edge amplitude phi=0.133.

METHOD:
-------
1. Build D_K at tau=0.190 from first principles (su3 -> Jensen metric -> connection -> spinor)
2. Build K_7 (Kosmann derivative, a=7) in the FULL 16x16 spinor basis at tau=0.190
3. Construct the H_j fluctuation: phi_Hj = [D_K, H_j] where H_j is the quaternionic
   generator acting on the lepton doublet sector of C^{16}
4. Apply the J operator: D_phys = D_K + phi*(phi_Hj + J*phi_Hj*J^{-1})
5. Compute [iK_7, D_phys] in the spinor basis
6. Report ||[iK_7, D_phys]||_F / ||D_phys||_F

GATE K7-DPHYS-35 (INFORMATIVE):
  Near-zero (< 0.01): U(1)_7 preserved under inner fluctuations. Stronger symmetry.
  O(0.1) or larger:   U(1)_7 broken. Extract electroweak mixing angle.

Author: baptista-spacetime-analyst, Session 35
Date: 2026-03-07
"""

import os
import sys
import time
import numpy as np
from numpy.linalg import eigh, norm
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from tier1_dirac_spectrum import (
    su3_generators, compute_structure_constants,
    compute_killing_form, jensen_metric, orthonormal_frame,
    frame_structure_constants, connection_coefficients,
    build_cliff8, spinor_connection_offset
)
from s23a_kosmann_singlet import kosmann_operator_antisymmetric
from s34a_dphys_fold import (
    build_J_operator, apply_J_to_matrix, build_AF_generators
)

np.set_printoptions(precision=10, linewidth=140, suppress=True)
t0 = time.time()

# ======================================================================
#  STEP 0: Build all infrastructure at tau = 0.190
# ======================================================================

TAU = 0.190
PHI_GAP = 0.133  # gap-edge amplitude

print("=" * 78)
print(f"K7-DPHYS-35: [iK_7, D_phys] at tau = {TAU}, phi = {PHI_GAP}")
print("=" * 78)

# --- Build D_K from first principles ---
gens = su3_generators()
fabc = compute_structure_constants(gens)
Bk = compute_killing_form(fabc)
g_s = jensen_metric(Bk, TAU)
E = orthonormal_frame(g_s)
ft = frame_structure_constants(fabc, E)
Gamma = connection_coefficients(ft)
gammas = build_cliff8()
Omega = spinor_connection_offset(Gamma, gammas)
D_K = 1j * Omega  # Hermitian Dirac operator

# Verify hermiticity
herm_err_DK = np.max(np.abs(D_K - D_K.conj().T))
print(f"\nStep 0: D_K at tau={TAU}")
print(f"  Hermiticity: |D_K - D_K^dag| = {herm_err_DK:.2e}")
assert herm_err_DK < 1e-14, f"D_K not hermitian: {herm_err_DK}"

# Diagonalize D_K
evals_DK, evecs_DK = eigh(D_K)
print(f"  Eigenvalues: {evals_DK}")

# --- Build K_7 in the SPINOR basis (not eigenbasis) ---
K7_spinor, A7_antisym = kosmann_operator_antisymmetric(Gamma, gammas, 7)
print(f"\nStep 0: K_7 (Kosmann, a=7) in spinor basis")
print(f"  Anti-hermiticity: |K_7 + K_7^dag| = {np.max(np.abs(K7_spinor + K7_spinor.conj().T)):.2e}")
print(f"  ||K_7||_F = {norm(K7_spinor, 'fro'):.6f}")

# iK_7 should be Hermitian
iK7 = 1j * K7_spinor
herm_err_iK7 = np.max(np.abs(iK7 - iK7.conj().T))
print(f"  Hermiticity of iK_7: |iK_7 - iK_7^dag| = {herm_err_iK7:.2e}")
assert herm_err_iK7 < 1e-14, f"iK_7 not hermitian: {herm_err_iK7}"

# --- Cross-check: [iK_7, D_K] should be zero ---
comm_bare = iK7 @ D_K - D_K @ iK7
comm_bare_norm = norm(comm_bare, 'fro')
DK_norm = norm(D_K, 'fro')
print(f"\nStep 0: Cross-check [iK_7, D_K]")
print(f"  ||[iK_7, D_K]||_F = {comm_bare_norm:.2e}")
print(f"  ||D_K||_F = {DK_norm:.6f}")
print(f"  Ratio = {comm_bare_norm/DK_norm:.2e}")
assert comm_bare_norm / DK_norm < 1e-12, f"[iK_7, D_K] != 0: ratio = {comm_bare_norm/DK_norm}"
print(f"  CONFIRMED: [iK_7, D_K] = 0 to machine epsilon at tau={TAU}")

# --- Build J operator ---
B_J = build_J_operator(gammas)
print(f"\nStep 0: J operator (C2 = gamma_1*gamma_3*gamma_5*gamma_7)")
jdj = apply_J_to_matrix(B_J, D_K)
jdj_err = np.max(np.abs(jdj - D_K))
print(f"  |J D_K J^{{-1}} - D_K| = {jdj_err:.2e}")
assert jdj_err < 1e-12, f"J D J^{{-1}} != D: {jdj_err}"

# ======================================================================
#  STEP 1: Build inner fluctuation in H_j direction
# ======================================================================

print(f"\n{'='*78}")
print(f"Step 1: Inner fluctuation phi_Hj = [D_K, H_j]")
print(f"{'='*78}")

# Build A_F generators (includes H_j)
af_gens = build_AF_generators()
H_j_gen = None
for name, gen in af_gens:
    if name == 'H_j':
        H_j_gen = gen
        break
assert H_j_gen is not None, "H_j generator not found in A_F"

# Compute [D_K, H_j] in the spinor basis
commutator_DK_Hj = D_K @ H_j_gen - H_j_gen @ D_K
print(f"  ||[D_K, H_j]||_F = {norm(commutator_DK_Hj, 'fro'):.6f}")

# Check hermiticity of [D_K, H_j]
herm_comm = np.max(np.abs(commutator_DK_Hj - commutator_DK_Hj.conj().T))
print(f"  Hermiticity of [D_K, H_j]: {herm_comm:.2e}")

# Note: [D_K, H_j] may or may not be Hermitian. For the physical fluctuation
# phi + J phi J^{-1}, it is the self-adjoint combination that enters D_phys.
# D_phys = D_K + phi * ([D_K, H_j] + J [D_K, H_j] J^{-1})

phi_Hj = commutator_DK_Hj
J_phi_Hj = apply_J_to_matrix(B_J, phi_Hj)

# The self-adjoint inner fluctuation
A_inner = phi_Hj + J_phi_Hj
herm_A = np.max(np.abs(A_inner - A_inner.conj().T))
print(f"  A = [D_K,H_j] + J[D_K,H_j]J^{{-1}}")
print(f"  Hermiticity of A: {herm_A:.2e}")
print(f"  ||A||_F = {norm(A_inner, 'fro'):.6f}")

# If A is not hermitian, symmetrize for D_phys (physical requirement)
if herm_A > 1e-10:
    print(f"  WARNING: A not hermitian. Using (A + A^dag)/2 for D_phys.")
    A_inner = 0.5 * (A_inner + A_inner.conj().T)

# ======================================================================
#  STEP 2: Construct D_phys = D_K + phi * A
# ======================================================================

print(f"\n{'='*78}")
print(f"Step 2: D_phys = D_K + {PHI_GAP} * A")
print(f"{'='*78}")

D_phys = D_K + PHI_GAP * A_inner
herm_err_Dphys = np.max(np.abs(D_phys - D_phys.conj().T))
print(f"  Hermiticity of D_phys: {herm_err_Dphys:.2e}")

evals_phys, evecs_phys = eigh(D_phys)
print(f"  D_phys eigenvalues: {evals_phys}")
print(f"  ||D_phys||_F = {norm(D_phys, 'fro'):.6f}")

# Compare with D_K
print(f"\n  Eigenvalue comparison D_K vs D_phys:")
print(f"  {'D_K':>12s}  {'D_phys':>12s}  {'Shift':>12s}")
for i in range(16):
    print(f"  {evals_DK[i]:12.6f}  {evals_phys[i]:12.6f}  {evals_phys[i]-evals_DK[i]:12.6f}")

# ======================================================================
#  STEP 3: Compute [iK_7, D_phys]
# ======================================================================

print(f"\n{'='*78}")
print(f"Step 3: Commutator [iK_7, D_phys]")
print(f"{'='*78}")

comm_phys = iK7 @ D_phys - D_phys @ iK7
comm_phys_frob = norm(comm_phys, 'fro')
Dphys_frob = norm(D_phys, 'fro')
ratio = comm_phys_frob / Dphys_frob

print(f"  ||[iK_7, D_phys]||_F = {comm_phys_frob:.10f}")
print(f"  ||D_phys||_F = {Dphys_frob:.10f}")
print(f"  RATIO = {ratio:.10f}")

# Decompose: since [iK_7, D_K] = 0, the entire commutator comes from the fluctuation:
# [iK_7, D_phys] = [iK_7, D_K] + phi * [iK_7, A]
#                = 0            + phi * [iK_7, A]
comm_A = iK7 @ A_inner - A_inner @ iK7
comm_A_frob = norm(comm_A, 'fro')
print(f"\n  Decomposition:")
print(f"  [iK_7, D_phys] = [iK_7, D_K] + phi * [iK_7, A]")
print(f"  ||[iK_7, D_K]||_F = {comm_bare_norm:.2e}  (zero by Session 34 result)")
print(f"  ||[iK_7, A]||_F = {comm_A_frob:.10f}")
print(f"  phi * ||[iK_7, A]||_F = {PHI_GAP * comm_A_frob:.10f}")
print(f"  Cross-check: {PHI_GAP * comm_A_frob:.10f} vs {comm_phys_frob:.10f}  "
      f"(diff = {abs(comm_phys_frob - PHI_GAP * comm_A_frob):.2e})")

# Further decompose: [iK_7, A] = [iK_7, [D_K, H_j]] + [iK_7, J[D_K,H_j]J^{-1}]
comm_phi = iK7 @ phi_Hj - phi_Hj @ iK7
comm_Jphi = iK7 @ J_phi_Hj - J_phi_Hj @ iK7
print(f"\n  Further decomposition:")
print(f"  ||[iK_7, [D_K,H_j]]||_F = {norm(comm_phi, 'fro'):.10f}")
print(f"  ||[iK_7, J[D_K,H_j]J^{{-1}}]||_F = {norm(comm_Jphi, 'fro'):.10f}")

# ======================================================================
#  STEP 4: Project into eigenspaces for physical interpretation
# ======================================================================

print(f"\n{'='*78}")
print(f"Step 4: Eigenspace analysis")
print(f"{'='*78}")

# Project [iK_7, D_phys] into D_phys eigenbasis
comm_eig = evecs_phys.conj().T @ comm_phys @ evecs_phys
print(f"  Commutator in D_phys eigenbasis:")
print(f"  Max diagonal |element| = {np.max(np.abs(np.diag(comm_eig))):.10f}")
print(f"  Max off-diagonal |element| = {np.max(np.abs(comm_eig - np.diag(np.diag(comm_eig)))):.10f}")

# Identify B2 modes in D_phys (by overlap with bare B2)
pos_bare = np.where(evals_DK > 0)[0]
pos_bare_sorted = pos_bare[np.argsort(evals_DK[pos_bare])]
B2_bare = pos_bare_sorted[1:5]  # B2 = 4 modes between B1 and B3

pos_phys = np.where(evals_phys > 0)[0]
pos_phys_sorted = pos_phys[np.argsort(evals_phys[pos_phys])]

# Compute B2-ness of each D_phys mode
b2_ness = np.zeros(len(pos_phys_sorted))
for i_ph, idx_ph in enumerate(pos_phys_sorted):
    for idx_b in B2_bare:
        overlap = np.abs(np.dot(evecs_phys[:, idx_ph].conj(), evecs_DK[:, idx_b]))**2
        b2_ness[i_ph] += overlap

B2_phys_local = np.argsort(b2_ness)[-4:]
B2_phys_idx = pos_phys_sorted[B2_phys_local]

print(f"\n  B2 mode identification (D_phys):")
for i in B2_phys_idx:
    print(f"    Mode {i}: lambda_phys = {evals_phys[i]:.8f}, B2-ness = {b2_ness[np.where(pos_phys_sorted==i)[0][0]]:.4f}")

# Extract B2 block of commutator in D_phys eigenbasis
B2_comm = comm_eig[np.ix_(B2_phys_idx, B2_phys_idx)]
print(f"\n  B2 x B2 block of [iK_7, D_phys] in D_phys eigenbasis:")
print(f"  {B2_comm}")
print(f"  ||B2 block||_F = {norm(B2_comm, 'fro'):.10f}")

# ======================================================================
#  STEP 5: iK_7 eigenvalues on D_phys eigenmodes
# ======================================================================

print(f"\n{'='*78}")
print(f"Step 5: iK_7 structure on D_phys eigenmodes")
print(f"{'='*78}")

# Project iK_7 into D_phys eigenbasis
iK7_phys = evecs_phys.conj().T @ iK7 @ evecs_phys
print(f"  iK_7 in D_phys eigenbasis:")
print(f"  Diagonal elements (charges):")
for i in range(16):
    q_phys = np.real(iK7_phys[i, i])
    q_rounded = round(q_phys * 4) / 4
    branch = "B2" if i in B2_phys_idx else "other"
    print(f"    Mode {i:2d}: lambda={evals_phys[i]:+10.6f}, q_phys={q_phys:+10.6f}, "
          f"q_rounded={q_rounded:+5.2f}, {branch}")

# If [iK_7, D_phys] != 0, iK_7 is NOT diagonal in D_phys eigenbasis
# Check how far from diagonal it is
iK7_offdiag = iK7_phys - np.diag(np.diag(iK7_phys))
print(f"\n  iK_7 off-diagonal in D_phys eigenbasis:")
print(f"  ||off-diag||_F = {norm(iK7_offdiag, 'fro'):.10f}")
print(f"  ||iK_7||_F = {norm(iK7_phys, 'fro'):.10f}")
print(f"  Off-diag fraction = {norm(iK7_offdiag, 'fro')/norm(iK7_phys, 'fro'):.10f}")

# ======================================================================
#  STEP 6: Phi amplitude sweep
# ======================================================================

print(f"\n{'='*78}")
print(f"Step 6: [iK_7, D_phys] vs phi amplitude")
print(f"{'='*78}")

phi_values = np.linspace(0, 0.25, 51)
ratios = np.zeros_like(phi_values)
comm_norms = np.zeros_like(phi_values)
dphys_norms = np.zeros_like(phi_values)

for i, phi in enumerate(phi_values):
    D_phi = D_K + phi * A_inner
    c_phi = iK7 @ D_phi - D_phi @ iK7
    comm_norms[i] = norm(c_phi, 'fro')
    dphys_norms[i] = norm(D_phi, 'fro')
    ratios[i] = comm_norms[i] / dphys_norms[i]

print(f"  {'phi':>8s}  {'||[iK7,Dphi]||':>16s}  {'||Dphi||':>12s}  {'Ratio':>12s}")
for i in range(0, len(phi_values), 5):
    print(f"  {phi_values[i]:8.4f}  {comm_norms[i]:16.10f}  {dphys_norms[i]:12.6f}  {ratios[i]:12.10f}")

# Check linearity in phi (since [iK_7, D_K] = 0, ||[iK_7, D_phys]|| = phi * ||[iK_7, A]||)
if PHI_GAP > 0:
    print(f"\n  Linearity check: ||[iK_7, D_phys]|| / phi at phi=gap:")
    print(f"    ||[iK_7, A]||_F = {comm_A_frob:.10f}")
    for i in [5, 10, 20, 25]:
        if i < len(phi_values) and phi_values[i] > 1e-10:
            slope = comm_norms[i] / phi_values[i]
            print(f"    phi={phi_values[i]:.4f}: slope = {slope:.10f} "
                  f"(expected {comm_A_frob:.10f}, ratio = {slope/comm_A_frob:.6f})")

# ======================================================================
#  STEP 7: Test ALL A_F generators (not just H_j)
# ======================================================================

print(f"\n{'='*78}")
print(f"Step 7: [iK_7, D_phys(gen)] for ALL A_F generator directions")
print(f"{'='*78}")

print(f"  Testing at phi = {PHI_GAP}")
print(f"  {'Generator':>12s}  {'||A||_F':>10s}  {'||[iK7,A]||':>14s}  {'Ratio':>12s}  {'U(1)_7 broken?':>16s}")

gen_results = {}
for name, gen in af_gens:
    # Compute [D_K, gen]
    phi_gen = D_K @ gen - gen @ D_K
    if norm(phi_gen, 'fro') < 1e-12:
        gen_results[name] = {'ratio': 0.0, 'broken': False}
        print(f"  {name:>12s}  {'(trivial)':>10s}  {'---':>14s}  {'---':>12s}  {'N/A (zero fluct)':>16s}")
        continue

    J_phi_gen = apply_J_to_matrix(B_J, phi_gen)
    A_gen = phi_gen + J_phi_gen
    # Hermitize if needed
    if np.max(np.abs(A_gen - A_gen.conj().T)) > 1e-10:
        A_gen = 0.5 * (A_gen + A_gen.conj().T)

    D_phys_gen = D_K + PHI_GAP * A_gen
    comm_gen = iK7 @ D_phys_gen - D_phys_gen @ iK7
    r_gen = norm(comm_gen, 'fro') / norm(D_phys_gen, 'fro')
    broken = r_gen > 0.01

    gen_results[name] = {
        'A_norm': norm(A_gen, 'fro'),
        'comm_norm': norm(comm_gen, 'fro'),
        'ratio': r_gen,
        'broken': broken,
    }
    print(f"  {name:>12s}  {norm(A_gen, 'fro'):10.6f}  {norm(comm_gen, 'fro'):14.10f}  "
          f"{r_gen:12.10f}  {'YES' if broken else 'NO':>16s}")

n_broken = sum(1 for v in gen_results.values() if v['broken'])
n_preserved = sum(1 for v in gen_results.values() if not v['broken'])
print(f"\n  U(1)_7 preserved: {n_preserved}/{len(gen_results)} generators")
print(f"  U(1)_7 broken: {n_broken}/{len(gen_results)} generators")

# ======================================================================
#  STEP 8: If broken, extract mixing angle from B2 subspace
# ======================================================================

print(f"\n{'='*78}")
print(f"Step 8: Mixing angle extraction (if U(1)_7 broken)")
print(f"{'='*78}")

if ratio > 0.01:
    # The commutator [iK_7, A_inner] in the B2 subspace tells us how much
    # the inner fluctuation rotates within the U(1)_7 charge eigenspaces.

    # Project A_inner into D_K eigenbasis
    A_eig = evecs_DK.conj().T @ A_inner @ evecs_DK

    # B2 indices in sorted eigenvalue basis (positive sector, indices 1:5)
    B2_DK_idx = pos_bare_sorted[1:5]

    # Extract B2 block of iK_7 in D_K eigenbasis (should be diagonal +/-1/4)
    iK7_DK = evecs_DK.conj().T @ iK7 @ evecs_DK
    B2_iK7 = iK7_DK[np.ix_(B2_DK_idx, B2_DK_idx)]
    print(f"  iK_7 in B2 block (D_K eigenbasis):")
    print(f"  {np.real(B2_iK7)}")

    # Extract B2 block of A
    B2_A = A_eig[np.ix_(B2_DK_idx, B2_DK_idx)]
    print(f"\n  A_inner in B2 block (D_K eigenbasis):")
    print(f"  {B2_A}")

    # The commutator [iK_7, A] in B2 block
    B2_comm_A = B2_iK7 @ B2_A - B2_A @ B2_iK7
    print(f"\n  [iK_7, A] in B2 block:")
    print(f"  {B2_comm_A}")
    print(f"  ||[iK_7, A]_B2||_F = {norm(B2_comm_A, 'fro'):.10f}")

    # Mixing angle: if the B2 charges are +1/4 and -1/4, and A mixes them,
    # then the off-diagonal element couples q=+1/4 to q=-1/4 states.
    # theta = arctan(|A_{+-}| / |A_{++} - A_{--}|)
    # where ++ and -- are same-charge diagonal elements
    # and +- is the cross-charge off-diagonal element.

    # Identify charge sectors within B2
    B2_charges = np.real(np.diag(B2_iK7))
    print(f"\n  B2 charges: {B2_charges}")

    pos_q = np.where(B2_charges > 0.1)[0]
    neg_q = np.where(B2_charges < -0.1)[0]
    print(f"  q > 0 indices (within B2): {pos_q}")
    print(f"  q < 0 indices (within B2): {neg_q}")

    if len(pos_q) > 0 and len(neg_q) > 0:
        # Off-diagonal cross-charge coupling
        cross_block = B2_A[np.ix_(pos_q, neg_q)]
        same_pp = B2_A[np.ix_(pos_q, pos_q)]
        same_mm = B2_A[np.ix_(neg_q, neg_q)]

        print(f"\n  Cross-charge block (q=+1/4 to q=-1/4):")
        print(f"  {cross_block}")
        print(f"  ||cross||_F = {norm(cross_block, 'fro'):.10f}")

        print(f"\n  Same-charge block (q=+1/4 to q=+1/4):")
        print(f"  {same_pp}")
        print(f"  ||same++||_F = {norm(same_pp, 'fro'):.10f}")

        print(f"\n  Same-charge block (q=-1/4 to q=-1/4):")
        print(f"  {same_mm}")
        print(f"  ||same--||_F = {norm(same_mm, 'fro'):.10f}")

        off_norm = norm(cross_block, 'fro')
        diag_diff = abs(norm(same_pp, 'fro') - norm(same_mm, 'fro'))

        if off_norm > 1e-12:
            theta = np.arctan2(off_norm, max(diag_diff, 1e-15))
            print(f"\n  Mixing angle theta = arctan(cross/diag_diff):")
            print(f"    theta = {theta:.6f} rad = {np.degrees(theta):.4f} deg")
            print(f"    sin^2(theta) = {np.sin(theta)**2:.6f}")
            print(f"    Compare Weinberg: sin^2(theta_W) = 0.2312")
        else:
            theta = 0.0
            print(f"\n  Cross-charge coupling is ZERO. No mixing angle.")
    else:
        theta = None
        print(f"  Cannot identify charge sectors in B2 block.")
else:
    theta = 0.0
    print(f"  Ratio = {ratio:.10f} < 0.01: U(1)_7 preserved. No mixing angle needed.")

# ======================================================================
#  STEP 9: Jacobi identity check
# ======================================================================

print(f"\n{'='*78}")
print(f"Step 9: Jacobi identity cross-check")
print(f"{'='*78}")

# [iK_7, [D_K, H_j]] = [[iK_7, D_K], H_j] + [D_K, [iK_7, H_j]]
#                      = [0, H_j] + [D_K, [iK_7, H_j]]
#                      = [D_K, [iK_7, H_j]]
comm_K7_Hj = iK7 @ H_j_gen - H_j_gen @ iK7
jacobi_rhs = D_K @ comm_K7_Hj - comm_K7_Hj @ D_K
jacobi_lhs = comm_phi  # = [iK_7, [D_K, H_j]]
jacobi_err = norm(jacobi_lhs - jacobi_rhs, 'fro')
print(f"  Jacobi: [iK_7, [D_K, H_j]] = [D_K, [iK_7, H_j]]")
print(f"  ||LHS - RHS||_F = {jacobi_err:.2e}")
print(f"  ||[iK_7, H_j]||_F = {norm(comm_K7_Hj, 'fro'):.10f}")
print(f"  ||[D_K, [iK_7, H_j]]||_F = {norm(jacobi_rhs, 'fro'):.10f}")

if norm(comm_K7_Hj, 'fro') < 1e-12:
    print(f"\n  KEY FINDING: [iK_7, H_j] = 0")
    print(f"  => H_j commutes with iK_7 in the spinor representation")
    print(f"  => Inner fluctuation in H_j direction PRESERVES U(1)_7")
    print(f"  => [iK_7, D_phys] = phi * [iK_7, [D_K,H_j] + J[D_K,H_j]J^{{-1}}]")
    print(f"     = phi * ([D_K, [iK_7,H_j]] + J [D_K,[iK_7,H_j]] J^{{-1}})")
    print(f"     = phi * (0 + 0) = 0  IF [iK_7, H_j] = 0")
else:
    print(f"\n  [iK_7, H_j] != 0: inner fluctuation BREAKS U(1)_7")
    print(f"  The breaking comes from the A_F algebra element H_j not commuting")
    print(f"  with the isometry generator K_7 in the spinor representation.")

# Check [iK_7, H_j] for ALL generators
print(f"\n  [iK_7, gen] for all A_F generators:")
for name, gen in af_gens:
    c = iK7 @ gen - gen @ iK7
    c_norm = norm(c, 'fro')
    print(f"    [iK_7, {name}]: ||comm||_F = {c_norm:.10f}  {'COMMUTES' if c_norm < 1e-10 else 'DOES NOT COMMUTE'}")

# ======================================================================
#  GATE VERDICT
# ======================================================================

print(f"\n{'='*78}")
print(f"GATE K7-DPHYS-35: VERDICT")
print(f"{'='*78}")

print(f"\n  Configuration: tau={TAU}, phi={PHI_GAP} (gap-edge), direction=H_j")
print(f"  ||[iK_7, D_phys]||_F / ||D_phys||_F = {ratio:.10f}")

if ratio < 1e-10:
    verdict_str = "NEAR-ZERO: U(1)_7 PRESERVED exactly"
    verdict_short = "PRESERVED"
elif ratio < 0.01:
    verdict_str = f"NEAR-ZERO: U(1)_7 effectively preserved (ratio = {ratio:.2e})"
    verdict_short = "PRESERVED"
elif ratio < 0.1:
    verdict_str = f"WEAK BREAKING: ratio = {ratio:.6f}, U(1)_7 broken at O(phi*[K7,Hj])"
    verdict_short = "WEAK_BREAK"
else:
    verdict_str = f"STRONG BREAKING: ratio = {ratio:.6f}, extract mixing angle"
    verdict_short = "STRONG_BREAK"

print(f"  VERDICT: {verdict_str}")

if theta is not None and theta > 0.001:
    print(f"  Mixing angle: theta = {np.degrees(theta):.4f} deg, sin^2(theta) = {np.sin(theta)**2:.6f}")

# Physical interpretation
print(f"\n  PHYSICAL INTERPRETATION:")
if ratio < 0.01:
    print(f"  The U(1)_7 symmetry that survives the Jensen deformation of SU(3)")
    print(f"  ALSO survives inner fluctuations in the H_j direction.")
    print(f"  This means the U(1)_7 charge is a conserved quantum number of D_phys,")
    print(f"  not just D_K. This strengthens the selection rule structure.")
    print(f"  The B2 doublet splits into definite-charge sectors under D_phys.")
else:
    print(f"  The inner fluctuation in the H_j direction BREAKS the U(1)_7 symmetry.")
    print(f"  K_7 was a symmetry of D_K but is NOT a symmetry of D_phys.")
    print(f"  This is physically expected: inner fluctuations (Higgs field) typically")
    print(f"  break gauge symmetries. The ratio {ratio:.6f} measures the breaking strength.")
    if theta is not None and theta > 0.001:
        print(f"  The mixing angle theta = {np.degrees(theta):.4f} deg is a prediction")
        print(f"  for the electroweak-analog mixing in this NCG framework.")

# ======================================================================
#  SAVE
# ======================================================================

save_dict = {
    'tau': TAU,
    'phi_gap': PHI_GAP,
    'ratio': ratio,
    'comm_norm': comm_phys_frob,
    'dphys_norm': Dphys_frob,
    'comm_A_norm': comm_A_frob,
    'evals_DK': evals_DK,
    'evals_phys': evals_phys,
    'phi_values': phi_values,
    'ratios_vs_phi': ratios,
    'comm_norms_vs_phi': comm_norms,
    'dphys_norms_vs_phi': dphys_norms,
    'verdict': verdict_short,
    'gen_names': np.array([name for name, _ in af_gens], dtype='U20'),
    'gen_ratios': np.array([gen_results.get(name, {}).get('ratio', 0.0) for name, _ in af_gens]),
    'gen_broken': np.array([gen_results.get(name, {}).get('broken', False) for name, _ in af_gens]),
}
if theta is not None:
    save_dict['mixing_angle_rad'] = theta
    save_dict['mixing_angle_deg'] = np.degrees(theta)
    save_dict['sin2_theta'] = np.sin(theta)**2

OUT_NPZ = os.path.join(SCRIPT_DIR, 's35_k7_dphys.npz')
np.savez_compressed(OUT_NPZ, **save_dict)
print(f"\n  Data saved: {OUT_NPZ}")

# ======================================================================
#  PLOT
# ======================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle(f'K7-DPHYS-35: [iK_7, D_phys] at tau={TAU}, phi={PHI_GAP}\n'
             f'Verdict: {verdict_str}', fontsize=12, fontweight='bold')

# Panel (a): Ratio vs phi
ax = axes[0, 0]
ax.plot(phi_values, ratios, 'b-o', markersize=3, lw=1.5)
ax.axhline(0.01, color='g', ls='--', alpha=0.6, label='threshold 0.01')
ax.axhline(0.1, color='r', ls='--', alpha=0.6, label='threshold 0.1')
ax.axvline(PHI_GAP, color='orange', ls=':', alpha=0.7, label=f'phi_gap={PHI_GAP}')
ax.set_xlabel('phi amplitude')
ax.set_ylabel('||[iK_7, D_phys]|| / ||D_phys||')
ax.set_title('(a) U(1)_7 breaking vs fluctuation amplitude')
ax.legend(fontsize=8)

# Panel (b): Per-generator ratios
ax = axes[0, 1]
names = [name for name, _ in af_gens]
r_vals = [gen_results.get(name, {}).get('ratio', 0.0) for name in names]
colors = ['red' if gen_results.get(n, {}).get('broken', False) else 'green' for n in names]
ax.barh(range(len(names)), r_vals, color=colors, edgecolor='k', lw=0.5)
ax.set_yticks(range(len(names)))
ax.set_yticklabels(names, fontsize=7)
ax.axvline(0.01, color='g', ls='--', alpha=0.6)
ax.set_xlabel('||[iK_7, D_phys]|| / ||D_phys||')
ax.set_title(f'(b) Per-generator U(1)_7 breaking at phi={PHI_GAP}')

# Panel (c): D_K vs D_phys eigenvalues
ax = axes[1, 0]
ax.plot(range(16), evals_DK, 'bo', markersize=6, label='D_K', zorder=5)
ax.plot(range(16), evals_phys, 'r^', markersize=6, label='D_phys (H_j)', zorder=5)
for i in range(16):
    ax.plot([i, i], [evals_DK[i], evals_phys[i]], 'k-', lw=0.5, alpha=0.5)
ax.set_xlabel('Mode index (sorted)')
ax.set_ylabel('Eigenvalue')
ax.set_title('(c) Eigenvalue shift under inner fluctuation')
ax.legend(fontsize=8)
ax.axhline(0, color='gray', ls='--', alpha=0.3)

# Panel (d): Commutator matrix heatmap in D_phys eigenbasis
ax = axes[1, 1]
im = ax.imshow(np.abs(comm_eig), cmap='hot', aspect='auto', interpolation='none')
plt.colorbar(im, ax=ax, label='|[iK_7, D_phys]|')
ax.set_xlabel('Mode index')
ax.set_ylabel('Mode index')
ax.set_title('(d) |[iK_7, D_phys]| in D_phys eigenbasis')

plt.tight_layout()
OUT_PNG = os.path.join(SCRIPT_DIR, 's35_k7_dphys.png')
plt.savefig(OUT_PNG, dpi=150)
print(f"  Plot saved: {OUT_PNG}")

elapsed = time.time() - t0
print(f"\n  Total runtime: {elapsed:.1f}s")

print(f"\n  GATE K7-DPHYS-35: {verdict_str}")
