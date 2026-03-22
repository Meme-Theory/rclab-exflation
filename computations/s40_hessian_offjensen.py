#!/usr/bin/env python3
"""
HESS-40: Off-Jensen Hessian at the Fold — FRAMEWORK DECISIVE
==============================================================

Tests whether the Jensen trajectory tau=0.190 is a LOCAL MINIMUM of S_full
in the 28-dimensional space of left-invariant metrics on SU(3), or merely
a saddle point with tachyonic transverse directions.

Strategy:
  Level 1: 3 diagonal deformations within complement sector (6 evals)
  Level 2: All 7 independent volume-preserving diagonal deformations (14+ evals)
  Level 3: Off-diagonal metric components (not implemented unless needed)

Pre-registered gate HESS-40:
  PASS (TRAPPING):         Any H_ii < -h^2 (negative eigenvalue, saddle point)
  FAIL (COMPOUND NUCLEUS): All H_ii > +h^2 (local minimum, no escape)
  NULL:                    Diagonal-only and all positive -> FAIL (DIAGONAL ONLY)

Spectral action: S_full(g) = sum_{(p,q)} dim(p,q)^2 * sum_k |lambda_k^{(p,q)}(g)|
where lambda_k are eigenvalues of iD_{(p,q)} (Hermitian).

Author: Gen-Physicist (Session 40)
Date: 2026-03-11
"""

import numpy as np
from numpy.linalg import eigh, eigvalsh, inv, cholesky
import sys
import os
import time

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
from tier1_dirac_spectrum import (
    su3_generators,
    compute_structure_constants,
    compute_killing_form,
    orthonormal_frame,
    frame_structure_constants,
    connection_coefficients,
    validate_connection,
    build_cliff8,
    validate_clifford,
    spinor_connection_offset,
    get_irrep,
    dirac_operator_on_irrep,
    _irrep_cache,
    jensen_metric,
    U1_IDX, SU2_IDX, C2_IDX,
)
from canonical_constants import tau_fold as TAU_FOLD


# =============================================================================
# CONFIGURATION
# =============================================================================

# Sectors through KK level 3 (same as s36)
ALL_SECTORS = [
    (0, 0),
    (1, 0), (0, 1),
    (1, 1), (2, 0), (0, 2),
    (3, 0), (0, 3), (2, 1), (1, 2),
]

# Finite difference step sizes for Richardson extrapolation
EPS_LARGE = 0.01
EPS_SMALL = 0.005  # eps/2

def dim_pq(p, q):
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def mult_pq(p, q):
    """Peter-Weyl multiplicity: dim(p,q)^2."""
    return dim_pq(p, q) ** 2


# =============================================================================
# GENERAL DIAGONAL METRIC CONSTRUCTION
# =============================================================================

def general_diagonal_metric(B_ab, scale_factors):
    """
    Construct a general diagonal left-invariant metric on SU(3).

    g_ab = |B_ab| * scale_factors[a] * delta_{ab}

    For the Jensen metric at parameter s:
      scale_factors = [e^{-2s}, e^{-2s}, e^{-2s},   # su(2): indices 0,1,2
                       e^s, e^s, e^s, e^s,            # C^2: indices 3,4,5,6
                       e^{2s}]                         # u(1): index 7

    Args:
        B_ab: (8,8) Killing form (diagonal, = -3*I for our normalization)
        scale_factors: array of 8 positive floats

    Returns:
        g: (8,8) positive definite diagonal metric
    """
    g = np.zeros((8, 8), dtype=np.float64)
    for a in range(8):
        g[a, a] = abs(B_ab[a, a]) * scale_factors[a]
    return g


def jensen_scale_factors(s):
    """
    Return the 8 scale factors for the Jensen metric at parameter s.

    Ordering: indices 0,1,2 = su(2), indices 3,4,5,6 = C^2, index 7 = u(1).
    """
    L2 = np.exp(-2.0 * s)  # su(2)
    L3 = np.exp(s)          # C^2
    L1 = np.exp(2.0 * s)   # u(1)
    return np.array([L2, L2, L2, L3, L3, L3, L3, L1])


def volume_factor(scale_factors):
    """
    Volume factor V = prod_a L_a^{1/2} for diagonal metric.

    For left-invariant metric g = |B| * diag(L_a), the volume element is
    proportional to sqrt(det(g)) = sqrt(prod |B_aa| * L_a) = (sqrt(3))^8 * prod L_a^{1/2}.
    The |B| part is universal. The L-dependent part is prod L_a^{1/2}.
    """
    return np.prod(np.sqrt(scale_factors))


# =============================================================================
# S_full COMPUTATION AT GENERAL DIAGONAL METRIC
# =============================================================================

