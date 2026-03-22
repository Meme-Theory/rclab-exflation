#!/usr/bin/env python3
"""
S46 RG-PAIR-TRANSFER-46: Richardson-Gaudin Pair Transfer Spectral Function
==========================================================================

Computes the pair-transfer spectral function S(omega, k) from the 8-mode
Richardson-Gaudin (BCS) Hamiltonian at the fold.

METHODOLOGY:
1. Build the full 2^8 = 256 state Fock space for 8 fermionic modes.
2. Construct the BCS Hamiltonian:
      H = sum_k (eps_k - mu) * n_k  -  sum_{kk'} V_{kk'} c^+_k c^+_{k_bar} c_{k'_bar} c_{k'}
   where modes are grouped by SU(3) representation sector (B1/B2/B3) with
   energies and pairing matrix elements from upstream computations.
3. Diagonalize H exactly (256x256 matrix) to find all eigenstates |n>.
4. Identify the ground state |GS> (the GGE/BCS ground state at the fold).
5. For each sector s = (p,q), construct the pair-creation operator restricted
   to that sector:
      P^+_s = sum_{k in sector s} c^+_{k,up} c^+_{k,dn}
   Here each "mode k" is a Kramers pair (k, k_bar). The pair creation
   operator adds one Cooper pair within sector s.
6. Compute S(omega, s) = sum_n |<n|P^+_s|GS>|^2 * delta(omega - E_n + E_GS)
   by exact projection onto all 256 eigenstates.
7. Extract per-sector diagnostics: integrated strength, centroid, width,
   fragmentation (number of significant peaks).

PHYSICAL BASIS (Nazarewicz perspective):
- The pair-transfer spectral function is the nuclear analogue of the
  (p,t) or (t,p) reaction cross section measured in pair-transfer experiments.
- In nuclear structure (Papers 03, 13), pair-addition strength fragments
  among shell-model states. The Giant Pairing Vibration (GPV) collects
  60-80% of the sum rule into a single collective mode.
- For the SU(3) BCS system, the question is: is the strength concentrated
  (sharp GPV) or fragmented (many comparable peaks)? This directly determines
  the effective hose count for n_s.
- The INTEGRATED strength sum_omega S(omega, s) = <GS|P^-_s P^+_s|GS>
  is the pair-transfer sum rule for sector s. This equals the hose count
  from W1-2 if all pair modes are counted.

GATE: INFO (diagnostic). This computation upgrades the W1-2 hose count from
an approximate counting argument to an exact spectral function.

Session 46 Wave 2, Agent: nazarewicz-nuclear-structure-theorist
Provenance: s42_hauser_feshbach.npz, s38_cc_instanton.npz, s43_flat_band.npz,
            s45_qtheory_bcs.npz, canonical_constants.py
"""

import sys
sys.path.insert(0, '.')

import numpy as np
from scipy.linalg import eigh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    E_cond, Delta_0_GL, Delta_0_OES, Delta_B3,
    xi_BCS, tau_fold, E_B1, E_B2_mean, E_B3_mean,
    omega_PV, M_max_thouless, N_dof_BCS, S_inst
)

print("=" * 78)
print("S46 RG-PAIR-TRANSFER-46: Pair Transfer Spectral Function")
print("=" * 78)
print()

# ==============================================================================
# SECTION 1: Define the 8-mode model
# ==============================================================================
#
# The 8 modes at the fold (tau = 0.19) are:
#   Mode 0: B1 sector (singlet, 1 Kramers pair) -- eps = E_B1 = 0.819
#   Modes 1-4: B2 sector (adjoint, 4 Kramers pairs) -- eps = E_B2 = 0.845
#   Modes 5-7: B3 sector (3 Kramers pairs) -- eps = E_B3 = 0.978
#
# Each "mode" k represents a Kramers pair. The Fock space basis state is
# |n_0, n_1, ..., n_7> where n_k = 0 or 1 (pair k occupied or empty).
# A state with n_k = 1 means the Cooper pair at mode k is present:
# both c^+_{k,up} and c^+_{k,dn} are occupied.
#
# Total Fock space dimension: 2^8 = 256 pair states.
#
# The Hamiltonian in the pair representation:
#   H = sum_k 2*eps_k * n_k  -  sum_{kk'} V_{kk'} * P^+_k P^-_{k'}
# where P^+_k = c^+_{k,up} c^+_{k,dn} creates a pair at mode k.

N_modes = 8
N_fock = 2**N_modes

print(f"Model: {N_modes} modes (Kramers pairs), Fock space dim = {N_fock}")
print()

# Mode assignments
# Index: [B1_0, B2_0, B2_1, B2_2, B2_3, B3_0, B3_1, B3_2]
mode_sector = ['B1', 'B2', 'B2', 'B2', 'B2', 'B3', 'B3', 'B3']
mode_eps = np.array([
    E_B1,       # B1: 0.8191
    E_B2_mean,  # B2: 0.8453
    E_B2_mean,
    E_B2_mean,
    E_B2_mean,
    E_B3_mean,  # B3: 0.9782
    E_B3_mean,
    E_B3_mean,
])

# Add small intra-sector splitting to break exact degeneracy
# This represents the fine structure from the Jensen metric deformation.
# Within B2: use the actual Thouless eigenvalues as a proxy for splitting
# From s43_flat_band.npz: M_B2_evals = [1.292, 0.376, 0.108, -0.348]
# These are pairing matrix eigenvalues, not single-particle energies,
# but the spread indicates ~0.01 internal variation.
# For B3: spread ~0.005 from Dirac spectrum fine structure
B2_split = np.array([-0.012, -0.004, 0.004, 0.012])  # +/- 12 meV
B3_split = np.array([-0.005, 0.000, 0.005])            # +/- 5 meV

mode_eps[1:5] += B2_split
mode_eps[5:8] += B3_split

print("Mode single-particle energies (eps_k):")
for i, (s, e) in enumerate(zip(mode_sector, mode_eps)):
    print(f"  Mode {i} ({s}): eps = {e:.6f}")
print()

# Chemical potential: mu = 0 by PH symmetry (S34 MU-35a)
mu = 0.0

# ==============================================================================
# SECTION 2: Load the pairing interaction matrix V_{kk'}
# ==============================================================================
#
# The pairing matrix elements from the Dirac spectrum computation:
# V_B2B2 is the 4x4 matrix from s43_flat_band.npz (exact from spectrum)
# V_B1B1, V_B3B3: estimated from scaling (no direct computation)
# V_B2B1, V_B2B3: from s42_hauser_feshbach.npz (RMS values)
#
# From W1-1 (Volovik): the coupling must be rescaled by alpha* = 0.4347
# so that the ground state energy matches E_cond = -0.137 M_KK.
# I will determine the coupling self-consistently below.

d_fb = np.load('s43_flat_band.npz', allow_pickle=True)
V_B2B2_raw = d_fb['V_B2B2']  # 4x4 matrix
g_eff = float(d_fb['g_eff'])   # 0.0376

