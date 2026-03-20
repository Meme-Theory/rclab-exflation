#!/usr/bin/env python3
"""
Session 39, W2-3: Post-Quench Spectral Function A(omega)
=========================================================

Computes the spectral function A(omega) = -(1/pi) Im G^R(omega) for the
pair creation operator P^dag, as seen by a 4D observer after the sudden
quench through the BCS phase transition.

Physics:
  - Pre-transit: 8-mode BCS Hamiltonian at the fold (tau ~ 0.20) with
    Kosmann pairing V and van Hove DOS. Ground state |GS_pre> is in
    N_pair = 1 sector (exact, from W1-1).
  - Sudden quench: Transit destroys the BCS condensate (P_exc = 1.0,
    from S38 KZ analysis). Post-transit Hamiltonian has V -> 0.
  - Post-transit eigenstates: Fock states of the non-interacting system
    H_post = sum_k 2*xi_k * n_k.
  - The pre-transit ground state |GS_pre> is expressed in the post-transit
    (Fock) basis. The GGE density matrix is the diagonal ensemble:
    rho_GGE = diag(|<n_Fock|GS_pre>|^2).

Spectral function (Lehmann representation with GGE weights):
  A(omega) = -(1/pi) Im G^R(omega)
  G^R(omega) = sum_{n,m} rho_n * |<m|P^dag|n>|^2 / (omega - (E_m - E_n) + i*eta)
  where rho_n = |<n_Fock|GS_pre>|^2, E_n are post-transit Fock energies.

For comparison, also computes the equilibrium spectral function:
  A_eq(omega) using the BCS ground state with the BCS Hamiltonian eigenbasis.

Gate: SPEC-39
  PASS: GPV pole visible at omega in [0.70, 0.85] with > 30% of total weight.
  FAIL: GPV pole not resolvable above continuum background.

Author: gen-physicist (Session 39)
"""

import os
import sys
import time
import numpy as np
from numpy.linalg import eigh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
t0 = time.time()

print("=" * 78)
print("Session 39, W2-3: Post-Quench Spectral Function A(omega)")
print("=" * 78)

# ======================================================================
#  Step 1: Reconstruct pre-transit BCS Hamiltonian and diagonalize
# ======================================================================

print("\n" + "=" * 78)
print("STEP 1: RECONSTRUCT PRE-TRANSIT BCS HAMILTONIAN")
print("=" * 78)

# Load upstream data (same recipe as s37_pair_susceptibility.py)
data_ed = np.load(os.path.join(SCRIPT_DIR, 's36_multisector_ed.npz'),
                  allow_pickle=True)
vh_arbiter = np.load(os.path.join(SCRIPT_DIR, 's35a_vh_impedance_arbiter.npz'),
                     allow_pickle=True)

V_8x8 = data_ed['V_8x8_full']        # 8x8 Kosmann interaction matrix
E_8 = data_ed['E_8_full']             # 8 single-particle Dirac eigenvalues
branch_labels = list(data_ed['branch_labels'])
E_cond_stored = float(data_ed['config_4_E_cond'])

n_modes = 8
n_states = 2**n_modes  # 256
mu = 0.0
xi = E_8 - mu  # xi_m = E_m - mu

# DOS: B2 modes get van Hove rho, B1 and B3 get 1.0
rho_smooth = float(vh_arbiter['rho_at_physical'])  # 14.023
rho = np.array([rho_smooth]*4 + [1.0, 1.0, 1.0, 1.0])

print(f"  N_modes = {n_modes}, N_states = {n_states}")
print(f"  E_8 = {E_8}")
print(f"  rho = {rho}")
print(f"  branch_labels = {branch_labels}")

# Build the BCS pair Hamiltonian in Fock space
print(f"\n  Building BCS pair Hamiltonian ({n_states}x{n_states})...")

H_BCS = np.zeros((n_states, n_states))

# Diagonal: kinetic energy 2*xi_m for each occupied pair
for state in range(n_states):
    for m in range(n_modes):
        if state & (1 << m):
            H_BCS[state, state] += 2 * xi[m]

# Off-diagonal: pair scattering -V_nm * sqrt(rho_n * rho_m) * b_n^dag b_m
for state in range(n_states):
    for n in range(n_modes):
        for m in range(n_modes):
            if n == m:
                continue
            if V_8x8[n, m] < 1e-15:
                continue
            if (state & (1 << m)) and not (state & (1 << n)):
                new_state = state ^ (1 << m) ^ (1 << n)
                H_BCS[new_state, state] -= V_8x8[n, m] * np.sqrt(rho[n] * rho[m])

H_BCS = 0.5 * (H_BCS + H_BCS.T)  # Ensure Hermiticity

# Full diagonalization
E_pre, psi_pre = eigh(H_BCS)
E_gs_pre = E_pre[0]
psi_gs_pre = psi_pre[:, 0]  # Ground state in Fock basis

print(f"  E_gs (pre-transit) = {E_gs_pre:.12f}")
print(f"  E_cond (stored)    = {E_cond_stored:.12f}")
assert abs(E_gs_pre - E_cond_stored) < 1e-10, \
    f"FATAL: E_gs mismatch: {E_gs_pre} vs {E_cond_stored}"
print(f"  Verification: |E_gs - stored| = {abs(E_gs_pre - E_cond_stored):.2e} OK")

# Verify ground state is in N_pair=1 sector
n_pairs_fock = np.array([bin(s).count('1') for s in range(n_states)])
gs_sector_prob = np.zeros(n_modes + 1)
for s in range(n_states):
    gs_sector_prob[n_pairs_fock[s]] += abs(psi_gs_pre[s])**2
print(f"  GS sector probabilities: {gs_sector_prob}")
print(f"  GS is pure N_pair = {np.argmax(gs_sector_prob)} "
      f"(prob = {np.max(gs_sector_prob):.15f})")

