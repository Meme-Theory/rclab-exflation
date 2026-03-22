"""
Session 28b Computation 3: L-5 Per-Sector Pomeranchuk Map
=========================================================

PHYSICS:
    The Landau-Pomeranchuk instability criterion for a Fermi-liquid-like
    system is that the dimensionless Landau parameter

        f_l < -(2l + 1)

    triggers a Pomeranchuk instability in angular momentum channel l.
    For l=0 (s-wave): f_0 < -1.

    On the compact KK spectrum, we define the analog:

        f_0^{(p,q)}(tau) = -N^{(p,q)}(0, tau) * V_max^{(p,q)}(tau)

    where:
        N(0) = effective density of states at gap edge = 1 / delta_lambda
        delta_lambda = minimum level spacing at the gap edge
        V_max = maximum eigenvalue of the Kosmann pairing matrix

    This is the s-wave Landau parameter: f_0 < -1 indicates the Fermi
    surface is unstable to isotropic distortion (Pomeranchuk instability).

    Session 22c found f(0,0) = -4.687 < -3 in the singlet at tau=0.30
    using eigenvalue-flow-based definition. Here we use the Kosmann-coupling
    definition from the actual BCS pairing matrices computed in S27 and S28a.

DATA SOURCES:
    - s27_multisector_bcs.npz: 9 sectors, 9 tau values (D_K eigenbasis)
    - s28a_torsionful_bcs.npz: 8 sectors (no singlet), 10 tau values
      (both D_can and D_K eigenbases)

    We compute f_0 for BOTH bases to compare the effect of torsion.

OUTPUT:
    - s28b_pomeranchuk.npz: per-sector f_0 maps
    - s28b_pomeranchuk.png: heatmap visualization

GATE L-5: Diagnostic. Deepest instability in (3,0)+(0,3) at tau~0.30-0.35
    would be consistent with BCS interior minimum. Deepest in (2,1) would
    indicate high-multiplicity drives physics.

Author: phonon-exflation-sim
Date: 2026-02-27
Session: 28b, Computation 3
"""

import sys
import os
import time
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.colors import TwoSlopeNorm

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# ===========================================================================
# LOAD DATA
# ===========================================================================

def load_s27_data():
    """Load S27 multi-sector BCS data (D_K eigenbasis)."""
    path = os.path.join(SCRIPT_DIR, "s27_multisector_bcs.npz")
    d = np.load(path, allow_pickle=True)
    return d


def load_s28a_data():
    """Load S28a torsionful BCS data (D_can and D_K eigenbases)."""
    path = os.path.join(SCRIPT_DIR, "s28a_torsionful_bcs.npz")
    d = np.load(path, allow_pickle=True)
    return d


# ===========================================================================
# POMERANCHUK PARAMETER COMPUTATION
# ===========================================================================

def gap_edge_spacing(evals):
    """Compute the level spacing at the gap edge.

    The gap edge is defined as the eigenvalue(s) closest to zero.
    For a gapped spectrum with Kramers degeneracy, the gap-edge eigenvalues
    come in +/- pairs. The "level spacing" is the distance between the
    gap-edge level and the next distinct level.

    Parameters:
        evals: (N,) eigenvalues (real, from eigh of 1j*D)

    Returns:
        delta_lambda: minimum spacing between distinct |eigenvalue| levels
                      at the gap edge
        lambda_min: minimum |eigenvalue|
        n_gap_edge: number of eigenvalues at the gap edge (degeneracy)
    """
    abs_evals = np.sort(np.abs(evals))
    lambda_min = abs_evals[0]

    # Find distinct levels: group eigenvalues within 1e-10 of each other
    distinct = [abs_evals[0]]
    for e in abs_evals[1:]:
        if e - distinct[-1] > 1e-10:
            distinct.append(e)
    distinct = np.array(distinct)

    # Number of eigenvalues at gap edge
    n_gap_edge = int(np.sum(np.abs(abs_evals - lambda_min) < 1e-10))

    # Level spacing = distance to next distinct level
    if len(distinct) >= 2:
        delta_lambda = distinct[1] - distinct[0]
    else:
        # Only one distinct level -- use the level itself as a scale
        delta_lambda = lambda_min

    return delta_lambda, lambda_min, n_gap_edge


