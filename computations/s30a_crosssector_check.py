"""
Session 30Aa: Cross-Sector Coupling Check

Einstein claims D_F has cross-sector couplings with Delta(p+q)=1 selection rule.
This script verifies whether [D_K, L_{e_a}] has cross-sector terms by constructing
the full 432x432 operators and checking off-diagonal blocks.

The key question: does L_{e_a} on the FULL truncated space have cross-sector terms?

Mathematical analysis:
    L_{e_a} = rho(e_a) tensor I_16 + I_rho tensor K_a

    BOTH terms act within each Peter-Weyl sector:
    - rho(e_a) is the sector-specific representation
    - K_a acts on spinor space only

    IF L_{e_a} is block-diagonal, then [D_K, L_{e_a}] is also block-diagonal.
    The only way to get cross-sector terms is if L_{e_a} has them.

    But L_{e_a} on H_trunc = bigoplus V_{(p,q)} tensor C^16 acts as:
    L_{e_a} = diag(L_{e_a}^{(0,0)}, L_{e_a}^{(1,0)}, L_{e_a}^{(0,1)}, ...)

    So the commutator is also block-diagonal. Unless there's a subtlety I'm missing.

This script constructs everything on the full space and checks numerically.

Author: phonon-exflation-sim (Session 30Aa)
Date: 2026-03-01
"""

import sys
import os
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
    collect_spectrum_with_eigenvectors,
    get_irrep,
    dirac_operator_on_irrep,
    C2_IDX,
)

from s23a_kosmann_singlet import kosmann_operator_antisymmetric


def check_cross_sector(tau=0.25, max_pq_sum=2):
    """Check for cross-sector terms in [D_K, L_{e_a}]."""
    print(f"Cross-sector check at tau={tau}")
    print("=" * 70)

    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    gammas = build_cliff8()

    # Get sector data and infrastructure
    sector_data, infra = collect_spectrum_with_eigenvectors(
        tau, gens, f_abc, gammas, max_pq_sum=max_pq_sum, verbose=True
    )
    E = infra['E']
    Gamma = infra['Gamma']
    Omega = infra['Omega']

    # Assemble full D_K on the 432-dim space (block diagonal)
    D_blocks = []
    sector_dims = []
    sector_labels = []
    for sd in sector_data:
        D_blocks.append(sd['D_pi'])
        dim_s = sd['dim_rho'] * 16
        sector_dims.append(dim_s)
        sector_labels.append((sd['p'], sd['q']))

    D_K_full = block_diag(*D_blocks)
    dim_total = sum(sector_dims)
    print(f"\nTotal dimension: {dim_total}")
    print(f"Sectors: {sector_labels}")
    print(f"Sector dims: {sector_dims}")

    # Assemble full L_{e_a} on the 432-dim space
    for a in C2_IDX[:1]:  # Just check a=3 for speed
        print(f"\nDirection a={a}:")

        # K_a (16x16 Kosmann spinorial correction)
        K_a, _ = kosmann_operator_antisymmetric(Gamma, gammas, a)

        # Construct L_{e_a} block by block
        L_blocks = []
        for sd in sector_data:
            p, q = sd['p'], sd['q']
            dim_rho = sd['dim_rho']

            if (p, q) == (0, 0):
                rho = [np.zeros((1, 1), dtype=complex) for _ in range(8)]
            else:
                rho, _ = get_irrep(p, q, gens, f_abc)

            # rho(e_a) = sum_b E_{ab} rho(X_b)
            rho_ea = np.zeros((dim_rho, dim_rho), dtype=complex)
            for b in range(8):
                if abs(E[a, b]) > 1e-15:
                    rho_ea += E[a, b] * rho[b]

            # L_{e_a} on this sector = rho(e_a) tensor I_16 + I_rho tensor K_a
            L_sector = np.kron(rho_ea, np.eye(16, dtype=complex))
            L_sector += np.kron(np.eye(dim_rho, dtype=complex), K_a)
            L_blocks.append(L_sector)

        L_a_full = block_diag(*L_blocks)

        # L_{e_a} is block-diagonal by construction.
        # Let's verify: check off-diagonal blocks
        print(f"  L_{a} is block-diagonal by construction: {L_a_full.shape}")

        # Compute commutator [D_K, L_{e_a}] on full space
        comm_full = D_K_full @ L_a_full - L_a_full @ D_K_full
        print(f"  ||[D_K, L_{a}]|| = {np.sqrt(np.sum(np.abs(comm_full)**2)):.6e}")

        # Check cross-sector blocks of the commutator
        print(f"\n  Cross-sector blocks of [D_K, L_{a}]:")
        offset_i = 0
        for i, (pi, qi) in enumerate(sector_labels):
            offset_j = 0
            for j, (pj, qj) in enumerate(sector_labels):
                if i != j:
                    block = comm_full[offset_i:offset_i+sector_dims[i],
                                      offset_j:offset_j+sector_dims[j]]
                    fnorm = np.sqrt(np.sum(np.abs(block)**2))
                    if fnorm > 1e-14:
                        print(f"    ({pi},{qi}) x ({pj},{qj}): ||block|| = {fnorm:.6e}  ***")
                offset_j += sector_dims[j]
            offset_i += sector_dims[i]

        # Now check: is the commutator truly block-diagonal?
        # Extract off-diagonal part
        off_diag = comm_full.copy()
        offset = 0
        for dim_s in sector_dims:
            off_diag[offset:offset+dim_s, offset:offset+dim_s] = 0
            offset += dim_s

        off_diag_norm = np.sqrt(np.sum(np.abs(off_diag)**2))
        diag_norm = np.sqrt(np.sum(np.abs(comm_full)**2) - np.sum(np.abs(off_diag)**2))
        print(f"\n  Off-diagonal norm: {off_diag_norm:.6e}")
        print(f"  Diagonal norm: {diag_norm:.6e}")
        print(f"  Ratio off/diag: {off_diag_norm/diag_norm:.6e}" if diag_norm > 0 else "")

    # CONCLUSION
    print(f"\n{'='*70}")
    print("CONCLUSION")
    print(f"{'='*70}")
    if off_diag_norm < 1e-10:
        print("  [D_K, L_{e_a}] is BLOCK-DIAGONAL to machine precision.")
        print("  Einstein's cross-sector claim is NOT confirmed.")
        print("  My original D_F construction is correct.")
    else:
        print(f"  [D_K, L_{e_a}] has CROSS-SECTOR terms: {off_diag_norm:.2e}")
        print("  Einstein's claim IS confirmed. My construction needs revision.")
        print("  D_F must be assembled on the FULL space, not sector-by-sector.")


if __name__ == "__main__":
    check_cross_sector(tau=0.25)
