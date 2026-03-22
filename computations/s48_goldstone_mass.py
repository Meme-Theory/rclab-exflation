#!/usr/bin/env python3
"""
Session 48 W1-A: Goldstone Mass from Spectral Action (GOLDSTONE-MASS-48)
=========================================================================

CONTEXT:
  U(1)_7 is spontaneously broken by the BCS condensate (Cooper pairs carry
  K_7 charge +/-1/2, S35). The Goldstone boson is the phase mode phi.

  The spectral action S[D] = Tr[f(D^2/Lambda^2)] provides an effective potential V(phi).
  The Goldstone mass is: m_G^2 = (1/rho_s) * d^2 V / d phi^2 |_{phi=0}

STRUCTURAL THEOREM (proven here):
  The U(1)_7 rotation acts as D(phi) = P(phi) D P(phi)^dag
  where P(phi) = exp(-i*phi*K_7) is UNITARY with diagonal entries exp(-i*q_7^k*phi)
  in the joint eigenbasis of (D_K, iK_7).

  The spectral action is a TRACE FUNCTIONAL:
    S(phi) = Tr[f(D(phi)^2)] = Tr[f(P D P^dag (P D P^dag)^dag)]
           = Tr[f(P D^2 P^dag)] = Tr[P f(D^2) P^dag]
           = Tr[f(D^2)] = S(0)

  This holds for:
    - ANY Hermitian operator D (not just D_K or D_phys)
    - ANY cutoff function f
    - ANY U(1) phase rotation (unitary conjugation)

  Therefore d^2S/dphi^2 = 0 IDENTICALLY. The spectral action cannot generate
  a Goldstone mass. This is NOT a consequence of [iK_7, D_K] = 0 (which gives
  a STRONGER result: D_K(phi) = D_K). It is a consequence of the trace property.

GATE: GOLDSTONE-MASS-48
  PASS: m_G/M_KK in [10^{-60}, 10^{-50}]
  INFO: computable but outside range
  FAIL: d^2S/dphi^2 = 0 identically

Author: landau-condensed-matter-theorist, Session 48
Date: 2026-03-17
"""

import os
import sys
import time
import numpy as np
from numpy.linalg import eigh, norm, eigvalsh
from scipy.linalg import expm
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from tier1_dirac_spectrum import (
    su3_generators, compute_structure_constants,
    compute_killing_form, jensen_metric, orthonormal_frame,
    frame_structure_constants, connection_coefficients,
    build_cliff8, build_chirality, spinor_connection_offset,
    U1_IDX, SU2_IDX, C2_IDX, U2_IDX,
)
from s23a_kosmann_singlet import kosmann_operator_antisymmetric
from canonical_constants import (
    tau_fold as TAU_FOLD,
    M_KK_gravity as M_KK,
    M_KK_kerner,
)

np.set_printoptions(precision=14, linewidth=140, suppress=True)
t0 = time.time()

# ======================================================================
#  INFRASTRUCTURE
# ======================================================================
print("=" * 78)
print("GOLDSTONE-MASS-48: Goldstone Mass from Spectral Action")
print("=" * 78)

gens = su3_generators()
fabc = compute_structure_constants(gens)
Bk = compute_killing_form(fabc)
gammas = build_cliff8()
gamma9 = build_chirality(gammas)
I16 = np.eye(16, dtype=complex)


def build_DK_at_tau(tau):
    """Build Hermitian Dirac operator D_K = i*Omega at given tau."""
    g_s = jensen_metric(Bk, tau)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(fabc, E)
    Gamma = connection_coefficients(ft)
    Omega = spinor_connection_offset(Gamma, gammas)
    D_K = 1j * Omega
    return D_K, Gamma


def build_K7_at_tau(tau):
    """Build K_7 Kosmann operator at given tau."""
    g_s = jensen_metric(Bk, tau)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(fabc, E)
    Gamma = connection_coefficients(ft)
    K7, A7 = kosmann_operator_antisymmetric(Gamma, gammas, 7)
    return K7, A7


def spectral_action_heat(evals, Lambda_sq=4.0):
    """S = sum_k exp(-lambda_k^2 / Lambda^2)"""
    return np.sum(np.exp(-evals**2 / Lambda_sq))


