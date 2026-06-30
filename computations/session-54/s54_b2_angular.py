#!/usr/bin/env python3
"""
S54 B2-ANGULAR-54: Wavefunction Angular Decomposition (Mass Variation Sign)
===========================================================================

QUESTION: Does the B2 sector sit preferentially in the e^{+tau} stretching
direction (C^2 block) or the e^{-2tau} shrinking direction (su(2) block)?
The sign determines whether the BCS mass variation during transit produces
expansion or contraction.

METHOD:
  1. Build the (0,0) singlet Dirac operator Omega(tau) at multiple tau values
  2. Diagonalize to get B2 eigenvectors
  3. Decompose dOmega/dtau into Jensen subspace contributions:
     - d/dtau(Omega)|_{u(1)}: contribution from u(1) direction (metric e^{+2tau})
     - d/dtau(Omega)|_{su(2)}: contribution from su(2) direction (metric e^{-2tau})
     - d/dtau(Omega)|_{C^2}: contribution from C^2 direction (metric e^{+tau})
  4. Use first-order perturbation theory:
     d(lambda_k^2)/dtau = 2*lambda_k * <psi_k| dOmega/dtau |psi_k>
  5. Decompose into subspace contributions to determine sign

JENSEN METRIC:
  g_s = e^{+2s} g_0|_{u(1)} + e^{-2s} g_0|_{su(2)} + e^{+s} g_0|_{C^2}

  d/ds(g) = +2 e^{+2s} g_0|_{u(1)} - 2 e^{-2s} g_0|_{su(2)} + e^{+s} g_0|_{C^2}

  So the metric derivatives have coefficients +2, -2, +1 for the three subspaces.
  The su(2) direction SHRINKS (coefficient -2) while u(1) and C^2 STRETCH.

SIGN CONVENTION:
  - If d(m^2)/dtau > 0 at fold: mass INCREASES -> contraction tendency
  - If d(m^2)/dtau < 0 at fold: mass DECREASES -> expansion tendency

Author: baptista-spacetime-analyst, Session 54
Date: 2026-03-21
"""

import os
import sys
import time
import numpy as np
from numpy.linalg import eigh, eigvalsh, inv, cholesky, eigvals, eig
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Path setup
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVE_DIR = os.path.join(os.path.dirname(SCRIPT_DIR), 'computations/_shared')
sys.path.insert(0, SCRIPT_DIR)
sys.path.insert(0, ARCHIVE_DIR)

from canonical_constants import tau_fold

# Import the Gell-Mann matrices from the archive
from branching_computation import gell_mann_matrices

###############################################################################
# SECTION 1: SU(3) Lie algebra infrastructure (from dirac_spectrum.py)
###############################################################################

# Decomposition indices (Baptista eq 3.58)
# su(3) = u(1) + su(2) + C^2
U1_IDX = [7]            # u(1) generator: lambda_8
SU2_IDX = [0, 1, 2]    # su(2) generators: lambda_1, lambda_2, lambda_3
C2_IDX = [3, 4, 5, 6]  # C^2 generators: lambda_4, lambda_5, lambda_6, lambda_7


def su3_generators():
    """Anti-Hermitian generators e_a = -i/2 * lambda_a for a=0..7."""
    gm = gell_mann_matrices()
    return [-1j / 2.0 * lam for lam in gm]


def compute_structure_constants(gens):
    """f_{abc} from [e_a, e_b] = f_{abc} e_c."""
    n = len(gens)
    f = np.zeros((n, n, n), dtype=np.float64)
    for a in range(n):
        for b in range(a + 1, n):
            comm = gens[a] @ gens[b] - gens[b] @ gens[a]
            for c in range(n):
                val = -2.0 * np.trace(comm @ gens[c])  # (local)
                f[a, b, c] = val.real
                f[b, a, c] = -val.real
    return f


def jensen_metric(B_ab, s):
    """Jensen deformed metric g_s on su(3). Volume-preserving."""
    g0 = np.abs(B_ab)
    g = np.zeros((8, 8), dtype=np.float64)
    L1 = np.exp(2.0 * s)   # u(1)
    L2 = np.exp(-2.0 * s)  # su(2)
    L3 = np.exp(s)          # C^2
    for a in U1_IDX:
        for b in U1_IDX:
            g[a, b] = g0[a, b] * L1
    for a in SU2_IDX:
        for b in SU2_IDX:
            g[a, b] = g0[a, b] * L2
    for a in C2_IDX:
        for b in C2_IDX:
            g[a, b] = g0[a, b] * L3
    return g


def orthonormal_frame(g_s):
    """E = inv(chol(g_s)): e_a = E_{ab} X_b with g_s(e_a,e_b)=delta."""
    L = cholesky(g_s)
    return inv(L)


def frame_structure_constants(f_abc, E):
    """Structure constants in ON frame: ft^f_{ab} = E_{ac} E_{bd} f_{cde} (E^{-1})_{ef}."""
    E_inv = inv(E)
    return np.einsum('ac,bd,cde,ef->abf', E, E, f_abc, E_inv)


def connection_coefficients(ft):
    """Levi-Civita Gamma^c_{ab} in ON frame: 2*Gamma_{cab} = ft_{abc} - ft_{bca} + ft_{cab}."""
    n = ft.shape[0]
    Gamma = np.zeros((n, n, n), dtype=np.float64)
    for c in range(n):
        for a in range(n):
            for b in range(n):
                Gamma[c, a, b] = 0.5 * (ft[a, b, c] - ft[b, c, a] + ft[c, a, b])
    return Gamma


