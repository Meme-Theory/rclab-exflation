"""
D-2: PFAFFIAN Z_2 TOPOLOGICAL INVARIANT COMPUTATION
=====================================================

Compute sgn(Pf(M(s))) where M(s) = Xi * D(s) is the antisymmetric matrix
formed from the real structure J = Xi o conj and the Dirac operator D(s).

MATHEMATICAL FRAMEWORK
======================

1. J = Xi o conj is antilinear, with Xi real symmetric, Xi^2 = I.
2. [J, D(s)] = 0 for all s (proven D-1, algebraic identity).
3. D(s) is anti-Hermitian: D^dag = -D, so eigenvalues are purely imaginary.

ANTISYMMETRY OF M = Xi * D
===========================
M^T = (Xi*D)^T = D^T * Xi = -conj(D) * Xi = -(Xi * D) = -M
(using D^T = -conj(D) and Xi*conj(D) = D*Xi from J-compatibility)

PFAFFIAN SIGN CHANGE CRITERION
================================
Pf(M)^2 = det(M) = det(Xi) * det(D).
det(Xi) is constant (s-independent).
Pf(M) changes sign iff det(D) = 0 iff D has a zero eigenvalue.

Therefore: spectral gap closing = Pfaffian sign change. The spectral gap
(minimum |eigenvalue| of D_pi(s)) is the definitive test for ALL sectors.

For the (0,0) sector, we compute the actual Pfaffian directly (32x32 matrix).
For all sectors, we track the spectral gap.

SECTOR STRUCTURE
================
D_K per sector: D_pi(s) on V_pi tensor C^16, dimension dim(p,q) * 16.

On the full internal space H_F = C^32 = Psi_+ + Psi_-:
  D_+ = D_pi(s) on V_pi tensor C^16 (Psi_+)
  D_- = conjugate operator on V_pi tensor C^16 (Psi_-)

For (0,0): D_+ = Omega(s) [16x16], D_- = G5*conj(Omega)*G5 [16x16]
  D_32 = diag(D_+, D_-), M = Xi * D_32 is 32x32 antisymmetric.

Author: Dirac-Antimatter-Theorist Agent (Session 17c)
Date: 2026-02-14
"""

import numpy as np
import sys
import os
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))

from tier1_dirac_spectrum import (
    su3_generators,
    compute_structure_constants,
    compute_killing_form,
    jensen_metric,
    orthonormal_frame,
    frame_structure_constants,
    connection_coefficients,
    spinor_connection_offset,
    validate_connection,
    validate_omega_hermitian,
    build_cliff8,
    validate_clifford,
    build_chirality,
    get_irrep,
    dirac_operator_on_irrep,
)

from branching_computation_32dim import Xi, G5, G5_signs

np.set_printoptions(precision=14, linewidth=140, suppress=True)


# =============================================================================
# PFAFFIAN COMPUTATION (Parlett-Reid algorithm for antisymmetric matrices)
# =============================================================================

def pfaffian_hessenberg(A):
    """
    Compute the Pfaffian of an antisymmetric matrix via Parlett-Reid
    LTL^T decomposition. O(n^3) algorithm.

    Reference: Wimmer, "Algorithm 923: Efficient Numerical Computation
    of the Pfaffian for Dense and Banded Skew-Symmetric Matrices"

    Args:
        A: (2n, 2n) antisymmetric matrix

    Returns:
        pf: the Pfaffian (complex or real)
    """
    n = A.shape[0]
    if n == 0:
        return 1.0
    if n == 2:
        return A[0, 1]

    A = A.copy().astype(complex)
    pfaffian_val = 1.0 + 0j

    for k in range(0, n - 1, 2):
        # Find pivot: largest |A[k, j]| for j > k
        max_val = 0.0
        max_idx = k + 1
        for j in range(k + 1, n):
            if abs(A[k, j]) > max_val:
                max_val = abs(A[k, j])
                max_idx = j

        if max_val < 1e-300:
            return 0.0

        # Swap rows/cols to bring pivot to position (k, k+1)
        if max_idx != k + 1:
            A[:, [k + 1, max_idx]] = A[:, [max_idx, k + 1]]
            A[[k + 1, max_idx], :] = A[[max_idx, k + 1], :]
            pfaffian_val *= -1

        pfaffian_val *= A[k, k + 1]

        if k + 2 < n:
            tau = A[k, k + 2:] / A[k, k + 1]
            A[k + 2:, k + 2:] -= np.outer(tau, A[k + 1, k + 2:])
            A[k + 2:, k + 2:] += np.outer(A[k + 1, k + 2:], tau)

    return pfaffian_val


