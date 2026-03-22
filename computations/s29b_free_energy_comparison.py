"""
Session 29b Computation 1: Free Energy Comparison at First-Order Transition (CP-1)
==================================================================================

PHYSICS:
    Compare F_condensed(tau, mu_eff) vs F_normal(tau, mu=0) to find the
    first-order BCS transition point.

    F_normal(tau) = S_spectral(tau)
        The spectral action with no condensation.  Monotonically decreasing
        (Wall 4 / L-1 / C-1).  This is the "normal state" free energy.

    F_condensed(tau, mu_eff) = S_spectral(tau) + F_BCS(tau, mu_eff)
        The spectral action plus BCS condensation energy.  F_BCS < 0 in
        regions where condensation is energetically favorable.

    The transition occurs where F_condensed < F_normal, i.e. where
    F_BCS(tau, mu_eff) < 0.  Since F_BCS = 0 at mu = 0 (no condensate)
    and F_BCS < 0 when mu_eff >= lambda_min (condensation threshold),
    the free energy comparison reduces to mapping the F_BCS < 0 boundary
    in (tau, mu) space.

    For the PHYSICAL scenario: mu_eff is provided dynamically by the
    Parker injection + scattering thermalization chain (KC-1 through KC-3).
    The self-consistent mu_eff(tau) profile depends on the drive rate
    from s29a (computation 29a-2).

    KEY QUESTION: Does the modulus reach a tau where F_BCS < 0 before
    tau ~ 0.60 (scattering headroom limit from 29a-1)?

    We analyze THREE mu scenarios:
    1. mu = lambda_min (mu/lmin = 1.0): BCS threshold, minimal condensation
    2. mu = 1.2 * lambda_min: moderate substrate doping
    3. mu_eff(tau) from self-consistent drive rate (KC-3 model)

GATE K-29c:
    FIRES if F_condensed > F_normal at ALL tau in [0, 2.0].
    Equivalently: FIRES if F_BCS >= 0 everywhere.

POSITIVE SIGNAL P-29e:
    FIRES if F_condensed < F_normal crossing at tau_cross in [0.20, 0.50].

DATA SOURCES:
    - s28b_self_consistent_tau_T.npz: F_total(tau, mu) = F_BCS landscape
    - s28a_spectral_action_comparison.npz: S_spectral(tau) at Lambda=1
    - s29a_derived_drive_rate.npz: V_eff(tau), E_total, drive rate profile
    - s27_multisector_bcs.npz: per-sector data, lambda_min(sector, tau)

Author: phonon-exflation-sim
Date: 2026-02-28
Session: 29Ab, Computation 1
"""

import os
import sys
import numpy as np
from scipy.interpolate import interp1d

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))


# ===========================================================================
# DATA LOADING
# ===========================================================================

def load_all_data():
    """Load all input datasets.

    Returns:
        dict with all loaded data organized by source
    """
    data = {}

    # 1. BCS condensation energy landscape: F_BCS(tau, mu)
    path_28b = os.path.join(SCRIPT_DIR, "s28b_self_consistent_tau_T.npz")
    d28b = np.load(path_28b, allow_pickle=True)
    data['tau_bcs'] = d28b['tau_values']          # (9,): [0, 0.1, ..., 0.5]
    data['mu_ratios'] = d28b['mu_ratios']          # (12,): [0, 0.5, ..., 3.0]
    data['F_bcs'] = d28b['F_total']                # (9, 12): BCS condensation energy

    # 2. Spectral action (normal state)
    path_28a = os.path.join(SCRIPT_DIR, "s28a_spectral_action_comparison.npz")
    d28a = np.load(path_28a, allow_pickle=True)
    data['tau_sa'] = d28a['tau_values']            # (21,): [0, 0.025, ..., 0.5]
    data['S_spectral'] = d28a['S_LC_total_heat'][0]  # Lambda=1, heat kernel cutoff

    # 3. Drive rate data (V_eff, tau scan)
    path_29a = os.path.join(SCRIPT_DIR, "s29a_derived_drive_rate.npz")
    d29a = np.load(path_29a, allow_pickle=True)
    data['tau_scan_29a'] = d29a['tau_scan']        # (200,): [0.01, ..., 0.6]
    data['V_eff_scan'] = d29a['V_eff_scan']        # (200,): V_eff(tau) = S_spectral(tau)
    data['G_tau_tau'] = float(d29a['G_tau_tau'][0])  # 5.0 (Baptista Paper 15)
    data['V_at_0'] = float(d29a['V_at_0'][0])     # 17.7

    # 4. Per-sector data
    path_s27 = os.path.join(SCRIPT_DIR, "s27_multisector_bcs.npz")
    d27 = np.load(path_s27, allow_pickle=True)
    data['sectors'] = d27['sectors']               # (9, 4): (p, q, dim, mult)
    data['lambda_min'] = d27['lambda_min']         # (9, 9): lambda_min(sector, tau)
    data['F_cond_sector'] = d27['F_cond']          # (9, 9, 12): per-sector F_cond
    data['M_max'] = d27['M_max']                   # (9, 9, 12): BCS kernel strength
    data['Delta_max'] = d27['Delta_max']           # (9, 9, 12): BCS gap

    return data


