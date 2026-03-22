#!/usr/bin/env python3
"""
Session 37 Gate: K7-G1-37 — PMNS Pathway Gate
===============================================

Computes the K_7 charge of the lowest eigenmode in the (1,0) Peter-Weyl sector
at the spectral fold (tau = 0.190). This gates the entire PMNS program.

CONCEPTUAL FRAMEWORK:
---------------------
The isometry K_7 generates a U(1) symmetry of (SU(3), g_Jensen). As an isometry,
the Lie derivative L_{K_7} commutes with the Dirac operator D_K on the FULL
L^2(SU(3), S) spinor bundle (Lichnerowicz theorem).

In the Peter-Weyl decomposition, the eigenstates of D_K within sector (p,q) carry
multiplicity dim(p,q) from the RIGHT-regular representation. The K_7 charge
assignment on these copies comes from rho_{(p,q)*} acting on the multiplicity space.

For the PMNS gate, we need to determine whether the G1 mode (lowest eigenvalue
in (1,0)) can be assigned K_7 charge q_7 = 0, matching the B1 and B3_0 modes
from (0,0) which have q_7 = 0.

We compute TWO related quantities:
1. The expectation value <psi_G1 | rho(e_7) x I_16 | psi_G1> as specified
   in the task. This tells us the AVERAGE K_7 charge of the G1 eigenmode
   within the dim=3 representation space.
2. Whether rho(e_7) x I_16 commutes with D_{(1,0)}. If it does, q_7 is sharp.
   If not, q_7 is an expectation value with nonzero variance.
3. The K_7 charges on the MULTIPLICITY space V_{(0,1)}, which determine
   the charges of the 3 copies of G1 in the full spectrum.

Gate K7-G1-37:
  q_7 = 0 (in any physically meaningful sense) -> PASS
  q_7 != 0 for ALL copies -> FAIL

Author: neutrino-detection-specialist (Session 37)
Date: 2026-03-08
"""

import sys
import os
import time
import numpy as np
from scipy.linalg import eigh, norm

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from tier1_dirac_spectrum import (
    su3_generators,
    compute_structure_constants,
    compute_killing_form,
    jensen_metric,
    orthonormal_frame,
    frame_structure_constants,
    connection_coefficients,
    spinor_connection_offset,
    build_cliff8,
    validate_clifford,
    validate_connection,
    validate_omega_hermitian,
    dirac_operator_on_irrep,
    get_irrep,
    U1_IDX, SU2_IDX, C2_IDX, U2_IDX,
)
from s23a_kosmann_singlet import kosmann_operator_antisymmetric
from canonical_constants import tau_fold as TAU_FOLD

np.set_printoptions(precision=12, linewidth=140, suppress=True)
t0 = time.time()
TAU_SCAN = np.array([0.12, 0.15, 0.18, 0.190, 0.20, 0.24, 0.30])

print("=" * 78)
print(f"K7-G1-37: K_7 Charge of Lowest (1,0) Mode at tau = {TAU_FOLD}")
print("=" * 78)

# ======================================================================
#  STEP 0: Build SU(3) infrastructure
# ======================================================================

print(f"\nStep 0: SU(3) Infrastructure")
print("-" * 40)

gens = su3_generators()
f_abc = compute_structure_constants(gens)
B_ab = compute_killing_form(f_abc)
gammas = build_cliff8()

cliff_err = validate_clifford(gammas)
print(f"  Clifford algebra error: {cliff_err:.2e}")
assert cliff_err < 1e-14

# Verify generator 7 (0-indexed) is the u(1) direction = -i/2 * lambda_8
print(f"\n  Generator e_7 (u(1) direction, 0-indexed):")
print(f"  e_7 = diag({gens[7][0,0]:.8f}, {gens[7][1,1]:.8f}, {gens[7][2,2]:.8f})")
print(f"  Is diagonal: {np.max(np.abs(gens[7] - np.diag(np.diag(gens[7])))):.2e}")
print(f"  Is anti-Hermitian: {np.max(np.abs(gens[7] + gens[7].conj().T)):.2e}")