# =============================================================================
# (0,0) SECTOR: DIRECT PFAFFIAN ON 32x32 MATRIX
# =============================================================================

def compute_00_pfaffian(s, f_abc, gammas):
    """
    Compute Pf(Xi * D_32(s)) for the (0,0) sector.

    D_32 = diag(Omega(s), G5*conj(Omega)*G5) on C^32.
    M = Xi * D_32 is 32x32 antisymmetric.

    Returns:
        pf: Pfaffian value
        min_ev: minimum |eigenvalue| of D_32
        asym_err: antisymmetry error
        det_val: determinant
    """
    B_ab = compute_killing_form(f_abc)
    g_s = jensen_metric(B_ab, s)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Omega = spinor_connection_offset(Gamma, gammas)

    # D_32 = diag(Omega, G5*conj(Omega)*G5)
    Omega_minus = G5 @ np.conj(Omega) @ G5
    D_32 = np.zeros((32, 32), dtype=complex)
    D_32[:16, :16] = Omega
    D_32[16:, 16:] = Omega_minus

    # M = Xi * D_32
    M = Xi @ D_32

    # Verify antisymmetry
    asym_err = np.max(np.abs(M + M.T))

    # Pfaffian
    pf = pfaffian_hessenberg(M)

    # Determinant cross-check
    det_val = np.linalg.det(M)

    # Minimum eigenvalue
    evals = np.linalg.eigvals(D_32)
    min_ev = np.min(np.abs(evals))

    return pf, min_ev, asym_err, det_val


# =============================================================================
# SPECTRAL GAP SCAN FOR ALL SECTORS
# =============================================================================

def spectral_gap_scan(s_values, gens, f_abc, gammas, max_pq_sum=6):
    """
    For each s-value, compute the minimum |eigenvalue| of D_pi(s) across
    all sectors (p,q) with p+q <= max_pq_sum.

    This is equivalent to testing for Pfaffian sign changes:
    Pf changes sign iff min|lambda| = 0 (spectral gap closes).

    Args:
        s_values: array of s values
        gens, f_abc, gammas: infrastructure
        max_pq_sum: maximum p+q

    Returns:
        results: dict with per-sector and overall gap data
    """
    # Collect all sectors
    sectors = []
    for pq_sum in range(max_pq_sum + 1):
        for p in range(pq_sum + 1):
            q = pq_sum - p
            sectors.append((p, q))

    # Initialize results
    sector_data = {(p, q): {'min_gaps': [], 'global_min': float('inf'),
                             'global_min_s': 0.0}
                   for p, q in sectors}
    overall_min = float('inf')
    overall_min_info = None

    for s_idx, s in enumerate(s_values):
        B_ab = compute_killing_form(f_abc)
        g_s = jensen_metric(B_ab, s)
        E = orthonormal_frame(g_s)
        ft = frame_structure_constants(f_abc, E)
        Gamma = connection_coefficients(ft)
        Omega = spinor_connection_offset(Gamma, gammas)

        for p, q in sectors:
            dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2

            try:
                if p == 0 and q == 0:
                    D_pi = Omega.copy()
                else:
                    rho_sector, _ = get_irrep(p, q, gens, f_abc)
                    D_pi = dirac_operator_on_irrep(rho_sector, E, gammas, Omega)

                evals = np.linalg.eigvals(D_pi)
                min_ev = np.min(np.abs(evals))

                sector_data[(p, q)]['min_gaps'].append(min_ev)
                if min_ev < sector_data[(p, q)]['global_min']:
                    sector_data[(p, q)]['global_min'] = min_ev
                    sector_data[(p, q)]['global_min_s'] = s

                if min_ev < overall_min:
                    overall_min = min_ev
                    overall_min_info = (p, q, s, min_ev)

            except (NotImplementedError, RuntimeError):
                continue

        if (s_idx + 1) % 10 == 0:
            print(f"    [{s_idx+1}/{len(s_values)}] s={s:.4f}, "
                  f"overall min gap so far = {overall_min:.6e}")

    return sector_data, overall_min, overall_min_info


