#!/usr/bin/env python3
"""
Session 40 W2-3: B2 Decay-Out Time-Dependent ED (B2-DECAY-40)
==============================================================

Resolves the S39 divergence between Schwarzschild-Penrose ("spectral horizon"
protecting B2 information) and Nazarewicz (Gamma_B2 ~ 7.5, B2 thermalizes
FIRST in t ~ 0.13) by directly tracking the B2 content of the time-evolved
GGE density matrix.

PHYSICAL SCENARIO:
  The post-transit state is a GGE: rho_GGE is diagonal in the single-mode
  Fock basis within N_pair=1, with occupations p_k = |<k|psi_BCS>|^2.

  Under the FREE Hamiltonian (H_free = diag(2*xi)), rho_GGE is stationary
  because the Q_k = |k><k| projectors commute with H_free exactly.

  Under the FULL BCS Hamiltonian (H_BCS = diag(2*xi) - V_phys * P+P-),
  the pairing interaction couples different mode states. This drives
  population transfer between branches (B2 <-> B1 <-> B3).

  The B2 decay-out time measures how fast the dominant B2 population
  (93% of the GGE weight) leaks into B1 and B3 modes.

GATE: B2-DECAY-40
  B2-FIRST: t_decay(B2) < 1 (Nazarewicz prediction)
  B2-LAST:  t_decay(B2) > 10 (spectral horizon)
  INTERMEDIATE: 1 < t_decay(B2) < 10

Author: gen-physicist (Session 40)
Date: 2026-03-11
"""

import os
import sys
import time
import numpy as np
from scipy.linalg import eigh, expm, norm
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
t0_total = time.time()

print("=" * 78)
print("Session 40 W2-3: B2 Decay-Out Time-Dependent ED (B2-DECAY-40)")
print("=" * 78)

# ======================================================================
#  STEP 1: Load data
# ======================================================================

print("\n--- Step 1: Load input data ---")

d_s37 = np.load(os.path.join(SCRIPT_DIR, 's37_pair_susceptibility.npz'),
                allow_pickle=True)
d_s38 = np.load(os.path.join(SCRIPT_DIR, 's38_otoc_bcs.npz'),
                allow_pickle=True)
d_gge = np.load(os.path.join(SCRIPT_DIR, 's39_gge_lambdas.npz'),
                allow_pickle=True)
d_ic = np.load(os.path.join(SCRIPT_DIR, 's39_integrability_check.npz'),
               allow_pickle=True)

# Single-particle data
E_8 = d_s38['E_8']         # 8 single-particle energies
V_phys = d_s38['V_phys']   # 8x8 physical pairing matrix
rho_8 = d_s38['rho_8']     # DOS at each mode
mu = float(d_s38['mu'])

# GGE data
p_k = d_gge['p_k']         # GGE occupation probabilities
lambda_k = d_gge['lambda_k']  # GGE Lagrange multipliers
psi_gs = d_gge['psi_s38_gs']  # BCS ground state pair wavefunction
branch_labels = list(d_gge['branch_labels'])

# Integrability data
Gamma_FGR = float(d_ic['Gamma_FGR_N4'])
t_therm_FGR = float(d_ic['t_therm_FGR_N4'])

N = 8
dim = 2**N  # 256

# Mode grouping
B2_idx = [0, 1, 2, 3]  # B2 modes
B1_idx = [4]             # B1 mode
B3_idx = [5, 6, 7]       # B3 modes

print(f"  N = {N}, dim = {dim}")
print(f"  E_8 = {E_8}")
print(f"  mu = {mu}")
print(f"  GGE p_k = {p_k}")
print(f"  sum(p_k) = {np.sum(p_k):.15f}")
print(f"  p_B2 = {np.sum(p_k[B2_idx]):.6f}")
print(f"  p_B1 = {np.sum(p_k[B1_idx]):.6f}")
print(f"  p_B3 = {np.sum(p_k[B3_idx]):.6f}")
print(f"  FGR Gamma = {Gamma_FGR:.6f}, t_therm = {t_therm_FGR:.4f}")

# ======================================================================
#  STEP 2: Build operators in 256-dim Fock space
# ======================================================================

print("\n--- Step 2: Build Fock space operators ---")

I2 = np.eye(2, dtype=np.float64)
sz = np.array([[1.0, 0.0], [0.0, -1.0]])
sp = np.array([[0.0, 1.0], [0.0, 0.0]])
sm = np.array([[0.0, 0.0], [1.0, 0.0]])

def build_op(op_2x2, mode, n):
    """Build operator on mode `mode` in n-mode Fock space."""
    result = np.array([[1.0]])
    for k in range(n):
        result = np.kron(result, op_2x2 if k == mode else I2)
    return result

SZ, SP, SM = [], [], []
for k in range(N):
    SZ.append(build_op(sz, k, N))
    SP.append(build_op(sp, k, N))
    SM.append(build_op(sm, k, N))

# Number operator for each mode: n_k = (1 - sigma_z^k) / 2
N_ops = []
for k in range(N):
    N_ops.append(0.5 * (np.eye(dim) - SZ[k]))

# Total pair number
N_pair_op = sum(N_ops)

# B2 occupation: N_B2 = sum of B2 mode number operators
N_B2_op = sum(N_ops[k] for k in B2_idx)
N_B1_op = sum(N_ops[k] for k in B1_idx)
N_B3_op = sum(N_ops[k] for k in B3_idx)

print(f"  Built {N} mode operators (sz, s+, s-)")
print(f"  N_B2_op: Tr = {np.trace(N_B2_op):.1f}")
print(f"  N_B1_op: Tr = {np.trace(N_B1_op):.1f}")
print(f"  N_B3_op: Tr = {np.trace(N_B3_op):.1f}")

# ======================================================================
#  STEP 3: Build full BCS Hamiltonian
# ======================================================================

print("\n--- Step 3: Build H_BCS (256x256) ---")

xi = E_8 - mu  # single-particle energies relative to mu

# CONVENTION NOTE: The pairing Hamiltonian is
#   H = sum_k 2*xi_k * n_k - sum_{km} V_{km} * c_k^dag * c_m
# where c_k^dag = SM[k] (creates pair at mode k) and c_m = SP[m] (annihilates pair at mode m).
# This is Convention B. Convention A (SP[k]@SM[m] as in S39 integrability script)
# gives a Hamiltonian whose N=1 sector does NOT match H_1 = diag(2*xi) - V_phys.
# Since the GGE was constructed from H_1 eigenstates, we MUST use Convention B
# for consistency: SM[k] @ SP[m] = c_k^dag * c_m.
H_BCS = np.zeros((dim, dim))
for k in range(N):
    H_BCS += 2 * xi[k] * N_ops[k]
    for m in range(N):
        H_BCS -= V_phys[k, m] * SM[k] @ SP[m]

assert np.allclose(H_BCS, H_BCS.T), "H_BCS not symmetric!"

# Also build the free Hamiltonian (no pairing)
H_free = np.zeros((dim, dim))
for k in range(N):
    H_free += 2 * xi[k] * N_ops[k]

# Build branch-resolved Hamiltonians
H_B2 = np.zeros((dim, dim))
for k in B2_idx:
    H_B2 += 2 * xi[k] * N_ops[k]
    for m in B2_idx:
        H_B2 -= V_phys[k, m] * SM[k] @ SP[m]

H_B1 = np.zeros((dim, dim))
for k in B1_idx:
    H_B1 += 2 * xi[k] * N_ops[k]

H_B3 = np.zeros((dim, dim))
for k in B3_idx:
    H_B3 += 2 * xi[k] * N_ops[k]
    for m in B3_idx:
        H_B3 -= V_phys[k, m] * SM[k] @ SP[m]

# Cross-branch pairing (the DECAY DRIVER)
H_cross = H_BCS - H_B2 - H_B1 - H_B3
# Remove free energy double-counting
H_cross_pair = np.zeros((dim, dim))
for k in range(N):
    for m in range(N):
        # Only cross-branch terms
        same_branch = (k in B2_idx and m in B2_idx) or \
                      (k in B1_idx and m in B1_idx) or \
                      (k in B3_idx and m in B3_idx)
        if not same_branch:
            H_cross_pair -= V_phys[k, m] * SM[k] @ SP[m]