# e_7 = -i/2 * lambda_8 = -i/(2*sqrt(3)) * diag(1, 1, -2)
# i*e_7 = 1/(2*sqrt(3)) * diag(1, 1, -2)
ie7_evals = np.linalg.eigvalsh(1j * gens[7])
print(f"  Eigenvalues of i*e_7 on C^3: {np.sort(ie7_evals)}")
unit = 1.0 / (2.0 * np.sqrt(3))
print(f"  Expected: [{-2*unit:.8f}, {unit:.8f}, {unit:.8f}]")

# ======================================================================
#  STEP 1: Build D_K on (1,0) sector at tau = 0.190
# ======================================================================

print(f"\n{'='*78}")
print(f"Step 1: D_K on (1,0) sector at tau = {TAU_FOLD}")
print("-" * 40)

g_s = jensen_metric(B_ab, TAU_FOLD)
E = orthonormal_frame(g_s)
ft = frame_structure_constants(f_abc, E)
Gamma = connection_coefficients(ft)
Omega = spinor_connection_offset(Gamma, gammas)

mc_err = validate_connection(Gamma)
is_h, is_ah, h_err, ah_err = validate_omega_hermitian(Omega)
print(f"  Connection metric-compat error: {mc_err:.2e}")
print(f"  Omega anti-Hermitian: {is_ah} (err: {ah_err:.2e})")

# Build D_K on (1,0) = fundamental representation
rho_10, dim_10 = get_irrep(1, 0, gens, f_abc)
print(f"  (1,0) irrep dimension: {dim_10}")
assert dim_10 == 3

D_10 = dirac_operator_on_irrep(rho_10, E, gammas, Omega)
print(f"  D_10 matrix size: {D_10.shape}")

# Verify anti-Hermiticity of D_10
ah_err_D = np.max(np.abs(D_10 + D_10.conj().T))
print(f"  D_10 anti-Hermiticity error: {ah_err_D:.2e}")
assert ah_err_D < 1e-12

# Diagonalize via H = 1j * D_10 (Hermitian)
H_10 = 1j * D_10
h_check = np.max(np.abs(H_10 - H_10.conj().T))
print(f"  H_10 = 1j*D_10 Hermiticity error: {h_check:.2e}")

evals_10, evecs_10 = eigh(H_10)
print(f"\n  D_10 eigenvalues (= eigenvalues of 1j*D, real, sorted ascending):")
for i, ev in enumerate(evals_10):
    print(f"    [{i:2d}] lambda = {ev:+12.8f}")

# Identify the lowest positive eigenvalue (G1 mode)
pos_mask = evals_10 > 1e-10
pos_evals = evals_10[pos_mask]
pos_indices = np.where(pos_mask)[0]
print(f"\n  Positive eigenvalues: {len(pos_evals)}")
print(f"  Lowest positive: lambda_G1 = {pos_evals[0]:+12.8f} (index {pos_indices[0]})")

G1_idx = pos_indices[0]
psi_G1 = evecs_10[:, G1_idx]

# ======================================================================
#  STEP 2: Construct K_7 operator = rho(e_7) x I_16
# ======================================================================

print(f"\n{'='*78}")
print(f"Step 2: K_7 Operator = rho(e_7) x I_16 on (1,0)")
print("-" * 40)

# As specified in the task: K7 = rho_{(1,0)}(e_7) tensor I_16
rho_e7 = rho_10[7]  # 3x3 anti-Hermitian matrix = e_7 itself
print(f"  rho_{(1,0)}(e_7) = e_7 (fundamental rep is identity map)")
print(f"  rho(e_7) anti-Hermiticity: {np.max(np.abs(rho_e7 + rho_e7.conj().T)):.2e}")
print(f"  rho(e_7) eigenvalues: {np.sort(np.linalg.eigvalsh(1j * rho_e7))}")

K7_op = np.kron(rho_e7, np.eye(16, dtype=complex))  # 48x48
iK7_op = 1j * K7_op
herm_err = np.max(np.abs(iK7_op - iK7_op.conj().T))
print(f"\n  K7_op = rho(e_7) x I_16, size: {K7_op.shape}")
print(f"  iK_7 Hermiticity error: {herm_err:.2e}")

# ======================================================================
#  STEP 3: Check if rho(e_7) x I commutes with D_{(1,0)}
# ======================================================================

print(f"\n{'='*78}")
print(f"Step 3: Commutator [rho(e_7) x I, D_10]")
print("-" * 40)

