"""
Session 34a: Trap 1 Re-evaluation With Full 8-Generator Kosmann Kernel
======================================================================

CONTEXT:
  Session 23a established "Trap 1": V(gap,gap) = 0 exactly at the gap edge.
  The gap edge is the eigenvalue closest to zero in the singlet sector --
  this is the B1 mode (1-fold, lowest positive eigenvalue).

  Session 33b retracted K-1e: V(B2,B2) = 0 was a C^2-generator artifact.
  With the full 8-generator kernel, V(B2,B2) = 0.287 (U(1) + SU(2) channels).

  THIS COMPUTATION: Does V(gap,gap) remain zero with the full kernel?
  "Gap" here means the B1 mode (index 7 in the A_antisym 8x8 basis),
  NOT the B2 modes. V(gap,gap) is the DIAGONAL self-coupling of the
  gap-edge mode through the Kosmann pairing kernel.

  The distinction matters because B1 is a SINGLET under U(2), while B2
  is a QUARTET. The representation theory that kills V(B2,B2) under C^2
  (U(1) charge conservation) may or may not kill V(B1,B1) under the full
  algebra.

DATA:
  Source: s23a_kosmann_singlet.npz
  Keys used:
    - A_antisym_{tau_idx}_{a}: 8x8 Kosmann matrices in branch basis (a=0..7)
    - eigenvalues_{tau_idx}: 16 eigenvalues sorted ascending
    - gap_edge_indices_{tau_idx}: [idx_pos, idx_neg] of gap-edge modes
    - K_a_matrix_{tau_idx}_{a}: 16x16 Kosmann matrices in eigenspinor basis
    - eigenvectors_{tau_idx}: 16x16 eigenvector matrix

GATE TRAP1-34a (pre-registered):
  CONFIRMED: V(gap,gap) = 0 (to ~1e-14) with full kernel at all tau -> Trap 1 remains.
  BROKEN:    V(gap,gap) > 0.01 with full kernel -> Trap 1 RETRACTED.
             Gap edge becomes additional pairing channel (STRENGTHENS BCS).

Author: connes (connes-ncg-theorist), Session 34a
Date: 2026-03-06
"""

import os
import time
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

TAU_VALUES = np.array([0.0, 0.10, 0.15, 0.20, 0.25, 0.30, 0.35, 0.40, 0.50])

# Branch indices in the A_antisym 8x8 basis (positive eigenvalue sector)
# Ordering: B3 = {0,1,2}, B2 = {3,4,5,6}, B1 = {7}
B3_IDX = np.array([0, 1, 2])
B2_IDX = np.array([3, 4, 5, 6])
B1_IDX = np.array([7])

# Generator classification (su(3) = su(2) + u(1) + C^2)
SU2_GEN = [0, 1, 2]   # SU(2) subalgebra
C2_GEN  = [3, 4, 5, 6]  # C^2 (charged under U(1))
U1_GEN  = [7]           # U(1) generator


def load_data():
    """Load Kosmann singlet data."""
    path = os.path.join(SCRIPT_DIR, 's23a_kosmann_singlet.npz')
    return np.load(path, allow_pickle=True)


def compute_V_gap_gap(kosmann, tau_idx, gen_list=None):
    """Compute V(gap,gap) = sum_{a in gen_list} |A_a[7,7]|^2.

    In the A_antisym basis, B1 = index 7. V(gap,gap) is the
    diagonal element A_antisym[7,7] summed over generators.

    Parameters:
        kosmann: loaded npz data
        tau_idx: index into TAU_VALUES (0..8)
        gen_list: list of generator indices (default: all 8)

    Returns:
        V_gap_gap: float, the self-coupling
        V_per_gen: dict mapping generator index -> |A_a[7,7]|^2
    """
    if gen_list is None:
        gen_list = list(range(8))

    V_gap_gap = 0.0
    V_per_gen = {}
    for a in gen_list:
        A = kosmann[f'A_antisym_{tau_idx}_{a}']
        val = abs(A[7, 7]) ** 2
        V_per_gen[a] = val
        V_gap_gap += val

    return V_gap_gap, V_per_gen


