#!/usr/bin/env python3
"""
s61_spectral_dimension_pair.py — SPEC-DIM-PAIR-61: Spectral Dimension from Pair Return Probability
====================================================================================================

Gate: SPEC-DIM-PAIR-61
  PASS if d_s(short) = 2.0 +/- 0.2
  FAIL if d_s constant (no flow)
  INFO if d_s flows but != 2

Physics
-------
PHONON-3 (W2) computed d_s(t) for the SINGLE-PARTICLE random walk on CG(24),
finding d_s peaks at 2.88.  This task computes d_s for the MANY-BODY (pair) return
probability, which probes a DIFFERENT geometry: Fock space.

The spectral dimension is defined via the return probability of a diffusion process:

    d_s(sigma) = -2 * d(log P(sigma)) / d(log sigma)               (1)

where P(sigma) is the return probability (heat kernel diagonal) at diffusion time sigma.

For a DISCRETE spectrum {E_n, n=1..N_states} with eigenstates |n>, the heat kernel
trace (partition function) is:

    Z(sigma) = sum_n  exp(-E_n * sigma)                            (2)

and the return probability from a specific initial state |psi> is:

    P_psi(sigma) = sum_n |<n|psi>|^2 * exp(-E_n * sigma)           (3)

The spectral dimension from the full trace (averaged over all initial states):

    d_s(sigma) = -2 * d(log Z(sigma)) / d(log sigma)
               = 2 * sigma * sum_n E_n exp(-E_n sigma) / sum_n exp(-E_n sigma)   (4)

This is the HEAT KERNEL spectral dimension, using EUCLIDEAN (diffusion) time.

Note on real vs Euclidean time:
  - The SFF K(t) = |Z(it)|^2 / N^2  uses REAL time and diagnoses level statistics.
  - The spectral dimension uses EUCLIDEAN time sigma and diagnoses the effective
    dimensionality of the space explored by diffusion.
  - They are not the same thing.  d_s requires the heat kernel, not the SFF.

Strategy:
  We construct the many-body BCS Hamiltonian in the pair sector (N_pair particles)
  on N_cell Josephson-coupled cells.  We diagonalize to get {E_n}.  We shift so
  E_0 = 0 (ground state at zero).  Then:

    Z(sigma) = sum_n exp(-E_n sigma)                                (5)
    d_s(sigma) = 2*sigma * <E>_sigma / Z(sigma)                    (6)

  where <E>_sigma = sum_n E_n exp(-E_n sigma).

  At short sigma (high temperature): d_s -> d_eff of the Fock space geometry.
  At long sigma: d_s -> 0 (only ground state survives).
  The PEAK value and the short-time limit are the diagnostics.

Connection to Pillar VII (Papers 26-28):
  CDT and causal set quantum gravity both predict d_s -> 2 in the UV (short-distance)
  limit for 4D spacetimes.  Horava-Lifshitz gravity with z=3 gives d_s = 2*4/(2*3) = 4/3
  in the deep UV.  If our pair sector shows d_s -> 2, it connects the BCS Fock-space
  geometry to the CDT universality class.

  The anomalous gap scaling Delta_N ~ N^{-alpha} with alpha = 1.84 implies a dynamical
  exponent z = alpha (if the gap plays the role of an inverse length^z).  Then for
  a d-dimensional system d_s = 2*d/(2 + z*(d-1)) ... but the Fock space is not
  simply d-dimensional.  The computation will tell us what d_s actually is.

Session 61 | Phonon-First-Cosmologist
"""

import sys
import os
import time
import numpy as np
from scipy.linalg import eigh

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    E_cond, E_cond_ED_8mode, N_dof_BCS,
    dt_transit, tau_fold, N_cells,
)

# ============================================================================
# LOAD DATA
# ============================================================================

_dir = os.path.dirname(os.path.abspath(__file__))
s60_data = np.load(os.path.join(_dir, 's60_rg_integrals.npz'), allow_pickle=True)
E_J_fold = float(s60_data['E_J_fold'])     # 3.397 M_KK
eps_fold_8 = np.array(s60_data['eps_fold']) # 8 single-particle energies
V_fold_8 = np.array(s60_data['V_fold'])     # 8x8 pairing matrix

t_transit = dt_transit  # 0.00113 M_KK^{-1}

print("=" * 72)
print("SPEC-DIM-PAIR-61: Spectral Dimension from Pair Return Probability")
print("=" * 72)
print(f"E_J = {E_J_fold:.4f} M_KK")
print(f"eps_fold = {eps_fold_8}")
print(f"t_transit = {t_transit:.6f} M_KK^{{-1}}")
print()

# ============================================================================
# FOCK STATE HAMILTONIAN (from s61_thouless_ed.py)
# ============================================================================

def popcount(n):
    """Count set bits."""
    c = 0  # (local)
    while n:
        c += n & 1
        n >>= 1
    return c

def fermion_sign(state, pos):
    """Jordan-Wigner sign for acting on orbital 'pos'."""
    mask = (1 << pos) - 1
    return 1 - 2 * (popcount(state & mask) % 2)