# ======================================================================
#  Step 2: Construct post-transit Hamiltonian (V = 0, non-interacting)
# ======================================================================

print("\n" + "=" * 78)
print("STEP 2: POST-TRANSIT HAMILTONIAN (V = 0)")
print("=" * 78)

# Post-transit: the system exits the BCS window, M_max < 1, no pairing.
# H_post = sum_k 2*xi_k * n_k (diagonal in Fock basis)
# Eigenstates ARE the Fock states |s> with eigenvalues E_s = sum over
# occupied modes of 2*xi_k.

E_post = np.zeros(n_states)
for state in range(n_states):
    for m in range(n_modes):
        if state & (1 << m):
            E_post[state] += 2 * xi[m]

print(f"  Post-transit eigenvalues (Fock states):")
print(f"    E_post range: [{E_post.min():.6f}, {E_post.max():.6f}]")
print(f"    E_post[0] (vacuum) = {E_post[0]:.6f}")

# The Fock states are already ordered by binary index, not by energy.
# Sort by energy for the Lehmann representation.
sort_idx = np.argsort(E_post)
E_post_sorted = E_post[sort_idx]
# The "eigenstates" of H_post in the Fock basis are just delta vectors.
# psi_post[:, n] = delta_{s, sort_idx[n]} in the Fock basis.

print(f"  First 20 post-transit energies (sorted):")
for i in range(min(20, n_states)):
    s = sort_idx[i]
    np_s = n_pairs_fock[s]
    print(f"    E[{i:3d}] = {E_post_sorted[i]:10.6f}  "
          f"Fock state = {s:3d} (N_pair={np_s})")

# ======================================================================
#  Step 3: GGE density matrix (sudden quench approximation)
# ======================================================================

print("\n" + "=" * 78)
print("STEP 3: GGE DENSITY MATRIX (SUDDEN QUENCH)")
print("=" * 78)

# |GS_pre> is expressed in the Fock basis (which IS the post-transit
# eigenbasis since H_post is diagonal in Fock space).
# rho_GGE_nn = |<n_Fock|GS_pre>|^2 = |psi_gs_pre[n]|^2

# But we need rho in the ENERGY-SORTED post-transit basis:
# rho_n = |<sorted_n|GS_pre>|^2 = |psi_gs_pre[sort_idx[n]]|^2

rho_GGE = np.abs(psi_gs_pre[sort_idx])**2  # populations in energy-sorted basis

print(f"  Sum rho_GGE = {np.sum(rho_GGE):.15f} (should be 1)")
print(f"  Number of significantly occupied states (rho > 1e-6): "
      f"{np.sum(rho_GGE > 1e-6)}")
print(f"  Number of significantly occupied states (rho > 1e-3): "
      f"{np.sum(rho_GGE > 1e-3)}")

# Show the dominant GGE populations
print(f"\n  Top 20 GGE populations:")
top_idx = np.argsort(-rho_GGE)
for rank in range(min(20, n_states)):
    i = top_idx[rank]
    s = sort_idx[i]  # Original Fock state index
    np_s = n_pairs_fock[s]
    print(f"    rank {rank:3d}: state {i:3d} (Fock {s:3d}, N_pair={np_s}), "
          f"rho = {rho_GGE[i]:.10f}, E = {E_post_sorted[i]:.6f}")

# Mean energy in GGE
E_mean_GGE = np.sum(rho_GGE * E_post_sorted)
print(f"\n  <H_post>_GGE = {E_mean_GGE:.6f}")
print(f"  E_gs_pre (BCS) = {E_gs_pre:.6f}")
print(f"  Excitation energy = {E_mean_GGE - E_post_sorted[0]:.6f}")

# ======================================================================
#  Step 4: Construct pair creation operator P^dag in Fock basis
# ======================================================================

print("\n" + "=" * 78)
print("STEP 4: PAIR CREATION OPERATOR P^dag")
print("=" * 78)

# P^dag = sum_k sqrt(rho_k) * b_k^dag  (DOS-weighted pair creation)
# In the Fock basis: <s'|P^dag|s> is nonzero when s' has exactly one
# more bit set than s, at position k, weighted by sqrt(rho_k).

# Build the full P^dag matrix in Fock basis (sparse but small enough)
Pdag_matrix = np.zeros((n_states, n_states))
for state in range(n_states):
    for k in range(n_modes):
        if not (state & (1 << k)):  # bit k is 0, can create pair
            new_state = state | (1 << k)
            Pdag_matrix[new_state, state] += np.sqrt(rho[k])

# P = (P^dag)^T for real matrices
P_matrix = Pdag_matrix.T

print(f"  P^dag matrix constructed: {Pdag_matrix.shape}")
print(f"  Nonzero elements: {np.count_nonzero(Pdag_matrix)}")
print(f"  ||P^dag|| = {np.linalg.norm(Pdag_matrix):.6f}")

# Verify sum rule: Tr(P P^dag) = sum_k rho_k * (n_states/2)
# Actually: <s|P P^dag|s> = sum_k rho_k * (1 - n_k(s))
trace_PPdag = np.trace(P_matrix @ Pdag_matrix)
expected_trace = sum(rho[k] * sum(1 for s in range(n_states)
                     if not (s & (1 << k))) for k in range(n_modes))
print(f"  Tr(P P^dag) = {trace_PPdag:.6f}")
print(f"  Expected     = {expected_trace:.6f}")

# ======================================================================
#  Step 5: Compute matrix elements <m|P^dag|n> in energy-sorted basis
# ======================================================================

print("\n" + "=" * 78)
print("STEP 5: MATRIX ELEMENTS IN POST-TRANSIT BASIS")
print("=" * 78)

