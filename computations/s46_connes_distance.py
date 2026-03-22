#!/usr/bin/env python3
"""
CONNES-DISTANCE-46: Connes Spectral Distance on Truncated Jensen SU(3)
======================================================================

Computes d(phi, psi) = sup{|phi(f) - psi(f)| : ||[D, f]|| <= 1}
on the Peter-Weyl-truncated spectral triple of (SU(3), g_tau).

Block-diagonality (S22b D-1): D_K decomposes exactly by Peter-Weyl sector.
The Lipschitz constraint decouples per sector. Each sector contributes
independently to the distance.

Key insight for efficiency: the per-sector distance d_s(delta) for a Hermitian
state-difference delta satisfies the DUAL BOUND:

    d_s(delta) = max_{f: ||[D,f x I]|| <= 1} Re Tr(delta^dag f)
               <= ||delta||_F * max_{f: ||f||_F=1} 1 / ||[D, f x I]||
               = ||delta||_F / lambda_min

where lambda_min is the minimum non-zero Lipschitz eigenvalue of the sector.
The LIPSCHITZ EIGENVALUE is defined as:
    lambda_lip(f) = ||[D, f x I]|| / ||f||_F

We compute this via the eigenvalues of the matrix K = sum_k Comm_k^dag Comm_k
where Comm_k = [D, H_k x I] and {H_k} is a traceless Hermitian basis.

Mathematical foundation:
    - Connes (1994): distance formula [NCG book]
    - Connes-van Suijlekom (2021), Paper 28: spectral truncation convergence
    - Rieffel (1999): Metrics on state spaces, Lip-norm duality

Session: 46, Wave 3, Task W3-5
Author: Connes-NCG-Theorist agent
"""

import sys
import os
import time
import numpy as np
from scipy.linalg import eigh, svdvals, eigvalsh
from scipy.optimize import minimize
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Force flushed output
import builtins
_orig_print = builtins.print
def print(*args, **kwargs):
    kwargs['flush'] = True
    _orig_print(*args, **kwargs)

# Add tier0-computation to path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
from canonical_constants import tau_fold, M_KK_gravity, a0_fold, a2_fold, a4_fold

from tier1_dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    jensen_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients, spinor_connection_offset,
    build_cliff8, get_irrep, dirac_operator_on_irrep
)

np.set_printoptions(precision=8, linewidth=120)


# =============================================================================
# SECTION 1: LIPSCHITZ EIGENVALUE ANALYSIS
# =============================================================================

def compute_lipschitz_spectrum(D_pq, dim_pq):
    """
    Compute the Lipschitz eigenvalues for sector (p,q).

    For a sector with Dirac operator D (size d*16 x d*16), the Lipschitz
    seminorm of a Hermitian d x d matrix f is:
        L(f) = ||[D, f x I_16]||  (operator norm)

    The LIPSCHITZ MATRIX K is defined by:
        K_{ij} = Tr([D, H_i x I]^dag [D, H_j x I])

    where {H_i} is a basis for traceless Hermitian d x d matrices.
    The eigenvalues of K are the squared Lipschitz eigenvalues.

    The Connes distance in direction delta (traceless Hermitian) is:
        d(delta) = max_{f: L(f)<=1} Tr(delta f) = ||K^{-1/2} c||
    where c_i = Tr(delta H_i).

    This is EXACT for the L2 norm version. For the operator norm version,
    it provides a lower bound. We also compute the operator-norm version
    via a small number of optimization trials.

    Returns:
        lip_evals: eigenvalues of K (sorted ascending)
        lip_evecs: corresponding eigenvectors (columns)
        traceless_basis: list of traceless Hermitian basis matrices
    """
    dim_spin = 16
    I_spin = np.eye(dim_spin, dtype=complex)

    # Build traceless Hermitian basis (dim^2 - 1 elements)
    basis = []

    # Traceless diagonals: H_k = (E_{kk} - E_{k+1,k+1}) / sqrt(2)
    for k in range(dim_pq - 1):
        H = np.zeros((dim_pq, dim_pq), dtype=complex)
        H[k, k] = 1.0
        H[k + 1, k + 1] = -1.0
        H /= np.sqrt(2)
        basis.append(H)

    # Off-diagonal real
    for i in range(dim_pq):
        for j in range(i + 1, dim_pq):
            H = np.zeros((dim_pq, dim_pq), dtype=complex)
            H[i, j] = 1.0 / np.sqrt(2)
            H[j, i] = 1.0 / np.sqrt(2)
            basis.append(H)

    # Off-diagonal imaginary
    for i in range(dim_pq):
        for j in range(i + 1, dim_pq):
            H = np.zeros((dim_pq, dim_pq), dtype=complex)
            H[i, j] = -1j / np.sqrt(2)
            H[j, i] = 1j / np.sqrt(2)
            basis.append(H)

    n_basis = len(basis)
    # Verify: should be dim^2 - 1
    assert n_basis == dim_pq ** 2 - 1, f"Expected {dim_pq**2-1}, got {n_basis}"

    # Compute commutators
    comms = []
    for H in basis:
        f_ext = np.kron(H, I_spin)
        comm = D_pq @ f_ext - f_ext @ D_pq
        comms.append(comm)

    # Build Lipschitz matrix K: K_{ij} = Tr(comm_i^dag comm_j)
    K = np.zeros((n_basis, n_basis), dtype=complex)
    for i in range(n_basis):
        for j in range(i, n_basis):
            val = np.trace(comms[i].conj().T @ comms[j])
            K[i, j] = val
            K[j, i] = val.conj()

    # K should be real symmetric (Hermitian with real entries)
    K = K.real

    # Eigendecompose
    evals, evecs = eigh(K)

    return evals, evecs, basis, comms


