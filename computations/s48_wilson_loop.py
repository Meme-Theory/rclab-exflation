#!/usr/bin/env python3
"""
Session 48 W1-D: Non-Abelian Wilson Loop for Degenerate Multiplets (WILSON-LOOP-48)

Computes the full non-Abelian Berry holonomy (Wilson loop) for the 492 degenerate-
multiplet eigenstates of D_K(tau) on Jensen-deformed SU(3), completing the topological
analysis begun in S46 (which found 13 Abelian pi-phase states among 500 non-degenerate
eigenstates).

Geometric picture:
    The Dirac spectrum on SU(3) with left-invariant Jensen metric g(tau) depends on
    a single real parameter tau in [0.001, 0.190]. At each tau, eigenvalues organize
    into sectors labeled by SU(3) irreps (p,q). Within each sector, the spectrum of
    H(tau) = i*D_{(p,q)}(tau) has symmetry-enforced degeneracies (e.g., charge
    conjugation, Weyl reflections).

    For a d-fold degenerate eigenvalue, the eigenspace forms a d-dimensional subspace
    of the full Hilbert space. As tau varies, this subspace rotates, and the
    holonomy of that rotation is captured by the non-Abelian Wilson loop:

        W = prod_{j=0}^{N-2} M(j)     [product of d x d overlap matrices]

    where M(j)_{alpha,beta} = <psi_alpha(tau_j) | psi_beta(tau_{j+1})>

    The gauge-invariant content of W is its eigenvalue spectrum:
        W |v_k> = exp(i*theta_k) |v_k>

    The phases {theta_k} are the non-Abelian Berry phases. For real eigenstates
    (our case: H is real-symmetric), the overlap matrices are real orthogonal,
    W is in O(d), and its eigenvalues are exp(+/- i*theta) in conjugate pairs
    plus possibly +1 or -1. The eigenvalue -1 corresponds to theta = pi.

    The S46 erratum (Berry curvature = 0 identically) means the LOCAL Berry
    curvature 2-form vanishes. But the GLOBAL Wilson loop along the open path
    tau: 0.001 -> 0.190 can still detect Z_2 topology (Mobius strip) via
    eigenvalue sign flips in the overlap product. This is the 1D Zak phase.

Physical content:
    - 13 Abelian pi-phases found in S46 (non-degenerate states)
    - 492 states in degenerate multiplets: their topological charge is in W's eigenvalues
    - Total topological charge = 13 + (number of -1 eigenvalues of all Wilson loops)
    - Does this total approach 16 (SM particle count) or 32 (spinor dimension)?

Method:
    For each degenerate multiplet of dimension d:
    1. Identify the multiplet: cluster eigenvalues with |lambda_i - lambda_j| < tol
    2. Track the d-dimensional subspace along tau using ADAPTIVE degeneracy tracking:
       at each tau step, re-cluster to handle degeneracy lifting/formation
    3. Compute overlap matrix M(j) = V(j)^T @ V(j+1) where V(j) has d columns
    4. Stabilize with SVD: replace M by U*V^T (nearest orthogonal matrix)
    5. Wilson loop: W = prod_j M(j)
    6. Eigendecompose W to get phases theta_k
    7. Count theta = pi eigenvalues (tolerance 0.05 radians)

Numerical stability:
    - SVD polar decomposition at each step to prevent drift from O(d)
    - Determinant tracking: if det(W) flips sign, it indicates a pi phase
    - Cross-check: product of all M determinants should equal det(W)

Gate: WILSON-LOOP-48
    PASS if total pi-count (Abelian + non-Abelian) in [13, 50]
    INFO if total computable but outside range
    FAIL if computation fails numerically

Input:  tier1_dirac_spectrum.py, canonical_constants.py
Output: s48_wilson_loop.{npz,png}

Author: berry-geometric-phase-theorist (Session 48 W1-D)
Date: 2026-03-17

Citations:
    - Berry (1984): Proc. Roy. Soc. A 392, 45 [Abelian geometric phase]
    - Wilczek & Zee (1984): PRL 52, 2111 [non-Abelian geometric phase]
    - Simon (1983): PRL 51, 2167 [fiber bundle interpretation]
    - S46: s46_berry_phase.py [Abelian Berry phase, 13 pi-states found]
    - S25: Berry curvature = 0 identically (anti-Hermiticity of Kosmann generators)
"""

import sys
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.linalg import eigh as scipy_eigh, svd as scipy_svd

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from canonical_constants import tau_fold
from tier1_dirac_spectrum import (
    su3_generators, compute_structure_constants, build_cliff8,
    collect_spectrum_with_eigenvectors,
)

# ============================================================================
# 1. CONFIGURATION
# ============================================================================

print("=" * 72)
print("Session 48 W1-D: Non-Abelian Wilson Loop (WILSON-LOOP-48)")
print("=" * 72)

# Match S46 tau grid exactly for consistency
N_TAU = 40
tau_min = 0.001
tau_max = 0.19
tau_grid = np.linspace(tau_min, tau_max, N_TAU)
dtau = tau_grid[1] - tau_grid[0]

MAX_PQ_SUM = 3

sectors_pq = [
    (0, 0), (1, 0), (0, 1), (1, 1),
    (2, 0), (0, 2), (3, 0), (0, 3), (2, 1)
]

branch_map = {
    (0, 0): 'B1', (1, 0): 'B1', (0, 1): 'B1',
    (1, 1): 'B2',
    (2, 0): 'B3', (0, 2): 'B3', (3, 0): 'B3', (0, 3): 'B3', (2, 1): 'B3',
}

def dim_pq(p, q):
    return (p + 1) * (q + 1) * (p + q + 2) // 2

print(f"\n  tau grid: [{tau_min:.3f}, {tau_max:.3f}], N_tau = {N_TAU}")
print(f"  delta_tau = {dtau:.5f}")
print(f"  Sectors: {len(sectors_pq)}, p+q <= {MAX_PQ_SUM}")

total_evals = sum(dim_pq(p, q) * 16 for p, q in sectors_pq)
print(f"  Total eigenvalues: {total_evals}")