def compute_S_full(scale_factors, B_ab, gens, f_abc, gammas, sectors=None,
                   verbose=False):
    """
    Compute S_full at a general diagonal metric specified by scale_factors.

    S_full = sum_{(p,q)} dim(p,q)^2 * sum_k |lambda_k^{(p,q)}|

    Args:
        scale_factors: array of 8 positive scale factors
        B_ab: (8,8) Killing form
        gens: su(3) generators
        f_abc: structure constants
        gammas: Clifford generators
        sectors: list of (p,q) tuples to include (default: ALL_SECTORS)
        verbose: print diagnostics

    Returns:
        S_full: float, the total spectral action
        sector_actions: dict (p,q) -> S_{(p,q)}
    """
    if sectors is None:
        sectors = ALL_SECTORS

    # Build metric
    g = general_diagonal_metric(B_ab, scale_factors)

    # Orthonormal frame (diagonal since g is diagonal)
    E = orthonormal_frame(g)

    # Frame structure constants
    ft = frame_structure_constants(f_abc, E)

    # Connection coefficients
    Gamma = connection_coefficients(ft)

    if verbose:
        mc_err = validate_connection(Gamma)
        print(f"  Connection metric-compat err: {mc_err:.2e}")

    # Spinor connection offset
    Omega = spinor_connection_offset(Gamma, gammas)

    # Clear irrep cache to avoid stale data
    _irrep_cache.clear()

    S_full = 0.0
    sector_actions = {}

    for p, q in sectors:
        d = dim_pq(p, q)
        m = mult_pq(p, q)

        # Get representation
        rho, dim_r = get_irrep(p, q, gens, f_abc)
        assert dim_r == d, f"dim mismatch for ({p},{q}): {dim_r} vs {d}"

        # Build Dirac operator
        D_pi = dirac_operator_on_irrep(rho, E, gammas, Omega)

        # Verify anti-Hermiticity
        ah_err = np.max(np.abs(D_pi + D_pi.conj().T))
        if ah_err > 1e-10:
            print(f"  WARNING: D anti-Herm err = {ah_err:.2e} for ({p},{q})")

        # Eigenvalues of iD (Hermitian)
        iD = 1j * D_pi
        evals = eigvalsh(iD)

        # Spectral action for this sector
        S_sector = np.sum(np.abs(evals))
        sector_actions[(p, q)] = S_sector

        S_full += m * S_sector

        if verbose:
            print(f"  ({p},{q}): dim={d}, mult={m}, S={S_sector:.6f}, "
                  f"contrib={m*S_sector:.2f}, ah_err={ah_err:.2e}")

    return S_full, sector_actions


# =============================================================================
# VOLUME-PRESERVING DEFORMATION DIRECTIONS
# =============================================================================

def make_deformation_direction(positive_indices, negative_indices,
                               base_scale_factors):
    """
    Construct a volume-preserving deformation direction in scale-factor space.

    The deformation scales factors at positive_indices by (1+eps) and
    at negative_indices by (1-eps*correction) to maintain volume.

    For a diagonal metric with scale factors L_a, volume ~ prod L_a^{1/2}.
    Volume preservation to first order requires sum_a (delta L_a / L_a) = 0.

    We define the deformation as: L_a -> L_a * exp(eps * sigma_a) where
    sigma_a is the direction vector satisfying sum_a sigma_a = 0.

    Args:
        positive_indices: list of indices to scale up
        negative_indices: list of indices to scale down
        base_scale_factors: reference scale factors (for normalization)

    Returns:
        sigma: (8,) direction vector with sum(sigma) = 0
        label: string description
    """
    sigma = np.zeros(8)
    n_pos = len(positive_indices)
    n_neg = len(negative_indices)

    # Equal weight: +1 on positive, -n_pos/n_neg on negative
    for i in positive_indices:
        sigma[i] = 1.0
    for i in negative_indices:
        sigma[i] = -n_pos / n_neg

    # Normalize to unit length
    sigma /= np.linalg.norm(sigma)

    return sigma


def apply_deformation(base_sf, sigma, eps):
    """
    Apply deformation: L_a -> L_a * exp(eps * sigma_a).

    This is exactly volume-preserving when sum(sigma) = 0:
      prod L_a^{1/2} exp(eps*sigma_a/2) = prod L_a^{1/2} * exp(eps/2 * sum sigma_a)
                                         = prod L_a^{1/2}  (since sum sigma = 0)

    Args:
        base_sf: (8,) base scale factors
        sigma: (8,) direction vector with sum(sigma) = 0
        eps: deformation magnitude

    Returns:
        deformed_sf: (8,) deformed scale factors
    """
    return base_sf * np.exp(eps * sigma)


# =============================================================================
# DEFINE TRANSVERSE DIRECTIONS
# =============================================================================

def define_level1_directions():
    """
    Level 1: 3 deformations within the complement sector.

    The complement m = C^2 has indices {3,4,5,6}. The Jensen metric treats
    all 4 equally. We break this symmetry in 3 independent ways:

    sigma_1: {3,4} up, {5,6} down  (break SU(2)_R within m)
    sigma_2: {3} up, {4,5,6} down  (single mode split)
    sigma_3: {3,4,5} up, {6} down  (complementary single mode split)

    All are volume-preserving (sum sigma = 0) within the complement.
    We also need global volume preservation, so we set sigma = 0 on u(2) indices.
    Since sum over complement = 0, global sum = 0 automatically.
    """
    directions = []

    # sigma_1: {3,4} vs {5,6}
    s1 = np.zeros(8)
    s1[3] = 1.0; s1[4] = 1.0; s1[5] = -1.0; s1[6] = -1.0
    s1 /= np.linalg.norm(s1)
    directions.append((s1, "sigma_1: {3,4}+/{5,6}-"))

    # sigma_2: {3} vs {4,5,6}
    s2 = np.zeros(8)
    s2[3] = 3.0; s2[4] = -1.0; s2[5] = -1.0; s2[6] = -1.0
    s2 /= np.linalg.norm(s2)
    directions.append((s2, "sigma_2: {3}+/{4,5,6}-"))

    # sigma_3: {3,4,5} vs {6}
    s3 = np.zeros(8)
    s3[3] = 1.0; s3[4] = 1.0; s3[5] = 1.0; s3[6] = -3.0
    s3 /= np.linalg.norm(s3)
    directions.append((s3, "sigma_3: {3,4,5}+/{6}-"))

    return directions


