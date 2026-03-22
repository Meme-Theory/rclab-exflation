"""
H-2: SPECTRAL FREE ENERGY PHASE DIAGRAM (Session 17c Deliverable)
==================================================================

Computes the spectral free energy F(s, mu) across the (s, mu) plane,
identifies critical points, classifies phase transitions, and compares
to the H-1 Coleman-Weinberg effective potential results.

Physical interpretation (Hawking's coffee-table insight):
  F(s, mu) = Helmholtz free energy of the internal SU(3) geometry
  s = order parameter (Jensen deformation)
  mu = temperature scale (renormalization point)
  Critical point dF/ds = 0 = spontaneous symmetry breaking
  Phase transition = Hawking-Page transition in internal space

Spectral zeta regularization:
  F(s, mu) = -sum_{(p,q)} dim(p,q) sum_j ln(|lambda_j^{(p,q)}(s)|^2 / mu^2)

This is zeta'(0), the derivative of the spectral zeta function at the origin.
Logarithmic UV behavior (vs lambda^4 in CW) gives dramatically better convergence.

Author: Hawking-Theorist Agent (Session 17c)
Date: 2026-02-14

References:
  - Hawking (1977): Zeta function regularization (Commun. Math. Phys. 55)
  - Gibbons & Hawking (1977): Partition function and Euclidean path integral
  - Connes (1996): Spectral action = phonon free energy
"""

import numpy as np
from scipy.optimize import brentq
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


def dim_su3_irrep(p, q):
    """Dimension of SU(3) irrep (p,q)."""
    return (p + 1) * (q + 1) * (p + q + 2) // 2


# =============================================================================
# CORE COMPUTATION: Free energy and derivatives
# =============================================================================

def spectral_free_energy(eval_data, mu):
    """
    Unregulated spectral free energy:
      F(s, mu) = -sum_{(p,q)} dim(p,q) * sum_j ln(|lambda_j|^2 / mu^2)

    Returns: (F_total, n_zero_modes, per_sector_dict)
    """
    mu_sq = mu ** 2
    F_total = 0.0
    n_zero = 0
    sectors = {}
    for p, q, evals in eval_data:
        d = dim_su3_irrep(p, q)
        a = np.abs(evals)
        mask = a > 1e-12
        n_zero += d * np.sum(~mask)
        nz = a[mask]
        if len(nz) == 0:
            sectors[(p, q)] = 0.0
            continue
        f_sector = -d * np.sum(np.log(nz ** 2 / mu_sq))
        sectors[(p, q)] = f_sector
        F_total += f_sector
    return F_total, n_zero, sectors


def spectral_free_energy_regulated(eval_data, mu, Lambda):
    """
    Boltzmann-regulated spectral free energy:
      F_reg = -sum dim(p,q) * sum_j exp(-|lam_j|^2/Lambda^2) * ln(|lam_j|^2/mu^2)

    Returns: (F_reg, N_eff)
    """
    mu_sq = mu ** 2
    Lsq = Lambda ** 2
    F_reg = 0.0
    N_eff = 0.0
    for p, q, evals in eval_data:
        d = dim_su3_irrep(p, q)
        a = np.abs(evals)
        nz = a[a > 1e-12]
        if len(nz) == 0:
            continue
        w = np.exp(-nz ** 2 / Lsq)
        F_reg += -d * np.sum(w * np.log(nz ** 2 / mu_sq))
        N_eff += d * np.sum(w)
    return F_reg, N_eff


def spectral_specific_heat(eval_data, mu, Lambda):
    """
    Specific heat C_V = -mu * d^2F/dmu^2 = 2 * N_eff / mu.
    The s-dependence comes entirely through N_eff(s, Lambda).
    """
    _, N_eff = spectral_free_energy_regulated(eval_data, mu, Lambda)
    return 2.0 * N_eff / mu, N_eff


# =============================================================================
# PHASE DIAGRAM ENGINE
# =============================================================================

