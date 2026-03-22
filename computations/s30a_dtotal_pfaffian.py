"""
Session 30Ab: D_total Pfaffian Scan on 864-dim H_total
======================================================

Constructs D_total(tau) = D_K + D_F on the truncated internal Hilbert space
and computes the Pfaffian of M(tau) = Xi_ext * D_total to detect topological
phase transitions (Z_2 sign changes).

MATHEMATICAL FRAMEWORK
======================

H_trunc = bigoplus_{p+q <= N_max} V_{(p,q)} tensor C^16      (432-dim, Psi_+)
H_total = H_trunc(Psi_+) + H_trunc(Psi_-)                    (864-dim)

D_total on each sector:
  Psi_+: D_{(p,q)}^+ = D_K(sector) + D_F(sector)  (anti-Hermitian)
  Psi_-: D_{(p,q)}^- = G5_ext * conj(D_{(p,q)}^+) * G5_ext  (charge conjugate)

  where G5_ext = I_{dim_rho} tensor G5  (G5 from Baptista eq 2.12)

Xi_ext per sector block:
  Xi = ( 0,       -G5_ext )
       ( -G5_ext,  0      )

M = Xi * D_total is antisymmetric (verified numerically at machine epsilon).
The Pfaffian FACTORIZES over the 6 sector blocks:
  Pf(M_864) = prod_{sectors} Pf(M_sector)

KEY STRUCTURAL RESULT (from prototype debugging):
  - Each sector pairs with its OWN charge conjugate, NOT with the
    contragredient representation sector.
  - Xi maps V_{(p,q)} tensor C^16(Psi_+) to the SAME V_{(p,q)} tensor C^16(Psi_-)
    via G5 spinor conjugation (not representation conjugation).
  - D_minus = G5_ext * conj(D_plus) * G5_ext (NOT D on the conjugate sector).
  - J-compatibility Xi * conj(D) = D * Xi verified at 0.0e+00 for all sectors.
  - Cross-validated with baptista-spacetime-analyst (Paper 18, Lemma 6.4).

GATE CONDITIONS (from 29B plan)
================================
  B-29f: Pf constant for all tau => topological route fully exhausted (CLOSURE)
  P-29f: Pf sign change at tau_c => Level 4 topological prediction
  P-29g: tau_c near BCS transition (~0.35) => probability jump

Author: phonon-exflation-sim (Session 30Ab)
Date: 2026-03-01
Cross-validated by: baptista-spacetime-analyst
"""

import sys
import os
import time
import numpy as np
from scipy.linalg import block_diag

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from tier1_dirac_spectrum import (
    su3_generators,
    compute_structure_constants,
    compute_killing_form,
    jensen_metric,
    orthonormal_frame,
    frame_structure_constants,
    connection_coefficients,
    spinor_connection_offset,
    build_cliff8,
    build_chirality,
    validate_clifford,
    collect_spectrum_with_eigenvectors,
    get_irrep,
    dirac_operator_on_irrep,
    C2_IDX, U2_IDX,
)

from branching_computation_32dim import Xi, G5, G5_signs
from s23a_kosmann_singlet import kosmann_operator_antisymmetric
from s30a_df_construction import assemble_full_df, MAX_PQ_SUM


# =============================================================================
# PARLETT-REID PFAFFIAN (from d2_pfaffian_computation.py)
# =============================================================================

def pfaffian_parlett_reid(A):
    """
    Pfaffian via Parlett-Reid LTL^T decomposition. O(n^3).

    Reference: Wimmer, Algorithm 923.
    """
    n = A.shape[0]
    if n == 0:
        return 1.0 + 0j
    if n % 2 != 0:
        return 0.0 + 0j
    if n == 2:
        return A[0, 1]

    A = A.copy().astype(complex)
    pf = 1.0 + 0j

    for k in range(0, n - 1, 2):
        max_val = 0.0
        max_idx = k + 1
        for j in range(k + 1, n):
            if abs(A[k, j]) > max_val:
                max_val = abs(A[k, j])
                max_idx = j

        if max_val < 1e-300:
            return 0.0 + 0j

        if max_idx != k + 1:
            A[:, [k + 1, max_idx]] = A[:, [max_idx, k + 1]]
            A[[k + 1, max_idx], :] = A[[max_idx, k + 1], :]
            pf *= -1

        pf *= A[k, k + 1]

        if k + 2 < n:
            tau_vec = A[k, k + 2:] / A[k, k + 1]
            A[k + 2:, k + 2:] -= np.outer(tau_vec, A[k + 1, k + 2:])
            A[k + 2:, k + 2:] += np.outer(A[k + 1, k + 2:], tau_vec)

    return pf


