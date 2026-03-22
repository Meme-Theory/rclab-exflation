#!/usr/bin/env python3
"""
Session 46 W4-2: Band Inversion Berry Phase (BAND-INVERSION-BERRY-46)

Computes the Berry connection A = i <u_k(tau)|d/dtau|u_k(tau)> and Berry phase
around closed loops in (p,q,tau) space for the Dirac operator D_K(tau) on
Jensen-deformed SU(3).

Physical setup:
    At tau=0 (round SU(3)), eigenvalues are maximally degenerate.
    As tau increases, the Jensen deformation lifts degeneracies (band splitting).
    If bands invert (levels cross), the Berry phase accumulated along a closed
    path in parameter space equals pi, signaling topologically protected pair
    creation -- producing exactly one pair per Chern sector per transit.

    Berry connection:  A_n(tau) = i <u_n(tau)| d/dtau |u_n(tau)>
    Berry phase:       gamma_n = oint A_n(tau) dtau

    For a discrete tau grid, we use the gauge-invariant formula:
        gamma_n = -Im sum_{j} log <u_n(tau_j) | u_n(tau_{j+1})>
    which is insensitive to the arbitrary phase choice of each eigenvector.

Mathematical structure:
    D_K(tau) is anti-Hermitian; H(tau) = i*D_K(tau) is Hermitian.
    Eigenstates |u_n(tau)> from scipy.linalg.eigh are real-orthonormal.
    Berry phase for real eigenstates is quantized to 0 or pi (mod 2pi).

    This is PRECISELY the Z_2 invariant of the BDI symmetry class (T^2 = +1).
    The Berry phase being pi = topologically nontrivial = protected level crossing.

Formulas:
    (1) A_n(tau) = i <u_n(tau)| d/dtau |u_n(tau)>   [dimensionless, tau dimensionless]
    (2) gamma_n = -Im sum_j ln <u_n(tau_j)|u_n(tau_{j+1})>   [rad]
    (3) Pancharatnam overlap: O_j = <u_n(tau_j)|u_n(tau_{j+1})>   [dimensionless]
    (4) Wilson loop: W = prod_j O_j / |prod_j O_j|   [phase, |W|=1]

Dimensional check:
    - All quantities dimensionless (tau is dimensionless deformation parameter)
    - Berry phase in radians, quantized to 0 or pi for real eigenstates

Limiting cases:
    - tau -> 0 (round metric): maximal degeneracy, Berry phase undefined
      within degenerate subspace (use non-Abelian Berry phase there)
    - Single non-degenerate level: Berry phase = 0 (no partner to invert with)
    - Two-level avoided crossing: Berry phase = pi per branch

Citations:
    - Berry (1984): Proc. Roy. Soc. A 392, 45
    - Simon (1983): Phys. Rev. Lett. 51, 2167 (fiber bundle interpretation)
    - Volovik (2003): Universe in a Helium Droplet, Ch. 8 (topological protection)
    - Paper 10 (Volovik): emergent gauge fields from Berry phase in order parameter space
    - Paper 08 (Dirac cones): Berry phase pi at Dirac points in phononic crystals

Gate: BAND-INVERSION-BERRY-46 (Diagnostic)
    Report Berry phase per sector and whether any equals pi.

Input:  s44_dos_tau.npz, s45_acoustic_ns.npz, canonical_constants.py
Output: s46_berry_phase.{npz,png}

Author: tesla-resonance (Session 46 W4-2)
Date: 2026-03-15
"""

import sys
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.linalg import eigh as scipy_eigh

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from canonical_constants import tau_fold, M_KK_gravity, E_cond
from tier1_dirac_spectrum import (
    su3_generators, compute_structure_constants, build_cliff8,
    collect_spectrum_with_eigenvectors,
)

# ============================================================================
# 1. CONFIGURATION
# ============================================================================

print("=" * 72)
print("Session 46 W4-2: Band Inversion Berry Phase (BAND-INVERSION-BERRY-46)")
print("=" * 72)

# Dense tau grid for Berry phase computation
# 5 original tau points are too coarse -- Berry phase needs fine resolution
# to properly track adiabatic eigenstates. Use 40 points.
N_TAU = 40
tau_min = 0.001  # avoid exact tau=0 (maximal degeneracy)
tau_max = 0.19   # fold
tau_grid = np.linspace(tau_min, tau_max, N_TAU)

# Sector truncation
MAX_PQ_SUM = 3  # p+q <= 3 covers all 9 sectors with 992 eigenvalues

# Sectors in the computation
sectors_pq = [
    (0, 0), (1, 0), (0, 1), (1, 1),
    (2, 0), (0, 2), (3, 0), (0, 3), (2, 1)
]