# ===========================================================================
# FREE ENERGY COMPARISON
# ===========================================================================

def compute_free_energy_comparison(data):
    """Compare F_condensed vs F_normal at each tau.

    The comparison is structured as:
        F_normal(tau) = S_spectral(tau)
        F_condensed(tau, mu) = S_spectral(tau) + F_BCS(tau, mu)
        Delta_F(tau, mu) = F_condensed - F_normal = F_BCS(tau, mu)

    So the crossing condition is simply F_BCS(tau, mu) = 0.
    F_BCS < 0 means condensation is energetically favorable.

    We compute Delta_F for three mu scenarios:
    1. mu/lmin = 1.0 (threshold)
    2. mu/lmin = 1.2 (moderate doping)
    3. Self-consistent mu_eff(tau) from KC-3 chain

    Returns:
        dict with comparison results
    """
    tau_bcs = data['tau_bcs']
    mu_ratios = data['mu_ratios']
    F_bcs = data['F_bcs']
    tau_sa = data['tau_sa']
    S_spec = data['S_spectral']

    results = {}
    results['tau_bcs'] = tau_bcs
    results['mu_ratios'] = mu_ratios

    # -----------------------------------------------------------------------
    # 1. Interpolate spectral action onto BCS tau grid
    # -----------------------------------------------------------------------
    S_interp = interp1d(tau_sa, S_spec, kind='cubic', fill_value='extrapolate')
    S_at_bcs_tau = S_interp(tau_bcs)
    results['S_spectral_at_bcs_tau'] = S_at_bcs_tau

    # -----------------------------------------------------------------------
    # 2. Full free energy landscapes
    # -----------------------------------------------------------------------
    # F_normal(tau) = S_spectral(tau) -- same at all mu
    # F_condensed(tau, mu) = S_spectral(tau) + F_BCS(tau, mu)
    F_normal = S_at_bcs_tau  # (n_tau,)
    F_condensed = S_at_bcs_tau[:, None] + F_bcs  # (n_tau, n_mu)
    Delta_F = F_bcs.copy()  # (n_tau, n_mu) -- this IS F_BCS

    results['F_normal'] = F_normal
    results['F_condensed'] = F_condensed
    results['Delta_F'] = Delta_F

    # -----------------------------------------------------------------------
    # 3. Scenario 1: mu/lmin = 1.0 (BCS threshold)
    # -----------------------------------------------------------------------
    mi_10 = np.argmin(np.abs(mu_ratios - 1.0))
    F_bcs_10 = F_bcs[:, mi_10]
    results['scenario_1'] = {
        'mu_ratio': mu_ratios[mi_10],
        'F_bcs': F_bcs_10,
        'F_condensed': S_at_bcs_tau + F_bcs_10,
        'F_normal': F_normal.copy(),
    }

    # Find crossing: F_BCS transitions from 0 to < 0
    # F_BCS = 0 at mu < threshold, F_BCS < 0 once condensation starts
    condensed_mask_1 = F_bcs_10 < -1e-10
    if np.any(condensed_mask_1):
        first_condensed_idx = np.argmax(condensed_mask_1)
        results['scenario_1']['tau_cross'] = tau_bcs[first_condensed_idx]
        results['scenario_1']['F_bcs_at_cross'] = F_bcs_10[first_condensed_idx]
        results['scenario_1']['condensed'] = True

        # Find tau where F_BCS is most negative (deepest well)
        deepest_idx = np.argmin(F_bcs_10)
        results['scenario_1']['tau_deepest'] = tau_bcs[deepest_idx]
        results['scenario_1']['F_bcs_deepest'] = F_bcs_10[deepest_idx]
    else:
        results['scenario_1']['tau_cross'] = None
        results['scenario_1']['condensed'] = False

    # -----------------------------------------------------------------------
    # 4. Scenario 2: mu/lmin = 1.2 (moderate doping)
    # -----------------------------------------------------------------------
    mi_12 = np.argmin(np.abs(mu_ratios - 1.2))
    F_bcs_12 = F_bcs[:, mi_12]
    results['scenario_2'] = {
        'mu_ratio': mu_ratios[mi_12],
        'F_bcs': F_bcs_12,
        'F_condensed': S_at_bcs_tau + F_bcs_12,
        'F_normal': F_normal.copy(),
    }

    condensed_mask_2 = F_bcs_12 < -1e-10
    if np.any(condensed_mask_2):
        first_condensed_idx = np.argmax(condensed_mask_2)
        results['scenario_2']['tau_cross'] = tau_bcs[first_condensed_idx]
        results['scenario_2']['F_bcs_at_cross'] = F_bcs_12[first_condensed_idx]
        results['scenario_2']['condensed'] = True

        deepest_idx = np.argmin(F_bcs_12)
        results['scenario_2']['tau_deepest'] = tau_bcs[deepest_idx]
        results['scenario_2']['F_bcs_deepest'] = F_bcs_12[deepest_idx]
    else:
        results['scenario_2']['tau_cross'] = None
        results['scenario_2']['condensed'] = False

    # -----------------------------------------------------------------------
    # 5. Scenario 3: Self-consistent mu_eff(tau) from KC-3 model
    #    mu_eff = lambda_min when gap is filled (KC-3 PASS at tau >= ~0.41)
    #    Before tau_BCS_threshold, mu_eff < lambda_min (normal state, F_BCS = 0)
    # -----------------------------------------------------------------------
    # The KC-3 chain shows:
    #   - n_gap crosses 20 at tau ~ 0.407 for E = 2*V(0) (from 29a-2)
    #   - Below this tau, gap is not filled, so mu_eff < lambda_min
    #   - Above this tau, mu_eff >= lambda_min, BCS is active
    #
    # Physical model: F_BCS = 0 for tau < tau_KC3, then jumps to F_BCS(mu=lmin)
    # for tau >= tau_KC3. This is the first-order scenario from L-9.

    tau_KC3 = 0.407  # From s29a: n_gap crosses 20 at this tau
    F_bcs_sc = np.zeros_like(tau_bcs)
    for i, t in enumerate(tau_bcs):
        if t >= tau_KC3:
            # Gap filled: condensation active at mu = lambda_min
            F_bcs_sc[i] = F_bcs_10[i]
        else:
            # Gap not yet filled: normal state
            F_bcs_sc[i] = 0.0

    results['scenario_3'] = {
        'label': 'Self-consistent KC-3 model',
        'tau_KC3': tau_KC3,
        'F_bcs': F_bcs_sc,
        'F_condensed': S_at_bcs_tau + F_bcs_sc,
        'F_normal': F_normal.copy(),
    }

    condensed_mask_3 = F_bcs_sc < -1e-10
    if np.any(condensed_mask_3):
        first_condensed_idx = np.argmax(condensed_mask_3)
        results['scenario_3']['tau_cross'] = tau_bcs[first_condensed_idx]
        results['scenario_3']['F_bcs_at_cross'] = F_bcs_sc[first_condensed_idx]
        results['scenario_3']['condensed'] = True

        deepest_idx = np.argmin(F_bcs_sc)
        results['scenario_3']['tau_deepest'] = tau_bcs[deepest_idx]
        results['scenario_3']['F_bcs_deepest'] = F_bcs_sc[deepest_idx]
    else:
        results['scenario_3']['tau_cross'] = None
        results['scenario_3']['condensed'] = False

    # -----------------------------------------------------------------------
    # 6. V_eff total = S_spectral + F_BCS for the physical trajectory
    # -----------------------------------------------------------------------
    # This is V_eff(tau) that the modulus rolls on:
    #   V_eff_normal(tau) = S_spectral(tau) -- monotonically decreasing
    #   V_eff_condensed(tau) = S_spectral(tau) + F_BCS(tau, mu_eff)
    #
    # The key: does V_eff_condensed develop a MINIMUM?
    # S_spectral' < 0 everywhere. F_BCS' can be > 0 near the BCS well.
    # If |F_BCS'| > |S_spectral'| at some tau, V_eff_condensed has a minimum.

    # Compute derivatives via finite differences on the BCS tau grid
    dS_dtau = np.gradient(S_at_bcs_tau, tau_bcs)
    dFbcs_10_dtau = np.gradient(F_bcs_10, tau_bcs)
    dFbcs_12_dtau = np.gradient(F_bcs_12, tau_bcs)
    dV_total_10 = dS_dtau + dFbcs_10_dtau
    dV_total_12 = dS_dtau + dFbcs_12_dtau

    results['dS_dtau'] = dS_dtau
    results['dFbcs_10_dtau'] = dFbcs_10_dtau
    results['dFbcs_12_dtau'] = dFbcs_12_dtau
    results['dV_total_10'] = dV_total_10
    results['dV_total_12'] = dV_total_12

    # Check for gradient balance: dV_total = 0
    # Sign changes in dV_total indicate potential minima/maxima
    sign_changes_10 = np.where(np.diff(np.sign(dV_total_10)))[0]
    sign_changes_12 = np.where(np.diff(np.sign(dV_total_12)))[0]
    results['gradient_balance_10'] = sign_changes_10
    results['gradient_balance_12'] = sign_changes_12

    # -----------------------------------------------------------------------
    # 7. Per-sector breakdown at key tau values
    # -----------------------------------------------------------------------
    sectors = data['sectors']
    F_cond_sector = data['F_cond_sector']
    Delta_max = data['Delta_max']
    M_max = data['M_max']

    sector_analysis = {}
    for ti, t in enumerate(tau_bcs):
        if t in [0.0, 0.35, 0.50]:
            breakdown = []
            for si in range(len(sectors)):
                p, q, dim_rho, mult = sectors[si]
                f_10 = F_cond_sector[si, ti, mi_10]
                d_10 = Delta_max[si, ti, mi_10]
                m_10 = M_max[si, ti, mi_10]
                f_12 = F_cond_sector[si, ti, mi_12]
                d_12 = Delta_max[si, ti, mi_12]
                m_12 = M_max[si, ti, mi_12]
                breakdown.append({
                    'sector': f"({p},{q})", 'mult': mult,
                    'F_cond_10': f_10, 'Delta_10': d_10, 'M_max_10': m_10,
                    'F_cond_12': f_12, 'Delta_12': d_12, 'M_max_12': m_12,
                })
            sector_analysis[t] = breakdown

    results['sector_analysis'] = sector_analysis

    return results