def compute_V_gap_offdiag(kosmann, tau_idx):
    """Compute V(gap, n) for all n != gap (off-diagonal from B1).

    V(B1, n) = sum_{a=0..7} |A_a[7, n]|^2 for n = 0..6 (B3 and B2 modes).

    Returns:
        V_gap_n: array of shape (7,), one entry per non-gap mode
        V_gap_n_decomposed: dict with 'SU2', 'C2', 'U1' contributions
    """
    V_gap_n = np.zeros(7)
    V_SU2 = np.zeros(7)
    V_C2  = np.zeros(7)
    V_U1  = np.zeros(7)

    for a in range(8):
        A = kosmann[f'A_antisym_{tau_idx}_{a}']
        for n in range(7):
            val = abs(A[7, n]) ** 2
            V_gap_n[n] += val
            if a in SU2_GEN:
                V_SU2[n] += val
            elif a in C2_GEN:
                V_C2[n] += val
            else:
                V_U1[n] += val

    return V_gap_n, {'SU2': V_SU2, 'C2': V_C2, 'U1': V_U1}


def compute_V_gap_gap_16x16(kosmann, tau_idx):
    """Cross-check: compute V(gap,gap) directly from 16x16 K_a matrices.

    The gap-edge mode is identified by gap_edge_indices. We extract the
    diagonal element in the eigenspinor basis directly.

    This serves as a CONSISTENCY CHECK against the A_antisym computation.
    """
    gap_indices = kosmann[f'gap_edge_indices_{tau_idx}']
    # gap_indices[0] = positive gap-edge index, gap_indices[1] = negative
    idx_pos = int(gap_indices[0])
    idx_neg = int(gap_indices[1])

    V_pos_pos = 0.0
    V_neg_neg = 0.0
    V_pos_neg = 0.0

    for a in range(8):
        K = kosmann[f'K_a_matrix_{tau_idx}_{a}']
        V_pos_pos += abs(K[idx_pos, idx_pos]) ** 2
        V_neg_neg += abs(K[idx_neg, idx_neg]) ** 2
        V_pos_neg += abs(K[idx_pos, idx_neg]) ** 2

    return V_pos_pos, V_neg_neg, V_pos_neg, idx_pos, idx_neg


def compute_full_V_matrix(kosmann, tau_idx):
    """Build the full 8x8 V_nm = sum_{a} |A_a[n,m]|^2 matrix."""
    V = np.zeros((8, 8))
    for a in range(8):
        A = kosmann[f'A_antisym_{tau_idx}_{a}']
        V += np.abs(A) ** 2
    return V


