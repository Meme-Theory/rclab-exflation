"""
TIER 1: SPECTRAL FREE ENERGY AND PHASE STRUCTURE (H-2)
======================================================

Assignment H-2 from Session 17c:
  Compute F(s, mu) = -sum_{(p,q)} dim(p,q) sum_j ln(|lambda_j^{(p,q)}(s)|^2 / mu^2)
  using Dirac eigenvalues from tier1_dirac_spectrum.py.

This is the spectral ZETA regularization approach (zeta'(0)), distinct from
the Coleman-Weinberg (lambda^4 * ln lambda) formula in H-1.

Physical interpretation (Hawking):
  F(s, mu) = Helmholtz free energy with s = order parameter, mu = temperature scale.
  Critical points dF/ds = 0 are entropy maxima.
  Phase transitions classified by specific heat singularity.

Key advantage over CW:
  ln(lambda^2) grows LOGARITHMICALLY vs lambda^4 in CW.
  UV convergence is dramatically better.
  The s-dependence should be more reliable.

Deliverables:
  1. Phase diagram in (s, mu) plane (heatmap/contour)
  2. Location and order of each phase transition
  3. Comparison to V_eff minimum from H-1

Author: Hawking-Theorist Agent (Session 17c)
Date: 2026-02-14

References:
  - Hawking (1977): Zeta function regularization (Commun. Math. Phys. 55)
  - Gibbons & Hawking (1977): Partition function and Euclidean path integral
  - Connes (1996): Spectral action = phonon free energy (identity, not analogy)
"""

import numpy as np
from scipy.optimize import minimize_scalar
from scipy.signal import argrelmin
import sys
import os
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from tier1_dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    build_cliff8, validate_clifford,
    jensen_metric, orthonormal_frame, frame_structure_constants,
    connection_coefficients, spinor_connection_offset,
    collect_spectrum,
)
from tier1_spectral_action import dim_su3_irrep


# =============================================================================
# MODULE 1: SPECTRAL FREE ENERGY F(s, mu)
# =============================================================================

def spectral_free_energy(eval_data, mu, include_zero=False):
    """
    Compute spectral free energy:

    F(s, mu) = -sum_{(p,q)} dim(p,q) * sum_j ln(|lambda_j^{(p,q)}(s)|^2 / mu^2)

    where the sum runs over ALL eigenvalues (both +/- signs counted).

    For |lambda_j| = 0 (zero modes): these contribute -infinity to F.
    Physical interpretation: zero modes are MASSLESS excitations,
    giving infinite degeneracy in the partition function.
    We handle them separately.

    Args:
        eval_data: list of (p, q, eigenvalues_array) from collect_spectrum
        mu: scale parameter (NOT squared)
        include_zero: if True, count zero modes separately

    Returns:
        F: free energy value
        n_zero: number of zero modes (weighted by dim(p,q))
        F_sectors: dict (p,q) -> sector contribution
    """
    mu_sq = mu**2
    F = 0.0
    n_zero = 0
    F_sectors = {}

    for p, q, evals in eval_data:
        d_pq = dim_su3_irrep(p, q)
        abs_evals = np.abs(evals)

        # Separate zero modes
        nonzero_mask = abs_evals > 1e-12
        n_z = d_pq * np.sum(~nonzero_mask)
        n_zero += n_z

        nonzero = abs_evals[nonzero_mask]
        if len(nonzero) == 0:
            F_sectors[(p, q)] = 0.0
            continue

        # F contribution: -dim(p,q) * sum ln(|lam|^2 / mu^2)
        sector_F = -d_pq * np.sum(np.log(nonzero**2 / mu_sq))
        F_sectors[(p, q)] = sector_F
        F += sector_F

    return F, n_zero, F_sectors