def run_phase_diagram(gens, f_abc, gammas, max_pq_sum=6,
                      n_s=51, n_mu=31,
                      s_range=(0.0, 2.5), mu_range=(0.1, 10.0),
                      Lambda_values=None, verbose=True):
    """
    Full (s, mu) phase diagram computation.

    Steps:
      1. Pre-compute Dirac eigenvalues at each s (the expensive step)
      2. Evaluate F(s, mu) and F_reg(s, mu, Lambda) on the grid
      3. Numerical gradient dF/ds, d^2F/ds^2
      4. Find critical points, classify transitions
      5. Compute specific heat profile
    """
    if Lambda_values is None:
        Lambda_values = [0.5, 1.0, 1.23, 2.0, 5.0]

    s_vals = np.linspace(s_range[0], s_range[1], n_s)
    mu_vals = np.logspace(np.log10(mu_range[0]), np.log10(mu_range[1]), n_mu)
    ds = s_vals[1] - s_vals[0] if n_s > 1 else 0.05

    if verbose:
        print(f"\n{'='*72}")
        print(f"  H-2: SPECTRAL FREE ENERGY PHASE DIAGRAM")
        print(f"  {n_s} s-values x {n_mu} mu-values x {len(Lambda_values)} Lambda-values")
        print(f"  s in [{s_range[0]}, {s_range[1]}], mu in [{mu_range[0]}, {mu_range[1]}]")
        print(f"  Lambda = {Lambda_values}")
        print(f"  max_pq_sum = {max_pq_sum}")
        print(f"  Estimated eigenvalue time: ~{n_s * 8.7:.0f}s ({n_s * 8.7 / 60:.1f} min)")
        print(f"{'='*72}\n")

    # ------------------------------------------------------------------
    # STEP 1: Pre-compute Dirac eigenvalues
    # ------------------------------------------------------------------
    if verbose:
        print("  [Step 1] Pre-computing Dirac eigenvalues...")
    t0 = time.time()
    eig_cache = {}
    for i, s in enumerate(s_vals):
        if verbose and (i % 5 == 0 or i == n_s - 1):
            elapsed = time.time() - t0
            rate = max((i + 1) / max(elapsed, 0.01), 0.001)
            eta = (n_s - i - 1) / rate
            print(f"    s={s:.3f} ({i+1}/{n_s}), elapsed={elapsed:.0f}s, ETA={eta:.0f}s",
                  flush=True)
            sys.stdout.flush()
        _, eval_data = collect_spectrum(
            s, gens, f_abc, gammas, max_pq_sum=max_pq_sum, verbose=False
        )
        eig_cache[i] = eval_data

    t_eig = time.time() - t0
    if verbose:
        print(f"  Eigenvalue step: {t_eig:.1f}s ({t_eig/n_s:.1f}s per s-value)\n")

    # ------------------------------------------------------------------
    # STEP 2: Unregulated F(s, mu) on the grid
    # ------------------------------------------------------------------
    if verbose:
        print("  [Step 2] Unregulated F(s, mu)...")
    F_unreg = np.zeros((n_s, n_mu))
    n_zero_arr = np.zeros(n_s)
    for i in range(n_s):
        for j, mu in enumerate(mu_vals):
            Fv, nz, _ = spectral_free_energy(eig_cache[i], mu)
            F_unreg[i, j] = Fv
            if j == 0:
                n_zero_arr[i] = nz
    if verbose:
        print(f"    Zero modes: {n_zero_arr[0]:.0f} (s=0) to {n_zero_arr[-1]:.0f} (s={s_vals[-1]:.1f})")

    # ------------------------------------------------------------------
    # STEP 3: Boltzmann-regulated F(s, mu, Lambda)
    # ------------------------------------------------------------------
    if verbose:
        print("  [Step 3] Boltzmann-regulated F(s, mu, Lambda)...")
    F_reg = {}
    N_eff = {}
    for Lam in Lambda_values:
        F_reg[Lam] = np.zeros((n_s, n_mu))
        N_eff[Lam] = np.zeros(n_s)
        for i in range(n_s):
            for j, mu in enumerate(mu_vals):
                fv, ne = spectral_free_energy_regulated(eig_cache[i], mu, Lam)
                F_reg[Lam][i, j] = fv
                if j == 0:
                    N_eff[Lam][i] = ne
        if verbose:
            print(f"    Lambda={Lam:.2f}: N_eff in [{np.min(N_eff[Lam]):.1f}, {np.max(N_eff[Lam]):.1f}]")

    # ------------------------------------------------------------------
    # STEP 4: Critical points dF/ds = 0
    # ------------------------------------------------------------------
    if verbose:
        print("\n  [Step 4] Finding critical points (dF/ds = 0)...")

    critical_pts = {}
    for Lam in Lambda_values:
        critical_pts[Lam] = {}
        for j, mu in enumerate(mu_vals):
            F_slice = F_reg[Lam][:, j]
            dF = np.gradient(F_slice, ds)
            d2F = np.gradient(dF, ds)
            crits_j = []
            for k in range(len(dF) - 1):
                if dF[k] * dF[k+1] < 0:
                    sc = s_vals[k] - dF[k] * ds / (dF[k+1] - dF[k])
                    d2Fc = np.interp(sc, s_vals, d2F)
                    Fc = np.interp(sc, s_vals, F_slice)
                    crits_j.append({
                        's_c': sc, 'F_c': Fc, 'd2F': d2Fc,
                        'type': 'minimum' if d2Fc > 0 else 'maximum',
                    })
            critical_pts[Lam][j] = crits_j

    # Summary at reference mu
    mu_ref_idx = n_mu // 2
    mu_ref = mu_vals[mu_ref_idx]
    if verbose:
        print(f"    Reference mu = {mu_ref:.3f}")
        for Lam in Lambda_values:
            cps = critical_pts[Lam].get(mu_ref_idx, [])
            if cps:
                for c in cps:
                    print(f"    Lambda={Lam:.2f}: {c['type']} at s={c['s_c']:.4f}, "
                          f"F''={c['d2F']:.3e}")
            else:
                print(f"    Lambda={Lam:.2f}: MONOTONIC (no critical points)")

    # ------------------------------------------------------------------
    # STEP 5: Specific heat C_V(s)
    # ------------------------------------------------------------------
    if verbose:
        print("\n  [Step 5] Specific heat C_V(s)...")
    C_V = {}
    for Lam in Lambda_values:
        C_V[Lam] = np.zeros(n_s)
        for i in range(n_s):
            cv, _ = spectral_specific_heat(eig_cache[i], mu_ref, Lam)
            C_V[Lam][i] = cv

    # ------------------------------------------------------------------
    # STEP 6: Spectral flow (zero mode count changes)
    # ------------------------------------------------------------------
    if verbose:
        print("\n  [Step 6] Spectral flow analysis...")
    spectral_flow_transitions = []
    n_z_changes = np.where(np.diff(n_zero_arr) != 0)[0]
    if len(n_z_changes) > 0:
        for idx in n_z_changes:
            spectral_flow_transitions.append({
                's_left': s_vals[idx],
                's_right': s_vals[idx + 1],
                'n_zero_left': n_zero_arr[idx],
                'n_zero_right': n_zero_arr[idx + 1],
            })
            if verbose:
                print(f"    SPECTRAL FLOW at s in [{s_vals[idx]:.3f}, {s_vals[idx+1]:.3f}]: "
                      f"n_zero = {n_zero_arr[idx]:.0f} -> {n_zero_arr[idx+1]:.0f}")
    else:
        if verbose:
            print(f"    No spectral flow detected. Zero mode count = {n_zero_arr[0]:.0f} for all s.")

    # ------------------------------------------------------------------
    # STEP 7: Phase transition classification
    # ------------------------------------------------------------------
    if verbose:
        print("\n  [Step 7] Phase transition classification...")

    transitions = []
    for Lam in Lambda_values:
        Neff = N_eff[Lam]
        dN = np.gradient(Neff, ds)
        d2N = np.gradient(dN, ds)
        threshold = 10.0 * np.std(d2N) if np.std(d2N) > 0 else 1e10
        sharp = np.where(np.abs(d2N) > threshold)[0]
        if len(sharp) > 0:
            # Cluster
            clusters = [[sharp[0]]]
            for k in range(1, len(sharp)):
                if sharp[k] - sharp[k-1] <= 2:
                    clusters[-1].append(sharp[k])
                else:
                    clusters.append([sharp[k]])
            for cl in clusters:
                s_t = s_vals[int(np.mean(cl))]
                mag = np.max(np.abs(dN[cl]))
                ttype = 'first-order-like' if mag > 50 else ('second-order-like' if mag > 10 else 'crossover')
                transitions.append({'Lambda': Lam, 's_trans': s_t, 'type': ttype, '|dN/ds|': mag})
                if verbose:
                    print(f"    Lambda={Lam:.2f}: {ttype} at s={s_t:.3f}, |dN/ds|={mag:.1f}")

    if not transitions and verbose:
        print("    No sharp transitions. All changes are smooth crossovers.")

    return {
        's_vals': s_vals, 'mu_vals': mu_vals, 'ds': ds,
        'Lambda_values': Lambda_values,
        'F_unreg': F_unreg, 'F_reg': F_reg,
        'N_eff': N_eff, 'n_zero': n_zero_arr,
        'critical_pts': critical_pts,
        'C_V': C_V,
        'spectral_flow': spectral_flow_transitions,
        'transitions': transitions,
        'eig_cache': eig_cache,
        'mu_ref_idx': mu_ref_idx,
    }


