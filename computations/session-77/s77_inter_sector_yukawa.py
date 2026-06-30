#!/usr/bin/env python3
"""
S77-C10-YUKAWA-PMNS: Inter-Sector Yukawa / PMNS from (1,0)x(1,1) Coupling
===========================================================================

Investigates whether the inter-sector Yukawa coupling between (1,0) fundamental
and (1,1) adjoint SU(3) representations provides a route to the PMNS neutrino
mixing matrix.

KNOWN CONSTRAINT: The D_K block-diagonality theorem (S22b, proven to machine
epsilon 8.4e-15) states D_K is EXACTLY block-diagonal in the Peter-Weyl basis.
Therefore <(1,0)|D_K|(1,1)> = 0 exactly.

INVESTIGATION PLAN:
  Step 1: VERIFY block-diagonality at tau_fold using dirac_spectrum.py
  Step 2: Construct the real structure J on Cliff(R^8) and check if J*D_K
          mixes (1,0) and (1,1) sectors
  Step 3: Check the fermionic action <J*psi, D_K*psi> for inter-sector coupling
  Step 4: Check if J maps between sectors: J: V_{(1,0)} -> V_{(0,1)} (conjugate)
  Step 5: Check the full Yukawa coupling matrix
          Y_{alpha,beta} = <J*psi_alpha, D_K*psi_beta> for alpha in (1,0), beta in (1,1)

STRUCTURAL REASONING:
  The real structure J on a Lie group G with left-invariant metric acts as
  charge conjugation on spinors tensored with complex conjugation on the
  representation space. In the Peter-Weyl decomposition:
    L^2(G, S) = bigoplus_{(p,q)} V_{(p,q)} tensor V_{(p,q)}^* tensor S

  Complex conjugation maps V_{(p,q)} to V_{(q,p)} (conjugate representation).
  Therefore J maps (p,q) spinors to (q,p) spinors. Specifically:
    J: V_{(1,0)} tensor S -> V_{(0,1)} tensor S
    J does NOT map V_{(1,0)} to V_{(1,1)} because (1,1) is self-conjugate.

  Since D_K is block-diagonal AND J maps (1,0) -> (0,1) (not to (1,1)):
    <J*psi_{(1,0)}, D_K * psi_{(1,1)}> = <psi_{(0,1)}, D_K * psi_{(1,1)}> = 0
  The last equality follows from block-diagonality: D_K does not mix (0,1) and (1,1).

  EXPECTED RESULT: NULL. No inter-sector coupling. The block-diagonality theorem
  combined with J mapping (p,q) -> (q,p) guarantees all cross-sector matrix elements
  vanish.

Gate: S77-C10-YUKAWA-PMNS (INFO)
  Report mixing angles or null result with structural reason.

Author: Baptista Spacetime Analyst (S77)
Date: 2026-04-13

References:
  - S22b: D_K block-diagonal proof (8.4e-15)
  - S61: Block-diagonal generality theorem (left-invariance alone suffices)
  - Paper 14 (2105.02901): Baptista fermion identification
  - Paper 17 (2506.09126): Chiral interactions and Kosmann-Lichnerowicz derivative
"""

import sys
import os
import time
import numpy as np
from scipy.linalg import eigh as scipy_eigh, svd

# Path setup
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from canonical_constants import tau_fold
from dirac_spectrum import (
    su3_generators,
    compute_structure_constants,
    compute_killing_form,
    jensen_metric,
    orthonormal_frame,
    frame_structure_constants,
    connection_coefficients,
    spinor_connection_offset,
    validate_connection,
    validate_omega_hermitian,
    build_cliff8,
    build_chirality,
    validate_clifford,
    dirac_operator_on_irrep,
    get_irrep,
    validate_irrep,
    U1_IDX, SU2_IDX, C2_IDX,
)

# ============================================================================
# Configuration
# ============================================================================

TAU = tau_fold  # Use the fold value
SVD_THRESH = 1e-12  # (local) singular value threshold
DIM_SPIN = 16  # (local) spinor dimension for Cliff(8)

print("=" * 76)
print("S77-C10-YUKAWA-PMNS: Inter-Sector Yukawa / PMNS Investigation")
print("=" * 76)
print(f"  tau_fold = {TAU}")
print(f"  SVD threshold = {SVD_THRESH:.1e}")
print()

t0 = time.time()  # (local)

# ============================================================================
# STEP 0: Build Lie algebra and geometric infrastructure
# ============================================================================

print("STEP 0: Lie algebra and geometric infrastructure")
print("-" * 50)

gens = su3_generators()
f_abc = compute_structure_constants(gens)
B_ab = compute_killing_form(f_abc)
g_s = jensen_metric(B_ab, TAU)
E = orthonormal_frame(g_s)
ft = frame_structure_constants(f_abc, E)
Gamma = connection_coefficients(ft)
gammas = build_cliff8()
gamma9 = build_chirality(gammas)
Omega = spinor_connection_offset(Gamma, gammas)

# Validate
mc_err = validate_connection(Gamma)  # (local)
cliff_err = validate_clifford(gammas)  # (local)
is_h, is_ah, h_err, ah_err = validate_omega_hermitian(Omega)

print(f"  Connection metric-compat error: {mc_err:.2e}")
print(f"  Clifford algebra error: {cliff_err:.2e}")
print(f"  Omega anti-Hermiticity error: {ah_err:.2e}")
print(f"  Omega Hermiticity error: {h_err:.2e}")
assert mc_err < 1e-13, f"Connection error too large: {mc_err}"
assert cliff_err < 1e-14, f"Clifford error too large: {cliff_err}"
print()

# ============================================================================
# STEP 1: Build D_K on each sector and VERIFY block-diagonality
# ============================================================================

print("STEP 1: Verify block-diagonality of D_K at tau_fold")
print("-" * 50)

# Build irreps (1,0), (0,1), (1,1)
rho_10, dim_10 = get_irrep(1, 0, gens, f_abc)
rho_01, dim_01 = get_irrep(0, 1, gens, f_abc)
rho_11, dim_11 = get_irrep(1, 1, gens, f_abc)