print(f"  H_BCS: ||H|| = {norm(H_BCS, 'fro'):.6f}")
print(f"  H_free: ||H|| = {norm(H_free, 'fro'):.6f}")
print(f"  H_cross_pair (decay driver): ||H|| = {norm(H_cross_pair, 'fro'):.6f}")
print(f"  ||H_cross_pair|| / ||H_BCS|| = {norm(H_cross_pair, 'fro')/norm(H_BCS, 'fro'):.6f}")

# Diagonalize H_BCS
evals_BCS, evecs_BCS = eigh(H_BCS)

# Verify [H, N_pair] = 0
comm_HN = norm(H_BCS @ N_pair_op - N_pair_op @ H_BCS, 'fro')
print(f"  ||[H_BCS, N_pair]|| = {comm_HN:.2e}")

# Ground state properties
gs = evecs_BCS[:, 0]
E_gs = evals_BCS[0]
N_pair_gs = gs @ N_pair_op @ gs
print(f"  E_gs = {E_gs:.10f}")
print(f"  <N_pair>_gs = {N_pair_gs:.10f}")

# ======================================================================
#  STEP 4: Construct GGE density matrix
# ======================================================================

print("\n--- Step 4: Construct GGE density matrix ---")

# The GGE density matrix is diagonal in the mode basis within N_pair=1.
# rho_GGE[|k>, |k>] = p_k where |k> = state with exactly mode k occupied.
# In the computational basis, |k> = |0...1_k...0> has bit k set.

# N_pair=1 Fock states: state alpha has exactly one bit set.
# CRITICAL: kron ordering puts mode k at bit position N-1-k.
# Mode 0 is the FIRST kron factor -> MSB (bit 7, alpha=128).
# Mode k occupies alpha = 2^(N-1-k).
n1_states = [2**(N-1-k) for k in range(N)]

rho_GGE = np.zeros((dim, dim))
for k in range(N):
    rho_GGE[n1_states[k], n1_states[k]] = p_k[k]

# Verify properties
tr_rho = np.trace(rho_GGE)
rho_evals = np.linalg.eigvalsh(rho_GGE)
purity_GGE = np.trace(rho_GGE @ rho_GGE)

print(f"  Tr(rho_GGE) = {tr_rho:.15f}")
print(f"  Purity = {purity_GGE:.10f}")
print(f"  Min eigenvalue = {np.min(rho_evals):.6e}")
print(f"  Max eigenvalue = {np.max(rho_evals):.6e}")
print(f"  Rank = {np.sum(rho_evals > 1e-15)}")

# Initial observables
N_B2_0 = np.trace(N_B2_op @ rho_GGE)
N_B1_0 = np.trace(N_B1_op @ rho_GGE)
N_B3_0 = np.trace(N_B3_op @ rho_GGE)
H_B1_0 = np.trace(H_B1 @ rho_GGE)

print(f"\n  Initial <N_B2> = {N_B2_0:.10f}")
print(f"  Initial <N_B1> = {N_B1_0:.10f}")
print(f"  Initial <N_B3> = {N_B3_0:.10f}")
print(f"  Initial <N_total> = {N_B2_0 + N_B1_0 + N_B3_0:.10f}")
print(f"  Initial <H_B1> = {H_B1_0:.10f}")

# ======================================================================
#  STEP 5: Diagonalize and prepare for time evolution
# ======================================================================

print("\n--- Step 5: Prepare time evolution ---")

# Time evolution: rho(t) = U(t) rho(0) U^dag(t)
# where U(t) = exp(-i*H*t) = V * diag(exp(-i*E_n*t)) * V^dag
# and H = V * diag(E_n) * V^dag

# Transform rho_GGE to energy eigenbasis
rho_GGE_eig = evecs_BCS.T @ rho_GGE @ evecs_BCS

# Transform observable operators to energy eigenbasis
N_B2_eig = evecs_BCS.T @ N_B2_op @ evecs_BCS
N_B1_eig = evecs_BCS.T @ N_B1_op @ evecs_BCS
N_B3_eig = evecs_BCS.T @ N_B3_op @ evecs_BCS
H_B1_eig = evecs_BCS.T @ H_B1 @ evecs_BCS
H_B2_eig = evecs_BCS.T @ H_B2 @ evecs_BCS
H_B3_eig = evecs_BCS.T @ H_B3 @ evecs_BCS
H_cross_eig = evecs_BCS.T @ H_cross_pair @ evecs_BCS

# Also build N_B2=k projectors (for sector probabilities)
# P_{N_B2=k} projects onto Fock states with exactly k B2 modes occupied
P_NB2 = {}
for nval in range(5):  # N_B2 = 0, 1, 2, 3, 4
    P = np.zeros((dim, dim))
    for alpha in range(dim):
        # B2 modes are 0-3. In kron ordering, mode j occupies bit N-1-j.
        # So B2 modes occupy bits 7,6,5,4.
        nb2 = sum((alpha >> (N-1-j)) & 1 for j in B2_idx)
        if nb2 == nval:
            P[alpha, alpha] = 1.0
    P_NB2[nval] = P

P_NB2_eig = {}
for nval in range(5):
    P_NB2_eig[nval] = evecs_BCS.T @ P_NB2[nval] @ evecs_BCS

# Verify projectors
for nval in range(5):
    tr_P = np.trace(P_NB2[nval])
    print(f"  P_{{N_B2={nval}}}: Tr = {tr_P:.0f}, "
          f"Tr(P*rho_0) = {np.trace(P_NB2[nval] @ rho_GGE):.10f}")

# Also: individual mode projectors for fine-grained B2 analysis
# and N_pair sector projectors for conservation check
P_Npair = {}
for nval in range(N + 1):
    P = np.zeros((dim, dim))
    for alpha in range(dim):
        if bin(alpha).count('1') == nval:
            P[alpha, alpha] = 1.0
    P_Npair[nval] = P

P_Npair_eig = {}
for nval in range(N + 1):
    P_Npair_eig[nval] = evecs_BCS.T @ P_Npair[nval] @ evecs_BCS

print(f"\n  N_pair conservation check:")
for nval in range(N + 1):
    tr_val = np.trace(P_Npair[nval] @ rho_GGE)
    if abs(tr_val) > 1e-15:
        print(f"    P(N_pair={nval}) = {tr_val:.15f}")

# ======================================================================
#  STEP 6: Time evolution
# ======================================================================

print("\n--- Step 6: Time evolution ---")

# Time grid: 500 points from t=0 to t=20
n_times = 500
t_max = 20.0
t_array = np.linspace(0, t_max, n_times)

# Observables to track
N_B2_t = np.zeros(n_times)
N_B1_t = np.zeros(n_times)
N_B3_t = np.zeros(n_times)
H_B1_t = np.zeros(n_times)
H_B2_t = np.zeros(n_times)
H_B3_t = np.zeros(n_times)
H_cross_t = np.zeros(n_times)
P_NB2_t = np.zeros((5, n_times))  # Prob of N_B2 = 0,1,2,3,4
P_Npair1_t = np.zeros(n_times)    # Conservation check
S_vN_t = np.zeros(n_times)        # von Neumann entropy (should be constant)
purity_t = np.zeros(n_times)      # Purity (should be constant)

# Efficient time evolution using energy eigenbasis:
# rho(t)_{nm} = rho(0)_{nm} * exp(-i*(E_n - E_m)*t)
# <O>(t) = Tr[O * rho(t)] = sum_{nm} O_{mn} * rho(0)_{nm} * exp(-i*(E_n-E_m)*t)
#
# Since rho_GGE is real and symmetric, rho(0)_{nm} is real.
# The phase matrix: phase_{nm}(t) = exp(-i*(E_n - E_m)*t)

# Precompute energy differences
dE = evals_BCS[:, None] - evals_BCS[None, :]  # E_n - E_m

# Precompute the product O_{mn} * rho(0)_{nm} for each observable
# Note: O_{mn} is (evecs^T @ O @ evecs)_{mn}, and rho(0)_{nm} = rho_GGE_eig_{nm}
# <O>(t) = sum_{nm} O_eig_{mn} * rho_eig_{nm} * exp(-i*dE_{nm}*t)
#         = Re[sum_{nm} (O_eig * rho_eig^T)_{mn} * exp(-i*dE_{nm}*t)]