# =============================================================================
# HIGH-RESOLUTION REFINEMENT near detected critical points
# =============================================================================

def refine_critical_points(results, gens, f_abc, gammas, max_pq_sum=6,
                           window=0.2, n_refine=21, verbose=True):
    """
    Zoom in on detected critical points with higher s-resolution.
    """
    Lambda_values = results['Lambda_values']
    mu_ref_idx = results['mu_ref_idx']
    mu_ref = results['mu_vals'][mu_ref_idx]

    refined = {}
    for Lam in Lambda_values:
        cps = results['critical_pts'][Lam].get(mu_ref_idx, [])
        if not cps:
            continue
        for cp in cps:
            sc = cp['s_c']
            s_lo = max(0.0, sc - window)
            s_hi = sc + window
            s_fine = np.linspace(s_lo, s_hi, n_refine)
            ds_fine = s_fine[1] - s_fine[0]

            F_fine = np.zeros(n_refine)
            for i, s in enumerate(s_fine):
                _, eval_data = collect_spectrum(
                    s, gens, f_abc, gammas, max_pq_sum=max_pq_sum, verbose=False
                )
                fv, _ = spectral_free_energy_regulated(eval_data, mu_ref, Lam)
                F_fine[i] = fv

            dF = np.gradient(F_fine, ds_fine)
            d2F = np.gradient(dF, ds_fine)

            # Refined critical point via interpolation
            for k in range(len(dF) - 1):
                if dF[k] * dF[k+1] < 0:
                    sc_ref = s_fine[k] - dF[k] * ds_fine / (dF[k+1] - dF[k])
                    d2Fc_ref = np.interp(sc_ref, s_fine, d2F)
                    key = (Lam, cp['type'])
                    refined[key] = {
                        's_c': sc_ref,
                        'd2F': d2Fc_ref,
                        'type': cp['type'],
                        'Lambda': Lam,
                        's_fine': s_fine,
                        'F_fine': F_fine,
                    }
                    if verbose:
                        print(f"    Refined: Lambda={Lam:.2f}, {cp['type']} at s={sc_ref:.6f}, "
                              f"F''={d2Fc_ref:.4e}")
                    break

    return refined