# Branch classification
branch_map = {
    (0, 0): 'B1', (1, 0): 'B1', (0, 1): 'B1',
    (1, 1): 'B2',
    (2, 0): 'B3', (0, 2): 'B3', (3, 0): 'B3', (0, 3): 'B3', (2, 1): 'B3',
}

def dim_pq(p, q):
    return (p + 1) * (q + 1) * (p + q + 2) // 2

print(f"\n  tau grid: [{tau_min:.3f}, {tau_max:.3f}], N_tau = {N_TAU}")
print(f"  delta_tau = {tau_grid[1]-tau_grid[0]:.5f}")
print(f"  Sector truncation: p+q <= {MAX_PQ_SUM}")
print(f"  Number of sectors: {len(sectors_pq)}")
print(f"  Eigenvalues per sector at each tau:")
for (p, q) in sectors_pq:
    d = dim_pq(p, q)
    print(f"    ({p},{q}): dim={d}, D size={d*16}, eigenvalues={d*16}")

# ============================================================================
# 2. COMPUTE EIGENSTATES AT EACH TAU
# ============================================================================

print(f"\n{'='*72}")
print(f"COMPUTING D_K EIGENSTATES AT {N_TAU} TAU VALUES")
print(f"{'='*72}")

# Initialize algebra
gens = su3_generators()
f_abc = compute_structure_constants(gens)
gammas = build_cliff8()

# Store per-sector eigenvalues and eigenvectors at each tau
# sector_evals[i_sector][i_tau] = 1D array of eigenvalues
# sector_evecs[i_sector][i_tau] = 2D array (D_size x D_size) of eigenvectors
sector_evals = {pq: [] for pq in sectors_pq}
sector_evecs = {pq: [] for pq in sectors_pq}

for i_tau, tau in enumerate(tau_grid):
    if i_tau % 10 == 0 or i_tau == N_TAU - 1:
        print(f"\n  Computing tau = {tau:.4f} ({i_tau+1}/{N_TAU})...")
        verbose = (i_tau == 0)
    else:
        verbose = False

    sector_data, infra = collect_spectrum_with_eigenvectors(
        tau, gens, f_abc, gammas, max_pq_sum=MAX_PQ_SUM, verbose=verbose
    )

    # Map sector_data to our sector list
    sector_map = {(sd['p'], sd['q']): sd for sd in sector_data}

    for pq in sectors_pq:
        if pq in sector_map:
            sd = sector_map[pq]
            sector_evals[pq].append(sd['evals'])
            sector_evecs[pq].append(sd['evecs'])
        else:
            # This should not happen for p+q <= MAX_PQ_SUM
            raise RuntimeError(f"Sector {pq} not found at tau={tau}")

# Convert to arrays
for pq in sectors_pq:
    sector_evals[pq] = np.array(sector_evals[pq])  # (N_TAU, n_evals)
    # sector_evecs stays as list of arrays (each is D_size x D_size)

print(f"\n  Eigenvalue shapes per sector:")
for pq in sectors_pq:
    shape = sector_evals[pq].shape
    print(f"    ({pq[0]},{pq[1]}): evals shape = {shape}")

# ============================================================================
# 3. ADIABATIC STATE TRACKING (GAUGE FIXING)
# ============================================================================

print(f"\n{'='*72}")
print("ADIABATIC STATE TRACKING")
print("=" * 72)

# The eigenvectors from eigh have arbitrary signs at each tau.
# For Berry phase computation, we need a smooth gauge: each eigenstate
# must be continuously connected through tau.
#
# Strategy: maximize overlap |<u_n(tau_j)|u_n(tau_{j+1})>| by multiplying
# by sign = sgn(Re(<u_n(tau_j)|u_n(tau_{j+1})>)).
# For real eigenstates from eigh of real-symmetric H, this is a sign choice.
#
# For degenerate subspaces, we need the non-Abelian Berry phase (Wilson loop).
# We handle this by working within the full degenerate subspace.