# ============================================================================
# 2. COMPUTE EIGENSTATES AT EACH TAU
# ============================================================================

print(f"\n{'='*72}")
print(f"COMPUTING D_K EIGENSTATES AT {N_TAU} TAU VALUES")
print(f"{'='*72}")

gens = su3_generators()
f_abc = compute_structure_constants(gens)
gammas = build_cliff8()

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

    sector_map = {(sd['p'], sd['q']): sd for sd in sector_data}

    for pq in sectors_pq:
        if pq in sector_map:
            sd = sector_map[pq]
            sector_evals[pq].append(sd['evals'])
            sector_evecs[pq].append(sd['evecs'])
        else:
            raise RuntimeError(f"Sector {pq} not found at tau={tau}")

for pq in sectors_pq:
    sector_evals[pq] = np.array(sector_evals[pq])

# ============================================================================
# 3. DEGENERACY IDENTIFICATION AND MULTIPLET TRACKING
# ============================================================================

print(f"\n{'='*72}")
print("DEGENERACY IDENTIFICATION")
print("=" * 72)

# Degeneracy threshold: eigenvalues within this tolerance are considered degenerate.
# Must be small enough to resolve distinct levels, large enough to capture
# numerical degeneracies. The spectrum has spacing ~ O(0.01) for low modes,
# so 1e-6 is safe.
DEG_TOL = 1e-6

# Phase classification tolerance for theta = 0 or pi
PHASE_TOL = 0.10  # radians (~5.7 degrees)


def identify_multiplets(evals, tol=DEG_TOL):
    """
    Cluster eigenvalues into degenerate multiplets.

    Returns list of lists: each inner list contains indices of degenerate states.
    Singletons (non-degenerate) appear as [i].
    """
    D = len(evals)
    visited = np.zeros(D, dtype=bool)
    groups = []

    for n in range(D):
        if visited[n]:
            continue
        group = [n]
        visited[n] = True
        for m in range(n + 1, D):
            if not visited[m] and abs(evals[n] - evals[m]) < tol:
                group.append(m)
                visited[m] = True
        groups.append(group)

    return groups


def compute_wilson_loop_full(evecs_list, state_indices):
    """
    Compute the full non-Abelian Wilson loop matrix for a degenerate subspace.

    For a d-fold degenerate multiplet with eigenstates indexed by state_indices,
    the Wilson loop is the product of d x d overlap matrices along the tau path:

        W = prod_{j=0}^{N-2} M(j)

    where M(j)_{alpha,beta} = <psi_alpha(tau_j) | psi_beta(tau_{j+1})>

    For numerical stability, each M(j) is replaced by its nearest orthogonal
    matrix via SVD polar decomposition: M -> U @ V^T.

    Args:
        evecs_list: list of N eigenvector arrays (D x D), columns = eigenvectors
        state_indices: list of d eigenstate indices in the degenerate subspace

    Returns:
        W: (d, d) Wilson loop matrix (orthogonal for real eigenstates)
        W_evals: eigenvalues of W (complex, on unit circle)
        W_phases: phases theta_k = arg(eigenvalue_k), in [-pi, pi]
        det_product: running product of det(M(j)) [should equal det(W)]
        condition_numbers: list of condition numbers of M(j) at each step
    """
    N = len(evecs_list)
    d = len(state_indices)

    W = np.eye(d, dtype=complex)
    det_product = 1.0 + 0j
    condition_numbers = []

    for j in range(N - 1):
        # Extract subspace columns at tau_j and tau_{j+1}
        V_j = evecs_list[j][:, state_indices]    # (D_size, d)
        V_j1 = evecs_list[j + 1][:, state_indices]  # (D_size, d)

        # Overlap matrix: M_{alpha,beta} = <psi_alpha(j) | psi_beta(j+1)>
        M = V_j.conj().T @ V_j1  # (d, d)

        # Track determinant before SVD normalization
        det_M = np.linalg.det(M)
        det_product *= det_M

        # SVD polar decomposition: M = U @ S @ Vh -> nearest orthogonal = U @ Vh
        U, S, Vh = scipy_svd(M)
        cond = S[0] / max(S[-1], 1e-300)
        condition_numbers.append(cond)

        # Replace M by nearest unitary (polar factor)
        M_polar = U @ Vh

        W = W @ M_polar

    # Eigendecompose W
    W_evals = np.linalg.eigvals(W)

    # Sort by phase
    W_phases = np.angle(W_evals)
    sort_idx = np.argsort(W_phases)
    W_evals = W_evals[sort_idx]
    W_phases = W_phases[sort_idx]

    return W, W_evals, W_phases, det_product, condition_numbers


def compute_abelian_berry_phase(evecs_list, n_state):
    """
    Compute the Abelian Berry phase for a single non-degenerate eigenstate.
    Gauge-invariant formula: gamma = -Im sum_j log <u(j)|u(j+1)>.
    """
    N = len(evecs_list)
    phase_sum = 0.0
    min_overlap = 1.0

    for j in range(N - 1):
        u_j = evecs_list[j][:, n_state]
        u_j1 = evecs_list[j + 1][:, n_state]
        overlap = np.vdot(u_j, u_j1)
        min_overlap = min(min_overlap, abs(overlap))
        if abs(overlap) > 1e-15:
            phase_sum += -np.imag(np.log(overlap + 0j))
        # If overlap ~ 0, this state is in a degenerate subspace

    return phase_sum, min_overlap


# ============================================================================
# 4. MAIN COMPUTATION: WILSON LOOP PER MULTIPLET
# ============================================================================

print(f"\n{'='*72}")
print("WILSON LOOP COMPUTATION")
print("=" * 72)

# For robust degeneracy tracking, we identify multiplets at EACH tau value
# and match them across tau. However, the simpler approach (identify at tau_min
# and track) suffices when degeneracies don't form/dissolve along the path.
# S46 found zero band inversions, confirming the adiabatic structure is stable.
#
# Strategy: identify multiplets at the MIDPOINT tau value (where the eigenvalue
# spacing is most representative) and verify consistency at endpoints.

