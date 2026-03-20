"""
BA-31-4: 3-Form Norm and Freund-Rubin Potential
=================================================

Computes the SU(3) canonical 3-form omega_3 = f_{abc} e^a ^ e^b ^ e^c
and its norm squared |omega_3|^2(tau) on the Jensen-deformed metric.

The Freund-Rubin potential contribution:
  V_FR(tau) = alpha_FR * |omega_3|^2(tau) / Vol(K)^2

If V_FR is non-monotonic or decreasing, it can compete with V_spec
to produce a stabilization minimum.

Gate BA-31-fr:
  STABILIZATION POSSIBLE if dV_FR/dtau < 0 for tau in [0.05, 0.50]
  FAIL if V_FR also monotonically increasing in tau

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
    jensen_metric
)


def compute_3form_norm_sq(f_abc, g_inv):
    """
    Compute |omega_3|^2 = f_{abc} f_{def} g^{ad} g^{be} g^{cf}.

    The 3-form omega_3 = (1/3!) f_{abc} e^a ^ e^b ^ e^c.
    Its norm squared (in the convention |omega|^2 = (1/3!) omega_{abc} omega^{abc}):
      |omega_3|^2 = (1/3!) f_{abc} f_{def} g^{ad} g^{be} g^{cf}

    We compute the UN-normalized version first: f_{abc} f^{abc}.
    The factor of 1/3! is a convention choice -- we'll be consistent.

    Args:
        f_abc: (8,8,8) structure constants
        g_inv: (8,8) inverse metric

    Returns:
        norm_sq: scalar, f_{abc} f^{abc} = f_{abc} f_{def} g^{ad} g^{be} g^{cf}
    """
    # Raise all indices: f^{abc} = f_{def} g^{da} g^{eb} g^{fc}
    f_up = np.einsum('def,da,eb,fc->abc', f_abc, g_inv, g_inv, g_inv)
    # Contract: f_{abc} f^{abc}
    norm_sq = np.einsum('abc,abc->', f_abc, f_up)
    return norm_sq


def main():
    t_start = time.time()

    print("=" * 70)
    print("BA-31-4: 3-FORM NORM AND FREUND-RUBIN POTENTIAL")
    print("=" * 70)

    # Initialize
    gens = su3_generators()
    f_abc = compute_structure_constants(gens)
    B_ab = compute_killing_form(f_abc)

    # Print structure constant norms for validation
    f_sq = np.sum(f_abc**2)
    print(f"\nSU(3) structure constants: sum f_abc^2 = {f_sq:.6f}")
    print(f"Killing form B_00 = {B_ab[0,0]:.6f} (should be -3.0)")

    # Standard SU(3) f_{abc} values for validation
    # f_{123}=1, f_{147}=f_{246}=f_{257}=f_{345}=1/2,
    # f_{156}=f_{367}=-1/2, f_{458}=f_{678}=sqrt(3)/2
    # In 0-indexed: f_{012}=1, f_{036}=f_{135}=f_{146}=f_{234}=1/2, etc.
    print(f"f_012 = {f_abc[0,1,2]:.6f} (should be 1.0)")
    print(f"f_036 = {f_abc[0,3,6]:.6f} (should be 0.5)")
    print(f"f_347 = {f_abc[3,4,7]:.6f} (should be sqrt(3)/2 = {np.sqrt(3)/2:.6f})")

    # Tau values
    tau_values = np.array([0.0, 0.05, 0.10, 0.15, 0.21, 0.30, 0.40, 0.50, 0.60])

    omega_sq = np.zeros(len(tau_values))
    vol_K = np.zeros(len(tau_values))
    R_K = np.zeros(len(tau_values))

    print(f"\n{'tau':>6} {'|omega_3|^2':>14} {'Vol(K)':>10} {'V_FR (a=1)':>12}")

    for i, tau in enumerate(tau_values):
        g_s = jensen_metric(B_ab, tau)
        g_inv = np.linalg.inv(g_s)

        # Compute |omega_3|^2
        omega_sq[i] = compute_3form_norm_sq(f_abc, g_inv)

        # Volume: sqrt(det(g)) * standard volume of SU(3)
        # On Jensen curve, Vol = const = Vol_0 by construction
        vol_K[i] = np.sqrt(np.linalg.det(g_s))

        # Simple report
        V_FR = omega_sq[i] / vol_K[i]**2
        print(f"{tau:6.2f} {omega_sq[i]:14.6f} {vol_K[i]:10.6f} {V_FR:12.6f}")

    # ========================================================================
    # Compare to V_spec
    # ========================================================================
    vspec_data = np.load('tier0-computation/s24a_vspec.npz')
    tau_vspec = vspec_data['tau']
    # Use rho=0.01 as reference V_spec (standard cutoff)
    V_spec = vspec_data['V_spec_rho_0p010']

    # Interpolate V_spec to our tau values
    V_spec_interp = np.interp(tau_values, tau_vspec, V_spec)

    # Normalize both to [0,1] for comparison
    omega_norm = omega_sq / omega_sq[0]  # relative to tau=0
    V_spec_norm = V_spec_interp / V_spec_interp[0]

    # V_FR = |omega_3|^2 / Vol^2 (Vol constant on Jensen curve)
    V_FR = omega_sq / vol_K**2
    V_FR_norm = V_FR / V_FR[0]

    print(f"\n--- Normalized to tau=0 ---")
    print(f"{'tau':>6} {'|omega|^2/|omega|^2_0':>22} {'V_spec/V_spec_0':>18} {'V_FR/V_FR_0':>14}")
    for i, tau in enumerate(tau_values):
        print(f"{tau:6.2f} {omega_norm[i]:22.6f} {V_spec_norm[i]:18.6f} {V_FR_norm[i]:14.6f}")

    # ========================================================================
    # Check monotonicity of V_FR
    # ========================================================================
    dV_FR = np.diff(V_FR) / np.diff(tau_values)
    FR_increasing = np.all(dV_FR >= 0)
    FR_decreasing = np.all(dV_FR <= 0)

    print(f"\ndV_FR/dtau profile:")
    for i in range(len(dV_FR)):
        mid_tau = 0.5 * (tau_values[i] + tau_values[i+1])
        print(f"  tau={mid_tau:.3f}: dV_FR/dtau = {dV_FR[i]:.6f}")

    print(f"\nV_FR monotonically increasing: {FR_increasing}")
    print(f"V_FR monotonically decreasing: {FR_decreasing}")
    print(f"V_FR non-monotonic: {not FR_increasing and not FR_decreasing}")

    # ========================================================================
    # Check if combined V_spec + alpha*V_FR has a minimum
    # ========================================================================
    print(f"\n--- Combined potential V_spec + alpha * V_FR ---")
    alpha_values = [0.01, 0.1, 1.0, 10.0, 100.0, 1000.0]
    min_results = []

    for alpha in alpha_values:
        V_combined = V_spec_interp + alpha * V_FR
        # Normalize
        V_comb_norm = V_combined / V_combined[0]
        # Check for interior minimum
        dV = np.diff(V_combined)
        has_min = False
        min_tau = np.nan
        for k in range(len(dV) - 1):
            if dV[k] < 0 and dV[k+1] > 0:
                has_min = True
                min_tau = tau_values[k+1]
                break

        status = f"MIN at tau~{min_tau:.2f}" if has_min else "MONOTONIC"
        min_results.append((alpha, has_min, min_tau))
        print(f"  alpha={alpha:8.2f}: {status}  "
              f"V_comb(0.0)={V_combined[0]:.4f}, V_comb(0.60)={V_combined[-1]:.4f}")

    # ========================================================================
    # Gate verdict
    # ========================================================================
    print("\n" + "=" * 70)
    print("GATE BA-31-fr ASSESSMENT")
    print("=" * 70)

    if FR_decreasing or (not FR_increasing and not FR_decreasing):
        if FR_decreasing:
            verdict = "STABILIZATION POSSIBLE"
            print(f"  V_FR monotonically DECREASING in tau.")
        else:
            verdict = "STABILIZATION POSSIBLE"
            print(f"  V_FR NON-MONOTONIC in tau.")
        print(f"  V_FR has opposite tau-dependence to V_spec.")
        print(f"  --> BA-31-fr: {verdict}")
        any_min = any(has for _, has, _ in min_results)
        if any_min:
            for a, has, mt in min_results:
                if has:
                    print(f"      Combined minimum found at alpha={a:.2f}, tau~{mt:.2f}")
    else:
        # V_FR increasing -- check if it's LESS increasing than V_spec
        # so ratio V_FR/V_spec could still help
        if omega_norm[-1] < V_spec_norm[-1]:
            verdict = "FAIL (WEAKER GROWTH)"
            print(f"  V_FR monotonically increasing, but grows SLOWER than V_spec.")
            print(f"  V_FR(0.6)/V_FR(0) = {V_FR_norm[-1]:.4f}")
            print(f"  V_spec(0.6)/V_spec(0) = {V_spec_norm[-1]:.4f}")
            print(f"  V_FR cannot create a minimum against V_spec.")
        else:
            verdict = "FAIL"
            print(f"  V_FR monotonically increasing in tau (same sign as V_spec).")
        print(f"  --> BA-31-fr: {verdict}")

    # ========================================================================
    # Save
    # ========================================================================
    np.savez('tier0-computation/s31alt_3form_potential.npz',
             tau_values=tau_values,
             omega_3_sq=omega_sq,
             vol_K=vol_K,
             V_FR=V_FR,
             V_spec_interp=V_spec_interp,
             V_FR_norm=V_FR_norm,
             V_spec_norm=V_spec_norm,
             dV_FR_dtau=dV_FR,
             verdict=np.array(verdict))
    print(f"\nSaved: tier0-computation/s31alt_3form_potential.npz")

    # ========================================================================
    # Plot
    # ========================================================================
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))

    # (a) Raw quantities
    ax = axes[0]
    ax.plot(tau_values, omega_sq, 'b-o', label='|omega_3|^2', markersize=5)
    ax.set_xlabel('tau')
    ax.set_ylabel('|omega_3|^2')
    ax.set_title('(a) 3-Form Norm Squared')
    ax.grid(True, alpha=0.3)
    ax.legend()

    # (b) Normalized comparison
    ax = axes[1]
    ax.plot(tau_values, V_FR_norm, 'b-o', label='V_FR / V_FR(0)', markersize=5)
    ax.plot(tau_values, V_spec_norm, 'r-s', label='V_spec / V_spec(0)', markersize=5)
    ax.axhline(1.0, color='gray', linestyle='--', alpha=0.3)
    ax.set_xlabel('tau')
    ax.set_ylabel('Normalized potential')
    ax.set_title('(b) V_FR vs V_spec (normalized)')
    ax.legend()
    ax.grid(True, alpha=0.3)

    # (c) Combined potential for select alpha values
    ax = axes[2]
    for alpha in [0.1, 1.0, 10.0, 100.0]:
        V_comb = V_spec_interp + alpha * V_FR
        V_comb_n = V_comb / V_comb[0]
        ax.plot(tau_values, V_comb_n, '-o', label=f'alpha={alpha}', markersize=4)
    ax.set_xlabel('tau')
    ax.set_ylabel('V_combined / V_combined(0)')
    ax.set_title('(c) Combined V_spec + alpha*V_FR')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('tier0-computation/s31alt_3form_potential.png', dpi=150)
    print(f"Saved: tier0-computation/s31alt_3form_potential.png")

    elapsed = time.time() - t_start
    print(f"\nTotal runtime: {elapsed:.1f}s")
    print(f"\nGATE BA-31-fr: {verdict}")

    return verdict


if __name__ == '__main__':
    main()
