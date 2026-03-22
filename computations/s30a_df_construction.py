"""
Session 30Aa Steps 2-3: D_F Construction from [D_K, L_{e_a}] Commutator

Constructs the finite Dirac operator D_F(tau) via Baptista's Approach B:

    D_F_{alpha,beta} = sum_{a in C^2} <psi_alpha | [D_K, L_{e_a}] | psi_beta>

where L_{e_a} is the Kosmann-Lichnerowicz derivative along the 4 non-Killing
(C^2) directions, and |psi_alpha>, |psi_beta> are eigenstates of D_K.

Mathematical structure:
    On Peter-Weyl sector (p,q), the KL derivative acts as:
        L_{e_a} = rho(e_a) tensor I_{16} + I_{dim_rho} tensor K_a

    where:
        - rho(e_a) = sum_b E_{ab} rho(X_b) is the representation in ON frame
        - K_a is the 16x16 Kosmann spinorial correction (antisymmetric formula)

    The commutator [D_pi, L_{e_a}] is computed directly as a matrix product,
    then projected into the D_K eigenbasis.

    D_F(tau) is the direct sum over sectors of these projected commutator
    matrices, summed over the 4 non-Killing directions.

Key structural fact (Session 22b):
    D_K and L_{e_a} are BOTH block-diagonal in Peter-Weyl. Therefore
    [D_K, L_{e_a}] is also block-diagonal. D_F constructed this way
    has NO inter-sector couplings.

Output: s30a_df_construction.npz with D_F(tau) for tau in [0, 0.50]

Author: phonon-exflation-sim (Session 30Aa)
Date: 2026-03-01

References:
    - Baptista Paper 17, eq 1.3-1.4: [D_K, L_X] formula
    - Session 22b: D_K block-diagonality theorem
    - Session 23a: Kosmann operator (corrected antisymmetric formula)
"""

import sys
import os
import time
import numpy as np
from scipy.linalg import eigh, block_diag

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
    lie_derivative_metric,
    covariant_derivative_lie_metric,
    C2_IDX, U2_IDX,
)

from s23a_kosmann_singlet import kosmann_operator_antisymmetric


# =============================================================================
# TAU VALUES AND CONFIGURATION
# =============================================================================

TAU_VALUES = np.array([0.0, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.50])
MAX_PQ_SUM = 2  # N_max=2: sectors (0,0),(1,0),(0,1),(2,0),(0,2),(1,1); dim=432


# =============================================================================
# STEP 2: Construct L_{e_a} on each Peter-Weyl sector and compute [D_K, L_{e_a}]
# =============================================================================

def construct_lie_derivative_on_sector(rho, E, gammas, Gamma, p, q):
    """
    Construct the Kosmann-Lichnerowicz derivative L_{e_a} as a matrix
    on V_{(p,q)} tensor C^16 for each non-Killing direction a.

    L_{e_a} = rho(e_a) tensor I_{16} + I_{dim_rho} tensor (omega_a + K_a)

    where rho(e_a) = sum_b E_{ab} rho(X_b) is the representation of
    the ON frame vector e_a, omega_a is the spin connection 1-form
    along e_a, and K_a is the Kosmann correction.

    Args:
        rho: list of 8 representation matrices (dim_rho x dim_rho)
             in the ORIGINAL basis {X_b}
        E: (8,8) orthonormal frame matrix, e_a = E_{ab} X_b
        gammas: list of 8 Clifford generators (16x16)
        Gamma: (8,8,8) connection coefficients
        p, q: irrep labels (for labeling only)

    Returns:
        L_ops: dict mapping direction a -> (dim_total, dim_total) complex matrix
               Only for non-Killing directions a in C2_IDX
        K_ops: dict mapping direction a -> (16, 16) complex Kosmann matrix
    """
    dim_rho = rho[0].shape[0]
    dim_spin = 16
    dim_total = dim_rho * dim_spin

    L_ops = {}
    K_ops = {}

    for a in C2_IDX:
        # 1. Representation of e_a in ON frame: rho(e_a) = sum_b E_{ab} rho(X_b)
        rho_ea = np.zeros((dim_rho, dim_rho), dtype=complex)
        for b in range(8):
            if abs(E[a, b]) > 1e-15:
                rho_ea += E[a, b] * rho[b]

        # 2. Kosmann operator K_a (16x16 spinor matrix)
        K_a, A_antisym = kosmann_operator_antisymmetric(Gamma, gammas, a)
        K_ops[a] = K_a

        # 3. Spin connection 1-form along e_a (ON frame direction a):
        #    omega_a = (1/4) sum_{b,c} Gamma^b_{ac} gamma_b gamma_c
        #    Convention: Gamma[b, a, c] = Gamma^b_{ac} (upper, nabla_dir, vector)
        omega_a = np.zeros((dim_spin, dim_spin), dtype=complex)
        for b in range(8):
            for c in range(8):
                coeff = Gamma[b, a, c]
                if abs(coeff) > 1e-15:
                    omega_a += coeff * (gammas[b] @ gammas[c])
        omega_a *= 0.25

        # 4. L_{e_a} = rho(e_a) tensor I_{16} + I_{dim_rho} tensor (omega_a + K_a)
        L_a = np.kron(rho_ea, np.eye(dim_spin, dtype=complex))
        L_a += np.kron(np.eye(dim_rho, dtype=complex), omega_a + K_a)

        L_ops[a] = L_a

    return L_ops, K_ops