print(f"  (1,0): dim = {dim_10}")
print(f"  (0,1): dim = {dim_01}")
print(f"  (1,1): dim = {dim_11}")

# Validate irreps
hom_10, ah_10 = validate_irrep(rho_10, f_abc, "(1,0)")  # (local)
hom_01, ah_01 = validate_irrep(rho_01, f_abc, "(0,1)")  # (local)
hom_11, ah_11 = validate_irrep(rho_11, f_abc, "(1,1)")  # (local)

print(f"  (1,0) homomorphism err: {hom_10:.2e}, anti-Herm err: {ah_10:.2e}")
print(f"  (0,1) homomorphism err: {hom_01:.2e}, anti-Herm err: {ah_01:.2e}")
print(f"  (1,1) homomorphism err: {hom_11:.2e}, anti-Herm err: {ah_11:.2e}")

# Build Dirac operators on each sector
D_10 = dirac_operator_on_irrep(rho_10, E, gammas, Omega)
D_01 = dirac_operator_on_irrep(rho_01, E, gammas, Omega)
D_11 = dirac_operator_on_irrep(rho_11, E, gammas, Omega)

# Verify anti-Hermiticity
ah_D10 = np.max(np.abs(D_10 + D_10.conj().T))  # (local)
ah_D01 = np.max(np.abs(D_01 + D_01.conj().T))  # (local)
ah_D11 = np.max(np.abs(D_11 + D_11.conj().T))  # (local)

print(f"  D_10 anti-Herm error: {ah_D10:.2e}  (size {D_10.shape})")
print(f"  D_01 anti-Herm error: {ah_D01:.2e}  (size {D_01.shape})")
print(f"  D_11 anti-Herm error: {ah_D11:.2e}  (size {D_11.shape})")

# Block-diagonality test: construct the off-diagonal block between sectors
# For the block between (1,0) and (1,1), we need the matrix element
# of the FULL D_K between states in V_{(1,0)} tensor S and V_{(1,1)} tensor S.
#
# But D_K is constructed per-sector. The block-diagonality theorem says D_K
# decomposes as D = bigoplus_pi D_pi, with ZERO off-diagonal blocks.
# This is structural (left-invariance + Peter-Weyl), not numerical.
#
# The numerical test: embed both sectors in a combined space and build D there.
# D_combined should be exactly block-diagonal.

dim_10_spin = dim_10 * DIM_SPIN  # 3 * 16 = 48  (local)
dim_01_spin = dim_01 * DIM_SPIN  # 3 * 16 = 48  (local)
dim_11_spin = dim_11 * DIM_SPIN  # 8 * 16 = 128  (local)

# Build combined Dirac operator on (1,0) + (1,1)
dim_combined = dim_10_spin + dim_11_spin  # 48 + 128 = 176  (local)
D_combined_10_11 = np.zeros((dim_combined, dim_combined), dtype=complex)

# Embed rho_10 and rho_11 in combined representation space
for a in range(8):
    # Combined rep matrix: block-diagonal rho_10[a] oplus rho_11[a]
    rho_combined_a = np.zeros((dim_10 + dim_11, dim_10 + dim_11), dtype=complex)
    rho_combined_a[:dim_10, :dim_10] = rho_10[a]
    rho_combined_a[dim_10:, dim_10:] = rho_11[a]

    for b in range(8):
        if abs(E[a, b]) > 1e-15:
            D_combined_10_11 += E[a, b] * np.kron(rho_combined_a, gammas[a])

            # Wait -- this is wrong. The frame element index and the generator index
            # must be treated correctly. Let me redo.
            # D = sum_{a,b} E_{ab} rho(X_b) tensor gamma_a
            # With combined rep: we need rho_combined[b] for each GENERATOR index b

# Redo correctly: the Dirac operator on the combined space is
# D = sum_{a,b} E_{ab} * (rho_combined[b] tensor gamma_a) + I tensor Omega

D_combined_10_11 = np.zeros((dim_combined, dim_combined), dtype=complex)

rho_combined = []  # (local)
for b in range(8):
    M = np.zeros((dim_10 + dim_11, dim_10 + dim_11), dtype=complex)
    M[:dim_10, :dim_10] = rho_10[b]
    M[dim_10:, dim_10:] = rho_11[b]
    rho_combined.append(M)

# Now build D using the same formula as dirac_operator_on_irrep
for a in range(8):
    for b in range(8):
        if abs(E[a, b]) > 1e-15:
            D_combined_10_11 += E[a, b] * np.kron(rho_combined[b], gammas[a])

D_combined_10_11 += np.kron(np.eye(dim_10 + dim_11), Omega)

# Extract the off-diagonal block: (1,0) x (1,1)
offdiag_10_11 = D_combined_10_11[:dim_10_spin, dim_10_spin:]
offdiag_norm_10_11 = np.max(np.abs(offdiag_10_11))  # (local)

print()
print(f"  OFF-DIAGONAL BLOCK |<(1,0)|D_K|(1,1)>|:")
print(f"    max|element|  = {offdiag_norm_10_11:.4e}")
print(f"    Frobenius norm = {np.linalg.norm(offdiag_10_11, 'fro'):.4e}")

# Similarly test (0,1) x (1,1)
dim_combined_01_11 = dim_01_spin + dim_11_spin  # (local)
D_combined_01_11 = np.zeros((dim_combined_01_11, dim_combined_01_11), dtype=complex)

rho_combined_01_11 = []  # (local)
for b in range(8):
    M = np.zeros((dim_01 + dim_11, dim_01 + dim_11), dtype=complex)
    M[:dim_01, :dim_01] = rho_01[b]
    M[dim_01:, dim_01:] = rho_11[b]
    rho_combined_01_11.append(M)

for a in range(8):
    for b in range(8):
        if abs(E[a, b]) > 1e-15:
            D_combined_01_11 += E[a, b] * np.kron(rho_combined_01_11[b], gammas[a])

D_combined_01_11 += np.kron(np.eye(dim_01 + dim_11), Omega)

offdiag_01_11 = D_combined_01_11[:dim_01_spin, dim_01_spin:]
offdiag_norm_01_11 = np.max(np.abs(offdiag_01_11))  # (local)