def gauge_fix_eigenvectors(evecs_list, evals_list):
    """
    Fix the gauge of eigenvectors for smooth adiabatic tracking.

    For each eigenstate n, at each consecutive tau step, multiply by the
    sign of the overlap with the previous tau's eigenstate.

    Also detects level crossings by checking if the maximum overlap switches
    between different eigenstate indices.

    Args:
        evecs_list: list of N_TAU arrays, each (D, D) with columns = eigenvectors
        evals_list: (N_TAU, D) eigenvalue array

    Returns:
        fixed_evecs: list of gauge-fixed eigenvector arrays
        crossing_events: list of (tau_idx, n1, n2) for detected crossings
    """
    N = len(evecs_list)
    D = evecs_list[0].shape[1]
    fixed_evecs = [evecs_list[0].copy()]
    crossing_events = []

    for j in range(1, N):
        prev = fixed_evecs[j-1]
        curr = evecs_list[j].copy()

        # Compute overlap matrix O_{mn} = <prev_m | curr_n>
        O = prev.conj().T @ curr  # (D, D)

        # For each state m in prev, find the best match in curr
        # using maximum absolute overlap
        assignment = np.argmax(np.abs(O), axis=1)

        # Check for level crossings (non-identity permutation)
        if not np.all(assignment == np.arange(D)):
            # Detect which states swapped
            for m in range(D):
                if assignment[m] != m:
                    crossing_events.append((j, m, assignment[m]))

        # Apply gauge fixing: multiply each column by sign of its overlap
        for n in range(D):
            overlap = O[n, n]
            if np.abs(overlap) > 1e-10:
                phase = overlap / np.abs(overlap)
                curr[:, n] *= np.conj(phase)

        fixed_evecs.append(curr)

    return fixed_evecs, crossing_events


# Apply gauge fixing per sector
sector_fixed_evecs = {}
sector_crossings = {}

for pq in sectors_pq:
    evecs_list = sector_evecs[pq]
    evals_arr = sector_evals[pq]

    fixed, crossings = gauge_fix_eigenvectors(evecs_list, evals_arr)
    sector_fixed_evecs[pq] = fixed
    sector_crossings[pq] = crossings

    n_cross = len(crossings)
    if n_cross > 0:
        print(f"  Sector ({pq[0]},{pq[1]}): {n_cross} crossing events detected")
    else:
        print(f"  Sector ({pq[0]},{pq[1]}): no crossings (smooth adiabatic evolution)")

# ============================================================================
# 4. BERRY CONNECTION AND BERRY PHASE (GAUGE-INVARIANT)
# ============================================================================

print(f"\n{'='*72}")
print("BERRY PHASE COMPUTATION (GAUGE-INVARIANT FORMULA)")
print("=" * 72)

# Use the gauge-invariant discrete Berry phase formula:
#   gamma_n = -Im sum_{j=0}^{N-2} log <u_n(tau_j)|u_n(tau_{j+1})>
#
# For a CLOSED loop, add the overlap from tau_{N-1} back to tau_0.
# Our path is tau_min -> tau_max (one-way).
#
# For the OPEN path Berry phase (Zak phase analog):
#   gamma_n = -Im sum_{j} log <u_n(tau_j)|u_n(tau_{j+1})>
#
# For REAL eigenstates (from eigh of real-symmetric matrix):
#   <u_n(tau_j)|u_n(tau_{j+1})> is real, so Im(log(real)) = 0 or pi
#   Berry phase is quantized to 0 or pi per segment.
#   Total: sum of 0 or pi per segment = n*pi.

def compute_berry_phase_path(evecs_list, n_state):
    """
    Compute the Berry phase along the tau path for eigenstate n_state.

    Uses the gauge-invariant formula:
        gamma = -Im sum_j log <u_n(j)|u_n(j+1)>

    Also returns:
        - per-segment overlaps
        - Berry connection A(tau) = Im(log(<u(j)|u(j+1)>)) / dtau

    Args:
        evecs_list: list of N eigenvector arrays (D x D)
        n_state: index of eigenstate to track

    Returns:
        berry_phase: total Berry phase [rad]
        overlaps: array of <u_n(j)|u_n(j+1)> complex overlaps
        A_tau: Berry connection at each tau midpoint
    """
    N = len(evecs_list)
    overlaps = np.zeros(N - 1, dtype=complex)

    for j in range(N - 1):
        u_j = evecs_list[j][:, n_state]
        u_j1 = evecs_list[j+1][:, n_state]
        overlaps[j] = np.vdot(u_j, u_j1)  # <u_j|u_{j+1}>

    # Berry phase: -Im sum log(overlap)
    # Handle sign carefully for real overlaps
    log_overlaps = np.log(overlaps + 0j)  # ensure complex log
    berry_phase = -np.sum(log_overlaps.imag)

    # Berry connection: A(tau) at midpoints
    dtau = tau_grid[1] - tau_grid[0]
    A_tau = -log_overlaps.imag / dtau

    return berry_phase, overlaps, A_tau


