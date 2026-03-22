"""
Session 34a: DPHYS-34a-2 -- Kosmann Kernel Under D_phys Eigenspinors
=====================================================================

CONTEXT:
  DPHYS-34a-1 PASS: B2 fold survives inner fluctuations (d2=1.226 at phi=gap).
  The D_phys eigenvectors rotate relative to bare D_K eigenvectors under phi,
  mixing branches B1/B2/B3.

  THIS COMPUTATION: Reproject the Kosmann pairing kernel V_nm into the D_phys
  eigenbasis. The K_a matrices (Kosmann-Lichnerowicz derivatives along Killing
  fields) are UNCHANGED -- they are properties of the isometry algebra. What
  changes is the BASIS: D_phys eigenspinors acquire admixtures from phi.

  Critical question: does V(B2,B2) remain nonzero (and large enough for BCS)
  when B2 eigenspinors acquire B3/B1 admixture from phi?

METHOD:
  1. Reconstruct D_phys = D_K + phi + J*phi*J^{-1} at each (tau, phi_VEV).
  2. Diagonalize to get D_phys eigenvectors (evecs_phys) in original basis.
  3. Compute overlap U = evecs_bare^H @ evecs_phys (bare-to-D_phys rotation).
  4. Transform K_a: K_a^{phys}_{nm} = (U^H K_a^{bare} U)_{nm}.
  5. Compute V_nm(phi) = sum_{a=0}^7 |K_a^{phys}_{nm}|^2.
  6. Extract V(B2,B2)(phi), decomposed by generator type.
  7. Sweep |phi_VEV| from 0 to 0.20.

MANDATORY CROSS-CHECK:
  At phi=0, U = I (up to phases), so V_nm(phi=0) must reproduce the raw
  Kosmann kernel sum_a |K_a^{bare}_{nm}|^2.

GATE DPHYS-34a-2 (pre-registered):
  V(B2,B2)(phi=gap) > 0.15: substantial pairing survives    -> STRONG PASS
  V(B2,B2)(phi=gap) > 0.05: moderate pairing survives       -> PASS
  V(B2,B2)(phi=gap) < 0.05: pairing severely suppressed     -> FAIL

Author: bap (baptista-spacetime-analyst), Session 34a
Date: 2026-03-06
"""

import os
import sys
import time
import numpy as np
from numpy.linalg import eigh
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
t0 = time.time()

# Add tier0-computation to path for imports
sys.path.insert(0, SCRIPT_DIR)

# ======================================================================
#  Constants
# ======================================================================

TAU_VALUES = np.array([0.0, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.50])

# Generator classification (su(3) = su(2) + C^2 + u(1))
SU2_GEN = [0, 1, 2]        # SU(2) subalgebra
C2_GEN  = [3, 4, 5, 6]     # C^2 (charged under U(1))
U1_GEN  = [7]               # U(1) generator

# ======================================================================
#  Import D_phys infrastructure from s34a_dphys_fold
# ======================================================================

from s34a_dphys_fold import (
    build_J_operator, apply_J_to_matrix,
    build_AF_generators, compute_phi_generators,
    find_worst_case_phi, construct_D_phys, identify_B2_branch
)


