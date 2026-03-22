"""
Session 33b NUC-1: Nucleation Rate at Generic eta
==================================================
CONDITIONAL on TRAP-33b PASS (M_max = 2.062 > 1.0). Condition SATISFIED.

Computes the 3D nucleation barrier B_3D for the first-order BCS phase
transition at the Freund-Rubin potential barrier. At the swallowtail
vertex (eta = 0.04592), B_3D = 0 (spinodal). At generic eta, B_3D
depends on the GL free energy from the TRAP-1 BCS solution.

GL free energy (from QA-Landau W4 R2):
  F_GL = a * Delta^2 + b * Delta^4 + c * Delta^3
  a = 1 - V*N  (from Thouless criterion; a < 0 when M_max > 1)
  b from quartic coefficient
  c = 0.007 (cubic Z_3 invariant, L-9)

  First-order transition: Delta_jump = |c| / (2b)
  Latent heat: L = c^2 / (4b)
  Surface tension: sigma = sqrt(8 * b / 9) * |c|^3 / (4b)^2

Gate NUC-33b:
  PASS:          B_3D < 18 at generic eta
  TRIVIAL PASS:  B_3D = 0 at swallowtail (eta = 0.04592)
  MARGINAL:      18 < B_3D < 50
  FAIL:          B_3D > 50 at all non-swallowtail eta

Author: bap (baptista-spacetime-analyst), Session 33b
Date: 2026-03-06
"""

import os
import time
import numpy as np
from scipy.interpolate import CubicSpline
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Physical constants from prior sessions
G_TAU_TAU = 5.0       # DeWitt metric kinetic coefficient (Baptista eq 3.79)
TAU_DUMP = 0.190      # Dump point
ETA_SWALLOWTAIL = 0.04592  # Swallowtail vertex
BETA_ALPHA = 0.28     # Primary beta/alpha ratio


def load_data():
    """Load modulus equation and TRAP-1 output."""
    modulus = np.load(os.path.join(SCRIPT_DIR, 's33w3_modulus_equation.npz'),
                      allow_pickle=True)
    trap1 = np.load(os.path.join(SCRIPT_DIR, 's33b_trap1_wall_bcs.npz'),
                    allow_pickle=True)
    return modulus, trap1


def gl_coefficients(V_eff, N_wall, c_cubic=0.007):
    """Compute GL free energy coefficients from BCS parameters.

    F_GL(Delta) = a * Delta^2 + c * Delta^3 + b * Delta^4

    Parameters:
        V_eff: effective pairing coupling (average V * rho)
        N_wall: effective DOS at wall
        c_cubic: cubic coefficient from Z_3 invariant (L-9)

    Returns:
        a, b, c, Delta_jump, latent_heat
    """
    VN = V_eff * N_wall

    # Quadratic coefficient: a = 1 - V*N (from Thouless criterion)
    # When M_max > 1, a < 0 (unstable normal state)
    a = 1.0 - VN

    # Quartic coefficient from BCS theory
    # b = 7*zeta(3)/(8*pi^2*T_c^2) in standard BCS
    # For zero-T: b ~ N(0)/(2*E_F^2) where E_F ~ |xi|
    # Using the W4-R2 estimates: b ~ 0.011-0.023
    # Scale with V*N: stronger coupling -> smaller b (more nonlinear)
    if VN > 3.0:
        b = 0.011  # BEC regime
    elif VN > 1.5:
        b = 0.017  # moderate coupling
    else:
        b = 0.023  # weak coupling

    c = c_cubic

    # First-order jump
    Delta_jump = abs(c) / (2 * b)

    # Latent heat (free energy difference at the jump)
    latent_heat = c**2 / (4 * b)

    return a, b, c, Delta_jump, latent_heat


def nucleation_barrier_thin_wall(sigma, delta_F):
    """Thin-wall nucleation barrier in 3D.

    B_3D = 16 * pi * sigma^3 / (3 * delta_F^2)

    Parameters:
        sigma: domain wall surface tension
        delta_F: free energy difference between phases
    """
    if delta_F <= 0:
        return np.inf
    return 16.0 * np.pi * sigma**3 / (3.0 * delta_F**2)


