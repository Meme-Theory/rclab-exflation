#!/usr/bin/env python3
"""
QRPA-40: Quasiparticle Random Phase Approximation collective modes
of the residual interaction V_rem in the 8-mode BCS system at the fold.

Tests whether the BCS ground state is locally stable against collective
particle-hole and particle-particle excitations.

Gate: QRPA-40
  PASS (INSTABILITY): Any eigenvalue omega_n^2 < 0
  FAIL (STABLE): All omega_n^2 > 0

Physics:
  The QRPA equation is the small-amplitude limit of time-dependent HFB.
  It tests the BCS vacuum |BCS> against 2-quasiparticle excitations
  Q_n^dagger |BCS> where Q_n^dagger = sum_{k<k'} [X_n(kk') a_k^+ a_{k'}^+
                                                   - Y_n(kk') a_{k'} a_k]
  The QRPA matrix is:
    [A   B ] [X]       [X]
    [-B -A ] [Y] = E_n [Y]

  where A, B are constructed from the residual interaction V_rem in the
  quasiparticle basis using the BCS coherence factors u_k, v_k.

Input: tier0-computation/s39_richardson_gaudin.npz
       tier0-computation/s37_pair_susceptibility.npz
Output: tier0-computation/s40_qrpa_modes.npz
        tier0-computation/s40_qrpa_modes.png
"""

import numpy as np
from scipy import linalg
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ============================================================
# 1. LOAD DATA
# ============================================================

rg = np.load('tier0-computation/s39_richardson_gaudin.npz', allow_pickle=True)
ps = np.load('tier0-computation/s37_pair_susceptibility.npz', allow_pickle=True)

labels = rg['branch_labels']
n_modes = 8

# Single-particle energies at the fold (tau=0.20 data point, index 3)
E_sp = rg['E_8_tau'][3]  # shape (8,)

# BCS coherence factors from the RG pair wavefunction
u_k = rg['u_k_fold']  # shape (8,)
v_k = rg['v_k_fold']  # shape (8,)
n_k = rg['n_k_fold']  # n_k = v_k^2

# Chemical potential
mu = float(rg['mu'])  # = 0

# Single-particle energies relative to Fermi level
xi_k = E_sp - mu

# Full pairing interaction at fold
V_phys = rg['V_phys_fold']  # shape (8, 8), symmetric

# BCS quasiparticle energies: E_qp_k = sqrt(xi_k^2 + Delta_k^2)
# But since u,v are from RG (not self-consistent BCS), we compute
# E_qp from the Bogoliubov transformation directly:
# E_qp_k = sqrt(xi_k^2 + Delta_eff_k^2) where Delta_eff is the
# effective gap that reproduces the given u_k, v_k
# From u_k^2 = (1 + xi_k/E_qp)/2: E_qp = xi_k / (2*u_k^2 - 1)
E_qp = xi_k / (2 * u_k**2 - 1)
print("=" * 70)
print("QRPA-40: Collective Modes of the Residual Interaction")
print("=" * 70)

print(f"\n--- 1. INPUT DATA ---")
print(f"n_modes = {n_modes}")
print(f"mu = {mu}")
print(f"Fold tau = {float(rg['tau_fold']):.6f}")

print(f"\nSingle-particle structure:")
for i in range(n_modes):
    print(f"  {labels[i]:>5s}: E_sp={E_sp[i]:.6f}, xi={xi_k[i]:.6f}, "
          f"u={u_k[i]:.6f}, v={v_k[i]:.6f}, n={n_k[i]:.6f}, E_qp={E_qp[i]:.6f}")

print(f"\nE_qp range: [{E_qp.min():.4f}, {E_qp.max():.4f}]")

# Verify: u^2 + v^2 = 1
assert np.allclose(u_k**2 + v_k**2, 1.0, atol=1e-12), "u^2 + v^2 != 1"

# ============================================================
# 2. RANK-1 DECOMPOSITION: V = V_sep + V_rem
# ============================================================

print(f"\n--- 2. RANK-1 DECOMPOSITION ---")

eigvals_V, eigvecs_V = np.linalg.eigh(V_phys)
# Dominant eigenvalue (largest by magnitude is the last one since eigh sorts ascending)
idx_dom = np.argmax(np.abs(eigvals_V))
lam_dom = eigvals_V[idx_dom]
v_dom = eigvecs_V[:, idx_dom]

V_sep = lam_dom * np.outer(v_dom, v_dom)
V_rem = V_phys - V_sep

F_V = np.linalg.norm(V_phys, 'fro')
F_sep = np.linalg.norm(V_sep, 'fro')
F_rem = np.linalg.norm(V_rem, 'fro')
var_sep = F_sep**2 / F_V**2
var_rem = F_rem**2 / F_V**2

print(f"Dominant eigenvalue: lambda = {lam_dom:.6f}")
print(f"||V_phys||_F = {F_V:.6f}")
print(f"||V_sep||_F = {F_sep:.6f}")
print(f"||V_rem||_F = {F_rem:.6f}")
print(f"Variance in rank-1: {var_sep:.4f} ({100*var_sep:.1f}%)")
print(f"Variance in residual: {var_rem:.4f} ({100*var_rem:.1f}%)")

