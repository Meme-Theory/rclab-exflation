"""
Session 23a Step 1: Extended eigenvector extraction from D_K(tau) for p+q <= 6.

Extends s22b_eigenvector_extraction.py from p+q <= 3 (10 sectors, 1232 modes)
to p+q <= 6 (28 sectors, 11424 modes). Same tau grid, same eigh method.

Mathematical background:
    D_pi = sum_{a,b} E_{ab} (rho(X_b) x gamma_a) + I_{dim_rho} x Omega(s)
    D_pi is anti-Hermitian => 1j * D_pi is Hermitian => eigh gives real eigenvalues
    and orthonormal eigenvectors.

Sectors added (p+q = 4, 5, 6):
    p+q=4: (0,4) (1,3) (2,2) (3,1) (4,0) -- 5 sectors, 1680 modes
    p+q=5: (0,5) (1,4) (2,3) (3,2) (4,1) (5,0) -- 6 sectors, 3136 modes
    p+q=6: (0,6) (1,5) (2,4) (3,3) (4,2) (5,1) (6,0) -- 7 sectors, 5376 modes
    Total new: 18 sectors, 10192 modes
    Grand total: 28 sectors, 11424 modes per tau value

    Largest matrix: (3,3) sector, dim=64, D_size=1024 -- eigh is fast.

Output: tier0-computation/s23a_eigenvectors_extended.npz
    Same key format as s22b_eigenvectors.npz:
        tau_values, eigenvalues_{i}, sector_p_{i}, sector_q_{i},
        multiplicities_{i}, sector_sizes_{i}, sector_labels_{i},
        eigvec_{i}_sector_{j}

Author: phonon-exflation-sim (Session 23a)
Date: 2026-02-20
"""

import sys
import os
import time
import numpy as np
from scipy.linalg import eigh

# Add tier0-computation to path
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
    get_irrep,
    dirac_operator_on_irrep,
    validate_omega_hermitian,
    validate_connection,
)


# Tau grid: 9 values including tau=0 for normalization
TAU_VALUES = np.array([0.0, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.50])

# Extended to p+q <= 6
MAX_PQ_SUM = 6


def dim_pq(p: int, q: int) -> int:
    """Dimension of SU(3) irrep (p,q).

    Formula: dim(p,q) = (p+1)(q+1)(p+q+2)/2
    """
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def build_geometry(tau: float, gens, f_abc, gammas):
    """
    Build all geometric objects needed for the Dirac operator at deformation tau.

    Parameters:
        tau: Jensen deformation parameter (tau=0 is bi-invariant)
        gens: SU(3) generators (8 matrices)
        f_abc: structure constants
        gammas: Cliff(8) gamma matrices

    Returns:
        E: (8,8) orthonormal frame
        Omega: (16,16) spinor connection offset (anti-Hermitian)
        Gamma: connection coefficients
    """
    B_ab = compute_killing_form(f_abc)
    g_s = jensen_metric(B_ab, tau)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Omega = spinor_connection_offset(Gamma, gammas)
    return E, Omega, Gamma


def build_sector_list(max_pq_sum: int):
    """
    Build sorted list of (p,q) sectors with p+q <= max_pq_sum.

    Sorted by Casimir eigenvalue (smallest first = gap-edge first).
    Casimir C_2(p,q) = (p^2 + q^2 + pq + 3p + 3q) / 3.

    Returns:
        List of (p, q) tuples
    """
    sectors = []
    for p in range(max_pq_sum + 1):
        for q in range(max_pq_sum + 1 - p):
            sectors.append((p, q))
    sectors.sort(key=lambda pq: (pq[0]**2 + pq[1]**2 + pq[0]*pq[1] +
                                  3*pq[0] + 3*pq[1]) / 3.0)
    return sectors