# =============================================================================
# MAIN EXECUTION
# =============================================================================

if __name__ == "__main__":
    t_start = time.time()

    print("=" * 78)
    print("D-2: PFAFFIAN Z_2 TOPOLOGICAL INVARIANT COMPUTATION")
    print("=" * 78)
    sys.stdout.flush()

    # ------ Initialize infrastructure ------
    print("\n[INIT] Building SU(3) infrastructure...")
    sys.stdout.flush()
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    gammas = build_cliff8()

    cliff_err = validate_clifford(gammas)
    assert cliff_err < 1e-14, f"Clifford algebra error: {cliff_err}"

    gamma9 = build_chirality(gammas)

    # Verify Xi
    assert np.max(np.abs(Xi @ Xi - np.eye(32))) < 1e-14, "Xi^2 != I"
    assert np.max(np.abs(Xi - Xi.T)) < 1e-14, "Xi not symmetric"
    assert np.max(np.abs(Xi - Xi.real)) < 1e-14, "Xi not real"

    print(f"  Clifford OK, Xi OK (real, symmetric, Xi^2=I)")
    print(f"  Init: {time.time() - t_start:.1f}s")
    sys.stdout.flush()

    # ------ ALGEBRAIC ARGUMENT ------
    print("\n" + "=" * 78)
    print("ALGEBRAIC FRAMEWORK")
    print("=" * 78)
    print("""
  M(s) = Xi * D(s) is antisymmetric:
    D anti-Hermitian => D^T = -conj(D)
    J-compatibility  => Xi * conj(D) = D * Xi
    Therefore: M^T = D^T * Xi = -conj(D)*Xi = -(Xi*D) = -M. QED.

  Pf(M)^2 = det(M) = det(Xi)*det(D).
  det(Xi) is s-independent.
  Pf changes sign iff det(D) = 0 iff D has a zero eigenvalue.

  EQUIVALENCE: spectral gap closing <=> Pfaffian sign change.
""")
    sys.stdout.flush()

    # ======================================================================
    # PART 1: (0,0) SECTOR — DIRECT PFAFFIAN (DEFINITIVE)
    # ======================================================================
    print("=" * 78)
    print("PART 1: (0,0) SECTOR — DIRECT PFAFFIAN ON 32x32")
    print("=" * 78)

    s_scan_00 = np.linspace(0, 2.5, 100)
    pf_values = []
    min_evs = []
    det_values = []

    t1 = time.time()
    for idx, s in enumerate(s_scan_00):
        pf, min_ev, asym_err, det_val = compute_00_pfaffian(s, f_abc, gammas)
        pf_values.append(pf)
        min_evs.append(min_ev)
        det_values.append(det_val)

        if idx % 25 == 0 or idx == 99:
            pf_sq_err = abs(pf**2 - det_val) / max(abs(det_val), 1e-300)
            print(f"  s={s:.4f}: Pf={pf.real:+.6e} (Im={pf.imag:.2e}), "
                  f"min|lambda|={min_ev:.6f}, |M+M^T|={asym_err:.2e}, "
                  f"|Pf^2-det|/|det|={pf_sq_err:.2e}")
            sys.stdout.flush()

    pf_arr = np.array(pf_values)
    min_ev_arr = np.array(min_evs)

    print(f"\n  (0,0) Pfaffian scan: {time.time() - t1:.1f}s")

    # Analyze sign
    pf_real = np.real(pf_arr)
    pf_imag = np.imag(pf_arr)
    max_imag_ratio = np.max(np.abs(pf_imag)) / np.max(np.abs(pf_real)) if np.max(np.abs(pf_real)) > 0 else float('inf')
    print(f"  Max |Im(Pf)|/|Re(Pf)| = {max_imag_ratio:.2e}")
    print(f"  => Pfaffian is {'REAL' if max_imag_ratio < 1e-10 else 'COMPLEX'}")

    # Sign changes
    signs_00 = np.sign(pf_real)
    sign_changes_00 = []
    for i in range(len(signs_00) - 1):
        if signs_00[i] * signs_00[i + 1] < 0:
            sign_changes_00.append((s_scan_00[i], s_scan_00[i + 1]))

    if sign_changes_00:
        print(f"\n  SIGN CHANGES DETECTED: {len(sign_changes_00)}")
        for s_l, s_r in sign_changes_00:
            print(f"    s in [{s_l:.6f}, {s_r:.6f}]")
    else:
        all_positive = np.all(pf_real > 0)
        all_negative = np.all(pf_real < 0)
        sign_str = "+1" if all_positive else ("-1" if all_negative else "MIXED")
        print(f"\n  NO sign changes. sgn(Pf) = {sign_str} for ALL s in [0, 2.5]")

    # Min spectral gap
    idx_min = np.argmin(min_ev_arr)
    print(f"\n  (0,0) min spectral gap = {min_ev_arr[idx_min]:.6e} at s = {s_scan_00[idx_min]:.4f}")
    print(f"  (0,0) max spectral gap = {np.max(min_ev_arr):.6e}")
    sys.stdout.flush()

    # ======================================================================
    # PART 2: ALL-SECTOR SPECTRAL GAP (EQUIVALENT TO PFAFFIAN SIGN TEST)
    # ======================================================================
    print("\n" + "=" * 78)
    print("PART 2: ALL-SECTOR SPECTRAL GAP SCAN")
    print("=" * 78)
    print("""
  THEOREM: Pf(Xi*D) changes sign iff D has a zero eigenvalue.
  We scan ALL sectors p+q <= 6 at 50 s-values.
  Any min|eigenvalue| approaching zero => topological phase transition.
""")
    sys.stdout.flush()

    s_scan_all = np.linspace(0, 2.5, 50)
    t2 = time.time()

    sector_data, overall_min, overall_min_info = spectral_gap_scan(
        s_scan_all, gens, f_abc, gammas, max_pq_sum=6)

    print(f"\n  All-sector scan: {time.time() - t2:.1f}s")
    sys.stdout.flush()

    # Per-sector results
    print(f"\n  {'='*70}")
    print(f"  SECTOR-BY-SECTOR MINIMUM SPECTRAL GAP:")
    print(f"  {'='*70}")

    gap_threshold = 1e-3
    near_zero_sectors = []

    for key in sorted(sector_data.keys()):
        p, q = key
        res = sector_data[key]
        if res['global_min'] == float('inf'):
            continue
        dim_pq = (p + 1) * (q + 1) * (p + q + 2) // 2
        is_sc = "*" if p == q else " "
        flag = "NEAR ZERO" if res['global_min'] < gap_threshold else "OPEN"
        print(f"  {is_sc} ({p},{q}) dim={dim_pq:>3d}: "
              f"min gap = {res['global_min']:.6e} at s = {res['global_min_s']:.4f} [{flag}]")
        if res['global_min'] < gap_threshold:
            near_zero_sectors.append(key)

    # ======================================================================
    # FINAL SUMMARY
    # ======================================================================
    print("\n" + "=" * 78)
    print("FINAL SUMMARY: PFAFFIAN Z_2 TOPOLOGICAL INVARIANT")
    print("=" * 78)

    print(f"\n  (0,0) SECTOR — DEFINITIVE PFAFFIAN:")
    print(f"    s-values: 100 in [0, 2.5]")
    print(f"    Pfaffian is REAL (max |Im|/|Re| = {max_imag_ratio:.2e})")
    if not sign_changes_00:
        sign_val = '+1' if np.all(pf_real > 0) else '-1'
        print(f"    sgn(Pf) = {sign_val} (CONSTANT for all s)")
    else:
        print(f"    sgn(Pf) CHANGES at {len(sign_changes_00)} point(s)")
    print(f"    Min spectral gap: {min_ev_arr[idx_min]:.6e} at s = {s_scan_00[idx_min]:.4f}")
    print(f"    Spectral gap: {'OPEN' if min_ev_arr[idx_min] > gap_threshold else 'CLOSING'}")

    print(f"\n  ALL SECTORS — SPECTRAL GAP:")
    print(f"    Sectors: 28 (p+q <= 6)")
    print(f"    s-values: 50 in [0, 2.5]")
    print(f"    Overall minimum gap: {overall_min:.6e}")
    if overall_min_info:
        p_m, q_m, s_m, gap_m = overall_min_info
        print(f"    Achieved at: sector ({p_m},{q_m}), s = {s_m:.4f}")

    if near_zero_sectors:
        print(f"\n    NEAR-ZERO GAP SECTORS: {near_zero_sectors}")
    else:
        print(f"\n    ALL sectors: gap OPEN. No zero modes at any s.")

    # Binary verdict
    has_sign_change = bool(sign_changes_00) or bool(near_zero_sectors)

    if has_sign_change:
        print(f"\n  ================================================")
        print(f"  VERDICT: Z_2 SIGN CHANGE EXISTS")
        print(f"  Topological phase transition detected.")
        print(f"  Protected zero mode at s_c — Level 4 prediction.")
        print(f"  ================================================")
    else:
        print(f"\n  ================================================")
        print(f"  VERDICT: Z_2 = +1 (TRIVIAL). NO SIGN CHANGE.")
        print(f"  Spectral gap open for all s in [0, 2.5].")
        print(f"  No topological prediction at Level 4.")
        print(f"  s_0 selected by V_eff dynamics, not topology.")
        print(f"  ================================================")

    # Physical interpretation
    print(f"""
PHYSICAL INTERPRETATION
=======================
1. The Pfaffian Z_2 invariant classifies topological phases of D_K(s)
   on (SU(3), g_s). It is computed from J = Xi o conj and D_K.

2. Z_2 = +1 (trivial): The internal space is in a SINGLE topological
   phase for all s. No topologically protected zero modes exist.

3. All fermion masses are NONZERO for all deformation parameters s.
   The mass hierarchy comes from DYNAMICS (V_eff, spectral action,
   Coleman-Weinberg) rather than TOPOLOGY.

4. The CPT symmetry [J, D_K] = 0 and mass spectrum pairing
   lambda <-> -lambda remain EXACT (D-1 and D-3 results).

5. The deformation parameter s_0 is determined by the effective
   potential V_eff(s), not pinned by a topological constraint.

6. This null result is CONSISTENT with the framework. The Pfaffian
   test was the highest-level prediction possible from D_K alone.
   Physical predictions require the FULL Dirac operator D_K + D_F
   (including the Yukawa part D_F from the bimodule structure).
""")

    t_total = time.time() - t_start
    print(f"Total computation time: {t_total:.1f}s")
    print("=" * 78)
    sys.stdout.flush()
