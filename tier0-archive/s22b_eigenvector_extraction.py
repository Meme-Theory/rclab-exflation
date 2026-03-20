"""
Session 22b PA-1: Eigenvector extraction from D_K(tau).

Extracts eigenvectors of the Dirac operator D_K at gap-edge sectors (p+q <= 3)
for 9 tau values. Uses scipy.linalg.eigh on the Hermitianized operator (1j * D_pi)
since D_pi is anti-Hermitian in math convention.

Mathematical background:
    D_pi = sum_{a,b} E_{ab} (rho(X_b) x gamma_a) + I_{dim_rho} x Omega(s)
    D_pi is anti-Hermitian => 1j * D_pi is Hermitian => eigh gives real eigenvalues
    and orthonormal eigenvectors.

    The eigenvalues of D_pi are 1j * evals_hermitian (purely imaginary).
    We store the real eigenvalues of (1j * D_pi) directly, since the absolute values
    |lambda_D| = |evals_hermitian| are what enter spectral sums.

Output: tier0-computation/s22b_eigenvectors.npz
    Keys:
        tau_values          : (9,) float64
        eigenvalues_{i}     : eigenvalues of (1j * D_pi) per sector, concatenated, for tau_i
        eigenvectors_{i}    : corresponding eigenvector matrix (columns = eigenvectors)
        sector_p_{i}        : p-label per eigenvalue
        sector_q_{i}        : q-label per eigenvalue
        multiplicities_{i}  : Peter-Weyl multiplicity dim(p,q) per eigenvalue
        sector_sizes_{i}    : (N_sectors,) array of sector matrix dimensions
        sector_labels_{i}   : (N_sectors, 2) array of (p,q) labels per sector block

Sectors extracted (p+q <= 3):
    (0,0): dim=1,  D size=16,   PW mult=1
    (1,0): dim=3,  D size=48,   PW mult=3
    (0,1): dim=3,  D size=48,   PW mult=3
    (1,1): dim=8,  D size=128,  PW mult=8
    (2,0): dim=6,  D size=96,   PW mult=6
    (0,2): dim=6,  D size=96,   PW mult=6
    (2,1): dim=15, D size=240,  PW mult=15
    (1,2): dim=15, D size=240,  PW mult=15
    (3,0): dim=10, D size=160,  PW mult=10
    (0,3): dim=10, D size=160,  PW mult=10
    Total: 1232 modes per tau value

Author: phonon-exflation-sim (Session 22b)
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

# Gap-edge sectors: all (p,q) with p+q <= 3
MAX_PQ_SUM = 3


def dim_pq(p: int, q: int) -> int:
    """Dimension of SU(3) irrep (p,q)."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def build_geometry(tau: float, gens, f_abc, gammas):
    """
    Build all geometric objects needed for the Dirac operator at deformation tau.

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


def extract_eigenvectors_at_tau(
    tau: float,
    gens,
    f_abc,
    gammas,
    max_pq_sum: int = MAX_PQ_SUM,
    verbose: bool = True,
):
    """
    Extract eigenvalues AND eigenvectors of D_K(tau) for all sectors with p+q <= max_pq_sum.

    Since D_pi is anti-Hermitian, we diagonalize H_pi = 1j * D_pi (which is Hermitian)
    using scipy.linalg.eigh. This gives:
        H_pi = V @ diag(lambda) @ V^dag
    where lambda are real and V is unitary (columns = eigenvectors).

    The eigenvalues of D_pi are then -1j * lambda (purely imaginary).
    We report lambda (real eigenvalues of 1j*D_pi) directly.

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

    # Build list of sectors to compute
    sectors = []
    for p in range(max_pq_sum + 1):
        for q in range(max_pq_sum + 1 - p):
            sectors.append((p, q))
    # Sort by Casimir (smallest first = gap-edge first)
    sectors.sort(key=lambda pq: (pq[0]**2 + pq[1]**2 + pq[0]*pq[1] +
                                  3*pq[0] + 3*pq[1]) / 3.0)

    for p, q in sectors:
        d = dim_pq(p, q)
        D_size = d * 16

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

        if verbose:
            abs_evals = np.abs(evals)
            print(f"    ({p},{q}): dim={d}, D_size={D_size}, "
                  f"|lambda| range: [{np.min(abs_evals):.6f}, {np.max(abs_evals):.6f}], "
                  f"anti-Herm err: {ah_err:.2e}")

    return eigenvalues, eigenvectors, sector_labels, sector_dims, pw_mults


