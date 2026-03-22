#!/usr/bin/env python3
"""
ZMATRIX-43: Off-Jensen Gradient Stiffness Z_{ij} (3x3)
=========================================================

Extends the S42 gradient stiffness computation to the full 3x3 matrix
Z_{ij} on the U(2)-invariant moduli space of left-invariant metrics
on SU(3).

The U(2)-invariant metric (Baptista Paper 15 eq 3.60) has three
independent scale factors:
    g = L1 * g_0|_{u(1)} + L2 * g_0|_{su(2)} + L3 * g_0|_{C^2}

with multiplicities (1, 3, 4) respectively.

We define three moduli space directions:
  1. Jensen (sigma): (d ln L1, d ln L2, d ln L3) = (2, -2, 1)
     Volume-preserving: 1*2 + 3*(-2) + 4*1 = 0. CHECK.
  2. Volume (phi): uniform rescaling with weight (1, 1, 1) in log space.
     d ln(vol)/dphi = 1*1 + 3*1 + 4*1 = 8.
  3. T2 (cross-block): volume-preserving AND orthogonal to Jensen
     in the DeWitt metric. Found by Gram-Schmidt.

The spectral gradient stiffness matrix is:
    Z_{ij} = sum_k mult_k * (d lambda_k / d modulus_i)(d lambda_k / d modulus_j)

where the sum runs over all KK modes (irreps and spinor eigenvalues).

Paper 15 eq 3.79 analytic check:
    Kinetic term T = (1/2)(dphi)^2 + (5/2)(dsigma)^2
    => Z_{phi,phi}^{DeWitt} = 1, Z_{sigma,sigma}^{DeWitt} = 5,
       Z_{phi,sigma}^{DeWitt} = 0.

Pre-registered gate ZMATRIX-43: INFO. Report condition number Z_max/Z_min.

Author: baptista-spacetime-analyst (Session 43)
Date: 2026-03-14
"""

import sys
import os
import time
import numpy as np
from numpy.linalg import eigh, eigvalsh, inv, det, cholesky
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from tier1_dirac_spectrum import (
    su3_generators,
    compute_structure_constants,
    compute_killing_form,
    jensen_metric,
    u2_invariant_metric,
    orthonormal_frame,
    frame_structure_constants,
    connection_coefficients,
    spinor_connection_offset,
    build_cliff8,
    validate_clifford,
    validate_connection,
    get_irrep,
    dirac_operator_on_irrep,
    _irrep_cache,
    U1_IDX, SU2_IDX, C2_IDX,
)
from canonical_constants import tau_fold as TAU_FOLD


# =========================================================================
# CONFIGURATION
# =========================================================================
H_FD = 0.0001  # finite difference step for eigenvalue derivatives (matches S42)

# Sectors for multi-sector spectral action (KK levels 0-3)
KK_SECTORS = [
    (0, 0), (1, 0), (0, 1),
    (1, 1), (2, 0), (0, 2),
    (3, 0), (0, 3), (2, 1), (1, 2),
]


def dim_pq(p, q):
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def mult_pq(p, q):
    return dim_pq(p, q) ** 2


# =========================================================================
# MODULI SPACE DIRECTIONS
# =========================================================================