###############################################################################
# SECTION 2: Clifford algebra Cliff(R^8) -> C^16
###############################################################################

def build_cliff8():
    """gamma_1,...,gamma_8: Hermitian 16x16 with {gamma_a, gamma_b} = 2 delta_{ab} I."""
    s1 = np.array([[0, 1], [1, 0]], dtype=complex)
    s2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
    s3 = np.array([[1, 0], [0, -1]], dtype=complex)
    I2 = np.eye(2, dtype=complex)

    def kron4(A, B, C, D):
        return np.kron(A, np.kron(B, np.kron(C, D)))

    return [
        kron4(s1, I2, I2, I2),   # gamma_1
        kron4(s2, I2, I2, I2),   # gamma_2
        kron4(s3, s1, I2, I2),   # gamma_3
        kron4(s3, s2, I2, I2),   # gamma_4
        kron4(s3, s3, s1, I2),   # gamma_5
        kron4(s3, s3, s2, I2),   # gamma_6
        kron4(s3, s3, s3, s1),   # gamma_7
        kron4(s3, s3, s3, s2),   # gamma_8
    ]


###############################################################################
# SECTION 3: Omega and its subspace decomposition
###############################################################################

def spinor_connection_offset(Gamma, gammas):
    """Omega = (1/4) sum_{a,b,c} Gamma^b_{ac} gamma_a gamma_b gamma_c."""
    n = len(gammas)
    dim_spin = gammas[0].shape[0]
    Omega = np.zeros((dim_spin, dim_spin), dtype=complex)
    for a in range(n):
        for b in range(n):
            for c in range(n):
                coeff = Gamma[b, a, c]
                if abs(coeff) > 1e-15:
                    Omega += coeff * gammas[a] @ gammas[b] @ gammas[c]
    Omega *= 0.25
    return Omega


def spinor_connection_offset_partial(Gamma, gammas, a_indices):
    """
    Partial Omega restricted to a subset of the FIRST index a.

    Omega_I = (1/4) sum_{a in I} sum_{b,c} Gamma^b_{ac} gamma_a gamma_b gamma_c

    This decomposes Omega = Omega_{u(1)} + Omega_{su(2)} + Omega_{C^2}
    according to which direction the Dirac operator "sees" through index a.

    Note: Index a corresponds to the direction of differentiation in
    nabla^S_{e_a}. When we sum gamma_a nabla_{e_a}, the index a runs
    over all directions. Restricting to a subset gives the contribution
    from that subspace to the total Dirac operator.
    """
    n = len(gammas)
    dim_spin = gammas[0].shape[0]
    Omega_partial = np.zeros((dim_spin, dim_spin), dtype=complex)
    for a in a_indices:
        for b in range(n):
            for c in range(n):
                coeff = Gamma[b, a, c]
                if abs(coeff) > 1e-15:
                    Omega_partial += coeff * gammas[a] @ gammas[b] @ gammas[c]
    Omega_partial *= 0.25
    return Omega_partial


def build_Omega_at_tau(tau, gens, f_abc, gammas):
    """Build the full (0,0) singlet Dirac operator at given tau."""
    B_ab = np.einsum('acd,bcd->ab', f_abc, f_abc)
    g_s = jensen_metric(B_ab, tau)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Omega = spinor_connection_offset(Gamma, gammas)
    return Omega, Gamma


def build_Omega_decomposed(tau, gens, f_abc, gammas):
    """
    Build Omega and its three subspace components at given tau.

    Returns:
        Omega_total, Omega_u1, Omega_su2, Omega_c2, Gamma
    """
    B_ab = np.einsum('acd,bcd->ab', f_abc, f_abc)
    g_s = jensen_metric(B_ab, tau)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)

    Omega_total = spinor_connection_offset(Gamma, gammas)
    Omega_u1 = spinor_connection_offset_partial(Gamma, gammas, U1_IDX)
    Omega_su2 = spinor_connection_offset_partial(Gamma, gammas, SU2_IDX)
    Omega_c2 = spinor_connection_offset_partial(Gamma, gammas, C2_IDX)

    return Omega_total, Omega_u1, Omega_su2, Omega_c2, Gamma


###############################################################################
# SECTION 4: Eigenvalue analysis and B2 identification
###############################################################################