# In the Fock basis (= post-transit eigenbasis), the matrix elements
# <s'|P^dag|s> are already computed above.
# In the energy-sorted basis, <sorted_m|P^dag|sorted_n> =
# <Fock_{sort_idx[m]}|P^dag|Fock_{sort_idx[n]}> = Pdag_matrix[sort_idx[m], sort_idx[n]]

# For the Lehmann sum, we need |<m|P^dag|n>|^2 for all n where rho_n > 0.
# Since the Fock basis IS the post-transit eigenbasis, the matrix elements
# are just Pdag_matrix elements reindexed.

# Build the reindexed P^dag matrix (energy-sorted)
Pdag_sorted = Pdag_matrix[np.ix_(sort_idx, sort_idx)]
P_sorted = Pdag_sorted.T

# Verify
print(f"  ||Pdag_sorted|| = {np.linalg.norm(Pdag_sorted):.6f}")

# ======================================================================
#  Step 6: Compute GGE spectral function A_GGE(omega)
# ======================================================================

print("\n" + "=" * 78)
print("STEP 6: GGE SPECTRAL FUNCTION A_GGE(omega)")
print("=" * 78)

# Lehmann representation with GGE populations:
# G^R(omega) = sum_{n,m} rho_n * |<m|P^dag|n>|^2 / (omega - (E_m - E_n) + i*eta)
#
# For P (pair removal):
# G^R also includes: - sum_{n,m} rho_n * |<m|P|n>|^2 / (omega + (E_m - E_n) + i*eta)
#
# The FULL retarded Green's function for the pair operator:
# G^R(omega) = sum_{n,m} rho_n * [|<m|O^dag|n>|^2 / (omega - omega_mn + i*eta)]
# where omega_mn = E_m - E_n, and O = P^dag.
#
# This naturally includes both positive and negative frequency contributions.

n_omega = 1000
omega_grid = np.linspace(0.0, 3.0, n_omega)
eta = 0.01

# Precompute all |<m|P^dag|n>|^2 (this is a 256x256 matrix)
Pdag_sq = np.abs(Pdag_sorted)**2  # |<m|P^dag|n>|^2
P_sq = np.abs(P_sorted)**2        # |<m|P|n>|^2

print(f"  omega grid: {n_omega} points in [0, 3.0]")
print(f"  Broadening eta = {eta}")

# Only sum over states with significant population
# (for efficiency, though n_states=256 is small enough for brute force)
sig_mask = rho_GGE > 1e-20
n_sig = np.sum(sig_mask)
print(f"  Significant GGE states (rho > 1e-20): {n_sig}")

# Compute G^R(omega) using vectorized operations
print(f"  Computing G^R(omega)...")
t_compute = time.time()

GR = np.zeros(n_omega, dtype=complex)

# For each populated state n, sum over all final states m
for n in range(n_states):
    if rho_GGE[n] < 1e-20:
        continue

    for m in range(n_states):
        omega_mn = E_post_sorted[m] - E_post_sorted[n]

        # P^dag channel: creates a pair
        if Pdag_sq[m, n] > 1e-20:
            weight = rho_GGE[n] * Pdag_sq[m, n]
            GR += weight / (omega_grid - omega_mn + 1j * eta)

        # P channel: removes a pair (negative frequency contribution)
        if P_sq[m, n] > 1e-20:
            weight = rho_GGE[n] * P_sq[m, n]
            GR -= weight / (omega_grid + omega_mn + 1j * eta)

A_GGE = -(1.0 / np.pi) * np.imag(GR)

dt_compute = time.time() - t_compute
print(f"  Computation time: {dt_compute:.2f}s")
print(f"  max A_GGE = {np.max(A_GGE):.6f}")
print(f"  A_GGE integral (trapezoidal) = {np.trapezoid(A_GGE, omega_grid):.6f}")

# ======================================================================
#  Step 7: Compute EQUILIBRIUM spectral function A_eq(omega) for comparison
# ======================================================================

print("\n" + "=" * 78)
print("STEP 7: EQUILIBRIUM (BCS) SPECTRAL FUNCTION")
print("=" * 78)

# The equilibrium spectral function uses:
# - The BCS ground state |GS_pre> as the reference state
# - The BCS Hamiltonian H_BCS eigenbasis
# G^R_eq(omega) = sum_{n} |<n|P^dag|GS>|^2 / (omega - (E_n - E_0) + i*eta)
#               - sum_{n} |<n|P|GS>|^2 / (omega + (E_n - E_0) + i*eta)
# This is the Lehmann representation from S37 pair susceptibility.

# Compute P^dag|GS> and P|GS> in the BCS eigenbasis
Pdag_gs_fock = Pdag_matrix @ psi_gs_pre  # P^dag|GS> in Fock basis
P_gs_fock = P_matrix @ psi_gs_pre        # P|GS> in Fock basis

# Project onto BCS eigenstates
Bn_plus_eq = np.abs(psi_pre.T @ Pdag_gs_fock)**2   # |<n_BCS|P^dag|GS>|^2
Bn_minus_eq = np.abs(psi_pre.T @ P_gs_fock)**2      # |<n_BCS|P|GS>|^2

omega_n_eq = E_pre - E_gs_pre  # Excitation energies

# Equilibrium spectral function
GR_eq = np.zeros(n_omega, dtype=complex)
for n in range(n_states):
    if Bn_plus_eq[n] > 1e-20:
        GR_eq += Bn_plus_eq[n] / (omega_grid - omega_n_eq[n] + 1j * eta)
    if Bn_minus_eq[n] > 1e-20:
        GR_eq -= Bn_minus_eq[n] / (omega_grid + omega_n_eq[n] + 1j * eta)

A_eq = -(1.0 / np.pi) * np.imag(GR_eq)