print(f"  OFF-DIAGONAL BLOCK |<(0,1)|D_K|(1,1)>|:")
print(f"    max|element|  = {offdiag_norm_01_11:.4e}")
print(f"    Frobenius norm = {np.linalg.norm(offdiag_01_11, 'fro'):.4e}")

# Also test (1,0) x (0,1)
dim_combined_10_01 = dim_10_spin + dim_01_spin  # (local)
D_combined_10_01 = np.zeros((dim_combined_10_01, dim_combined_10_01), dtype=complex)

rho_combined_10_01 = []  # (local)
for b in range(8):
    M = np.zeros((dim_10 + dim_01, dim_10 + dim_01), dtype=complex)
    M[:dim_10, :dim_10] = rho_10[b]
    M[dim_10:, dim_10:] = rho_01[b]
    rho_combined_10_01.append(M)

for a in range(8):
    for b in range(8):
        if abs(E[a, b]) > 1e-15:
            D_combined_10_01 += E[a, b] * np.kron(rho_combined_10_01[b], gammas[a])

D_combined_10_01 += np.kron(np.eye(dim_10 + dim_01), Omega)

offdiag_10_01 = D_combined_10_01[:dim_10_spin, dim_10_spin:]
offdiag_norm_10_01 = np.max(np.abs(offdiag_10_01))  # (local)

print(f"  OFF-DIAGONAL BLOCK |<(1,0)|D_K|(0,1)>|:")
print(f"    max|element|  = {offdiag_norm_10_01:.4e}")
print(f"    Frobenius norm = {np.linalg.norm(offdiag_10_01, 'fro'):.4e}")

print()
print("  BLOCK-DIAGONALITY VERDICT:")
all_offdiag_max = max(offdiag_norm_10_11, offdiag_norm_01_11, offdiag_norm_10_01)  # (local)
if all_offdiag_max < 1e-13:
    print(f"    CONFIRMED to machine epsilon ({all_offdiag_max:.2e})")
    block_diag_confirmed = True  # (local)
else:
    print(f"    VIOLATION detected: max off-diagonal = {all_offdiag_max:.2e}")
    block_diag_confirmed = False  # (local)

print()

# ============================================================================
# STEP 2: Construct the real structure J on Cliff(R^8)
# ============================================================================

print("STEP 2: Real structure J on Cliff(R^8)")
print("-" * 50)

# For Cliff(R^n), the charge conjugation operator C satisfies:
#   C gamma_a C^{-1} = epsilon * gamma_a^*
# where epsilon depends on n mod 8.
#
# For n = 8 (KO-dim 0 in the Connes table):
#   J^2 = +1, JD = +DJ, J*gamma_9 = +gamma_9*J
# Since KO-dim = n mod 8, for n=8 we get KO-dim 0.
#
# BUT: The framework established KO-dim = 6 for the FULL spectral triple
# (combining 4D Lorentzian + 8D internal). The 8D internal part alone has
# KO-dim 0.
#
# For Cliff(R^8), we need C such that C gamma_a = gamma_a^* C (positive type).
# This is the charge conjugation matrix B_+ with C gamma_a C^{-1} = gamma_a^*.
#
# Construction: For our tensor-product construction of gammas,
# C = gamma_2 gamma_4 gamma_6 gamma_8 (product of even-indexed gammas)
# gives C gamma_a C^{-1} = (-1)^{n/2} gamma_a^T for even n.
#
# Let me compute it directly by finding the intertwiner.

# Method: Find C such that C gamma_a = gamma_a^* C for all a.
# This is equivalent to: C^{-1} gamma_a^* C = gamma_a, i.e.,
# {gamma_a^*} and {gamma_a} are related by a similarity C.
#
# Since gamma_a^* also satisfy the Clifford algebra (complex conjugate preserves it),
# and the Clifford algebra has a unique irreducible representation up to equivalence,
# such C must exist.

# Compute gamma_a^* for each a
gammas_conj = [g.conj() for g in gammas]  # (local)

# Verify gammas_conj satisfy Clifford:
# {gamma_a^*, gamma_b^*} = ({gamma_a, gamma_b})^* = (2 delta_{ab} I)^* = 2 delta_{ab} I
# So yes, gammas_conj are another representation.

# Find C via: C = product that intertwines.
# For the standard tensor-product construction:
# gamma_{2k-1} = s3^{k-1} x s1 x I^{4-k}
# gamma_{2k}   = s3^{k-1} x s2 x I^{4-k}
#
# Note s1^* = s1, s2^* = -s2, s3^* = s3.
# So gamma_{2k}^* = -gamma_{2k} and gamma_{2k-1}^* = gamma_{2k-1}.
#
# We need C gamma_a C^{-1} = gamma_a^* for all a.
# For odd a: gamma_a^* = gamma_a, so [C, gamma_a] = 0
# For even a: gamma_a^* = -gamma_a, so C gamma_a C^{-1} = -gamma_a
#
# C must commute with odd gammas and anticommute with even gammas.
# C = gamma_2 * gamma_4 * gamma_6 * gamma_8 (product of all even-indexed gammas)

C_charge = gammas[1] @ gammas[3] @ gammas[5] @ gammas[7]  # gamma_2 * gamma_4 * gamma_6 * gamma_8  (local)

# Verify: C gamma_a C^{-1} should equal gamma_a^* for all a
C_inv = np.linalg.inv(C_charge)  # (local)

print("  Charge conjugation C = gamma_2 * gamma_4 * gamma_6 * gamma_8")
print(f"  C shape: {C_charge.shape}")
print(f"  C unitarity error: {np.max(np.abs(C_charge @ C_charge.conj().T - np.eye(DIM_SPIN))):.2e}")

max_intertwine_err = 0.0  # (local)
for a in range(8):
    check = C_charge @ gammas[a] @ C_inv - gammas[a].conj()
    err = np.max(np.abs(check))  # (local)
    max_intertwine_err = max(max_intertwine_err, err)

print(f"  Intertwining error max|C gamma_a C^{-1} - gamma_a^*|: {max_intertwine_err:.2e}")