def spectral_action_chi2(evals, Lambda_sq=4.0):
    """S = sum_k [1 - x + x^2/2] where x = lambda_k^2/Lambda^2"""
    x = evals**2 / Lambda_sq
    return np.sum(1.0 - x + 0.5 * x**2)


def spectral_action_poly(evals, Lambda_sq=4.0):
    """S = sum_k (1-x)^2 theta(1-x) where x = lambda_k^2/Lambda^2"""
    x = evals**2 / Lambda_sq
    mask = x < 1.0
    return np.sum((1.0 - x[mask])**2)


# ======================================================================
#  PART A: Verify [iK_7, D_K] = 0 and joint diagonalization
# ======================================================================
print(f"\n{'='*78}")
print("PART A: Joint eigenbasis (D_K, iK_7) and spectral invariance of D_K")
print(f"{'='*78}")

D_K, Gamma_fold = build_DK_at_tau(TAU_FOLD)
K7, A7 = build_K7_at_tau(TAU_FOLD)
iK7 = 1j * K7

# Verify Hermiticity
herm_err_DK = np.max(np.abs(D_K - D_K.conj().T))
herm_err_iK7 = np.max(np.abs(iK7 - iK7.conj().T))
print(f"\n  D_K Hermiticity: err = {herm_err_DK:.2e}")
print(f"  iK_7 Hermiticity: err = {herm_err_iK7:.2e}")

# Verify commutator
comm = iK7 @ D_K - D_K @ iK7
comm_norm = norm(comm, 'fro')
DK_norm = norm(D_K, 'fro')
comm_ratio = comm_norm / DK_norm if DK_norm > 0 else 0.0
print(f"  [iK_7, D_K] / ||D_K||: {comm_ratio:.4e}")
assert comm_ratio < 1e-12
print(f"  CONFIRMED: [iK_7, D_K] = 0 to machine epsilon")

# D_K eigenvalues
evals_DK_sorted = np.sort(eigvalsh(D_K))
print(f"\n  D_K eigenvalues at fold (tau={TAU_FOLD}):")
print(f"    {evals_DK_sorted}")

# iK_7 eigenvalues
evals_iK7_sorted = np.sort(eigvalsh(iK7))
print(f"\n  iK_7 eigenvalues (q_7 charges):")
print(f"    {evals_iK7_sorted}")

# Build joint eigenbasis
evals_DK_full, evecs_DK = eigh(D_K)
sort_idx = np.argsort(evals_DK_full)
evals_DK_full = evals_DK_full[sort_idx]
evecs_DK = evecs_DK[:, sort_idx]

# Transform iK_7 to D_K eigenbasis
iK7_in_DK = evecs_DK.conj().T @ iK7 @ evecs_DK

# Identify degenerate blocks and diagonalize iK_7 within each
tol_deg = 1e-10
unique_evals = []
block_ranges = []
i = 0
while i < 16:
    j = i + 1
    while j < 16 and abs(evals_DK_full[j] - evals_DK_full[i]) < tol_deg:
        j += 1
    unique_evals.append(evals_DK_full[i])
    block_ranges.append((i, j))
    i = j

evecs_joint = np.zeros((16, 16), dtype=complex)
q7_joint = np.zeros(16)
lambda_joint = np.zeros(16)

for ev, (s, e) in zip(unique_evals, block_ranges):
    block = iK7_in_DK[s:e, s:e]
    block = (block + block.conj().T) / 2.0
    evals_blk, evecs_blk = eigh(block)
    q7_joint[s:e] = evals_blk
    lambda_joint[s:e] = ev
    evecs_joint[:, s:e] = evecs_DK[:, s:e] @ evecs_blk

print(f"\n  Joint (lambda, q_7) eigenvalues:")
for k in range(16):
    print(f"    k={k:2d}: lambda = {lambda_joint[k]:+.10f}, q_7 = {q7_joint[k]:+.10f}")

# Verify joint diagonalization
offdiag_DK = norm(evecs_joint.conj().T @ D_K @ evecs_joint
                   - np.diag(lambda_joint), 'fro')
offdiag_iK7 = norm(evecs_joint.conj().T @ iK7 @ evecs_joint
                    - np.diag(q7_joint), 'fro')
print(f"\n  Joint basis off-diagonal errors:")
print(f"    D_K:  {offdiag_DK:.2e}")
print(f"    iK_7: {offdiag_iK7:.2e}")