def define_moduli_directions():
    """
    Define three orthogonal directions in the U(2)-invariant moduli space.

    The moduli space is parameterized by (ln L1, ln L2, ln L3) where
    L_a are scale factors for u(1), su(2), C^2 with multiplicities (1, 3, 4).

    The DeWitt metric on this space is:
        G_{IJ} = (1/4) sum_a mult_a * (d ln L_a / d phi^I)(d ln L_a / d phi^J)

    In our conventions, the "weighted" coordinates are:
        x_a = sqrt(mult_a) * ln L_a

    and the metric in (ln L1, ln L2, ln L3) space is the diagonal matrix:
        G = (1/4) * diag(1, 3, 4)

    (since (d ln L_a / dphi)^2 is weighted by mult_a).

    Directions in (d ln L1, d ln L2, d ln L3) space:

    1. Jensen: (2, -2, 1) -- volume-preserving, Paper 15 eq 3.68
    2. Volume: proportional to (1, 1, 1) -- uniform scaling
    3. T2: volume-preserving, orthogonal to Jensen

    Volume constraint: sum_a mult_a * d(ln L_a) = 0
    i.e., 1*v_1 + 3*v_2 + 4*v_3 = 0.

    We need to work with the DeWitt inner product:
        <u, v>_G = (1/4) sum_a mult_a * u_a * v_a

    where mult = (1, 3, 4).

    Returns:
        dirs: dict with keys 'Jensen', 'Volume', 'T2'
              each value is a (3,) array [d(lnL1), d(lnL2), d(lnL3)]
              normalized so that <dir, dir>_G = 1.
    """
    mult = np.array([1.0, 3.0, 4.0])

    # Jensen direction: (2, -2, 1)
    v_J = np.array([2.0, -2.0, 1.0])
    # Check volume-preserving: mult . v_J = 1*2 + 3*(-2) + 4*1 = 0
    assert abs(np.dot(mult, v_J)) < 1e-14, "Jensen not volume-preserving"
    # Norm^2 in DeWitt metric: (1/4) * (1*4 + 3*4 + 4*1) = (1/4)*20 = 5
    norm2_J = 0.25 * np.dot(mult, v_J**2)
    print(f"  Jensen DeWitt norm^2 = {norm2_J:.4f} (expected 5.0)")
    v_J_hat = v_J / np.sqrt(norm2_J)

    # Volume direction: (1, 1, 1)
    # This is NOT volume-preserving: mult . (1,1,1) = 8
    v_V = np.array([1.0, 1.0, 1.0])
    # DeWitt norm^2: (1/4) * (1+3+4) = 2
    norm2_V = 0.25 * np.dot(mult, v_V**2)
    print(f"  Volume DeWitt norm^2 = {norm2_V:.4f} (expected 2.0)")
    # Check orthogonality with Jensen:
    inner_JV = 0.25 * np.dot(mult, v_J * v_V)
    print(f"  <Jensen, Volume>_G = {inner_JV:.6f} (expected 0)")
    # Not orthogonal! inner = (1/4)*(1*2 + 3*(-2) + 4*1) = (1/4)*(2-6+4) = 0
    # Actually it IS zero! Volume-preserving directions are orthogonal to
    # the volume direction in the DeWitt metric. This is because the
    # volume constraint IS the orthogonality condition.
    assert abs(inner_JV) < 1e-14, "Jensen not orthogonal to Volume"
    v_V_hat = v_V / np.sqrt(norm2_V)

    # T2 direction: volume-preserving AND orthogonal to Jensen
    # Constraint 1: mult . v = 0  =>  v_1 + 3*v_2 + 4*v_3 = 0
    # Constraint 2: <v, v_J>_G = 0  =>  (1/4)*(1*2*v_1 + 3*(-2)*v_2 + 4*1*v_3) = 0
    #                                  =>  2*v_1 - 6*v_2 + 4*v_3 = 0
    # From constraint 1: v_1 = -3*v_2 - 4*v_3
    # Sub into constraint 2: 2*(-3*v_2 - 4*v_3) - 6*v_2 + 4*v_3 = 0
    #                        -6*v_2 - 8*v_3 - 6*v_2 + 4*v_3 = 0
    #                        -12*v_2 - 4*v_3 = 0
    #                        v_3 = -3*v_2
    # From constraint 1: v_1 = -3*v_2 - 4*(-3*v_2) = -3*v_2 + 12*v_2 = 9*v_2
    # Choose v_2 = 1: v_T2 = (9, 1, -3)
    v_T2 = np.array([9.0, 1.0, -3.0])

    # Verify constraints
    assert abs(np.dot(mult, v_T2)) < 1e-14, "T2 not volume-preserving"
    inner_JT2 = 0.25 * np.dot(mult, v_J * v_T2)
    assert abs(inner_JT2) < 1e-14, "T2 not orthogonal to Jensen"
    inner_VT2 = 0.25 * np.dot(mult, v_V * v_T2)
    print(f"  <Volume, T2>_G = {inner_VT2:.6f} (expected 0)")
    # = (1/4)*(1*9 + 3*1 + 4*(-3)) = (1/4)*(9+3-12) = 0
    assert abs(inner_VT2) < 1e-14, "T2 not orthogonal to Volume"

    norm2_T2 = 0.25 * np.dot(mult, v_T2**2)
    print(f"  T2 DeWitt norm^2 = {norm2_T2:.4f}")
    v_T2_hat = v_T2 / np.sqrt(norm2_T2)

    # Verify Paper 15 eq 3.79: kinetic coefficients
    # T = (1/2)(dphi)^2 + (5/2)(dsigma)^2
    # In terms of the DeWitt norm: Z_{JJ}^{DeWitt} = <v_J, v_J>_G = 5
    # For a canonically normalized sigma with T = (5/2)(dsigma)^2:
    #   (1/2)*Z_{sigma,sigma}*(dsigma)^2 = (5/2)*(dsigma)^2
    #   => Z_{sigma,sigma} = 5
    # For phi with T = (1/2)(dphi)^2:
    #   (1/2)*Z_{phi,phi}*(dphi)^2 = (1/2)*(dphi)^2
    #   => Z_{phi,phi} = 1
    # But these are for the Baptista normalization of phi and sigma.
    #
    # Our sigma_hat has |sigma_hat|_G^2 = 1, so if we use sigma_hat
    # as modulus, the kinetic term would be (1/2)*(dsigma_hat)^2.
    # Baptista's sigma has kinetic coefficient 5/2 because his sigma
    # is not unit-normalized: |v_J|_G^2 = 5.

    dirs = {
        'Jensen': v_J,          # not normalized
        'Volume': v_V,          # not normalized
        'T2': v_T2,             # not normalized
        'Jensen_hat': v_J_hat,  # unit normalized in DeWitt metric
        'Volume_hat': v_V_hat,
        'T2_hat': v_T2_hat,
    }

    # Print the directions
    print("\n  Moduli space directions (d ln L1, d ln L2, d ln L3):")
    print(f"  {'Direction':>12}  {'d(lnL1)':>9}  {'d(lnL2)':>9}  {'d(lnL3)':>9}  "
          f"{'|v|^2_G':>9}  {'Vol-pres?':>10}")
    print("  " + "-" * 65)
    for name, v in [('Jensen', v_J), ('Volume', v_V), ('T2', v_T2)]:
        n2 = 0.25 * np.dot(mult, v**2)
        vp = abs(np.dot(mult, v)) < 1e-14
        print(f"  {name:>12}  {v[0]:9.4f}  {v[1]:9.4f}  {v[2]:9.4f}  "
              f"{n2:9.4f}  {'YES' if vp else 'NO':>10}")

    return dirs


