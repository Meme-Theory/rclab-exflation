#!/usr/bin/env python3
"""
COH-35: Intra-B2 Coherence Under Wall Transport
=================================================
Quantifies whether BCS pairing coherence survives transport across
the domain wall by computing eigenvector overlap matrices between
tau = 0.20 (fold center) and tau = 0.15 / tau = 0.25 (wall endpoints).

Physics:
  The BCS gap function Delta is the dominant eigenvector of the Thouless
  matrix M_nm = V_nm * rho_m / (2 * |xi_m|) at the fold center tau = 0.20.
  When the system is transported to a neighboring tau, the eigenbasis
  rotates. The transported pairing amplitude is:

    Delta_transported(tau') = O^dagger(tau_0, tau') * Delta(tau_0)

  where O_ij = <psi_i(tau_0) | psi_j(tau')> is the overlap matrix
  restricted to the B2+B1 subspace.

  The coherence fraction is:
    C = |Delta_transported|^2 / |Delta|^2

  If C ~ 1, the BCS pairing survives transport. If C << 1, the
  eigenvector rotation destroys pairing coherence.

  Additionally, we compute the EFFECTIVE transported Thouless matrix:
    M_eff(tau') = O^dag * M(tau_0) * O
  and check whether its largest eigenvalue is preserved.

Gate COH-35 (INFORMATIVE):
  Overlap > 0.7 = coherence preserved
  Overlap < 0.5 = coherence destroyed

Author: gen-physicist, Session 35
Date: 2026-03-07
Source data: s23a_kosmann_singlet.npz, s35a_vh_impedance_arbiter.npz
"""

import os
import time
import numpy as np
from scipy.linalg import eigh, svd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ======================================================================
#  Paths
# ======================================================================
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = SCRIPT_DIR

SINGLET_FILE = os.path.join(DATA_DIR, "s23a_kosmann_singlet.npz")
VH_FILE = os.path.join(DATA_DIR, "s35a_vh_impedance_arbiter.npz")
OUTPUT_NPZ = os.path.join(DATA_DIR, "s35_b2_coherence.npz")
OUTPUT_PNG = os.path.join(DATA_DIR, "s35_b2_coherence.png")

# ======================================================================
#  Constants
# ======================================================================
TAU_VALUES = np.array([0.0, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.50])

# Full 16-mode index assignments (eigenvalues sorted ascending):
# Negative sector (0-7): B3_neg=[0,1,2], B2_neg=[3,4,5,6], B1_neg=[7]
# Positive sector (8-15): B1_pos=[8], B2_pos=[9,10,11,12], B3_pos=[13,14,15]
B1_POS = [8]
B2_POS = [9, 10, 11, 12]
B3_POS = [13, 14, 15]
B2B1_POS = B2_POS + B1_POS   # [9, 10, 11, 12, 8] — 5 modes

# Branch indices in the 8-mode positive-sector basis (used for Thouless)
B2_8 = np.array([3, 4, 5, 6])   # B2 in pos sector
B1_8 = np.array([7])             # B1 in pos sector
B2B1_8 = np.array([3, 4, 5, 6, 7])

# Regulator
ETA_REG_FRAC = 0.001

# Multi-sector factor (from SECT-33a)
MULTI_SECTOR_FACTOR = 1.046


# ======================================================================
#  Overlap Matrix Construction
# ======================================================================

def compute_overlap_16x16(kosmann, idx_ref, idx_target):
    """Compute full 16x16 overlap matrix O = <psi_i(ref)|psi_j(target)>.

    Returns unitary matrix O where O_ij gives the projection of
    eigenvector i at tau_ref onto eigenvector j at tau_target.
    """
    evecs_ref = kosmann[f'eigenvectors_{idx_ref}']
    evecs_tgt = kosmann[f'eigenvectors_{idx_target}']
    O = evecs_ref.conj().T @ evecs_tgt
    return O