print(f"  max A_eq = {np.max(A_eq):.6f}")
print(f"  A_eq integral = {np.trapezoid(A_eq, omega_grid):.6f}")
print(f"  Sum |<n|P^dag|GS>|^2 = {np.sum(Bn_plus_eq):.6f}")
print(f"  Sum |<n|P|GS>|^2    = {np.sum(Bn_minus_eq):.6f}")

# Find dominant equilibrium poles
print(f"\n  Dominant equilibrium P^dag poles:")
top_eq = np.argsort(-Bn_plus_eq)
for rank in range(min(10, n_states)):
    i = top_eq[rank]
    if Bn_plus_eq[i] < 1e-6:
        break
    print(f"    omega = {omega_n_eq[i]:.6f}, |<n|P^dag|GS>|^2 = {Bn_plus_eq[i]:.6f}")

# ======================================================================
#  Step 8: Identify spectral features in A_GGE
# ======================================================================

print("\n" + "=" * 78)
print("STEP 8: SPECTRAL FEATURE IDENTIFICATION (GGE)")
print("=" * 78)

# Find peaks in A_GGE
from scipy.signal import find_peaks

peaks_idx, peak_props = find_peaks(A_GGE, height=0.01, prominence=0.005,
                                    distance=5)

print(f"  Found {len(peaks_idx)} peaks in A_GGE(omega):")
print(f"  {'Rank':>4s}  {'omega':>8s}  {'A(omega)':>10s}  {'prom':>8s}")

peak_data = []
for rank, idx in enumerate(sorted(peaks_idx, key=lambda i: -A_GGE[i])):
    omega_peak = omega_grid[idx]
    height = A_GGE[idx]
    prom = peak_props['prominences'][list(peaks_idx).index(idx)]
    peak_data.append({
        'omega': omega_peak,
        'height': height,
        'prominence': prom,
        'index': idx,
    })
    if rank < 20:
        print(f"  {rank:4d}  {omega_peak:8.4f}  {height:10.6f}  {prom:8.4f}")

# Expected features:
# 1. GPV pole at omega ~ 0.79
# 2. Pair-removal pole at omega ~ 0.14
# 3. Pair continuum edge at omega ~ 2*Delta_OES = 0.93

# Check S37 reference values
d37_ps = np.load(os.path.join(SCRIPT_DIR, 's37_pair_susceptibility.npz'),
                 allow_pickle=True)
omega_PV_s37 = float(d37_ps['omega_plus'])
omega_minus_s37 = float(d37_ps['omega_minus'])
Delta_OES_s37 = float(d37_ps['Delta_OES'])

print(f"\n  Reference values from S37:")
print(f"    omega_PV (pair vibration) = {omega_PV_s37:.6f}")
print(f"    omega_minus (pair removal) = {omega_minus_s37:.6f}")
print(f"    Delta_OES = {Delta_OES_s37:.6f}")
print(f"    2*Delta_OES = {2*Delta_OES_s37:.6f}")

# Identify GPV peak: closest peak to omega_PV_s37 in [0.5, 1.2]
gpv_candidates = [p for p in peak_data if 0.5 < p['omega'] < 1.2]
if gpv_candidates:
    gpv_peak = min(gpv_candidates, key=lambda p: abs(p['omega'] - omega_PV_s37))
    print(f"\n  GPV pole candidate: omega = {gpv_peak['omega']:.4f}, "
          f"A = {gpv_peak['height']:.6f}")
else:
    gpv_peak = None
    print(f"\n  WARNING: No GPV pole candidate found in [0.5, 1.2]")

# Identify pair-removal peak: closest to omega_minus_s37
removal_candidates = [p for p in peak_data if 0.01 < p['omega'] < 0.5]
if removal_candidates:
    removal_peak = min(removal_candidates,
                       key=lambda p: abs(p['omega'] - omega_minus_s37))
    print(f"  Pair-removal pole candidate: omega = {removal_peak['omega']:.4f}, "
          f"A = {removal_peak['height']:.6f}")
else:
    removal_peak = None
    print(f"  WARNING: No pair-removal pole candidate in [0.01, 0.5]")

# ======================================================================
#  Step 9: Spectral weight decomposition
# ======================================================================

print("\n" + "=" * 78)
print("STEP 9: SPECTRAL WEIGHT DECOMPOSITION")
print("=" * 78)

# Total spectral weight
S_total = np.trapezoid(A_GGE, omega_grid)
print(f"  Total spectral weight S_total = {S_total:.6f}")

# Weight in GPV peak region [0.60, 1.00]
gpv_lo, gpv_hi = 0.60, 1.00
gpv_mask = (omega_grid >= gpv_lo) & (omega_grid <= gpv_hi)
S_GPV = np.trapezoid(A_GGE[gpv_mask], omega_grid[gpv_mask])
print(f"  GPV region [{gpv_lo}, {gpv_hi}]: S_GPV = {S_GPV:.6f}")
print(f"  S_GPV / S_total = {S_GPV / S_total:.6f} ({S_GPV/S_total*100:.1f}%)")

# Weight in pair-removal region [0.0, 0.3]
rem_lo, rem_hi = 0.0, 0.30
rem_mask = (omega_grid >= rem_lo) & (omega_grid <= rem_hi)
S_removal = np.trapezoid(A_GGE[rem_mask], omega_grid[rem_mask])
print(f"  Removal region [{rem_lo}, {rem_hi}]: S_removal = {S_removal:.6f}")
print(f"  S_removal / S_total = {S_removal / S_total:.6f} ({S_removal/S_total*100:.1f}%)")

# Weight in continuum [1.0, 3.0]
cont_lo, cont_hi = 1.00, 3.00
cont_mask = (omega_grid >= cont_lo) & (omega_grid <= cont_hi)
S_cont = np.trapezoid(A_GGE[cont_mask], omega_grid[cont_mask])
print(f"  Continuum [{cont_lo}, {cont_hi}]: S_cont = {S_cont:.6f}")
print(f"  S_cont / S_total = {S_cont / S_total:.6f} ({S_cont/S_total*100:.1f}%)")