d_hf = np.load('s42_hauser_feshbach.npz', allow_pickle=True)
V_B2B2_rms = float(d_hf['V_B2B2_rms'])  # 0.589
V_B2_B1_rms = float(d_hf['V_B2_B1_rms'])  # 0.299
V_B2_B3_rms = float(d_hf['V_B2_B3_rms'])  # 0.068

print("Pairing matrix elements (upstream):")
print(f"  V_B2B2 (4x4 from spectrum):")
for row in V_B2B2_raw:
    print(f"    [{', '.join(f'{v:.5f}' for v in row)}]")
print(f"  V_B2B2_rms = {V_B2B2_rms:.4f}")
print(f"  V_B2_B1_rms = {V_B2_B1_rms:.4f}")
print(f"  V_B2_B3_rms = {V_B2_B3_rms:.4f}")
print(f"  g_eff = {g_eff:.6f}")
print()

# Build the full 8x8 pairing interaction matrix V[k,k']
# The V matrix is POSITIVE for attractive interaction in our convention:
# H_pair = - sum_{kk'} V_{kk'} P^+_k P^-_{k'}
#
# Off-diagonal blocks estimated from RMS values with random phases
# (the RMS is what enters the BCS gap equation; we use it directly)

V_full = np.zeros((N_modes, N_modes))

# B2-B2 block (indices 1-4): use the actual matrix
V_full[1:5, 1:5] = V_B2B2_raw

# B1-B1 (index 0,0): single mode, self-pairing
# Estimated from V_B2B1 * V_B1B2 / V_B2B2 ~ V_B2B1_rms^2 / V_B2B2_rms
V_B1B1 = V_B2_B1_rms**2 / V_B2B2_rms
V_full[0, 0] = V_B1B1

# B3-B3 block (indices 5-7): estimated from V_B2B3 scaling
# V_B3B3 ~ V_B2B3^2 / V_B2B2 (second-order perturbation theory estimate)
V_B3B3_elem = V_B2_B3_rms**2 / V_B2B2_rms
V_full[5:8, 5:8] = V_B3B3_elem
# Diagonal elements slightly enhanced
for i in range(5, 8):
    V_full[i, i] = V_B3B3_elem * 1.2

# B1-B2 off-diagonal (index 0 vs 1-4)
for j in range(1, 5):
    V_full[0, j] = V_B2_B1_rms / 2.0  # distribute RMS among 4 modes
    V_full[j, 0] = V_full[0, j]

# B2-B3 off-diagonal (indices 1-4 vs 5-7)
for i in range(1, 5):
    for j in range(5, 8):
        V_full[i, j] = V_B2_B3_rms / np.sqrt(12.0)  # distribute among 12 pairs
        V_full[j, i] = V_full[i, j]

# B1-B3 off-diagonal (index 0 vs 5-7): very weak
for j in range(5, 8):
    V_full[0, j] = V_B2_B3_rms * V_B2_B1_rms / (V_B2B2_rms * 3.0)
    V_full[j, 0] = V_full[0, j]

# Symmetrize
V_full = 0.5 * (V_full + V_full.T)

print("Full 8x8 pairing matrix V[k,k']:")
for i in range(N_modes):
    print(f"  [{', '.join(f'{V_full[i,j]:8.5f}' for j in range(N_modes))}]  ({mode_sector[i]})")
print()

# ==============================================================================
# SECTION 3: Rescale coupling to match E_cond
# ==============================================================================
#
# The ground state energy must match E_cond = -0.137 M_KK (from 32-state
# exact diagonalization in S35). We rescale V -> alpha_star * V and find
# alpha_star by requiring E_GS(alpha_star) = E_cond.
#
# This is the same rescaling found in W1-1 (alpha* = 0.4347).

def build_hamiltonian(eps_arr, V_mat, coupling):
    """
    Build the BCS Hamiltonian in the pair Fock space.

    H = sum_k 2*(eps_k - mu) * n_k  -  coupling * sum_{kk'} V_{kk'} P^+_k P^-_{k'}

    In the pair representation, each basis state |b> encodes which pairs are
    occupied via the binary representation of b.

    P^+_k creates a pair at mode k: P^+_k |...0_k...> = |...1_k...>
    P^-_k destroys a pair at mode k: P^-_k |...1_k...> = |...0_k...>
    n_k = P^+_k P^-_k is the pair occupation number.
    """
    N = len(eps_arr)
    dim = 2**N
    H = np.zeros((dim, dim))

    for b in range(dim):
        # Diagonal: kinetic energy
        for k in range(N):
            if b & (1 << k):
                H[b, b] += 2.0 * (eps_arr[k] - mu)

        # Off-diagonal and diagonal: pairing interaction
        for k in range(N):
            for kp in range(N):
                # P^+_k P^-_{k'} |b> -> nonzero only if k' occupied, k empty (or k=k')
                if k == kp:
                    # Diagonal contribution: V[k,k] * n_k
                    if b & (1 << k):
                        H[b, b] -= coupling * V_mat[k, k]
                else:
                    # Off-diagonal: k' must be occupied in |b>, k must be empty
                    if (b & (1 << kp)) and not (b & (1 << k)):
                        # Remove pair at k', add pair at k
                        b_new = (b ^ (1 << kp)) | (1 << k)
                        H[b_new, b] -= coupling * V_mat[k, kp]

    return H


def ground_state_energy(eps_arr, V_mat, coupling):
    """Return ground state energy for given coupling."""
    H = build_hamiltonian(eps_arr, V_mat, coupling)
    evals = np.linalg.eigvalsh(H)
    return evals[0]


# Binary search for alpha_star that gives E_GS = E_cond
target_E = E_cond  # -0.137
print(f"Target ground state energy: E_cond = {target_E:.6f} M_KK")

# Search bounds
alpha_lo, alpha_hi = 0.01, 5.0
for _ in range(50):
    alpha_mid = 0.5 * (alpha_lo + alpha_hi)
    E_test = ground_state_energy(mode_eps, V_full, alpha_mid)
    if E_test < target_E:
        alpha_hi = alpha_mid
    else:
        alpha_lo = alpha_mid

alpha_star = 0.5 * (alpha_lo + alpha_hi)
E_gs_check = ground_state_energy(mode_eps, V_full, alpha_star)
print(f"Coupling rescale: alpha* = {alpha_star:.6f}")
print(f"E_GS(alpha*) = {E_gs_check:.6f} (target: {target_E:.6f}, "
      f"error: {abs(E_gs_check - target_E):.2e})")
print()

# ==============================================================================
# SECTION 4: Full exact diagonalization
# ==============================================================================

print("EXACT DIAGONALIZATION OF H_BCS")
print("-" * 78)

H = build_hamiltonian(mode_eps, V_full, alpha_star)

# Verify Hermiticity
assert np.allclose(H, H.T), "Hamiltonian is not symmetric!"

# Diagonalize
eigenvalues, eigenvectors = eigh(H)

E_GS = eigenvalues[0]
psi_GS = eigenvectors[:, 0]