# Eigenvalues of V_rem
eigvals_rem = np.linalg.eigvalsh(V_rem)
print(f"\nV_rem eigenvalues: {eigvals_rem}")

# ============================================================
# 3. TIME-EVEN / TIME-ODD DECOMPOSITION
# ============================================================

print(f"\n--- 3. TIME-EVEN / TIME-ODD DECOMPOSITION ---")

# V_rem^even = (V_rem + V_rem^T) / 2
# V_rem^odd  = (V_rem - V_rem^T) / 2
V_rem_even = 0.5 * (V_rem + V_rem.T)
V_rem_odd  = 0.5 * (V_rem - V_rem.T)

norm_even = np.linalg.norm(V_rem_even, 'fro')
norm_odd  = np.linalg.norm(V_rem_odd, 'fro')

print(f"||V_rem^even||_F = {norm_even:.6e}")
print(f"||V_rem^odd||_F  = {norm_odd:.6e}")
print(f"V_rem is symmetric: {np.allclose(V_rem, V_rem.T, atol=1e-14)}")
print(f"V_rem^odd is zero: {np.allclose(V_rem_odd, 0, atol=1e-14)}")
print(f"\nCONSEQUENCE: V_rem is purely time-even.")
print(f"No time-reversal breaking from the residual interaction.")
print(f"The QRPA B matrix receives contributions only from the")
print(f"particle-particle channel (no time-odd driving).")

# ============================================================
# 4. CONSTRUCT QRPA MATRIX
# ============================================================

print(f"\n--- 4. QRPA MATRIX CONSTRUCTION ---")

# Enumerate 2-quasiparticle pairs (k < k')
# For 8 modes: 8*7/2 = 28 pairs
pairs = []
pair_labels = []
for k in range(n_modes):
    for kp in range(k+1, n_modes):
        pairs.append((k, kp))
        pair_labels.append(f"({labels[k]},{labels[kp]})")
n_pairs = len(pairs)
print(f"Number of 2QP pairs: {n_pairs}")

# QRPA A and B matrices in the 2-quasiparticle basis
#
# The QRPA for a general pairing interaction V_{kk'} is:
#
# A_{(kk'),(ll')} = (E_qp_k + E_qp_{k'}) delta_{kk',ll'} + V^{ph}_{(kk'),(ll')}
# B_{(kk'),(ll')} = V^{pp}_{(kk'),(ll')}
#
# The particle-hole (ph) and particle-particle (pp) matrix elements
# are constructed from V_rem using the BCS coherence factors.
#
# For the pairing Hamiltonian H_pair = sum_{kk'} V_{kk'} c_k^+ c_{-k}^+ c_{-k'} c_{k'}
# the QRPA matrix elements in the quasiparticle basis are:
#
# V^{ph}_{(kk'),(ll')} = V_rem_{kl} (u_k u_l u_{k'} u_{l'} + v_k v_l v_{k'} v_{l'})  [k!=l, k'!=l']
#                       + similar terms with proper index structure
#
# For a PAIRING interaction (pair-pair scattering), the relevant channels are:
#
# In the particle-particle (pp) channel for QRPA:
#   The pair transfer operator P^+_k = c^+_k c^+_{-k} creates a Cooper pair.
#   In the quasiparticle basis: c^+_k c^+_{-k} = u_k v_k (1 - 2 alpha^+_k alpha_k)
#   plus pair-scattering terms.
#
# Standard QRPA for pairing-only Hamiltonian (Ring & Schuck, ch. 8):
#
# A_{kk'} = 2*E_qp_k * delta_{kk'} + (u_k u_{k'} - v_k v_{k'})^2 * V_rem_{kk'}
# B_{kk'} = -4 * u_k v_k * u_{k'} v_{k'} * V_rem_{kk'}
#
# Wait -- this is for the PAIR ADDITION (Delta N = +2) mode, not the
# particle-hole mode. The distinction matters.
#
# For the FULL QRPA with both ph and pp channels, we need to be careful.
#
# Let me use the standard nuclear QRPA formulation.
# In the quasiparticle representation, the residual interaction generates
# both forward (A) and backward (B) scattering amplitudes.
#
# For a SEPARABLE pairing force V = -G |Delta><Delta|, the QRPA reduces to:
# A_{kk'} = 2E_k delta_{kk'} - (u_k^2 - v_k^2)(u_{k'}^2 - v_{k'}^2) V_{kk'}^{rem}
# B_{kk'} = 2 u_k v_k * 2 u_{k'} v_{k'} * V_{kk'}^{rem}
#
# But I need to be more systematic. Let me use the FORMULATION from
# Ring & Schuck (The Nuclear Many-Body Problem) Chapter 8.
#
# The QRPA for a general two-body interaction in the particle-particle
# channel (pair vibrations) with the Hamiltonian:
#   H = sum_k E_k N_k + (1/2) sum_{kk'} V_{kk'} P^+_k P_{k'}
# where P^+_k = c^+_k c^+_{bar{k}} is the pair creation operator.
#
# In the quasiparticle basis:
#   P^+_k = u_k v_k (alpha^+_k alpha^+_{bar{k}} + alpha_{bar{k}} alpha_k)
#         + (u_k^2 - ...) terms from the Bogoliubov transformation
#
# Actually, for our problem the modes are ALREADY paired (pair representation).
# Each "mode" k is a pair state. The BCS Hamiltonian is:
#   H = sum_k 2*epsilon_k * n_k + sum_{kk'} V_{kk'} sigma^+_k sigma^-_{k'}
# where sigma^+_k creates a pair in mode k.
#
# The QRPA for pair vibrations (Delta N = +/-2 modes) is:
#
# For the pair-addition mode (raising):
#   [A  B ] [X] = omega [X]
#   [B  A ] [Y] = -omega [Y]   ... NO, sign structure depends on convention
#
# Let me use the explicit BdG-QRPA approach:
#
# The BCS Hamiltonian in quasiparticle representation has the form
# H_BCS = E_0 + sum_k E_qp_k alpha^+_k alpha_k + H_res
# where H_res contains the non-diagonal part from V_rem.
#
# The QRPA treats H_res in the harmonic (small amplitude) approximation.
# For PAIR modes (which are what we want, since V is a pairing interaction),
# the excitation operators are:
#   Q^+_n = sum_k [X_n(k) A^+_k - Y_n(k) A_k]
# where A^+_k = alpha^+_k alpha^+_{bar{k}} creates a pair of quasiparticles
# in time-reversed states (k, bar{k}).
#
# The dimension of the QRPA matrix is n_modes (not n_pairs), because
# each pair mode involves one time-reversed pair, not two distinct modes.
#
# The QRPA equations for PAIR modes are (Ring & Schuck eq 8.31):
#
#  sum_{k'} [A_{kk'} X_n(k') + B_{kk'} Y_n(k')] = omega_n X_n(k)
#  sum_{k'} [B_{kk'} X_n(k') + A_{kk'} Y_n(k')] = -omega_n Y_n(k)
#
# where:
#  A_{kk'} = 2 E_qp_k delta_{kk'} + (u_k u_{k'} - v_k v_{k'})^2 V_rem_{kk'}
#  B_{kk'} = -(2 u_k v_k)(2 u_{k'} v_{k'}) V_rem_{kk'}
#
# The factor of 2 in the diagonal of A is because we excite a PAIR
# of quasiparticles (energy 2*E_qp).
#
# Note the sign: B has a MINUS because V_rem enters with opposite sign
# in the pp channel relative to the ph channel. For attractive V (V > 0
# in our convention), B_{kk'} < 0 when u_k v_k > 0.
#
# The eigenvalues omega_n^2 are found from:
#   (A - B)(A + B) X = omega^2 X
# or equivalently:
#   (A + B)(A - B) Y = omega^2 Y
#
# If omega_n^2 < 0 for any n, the BCS vacuum is UNSTABLE.