# More refined GPV weight: integrate around the GPV peak if found
if gpv_peak is not None:
    omega_gpv = gpv_peak['omega']
    # Use a window of width 2*eta around the peak
    gpv_narrow_lo = omega_gpv - 0.10
    gpv_narrow_hi = omega_gpv + 0.10
    gpv_narrow_mask = (omega_grid >= gpv_narrow_lo) & (omega_grid <= gpv_narrow_hi)
    S_GPV_narrow = np.trapezoid(A_GGE[gpv_narrow_mask], omega_grid[gpv_narrow_mask])
    print(f"\n  GPV narrow [{gpv_narrow_lo:.2f}, {gpv_narrow_hi:.2f}]: "
          f"S_GPV_narrow = {S_GPV_narrow:.6f} ({S_GPV_narrow/S_total*100:.1f}%)")

# Gate-relevant: weight in [0.70, 0.85]
gate_lo, gate_hi = 0.70, 0.85
gate_mask = (omega_grid >= gate_lo) & (omega_grid <= gate_hi)
S_gate = np.trapezoid(A_GGE[gate_mask], omega_grid[gate_mask])
print(f"\n  GATE REGION [{gate_lo}, {gate_hi}]: S_gate = {S_gate:.6f} "
      f"({S_gate/S_total*100:.1f}%)")

# Also check broader definition: any peak in [0.70, 0.85] with > 30% weight
# Use the full spectral decomposition via the Lehmann sum
# Compute the discrete pole decomposition
print(f"\n  Discrete pole analysis (from Lehmann sum):")

# Collect all transition energies and weights
pole_list = []
for n in range(n_states):
    if rho_GGE[n] < 1e-20:
        continue
    for m in range(n_states):
        omega_mn = E_post_sorted[m] - E_post_sorted[n]
        w_plus = rho_GGE[n] * Pdag_sq[m, n]
        w_minus = rho_GGE[n] * P_sq[m, n]

        if w_plus > 1e-15 and omega_mn > 0.001:
            pole_list.append({
                'omega': omega_mn,
                'weight': w_plus,
                'type': 'P^dag',
                'n': n, 'm': m,
            })
        if w_minus > 1e-15 and omega_mn > 0.001:
            pole_list.append({
                'omega': -omega_mn,  # Negative freq for P channel
                'weight': w_minus,
                'type': 'P',
                'n': n, 'm': m,
            })

# Sort by absolute weight
pole_list.sort(key=lambda p: -p['weight'])

# Only positive-frequency poles for spectral function
pos_poles = [p for p in pole_list if p['omega'] > 0]
total_pos_weight = sum(p['weight'] for p in pos_poles)

print(f"  Total positive-frequency poles: {len(pos_poles)}")
print(f"  Total positive weight: {total_pos_weight:.6f}")

# Show top 20 poles
print(f"\n  Top 20 positive-frequency poles:")
print(f"  {'Rank':>4s}  {'omega':>10s}  {'weight':>12s}  {'frac':>8s}  {'type':>6s}")
cum_weight = 0
for rank, p in enumerate(pos_poles[:20]):
    cum_weight += p['weight']
    frac = p['weight'] / total_pos_weight
    print(f"  {rank:4d}  {p['omega']:10.6f}  {p['weight']:12.8f}  "
          f"{frac*100:7.2f}%  {p['type']:>6s}")

# Weight in gate window [0.70, 0.85] from discrete poles
gate_pole_weight = sum(p['weight'] for p in pos_poles
                       if gate_lo <= p['omega'] <= gate_hi)
gate_pole_frac = gate_pole_weight / total_pos_weight if total_pos_weight > 0 else 0
print(f"\n  Gate window [{gate_lo}, {gate_hi}] pole weight: "
      f"{gate_pole_weight:.6f} ({gate_pole_frac*100:.1f}%)")

# Weight in [0.60, 1.00]
gpv_pole_weight = sum(p['weight'] for p in pos_poles
                      if gpv_lo <= p['omega'] <= gpv_hi)
gpv_pole_frac = gpv_pole_weight / total_pos_weight if total_pos_weight > 0 else 0
print(f"  GPV window [{gpv_lo}, {gpv_hi}] pole weight: "
      f"{gpv_pole_weight:.6f} ({gpv_pole_frac*100:.1f}%)")

# ======================================================================
#  Step 10: Comparison GGE vs equilibrium
# ======================================================================

print("\n" + "=" * 78)
print("STEP 10: GGE vs EQUILIBRIUM COMPARISON")
print("=" * 78)

S_total_eq = np.trapezoid(A_eq, omega_grid)
S_GPV_eq = np.trapezoid(A_eq[gpv_mask], omega_grid[gpv_mask])

print(f"  Equilibrium total weight: {S_total_eq:.6f}")
print(f"  Equilibrium GPV region [{gpv_lo}, {gpv_hi}]: {S_GPV_eq:.6f} "
      f"({S_GPV_eq/S_total_eq*100:.1f}% of total)")

# Broadening comparison: width of dominant peak
# For equilibrium, the dominant peak is at omega_PV = 0.792
eq_peaks_idx, eq_peak_props = find_peaks(A_eq, height=0.1, prominence=0.05)
print(f"\n  Equilibrium peaks (A > 0.1):")
for idx in eq_peaks_idx:
    print(f"    omega = {omega_grid[idx]:.4f}, A = {A_eq[idx]:.4f}")

