#!/usr/bin/env python3
"""
LEGGETT-GGE-49: Leggett relative-phase correlator in the GGE
=============================================================

Gate: LEGGETT-GGE-49
  PASS: C_L(t) oscillates AND phi_rel independent of 8 I_alpha
  INFO: damped oscillations or phi_rel dependent
  FAIL: C_L(t) decays monotonically

Method:
  1. Construct full 256-state Fock space for 8 modes (4 B2 + 1 B1 + 3 B3)
  2. Build BCS Hamiltonian H_BCS with pairing interaction V_phys
  3. Construct GGE density matrix rho_GGE = exp(-sum beta_alpha I_alpha) / Z
     where I_alpha = n_alpha (Richardson-Gaudin integrals for integrable BCS)
  4. Define Leggett relative-phase operator phi_rel = phi_B3 - phi_B2
     In second quantization: phi_rel ~ (pair creation in B3, pair annihilation in B2) - h.c.
  5. Compute C_L(t) = Tr[rho_GGE phi_rel(t) phi_rel(0)]
  6. Test whether phi_rel commutes with (or is a function of) the 8 I_alpha

Nuclear benchmark: pair-transfer strength above T_c in ^158Er
  Above T_c, nuclear pair vibrations survive as enhanced pair-transfer fluctuations
  (Broglia-Mottelson-Bes effect). The question: does the same happen here?

Author: Nazarewicz agent (S49 W1-T)
"""

import sys
sys.path.insert(0, '.')
import numpy as np
from scipy.linalg import expm
from canonical_constants import (
    E_cond, E_cond_ED_8mode, N_dof_BCS, Delta_B3,
    omega_PV, xi_BCS, tau_fold, n_pairs, P_exc_kz,
    E_B1, E_B2_mean, E_B3_mean, rho_B2_per_mode
)

# ==============================================================================
#  Section 1: Load upstream data
# ==============================================================================

otoc = np.load('tier0-computation/s38_otoc_bcs.npz', allow_pickle=True)
leggett = np.load('tier0-computation/s48_leggett_mode.npz', allow_pickle=True)
kz = np.load('tier0-computation/s38_kz_defects.npz', allow_pickle=True)

E_8 = otoc['E_8']        # 8 mode energies (M_KK units)
V_phys = otoc['V_phys']  # 8x8 pairing interaction
rho_8 = otoc['rho_8']    # 8 DOS values
mu = float(otoc['mu'])    # chemical potential (= 0)
n_modes = int(otoc['n_modes'])  # = 8
dim = int(otoc['dim'])    # = 256 Fock states

# Sector assignments: modes 0-3 = B2, mode 4 = B1, modes 5-7 = B3
sector_B2 = [0, 1, 2, 3]
sector_B1 = [4]
sector_B3 = [5, 6, 7]

print("=" * 78)
print("LEGGETT-GGE-49: Leggett Correlator in the Generalized Gibbs Ensemble")
print("=" * 78)
print(f"\nUpstream: E_8 = {E_8}")
print(f"Upstream: mu = {mu}")
print(f"Upstream: P_exc = {P_exc_kz}")
print(f"Upstream: n_Bog pairs = {n_pairs}")
print(f"Sector assignment: B2={sector_B2}, B1={sector_B1}, B3={sector_B3}")

# ==============================================================================
#  Section 2: Build Fock space operators
# ==============================================================================

# Fock basis: |n_0, n_1, ..., n_7> where n_i in {0, 1}
# State index: i = sum(n_k * 2^k)

def fock_state(dim_fock, n_modes_f):
    """Return occupation number array for each Fock state."""
    states = np.zeros((dim_fock, n_modes_f), dtype=int)
    for i in range(dim_fock):
        for k in range(n_modes_f):
            states[i, k] = (i >> k) & 1
    return states

fock = fock_state(dim, n_modes)

# Creation and annihilation operators in Fock space
def creation_op(mode, n_modes_f, dim_fock):
    """c^dag_mode in Fock space."""
    op = np.zeros((dim_fock, dim_fock))
    for i in range(dim_fock):
        occ = [(i >> k) & 1 for k in range(n_modes_f)]
        if occ[mode] == 0:
            new_occ = list(occ)
            new_occ[mode] = 1
            j = sum(new_occ[k] * (1 << k) for k in range(n_modes_f))
            # Fermionic sign: count occupied states below 'mode'
            sign = (-1) ** sum(occ[k] for k in range(mode))
            op[j, i] = sign
    return op

print("\nBuilding Fock-space operators...")
c_dag = [creation_op(m, n_modes, dim) for m in range(n_modes)]
c_ann = [cd.T.copy() for cd in c_dag]
n_op = [c_dag[m] @ c_ann[m] for m in range(n_modes)]

# Number operator
N_total = sum(n_op)

# Verify: anti-commutation relations
print("Anti-commutation check: {c_i^dag, c_j} = delta_ij")
max_err = 0
for i in range(n_modes):
    for j in range(n_modes):
        ac = c_dag[i] @ c_ann[j] + c_ann[j] @ c_dag[i]
        expected = np.eye(dim) if i == j else np.zeros((dim, dim))
        max_err = max(max_err, np.max(np.abs(ac - expected)))
print(f"  Max error: {max_err:.2e}")

# ==============================================================================
#  Section 3: Build BCS Hamiltonian
# ==============================================================================

# H = sum_k (e_k - mu) n_k - sum_{k,k'} V_{kk'} c^dag_k c^dag_kbar c_kbar' c_k'
# For our system: modes come in pairs implicitly through the V matrix
# Following S38: H_BCS = sum_k epsilon_k n_k - (1/2) sum_{kk'} V_{kk'} n_k n_k'
# (simplified for the 0D paired system where pairing acts in occupation-number space)

# Actually, the proper BCS Hamiltonian for this system uses the REDUCED BCS form:
# H = sum_k e_k n_k - sum_{k<k'} V_{kk'} (c^dag_k c^dag_k')(c_k' c_k)
# But in the 8-mode system, each "mode" IS a pair level, and the interaction
# is between pair levels. Following S38 OTOC construction:

print("\nBuilding H_BCS...")

# Single-particle part
H_sp = np.zeros((dim, dim))
for k in range(n_modes):
    H_sp += (E_8[k] - mu) * n_op[k]

# Interaction part: -V_{kk'} n_k n_k' (density-density from S38)
# This is the form used in s38_otoc_bcs.py for the 256-state Fock space
H_int = np.zeros((dim, dim))
for k in range(n_modes):
    for kp in range(n_modes):
        if k != kp:
            H_int -= 0.5 * V_phys[k, kp] * n_op[k] @ n_op[kp]

H_BCS = H_sp + H_int

# Diagonalize
evals_H, evecs_H = np.linalg.eigh(H_BCS)
print(f"H_BCS eigenvalues: min={evals_H[0]:.6f}, max={evals_H[-1]:.6f}")
print(f"Ground state energy: {evals_H[0]:.6f}")

# Verify ground state particle number
gs_vec = evecs_H[:, 0]
N_gs = gs_vec @ N_total @ gs_vec
print(f"Ground state <N>: {N_gs:.6f}")

# ==============================================================================
#  Section 4: Build GGE density matrix
# ==============================================================================
# The GGE for an integrable system is:
#   rho_GGE = exp(-sum_alpha beta_alpha I_alpha) / Z
# For the Richardson-Gaudin integrable BCS, the conserved quantities are
# the quasiparticle occupation numbers I_alpha = n_alpha (in the Bogoliubov basis).
# Post-transit (P_exc = 1): ALL quasiparticles excited, so <I_alpha> = 1 for all alpha.
#
# In practice, we need to find the Bogoliubov transformation that diagonalizes H_BCS.
# The eigenstates of H_BCS in the Fock basis give us the many-body spectrum.
# The GGE is constructed from the constraint that <n_alpha> = n_alpha^{post-transit}.

