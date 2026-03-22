#!/usr/bin/env python3
"""
s32c_topo_t2_scan.py — TOPO-T2: B2-B3 Gap Along T2 Direction
=============================================================

Session 32c: Scan the B2-B3 eigenvalue gap along the T2 direction
(maximum U(2) symmetry-breaking) at fixed tau = 0.18.

T2 parametrization (from Session 29Bb, s30b_grid_bcs.py):
  log L1 = 2*tau - 11*eps/N_T2
  log L2 = -2*tau - 7*eps/N_T2
  log L3 = tau + 8*eps/N_T2
  N_T2 = sqrt(234) ~ 15.297

At each (tau=0.18, eps):
  1. Construct U(2)-invariant metric with scale factors (L1, L2, L3)
  2. Compute spinor connection offset Omega (16x16 matrix)
  3. Diagonalize Omega for (0,0) singlet eigenvalues
  4. Track the 8 near-degenerate modes by continuity from eps=0
  5. Compute Delta_gap(eps) = min(B3) - max(B2)

Branch classification at eps=0 from s32a_umklapp_vertex.npz:
  B1: 1 mode (trivial rep of U(2))
  B2: 4 modes (U(2) fundamental, flat band)
  B3: 3 modes (SU(2) adjoint, optical)

Gate TT-32c: PASS if gap closes (Delta_gap = 0) at some epsilon.
             OPEN if gap minimum < 0.1 but does not close.
             FAIL if gap minimum > 0.2 along entire T2 scan.

If gap closes: compute BDI Z invariant (Pfaffian sign) on both sides.

Author: baptista (baptista-spacetime-analyst), Session 32c
Date: 2026-03-03
"""

import numpy as np
from numpy.linalg import eigvalsh, inv, cholesky
import sys
import os
import time

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from tier1_dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    u2_invariant_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients, spinor_connection_offset, build_cliff8,
    build_chirality
)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from pathlib import Path

# ─── Configuration ──────────────────────────────────────────────────────
DATA_DIR = Path(SCRIPT_DIR)
OUT_NPZ = DATA_DIR / 's32c_topo_t2_scan.npz'
OUT_PNG = DATA_DIR / 's32c_topo_t2_scan.png'

# T2 direction normalization (from s30b_grid_bcs.py)
T2_DIR = np.array([-11.0, -7.0, 8.0])
N_T2 = np.sqrt(np.dot(T2_DIR, T2_DIR))  # sqrt(234) ~ 15.297

# Fixed tau, scanning eps
TAU_FIXED = 0.18
N_EPS = 41  # 41 points for higher resolution along T2
EPS_MIN, EPS_MAX = -0.15, 0.15

# For Z invariant computation (if gap closure found)
DO_Z_INVARIANT = True


# ==========================================================================
# MODULE 1: Parametrization
# ==========================================================================

def tau_eps_to_lambdas(tau, eps):
    """Convert (tau, eps) to (L1, L2, L3) on volume-preserving surface.

    Parametrization:
      log L1 = 2*tau - 11*eps/N_T2
      log L2 = -2*tau - 7*eps/N_T2
      log L3 = tau + 8*eps/N_T2

    Volume-preserving: L1^1 * L2^3 * L3^4 = 1 on the Jensen curve (eps=0).
    Off-Jensen (eps != 0): 1*(-11/N) + 3*(-7/N) + 4*(8/N) = (-11-21+32)/N = 0.
    So volume is preserved for all eps. Good.
    """
    L1 = np.exp(2.0 * tau - 11.0 * eps / N_T2)
    L2 = np.exp(-2.0 * tau - 7.0 * eps / N_T2)
    L3 = np.exp(tau + 8.0 * eps / N_T2)
    return L1, L2, L3


# ==========================================================================
# MODULE 2: Singlet eigenvalue computation
# ==========================================================================