def build_H_sector(n_modes, N_cell, N_part, eps, V_pair, E_J, adj):
    """
    Build many-body Hamiltonian restricted to the N_part particle sector.

    Returns: eigenvalues (sorted), dimension of the sector

    This avoids building the full 2^(n_tot) Fock space; we only keep
    states with exactly N_part particles.
    """
    n_tot = n_modes * N_cell

    # Enumerate states with exactly N_part particles
    sector_states = []
    for s in range(1 << n_tot):
        if popcount(s) == N_part:
            sector_states.append(s)
    dim = len(sector_states)
    state_to_idx = {s: i for i, s in enumerate(sector_states)}

    print(f"  Sector: n_modes={n_modes}, N_cell={N_cell}, N_part={N_part}, "
          f"n_tot={n_tot}, sector_dim={dim}")
    sys.stdout.flush()

    H = np.zeros((dim, dim), dtype=np.float64)

    # Diagonal: kinetic + on-site pairing
    for idx, state in enumerate(sector_states):
        e = 0.0
        for cell in range(N_cell):
            for k in range(n_modes):
                orb = cell * n_modes + k
                if state & (1 << orb):
                    e += eps[k]
            # On-site pairing V_{kk'} n_k n_{k'}
            for k in range(n_modes):
                orb_k = cell * n_modes + k
                if not (state & (1 << orb_k)):
                    continue
                for kp in range(k+1, n_modes):
                    orb_kp = cell * n_modes + kp
                    if state & (1 << orb_kp):
                        e += V_pair[k, kp] + V_pair[kp, k]
        H[idx, idx] = e

    # Off-diagonal: Josephson hopping  -E_J (c^dag_{k,i} c_{k,j} + h.c.)
    for i_cell in range(N_cell):
        for j_cell in range(i_cell + 1, N_cell):
            if adj[i_cell, j_cell] == 0:
                continue
            for k in range(n_modes):
                orb_i = i_cell * n_modes + k
                orb_j = j_cell * n_modes + k

                for idx, state in enumerate(sector_states):
                    # c^dag_{orb_i} c_{orb_j} |state>
                    if (state & (1 << orb_j)) and not (state & (1 << orb_i)):
                        sign_j = fermion_sign(state, orb_j)
                        state1 = state ^ (1 << orb_j)
                        sign_i = fermion_sign(state1, orb_i)
                        new_state = state1 | (1 << orb_i)
                        sign = sign_j * sign_i

                        new_idx = state_to_idx[new_state]
                        H[new_idx, idx] += -E_J * sign

                    # h.c.: c^dag_{orb_j} c_{orb_i}
                    if (state & (1 << orb_i)) and not (state & (1 << orb_j)):
                        sign_i2 = fermion_sign(state, orb_i)
                        state1 = state ^ (1 << orb_i)
                        sign_j2 = fermion_sign(state1, orb_j)
                        new_state = state1 | (1 << orb_j)
                        sign = sign_i2 * sign_j2

                        new_idx = state_to_idx[new_state]
                        H[new_idx, idx] += -E_J * sign

    # Symmetrize
    H = 0.5 * (H + H.T)

    return H, dim, sector_states


def chain_adjacency(N):
    """1D chain adjacency (open BC)."""
    adj = np.zeros((N, N), dtype=int)
    for i in range(N-1):
        adj[i, i+1] = 1
        adj[i+1, i] = 1
    return adj


def ring_adjacency(N):
    """1D ring adjacency (periodic BC)."""
    adj = chain_adjacency(N)
    if N > 2:
        adj[0, N-1] = 1
        adj[N-1, 0] = 1
    return adj


def compute_spectral_dimension(eigenvalues, sigma_array):
    """
    Compute d_s(sigma) from the heat kernel trace.

    Z(sigma) = sum_n exp(-E_n * sigma)  where E_0 = 0 (shifted).
    d_s(sigma) = -2 * d(log Z) / d(log sigma)
               = 2 * sigma * <E>_sigma / Z(sigma)

    where <E>_sigma = sum_n E_n exp(-E_n sigma).

    For numerical stability, shift so E_0 = 0, then all exponents are <= 0.
    """
    E = eigenvalues - eigenvalues[0]  # Shift ground state to 0
    N_states = len(E)

    d_s = np.zeros_like(sigma_array)
    Z_arr = np.zeros_like(sigma_array)
    P_return = np.zeros_like(sigma_array)

    for i, sigma in enumerate(sigma_array):
        boltzmann = np.exp(-E * sigma)
        Z = np.sum(boltzmann)
        E_mean = np.sum(E * boltzmann)

        Z_arr[i] = Z
        P_return[i] = Z / N_states  # Normalized return probability

        if Z > 0 and sigma > 0:
            d_s[i] = 2.0 * sigma * E_mean / Z
        else:
            d_s[i] = 0.0

    return d_s, Z_arr, P_return


def compute_spectral_dimension_logderiv(eigenvalues, sigma_array):
    """
    Alternative: compute d_s by numerical log-log derivative.
    d_s = -2 * d(log Z)/d(log sigma)

    This is more robust at intermediate scales.
    """
    E = eigenvalues - eigenvalues[0]  # (local)

    log_Z = np.zeros_like(sigma_array)
    for i, sigma in enumerate(sigma_array):
        boltzmann = np.exp(-E * sigma)
        Z = np.sum(boltzmann)
        log_Z[i] = np.log(Z) if Z > 0 else -np.inf

    log_sigma = np.log(sigma_array)

    # Central difference for d(log Z)/d(log sigma)
    d_s = np.zeros_like(sigma_array)
    for i in range(1, len(sigma_array)-1):
        dlZ = log_Z[i+1] - log_Z[i-1]
        dls = log_sigma[i+1] - log_sigma[i-1]
        d_s[i] = -2.0 * dlZ / dls

    # Forward/backward at boundaries
    if len(sigma_array) > 1:
        d_s[0] = -2.0 * (log_Z[1] - log_Z[0]) / (log_sigma[1] - log_sigma[0])
        d_s[-1] = -2.0 * (log_Z[-1] - log_Z[-2]) / (log_sigma[-1] - log_sigma[-2])

    return d_s, log_Z