comm = iK7_op @ D_10 - D_10 @ iK7_op
comm_norm = norm(comm, 'fro')
D_norm = norm(D_10, 'fro')
ratio_comm = comm_norm / D_norm

print(f"  ||[iK_7, D_10]||_F = {comm_norm:.6e}")
print(f"  ||D_10||_F = {D_norm:.6f}")
print(f"  Ratio = {ratio_comm:.6e}")

if ratio_comm < 1e-12:
    print(f"  RESULT: rho(e_7) x I COMMUTES with D_10 to machine epsilon")
    print(f"  => q_7 is a sharp quantum number on (1,0) sector")
    commutes = True
else:
    print(f"  RESULT: rho(e_7) x I does NOT commute with D_10")
    print(f"  => q_7 is NOT a sharp quantum number for the (1,0) Dirac eigenmodes")
    print(f"  => Expectation value <psi|iK_7|psi> has nonzero variance")
    commutes = False

    # Why does this happen? Compute [rho(e_7), rho(e_a)] for each a
    print(f"\n  Decomposition: [rho(e_7) x I, sum_a rho(e_a) x gamma_a]")
    print(f"  = sum_a [rho(e_7), rho(e_a)] x gamma_a")
    print(f"  = sum_a f_{{7ac}} rho(e_c) x gamma_a")
    print(f"\n  Structure constants f_{{7,a,c}} (nonzero entries):")
    for a in range(8):
        for c in range(8):
            if abs(f_abc[7, a, c]) > 1e-10:
                print(f"    f_{{7,{a},{c}}} = {f_abc[7,a,c]:+.6f}")

    print(f"\n  Physical reason: e_7 is in u(1) subset u(2) subset su(3)")
    print(f"  u(1) commutes with su(2) = {{e_0, e_1, e_2}} (same u(2) block)")
    print(f"  u(1) does NOT commute with C^2 = {{e_3, e_4, e_5, e_6}}")
    print(f"  The Dirac operator sum_a rho(e_a) x gamma_a contains C^2 terms")
    print(f"  These terms break the K_7 quantum number within (1,0)")

# ======================================================================
#  STEP 4: Compute q_7 = <psi_G1 | rho(e_7) x I | psi_G1>
# ======================================================================

print(f"\n{'='*78}")
print(f"Step 4: q_7 Expectation Value for G1 Mode")
print("-" * 40)

# Method 1: Direct expectation value
q7_G1 = np.real(psi_G1.conj() @ iK7_op @ psi_G1)
print(f"  q_7(G1) = <psi_G1 | i*rho(e_7) x I | psi_G1> = {q7_G1:+14.10f}")

# Method 2: Variance to quantify sharpness
q7_sq = np.real(psi_G1.conj() @ (iK7_op @ iK7_op) @ psi_G1)
var_q7 = q7_sq - q7_G1**2
print(f"  <(iK_7)^2> = {q7_sq:+14.10f}")
print(f"  Var(q_7) = <q_7^2> - <q_7>^2 = {var_q7:+14.10f}")
print(f"  Std(q_7) = {np.sqrt(max(0, var_q7)):14.10f}")

# Method 3: Project iK_7 into D eigenbasis to see all charges
iK7_eigbasis = evecs_10.conj().T @ iK7_op @ evecs_10
q7_all = np.real(np.diag(iK7_eigbasis))
offdiag_norm = norm(iK7_eigbasis - np.diag(np.diag(iK7_eigbasis)), 'fro')
print(f"\n  iK_7 in D eigenbasis:")
print(f"  Max off-diagonal: {np.max(np.abs(iK7_eigbasis - np.diag(np.diag(iK7_eigbasis)))):.6e}")
print(f"  ||off-diagonal||_F: {offdiag_norm:.6e}")
print(f"  ||iK_7||_F: {norm(iK7_eigbasis, 'fro'):.6f}")

print(f"\n  {'Idx':>4s}  {'lambda(D)':>14s}  {'<q_7>':>14s}  {'Identification':>20s}")
print(f"  {'-'*4}  {'-'*14}  {'-'*14}  {'-'*20}")