def identify_blocks(evals, tol=1e-6):
    """
    Identify B1, B2, B3 blocks from the 16 eigenvalues of the (0,0) singlet.

    At tau=0 (bi-invariant): all 16 eigenvalues degenerate (8 positive, 8 negative).
    At tau>0: positive sector splits into B3 (3-fold), B2 (4-fold), B1 (1-fold),
    ordered by increasing |eigenvalue|. Negative sector mirrors.

    Returns:
        dict with 'B3_pos', 'B2_pos', 'B1_pos' index arrays (into sorted eigenvalue array)
    """
    # Sort by real part (eigenvalues should be purely imaginary for anti-Hermitian Omega,
    # or real if we use i*Omega)
    idx_sorted = np.argsort(evals.real)
    sorted_evals = evals[idx_sorted]

    # Positive eigenvalues
    pos_mask = sorted_evals.real > 0
    pos_indices = np.where(pos_mask)[0]
    pos_vals = sorted_evals[pos_indices].real

    if len(pos_indices) != 8:
        print(f"WARNING: Expected 8 positive eigenvalues, got {len(pos_indices)}")
        return None

    # Cluster the 8 positive eigenvalues into groups
    # Sort positive eigenvalues by value
    pos_sort = np.argsort(pos_vals)
    pos_vals_sorted = pos_vals[pos_sort]

    # At tau>0, expect 3 groups: B3(3), B2(4), B1(1) by increasing eigenvalue
    # Use gap detection
    gaps = np.diff(pos_vals_sorted)

    # For debugging
    result = {
        'sorted_idx': idx_sorted,
        'pos_indices': pos_indices,
        'pos_vals_sorted': pos_vals_sorted,
        'pos_sort': pos_sort,
    }

    # Identify clusters
    if np.max(gaps) < tol:
        # All degenerate (tau ~ 0)
        result['degenerate'] = True
        result['B3_local'] = np.array([0, 1, 2])
        result['B2_local'] = np.array([3, 4, 5, 6])
        result['B1_local'] = np.array([7])
    else:
        result['degenerate'] = False
        # Find the two largest gaps
        gap_order = np.argsort(gaps)[::-1]
        gap1 = gap_order[0]
        gap2 = gap_order[1] if len(gap_order) > 1 else gap1

        splits = sorted([gap1 + 1, gap2 + 1])

        # Verify 3-4-1 splitting
        n1 = splits[0]
        n2 = splits[1] - splits[0]
        n3 = 8 - splits[1]

        if (n1, n2, n3) == (3, 4, 1):
            result['B3_local'] = np.arange(0, 3)
            result['B2_local'] = np.arange(3, 7)
            result['B1_local'] = np.array([7])
        elif (n1, n2, n3) == (1, 4, 3):
            # Reversed ordering
            result['B1_local'] = np.array([0])
            result['B2_local'] = np.arange(1, 5)
            result['B3_local'] = np.arange(5, 8)
        else:
            print(f"WARNING: Unexpected splitting {n1}-{n2}-{n3}")
            result['B3_local'] = np.arange(0, 3)
            result['B2_local'] = np.arange(3, 7)
            result['B1_local'] = np.array([7])

    return result


###############################################################################
# SECTION 5: Mass variation decomposition
###############################################################################

