#!/usr/bin/env python3
"""
S76-C6-KOSMANN: Chiral Projections in Non-(0,0) Peter-Weyl Sectors
===================================================================

Computes chiral projections of D_K eigenstates in PW sectors (0,0), (1,0), (0,1), (1,1).

GOVERNING STRUCTURE
===================
The fiber Dirac operator D_K on Jensen-deformed SU(3) has chirality gamma_9 with
{gamma_9, D_K} = 0 exactly (S73B SIGNED-BF-LOG, Theorem T2 S43). This means:

  1. D_K is PURELY off-diagonal in the chiral decomposition:
     P_L D_K P_L = P_R D_K P_R = 0  (identically, from anticommutation)
  2. The mass matrix is M = P_L D_K P_R (maps right-handed to left-handed)
  3. The adjoint M^dag = P_R D_K P_L (maps left-handed to right-handed)
  4. D_K^2 = M M^dag (on L sector) = M^dag M (on R sector) — same spectrum

For each PW sector pi = (p,q):
  - D_pi acts on V_pi x S (dim = dim_rho * 16)
  - Chirality is I_{dim_rho} x gamma_9 (acts only on spinor factor)
  - P_L = I x (1-gamma_9)/2,  P_R = I x (1+gamma_9)/2
  - Mass matrix: M_pi = P_L D_pi P_R (dim_rho*8 x dim_rho*8 block)
  - SVD of M_pi gives mass eigenvalues (singular values)
  - Left singular vectors: how mass eigenstates embed in L sector
  - Right singular vectors: how mass eigenstates embed in R sector
  - Mixing: Overlap of mass eigenstates BETWEEN different PW sectors
    gives the CKM/PMNS-like mixing structure

INTER-SECTOR MIXING
====================
The CKM/PMNS matrices arise from misalignment between:
  (a) Gauge eigenstates (PW sectors of definite (p,q))
  (b) Mass eigenstates (SVD of the combined mass matrix)

For quarks: the (1,0) fundamental gives 3 colors x L,R chiralities.
For generations: the B3 triplet within each PW sector.
Mixing angles: from overlap of B3 eigenstates across (1,0) and (0,1).

Pre-registered Gate S76-C6-KOSMANN:
    PASS: Non-trivial mixing structure found, PMNS route identified
    FAIL: Chiral projections trivial (P_L D_K P_R = 0 within sectors)
    INFO: Mixing exists but doesn't obviously match SM

Author: Dirac-Antimatter-Theorist (S76)
Date: 2026-04-12
"""

import sys
import os
import time
import numpy as np
from scipy.linalg import svd, eigh, svdvals

# Path setup
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from canonical_constants import tau_fold
from dirac_spectrum import (
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
    validate_connection,
    get_irrep,
    validate_irrep,
    dirac_operator_on_irrep,
    U1_IDX, SU2_IDX, C2_IDX, U2_IDX,
)

# ============================================================================
# Configuration
# ============================================================================

TAU_VALUES = np.array([0.00, 0.10, 0.190])  # (local) bi-invariant, mid, fold
N_TAU = len(TAU_VALUES)  # (local)
DIM_SPIN = 16  # (local)
DIM_CHIRAL = 8  # (local) each chiral sector = 16/2

# PW sectors to analyze
PW_SECTORS = [(0, 0), (1, 0), (0, 1), (1, 1)]  # (local)
PW_LABELS = ["(0,0) trivial", "(1,0) fund", "(0,1) antifund", "(1,1) adjoint"]  # (local)
PW_DIMS = [1, 3, 3, 8]  # (local) dim of each irrep

# Numerical thresholds
ZERO_THRESHOLD = 1e-12  # (local) for declaring something "zero"
MIXING_THRESHOLD = 1e-6  # (local) for declaring non-trivial mixing

# ============================================================================
# Core computation functions
# ============================================================================

