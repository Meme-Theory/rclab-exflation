#!/usr/bin/env python3
"""
S63 PS-KASPAROV-63: Pati-Salam Gauge Module Check
=====================================================

Compute [D_K, T_a^PS] for all 9 Pati-Salam generators on the Jensen-deformed
SU(3) background. Verify that all commutators lie within the extended 1-form
space (rank 775 from GAUGE-MODULE-61) or its PS enlargement.

MATHEMATICAL FRAMEWORK
----------------------

The Pati-Salam algebra A_PS = H_L + H_R + M_4(C) extends the SM algebra
A_SM = C + H + M_3(C). The 9 additional PS generators beyond SM are:

  SU(2)_R generators (3):
    - T_{R,1}, T_{R,2}, T_{R,3}: i*sigma_j acting on right-handed sector
    - In the 4x4 bimodule convention, these act on (row 0) as isospin partners
      with (rows 2,3 = SU(2)_L), but flipped to the singlet slot.

  SU(4)/[SU(3)xU(1)] leptoquark generators (6):
    - T_{LQ,a}: mix the 4th color (lepton) with colors 1,2,3 (quarks)
    - 6 generators: 3 complex off-diagonal (a=1..3 color <-> lepton, Re/Im)

For the Kasparov product verification (van den Dungen, Paper 05), we need:

  1. Compute the 1-forms omega_a = [D_K, T_a^PS] for each PS generator T_a
  2. Project each omega_a onto the rank-775 extended bimodule basis
  3. If residual < threshold for ALL 9: PASS (PS gauge module verified)
  4. If any residual > threshold: compute the PS-enlarged 1-form space rank

GATE: PS-KASPAROV-63
  PASS: all 9 commutators in extended 1-form space
  FAIL: any commutator falls outside

Author: Connes NCG Theorist (Session 63, Wave 6)
Date: 2026-03-31
Sources: GAUGE-MODULE-61, S62 PATI-SALAM-EXTENSION-62, VDD-S63-3
"""

import numpy as np
from numpy.linalg import norm as la_norm, svd, matrix_rank
import sys
import os
import time
import traceback

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
from canonical_constants import tau_fold

from s61_gauge_module_check import (
    build_AF_generators, build_DK_fundamental, build_unitary_generators,
    o_map_16, G5, flat_idx, build_bimodule_16, _gell_mann_matrices,
    compute_omega1_space, project_onto_omega1,
)
from s61_gauge_module_extended import (
    compute_extended_omega1_basis, check_bimodule_on_basis, check_gauge_on_basis,
)
from dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    jensen_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients, spinor_connection_offset,
    build_cliff8, build_chirality,
)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

np.set_printoptions(precision=10, linewidth=140, suppress=True)

OUTDIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_NPZ = os.path.join(OUTDIR, "s63_ps_kasparov.npz")
OUTPUT_PNG = os.path.join(OUTDIR, "s63_ps_kasparov.png")


# =============================================================================
# SECTION 1: PATI-SALAM GENERATOR CONSTRUCTION
# =============================================================================