def compute_singlet_eigenvalues(B_ab, f_abc, gammas, L1, L2, L3):
    """
    Compute (0,0) singlet eigenvalues of the Dirac operator on SU(3)
    at a U(2)-invariant metric with scale factors (L1, L2, L3).

    For the trivial irrep (0,0), rho(e_a) = 0. The Dirac operator reduces to
    D_{(0,0)} = Omega (the spinor connection offset), which is a 16x16 matrix.

    Returns sorted positive eigenvalues (8 values, using spectral pairing
    to discard negative half).
    """
    g = u2_invariant_metric(B_ab, L1, L2, L3)
    E = orthonormal_frame(g)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Omega = spinor_connection_offset(Gamma, gammas)

    # Eigenvalues of Omega (anti-Hermitian => purely imaginary eigenvalues)
    # The Dirac eigenvalues are the imaginary parts (math convention)
    evals = np.linalg.eigvals(Omega)
    # Eigenvalues come in +/- pairs (spectral pairing)
    # Sort by imaginary part and take the positive half
    imag_evals = np.sort(evals.imag)
    # Last 8 are the positive ones
    pos_evals = imag_evals[8:]  # sorted ascending
    return pos_evals, Omega


# ==========================================================================
# MODULE 3: Branch tracking by continuity
# ==========================================================================

def classify_branches_at_jensen(pos_evals_ref, tau, B_ab, f_abc, gammas):
    """
    Classify the 8 singlet modes into B1(1), B2(4), B3(3) at the Jensen
    point (eps=0) using eigenvalue derivative magnitudes.

    Uses finite-difference derivative from stored data or inline computation.
    """
    # Compute at tau and tau+delta for derivative
    delta = 0.005
    L1_m, L2_m, L3_m = tau_eps_to_lambdas(tau - delta, 0.0)
    L1_p, L2_p, L3_p = tau_eps_to_lambdas(tau + delta, 0.0)

    ev_m, _ = compute_singlet_eigenvalues(B_ab, f_abc, gammas, L1_m, L2_m, L3_m)
    ev_p, _ = compute_singlet_eigenvalues(B_ab, f_abc, gammas, L1_p, L2_p, L3_p)

    # Derivative by centered finite difference
    deriv = (ev_p - ev_m) / (2 * delta)
    abs_deriv = np.abs(deriv)

    # B3 = 3 modes with largest |deriv|
    # B2 = 4 modes with smallest |deriv|
    # B1 = 1 remaining mode (intermediate)
    sorted_idx = np.argsort(abs_deriv)

    # sorted_idx[0:4] = smallest derivatives = B2
    # sorted_idx[4] = intermediate = B1
    # sorted_idx[5:8] = largest derivatives = B3
    branch_labels = np.empty(8, dtype='U2')
    branch_labels[sorted_idx[0:4]] = 'B2'
    branch_labels[sorted_idx[4]] = 'B1'
    branch_labels[sorted_idx[5:8]] = 'B3'

    return branch_labels, deriv


def track_branches(all_evals, eps_arr, branch_labels_ref):
    """
    Track branch assignment across all eps values by eigenvalue continuity.

    At each eps step, match eigenvalues to the previous step's assignment
    by minimizing total distance (greedy nearest-neighbor tracking).

    Parameters
    ----------
    all_evals : (N_eps, 8) array
        Positive singlet eigenvalues at each eps, sorted ascending.
    eps_arr : (N_eps,) array
        Epsilon values.
    branch_labels_ref : (8,) string array
        Branch labels at the reference point (eps=0).

    Returns
    -------
    tracked_evals : (N_eps, 8) array
        Eigenvalues reordered so each column tracks a single mode.
    tracked_labels : (8,) string array
        Branch labels (same as ref, modes tracked by continuity).
    """
    N = len(eps_arr)

    # Find the reference index (eps closest to 0)
    ref_idx = np.argmin(np.abs(eps_arr))

    # Initialize tracked arrays
    tracked_evals = np.zeros_like(all_evals)
    tracked_evals[ref_idx] = all_evals[ref_idx]

    # Track forward from ref_idx
    for i in range(ref_idx + 1, N):
        prev = tracked_evals[i - 1]
        curr = all_evals[i]
        # Greedy matching by closest eigenvalue
        used = set()
        order = np.argsort(np.abs(prev - np.mean(prev)))  # start from extremes
        assignment = np.zeros(8, dtype=int)
        for k in range(8):
            # For mode k, find closest unmatched eigenvalue in curr
            dists = np.abs(curr - prev[k])
            sorted_j = np.argsort(dists)
            for j in sorted_j:
                if j not in used:
                    assignment[k] = j
                    used.add(j)
                    break
        tracked_evals[i] = curr[assignment]

    # Track backward from ref_idx
    for i in range(ref_idx - 1, -1, -1):
        prev = tracked_evals[i + 1]
        curr = all_evals[i]
        used = set()
        assignment = np.zeros(8, dtype=int)
        for k in range(8):
            dists = np.abs(curr - prev[k])
            sorted_j = np.argsort(dists)
            for j in sorted_j:
                if j not in used:
                    assignment[k] = j
                    used.add(j)
                    break
        tracked_evals[i] = curr[assignment]

    return tracked_evals, branch_labels_ref