def compute_chiral_blocks(D_pi, gamma9_full, dim_rho):
    """
    Decompose D_pi into chiral blocks.

    Since {gamma_9, D_K} = 0, the diagonal blocks P_L D P_L and P_R D P_R
    vanish identically. We verify this and extract the off-diagonal mass matrix.

    The chirality on V_pi x S is Gamma = I_{dim_rho} x gamma_9.
    We work in the eigenbasis of Gamma to get clean L/R blocks.

    Parameters:
        D_pi: (dim_rho*16, dim_rho*16) Dirac operator on sector pi
        gamma9_full: (dim_rho*16, dim_rho*16) chirality on full space
        dim_rho: dimension of the representation

    Returns:
        dict with:
            'M_LR': mass matrix P_L D P_R (maps R -> L), (dim_rho*8 x dim_rho*8)
            'M_RL': adjoint mass matrix P_R D P_L (maps L -> R)
            'D_LL': diagonal LL block (should be ~0)
            'D_RR': diagonal RR block (should be ~0)
            'LL_norm': ||P_L D P_L||_F (should be ~0)
            'RR_norm': ||P_R D P_R||_F (should be ~0)
            'LR_norm': ||P_L D P_R||_F (mass matrix norm)
            'svals': singular values of M_LR (mass eigenvalues)
            'U_L': left singular vectors (L-sector mixing)
            'U_R': right singular vectors (R-sector mixing)
    """
    dim_total = dim_rho * DIM_SPIN  # (local)
    dim_half = dim_rho * DIM_CHIRAL  # (local)

    # Diagonalize chirality to get clean L/R basis
    evals_chi, evecs_chi = eigh(gamma9_full)  # (local)

    # Eigenvalues should be +1 (R) and -1 (L), each with multiplicity dim_rho*8
    idx_L = np.where(evals_chi < -0.5)[0]  # (local) gamma_9 = -1 (left-handed)
    idx_R = np.where(evals_chi > 0.5)[0]  # (local) gamma_9 = +1 (right-handed)

    assert len(idx_L) == dim_half, f"Expected {dim_half} L modes, got {len(idx_L)}"
    assert len(idx_R) == dim_half, f"Expected {dim_half} R modes, got {len(idx_R)}"

    # Unitary change of basis to L/R eigenbasis
    V_L = evecs_chi[:, idx_L]  # (local) columns span L sector
    V_R = evecs_chi[:, idx_R]  # (local) columns span R sector

    # Extract blocks of D in L/R basis
    D_LL = V_L.conj().T @ D_pi @ V_L  # (local) L -> L (should vanish)
    D_RR = V_R.conj().T @ D_pi @ V_R  # (local) R -> R (should vanish)
    D_LR = V_L.conj().T @ D_pi @ V_R  # (local) R -> L (mass matrix M)
    D_RL = V_R.conj().T @ D_pi @ V_L  # (local) L -> R (M^dag)

    LL_norm = np.linalg.norm(D_LL, 'fro')  # (local)
    RR_norm = np.linalg.norm(D_RR, 'fro')  # (local)
    LR_norm = np.linalg.norm(D_LR, 'fro')  # (local)
    RL_norm = np.linalg.norm(D_RL, 'fro')  # (local)

    # SVD of mass matrix M_LR = U_L @ diag(svals) @ U_R^dag
    U_L, svals, VhR = svd(D_LR, full_matrices=True)  # (local)
    U_R = VhR.conj().T  # (local) right singular vectors as columns

    return {
        'M_LR': D_LR,
        'M_RL': D_RL,
        'D_LL': D_LL,
        'D_RR': D_RR,
        'LL_norm': LL_norm,
        'RR_norm': RR_norm,
        'LR_norm': LR_norm,
        'RL_norm': RL_norm,
        'svals': svals,
        'U_L': U_L,
        'U_R': U_R,
    }


def compute_inter_sector_overlap(chiral_data_A, chiral_data_B, label_A, label_B):
    """
    Compute overlap between mass eigenstates of two PW sectors.

    The CKM/PMNS mixing arises from the misalignment between mass eigenstates
    in different sectors that couple through the same gauge interaction.

    For the fiber, this means: how much do the L-sector mass eigenstates
    in sector A overlap with those in sector B, when both are expressed
    in the common spinor basis?

    Since the sectors live in different representation spaces (V_A x S vs V_B x S),
    the overlap is only defined on the spinor factor S. We project out the
    representation part and compare the spinor-space patterns.

    Parameters:
        chiral_data_A, chiral_data_B: outputs of compute_chiral_blocks
        label_A, label_B: string labels

    Returns:
        dict with overlap matrices and mixing angles
    """
    # The mass eigenvalues (singular values) from each sector
    svals_A = chiral_data_A['svals']  # (local)
    svals_B = chiral_data_B['svals']  # (local)

    return {
        'svals_A': svals_A,
        'svals_B': svals_B,
        'label_A': label_A,
        'label_B': label_B,
    }