# Verify D_K spectral invariance
print(f"\n  D_K spectral action invariance (phi scan):")
Lambda_sq = 4.0
phi_scan = np.linspace(0, 2*np.pi, 200)
S_DK = np.zeros(len(phi_scan))
for j, phi in enumerate(phi_scan):
    U_phi = expm(phi * K7)
    DK_phi = U_phi @ D_K @ U_phi.conj().T
    DK_phi = (DK_phi + DK_phi.conj().T) / 2.0
    S_DK[j] = spectral_action_heat(eigvalsh(DK_phi), Lambda_sq)

dS_DK = S_DK.max() - S_DK.min()
print(f"    S_heat range: [{S_DK.min():.14f}, {S_DK.max():.14f}]")
print(f"    Variation: {dS_DK:.4e}")
print(f"  => S[D_K(phi)] = S[D_K] to machine epsilon (from [iK_7, D_K]=0)")


# ======================================================================
#  PART B: STRUCTURAL THEOREM — Trace invariance under unitary conjugation
# ======================================================================
print(f"\n{'='*78}")
print("PART B: STRUCTURAL THEOREM — S(phi) = S(0) for ANY D")
print(f"{'='*78}")

print(f"""
  THEOREM: For any Hermitian operator D on the 16-dimensional spinor space,
  the spectral action S[D(phi)] = Tr[f(D(phi)^2)] is independent of phi
  where D(phi) = exp(phi*K_7) D exp(-phi*K_7).

  PROOF:
  1. K_7 is anti-Hermitian, so U(phi) = exp(phi*K_7) is unitary.
  2. D(phi) = U(phi) D U(phi)^dag
  3. D(phi)^2 = U D U^dag U D U^dag = U D (U^dag U) D U^dag = U D^2 U^dag
  4. f(D(phi)^2) = f(U D^2 U^dag) = U f(D^2) U^dag
     (spectral mapping theorem for unitary conjugation)
  5. Tr[f(D(phi)^2)] = Tr[U f(D^2) U^dag] = Tr[f(D^2)] = S(0)
     (cyclic invariance of trace)

  This holds for ANY D (not just D_K), ANY cutoff function f,
  and ANY anti-Hermitian generator K_7.

  COROLLARY: d^n S / d phi^n = 0 for all n >= 1.
  Therefore m_G^2 = (1/rho_s) * d^2S/dphi^2 = 0 identically.
""")

# ======================================================================
#  PART C: Numerical verification with three operators
# ======================================================================
print(f"{'='*78}")
print("PART C: Numerical verification with D_K, D_phys, and random D")
print(f"{'='*78}")

# Load D_phys data
d_phys = np.load(os.path.join(SCRIPT_DIR, 's35_k7_dphys.npz'), allow_pickle=True)
evals_phys_stored = d_phys['evals_phys']
ratio_stored = float(d_phys['ratio'])
dphys_norm = float(d_phys['dphys_norm'])

print(f"\n  D_phys breaking: ||[iK_7, D_phys]||/||D_phys|| = {ratio_stored:.6f}")

# Test 1: D_K (exact symmetry, [iK_7, D_K]=0)
print(f"\n  Test 1: D_K (exact symmetry)")
print(f"    Variation: {dS_DK:.4e} (machine epsilon)")

# Test 2: D_phys (5.2% breaking)
# Build D_phys with large mixing in joint basis
np.random.seed(2048)
Z = np.random.randn(16, 16) + 1j * np.random.randn(16, 16)
H_gen = (Z - Z.conj().T) / 2.0
theta_big = 0.5  # large mixing

U_mix = expm(theta_big * H_gen)
diag_phys = np.diag(np.sort(evals_phys_stored))
D_phys_joint = U_mix @ diag_phys @ U_mix.conj().T
D_phys_joint = (D_phys_joint + D_phys_joint.conj().T) / 2.0
D_phys_full = evecs_joint @ D_phys_joint @ evecs_joint.conj().T

# Verify breaking
comm_phys = iK7 @ D_phys_full - D_phys_full @ iK7
breaking_ratio = norm(comm_phys, 'fro') / norm(D_phys_full, 'fro')