# ==========================================================================
# MODULE 4: Gap computation
# ==========================================================================

def compute_b2_b3_gap(tracked_evals, branch_labels):
    """
    Compute Delta_gap(eps) = min(B3 eigenvalues) - max(B2 eigenvalues)
    at each eps value.

    Returns
    -------
    gap : (N_eps,) array
        B2-B3 gap at each eps. Positive = gap open. Zero/negative = gap closed.
    b2_max : (N_eps,) array
        Maximum B2 eigenvalue at each eps.
    b3_min : (N_eps,) array
        Minimum B3 eigenvalue at each eps.
    """
    b2_mask = branch_labels == 'B2'
    b3_mask = branch_labels == 'B3'

    b2_evals = tracked_evals[:, b2_mask]  # (N_eps, 4)
    b3_evals = tracked_evals[:, b3_mask]  # (N_eps, 3)

    b2_max = np.max(b2_evals, axis=1)
    b3_min = np.min(b3_evals, axis=1)

    gap = b3_min - b2_max
    return gap, b2_max, b3_min


# ==========================================================================
# MODULE 5: BDI Z invariant (Pfaffian of Q = C * gamma_5 * D_K)
# ==========================================================================

def compute_pfaffian_sign(M):
    """
    Compute the sign of the Pfaffian of an antisymmetric matrix M via
    the Parlett-Reid LTL^T factorization.

    For the BDI topological invariant, the Z index is:
      Z = sgn Pf(Q) where Q = C * gamma_5 * M_D
    and C is the charge conjugation operator, gamma_5 the chirality.

    We use the simple formula: Pf(M) = (-1)^{n(n-1)/2} * product of
    upper-off-diagonal elements in the Pfaffian normal form.
    For practical purposes, we use det(M) = Pf(M)^2, so
    sgn(Pf) = +1 or -1 (determined by continuity from a reference).

    For small matrices (16x16), we use the LTL^T decomposition.
    """
    n = M.shape[0]
    if n % 2 != 0:
        return 0.0  # Odd-dimensional, Pf = 0

    # Ensure antisymmetric
    M_anti = 0.5 * (M - M.T)
    max_sym = np.max(np.abs(M + M.T))

    # Parlett-Reid LTL^T factorization
    # Simple implementation for 16x16
    A = M_anti.copy().astype(np.float64)
    nn = n // 2
    sign = 1.0

    for k in range(nn):
        # Find pivot: largest |A[2k, j]| for j > 2k
        pivot_idx = 2 * k + 1 + np.argmax(np.abs(A[2*k, 2*k+1:]))
        if pivot_idx != 2 * k + 1:
            # Swap rows and columns
            A[[2*k+1, pivot_idx], :] = A[[pivot_idx, 2*k+1], :]
            A[:, [2*k+1, pivot_idx]] = A[:, [pivot_idx, 2*k+1]]
            sign *= -1.0

        pivot = A[2*k, 2*k+1]
        if abs(pivot) < 1e-15:
            return 0.0  # Degenerate

        sign *= np.sign(pivot)

        # Eliminate below
        for i in range(2*k+2, n):
            for j in range(2*k+2, n):
                A[i, j] -= (A[i, 2*k] * A[2*k+1, j] - A[i, 2*k+1] * A[2*k, j]) / pivot

    return sign