# For P_exc = 1: every Bogoliubov quasiparticle is excited.
# The GGE density matrix in the ENERGY eigenbasis:
# In the fully-excited state, the quasiparticle occupations are all 1.
# The BCS ground state has n_alpha = 0 for all alpha.
# P_exc = 1 means the post-transit state is the "fully excited" state:
# all quasiparticle modes occupied.

# For Richardson-Gaudin integrability with 8 modes, the conserved quantities
# in the diagonal basis are the 8 quasiparticle number operators.
# The GGE with <n_alpha> = n_alpha^{post} determines beta_alpha.

# With P_exc = 1, the post-transit state has EVERY quasiparticle excited.
# In nuclear BCS: this is like the compound nucleus at very high excitation.
# The GGE then thermalizes WITHIN the constraints of the 8 conserved quantities.

# KEY INSIGHT: In the 8-mode system with N=1 (canonical), the Fock space
# decomposes into N-particle sectors. The N=1 sector has 8 states.
# The GGE density matrix must respect particle number conservation.

# Let's work in the FULL 256-dimensional Fock space and project to fixed N sectors.

# First: identify the BCS ground state and the "fully excited" post-transit state
print("\n--- GGE Construction ---")

# The S38 result: n_Bog = 0.999 per mode. ALL modes excited.
# In the 8-mode BCS language: the post-transit state has all pair levels occupied.
# For canonical N=1: the ground state IS the BCS ground state in the N=1 sector.

# Approach: construct GGE from EXACT diagonalization.
# The 8 conserved quantities I_alpha are the occupation numbers of the 8
# ENERGY EIGENMODES in each N-sector.

# For N=1 sector: 8 states. Energy eigenvalues give 8 levels.
# For the GGE, we need the post-transit DISTRIBUTION over these 8 states.

# N=1 sector extraction
N1_mask = np.array([bin(i).count('1') == 1 for i in range(dim)])
N1_indices = np.where(N1_mask)[0]
print(f"N=1 sector: {len(N1_indices)} states")

# H_BCS restricted to N=1
H_N1 = np.zeros((len(N1_indices), len(N1_indices)))
for i, ii in enumerate(N1_indices):
    for j, jj in enumerate(N1_indices):
        H_N1[i, j] = H_BCS[ii, jj]

evals_N1, evecs_N1 = np.linalg.eigh(H_N1)
print(f"N=1 eigenvalues: {evals_N1}")

# For N=2 sector (relevant for pair correlations)
N2_mask = np.array([bin(i).count('1') == 2 for i in range(dim)])
N2_indices = np.where(N2_mask)[0]
print(f"N=2 sector: {len(N2_indices)} states (C(8,2)=28)")

H_N2 = np.zeros((len(N2_indices), len(N2_indices)))
for i, ii in enumerate(N2_indices):
    for j, jj in enumerate(N2_indices):
        H_N2[i, j] = H_BCS[ii, jj]

evals_N2, evecs_N2 = np.linalg.eigh(H_N2)
print(f"N=2 eigenvalues: min={evals_N2[0]:.6f}, max={evals_N2[-1]:.6f}")

# N=0 sector (vacuum)
N0_mask = np.array([bin(i).count('1') == 0 for i in range(dim)])
N0_indices = np.where(N0_mask)[0]
print(f"N=0 sector: {len(N0_indices)} state (vacuum)")

# Post-transit GGE: All Bogoliubov quasiparticles excited.
# In the canonical N=1 sector, the post-transit state is the THERMAL state
# at the microcanonical temperature T_compound = E_exc/N_dof.
# But the GGE is NOT thermal -- it retains memory of the initial state
# through 8 conserved quantities.

# The Landau approach: the GGE preserves ALL I_alpha independently.
# For the N=1 sector with 8 states, the 8 "conserved quantities" are
# the projectors |E_alpha><E_alpha| onto the energy eigenstates.
# The GGE with constraints <|E_alpha><E_alpha|> = p_alpha gives
# rho_GGE = sum_alpha p_alpha |E_alpha><E_alpha|.

# S38 result: P_exc = 1, n_Bog = 0.999 per mode.
# This means the post-transit state is the MAXIMALLY MIXED state
# in the N=1 sector: p_alpha = 1/8 for all alpha.
# (Infinite temperature GGE -- all beta_alpha = 0.)

# ACTUALLY: P_exc = 1 means the BCS condensate is destroyed.
# In the grand canonical picture, the post-transit state populates ALL
# Fock-space sectors. But in canonical N=1, the maximally excited state
# is the one with the HIGHEST energy eigenstate occupied.
# The GGE retains the information about WHICH modes were excited.

# For a more nuanced treatment: the S38 Bogoliubov transformation gives
# n_k = v_k^2 (ground state) -> 1 - v_k^2 = u_k^2 (fully excited).
# In the N=1 sector, this maps to specific occupation probabilities.

# The BCS ground state in terms of energy eigenstates of H_N1:
# |BCS, N=1> = sum_alpha c_alpha |E_alpha>
# The fully excited state (all quasiparticles flipped) maps to:
# |excited, N=1> = sum_alpha d_alpha |E_alpha>
# where d_alpha depend on the Bogoliubov transformation.

# For our purposes: construct the GGE as the MICROCANONICAL ensemble
# at E = E_exc, constrained by the 8 I_alpha values.
# Since P_exc = 1 and N=1, the simplest GGE is the EQUAL-WEIGHT mixture
# over all N=1 states (maximum entropy subject to fixed N=1).
# This is the infinite-temperature Gibbs ensemble projected to N=1.

# Cross-check: Gibbs thermal state at T_compound in N=1 sector
T_compound = float(E_cond_ED_8mode) * (-1) * 443.0 / 8  # E_exc / N_dof
print(f"\nT_compound = {T_compound:.4f} M_KK")

# Gibbs weights in N=1
boltz_N1 = np.exp(-evals_N1 / T_compound)
Z_N1 = np.sum(boltz_N1)
p_gibbs_N1 = boltz_N1 / Z_N1
print(f"Gibbs weights (N=1): {p_gibbs_N1}")
print(f"Max/min weight ratio: {p_gibbs_N1.max()/p_gibbs_N1.min():.6f}")

# GGE weights: for P_exc = 1 (all quasiparticles excited),
# the GGE in the N=1 sector is UNIFORM (beta_alpha = 0 for all alpha)
p_gge_N1 = np.ones(len(evals_N1)) / len(evals_N1)
print(f"GGE weights (uniform): {p_gge_N1}")

# The Gibbs and GGE are nearly identical because T_compound >> bandwidth(N=1)
bw_N1 = evals_N1.max() - evals_N1.min()
print(f"N=1 bandwidth: {bw_N1:.6f}")
print(f"T_compound / bandwidth: {T_compound / bw_N1:.2f}")
print(f"  (>> 1 confirms GGE ~ uniform ~ infinite-T Gibbs)")

# Construct GGE density matrix in N=1 sector
rho_gge_N1 = np.zeros((len(N1_indices), len(N1_indices)))
for alpha in range(len(evals_N1)):
    v = evecs_N1[:, alpha]
    rho_gge_N1 += p_gge_N1[alpha] * np.outer(v, v)

# Verify: Tr[rho] = 1
print(f"Tr[rho_GGE] = {np.trace(rho_gge_N1):.10f}")

# Promote to full 256-dim Fock space
rho_gge_full = np.zeros((dim, dim))
for i, ii in enumerate(N1_indices):
    for j, jj in enumerate(N1_indices):
        rho_gge_full[ii, jj] = rho_gge_N1[i, j]