# =============================================================================
# REPORT
# =============================================================================

def print_report(results, verbose=True):
    """Print the full H-2 deliverable report."""
    s_vals = results['s_vals']
    mu_vals = results['mu_vals']
    Lambda_values = results['Lambda_values']
    mu_ref_idx = results['mu_ref_idx']
    mu_ref = mu_vals[mu_ref_idx]

    print(f"\n{'='*72}")
    print(f"  H-2 REPORT: SPECTRAL FREE ENERGY AND PHASE STRUCTURE")
    print(f"{'='*72}")

    # 1. Critical points
    print(f"\n  1. CRITICAL POINTS (dF/ds = 0) at mu = {mu_ref:.3f}")
    print(f"  {'Lambda':<10} {'s_c':<12} {'Type':<12} {'F\"(s_c)':<14}")
    print(f"  {'-'*48}")
    any_crit = False
    for Lam in Lambda_values:
        cps = results['critical_pts'][Lam].get(mu_ref_idx, [])
        for c in cps:
            print(f"  {Lam:<10.2f} {c['s_c']:<12.6f} {c['type']:<12} {c['d2F']:<14.4e}")
            any_crit = True
    if not any_crit:
        print(f"  (NONE found at reference mu)")

    # Scan all mu for critical points
    print(f"\n  Critical point scan across ALL mu values:")
    for Lam in Lambda_values:
        all_sc = []
        for j in range(len(mu_vals)):
            cps = results['critical_pts'][Lam].get(j, [])
            for c in cps:
                all_sc.append((mu_vals[j], c['s_c'], c['type']))
        if all_sc:
            s_min_c = min(x[1] for x in all_sc)
            s_max_c = max(x[1] for x in all_sc)
            n_min = sum(1 for x in all_sc if x[2] == 'minimum')
            n_max = sum(1 for x in all_sc if x[2] == 'maximum')
            print(f"    Lambda={Lam:.2f}: {len(all_sc)} critical pts, "
                  f"s_c in [{s_min_c:.4f}, {s_max_c:.4f}], "
                  f"{n_min} minima, {n_max} maxima")
        else:
            print(f"    Lambda={Lam:.2f}: MONOTONIC for ALL mu (no critical points)")

    # 2. N_eff
    print(f"\n  2. EFFECTIVE MODE COUNT N_eff(s)")
    for Lam in Lambda_values:
        N = results['N_eff'][Lam]
        imin = np.argmin(N)
        imax = np.argmax(N)
        print(f"    Lambda={Lam:.2f}: min={N[imin]:.1f} (s={s_vals[imin]:.2f}), "
              f"max={N[imax]:.1f} (s={s_vals[imax]:.2f}), "
              f"range={N[imax]-N[imin]:.1f}")

    # 3. Phase transitions
    print(f"\n  3. PHASE TRANSITION CLASSIFICATION")
    trans = results['transitions']
    if trans:
        for t in trans:
            print(f"    Lambda={t['Lambda']:.2f}: {t['type']} at s={t['s_trans']:.3f}, "
                  f"|dN/ds|={t['|dN/ds|']:.1f}")
    else:
        print(f"    No sharp phase transitions. All changes = smooth crossovers.")
        print(f"    REASON: Dirac eigenvalues on compact spaces are smooth functions of metric.")
        print(f"    Level crossings (if any) would produce non-analyticities but none detected.")

    # 4. Spectral flow
    print(f"\n  4. SPECTRAL FLOW (zero mode count)")
    sf = results['spectral_flow']
    if sf:
        for t in sf:
            print(f"    TRANSITION at s in [{t['s_left']:.3f}, {t['s_right']:.3f}]: "
                  f"n_zero = {t['n_zero_left']:.0f} -> {t['n_zero_right']:.0f}")
            print(f"    THIS IS A TOPOLOGICAL TRANSITION!")
    else:
        print(f"    Zero mode count = {results['n_zero'][0]:.0f} for all s. No spectral flow.")

    # 5. Comparison to H-1
    print(f"\n  5. COMPARISON TO H-1 (Coleman-Weinberg V_eff)")
    print(f"    H-1 results:")
    print(f"      Raw CW: 0/40 minima (BINDING FAILURE)")
    print(f"      Boltzmann primary:   s_0 = 0.164 at Lambda_UV ~ 1.23")
    print(f"      Boltzmann secondary: s_0 = 0.481 at Lambda_UV = 1.43")
    print(f"      NOT CONVERGED: 80% change pq=5 -> pq=6")
    print(f"    B-1 gauge coupling:    s_W = 0.2994 (from sin^2 theta_W)")
    print()

    # Check matches
    h1_targets = [
        (0.164, 'H-1 primary (s=0.164)'),
        (0.481, 'H-1 secondary (s=0.481)'),
        (0.2994, 'sin^2(theta_W) (s=0.2994)'),
    ]
    matched_any = False
    for Lam in Lambda_values:
        for j in range(len(mu_vals)):
            cps = results['critical_pts'][Lam].get(j, [])
            for c in cps:
                if c['type'] == 'minimum':
                    for s_ref, label in h1_targets:
                        if abs(c['s_c'] - s_ref) < 0.05:
                            print(f"    MATCH: Lambda={Lam:.2f}, mu={mu_vals[j]:.2f}, "
                                  f"s_c={c['s_c']:.4f} ~ {label}")
                            matched_any = True
    if not matched_any:
        print(f"    NO H-2 minima match H-1 targets within Delta_s < 0.05")
        print(f"    CONCLUSION: Free energy and CW potential have DIFFERENT structures.")

    # 6. Thermodynamic interpretation
    print(f"\n  6. THERMODYNAMIC INTERPRETATION")
    print(f"    F(s, mu) = -sum dim(p,q) * sum_j ln(|lam_j|^2/mu^2)")
    print(f"    This is the spectral zeta function zeta'(0), i.e., the determinant")
    print(f"    of the Dirac operator: F = -ln det(D/mu).")
    print(f"    Physical meaning: Helmholtz free energy of the internal geometry.")
    print(f"    Critical point = thermodynamic equilibrium of internal shape.")
    print(f"    The Boltzmann regulator exp(-|lam|^2/Lambda^2) is the thermal weight")
    print(f"    at effective temperature T ~ Lambda.")
    print(f"")
    print(f"    For the phonon-exflation picture:")
    print(f"      - s = 0 (bi-invariant) = high-symmetry (disordered) phase")
    print(f"      - s > 0 (Jensen deformed) = broken-symmetry (ordered) phase")
    print(f"      - If F has minimum at s_0 > 0: spontaneous symmetry breaking")
    print(f"      - If F is monotonically decreasing: no stable shape (runaway)")

    print(f"\n{'='*72}")


