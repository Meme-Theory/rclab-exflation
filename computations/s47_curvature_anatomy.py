#!/usr/bin/env python3
"""
S47 CURVATURE-ANATOMY-47: Sectional Curvature Landscape of Jensen-Deformed SU(3)
==================================================================================

Computes and visualizes all 28 = C(8,2) sectional curvatures K(e_a, e_b; tau)
for the Jensen-deformed left-invariant metric on SU(3).

Mathematical framework:
    su(3) = u(1) + su(2) + C^2     (Baptista reductive decomposition)
    g_tau = e^{2tau} g_0|_{u(1)} + e^{-2tau} g_0|_{su(2)} + e^{tau} g_0|_{C^2}

    Generators (Gell-Mann / anti-Hermitian convention):
        u(1):   e_7 = lambda_8         (1D: Cartan generator H_8)
        su(2):  e_0, e_1, e_2          (3D: lambda_1, lambda_2, lambda_3)
        C^2:    e_3, e_4, e_5, e_6     (4D: lambda_4, lambda_5, lambda_6, lambda_7)

    Sectional curvature K(e_a, e_b) = R(e_a,e_b,e_b,e_a) in ON frame:
        K(e_a, e_b) = R^a_{bba}  [= R_abcd[a,b,b,a] in our storage]

    For bi-invariant SU(3) at tau=0:
        K(X,Y) = (1/4)|[X,Y]|^2  (Milnor formula for bi-invariant metrics)
        This is NOT constant -- SU(3) is not rank-1 symmetric.
        K=0 for commuting pairs (e.g. u(1)-su(2)).

Pair classification (28 total):
    SU2-SU2:  su(2)-su(2)      (3 pairs: within {e_0, e_1, e_2})
    SU2-C2:   su(2)-C^2        (12 pairs: cross su(2) x C^2)
    C2-C2:    C^2-C^2          (6 pairs: within {e_3, e_4, e_5, e_6})
    U1-SU2:   u(1)-su(2)       (3 pairs: e_7 with e_0, e_1, e_2)
    U1-C2:    u(1)-C^2         (4 pairs: e_7 with e_3, e_4, e_5, e_6)
    Total: 3 + 12 + 6 + 3 + 4 = 28.

Baptista reference: Paper 13, Section 2.6 (scalar curvature formula eq 2.40).
    Uses Riemann tensor from connection infrastructure in tier1_dirac_spectrum.py
    (validated in r20a_riemann_tensor.py, 147/147 checks).

Output:
    - s47_curvature_anatomy.npz
    - s47_curvature_anatomy.png (two-panel figure)

Author: Baptista-Spacetime-Analyst (Session 47)
Date: 2026-03-16
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tier1_dirac_spectrum import (
    su3_generators,
    compute_structure_constants,
    compute_killing_form,
    jensen_metric,
    orthonormal_frame,
    frame_structure_constants,
    connection_coefficients,
    U1_IDX,
    SU2_IDX,
    C2_IDX,
)
from canonical_constants import tau_fold


# =============================================================================
# MODULE 1: RIEMANN TENSOR
# =============================================================================

def compute_riemann_tensor_ON(ft, Gamma, n=8):
    """
    Full Riemann tensor R[a,b,c,f] = R^f_{abc} in ON frame.

    R^f_{abc} = sum_d (Gamma^d_{bc} Gamma^f_{ad} - Gamma^d_{ac} Gamma^f_{bd}
                       - ft^d_{ab} Gamma^f_{dc})

    Storage: R[a,b,c,f] = R^f_{abc} where f is the free (upper) index.
    Equivalent to r20a convention: R_abcd[a,b,c,d] = R^d_{abc}.
    """
    R = np.zeros((n, n, n, n), dtype=np.float64)
    for a in range(n):
        for b in range(n):
            for c in range(n):
                for f in range(n):
                    val = 0.0
                    for d in range(n):
                        val += Gamma[d, b, c] * Gamma[f, a, d]
                        val -= Gamma[d, a, c] * Gamma[f, b, d]
                        val -= ft[a, b, d] * Gamma[f, d, c]
                    R[a, b, c, f] = val
    return R


# =============================================================================
# MODULE 2: PAIR CLASSIFICATION
# =============================================================================

GEN_SHORT = ['l1', 'l2', 'l3', 'l4', 'l5', 'l6', 'l7', 'l8']


def classify_pair(a, b):
    """Classify a pair (a, b) by type."""
    a_type = 'u1' if a in U1_IDX else ('su2' if a in SU2_IDX else 'c2')
    b_type = 'u1' if b in U1_IDX else ('su2' if b in SU2_IDX else 'c2')
    types = tuple(sorted([a_type, b_type]))
    type_map = {
        ('su2', 'su2'): 'SU2-SU2',
        ('c2', 'c2'):   'C2-C2',
        ('c2', 'su2'):  'SU2-C2',
        ('su2', 'u1'):  'U1-SU2',
        ('c2', 'u1'):   'U1-C2',
    }
    return type_map[types]


def get_all_pairs():
    """Get all 28 pairs (a,b) with a<b, classified by type."""
    pairs = []
    for a in range(8):
        for b in range(a + 1, 8):
            ptype = classify_pair(a, b)
            label = f'{GEN_SHORT[a]}-{GEN_SHORT[b]}'
            pairs.append((a, b, ptype, label))
    return pairs


# =============================================================================
# MODULE 3: COMPUTE ALL CURVATURES AT ONE TAU
# =============================================================================

def compute_all_at_tau(s, pairs):
    """
    Compute all 28 sectional curvatures, Ricci tensor, and scalar curvature
    at Jensen parameter s.
    """
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    B_ab = compute_killing_form(f_abc)
    g_s = jensen_metric(B_ab, s)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    R_abcd = compute_riemann_tensor_ON(ft, Gamma)

    # Sectional curvatures: K(e_a, e_b) = R^a_{bba} = R_abcd[a,b,b,a]
    K_vec = np.array([R_abcd[a, b, b, a] for a, b, _, _ in pairs])

    # Ricci tensor: Ric_{bc} = sum_a R^a_{bca} = einsum('abca->bc', R)
    Ric = np.einsum('abca->bc', R_abcd)
    R_scalar = np.trace(Ric)
    Ric_eigs = np.sort(np.linalg.eigvalsh(Ric))

    return K_vec, Ric, R_scalar, Ric_eigs, ft


# =============================================================================
# MODULE 4: FIND DISTINCT VALUES
# =============================================================================

def find_distinct(arr, tol=1e-8):
    """Find distinct values in array, returning (value, multiplicity) list."""
    s = np.sort(arr)
    groups = []
    current = s[0]
    count = 1
    for i in range(1, len(s)):
        if abs(s[i] - current) < tol:
            count += 1
        else:
            groups.append((current, count))
            current = s[i]
            count = 1
    groups.append((current, count))
    return groups


# =============================================================================
# MAIN
# =============================================================================

def main():
    print("=" * 78)
    print("  S47 CURVATURE-ANATOMY-47: Sectional Curvature Landscape")
    print("  Jensen-Deformed SU(3)")
    print("=" * 78)

    pairs = get_all_pairs()
    n_pairs = len(pairs)

    # Tau grid: fine spacing from 0 to 0.25
    tau_coarse = np.arange(0, 0.26, 0.01)
    tau_values = np.unique(np.sort(np.concatenate([tau_coarse, [tau_fold]])))
    n_tau = len(tau_values)

    print(f"\n  {n_pairs} pairs, {n_tau} tau values [{tau_values[0]:.3f}, {tau_values[-1]:.3f}]")
    type_counts = {}
    for _, _, ptype, _ in pairs:
        type_counts[ptype] = type_counts.get(ptype, 0) + 1
    for ptype in ['SU2-SU2', 'SU2-C2', 'C2-C2', 'U1-SU2', 'U1-C2']:
        print(f"    {ptype:10s}: {type_counts.get(ptype, 0)} pairs")

    # =========================================================================
    #  SWEEP
    # =========================================================================
    K_all = np.zeros((n_tau, n_pairs))
    R_scalar_all = np.zeros(n_tau)
    Ric_eigs_all = np.zeros((n_tau, 8))

    report_taus = {0.0, 0.05, 0.10, 0.15, 0.19, 0.25}
    ft_at_0 = None

    for i, tau in enumerate(tau_values):
        K_vec, Ric, R_scalar, Ric_eigs, ft = compute_all_at_tau(tau, pairs)
        K_all[i] = K_vec
        R_scalar_all[i] = R_scalar
        Ric_eigs_all[i] = Ric_eigs
        if tau == 0.0:
            ft_at_0 = ft.copy()
        if tau in report_taus:
            K_pos = K_vec[K_vec > 1e-14]
            print(f"\n  tau={tau:.2f}: R={R_scalar:.8f}  "
                  f"K in [{K_vec.min():.8f}, {K_vec.max():.8f}]  "
                  f"{'ratio=' + f'{K_pos.max()/K_pos.min():.3f}' if len(K_pos) > 0 and K_pos.min() > 0 else ''}")

    # =========================================================================
    #  VALIDATION: tau = 0
    # =========================================================================
    print(f"\n{'='*78}")
    print("  VALIDATION: tau = 0 (bi-invariant metric)")
    print(f"{'='*78}")

    K_at_0 = K_all[0]

    # For bi-invariant metrics: K(X,Y) = (1/4)|[X,Y]|^2 in ON frame
    # This is NOT constant on SU(3) -- only on rank-1 symmetric spaces (S^n, etc.)
    print(f"  R_scalar(0) = {R_scalar_all[0]:.12f}  (expected 2.0)")
    err_R0 = abs(R_scalar_all[0] - 2.0)
    print(f"  |R(0) - 2| = {err_R0:.2e}  {'PASS' if err_R0 < 1e-10 else 'FAIL'}")

    # Verify bi-invariant formula: K = (1/4) |[e_a,e_b]|^2
    max_err = 0.0
    for j, (a, b, ptype, label) in enumerate(pairs):
        comm_sq = np.sum(ft_at_0[a, b, :] ** 2)
        K_formula = 0.25 * comm_sq
        max_err = max(max_err, abs(K_at_0[j] - K_formula))
    print(f"  K = (1/4)|[e_a,e_b]|^2 check: max error = {max_err:.2e}  "
          f"{'PASS' if max_err < 1e-12 else 'FAIL'}")

    # R = 2*sum_{a<b} K(a,b) identity
    R_from_sum = 2.0 * np.sum(K_at_0)
    err_R_sum = abs(R_from_sum - R_scalar_all[0])
    print(f"  R = 2*sum(K) check: {R_from_sum:.12f} vs {R_scalar_all[0]:.12f}  "
          f"err={err_R_sum:.2e}  {'PASS' if err_R_sum < 1e-10 else 'FAIL'}")

    # Distinct K values at tau=0
    dist_0 = find_distinct(K_at_0)
    print(f"\n  Distinct K at tau=0: {len(dist_0)} branches")
    for K_val, cnt in dist_0:
        # Identify which type(s) have this K
        types_at = set()
        for j, (a, b, ptype, label) in enumerate(pairs):
            if abs(K_at_0[j] - K_val) < 1e-10:
                types_at.add(ptype)
        print(f"    K = {K_val:.10f}  (deg {cnt})  types: {', '.join(sorted(types_at))}")

    # =========================================================================
    #  RESULTS AT FOLD
    # =========================================================================
    idx_fold = np.argmin(np.abs(tau_values - tau_fold))
    K_fold = K_all[idx_fold]

    print(f"\n{'='*78}")
    print(f"  RESULTS AT FOLD (tau = {tau_values[idx_fold]:.2f})")
    print(f"{'='*78}")

    # Group by type
    type_groups = {}
    for j, (a, b, ptype, label) in enumerate(pairs):
        type_groups.setdefault(ptype, []).append((j, a, b, label, K_fold[j]))

    for ptype in ['SU2-SU2', 'U1-SU2', 'C2-C2', 'U1-C2', 'SU2-C2']:
        group = type_groups.get(ptype, [])
        if not group:
            continue
        K_group = [g[4] for g in group]
        print(f"\n  {ptype} ({len(group)} pairs):")
        for j, a, b, label, K_val in group:
            print(f"    {label:8s}: K = {K_val:.8f}")
        print(f"    mean = {np.mean(K_group):.8f}, std = {np.std(K_group):.2e}")

    # Overall statistics
    K_pos = K_fold[K_fold > 1e-14]
    K_neg = K_fold[K_fold < -1e-14]
    K_zero = K_fold[np.abs(K_fold) < 1e-14]

    print(f"\n  Summary:")
    print(f"    K_min  = {K_fold.min():.8f}")
    print(f"    K_max  = {K_fold.max():.8f}")
    if len(K_pos) > 0:
        print(f"    K_max/K_min (positive) = {K_pos.max()/K_pos.min():.4f}")
    print(f"    Flat directions (K=0):  {len(K_zero)}")
    print(f"    Negative curvatures:    {len(K_neg)}")

    # Distinct K at fold
    dist_fold = find_distinct(K_fold)
    print(f"\n  Distinct K at fold: {len(dist_fold)} branches")
    for K_val, cnt in dist_fold:
        types_at = set()
        for j, (a, b, ptype, label) in enumerate(pairs):
            if abs(K_fold[j] - K_val) < 1e-8:
                types_at.add(ptype)
        print(f"    K = {K_val:.8f}  (deg {cnt})  types: {', '.join(sorted(types_at))}")

    # Cross-check R at fold against s46
    R_s46_fold = 2.018143955851359
    R_here = R_scalar_all[idx_fold]
    err_R = abs(R_here - R_s46_fold) / abs(R_s46_fold)
    print(f"\n  R cross-check at fold:")
    print(f"    computed = {R_here:.12f}")
    print(f"    s46 ref  = {R_s46_fold:.12f}")
    print(f"    rel err  = {err_R:.2e}  {'PASS' if err_R < 1e-8 else 'FAIL'}")

    # =========================================================================
    #  FIGURES
    # =========================================================================
    print(f"\n{'='*78}")
    print("  GENERATING FIGURES")
    print(f"{'='*78}")

    type_colors = {
        'SU2-SU2': '#1565C0',    # Dark blue
        'C2-C2':   '#2E7D32',    # Dark green
        'SU2-C2':  '#E65100',    # Dark orange
        'U1-SU2':  '#7B1FA2',    # Dark purple
        'U1-C2':   '#C62828',    # Dark red
    }
    type_labels_nice = {
        'SU2-SU2': 'su(2)-su(2)',
        'C2-C2':   r'$\mathbb{C}^2$-$\mathbb{C}^2$',
        'SU2-C2':  r'su(2)-$\mathbb{C}^2$',
        'U1-SU2':  'u(1)-su(2)',
        'U1-C2':   r'u(1)-$\mathbb{C}^2$',
    }

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 7.5))

    # --- Panel A: Curvature rose at the fold ---
    type_order = ['SU2-SU2', 'U1-SU2', 'C2-C2', 'U1-C2', 'SU2-C2']
    bar_x = []
    bar_K = []
    bar_colors = []
    tick_positions = []
    tick_labels_plot = []
    group_boundaries = []
    x_pos = 0

    for ptype in type_order:
        group = type_groups.get(ptype, [])
        if not group:
            continue
        group_start = x_pos
        for j, a, b, label, K_val in group:
            bar_x.append(x_pos)
            bar_K.append(K_val)
            bar_colors.append(type_colors[ptype])
            x_pos += 1
        group_center = (group_start + x_pos - 1) / 2.0
        tick_positions.append(group_center)
        tick_labels_plot.append(f'{type_labels_nice[ptype]}\n({len(group)})')
        group_boundaries.append(x_pos - 0.5)
        x_pos += 1

    ax1.bar(bar_x, bar_K, color=bar_colors, edgecolor='black', linewidth=0.5, width=0.7)

    # Reference lines: K values at tau=0
    for K_val, cnt in dist_0:
        if K_val > 1e-10:
            ax1.axhline(y=K_val, color='black', linestyle='--', linewidth=0.8, alpha=0.4)

    # Label the tau=0 reference
    K_max_0 = max(v for v, _ in dist_0)
    ax1.annotate(f'K(bi-inv) = {K_max_0:.4f}',
                 xy=(0, K_max_0), xytext=(2, K_max_0 + 0.003),
                 fontsize=9, color='black', alpha=0.6)

    for xb in group_boundaries[:-1]:
        ax1.axvline(x=xb, color='gray', linestyle=':', linewidth=0.8, alpha=0.4)

    ax1.set_xticks(tick_positions)
    ax1.set_xticklabels(tick_labels_plot, fontsize=9)
    ax1.set_ylabel('Sectional curvature K', fontsize=12)
    ax1.set_title(r'(A) Sectional curvatures at the fold ($\tau$ = ' + f'{tau_fold})', fontsize=13)
    ax1.grid(axis='y', alpha=0.3)

    # --- Panel B: Curvature evolution ---
    # Plot each DISTINCT branch as a separate line.
    # At each tau, group pair indices by their K value. Track branch identity
    # by the pair index of a representative from each branch at the fold.
    # Strategy: find distinct branches at fold, then plot each representative.
    branch_reps = []  # (pair_index, K_fold, type, deg)
    used = set()
    for K_val, cnt in dist_fold:
        for j, (a, b, ptype, label) in enumerate(pairs):
            if j not in used and abs(K_fold[j] - K_val) < 1e-8:
                branch_reps.append((j, K_val, ptype, cnt))
                # Mark all pairs with this K value as used
                for jj, (aa, bb, pp, ll) in enumerate(pairs):
                    if abs(K_fold[jj] - K_val) < 1e-8:
                        used.add(jj)
                break

    # Sort by K value at fold (ascending) for consistent visual ordering
    branch_reps.sort(key=lambda x: x[1])

    for j_rep, K_val, ptype, deg in branch_reps:
        lw = 2.5 if deg >= 4 else 2.0
        ls = '-'
        # For C2-C2 which has two sub-branches, use dashed for the minor one
        same_type_branches = [(j2, k2, p2, d2) for j2, k2, p2, d2 in branch_reps if p2 == ptype]
        if len(same_type_branches) > 1:
            idx_in_type = [j2 for j2, _, _, _ in same_type_branches].index(j_rep)
            ls = ['-', '--'][idx_in_type] if idx_in_type < 2 else '-.'

        ax2.plot(tau_values, K_all[:, j_rep],
                 color=type_colors[ptype], linewidth=lw, linestyle=ls,
                 label=f'{type_labels_nice[ptype]} (deg {deg})',
                 marker='o', markersize=2.5)

    ax2.axvline(x=tau_fold, color='gray', linestyle=':', linewidth=1.5,
                label=r'$\tau_{\rm fold}$' + f' = {tau_fold}', alpha=0.7)

    ax2.set_xlabel(r'Jensen parameter $\tau$', fontsize=12)
    ax2.set_ylabel('Sectional curvature K', fontsize=12)
    ax2.set_title('(B) Curvature splitting under Jensen deformation', fontsize=13)
    ax2.legend(fontsize=8.5, loc='upper left', ncol=1)
    ax2.grid(alpha=0.3)

    plt.tight_layout()
    fig_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            's47_curvature_anatomy.png')
    plt.savefig(fig_path, dpi=200, bbox_inches='tight')
    print(f"\n  Saved: {fig_path}")
    plt.close()

    # =========================================================================
    #  SAVE DATA
    # =========================================================================
    npz_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            's47_curvature_anatomy.npz')
    pair_types = np.array([p[2] for p in pairs])
    pair_labels = np.array([p[3] for p in pairs])
    pair_indices = np.array([(p[0], p[1]) for p in pairs])

    K_pos_fold = K_fold[K_fold > 1e-14]
    anisotropy = K_pos_fold.max() / K_pos_fold.min() if len(K_pos_fold) > 0 and K_pos_fold.min() > 0 else np.inf

    np.savez(npz_path,
             tau_values=tau_values,
             K_all=K_all,
             R_scalar_all=R_scalar_all,
             Ric_eigs_all=Ric_eigs_all,
             pair_types=pair_types,
             pair_labels=pair_labels,
             pair_indices=pair_indices,
             tau_fold=tau_fold,
             K_fold=K_fold,
             K_fold_min=K_fold.min(),
             K_fold_max=K_fold.max(),
             K_fold_anisotropy=anisotropy,
             n_flat_directions=int(np.sum(np.abs(K_fold) < 1e-14)),
             any_negative=bool(np.any(K_all < -1e-14)),
             R_crosscheck_err=err_R,
             )
    print(f"  Saved: {npz_path}")

    # =========================================================================
    #  SUMMARY
    # =========================================================================
    print(f"\n{'='*78}")
    print("  CURVATURE-ANATOMY-47 SUMMARY")
    print(f"{'='*78}")
    print(f"  Bi-invariant (tau=0):")
    for K_val, cnt in dist_0:
        print(f"    K = {K_val:.10f}  (deg {cnt})")
    print(f"    R_scalar = {R_scalar_all[0]:.10f}")
    print(f"\n  At fold (tau={tau_fold}):")
    for K_val, cnt in dist_fold:
        print(f"    K = {K_val:.8f}  (deg {cnt})")
    print(f"    K_max/K_min (positive) = {anisotropy:.4f}")
    print(f"    Flat directions: {int(np.sum(np.abs(K_fold) < 1e-14))}")
    print(f"    Negative curvatures: {int(np.sum(K_fold < -1e-14))}")
    print(f"    R_scalar = {R_scalar_all[idx_fold]:.10f}")
    print(f"    R cross-check: {'PASS' if err_R < 1e-8 else 'FAIL'} (err={err_R:.2e})")
    print(f"\n  Physical interpretation:")
    print(f"    The Jensen deformation splits the uniform bi-invariant curvature")
    print(f"    into {len(dist_fold)} distinct branches. The su(2)-su(2) planes")
    print(f"    become the most curved (K={K_fold.max():.6f}), while su(2)-C^2")
    print(f"    planes flatten toward zero (K={K_fold[np.array([j for j,(a,b,p,l) in enumerate(pairs) if p=='SU2-C2'])].mean():.6f}).")
    print(f"    The u(1)-su(2) planes remain EXACTLY flat at all tau (K=0).")
    print(f"    This is because [u(1), su(2)] = 0 exactly, and the Jensen")
    print(f"    deformation preserves this commutation since both subspaces")
    print(f"    are within u(2).")
    print(f"\n  Gate CURVATURE-ANATOMY-47: INFO (visualization task)")


if __name__ == '__main__':
    main()