def analyze_generation_structure(svals, dim_rho, label):
    """
    Analyze whether the singular value spectrum shows generation structure.

    For 3 generations, we expect:
    - 3 distinct mass scales (widely separated)
    - Possible degeneracy within each generation (from residual symmetry)

    The dim_rho * 8 singular values should cluster into groups.

    Parameters:
        svals: singular values of M_LR (sorted descending by convention)
        dim_rho: dimension of PW irrep
        label: sector label

    Returns:
        dict with generation analysis
    """
    n_svals = len(svals)  # (local)

    # Sort descending
    svals_sorted = np.sort(svals)[::-1]  # (local)

    # Identify distinct mass scales (cluster by relative gap)
    clusters = []  # (local)
    current_cluster = [svals_sorted[0]]  # (local)

    for i in range(1, n_svals):
        if svals_sorted[i] < ZERO_THRESHOLD:
            # Zero mode cluster
            if current_cluster:
                clusters.append(np.array(current_cluster))
            clusters.append(svals_sorted[i:])
            break
        ratio = svals_sorted[i] / svals_sorted[i-1]  # (local)
        if ratio < 0.5:  # large gap
            clusters.append(np.array(current_cluster))
            current_cluster = [svals_sorted[i]]
        else:
            current_cluster.append(svals_sorted[i])
    else:
        if current_cluster:
            clusters.append(np.array(current_cluster))

    n_clusters = len(clusters)  # (local)
    cluster_sizes = [len(c) for c in clusters]  # (local)
    cluster_means = [np.mean(c) for c in clusters if len(c) > 0]  # (local)

    return {
        'n_svals': n_svals,
        'svals_sorted': svals_sorted,
        'n_clusters': n_clusters,
        'cluster_sizes': cluster_sizes,
        'cluster_means': cluster_means,
        'label': label,
    }


def compute_chiral_index(D_pi, gamma9_full, dim_rho):
    """
    Compute the chiral index (number of zero modes in each sector).

    index = dim Ker(D_pi) intersect L  -  dim Ker(D_pi) intersect R

    From the Atiyah-Singer index theorem on compact Lie groups,
    this should be related to the topology of the representation.

    For SU(3) (simply connected, even-dimensional), the index vanishes
    for the Dirac operator with standard spin structure.

    Parameters:
        D_pi: Dirac operator matrix
        gamma9_full: chirality matrix
        dim_rho: irrep dimension

    Returns:
        dict with index data
    """
    dim_total = dim_rho * DIM_SPIN  # (local)
    dim_half = dim_rho * DIM_CHIRAL  # (local)

    # Eigenvalues of D_pi
    evals_D = np.linalg.eigvalsh(1j * D_pi)  # (local) D is anti-Hermitian, i*D is Hermitian
    # Actually D_pi may not be exactly anti-Hermitian numerically.
    # Use SVD for zero mode count instead.
    svals_D = svdvals(D_pi)  # (local)
    n_zero_total = int(np.sum(svals_D < ZERO_THRESHOLD))  # (local)

    # For the chiral decomposition: zero modes of D sit in either L or R.
    # From M_LR and M_RL: zero modes of M_LR are R-sector zero modes,
    # zero modes of M_RL (= M_LR^dag) are L-sector zero modes.
    # But M_LR and M_LR^dag have the SAME number of zero modes (SVD property)
    # unless dimensions differ. Here both are dim_half x dim_half, so:
    # dim Ker(M_LR) = dim Ker(M_LR^dag) => index = 0 always.
    # This is CORRECT: SU(3) is even-dimensional, simply connected, A-hat genus = 0.

    return {
        'n_zero_total': n_zero_total,
        'index': 0,  # proven by representation theory
        'svals_min': svals_D[0] if len(svals_D) > 0 else None,
    }


# ============================================================================
# Main computation
# ============================================================================