# Construct A and B (n_modes x n_modes)
A_qrpa = np.zeros((n_modes, n_modes))
B_qrpa = np.zeros((n_modes, n_modes))

for k in range(n_modes):
    for kp in range(n_modes):
        # Coherence factor combinations
        uu_vv = u_k[k]*u_k[kp] - v_k[k]*v_k[kp]  # (u_k u_k' - v_k v_k')
        uv_k = 2 * u_k[k] * v_k[k]    # 2 u_k v_k (anomalous density)
        uv_kp = 2 * u_k[kp] * v_k[kp]  # 2 u_k' v_k'

        A_qrpa[k, kp] = uu_vv**2 * V_rem[k, kp]
        B_qrpa[k, kp] = -uv_k * uv_kp * V_rem[k, kp]

        if k == kp:
            A_qrpa[k, kp] += 2 * E_qp[k]

print(f"\n--- A matrix (diagonal = 2*E_qp + V_rem^ph) ---")
print(f"A diagonal: {np.diag(A_qrpa)}")
print(f"A off-diagonal max: {np.max(np.abs(A_qrpa - np.diag(np.diag(A_qrpa)))):.6f}")
print(f"A symmetry: max|A - A^T| = {np.max(np.abs(A_qrpa - A_qrpa.T)):.2e}")

print(f"\n--- B matrix (pair-pair scattering) ---")
print(f"B diagonal: {np.diag(B_qrpa)}")
print(f"B off-diagonal max: {np.max(np.abs(B_qrpa - np.diag(np.diag(B_qrpa)))):.6f}")
print(f"B symmetry: max|B - B^T| = {np.max(np.abs(B_qrpa - B_qrpa.T)):.2e}")

# Print the matrices
print(f"\nA matrix:")
for i in range(n_modes):
    row = " ".join(f"{A_qrpa[i,j]:10.6f}" for j in range(n_modes))
    print(f"  {row}")

print(f"\nB matrix:")
for i in range(n_modes):
    row = " ".join(f"{B_qrpa[i,j]:10.6f}" for j in range(n_modes))
    print(f"  {row}")

# ============================================================
# 5. QRPA STABILITY MATRIX AND EIGENVALUES
# ============================================================

print(f"\n--- 5. QRPA EIGENVALUES ---")

# Method 1: Direct diagonalization of the full QRPA matrix
# M = [[A, B], [-B, -A]]
M_qrpa = np.block([
    [A_qrpa,  B_qrpa],
    [-B_qrpa, -A_qrpa]
])