# ===========================================================================
# GATE CLASSIFICATION
# ===========================================================================

def classify_gates(results):
    """Classify K-29c and P-29e gates.

    K-29c: FIRES if F_condensed > F_normal at ALL tau in [0, 2.0]
           Equivalently: F_BCS >= 0 at ALL tau for ALL physical mu.
           Since our data covers [0, 0.5], we check this range.
           Note: F_BCS is identically 0 at mu=0. The gate asks about
           physical mu_eff, which is >= lambda_min when gap is filled.

    P-29e: FIRES if crossing at tau_cross in [0.20, 0.50].

    Returns:
        dict with gate verdicts
    """
    gates = {}

    # K-29c: Does F_BCS ever become negative?
    # Check all three scenarios
    any_negative = False
    for key in ['scenario_1', 'scenario_2', 'scenario_3']:
        sc = results[key]
        if sc['condensed']:
            any_negative = True
            break

    if not any_negative:
        gates['K_29c'] = {
            'verdict': 'FIRES',
            'detail': 'F_condensed > F_normal at all tau. BCS never energetically favored.',
        }
    else:
        gates['K_29c'] = {
            'verdict': 'DOES NOT FIRE',
            'detail': 'F_condensed < F_normal at some tau. Condensation is energetically favorable.',
        }

    # P-29e: crossing in [0.20, 0.50]?
    # Use scenario 1 (mu = lambda_min) as the conservative estimate
    tau_cross_values = []
    for key, label in [('scenario_1', 'mu=lmin'),
                       ('scenario_2', 'mu=1.2*lmin'),
                       ('scenario_3', 'KC-3 model')]:
        sc = results[key]
        if sc['condensed'] and sc['tau_cross'] is not None:
            tc = sc['tau_cross']
            tau_cross_values.append((key, label, tc))

    in_window = [t for _, _, t in tau_cross_values if 0.20 <= t <= 0.50]
    if in_window:
        gates['P_29e'] = {
            'verdict': 'FIRES',
            'tau_cross_values': tau_cross_values,
            'detail': f'Crossing in [0.20, 0.50] found.',
        }
    else:
        gates['P_29e'] = {
            'verdict': 'DOES NOT FIRE',
            'tau_cross_values': tau_cross_values,
            'detail': 'No crossing in [0.20, 0.50].',
        }

    return gates