def compute_mass_variation_decomposition(tau_values, gens, f_abc, gammas, dtau=1e-5):
    """
    For each tau, compute:
      1. B2 eigenvalues and eigenvectors
      2. d(lambda^2)/dtau via finite difference
      3. Decomposition into u(1), su(2), C^2 contributions via perturbation theory

    The perturbation theory formula:
      d(lambda_k)/dtau = <psi_k| dOmega/dtau |psi_k>
      d(lambda_k^2)/dtau = 2*lambda_k * <psi_k| dOmega/dtau |psi_k>

    We decompose dOmega/dtau = dOmega_u1/dtau + dOmega_su2/dtau + dOmega_c2/dtau
    """
    results = []

    for tau in tau_values:
        print(f"\n=== tau = {tau:.4f} ===")

        # Build Omega and decomposed parts at tau
        Omega, Omega_u1, Omega_su2, Omega_c2, _ = build_Omega_decomposed(
            tau, gens, f_abc, gammas)

        # Build at tau + dtau and tau - dtau for finite difference
        Omega_p, Omega_u1_p, Omega_su2_p, Omega_c2_p, _ = build_Omega_decomposed(
            tau + dtau, gens, f_abc, gammas)
        Omega_m, Omega_u1_m, Omega_su2_m, Omega_c2_m, _ = build_Omega_decomposed(
            tau - dtau, gens, f_abc, gammas)

        # Numerical derivatives
        dOmega_dtau = (Omega_p - Omega_m) / (2 * dtau)
        dOmega_u1_dtau = (Omega_u1_p - Omega_u1_m) / (2 * dtau)
        dOmega_su2_dtau = (Omega_su2_p - Omega_su2_m) / (2 * dtau)
        dOmega_c2_dtau = (Omega_c2_p - Omega_c2_m) / (2 * dtau)

        # Verify decomposition of derivative
        dOmega_sum = dOmega_u1_dtau + dOmega_su2_dtau + dOmega_c2_dtau
        decomp_err = np.max(np.abs(dOmega_dtau - dOmega_sum))
        print(f"  dOmega decomposition error: {decomp_err:.2e}")

        # Diagonalize Omega
        # Omega may be anti-Hermitian or Hermitian depending on convention
        # Check:
        herm_err = np.max(np.abs(Omega - Omega.conj().T))
        aherm_err = np.max(np.abs(Omega + Omega.conj().T))

        if aherm_err < 1e-10:
            # Anti-Hermitian: eigenvalues are purely imaginary
            # Use i*Omega which is Hermitian
            H = 1j * Omega
            evals_H, evecs_H = eigh(H)  # Real eigenvalues, ON eigenvectors
            # Dirac eigenvalues are -i * evals_H (imaginary)
            # |eigenvalue|^2 = evals_H^2
            evals_abs = np.abs(evals_H)
            evals_signed = evals_H  # These are the real eigenvalues of i*Omega
            eigvecs = evecs_H
            is_antiherm = True

            # Also compute derivatives of i*Omega
            dH_dtau = 1j * dOmega_dtau
            dH_u1 = 1j * dOmega_u1_dtau
            dH_su2 = 1j * dOmega_su2_dtau
            dH_c2 = 1j * dOmega_c2_dtau
        else:
            # Hermitian (or general): use eigvals
            evals_raw = eigvals(Omega)
            idx_sort = np.argsort(evals_raw.real)
            evals_signed = evals_raw[idx_sort].real
            evals_abs = np.abs(evals_signed)

            # For Hermitian Omega, use eigh
            evals_signed, eigvecs = eigh(Omega.real + 0j)
            is_antiherm = False

            dH_dtau = dOmega_dtau
            dH_u1 = dOmega_u1_dtau
            dH_su2 = dOmega_su2_dtau
            dH_c2 = dOmega_c2_dtau

        print(f"  Anti-Hermitian: {is_antiherm} (herm_err={herm_err:.2e}, aherm_err={aherm_err:.2e})")
        print(f"  Eigenvalues (i*Omega): {np.sort(evals_signed)}")

        # Identify B2 modes
        blocks = identify_blocks(evals_signed)
        if blocks is None:
            print("  ERROR: Could not identify blocks")
            results.append(None)
            continue

        B2_local = blocks['B2_local']
        B3_local = blocks['B3_local']
        B1_local = blocks['B1_local']

        # Map local indices to global eigenvector indices
        # The positive eigenvalues are the upper 8 in sorted order
        pos_mask = evals_signed > 0
        pos_global_idx = np.where(pos_mask)[0]
        pos_vals = evals_signed[pos_global_idx]
        pos_sort = np.argsort(pos_vals)

        B2_global = pos_global_idx[pos_sort[B2_local]]
        B3_global = pos_global_idx[pos_sort[B3_local]]
        B1_global = pos_global_idx[pos_sort[B1_local]]

        B2_evals = evals_signed[B2_global]
        B3_evals = evals_signed[B3_global]
        B1_evals = evals_signed[B1_global]

        print(f"  B3 eigenvalues: {B3_evals}")
        print(f"  B2 eigenvalues: {B2_evals}")
        print(f"  B1 eigenvalues: {B1_evals}")

        # Compute perturbation theory expectation values for B2
        # d(lambda_k)/dtau = <psi_k| dH/dtau |psi_k>
        # d(lambda_k^2)/dtau = 2*lambda_k * d(lambda_k)/dtau

        dlam_total = np.zeros(4)
        dlam_u1 = np.zeros(4)
        dlam_su2 = np.zeros(4)
        dlam_c2 = np.zeros(4)

        # Also compute projection of eigenvectors onto subspace-associated spinor blocks
        # This is a separate question from the mass variation

        for i, gi in enumerate(B2_global):
            psi = eigvecs[:, gi]  # 16-component eigenvector

            # First-order perturbation theory
            dlam_total[i] = np.real(psi.conj() @ dH_dtau @ psi)
            dlam_u1[i] = np.real(psi.conj() @ dH_u1 @ psi)
            dlam_su2[i] = np.real(psi.conj() @ dH_su2 @ psi)
            dlam_c2[i] = np.real(psi.conj() @ dH_c2 @ psi)

        # Mass variation: d(m^2)/dtau = d(lambda^2)/dtau = 2*lambda*d(lambda)/dtau
        dm2_total = 2 * B2_evals * dlam_total
        dm2_u1 = 2 * B2_evals * dlam_u1
        dm2_su2 = 2 * B2_evals * dlam_su2
        dm2_c2 = 2 * B2_evals * dlam_c2

        # Average over B2 modes
        dm2_avg = np.mean(dm2_total)
        dm2_u1_avg = np.mean(dm2_u1)
        dm2_su2_avg = np.mean(dm2_su2)
        dm2_c2_avg = np.mean(dm2_c2)

        decomp_sum = dm2_u1_avg + dm2_su2_avg + dm2_c2_avg

        print(f"\n  d(m^2)/dtau decomposition (B2 average):")
        print(f"    u(1)  : {dm2_u1_avg:+.8f}  (metric e^{{+2tau}}, STRETCHING)")
        print(f"    su(2) : {dm2_su2_avg:+.8f}  (metric e^{{-2tau}}, SHRINKING)")
        print(f"    C^2   : {dm2_c2_avg:+.8f}  (metric e^{{+tau}},  STRETCHING)")
        print(f"    TOTAL : {dm2_avg:+.8f}")
        print(f"    SUM   : {decomp_sum:+.8f}  (should match total)")
        print(f"    Error : {abs(dm2_avg - decomp_sum):.2e}")

        # Sign determination
        stretch = dm2_u1_avg + dm2_c2_avg
        shrink = dm2_su2_avg
        print(f"\n  Stretching contribution (u1+C2): {stretch:+.8f}")
        print(f"  Shrinking contribution (su2):    {shrink:+.8f}")
        if dm2_avg > 0:
            print(f"  >>> MASS INCREASES: contraction tendency")
        elif dm2_avg < 0:
            print(f"  >>> MASS DECREASES: expansion tendency")
        else:
            print(f"  >>> MASS STATIONARY")

        # Also compute for B3 and B1 for comparison
        dlam_B3 = np.zeros(len(B3_global))
        dlam_B1 = np.zeros(len(B1_global))
        for i, gi in enumerate(B3_global):
            psi = eigvecs[:, gi]
            dlam_B3[i] = np.real(psi.conj() @ dH_dtau @ psi)
        for i, gi in enumerate(B1_global):
            psi = eigvecs[:, gi]
            dlam_B1[i] = np.real(psi.conj() @ dH_dtau @ psi)

        dm2_B3 = 2 * B3_evals * dlam_B3
        dm2_B1 = 2 * B1_evals * dlam_B1

        print(f"\n  Comparison - d(m^2)/dtau per mode:")
        print(f"    B3 (3 modes): {dm2_B3}")
        print(f"    B2 (4 modes): {dm2_total}")
        print(f"    B1 (1 mode) : {dm2_B1}")

        # Verify with finite difference of eigenvalues
        evals_p, _ = eigh(1j * Omega_p) if is_antiherm else eigh(Omega_p)
        evals_m, _ = eigh(1j * Omega_m) if is_antiherm else eigh(Omega_m)

        # Sort and pick positive B2 modes
        pos_p = np.sort(evals_p[evals_p > 0])
        pos_m = np.sort(evals_m[evals_m > 0])

        dm2_fd = (pos_p**2 - pos_m**2) / (2 * dtau)
        print(f"\n  Finite-difference d(m^2)/dtau (all positive modes):")
        print(f"    {dm2_fd}")
        print(f"    B2 modes (idx 3-6): {dm2_fd[3:7]}")
        print(f"    B2 FD average: {np.mean(dm2_fd[3:7]):+.8f}")

        res = {
            'tau': tau,
            'B2_evals': B2_evals,
            'B3_evals': B3_evals,
            'B1_evals': B1_evals,
            'dm2_total': dm2_total,
            'dm2_u1': dm2_u1,
            'dm2_su2': dm2_su2,
            'dm2_c2': dm2_c2,
            'dm2_avg': dm2_avg,
            'dm2_u1_avg': dm2_u1_avg,
            'dm2_su2_avg': dm2_su2_avg,
            'dm2_c2_avg': dm2_c2_avg,
            'dm2_B3': dm2_B3,
            'dm2_B1': dm2_B1,
            'dm2_fd_B2': np.mean(dm2_fd[3:7]),
            'decomp_err': decomp_err,
        }
        results.append(res)

    return results