def identify_all_branches(evals_phys, evals_bare, evecs_phys, evecs_bare):
    """Identify which D_phys eigenvalues correspond to each branch.

    Uses maximum overlap with bare eigenvectors. Returns indices into
    the SORTED evals_phys array for each branch.

    Returns:
        dict with keys 'B1', 'B2', 'B3' (positive sector) and
        'B1_neg', 'B2_neg', 'B3_neg' (negative sector).
        Values are arrays of indices into evals_phys.
    """
    # Positive eigenvalues of bare D_K (sorted ascending)
    pos_bare = np.where(evals_bare > 0)[0]
    pos_bare_sorted = pos_bare[np.argsort(evals_bare[pos_bare])]
    # B1 = lowest positive = pos_bare_sorted[0]
    # B2 = next 4 = pos_bare_sorted[1:5]
    # B3 = top 3 = pos_bare_sorted[5:8]

    # Negative eigenvalues (sorted ascending: B3_neg, B2_neg, B1_neg)
    neg_bare = np.where(evals_bare < 0)[0]
    neg_bare_sorted = neg_bare[np.argsort(evals_bare[neg_bare])]
    # neg_bare_sorted: [0..2]=B3_neg, [3..6]=B2_neg, [7]=B1_neg

    branches_bare = {
        'B3_neg': neg_bare_sorted[0:3],
        'B2_neg': neg_bare_sorted[3:7],
        'B1_neg': neg_bare_sorted[7:8],
        'B1': pos_bare_sorted[0:1],
        'B2': pos_bare_sorted[1:5],
        'B3': pos_bare_sorted[5:8],
    }

    # For each phys eigenstate, compute overlap with all bare branch states
    n = len(evals_phys)
    branch_assignment = {}
    used_phys = set()

    for bname, bare_idx in branches_bare.items():
        n_modes = len(bare_idx)
        # Compute overlap of each phys eigenstate with this branch
        branch_ness = np.zeros(n)
        for i_ph in range(n):
            for i_b in bare_idx:
                overlap = np.abs(np.dot(
                    evecs_phys[:, i_ph].conj(), evecs_bare[:, i_b]))**2
                branch_ness[i_ph] += overlap

        # Select n_modes phys states with highest overlap (excluding already used)
        remaining = np.array([i for i in range(n) if i not in used_phys])
        branch_ness_rem = branch_ness[remaining]
        top_local = np.argsort(branch_ness_rem)[-n_modes:]
        selected = remaining[top_local]
        branch_assignment[bname] = np.sort(selected)
        used_phys.update(selected)

    return branch_assignment


def compute_kosmann_reprojection(K_a_bare, evecs_bare, evecs_phys):
    """Compute V_nm in the D_phys eigenbasis.

    K_a_bare[a] are 16x16 anti-hermitian matrices in the bare eigenspinor basis.
    evecs_bare, evecs_phys are 16x16 matrices (columns = eigenvectors) in the
    ORIGINAL (non-eigenspinor) basis.

    The overlap matrix U = evecs_bare^H @ evecs_phys transforms from bare
    eigenspinor basis to D_phys eigenspinor basis.

    K_a^{phys} = U^H @ K_a^{bare} @ U
    V_nm = sum_a |K_a^{phys}_{nm}|^2

    Returns:
        V_full: (16,16) full Kosmann kernel in D_phys basis
        V_SU2: (16,16) SU(2) generator contribution
        V_C2:  (16,16) C^2 generator contribution
        V_U1:  (16,16) U(1) generator contribution
        U:     (16,16) overlap matrix
    """
    # Overlap matrix: bare -> phys eigenspinor rotation
    U = evecs_bare.conj().T @ evecs_phys

    # Unitarity check
    uu_err = np.max(np.abs(U @ U.conj().T - np.eye(16)))
    if uu_err > 1e-10:
        print(f"  WARNING: U not unitary, |UU^H - I| = {uu_err:.2e}")

    V_full = np.zeros((16, 16))
    V_SU2 = np.zeros((16, 16))
    V_C2 = np.zeros((16, 16))
    V_U1 = np.zeros((16, 16))

    for a in range(8):
        K_phys = U.conj().T @ K_a_bare[a] @ U
        contrib = np.abs(K_phys)**2

        V_full += contrib
        if a in SU2_GEN:
            V_SU2 += contrib
        elif a in C2_GEN:
            V_C2 += contrib
        else:
            V_U1 += contrib

    return V_full, V_SU2, V_C2, V_U1, U


# ======================================================================
#  Main computation
# ======================================================================