def define_level2_directions():
    """
    Level 2: All 7 independent volume-preserving diagonal deformations.

    The 8 diagonal scale factors have 1 constraint (volume preservation),
    leaving 7 DOF. The Jensen trajectory uses 1 DOF (direction
    sigma_J = (-2,-2,-2, 1,1,1,1, 2)/norm). The remaining 6 are transverse.

    We construct a complete orthonormal basis for the 7D volume-preserving
    subspace, then identify which is the Jensen direction and which are
    transverse.

    Basis construction:
    The constraint is sum_a sigma_a = 0 (7D hyperplane in R^8).
    We use Gram-Schmidt on natural basis vectors.
    """
    # Jensen direction (unnormalized): delta L_a / L_a proportional to
    # d/ds [ln L_a(s)]. For Jensen: L_{0,1,2} = e^{-2s}, L_{3,4,5,6} = e^s, L_7 = e^{2s}
    # d/ds ln L_a: {-2,-2,-2, 1,1,1,1, 2}
    sigma_J = np.array([-2.0, -2.0, -2.0, 1.0, 1.0, 1.0, 1.0, 2.0])
    assert abs(np.sum(sigma_J)) < 1e-14, "Jensen direction not volume-preserving!"
    sigma_J /= np.linalg.norm(sigma_J)

    # Build orthonormal basis for the 7D volume-preserving hyperplane
    # Constraint normal: n = (1,1,1,1,1,1,1,1)/sqrt(8)
    n = np.ones(8) / np.sqrt(8)

    # Start with standard basis vectors, project out n, then Gram-Schmidt
    # Or more directly: use the 7 vectors e_a - e_8 (a=0..6) and orthonormalize
    raw_basis = []
    for a in range(7):
        v = np.zeros(8)
        v[a] = 1.0
        v[7] = -1.0  # ensures sum = 0
        raw_basis.append(v)

    # Gram-Schmidt orthonormalization
    ortho_basis = []
    for v in raw_basis:
        w = v.copy()
        for u in ortho_basis:
            w -= np.dot(w, u) * u
        norm = np.linalg.norm(w)
        if norm > 1e-12:
            ortho_basis.append(w / norm)

    assert len(ortho_basis) == 7, f"Expected 7 basis vectors, got {len(ortho_basis)}"

    # Verify orthonormality
    for i in range(7):
        for j in range(7):
            dot = np.dot(ortho_basis[i], ortho_basis[j])
            expected = 1.0 if i == j else 0.0
            assert abs(dot - expected) < 1e-12, \
                f"Orthonormality violated: <b_{i}, b_{j}> = {dot}"

    # Verify all are volume-preserving
    for i, b in enumerate(ortho_basis):
        assert abs(np.sum(b)) < 1e-12, f"Basis vector {i} not volume-preserving"

    # Now project out the Jensen direction to get 6 transverse directions
    transverse = []
    for b in ortho_basis:
        w = b - np.dot(b, sigma_J) * sigma_J
        norm = np.linalg.norm(w)
        if norm > 0.1:  # not (anti-)parallel to Jensen
            transverse.append(w / norm)

    # Re-orthogonalize the transverse directions
    ortho_trans = []
    for v in transverse:
        w = v.copy()
        for u in ortho_trans:
            w -= np.dot(w, u) * u
        norm = np.linalg.norm(w)
        if norm > 1e-10:
            ortho_trans.append(w / norm)

    # Verify
    for i in range(len(ortho_trans)):
        assert abs(np.dot(ortho_trans[i], sigma_J)) < 1e-12, \
            f"Direction {i} not transverse to Jensen!"
        assert abs(np.sum(ortho_trans[i])) < 1e-12, \
            f"Direction {i} not volume-preserving!"

    assert len(ortho_trans) == 6, f"Expected 6 transverse directions, got {len(ortho_trans)}"

    # Also include Jensen direction itself as a consistency check
    directions = [(sigma_J, "sigma_J: Jensen tangent (-2,-2,-2,1,1,1,1,2)")]
    for i, d in enumerate(ortho_trans):
        # Identify the direction by its dominant components
        dominant = np.argsort(np.abs(d))[::-1][:3]
        desc = f"sigma_T{i+1}: dominant indices {list(dominant)}, " \
               f"components [{', '.join(f'{d[k]:+.3f}' for k in range(8))}]"
        directions.append((d, desc))

    return directions, sigma_J, ortho_trans


# =============================================================================
# HESSIAN COMPUTATION WITH RICHARDSON EXTRAPOLATION
# =============================================================================

def compute_hessian_diagonal(base_sf, sigma, B_ab, gens, f_abc, gammas,
                              eps_large=EPS_LARGE, eps_small=EPS_SMALL,
                              sectors=None, verbose=True):
    """
    Compute the diagonal Hessian element H_{sigma,sigma} = d^2 S_full / deps^2
    along direction sigma using centered finite differences with Richardson
    extrapolation.

    H(eps) = [S(+eps) + S(-eps) - 2*S(0)] / eps^2 + O(eps^2)
    H_exact ~ [4*H(eps/2) - H(eps)] / 3  (Richardson, cancels O(eps^2) error)

    Args:
        base_sf: (8,) base scale factors
        sigma: (8,) direction vector
        B_ab: Killing form
        gens, f_abc, gammas: Lie algebra infrastructure
        eps_large, eps_small: step sizes for Richardson
        sectors: which sectors to include
        verbose: print diagnostics

    Returns:
        H_rich: Richardson-extrapolated Hessian element
        H_large: raw Hessian at eps_large
        H_small: raw Hessian at eps_small
        S_0: S_full at base point
        details: dict with all computed S values
    """
    # S at base point
    S_0, _ = compute_S_full(base_sf, B_ab, gens, f_abc, gammas,
                             sectors=sectors, verbose=False)

    # Large step
    sf_plus = apply_deformation(base_sf, sigma, eps_large)
    sf_minus = apply_deformation(base_sf, sigma, -eps_large)

    S_plus_L, _ = compute_S_full(sf_plus, B_ab, gens, f_abc, gammas,
                                  sectors=sectors, verbose=False)
    S_minus_L, _ = compute_S_full(sf_minus, B_ab, gens, f_abc, gammas,
                                   sectors=sectors, verbose=False)

    H_large = (S_plus_L + S_minus_L - 2.0 * S_0) / (eps_large ** 2)

    # Small step
    sf_plus_s = apply_deformation(base_sf, sigma, eps_small)
    sf_minus_s = apply_deformation(base_sf, sigma, -eps_small)

    S_plus_S, _ = compute_S_full(sf_plus_s, B_ab, gens, f_abc, gammas,
                                  sectors=sectors, verbose=False)
    S_minus_S, _ = compute_S_full(sf_minus_s, B_ab, gens, f_abc, gammas,
                                   sectors=sectors, verbose=False)

    H_small = (S_plus_S + S_minus_S - 2.0 * S_0) / (eps_small ** 2)

    # Richardson extrapolation: H_exact ~ (4*H_small - H_large) / 3
    H_rich = (4.0 * H_small - H_large) / 3.0

    # Gradient (first derivative) for diagnostics
    grad_large = (S_plus_L - S_minus_L) / (2.0 * eps_large)
    grad_small = (S_plus_S - S_minus_S) / (2.0 * eps_small)

    details = {
        'S_0': S_0,
        'S_plus_L': S_plus_L, 'S_minus_L': S_minus_L,
        'S_plus_S': S_plus_S, 'S_minus_S': S_minus_S,
        'H_large': H_large, 'H_small': H_small, 'H_rich': H_rich,
        'grad_large': grad_large, 'grad_small': grad_small,
        'eps_large': eps_large, 'eps_small': eps_small,
        'volume_plus_L': volume_factor(sf_plus),
        'volume_minus_L': volume_factor(sf_minus),
        'volume_plus_S': volume_factor(sf_plus_s),
        'volume_minus_S': volume_factor(sf_minus_s),
    }

    if verbose:
        print(f"    S(0) = {S_0:.6f}")
        print(f"    S(+{eps_large}) = {S_plus_L:.6f}, "
              f"S(-{eps_large}) = {S_minus_L:.6f}")
        print(f"    H(eps={eps_large}) = {H_large:.4f}")
        print(f"    S(+{eps_small}) = {S_plus_S:.6f}, "
              f"S(-{eps_small}) = {S_minus_S:.6f}")
        print(f"    H(eps={eps_small}) = {H_small:.4f}")
        print(f"    H(Richardson) = {H_rich:.4f}")
        print(f"    grad(large) = {grad_large:.4f}, grad(small) = {grad_small:.4f}")
        print(f"    Volume checks: {details['volume_plus_L']:.10f}, "
              f"{details['volume_minus_L']:.10f}")

    return H_rich, H_large, H_small, S_0, details