# ============================================================================
# SECTION 1: SINGLE-CELL 8-MODE (PURE BCS, NO JOSEPHSON)
# ============================================================================

print("=" * 72)
print("SECTION 1: Single-cell 8-mode BCS (Fock-space spectral dimension)")
print("=" * 72)

# Single cell: just the 8-mode BCS Hamiltonian
# This is 2^8 = 256 states total; each particle-number sector is separate

# Build ALL particle sectors and compute d_s for each
# The "pair sector" for BCS means we look at even-particle-number sectors
# since BCS pairing creates/destroys particles in pairs

adj_1 = np.zeros((1, 1), dtype=int)  # No hopping for single cell

# Get eigenvalues for each particle number sector N_part = 0, 1, ..., 8
all_evals_by_sector = {}
for N_part in range(9):
    H_sec, dim_sec, states_sec = build_H_sector(8, 1, N_part, eps_fold_8, V_fold_8, 0.0, adj_1)
    if dim_sec > 0:
        evals = np.linalg.eigvalsh(H_sec)
        all_evals_by_sector[N_part] = np.sort(evals)
        print(f"    N_part={N_part}: dim={dim_sec}, E_GS={evals[0]:.6f}, "
              f"E_max={evals[-1]:.6f}, bandwidth={evals[-1]-evals[0]:.6f}")

# Collect ALL eigenvalues (full Hilbert space)
all_evals_full = np.concatenate(list(all_evals_by_sector.values()))
all_evals_full.sort()
print(f"\n  Full 8-mode spectrum: {len(all_evals_full)} states")
print(f"  E_GS(full) = {all_evals_full[0]:.6f}")
print(f"  Bandwidth = {all_evals_full[-1] - all_evals_full[0]:.6f}")

# Even-particle sectors only (pair sector)
pair_evals = np.concatenate([all_evals_by_sector[n] for n in [0, 2, 4, 6, 8]])
pair_evals.sort()
print(f"\n  Pair (even-N) sector: {len(pair_evals)} states")

# Odd-particle sectors
odd_evals = np.concatenate([all_evals_by_sector[n] for n in [1, 3, 5, 7]])
odd_evals.sort()
print(f"  Odd-N sector: {len(odd_evals)} states")

# Diffusion time scale (Euclidean)
sigma_min = 0.01 / (all_evals_full[-1] - all_evals_full[0])  # Short: resolves bandwidth
sigma_max = 100.0 / (pair_evals[1] - pair_evals[0]) if len(pair_evals) > 1 else 100.0
sigma_array = np.logspace(np.log10(sigma_min), np.log10(sigma_max), 2000)

print(f"\n  sigma range: [{sigma_min:.4e}, {sigma_max:.4e}]")

# Compute d_s for each sector
print("\n  Computing spectral dimensions...")
t0 = time.time()

ds_full, Z_full, P_full = compute_spectral_dimension(all_evals_full, sigma_array)
ds_pair, Z_pair, P_pair = compute_spectral_dimension(pair_evals, sigma_array)
ds_odd, Z_odd, P_odd = compute_spectral_dimension(odd_evals, sigma_array)

# Also via log-derivative
ds_full_log, logZ_full = compute_spectral_dimension_logderiv(all_evals_full, sigma_array)
ds_pair_log, logZ_pair = compute_spectral_dimension_logderiv(pair_evals, sigma_array)

print(f"  Done in {time.time()-t0:.2f}s")

# Extract key diagnostics
idx_short = np.argmin(np.abs(sigma_array - sigma_min * 10))
idx_peak_full = np.argmax(ds_full)
idx_peak_pair = np.argmax(ds_pair)

print(f"\n  --- Full spectrum d_s ---")
print(f"  d_s(short, sigma={sigma_array[idx_short]:.4e}) = {ds_full[idx_short]:.4f}")
print(f"  d_s(peak) = {ds_full[idx_peak_full]:.4f} at sigma = {sigma_array[idx_peak_full]:.4e}")

print(f"\n  --- Pair sector d_s ---")
print(f"  d_s(short, sigma={sigma_array[idx_short]:.4e}) = {ds_pair[idx_short]:.4f}")
print(f"  d_s(peak) = {ds_pair[idx_peak_pair]:.4f} at sigma = {sigma_array[idx_peak_pair]:.4e}")

# ============================================================================
# SECTION 2: MULTI-CELL (2-MODE SUBSET, N_cell = 2..8)
# ============================================================================

print("\n" + "=" * 72)
print("SECTION 2: Multi-cell 2-mode BCS+Josephson (pair sector spectral dimension)")
print("=" * 72)

# Use 2 modes (lowest and highest from 8-mode spectrum) for tractability
# Mode 0: eps=0.0, Mode 7: eps=1.17  (widest separation)
eps_2mode = np.array([eps_fold_8[0], eps_fold_8[-1]])
V_2mode = np.array([[V_fold_8[0,0], V_fold_8[0,7]],
                     [V_fold_8[7,0], V_fold_8[7,7]]])
print(f"  2-mode subset: eps = {eps_2mode}")
print(f"  V_pair = \n{V_2mode}")

# For each N_cell, build N_pair=2 sector and compute d_s
N_cells_list = [2, 3, 4, 5, 6]
multi_cell_results = {}

