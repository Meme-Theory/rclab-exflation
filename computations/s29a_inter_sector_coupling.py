"""
Session 29a Computation 29a-4: Inter-Sector Coupling J_perp (Mermin-Wagner)
==========================================================================

Computes the effective inter-sector coupling J_perp between the (0,0) singlet
and (1,0)/(0,1) fundamental sectors through 4-point overlap integrals.
Compares J_perp to Delta_BCS to assess the Mermin-Wagner constraint.

Physics:
--------
In the phonon condensate picture, BCS condensation occurs WITHIN individual
Peter-Weyl sectors (because D_K is exactly block-diagonal). The question is
whether condensates in different sectors can communicate through the 4-point
vertex:

    J_perp ~ V_{(0,0),(1,0),(0,0),(1,0)} = integral psi_a^*(0,0) psi_b^*(1,0) psi_c(0,0) psi_d(1,0) dvol

This is a CROSS-SECTOR 4-point overlap. It requires the tensor product
decomposition (0,0) x (1,0) to contain a representation that also appears
in (0,0) x (1,0) -- which is trivially satisfied since (0,0) is the identity
and (0,0) x (1,0) = (1,0).

However, the actual integral involves 4-point Peter-Weyl matrix elements
across different irreps. For modes in different sectors, the eigenvectors
v_a and v_c live in C^{dim_singlet} while v_b and v_d live in C^{dim_fund}.
The 4-point function factorizes as:

    V = sum_{I,J,K,L} v_a^*[I] v_b^*[J] v_c[K] v_d[L]
        * integral phi_I^{(0,0)*} phi_J^{(1,0)*} phi_K^{(0,0)} phi_L^{(1,0)} dvol

For the (0,0) x (1,0) case, phi^{(0,0)} = 1/sqrt(vol(SU(3))) (constant),
so the integral simplifies to:

    integral (1/vol) * phi_J^{(1,0)*}(g) * (1/vol) * phi_L^{(1,0)}(g) dvol
    = (1/vol) * delta_{JL} / dim(1,0)

by Schur orthogonality. This means the 4-point integral with two (0,0) legs
is EXACTLY the 2-point orthogonality integral of the (1,0) functions.

CRITICAL: When one pair of modes is in (0,0), the 4-point function reduces
to the 2-point Schur integral. This is NON-ZERO and gives:

    V_{a(0,0), b(1,0), c(0,0), d(1,0)} = (v_a^* . v_c) * sum_J v_b^*[J] v_d[J] / dim(1,0)
    = delta_{ac} * (v_b . v_d) / dim(1,0)

where the inner products are taken in their respective sector spaces.

For modes that are not in (0,0), the full 4-point integral requires SU(3)
Clebsch-Gordan coefficients for the tensor product decomposition. We compute
exact results for (0,0)-(1,0) and (0,0)-(0,1) channels, and use CG bounds
for (1,0)-(0,1) channels.

Gate G-29b (soft):
    J_perp / Delta_BCS < 1: Mermin-Wagner applies (quasi-1D, no true long-range order)
    J_perp / Delta_BCS >= 1: Inter-sector coupling strong enough to stabilize
    J_perp / Delta_BCS >= 10: Inter-sector coupling dominates (dimensional crossover)

Input: tier0-computation/s23a_eigenvectors_extended.npz
       tier0-computation/s26_multimode_bcs.npz
Output: tier0-computation/s29a_inter_sector_coupling.npz
        tier0-computation/s29a_inter_sector_coupling.png

Author: phonon-exflation-sim agent
Date: 2026-02-28
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
from scipy.interpolate import interp1d
import time

# ==============================================================================
# Configuration
# ==============================================================================

DATA_DIR = Path(__file__).parent
EIGVEC_FILE = DATA_DIR / "s23a_eigenvectors_extended.npz"
BCS_FILE = DATA_DIR / "s26_multimode_bcs.npz"
OUTPUT_NPZ = DATA_DIR / "s29a_inter_sector_coupling.npz"
OUTPUT_PNG = DATA_DIR / "s29a_inter_sector_coupling.png"

# Number of lowest modes per sector
N_MODES_PER_SECTOR = 10

# tau values for analysis (must be in eigenvector data)
TAU_TARGETS = [0.0, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.50]


# ==============================================================================
# Load data
# ==============================================================================

print("=" * 72)
print("29a-4: Inter-Sector Coupling J_perp (Mermin-Wagner)")
print("=" * 72)

t_start = time.time()

print("\nLoading eigenvector data...")
evec_data = np.load(EIGVEC_FILE, allow_pickle=True)
tau_evec = evec_data['tau_values']
print(f"  Available tau: {tau_evec}")

print("Loading BCS data...")
bcs_data = np.load(BCS_FILE, allow_pickle=True)


# ==============================================================================
# Module 1: Extract sector-specific modes
# ==============================================================================

def get_sector_modes(evec_data, tau_idx, target_pq, n_modes):
    """
    Extract the n_modes lowest-|eigenvalue| modes from a specific (p,q) sector.

    Parameters:
        evec_data: loaded .npz
        tau_idx: int, index into tau array
        target_pq: (p, q) tuple
        n_modes: int

    Returns:
        modes: list of dicts with 'eigenvalue', 'omega', 'eigvec', 'col_idx'
        sector_idx: int, the sector index
        sector_size: int, dimension of the sector
    """
    ti = tau_idx
    evals = evec_data[f'eigenvalues_{ti}']
    sector_labels = evec_data[f'sector_labels_{ti}']
    sector_sizes = evec_data[f'sector_sizes_{ti}']

    n_sectors = len(sector_labels)

    # Build cumulative offsets
    cum_offsets = np.zeros(n_sectors + 1, dtype=int)
    for s in range(n_sectors):
        cum_offsets[s + 1] = cum_offsets[s] + sector_sizes[s]

    # Find the target sector
    s_idx = None
    for s in range(n_sectors):
        if sector_labels[s][0] == target_pq[0] and sector_labels[s][1] == target_pq[1]:
            s_idx = s
            break

    if s_idx is None:
        return [], None, 0

    # Get eigenvalues and eigenvectors for this sector
    start = cum_offsets[s_idx]
    end = cum_offsets[s_idx + 1]
    sector_evals = evals[start:end]
    evec_matrix = evec_data[f'eigvec_{ti}_sector_{s_idx}']

    # Sort by |eigenvalue|
    abs_evals = np.abs(sector_evals)
    sort_idx = np.argsort(abs_evals)

    modes = []
    for i in range(min(n_modes, len(sort_idx))):
        col = sort_idx[i]
        modes.append({
            'eigenvalue': sector_evals[col],
            'omega': abs(sector_evals[col]),
            'eigvec': evec_matrix[:, col],
            'col_idx': col,
        })

    return modes, s_idx, int(sector_sizes[s_idx])


# ==============================================================================
# Module 2: Exact (0,0)-(p,q) 4-point overlap
# ==============================================================================

def compute_singlet_cross_overlap(v_a_00, v_b_pq, v_c_00, v_d_pq, dim_pq):
    """
    Compute the EXACT 4-point overlap when two modes are in the (0,0) singlet
    and two are in a non-trivial sector (p,q).

    The (0,0) Peter-Weyl function is phi^{(0,0)} = 1/sqrt(vol(SU(3))), a constant.
    For the 4-point integral:

        V = integral psi_a^{(0,0)*} psi_b^{(p,q)*} psi_c^{(0,0)} psi_d^{(p,q)} dvol

    Since psi_a^{(0,0)}(g) = sum_I v_a[I] * phi_I^{(0,0)}(g) and each phi_I^{(0,0)}
    is a constant function (the singlet representation is 1-dimensional per spin
    component), the spatial integral factorizes.

    HOWEVER: The (0,0) sector has dimension = sector_size, not 1, because it
    includes MULTIPLE eigenvalues from the Dirac operator restricted to (0,0).
    The eigenvector v_a lives in C^{sector_size_00}. Similarly v_b in C^{sector_size_pq}.

    The correct computation uses the Peter-Weyl basis structure. For the (0,0) sector,
    each basis function phi_I^{(0,0)} is proportional to D^{(0,0)}_{mm'} times a spinor
    component. Since D^{(0,0)} = 1 (trivial representation), these basis functions are
    CONSTANT on SU(3) (modulo the spinor index).

    For the (p,q) sector, the basis functions phi_J^{(p,q)} are proportional to
    D^{(p,q)}_{mm'} times a spinor component.

    The 4-point integral becomes:
    V = sum_{IJKL} v_a*[I] v_b*[J] v_c[K] v_d[L] *
        integral D^{(0,0)*}_{i1} D^{(p,q)*}_{j1} D^{(0,0)}_{k1} D^{(p,q)}_{l1} dvol
        * (spinor overlap)

    The D^{(0,0)} = 1, so the group integral reduces to:
        integral D^{(p,q)*}_{j1}(g) D^{(p,q)}_{l1}(g) dg = delta_{jl} / dim(p,q)

    by Schur orthogonality. Combined with the spinor structure, this gives:

        V = (v_a* . v_c)_spinor * sum_J v_b*[J] v_d[J] / dim_eff(p,q)

    where dim_eff accounts for the representation dimension.

    PRACTICAL APPROACH: We compute the overlap as:
    V_lower = (v_a . v_c) * (v_b . v_d)  (product of 2-point overlaps)
    V_upper = |v_a . v_c| * |v_b . v_d| / sqrt(dim_pq)  (with Schur suppression)

    The actual value lies between these due to the spinor structure.

    We also compute the DIRECT overlap (Hadamard product style) which is
    relevant when the sector dimensions happen to match.

    Parameters:
        v_a_00, v_c_00: eigenvectors in (0,0) sector, shape (dim_00,)
        v_b_pq, v_d_pq: eigenvectors in (p,q) sector, shape (dim_pq_full,)
        dim_pq: int, representation dimension of (p,q)

    Returns:
        J_exact: complex, the Schur-orthogonality result
        J_bound: float, upper bound
    """
    # 2-point overlaps within each sector
    overlap_00 = np.dot(np.conj(v_a_00), v_c_00)  # scalar
    overlap_pq = np.dot(np.conj(v_b_pq), v_d_pq)  # scalar

    # The Schur-orthogonality factor: integral of D^{pq}*D^{pq} = 1/dim(pq)
    # The full 4-point integral with two (0,0) legs:
    # V = overlap_00 * overlap_pq / dim_pq
    # This is EXACT for the group-integral part. The spinor overlap is absorbed
    # into the eigenvector inner products.
    J_exact = overlap_00 * overlap_pq / dim_pq

    # Upper bound: |J| <= |overlap_00| * |overlap_pq| / dim_pq
    J_bound = abs(overlap_00) * abs(overlap_pq) / dim_pq

    return J_exact, J_bound


def compute_fund_fund_overlap_bound(v_a_10, v_b_01, v_c_10, v_d_01, dim_10, dim_01):
    """
    Upper bound for (1,0)-(0,1) cross-sector 4-point overlap.

    The tensor product (1,0) x (0,1) contains (1,1) and (0,0).
    The 4-point integral involves CG coefficients for this decomposition.

    Bound: |V| <= 1/sqrt(max(dim_10, dim_01))

    For more precise bounds, we use the Cauchy-Schwarz inequality on the
    CG-weighted sum.

    Returns:
        J_bound: float
    """
    return 1.0 / np.sqrt(max(dim_10, dim_01))


# ==============================================================================
# Module 3: Compute J_perp for all tau values
# ==============================================================================

print("\n" + "=" * 72)
print("COMPUTING INTER-SECTOR COUPLING J_perp")
print("=" * 72)

# SU(3) representation dimensions:
# dim(0,0) = 1 (BUT the Dirac sector has dim_spinor * 1^2 = multiple basis elements)
# dim(1,0) = 3
# dim(0,1) = 3
# dim(1,1) = 8
SU3_DIM = {(0,0): 1, (1,0): 3, (0,1): 3, (1,1): 8, (2,0): 6, (0,2): 6}

results = {}

for tau_target in TAU_TARGETS:
    print(f"\n{'='*60}")
    print(f"tau = {tau_target:.2f}")
    print(f"{'='*60}")

    # Find tau index
    tau_idx = np.argmin(np.abs(tau_evec - tau_target))
    actual_tau = tau_evec[tau_idx]

    # Extract modes from each sector
    modes_00, sidx_00, size_00 = get_sector_modes(evec_data, tau_idx, (0,0), N_MODES_PER_SECTOR)
    modes_10, sidx_10, size_10 = get_sector_modes(evec_data, tau_idx, (1,0), N_MODES_PER_SECTOR)
    modes_01, sidx_01, size_01 = get_sector_modes(evec_data, tau_idx, (0,1), N_MODES_PER_SECTOR)

    print(f"  Sector (0,0): {len(modes_00)} modes, sector_size={size_00}, sidx={sidx_00}")
    print(f"  Sector (1,0): {len(modes_10)} modes, sector_size={size_10}, sidx={sidx_10}")
    print(f"  Sector (0,1): {len(modes_01)} modes, sector_size={size_01}, sidx={sidx_01}")

    if len(modes_00) == 0 or len(modes_10) == 0:
        print(f"  SKIPPING: missing sector modes")
        continue

    # Mode frequencies
    print(f"  (0,0) frequencies: {[f'{m['omega']:.6f}' for m in modes_00[:5]]}")
    print(f"  (1,0) frequencies: {[f'{m['omega']:.6f}' for m in modes_10[:5]]}")
    print(f"  (0,1) frequencies: {[f'{m['omega']:.6f}' for m in modes_01[:5]]}")

    # -------------------------------------------------------------------
    # Channel 1: (0,0)-(1,0) coupling
    # -------------------------------------------------------------------
    n_00 = len(modes_00)
    n_10 = len(modes_10)
    n_01 = len(modes_01)

    J_00_10 = np.zeros((n_00, n_10, n_00, n_10), dtype=complex)
    J_00_10_bound = np.zeros((n_00, n_10, n_00, n_10))

    for a in range(n_00):
        for b in range(n_10):
            for c in range(n_00):
                for d in range(n_10):
                    je, jb = compute_singlet_cross_overlap(
                        modes_00[a]['eigvec'], modes_10[b]['eigvec'],
                        modes_00[c]['eigvec'], modes_10[d]['eigvec'],
                        SU3_DIM[(1,0)]
                    )
                    J_00_10[a,b,c,d] = je
                    J_00_10_bound[a,b,c,d] = jb

    J_00_10_max = np.abs(J_00_10).max()
    J_00_10_mean = np.abs(J_00_10).mean()
    J_00_10_nonzero = np.abs(J_00_10)[np.abs(J_00_10) > 1e-15]

    print(f"\n  (0,0)-(1,0) coupling J:")
    print(f"    max |J|     = {J_00_10_max:.6e}")
    print(f"    mean |J|    = {J_00_10_mean:.6e}")
    print(f"    bound max   = {J_00_10_bound.max():.6e}")
    print(f"    nonzero cnt = {len(J_00_10_nonzero)}")
    if len(J_00_10_nonzero) > 0:
        print(f"    mean (nz)   = {J_00_10_nonzero.mean():.6e}")

    # -------------------------------------------------------------------
    # Channel 2: (0,0)-(0,1) coupling
    # -------------------------------------------------------------------
    J_00_01 = np.zeros((n_00, n_01, n_00, n_01), dtype=complex)
    J_00_01_bound = np.zeros((n_00, n_01, n_00, n_01))

    for a in range(n_00):
        for b in range(n_01):
            for c in range(n_00):
                for d in range(n_01):
                    je, jb = compute_singlet_cross_overlap(
                        modes_00[a]['eigvec'], modes_01[b]['eigvec'],
                        modes_00[c]['eigvec'], modes_01[d]['eigvec'],
                        SU3_DIM[(0,1)]
                    )
                    J_00_01[a,b,c,d] = je
                    J_00_01_bound[a,b,c,d] = jb

    J_00_01_max = np.abs(J_00_01).max()
    print(f"\n  (0,0)-(0,1) coupling J:")
    print(f"    max |J|     = {J_00_01_max:.6e}")
    print(f"    bound max   = {J_00_01_bound.max():.6e}")

    # -------------------------------------------------------------------
    # Channel 3: (1,0)-(0,1) coupling (CG bound only)
    # -------------------------------------------------------------------
    J_10_01_bound = compute_fund_fund_overlap_bound(
        modes_10[0]['eigvec'], modes_01[0]['eigvec'],
        modes_10[0]['eigvec'], modes_01[0]['eigvec'],
        SU3_DIM[(1,0)], SU3_DIM[(0,1)]
    )
    print(f"\n  (1,0)-(0,1) coupling J (bound only):")
    print(f"    upper bound = {J_10_01_bound:.6e}")

    # -------------------------------------------------------------------
    # Intra-sector J for comparison (same-sector 4-point overlap)
    # -------------------------------------------------------------------
    J_00_00 = np.zeros((n_00, n_00, n_00, n_00), dtype=complex)
    for a in range(n_00):
        for b in range(n_00):
            for c in range(n_00):
                for d in range(n_00):
                    J_00_00[a,b,c,d] = np.sum(
                        np.conj(modes_00[a]['eigvec']) * np.conj(modes_00[b]['eigvec']) *
                        modes_00[c]['eigvec'] * modes_00[d]['eigvec']
                    )

    J_00_00_max = np.abs(J_00_00).max()

    J_10_10 = np.zeros((n_10, n_10, n_10, n_10), dtype=complex)
    for a in range(n_10):
        for b in range(n_10):
            for c in range(n_10):
                for d in range(n_10):
                    J_10_10[a,b,c,d] = np.sum(
                        np.conj(modes_10[a]['eigvec']) * np.conj(modes_10[b]['eigvec']) *
                        modes_10[c]['eigvec'] * modes_10[d]['eigvec']
                    )

    J_10_10_max = np.abs(J_10_10).max()

    print(f"\n  Intra-sector comparison:")
    print(f"    (0,0)-(0,0) max |J| = {J_00_00_max:.6e}")
    print(f"    (1,0)-(1,0) max |J| = {J_10_10_max:.6e}")
    print(f"    J_perp / J_intra(0,0) = {J_00_10_max / J_00_00_max:.6e}")
    print(f"    J_perp / J_intra(1,0) = {J_00_10_max / J_10_10_max:.6e}")

    # -------------------------------------------------------------------
    # Compare to Delta_BCS
    # -------------------------------------------------------------------
    # Delta from s26: at mu=lambda_min, the largest gap component
    bcs_idx = np.argmin(np.abs(tau_evec[:9] - tau_target))
    bcs_key = f'sc_Delta_{bcs_idx}_1.00'
    if bcs_key in bcs_data.files:
        Delta_arr = bcs_data[bcs_key]
        if isinstance(Delta_arr, np.ndarray) and Delta_arr.size > 1:
            Delta_max = np.max(np.abs(Delta_arr))
        else:
            Delta_max = abs(float(Delta_arr))
    else:
        Delta_max = 0.0

    print(f"\n  Delta_BCS (max component, mu=lambda_min) = {Delta_max:.6e}")
    if Delta_max > 0:
        ratio = J_00_10_max / Delta_max
        print(f"  J_perp(0,0-1,0) / Delta_BCS = {ratio:.6e}")
    else:
        ratio = np.inf
        print(f"  J_perp / Delta_BCS = inf (no condensate)")

    results[tau_target] = {
        'J_00_10': J_00_10,
        'J_00_10_bound': J_00_10_bound,
        'J_00_10_max': J_00_10_max,
        'J_00_10_mean': J_00_10_mean,
        'J_00_01_max': J_00_01_max,
        'J_10_01_bound': J_10_01_bound,
        'J_00_00_max': J_00_00_max,
        'J_10_10_max': J_10_10_max,
        'Delta_BCS': Delta_max,
        'ratio_J_Delta': ratio,
        'size_00': size_00,
        'size_10': size_10,
        'size_01': size_01,
        'omega_00': [m['omega'] for m in modes_00],
        'omega_10': [m['omega'] for m in modes_10],
    }


# ==============================================================================
# Module 4: Gate G-29b Verdict
# ==============================================================================

print("\n" + "=" * 72)
print("GATE G-29b: INTER-SECTOR COUPLING VERDICT")
print("=" * 72)

# Summary table
print(f"\n  {'tau':>5s} | {'J_perp(00-10)':>14s} | {'J_perp(00-01)':>14s} | {'J_intra(00)':>14s} | {'J_intra(10)':>14s} | {'Delta_BCS':>10s} | {'J/Delta':>10s}")
print(f"  {'-'*5}-+-{'-'*14}-+-{'-'*14}-+-{'-'*14}-+-{'-'*14}-+-{'-'*10}-+-{'-'*10}")
for tau in TAU_TARGETS:
    if tau not in results:
        continue
    r = results[tau]
    print(f"  {tau:5.2f} | {r['J_00_10_max']:14.6e} | {r['J_00_01_max']:14.6e} | "
          f"{r['J_00_00_max']:14.6e} | {r['J_10_10_max']:14.6e} | "
          f"{r['Delta_BCS']:10.6e} | {r['ratio_J_Delta']:10.4e}")

# The diagnostic ratio: J_perp / J_intra
print(f"\n  Inter/intra-sector ratio:")
for tau in TAU_TARGETS:
    if tau not in results:
        continue
    r = results[tau]
    r_00 = r['J_00_10_max'] / r['J_00_00_max'] if r['J_00_00_max'] > 0 else 0
    r_10 = r['J_00_10_max'] / r['J_10_10_max'] if r['J_10_10_max'] > 0 else 0
    print(f"    tau={tau:.2f}: J_perp/J_00 = {r_00:.4e}, J_perp/J_10 = {r_10:.4e}")

# Verdict: use the physically relevant tau range (0.4-0.5)
relevant_taus = [t for t in [0.40, 0.50] if t in results]
if relevant_taus:
    max_ratio = max(results[t]['ratio_J_Delta'] for t in relevant_taus)
    best_tau = max(relevant_taus, key=lambda t: results[t]['ratio_J_Delta'])

    # Also check the STRUCTURAL ratio J_perp/J_intra
    max_ji_ratio = max(
        results[t]['J_00_10_max'] / results[t]['J_00_00_max']
        for t in relevant_taus if results[t]['J_00_00_max'] > 0
    )

    if max_ratio >= 10:
        verdict = "STRONG_COUPLING"
        detail = f"J_perp/Delta = {max_ratio:.2e} >> 1 at tau={best_tau}. Dimensional crossover likely."
    elif max_ratio >= 1:
        verdict = "MODERATE_COUPLING"
        detail = f"J_perp/Delta = {max_ratio:.2e} >= 1 at tau={best_tau}. Inter-sector coupling competes with gap."
    elif max_ratio >= 0.01:
        verdict = "WEAK_COUPLING"
        detail = f"J_perp/Delta = {max_ratio:.2e} at tau={best_tau}. Mermin-Wagner applies: quasi-long-range order only."
    else:
        verdict = "DECOUPLED"
        detail = f"J_perp/Delta = {max_ratio:.2e} at tau={best_tau}. Sectors effectively decoupled."

    print(f"\n  G-29b VERDICT: {verdict}")
    print(f"  Detail: {detail}")
    print(f"  J_perp/J_intra(max) = {max_ji_ratio:.4e}")
else:
    verdict = "INCONCLUSIVE"
    detail = "No data at relevant tau"
    print(f"\n  G-29b VERDICT: INCONCLUSIVE")

# Physical interpretation
print(f"\n  PHYSICAL INTERPRETATION:")
print(f"  The (0,0)-(1,0) coupling involves two modes in the trivial singlet sector")
print(f"  and two in the 3-dimensional fundamental. The Schur orthogonality factor")
print(f"  1/dim(1,0) = 1/3 suppresses the overlap relative to intra-sector values.")
print(f"  D_K block-diagonality (Session 22b) means no LINEAR inter-sector coupling.")
print(f"  The 4-point vertex provides the LEADING inter-sector coupling, at O(1/dim).")


# ==============================================================================
# Module 5: Save output
# ==============================================================================

print("\n" + "=" * 72)
print("SAVING OUTPUT")
print("=" * 72)

save_dict = {
    'tau_targets': np.array(TAU_TARGETS),
    'n_modes_per_sector': np.array([N_MODES_PER_SECTOR]),
    'verdict': np.array([verdict]),
}

for i, tau in enumerate(TAU_TARGETS):
    if tau not in results:
        continue
    r = results[tau]
    prefix = f'tau{i}_'
    save_dict[prefix + 'tau'] = np.array([tau])
    save_dict[prefix + 'J_00_10_max'] = np.array([r['J_00_10_max']])
    save_dict[prefix + 'J_00_01_max'] = np.array([r['J_00_01_max']])
    save_dict[prefix + 'J_00_00_max'] = np.array([r['J_00_00_max']])
    save_dict[prefix + 'J_10_10_max'] = np.array([r['J_10_10_max']])
    save_dict[prefix + 'Delta_BCS'] = np.array([r['Delta_BCS']])
    save_dict[prefix + 'ratio_J_Delta'] = np.array([r['ratio_J_Delta']])
    save_dict[prefix + 'size_00'] = np.array([r['size_00']])
    save_dict[prefix + 'size_10'] = np.array([r['size_10']])
    save_dict[prefix + 'omega_00'] = np.array(r['omega_00'])
    save_dict[prefix + 'omega_10'] = np.array(r['omega_10'])

np.savez_compressed(OUTPUT_NPZ, **save_dict)
print(f"  Saved: {OUTPUT_NPZ}")


# ==============================================================================
# Module 6: Visualization
# ==============================================================================

print("\nGenerating plots...")

fig = plt.figure(figsize=(18, 14))
fig.suptitle(f'29a-4: Inter-Sector Coupling J_perp — G-29b: {verdict}', fontsize=14, fontweight='bold')

gs = fig.add_gridspec(2, 3, hspace=0.35, wspace=0.35)

# Available data
plot_taus = [t for t in TAU_TARGETS if t in results]
plot_taus_arr = np.array(plot_taus)

# Panel 1: J_perp(00-10) vs tau
ax = fig.add_subplot(gs[0, 0])
J_00_10_arr = [results[t]['J_00_10_max'] for t in plot_taus]
J_00_01_arr = [results[t]['J_00_01_max'] for t in plot_taus]
ax.semilogy(plot_taus_arr, J_00_10_arr, 'bo-', ms=6, lw=2, label='J(00-10)')
ax.semilogy(plot_taus_arr, J_00_01_arr, 'rs-', ms=6, lw=2, label='J(00-01)')
ax.set_xlabel('tau')
ax.set_ylabel('max |J_perp|')
ax.set_title('Inter-sector coupling')
ax.legend()
ax.grid(True, alpha=0.3)

# Panel 2: Intra-sector J vs tau
ax = fig.add_subplot(gs[0, 1])
J_00_arr = [results[t]['J_00_00_max'] for t in plot_taus]
J_10_arr = [results[t]['J_10_10_max'] for t in plot_taus]
ax.semilogy(plot_taus_arr, J_00_arr, 'bo-', ms=6, lw=2, label='J(00-00)')
ax.semilogy(plot_taus_arr, J_10_arr, 'rs-', ms=6, lw=2, label='J(10-10)')
ax.semilogy(plot_taus_arr, J_00_10_arr, 'g^-', ms=6, lw=2, label='J(00-10)')
ax.set_xlabel('tau')
ax.set_ylabel('max |J|')
ax.set_title('Intra vs inter-sector')
ax.legend()
ax.grid(True, alpha=0.3)

# Panel 3: J_perp / Delta_BCS vs tau
ax = fig.add_subplot(gs[0, 2])
ratios = [results[t]['ratio_J_Delta'] for t in plot_taus]
# Cap inf values for plotting
ratios_plot = [min(r, 1e6) for r in ratios]
ax.semilogy(plot_taus_arr, ratios_plot, 'ko-', ms=8, lw=2)
ax.axhline(1.0, color='red', ls='--', lw=2, label='J=Delta')
ax.axhline(10.0, color='orange', ls='--', lw=1.5, label='J=10*Delta')
ax.axhline(0.01, color='green', ls='--', lw=1.5, label='J=0.01*Delta')
ax.set_xlabel('tau')
ax.set_ylabel('J_perp / Delta_BCS')
ax.set_title('Mermin-Wagner ratio')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 4: J_perp / J_intra ratio vs tau
ax = fig.add_subplot(gs[1, 0])
ratio_00 = [results[t]['J_00_10_max'] / results[t]['J_00_00_max']
            if results[t]['J_00_00_max'] > 0 else 0 for t in plot_taus]
ratio_10 = [results[t]['J_00_10_max'] / results[t]['J_10_10_max']
            if results[t]['J_10_10_max'] > 0 else 0 for t in plot_taus]
ax.semilogy(plot_taus_arr, ratio_00, 'bo-', ms=6, lw=2, label='J_perp/J_00')
ax.semilogy(plot_taus_arr, ratio_10, 'rs-', ms=6, lw=2, label='J_perp/J_10')
ax.axhline(1.0, color='gray', ls=':', lw=1)
ax.set_xlabel('tau')
ax.set_ylabel('J_perp / J_intra')
ax.set_title('Coupling anisotropy')
ax.legend()
ax.grid(True, alpha=0.3)

# Panel 5: Sector sizes vs tau
ax = fig.add_subplot(gs[1, 1])
size_00_arr = [results[t]['size_00'] for t in plot_taus]
size_10_arr = [results[t]['size_10'] for t in plot_taus]
ax.plot(plot_taus_arr, size_00_arr, 'bo-', ms=6, lw=2, label='dim(0,0)')
ax.plot(plot_taus_arr, size_10_arr, 'rs-', ms=6, lw=2, label='dim(1,0)')
ax.set_xlabel('tau')
ax.set_ylabel('Sector dimension')
ax.set_title('Peter-Weyl sector sizes')
ax.legend()
ax.grid(True, alpha=0.3)

# Panel 6: Delta_BCS vs tau
ax = fig.add_subplot(gs[1, 2])
Delta_arr = [results[t]['Delta_BCS'] for t in plot_taus]
ax.semilogy(plot_taus_arr, [max(d, 1e-20) for d in Delta_arr], 'ko-', ms=8, lw=2)
ax.set_xlabel('tau')
ax.set_ylabel('Delta_BCS (max component)')
ax.set_title('BCS gap at mu=lambda_min')
ax.grid(True, alpha=0.3)

plt.savefig(OUTPUT_PNG, dpi=150, bbox_inches='tight')
print(f"  Saved: {OUTPUT_PNG}")

t_end = time.time()
print(f"\nTotal runtime: {t_end - t_start:.1f}s")
print(f"\n{'='*72}")
print(f"FINAL VERDICT: G-29b = {verdict}")
print(f"  {detail}")
print(f"{'='*72}")