eigvals_M = np.linalg.eigvals(M_qrpa)
eigvals_M_sorted = np.sort(eigvals_M.real)  # eigenvalues come in +/- pairs
print(f"Full QRPA matrix eigenvalues (real parts):")
for i, ev in enumerate(eigvals_M_sorted):
    imag = eigvals_M[np.argsort(eigvals_M.real)][i].imag
    print(f"  omega_{i} = {ev:.6f} (imag = {imag:.2e})")

# Check: eigenvalues should come in +/- pairs
pos_eigs = eigvals_M_sorted[eigvals_M_sorted > 0]
neg_eigs = eigvals_M_sorted[eigvals_M_sorted < 0]
print(f"\nPositive eigenvalues: {pos_eigs}")
print(f"Negative eigenvalues: {neg_eigs}")

# Method 2: omega^2 from (A-B)(A+B)
# This is the standard stability matrix
ApB = A_qrpa + B_qrpa
AmB = A_qrpa - B_qrpa

# Check positive definiteness of A-B and A+B
eigvals_AmB = np.linalg.eigvalsh(AmB)
eigvals_ApB = np.linalg.eigvalsh(ApB)
print(f"\nEigenvalues of (A - B):")
for i, ev in enumerate(eigvals_AmB):
    print(f"  {ev:.6f}")
print(f"\nEigenvalues of (A + B):")
for i, ev in enumerate(eigvals_ApB):
    print(f"  {ev:.6f}")

# Stability matrix S = (A-B)(A+B)
S_stab = AmB @ ApB
eigvals_S = np.linalg.eigvals(S_stab)
omega_sq = np.sort(eigvals_S.real)
omega_qrpa = np.sqrt(np.abs(omega_sq)) * np.sign(omega_sq)

print(f"\nomega^2 from stability matrix (A-B)(A+B):")
for i in range(n_modes):
    status = "STABLE" if omega_sq[i] > 0 else "UNSTABLE"
    omega_val = np.sqrt(abs(omega_sq[i]))
    print(f"  omega^2_{i} = {omega_sq[i]:12.6f}  |omega| = {omega_val:.6f}  [{status}]")

# Also compute via (A+B)(A-B) as cross-check
S_stab2 = ApB @ AmB
eigvals_S2 = np.linalg.eigvals(S_stab2)
omega_sq2 = np.sort(eigvals_S2.real)
print(f"\nCross-check: omega^2 from (A+B)(A-B):")
for i in range(n_modes):
    print(f"  omega^2_{i} = {omega_sq2[i]:12.6f}")
print(f"Max discrepancy: {np.max(np.abs(omega_sq - omega_sq2)):.2e}")

# Method 3: Proper QRPA via generalized eigenvalue problem
# The QRPA metric is sigma_3 = diag(I, -I)
# M sigma_3 |psi> = omega |psi>
# This gives the physical eigenvalues directly
sigma3 = np.diag(np.concatenate([np.ones(n_modes), -np.ones(n_modes)]))
# omega_n are eigenvalues of sigma_3 @ M
eigvals_method3 = np.linalg.eigvals(sigma3 @ M_qrpa)
print(f"\nMethod 3 (sigma_3 M): {np.sort(eigvals_method3.real)}")

# ============================================================
# 6. GATE VERDICT
# ============================================================

print(f"\n{'='*70}")
print(f"GATE VERDICT: QRPA-40")
print(f"{'='*70}")

n_unstable = np.sum(omega_sq < -1e-10)
min_omega_sq = np.min(omega_sq)
max_imaginary = np.max(np.abs(np.array([ev.imag for ev in eigvals_M])))

if n_unstable > 0:
    verdict = "PASS (INSTABILITY)"
    print(f"  {n_unstable} mode(s) with omega^2 < 0")
    for i in range(n_modes):
        if omega_sq[i] < -1e-10:
            print(f"    omega^2 = {omega_sq[i]:.6f} -> IMAGINARY omega = {np.sqrt(-omega_sq[i]):.6f}i")
else:
    verdict = "FAIL (STABLE)"
    print(f"  All omega^2 > 0: BCS ground state is locally STABLE")

print(f"\n  Verdict: {verdict}")
print(f"  Lowest omega^2: {min_omega_sq:.6f}")
print(f"  Lowest |omega|: {np.sqrt(abs(min_omega_sq)):.6f}")
print(f"  Max imaginary part of QRPA eigenvalues: {max_imaginary:.2e}")

# ============================================================
# 7. PHYSICAL ANALYSIS
# ============================================================

print(f"\n--- 7. PHYSICAL ANALYSIS ---")

# QRPA eigenvalues (physical: positive branch)
omega_phys = np.sqrt(np.maximum(omega_sq, 0))
omega_phys_sorted = np.sort(omega_phys[omega_sq > 0])

print(f"\nPhysical QRPA frequencies (positive branch):")
for i, om in enumerate(omega_phys_sorted):
    print(f"  omega_{i} = {om:.6f}")