def deform_metric(B_ab, tau, direction, epsilon):
    """
    Construct the U(2)-invariant metric at a point displaced from the
    Jensen curve by epsilon in the given direction.

    Starting from the Jensen metric at parameter tau:
        L1_0 = exp(2*tau), L2_0 = exp(-2*tau), L3_0 = exp(tau)

    The displacement in direction v = (v1, v2, v3) by step epsilon gives:
        L_a(epsilon) = L_a_0 * exp(epsilon * v_a)

    This ensures positivity and composes correctly with the logarithmic
    parameterization.

    Args:
        B_ab: (8,8) Killing form
        tau: Jensen parameter
        direction: (3,) array [d(lnL1), d(lnL2), d(lnL3)]
        epsilon: displacement size

    Returns:
        g: (8,8) metric tensor
    """
    L1_0 = np.exp(2.0 * tau)
    L2_0 = np.exp(-2.0 * tau)
    L3_0 = np.exp(tau)

    L1 = L1_0 * np.exp(epsilon * direction[0])
    L2 = L2_0 * np.exp(epsilon * direction[1])
    L3 = L3_0 * np.exp(epsilon * direction[2])

    return u2_invariant_metric(B_ab, L1, L2, L3)


def compute_eigenvalues_at_metric(g, f_abc, gens, gammas):
    """
    Compute sorted eigenvalues of iD_K for each KK sector at a given metric.

    Args:
        g: (8,8) metric tensor
        f_abc: structure constants
        gens: generators
        gammas: Clifford algebra generators

    Returns:
        sector_evals: dict (p,q) -> sorted eigenvalue array
        S_total: total spectral action sum |lambda| * mult
    """
    E = orthonormal_frame(g)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)

    conn_err = validate_connection(Gamma)
    if conn_err > 1e-10:
        print(f"    WARNING: Connection metric compatibility error = {conn_err:.2e}")

    Omega = spinor_connection_offset(Gamma, gammas)

    _irrep_cache.clear()
    sector_evals = {}
    S_total = 0.0

    for p, q in KK_SECTORS:
        rho, dim_r = get_irrep(p, q, gens, f_abc)
        D_pi = dirac_operator_on_irrep(rho, E, gammas, Omega)
        iD = 1j * D_pi
        ev = eigvalsh(iD)
        sector_evals[(p, q)] = np.sort(ev)
        m = mult_pq(p, q)
        S_total += m * np.sum(np.abs(ev))

    return sector_evals, S_total


# =========================================================================
# ANALYTIC DeWitt METRIC COMPUTATION (Approach A)
# =========================================================================

def compute_dewitt_metric_analytic():
    """
    Compute the analytic 3x3 DeWitt metric G_{IJ} on the moduli space.

    For the U(2)-invariant metrics with scale factors (L1, L2, L3)
    and multiplicities (1, 3, 4), the DeWitt metric in log-scale
    coordinates u_a = ln L_a is:

        G_{IJ} = (1/4) sum_a mult_a * (du_a/dphi^I)(du_a/dphi^J)

    where phi^I are the moduli. For our three directions:

    Jensen: (du_1, du_2, du_3) = (2, -2, 1)
    Volume: (du_1, du_2, du_3) = (1, 1, 1)
    T2:     (du_1, du_2, du_3) = (9, 1, -3)

    Returns:
        G: (3,3) DeWitt metric in the (Jensen, Volume, T2) basis
    """
    mult = np.array([1.0, 3.0, 4.0])
    dirs = np.array([
        [2.0, -2.0, 1.0],    # Jensen
        [1.0, 1.0, 1.0],     # Volume
        [9.0, 1.0, -3.0],    # T2
    ])

    G = np.zeros((3, 3))
    for I in range(3):
        for J in range(3):
            G[I, J] = 0.25 * np.sum(mult * dirs[I] * dirs[J])

    return G


# =========================================================================
# SPECTRAL GRADIENT STIFFNESS MATRIX
# =========================================================================

