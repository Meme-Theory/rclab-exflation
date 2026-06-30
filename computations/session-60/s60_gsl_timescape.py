#!/usr/bin/env python3
"""
GSL-TIMESCAPE-60: Generalized Second Law Check on Timescape Mechanism
=====================================================================
Session 60, Task #22
Agent: Hawking-Theorist

Physics:
  The S59 timescape mechanism (TIMESCAPE-WA-59) generates apparent w_a = -0.645
  through spatial variation of the Jensen parameter tau across the 32-cell
  Voronoi fabric. Voids have tau_void < tau_fold, walls have tau_wall > tau_fold.
  This produces delta_G/G = -0.526 (53% G variation).

  The Generalized Second Law constrains this mechanism independently of
  observational bounds. In the framework, gravitational entropy is the spectral
  action S_spec(tau), playing the role of A/(4G) (Jacobson 1995 / Paper 17;
  Bekenstein 1973 / Paper 11; GSL-40, GSL-43, GSL-QTHEORY-46).

  The key test:
  1. The spectral action S_spec(tau) is the gravitational entropy functional.
     If tau varies spatially, S_grav = sum_cells S_spec(tau_cell).
  2. The Bekenstein-Hawking entropy of a local causal diamond scales as
     A_local / (4 * G_local), and G_local varies with tau.
  3. The matter entropy (Bogoliubov excitations) also depends on the local
     gap structure, which varies with tau.
  4. GSL requires: S_gen(inhomogeneous) >= S_gen(uniform) at every instant,
     AND dS_gen/dt >= 0 during the development of inhomogeneity.

  Critical mathematical structure:
  - S_spec(tau) has d^2S/dtau^2 > 0 at the fold (HESS-40: 22/22 positive).
    Jensen's inequality: <S_spec(tau)> >= S_spec(<tau>).
    So spectral action FAVORS inhomogeneity -- no GSL violation from S_grav alone.
  - But G(tau) = G_N * (a2_fold / a2(tau)). If tau decreases, a2 decreases,
    G increases, and the Bekenstein-Hawking entropy A/(4G) DECREASES.
  - The competition between S_spec (convex, favors inhomogeneity) and
    S_BH ~ 1/G(tau) determines the GSL verdict.

  The CRUCIAL physical observable: the entropy PRODUCTION RATE.
  As the fabric develops tau-inhomogeneity (during structure formation),
  does the total S_gen increase or decrease?

Gate: GSL-TIMESCAPE-60
  Pre-registered criterion:
    PASS: GSL violated (timescape thermodynamically forbidden by entropy decrease)
    FAIL: GSL satisfied (no additional closure from thermodynamics)
    INFO: Marginal or model-dependent

Input: s59_timescape_wa.npz, canonical_constants.py
Output: s60_gsl_timescape.{npz, png}

References:
  - Bekenstein 1973 (Paper 11): S_BH = A/(4*l_P^2)
  - Jacobson 1995 (Paper 17): Einstein eqs from thermodynamics
  - GSL-40 (s40_gsl_transit): structural 3-term GSL PASS, v_min=0
  - GSL-43 (s43_gsl_transit): 32-cell fabric GSL, 2560x margin
  - GSL-QTHEORY-46: 0/599 neg steps, 35,983x grav dominance
  - HESS-40: 22/22 positive eigenvalues, d^2S/dtau^2 > 0 (convex at fold)
  - TIMESCAPE-WA-59: w_a=-0.645, delta_G/G=-0.526
"""

import os
import sys
import time
import numpy as np

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, SCRIPT_DIR)

LOGPATH = os.path.join(SCRIPT_DIR, "s60_gsl_timescape_log.txt")
log = open(LOGPATH, "w")

def pr(msg=""):
    log.write(str(msg) + "\n")
    log.flush()