# ==============================================================================
#  Section 5: Define Leggett phase operator
# ==============================================================================
# The Leggett relative phase measures the phase difference between sector
# order parameters. In second quantization:
#   phi_rel ~ i * (P^dag_{B3} P_{B2} - P^dag_{B2} P_{B3})
# where P^dag_sector = sum_{k in sector} c^dag_k creates a particle in that sector.
#
# More precisely, the Leggett mode probes the PAIR TRANSFER between sectors.
# The pair-transfer operator from B2 to B3:
#   T_{B2->B3} = sum_{k in B3, k' in B2} c^dag_k c_{k'}
# The relative phase correlator is:
#   C_L(t) = <T^dag(t) T(0)> in the GGE
#
# For our N=1 system: pair transfer moves the single particle between sectors.
# This IS the relevant Leggett-type correlator at N=1.

print("\n--- Leggett Phase Operator ---")

# Sector pair-transfer operators
# T_{B2->B3} = sum_{k in B3} sum_{k' in B2} c^dag_k c_{k'}
T_B2_to_B3 = np.zeros((dim, dim))
for k in sector_B3:
    for kp in sector_B2:
        T_B2_to_B3 += c_dag[k] @ c_ann[kp]

T_B3_to_B2 = T_B2_to_B3.T.copy()  # Hermitian conjugate

# Leggett phase operator: phi_rel ~ i(T_{B2->B3} - T_{B3->B2})
# This is anti-Hermitian; multiply by i to get Hermitian
phi_rel = 1j * (T_B2_to_B3 - T_B3_to_B2)
# Make sure it's Hermitian
assert np.allclose(phi_rel, phi_rel.conj().T, atol=1e-14), "phi_rel not Hermitian"

# Also define the Hermitian "amplitude" operator
A_rel = T_B2_to_B3 + T_B3_to_B2

# And the full inter-sector transfer operators for all pairs
T_B1_to_B2 = np.zeros((dim, dim))
for k in sector_B2:
    for kp in sector_B1:
        T_B1_to_B2 += c_dag[k] @ c_ann[kp]

T_B1_to_B3 = np.zeros((dim, dim))
for k in sector_B3:
    for kp in sector_B1:
        T_B1_to_B3 += c_dag[k] @ c_ann[kp]

# Leggett mode eigenvectors from S48:
# L1: B3 vs (B1+B2) — mainly J_23
# L2: B1 vs B2 — mainly J_12
# So phi_L1 ~ phi_B3 - (phi_B1 + phi_B2)/2
# In transfer operators: T_{(B1+B2)->B3}

# Sector number operators
N_B2 = sum(n_op[k] for k in sector_B2)
N_B1 = sum(n_op[k] for k in sector_B1)
N_B3 = sum(n_op[k] for k in sector_B3)

# Check sector occupations in GGE
occ_B2_gge = np.trace(rho_gge_full @ N_B2).real
occ_B1_gge = np.trace(rho_gge_full @ N_B1).real
occ_B3_gge = np.trace(rho_gge_full @ N_B3).real
print(f"GGE sector occupations: B2={occ_B2_gge:.4f}, B1={occ_B1_gge:.4f}, B3={occ_B3_gge:.4f}")
print(f"  (Expected: B2=4/8=0.5, B1=1/8=0.125, B3=3/8=0.375)")
print(f"  (Sum = {occ_B2_gge + occ_B1_gge + occ_B3_gge:.6f})")

# ==============================================================================
#  Section 6: Compute C_L(t) in the GGE
# ==============================================================================
# C_L(t) = Tr[rho_GGE phi_rel(t) phi_rel(0)]
#         = Tr[rho_GGE e^{iHt} phi_rel e^{-iHt} phi_rel]
#
# In the energy eigenbasis:
# C_L(t) = sum_{mn} rho_mm <m|phi_rel|n> <n|phi_rel|m> e^{i(E_m-E_n)t}
#
# This is the SPECTRAL DECOMPOSITION of the correlator.

print("\n--- Computing C_L(t) spectral decomposition ---")

# phi_rel matrix elements in N=1 energy eigenbasis
# phi_rel restricted to N=1 sector
phi_N1 = np.zeros((len(N1_indices), len(N1_indices)), dtype=complex)
for i, ii in enumerate(N1_indices):
    for j, jj in enumerate(N1_indices):
        phi_N1[i, j] = phi_rel[ii, jj]

# Transform to energy eigenbasis
phi_N1_eig = evecs_N1.T @ phi_N1 @ evecs_N1
print(f"phi_rel in energy eigenbasis (first 4x4 magnitude):")
print(np.abs(phi_N1_eig[:4, :4]))

# Same for amplitude operator
A_N1 = np.zeros((len(N1_indices), len(N1_indices)), dtype=complex)
for i, ii in enumerate(N1_indices):
    for j, jj in enumerate(N1_indices):
        A_N1[i, j] = A_rel[ii, jj]

A_N1_eig = evecs_N1.T @ A_N1 @ evecs_N1

# Spectral function: S(omega) = sum_{m,n} p_m |<m|phi_rel|n>|^2 delta(omega - (E_n - E_m))
# Collect all transitions
transitions = []
for m in range(len(evals_N1)):
    for n in range(len(evals_N1)):
        omega_mn = evals_N1[n] - evals_N1[m]
        weight = p_gge_N1[m] * np.abs(phi_N1_eig[m, n])**2
        if weight > 1e-15:
            transitions.append((omega_mn, weight))

transitions.sort(key=lambda x: x[0])
print(f"\nSpectral transitions (phi_rel): {len(transitions)} non-zero")
print(f"{'omega':>12s} {'weight':>12s}")
for omega, w in transitions:
    if w > 1e-6:
        print(f"  {omega:12.6f} {w:12.8f}")

# Identify unique frequencies
omega_unique = {}
for omega, w in transitions:
    key = round(omega, 8)
    omega_unique[key] = omega_unique.get(key, 0) + w

print(f"\nUnique transition frequencies: {len(omega_unique)}")
for om, w in sorted(omega_unique.items(), key=lambda x: abs(x[0])):
    if w > 1e-6:
        print(f"  omega = {om:12.6f}, total weight = {w:12.8f}")

# C_L(t) = sum over transitions
t_max = 200.0  # M_KK^{-1}
n_t = 4000
t_array = np.linspace(0, t_max, n_t)

# Compute C_L(t) directly from spectral decomposition
C_L = np.zeros(n_t, dtype=complex)
for omega, w in transitions:
    C_L += w * np.exp(1j * omega * t_array)

# Also compute the amplitude correlator
transitions_A = []
for m in range(len(evals_N1)):
    for n in range(len(evals_N1)):
        omega_mn = evals_N1[n] - evals_N1[m]
        weight = p_gge_N1[m] * np.abs(A_N1_eig[m, n])**2
        if weight > 1e-15:
            transitions_A.append((omega_mn, weight))

C_A = np.zeros(n_t, dtype=complex)
for omega, w in transitions_A:
    C_A += w * np.exp(1j * omega * t_array)

print(f"\nC_L(0) = {C_L[0].real:.8f} (equal-time correlator)")
print(f"C_A(0) = {C_A[0].real:.8f}")

# ==============================================================================
#  Section 7: Analyze oscillatory structure
# ==============================================================================
print("\n--- Oscillatory Structure Analysis ---")

# Check if C_L(t) oscillates or decays monotonically
C_L_real = C_L.real
C_L_env = np.abs(C_L)

# Find zero crossings
crossings = []
for i in range(len(C_L_real) - 1):
    if C_L_real[i] * C_L_real[i+1] < 0:
        # Linear interpolation
        t_cross = t_array[i] + (t_array[i+1] - t_array[i]) * abs(C_L_real[i]) / (abs(C_L_real[i]) + abs(C_L_real[i+1]))
        crossings.append(t_cross)

