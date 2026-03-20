"""
s39_entanglement_entropy.py — ENT-39: Entanglement Entropy of Post-Transit GGE

Computes entanglement entropy between B2 quartet (subsystem A, modes 0-3) and
B1+B3 (subsystem B, modes 4-7) for the post-transit GGE state.

The GGE density matrix in the 2^8 = 256-dim Fock space is:
    rho_GGE = (1/Z) exp(-sum_k lambda_k Q_k)

where Q_k are the Richardson-Gaudin conserved charges (quasiparticle number operators
in the mean-field limit). Since [Q_j, Q_k] = 0, the GGE factorizes in the
quasiparticle basis as:
    rho_GGE = tensor_k  rho_k^{qp}
where rho_k^{qp} = diag(1-p_k, p_k) in the {|0_k>, |1_k>} quasiparticle basis.

The physical (pair-level) basis is related by the Bogoliubov transformation:
    |0_k>_qp = u_k |0_k>_phys + v_k |1_k>_phys    (BCS vacuum for level k)
    |1_k>_qp = -v_k |0_k>_phys + u_k |1_k>_phys   (quasiparticle excitation)

Since the Bogoliubov transformation is MODE-DIAGONAL (gamma_k mixes only c_k and
c_k^dag, not different k), the density matrix in the physical basis also factorizes:
    rho_GGE = tensor_k rho_k^{phys}

where rho_k^{phys} = U_k rho_k^{qp} U_k^dag, with U_k the 2x2 Bogoliubov rotation.

CRITICAL CONSEQUENCE: For a mode-diagonal Bogoliubov transformation, any partition
of modes into subsystems A and B yields:
    rho_A = tensor_{k in A} rho_k^{phys}
    S(A) = sum_{k in A} S(rho_k^{phys})

The entanglement entropy between A and B is ZERO for a product state.
This is a STRUCTURAL result: the GGE is separable across any mode partition.

However, the physically interesting quantity is the SINGLE-MODE entropy and the
comparison with the thermal (Gibbs) state, which we compute in full generality.

We also construct the full 256-dim density matrix explicitly for cross-checking
and compute the entropy in every possible way.

Author: gen-physicist (Claude Opus 4.6)
Session: 39, Gate: ENT-39
"""

import numpy as np
from scipy.linalg import logm
import os

# ============================================================
# 1. Load data
# ============================================================
gge_data = np.load('tier0-computation/s39_gge_lambdas.npz', allow_pickle=True)
bcs_data = np.load('tier0-computation/s38_otoc_bcs.npz', allow_pickle=True)

lambda_k = gge_data['lambda_k']       # (8,) GGE Lagrange multipliers
p_k = gge_data['p_k']                 # (8,) quasiparticle occupation probabilities
u_k = gge_data['u_k_fold']            # (8,) Bogoliubov u coefficients
v_k = gge_data['v_k_fold']            # (8,) Bogoliubov v coefficients
branch_labels = gge_data['branch_labels']
E_8 = gge_data['E_8_s38']             # (8,) single-particle energies
V_phys = gge_data['V_phys_s38']       # (8,8) pairing interaction matrix
n_k_fold = gge_data['n_k_fold']       # (8,) physical pair occupations from S38
S_gge_stored = float(gge_data['S_gge'])
evals_BCS = bcs_data['evals_BCS']     # (256,) BCS Hamiltonian eigenvalues

n_modes = 8
dim = 2**n_modes  # 256

print("=" * 70)
print("ENT-39: Entanglement Entropy of Post-Transit GGE")
print("=" * 70)

# ============================================================
# 2. Construct single-mode density matrices in physical basis
# ============================================================
# In quasiparticle basis: rho_k^{qp} = diag(1-p_k, p_k)
# Bogoliubov rotation: U_k = [[u_k, v_k], [-v_k, u_k]]
# Physical basis: rho_k^{phys} = U_k @ rho_k^{qp} @ U_k^T