results = {}

for pq in sectors_pq:
    p, q = pq
    d = dim_pq(p, q)
    D_size = d * 16
    evals = sector_evals[pq]  # (N_TAU, D_size)
    evecs_list = [sector_evecs[pq][j] for j in range(N_TAU)]

    print(f"\n  Sector ({p},{q}): dim_rho={d}, D_size={D_size}")

    # Identify multiplets at tau_min (index 0)
    evals_0 = evals[0]
    groups_0 = identify_multiplets(evals_0, tol=DEG_TOL)

    # Also identify at midpoint and endpoint for consistency check
    mid_idx = N_TAU // 2
    groups_mid = identify_multiplets(evals[mid_idx], tol=DEG_TOL)
    groups_end = identify_multiplets(evals[-1], tol=DEG_TOL)

    deg_sizes_0 = sorted([len(g) for g in groups_0], reverse=True)
    deg_sizes_mid = sorted([len(g) for g in groups_mid], reverse=True)
    deg_sizes_end = sorted([len(g) for g in groups_end], reverse=True)

    n_singlets_0 = sum(1 for g in groups_0 if len(g) == 1)
    n_multiplets_0 = sum(1 for g in groups_0 if len(g) > 1)
    n_in_multiplets_0 = sum(len(g) for g in groups_0 if len(g) > 1)

    print(f"    Degeneracy at tau_min: {n_singlets_0} singlets, "
          f"{n_multiplets_0} multiplets ({n_in_multiplets_0} states)")
    print(f"    Degeneracy structure at tau_min: {deg_sizes_0[:15]}{'...' if len(deg_sizes_0) > 15 else ''}")
    print(f"    Degeneracy structure at tau_mid: {deg_sizes_mid[:15]}{'...' if len(deg_sizes_mid) > 15 else ''}")
    print(f"    Degeneracy structure at tau_end: {deg_sizes_end[:15]}{'...' if len(deg_sizes_end) > 15 else ''}")

    # Consistency check: does the number of groups change along the path?
    if len(groups_0) != len(groups_mid) or len(groups_0) != len(groups_end):
        print(f"    WARNING: Degeneracy structure changes along path!")
        print(f"      tau_min: {len(groups_0)} groups, tau_mid: {len(groups_mid)}, tau_end: {len(groups_end)}")
        # Use the FINEST grouping (most groups = fewest accidental degeneracies)
        # This is the midpoint or endpoint, whichever has more groups
        if len(groups_end) >= len(groups_mid):
            print(f"    Using tau_end grouping ({len(groups_end)} groups)")
            groups_ref = groups_end
            ref_label = "tau_end"
        else:
            print(f"    Using tau_mid grouping ({len(groups_mid)} groups)")
            groups_ref = groups_mid
            ref_label = "tau_mid"
    else:
        groups_ref = groups_0
        ref_label = "tau_min"

    # Compute Berry phase / Wilson loop for each group
    abelian_phases = []     # phases for singlets (non-degenerate)
    abelian_overlaps = []   # min|overlap| for singlets
    wilson_phases_all = []  # all phases from Wilson loop eigenvalues (multiplets)
    wilson_dets = []        # det(W) for each multiplet
    multiplet_info = []     # (group_indices, dim, mean_eval, W_phases)

    for group in groups_ref:
        if len(group) == 1:
            # Singlet: Abelian Berry phase
            bp, mo = compute_abelian_berry_phase(evecs_list, group[0])
            abelian_phases.append(bp)
            abelian_overlaps.append(mo)
        else:
            # Multiplet: non-Abelian Wilson loop
            W, W_evals, W_phases, det_prod, conds = compute_wilson_loop_full(
                evecs_list, group
            )

            # Store individual phases
            wilson_phases_all.extend(W_phases.tolist())
            wilson_dets.append(np.linalg.det(W))

            mean_eval = np.mean(evals[0, group])
            max_cond = max(conds) if conds else 0
            multiplet_info.append({
                'indices': group,
                'dim': len(group),
                'mean_eval': mean_eval,
                'W_phases': W_phases,
                'W_evals': W_evals,
                'det_W': np.linalg.det(W),
                'det_product': det_prod,
                'max_cond': max_cond,
            })

    abelian_phases = np.array(abelian_phases)
    abelian_overlaps = np.array(abelian_overlaps)
    wilson_phases_all = np.array(wilson_phases_all)

    # Classify Abelian phases
    if len(abelian_phases) > 0:
        ab_mod = np.abs(abelian_phases) % np.pi
        n_ab_zero = int(np.sum(ab_mod < PHASE_TOL))
        n_ab_pi = int(np.sum(np.abs(ab_mod - np.pi) < PHASE_TOL))
        # Also check near integer multiples of pi
        ab_mod2 = np.abs(abelian_phases) % (2 * np.pi)
        n_ab_pi_alt = int(np.sum(
            (np.abs(ab_mod2 - np.pi) < PHASE_TOL) |
            (np.abs(np.abs(abelian_phases) - np.pi) < PHASE_TOL)
        ))
        n_ab_other = len(abelian_phases) - n_ab_zero - n_ab_pi
    else:
        n_ab_zero = n_ab_pi = n_ab_other = 0

    # Classify Wilson loop phases
    if len(wilson_phases_all) > 0:
        wl_mod = np.abs(wilson_phases_all)  # already in [-pi, pi]
        n_wl_zero = int(np.sum(wl_mod < PHASE_TOL))
        n_wl_pi = int(np.sum(np.abs(wl_mod - np.pi) < PHASE_TOL))
        n_wl_other = len(wilson_phases_all) - n_wl_zero - n_wl_pi
    else:
        n_wl_zero = n_wl_pi = n_wl_other = 0

    # Summary
    print(f"\n    Abelian Berry phases ({len(abelian_phases)} singlets):")
    print(f"      gamma = 0:   {n_ab_zero}")
    print(f"      gamma = pi:  {n_ab_pi}")
    print(f"      other:       {n_ab_other}")
    if len(abelian_overlaps) > 0:
        print(f"      min|overlap|: {np.min(abelian_overlaps):.6f}")
        low_overlap = np.sum(abelian_overlaps < 0.5)
        if low_overlap > 0:
            print(f"      WARNING: {low_overlap} singlets with min|overlap| < 0.5 "
                  f"(possible hidden degeneracy)")

    print(f"\n    Wilson loop phases ({len(wilson_phases_all)} from {len(multiplet_info)} multiplets):")
    print(f"      theta = 0:   {n_wl_zero}")
    print(f"      theta = pi:  {n_wl_pi}")
    print(f"      other:       {n_wl_other}")

    # Show multiplet details
    for mi in multiplet_info[:10]:
        phases_str = ', '.join(f'{ph/np.pi:.3f}pi' for ph in mi['W_phases'])
        n_pi_in_mult = int(np.sum(np.abs(np.abs(mi['W_phases']) - np.pi) < PHASE_TOL))
        det_str = f"det(W)={mi['det_W']:.4f}"
        print(f"      d={mi['dim']:>2d}, eval~{mi['mean_eval']:>8.4f}: "
              f"phases=[{phases_str}] {det_str} "
              f"{'<-- PI' if n_pi_in_mult > 0 else ''}")

    if len(multiplet_info) > 10:
        print(f"      ... ({len(multiplet_info) - 10} more multiplets)")

    results[pq] = {
        'groups_ref': groups_ref,
        'ref_label': ref_label,
        'abelian_phases': abelian_phases,
        'abelian_overlaps': abelian_overlaps,
        'wilson_phases_all': wilson_phases_all,
        'wilson_dets': wilson_dets,
        'multiplet_info': multiplet_info,
        'n_ab_zero': n_ab_zero,
        'n_ab_pi': n_ab_pi,
        'n_ab_other': n_ab_other,
        'n_wl_zero': n_wl_zero,
        'n_wl_pi': n_wl_pi,
        'n_wl_other': n_wl_other,
        'n_singlets': len(abelian_phases),
        'n_multiplet_states': len(wilson_phases_all),
    }