def extract_B2B1_block(O_full):
    """Extract the 5x5 B2+B1 overlap block from the 16x16 matrix.

    Rows and columns correspond to B2_POS + B1_POS = [9,10,11,12,8].
    """
    return O_full[np.ix_(B2B1_POS, B2B1_POS)]


def extract_B2_block(O_full):
    """Extract the 4x4 B2-only overlap block from the 16x16 matrix."""
    return O_full[np.ix_(B2_POS, B2_POS)]


# ======================================================================
#  Thouless Matrix and BCS Gap Function
# ======================================================================

def build_V_pairing_B2B1(kosmann, tau_idx):
    """Extract the 5x5 V_pairing submatrix for B2+B1 positive modes.

    V_pairing is stored as 16x16. We extract the B2B1 block.
    """
    V_full = kosmann[f'V_pairing_{tau_idx}']
    return V_full[np.ix_(B2B1_POS, B2B1_POS)]


def build_thouless_matrix(V_5x5, E_5, mu, rho_B2, rho_B1):
    """Build the 5x5 Thouless matrix M_nm = V_nm * rho_m / (2*|xi_m|).

    Parameters:
        V_5x5: pairing interaction in B2+B1 subspace
        E_5: eigenvalues for B2(4) + B1(1) modes
        mu: chemical potential
        rho_B2: DOS per mode for B2
        rho_B1: DOS per mode for B1
    """
    xi = E_5 - mu
    lambda_min = np.min(np.abs(E_5))
    eta = max(ETA_REG_FRAC * lambda_min, 1e-15)
    abs_xi = np.maximum(np.abs(xi), eta)

    rho = np.array([rho_B2] * 4 + [rho_B1])

    M = np.zeros((5, 5))
    for m in range(5):
        M[:, m] = V_5x5[:, m] * rho[m] / (2.0 * abs_xi[m])

    return M


def get_bcs_gap_function(M):
    """Compute the BCS gap function = dominant eigenvector of M.

    The Thouless criterion is: BCS instability when max Re(eigenvalue of M) > 1.
    The gap function Delta is the corresponding eigenvector.

    Returns:
        M_max: largest real eigenvalue
        Delta: corresponding eigenvector (normalized)
        evals: all eigenvalues of M
    """
    evals, evecs = np.linalg.eig(M)
    idx_max = np.argmax(np.real(evals))
    M_max = np.real(evals[idx_max])
    Delta = evecs[:, idx_max]

    # Normalize
    Delta = Delta / np.linalg.norm(Delta)

    # Fix phase: make largest component real and positive
    idx_largest = np.argmax(np.abs(Delta))
    Delta *= np.conj(Delta[idx_largest]) / np.abs(Delta[idx_largest])

    return M_max, Delta, evals


# ======================================================================
#  Coherence Transport Computation
# ======================================================================

def transport_gap_function(Delta_ref, O_B2B1):
    """Transport the BCS gap function through the overlap matrix.

    The transported gap function at tau_target is:
        Delta_transported = O^dagger * Delta_ref

    where O = <psi_i(ref)|psi_j(target)> in the B2+B1 subspace.

    This computes how much of the original pairing amplitude projects
    onto the eigenbasis at the target tau.

    Returns:
        Delta_transported: the gap function expressed in the target basis
        coherence_fraction: |Delta_transported|^2 / |Delta_ref|^2
    """
    Delta_transported = O_B2B1.conj().T @ Delta_ref
    coherence = np.sum(np.abs(Delta_transported)**2) / np.sum(np.abs(Delta_ref)**2)
    return Delta_transported, coherence


def transport_thouless_matrix(M_ref, O_B2B1):
    """Transport the Thouless matrix: M_eff = O^dag M O.

    This computes what the effective Thouless matrix looks like
    in the target tau eigenbasis, assuming the pairing interaction
    is generated at tau_ref and then transported.

    Returns:
        M_eff: effective Thouless matrix at target tau
        M_max_eff: largest real eigenvalue of M_eff
    """
    M_eff = O_B2B1.conj().T @ M_ref @ O_B2B1
    evals_eff = np.linalg.eigvals(M_eff)
    M_max_eff = np.max(np.real(evals_eff))
    return M_eff, M_max_eff, evals_eff