# Compare with GPV frequency from S37
omega_gpv = 0.792  # from S37 pair susceptibility
print(f"\nomega_GPV (S37) = {omega_gpv:.3f}")
if len(omega_phys_sorted) > 0:
    closest_idx = np.argmin(np.abs(omega_phys_sorted - omega_gpv))
    print(f"Closest QRPA mode: omega_{closest_idx} = {omega_phys_sorted[closest_idx]:.6f}")
    print(f"Ratio omega_QRPA/omega_GPV = {omega_phys_sorted[closest_idx]/omega_gpv:.4f}")

# Eigenvectors for mode identification
# Diagonalize (A-B)^{1/2} (A+B) (A-B)^{1/2} for proper eigenvectors
# But first check if A-B is positive definite
if np.all(eigvals_AmB > 0):
    print(f"\n(A-B) is positive definite -> can compute proper QRPA eigenvectors")
    AmB_sqrt = linalg.sqrtm(AmB)
    AmB_sqrt_inv = np.linalg.inv(AmB_sqrt)
    S_symm = AmB_sqrt @ ApB @ AmB_sqrt
    omega_sq_symm, U = np.linalg.eigh(S_symm)

    print(f"\nomega^2 from symmetric form (cross-check):")
    for i, osq in enumerate(np.sort(omega_sq_symm)):
        print(f"  omega^2_{i} = {osq:.6f}")

    # Reconstruct X, Y amplitudes
    # X_n = (A-B)^{1/2} U_n / sqrt(2*omega_n)
    # Y_n = -(A-B)^{-1/2} (A+B) X_n + omega_n * (A-B)^{-1/2} X_n ... complicated
    # Simpler: solve the full eigenvalue problem
else:
    print(f"\n(A-B) has negative eigenvalues -> instability from particle-hole channel")
    print(f"Min eigenvalue of (A-B): {np.min(eigvals_AmB):.6f}")

# Also check A+B positive definiteness
if np.all(eigvals_ApB > 0):
    print(f"(A+B) is positive definite")
else:
    print(f"(A+B) has negative eigenvalues -> Thouless instability (pairing collapse)")
    print(f"Min eigenvalue of (A+B): {np.min(eigvals_ApB):.6f}")

# Transition amplitudes and sum rules
# For the pair transfer operator F = sum_k (sigma^+_k + sigma^-_k)
# In quasiparticle basis: F ~ sum_k [2 u_k v_k (1 - 2 n_qp_k) + ...]
# The QRPA transition amplitude is <n|F|0> = sum_k f_k (X_n(k) + Y_n(k))
# where f_k = 2 u_k v_k for pair transfer

# Full eigenvector decomposition
eigvals_full, eigvecs_full = np.linalg.eig(M_qrpa)
# Sort by real part (ascending)
idx_sort = np.argsort(eigvals_full.real)
eigvals_full = eigvals_full[idx_sort]
eigvecs_full = eigvecs_full[:, idx_sort]

# Physical modes: positive eigenvalues
pos_mask = eigvals_full.real > 1e-10
n_phys_modes = np.sum(pos_mask)

# Pair transfer operator matrix elements
f_k = 2 * u_k * v_k  # pair transfer amplitudes

print(f"\n--- TRANSITION AMPLITUDES ---")
print(f"Pair transfer amplitudes f_k = 2*u_k*v_k:")
for i in range(n_modes):
    print(f"  {labels[i]:>5s}: f_k = {f_k[i]:.6f}")

# For each positive-energy QRPA mode, compute transition strength
# |<n|F|0>|^2 and energy-weighted sum rule contribution
strengths = []
omegas_pos = []
for i in range(2*n_modes):
    if eigvals_full[i].real > 1e-10 and abs(eigvals_full[i].imag) < 1e-6:
        psi = eigvecs_full[:, i].real
        X_n = psi[:n_modes]
        Y_n = psi[n_modes:]

        # Normalize: X^T X - Y^T Y = 1 (QRPA norm)
        norm_qrpa = X_n @ X_n - Y_n @ Y_n
        if abs(norm_qrpa) > 1e-10:
            X_n /= np.sqrt(abs(norm_qrpa))
            Y_n /= np.sqrt(abs(norm_qrpa))

        # Transition amplitude
        Fn = np.dot(f_k, X_n + Y_n)
        strength = Fn**2
        omega_n = eigvals_full[i].real

        omegas_pos.append(omega_n)
        strengths.append(strength)

        print(f"\n  Mode at omega = {omega_n:.6f}:")
        print(f"    X = [{', '.join(f'{x:.4f}' for x in X_n)}]")
        print(f"    Y = [{', '.join(f'{y:.4f}' for y in Y_n)}]")
        print(f"    |<n|F|0>|^2 = {strength:.6f}")
        print(f"    omega * |<n|F|0>|^2 = {omega_n * strength:.6f}")

omegas_pos = np.array(omegas_pos)
strengths = np.array(strengths)

# Energy-weighted sum rule
EWSR = np.sum(omegas_pos * strengths)
print(f"\n--- ENERGY-WEIGHTED SUM RULE ---")
print(f"EWSR = sum_n omega_n |<n|F|0>|^2 = {EWSR:.6f}")
if EWSR > 0 and len(strengths) > 0:
    EWSR_lowest = omegas_pos[0] * strengths[0]
    print(f"Lowest mode contribution: {EWSR_lowest:.6f} ({100*EWSR_lowest/EWSR:.1f}%)")
    # EWSR for pair transfer should equal the commutator
    # [F, [H, F]] / 2 = sum_k f_k^2 * 2*E_qp_k (Thouless theorem)
    EWSR_thouless = np.sum(f_k**2 * 2 * E_qp)
    print(f"Thouless sum rule: {EWSR_thouless:.6f}")
    print(f"Ratio EWSR/Thouless: {EWSR/EWSR_thouless:.4f}")