print(f"Ground state energy: E_GS = {E_GS:.8f} M_KK")
print(f"First excited state: E_1 = {eigenvalues[1]:.8f}, gap = {eigenvalues[1] - E_GS:.6f}")
print(f"Highest state: E_max = {eigenvalues[-1]:.8f}")
print(f"Spectral range: {eigenvalues[-1] - E_GS:.4f} M_KK")
print()

# Ground state properties
print("Ground state occupation numbers:")
n_occ = np.zeros(N_modes)
for b in range(N_fock):
    prob = psi_GS[b]**2
    for k in range(N_modes):
        if b & (1 << k):
            n_occ[k] += prob

n_pairs_gs = np.sum(n_occ)
print(f"  {'Mode':<8} {'Sector':<8} {'<n_k>':<10} {'v_k^2':<10}")
for k in range(N_modes):
    print(f"  {k:<8} {mode_sector[k]:<8} {n_occ[k]:<10.6f} {n_occ[k]:<10.6f}")
print(f"  Total pair number: <N> = {n_pairs_gs:.4f}")
print()

# Particle number distribution
pair_number_dist = np.zeros(N_modes + 1)
for b in range(N_fock):
    n_pairs = bin(b).count('1')
    pair_number_dist[n_pairs] += psi_GS[b]**2

print("Pair number distribution P(N_pairs):")
for n in range(N_modes + 1):
    if pair_number_dist[n] > 1e-8:
        print(f"  N = {n}: P = {pair_number_dist[n]:.6f}")
print()

# ==============================================================================
# SECTION 5: Define sector-to-mode mapping for pair operators
# ==============================================================================
#
# The 9 SU(3) representations map to modes via their block structure:
#   B1 block: reps with q_7 > 0:  (1,0), (2,0), (3,0), (2,1) -> B1 modes
#   B2 block: reps with q_7 = 0:  (0,0), (1,1) -> B2 modes
#   B3 block: reps with q_7 < 0:  (0,1), (0,2), (0,3) -> B3 modes
#
# BUT in the 8-mode model, we have only 1 B1, 4 B2, 3 B3 modes.
# The modes don't correspond 1:1 to individual (p,q) reps.
# Instead, each sector (B1/B2/B3) is a collection of modes that could
# be excited by pair creation in ANY rep in that block.
#
# For the pair-transfer spectral function, the relevant question is:
# "If I create a pair in sector (p,q), which modes does it excite?"
#
# The physical pair operator for sector (p,q) is:
#   P^+_{(p,q)} = sum_{k in block(p,q)} w_{k,(p,q)} c^+_k c^+_{k_bar}
# where w_{k,(p,q)} are the Clebsch-Gordan-like weights from the
# Peter-Weyl decomposition of the pair wavefunction in rep (p,q).
#
# For the EXACT computation, I define the pair operators per BLOCK:
#   P^+_{B1} = c^+_0 c^+_{0_bar}  (1 mode)
#   P^+_{B2} = sum_{k=1}^{4} c^+_k c^+_{k_bar}  (4 modes)
#   P^+_{B3} = sum_{k=5}^{7} c^+_k c^+_{k_bar}  (3 modes)
#
# And per individual MODE:
#   P^+_k = c^+_k c^+_{k_bar}  (creates one pair at mode k)
#
# The per-rep spectral function is then a weighted combination:
#   S(omega, (p,q)) = sum_k |w_{k,(p,q)}|^2 * S_k(omega)
# where S_k(omega) = sum_n |<n|P^+_k|GS>|^2 delta(omega - E_n + E_GS)
# is the single-mode pair transfer spectral function.

print("PAIR-TRANSFER SPECTRAL FUNCTION COMPUTATION")
print("=" * 78)
print()

# Define blocks
blocks = {
    'B1': [0],         # 1 mode
    'B2': [1, 2, 3, 4],  # 4 modes
    'B3': [5, 6, 7],     # 3 modes
}

# SU(3) representation catalog
# (p,q): dim, C2, k=sqrt(C2), q7=(p-q)/3, block
reps = [
    (0, 0,  1, 0.000, 0.0000, 0.000, 'B2'),
    (1, 0,  3, 1.333, 1.1547, 0.333, 'B1'),
    (0, 1,  3, 1.333, 1.1547,-0.333, 'B3'),
    (1, 1,  8, 3.000, 1.7321, 0.000, 'B2'),
    (2, 0,  6, 3.333, 1.8257, 0.667, 'B1'),
    (0, 2,  6, 3.333, 1.8257,-0.667, 'B3'),
    (3, 0, 10, 6.000, 2.4495, 1.000, 'B1'),
    (0, 3, 10, 6.000, 2.4495,-1.000, 'B3'),
    (2, 1, 15, 5.000, 2.2361, 0.333, 'B1'),
]

# ==============================================================================
# SECTION 6: Compute per-mode pair-transfer spectral functions S_k(omega)
# ==============================================================================
#
# For each mode k, the pair creation operator P^+_k in the pair Fock space
# acts as:  P^+_k |b> = |b + 2^k> if bit k of b is 0, else 0.
#
# S_k(omega) = sum_n |<n|P^+_k|GS>|^2 * delta(omega - (E_n - E_GS))
#
# We compute <n|P^+_k|GS> = sum_b <n|b+2^k> * <b|GS> * (1 if bit k of b is 0)
#                           = sum_{b: bit k=0} eigvec[b+2^k, n] * psi_GS[b]

print("Computing per-mode pair-transfer spectral functions...")
print()

# Storage for spectral functions
S_mode = {}  # k -> (excitation_energies, strengths) arrays

for k in range(N_modes):
    # Apply P^+_k to |GS>
    P_psi = np.zeros(N_fock)
    for b in range(N_fock):
        if not (b & (1 << k)):  # bit k is 0 -> can create pair
            P_psi[b | (1 << k)] = psi_GS[b]

    # Project onto eigenstates: <n|P^+_k|GS> = eigvectors[:, n]^T . P_psi
    overlaps = eigenvectors.T @ P_psi  # shape (N_fock,)
    strengths = overlaps**2  # |<n|P^+_k|GS>|^2
    exc_energies = eigenvalues - E_GS  # E_n - E_GS

    # Filter to significant contributions
    mask = strengths > 1e-12

    S_mode[k] = {
        'exc_energies': exc_energies[mask],
        'strengths': strengths[mask],
        'total_strength': np.sum(strengths),
        'n_peaks': np.sum(mask),
    }

print(f"{'Mode':<6} {'Sector':<8} {'Total S':<12} {'N_peaks':<10} {'Largest frac':<15} {'Centroid':<12} {'Width':<10}")
for k in range(N_modes):
    s = S_mode[k]
    total = s['total_strength']
    if total > 1e-15:
        centroid = np.sum(s['exc_energies'] * s['strengths']) / total
        variance = np.sum((s['exc_energies'] - centroid)**2 * s['strengths']) / total
        width = np.sqrt(variance) if variance > 0 else 0
        max_frac = np.max(s['strengths']) / total if total > 0 else 0
    else:
        centroid = 0
        width = 0
        max_frac = 0

    S_mode[k]['centroid'] = centroid
    S_mode[k]['width'] = width
    S_mode[k]['max_frac'] = max_frac

    print(f"  {k:<6} {mode_sector[k]:<8} {total:<12.6f} {s['n_peaks']:<10} "
          f"{max_frac:<15.4f} {centroid:<12.6f} {width:<10.6f}")