def build_PS_generators():
    """Build the 9 Pati-Salam generators BEYOND the SM on 16-dim Psi_+ space.

    The SM algebra A_SM = C + H + M_3(C) has gauge group U(1) x SU(2)_L x SU(3).
    The PS algebra A_PS = H_L + H_R + M_4(C) has gauge group SU(2)_L x SU(2)_R x SU(4).

    The 9 additional generators are:
      3 x SU(2)_R generators:
        Act on (row 0, row 1) doublet, i.e., the nu_R/e_R and u_R/d_R sectors.
        In the 4x4 left-action convention:
          Row 0 = right-handed singlet (nu_R)
          Row 1 = (not used for SU(2)_L, but is the SU(2)_R partner)

        Actually: In the Connes bimodule on M_4(C), the LEFT action of H_R
        acts on rows (0,1) as the right-handed doublet. H_L acts on (2,3).

      6 x SU(4)/[SU(3)xU(1)] leptoquark generators:
        The SM has M_3(C) acting on columns (1,2,3). SU(4) extends this to
        columns (0,1,2,3) where column 0 = lepton number.
        The 6 extra generators mix column 0 with columns 1,2,3.
        These are the off-diagonal blocks of the fundamental of SU(4).

    Convention:
      16-dim space = M_4(C) bimodule with flat_idx(row, col).
      Rows: 0=singlet(R), 1=(not in SM L), 2,3 = SU(2)_L doublet
      Cols: 0=lepton, 1,2,3 = quark colors

    Returns:
        PS_16: list of 9 (16,16) complex matrices (anti-Hermitian)
        PS_names: list of generator names
        PS_types: list of types ('SU2R' or 'LQ')
    """
    PS_16 = []
    PS_names = []
    PS_types = []

    # ---- SU(2)_R generators ----
    # Act on left index rows (0,1). These are the right-handed doublet.
    # Anti-Hermitian: i * sigma_j / 2

    # sigma_1: rows 0 <-> 1
    L_R1 = np.zeros((4, 4), dtype=complex)
    L_R1[0, 1] = 1j
    L_R1[1, 0] = 1j
    PS_16.append(build_bimodule_16(L_R1, np.eye(4)))
    PS_names.append('su2R_1')
    PS_types.append('SU2R')

    # sigma_2: rows 0 <-> 1 with phase
    L_R2 = np.zeros((4, 4), dtype=complex)
    L_R2[0, 1] = 1.0
    L_R2[1, 0] = -1.0
    PS_16.append(build_bimodule_16(L_R2, np.eye(4)))
    PS_names.append('su2R_2')
    PS_types.append('SU2R')

    # sigma_3: diagonal on (0,1)
    L_R3 = np.zeros((4, 4), dtype=complex)
    L_R3[0, 0] = 1j
    L_R3[1, 1] = -1j
    PS_16.append(build_bimodule_16(L_R3, np.eye(4)))
    PS_names.append('su2R_3')
    PS_types.append('SU2R')

    # ---- SU(4)/[SU(3) x U(1)] leptoquark generators ----
    # These mix column 0 (lepton) with columns 1,2,3 (quarks).
    # In M_4(C), the 15 generators of SU(4) include 8 of SU(3) + 1 of U(1)_{B-L}
    # + 6 leptoquark generators.
    #
    # Leptoquark generators T_a^LQ (a=1..6):
    #   E_{0,c} + E_{c,0} (real parts, c=1,2,3)     -> 3 generators
    #   -i*E_{0,c} + i*E_{c,0} (imag parts, c=1,2,3) -> 3 generators
    #
    # These act on the RIGHT (column index) in the bimodule.
    # Anti-Hermitian: i * (E_{0c} + E_{c0})/2 and (E_{0c} - E_{c0})/2

    for c in range(3):
        # Real part: i*(E_{0,c+1} + E_{c+1,0})/2  [anti-Hermitian]
        R_Re = np.zeros((4, 4), dtype=complex)
        R_Re[0, c+1] = 1j / 2
        R_Re[c+1, 0] = 1j / 2
        # Right action uses R^{T*} in bimodule convention
        PS_16.append(build_bimodule_16(np.eye(4), R_Re.conj().T))
        PS_names.append(f'LQ_{c+1}_Re')
        PS_types.append('LQ')

        # Imag part: (E_{0,c+1} - E_{c+1,0})/2  [anti-Hermitian]
        R_Im = np.zeros((4, 4), dtype=complex)
        R_Im[0, c+1] = 0.5
        R_Im[c+1, 0] = -0.5
        PS_16.append(build_bimodule_16(np.eye(4), R_Im.conj().T))
        PS_names.append(f'LQ_{c+1}_Im')
        PS_types.append('LQ')

    return PS_16, PS_names, PS_types