# ============================================================
# 8. COMPARISON WITH S37 GPV
# ============================================================

print(f"\n--- 8. COMPARISON WITH S37 GPV ---")
print(f"omega_GPV (S37 pair susceptibility pole) = {omega_gpv:.4f}")
print(f"omega_pair_addition (S37) = {float(ps['omega_plus']):.4f}")
print(f"omega_pair_removal (S37) = {float(ps['omega_minus']):.4f}")
print(f"omega_split (S37) = {float(ps['omega_split']):.4f}")
print(f"Delta_pair (S37) = {float(ps['Delta_pair']):.4f}")

if len(omegas_pos) > 0:
    print(f"\nQRPA modes vs GPV:")
    for i, om in enumerate(np.sort(omegas_pos)):
        ratio = om / omega_gpv
        print(f"  QRPA mode {i}: omega = {om:.4f}, ratio to GPV = {ratio:.4f}")

# ============================================================
# 9. ADDITIONAL CROSS-CHECKS
# ============================================================

print(f"\n--- 9. CROSS-CHECKS ---")

# Check 1: Thouless criterion
# The BCS solution is stable iff (A-B) > 0 AND (A+B) > 0
# (A-B) > 0: particle-hole stability
# (A+B) > 0: particle-particle (Thouless) stability
print(f"Thouless stability criterion:")
print(f"  min eig(A-B) = {np.min(eigvals_AmB):.6f} {'> 0 STABLE' if np.min(eigvals_AmB) > 0 else '< 0 UNSTABLE'}")
print(f"  min eig(A+B) = {np.min(eigvals_ApB):.6f} {'> 0 STABLE' if np.min(eigvals_ApB) > 0 else '< 0 UNSTABLE'}")

# Check 2: Verify V_rem is traceless (rank-1 removed dominant eigenvector)
tr_V_rem = np.trace(V_rem)
print(f"\ntr(V_rem) = {tr_V_rem:.6f} (should be tr(V) - lambda_dom = {np.trace(V_phys) - lam_dom:.6f})")

# Check 3: Ratio of B to A off-diagonal
A_offdiag = A_qrpa - np.diag(np.diag(A_qrpa))
B_offdiag = B_qrpa - np.diag(np.diag(B_qrpa))
print(f"\n||A_offdiag||_F / ||A_diag|| = {np.linalg.norm(A_offdiag, 'fro') / np.linalg.norm(np.diag(A_qrpa)):.4f}")
print(f"||B||_F / ||A||_F = {np.linalg.norm(B_qrpa, 'fro') / np.linalg.norm(A_qrpa, 'fro'):.4f}")

# Check 4: Spurious mode check
# If V_sep is removed perfectly, there should be no Goldstone mode at omega=0
# The full V has a large eigenvalue -> collective pair mode
# V_rem should NOT produce a zero mode
print(f"\nSpurious mode check:")
print(f"  Min |omega^2| = {np.min(np.abs(omega_sq)):.6e}")
print(f"  (Should be > 0 if V_sep removal is clean)")

# Check 5: Compare with FULL V QRPA (V_phys instead of V_rem)
A_full = np.zeros((n_modes, n_modes))
B_full = np.zeros((n_modes, n_modes))
for k in range(n_modes):
    for kp in range(n_modes):
        uu_vv = u_k[k]*u_k[kp] - v_k[k]*v_k[kp]
        uv_k = 2 * u_k[k] * v_k[k]
        uv_kp = 2 * u_k[kp] * v_k[kp]
        A_full[k, kp] = uu_vv**2 * V_phys[k, kp]
        B_full[k, kp] = -uv_k * uv_kp * V_phys[k, kp]
        if k == kp:
            A_full[k, kp] += 2 * E_qp[k]

ApB_full = A_full + B_full
AmB_full = A_full - B_full
S_full = (AmB_full) @ (ApB_full)
omega_sq_full = np.sort(np.linalg.eigvals(S_full).real)

print(f"\nFull V QRPA omega^2 (for comparison):")
for i in range(n_modes):
    status = "STABLE" if omega_sq_full[i] > 0 else "UNSTABLE"
    print(f"  omega^2_{i} = {omega_sq_full[i]:12.6f}  [{status}]")

# Check 6: Sensitivity to V_rem scale
# How large would V_rem need to be for instability?
# omega^2 = 0 when det(A-B) = 0 or det(A+B) = 0
# Scale V_rem -> alpha * V_rem and find critical alpha
print(f"\n--- CRITICAL SCALING ---")
alpha_crit_AmB = None
alpha_crit_ApB = None

