"""
F-1: Heat kernel spectral dimension over tau distribution.

Computes d_s(t) = -2 * d(ln K) / d(ln t) where K(t) = sum_k exp(-t * lambda_k^2)
for the Dirac operator D_K on Jensen-deformed SU(3).

Three tau distributions tested:
  (a) INCOHERENT: uniform tau in [0, 0.55] (Planck popcorn, no phase-locking)
  (b) COHERENT: Gaussian centered at tau=0.18, sigma=0.02 (condensate)
  (c) SINGLE: tau=0.18 (static vacuum at gradient-balance point)

Gate F-1-G: PASS if <d_s>_incoherent ~ 2 at small t.

Mathematical background:
  The heat kernel K(t) = Tr exp(-t D^2) encodes the spectral geometry.
  The spectral dimension d_s(t) interpolates between the UV dimension
  (t -> 0, probing high eigenvalues) and the IR dimension (t -> inf,
  probing the zero-mode sector). For a d-dimensional manifold,
  d_s(t) -> d as t -> 0 (Weyl's law). CDT quantum gravity predicts
  d_s -> 2 at the Planck scale, a universal short-distance behavior.

  For D_K on SU(3) with KO-dim=6, the UV spectral dimension should be 6
  (the geometric dimension of SU(3)) at each fixed tau. The question is
  whether AVERAGING over a tau distribution modifies this.

  With Peter-Weyl multiplicities: K(t) = sum_{(p,q)} dim(p,q)^2 *
  sum_k exp(-t * |lambda_k^{(p,q)}|^2) where lambda_k are eigenvalues
  of D in sector (p,q).

Input: tier0-computation/tier1_dirac_spectrum.py (spectrum computation)
Output: s31Ca_foam_spectral_dim.{npz,png}

Session 31Ca -- Quantum Foam Diagnostics
"""

import sys
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# Add tier0-computation to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__)))
from tier1_dirac_spectrum import (
    su3_generators, compute_structure_constants, compute_killing_form,
    build_cliff8, collect_spectrum
)


def compute_heat_kernel(eigenvalues_sq, multiplicities, t_values):
    """
    Compute heat kernel K(t) = sum_k m_k * exp(-t * lambda_k^2).

    Args:
        eigenvalues_sq: array of |lambda_k|^2 values
        multiplicities: array of Peter-Weyl multiplicities for each eigenvalue
        t_values: array of diffusion times

    Returns:
        K: array of K(t) values, shape (len(t_values),)
    """
    # Vectorized: K(t) = sum_k m_k * exp(-t * lam_k^2)
    # Shape: (n_t, n_eig)
    exponent = -np.outer(t_values, eigenvalues_sq)
    # Clip to avoid underflow issues
    exponent = np.clip(exponent, -700, 0)
    K = np.sum(multiplicities[None, :] * np.exp(exponent), axis=1)
    return K


def compute_spectral_dimension(K, t_values):
    """
    Compute spectral dimension d_s(t) = -2 * d(ln K) / d(ln t).

    Uses central finite differences on log-log data for numerical stability.

    Args:
        K: heat kernel values K(t)
        t_values: diffusion time values

    Returns:
        d_s: spectral dimension at interior t points
        t_mid: corresponding t values (interior points)
    """
    ln_K = np.log(K)
    ln_t = np.log(t_values)

    # Central differences for interior points
    d_lnK = np.diff(ln_K)
    d_lnt = np.diff(ln_t)
    dln_ratio = d_lnK / d_lnt

    # d_s at midpoints
    t_mid = np.sqrt(t_values[:-1] * t_values[1:])  # geometric mean
    d_s = -2.0 * dln_ratio

    return d_s, t_mid