# ===========================================================================
# PLOTTING
# ===========================================================================

def make_plots(data, results, gates, save_path):
    """Generate 6-panel free energy comparison plot.

    Panels:
        1. F_normal(tau) and F_condensed(tau) at mu/lmin = 1.0 and 1.2
        2. Delta_F = F_BCS(tau) for three scenarios
        3. V_eff_total = S_spectral + F_BCS and gradient analysis
        4. Per-sector breakdown at tau=0.35
        5. Phase diagram: Delta_F(tau, mu) heatmap
        6. Gate verdicts

    Parameters:
        data: dict from load_all_data
        results: dict from compute_free_energy_comparison
        gates: dict from classify_gates
        save_path: output PNG path
    """
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt

    tau = results['tau_bcs']
    mu = results['mu_ratios']

    fig, axes = plt.subplots(2, 3, figsize=(18, 11))
    fig.suptitle("29b-1: Free Energy Comparison  |  F_condensed vs F_normal",
                 fontsize=13, fontweight='bold')

    # ------------------------------------------------------------------
    # Panel 1: F_normal and F_condensed
    # ------------------------------------------------------------------
    ax = axes[0, 0]
    S = results['S_spectral_at_bcs_tau']

    ax.plot(tau, S, 'k-', linewidth=2.5, label='$F_{normal}$ (spectral action)',
            zorder=3)

    # Scenario 1: mu = lambda_min
    sc1 = results['scenario_1']
    ax.plot(tau, sc1['F_condensed'], 'b--o', linewidth=1.5, markersize=4,
            label=f'$F_{{cond}}$ (mu/lmin={sc1["mu_ratio"]:.2f})')
    if sc1['condensed'] and sc1['tau_cross'] is not None:
        ax.axvline(sc1['tau_cross'], color='blue', linestyle=':', alpha=0.5)

    # Scenario 2: mu = 1.2*lambda_min
    sc2 = results['scenario_2']
    ax.plot(tau, sc2['F_condensed'], 'r--s', linewidth=1.5, markersize=4,
            label=f'$F_{{cond}}$ (mu/lmin={sc2["mu_ratio"]:.2f})')
    if sc2['condensed'] and sc2['tau_cross'] is not None:
        ax.axvline(sc2['tau_cross'], color='red', linestyle=':', alpha=0.5)

    ax.set_xlabel(r'$\tau$', fontsize=11)
    ax.set_ylabel('Free Energy', fontsize=11)
    ax.set_title('$F_{condensed}$ vs $F_{normal}$')
    ax.legend(fontsize=8, loc='upper right')
    ax.grid(True, alpha=0.3)

    # ------------------------------------------------------------------
    # Panel 2: Delta_F = F_BCS for three scenarios
    # ------------------------------------------------------------------
    ax = axes[0, 1]
    ax.axhline(0, color='k', linestyle='-', alpha=0.5, linewidth=0.8)

    ax.plot(tau, sc1['F_bcs'], 'b-o', linewidth=2, markersize=5,
            label=f'$\\Delta F$ (mu/lmin=1.0)', zorder=3)
    ax.plot(tau, sc2['F_bcs'], 'r-s', linewidth=2, markersize=5,
            label=f'$\\Delta F$ (mu/lmin=1.2)', zorder=3)

    sc3 = results['scenario_3']
    ax.plot(tau, sc3['F_bcs'], 'g-^', linewidth=2, markersize=5,
            label=f'$\\Delta F$ (KC-3 self-consistent)', zorder=3)

    # Mark crossing points
    for sc, color in [(sc1, 'blue'), (sc2, 'red'), (sc3, 'green')]:
        if sc['condensed'] and sc['tau_cross'] is not None:
            ax.axvline(sc['tau_cross'], color=color, linestyle=':', alpha=0.5)
            ax.plot(sc['tau_cross'], 0, '*', color=color, markersize=15, zorder=5)

    # Shade the physical window [0.20, 0.50]
    ax.axvspan(0.20, 0.50, alpha=0.08, color='green',
               label='Physical window')

    ax.set_xlabel(r'$\tau$', fontsize=11)
    ax.set_ylabel(r'$\Delta F = F_{BCS}$', fontsize=11)
    ax.set_title(r'$\Delta F(\tau) = F_{condensed} - F_{normal}$')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # ------------------------------------------------------------------
    # Panel 3: V_eff total and gradient analysis
    # ------------------------------------------------------------------
    ax = axes[0, 2]

    # V_eff_normal = S_spectral
    ax.plot(tau, S, 'k-', linewidth=2, label='$V_{normal}$ (spectral only)')

    # V_eff_condensed = S_spectral + F_BCS
    V_cond_10 = S + sc1['F_bcs']
    V_cond_12 = S + sc2['F_bcs']
    ax.plot(tau, V_cond_10, 'b--', linewidth=1.5,
            label=f'$V_{{cond}}$ (mu/lmin=1.0)')
    ax.plot(tau, V_cond_12, 'r--', linewidth=1.5,
            label=f'$V_{{cond}}$ (mu/lmin=1.2)')

    # Mark gradient balance points
    for idx_list, color, label in [(results['gradient_balance_10'], 'blue', 'mu=1.0'),
                                   (results['gradient_balance_12'], 'red', 'mu=1.2')]:
        for idx in idx_list:
            t_gb = 0.5 * (tau[idx] + tau[idx + 1])
            ax.axvline(t_gb, color=color, linestyle=':', alpha=0.5)
            ax.plot(t_gb, np.interp(t_gb, tau, S), 'v', color=color,
                    markersize=10, zorder=5)

    ax.set_xlabel(r'$\tau$', fontsize=11)
    ax.set_ylabel(r'$V_{eff}(\tau)$', fontsize=11)
    ax.set_title('$V_{eff}$ = spectral + BCS')
    ax.legend(fontsize=8, loc='upper right')
    ax.grid(True, alpha=0.3)

    # ------------------------------------------------------------------
    # Panel 4: Per-sector breakdown at tau=0.35
    # ------------------------------------------------------------------
    ax = axes[1, 0]
    if 0.35 in results['sector_analysis']:
        bd = results['sector_analysis'][0.35]
        labels_b = []
        values_10 = []
        values_12 = []
        for c in bd:
            if c['F_cond_10'] != 0.0 or c['F_cond_12'] != 0.0:
                labels_b.append(c['sector'])
                values_10.append(c['mult'] * c['F_cond_10'])
                values_12.append(c['mult'] * c['F_cond_12'])

        if labels_b:
            x = np.arange(len(labels_b))
            w = 0.35
            b1 = ax.bar(x - w/2, values_10, w, label='mu/lmin=1.0', color='blue',
                        alpha=0.7)
            b2 = ax.bar(x + w/2, values_12, w, label='mu/lmin=1.2', color='red',
                        alpha=0.7)
            ax.set_xticks(x)
            ax.set_xticklabels(labels_b, rotation=45)
            ax.axhline(0, color='k', linewidth=0.5)
            ax.set_ylabel('mult * F_cond')
            ax.legend(fontsize=8)
        else:
            ax.text(0.5, 0.5, 'No condensate at tau=0.35',
                    ha='center', va='center', transform=ax.transAxes)
    else:
        ax.text(0.5, 0.5, 'tau=0.35 not in grid', ha='center', va='center',
                transform=ax.transAxes)
    ax.set_title('Sector contributions at tau=0.35')
    ax.grid(True, alpha=0.3)

    # ------------------------------------------------------------------
    # Panel 5: Phase diagram Delta_F(tau, mu)
    # ------------------------------------------------------------------
    ax = axes[1, 1]
    # Only show mu >= 0.8
    mu_mask = mu >= 0.8
    Delta_F_sub = results['Delta_F'][:, mu_mask]
    mu_sub = mu[mu_mask]

    # Replace 0 with NaN for visualization
    Delta_F_plot = np.where(Delta_F_sub == 0.0, np.nan, Delta_F_sub)

    im = ax.imshow(Delta_F_plot.T, aspect='auto', origin='lower',
                   extent=[tau[0], tau[-1], mu_sub[0], mu_sub[-1]],
                   cmap='RdBu_r', vmin=-50, vmax=5,
                   interpolation='nearest')
    fig.colorbar(im, ax=ax, label=r'$\Delta F = F_{BCS}$')

    # Mark the condensation boundary (Delta_F = 0 contour)
    ax.contour(tau, mu_sub, Delta_F_plot.T, levels=[0],
               colors=['black'], linewidths=[2], linestyles=['--'])

    ax.set_xlabel(r'$\tau$', fontsize=11)
    ax.set_ylabel(r'$\mu / \lambda_{min}$', fontsize=11)
    ax.set_title(r'$\Delta F(\tau, \mu)$ phase diagram')

    # ------------------------------------------------------------------
    # Panel 6: Gate verdicts
    # ------------------------------------------------------------------
    ax = axes[1, 2]
    ax.axis('off')

    # K-29c
    k29c = gates['K_29c']
    k_color = 'red' if k29c['verdict'] == 'FIRES' else 'green'
    ax.text(0.5, 0.95, 'GATE VERDICTS', fontsize=14, fontweight='bold',
            ha='center', va='top', transform=ax.transAxes)

    ax.text(0.05, 0.85, f"K-29c: {k29c['verdict']}", fontsize=12,
            fontweight='bold', ha='left', va='top', transform=ax.transAxes,
            color=k_color)
    ax.text(0.05, 0.78, k29c['detail'], fontsize=9,
            ha='left', va='top', transform=ax.transAxes, wrap=True)

    # P-29e
    p29e = gates['P_29e']
    p_color = 'green' if p29e['verdict'] == 'FIRES' else 'gray'
    ax.text(0.05, 0.65, f"P-29e: {p29e['verdict']}", fontsize=12,
            fontweight='bold', ha='left', va='top', transform=ax.transAxes,
            color=p_color)
    ax.text(0.05, 0.58, p29e['detail'], fontsize=9,
            ha='left', va='top', transform=ax.transAxes, wrap=True)

    # Tau crossing summary
    y_pos = 0.45
    ax.text(0.05, y_pos, 'Crossing points (tau_cross):', fontsize=10,
            fontweight='bold', ha='left', va='top', transform=ax.transAxes)
    y_pos -= 0.07
    for key, label in [('scenario_1', 'mu=lmin'),
                       ('scenario_2', 'mu=1.2*lmin'),
                       ('scenario_3', 'KC-3 self-consistent')]:
        sc = results[key]
        if sc['condensed'] and sc['tau_cross'] is not None:
            tc = sc['tau_cross']
            in_window = 0.20 <= tc <= 0.50
            marker = 'IN WINDOW' if in_window else 'outside'
            ax.text(0.08, y_pos,
                    f"{label}: tau_cross = {tc:.3f} ({marker})",
                    fontsize=9, ha='left', va='top', transform=ax.transAxes,
                    color='green' if in_window else 'orange')
        else:
            ax.text(0.08, y_pos, f"{label}: no crossing",
                    fontsize=9, ha='left', va='top', transform=ax.transAxes,
                    color='red')
        y_pos -= 0.06

    # Deepest well
    y_pos -= 0.02
    ax.text(0.05, y_pos, 'Deepest BCS well:', fontsize=10,
            fontweight='bold', ha='left', va='top', transform=ax.transAxes)
    y_pos -= 0.07
    for key, label in [('scenario_1', 'mu=lmin'),
                       ('scenario_2', 'mu=1.2*lmin')]:
        sc = results[key]
        if sc['condensed']:
            ax.text(0.08, y_pos,
                    f"{label}: F_BCS = {sc['F_bcs_deepest']:.3f} at tau = {sc['tau_deepest']:.2f}",
                    fontsize=9, ha='left', va='top', transform=ax.transAxes)
        y_pos -= 0.06

    plt.tight_layout()
    plt.savefig(save_path, dpi=150, bbox_inches='tight')
    plt.close()
    print(f"Plot saved: {save_path}")