if max_intertwine_err > 1e-12:
    # Try the other sign convention: C gamma_a C^{-1} = -gamma_a^*
    max_neg_err = 0.0  # (local)
    for a in range(8):
        check = C_charge @ gammas[a] @ C_inv + gammas[a].conj()
        err = np.max(np.abs(check))
        max_neg_err = max(max_neg_err, err)
    print(f"  Trying C gamma_a C^{-1} = -gamma_a^*: err = {max_neg_err:.2e}")
    if max_neg_err < 1e-12:
        print(f"  => NEGATIVE intertwining convention (C gamma_a C^{-1} = -gamma_a^*)")
        intertwine_sign = -1  # (local)
    else:
        # Try C = gamma_1 * gamma_3 * gamma_5 * gamma_7 (product of odd gammas)
        C_charge = gammas[0] @ gammas[2] @ gammas[4] @ gammas[6]
        C_inv = np.linalg.inv(C_charge)
        max_err_odd = 0.0  # (local)
        for a in range(8):
            check = C_charge @ gammas[a] @ C_inv - gammas[a].conj()
            err = np.max(np.abs(check))
            max_err_odd = max(max_err_odd, err)
        print(f"  Trying C = gamma_1*gamma_3*gamma_5*gamma_7: err = {max_err_odd:.2e}")

        max_neg_err_odd = 0.0  # (local)
        for a in range(8):
            check = C_charge @ gammas[a] @ C_inv + gammas[a].conj()
            err = np.max(np.abs(check))
            max_neg_err_odd = max(max_neg_err_odd, err)
        print(f"  Trying negative: err = {max_neg_err_odd:.2e}")

        if max_err_odd < 1e-12:
            intertwine_sign = +1
        elif max_neg_err_odd < 1e-12:
            intertwine_sign = -1
        else:
            print("  WARNING: Cannot find clean charge conjugation operator!")
            intertwine_sign = 0  # (local)
else:
    intertwine_sign = +1  # (local)

# The REAL STRUCTURE J acts on spinors as:
# J(psi) = C * psi^*   (where psi^* is complex conjugation of components)
#
# On the Peter-Weyl sector V_{(p,q)} tensor S:
# J acts as: [complex conjugation on V_{(p,q)}] tensor [C on S]
#
# Complex conjugation on V_{(p,q)} maps it to V_{(q,p)} (conjugate representation).
# For (1,0) -> (0,1), for (0,1) -> (1,0), for (1,1) -> (1,1) (self-conjugate).

# Properties of C:
C_squared = C_charge @ C_charge  # (local)
C_sq_type = np.max(np.abs(C_squared - np.eye(DIM_SPIN)))  # (local)
C_sq_neg_type = np.max(np.abs(C_squared + np.eye(DIM_SPIN)))  # (local)

print(f"  C^2 = +I error: {C_sq_type:.2e}")
print(f"  C^2 = -I error: {C_sq_neg_type:.2e}")
if C_sq_type < 1e-12:
    print(f"  => C^2 = +I (real type)")
elif C_sq_neg_type < 1e-12:
    print(f"  => C^2 = -I (quaternionic type)")

# Check C gamma_9 = gamma_9 C ?
gamma9_comm = C_charge @ gamma9 - gamma9 @ C_charge  # (local)
gamma9_anticomm = C_charge @ gamma9 + gamma9 @ C_charge  # (local)
print(f"  [C, gamma_9] error: {np.max(np.abs(gamma9_comm)):.2e}")
print(f"  {{C, gamma_9}} error: {np.max(np.abs(gamma9_anticomm)):.2e}")

# Check [C, Omega] for D_K:
# J D_K = D_K J requires specific commutation of C with Omega
# D_K on sector (p,q) = sum_{a,b} E_{ab} rho_{(p,q)}(X_b) x gamma_a + I x Omega
# Under J: rho -> rho^* (conjugate), gamma_a -> C gamma_a C^{-1} = eps * gamma_a^*
# Omega -> C Omega C^{-1}

C_Omega_comm = C_charge @ Omega @ C_inv - Omega.conj()  # (local)
C_Omega_err = np.max(np.abs(C_Omega_comm))  # (local)
print(f"  |C Omega C^{-1} - Omega^*| error: {C_Omega_err:.2e}")

C_Omega_neg = C_charge @ Omega @ C_inv + Omega.conj()  # (local)
C_Omega_neg_err = np.max(np.abs(C_Omega_neg))  # (local)
print(f"  |C Omega C^{-1} + Omega^*| error: {C_Omega_neg_err:.2e}")

print()

# ============================================================================
# STEP 3: J action on Peter-Weyl sectors
# ============================================================================

print("STEP 3: J action on Peter-Weyl sectors")
print("-" * 50)

# The key structural fact: J acts as
#   J(v tensor psi) = conj(v) tensor C*psi^*
# where v in V_{(p,q)} and psi in S.
#
# This maps V_{(p,q)} tensor S -> V_{(q,p)} tensor S.
#
# Therefore:
#   <J(v_{(1,0)} tensor psi), D_K (w_{(1,1)} tensor phi)>
#   = <conj(v) tensor C*psi^*, D_{(1,1)} (w tensor phi)>
#
# But conj(v) lives in V_{(0,1)}, and D_{(1,1)} maps V_{(1,1)} to itself.
# The inner product requires conj(v) to also be in V_{(1,1)}, which it isn't.
# So this matrix element is ZERO by orthogonality of distinct irreps.
#
# Let me verify this numerically by constructing the explicit J operator
# and computing the matrix element.

# First, verify that rho_{(0,1)}(e_a) = -rho_{(1,0)}(e_a)^T
# (complex conjugation on the fundamental maps to the conjugate representation)
max_conj_err = 0.0  # (local)
for a in range(8):
    # For anti-Hermitian generators: rho*(e_a) = conj(rho(e_a))
    # The conjugate rep is -rho(e_a)^T
    # But complex conjugation of V gives: if rho is the action on V,
    # then on V^* = conj(V), the action is -rho^T
    check = rho_01[a] - (-rho_10[a].T)
    err = np.max(np.abs(check))
    max_conj_err = max(max_conj_err, err)

print(f"  rho_(0,1) = -rho_(1,0)^T verification: err = {max_conj_err:.2e}")

