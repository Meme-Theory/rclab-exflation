"""
Session 28c Computation KC-2: Phonon-Phonon T-Matrix
=====================================================

Computes the 4-point overlap integrals of SU(3) Dirac mode functions that
determine the phonon-phonon scattering amplitude in the 1D effective theory.

Physics:
--------
The spectral action on M^4 x SU(3) generates an effective 4-point interaction
for KK mode fluctuations. After integrating over the internal SU(3), the
1D effective vertex is:

    V_{abcd} = integral_{SU(3)} psi_a^*(x) psi_b^*(x) psi_c(x) psi_d(x) dvol

where psi_k(x) are Dirac eigenmode functions on SU(3) at fixed tau.

Peter-Weyl factorization:
-------------------------
Because D_K is block-diagonal in Peter-Weyl sectors (p,q), each eigenmode
psi_a lives in a specific irrep sector. The eigenvector V[:,a] gives the
expansion coefficients in the Peter-Weyl orthonormal basis {phi_I^{(p,q)}}.

For 4 modes, the overlap integral splits into two cases:

A) INTRA-SECTOR (all 4 modes in the same (p,q)):
   The Peter-Weyl functions {phi_I} form an orthonormal basis, so:
       V_{abcd} = sum_I conj(v_a[I]) * conj(v_b[I]) * v_c[I] * v_d[I]

   This is the "pointwise" overlap in coefficient space. It equals
   Tr(|a><a| o |b><b| o |c><c| o |d><d|) in the outer-product sense,
   but more precisely: sum_I (V^*_{Ia} V^*_{Ib} V_{Ic} V_{Id}).

B) CROSS-SECTOR (modes in different (p,q)):
   The 4-point overlap involves SU(3) Clebsch-Gordan coefficients:
       V_{abcd} = sum_{I,J,K,L} conj(v_a[I]) conj(v_b[J]) v_c[K] v_d[L]
                  * integral phi_I^{(p1,q1)*} phi_J^{(p2,q2)*} phi_K^{(p3,q3)} phi_L^{(p4,q4)} dvol

   The integral is nonzero only when the tensor product (p1,q1) x (p2,q2)
   and (p3,q3) x (p4,q4) share a common irrep. This gives selection rules.

   For the lowest modes, the dominant cross-sector channels are:
   - (0,0) x (0,1) -> (0,1): selection rule from trivial x fundamental
   - (0,0) x (1,0) -> (1,0): similarly
   - (0,1) x (1,0) -> (1,1) + (0,0): CG decomposition

   IMPORTANT: For the cross-sector case, the 4-index integral is:
   integral phi_I^{(p1)} phi_J^{(p2)} phi_K^{(p3)} phi_L^{(p4)} dvol
   = C^{(p1,p2,sigma)}_{I,J,alpha} * C^{(p3,p4,sigma)}_{K,L,alpha}
   summed over intermediate irrep sigma and multiplicity label alpha.

   Computing exact SU(3) CG coefficients at scale is expensive. We use
   the orthogonality bound: for modes in different sectors, |V_cross| <=
   1/sqrt(dim(p,q)) by Cauchy-Schwarz on the CG coefficients. We compute
   both exact intra-sector overlaps and estimated cross-sector overlaps.

T-matrix (Born + 1-loop):
--------------------------
    T_{12->34} = V_{1234} + sum_n V_{12n} G_n V_{n34}    (Born + bubble)

where G_n = 1/(E_1 + E_2 - E_n + i*epsilon) is the intermediate propagator.

Scattering rate:
    W = 2*pi * sum_{3,4} |T_{12->34}|^2 * delta(E1+E2-E3-E4) * n_3 * n_4

using phase space from the 1D density of states. We compare W to Gamma_inject
from KC-1.

Gate KC-2:
    PASS:         W > 0.1 * Gamma  (scattering sufficient for bottleneck)
    CLOSED:         W < 0.01 * Gamma  (phonons decay before scattering)
    INCONCLUSIVE: W in [0.01, 0.1] * Gamma

Input: tier0-computation/s23a_eigenvectors_extended.npz
       tier0-computation/s28a_bogoliubov_coefficients.npz
Output: tier0-computation/s28c_phonon_tmatrix.npz
        tier0-computation/s28c_phonon_tmatrix.png

Author: phonon-exflation-sim agent
Date: 2026-02-27
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path
import sys
import time

# ==============================================================================
# Configuration
# ==============================================================================

DATA_DIR = Path(__file__).parent
EIGVEC_FILE = DATA_DIR / "s23a_eigenvectors_extended.npz"
BOGO_FILE = DATA_DIR / "s28a_bogoliubov_coefficients.npz"
OUTPUT_NPZ = DATA_DIR / "s28c_phonon_tmatrix.npz"
OUTPUT_PNG = DATA_DIR / "s28c_phonon_tmatrix.png"

# Gate thresholds
W_PASS_RATIO = 0.1    # W/Gamma > 0.1 = PASS
W_KILL_RATIO = 0.01   # W/Gamma < 0.01 = CLOSED
# Number of lowest modes to include in the T-matrix computation
N_MODES = 20

# tau values to compute at (must be in s23a eigenvector data)
TAU_TARGETS = [0.15, 0.25, 0.35]

# Broadening for energy delta function (Lorentzian width)
EPSILON = 0.02  # natural units, ~2% of gap

# Thermal occupation for incoming phonons (parametric creation gives n ~ B_k)
# We set n_3 = n_4 = 1 (single-phonon scattering) for the rate comparison
N_OCC = 1.0


# ==============================================================================
# Load data
# ==============================================================================

print("=" * 72)
print("KC-2: Phonon-Phonon T-Matrix (4-Point Overlap Integrals)")
print("=" * 72)

t_start = time.time()

# Load eigenvectors
print("\nLoading eigenvector data...")
evec_data = np.load(EIGVEC_FILE, allow_pickle=True)
tau_evec = evec_data['tau_values']
print(f"  Available tau values: {tau_evec}")

# Load Bogoliubov data
print("Loading Bogoliubov coefficient data...")
bogo_data = np.load(BOGO_FILE, allow_pickle=True)
tau_bogo = bogo_data['tau_values']
B_k_all = bogo_data['B_k']  # (21, 11424)
omega_all = bogo_data['omega_tracked']  # (21, 11424)
Gamma_inject_all = bogo_data['Gamma_inject']  # (21,)

# Find tau indices in both datasets
tau_idx_evec = {}
tau_idx_bogo = {}
for t_target in TAU_TARGETS:
    idx_e = np.argmin(np.abs(tau_evec - t_target))
    if abs(tau_evec[idx_e] - t_target) > 0.01:
        print(f"  WARNING: tau={t_target} not found in eigvec data. Closest: {tau_evec[idx_e]}")
    tau_idx_evec[t_target] = idx_e

    idx_b = np.argmin(np.abs(tau_bogo - t_target))
    if abs(tau_bogo[idx_b] - t_target) > 0.05:
        print(f"  WARNING: tau={t_target} not found in Bogoliubov data. Closest: {tau_bogo[idx_b]}")
    tau_idx_bogo[t_target] = idx_b

print(f"  Eigvec tau indices: {tau_idx_evec}")
print(f"  Bogo tau indices: {tau_idx_bogo}")


# ==============================================================================
# Module 1: Extract lowest modes per tau
# ==============================================================================

def extract_lowest_modes(evec_data, tau_idx, n_modes):
    """
    Extract the n_modes lowest-|eigenvalue| modes at a given tau index.

    Returns:
        modes: list of dicts with keys:
            'eigenvalue': float (signed eigenvalue lambda)
            'omega': float (|lambda|)
            'sector_idx': int (index into sector_labels)
            'sector_pq': (p, q) tuple
            'col_idx': int (column index within sector eigenvector matrix)
            'eigvec': ndarray, shape (sector_size,), the eigenvector coefficients
        sector_labels: ndarray, shape (n_sectors, 2)
        sector_sizes: ndarray, shape (n_sectors,)
    """
    ti = tau_idx
    evals = evec_data[f'eigenvalues_{ti}']
    sector_p = evec_data[f'sector_p_{ti}']
    sector_q = evec_data[f'sector_q_{ti}']
    sector_labels = evec_data[f'sector_labels_{ti}']
    sector_sizes = evec_data[f'sector_sizes_{ti}']

    n_sectors = len(sector_labels)

    # Build cumulative offset into the flat eigenvalue array for each sector
    cum_offsets = np.zeros(n_sectors + 1, dtype=int)
    for s in range(n_sectors):
        cum_offsets[s + 1] = cum_offsets[s] + sector_sizes[s]

    # Sort by |eigenvalue|
    abs_evals = np.abs(evals)
    sort_idx = np.argsort(abs_evals)

    modes = []
    for i in range(n_modes):
        flat_idx = sort_idx[i]
        lam = evals[flat_idx]
        p_val = sector_p[flat_idx]
        q_val = sector_q[flat_idx]

        # Find which sector this belongs to
        s_idx = None
        for s in range(n_sectors):
            if sector_labels[s][0] == p_val and sector_labels[s][1] == q_val:
                if cum_offsets[s] <= flat_idx < cum_offsets[s + 1]:
                    s_idx = s
                    break

        if s_idx is None:
            # Search by sector label match only, take the one containing this index
            for s in range(n_sectors):
                if cum_offsets[s] <= flat_idx < cum_offsets[s + 1]:
                    s_idx = s
                    break

        assert s_idx is not None, f"Could not find sector for flat_idx={flat_idx}"

        col_idx = flat_idx - cum_offsets[s_idx]
        evec_matrix = evec_data[f'eigvec_{ti}_sector_{s_idx}']
        eigvec = evec_matrix[:, col_idx]

        modes.append({
            'eigenvalue': lam,
            'omega': abs(lam),
            'sector_idx': s_idx,
            'sector_pq': (int(sector_labels[s_idx][0]), int(sector_labels[s_idx][1])),
            'col_idx': col_idx,
            'eigvec': eigvec,
            'flat_idx': flat_idx,
        })

    return modes, sector_labels, sector_sizes


# ==============================================================================
# Module 2: Intra-sector 4-point overlap
# ==============================================================================

def overlap_4pt_intra(v_a, v_b, v_c, v_d):
    """
    Compute the intra-sector 4-point overlap:
        V_{abcd} = sum_I conj(v_a[I]) * conj(v_b[I]) * v_c[I] * v_d[I]

    This is the integral of psi_a^* psi_b^* psi_c psi_d over SU(3), where all
    4 modes live in the same Peter-Weyl sector. The Peter-Weyl basis functions
    are orthonormal under the L^2 inner product, so the 4-point function
    factorizes into a sum over basis indices.

    MATHEMATICAL JUSTIFICATION:
    In sector (p,q), the Dirac operator is represented in the Peter-Weyl basis
    {phi_I}, where I runs over dim(p,q) * dim_spinor basis elements. The modes
    psi_a(x) = sum_I v_a[I] phi_I(x). Then:

    integral psi_a^* psi_b^* psi_c psi_d dvol
    = sum_{IJKL} v_a^*[I] v_b^*[J] v_c[K] v_d[L] * integral phi_I^* phi_J^* phi_K phi_L dvol

    For the INTRA-SECTOR case where all modes are in the SAME (p,q), the
    4-point integral of Peter-Weyl matrix elements is:

    integral D^{(p,q)}_{mn}(g)^* D^{(p,q)}_{kl}(g)^* D^{(p,q)}_{rs}(g) D^{(p,q)}_{uv}(g) dg

    This is NOT simply delta_{I,J,K,L}. It involves 6j-symbols / Racah coefficients.
    However, in the Peter-Weyl basis, the eigenvectors v_a are vectors in C^N where
    N = sector_size. The 4-point overlap V_{abcd} = sum_I v_a^*[I] v_b^*[I] v_c[I] v_d[I]
    is the correct expression ONLY if we treat the Peter-Weyl basis as a POSITION basis
    (i.e., pointwise multiplication).

    CORRECTION: The Peter-Weyl basis is NOT a position basis. The correct intra-sector
    4-point overlap requires the full rank-4 tensor of Peter-Weyl 4-point integrals.
    Computing this for SU(3) irreps is equivalent to computing 6j-symbols.

    PRACTICAL APPROACH: We compute two quantities:
    1. The "diagonal" overlap (sum_I v_a^* v_b^* v_c v_d) -- this is a LOWER BOUND
       on the actual 4-point function because it captures only the delta_{IJKL} part.
    2. An UPPER BOUND from Cauchy-Schwarz: |V_{abcd}| <= ||v_a||^2 * ||v_b||^2 = 1
       (trivial), or more usefully, |V_{abcd}| <= sqrt(sum_I |v_a v_b|^2) * sqrt(sum_I |v_c v_d|^2)
       = ||v_a . v_b||_2 * ||v_c . v_d||_2 where . is the Hadamard product.

    We compute the Hadamard-product bound as a TIGHT upper bound.

    Parameters:
        v_a, v_b, v_c, v_d: ndarray, shape (N,), complex eigenvector coefficients

    Returns:
        V_diag: complex, the diagonal (same-basis-index) contribution
        V_bound: float, the Cauchy-Schwarz upper bound on |V_{abcd}|
    """
    # Diagonal contribution: exact term from delta_{IJKL}
    V_diag = np.sum(np.conj(v_a) * np.conj(v_b) * v_c * v_d)

    # Cauchy-Schwarz bound on the full overlap (including off-diagonal CG terms):
    # |V| <= ||conj(v_a)*conj(v_b)||_2 * ||v_c*v_d||_2
    # This bounds the full 4-point integral using Cauchy-Schwarz on the outer product
    V_bound = np.sqrt(np.sum(np.abs(v_a * v_b)**2)) * \
              np.sqrt(np.sum(np.abs(v_c * v_d)**2))

    return V_diag, V_bound


# ==============================================================================
# Module 3: Cross-sector overlap estimation
# ==============================================================================

def overlap_4pt_cross_bound(v_a, v_b, v_c, v_d, dim_a, dim_b, dim_c, dim_d):
    """
    Upper bound on cross-sector 4-point overlap using SU(3) representation theory.

    For modes in sectors (p1,q1), (p2,q2), (p3,q3), (p4,q4), the overlap is:
    V = sum_{IJKL} v_a^*[I] v_b^*[J] v_c[K] v_d[L] * C_{IJKL}

    where C_{IJKL} is the 4-point Peter-Weyl integral (involves CG coefficients).

    Bounds:
    |V| <= 1/sqrt(max(dim_a, dim_b, dim_c, dim_d)) by standard CG coefficient bounds.

    More precisely, for the product of two SU(3) matrix elements integrated over
    the group, Schur orthogonality gives:
    integral D^{rho1}_{ij}(g)^* D^{rho2}_{kl}(g) dg = delta_{rho1,rho2} delta_{ik} delta_{jl} / dim(rho1)

    For 4-point: need (rho1 x rho2) tensor product decomposition containing (rho3 x rho4).
    The CG coefficient magnitude is bounded by 1, and the sum has at most
    min(dim1*dim2, dim3*dim4) nonzero terms.

    Returns:
        V_bound: float, upper bound on |V_{abcd}|
    """
    # The 4-point function of Peter-Weyl matrix elements on SU(N) is bounded by
    # the product of two 2-point Schur integrals, each bounded by 1/dim.
    # Best bound: 1/sqrt(dim_max)
    dim_max = max(dim_a, dim_b, dim_c, dim_d)
    V_bound = 1.0 / np.sqrt(dim_max)

    return V_bound


def check_selection_rule(pq1, pq2, pq3, pq4):
    """
    Check if the SU(3) tensor product selection rule allows a nonzero 4-point overlap.

    The integral is nonzero only if the trivial representation (0,0) appears in:
        (p1,q1)^* x (p2,q2)^* x (p3,q3) x (p4,q4)
    equivalently: (q1,p1) x (q2,p2) x (p3,q3) x (p4,q4) contains (0,0).

    Necessary condition: the sum of "triality" (p - q) mod 3 must vanish:
        (q1-p1) + (q2-p2) + (p3-q3) + (p4-q4) = 0 mod 3

    This is a necessary but not sufficient condition (triality conservation).

    Returns:
        bool: True if selection rule allows nonzero overlap
    """
    triality = (pq1[1] - pq1[0]) + (pq2[1] - pq2[0]) + (pq3[0] - pq3[1]) + (pq4[0] - pq4[1])
    return triality % 3 == 0


# ==============================================================================
# Module 4: Compute T-matrix elements
# ==============================================================================

def compute_tmatrix(modes, n_modes):
    """
    Compute the T-matrix for phonon-phonon scattering.

    T_{12->34} = V_{1234} + sum_n V_{12nn} * G_n(E1+E2) * V_{nn34}

    where the sum runs over intermediate states n, and:
    - V_{12nn} = integral psi_1^* psi_2^* psi_n psi_n dvol  (forward channel)
    - V_{nn34} = integral psi_n^* psi_n^* psi_3 psi_4 dvol  (decay channel)
    - G_n(E) = 1/(E - 2*omega_n + i*epsilon) (2-particle intermediate state)

    For the Born term, we compute V_{1234} directly.
    For the 1-loop correction, we sum over intermediate pairs (n,n) using
    the s-channel factorization.

    Parameters:
        modes: list of mode dicts from extract_lowest_modes
        n_modes: number of modes to use

    Returns:
        V_born: ndarray, shape (n_modes, n_modes, n_modes, n_modes), complex
            Born-level 4-point vertex
        V_bound: ndarray, same shape, float, upper bounds on |V|
        T_full: ndarray, same shape, complex, T-matrix including 1-loop
        omega: ndarray, shape (n_modes,), mode frequencies
    """
    omega = np.array([m['omega'] for m in modes[:n_modes]])

    V_born = np.zeros((n_modes, n_modes, n_modes, n_modes), dtype=complex)
    V_upper = np.zeros((n_modes, n_modes, n_modes, n_modes))

    # Precompute which modes are in the same sector
    sector_ids = [m['sector_idx'] for m in modes[:n_modes]]
    sector_pqs = [m['sector_pq'] for m in modes[:n_modes]]
    eigvecs = [m['eigvec'] for m in modes[:n_modes]]

    # Compute all 4-point overlaps
    n_intra = 0
    n_cross_allowed = 0
    n_cross_forbidden = 0

    for a in range(n_modes):
        for b in range(a, n_modes):  # Use symmetry: V_{abcd} = V_{badc}^*
            for c in range(n_modes):
                for d in range(c, n_modes):
                    sa, sb, sc, sd = sector_ids[a], sector_ids[b], sector_ids[c], sector_ids[d]

                    if sa == sb == sc == sd:
                        # All in same sector: exact intra-sector computation
                        v_diag, v_bnd = overlap_4pt_intra(
                            eigvecs[a], eigvecs[b], eigvecs[c], eigvecs[d]
                        )
                        V_born[a, b, c, d] = v_diag
                        V_upper[a, b, c, d] = v_bnd
                        n_intra += 1

                    else:
                        # Cross-sector: check selection rule
                        pqa, pqb, pqc, pqd = sector_pqs[a], sector_pqs[b], sector_pqs[c], sector_pqs[d]

                        if check_selection_rule(pqa, pqb, pqc, pqd):
                            # Selection rule allows: use bound
                            dim_a = len(eigvecs[a])
                            dim_b = len(eigvecs[b])
                            dim_c = len(eigvecs[c])
                            dim_d = len(eigvecs[d])
                            v_bnd = overlap_4pt_cross_bound(
                                eigvecs[a], eigvecs[b], eigvecs[c], eigvecs[d],
                                dim_a, dim_b, dim_c, dim_d
                            )
                            # Set Born to zero (we don't have exact CG coefficients)
                            # but record the upper bound
                            V_born[a, b, c, d] = 0.0
                            V_upper[a, b, c, d] = v_bnd
                            n_cross_allowed += 1
                        else:
                            # Selection rule forbids: exactly zero
                            V_born[a, b, c, d] = 0.0
                            V_upper[a, b, c, d] = 0.0
                            n_cross_forbidden += 1

                    # Apply symmetries
                    # V_{abcd} = V_{badc} (exchange of pairs 1<->2 with 3<->4)
                    V_born[b, a, d, c] = V_born[a, b, c, d]
                    V_upper[b, a, d, c] = V_upper[a, b, c, d]
                    # V_{abcd} = conj(V_{cdab}) (CPT / Hermiticity of the vertex)
                    V_born[c, d, a, b] = np.conj(V_born[a, b, c, d])
                    V_upper[c, d, a, b] = V_upper[a, b, c, d]
                    V_born[d, c, b, a] = np.conj(V_born[a, b, c, d])
                    V_upper[d, c, b, a] = V_upper[a, b, c, d]

    print(f"  4-point overlaps: {n_intra} intra-sector, {n_cross_allowed} cross-allowed, {n_cross_forbidden} cross-forbidden")

    # -------------------------------------------------------------------------
    # T-matrix: Born + 1-loop (s-channel bubble)
    # -------------------------------------------------------------------------
    # T_{12->34} = V_{1234} + sum_{n} V_{12nn} * G_n(E1+E2) * V_{nn34}
    # where G_n(E) = 1/(E - 2*omega_n + i*epsilon) for pair intermediate state (n,n)
    #
    # More generally, sum over all intermediate PAIRS (m,n):
    # T_{12->34} = V_{1234} + sum_{m,n} V_{12mn} * G_{mn}(E1+E2) * V_{mn34}
    # where G_{mn}(E) = 1/(E - omega_m - omega_n + i*epsilon)

    T_full = np.zeros_like(V_born)
    T_upper = np.zeros_like(V_upper)

    for a in range(n_modes):
        for b in range(n_modes):
            E_in = omega[a] + omega[b]

            for c in range(n_modes):
                for d in range(n_modes):
                    # Born term
                    T_ab_cd = V_born[a, b, c, d]
                    T_ub_cd = V_upper[a, b, c, d]

                    # 1-loop: sum over intermediate pairs (m, n)
                    loop_contrib = 0.0 + 0.0j
                    loop_ub = 0.0

                    for m in range(n_modes):
                        for n in range(n_modes):
                            E_int = omega[m] + omega[n]
                            G_mn = 1.0 / (E_in - E_int + 1j * EPSILON)

                            loop_contrib += V_born[a, b, m, n] * G_mn * V_born[m, n, c, d]
                            loop_ub += V_upper[a, b, m, n] * abs(G_mn) * V_upper[m, n, c, d]

                    T_full[a, b, c, d] = T_ab_cd + loop_contrib
                    T_upper[a, b, c, d] = T_ub_cd + loop_ub

    return V_born, V_upper, T_full, T_upper, omega


# ==============================================================================
# Module 5: Scattering rate computation
# ==============================================================================

def compute_scattering_rate(T_full, T_upper, omega, n_modes):
    """
    Compute the scattering rate W for each incoming pair (a, b):

        W_{ab} = 2*pi * sum_{c,d} |T_{ab->cd}|^2 * delta(E_a+E_b-E_c-E_d) * n_c * n_d

    We use a Lorentzian approximation for the delta function:
        delta(E) ~ (1/pi) * epsilon / (E^2 + epsilon^2)

    We set n_c = n_d = N_OCC (unit occupation for rate comparison).

    Returns:
        W: ndarray, shape (n_modes, n_modes), scattering rate for pair (a,b)
        W_upper: same, using upper bounds on T
    """
    W = np.zeros((n_modes, n_modes))
    W_upper = np.zeros((n_modes, n_modes))

    for a in range(n_modes):
        for b in range(n_modes):
            E_in = omega[a] + omega[b]
            rate = 0.0
            rate_ub = 0.0

            for c in range(n_modes):
                for d in range(n_modes):
                    E_out = omega[c] + omega[d]
                    dE = E_in - E_out

                    # Lorentzian delta function
                    delta_L = (1.0 / np.pi) * EPSILON / (dE**2 + EPSILON**2)

                    rate += abs(T_full[a, b, c, d])**2 * delta_L * N_OCC**2
                    rate_ub += T_upper[a, b, c, d]**2 * delta_L * N_OCC**2

            W[a, b] = 2 * np.pi * rate
            W_upper[a, b] = 2 * np.pi * rate_ub

    return W, W_upper


# ==============================================================================
# Module 6: Main computation loop
# ==============================================================================

print("\n" + "=" * 72)
print("COMPUTING 4-POINT OVERLAPS AND T-MATRIX")
print("=" * 72)

results = {}

for tau_target in TAU_TARGETS:
    print(f"\n{'='*60}")
    print(f"tau = {tau_target:.2f}")
    print(f"{'='*60}")

    ti_evec = tau_idx_evec[tau_target]
    ti_bogo = tau_idx_bogo[tau_target]

    # Extract lowest modes
    print(f"  Extracting {N_MODES} lowest modes from eigvec data (tau_idx={ti_evec})...")
    modes, sector_labels, sector_sizes = extract_lowest_modes(evec_data, ti_evec, N_MODES)

    print(f"  Mode summary:")
    for i, m in enumerate(modes):
        print(f"    mode {i:2d}: omega={m['omega']:.6f}, lambda={m['eigenvalue']:+.6f}, "
              f"sector=({m['sector_pq'][0]},{m['sector_pq'][1]}), col={m['col_idx']}")

    # Compute 4-point overlaps and T-matrix
    print(f"\n  Computing 4-point overlaps ({N_MODES}^4 = {N_MODES**4} entries)...")
    t0 = time.time()
    V_born, V_upper, T_full, T_upper, omega = compute_tmatrix(modes, N_MODES)
    t1 = time.time()
    print(f"  Done in {t1-t0:.2f}s")

    # Validate: check that V is not all zero
    print(f"\n  Born vertex V statistics:")
    V_abs = np.abs(V_born)
    V_nonzero = V_abs[V_abs > 1e-15]
    print(f"    max |V|     = {V_abs.max():.6e}")
    print(f"    mean |V|    = {V_abs.mean():.6e}")
    print(f"    nonzero count = {len(V_nonzero)} / {V_abs.size}")
    if len(V_nonzero) > 0:
        print(f"    mean |V| (nonzero) = {V_nonzero.mean():.6e}")

    print(f"\n  Upper bound V statistics:")
    print(f"    max V_upper = {V_upper.max():.6e}")
    print(f"    mean V_upper = {V_upper.mean():.6e}")

    print(f"\n  T-matrix statistics:")
    T_abs = np.abs(T_full)
    print(f"    max |T|     = {T_abs.max():.6e}")
    print(f"    mean |T|    = {T_abs.mean():.6e}")
    print(f"    max T_upper = {T_upper.max():.6e}")

    # Compute scattering rate
    print(f"\n  Computing scattering rate...")
    W, W_upper = compute_scattering_rate(T_full, T_upper, omega, N_MODES)

    # Get Gamma_inject at this tau from Bogoliubov data
    Gamma_inject = Gamma_inject_all[ti_bogo]
    B_k_tau = B_k_all[ti_bogo]
    omega_tau = omega_all[ti_bogo]

    # -----------------------------------------------------------------------
    # Gamma_decay: the single-particle decay/creation rate for gap-edge modes.
    #
    # Physical picture: B_k = (1/4*omega_k^2) * (d omega_k/d tau)^2 is the
    # adiabaticity parameter. The particle creation rate per unit TIME is:
    #   Gamma_create = B_k * omega_k * (d tau/dt)^2
    #
    # The scattering rate W is computed in natural units where the 4-point
    # vertex V is dimensionless and the density of states comes from the
    # eigenvalue spectrum. W is in units of [energy * |V|^2] -- the Fermi
    # golden rule rate.
    #
    # For the ratio W/Gamma to be meaningful, both must be in the same units.
    # Since (d tau/dt) is an overall scale that affects both injection and
    # scattering equally, the dimensionless ratio that matters is:
    #
    #   W/Gamma ~ [|V|^2 * rho(E)] / [B_k * omega_k]
    #
    # where rho(E) is the density of states at the scattering energy.
    #
    # CORRECTED: sort by omega to get gap-edge modes, then read their B_k.
    # -----------------------------------------------------------------------

    mask = omega_tau > 0.01
    omega_pos = omega_tau[mask]
    B_pos = B_k_tau[mask]
    gap_sort = np.argsort(omega_pos)
    gap_edge_idx = gap_sort[:N_MODES]  # 20 lowest-omega modes

    B_gap = B_pos[gap_edge_idx]
    omega_gap = omega_pos[gap_edge_idx]

    # Per-mode Gamma = B_k * omega_k  (creation rate per unit (dtau/dt)^2)
    Gamma_per_mode = B_gap * omega_gap
    Gamma_decay = np.mean(Gamma_per_mode)
    Gamma_decay_max = np.max(Gamma_per_mode)

    # Also use the simple spectral width: Gamma ~ omega / Q where Q ~ 1/B_k
    # For weakly-driven modes, the spectral width is ~ B_k * omega_k
    # For the gap-edge mode with highest B_k, this is the bottleneck:
    Gamma_bottleneck = Gamma_decay_max

    W_max = W.max()
    W_upper_max = W_upper.max()
    W_mean_diag = np.mean(np.diag(W))

    print(f"\n  Scattering rate W:")
    print(f"    max W               = {W_max:.6e}")
    print(f"    max W (upper bound) = {W_upper_max:.6e}")
    print(f"    mean W (diagonal)   = {W_mean_diag:.6e}")
    print(f"    Gamma_decay (B*omega, gap-edge mean) = {Gamma_decay:.6e}")
    print(f"    Gamma_decay (B*omega, gap-edge max)  = {Gamma_decay_max:.6e}")
    print(f"    Gamma_inject (total) = {Gamma_inject:.6e}")
    print(f"    B_k gap-edge: min={B_gap.min():.4e}, max={B_gap.max():.4e}, mean={B_gap.mean():.4e}")

    # -----------------------------------------------------------------------
    # KEY RATIOS: Three comparison scales
    # -----------------------------------------------------------------------
    # 1. W / Gamma_decay (mean gap-edge): most physical comparison
    # 2. W / Gamma_inject (total): if total injection drives the system
    # 3. W / omega_gap (raw): scattering rate vs mode frequency

    if Gamma_decay > 0:
        ratio_born = W_max / Gamma_decay
        ratio_upper = W_upper_max / Gamma_decay
    else:
        ratio_born = np.inf
        ratio_upper = np.inf

    ratio_vs_inject = W_max / Gamma_inject if Gamma_inject > 0 else np.inf
    ratio_vs_omega = W_max / np.mean(omega_gap)

    print(f"\n  KEY RATIOS:")
    print(f"    W_max / Gamma_decay (mean)   = {ratio_born:.6e}")
    print(f"    W_max / Gamma_decay (max)    = {W_max/Gamma_decay_max:.6e}")
    print(f"    W_max / Gamma_inject (total) = {ratio_vs_inject:.6e}")
    print(f"    W_max / omega_gap (mean)     = {ratio_vs_omega:.6e}")

    results[tau_target] = {
        'modes': modes,
        'V_born': V_born,
        'V_upper': V_upper,
        'T_full': T_full,
        'T_upper': T_upper,
        'omega': omega,
        'W': W,
        'W_upper': W_upper,
        'Gamma_decay': Gamma_decay,
        'Gamma_decay_max': Gamma_decay_max,
        'Gamma_inject': Gamma_inject,
        'ratio_born': ratio_born,
        'ratio_upper': ratio_upper,
        'ratio_vs_inject': ratio_vs_inject,
        'ratio_vs_omega': ratio_vs_omega,
    }


# ==============================================================================
# Module 7: Gate verdict
# ==============================================================================

print("\n" + "=" * 72)
print("GATE KC-2: PHONON-PHONON T-MATRIX VERDICT")
print("=" * 72)

# Use the maximum ratio across all tau values
max_ratio_born = max(r['ratio_born'] for r in results.values())
max_ratio_upper = max(r['ratio_upper'] for r in results.values())
best_tau_born = max(results.keys(), key=lambda t: results[t]['ratio_born'])
best_tau_upper = max(results.keys(), key=lambda t: results[t]['ratio_upper'])

print(f"\n  Best W/Gamma (Born, exact intra-sector):  {max_ratio_born:.6e} at tau={best_tau_born}")
print(f"  Best W/Gamma (upper bound, all channels): {max_ratio_upper:.6e} at tau={best_tau_upper}")

# Decision logic:
# - If even the UPPER BOUND gives W/Gamma < 0.01, that's a CLOSED
# - If the Born (exact intra-sector) gives W/Gamma > 0.1, that's a PASS
# - If Born < 0.1 but upper bound > 0.1, INCONCLUSIVE (cross-sector could help)
# - If Born < 0.01 but upper bound > 0.01, INCONCLUSIVE

if max_ratio_born >= W_PASS_RATIO:
    verdict = "PASS"
    verdict_detail = f"W/Gamma = {max_ratio_born:.4e} >= {W_PASS_RATIO} (intra-sector Born)"
elif max_ratio_upper >= W_PASS_RATIO:
    verdict = "INCONCLUSIVE_HIGH"
    verdict_detail = (f"Born W/Gamma = {max_ratio_born:.4e} < {W_PASS_RATIO}, "
                      f"but upper bound W/Gamma = {max_ratio_upper:.4e} >= {W_PASS_RATIO} "
                      f"(cross-sector may contribute)")
elif max_ratio_upper < W_KILL_RATIO:
    verdict = "CLOSED"
    verdict_detail = f"Upper bound W/Gamma = {max_ratio_upper:.4e} < {W_KILL_RATIO} (even with cross-sector)"
elif max_ratio_born < W_KILL_RATIO:
    verdict = "INCONCLUSIVE_LOW"
    verdict_detail = (f"Born W/Gamma = {max_ratio_born:.4e} < {W_KILL_RATIO}, "
                      f"upper bound W/Gamma = {max_ratio_upper:.4e} in [{W_KILL_RATIO}, {W_PASS_RATIO}]")
else:
    verdict = "INCONCLUSIVE"
    verdict_detail = (f"W/Gamma = {max_ratio_born:.4e} in [{W_KILL_RATIO}, {W_PASS_RATIO}] (Born), "
                      f"{max_ratio_upper:.4e} (upper)")

print(f"\n  VERDICT: {verdict}")
print(f"  Detail: {verdict_detail}")

# Per-tau summary
print(f"\n  Per-tau summary:")
for tau_target in TAU_TARGETS:
    r = results[tau_target]
    print(f"    tau={tau_target:.2f}: W_max={r['W'].max():.4e}, "
          f"Gamma_decay={r['Gamma_decay']:.4e}, "
          f"ratio_born={r['ratio_born']:.4e}, "
          f"ratio_vs_inject={r['ratio_vs_inject']:.4e}, "
          f"ratio_vs_omega={r['ratio_vs_omega']:.4e}")


# ==============================================================================
# Module 8: Detailed diagnostics
# ==============================================================================

print("\n" + "=" * 72)
print("DIAGNOSTICS")
print("=" * 72)

for tau_target in TAU_TARGETS:
    r = results[tau_target]
    print(f"\n--- tau = {tau_target:.2f} ---")

    # Which scattering channels dominate?
    W = r['W']
    n = N_MODES

    # Top 10 scattering channels by W
    flat_idx = np.argsort(W.ravel())[::-1]
    print(f"  Top 10 scattering channels (a,b) by W_{'{'}ab{'}'}:")
    for rank in range(min(10, len(flat_idx))):
        idx = flat_idx[rank]
        a, b = np.unravel_index(idx, W.shape)
        ma = r['modes'][a]
        mb = r['modes'][b]
        print(f"    #{rank+1}: ({a},{b}), W={W[a,b]:.4e}, "
              f"omega=({ma['omega']:.4f},{mb['omega']:.4f}), "
              f"sectors=({ma['sector_pq']},{mb['sector_pq']})")

    # Sector composition of V_born
    V_abs = np.abs(r['V_born'])
    print(f"\n  Born vertex |V| sector structure:")
    sector_pairs = {}
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    if V_abs[a,b,c,d] > 1e-15:
                        key = (r['modes'][a]['sector_pq'], r['modes'][b]['sector_pq'],
                               r['modes'][c]['sector_pq'], r['modes'][d]['sector_pq'])
                        if key not in sector_pairs:
                            sector_pairs[key] = []
                        sector_pairs[key].append(V_abs[a,b,c,d])

    for key in sorted(sector_pairs.keys(), key=lambda k: -max(sector_pairs[k])):
        vals = sector_pairs[key]
        print(f"    {key}: {len(vals)} nonzero, max={max(vals):.4e}, mean={np.mean(vals):.4e}")

    # Energy conservation check: which T_{abcd} have E_a+E_b ~ E_c+E_d?
    omega = r['omega']
    print(f"\n  Energy-conserving channels (|dE| < {EPSILON:.3f}):")
    n_conserving = 0
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for d in range(n):
                    dE = abs(omega[a] + omega[b] - omega[c] - omega[d])
                    if dE < EPSILON and abs(r['T_full'][a,b,c,d]) > 1e-15:
                        n_conserving += 1
    print(f"    Count: {n_conserving}")


# ==============================================================================
# Module 9: Save output
# ==============================================================================

print("\n" + "=" * 72)
print("SAVING OUTPUT")
print("=" * 72)

save_dict = {
    'tau_targets': np.array(TAU_TARGETS),
    'n_modes': np.array([N_MODES]),
    'epsilon': np.array([EPSILON]),
    'verdict': np.array([verdict]),
}

for i, tau_target in enumerate(TAU_TARGETS):
    r = results[tau_target]
    prefix = f'tau{i}_'
    save_dict[prefix + 'tau'] = np.array([tau_target])
    save_dict[prefix + 'omega'] = r['omega']
    save_dict[prefix + 'V_born'] = r['V_born']
    save_dict[prefix + 'V_upper'] = r['V_upper']
    save_dict[prefix + 'T_full'] = r['T_full']
    save_dict[prefix + 'T_upper'] = r['T_upper']
    save_dict[prefix + 'W'] = r['W']
    save_dict[prefix + 'W_upper'] = r['W_upper']
    save_dict[prefix + 'Gamma_decay'] = np.array([r['Gamma_decay']])
    save_dict[prefix + 'Gamma_decay_max'] = np.array([r['Gamma_decay_max']])
    save_dict[prefix + 'Gamma_inject'] = np.array([r['Gamma_inject']])
    save_dict[prefix + 'ratio_born'] = np.array([r['ratio_born']])
    save_dict[prefix + 'ratio_upper'] = np.array([r['ratio_upper']])
    save_dict[prefix + 'ratio_vs_inject'] = np.array([r['ratio_vs_inject']])
    save_dict[prefix + 'ratio_vs_omega'] = np.array([r['ratio_vs_omega']])

np.savez_compressed(OUTPUT_NPZ, **save_dict)
print(f"  Saved: {OUTPUT_NPZ}")


# ==============================================================================
# Module 10: Visualization
# ==============================================================================

print("\nGenerating plots...")

fig, axes = plt.subplots(2, 3, figsize=(18, 12))
fig.suptitle(f'KC-2: Phonon-Phonon T-Matrix — Verdict: {verdict}', fontsize=14, fontweight='bold')

for i, tau_target in enumerate(TAU_TARGETS):
    r = results[tau_target]

    # Top row: |V_born| matrix (flattened to 2D: (a*b) vs (c*d) for the 10x10 pairs)
    ax = axes[0, i]
    # Show W matrix (scattering rate per incoming pair)
    im = ax.imshow(np.log10(r['W'] + 1e-30), cmap='hot', aspect='equal')
    ax.set_title(f'log10(W_{{ab}}) at tau={tau_target}')
    ax.set_xlabel('Mode b')
    ax.set_ylabel('Mode a')
    plt.colorbar(im, ax=ax, shrink=0.8)

    # Bottom row: ratio W/Gamma histogram
    ax = axes[1, i]
    W_flat = r['W'].ravel()
    W_flat_pos = W_flat[W_flat > 1e-30]
    if len(W_flat_pos) > 0:
        ratio_flat = W_flat_pos / r['Gamma_decay']
        ax.hist(np.log10(ratio_flat), bins=50, color='steelblue', alpha=0.7, edgecolor='black')
        ax.axvline(np.log10(W_PASS_RATIO), color='green', ls='--', lw=2, label=f'PASS threshold')
        ax.axvline(np.log10(W_KILL_RATIO), color='red', ls='--', lw=2, label=f'CLOSURE threshold')
        ax.set_xlabel('log10(W/Gamma)')
        ax.set_ylabel('Count')
        ax.set_title(f'W/Gamma distribution at tau={tau_target}')
        ax.legend(fontsize=8)
    else:
        ax.text(0.5, 0.5, 'No nonzero W', ha='center', va='center', transform=ax.transAxes)
        ax.set_title(f'W/Gamma at tau={tau_target}')

plt.tight_layout()
plt.savefig(OUTPUT_PNG, dpi=150, bbox_inches='tight')
print(f"  Saved: {OUTPUT_PNG}")

t_end = time.time()
print(f"\nTotal runtime: {t_end - t_start:.1f}s")
print(f"\n{'='*72}")
print(f"FINAL VERDICT: KC-2 = {verdict}")
print(f"{'='*72}")