def compute_bdi_z_invariant(Omega, gammas):
    """
    Compute the BDI Z invariant for the singlet Dirac operator.

    For the (0,0) singlet, D = Omega. The Z invariant is:
      Z = sgn Pf(C * Gamma_9 * D)
    where C is charge conjugation (real structure J with J^2 = +1)
    and Gamma_9 is the chirality.

    In our convention:
      C = product of "real" gamma matrices (gamma_1, gamma_3, gamma_5, gamma_7)
      acting as complex conjugation + matrix.

    For KO-dim 6 with J^2 = +1: C * conj(Omega) * C^{-1} = Omega.
    The matrix M = C * Gamma_9 * Omega should be antisymmetric.
    """
    gamma9 = build_chirality(gammas)

    # Real structure for KO-dim 6: J = C * K (complex conjugation)
    # C = gamma_1 * gamma_3 * gamma_5 * gamma_7 (product of odd-indexed gammas)
    C = gammas[0] @ gammas[2] @ gammas[4] @ gammas[6]

    # Q = C * gamma_9 * Omega
    Q = C @ gamma9 @ Omega

    # Q should be antisymmetric for the Pfaffian to be defined
    Q_real = Q.real
    antisym_err = np.max(np.abs(Q_real + Q_real.T))
    Q_anti = 0.5 * (Q_real - Q_real.T)

    pf_sign = compute_pfaffian_sign(Q_anti)
    return pf_sign, antisym_err


# ==========================================================================
# MODULE 6: Cross-check with stored Jensen data
# ==========================================================================

def cross_check_jensen(B_ab, f_abc, gammas, tau):
    """
    Cross-check: compute singlet eigenvalues at (tau, eps=0) and compare
    with stored data from s32a_umklapp_vertex.npz.
    """
    L1, L2, L3 = tau_eps_to_lambdas(tau, 0.0)
    pos_evals, _ = compute_singlet_eigenvalues(B_ab, f_abc, gammas, L1, L2, L3)

    # Load reference from s32a
    ref_file = DATA_DIR / 's32a_umklapp_vertex.npz'
    if ref_file.exists():
        ref = np.load(ref_file)
        tau_vals = ref['tau_values']
        # Find closest tau
        idx = np.argmin(np.abs(tau_vals - tau))
        ref_evals = ref['pos_evals'][idx]
        if len(ref_evals) == 8:
            max_diff = np.max(np.abs(np.sort(pos_evals) - np.sort(ref_evals)))
            return max_diff, ref_evals
    return None, None


# ==========================================================================
# MODULE 7: Main computation
# ==========================================================================