def compute_commutator_in_eigenbasis(D_pi, L_ops, evecs, evals):
    """
    Compute [D_pi, L_{e_a}] for each non-Killing direction and project
    into the D_K eigenbasis.

    The commutator matrix in the eigenbasis is:
        C^a_{nm} = <psi_n | [D_pi, L_{e_a}] | psi_m>
                 = sum_k (evecs^dag @ (D_pi @ L_a - L_a @ D_pi) @ evecs)_{nm}

    This is the core ingredient of D_F.

    Args:
        D_pi: (dim, dim) anti-Hermitian Dirac matrix on sector
        L_ops: dict a -> (dim, dim) L_{e_a} matrix
        evecs: (dim, dim) unitary, columns = eigenvectors of 1j*D_pi
        evals: (dim,) real eigenvalues of 1j*D_pi

    Returns:
        comm_eig: dict a -> (dim, dim) complex commutator in eigenbasis
        comm_raw: dict a -> (dim, dim) complex commutator in original basis
    """
    dim = D_pi.shape[0]
    comm_eig = {}
    comm_raw = {}

    for a, L_a in L_ops.items():
        # [D_pi, L_{e_a}] in original basis
        C_raw = D_pi @ L_a - L_a @ D_pi
        comm_raw[a] = C_raw

        # Project into eigenbasis
        C_eig = evecs.conj().T @ C_raw @ evecs
        comm_eig[a] = C_eig

    return comm_eig, comm_raw


def assemble_df_sector(comm_eig_all, dim):
    """
    Assemble D_F on a single sector by summing commutator contributions
    over non-Killing directions.

    D_F^{sector}_{nm} = sum_{a in C^2} C^a_{nm}

    Args:
        comm_eig_all: dict a -> (dim, dim) commutator in eigenbasis
        dim: expected dimension

    Returns:
        D_F_sector: (dim, dim) complex matrix
    """
    D_F_sector = np.zeros((dim, dim), dtype=complex)
    for a in C2_IDX:
        if a in comm_eig_all:
            D_F_sector += comm_eig_all[a]
    return D_F_sector


# =============================================================================
# STEP 3: Assemble full D_F on truncated Hilbert space
# =============================================================================