def compute_wilson_loop(evecs_list, state_indices):
    """
    Compute the non-Abelian Wilson loop for a degenerate subspace.

    W = prod_j det(O_j)  where O_j is the overlap matrix restricted
    to the subspace indices.

    The Berry phase of the degenerate subspace is arg(det(W)).

    Args:
        evecs_list: list of N eigenvector arrays (D x D)
        state_indices: list of eigenstate indices in the degenerate subspace

    Returns:
        W: det of Wilson loop (complex number)
        berry_phase: arg(W) [rad]
    """
    N = len(evecs_list)
    n_sub = len(state_indices)
    W_det = 1.0 + 0j

    for j in range(N - 1):
        # Overlap matrix within subspace
        O_sub = np.zeros((n_sub, n_sub), dtype=complex)
        for mi, m in enumerate(state_indices):
            for ni, n in enumerate(state_indices):
                O_sub[mi, ni] = np.vdot(evecs_list[j][:, m], evecs_list[j+1][:, n])
        W_det *= np.linalg.det(O_sub)

    berry_phase = np.angle(W_det)
    return W_det, berry_phase


# Compute per-sector Berry phases
results = {}

for pq in sectors_pq:
    p, q = pq
    d = dim_pq(p, q)
    D_size = d * 16
    evals = sector_evals[pq]  # (N_TAU, D_size)
    evecs_list = sector_fixed_evecs[pq]

    print(f"\n  Sector ({p},{q}): dim={d}, D_size={D_size}")

    # --- Identify degenerate subspaces at tau_min ---
    evals_0 = evals[0]
    # Group eigenvalues by near-degeneracy
    deg_tol = 1e-6
    unique_evals = []
    deg_groups = []  # list of lists of indices

    visited = np.zeros(D_size, dtype=bool)
    for n in range(D_size):
        if visited[n]:
            continue
        group = [n]
        visited[n] = True
        for m in range(n+1, D_size):
            if not visited[m] and abs(evals_0[n] - evals_0[m]) < deg_tol:
                group.append(m)
                visited[m] = True
        unique_evals.append(evals_0[n])
        deg_groups.append(group)

    n_unique = len(unique_evals)
    print(f"    Unique eigenvalues at tau_min: {n_unique} / {D_size}")
    deg_sizes = [len(g) for g in deg_groups]
    print(f"    Degeneracy structure: {sorted(set(deg_sizes), reverse=True)}")

    # --- Berry phase for each individual eigenstate ---
    berry_phases = np.zeros(D_size)
    all_overlaps = []
    all_A_tau = []
    min_overlap_per_state = np.zeros(D_size)

    for n in range(D_size):
        bp, ovl, A = compute_berry_phase_path(evecs_list, n)
        berry_phases[n] = bp
        all_overlaps.append(ovl)
        all_A_tau.append(A)
        min_overlap_per_state[n] = np.min(np.abs(ovl))

    # --- Berry phase for degenerate subspaces (Wilson loop) ---
    wilson_phases = []
    for group in deg_groups:
        if len(group) == 1:
            wilson_phases.append(berry_phases[group[0]])
        else:
            W_det, w_phase = compute_wilson_loop(evecs_list, group)
            wilson_phases.append(w_phase)

    wilson_phases = np.array(wilson_phases)
    unique_evals = np.array(unique_evals)

    # --- Classify Berry phases ---
    # Quantized to 0 or pi?
    bp_mod_pi = np.abs(berry_phases) % np.pi
    n_zero = np.sum(bp_mod_pi < 0.1)
    n_pi = np.sum(np.abs(bp_mod_pi - np.pi) < 0.1)
    n_other = D_size - n_zero - n_pi

    # Same for Wilson phases
    wp_mod_pi = np.abs(wilson_phases) % np.pi
    n_wp_zero = np.sum(wp_mod_pi < 0.1)
    n_wp_pi = np.sum(np.abs(wp_mod_pi - np.pi) < 0.1)
    n_wp_other = len(wilson_phases) - n_wp_zero - n_wp_pi

    print(f"    Individual Berry phases:")
    print(f"      gamma ~ 0:   {n_zero} states")
    print(f"      gamma ~ pi:  {n_pi} states")
    print(f"      other:        {n_other} states")
    print(f"      min|overlap|: {min_overlap_per_state.min():.6f} "
          f"(adiabatic quality)")

    print(f"    Wilson loop Berry phases ({n_unique} degenerate subspaces):")
    print(f"      gamma ~ 0:   {n_wp_zero}")
    print(f"      gamma ~ pi:  {n_wp_pi}")
    print(f"      other:        {n_wp_other}")

    # Report any pi phases
    pi_states = np.where(np.abs(bp_mod_pi - np.pi) < 0.1)[0]
    if len(pi_states) > 0:
        print(f"    *** PI BERRY PHASES FOUND ***")
        for idx in pi_states[:10]:  # show first 10
            print(f"      state {idx}: gamma = {berry_phases[idx]:.6f} rad "
                  f"({berry_phases[idx]/np.pi:.4f} pi), "
                  f"eval = {evals[0, idx]:.6f}")

    # --- Check for band inversions ---
    # A band inversion occurs when the ordering of eigenvalues changes
    # between tau_min and tau_max
    order_0 = np.argsort(evals[0])
    order_f = np.argsort(evals[-1])
    n_inversions = np.sum(order_0 != order_f)
    print(f"    Band inversions (reordering): {n_inversions} / {D_size}")

    # Store results
    results[pq] = {
        'berry_phases': berry_phases,
        'wilson_phases': wilson_phases,
        'unique_evals': unique_evals,
        'deg_groups': deg_groups,
        'n_pi': n_pi,
        'n_zero': n_zero,
        'n_other': n_other,
        'n_wp_pi': n_wp_pi,
        'n_wp_zero': n_wp_zero,
        'n_inversions': n_inversions,
        'min_overlap': min_overlap_per_state.min(),
        'crossings': sector_crossings[pq],
        'all_A_tau': np.array(all_A_tau),
    }