rho_k_phys = np.zeros((n_modes, 2, 2))
S_k = np.zeros(n_modes)  # single-mode entropies

print("\n--- Single-mode density matrices (physical basis) ---")
for k in range(n_modes):
    U = np.array([[u_k[k], v_k[k]], [-v_k[k], u_k[k]]])
    rho_qp = np.diag([1 - p_k[k], p_k[k]])
    rho_phys = U @ rho_qp @ U.T
    rho_k_phys[k] = rho_phys

    # Eigenvalues for entropy
    evals_k = np.linalg.eigvalsh(rho_phys)
    evals_k = evals_k[evals_k > 1e-30]  # remove zeros for log safety
    S_k[k] = -np.sum(evals_k * np.log2(evals_k))

    # Physical pair occupation
    n_k_computed = rho_phys[1, 1]  # <1|rho|1> = pair occupation

    print(f"  Mode {k} ({branch_labels[k]}): "
          f"n_pair = {n_k_computed:.6f}, "
          f"off-diag = {rho_phys[0,1]:.6f}, "
          f"S_k = {S_k[k]:.6f} bits")

# Verify pair occupations match stored values
n_k_computed = np.array([rho_k_phys[k, 1, 1] for k in range(n_modes)])
print(f"\n  Pair occupations match n_k_fold: {np.allclose(n_k_computed, n_k_fold, atol=1e-6)}")
print(f"  Max discrepancy: {np.max(np.abs(n_k_computed - n_k_fold)):.2e}")

# ============================================================
# 3. Total single-mode entropy (sum of individual modes)
# ============================================================
S_total_modes = np.sum(S_k)
print(f"\n--- Mode-by-mode entropy ---")
print(f"  S_total = sum_k S_k = {S_total_modes:.6f} bits")

# Cross-check with stored S_gge (should be in nats or bits)
S_gge_bits = S_gge_stored / np.log(2) if S_gge_stored > S_total_modes else S_gge_stored
print(f"  S_gge stored = {S_gge_stored:.6f} (nats: {S_gge_stored:.6f}, bits: {S_gge_stored/np.log(2):.6f})")

# Recompute S_gge in nats from p_k directly
S_gge_nats = 0.0
for k in range(n_modes):
    if p_k[k] > 1e-30:
        S_gge_nats -= p_k[k] * np.log(p_k[k])
    if (1 - p_k[k]) > 1e-30:
        S_gge_nats -= (1 - p_k[k]) * np.log(1 - p_k[k])
S_gge_bits_recomputed = S_gge_nats / np.log(2)
print(f"  S_gge recomputed from p_k: {S_gge_nats:.6f} nats = {S_gge_bits_recomputed:.6f} bits")

# ============================================================
# 4. Build full 256-dim density matrix
# ============================================================
print("\n--- Full 256-dim density matrix construction ---")

# Build rho_GGE as tensor product of single-mode rho_k^{phys}
# Fock basis: |n_0 n_1 ... n_7> where n_k in {0,1}
# Index i corresponds to binary representation: i = sum_k n_k * 2^k

rho_full = np.array([[1.0]])  # start with 1x1 identity
for k in range(n_modes):
    rho_full = np.kron(rho_full, rho_k_phys[k])

print(f"  rho_full shape: {rho_full.shape}")
print(f"  Tr(rho_full) = {np.trace(rho_full):.12f}")
print(f"  Hermiticity: max|rho - rho^dag| = {np.max(np.abs(rho_full - rho_full.T)):.2e}")

# Eigenvalues of full rho
evals_full = np.linalg.eigvalsh(rho_full)
evals_full_pos = evals_full[evals_full > 1e-30]
S_full = -np.sum(evals_full_pos * np.log2(evals_full_pos))
print(f"  S(rho_full) = {S_full:.6f} bits")
print(f"  Cross-check S_full vs sum S_k: |diff| = {abs(S_full - S_total_modes):.2e}")