print()

# ==============================================================================
# SECTION 7: Compute per-block (sector) pair-transfer spectral functions
# ==============================================================================
#
# The block pair operator is: P^+_{block} = sum_{k in block} P^+_k
# This is the coherent sum -- the nuclear pair-addition operator restricted
# to the block. Its spectral function reveals the GPV.

print("PER-BLOCK PAIR-TRANSFER SPECTRAL FUNCTIONS")
print("-" * 78)

S_block = {}

for block_name, mode_indices in blocks.items():
    # Apply P^+_block = sum_k P^+_k to |GS>
    P_psi = np.zeros(N_fock)
    for k in mode_indices:
        for b in range(N_fock):
            if not (b & (1 << k)):
                P_psi[b | (1 << k)] += psi_GS[b]

    # Project onto eigenstates
    overlaps = eigenvectors.T @ P_psi
    strengths = overlaps**2
    exc_energies = eigenvalues - E_GS

    # Significant peaks
    mask = strengths > 1e-12
    total = np.sum(strengths)

    if total > 1e-15:
        centroid = np.sum(exc_energies[mask] * strengths[mask]) / total
        variance = np.sum((exc_energies[mask] - centroid)**2 * strengths[mask]) / total
        width = np.sqrt(variance) if variance > 0 else 0
        max_frac = np.max(strengths[mask]) / total
    else:
        centroid = 0
        width = 0
        max_frac = 0

    # Count peaks above 1/e of maximum
    if np.max(strengths[mask]) > 0:
        n_above_1e = np.sum(strengths[mask] / np.max(strengths[mask]) > 1.0/np.e)
    else:
        n_above_1e = 0

    S_block[block_name] = {
        'exc_energies': exc_energies[mask],
        'strengths': strengths[mask],
        'total_strength': total,
        'n_peaks': np.sum(mask),
        'n_above_1e': n_above_1e,
        'centroid': centroid,
        'width': width,
        'max_frac': max_frac,
    }

    print(f"\nBlock {block_name} ({len(mode_indices)} modes):")
    print(f"  Total strength (sum rule): {total:.6f}")
    print(f"  Number of significant peaks: {np.sum(mask)}")
    print(f"  Peaks above 1/e of max: {n_above_1e}")
    print(f"  Largest peak fraction: {max_frac:.4f}")
    print(f"  Centroid energy: {centroid:.6f} M_KK")
    print(f"  Width (std dev): {width:.6f} M_KK")
    print(f"  GPV concentration: {'SHARP' if max_frac > 0.5 else 'FRAGMENTED'}")

    # Print the top 5 peaks
    sorted_idx = np.argsort(strengths[mask])[::-1]
    exc_e_sig = exc_energies[mask]
    str_sig = strengths[mask]
    n_show = min(5, len(sorted_idx))
    print(f"  Top {n_show} peaks:")
    for i in range(n_show):
        idx = sorted_idx[i]
        frac = str_sig[idx] / total if total > 0 else 0
        print(f"    E = {exc_e_sig[idx]:.6f}, S = {str_sig[idx]:.6f} ({frac*100:.1f}%)")

print()

# ==============================================================================
# SECTION 8: Map to SU(3) representations via k = sqrt(C_2)
# ==============================================================================
#
# Each (p,q) representation has Casimir k = sqrt(C_2) and maps to a block.
# The pair operator for rep (p,q) is P^+_{(p,q)} restricted to the
# appropriate block. The NUMBER of pair modes within each rep determines
# the relative weight:
#   weight(p,q) = dim(p,q) / (2 * total_dim_in_block)
#
# For the hose count, what matters is: at each k, how many independent
# pair-transfer peaks are there?

print("REPRESENTATION-RESOLVED PAIR TRANSFER SPECTRUM")
print("-" * 78)

# Map each rep to its block and compute the scaled spectral function
rep_results = []

for p, q, dim_pq, C2, k_val, q7, block in reps:
    if k_val == 0:
        # Singlet: no pair transfer (dim=1, only 0 or 1 pair, trivial)
        rep_results.append({
            'p': p, 'q': q, 'dim': dim_pq, 'C2': C2, 'k': k_val,
            'q7': q7, 'block': block,
            'total_strength': 0.0,
            'n_peaks': 0, 'n_above_1e': 0,
            'centroid': 0.0, 'width': 0.0, 'max_frac': 0.0,
            'n_eff_pairs': 0.0,
        })
        continue

    # Get the block spectral function
    sb = S_block[block]

    # The rep's share of the block pair-transfer strength is proportional to
    # dim(p,q) / total_dim_in_block, where total_dim = sum of dim for all
    # reps in this block.
    # B1 reps: (1,0)dim=3, (2,0)dim=6, (3,0)dim=10, (2,1)dim=15 -> total=34
    # B2 reps: (0,0)dim=1, (1,1)dim=8 -> total=9
    # B3 reps: (0,1)dim=3, (0,2)dim=6, (0,3)dim=10 -> total=19
    block_total_dim = {
        'B1': 3 + 6 + 10 + 15,  # 34
        'B2': 1 + 8,              # 9
        'B3': 3 + 6 + 10,         # 19
    }

    # The NUMBER of Kramers pairs in rep (p,q) that can participate:
    # = dim(p,q) / 2 (each pair involves two states)
    n_kramers = dim_pq / 2.0

    # Weight for this rep's share of the block spectral function
    # Proportional to n_kramers / total_kramers_in_block
    total_kramers_block = block_total_dim[block] / 2.0
    weight = n_kramers / total_kramers_block

    # Scaled spectral function for this rep
    total_strength_rep = sb['total_strength'] * weight

    # The number of EFFECTIVE independent pair peaks for this rep:
    # If the block has n_above_1e peaks, this rep contributes a fraction
    # weight of them. The effective peak count is at least 1 (from the GPV).
    # But more accurately: the number of pair modes in this rep is n_kramers,
    # and the block's spectral function reveals how they distribute.
    #
    # KEY RESULT: The block spectral function already tells us the FRAGMENTATION.
    # If the block has 1 dominant GPV peak (max_frac > 0.5), then this rep
    # also has 1 dominant peak. If fragmented, scale by weight.

    if sb['n_above_1e'] > 0:
        # Effective pair modes for this rep: min(n_kramers, n_block_peaks * weight)
        # But cannot exceed the actual Kramers pair count
        n_eff = min(n_kramers, sb['n_above_1e'] * weight)
        n_eff = max(1.0, n_eff)  # at least 1 pair mode
    else:
        n_eff = 1.0

    rep_results.append({
        'p': p, 'q': q, 'dim': dim_pq, 'C2': C2, 'k': k_val,
        'q7': q7, 'block': block,
        'total_strength': total_strength_rep,
        'n_peaks': sb['n_peaks'],
        'n_above_1e': sb['n_above_1e'],
        'centroid': sb['centroid'],
        'width': sb['width'],
        'max_frac': sb['max_frac'],
        'n_eff_pairs': n_eff,
        'weight': weight,
    })