# =============================================================================
# MAIN COMPUTATION
# =============================================================================

# =============================================================================
# LEVEL 3: OFF-DIAGONAL METRIC DEFORMATIONS
# =============================================================================

def compute_S_full_general_metric(g_metric, gens, f_abc, gammas, sectors=None,
                                   verbose=False):
    """
    Compute S_full at a general (possibly off-diagonal) PD metric.

    Uses the full Cholesky-based orthonormal frame from tier1_dirac_spectrum.

    Args:
        g_metric: (8,8) positive definite symmetric metric
        gens, f_abc, gammas: infrastructure
        sectors: list of (p,q)
        verbose: diagnostics

    Returns:
        S_full: float
    """
    if sectors is None:
        sectors = ALL_SECTORS

    E = orthonormal_frame(g_metric)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Omega = spinor_connection_offset(Gamma, gammas)

    _irrep_cache.clear()

    S_full = 0.0
    for p, q in sectors:
        d = dim_pq(p, q)
        m = mult_pq(p, q)
        rho, dim_r = get_irrep(p, q, gens, f_abc)
        D_pi = dirac_operator_on_irrep(rho, E, gammas, Omega)

        # Anti-Hermiticity check
        ah_err = np.max(np.abs(D_pi + D_pi.conj().T))
        if ah_err > 1e-10 and verbose:
            print(f"  WARNING: ah_err={ah_err:.2e} for ({p},{q})")

        iD = 1j * D_pi
        evals = eigvalsh(iD)
        S_full += m * np.sum(np.abs(evals))

    return S_full


def compute_hessian_offdiag(base_metric, delta_g, gens, f_abc, gammas,
                             eps=0.01, sectors=None, verbose=True):
    """
    Compute Hessian diagonal element for an off-diagonal metric deformation.

    g(eps) = base_metric + eps * delta_g

    The deformation must preserve positive-definiteness at +-eps.

    Args:
        base_metric: (8,8) PD symmetric base metric
        delta_g: (8,8) symmetric perturbation matrix
        gens, f_abc, gammas: infrastructure
        eps: step size
        sectors: which sectors

    Returns:
        H: d^2 S / deps^2 (centered finite difference)
        S_0, S_plus, S_minus: function values
    """
    if sectors is None:
        sectors = ALL_SECTORS

    g_plus = base_metric + eps * delta_g
    g_minus = base_metric - eps * delta_g

    # Verify PD
    evals_plus = eigvalsh(g_plus)
    evals_minus = eigvalsh(g_minus)
    if np.min(evals_plus) <= 0 or np.min(evals_minus) <= 0:
        print(f"  WARNING: metric not PD! min eig = {min(np.min(evals_plus), np.min(evals_minus)):.6e}")
        return np.nan, np.nan, np.nan, np.nan

    S_0 = compute_S_full_general_metric(base_metric, gens, f_abc, gammas,
                                         sectors=sectors)
    S_plus = compute_S_full_general_metric(g_plus, gens, f_abc, gammas,
                                            sectors=sectors)
    S_minus = compute_S_full_general_metric(g_minus, gens, f_abc, gammas,
                                             sectors=sectors)

    H = (S_plus + S_minus - 2.0 * S_0) / (eps ** 2)

    # Richardson: also compute at eps/2
    eps2 = eps / 2.0
    g_plus2 = base_metric + eps2 * delta_g
    g_minus2 = base_metric - eps2 * delta_g
    S_plus2 = compute_S_full_general_metric(g_plus2, gens, f_abc, gammas,
                                             sectors=sectors)
    S_minus2 = compute_S_full_general_metric(g_minus2, gens, f_abc, gammas,
                                              sectors=sectors)
    H2 = (S_plus2 + S_minus2 - 2.0 * S_0) / (eps2 ** 2)
    H_rich = (4.0 * H2 - H) / 3.0

    if verbose:
        print(f"    S(0) = {S_0:.6f}")
        print(f"    S(+eps) = {S_plus:.6f}, S(-eps) = {S_minus:.6f}")
        print(f"    H(eps={eps}) = {H:.4f}, H(eps/2) = {H2:.4f}")
        print(f"    H(Richardson) = {H_rich:.4f}")
        vol_0 = np.sqrt(np.linalg.det(base_metric))
        vol_p = np.sqrt(np.linalg.det(g_plus))
        vol_m = np.sqrt(np.linalg.det(g_minus))
        print(f"    Volume: base={vol_0:.6f}, +eps={vol_p:.6f}, -eps={vol_m:.6f}")

    return H_rich, S_0, S_plus, S_minus


