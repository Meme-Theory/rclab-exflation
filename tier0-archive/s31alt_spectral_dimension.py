"""
BA-31-1: Spectral Dimension Flow d_s(E) on Jensen-Deformed SU(3)
================================================================

Computes the effective spectral dimension via the return probability:
  P(t) = Sum_n exp(-t * lambda_n^2)
  d_s(t) = -2 * d(log P) / d(log t)

where lambda_n are the eigenvalues of D_K (purely imaginary; we use |lambda_n|).

UV limit (t->0): d_s -> 8 (Weyl's law, internal SU(3) dimension).
IR limit (t->inf): d_s -> 0 (gapped spectrum, exponential decay).
Intermediate: may show non-trivial flow (distinguishing prediction).

Gate BA-31-ds:
  DISTINGUISH if d_s(t = lambda_min^{-2}) < 7.2
  GENERIC if d_s = 8 everywhere above gap scale

Author: sim (phonon-exflation-sim), Session 31Aa
Date: 2026-03-02
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sys
import os
import time

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))

from tier1_dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    build_cliff8, collect_spectrum
)

# ============================================================================
# 1. Collect full eigenvalue spectra at 4 tau values
# ============================================================================

def collect_all_eigenvalues(tau, gens, f_abc, gammas, max_pq_sum=6):
    """
    Collect ALL eigenvalues (with Peter-Weyl multiplicities) at given tau.

    Returns:
        abs_evals: sorted array of |lambda| values (with PW multiplicity expanded)
        n_distinct: number of distinct eigenvalue magnitudes
        n_total: total count with multiplicities
    """
    all_evals, eval_data = collect_spectrum(tau, gens, f_abc, gammas,
                                            max_pq_sum=max_pq_sum, verbose=False)

    # all_evals is list of (complex_eigenvalue, PW_multiplicity)
    # Expand with multiplicities for return probability
    abs_list = []
    for ev, mult in all_evals:
        lam = np.abs(ev)
        # Each eigenvalue appears mult times in the full L^2 spectrum
        for _ in range(mult):
            abs_list.append(lam)

    abs_evals = np.sort(np.array(abs_list))
    n_distinct = len(eval_data)

    return abs_evals, n_distinct, len(abs_evals), eval_data


def compute_return_probability(abs_evals_sq, t_values):
    """
    Compute P(t) = Sum_n exp(-t * lambda_n^2).

    Uses lambda_n^2 (pre-squared) for efficiency.

    Args:
        abs_evals_sq: array of lambda_n^2 values (with multiplicities)
        t_values: array of diffusion times

    Returns:
        P: array of P(t) values
    """
    # Vectorized: P(t) = sum_n exp(-t * lam_n^2)
    # Shape: (len(t), len(evals)) -> sum over evals axis
    P = np.zeros(len(t_values))
    for i, t in enumerate(t_values):
        exponents = -t * abs_evals_sq
        # Clip to avoid underflow issues
        P[i] = np.sum(np.exp(np.clip(exponents, -700, 0)))
    return P


def compute_spectral_dimension(log_t, log_P):
    """
    Compute d_s(t) = -2 * d(log P)/d(log t) via central finite differences.

    Returns d_s at interior points (len - 2).
    """
    dt = np.diff(log_t)
    dP = np.diff(log_P)

    # Central differences at interior points
    d_s = np.zeros(len(log_t) - 2)
    for i in range(len(d_s)):
        # Average of forward and backward differences
        slope = (log_P[i+2] - log_P[i]) / (log_t[i+2] - log_t[i])
        d_s[i] = -2.0 * slope

    return d_s


def main():
    t_start = time.time()

    print("=" * 70)
    print("BA-31-1: SPECTRAL DIMENSION FLOW d_s(E)")
    print("=" * 70)

    # Initialize infrastructure
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    gammas = build_cliff8()

    tau_values = [0.0, 0.15, 0.21, 0.50]
    N_max = 6

    # Diffusion time range
    n_t = 200
    t_values = np.logspace(-4, 4, n_t)
    log_t = np.log(t_values)

    # Storage
    results = {}

    for tau in tau_values:
        print(f"\n--- tau = {tau:.2f}, N_max = {N_max} ---")
        t0 = time.time()

        abs_evals, n_sectors, n_total, eval_data = collect_all_eigenvalues(
            tau, gens, f_abc, gammas, max_pq_sum=N_max
        )

        dt_comp = time.time() - t0
        print(f"  Eigenvalues: {n_total} total (with PW multiplicities)")
        print(f"  |lambda| range: [{abs_evals[0]:.6f}, {abs_evals[-1]:.4f}]")
        print(f"  lambda_min = {abs_evals[abs_evals > 1e-10].min() if np.any(abs_evals > 1e-10) else 0:.6f}")
        print(f"  Compute time: {dt_comp:.1f}s")

        # Compute return probability
        abs_evals_sq = abs_evals**2
        P = compute_return_probability(abs_evals_sq, t_values)

        # Avoid log(0) -- P should always be > 0 if there are any eigenvalues
        mask = P > 0
        log_P = np.full(n_t, np.nan)
        log_P[mask] = np.log(P[mask])

        # Spectral dimension via finite differences (at interior points)
        # Use only points where P > 0
        valid = np.isfinite(log_P)
        d_s_full = np.full(n_t, np.nan)

        if np.sum(valid) > 2:
            # Find contiguous valid region
            valid_idx = np.where(valid)[0]
            # Compute d_s at interior valid points
            for k in range(1, len(valid_idx) - 1):
                i_prev = valid_idx[k-1]
                i_curr = valid_idx[k]
                i_next = valid_idx[k+1]
                slope = (log_P[i_next] - log_P[i_prev]) / (log_t[i_next] - log_t[i_prev])
                d_s_full[i_curr] = -2.0 * slope

        # Key diagnostics
        lambda_min_nonzero = abs_evals[abs_evals > 1e-10].min() if np.any(abs_evals > 1e-10) else np.inf
        t_gap = 1.0 / lambda_min_nonzero**2 if lambda_min_nonzero < np.inf else np.inf

        # Find d_s at the gap scale
        if t_gap < t_values[-1]:
            idx_gap = np.argmin(np.abs(t_values - t_gap))
            ds_at_gap = d_s_full[idx_gap] if np.isfinite(d_s_full[idx_gap]) else np.nan
        else:
            idx_gap = -1
            ds_at_gap = np.nan

        # UV limit: d_s at smallest t
        ds_uv = d_s_full[np.isfinite(d_s_full)][0] if np.any(np.isfinite(d_s_full)) else np.nan

        # Find d_s at t=0.01 (deep UV)
        idx_uv = np.argmin(np.abs(t_values - 0.01))
        ds_at_001 = d_s_full[idx_uv] if np.isfinite(d_s_full[idx_uv]) else np.nan

        # Find any intermediate plateaus (look for regions where dd_s/d(log t) ~ 0)
        finite_ds = d_s_full[np.isfinite(d_s_full)]

        print(f"  lambda_min (nonzero) = {lambda_min_nonzero:.6f}")
        print(f"  t_gap = 1/lambda_min^2 = {t_gap:.4f}")
        print(f"  d_s(t=0.01) = {ds_at_001:.4f}")
        print(f"  d_s(t=t_gap) = {ds_at_gap:.4f}")
        print(f"  d_s UV (smallest t) = {ds_uv:.4f}")
        print(f"  d_s range: [{np.nanmin(d_s_full):.4f}, {np.nanmax(d_s_full):.4f}]")

        results[tau] = {
            'abs_evals': abs_evals,
            'P': P,
            'log_P': log_P,
            'd_s': d_s_full,
            'lambda_min': lambda_min_nonzero,
            't_gap': t_gap,
            'ds_at_gap': ds_at_gap,
            'ds_uv': ds_uv,
            'n_total': n_total,
        }

    # ========================================================================
    # 2. Gate verdict
    # ========================================================================
    print("\n" + "=" * 70)
    print("GATE BA-31-ds ASSESSMENT")
    print("=" * 70)

    gate_results = {}
    for tau in tau_values:
        r = results[tau]
        ds_gap = r['ds_at_gap']
        print(f"  tau={tau:.2f}: d_s(t=lambda_min^{{-2}}) = {ds_gap:.4f}  "
              f"[threshold: 7.2 for DISTINGUISH]")
        gate_results[tau] = ds_gap

    # Check if ANY tau shows d_s < 7.2 at gap scale
    distinguish = any(v < 7.2 for v in gate_results.values() if np.isfinite(v))

    if distinguish:
        verdict = "DISTINGUISH"
        print(f"\n  --> BA-31-ds: {verdict}")
        print(f"      d_s shows non-trivial UV modification at the gap scale.")
    else:
        verdict = "GENERIC"
        print(f"\n  --> BA-31-ds: {verdict}")
        print(f"      d_s = 8 (Weyl behavior) at all tested tau above gap.")

    # ========================================================================
    # 3. Total spectral dimension with CDT M4 component
    # ========================================================================
    print("\n--- Total d_s = d_s^M4(CDT) + d_s^K ---")
    # CDT model: d_s^M4 = 4 at large t, transitions to ~2 at small t
    # Parameterize as d_s^M4(t) = 2 + 2/(1 + (t_Planck/t)^alpha)
    # with t_Planck ~ 1 (in Planck units), alpha ~ 1
    # For display only:
    t_Planck = 1.0  # in units of internal geometry
    alpha_cdt = 1.0
    ds_M4_cdt = 2.0 + 2.0 / (1.0 + (t_Planck / t_values)**alpha_cdt)

    for tau in tau_values:
        r = results[tau]
        ds_total = ds_M4_cdt + r['d_s']  # where both are defined
        results[tau]['ds_total'] = ds_total
        results[tau]['ds_M4'] = ds_M4_cdt

        # Report total at gap scale
        if np.isfinite(r['ds_at_gap']):
            idx_gap = np.argmin(np.abs(t_values - r['t_gap']))
            ds_total_gap = ds_M4_cdt[idx_gap] + r['ds_at_gap']
            print(f"  tau={tau:.2f}: d_s^total(t_gap) = {ds_total_gap:.2f} "
                  f"= {ds_M4_cdt[idx_gap]:.2f} (M4) + {r['ds_at_gap']:.2f} (K)")

    # ========================================================================
    # 4. Save results
    # ========================================================================
    save_dict = {
        'tau_values': np.array(tau_values),
        't_values': t_values,
        'log_t': log_t,
        'ds_M4_cdt': ds_M4_cdt,
        'verdict': np.array(verdict),
    }

    for tau in tau_values:
        r = results[tau]
        prefix = f'tau_{tau:.2f}_'.replace('.', 'p')
        save_dict[prefix + 'abs_evals'] = r['abs_evals']
        save_dict[prefix + 'P'] = r['P']
        save_dict[prefix + 'log_P'] = r['log_P']
        save_dict[prefix + 'd_s'] = r['d_s']
        save_dict[prefix + 'ds_total'] = r['ds_total']
        save_dict[prefix + 'lambda_min'] = np.array(r['lambda_min'])
        save_dict[prefix + 't_gap'] = np.array(r['t_gap'])
        save_dict[prefix + 'ds_at_gap'] = np.array(r['ds_at_gap'])
        save_dict[prefix + 'n_total'] = np.array(r['n_total'])

    np.savez('tier0-computation/s31alt_spectral_dimension.npz', **save_dict)
    print(f"\nSaved: tier0-computation/s31alt_spectral_dimension.npz")

    # ========================================================================
    # 5. Plot
    # ========================================================================
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']

    # Panel (a): Return probability P(t)
    ax = axes[0, 0]
    for i, tau in enumerate(tau_values):
        r = results[tau]
        mask = r['P'] > 0
        ax.semilogy(t_values[mask], r['P'][mask], color=colors[i],
                    label=f'tau={tau:.2f}')
    ax.set_xlabel('Diffusion time t')
    ax.set_ylabel('P(t)')
    ax.set_xscale('log')
    ax.set_title('(a) Return Probability P(t) = Tr exp(-t D_K^2)')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Panel (b): Spectral dimension d_s(t)
    ax = axes[0, 1]
    for i, tau in enumerate(tau_values):
        r = results[tau]
        valid = np.isfinite(r['d_s'])
        ax.semilogx(t_values[valid], r['d_s'][valid], color=colors[i],
                    label=f'tau={tau:.2f}', linewidth=1.5)
        # Mark gap scale
        if r['t_gap'] < t_values[-1]:
            ax.axvline(r['t_gap'], color=colors[i], linestyle=':', alpha=0.5)

    ax.axhline(8.0, color='gray', linestyle='--', alpha=0.5, label='d=8 (Weyl)')
    ax.axhline(7.2, color='red', linestyle='--', alpha=0.5, label='d=7.2 (threshold)')
    ax.set_xlabel('Diffusion time t')
    ax.set_ylabel('d_s(t)')
    ax.set_title('(b) Spectral Dimension d_s(t) on SU(3)')
    ax.set_ylim(-0.5, 10)
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel (c): Total spectral dimension d_s^total = d_s^M4 + d_s^K
    ax = axes[1, 0]
    ax.semilogx(t_values, ds_M4_cdt, 'k--', alpha=0.5, label='d_s^M4 (CDT)')
    for i, tau in enumerate(tau_values):
        r = results[tau]
        valid = np.isfinite(r['ds_total'])
        ax.semilogx(t_values[valid], r['ds_total'][valid], color=colors[i],
                    label=f'tau={tau:.2f} total', linewidth=1.5)

    ax.axhline(12.0, color='gray', linestyle='--', alpha=0.3, label='d=12 (IR)')
    ax.set_xlabel('Diffusion time t')
    ax.set_ylabel('d_s^total(t)')
    ax.set_title('(c) Total Spectral Dimension (CDT M4 + SU(3))')
    ax.set_ylim(-0.5, 14)
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel (d): Eigenvalue density histogram at tau=0.15
    ax = axes[1, 1]
    for i, tau in enumerate(tau_values):
        r = results[tau]
        evals = r['abs_evals']
        evals_nz = evals[evals > 1e-10]
        ax.hist(evals_nz, bins=50, alpha=0.4, color=colors[i],
                label=f'tau={tau:.2f} (N={len(evals_nz)})')
    ax.set_xlabel('|lambda|')
    ax.set_ylabel('Count (with PW multiplicity)')
    ax.set_title('(d) Eigenvalue Density')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('tier0-computation/s31alt_spectral_dimension.png', dpi=150)
    print(f"Saved: tier0-computation/s31alt_spectral_dimension.png")

    # ========================================================================
    # 6. Summary
    # ========================================================================
    elapsed = time.time() - t_start
    print(f"\nTotal runtime: {elapsed:.1f}s")
    print(f"\nGATE BA-31-ds: {verdict}")

    return verdict, results


if __name__ == '__main__':
    verdict, results = main()