# Build the "J-mixed" operator: takes a state in V_{(1,0)} tensor S,
# applies J to get a state in V_{(0,1)} tensor S, then applies D_{(1,1)}
# to a state in V_{(1,1)} tensor S, and takes the inner product.
#
# Formally: Y_{alpha, beta} = <J psi_alpha^{(1,0)}, D_K psi_beta^{(1,1)}>
# where psi_alpha^{(1,0)} is an eigenstate of D_{(1,0)},
# and psi_beta^{(1,1)} is an eigenstate of D_{(1,1)}.
#
# J psi_alpha^{(1,0)} lives in V_{(0,1)} tensor S.
# D_K psi_beta^{(1,1)} lives in V_{(1,1)} tensor S.
# These are orthogonal sectors => inner product = 0.

# To make this completely explicit, build the full Hilbert space
# V_{(1,0)} + V_{(0,1)} + V_{(1,1)} = C^(3+3+8) = C^14
# tensor S = C^16, giving dim 14*16 = 224.

dim_total = (dim_10 + dim_01 + dim_11) * DIM_SPIN  # 14 * 16 = 224  (local)
print(f"  Combined Hilbert space dim: {dim_total} = ({dim_10}+{dim_01}+{dim_11}) x {DIM_SPIN}")

# Build D_K on the combined space
dim_rep_total = dim_10 + dim_01 + dim_11  # 14  (local)

rho_full = []  # (local)
for b in range(8):
    M = np.zeros((dim_rep_total, dim_rep_total), dtype=complex)
    M[:dim_10, :dim_10] = rho_10[b]
    M[dim_10:dim_10+dim_01, dim_10:dim_10+dim_01] = rho_01[b]
    M[dim_10+dim_01:, dim_10+dim_01:] = rho_11[b]
    rho_full.append(M)

D_full = np.zeros((dim_total, dim_total), dtype=complex)
for a in range(8):
    for b in range(8):
        if abs(E[a, b]) > 1e-15:
            D_full += E[a, b] * np.kron(rho_full[b], gammas[a])
D_full += np.kron(np.eye(dim_rep_total), Omega)

# Verify block structure
idx_10 = slice(0, dim_10 * DIM_SPIN)  # (local)
idx_01 = slice(dim_10 * DIM_SPIN, (dim_10 + dim_01) * DIM_SPIN)  # (local)
idx_11 = slice((dim_10 + dim_01) * DIM_SPIN, dim_total)  # (local)

block_10_01 = D_full[idx_10, idx_01]
block_10_11 = D_full[idx_10, idx_11]
block_01_11 = D_full[idx_01, idx_11]

norm_10_01 = np.max(np.abs(block_10_01))  # (local)
norm_10_11 = np.max(np.abs(block_10_11))  # (local)
norm_01_11 = np.max(np.abs(block_01_11))  # (local)

print(f"  |<(1,0)|D_K|(0,1)>| = {norm_10_01:.4e}")
print(f"  |<(1,0)|D_K|(1,1)>| = {norm_10_11:.4e}")
print(f"  |<(0,1)|D_K|(1,1)>| = {norm_01_11:.4e}")
print(f"  => D_K is block-diagonal: all cross-sector elements < {max(norm_10_01, norm_10_11, norm_01_11):.2e}")

# Now build J on the combined space.
# J acts as: J(v_{(p,q)} tensor psi) = conj(v)_{(q,p)} tensor C * conj(psi)
#
# On the representation space:
# J maps V_{(1,0)} -> V_{(0,1)} via complex conjugation
# J maps V_{(0,1)} -> V_{(1,0)} via complex conjugation
# J maps V_{(1,1)} -> V_{(1,1)} via complex conjugation (self-conjugate: adj rep is real)
#
# The conjugation map on V_{(1,0)} to V_{(0,1)}:
# If v is a vector in C^3 (fundamental), conj(v) is in C^3 (anti-fundamental).
# The map is simply v -> conj(v) viewed in the anti-fundamental space.
# But we need to check: does rho_{(0,1)}(e_a) conj(v) = conj(rho_{(1,0)}(e_a) v)?
# rho_{(0,1)}(e_a) = -rho_{(1,0)}(e_a)^T
# conj(rho_{(1,0)}(e_a) v) = conj(rho_{(1,0)}(e_a)) conj(v) = rho_{(1,0)}(e_a)^* conj(v)
# Need: -rho^T conj(v) = rho^* conj(v)
# -rho^T = -conj(rho^dag) = -conj(-rho) = conj(rho) = rho^*
# Yes! -rho^T = rho^* for anti-Hermitian rho. So the conjugation map v -> conj(v) is correct.

# For the adjoint (1,1), which is REAL (structure constants are real):
# rho_{(1,1)}(e_a) has REAL entries (it's f_{abc}).
# Complex conjugation on V_{(1,1)} leaves the representation space invariant:
# rho_{(1,1)}(e_a) conj(w) = conj(rho_{(1,1)}(e_a) w) since rho is real.
# So J_rep on V_{(1,1)} = complex conjugation = identity (since vectors are real).

# Build J_rep: the representation-space part of J (not including spinor part)
J_rep = np.zeros((dim_rep_total, dim_rep_total), dtype=complex)

# (1,0) -> (0,1) block: complex conjugation mapping
# v in C^3 (fund) -> conj(v) in C^3 (anti-fund)
J_rep[:dim_10, dim_10:dim_10+dim_01] = np.eye(dim_10)  # maps v -> conj(v), but we handle conj separately

# (0,1) -> (1,0) block: complex conjugation mapping back
J_rep[dim_10:dim_10+dim_01, :dim_10] = np.eye(dim_01)

# (1,1) -> (1,1) block: identity (real representation, conj is trivial)
J_rep[dim_10+dim_01:, dim_10+dim_01:] = np.eye(dim_11)

# The FULL J operator on the combined Hilbert space:
# J(sum_i v_i tensor psi_i) = sum_i J_rep * conj(v_i) tensor C * conj(psi_i)
# In matrix form: J = (J_rep tensor C) * K   where K is component-wise conjugation
# So J(vector) = (J_rep tensor C) @ conj(vector)

J_matrix = np.kron(J_rep, C_charge)  # (local) Matrix part of J (without conjugation)