try:
    from canonical_constants import (
        tau_fold, S_fold, dS_fold, d2S_fold, Z_fold, G_DeWitt,
        a0_fold, a2_fold, a4_fold,
        N_cells, M_KK_gravity, M_KK_kerner, M_KK,
        G_N, l_Planck, hbar_SI, c_light, k_B_SI,
        H_0_km_s_Mpc, Omega_m, Omega_Lambda,
        rho_crit_GeV4, rho_Lambda_obs,
        T_acoustic, E_cond, n_pairs, N_dof_BCS,
        E_B1, E_B2_mean, E_B3_mean,
        Delta_0_GL, xi_BCS,
        clock_coeff, c_fabric,
        Mpc_to_m, c_light_km_s,
    )
    pr("Canonical constants loaded.")

    # Load timescape data from S59
    d59 = np.load(os.path.join(SCRIPT_DIR, "s59_timescape_wa.npz"), allow_pickle=True)
    sigma_tau = float(d59['sigma_tau'])
    delta_G_over_G = float(d59['delta_G_over_G'])
    delta_tau_eff = float(d59['delta_tau_eff'])
    wa_result = float(d59['wa_result'])
    pr("S59 timescape data loaded.")

    t0 = time.time()
    out = {}

    pr("=" * 78)
    pr("GSL-TIMESCAPE-60: Generalized Second Law on Timescape Mechanism")
    pr("=" * 78)

    # ======================================================================
    #  Step 1: Spectral action as gravitational entropy
    # ======================================================================
    pr("\n" + "=" * 78)
    pr("STEP 1: SPECTRAL ACTION ENTROPY LANDSCAPE")
    pr("=" * 78)

    # S_spec(tau) ~ S_fold + dS_fold*(tau-tau_fold) + (1/2)*d2S_fold*(tau-tau_fold)^2
    # This is the Taylor expansion around the fold.
    # d2S_fold > 0 means S_spec is CONVEX at the fold.

    # Void and wall tau values
    # Convention: voids have LOWER tau (less compactified), walls HIGHER
    # delta_tau_eff = sigma_tau ~ 0.00530
    f_void = 0.76   # Wiltshire 2007 void fraction  # (local)
    f_wall = 1.0 - f_void

    tau_void = tau_fold - delta_tau_eff   # = 0.19 - 0.00530 = 0.1847
    tau_wall = tau_fold + delta_tau_eff * f_void / f_wall  # Mass-weighted: f_v*delta_v + f_w*delta_w = 0
    # Actually: for the mean to be tau_fold, we need
    # f_void * tau_void + f_wall * tau_wall = tau_fold
    # f_void * (tau_fold - d_v) + f_wall * (tau_fold + d_w) = tau_fold
    # -f_void * d_v + f_wall * d_w = 0 => d_w = (f_void/f_wall) * d_v
    d_v = delta_tau_eff  # void shift
    d_w = (f_void / f_wall) * d_v  # wall shift (ensures volume-weighted mean = tau_fold)

    tau_void = tau_fold - d_v
    tau_wall = tau_fold + d_w

    pr(f"  f_void = {f_void}, f_wall = {f_wall:.2f}")
    pr(f"  delta_tau_eff = {delta_tau_eff:.6f}")
    pr(f"  d_v (void shift) = {d_v:.6f}")
    pr(f"  d_w (wall shift) = {d_w:.6f}")
    pr(f"  tau_void = {tau_void:.6f}")
    pr(f"  tau_wall = {tau_wall:.6f}")
    pr(f"  Check: f_v*tau_v + f_w*tau_w = {f_void*tau_void + f_wall*tau_wall:.6f} (should be {tau_fold})")

    # Spectral action at void and wall
    def S_spec(tau):
        dt = tau - tau_fold
        return S_fold + dS_fold * dt + 0.5 * d2S_fold * dt**2

    S_void = S_spec(tau_void)
    S_wall = S_spec(tau_wall)
    S_uniform = S_spec(tau_fold)  # = S_fold

    # Volume-weighted average
    S_avg_inhomog = f_void * S_void + f_wall * S_wall
    Delta_S_grav = S_avg_inhomog - S_uniform

    pr(f"\n  S_spec(tau_void) = {S_void:.2f}")
    pr(f"  S_spec(tau_fold) = {S_uniform:.2f}")
    pr(f"  S_spec(tau_wall) = {S_wall:.2f}")
    pr(f"  <S_spec>_inhomog = {S_avg_inhomog:.2f}")
    pr(f"  Delta_S_grav = <S>_inhomog - S_uniform = {Delta_S_grav:.4f}")

    # Jensen's inequality check: for convex S (d2S > 0), <S(tau)> >= S(<tau>)
    # Delta_S_grav should be POSITIVE
    jensen_sign = "POSITIVE (convex, as expected)" if Delta_S_grav > 0 else "NEGATIVE (ANOMALOUS)"
    pr(f"  Jensen inequality: {jensen_sign}")

    # Exact Jensen excess for two-point distribution:
    # Delta = (1/2) * d2S * [f_v * d_v^2 + f_w * d_w^2]
    jensen_exact = 0.5 * d2S_fold * (f_void * d_v**2 + f_wall * d_w**2)
    pr(f"  Jensen excess (exact) = {jensen_exact:.4f}")
    pr(f"  Jensen excess (computed) = {Delta_S_grav:.4f}")
    pr(f"  Ratio to S_fold = {Delta_S_grav / S_fold:.2e}")

    out['S_void'] = np.array(S_void)
    out['S_wall'] = np.array(S_wall)
    out['S_uniform'] = np.array(S_uniform)
    out['Delta_S_grav'] = np.array(Delta_S_grav)

    # ======================================================================
    #  Step 2: Bekenstein-Hawking entropy with varying G
    # ======================================================================
    pr("\n" + "=" * 78)
    pr("STEP 2: BEKENSTEIN-HAWKING ENTROPY WITH VARYING G")
    pr("=" * 78)

    # In the framework, the effective Newton's constant is extracted from the
    # spectral action: G_eff(tau) = pi / (48 * a2(tau) * M_KK^2)
    # (from the 4D Ricci scalar coefficient in the spectral action).
    #
    # If tau varies, G_eff varies. The S59 computation found:
    # delta_G/G = -frac_da2 * delta_tau_eff = -0.526
    #
    # For the Bekenstein-Hawking entropy of a causal diamond of area A:
    #   S_BH = A / (4 * G_eff * l_P^2) ... but in M_KK units, S_BH = a2(tau)
    # The spectral action a2 coefficient IS the gravitational entropy density.

    # The a2(tau) variation
    # From S59: frac_da2 = (da2/dtau) / a2 = 99.127 at fold
    frac_da2 = 99.127  # from S59 log  # (local)

    a2_void = a2_fold * (1 + frac_da2 * (-d_v))  # = a2_fold * (1 - 99.127 * 0.00530)
    a2_wall = a2_fold * (1 + frac_da2 * d_w)

    # G varies inversely with a2: G ~ 1/a2
    G_void_over_G0 = a2_fold / a2_void  # G increases when a2 decreases
    G_wall_over_G0 = a2_fold / a2_wall

    delta_G_void = G_void_over_G0 - 1
    delta_G_wall = G_wall_over_G0 - 1

    pr(f"  frac_da2 = {frac_da2:.3f}")
    pr(f"  a2_void = {a2_void:.4f} (a2_fold = {a2_fold:.4f})")
    pr(f"  a2_wall = {a2_wall:.4f}")
    pr(f"  G_void/G_0 = {G_void_over_G0:.6f} (delta = {delta_G_void:+.4f})")
    pr(f"  G_wall/G_0 = {G_wall_over_G0:.6f} (delta = {delta_G_wall:+.4f})")
    pr(f"  Volume-weighted <delta_G/G> = {f_void*delta_G_void + f_wall*delta_G_wall:.6f} (should ~ 0)")

    # S_BH ~ A / (4G) ~ A * a2(tau)
    # For equal-area cells: S_BH(void)/S_BH(uniform) = a2_void/a2_fold
    # Total: S_BH_total = f_v * (A/4G_v) + f_w * (A/4G_w) = A/4G_0 * [f_v * a2_v/a2_0 + f_w * a2_w/a2_0]

    ratio_BH_void = a2_void / a2_fold
    ratio_BH_wall = a2_wall / a2_fold
    ratio_BH_avg = f_void * ratio_BH_void + f_wall * ratio_BH_wall

    Delta_S_BH_frac = ratio_BH_avg - 1.0  # fractional change in total BH entropy

    pr(f"\n  S_BH(void)/S_BH(uniform) = {ratio_BH_void:.6f}")
    pr(f"  S_BH(wall)/S_BH(uniform) = {ratio_BH_wall:.6f}")
    pr(f"  <S_BH>_inhomog / S_BH_uniform = {ratio_BH_avg:.6f}")
    pr(f"  Fractional change = {Delta_S_BH_frac:+.6e}")

    # Note: a2(tau) is nearly LINEAR near the fold (large slope).
    # For a linear function, <f(tau)> = f(<tau>) exactly (no Jensen excess).
    # The fractional BH change comes from the nonlinear part.

    # Since a2 is approximately linear: a2(tau) ~ a2_fold + (da2/dtau)*(tau - tau_fold)
    # <a2> = a2_fold + (da2/dtau) * [f_v*(-d_v) + f_w*d_w] = a2_fold (mean preserving)
    # So Delta_S_BH_frac ~ 0 at linear order.
    # At quadratic order: Delta_S_BH ~ (1/2) * d2(a2)/dtau^2 * [f_v*d_v^2 + f_w*d_w^2] / a2_fold

    # We need d2(a2)/dtau^2. From spectral action structure:
    # a2 is a smooth function of tau. Let's compute it from the S_spec expansion.
    # S_spec = sum_k f(lambda_k^2) involves a2 as one coefficient.
    # We don't have d2(a2)/dtau^2 directly, but we can use the frac_da2.
    # For a2(tau) = a2_fold * exp(frac_da2 * (tau - tau_fold)) [exponential approx]:
    # d2(a2)/dtau^2 = a2_fold * frac_da2^2
    # Then Delta_S_BH ~ (1/2) * a2_fold * frac_da2^2 * [f_v*d_v^2 + f_w*d_w^2] / a2_fold
    #                 = (1/2) * frac_da2^2 * variance_tau

    variance_tau = f_void * d_v**2 + f_wall * d_w**2
    Delta_S_BH_quadratic = 0.5 * frac_da2**2 * variance_tau

    pr(f"\n  Variance of tau = {variance_tau:.6e}")
    pr(f"  Quadratic BH correction = {Delta_S_BH_quadratic:.6e}")
    pr(f"  (This is fractional; multiply by S_BH to get absolute)")

    out['a2_void'] = np.array(a2_void)
    out['a2_wall'] = np.array(a2_wall)
    out['G_void_over_G0'] = np.array(G_void_over_G0)
    out['G_wall_over_G0'] = np.array(G_wall_over_G0)
    out['Delta_S_BH_frac'] = np.array(Delta_S_BH_frac)

    # ======================================================================
    #  Step 3: Matter entropy with varying gap
    # ======================================================================
    pr("\n" + "=" * 78)
    pr("STEP 3: MATTER ENTROPY WITH VARYING GAP")
    pr("=" * 78)

    # The BCS gap Delta(tau) varies with tau. Near the fold:
    # Delta(tau) ~ Delta_0 * |1 - tau/tau_fold|^{1/2} (BCS critical behavior)
    # But we're near the fold, so the gap is approximately:
    # Delta_void and Delta_wall differ.
    #
    # The matter entropy in each cell comes from Bogoliubov quasiparticle excitations.
    # For the GGE state, S_matter ~ sum_k h(n_k) where n_k = |beta_k|^2.
    #
    # The key physics: the BCS gap is LARGER away from the fold (both above and below),
    # so both void and wall have larger gaps than the fold.
    # Actually: Delta(tau) opens below tau_fold and closes AT tau_fold.
    # tau_void < tau_fold => gap still open, larger
    # tau_wall > tau_fold => gap reopening after fold, or still evolving
    #
    # For the matter entropy, the Bogoliubov excitation from the transit is fixed:
    # n_k = |beta_k|^2 = 0.273 (S59 flat spectrum result).
    # This is a PROPERTY OF THE TRANSIT, not of the local tau.
    # The matter entropy per cell is the same regardless of local tau
    # (the transit creates the same excitations everywhere -- it's a global quench).

    n_k_bog = 0.273  # S59 flat Bogoliubov occupation
    S_matter_per_mode = -n_k_bog * np.log(n_k_bog) - (1 - n_k_bog) * np.log(1 - n_k_bog)
    S_matter_per_cell = N_dof_BCS * S_matter_per_mode
    S_matter_total_uniform = N_cells * S_matter_per_cell
    S_matter_total_inhomog = S_matter_total_uniform  # Same -- global quench

    pr(f"  n_k (Bogoliubov) = {n_k_bog}")
    pr(f"  S per mode = {S_matter_per_mode:.6f} nats")
    pr(f"  S per cell (8 modes) = {S_matter_per_cell:.6f} nats")
    pr(f"  S matter total (32 cells) = {S_matter_total_uniform:.4f} nats")
    pr(f"  S matter SAME in uniform and inhomogeneous (global quench)")

    out['S_matter_per_mode'] = np.array(S_matter_per_mode)
    out['S_matter_total'] = np.array(S_matter_total_uniform)

    # ======================================================================
    #  Step 4: Generalized entropy comparison
    # ======================================================================
    pr("\n" + "=" * 78)
    pr("STEP 4: GENERALIZED ENTROPY COMPARISON")
    pr("=" * 78)

    # S_gen = S_grav + S_matter
    # S_grav is the spectral action (playing role of A/4G in Jacobson formulation)
    # S_matter is from Bogoliubov excitations

    # Uniform configuration (32 cells, all at tau_fold):
    S_gen_uniform = N_cells * S_uniform + S_matter_total_uniform

    # Inhomogeneous configuration:
    # N_void cells at tau_void, N_wall cells at tau_wall
    N_void = int(round(f_void * N_cells))  # = 24
    N_wall = N_cells - N_void               # = 8

    S_gen_inhomog = N_void * S_void + N_wall * S_wall + S_matter_total_inhomog

    Delta_S_gen = S_gen_inhomog - S_gen_uniform

    pr(f"  N_void = {N_void}, N_wall = {N_wall}")
    pr(f"\n  UNIFORM:")
    pr(f"    S_grav = {N_cells} * {S_uniform:.2f} = {N_cells * S_uniform:.2f}")
    pr(f"    S_matter = {S_matter_total_uniform:.4f}")
    pr(f"    S_gen = {S_gen_uniform:.2f}")
    pr(f"\n  INHOMOGENEOUS:")
    pr(f"    S_grav = {N_void}*{S_void:.2f} + {N_wall}*{S_wall:.2f} = {N_void*S_void + N_wall*S_wall:.2f}")
    pr(f"    S_matter = {S_matter_total_inhomog:.4f}")
    pr(f"    S_gen = {S_gen_inhomog:.2f}")
    pr(f"\n  Delta_S_gen = S_inhomog - S_uniform = {Delta_S_gen:.4f}")
    pr(f"  Fractional = Delta_S_gen / S_gen_uniform = {Delta_S_gen / S_gen_uniform:.2e}")

    # The sign of Delta_S_gen determines the GSL verdict:
    # If Delta_S_gen > 0: inhomogeneity has MORE entropy, GSL SATISFIED
    # If Delta_S_gen < 0: inhomogeneity has LESS entropy, GSL VIOLATED
    # (for the transition uniform -> inhomogeneous)

    out['S_gen_uniform'] = np.array(S_gen_uniform)
    out['S_gen_inhomog'] = np.array(S_gen_inhomog)
    out['Delta_S_gen'] = np.array(Delta_S_gen)

    # ======================================================================
    #  Step 5: Entropy production rate during structure formation
    # ======================================================================
    pr("\n" + "=" * 78)
    pr("STEP 5: ENTROPY PRODUCTION RATE")
    pr("=" * 78)

    # Model the development of inhomogeneity as a gradual process:
    # delta_tau(t) grows from 0 (uniform) to delta_tau_eff (full timescape).
    # Parameterize by epsilon in [0, 1]: delta_tau(t) = epsilon * delta_tau_eff

    N_eps = 500
    epsilon = np.linspace(0, 1, N_eps)
    S_gen_eps = np.zeros(N_eps)

    for i, eps in enumerate(epsilon):
        dv = eps * d_v
        dw = eps * d_w
        tv = tau_fold - dv
        tw = tau_fold + dw
        Sv = S_spec(tv)
        Sw = S_spec(tw)
        S_gen_eps[i] = N_void * Sv + N_wall * Sw + S_matter_total_uniform

    # Check monotonicity
    dS_deps = np.diff(S_gen_eps) / np.diff(epsilon)
    n_negative = np.sum(dS_deps < 0)
    min_dS = np.min(dS_deps)
    max_dS = np.max(dS_deps)

    pr(f"  Swept epsilon from 0 to 1 in {N_eps} steps")
    pr(f"  S_gen(eps=0) = {S_gen_eps[0]:.4f}")
    pr(f"  S_gen(eps=1) = {S_gen_eps[-1]:.4f}")
    pr(f"  dS/deps: min = {min_dS:.4f}, max = {max_dS:.4f}")
    pr(f"  Negative steps: {n_negative} / {N_eps - 1}")

    if n_negative == 0:
        monotonic = "MONOTONICALLY NON-DECREASING"
    else:
        monotonic = f"VIOLATED ({n_negative} negative steps)"

    pr(f"  Monotonicity: {monotonic}")

    # The production rate at full inhomogeneity:
    # dS_gen/dt = dS_gen/d(delta_tau) * d(delta_tau)/dt
    # dS_gen/d(delta_tau) at eps=1:
    dS_gen_d_delta_tau = dS_deps[-1] / delta_tau_eff  # chain rule

    # Structure formation timescale: ~Gyr for cosmic web
    # In M_KK units: 1 Gyr ~ 10^{50} M_KK^{-1} (for M_KK ~ 10^{16} GeV)
    t_struct_Gyr = 5.0  # typical structure formation timescale  # (local)
    t_struct_MKK = t_struct_Gyr * 3.156e16 / (hbar_SI / (M_KK * 1.602e-10))
    # Actually: 1/M_KK in seconds = hbar/(M_KK * GeV_to_J)
    # t_MKK = hbar_SI / (M_KK * 1.602e-10) = 1.054e-34 / (7.43e16 * 1.602e-10)
    t_MKK_seconds = hbar_SI / (M_KK * 1.602176634e-10)  # seconds per M_KK^{-1}
    t_struct_seconds = t_struct_Gyr * 3.156e16  # Gyr to seconds
    t_struct_in_MKK = t_struct_seconds / t_MKK_seconds

    delta_tau_rate = delta_tau_eff / t_struct_in_MKK  # dtau/dt in M_KK units
    dS_gen_dt = dS_gen_d_delta_tau * delta_tau_rate

    pr(f"\n  Structure formation timescale: {t_struct_Gyr} Gyr")
    pr(f"  = {t_struct_in_MKK:.3e} M_KK^{{-1}}")
    pr(f"  d(delta_tau)/dt = {delta_tau_rate:.3e} M_KK")
    pr(f"  dS_gen/d(delta_tau) = {dS_gen_d_delta_tau:.4f} per M_KK^{{-1}}")
    pr(f"  dS_gen/dt = {dS_gen_dt:.3e} M_KK")

    out['epsilon'] = epsilon
    out['S_gen_eps'] = S_gen_eps
    out['n_negative_steps'] = np.array(n_negative)
    out['min_dS_deps'] = np.array(min_dS)
    out['dS_gen_dt'] = np.array(dS_gen_dt)

    # ======================================================================
    #  Step 6: Bekenstein bound cross-check
    # ======================================================================
    pr("\n" + "=" * 78)
    pr("STEP 6: BEKENSTEIN BOUND CROSS-CHECK")
    pr("=" * 78)

    # The Bekenstein bound: S <= 2*pi*R*E
    # In a cell of the fabric, R ~ (volume)^{1/3}, E ~ energy content
    # The question: does the tau-variation ITSELF carry enough energy to
    # violate the Bekenstein bound?
    #
    # Energy in the tau gradient: E_grad = (1/2) * Z_fold * (delta_tau / L)^2 * L^3
    # where L is the cell size.
    #
    # In M_KK units, the fabric has 32 cells.
    # Cell volume ~ Vol_total / N_cells. If the total volume is L_total^3,
    # then L_cell ~ L_total / N_cells^{1/3}
    #
    # The gradient energy per cell: E_grad_cell = (1/2) * Z_fold * (delta_tau_eff / L_cell)^2 * L_cell^3
    # = (1/2) * Z_fold * delta_tau_eff^2 * L_cell
    #
    # For the Bekenstein bound: S_cell <= 2*pi * L_cell * E_cell
    # With S_cell ~ S_fold (spectral action per cell ~ 250,000)
    # and E_cell ~ E_grad_cell + E_matter_cell

    # The Bekenstein ratio:
    # S_cell / (2*pi*R*E) where R and E are in M_KK units
    # We don't have L_cell directly, but from the Hubble radius:
    # At M_KK ~ 10^{16} GeV, the Hubble radius H^{-1} ~ 10^{26} m
    # L_cell ~ H^{-1} / N_cells^{1/3} ~ 10^{25} m ~ 10^{57} l_P ~ 10^{40} M_KK^{-1}
    H_inv_m = c_light / (H_0_km_s_Mpc * 1e3 / (Mpc_to_m))  # Hubble radius in meters
    H_inv_MKK = H_inv_m / (hbar_SI * c_light / (M_KK * 1.602176634e-10))  # in M_KK^{-1}
    L_cell_MKK = H_inv_MKK / N_cells**(1.0/3)

    # Gradient energy per cell
    E_grad_cell = 0.5 * Z_fold * delta_tau_eff**2 * L_cell_MKK

    # Bekenstein bound
    S_grav_per_cell = S_fold  # spectral action per cell
    S_Bek_bound = 2 * np.pi * L_cell_MKK * E_grad_cell
    Bek_ratio = S_grav_per_cell / S_Bek_bound

    pr(f"  H^{{-1}} = {H_inv_m:.3e} m")
    pr(f"  H^{{-1}} = {H_inv_MKK:.3e} M_KK^{{-1}}")
    pr(f"  L_cell = {L_cell_MKK:.3e} M_KK^{{-1}}")
    pr(f"  E_grad per cell = {E_grad_cell:.3e} M_KK")
    pr(f"  S_grav per cell = {S_grav_per_cell:.2f}")
    pr(f"  Bekenstein bound (2*pi*R*E) = {S_Bek_bound:.3e}")
    pr(f"  Bekenstein ratio S/S_Bek = {Bek_ratio:.3e}")

    if Bek_ratio < 1:
        bek_verdict = "SATISFIED (S < S_Bek)"
    else:
        bek_verdict = f"VIOLATED (S/S_Bek = {Bek_ratio:.2e})"

    pr(f"  Bekenstein bound: {bek_verdict}")

    out['L_cell_MKK'] = np.array(L_cell_MKK)
    out['E_grad_cell'] = np.array(E_grad_cell)
    out['Bek_ratio'] = np.array(Bek_ratio)

    # ======================================================================
    #  Step 7: Holographic entropy bound (Bousso)
    # ======================================================================
    pr("\n" + "=" * 78)
    pr("STEP 7: BOUSSO COVARIANT ENTROPY BOUND")
    pr("=" * 78)

    # The Bousso bound: S_light-sheet <= A / (4 G)
    # where A is the area of the bounding surface.
    #
    # For a cell of the cosmic web:
    # A_cell ~ L_cell^2
    # S_Bousso = A_cell / (4 * G_eff)
    # In M_KK units: G_eff ~ 1/(a2_fold * M_KK^2)
    # so S_Bousso ~ a2_fold * M_KK^2 * L_cell^2
    #
    # Actually in Planck units: S_Bousso = A / (4 * l_P^2)
    # A = L_cell^2 (in meters)
    L_cell_m = L_cell_MKK * hbar_SI * c_light / (M_KK * 1.602176634e-10)
    A_cell_m2 = L_cell_m**2
    S_Bousso = A_cell_m2 / (4 * l_Planck**2)

    pr(f"  L_cell = {L_cell_m:.3e} m")
    pr(f"  A_cell = {A_cell_m2:.3e} m^2")
    pr(f"  S_Bousso = A/(4*l_P^2) = {S_Bousso:.3e}")
    pr(f"  S_matter per cell = {S_matter_per_cell:.4f} nats")
    pr(f"  S_grav per cell = {S_grav_per_cell:.2f}")
    pr(f"  Holographic saturation = S/(S_Bousso) = {(S_grav_per_cell + S_matter_per_cell)/S_Bousso:.3e}")

    out['S_Bousso'] = np.array(S_Bousso)

    # ======================================================================
    #  Step 8: The physical GSL constraint on delta_G/G
    # ======================================================================
    pr("\n" + "=" * 78)
    pr("STEP 8: GSL CONSTRAINT ON delta_G/G MAGNITUDE")
    pr("=" * 78)

    # The real GSL constraint comes from the SECOND LAW applied to the
    # process of tau-homogenization:
    # If the universe starts inhomogeneous (timescape) and equilibrates to
    # uniform tau, the entropy must INCREASE.
    # Conversely, if the universe starts uniform and develops inhomogeneity,
    # the entropy must INCREASE.
    #
    # From Step 4: Delta_S_gen > 0 (convexity of S_spec means inhomogeneity
    # has MORE spectral entropy). So the GSL is SATISFIED for the process
    # uniform -> inhomogeneous.
    #
    # But what about the REVERSE process? If tau homogenizes (e.g., late-time
    # relaxation), then S_gen would DECREASE -- violating the GSL.
    # This means: ONCE the tau-inhomogeneity develops, the GSL FORBIDS
    # homogenization. The timescape is an entropy trap.
    #
    # However, the REAL constraint is on whether the OBSERVATIONAL consequence
    # (delta_G/G = -0.53) is independently excluded. The LUNAR LASER RANGING
    # bound on G-dot/G ~ 10^{-13} yr^{-1} already constrains this.
    # But the GSL gives a THERMODYNAMIC constraint, not an observational one.

    # Scan delta_G/G from 0 to 1 and compute Delta_S_gen
    dG_scan = np.linspace(0, 1.0, 200)
    Delta_S_scan = np.zeros_like(dG_scan)

    for i, dG in enumerate(dG_scan):
        # Invert: delta_G/G = -frac_da2 * delta_tau
        # so delta_tau = |dG| / frac_da2
        dt_eff = dG / abs(frac_da2)
        dvi = dt_eff
        dwi = (f_void / f_wall) * dvi
        tvi = tau_fold - dvi
        twi = tau_fold + dwi
        Svi = S_spec(tvi)
        Swi = S_spec(twi)
        S_inh = N_void * Svi + N_wall * Swi
        S_uni = N_cells * S_uniform
        Delta_S_scan[i] = S_inh - S_uni

    pr(f"  Scanning delta_G/G from 0 to 1.0:")
    pr(f"  Delta_S_gen(delta_G/G=0) = {Delta_S_scan[0]:.4f}")
    pr(f"  Delta_S_gen(delta_G/G=0.1) = {Delta_S_scan[20]:.4f}")
    pr(f"  Delta_S_gen(delta_G/G=0.3) = {Delta_S_scan[60]:.4f}")
    pr(f"  Delta_S_gen(delta_G/G=0.526) = {Delta_S_scan[min(105, 199)]:.4f}")
    pr(f"  Delta_S_gen(delta_G/G=1.0) = {Delta_S_scan[-1]:.4f}")
    pr(f"  All positive? {np.all(Delta_S_scan >= 0)}")
    pr(f"  Minimum = {np.min(Delta_S_scan):.6f}")

    # The convexity of S_spec means Delta_S is ALWAYS positive for any delta_G/G.
    # The GSL does NOT constrain the magnitude of delta_G/G!
    # Thermodynamics ALLOWS arbitrary tau-inhomogeneity.

    out['dG_scan'] = dG_scan
    out['Delta_S_scan'] = Delta_S_scan

    # ======================================================================
    #  Step 9: Clausius inequality check
    # ======================================================================
    pr("\n" + "=" * 78)
    pr("STEP 9: CLAUSIUS INEQUALITY (IRREVERSIBILITY)")
    pr("=" * 78)

    # The Clausius inequality: dS >= delta_Q / T
    # For the development of inhomogeneity, the heat flow is between
    # void and wall cells. The Clausius inequality requires that
    # heat flows from hot to cold (or entropy is produced in the process).
    #
    # In the framework:
    # T_acoustic = 0.112 M_KK (from GGE, S42/S47)
    # If voids are at T_void and walls at T_wall, with tau variation
    # affecting the local temperature, then we need:
    # T_void != T_wall for heat to flow.
    #
    # From the no-hair analysis (NOHAIR-40 FAIL):
    # T varies 64.6% across modes due to gap hierarchy.
    # But the SPATIAL T-variation from tau-shift is:
    # delta_T/T ~ delta_tau * (dT/dtau) / T
    #
    # The acoustic temperature T_a = alpha * (spectral_function)
    # varies with tau. From T-ACOUSTIC-40:
    # T_a/T_Gibbs = 0.993 (acoustic metric) at the fold.
    # The tau-dependence comes through the gap: Delta(tau).

    # For a BCS system, T_BCS ~ Delta(tau) / (k_B * f(gap_ratio))
    # Near the fold, Delta ~ sqrt(|tau - tau_fold|) (mean-field BCS)
    # So delta_T/T ~ (1/2) * delta_tau / (tau - tau_fold)
    # At the fold itself, Delta -> 0 and T is ill-defined.
    #
    # Instead, use the GGE temperature T_acoustic = 0.112 M_KK.
    # The spatial variation: delta_T/T ~ delta_tau / tau_fold * (some O(1) factor)
    delta_T_over_T = delta_tau_eff / tau_fold  # ~ 2.8%
    T_void = T_acoustic * (1 - delta_T_over_T / 2)
    T_wall = T_acoustic * (1 + delta_T_over_T / 2)

    # Entropy produced by heat flow from wall to void:
    # sigma_Clausius = Q * (1/T_void - 1/T_wall)
    # Q ~ heat transported ~ T * S_matter_per_cell * delta_T/T
    Q_transported = T_acoustic * S_matter_per_cell * delta_T_over_T
    sigma_Clausius = Q_transported * (1/T_void - 1/T_wall)

    pr(f"  T_acoustic = {T_acoustic:.4f} M_KK")
    pr(f"  delta_T/T = {delta_T_over_T:.4f}")
    pr(f"  T_void = {T_void:.6f} M_KK")
    pr(f"  T_wall = {T_wall:.6f} M_KK")
    pr(f"  Q transported ~ {Q_transported:.6f} M_KK")
    pr(f"  sigma_Clausius = {sigma_Clausius:.6e} nats")
    pr(f"  (positive = entropy production, GSL satisfied)")

    clausius_sign = "POSITIVE (irreversible, GSL OK)" if sigma_Clausius > 0 else "NEGATIVE (VIOLATION)"
    pr(f"  Clausius: {clausius_sign}")

    out['delta_T_over_T'] = np.array(delta_T_over_T)
    out['sigma_Clausius'] = np.array(sigma_Clausius)

    # ======================================================================
    #  Step 10: Gate verdict
    # ======================================================================
    pr("\n" + "=" * 78)
    pr("STEP 10: GATE VERDICT")
    pr("=" * 78)

    # Summary of findings:
    # 1. S_spec is CONVEX at fold (d2S > 0, HESS-40).
    #    => Inhomogeneous tau has MORE spectral entropy than uniform.
    #    => Delta_S_grav > 0 for any tau-inhomogeneity.
    #
    # 2. Matter entropy is UNCHANGED (global quench, same n_k everywhere).
    #    => Delta_S_matter = 0.
    #
    # 3. S_gen(inhomog) > S_gen(uniform) for all delta_G/G in [0, 1].
    #    => GSL SATISFIED for the process uniform -> inhomogeneous.
    #    => The timescape is NOT thermodynamically forbidden.
    #
    # 4. The entropy production is MONOTONICALLY INCREASING as inhomogeneity
    #    develops (0 negative steps out of 499).
    #
    # 5. The Bekenstein bound is trivially satisfied (S/S_Bek << 1).
    #
    # 6. Clausius inequality: sigma > 0 (heat flows correctly).
    #
    # THEREFORE: The GSL does NOT close the timescape mechanism.
    # The 53% G-variation is thermodynamically ALLOWED.
    # The closure of timescape (if any) must come from OBSERVATIONAL bounds
    # (lunar laser ranging, BBN, etc.), not from thermodynamics.

    gate_name = "GSL-TIMESCAPE-60"

    if Delta_S_gen > 0 and n_negative == 0:
        verdict = "FAIL"
        detail = (
            f"GSL SATISFIED. Delta_S_gen = +{Delta_S_gen:.2f} (inhomogeneity has MORE entropy). "
            f"Monotonic: 0/{N_eps-1} negative steps. "
            f"Convexity of S_spec (d2S = {d2S_fold:.0f} > 0, HESS-40) guarantees "
            f"<S(tau)> >= S(<tau>) by Jensen inequality. "
            f"Matter entropy unchanged (global quench). "
            f"Timescape NOT thermodynamically forbidden. "
            f"delta_G/G = {delta_G_over_G:.3f} must be constrained observationally, not thermodynamically."
        )
    elif Delta_S_gen < 0:
        verdict = "PASS"
        detail = (
            f"GSL VIOLATED. Delta_S_gen = {Delta_S_gen:.2f} (inhomogeneity has LESS entropy). "
            f"Timescape thermodynamically forbidden."
        )
    else:
        verdict = "INFO"
        detail = f"Marginal. Delta_S_gen = {Delta_S_gen:.4f}."

    pr(f"\n  GATE: {gate_name}")
    pr(f"  VERDICT: {verdict}")
    pr(f"  DETAIL: {detail}")
    pr(f"\n  Key numbers:")
    pr(f"    Delta_S_gen = {Delta_S_gen:.4f}")
    pr(f"    Delta_S_gen / S_gen = {Delta_S_gen / S_gen_uniform:.2e}")
    pr(f"    Negative steps = {n_negative} / {N_eps - 1}")
    pr(f"    Convexity: d2S/dtau2 = {d2S_fold:.0f} > 0 (HESS-40)")
    pr(f"    delta_G/G = {delta_G_over_G:.4f}")
    pr(f"    Bekenstein ratio = {Bek_ratio:.3e}")
    pr(f"    Clausius sigma = {sigma_Clausius:.3e}")

    out['gate_name'] = np.array([gate_name])
    out['gate_verdict'] = np.array([verdict])
    out['gate_detail'] = np.array([detail])
    out['verdict'] = np.array([verdict])

    # ======================================================================
    #  Plotting
    # ======================================================================
    pr("\n" + "=" * 78)
    pr("PLOTTING")
    pr("=" * 78)

    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(2, 2, figsize=(14, 10))
    fig.suptitle("GSL-TIMESCAPE-60: Generalized Second Law on Timescape", fontsize=14, fontweight="bold")

    # Panel 1: S_gen vs epsilon (inhomogeneity development)
    ax1 = axes[0, 0]
    ax1.plot(epsilon, S_gen_eps, 'b-', lw=2)
    ax1.axhline(S_gen_uniform, color='r', ls='--', lw=1, label=f'S_gen(uniform) = {S_gen_uniform:.0f}')
    ax1.set_xlabel(r'$\epsilon$ (inhomogeneity parameter)')
    ax1.set_ylabel(r'$S_{\rm gen}$')
    ax1.set_title(r'Generalized entropy vs inhomogeneity')
    ax1.legend(fontsize=9)
    ax1.grid(True, alpha=0.3)
    ax1.annotate(f'$\\Delta S$ = +{Delta_S_gen:.2f}',
                 xy=(0.6, 0.3), xycoords='axes fraction', fontsize=11,
                 bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.8))

    # Panel 2: Delta_S_gen vs delta_G/G
    ax2 = axes[0, 1]
    ax2.plot(dG_scan * 100, Delta_S_scan, 'b-', lw=2)
    ax2.axvline(abs(delta_G_over_G) * 100, color='r', ls='--', lw=1.5,
                label=f'Framework: |$\\delta G/G$| = {abs(delta_G_over_G)*100:.1f}%')
    ax2.axhline(0, color='gray', ls=':', lw=0.5)
    ax2.set_xlabel(r'$|\delta G / G|$ (%)')
    ax2.set_ylabel(r'$\Delta S_{\rm gen}$ (inhomog - uniform)')
    ax2.set_title(r'Entropy excess from inhomogeneity')
    ax2.legend(fontsize=9)
    ax2.grid(True, alpha=0.3)
    ax2.annotate('Convex S: always positive\n(Jensen inequality)',
                 xy=(0.05, 0.85), xycoords='axes fraction', fontsize=9,
                 bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    # Panel 3: dS/d(epsilon) — entropy production rate
    ax3 = axes[1, 0]
    eps_mid = 0.5 * (epsilon[:-1] + epsilon[1:])
    ax3.plot(eps_mid, dS_deps, 'g-', lw=2)
    ax3.axhline(0, color='red', ls='--', lw=1, label='GSL boundary')
    ax3.set_xlabel(r'$\epsilon$ (inhomogeneity parameter)')
    ax3.set_ylabel(r'$dS_{\rm gen}/d\epsilon$')
    ax3.set_title(r'Entropy production rate')
    ax3.legend(fontsize=9)
    ax3.grid(True, alpha=0.3)
    ax3.annotate(f'Negative steps: {n_negative}/{N_eps-1}',
                 xy=(0.05, 0.85), xycoords='axes fraction', fontsize=10,
                 color='green' if n_negative == 0 else 'red',
                 bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    # Panel 4: Summary text
    ax4 = axes[1, 1]
    ax4.axis('off')
    txt = (
        f"GATE: {gate_name}\n"
        f"VERDICT: {verdict}\n\n"
        f"Key findings:\n"
        f"  S_spec(tau) CONVEX at fold (d2S > 0)\n"
        f"  Jensen: <S(tau)> >= S(<tau>)\n"
        f"  => Delta_S_grav = +{Delta_S_gen:.2f}\n"
        f"  => Inhomogeneity has MORE entropy\n\n"
        f"  Matter S unchanged (global quench)\n"
        f"  Bekenstein: {Bek_ratio:.1e} << 1\n"
        f"  Clausius sigma = {sigma_Clausius:.2e}\n\n"
        f"Physical consequence:\n"
        f"  GSL does NOT constrain delta_G/G.\n"
        f"  53% G-variation thermodynamically\n"
        f"  ALLOWED. Closure must come from\n"
        f"  observational bounds, not entropy."
    )
    ax4.text(0.05, 0.95, txt, transform=ax4.transAxes,
             fontsize=9, va='top', fontfamily='monospace',
             bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

    plt.tight_layout()
    plotpath = os.path.join(SCRIPT_DIR, "s60_gsl_timescape.png")
    plt.savefig(plotpath, dpi=150, bbox_inches='tight')
    pr(f"\nPlot saved: {plotpath}")

    # Save npz
    npzpath = os.path.join(SCRIPT_DIR, "s60_gsl_timescape.npz")
    np.savez(npzpath, **out)
    pr(f"Data saved: {npzpath}")

    elapsed = time.time() - t0
    pr(f"\nWall time: {elapsed:.2f}s")
    pr(f"\n=== GSL-TIMESCAPE-60 COMPLETE ===")

except Exception as e:
    import traceback
    pr(f"\n=== ERROR ===\n{traceback.format_exc()}")

finally:
    log.close()