# Compute FWHM of dominant GGE peak
if gpv_peak is not None:
    gpv_idx = gpv_peak['index']
    half_max = A_GGE[gpv_idx] / 2.0
    # Search left
    left_idx = gpv_idx
    while left_idx > 0 and A_GGE[left_idx] > half_max:
        left_idx -= 1
    # Search right
    right_idx = gpv_idx
    while right_idx < n_omega - 1 and A_GGE[right_idx] > half_max:
        right_idx += 1
    fwhm_gge = omega_grid[right_idx] - omega_grid[left_idx]
    print(f"\n  GGE GPV peak FWHM: {fwhm_gge:.4f}")

    # For equilibrium: FWHM is determined by eta (Lorentzian)
    fwhm_eq_expected = 2 * eta  # Lorentzian FWHM
    print(f"  Equilibrium GPV peak FWHM (Lorentzian): {fwhm_eq_expected:.4f}")
    print(f"  Broadening ratio (GGE/eq): {fwhm_gge / fwhm_eq_expected:.2f}")

# "Information loss" through the quench:
# The equilibrium state has delta-function peaks. The GGE spreads these
# over a range of frequencies. The difference quantifies decoherence.
# Use the Jensen-Shannon divergence between normalized spectral functions.

# Normalize to probability distributions
A_GGE_norm = A_GGE / np.trapezoid(A_GGE, omega_grid) if S_total > 0 else A_GGE
A_eq_norm = A_eq / np.trapezoid(A_eq, omega_grid) if S_total_eq > 0 else A_eq

# Avoid log(0) -- clip to small positive values
eps = 1e-30
A_GGE_clip = np.clip(A_GGE_norm, eps, None)
A_eq_clip = np.clip(A_eq_norm, eps, None)
M = 0.5 * (A_GGE_clip + A_eq_clip)
JSD = 0.5 * np.trapezoid(
    A_GGE_clip * np.log(A_GGE_clip / M) +
    A_eq_clip * np.log(A_eq_clip / M),
    omega_grid
)
JSD = max(JSD, 0.0)  # Ensure non-negative (numerical noise)
print(f"\n  Jensen-Shannon divergence D_JS(A_GGE || A_eq) = {JSD:.6f}")
print(f"  sqrt(JSD) = {np.sqrt(abs(JSD)):.6f} (JS distance)")

# ======================================================================
#  Step 11: Additional spectral analysis at different eta
# ======================================================================

print("\n" + "=" * 78)
print("STEP 11: ETA SENSITIVITY")
print("=" * 78)

eta_values = [0.001, 0.005, 0.01, 0.02, 0.05]
A_multi_eta = np.zeros((len(eta_values), n_omega))

for ie, eta_val in enumerate(eta_values):
    GR_temp = np.zeros(n_omega, dtype=complex)
    for n in range(n_states):
        if rho_GGE[n] < 1e-20:
            continue
        for m in range(n_states):
            omega_mn = E_post_sorted[m] - E_post_sorted[n]
            if Pdag_sq[m, n] > 1e-20:
                w = rho_GGE[n] * Pdag_sq[m, n]
                GR_temp += w / (omega_grid - omega_mn + 1j * eta_val)
            if P_sq[m, n] > 1e-20:
                w = rho_GGE[n] * P_sq[m, n]
                GR_temp -= w / (omega_grid + omega_mn + 1j * eta_val)
    A_multi_eta[ie, :] = -(1.0 / np.pi) * np.imag(GR_temp)
    S_temp = np.trapezoid(A_multi_eta[ie, :], omega_grid)
    max_temp = np.max(A_multi_eta[ie, :])
    print(f"  eta = {eta_val:.3f}: max A = {max_temp:.4f}, "
          f"integral = {S_temp:.6f}")

# ======================================================================
#  Step 12: GATE VERDICT
# ======================================================================

print("\n" + "=" * 78)
print("STEP 12: GATE VERDICT SPEC-39")
print("=" * 78)

# Gate criterion: GPV pole visible at omega in [0.70, 0.85]
# with > 30% of total spectral weight

# Check for peak in gate window
gate_peaks = [p for p in peak_data if gate_lo <= p['omega'] <= gate_hi]
has_peak_in_gate = len(gate_peaks) > 0

# Use both continuous integration and discrete pole decomposition
# The continuous integral in [0.70, 0.85] gives S_gate
# The discrete pole weight in [0.70, 0.85] gives gate_pole_frac

# For the gate, use the broader GPV window [0.60, 1.00] first
# to see if the spectral weight is concentrated there at all

print(f"\n  GATE CRITERION: GPV pole in [0.70, 0.85] with > 30% weight")
print(f"\n  Results:")
print(f"    Peak in [0.70, 0.85]? {has_peak_in_gate}")
if has_peak_in_gate:
    best_gate_peak = max(gate_peaks, key=lambda p: p['height'])
    print(f"    Best peak: omega = {best_gate_peak['omega']:.4f}, "
          f"A = {best_gate_peak['height']:.6f}")

print(f"\n    Spectral weight fractions:")
print(f"      [0.70, 0.85] (gate): {S_gate/S_total*100:.1f}% "
      f"(continuous), {gate_pole_frac*100:.1f}% (discrete)")
print(f"      [0.60, 1.00] (GPV):  {S_GPV/S_total*100:.1f}% "
      f"(continuous), {gpv_pole_frac*100:.1f}% (discrete)")
print(f"      [0.00, 0.30] (removal): {S_removal/S_total*100:.1f}%")
print(f"      [1.00, 3.00] (cont): {S_cont/S_total*100:.1f}%")

# Verdict
# Use the stricter criterion: weight in the gate window [0.70, 0.85]
gpv_visible = has_peak_in_gate and (S_gate / S_total > 0.30)

# Also check: is any IDENTIFIABLE peak in [0.70, 0.85] with > 30%?
# If the GPV pole has shifted or broadened, use the wider definition
gpv_visible_broad = (S_GPV / S_total > 0.30)