def compute_f0(evals, V_matrix):
    """Compute the s-wave Pomeranchuk parameter f_0.

    f_0 = -N(0) * V_max

    where:
        N(0) = 1 / delta_lambda  (density of states at gap edge)
        V_max = max eigenvalue of the Kosmann pairing matrix V

    Parameters:
        evals: (N,) eigenvalues
        V_matrix: (N, N) Kosmann pairing matrix (real symmetric PSD)

    Returns:
        f0: Pomeranchuk parameter (negative means attractive)
        N0: density of states
        V_max: maximum Kosmann coupling eigenvalue
        delta_lambda: gap-edge level spacing
        lambda_min: minimum |eigenvalue|
        n_gap_edge: gap-edge degeneracy
    """
    delta_lambda, lambda_min, n_gap_edge = gap_edge_spacing(evals)

    # N(0) = effective density of states at gap edge
    # For a discrete spectrum, N(0) = degeneracy / spacing
    N0 = 1.0 / max(delta_lambda, 1e-15)

    # V_max = maximum eigenvalue of the pairing matrix
    V_evals = np.linalg.eigvalsh(0.5 * (V_matrix + V_matrix.T))
    V_max = V_evals[-1]

    # Pomeranchuk parameter
    f0 = -N0 * V_max

    return f0, N0, V_max, delta_lambda, lambda_min, n_gap_edge


# ===========================================================================
# MAIN COMPUTATION
# ===========================================================================