def build_PS_generators_direct():
    """Build PS generators directly on 16x16 without bimodule convention issues.

    Alternative construction: build the 9 PS generators as explicit 16x16 matrices
    using the flat_idx mapping, to cross-check the bimodule construction.
    """
    PS_16 = []
    PS_names = []
    PS_types = []

    # SU(2)_R: act on left index (row) (0,1)
    # For each column j, the row indices (0,j) and (1,j) should form a doublet.
    # flat_idx(0,j) and flat_idx(1,j) for j=0..3

    # sigma_1: swap rows 0 <-> 1 (with factor i for anti-Hermitian)
    T = np.zeros((16, 16), dtype=complex)
    for j in range(4):
        i0 = flat_idx(0, j)
        i1 = flat_idx(1, j)
        T[i0, i1] = 1j
        T[i1, i0] = 1j
    PS_16.append(T)
    PS_names.append('su2R_1_direct')
    PS_types.append('SU2R')

    # sigma_2
    T = np.zeros((16, 16), dtype=complex)
    for j in range(4):
        i0 = flat_idx(0, j)
        i1 = flat_idx(1, j)
        T[i0, i1] = 1.0
        T[i1, i0] = -1.0
    PS_16.append(T)
    PS_names.append('su2R_2_direct')
    PS_types.append('SU2R')

    # sigma_3
    T = np.zeros((16, 16), dtype=complex)
    for j in range(4):
        i0 = flat_idx(0, j)
        i1 = flat_idx(1, j)
        T[i0, i0] = 1j
        T[i1, i1] = -1j
    PS_16.append(T)
    PS_names.append('su2R_3_direct')
    PS_types.append('SU2R')

    # SU(4)/[SU(3)xU(1)] leptoquark: mix column 0 with columns 1,2,3
    # For each row i, flat_idx(i,0) and flat_idx(i,c) for c=1,2,3 form the mixing
    for c in range(1, 4):
        # Real part: i*(E_{0c} + E_{c0})/2 on column index
        T = np.zeros((16, 16), dtype=complex)
        for row in range(4):
            i_lep = flat_idx(row, 0)
            i_col = flat_idx(row, c)
            T[i_lep, i_col] = 1j / 2
            T[i_col, i_lep] = 1j / 2
        PS_16.append(T)
        PS_names.append(f'LQ_{c}_Re_direct')
        PS_types.append('LQ')

        # Imag part: (E_{0c} - E_{c0})/2 on column index
        T = np.zeros((16, 16), dtype=complex)
        for row in range(4):
            i_lep = flat_idx(row, 0)
            i_col = flat_idx(row, c)
            T[i_lep, i_col] = 0.5
            T[i_col, i_lep] = -0.5
        PS_16.append(T)
        PS_names.append(f'LQ_{c}_Im_direct')
        PS_types.append('LQ')

    return PS_16, PS_names, PS_types


# =============================================================================
# SECTION 2: COMMUTATOR COMPUTATION AND PROJECTION
# =============================================================================

def compute_ps_commutators(D_K, PS_16, dim_rep=3):
    """Compute [D_K, T_a^PS] for all 9 PS generators.

    Args:
        D_K: (n, n) Dirac operator on fundamental sector
        PS_16: list of 9 PS generators (16x16)
        dim_rep: representation dimension (3 for fundamental)

    Returns:
        commutators: list of (n, n) matrices [D_K, T_a^PS]
        norms: array of ||[D_K, T_a^PS]|| for each generator
    """
    n = D_K.shape[0]
    if dim_rep == 1:
        PS_gens = [g.copy() for g in PS_16]
    else:
        PS_gens = [np.kron(np.eye(dim_rep), g) for g in PS_16]

    commutators = []
    norms = []
    for T in PS_gens:
        comm = D_K @ T - T @ D_K
        commutators.append(comm)
        norms.append(la_norm(comm))

    return commutators, np.array(norms)


def project_commutators_onto_basis(commutators, basis):
    """Project each [D_K, T_a^PS] onto the extended 1-form basis.

    Returns:
        residuals: fractional residuals ||[D,T] - proj|| / ||[D,T]||
        projections: list of projected vectors
    """
    residuals = []
    projections = []
    for comm in commutators:
        vec = comm.flatten()
        norm_orig = la_norm(vec)
        if norm_orig < 1e-15:
            residuals.append(0.0)
            projections.append(np.zeros_like(vec))
            continue
        # Project: coeffs = basis @ vec^* (row basis), proj = coeffs^* @ basis
        coeffs = basis @ vec.conj()
        proj = coeffs.conj() @ basis
        resid = la_norm(vec - proj) / norm_orig
        residuals.append(resid)
        projections.append(proj)

    return np.array(residuals), projections


# =============================================================================
# SECTION 3: PS-ENLARGED 1-FORM SPACE
# =============================================================================