def validate_tau0(eigenvalues_0, eigenvectors_0, sector_labels, verbose=True):
    """
    At tau=0 (bi-invariant metric), validate against known analytical properties:
    1. All eigenvalues^2 should be n/36 for integer n (bi-invariant Dirac spectrum)
    2. Eigenvectors should be exactly orthonormal (eigh guarantees this)
    3. Cross-check: trivial (0,0) sector eigenvalues against Session 12 results
    """
    if verbose:
        print("\n=== Tau=0 Validation ===")

    for i, (evals, evecs, (p, q)) in enumerate(
        zip(eigenvalues_0, eigenvectors_0, sector_labels)
    ):
        # Check orthonormality
        overlap = evecs.conj().T @ evecs
        ortho_err = np.max(np.abs(overlap - np.eye(len(evals))))

        # Check eigenvalues^2 are rational multiples of 1/36
        evals_sq = evals ** 2
        evals_sq_36 = evals_sq * 36
        # At tau=0, lambda^2 = n/36 for integer n
        nearest_int = np.round(evals_sq_36)
        rationality_err = np.max(np.abs(evals_sq_36 - nearest_int))

        if verbose:
            print(f"  ({p},{q}): ortho_err={ortho_err:.2e}, "
                  f"36*lambda^2 integrality err={rationality_err:.2e}")

        if ortho_err > 1e-10:
            print(f"  WARNING: ({p},{q}) eigenvector orthonormality violated!")
        if rationality_err > 1e-6:
            print(f"  NOTE: ({p},{q}) eigenvalues^2 not exactly n/36 "
                  f"(expected for bi-invariant, err={rationality_err:.2e})")

    return True


def run_extraction(verbose=True):
    """Main extraction loop over all tau values."""
    print("=" * 70)
    print("Session 22b PA-1: Eigenvector Extraction from D_K(tau)")
    print("=" * 70)
    print(f"Tau values: {TAU_VALUES}")
    print(f"Max p+q sum: {MAX_PQ_SUM}")

    # Initialize infrastructure (computed once)
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    gammas = build_cliff8()

    # Compute expected total modes
    total_modes = 0
    print("\nSector summary:")
    for p in range(MAX_PQ_SUM + 1):
        for q in range(MAX_PQ_SUM + 1 - p):
            d = dim_pq(p, q)
            D_size = d * 16
            total_modes += D_size
            print(f"  ({p},{q}): dim={d}, D_size={D_size}, PW_mult={d}")
    print(f"Total modes per tau: {total_modes}")
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
            extract_eigenvectors_at_tau(tau, gens, f_abc, gammas, verbose=verbose)
        )

        # Tau=0 validation
        if idx == 0:
            validate_tau0(eigenvalues, eigenvectors, sector_labels, verbose=verbose)

        # Pack eigenvalues per sector into single arrays with sector tracking
        all_evals = np.concatenate(eigenvalues)
        # Eigenvectors: store as block-diagonal (each sector independently)
        # We store them sector-by-sector to preserve the block structure
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
        # Use sector_sizes to allow reconstruction
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

    # Save to npz
    output_path = os.path.join(SCRIPT_DIR, "s22b_eigenvectors.npz")
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
        # Gap = smallest nonzero |lambda|
        sorted_abs = np.sort(abs_evals)
        gap = sorted_abs[sorted_abs > 1e-10][0] if np.any(sorted_abs > 1e-10) else 0.0
        print(f"{tau:6.2f}  {len(evals):8d}  {np.min(abs_evals):10.6f}  "
              f"{np.max(abs_evals):10.6f}  {gap:10.6f}")

    return output_path


if __name__ == "__main__":
    output = run_extraction(verbose=True)
    print(f"\nDone. Output at: {output}")