# Purity
purity_full = np.trace(rho_full @ rho_full)
print(f"  Purity Tr(rho^2) = {purity_full:.8f}")
print(f"  Stored purity = {float(gge_data['purity']):.8f}")

# ============================================================
# 5. Partition into A (B2, modes 0-3) and B (B1+B3, modes 4-7)
# ============================================================
print("\n--- Subsystem partition: A = B2 (modes 0-3), B = B1+B3 (modes 4-7) ---")

n_A = 4  # modes 0-3
n_B = 4  # modes 4-7
dim_A = 2**n_A  # 16
dim_B = 2**n_B  # 16

# Partial trace over B to get rho_A
# rho_full is in basis |a>|b> with a in {0,...,15}, b in {0,...,15}
# rho_A[a1,a2] = sum_b rho_full[a1*dim_B+b, a2*dim_B+b]

rho_full_reshaped = rho_full.reshape(dim_A, dim_B, dim_A, dim_B)
rho_A = np.trace(rho_full_reshaped, axis1=1, axis2=3)  # trace over B indices

print(f"  rho_A shape: {rho_A.shape}")
print(f"  Tr(rho_A) = {np.trace(rho_A):.12f}")

evals_A = np.linalg.eigvalsh(rho_A)
evals_A_pos = evals_A[evals_A > 1e-30]
S_A = -np.sum(evals_A_pos * np.log2(evals_A_pos))
print(f"  S(A) = {S_A:.6f} bits")
print(f"  S(A) from sum of mode entropies (0-3) = {np.sum(S_k[:4]):.6f}")
print(f"  Match: {abs(S_A - np.sum(S_k[:4])) < 1e-8}")

# Partial trace over A to get rho_B
rho_B = np.trace(rho_full_reshaped, axis1=0, axis2=2)  # trace over A indices

print(f"\n  rho_B shape: {rho_B.shape}")
print(f"  Tr(rho_B) = {np.trace(rho_B):.12f}")

evals_B = np.linalg.eigvalsh(rho_B)
evals_B_pos = evals_B[evals_B > 1e-30]
S_B = -np.sum(evals_B_pos * np.log2(evals_B_pos))
print(f"  S(B) = {S_B:.6f} bits")
print(f"  S(B) from sum of mode entropies (4-7) = {np.sum(S_k[4:]):.6f}")
print(f"  Match: {abs(S_B - np.sum(S_k[4:])) < 1e-8}")

# ============================================================
# 6. Entanglement entropy and mutual information
# ============================================================
print("\n--- Entanglement entropy ---")

# For a product state rho = rho_A tensor rho_B:
#   S(AB) = S(A) + S(B)
#   => Mutual information I(A:B) = S(A) + S(B) - S(AB) = 0
#   => Entanglement entropy = 0

S_AB = S_full
I_AB = S_A + S_B - S_AB
print(f"  S(A)  = {S_A:.6f} bits")
print(f"  S(B)  = {S_B:.6f} bits")
print(f"  S(AB) = {S_AB:.6f} bits")
print(f"  S(A) + S(B) = {S_A + S_B:.6f} bits")
print(f"  I(A:B) = S(A) + S(B) - S(AB) = {I_AB:.6e} bits")

# Verify product structure explicitly
rho_AB_product = np.kron(rho_A, rho_B)
product_error = np.max(np.abs(rho_full - rho_AB_product))
print(f"\n  Product structure verification: max|rho_AB - rho_A x rho_B| = {product_error:.2e}")
print(f"  rho_GGE is {'SEPARABLE' if product_error < 1e-10 else 'ENTANGLED'} across A|B partition")

# The entanglement entropy (von Neumann entropy of reduced state for a pure state)
# only applies to pure states. The GGE is a MIXED state, so the "entanglement entropy"
# is better characterized by the mutual information I(A:B).
# For a product mixed state: I(A:B) = 0 exactly.