n_crossings = len(crossings)
print(f"Zero crossings in [0, {t_max}]: {n_crossings}")

if n_crossings >= 2:
    periods = np.diff(crossings[:20])  # First 20 half-periods
    if len(periods) > 0:
        mean_half_period = np.mean(periods)
        omega_osc = np.pi / mean_half_period
        print(f"Mean half-period: {mean_half_period:.4f} M_KK^{{-1}}")
        print(f"Oscillation frequency: {omega_osc:.6f} M_KK")
        print(f"Compare omega_L1 = {float(leggett['omega_L1_fold']):.6f} M_KK")

# Envelope analysis: does |C_L| decay?
# Sample at quarter-periods
if n_crossings >= 4:
    peak_times = []
    peak_vals = []
    for i in range(len(crossings) - 1):
        t_mid = (crossings[i] + crossings[i+1]) / 2
        idx = np.argmin(np.abs(t_array - t_mid))
        peak_times.append(t_mid)
        peak_vals.append(np.abs(C_L_real[idx]))

    if len(peak_vals) >= 4:
        # Check monotonic decay
        is_decaying = all(peak_vals[i] >= peak_vals[i+1] * 0.95
                          for i in range(min(10, len(peak_vals)-1)))
        # Check oscillation persistence
        persistence = peak_vals[-1] / peak_vals[0] if peak_vals[0] > 0 else 0
        print(f"First peak: {peak_vals[0]:.8f}")
        print(f"Last peak: {peak_vals[-1]:.8f}")
        print(f"Persistence ratio: {persistence:.6f}")
        print(f"Monotonic decay: {is_decaying}")

# FFT for spectral analysis
from scipy.fft import fft, fftfreq
C_L_fft = fft(C_L_real)
freqs = fftfreq(n_t, d=(t_array[1] - t_array[0]))
power = np.abs(C_L_fft)**2
# Only positive frequencies
pos_mask = freqs > 0
freqs_pos = freqs[pos_mask]
power_pos = power[pos_mask]

# Find dominant peaks
peak_indices = []
for i in range(1, len(power_pos) - 1):
    if power_pos[i] > power_pos[i-1] and power_pos[i] > power_pos[i+1]:
        if power_pos[i] > 0.01 * power_pos.max():
            peak_indices.append(i)

print(f"\nFFT peaks (>1% of max):")
for idx in sorted(peak_indices, key=lambda i: power_pos[i], reverse=True)[:10]:
    omega_peak = 2 * np.pi * freqs_pos[idx]
    print(f"  omega = {omega_peak:.6f}, power = {power_pos[idx]:.4e}")

# ==============================================================================
#  Section 8: Test phi_rel independence from I_alpha
# ==============================================================================
print("\n--- Independence Test: phi_rel vs I_alpha ---")

# The 8 Richardson-Gaudin conserved quantities in the N=1 sector are
# the 8 projectors |E_alpha><E_alpha| (since H is diagonal in its own basis).
# phi_rel is independent if it does NOT commute with these projectors.
# Equivalently: phi_rel has off-diagonal elements in the energy eigenbasis.

off_diag_norm = 0
diag_norm = 0
for m in range(len(evals_N1)):
    for n in range(len(evals_N1)):
        val = np.abs(phi_N1_eig[m, n])**2
        if m == n:
            diag_norm += val
        else:
            off_diag_norm += val

total_norm = diag_norm + off_diag_norm
off_diag_frac = off_diag_norm / total_norm if total_norm > 0 else 0
print(f"phi_rel: diagonal norm = {diag_norm:.8f}")
print(f"phi_rel: off-diagonal norm = {off_diag_norm:.8f}")
print(f"phi_rel: off-diagonal fraction = {off_diag_frac:.6f}")

# Commutator [H, phi_rel] in N=1 sector
comm_H_phi = H_N1 @ phi_N1 - phi_N1 @ H_N1
comm_norm = np.linalg.norm(comm_H_phi) / np.linalg.norm(phi_N1) if np.linalg.norm(phi_N1) > 0 else 0
print(f"||[H, phi_rel]|| / ||phi_rel|| = {comm_norm:.8f}")

# If [H, phi_rel] = 0, phi_rel is a function of the I_alpha (DEPENDENT)
# If [H, phi_rel] != 0, phi_rel carries independent information (INDEPENDENT)
phi_rel_independent = comm_norm > 0.01
print(f"phi_rel INDEPENDENT of I_alpha: {phi_rel_independent}")

# Also check: is phi_rel diagonal in the energy eigenbasis?
phi_is_diagonal = off_diag_frac < 0.01
print(f"phi_rel is diagonal in eigenbasis: {phi_is_diagonal}")

# ==============================================================================
#  Section 9: Nuclear benchmark — pair-transfer strength above T_c
# ==============================================================================
print("\n--- Nuclear Benchmark: Pair-Transfer Strength Above T_c ---")

# In nuclear physics (Broglia-Mottelson-Bes, 1976):
# The pair-addition strength function S+(omega) = sum_n |<n|P+|0>|^2 delta(omega - E_n + E_0)
# shows a COLLECTIVE peak (Giant Pair Vibration) even above T_c.
# This is because pair fluctuations enhance the two-particle transfer cross section.
#
# Nuclear benchmark: ^158Er at T_c ~ 0.7 MeV
# Below T_c: pair vibration at omega_PV ~ 2*Delta ~ 1.4 MeV (BCS coherent)
# Above T_c: pair-transfer strength REDISTRIBUTED but not zero
# Enhancement factor: sigma(T>T_c) / sigma(uncorrelated) ~ 2-5x
#
# Paper 08 (Nazarewicz, high-spin): pairing collapses at omega_c.
# Above omega_c: no gap, but correlations visible in moments of inertia.
# Paper 03 (HFB formalism): gradual superfluid transition, gap maximal at f~0.5.

# Compute pair-transfer strength in the GGE (above "T_c")
# P+ = sum_{k in B2, k' in B3} c^dag_k c^dag_{k'} (pair addition, B2-B3)
# For N=1 -> N=2 transitions (pair addition to N=2 sector)

# But wait: in canonical N=1, pair ADDITION goes to N=2.
# Pair REMOVAL goes to N=0 (vacuum).
# The correlator C_L(t) within N=1 probes INTRA-sector pair transfer
# (one particle moves between sectors, not pair creation/annihilation).

# The true NUCLEAR analog is the pair-transfer strength:
# S(omega) = sum_f |<f|T_{B2->B3}|i>|^2 delta(omega - E_f + E_i)
# averaged over the GGE ensemble for |i>.

# This IS what we computed above as the spectral decomposition of C_L(t).
# The pair-transfer strength is:
S_pair = {}
for m in range(len(evals_N1)):
    for n in range(len(evals_N1)):
        omega_mn = evals_N1[n] - evals_N1[m]
        # Use amplitude operator A_rel (Hermitian part of transfer)
        weight = p_gge_N1[m] * np.abs(A_N1_eig[m, n])**2
        if weight > 1e-15:
            key = round(omega_mn, 8)
            S_pair[key] = S_pair.get(key, 0) + weight

print("Pair-transfer spectral function S(omega) in GGE:")
total_strength = sum(S_pair.values())
print(f"  Total strength: {total_strength:.8f}")
for om, s in sorted(S_pair.items()):
    if s > 1e-4 * total_strength:
        print(f"  omega = {om:10.6f}, S(omega) = {s:12.8f} ({100*s/total_strength:5.1f}%)")

# Uncorrelated (single-particle) strength for comparison
# If there were no interaction, the transfer matrix elements would be just
# the overlap integrals. Compute in the NON-INTERACTING basis.
H_free = np.zeros((dim, dim))
for k in range(n_modes):
    H_free += E_8[k] * n_op[k]