def compute_ps_enlarged_omega1(D_K, AF_16, PS_16, dim_rep=3, n_levels=3):
    """Compute the PS-enlarged 1-form space.

    Start with SM Omega^1_D (rank 775 from GAUGE-MODULE-61), add all
    PS generator 1-forms {a_PS [D, b_PS]}, and iteratively close under
    A_PS x A_PS^o multiplication.

    Returns:
        rank_ps: rank of PS-enlarged space
        basis_ps: orthonormal basis
    """
    n = D_K.shape[0]
    all_gens = AF_16 + PS_16  # combined A_PS generators

    if dim_rep == 1:
        A_gens = [g.copy() for g in all_gens]
        opp_gens = [o_map_16(g) for g in all_gens]
    else:
        A_gens = [np.kron(np.eye(dim_rep), g) for g in all_gens]
        opp_gens = [np.kron(np.eye(dim_rep), o_map_16(g)) for g in all_gens]

    n_gen = len(A_gens)

    # Level 0: all 1-forms a [D, b] for a, b in A_PS
    forms_vecs = []
    for i in range(n_gen):
        for j in range(n_gen):
            comm = D_K @ A_gens[j] - A_gens[j] @ D_K
            omega = A_gens[i] @ comm
            forms_vecs.append(omega.flatten())

    def current_rank(vecs):
        if not vecs:
            return 0, None
        mat = np.array(vecs)
        U, S, Vh = svd(mat, full_matrices=False)
        tol = max(mat.shape) * np.finfo(float).eps * S[0] if S[0] > 0 else 1e-14
        r = int(np.sum(S > tol))
        return r, Vh[:r, :]

    r0, basis0 = current_rank(forms_vecs)
    print(f"  PS Level 0: rank = {r0} ({n_gen}^2 = {n_gen**2} generators)")

    prev_rank = r0
    prev_basis_vecs = [v.copy() for v in forms_vecs]

    for level in range(1, n_levels + 1):
        new_vecs = list(prev_basis_vecs)
        r_curr, basis_curr = current_rank(new_vecs)
        basis_mats = [basis_curr[k].reshape(n, n) for k in range(min(r_curr, 60))]

        for k in range(len(basis_mats)):
            omega_k = basis_mats[k]
            for c in range(n_gen):
                new_vecs.append((A_gens[c] @ omega_k).flatten())
                new_vecs.append((omega_k @ A_gens[c]).flatten())
                new_vecs.append((opp_gens[c] @ omega_k).flatten())
                new_vecs.append((omega_k @ opp_gens[c]).flatten())

        r_new, basis_new = current_rank(new_vecs)
        print(f"  PS Level {level}: rank = {r_new} (from {len(new_vecs)} vectors)")

        if r_new == prev_rank:
            print(f"  PS rank stabilized at level {level}")
            return r_new, basis_new
        prev_rank = r_new
        prev_basis_vecs = new_vecs

    r_final, basis_final = current_rank(prev_basis_vecs)
    return r_final, basis_final


# =============================================================================
# SECTION 4: CROSS-CHECKS
# =============================================================================

def verify_anti_hermiticity(PS_16, PS_names):
    """Verify that PS generators are anti-Hermitian (Lie algebra generators)."""
    results = []
    for i, (T, name) in enumerate(zip(PS_16, PS_names)):
        err = la_norm(T + T.conj().T)
        results.append((name, err))
    return results


def check_algebra_closure(PS_16, PS_names, PS_types):
    """Check that PS generators close under commutation (form a Lie subalgebra).

    For SU(2)_R: [T_i, T_j] should be epsilon_{ijk} T_k (up to normalization).
    For leptoquark sector: more complex structure constants.
    """
    n_gen = len(PS_16)
    closure_matrix = np.zeros((n_gen, n_gen))

    for i in range(n_gen):
        for j in range(i+1, n_gen):
            comm = PS_16[i] @ PS_16[j] - PS_16[j] @ PS_16[i]
            # Project onto each generator
            max_proj = 0.0
            for k in range(n_gen):
                # Frobenius inner product
                ip = np.real(np.trace(comm.conj().T @ PS_16[k]))
                max_proj = max(max_proj, abs(ip))

            # Residual after projecting onto all generators
            proj = np.zeros_like(comm)
            for k in range(n_gen):
                ip = np.trace(comm.conj().T @ PS_16[k]) / np.trace(PS_16[k].conj().T @ PS_16[k])
                proj += ip * PS_16[k]
            res_norm = la_norm(comm - proj)
            comm_norm = la_norm(comm)
            if comm_norm > 1e-15:
                closure_matrix[i, j] = res_norm / comm_norm
            else:
                closure_matrix[i, j] = 0.0

    return closure_matrix