print(f"\n  RESULT: The GGE is a product state across the A|B partition.")
print(f"  The entanglement entropy is ZERO.")
print(f"  This is STRUCTURAL: mode-diagonal Bogoliubov => product state for any partition.")

# ============================================================
# 7. Entropy of GGE vs Gibbs (thermal) state
# ============================================================
print("\n--- GGE vs Gibbs comparison ---")

# The Gibbs state maximizes entropy subject to <H> = E_GGE
# For the BCS Hamiltonian, the Gibbs state is:
#   rho_Gibbs = exp(-beta H) / Z
# We use the BCS eigenvalues to construct it.

E_GGE = np.sum(evals_full * np.diag(rho_full))  # Not right for product states
# Better: compute <H> in GGE
# <H>_GGE = Tr(H rho_GGE) — we need to reconstruct H in 256-dim basis

# Reconstruct BCS Hamiltonian from eigenvalues and the Fock-space structure
# The BCS Hamiltonian is H = sum_k E_k n_k - sum_{k,l} V_{kl} c_k^dag c_l^dag c_l c_k
# We can directly use E_GGE = sum of eigenvalues of H weighted by rho_GGE diagonal

# Actually, let's compute <H>_GGE directly
# In quasiparticle basis, H = E_0 + sum_k epsilon_k gamma_k^dag gamma_k + ...
# But simpler: we have evals_BCS (256 eigenvalues) and can construct H in Fock basis

# Compute <H> from the pair-level representation
# H_BCS = sum_k 2*eps_k n_k - sum_{kl} V_{kl} P_k^dag P_l
# where P_k = c_{k,down} c_{k,up} is the pair annihilation operator

# For the pair representation:
# n_k -> sigma_z^{(k)}/2 + 1/2 (pair occupation)
# P_k -> sigma_-^{(k)} (pair annihilation)
# P_k^dag -> sigma_+^{(k)} (pair creation)

# Construct H in the 256-dim Fock space
sigma_z = np.array([[1, 0], [0, -1]], dtype=float)
sigma_plus = np.array([[0, 1], [0, 0]], dtype=float)
sigma_minus = np.array([[0, 0], [1, 0]], dtype=float)
I2 = np.eye(2)

def kron_chain(ops):
    """Tensor product of a list of 2x2 matrices."""
    result = ops[0]
    for op in ops[1:]:
        result = np.kron(result, op)
    return result

def make_n_k(k, n):
    """Number operator for mode k in n-mode Fock space."""
    ops = [I2] * n
    ops[k] = (np.eye(2) - sigma_z) / 2  # |1><1| = (I - sigma_z)/2
    return kron_chain(ops)

def make_P_k(k, n):
    """Pair annihilation for mode k."""
    ops = [I2] * n
    ops[k] = sigma_minus
    return kron_chain(ops)

def make_Pdag_k(k, n):
    """Pair creation for mode k."""
    ops = [I2] * n
    ops[k] = sigma_plus
    return kron_chain(ops)

# Build H_BCS using EXACT S38 convention (s38_otoc_bcs.py build_H_BCS):
#   Diagonal: sum_k (2*xi_k - V_kk) * n_k   (xi_k = E_k - mu, mu=0)
#   Off-diag: -sum_{k!=k'} V_{kk'} P_k^dag P_{k'}
# This matches the stored evals_BCS to machine precision.
xi = E_8  # mu = 0
H_BCS = np.zeros((dim, dim))
for alpha in range(dim):
    E_diag = 0.0
    for k in range(n_modes):
        if alpha & (1 << k):
            E_diag += 2 * xi[k] - V_phys[k, k]
    H_BCS[alpha, alpha] = E_diag
    for k in range(n_modes):
        for kp in range(n_modes):
            if k == kp:
                continue
            if (alpha & (1 << kp)) and not (alpha & (1 << k)):
                beta = (alpha ^ (1 << kp)) | (1 << k)
                H_BCS[beta, alpha] -= V_phys[k, kp]