# ============================================================================
# 5. AGGREGATE ANALYSIS
# ============================================================================

print(f"\n{'='*72}")
print("AGGREGATE BERRY PHASE RESULTS")
print("=" * 72)

print(f"\n{'Sector':>10s} | {'Branch':>6s} | {'D_size':>6s} | {'n_uniq':>6s} | "
      f"{'n(0)':>5s} | {'n(pi)':>5s} | {'n(oth)':>5s} | {'inversions':>10s} | "
      f"{'min|ovl|':>8s}")
print("-" * 90)

total_pi = 0
total_zero = 0
total_other = 0
total_inversions = 0

for pq in sectors_pq:
    p, q = pq
    d = dim_pq(p, q)
    D_size = d * 16
    r = results[pq]

    print(f"  ({p},{q}){' '*(6-len(f'({p},{q})'))} | {branch_map[pq]:>6s} | "
          f"{D_size:>6d} | {len(r['unique_evals']):>6d} | "
          f"{r['n_zero']:>5d} | {r['n_pi']:>5d} | {r['n_other']:>5d} | "
          f"{r['n_inversions']:>10d} | {r['min_overlap']:>8.6f}")

    total_pi += r['n_pi']
    total_zero += r['n_zero']
    total_other += r['n_other']
    total_inversions += r['n_inversions']

print("-" * 90)
print(f"  {'TOTAL':>8s} | {'':>6s} | {sum(dim_pq(p,q)*16 for p,q in sectors_pq):>6d} | "
      f"{'':>6s} | {total_zero:>5d} | {total_pi:>5d} | {total_other:>5d} | "
      f"{total_inversions:>10d} |")

# ============================================================================
# 6. BERRY PHASE AS TOPOLOGICAL PAIR CREATION INDICATOR
# ============================================================================

print(f"\n{'='*72}")
print("TOPOLOGICAL PAIR CREATION ANALYSIS")
print("=" * 72)

# The resonance structure: Each pi Berry phase represents a topological
# winding in the band structure -- an eigenvalue that has performed a
# half-twist relative to its partner. In the condensed matter analog,
# this is the Z_2 index that protects Kramers pairs.
#
# In the phonon-exflation context:
# - Transit takes tau from 0 -> tau_fold
# - Each pi Berry phase = one protected pair creation event
# - If the Berry phase counts match the BCS pair count (n_pairs ~ 59.8),
#   pair creation is topological, not thermal

n_pi_per_branch = {'B1': 0, 'B2': 0, 'B3': 0}
n_modes_per_branch = {'B1': 0, 'B2': 0, 'B3': 0}

for pq in sectors_pq:
    p, q = pq
    d = dim_pq(p, q)
    branch = branch_map[pq]
    n_pi_per_branch[branch] += results[pq]['n_pi']
    n_modes_per_branch[branch] += d * 16

print(f"\n  Berry phase pi count by BCS branch:")
for branch in ['B1', 'B2', 'B3']:
    print(f"    {branch}: {n_pi_per_branch[branch]} pi-phase states / "
          f"{n_modes_per_branch[branch]} total modes")

total_pi_weighted = 0
for pq in sectors_pq:
    p, q = pq
    d2 = dim_pq(p, q) ** 2  # Peter-Weyl multiplicity
    # Each pi Berry phase in sector (p,q) represents d(p,q) physical pair creations
    # because Peter-Weyl says the sector appears dim(p,q) times in L^2(SU(3))
    total_pi_weighted += results[pq]['n_pi'] * dim_pq(p, q)