print(f"{'(p,q)':<8} {'dim':<5} {'k':<8} {'block':<6} {'weight':<8} "
      f"{'S_total':<10} {'centroid':<10} {'width':<10} {'n_eff':<8}")
for r in rep_results:
    print(f"({r['p']},{r['q']}){'':<3} {r['dim']:<5} {r['k']:<8.4f} "
          f"{r['block']:<6} {r.get('weight', 0):<8.4f} "
          f"{r['total_strength']:<10.6f} {r['centroid']:<10.6f} "
          f"{r['width']:<10.6f} {r['n_eff_pairs']:<8.3f}")
print()

# ==============================================================================
# SECTION 9: Group by wavenumber k and compute the hose-count exponent
# ==============================================================================
#
# At each unique k = sqrt(C_2), sum the pair-transfer strength and effective
# pair modes from all reps at that k (conjugate pairs are at the same k).

print("WAVENUMBER-GROUPED PAIR TRANSFER")
print("-" * 78)

k_data = {}
for r in rep_results:
    k_val = round(r['k'], 4)
    if k_val == 0:
        continue
    if k_val not in k_data:
        k_data[k_val] = {
            'k': r['k'], 'S_total': 0, 'n_eff_sum': 0,
            'centroid_weighted': 0, 'width_max': 0,
            'reps': [], 'dim_total': 0,
        }
    k_data[k_val]['S_total'] += r['total_strength']
    k_data[k_val]['n_eff_sum'] += r['n_eff_pairs']
    k_data[k_val]['centroid_weighted'] += r['total_strength'] * r['centroid']
    k_data[k_val]['width_max'] = max(k_data[k_val]['width_max'], r['width'])
    k_data[k_val]['reps'].append(f"({r['p']},{r['q']})")
    k_data[k_val]['dim_total'] += r['dim']

# Compute weighted centroids
for kv in k_data:
    d = k_data[kv]
    if d['S_total'] > 0:
        d['centroid'] = d['centroid_weighted'] / d['S_total']
    else:
        d['centroid'] = 0

k_sorted = sorted(k_data.keys())
k_arr = np.array([k_data[ki]['k'] for ki in k_sorted])
S_total_arr = np.array([k_data[ki]['S_total'] for ki in k_sorted])
n_eff_arr = np.array([k_data[ki]['n_eff_sum'] for ki in k_sorted])
centroid_arr = np.array([k_data[ki]['centroid'] for ki in k_sorted])
width_arr = np.array([k_data[ki]['width_max'] for ki in k_sorted])
dim_arr = np.array([k_data[ki]['dim_total'] for ki in k_sorted])

print(f"{'k':<10} {'S_total':<12} {'n_eff':<10} {'centroid':<12} {'width':<10} "
      f"{'dim':<6} {'reps':<25}")
for ki in k_sorted:
    d = k_data[ki]
    print(f"{d['k']:<10.4f} {d['S_total']:<12.6f} {d['n_eff_sum']:<10.3f} "
          f"{d['centroid']:<12.6f} {d['width_max']:<10.6f} "
          f"{d['dim_total']:<6} {' '.join(d['reps']):<25}")
print()

# Hose count from the spectral function: n_hose(k)
# This is the MAIN result that upgrades W1-2.
# Method: n_eff from the exact pair-transfer spectral function
# This counts how many independent pair-creation channels carry
# significant strength at each k.

# Also compute from the integrated strength directly:
# The pair-transfer sum rule for each block gives the TOTAL pair modes.
# The fragmentation tells us how many are ACTIVE.

print("HOSE COUNT FROM PAIR-TRANSFER SPECTRAL FUNCTION")
print("-" * 78)

# Three hose counting methods:
# Method A: n_eff from 1/e criterion on the block spectral function
# Method B: Integrated strength S_total(k) as effective pair count
# Method C: dim/2 (raw, for comparison with W1-2)

n_hose_A = n_eff_arr  # From per-rep effective pair modes
n_hose_B = S_total_arr  # Integrated strength = sum rule
n_hose_C = dim_arr / 2.0  # Raw Kramers pair count

print(f"{'k':<10} {'n_A (eff)':<12} {'n_B (sum rule)':<16} {'n_C (dim/2)':<14}")
for i in range(len(k_arr)):
    print(f"{k_arr[i]:<10.4f} {n_hose_A[i]:<12.3f} {n_hose_B[i]:<16.6f} {n_hose_C[i]:<14.1f}")
print()

# Power-law fit: n_hose(k) ~ A * k^alpha
from scipy.optimize import curve_fit

def power_law(k, A, alpha):
    return A * k**alpha

fit_results = {}
for label, n_data in [('n_eff (1/e)', n_hose_A),
                       ('sum rule', n_hose_B),
                       ('dim/2', n_hose_C)]:
    try:
        mask = (k_arr > 0) & (n_data > 0)
        popt, pcov = curve_fit(power_law, k_arr[mask], n_data[mask],
                               p0=[1.0, 1.0], maxfev=10000)
        perr = np.sqrt(np.diag(pcov))

        residuals = n_data[mask] - power_law(k_arr[mask], *popt)
        ss_res = np.sum(residuals**2)
        ss_tot = np.sum((n_data[mask] - np.mean(n_data[mask]))**2)
        r2 = 1 - ss_res / ss_tot if ss_tot > 0 else 0

        fit_results[label] = {
            'A': popt[0], 'alpha': popt[1],
            'A_err': perr[0], 'alpha_err': perr[1],
            'R2': r2,
        }
        print(f"  {label:<20}: alpha = {popt[1]:.4f} +/- {perr[1]:.4f}, "
              f"A = {popt[0]:.4f}, R^2 = {r2:.4f}")
    except Exception as e:
        print(f"  {label:<20}: FIT FAILED ({e})")
        fit_results[label] = {'alpha': np.nan, 'alpha_err': np.nan}

# Log-log fit for robustness
print("\nLog-log linear regression:")
for label, n_data in [('n_eff (1/e)', n_hose_A),
                       ('sum rule', n_hose_B),
                       ('dim/2', n_hose_C)]:
    mask = (k_arr > 0) & (n_data > 0)
    if np.sum(mask) >= 2:
        log_k = np.log(k_arr[mask])
        log_n = np.log(n_data[mask])
        coeffs = np.polyfit(log_k, log_n, 1)
        print(f"  {label:<20}: alpha_loglog = {coeffs[0]:.4f}")
        fit_results[label + '_loglog'] = {'alpha': coeffs[0]}

print()