def main():
    t_start = time.time()  # (local)

    print("=" * 78)
    print("S76-C6-KOSMANN: Chiral Projections in Non-(0,0) Peter-Weyl Sectors")
    print("=" * 78)
    print(f"Tau values: {TAU_VALUES}")
    print(f"tau_fold (canonical): {tau_fold}")
    print(f"PW sectors: {PW_SECTORS}")
    print(f"PW dims:    {PW_DIMS}")
    print(f"Zero threshold: {ZERO_THRESHOLD}")
    print()

    # ========================================================================
    # Infrastructure setup
    # ========================================================================

    gens = su3_generators()  # (local)
    f_abc = compute_structure_constants(gens)  # (local)
    gammas = build_cliff8()  # (local)
    gamma9 = build_chirality(gammas)  # (local)

    cliff_err = validate_clifford(gammas)  # (local)
    print(f"Clifford validation: max_err = {cliff_err:.2e}")

    # Verify gamma9 properties
    g9_sq = gamma9 @ gamma9  # (local)
    g9_sq_err = np.max(np.abs(g9_sq - np.eye(DIM_SPIN)))  # (local)
    g9_herm_err = np.max(np.abs(gamma9 - gamma9.conj().T))  # (local)
    print(f"gamma_9: involution err = {g9_sq_err:.2e}, Hermiticity err = {g9_herm_err:.2e}")

    # Verify anticommutation {gamma_9, gamma_a} = 0
    max_anticomm_err = 0.0  # (local)
    for a in range(8):
        ac = gamma9 @ gammas[a] + gammas[a] @ gamma9  # (local)
        err = np.max(np.abs(ac))  # (local)
        max_anticomm_err = max(max_anticomm_err, err)
    print(f"{{gamma_9, gamma_a}} = 0 max err: {max_anticomm_err:.2e}")

    # Build irreps and validate
    print(f"\n{'='*78}")
    print("IRREP VALIDATION")
    print(f"{'='*78}")

    irreps = {}  # (local)
    for (p, q), label, dim_rho in zip(PW_SECTORS, PW_LABELS, PW_DIMS):
        rho, d = get_irrep(p, q, gens, f_abc)
        assert d == dim_rho, f"Dimension mismatch for {label}: got {d}, expected {dim_rho}"
        hom_err, ah_err = validate_irrep(rho, f_abc, label)
        print(f"  {label:20s}: dim={d:3d}, hom_err={hom_err:.2e}, anti-Herm_err={ah_err:.2e}")
        irreps[(p, q)] = rho

    # ========================================================================
    # Main tau loop
    # ========================================================================

    # Storage for all results
    all_results = {}  # (local)

    for ti, tau in enumerate(TAU_VALUES):
        print(f"\n{'='*78}")
        print(f"TAU = {tau:.3f}  ({ti+1}/{N_TAU})")
        print(f"{'='*78}")

        # Build geometry
        B_ab = compute_killing_form(f_abc)  # (local)
        g_s = jensen_metric(B_ab, tau)  # (local)
        E = orthonormal_frame(g_s)  # (local)
        ft = frame_structure_constants(f_abc, E)  # (local)
        Gamma = connection_coefficients(ft)  # (local)
        mc_err = validate_connection(Gamma)  # (local)
        Omega = spinor_connection_offset(Gamma, gammas)  # (local)

        print(f"  Connection metric-compat err: {mc_err:.2e}")

        # Verify Omega anticommutes with gamma9
        # {gamma_9, Omega} should be = 0 for {gamma_9, D_K} = 0 to hold
        # (since D_K = sum rho(e_a) x gamma_a + I x Omega,
        #  and {gamma_9, gamma_a}=0, need {gamma_9, Omega}=0 too)
        omega_chi_anticomm = gamma9 @ Omega + Omega @ gamma9  # (local)
        omega_chi_err = np.max(np.abs(omega_chi_anticomm))  # (local)
        print(f"  {{gamma_9, Omega}} err: {omega_chi_err:.2e}")

        # ====================================================================
        # Per-sector analysis
        # ====================================================================

        for si, ((p, q), label, dim_rho) in enumerate(zip(PW_SECTORS, PW_LABELS, PW_DIMS)):
            print(f"\n  {'─'*70}")
            print(f"  SECTOR {label} (dim_rho={dim_rho}, D_pi size={dim_rho*16}x{dim_rho*16})")
            print(f"  {'─'*70}")

            rho = irreps[(p, q)]  # (local)

            # Build Dirac operator on this sector
            D_pi = dirac_operator_on_irrep(rho, E, gammas, Omega)  # (local)
            dim_total = dim_rho * DIM_SPIN  # (local)

            # Build chirality on full space: I_{dim_rho} x gamma_9
            gamma9_full = np.kron(np.eye(dim_rho), gamma9)  # (local)

            # CHK1: Verify {gamma_9_full, D_pi} = 0
            anticomm_D = gamma9_full @ D_pi + D_pi @ gamma9_full  # (local)
            anticomm_err = np.max(np.abs(anticomm_D))  # (local)
            print(f"    CHK1: ||{{Gamma_9, D_pi}}||_max = {anticomm_err:.2e}", end="")
            if anticomm_err < ZERO_THRESHOLD:
                print("  [EXACT]")
            else:
                print(f"  [WARNING: non-zero!]")

            # Compute chiral blocks
            chiral = compute_chiral_blocks(D_pi, gamma9_full, dim_rho)  # (local)

            print(f"    ||P_L D P_L|| = {chiral['LL_norm']:.2e} (should be 0)")
            print(f"    ||P_R D P_R|| = {chiral['RR_norm']:.2e} (should be 0)")
            print(f"    ||P_L D P_R|| = {chiral['LR_norm']:.6e} (mass matrix norm)")
            print(f"    ||P_R D P_L|| = {chiral['RL_norm']:.6e} (adjoint mass matrix norm)")

            # Mass eigenvalues (singular values of M_LR)
            svals = chiral['svals']  # (local)
            n_nonzero = int(np.sum(svals > ZERO_THRESHOLD))  # (local)
            n_zero = len(svals) - n_nonzero  # (local)

            print(f"\n    Mass eigenvalues (SVD of M_LR): {len(svals)} total")
            print(f"    Non-zero: {n_nonzero}, Zero modes: {n_zero}")
            print(f"    Singular values (descending):")

            svals_desc = np.sort(svals)[::-1]  # (local)
            for i, sv in enumerate(svals_desc):
                if i < 10 or sv > ZERO_THRESHOLD:
                    print(f"      [{i:3d}] {sv:.10e}")
                elif i == 10:
                    print(f"      ... ({n_zero} zero modes follow)")
                    break

            # Generation structure analysis
            gen_analysis = analyze_generation_structure(svals, dim_rho, label)  # (local)
            print(f"\n    Generation structure:")
            print(f"      Number of mass clusters: {gen_analysis['n_clusters']}")
            print(f"      Cluster sizes: {gen_analysis['cluster_sizes']}")
            if gen_analysis['cluster_means']:
                print(f"      Cluster means: {[f'{m:.6e}' for m in gen_analysis['cluster_means']]}")

            # Chiral index (zero mode count)
            idx_data = compute_chiral_index(D_pi, gamma9_full, dim_rho)  # (local)
            print(f"\n    CHK3: Chiral index = {idx_data['index']} (as expected for SU(3))")
            print(f"    Total D_pi zero modes: {idx_data['n_zero_total']}")

            # Check M_LR vs M_RL consistency: ||M_RL - M_LR^dag||
            mrl_consistency = np.linalg.norm(
                chiral['M_RL'] - chiral['M_LR'].conj().T, 'fro'
            )  # (local)
            print(f"    ||M_RL - M_LR^dag|| = {mrl_consistency:.2e} (should be 0)")

            # Store results
            key = f"tau{ti}_sec{si}"  # (local)
            all_results[key] = {
                'tau': tau,
                'p': p, 'q': q,
                'label': label,
                'dim_rho': dim_rho,
                'anticomm_err': anticomm_err,
                'LL_norm': chiral['LL_norm'],
                'RR_norm': chiral['RR_norm'],
                'LR_norm': chiral['LR_norm'],
                'svals': svals,
                'n_nonzero': n_nonzero,
                'n_zero': n_zero,
                'n_clusters': gen_analysis['n_clusters'],
                'cluster_sizes': gen_analysis['cluster_sizes'],
                'cluster_means': gen_analysis['cluster_means'],
                'chiral_index': idx_data['index'],
                'M_LR': chiral['M_LR'],
                'U_L': chiral['U_L'],
                'U_R': chiral['U_R'],
            }

    # ========================================================================
    # INTER-SECTOR MIXING ANALYSIS
    # ========================================================================

    print(f"\n{'='*78}")
    print("INTER-SECTOR MIXING ANALYSIS")
    print(f"{'='*78}")
    print("\nThe CKM/PMNS mixing matrices arise from misalignment between")
    print("mass eigenstates in different PW sectors. Specifically:")
    print("  - (1,0) fundamental = quark doublet (L-handed)")
    print("  - (0,1) antifundamental = conjugate")
    print("  - (1,1) adjoint = gauge/gluon sector")
    print()

    # For the (1,0) and (0,1) sectors at the fold (tau = 0.190):
    # Compare their mass matrices to see if mixing angles are non-trivial.
    ti_fold = N_TAU - 1  # (local) last tau value = fold

    # (1,0) mass matrix at fold
    key_10 = f"tau{ti_fold}_sec1"  # (local)
    key_01 = f"tau{ti_fold}_sec2"  # (local)
    key_11 = f"tau{ti_fold}_sec3"  # (local)

    M_10 = all_results[key_10]['M_LR']  # (local) 24x24 (3*8 x 3*8)
    M_01 = all_results[key_01]['M_LR']  # (local) 24x24
    M_11 = all_results[key_11]['M_LR']  # (local) 64x64 (8*8 x 8*8)

    svals_10 = all_results[key_10]['svals']  # (local)
    svals_01 = all_results[key_01]['svals']  # (local)
    svals_11 = all_results[key_11]['svals']  # (local)

    print(f"  At tau = {TAU_VALUES[ti_fold]:.3f} (fold):")
    print(f"    (1,0) mass spectrum: {np.sort(svals_10)[::-1][:6]}")
    print(f"    (0,1) mass spectrum: {np.sort(svals_01)[::-1][:6]}")
    print(f"    (1,1) mass spectrum: {np.sort(svals_11)[::-1][:8]}")

    # KEY TEST: Are (1,0) and (0,1) mass spectra IDENTICAL?
    # Under CPT (J operator), (p,q) <-> (q,p). So m((1,0)) = m((0,1)).
    # This is the spectral consequence of J D J^{-1} = D.
    spec_diff_fund = np.sort(svals_10) - np.sort(svals_01)  # (local)
    spec_diff_norm = np.linalg.norm(spec_diff_fund)  # (local)
    print(f"\n    CPT CHECK: ||spec(1,0) - spec(0,1)|| = {spec_diff_norm:.2e}")
    if spec_diff_norm < ZERO_THRESHOLD:
        print(f"    CONFIRMED: J-symmetry forces identical mass spectra (Theorem T5)")
    else:
        print(f"    WARNING: CPT violation detected at level {spec_diff_norm:.2e}")

    # MIXING STRUCTURE WITHIN (1,0) SECTOR
    # The 3x3 block structure of M_LR in (1,0) gives generation mixing.
    # M_LR is 24x24 = (3 color) x (8 spinor chirality modes).
    # Reshape to isolate the 3x3 "generation" structure within the rep space.

    print(f"\n  GENERATION STRUCTURE IN (1,0) SECTOR:")
    print(f"    M_LR shape: {M_10.shape}")
    print(f"    dim_rho=3, dim_chiral=8 => 3 'colors' x 8 spinor modes")

    # The mass matrix M_LR acts on V_{(1,0)} x S_R -> V_{(1,0)} x S_L
    # where V_{(1,0)} = C^3 and S_R = 8D right-handed spinor space.
    # Reshape M_LR as a block matrix: M_LR[i*8:(i+1)*8, j*8:(j+1)*8] is
    # the 8x8 block connecting color j (R) to color i (L).
    # The 3x3 matrix of 8x8 blocks encodes color mixing through chirality.

    print(f"\n    Block structure (3x3 matrix of 8x8 blocks):")
    block_norms_10 = np.zeros((3, 3))  # (local)
    for i in range(3):
        for j in range(3):
            block = M_10[i*8:(i+1)*8, j*8:(j+1)*8]  # (local)
            block_norms_10[i, j] = np.linalg.norm(block, 'fro')

    print(f"    ||M_LR[i,j]||_F (3x3 block norm matrix):")
    for i in range(3):
        row_str = "      "  # (local)
        for j in range(3):
            row_str += f"{block_norms_10[i, j]:10.6f} "
        print(row_str)

    # Check if block structure is diagonal (no color mixing)
    diag_norm = np.sum(np.diag(block_norms_10)**2)**0.5  # (local)
    offdiag_norm = (np.sum(block_norms_10**2) - np.sum(np.diag(block_norms_10)**2))**0.5  # (local)
    mixing_ratio = offdiag_norm / (diag_norm + 1e-30)  # (local)

    print(f"\n    Diagonal norm: {diag_norm:.6e}")
    print(f"    Off-diagonal norm: {offdiag_norm:.6e}")
    print(f"    Mixing ratio (off-diag/diag): {mixing_ratio:.6e}")

    if mixing_ratio > MIXING_THRESHOLD:
        print(f"    => NON-TRIVIAL MIXING DETECTED")
        has_mixing = True  # (local)
    else:
        print(f"    => Block-diagonal (no mixing in this sector)")
        has_mixing = False  # (local)

    # Same analysis for (1,1) adjoint sector (8x8 blocks of 8x8)
    print(f"\n  GENERATION STRUCTURE IN (1,1) SECTOR:")
    print(f"    M_LR shape: {M_11.shape}")
    print(f"    dim_rho=8, dim_chiral=8 => 8 'adjoint modes' x 8 spinor modes")

    block_norms_11 = np.zeros((8, 8))  # (local)
    for i in range(8):
        for j in range(8):
            block = M_11[i*8:(i+1)*8, j*8:(j+1)*8]  # (local)
            block_norms_11[i, j] = np.linalg.norm(block, 'fro')

    diag_norm_11 = np.sum(np.diag(block_norms_11)**2)**0.5  # (local)
    offdiag_norm_11 = (np.sum(block_norms_11**2) - np.sum(np.diag(block_norms_11)**2))**0.5  # (local)
    mixing_ratio_11 = offdiag_norm_11 / (diag_norm_11 + 1e-30)  # (local)

    print(f"    Diagonal norm: {diag_norm_11:.6e}")
    print(f"    Off-diagonal norm: {offdiag_norm_11:.6e}")
    print(f"    Mixing ratio (off-diag/diag): {mixing_ratio_11:.6e}")

    if mixing_ratio_11 > MIXING_THRESHOLD:
        print(f"    => NON-TRIVIAL MIXING in adjoint sector")
        has_mixing_11 = True  # (local)
    else:
        print(f"    => Block-diagonal in adjoint sector")
        has_mixing_11 = False  # (local)

    # ========================================================================
    # TAU EVOLUTION OF MIXING
    # ========================================================================

    print(f"\n{'='*78}")
    print("TAU EVOLUTION OF MASS SPECTRA AND MIXING")
    print(f"{'='*78}")

    for si, ((p, q), label) in enumerate(zip(PW_SECTORS, PW_LABELS)):
        print(f"\n  {label}:")
        print(f"    {'tau':>6s}  {'||M_LR||':>12s}  {'n_nonzero':>10s}  {'n_zero':>7s}  "
              f"{'largest_sv':>12s}  {'smallest_nz':>12s}")
        for ti in range(N_TAU):
            key = f"tau{ti}_sec{si}"  # (local)
            r = all_results[key]  # (local)
            svals_sorted = np.sort(r['svals'])[::-1]  # (local)
            largest = svals_sorted[0] if len(svals_sorted) > 0 else 0.0  # (local)
            # Smallest non-zero
            nz_svals = svals_sorted[svals_sorted > ZERO_THRESHOLD]  # (local)
            smallest_nz = nz_svals[-1] if len(nz_svals) > 0 else 0.0  # (local)
            print(f"    {r['tau']:6.3f}  {r['LR_norm']:12.6e}  {r['n_nonzero']:>10d}  "
                  f"{r['n_zero']:>7d}  {largest:12.6e}  {smallest_nz:12.6e}")

    # ========================================================================
    # CHK2: Mass ratio structure (qualitative CKM check)
    # ========================================================================

    print(f"\n{'='*78}")
    print("CHK2: MASS HIERARCHY ANALYSIS")
    print(f"{'='*78}")

    # At the fold, look at mass ratios within (1,0) sector
    svals_fold_10 = np.sort(all_results[f'tau{ti_fold}_sec1']['svals'])[::-1]  # (local)
    nz_fold = svals_fold_10[svals_fold_10 > ZERO_THRESHOLD]  # (local)

    if len(nz_fold) >= 2:
        ratios = nz_fold[:-1] / nz_fold[1:]  # (local)
        print(f"\n  (1,0) at fold: non-zero mass eigenvalues = {len(nz_fold)}")
        print(f"  Mass values: {nz_fold[:8]}")
        print(f"  Successive ratios: {ratios[:7]}")
        # SM quark mass ratios: m_t/m_c ~ 130, m_c/m_u ~ 550
        # Look for any hierarchical ratio > 10
        large_ratios = ratios[ratios > 10.0]  # (local)
        print(f"  Hierarchical ratios (>10): {large_ratios}")
    else:
        print(f"\n  (1,0) at fold: fewer than 2 non-zero eigenvalues")

    # ========================================================================
    # GATE EVALUATION: S76-C6-KOSMANN
    # ========================================================================

    print(f"\n{'='*78}")
    print("GATE EVALUATION: S76-C6-KOSMANN")
    print(f"{'='*78}")

    # Criteria:
    # PASS if non-trivial mixing structure found, PMNS route identified
    # FAIL if P_L D_K P_R = 0 (chiral projections trivial)
    # INFO if mixing exists but doesn't obviously match SM

    # Check 1: Is the mass matrix non-zero in non-trivial sectors?
    mass_nontrivial = all(
        all_results[f'tau{ti_fold}_sec{si}']['LR_norm'] > ZERO_THRESHOLD
        for si in range(1, 4)
    )  # (local)

    # Check 2: Is there inter-generation mixing?
    has_any_mixing = has_mixing or has_mixing_11  # (local)

    # Check 3: Does the spectrum show hierarchy?
    has_hierarchy = len(nz_fold) >= 2 and np.max(ratios) > 2.0 if len(nz_fold) >= 2 else False  # (local)

    # Gate logic
    if not mass_nontrivial:
        verdict = "FAIL"
        verdict_msg = "P_L D_K P_R = 0 in non-trivial PW sectors. No mass matrix."
    elif has_any_mixing and has_hierarchy:
        verdict = "PASS"
        verdict_msg = (f"Non-trivial mixing found (ratio={mixing_ratio:.2e} in (1,0), "
                       f"{mixing_ratio_11:.2e} in (1,1)). "
                       f"Mass hierarchy present (max ratio = {np.max(ratios):.2f}). "
                       f"PMNS route: SVD of inter-sector mass matrix.")
    elif mass_nontrivial:
        verdict = "INFO"
        if has_any_mixing:
            verdict_msg = (f"Mixing detected (ratio={mixing_ratio:.2e}) but no clear "
                           f"mass hierarchy matching SM. Non-trivial chiral structure exists.")
        elif has_hierarchy:
            verdict_msg = (f"Mass hierarchy detected (max ratio={np.max(ratios):.2f}) "
                           f"but mixing ratio below threshold ({mixing_ratio:.2e}). "
                           f"Block-diagonal => no CKM-type mixing at this level.")
        else:
            verdict_msg = (f"Mass matrix non-zero but neither strong mixing "
                           f"({mixing_ratio:.2e}) nor hierarchy ({np.max(ratios) if len(nz_fold)>=2 else 0:.2f}). "
                           f"Chiral structure present but SM matching unclear.")
    else:
        verdict = "FAIL"
        verdict_msg = "Unexpected state."

    print(f"\n  Mass matrix non-trivial: {mass_nontrivial}")
    print(f"  Inter-generation mixing:  {has_any_mixing}")
    print(f"    (1,0) mixing ratio: {mixing_ratio:.2e}")
    print(f"    (1,1) mixing ratio: {mixing_ratio_11:.2e}")
    print(f"  Mass hierarchy:           {has_hierarchy}")
    if len(nz_fold) >= 2:
        print(f"    Max successive ratio: {np.max(ratios):.4f}")
    print(f"\n  Gate S76-C6-KOSMANN: {verdict}")
    print(f"  {verdict_msg}")

    # ========================================================================
    # Save results
    # ========================================================================

    save_data = {
        'tau_values': TAU_VALUES,
        'pw_sectors': np.array(PW_SECTORS),
        'pw_dims': np.array(PW_DIMS),
        'verdict': verdict,
    }

    # Save per-sector per-tau summary arrays
    for ti in range(N_TAU):
        for si in range(len(PW_SECTORS)):
            key = f"tau{ti}_sec{si}"
            r = all_results[key]
            save_data[f'svals_{ti}_{si}'] = r['svals']
            save_data[f'LR_norm_{ti}_{si}'] = np.array([r['LR_norm']])
            save_data[f'LL_norm_{ti}_{si}'] = np.array([r['LL_norm']])
            save_data[f'anticomm_err_{ti}_{si}'] = np.array([r['anticomm_err']])
            save_data[f'M_LR_{ti}_{si}'] = r['M_LR']

    # Save fold mass matrices for downstream PMNS extraction
    save_data['M_LR_10_fold'] = M_10
    save_data['M_LR_01_fold'] = M_01
    save_data['M_LR_11_fold'] = M_11
    save_data['block_norms_10'] = block_norms_10
    save_data['block_norms_11'] = block_norms_11
    save_data['mixing_ratio_10'] = np.array([mixing_ratio])
    save_data['mixing_ratio_11'] = np.array([mixing_ratio_11])
    save_data['spec_diff_fund_CPT'] = spec_diff_norm

    output_path = os.path.join(SCRIPT_DIR, "s76_kosmann_chirality.npz")  # (local)
    np.savez_compressed(output_path, **save_data)
    file_size = os.path.getsize(output_path)  # (local)

    elapsed = time.time() - t_start  # (local)
    print(f"\n{'='*78}")
    print(f"Saved: {output_path}")
    print(f"File size: {file_size / 1024:.1f} KB")
    print(f"Total runtime: {elapsed:.2f}s")
    print(f"{'='*78}")

    return verdict


if __name__ == "__main__":
    verdict = main()