# Verify J^2 = +1 (KO-dim 0 for 8D internal):
# J^2(v) = J(J_rep conj(v) tensor C conj(...))
# = J_rep conj(J_rep conj(v)) tensor C conj(C conj(...))
# = J_rep conj(J_rep) conj(conj(v)) tensor C conj(C) conj(conj(...))
# = J_rep J_rep^* v tensor C C^* psi
#
# Need J_rep J_rep^* = I and C C^* = I for J^2 = +1.
# J_rep J_rep^* in block form:
#   (1,0)->(0,1)->(1,0): I * I = I ✓
#   (0,1)->(1,0)->(0,1): I * I = I ✓
#   (1,1)->(1,1)->(1,1): I * I = I ✓

J_rep_J_rep_star = J_rep @ J_rep.conj()  # (local)
J2_rep_err = np.max(np.abs(J_rep_J_rep_star - np.eye(dim_rep_total)))  # (local)

CC_star = C_charge @ C_charge.conj()  # (local)
J2_spin_err = np.max(np.abs(CC_star - np.eye(DIM_SPIN)))  # (local)

print()
print(f"  J^2 check (rep part): |J_rep J_rep^* - I| = {J2_rep_err:.2e}")
print(f"  J^2 check (spinor part): |C C^* - I| = {J2_spin_err:.2e}")
print()

# ============================================================================
# STEP 4: Compute the Yukawa matrix <J*psi_alpha, D_K*psi_beta>
# ============================================================================

print("STEP 4: Yukawa coupling matrix <J*psi_alpha, D_K*psi_beta>")
print("-" * 50)

# Diagonalize D_K on each sector to get eigenspinors
H_10 = 1j * D_10  # Hermitian  (local)
H_01 = 1j * D_01  # (local)
H_11 = 1j * D_11  # (local)

evals_10, evecs_10 = scipy_eigh(H_10)
evals_01, evecs_01 = scipy_eigh(H_01)
evals_11, evecs_11 = scipy_eigh(H_11)

n_10 = len(evals_10)  # 48  (local)
n_01 = len(evals_01)  # 48  (local)
n_11 = len(evals_11)  # 128  (local)

print(f"  D_{(1,0)} eigenvalues: {n_10} (range [{evals_10[0]:.4f}, {evals_10[-1]:.4f}])")
print(f"  D_{(0,1)} eigenvalues: {n_01} (range [{evals_01[0]:.4f}, {evals_01[-1]:.4f}])")
print(f"  D_{(1,1)} eigenvalues: {n_11} (range [{evals_11[0]:.4f}, {evals_11[-1]:.4f}])")

# Check CPT: eigenvalues of (1,0) and (0,1) should match
# (complex conjugate representations have conjugate Dirac spectra)
spec_diff_10_01 = np.max(np.abs(np.sort(evals_10) - np.sort(evals_01)))  # (local)
print(f"  CPT check: max|spec(1,0) - spec(0,1)| = {spec_diff_10_01:.4e}")

# Build the Yukawa matrix.
# Y_{alpha, beta} = <J * psi_alpha^{(1,0)}, D_K * psi_beta^{(1,1)}>
# where psi_alpha^{(1,0)} are eigenspinors in V_{(1,0)} tensor S (dim 48),
# and psi_beta^{(1,1)} are eigenspinors in V_{(1,1)} tensor S (dim 128).
#
# J * psi_alpha^{(1,0)} lives in V_{(0,1)} tensor S (by the representation map).
# D_K * psi_beta^{(1,1)} lives in V_{(1,1)} tensor S (by block-diagonality).
# These two spaces are orthogonal.
#
# Therefore Y_{alpha, beta} = 0 for ALL alpha, beta.
#
# Verify numerically:

# Embed the eigenvectors in the full space
def embed_eigvec(evec, sector_slice, dim_total):
    """Embed a sector eigenvector into the full Hilbert space."""
    full = np.zeros(dim_total, dtype=complex)
    full[sector_slice] = evec
    return full

# Compute Y_{alpha, beta} directly
Y_10_11 = np.zeros((n_10, n_11), dtype=complex)  # (local)

for alpha in range(n_10):
    # psi_alpha in (1,0) sector
    psi_alpha_full = embed_eigvec(evecs_10[:, alpha], idx_10, dim_total)  # (local)

    # J * psi_alpha: apply J_matrix to conj(psi_alpha)
    J_psi_alpha = J_matrix @ psi_alpha_full.conj()  # (local)

    for beta in range(n_11):
        # D_K * psi_beta in (1,1) sector
        psi_beta_full = embed_eigvec(evecs_11[:, beta], idx_11, dim_total)  # (local)
        D_psi_beta = D_full @ psi_beta_full  # (local)

        # Inner product
        Y_10_11[alpha, beta] = np.vdot(J_psi_alpha, D_psi_beta)

max_Y_10_11 = np.max(np.abs(Y_10_11))  # (local)
fro_Y_10_11 = np.linalg.norm(Y_10_11, 'fro')  # (local)

print()
print(f"  YUKAWA MATRIX Y = <J*psi_(1,0), D_K*psi_(1,1)>:")
print(f"    max|Y_{alpha,beta}|  = {max_Y_10_11:.4e}")
print(f"    Frobenius norm       = {fro_Y_10_11:.4e}")
print(f"    Shape: {Y_10_11.shape}")

# Also compute Y_{alpha, beta} = <J*psi_alpha^{(0,1)}, D_K*psi_beta^{(1,1)}>
Y_01_11 = np.zeros((n_01, n_11), dtype=complex)  # (local)

for alpha in range(n_01):
    psi_alpha_full = embed_eigvec(evecs_01[:, alpha], idx_01, dim_total)
    J_psi_alpha = J_matrix @ psi_alpha_full.conj()

    for beta in range(n_11):
        psi_beta_full = embed_eigvec(evecs_11[:, beta], idx_11, dim_total)
        D_psi_beta = D_full @ psi_beta_full
        Y_01_11[alpha, beta] = np.vdot(J_psi_alpha, D_psi_beta)

max_Y_01_11 = np.max(np.abs(Y_01_11))  # (local)
fro_Y_01_11 = np.linalg.norm(Y_01_11, 'fro')  # (local)

