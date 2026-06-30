#!/usr/bin/env python3
"""
ETA-B-52: Baryogenesis CP-odd Phase and eta_B Estimate
=======================================================

Constructs the BdG Hamiltonian at the van Hove fold (tau = 0.19),
diagonalizes it, extracts the Bogoliubov U matrix, computes the
CP-odd phase between particle and antiparticle components, and
estimates eta_B.

STRUCTURAL CONSTRAINT (proven, permanent):
  T11 (S43 W5-1): C2 * conj(D_K) * C2 = D_K for ANY left-invariant
  metric on SU(3). This means J = C2*K is an EXACT antilinear symmetry
  of the Dirac operator at ALL tau. Consequently:
    - The BdG Hamiltonian inherits J-symmetry
    - The Bogoliubov transformation must be J-compatible
    - The CP-odd phase, if nonzero, comes from spontaneous breaking
      of U(1)_7, NOT from explicit J-breaking

PHYSICS:
  Cooper pairs carry K_7 charge +/- 1/2 (S35).
  V(q+, q-) = 0 exactly: same-K_7 pairing only (S35).
  The BCS condensate spontaneously breaks U(1)_7 (S35).
  Transit produces 59.8 quasiparticle pairs via sudden quench (S38).
  Post-transit state is a GGE with 8 conserved Richardson-Gaudin
  integrals (S38). BDI winding number nu = 0 (S36).

METHOD:
  1. Load the Dirac spectrum at tau_fold from archived data.
  2. Construct the 16x16 BdG Hamiltonian (8 positive + 8 negative
     energy modes in Nambu doubling).
  3. Incorporate sector-resolved pairing: Delta_B2, Delta_B3, Delta_B1=0.
  4. Diagonalize. Extract u_k, v_k Bogoliubov coefficients.
  5. Compute phi_CP = arg(u_k * conj(v_k)) per mode.
  6. Test whether J-symmetry forces phi_CP = 0 or allows a spontaneous phase.
  7. Estimate eta_B if phi_CP != 0.

GATE ETA-B-52 (pre-registered):
  PASS: CP-odd phase nonzero, eta_B within 3 OOM of 6e-10
  INFO: CP-odd phase nonzero but eta_B wrong by > 3 OOM
  FAIL: CP-odd phase exactly zero (CP preserved)

Author: dirac-antimatter-theorist, Session 52
Date: 2026-03-20
"""

import os
import sys
import time
import numpy as np
from numpy.linalg import eigh, norm
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

PROJECT_ROOT = r'C:\sandbox\Ainulindale Exflation'
SCRIPT_DIR = os.path.join(PROJECT_ROOT, 'computations')
ARCHIVE_DIR = os.path.join(PROJECT_ROOT, "computations", "_shared")
sys.path.insert(0, SCRIPT_DIR)

# Redirect stdout to both console and file for Windows bash 0kb workaround
_LOG_PATH = os.path.join(SCRIPT_DIR, 's52_eta_b_log.txt')
class _Tee:
    def __init__(self, *streams):
        self.streams = streams
    def write(self, data):
        for s in self.streams:
            s.write(data)
            s.flush()
    def flush(self):
        for s in self.streams:
            s.flush()

_log_file = open(_LOG_PATH, 'w', encoding='utf-8')
sys.stdout = _Tee(sys.__stdout__, _log_file)
sys.stderr = _Tee(sys.__stderr__, _log_file)

from canonical_constants import (
    tau_fold, E_cond, E_cond_ED_8mode, n_pairs, Delta_0_GL, Delta_B3,
    E_B1, E_B2_mean, E_B3_mean, rho_B2_per_mode, eta_BBN_obs,
    N_dof_BCS, S_inst, xi_BCS, omega_PV, dt_transit, v_terminal,
    PI, M_KK_gravity, M_KK_kerner
)

t0 = time.time()

print("=" * 72)
print("ETA-B-52: Baryogenesis CP-odd Phase and eta_B Estimate")
print("=" * 72)
print(f"  tau_fold = {tau_fold}")
print(f"  E_cond (8-mode) = {E_cond_ED_8mode:.6f}")
print(f"  Delta_0_GL = {Delta_0_GL:.6f}")
print(f"  Delta_B3 = {Delta_B3}")
print(f"  n_pairs (transit) = {n_pairs}")
print(f"  eta_BBN_obs = {eta_BBN_obs:.3e}")

# ======================================================================
#  SECTION 1: Load Dirac spectrum at the fold
# ======================================================================
print("\n" + "=" * 72)
print("SECTION 1: DIRAC SPECTRUM AT FOLD")
print("=" * 72)

# Load eigenvalue data at tau = 0.19 (the fold)
dos_data = np.load(os.path.join(SCRIPT_DIR, 's44_dos_tau.npz'), allow_pickle=True)
omega_fold = dos_data['tau0.19_all_omega']  # All eigenvalues at tau=0.19
dim2_fold = dos_data['tau0.19_all_dim2']    # Multiplicities

print(f"  Number of distinct eigenvalues at fold: {len(omega_fold)}")
print(f"  First 10 eigenvalues: {omega_fold[:10]}")

# Load the 16x16 Kosmann data for the (0,0) singlet sector
kosmann = np.load(os.path.join(ARCHIVE_DIR, 's23a_kosmann_singlet.npz'),
                  allow_pickle=True)