# Verify eigenvalues match
evals_H = np.sort(np.linalg.eigvalsh(H_BCS))
evals_stored = np.sort(evals_BCS)
print(f"  H_BCS eigenvalue check: max|evals - stored| = {np.max(np.abs(evals_H - evals_stored)):.2e}")

# Compute <H>_GGE
E_GGE_val = np.trace(H_BCS @ rho_full)
print(f"  <H>_GGE = {E_GGE_val:.8f}")

# Ground state energy
E_gs = evals_stored[0]
print(f"  E_ground = {E_gs:.8f}")
print(f"  E_excitation = <H>_GGE - E_gs = {E_GGE_val - E_gs:.8f}")

# Find beta for Gibbs state with same <H>
from scipy.optimize import brentq

def gibbs_energy(beta):
    """<H>_Gibbs as function of inverse temperature."""
    boltz = np.exp(-beta * (evals_stored - evals_stored[0]))  # shift for numerical stability
    Z = np.sum(boltz)
    probs = boltz / Z
    return np.sum(probs * evals_stored)

def gibbs_entropy(beta):
    """S_Gibbs in bits."""
    boltz = np.exp(-beta * (evals_stored - evals_stored[0]))
    Z = np.sum(boltz)
    probs = boltz / Z
    probs_pos = probs[probs > 1e-30]
    return -np.sum(probs_pos * np.log2(probs_pos))

# Find beta such that <H>_Gibbs = <H>_GGE
# At beta=0 (infinite T): <H> = mean(evals)
# At beta=inf: <H> = E_gs
E_high_T = np.mean(evals_stored)
print(f"  E(beta=0) = {E_high_T:.8f}")
print(f"  E(beta=inf) = {E_gs:.8f}")
print(f"  E_GGE = {E_GGE_val:.8f}")

if E_GGE_val > E_high_T:
    print("  WARNING: E_GGE > E(beta=0), Gibbs state at negative temperature needed")
    # For negative beta, need to search in negative beta range
    beta_gibbs = brentq(lambda b: gibbs_energy(b) - E_GGE_val, -100, 0)
elif E_GGE_val < E_gs + 1e-10:
    print("  E_GGE ~ E_gs, beta -> infinity")
    beta_gibbs = 100.0
else:
    beta_gibbs = brentq(lambda b: gibbs_energy(b) - E_GGE_val, 0.001, 100)

print(f"  beta_Gibbs = {beta_gibbs:.6f}")
S_gibbs = gibbs_entropy(beta_gibbs)
print(f"  S_Gibbs = {S_gibbs:.6f} bits")

# Entropy deficit
Delta_S = S_gibbs - S_full
print(f"\n  S_GGE  = {S_full:.6f} bits")
print(f"  S_Gibbs = {S_gibbs:.6f} bits")
print(f"  Delta_S = S_Gibbs - S_GGE = {Delta_S:.6f} bits")
print(f"  Information preserved in GGE = {Delta_S:.6f} bits")

# ============================================================
# 8. Alternative partitions: individual branch entropies
# ============================================================
print("\n--- Branch-resolved entropies ---")

S_B2 = np.sum(S_k[:4])
S_B1 = S_k[4]
S_B3 = np.sum(S_k[5:])

print(f"  S(B2, 4 modes) = {S_B2:.6f} bits")
print(f"  S(B1, 1 mode)  = {S_B1:.6f} bits")
print(f"  S(B3, 3 modes) = {S_B3:.6f} bits")
print(f"  Total = {S_B2 + S_B1 + S_B3:.6f} bits")

# ============================================================
# 9. Gibbs state mutual information (for contrast)
# ============================================================
print("\n--- Gibbs state mutual information ---")