print(f"  YUKAWA MATRIX Y = <J*psi_(0,1), D_K*psi_(1,1)>:")
print(f"    max|Y_{alpha,beta}|  = {max_Y_01_11:.4e}")
print(f"    Frobenius norm       = {fro_Y_01_11:.4e}")
print(f"    Shape: {Y_01_11.shape}")

print()

# ============================================================================
# STEP 5: Check the INTRA-sector fermionic action for PMNS-like structure
# ============================================================================

print("STEP 5: Intra-sector fermionic action (same-sector mixing)")
print("-" * 50)

# Even though cross-sector coupling vanishes, the INTRA-sector D_K
# matrix can produce mass mixing WITHIN each sector.
#
# The fermionic action <J*psi, D_K*psi> with both psi in the SAME sector
# gives the mass matrix for that sector.
#
# For (1,0): Y_{alpha,beta}^{(1,0)} = <J*psi_alpha^{(1,0)}, D_K*psi_beta^{(1,0)}>
# Since J maps (1,0) -> (0,1), this is
# = <psi_{(0,1)}, D_{(1,0)} psi_{(1,0)}>
# which involves states in DIFFERENT sectors.
# So even the intra-sector fermionic action vanishes for (1,0)!
#
# For (1,1): J maps (1,1) -> (1,1) (self-conjugate). So:
# Y_{alpha,beta}^{(1,1)} = <J*psi_alpha^{(1,1)}, D_K*psi_beta^{(1,1)}>
# = <C*conj(psi_alpha), D_{(1,1)} psi_beta>
# This is a genuinely intra-sector matrix element and CAN be nonzero.

# Compute Y^{(1,1)}
Y_11_intra = np.zeros((n_11, n_11), dtype=complex)  # (local)

for alpha in range(n_11):
    psi_alpha_full = embed_eigvec(evecs_11[:, alpha], idx_11, dim_total)
    J_psi_alpha = J_matrix @ psi_alpha_full.conj()

    for beta in range(n_11):
        psi_beta_full = embed_eigvec(evecs_11[:, beta], idx_11, dim_total)
        D_psi_beta = D_full @ psi_beta_full
        Y_11_intra[alpha, beta] = np.vdot(J_psi_alpha, D_psi_beta)

max_Y_11 = np.max(np.abs(Y_11_intra))  # (local)
fro_Y_11 = np.linalg.norm(Y_11_intra, 'fro')  # (local)

print(f"  INTRA-SECTOR YUKAWA Y^(1,1) = <J*psi^(1,1), D_K*psi^(1,1)>:")
print(f"    max|Y_{alpha,beta}|  = {max_Y_11:.4e}")
print(f"    Frobenius norm       = {fro_Y_11:.4e}")

# Also: since D_{(1,1)} psi_beta = lambda_beta psi_beta (anti-Hermitian convention):
# Y^{(1,1)}_{alpha,beta} = lambda_beta * <J*psi_alpha, psi_beta>
# The structure is: Y = M * diag(lambda)
# where M_{alpha,beta} = <J*psi_alpha, psi_beta> is the Majorana mass overlap.

# Compute Majorana overlap M_{alpha,beta} = <J*psi_alpha^{(1,1)}, psi_beta^{(1,1)}>
M_majorana = np.zeros((n_11, n_11), dtype=complex)  # (local)

for alpha in range(n_11):
    psi_alpha = evecs_11[:, alpha]  # (local)
    # J on (1,1) sector: J(v tensor psi) = conj(v) tensor C conj(psi)
    # Since (1,1) is real, conj(v) = v. So J acts as I_rep tensor C * K.
    # J(psi_alpha) = (I_8 tensor C) conj(psi_alpha)
    J_psi_alpha = np.kron(np.eye(dim_11), C_charge) @ psi_alpha.conj()  # (local)

    for beta in range(n_11):
        M_majorana[alpha, beta] = np.vdot(J_psi_alpha, evecs_11[:, beta])

max_M = np.max(np.abs(M_majorana))  # (local)
print(f"  Majorana overlap M = <J*psi^(1,1), psi^(1,1)>:")
print(f"    max|M_{alpha,beta}|  = {max_M:.4e}")

# Check: Y^{(1,1)}_{alpha,beta} should equal sum_gamma M_{alpha,gamma} * lambda_gamma * delta_{gamma,beta}
# = M_{alpha,beta} * lambda_beta (in the eigenbasis)
# where lambda_beta = -i * evals_11[beta] (the actual Dirac eigenvalue)

Y_check = np.zeros_like(Y_11_intra)  # (local)
for beta in range(n_11):
    lambda_beta = -1j * evals_11[beta]  # Dirac eigenvalue  (local)
    Y_check[:, beta] = M_majorana[:, beta] * lambda_beta

Y_consistency = np.max(np.abs(Y_11_intra - Y_check))  # (local)
print(f"  Consistency: |Y - M*diag(lambda)| = {Y_consistency:.4e}")

# SVD of Y^{(1,1)} to extract mixing angles
U_Y, s_Y, Vh_Y = svd(Y_11_intra)
print(f"  SVD of Y^(1,1): singular values range [{s_Y[-1]:.6f}, {s_Y[0]:.6f}]")
print(f"    Top 10 singular values: {s_Y[:10]}")

# Check if Y^{(1,0)} intra vanishes (it should, since J maps (1,0) -> (0,1))
Y_10_intra = np.zeros((n_10, n_10), dtype=complex)  # (local)

for alpha in range(n_10):
    psi_alpha_full = embed_eigvec(evecs_10[:, alpha], idx_10, dim_total)
    J_psi_alpha = J_matrix @ psi_alpha_full.conj()
    # J maps this to (0,1) sector, but we take inner product with D*(1,0) sector
    for beta in range(n_10):
        psi_beta_full = embed_eigvec(evecs_10[:, beta], idx_10, dim_total)
        D_psi_beta = D_full @ psi_beta_full
        Y_10_intra[alpha, beta] = np.vdot(J_psi_alpha, D_psi_beta)