def get_full_spectrum_at_tau(tau, gens, f_abc, gammas, max_pq_sum=6):
    """
    Compute full Dirac spectrum at given tau, returning eigenvalue-squared
    and Peter-Weyl multiplicities.

    Args:
        tau: Jensen deformation parameter
        gens: su(3) generators
        f_abc: structure constants
        gammas: Clifford generators
        max_pq_sum: truncation level

    Returns:
        evals_sq: array of |lambda|^2 for each distinct eigenvalue
        mults: array of Peter-Weyl multiplicities
    """
    all_evals, eval_data = collect_spectrum(tau, gens, f_abc, gammas,
                                            max_pq_sum=max_pq_sum,
                                            verbose=False)

    evals_sq = []
    mults = []
    for (ev, mult) in all_evals:
        evals_sq.append(np.abs(ev)**2)
        mults.append(mult)

    return np.array(evals_sq), np.array(mults, dtype=float)


def main():
    print("=" * 70)
    print("F-1: Heat Kernel Spectral Dimension over Tau Distribution")
    print("=" * 70)

    # Initialize SU(3) algebra infrastructure
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    gammas = build_cliff8()

    # Diffusion time range: t in logspace(-3, 3, 100)
    n_t = 100
    t_values = np.logspace(-3, 3, n_t)

    # Tau grid: 12 points spanning [0, 0.55] for good coverage
    # Including the 9 points from s23a + extras for smooth averaging
    tau_grid = np.array([0.0, 0.05, 0.10, 0.15, 0.18, 0.20, 0.25, 0.30,
                          0.35, 0.40, 0.45, 0.50, 0.55])
    n_tau = len(tau_grid)

    max_pq = 6  # N_max=6 for full spectrum (11,424 eigenvalues)

    # Compute spectrum at each tau
    print(f"\nComputing Dirac spectrum at {n_tau} tau values (N_max={max_pq})...")
    spectra = {}  # tau -> (evals_sq, mults)
    heat_kernels = {}  # tau -> K(t)

    for i, tau in enumerate(tau_grid):
        print(f"  [{i+1}/{n_tau}] tau = {tau:.3f} ...", end=" ", flush=True)
        evals_sq, mults = get_full_spectrum_at_tau(tau, gens, f_abc, gammas,
                                                    max_pq_sum=max_pq)
        n_evals = len(evals_sq)
        n_total = int(np.sum(mults))  # total with multiplicities
        print(f"{n_evals} distinct eigenvalues, {n_total} total (with PW mult)")

        spectra[tau] = (evals_sq, mults)
        K = compute_heat_kernel(evals_sq, mults, t_values)
        heat_kernels[tau] = K

    # =====================================================================
    # (c) SINGLE tau = 0.18
    # =====================================================================
    print("\n--- (c) Single tau = 0.18 ---")
    K_single = heat_kernels[0.18]
    d_s_single, t_mid = compute_spectral_dimension(K_single, t_values)
    print(f"  d_s at smallest t: {d_s_single[0]:.3f}")
    print(f"  d_s at largest t:  {d_s_single[-1]:.3f}")
    print(f"  d_s at t=1:        {d_s_single[np.argmin(np.abs(t_mid - 1.0))]:.3f}")

    # =====================================================================
    # (a) INCOHERENT: uniform average over tau in [0, 0.55]
    # =====================================================================
    print("\n--- (a) Incoherent: uniform tau in [0, 0.55] ---")
    # Trapezoidal integration: <K(t)> = (1/Delta_tau) * integral K(t, tau) dtau
    K_incoherent = np.zeros(n_t)
    for i, tau in enumerate(tau_grid):
        K_incoherent += heat_kernels[tau]  # equal weight for now
    # Weight by trapezoidal rule
    weights_trap = np.ones(n_tau)
    weights_trap[0] = 0.5
    weights_trap[-1] = 0.5
    dtau = np.diff(tau_grid)
    # Manual trapezoidal
    K_incoherent = np.zeros(n_t)
    for i in range(n_tau - 1):
        K_incoherent += 0.5 * (heat_kernels[tau_grid[i]] + heat_kernels[tau_grid[i+1]]) * dtau[i]
    K_incoherent /= (tau_grid[-1] - tau_grid[0])  # normalize

    d_s_incoherent, _ = compute_spectral_dimension(K_incoherent, t_values)
    print(f"  <d_s> at smallest t: {d_s_incoherent[0]:.3f}")
    print(f"  <d_s> at largest t:  {d_s_incoherent[-1]:.3f}")
    print(f"  <d_s> at t=1:        {d_s_incoherent[np.argmin(np.abs(t_mid - 1.0))]:.3f}")

    # =====================================================================
    # (b) COHERENT: Gaussian at tau=0.18, sigma=0.02
    # =====================================================================
    print("\n--- (b) Coherent: Gaussian(0.18, 0.02) ---")
    tau_center = 0.18
    tau_sigma = 0.02
    gauss_weights = np.exp(-0.5 * ((tau_grid - tau_center) / tau_sigma)**2)
    gauss_weights /= np.sum(gauss_weights)  # normalize to sum=1

    K_coherent = np.zeros(n_t)
    for i, tau in enumerate(tau_grid):
        K_coherent += gauss_weights[i] * heat_kernels[tau]

    d_s_coherent, _ = compute_spectral_dimension(K_coherent, t_values)
    print(f"  <d_s> at smallest t: {d_s_coherent[0]:.3f}")
    print(f"  <d_s> at largest t:  {d_s_coherent[-1]:.3f}")
    print(f"  <d_s> at t=1:        {d_s_coherent[np.argmin(np.abs(t_mid - 1.0))]:.3f}")

    # =====================================================================
    # Gate F-1-G Assessment
    # =====================================================================
    print("\n" + "=" * 70)
    print("GATE F-1-G ASSESSMENT")
    print("=" * 70)
    # Check d_s at small t for incoherent case
    # "Small t" = t < 0.01 (probing UV)
    uv_mask = t_mid < 0.01
    d_s_uv_incoherent = np.mean(d_s_incoherent[uv_mask]) if np.any(uv_mask) else d_s_incoherent[0]
    d_s_uv_coherent = np.mean(d_s_coherent[uv_mask]) if np.any(uv_mask) else d_s_coherent[0]
    d_s_uv_single = np.mean(d_s_single[uv_mask]) if np.any(uv_mask) else d_s_single[0]

    print(f"\n  UV spectral dimension (t < 0.01):")
    print(f"    Single tau=0.18:  d_s = {d_s_uv_single:.4f}")
    print(f"    Coherent (Gauss): d_s = {d_s_uv_coherent:.4f}")
    print(f"    Incoherent (unif):d_s = {d_s_uv_incoherent:.4f}")

    # Mid-range (t ~ 1)
    mid_mask = (t_mid > 0.3) & (t_mid < 3.0)
    d_s_mid_incoherent = np.mean(d_s_incoherent[mid_mask]) if np.any(mid_mask) else np.nan
    d_s_mid_coherent = np.mean(d_s_coherent[mid_mask]) if np.any(mid_mask) else np.nan
    d_s_mid_single = np.mean(d_s_single[mid_mask]) if np.any(mid_mask) else np.nan

    print(f"\n  Mid-range spectral dimension (0.3 < t < 3.0):")
    print(f"    Single tau=0.18:  d_s = {d_s_mid_single:.4f}")
    print(f"    Coherent (Gauss): d_s = {d_s_mid_coherent:.4f}")
    print(f"    Incoherent (unif):d_s = {d_s_mid_incoherent:.4f}")

    # IR (t > 100)
    ir_mask = t_mid > 100
    d_s_ir_incoherent = np.mean(d_s_incoherent[ir_mask]) if np.any(ir_mask) else d_s_incoherent[-1]
    d_s_ir_coherent = np.mean(d_s_coherent[ir_mask]) if np.any(ir_mask) else d_s_coherent[-1]
    d_s_ir_single = np.mean(d_s_single[ir_mask]) if np.any(ir_mask) else d_s_single[-1]

    print(f"\n  IR spectral dimension (t > 100):")
    print(f"    Single tau=0.18:  d_s = {d_s_ir_single:.4f}")
    print(f"    Coherent (Gauss): d_s = {d_s_ir_coherent:.4f}")
    print(f"    Incoherent (unif):d_s = {d_s_ir_incoherent:.4f}")

    # Gate verdict
    CDT_target = 2.0
    tolerance = 0.5  # d_s ~ 2 means within 0.5
    if abs(d_s_uv_incoherent - CDT_target) < tolerance:
        verdict = "PASS"
        verdict_detail = f"<d_s>_incoherent = {d_s_uv_incoherent:.3f} at small t (within {tolerance} of {CDT_target})"
    else:
        verdict = "DOES NOT FIRE"
        verdict_detail = (f"<d_s>_incoherent = {d_s_uv_incoherent:.3f} at small t "
                          f"(expected ~{CDT_target}, deviation = {abs(d_s_uv_incoherent - CDT_target):.3f})")

    print(f"\n  Gate F-1-G verdict: {verdict}")
    print(f"  Detail: {verdict_detail}")

    # Also check whether coherent restores dimensionality faster
    # Compare slope of d_s(t) between coherent and incoherent
    crossover_idx = np.argmin(np.abs(d_s_coherent - d_s_incoherent))
    if len(d_s_coherent) > 0:
        coherence_effect = d_s_coherent[-1] - d_s_incoherent[-1]
        print(f"\n  Coherence effect (IR): d_s_coherent - d_s_incoherent = {coherence_effect:.4f}")

    # =====================================================================
    # Save results
    # =====================================================================
    outfile = os.path.join(os.path.dirname(__file__), "s31Ca_foam_spectral_dim.npz")
    save_dict = {
        't_values': t_values,
        't_mid': t_mid,
        'tau_grid': tau_grid,
        'd_s_single': d_s_single,
        'd_s_incoherent': d_s_incoherent,
        'd_s_coherent': d_s_coherent,
        'K_single': K_single,
        'K_incoherent': K_incoherent,
        'K_coherent': K_coherent,
        'd_s_uv_single': np.array(d_s_uv_single),
        'd_s_uv_incoherent': np.array(d_s_uv_incoherent),
        'd_s_uv_coherent': np.array(d_s_uv_coherent),
        'd_s_ir_single': np.array(d_s_ir_single),
        'd_s_ir_incoherent': np.array(d_s_ir_incoherent),
        'd_s_ir_coherent': np.array(d_s_ir_coherent),
        'verdict': np.array(verdict),
    }
    # Also save per-tau eigenvalue-squared arrays for cross-check
    for tau in tau_grid:
        key = f"evals_sq_tau{tau:.3f}"
        save_dict[key] = spectra[tau][0]
        key_m = f"mults_tau{tau:.3f}"
        save_dict[key_m] = spectra[tau][1]

    np.savez_compressed(outfile, **save_dict)
    print(f"\n  Saved: {outfile}")

    # =====================================================================
    # Plot
    # =====================================================================
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Panel 1: Spectral dimension d_s(t) for all three distributions
    ax = axes[0, 0]
    ax.semilogx(t_mid, d_s_single, 'b-', lw=2, label=r'Single $\tau=0.18$')
    ax.semilogx(t_mid, d_s_coherent, 'r-', lw=2, label=r'Coherent (Gauss $\sigma=0.02$)')
    ax.semilogx(t_mid, d_s_incoherent, 'k-', lw=2, label=r'Incoherent (uniform)')
    ax.axhline(2.0, color='green', ls='--', lw=1, alpha=0.7, label=r'$d_s=2$ (CDT)')
    ax.axhline(6.0, color='orange', ls='--', lw=1, alpha=0.7, label=r'$d_s=6$ (Weyl)')
    ax.axhline(8.0, color='purple', ls='--', lw=1, alpha=0.5, label=r'$d_s=8$ (Seeley-DeWitt)')
    ax.set_xlabel(r'Diffusion time $t$')
    ax.set_ylabel(r'Spectral dimension $d_s(t)$')
    ax.set_title('F-1: Spectral Dimension Flow')
    ax.legend(fontsize=8)
    ax.set_ylim(-0.5, 12)
    ax.grid(True, alpha=0.3)

    # Panel 2: Heat kernels K(t) for all three
    ax = axes[0, 1]
    ax.loglog(t_values, K_single, 'b-', lw=2, label=r'Single $\tau=0.18$')
    ax.loglog(t_values, K_coherent, 'r-', lw=2, label='Coherent')
    ax.loglog(t_values, K_incoherent, 'k-', lw=2, label='Incoherent')
    ax.set_xlabel(r'Diffusion time $t$')
    ax.set_ylabel(r'Heat kernel $K(t)$')
    ax.set_title('Heat Kernel Traces')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel 3: Per-tau spectral dimension curves (spaghetti)
    ax = axes[1, 0]
    cmap = plt.cm.viridis
    for i, tau in enumerate(tau_grid):
        K_tau = heat_kernels[tau]
        d_s_tau, _ = compute_spectral_dimension(K_tau, t_values)
        color = cmap(i / (n_tau - 1))
        ax.semilogx(t_mid, d_s_tau, '-', color=color, lw=1, alpha=0.8,
                     label=f'$\\tau={tau:.2f}$' if i % 3 == 0 else None)
    ax.axhline(2.0, color='green', ls='--', lw=1, alpha=0.7)
    ax.axhline(6.0, color='orange', ls='--', lw=1, alpha=0.7)
    ax.set_xlabel(r'Diffusion time $t$')
    ax.set_ylabel(r'$d_s(t)$')
    ax.set_title(r'Per-$\tau$ Spectral Dimensions')
    ax.legend(fontsize=7, ncol=2)
    ax.set_ylim(-0.5, 12)
    ax.grid(True, alpha=0.3)

    # Panel 4: UV spectral dimension vs tau
    ax = axes[1, 1]
    d_s_uv_per_tau = []
    d_s_ir_per_tau = []
    for tau in tau_grid:
        K_tau = heat_kernels[tau]
        d_s_tau, t_m = compute_spectral_dimension(K_tau, t_values)
        uv = t_m < 0.01
        ir = t_m > 100
        d_s_uv_per_tau.append(np.mean(d_s_tau[uv]) if np.any(uv) else d_s_tau[0])
        d_s_ir_per_tau.append(np.mean(d_s_tau[ir]) if np.any(ir) else d_s_tau[-1])
    ax.plot(tau_grid, d_s_uv_per_tau, 'bo-', lw=2, label=r'UV ($t<0.01$)')
    ax.plot(tau_grid, d_s_ir_per_tau, 'rs-', lw=2, label=r'IR ($t>100$)')
    ax.axhline(2.0, color='green', ls='--', lw=1, alpha=0.7, label='CDT target')
    ax.axhline(6.0, color='orange', ls='--', lw=1, alpha=0.7, label='Weyl (d=6)')
    ax.axvline(0.18, color='gray', ls=':', lw=1, alpha=0.7, label=r'$\tau=0.18$')
    ax.set_xlabel(r'Jensen parameter $\tau$')
    ax.set_ylabel(r'$d_s$')
    ax.set_title(r'UV and IR Spectral Dimension vs $\tau$')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    plt.suptitle(f'F-1: Heat Kernel Spectral Dimension | Gate: {verdict}', fontsize=14, fontweight='bold')
    plt.tight_layout()

    plotfile = os.path.join(os.path.dirname(__file__), "s31Ca_foam_spectral_dim.png")
    plt.savefig(plotfile, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"  Saved: {plotfile}")

    print("\n" + "=" * 70)
    print(f"F-1 COMPLETE. Gate F-1-G: {verdict}")
    print(f"  {verdict_detail}")
    print("=" * 70)


if __name__ == "__main__":
    main()