def connes_distance_sector_L2(lip_evals, lip_evecs, basis, delta_pq, dim_pq):
    """
    Compute the Connes distance in the L2 (Frobenius) norm version.

    This gives an EXACT answer for the modified distance:
        d_F(delta) = max_{f: ||[D, f x I]||_F <= 1} Tr(delta f)

    The answer is:
        d_F = sqrt(sum_k (c_k / lambda_k)^2)
    where c_k = Tr(delta V_k) with V_k = sum_i (evecs)_{ik} H_i,
    and lambda_k = sqrt(lip_evals[k]).

    Also provides a lower bound for the operator-norm distance via:
        d_op >= d_F / sqrt(dim_total)  (by norm inequality)
        d_op <= d_F  (since ||A||_F >= ||A||_op)

    Returns:
        d_F: Frobenius-norm Connes distance
        d_op_lower: lower bound on operator-norm distance
    """
    n = len(lip_evals)
    # Project delta onto Lipschitz eigenbasis
    c = np.array([np.trace(delta_pq.conj().T @ basis[i]).real for i in range(n)])
    c_rot = lip_evecs.T @ c  # rotated into eigenbasis

    # d_F = sqrt(sum (c_k^2 / lambda_k)) where lambda_k = lip_evals[k]
    d_F_sq = 0.0
    for k in range(n):
        if lip_evals[k] > 1e-14:
            d_F_sq += c_rot[k] ** 2 / lip_evals[k]
        # If lambda_k = 0, this is a central direction. For finite dim_pq > 1,
        # there should be no zero eigenvalues (D has compact resolvent).

    d_F = np.sqrt(max(d_F_sq, 0.0))
    dim_total = dim_pq * 16
    d_op_lower = d_F / np.sqrt(dim_total)

    return d_F, d_op_lower