print(f"\n  Total pi-phase states (unweighted): {total_pi}")
print(f"  Total pi-phase (PW-weighted: n_pi * dim(p,q)): {total_pi_weighted}")
print(f"  Comparison: BCS transit pair count = {59.8:.1f}")
print(f"  Ratio (PW-weighted pi / n_pairs): {total_pi_weighted / 59.8:.2f}")

# ============================================================================
# 7. BERRY CONNECTION PROFILE
# ============================================================================

print(f"\n{'='*72}")
print("BERRY CONNECTION A(tau) PROFILE")
print("=" * 72)

# Compute the total Berry curvature summed over all states per sector
tau_mid = 0.5 * (tau_grid[:-1] + tau_grid[1:])

# Report peak Berry connection location for each sector
for pq in sectors_pq:
    p, q = pq
    A_all = results[pq]['all_A_tau']  # (D_size, N_TAU-1)
    A_sum = np.sum(np.abs(A_all), axis=0)  # total |A| vs tau
    peak_idx = np.argmax(A_sum)
    peak_tau = tau_mid[peak_idx]
    peak_val = A_sum[peak_idx]
    print(f"  ({p},{q}): peak |A| at tau = {peak_tau:.4f}, "
          f"sum|A| = {peak_val:.4f}")

# ============================================================================
# 8. EIGENVALUE TRACKING PLOTS
# ============================================================================

print(f"\n{'='*72}")
print("GENERATING PLOTS")
print("=" * 72)

fig = plt.figure(figsize=(20, 16))
fig.suptitle("Berry Phase on Jensen-Deformed SU(3) (BAND-INVERSION-BERRY-46)",
             fontsize=13, fontweight='bold')

# Layout: 3 rows x 3 columns
# Row 1: Eigenvalue tracking for 3 largest sectors
# Row 2: Berry phase histograms + connection profiles
# Row 3: Summary

# --- Panel 1-3: Eigenvalue tracking for largest sectors ---
largest_sectors = [(2, 1), (0, 3), (3, 0)]  # D_size = 240, 160, 160
for panel_idx, pq in enumerate(largest_sectors[:3]):
    ax = fig.add_subplot(3, 3, panel_idx + 1)
    p, q = pq
    evals = sector_evals[pq]  # (N_TAU, D_size)
    D_size = evals.shape[1]

    # Color by Berry phase
    bp = results[pq]['berry_phases']
    for n in range(D_size):
        bp_val = np.abs(bp[n]) % np.pi
        if np.abs(bp_val - np.pi) < 0.1:
            color = 'red'
            alpha = 0.8
            lw = 1.0
        elif bp_val < 0.1:
            color = 'blue'
            alpha = 0.2
            lw = 0.3
        else:
            color = 'green'
            alpha = 0.4
            lw = 0.5
        ax.plot(tau_grid, evals[:, n], '-', color=color, alpha=alpha, lw=lw)

    ax.set_xlabel('$\\tau$')
    ax.set_ylabel('eigenvalue ($M_{KK}$)')
    ax.set_title(f'Sector ({p},{q}): {D_size} levels '
                 f'[{results[pq]["n_pi"]} $\\pi$-phase]')
    ax.set_xlim(tau_min, tau_max)

# Custom legend for eigenvalue panels
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], color='red', lw=1.5, label='$\\gamma = \\pi$'),
    Line2D([0], [0], color='blue', lw=1.0, alpha=0.5, label='$\\gamma = 0$'),
    Line2D([0], [0], color='green', lw=1.0, alpha=0.7, label='other'),
]
fig.axes[0].legend(handles=legend_elements, fontsize=7, loc='upper left')

# --- Panel 4: Berry phase distribution (histogram) ---
ax4 = fig.add_subplot(3, 3, 4)
all_bp = []
all_labels = []
for pq in sectors_pq:
    all_bp.extend(results[pq]['berry_phases'])
    all_labels.extend([f'({pq[0]},{pq[1]})'] * len(results[pq]['berry_phases']))
all_bp = np.array(all_bp)

# Histogram of Berry phases mod 2pi
bp_mod = all_bp % (2 * np.pi)
bp_mod[bp_mod > np.pi] -= 2 * np.pi
ax4.hist(bp_mod, bins=50, color='steelblue', edgecolor='black', alpha=0.7)
ax4.axvline(0, color='blue', ls='--', lw=1.5, label='$\\gamma = 0$')
ax4.axvline(np.pi, color='red', ls='--', lw=1.5, label='$\\gamma = \\pi$')
ax4.axvline(-np.pi, color='red', ls='--', lw=1.5)
ax4.set_xlabel('Berry phase $\\gamma$ (rad)')
ax4.set_ylabel('Count')
ax4.set_title('Berry Phase Distribution (all sectors)')
ax4.legend(fontsize=8)