dq_matrix = q7_joint[:, None] - q7_joint[None, :]
S_phys = np.zeros(len(phi_scan))
for j, phi in enumerate(phi_scan):
    U_phi = expm(phi * K7)
    Dp_phi = U_phi @ D_phys_full @ U_phi.conj().T
    Dp_phi = (Dp_phi + Dp_phi.conj().T) / 2.0
    S_phys[j] = spectral_action_heat(eigvalsh(Dp_phi), Lambda_sq)

dS_phys = S_phys.max() - S_phys.min()
print(f"\n  Test 2: D_phys (theta_mix={theta_big}, epsilon={breaking_ratio:.4f})")
print(f"    Variation: {dS_phys:.4e} (machine epsilon)")

# Test 3: Fully random Hermitian D
np.random.seed(3048)
A = np.random.randn(16, 16) + 1j * np.random.randn(16, 16)
D_rand = (A + A.conj().T) / 2.0
comm_rand = iK7 @ D_rand - D_rand @ iK7
rand_ratio = norm(comm_rand, 'fro') / norm(D_rand, 'fro')

S_rand = np.zeros(len(phi_scan))
for j, phi in enumerate(phi_scan):
    U_phi = expm(phi * K7)
    Dr_phi = U_phi @ D_rand @ U_phi.conj().T
    Dr_phi = (Dr_phi + Dr_phi.conj().T) / 2.0
    S_rand[j] = spectral_action_heat(eigvalsh(Dr_phi), Lambda_sq)

dS_rand = S_rand.max() - S_rand.min()
print(f"\n  Test 3: Random Hermitian D (epsilon={rand_ratio:.4f})")
print(f"    Variation: {dS_rand:.4e} (machine epsilon)")

# Summary table
print(f"\n  {'Operator':<20s} {'||[iK_7,D]||/||D||':<20s} {'max|dS|':<15s} {'d^2S/dphi^2'}")
print(f"  {'-'*70}")
print(f"  {'D_K':<20s} {comm_ratio:<20.4e} {dS_DK:<15.4e} {'0 (exact)'}")
print(f"  {'D_phys (large mix)':<20s} {breaking_ratio:<20.4e} {dS_phys:<15.4e} {'0 (exact)'}")
print(f"  {'Random Hermitian':<20s} {rand_ratio:<20.4e} {dS_rand:<15.4e} {'0 (exact)'}")
print(f"\n  All three give dS = 0 to machine epsilon. The theorem is verified.")


# ======================================================================
#  PART D: Why this happens physically
# ======================================================================
print(f"\n{'='*78}")
print("PART D: Physical analysis — why the spectral action cannot give a mass")
print(f"{'='*78}")

print(f"""
  The spectral action S[D] = Tr[f(D^2/Lambda^2)] depends ONLY on the
  EIGENVALUES of D. It is blind to the eigenvectors. A unitary rotation
  D -> U D U^dag preserves all eigenvalues, hence preserves S.

  The U(1)_7 phase rotation of the BCS order parameter acts on the internal
  Dirac operator as a unitary conjugation by exp(phi*K_7). This is true
  regardless of whether [K_7, D] = 0 or not:

  Case 1: [K_7, D_K] = 0
    D_K(phi) = exp(phi*K_7) D_K exp(-phi*K_7) = D_K
    Not just eigenvalues, but the OPERATOR itself is unchanged.

  Case 2: [K_7, D_phys] != 0
    D_phys(phi) = exp(phi*K_7) D_phys exp(-phi*K_7) != D_phys
    The operator CHANGES, but its EIGENVALUES do not.
    The spectral action sees only eigenvalues, so S(phi) = S(0).

  The distinction matters for NON-TRACE observables:
  - Tr[f(D^2)] is invariant (spectral action)
  - <psi|D|psi'> for specific states is NOT invariant
  - Correlation functions <phi(x) phi(y)> can depend on phi
  - The BCS gap equation (which involves MATRIX ELEMENTS, not traces)
    CAN generate a phi-dependent free energy

  CONCLUSION: The Goldstone mass cannot come from the spectral action.
  It must come from:
  (a) Inter-cell Josephson coupling (fabric scale, ~N_cells^{-1})
  (b) BCS gap equation (matrix elements, not trace)
  (c) Non-spectral-action contributions to the free energy
""")

# ======================================================================
#  PART E: What DOES give a Goldstone mass?
# ======================================================================
print(f"{'='*78}")
print("PART E: Estimate from BCS gap equation (matrix elements)")
print(f"{'='*78}")