def compute_z_matrix(tau, gens, f_abc, B_ab, gammas, directions, h=H_FD):
    """
    Compute the 3x3 spectral gradient stiffness matrix Z_{ij} at a given tau.

    Z_{ij} = sum_k mult_k * (d lambda_k / d modulus_i)(d lambda_k / d modulus_j)

    where the derivatives are taken with respect to the three moduli space
    directions (Jensen, Volume, T2).

    Method: Central finite differences. For each direction i, compute
    eigenvalues at tau +/- h*direction_i, then:
        d lambda_k / d modulus_i = (lambda_k(+h) - lambda_k(-h)) / (2*h)

    Args:
        tau: Jensen parameter (fold point)
        gens, f_abc, B_ab, gammas: infrastructure
        directions: dict with 'Jensen', 'Volume', 'T2' entries
        h: finite difference step size

    Returns:
        Z: (3,3) spectral stiffness matrix
        Z_per_sector: dict (p,q) -> (3,3) contribution from that sector
        evals_center: eigenvalues at the center point
        S_center: spectral action at the center
        metadata: additional diagnostic information
    """
    dir_names = ['Jensen', 'Volume', 'T2']
    dir_vecs = [directions[name] for name in dir_names]

    print(f"\n  Computing eigenvalues at tau = {tau:.4f}...")
    t0 = time.time()

    # Step 1: Compute eigenvalues at the center point (Jensen metric at tau)
    g_center = jensen_metric(B_ab, tau)
    evals_center, S_center = compute_eigenvalues_at_metric(
        g_center, f_abc, gens, gammas
    )
    print(f"    Center point: S_total = {S_center:.2f}")

    # Step 2: Compute eigenvalues at +h and -h for each direction
    # We need 6 off-center points: 3 directions x 2 signs
    evals_displaced = {}  # (dir_idx, sign) -> sector_evals

    for i, (name, v) in enumerate(zip(dir_names, dir_vecs)):
        for sign, label in [(+1, '+'), (-1, '-')]:
            g_disp = deform_metric(B_ab, tau, v, sign * h)
            ev_disp, S_disp = compute_eigenvalues_at_metric(
                g_disp, f_abc, gens, gammas
            )
            evals_displaced[(i, sign)] = ev_disp
            print(f"    {name} ({label}h): S_total = {S_disp:.2f}")

    # Step 3: Compute eigenvalue derivatives by central differences
    # d lambda_k^{(p,q)} / d modulus_i = (ev(+h)_k - ev(-h)_k) / (2*h)
    # for each sector (p,q) and each direction i

    dlambda = {}  # (dir_idx, (p,q)) -> array of derivatives

    for i in range(3):
        for p, q in KK_SECTORS:
            ev_plus = evals_displaced[(i, +1)][(p, q)]
            ev_minus = evals_displaced[(i, -1)][(p, q)]
            dl = (ev_plus - ev_minus) / (2 * h)
            dlambda[(i, (p, q))] = dl

    # Step 4: Construct Z_{ij} = sum_{(p,q)} mult * sum_k dlambda_i_k * dlambda_j_k
    Z = np.zeros((3, 3))
    Z_per_sector = {}

    for p, q in KK_SECTORS:
        m = mult_pq(p, q)
        Z_sec = np.zeros((3, 3))

        for i in range(3):
            for j in range(3):
                dl_i = dlambda[(i, (p, q))]
                dl_j = dlambda[(j, (p, q))]
                Z_sec[i, j] = m * np.sum(dl_i * dl_j)

        Z += Z_sec
        Z_per_sector[(p, q)] = Z_sec

    elapsed = time.time() - t0
    print(f"    Elapsed: {elapsed:.1f}s")

    # Step 5: Verify symmetry of Z
    sym_err = np.max(np.abs(Z - Z.T))
    print(f"    Z symmetry error: {sym_err:.2e}")

    # Metadata for diagnostics
    metadata = {
        'elapsed': elapsed,
        'sym_err': sym_err,
        'S_center': S_center,
        'h': h,
    }

    return Z, Z_per_sector, evals_center, S_center, metadata


# =========================================================================
# MAIN COMPUTATION
# =========================================================================