def define_level3_offdiag_directions(base_metric):
    """
    Define off-diagonal metric perturbations.

    For a diagonal base metric, off-diagonal perturbations delta_g_{ab}
    are automatically volume-preserving to first order (since
    Tr(g^{-1} delta_g) = sum_a g_aa^{-1} * 0 = 0 for off-diagonal delta_g).

    We test representative off-diagonal mixing:
    1. Within complement: g_{34}, g_{35}, g_{36}, g_{45}, g_{46}, g_{56}
    2. Between u(2) and complement: g_{03}, g_{13}, g_{23}, g_{73}
    3. Within u(2): g_{01}, g_{02}, g_{12}, g_{07}, g_{17}, g_{27}

    Total: 6 + 4 + 6 = 16 directions. With Richardson, 4 evals each = 64 evals.
    At ~0.1s per eval, ~6-7s total.

    Each delta_g = (E_{ab} + E_{ba}) / sqrt(2) (symmetric, unit Frobenius norm).
    """
    directions = []

    # Within complement (3,4,5,6)
    for i, a in enumerate([3, 4, 5, 6]):
        for b in range(a + 1, 7):
            delta = np.zeros((8, 8))
            delta[a, b] = 1.0 / np.sqrt(2)
            delta[b, a] = 1.0 / np.sqrt(2)
            directions.append((delta, f"g_{{{a}{b}}} (complement-complement)"))

    # Between u(2)={0,1,2,7} and complement={3,4,5,6}: pick representative
    for a in [0, 1, 2, 7]:
        for b in [3]:  # Just one complement index to start; expand if needed
            delta = np.zeros((8, 8))
            delta[a, b] = 1.0 / np.sqrt(2)
            delta[b, a] = 1.0 / np.sqrt(2)
            directions.append((delta, f"g_{{{a}{b}}} (u2-complement)"))

    # Within u(2): {0,1,2} and {7}
    for a in [0, 1, 2]:
        for b in range(a + 1, 3):
            delta = np.zeros((8, 8))
            delta[a, b] = 1.0 / np.sqrt(2)
            delta[b, a] = 1.0 / np.sqrt(2)
            directions.append((delta, f"g_{{{a}{b}}} (su2-su2)"))

    for a in [0, 1, 2]:
        delta = np.zeros((8, 8))
        delta[a, 7] = 1.0 / np.sqrt(2)
        delta[7, a] = 1.0 / np.sqrt(2)
        directions.append((delta, f"g_{{{a}7}} (su2-u1)"))

    return directions