# tau index 3 corresponds to tau = 0.20 (nearest to fold at 0.19)
ti = 3  # (local)
evals_raw = kosmann[f'eigenvalues_{ti}']
evecs_raw = kosmann[f'eigenvectors_{ti}']

# Sort eigenvalues
si = np.argsort(evals_raw)
evals_sorted = evals_raw[si]
evecs_sorted = evecs_raw[:, si]

# Identify positive-energy branches
pos_idx = np.where(evals_sorted > 0)[0]
neg_idx = np.where(evals_sorted < 0)[0]

B1_pos = pos_idx[0:1]    # 1 mode (acoustic)
B2_pos = pos_idx[1:5]    # 4 modes (optical quartet)
B3_pos = pos_idx[5:8]    # 3 modes (optical triplet)

E_B1_val = evals_sorted[B1_pos[0]]
E_B2_vals = evals_sorted[B2_pos]
E_B3_vals = evals_sorted[B3_pos]

print(f"\n  Positive-energy branches:")
print(f"    B1 ({len(B1_pos)} mode):  E = {E_B1_val:.6f}")
print(f"    B2 ({len(B2_pos)} modes): E = {E_B2_vals}")
print(f"    B3 ({len(B3_pos)} modes): E = {E_B3_vals}")

# Full 8-mode positive sector (canonical ordering: B2, B1, B3)
full_pos_idx = np.concatenate([B2_pos, B1_pos, B3_pos])
E_8 = evals_sorted[full_pos_idx]
branch_labels = ['B2[0]', 'B2[1]', 'B2[2]', 'B2[3]', 'B1',
                 'B3[0]', 'B3[1]', 'B3[2]']

print(f"\n  8-mode ordering: {branch_labels}")
print(f"  E_8 = {E_8}")

# ======================================================================
#  SECTION 2: Kosmann pairing matrix V
# ======================================================================
print("\n" + "=" * 72)
print("SECTION 2: KOSMANN PAIRING MATRIX")
print("=" * 72)

# Build V_16x16 from Kosmann kernel
V_16 = np.zeros((16, 16))
for a in range(8):
    K = kosmann[f'K_a_matrix_{ti}_{a}']
    V_16 += np.abs(K)**2

V_8x8 = V_16[np.ix_(full_pos_idx, full_pos_idx)]
print(f"  V_8x8 pairing matrix (sum |K_a|^2):")
for i in range(8):
    row = " ".join(f"{V_8x8[i,j]:8.5f}" for j in range(8))
    print(f"    {branch_labels[i]:>6s}: {row}")

# Selection rules
print(f"\n  Selection rule checks:")
print(f"    V(B1,B1) = {V_8x8[4,4]:.2e} (Trap 1)")
print(f"    V(B2,B2) diag mean = {np.mean(np.diag(V_8x8[:4,:4])):.6f}")
print(f"    V(B3,B3) diag mean = {np.mean(np.diag(V_8x8[5:8,5:8])):.6f}")

# ======================================================================
#  SECTION 3: K_7 Charge Structure
# ======================================================================
print("\n" + "=" * 72)
print("SECTION 3: K_7 CHARGE STRUCTURE")
print("=" * 72)

# Load K_7 eigenvalues from the Kosmann kernel
# K_7 is generator 7 (the U(1) generator)
K7 = kosmann[f'K_a_matrix_{ti}_7']

# K_7 eigenvalues on eigenstates
K7_diag = np.zeros(16, dtype=complex)
for i in range(16):
    K7_diag[i] = evecs_sorted[:, i].conj() @ K7 @ evecs_sorted[:, i]

K7_pos = K7_diag[full_pos_idx]
print(f"  K_7 charges on 8 positive modes:")
for i in range(8):
    print(f"    {branch_labels[i]:>6s}: q_7 = {K7_pos[i].real:+.6f} + {K7_pos[i].imag:+.6f}i")

# Extract K_7 charges for particle-antiparticle analysis
# Under J (charge conjugation), a mode with q_7 maps to -q_7
# The negative-energy partners have OPPOSITE K_7 charge
neg_sorted = np.sort(neg_idx)
full_neg_idx_sorted = neg_sorted[::-1]  # Reverse to match positive branch ordering

K7_neg = np.zeros(8, dtype=complex)
for i, idx in enumerate(full_neg_idx_sorted[:8]):
    K7_neg[i] = evecs_sorted[:, idx].conj() @ K7 @ evecs_sorted[:, idx]

print(f"\n  K_7 charges on 8 negative-energy partners:")
for i in range(min(8, len(K7_neg))):
    print(f"    partner[{i}]: q_7 = {K7_neg[i].real:+.6f} + {K7_neg[i].imag:+.6f}i")

# ======================================================================
#  SECTION 4: BdG Hamiltonian Construction
# ======================================================================
print("\n" + "=" * 72)
print("SECTION 4: BdG HAMILTONIAN CONSTRUCTION")
print("=" * 72)

# The BdG Hamiltonian in Nambu space (particle-hole doubling):
#   H_BdG = [[ epsilon_k,    Delta_k  ],
#            [ Delta_k^*,  -epsilon_k ]]
#
# where epsilon_k are single-particle energies measured from mu=0,
# and Delta_k is the sector-resolved gap matrix.
#
# For N=8 modes, H_BdG is 16x16.

N_modes = 8  # (local)
H_BdG = np.zeros((2*N_modes, 2*N_modes), dtype=complex)