# ==============================================================================
# SECTION 10: Centroid tilt analysis (n_s connection)
# ==============================================================================
#
# If the centroid omega_0(k) varies with k, the pair-transfer spectrum has
# a built-in tilt that could contribute to n_s. This is the Anderson-Bogoliubov
# dispersion analog: collective pair vibrations have a dispersion relation
# omega(k) that tilts the primordial spectrum.

print("CENTROID TILT ANALYSIS")
print("-" * 78)

# Fit centroid vs k
if np.all(centroid_arr > 0):
    # Linear fit: omega_0 = a + b*k
    coeffs_lin = np.polyfit(k_arr, centroid_arr, 1)
    tilt = coeffs_lin[0]
    intercept = coeffs_lin[1]

    # Fractional tilt across the k range
    delta_centroid = centroid_arr[-1] - centroid_arr[0]
    delta_k = k_arr[-1] - k_arr[0]
    frac_tilt = delta_centroid / np.mean(centroid_arr) if np.mean(centroid_arr) > 0 else 0

    print(f"  Centroid at k_min ({k_arr[0]:.3f}): omega_0 = {centroid_arr[0]:.6f} M_KK")
    print(f"  Centroid at k_max ({k_arr[-1]:.3f}): omega_0 = {centroid_arr[-1]:.6f} M_KK")
    print(f"  Linear tilt: d(omega_0)/dk = {tilt:.6f} M_KK per unit k")
    print(f"  Fractional tilt: delta(omega_0)/omega_0 = {frac_tilt:.4f} ({frac_tilt*100:.2f}%)")

    # Power-law fit: omega_0 ~ k^gamma
    if np.all(centroid_arr > 0):
        try:
            popt_c, pcov_c = curve_fit(power_law, k_arr, centroid_arr,
                                        p0=[1.0, 0.5], maxfev=10000)
            print(f"  Power-law: omega_0 ~ k^{popt_c[1]:.4f} (A = {popt_c[0]:.4f})")
            centroid_exponent = popt_c[1]
        except:
            centroid_exponent = 0

    # The centroid tilt contributes an additional term to n_s:
    # P(k) ~ k^{alpha} * omega_0(k)^{-2} (pair creation rate scales inversely with energy)
    # If omega_0 ~ k^gamma, then P(k) ~ k^{alpha - 2*gamma}
    # n_s - 1 = (alpha - 2*gamma) - beta

    alpha_eff = fit_results.get('sum rule', {}).get('alpha', 0)
    gamma = centroid_exponent if 'centroid_exponent' in dir() else 0
    ns_with_tilt = 1 + alpha_eff - 2 * gamma - 1.68  # beta = 1.68
    print(f"\n  Effective alpha_eff = alpha - 2*gamma = {alpha_eff:.4f} - 2*{gamma:.4f} = {alpha_eff - 2*gamma:.4f}")
    print(f"  n_s (with tilt) = 1 + {alpha_eff - 2*gamma:.4f} - 1.68 = {ns_with_tilt:.4f}")
else:
    tilt = 0
    frac_tilt = 0
    centroid_exponent = 0
    ns_with_tilt = 0
    print("  WARNING: Some centroid values are zero; tilt analysis skipped")

print()

# ==============================================================================
# SECTION 11: Width (fragmentation) analysis
# ==============================================================================
#
# The width sigma(k) of the spectral function tells us about fragmentation.
# A narrow spectral function (sigma << centroid) means the GPV is sharp:
# pair-transfer strength is concentrated in one peak.
# A broad spectral function (sigma ~ centroid) means fragmentation:
# strength is distributed among many states.
#
# Nuclear benchmark: in medium-mass nuclei, the GPV width is typically
# Gamma_GPV ~ 2-5 MeV out of centroid E_GPV ~ 10-15 MeV above the Fermi
# energy, giving sigma/centroid ~ 0.15-0.50 (Papers 23-25).

print("FRAGMENTATION ANALYSIS")
print("-" * 78)

for block_name in ['B1', 'B2', 'B3']:
    sb = S_block[block_name]
    frag_ratio = sb['width'] / sb['centroid'] if sb['centroid'] > 0 else 0

    print(f"\n  Block {block_name}:")
    print(f"    Centroid: {sb['centroid']:.6f} M_KK")
    print(f"    Width:    {sb['width']:.6f} M_KK")
    print(f"    sigma/centroid = {frag_ratio:.4f}")
    print(f"    Largest peak: {sb['max_frac']*100:.1f}% of total strength")
    print(f"    Peaks > 1/e of max: {sb['n_above_1e']}")

    if frag_ratio < 0.3:
        verdict = "SHARP GPV (nuclear-like, < 30%)"
    elif frag_ratio < 0.6:
        verdict = "MODERATE fragmentation (nuclear intermediate)"
    else:
        verdict = "STRONG fragmentation (deviates from nuclear GPV)"
    print(f"    Fragmentation verdict: {verdict}")

print()

# ==============================================================================
# SECTION 12: Comparison with W1-2 hose count
# ==============================================================================

print("COMPARISON WITH W1-2 HOSE COUNT")
print("-" * 78)

# W1-2 results (from s46_hose_count.npz)
try:
    d_w12 = np.load('s46_hose_count.npz', allow_pickle=True)
    k_w12 = d_w12['k_arr']
    n_gpv_w12 = d_w12['n_hose_gpv']
    n_raw_w12 = d_w12['n_hose_raw']
    alpha_w12 = float(d_w12['alpha_best'])

    print(f"  W1-2 alpha (GPV combined): {alpha_w12:.4f}")
    print(f"  W2-2 alpha (sum rule):     {fit_results.get('sum rule', {}).get('alpha', 'N/A')}")
    print(f"  W2-2 alpha (n_eff 1/e):    {fit_results.get('n_eff (1/e)', {}).get('alpha', 'N/A')}")
    print(f"  W2-2 alpha (dim/2):        {fit_results.get('dim/2', {}).get('alpha', 'N/A')}")
except:
    print("  W1-2 data not loaded; comparison skipped")

print()

# ==============================================================================
# SECTION 13: Nuclear benchmarks
# ==============================================================================
#
# Compare the fragmentation pattern with nuclear pair-transfer spectroscopy:
#
# Paper 03 (Bogoliubov / odd-even mass):
#   Odd-even staggering Delta^(3) ~ 1 MeV in medium-mass nuclei.
#   Pairing gap controls the spectral function width.
#
# Paper 13 (GCM):
#   Generator Coordinate Method: pair modes couple to collective coordinates.
#   The GPV in ^208Pb is at ~5 MeV above the Fermi energy with Gamma ~ 2 MeV.
#
# Paper 08 (pairing collapse):
#   At high angular momentum (or temperature), pairing collapses and the
#   spectral function changes from sharp GPV to fragmented.
#   Critical temperature: T_c/Delta ~ 0.34 (BCS), 0.57 (exact).
#
# For our system:
#   Delta_BCS ~ 0.77 M_KK (B2 gap)
#   E_GPV ~ centroid of B2 block
#   sigma_GPV ~ width of B2 block
#   The system is at T=0 (ground state) so pairing is NOT collapsed.