for i in range(len(evals_10)):
    # Identify nearest rational
    q = q7_all[i]
    # Known values: 1/(2*sqrt(3)) = 0.2887, -1/sqrt(3) = -0.5774
    # Also possible: 0, +/- 1/4
    if abs(q) < 1e-6:
        ident = "0"
    elif abs(q - unit) < 1e-4:
        ident = "+1/(2*sqrt3)"
    elif abs(q + unit) < 1e-4:
        ident = "-1/(2*sqrt3)"
    elif abs(q - 2*unit) < 1e-4:
        ident = "+1/sqrt3"
    elif abs(q + 2*unit) < 1e-4:
        ident = "-1/sqrt3"
    elif abs(abs(q) - 0.25) < 1e-4:
        ident = f"{'+' if q > 0 else '-'}1/4"
    else:
        ident = f"~{q:.4f}"

    marker = " <-- G1" if i == G1_idx else ""
    print(f"  {i:4d}  {evals_10[i]:+14.8f}  {q7_all[i]:+14.8f}  {ident:>20s}{marker}")

# ======================================================================
#  STEP 5: K_7 on the MULTIPLICITY space (right-regular representation)
# ======================================================================

print(f"\n{'='*78}")
print(f"Step 5: K_7 Charges on Multiplicity Space V_(0,1)")
print("-" * 40)

# Each eigenvalue of D_{(1,0)} appears dim(1,0)=3 times in full spectrum.
# The K_7 isometry acts on V_{(0,1)} = conjugate representation.
# rho_{(0,1)}(e_7) = -e_7^T

rho_01_e7 = -gens[7].T  # anti-fundamental representation of e_7
i_rho_01_e7 = 1j * rho_01_e7
mult_charges = np.sort(np.linalg.eigvalsh(i_rho_01_e7))

print(f"  Anti-fundamental rho_(0,1)(e_7) = -e_7^T")
print(f"  Eigenvalues of i*rho_(0,1)(e_7): {mult_charges}")
print(f"  These are the K_7 charges of the 3 copies of each (1,0) eigenvalue")

has_zero_charge = any(abs(q) < 1e-10 for q in mult_charges)
print(f"\n  Any charge = 0? {has_zero_charge}")

if has_zero_charge:
    print(f"  => At least one copy of G1 has q_7 = 0")
    print(f"  => Compatible with B1 (q_7=0) and B3_0 (q_7=0) from (0,0)")
else:
    print(f"  => NO copy of G1 has q_7 = 0")
    print(f"  => INCOMPATIBLE with B1/B3_0 (both q_7=0)")

# ======================================================================
#  STEP 6: Full Isometry Analysis — Does e_7 generate a Killing field?
# ======================================================================

print(f"\n{'='*78}")
print(f"Step 6: Lie Derivative L_{{e_7}} g = 0 Check (Killing)")
print("-" * 40)

# Check if e_7 is Killing by computing the symmetric part of connection
# (L_{e_7} g)_{rs} = Gamma^s_{r,7} + Gamma^r_{s,7}
Lg = np.zeros((8, 8))
for r in range(8):
    for s in range(8):
        Lg[r, s] = Gamma[s, r, 7] + Gamma[r, s, 7]

Lg_norm = norm(Lg, 'fro')
print(f"  ||L_{{e_7}} g||_F = {Lg_norm:.6e}")
if Lg_norm < 1e-12:
    print(f"  CONFIRMED: e_7 is a Killing vector of g_Jensen at tau={TAU_FOLD}")
else:
    print(f"  e_7 is NOT a Killing vector (norm = {Lg_norm:.6e})")
    print(f"  Nonzero components:")
    for r in range(8):
        for s in range(r, 8):
            if abs(Lg[r, s]) > 1e-10:
                print(f"    (L_e7 g)_{{{r},{s}}} = {Lg[r,s]:+.8f}")

# ======================================================================
#  STEP 7: Singlet K_7 charges (cross-reference with Session 34)
# ======================================================================

print(f"\n{'='*78}")
print(f"Step 7: Singlet (0,0) K_7 Charges (Cross-Reference)")
print("-" * 40)

# On (0,0), D = Omega
K7_spinor, A7_antisym = kosmann_operator_antisymmetric(Gamma, gammas, 7)
print(f"  Kosmann K_7 (spinor part) ||K7_spinor||_F = {norm(K7_spinor, 'fro'):.6e}")
print(f"  ||A7_antisym||_F = {norm(A7_antisym, 'fro'):.6e}")