# The Gibbs state is NOT a product state (H has interactions V_{kl})
# So I(A:B)_Gibbs > 0 in general
boltz_gibbs = np.exp(-beta_gibbs * (evals_stored - evals_stored[0]))
Z_gibbs = np.sum(boltz_gibbs)
probs_gibbs = boltz_gibbs / Z_gibbs

# Construct Gibbs density matrix in eigenbasis of H
# We need the eigenvectors of H_BCS
evals_H_full, evecs_H = np.linalg.eigh(H_BCS)
# rho_Gibbs = sum_n p_n |n><n|
rho_gibbs = np.zeros((dim, dim))
for n in range(dim):
    rho_gibbs += probs_gibbs[n] * np.outer(evecs_H[:, n], evecs_H[:, n])

print(f"  Tr(rho_Gibbs) = {np.trace(rho_gibbs):.12f}")

# Partial traces for Gibbs
rho_gibbs_reshaped = rho_gibbs.reshape(dim_A, dim_B, dim_A, dim_B)
rho_gibbs_A = np.trace(rho_gibbs_reshaped, axis1=1, axis2=3)
rho_gibbs_B = np.trace(rho_gibbs_reshaped, axis1=0, axis2=2)

evals_gA = np.linalg.eigvalsh(rho_gibbs_A)
evals_gA_pos = evals_gA[evals_gA > 1e-30]
S_gibbs_A = -np.sum(evals_gA_pos * np.log2(evals_gA_pos))

evals_gB = np.linalg.eigvalsh(rho_gibbs_B)
evals_gB_pos = evals_gB[evals_gB > 1e-30]
S_gibbs_B = -np.sum(evals_gB_pos * np.log2(evals_gB_pos))

I_gibbs = S_gibbs_A + S_gibbs_B - S_gibbs
print(f"  S_Gibbs(A) = {S_gibbs_A:.6f} bits")
print(f"  S_Gibbs(B) = {S_gibbs_B:.6f} bits")
print(f"  S_Gibbs(AB) = {S_gibbs:.6f} bits")
print(f"  I_Gibbs(A:B) = {I_gibbs:.6f} bits")

# Product check for Gibbs
rho_gibbs_product = np.kron(rho_gibbs_A, rho_gibbs_B)
gibbs_product_error = np.max(np.abs(rho_gibbs - rho_gibbs_product))
print(f"  Gibbs product error: max|rho - rho_A x rho_B| = {gibbs_product_error:.2e}")
print(f"  Gibbs state is {'SEPARABLE' if gibbs_product_error < 1e-10 else 'ENTANGLED'} across A|B")

# ============================================================
# 10. Maximum entropy bound
# ============================================================
print("\n--- Entropy bounds ---")

S_max = n_modes  # log2(2^8) = 8 bits for maximally mixed state
# For fixed <N_pair>, the max entropy is log2(C(8,N))
from math import comb
N_pair_gge = np.trace(sum(make_n_k(k, n_modes) for k in range(n_modes)) @ rho_full)
print(f"  <N_pair>_GGE = {N_pair_gge:.6f}")

# S38 estimate was S_ent <= 5.55 bits — this was the TOTAL entropy, not entanglement
print(f"\n  S_max (full Fock space) = {S_max:.1f} bits")
print(f"  S_GGE = {S_full:.6f} bits  ({100*S_full/S_max:.1f}% of max)")
print(f"  S_Gibbs = {S_gibbs:.6f} bits  ({100*S_gibbs/S_max:.1f}% of max)")
print(f"  S38 estimate: S_ent <= 5.55 bits")

# ============================================================
# 11. Negativity (entanglement measure for mixed states)
# ============================================================
print("\n--- Negativity (entanglement monotone for mixed states) ---")