# =============================================================================
# PLOTTING
# =============================================================================

def make_plots(results, refined=None, save_path=None):
    """Generate comprehensive H-2 plots."""
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    s_vals = results['s_vals']
    mu_vals = results['mu_vals']
    Lam_vals = results['Lambda_values']
    mu_ref_idx = results['mu_ref_idx']
    mu_ref = mu_vals[mu_ref_idx]

    fig, axes = plt.subplots(3, 2, figsize=(16, 18))
    fig.suptitle('H-2: Spectral Free Energy Phase Diagram (Session 17c)',
                 fontsize=14, fontweight='bold')

    # -- Panel 1: Phase diagram heatmap (Lambda = 1.23, H-1's critical value) --
    ax = axes[0, 0]
    Lam_key = min(Lam_vals, key=lambda L: abs(L - 1.23))
    Fgrid = results['F_reg'][Lam_key]
    # Column-normalize for visualization
    Fnorm = np.zeros_like(Fgrid)
    for j in range(len(mu_vals)):
        col = Fgrid[:, j]
        rng = np.ptp(col)
        if rng > 0:
            Fnorm[:, j] = (col - np.min(col)) / rng
    im = ax.pcolormesh(s_vals, mu_vals, Fnorm.T, shading='auto', cmap='RdYlBu_r')
    plt.colorbar(im, ax=ax, label='F (column-normalized)')
    ax.set_xlabel('Jensen parameter s')
    ax.set_ylabel('Scale mu')
    ax.set_yscale('log')
    ax.set_title(f'Phase diagram (Lambda={Lam_key:.2f})')

    # Overlay critical points
    for j in range(len(mu_vals)):
        cps = results['critical_pts'][Lam_key].get(j, [])
        for c in cps:
            marker = 'o' if c['type'] == 'minimum' else 'x'
            color = 'lime' if c['type'] == 'minimum' else 'red'
            ax.scatter(c['s_c'], mu_vals[j], marker=marker, c=color, s=12, zorder=5)

    # -- Panel 2: F(s) at fixed mu for each Lambda --
    ax = axes[0, 1]
    for Lam in Lam_vals:
        F_slice = results['F_reg'][Lam][:, mu_ref_idx]
        F0 = F_slice[0] if abs(F_slice[0]) > 1e-30 else 1.0
        ax.plot(s_vals, F_slice / abs(F0), label=f'L={Lam:.2f}')
    ax.set_xlabel('s')
    ax.set_ylabel('F(s) / |F(0)|')
    ax.set_title(f'Free energy at mu={mu_ref:.2f}')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # -- Panel 3: N_eff(s) --
    ax = axes[1, 0]
    for Lam in Lam_vals:
        ax.plot(s_vals, results['N_eff'][Lam], label=f'L={Lam:.2f}')
    ax.set_xlabel('s')
    ax.set_ylabel('N_eff(s)')
    ax.set_title('Effective mode count')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # -- Panel 4: dF/ds --
    ax = axes[1, 1]
    ds = results['ds']
    for Lam in Lam_vals:
        F_slice = results['F_reg'][Lam][:, mu_ref_idx]
        dF = np.gradient(F_slice, ds)
        ax.plot(s_vals, dF, label=f'L={Lam:.2f}')
    ax.axhline(0, color='k', ls='--', alpha=0.3)
    ax.set_xlabel('s')
    ax.set_ylabel('dF/ds')
    ax.set_title(f'Gradient at mu={mu_ref:.2f}')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # -- Panel 5: Specific heat C_V(s) --
    ax = axes[2, 0]
    for Lam in Lam_vals:
        ax.plot(s_vals, results['C_V'][Lam], label=f'L={Lam:.2f}')
    ax.set_xlabel('s')
    ax.set_ylabel('C_V(s)')
    ax.set_title(f'Specific heat (mu={mu_ref:.2f})')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    # -- Panel 6: Critical point map (s_c vs Lambda) --
    ax = axes[2, 1]
    for Lam in Lam_vals:
        for j in range(len(mu_vals)):
            cps = results['critical_pts'][Lam].get(j, [])
            for c in cps:
                marker = 'o' if c['type'] == 'minimum' else 'x'
                color = 'green' if c['type'] == 'minimum' else 'red'
                ax.scatter(Lam, c['s_c'], marker=marker, color=color, s=8, alpha=0.15)

    # H-1 reference lines
    ax.axhline(0.164, color='orange', ls='--', alpha=0.6, label='H-1 primary (0.164)')
    ax.axhline(0.481, color='purple', ls='--', alpha=0.6, label='H-1 secondary (0.481)')
    ax.axhline(0.2994, color='cyan', ls='--', alpha=0.6, label='sin2thetaW (0.2994)')
    ax.set_xlabel('Lambda')
    ax.set_ylabel('Critical s_c')
    ax.set_title('Critical points vs Lambda')
    ax.legend(fontsize=7)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    if save_path is None:
        save_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 'h2_phase_diagram.png')
    plt.savefig(save_path, dpi=150)
    plt.close()
    print(f"  Plot saved: {save_path}")
    return save_path