def assemble_full_df(tau, gens, f_abc, gammas, max_pq_sum=MAX_PQ_SUM, verbose=True):
    """
    Assemble D_F(tau) on the truncated Hilbert space.

    The truncated space is:
        H_trunc = bigoplus_{p+q <= N_max} V_{(p,q)} tensor C^16

    For N_max=2: dim = (1+3+3+6+6+8)*16 = 432

    D_F is block-diagonal in Peter-Weyl (proven in Session 22b).
    Within each sector, D_F = sum_{a in C^2} [D_pi, L_{e_a}] projected
    into the D_K eigenbasis.

    Args:
        tau: Jensen deformation parameter
        gens: SU(3) generators
        f_abc: structure constants
        gammas: Clifford generators
        max_pq_sum: truncation level
        verbose: print details

    Returns:
        D_F: (dim_trunc, dim_trunc) complex matrix in D_K eigenbasis
        D_K_diag: (dim_trunc,) real diagonal of D_K in eigenbasis
                  (eigenvalues of 1j*D, so Dirac eigenvalues are -1j*D_K_diag)
        sector_info: list of dicts with per-sector details
        gamma_F: (dim_trunc, dim_trunc) chirality operator in eigenbasis
        infra: geometric infrastructure dict
    """
    if verbose:
        print(f"\n  Assembling D_F at tau={tau:.2f}...")

    # Step 0: Get eigenvectors and infrastructure
    sector_data, infra = collect_spectrum_with_eigenvectors(
        tau, gens, f_abc, gammas, max_pq_sum=max_pq_sum, verbose=verbose
    )
    E = infra['E']
    Gamma = infra['Gamma']

    # Build chirality operator gamma_9 = gamma_1 ... gamma_8
    gamma9 = build_chirality(gammas)

    # Track sector ordering and dimensions for block assembly
    sector_blocks_df = []
    sector_blocks_dk = []
    sector_blocks_chirality = []
    sector_info = []
    total_dim = 0

    for sd in sector_data:
        p, q = sd['p'], sd['q']
        dim_rho = sd['dim_rho']
        dim_sector = dim_rho * 16
        evals = sd['evals']
        evecs = sd['evecs']
        D_pi = sd['D_pi']

        if verbose:
            print(f"    Sector ({p},{q}): dim_rho={dim_rho}, dim_sector={dim_sector}")

        # Get representation matrices
        if (p, q) == (0, 0):
            rho = [np.zeros((1, 1), dtype=complex) for _ in range(8)]
        else:
            rho, _ = get_irrep(p, q, gens, f_abc)

        # Step 2a: Construct L_{e_a} on this sector
        L_ops, K_ops = construct_lie_derivative_on_sector(rho, E, gammas, Gamma, p, q)

        # Step 2b: Compute [D_pi, L_{e_a}] in eigenbasis
        comm_eig, comm_raw = compute_commutator_in_eigenbasis(D_pi, L_ops, evecs, evals)

        # Step 3a: Sum over non-Killing directions
        D_F_sector = assemble_df_sector(comm_eig, dim_sector)

        # D_K in eigenbasis is diagonal with eigenvalues evals (of 1j*D)
        # The actual Dirac eigenvalues are lambda_n = -1j * evals[n]
        D_K_sector = np.diag(evals)

        # Chirality in eigenbasis: gamma_F = evecs^dag @ (I_rho tensor gamma9) @ evecs
        gamma_F_full = np.kron(np.eye(dim_rho, dtype=complex), gamma9)
        gamma_F_eig = evecs.conj().T @ gamma_F_full @ evecs

        # Validate: gamma_F should be Hermitian involution
        inv_err = np.max(np.abs(gamma_F_eig @ gamma_F_eig - np.eye(dim_sector)))
        herm_err = np.max(np.abs(gamma_F_eig - gamma_F_eig.conj().T))

        # Commutator diagnostics
        comm_norms = {a: np.sqrt(np.sum(np.abs(comm_eig[a])**2))
                      for a in comm_eig}
        df_norm = np.sqrt(np.sum(np.abs(D_F_sector)**2))

        # Check anti-commutation of D_F with gamma_F
        # D_F should anti-commute with chirality: {D_F, gamma_F} = 0
        anticomm = D_F_sector @ gamma_F_eig + gamma_F_eig @ D_F_sector
        anticomm_err = np.max(np.abs(anticomm))

        # Check Hermiticity of D_F
        df_herm_err = np.max(np.abs(D_F_sector - D_F_sector.conj().T))

        # Check anti-Hermiticity of D_F (it might be anti-Hermitian like D_K)
        df_aherm_err = np.max(np.abs(D_F_sector + D_F_sector.conj().T))

        if verbose:
            print(f"      ||D_F||={df_norm:.6e}, "
                  f"{{{('D_F,gamma_F')}}}={anticomm_err:.2e}")
            print(f"      D_F Herm err={df_herm_err:.2e}, "
                  f"anti-Herm err={df_aherm_err:.2e}")
            print(f"      gamma_F: inv_err={inv_err:.2e}, herm_err={herm_err:.2e}")
            for a in sorted(comm_norms):
                print(f"      ||[D,L_{a}]||={comm_norms[a]:.6e}")

        sector_blocks_df.append(D_F_sector)
        sector_blocks_dk.append(evals)
        sector_blocks_chirality.append(gamma_F_eig)

        sector_info.append({
            'p': p, 'q': q, 'dim_rho': dim_rho,
            'dim_sector': dim_sector,
            'df_norm': df_norm,
            'anticomm_err': anticomm_err,
            'df_herm_err': df_herm_err,
            'df_aherm_err': df_aherm_err,
            'gamma_F_inv_err': inv_err,
            'comm_norms': comm_norms,
            'evals': evals,
        })

        total_dim += dim_sector

    # Assemble block-diagonal D_F
    D_F = block_diag(*sector_blocks_df)
    D_K_diag = np.concatenate(sector_blocks_dk)
    gamma_F = block_diag(*sector_blocks_chirality)

    if verbose:
        print(f"\n  Total truncated dimension: {total_dim}")
        print(f"  D_F shape: {D_F.shape}")
        print(f"  ||D_F|| total: {np.sqrt(np.sum(np.abs(D_F)**2)):.6e}")

        # Global chirality anti-commutation
        global_anticomm = D_F @ gamma_F + gamma_F @ D_F
        global_anticomm_err = np.max(np.abs(global_anticomm))
        print(f"  Global {{D_F, gamma_F}} err: {global_anticomm_err:.2e}")

    return D_F, D_K_diag, sector_info, gamma_F, infra