###############################################################################
# SECTION 6: Alternative analytic approach via Casimir decomposition
###############################################################################

def analytic_casimir_projection(tau, gens, f_abc, gammas):
    """
    Analytic approach: The B2 sector has Casimir C_2 = 0.1557 (known from S34).
    Under the adjoint decomposition su(3) = u(1) + su(2) + C^2, the Casimir
    decomposes as C_2 = C_2^{u(1)} + C_2^{su(2)} + C_2^{C^2}.

    The spinor Casimir for each subspace is:
      C_2^I = sum_{a in I} (spin representation matrix of e_a)^2

    For the spin representation on C^16:
      sigma_a = (1/4) sum_{b<c} f_{abc} gamma_b gamma_c

    The spin Casimir restricted to subspace I:
      C_2^{spin,I} = sum_{a in I} sigma_a^2

    NOTE: This Casimir decomposition gives the STATIC structure (how much of the
    curvature comes from each subspace at a given tau), but the MASS VARIATION
    requires the tau-derivative, which depends on how the connection changes.
    """
    B_ab = np.einsum('acd,bcd->ab', f_abc, f_abc)
    g_s = jensen_metric(B_ab, tau)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)

    # Build spin representation matrices in ON frame
    # sigma_a = (1/4) sum_{b<c} ft^c_{ab} [gamma_b, gamma_c]
    # Actually: sigma_a = (1/4) sum_{b,c} ft_{abc} gamma_b gamma_c
    # With ft antisymmetric in (a,b) for ON frame, this is:
    # sigma_a = (1/2) sum_{b<c} ft[a,b,c] gamma_b gamma_c

    # But the correct spin representation is the GAUGE representation,
    # not the frame-rotated one. Let me use the structure constants directly.

    # The spin representation of su(3) is:
    # For generator e_a with ON frame structure constants ft:
    # sigma_a = (1/4) sum_{b<c} ft[b,c,a_lowered] gamma_b gamma_c
    # Wait, I need to be more careful.

    # The Lie algebra su(3) acts on spinors through the spin representation.
    # For the embedding spin(8) -> spin, the su(3) generators map to:
    # sigma(e_a) = (1/2) sum_{b<c} omega^{bc}(e_a) gamma_b gamma_c / 2
    # where omega^{bc}(e_a) = Gamma^b_{ac} (ON frame connection).

    # Actually, the spin lift of the LEFT action of SU(3) on itself is
    # given by the Kosmann lift. For left-invariant vector fields,
    # the spin rep generators are:
    # K_a = sum_{b<c} Gamma^b_{ac} (gamma_b gamma_c / 4)

    # But this is exactly the spinor connection restricted to direction a.
    # These are NOT the same as the Kosmann matrices -- the Kosmann matrices
    # are the FULL spinor Lie derivative, which includes the orbital part.

    # For the (0,0) singlet, there's no orbital part. So the relevant
    # object is just the spinor connection in each direction.

    Gamma = connection_coefficients(ft)

    # Spinor connection in direction a: omega^spin_a = (1/4) sum_{b,c} Gamma^b_{ac} gamma_b gamma_c
    omega_spin = []
    for a in range(8):
        om = np.zeros((16, 16), dtype=complex)
        for b in range(8):
            for c in range(8):
                coeff = Gamma[b, a, c]
                if abs(coeff) > 1e-15:
                    om += coeff * gammas[b] @ gammas[c]
        om *= 0.25
        omega_spin.append(om)

    # Now Omega = sum_a gamma_a @ omega_spin_a
    # The "Casimir" in each subspace:
    # P_I = sum_{a in I} omega_spin_a^dag @ omega_spin_a
    # (this is the squared norm of the spinor connection in subspace I)

    # But actually, what matters for B2 is the EIGENVECTOR projection.
    # Let me compute the B2 eigenvectors and then project onto the
    # subspace-specific connection.

    # Actually, the most direct and meaningful quantity is what we already
    # computed above: the perturbation theory decomposition.
    # The Casimir approach gives a different (complementary) quantity.

    # Let me compute the static "weight" of each subspace in the B2 modes:
    # w_I(k) = sum_{a in I} |<psi_k| gamma_a omega_spin_a |psi_k>|  /  |lambda_k|

    Omega_total = sum(gammas[a] @ omega_spin[a] for a in range(8))

    # Check it matches
    Omega_check, _ = build_Omega_at_tau(tau, gens, f_abc, gammas)
    match_err = np.max(np.abs(Omega_total - Omega_check))
    print(f"  Omega reconstruction error: {match_err:.2e}")

    # Get eigenvectors
    H = 1j * Omega_total
    evals_H, evecs_H = eigh(H)

    blocks = identify_blocks(evals_H)
    B2_local = blocks['B2_local']
    pos_mask = evals_H > 0
    pos_global_idx = np.where(pos_mask)[0]
    pos_vals = evals_H[pos_global_idx]
    pos_sort = np.argsort(pos_vals)
    B2_global = pos_global_idx[pos_sort[B2_local]]

    # For each B2 mode, compute the subspace weight
    print(f"\n  Static subspace weights for B2 (tau={tau:.4f}):")
    print(f"  {'Mode':>6} | {'lambda':>10} | {'w_u1':>10} | {'w_su2':>10} | {'w_c2':>10} | {'sum':>10}")

    weights = []
    for i, gi in enumerate(B2_global):
        psi = evecs_H[:, gi]
        lam = evals_H[gi]

        # Contribution from each subspace to the eigenvalue
        w_u1 = sum(np.real(psi.conj() @ (gammas[a] @ omega_spin[a]) @ psi)
                    for a in U1_IDX)
        w_su2 = sum(np.real(psi.conj() @ (gammas[a] @ omega_spin[a]) @ psi)
                     for a in SU2_IDX)
        w_c2 = sum(np.real(psi.conj() @ (gammas[a] @ omega_spin[a]) @ psi)
                    for a in C2_IDX)

        # These should sum to the eigenvalue of Omega (not i*Omega)
        # For anti-Hermitian Omega: eigenvalue of Omega = -i * lambda
        # So w_u1 + w_su2 + w_c2 should give eigenvalue of Omega = -i*lambda
        w_sum = w_u1 + w_su2 + w_c2

        # Actually, <psi|Omega|psi> for eigenvector of i*Omega with eigenvalue lambda
        # gives <psi|(-i*lambda)|psi> = -i*lambda (since Omega = -i*diag(lambda) in eigenbasis)
        # But w_I are real parts... let me be more careful

        # <psi|Omega|psi> is purely imaginary (Omega anti-Hermitian)
        omega_ev = psi.conj() @ Omega_total @ psi

        # So I should use imaginary parts
        w_u1_im = sum(np.imag(psi.conj() @ (gammas[a] @ omega_spin[a]) @ psi)
                       for a in U1_IDX)
        w_su2_im = sum(np.imag(psi.conj() @ (gammas[a] @ omega_spin[a]) @ psi)
                        for a in SU2_IDX)
        w_c2_im = sum(np.imag(psi.conj() @ (gammas[a] @ omega_spin[a]) @ psi)
                       for a in C2_IDX)

        total_im = w_u1_im + w_su2_im + w_c2_im

        # Normalize by total
        if abs(total_im) > 1e-15:
            r_u1 = w_u1_im / total_im
            r_su2 = w_su2_im / total_im
            r_c2 = w_c2_im / total_im
        else:
            r_u1 = r_su2 = r_c2 = 0.0

        print(f"  {i:6d} | {lam:10.6f} | {r_u1:10.6f} | {r_su2:10.6f} | {r_c2:10.6f} | {r_u1+r_su2+r_c2:10.6f}")

        weights.append({
            'lambda': lam,
            'r_u1': r_u1,
            'r_su2': r_su2,
            'r_c2': r_c2,
            'w_u1_im': w_u1_im,
            'w_su2_im': w_su2_im,
            'w_c2_im': w_c2_im,
        })

    return weights