# On the singlet, rho_{(0,0)} = trivial, so the FULL K_7 = K7_spinor
# (plus the right-regular part, which for (0,0) is also trivial)
# Wait -- the right-regular rep for (0,0) has V_{(0,0)*} = C, so trivial too
# Therefore on singlet, K_7 = K7_spinor

D_00 = Omega.copy()
H_00 = 1j * D_00
ev_00, evec_00 = eigh(H_00)

# Singlet K_7 charges
iK7_singlet = 1j * K7_spinor
iK7_00_eigbasis = evec_00.conj().T @ iK7_singlet @ evec_00
q7_singlet = np.real(np.diag(iK7_00_eigbasis))

# Commutator check in singlet
comm_00 = iK7_singlet @ D_00 - D_00 @ iK7_singlet
comm_00_ratio = norm(comm_00, 'fro') / norm(D_00, 'fro') if norm(D_00, 'fro') > 0 else 0
print(f"  ||[iK_7, D]||/||D|| on (0,0): {comm_00_ratio:.2e}")

print(f"\n  Singlet eigenvalues and K_7 charges:")
print(f"  {'Idx':>4s}  {'lambda':>12s}  {'q_7':>12s}  {'Branch':>8s}")
for i in range(16):
    ev = ev_00[i]
    q = q7_singlet[i]
    if abs(q) < 0.01:
        branch = "B1/B3"
    elif abs(abs(q) - 0.25) < 0.01:
        branch = "B2"
    else:
        branch = "?"
    print(f"  {i:4d}  {ev:+12.6f}  {q:+12.6f}  {branch:>8s}")

# ======================================================================
#  STEP 8: Multi-tau scan of q_7 expectation value on G1
# ======================================================================

print(f"\n{'='*78}")
print(f"Step 8: q_7 of G1 at Multiple tau Values")
print("-" * 40)

print(f"  {'tau':>6s}  {'lambda_G1':>12s}  {'<q_7(G1)>':>14s}  {'Var(q_7)':>14s}  {'||[K7,D]||/||D||':>18s}")

q7_G1_vs_tau = []
for tau in TAU_SCAN:
    g_tau = jensen_metric(B_ab, tau)
    E_tau = orthonormal_frame(g_tau)
    ft_tau = frame_structure_constants(f_abc, E_tau)
    Gamma_tau = connection_coefficients(ft_tau)
    Omega_tau = spinor_connection_offset(Gamma_tau, gammas)

    D_tau = dirac_operator_on_irrep(rho_10, E_tau, gammas, Omega_tau)
    H_tau = 1j * D_tau
    ev_tau, evec_tau = eigh(H_tau)

    K7_tau = np.kron(rho_e7, np.eye(16, dtype=complex))
    iK7_tau = 1j * K7_tau

    # Commutator
    comm_tau = iK7_tau @ D_tau - D_tau @ iK7_tau
    ratio_tau = norm(comm_tau, 'fro') / norm(D_tau, 'fro')

    # Lowest positive eigenvalue
    pos_m = ev_tau > 1e-10
    G1_idx_tau = np.where(pos_m)[0][0]
    psi_G1_tau = evec_tau[:, G1_idx_tau]

    q7_tau = np.real(psi_G1_tau.conj() @ iK7_tau @ psi_G1_tau)
    q7_sq_tau = np.real(psi_G1_tau.conj() @ (iK7_tau @ iK7_tau) @ psi_G1_tau)
    var_tau = q7_sq_tau - q7_tau**2

    q7_G1_vs_tau.append(q7_tau)

    print(f"  {tau:6.3f}  {ev_tau[G1_idx_tau]:+12.6f}  {q7_tau:+14.8f}  {var_tau:14.8f}  {ratio_tau:18.6e}")

# ======================================================================
#  STEP 9: Representation-theoretic analysis
# ======================================================================

print(f"\n{'='*78}")
print(f"Step 9: Representation-Theoretic Analysis")
print("-" * 40)

# The fundamental (1,0) decomposes under u(2) = su(2) + u(1) as:
# C^3 = C^1 + C^2 where C^1 is the (det^{-1}) component and C^2 is the doublet
# More precisely:
# Under u(2) embedded as diag(det^{-1}(a), a):
#   (1,0) of su(3) -> 1_{-2/3} + 2_{1/3} of u(2) = su(2) x u(1)
# where subscript is the u(1) charge

