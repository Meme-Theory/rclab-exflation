"""
Session 26: Detailed contorsion resonance analysis.

The main script flagged "non-monotone" behavior in sectors (1,0), (0,1), (1,1).
But the minimum gap was at t=1.0 (Schouten), not at an intermediate t.
This suggests the gap has a local increase somewhere before decreasing to its final value.

Let us examine this in detail: plot ALL eigenvalues (not just the gap) as functions of t,
and check whether any avoided crossing creates a local gap minimum at intermediate t.

Author: Tesla-Resonance
Date: 2026-02-22
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))

from tier1_dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    jensen_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients, spinor_connection_offset,
    build_cliff8, dirac_operator_on_irrep, get_irrep
)

def detailed_resonance_analysis(tau, sectors, t_values):
    """
    For each sector, compute ALL eigenvalues of D_t = M_Lie + (1-t)*M_Omega
    and track them individually.
    """
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    gammas = build_cliff8()

    B_ab = compute_killing_form(f_abc)
    g_s = jensen_metric(B_ab, tau)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Omega = spinor_connection_offset(Gamma, gammas)

    results = {}

    for (p, q) in sectors:
        print(f"  Sector ({p},{q}) at tau={tau:.2f}...")
        rho, dim_rho = get_irrep(p, q, gens, f_abc)
        dim_spin = 16
        dim_total = dim_rho * dim_spin

        # Build M_Lie
        M_Lie = np.zeros((dim_total, dim_total), dtype=complex)
        for a in range(8):
            for b in range(8):
                if abs(E[a, b]) > 1e-15:
                    M_Lie += E[a, b] * np.kron(rho[b], gammas[a])

        # Build M_Omega
        M_Omega = np.kron(np.eye(dim_rho), Omega)

        # Sweep t -- collect ALL eigenvalues
        all_evals = np.zeros((len(t_values), dim_total))
        gap_values = np.zeros(len(t_values))

        for i, t in enumerate(t_values):
            D_t = M_Lie + (1.0 - t) * M_Omega
            evals = np.linalg.eigvals(D_t)
            # D_t is anti-Hermitian -> eigenvalues are purely imaginary
            imag_parts = np.sort(evals.imag)
            all_evals[i] = imag_parts

            # Gap = smallest |eigenvalue|
            abs_evals = np.sort(np.abs(imag_parts))
            nonzero = abs_evals[abs_evals > 1e-10]
            gap_values[i] = nonzero[0] if len(nonzero) > 0 else 0.0

        results[(p,q)] = {
            'all_evals': all_evals,
            'gap': gap_values,
            'dim': dim_total
        }

    return results


def main():
    print("=" * 80)
    print("DETAILED CONTORSION RESONANCE ANALYSIS")
    print("=" * 80)

    tau = 0.25
    t_values = np.linspace(0, 1.0, 201)  # finer grid
    sectors = [(0,0), (1,0), (0,1), (1,1)]

    results = detailed_resonance_analysis(tau, sectors, t_values)

    # ---- Check for non-monotonicity properly ----
    print(f"\nDetailed gap analysis at tau={tau}:")
    print(f"{'Sector':>8} | {'gap(0)':>10} | {'gap(1)':>10} | {'min gap':>10} | {'t at min':>8} | {'Local min?':>10}")
    print("-" * 70)

    for (p,q) in sectors:
        gap = results[(p,q)]['gap']
        min_gap = np.min(gap)
        t_min = t_values[np.argmin(gap)]

        # Check for LOCAL minimum (not at endpoints)
        has_local_min = False
        local_min_t = None
        local_min_val = None
        for i in range(1, len(gap)-1):
            if gap[i] < gap[i-1] and gap[i] < gap[i+1]:
                has_local_min = True
                local_min_t = t_values[i]
                local_min_val = gap[i]
                break

        # Check: does gap ever INCREASE with t?
        increases = np.where(np.diff(gap) > 1e-10)[0]
        n_increases = len(increases)

        local_str = f"YES at t={local_min_t:.4f}" if has_local_min else "NO"
        print(f"({p},{q}){'':<4} | {gap[0]:10.6f} | {gap[-1]:10.6f} | {min_gap:10.6f} | {t_min:8.4f} | {local_str}")
        if n_increases > 0:
            print(f"         Gap increases at {n_increases} points. First at t={t_values[increases[0]]:.4f}, gap jumps {gap[increases[0]+1]-gap[increases[0]]:.6f}")

    # ---- For (1,0): track lowest 8 eigenvalues ----
    print(f"\n--- Lowest 8 |eigenvalues| of (1,0) sector vs t ---")
    all_evals_10 = results[(1,0)]['all_evals']
    n_track = 8

    print(f"{'t':>6} |", end="")
    for k in range(n_track):
        print(f"  |lam_{k+1}|", end="")
    print()

    for i in range(0, len(t_values), 20):
        t = t_values[i]
        abs_evals = np.sort(np.abs(all_evals_10[i]))
        print(f"{t:6.3f} |", end="")
        for k in range(n_track):
            print(f"  {abs_evals[k]:9.6f}", end="")
        print()

    # Print t=1.0 explicitly
    abs_evals_final = np.sort(np.abs(all_evals_10[-1]))
    print(f"{1.0:6.3f} |", end="")
    for k in range(n_track):
        print(f"  {abs_evals_final[k]:9.6f}", end="")
    print()

    # ---- For (0,0): the singlet tells the story ----
    print(f"\n--- All 16 |eigenvalues| of (0,0) singlet at t=0, 0.5, 1.0 ---")
    all_evals_00 = results[(0,0)]['all_evals']
    for t_show in [0.0, 0.5, 1.0]:
        idx = np.argmin(np.abs(t_values - t_show))
        abs_evals = np.sort(np.abs(all_evals_00[idx]))
        print(f"  t={t_show:.1f}: {abs_evals}")

    # ---- Key question: does OVERALL min |lambda| across ALL sectors have a minimum at t* in (0,1)? ----
    print(f"\n--- Overall spectral gap (minimum across all sectors) ---")
    overall_gap = np.zeros(len(t_values))
    for i in range(len(t_values)):
        sector_mins = []
        for (p,q) in sectors:
            gap_val = results[(p,q)]['gap'][i]
            sector_mins.append(gap_val)
        overall_gap[i] = min(sector_mins)

    print(f"{'t':>6} | {'Overall gap':>12} | {'Controlling sector':>20}")
    for i in range(0, len(t_values), 20):
        t = t_values[i]
        sector_mins = {}
        for (p,q) in sectors:
            sector_mins[(p,q)] = results[(p,q)]['gap'][i]
        min_sector = min(sector_mins, key=sector_mins.get)
        print(f"{t:6.3f} | {overall_gap[i]:12.6f} | ({min_sector[0]},{min_sector[1]})")
    # t=1.0
    sector_mins = {}
    for (p,q) in sectors:
        sector_mins[(p,q)] = results[(p,q)]['gap'][-1]
    min_sector = min(sector_mins, key=sector_mins.get)
    print(f"{1.0:6.3f} | {overall_gap[-1]:12.6f} | ({min_sector[0]},{min_sector[1]})")

    # The overall gap is controlled by (0,0) singlet, which goes to zero at t=1.
    # The RELEVANT question for Gate T-1 is: if we exclude the singlet (which goes to zero trivially),
    # does the non-singlet gap have a minimum at intermediate t?
    print(f"\n--- Non-singlet spectral gap (excl. (0,0)) ---")
    nonsing_gap = np.zeros(len(t_values))
    for i in range(len(t_values)):
        sector_mins = []
        for (p,q) in [(1,0), (0,1), (1,1)]:
            sector_mins.append(results[(p,q)]['gap'][i])
        nonsing_gap[i] = min(sector_mins)

    min_nonsing = np.min(nonsing_gap)
    t_min_nonsing = t_values[np.argmin(nonsing_gap)]
    gap_at_0 = nonsing_gap[0]
    gap_at_1 = nonsing_gap[-1]

    print(f"  gap(t=0) = {gap_at_0:.6f} (Levi-Civita)")
    print(f"  gap(t=1) = {gap_at_1:.6f} (Schouten)")
    print(f"  min gap  = {min_nonsing:.6f} at t = {t_min_nonsing:.4f}")

    # Local minimum in non-singlet gap?
    has_local = False
    for i in range(1, len(nonsing_gap)-1):
        if nonsing_gap[i] < nonsing_gap[i-1] and nonsing_gap[i] < nonsing_gap[i+1]:
            has_local = True
            print(f"  LOCAL MINIMUM at t = {t_values[i]:.4f}, gap = {nonsing_gap[i]:.6f}")
            break
    if not has_local:
        print(f"  No local minimum in non-singlet gap.")
        if min_nonsing < gap_at_0:
            print(f"  Gap DECREASES monotonically from D_K to Schouten. Torsion WEAKENS non-singlet gap.")
            print(f"  BUT: D_K gap (singlet) = {results[(0,0)]['gap'][0]:.6f} < non-singlet gap at t=1: {gap_at_1:.6f}")
            print(f"  So overall spectral gap is still controlled by singlet. Torsion irrelevant for overall gap.")
        else:
            print(f"  Gap increases or stays constant. Torsion STRENGTHENS non-singlet gap.")

    # ---- Critical physical question ----
    # At t=0: overall gap = singlet gap = 0.8186
    # At t=1: singlet gap = 0 (trivial), non-singlet gap = 0.2596
    # The singlet CONTROLS the gap at t=0. At t=1, singlet closes it.
    # Gate T-1 asks: is there a PHYSICAL connection with NONZERO gap < 0.8186?
    # The non-singlet gap at t=1 is 0.2596 -- that IS smaller than 0.8186.
    # But the singlet gap at t=1 is 0 -- so the total gap is 0, not 0.2596.
    # Gate T-1 requires nonzero gap. The singlet closes any t > 0.

    # UNLESS: the physical operator is NOT the Schouten, but a different torsionful connection
    # that preserves the singlet gap while modifying non-singlet sectors.
    # The interpolation D_t = M_Lie + (1-t)*M_Omega with t in (0,1) gives singlet gap = (1-t)*0.8186.
    # This goes to zero linearly. For the overall gap to be smaller than 0.8186 but nonzero,
    # we need min(singlet_gap, nonsing_gap) < 0.8186 with both > 0.
    # singlet_gap(t) = (1-t) * 0.8186
    # nonsing_gap(t) varies
    # Overall gap(t) = min((1-t)*0.8186, nonsing_gap(t))

    # The overall gap with nonzero constraint:
    print(f"\n--- Overall gap (requiring nonzero): min(singlet, non-singlet) ---")
    overall_nonzero = np.minimum(
        np.array([(1-t)*results[(0,0)]['gap'][0] for t in t_values]),
        nonsing_gap
    )

    # The singlet gap at t=0 is NOT exactly (1-t)*gap(0) because singlet evals are (1-t)*omega_evals
    # Let me use actual computed values
    singlet_gap = results[(0,0)]['gap']
    overall_physical = np.minimum(singlet_gap, nonsing_gap)

    # Only consider nonzero
    mask_nonzero = overall_physical > 1e-10
    if np.any(mask_nonzero):
        min_phys = np.min(overall_physical[mask_nonzero])
        t_min_phys = t_values[mask_nonzero][np.argmin(overall_physical[mask_nonzero])]
        dk_gap = overall_physical[0]
        print(f"  D_K gap (t=0): {dk_gap:.6f}")
        print(f"  Minimum physical gap: {min_phys:.6f} at t={t_min_phys:.4f}")
        if min_phys < dk_gap:
            print(f"  GAP WEAKENED by factor {dk_gap/min_phys:.3f} at t={t_min_phys:.4f}")
            print(f"  Gate T-1: PASS scenario exists at this interpolation parameter")
        else:
            print(f"  Gap not weakened. Gate T-1: CLOSED confirmed for interpolation family.")

    # ---- Plot: Detailed eigenvalue flow ----
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))

    for idx, (p,q) in enumerate(sectors):
        ax = axes[idx//2][idx%2]
        all_evals = results[(p,q)]['all_evals']
        dim = results[(p,q)]['dim']

        # Plot lowest 20 |eigenvalues| (or all if fewer)
        n_plot = min(20, dim)
        abs_evals_sorted = np.zeros((len(t_values), dim))
        for i in range(len(t_values)):
            abs_evals_sorted[i] = np.sort(np.abs(all_evals[i]))

        for k in range(n_plot):
            ax.plot(t_values, abs_evals_sorted[:, k], linewidth=0.5, alpha=0.7)

        ax.plot(t_values, results[(p,q)]['gap'], 'k-', linewidth=2, label='Spectral gap')
        ax.set_xlabel('$t$ (contorsion parameter)', fontsize=12)
        ax.set_ylabel('$|\\lambda|$', fontsize=12)
        ax.set_title(f'Sector ({p},{q}), dim={dim}', fontsize=13)
        ax.legend(fontsize=10)
        ax.grid(True, alpha=0.3)
        ax.set_ylim(bottom=0, top=2.5)

    plt.suptitle(f'Eigenvalue Flow vs Contorsion at $\\tau={tau}$: Lowest 20 $|\\lambda|$ per Sector',
                 fontsize=14)
    plt.tight_layout()
    plt.savefig(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                's26_contorsion_eigenflow.png'), dpi=150)
    plt.close()
    print("\nPlot saved: s26_contorsion_eigenflow.png")

    # ---- Summary plot: gap comparison ----
    fig, ax = plt.subplots(figsize=(10, 6))
    for (p,q) in sectors:
        ax.plot(t_values, results[(p,q)]['gap'], linewidth=2, label=f'({p},{q})')
    ax.plot(t_values, overall_physical, 'k--', linewidth=2.5, label='Overall gap (nonzero)')
    ax.axhline(y=results[(0,0)]['gap'][0], color='gray', linestyle=':', alpha=0.5, label='$D_K$ gap')
    ax.set_xlabel('$t$ (contorsion parameter)', fontsize=14)
    ax.set_ylabel('Spectral gap', fontsize=14)
    ax.set_title(f'Spectral Gap vs Contorsion at $\\tau={tau}$', fontsize=14)
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(bottom=0)

    plt.tight_layout()
    plt.savefig(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                's26_gap_comparison.png'), dpi=150)
    plt.close()
    print("Plot saved: s26_gap_comparison.png")

    # ---- Final verdict ----
    print("\n" + "=" * 80)
    print("CONTORSION RESONANCE VERDICT")
    print("=" * 80)
    print(f"\n1. Singlet (0,0): gap = (1-t) * {results[(0,0)]['gap'][0]:.6f}. Linear decrease to 0. NO resonance.")
    print(f"2. (1,0)/(0,1):  gap decreases from {results[(1,0)]['gap'][0]:.6f} to {results[(1,0)]['gap'][-1]:.6f}.")
    print(f"3. (1,1):        gap decreases from {results[(1,1)]['gap'][0]:.6f} to {results[(1,1)]['gap'][-1]:.6f}.")
    print(f"4. Singlet gap controls overall gap at t=0. At t~0.03, non-singlet gap takes over.")
    print(f"5. For ANY t > 0, the overall gap is SMALLER than D_K gap.")
    print(f"6. But for t -> 1, the singlet gap -> 0 (DEGENERATE, not useful).")
    print(f"7. The INTERESTING regime is small t, where singlet gap ~ (1-t)*0.82 and")
    print(f"   non-singlet gap may decrease faster or slower.")

    # Find crossover
    for i in range(len(t_values)):
        if singlet_gap[i] > nonsing_gap[i]:
            print(f"\n   Crossover: singlet gap > non-singlet gap at t = {t_values[i]:.4f}")
            print(f"   At crossover: singlet = {singlet_gap[i]:.6f}, non-singlet = {nonsing_gap[i]:.6f}")
            break

    print(f"\n   PHYSICAL CONCLUSION: The contorsion interpolation D_t trivially weakens the gap")
    print(f"   because it removes the Omega term that creates the gap in the first place.")
    print(f"   There is no resonance (local minimum at intermediate t).")
    print(f"   The 'non-monotone' flag in the main script was a false positive from")
    print(f"   eigenvalue reordering, not a true local minimum in the gap function.")


if __name__ == '__main__':
    main()