# --- Panel 5: Berry phase by sector ---
ax5 = fig.add_subplot(3, 3, 5)
sector_labels = [f'({p},{q})' for p, q in sectors_pq]
n_pi_arr = [results[pq]['n_pi'] for pq in sectors_pq]
n_zero_arr = [results[pq]['n_zero'] for pq in sectors_pq]
n_other_arr = [results[pq]['n_other'] for pq in sectors_pq]

x = np.arange(len(sectors_pq))
w = 0.25
ax5.bar(x - w, n_zero_arr, w, label='$\\gamma=0$', color='steelblue')
ax5.bar(x, n_pi_arr, w, label='$\\gamma=\\pi$', color='crimson')
ax5.bar(x + w, n_other_arr, w, label='other', color='green')
ax5.set_xticks(x)
ax5.set_xticklabels(sector_labels, fontsize=7)
ax5.set_ylabel('Number of states')
ax5.set_title('Berry Phase Classification by Sector')
ax5.legend(fontsize=7)

# --- Panel 6: Berry connection A(tau) for selected sectors ---
ax6 = fig.add_subplot(3, 3, 6)
colors_sector = plt.cm.tab10(np.linspace(0, 1, len(sectors_pq)))
for idx, pq in enumerate(sectors_pq):
    A_all = results[pq]['all_A_tau']  # (D_size, N_TAU-1)
    A_mean = np.mean(np.abs(A_all), axis=0)
    ax6.plot(tau_mid, A_mean, '-', color=colors_sector[idx], lw=1.2,
             label=f'({pq[0]},{pq[1]})', alpha=0.8)
ax6.set_xlabel('$\\tau$')
ax6.set_ylabel('$\\langle |A(\\tau)| \\rangle$ per state')
ax6.set_title('Mean Berry Connection vs $\\tau$')
ax6.legend(fontsize=6, ncol=3)
ax6.grid(alpha=0.3)

# --- Panel 7: Band inversions by sector ---
ax7 = fig.add_subplot(3, 3, 7)
inv_arr = [results[pq]['n_inversions'] for pq in sectors_pq]
D_sizes = [dim_pq(p, q) * 16 for p, q in sectors_pq]
inv_frac = [inv_arr[i] / D_sizes[i] if D_sizes[i] > 0 else 0
            for i in range(len(sectors_pq))]
ax7.bar(x, inv_frac, color='darkorange', edgecolor='black', alpha=0.8)
ax7.set_xticks(x)
ax7.set_xticklabels(sector_labels, fontsize=7)
ax7.set_ylabel('Fraction of inverted levels')
ax7.set_title('Band Inversions (level reordering)')

# --- Panel 8: Minimum overlap (adiabatic quality) ---
ax8 = fig.add_subplot(3, 3, 8)
min_ovl_arr = [results[pq]['min_overlap'] for pq in sectors_pq]
ax8.bar(x, min_ovl_arr, color='teal', edgecolor='black', alpha=0.8)
ax8.set_xticks(x)
ax8.set_xticklabels(sector_labels, fontsize=7)
ax8.set_ylabel('min $|\\langle u(\\tau_j)|u(\\tau_{j+1})\\rangle|$')
ax8.set_title('Adiabatic Quality (per sector)')
ax8.axhline(0.9, color='red', ls=':', lw=1, label='threshold 0.9')
ax8.legend(fontsize=7)

# --- Panel 9: Summary text ---
ax9 = fig.add_subplot(3, 3, 9)
ax9.axis('off')

summary_text = (
    f"BAND-INVERSION-BERRY-46 SUMMARY\n"
    f"{'='*40}\n\n"
    f"tau range: [{tau_min:.3f}, {tau_max:.3f}], N_tau = {N_TAU}\n"
    f"Sectors: {len(sectors_pq)} (p+q <= {MAX_PQ_SUM})\n"
    f"Total eigenvalues: {sum(dim_pq(p,q)*16 for p,q in sectors_pq)}\n\n"
    f"Berry phase results:\n"
    f"  gamma = 0:  {total_zero}\n"
    f"  gamma = pi: {total_pi}\n"
    f"  other:      {total_other}\n\n"
    f"Total band inversions: {total_inversions}\n"
    f"PW-weighted pi count: {total_pi_weighted}\n"
    f"BCS pair count:       59.8\n"
    f"Ratio: {total_pi_weighted / 59.8 if total_pi_weighted > 0 else 0:.2f}\n\n"
    f"Gate: DIAGNOSTIC"
)