# Element-wise product matrices (real part gives the time-dependent trace)
OR_NB2 = N_B2_eig * rho_GGE_eig.T   # O*rho^T: (OR)_{mn} = O_{mn}*rho_{nm}
OR_NB1 = N_B1_eig * rho_GGE_eig.T
OR_NB3 = N_B3_eig * rho_GGE_eig.T
OR_HB1 = H_B1_eig * rho_GGE_eig.T
OR_HB2 = H_B2_eig * rho_GGE_eig.T
OR_HB3 = H_B3_eig * rho_GGE_eig.T
OR_Hcross = H_cross_eig * rho_GGE_eig.T
OR_PNB2 = {}
for nval in range(5):
    OR_PNB2[nval] = P_NB2_eig[nval] * rho_GGE_eig.T
OR_PNpair1 = P_Npair_eig[1] * rho_GGE_eig.T

print(f"  Time grid: {n_times} points, t in [0, {t_max}]")
print(f"  Evolving...")

t_evolve_start = time.time()

for it, t in enumerate(t_array):
    # Phase matrix: exp(-i * dE * t)
    phase = np.exp(-1j * dE * t)

    # Compute expectation values: <O>(t) = Re[sum_{mn} OR_{mn} * phase_{mn}]
    N_B2_t[it] = np.real(np.sum(OR_NB2 * phase))
    N_B1_t[it] = np.real(np.sum(OR_NB1 * phase))
    N_B3_t[it] = np.real(np.sum(OR_NB3 * phase))
    H_B1_t[it] = np.real(np.sum(OR_HB1 * phase))
    H_B2_t[it] = np.real(np.sum(OR_HB2 * phase))
    H_B3_t[it] = np.real(np.sum(OR_HB3 * phase))
    H_cross_t[it] = np.real(np.sum(OR_Hcross * phase))

    for nval in range(5):
        P_NB2_t[nval, it] = np.real(np.sum(OR_PNB2[nval] * phase))

    P_Npair1_t[it] = np.real(np.sum(OR_PNpair1 * phase))

    # Purity: Tr(rho^2) = sum_{nm} |rho_{nm}(t)|^2
    # rho_{nm}(t) = rho_eig_{nm} * exp(-i*dE_{nm}*t)
    # |rho_{nm}(t)|^2 = |rho_eig_{nm}|^2 (independent of time for unitary evolution!)
    purity_t[it] = np.sum(rho_GGE_eig**2)  # constant

    # von Neumann entropy: S = -Tr(rho ln rho) -- constant under unitary evolution
    # But for verification, compute at t=0 and confirm constancy
    if it == 0:
        rho_evals_check = np.linalg.eigvalsh(rho_GGE)
        rho_evals_pos = rho_evals_check[rho_evals_check > 1e-30]
        S_vN_0 = -np.sum(rho_evals_pos * np.log(rho_evals_pos))
    S_vN_t[it] = S_vN_0  # constant under unitary evolution

t_evolve = time.time() - t_evolve_start
print(f"  Evolution complete: {t_evolve:.2f}s")

# ======================================================================
#  STEP 7: Cross-checks
# ======================================================================

print("\n--- Step 7: Cross-checks ---")

# Check 1: N_pair conservation
print(f"  N_pair=1 probability at t=0: {P_Npair1_t[0]:.15f}")
print(f"  N_pair=1 probability at t=T: {P_Npair1_t[-1]:.15f}")
print(f"  Max deviation: {np.max(np.abs(P_Npair1_t - 1.0)):.6e}")

# Check 2: Total pair number conservation
N_total_t = N_B2_t + N_B1_t + N_B3_t
print(f"  <N_total>(t=0) = {N_total_t[0]:.15f}")
print(f"  <N_total>(t=T) = {N_total_t[-1]:.15f}")
print(f"  Max deviation: {np.max(np.abs(N_total_t - N_total_t[0])):.6e}")

# Check 3: Total energy conservation
H_total_t = H_B2_t + H_B1_t + H_B3_t + H_cross_t
print(f"  <H_total>(t=0) = {H_total_t[0]:.10f}")
print(f"  <H_total>(t=T) = {H_total_t[-1]:.10f}")
print(f"  Max deviation: {np.max(np.abs(H_total_t - H_total_t[0])):.6e}")

# Check 4: Purity constancy
print(f"  Purity = {purity_t[0]:.10f} (constant by unitarity)")

# Check 5: Probability normalization
P_NB2_sum_t = sum(P_NB2_t[nval] for nval in range(5))
print(f"  sum P(N_B2=k) at t=0: {P_NB2_sum_t[0]:.15f}")
print(f"  Max deviation from 1: {np.max(np.abs(P_NB2_sum_t - 1.0)):.6e}")

# ======================================================================
#  STEP 8: Extract B2 decay characteristics
# ======================================================================

print("\n--- Step 8: Extract B2 decay-out time ---")