def check_ps_gauge_covariance(basis, n, PS_16, dim_rep=3):
    """Check if each PS generator preserves the given 1-form basis under conjugation.

    For each T_a^PS and each basis omega_k:
      [T_a, omega_k] in span(basis)?

    Returns per-generator max residual.
    """
    rank = basis.shape[0]
    if dim_rep == 1:
        T_gens = [g.copy() for g in PS_16]
    else:
        T_gens = [np.kron(np.eye(dim_rep), g) for g in PS_16]

    basis_mats = [basis[k].reshape(n, n) for k in range(min(rank, 60))]

    per_gen = []
    for T in T_gens:
        gen_max = 0.0  # (local)
        for omega_k in basis_mats:
            comm = T @ omega_k - omega_k @ T
            vec = comm.flatten()
            norm_orig = la_norm(vec)
            if norm_orig < 1e-15:
                continue
            coeffs = basis @ vec.conj()
            proj = coeffs.conj() @ basis
            res = la_norm(vec - proj) / norm_orig
            gen_max = max(gen_max, res)
        per_gen.append(gen_max)

    return np.array(per_gen)


# =============================================================================
# SECTION 5: VISUALIZATION
# =============================================================================

def make_plot(PS_names, PS_types, residuals_sm, residuals_ps,
              comm_norms, rank_sm, rank_ps, sm_gauge_res):
    """Create summary plot with 4 panels."""
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Panel 1: Commutator norms
    ax = axes[0, 0]
    colors = ['#d62728' if t == 'SU2R' else '#1f77b4' for t in PS_types]
    bars = ax.bar(range(len(PS_names)), comm_norms, color=colors, alpha=0.8)
    ax.set_xticks(range(len(PS_names)))
    ax.set_xticklabels(PS_names, rotation=45, ha='right', fontsize=8)
    ax.set_ylabel('||[D_K, T_a^PS]||')
    ax.set_title('Commutator Norms (red=SU(2)_R, blue=Leptoquark)')
    ax.set_yscale('log')
    ax.axhline(y=1e-10, color='gray', ls='--', alpha=0.5, label='machine eps scale')

    # Panel 2: Residuals on SM basis (rank 775)
    ax = axes[0, 1]
    colors2 = ['#d62728' if t == 'SU2R' else '#1f77b4' for t in PS_types]
    ax.bar(range(len(PS_names)), residuals_sm + 1e-16, color=colors2, alpha=0.8)
    ax.set_xticks(range(len(PS_names)))
    ax.set_xticklabels(PS_names, rotation=45, ha='right', fontsize=8)
    ax.set_ylabel('Fractional residual')
    ax.set_title(f'Projection onto SM Omega^1_D (rank {rank_sm})')
    ax.set_yscale('log')
    ax.axhline(y=1e-10, color='green', ls='--', label='PASS threshold')
    ax.legend(fontsize=8)

    # Panel 3: Residuals on PS-enlarged basis
    ax = axes[1, 0]
    if residuals_ps is not None:
        ax.bar(range(len(PS_names)), residuals_ps + 1e-16, color=colors2, alpha=0.8)
        ax.set_xticks(range(len(PS_names)))
        ax.set_xticklabels(PS_names, rotation=45, ha='right', fontsize=8)
        ax.set_ylabel('Fractional residual')
        ax.set_title(f'Projection onto PS Omega^1_D (rank {rank_ps})')
        ax.set_yscale('log')
        ax.axhline(y=1e-10, color='green', ls='--', label='PASS threshold')
        ax.legend(fontsize=8)
    else:
        ax.text(0.5, 0.5, 'All in SM space\n(rank enlargement not needed)',
                transform=ax.transAxes, ha='center', va='center', fontsize=12)
        ax.set_title(f'PS Omega^1_D = SM Omega^1_D (rank {rank_sm})')

    # Panel 4: SM gauge generator comparison
    ax = axes[1, 1]
    sm_names = ['u1', 'su2_1', 'su2_2', 'su2_3',
                'su3_1', 'su3_2', 'su3_3', 'su3_4',
                'su3_5', 'su3_6', 'su3_7', 'su3_8', 'u1_c']
    n_sm = min(len(sm_gauge_res), len(sm_names))
    ax.bar(range(n_sm), sm_gauge_res[:n_sm] + 1e-16, color='#2ca02c', alpha=0.8)
    ax.set_xticks(range(n_sm))
    ax.set_xticklabels(sm_names[:n_sm], rotation=45, ha='right', fontsize=8)
    ax.set_ylabel('Gauge covariance residual')
    ax.set_title('SM generators on extended basis (GAUGE-MODULE-61)')
    ax.set_yscale('log')
    ax.axhline(y=1e-10, color='green', ls='--')

    plt.tight_layout()
    plt.savefig(OUTPUT_PNG, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"\n  Plot saved: {OUTPUT_PNG}")


# =============================================================================
# MAIN
# =============================================================================

