"""
SESSION 26: TORSION DIAGNOSTICS ON JENSEN-DEFORMED SU(3)
=========================================================

Four computations from Tesla-Resonance collab review (Sections 3.1-3.3, 5.4):

Computation 1 (Section 3.1): Schouten torsion norm |T^0(tau)|^2
  - Decomposed by subspace type (WW->W, WC->C, YC->C, CC->W, CC->Y)
  - Compare growth rate to R_K(tau)
  - Assess Gate T-2

Computation 2 (Section 3.2): Torsion decomposition ratio
  - T^{(3)} = totally antisymmetric part
  - T^{(rest)} = remainder
  - Ratio |T^{(rest)}|/|T^{(3)}| across tau in [0, 2.0]
  - Constraint Condition: ratio < 0.5 everywhere => P(PASS) = 4-8%

Computation 3 (Section 3.3): Resonance in contorsion parameter t
  - Decompose M_K = M_0 + M_Omega per sector
  - Eigenvalues of M_0 + (1-t)*M_Omega for t in [0,1]
  - Look for non-monotonic min|eigenvalue| vs t

Computation 4 (Section 5.4): Torsion-curvature balance
  - |T^0(tau)|^2 / R_K(tau) across [0, 0.5]
  - Predicted ~1 at tau ~ 0.30

Author: Tesla-Resonance
Date: 2026-02-22
Grounded in: Papers 06 (phononic crystals), 08 (Dirac cones), 09 (Landau),
             10 (Volovik), Baptista Papers 14-15
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys
import os

# Add tier0-computation to path
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
from tier1_dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    jensen_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients, spinor_connection_offset, build_cliff8,
    dirac_operator_on_irrep, get_irrep, _irrep_cache
)

OUTDIR = os.path.dirname(os.path.abspath(__file__))


# =============================================================================
# INFRASTRUCTURE: SUBSPACE CLASSIFICATION
# =============================================================================

U1_IDX = [7]           # u(1): lambda_8
SU2_IDX = [0, 1, 2]    # su(2): lambda_1, lambda_2, lambda_3
C2_IDX = [3, 4, 5, 6]  # C^2: lambda_4, lambda_5, lambda_6, lambda_7

def subspace_of(idx):
    """Return subspace label for generator index."""
    if idx in U1_IDX:
        return 'Y'
    elif idx in SU2_IDX:
        return 'W'
    elif idx in C2_IDX:
        return 'C'
    raise ValueError(f"Invalid index {idx}")


def compute_torsion_from_code(tau, gens, f_abc, gammas):
    """Compute the Schouten torsion T^0_{abc}(tau) numerically.

    The Schouten torsion equals the ON-frame structure constants ft[a,b,c].

    Returns:
        ft: (8,8,8) structure constants in g_tau-ONB = Schouten torsion
        Omega_mat: (16,16) the Omega spinor connection offset
        E: (8,8) orthonormal frame
    """
    B_ab = compute_killing_form(f_abc)
    g_s = jensen_metric(B_ab, tau)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Omega_mat = spinor_connection_offset(Gamma, gammas)
    return ft, Omega_mat, E


def compute_T3_and_Trest(ft):
    """Decompose Schouten torsion into totally antisymmetric and remainder.

    T^{(3)}_{abc} = (1/3)(T^0_{abc} + T^0_{bca} + T^0_{cab})
    T^{(rest)} = T^0 - T^{(3)}

    Returns:
        T3: (8,8,8) totally antisymmetric part
        Trest: (8,8,8) remainder
    """
    n = ft.shape[0]
    T3 = np.zeros((n, n, n))
    for a in range(n):
        for b in range(n):
            for c in range(n):
                T3[a, b, c] = (ft[a, b, c] + ft[b, c, a] + ft[c, a, b]) / 3.0
    Trest = ft - T3
    return T3, Trest


def torsion_norm_squared(T):
    """Compute |T|^2 = sum_{a,b,c} T_{abc}^2 (unrestricted sum)."""
    return np.sum(T**2)


# =============================================================================
# COMPUTATION 1: |T^0(tau)|^2 DECOMPOSED BY SUBSPACE TYPE
# =============================================================================

def computation_1(tau_values, gens, f_abc, gammas):
    """Compute |T^0(tau)|^2 and decompose by bracket type."""
    print("\n" + "="*70)
    print("COMPUTATION 1: Schouten Torsion Norm |T^0(tau)|^2")
    print("="*70)

    types = ['(W,W)->W', '(W,C)->C', '(Y,C)->C', '(C,C)->W', '(C,C)->Y', 'other']

    results = {
        'tau': tau_values,
        'T0_norm2': np.zeros(len(tau_values)),
        'T3_norm2': np.zeros(len(tau_values)),
        'Trest_norm2': np.zeros(len(tau_values)),
        'by_type': {t: np.zeros(len(tau_values)) for t in types},
    }

    for i, tau in enumerate(tau_values):
        ft, _, _ = compute_torsion_from_code(tau, gens, f_abc, gammas)
        T3, Trest = compute_T3_and_Trest(ft)

        results['T0_norm2'][i] = torsion_norm_squared(ft)
        results['T3_norm2'][i] = torsion_norm_squared(T3)
        results['Trest_norm2'][i] = torsion_norm_squared(Trest)

        # Decompose by bracket type
        for a in range(8):
            for b in range(8):
                for c in range(8):
                    val2 = ft[a, b, c]**2
                    if abs(val2) < 1e-30:
                        continue
                    sa, sb, sc = subspace_of(a), subspace_of(b), subspace_of(c)
                    pair = tuple(sorted([sa, sb]))

                    if pair == ('W', 'W') and sc == 'W':
                        results['by_type']['(W,W)->W'][i] += val2
                    elif pair == ('C', 'W') and sc == 'C':
                        results['by_type']['(W,C)->C'][i] += val2
                    elif pair == ('C', 'Y') and sc == 'C':
                        results['by_type']['(Y,C)->C'][i] += val2
                    elif pair == ('C', 'C') and sc == 'W':
                        results['by_type']['(C,C)->W'][i] += val2
                    elif pair == ('C', 'C') and sc == 'Y':
                        results['by_type']['(C,C)->Y'][i] += val2
                    else:
                        results['by_type']['other'][i] += val2

        if abs(tau) < 1e-10 or abs(tau-0.25) < 1e-10 or abs(tau-0.50) < 1e-10 or abs(tau-1.0) < 1e-10 or abs(tau-2.0) < 1e-10:
            print(f"\n  tau = {tau:.2f}:")
            print(f"    |T^0|^2 = {results['T0_norm2'][i]:.6f}")
            print(f"    |T^(3)|^2 = {results['T3_norm2'][i]:.6f}")
            print(f"    |T^(rest)|^2 = {results['Trest_norm2'][i]:.6f}")
            for t in types:
                if results['by_type'][t][i] > 1e-10:
                    pct = 100*results['by_type'][t][i]/max(results['T0_norm2'][i], 1e-30)
                    print(f"    {t}: {results['by_type'][t][i]:.6f} ({pct:.1f}%)")

    return results


# =============================================================================
# COMPUTATION 2: TORSION DECOMPOSITION RATIO
# =============================================================================

def computation_2(tau_values, gens, f_abc, gammas):
    """Compute |T^{(rest)}| / |T^{(3)}| across tau range.

    Constraint Condition: ratio < 0.5 everywhere => P(PASS) = 4-8%
    """
    print("\n" + "="*70)
    print("COMPUTATION 2: Torsion Decomposition Ratio |T^(rest)|/|T^(3)|")
    print("="*70)

    ratios = np.zeros(len(tau_values))
    T3_norms = np.zeros(len(tau_values))
    Trest_norms = np.zeros(len(tau_values))

    for i, tau in enumerate(tau_values):
        ft, _, _ = compute_torsion_from_code(tau, gens, f_abc, gammas)
        T3, Trest = compute_T3_and_Trest(ft)

        T3_norm = np.sqrt(torsion_norm_squared(T3))
        Trest_norm = np.sqrt(torsion_norm_squared(Trest))
        T3_norms[i] = T3_norm
        Trest_norms[i] = Trest_norm

        if T3_norm > 1e-15:
            ratios[i] = Trest_norm / T3_norm
        else:
            ratios[i] = 0.0

    # Print key values
    print(f"\n  {'tau':>6s}  {'|T^(3)|':>10s}  {'|T^(rest)|':>10s}  {'ratio':>8s}")
    print(f"  {'-'*6}  {'-'*10}  {'-'*10}  {'-'*8}")
    for i, tau in enumerate(tau_values):
        if tau <= 0.55 or abs(tau - 1.0) < 0.01 or abs(tau - 1.5) < 0.01 or abs(tau - 2.0) < 0.01:
            print(f"  {tau:6.3f}  {T3_norms[i]:10.6f}  {Trest_norms[i]:10.6f}  {ratios[i]:8.5f}")

    max_ratio = np.max(ratios)
    argmax_tau = tau_values[np.argmax(ratios)]
    print(f"\n  Max ratio: {max_ratio:.5f} at tau = {argmax_tau:.3f}")

    if max_ratio < 0.5:
        print(f"  Constraint Condition MET: ratio < 0.5 everywhere => P(PASS) = 4-8%")
        print(f"  Perturbative estimate holds: max correction ~ ratio^2 = {max_ratio**2:.5f}")
    elif max_ratio < 1.0:
        print(f"  INTERMEDIATE: ratio in [0.5, 1.0). Perturbative estimate marginal.")
    else:
        print(f"  PASSES: ratio >= 1.0. Non-antisymmetric torsion dominates.")

    return ratios, T3_norms, Trest_norms


# =============================================================================
# COMPUTATION 3: RESONANCE IN CONTORSION PARAMETER t
# =============================================================================

def computation_3(tau_fixed, gens, f_abc, gammas, sectors=None, n_t=200):
    """For given sectors at fixed tau, interpolate D(t) = M_0 + (1-t)*M_Omega.

    At t=0: D_K (Levi-Civita Dirac operator)
    At t=1: D_0 (Schouten Dirac operator, Lie derivative only)
    """
    if sectors is None:
        sectors = [(1, 0), (0, 1), (1, 1), (0, 0)]

    print(f"\n" + "="*70)
    print(f"COMPUTATION 3: Resonance in Contorsion Parameter t (tau={tau_fixed})")
    print("="*70)

    B_ab = compute_killing_form(f_abc)
    g_s = jensen_metric(B_ab, tau_fixed)
    E = orthonormal_frame(g_s)
    ft = frame_structure_constants(f_abc, E)
    Gamma = connection_coefficients(ft)
    Omega_mat = spinor_connection_offset(Gamma, gammas)

    t_values = np.linspace(0, 1, n_t + 1)
    sector_results = {}

    for (p, q) in sectors:
        _irrep_cache.clear()
        rho, dim_rho = get_irrep(p, q, gens, f_abc)
        dim_spin = 16
        dim_total = dim_rho * dim_spin

        # Build M_0 (Lie derivative part only)
        M_0 = np.zeros((dim_total, dim_total), dtype=complex)
        for a in range(8):
            for b in range(8):
                if abs(E[a, b]) > 1e-15:
                    M_0 += E[a, b] * np.kron(rho[b], gammas[a])

        # Build M_Omega (spinor connection offset)
        M_Omega = np.kron(np.eye(dim_rho), Omega_mat)

        # Verify reconstruction
        D_K_full = dirac_operator_on_irrep(rho, E, gammas, Omega_mat)
        reconstruct_err = np.max(np.abs(D_K_full - (M_0 + M_Omega)))

        # Sweep t
        min_abs_evals = np.zeros(len(t_values))
        all_evals_at_t = []

        for j, t in enumerate(t_values):
            D_t = M_0 + (1.0 - t) * M_Omega
            evals = np.linalg.eigvals(D_t)
            evals_imag = np.sort(np.abs(evals.imag))
            min_abs_evals[j] = evals_imag[0] if len(evals_imag) > 0 else 0.0
            all_evals_at_t.append(evals_imag)

        gap_at_0 = min_abs_evals[0]
        gap_at_1 = min_abs_evals[-1]

        # Find genuine local minima (not monotone decrease toward zero)
        local_mins = []
        for j in range(1, len(min_abs_evals) - 1):
            if (min_abs_evals[j] < min_abs_evals[j-1] - 1e-12 and
                min_abs_evals[j] < min_abs_evals[j+1] - 1e-12 and
                min_abs_evals[j] > 1e-10):
                local_mins.append((t_values[j], min_abs_evals[j]))

        interior_min_val = np.min(min_abs_evals[1:-1]) if len(min_abs_evals) > 2 else gap_at_0
        interior_min_t = t_values[1 + np.argmin(min_abs_evals[1:-1])] if len(min_abs_evals) > 2 else 0.0

        sector_results[(p, q)] = {
            't': t_values,
            'min_abs_evals': min_abs_evals,
            'gap_at_0': gap_at_0,
            'gap_at_1': gap_at_1,
            'local_mins': local_mins,
            'interior_min': (interior_min_t, interior_min_val),
            'reconstruct_err': reconstruct_err,
            'all_evals_at_t': all_evals_at_t,
        }

        print(f"\n  Sector ({p},{q}), dim={dim_rho}x16={dim_total}:")
        print(f"    Reconstruction err: {reconstruct_err:.2e}")
        print(f"    Gap at t=0 (D_K): {gap_at_0:.6f}")
        print(f"    Gap at t=1 (D_0): {gap_at_1:.6f}")
        if local_mins:
            for t_min, val_min in local_mins:
                print(f"    LOCAL MINIMUM at t={t_min:.4f}: min|eval| = {val_min:.6f}")
                print(f"    ** RESONANCE DETECTED **")
        else:
            print(f"    No local minimum found (monotonic or simple decrease)")
        print(f"    Interior min = {interior_min_val:.6f} at t = {interior_min_t:.4f}")

    return sector_results


# =============================================================================
# COMPUTATION 4: TORSION-CURVATURE BALANCE
# =============================================================================

def computation_4(tau_values, gens, f_abc, gammas):
    """Compute |T^0(tau)|^2 / R_K(tau)."""
    print("\n" + "="*70)
    print("COMPUTATION 4: Torsion-Curvature Balance |T^0|^2 / R_K")
    print("="*70)

    data_path = os.path.join(OUTDIR, 's25_baptista_results.npz')
    if os.path.exists(data_path):
        d = np.load(data_path)
        tau_fine = d['tau_fine']
        R_K_fine = d['R_K_fine']
        print(f"  Loaded R_K from {data_path}")
    else:
        tau_fine = None
        R_K_fine = None
        print(f"  WARNING: {data_path} not found.")

    T0_norm2 = np.zeros(len(tau_values))
    R_K_interp = np.zeros(len(tau_values))
    ratio = np.zeros(len(tau_values))

    for i, tau in enumerate(tau_values):
        ft, _, _ = compute_torsion_from_code(tau, gens, f_abc, gammas)
        T0_norm2[i] = torsion_norm_squared(ft)

        if tau_fine is not None:
            R_K_interp[i] = np.interp(tau, tau_fine, R_K_fine)
        else:
            # Fallback: analytical (Baptista normalization / 6)
            R_K_interp[i] = 0.25 * (2*np.exp(2*tau) - 1 + 8*np.exp(-tau) - np.exp(-4*tau))

        if R_K_interp[i] > 1e-15:
            ratio[i] = T0_norm2[i] / R_K_interp[i]

    print(f"\n  {'tau':>6s}  {'|T^0|^2':>10s}  {'R_K':>10s}  {'ratio':>8s}")
    print(f"  {'-'*6}  {'-'*10}  {'-'*10}  {'-'*8}")
    for i, tau in enumerate(tau_values):
        if tau <= 0.55 or abs(tau - 1.0) < 0.01 or abs(tau - 1.5) < 0.01 or abs(tau - 2.0) < 0.01:
            print(f"  {tau:6.3f}  {T0_norm2[i]:10.4f}  {R_K_interp[i]:10.4f}  {ratio[i]:8.4f}")

    # Find ratio=1 crossings
    crossings = []
    for i in range(len(ratio) - 1):
        if (ratio[i] - 1.0) * (ratio[i+1] - 1.0) < 0:
            t_cross = tau_values[i] + (1.0 - ratio[i]) / (ratio[i+1] - ratio[i]) * (tau_values[i+1] - tau_values[i])
            crossings.append(t_cross)

    if crossings:
        print(f"\n  |T^0|^2 / R_K = 1 crossings at tau = {[f'{c:.4f}' for c in crossings]}")
    else:
        print(f"\n  No crossing at ratio = 1 in [{tau_values[0]:.2f}, {tau_values[-1]:.2f}]")
        closest = np.argmin(np.abs(ratio - 1.0))
        print(f"  Closest: ratio = {ratio[closest]:.4f} at tau = {tau_values[closest]:.3f}")

    return T0_norm2, R_K_interp, ratio


# =============================================================================
# PLOTTING
# =============================================================================

def plot_computation_1(tau_values, results):
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    ax = axes[0]
    ax.semilogy(tau_values, results['T0_norm2'], 'k-', lw=2, label='$|T^0|^2$ (total)')
    ax.semilogy(tau_values, results['T3_norm2'], 'b--', lw=2, label='$|T^{(3)}|^2$ (antisym)')
    mask_rest = results['Trest_norm2'] > 1e-20
    ax.semilogy(tau_values[mask_rest], results['Trest_norm2'][mask_rest],
                'r:', lw=2, label='$|T^{(rest)}|^2$ (remainder)')
    ax.set_xlabel(r'$\tau$', fontsize=13)
    ax.set_ylabel('Torsion norm squared', fontsize=13)
    ax.set_title('Schouten Torsion Decomposition', fontsize=14)
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)

    ax = axes[1]
    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd']
    type_labels = ['(W,W)->W', '(W,C)->C', '(Y,C)->C', '(C,C)->W', '(C,C)->Y']
    for j, t in enumerate(type_labels):
        vals = results['by_type'][t]
        mask = vals > 1e-20
        if np.any(mask):
            ax.semilogy(tau_values[mask], vals[mask], color=colors[j], lw=2, label=t)
    ax.set_xlabel(r'$\tau$', fontsize=13)
    ax.set_ylabel('$|T^0|^2$ contribution', fontsize=13)
    ax.set_title('Torsion by Bracket Type', fontsize=14)
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    outpath = os.path.join(OUTDIR, 's26_torsion_norms.png')
    plt.savefig(outpath, dpi=150)
    plt.close()
    print(f"\n  Plot saved: {outpath}")


def plot_computation_2(tau_values, ratios, T3_norms, Trest_norms):
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    ax = axes[0]
    ax.plot(tau_values, ratios, 'r-', lw=2)
    ax.axhline(y=0.5, color='gray', ls='--', lw=1, label='CLOSURE threshold (0.5)')
    ax.axhline(y=1.0, color='orange', ls='--', lw=1, label='Dominance threshold (1.0)')
    ax.set_xlabel(r'$\tau$', fontsize=13)
    ax.set_ylabel(r'$|T^{(\mathrm{rest})}| / |T^{(3)}|$', fontsize=13)
    ax.set_title('Torsion Decomposition Ratio', fontsize=14)
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)
    ax.set_xlim([0, 2.0])

    ax = axes[1]
    ax.plot(tau_values, T3_norms, 'b-', lw=2, label=r'$|T^{(3)}|$')
    ax.plot(tau_values, Trest_norms, 'r--', lw=2, label=r'$|T^{(\mathrm{rest})}|$')
    ax.set_xlabel(r'$\tau$', fontsize=13)
    ax.set_ylabel('Torsion norm', fontsize=13)
    ax.set_title('Antisymmetric vs Remainder Norms', fontsize=14)
    ax.legend(fontsize=11)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    outpath = os.path.join(OUTDIR, 's26_torsion_ratio.png')
    plt.savefig(outpath, dpi=150)
    plt.close()
    print(f"  Plot saved: {outpath}")


def plot_computation_3(tau_fixed, sector_results):
    n_sectors = len(sector_results)
    fig, axes = plt.subplots(1, min(n_sectors, 4), figsize=(5*min(n_sectors, 4), 5))
    if n_sectors == 1:
        axes = [axes]

    for idx, ((p, q), res) in enumerate(sector_results.items()):
        if idx >= 4:
            break
        ax = axes[idx]
        ax.plot(res['t'], res['min_abs_evals'], 'b-', lw=2)
        ax.axhline(y=res['gap_at_0'], color='green', ls=':', lw=1, alpha=0.5,
                   label=f'$D_K$ gap = {res["gap_at_0"]:.4f}')

        for t_min, val_min in res['local_mins']:
            ax.plot(t_min, val_min, 'ro', ms=8, label=f'Resonance t={t_min:.3f}')

        ax.set_xlabel('t (contorsion parameter)', fontsize=12)
        ax.set_ylabel(r'$\min|\lambda|$', fontsize=12)
        ax.set_title(f'({p},{q}), $\\tau$={tau_fixed}', fontsize=13)
        ax.legend(fontsize=9)
        ax.grid(True, alpha=0.3)
        ax.set_xlim([0, 1])

    plt.tight_layout()
    outpath = os.path.join(OUTDIR, 's26_contorsion_resonance.png')
    plt.savefig(outpath, dpi=150)
    plt.close()
    print(f"  Plot saved: {outpath}")


def plot_computation_3_flow(tau_fixed, sector_results):
    """Plot lowest eigenvalue flows as function of t."""
    n_sectors = len(sector_results)
    fig, axes = plt.subplots(1, min(n_sectors, 4), figsize=(5*min(n_sectors, 4), 5))
    if n_sectors == 1:
        axes = [axes]

    for idx, ((p, q), res) in enumerate(sector_results.items()):
        if idx >= 4:
            break
        ax = axes[idx]
        t_vals = res['t']
        all_evals = res['all_evals_at_t']
        n_evals = len(all_evals[0])
        n_plot = min(20, n_evals)

        for k in range(n_plot):
            evals_k = np.array([all_evals[j][k] for j in range(len(t_vals))])
            alpha = 0.8 if k < 5 else 0.3
            lw = 1.5 if k < 5 else 0.5
            ax.plot(t_vals, evals_k, lw=lw, alpha=alpha)

        ax.set_xlabel('t', fontsize=12)
        ax.set_ylabel(r'$|\lambda|$ (sorted)', fontsize=12)
        ax.set_title(f'({p},{q}): eigenvalue flow', fontsize=13)
        ax.grid(True, alpha=0.3)

    plt.tight_layout()
    outpath = os.path.join(OUTDIR, 's26_eigenvalue_flow.png')
    plt.savefig(outpath, dpi=150)
    plt.close()
    print(f"  Plot saved: {outpath}")


def plot_computation_4(tau_values, T0_norm2, R_K, ratio):
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    ax = axes[0]
    ax.plot(tau_values, T0_norm2, 'r-', lw=2, label=r'$|T^0|^2$')
    ax.plot(tau_values, R_K, 'b-', lw=2, label=r'$R_K$')
    ax.set_xlabel(r'$\tau$', fontsize=13)
    ax.set_ylabel('Magnitude', fontsize=13)
    ax.set_title('Torsion vs Curvature', fontsize=14)
    ax.legend(fontsize=12)
    ax.grid(True, alpha=0.3)

    ax = axes[1]
    ax.plot(tau_values, ratio, 'k-', lw=2)
    ax.axhline(y=1.0, color='red', ls='--', lw=1, label='Balance (ratio = 1)')
    ax.set_xlabel(r'$\tau$', fontsize=13)
    ax.set_ylabel(r'$|T^0|^2 / R_K$', fontsize=13)
    ax.set_title('Torsion-Curvature Balance', fontsize=14)
    ax.legend(fontsize=12)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    outpath = os.path.join(OUTDIR, 's26_torsion_curvature_balance.png')
    plt.savefig(outpath, dpi=150)
    plt.close()
    print(f"  Plot saved: {outpath}")


# =============================================================================
# MAIN
# =============================================================================

def main():
    print("SESSION 26: TORSION DIAGNOSTICS ON JENSEN-DEFORMED SU(3)")
    print("="*70)
    print("Author: Tesla-Resonance")
    print("Date: 2026-02-22\n")

    # Initialize
    print("Initializing SU(3) Lie algebra infrastructure...")
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    gammas = build_cliff8()

    B_ab = compute_killing_form(f_abc)
    print(f"  Killing form diagonal: {np.diag(B_ab)}")
    print(f"  Killing form off-diag max: {np.max(np.abs(B_ab - np.diag(np.diag(B_ab)))):.2e}")

    f_antisym_err = np.max(np.abs(f_abc + np.transpose(f_abc, (1,0,2))))
    print(f"  f_abc antisymmetry (a,b) err: {f_antisym_err:.2e}")

    # Check total antisymmetry at tau=0
    ft0, _, _ = compute_torsion_from_code(0.0, gens, f_abc, gammas)
    ta_err = 0.0
    for a in range(8):
        for b in range(8):
            for c in range(8):
                ta_err = max(ta_err, abs(ft0[a,b,c] - ft0[b,c,a]))
    print(f"  Total antisymmetry of f_tilde at tau=0: {ta_err:.2e}")

    # Dense grid
    tau_dense = np.linspace(0.0, 2.0, 201)

    # =========================================================================
    # COMPUTATION 1
    # =========================================================================
    results_1 = computation_1(tau_dense, gens, f_abc, gammas)
    plot_computation_1(tau_dense, results_1)

    # =========================================================================
    # COMPUTATION 2
    # =========================================================================
    ratios, T3_norms, Trest_norms = computation_2(tau_dense, gens, f_abc, gammas)
    plot_computation_2(tau_dense, ratios, T3_norms, Trest_norms)

    # =========================================================================
    # COMPUTATION 4 (before 3)
    # =========================================================================
    tau_for_4 = np.linspace(0.0, 0.5, 101)
    T0_norm2_4, R_K_4, balance_ratio = computation_4(tau_for_4, gens, f_abc, gammas)
    plot_computation_4(tau_for_4, T0_norm2_4, R_K_4, balance_ratio)

    # =========================================================================
    # COMPUTATION 3 (most expensive -- sectors at tau=0.25)
    # =========================================================================
    sectors_to_test = [(0, 0), (1, 0), (0, 1), (1, 1)]
    tau_fixed = 0.25
    sector_results = computation_3(tau_fixed, gens, f_abc, gammas,
                                   sectors=sectors_to_test, n_t=200)
    plot_computation_3(tau_fixed, sector_results)
    plot_computation_3_flow(tau_fixed, sector_results)

    # Additional tau values
    print("\n  --- Computation 3 at tau=0.15, 0.50 ---")
    for tau_extra in [0.15, 0.50]:
        _irrep_cache.clear()
        sr_extra = computation_3(tau_extra, gens, f_abc, gammas,
                                 sectors=[(1, 0), (0, 1), (1, 1)], n_t=100)

    # =========================================================================
    # GATE VERDICTS
    # =========================================================================
    print("\n" + "="*70)
    print("GATE VERDICTS")
    print("="*70)

    # Gate T-2: Bosonic torsion stabilization
    print("\n  Gate T-2 (Bosonic torsion stabilization):")
    # Fit growth rate of |T^0|^2 on [0.5, 2.0]
    mask = tau_dense >= 0.5
    valid = results_1['T0_norm2'][mask] > 0
    growth_rate = 0.0
    if np.sum(valid) > 2:
        tau_fit = tau_dense[mask][valid]
        log_T0 = np.log(results_1['T0_norm2'][mask][valid])
        coeffs = np.polyfit(tau_fit, log_T0, 1)
        growth_rate = coeffs[0]
        print(f"    |T^0|^2 exponential growth rate (tau > 0.5): {growth_rate:.3f}")
        print(f"    Theoretical prediction: e^{{4*tau}} => rate ~ 4.0 for (C,C)->W dominance")

    if growth_rate > 2.5:
        print(f"    VERDICT: T-2 CLOSED.")
        print(f"    |T^0|^2 grows as ~e^{{{growth_rate:.1f}*tau}}, faster than R_K ~ e^{{2*tau}}.")
        print(f"    Torsion WORSENS bosonic potential runaway.")
        T2_verdict = "CLOSED"
    else:
        print(f"    Growth rate {growth_rate:.2f} -- T-2 OPEN.")
        T2_verdict = "OPEN"

    # Gate T-1 assessment
    print(f"\n  Gate T-1 assessment (from torsion ratio):")
    max_ratio = np.max(ratios)
    argmax = tau_dense[np.argmax(ratios)]
    print(f"    Max |T^(rest)|/|T^(3)| = {max_ratio:.5f} at tau = {argmax:.3f}")
    if max_ratio < 0.5:
        print(f"    ASSESSMENT: Perturbative regime. P(T-1 PASS) = 4-8%.")
        T1_assessment = "LIKELY CLOSED (4-8%)"
    elif max_ratio < 1.0:
        print(f"    ASSESSMENT: Marginally perturbative. P(T-1 PASS) = 8-12%.")
        T1_assessment = "MARGINAL (8-12%)"
    else:
        print(f"    ASSESSMENT: Non-perturbative. P(T-1 PASS) = 10-15%.")
        T1_assessment = "OPEN (10-15%)"

    # Resonance check
    print(f"\n  Computation 3 resonance summary (tau={tau_fixed}):")
    any_resonance = False
    for (p, q), res in sector_results.items():
        if res['local_mins']:
            any_resonance = True
            for t_min, val_min in res['local_mins']:
                print(f"    RESONANCE in ({p},{q}) at t={t_min:.4f}: "
                      f"min|eval| = {val_min:.6f}")
    if not any_resonance:
        print(f"    No resonance found in any sector.")

    # =========================================================================
    # SAVE
    # =========================================================================
    save_path = os.path.join(OUTDIR, 's26_torsion_diagnostics.npz')
    np.savez(save_path,
             tau_dense=tau_dense,
             T0_norm2=results_1['T0_norm2'],
             T3_norm2=results_1['T3_norm2'],
             Trest_norm2=results_1['Trest_norm2'],
             decomp_ratios=ratios,
             T3_norms=T3_norms,
             Trest_norms=Trest_norms,
             tau_balance=tau_for_4,
             balance_T0=T0_norm2_4,
             balance_RK=R_K_4,
             balance_ratio=balance_ratio,
             T2_growth_rate=np.array(growth_rate),
    )
    print(f"\n  Data saved: {save_path}")

    print("\n" + "="*70)
    print("SESSION 26 TORSION DIAGNOSTICS COMPLETE")
    print("="*70)


if __name__ == '__main__':
    main()