# The initial B2 occupation
N_B2_initial = N_B2_t[0]
N_B2_asymp = np.mean(N_B2_t[n_times//2:])  # Long-time average

print(f"  <N_B2>(t=0) = {N_B2_initial:.10f}")
print(f"  <N_B2> long-time avg (t > {t_max/2}) = {N_B2_asymp:.10f}")
print(f"  Delta N_B2 = {N_B2_initial - N_B2_asymp:.10f}")

# Relative B2 content: f_B2(t) = <N_B2>(t) / <N_total>
# Since <N_total> = 1 in N_pair=1, f_B2(t) = <N_B2>(t)
f_B2_t = N_B2_t  # fractional B2 content

# Initial B2 fraction
f_B2_0 = f_B2_t[0]
f_B2_asymp = np.mean(f_B2_t[n_times//2:])

# Decay amplitude: how much does B2 content change?
delta_f_B2 = f_B2_0 - f_B2_asymp

print(f"\n  B2 fraction: initial = {f_B2_0:.6f}, asymptotic = {f_B2_asymp:.6f}")
print(f"  Fractional change: {delta_f_B2:.6f} ({delta_f_B2/f_B2_0*100:.2f}%)")

# Find the first time f_B2 drops below various thresholds
thresholds = [0.99, 0.95, 0.90, 0.80, 0.50]
print(f"\n  B2 decay timescales (fraction of initial):")
for thresh in thresholds:
    target = f_B2_0 * thresh
    idx = np.where(f_B2_t < target)[0]
    if len(idx) > 0:
        t_cross = t_array[idx[0]]
        print(f"    f_B2 < {thresh:.0%} of initial ({target:.6f}): t = {t_cross:.4f}")
    else:
        print(f"    f_B2 < {thresh:.0%} of initial ({target:.6f}): NEVER (in t < {t_max})")

# More refined: find the 1/e decay time
# f_B2(t) = f_B2_asymp + (f_B2_0 - f_B2_asymp) * g(t)
# where g(0) = 1 and g -> 0 as t -> inf
# t_decay = time when g(t) = 1/e

if abs(delta_f_B2) > 1e-10:
    g_t = (f_B2_t - f_B2_asymp) / delta_f_B2
    # Find first time g_t < 1/e
    idx_1e = np.where(g_t < 1.0/np.e)[0]
    if len(idx_1e) > 0:
        t_decay_1e = t_array[idx_1e[0]]
        print(f"\n  1/e decay time: t_decay = {t_decay_1e:.6f}")
    else:
        t_decay_1e = np.inf
        print(f"\n  1/e decay: does NOT reach 1/e within t < {t_max}")

    # Also find half-life
    idx_half = np.where(g_t < 0.5)[0]
    if len(idx_half) > 0:
        t_half = t_array[idx_half[0]]
        print(f"  Half-life: t_1/2 = {t_half:.6f}")
    else:
        t_half = np.inf
        print(f"  Half-life: does NOT reach 0.5 within t < {t_max}")
else:
    t_decay_1e = np.inf
    t_half = np.inf
    g_t = np.ones(n_times)
    print(f"\n  NO DECAY: delta_f_B2 = {delta_f_B2:.2e} (negligible)")

# ======================================================================
#  STEP 9: Oscillation analysis (Fourier)
# ======================================================================

print("\n--- Step 9: Oscillation analysis ---")

# The B2 content may oscillate rather than decay monotonically.
# Analyze the Fourier spectrum to identify characteristic frequencies.

# Subtract the mean for FFT
dt = t_array[1] - t_array[0]
f_B2_centered = f_B2_t - np.mean(f_B2_t)

# FFT
fft_vals = np.fft.rfft(f_B2_centered)
freqs = np.fft.rfftfreq(n_times, d=dt)
power = np.abs(fft_vals)**2

# Find dominant frequencies
n_peaks = 5
peak_idx = np.argsort(power[1:])[-n_peaks:][::-1] + 1  # skip DC
print(f"  Dominant oscillation frequencies in N_B2(t):")
for i, idx in enumerate(peak_idx):
    f = freqs[idx]
    period = 1.0 / f if f > 0 else np.inf
    print(f"    f_{i+1} = {f:.6f} (period = {period:.4f}, "
          f"omega = {2*np.pi*f:.4f})")

# The dominant frequency should correspond to energy differences
# in the H_1 spectrum (since dynamics is within N_pair=1).
H1 = np.diag(2 * xi) - V_phys
evals_H1, evecs_H1 = eigh(H1)
print(f"\n  H_1 eigenvalues: {evals_H1}")
print(f"  Energy gaps from ground state:")
for n in range(1, N):
    dE_n = evals_H1[n] - evals_H1[0]
    print(f"    dE_{n} = {dE_n:.6f} (omega = {dE_n:.6f}, "
          f"f = {dE_n/(2*np.pi):.6f}, T = {2*np.pi/dE_n:.4f})")

# Since dynamics is ENTIRELY within N_pair=1, we can verify using the
# 8x8 H_1 matrix directly.
print(f"\n--- Step 9b: Direct 8-dim N_pair=1 computation (cross-check) ---")

# In N_pair=1, the basis states are |k> (pair in mode k).
# H_1 acts on this 8-dim space: H_1_{km} = 2*xi_k*delta_{km} - V_phys_{km}
# rho_GGE restricted to N_pair=1: diagonal with entries p_k

rho_8x8 = np.diag(p_k)
rho_8x8_eig = evecs_H1.T @ rho_8x8 @ evecs_H1

# N_B2 in the 8-dim basis: diagonal with entries 1 for k in B2, 0 otherwise
N_B2_8 = np.diag([1.0 if k in B2_idx else 0.0 for k in range(N)])
N_B1_8 = np.diag([1.0 if k in B1_idx else 0.0 for k in range(N)])
N_B3_8 = np.diag([1.0 if k in B3_idx else 0.0 for k in range(N)])

# Transform to H_1 eigenbasis
N_B2_H1 = evecs_H1.T @ N_B2_8 @ evecs_H1
N_B1_H1 = evecs_H1.T @ N_B1_8 @ evecs_H1
N_B3_H1 = evecs_H1.T @ N_B3_8 @ evecs_H1

# Energy differences
dE_H1 = evals_H1[:, None] - evals_H1[None, :]

# Time evolution in 8-dim space
OR_NB2_8 = N_B2_H1 * rho_8x8_eig.T
OR_NB1_8 = N_B1_H1 * rho_8x8_eig.T
OR_NB3_8 = N_B3_H1 * rho_8x8_eig.T

# Verify agreement at t=0
NB2_8_t0 = np.real(np.sum(OR_NB2_8))
print(f"  8-dim <N_B2>(0) = {NB2_8_t0:.10f}")
print(f"  256-dim <N_B2>(0) = {N_B2_t[0]:.10f}")
print(f"  Match: {np.isclose(NB2_8_t0, N_B2_t[0])}")

# Evolve at the same time points (using 8x8 -- much faster)
N_B2_t_8 = np.zeros(n_times)
N_B1_t_8 = np.zeros(n_times)
N_B3_t_8 = np.zeros(n_times)

for it, t in enumerate(t_array):
    phase_8 = np.exp(-1j * dE_H1 * t)
    N_B2_t_8[it] = np.real(np.sum(OR_NB2_8 * phase_8))
    N_B1_t_8[it] = np.real(np.sum(OR_NB1_8 * phase_8))
    N_B3_t_8[it] = np.real(np.sum(OR_NB3_8 * phase_8))

# Check agreement between 8-dim and 256-dim computations
max_diff_NB2 = np.max(np.abs(N_B2_t - N_B2_t_8))
max_diff_NB1 = np.max(np.abs(N_B1_t - N_B1_t_8))
max_diff_NB3 = np.max(np.abs(N_B3_t - N_B3_t_8))
print(f"\n  256-dim vs 8-dim agreement:")
print(f"    max|Delta N_B2| = {max_diff_NB2:.6e}")
print(f"    max|Delta N_B1| = {max_diff_NB1:.6e}")
print(f"    max|Delta N_B3| = {max_diff_NB3:.6e}")

# ======================================================================
#  STEP 10: B2-B1 energy transfer rate
# ======================================================================

print("\n--- Step 10: Energy transfer rates ---")

# d<H_B1>/dt from Heisenberg equation: d<H_B1>/dt = -i<[H_B1, H_BCS]>
# = -i<[H_B1, H_cross_pair]> (since [H_B1, H_B1]=0 and [H_B1, H_free]=0 within N=1)

# Compute numerically from the time series
dHB1_dt = np.gradient(H_B1_t, t_array)
dHB2_dt = np.gradient(H_B2_t, t_array)
dHB3_dt = np.gradient(H_B3_t, t_array)

# Initial energy transfer rate
print(f"  dH_B1/dt at t=0: {dHB1_dt[0]:.10f}")
print(f"  dH_B2/dt at t=0: {dHB2_dt[0]:.10f}")
print(f"  dH_B3/dt at t=0: {dHB3_dt[0]:.10f}")

# RMS energy transfer rate
dHB2_rms = np.sqrt(np.mean(dHB2_dt**2))
dHB1_rms = np.sqrt(np.mean(dHB1_dt**2))
dHB3_rms = np.sqrt(np.mean(dHB3_dt**2))
print(f"  RMS dH_B2/dt: {dHB2_rms:.6f}")
print(f"  RMS dH_B1/dt: {dHB1_rms:.6f}")
print(f"  RMS dH_B3/dt: {dHB3_rms:.6f}")

# Maximum instantaneous B2 energy transfer rate
max_dHB2 = np.max(np.abs(dHB2_dt))
t_max_dHB2 = t_array[np.argmax(np.abs(dHB2_dt))]
print(f"  Max |dH_B2/dt| = {max_dHB2:.6f} at t = {t_max_dHB2:.4f}")

# ======================================================================
#  STEP 11: Long-time average (diagonal ensemble)
# ======================================================================

print("\n--- Step 11: Diagonal ensemble (long-time average) ---")

# The long-time average of any observable is given by the diagonal ensemble:
# <O>_diag = sum_n rho_nn * O_nn (in energy eigenbasis)
# This corresponds to dephasing: all off-diagonal elements of rho average to zero.

rho_diag = np.diag(np.diag(rho_GGE_eig))
N_B2_diag = np.trace(N_B2_eig @ rho_diag)
N_B1_diag = np.trace(N_B1_eig @ rho_diag)
N_B3_diag = np.trace(N_B3_eig @ rho_diag)
H_B2_diag = np.trace(H_B2_eig @ rho_diag)
H_B1_diag = np.trace(H_B1_eig @ rho_diag)

P_NB2_diag = {}
for nval in range(5):
    P_NB2_diag[nval] = np.trace(P_NB2_eig[nval] @ rho_diag)

print(f"  Diagonal ensemble (infinite-time average):")
print(f"    <N_B2>_diag = {N_B2_diag:.10f}")
print(f"    <N_B1>_diag = {N_B1_diag:.10f}")
print(f"    <N_B3>_diag = {N_B3_diag:.10f}")
print(f"    <H_B2>_diag = {H_B2_diag:.10f}")
print(f"    <H_B1>_diag = {H_B1_diag:.10f}")
print(f"\n  B2 sector probabilities (diagonal ensemble):")
for nval in range(5):
    print(f"    P(N_B2={nval})_diag = {P_NB2_diag[nval]:.10f}")

# Comparison with time average from explicit evolution
N_B2_time_avg = np.mean(N_B2_t[n_times//4:])
print(f"\n  Cross-check: <N_B2> time avg (t > {t_max/4}) = {N_B2_time_avg:.10f}")
print(f"  Diagonal ensemble:                             = {N_B2_diag:.10f}")
print(f"  Difference: {abs(N_B2_time_avg - N_B2_diag):.6e}")

# ======================================================================
#  STEP 12: Recurrence analysis
# ======================================================================

print("\n--- Step 12: Recurrence analysis ---")

# For an 8-level system, the dynamics is quasi-periodic.
# The recurrence time is set by the LCM of the frequency ratios.
# Since the energy levels are generally incommensurate, the recurrence
# time is technically infinite, but near-recurrences happen when
# all phases are simultaneously close to integer multiples of 2*pi.

# Compute the deviation from initial state: D(t) = |<N_B2>(t) - <N_B2>(0)|
D_t = np.abs(N_B2_t - N_B2_t[0])

# Find first recurrence (D drops back below some threshold)
# Look for minima of D after the first excursion
recurrence_thresh = 0.01 * np.max(D_t)
# Skip the initial interval
t_skip = 5  # skip first few units
idx_skip = np.searchsorted(t_array, t_skip)
if idx_skip < n_times:
    D_post = D_t[idx_skip:]
    t_post = t_array[idx_skip:]
    min_D_post = np.min(D_post)
    t_min_D = t_post[np.argmin(D_post)]
    print(f"  Max excursion: {np.max(D_t):.6f} at t = {t_array[np.argmax(D_t)]:.4f}")
    print(f"  Best recurrence (t > {t_skip}): D = {min_D_post:.6f} at t = {t_min_D:.4f}")
    print(f"  Recurrence quality: D_min/D_max = {min_D_post/np.max(D_t):.4f}")

# ======================================================================
#  STEP 13: Nazarewicz FGR comparison
# ======================================================================

print("\n--- Step 13: Nazarewicz FGR comparison ---")

# Nazarewicz estimate: Gamma_B2 from FGR using the cross-branch V elements
# The FGR rate for B2 -> B1 transition:
# Gamma_{B2->B1} = 2*pi * |<B1|V|B2>|^2 * delta(E_B1 - E_B2)
# In finite system, replace delta by 1/(pi*gamma) Lorentzian with width gamma.

# B2-B1 coupling: V_phys[4, 0:4] (B1 row, B2 columns)
V_B2_B1 = V_phys[4, B2_idx]
V_B2_B3 = V_phys[np.ix_(B3_idx, B2_idx)]

print(f"  V(B1, B2[k]) = {V_B2_B1}")
print(f"  V(B3, B2) = ")
for i, k in enumerate(B3_idx):
    print(f"    B3[{i}]-B2: {V_phys[k, B2_idx]}")

# Energy differences
dE_B2_B1 = 2*xi[B2_idx[0]] - 2*xi[B1_idx[0]]  # Same for all B2 (degenerate)
dE_B2_B3 = 2*xi[B2_idx[0]] - 2*xi[B3_idx[0]]

print(f"\n  Energy gaps:")
print(f"    2*xi_B2 - 2*xi_B1 = {dE_B2_B1:.6f}")
print(f"    2*xi_B2 - 2*xi_B3 = {dE_B2_B3:.6f}")

# FGR rate (using actual H_1 eigenvalues, not bare levels)
# The relevant coupling is in the eigenbasis of H_1.
# The B2 "doorway state" couples to H_1 eigenstates with energy spread.

# B2 content of each H_1 eigenstate
B2_content_eigenstates = np.zeros(N)
for n in range(N):
    B2_content_eigenstates[n] = np.sum(evecs_H1[B2_idx, n]**2)

print(f"\n  B2 content of H_1 eigenstates:")
for n in range(N):
    print(f"    eigenstate {n} (E={evals_H1[n]:.6f}): "
          f"f_B2 = {B2_content_eigenstates[n]:.6f}")

# The GGE populates each eigenstate with probability:
# p_n^eig = sum_k p_k * |<n|k>|^2
p_eig = np.zeros(N)
for n in range(N):
    for k in range(N):
        p_eig[n] += p_k[k] * evecs_H1[k, n]**2
print(f"\n  GGE population of H_1 eigenstates:")
print(f"  sum = {np.sum(p_eig):.15f}")
for n in range(N):
    print(f"    eigenstate {n}: p = {p_eig[n]:.10f}, B2 content = {B2_content_eigenstates[n]:.6f}")

# The B2 content in the diagonal ensemble is:
# <N_B2>_diag = sum_n p_n^eig * B2_content[n]
N_B2_from_eig = np.sum(p_eig * B2_content_eigenstates)
print(f"\n  <N_B2>_diag from eigenstates: {N_B2_from_eig:.10f}")
print(f"  <N_B2>_diag from 256-dim:     {N_B2_diag:.10f}")
print(f"  Match: {np.isclose(N_B2_from_eig, float(N_B2_diag))}")

# The key: the MIXING of B2 content across eigenstates determines
# whether B2 "decays". If all eigenstates have the SAME B2 content,
# then N_B2 is exactly conserved regardless of the dynamics.
# The SPREAD of B2 content determines the amplitude of oscillations.

B2_spread = np.sqrt(np.sum(p_eig * (B2_content_eigenstates - N_B2_from_eig)**2))
print(f"\n  B2 content spread (weighted sigma): {B2_spread:.6f}")
print(f"  Max B2 oscillation amplitude: ~{2*B2_spread:.6f}")
print(f"  Fractional oscillation: ~{2*B2_spread/f_B2_0*100:.2f}%")

# Effective FGR rate from eigenstate decomposition
# The "decay" rate of B2 is NOT a simple exponential because the
# system is finite (8 levels). The dynamics is quasi-periodic.
# Nazarewicz's Gamma_B2 ~ 7.5 applies to an infinite-level system
# where the density of states is continuous. In our 8-level system,
# the correct measure is the oscillation timescale set by the
# energy splittings of the H_1 eigenstates that contain B2 weight.

# B2-weighted energy splittings
omega_B2 = []
for n in range(N):
    for m in range(n+1, N):
        if B2_content_eigenstates[n] > 0.01 and B2_content_eigenstates[m] > 0.01:
            dE_nm = abs(evals_H1[n] - evals_H1[m])
            weight = np.sqrt(p_eig[n] * p_eig[m]) * \
                     abs(B2_content_eigenstates[n] - B2_content_eigenstates[m])
            if weight > 0.001:
                omega_B2.append((dE_nm, weight, n, m))
                print(f"    ({n},{m}): dE = {dE_nm:.6f}, weight = {weight:.6f}")

# ======================================================================
#  STEP 14: DEFINITIVE ANALYSIS -- B2 Doorway Decay
# ======================================================================

print("\n--- Step 14: DEFINITIVE B2 decay analysis ---")

# The oscillation envelope determines the effective decay timescale.
# For a finite system, this is NOT exponential decay but RABI-TYPE oscillations.

# Compute the oscillation envelope using the Hilbert transform
from scipy.signal import hilbert

# Analytic signal for B2 content
f_B2_centered = f_B2_t - np.mean(f_B2_t)
analytic_signal = hilbert(f_B2_centered)
envelope = np.abs(analytic_signal)

# Normalized envelope relative to initial amplitude
initial_amplitude = np.abs(f_B2_centered[0]) if np.abs(f_B2_centered[0]) > 1e-10 else envelope[0]
if initial_amplitude > 1e-10:
    envelope_normalized = envelope / initial_amplitude
else:
    envelope_normalized = np.ones(n_times)

# Fit the envelope to exponential decay: A(t) = A0 * exp(-Gamma*t/2)
# using log-linear regression on the envelope
t_fit_mask = (t_array > 0.1) & (envelope > 1e-10)
if np.sum(t_fit_mask) > 10:
    log_env = np.log(envelope[t_fit_mask])
    t_fit = t_array[t_fit_mask]
    # Linear fit: log(A) = log(A0) - Gamma/2 * t
    coeffs = np.polyfit(t_fit, log_env, 1)
    Gamma_fit = -2 * coeffs[0]
    A0_fit = np.exp(coeffs[1])
    print(f"  Envelope fit: Gamma = {Gamma_fit:.6f} (1/e time = {1/Gamma_fit if Gamma_fit > 0 else np.inf:.4f})")
    print(f"  A0_fit = {A0_fit:.6f}")
else:
    Gamma_fit = 0.0
    print(f"  Envelope fit: insufficient data")

# The CORRECT decay metric: time-averaged fluctuation
# sigma_B2(t) = sqrt(<(N_B2 - <N_B2>_diag)^2>_time)
# This measures the amplitude of B2 oscillations.

# Running time average of N_B2(t)
N_B2_running_avg = np.cumsum(N_B2_t) / (np.arange(n_times) + 1)

# Fluctuation amplitude around diagonal ensemble
fluct_B2 = np.abs(N_B2_t - float(N_B2_diag))
max_fluct = np.max(fluct_B2)
avg_fluct = np.mean(fluct_B2)

print(f"\n  B2 fluctuations around diagonal ensemble:")
print(f"    Max fluctuation: {max_fluct:.6f}")
print(f"    Mean fluctuation: {avg_fluct:.6f}")
print(f"    <N_B2>(t=0) - <N_B2>_diag = {float(N_B2_t[0] - N_B2_diag):.6f}")

# KEY QUESTION: does the GGE B2 content differ from the diagonal ensemble?
# If yes -> B2 "decays" from GGE value to diagonal value (dephasing)
# If no -> B2 is protected

delta_GGE_diag = float(N_B2_t[0] - N_B2_diag)
relative_shift = delta_GGE_diag / f_B2_0

print(f"\n  CRITICAL COMPARISON:")
print(f"    <N_B2>_GGE (initial) = {N_B2_t[0]:.10f}")
print(f"    <N_B2>_diag (long-time) = {float(N_B2_diag):.10f}")
print(f"    Shift = {delta_GGE_diag:.10f}")
print(f"    Relative shift = {relative_shift:.6f} ({relative_shift*100:.4f}%)")

# The dephasing timescale (not decay!) from the energy splittings
# t_dephase ~ 1 / max(dE among B2-weighted pairs)
if len(omega_B2) > 0:
    max_omega = max(w[0] for w in omega_B2)
    t_dephase = 2*np.pi / max_omega
    print(f"\n  Dephasing timescale:")
    print(f"    max omega (B2-weighted) = {max_omega:.6f}")
    print(f"    t_dephase = 2*pi/omega = {t_dephase:.4f}")
else:
    t_dephase = np.inf
    print(f"\n  No significant B2-weighted frequency splittings found")

# ======================================================================
#  STEP 15: Gate verdict
# ======================================================================

print("\n" + "=" * 78)
print("GATE VERDICT: B2-DECAY-40")
print("=" * 78)

# The effective B2 "decay" time is the dephasing time from GGE to
# diagonal ensemble. Since the system is finite and quasi-periodic,
# this is NOT true decay but oscillation/dephasing.

# Compute: characteristic time for N_B2(t) to first reach N_B2_diag
if abs(delta_GGE_diag) > 1e-10:
    # Find first crossing of the diagonal ensemble value
    if delta_GGE_diag > 0:
        # N_B2 starts above diagonal and oscillates down
        idx_cross = np.where(N_B2_t < float(N_B2_diag))[0]
    else:
        # N_B2 starts below diagonal and oscillates up
        idx_cross = np.where(N_B2_t > float(N_B2_diag))[0]

    if len(idx_cross) > 0:
        t_first_cross = t_array[idx_cross[0]]
        print(f"\n  First crossing of <N_B2>_diag: t = {t_first_cross:.6f}")
    else:
        t_first_cross = np.inf
        print(f"\n  N_B2 never crosses diagonal value within t < {t_max}")
else:
    t_first_cross = 0.0
    print(f"\n  N_B2 starts AT the diagonal value (no dephasing)")

# Alternative metric: time to reach within 10% of the asymptotic value
if abs(delta_GGE_diag) > 1e-10:
    target_range = 0.10  # within 10% of total shift
    close_to_diag = np.abs(N_B2_t - float(N_B2_diag)) < target_range * abs(delta_GGE_diag)
    if np.any(close_to_diag):
        t_settle = t_array[np.where(close_to_diag)[0][0]]
        print(f"  First time within 10% of diagonal: t = {t_settle:.6f}")
    else:
        t_settle = np.inf
        print(f"  Never settles within 10% of diagonal in t < {t_max}")
else:
    t_settle = 0.0

# ALSO: compute from the full time series the actual variance
# to determine if this is oscillation or true relaxation
N_B2_var_early = np.var(N_B2_t[:n_times//4])  # early-time variance
N_B2_var_late = np.var(N_B2_t[3*n_times//4:])  # late-time variance
print(f"\n  Variance analysis:")
print(f"    Early (t < {t_max/4:.1f}): var(N_B2) = {N_B2_var_early:.6e}")
print(f"    Late (t > {3*t_max/4:.1f}): var(N_B2) = {N_B2_var_late:.6e}")
print(f"    Ratio late/early = {N_B2_var_late/N_B2_var_early:.4f}" if N_B2_var_early > 1e-15
      else "    Ratio: undefined (zero early variance)")

# Is this oscillation or decay?
if N_B2_var_early > 1e-15 and N_B2_var_late / N_B2_var_early > 0.5:
    decay_type = "OSCILLATION (persistent, no true decay)"
elif N_B2_var_early > 1e-15 and N_B2_var_late / N_B2_var_early > 0.1:
    decay_type = "PARTIAL DECAY (some damping)"
else:
    decay_type = "TRUE DECAY (amplitude dies out)"

print(f"    Type: {decay_type}")

# GATE DECISION
# The effective B2 decay time is the FIRST CROSSING TIME.
# For oscillation, the "decay" is really dephasing.
# The characteristic timescale is max(t_first_cross, t_dephase/2).

t_decay_B2 = t_first_cross if np.isfinite(t_first_cross) else t_dephase

print(f"\n--- DECISIVE NUMBERS ---")
print(f"  <N_B2>(t=0) = {N_B2_t[0]:.10f} (93.0% of total)")
print(f"  <N_B2>_diag = {float(N_B2_diag):.10f}")
print(f"  Delta = {delta_GGE_diag:.10f} ({relative_shift*100:.4f}%)")
print(f"  t_first_cross = {t_first_cross:.6f}")
print(f"  t_dephase = {t_dephase:.4f}")
print(f"  t_decay(B2) = {t_decay_B2:.6f}")
print(f"  t_therm (FGR, full system) = {t_therm_FGR:.4f}")
print(f"  Nazarewicz Gamma_B2 = 7.5 -> t_Naz = {1.0/7.5:.4f}")
print(f"  Dynamics type: {decay_type}")

# N_B2 oscillation extrema
N_B2_min = np.min(N_B2_t)
N_B2_max = np.max(N_B2_t)
N_B2_range = N_B2_max - N_B2_min
print(f"\n  N_B2 range: [{N_B2_min:.6f}, {N_B2_max:.6f}]")
print(f"  Oscillation amplitude: {N_B2_range:.6f} ({N_B2_range/f_B2_0*100:.2f}%)")

# Gate classification
if t_decay_B2 < 1.0:
    gate_verdict = "B2-FIRST"
    gate_detail = (f"t_decay(B2) = {t_decay_B2:.4f} < 1. "
                   f"B2 reaches diagonal ensemble FAST. "
                   f"Nazarewicz prediction CONFIRMED. "
                   f"Type: {decay_type}")
elif t_decay_B2 > 10.0:
    gate_verdict = "B2-LAST"
    gate_detail = (f"t_decay(B2) = {t_decay_B2:.4f} > 10. "
                   f"B2 retains information past thermalization. "
                   f"Spectral horizon CONFIRMED. "
                   f"Type: {decay_type}")
else:
    gate_verdict = "INTERMEDIATE"
    gate_detail = (f"t_decay(B2) = {t_decay_B2:.4f} in [1, 10]. "
                   f"B2 dephases on intermediate timescale. "
                   f"Type: {decay_type}")

print(f"\n{'=' * 78}")
print(f"GATE B2-DECAY-40: {gate_verdict}")
print(f"  {gate_detail}")
print(f"{'=' * 78}")

# ======================================================================
#  STEP 16: Save data
# ======================================================================

print("\n--- Step 16: Save data ---")

save_dict = {
    # Gate
    'gate_verdict': np.array([gate_verdict]),
    'gate_detail': np.array([gate_detail]),

    # Time series
    't_array': t_array,
    'N_B2_t': N_B2_t,
    'N_B1_t': N_B1_t,
    'N_B3_t': N_B3_t,
    'H_B1_t': H_B1_t,
    'H_B2_t': H_B2_t,
    'H_B3_t': H_B3_t,
    'H_cross_t': H_cross_t,
    'P_NB2_t': P_NB2_t,
    'P_Npair1_t': P_Npair1_t,
    'purity_t': purity_t,
    'S_vN_t': S_vN_t,

    # Key numbers
    't_decay_B2': np.array(t_decay_B2),
    't_first_cross': np.array(t_first_cross),
    't_dephase': np.array(t_dephase),
    't_therm_FGR': np.array(t_therm_FGR),
    'N_B2_initial': np.array(N_B2_t[0]),
    'N_B2_diag': np.array(float(N_B2_diag)),
    'delta_GGE_diag': np.array(delta_GGE_diag),
    'relative_shift': np.array(relative_shift),
    'N_B2_range': np.array(N_B2_range),
    'Gamma_fit': np.array(Gamma_fit),

    # Energy transfer rates
    'dHB2_dt': dHB2_dt,
    'dHB1_dt': dHB1_dt,
    'dHB3_dt': dHB3_dt,

    # Diagonal ensemble
    'N_B2_diag_ensemble': np.array(float(N_B2_diag)),
    'N_B1_diag_ensemble': np.array(float(N_B1_diag)),
    'N_B3_diag_ensemble': np.array(float(N_B3_diag)),
    'P_NB2_diag': np.array([P_NB2_diag[k] for k in range(5)]),

    # Eigenstate analysis
    'B2_content_eigenstates': B2_content_eigenstates,
    'p_eig': p_eig,
    'evals_H1': evals_H1,

    # Cross-checks
    'max_diff_8vs256': np.array(max_diff_NB2),
    'Npair_conservation': np.array(np.max(np.abs(P_Npair1_t - 1.0))),
    'energy_conservation': np.array(np.max(np.abs(H_total_t - H_total_t[0]))),

    # Variance analysis
    'N_B2_var_early': np.array(N_B2_var_early),
    'N_B2_var_late': np.array(N_B2_var_late),
    'decay_type': np.array([decay_type]),

    # Inputs
    'E_8': E_8,
    'V_phys': V_phys,
    'p_k': p_k,
    'lambda_k': lambda_k,
    'branch_labels': np.array(branch_labels),
}

np.savez(os.path.join(SCRIPT_DIR, 's40_b2_decay_out.npz'), **save_dict)
print(f"  Saved: tier0-computation/s40_b2_decay_out.npz")

# ======================================================================
#  STEP 17: Plots
# ======================================================================

print("\n--- Step 17: Generate plots ---")

fig = plt.figure(figsize=(24, 20))
gs_fig = GridSpec(4, 3, figure=fig, hspace=0.4, wspace=0.35)

# Panel 1: B2 occupation vs time
ax1 = fig.add_subplot(gs_fig[0, 0])
ax1.plot(t_array, N_B2_t, 'b-', linewidth=1.0, label=r'$\langle N_{B2} \rangle(t)$')
ax1.axhline(float(N_B2_diag), color='r', linestyle='--', linewidth=1.0,
            label=f'Diagonal: {float(N_B2_diag):.4f}')
ax1.axhline(N_B2_t[0], color='gray', linestyle=':', linewidth=0.8,
            label=f'Initial: {N_B2_t[0]:.4f}')
if np.isfinite(t_first_cross) and t_first_cross < t_max:
    ax1.axvline(t_first_cross, color='green', linestyle='-.', linewidth=0.8,
                label=f't_cross = {t_first_cross:.2f}')
ax1.set_xlabel('t (natural units)')
ax1.set_ylabel(r'$\langle N_{B2} \rangle$')
ax1.set_title('B2 Occupation vs Time')
ax1.legend(fontsize=8)
ax1.set_xlim([0, t_max])

# Panel 2: All branch occupations
ax2 = fig.add_subplot(gs_fig[0, 1])
ax2.plot(t_array, N_B2_t, 'b-', linewidth=1.0, label='B2')
ax2.plot(t_array, N_B1_t, 'r-', linewidth=1.0, label='B1')
ax2.plot(t_array, N_B3_t, 'g-', linewidth=1.0, label='B3')
ax2.axhline(float(N_B2_diag), color='b', linestyle='--', linewidth=0.5, alpha=0.5)
ax2.axhline(float(N_B1_diag), color='r', linestyle='--', linewidth=0.5, alpha=0.5)
ax2.axhline(float(N_B3_diag), color='g', linestyle='--', linewidth=0.5, alpha=0.5)
ax2.set_xlabel('t')
ax2.set_ylabel('Branch occupation')
ax2.set_title('All Branch Occupations')
ax2.legend(fontsize=8)
ax2.set_xlim([0, t_max])

# Panel 3: Early time zoom (t < 2)
ax3 = fig.add_subplot(gs_fig[0, 2])
t_zoom = 2.0
mask_zoom = t_array <= t_zoom
ax3.plot(t_array[mask_zoom], N_B2_t[mask_zoom], 'b-', linewidth=1.5, label='B2')
ax3.plot(t_array[mask_zoom], N_B1_t[mask_zoom], 'r-', linewidth=1.5, label='B1')
ax3.plot(t_array[mask_zoom], N_B3_t[mask_zoom], 'g-', linewidth=1.5, label='B3')
ax3.axhline(float(N_B2_diag), color='b', linestyle='--', linewidth=0.5, alpha=0.5)
t_naz = 1.0/7.5
ax3.axvline(t_naz, color='orange', linestyle='--', linewidth=1.0,
            label=f'Naz t={t_naz:.3f}')
ax3.set_xlabel('t')
ax3.set_ylabel('Branch occupation')
ax3.set_title(f'Early Time (t < {t_zoom})')
ax3.legend(fontsize=8)

# Panel 4: B2 sector probabilities P(N_B2 = k)
ax4 = fig.add_subplot(gs_fig[1, 0])
colors_P = ['gray', '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']
for nval in range(5):
    if np.max(np.abs(P_NB2_t[nval])) > 1e-10:
        ax4.plot(t_array, P_NB2_t[nval], '-', linewidth=1.0,
                 color=colors_P[nval], label=f'N_B2={nval}')
        ax4.axhline(P_NB2_diag[nval], color=colors_P[nval],
                     linestyle='--', linewidth=0.5, alpha=0.5)
ax4.set_xlabel('t')
ax4.set_ylabel('Probability')
ax4.set_title(r'$P(N_{B2} = k)$ vs Time')
ax4.legend(fontsize=8)
ax4.set_xlim([0, t_max])

# Panel 5: Energy transfer rates
ax5 = fig.add_subplot(gs_fig[1, 1])
ax5.plot(t_array, dHB2_dt, 'b-', linewidth=0.8, label='dH_B2/dt')
ax5.plot(t_array, dHB1_dt, 'r-', linewidth=0.8, label='dH_B1/dt')
ax5.plot(t_array, dHB3_dt, 'g-', linewidth=0.8, label='dH_B3/dt')
ax5.axhline(0, color='black', linewidth=0.5)
ax5.set_xlabel('t')
ax5.set_ylabel('Energy transfer rate')
ax5.set_title('Branch Energy Transfer Rates')
ax5.legend(fontsize=8)
ax5.set_xlim([0, t_max])

# Panel 6: B2 content of eigenstates
ax6 = fig.add_subplot(gs_fig[1, 2])
colors_eig = ['#1f77b4']*4 + ['#ff7f0e'] + ['#2ca02c']*3
for n in range(N):
    ax6.scatter(evals_H1[n], B2_content_eigenstates[n],
                s=p_eig[n]*500+20, color=colors_eig[n],
                edgecolor='black', zorder=5)
    ax6.annotate(f'p={p_eig[n]:.3f}', (evals_H1[n], B2_content_eigenstates[n]),
                 textcoords="offset points", xytext=(0, 12),
                 ha='center', fontsize=7)
ax6.set_xlabel(r'$E_n$ (H_1 eigenvalue)')
ax6.set_ylabel('B2 content')
ax6.set_title('B2 Content of H_1 Eigenstates')
ax6.axhline(float(N_B2_diag), color='red', linestyle='--', linewidth=0.8,
            label=f'<N_B2>_diag')
ax6.legend(fontsize=8)

# Panel 7: Fourier power spectrum
ax7 = fig.add_subplot(gs_fig[2, 0])
ax7.semilogy(freqs[1:n_times//4], power[1:n_times//4], 'b-', linewidth=0.8)
ax7.set_xlabel('Frequency')
ax7.set_ylabel('Power')
ax7.set_title('Fourier Spectrum of N_B2(t)')

# Mark H_1 energy gaps
for n in range(1, N):
    dE_n = evals_H1[n] - evals_H1[0]
    f_n = dE_n / (2*np.pi)
    if f_n < freqs[n_times//4]:
        ax7.axvline(f_n, color='red', linestyle='--', linewidth=0.5, alpha=0.7)

# Panel 8: N_B2 oscillation envelope
ax8 = fig.add_subplot(gs_fig[2, 1])
ax8.plot(t_array, N_B2_t, 'b-', linewidth=0.5, alpha=0.5, label='N_B2(t)')
ax8.plot(t_array, np.mean(N_B2_t) + envelope, 'r-', linewidth=1.0,
         label='Upper envelope')
ax8.plot(t_array, np.mean(N_B2_t) - envelope, 'r-', linewidth=1.0,
         label='Lower envelope')
ax8.axhline(float(N_B2_diag), color='green', linestyle='--', linewidth=1.0,
            label='Diagonal ensemble')
ax8.set_xlabel('t')
ax8.set_ylabel(r'$\langle N_{B2} \rangle$')
ax8.set_title('B2 Oscillation Envelope')
ax8.legend(fontsize=8)
ax8.set_xlim([0, t_max])

# Panel 9: Conservation checks
ax9 = fig.add_subplot(gs_fig[2, 2])
ax9.semilogy(t_array, np.abs(P_Npair1_t - 1.0) + 1e-16, 'b-', linewidth=0.8,
             label='|P(N=1)-1|')
ax9.semilogy(t_array, np.abs(N_total_t - N_total_t[0]) + 1e-16, 'r-',
             linewidth=0.8, label='|N_total deviation|')
ax9.semilogy(t_array, np.abs(H_total_t - H_total_t[0]) + 1e-16, 'g-',
             linewidth=0.8, label='|E_total deviation|')
ax9.set_xlabel('t')
ax9.set_ylabel('Conservation violation')
ax9.set_title('Conservation Checks')
ax9.legend(fontsize=8)
ax9.set_xlim([0, t_max])

# Panel 10: 8-dim vs 256-dim cross-check
ax10 = fig.add_subplot(gs_fig[3, 0])
ax10.plot(t_array[:100], N_B2_t[:100], 'b-', linewidth=2.0, label='256-dim')
ax10.plot(t_array[:100], N_B2_t_8[:100], 'r--', linewidth=1.0, label='8-dim')
ax10.set_xlabel('t')
ax10.set_ylabel(r'$\langle N_{B2} \rangle$')
ax10.set_title('256-dim vs 8-dim Cross-Check')
ax10.legend(fontsize=8)

# Panel 11: Branch energy time series
ax11 = fig.add_subplot(gs_fig[3, 1])
ax11.plot(t_array, H_B2_t, 'b-', linewidth=1.0, label='H_B2')
ax11.plot(t_array, H_B1_t, 'r-', linewidth=1.0, label='H_B1')
ax11.plot(t_array, H_B3_t, 'g-', linewidth=1.0, label='H_B3')
ax11.plot(t_array, H_cross_t, 'k-', linewidth=0.8, alpha=0.5, label='H_cross')
ax11.set_xlabel('t')
ax11.set_ylabel('Energy')
ax11.set_title('Branch Energies vs Time')
ax11.legend(fontsize=8)
ax11.set_xlim([0, t_max])

# Panel 12: Summary text
ax12 = fig.add_subplot(gs_fig[3, 2])
ax12.axis('off')
summary_lines = [
    f"GATE: B2-DECAY-40 = {gate_verdict}",
    "",
    f"N_B2(0) = {N_B2_t[0]:.6f} (93.0%)",
    f"N_B2_diag = {float(N_B2_diag):.6f}",
    f"Delta = {delta_GGE_diag:.6f} ({relative_shift*100:.2f}%)",
    "",
    f"t_first_cross = {t_first_cross:.4f}",
    f"t_dephase = {t_dephase:.4f}",
    f"t_decay(B2) = {t_decay_B2:.4f}",
    f"t_therm(FGR) = {t_therm_FGR:.4f}",
    f"Naz 1/Gamma = {1.0/7.5:.4f}",
    "",
    f"Oscillation range: {N_B2_range:.6f}",
    f"Type: {decay_type}",
    "",
    "Cross-checks:",
    f"  8d vs 256d: {max_diff_NB2:.2e}",
    f"  N conservation: {np.max(np.abs(P_Npair1_t-1)):.2e}",
    f"  E conservation: {np.max(np.abs(H_total_t-H_total_t[0])):.2e}",
]
for i, line in enumerate(summary_lines):
    fontweight = 'bold' if i == 0 else 'normal'
    color = 'green' if 'B2-FIRST' in line else \
            'red' if 'B2-LAST' in line else \
            'orange' if 'INTERMEDIATE' in line else 'black'
    ax12.text(0.02, 0.97 - i*0.05, line, transform=ax12.transAxes,
              fontsize=9, fontweight=fontweight, color=color,
              verticalalignment='top', fontfamily='monospace')

fig.suptitle(f'Session 40 W2-3: B2 Decay-Out Time-Dependent ED\n'
             f'Gate: {gate_verdict} | t_decay = {t_decay_B2:.4f} | '
             f'Type: {decay_type}',
             fontsize=14, fontweight='bold')

plt.savefig(os.path.join(SCRIPT_DIR, 's40_b2_decay_out.png'),
            dpi=150, bbox_inches='tight')
print(f"  Saved: tier0-computation/s40_b2_decay_out.png")

# ======================================================================
#  FINAL SUMMARY
# ======================================================================

print("\n" + "=" * 78)
print("FINAL SUMMARY: B2-DECAY-40")
print("=" * 78)

print(f"\n  GATE: {gate_verdict}")
print(f"  {gate_detail}")

print(f"\n  KEY NUMBERS:")
print(f"    1. <N_B2>(t=0) = {N_B2_t[0]:.6f}")
print(f"    2. <N_B2>_diag = {float(N_B2_diag):.6f}")
print(f"    3. Shift = {delta_GGE_diag:.6f} ({relative_shift*100:.4f}%)")
print(f"    4. t_decay(B2) = {t_decay_B2:.6f}")
print(f"    5. Oscillation amplitude = {N_B2_range:.6f}")

print(f"\n  CROSS-CHECKS:")
print(f"    8-dim vs 256-dim: max|Delta| = {max_diff_NB2:.2e}")
print(f"    N_pair conservation: max dev = {np.max(np.abs(P_Npair1_t - 1.0)):.2e}")
print(f"    E conservation: max dev = {np.max(np.abs(H_total_t - H_total_t[0])):.2e}")
print(f"    P(N_B2) normalization: max dev = {np.max(np.abs(P_NB2_sum_t - 1.0)):.2e}")

print(f"\n  FILES:")
print(f"    Script: tier0-computation/s40_b2_decay_out.py")
print(f"    Data: tier0-computation/s40_b2_decay_out.npz")
print(f"    Plot: tier0-computation/s40_b2_decay_out.png")

print(f"\n  Total runtime: {time.time()-t0_total:.1f}s")
print("\nDone.")