def compute_full_coherence_analysis(kosmann, vh_data, tau_ref_idx, tau_target_idx,
                                     label, rho_B2, rho_B1=1.0, mu=0.0):
    """Full coherence analysis between tau_ref and tau_target.

    Returns dict with all results.
    """
    tau_ref = TAU_VALUES[tau_ref_idx]
    tau_target = TAU_VALUES[tau_target_idx]

    # 1. Build Thouless matrix at reference tau
    V_ref = build_V_pairing_B2B1(kosmann, tau_ref_idx)
    evals_ref = kosmann[f'eigenvalues_{tau_ref_idx}']
    pos_ref = np.sort(evals_ref[evals_ref > 0])
    E_B2B1_ref = np.array([pos_ref[1], pos_ref[2], pos_ref[3], pos_ref[4], pos_ref[0]])

    M_ref = build_thouless_matrix(V_ref, E_B2B1_ref, mu, rho_B2, rho_B1)
    M_max_ref, Delta_ref, evals_M_ref = get_bcs_gap_function(M_ref)

    # 2. Build overlap matrix
    O_full = compute_overlap_16x16(kosmann, tau_ref_idx, tau_target_idx)
    O_B2B1 = extract_B2B1_block(O_full)
    O_B2 = extract_B2_block(O_full)

    # 3. SVD analysis of overlap blocks
    sv_B2B1 = svd(O_B2B1, compute_uv=False)
    sv_B2 = svd(O_B2, compute_uv=False)
    sv_full = svd(O_full, compute_uv=False)

    # 4. Transport gap function
    Delta_transported, coherence_frac = transport_gap_function(Delta_ref, O_B2B1)

    # 5. Transport Thouless matrix
    M_eff, M_max_eff, evals_M_eff = transport_thouless_matrix(M_ref, O_B2B1)

    # 6. Also compute local Thouless matrix at target tau for comparison
    V_tgt = build_V_pairing_B2B1(kosmann, tau_target_idx)
    evals_tgt = kosmann[f'eigenvalues_{tau_target_idx}']
    pos_tgt = np.sort(evals_tgt[evals_tgt > 0])
    E_B2B1_tgt = np.array([pos_tgt[1], pos_tgt[2], pos_tgt[3], pos_tgt[4], pos_tgt[0]])

    M_local = build_thouless_matrix(V_tgt, E_B2B1_tgt, mu, rho_B2, rho_B1)
    M_max_local, Delta_local, evals_M_local = get_bcs_gap_function(M_local)

    # 7. Overlap between transported and local gap functions
    delta_overlap = np.abs(np.dot(Delta_transported.conj(), Delta_local))**2

    # 8. Branch-resolved analysis: how much B2 stays in B2?
    # Transmission in full 16: for each B2+ mode at ref, how much stays in B2+ at target?
    T_B2_stay = np.zeros(4)
    T_B2_to_B1 = np.zeros(4)
    T_B2_to_B3 = np.zeros(4)
    T_B2_to_neg = np.zeros(4)
    for i, k in enumerate(B2_POS):
        T_B2_stay[i] = sum(np.abs(O_full[k, l])**2 for l in B2_POS)
        T_B2_to_B1[i] = sum(np.abs(O_full[k, l])**2 for l in B1_POS)
        T_B2_to_B3[i] = sum(np.abs(O_full[k, l])**2 for l in B3_POS)
        T_B2_to_neg[i] = sum(np.abs(O_full[k, l])**2 for l in range(8))

    # B1 transmission
    T_B1_stay = sum(np.abs(O_full[8, l])**2 for l in B1_POS)
    T_B1_to_B2 = sum(np.abs(O_full[8, l])**2 for l in B2_POS)

    results = {
        'label': label,
        'tau_ref': tau_ref,
        'tau_target': tau_target,
        'M_max_ref': M_max_ref,
        'Delta_ref': Delta_ref,
        'evals_M_ref': evals_M_ref,
        'O_full': O_full,
        'O_B2B1': O_B2B1,
        'O_B2': O_B2,
        'sv_B2B1': sv_B2B1,
        'sv_B2': sv_B2,
        'sv_full': sv_full,
        'Delta_transported': Delta_transported,
        'coherence_fraction': coherence_frac,
        'M_eff': M_eff,
        'M_max_eff': M_max_eff,
        'evals_M_eff': evals_M_eff,
        'M_max_local': M_max_local,
        'Delta_local': Delta_local,
        'evals_M_local': evals_M_local,
        'delta_overlap': delta_overlap,
        'T_B2_stay': T_B2_stay,
        'T_B2_to_B1': T_B2_to_B1,
        'T_B2_to_B3': T_B2_to_B3,
        'T_B2_to_neg': T_B2_to_neg,
        'T_B1_stay': T_B1_stay,
        'T_B1_to_B2': T_B1_to_B2,
        'V_ref': V_ref,
        'E_B2B1_ref': E_B2B1_ref,
        'V_tgt': V_tgt,
        'E_B2B1_tgt': E_B2B1_tgt,
    }
    return results