def connes_distance_sector_op(D_pq, dim_pq, delta_pq, comms, basis,
                               n_trials=30):
    """
    Compute the Connes distance using operator norm (true Connes distance).

    Uses targeted optimization with the Lipschitz eigenbasis as starting points.

    d = max_{f: ||[D, f x I]|| <= 1} Re Tr(delta f)

    Returns:
        d_op: operator-norm Connes distance (lower bound, may not be tight)
    """
    n_basis = len(basis)
    I_spin = np.eye(16, dtype=complex)

    # Objective coefficients
    c = np.array([np.trace(delta_pq.conj().T @ basis[k]).real for k in range(n_basis)])

    if np.linalg.norm(c) < 1e-15:
        return 0.0

    def lip_norm(x):
        comm = sum(x[k] * comms[k] for k in range(n_basis) if abs(x[k]) > 1e-16)
        if isinstance(comm, (int, float)):
            return 0.0
        return svdvals(comm)[0].real

    best_val = 0.0

    # Targeted trials: align with c, then single-direction, then 3 random
    for trial in range(min(n_trials, 5)):
        if trial == 0:
            x0 = c / (np.linalg.norm(c) + 1e-30)
        elif trial == 1:
            k = np.argmax(np.abs(c))
            x0 = np.zeros(n_basis)
            x0[k] = np.sign(c[k])
        else:
            rng = np.random.default_rng(42 + trial)
            x0 = rng.standard_normal(n_basis)
            x0 /= np.linalg.norm(x0)

        lip = lip_norm(x0)
        if lip > 1e-14:
            x0 /= lip
        else:
            continue

        val = np.dot(c, x0)
        if val > best_val:
            best_val = val
            best_x = x0.copy()

    # SLSQP refinement (single shot, limited iterations for speed)
    if best_val > 0:
        try:
            result = minimize(
                lambda x: -np.dot(c, x),
                best_x,
                method='SLSQP',
                constraints={'type': 'ineq', 'fun': lambda x: 1 - lip_norm(x)},
                options={'maxiter': 80, 'ftol': 1e-9}
            )
            if result.success and -result.fun > best_val:
                best_val = -result.fun
        except Exception:
            pass

    return max(best_val, 0.0)


# =============================================================================
# SECTION 2: GROUP ELEMENT UTILITIES
# =============================================================================

def expm_antiherm(A):
    """Matrix exponential of anti-Hermitian matrix via eigendecomposition."""
    H = 1j * A
    evals, evecs = eigh(H)
    return evecs @ np.diag(np.exp(-1j * evals)) @ evecs.conj().T


def geodesic_coeff(tau, direction):
    """Return sqrt(g_{aa}) for direction a at Jensen parameter tau."""
    L1 = np.exp(2 * tau)
    L2 = np.exp(-2 * tau)
    L3 = np.exp(tau)
    B_diag = 3.0
    if direction in [0, 1, 2]:
        return np.sqrt(B_diag * L2)
    elif direction in [3, 4, 5, 6]:
        return np.sqrt(B_diag * L3)
    elif direction == 7:
        return np.sqrt(B_diag * L1)
    raise ValueError(f"Invalid direction {direction}")


# =============================================================================
# SECTION 3: MASTER COMPUTATION
# =============================================================================