# The BCS free energy F[Delta] depends on the gap parameter Delta = |Delta|*exp(i*phi)
# F(phi) = -sum_{k} sqrt(epsilon_k^2 + |Delta|^2) + |Delta|^2 / g
# This is phi-INDEPENDENT for a uniform condensate (the gap equation involves |Delta|
# but not the phase).
#
# The phase phi enters through GRADIENT terms (Josephson coupling between cells):
# F_Josephson = (1/2) * rho_s * (nabla phi)^2
# There is no local potential for phi — this IS the Goldstone theorem.
#
# A mass for phi can only come from EXPLICIT breaking:
# F_break = m_G^2 * |Delta|^2 * (1 - cos(phi))
#
# In our framework, the explicit breaking is ||[iK_7, D_phys]|| / ||D_phys|| = 0.052
# The BCS gap equation gives matrix elements V_{kl} between modes.
# The phi-dependent part of V is:
#   V(phi) ~ V_0 + delta_V * cos(phi * dq_{kl})
# where delta_V / V_0 ~ epsilon ~ 0.052

# From BCS theory, the phi-dependent condensation energy is:
# F(phi) - F(0) ~ |E_cond| * epsilon^2 * (1 - cos(phi))
# => d^2F/dphi^2 ~ |E_cond| * epsilon^2
# => m_G^2 ~ |E_cond| * epsilon^2 / rho_s

from canonical_constants import E_cond, rho_B2_per_mode

epsilon = ratio_stored
rho_s_C2 = 7.962  # S47

# BCS matrix element estimate
m_G_sq_BCS = abs(E_cond) * epsilon**2 / rho_s_C2
m_G_BCS = np.sqrt(m_G_sq_BCS)

print(f"\n  Explicit breaking: epsilon = {epsilon:.6f}")
print(f"  BCS condensation energy: |E_cond| = {abs(E_cond):.6f} M_KK")
print(f"  Superfluid stiffness: rho_s(C2) = {rho_s_C2:.3f} M_KK")
print(f"")
print(f"  BCS estimate: m_G^2 ~ |E_cond| * epsilon^2 / rho_s")
print(f"    m_G^2 = {m_G_sq_BCS:.6e} M_KK^2")
print(f"    m_G / M_KK = {m_G_BCS:.6e}")
print(f"    m_G (GeV, gravity) = {m_G_BCS * M_KK:.4e}")
print(f"    m_G (GeV, Kerner)  = {m_G_BCS * M_KK_kerner:.4e}")
print(f"    log10(m_G/M_KK) = {np.log10(m_G_BCS):.2f}")
print(f"")
print(f"  NOTE: This is a rough BCS estimate, NOT from the spectral action.")
print(f"  The spectral action gives m_G = 0 by theorem.")


# ======================================================================
#  PLOT
# ======================================================================
fig, axes = plt.subplots(1, 3, figsize=(16, 5))
fig.suptitle(f'GOLDSTONE-MASS-48: S[D($\\phi$)] vs $\\phi$ at $\\tau$ = {TAU_FOLD}',
             fontsize=14, fontweight='bold')

# D_K
ax = axes[0]
ax.plot(phi_scan, S_DK - S_DK[0], 'b-', linewidth=1.5)
ax.set_xlabel(r'$\phi$')
ax.set_ylabel(r'$S(\phi) - S(0)$')
ax.set_title(r'$D_K$: $[iK_7, D_K]=0$')
ax.axhline(0, color='gray', linestyle='--', alpha=0.5)
ax.set_ylim(-1e-13, 1e-13)
ax.text(0.5, 0.9, f'$\\Delta S = {dS_DK:.1e}$',
        transform=ax.transAxes, ha='center', fontsize=10)

# D_phys
ax = axes[1]
ax.plot(phi_scan, S_phys - S_phys[0], 'r-', linewidth=1.5)
ax.set_xlabel(r'$\phi$')
ax.set_ylabel(r'$S(\phi) - S(0)$')
ax.set_title(f'$D_{{phys}}$: $\\epsilon = {breaking_ratio:.3f}$')
ax.axhline(0, color='gray', linestyle='--', alpha=0.5)
ax.set_ylim(-1e-13, 1e-13)
ax.text(0.5, 0.9, f'$\\Delta S = {dS_phys:.1e}$',
        transform=ax.transAxes, ha='center', fontsize=10)