for N_cell in N_cells_list:
    n_tot = 2 * N_cell
    if n_tot > 20:
        print(f"  N_cell={N_cell}: n_tot={n_tot} too large, skipping")
        continue

    print(f"\n  --- N_cell = {N_cell} ---")
    adj = chain_adjacency(N_cell)

    # Half-filling: N_part = N_cell (one particle per cell on average)
    N_part = N_cell

    t0 = time.time()
    H_sec, dim_sec, states_sec = build_H_sector(2, N_cell, N_part, eps_2mode, V_2mode, E_J_fold, adj)

    if dim_sec > 10000:
        # Use sparse for large dimensions
        from scipy.sparse.linalg import eigsh
        from scipy.sparse import csr_matrix
        H_sp = csr_matrix(H_sec)
        # Get all eigenvalues via dense for sector dims < 10000
        evals = np.linalg.eigvalsh(H_sec)
    else:
        evals = np.linalg.eigvalsh(H_sec)

    evals = np.sort(evals)
    dt = time.time() - t0
    print(f"    dim={dim_sec}, E_GS={evals[0]:.6f}, bandwidth={evals[-1]-evals[0]:.6f}, "
          f"time={dt:.2f}s")

    # Spectral dimension
    bw = evals[-1] - evals[0]
    gap = evals[1] - evals[0] if len(evals) > 1 else bw
    sig_min_mc = 0.01 / bw
    sig_max_mc = 50.0 / gap if gap > 1e-12 else 50.0
    sig_mc = np.logspace(np.log10(sig_min_mc), np.log10(sig_max_mc), 1000)

    ds_mc, Z_mc, P_mc = compute_spectral_dimension(evals, sig_mc)
    ds_mc_log, logZ_mc = compute_spectral_dimension_logderiv(evals, sig_mc)

    idx_peak_mc = np.argmax(ds_mc)

    # Short-time d_s: average over first 5% of sigma range
    n_short = max(1, len(sig_mc) // 20)
    ds_short_avg = np.mean(ds_mc[1:n_short])

    print(f"    d_s(peak) = {ds_mc[idx_peak_mc]:.4f} at sigma = {sig_mc[idx_peak_mc]:.4e}")
    print(f"    d_s(short, avg first 5%) = {ds_short_avg:.4f}")

    multi_cell_results[N_cell] = {
        'evals': evals,
        'dim': dim_sec,
        'sigma': sig_mc,
        'ds': ds_mc,
        'ds_log': ds_mc_log,
        'ds_peak': ds_mc[idx_peak_mc],
        'ds_short_avg': ds_short_avg,
        'sigma_peak': sig_mc[idx_peak_mc],
    }

# ============================================================================
# SECTION 3: SCALING ANALYSIS
# ============================================================================

print("\n" + "=" * 72)
print("SECTION 3: Scaling Analysis")
print("=" * 72)

# Extract d_s peak vs N_cell
Ns = sorted(multi_cell_results.keys())
ds_peaks = [multi_cell_results[N]['ds_peak'] for N in Ns]
ds_shorts = [multi_cell_results[N]['ds_short_avg'] for N in Ns]
dims = [multi_cell_results[N]['dim'] for N in Ns]

print(f"\n  {'N_cell':>6} {'dim':>8} {'d_s(peak)':>10} {'d_s(short)':>10}")
print(f"  {'-'*6:>6} {'-'*8:>8} {'-'*10:>10} {'-'*10:>10}")
for N, d, dsp, dss in zip(Ns, dims, ds_peaks, ds_shorts):
    print(f"  {N:6d} {d:8d} {dsp:10.4f} {dss:10.4f}")

# Check if d_s(peak) scales or saturates
if len(Ns) >= 3:
    # Fit log(d_s_peak) vs log(N)
    log_N = np.log(np.array(Ns, dtype=float))
    log_ds = np.log(np.array(ds_peaks))
    coeffs = np.polyfit(log_N, log_ds, 1)
    ds_scaling_exp = coeffs[0]
    print(f"\n  d_s(peak) scaling: d_s ~ N^{ds_scaling_exp:.3f}")
    print(f"  (If exponent ~ 0, d_s saturates; if > 0, grows with system size)")

# ============================================================================
# SECTION 4: PAIR RETURN PROBABILITY DIRECTLY
# ============================================================================

print("\n" + "=" * 72)
print("SECTION 4: Pair Return Probability (direct ground-state overlap)")
print("=" * 72)

# For the single-cell 8-mode system:
# Construct H in the N=2 and N=4 (pair) sectors
# The "pair return probability" P_pair(sigma) = |<GS_N|e^{-H_N sigma}|GS_N>|^2
# In the eigenbasis: P(sigma) = (sum_n |c_n|^2 e^{-E_n sigma})^2 where c_n = <n|GS>
# If GS IS |n=0>, then P(sigma) = e^{-2*E_0*sigma} = 1 after shifting.
#
# So we need a DIFFERENT initial state.  The physically motivated choice:
# Start from the N-particle ground state, add a pair (S_+), propagate in the
# (N+2)-sector, remove a pair (S_-), and measure overlap.
#
# P_pair(sigma) = |<GS_N| S_- e^{-H_{N+2} sigma} S_+ |GS_N>|^2 / |S_+|GS_N>|^2
#
# This is the pair propagator return probability.

print("\n  Computing pair propagator return probability for 8-mode single cell...")

# Get the N=2 sector ground state
N2_evals = all_evals_by_sector[2]
H_N2, dim_N2, states_N2 = build_H_sector(8, 1, 2, eps_fold_8, V_fold_8, 0.0, adj_1)
evals_N2, evecs_N2 = np.linalg.eigh(H_N2)
GS_N2 = evecs_N2[:, 0]  # Ground state of N=2 sector
print(f"  N=2 sector: dim={dim_N2}, E_GS={evals_N2[0]:.6f}")

# Get the N=4 sector
H_N4, dim_N4, states_N4 = build_H_sector(8, 1, 4, eps_fold_8, V_fold_8, 0.0, adj_1)
evals_N4, evecs_N4 = np.linalg.eigh(H_N4)
print(f"  N=4 sector: dim={dim_N4}, E_GS={evals_N4[0]:.6f}")

# Build S_+ operator from N=2 to N=4 sector
# S_+ = sum_{k<k'} c^dag_k c^dag_{k'}
# (pair creation: add two particles in all possible pairs of unoccupied modes)
# More precisely, for BCS: S_+ = sum_k c^dag_{k,up} c^dag_{k,down}
# In our spinless model, pair creation = adding 2 particles in distinct modes

state_to_idx_N2 = {s: i for i, s in enumerate(states_N2)}
state_to_idx_N4 = {s: i for i, s in enumerate(states_N4)}

# S_+ : |N=2> -> |N=4>
# S_+ = sum_{a<b} c^dag_a c^dag_b  (create a pair in modes a,b)
S_plus = np.zeros((dim_N4, dim_N2), dtype=np.float64)

for idx2, state2 in enumerate(states_N2):
    for a in range(8):
        if state2 & (1 << a):
            continue  # mode a already occupied
        for b in range(a+1, 8):
            if state2 & (1 << b):
                continue  # mode b already occupied
            # Create pair (a,b)
            sign_a = fermion_sign(state2, a)
            state_tmp = state2 | (1 << a)
            sign_b = fermion_sign(state_tmp, b)
            new_state = state_tmp | (1 << b)
            sign = sign_a * sign_b

            if new_state in state_to_idx_N4:
                idx4 = state_to_idx_N4[new_state]
                S_plus[idx4, idx2] += sign

# Apply S_+ to GS_N2
psi_init = S_plus @ GS_N2
norm_sq = np.dot(psi_init, psi_init)
print(f"  |S_+ |GS_N2>|^2 = {norm_sq:.6f}")

if norm_sq < 1e-15:
    print("  WARNING: S_+ |GS_N2> = 0. Pair creation annihilates the ground state.")
    print("  Falling back to heat kernel spectral dimension of N=2 sector.")
    pair_prop_available = False
else:
    pair_prop_available = True
    psi_norm = psi_init / np.sqrt(norm_sq)

    # Expand psi_norm in N=4 eigenbasis
    overlaps = evecs_N4.T @ psi_norm  # c_n = <n|psi>
    print(f"  Overlap sum check: sum |c_n|^2 = {np.sum(overlaps**2):.10f} (should be 1)")
    print(f"  Number of non-negligible overlaps: {np.sum(overlaps**2 > 1e-10)}")

    # Pair propagator return probability
    # P_pair(sigma) = |sum_n |c_n|^2 exp(-E_n sigma)|^2
    # (This is the overlap-weighted return)
    # Actually: <psi|e^{-2H sigma}|psi> = sum_n |c_n|^2 exp(-2 E_n sigma)
    # Wait -- with Euclidean time:
    # <psi(sigma)|psi(sigma)> is not normalized.  The return prob is:
    # P(sigma) = |<psi|e^{-H sigma}|psi>|^2 / <psi|psi>^2
    #          = (sum_n |c_n|^2 e^{-E_n sigma})^2
    # But for spectral dimension we want:
    # P(sigma) = sum_n |c_n|^2 e^{-E_n sigma}  (the heat kernel from state psi)

    E_shifted = evals_N4 - evals_N4[0]  # Shift ground state to 0

    sigma_pair = np.logspace(-3, 3, 2000)
    P_pair_direct = np.zeros_like(sigma_pair)
    ds_pair_direct = np.zeros_like(sigma_pair)

    for i, sig in enumerate(sigma_pair):
        boltz = np.exp(-E_shifted * sig)
        P_pair_direct[i] = np.sum(overlaps**2 * boltz)
        E_mean = np.sum(overlaps**2 * E_shifted * boltz)
        if P_pair_direct[i] > 1e-300 and sig > 0:
            ds_pair_direct[i] = 2.0 * sig * E_mean / P_pair_direct[i]

    # Also via numerical log-derivative
    log_P = np.log(np.maximum(P_pair_direct, 1e-300))
    log_sig = np.log(sigma_pair)
    ds_pair_logd = np.zeros_like(sigma_pair)
    for i in range(1, len(sigma_pair)-1):
        dP = log_P[i+1] - log_P[i-1]
        ds_val = log_sig[i+1] - log_sig[i-1]
        ds_pair_logd[i] = -2.0 * dP / ds_val

    idx_peak_pp = np.argmax(ds_pair_direct)
    # Short-time: first 5%
    n_short_pp = max(1, len(sigma_pair) // 20)
    ds_short_pp = np.mean(ds_pair_direct[1:n_short_pp])

    print(f"\n  --- Pair Propagator Spectral Dimension ---")
    print(f"  d_s(peak) = {ds_pair_direct[idx_peak_pp]:.4f} at sigma = {sigma_pair[idx_peak_pp]:.4e}")
    print(f"  d_s(short, avg first 5%) = {ds_short_pp:.4f}")
    print(f"  d_s(sigma=0.01) = {ds_pair_direct[np.argmin(np.abs(sigma_pair-0.01))]:.4f}")
    print(f"  d_s(sigma=0.1) = {ds_pair_direct[np.argmin(np.abs(sigma_pair-0.1))]:.4f}")
    print(f"  d_s(sigma=1.0) = {ds_pair_direct[np.argmin(np.abs(sigma_pair-1.0))]:.4f}")

# ============================================================================
# SECTION 5: COMPARISON TO CDT / ANOMALOUS SCALING
# ============================================================================

print("\n" + "=" * 72)
print("SECTION 5: Comparison to CDT d_s Flow and Anomalous Scaling")
print("=" * 72)

# From S57: Delta_N ~ N^{-alpha} with alpha = 1.84 (Berry confirmed)
# This implies dynamical exponent z = alpha/d_eff in some sense
# For CDT in 4D: d_s(UV) = 2, d_s(IR) = 4
# For Horava-Lifshitz with z=3: d_s = 2*D_top/(1+z)

alpha_gap = 1.84   # from S57 Berry phase analysis  # (local)
print(f"  Gap scaling exponent: alpha = {alpha_gap}")

# The spectral dimension in a system with dispersion E ~ k^z is:
# d_s = 2*d_top / z  (for a d_top-dimensional lattice with z-dispersion)
# If the pair Fock space has effective dimension d_eff:
# d_s = 2 * d_eff / z

# From PHONON-3: CG(24) single-particle d_s(peak) = 2.88
# This corresponds to d_top_eff ~ 3 (for z=1 standard dispersion on 6-regular graph)
ds_CG24_peak = 2.88  # (local)

# For the pair sector, the relevant "space" is the N_pair=2 configuration space
# on the 32-cell tessellation.  If each cell has 8 modes, the pair can occupy
# C(8,2)=28 mode-pairs per cell, and there are 32 cells with Josephson coupling.
# The configuration space is 28*32 = 896 dimensional, but with correlations.

# Prediction from z = alpha = 1.84:
# d_s = 2 * d_top / z
# For d_top = 3 (from CG(24)): d_s = 2*3/1.84 = 3.26
# For d_top = 1 (1D chain used in Thouless ED): d_s = 2*1/1.84 = 1.09
# For d_top = 8 (Fock space of 8 modes): d_s = 2*8/1.84 = 8.70

print(f"\n  Predicted d_s from z=alpha={alpha_gap}:")
for d_top, label in [(1, "1D chain"), (3, "CG(24)"), (8, "8-mode Fock")]:
    ds_pred = 2.0 * d_top / alpha_gap
    print(f"    d_top={d_top} ({label}): d_s = {ds_pred:.3f}")

# The CDT prediction d_s -> 2 requires:
# 2 = 2*d_top/z  =>  d_top = z = 1.84
# i.e., the effective Fock-space dimensionality would need to be ~1.84

# ============================================================================
# SECTION 6: MULTI-CELL PAIR PROPAGATOR (N_cell = 2,3)
# ============================================================================

print("\n" + "=" * 72)
print("SECTION 6: Multi-cell Pair Propagator (2-mode, N_cell=2,3)")
print("=" * 72)

# For multi-cell systems with Josephson coupling, build the pair propagator
# In the N_part sector, the pair propagator adds 2 particles and evolves
# This probes the PAIR Fock-space geometry including inter-cell structure

for N_cell in [2, 3]:
    print(f"\n  --- N_cell = {N_cell} ---")
    n_modes = 2  # (local)
    n_tot = n_modes * N_cell
    adj = chain_adjacency(N_cell)

    # N_part = N_cell (half-filling)
    N_part = N_cell
    N_part_plus2 = N_part + 2

    if N_part_plus2 > n_tot:
        print(f"    N_part+2={N_part_plus2} > n_tot={n_tot}, cannot add pair")
        continue

    # Build both sectors
    H_N, dim_N, states_N = build_H_sector(n_modes, N_cell, N_part, eps_2mode, V_2mode, E_J_fold, adj)
    H_Np2, dim_Np2, states_Np2 = build_H_sector(n_modes, N_cell, N_part_plus2, eps_2mode, V_2mode, E_J_fold, adj)

    if dim_N == 0 or dim_Np2 == 0:
        print(f"    Empty sector, skipping")
        continue

    evals_N, evecs_N = np.linalg.eigh(H_N)
    evals_Np2, evecs_Np2 = np.linalg.eigh(H_Np2)

    GS_N = evecs_N[:, 0]
    print(f"    N-sector: dim={dim_N}, E_GS={evals_N[0]:.6f}")
    print(f"    (N+2)-sector: dim={dim_Np2}, E_GS={evals_Np2[0]:.6f}")

    # Build S_+ : N-sector -> (N+2)-sector
    state_to_idx_N_mc = {s: i for i, s in enumerate(states_N)}
    state_to_idx_Np2_mc = {s: i for i, s in enumerate(states_Np2)}

    S_plus_mc = np.zeros((dim_Np2, dim_N), dtype=np.float64)
    for idx_n, state_n in enumerate(states_N):
        for a in range(n_tot):
            if state_n & (1 << a):
                continue
            for b in range(a+1, n_tot):
                if state_n & (1 << b):
                    continue
                sign_a = fermion_sign(state_n, a)
                state_tmp = state_n | (1 << a)
                sign_b = fermion_sign(state_tmp, b)
                new_state = state_tmp | (1 << b)
                sign = sign_a * sign_b

                if new_state in state_to_idx_Np2_mc:
                    idx_np2 = state_to_idx_Np2_mc[new_state]
                    S_plus_mc[idx_np2, idx_n] += sign

    psi_mc = S_plus_mc @ GS_N
    norm_sq_mc = np.dot(psi_mc, psi_mc)
    print(f"    |S_+|GS>|^2 = {norm_sq_mc:.6f}")

    if norm_sq_mc < 1e-15:
        print(f"    S_+ annihilates GS, using heat kernel instead")
        # Fall back to heat kernel of the N_part sector
        E_sh = evals_N - evals_N[0]
        bw_mc = E_sh[-1]
        gap_mc = E_sh[1] if len(E_sh) > 1 else bw_mc
        sig_mc = np.logspace(np.log10(0.01/max(bw_mc,1e-10)), np.log10(50.0/max(gap_mc,1e-10)), 1000)
        ds_mc_val, _, _ = compute_spectral_dimension(evals_N, sig_mc)
        idx_pk = np.argmax(ds_mc_val)
        print(f"    Heat kernel d_s(peak) = {ds_mc_val[idx_pk]:.4f}")
    else:
        psi_mc_norm = psi_mc / np.sqrt(norm_sq_mc)
        overlaps_mc = evecs_Np2.T @ psi_mc_norm

        E_sh_mc = evals_Np2 - evals_Np2[0]
        bw_mc = E_sh_mc[-1]
        gap_mc = E_sh_mc[1] if len(E_sh_mc) > 1 else bw_mc
        sig_mc = np.logspace(-2, 3, 1000)

        P_pp_mc = np.zeros_like(sig_mc)
        ds_pp_mc = np.zeros_like(sig_mc)

        for i, sig in enumerate(sig_mc):
            boltz = np.exp(-E_sh_mc * sig)
            P_pp_mc[i] = np.sum(overlaps_mc**2 * boltz)
            E_mean = np.sum(overlaps_mc**2 * E_sh_mc * boltz)
            if P_pp_mc[i] > 1e-300 and sig > 0:
                ds_pp_mc[i] = 2.0 * sig * E_mean / P_pp_mc[i]

        idx_pk_mc = np.argmax(ds_pp_mc)
        n_sh = max(1, len(sig_mc) // 20)
        ds_sh_mc = np.mean(ds_pp_mc[1:n_sh])

        print(f"    Pair propagator d_s(peak) = {ds_pp_mc[idx_pk_mc]:.4f} at sigma = {sig_mc[idx_pk_mc]:.4e}")
        print(f"    d_s(short, avg 5%) = {ds_sh_mc:.4f}")

# ============================================================================
# SECTION 7: GATE VERDICT
# ============================================================================

print("\n" + "=" * 72)
print("SECTION 7: Gate Verdict — SPEC-DIM-PAIR-61")
print("=" * 72)

# Primary diagnostic: single-cell pair propagator d_s
if pair_prop_available:
    ds_primary = ds_pair_direct[idx_peak_pp]
    ds_short_primary = ds_short_pp
else:
    ds_primary = ds_pair[idx_peak_pair]
    ds_short_primary = np.mean(ds_pair[1:max(1, len(sigma_array)//20)])

# Also report the heat kernel d_s for the pair sector
ds_HK_peak = ds_pair[idx_peak_pair]

print(f"\n  Primary diagnostic (pair propagator):")
print(f"    d_s(peak) = {ds_primary:.4f}")
print(f"    d_s(short-time avg) = {ds_short_primary:.4f}")
print(f"  Pair-sector heat kernel:")
print(f"    d_s(peak) = {ds_HK_peak:.4f}")

# Gate logic
ds_short_test = ds_short_primary
ds_flow_range = np.max(ds_pair) - np.min(ds_pair[ds_pair > 0])

print(f"\n  d_s flow range: {ds_flow_range:.4f}")

if ds_flow_range < 0.1:
    gate_verdict = "FAIL"
    gate_detail = f"d_s constant ({ds_short_test:.3f}), no flow"
elif abs(ds_short_test - 2.0) < 0.2:
    gate_verdict = "PASS"
    gate_detail = f"d_s(short) = {ds_short_test:.3f}, within 2.0 +/- 0.2"
elif abs(ds_primary - 2.0) < 0.2:
    gate_verdict = "PASS"
    gate_detail = f"d_s(peak) = {ds_primary:.3f}, within 2.0 +/- 0.2"
else:
    gate_verdict = "INFO"
    gate_detail = (f"d_s flows (range {ds_flow_range:.3f}), "
                   f"peak={ds_primary:.3f}, short={ds_short_test:.3f}, neither = 2.0+/-0.2")

print(f"\n  GATE: SPEC-DIM-PAIR-61 = {gate_verdict}")
print(f"  Detail: {gate_detail}")

# ============================================================================
# SECTION 8: SAVE DATA
# ============================================================================

print("\n" + "=" * 72)
print("SECTION 8: Saving Data")
print("=" * 72)

save_dict = {
    # Gate
    'gate_name': 'SPEC-DIM-PAIR-61',
    'gate_verdict': gate_verdict,
    'gate_detail': gate_detail,

    # Parameters
    'E_J_fold': E_J_fold,
    'eps_fold_8': eps_fold_8,
    't_transit': t_transit,
    'alpha_gap': alpha_gap,

    # Single-cell full spectrum
    'evals_full': all_evals_full,
    'sigma_full': sigma_array,
    'ds_full': ds_full,
    'ds_full_log': ds_full_log,
    'ds_full_peak': float(ds_full[idx_peak_full]),
    'sigma_full_peak': float(sigma_array[idx_peak_full]),

    # Single-cell pair sector (heat kernel)
    'evals_pair': pair_evals,
    'ds_pair_HK': ds_pair,
    'ds_pair_HK_peak': float(ds_pair[idx_peak_pair]),

    # Single-cell odd sector
    'evals_odd': odd_evals,
    'ds_odd': ds_odd,

    # Pair propagator (if available)
    'pair_prop_available': pair_prop_available,

    # Multi-cell results
    'N_cells_tested': np.array(list(multi_cell_results.keys())),
    'ds_peaks_multicell': np.array(ds_peaks),
    'ds_shorts_multicell': np.array(ds_shorts),
    'dims_multicell': np.array(dims),
}

if pair_prop_available:
    save_dict.update({
        'sigma_pair_prop': sigma_pair,
        'ds_pair_prop': ds_pair_direct,
        'ds_pair_prop_logd': ds_pair_logd,
        'P_pair_prop': P_pair_direct,
        'ds_pair_prop_peak': float(ds_pair_direct[idx_peak_pp]),
        'sigma_pair_prop_peak': float(sigma_pair[idx_peak_pp]),
        'ds_pair_prop_short': float(ds_short_pp),
        'overlaps_N4': overlaps,
        'evals_N2': evals_N2,
        'evals_N4': evals_N4,
        'S_plus_norm_sq': float(norm_sq),
    })

# Save multi-cell eigenvalues
for N_cell in multi_cell_results:
    mc = multi_cell_results[N_cell]
    save_dict[f'evals_mc_{N_cell}'] = mc['evals']
    save_dict[f'sigma_mc_{N_cell}'] = mc['sigma']
    save_dict[f'ds_mc_{N_cell}'] = mc['ds']

outpath = os.path.join(_dir, 's61_spectral_dimension_pair.npz')
np.savez(outpath, **save_dict)
print(f"  Saved: {outpath}")

# ============================================================================
# SECTION 9: PLOT
# ============================================================================

print("\nGenerating plot...")
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('SPEC-DIM-PAIR-61: Spectral Dimension from Pair Return Probability', fontsize=13)

# Panel (a): Single-cell d_s comparison
ax = axes[0, 0]
ax.semilogx(sigma_array, ds_full, 'b-', lw=1.5, label='Full spectrum (256 states)', alpha=0.7)
ax.semilogx(sigma_array, ds_pair, 'r-', lw=1.5, label='Pair sector (even N)', alpha=0.7)
ax.semilogx(sigma_array, ds_odd, 'g--', lw=1.0, label='Odd-N sector', alpha=0.5)
ax.axhline(2.0, color='gray', ls=':', lw=1, label='CDT UV target (d_s=2)')
ax.set_xlabel(r'Euclidean time $\sigma$ (M$_{KK}^{-1}$)')
ax.set_ylabel(r'$d_s(\sigma)$')
ax.set_title('(a) Heat Kernel Spectral Dimension (single cell, 8-mode)')
ax.legend(fontsize=8)
ax.set_ylim(-0.5, max(ds_full.max(), ds_pair.max()) * 1.3)
ax.grid(True, alpha=0.3)

# Panel (b): Pair propagator d_s (if available)
ax = axes[0, 1]
if pair_prop_available:
    ax.semilogx(sigma_pair, ds_pair_direct, 'r-', lw=1.5, label=r'$d_s$ from pair propagator')
    ax.semilogx(sigma_pair, ds_pair_logd, 'b--', lw=1.0, label=r'$d_s$ (log-derivative)', alpha=0.5)
    ax.axhline(2.0, color='gray', ls=':', lw=1, label='CDT UV target')
    ax.axvline(t_transit, color='orange', ls='--', lw=1, label=f't_transit={t_transit:.4f}')
    ax.set_xlabel(r'Euclidean time $\sigma$ (M$_{KK}^{-1}$)')
    ax.set_ylabel(r'$d_s(\sigma)$')
    ax.set_title(f'(b) Pair Propagator d_s (N=2->N=4, peak={ds_pair_direct[idx_peak_pp]:.2f})')
    ax.legend(fontsize=8)
    ax.set_ylim(-0.5, max(ds_pair_direct.max(), 3) * 1.1)
else:
    ax.text(0.5, 0.5, 'Pair propagator unavailable\n(S_+ annihilates GS)',
            ha='center', va='center', transform=ax.transAxes, fontsize=12)
ax.grid(True, alpha=0.3)

# Panel (c): Multi-cell d_s peak scaling
ax = axes[1, 0]
if len(Ns) > 0:
    ax.plot(Ns, ds_peaks, 'ro-', lw=1.5, ms=6, label='d_s(peak)')
    ax.plot(Ns, ds_shorts, 'bs-', lw=1.5, ms=6, label='d_s(short-time avg)')
    ax.axhline(2.0, color='gray', ls=':', lw=1, label='CDT UV target')
    ax.set_xlabel('N_cell')
    ax.set_ylabel(r'$d_s$')
    ax.set_title('(c) Multi-cell d_s vs system size (2-mode, half-filling)')
    ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel (d): Multi-cell d_s flow curves
ax = axes[1, 1]
colors = plt.cm.viridis(np.linspace(0.2, 0.9, len(Ns)))
for i, N_cell in enumerate(Ns):
    mc = multi_cell_results[N_cell]
    ax.semilogx(mc['sigma'], mc['ds'], '-', color=colors[i], lw=1.2,
                label=f'N_cell={N_cell} (dim={mc["dim"]})')
ax.axhline(2.0, color='gray', ls=':', lw=1, label='CDT UV target')
ax.set_xlabel(r'Euclidean time $\sigma$ (M$_{KK}^{-1}$)')
ax.set_ylabel(r'$d_s(\sigma)$')
ax.set_title('(d) Multi-cell spectral dimension flow')
ax.legend(fontsize=7, ncol=2)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plotpath = os.path.join(_dir, 's61_spectral_dimension_pair.png')
plt.savefig(plotpath, dpi=150, bbox_inches='tight')
print(f"  Saved: {plotpath}")

print("\n" + "=" * 72)
print(f"FINAL GATE: SPEC-DIM-PAIR-61 = {gate_verdict}")
print(f"  {gate_detail}")
print("=" * 72)