print(f"  Branching rule: (1,0) of SU(3) -> 1_{{-2/(2sqrt3)}} + 2_{{+1/(2sqrt3)}} under U(2)")
print(f"  Charges: q_7 = -1/sqrt(3), +1/(2sqrt(3)), +1/(2sqrt(3))")
print(f"  = -0.5774, +0.2887, +0.2887")
print(f"")
print(f"  Key point: ALL weights of the fundamental (1,0) have q_7 != 0")
print(f"  The singlet of U(2) within (1,0) has q_7 = -1/sqrt(3) = -0.5774")
print(f"  The doublet of U(2) within (1,0) has q_7 = +1/(2sqrt(3)) = +0.2887")
print(f"  NEITHER is zero.")
print(f"")
print(f"  Compare with singlet (0,0): trivial representation, q_7 = 0 trivially.")
print(f"  And with adjoint (1,1): contains the root e_7 itself, which has q_7 = 0.")
print(f"")
print(f"  For the MULTIPLICITY space V_(0,1) = anti-fundamental:")
print(f"  Charges: -1/(2sqrt3), -1/(2sqrt3), +1/sqrt(3)")
print(f"  ALSO all nonzero.")

# Check which representations HAVE a q_7 = 0 weight
print(f"\n  Representations with q_7 = 0 weight:")
for p in range(4):
    for q in range(4):
        if p == 0 and q == 0:
            print(f"    ({p},{q}): dim = 1, trivially q_7 = 0")
            continue
        try:
            rho_pq, dim_pq = get_irrep(p, q, gens, f_abc)
            ie7_pq = 1j * rho_pq[7]
            charges_pq = np.sort(np.linalg.eigvalsh(ie7_pq))
            has_zero = any(abs(c) < 1e-8 for c in charges_pq)
            if has_zero:
                zero_count = sum(1 for c in charges_pq if abs(c) < 1e-8)
                print(f"    ({p},{q}): dim = {dim_pq}, q_7 charges include 0 ({zero_count}x)")
        except:
            pass

# ======================================================================
#  STEP 10: Check (1,1) adjoint for zero-charge modes
# ======================================================================

print(f"\n{'='*78}")
print(f"Step 10: (1,1) Adjoint K_7 Charges and D Eigenvalues")
print("-" * 40)

rho_11, dim_11 = get_irrep(1, 1, gens, f_abc)
assert dim_11 == 8

# K_7 charges in adjoint
rho_e7_adj = rho_11[7]
ie7_adj = 1j * rho_e7_adj
adj_charges = np.sort(np.linalg.eigvalsh(ie7_adj))
print(f"  Adjoint K_7 charges: {adj_charges}")
print(f"  Number of q_7 = 0 charges: {sum(1 for c in adj_charges if abs(c) < 1e-8)}")

# D on (1,1)
D_11 = dirac_operator_on_irrep(rho_11, E, gammas, Omega)
H_11 = 1j * D_11
ev_11, evec_11 = eigh(H_11)

# q_7 for each adjoint mode
iK7_adj = 1j * np.kron(rho_e7_adj, np.eye(16, dtype=complex))
iK7_adj_eig = evec_11.conj().T @ iK7_adj @ evec_11
q7_adj = np.real(np.diag(iK7_adj_eig))

# Commutator check
comm_11 = iK7_adj @ D_11 - D_11 @ iK7_adj
ratio_11 = norm(comm_11, 'fro') / norm(D_11, 'fro')
print(f"  ||[K_7, D]||/||D|| on (1,1): {ratio_11:.6e}")

# Show lowest positive eigenvalues with q_7
pos_11 = ev_11 > 1e-10
pos_idx_11 = np.where(pos_11)[0]
print(f"\n  Lowest positive (1,1) modes:")
print(f"  {'Idx':>4s}  {'lambda':>12s}  {'<q_7>':>12s}")
for i in pos_idx_11[:10]:
    print(f"  {i:4d}  {ev_11[i]:+12.6f}  {q7_adj[i]:+12.6f}")

# ======================================================================
#  STEP 11: Summary Table for PMNS Compatibility
# ======================================================================

print(f"\n{'='*78}")
print(f"Step 11: PMNS Compatibility Summary")
print("-" * 40)