# Partial transpose of rho_full w.r.t. subsystem B
# rho^{T_B}_{(a1,b1),(a2,b2)} = rho_{(a1,b2),(a2,b1)}
rho_PT = rho_full_reshaped.transpose(0, 3, 2, 1).reshape(dim, dim)
evals_PT = np.linalg.eigvalsh(rho_PT)
negativity = (np.sum(np.abs(evals_PT)) - 1) / 2
log_negativity = np.log2(2 * negativity + 1)
print(f"  Negativity N = {negativity:.2e}")
print(f"  Log-negativity E_N = {log_negativity:.2e}")
print(f"  (N=0 confirms separability)")

# Also for Gibbs state
rho_gibbs_reshaped_4d = rho_gibbs.reshape(dim_A, dim_B, dim_A, dim_B)
rho_gibbs_PT = rho_gibbs_reshaped_4d.transpose(0, 3, 2, 1).reshape(dim, dim)
evals_gibbs_PT = np.linalg.eigvalsh(rho_gibbs_PT)
neg_gibbs = (np.sum(np.abs(evals_gibbs_PT)) - 1) / 2
log_neg_gibbs = np.log2(2 * neg_gibbs + 1)
print(f"  Negativity_Gibbs = {neg_gibbs:.6f}")
print(f"  Log-negativity_Gibbs = {log_neg_gibbs:.6f}")

# ============================================================
# 12. Second Renyi entropy
# ============================================================
print("\n--- Renyi entropies ---")

# S_2 = -log2(Tr(rho^2))
purity_A = np.trace(rho_A @ rho_A)
purity_B = np.trace(rho_B @ rho_B)
S2_A = -np.log2(purity_A)
S2_B = -np.log2(purity_B)
S2_AB = -np.log2(purity_full)
I2_AB = S2_A + S2_B - S2_AB

print(f"  S_2(A) = {S2_A:.6f} bits")
print(f"  S_2(B) = {S2_B:.6f} bits")
print(f"  S_2(AB) = {S2_AB:.6f} bits")
print(f"  I_2(A:B) = {I2_AB:.6e} bits")

# Gibbs Renyi
purity_gibbs_full = np.trace(rho_gibbs @ rho_gibbs)
purity_gibbs_A = np.trace(rho_gibbs_A @ rho_gibbs_A)
purity_gibbs_B = np.trace(rho_gibbs_B @ rho_gibbs_B)
S2_gibbs = -np.log2(purity_gibbs_full)
S2_gibbs_A = -np.log2(purity_gibbs_A)
S2_gibbs_B = -np.log2(purity_gibbs_B)
I2_gibbs = S2_gibbs_A + S2_gibbs_B - S2_gibbs

print(f"  S_2,Gibbs(A) = {S2_gibbs_A:.6f} bits")
print(f"  S_2,Gibbs(B) = {S2_gibbs_B:.6f} bits")
print(f"  S_2,Gibbs(AB) = {S2_gibbs:.6f} bits")
print(f"  I_2,Gibbs(A:B) = {I2_gibbs:.6f} bits")

# ============================================================
# 13. Summary
# ============================================================
print("\n" + "=" * 70)
print("SUMMARY: ENT-39")
print("=" * 70)