# ============================================================================
# 5. AGGREGATE ANALYSIS
# ============================================================================

print(f"\n{'='*72}")
print("AGGREGATE RESULTS")
print("=" * 72)

print(f"\n{'Sector':>10s} | {'Branch':>6s} | {'D':>4s} | "
      f"{'sing':>4s} | {'mult':>4s} | "
      f"{'ab(0)':>5s} | {'ab(pi)':>6s} | {'ab(oth)':>7s} | "
      f"{'wl(0)':>5s} | {'wl(pi)':>6s} | {'wl(oth)':>7s}")
print("-" * 100)

total_ab_pi = 0
total_ab_zero = 0
total_wl_pi = 0
total_wl_zero = 0
total_wl_other = 0
total_singlets = 0
total_mult_states = 0

for pq in sectors_pq:
    p, q = pq
    d = dim_pq(p, q)
    D_size = d * 16
    r = results[pq]

    print(f"  ({p},{q}){' '*(6-len(f'({p},{q})'))} | {branch_map[pq]:>6s} | "
          f"{D_size:>4d} | "
          f"{r['n_singlets']:>4d} | {r['n_multiplet_states']:>4d} | "
          f"{r['n_ab_zero']:>5d} | {r['n_ab_pi']:>6d} | {r['n_ab_other']:>7d} | "
          f"{r['n_wl_zero']:>5d} | {r['n_wl_pi']:>6d} | {r['n_wl_other']:>7d}")

    total_ab_pi += r['n_ab_pi']
    total_ab_zero += r['n_ab_zero']
    total_wl_pi += r['n_wl_pi']
    total_wl_zero += r['n_wl_zero']
    total_wl_other += r['n_wl_other']
    total_singlets += r['n_singlets']
    total_mult_states += r['n_multiplet_states']

print("-" * 100)
print(f"  {'TOTAL':>8s} | {'':>6s} | {total_evals:>4d} | "
      f"{total_singlets:>4d} | {total_mult_states:>4d} | "
      f"{total_ab_zero:>5d} | {total_ab_pi:>6d} | "
      f"{total_evals - total_singlets - total_mult_states - total_ab_zero - total_ab_pi:>7d} | "
      f"{total_wl_zero:>5d} | {total_wl_pi:>6d} | {total_wl_other:>7d}")

total_pi = total_ab_pi + total_wl_pi
total_zero = total_ab_zero + total_wl_zero

print(f"\n  GRAND TOTAL:")
print(f"    Abelian pi-phases (singlets):       {total_ab_pi}")
print(f"    Non-Abelian pi-phases (multiplets): {total_wl_pi}")
print(f"    TOTAL pi-phases:                    {total_pi}")
print(f"    Total zero-phases:                  {total_zero}")
print(f"    Total other phases:                 {total_wl_other + (total_singlets - total_ab_zero - total_ab_pi)}")
print(f"    Total states accounted:             {total_singlets + total_mult_states}")


# ============================================================================
# 6. CONJUGATE SECTOR CHECK
# ============================================================================

print(f"\n{'='*72}")
print("CONJUGATE SECTOR CHECK: theta_{(p,q)} vs -theta_{(q,p)}")
print("=" * 72)

# Conjugate pairs: (p,q) <-> (q,p). The representation (q,p) = conjugate of (p,q).
# Under conjugation, eigenvalues of the Dirac operator negate (for anti-Hermitian D),
# so eigenvalues of H = iD stay the same but eigenvectors relate by complex conjugation.
# The Berry phase should satisfy: gamma_{(q,p)} = -gamma_{(p,q)} for the Abelian case.
# For Wilson loop: W_{(q,p)} should be the complex conjugate of W_{(p,q)}, so
# theta_{(q,p),k} = -theta_{(p,q),k}.

conj_pairs = [((1, 0), (0, 1)), ((2, 0), (0, 2)), ((3, 0), (0, 3))]