def spectral_entropy(eval_data, mu):
    """
    Spectral entropy S(s, mu) = -dF/dT where T is identified with mu.

    Since F = -sum dim * sum ln(|lam|^2/mu^2), we have:
      dF/dmu = -sum dim * sum d/dmu[-2 ln|lam| + 2 ln(mu)]
             = -sum dim * sum (2/mu)
             = -2 N_modes / mu

    where N_modes = sum dim(p,q) * n_eigenvalues(p,q) is the total mode count.

    This gives S = -dF/d(ln mu) = 2 * N_modes (CONSTANT in s).

    The INTERESTING entropy is the one from the BOLTZMANN-regulated free energy:
      F_B(s, mu, Lambda) = -sum dim * sum ln(|lam|^2/mu^2) * exp(-|lam|^2/Lambda^2)

    where the regulator introduces s-dependence into the entropy.

    Returns:
        S: entropy (mu-derivative)
        S_regulated: Boltzmann-regulated entropy (s-dependent)
    """
    N_modes = 0
    for p, q, evals in eval_data:
        d_pq = dim_su3_irrep(p, q)
        abs_evals = np.abs(evals)
        N_modes += d_pq * np.sum(abs_evals > 1e-12)

    S_trivial = 2 * N_modes  # s-independent

    return S_trivial, N_modes


def spectral_free_energy_regulated(eval_data, mu, Lambda, f_type='boltzmann'):
    """
    Regulated spectral free energy:

    F_reg(s, mu, Lambda) = -sum dim(p,q) * sum_j f(|lam_j|/Lambda) * ln(|lam_j|^2 / mu^2)

    where f is a regulator function:
      'boltzmann': f(x) = exp(-x^2)
      'lorentz':   f(x) = 1/(1+x^2)^2
      'sharp':     f(x) = theta(1 - x)  [sharp cutoff at Lambda]

    The regulator suppresses UV modes (|lam| >> Lambda), making the sum
    convergent AND introducing s-dependence into the mu-derivative (entropy).

    Args:
        eval_data: list of (p, q, eigenvalues_array)
        mu: scale parameter
        Lambda: UV cutoff
        f_type: regulator type

    Returns:
        F_reg: regulated free energy
        N_eff: effective mode count (weighted by regulator)
    """
    mu_sq = mu**2
    F_reg = 0.0
    N_eff = 0.0

    for p, q, evals in eval_data:
        d_pq = dim_su3_irrep(p, q)
        abs_evals = np.abs(evals)
        nonzero = abs_evals[abs_evals > 1e-12]

        if len(nonzero) == 0:
            continue

        x = nonzero / Lambda
        if f_type == 'boltzmann':
            w = np.exp(-x**2)
        elif f_type == 'lorentz':
            w = 1.0 / (1.0 + x**2)**2
        elif f_type == 'sharp':
            w = (x < 1.0).astype(float)
        else:
            raise ValueError(f"Unknown f_type: {f_type}")

        log_term = np.log(nonzero**2 / mu_sq)
        F_reg += -d_pq * np.sum(w * log_term)
        N_eff += d_pq * np.sum(w)

    return F_reg, N_eff


def specific_heat(eval_data, mu, Lambda, f_type='boltzmann'):
    """
    Specific heat C(s, mu) = -mu * d^2F/dmu^2

    For the regulated free energy:
      F = -sum dim * sum w(|lam|/Lambda) * ln(|lam|^2/mu^2)
      dF/dmu = sum dim * sum w * (2/mu) = 2 N_eff / mu
      d^2F/dmu^2 = -2 N_eff / mu^2

    => C = -mu * (-2 N_eff / mu^2) = 2 N_eff / mu

    This is POSITIVE (non-gravitational behavior) and proportional to N_eff(s).
    The interesting quantity is how C varies with s (proportional to N_eff(s)).

    For the PHYSICAL specific heat we need the SECOND derivative with
    respect to the physical temperature, which requires identifying mu with T.
    Here we compute the formal result.

    Returns:
        C_V: specific heat
        N_eff: effective mode count
    """
    _, N_eff = spectral_free_energy_regulated(eval_data, mu, Lambda, f_type)
    C_V = 2 * N_eff / mu
    return C_V, N_eff


# =============================================================================
# MODULE 2: PHASE DIAGRAM COMPUTATION
# =============================================================================