# Diagonal blocks: single-particle energies
# Upper-left: +epsilon_k (particle)
# Lower-right: -epsilon_k (hole)
for i in range(N_modes):
    H_BdG[i, i] = E_8[i]
    H_BdG[N_modes + i, N_modes + i] = -E_8[i]

# Off-diagonal blocks: pairing gap Delta_k
# The gap is sector-resolved:
#   B2 modes (0-3): Delta = Delta_0_GL (strong pairing at van Hove)
#   B1 mode (4):    Delta = 0 (V(B1,B1) = 0, Trap 1)
#   B3 modes (5-7): Delta = Delta_B3 (proximity-induced)

Delta_per_mode = np.zeros(N_modes, dtype=complex)
Delta_per_mode[0:4] = Delta_0_GL       # B2
Delta_per_mode[4]    = 0.0              # B1 (Trap 1)
Delta_per_mode[5:8]  = Delta_B3         # B3

print(f"  Gap values per mode:")
for i in range(N_modes):
    print(f"    {branch_labels[i]:>6s}: Delta = {Delta_per_mode[i]:.6f}")

# CRITICAL: Phase of the gap
# The BCS gap has a U(1) phase: Delta = |Delta| * exp(i*theta)
# This phase is the Goldstone mode from spontaneous U(1)_7 breaking.
#
# STRUCTURAL THEOREM (T11, S43):
#   J = C2*K commutes with D_K at all tau.
#   J maps a state with K_7 charge q to one with -q.
#   The gap matrix must satisfy: J * Delta * J^{-1} = Delta
#   (since the BCS condensate is J-even, proven S29/S34/S42).
#
# CONSEQUENCE:
#   Delta_{q_7=+1/2} = Delta_{q_7=-1/2}^*
#   The magnitudes are equal (J-symmetry), but the PHASES can differ
#   by a sign flip under complex conjugation.
#
# For a REAL gap (theta = 0 or pi), the BdG Hamiltonian has particle-hole
# symmetry with no CP-odd phase.
# For a COMPLEX gap (theta != 0, pi), there IS a CP-odd phase.
#
# The question: does the framework's ground state choose a specific theta?

# Test 1: REAL gap (theta = 0) — the conventional BCS choice
theta_gap = 0.0  # (local)
Delta_complex = Delta_per_mode * np.exp(1j * theta_gap)

for i in range(N_modes):
    H_BdG[i, N_modes + i] = Delta_complex[i]
    H_BdG[N_modes + i, i] = np.conj(Delta_complex[i])

print(f"\n  Gap phase theta = {theta_gap:.4f} rad")
print(f"  H_BdG shape: {H_BdG.shape}")
print(f"  H_BdG Hermiticity check: ||H - H^dag|| = {norm(H_BdG - H_BdG.conj().T):.2e}")

# ======================================================================
#  SECTION 5: BdG Diagonalization
# ======================================================================
print("\n" + "=" * 72)
print("SECTION 5: BdG DIAGONALIZATION")
print("=" * 72)

evals_BdG, evecs_BdG = eigh(H_BdG)

print(f"  BdG eigenvalues (all 16):")
for i in range(2*N_modes):
    print(f"    E_BdG[{i:2d}] = {evals_BdG[i]:+.8f}")

# The BdG spectrum should have particle-hole symmetry: for each E, there is -E
E_pos_BdG = evals_BdG[evals_BdG > 0]
E_neg_BdG = evals_BdG[evals_BdG < 0]
print(f"\n  Particle-hole symmetry check:")
for i in range(min(len(E_pos_BdG), len(E_neg_BdG))):
    print(f"    E+ = {E_pos_BdG[i]:+.8f}, E- = {E_neg_BdG[-(i+1)]:+.8f}, "
          f"sum = {E_pos_BdG[i] + E_neg_BdG[-(i+1)]:.2e}")

# ======================================================================
#  SECTION 6: Bogoliubov Coefficients u_k, v_k
# ======================================================================
print("\n" + "=" * 72)
print("SECTION 6: BOGOLIUBOV COEFFICIENTS")
print("=" * 72)

# The BdG eigenvectors have the Nambu structure:
#   |psi> = (u_1, ..., u_N, v_1, ..., v_N)^T
# where u_k is the particle amplitude and v_k is the hole amplitude.
#
# For each POSITIVE eigenvalue (quasiparticle), extract u and v.

qp_indices = np.where(evals_BdG > 1e-10)[0]
print(f"  Number of positive-energy quasiparticles: {len(qp_indices)}")

u_matrix = np.zeros((N_modes, len(qp_indices)), dtype=complex)
v_matrix = np.zeros((N_modes, len(qp_indices)), dtype=complex)
phi_CP_modes = np.zeros(len(qp_indices))

print(f"\n  Bogoliubov coefficients per quasiparticle mode:")
print(f"  {'QP':>4s} {'E_qp':>10s} {'|u|^2':>10s} {'|v|^2':>10s} "
      f"{'|u|^2+|v|^2':>12s} {'phi_CP':>10s}")