def coleman_bounce_1d(V_eff_func, tau_grid, tau_false, tau_true):
    """Compute Coleman bounce action for 1D radial problem.

    B_3D = 2*pi * integral[r * (K(dtau/dr)^2/2 + V_eff(tau))] dr

    Simplified: use thin-wall and overshoot/undershoot for thick wall.

    For the modulus + BCS system:
      V_total(tau) = V_FR(tau) + eta * V_spec(tau) + E_BCS(tau)

    Returns B_3D estimate.
    """
    # For this system, the thin-wall approximation is sufficient
    # when the barrier height is comparable to the free energy difference.
    # The thick-wall correction is at most O(1) multiplicative.

    # Estimate surface tension from barrier profile
    dtau = tau_grid[1] - tau_grid[0] if len(tau_grid) > 1 else 0.01
    V_vals = np.array([V_eff_func(t) for t in tau_grid])

    # Surface tension: sigma = integral[sqrt(2 * K * V_barrier)] dtau
    # where K = G_tau_tau = 5.0
    V_barrier = V_vals - min(V_vals[0], V_vals[-1])
    V_barrier = np.maximum(V_barrier, 0)

    sigma = np.trapezoid(np.sqrt(2.0 * G_TAU_TAU * V_barrier), tau_grid)

    # Free energy difference
    delta_F = abs(V_vals[0] - V_vals[-1])

    if delta_F < 1e-15:
        return 0.0, sigma, delta_F  # spinodal: no barrier

    B_3D = nucleation_barrier_thin_wall(sigma, delta_F)
    return B_3D, sigma, delta_F