# =============================================================================
# MAIN
# =============================================================================

def flush():
    """Force stdout flush (Windows/MINGW buffering workaround)."""
    sys.stdout.flush()


def main():
    # Force unbuffered output
    sys.stdout.reconfigure(line_buffering=True)

    print(f"{'='*72}")
    print(f"  H-2: SPECTRAL FREE ENERGY PHASE DIAGRAM")
    print(f"  Hawking-Theorist Agent, Session 17c")
    print(f"  {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*72}")
    flush()

    # Initialize infrastructure
    print(f"\n  Initializing SU(3) infrastructure...")
    flush()
    t_start = time.time()
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    gammas = build_cliff8()
    cliff_err = validate_clifford(gammas)
    print(f"  Clifford algebra error: {cliff_err:.2e}")
    flush()

    # Configuration
    MAX_PQ = 6          # Same truncation as H-1 for comparison
    N_S = 51            # s resolution: 0.05
    N_MU = 31           # mu resolution (log-spaced)
    LAMBDAS = [0.5, 1.0, 1.23, 2.0, 5.0]

    # Run the full phase diagram
    results = run_phase_diagram(
        gens, f_abc, gammas,
        max_pq_sum=MAX_PQ,
        n_s=N_S, n_mu=N_MU,
        s_range=(0.0, 2.5),
        mu_range=(0.1, 10.0),
        Lambda_values=LAMBDAS,
        verbose=True,
    )
    flush()

    # Full report (skip refinement — too slow for marginal gain)
    print_report(results)
    flush()

    # Plots
    try:
        plot_path = make_plots(results)
    except Exception as e:
        print(f"\n  PLOT ERROR: {e}")
        import traceback
        traceback.print_exc()
        plot_path = "(failed)"
    flush()

    # Summary
    t_total = time.time() - t_start
    print(f"\n  Total runtime: {t_total:.1f}s ({t_total/60:.1f} min)")
    print(f"\n{'='*72}")
    print(f"  H-2 COMPLETE")
    print(f"{'='*72}")
    flush()


if __name__ == '__main__':
    main()