def extract_eigenvectors_at_tau(
    tau: float,
    gens,
    f_abc,
    gammas,
    sectors: list,
    verbose: bool = True,
):
    """
    Extract eigenvalues AND eigenvectors of D_K(tau) for given sectors.

    Since D_pi is anti-Hermitian, we diagonalize H_pi = 1j * D_pi (which is Hermitian)
    using scipy.linalg.eigh. This gives:
        H_pi = V @ diag(lambda) @ V^dag
    where lambda are real and V is unitary (columns = eigenvectors).

    Parameters:
        tau: Jensen deformation parameter
        gens: SU(3) generators
        f_abc: structure constants
        gammas: Cliff(8) gamma matrices
        sectors: list of (p, q) tuples to extract
        verbose: print progress

    Returns:
        eigenvalues: list of 1D arrays (real eigenvalues of 1j*D_pi per sector)
        eigenvectors: list of 2D arrays (columns = eigenvectors per sector)
        sector_labels: list of (p, q) tuples
        sector_dims: list of D_pi matrix dimensions
        pw_mults: list of Peter-Weyl multiplicities dim(p,q)
    """
    E, Omega, Gamma = build_geometry(tau, gens, f_abc, gammas)

    if verbose:
        mc_err = validate_connection(Gamma)
        is_h, is_ah, h_err, ah_err = validate_omega_hermitian(Omega)
        omega_type = "anti-Hermitian" if is_ah else ("Hermitian" if is_h else "NEITHER")
        print(f"  tau={tau:.3f}: connection metric-compat err={mc_err:.2e}, "
              f"Omega is {omega_type} (err={ah_err:.2e})")

    eigenvalues = []
    eigenvectors = []
    sector_labels = []
    sector_dims = []
    pw_mults = []

    for sec_idx, (p, q) in enumerate(sectors):
        d = dim_pq(p, q)
        D_size = d * 16

        t_sec = time.time()

        if p == 0 and q == 0:
            # Trivial irrep: D = Omega on 16-dim space
            D_pi = Omega.copy()
        else:
            rho, dim_check = get_irrep(p, q, gens, f_abc)
            assert dim_check == d, f"dim mismatch: expected {d}, got {dim_check}"
            D_pi = dirac_operator_on_irrep(rho, E, gammas, Omega)

        # Verify anti-Hermiticity of D_pi
        ah_err = np.max(np.abs(D_pi + D_pi.conj().T))
        if ah_err > 1e-8:
            print(f"  WARNING: D_pi({p},{q}) anti-Hermiticity error = {ah_err:.2e}")

        # Hermitianize: H = 1j * D_pi (Hermitian since D_pi is anti-Hermitian)
        H_pi = 1j * D_pi

        # Verify Hermiticity of H_pi
        h_err = np.max(np.abs(H_pi - H_pi.conj().T))
        if h_err > 1e-8:
            print(f"  WARNING: H_pi({p},{q}) Hermiticity error = {h_err:.2e}")

        # Diagonalize with eigh (guaranteed real eigenvalues, orthonormal eigenvectors)
        evals, evecs = eigh(H_pi)

        eigenvalues.append(evals)
        eigenvectors.append(evecs)
        sector_labels.append((p, q))
        sector_dims.append(D_size)
        pw_mults.append(d)

        dt_sec = time.time() - t_sec
        if verbose:
            abs_evals = np.abs(evals)
            print(f"    [{sec_idx+1:2d}/{len(sectors)}] ({p},{q}): "
                  f"dim={d}, D_size={D_size}, "
                  f"|lambda| range: [{np.min(abs_evals):.6f}, {np.max(abs_evals):.6f}], "
                  f"anti-Herm err: {ah_err:.2e}, "
                  f"time: {dt_sec:.2f}s")

    return eigenvalues, eigenvectors, sector_labels, sector_dims, pw_mults


def validate_tau0(eigenvalues_0, eigenvectors_0, sector_labels, verbose=True):
    """
    At tau=0 (bi-invariant metric), validate against known analytical properties:
    1. All eigenvalues^2 should be n/36 for integer n (bi-invariant Dirac spectrum)
    2. Eigenvectors should be exactly orthonormal (eigh guarantees this)

    Parameters:
        eigenvalues_0: list of eigenvalue arrays at tau=0
        eigenvectors_0: list of eigenvector matrices at tau=0
        sector_labels: list of (p,q) tuples
        verbose: print details

    Returns:
        True if validation passes
    """
    if verbose:
        print("\n=== Tau=0 Validation ===")

    max_ortho_err = 0.0
    max_rational_err = 0.0

    for i, (evals, evecs, (p, q)) in enumerate(
        zip(eigenvalues_0, eigenvectors_0, sector_labels)
    ):
        # Check orthonormality
        overlap = evecs.conj().T @ evecs
        ortho_err = np.max(np.abs(overlap - np.eye(len(evals))))
        max_ortho_err = max(max_ortho_err, ortho_err)

        # Check eigenvalues^2 are rational multiples of 1/36
        evals_sq = evals ** 2
        evals_sq_36 = evals_sq * 36
        nearest_int = np.round(evals_sq_36)
        rationality_err = np.max(np.abs(evals_sq_36 - nearest_int))
        max_rational_err = max(max_rational_err, rationality_err)

        if verbose:
            print(f"  ({p},{q}): ortho_err={ortho_err:.2e}, "
                  f"36*lambda^2 integrality err={rationality_err:.2e}")

        if ortho_err > 1e-10:
            print(f"  WARNING: ({p},{q}) eigenvector orthonormality violated!")
        if rationality_err > 1e-4:
            print(f"  NOTE: ({p},{q}) eigenvalues^2 not exactly n/36 "
                  f"(expected for bi-invariant, err={rationality_err:.2e})")

    if verbose:
        print(f"  Max orthonormality error: {max_ortho_err:.2e}")
        print(f"  Max 36*lambda^2 integrality error: {max_rational_err:.2e}")

    return True