# ======================================================================
#  Continuous tau scan (finer grid via interpolation)
# ======================================================================

def coherence_vs_tau_scan(kosmann, tau_ref_idx, rho_B2, rho_B1=1.0, mu=0.0):
    """Compute coherence fraction for all available tau targets vs tau_ref.

    Returns arrays for plotting.
    """
    n_tau = len(TAU_VALUES)
    coh_fracs = np.zeros(n_tau)
    M_max_transported = np.zeros(n_tau)
    M_max_local = np.zeros(n_tau)
    sv_min_B2B1 = np.zeros(n_tau)

    for idx in range(n_tau):
        if idx == tau_ref_idx:
            coh_fracs[idx] = 1.0
            # Build local M
            V_loc = build_V_pairing_B2B1(kosmann, idx)
            evals_loc = kosmann[f'eigenvalues_{idx}']
            pos_loc = np.sort(evals_loc[evals_loc > 0])
            E_loc = np.array([pos_loc[1], pos_loc[2], pos_loc[3], pos_loc[4], pos_loc[0]])
            M_loc = build_thouless_matrix(V_loc, E_loc, mu, rho_B2, rho_B1)
            M_max_val, _, _ = get_bcs_gap_function(M_loc)
            M_max_transported[idx] = M_max_val
            M_max_local[idx] = M_max_val
            sv_min_B2B1[idx] = 1.0
            continue

        res = compute_full_coherence_analysis(
            kosmann, None, tau_ref_idx, idx,
            f"tau={TAU_VALUES[tau_ref_idx]:.2f}->{TAU_VALUES[idx]:.2f}",
            rho_B2, rho_B1, mu
        )
        coh_fracs[idx] = res['coherence_fraction']
        M_max_transported[idx] = res['M_max_eff']
        M_max_local[idx] = res['M_max_local']
        sv_min_B2B1[idx] = np.min(res['sv_B2B1'])

    return coh_fracs, M_max_transported, M_max_local, sv_min_B2B1


# ======================================================================
#  Main
# ======================================================================