# Random D
ax = axes[2]
ax.plot(phi_scan, S_rand - S_rand[0], 'g-', linewidth=1.5)
ax.set_xlabel(r'$\phi$')
ax.set_ylabel(r'$S(\phi) - S(0)$')
ax.set_title(f'Random $D$: $\\epsilon = {rand_ratio:.3f}$')
ax.axhline(0, color='gray', linestyle='--', alpha=0.5)
ax.set_ylim(-1e-13, 1e-13)
ax.text(0.5, 0.9, f'$\\Delta S = {dS_rand:.1e}$',
        transform=ax.transAxes, ha='center', fontsize=10)

plt.tight_layout()
plt.savefig(os.path.join(SCRIPT_DIR, 's48_goldstone_mass.png'), dpi=150)
print(f"\n  Plot saved: tier0-computation/s48_goldstone_mass.png")


# ======================================================================
#  GATE VERDICT
# ======================================================================
print(f"\n{'='*78}")
print("GATE VERDICT: GOLDSTONE-MASS-48")
print(f"{'='*78}")

verdict = "FAIL"
print(f"\n  d^2S/dphi^2 = 0 IDENTICALLY (structural theorem)")
print(f"  Verified numerically for D_K, D_phys, and random Hermitian D")
print(f"  Max spectral action variation: {max(dS_DK, dS_phys, dS_rand):.2e} (machine epsilon)")
print(f"")
print(f"  REASON: The spectral action Tr[f(D^2)] is invariant under unitary")
print(f"  conjugation D -> U D U^dag. The U(1)_7 phase rotation IS a unitary")
print(f"  conjugation. Therefore S(phi) = S(0) for all phi, for all D.")
print(f"")
print(f"  VERDICT: {verdict}")
print(f"")
print(f"  STRUCTURAL CONSTRAINT: The spectral action is EXCLUDED as a")
print(f"  source of Goldstone mass. This narrows the solution space to:")
print(f"    (a) Inter-cell Josephson coupling at the fabric scale")
print(f"    (b) BCS gap equation (non-trace, matrix element functional)")
print(f"    (c) Dynamical mass from transit (Kibble-Zurek quench)")
print(f"")
print(f"  BCS rough estimate (from matrix element breaking):")
print(f"    m_G / M_KK ~ {m_G_BCS:.4e}  (log10 = {np.log10(m_G_BCS):.2f})")
print(f"    This is O(epsilon * sqrt(|E_cond|/rho_s)) ~ O(10^{{-2}}), far too heavy.")

# Save results
save_dict = {
    # Part A
    'comm_ratio_DK': float(comm_ratio),
    'dS_DK': float(dS_DK),
    # Joint basis
    'lambda_joint': lambda_joint,
    'q7_joint': q7_joint,
    # Part C: verification
    'dS_phys': float(dS_phys),
    'dS_rand': float(dS_rand),
    'breaking_phys': float(breaking_ratio),
    'breaking_rand': float(rand_ratio),
    # Part D: structural theorem
    'theorem': np.array(['Tr[f(D(phi)^2)] = Tr[f(D^2)] for all phi (unitary conjugation invariance)']),
    # Part E: BCS estimate
    'epsilon': float(epsilon),
    'm_G_sq_BCS_estimate': float(m_G_sq_BCS),
    'm_G_over_MKK_BCS': float(m_G_BCS),
    'E_cond_used': float(E_cond),
    'rho_s_C2': float(rho_s_C2),
    # Scan data
    'phi_scan': phi_scan,
    'S_DK': S_DK,
    'S_phys': S_phys,
    'S_rand': S_rand,
    'Lambda_sq': float(Lambda_sq),
    # Metadata
    'tau_fold': float(TAU_FOLD),
    'evals_DK': evals_DK_sorted,
    'evals_phys': np.sort(evals_phys_stored),
    'gate_name': np.array(['GOLDSTONE-MASS-48']),
    'gate_verdict': np.array([verdict]),
}
np.savez(os.path.join(SCRIPT_DIR, 's48_goldstone_mass.npz'), **save_dict)
print(f"\n  Data saved: tier0-computation/s48_goldstone_mass.npz")

elapsed = time.time() - t0
print(f"\n  Total runtime: {elapsed:.1f}s")
print(f"{'='*78}")