print(f"""
STRUCTURAL RESULT: The GGE density matrix is a PRODUCT STATE across any
mode partition. This follows from the mode-diagonal Bogoliubov transformation
in the Richardson-Gaudin model.

Entanglement entropy S_ent(A:B) = 0  (EXACT)
Mutual information I(A:B) = {I_AB:.2e} bits  (ZERO to machine precision)
Negativity N(A:B) = {negativity:.2e}  (ZERO to machine precision)

Total GGE entropy:
  S_GGE = {S_full:.4f} bits  ({S_full * np.log(2):.4f} nats)
  This is the SUM of single-mode entropies (no inter-mode correlations).

Mode-resolved entropies:
  B2[0-3]: {S_k[0]:.4f}, {S_k[1]:.4f}, {S_k[2]:.4f}, {S_k[3]:.4f} bits each
  B1:      {S_k[4]:.4f} bits
  B3[0-2]: {S_k[5]:.4f}, {S_k[6]:.4f}, {S_k[7]:.4f} bits each

Branch totals:
  S(B2) = {S_B2:.4f} bits  (4 modes, {100*S_B2/S_full:.1f}% of total)
  S(B1) = {S_B1:.4f} bits  (1 mode,  {100*S_B1/S_full:.1f}% of total)
  S(B3) = {S_B3:.4f} bits  (3 modes, {100*S_B3/S_full:.1f}% of total)

Thermalization entropy increase:
  S_GGE   = {S_full:.4f} bits
  S_Gibbs = {S_gibbs:.4f} bits  (at beta = {beta_gibbs:.4f})
  Delta_S = {Delta_S:.4f} bits  (information lost in thermalization)
  {100*Delta_S/S_full:.1f}% entropy increase from GGE -> Gibbs

Gibbs state correlations:
  I_Gibbs(A:B) = {I_gibbs:.4f} bits  (inter-sector entanglement from V_{{kl}})
  Negativity_Gibbs = {neg_gibbs:.4f}

PHYSICAL INTERPRETATION:
The post-transit GGE state carries {S_full:.2f} bits of entropy, but this is
ENTIRELY single-mode (diagonal) entropy — there is NO inter-mode entanglement.
The 8 Richardson-Gaudin conserved charges independently constrain each mode,
preventing any inter-mode quantum correlations.

Thermalization (GGE -> Gibbs) would generate {Delta_S:.2f} bits of additional
entropy and create {I_gibbs:.4f} bits of A:B mutual information.
The {Delta_S:.2f}-bit deficit is the INFORMATION CONTENT of the GGE —
the memory of the pre-transit ground state preserved by integrability.

Gate ENT-39: INFO. S_ent = 0.0000 bits (B2|B1+B3 partition).
  Total GGE entropy = {S_full:.4f} bits.
  Gibbs entropy = {S_gibbs:.4f} bits.
  Information preserved = {Delta_S:.4f} bits.
""")

# ============================================================
# 14. Save results
# ============================================================
np.savez('tier0-computation/s39_entanglement_entropy.npz',
    # Gate verdict
    gate_id='ENT-39',
    gate_type='INFO',

    # Core results
    S_ent_AB=0.0,          # entanglement entropy (exact zero)
    I_AB=I_AB,             # mutual information GGE
    negativity_AB=negativity,
    log_negativity_AB=log_negativity,

    # Single-mode entropies
    S_k=S_k,              # (8,) individual mode entropies in bits
    S_total_modes=S_total_modes,

    # Branch totals
    S_B2=S_B2, S_B1=S_B1, S_B3=S_B3,

    # Full system
    S_GGE=S_full,          # total GGE entropy in bits
    S_GGE_nats=S_full * np.log(2),
    S_Gibbs=S_gibbs,       # Gibbs entropy at matched <H>
    beta_Gibbs=beta_gibbs,
    Delta_S=Delta_S,        # S_Gibbs - S_GGE (information preserved)
    E_GGE=E_GGE_val,

    # Gibbs correlations
    I_Gibbs_AB=I_gibbs,
    negativity_Gibbs=neg_gibbs,
    S_Gibbs_A=S_gibbs_A,
    S_Gibbs_B=S_gibbs_B,

    # Renyi
    S2_A=S2_A, S2_B=S2_B, S2_AB=S2_AB,
    I2_AB=I2_AB,
    I2_Gibbs_AB=I2_gibbs,

    # Verification
    product_error=product_error,
    purity_full=purity_full,

    # Density matrices (for downstream use)
    rho_A=rho_A,           # 16x16 reduced density matrix
    rho_B=rho_B,           # 16x16 reduced density matrix
    rho_k_phys=rho_k_phys, # (8,2,2) single-mode density matrices

    # Metadata
    branch_labels=branch_labels,
    partition='A=B2(0-3), B=B1+B3(4-7)'
)
print("Saved: tier0-computation/s39_entanglement_entropy.npz")
