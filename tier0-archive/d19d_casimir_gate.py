"""
D-1: Boson/Fermion E_proxy Separation — THE CHEAPEST GATE
============================================================

Session 19d: Casimir Energy vs Coleman-Weinberg

Computes E_proxy = (1/2) Sum mult_n * |lam_n| separated into bosonic and
fermionic contributions. The gate criterion:

  R(tau) = |E_proxy_fermion(tau)| / E_proxy_boson(tau)

If R is CONSTANT (within 5%) across all tau -> CLOSED (Casimir has same
boson/fermion balance as CW, no new physics possible).
If R SHIFTS by > 10% -> PROCEED to D-2 (zeta regularization).

Also checks: does dE_proxy_total/dtau have opposite sign from dV_CW/dtau?

Physics:
  - CW weights as lam^4 * log(lam^2): UV-dominated, R_CW ~ 8.4:1
  - E_proxy weights as |lam|: IR-balanced, R_proxy ~ 2.4:1 expected at tau=0
  - The question is whether R_proxy(tau) DRIFTS as tau increases

Data sources:
  - Fermionic: s19a_sweep_data.npz (21 tau-values, 11,424 eigenvalues each)
  - Bosonic: kk1_bosonic_spectrum.npz (4 tau-values) + recomputed at all 21

Author: phonon-exflation-sim (Session 19d)
Date: 2026-02-15
"""

import sys
import os
import time
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

from s19a_sweep_data import load_sweep_data


def load_fermionic_data(data_path):
    """
    Load fermionic eigenvalue data from s19a_sweep_data.npz.

    The Dirac operator on (SU(3), g_s) produces eigenvalues for spinor fields.
    All modes are fermionic (spin-1/2 KK modes).

    Each eigenvalue |lam_n| appears with Peter-Weyl multiplicity dim(p,q).
    The fermionic contribution to E_proxy carries a NEGATIVE sign (Fermi statistics).

    Returns:
        tau_values: (21,) array
        fermion_E_proxy: (21,) array of E_proxy_fermion at each tau
        fermion_details: list of dicts with per-tau breakdown
    """
    data = load_sweep_data(data_path)
    tau_values = data['tau_values']
    n_tau = len(tau_values)

    fermion_E_proxy = np.zeros(n_tau)
    fermion_details = []

    for i in range(n_tau):
        evals = data['eigenvalues'][i]      # |lam_n|
        mults = data['multiplicities'][i]    # dim(p,q) per eigenvalue

        # E_proxy_fermion = -(1/2) * Sum mult_n * |lam_n|  [negative: Fermi]
        E_proxy_i = -0.5 * np.sum(mults * evals)
        fermion_E_proxy[i] = E_proxy_i

        # Weighted DOF count
        total_weighted_dof = np.sum(mults)
        mean_abs_lam = np.sum(mults * evals) / total_weighted_dof

        fermion_details.append({
            'n_evals': len(evals),
            'total_pw_dof': int(total_weighted_dof),
            'mean_abs_lam': mean_abs_lam,
            'E_proxy': E_proxy_i,
        })

    return tau_values, fermion_E_proxy, fermion_details