def main():
    t0 = time.time()
    print("=" * 80)
    print("COH-35: Intra-B2 Coherence Under Wall Transport")
    print("=" * 80)
    print()

    # Load data
    kosmann = np.load(SINGLET_FILE, allow_pickle=True)
    vh_data = np.load(VH_FILE, allow_pickle=True)

    # Get physical rho from VH arbiter
    rho_phys = float(vh_data['rho_phys_per_mode'])
    rho_phys_eff = float(vh_data['rho_phys_eff'])
    print(f"Physical rho_per_mode from VH arbiter: {rho_phys:.4f}")
    print(f"Physical rho_eff (with SECT factor): {rho_phys_eff:.4f}")
    print()

    # Reference: tau = 0.20 (index 3), which is closest to the fold at tau ~ 0.190
    tau_ref_idx = 3
    print(f"Reference tau = {TAU_VALUES[tau_ref_idx]:.2f} (fold center)")
    print()

    # ================================================================
    #  Primary computations: tau=0.20 -> tau=0.15 and tau=0.20 -> tau=0.25
    # ================================================================

    # Use physical rho for the Thouless matrix
    rho_B2 = rho_phys_eff
    rho_B1 = 1.0  # B1 is not at the van Hove singularity

    print("=" * 60)
    print("  TRANSPORT: tau=0.20 -> tau=0.15 (inward, toward B3 crossing)")
    print("=" * 60)
    res_15 = compute_full_coherence_analysis(
        kosmann, vh_data, tau_ref_idx, 2,  # idx 2 = tau=0.15
        "tau=0.20->0.15", rho_B2, rho_B1
    )
    print_results(res_15)

    print()
    print("=" * 60)
    print("  TRANSPORT: tau=0.20 -> tau=0.25 (outward, toward larger tau)")
    print("=" * 60)
    res_25 = compute_full_coherence_analysis(
        kosmann, vh_data, tau_ref_idx, 4,  # idx 4 = tau=0.25
        "tau=0.20->0.25", rho_B2, rho_B1
    )
    print_results(res_25)

    # ================================================================
    #  Full tau scan from tau=0.20
    # ================================================================
    print()
    print("=" * 60)
    print("  FULL TAU SCAN (reference: tau=0.20)")
    print("=" * 60)
    coh_scan, M_trans_scan, M_local_scan, sv_min_scan = coherence_vs_tau_scan(
        kosmann, tau_ref_idx, rho_B2, rho_B1
    )
    print(f"{'tau':>6s}  {'C_frac':>8s}  {'M_transported':>14s}  {'M_local':>8s}  {'sv_min':>8s}")
    print("-" * 52)
    for i in range(len(TAU_VALUES)):
        print(f"{TAU_VALUES[i]:6.2f}  {coh_scan[i]:8.6f}  {M_trans_scan[i]:14.6f}  "
              f"{M_local_scan[i]:8.6f}  {sv_min_scan[i]:8.6f}")

    # ================================================================
    #  Also compute at a LOWER rho (step-function reference) for comparison
    # ================================================================
    rho_step = float(vh_data['rho_step'])
    print()
    print(f"Step-function rho = {rho_step:.4f} (for comparison)")
    res_15_step = compute_full_coherence_analysis(
        kosmann, vh_data, tau_ref_idx, 2,
        "tau=0.20->0.15 (step rho)", rho_step * MULTI_SECTOR_FACTOR, rho_B1
    )
    res_25_step = compute_full_coherence_analysis(
        kosmann, vh_data, tau_ref_idx, 4,
        "tau=0.20->0.25 (step rho)", rho_step * MULTI_SECTOR_FACTOR, rho_B1
    )
    print(f"  Step rho: C(0.20->0.15) = {res_15_step['coherence_fraction']:.6f}, "
          f"M_eff = {res_15_step['M_max_eff']:.6f}")
    print(f"  Step rho: C(0.20->0.25) = {res_25_step['coherence_fraction']:.6f}, "
          f"M_eff = {res_25_step['M_max_eff']:.6f}")

    # ================================================================
    #  Cross-check with VH arbiter overlap data
    # ================================================================
    print()
    print("=" * 60)
    print("  CROSS-CHECK: VH arbiter O_full (tau=0.15->0.25)")
    print("=" * 60)
    O_vh = vh_data['O_full']
    O_B2_vh = vh_data['O_B2_block']
    T_branch_vh = vh_data['T_branch_B2']
    print(f"  VH O_B2 SVD: {svd(O_B2_vh, compute_uv=False)}")
    print(f"  VH T_branch_B2: {T_branch_vh}")
    print(f"  VH impedance: {float(vh_data['impedance_from_overlap']):.4f}")

    # Our O(0.15->0.25) for comparison
    O_ours = compute_overlap_16x16(kosmann, 2, 4)
    O_B2_ours = extract_B2_block(O_ours)
    print(f"  Our O_B2(0.15->0.25) SVD: {svd(O_B2_ours, compute_uv=False)}")
    T_branch_ours = np.array([sum(np.abs(O_ours[k, l])**2 for l in B2_POS) for k in B2_POS])
    print(f"  Our T_branch_B2: {T_branch_ours}")

    # ================================================================
    #  Gate verdict
    # ================================================================
    print()
    print("=" * 60)
    print("  GATE COH-35 VERDICT")
    print("=" * 60)

    c_15 = res_15['coherence_fraction']
    c_25 = res_25['coherence_fraction']
    c_min = min(c_15, c_25)

    print(f"  Coherence fraction (tau=0.20 -> 0.15): {c_15:.6f}")
    print(f"  Coherence fraction (tau=0.20 -> 0.25): {c_25:.6f}")
    print(f"  Minimum coherence: {c_min:.6f}")
    print()

    if c_min > 0.7:
        verdict = "PASS"
        print(f"  COH-35: {verdict} (C_min = {c_min:.4f} > 0.7)")
        print("  Pairing coherence PRESERVED under wall transport.")
    elif c_min > 0.5:
        verdict = "MARGINAL"
        print(f"  COH-35: {verdict} (0.5 < C_min = {c_min:.4f} < 0.7)")
        print("  Pairing coherence PARTIALLY preserved.")
    else:
        verdict = "FAIL"
        print(f"  COH-35: {verdict} (C_min = {c_min:.4f} < 0.5)")
        print("  Pairing coherence DESTROYED under wall transport.")

    # ================================================================
    #  Additional diagnostic: is the coherence loss from B2 mixing or B2-B1?
    # ================================================================
    print()
    print("=" * 60)
    print("  DIAGNOSTIC: Source of Coherence Loss")
    print("=" * 60)
    for label, res in [("0.20->0.15", res_15), ("0.20->0.25", res_25)]:
        print(f"\n  {label}:")
        print(f"    B2 intra-branch transmission: {res['T_B2_stay']}")
        print(f"    B2->B1 leakage: {res['T_B2_to_B1']}")
        print(f"    B2->B3 leakage: {res['T_B2_to_B3']}")
        print(f"    B2->negative leakage: {res['T_B2_to_neg']}")
        print(f"    B1 self-overlap: {res['T_B1_stay']:.6f}")
        print(f"    B1->B2 leakage: {res['T_B1_to_B2']:.6f}")
        print(f"    O_B2B1 SVD: {res['sv_B2B1']}")
        print(f"    O_B2 SVD: {res['sv_B2']}")
        print(f"    Delta_ref: {res['Delta_ref']}")
        print(f"    Delta_transported: {res['Delta_transported']}")
        print(f"    Delta_local: {res['Delta_local']}")
        print(f"    <Delta_transported|Delta_local>^2: {res['delta_overlap']:.6f}")

    # ================================================================
    #  Save data
    # ================================================================
    save_dict = {
        # Primary results
        'tau_ref': TAU_VALUES[tau_ref_idx],
        'tau_target_lo': TAU_VALUES[2],
        'tau_target_hi': TAU_VALUES[4],
        'rho_B2_used': rho_B2,
        'rho_B1_used': rho_B1,

        # Coherence fractions
        'coherence_frac_lo': c_15,
        'coherence_frac_hi': c_25,
        'coherence_min': c_min,

        # Overlap matrices
        'O_full_20_15': res_15['O_full'],
        'O_full_20_25': res_25['O_full'],
        'O_B2B1_20_15': res_15['O_B2B1'],
        'O_B2B1_20_25': res_25['O_B2B1'],
        'O_B2_20_15': res_15['O_B2'],
        'O_B2_20_25': res_25['O_B2'],

        # SVD values
        'sv_B2B1_20_15': res_15['sv_B2B1'],
        'sv_B2B1_20_25': res_25['sv_B2B1'],
        'sv_B2_20_15': res_15['sv_B2'],
        'sv_B2_20_25': res_25['sv_B2'],

        # Thouless analysis
        'M_max_ref': res_15['M_max_ref'],
        'M_max_eff_lo': res_15['M_max_eff'],
        'M_max_eff_hi': res_25['M_max_eff'],
        'M_max_local_lo': res_15['M_max_local'],
        'M_max_local_hi': res_25['M_max_local'],

        # Gap functions
        'Delta_ref': res_15['Delta_ref'],
        'Delta_transported_lo': res_15['Delta_transported'],
        'Delta_transported_hi': res_25['Delta_transported'],
        'Delta_local_lo': res_15['Delta_local'],
        'Delta_local_hi': res_25['Delta_local'],

        # Gap function overlaps
        'delta_overlap_lo': res_15['delta_overlap'],
        'delta_overlap_hi': res_25['delta_overlap'],

        # Branch transmission
        'T_B2_stay_lo': res_15['T_B2_stay'],
        'T_B2_stay_hi': res_25['T_B2_stay'],
        'T_B2_to_B1_lo': res_15['T_B2_to_B1'],
        'T_B2_to_B1_hi': res_25['T_B2_to_B1'],
        'T_B1_stay_lo': res_15['T_B1_stay'],
        'T_B1_stay_hi': res_25['T_B1_stay'],

        # Full scan
        'tau_scan': TAU_VALUES,
        'coherence_scan': coh_scan,
        'M_transported_scan': M_trans_scan,
        'M_local_scan': M_local_scan,
        'sv_min_scan': sv_min_scan,

        # Gate
        'gate_verdict': np.array([verdict]),
    }

    np.savez_compressed(OUTPUT_NPZ, **save_dict)
    print(f"\nData saved to: {OUTPUT_NPZ}")

    # ================================================================
    #  Plotting
    # ================================================================
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle("COH-35: Intra-B2 Coherence Under Wall Transport", fontsize=14, fontweight='bold')

    # Panel (a): Coherence fraction vs tau
    ax = axes[0, 0]
    ax.plot(TAU_VALUES, coh_scan, 'ko-', markersize=8, linewidth=2, label='Coherence fraction')
    ax.axhline(0.7, color='g', linestyle='--', alpha=0.7, label='PASS threshold (0.7)')
    ax.axhline(0.5, color='r', linestyle='--', alpha=0.7, label='FAIL threshold (0.5)')
    ax.axvspan(0.15, 0.25, alpha=0.1, color='blue', label='Wall region')
    ax.axvline(0.20, color='gray', linestyle=':', alpha=0.5, label='Fold center')
    ax.set_xlabel(r'$\tau_{\mathrm{target}}$', fontsize=12)
    ax.set_ylabel(r'Coherence fraction $C$', fontsize=12)
    ax.set_title('(a) Pairing coherence vs transport distance', fontsize=11)
    ax.legend(fontsize=9, loc='lower left')
    ax.set_ylim(-0.05, 1.05)
    ax.grid(True, alpha=0.3)

    # Panel (b): M_max transported vs local
    ax = axes[0, 1]
    ax.plot(TAU_VALUES, M_trans_scan, 'bs-', markersize=7, linewidth=2, label=r'$M_{\max}$ (transported)')
    ax.plot(TAU_VALUES, M_local_scan, 'r^-', markersize=7, linewidth=2, label=r'$M_{\max}$ (local)')
    ax.axhline(1.0, color='k', linestyle='--', alpha=0.5, label='BCS threshold')
    ax.axvspan(0.15, 0.25, alpha=0.1, color='blue')
    ax.set_xlabel(r'$\tau_{\mathrm{target}}$', fontsize=12)
    ax.set_ylabel(r'$M_{\max}$', fontsize=12)
    ax.set_title('(b) Thouless eigenvalue: transported vs local', fontsize=11)
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

    # Panel (c): SVD of overlap matrices
    ax = axes[1, 0]
    ax.plot(TAU_VALUES, sv_min_scan, 'go-', markersize=8, linewidth=2, label=r'min $\sigma$ (B2+B1)')
    ax.axhline(1.0, color='gray', linestyle=':', alpha=0.5)
    ax.axvspan(0.15, 0.25, alpha=0.1, color='blue')
    ax.set_xlabel(r'$\tau_{\mathrm{target}}$', fontsize=12)
    ax.set_ylabel(r'Minimum singular value', fontsize=12)
    ax.set_title('(c) Overlap matrix quality (SVD)', fontsize=11)
    ax.legend(fontsize=9)
    ax.set_ylim(0.0, 1.05)
    ax.grid(True, alpha=0.3)

    # Panel (d): |O|^2 heatmap for B2+B1 block (0.20->0.15)
    ax = axes[1, 1]
    O_show = np.abs(res_15['O_B2B1'])**2
    im = ax.imshow(O_show, cmap='viridis', vmin=0, vmax=1, aspect='equal')
    ax.set_xticks(range(5))
    ax.set_xticklabels(['B2a', 'B2b', 'B2c', 'B2d', 'B1'], fontsize=9)
    ax.set_yticks(range(5))
    ax.set_yticklabels(['B2a', 'B2b', 'B2c', 'B2d', 'B1'], fontsize=9)
    ax.set_xlabel(r'Target modes ($\tau=0.15$)', fontsize=11)
    ax.set_ylabel(r'Reference modes ($\tau=0.20$)', fontsize=11)
    ax.set_title(r'(d) $|O_{ij}|^2$ (B2+B1, $\tau$: 0.20$\to$0.15)', fontsize=11)
    plt.colorbar(im, ax=ax, shrink=0.8)
    # Add text annotations
    for i in range(5):
        for j in range(5):
            ax.text(j, i, f'{O_show[i, j]:.2f}', ha='center', va='center',
                    color='white' if O_show[i, j] < 0.5 else 'black', fontsize=8)

    plt.tight_layout()
    plt.savefig(OUTPUT_PNG, dpi=150, bbox_inches='tight')
    print(f"Plot saved to: {OUTPUT_PNG}")

    dt = time.time() - t0
    print(f"\nTotal runtime: {dt:.2f}s")