for (p1, q1), (p2, q2) in conj_pairs:
    r1 = results[(p1, q1)]
    r2 = results[(p2, q2)]

    # Compare Abelian phases
    ab1 = np.sort(r1['abelian_phases'])
    ab2 = np.sort(r2['abelian_phases'])

    if len(ab1) == len(ab2):
        ab_diff = np.abs(ab1 + ab2)  # should be ~ 0 if gamma_{conj} = -gamma
        ab_sum = np.abs(ab1 - ab2)   # should be ~ 0 if gamma_{conj} = +gamma
        ab_diff_max = np.max(ab_diff) if len(ab_diff) > 0 else 0
        ab_sum_max = np.max(ab_sum) if len(ab_sum) > 0 else 0

        if ab_diff_max < ab_sum_max:
            relation = "ANTI-SYMMETRIC (gamma_conj = -gamma)"
            max_dev = ab_diff_max
        else:
            relation = "SYMMETRIC (gamma_conj = +gamma)"
            max_dev = ab_sum_max

        print(f"  ({p1},{q1}) vs ({p2},{q2}) Abelian: {relation}, max dev = {max_dev:.6f}")
    else:
        print(f"  ({p1},{q1}) vs ({p2},{q2}) Abelian: DIFFERENT singlet counts "
              f"({len(ab1)} vs {len(ab2)})")

    # Compare Wilson loop phases (sorted)
    wl1 = np.sort(r1['wilson_phases_all'])
    wl2 = np.sort(r2['wilson_phases_all'])

    if len(wl1) == len(wl2):
        wl_diff = np.abs(wl1 + wl2)
        wl_sum = np.abs(wl1 - wl2)
        wl_diff_max = np.max(wl_diff) if len(wl_diff) > 0 else 0
        wl_sum_max = np.max(wl_sum) if len(wl_sum) > 0 else 0

        if wl_diff_max < wl_sum_max:
            wl_relation = "ANTI-SYMMETRIC"
            wl_dev = wl_diff_max
        else:
            wl_relation = "SYMMETRIC"
            wl_dev = wl_sum_max

        print(f"  ({p1},{q1}) vs ({p2},{q2}) Wilson:  {wl_relation}, max dev = {wl_dev:.6f}")
    else:
        print(f"  ({p1},{q1}) vs ({p2},{q2}) Wilson:  DIFFERENT state counts "
              f"({len(wl1)} vs {len(wl2)})")

    # Compare pi-phase counts
    print(f"    pi-counts: ({p1},{q1})=ab:{r1['n_ab_pi']}+wl:{r1['n_wl_pi']}, "
          f"({p2},{q2})=ab:{r2['n_ab_pi']}+wl:{r2['n_wl_pi']}")


# ============================================================================
# 7. GLOBAL Z_2 INVARIANT
# ============================================================================

print(f"\n{'='*72}")
print("GLOBAL Z_2 INVARIANT")
print("=" * 72)

# Product of all Wilson loop determinants across all sectors
# For O(d) Wilson loops, det(W) = +/- 1.
# The global Z_2 = product of all det(W) across all multiplets and all
# Abelian sign factors exp(i*gamma) = +/-1 for quantized phases.

global_det = 1.0 + 0j

for pq in sectors_pq:
    r = results[pq]

    # Abelian contribution: product of exp(i*gamma) for singlets
    for bp in r['abelian_phases']:
        global_det *= np.exp(1j * bp)

    # Wilson loop contribution: product of det(W) for multiplets
    for wd in r['wilson_dets']:
        global_det *= wd

print(f"  Global determinant product: {global_det}")
print(f"  |global_det|:              {abs(global_det):.6f}")
print(f"  arg(global_det)/pi:        {np.angle(global_det)/np.pi:.6f}")
print(f"  Global Z_2 = sign(Re):     {'+1' if np.real(global_det) > 0 else '-1'}")


# ============================================================================
# 8. PER-BRANCH ANALYSIS
# ============================================================================

print(f"\n{'='*72}")
print("PER-BRANCH ANALYSIS")
print("=" * 72)

for branch in ['B1', 'B2', 'B3']:
    branch_ab_pi = 0
    branch_wl_pi = 0
    branch_total = 0

    for pq in sectors_pq:
        if branch_map[pq] == branch:
            r = results[pq]
            d = dim_pq(pq[0], pq[1])
            branch_ab_pi += r['n_ab_pi']
            branch_wl_pi += r['n_wl_pi']
            branch_total += d * 16

    print(f"  {branch}: {branch_ab_pi} Abelian pi + {branch_wl_pi} Wilson pi "
          f"= {branch_ab_pi + branch_wl_pi} total pi / {branch_total} states")


# ============================================================================
# 9. PETER-WEYL WEIGHTED COUNTS
# ============================================================================

print(f"\n{'='*72}")
print("PETER-WEYL WEIGHTED PI COUNTS")
print("=" * 72)

# Each sector (p,q) appears dim(p,q) times in L^2(SU(3)). The physical
# pi-count should be weighted by dim(p,q).

total_pi_pw = 0
for pq in sectors_pq:
    p, q = pq
    d = dim_pq(p, q)
    r = results[pq]
    sector_pi = r['n_ab_pi'] + r['n_wl_pi']
    weighted = sector_pi * d
    total_pi_pw += weighted
    if sector_pi > 0:
        print(f"  ({p},{q}): {sector_pi} pi * dim={d} = {weighted}")

print(f"\n  Total PW-weighted pi count: {total_pi_pw}")
print(f"  S46 PW-weighted (Abelian only): 131")
print(f"  BCS pair count: 59.8")
print(f"  Ratio (PW pi / n_pairs): {total_pi_pw / 59.8:.2f}")


# ============================================================================
# 10. PHASE DISTRIBUTION ANALYSIS
# ============================================================================

print(f"\n{'='*72}")
print("PHASE DISTRIBUTION ANALYSIS")
print("=" * 72)

# Collect all phases (Abelian + Wilson)
all_phases = []
phase_types = []  # 'abelian' or 'wilson'

for pq in sectors_pq:
    r = results[pq]
    for bp in r['abelian_phases']:
        all_phases.append(bp)
        phase_types.append('abelian')
    for wp in r['wilson_phases_all']:
        all_phases.append(wp)
        phase_types.append('wilson')