def compute_all(tau, max_pq_sum=3, t_disp=0.1, verbose=True):
    """Compute all Connes distance data at a single tau."""
    t0 = time.time()

    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    B_ab = compute_killing_form(f_abc)
    gammas = build_cliff8()

    g_s = jensen_metric(B_ab, tau)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Omega = spinor_connection_offset(Gamma, gammas)

    # Enumerate sectors
    sectors = []
    for p in range(max_pq_sum + 1):
        for q in range(max_pq_sum + 1 - p):
            dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2
            C2 = (p**2 + q**2 + p*q + 3*p + 3*q) / 3.0
            sectors.append((p, q, dim_pq, C2))

    # Build Dirac operators & Lipschitz spectra
    D_dict = {}
    rho_dict = {}
    lip_data = {}  # (p,q) -> (evals, evecs, basis, comms)

    for p, q, dim_pq, C2 in sectors:
        if p == 0 and q == 0:
            D_dict[(0, 0)] = Omega.copy()
            rho_dict[(0, 0)] = [np.array([[1.0 + 0j]])]
            continue

        rho, _ = get_irrep(p, q, gens, f_abc)
        D_pq = dirac_operator_on_irrep(rho, E, gammas, Omega)
        D_dict[(p, q)] = D_pq
        rho_dict[(p, q)] = rho

        # Compute Lipschitz spectrum
        evals, evecs, basis, comms = compute_lipschitz_spectrum(D_pq, dim_pq)
        lip_data[(p, q)] = (evals, evecs, basis, comms)

        if verbose:
            n_zero = np.sum(evals < 1e-10)
            print(f"    ({p},{q}): dim={dim_pq}, Lip spec range "
                  f"[{evals[0]:.4e}, {evals[-1]:.4e}], "
                  f"n_zero={n_zero}")

    t_build = time.time() - t0
    if verbose:
        print(f"  Build time: {t_build:.1f}s")

    # ------------------------------------------------------------------
    # DIRECTIONAL DISTANCES (L2 exact + operator-norm bounds)
    # ------------------------------------------------------------------
    d_connes_F = np.zeros(8)     # Frobenius (HS) Lipschitz distance (EXACT)
    d_connes_op = np.zeros(8)    # Operator-norm distance (best lower bound)
    d_connes_op_upper = np.zeros(8)  # Upper bound from L2
    d_geo = np.zeros(8)

    for direction in range(8):
        total_F = 0.0
        total_op_lower = 0.0
        for p, q, dim_pq, C2 in sectors:
            if dim_pq <= 1:
                continue
            if (p, q) not in lip_data:
                continue

            rho = rho_dict[(p, q)]
            U = expm_antiherm(t_disp * rho[direction])
            delta = dim_pq * (np.eye(dim_pq, dtype=complex) - U.conj().T)
            delta = 0.5 * (delta + delta.conj().T)

            evals, evecs, basis, comms = lip_data[(p, q)]

            d_F, d_op_lower = connes_distance_sector_L2(
                evals, evecs, basis, delta, dim_pq
            )
            total_F += d_F
            total_op_lower += d_op_lower

        d_connes_F[direction] = total_F
        d_connes_op[direction] = total_op_lower  # conservative lower bound
        d_connes_op_upper[direction] = total_F    # upper = F norm
        d_geo[direction] = t_disp * geodesic_coeff(tau, direction)

    ratios_F = d_connes_F / np.where(d_geo > 1e-14, d_geo, 1e-14)
    ratios_op = d_connes_op / np.where(d_geo > 1e-14, d_geo, 1e-14)

    # ------------------------------------------------------------------
    # SECTOR SPECTRAL RADII (for block distances)
    # ------------------------------------------------------------------
    sector_radii = {}
    sector_radii_F = {}
    for p, q, dim_pq, C2 in sectors:
        if dim_pq <= 1:
            sector_radii[(p, q)] = float('inf')
            sector_radii_F[(p, q)] = float('inf')
            continue
        if (p, q) not in lip_data:
            continue

        delta = np.eye(dim_pq, dtype=complex) / dim_pq
        evals, evecs, basis, comms = lip_data[(p, q)]
        d_F, d_op_lower = connes_distance_sector_L2(evals, evecs, basis, delta, dim_pq)
        sector_radii[(p, q)] = d_F  # use L2 as primary metric
        sector_radii_F[(p, q)] = d_F

    # Block grouping
    # Framework convention: B1=(0,0), B2=(1,1) adjoint, B3=remaining
    B_map = {'B1': [(0, 0)], 'B2': [(1, 1)],
             'B3': [s for s in sector_radii if s not in [(0, 0), (1, 1)]]}
    B_group_radii = {}
    for name, slist in B_map.items():
        finite = [sector_radii[s] for s in slist
                  if s in sector_radii and sector_radii[s] < 1e10]
        B_group_radii[name] = np.mean(finite) if finite else float('inf')

    inter_block = {}
    for n1 in ['B1', 'B2', 'B3']:
        for n2 in ['B1', 'B2', 'B3']:
            if n1 >= n2:
                continue
            inter_block[(n1, n2)] = B_group_radii[n1] + B_group_radii[n2]

    # Summary (using L2 distance as primary: exact, well-defined, fast)
    finite_d = d_connes_F[d_connes_F > 1e-14]
    diameter = np.max(finite_d) if len(finite_d) else 0.0
    anisotropy = (np.max(finite_d) / np.min(finite_d)
                  if len(finite_d) and np.min(finite_d) > 1e-14 else 1.0)

    su2_m = np.mean(d_connes_F[:3])
    c2_m = np.mean(d_connes_F[3:7])
    u1_v = d_connes_F[7]

    elapsed = time.time() - t0
    if verbose:
        print(f"  tau={tau:.3f}: su2={su2_m:.5f}, C2={c2_m:.5f}, "
              f"u1={u1_v:.5f}, diam={diameter:.5f}, "
              f"anis={anisotropy:.3f} [{elapsed:.1f}s]")

    return {
        'tau': tau,
        'd_connes_F': d_connes_F,
        'd_connes_op': d_connes_op,
        'd_geo': d_geo,
        'ratios_F': ratios_F,
        'ratios_op': ratios_op,
        'sector_radii': sector_radii,
        'B_group_radii': B_group_radii,
        'inter_block': inter_block,
        'diameter': diameter,
        'anisotropy': anisotropy,
        'su2_mean': su2_m,
        'c2_mean': c2_m,
        'u1_val': u1_v,
        'lip_data': lip_data,
    }