H_free_N1 = np.zeros((len(N1_indices), len(N1_indices)))
for i, ii in enumerate(N1_indices):
    for j, jj in enumerate(N1_indices):
        H_free_N1[i, j] = H_free[ii, jj]

evals_free_N1, evecs_free_N1 = np.linalg.eigh(H_free_N1)

# In non-interacting basis, phi_rel matrix elements
phi_free_eig = evecs_free_N1.T @ phi_N1 @ evecs_free_N1
A_free_eig = evecs_free_N1.T @ A_N1 @ evecs_free_N1

S_pair_free = {}
p_free = np.ones(len(evals_free_N1)) / len(evals_free_N1)
for m in range(len(evals_free_N1)):
    for n in range(len(evals_free_N1)):
        omega_mn = evals_free_N1[n] - evals_free_N1[m]
        weight = p_free[m] * np.abs(A_free_eig[m, n])**2
        if weight > 1e-15:
            key = round(omega_mn, 8)
            S_pair_free[key] = S_pair_free.get(key, 0) + weight

total_free = sum(S_pair_free.values())
print(f"\nFree pair-transfer strength: {total_free:.8f}")

# Enhancement factor (Broglia effect)
enhancement = total_strength / total_free if total_free > 0 else float('inf')
print(f"Enhancement factor (interacting/free): {enhancement:.4f}")
print(f"  Nuclear benchmark: 2-5x above T_c (Broglia-Mottelson)")

# ==============================================================================
#  Section 10: Collectivity measure — participation ratio of strength
# ==============================================================================
print("\n--- Collectivity Analysis ---")

# Participation ratio: PR = (sum S_i)^2 / sum S_i^2
# PR = 1: single transition (maximally collective)
# PR = N: N equal transitions (maximally fragmented)
strengths = list(S_pair.values())
pr_gge = (sum(strengths))**2 / sum(s**2 for s in strengths) if strengths else 0

strengths_free = list(S_pair_free.values())
pr_free = (sum(strengths_free))**2 / sum(s**2 for s in strengths_free) if strengths_free else 0

print(f"Participation ratio (interacting GGE): {pr_gge:.2f}")
print(f"Participation ratio (free): {pr_free:.2f}")
print(f"Nuclear comparison: PR ~ 1-3 below T_c (collective), PR ~ N above T_c (fragmented)")

# ==============================================================================
#  Section 11: Direct time-domain verification
# ==============================================================================
print("\n--- Direct time-domain C_L(t) ---")

# Verify the spectral decomposition by direct matrix exponentiation at selected times
t_check_points = [0, 10, 50, 100, 200]
for t_check in t_check_points:
    # e^{iHt} phi_rel e^{-iHt} in N=1 sector
    U = expm(1j * H_N1 * t_check)
    phi_t = U @ phi_N1 @ U.conj().T
    C_direct = np.trace(rho_gge_N1 @ phi_t @ phi_N1)
    # Compare with spectral
    idx_t = np.argmin(np.abs(t_array - t_check))
    C_spectral = C_L[idx_t]
    err = abs(C_direct - C_spectral) / (abs(C_spectral) + 1e-20)
    print(f"  t={t_check:6.1f}: C_direct = {C_direct.real:+.8f}{C_direct.imag:+.8f}i, "
          f"C_spectral = {C_spectral.real:+.8f}{C_spectral.imag:+.8f}i, "
          f"rel_err = {err:.2e}")

# ==============================================================================
#  Section 12: Recurrence and long-time behavior
# ==============================================================================
print("\n--- Long-time Behavior ---")

# For a finite system, C_L(t) is quasiperiodic.
# The recurrence time is T_rec ~ 2*pi / min(|omega_m - omega_n|) for non-degenerate transitions.
omega_diffs = []
for omega1, _ in transitions:
    for omega2, _ in transitions:
        diff = abs(omega1 - omega2)
        if 1e-10 < diff < 10:
            omega_diffs.append(diff)

if omega_diffs:
    min_diff = min(omega_diffs)
    T_rec = 2 * np.pi / min_diff
    print(f"Minimum frequency spacing: {min_diff:.8f} M_KK")
    print(f"Recurrence time: {T_rec:.2f} M_KK^{{-1}}")
else:
    T_rec = float('inf')
    print("No non-degenerate frequency pairs found")