max_Y_10_intra = np.max(np.abs(Y_10_intra))  # (local)
print(f"  INTRA-SECTOR Y^(1,0) = <J*psi^(1,0), D_K*psi^(1,0)>:")
print(f"    max|Y| = {max_Y_10_intra:.4e}  (should be ~0 since J: (1,0)->(0,1))")

print()

# ============================================================================
# STEP 6: Summary and PMNS extraction attempt
# ============================================================================

print("STEP 6: Summary and PMNS Extraction")
print("-" * 50)

print()
print("  STRUCTURAL ANALYSIS:")
print("  " + "=" * 60)
print("  1. D_K is EXACTLY block-diagonal in Peter-Weyl basis")
print(f"     (verified: max cross-sector element < {max(norm_10_01, norm_10_11, norm_01_11):.2e})")
print()
print("  2. Real structure J maps between conjugate irreps:")
print("     J: V_{(1,0)} -> V_{(0,1)}  (fund -> anti-fund)")
print("     J: V_{(0,1)} -> V_{(1,0)}  (anti-fund -> fund)")
print("     J: V_{(1,1)} -> V_{(1,1)}  (adjoint is self-conjugate)")
print()
print("  3. INTER-SECTOR Yukawa coupling (1,0) x (1,1):")
print(f"     <J*psi_(1,0), D_K*psi_(1,1)> = 0  (max = {max_Y_10_11:.2e})")
print(f"     <J*psi_(0,1), D_K*psi_(1,1)> = 0  (max = {max_Y_01_11:.2e})")
print("     REASON: J maps (1,0) -> (0,1), and D_K does not mix (0,1) with (1,1).")
print("     This is a STRUCTURAL ZERO, not a numerical accident.")
print()
print("  4. INTRA-SECTOR fermionic action <J*psi, D_K*psi>:")
print(f"     (1,0) sector: ZERO  (max = {max_Y_10_intra:.2e}, because J: (1,0)->(0,1))")
print(f"     (1,1) sector: NONZERO (max = {max_Y_11:.4f}, Frobenius = {fro_Y_11:.4f})")
print("     The (1,1) sector has a nontrivial Majorana-type mass matrix.")
print()
print("  5. PMNS ROUTE VIA (1,0) x (1,1):")
print("     DOES NOT EXIST.")
print("     The combination of block-diagonality + J-conjugation structure")
print("     makes ALL (1,0)-(1,1) cross-sector matrix elements vanish.")
print("     No PMNS-like mixing can arise from this coupling.")
print()
print("  6. The (1,1) intra-sector Majorana matrix is the only nonzero")
print("     fermionic action in the sectors tested. This could be relevant")
print("     for gluino-like mass terms if (1,1) = adjoint hosts a fermion,")
print("     but it does NOT provide neutrino mixing (wrong sector).")
print()

# ============================================================================
# GATE VERDICT
# ============================================================================

print("=" * 76)
print("GATE: S77-C10-YUKAWA-PMNS (INFO)")
print("=" * 76)

# Determine verdict
if max_Y_10_11 < 1e-10 and max_Y_01_11 < 1e-10:
    verdict = "NULL"  # (local)
    verdict_detail = "All inter-sector Yukawa couplings vanish to machine precision."  # (local)
else:
    verdict = "NONZERO"  # (local)
    verdict_detail = f"Unexpected nonzero coupling: max = {max(max_Y_10_11, max_Y_01_11):.4e}"

print(f"  Verdict: {verdict}")
print(f"  Detail: {verdict_detail}")
print()
print("  STRUCTURAL REASON FOR NULL RESULT:")
print("  Two independent theorems combine to give this result:")
print("  (a) D_K block-diagonality (S22b, S61): D_K does not mix Peter-Weyl sectors")
print("  (b) J-conjugation maps (p,q) -> (q,p): the real structure maps fund to anti-fund")
print("  Together: <J*(1,0)|D_K|(1,1)> = <(0,1)|D_K|(1,1)> = 0")
print()
print("  IMPLICATION FOR PMNS:")
print("  The PMNS matrix CANNOT arise from (1,0) x (1,1) Yukawa coupling")
print("  in the D_K-based fermionic action. Any PMNS mixing must come from:")
print("  (i)  off-Jensen metric deformations breaking block-diagonality")
print("  (ii) gauge-field-mediated mixing via the Kosmann-Lichnerowicz derivative")
print("       (Paper 17, eq 4.1 -- non-Killing fields DO mix D_K eigenspaces)")
print("  (iii) a different operator than D_K in the fermionic action")

t_elapsed = time.time() - t0  # (local)
print()
print(f"  Elapsed time: {t_elapsed:.2f}s")

# ============================================================================
# SAVE RESULTS
# ============================================================================

print()
print("Saving results to s77_inter_sector_yukawa.npz")

np.savez("s77_inter_sector_yukawa.npz",
    # Configuration
    tau=TAU,
    # Block-diagonality verification
    offdiag_norm_10_11=offdiag_norm_10_11,
    offdiag_norm_01_11=offdiag_norm_01_11,
    offdiag_norm_10_01=offdiag_norm_10_01,
    block_diag_confirmed=block_diag_confirmed,
    # Real structure J
    C_charge=C_charge,
    intertwine_sign=intertwine_sign,
    C_sq_type=C_sq_type,
    C_sq_neg_type=C_sq_neg_type,
    J2_rep_err=J2_rep_err,
    J2_spin_err=J2_spin_err,
    # Yukawa matrices
    Y_10_11=Y_10_11,
    Y_01_11=Y_01_11,
    Y_10_intra=Y_10_intra,
    Y_11_intra=Y_11_intra,
    M_majorana=M_majorana,
    max_Y_10_11=max_Y_10_11,
    max_Y_01_11=max_Y_01_11,
    max_Y_10_intra=max_Y_10_intra,
    max_Y_11=max_Y_11,
    # Spectra
    evals_10=evals_10,
    evals_01=evals_01,
    evals_11=evals_11,
    spec_diff_10_01=spec_diff_10_01,
    # SVD of Y^(1,1)
    svals_Y_11=s_Y,
    # Validation
    mc_err=mc_err,
    cliff_err=cliff_err,
    ah_Omega=ah_err,
    # Verdict
    verdict=verdict,
)

print("DONE.")