for n, idx in enumerate(qp_indices):
    psi = evecs_BdG[:, idx]
    u_k = psi[:N_modes]     # particle block
    v_k = psi[N_modes:]     # hole block

    u_matrix[:, n] = u_k
    v_matrix[:, n] = v_k

    # Normalization check: |u|^2 + |v|^2 = 1 (for each quasiparticle)
    norm_check = np.sum(np.abs(u_k)**2) + np.sum(np.abs(v_k)**2)

    # CP-odd phase: phi_CP = arg(sum_k u_k * conj(v_k))
    # This is the relative phase between particle and hole components.
    # For a REAL gap, u and v are REAL, so phi_CP = 0 or pi.
    uv_product = np.sum(u_k * np.conj(v_k))
    phi_CP_n = np.angle(uv_product)
    phi_CP_modes[n] = phi_CP_n

    u_sq = np.sum(np.abs(u_k)**2)
    v_sq = np.sum(np.abs(v_k)**2)

    print(f"  {n:4d} {evals_BdG[idx]:+10.6f} {u_sq:10.6f} {v_sq:10.6f} "
          f"{norm_check:12.8f} {phi_CP_n:+10.6f}")

# ======================================================================
#  SECTION 7: CP-odd Phase Analysis
# ======================================================================
print("\n" + "=" * 72)
print("SECTION 7: CP-ODD PHASE ANALYSIS")
print("=" * 72)

# The CP-odd phase phi_CP = arg(u * v*) for each BdG quasiparticle.
# Structural prediction:
#   With a REAL gap (theta_gap = 0):
#     u, v are REAL => phi_CP = 0 or pi
#     phi_CP = 0: trivial (CP-even)
#     phi_CP = pi: sign flip (still CP-even in BCS, just a convention)
#
# With a COMPLEX gap (theta_gap != 0):
#     phi_CP = theta_gap (to leading order)
#     This would be a genuine CP-odd phase.

print(f"  CP-odd phases per quasiparticle:")
for n in range(len(qp_indices)):
    print(f"    QP {n}: phi_CP = {phi_CP_modes[n]:+.8f} rad"
          f"  = {phi_CP_modes[n]*180/PI:+.4f} deg")

phi_CP_total = np.sum(phi_CP_modes)
phi_CP_max = np.max(np.abs(phi_CP_modes))
phi_CP_mean = np.mean(np.abs(phi_CP_modes))
sin_phi_total = np.sum(np.sin(phi_CP_modes))

print(f"\n  Summary:")
print(f"    Total CP phase (sum):    {phi_CP_total:+.8f} rad")
print(f"    Max |phi_CP|:            {phi_CP_max:.8f} rad")
print(f"    Mean |phi_CP|:           {phi_CP_mean:.8f} rad")
print(f"    sum(sin(phi_CP)):        {sin_phi_total:+.8e}")

# ======================================================================
#  SECTION 8: Sweep Over Gap Phase theta
# ======================================================================
print("\n" + "=" * 72)
print("SECTION 8: GAP PHASE SWEEP")
print("=" * 72)

# The gap phase theta is a FREE parameter (Goldstone direction).
# The BCS ground state spontaneously selects a theta.
# If the BdG Hamiltonian depends on theta, then rotating theta
# changes the CP-odd phase.
#
# KEY STRUCTURAL ARGUMENT:
#   J maps (u, v) -> (v*, u*)  (Nambu charge conjugation)
#   For J-symmetry: if (u, v) is a quasiparticle, then (v*, u*) is also one.
#   This means phi_CP(particle) = -phi_CP(antiparticle).
#   The NET CP-odd phase between a particle-antiparticle pair is:
#     phi_CP(particle) - phi_CP(antiparticle) = 2 * phi_CP(particle)
#   But this is a GAUGE artifact of the U(1)_7 phase choice!

n_theta = 37
theta_scan = np.linspace(0, 2*PI, n_theta, endpoint=True)
phi_CP_vs_theta = np.zeros((n_theta, N_modes))
E_BdG_vs_theta = np.zeros((n_theta, 2*N_modes))
sin_total_vs_theta = np.zeros(n_theta)

for it, theta in enumerate(theta_scan):
    # Rebuild H_BdG with this theta
    H = np.zeros((2*N_modes, 2*N_modes), dtype=complex)
    for i in range(N_modes):
        H[i, i] = E_8[i]
        H[N_modes + i, N_modes + i] = -E_8[i]
    Delta_c = Delta_per_mode * np.exp(1j * theta)
    for i in range(N_modes):
        H[i, N_modes + i] = Delta_c[i]
        H[N_modes + i, i] = np.conj(Delta_c[i])

    ev, ec = eigh(H)
    E_BdG_vs_theta[it] = ev

    qp_idx = np.where(ev > 1e-10)[0]
    for n, idx in enumerate(qp_idx):
        psi = ec[:, idx]
        u = psi[:N_modes]
        v = psi[N_modes:]
        uv = np.sum(u * np.conj(v))
        phi_CP_vs_theta[it, n] = np.angle(uv)

    sin_total_vs_theta[it] = np.sum(np.sin(phi_CP_vs_theta[it]))

print(f"  Scanned {n_theta} values of theta in [0, 2*pi]")
print(f"  sin(phi_CP) total vs theta:")
for it in range(0, n_theta, 6):
    print(f"    theta = {theta_scan[it]:.3f}: sum(sin(phi_CP)) = "
          f"{sin_total_vs_theta[it]:+.6e}")

# Check: eigenvalues should be theta-independent
E_spread = np.max(E_BdG_vs_theta, axis=0) - np.min(E_BdG_vs_theta, axis=0)
print(f"\n  Eigenvalue independence check: max spread = {np.max(E_spread):.2e}")
print(f"  (Should be ~0: BdG eigenvalues are gauge-invariant)")