print("NUCLEAR BENCHMARKS")
print("-" * 78)

sb2 = S_block['B2']
Delta_BCS = Delta_0_GL  # 0.770 M_KK

# GPV energy in nuclear units
E_GPV = sb2['centroid']
sigma_GPV = sb2['width']

print(f"  B2 sector (dominant pairing):")
print(f"    BCS gap: Delta = {Delta_BCS:.4f} M_KK")
print(f"    GPV centroid: E_GPV = {E_GPV:.4f} M_KK")
print(f"    GPV width: sigma = {sigma_GPV:.4f} M_KK")
print(f"    E_GPV / Delta = {E_GPV/Delta_BCS:.4f}" if Delta_BCS > 0 else "    N/A")
print(f"    sigma / Delta = {sigma_GPV/Delta_BCS:.4f}" if Delta_BCS > 0 else "    N/A")
print()

# Nuclear comparison: E_GPV/Delta ~ 2-3, sigma/Delta ~ 0.5-1.5
# (Paper 24, Fortunato 2019: GPV in heavy nuclei)
print("  Nuclear GPV benchmarks (Papers 23-25):")
print("    E_GPV/Delta ~ 2-3 (medium-mass nuclei)")
print("    sigma/Delta ~ 0.5-1.5")
print("    GPV fraction of sum rule: 60-80%")
print()

ratio_E = E_GPV / Delta_BCS if Delta_BCS > 0 else 0
ratio_sigma = sigma_GPV / Delta_BCS if Delta_BCS > 0 else 0

if 1.5 < ratio_E < 4.0:
    e_verdict = "CONSISTENT with nuclear GPV"
else:
    e_verdict = "OUTSIDE nuclear range"

if 0.3 < ratio_sigma < 2.0:
    s_verdict = "CONSISTENT with nuclear fragmentation"
else:
    s_verdict = "OUTSIDE nuclear range"

print(f"  Our E_GPV/Delta = {ratio_E:.4f}: {e_verdict}")
print(f"  Our sigma/Delta = {ratio_sigma:.4f}: {s_verdict}")
print()

# ==============================================================================
# SECTION 14: Gate verdict
# ==============================================================================

print("=" * 78)
print("GATE VERDICT: RG-PAIR-TRANSFER-46")
print("=" * 78)

alpha_sum_rule = fit_results.get('sum rule', {}).get('alpha', np.nan)
alpha_sum_rule_err = fit_results.get('sum rule', {}).get('alpha_err', np.nan)
alpha_neff = fit_results.get('n_eff (1/e)', {}).get('alpha', np.nan)
alpha_neff_err = fit_results.get('n_eff (1/e)', {}).get('alpha_err', np.nan)
alpha_dim2 = fit_results.get('dim/2', {}).get('alpha', np.nan)

gate_verdict = "INFO"
gate_detail = (
    f"Pair-transfer spectral function computed for all 3 blocks. "
    f"B2 GPV fraction: {sb2['max_frac']*100:.1f}%. "
    f"Fragmentation sigma/Delta = {ratio_sigma:.3f}. "
    f"alpha(sum rule) = {alpha_sum_rule:.3f}, "
    f"alpha(n_eff) = {alpha_neff:.3f}. "
    f"Centroid tilt: {frac_tilt*100:.2f}%."
)

print(f"  Verdict: {gate_verdict}")
print(f"  Detail: {gate_detail}")
print()

# ==============================================================================
# SECTION 15: Save results
# ==============================================================================

# Collect all mode spectral function data
mode_centroids = np.array([S_mode[k]['centroid'] for k in range(N_modes)])
mode_widths = np.array([S_mode[k]['width'] for k in range(N_modes)])
mode_totals = np.array([S_mode[k]['total_strength'] for k in range(N_modes)])
mode_max_fracs = np.array([S_mode[k]['max_frac'] for k in range(N_modes)])
mode_npeaks = np.array([S_mode[k]['n_peaks'] for k in range(N_modes)])

# Block data
block_names = np.array(['B1', 'B2', 'B3'])
block_centroids = np.array([S_block[b]['centroid'] for b in ['B1', 'B2', 'B3']])
block_widths = np.array([S_block[b]['width'] for b in ['B1', 'B2', 'B3']])
block_totals = np.array([S_block[b]['total_strength'] for b in ['B1', 'B2', 'B3']])
block_max_fracs = np.array([S_block[b]['max_frac'] for b in ['B1', 'B2', 'B3']])
block_n_above_1e = np.array([S_block[b]['n_above_1e'] for b in ['B1', 'B2', 'B3']])

outfile = 's46_rg_pair_transfer.npz'
np.savez(outfile,
    # Gate
    gate_verdict=np.array([gate_verdict]),
    gate_detail=np.array([gate_detail]),
    # Model parameters
    mode_eps=mode_eps,
    mode_sector=np.array(mode_sector),
    alpha_star=alpha_star,
    E_GS=E_GS,
    V_full=V_full,
    mu=mu,
    # Ground state
    n_occ=n_occ,
    n_pairs_gs=n_pairs_gs,
    pair_number_dist=pair_number_dist,
    # Per-mode spectral functions
    mode_centroids=mode_centroids,
    mode_widths=mode_widths,
    mode_totals=mode_totals,
    mode_max_fracs=mode_max_fracs,
    mode_npeaks=mode_npeaks,
    # Per-block spectral functions
    block_names=block_names,
    block_centroids=block_centroids,
    block_widths=block_widths,
    block_totals=block_totals,
    block_max_fracs=block_max_fracs,
    block_n_above_1e=block_n_above_1e,
    # Representation-resolved
    k_arr=k_arr,
    S_total_arr=S_total_arr,
    n_eff_arr=n_eff_arr,
    centroid_arr=centroid_arr,
    width_arr=width_arr,
    dim_arr=dim_arr,
    # Power-law fits
    alpha_sum_rule=alpha_sum_rule,
    alpha_sum_rule_err=alpha_sum_rule_err if not np.isnan(alpha_sum_rule_err) else 0.0,
    alpha_neff=alpha_neff,
    alpha_neff_err=alpha_neff_err if not np.isnan(alpha_neff_err) else 0.0,
    alpha_dim2=alpha_dim2,
    # Centroid tilt
    centroid_tilt_slope=tilt,
    centroid_frac_tilt=frac_tilt,
    centroid_exponent=centroid_exponent,
    # Nuclear benchmarks
    E_GPV_over_Delta=ratio_E,
    sigma_over_Delta=ratio_sigma,
    GPV_fraction_B2=sb2['max_frac'],
    # Eigenvalue data for detailed analysis
    eigenvalues=eigenvalues,
    E_GS_val=E_GS,
)
print(f"Saved: {outfile}")

# ==============================================================================
# SECTION 16: Plot
# ==============================================================================

fig = plt.figure(figsize=(18, 14))
fig.suptitle('S46 RG-PAIR-TRANSFER-46: Pair Transfer Spectral Function',
             fontsize=14, fontweight='bold')