def main():
    t_start = time.time()

    print("=" * 72)
    print("SESSION 28b L-5: PER-SECTOR POMERANCHUK MAP")
    print("=" * 72)
    print()

    # ------------------------------------------------------------------
    # 1. S27 DATA: D_K eigenbasis, 9 sectors, 9 tau values
    # ------------------------------------------------------------------
    print("Loading S27 multi-sector BCS data...")
    d27 = load_s27_data()
    tau_27 = d27['tau_values']
    sectors_27 = d27['sectors']
    n_sec_27 = len(sectors_27)
    n_tau_27 = len(tau_27)

    print(f"  {n_sec_27} sectors, {n_tau_27} tau values: {tau_27}")
    print()

    # Storage for S27 results
    f0_K_27 = np.full((n_sec_27, n_tau_27), np.nan)
    N0_K_27 = np.full((n_sec_27, n_tau_27), np.nan)
    Vmax_K_27 = np.full((n_sec_27, n_tau_27), np.nan)
    dlam_K_27 = np.full((n_sec_27, n_tau_27), np.nan)
    lammin_K_27 = np.full((n_sec_27, n_tau_27), np.nan)
    ngap_K_27 = np.full((n_sec_27, n_tau_27), np.nan)

    print("Computing f_0 for S27 (D_K eigenbasis):")
    print(f"  {'Sector':>8s} {'tau':>5s} {'f_0':>10s} {'N(0)':>10s} "
          f"{'V_max':>10s} {'d_lam':>10s} {'lam_min':>10s} {'n_gap':>6s}")
    print("-" * 75)

    for i_s in range(n_sec_27):
        p, q = int(sectors_27[i_s, 0]), int(sectors_27[i_s, 1])
        for i_t in range(n_tau_27):
            evals_key = f"evals_{p}_{q}_{i_t}"
            V_key = f"V_{p}_{q}_{i_t}"

            if evals_key not in d27 or V_key not in d27:
                continue

            evals = d27[evals_key]
            V = d27[V_key]

            f0, N0, Vmax, dlam, lmin, ngap = compute_f0(evals, V)

            f0_K_27[i_s, i_t] = f0
            N0_K_27[i_s, i_t] = N0
            Vmax_K_27[i_s, i_t] = Vmax
            dlam_K_27[i_s, i_t] = dlam
            lammin_K_27[i_s, i_t] = lmin
            ngap_K_27[i_s, i_t] = ngap

        # Print selected tau values
        for i_t in [0, 4, 8]:
            if i_t < n_tau_27 and not np.isnan(f0_K_27[i_s, i_t]):
                print(f"  ({p},{q})  {tau_27[i_t]:5.2f} {f0_K_27[i_s, i_t]:10.3f} "
                      f"{N0_K_27[i_s, i_t]:10.3f} {Vmax_K_27[i_s, i_t]:10.5f} "
                      f"{dlam_K_27[i_s, i_t]:10.5f} {lammin_K_27[i_s, i_t]:10.5f} "
                      f"{int(ngap_K_27[i_s, i_t]):6d}")

    print()

    # ------------------------------------------------------------------
    # 2. S28a DATA: D_can and D_K eigenbases, 8 sectors, 10 tau values
    # ------------------------------------------------------------------
    print("Loading S28a torsionful BCS data...")
    d28 = load_s28a_data()
    tau_28 = d28['tau_values']
    sectors_28 = d28['sectors']
    n_sec_28 = len(sectors_28)
    n_tau_28 = len(tau_28)

    print(f"  {n_sec_28} sectors, {n_tau_28} tau values: {tau_28}")
    print()

    # Storage for S28a results (both bases)
    f0_can_28 = np.full((n_sec_28, n_tau_28), np.nan)
    f0_K_28 = np.full((n_sec_28, n_tau_28), np.nan)
    N0_can_28 = np.full((n_sec_28, n_tau_28), np.nan)
    N0_K_28 = np.full((n_sec_28, n_tau_28), np.nan)
    Vmax_can_28 = np.full((n_sec_28, n_tau_28), np.nan)
    Vmax_K_28 = np.full((n_sec_28, n_tau_28), np.nan)
    dlam_can_28 = np.full((n_sec_28, n_tau_28), np.nan)
    dlam_K_28 = np.full((n_sec_28, n_tau_28), np.nan)
    lammin_can_28 = np.full((n_sec_28, n_tau_28), np.nan)
    lammin_K_28 = np.full((n_sec_28, n_tau_28), np.nan)

    print("Computing f_0 for S28a (D_can eigenbasis):")
    print(f"  {'Sector':>8s} {'tau':>5s} {'f0_can':>10s} {'f0_K':>10s} "
          f"{'ratio':>8s} {'V_can':>10s} {'V_K':>10s}")
    print("-" * 75)

    for i_s in range(n_sec_28):
        p, q = int(sectors_28[i_s, 0]), int(sectors_28[i_s, 1])
        for i_t in range(n_tau_28):
            # Canonical (torsionful) basis
            ec_key = f"evals_can_{p}_{q}_{i_t}"
            Vc_key = f"V_can_{p}_{q}_{i_t}"
            if ec_key in d28 and Vc_key in d28:
                evals_c = d28[ec_key]
                V_c = d28[Vc_key]
                f0c, N0c, Vc_max, dlam_c, lmin_c, _ = compute_f0(evals_c, V_c)
                f0_can_28[i_s, i_t] = f0c
                N0_can_28[i_s, i_t] = N0c
                Vmax_can_28[i_s, i_t] = Vc_max
                dlam_can_28[i_s, i_t] = dlam_c
                lammin_can_28[i_s, i_t] = lmin_c

            # Kosmann (LC) basis
            ek_key = f"evals_K_{p}_{q}_{i_t}"
            Vk_key = f"V_K_{p}_{q}_{i_t}"
            if ek_key in d28 and Vk_key in d28:
                evals_k = d28[ek_key]
                V_k = d28[Vk_key]
                f0k, N0k, Vk_max, dlam_k, lmin_k, _ = compute_f0(evals_k, V_k)
                f0_K_28[i_s, i_t] = f0k
                N0_K_28[i_s, i_t] = N0k
                Vmax_K_28[i_s, i_t] = Vk_max
                dlam_K_28[i_s, i_t] = dlam_k
                lammin_K_28[i_s, i_t] = lmin_k

        # Print selected tau values
        for i_t in [0, 3, 5, 9]:
            if i_t < n_tau_28:
                fc = f0_can_28[i_s, i_t]
                fk = f0_K_28[i_s, i_t]
                vc = Vmax_can_28[i_s, i_t]
                vk = Vmax_K_28[i_s, i_t]
                ratio = fc / fk if abs(fk) > 1e-15 else np.nan
                print(f"  ({p},{q})  {tau_28[i_t]:5.2f} {fc:10.3f} {fk:10.3f} "
                      f"{ratio:8.3f} {vc:10.5f} {vk:10.5f}")

    print()

    # ------------------------------------------------------------------
    # 3. ANALYSIS: Deepest instability
    # ------------------------------------------------------------------
    print("=" * 72)
    print("POMERANCHUK INSTABILITY SUMMARY")
    print("=" * 72)
    print()

    # S27 analysis (includes singlet)
    print("--- S27 D_K basis (includes (0,0) singlet) ---")
    print(f"  {'Sector':>8s} {'min f_0':>10s} {'at tau':>7s} {'Unstable?':>10s}")
    print("  " + "-" * 40)

    deepest_K_sector = None
    deepest_K_f0 = 0.0
    deepest_K_tau = 0.0

    for i_s in range(n_sec_27):
        p, q = int(sectors_27[i_s, 0]), int(sectors_27[i_s, 1])
        f0_row = f0_K_27[i_s, :]
        valid = ~np.isnan(f0_row)
        if not np.any(valid):
            continue
        min_f0 = np.nanmin(f0_row)
        min_tau = tau_27[np.nanargmin(f0_row)]
        unstable = min_f0 < -1.0
        marker = "YES" if unstable else "no"

        print(f"  ({p},{q})  {min_f0:10.3f} {min_tau:7.2f} {marker:>10s}")

        if min_f0 < deepest_K_f0:
            deepest_K_f0 = min_f0
            deepest_K_tau = min_tau
            deepest_K_sector = (p, q)

    print()
    if deepest_K_sector is not None:
        print(f"  DEEPEST K: ({deepest_K_sector[0]},{deepest_K_sector[1]}) "
              f"at tau={deepest_K_tau:.2f}, f_0={deepest_K_f0:.3f}")
    print()

    # S28a analysis (canonical basis)
    print("--- S28a D_can basis (torsionful) ---")
    print(f"  {'Sector':>8s} {'min f0_can':>12s} {'at tau':>7s} "
          f"{'min f0_K':>10s} {'at tau':>7s} {'can/K':>7s}")
    print("  " + "-" * 58)

    deepest_can_sector = None
    deepest_can_f0 = 0.0
    deepest_can_tau = 0.0

    for i_s in range(n_sec_28):
        p, q = int(sectors_28[i_s, 0]), int(sectors_28[i_s, 1])
        fc_row = f0_can_28[i_s, :]
        fk_row = f0_K_28[i_s, :]

        min_fc = np.nanmin(fc_row)
        min_fc_tau = tau_28[np.nanargmin(fc_row)]
        min_fk = np.nanmin(fk_row)
        min_fk_tau = tau_28[np.nanargmin(fk_row)]

        ratio = min_fc / min_fk if abs(min_fk) > 1e-15 else np.nan

        print(f"  ({p},{q})  {min_fc:12.3f} {min_fc_tau:7.2f} "
              f"{min_fk:10.3f} {min_fk_tau:7.2f} {ratio:7.2f}")

        if min_fc < deepest_can_f0:
            deepest_can_f0 = min_fc
            deepest_can_tau = min_fc_tau
            deepest_can_sector = (p, q)

    print()
    if deepest_can_sector is not None:
        print(f"  DEEPEST CAN: ({deepest_can_sector[0]},{deepest_can_sector[1]}) "
              f"at tau={deepest_can_tau:.2f}, f_0={deepest_can_f0:.3f}")
    print()

    # ------------------------------------------------------------------
    # 4. COMPARISON WITH BCS M_max FROM S27
    # ------------------------------------------------------------------
    print("--- Correlation with BCS M_max (S27, mu=0) ---")
    M_max_27 = d27['M_max']  # (n_sec_27, n_tau_27, n_mu)
    print(f"  {'Sector':>8s} {'f0(0.30)':>10s} {'M_max(0.30)':>12s} {'f0(0.15)':>10s} {'M_max(0.15)':>12s}")
    print("  " + "-" * 50)

    for i_s in range(n_sec_27):
        p, q = int(sectors_27[i_s, 0]), int(sectors_27[i_s, 1])
        # Find tau indices for 0.15 and 0.30
        i_015 = np.argmin(np.abs(tau_27 - 0.15))
        i_030 = np.argmin(np.abs(tau_27 - 0.30))
        f015 = f0_K_27[i_s, i_015]
        f030 = f0_K_27[i_s, i_030]
        M015 = M_max_27[i_s, i_015, 0]  # mu=0
        M030 = M_max_27[i_s, i_030, 0]
        print(f"  ({p},{q})  {f030:10.3f} {M030:12.5f} {f015:10.3f} {M015:12.5f}")

    print()

    # ------------------------------------------------------------------
    # 5. TORSION ENHANCEMENT FACTOR
    # ------------------------------------------------------------------
    print("--- Torsion enhancement of Pomeranchuk instability ---")
    print(f"  {'Sector':>8s} ", end="")
    for t in tau_28:
        print(f"{'t=' + f'{t:.2f}':>8s}", end="")
    print()
    print("  " + "-" * (8 + 8 * n_tau_28))

    enhance = np.full((n_sec_28, n_tau_28), np.nan)
    for i_s in range(n_sec_28):
        p, q = int(sectors_28[i_s, 0]), int(sectors_28[i_s, 1])
        for i_t in range(n_tau_28):
            fc = f0_can_28[i_s, i_t]
            fk = f0_K_28[i_s, i_t]
            if abs(fk) > 1e-15:
                enhance[i_s, i_t] = fc / fk
        print(f"  ({p},{q})  ", end="")
        for i_t in range(n_tau_28):
            e = enhance[i_s, i_t]
            if np.isnan(e):
                print(f"{'N/A':>8s}", end="")
            else:
                print(f"{e:8.2f}", end="")
        print()

    print()

    # ------------------------------------------------------------------
    # 6. GATE VERDICT
    # ------------------------------------------------------------------
    print("=" * 72)
    print("GATE L-5 VERDICT")
    print("=" * 72)
    print()

    # Count unstable sectors in each basis
    n_unstable_K = 0
    n_unstable_can = 0
    for i_s in range(n_sec_27):
        if np.nanmin(f0_K_27[i_s, :]) < -1.0:
            n_unstable_K += 1
    for i_s in range(n_sec_28):
        if np.nanmin(f0_can_28[i_s, :]) < -1.0:
            n_unstable_can += 1

    print(f"Pomeranchuk-unstable sectors (D_K basis):  {n_unstable_K}/{n_sec_27}")
    print(f"Pomeranchuk-unstable sectors (D_can basis): {n_unstable_can}/{n_sec_28}")
    print()

    if deepest_K_sector is not None:
        print(f"Deepest D_K instability:  ({deepest_K_sector[0]},{deepest_K_sector[1]}) "
              f"at tau={deepest_K_tau:.2f}, f_0={deepest_K_f0:.3f}")
    if deepest_can_sector is not None:
        print(f"Deepest D_can instability: ({deepest_can_sector[0]},{deepest_can_sector[1]}) "
              f"at tau={deepest_can_tau:.2f}, f_0={deepest_can_f0:.3f}")
    print()

    # Determine verdict
    if deepest_can_sector is not None and (deepest_can_sector == (3, 0) or deepest_can_sector == (0, 3)):
        if 0.25 <= deepest_can_tau <= 0.40:
            verdict = "CONSISTENT: (3,0)/(0,3) deepest at tau~0.30-0.35"
        else:
            verdict = f"PARTIAL: (3,0)/(0,3) deepest but at tau={deepest_can_tau:.2f}"
    elif deepest_can_sector is not None and deepest_can_sector == (2, 1):
        verdict = "HIGH-MULTIPLICITY: (2,1) dominates — dim=15 drives physics"
    else:
        sp_str = f"({deepest_can_sector[0]},{deepest_can_sector[1]})" if deepest_can_sector else "none"
        verdict = f"OTHER: deepest in {sp_str}"

    print(f"VERDICT: {verdict}")
    print()

    mean_enhance = np.nanmean(enhance[:, 1:])  # skip tau=0
    print(f"Mean torsion enhancement (can/K): {mean_enhance:.2f}")
    print(f"  Torsion {'STRENGTHENS' if mean_enhance > 1.0 else 'WEAKENS'} "
          f"Pomeranchuk instability by factor {mean_enhance:.2f}")
    print()

    # ------------------------------------------------------------------
    # 7. SAVE DATA
    # ------------------------------------------------------------------
    outpath = os.path.join(SCRIPT_DIR, "s28b_pomeranchuk.npz")
    save_dict = {
        # S27 D_K results
        "tau_27": tau_27,
        "sectors_27": sectors_27,
        "f0_K_27": f0_K_27,
        "N0_K_27": N0_K_27,
        "Vmax_K_27": Vmax_K_27,
        "dlam_K_27": dlam_K_27,
        "lammin_K_27": lammin_K_27,
        # S28a results (both bases)
        "tau_28": tau_28,
        "sectors_28": sectors_28,
        "f0_can_28": f0_can_28,
        "f0_K_28": f0_K_28,
        "N0_can_28": N0_can_28,
        "N0_K_28": N0_K_28,
        "Vmax_can_28": Vmax_can_28,
        "Vmax_K_28": Vmax_K_28,
        "dlam_can_28": dlam_can_28,
        "dlam_K_28": dlam_K_28,
        "lammin_can_28": lammin_can_28,
        "lammin_K_28": lammin_K_28,
        "enhance": enhance,
        "verdict": np.array(verdict),
    }
    np.savez_compressed(outpath, **save_dict)
    print(f"Saved: {outpath}")
    print()

    # ------------------------------------------------------------------
    # 8. PLOT
    # ------------------------------------------------------------------
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle("L-5 Per-Sector Pomeranchuk Map", fontsize=14, fontweight='bold')

    # --- Panel (a): S27 D_K heatmap ---
    ax = axes[0, 0]
    sector_labels_27 = [f"({int(s[0])},{int(s[1])})" for s in sectors_27]

    # Replace NaN with 0 for plotting
    data_plot = np.where(np.isnan(f0_K_27), 0, f0_K_27)
    vmin = min(np.nanmin(f0_K_27), -1)
    vmax = max(np.nanmax(f0_K_27), 0)
    # Use diverging colormap centered at -1 (instability threshold)
    if vmin < -1 and vmax > -1:
        norm = TwoSlopeNorm(vmin=vmin, vcenter=-1, vmax=max(vmax, -0.5))
    else:
        norm = None
    im = ax.imshow(data_plot, aspect='auto', cmap='RdBu_r', norm=norm,
                   interpolation='nearest')
    ax.set_xticks(range(n_tau_27))
    ax.set_xticklabels([f"{t:.2f}" for t in tau_27], fontsize=8, rotation=45)
    ax.set_yticks(range(n_sec_27))
    ax.set_yticklabels(sector_labels_27, fontsize=9)
    ax.set_xlabel(r"$\tau$")
    ax.set_ylabel("Sector (p,q)")
    ax.set_title(r"$f_0$ (D_K basis, S27)")
    plt.colorbar(im, ax=ax, label=r"$f_0$")
    # Mark unstable cells
    for i_s in range(n_sec_27):
        for i_t in range(n_tau_27):
            val = f0_K_27[i_s, i_t]
            if not np.isnan(val) and val < -1.0:
                ax.plot(i_t, i_s, 'kx', markersize=8, markeredgewidth=2)
            if not np.isnan(val):
                ax.text(i_t, i_s, f"{val:.1f}", ha='center', va='center',
                        fontsize=6, color='white' if val < -2 else 'black')

    # --- Panel (b): S28a D_can heatmap ---
    ax = axes[0, 1]
    sector_labels_28 = [f"({int(s[0])},{int(s[1])})" for s in sectors_28]

    data_plot2 = np.where(np.isnan(f0_can_28), 0, f0_can_28)
    vmin2 = min(np.nanmin(f0_can_28), -1)
    vmax2 = max(np.nanmax(f0_can_28), 0)
    if vmin2 < -1 and vmax2 > -1:
        norm2 = TwoSlopeNorm(vmin=vmin2, vcenter=-1, vmax=max(vmax2, -0.5))
    else:
        norm2 = None
    im2 = ax.imshow(data_plot2, aspect='auto', cmap='RdBu_r', norm=norm2,
                    interpolation='nearest')
    ax.set_xticks(range(n_tau_28))
    ax.set_xticklabels([f"{t:.2f}" for t in tau_28], fontsize=8, rotation=45)
    ax.set_yticks(range(n_sec_28))
    ax.set_yticklabels(sector_labels_28, fontsize=9)
    ax.set_xlabel(r"$\tau$")
    ax.set_ylabel("Sector (p,q)")
    ax.set_title(r"$f_0$ (D_can basis, S28a)")
    plt.colorbar(im2, ax=ax, label=r"$f_0$")
    for i_s in range(n_sec_28):
        for i_t in range(n_tau_28):
            val = f0_can_28[i_s, i_t]
            if not np.isnan(val) and val < -1.0:
                ax.plot(i_t, i_s, 'kx', markersize=8, markeredgewidth=2)
            if not np.isnan(val):
                ax.text(i_t, i_s, f"{val:.1f}", ha='center', va='center',
                        fontsize=6, color='white' if val < -2 else 'black')

    # --- Panel (c): Torsion enhancement ---
    ax = axes[1, 0]
    data_enh = np.where(np.isnan(enhance), 1.0, enhance)
    im3 = ax.imshow(data_enh, aspect='auto', cmap='coolwarm',
                    norm=TwoSlopeNorm(vmin=np.nanmin(enhance[~np.isnan(enhance)]),
                                      vcenter=1.0,
                                      vmax=np.nanmax(enhance[~np.isnan(enhance)])),
                    interpolation='nearest')
    ax.set_xticks(range(n_tau_28))
    ax.set_xticklabels([f"{t:.2f}" for t in tau_28], fontsize=8, rotation=45)
    ax.set_yticks(range(n_sec_28))
    ax.set_yticklabels(sector_labels_28, fontsize=9)
    ax.set_xlabel(r"$\tau$")
    ax.set_ylabel("Sector (p,q)")
    ax.set_title(r"Torsion enhancement $f_0^{can}/f_0^K$")
    plt.colorbar(im3, ax=ax, label="Enhancement ratio")
    for i_s in range(n_sec_28):
        for i_t in range(n_tau_28):
            e = enhance[i_s, i_t]
            if not np.isnan(e):
                ax.text(i_t, i_s, f"{e:.2f}", ha='center', va='center',
                        fontsize=6)

    # --- Panel (d): f_0 vs tau line plot for selected sectors ---
    ax = axes[1, 1]
    colors = plt.cm.tab10(np.linspace(0, 1, n_sec_27))

    for i_s in range(n_sec_27):
        p, q = int(sectors_27[i_s, 0]), int(sectors_27[i_s, 1])
        valid = ~np.isnan(f0_K_27[i_s, :])
        if np.any(valid):
            ax.plot(tau_27[valid], f0_K_27[i_s, valid], 'o-',
                    color=colors[i_s], label=f"({p},{q}) K", markersize=4)

    # Add D_can lines for comparison (dashed)
    for i_s in range(n_sec_28):
        p, q = int(sectors_28[i_s, 0]), int(sectors_28[i_s, 1])
        # Find matching color from S27
        color_idx = None
        for j_s in range(n_sec_27):
            if int(sectors_27[j_s, 0]) == p and int(sectors_27[j_s, 1]) == q:
                color_idx = j_s
                break
        if color_idx is None:
            continue
        valid = ~np.isnan(f0_can_28[i_s, :])
        if np.any(valid):
            ax.plot(tau_28[valid], f0_can_28[i_s, valid], 's--',
                    color=colors[color_idx], markersize=3, alpha=0.7)

    ax.axhline(y=-1.0, color='red', linestyle=':', linewidth=2, label='f_0 = -1 threshold')
    ax.set_xlabel(r"$\tau$")
    ax.set_ylabel(r"$f_0(\tau)$")
    ax.set_title(r"$f_0$ vs $\tau$ (solid=D_K, dashed=D_can)")
    ax.legend(fontsize=7, ncol=2, loc='lower left')
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    figpath = os.path.join(SCRIPT_DIR, "s28b_pomeranchuk.png")
    fig.savefig(figpath, dpi=150, bbox_inches='tight')
    print(f"Saved: {figpath}")
    plt.close(fig)

    elapsed = time.time() - t_start
    print(f"\nTotal time: {elapsed:.1f}s")


if __name__ == "__main__":
    main()