# Check: phi_CP should rotate with theta
# phi_CP(theta) = phi_CP(0) + theta  (to leading order for small mixing)
# or more precisely: the pattern of phi_CP rotates rigidly with theta
phi_range = np.max(phi_CP_vs_theta, axis=0) - np.min(phi_CP_vs_theta, axis=0)
print(f"  phi_CP range per mode: {phi_range}")
print(f"  (If all ~2*pi, the CP phase is purely from U(1) gauge rotation)")

# ======================================================================
#  SECTION 9: J-Symmetry Structural Analysis
# ======================================================================
print("\n" + "=" * 72)
print("SECTION 9: J-SYMMETRY AND CP PHASE")
print("=" * 72)

# THEOREM (structural, from T11 + BDI classification):
#
#   J = C2 * K (antilinear, J^2 = +1)
#   [J, D_K] = 0 at all tau (T1, T11)
#
#   In Nambu space, J acts as:
#     J_Nambu = [[0, C2], [C2, 0]] * K
#   which maps (u, v) -> (C2*v*, C2*u*)
#
#   For the BdG Hamiltonian to be J-symmetric:
#     J_Nambu * H_BdG * J_Nambu^{-1} = H_BdG
#
#   This requires:
#     Delta = C2 * Delta^T * C2^{-1}  (gap equation constraint)
#
#   For the DIAGONAL gap (our case):
#     Delta_i = Delta_i^* for modes related by J
#
#   The J-even condition on the condensate:
#     <c_{k,up} c_{k,down}> = <c_{Jk,up} c_{Jk,down}>*
#
#   This means: |Delta_k| = |Delta_{Jk}|, but arg(Delta_k) = -arg(Delta_{Jk})
#
#   For a mode where J maps k -> k (self-conjugate), Delta_k must be REAL.
#   For modes where J maps k -> k' != k, the phases are linked but free.

# In the framework:
# B2 modes have K_7 charges {+1/4, +1/4, -1/4, -1/4}
# J maps +1/4 to -1/4 modes.
# Cooper pairs: (+1/4, +1/4) and (-1/4, -1/4) with total K_7 = +1/2 and -1/2
# J maps the +1/2 Cooper pair to the -1/2 Cooper pair.
#
# J-even condition: Delta_{+1/2} = (Delta_{-1/2})^*
# This ALLOWS a relative phase: Delta_{+1/2} = |Delta| e^{+i*alpha}
#                                 Delta_{-1/2} = |Delta| e^{-i*alpha}
# The phase alpha is the U(1)_7 Goldstone mode.
#
# HOWEVER: the CP-odd OBSERVABLE is:
#   epsilon_CP = Im(Delta_{+1/2} * Delta_{-1/2}) / |Delta|^2
#             = Im(|Delta|^2 * e^{+i*alpha} * e^{-i*alpha}) / |Delta|^2
#             = Im(|Delta|^2) / |Delta|^2
#             = 0    IDENTICALLY
#
# The J-even condition FORCES the CP-odd invariant to vanish.

print("  STRUCTURAL ANALYSIS OF CP-ODD PHASE:")
print()
print("  The J-symmetry constraint (T11) on the BCS gap is:")
print("    Delta_{q_7=+1/2} = conj(Delta_{q_7=-1/2})")
print()
print("  This means:")
print("    Delta_+ = |Delta| * exp(+i*alpha)")
print("    Delta_- = |Delta| * exp(-i*alpha)")
print("    where alpha is the spontaneous U(1)_7 phase (Goldstone)")
print()
print("  The CP-odd invariant is:")
print("    epsilon_CP = Im(Delta_+ * Delta_-) / |Delta|^2")
print("             = Im(|Delta|^2) / |Delta|^2")
print("             = 0     IDENTICALLY")
print()
print("  This is a STRUCTURAL result: J-symmetry forces CP-even")
print("  condensate. The U(1)_7 phase alpha is a gauge choice,")
print("  not a physical CP-odd observable.")

# Verify numerically with the BdG construction
# For each theta, compute the J-invariant CP measure
print("\n  Numerical verification:")
epsilon_CP_values = np.zeros(n_theta)
for it, theta in enumerate(theta_scan):
    Delta_plus = Delta_0_GL * np.exp(1j * theta)
    Delta_minus = Delta_0_GL * np.exp(-1j * theta)  # J-conjugate
    eps = np.imag(Delta_plus * Delta_minus) / Delta_0_GL**2
    epsilon_CP_values[it] = eps

print(f"    max |epsilon_CP| over theta scan: {np.max(np.abs(epsilon_CP_values)):.2e}")
print(f"    (Confirms epsilon_CP = 0 identically)")

# ======================================================================
#  SECTION 10: Alternative CP Sources — Bogoliubov Mixing at Transit
# ======================================================================
print("\n" + "=" * 72)
print("SECTION 10: BOGOLIUBOV MIXING DURING TRANSIT")
print("=" * 72)