ax9.text(0.05, 0.95, summary_text, transform=ax9.transAxes,
         fontsize=9, verticalalignment='top', fontfamily='monospace',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.tight_layout()
plot_path = os.path.join(SCRIPT_DIR, "s46_berry_phase.png")
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"Saved plot: {plot_path}")
plt.close()

# ============================================================================
# 9. SAVE DATA
# ============================================================================

print(f"\n{'='*72}")
print("SAVING DATA")
print("=" * 72)

output_data = {
    'tau_grid': tau_grid,
    'tau_mid': tau_mid,
    'N_TAU': N_TAU,
    'MAX_PQ_SUM': MAX_PQ_SUM,
    'total_pi': total_pi,
    'total_zero': total_zero,
    'total_other': total_other,
    'total_inversions': total_inversions,
    'total_pi_weighted': total_pi_weighted,
}

for pq in sectors_pq:
    p, q = pq
    prefix = f's{p}{q}'
    r = results[pq]
    output_data[f'{prefix}_berry_phases'] = r['berry_phases']
    output_data[f'{prefix}_wilson_phases'] = r['wilson_phases']
    output_data[f'{prefix}_unique_evals'] = r['unique_evals']
    output_data[f'{prefix}_n_pi'] = r['n_pi']
    output_data[f'{prefix}_n_zero'] = r['n_zero']
    output_data[f'{prefix}_n_other'] = r['n_other']
    output_data[f'{prefix}_n_inversions'] = r['n_inversions']
    output_data[f'{prefix}_min_overlap'] = r['min_overlap']
    output_data[f'{prefix}_evals'] = sector_evals[pq]

    # Berry connection: mean over states
    A_all = r['all_A_tau']
    output_data[f'{prefix}_A_mean'] = np.mean(np.abs(A_all), axis=0)
    output_data[f'{prefix}_A_max'] = np.max(np.abs(A_all), axis=0)

out_path = os.path.join(SCRIPT_DIR, "s46_berry_phase.npz")
np.savez_compressed(out_path, **output_data)
print(f"Saved data: {out_path}")

# ============================================================================
# 10. FINAL REPORT
# ============================================================================

print(f"\n{'='*72}")
print("BAND-INVERSION-BERRY-46: FINAL REPORT")
print("=" * 72)

print(f"""
COMPUTATION:
  Berry connection A_n(tau) = i <u_n(tau)|d/dtau|u_n(tau)>
  Berry phase gamma_n = -Im sum_j log<u_n(j)|u_n(j+1)>  (gauge-invariant)
  tau grid: [{tau_min:.3f}, {tau_max:.3f}], {N_TAU} points
  Sectors: 9 sectors with p+q <= {MAX_PQ_SUM}
  Total eigenstates tracked: {sum(dim_pq(p,q)*16 for p,q in sectors_pq)}

RESULTS:
  Berry phase = 0:   {total_zero} states
  Berry phase = pi:  {total_pi} states
  Other:             {total_other} states
  Band inversions:   {total_inversions}

PER-SECTOR PI COUNTS:""")

for pq in sectors_pq:
    p, q = pq
    d = dim_pq(p, q)
    r = results[pq]
    print(f"  ({p},{q}) [{branch_map[pq]}]: {r['n_pi']} pi-phase / {d*16} states, "
          f"{r['n_inversions']} inversions, min|ovl|={r['min_overlap']:.4f}")

print(f"""
TOPOLOGICAL PAIR CREATION:
  PW-weighted pi count: {total_pi_weighted}
  BCS pair count (S38): 59.8
  Ratio: {total_pi_weighted / 59.8 if total_pi_weighted > 0 else 0:.2f}

PHYSICAL INTERPRETATION:
  Berry phase = pi signals topological band inversion.
  In the condensed matter analog, this is the Z_2 invariant of the BDI class.
  Each pi-phase state represents a protected level crossing during the
  tau transit. The pair creation at such points is topologically protected --
  it produces exactly one pair per transit regardless of the transit speed.

  Cross-domain connection:
  - Acoustic analog: pi Berry phase at Dirac cones in phononic crystals (Paper 08)
  - Superfluid analog: vortex-antivortex pair creation by topological unwinding (Paper 10, Volovik)
  - Electromagnetic analog: geometric phase of polarization around singular points (Berry 1984)

  The Berry phase counts quantify whether pair creation in the phonon-exflation
  transit is topological (alpha = 1 from Z_2) or dynamical (alpha from BCS).

Gate: BAND-INVERSION-BERRY-46 (DIAGNOSTIC)
Output: tier0-computation/s46_berry_phase.{{npz,png,py}}
""")