def main():
    t_start = time.time()
    print("=" * 70)
    print("Session 32c: TOPO-T2 — B2-B3 Gap Along T2 Direction")
    print(f"  Fixed tau = {TAU_FIXED}")
    print(f"  Epsilon range: [{EPS_MIN}, {EPS_MAX}], {N_EPS} points")
    print(f"  T2 direction: {T2_DIR}, ||T2|| = {N_T2:.3f}")
    print("=" * 70)

    # ── Setup ──
    print("\n[SETUP] Building algebra infrastructure...")
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    B_ab = compute_killing_form(f_abc)
    gammas = build_cliff8()

    # ── Cross-check with Jensen reference ──
    print("\n[CHECK] Cross-checking with s32a reference at Jensen point...")
    xc_diff, xc_ref = cross_check_jensen(B_ab, f_abc, gammas, TAU_FIXED)
    if xc_diff is not None:
        print(f"  Max eigenvalue difference from s32a reference: {xc_diff:.2e}")
        if xc_diff > 1e-10:
            print("  WARNING: Large discrepancy with stored data!")
    else:
        print("  Reference file not found; skipping cross-check.")

    # ── Branch classification at Jensen ──
    print("\n[CLASSIFY] Classifying branches at Jensen point (eps=0)...")
    L1_ref, L2_ref, L3_ref = tau_eps_to_lambdas(TAU_FIXED, 0.0)
    ref_evals, _ = compute_singlet_eigenvalues(B_ab, f_abc, gammas, L1_ref, L2_ref, L3_ref)
    branch_labels, deriv_ref = classify_branches_at_jensen(
        ref_evals, TAU_FIXED, B_ab, f_abc, gammas)

    print(f"  Reference eigenvalues (eps=0): {ref_evals}")
    print(f"  Branch labels: {branch_labels}")
    print(f"  Derivatives (dlambda/dtau): {deriv_ref}")
    b1_mask = branch_labels == 'B1'
    b2_mask = branch_labels == 'B2'
    b3_mask = branch_labels == 'B3'
    print(f"  B1 evals: {ref_evals[b1_mask]}")
    print(f"  B2 evals: {ref_evals[b2_mask]} (4-fold: spread = {np.ptp(ref_evals[b2_mask]):.2e})")
    print(f"  B3 evals: {ref_evals[b3_mask]} (3-fold: spread = {np.ptp(ref_evals[b3_mask]):.2e})")
    print(f"  B2-B3 gap at eps=0: {np.min(ref_evals[b3_mask]) - np.max(ref_evals[b2_mask]):.6f}")

    # ── T2 scan ──
    eps_arr = np.linspace(EPS_MIN, EPS_MAX, N_EPS)
    all_evals = np.zeros((N_EPS, 8))
    all_omega = []  # Store Omega matrices for Z invariant
    all_L = np.zeros((N_EPS, 3))

    print(f"\n[SCAN] Computing singlet eigenvalues at {N_EPS} epsilon values...")
    for i, eps in enumerate(eps_arr):
        L1, L2, L3 = tau_eps_to_lambdas(TAU_FIXED, eps)
        all_L[i] = [L1, L2, L3]
        pos_evals, Omega = compute_singlet_eigenvalues(
            B_ab, f_abc, gammas, L1, L2, L3)
        all_evals[i] = pos_evals
        all_omega.append(Omega)

        if i % 10 == 0 or i == N_EPS - 1:
            print(f"  eps={eps:+.4f}: evals = [{pos_evals[0]:.6f}, ..., {pos_evals[-1]:.6f}]"
                  f"  L=({L1:.4f}, {L2:.4f}, {L3:.4f})")

    t_scan = time.time() - t_start
    print(f"  Scan complete: {t_scan:.1f}s")

    # ── Track branches ──
    print("\n[TRACK] Tracking branches by continuity...")
    tracked_evals, tracked_labels = track_branches(all_evals, eps_arr, branch_labels)

    # Verify tracking: check B2 4-fold degeneracy at eps=0
    ref_idx = np.argmin(np.abs(eps_arr))
    b2_at_ref = tracked_evals[ref_idx, b2_mask]
    b3_at_ref = tracked_evals[ref_idx, b3_mask]
    print(f"  B2 at eps=0: {b2_at_ref} (spread: {np.ptp(b2_at_ref):.2e})")
    print(f"  B3 at eps=0: {b3_at_ref} (spread: {np.ptp(b3_at_ref):.2e})")

    # ── Compute gap ──
    print("\n[GAP] Computing B2-B3 gap along T2...")
    gap, b2_max, b3_min = compute_b2_b3_gap(tracked_evals, tracked_labels)

    gap_min_idx = np.argmin(gap)
    gap_min = gap[gap_min_idx]
    eps_at_gap_min = eps_arr[gap_min_idx]

    print(f"  Gap at eps=0: {gap[ref_idx]:.6f}")
    print(f"  Gap minimum: {gap_min:.6f} at eps = {eps_at_gap_min:.4f}")
    print(f"  Gap range: [{np.min(gap):.6f}, {np.max(gap):.6f}]")

    # ── Check for degeneracy splitting ──
    print("\n[SPLIT] Checking B2 degeneracy splitting off-Jensen...")
    b2_evals = tracked_evals[:, b2_mask]
    b2_spread = np.ptp(b2_evals, axis=1)  # max - min within B2 at each eps
    b3_evals = tracked_evals[:, b3_mask]
    b3_spread = np.ptp(b3_evals, axis=1)

    print(f"  B2 spread at eps=0: {b2_spread[ref_idx]:.2e}")
    print(f"  B2 max spread: {np.max(b2_spread):.6f} at eps = {eps_arr[np.argmax(b2_spread)]:.4f}")
    print(f"  B3 spread at eps=0: {b3_spread[ref_idx]:.2e}")
    print(f"  B3 max spread: {np.max(b3_spread):.6f} at eps = {eps_arr[np.argmax(b3_spread)]:.4f}")

    # ── Gap closure detection ──
    gap_closure_found = False
    eps_closure = None
    z_before = None
    z_after = None

    if gap_min <= 0:
        gap_closure_found = True
        # Find zero crossing by linear interpolation
        for i in range(len(gap) - 1):
            if gap[i] > 0 and gap[i+1] <= 0:
                # Linear interpolation
                eps_closure = eps_arr[i] + (eps_arr[i+1] - eps_arr[i]) * gap[i] / (gap[i] - gap[i+1])
                break
            elif gap[i] <= 0 and gap[i+1] > 0:
                eps_closure = eps_arr[i] + (eps_arr[i+1] - eps_arr[i]) * (-gap[i]) / (gap[i+1] - gap[i])
                break
        if eps_closure is None:
            eps_closure = eps_at_gap_min

        print(f"\n*** GAP CLOSURE DETECTED at eps ~ {eps_closure:.4f} ***")

        if DO_Z_INVARIANT:
            print("\n[Z-INV] Computing BDI Z invariant on both sides of closure...")
            # Find indices flanking closure
            idx_before = max(0, gap_min_idx - 2)
            idx_after = min(N_EPS - 1, gap_min_idx + 2)

            z_before, asym_err_before = compute_bdi_z_invariant(
                all_omega[idx_before], gammas)
            z_after, asym_err_after = compute_bdi_z_invariant(
                all_omega[idx_after], gammas)

            print(f"  Z(eps={eps_arr[idx_before]:.4f}) = {z_before} (antisym err: {asym_err_before:.2e})")
            print(f"  Z(eps={eps_arr[idx_after]:.4f}) = {z_after} (antisym err: {asym_err_after:.2e})")

            if z_before != z_after:
                print(f"  *** TOPOLOGICAL TRANSITION: Z changes from {z_before} to {z_after} ***")
                print(f"  Topological edge modes GUARANTEED by Atiyah-Singer index theorem")
            else:
                print(f"  Z invariant unchanged ({z_before} on both sides)")
                print(f"  Gap closure is NOT topological (accidental degeneracy)")
    else:
        print(f"\n  No gap closure: minimum gap = {gap_min:.6f} > 0")

    # ── Also compute Z invariant at endpoints for reference ──
    print("\n[Z-INV] Computing Z invariant at scan endpoints for reference...")
    z_start, asym_start = compute_bdi_z_invariant(all_omega[0], gammas)
    z_end, asym_end = compute_bdi_z_invariant(all_omega[-1], gammas)
    z_ref, asym_ref = compute_bdi_z_invariant(all_omega[ref_idx], gammas)
    print(f"  Z(eps={eps_arr[0]:.3f}) = {z_start} (antisym: {asym_start:.2e})")
    print(f"  Z(eps=0) = {z_ref} (antisym: {asym_ref:.2e})")
    print(f"  Z(eps={eps_arr[-1]:.3f}) = {z_end} (antisym: {asym_end:.2e})")

    # ── Gate verdict ──
    print("\n" + "=" * 70)
    print("GATE VERDICT: TT-32c")
    print("=" * 70)

    if gap_closure_found:
        print(f"  VERDICT: PASS — Gap closes at eps* = {eps_closure:.4f}")
        if z_before is not None and z_after is not None and z_before != z_after:
            print(f"  TOPOLOGICAL: Z changes from {z_before} to {z_after}")
            print(f"  => Topological edge modes guaranteed by index theorem")
            verdict = "PASS_TOPOLOGICAL"
        else:
            print(f"  Gap closure found but Z invariant unchanged")
            print(f"  => Accidental degeneracy, not topological")
            verdict = "PASS_ACCIDENTAL"
    elif gap_min < 0.1:
        print(f"  VERDICT: OPEN — Gap minimum = {gap_min:.6f} < 0.1")
        print(f"  Near-closure at eps = {eps_at_gap_min:.4f}")
        print(f"  Full TOPO-1 2D grid needed to check other directions")
        verdict = "OPEN"
    elif gap_min < 0.2:
        print(f"  VERDICT: OPEN — Gap minimum = {gap_min:.6f} < 0.2")
        print(f"  Moderate gap at eps = {eps_at_gap_min:.4f}")
        verdict = "OPEN"
    else:
        print(f"  VERDICT: FAIL — Gap minimum = {gap_min:.6f} > 0.2")
        print(f"  Tesla zone-boundary prediction falsified along T2")
        verdict = "FAIL"

    # ── U(2) symmetry breaking diagnostic ──
    print("\n[DIAG] U(2) symmetry breaking along T2:")
    for i in [0, N_EPS // 4, N_EPS // 2, 3 * N_EPS // 4, N_EPS - 1]:
        L1, L2, L3 = all_L[i]
        sin2_tw = L2 / (L1 + L2)
        g1g2 = np.sqrt(L2 / L1)
        print(f"  eps={eps_arr[i]:+.3f}: L=({L1:.4f},{L2:.4f},{L3:.4f})"
              f"  sin2tw={sin2_tw:.4f}  g1/g2={g1g2:.4f}")

    # ── Summary table ──
    print("\n" + "=" * 70)
    print("EIGENVALUE FAN DIAGRAM (sampled)")
    print("=" * 70)
    print(f"{'eps':>8s}  {'B1':>10s}  {'B2 min':>10s}  {'B2 max':>10s}  {'B3 min':>10s}  {'B3 max':>10s}  {'Gap':>10s}  {'B2 spread':>10s}")
    for i in range(0, N_EPS, max(1, N_EPS // 15)):
        b1_val = tracked_evals[i, b1_mask][0]
        b2_min_val = np.min(tracked_evals[i, b2_mask])
        b2_max_val = np.max(tracked_evals[i, b2_mask])
        b3_min_val = np.min(tracked_evals[i, b3_mask])
        b3_max_val = np.max(tracked_evals[i, b3_mask])
        print(f"{eps_arr[i]:+8.4f}  {b1_val:10.6f}  {b2_min_val:10.6f}  {b2_max_val:10.6f}"
              f"  {b3_min_val:10.6f}  {b3_max_val:10.6f}  {gap[i]:10.6f}  {b2_spread[i]:10.6f}")

    # ── Save ──
    print(f"\n[SAVE] Writing outputs...")
    save_dict = {
        'tau_fixed': TAU_FIXED,
        'eps_arr': eps_arr,
        'all_evals_raw': all_evals,
        'tracked_evals': tracked_evals,
        'branch_labels': branch_labels,
        'gap': gap,
        'b2_max': b2_max,
        'b3_min': b3_min,
        'b2_spread': b2_spread,
        'b3_spread': b3_spread,
        'gap_min': gap_min,
        'eps_gap_min': eps_at_gap_min,
        'gap_closure_found': gap_closure_found,
        'eps_closure': eps_closure if eps_closure is not None else np.nan,
        'verdict': verdict,
        'all_L': all_L,
        'ref_evals_jensen': ref_evals,
        'deriv_ref': deriv_ref,
        'z_start': z_start if z_start is not None else np.nan,
        'z_end': z_end if z_end is not None else np.nan,
        'z_ref': z_ref if z_ref is not None else np.nan,
    }
    if z_before is not None:
        save_dict['z_before_closure'] = z_before
        save_dict['z_after_closure'] = z_after

    np.savez_compressed(OUT_NPZ, **save_dict)
    print(f"  Saved: {OUT_NPZ}")

    # ── Plot ──
    print("\n[PLOT] Generating eigenvalue fan diagram...")
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Panel 1: All 8 tracked eigenvalues vs eps (fan diagram)
    ax = axes[0, 0]
    for k in range(8):
        label = branch_labels[k]
        color = {'B1': 'green', 'B2': 'blue', 'B3': 'red'}[label]
        ls = '-' if label != 'B1' else '--'
        ax.plot(eps_arr, tracked_evals[:, k], color=color, linestyle=ls,
                linewidth=1.5, alpha=0.8)
    # Add legend entries
    ax.plot([], [], 'g--', linewidth=2, label='B1 (1 mode)')
    ax.plot([], [], 'b-', linewidth=2, label='B2 (4 modes)')
    ax.plot([], [], 'r-', linewidth=2, label='B3 (3 modes)')
    if gap_closure_found and eps_closure is not None:
        ax.axvline(eps_closure, color='black', linestyle=':', linewidth=1, label=f'Gap closure eps*={eps_closure:.3f}')
    ax.axvline(0, color='gray', linestyle=':', linewidth=0.5, alpha=0.5)
    ax.set_xlabel('epsilon (T2 direction)')
    ax.set_ylabel('Dirac eigenvalue (positive)')
    ax.set_title(f'Eigenvalue Fan Diagram (tau={TAU_FIXED})')
    ax.legend(fontsize=8, loc='upper left')
    ax.grid(True, alpha=0.3)

    # Panel 2: B2-B3 gap vs eps
    ax = axes[0, 1]
    ax.plot(eps_arr, gap, 'k-', linewidth=2, label='Delta_gap = min(B3) - max(B2)')
    ax.axhline(0, color='red', linestyle='--', linewidth=1, alpha=0.7, label='Gap closure')
    ax.axhline(0.1, color='orange', linestyle=':', linewidth=1, alpha=0.5, label='OPEN threshold (0.1)')
    ax.axhline(0.2, color='green', linestyle=':', linewidth=1, alpha=0.5, label='FAIL threshold (0.2)')
    ax.axvline(0, color='gray', linestyle=':', linewidth=0.5, alpha=0.5)
    if gap_closure_found and eps_closure is not None:
        ax.axvline(eps_closure, color='red', linestyle=':', linewidth=1)
        ax.plot(eps_closure, 0, 'ro', markersize=10, zorder=5)
    ax.plot(eps_at_gap_min, gap_min, 'kv', markersize=10, zorder=5, label=f'Min: {gap_min:.4f} at eps={eps_at_gap_min:.3f}')
    ax.set_xlabel('epsilon (T2 direction)')
    ax.set_ylabel('B2-B3 gap')
    ax.set_title(f'B2-B3 Gap vs T2 Perturbation | TT-32c: {verdict}')
    ax.legend(fontsize=7, loc='upper right')
    ax.grid(True, alpha=0.3)

    # Panel 3: B2 and B3 degeneracy splitting
    ax = axes[1, 0]
    ax.plot(eps_arr, b2_spread, 'b-', linewidth=2, label='B2 spread (4 modes)')
    ax.plot(eps_arr, b3_spread, 'r-', linewidth=2, label='B3 spread (3 modes)')
    ax.axvline(0, color='gray', linestyle=':', linewidth=0.5, alpha=0.5)
    ax.set_xlabel('epsilon (T2 direction)')
    ax.set_ylabel('Eigenvalue spread within branch')
    ax.set_title('Degeneracy Splitting Off-Jensen')
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    ax.set_yscale('log')

    # Panel 4: Metric parameters along T2
    ax = axes[1, 1]
    ax.plot(eps_arr, all_L[:, 0], 'r-', linewidth=2, label='L1 (u(1))')
    ax.plot(eps_arr, all_L[:, 1], 'b-', linewidth=2, label='L2 (su(2))')
    ax.plot(eps_arr, all_L[:, 2], 'g-', linewidth=2, label='L3 (C^2)')
    sin2_tw = all_L[:, 1] / (all_L[:, 0] + all_L[:, 1])
    ax2 = ax.twinx()
    ax2.plot(eps_arr, sin2_tw, 'k--', linewidth=1.5, alpha=0.7, label='sin2(theta_W)')
    ax2.axhline(0.231, color='purple', linestyle=':', linewidth=1, alpha=0.5)
    ax2.set_ylabel('sin^2(theta_W)', color='black')
    ax.axvline(0, color='gray', linestyle=':', linewidth=0.5, alpha=0.5)
    ax.set_xlabel('epsilon (T2 direction)')
    ax.set_ylabel('Scale factor')
    ax.set_title('Metric Parameters Along T2')
    ax.legend(fontsize=8, loc='upper left')
    ax2.legend(fontsize=8, loc='upper right')
    ax.grid(True, alpha=0.3)

    plt.suptitle(f'TOPO-T2: B2-B3 Gap Scan | tau={TAU_FIXED}, eps in [{EPS_MIN},{EPS_MAX}] | {verdict}',
                 fontsize=12, fontweight='bold')
    plt.tight_layout()
    plt.savefig(OUT_PNG, dpi=150, bbox_inches='tight')
    print(f"  Saved: {OUT_PNG}")

    t_total = time.time() - t_start
    print(f"\n{'=' * 70}")
    print(f"TOPO-T2 COMPLETE. {N_EPS} points in {t_total:.1f}s.")
    print(f"  Gap minimum: {gap_min:.6f} at eps = {eps_at_gap_min:.4f}")
    print(f"  Verdict: {verdict}")
    print(f"{'=' * 70}")

    return {
        'gap_min': gap_min,
        'eps_gap_min': eps_at_gap_min,
        'gap_closure_found': gap_closure_found,
        'eps_closure': eps_closure,
        'verdict': verdict,
        'z_start': z_start,
        'z_end': z_end,
        'z_ref': z_ref,
    }


if __name__ == '__main__':
    results = main()