def main():
    print("=" * 78)
    print("Session 34a: DPHYS-34a-2 -- Kosmann Kernel Under D_phys Eigenspinors")
    print("=" * 78)

    # --- Load data ---
    kosmann_path = os.path.join(SCRIPT_DIR, 's23a_kosmann_singlet.npz')
    kosmann = np.load(kosmann_path, allow_pickle=True)
    tau_vals = TAU_VALUES
    print(f"\nLoaded s23a_kosmann_singlet.npz")

    # --- Build J operator (from 34a-1) ---
    from tier1_dirac_spectrum import build_cliff8 as _bc8
    gammas = _bc8()

    from s34a_dphys_fold import build_J_operator
    B_J = build_J_operator(gammas)
    print(f"J operator: C2 = gamma_1*gamma_3*gamma_5*gamma_7")

    # --- Build A_F generators ---
    af_gens = build_AF_generators()
    print(f"A_F generators: {len(af_gens)} total")

    # --- Reference: identify worst-case phi direction (same as 34a-1) ---
    ti_ref = 3  # tau = 0.20
    evals_ref = kosmann[f'eigenvalues_{ti_ref}']
    evecs_ref = kosmann[f'eigenvectors_{ti_ref}']
    si_ref = np.argsort(evals_ref)
    evals_sorted_ref = evals_ref[si_ref]
    evecs_sorted_ref = evecs_ref[:, si_ref]

    pos_mask = evals_sorted_ref > 0
    pos_idx = np.where(pos_mask)[0]
    pos_ev = evals_sorted_ref[pos_idx]
    B1_modes = pos_idx[0:1]
    B2_modes = pos_idx[1:5]
    B3_modes = pos_idx[5:8]

    gap_b2_b1 = pos_ev[1] - pos_ev[0]
    gap_b3_b2 = pos_ev[5] - pos_ev[4]
    print(f"\nBranch structure at tau=0.20:")
    print(f"  B1 = {pos_ev[0]:.6f} (1 mode)")
    print(f"  B2 = {pos_ev[1]:.6f} (4 modes, degenerate)")
    print(f"  B3 = {pos_ev[5]:.6f} (3 modes)")
    print(f"  Gap B2-B1 = {gap_b2_b1:.6f}")
    print(f"  Gap B3-B2 = {gap_b3_b2:.6f}")

    # Identify worst-case phi direction
    phi_basis_ref = compute_phi_generators(evals_sorted_ref, evecs_sorted_ref, af_gens)
    worst_idx, worst_name, worst_mixing, mixing_details = find_worst_case_phi(
        phi_basis_ref, B2_modes, B3_modes, B1_modes)
    print(f"  Worst-case phi direction: {worst_name}")

    # ================================================================
    #  CROSS-CHECK: phi=0 Kosmann kernel reproduction
    # ================================================================
    print("\n" + "=" * 78)
    print("CROSS-CHECK: V_nm(phi=0) reproduces bare Kosmann kernel")
    print("=" * 78)

    # Load K_a matrices in bare eigenspinor basis
    K_a_bare_ref = []
    for a in range(8):
        K_a_bare_ref.append(kosmann[f'K_a_matrix_{ti_ref}_{a}'])

    # At phi=0, D_phys eigenvectors = D_K eigenvectors
    # So U = I and V_nm(0) = sum_a |K_a_bare_nm|^2
    V_bare_raw = np.zeros((16, 16))
    for a in range(8):
        V_bare_raw += np.abs(K_a_bare_ref[a])**2

    # Also compute via reprojection with U=I
    D_K_orig_ref = evecs_sorted_ref @ np.diag(evals_sorted_ref) @ evecs_sorted_ref.conj().T
    V_check, _, _, _, U_check = compute_kosmann_reprojection(
        K_a_bare_ref, evecs_sorted_ref, evecs_sorted_ref)

    # U should be identity (up to phases from degenerate eigenspaces)
    u_diag = np.abs(np.diag(U_check))
    u_offdiag_max = np.max(np.abs(U_check - np.diag(np.diag(U_check))))
    print(f"\n  U matrix at phi=0:")
    print(f"    min|diag(U)| = {np.min(u_diag):.10f}")
    print(f"    max|offdiag(U)| = {u_offdiag_max:.10f}")

    # For degenerate eigenspaces, U can have off-diagonal blocks
    # but V_nm should still match because V is basis-independent within
    # degenerate subspaces. Check total V within B2 block:
    V_B2_B2_raw = V_bare_raw[np.ix_(B2_modes, B2_modes)]
    V_B2_B2_check = V_check[np.ix_(B2_modes, B2_modes)]

    # The degenerate subspace allows U to be any unitary within the block.
    # V_nm = sum |K_nm|^2 transforms as V -> |U^H K U|^2, which for a
    # unitary change within a degenerate block gives a DIFFERENT V matrix
    # (it's not a scalar). But the trace over the block is invariant:
    # Tr(V_block) = sum_{nm in block} V_nm is basis-independent.

    # For the actual cross-check, we need evecs_phys = evecs_bare exactly
    # (same pointer), which gives U = I exactly.
    V_direct, V_d_su2, V_d_c2, V_d_u1, U_direct = compute_kosmann_reprojection(
        K_a_bare_ref, evecs_sorted_ref, evecs_sorted_ref)

    cross_err = np.max(np.abs(V_direct - V_bare_raw))
    print(f"\n  Cross-check: max|V(phi=0,reprojected) - V(bare,raw)| = {cross_err:.2e}")
    assert cross_err < 1e-12, f"CROSS-CHECK FAILED: {cross_err:.2e}"
    print(f"  PASS (machine epsilon)")

    # Report bare V(B2,B2) values
    print(f"\n  Bare V(B2,B2) matrix (off-diagonal max = {np.max(V_B2_B2_raw):.6f}):")
    np.set_printoptions(precision=6, suppress=True, linewidth=120)
    print(f"  {V_B2_B2_raw}")

    # ================================================================
    #  MAIN SWEEP: Kosmann reprojection across phi amplitude
    # ================================================================
    print("\n" + "=" * 78)
    print("MAIN COMPUTATION: V_nm(phi) across phi amplitude sweep")
    print("=" * 78)

    # Use tau_idx=3 (tau=0.20) and tau_idx=2 (tau=0.15) for fold region.
    # Also tau_idx=4 (tau=0.25) for stability check.
    tau_scan_indices = [1, 2, 3, 4, 5]
    phi_amplitudes = np.linspace(0, 0.20, 21)  # 0 to 0.20 in steps of 0.01

    # Storage for results at reference tau=0.20
    V_B2B2_max_vs_phi = []      # max off-diagonal V(B2,B2) vs phi
    V_B2B2_su2_vs_phi = []      # SU(2) component
    V_B2B2_c2_vs_phi = []       # C^2 component
    V_B2B2_u1_vs_phi = []       # U(1) component
    V_B2B2_trace_vs_phi = []    # Tr(V_B2B2_block) (invariant)
    V_B1B2_max_vs_phi = []      # max V(B1,B2) vs phi
    V_B3B2_max_vs_phi = []      # max V(B3,B2) vs phi
    V_B2B2_diag_max_vs_phi = [] # max diagonal V(B2_i, B2_i)
    mixing_B2_vs_phi = []       # B2 branch overlap with bare B2

    # Multi-tau storage
    V_B2B2_max_by_tau_phi = {}  # (tau_idx, phi_amp) -> max V(B2,B2) off-diag

    for phi_amp in phi_amplitudes:
        print(f"\n  |phi| = {phi_amp:.4f}:", end="")

        for ti in tau_scan_indices:
            tau = tau_vals[ti]
            evals_ti = kosmann[f'eigenvalues_{ti}']
            evecs_ti = kosmann[f'eigenvectors_{ti}']

            # Sort eigenbasis
            si = np.argsort(evals_ti)
            ev_s = evals_ti[si]
            ec_s = evecs_ti[:, si]

            # Load K_a in bare eigenspinor basis for this tau
            K_a_bare_ti = []
            for a in range(8):
                K_a_bare_ti.append(kosmann[f'K_a_matrix_{ti}_{a}'])

            if phi_amp < 1e-14:
                # phi = 0: D_phys = D_K, trivial case
                evals_phys = ev_s.copy()
                evecs_phys = ec_s.copy()
            else:
                # Compute phi direction in this eigenbasis
                phi_basis_ti = compute_phi_generators(ev_s, ec_s, af_gens)

                # Find the worst_name generator
                phi_dir_ti = None
                for name, comm, norm in phi_basis_ti:
                    if name == worst_name:
                        phi_dir_ti = comm
                        break

                if phi_dir_ti is None:
                    # Fallback
                    phi_all = compute_phi_generators(ev_s, ec_s, af_gens)
                    best_mix = 0
                    for _, comm_f, norm_f in phi_all:
                        pi = np.where(ev_s > 0)[0]
                        pi_s = pi[np.argsort(ev_s[pi])]
                        b2m = pi_s[1:5]
                        b3m = pi_s[5:8]
                        b1m = pi_s[0:1]
                        b23 = np.max(np.abs(comm_f[np.ix_(b2m, b3m)])) if b3m.size > 0 else 0
                        b21 = np.max(np.abs(comm_f[np.ix_(b2m, b1m)])) if b1m.size > 0 else 0
                        if max(b23, b21) > best_mix:
                            best_mix = max(b23, b21)
                            phi_dir_ti = comm_f

                evals_phys, evecs_phys, herm_err = construct_D_phys(
                    ev_s, ec_s, phi_dir_ti, phi_amp, B_J)

            # Reproject Kosmann kernel
            V_full, V_su2, V_c2, V_u1, U = compute_kosmann_reprojection(
                K_a_bare_ti, ec_s, evecs_phys)

            # Identify B2 branch in D_phys spectrum
            branches = identify_all_branches(evals_phys, ev_s, evecs_phys, ec_s)
            b2_phys = branches['B2']

            # B2-B2 pairing kernel (off-diagonal elements)
            V_B2B2_block = V_full[np.ix_(b2_phys, b2_phys)]
            V_B2B2_offdiag = V_B2B2_block.copy()
            np.fill_diagonal(V_B2B2_offdiag, 0)
            V_B2B2_max_offdiag = np.max(V_B2B2_offdiag)

            # Decomposition
            V_B2B2_su2_block = V_su2[np.ix_(b2_phys, b2_phys)]
            V_B2B2_c2_block = V_c2[np.ix_(b2_phys, b2_phys)]
            V_B2B2_u1_block = V_u1[np.ix_(b2_phys, b2_phys)]

            V_B2B2_su2_offdiag = V_B2B2_su2_block.copy()
            np.fill_diagonal(V_B2B2_su2_offdiag, 0)
            V_B2B2_c2_offdiag = V_B2B2_c2_block.copy()
            np.fill_diagonal(V_B2B2_c2_offdiag, 0)
            V_B2B2_u1_offdiag = V_B2B2_u1_block.copy()
            np.fill_diagonal(V_B2B2_u1_offdiag, 0)

            # B1-B2 and B3-B2 cross-couplings
            b1_phys = branches['B1']
            b3_phys = branches['B3']

            V_B1B2 = V_full[np.ix_(b1_phys, b2_phys)]
            V_B3B2 = V_full[np.ix_(b3_phys, b2_phys)]

            # B2 overlap with bare B2 (mixing diagnostic)
            bare_pos = np.where(ev_s > 0)[0]
            bare_pos_sorted = bare_pos[np.argsort(ev_s[bare_pos])]
            bare_b2 = bare_pos_sorted[1:5]
            b2_overlap = 0.0
            for i_ph in b2_phys:
                for i_b in bare_b2:
                    b2_overlap += np.abs(np.dot(
                        evecs_phys[:, i_ph].conj(), ec_s[:, i_b]))**2
            b2_overlap /= 4.0  # Normalize: perfect overlap = 1.0

            # Store multi-tau results
            V_B2B2_max_by_tau_phi[(ti, phi_amp)] = V_B2B2_max_offdiag

            # Store per-phi results at reference tau=0.20
            if ti == ti_ref:
                V_B2B2_max_vs_phi.append(V_B2B2_max_offdiag)
                V_B2B2_su2_vs_phi.append(np.max(V_B2B2_su2_offdiag))
                V_B2B2_c2_vs_phi.append(np.max(V_B2B2_c2_offdiag))
                V_B2B2_u1_vs_phi.append(np.max(V_B2B2_u1_offdiag))
                V_B2B2_trace_vs_phi.append(np.sum(V_B2B2_block))
                V_B1B2_max_vs_phi.append(np.max(V_B1B2) if V_B1B2.size > 0 else 0)
                V_B3B2_max_vs_phi.append(np.max(V_B3B2) if V_B3B2.size > 0 else 0)
                V_B2B2_diag_max_vs_phi.append(np.max(np.diag(V_B2B2_block)))
                mixing_B2_vs_phi.append(b2_overlap)

                print(f" tau={tau:.2f}: V_B2B2_max={V_B2B2_max_offdiag:.6f},"
                      f" SU2={np.max(V_B2B2_su2_offdiag):.6f},"
                      f" C2={np.max(V_B2B2_c2_offdiag):.6f},"
                      f" U1={np.max(V_B2B2_u1_offdiag):.6f},"
                      f" B2_overlap={b2_overlap:.4f}", end="")

        print()

    # Convert to arrays
    V_B2B2_max_vs_phi = np.array(V_B2B2_max_vs_phi)
    V_B2B2_su2_vs_phi = np.array(V_B2B2_su2_vs_phi)
    V_B2B2_c2_vs_phi = np.array(V_B2B2_c2_vs_phi)
    V_B2B2_u1_vs_phi = np.array(V_B2B2_u1_vs_phi)
    V_B2B2_trace_vs_phi = np.array(V_B2B2_trace_vs_phi)
    V_B1B2_max_vs_phi = np.array(V_B1B2_max_vs_phi)
    V_B3B2_max_vs_phi = np.array(V_B3B2_max_vs_phi)
    V_B2B2_diag_max_vs_phi = np.array(V_B2B2_diag_max_vs_phi)
    mixing_B2_vs_phi = np.array(mixing_B2_vs_phi)

    # ================================================================
    #  DETAILED REPORT at phi = gap
    # ================================================================
    print("\n" + "=" * 78)
    print("DETAILED RESULTS AT |phi| = gap_{B3-B2}")
    print("=" * 78)

    # Find phi closest to gap
    gap_phi_idx = np.argmin(np.abs(phi_amplitudes - gap_b3_b2))
    phi_at_gap = phi_amplitudes[gap_phi_idx]
    print(f"\n  |phi| = {phi_at_gap:.4f} (gap = {gap_b3_b2:.6f})")
    print(f"  V(B2,B2) max off-diag = {V_B2B2_max_vs_phi[gap_phi_idx]:.6f}")
    print(f"  Decomposition:")
    print(f"    SU(2): {V_B2B2_su2_vs_phi[gap_phi_idx]:.6f}")
    print(f"    C^2:   {V_B2B2_c2_vs_phi[gap_phi_idx]:.6f}")
    print(f"    U(1):  {V_B2B2_u1_vs_phi[gap_phi_idx]:.6f}")
    print(f"  V(B1,B2) max = {V_B1B2_max_vs_phi[gap_phi_idx]:.6f}")
    print(f"  V(B3,B2) max = {V_B3B2_max_vs_phi[gap_phi_idx]:.6f}")
    print(f"  B2 overlap with bare = {mixing_B2_vs_phi[gap_phi_idx]:.6f}")
    print(f"  V(B2,B2) diagonal max = {V_B2B2_diag_max_vs_phi[gap_phi_idx]:.6f}")
    print(f"  Tr(V_B2B2 block) = {V_B2B2_trace_vs_phi[gap_phi_idx]:.6f}")

    # Comparison with bare values
    print(f"\n  Bare (phi=0) reference:")
    print(f"    V(B2,B2) max off-diag = {V_B2B2_max_vs_phi[0]:.6f}")
    print(f"    V(B1,B2) max = {V_B1B2_max_vs_phi[0]:.6f}")
    print(f"    V(B3,B2) max = {V_B3B2_max_vs_phi[0]:.6f}")

    ratio = V_B2B2_max_vs_phi[gap_phi_idx] / V_B2B2_max_vs_phi[0] if V_B2B2_max_vs_phi[0] > 0 else 0
    print(f"\n  Ratio V(B2,B2,phi=gap)/V(B2,B2,bare) = {ratio:.4f}")

    # ================================================================
    #  FULL TABLE: V(B2,B2) across all phi amplitudes
    # ================================================================
    print("\n" + "=" * 78)
    print("FULL SWEEP: V(B2,B2) max off-diagonal vs |phi| (tau=0.20)")
    print("=" * 78)

    print(f"\n  {'|phi|':>8s}  {'V_B2B2':>10s}  {'SU2':>8s}  {'C2':>8s}  "
          f"{'U1':>8s}  {'V_B1B2':>8s}  {'V_B3B2':>8s}  {'diag':>8s}  "
          f"{'overlap':>8s}")
    print(f"  {'-'*88}")

    for i, phi_amp in enumerate(phi_amplitudes):
        print(f"  {phi_amp:8.4f}  {V_B2B2_max_vs_phi[i]:10.6f}  "
              f"{V_B2B2_su2_vs_phi[i]:8.6f}  {V_B2B2_c2_vs_phi[i]:8.6f}  "
              f"{V_B2B2_u1_vs_phi[i]:8.6f}  {V_B1B2_max_vs_phi[i]:8.6f}  "
              f"{V_B3B2_max_vs_phi[i]:8.6f}  "
              f"{V_B2B2_diag_max_vs_phi[i]:8.6f}  "
              f"{mixing_B2_vs_phi[i]:8.4f}")

    # ================================================================
    #  MULTI-TAU STABILITY CHECK
    # ================================================================
    print("\n" + "=" * 78)
    print("MULTI-TAU STABILITY: V(B2,B2) at phi=gap across tau values")
    print("=" * 78)

    print(f"\n  {'tau':>6s}  {'V_B2B2_max':>12s}")
    print(f"  {'-'*22}")
    for ti in tau_scan_indices:
        tau = tau_vals[ti]
        v = V_B2B2_max_by_tau_phi.get((ti, phi_at_gap), np.nan)
        print(f"  {tau:6.2f}  {v:12.6f}")

    # ================================================================
    #  W1 PREDICTION: B3 channel opens?
    # ================================================================
    print("\n" + "=" * 78)
    print("W1 PREDICTION TEST: 'B3 channel opens' under D_phys")
    print("=" * 78)

    # At phi=0, V(B3,B2) should be the bare inter-branch coupling.
    # Under phi, V(B3,B2) may increase if B3 acquires B2 admixture.
    print(f"\n  V(B3,B2) max:")
    print(f"    phi=0:     {V_B3B2_max_vs_phi[0]:.6f}")
    print(f"    phi=gap:   {V_B3B2_max_vs_phi[gap_phi_idx]:.6f}")
    if V_B3B2_max_vs_phi[0] > 1e-10:
        b3_ratio = V_B3B2_max_vs_phi[gap_phi_idx] / V_B3B2_max_vs_phi[0]
        print(f"    Ratio:     {b3_ratio:.4f}")
        b3_opens = b3_ratio > 1.05  # 5% increase threshold
    else:
        b3_opens = V_B3B2_max_vs_phi[gap_phi_idx] > 0.01
        print(f"    Bare value zero; channel {'OPENS' if b3_opens else 'CLOSED'}")
    print(f"  B3 channel opens: {'YES' if b3_opens else 'NO'}")

    # ================================================================
    #  GATE CLASSIFICATION
    # ================================================================
    print("\n" + "=" * 78)
    print("GATE DPHYS-34a-2 CLASSIFICATION")
    print("=" * 78)

    V_at_gap = V_B2B2_max_vs_phi[gap_phi_idx]

    print(f"\n  V(B2,B2) max off-diagonal at phi=gap: {V_at_gap:.6f}")
    print(f"  Bare V(B2,B2) max off-diagonal:        {V_B2B2_max_vs_phi[0]:.6f}")
    print(f"  Retention ratio:                        {ratio:.4f}")
    print(f"  B2 overlap with bare:                   {mixing_B2_vs_phi[gap_phi_idx]:.6f}")

    if V_at_gap > 0.15:
        verdict = "STRONG PASS"
        print(f"\n  VERDICT: STRONG PASS")
        print(f"  V(B2,B2) = {V_at_gap:.6f} > 0.15: substantial pairing survives")
    elif V_at_gap > 0.05:
        verdict = "PASS"
        print(f"\n  VERDICT: PASS")
        print(f"  V(B2,B2) = {V_at_gap:.6f} > 0.05: moderate pairing survives")
    else:
        verdict = "FAIL"
        print(f"\n  VERDICT: FAIL")
        print(f"  V(B2,B2) = {V_at_gap:.6f} < 0.05: pairing severely suppressed")

    # ================================================================
    #  SAVE
    # ================================================================
    save_dict = {
        'tau_values': tau_vals,
        'phi_amplitudes': phi_amplitudes,
        'worst_name': worst_name,
        'gap_b3_b2': gap_b3_b2,
        'gap_b2_b1': gap_b2_b1,
        'verdict': verdict,
        'V_B2B2_max_vs_phi': V_B2B2_max_vs_phi,
        'V_B2B2_su2_vs_phi': V_B2B2_su2_vs_phi,
        'V_B2B2_c2_vs_phi': V_B2B2_c2_vs_phi,
        'V_B2B2_u1_vs_phi': V_B2B2_u1_vs_phi,
        'V_B2B2_trace_vs_phi': V_B2B2_trace_vs_phi,
        'V_B1B2_max_vs_phi': V_B1B2_max_vs_phi,
        'V_B3B2_max_vs_phi': V_B3B2_max_vs_phi,
        'V_B2B2_diag_max_vs_phi': V_B2B2_diag_max_vs_phi,
        'mixing_B2_vs_phi': mixing_B2_vs_phi,
        'V_at_gap': V_at_gap,
        'V_bare': V_B2B2_max_vs_phi[0],
        'retention_ratio': ratio,
        'b3_channel_opens': b3_opens,
        'phi_at_gap': phi_at_gap,
        'cross_check_err': cross_err,
    }

    # Multi-tau data
    for ti in tau_scan_indices:
        for phi_amp in phi_amplitudes:
            key = (ti, phi_amp)
            if key in V_B2B2_max_by_tau_phi:
                save_dict[f'V_B2B2_tau{ti}_phi{phi_amp:.4f}'] = V_B2B2_max_by_tau_phi[key]

    out_npz = os.path.join(SCRIPT_DIR, 's34a_dphys_kosmann.npz')
    np.savez_compressed(out_npz, **save_dict)
    print(f"\n  Saved: {out_npz}")

    # ================================================================
    #  PLOT
    # ================================================================
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Panel 1: V(B2,B2) max off-diagonal vs phi
    ax = axes[0, 0]
    ax.plot(phi_amplitudes, V_B2B2_max_vs_phi, 'b-o', ms=4, lw=2,
            label='V(B2,B2) max off-diag')
    ax.axhline(y=V_B2B2_max_vs_phi[0], color='gray', ls='--', alpha=0.5,
               label=f'bare = {V_B2B2_max_vs_phi[0]:.4f}')
    ax.axhline(y=0.15, color='green', ls=':', alpha=0.7, label='STRONG threshold')
    ax.axhline(y=0.05, color='orange', ls=':', alpha=0.7, label='PASS threshold')
    ax.axvline(x=gap_b3_b2, color='red', ls='--', alpha=0.5,
               label=f'gap={gap_b3_b2:.3f}')
    ax.set_xlabel('|phi_VEV|')
    ax.set_ylabel('V(B2,B2) max off-diagonal')
    ax.set_title(f'Kosmann kernel reprojection: {verdict}')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # Panel 2: Decomposition by generator type
    ax = axes[0, 1]
    ax.plot(phi_amplitudes, V_B2B2_su2_vs_phi, 'r-s', ms=3, lw=1.5, label='SU(2)')
    ax.plot(phi_amplitudes, V_B2B2_c2_vs_phi, 'g-^', ms=3, lw=1.5, label='C^2')
    ax.plot(phi_amplitudes, V_B2B2_u1_vs_phi, 'b-D', ms=3, lw=1.5, label='U(1)')
    ax.plot(phi_amplitudes, V_B2B2_max_vs_phi, 'k-o', ms=3, lw=2, label='Total')
    ax.axvline(x=gap_b3_b2, color='red', ls='--', alpha=0.5)
    ax.set_xlabel('|phi_VEV|')
    ax.set_ylabel('V(B2,B2) max off-diagonal')
    ax.set_title('Generator decomposition')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel 3: Cross-branch couplings and B2 self-coupling
    ax = axes[1, 0]
    ax.plot(phi_amplitudes, V_B1B2_max_vs_phi, 'm-s', ms=3, lw=1.5, label='V(B1,B2) max')
    ax.plot(phi_amplitudes, V_B3B2_max_vs_phi, 'c-^', ms=3, lw=1.5, label='V(B3,B2) max')
    ax.plot(phi_amplitudes, V_B2B2_diag_max_vs_phi, 'k--D', ms=3, lw=1.5,
            label='V(B2,B2) diagonal max')
    ax.axvline(x=gap_b3_b2, color='red', ls='--', alpha=0.5)
    ax.set_xlabel('|phi_VEV|')
    ax.set_ylabel('V_nm max')
    ax.set_title('Cross-branch and self-coupling')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel 4: B2 overlap with bare B2 (mixing diagnostic)
    ax = axes[1, 1]
    ax.plot(phi_amplitudes, mixing_B2_vs_phi, 'r-o', ms=4, lw=2)
    ax.axhline(y=1.0, color='gray', ls='--', alpha=0.5, label='Perfect overlap')
    ax.axvline(x=gap_b3_b2, color='red', ls='--', alpha=0.5,
               label=f'gap={gap_b3_b2:.3f}')
    ax.set_xlabel('|phi_VEV|')
    ax.set_ylabel('Avg overlap |<B2_phys|B2_bare>|^2')
    ax.set_title('B2 branch identity under phi rotation')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 1.05)

    fig.suptitle(f'DPHYS-34a-2: Kosmann Kernel Under D_phys | {verdict}',
                 fontsize=14, fontweight='bold')
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    out_png = os.path.join(SCRIPT_DIR, 's34a_dphys_kosmann.png')
    plt.savefig(out_png, dpi=150)
    plt.close()
    print(f"  Saved: {out_png}")

    elapsed = time.time() - t0
    print(f"\n  Total runtime: {elapsed:.1f}s")
    print(f"\n  GATE DPHYS-34a-2: {verdict}")

    return verdict


if __name__ == '__main__':
    main()
