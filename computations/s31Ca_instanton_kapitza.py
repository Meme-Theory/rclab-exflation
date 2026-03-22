"""
Instanton-Driven V_Kapitza: Replace Hessian Frequencies with Instanton Rates.

K-1 (Session 31Ba) showed that V_Kapitza has no interior minimum at the
physical Hessian frequencies omega^2 = T3 (8.326) and T4 (9.893), but
the extended scan found a sharp phase transition: minima APPEAR for
omega^2 < 5-8. The instanton gas from I-1 provides effective frequencies
omega_eff^2 = Gamma_inst^2 in the range ~0.3 to ~50, depending on the
coupling ratio r = alpha_YM / alpha_grav.

This script recomputes V_Kapitza using Gamma_inst(tau) as the effective
frequency. Two key refinements over K-1:

  1. TAU-DEPENDENT omega: The instanton rate Gamma_inst varies with tau
     (peaking at tau ~ 0.18). The Kapitza correction at each tau uses
     the LOCAL instanton rate, not a global constant.

  2. FULL COUPLING SCAN: All 6 coupling ratios r = {0.1, 0.3, 0.5, 1.0,
     2.0, 5.0} are tested. The soft-mode regime (r > 2) is where minima
     are expected.

Mathematical formula:
  V_Kap(tau; A) = V_avg(tau; A) + <(dV/deps)^2>(tau; A) / (4 * omega_eff(tau)^2)

  where omega_eff(tau) = Gamma_inst(tau; r) from the instanton gas.

  When omega_eff^2 is tau-dependent, the Kapitza correction is no longer
  a simple rescaling of the constant-omega case. The correction is LARGER
  at tau values where Gamma_inst is small (soft regions), creating
  position-dependent enhancement that can preferentially lift the
  potential at certain tau values.

Input:
  - s31Ba_kapitza_gate.npz (V_avg, V_corr at T3 for each A)
  - s31Ba_instanton_kapitza.npz (Gamma_inst at 6 coupling ratios)

Output:
  - s31Ca_instanton_kapitza.{npz,png}

Gate: If a minimum appears near tau ~ 0.18, this is the first positive
signal from a pre-registered dynamical gate in the project's history.
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os

ROOT = r"C:\sandbox\Ainulindale Exflation"
T0 = os.path.join(ROOT, "tier0-computation")

# ── Load data ────────────────────────────────────────────────────────────
print("Loading data...")
dk = np.load(os.path.join(T0, "s31Ba_kapitza_gate.npz"), allow_pickle=True)
di = np.load(os.path.join(T0, "s31Ba_instanton_kapitza.npz"), allow_pickle=True)

tau_fine = dk['tau_fine']          # (201,) in [0.01, 0.59]
V_jensen = dk['V_jensen']         # (201,) V_total along Jensen (eps=0)
omega_sq_T3 = float(dk['omega_sq_T3'])

tau_inst = di['tau']               # (201,) same grid
coupling_ratios = di['coupling_ratios']  # [0.1, 0.3, 0.5, 1.0, 2.0, 5.0]

# Verify grids match
assert np.allclose(tau_fine, tau_inst), "Tau grids do not match!"
print(f"  tau: [{tau_fine[0]:.3f}, {tau_fine[-1]:.3f}], n={len(tau_fine)}")
print(f"  omega_sq_T3 = {omega_sq_T3:.4f}")
print(f"  Coupling ratios: {coupling_ratios}")

# Amplitudes to scan
A_values = [0.02, 0.05, 0.08, 0.10, 0.12, 0.15]
A_strs = ['0p02', '0p05', '0p08', '0p10', '0p12', '0p15']


def find_interior_minima(tau_arr, V_arr, tau_lo=0.05, tau_hi=0.55):
    """Find interior minima via sign change of numerical gradient."""
    dV = np.gradient(V_arr, tau_arr)
    d2V = np.gradient(dV, tau_arr)

    mask_interior = (tau_arr > tau_lo) & (tau_arr < tau_hi)
    idx_int = np.where(mask_interior)[0]
    results = []

    for k in range(len(idx_int) - 1):
        j = idx_int[k]
        j1 = idx_int[k + 1]
        if dV[j] < 0 and dV[j1] > 0:
            frac = -dV[j] / (dV[j1] - dV[j])
            tau_min = tau_arr[j] + frac * (tau_arr[j1] - tau_arr[j])
            V_min = V_arr[j] + frac * (V_arr[j1] - V_arr[j])
            d2V_min = d2V[j] + frac * (d2V[j1] - d2V[j])
            results.append((tau_min, V_min, d2V_min))

    return results


# ── Extract raw gradient-squared from K-1 data ──────────────────────────
# V_corr(stored) = <(dV/deps)^2> / (4 * omega_sq_T3)
# So <(dV/deps)^2> = V_corr(stored) * 4 * omega_sq_T3
print("\nExtracting gradient-squared profiles...")
V_avg_by_A = {}
grad_sq_by_A = {}

for A, A_str in zip(A_values, A_strs):
    V_avg = dk[f'V_avg_T3_A{A_str}']
    V_corr_T3 = dk[f'V_corr_T3_A{A_str}']
    grad_sq = V_corr_T3 * 4.0 * omega_sq_T3  # = <(dV/deps)^2>
    V_avg_by_A[A] = V_avg
    grad_sq_by_A[A] = grad_sq
    print(f"  A={A:.2f}: <(dV/deps)^2> range = [{grad_sq.min():.4f}, {grad_sq.max():.4f}]")


# ── Load instanton rates ────────────────────────────────────────────────
r_strs = ['0p1', '0p3', '0p5', '1p0', '2p0', '5p0']
Gamma_inst = {}
for r, r_str in zip(coupling_ratios, r_strs):
    Gamma_inst[r] = di[f'Gamma_inst_r{r_str}']

print("\nInstanton effective frequencies omega_eff^2 = Gamma^2 at tau=0.18:")
for r in coupling_ratios:
    idx_018 = np.argmin(np.abs(tau_fine - 0.18))
    g = Gamma_inst[r][idx_018]
    print(f"  r={r:.1f}: Gamma={g:.4f}, omega_eff^2={g**2:.3f}")


# ── Main computation ─────────────────────────────────────────────────────
print("\n" + "=" * 70)
print("INSTANTON-DRIVEN V_KAPITZA COMPUTATION")
print("=" * 70)

all_results = []

for r in coupling_ratios:
    gamma = Gamma_inst[r]
    omega_eff_sq = gamma**2  # tau-dependent effective frequency

    # Regularize: where gamma is very small, omega_eff^2 -> 0 and
    # the correction diverges. Clamp to a minimum frequency.
    omega_eff_sq_safe = np.maximum(omega_eff_sq, 0.01)

    print(f"\n--- Coupling ratio r = {r:.1f} ---")
    print(f"  omega_eff^2 range: [{omega_eff_sq.min():.4f}, {omega_eff_sq.max():.4f}]")
    print(f"  omega_eff^2 at tau=0.18: {omega_eff_sq[np.argmin(np.abs(tau_fine-0.18))]:.4f}")

    for A, A_str in zip(A_values, A_strs):
        V_avg = V_avg_by_A[A]
        grad_sq = grad_sq_by_A[A]

        # Tau-dependent Kapitza correction
        V_corr_inst = grad_sq / (4.0 * omega_eff_sq_safe)
        V_kap_inst = V_avg + V_corr_inst

        # Find minima
        minima = find_interior_minima(tau_fine, V_kap_inst)

        corr_max = V_corr_inst.max()
        V_range = V_kap_inst.max() - V_kap_inst.min()

        result = {
            'r': r,
            'A': A,
            'V_kap': V_kap_inst.copy(),
            'V_avg': V_avg.copy(),
            'V_corr': V_corr_inst.copy(),
            'minima': minima,
            'corr_max': corr_max,
            'V_range': V_range,
        }
        all_results.append(result)

        if len(minima) > 0:
            for tm, vm, d2vm in minima:
                # Get phi_30 and sin2_B at minimum from grid data
                # (Load grid data for cross-reference)
                print(f"  A={A:.2f}: *** MINIMUM *** at tau*={tm:.4f}, "
                      f"d2V/dtau2={d2vm:.4f}, "
                      f"corr_max/V_range={corr_max/V_range:.4f}")
        else:
            ratio = corr_max / V_range if V_range > 0 else 0
            if A == 0.15:
                print(f"  A={A:.2f}: No minimum. corr/range={ratio:.4f}")


# ── Also run constant-omega comparison at instanton frequencies ──────────
# This uses a GLOBAL omega^2 (evaluated at tau=0.18), not tau-dependent
print("\n" + "=" * 70)
print("COMPARISON: CONSTANT omega_eff^2 (evaluated at tau=0.18)")
print("=" * 70)

const_results = []
A_test = 0.15
grad_sq = grad_sq_by_A[A_test]
V_avg = V_avg_by_A[A_test]

for r in coupling_ratios:
    idx_018 = np.argmin(np.abs(tau_fine - 0.18))
    omega_eff_sq_const = Gamma_inst[r][idx_018]**2

    if omega_eff_sq_const < 0.01:
        omega_eff_sq_const = 0.01  # same regularization

    V_corr_const = grad_sq / (4.0 * omega_eff_sq_const)
    V_kap_const = V_avg + V_corr_const

    minima = find_interior_minima(tau_fine, V_kap_const)

    result = {
        'r': r,
        'omega_sq': omega_eff_sq_const,
        'V_kap': V_kap_const.copy(),
        'V_corr': V_corr_const.copy(),
        'minima': minima,
    }
    const_results.append(result)

    if len(minima) > 0:
        for tm, vm, d2vm in minima:
            print(f"  r={r:.1f} (omega^2={omega_eff_sq_const:.3f}): "
                  f"*** MINIMUM *** at tau*={tm:.4f}, d2V={d2vm:.4f}")
    else:
        corr_max = V_corr_const.max()
        V_range = V_kap_const.max() - V_kap_const.min()
        ratio = corr_max / V_range if V_range > 0 else 0
        print(f"  r={r:.1f} (omega^2={omega_eff_sq_const:.3f}): "
              f"No minimum. corr/range={ratio:.4f}")


# ── Detailed analysis for the most promising case ───────────────────────
print("\n" + "=" * 70)
print("DETAILED ANALYSIS: Best cases")
print("=" * 70)

# Find all configurations with minima
configs_with_minima = [r for r in all_results if len(r['minima']) > 0]
const_with_minima = [r for r in const_results if len(r['minima']) > 0]

print(f"\n  Tau-dependent omega: {len(configs_with_minima)} configurations with minima "
      f"(out of {len(all_results)} total)")
print(f"  Constant omega:     {len(const_with_minima)} configurations with minima "
      f"(out of {len(const_results)} total)")

if configs_with_minima:
    print("\n  Tau-dependent omega minima:")
    for res in configs_with_minima:
        for tm, vm, d2vm in res['minima']:
            # Evaluate instanton frequency at the minimum
            idx_min = np.argmin(np.abs(tau_fine - tm))
            gamma_at_min = Gamma_inst[res['r']][idx_min]
            omega_sq_at_min = gamma_at_min**2
            print(f"    r={res['r']:.1f}, A={res['A']:.2f}: "
                  f"tau*={tm:.4f}, d2V={d2vm:.4f}, "
                  f"omega_eff^2(tau*)={omega_sq_at_min:.4f}, "
                  f"Gamma(tau*)={gamma_at_min:.4f}")

if const_with_minima:
    print("\n  Constant omega minima:")
    for res in const_with_minima:
        for tm, vm, d2vm in res['minima']:
            print(f"    r={res['r']:.1f}, omega^2={res['omega_sq']:.3f}: "
                  f"tau*={tm:.4f}, d2V={d2vm:.4f}")

# Cross-reference with K-1 extended scan results
print("\n  K-1 reference (from 31Ba extended scan at constant omega, A=0.15):")
print("    omega^2=8.326 (T3): No minimum")
print("    omega^2=5.0: Minimum at tau*=0.165, phi_30=1.529, sin2_B=0.608")
print("    omega^2=2.0: Minimum at tau*=0.197, phi_30=1.521, sin2_B=0.577")
print("    omega^2=1.0: Minimum at tau*=0.201, phi_30=1.520, sin2_B=0.574")
print("    omega^2=0.5: Minimum at tau*=0.524, phi_30=1.354, sin2_B=0.269")


# ── Gate assessment ──────────────────────────────────────────────────────
print("\n" + "=" * 70)
print("INSTANTON-KAPITZA GATE ASSESSMENT")
print("=" * 70)

any_minimum_near_018 = False
best_near_018 = None

for res in all_results + const_results:
    for tm, vm, d2vm in res.get('minima', []):
        if 0.10 < tm < 0.30:  # "near tau ~ 0.18"
            any_minimum_near_018 = True
            if best_near_018 is None or abs(tm - 0.18) < abs(best_near_018[0] - 0.18):
                best_near_018 = (tm, vm, d2vm, res)

any_minimum_anywhere = len(configs_with_minima) > 0 or len(const_with_minima) > 0

if any_minimum_near_018:
    tm, vm, d2vm, res = best_near_018
    verdict = "FIRES"
    verdict_detail = (f"Interior minimum at tau*={tm:.4f} (d2V={d2vm:.4f}) "
                       f"with r={res['r']:.1f}, A={res.get('A', 0.15):.2f}. "
                       f"First positive dynamical signal.")
elif any_minimum_anywhere:
    # Get the closest minimum to 0.18
    all_minima = []
    for res in all_results + const_results:
        for tm, vm, d2vm in res.get('minima', []):
            all_minima.append((tm, vm, d2vm, res))
    if all_minima:
        best_any = min(all_minima, key=lambda x: abs(x[0] - 0.18))
        tm, vm, d2vm, res = best_any
        verdict = "PARTIAL"
        verdict_detail = (f"Interior minimum found at tau*={tm:.4f} "
                           f"(r={res['r']:.1f}), but not near tau~0.18. "
                           f"Distance: |tau*-0.18| = {abs(tm-0.18):.3f}")
    else:
        verdict = "DOES NOT FIRE"
        verdict_detail = "No interior minimum at any tested configuration."
else:
    verdict = "DOES NOT FIRE"
    verdict_detail = "No interior minimum at any tested configuration."

print(f"\n  Verdict: {verdict}")
print(f"  Detail: {verdict_detail}")


# ── Save ─────────────────────────────────────────────────────────────────
save_dict = {
    'tau_fine': tau_fine,
    'V_jensen': V_jensen,
    'coupling_ratios': coupling_ratios,
    'A_values': np.array(A_values),
    'omega_sq_T3': np.array(omega_sq_T3),
    'verdict': np.array(verdict),
}

# Save tau-dependent V_Kapitza for key cases
for res in all_results:
    r = res['r']
    A = res['A']
    key = f"r{r:.1f}_A{A:.2f}".replace('.', 'p')
    save_dict[f'V_kap_{key}'] = res['V_kap']
    save_dict[f'V_corr_{key}'] = res['V_corr']

# Save constant-omega V_Kapitza
for res in const_results:
    r = res['r']
    key = f"const_r{r:.1f}".replace('.', 'p')
    save_dict[f'V_kap_{key}'] = res['V_kap']
    save_dict[f'V_corr_{key}'] = res['V_corr']

# Save instanton frequencies
for r, r_str in zip(coupling_ratios, r_strs):
    save_dict[f'Gamma_inst_r{r_str}'] = Gamma_inst[r]
    save_dict[f'omega_eff_sq_r{r_str}'] = Gamma_inst[r]**2

outfile = os.path.join(T0, "s31Ca_instanton_kapitza.npz")
np.savez_compressed(outfile, **save_dict)
print(f"\nSaved: {outfile}")


# ── Plotting ─────────────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 3, figsize=(18, 10))

# Normalize all V_kap by subtracting V_kap[0] for visibility
V0 = V_jensen[0]

# Panel 1: Tau-dependent omega, A=0.15, all coupling ratios
ax = axes[0, 0]
V_ref = V_jensen - V0
ax.plot(tau_fine, V_ref, 'k-', lw=2.5, label='V_total (static)')
A_plot = 0.15
for r, r_str, color in zip(coupling_ratios,
                             r_strs,
                             ['navy', 'blue', 'deepskyblue', 'green', 'orange', 'red']):
    for res in all_results:
        if res['r'] == r and res['A'] == A_plot:
            V_kap = res['V_kap'] - V0
            ax.plot(tau_fine, V_kap, '-', color=color, lw=1.5,
                     label=f'r={r:.1f}')
            for tm, vm, d2vm in res['minima']:
                ax.plot(tm, vm - V0, 'o', color=color, ms=10, zorder=5,
                         markeredgecolor='k')
            break
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$V - V(\tau_{min})$')
ax.set_title(f'Tau-dependent $\\omega_{{eff}}$, A={A_plot}')
ax.legend(fontsize=7, ncol=2)
ax.grid(True, alpha=0.3)

# Panel 2: Constant omega, A=0.15, all coupling ratios
ax = axes[0, 1]
ax.plot(tau_fine, V_ref, 'k-', lw=2.5, label='V_total (static)')
for res, color in zip(const_results,
                       ['navy', 'blue', 'deepskyblue', 'green', 'orange', 'red']):
    V_kap = res['V_kap'] - V0
    ax.plot(tau_fine, V_kap, '-', color=color, lw=1.5,
             label=f'r={res["r"]:.1f} ($\\omega^2$={res["omega_sq"]:.2f})')
    for tm, vm, d2vm in res['minima']:
        ax.plot(tm, vm - V0, 'o', color=color, ms=10, zorder=5,
                 markeredgecolor='k')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$V - V(\tau_{min})$')
ax.set_title(f'Constant $\\omega_{{eff}}(\\tau=0.18)$, A={A_plot}')
ax.legend(fontsize=6, ncol=2)
ax.grid(True, alpha=0.3)

# Panel 3: Correction term magnitude for tau-dep vs constant
ax = axes[0, 2]
for r, color in zip([1.0, 2.0, 5.0], ['green', 'orange', 'red']):
    for res in all_results:
        if res['r'] == r and res['A'] == 0.15:
            ax.plot(tau_fine, res['V_corr'], '-', color=color, lw=1.5,
                     label=f'r={r} (tau-dep)')
            break
    for res in const_results:
        if res['r'] == r:
            ax.plot(tau_fine, res['V_corr'], '--', color=color, lw=1.5,
                     label=f'r={r} (const)')
            break
ax.set_xlabel(r'$\tau$')
ax.set_ylabel('Kapitza correction')
ax.set_title('Correction: tau-dep vs constant')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)

# Panel 4: Effective omega^2 vs tau for each coupling ratio
ax = axes[1, 0]
for r, r_str, color in zip(coupling_ratios, r_strs,
                             ['navy', 'blue', 'deepskyblue', 'green', 'orange', 'red']):
    omega_sq = Gamma_inst[r]**2
    ax.semilogy(tau_fine, omega_sq, '-', color=color, lw=1.5,
                 label=f'r={r:.1f}')
ax.axhline(omega_sq_T3, color='gray', ls='--', lw=1, label=f'T3={omega_sq_T3:.1f}')
ax.axhline(5.0, color='purple', ls=':', lw=1, label=r'$\omega_{crit}^2 \sim 5$')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$\omega_{eff}^2 = \Gamma_{inst}^2$')
ax.set_title('Instanton effective frequency')
ax.legend(fontsize=7, ncol=2)
ax.grid(True, alpha=0.3)

# Panel 5: Amplitude scan at best coupling ratio
ax = axes[1, 1]
# Find best r (most minima or closest minimum to 0.18)
best_r = 5.0  # expect this is the softest
ax.plot(tau_fine, V_ref, 'k-', lw=2.5, label='V_total (static)')
for A, color in zip(A_values, ['navy', 'blue', 'deepskyblue', 'green', 'orange', 'red']):
    for res in all_results:
        if res['r'] == best_r and res['A'] == A:
            V_kap = res['V_kap'] - V0
            ax.plot(tau_fine, V_kap, '-', color=color, lw=1.5,
                     label=f'A={A:.2f}')
            for tm, vm, d2vm in res['minima']:
                ax.plot(tm, vm - V0, 'o', color=color, ms=8, zorder=5,
                         markeredgecolor='k')
            break
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$V - V(\tau_{min})$')
ax.set_title(f'Tau-dep $\\omega_{{eff}}$, r={best_r} (softest)')
ax.legend(fontsize=7)
ax.grid(True, alpha=0.3)

# Panel 6: Gradient comparison for best case
ax = axes[1, 2]
dV_jensen = np.gradient(V_jensen, tau_fine)
ax.plot(tau_fine, dV_jensen, 'k-', lw=2, label='dV_static/dtau')
for r, color in zip([2.0, 5.0], ['orange', 'red']):
    for res in all_results:
        if res['r'] == r and res['A'] == 0.15:
            dV_kap = np.gradient(res['V_kap'], tau_fine)
            ax.plot(tau_fine, dV_kap, '-', color=color, lw=1.5,
                     label=f'dV_Kap/dtau (r={r})')
            break
ax.axhline(0, color='gray', ls='-', lw=0.5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$dV/d\tau$')
ax.set_title('Gradient: zero crossing = minimum')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

plt.suptitle(f'Instanton-Driven V_Kapitza | Verdict: {verdict}',
              fontsize=14, fontweight='bold')
plt.tight_layout()

plotfile = os.path.join(T0, "s31Ca_instanton_kapitza.png")
plt.savefig(plotfile, dpi=150, bbox_inches='tight')
plt.close()
print(f"Saved: {plotfile}")

print(f"\n{'='*70}")
print(f"INSTANTON-KAPITZA COMPLETE. Verdict: {verdict}")
print(f"  {verdict_detail}")
print(f"{'='*70}")