def print_results(res):
    """Print detailed results for a single transport computation."""
    print(f"\n  Label: {res['label']}")
    print(f"  tau_ref = {res['tau_ref']:.2f}, tau_target = {res['tau_target']:.2f}")
    print()

    # Thouless at reference
    print(f"  M_max at reference: {res['M_max_ref']:.6f}")
    print(f"  Thouless eigenvalues at ref: {np.sort(np.real(res['evals_M_ref']))[::-1]}")
    print()

    # Overlap quality
    print(f"  O_B2B1 singular values: {res['sv_B2B1']}")
    print(f"  O_B2 singular values:   {res['sv_B2']}")
    print(f"  O_full singular values:  min={np.min(res['sv_full']):.6f}, "
          f"max={np.max(res['sv_full']):.6f}")
    print()

    # Coherence
    print(f"  === COHERENCE FRACTION: {res['coherence_fraction']:.6f} ===")
    print()

    # Transported Thouless
    print(f"  M_max transported: {res['M_max_eff']:.6f}")
    print(f"  M_max local (at target): {res['M_max_local']:.6f}")
    print(f"  Ratio transported/local: {res['M_max_eff'] / res['M_max_local']:.6f}")
    print()

    # Gap function overlap
    print(f"  |<Delta_transported|Delta_local>|^2: {res['delta_overlap']:.6f}")


if __name__ == '__main__':
    main()