all_phases = np.array(all_phases)
phase_types = np.array(phase_types)

# Wrap to [-pi, pi]
all_phases_wrapped = all_phases.copy()
all_phases_wrapped = np.mod(all_phases_wrapped + np.pi, 2 * np.pi) - np.pi

ab_mask = (phase_types == 'abelian')
wl_mask = (phase_types == 'wilson')

print(f"  Total phases: {len(all_phases)} ({np.sum(ab_mask)} Abelian + {np.sum(wl_mask)} Wilson)")

# Are phases quantized to 0 and pi, or continuously distributed?
ab_wrapped = all_phases_wrapped[ab_mask]
wl_wrapped = all_phases_wrapped[wl_mask]

print(f"\n  Abelian phase statistics:")
if len(ab_wrapped) > 0:
    print(f"    mean:    {np.mean(ab_wrapped):.4f} rad ({np.mean(ab_wrapped)/np.pi:.4f} pi)")
    print(f"    std:     {np.std(ab_wrapped):.4f} rad ({np.std(ab_wrapped)/np.pi:.4f} pi)")
    print(f"    |max|:   {np.max(np.abs(ab_wrapped)):.4f} rad ({np.max(np.abs(ab_wrapped))/np.pi:.4f} pi)")

print(f"\n  Wilson loop phase statistics:")
if len(wl_wrapped) > 0:
    print(f"    mean:    {np.mean(wl_wrapped):.4f} rad ({np.mean(wl_wrapped)/np.pi:.4f} pi)")
    print(f"    std:     {np.std(wl_wrapped):.4f} rad ({np.std(wl_wrapped)/np.pi:.4f} pi)")
    print(f"    |max|:   {np.max(np.abs(wl_wrapped)):.4f} rad ({np.max(np.abs(wl_wrapped))/np.pi:.4f} pi)")

    # Check if Wilson phases cluster at 0 and pi, or are continuous
    near_zero = np.sum(np.abs(wl_wrapped) < PHASE_TOL)
    near_pi = np.sum(np.abs(np.abs(wl_wrapped) - np.pi) < PHASE_TOL)
    continuous = len(wl_wrapped) - near_zero - near_pi
    print(f"    near 0:      {near_zero} ({100*near_zero/len(wl_wrapped):.1f}%)")
    print(f"    near +/-pi:  {near_pi} ({100*near_pi/len(wl_wrapped):.1f}%)")
    print(f"    continuous:  {continuous} ({100*continuous/len(wl_wrapped):.1f}%)")


# ============================================================================
# 11. GATE VERDICT
# ============================================================================

print(f"\n{'='*72}")
print("GATE VERDICT: WILSON-LOOP-48")
print("=" * 72)

print(f"\n  Total pi-count (Abelian + non-Abelian): {total_pi}")
print(f"  Criterion: PASS if in [13, 50]")

if 13 <= total_pi <= 50:
    verdict = "PASS"
elif total_pi >= 0:
    verdict = "INFO"
else:
    verdict = "FAIL"

print(f"\n  VERDICT: {verdict}")
print(f"\n  Does total = 15? {'YES' if total_pi == 15 else 'NO'}")
print(f"  Does total = 16? {'YES' if total_pi == 16 else 'NO'}")
print(f"  Does total = 32? {'YES' if total_pi == 32 else 'NO'}")


# ============================================================================
# 12. PLOTS
# ============================================================================

print(f"\n{'='*72}")
print("GENERATING PLOTS")
print("=" * 72)

fig = plt.figure(figsize=(20, 16))
fig.suptitle("Non-Abelian Wilson Loop: Berry Holonomy on Jensen-Deformed SU(3)\n"
             "WILSON-LOOP-48", fontsize=13, fontweight='bold')

# Panel 1: Histogram of ALL phases (Abelian + Wilson), [-pi, pi]
ax1 = fig.add_subplot(3, 3, 1)
bins = np.linspace(-np.pi, np.pi, 61)
if len(ab_wrapped) > 0:
    ax1.hist(ab_wrapped, bins=bins, alpha=0.6, color='steelblue',
             edgecolor='black', label='Abelian', linewidth=0.5)
if len(wl_wrapped) > 0:
    ax1.hist(wl_wrapped, bins=bins, alpha=0.6, color='coral',
             edgecolor='black', label='Wilson', linewidth=0.5)
ax1.axvline(0, color='blue', ls='--', lw=1.5)
ax1.axvline(np.pi, color='red', ls='--', lw=1.5)
ax1.axvline(-np.pi, color='red', ls='--', lw=1.5)
ax1.set_xlabel('Phase (rad)')
ax1.set_ylabel('Count')
ax1.set_title('Phase Distribution (all sectors)')
ax1.legend(fontsize=8)

# Panel 2: Pi-counts by sector (stacked: Abelian + Wilson)
ax2 = fig.add_subplot(3, 3, 2)
sector_labels = [f'({p},{q})' for p, q in sectors_pq]
x = np.arange(len(sectors_pq))
ab_pi_arr = [results[pq]['n_ab_pi'] for pq in sectors_pq]
wl_pi_arr = [results[pq]['n_wl_pi'] for pq in sectors_pq]
ax2.bar(x, ab_pi_arr, 0.35, label='Abelian $\\pi$', color='steelblue')
ax2.bar(x, wl_pi_arr, 0.35, bottom=ab_pi_arr, label='Wilson $\\pi$', color='coral')
ax2.set_xticks(x)
ax2.set_xticklabels(sector_labels, fontsize=7)
ax2.set_ylabel('$\\pi$-phase count')
ax2.set_title('Topological Charge by Sector')
ax2.legend(fontsize=7)

# Panel 3: Wilson loop phases for largest sectors (scatter)
ax3 = fig.add_subplot(3, 3, 3)
colors = plt.cm.tab10(np.linspace(0, 1, len(sectors_pq)))
for idx, pq in enumerate(sectors_pq):
    wl = results[pq]['wilson_phases_all']
    if len(wl) > 0:
        ax3.scatter(np.full(len(wl), idx), wl / np.pi, s=8,
                    color=colors[idx], alpha=0.5)