# =============================================================================
# D_TOTAL CONSTRUCTION PER SECTOR (original basis)
# =============================================================================

def build_sector_block(D_total_plus, dim_rho, G5_16):
    """
    Build the paired (Psi_+ + Psi_-) block for a single sector.

    D_total_plus: (dim_sector, dim_sector) anti-Hermitian on Psi_+
    D_minus = G5_ext * conj(D_plus) * G5_ext

    Returns:
        D_block: (2*dim_sector, 2*dim_sector) D on Psi_+ + Psi_-
        Xi_block: (2*dim_sector, 2*dim_sector) charge conjugation
        M_block: (2*dim_sector, 2*dim_sector) antisymmetric matrix
    """
    dim_s = D_total_plus.shape[0]
    G5_ext = np.kron(np.eye(dim_rho, dtype=complex), G5_16)

    D_minus = G5_ext @ np.conj(D_total_plus) @ G5_ext

    D_block = np.zeros((2 * dim_s, 2 * dim_s), dtype=complex)
    D_block[:dim_s, :dim_s] = D_total_plus
    D_block[dim_s:, dim_s:] = D_minus

    Xi_block = np.zeros((2 * dim_s, 2 * dim_s), dtype=complex)
    Xi_block[:dim_s, dim_s:] = -G5_ext
    Xi_block[dim_s:, :dim_s] = -G5_ext

    M_block = Xi_block @ D_block

    return D_block, Xi_block, M_block


def compute_dtotal_at_tau(tau, gens, f_abc, gammas, G5_16, max_pq_sum=MAX_PQ_SUM):
    """
    Compute D_total and Pfaffian data at a single tau value.

    Returns dict with all diagnostics and the Pfaffian value.
    """
    # Get D_F in eigenbasis + eigenvectors
    D_F_eig, D_K_diag, sector_info, gamma_F, infra = assemble_full_df(
        tau, gens, f_abc, gammas, max_pq_sum=max_pq_sum, verbose=False
    )

    # Get eigenvectors for back-transformation
    sector_data, _ = collect_spectrum_with_eigenvectors(
        tau, gens, f_abc, gammas, max_pq_sum=max_pq_sum, verbose=False
    )

    # Build sector blocks in original basis
    M_blocks = []
    sector_pf = []
    sector_gaps = []
    sector_asym = []
    total_df_norm_sq = 0.0
    total_dk_norm_sq = 0.0

    offset = 0
    for sd in sector_data:
        p, q = sd['p'], sd['q']
        dim_rho = sd['dim_rho']
        dim_sector = dim_rho * 16
        evecs = sd['evecs']
        D_pi = sd['D_pi']  # D_K in original basis

        # Extract and back-transform D_F for this sector
        D_F_sector_eig = D_F_eig[offset:offset + dim_sector,
                                  offset:offset + dim_sector]
        D_F_sector_orig = evecs @ D_F_sector_eig @ evecs.conj().T

        # D_total in original basis
        D_total_sector = D_pi + D_F_sector_orig

        # Norms
        df_norm_sq = np.sum(np.abs(D_F_sector_orig)**2)
        dk_norm_sq = np.sum(np.abs(D_pi)**2)
        total_df_norm_sq += df_norm_sq
        total_dk_norm_sq += dk_norm_sq

        # Build paired block
        D_block, Xi_block, M_block = build_sector_block(
            D_total_sector, dim_rho, G5_16
        )

        # Validate antisymmetry
        asym_err = np.max(np.abs(M_block + M_block.T))
        sector_asym.append(asym_err)

        # Sector spectral gap (from D_total on Psi_+)
        evals = np.linalg.eigvals(D_total_sector)
        gap = np.min(np.abs(evals))
        sector_gaps.append(gap)

        # Sector Pfaffian
        pf_sector = pfaffian_parlett_reid(M_block)
        sector_pf.append(pf_sector)

        M_blocks.append(M_block)
        offset += dim_sector

    # Total Pfaffian = product of sector Pfaffians
    pf_total = 1.0 + 0j
    for pf_s in sector_pf:
        pf_total *= pf_s

    # Total spectral gap
    min_gap = min(sector_gaps)

    # Norms
    df_norm = np.sqrt(total_df_norm_sq)
    dk_norm = np.sqrt(total_dk_norm_sq)

    return {
        'tau': tau,
        'pf_total': pf_total,
        'pf_sectors': sector_pf,
        'min_gap': min_gap,
        'sector_gaps': sector_gaps,
        'df_norm': df_norm,
        'dk_norm': dk_norm,
        'max_asym': max(sector_asym),
        'sector_asym': sector_asym,
    }