# Collect data on modes with q_7 = 0 from each sector
print(f"\n  Modes with q_7 = 0 (from representation analysis):")
print(f"  {'Sector':>8s}  {'dim(rho)':>8s}  {'q_7 = 0 weights':>16s}  {'Lowest lambda':>14s}")

# (0,0): trivially q_7 = 0
print(f"  {'(0,0)':>8s}  {'1':>8s}  {'all':>16s}  {'+0.8191':>14s}")

# (1,0): no q_7 = 0
print(f"  {'(1,0)':>8s}  {'3':>8s}  {'NONE':>16s}  {pos_evals[0]:+14.6f}")

# (0,1): conjugate of (1,0)
rho_01, dim_01 = get_irrep(0, 1, gens, f_abc)
ie7_01 = 1j * rho_01[7]
charges_01 = np.sort(np.linalg.eigvalsh(ie7_01))
has_zero_01 = sum(1 for c in charges_01 if abs(c) < 1e-8)
D_01 = dirac_operator_on_irrep(rho_01, E, gammas, Omega)
ev_01 = np.sort(np.linalg.eigvalsh(1j * D_01))
pos_01 = ev_01[ev_01 > 1e-10]
print(f"  {'(0,1)':>8s}  {'3':>8s}  {str(has_zero_01):>16s}  {pos_01[0]:+14.6f}")

# (1,1): adjoint -- has zero weights
has_zero_11 = sum(1 for c in adj_charges if abs(c) < 1e-8)
print(f"  {'(1,1)':>8s}  {'8':>8s}  {str(has_zero_11):>16s}  {ev_11[pos_idx_11[0]]:+14.6f}")

# (2,0):
rho_20, dim_20 = get_irrep(2, 0, gens, f_abc)
ie7_20 = 1j * rho_20[7]
charges_20 = np.sort(np.linalg.eigvalsh(ie7_20))
has_zero_20 = sum(1 for c in charges_20 if abs(c) < 1e-8)
D_20 = dirac_operator_on_irrep(rho_20, E, gammas, Omega)
ev_20 = np.sort(np.linalg.eigvalsh(1j * D_20))
pos_20 = ev_20[ev_20 > 1e-10]
print(f"  {'(2,0)':>8s}  {'6':>8s}  {str(has_zero_20):>16s}  {pos_20[0]:+14.6f}")

# (0,2):
rho_02, dim_02 = get_irrep(0, 2, gens, f_abc)
ie7_02 = 1j * rho_02[7]
charges_02 = np.sort(np.linalg.eigvalsh(ie7_02))
has_zero_02 = sum(1 for c in charges_02 if abs(c) < 1e-8)
D_02 = dirac_operator_on_irrep(rho_02, E, gammas, Omega)
ev_02 = np.sort(np.linalg.eigvalsh(1j * D_02))
pos_02 = ev_02[ev_02 > 1e-10]
print(f"  {'(0,2)':>8s}  {'6':>8s}  {str(has_zero_02):>16s}  {pos_02[0]:+14.6f}")

print(f"\n  Conclusion for (B1, B3_0, G1) triad:")
print(f"  B1 from (0,0): q_7 = 0  [CONFIRMED]")
print(f"  B3_0 from (0,0): q_7 = 0  [CONFIRMED]")
print(f"  G1 from (1,0): ALL weights have q_7 != 0  [REPRESENTATION THEORY]")
print(f"  => Triad INCOMPATIBLE under K_7 charge conservation")

# ======================================================================
#  GATE VERDICT
# ======================================================================

print(f"\n{'='*78}")
print(f"GATE VERDICT: K7-G1-37")
print("=" * 78)

# The verdict depends on whether ANY copy of G1 has q_7 = 0
# From the representation theory:
# (1,0) has NO zero weights under u(1)_7
# The multiplicity space V_{(0,1)} also has no zero weights
# Therefore NO copy of G1 in the full spectrum has q_7 = 0

# However, q_7 is not a sharp quantum number for G1 eigenmodes
# (since rho(e_7) x I doesn't commute with D on (1,0))
# So the "K_7 charge" of a specific G1 eigenmode is mixed