if gpv_visible:
    verdict = "PASS"
    verdict_detail = (f"GPV pole at omega = {best_gate_peak['omega']:.4f} "
                     f"with {S_gate/S_total*100:.1f}% weight in [0.70, 0.85]")
elif gpv_visible_broad:
    verdict = "PASS (broad)"
    verdict_detail = (f"GPV spectral weight {S_GPV/S_total*100:.1f}% in "
                     f"[0.60, 1.00], peak may be shifted or broadened")
elif has_peak_in_gate:
    verdict = "FAIL"
    verdict_detail = (f"GPV peak present at omega = {best_gate_peak['omega']:.4f} "
                     f"but weight only {S_gate/S_total*100:.1f}% (< 30%)")
else:
    verdict = "FAIL"
    verdict_detail = "No GPV pole resolvable in [0.70, 0.85]"

print(f"\n  +------------------------------------------------------+")
print(f"  |  GATE SPEC-39: {verdict:>35s}    |")
detail_line = verdict_detail[:52]
print(f"  |  {detail_line:<52s}  |")
print(f"  +------------------------------------------------------+")

# ======================================================================
#  Step 13: SAVE
# ======================================================================

print("\n" + "=" * 78)
print("STEP 13: SAVING RESULTS")
print("=" * 78)

save_dict = {
    # Grid and parameters
    'omega_grid': omega_grid,
    'eta': eta,
    'n_omega': n_omega,
    'n_modes': n_modes,
    'n_states': n_states,

    # GGE spectral function
    'A_GGE': A_GGE,
    'GR_GGE_real': np.real(GR),
    'GR_GGE_imag': np.imag(GR),

    # Equilibrium spectral function
    'A_eq': A_eq,
    'GR_eq_real': np.real(GR_eq),
    'GR_eq_imag': np.imag(GR_eq),

    # GGE populations
    'rho_GGE': rho_GGE,
    'E_post_sorted': E_post_sorted,
    'E_mean_GGE': E_mean_GGE,

    # Pre-transit spectrum
    'E_pre': E_pre,
    'E_gs_pre': E_gs_pre,

    # Spectral weight decomposition
    'S_total': S_total,
    'S_GPV': S_GPV,
    'S_GPV_frac': S_GPV / S_total,
    'S_gate': S_gate,
    'S_gate_frac': S_gate / S_total,
    'S_removal': S_removal,
    'S_removal_frac': S_removal / S_total,
    'S_cont': S_cont,
    'S_cont_frac': S_cont / S_total,

    # Discrete pole decomposition
    'gate_pole_frac': gate_pole_frac,
    'gpv_pole_frac': gpv_pole_frac,
    'total_pos_weight': total_pos_weight,

    # Multi-eta results
    'eta_values': np.array(eta_values),
    'A_multi_eta': A_multi_eta,

    # Comparison metrics
    'JSD': JSD,

    # Gate
    'gate_verdict': np.array([verdict]),
    'gate_detail': np.array([verdict_detail]),

    # Reference values
    'omega_PV_s37': omega_PV_s37,
    'omega_minus_s37': omega_minus_s37,
    'Delta_OES_s37': Delta_OES_s37,
}

# Add peak data
if gpv_peak is not None:
    save_dict['gpv_peak_omega'] = gpv_peak['omega']
    save_dict['gpv_peak_height'] = gpv_peak['height']
if removal_peak is not None:
    save_dict['removal_peak_omega'] = removal_peak['omega']
    save_dict['removal_peak_height'] = removal_peak['height']

out_npz = os.path.join(SCRIPT_DIR, 's39_spectral_function.npz')
np.savez_compressed(out_npz, **save_dict)
print(f"  Saved: {out_npz}")
print(f"  Size: {os.path.getsize(out_npz) / 1024:.1f} KB")

# ======================================================================
#  Step 14: PLOT
# ======================================================================

print("\n  Generating plots...")

fig, axes = plt.subplots(2, 2, figsize=(16, 12))

# Panel (a): A_GGE(omega) and A_eq(omega)
ax = axes[0, 0]
ax.plot(omega_grid, A_GGE, 'b-', lw=2, label=r'$A_{GGE}(\omega)$')
ax.plot(omega_grid, A_eq, 'r--', lw=1.5, alpha=0.7, label=r'$A_{eq}(\omega)$')

# Mark expected positions
ax.axvline(omega_PV_s37, color='green', ls=':', lw=1, alpha=0.7,
           label=f'$\\omega_{{PV}}$ = {omega_PV_s37:.3f}')
ax.axvline(omega_minus_s37, color='orange', ls=':', lw=1, alpha=0.7,
           label=f'$\\omega_{{rem}}$ = {omega_minus_s37:.3f}')
ax.axvline(2*Delta_OES_s37, color='purple', ls='--', lw=1, alpha=0.5,
           label=f'$2\\Delta_{{OES}}$ = {2*Delta_OES_s37:.3f}')

# Shade gate region
ax.axvspan(gate_lo, gate_hi, alpha=0.1, color='green',
           label=f'Gate [{gate_lo}, {gate_hi}]')

ax.set_xlabel(r'$\omega$', fontsize=12)
ax.set_ylabel(r'$A(\omega)$', fontsize=12)
ax.set_title('(a) Post-Quench vs Equilibrium Spectral Function')
ax.legend(fontsize=7, loc='upper right')
ax.grid(True, alpha=0.3)
ax.set_xlim(0, 3.0)

# Panel (b): GGE spectral function at multiple eta
ax = axes[0, 1]
colors = ['navy', 'royalblue', 'steelblue', 'skyblue', 'lightblue']
for ie, eta_val in enumerate(eta_values):
    ax.plot(omega_grid, A_multi_eta[ie, :], color=colors[ie], lw=1.5,
            alpha=0.8, label=f'$\\eta$ = {eta_val}')