###############################################################################
# SECTION 7: Main computation
###############################################################################

def main():
    t0 = time.time()
    print("=" * 72)
    print("S54 B2-ANGULAR-54: B2 Wavefunction Angular Decomposition")
    print("=" * 72)

    # Initialize algebra
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    gammas = build_cliff8()

    # Verify Clifford algebra
    cliff_err = 0.0  # (local)
    for a in range(8):
        for b in range(8):
            ac = gammas[a] @ gammas[b] + gammas[b] @ gammas[a]
            target = 2.0 * (1 if a == b else 0) * np.eye(16)
            cliff_err = max(cliff_err, np.max(np.abs(ac - target)))
    print(f"\nClifford algebra verification: max error = {cliff_err:.2e}")

    # Tau values: focus on the transit range with fine spacing near fold
    tau_values = np.array([0.0, 0.05, 0.10, 0.15, 0.19, 0.25, 0.30, 0.40, 0.50])

    print(f"\nComputing mass variation decomposition at {len(tau_values)} tau points...")

    # ====================================================================
    # PART A: Numerical mass variation via perturbation theory
    # ====================================================================
    print("\n" + "=" * 72)
    print("PART A: Perturbation theory mass variation decomposition")
    print("=" * 72)

    results = compute_mass_variation_decomposition(
        tau_values, gens, f_abc, gammas, dtau=1e-5)

    # ====================================================================
    # PART B: Static subspace weights (Casimir projection)
    # ====================================================================
    print("\n" + "=" * 72)
    print("PART B: Static subspace weights at key tau values")
    print("=" * 72)

    key_taus = [0.0, 0.10, 0.19, 0.30, 0.50]
    weight_results = {}
    for tau in key_taus:
        print(f"\n--- tau = {tau:.2f} ---")
        weights = analytic_casimir_projection(tau, gens, f_abc, gammas)
        weight_results[tau] = weights

    # ====================================================================
    # PART C: Summary table
    # ====================================================================
    print("\n" + "=" * 72)
    print("SUMMARY TABLE: B2 Mass Variation Sign")
    print("=" * 72)

    print(f"\n{'tau':>6} | {'dm2/dtau':>12} | {'u(1)':>12} | {'su(2)':>12} | {'C^2':>12} | {'FD check':>12} | {'sign':>10}")
    print("-" * 90)

    for r in results:
        if r is None:
            continue
        sign_str = "INCREASE" if r['dm2_avg'] > 0 else ("DECREASE" if r['dm2_avg'] < 0 else "ZERO")
        print(f"{r['tau']:6.3f} | {r['dm2_avg']:+12.6f} | {r['dm2_u1_avg']:+12.6f} | "
              f"{r['dm2_su2_avg']:+12.6f} | {r['dm2_c2_avg']:+12.6f} | "
              f"{r['dm2_fd_B2']:+12.6f} | {sign_str:>10}")

    # ====================================================================
    # PART D: Sign at the fold
    # ====================================================================
    fold_result = None
    for r in results:
        if r is not None and abs(r['tau'] - tau_fold) < 0.01:
            fold_result = r
            break

    print(f"\n{'=' * 72}")
    print(f"DECISIVE RESULT: Mass variation at fold (tau = {tau_fold})")
    print(f"{'=' * 72}")

    if fold_result is not None:
        print(f"\n  d(m^2_B2)/dtau = {fold_result['dm2_avg']:+.8f}")
        print(f"")
        print(f"  Decomposition:")
        print(f"    u(1)  [+2tau] : {fold_result['dm2_u1_avg']:+.8f}  (hypercharge, STRETCHING)")
        print(f"    su(2) [-2tau] : {fold_result['dm2_su2_avg']:+.8f}  (isospin, SHRINKING)")
        print(f"    C^2   [+tau ] : {fold_result['dm2_c2_avg']:+.8f}  (coset, STRETCHING)")
        print(f"")

        if fold_result['dm2_avg'] > 0:
            verdict = "MASS INCREASES -> CONTRACTION tendency"
        elif fold_result['dm2_avg'] < 0:
            verdict = "MASS DECREASES -> EXPANSION tendency"
        else:
            verdict = "MASS STATIONARY -> NEUTRAL"

        print(f"  VERDICT: {verdict}")

        # Ratio of stretching to shrinking
        stretch_total = fold_result['dm2_u1_avg'] + fold_result['dm2_c2_avg']
        shrink_total = fold_result['dm2_su2_avg']
        if abs(shrink_total) > 1e-15:
            ratio = abs(stretch_total / shrink_total)
            print(f"  |Stretch/Shrink| = {ratio:.4f}")

        # Finite difference cross-check
        print(f"\n  Cross-check: FD d(m^2)/dtau = {fold_result['dm2_fd_B2']:+.8f}")
        print(f"  Perturbation theory:          {fold_result['dm2_avg']:+.8f}")
        if abs(fold_result['dm2_fd_B2']) > 1e-10:
            rel_err = abs(fold_result['dm2_avg'] - fold_result['dm2_fd_B2']) / abs(fold_result['dm2_fd_B2'])
            print(f"  Relative error: {rel_err:.2e}")

    # ====================================================================
    # PART E: All-sector comparison
    # ====================================================================
    print(f"\n{'=' * 72}")
    print("ALL SECTOR COMPARISON: d(m^2)/dtau at fold")
    print(f"{'=' * 72}")

    if fold_result is not None:
        print(f"\n  B3 (3 modes): {fold_result['dm2_B3']}")
        print(f"  B3 average:   {np.mean(fold_result['dm2_B3']):+.8f}")
        print(f"  B2 (4 modes): {fold_result['dm2_total']}")
        print(f"  B2 average:   {np.mean(fold_result['dm2_total']):+.8f}")
        print(f"  B1 (1 mode):  {fold_result['dm2_B1']}")
        print(f"  B1 value:     {fold_result['dm2_B1'][0]:+.8f}")

        # Net over all 8 positive modes
        all_dm2 = np.concatenate([fold_result['dm2_B3'], fold_result['dm2_total'], fold_result['dm2_B1']])
        print(f"\n  All positive modes average: {np.mean(all_dm2):+.8f}")
        print(f"  All positive modes sum:     {np.sum(all_dm2):+.8f}")

    # ====================================================================
    # PART F: Plot
    # ====================================================================
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    taus = [r['tau'] for r in results if r is not None]
    dm2_avgs = [r['dm2_avg'] for r in results if r is not None]
    dm2_u1s = [r['dm2_u1_avg'] for r in results if r is not None]
    dm2_su2s = [r['dm2_su2_avg'] for r in results if r is not None]
    dm2_c2s = [r['dm2_c2_avg'] for r in results if r is not None]
    dm2_fds = [r['dm2_fd_B2'] for r in results if r is not None]

    # Plot 1: Total mass variation
    ax = axes[0, 0]
    ax.plot(taus, dm2_avgs, 'ko-', linewidth=2, markersize=6, label='Perturbation theory')
    ax.plot(taus, dm2_fds, 'r^--', linewidth=1.5, markersize=5, label='Finite difference')
    ax.axhline(y=0, color='gray', linestyle=':', linewidth=0.5)
    ax.axvline(x=tau_fold, color='blue', linestyle='--', alpha=0.5, label=f'tau_fold={tau_fold}')
    ax.set_xlabel('tau')
    ax.set_ylabel('d(m^2_B2)/dtau')
    ax.set_title('B2 Mass Variation vs tau')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Plot 2: Subspace decomposition
    ax = axes[0, 1]
    ax.plot(taus, dm2_u1s, 's-', color='red', linewidth=1.5, markersize=5, label='u(1) [e^{+2tau}]')
    ax.plot(taus, dm2_su2s, 'D-', color='blue', linewidth=1.5, markersize=5, label='su(2) [e^{-2tau}]')
    ax.plot(taus, dm2_c2s, 'o-', color='green', linewidth=1.5, markersize=5, label='C^2 [e^{+tau}]')
    ax.plot(taus, dm2_avgs, 'k--', linewidth=1, alpha=0.5, label='Total')
    ax.axhline(y=0, color='gray', linestyle=':', linewidth=0.5)
    ax.axvline(x=tau_fold, color='blue', linestyle='--', alpha=0.5)
    ax.set_xlabel('tau')
    ax.set_ylabel('d(m^2_B2)/dtau contribution')
    ax.set_title('Subspace Decomposition of Mass Variation')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Plot 3: All sectors comparison
    ax = axes[1, 0]
    dm2_B3_avgs = [np.mean(r['dm2_B3']) for r in results if r is not None]
    dm2_B1_vals = [r['dm2_B1'][0] for r in results if r is not None]
    ax.plot(taus, dm2_B3_avgs, 'v-', color='purple', linewidth=1.5, markersize=5, label='B3 (3 modes)')
    ax.plot(taus, dm2_avgs, 'o-', color='green', linewidth=1.5, markersize=5, label='B2 (4 modes)')
    ax.plot(taus, dm2_B1_vals, 's-', color='orange', linewidth=1.5, markersize=5, label='B1 (1 mode)')
    ax.axhline(y=0, color='gray', linestyle=':', linewidth=0.5)
    ax.axvline(x=tau_fold, color='blue', linestyle='--', alpha=0.5)
    ax.set_xlabel('tau')
    ax.set_ylabel('d(m^2)/dtau')
    ax.set_title('Mass Variation by Sector')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Plot 4: B2 eigenvalues vs tau
    ax = axes[1, 1]
    for r in results:
        if r is not None:
            ax.plot([r['tau']] * 3, r['B3_evals'], 'v', color='purple', markersize=4)
            ax.plot([r['tau']] * 4, r['B2_evals'], 'o', color='green', markersize=4)
            ax.plot([r['tau']] * 1, r['B1_evals'], 's', color='orange', markersize=4)
    ax.set_xlabel('tau')
    ax.set_ylabel('Eigenvalue (i*Omega)')
    ax.set_title('Singlet Spectrum vs tau')
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plot_path = os.path.join(SCRIPT_DIR, 's54_b2_angular.png')
    plt.savefig(plot_path, dpi=150)
    print(f"\nPlot saved to: {plot_path}")

    # ====================================================================
    # PART G: Save data
    # ====================================================================
    save_data = {
        'tau_values': np.array(taus),
        'dm2_B2_avg': np.array(dm2_avgs),
        'dm2_u1_avg': np.array(dm2_u1s),
        'dm2_su2_avg': np.array(dm2_su2s),
        'dm2_c2_avg': np.array(dm2_c2s),
        'dm2_fd_B2': np.array(dm2_fds),
        'tau_fold': tau_fold,
    }

    for i, r in enumerate(results):
        if r is not None:
            save_data[f'B2_evals_{i}'] = r['B2_evals']
            save_data[f'B3_evals_{i}'] = r['B3_evals']
            save_data[f'B1_evals_{i}'] = r['B1_evals']
            save_data[f'dm2_B2_{i}'] = r['dm2_total']
            save_data[f'dm2_B3_{i}'] = r['dm2_B3']
            save_data[f'dm2_B1_{i}'] = r['dm2_B1']

    npz_path = os.path.join(SCRIPT_DIR, 's54_b2_angular.npz')
    np.savez(npz_path, **save_data)
    print(f"Data saved to: {npz_path}")

    elapsed = time.time() - t0
    print(f"\nTotal runtime: {elapsed:.1f}s")

    return results, weight_results


if __name__ == '__main__':
    results, weights = main()