# =============================================================================
# MAIN COMPUTATION: D_F AT MULTIPLE TAU VALUES
# =============================================================================

def run_df_construction():
    """Main computation: D_F(tau) at all tau values."""
    print("=" * 70)
    print("Session 30Aa: D_F Construction via [D_K, L_{e_a}] Commutator")
    print("=" * 70)
    print(f"Tau values: {TAU_VALUES}")
    print(f"N_max = {MAX_PQ_SUM}")
    print(f"Sectors: (0,0),(1,0),(0,1),(2,0),(0,2),(1,1)")
    print(f"Expected dimension: (1+3+3+6+6+8)*16 = 432")
    print()

    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    gammas = build_cliff8()

    cliff_err = validate_clifford(gammas)
    print(f"Clifford validation: max_err = {cliff_err:.2e}")

    # Storage for all tau values
    npz_data = {"tau_values": TAU_VALUES, "max_pq_sum": MAX_PQ_SUM}
    results = []

    t_total = time.time()

    for idx, tau in enumerate(TAU_VALUES):
        t_start = time.time()
        print(f"\n{'='*60}")
        print(f"tau = {tau:.2f}  ({idx+1}/{len(TAU_VALUES)})")
        print(f"{'='*60}")

        D_F, D_K_diag, sector_info, gamma_F, infra = assemble_full_df(
            tau, gens, f_abc, gammas, max_pq_sum=MAX_PQ_SUM, verbose=True
        )

        elapsed = time.time() - t_start

        # Store results
        npz_data[f"D_F_{idx}"] = D_F
        npz_data[f"D_K_diag_{idx}"] = D_K_diag
        npz_data[f"gamma_F_{idx}"] = gamma_F

        # Summary
        df_norm = np.sqrt(np.sum(np.abs(D_F)**2))
        dk_norm = np.sqrt(np.sum(D_K_diag**2))

        # Chirality anti-commutation
        anticomm = D_F @ gamma_F + gamma_F @ D_F
        anticomm_err = np.max(np.abs(anticomm))

        # D_F eigenvalues (it's block-diagonal and complex)
        # For diagnostic: eigenvalues of the Hermitian part
        D_F_herm = 0.5 * (D_F + D_F.conj().T)
        D_F_aherm = 0.5 * (D_F - D_F.conj().T)
        herm_norm = np.sqrt(np.sum(np.abs(D_F_herm)**2))
        aherm_norm = np.sqrt(np.sum(np.abs(D_F_aherm)**2))

        # D_F eigenvalues (using eigh if Hermitian, eigvals otherwise)
        df_evals = np.linalg.eigvals(D_F)
        df_evals_sorted = np.sort(np.abs(df_evals))

        # Spectral gap of D_F
        df_gap = df_evals_sorted[0] if len(df_evals_sorted) > 0 else 0.0
        # Number of near-zero eigenvalues
        n_zero = np.sum(np.abs(df_evals) < 1e-10)

        # Scale comparison: ||D_F|| / ||D_K||
        scale_ratio = df_norm / dk_norm if dk_norm > 0 else float('inf')

        print(f"\n  SUMMARY at tau={tau:.2f}:")
        print(f"    ||D_F|| = {df_norm:.6e}")
        print(f"    ||D_K|| = {dk_norm:.6e}")
        print(f"    ||D_F||/||D_K|| = {scale_ratio:.4f}")
        print(f"    {{D_F, gamma_F}} = {anticomm_err:.2e}")
        print(f"    D_F Hermitian norm = {herm_norm:.6e}")
        print(f"    D_F anti-Hermitian norm = {aherm_norm:.6e}")
        print(f"    D_F spectral gap: {df_gap:.6e}")
        print(f"    D_F near-zero modes: {n_zero}")
        print(f"    D_F |eigenvalue| range: [{df_evals_sorted[0]:.6e}, {df_evals_sorted[-1]:.6e}]")
        print(f"    Time: {elapsed:.2f}s")

        results.append({
            'tau': tau,
            'df_norm': df_norm,
            'dk_norm': dk_norm,
            'scale_ratio': scale_ratio,
            'anticomm_err': anticomm_err,
            'df_gap': df_gap,
            'n_zero': n_zero,
            'df_evals_range': (df_evals_sorted[0], df_evals_sorted[-1]),
            'sector_info': sector_info,
        })

    total_elapsed = time.time() - t_total

    # ================================================================
    # SUMMARY TABLE
    # ================================================================
    print(f"\n{'='*70}")
    print("D_F CONSTRUCTION SUMMARY")
    print(f"{'='*70}")
    print(f"{'tau':>6s}  {'||D_F||':>12s}  {'||D_K||':>12s}  {'ratio':>8s}  "
          f"{'{{D_F,g_F}}':>10s}  {'gap':>12s}  {'n_zero':>6s}")
    for r in results:
        print(f"{r['tau']:6.2f}  {r['df_norm']:12.6e}  {r['dk_norm']:12.6e}  "
              f"{r['scale_ratio']:8.4f}  {r['anticomm_err']:10.2e}  "
              f"{r['df_gap']:12.6e}  {r['n_zero']:6d}")

    print(f"\nTotal computation time: {total_elapsed:.1f}s")

    # ================================================================
    # GATE CLASSIFICATION
    # ================================================================
    print(f"\n{'='*70}")
    print("GATE CLASSIFICATION")
    print(f"{'='*70}")

    # B-30b: D_F construction fails?
    max_anticomm = max(r['anticomm_err'] for r in results)
    all_norms_finite = all(np.isfinite(r['df_norm']) for r in results)
    any_nan = any(not np.isfinite(r['df_norm']) for r in results)

    if any_nan or max_anticomm > 1.0:
        print("  B-30b: FIRES — D_F construction numerically unstable")
        print(f"         max {{D_F, gamma_F}} = {max_anticomm:.2e}")
    else:
        print(f"  B-30b: DOES NOT FIRE — D_F constructed at all tau values")
        print(f"         max {{D_F, gamma_F}} = {max_anticomm:.2e}")
        if max_anticomm > 1e-5:
            print(f"         NOTE: chirality anti-commutation has large error")
            print(f"         D_F is NOT chirally graded to high precision")

    # Diagnostic: D_F scale relative to D_K
    print(f"\n  D_F/D_K scale ratio across tau:")
    for r in results:
        marker = " <-- comparable" if r['scale_ratio'] > 0.1 else ""
        print(f"    tau={r['tau']:.2f}: {r['scale_ratio']:.4f}{marker}")

    # Save
    output_path = os.path.join(SCRIPT_DIR, "s30a_df_construction.npz")
    np.savez_compressed(output_path, **npz_data)
    file_size_mb = os.path.getsize(output_path) / (1024 * 1024)
    print(f"\nSaved: {output_path}")
    print(f"File size: {file_size_mb:.1f} MB")

    return output_path, results


if __name__ == "__main__":
    output, results = run_df_construction()
    print(f"\nDone. Output at: {output}")