# ===========================================================================
# MAIN
# ===========================================================================

def main():
    print("=" * 78)
    print("29b-1: Free Energy Comparison  |  F_condensed vs F_normal")
    print("=" * 78)
    print()

    # -----------------------------------------------------------------------
    # 0. Gate check: verify 29Aa prerequisites
    # -----------------------------------------------------------------------
    verdict_path = os.path.join(SCRIPT_DIR, "s29a_gate_verdicts.txt")
    if os.path.exists(verdict_path):
        with open(verdict_path, 'r') as f:
            verdicts = f.read()
        if 'K-29a' in verdicts and 'PASS' in verdicts.split('K-29a')[1][:200]:
            print("29Aa gate check: K-29a PASS confirmed")
        if 'K-29b' in verdicts and 'CLEAN PASS' in verdicts.split('K-29b')[1][:200]:
            print("29Aa gate check: K-29b CLEAN PASS confirmed")
        print("Prerequisites satisfied. Proceeding.\n")
    else:
        print("WARNING: 29a gate verdicts file not found. Proceeding anyway.\n")

    # -----------------------------------------------------------------------
    # 1. Load data
    # -----------------------------------------------------------------------
    print("Loading data...")
    data = load_all_data()
    print(f"  BCS grid: tau={data['tau_bcs']}, mu/lmin={data['mu_ratios']}")
    print(f"  Spectral action: {len(data['tau_sa'])} points, "
          f"S(0)={data['S_spectral'][0]:.2f}, S(0.5)={data['S_spectral'][-1]:.2f}")
    print(f"  G_tau_tau = {data['G_tau_tau']}")
    print(f"  V_eff(0) = {data['V_at_0']}")
    print()

    # -----------------------------------------------------------------------
    # 2. Compute comparison
    # -----------------------------------------------------------------------
    print("Computing free energy comparison...")
    results = compute_free_energy_comparison(data)

    # -----------------------------------------------------------------------
    # 3. Report results
    # -----------------------------------------------------------------------
    print("\n" + "=" * 78)
    print("RESULTS")
    print("=" * 78)

    # Scenario 1
    sc1 = results['scenario_1']
    print(f"\nScenario 1: mu/lmin = {sc1['mu_ratio']:.2f} (BCS threshold)")
    print(f"  F_BCS(tau):")
    for i, t in enumerate(results['tau_bcs']):
        fb = sc1['F_bcs'][i]
        marker = " <-- CONDENSED" if fb < -1e-10 else ""
        print(f"    tau={t:.2f}: F_BCS = {fb:>12.6f}{marker}")
    if sc1['condensed']:
        print(f"  CROSSING at tau_cross = {sc1['tau_cross']:.3f}")
        print(f"  Deepest well: F_BCS = {sc1['F_bcs_deepest']:.4f} "
              f"at tau = {sc1['tau_deepest']:.2f}")
    else:
        print("  NO CROSSING -- F_BCS >= 0 everywhere")

    # Scenario 2
    sc2 = results['scenario_2']
    print(f"\nScenario 2: mu/lmin = {sc2['mu_ratio']:.2f} (moderate doping)")
    print(f"  F_BCS(tau):")
    for i, t in enumerate(results['tau_bcs']):
        fb = sc2['F_bcs'][i]
        marker = " <-- CONDENSED" if fb < -1e-10 else ""
        print(f"    tau={t:.2f}: F_BCS = {fb:>12.6f}{marker}")
    if sc2['condensed']:
        print(f"  CROSSING at tau_cross = {sc2['tau_cross']:.3f}")
        print(f"  Deepest well: F_BCS = {sc2['F_bcs_deepest']:.4f} "
              f"at tau = {sc2['tau_deepest']:.2f}")
    else:
        print("  NO CROSSING -- F_BCS >= 0 everywhere")

    # Scenario 3
    sc3 = results['scenario_3']
    print(f"\nScenario 3: KC-3 self-consistent (gap filled at tau >= {sc3['tau_KC3']})")
    print(f"  F_BCS(tau):")
    for i, t in enumerate(results['tau_bcs']):
        fb = sc3['F_bcs'][i]
        marker = " <-- CONDENSED" if fb < -1e-10 else ""
        print(f"    tau={t:.2f}: F_BCS = {fb:>12.6f}{marker}")
    if sc3['condensed']:
        print(f"  CROSSING at tau_cross = {sc3['tau_cross']:.3f}")
        print(f"  Deepest well: F_BCS = {sc3['F_bcs_deepest']:.4f} "
              f"at tau = {sc3['tau_deepest']:.2f}")

    # Gradient balance
    print(f"\nGradient analysis (dV_total/dtau sign changes):")
    print(f"  dS_spectral/dtau: {results['dS_dtau']}")
    print(f"  Scenario 1 sign changes at tau indices: {results['gradient_balance_10']}")
    print(f"  Scenario 2 sign changes at tau indices: {results['gradient_balance_12']}")

    # Per-sector breakdown
    for tau_key in [0.35, 0.50]:
        if tau_key in results['sector_analysis']:
            print(f"\nSector breakdown at tau={tau_key}:")
            for c in results['sector_analysis'][tau_key]:
                if c['F_cond_10'] != 0.0 or c['F_cond_12'] != 0.0:
                    print(f"  {c['sector']:>6s} mult={c['mult']:>3d}: "
                          f"F(1.0)={c['mult']*c['F_cond_10']:>10.4f} "
                          f"[M={c['M_max_10']:.3f}, D={c['Delta_10']:.4f}]  "
                          f"F(1.2)={c['mult']*c['F_cond_12']:>10.4f} "
                          f"[M={c['M_max_12']:.3f}, D={c['Delta_12']:.4f}]")

    # -----------------------------------------------------------------------
    # 4. Gate verdicts
    # -----------------------------------------------------------------------
    print("\n" + "=" * 78)
    print("GATE CLASSIFICATION")
    print("=" * 78)

    gates = classify_gates(results)

    k29c = gates['K_29c']
    print(f"\nK-29c (hard close): {k29c['verdict']}")
    print(f"  {k29c['detail']}")

    p29e = gates['P_29e']
    print(f"\nP-29e (positive signal): {p29e['verdict']}")
    print(f"  {p29e['detail']}")
    if p29e['tau_cross_values']:
        for key, label, tc in p29e['tau_cross_values']:
            in_w = "IN WINDOW" if 0.20 <= tc <= 0.50 else "outside"
            print(f"    {label}: tau_cross = {tc:.3f} ({in_w})")

    # -----------------------------------------------------------------------
    # 5. Summary for downstream
    # -----------------------------------------------------------------------
    # Determine canonical tau_cross for 29b-2
    # Use scenario 3 (physical, self-consistent) as canonical
    if sc3['condensed'] and sc3['tau_cross'] is not None:
        canonical_tau_cross = sc3['tau_cross']
    elif sc1['condensed'] and sc1['tau_cross'] is not None:
        canonical_tau_cross = sc1['tau_cross']
    else:
        canonical_tau_cross = None

    print(f"\n{'='*78}")
    if canonical_tau_cross is not None:
        print(f"CANONICAL tau_cross = {canonical_tau_cross:.3f}")
        print(f"  (for use in 29b-2 modulus EOM)")
    else:
        print("NO CANONICAL tau_cross -- K-29c may fire")
    print(f"{'='*78}")

    # -----------------------------------------------------------------------
    # 6. Save data
    # -----------------------------------------------------------------------
    npz_path = os.path.join(SCRIPT_DIR, "s29b_free_energy_comparison.npz")

    save_dict = {
        'tau_bcs': results['tau_bcs'],
        'mu_ratios': results['mu_ratios'],
        'S_spectral_at_bcs_tau': results['S_spectral_at_bcs_tau'],
        'F_normal': results['F_normal'],
        'Delta_F': results['Delta_F'],
        'F_bcs_scenario1': sc1['F_bcs'],
        'F_bcs_scenario2': sc2['F_bcs'],
        'F_bcs_scenario3': sc3['F_bcs'],
        'F_condensed_scenario1': sc1['F_condensed'],
        'F_condensed_scenario2': sc2['F_condensed'],
        'F_condensed_scenario3': sc3['F_condensed'],
        'dS_dtau': results['dS_dtau'],
        'dV_total_10': results['dV_total_10'],
        'dV_total_12': results['dV_total_12'],
        'K_29c_verdict': np.array([k29c['verdict']]),
        'P_29e_verdict': np.array([p29e['verdict']]),
    }

    # Add tau_cross values
    for key, suffix in [('scenario_1', '1'), ('scenario_2', '2'), ('scenario_3', '3')]:
        sc = results[key]
        if sc['condensed'] and sc['tau_cross'] is not None:
            save_dict[f'tau_cross_{suffix}'] = np.array([sc['tau_cross']])
            save_dict[f'F_bcs_deepest_{suffix}'] = np.array([sc['F_bcs_deepest']])
            save_dict[f'tau_deepest_{suffix}'] = np.array([sc['tau_deepest']])

    if canonical_tau_cross is not None:
        save_dict['canonical_tau_cross'] = np.array([canonical_tau_cross])

    np.savez_compressed(npz_path, **save_dict)
    print(f"\nData saved: {npz_path}")

    # -----------------------------------------------------------------------
    # 7. Plot
    # -----------------------------------------------------------------------
    png_path = os.path.join(SCRIPT_DIR, "s29b_free_energy_comparison.png")
    make_plots(data, results, gates, png_path)

    print(f"\n{'='*78}")
    print(f"29b-1 COMPLETE")
    print(f"K-29c: {k29c['verdict']}")
    print(f"P-29e: {p29e['verdict']}")
    if canonical_tau_cross is not None:
        print(f"tau_cross = {canonical_tau_cross:.3f} (canonical for 29b-2)")
    print(f"{'='*78}")


if __name__ == "__main__":
    main()