def main():
    print("=" * 70)
    print("ZMATRIX-43: OFF-JENSEN GRADIENT STIFFNESS Z_{ij} (3x3)")
    print("=" * 70)
    print(f"Fold point: tau_0 = {TAU_FOLD}")
    print(f"FD step: h = {H_FD}")
    print(f"Gate: ZMATRIX-43 (INFO -- structural)")
    print()

    t_total = time.time()

    # ===== Initialize infrastructure =====
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    B_ab = compute_killing_form(f_abc)
    gammas = build_cliff8()

    cliff_err = validate_clifford(gammas)
    print(f"Clifford algebra validation: max_err = {cliff_err:.2e}")
    assert cliff_err < 1e-14

    # ===== Define moduli space directions =====
    print("\n" + "=" * 70)
    print("MODULI SPACE DIRECTIONS")
    print("=" * 70)

    dirs = define_moduli_directions()

    # ===== Analytic DeWitt metric =====
    print("\n" + "=" * 70)
    print("APPROACH A: ANALYTIC DeWitt METRIC G_{IJ}")
    print("=" * 70)

    G_analytic = compute_dewitt_metric_analytic()
    print("\n  G_{IJ} (DeWitt metric) in (Jensen, Volume, T2) basis:")
    labels = ['Jensen', 'Volume', 'T2']
    print(f"  {'':>10}", end="")
    for l in labels:
        print(f"  {l:>10}", end="")
    print()
    for i in range(3):
        print(f"  {labels[i]:>10}", end="")
        for j in range(3):
            print(f"  {G_analytic[i, j]:10.4f}", end="")
        print()

    # Eigenvalues of G
    G_evals, G_evecs = np.linalg.eigh(G_analytic)
    print(f"\n  G eigenvalues: {G_evals}")
    print(f"  G condition number: {G_evals[-1]/G_evals[0]:.4f}")

    # Cross-check: Paper 15 eq 3.79 coefficients
    # The kinetic term (1/2)(dphi)^2 + (5/2)(dsigma)^2 corresponds to:
    # G_{JJ} = 5 (Jensen-Jensen) and G_{VV} = 2 (Volume-Volume)
    # Note: Baptista defines phi so that the kinetic term has coefficient 1/2.
    # Our Volume direction (1,1,1) has G_VV = (1/4)*(1+3+4) = 2.
    # With phi = sigma_V/sqrt(2*G_VV) (canonical normalization):
    #   (1/2)*G_VV*(dsigma_V)^2 = (1/2)*2*(dsigma_V)^2
    # Paper 15 uses phi such that T = (1/2)(dphi)^2, i.e., phi is
    # already canonically normalized. Our Volume direction gives G_VV = 2,
    # consistent with T = (1/2)*2*(dsigma_V)^2 = (dsigma_V)^2.
    # But Paper 15's (1/2)(dphi)^2 = (1/2)(dphi)^2 where phi is the
    # specific conformal factor in eq 3.39, not just any volume modulus.

    print(f"\n  Cross-check against Paper 15 eq 3.79:")
    print(f"    G_JJ = {G_analytic[0,0]:.4f} (expected 5.0 from DeWitt, "
          f"consistent with (5/2)*dsigma^2 for sigma = tau)")
    print(f"    G_VV = {G_analytic[1,1]:.4f} (expected 2.0 from DeWitt)")
    print(f"    G_TT = {G_analytic[2,2]:.4f} (T2 DeWitt norm)")
    print(f"    G_JV = {G_analytic[0,1]:.4f} (expected 0)")
    print(f"    G_JT = {G_analytic[0,2]:.4f} (expected 0)")
    print(f"    G_VT = {G_analytic[1,2]:.4f} (expected 0)")

    # ===== Spectral gradient stiffness matrix at fold =====
    print("\n" + "=" * 70)
    print("SPECTRAL GRADIENT STIFFNESS Z_{ij} AT FOLD")
    print("=" * 70)

    Z, Z_per_sector, evals_center, S_center, meta = compute_z_matrix(
        TAU_FOLD, gens, f_abc, B_ab, gammas, dirs, h=H_FD
    )

    # Print Z matrix
    print(f"\n  Z_{{ij}} matrix at tau = {TAU_FOLD:.3f}:")
    print(f"  {'':>10}", end="")
    for l in labels:
        print(f"  {l:>12}", end="")
    print()
    for i in range(3):
        print(f"  {labels[i]:>10}", end="")
        for j in range(3):
            print(f"  {Z[i, j]:12.4f}", end="")
        print()

    # Diagonalize Z
    Z_evals, Z_evecs = np.linalg.eigh(Z)
    print(f"\n  Z eigenvalues: {Z_evals}")
    print(f"  Z eigenvectors (columns):")
    for i in range(3):
        print(f"    eigvec_{i} ({labels[0]}={Z_evecs[0,i]:.4f}, "
              f"{labels[1]}={Z_evecs[1,i]:.4f}, "
              f"{labels[2]}={Z_evecs[2,i]:.4f})")

    Z_max = Z_evals[-1]
    Z_min = Z_evals[0]
    if Z_min > 0:
        cond = Z_max / Z_min
    else:
        cond = float('inf')
    print(f"\n  Z_max = {Z_max:.4f}")
    print(f"  Z_min = {Z_min:.4f}")
    print(f"  Condition number = Z_max / Z_min = {cond:.4f}")

    # ===== Cross-check: Z_JJ vs S42 result =====
    Z_JJ = Z[0, 0]
    Z_S42 = 74730.76  # from s42_gradient_stiffness.npz
    print(f"\n  Cross-check Z_JJ:")
    print(f"    Z_JJ (this computation) = {Z_JJ:.4f}")
    print(f"    Z_JJ (S42) = {Z_S42:.2f}")
    rel_err = abs(Z_JJ - Z_S42) / Z_S42
    print(f"    Relative error = {rel_err:.6e}")

    # ===== Finite-difference convergence check =====
    print("\n" + "=" * 70)
    print("CONVERGENCE CHECK: h = 0.0001 vs h = 0.00005")
    print("=" * 70)

    h2 = 0.00005
    Z2, _, _, _, _ = compute_z_matrix(
        TAU_FOLD, gens, f_abc, B_ab, gammas, dirs, h=h2
    )
    print(f"\n  Z at h={h2}:")
    for i in range(3):
        print(f"  {labels[i]:>10}", end="")
        for j in range(3):
            print(f"  {Z2[i, j]:12.4f}", end="")
        print()

    conv_err = np.max(np.abs(Z2 - Z)) / np.max(np.abs(Z))
    print(f"\n  Max relative difference |Z(h/2) - Z(h)| / max|Z| = {conv_err:.6e}")
    if conv_err < 0.01:
        print("  CONVERGED (< 1%)")
    else:
        print(f"  NOT CONVERGED ({conv_err*100:.2f}%)")

    # ===== Per-sector breakdown =====
    print("\n" + "=" * 70)
    print("PER-SECTOR BREAKDOWN AT FOLD")
    print("=" * 70)

    print(f"\n  {'Sector':>8}  {'mult':>6}  {'Z_JJ':>12}  {'Z_VV':>12}  "
          f"{'Z_TT':>12}  {'Z_JV':>12}  {'Z_JT':>12}  {'Z_VT':>12}")
    print("  " + "-" * 85)
    for p, q in KK_SECTORS:
        Zs = Z_per_sector[(p, q)]
        m = mult_pq(p, q)
        print(f"  ({p},{q}):   {m:5d}  {Zs[0,0]:12.4f}  {Zs[1,1]:12.4f}  "
              f"{Zs[2,2]:12.4f}  {Zs[0,1]:12.4f}  {Zs[0,2]:12.4f}  {Zs[1,2]:12.4f}")

    # Fraction of Z from each sector
    print(f"\n  Fractional contributions to Z_JJ, Z_VV, Z_TT:")
    print(f"  {'Sector':>8}  {'f_JJ':>8}  {'f_VV':>8}  {'f_TT':>8}")
    print("  " + "-" * 38)
    for p, q in KK_SECTORS:
        Zs = Z_per_sector[(p, q)]
        f_JJ = Zs[0,0] / Z[0,0] if abs(Z[0,0]) > 1e-15 else 0
        f_VV = Zs[1,1] / Z[1,1] if abs(Z[1,1]) > 1e-15 else 0
        f_TT = Zs[2,2] / Z[2,2] if abs(Z[2,2]) > 1e-15 else 0
        print(f"  ({p},{q}):   {f_JJ:8.5f}  {f_VV:8.5f}  {f_TT:8.5f}")

    # ===== Ratio Z_spectral / G_DeWitt =====
    print("\n" + "=" * 70)
    print("AMPLIFICATION: Z_spectral / G_DeWitt")
    print("=" * 70)

    ratio_matrix = np.zeros((3, 3))
    for i in range(3):
        for j in range(3):
            if abs(G_analytic[i, j]) > 1e-15:
                ratio_matrix[i, j] = Z[i, j] / G_analytic[i, j]
            else:
                ratio_matrix[i, j] = float('nan')

    print(f"\n  Z_{'{'}ij{'}'} / G_{'{'}ij{'}'}:")
    print(f"  {'':>10}", end="")
    for l in labels:
        print(f"  {l:>12}", end="")
    print()
    for i in range(3):
        print(f"  {labels[i]:>10}", end="")
        for j in range(3):
            if abs(G_analytic[i, j]) > 1e-15:
                print(f"  {ratio_matrix[i, j]:12.2f}", end="")
            else:
                print(f"  {'N/A':>12}", end="")
        print()

    # Diagonal amplification factors
    amp_J = Z[0, 0] / G_analytic[0, 0] if G_analytic[0, 0] > 0 else float('inf')
    amp_V = Z[1, 1] / G_analytic[1, 1] if G_analytic[1, 1] > 0 else float('inf')
    amp_T = Z[2, 2] / G_analytic[2, 2] if G_analytic[2, 2] > 0 else float('inf')

    print(f"\n  Amplification factors (diagonal):")
    print(f"    Jensen:  Z_JJ / G_JJ = {Z[0,0]:.2f} / {G_analytic[0,0]:.2f} = {amp_J:.2f}")
    print(f"    Volume:  Z_VV / G_VV = {Z[1,1]:.2f} / {G_analytic[1,1]:.2f} = {amp_V:.2f}")
    print(f"    T2:      Z_TT / G_TT = {Z[2,2]:.2f} / {G_analytic[2,2]:.2f} = {amp_T:.2f}")

    # ===== Paper 15 eq 3.79 coefficient check =====
    # The kinetic term for sigma (Jensen) has coefficient 5/2 in Paper 15.
    # Our Z_JJ should be the spectral amplification of G_JJ = 5.
    # Paper 15's coefficient of (5/2) is the DeWitt metric G_JJ/2 = 5/2.
    # The spectral kinetic coefficient would be Z_JJ/2.
    print(f"\n  Paper 15 eq 3.79 spectral kinetic coefficients:")
    print(f"    Jensen sigma: (1/2)*Z_JJ = {Z[0,0]/2:.2f} "
          f"(Paper 15 DeWitt: 5/2 = {5/2:.2f})")
    print(f"    Volume phi:   (1/2)*Z_VV = {Z[1,1]/2:.2f} "
          f"(Paper 15 DeWitt: 1/2 * G_VV = {G_analytic[1,1]/2:.2f})")
    print(f"    T2 cross:     (1/2)*Z_TT = {Z[2,2]/2:.2f} "
          f"(Paper 15 DeWitt: 1/2 * G_TT = {G_analytic[2,2]/2:.2f})")

    # ===== Accessibility analysis =====
    print("\n" + "=" * 70)
    print("ACCESSIBILITY ANALYSIS")
    print("=" * 70)

    # The question: if Z_min << Z_JJ = 74,731, then spatial perturbations
    # in the Z_min direction have low gradient cost -> accessible for
    # multi-field dynamics

    print(f"\n  Z_JJ (Jensen) = {Z[0,0]:.4f}")
    print(f"  Z_VV (Volume) = {Z[1,1]:.4f}")
    print(f"  Z_TT (T2)     = {Z[2,2]:.4f}")
    print(f"  Z_min         = {Z_min:.4f}")
    print(f"  Z_max         = {Z_max:.4f}")

    if Z_min > 0:
        print(f"\n  Z_min / Z_JJ = {Z_min / Z[0,0]:.6f}")
        if Z_min < Z[0, 0]:
            softest_idx = np.argmin(Z_evals)
            softest_vec = Z_evecs[:, softest_idx]
            print(f"  Softest direction: ({softest_vec[0]:.4f}*Jensen, "
                  f"{softest_vec[1]:.4f}*Volume, {softest_vec[2]:.4f}*T2)")
            print(f"  This direction has {Z_min / Z[0,0] * 100:.2f}% of Jensen stiffness")
            print(f"  => Spatial perturbations PREFER this direction over Jensen")
        else:
            print(f"  All directions have stiffness >= Jensen")
            print(f"  => Jensen IS the softest direction")
    else:
        print(f"\n  WARNING: Z has negative eigenvalue => INSTABILITY")
        neg_idx = np.where(Z_evals < 0)[0]
        for idx in neg_idx:
            print(f"    Unstable direction: ({Z_evecs[0,idx]:.4f}*Jensen, "
                  f"{Z_evecs[1,idx]:.4f}*Volume, {Z_evecs[2,idx]:.4f}*T2)")
            print(f"    Eigenvalue: {Z_evals[idx]:.6f}")

    # ===== Multi-field dynamics implications =====
    print("\n" + "=" * 70)
    print("MULTI-FIELD DYNAMICS IMPLICATIONS")
    print("=" * 70)

    # The off-diagonal entries Z_{ij} (i != j) determine mode coupling.
    # A large Z_{JT} means Jensen and T2 are dynamically coupled.
    # A small Z_{JT} means they evolve independently.

    for i in range(3):
        for j in range(i+1, 3):
            if Z[i, i] > 0 and Z[j, j] > 0:
                coupling = abs(Z[i, j]) / np.sqrt(Z[i, i] * Z[j, j])
                print(f"  Coupling |Z_{{{labels[i][0]},{labels[j][0]}}}| / "
                      f"sqrt(Z_{{{labels[i][0]}{labels[i][0]}}} * Z_{{{labels[j][0]}{labels[j][0]}}}) "
                      f"= {coupling:.6f}")
            else:
                print(f"  Coupling {labels[i]}-{labels[j]}: undefined (negative diagonal)")

    # ===== GATE VERDICT =====
    print("\n" + "=" * 70)
    print("GATE VERDICT: ZMATRIX-43")
    print("=" * 70)

    print(f"\n  Gate type: INFO (structural)")
    print(f"  Condition number Z_max/Z_min = {cond:.4f}")
    print(f"\n  Z_{'{'}ij{'}'} matrix:")
    for i in range(3):
        row = "    [" + ", ".join(f"{Z[i,j]:12.4f}" for j in range(3)) + "]"
        print(row)
    print(f"\n  Eigenvalues: {Z_evals}")
    print(f"  >>> ZMATRIX-43: INFO -- condition number = {cond:.4f} <<<")

    # ===================================================================
    # SAVE DATA
    # ===================================================================
    print("\n" + "=" * 70)
    print("SAVING DATA")
    print("=" * 70)

    save_data = {
        'tau_fold': np.array([TAU_FOLD]),
        'h_fd': np.array([H_FD]),
        'Z_matrix': Z,
        'Z_eigenvalues': Z_evals,
        'Z_eigenvectors': Z_evecs,
        'G_DeWitt': G_analytic,
        'G_eigenvalues': G_evals,
        'S_center': np.array([S_center]),
        'condition_number': np.array([cond]),
        'Z_JJ': np.array([Z[0, 0]]),
        'Z_VV': np.array([Z[1, 1]]),
        'Z_TT': np.array([Z[2, 2]]),
        'Z_JV': np.array([Z[0, 1]]),
        'Z_JT': np.array([Z[0, 2]]),
        'Z_VT': np.array([Z[1, 2]]),
        'amplification_J': np.array([amp_J]),
        'amplification_V': np.array([amp_V]),
        'amplification_T': np.array([amp_T]),
        'dir_Jensen': dirs['Jensen'],
        'dir_Volume': dirs['Volume'],
        'dir_T2': dirs['T2'],
        'convergence_err': np.array([conv_err]),
        'Z_matrix_h2': Z2,
    }

    # Per-sector Z
    for p, q in KK_SECTORS:
        save_data[f'Z_sector_{p}_{q}'] = Z_per_sector[(p, q)]

    outpath_npz = os.path.join(SCRIPT_DIR, 's43_offjensen_z_matrix.npz')
    np.savez_compressed(outpath_npz, **save_data)
    print(f"  Data saved: {outpath_npz}")

    # ===================================================================
    # PLOT
    # ===================================================================

    fig, axes = plt.subplots(2, 2, figsize=(16, 12))

    # Panel 1: Z matrix heatmap
    ax = axes[0, 0]
    im = ax.imshow(Z, cmap='viridis', aspect='auto')
    ax.set_xticks(range(3))
    ax.set_yticks(range(3))
    ax.set_xticklabels(labels, fontsize=11)
    ax.set_yticklabels(labels, fontsize=11)
    for i in range(3):
        for j in range(3):
            ax.text(j, i, f'{Z[i,j]:.1f}', ha='center', va='center',
                    color='white' if Z[i,j] < Z.max()*0.5 else 'black',
                    fontsize=10, fontweight='bold')
    plt.colorbar(im, ax=ax, label='Z_{ij}')
    ax.set_title('Spectral Gradient Stiffness Z_{ij}', fontsize=13)

    # Panel 2: G_DeWitt heatmap for comparison
    ax = axes[0, 1]
    im2 = ax.imshow(G_analytic, cmap='viridis', aspect='auto')
    ax.set_xticks(range(3))
    ax.set_yticks(range(3))
    ax.set_xticklabels(labels, fontsize=11)
    ax.set_yticklabels(labels, fontsize=11)
    for i in range(3):
        for j in range(3):
            ax.text(j, i, f'{G_analytic[i,j]:.2f}', ha='center', va='center',
                    color='white' if G_analytic[i,j] < G_analytic.max()*0.5 else 'black',
                    fontsize=10, fontweight='bold')
    plt.colorbar(im2, ax=ax, label='G_{ij}')
    ax.set_title('Analytic DeWitt Metric G_{ij}', fontsize=13)

    # Panel 3: Eigenvalue comparison
    ax = axes[1, 0]
    x = np.arange(3)
    width = 0.35
    bars1 = ax.bar(x - width/2, Z_evals, width, label='Z eigenvalues',
                   color='steelblue', alpha=0.8)
    bars2 = ax.bar(x + width/2, G_evals, width, label='G eigenvalues',
                   color='orange', alpha=0.8)
    ax.set_xticks(x)
    ax.set_xticklabels([f'e_{i+1}' for i in range(3)], fontsize=11)
    ax.set_ylabel('Eigenvalue', fontsize=12)
    ax.set_title('Z vs G Eigenvalues', fontsize=13)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3, axis='y')

    # Panel 4: Per-sector diagonal contributions
    ax = axes[1, 1]
    sector_labels = [f'({p},{q})' for p, q in KK_SECTORS]
    Z_JJ_sectors = [Z_per_sector[(p, q)][0, 0] for p, q in KK_SECTORS]
    Z_VV_sectors = [Z_per_sector[(p, q)][1, 1] for p, q in KK_SECTORS]
    Z_TT_sectors = [Z_per_sector[(p, q)][2, 2] for p, q in KK_SECTORS]

    x = np.arange(len(KK_SECTORS))
    width = 0.25
    ax.bar(x - width, Z_JJ_sectors, width, label='Z_JJ', color='steelblue', alpha=0.8)
    ax.bar(x, Z_VV_sectors, width, label='Z_VV', color='orange', alpha=0.8)
    ax.bar(x + width, Z_TT_sectors, width, label='Z_TT', color='green', alpha=0.8)
    ax.set_xticks(x)
    ax.set_xticklabels(sector_labels, fontsize=9)
    ax.set_xlabel('Sector (p,q)', fontsize=12)
    ax.set_ylabel('Z diagonal contribution', fontsize=12)
    ax.set_title('Z_{ii} by KK Sector', fontsize=13)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3, axis='y')

    plt.suptitle(
        f'ZMATRIX-43: Off-Jensen Gradient Stiffness\n'
        f'Condition number = {cond:.2f}, '
        f'Z_JJ={Z[0,0]:.0f}, Z_VV={Z[1,1]:.0f}, Z_TT={Z[2,2]:.0f}',
        fontsize=14, fontweight='bold'
    )
    plt.tight_layout()

    outpath_png = os.path.join(SCRIPT_DIR, 's43_offjensen_z_matrix.png')
    plt.savefig(outpath_png, dpi=150, bbox_inches='tight')
    print(f"  Plot saved: {outpath_png}")

    # ===================================================================
    # FINAL SUMMARY
    # ===================================================================
    elapsed_total = time.time() - t_total

    print(f"\n{'='*70}")
    print(f"FINAL SUMMARY: ZMATRIX-43")
    print(f"{'='*70}")
    print(f"""
MODULI SPACE: 3 directions on U(2)-invariant left-invariant metrics on SU(3)
  Jensen:  (d ln L1, d ln L2, d ln L3) = (2, -2, 1)   [volume-preserving]
  Volume:  (d ln L1, d ln L2, d ln L3) = (1, 1, 1)     [breathing mode]
  T2:      (d ln L1, d ln L2, d ln L3) = (9, 1, -3)    [cross-block, vol-preserving]

DeWitt METRIC G_ij (analytic, Paper 15):
  G_JJ = {G_analytic[0,0]:.4f}  (Jensen kinetic coefficient)
  G_VV = {G_analytic[1,1]:.4f}  (Volume kinetic coefficient)
  G_TT = {G_analytic[2,2]:.4f}  (T2 kinetic coefficient)
  All off-diagonals = 0 (orthogonal basis by construction)

SPECTRAL STIFFNESS Z_ij at tau = {TAU_FOLD}:
  Z_JJ = {Z[0,0]:.4f}  (Jensen, cross-check S42: {Z_S42:.2f}, rel err {rel_err:.2e})
  Z_VV = {Z[1,1]:.4f}  (Volume)
  Z_TT = {Z[2,2]:.4f}  (T2)
  Z_JV = {Z[0,1]:.4f}  Z_JT = {Z[0,2]:.4f}  Z_VT = {Z[1,2]:.4f}

EIGENVALUES of Z:
  e_1 = {Z_evals[0]:.4f}
  e_2 = {Z_evals[1]:.4f}
  e_3 = {Z_evals[2]:.4f}

CONDITION NUMBER: Z_max/Z_min = {cond:.4f}

AMPLIFICATION Z/G (spectral enhancement over geometry):
  Jensen: {amp_J:.2f}x
  Volume: {amp_V:.2f}x
  T2:     {amp_T:.2f}x

CONVERGENCE: h=0.0001 vs h=0.00005: max rel diff = {conv_err:.2e}

Total runtime: {elapsed_total:.1f}s
""")

    return Z, Z_evals, Z_evecs, G_analytic, cond


if __name__ == "__main__":
    Z, Z_evals, Z_evecs, G, cond = main()
    print(f"\nDone. Condition number: {cond:.4f}")