for alpha_test in np.linspace(0, 50, 5001):
    V_test = alpha_test * V_rem
    A_test = np.zeros((n_modes, n_modes))
    B_test = np.zeros((n_modes, n_modes))
    for k in range(n_modes):
        for kp in range(n_modes):
            uu_vv = u_k[k]*u_k[kp] - v_k[k]*v_k[kp]
            uv_k_val = 2 * u_k[k] * v_k[k]
            uv_kp_val = 2 * u_k[kp] * v_k[kp]
            A_test[k, kp] = uu_vv**2 * V_test[k, kp]
            B_test[k, kp] = -uv_k_val * uv_kp_val * V_test[k, kp]
            if k == kp:
                A_test[k, kp] += 2 * E_qp[k]

    eig_AmB_test = np.min(np.linalg.eigvalsh(A_test - B_test))
    eig_ApB_test = np.min(np.linalg.eigvalsh(A_test + B_test))

    if alpha_crit_AmB is None and eig_AmB_test < 0:
        alpha_crit_AmB = alpha_test
    if alpha_crit_ApB is None and eig_ApB_test < 0:
        alpha_crit_ApB = alpha_test

    if alpha_crit_AmB is not None and alpha_crit_ApB is not None:
        break

print(f"Critical alpha for (A-B) instability: {alpha_crit_AmB if alpha_crit_AmB else '> 50'}")
print(f"Critical alpha for (A+B) instability: {alpha_crit_ApB if alpha_crit_ApB else '> 50'}")
if alpha_crit_AmB is not None or alpha_crit_ApB is not None:
    alpha_crit = min(x for x in [alpha_crit_AmB, alpha_crit_ApB] if x is not None)
    print(f"V_rem would need to be {alpha_crit:.1f}x stronger for instability")
else:
    print(f"V_rem would need to be > 50x stronger for instability (deeply stable)")

# ============================================================
# 10. TAU-DEPENDENCE: QRPA across the transit
# ============================================================

print(f"\n--- 10. TAU DEPENDENCE ---")
tau_values = rg['tau_values']
n_tau = len(tau_values)
omega_sq_tau = np.zeros((n_tau, n_modes))
min_eigAmB_tau = np.zeros(n_tau)
min_eigApB_tau = np.zeros(n_tau)

for t_idx in range(n_tau):
    E_sp_t = rg['E_8_tau'][t_idx]
    xi_t = E_sp_t - mu

    # Use the tau-dependent pair wavefunction
    psi_t = rg['psi_pair_tau'][t_idx]
    v_t = np.abs(psi_t)
    u_t = np.sqrt(1.0 - v_t**2)

    # QP energies
    denom = 2*u_t**2 - 1
    # Avoid division by zero when u = v = 1/sqrt(2)
    safe_denom = np.where(np.abs(denom) > 1e-10, denom, 1e-10)
    E_qp_t = np.abs(xi_t / safe_denom)

    # V_phys at this tau
    V_t = rg['V_phys_tau'][t_idx]

    # Rank-1 decomposition at this tau
    eigvals_Vt, eigvecs_Vt = np.linalg.eigh(V_t)
    idx_dom_t = np.argmax(np.abs(eigvals_Vt))
    V_sep_t = eigvals_Vt[idx_dom_t] * np.outer(eigvecs_Vt[:, idx_dom_t], eigvecs_Vt[:, idx_dom_t])
    V_rem_t = V_t - V_sep_t

    # QRPA matrices
    A_t = np.zeros((n_modes, n_modes))
    B_t = np.zeros((n_modes, n_modes))
    for k in range(n_modes):
        for kp in range(n_modes):
            uu_vv = u_t[k]*u_t[kp] - v_t[k]*v_t[kp]
            uv_k_val = 2 * u_t[k] * v_t[k]
            uv_kp_val = 2 * u_t[kp] * v_t[kp]
            A_t[k, kp] = uu_vv**2 * V_rem_t[k, kp]
            B_t[k, kp] = -uv_k_val * uv_kp_val * V_rem_t[k, kp]
            if k == kp:
                A_t[k, kp] += 2 * E_qp_t[k]

    AmB_t = A_t - B_t
    ApB_t = A_t + B_t
    S_t = AmB_t @ ApB_t
    omega_sq_tau[t_idx] = np.sort(np.linalg.eigvals(S_t).real)
    min_eigAmB_tau[t_idx] = np.min(np.linalg.eigvalsh(AmB_t))
    min_eigApB_tau[t_idx] = np.min(np.linalg.eigvalsh(ApB_t))

print(f"\nQRPA stability across tau:")
print(f"{'tau':>6s} {'min(w^2)':>12s} {'min(A-B)':>10s} {'min(A+B)':>10s} {'status':>8s}")
for t_idx in range(n_tau):
    min_wsq = omega_sq_tau[t_idx, 0]
    status = "STABLE" if min_wsq > 0 and min_eigAmB_tau[t_idx] > 0 and min_eigApB_tau[t_idx] > 0 else "UNSTAB"
    print(f"{tau_values[t_idx]:6.3f} {min_wsq:12.4f} {min_eigAmB_tau[t_idx]:10.4f} {min_eigApB_tau[t_idx]:10.4f} {status:>8s}")

# ============================================================
# 11. SAVE DATA
# ============================================================