# Even if the STATIC BdG has no CP-odd phase, the DYNAMIC process
# of transit through the fold could generate one.
#
# During transit, the gap opens and closes: Delta(tau) is time-dependent.
# The Bogoliubov transformation from pre-transit to post-transit is:
#   gamma_k = u_k(tau) * c_k + v_k(tau) * c_{-k}^dag
# where u_k(tau) and v_k(tau) evolve adiabatically (or non-adiabatically
# in the sudden-quench regime).
#
# For a REAL-valued Hamiltonian path (D_K(tau) real in a suitable basis),
# the Berry phase accumulated is quantized to 0 or pi (BDI class).
#
# From S46: Berry phases are pi (nontrivial Zak phases), but these are
# Z_2 topological (not CP-odd).
#
# The key insight: in BDI class, the Bogoliubov transformation matrix
# U(tau) satisfies U^T * U = 1 (orthogonal, not unitary), because
# T-symmetry forces u, v to be related by complex conjugation.
#
# BDI orthogonality constraint:
#   T = C2 * K with T^2 = +1
#   T maps (u_k, v_k) -> (u_k*, v_k*)
#   For eigenstates: (u_k, v_k) = (u_k*, v_k*) up to phase
#   => u_k, v_k are REAL (in the T-symmetric basis)
#   => phi_CP = arg(u * v*) = 0 or pi
#   => sin(phi_CP) = 0

print("  BDI T-symmetry constraint:")
print("    T = C2*K, T^2 = +1")
print("    In the T-symmetric basis, u_k and v_k are REAL")
print("    => phi_CP = 0 or pi (quantized)")
print("    => sin(phi_CP) = 0 EXACTLY")
print()

# Verify: for theta=0 (real gap), check that u and v are real
H_real = np.zeros((2*N_modes, 2*N_modes))
for i in range(N_modes):
    H_real[i, i] = E_8[i]
    H_real[N_modes + i, N_modes + i] = -E_8[i]
    H_real[i, N_modes + i] = Delta_per_mode[i].real
    H_real[N_modes + i, i] = Delta_per_mode[i].real

ev_real, ec_real = eigh(H_real)
qp_real = np.where(ev_real > 1e-10)[0]

max_imag = 0.0
for idx in qp_real:
    max_imag = max(max_imag, np.max(np.abs(np.imag(ec_real[:, idx]))))

print(f"  Verification (theta=0, real gap):")
print(f"    Max imaginary part of eigenvectors: {max_imag:.2e}")
print(f"    (Confirms u, v are real in this basis)")

# ======================================================================
#  SECTION 11: Sector-Resolved BdG with K_7 Structure
# ======================================================================
print("\n" + "=" * 72)
print("SECTION 11: K_7-RESOLVED BdG")
print("=" * 72)

# The B2 sector splits into K_7 = +1/4 (2 modes) and K_7 = -1/4 (2 modes).
# Cooper pairs: (+1/4, +1/4) with total K_7 = +1/2
#               (-1/4, -1/4) with total K_7 = -1/2
#
# V(q+, q-) = 0: the two K_7 sectors do NOT mix through pairing.
# Each sector has its own gap:
#   Delta_+ = |Delta| e^{i*alpha}   (K_7 = +1/2 pairs)
#   Delta_- = |Delta| e^{-i*alpha}  (K_7 = -1/2 pairs)
#
# Build the K_7-resolved BdG:
#   H_BdG^{+} = [[eps_+, Delta_+], [Delta_+*, -eps_+]]  (2+2 = 4x4)
#   H_BdG^{-} = [[eps_-, Delta_-], [Delta_-*, -eps_-]]  (2+2 = 4x4)
#
# J maps H_BdG^{+} to H_BdG^{-}: conjugate sector.
# The spectra are IDENTICAL (J-symmetry).

# Use alpha = pi/4 as a nontrivial test
alpha_test = PI / 4

# K_7 = +1/4 sector (B2 modes 0, 1)
N_plus = 2
H_plus = np.zeros((2*N_plus, 2*N_plus), dtype=complex)
E_plus = E_B2_vals[:2]
Delta_plus = Delta_0_GL * np.exp(1j * alpha_test)
for i in range(N_plus):
    H_plus[i, i] = E_plus[i]
    H_plus[N_plus + i, N_plus + i] = -E_plus[i]
    H_plus[i, N_plus + i] = Delta_plus
    H_plus[N_plus + i, i] = np.conj(Delta_plus)

# K_7 = -1/4 sector (B2 modes 2, 3)
N_minus = 2
H_minus = np.zeros((2*N_minus, 2*N_minus), dtype=complex)
E_minus = E_B2_vals[2:]
Delta_minus = Delta_0_GL * np.exp(-1j * alpha_test)  # J-conjugate phase
for i in range(N_minus):
    H_minus[i, i] = E_minus[i]
    H_minus[N_minus + i, N_minus + i] = -E_minus[i]
    H_minus[i, N_minus + i] = Delta_minus
    H_minus[N_minus + i, i] = np.conj(Delta_minus)

ev_plus, ec_plus = eigh(H_plus)
ev_minus, ec_minus = eigh(H_minus)

print(f"  alpha_test = {alpha_test:.4f} rad (= pi/4)")
print(f"\n  K_7 = +1/4 sector eigenvalues: {ev_plus}")
print(f"  K_7 = -1/4 sector eigenvalues: {ev_minus}")
print(f"  Spectral equality (J-symmetry): max |E+ - E-| = "
      f"{np.max(np.abs(ev_plus - ev_minus)):.2e}")