def compute_phase_diagram(gens, f_abc, gammas, max_pq_sum=6,
                          n_s=51, n_mu=41, n_Lambda=5,
                          s_range=(0.0, 2.5), mu_range=(0.1, 10.0),
                          Lambda_values=None,
                          verbose=True):
    """
    Compute the full phase diagram in the (s, mu) plane.

    For each (s, mu) pair:
      1. Unregulated F(s, mu)
      2. Boltzmann-regulated F(s, mu, Lambda) for several Lambda
      3. dF/ds (numerical gradient)

    Phase transitions occur where dF/ds = 0 and d^2F/ds^2 changes sign.

    Args:
        (standard parameter documentation)

    Returns:
        results: dict with all computed arrays
    """
    if Lambda_values is None:
        Lambda_values = [0.5, 1.0, 2.0, 5.0, 10.0]

    s_values = np.linspace(s_range[0], s_range[1], n_s)
    mu_values = np.logspace(np.log10(mu_range[0]), np.log10(mu_range[1]), n_mu)

    # Pre-compute eigenvalues at each s
    if verbose:
        print(f"\n{'='*70}")
        print(f"  H-2: SPECTRAL FREE ENERGY AND PHASE STRUCTURE")
        print(f"  {n_s} s-values x {n_mu} mu-values x {n_Lambda} Lambda-values")
        print(f"  max_pq_sum = {max_pq_sum}")
        print(f"{'='*70}\n")
        print(f"  Phase 1: Pre-computing Dirac eigenvalues at {n_s} s-values...")

    t0 = time.time()
    eval_cache = {}
    for i, s in enumerate(s_values):
        if verbose and (i % 10 == 0):
            elapsed = time.time() - t0
            rate = (i + 1) / max(elapsed, 0.01)
            eta = (n_s - i - 1) / max(rate, 0.01)
            print(f"    s={s:.3f} ({i+1}/{n_s}), elapsed={elapsed:.0f}s, ETA={eta:.0f}s",
                  flush=True)
        _, eval_data = collect_spectrum(
            s, gens, f_abc, gammas, max_pq_sum=max_pq_sum, verbose=False
        )
        eval_cache[i] = eval_data

    t_evals = time.time() - t0
    if verbose:
        print(f"  Eigenvalue pre-computation: {t_evals:.1f}s ({t_evals/n_s:.1f}s per s)\n")

    # Phase 2: Compute unregulated F(s, mu)
    if verbose:
        print(f"  Phase 2: Computing F(s, mu) on {n_s}x{n_mu} grid...")

    F_unreg = np.zeros((n_s, n_mu))
    n_zero_arr = np.zeros(n_s)

    for i in range(n_s):
        for j, mu in enumerate(mu_values):
            F_val, n_z, _ = spectral_free_energy(eval_cache[i], mu)
            F_unreg[i, j] = F_val
            if j == 0:
                n_zero_arr[i] = n_z

    if verbose:
        print(f"    Done. Zero modes: {n_zero_arr[0]:.0f} (s=0) to "
              f"{n_zero_arr[-1]:.0f} (s={s_values[-1]:.1f})")

    # Phase 3: Compute Boltzmann-regulated F(s, mu, Lambda)
    if verbose:
        print(f"  Phase 3: Computing F_reg(s, mu, Lambda) for {len(Lambda_values)} Lambda values...")

    F_boltz = {}
    N_eff_arr = {}
    for Lambda in Lambda_values:
        F_boltz[Lambda] = np.zeros((n_s, n_mu))
        N_eff_arr[Lambda] = np.zeros(n_s)

        for i in range(n_s):
            for j, mu in enumerate(mu_values):
                F_val, N_eff = spectral_free_energy_regulated(
                    eval_cache[i], mu, Lambda, f_type='boltzmann'
                )
                F_boltz[Lambda][i, j] = F_val
                if j == 0:
                    N_eff_arr[Lambda][i] = N_eff

        if verbose:
            print(f"    Lambda={Lambda:.1f}: N_eff range = "
                  f"[{np.min(N_eff_arr[Lambda]):.1f}, {np.max(N_eff_arr[Lambda]):.1f}]")

    # Phase 4: Compute dF/ds (numerical gradient) and find critical points
    if verbose:
        print(f"\n  Phase 4: Finding critical points dF/ds = 0...")

    ds = s_values[1] - s_values[0] if len(s_values) > 1 else 0.05
    critical_points = {}

    for Lambda in Lambda_values:
        # Pick a reference mu (middle of range)
        mu_ref_idx = n_mu // 2
        F_slice = F_boltz[Lambda][:, mu_ref_idx]

        # Numerical first derivative
        dF_ds = np.gradient(F_slice, ds)
        # Second derivative
        d2F_ds2 = np.gradient(dF_ds, ds)

        # Find sign changes in dF/ds (critical points)
        crits = []
        for k in range(len(dF_ds) - 1):
            if dF_ds[k] * dF_ds[k+1] < 0:
                # Linear interpolation for s_crit
                s_c = s_values[k] - dF_ds[k] * ds / (dF_ds[k+1] - dF_ds[k])
                # Second derivative at critical point (interpolated)
                d2F_c = d2F_ds2[k] + (d2F_ds2[k+1] - d2F_ds2[k]) * (s_c - s_values[k]) / ds
                crits.append({
                    's_c': s_c,
                    'F_c': np.interp(s_c, s_values, F_slice),
                    'd2F': d2F_c,
                    'type': 'minimum' if d2F_c > 0 else 'maximum',
                    'mu_ref': mu_values[mu_ref_idx],
                })

        critical_points[Lambda] = crits

        if verbose:
            if crits:
                for c in crits:
                    print(f"    Lambda={Lambda:.1f}: {c['type']} at s={c['s_c']:.4f}, "
                          f"F''={c['d2F']:.3e}")
            else:
                print(f"    Lambda={Lambda:.1f}: NO critical points (monotonic)")

    # Phase 5: Scan critical points across ALL mu values
    if verbose:
        print(f"\n  Phase 5: Scanning critical points across mu range...")

    crit_map = {}  # Lambda -> list of (mu, s_c, type)
    for Lambda in Lambda_values:
        crit_map[Lambda] = []
        for j, mu in enumerate(mu_values):
            F_slice = F_boltz[Lambda][:, j]
            dF_ds = np.gradient(F_slice, ds)

            for k in range(len(dF_ds) - 1):
                if dF_ds[k] * dF_ds[k+1] < 0:
                    s_c = s_values[k] - dF_ds[k] * ds / (dF_ds[k+1] - dF_ds[k])
                    d2F = np.gradient(np.gradient(F_slice, ds), ds)
                    d2F_c = np.interp(s_c, s_values, d2F)
                    crit_map[Lambda].append({
                        'mu': mu,
                        's_c': s_c,
                        'type': 'min' if d2F_c > 0 else 'max',
                    })

        if verbose:
            n_crits = len(crit_map[Lambda])
            if n_crits > 0:
                s_min = min(c['s_c'] for c in crit_map[Lambda])
                s_max = max(c['s_c'] for c in crit_map[Lambda])
                print(f"    Lambda={Lambda:.1f}: {n_crits} critical points, "
                      f"s_c range [{s_min:.3f}, {s_max:.3f}]")
            else:
                print(f"    Lambda={Lambda:.1f}: 0 critical points across all mu")

    # Phase 6: Specific heat
    if verbose:
        print(f"\n  Phase 6: Computing specific heat...")

    C_V = {}
    for Lambda in Lambda_values:
        C_V[Lambda] = np.zeros(n_s)
        for i in range(n_s):
            mu_ref = mu_values[n_mu // 2]
            cv, _ = specific_heat(eval_cache[i], mu_ref, Lambda)
            C_V[Lambda][i] = cv

    # Phase 7: Comparison to H-1 V_eff minimum
    if verbose:
        print(f"\n  Phase 7: Comparison to H-1 results...")
        print(f"    H-1 Boltzmann minimum: s_min = 0.164 at Lambda_UV ~ 1.23")
        print(f"    H-1 second Boltzmann min: s_min = 0.481 at Lambda_UV = 1.43")
        print(f"    H-2 critical points at Lambda = 1.0:")
        if 1.0 in critical_points and critical_points[1.0]:
            for c in critical_points[1.0]:
                print(f"      {c['type']} at s = {c['s_c']:.4f}")
        else:
            print(f"      None found")

    results = {
        's_values': s_values,
        'mu_values': mu_values,
        'Lambda_values': Lambda_values,
        'F_unreg': F_unreg,
        'F_boltz': F_boltz,
        'N_eff': N_eff_arr,
        'n_zero': n_zero_arr,
        'critical_points': critical_points,
        'crit_map': crit_map,
        'C_V': C_V,
        'eval_cache': eval_cache,
    }

    return results


# =============================================================================
# MODULE 3: PHASE TRANSITION CLASSIFICATION
# =============================================================================

def classify_transitions(results, verbose=True):
    """
    Classify phase transitions from the phase diagram.

    First-order: discontinuity in dF/ds (latent heat)
    Second-order: divergence in d^2F/ds^2 (specific heat)
    Crossover: smooth, no singularity

    In our system, s is a continuous parameter and eigenvalues are continuous
    functions of s (by perturbation theory). So genuine first-order transitions
    in s would require level crossings (eigenvalue degeneracies).

    Returns:
        transitions: list of classified transitions
    """
    s_values = results['s_values']
    ds = s_values[1] - s_values[0]
    transitions = []

    if verbose:
        print(f"\n{'='*70}")
        print(f"  PHASE TRANSITION CLASSIFICATION")
        print(f"{'='*70}\n")

    for Lambda in results['Lambda_values']:
        N_eff = results['N_eff'][Lambda]

        # Look for sharp features in N_eff(s) — indicates eigenvalue crossing
        dN_ds = np.gradient(N_eff, ds)
        d2N_ds2 = np.gradient(dN_ds, ds)

        # Sharp feature = |d^2N/ds^2| > threshold
        threshold = 10 * np.std(d2N_ds2)
        sharp_idx = np.where(np.abs(d2N_ds2) > threshold)[0]

        if len(sharp_idx) > 0:
            # Cluster nearby sharp features
            clusters = []
            current = [sharp_idx[0]]
            for k in range(1, len(sharp_idx)):
                if sharp_idx[k] - sharp_idx[k-1] <= 2:
                    current.append(sharp_idx[k])
                else:
                    clusters.append(current)
                    current = [sharp_idx[k]]
            clusters.append(current)

            for cluster in clusters:
                s_trans = s_values[int(np.mean(cluster))]
                dN_magnitude = np.max(np.abs(dN_ds[cluster]))

                trans_type = 'crossover'  # default
                if dN_magnitude > 50:
                    trans_type = 'first-order-like'
                elif dN_magnitude > 10:
                    trans_type = 'second-order-like'

                transitions.append({
                    'Lambda': Lambda,
                    's_trans': s_trans,
                    'type': trans_type,
                    'dN_magnitude': dN_magnitude,
                })

                if verbose:
                    print(f"  Lambda={Lambda:.1f}: {trans_type} feature at s={s_trans:.3f}, "
                          f"|dN/ds|={dN_magnitude:.1f}")

        # Also check F for non-analyticity
        crits = results['critical_points'].get(Lambda, [])
        for c in crits:
            # Check if d^2F is very small (near-flat) — could indicate near-critical
            if abs(c['d2F']) < 1e-3:
                transitions.append({
                    'Lambda': Lambda,
                    's_trans': c['s_c'],
                    'type': 'near-critical (flat d2F)',
                    'dN_magnitude': 0,
                })
                if verbose:
                    print(f"  Lambda={Lambda:.1f}: near-critical at s={c['s_c']:.3f}, "
                          f"d2F={c['d2F']:.2e}")

    if not transitions and verbose:
        print(f"  No sharp phase transition features detected.")
        print(f"  All transitions are smooth crossovers in the deformation parameter s.")

    return transitions


# =============================================================================
# MODULE 4: PLOTTING
# =============================================================================

def plot_phase_diagram(results, save_prefix='spectral_free_energy'):
    """
    Generate comprehensive plots for the phase diagram.

    Plots:
      1. Phase diagram heatmap: F(s, mu) for each Lambda
      2. F(s) at fixed mu for multiple Lambda
      3. N_eff(s) for multiple Lambda
      4. dF/ds showing critical points
      5. Specific heat C_V(s)
      6. Critical point locations (s_c vs Lambda)
    """
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    from matplotlib.colors import Normalize

    s_values = results['s_values']
    mu_values = results['mu_values']
    Lambda_values = results['Lambda_values']

    fig, axes = plt.subplots(3, 2, figsize=(16, 18))
    fig.suptitle('H-2: Spectral Free Energy Phase Structure', fontsize=14, fontweight='bold')

    # --- Plot 1: Phase diagram heatmap (Lambda=1.0 or middle Lambda) ---
    ax = axes[0, 0]
    Lambda_ref = min(Lambda_values, key=lambda L: abs(L - 1.0))
    F_grid = results['F_boltz'][Lambda_ref]
    # Normalize per-mu column for visualization
    F_norm = np.zeros_like(F_grid)
    for j in range(len(mu_values)):
        col = F_grid[:, j]
        if np.ptp(col) > 0:
            F_norm[:, j] = (col - np.min(col)) / np.ptp(col)

    im = ax.pcolormesh(s_values, mu_values, F_norm.T,
                       shading='auto', cmap='RdYlBu_r')
    plt.colorbar(im, ax=ax, label='F (normalized)')
    ax.set_xlabel('Jensen parameter s')
    ax.set_ylabel('Scale mu')
    ax.set_yscale('log')
    ax.set_title(f'Phase diagram (Lambda={Lambda_ref:.1f})')

    # Overlay critical points
    crit_pts = results['crit_map'].get(Lambda_ref, [])
    if crit_pts:
        mins = [(c['mu'], c['s_c']) for c in crit_pts if c['type'] == 'min']
        maxs = [(c['mu'], c['s_c']) for c in crit_pts if c['type'] == 'max']
        if mins:
            ax.scatter([m[1] for m in mins], [m[0] for m in mins],
                      c='green', marker='o', s=15, zorder=5, label='minima')
        if maxs:
            ax.scatter([m[1] for m in maxs], [m[0] for m in maxs],
                      c='red', marker='x', s=15, zorder=5, label='maxima')
        ax.legend(fontsize=8)

    # --- Plot 2: F(s) at fixed mu for multiple Lambda ---
    ax = axes[0, 1]
    mu_ref_idx = len(mu_values) // 2
    mu_ref = mu_values[mu_ref_idx]
    for Lambda in Lambda_values:
        F_slice = results['F_boltz'][Lambda][:, mu_ref_idx]
        # Normalize to F(0)
        F0 = F_slice[0] if abs(F_slice[0]) > 1e-30 else 1.0
        ax.plot(s_values, F_slice / abs(F0), label=f'Lambda={Lambda:.1f}')
    ax.set_xlabel('Jensen parameter s')
    ax.set_ylabel('F(s) / |F(0)|')
    ax.set_title(f'Free energy at mu={mu_ref:.2f}')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # --- Plot 3: N_eff(s) for multiple Lambda ---
    ax = axes[1, 0]
    for Lambda in Lambda_values:
        ax.plot(s_values, results['N_eff'][Lambda], label=f'Lambda={Lambda:.1f}')
    ax.set_xlabel('Jensen parameter s')
    ax.set_ylabel('N_eff(s)')
    ax.set_title('Effective mode count')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # --- Plot 4: dF/ds showing critical points ---
    ax = axes[1, 1]
    ds = s_values[1] - s_values[0]
    for Lambda in Lambda_values:
        F_slice = results['F_boltz'][Lambda][:, mu_ref_idx]
        dF = np.gradient(F_slice, ds)
        ax.plot(s_values, dF, label=f'Lambda={Lambda:.1f}')
    ax.axhline(y=0, color='k', linestyle='--', alpha=0.3)
    ax.set_xlabel('Jensen parameter s')
    ax.set_ylabel('dF/ds')
    ax.set_title(f'Gradient at mu={mu_ref:.2f}')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Mark critical points
    for Lambda in Lambda_values:
        crits = results['critical_points'].get(Lambda, [])
        for c in crits:
            ax.axvline(x=c['s_c'], color='red', linestyle=':', alpha=0.3)

    # --- Plot 5: Specific heat C_V(s) ---
    ax = axes[2, 0]
    for Lambda in Lambda_values:
        ax.plot(s_values, results['C_V'][Lambda], label=f'Lambda={Lambda:.1f}')
    ax.set_xlabel('Jensen parameter s')
    ax.set_ylabel('C_V(s)')
    ax.set_title(f'Specific heat at mu={mu_ref:.2f}')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # --- Plot 6: Critical point locations ---
    ax = axes[2, 1]
    for Lambda in Lambda_values:
        crits = results['critical_points'].get(Lambda, [])
        if crits:
            for c in crits:
                marker = 'o' if c['type'] == 'minimum' else 'x'
                color = 'green' if c['type'] == 'minimum' else 'red'
                ax.scatter(Lambda, c['s_c'], marker=marker, color=color, s=100, zorder=5)

    # Also plot crit_map for all mu
    for Lambda in Lambda_values:
        crit_pts = results['crit_map'].get(Lambda, [])
        if crit_pts:
            s_crits = [c['s_c'] for c in crit_pts if c['type'] == 'min']
            if s_crits:
                ax.scatter([Lambda]*len(s_crits), s_crits,
                          marker='.', color='blue', alpha=0.1, s=10)

    ax.set_xlabel('Lambda')
    ax.set_ylabel('Critical s_c')
    ax.set_title('Critical points vs Lambda')
    ax.grid(True, alpha=0.3)

    # H-1 comparison
    ax.axhline(y=0.164, color='orange', linestyle='--', alpha=0.5, label='H-1: s=0.164')
    ax.axhline(y=0.481, color='purple', linestyle='--', alpha=0.5, label='H-1: s=0.481')
    ax.axhline(y=0.299, color='cyan', linestyle='--', alpha=0.5, label='sin2thetaW: s=0.299')
    ax.legend(fontsize=8)

    plt.tight_layout()
    save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             f'{save_prefix}.png')
    plt.savefig(save_path, dpi=150)
    plt.close()
    print(f"\n  Saved plot: {save_path}")
    return save_path