np.savez('tier0-computation/s40_qrpa_modes.npz',
    # Gate result
    gate_verdict=verdict,

    # Input parameters
    n_modes=n_modes,
    mu=mu,
    tau_fold=float(rg['tau_fold']),
    E_sp=E_sp,
    xi_k=xi_k,
    u_k=u_k,
    v_k=v_k,
    E_qp=E_qp,
    labels=labels,

    # Decomposition
    V_phys=V_phys,
    V_sep=V_sep,
    V_rem=V_rem,
    lam_dom=lam_dom,
    v_dom=v_dom,
    var_sep=var_sep,
    var_rem=var_rem,
    eigvals_Vrem=eigvals_rem,
    V_rem_even=V_rem_even,
    V_rem_odd=V_rem_odd,
    norm_even=norm_even,
    norm_odd=norm_odd,

    # QRPA matrices
    A_qrpa=A_qrpa,
    B_qrpa=B_qrpa,

    # Eigenvalues
    omega_sq=omega_sq,
    omega_sq_full=omega_sq_full,
    eigvals_AmB=eigvals_AmB,
    eigvals_ApB=eigvals_ApB,
    eigvals_M=eigvals_M,

    # Transition strengths
    omegas_pos=omegas_pos,
    strengths=strengths,
    EWSR=EWSR,
    f_k=f_k,

    # Tau dependence
    tau_values=tau_values,
    omega_sq_tau=omega_sq_tau,
    min_eigAmB_tau=min_eigAmB_tau,
    min_eigApB_tau=min_eigApB_tau,

    # Critical scaling
    alpha_crit_AmB=alpha_crit_AmB if alpha_crit_AmB is not None else -1,
    alpha_crit_ApB=alpha_crit_ApB if alpha_crit_ApB is not None else -1,

    # Comparison
    omega_gpv=omega_gpv,
)

print(f"\nData saved to tier0-computation/s40_qrpa_modes.npz")

# ============================================================
# 12. PLOT
# ============================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('QRPA-40: Collective Modes of V_rem', fontsize=14, fontweight='bold')

# Panel 1: QRPA spectrum at fold
ax = axes[0, 0]
omega_plot = np.sqrt(np.maximum(omega_sq, 0))
colors = ['C0' if wsq > 0 else 'red' for wsq in omega_sq]
ax.bar(range(n_modes), omega_plot, color=colors, alpha=0.7, edgecolor='black')
ax.axhline(omega_gpv, color='green', ls='--', lw=2, label=f'GPV = {omega_gpv:.3f}')
ax.set_xlabel('QRPA mode index')
ax.set_ylabel('omega_n')
ax.set_title(f'QRPA Spectrum at Fold (tau={float(rg["tau_fold"]):.3f})')
ax.legend()

# Mark unstable modes
for i in range(n_modes):
    if omega_sq[i] < -1e-10:
        ax.annotate('UNSTABLE', (i, 0.1), ha='center', color='red', fontweight='bold')

# Panel 2: V_rem eigenvalue spectrum
ax = axes[0, 1]
colors_eig = ['C3' if ev < 0 else 'C0' for ev in eigvals_rem]
ax.bar(range(n_modes), eigvals_rem, color=colors_eig, alpha=0.7, edgecolor='black')
ax.axhline(0, color='gray', ls='-', lw=0.5)
ax.set_xlabel('Eigenvalue index')
ax.set_ylabel('Eigenvalue')
ax.set_title(f'V_rem Spectrum (rank-1 removed, {100*var_rem:.1f}% of variance)')

# Panel 3: Tau dependence of min(omega^2)
ax = axes[1, 0]
ax.plot(tau_values, omega_sq_tau[:, 0], 'ko-', label='min(omega^2)', markersize=5)
ax.plot(tau_values, min_eigAmB_tau, 'bs--', label='min eig(A-B)', markersize=4)
ax.plot(tau_values, min_eigApB_tau, 'r^--', label='min eig(A+B)', markersize=4)
ax.axhline(0, color='gray', ls='-', lw=0.5)
ax.axvline(float(rg['tau_fold']), color='orange', ls=':', lw=1, label='fold')
ax.set_xlabel('tau')
ax.set_ylabel('Eigenvalue')
ax.set_title('QRPA Stability Across Transit')
ax.legend(fontsize=8)

# Panel 4: Transition strengths
ax = axes[1, 1]
if len(omegas_pos) > 0 and len(strengths) > 0:
    ax.stem(omegas_pos, strengths, linefmt='C0-', markerfmt='C0o', basefmt='gray')
    ax.axvline(omega_gpv, color='green', ls='--', lw=2, label=f'GPV = {omega_gpv:.3f}')
    ax.set_xlabel('omega_n')
    ax.set_ylabel('|<n|F|0>|^2')
    ax.set_title(f'Pair Transfer Strength (EWSR = {EWSR:.3f})')
    ax.legend()
else:
    ax.text(0.5, 0.5, 'No positive modes', ha='center', va='center', transform=ax.transAxes)

plt.tight_layout()
plt.savefig('tier0-computation/s40_qrpa_modes.png', dpi=150, bbox_inches='tight')
print(f"Plot saved to tier0-computation/s40_qrpa_modes.png")

print(f"\n{'='*70}")
print(f"COMPUTATION COMPLETE")
print(f"{'='*70}")