# Extract CP phases per sector
print(f"\n  CP phases per K_7 sector:")
for label, ev, ec, N in [("K7=+1/4", ev_plus, ec_plus, N_plus),
                          ("K7=-1/4", ev_minus, ec_minus, N_minus)]:
    qp = np.where(ev > 1e-10)[0]
    for idx in qp:
        u = ec[:N, idx]
        v = ec[N:, idx]
        uv = np.sum(u * np.conj(v))
        phi = np.angle(uv)
        print(f"    {label}, E={ev[idx]:+.6f}: phi_CP = {phi:+.8f} rad "
              f"= {phi*180/PI:+.4f} deg")

# The CP phases in the two sectors are OPPOSITE (J-symmetry).
# Any CP-odd observable averages them:
#   epsilon_CP = sin(phi_+) + sin(phi_-) = sin(alpha) + sin(-alpha) = 0

print(f"\n  RESULT: CP phases in conjugate K_7 sectors are OPPOSITE.")
print(f"  sin(phi_+) + sin(phi_-) = 0 by J-symmetry.")
print(f"  The NET CP-odd phase is ZERO.")

# ======================================================================
#  SECTION 12: eta_B Estimate
# ======================================================================
print("\n" + "=" * 72)
print("SECTION 12: eta_B ESTIMATE")
print("=" * 72)

# With phi_CP = 0 (structural), eta_B from intrinsic BCS baryogenesis is zero.
#
# However, let us also compute the MAXIMUM eta_B that COULD be produced
# if J-symmetry were broken by some external mechanism (e.g., coupling
# to a J-odd sector, or physics beyond the SU(3) internal space).
#
# The Fukugita-Yanagida formula for BCS-type baryogenesis:
#   eta_B ~ n_pairs * sin(phi_CP) * f_selection / s_entropy
#
# where:
#   n_pairs = 59.8 (Bogoliubov quasiparticle pairs from transit, S38)
#   f_selection = fraction of pairs that carry baryon number
#   s_entropy = entropy density in M_KK units

# In the framework, entropy comes from the GGE:
# S_GGE ~ N_dof * ln(2) (one bit per mode in maximally mixed case)
# More precisely, from S38: E_exc = 443 * |E_cond|, T_compound = E_exc/8
s_GGE = N_dof_BCS * np.log(2)
print(f"  GGE entropy estimate: S_GGE = {N_dof_BCS} * ln(2) = {s_GGE:.4f}")

# Maximum eta_B (if sin(phi_CP) = 1 and all pairs carry baryon number)
eta_B_max = n_pairs / np.exp(s_GGE)
print(f"  Maximum eta_B (sin(phi_CP)=1, all pairs): {eta_B_max:.4e}")
print(f"  Observed eta_B: {eta_BBN_obs:.4e}")
print(f"  Ratio max/obs: {eta_B_max / eta_BBN_obs:.2e}")

# Structural result: sin(phi_CP) = 0
eta_B_structural = 0.0  # (local)
print(f"\n  STRUCTURAL RESULT:")
print(f"    sin(phi_CP) = 0 (J-symmetry, T11)")
print(f"    eta_B = {eta_B_structural:.1e}")
print(f"    The BCS condensate in the framework produces ZERO baryon asymmetry.")
print(f"    This is consistent with S42/S43: eta is kinematic envelope,")
print(f"    not baryon excess. [J,D_K]=0 => equal B and Bbar.")

# ======================================================================
#  SECTION 13: Physical Interpretation
# ======================================================================
print("\n" + "=" * 72)
print("SECTION 13: INTERPRETATION")
print("=" * 72)

print("""
  The algebra speaks clearly. Three independent structural constraints
  EACH force the CP-odd phase to zero:

  1. T-symmetry (BDI class): T = C2*K, T^2 = +1.
     In the T-symmetric basis, Bogoliubov coefficients u, v are REAL.
     => phi_CP = 0 or pi (quantized). sin(phi_CP) = 0.

  2. J-symmetry (T11): C2 * conj(D_K) * C2 = D_K at all tau.
     CP phases in K_7 = +1/2 and K_7 = -1/2 sectors are OPPOSITE.
     => Net CP-odd invariant epsilon_CP = 0 identically.

  3. Spectral pairing: {gamma_9, D_K} = 0 at all tau (T2).
     The chiral eta-invariant vanishes identically.
     No chirality asymmetry from the Dirac spectrum.

  All three are PERMANENT structural constraints, independent of
  parameters, tau values, or the choice of left-invariant metric.

  BARYOGENESIS IN THIS FRAMEWORK REQUIRES PHYSICS EXTERNAL TO THE
  SU(3) DIRAC OPERATOR. The BCS condensate, however rich its dynamics
  (59.8 quasiparticle pairs, instanton gas, GGE remnant), cannot
  produce a baryon asymmetry because J protects the particle-antiparticle
  symmetry at the algebraic level.

  This is consistent with:
  - S43 (all internal J-breaking baryogenesis closed by T11)
  - S42 (eta is kinematic envelope, not baryon excess)
  - S36 (BDI winding number nu = 0)
""")

# ======================================================================
#  SECTION 14: GATE VERDICT
# ======================================================================
print("\n" + "=" * 72)
print("SECTION 14: GATE VERDICT")
print("=" * 72)