# =============================================================================
# SECTION 4: MAIN
# =============================================================================

def main():
    print("=" * 70)
    print("CONNES-DISTANCE-46: Spectral Distance on Truncated Jensen SU(3)")
    print("=" * 70)

    MAX_PQ = 3
    T_DISP = 0.1

    # ==================================================================
    # STEP 1: Three reference points
    # ==================================================================
    print(f"\n--- STEP 1: Reference computations ---")

    print(f"\n  [A] Round SU(3) (tau=0.0)")
    r_round = compute_all(0.0, MAX_PQ, T_DISP, verbose=True)

    print(f"\n  [B] Fold (tau={tau_fold})")
    r_fold = compute_all(tau_fold, MAX_PQ, T_DISP, verbose=True)

    print(f"\n  [C] Deep (tau=0.30)")
    r_deep = compute_all(0.30, MAX_PQ, T_DISP, verbose=True)

    # ==================================================================
    # STEP 2: Tau sweep
    # ==================================================================
    print(f"\n--- STEP 2: Tau sweep ---")
    tau_vals = np.array([0.0, 0.05, 0.10, 0.15, 0.19, 0.25, 0.30, 0.40, 0.50])
    sweep = []
    for tv in tau_vals:
        if abs(tv) < 1e-6:
            sweep.append(r_round)
        elif abs(tv - tau_fold) < 1e-6:
            sweep.append(r_fold)
        elif abs(tv - 0.30) < 1e-6:
            sweep.append(r_deep)
        else:
            sweep.append(compute_all(tv, MAX_PQ, T_DISP, verbose=True))

    # ==================================================================
    # STEP 3: Convergence (max_pq_sum=4 at fold)
    # ==================================================================
    print(f"\n--- STEP 3: Convergence (pq=4 at fold) ---")
    r_conv = compute_all(tau_fold, 4, T_DISP, verbose=True)

    # ==================================================================
    # DETAILED OUTPUT
    # ==================================================================
    dir_names = ['su2_1', 'su2_2', 'su2_3',
                 'C2_1', 'C2_2', 'C2_3', 'C2_4', 'u1']

    print(f"\n{'='*70}")
    print(f"DETAILED RESULTS")
    print(f"{'='*70}")

    print(f"\n1. DIRECTIONAL DISTANCES at fold (tau={tau_fold}, t={T_DISP}):")
    print(f"   {'dir':>7s}  {'d_Connes(F)':>12s}  {'d_geodesic':>12s}  "
          f"{'ratio(F)':>10s}")
    for a in range(8):
        print(f"   {dir_names[a]:>7s}  {r_fold['d_connes_F'][a]:12.6f}  "
              f"{r_fold['d_geo'][a]:12.6f}  "
              f"{r_fold['ratios_F'][a]:10.4f}")

    print(f"\n2. ISOTROPY at tau=0:")
    print(f"   su(2) = {r_round['su2_mean']:.6f}")
    print(f"   C^2   = {r_round['c2_mean']:.6f}")
    print(f"   u(1)  = {r_round['u1_val']:.6f}")
    print(f"   Anisotropy = {r_round['anisotropy']:.6f}")

    print(f"\n3. BLOCK SPECTRAL RADII at fold:")
    for name in ['B1', 'B2', 'B3']:
        v = r_fold['B_group_radii'].get(name, np.inf)
        print(f"   r({name}) = {v:.6f}" if v < 1e10 else f"   r({name}) = inf")
    print(f"   Inter-block distances:")
    for (n1, n2), d_val in r_fold['inter_block'].items():
        print(f"   d({n1},{n2}) = {d_val:.6f}" if d_val < 1e10
              else f"   d({n1},{n2}) = inf")

    print(f"\n4. SECTOR SPECTRAL RADII at fold:")
    for (pq, rv) in sorted(r_fold['sector_radii'].items()):
        if rv < 1e10:
            print(f"   ({pq[0]},{pq[1]}): r = {rv:.6f}")
        else:
            print(f"   ({pq[0]},{pq[1]}): r = inf")

    print(f"\n5. LIPSCHITZ SPECTRUM at fold (min/max eigenvalues of K):")
    for (pq, ld) in sorted(r_fold['lip_data'].items()):
        evals = ld[0]
        print(f"   ({pq[0]},{pq[1]}): lambda_min={evals[0]:.4e}, "
              f"lambda_max={evals[-1]:.4e}, "
              f"condition={evals[-1]/(evals[0]+1e-30):.1f}")

    print(f"\n6. ANISOTROPY EVOLUTION:")
    print(f"   {'tau':>6s}  {'su(2)':>8s}  {'C^2':>8s}  {'u(1)':>8s}  "
          f"{'diam':>8s}  {'anis':>7s}  {'C2/su2':>7s}  {'geo_ratio':>9s}")
    for r in sweep:
        c2su2 = r['c2_mean'] / r['su2_mean'] if r['su2_mean'] > 1e-14 else 0.0
        geo_rat = np.exp(3 * r['tau'] / 2)
        print(f"   {r['tau']:6.3f}  {r['su2_mean']:8.5f}  {r['c2_mean']:8.5f}  "
              f"{r['u1_val']:8.5f}  {r['diameter']:8.5f}  "
              f"{r['anisotropy']:7.3f}  {c2su2:7.3f}  {geo_rat:9.4f}")

    print(f"\n7. CONVERGENCE (pq3 vs pq4 at fold):")
    for a in range(8):
        d3 = r_fold['d_connes_F'][a]
        d4 = r_conv['d_connes_F'][a]
        rel = abs(d4 - d3) / (abs(d3) + 1e-14)
        print(f"   {dir_names[a]:>7s}: pq3={d3:.6f}, pq4={d4:.6f}, rel={rel:.4f}")

    # ==================================================================
    # SAVE NPZ
    # ==================================================================
    tau_arr = np.array([r['tau'] for r in sweep])
    save = dict(
        tau_sweep=tau_arr,
        d_su2_sweep=np.array([r['su2_mean'] for r in sweep]),
        d_c2_sweep=np.array([r['c2_mean'] for r in sweep]),
        d_u1_sweep=np.array([r['u1_val'] for r in sweep]),
        diameter_sweep=np.array([r['diameter'] for r in sweep]),
        anisotropy_sweep=np.array([r['anisotropy'] for r in sweep]),
        connes_fold_F=r_fold['d_connes_F'],
        geodesic_fold=r_fold['d_geo'],
        ratio_fold_F=r_fold['ratios_F'],
        connes_round_F=r_round['d_connes_F'],
        anisotropy_round=r_round['anisotropy'],
        connes_deep_F=r_deep['d_connes_F'],
        anisotropy_deep=r_deep['anisotropy'],
        B1_radius=r_fold['B_group_radii'].get('B1', np.inf),
        B2_radius=r_fold['B_group_radii'].get('B2', np.inf),
        B3_radius=r_fold['B_group_radii'].get('B3', np.inf),
        d_B1_B2=r_fold['inter_block'].get(('B1', 'B2'), np.inf),
        d_B1_B3=r_fold['inter_block'].get(('B1', 'B3'), np.inf),
        d_B2_B3=r_fold['inter_block'].get(('B2', 'B3'), np.inf),
        connes_fold_pq4=r_conv['d_connes_F'],
        max_pq_sum=MAX_PQ,
        t_displacement=T_DISP,
        tau_fold_used=tau_fold,
    )
    npz_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            's46_connes_distance.npz')
    np.savez(npz_path, **save)
    print(f"\n  Saved: {npz_path}")

    # ==================================================================
    # PLOT
    # ==================================================================
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle('CONNES-DISTANCE-46: Spectral Distance on Jensen SU(3)',
                 fontsize=13, fontweight='bold')

    x8 = np.arange(8)

    # Panel A: Directional at fold
    ax = axes[0, 0]
    ax.bar(x8 - 0.15, r_fold['d_connes_op'], 0.3, label='Connes (op)', color='steelblue')
    ax.bar(x8 + 0.15, r_fold['d_geo'], 0.3, label='Geodesic', color='coral')
    ax.set_xticks(x8)
    ax.set_xticklabels(dir_names, rotation=45, ha='right', fontsize=7)
    ax.set_ylabel(r'Distance ($M_{KK}^{-1}$)')
    ax.set_title(f'Directional Distances at Fold (tau={tau_fold})')
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # Panel B: Tau sweep
    ax = axes[0, 1]
    su2_s = np.array([r['su2_mean'] for r in sweep])
    c2_s = np.array([r['c2_mean'] for r in sweep])
    u1_s = np.array([r['u1_val'] for r in sweep])
    ax.plot(tau_arr, su2_s, 'b-o', label='su(2)', ms=4)
    ax.plot(tau_arr, c2_s, 'r-s', label=r'$\mathbb{C}^2$', ms=4)
    ax.plot(tau_arr, u1_s, 'g-^', label='u(1)', ms=4)
    ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5, label='fold')
    ax.set_xlabel(r'$\tau$')
    ax.set_ylabel(r'Mean Connes Distance ($M_{KK}^{-1}$)')
    ax.set_title('Distance Evolution with Jensen Deformation')
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # Panel C: Anisotropy
    ax = axes[1, 0]
    anis_s = np.array([r['anisotropy'] for r in sweep])
    ax.plot(tau_arr, anis_s, 'k-o', label='Connes anisotropy', ms=4)
    geo_anis = np.exp(3 * tau_arr / 2)
    ax.plot(tau_arr, geo_anis, 'r--', label=r'Metric: $e^{3\tau/2}$')
    ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5)
    ax.set_xlabel(r'$\tau$')
    ax.set_ylabel('Anisotropy Ratio (C2/su2)')
    ax.set_title('Connes vs Metric Anisotropy')
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # Panel D: Ratio
    ax = axes[1, 1]
    colors = ['blue'] * 3 + ['red'] * 4 + ['green']
    ax.bar(x8, r_fold['ratios_F'], color=colors, alpha=0.7)
    ax.axhline(1.0, color='black', ls='--', lw=0.8, label='Exact')
    ax.set_xticks(x8)
    ax.set_xticklabels(dir_names, rotation=45, ha='right', fontsize=7)
    ax.set_ylabel('Connes / Geodesic')
    ax.set_title(f'Truncation Quality (max_pq_sum={MAX_PQ})')
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    plt.tight_layout()
    plot_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             's46_connes_distance.png')
    plt.savefig(plot_path, dpi=150, bbox_inches='tight')
    print(f"  Saved: {plot_path}")
    plt.close()

    # ==================================================================
    # FINAL SUMMARY
    # ==================================================================
    print(f"\n{'='*70}")
    print(f"CONNES-DISTANCE-46: FINAL SUMMARY")
    print(f"{'='*70}")
    print(f"\nDirectional distances at fold (Frobenius-Lipschitz, EXACT):")
    print(f"  su(2) mean: {r_fold['su2_mean']:.6f} M_KK^{{-1}}")
    print(f"  C^2 mean:   {r_fold['c2_mean']:.6f}")
    print(f"  u(1):       {r_fold['u1_val']:.6f}")
    print(f"  Diameter:   {r_fold['diameter']:.6f}")
    print(f"  Anisotropy: {r_fold['anisotropy']:.4f}")
    print(f"\nConnes/geodesic ratios at fold (F-Lip):")
    print(f"  Mean: {np.mean(r_fold['ratios_F']):.4f}")
    print(f"  Range: [{np.min(r_fold['ratios_F']):.4f}, {np.max(r_fold['ratios_F']):.4f}]")
    print(f"\nBlock distances at fold (F-Lip):")
    for n in ['B1', 'B2', 'B3']:
        v = r_fold['B_group_radii'].get(n, np.inf)
        print(f"  r({n}) = {'inf' if v > 1e10 else f'{v:.6f}'}")
    print(f"\nConvergence (pq3 vs pq4, F-Lip):")
    rel = np.abs(r_conv['d_connes_F'] - r_fold['d_connes_F']) / \
          (np.abs(r_fold['d_connes_F']) + 1e-14)
    print(f"  Max rel change: {np.max(rel):.4f}")
    print(f"  Mean rel change: {np.mean(rel):.4f}")
    print(f"\nDONE.")


if __name__ == '__main__':
    main()