def main():
    t0 = time.time()
    print("=" * 72)
    print("S63 PS-KASPAROV-63: Pati-Salam Gauge Module Check")
    print("=" * 72)

    # --- Setup ---
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    gammas = build_cliff8()
    tau = tau_fold

    # Build D_K on fundamental (C^3 x C^16 = C^48)
    D_K = build_DK_fundamental(gammas, gens, f_abc, tau)
    n = D_K.shape[0]  # 48
    print(f"\nD_K dimension: {n}x{n}, tau = {tau}")

    # Verify self-adjointness
    sa_err = la_norm(D_K - D_K.conj().T)
    print(f"D_K self-adjointness: ||D - D^dag|| = {sa_err:.6e}")

    # --- Build SM algebra generators ---
    AF_16, AF_names, AF_factors = build_AF_generators()
    n_SM = len(AF_16)
    print(f"\nSM algebra generators: {n_SM}")

    # --- Build PS generators (both constructions) ---
    print("\n--- SECTION 1: Pati-Salam Generator Construction ---")

    PS_bimod, PS_bimod_names, PS_bimod_types = build_PS_generators()
    PS_direct, PS_direct_names, PS_direct_types = build_PS_generators_direct()
    print(f"PS generators (bimodule): {len(PS_bimod)}")
    print(f"PS generators (direct):   {len(PS_direct)}")

    # Cross-check: both constructions should agree
    print("\n  Cross-check bimodule vs direct construction:")
    max_diff = 0.0  # (local)
    for i in range(9):
        diff = la_norm(PS_bimod[i] - PS_direct[i])
        if diff > max_diff:
            max_diff = diff
        if diff > 1e-10:
            print(f"  WARNING: {PS_bimod_names[i]} vs {PS_direct_names[i]}: diff = {diff:.6e}")
    print(f"  Max bimodule-direct difference: {max_diff:.6e}")

    # Use direct construction (more transparent)
    # But if they disagree, test BOTH and report
    if max_diff > 1e-10:
        print("  Using DIRECT construction (disagreement detected, will test both)")
        PS_16 = PS_direct
        PS_names = PS_direct_names
        PS_types = PS_direct_types
        test_both = True
    else:
        print("  Constructions agree. Using direct construction.")
        PS_16 = PS_direct
        PS_names = PS_direct_names
        PS_types = PS_direct_types
        test_both = False

    # Verify anti-Hermiticity
    ah_results = verify_anti_hermiticity(PS_16, PS_names)
    print("\n  Anti-Hermiticity check:")
    max_ah = 0.0
    for name, err in ah_results:
        max_ah = max(max_ah, err)
    print(f"  Max ||T + T^dag||: {max_ah:.6e}")

    # Check PS algebra closure
    print("\n  Algebra closure check (within PS generators):")
    clos = check_algebra_closure(PS_16, PS_names, PS_types)
    max_closure_res = np.max(clos)
    print(f"  Max closure residual: {max_closure_res:.6e}")

    # --- Compute SM extended 1-form basis (reproduce GAUGE-MODULE-61) ---
    print("\n--- SECTION 2: Reproduce SM Extended 1-Form Space ---")

    rank_sm_ext, basis_sm_ext = compute_extended_omega1_basis(D_K, AF_16, dim_rep=3, n_levels=3)
    print(f"\n  SM extended Omega^1_D rank: {rank_sm_ext}")

    # Cross-check against stored value
    try:
        gm_data = np.load(os.path.join(OUTDIR, "s61_gauge_module_extended.npz"), allow_pickle=True)
        stored_rank = int(gm_data['rank_ext'])
        print(f"  Stored GAUGE-MODULE-61 rank: {stored_rank}")
        if rank_sm_ext == stored_rank:
            print(f"  MATCH: rank {rank_sm_ext} reproduced exactly.")
        else:
            print(f"  WARNING: rank mismatch ({rank_sm_ext} vs {stored_rank})")
    except Exception as e:
        print(f"  Could not load stored data: {e}")

    # --- Compute [D_K, T_a^PS] commutators ---
    print("\n--- SECTION 3: PS Commutators [D_K, T_a^PS] ---")

    comms, comm_norms = compute_ps_commutators(D_K, PS_16, dim_rep=3)
    print("\n  Generator        Type      ||[D_K, T]||")
    print("  " + "-" * 50)
    for i in range(9):
        print(f"  {PS_names[i]:18s} {PS_types[i]:6s}  {comm_norms[i]:.10e}")

    n_zero_comm = np.sum(comm_norms < 1e-10)
    n_nonzero = 9 - n_zero_comm
    print(f"\n  Nonzero commutators: {n_nonzero}/9")
    print(f"  Zero commutators:    {n_zero_comm}/9")

    # --- Project onto SM extended basis ---
    print("\n--- SECTION 4: Projection onto SM Extended Omega^1_D ---")

    residuals_sm, proj_sm = project_commutators_onto_basis(comms, basis_sm_ext)
    print("\n  Generator        Type      Residual       Status")
    print("  " + "-" * 60)
    threshold = 1e-6  # conservative threshold (local)
    all_in_sm = True
    for i in range(9):
        if comm_norms[i] < 1e-10:
            status = "ZERO (trivially in)"
        elif residuals_sm[i] < threshold:
            status = "IN"
        else:
            status = "OUTSIDE"
            all_in_sm = False
        print(f"  {PS_names[i]:18s} {PS_types[i]:6s}  {residuals_sm[i]:.10e}  {status}")

    print(f"\n  All 9 in SM extended space: {'YES' if all_in_sm else 'NO'}")

    # --- If any outside, compute PS-enlarged space ---
    rank_ps_ext = rank_sm_ext
    basis_ps_ext = basis_sm_ext
    residuals_ps = None

    if not all_in_sm:
        print("\n--- SECTION 5: PS-Enlarged 1-Form Space ---")
        rank_ps_ext, basis_ps_ext = compute_ps_enlarged_omega1(
            D_K, AF_16, PS_16, dim_rep=3, n_levels=3
        )
        print(f"\n  PS enlarged rank: {rank_ps_ext}")
        print(f"  Rank increase: {rank_ps_ext} - {rank_sm_ext} = {rank_ps_ext - rank_sm_ext}")

        # Re-project onto PS-enlarged basis
        residuals_ps, _ = project_commutators_onto_basis(comms, basis_ps_ext)
        print("\n  Generator        Type      SM Resid       PS Resid       PS Status")
        print("  " + "-" * 75)
        all_in_ps = True
        for i in range(9):
            if comm_norms[i] < 1e-10:
                ps_status = "ZERO"
            elif residuals_ps[i] < threshold:
                ps_status = "IN"
            else:
                ps_status = "OUTSIDE"
                all_in_ps = False
            print(f"  {PS_names[i]:18s} {PS_types[i]:6s}  {residuals_sm[i]:.6e}  "
                  f"{residuals_ps[i]:.6e}  {ps_status}")

        # Check bimodule closure of PS-enlarged space
        print("\n  Checking PS-enlarged bimodule closure...")
        combined_gens = AF_16 + PS_16
        ml, mr, mol, mor = check_bimodule_on_basis(
            basis_ps_ext, n, combined_gens, dim_rep=3
        )
        ps_is_bimodule = max(ml, mr, mol, mor) < 1e-4
        print(f"  Left A_PS:   {ml:.6e}")
        print(f"  Right A_PS:  {mr:.6e}")
        print(f"  Left A_PS^o: {mol:.6e}")
        print(f"  Right A_PS^o:{mor:.6e}")
        print(f"  PS is bimodule: {'YES' if ps_is_bimodule else 'NO'}")
    else:
        all_in_ps = True
        ps_is_bimodule = True  # inherited from SM

    # --- Check PS gauge covariance on the relevant basis ---
    print("\n--- SECTION 6: PS Gauge Covariance ---")
    ps_gauge_res = check_ps_gauge_covariance(basis_ps_ext, n, PS_16, dim_rep=3)
    print("\n  PS generator gauge covariance on extended basis:")
    for i in range(9):
        status = "PRESERVES" if ps_gauge_res[i] < 1e-4 else "BREAKS"
        print(f"  {PS_names[i]:18s} {PS_types[i]:6s}  {ps_gauge_res[i]:.10e}  [{status}]")

    n_ps_preserve = np.sum(ps_gauge_res < 1e-4)
    n_su2r_preserve = sum(1 for i in range(9) if PS_types[i] == 'SU2R' and ps_gauge_res[i] < 1e-4)
    n_lq_preserve = sum(1 for i in range(9) if PS_types[i] == 'LQ' and ps_gauge_res[i] < 1e-4)

    # --- Also test bimodule construction if disagreement ---
    bimod_residuals_sm = None
    if test_both:
        print("\n--- SECTION 6b: Bimodule Construction Cross-Check ---")
        comms_b, norms_b = compute_ps_commutators(D_K, PS_bimod, dim_rep=3)
        res_b, _ = project_commutators_onto_basis(comms_b, basis_sm_ext)
        bimod_residuals_sm = res_b
        print("  Bimodule construction residuals:")
        for i in range(9):
            print(f"  {PS_bimod_names[i]:18s}: ||[D,T]||={norms_b[i]:.6e}, resid={res_b[i]:.6e}")

    # --- Load SM gauge covariance for comparison plot ---
    try:
        gm_data = np.load(os.path.join(OUTDIR, "s61_gauge_module_extended.npz"), allow_pickle=True)
        sm_gauge_res = gm_data['gauge_residuals']
    except:
        sm_gauge_res = np.zeros(13)

    # --- GATE VERDICT ---
    print("\n" + "=" * 72)
    print("GATE VERDICT: PS-KASPAROV-63")
    print("=" * 72)

    # Primary criterion: all 9 commutators in extended 1-form space
    if all_in_sm:
        verdict = "PASS"
        reason = (f"All 9 PS commutators [D_K, T_a^PS] lie within the SM extended "
                  f"Omega^1_D (rank {rank_sm_ext}) to machine precision. "
                  f"PS gauge module = SM gauge module. No enlargement needed.")
    elif all_in_ps:
        verdict = "PASS"
        reason = (f"All 9 PS commutators lie within the PS-enlarged Omega^1_D "
                  f"(rank {rank_ps_ext}, up from SM rank {rank_sm_ext}). "
                  f"PS gauge module verified with {rank_ps_ext - rank_sm_ext} additional dimensions.")
    else:
        verdict = "FAIL"
        n_outside = sum(1 for i in range(9)
                       if comm_norms[i] > 1e-10 and
                       (residuals_ps[i] if residuals_ps is not None else residuals_sm[i]) > threshold)
        reason = (f"{n_outside}/9 PS commutators fall OUTSIDE the PS-enlarged "
                  f"Omega^1_D (rank {rank_ps_ext}). PS incompatible with Jensen geometry.")

    print(f"\n  Verdict: {verdict}")
    print(f"  Reason:  {reason}")
    print(f"\n  Key numbers:")
    print(f"    SM extended rank:        {rank_sm_ext}")
    print(f"    PS enlarged rank:        {rank_ps_ext}")
    print(f"    Max SM residual:         {np.max(residuals_sm):.6e}")
    if residuals_ps is not None:
        print(f"    Max PS residual:         {np.max(residuals_ps):.6e}")
    print(f"    Nonzero commutators:     {n_nonzero}/9")
    print(f"    PS gauge-preserving:     {n_ps_preserve}/9 (SU2R: {n_su2r_preserve}/3, LQ: {n_lq_preserve}/6)")
    print(f"    D_K self-adjointness:    {sa_err:.6e}")
    print(f"    Generator anti-Hermiticity: {max_ah:.6e}")

    dt = time.time() - t0
    print(f"\n  Runtime: {dt:.1f}s")

    # --- Save results ---
    np.savez(OUTPUT_NPZ,
             tau=tau,
             n_dim=n,
             verdict=verdict,
             reason=reason,
             # PS generators
             PS_names=np.array(PS_names),
             PS_types=np.array(PS_types),
             # Commutator norms
             comm_norms=comm_norms,
             # Residuals
             residuals_sm=residuals_sm,
             residuals_ps=residuals_ps if residuals_ps is not None else residuals_sm,
             # Ranks
             rank_sm_ext=rank_sm_ext,
             rank_ps_ext=rank_ps_ext,
             # PS gauge covariance
             ps_gauge_residuals=ps_gauge_res,
             n_ps_preserve=n_ps_preserve,
             n_su2r_preserve=n_su2r_preserve,
             n_lq_preserve=n_lq_preserve,
             # Cross-checks
             sa_err=sa_err,
             max_anti_herm=max_ah,
             max_closure_res=max_closure_res,
             bimod_direct_diff=max_diff,
             # Runtime
             runtime_s=dt,
             )
    print(f"  Data saved: {OUTPUT_NPZ}")

    # --- Plot ---
    make_plot(PS_names, PS_types, residuals_sm,
              residuals_ps, comm_norms, rank_sm_ext, rank_ps_ext, sm_gauge_res)

    return verdict


if __name__ == "__main__":
    try:
        verdict = main()
    except Exception as e:
        print(f"\nFATAL ERROR: {e}")
        traceback.print_exc()
        sys.exit(1)