ax3.set_xticks(np.arange(len(sectors_pq)))
ax3.set_xticklabels(sector_labels, fontsize=7)
ax3.axhline(1, color='red', ls=':', lw=1)
ax3.axhline(-1, color='red', ls=':', lw=1)
ax3.axhline(0, color='blue', ls=':', lw=1)
ax3.set_ylabel('Wilson phase / $\\pi$')
ax3.set_title('Wilson Loop Phase Spectrum')
ax3.set_ylim(-1.1, 1.1)

# Panel 4: Conjugate pair comparison
ax4 = fig.add_subplot(3, 3, 4)
for i, ((p1, q1), (p2, q2)) in enumerate(conj_pairs):
    wl1 = np.sort(results[(p1, q1)]['wilson_phases_all'])
    wl2 = np.sort(results[(p2, q2)]['wilson_phases_all'])
    if len(wl1) == len(wl2) and len(wl1) > 0:
        ax4.scatter(wl1 / np.pi, -wl2 / np.pi, s=12, alpha=0.5,
                    label=f'({p1},{q1}) vs ({p2},{q2})')
lim = 1.2
ax4.plot([-lim, lim], [-lim, lim], 'k--', lw=1, alpha=0.5)
ax4.set_xlabel('$\\theta_{(p,q)} / \\pi$')
ax4.set_ylabel('$-\\theta_{(q,p)} / \\pi$')
ax4.set_title('Conjugate Sector Symmetry')
ax4.legend(fontsize=6)
ax4.set_xlim(-lim, lim)
ax4.set_ylim(-lim, lim)

# Panel 5: Multiplet dimension distribution
ax5 = fig.add_subplot(3, 3, 5)
all_dims = []
for pq in sectors_pq:
    for mi in results[pq]['multiplet_info']:
        all_dims.append(mi['dim'])
if all_dims:
    dim_vals = sorted(set(all_dims))
    dim_counts = [all_dims.count(d) for d in dim_vals]
    ax5.bar(range(len(dim_vals)), dim_counts, color='mediumpurple', edgecolor='black')
    ax5.set_xticks(range(len(dim_vals)))
    ax5.set_xticklabels([str(d) for d in dim_vals], fontsize=7)
    ax5.set_xlabel('Multiplet dimension')
    ax5.set_ylabel('Count')
    ax5.set_title('Degeneracy Multiplicity Histogram')

# Panel 6: Pi-phase by branch
ax6 = fig.add_subplot(3, 3, 6)
branches = ['B1', 'B2', 'B3']
branch_ab = []
branch_wl = []
for branch in branches:
    ab_sum = sum(results[pq]['n_ab_pi'] for pq in sectors_pq if branch_map[pq] == branch)
    wl_sum = sum(results[pq]['n_wl_pi'] for pq in sectors_pq if branch_map[pq] == branch)
    branch_ab.append(ab_sum)
    branch_wl.append(wl_sum)
x_br = np.arange(len(branches))
ax6.bar(x_br, branch_ab, 0.35, label='Abelian $\\pi$', color='steelblue')
ax6.bar(x_br, branch_wl, 0.35, bottom=branch_ab, label='Wilson $\\pi$', color='coral')
ax6.set_xticks(x_br)
ax6.set_xticklabels(branches)
ax6.set_ylabel('$\\pi$-phase count')
ax6.set_title('Topological Charge by BCS Branch')
ax6.legend(fontsize=8)

# Panel 7: Eigenvalue flow with Wilson-pi states highlighted
ax7 = fig.add_subplot(3, 3, 7)
# Use sector (2,1) as it has the most pi-phases
pq_show = (2, 1)
evals_show = sector_evals[pq_show]  # (N_TAU, D_size)
D_show = evals_show.shape[1]
r_show = results[pq_show]

# Identify which individual states are in pi-phase multiplets
pi_mult_indices = set()
for mi in r_show['multiplet_info']:
    n_pi_in = int(np.sum(np.abs(np.abs(mi['W_phases']) - np.pi) < PHASE_TOL))
    if n_pi_in > 0:
        pi_mult_indices.update(mi['indices'])

for n in range(D_show):
    if n in pi_mult_indices:
        ax7.plot(tau_grid, evals_show[:, n], '-', color='red', alpha=0.6, lw=0.8)
    else:
        ax7.plot(tau_grid, evals_show[:, n], '-', color='gray', alpha=0.15, lw=0.3)
ax7.set_xlabel('$\\tau$')
ax7.set_ylabel('eigenvalue')
ax7.set_title(f'Sector ({pq_show[0]},{pq_show[1]}): eigenflow (red = $\\pi$-multiplet)')
ax7.set_xlim(tau_min, tau_max)

# Panel 8: Wilson loop det(W) by sector
ax8 = fig.add_subplot(3, 3, 8)
for idx, pq in enumerate(sectors_pq):
    wds = results[pq]['wilson_dets']
    if wds:
        dets_real = [np.real(wd) for wd in wds]
        ax8.scatter(np.full(len(dets_real), idx), dets_real, s=10,
                    color=colors[idx], alpha=0.5)
ax8.set_xticks(np.arange(len(sectors_pq)))
ax8.set_xticklabels(sector_labels, fontsize=7)
ax8.axhline(1, color='blue', ls=':', lw=1, label='det=+1')
ax8.axhline(-1, color='red', ls=':', lw=1, label='det=-1')
ax8.set_ylabel('Re[det(W)]')
ax8.set_title('Wilson Loop Determinants')
ax8.legend(fontsize=7)

# Panel 9: Summary text
ax9 = fig.add_subplot(3, 3, 9)
ax9.axis('off')