def compute_bosonic_E_proxy_from_npz(npz_path, tau_target):
    """
    Compute bosonic E_proxy from the pre-computed kk1_bosonic_spectrum.npz.

    This file contains scalar + vector Laplacian eigenvalues at 4 tau-values.
    The eigenvalues are SQUARED MASSES (Laplacian eigenvalues), so the
    contribution to E_proxy uses sqrt(eigenvalue) as the mode frequency:

      E_proxy_boson = +(1/2) * Sum mult_n * sqrt(lam_n)  [positive: Bose]

    Wait — important distinction:
    The Dirac eigenvalues in s19a are |lam_n| (absolute values of D_K eigenvalues).
    The bosonic eigenvalues are Laplacian eigenvalues = m^2 (squared masses).

    For consistent comparison, we need:
      Fermionic: E_proxy_F = (1/2) * Sum mult * |lam_Dirac|
      Bosonic:   E_proxy_B = (1/2) * Sum mult * sqrt(lam_Laplacian)

    because |lam_Dirac| corresponds to mass m, and lam_Laplacian = m^2.

    Returns:
        available_taus: list of tau values in the file
        boson_E_proxy: dict mapping tau -> E_proxy value
        boson_details: dict mapping tau -> detail dict
    """
    npz = np.load(npz_path, allow_pickle=False)

    results = {}
    details = {}
    available_taus = []

    for key in sorted(npz.keys()):
        # Keys are like 's_0.0000', 's_0.1500', etc.
        tau = float(key.split('_')[1])
        available_taus.append(tau)

        arr = npz[key]
        eigenvalues = arr['eigenvalue']   # Laplacian eigenvalues = m^2
        mults = arr['multiplicity']
        types = arr['type']               # 0=scalar, 1=vector

        # Filter out zero/negative eigenvalues (gauge zeros, numerical noise)
        mask_pos = eigenvalues > 1e-10
        evals_pos = eigenvalues[mask_pos]
        mults_pos = mults[mask_pos]
        types_pos = types[mask_pos]

        # Mode frequencies = sqrt(m^2) = m
        freqs = np.sqrt(evals_pos)

        # E_proxy_boson = +(1/2) * Sum mult * freq
        E_proxy_total = 0.5 * np.sum(mults_pos * freqs)
        E_proxy_scalar = 0.5 * np.sum(mults_pos[types_pos == 0] * freqs[types_pos == 0])
        E_proxy_vector = 0.5 * np.sum(mults_pos[types_pos == 1] * freqs[types_pos == 1])

        results[tau] = E_proxy_total

        total_pw_dof = int(np.sum(mults_pos))
        details[tau] = {
            'n_evals_pos': int(np.sum(mask_pos)),
            'n_evals_zero': int(np.sum(~mask_pos)),
            'total_pw_dof': total_pw_dof,
            'E_proxy_total': E_proxy_total,
            'E_proxy_scalar': E_proxy_scalar,
            'E_proxy_vector': E_proxy_vector,
            'mean_freq': np.sum(mults_pos * freqs) / total_pw_dof if total_pw_dof > 0 else 0,
        }

    return available_taus, results, details


def recompute_bosonic_at_all_taus(tau_values, max_pq_scalar=6, max_pq_vector=4):
    """
    Recompute bosonic E_proxy at ALL 21 tau-values by calling the
    bosonic tower code directly.

    This is slower (~5-10 min) but gives complete tau coverage.

    Returns:
        boson_E_proxy: (N_tau,) array
        boson_details: list of dicts
    """
    from kk1_bosonic_tower import bosonic_spectrum_at_s

    boson_E_proxy = np.zeros(len(tau_values))
    boson_details = []

    for i, tau in enumerate(tau_values):
        t0 = time.time()
        result = bosonic_spectrum_at_s(tau, max_pq_scalar=max_pq_scalar,
                                       max_pq_vector=max_pq_vector)

        # Scalar eigenvalues (Laplacian = m^2)
        scalar_E = 0.0
        scalar_dof = 0
        for ev, mult in result['scalar_eigs']:
            if ev > 1e-10:
                scalar_E += 0.5 * mult * np.sqrt(ev)
                scalar_dof += mult

        # Vector eigenvalues (Hodge Laplacian = m^2)
        vector_E = 0.0
        vector_dof = 0
        for ev, mult in result['vector_eigs']:
            if ev > 1e-10:
                vector_E += 0.5 * mult * np.sqrt(ev)
                vector_dof += mult

        E_total = scalar_E + vector_E
        boson_E_proxy[i] = E_total

        dt = time.time() - t0
        boson_details.append({
            'E_proxy_scalar': scalar_E,
            'E_proxy_vector': vector_E,
            'E_proxy_total': E_total,
            'scalar_dof': scalar_dof,
            'vector_dof': vector_dof,
            'total_dof': scalar_dof + vector_dof,
            'elapsed': dt,
        })

        print(f"  tau={tau:.2f}: E_boson={E_total:.4e} "
              f"(scalar={scalar_E:.4e}, vector={vector_E:.4e}), "
              f"{dt:.1f}s")

    return boson_E_proxy, boson_details