# C_L at long times: time-averaged value
C_L_time_avg = np.mean(C_L_real[n_t//2:])
C_L_fluct_rms = np.std(C_L_real[n_t//2:])
print(f"Time-averaged C_L (second half): {C_L_time_avg:.8f}")
print(f"RMS fluctuation: {C_L_fluct_rms:.8f}")
print(f"Fluctuation / C_L(0): {C_L_fluct_rms / C_L[0].real:.6f}" if C_L[0].real > 1e-15 else "")

# ==============================================================================
#  Section 13: Comparison with Gibbs thermal correlator
# ==============================================================================
print("\n--- GGE vs Gibbs Comparison ---")

# Gibbs correlator at T_compound
C_L_gibbs = np.zeros(n_t, dtype=complex)
phi_gibbs_eig = evecs_N1.T @ phi_N1 @ evecs_N1  # Same as phi_N1_eig
for m in range(len(evals_N1)):
    for n in range(len(evals_N1)):
        omega_mn = evals_N1[n] - evals_N1[m]
        weight = p_gibbs_N1[m] * np.abs(phi_gibbs_eig[m, n])**2
        C_L_gibbs += weight * np.exp(1j * omega_mn * t_array)

deviation = np.max(np.abs(C_L - C_L_gibbs)) / np.max(np.abs(C_L)) if np.max(np.abs(C_L)) > 1e-15 else 0
print(f"Max |C_GGE - C_Gibbs| / max|C_GGE|: {deviation:.8f}")
print(f"  (Small if T_compound >> bandwidth, confirming GGE ~ Gibbs in N=1)")

# ==============================================================================
#  Section 14: The key question — does C_L oscillate?
# ==============================================================================
print("\n" + "=" * 78)
print("GATE ASSESSMENT: LEGGETT-GGE-49")
print("=" * 78)

# Criteria:
# PASS: C_L(t) oscillates AND phi_rel independent of 8 I_alpha
# INFO: damped oscillations or phi_rel dependent
# FAIL: C_L(t) decays monotonically

oscillates = n_crossings >= 4  # At least 2 full oscillations
independent = phi_rel_independent  # [H, phi_rel] != 0

# Check for damping
if n_crossings >= 4:
    # Compare first and last peaks
    if len(peak_vals) >= 4:
        first_peak = np.mean(peak_vals[:3])
        last_peak = np.mean(peak_vals[-3:])
        persistence_ratio = last_peak / first_peak if first_peak > 0 else 0
        undamped = persistence_ratio > 0.5
    else:
        undamped = False
        persistence_ratio = 0
else:
    undamped = False
    persistence_ratio = 0

print(f"\n1. C_L(t) oscillates: {oscillates} ({n_crossings} zero crossings)")
print(f"2. phi_rel independent of I_alpha: {independent} (||[H,phi]||/||phi|| = {comm_norm:.6f})")
print(f"3. Oscillations undamped: {undamped} (persistence = {persistence_ratio:.4f})")
print(f"4. Enhancement over free: {enhancement:.4f}x (nuclear benchmark: 2-5x)")
print(f"5. Participation ratio: {pr_gge:.2f} (GGE) vs {pr_free:.2f} (free)")

if oscillates and independent:
    if undamped:
        verdict = "PASS"
        detail = (f"C_L(t) oscillates with {n_crossings} crossings, persistence {persistence_ratio:.4f}. "
                  f"phi_rel INDEPENDENT (||[H,phi]||/||phi|| = {comm_norm:.4f}). "
                  f"Enhancement {enhancement:.2f}x. Leggett correlations survive in GGE.")
    else:
        verdict = "INFO"
        detail = (f"C_L(t) oscillates ({n_crossings} crossings) but DAMPED (persistence {persistence_ratio:.4f}). "
                  f"phi_rel independent. Nuclear analog: pair fluctuations above T_c (Broglia effect).")
elif oscillates and not independent:
    verdict = "INFO"
    detail = (f"C_L(t) oscillates ({n_crossings} crossings) but phi_rel DEPENDENT on I_alpha "
              f"(||[H,phi]||/||phi|| = {comm_norm:.6f}). Not a 9th integral.")
elif not oscillates:
    verdict = "FAIL"
    detail = f"C_L(t) does NOT oscillate ({n_crossings} crossings). Leggett correlations fully destroyed."

print(f"\nVerdict: {verdict}")
print(f"Detail: {detail}")

# ==============================================================================
#  Section 15: Save results
# ==============================================================================
print("\n--- Saving results ---")

np.savez('tier0-computation/s49_leggett_gge.npz',
    # Gate
    gate_name='LEGGETT-GGE-49',
    gate_verdict=verdict,
    gate_detail=detail,
    # GGE parameters
    p_gge_N1=p_gge_N1,
    p_gibbs_N1=p_gibbs_N1,
    T_compound=T_compound,
    evals_N1=evals_N1,
    evals_N2=evals_N2,
    # Correlator
    t_array=t_array,
    C_L_real=C_L.real,
    C_L_imag=C_L.imag,
    C_L_gibbs_real=C_L_gibbs.real,
    C_A_real=C_A.real,
    # Spectral function
    transitions_omega=np.array([t[0] for t in transitions]),
    transitions_weight=np.array([t[1] for t in transitions]),
    # Independence test
    off_diag_frac=off_diag_frac,
    comm_norm=comm_norm,
    phi_rel_independent=phi_rel_independent,
    # Oscillation analysis
    n_crossings=n_crossings,
    persistence_ratio=persistence_ratio if 'persistence_ratio' in dir() else 0,
    # Nuclear benchmark
    enhancement=enhancement,
    pr_gge=pr_gge,
    pr_free=pr_free,
    total_strength=total_strength,
    total_free_strength=total_free,
    # Recurrence
    T_recurrence=T_rec,
    # GGE vs Gibbs deviation
    gge_gibbs_deviation=deviation,
)

print("Saved: tier0-computation/s49_leggett_gge.npz")

# ==============================================================================
#  Section 16: Plot
# ==============================================================================
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle(f'LEGGETT-GGE-49: Verdict = {verdict}', fontsize=14, fontweight='bold')

# Panel 1: C_L(t) time domain
ax = axes[0, 0]
ax.plot(t_array, C_L.real, 'b-', linewidth=0.8, label='Re C_L(t) [GGE]')
ax.plot(t_array, np.abs(C_L), 'r-', linewidth=0.5, alpha=0.5, label='|C_L(t)|')
if n_crossings > 0:
    ax.axhline(0, color='k', linewidth=0.3)
    for tc in crossings[:20]:
        ax.axvline(tc, color='gray', linewidth=0.2, alpha=0.3)
ax.set_xlabel('t (M_KK^{-1})')
ax.set_ylabel('C_L(t)')
ax.set_title('Leggett correlator in GGE')
ax.legend(fontsize=8)
ax.set_xlim(0, t_max)

# Panel 2: Spectral function
ax = axes[0, 1]
omega_trans = np.array([t[0] for t in transitions])
weight_trans = np.array([t[1] for t in transitions])
ax.stem(omega_trans, weight_trans, linefmt='b-', markerfmt='bo', basefmt='k-')
ax.set_xlabel('omega (M_KK)')
ax.set_ylabel('S(omega)')
ax.set_title('Pair-transfer spectral function')
ax.axvline(float(leggett['omega_L1_fold']), color='r', linestyle='--', alpha=0.5,
           label=f'omega_L1 = {float(leggett["omega_L1_fold"]):.4f}')
ax.legend(fontsize=8)

# Panel 3: FFT power spectrum
ax = axes[1, 0]
omega_fft = 2 * np.pi * freqs_pos
ax.semilogy(omega_fft, power_pos, 'b-', linewidth=0.8)
ax.set_xlabel('omega (M_KK)')
ax.set_ylabel('|FFT|^2')
ax.set_title('FFT power spectrum of C_L(t)')
ax.set_xlim(0, 2.0)
ax.axvline(float(leggett['omega_L1_fold']), color='r', linestyle='--', alpha=0.5,
           label=f'omega_L1 = {float(leggett["omega_L1_fold"]):.4f}')
ax.legend(fontsize=8)

# Panel 4: GGE vs Gibbs comparison
ax = axes[1, 1]
ax.plot(t_array[:500], C_L.real[:500], 'b-', linewidth=1.0, label='C_L [GGE]')
ax.plot(t_array[:500], C_L_gibbs.real[:500], 'r--', linewidth=1.0, label='C_L [Gibbs]')
ax.set_xlabel('t (M_KK^{-1})')
ax.set_ylabel('C_L(t)')
ax.set_title(f'GGE vs Gibbs (dev = {deviation:.2e})')
ax.legend(fontsize=8)

plt.tight_layout()
plt.savefig('tier0-computation/s49_leggett_gge.png', dpi=150)
print("Saved: tier0-computation/s49_leggett_gge.png")

print(f"\n{'=' * 78}")
print(f"FINAL VERDICT: {verdict}")
print(f"{'=' * 78}")

# ==============================================================================
#  Section 17: CRITICAL SELF-CHECK — Is N=1 trivial?
# ==============================================================================
# In N=1 sector, only ONE particle occupies one of 8 modes.
# The density-density interaction V * n_k * n_{k'} = 0 for k != k'
# because at most one n_k = 1 at a time.
# Therefore H_N1 = H_free_N1 EXACTLY. The interaction is ZERO.
# The oscillation at omega = 0.133 = E_B3 - E_B2 is the TRIVIAL
# single-particle energy splitting, NOT a collective Leggett mode.

print("\n" + "=" * 78)
print("CRITICAL SELF-CHECK: N=1 sector interaction contribution")
print("=" * 78)

# Verify H_N1 = H_free_N1
H_diff = H_N1 - H_free_N1
print(f"||H_BCS(N=1) - H_free(N=1)|| = {np.linalg.norm(H_diff):.2e}")
print(f"  (Must be zero: 1-body interaction n_k*n_k' vanishes for single occupancy)")

if np.linalg.norm(H_diff) < 1e-10:
    print("\n  CONFIRMED: N=1 sector is EXACTLY non-interacting.")
    print("  The oscillation at omega = 0.133 M_KK is the bare")
    print("  single-particle sector energy splitting E_B3 - E_B2.")
    print("  This is NOT a Leggett collective mode.")
    print("  Enhancement = 1.00 (no pair-fluctuation physics at N=1).")

# ==============================================================================
#  Section 18: N=2 sector — where interaction IS non-trivial
# ==============================================================================
print("\n" + "=" * 78)
print("N=2 SECTOR ANALYSIS (interaction non-trivial)")
print("=" * 78)

# In N=2: two particles occupy two modes. n_k*n_{k'} CAN be nonzero.
# This is the MINIMAL system for pair correlations.

# phi_rel in N=2 sector
phi_N2 = np.zeros((len(N2_indices), len(N2_indices)), dtype=complex)
for i, ii in enumerate(N2_indices):
    for j, jj in enumerate(N2_indices):
        phi_N2[i, j] = phi_rel[ii, jj]

A_N2 = np.zeros((len(N2_indices), len(N2_indices)), dtype=complex)
for i, ii in enumerate(N2_indices):
    for j, jj in enumerate(N2_indices):
        A_N2[i, j] = A_rel[ii, jj]

# Free Hamiltonian in N=2
H_free_N2 = np.zeros((len(N2_indices), len(N2_indices)))
for i, ii in enumerate(N2_indices):
    for j, jj in enumerate(N2_indices):
        H_free_N2[i, j] = H_free[ii, jj]

evals_free_N2, evecs_free_N2 = np.linalg.eigh(H_free_N2)

# Interacting Hamiltonian in N=2
H_int_N2 = H_N2 - H_free_N2
print(f"||H_int(N=2)|| = {np.linalg.norm(H_int_N2):.6f}")
print(f"||H_int(N=2)|| / ||H_free(N=2)|| = {np.linalg.norm(H_int_N2)/np.linalg.norm(H_free_N2):.4f}")

# GGE in N=2: uniform (infinite T)
p_gge_N2 = np.ones(len(evals_N2)) / len(evals_N2)

# Spectral decomposition of C_L(t) in N=2
phi_N2_eig = evecs_N2.T @ phi_N2 @ evecs_N2

transitions_N2 = []
for m in range(len(evals_N2)):
    for n in range(len(evals_N2)):
        omega_mn = evals_N2[n] - evals_N2[m]
        weight = p_gge_N2[m] * np.abs(phi_N2_eig[m, n])**2
        if weight > 1e-15:
            transitions_N2.append((omega_mn, weight))

# Unique frequencies
omega_unique_N2 = {}
for omega, w in transitions_N2:
    key = round(omega, 6)
    omega_unique_N2[key] = omega_unique_N2.get(key, 0) + w

print(f"\nN=2 spectral transitions: {len(transitions_N2)}")
print(f"N=2 unique frequencies: {len(omega_unique_N2)}")
n_printed = 0
for om, w in sorted(omega_unique_N2.items(), key=lambda x: -x[1]):
    if w > 1e-4 and n_printed < 20:
        print(f"  omega = {om:10.6f}, weight = {w:10.6f}")
        n_printed += 1

# Total strength N=2
total_N2 = sum(omega_unique_N2.values())

# Free pair-transfer strength in N=2
phi_free_N2_eig = evecs_free_N2.T @ phi_N2 @ evecs_free_N2
transitions_free_N2 = []
for m in range(len(evals_free_N2)):
    for n in range(len(evals_free_N2)):
        omega_mn = evals_free_N2[n] - evals_free_N2[m]
        weight = p_gge_N2[m] * np.abs(phi_free_N2_eig[m, n])**2
        if weight > 1e-15:
            transitions_free_N2.append((omega_mn, weight))

total_free_N2 = sum(w for _, w in transitions_free_N2)

enhancement_N2 = total_N2 / total_free_N2 if total_free_N2 > 0 else float('inf')
print(f"\nN=2 total pair-transfer strength: {total_N2:.6f}")
print(f"N=2 free pair-transfer strength: {total_free_N2:.6f}")
print(f"N=2 enhancement: {enhancement_N2:.4f}x")

# Participation ratio N=2
strengths_N2 = list(omega_unique_N2.values())
pr_N2 = (sum(strengths_N2))**2 / sum(s**2 for s in strengths_N2) if strengths_N2 else 0
print(f"N=2 participation ratio: {pr_N2:.2f}")

# C_L(t) in N=2
C_L_N2 = np.zeros(n_t, dtype=complex)
for omega, w in transitions_N2:
    C_L_N2 += w * np.exp(1j * omega * t_array)

# Crossings
crossings_N2 = []
for i in range(len(C_L_N2.real) - 1):
    if C_L_N2.real[i] * C_L_N2.real[i+1] < 0:
        t_cross = t_array[i] + (t_array[i+1] - t_array[i]) * abs(C_L_N2.real[i]) / (abs(C_L_N2.real[i]) + abs(C_L_N2.real[i+1]))
        crossings_N2.append(t_cross)

print(f"\nN=2 C_L(t) zero crossings: {len(crossings_N2)}")
if len(crossings_N2) >= 2:
    half_per = np.diff(crossings_N2[:20])
    if len(half_per) > 0:
        omega_dom = np.pi / np.mean(half_per)
        print(f"N=2 dominant frequency: {omega_dom:.6f} M_KK")

# Commutator [H_N2, phi_N2]
comm_N2 = H_N2 @ phi_N2 - phi_N2 @ H_N2
comm_norm_N2 = np.linalg.norm(comm_N2) / np.linalg.norm(phi_N2) if np.linalg.norm(phi_N2) > 0 else 0
print(f"N=2: ||[H, phi_rel]|| / ||phi_rel|| = {comm_norm_N2:.6f}")

# Off-diagonal fraction in N=2
off_diag_N2 = 0
diag_N2 = 0
for m in range(len(evals_N2)):
    for n in range(len(evals_N2)):
        val = np.abs(phi_N2_eig[m, n])**2
        if m == n:
            diag_N2 += val
        else:
            off_diag_N2 += val
total_N2_norm = diag_N2 + off_diag_N2
off_diag_frac_N2 = off_diag_N2 / total_N2_norm if total_N2_norm > 0 else 0
print(f"N=2: off-diagonal fraction = {off_diag_frac_N2:.6f}")
print(f"N=2: phi_rel INDEPENDENT of I_alpha: {comm_norm_N2 > 0.01}")

# ==============================================================================
#  Section 19: Interaction effect — spectral shift
# ==============================================================================
print("\n--- Interaction Effect on Spectrum ---")

# Compare interacting vs free eigenvalues in N=2
print(f"N=2 free eigenvalues (first 10): {evals_free_N2[:10]}")
print(f"N=2 BCS eigenvalues (first 10):  {evals_N2[:10]}")
print(f"Spectral shift (first 10): {evals_N2[:10] - evals_free_N2[:10]}")

# The key question: do the TRANSITION FREQUENCIES change?
# In the free case, transitions are at E_B3 - E_B2, E_B1 - E_B2, etc.
# In the interacting case, the interaction shifts these frequencies.
# The shift IS the pair-fluctuation effect.

omega_free_unique = {}
for omega, w in transitions_free_N2:
    key = round(omega, 6)
    omega_free_unique[key] = omega_free_unique.get(key, 0) + w

print(f"\nN=2 free unique frequencies: {len(omega_free_unique)}")
n_printed_f = 0
for om, w in sorted(omega_free_unique.items(), key=lambda x: -x[1]):
    if w > 1e-4 and n_printed_f < 10:
        print(f"  omega = {om:10.6f}, weight = {w:10.6f}")
        n_printed_f += 1

# ==============================================================================
#  Section 20: CORRECTED GATE ASSESSMENT
# ==============================================================================
print("\n" + "=" * 78)
print("CORRECTED GATE ASSESSMENT: LEGGETT-GGE-49")
print("=" * 78)

print("""
CRITICAL FINDING: The N=1 sector is EXACTLY non-interacting.
The density-density interaction n_k * n_{k'} vanishes identically
when only ONE particle is present. The oscillation at omega = 0.133 M_KK
in the N=1 GGE is the TRIVIAL single-particle energy splitting E_B3 - E_B2,
not a Leggett collective mode. Enhancement = 1.00 confirms this.

This is the nuclear analog of computing pair-transfer strength in a system
with ZERO Cooper pairs. You get single-particle transitions, not pair
vibrations. The Broglia fluctuation effect requires N >= 2.

For the N=2 sector (where interaction IS non-trivial), we find:
""")

# Determine if N=2 shows genuine interaction effects
freq_shift_exists = enhancement_N2 > 1.05 or enhancement_N2 < 0.95  # 5% threshold

# The honest assessment
if freq_shift_exists:
    print(f"  N=2 enhancement = {enhancement_N2:.4f}x (non-trivial interaction effect)")
    print(f"  Interaction DOES modify pair-transfer correlations at N=2.")
    # But: the physical system IS N=1 (S48 N-PAIR-FULL-48 proved N=1 exact)
    print(f"\n  HOWEVER: The physical system has N=1 (S48 N-PAIR-FULL proved this).")
    print(f"  At N=1, the interaction has NO EFFECT on any correlation function.")
    print(f"  The Leggett correlator is structurally trivial at N=1.")
    corrected_verdict = "INFO"
    corrected_detail = (
        f"C_L(t) oscillates at omega=0.133 M_KK in N=1 GGE, but this is the "
        f"TRIVIAL single-particle energy splitting E_B3-E_B2 (enhancement=1.00, "
        f"interaction exactly zero at N=1). phi_rel is formally independent of "
        f"I_alpha but carries no collective information. "
        f"N=2 shows enhancement={enhancement_N2:.2f}x (non-trivial), "
        f"but physical system is N=1. No Broglia pair-fluctuation effect."
    )
else:
    print(f"  N=2 enhancement = {enhancement_N2:.4f}x")
    corrected_verdict = "INFO"
    corrected_detail = (
        f"C_L(t) oscillates at omega=0.133 M_KK in N=1 GGE, but this is the "
        f"TRIVIAL single-particle energy splitting E_B3-E_B2. N=1 sector is "
        f"exactly non-interacting (enhancement=1.00). phi_rel formally independent "
        f"of I_alpha but carries no collective information. "
        f"N=2 enhancement={enhancement_N2:.2f}x."
    )

print(f"\nCORRECTED Verdict: {corrected_verdict}")
print(f"Detail: {corrected_detail}")

# Update the saved data
np.savez('tier0-computation/s49_leggett_gge.npz',
    # Gate
    gate_name='LEGGETT-GGE-49',
    gate_verdict=corrected_verdict,
    gate_detail=corrected_detail,
    # GGE parameters
    p_gge_N1=p_gge_N1,
    p_gibbs_N1=p_gibbs_N1,
    T_compound=T_compound,
    evals_N1=evals_N1,
    evals_N2=evals_N2,
    # Correlator N=1
    t_array=t_array,
    C_L_real=C_L.real,
    C_L_imag=C_L.imag,
    C_L_gibbs_real=C_L_gibbs.real,
    C_A_real=C_A.real,
    # Correlator N=2
    C_L_N2_real=C_L_N2.real,
    C_L_N2_imag=C_L_N2.imag,
    # Spectral function
    transitions_omega=np.array([t[0] for t in transitions]),
    transitions_weight=np.array([t[1] for t in transitions]),
    # N=2 data
    transitions_N2_omega=np.array([t[0] for t in transitions_N2]),
    transitions_N2_weight=np.array([t[1] for t in transitions_N2]),
    enhancement_N2=enhancement_N2,
    pr_N2=pr_N2,
    # Independence test
    off_diag_frac=off_diag_frac,
    comm_norm=comm_norm,
    phi_rel_independent=phi_rel_independent,
    comm_norm_N2=comm_norm_N2,
    off_diag_frac_N2=off_diag_frac_N2,
    # Oscillation analysis
    n_crossings=n_crossings,
    n_crossings_N2=len(crossings_N2),
    persistence_ratio=persistence_ratio,
    # Nuclear benchmark
    enhancement=enhancement,
    pr_gge=pr_gge,
    pr_free=pr_free,
    total_strength=total_strength,
    total_free_strength=total_free,
    # Critical: N=1 is non-interacting
    N1_interaction_norm=np.linalg.norm(H_diff),
    N1_is_trivial=True,
    oscillation_is_sp_splitting=True,
    omega_B3_minus_B2=float(E_8[5] - E_8[0]),
    # Recurrence
    T_recurrence=T_rec,
    gge_gibbs_deviation=deviation,
)
print("\nUpdated: tier0-computation/s49_leggett_gge.npz")

# Updated plot with N=2 comparison
fig2, axes2 = plt.subplots(2, 2, figsize=(14, 10))
fig2.suptitle(f'LEGGETT-GGE-49: Corrected Verdict = {corrected_verdict}\n'
              f'(N=1 trivial; oscillation is bare E_B3-E_B2 splitting)', fontsize=12, fontweight='bold')

ax = axes2[0, 0]
ax.plot(t_array, C_L.real, 'b-', linewidth=0.8, label='N=1 GGE (trivial)')
ax.plot(t_array, C_L_N2.real / C_L_N2[0].real * C_L[0].real, 'r-', linewidth=0.8,
        alpha=0.7, label='N=2 GGE (scaled)')
ax.axhline(0, color='k', linewidth=0.3)
ax.set_xlabel('t (M_KK^{-1})')
ax.set_ylabel('C_L(t)')
ax.set_title('Leggett correlator: N=1 vs N=2')
ax.legend(fontsize=8)
ax.set_xlim(0, t_max)

ax = axes2[0, 1]
omega_all_N2 = np.array([t[0] for t in transitions_N2])
weight_all_N2 = np.array([t[1] for t in transitions_N2])
ax.stem(omega_trans, weight_trans, linefmt='b-', markerfmt='bo', basefmt='k-',
        label='N=1')
if len(omega_all_N2) > 0:
    ax.stem(omega_all_N2, weight_all_N2, linefmt='r-', markerfmt='r^', basefmt='k-',
            label='N=2')
ax.set_xlabel('omega (M_KK)')
ax.set_ylabel('S(omega)')
ax.set_title('Pair-transfer spectral function')
ax.legend(fontsize=8)

ax = axes2[1, 0]
ax.bar(['N=1\n(trivial)', 'N=2\n(interacting)'], [enhancement, enhancement_N2],
       color=['lightblue', 'salmon'])
ax.axhline(1, color='k', linestyle='--', linewidth=0.5)
ax.axhline(2, color='green', linestyle=':', linewidth=0.5, label='Nuclear 2x threshold')
ax.axhline(5, color='green', linestyle='--', linewidth=0.5, label='Nuclear 5x threshold')
ax.set_ylabel('Enhancement over free')
ax.set_title('Broglia pair-fluctuation effect')
ax.legend(fontsize=8)

ax = axes2[1, 1]
ax.text(0.1, 0.8, f'N=1 SECTOR', fontsize=14, fontweight='bold', transform=ax.transAxes)
ax.text(0.1, 0.65, f'H_int(N=1) = 0 EXACTLY', fontsize=12, color='red', transform=ax.transAxes)
ax.text(0.1, 0.50, f'omega_osc = E_B3 - E_B2 = {E_8[5]-E_8[0]:.6f}', fontsize=10, transform=ax.transAxes)
ax.text(0.1, 0.38, f'Enhancement = {enhancement:.4f}x (no pair physics)', fontsize=10, transform=ax.transAxes)
ax.text(0.1, 0.22, f'N=2 SECTOR', fontsize=14, fontweight='bold', transform=ax.transAxes)
ax.text(0.1, 0.08, f'Enhancement = {enhancement_N2:.4f}x, PR = {pr_N2:.1f}', fontsize=10, transform=ax.transAxes)
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')
ax.set_title('Summary')

plt.tight_layout()
plt.savefig('tier0-computation/s49_leggett_gge.png', dpi=150)
print("Updated: tier0-computation/s49_leggett_gge.png")

print(f"\n{'=' * 78}")
print(f"CORRECTED FINAL VERDICT: {corrected_verdict}")
print(f"{'=' * 78}")