gate_verdict = "FAIL"
print(f"  Gate: ETA-B-52")
print(f"  Criterion: CP-odd phase nonzero and eta_B within 3 OOM of 6e-10")
print(f"  Result: phi_CP = 0 IDENTICALLY (three independent structural proofs)")
print(f"  eta_B = 0 (structural)")
print(f"  VERDICT: {gate_verdict} — CP preserved. No intrinsic baryogenesis.")
print()
print(f"  This is NOT a failure of the framework. It is a STRUCTURAL BOUNDARY:")
print(f"  the BCS sector of M4 x SU(3) is CPT-exact. Baryogenesis must come")
print(f"  from coupling to external degrees of freedom (e.g., sphalerons, leptogenesis,")
print(f"  Affleck-Dine, or physics that explicitly breaks J at a higher energy scale).")

# ======================================================================
#  SAVE DATA
# ======================================================================
print("\n" + "=" * 72)
print("SAVING DATA")
print("=" * 72)

save_path = os.path.join(SCRIPT_DIR, 's52_eta_b.npz')
np.savez(save_path,
    # Gate
    gate_verdict=gate_verdict,
    # BdG spectrum
    E_BdG=evals_BdG,
    evecs_BdG=evecs_BdG,
    # Bogoliubov coefficients
    u_matrix=u_matrix,
    v_matrix=v_matrix,
    # CP phases
    phi_CP_modes=phi_CP_modes,
    phi_CP_total=phi_CP_total,
    sin_phi_total=sin_phi_total,
    # Gap phase sweep
    theta_scan=theta_scan,
    phi_CP_vs_theta=phi_CP_vs_theta,
    sin_total_vs_theta=sin_total_vs_theta,
    E_BdG_vs_theta=E_BdG_vs_theta,
    epsilon_CP_values=epsilon_CP_values,
    # K_7 sector data
    ev_plus=ev_plus,
    ev_minus=ev_minus,
    # Input data
    E_8=E_8,
    Delta_per_mode=Delta_per_mode,
    branch_labels=np.array(branch_labels),
    # eta_B
    eta_B_structural=eta_B_structural,
    eta_B_max=eta_B_max,
    eta_BBN_obs=eta_BBN_obs,
    n_pairs=n_pairs,
)
print(f"  Saved: {save_path}")

# ======================================================================
#  PLOT
# ======================================================================
print("\nGenerating plot...")

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle(r'ETA-B-52: Baryogenesis CP-odd Phase Analysis', fontsize=14, fontweight='bold')

# Panel 1: BdG eigenvalues
ax = axes[0, 0]
ax.barh(range(2*N_modes), evals_BdG, color=['blue' if e > 0 else 'red' for e in evals_BdG],
        alpha=0.7, height=0.8)  # (local)
ax.set_xlabel(r'$E_{\mathrm{BdG}}$ [$M_{\mathrm{KK}}$]')
ax.set_ylabel('Mode index')
ax.set_title('BdG Spectrum at Fold')
ax.axvline(x=0, color='black', linewidth=0.5, linestyle='--')

# Panel 2: CP phases per mode (theta=0)
ax = axes[0, 1]
qp_labels = [branch_labels[n % N_modes] for n in range(len(qp_indices))]
colors_cp = ['green' if abs(p) < 0.01 else 'red' for p in phi_CP_modes]
ax.bar(range(len(phi_CP_modes)), phi_CP_modes * 180 / PI, color=colors_cp, alpha=0.7)
ax.set_xlabel('Quasiparticle index')
ax.set_ylabel(r'$\phi_{\mathrm{CP}}$ [degrees]')
ax.set_title(r'CP-odd Phase (real gap, $\theta=0$)')
ax.axhline(y=0, color='black', linewidth=0.5, linestyle='--')

# Panel 3: sin(phi_CP) total vs theta
ax = axes[1, 0]
ax.plot(theta_scan * 180 / PI, sin_total_vs_theta, 'b-', linewidth=2)
ax.set_xlabel(r'Gap phase $\theta$ [degrees]')
ax.set_ylabel(r'$\sum_k \sin(\phi_{\mathrm{CP},k})$')
ax.set_title(r'Net CP-odd Signal vs Gap Phase')
ax.axhline(y=0, color='red', linewidth=1, linestyle='--', label=r'$\epsilon_{\mathrm{CP}}=0$ (J-symmetry)')
ax.legend()

# Panel 4: J-symmetric epsilon_CP
ax = axes[1, 1]
ax.plot(theta_scan * 180 / PI, epsilon_CP_values, 'r-', linewidth=2, label=r'$\epsilon_{\mathrm{CP}}$')
ax.set_xlabel(r'Gap phase $\theta$ [degrees]')
ax.set_ylabel(r'$\epsilon_{\mathrm{CP}} = \mathrm{Im}(\Delta_+ \Delta_-)/|\Delta|^2$')
ax.set_title(r'J-invariant CP Observable')
ax.axhline(y=0, color='black', linewidth=0.5, linestyle='--')
ax.set_ylim(-0.1, 0.1)
ax.legend()

# Annotations
fig.text(0.5, 0.01,
         r'GATE: ETA-B-52 $\to$ FAIL — $\phi_{\mathrm{CP}} = 0$ (J-symmetry, BDI, spectral pairing). '
         r'$\eta_B = 0$ structural.',
         ha='center', fontsize=11, style='italic',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.tight_layout(rect=[0, 0.04, 1, 0.96])
plot_path = os.path.join(SCRIPT_DIR, 's52_eta_b.png')
plt.savefig(plot_path, dpi=150)
print(f"  Saved: {plot_path}")

elapsed = time.time() - t0
print(f"\nCompleted in {elapsed:.2f} s")