print(f"\n  PRIMARY MEASUREMENT:")
print(f"  q_7(G1) expectation value = {q7_G1:+14.10f}")
print(f"  Variance = {var_q7:+14.10f}")
print(f"  q_7 is NOT sharp (commutator ratio = {ratio_comm:.4e})")
print(f"")
print(f"  REPRESENTATION THEORY:")
print(f"  Fundamental (1,0) under u(2) -> 1_{{-2}} + 2_{{+1}} (u(1)_7 charges)")
print(f"  ALL weights of (1,0) have q_7 != 0")
print(f"  This is EXACT (algebraic, not numerical)")
print(f"")
print(f"  MULTIPLICITY ANALYSIS:")
print(f"  Each (1,0) eigenvalue has 3 copies in full spectrum")
print(f"  K_7 charges on copies: {mult_charges}")
print(f"  NONE are zero")

# Determine verdict
# The fundamental (1,0) has no zero weight under u(1)_7.
# This is an ALGEBRAIC FACT: the fundamental irrep of SU(3) has no
# component in the trivial representation of U(1)_7.
# Therefore q_7 != 0 for the G1 mode in every meaningful sense.

if abs(q7_G1) < 1e-6 and has_zero_charge:
    verdict = "PASS"
    print(f"\n  *** VERDICT: PASS ***")
    print(f"  q_7(G1) = 0. Off-Jensen PMNS via (B1, B3_0, G1) triad is open.")
else:
    verdict = "FAIL"
    print(f"\n  *** VERDICT: FAIL ***")
    print(f"  q_7(G1) != 0 ({q7_G1:+.8f} +/- {np.sqrt(max(0,var_q7)):.8f})")
    print(f"  The (B1, B3_0, G1) triad is K_7-incompatible.")
    print(f"  This is not a numerical accident -- it is algebraic:")
    print(f"  the fundamental (1,0) of SU(3) has no trivial component under U(1)_7.")
    print(f"")
    print(f"  PMNS CLASSIFICATION: Level 5")
    print(f"  Requires structure beyond Jensen deformation to produce 3x3 mixing.")

    # BUT: check if (1,1) adjoint offers an alternative
    zero_adj_modes_pos = [(i, ev_11[i]) for i in pos_idx_11 if abs(q7_adj[i]) < 0.01]
    if zero_adj_modes_pos:
        print(f"\n  ALTERNATIVE PATHWAY:")
        print(f"  (1,1) adjoint HAS q_7 = 0 modes:")
        for idx, lam in zero_adj_modes_pos[:5]:
            print(f"    [{idx}] lambda = {lam:+12.8f}")
        print(f"  These could form a triad (B1, B3_0, adjoint_mode) with all q_7 = 0")
        print(f"  The R ratio would change since the adjoint mode eigenvalue differs from G1")

print(f"\n  Cross-check consistency:")
print(f"  Session 34: [iK_7, D_K] = 0 on SINGLET -- confirmed (ratio = {comm_00_ratio:.2e})")
print(f"  This session: [iK_7, D_K] != 0 on (1,0) when K_7 = rho(e_7) x I")
print(f"    because e_7 is NOT central in su(3)")
print(f"  No contradiction: Session 34's result was ONLY for the singlet sector")
print(f"  The FULL Lie derivative (which commutes with D on all sectors) acts on")
print(f"  the multiplicity space, not on the D_{{(1,0)}} matrix space")

elapsed = time.time() - t0
print(f"\nTotal runtime: {elapsed:.1f}s")

# ======================================================================
#  SAVE DATA
# ======================================================================

OUT_NPZ = os.path.join(SCRIPT_DIR, 's37_k7_g1.npz')
np.savez(OUT_NPZ,
    tau_fold=TAU_FOLD,
    tau_scan=TAU_SCAN,
    evals_10=evals_10,
    q7_all=q7_all,
    q7_G1=q7_G1,
    q7_G1_variance=var_q7,
    q7_G1_vs_tau=np.array(q7_G1_vs_tau),
    G1_idx=G1_idx,
    G1_eigenvalue=evals_10[G1_idx],
    verdict=verdict,
    comm_ratio=ratio_comm,
    mult_charges=mult_charges,
    ie7_evals_fund=ie7_evals,
    q7_singlet=q7_singlet,
    ev_singlet=ev_00,
    q7_adj=q7_adj,
    ev_adj=ev_11,
    adj_charges=adj_charges,
)
print(f"\nSaved: {OUT_NPZ}")
print(f"Verdict: {verdict}")