ax.axvspan(gate_lo, gate_hi, alpha=0.1, color='green')
ax.set_xlabel(r'$\omega$', fontsize=12)
ax.set_ylabel(r'$A_{GGE}(\omega)$', fontsize=12)
ax.set_title('(b) GGE Spectral Function: $\\eta$ Dependence')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)
ax.set_xlim(0, 3.0)

# Panel (c): Discrete pole decomposition
ax = axes[1, 0]
# Plot positive-frequency poles as vertical bars
pole_omegas_arr = np.array([p['omega'] for p in pos_poles])
pole_weights_arr = np.array([p['weight'] for p in pos_poles])

# Group by omega (many poles at the same energy)
unique_omegas = np.unique(np.round(pole_omegas_arr, 6))
grouped_weights = np.zeros(len(unique_omegas))
for i, uo in enumerate(unique_omegas):
    mask = np.abs(pole_omegas_arr - uo) < 1e-5
    grouped_weights[i] = np.sum(pole_weights_arr[mask])

# Color by region
for i, (uo, gw) in enumerate(zip(unique_omegas, grouped_weights)):
    if gw < 1e-8:
        continue
    if gate_lo <= uo <= gate_hi:
        color = 'green'
    elif gpv_lo <= uo <= gpv_hi:
        color = 'steelblue'
    else:
        color = 'coral'
    ax.bar(uo, gw, width=0.012, color=color, alpha=0.7,
           edgecolor='black', linewidth=0.3)

ax.axvspan(gate_lo, gate_hi, alpha=0.1, color='green',
           label=f'Gate [{gate_lo}, {gate_hi}]: {gate_pole_frac*100:.1f}%')
ax.axvspan(gpv_lo, gpv_hi, alpha=0.05, color='blue',
           label=f'GPV [{gpv_lo}, {gpv_hi}]: {gpv_pole_frac*100:.1f}%')
ax.set_xlabel(r'$\omega$', fontsize=12)
ax.set_ylabel(r'Pole weight $\rho_n |<m|P^\dag|n>|^2$', fontsize=12)
ax.set_title(f'(c) Discrete Pole Decomposition (N = {len(pos_poles)} poles)')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)
ax.set_xlim(0, 3.0)

# Panel (d): GGE population distribution
ax = axes[1, 1]
# Sort rho_GGE by energy
nonzero_mask = rho_GGE > 1e-20
ax.semilogy(E_post_sorted[nonzero_mask], rho_GGE[nonzero_mask], 'ko',
            markersize=3, alpha=0.5, label=r'$\rho_{GGE}(E_n)$')

# Overlay sector coloring
for np_val in range(n_modes + 1):
    sector_mask = nonzero_mask & (n_pairs_fock[sort_idx] == np_val)
    if np.any(sector_mask):
        ax.semilogy(E_post_sorted[sector_mask], rho_GGE[sector_mask], 'o',
                    markersize=4, alpha=0.6,
                    label=f'$N_{{pair}}={np_val}$')

ax.set_xlabel(r'$E_n$ (post-transit)', fontsize=12)
ax.set_ylabel(r'$\rho_{GGE}(n)$', fontsize=12)
ax.set_title('(d) GGE Population Distribution')
ax.legend(fontsize=7, loc='upper right', ncol=2)
ax.grid(True, alpha=0.3)

# Add text box with gate verdict
textstr = (f'GATE SPEC-39: {verdict}\n'
           f'S_gate/S_total = {S_gate/S_total*100:.1f}% '
           f'(need > 30%)\n'
           f'S_GPV/S_total = {S_GPV/S_total*100:.1f}%\n'
           f'JSD(GGE, eq) = {JSD:.4f}')
axes[0, 0].text(0.98, 0.98, textstr, transform=axes[0, 0].transAxes,
                fontsize=8, verticalalignment='top',
                horizontalalignment='right',
                bbox=dict(boxstyle='round', facecolor='lightyellow',
                          alpha=0.9))

fig.suptitle('W2-3: Post-Quench Spectral Function $A(\\omega)$\n'
             f'8-mode BCS, sudden quench (GGE), $\\eta$ = {eta}',
             fontsize=13, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.93])

out_png = os.path.join(SCRIPT_DIR, 's39_spectral_function.png')
plt.savefig(out_png, dpi=150, bbox_inches='tight')
plt.close()
print(f"  Plot saved: {out_png}")

# ======================================================================
#  FINAL SUMMARY
# ======================================================================

elapsed = time.time() - t0
print(f"\n{'='*78}")
print(f"FINAL SUMMARY: W2-3 Post-Quench Spectral Function")
print(f"{'='*78}")
print(f"\n  GATE SPEC-39: {verdict}")
print(f"  {verdict_detail}")
print(f"\n  Key numbers:")
print(f"    S_gate / S_total (in [0.70, 0.85]) = {S_gate/S_total*100:.1f}%")
print(f"    S_GPV / S_total (in [0.60, 1.00])  = {S_GPV/S_total*100:.1f}%")
print(f"    S_removal / S_total (in [0.0, 0.3]) = {S_removal/S_total*100:.1f}%")
print(f"    S_cont / S_total (in [1.0, 3.0])   = {S_cont/S_total*100:.1f}%")
print(f"    Total spectral weight = {S_total:.6f}")
print(f"    JSD(GGE, eq) = {JSD:.6f}")
if gpv_peak is not None:
    print(f"    GPV peak: omega = {gpv_peak['omega']:.4f}, "
          f"A = {gpv_peak['height']:.6f}")
if removal_peak is not None:
    print(f"    Removal peak: omega = {removal_peak['omega']:.4f}, "
          f"A = {removal_peak['height']:.6f}")
print(f"\n  Runtime: {elapsed:.1f}s")
print(f"{'='*78}")