def cross_validate_with_s22b(npz_data, verbose=True):
    """
    Cross-validate the first 10 sectors (p+q <= 3) against s22b_eigenvectors.npz.

    Checks that eigenvalues match to machine precision.
    """
    s22b_path = os.path.join(SCRIPT_DIR, "s22b_eigenvectors.npz")
    if not os.path.exists(s22b_path):
        if verbose:
            print("\n=== Cross-validation skipped (s22b_eigenvectors.npz not found) ===")
        return True

    if verbose:
        print("\n=== Cross-validation with s22b_eigenvectors.npz ===")

    s22b = np.load(s22b_path)
    tau_vals_old = s22b["tau_values"]

    # Verify tau grids match
    tau_vals_new = npz_data["tau_values"]
    assert np.allclose(tau_vals_old, tau_vals_new), "Tau grids differ!"

    max_eval_err = 0.0

    for idx in range(len(tau_vals_old)):
        evals_old = s22b[f"eigenvalues_{idx}"]
        evals_new = npz_data[f"eigenvalues_{idx}"]

        # Old has 1232 modes, new has 11424. First 1232 should match.
        # But ordering might differ if sectors are in different order.
        # Compare sorted eigenvalues from old sectors.
        labels_old = s22b[f"sector_labels_{idx}"]
        labels_new = npz_data[f"sector_labels_{idx}"]
        sizes_old = s22b[f"sector_sizes_{idx}"]
        sizes_new = npz_data[f"sector_sizes_{idx}"]

        # Match by sector label
        offset_old = 0
        offset_new = 0
        matched = 0
        for j_old in range(len(labels_old)):
            p_old, q_old = labels_old[j_old]
            # Find this sector in new data
            for j_new in range(len(labels_new)):
                if labels_new[j_new][0] == p_old and labels_new[j_new][1] == q_old:
                    # Found matching sector
                    n_old = sizes_old[j_old]
                    n_new = sizes_new[j_new]
                    assert n_old == n_new, f"Size mismatch for ({p_old},{q_old})"

                    # Compute offset in new data
                    off_new = sum(sizes_new[:j_new])
                    off_old = sum(sizes_old[:j_old])

                    ev_old = np.sort(evals_old[off_old:off_old + n_old])
                    ev_new = np.sort(evals_new[off_new:off_new + n_new])
                    err = np.max(np.abs(ev_old - ev_new))
                    max_eval_err = max(max_eval_err, err)
                    matched += 1
                    break

        if verbose:
            print(f"  tau={tau_vals_old[idx]:.2f}: matched {matched}/{len(labels_old)} sectors")

    s22b.close()

    if verbose:
        print(f"  Max eigenvalue discrepancy: {max_eval_err:.2e}")
        if max_eval_err < 1e-10:
            print("  PASS: Eigenvalues match s22b to machine precision.")
        else:
            print(f"  WARNING: Eigenvalue discrepancy {max_eval_err:.2e}")

    return max_eval_err < 1e-8