# =============================================================================
# MODULE 5: DETAILED ANALYSIS AND REPORT
# =============================================================================

def generate_report(results, transitions, verbose=True):
    """
    Generate the H-2 deliverable report.

    Contains:
      1. Phase diagram description
      2. Critical point locations
      3. Phase transition classification
      4. Comparison to H-1
      5. Thermodynamic interpretation
    """
    s_values = results['s_values']
    Lambda_values = results['Lambda_values']

    if verbose:
        print(f"\n{'='*70}")
        print(f"  H-2 REPORT: SPECTRAL FREE ENERGY AND PHASE STRUCTURE")
        print(f"{'='*70}")

        # 1. Summary of critical points
        print(f"\n  1. CRITICAL POINTS (dF/ds = 0)")
        print(f"  {'Lambda':<8} {'s_c':<10} {'Type':<12} {'F\"(s_c)':<12}")
        print(f"  {'-'*42}")
        any_crit = False
        for Lambda in Lambda_values:
            crits = results['critical_points'].get(Lambda, [])
            for c in crits:
                print(f"  {Lambda:<8.1f} {c['s_c']:<10.4f} {c['type']:<12} {c['d2F']:<12.3e}")
                any_crit = True
        if not any_crit:
            print(f"  (none found)")

        # 2. N_eff summary
        print(f"\n  2. EFFECTIVE MODE COUNT N_eff(s)")
        for Lambda in Lambda_values:
            N = results['N_eff'][Lambda]
            idx_min = np.argmin(N)
            idx_max = np.argmax(N)
            print(f"  Lambda={Lambda:.1f}: min N_eff={N[idx_min]:.1f} at s={s_values[idx_min]:.2f}, "
                  f"max N_eff={N[idx_max]:.1f} at s={s_values[idx_max]:.2f}")

        # 3. Phase transitions
        print(f"\n  3. PHASE TRANSITION CLASSIFICATION")
        if transitions:
            for t in transitions:
                print(f"  Lambda={t['Lambda']:.1f}: {t['type']} at s={t['s_trans']:.3f}")
        else:
            print(f"  No sharp phase transitions detected.")
            print(f"  The deformation parameter s does NOT induce phase transitions in the")
            print(f"  spectral free energy. All changes are smooth crossovers.")
            print(f"  This is CONSISTENT with the eigenvalue perturbation theory: eigenvalues")
            print(f"  of the Dirac operator on a compact space are smooth functions of the metric.")

        # 4. Comparison to H-1
        print(f"\n  4. COMPARISON TO H-1 (V_eff MINIMUM)")
        print(f"  H-1 Boltzmann minimum: s_0 = 0.164 (Lambda_UV ~ 1.23)")
        print(f"  H-1 second minimum:    s_0 = 0.481 (Lambda_UV = 1.43)")
        print(f"  sin^2(theta_W) match:  s_W = 0.299 (from B-1)")

        # Check if any H-2 critical point matches H-1
        matched = False
        for Lambda in Lambda_values:
            crits = results['critical_points'].get(Lambda, [])
            for c in crits:
                if c['type'] == 'minimum':
                    # Check against H-1 values
                    for s_ref, label in [(0.164, 'H-1 primary'), (0.481, 'H-1 secondary'),
                                          (0.299, 'sin2thetaW')]:
                        if abs(c['s_c'] - s_ref) < 0.05:
                            print(f"  MATCH: Lambda={Lambda:.1f}, s_c={c['s_c']:.4f} ~ {label} ({s_ref})")
                            matched = True

        if not matched:
            print(f"  No H-2 critical point matches H-1 minimum within 0.05.")
            print(f"  This suggests the free energy and CW potential have different structures.")

        # 5. Thermodynamic interpretation
        print(f"\n  5. THERMODYNAMIC INTERPRETATION")
        print(f"  The spectral free energy F(s, mu) = -sum dim * sum ln(|lam|^2/mu^2)")
        print(f"  counts the LOGARITHMIC spectral measure. This is the spectral zeta")
        print(f"  function at s=0 (zeta'(0)), which is the Hawking free energy of the")
        print(f"  internal space.")
        print(f"")
        print(f"  Physical prediction: the spectral free energy is the ANALOG of the")
        print(f"  Gibbons-Hawking free energy for de Sitter space, applied to the")
        print(f"  internal SU(3) geometry. The critical point (if any) corresponds to")
        print(f"  a Hawking-Page-like transition in the internal geometry.")

        # 6. Zero mode structure
        n_zero = results['n_zero']
        print(f"\n  6. ZERO MODE STRUCTURE")
        print(f"  Zero modes at s=0: {n_zero[0]:.0f}")
        print(f"  Zero modes at s=2.5: {n_zero[-1]:.0f}")
        if np.any(np.diff(n_zero) != 0):
            # Find where zero mode count changes
            changes = np.where(np.diff(n_zero) != 0)[0]
            for idx in changes:
                print(f"  Zero mode count CHANGES between s={s_values[idx]:.3f} and "
                      f"s={s_values[idx+1]:.3f}: {n_zero[idx]:.0f} -> {n_zero[idx+1]:.0f}")
                print(f"  THIS IS A TOPOLOGICAL TRANSITION (spectral flow)!")
        else:
            print(f"  Zero mode count CONSTANT across all s. No spectral flow detected.")

        print(f"\n{'='*70}")