def main():
    print("=" * 72)
    print("HESS-40: Off-Jensen Hessian at the Fold")
    print("FRAMEWORK DECISIVE COMPUTATION")
    print("=" * 72)
    print(f"\nFold point: tau = {TAU_FOLD}")
    print(f"Step sizes: eps_large = {EPS_LARGE}, eps_small = {EPS_SMALL}")
    print(f"Sectors: {ALL_SECTORS}")
    print(f"Number of sectors: {len(ALL_SECTORS)}")

    t_total_start = time.time()

    # =========================================================================
    # INFRASTRUCTURE SETUP
    # =========================================================================
    print("\n--- Infrastructure Setup ---")
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    B_ab = compute_killing_form(f_abc)
    gammas = build_cliff8()

    cliff_err = validate_clifford(gammas)
    print(f"Clifford algebra error: {cliff_err:.2e}")
    assert cliff_err < 1e-14

    # Jensen scale factors at the fold
    base_sf = jensen_scale_factors(TAU_FOLD)
    print(f"\nJensen scale factors at tau={TAU_FOLD}:")
    print(f"  su(2) [0,1,2]: {base_sf[0]:.6f} (e^{{-2*{TAU_FOLD}}} = {np.exp(-2*TAU_FOLD):.6f})")
    print(f"  C^2   [3,4,5,6]: {base_sf[3]:.6f} (e^{{{TAU_FOLD}}} = {np.exp(TAU_FOLD):.6f})")
    print(f"  u(1)  [7]:       {base_sf[7]:.6f} (e^{{2*{TAU_FOLD}}} = {np.exp(2*TAU_FOLD):.6f})")
    print(f"  Volume factor: {volume_factor(base_sf):.10f}")

    # =========================================================================
    # CROSS-CHECK: S_full at Jensen point
    # =========================================================================
    print("\n--- Cross-Check: S_full at Jensen Point ---")
    t_xcheck = time.time()
    S_jensen, sector_jensen = compute_S_full(
        base_sf, B_ab, gens, f_abc, gammas, verbose=True
    )
    print(f"\n  S_full(Jensen, tau={TAU_FOLD}) = {S_jensen:.6f}")
    print(f"  Expected from s36 data:       250360.677")
    print(f"  Discrepancy:                  {abs(S_jensen - 250360.677):.3f}")
    print(f"  Cross-check time: {time.time() - t_xcheck:.1f}s")

    # Also cross-check with jensen_metric
    g_jensen = jensen_metric(B_ab, TAU_FOLD)
    g_general = general_diagonal_metric(B_ab, base_sf)
    metric_diff = np.max(np.abs(g_jensen - g_general))
    print(f"  Metric construction agreement: {metric_diff:.2e}")
    assert metric_diff < 1e-14, "Metric mismatch!"

    # =========================================================================
    # LEVEL 1: COMPLEMENT SECTOR DEFORMATIONS
    # =========================================================================
    print("\n" + "=" * 72)
    print("LEVEL 1: Complement Sector Deformations (3 directions)")
    print("=" * 72)

    level1_dirs = define_level1_directions()
    level1_results = []
    any_negative = False

    for idx, (sigma, label) in enumerate(level1_dirs):
        print(f"\n--- Direction {idx+1}/3: {label} ---")
        print(f"  sigma = [{', '.join(f'{s:+.4f}' for s in sigma)}]")
        print(f"  sum(sigma) = {np.sum(sigma):.2e} (volume check)")
        t_dir = time.time()

        H_rich, H_large, H_small, S_0, details = compute_hessian_diagonal(
            base_sf, sigma, B_ab, gens, f_abc, gammas, verbose=True
        )

        dt = time.time() - t_dir
        print(f"  Time: {dt:.1f}s")

        # Classify
        h2 = EPS_LARGE ** 2  # noise threshold
        if H_rich < -h2:
            verdict = "NEGATIVE (tachyonic)"
            any_negative = True
        elif H_rich > h2:
            verdict = "POSITIVE (stable)"
        else:
            verdict = f"MARGINAL (|H| < h^2 = {h2:.2e})"

        print(f"\n  >> H_{{sigma,sigma}} = {H_rich:.4f}  [{verdict}]")
        print(f"     Richardson quality: |H_large - H_small| / |H_rich| = "
              f"{abs(H_large - H_small) / max(abs(H_rich), 1e-10):.4f}")

        level1_results.append({
            'label': label,
            'sigma': sigma,
            'H_rich': H_rich,
            'H_large': H_large,
            'H_small': H_small,
            'S_0': S_0,
            'details': details,
            'verdict': verdict,
            'time': dt,
        })

        # EARLY STOP: if any negative, PASS immediately
        if any_negative:
            print("\n" + "*" * 72)
            print("*** NEGATIVE EIGENVALUE FOUND — GATE HESS-40: PASS (TRAPPING) ***")
            print("*" * 72)
            # Continue to check remaining L1 directions for completeness
            # but the gate verdict is already determined

    # =========================================================================
    # LEVEL 2: ALL VOLUME-PRESERVING DIAGONAL DIRECTIONS
    # =========================================================================
    print("\n" + "=" * 72)
    print("LEVEL 2: All Volume-Preserving Diagonal Directions")
    print("=" * 72)

    all_dirs, sigma_J, ortho_trans = define_level2_directions()
    level2_results = []

    for idx, (sigma, label) in enumerate(all_dirs):
        print(f"\n--- Direction {idx+1}/{len(all_dirs)}: {label} ---")
        print(f"  sigma = [{', '.join(f'{s:+.4f}' for s in sigma)}]")
        print(f"  sum(sigma) = {np.sum(sigma):.2e}")
        print(f"  dot(sigma, sigma_J) = {np.dot(sigma, sigma_J):.2e}")
        t_dir = time.time()

        H_rich, H_large, H_small, S_0, details = compute_hessian_diagonal(
            base_sf, sigma, B_ab, gens, f_abc, gammas, verbose=True
        )

        dt = time.time() - t_dir
        print(f"  Time: {dt:.1f}s")

        h2 = EPS_LARGE ** 2
        if H_rich < -h2:
            verdict = "NEGATIVE (tachyonic)"
            any_negative = True
        elif H_rich > h2:
            verdict = "POSITIVE (stable)"
        else:
            verdict = f"MARGINAL (|H| < h^2 = {h2:.2e})"

        print(f"\n  >> H_{{sigma,sigma}} = {H_rich:.4f}  [{verdict}]")

        level2_results.append({
            'label': label,
            'sigma': sigma,
            'H_rich': H_rich,
            'H_large': H_large,
            'H_small': H_small,
            'S_0': S_0,
            'details': details,
            'verdict': verdict,
            'time': dt,
            'is_jensen': idx == 0,
            'is_transverse': idx > 0,
        })

    # =========================================================================
    # LEVEL 3: OFF-DIAGONAL METRIC DEFORMATIONS
    # =========================================================================
    print("\n" + "=" * 72)
    print("LEVEL 3: Off-Diagonal Metric Deformations")
    print("=" * 72)

    base_metric = general_diagonal_metric(B_ab, base_sf)
    offdiag_dirs = define_level3_offdiag_directions(base_metric)
    level3_results = []

    print(f"\nTesting {len(offdiag_dirs)} off-diagonal directions...")

    for idx, (delta_g, label) in enumerate(offdiag_dirs):
        print(f"\n--- Off-diag {idx+1}/{len(offdiag_dirs)}: {label} ---")
        t_dir = time.time()

        H_rich, S_0, S_plus, S_minus = compute_hessian_offdiag(
            base_metric, delta_g, gens, f_abc, gammas,
            eps=EPS_LARGE, verbose=True
        )

        dt = time.time() - t_dir

        if np.isnan(H_rich):
            verdict = "INVALID (not PD)"
        elif H_rich < -(EPS_LARGE**2):
            verdict = "NEGATIVE (tachyonic)"
            any_negative = True
        elif H_rich > EPS_LARGE**2:
            verdict = "POSITIVE (stable)"
        else:
            verdict = "MARGINAL"

        print(f"  >> H = {H_rich:.4f}  [{verdict}]  ({dt:.1f}s)")

        level3_results.append({
            'label': label,
            'H_rich': H_rich,
            'verdict': verdict,
            'time': dt,
        })

        if any_negative and verdict == "NEGATIVE (tachyonic)":
            print("\n" + "*" * 72)
            print("*** NEGATIVE OFF-DIAGONAL HESSIAN — GATE HESS-40: PASS ***")
            print("*" * 72)

    H_offdiag = np.array([r['H_rich'] for r in level3_results
                           if not np.isnan(r['H_rich'])])

    # =========================================================================
    # ANALYSIS AND GATE VERDICT
    # =========================================================================
    print("\n" + "=" * 72)
    print("HESSIAN ANALYSIS")
    print("=" * 72)

    # Level 1 summary
    print("\nLevel 1 Results (complement sector deformations):")
    for r in level1_results:
        print(f"  {r['label']:40s}  H = {r['H_rich']:+12.4f}  [{r['verdict']}]")

    # Level 2 summary
    print("\nLevel 2 Results (all volume-preserving diagonal directions):")
    H_jensen = None
    H_transverse = []
    for r in level2_results:
        tag = " [JENSEN]" if r['is_jensen'] else " [TRANSVERSE]" if r['is_transverse'] else ""
        print(f"  {r['label'][:55]:55s}  H = {r['H_rich']:+12.4f}  [{r['verdict']}]{tag}")
        if r['is_jensen']:
            H_jensen = r['H_rich']
        if r['is_transverse']:
            H_transverse.append(r['H_rich'])

    H_transverse = np.array(H_transverse)

    # Level 3 summary
    print("\nLevel 3 Results (off-diagonal metric deformations):")
    for r in level3_results:
        h_str = f"{r['H_rich']:+12.4f}" if not np.isnan(r['H_rich']) else "         NaN"
        print(f"  {r['label']:40s}  H = {h_str}  [{r['verdict']}]")
    if len(H_offdiag) > 0:
        print(f"\n  Off-diagonal Hessian range: [{np.min(H_offdiag):.4f}, {np.max(H_offdiag):.4f}]")
        print(f"  min(H_offdiag) = {np.min(H_offdiag):.4f}")

    # Combine all transverse directions
    H_all_transverse = np.concatenate([H_transverse, H_offdiag])

    print(f"\nJensen direction Hessian:    H_J = {H_jensen:.4f}")
    print(f"Diagonal transverse Hessian elements:")
    for i, h in enumerate(H_transverse):
        print(f"  T{i+1}: {h:+12.4f}")
    print(f"  min:  {np.min(H_transverse):+12.4f}")
    print(f"  max:  {np.max(H_transverse):+12.4f}")

    print(f"\nAll transverse (diagonal + off-diagonal):")
    print(f"  Total directions tested: {len(H_all_transverse)}")
    print(f"  min:  {np.min(H_all_transverse):+12.4f}")
    print(f"  max:  {np.max(H_all_transverse):+12.4f}")

    # Condition number
    if np.min(np.abs(H_all_transverse)) > 0:
        cond = np.max(np.abs(H_all_transverse)) / np.min(np.abs(H_all_transverse))
        print(f"  Condition number: {cond:.2f}")
    else:
        cond = np.inf
        print(f"  Condition number: INF (zero eigenvalue)")

    # =========================================================================
    # GATE VERDICT
    # =========================================================================
    print("\n" + "=" * 72)
    print("GATE VERDICT: HESS-40")
    print("=" * 72)

    h2 = EPS_LARGE ** 2
    n_negative = np.sum(H_all_transverse < -h2)
    n_positive = np.sum(H_all_transverse > h2)
    n_marginal = len(H_all_transverse) - n_negative - n_positive

    n_diag = len(H_transverse)
    n_offdiag = len(H_offdiag)
    n_total = n_diag + n_offdiag

    print(f"\nThreshold: h^2 = {h2:.2e}")
    print(f"Total transverse directions tested: {n_total}")
    print(f"  Diagonal: {n_diag}, Off-diagonal: {n_offdiag}")
    print(f"  Negative (< -{h2:.2e}): {n_negative}")
    print(f"  Positive (> +{h2:.2e}): {n_positive}")
    print(f"  Marginal: {n_marginal}")

    if n_negative > 0:
        gate_verdict = "PASS (TRAPPING)"
        neg_mask = H_all_transverse < -h2
        gate_detail = (f"Jensen trajectory is a SADDLE POINT. {n_negative} tachyonic "
                       f"direction(s) found. Minimum H = {np.min(H_all_transverse):.4f}")
        print(f"\n  VERDICT: *** PASS (TRAPPING) ***")
        print(f"  {gate_detail}")
    elif n_positive == n_total:
        gate_verdict = "FAIL (COMPOUND NUCLEUS)"
        gate_detail = (f"All {n_total} transverse directions positive "
                       f"({n_diag} diagonal + {n_offdiag} off-diagonal). "
                       f"Min H = {np.min(H_all_transverse):.4f}. "
                       f"Jensen trajectory is a local minimum of S_full.")
        print(f"\n  VERDICT: *** FAIL (COMPOUND NUCLEUS) ***")
        print(f"  {gate_detail}")
        print(f"  Safety margin: min(H)/h^2 = {np.min(H_all_transverse)/h2:.1f}")
    else:
        gate_verdict = "NULL (inconclusive)"
        gate_detail = f"Marginal directions present. Further analysis needed."
        print(f"\n  VERDICT: {gate_verdict}")
        print(f"  {gate_detail}")

    total_time = time.time() - t_total_start
    print(f"\nTotal computation time: {total_time:.1f}s")

    # =========================================================================
    # SAVE DATA
    # =========================================================================
    print("\n--- Saving Data ---")
    outdir = os.path.dirname(os.path.abspath(__file__))

    # Collect all Hessian values
    all_H = np.concatenate([[H_jensen], H_transverse])
    all_labels = ['Jensen'] + [f'T{i+1}' for i in range(len(H_transverse))]
    all_sigmas = np.vstack([sigma_J] + list(ortho_trans))

    np.savez(os.path.join(outdir, 's40_hessian_offjensen.npz'),
             tau_fold=TAU_FOLD,
             S_jensen=S_jensen,
             base_scale_factors=base_sf,
             H_jensen=H_jensen,
             H_transverse=H_transverse,
             H_offdiag=H_offdiag,
             H_all_transverse=H_all_transverse,
             all_H=all_H,
             all_labels=np.array(all_labels),
             all_sigmas=all_sigmas,
             sigma_J=sigma_J,
             ortho_trans=np.array(ortho_trans),
             eps_large=EPS_LARGE,
             eps_small=EPS_SMALL,
             gate_verdict=gate_verdict,
             gate_detail=gate_detail,
             total_time=total_time,
             # Level 1 results
             level1_H=np.array([r['H_rich'] for r in level1_results]),
             level1_labels=np.array([r['label'] for r in level1_results]),
             # Level 2 results
             level2_H=np.array([r['H_rich'] for r in level2_results]),
             level2_labels=np.array([r['label'] for r in level2_results]),
             # Richardson quality
             level2_H_large=np.array([r['H_large'] for r in level2_results]),
             level2_H_small=np.array([r['H_small'] for r in level2_results]),
             # Level 3 results
             level3_H=np.array([r['H_rich'] for r in level3_results]),
             level3_labels=np.array([r['label'] for r in level3_results]),
             )

    print(f"  Data saved: s40_hessian_offjensen.npz")

    # =========================================================================
    # PLOT
    # =========================================================================
    print("\n--- Generating Plot ---")

    fig, axes = plt.subplots(1, 3, figsize=(18, 6))

    # Panel 1: All Hessian elements (diagonal + Jensen)
    ax1 = axes[0]
    colors = ['blue' if h > 0 else 'red' for h in all_H]
    bars = ax1.bar(range(len(all_H)), all_H, color=colors, alpha=0.7,
                   edgecolor='black', linewidth=0.5)
    ax1.axhline(y=0, color='black', linewidth=1)
    ax1.axhline(y=h2, color='gray', linewidth=0.5, linestyle='--',
                label=f'h^2 = {h2:.0e}')
    ax1.axhline(y=-h2, color='gray', linewidth=0.5, linestyle='--')
    ax1.set_xticks(range(len(all_H)))
    ax1.set_xticklabels(all_labels, rotation=45, ha='right', fontsize=8)
    ax1.set_ylabel('Hessian diagonal H_ii')
    ax1.set_title(f'Diagonal Hessian at tau={TAU_FOLD}\n(Jensen + 6 transverse)')
    ax1.legend(fontsize=8)
    ax1.grid(True, alpha=0.3)

    # Panel 2: Off-diagonal Hessian elements
    ax2 = axes[1]
    if len(H_offdiag) > 0:
        od_labels = [r['label'][:15] for r in level3_results
                      if not np.isnan(r['H_rich'])]
        colors2 = ['blue' if h > 0 else 'red' for h in H_offdiag]
        ax2.bar(range(len(H_offdiag)), H_offdiag, color=colors2, alpha=0.7,
                edgecolor='black', linewidth=0.5)
        ax2.axhline(y=0, color='black', linewidth=1)
        ax2.set_xticks(range(len(H_offdiag)))
        ax2.set_xticklabels(od_labels, rotation=90, ha='center', fontsize=6)
    ax2.set_ylabel('Hessian H_ii')
    ax2.set_title(f'Off-Diagonal Hessian (Level 3)\n{len(H_offdiag)} directions')
    ax2.grid(True, alpha=0.3)

    # Panel 3: Full transverse spectrum (sorted, all levels)
    ax3 = axes[2]
    sorted_H = np.sort(H_all_transverse)
    colors3 = ['red' if h < -h2 else ('blue' if h > h2 else 'gray')
                for h in sorted_H]
    ax3.bar(range(len(sorted_H)), sorted_H, color=colors3, alpha=0.7,
            edgecolor='black', linewidth=0.5)
    ax3.axhline(y=0, color='black', linewidth=1)
    ax3.axhline(y=h2, color='gray', linewidth=0.5, linestyle='--',
                label=f'+/- h^2 = {h2:.0e}')
    ax3.axhline(y=-h2, color='gray', linewidth=0.5, linestyle='--')
    ax3.set_xlabel('Sorted index')
    ax3.set_ylabel('Hessian eigenvalue')
    ax3.set_title(f'Full Transverse Hessian Spectrum\n'
                  f'{len(H_all_transverse)} dirs | Gate: {gate_verdict}')
    ax3.legend(fontsize=8)
    ax3.grid(True, alpha=0.3)

    plt.tight_layout()
    plot_path = os.path.join(outdir, 's40_hessian_offjensen.png')
    plt.savefig(plot_path, dpi=150)
    print(f"  Plot saved: {plot_path}")

    # =========================================================================
    # FINAL SUMMARY
    # =========================================================================
    print("\n" + "=" * 72)
    print("FINAL SUMMARY")
    print("=" * 72)
    print(f"Gate:     HESS-40")
    print(f"Verdict:  {gate_verdict}")
    print(f"Level:    3 (diagonal + off-diagonal)")
    print(f"Directions tested: {n_total} transverse "
          f"({n_diag} diagonal + {n_offdiag} off-diagonal)")
    print(f"S_full(Jensen, tau=0.190) = {S_jensen:.4f}")
    print(f"H_Jensen = {H_jensen:.4f}")
    print(f"H_transverse_diag = [{', '.join(f'{h:.1f}' for h in H_transverse)}]")
    if len(H_offdiag) > 0:
        print(f"H_offdiag range = [{np.min(H_offdiag):.1f}, {np.max(H_offdiag):.1f}]")
    print(f"min(H_all_transverse) = {np.min(H_all_transverse):.4f}")
    print(f"max(H_all_transverse) = {np.max(H_all_transverse):.4f}")
    if n_negative > 0:
        print(f"Tachyonic directions: {n_negative}")
    else:
        print(f"Safety margin: min(H)/h^2 = {np.min(H_all_transverse)/h2:.0f}")
    print(f"Total time: {total_time:.1f}s")
    print("=" * 72)

    return gate_verdict, gate_detail, all_H, H_transverse


if __name__ == '__main__':
    main()