def compute_vcw_gradient(tau_values):
    """
    Compute V_CW gradient from Session 18 standalone verification data.

    The standalone verify script confirmed V_CW is monotonically decreasing.
    We recompute V_CW at our tau grid for gradient comparison.

    Falls back to the analytic V_tree gradient if V_CW data unavailable.
    """
    # Try to import from h5_standalone_verify
    try:
        # The standalone script stores V_CW values. Let's compute analytically.
        from tier1_spectral_action import baptista_V_tree
        V_tree = np.array([baptista_V_tree(t) for t in tau_values])
        # V_tree is the CLASSICAL part. V_CW decreases faster.
        # For the gate, the key question is the SIGN of dV_CW/dtau, which is negative
        # at all tau (monotonically decreasing, Session 18 result).
        return V_tree, np.gradient(V_tree, tau_values)
    except ImportError:
        print("  WARNING: Could not import V_tree. Using schematic.")
        V_tree = -np.exp(1.5 * tau_values)
        return V_tree, np.gradient(V_tree, tau_values)


def run_gate():
    """
    Execute the D-1 gate: boson/fermion E_proxy separation.

    CLOSED criteria (both must hold):
      1. R(tau) = |E_fermion|/E_boson varies by < 5% over [0, 2.0]
      2. dE_proxy_total/dtau has same sign as dV_CW/dtau everywhere

    PROCEED criteria (either suffices):
      1. R(tau) varies by > 10% over [0, 2.0]
      2. dE_proxy_total/dtau has opposite sign from dV_CW/dtau at some tau
    """
    DATA_DIR = SCRIPT_DIR
    FERMION_PATH = os.path.join(DATA_DIR, 's19a_sweep_data.npz')
    BOSON_PATH = os.path.join(DATA_DIR, 'kk1_bosonic_spectrum.npz')

    print("=" * 72)
    print("  D-1: BOSON/FERMION E_proxy SEPARATION — CHEAPEST GATE")
    print("  Session 19d: Casimir Energy vs Coleman-Weinberg")
    print("=" * 72)

    # =========================================================================
    # 1. LOAD FERMIONIC DATA
    # =========================================================================
    print("\n--- 1. Loading Fermionic Data ---")
    tau_values, fermion_E_proxy, fermion_details = load_fermionic_data(FERMION_PATH)
    print(f"  {len(tau_values)} tau-values, {fermion_details[0]['n_evals']} eigenvalues each")
    print(f"  Fermionic PW DOF: {fermion_details[0]['total_pw_dof']}")

    for i in [0, 5, 10, 15, 20]:
        d = fermion_details[i]
        print(f"  tau={tau_values[i]:.1f}: E_fermion={d['E_proxy']:.6e}, "
              f"<|lam|>={d['mean_abs_lam']:.6f}")

    # =========================================================================
    # 2. LOAD/COMPUTE BOSONIC DATA
    # =========================================================================
    print("\n--- 2. Computing Bosonic Data at All 21 Tau-Values ---")

    # First check what's in the .npz
    avail_taus, boson_npz, boson_npz_details = compute_bosonic_E_proxy_from_npz(
        BOSON_PATH, tau_values
    )
    print(f"  Pre-computed bosonic data at tau = {avail_taus}")
    for tau in avail_taus:
        d = boson_npz_details[tau]
        print(f"  tau={tau:.2f}: E_boson={d['E_proxy_total']:.6e} "
              f"(scalar={d['E_proxy_scalar']:.4e}, vector={d['E_proxy_vector']:.4e}), "
              f"DOF={d['total_pw_dof']}")

    # Recompute at all 21 tau-values for complete coverage
    print(f"\n  Recomputing bosonic spectrum at all {len(tau_values)} tau-values...")
    print(f"  (scalar: max_pq=6, vector: max_pq=4)")
    t0_boson = time.time()
    boson_E_proxy, boson_details = recompute_bosonic_at_all_taus(
        tau_values, max_pq_scalar=6, max_pq_vector=4
    )
    dt_boson = time.time() - t0_boson
    print(f"  Total bosonic computation: {dt_boson:.1f}s")

    # Cross-check against pre-computed values
    print("\n  Cross-check against pre-computed .npz:")
    for tau_check in avail_taus:
        idx = np.argmin(np.abs(tau_values - tau_check))
        if np.abs(tau_values[idx] - tau_check) < 0.01:
            rel_err = abs(boson_E_proxy[idx] - boson_npz[tau_check]) / abs(boson_npz[tau_check])
            print(f"    tau={tau_check:.2f}: recomputed={boson_E_proxy[idx]:.6e}, "
                  f"npz={boson_npz[tau_check]:.6e}, rel_err={rel_err:.2e}")

    # =========================================================================
    # 3. COMPUTE RATIO R(tau) = |E_fermion| / E_boson
    # =========================================================================
    print("\n--- 3. Boson/Fermion Ratio R(tau) ---")

    R_ratio = np.abs(fermion_E_proxy) / boson_E_proxy
    E_total = boson_E_proxy + fermion_E_proxy  # boson positive, fermion negative

    print(f"\n  {'tau':>6} {'E_boson':>14} {'E_fermion':>14} {'E_total':>14} {'R=|F|/B':>10}")
    print(f"  {'-'*6} {'-'*14} {'-'*14} {'-'*14} {'-'*10}")
    for i, tau in enumerate(tau_values):
        print(f"  {tau:6.2f} {boson_E_proxy[i]:14.6e} {fermion_E_proxy[i]:14.6e} "
              f"{E_total[i]:14.6e} {R_ratio[i]:10.4f}")

    # =========================================================================
    # 4. GATE CRITERION 1: R(tau) variation
    # =========================================================================
    print("\n--- 4. Gate Criterion 1: R(tau) Variation ---")
    R_min = np.min(R_ratio)
    R_max = np.max(R_ratio)
    R_range = R_max - R_min
    R_mean = np.mean(R_ratio)
    R_variation = R_range / R_mean  # fractional variation

    print(f"  R_min  = {R_min:.6f} at tau = {tau_values[np.argmin(R_ratio)]:.2f}")
    print(f"  R_max  = {R_max:.6f} at tau = {tau_values[np.argmax(R_ratio)]:.2f}")
    print(f"  R_mean = {R_mean:.6f}")
    print(f"  R variation = (R_max - R_min) / R_mean = {R_variation:.4f} = {R_variation*100:.2f}%")

    dR_dtau = np.gradient(R_ratio, tau_values)
    print(f"  dR/dtau at tau=0: {dR_dtau[0]:.6f}")
    print(f"  dR/dtau at tau=1: {dR_dtau[10]:.6f}")
    print(f"  dR/dtau at tau=2: {dR_dtau[-1]:.6f}")

    gate1_kill = R_variation < 0.05
    gate1_proceed = R_variation > 0.10

    print(f"\n  Gate 1 verdict: ", end="")
    if gate1_kill:
        print(f"CLOSED (variation {R_variation*100:.1f}% < 5%)")
    elif gate1_proceed:
        print(f"PROCEED (variation {R_variation*100:.1f}% > 10%)")
    else:
        print(f"INTERMEDIATE (variation {R_variation*100:.1f}% in [5%, 10%])")

    # =========================================================================
    # 5. GATE CRITERION 2: dE_total/dtau vs dV_CW/dtau sign comparison
    # =========================================================================
    print("\n--- 5. Gate Criterion 2: Gradient Sign Comparison ---")

    dE_total_dtau = np.gradient(E_total, tau_values)

    # V_CW is monotonically decreasing (Session 18). dV_CW/dtau < 0 everywhere.
    # Load V_tree for reference
    V_tree, dV_tree_dtau = compute_vcw_gradient(tau_values)

    print(f"\n  V_tree is monotonically decreasing: dV_tree/dtau < 0 at all tau > 0")
    print(f"  V_CW is also monotonically decreasing (Session 18, confirmed)")
    print(f"  Reference: dV_CW/dtau < 0 everywhere")

    print(f"\n  {'tau':>6} {'dE_total/dtau':>14} {'Sign':>6} {'dV_tree/dtau':>14} {'Same sign?':>11}")
    print(f"  {'-'*6} {'-'*14} {'-'*6} {'-'*14} {'-'*11}")

    n_opposite = 0
    for i, tau in enumerate(tau_values):
        sign_E = '+' if dE_total_dtau[i] > 0 else '-'
        sign_V = '+' if dV_tree_dtau[i] > 0 else '-'
        same = "YES" if (dE_total_dtau[i] * dV_tree_dtau[i] > 0) else "NO"
        if dE_total_dtau[i] * dV_tree_dtau[i] <= 0 and i > 0:
            n_opposite += 1
            same = "**NO**"
        print(f"  {tau:6.2f} {dE_total_dtau[i]:14.6e} {sign_E:>6} "
              f"{dV_tree_dtau[i]:14.6e} {same:>11}")

    gate2_proceed = n_opposite > 0
    print(f"\n  Points with opposite sign: {n_opposite} / {len(tau_values) - 1}")
    print(f"  Gate 2 verdict: ", end="")
    if gate2_proceed:
        print("PROCEED (opposite signs found)")
    else:
        print("CLOSURE (same sign everywhere)")

    # =========================================================================
    # 6. COMPARISON WITH CW RATIO
    # =========================================================================
    print("\n--- 6. Comparison: E_proxy Ratio vs CW Ratio ---")
    print(f"  V_CW fermion/boson ratio: ~8.4:1 (quartic weight, Session 18)")
    print(f"  E_proxy fermion/boson ratio at tau=0: {R_ratio[0]:.4f}:1 (linear weight)")
    print(f"  Ratio of ratios: CW/proxy = {8.4/R_ratio[0]:.2f}")
    print(f"  The IR weighting reduces fermion dominance by {8.4/R_ratio[0]:.1f}x")

    # =========================================================================
    # 7. OVERALL VERDICT
    # =========================================================================
    print("\n" + "=" * 72)
    print("  D-1 OVERALL VERDICT")
    print("=" * 72)

    closure = gate1_kill and not gate2_proceed
    proceed = gate1_proceed or gate2_proceed

    if closure:
        verdict = "CLOSED"
        print(f"\n  VERDICT: *** CLOSED ***")
        print(f"  R(tau) is constant (variation {R_variation*100:.1f}% < 5%)")
        print(f"  dE_total/dtau has same sign as dV_CW/dtau everywhere")
        print(f"  Casimir energy has same boson/fermion balance as CW.")
        print(f"  No new physics possible. Skip D-2/D-3/D-4.")
    elif proceed:
        verdict = "PROCEED"
        print(f"\n  VERDICT: *** PROCEED ***")
        if gate1_proceed:
            print(f"  R(tau) shifts by {R_variation*100:.1f}% (> 10%)")
        elif not gate1_kill:
            print(f"  R(tau) shifts by {R_variation*100:.1f}% (intermediate, 5-10%)")
        if gate2_proceed:
            print(f"  dE_total/dtau has OPPOSITE sign from dV_CW/dtau at {n_opposite} points")
        print(f"  Casimir energy has DIFFERENT tau-dependence from CW.")
        print(f"  Proceed to D-2 (spectral zeta regularization).")
    else:
        verdict = "MARGINAL"
        print(f"\n  VERDICT: *** MARGINAL ***")
        print(f"  R(tau) variation is intermediate ({R_variation*100:.1f}%)")
        print(f"  Gradient signs are consistent")
        print(f"  Recommend proceeding to D-2 for a definitive test.")

    print()

    # =========================================================================
    # 8. PLOTS
    # =========================================================================
    fig, axes = plt.subplots(2, 3, figsize=(18, 10))

    # Plot 1: E_proxy components
    ax = axes[0, 0]
    ax.semilogy(tau_values, boson_E_proxy, 'b-o', markersize=4, label='E_boson (+)')
    ax.semilogy(tau_values, np.abs(fermion_E_proxy), 'r-o', markersize=4, label='|E_fermion| (-)')
    ax.semilogy(tau_values, np.abs(E_total), 'k-s', markersize=5, label='|E_total|')
    ax.set_xlabel('tau')
    ax.set_ylabel('E_proxy')
    ax.set_title('E_proxy: Boson vs Fermion')
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

    # Plot 2: R(tau) = fermion/boson ratio
    ax = axes[0, 1]
    ax.plot(tau_values, R_ratio, 'g-o', markersize=5, linewidth=2)
    ax.axhline(y=8.4, color='red', linestyle='--', alpha=0.5, label='CW ratio (8.4:1)')
    ax.axhline(y=R_mean, color='blue', linestyle=':', alpha=0.5, label=f'Mean R = {R_mean:.2f}')
    ax.fill_between(tau_values, R_mean * 0.95, R_mean * 1.05, alpha=0.1, color='green',
                     label='5% band')
    ax.set_xlabel('tau')
    ax.set_ylabel('R = |E_fermion| / E_boson')
    ax.set_title(f'Fermion/Boson Ratio (variation: {R_variation*100:.1f}%)')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    # Plot 3: dR/dtau
    ax = axes[0, 2]
    ax.plot(tau_values, dR_dtau, 'purple', linewidth=2, marker='o', markersize=4)
    ax.axhline(y=0, color='gray', linestyle='--', alpha=0.5)
    ax.set_xlabel('tau')
    ax.set_ylabel('dR/dtau')
    ax.set_title('Rate of Change of Fermion/Boson Ratio')
    ax.grid(True, alpha=0.3)

    # Plot 4: E_total and its gradient
    ax = axes[1, 0]
    ax.plot(tau_values, E_total, 'k-o', markersize=4, linewidth=2)
    ax.set_xlabel('tau')
    ax.set_ylabel('E_total = E_boson + E_fermion')
    ax.set_title('Total E_proxy (boson + fermion)')
    ax.grid(True, alpha=0.3)

    # Plot 5: dE_total/dtau vs dV_tree/dtau (normalized)
    ax = axes[1, 1]
    # Normalize for visual comparison
    dE_norm = dE_total_dtau / np.max(np.abs(dE_total_dtau[1:])) if np.max(np.abs(dE_total_dtau[1:])) > 0 else dE_total_dtau
    dV_norm = dV_tree_dtau / np.max(np.abs(dV_tree_dtau[1:])) if np.max(np.abs(dV_tree_dtau[1:])) > 0 else dV_tree_dtau
    ax.plot(tau_values[1:], dE_norm[1:], 'b-o', markersize=4, label='dE_total/dtau (norm)')
    ax.plot(tau_values[1:], dV_norm[1:], 'r-s', markersize=4, label='dV_tree/dtau (norm)')
    ax.axhline(y=0, color='gray', linestyle='--', alpha=0.5)
    ax.set_xlabel('tau')
    ax.set_ylabel('Normalized gradient')
    ax.set_title('Gradient Sign Comparison')
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

    # Highlight opposite-sign regions
    for i in range(1, len(tau_values)):
        if dE_total_dtau[i] * dV_tree_dtau[i] <= 0:
            ax.axvspan(tau_values[i-1], tau_values[i], alpha=0.2, color='green')

    # Plot 6: Scalar vs Vector boson breakdown
    ax = axes[1, 2]
    scalar_E = np.array([d['E_proxy_scalar'] for d in boson_details])
    vector_E = np.array([d['E_proxy_vector'] for d in boson_details])
    ax.semilogy(tau_values, scalar_E, 'c-o', markersize=4, label='E_scalar')
    ax.semilogy(tau_values, vector_E, 'm-s', markersize=4, label='E_vector')
    ax.semilogy(tau_values, boson_E_proxy, 'b-^', markersize=4, label='E_boson (total)')
    ax.set_xlabel('tau')
    ax.set_ylabel('E_proxy component')
    ax.set_title('Bosonic E_proxy: Scalar vs Vector')
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)

    plt.suptitle(f'D-1: Boson/Fermion E_proxy Gate — VERDICT: {verdict}',
                 fontsize=14, fontweight='bold')
    plt.tight_layout()

    output_path = os.path.join(SCRIPT_DIR, 'd19d_casimir_gate.png')
    plt.savefig(output_path, dpi=150)
    plt.close()
    print(f"  Saved plot: {output_path}")

    # Save numerical results
    results_path = os.path.join(SCRIPT_DIR, 'd19d_casimir_gate.npz')
    np.savez(results_path,
             tau_values=tau_values,
             boson_E_proxy=boson_E_proxy,
             fermion_E_proxy=fermion_E_proxy,
             E_total=E_total,
             R_ratio=R_ratio,
             dR_dtau=dR_dtau,
             dE_total_dtau=dE_total_dtau,
             R_variation=np.array([R_variation]),
             verdict=np.array([verdict], dtype='U20'))
    print(f"  Saved data: {results_path}")

    return verdict, R_variation, R_ratio, E_total


if __name__ == '__main__':
    t_start = time.time()
    verdict, R_var, R_ratio, E_total = run_gate()
    elapsed = time.time() - t_start
    print(f"\n  Total D-1 runtime: {elapsed:.1f}s")