# =============================================================================
# MODULE 6: MAIN EXECUTION
# =============================================================================

def main():
    """
    Run the full H-2 computation.
    """
    print(f"{'='*70}")
    print(f"  TIER 1: SPECTRAL FREE ENERGY AND PHASE STRUCTURE (H-2)")
    print(f"  Hawking-Theorist Agent, Session 17c")
    print(f"  {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*70}")

    # Initialize su(3) infrastructure
    print(f"\n  Initializing SU(3) infrastructure...")
    t0 = time.time()
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    gammas = build_cliff8()
    valid = validate_clifford(gammas)
    print(f"  Clifford algebra validated: {valid}")

    # Configuration
    max_pq_sum = 6  # Same as H-1 for consistency
    n_s = 51        # 0.05 resolution in s
    n_mu = 31       # Log-spaced mu values
    Lambda_values = [0.5, 1.0, 1.23, 2.0, 5.0]  # Include H-1's critical Lambda

    print(f"  max_pq_sum = {max_pq_sum}")
    print(f"  n_s = {n_s}, n_mu = {n_mu}")
    print(f"  Lambda values = {Lambda_values}")
    print(f"  Estimated runtime: {n_s * 8.7:.0f}s ({n_s * 8.7 / 60:.1f} min)")

    # Run phase diagram computation
    results = compute_phase_diagram(
        gens, f_abc, gammas,
        max_pq_sum=max_pq_sum,
        n_s=n_s, n_mu=n_mu,
        Lambda_values=Lambda_values,
        s_range=(0.0, 2.5),
        mu_range=(0.1, 10.0),
        verbose=True,
    )

    # Classify transitions
    transitions = classify_transitions(results, verbose=True)

    # Generate report
    generate_report(results, transitions, verbose=True)

    # Generate plots
    plot_path = plot_phase_diagram(results)

    # Timing
    total_time = time.time() - t0
    print(f"\n  Total runtime: {total_time:.1f}s ({total_time/60:.1f} min)")
    print(f"  Plot saved to: {plot_path}")
    print(f"\n{'='*70}")
    print(f"  H-2 COMPLETE")
    print(f"{'='*70}")


if __name__ == '__main__':
    main()