def run():
    print("=" * 80)
    print("Session 34a: Trap 1 Re-evaluation With Full 8-Generator Kosmann Kernel")
    print("Gate TRAP1-34a: Does V(gap,gap) = 0 survive with the full kernel?")
    print("=" * 80)
    print()

    t0 = time.time()
    kosmann = load_data()
    print(f"Data loaded in {time.time()-t0:.2f}s")
    print()

    # ==================================================================
    # STEP 1: V(gap,gap) in the A_antisym basis across all tau
    # ==================================================================
    print("=" * 70)
    print("STEP 1: V(gap,gap) = V(B1,B1) in A_antisym Basis, Full Kernel")
    print("=" * 70)
    print()
    print("B1 = mode index 7 in the A_antisym 8x8 basis (positive sector).")
    print("This is the gap-edge mode: closest positive eigenvalue to zero.")
    print()

    print(f"{'tau':>6s} {'V(gap,gap)':>14s} {'V_SU2':>12s} {'V_C2':>12s} "
          f"{'V_U1':>12s} {'lambda_B1':>12s}")
    print("-" * 76)

    results_by_tau = []
    for ti in range(len(TAU_VALUES)):
        V_gg, V_per = compute_V_gap_gap(kosmann, ti)
        V_su2 = sum(V_per.get(a, 0.0) for a in SU2_GEN)
        V_c2  = sum(V_per.get(a, 0.0) for a in C2_GEN)
        V_u1  = sum(V_per.get(a, 0.0) for a in U1_GEN)

        evals = kosmann[f'eigenvalues_{ti}']
        pos_evals = np.sort(evals[evals > 0])
        lambda_B1 = pos_evals[0]  # lowest positive = B1 = gap edge

        print(f"{TAU_VALUES[ti]:6.2f} {V_gg:14.10f} {V_su2:12.10f} {V_c2:12.10f} "
              f"{V_u1:12.10f} {lambda_B1:12.6f}")

        results_by_tau.append({
            'tau': TAU_VALUES[ti], 'V_gg': V_gg,
            'V_su2': V_su2, 'V_c2': V_c2, 'V_u1': V_u1,
            'lambda_B1': lambda_B1, 'V_per_gen': V_per,
        })

    print()

    # ==================================================================
    # STEP 2: Cross-check via 16x16 K_a matrices
    # ==================================================================
    print("=" * 70)
    print("STEP 2: Cross-Check via 16x16 K_a Matrices (Eigenspinor Basis)")
    print("=" * 70)
    print()
    print("Direct computation from K_a_matrix (16x16) at gap-edge indices.")
    print("Consistency check: V_16x16(pos,pos) should match V_8x8(B1,B1).")
    print()

    print(f"{'tau':>6s} {'V(+,+)':>14s} {'V(-,-)':>14s} {'V(+,-)':>14s} "
          f"{'idx_pos':>8s} {'idx_neg':>8s}")
    print("-" * 70)

    for ti in range(len(TAU_VALUES)):
        V_pp, V_nn, V_pn, ip, ine = compute_V_gap_gap_16x16(kosmann, ti)
        print(f"{TAU_VALUES[ti]:6.2f} {V_pp:14.10f} {V_nn:14.10f} {V_pn:14.10f} "
              f"{ip:>8d} {ine:>8d}")

    print()

    # ==================================================================
    # STEP 3: V(gap, other) off-diagonal elements
    # ==================================================================
    print("=" * 70)
    print("STEP 3: V(gap, n) Off-Diagonal Elements (B1 to B3/B2)")
    print("=" * 70)
    print()
    print("These are the off-diagonal couplings from the gap edge to other modes.")
    print("Ordering: B3(0,1,2), B2(3,4,5,6).")
    print()

    for ti in [0, 3, 5, 8]:  # tau = 0.0, 0.20, 0.30, 0.50
        V_gn, V_decomp = compute_V_gap_offdiag(kosmann, ti)
        print(f"tau = {TAU_VALUES[ti]:.2f}:")
        print(f"  V(B1,B3):  {V_gn[0]:.6f}  {V_gn[1]:.6f}  {V_gn[2]:.6f}")
        print(f"  V(B1,B2):  {V_gn[3]:.6f}  {V_gn[4]:.6f}  {V_gn[5]:.6f}  {V_gn[6]:.6f}")
        print(f"  By type -- SU2: B3={V_decomp['SU2'][:3].sum():.6f}, "
              f"B2={V_decomp['SU2'][3:].sum():.6f}")
        print(f"             C2:  B3={V_decomp['C2'][:3].sum():.6f}, "
              f"B2={V_decomp['C2'][3:].sum():.6f}")
        print(f"             U1:  B3={V_decomp['U1'][:3].sum():.6f}, "
              f"B2={V_decomp['U1'][3:].sum():.6f}")
        print()

    # ==================================================================
    # STEP 4: Full 8x8 V matrix at tau = 0.20 (reference)
    # ==================================================================
    print("=" * 70)
    print("STEP 4: Full 8x8 V Matrix at tau = 0.20")
    print("=" * 70)
    print()

    V_full_8x8 = compute_full_V_matrix(kosmann, 3)
    np.set_printoptions(precision=6, suppress=True, linewidth=120)
    print("V_nm = sum_{a=0..7} |A_a[n,m]|^2:")
    print(V_full_8x8)
    print()
    print(f"V(B1,B1) = V[7,7] = {V_full_8x8[7,7]:.12f}")
    print(f"V(B2,B2) max off-diag = {np.max(V_full_8x8[np.ix_(B2_IDX,B2_IDX)]):.6f}")
    print(f"V(B1,B2) = {V_full_8x8[7, B2_IDX]}")
    print(f"V(B1,B3) = {V_full_8x8[7, B3_IDX]}")
    print()

    # ==================================================================
    # STEP 5: Individual generator A_a[7,7] values (diagnostic)
    # ==================================================================
    print("=" * 70)
    print("STEP 5: Individual A_a[7,7] Values (Diagnostic)")
    print("=" * 70)
    print()
    print("The raw matrix element A_a[7,7] = <B1|K_a|B1> for each generator.")
    print("V(gap,gap) = sum |A_a[7,7]|^2.")
    print()

    for ti in [0, 3, 8]:  # tau = 0, 0.20, 0.50
        print(f"tau = {TAU_VALUES[ti]:.2f}:")
        for a in range(8):
            A = kosmann[f'A_antisym_{ti}_{a}']
            val = A[7, 7]
            gen_type = "SU(2)" if a in SU2_GEN else ("C^2" if a in C2_GEN else "U(1)")
            print(f"  a={a} ({gen_type:>5s}): A[7,7] = {val:+.10f}, |A[7,7]|^2 = {abs(val)**2:.12f}")
        print()

    # ==================================================================
    # STEP 6: Representation-theoretic analysis
    # ==================================================================
    print("=" * 70)
    print("STEP 6: Representation-Theoretic Analysis")
    print("=" * 70)
    print()

    # B1 is a U(2) singlet. Under SU(2) x U(1):
    # B3 transforms as (adj, 0) ~ 3-fold
    # B2 transforms as (fund, +/-1) ~ 2+2 fold
    # B1 transforms as (singlet, 0) ~ 1-fold
    #
    # For the diagonal V(B1,B1):
    # - SU(2) generators: K_{SU2} act on B1 as trivial rep -> <B1|K_{SU2}|B1> = 0
    #   UNLESS B1 carries residual SU(2) weight.
    # - C^2 generators: carry U(1) charge +/-1. <B1|K_{C^2}|B1> requires charge 0
    #   contribution. Since C^2 carries charge +/-1, diagonal elements vanish.
    # - U(1) generator: charge-neutral. <B1|K_{U1}|B1> can be nonzero.

    V_gg_tau020, V_per_tau020 = compute_V_gap_gap(kosmann, 3)  # tau = 0.20
    print(f"V(gap,gap) at tau=0.20: {V_gg_tau020:.12f}")
    print()
    print("Selection rule analysis:")
    print(f"  SU(2) contribution: {sum(V_per_tau020[a] for a in SU2_GEN):.12f}")
    print(f"    -> B1 is SU(2) singlet: <singlet|K_SU2|singlet> should vanish")
    print(f"       by angular momentum conservation (1 tensor 1 -> 1 requires J=0 component)")
    print(f"  C^2 contribution:  {sum(V_per_tau020[a] for a in C2_GEN):.12f}")
    print(f"    -> C^2 carries U(1) charge +/-1: <charge-0|K_C2|charge-0> = 0")
    print(f"  U(1) contribution: {sum(V_per_tau020[a] for a in U1_GEN):.12f}")
    print(f"    -> U(1) is charge-neutral: no selection rule forbids this")
    print()

    # ==================================================================
    # STEP 7: Comparison with V(B2,B2) (K-1e retraction reference)
    # ==================================================================
    print("=" * 70)
    print("STEP 7: Comparison with V(B2,B2) from K-1e Retraction")
    print("=" * 70)
    print()

    print(f"{'Mode pair':>12s} {'V(C^2-only)':>14s} {'V(full)':>14s} {'Status':>14s}")
    print("-" * 60)

    # V(B2,B2) max off-diagonal
    for ti in [3]:  # tau = 0.20
        V_C2_8x8 = np.zeros((8, 8))
        for a in C2_GEN:
            A = kosmann[f'A_antisym_{ti}_{a}']
            V_C2_8x8 += np.abs(A) ** 2

        V_B2B2_c2_max = 0.0
        V_B2B2_full_max = 0.0
        for i in B2_IDX:
            for j in B2_IDX:
                if i != j:
                    V_B2B2_c2_max = max(V_B2B2_c2_max, V_C2_8x8[i, j])
                    V_B2B2_full_max = max(V_B2B2_full_max, V_full_8x8[i, j])

        V_B1B1_c2 = V_C2_8x8[7, 7]
        V_B1B1_full = V_full_8x8[7, 7]

        print(f"{'V(B2,B2)':>12s} {V_B2B2_c2_max:14.10f} {V_B2B2_full_max:14.6f} "
              f"{'RETRACTED':>14s}")
        print(f"{'V(B1,B1)':>12s} {V_B1B1_c2:14.10f} {V_B1B1_full:14.10f} "
              f"{'<-- THIS':>14s}")

    print()

    # ==================================================================
    # GATE CLASSIFICATION
    # ==================================================================
    print("=" * 80)
    print("TRAP1-34a GATE CLASSIFICATION")
    print("=" * 80)
    print()

    # Check criterion across all tau
    all_zero = True
    max_V_gg = 0.0
    for ti in range(len(TAU_VALUES)):
        V_gg = results_by_tau[ti]['V_gg']
        max_V_gg = max(max_V_gg, V_gg)
        if V_gg > 0.01:
            all_zero = False

    print(f"V(gap,gap) across all tau:")
    for r in results_by_tau:
        flag = "  << NONZERO" if r['V_gg'] > 0.01 else ""
        print(f"  tau={r['tau']:.2f}: V(gap,gap) = {r['V_gg']:.12f}{flag}")

    print()
    print(f"Maximum V(gap,gap) across all tau: {max_V_gg:.12f}")
    print()

    if max_V_gg < 1e-14:
        verdict = "CONFIRMED"
        print(f"TRAP1-34a: *** {verdict} ***")
        print(f"  V(gap,gap) = 0 to machine epsilon ({max_V_gg:.2e}) at ALL tau.")
        print(f"  Trap 1 REMAINS. The gap-edge self-coupling vanishes identically")
        print(f"  with the full 8-generator Kosmann kernel.")
        print(f"  This is a DISTINCT selection rule from the C^2 vanishing in K-1e.")
    elif max_V_gg < 0.01:
        verdict = "WEAK"
        print(f"TRAP1-34a: *** {verdict} ***")
        print(f"  V(gap,gap) nonzero but small: max = {max_V_gg:.6f}")
        print(f"  Below gate threshold 0.01. Trap 1 weakened but not fully broken.")
    else:
        verdict = "BROKEN"
        print(f"TRAP1-34a: *** {verdict} ***")
        print(f"  V(gap,gap) = {max_V_gg:.6f} > 0.01 with full kernel.")
        print(f"  Trap 1 RETRACTED. Gap edge becomes additional pairing channel.")
        print(f"  This STRENGTHENS BCS -- the gap-edge divergence M ~ V/|xi|")
        print(f"  is now active with V > 0.")

    print()

    # Decomposition summary
    print("DECOMPOSITION AT REPRESENTATIVE tau VALUES:")
    for ti in [0, 3, 8]:
        r = results_by_tau[ti]
        print(f"  tau={r['tau']:.2f}: V(B1,B1) = {r['V_gg']:.12f}")
        print(f"    SU(2): {r['V_su2']:.12f}  |  C^2: {r['V_c2']:.12f}  |  U(1): {r['V_u1']:.12f}")

    print()

    # ==================================================================
    # SAVE
    # ==================================================================
    save_data = {
        'tau_values': TAU_VALUES,
        'verdict': np.array([verdict]),
        'max_V_gap_gap': max_V_gg,
    }

    for ti, r in enumerate(results_by_tau):
        save_data[f'V_gap_gap_{ti}'] = r['V_gg']
        save_data[f'V_gap_gap_SU2_{ti}'] = r['V_su2']
        save_data[f'V_gap_gap_C2_{ti}'] = r['V_c2']
        save_data[f'V_gap_gap_U1_{ti}'] = r['V_u1']
        save_data[f'lambda_B1_{ti}'] = r['lambda_B1']

    # Save full V matrix at tau=0.20
    save_data['V_full_8x8_tau020'] = V_full_8x8

    # Save off-diagonal V(gap,n) at tau=0.20
    V_gn_020, V_decomp_020 = compute_V_gap_offdiag(kosmann, 3)
    save_data['V_gap_offdiag_tau020'] = V_gn_020
    save_data['V_gap_offdiag_SU2_tau020'] = V_decomp_020['SU2']
    save_data['V_gap_offdiag_C2_tau020'] = V_decomp_020['C2']
    save_data['V_gap_offdiag_U1_tau020'] = V_decomp_020['U1']

    output_npz = os.path.join(SCRIPT_DIR, "s34a_trap1_reeval.npz")
    np.savez_compressed(output_npz, **save_data)
    print(f"Saved: {output_npz}")
    print(f"File size: {os.path.getsize(output_npz) / 1024:.1f} KB")
    print()

    # ==================================================================
    # PLOT
    # ==================================================================
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Panel 1: V(gap,gap) vs tau
    ax = axes[0, 0]
    taus = [r['tau'] for r in results_by_tau]
    V_ggs = [r['V_gg'] for r in results_by_tau]
    V_su2s = [r['V_su2'] for r in results_by_tau]
    V_c2s = [r['V_c2'] for r in results_by_tau]
    V_u1s = [r['V_u1'] for r in results_by_tau]

    ax.semilogy(taus, np.maximum(V_ggs, 1e-20), 'ko-', lw=2, ms=8, label='V(gap,gap) total')
    ax.semilogy(taus, np.maximum(V_su2s, 1e-20), 'bs--', lw=1.5, ms=6, label='SU(2)')
    ax.semilogy(taus, np.maximum(V_c2s, 1e-20), 'r^--', lw=1.5, ms=6, label='C^2')
    ax.semilogy(taus, np.maximum(V_u1s, 1e-20), 'gD--', lw=1.5, ms=6, label='U(1)')
    ax.axhline(y=0.01, color='red', ls=':', lw=2, label='Gate threshold')
    ax.axhline(y=1e-14, color='gray', ls=':', lw=1, alpha=0.5, label='Machine epsilon')
    ax.set_xlabel('tau (Jensen parameter)')
    ax.set_ylabel('V(gap,gap)')
    ax.set_title(f'Trap 1 Re-evaluation: V(B1,B1) vs tau\nTRAP1-34a: {verdict}')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(1e-22, 1)

    # Panel 2: V(gap,n) off-diagonal at tau=0.20
    ax = axes[0, 1]
    mode_labels = ['B3_0', 'B3_1', 'B3_2', 'B2_0', 'B2_1', 'B2_2', 'B2_3']
    colors_bar = ['tab:red']*3 + ['tab:blue']*4
    ax.bar(mode_labels, V_gn_020, color=colors_bar, alpha=0.7, edgecolor='black')
    for i, v in enumerate(V_gn_020):
        if v > 0.001:
            ax.text(i, v + 0.005, f'{v:.4f}', ha='center', va='bottom', fontsize=8)
    ax.set_ylabel('V(B1, mode_n)')
    ax.set_title('Off-diagonal: V(gap, other) at tau=0.20')
    ax.grid(True, alpha=0.3, axis='y')

    # Panel 3: Full V matrix heatmap at tau=0.20
    ax = axes[1, 0]
    im = ax.imshow(V_full_8x8, cmap='viridis', aspect='equal')
    plt.colorbar(im, ax=ax, shrink=0.8)
    ax.set_xticks(range(8))
    ax.set_yticks(range(8))
    labels_8 = ['B3_0', 'B3_1', 'B3_2', 'B2_0', 'B2_1', 'B2_2', 'B2_3', 'B1']
    ax.set_xticklabels(labels_8, fontsize=7, rotation=45)
    ax.set_yticklabels(labels_8, fontsize=7)
    ax.set_title('Full V_nm matrix (tau=0.20)')
    # Mark the B1 row/column
    ax.axhline(y=6.5, color='white', lw=2)
    ax.axvline(x=6.5, color='white', lw=2)

    # Panel 4: Comparison V(B1,B1) vs V(B2,B2) vs V(B1,B2)
    ax = axes[1, 1]
    V_B2B2_max = np.max(V_full_8x8[np.ix_(B2_IDX, B2_IDX)])
    V_B1B2_max = np.max(V_full_8x8[7, B2_IDX])
    V_B1B1 = V_full_8x8[7, 7]
    bar_labels = ['V(B2,B2)\nmax off-diag', 'V(B1,B2)\nmax', 'V(B1,B1)\ngap-gap']
    bar_values = [V_B2B2_max, V_B1B2_max, V_B1B1]
    bar_colors = ['tab:blue', 'tab:orange', 'tab:green' if V_B1B1 < 0.01 else 'tab:red']
    bars = ax.bar(bar_labels, bar_values, color=bar_colors, alpha=0.7, edgecolor='black')
    ax.axhline(y=0.01, color='red', ls='--', lw=2, label='Gate threshold')
    for bar, v in zip(bars, bar_values):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.005,
                f'{v:.6f}', ha='center', va='bottom', fontsize=9, fontweight='bold')
    ax.set_ylabel('V_nm')
    ax.set_title(f'Comparison: K-1e Retraction vs Trap 1\n(tau=0.20, full kernel)')
    ax.legend()
    ax.grid(True, alpha=0.3, axis='y')

    fig.suptitle(f'TRAP1-34a: {verdict} | max V(gap,gap) = {max_V_gg:.2e}',
                 fontsize=14, fontweight='bold')
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plot_path = os.path.join(SCRIPT_DIR, "s34a_trap1_reeval.png")
    plt.savefig(plot_path, dpi=150)
    plt.close()
    print(f"Plot saved: {plot_path}")

    return verdict, max_V_gg, results_by_tau


if __name__ == "__main__":
    t_start = time.time()
    verdict, max_V, results = run()
    elapsed = time.time() - t_start

    print()
    print("=" * 80)
    print(f"TRAP1-34a FINAL: {verdict} | max V(gap,gap) = {max_V:.12f}")
    print(f"Runtime: {elapsed:.1f}s")
    print("=" * 80)