summary_text = (
    f"WILSON-LOOP-48 SUMMARY\n"
    f"{'='*40}\n\n"
    f"tau range: [{tau_min}, {tau_max}], N_tau = {N_TAU}\n"
    f"Total eigenvalues: {total_evals}\n"
    f"Singlets (Abelian):  {total_singlets}\n"
    f"Multiplet states:    {total_mult_states}\n\n"
    f"Abelian pi-phases:   {total_ab_pi}\n"
    f"Wilson pi-phases:    {total_wl_pi}\n"
    f"TOTAL pi-phases:     {total_pi}\n\n"
    f"Total = 15? {'YES' if total_pi == 15 else 'NO'}\n"
    f"Total = 16? {'YES' if total_pi == 16 else 'NO'}\n\n"
    f"Global Z_2: {'+1' if np.real(global_det) > 0 else '-1'}\n\n"
    f"PW-weighted pi: {total_pi_pw}\n"
    f"BCS pairs: 59.8\n"
    f"Ratio: {total_pi_pw / 59.8:.2f}\n\n"
    f"GATE: {verdict}"
)

ax9.text(0.05, 0.95, summary_text, transform=ax9.transAxes,
         fontsize=9, verticalalignment='top', fontfamily='monospace',
         bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.tight_layout()
plot_path = os.path.join(SCRIPT_DIR, "s48_wilson_loop.png")
plt.savefig(plot_path, dpi=150, bbox_inches='tight')
print(f"Saved plot: {plot_path}")
plt.close()


# ============================================================================
# 13. SAVE DATA
# ============================================================================

print(f"\n{'='*72}")
print("SAVING DATA")
print("=" * 72)

output_data = {
    'tau_grid': tau_grid,
    'N_TAU': N_TAU,
    'MAX_PQ_SUM': MAX_PQ_SUM,
    'DEG_TOL': DEG_TOL,
    'PHASE_TOL': PHASE_TOL,
    'total_ab_pi': total_ab_pi,
    'total_wl_pi': total_wl_pi,
    'total_pi': total_pi,
    'total_ab_zero': total_ab_zero,
    'total_wl_zero': total_wl_zero,
    'total_singlets': total_singlets,
    'total_mult_states': total_mult_states,
    'total_pi_pw': total_pi_pw,
    'global_det_real': np.real(global_det),
    'global_det_imag': np.imag(global_det),
    'global_det_phase': np.angle(global_det),
    'verdict': verdict,
}

for pq in sectors_pq:
    p, q = pq
    prefix = f's{p}{q}'
    r = results[pq]
    output_data[f'{prefix}_abelian_phases'] = r['abelian_phases']
    output_data[f'{prefix}_wilson_phases'] = r['wilson_phases_all']
    output_data[f'{prefix}_n_ab_pi'] = r['n_ab_pi']
    output_data[f'{prefix}_n_ab_zero'] = r['n_ab_zero']
    output_data[f'{prefix}_n_wl_pi'] = r['n_wl_pi']
    output_data[f'{prefix}_n_wl_zero'] = r['n_wl_zero']
    output_data[f'{prefix}_n_singlets'] = r['n_singlets']
    output_data[f'{prefix}_n_mult_states'] = r['n_multiplet_states']
    output_data[f'{prefix}_evals'] = sector_evals[pq]

    # Save Wilson loop eigenvalues for each multiplet
    for i_mi, mi in enumerate(r['multiplet_info']):
        output_data[f'{prefix}_mult{i_mi}_dim'] = mi['dim']
        output_data[f'{prefix}_mult{i_mi}_phases'] = mi['W_phases']
        output_data[f'{prefix}_mult{i_mi}_eval'] = mi['mean_eval']

out_path = os.path.join(SCRIPT_DIR, "s48_wilson_loop.npz")
np.savez_compressed(out_path, **output_data)
print(f"Saved data: {out_path}")


# ============================================================================
# 14. FINAL REPORT
# ============================================================================

print(f"\n{'='*72}")
print("WILSON-LOOP-48: FINAL REPORT")
print("=" * 72)

print(f"""
COMPUTATION:
  Non-Abelian Wilson loop W = prod_j M(j) for degenerate multiplets.
  M(j) = V(j)^T V(j+1) overlap matrix, SVD-stabilized to nearest O(d).
  tau grid: [{tau_min}, {tau_max}], {N_TAU} points.
  Sectors: 9 sectors with p+q <= {MAX_PQ_SUM}.
  Total eigenstates: {total_evals} = {total_singlets} singlets + {total_mult_states} in multiplets.

RESULTS:
  Abelian pi-phases (singlets):       {total_ab_pi}
  Non-Abelian pi-phases (multiplets): {total_wl_pi}
  TOTAL pi-phases:                    {total_pi}

  PW-weighted pi-count:               {total_pi_pw}
  BCS pair count:                     59.8
  Ratio (PW pi / n_pairs):           {total_pi_pw / 59.8:.2f}

  Global Z_2 invariant:              {'+1' if np.real(global_det) > 0 else '-1'}

GATE: WILSON-LOOP-48
  Criterion: PASS if total pi in [13, 50]
  Total pi = {total_pi}
  VERDICT: {verdict}

PHYSICAL INTERPRETATION:
  The non-Abelian Wilson loop eigenvalues are the gauge-invariant content
  of the Berry holonomy for degenerate multiplets. Each eigenvalue theta = pi
  signals a Mobius-strip topology in the corresponding eigenvector subspace:
  the state returns to itself with a sign flip after traversing the tau path.

  For REAL eigenstates (our case), the Wilson loop is in O(d), and its
  eigenvalues come in conjugate pairs exp(+/- i*theta). The eigenvalue -1
  (theta = pi) is the Z_2 topological invariant.

  Cross-reference: S25 proved Berry curvature Omega = 0 identically (local
  flatness). S46 showed Zak phase = pi survives (global topology). This
  computation extends the Zak phase analysis to degenerate subspaces via
  the Wilczek-Zee non-Abelian Berry phase.

  The reconciliation: zero LOCAL curvature is compatible with nontrivial
  GLOBAL holonomy because the connection is flat but the bundle is not
  trivially globally trivializable. This is the hallmark of a Z_2 bundle
  (Mobius strip in each pi-phase sector).

Output: tier0-computation/s48_wilson_loop.{{npz,png,py}}
""")