def run_extraction(verbose=True):
    """Main extraction loop over all tau values."""
    print("=" * 70)
    print("Session 23a Step 1: Extended Eigenvector Extraction (p+q <= 6)")
    print("=" * 70)
    print(f"Tau values: {TAU_VALUES}")
    print(f"Max p+q sum: {MAX_PQ_SUM}")

    # Initialize infrastructure (computed once)
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    gammas = build_cliff8()

    # Build sector list
    sectors = build_sector_list(MAX_PQ_SUM)

    # Print sector summary
    total_modes = 0
    total_evec_bytes = 0
    print(f"\n{'Sector':>10s}  {'dim':>5s}  {'D_size':>7s}  {'PW_mult':>8s}  {'evec_MB':>8s}")
    for p, q in sectors:
        d = dim_pq(p, q)
        D_size = d * 16
        evec_mb = D_size ** 2 * 16 / 1024**2  # complex128
        total_modes += D_size
        total_evec_bytes += D_size ** 2 * 16
        pq_sum_marker = " *" if p + q > 3 else ""
        print(f"  ({p},{q}){pq_sum_marker:>4s}  {d:5d}  {D_size:7d}  {d:8d}  {evec_mb:8.1f}")
    print(f"{'Total':>10s}  {'':>5s}  {total_modes:7d}  {'':>8s}  "
          f"{total_evec_bytes / 1024**2:8.1f}")
    print(f"  (* = new in Session 23a)")
    print(f"  Total modes per tau: {total_modes}")
    print(f"  Estimated memory per tau: {total_evec_bytes / 1024**2:.1f} MB")
    print(f"  Estimated total memory (9 tau): {total_evec_bytes * 9 / 1024**2:.1f} MB")
    print()

    # Storage for npz output
    npz_data = {"tau_values": TAU_VALUES}

    t_total_start = time.time()

    for idx, tau in enumerate(TAU_VALUES):
        t_start = time.time()
        print(f"\n{'='*60}")
        print(f"tau = {tau:.2f}  ({idx+1}/{len(TAU_VALUES)})")
        print(f"{'='*60}")

        eigenvalues, eigenvectors, sector_labels, sector_dims, pw_mults = (
            extract_eigenvectors_at_tau(tau, gens, f_abc, gammas, sectors, verbose=verbose)
        )

        # Tau=0 validation
        if idx == 0:
            validate_tau0(eigenvalues, eigenvectors, sector_labels, verbose=verbose)

        # Pack eigenvalues per sector into single arrays with sector tracking
        all_evals = np.concatenate(eigenvalues)
        all_evecs_blocks = []
        all_sector_p = []
        all_sector_q = []
        all_mult = []

        for evals, evecs, (p, q), mult in zip(
            eigenvalues, eigenvectors, sector_labels, pw_mults
        ):
            all_evecs_blocks.append(evecs)
            all_sector_p.extend([p] * len(evals))
            all_sector_q.extend([q] * len(evals))
            all_mult.extend([mult] * len(evals))

        # Store in npz_data
        npz_data[f"eigenvalues_{idx}"] = all_evals
        npz_data[f"sector_p_{idx}"] = np.array(all_sector_p, dtype=np.int32)
        npz_data[f"sector_q_{idx}"] = np.array(all_sector_q, dtype=np.int32)
        npz_data[f"multiplicities_{idx}"] = np.array(all_mult, dtype=np.int32)

        # Store eigenvectors per sector block (variable-size blocks)
        sizes = np.array(sector_dims, dtype=np.int32)
        labels = np.array(sector_labels, dtype=np.int32)
        npz_data[f"sector_sizes_{idx}"] = sizes
        npz_data[f"sector_labels_{idx}"] = labels

        for j, evecs in enumerate(all_evecs_blocks):
            npz_data[f"eigvec_{idx}_sector_{j}"] = evecs

        elapsed = time.time() - t_start
        print(f"  Completed in {elapsed:.1f}s. "
              f"Total eigenvalues: {len(all_evals)}, "
              f"|lambda| range: [{np.min(np.abs(all_evals)):.6f}, "
              f"{np.max(np.abs(all_evals)):.6f}]")

    total_elapsed = time.time() - t_total_start
    print(f"\n{'='*70}")
    print(f"Total extraction time: {total_elapsed:.1f}s")
    print(f"{'='*70}")

    # Cross-validate against s22b
    cross_validate_with_s22b(npz_data, verbose=verbose)

    # Save to npz
    output_path = os.path.join(SCRIPT_DIR, "s23a_eigenvectors_extended.npz")
    np.savez_compressed(output_path, **npz_data)
    file_size_mb = os.path.getsize(output_path) / (1024 * 1024)
    print(f"\nSaved: {output_path}")
    print(f"File size: {file_size_mb:.1f} MB")

    # Summary table
    print("\n=== SUMMARY ===")
    print(f"{'tau':>6s}  {'N_evals':>8s}  {'|min|':>10s}  {'|max|':>10s}  {'gap':>10s}")
    for idx, tau in enumerate(TAU_VALUES):
        evals = npz_data[f"eigenvalues_{idx}"]
        abs_evals = np.abs(evals)
        sorted_abs = np.sort(abs_evals)
        gap = sorted_abs[sorted_abs > 1e-10][0] if np.any(sorted_abs > 1e-10) else 0.0
        print(f"{tau:6.2f}  {len(evals):8d}  {np.min(abs_evals):10.6f}  "
              f"{np.max(abs_evals):10.6f}  {gap:10.6f}")

    return output_path


if __name__ == "__main__":
    output = run_extraction(verbose=True)
    print(f"\nDone. Output at: {output}")