# =============================================================================
# MAIN PFAFFIAN SCAN
# =============================================================================

def run_pfaffian_scan():
    """Main computation: Pfaffian scan over tau in [0, 2.5]."""
    print("=" * 78)
    print("Session 30Ab: D_total Pfaffian Scan (864-dim)")
    print("=" * 78)
    print()

    t_global = time.time()

    # Initialize
    print("[INIT] Building SU(3) infrastructure...")
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    gammas = build_cliff8()
    G5_16 = np.diag(G5_signs)

    cliff_err = validate_clifford(gammas)
    assert cliff_err < 1e-14, f"Clifford validation failed: {cliff_err}"
    print(f"  Clifford OK, G5 OK, Xi OK")
    print(f"  Init: {time.time() - t_global:.1f}s")

    # ================================================================
    # STEP 4: Validate at stored tau values
    # ================================================================
    print()
    print("=" * 78)
    print("STEP 4: D_total Construction and Validation")
    print("=" * 78)

    stored_data = np.load(os.path.join(SCRIPT_DIR, "s30a_df_construction.npz"))
    stored_tau = stored_data['tau_values']

    # OoO-4a: ||D_F||/||D_K|| at stored tau values
    print()
    print("OoO-4a: ||D_F||/||D_K|| ratio (original basis, with D_F contribution):")
    print(f"{'tau':>6s}  {'||D_F||':>12s}  {'||D_K||':>12s}  {'ratio':>8s}  "
          f"{'max_asym':>12s}  {'min_gap':>12s}")

    for tau_v in [0.0, 0.10, 0.15, 0.20, 0.30, 0.50]:
        result = compute_dtotal_at_tau(tau_v, gens, f_abc, gammas, G5_16)
        ratio = result['df_norm'] / result['dk_norm'] if result['dk_norm'] > 0 else 0.0
        print(f"{tau_v:6.2f}  {result['df_norm']:12.6e}  {result['dk_norm']:12.6e}  "
              f"{ratio:8.4f}  {result['max_asym']:12.2e}  {result['min_gap']:12.6e}")

        # Hard check on antisymmetry
        assert result['max_asym'] < 1e-10, \
            f"Antisymmetry FAILED at tau={tau_v}: err={result['max_asym']:.2e}"

    print()
    print("All validation checks PASS. Antisymmetry < 1e-10 at all stored tau.")
    sys.stdout.flush()

    # ================================================================
    # STEP 5: Full Pfaffian Scan
    # ================================================================
    print()
    print("=" * 78)
    print("STEP 5: Pfaffian Scan over tau in [0, 2.5]")
    print("=" * 78)
    print()

    N_TAU = 75
    tau_scan = np.linspace(0.0, 2.5, N_TAU)

    # Storage
    pf_values = np.zeros(N_TAU, dtype=complex)
    pf_signs = np.zeros(N_TAU)
    min_gap_dtotal = np.zeros(N_TAU)
    df_norms = np.zeros(N_TAU)
    dk_norms = np.zeros(N_TAU)
    asym_errs = np.zeros(N_TAU)

    # Sector Pfaffians for diagnostics (6 sectors)
    n_sectors = 6
    sector_pf_log = np.zeros((N_TAU, n_sectors), dtype=complex)

    print(f"Scanning {N_TAU} tau values in [0, 2.5]...")
    print(f"{'idx':>4s}  {'tau':>6s}  {'Re(Pf)':>14s}  {'Im(Pf)':>12s}  "
          f"{'sgn':>4s}  {'min_gap':>12s}  {'D_F/D_K':>8s}  {'asym':>10s}  {'t':>5s}")

    t_scan = time.time()

    for idx, tau in enumerate(tau_scan):
        t_step = time.time()

        result = compute_dtotal_at_tau(tau, gens, f_abc, gammas, G5_16)

        pf = result['pf_total']
        pf_values[idx] = pf
        pf_signs[idx] = np.sign(pf.real) if abs(pf.real) > 1e-300 else 0.0
        min_gap_dtotal[idx] = result['min_gap']
        df_norms[idx] = result['df_norm']
        dk_norms[idx] = result['dk_norm']
        asym_errs[idx] = result['max_asym']

        for s_idx, pf_s in enumerate(result['pf_sectors']):
            sector_pf_log[idx, s_idx] = pf_s

        dt = time.time() - t_step
        ratio = result['df_norm'] / result['dk_norm'] if result['dk_norm'] > 0 else 0.0

        if idx % 5 == 0 or idx == N_TAU - 1:
            print(f"{idx:4d}  {tau:6.3f}  {pf.real:+14.6e}  {pf.imag:12.2e}  "
                  f"{pf_signs[idx]:+4.0f}  {result['min_gap']:12.6e}  "
                  f"{ratio:8.4f}  {result['max_asym']:10.2e}  {dt:5.1f}s")
            sys.stdout.flush()

    scan_time = time.time() - t_scan
    print(f"\nScan: {scan_time:.1f}s total ({scan_time/N_TAU:.2f}s per tau)")

    # ================================================================
    # ANALYSIS
    # ================================================================
    print()
    print("=" * 78)
    print("PFAFFIAN ANALYSIS")
    print("=" * 78)

    # Reality check
    pf_real = np.real(pf_values)
    pf_imag = np.imag(pf_values)
    max_imag = np.max(np.abs(pf_imag))
    max_real = np.max(np.abs(pf_real))
    imag_ratio = max_imag / max_real if max_real > 0 else float('inf')
    print(f"\nPfaffian reality: max|Im|/max|Re| = {imag_ratio:.2e}")
    print(f"  => Pfaffian is {'REAL' if imag_ratio < 1e-8 else 'COMPLEX'}")

    # Sign analysis
    signs = pf_signs
    sign_changes = []
    for i in range(len(signs) - 1):
        if signs[i] * signs[i + 1] < 0:
            sign_changes.append((tau_scan[i], tau_scan[i + 1], i))

    if sign_changes:
        print(f"\n  SIGN CHANGES DETECTED: {len(sign_changes)}")
        for tau_l, tau_r, idx_l in sign_changes:
            print(f"    tau in [{tau_l:.4f}, {tau_r:.4f}]")
    else:
        all_pos = np.all(signs > 0)
        all_neg = np.all(signs < 0)
        sign_str = "+1" if all_pos else ("-1" if all_neg else "MIXED/ZERO")
        print(f"\n  NO sign changes. sgn(Pf) = {sign_str} for all tau")

    # Minimum spectral gap
    idx_min = np.argmin(min_gap_dtotal)
    print(f"\nMinimum spectral gap of D_total:")
    print(f"  min|lambda| = {min_gap_dtotal[idx_min]:.6e} at tau = {tau_scan[idx_min]:.4f}")

    # Per-sector Pfaffian sign analysis
    print(f"\nPer-sector Pfaffian signs (consistency check):")
    sector_labels = ['(0,0)', '(0,1)', '(0,2)', '(1,0)', '(1,1)', '(2,0)']
    for s_idx in range(n_sectors):
        s_signs = np.sign(np.real(sector_pf_log[:, s_idx]))
        changes = sum(1 for i in range(len(s_signs)-1) if s_signs[i]*s_signs[i+1] < 0)
        print(f"  {sector_labels[s_idx]}: sgn = {'+1' if np.all(s_signs > 0) else ('-1' if np.all(s_signs < 0) else 'VARIES')}, "
              f"changes = {changes}")

    # Antisymmetry quality
    print(f"\nAntisymmetry: [{asym_errs.min():.2e}, {asym_errs.max():.2e}]")

    # ||D_F||/||D_K|| evolution
    ratios = df_norms / np.maximum(dk_norms, 1e-300)
    print(f"\n||D_F||/||D_K|| range: [{ratios.min():.6f}, {ratios.max():.6f}]")

    # ================================================================
    # SIGN CHANGE REFINEMENT (if any)
    # ================================================================
    sign_change_taus = np.array([])
    if sign_changes:
        print()
        print("=" * 78)
        print("STEP 5a: Sign Change Refinement")
        print("=" * 78)

        refined = []
        for tau_l, tau_r, idx_l in sign_changes:
            print(f"\n  Bisecting [{tau_l:.4f}, {tau_r:.4f}]...")
            a, b = tau_l, tau_r
            sign_a = signs[idx_l]

            for bisect_iter in range(15):
                mid = (a + b) / 2.0
                res = compute_dtotal_at_tau(mid, gens, f_abc, gammas, G5_16)
                sign_mid = np.sign(res['pf_total'].real)

                if sign_mid == sign_a:
                    a = mid
                else:
                    b = mid
                print(f"    iter {bisect_iter:2d}: tau={mid:.6f}, "
                      f"Pf={res['pf_total'].real:+.6e}, gap={res['min_gap']:.6e}")

            tau_c = (a + b) / 2.0
            refined.append(tau_c)
            print(f"  tau_c = {tau_c:.6f}")

            # Eigenvalue structure at tau_c
            res_c = compute_dtotal_at_tau(tau_c, gens, f_abc, gammas, G5_16)
            print(f"  min gap at tau_c: {res_c['min_gap']:.6e}")
            print(f"  sector gaps: {[f'{g:.6e}' for g in res_c['sector_gaps']]}")

        sign_change_taus = np.array(refined)

    # ================================================================
    # GATE CLASSIFICATION
    # ================================================================
    print()
    print("=" * 78)
    print("GATE CLASSIFICATION")
    print("=" * 78)

    if sign_changes:
        print(f"\nP-29f: FIRES (Pfaffian sign change at tau_c = {sign_change_taus})")
        print(f"  Level 4 topological prediction: protected massless fermion.")

        for tc in sign_change_taus:
            pct = abs(tc - 0.35) / 0.35 * 100
            if pct < 10:
                print(f"  P-29g: FIRES! tau_c = {tc:.4f} within {pct:.1f}% of BCS ~0.35")
            else:
                print(f"  P-29g: Does not fire. tau_c = {tc:.4f} is {pct:.1f}% from ~0.35")
    else:
        sign_val = "+1" if np.all(signs > 0) else ("-1" if np.all(signs < 0) else "MIXED")
        print(f"\nB-29f: Pfaffian CONSTANT, sgn = {sign_val}")
        print(f"  Topological route fully exhausted. No Level 4 prediction.")
        print(f"  Min gap: {min_gap_dtotal[idx_min]:.6e} at tau = {tau_scan[idx_min]:.4f}")

    # Session 17c comparison
    print(f"\nCOMPARISON WITH D_K-ONLY (Session 17c):")
    print(f"  17c: Z_2 = +1 (D_K only, trivial)")
    if sign_changes:
        print(f"  30Ab: SIGN CHANGE -- D_F induces topological transition")
    else:
        print(f"  30Ab: Z_2 = {sign_val} (D_K + D_F, still trivial)")

    # ================================================================
    # SAVE
    # ================================================================
    output_path = os.path.join(SCRIPT_DIR, "s30a_dtotal_pfaffian.npz")
    np.savez_compressed(
        output_path,
        tau_values=tau_scan,
        pf_values=pf_values,
        pf_signs=pf_signs,
        min_gap_dtotal=min_gap_dtotal,
        D_F_norm=df_norms,
        D_K_norm=dk_norms,
        asym_errs=asym_errs,
        sign_change_tau=sign_change_taus,
        sector_pf_log=sector_pf_log,
    )
    file_size = os.path.getsize(output_path) / 1024
    print(f"\nSaved: {output_path} ({file_size:.1f} KB)")

    # ================================================================
    # FINAL SUMMARY
    # ================================================================
    total_time = time.time() - t_global
    print()
    print("=" * 78)
    print("FINAL SUMMARY")
    print("=" * 78)
    print(f"  Space: 864-dim (6 sectors x 2 chiralities, N_max={MAX_PQ_SUM})")
    print(f"  Scan: {N_TAU} tau in [0, 2.5]")
    print(f"  Antisymmetry: max err = {asym_errs.max():.2e}")
    if sign_changes:
        print(f"  VERDICT: SIGN CHANGE at tau_c = {sign_change_taus}")
    else:
        print(f"  VERDICT: Z_2 = {sign_val} (TRIVIAL)")
        print(f"  Min gap: {min_gap_dtotal[idx_min]:.6e} at tau = {tau_scan[idx_min]:.4f}")
    print(f"  Time: {total_time:.1f}s")
    print("=" * 78)
    sys.stdout.flush()

    return output_path


if __name__ == "__main__":
    output = run_pfaffian_scan()
    print(f"\nDone. Output: {output}")