# Panel 1: Per-block spectral functions (3 panels stacked)
for bi, block_name in enumerate(['B1', 'B2', 'B3']):
    ax = fig.add_subplot(3, 3, bi + 1)
    sb = S_block[block_name]

    if len(sb['exc_energies']) > 0:
        # Sort by energy
        sorted_idx = np.argsort(sb['exc_energies'])
        E_sorted = sb['exc_energies'][sorted_idx]
        S_sorted = sb['strengths'][sorted_idx]

        # Plot as vertical lines (stick spectrum)
        ax.vlines(E_sorted, 0, S_sorted / sb['total_strength'],
                  colors='blue', linewidths=2, alpha=0.7)

        # Mark the centroid
        ax.axvline(sb['centroid'], color='red', linestyle='--', alpha=0.5,
                   label=f"centroid = {sb['centroid']:.3f}")

        # Mark the width
        ax.axvspan(sb['centroid'] - sb['width'], sb['centroid'] + sb['width'],
                   alpha=0.1, color='red', label=f'width = {sb["width"]:.3f}')

    ax.set_xlabel('Excitation energy (M_KK)')
    ax.set_ylabel('S(w) / S_total')
    ax.set_title(f'Block {block_name}: {len(blocks[block_name])} modes, '
                 f'GPV frac = {sb["max_frac"]*100:.1f}%')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

# Panel 4: Hose count vs k (comparison with W1-2)
ax = fig.add_subplot(3, 3, 4)
ax.loglog(k_arr, n_hose_C, 'ro-', label=f'dim/2 (alpha={alpha_dim2:.2f})', ms=8)
ax.loglog(k_arr, n_hose_B, 'bs-', label=f'Sum rule (alpha={alpha_sum_rule:.2f})', ms=8)
ax.loglog(k_arr, n_hose_A, 'g^-', label=f'n_eff 1/e (alpha={alpha_neff:.2f})', ms=8)

k_fit = np.linspace(k_arr.min() * 0.9, k_arr.max() * 1.1, 100)
ax.loglog(k_fit, 0.5 * k_fit**1.65, ':', color='gray', alpha=0.3, label='k^1.65 (Planck target)')
ax.set_xlabel('k = sqrt(C_2)')
ax.set_ylabel('Hose count')
ax.set_title('Pair Creation Channels vs Wavenumber')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)

# Panel 5: Centroid vs k (dispersion relation)
ax = fig.add_subplot(3, 3, 5)
ax.plot(k_arr, centroid_arr, 'ko-', ms=8, label='Pair-transfer centroid')
ax.fill_between(k_arr, centroid_arr - width_arr, centroid_arr + width_arr,
                alpha=0.2, color='blue', label='Width envelope')
if tilt != 0:
    k_fit_c = np.linspace(k_arr[0], k_arr[-1], 100)
    ax.plot(k_fit_c, np.polyval([tilt, intercept], k_fit_c),
            'r--', alpha=0.5, label=f'Linear fit: slope={tilt:.4f}')
ax.set_xlabel('k = sqrt(C_2)')
ax.set_ylabel('Centroid energy (M_KK)')
ax.set_title(f'Pair Dispersion: tilt = {frac_tilt*100:.2f}%')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)

# Panel 6: Ground state occupation numbers
ax = fig.add_subplot(3, 3, 6)
colors_mode = ['red'] + ['blue']*4 + ['green']*3
ax.bar(range(N_modes), n_occ, color=colors_mode, alpha=0.7)
ax.set_xlabel('Mode index')
ax.set_ylabel('Occupation <n_k>')
ax.set_title(f'Ground State: <N> = {n_pairs_gs:.3f} pairs')
ax.set_xticks(range(N_modes))
ax.set_xticklabels([f'{i}\n({mode_sector[i]})' for i in range(N_modes)], fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 7: Per-mode pair-transfer strength
ax = fig.add_subplot(3, 3, 7)
ax.bar(range(N_modes), mode_totals, color=colors_mode, alpha=0.7)
ax.set_xlabel('Mode index')
ax.set_ylabel('Total pair-transfer strength')
ax.set_title('Per-Mode Sum Rule')
ax.set_xticks(range(N_modes))
ax.set_xticklabels([f'{i}\n({mode_sector[i]})' for i in range(N_modes)], fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 8: Fragmentation ratio
ax = fig.add_subplot(3, 3, 8)
frag_ratios = [S_block[b]['width'] / S_block[b]['centroid']
               if S_block[b]['centroid'] > 0 else 0
               for b in ['B1', 'B2', 'B3']]
colors_block = ['red', 'blue', 'green']
bars = ax.bar(['B1', 'B2', 'B3'], frag_ratios, color=colors_block, alpha=0.7)
ax.axhline(y=0.3, color='gray', linestyle='--', alpha=0.5, label='Nuclear GPV lower bound')
ax.axhline(y=1.5, color='gray', linestyle=':', alpha=0.5, label='Nuclear upper bound')
ax.set_ylabel('sigma / centroid')
ax.set_title('Fragmentation Ratio by Block')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)

# Panel 9: Summary text
ax = fig.add_subplot(3, 3, 9)
ax.axis('off')
summary = (
    f"RG-PAIR-TRANSFER-46 RESULTS\n"
    f"{'=' * 42}\n\n"
    f"Model: 8 modes, 256-state Fock space\n"
    f"Coupling: alpha* = {alpha_star:.4f}\n"
    f"E_GS = {E_GS:.6f} M_KK\n\n"
    f"BLOCK SPECTRAL FUNCTIONS:\n"
    f"  B1: GPV frac={S_block['B1']['max_frac']*100:.0f}%, "
    f"sigma/w0={frag_ratios[0]:.3f}\n"
    f"  B2: GPV frac={S_block['B2']['max_frac']*100:.0f}%, "
    f"sigma/w0={frag_ratios[1]:.3f}\n"
    f"  B3: GPV frac={S_block['B3']['max_frac']*100:.0f}%, "
    f"sigma/w0={frag_ratios[2]:.3f}\n\n"
    f"HOSE COUNT EXPONENTS:\n"
    f"  alpha(sum rule) = {alpha_sum_rule:.3f}\n"
    f"  alpha(n_eff 1/e) = {alpha_neff:.3f}\n"
    f"  alpha(dim/2) = {alpha_dim2:.3f}\n\n"
    f"CENTROID TILT:\n"
    f"  delta(w0)/w0 = {frac_tilt*100:.2f}%\n"
    f"  gamma = {centroid_exponent:.3f}\n\n"
    f"Gate: {gate_verdict}"
)
ax.text(0.05, 0.95, summary, transform=ax.transAxes,
        fontsize=9, verticalalignment='top', fontfamily='monospace',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.tight_layout()
plt.savefig('s46_rg_pair_transfer.png', dpi=150, bbox_inches='tight')
print(f"Saved: s46_rg_pair_transfer.png")
print()
print("COMPUTATION COMPLETE")