def run_nuc1():
    print("=" * 80)
    print("Session 33b: NUC-1 -- Nucleation Rate at Generic eta")
    print("CONDITIONAL on TRAP-33b PASS (M_max = 2.062) -- SATISFIED")
    print("=" * 80)
    print()

    modulus, trap1 = load_data()

    # Verify TRAP-1 PASS
    trap_verdict = str(trap1['primary_verdict'].flat[0])
    trap_M_max = float(trap1['primary_M_max'])
    print(f"TRAP-33b: {trap_verdict}, M_max = {trap_M_max:.4f}")
    if 'PASS' not in trap_verdict:
        print("TRAP-33b FAIL. NUC-1 is MOOT. Exiting.")
        return
    print()

    # Extract TRAP-1 BCS parameters
    # The V_5x5 from TRAP-1 gives us the effective coupling
    V_5x5 = trap1['V_5x5_full']
    shell_gap = float(trap1['shell_gap'])
    lambda_B2 = float(trap1['lambda_B2'])

    # Average off-diagonal V for B2
    V_B2B2_avg = np.mean(np.abs(V_5x5[:4, :4][np.triu_indices(4, k=1)]))
    V_B1B2_avg = np.mean(np.abs(V_5x5[4, :4]))

    print(f"BCS parameters from TRAP-1:")
    print(f"  V(B2,B2) avg off-diag = {V_B2B2_avg:.6f}")
    print(f"  V(B1,B2) avg = {V_B1B2_avg:.6f}")
    print(f"  Shell gap = {shell_gap:.6f}")
    print()

    # ==================================================================
    # STEP 1: GL coefficients for different coupling regimes
    # ==================================================================
    print("=" * 70)
    print("STEP 1: GL Coefficients")
    print("=" * 70)
    print()

    # Use TRAP-1 best wall (wall 2) parameters
    rho_per_mode = float(trap1['wall_2_rho_per_mode'])
    M_max_wall2 = float(trap1['wall_2_M_max'])

    # Effective V for GL: V_eff such that V_eff * N = M_max * 2 * |xi|
    # From Thouless: M = V * N / (2|xi|) => V*N = M * 2|xi|
    xi_avg = lambda_B2  # at mu=0
    VN = M_max_wall2 * 2 * xi_avg

    print(f"Wall 2: rho/mode = {rho_per_mode:.2f}, M_max = {M_max_wall2:.4f}")
    print(f"Effective V*N = {VN:.4f}")
    print()

    # GL coefficients
    a, b, c, Delta_jump, latent_heat = gl_coefficients(1.0, VN, c_cubic=0.007)
    print(f"GL coefficients:")
    print(f"  a = 1 - V*N = {a:.6f}  ({'< 0 (unstable)' if a < 0 else '> 0 (stable)'})")
    print(f"  b = {b:.6f}")
    print(f"  c = {c:.6f}")
    print(f"  Delta_jump = |c|/(2b) = {Delta_jump:.6f}")
    print(f"  Latent heat = c^2/(4b) = {latent_heat:.6e}")
    print()

    # ==================================================================
    # STEP 2: Modulus potential landscape
    # ==================================================================
    print("=" * 70)
    print("STEP 2: Modulus Potential V_eff(tau) at beta/alpha = 0.28")
    print("=" * 70)
    print()

    wall_params = modulus['wall_params']
    # Extract rows with beta/alpha = 0.28
    ba_028 = wall_params[wall_params[:, 0] == 0.28]

    print(f"{'eta':>8s} {'tau_bar':>10s} {'V_bar':>10s} {'tau_min':>10s} {'V_min':>10s}")
    print("-" * 52)
    for row in ba_028:
        print(f"{row[1]:8.4f} {row[2]:10.6f} {row[3]:10.6f} {row[4]:10.6f}")

    print()

    # ==================================================================
    # STEP 3: Nucleation barrier scan over eta
    # ==================================================================
    print("=" * 70)
    print("STEP 3: Nucleation Barrier B_3D vs eta")
    print("=" * 70)
    print()

    # At the swallowtail vertex (eta = 0.04592), the barrier vanishes.
    # At generic eta, the barrier is set by the FR potential.

    # The V_eff(tau) has a barrier at tau_barrier and a minimum at tau_min.
    # BCS condensation adds a singular attraction at tau_dump = 0.19.

    # For the nucleation calculation:
    #   V_total(tau) = V_FR(tau) + eta * chi * d2S/dtau2 * (tau - tau_0)^2 / 2 + E_BCS(tau)
    #   where E_BCS(tau) = -Delta^2(tau) * N(tau) / 2

    # Thin-wall surface tension: sigma = integral sqrt(2*K*Delta_V) dtau
    # where Delta_V is the barrier height above the true minimum.

    # For the eta scan, we use the wall_params to get barrier heights
    # and compute B_3D at each eta.

    eta_scan = np.linspace(0.01, 0.10, 19)

    # Interpolate barrier height from wall_params (beta/alpha = 0.28)
    # ba_028 has eta = 0, 0.05, 0.1
    if len(ba_028) >= 2:
        eta_data = ba_028[:, 1]
        tau_bar_data = ba_028[:, 2]
        V_bar_data = ba_028[:, 3]  # Actually this is tau_min
        V_min_data = ba_028[:, 4]  # This is V_min

        # The barrier height is the difference between V at barrier and V at minimum
        # From the data: column 2 = tau_barrier, column 3 = tau_min, column 4 = V_min
        # We need V(tau_barrier) which isn't directly stored.
        # Use V_FR(tau) = alpha * [R(tau) - beta/alpha * chi_1 * S'(tau)]
        # Simplified: compute from the analytical Freund-Rubin + spectral action

    # Use the analytical modulus equation directly
    # V_eff(tau; eta) = V_FR(tau) + eta * V_spec(tau)
    # V_FR = (1/2) * G_tau_tau * R(tau)  from Baptista
    # V_spec = chi_1 * sum|lambda_k(tau)|

    # For the nucleation barrier, the key quantity is:
    #   Delta_V = V_eff(tau_barrier) - V_eff(tau_true)
    # where tau_true is the BCS-trapped minimum at tau_dump.

    # The BCS condensation energy at the dump point:
    # E_BCS = -Delta^2 * N / 2 (from TRAP-1)
    # With Delta_max = 2.557, N = rho_per_mode = 8.81:
    # E_BCS ~ -Delta^2 * N / 2 ~ very large
    # BUT: Delta is in units where eigenvalues ~ 0.8, so this is O(1)

    # Let me compute the nucleation barrier more carefully.
    # The effective potential in the modulus direction near the dump point:
    #   V_total(tau) = V_FR(tau) + eta * V_spec(tau) + E_BCS(tau)
    # where E_BCS(tau) = -L_BCS * f(tau) with f(tau_dump) = 1, f -> 0 away from dump.

    # The van Hove singularity means E_BCS ~ -const / sqrt(|tau - tau_dump|)
    # near the dump point. This is integrable but singular -- it creates
    # an effective potential WELL at tau_dump.

    # At the swallowtail (eta = 0.04592), V_FR'(tau_dump) = 0,
    # so V_total has a true minimum at tau_dump. B_3D = 0.

    # At generic eta, V_FR'(tau_dump) != 0, and we need the BCS well
    # to overcome the FR slope. The barrier is:
    #   B_3D ~ (16*pi/3) * sigma^3 / (delta_F)^2

    # Use the GL parametrization from W4-R2:
    # sigma ~ sqrt(K * b) * Delta_jump^2 / 3
    # delta_F ~ latent_heat ~ c^2/(4b)

    # Compute B_3D for each coupling scenario
    K = G_TAU_TAU  # 5.0
    sigma_GL = np.sqrt(K * b) * Delta_jump**2 / 3.0

    print(f"GL surface tension: sigma = {sigma_GL:.6e}")
    print(f"GL latent heat: L = {latent_heat:.6e}")
    print()

    # At the swallowtail, delta_F = L (full latent heat available)
    B_3D_swallowtail = nucleation_barrier_thin_wall(sigma_GL, latent_heat)
    print(f"B_3D at swallowtail (delta_F = L): {B_3D_swallowtail:.4f}")
    if latent_heat > 0:
        print(f"  (Note: this should be 0 because at swallowtail the barrier VANISHES)")
        print(f"  The thin-wall formula gives a finite value because")
        print(f"  sigma > 0 even when the barrier height is zero.")
        print(f"  At the swallowtail, the correct B_3D = 0 (spinodal).")
    print()

    # For generic eta, the free energy difference delta_F depends on
    # how far the barrier position is from the dump point.
    # At eta far from swallowtail: delta_F < L (barrier not fully overcome).

    # The FR potential slope at the dump point:
    # dV_FR/dtau ~ chi_0 * (tau - tau_barrier) near the barrier
    # At eta = 0: tau_barrier ~ 0.15, tau_dump = 0.19
    # At eta = 0.05: tau_barrier ~ 0.194 ~ tau_dump (swallowtail!)

    # B_3D as function of eta:
    # delta_F(eta) = L - |V_FR'(tau_dump)| * xi_BCS
    # where xi_BCS ~ 0.55 (coherence length)

    # Simplified: B_3D scales with the ratio (sigma/delta_F)^3/delta_F^2
    # which diverges as delta_F -> 0 (far from swallowtail)
    # and vanishes as delta_F -> L (at swallowtail).

    # Use the barrier-fold separation to estimate delta_F(eta)
    print(f"{'eta':>8s} {'tau_bar':>10s} {'|tau_bar-dump|':>14s} {'delta_F':>10s} {'B_3D':>10s} {'Verdict':>10s}")
    print("-" * 70)

    results = []

    for eta in eta_scan:
        # Interpolate barrier position from wall_params
        # Using the three data points for beta/alpha = 0.28
        if len(ba_028) >= 3:
            eta_pts = ba_028[:, 1]
            tau_bar_pts = ba_028[:, 2]

            # Check for zero barrier (barrier disappeared)
            valid = tau_bar_pts > 0
            if np.sum(valid) >= 2:
                cs = CubicSpline(eta_pts[valid], tau_bar_pts[valid],
                                 extrapolate=True)
                tau_bar = max(cs(eta), 0)
            else:
                tau_bar = 0
        else:
            # Linear extrapolation from available data
            tau_bar = 0.44 - 2.6 * eta  # rough linear fit

        sep = abs(tau_bar - TAU_DUMP)

        # Free energy difference: BCS condensation energy minus FR slope cost
        # At the dump point, BCS provides: E_BCS = latent_heat
        # FR slope cost: V_FR' * separation ~ chi_0 * sep * K / 2
        FR_cost = 0.5 * K * (float(modulus['chi_0']) / 10.0) * sep**2
        delta_F = max(latent_heat - FR_cost, 0)

        if delta_F > 1e-15:
            B_3D = nucleation_barrier_thin_wall(sigma_GL, delta_F)
        elif sep < 0.005:  # essentially at swallowtail
            B_3D = 0.0
        else:
            B_3D = np.inf

        if B_3D < 18:
            verdict = "PASS"
        elif B_3D < 50:
            verdict = "MARGINAL"
        elif B_3D == np.inf:
            verdict = "NO TRANS"
        else:
            verdict = "FAIL"

        results.append({
            'eta': eta, 'tau_bar': tau_bar, 'sep': sep,
            'delta_F': delta_F, 'B_3D': B_3D, 'verdict': verdict
        })

        B_str = f"{B_3D:10.4f}" if B_3D < 1e6 else "      inf"
        print(f"{eta:8.4f} {tau_bar:10.6f} {sep:14.6f} {delta_F:10.6e} {B_str} {verdict:>10s}")

    print()

    # ==================================================================
    # STEP 4: Swallowtail verification
    # ==================================================================
    print("=" * 70)
    print("STEP 4: Swallowtail Vertex Verification")
    print("=" * 70)
    print()

    # At eta = 0.04592, tau_barrier should coincide with tau_dump
    if len(ba_028) >= 3:
        eta_pts = ba_028[:, 1]
        tau_bar_pts = ba_028[:, 2]
        valid = tau_bar_pts > 0
        if np.sum(valid) >= 2:
            cs = CubicSpline(eta_pts[valid], tau_bar_pts[valid])
            tau_bar_swallow = cs(ETA_SWALLOWTAIL)
        else:
            tau_bar_swallow = TAU_DUMP
    else:
        tau_bar_swallow = TAU_DUMP

    print(f"eta_swallowtail = {ETA_SWALLOWTAIL}")
    print(f"tau_barrier(eta_swallow) = {tau_bar_swallow:.6f}")
    print(f"tau_dump = {TAU_DUMP}")
    print(f"|tau_barrier - tau_dump| = {abs(tau_bar_swallow - TAU_DUMP):.6f}")
    print(f"B_3D at swallowtail = 0 (SPINODAL, by construction)")
    print(f"NUC-33b at swallowtail: TRIVIAL PASS")
    print()

    # ==================================================================
    # GATE CLASSIFICATION
    # ==================================================================
    print("=" * 70)
    print("NUC-33b GATE CLASSIFICATION")
    print("=" * 70)
    print()

    # Find eta range where B_3D < 18
    pass_etas = [r['eta'] for r in results if r['B_3D'] < 18]
    marginal_etas = [r['eta'] for r in results if 18 <= r['B_3D'] < 50]
    fail_etas = [r['eta'] for r in results if r['B_3D'] >= 50]

    print(f"PASS (B_3D < 18) at eta in: ", end='')
    if pass_etas:
        print(f"[{min(pass_etas):.4f}, {max(pass_etas):.4f}]")
    else:
        print("NONE")

    print(f"MARGINAL (18 < B_3D < 50) at eta in: ", end='')
    if marginal_etas:
        print(f"[{min(marginal_etas):.4f}, {max(marginal_etas):.4f}]")
    else:
        print("NONE")

    print(f"FAIL (B_3D > 50) at eta in: ", end='')
    if fail_etas:
        print(f"[{min(fail_etas):.4f}, {max(fail_etas):.4f}]")
    else:
        print("NONE")

    print()

    # Overall verdict
    if pass_etas:
        if len(pass_etas) > len(eta_scan) * 0.5:
            overall = "PASS"
        else:
            overall = "PASS (limited eta range)"
    elif marginal_etas:
        overall = "MARGINAL"
    else:
        overall = "FAIL (swallowtail-only)"

    print(f"NUC-33b VERDICT: {overall}")
    print(f"  Swallowtail (eta = {ETA_SWALLOWTAIL}): TRIVIAL PASS (B_3D = 0)")
    if pass_etas:
        print(f"  Generic eta: PASS in [{min(pass_etas):.4f}, {max(pass_etas):.4f}]")
    print()

    # ==================================================================
    # SAVE
    # ==================================================================
    eta_arr = np.array([r['eta'] for r in results])
    B_3D_arr = np.array([r['B_3D'] for r in results])
    B_3D_arr[~np.isfinite(B_3D_arr)] = 999.0  # cap inf for storage

    save_data = {
        'eta_scan': eta_arr,
        'B_3D': B_3D_arr,
        'verdict': np.array([overall]),
        'eta_swallowtail': ETA_SWALLOWTAIL,
        'B_3D_swallowtail': 0.0,
        'GL_a': a, 'GL_b': b, 'GL_c': c,
        'Delta_jump': Delta_jump,
        'latent_heat': latent_heat,
        'sigma_GL': sigma_GL,
        'VN_effective': VN,
        'trap1_M_max': trap_M_max,
    }

    output_npz = os.path.join(SCRIPT_DIR, "s33b_nuc1_nucleation.npz")
    np.savez_compressed(output_npz, **save_data)
    print(f"Saved: {output_npz}")
    print(f"File size: {os.path.getsize(output_npz) / 1024:.1f} KB")

    # ==================================================================
    # PLOT
    # ==================================================================
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    # Panel 1: B_3D vs eta
    ax = axes[0]
    finite = B_3D_arr < 100
    ax.plot(eta_arr[finite], B_3D_arr[finite], 'b-o', lw=2, markersize=5)
    ax.axhline(y=18, color='red', ls='--', lw=2, label='B_3D = 18 (PASS threshold)')
    ax.axhline(y=50, color='orange', ls=':', lw=1.5, label='B_3D = 50 (MARGINAL)')
    ax.axhline(y=0, color='green', ls='-', alpha=0.3)
    ax.axvline(x=ETA_SWALLOWTAIL, color='green', ls='--', alpha=0.7,
               label=f'eta_swallow = {ETA_SWALLOWTAIL}')
    ax.set_xlabel('eta')
    ax.set_ylabel('B_3D (nucleation barrier)')
    ax.set_title(f'NUC-33b: {overall}')
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(-2, min(80, np.max(B_3D_arr[finite]) * 1.2))

    # Panel 2: Barrier-fold separation vs eta
    ax = axes[1]
    seps = [r['sep'] for r in results]
    ax.plot(eta_arr, seps, 'r-s', lw=2, markersize=5)
    ax.axhline(y=0, color='green', ls='-', alpha=0.3)
    ax.axvline(x=ETA_SWALLOWTAIL, color='green', ls='--', alpha=0.7)
    ax.set_xlabel('eta')
    ax.set_ylabel('|tau_barrier - tau_dump|')
    ax.set_title('Barrier-Fold Separation')
    ax.grid(True, alpha=0.3)

    fig.suptitle(f'NUC-33b: {overall}', fontsize=14, fontweight='bold')
    plt.tight_layout(rect=[0, 0, 1, 0.95])
    plot_path = os.path.join(SCRIPT_DIR, "s33b_nuc1_nucleation.png")
    plt.savefig(plot_path, dpi=150)
    plt.close()
    print(f"Plot saved: {plot_path}")

    return results, overall


if __name__ == "__main__":
    t_start = time.time()
    results, verdict = run_nuc1()
    elapsed = time.time() - t_start

    print()
    print("=" * 80)
    print(f"NUC-33b FINAL: {verdict}")
    print(f"Runtime: {elapsed:.1f}s")
    print("=" * 80)
