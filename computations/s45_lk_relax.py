#!/usr/bin/env python3
"""
s45_lk_relax.py — Landau-Khalatnikov Relaxation Dynamics (LK-RELAX-45)
========================================================================

Gate: LK-RELAX-45
  PASS: N_e > 10 during dwell (sufficient for observable signature)
  FAIL: N_e < 0.1
  INFO: N_e in [0.1, 10]

Physics:
  The Landau-Khalatnikov equation governs overdamped relaxation of the
  order parameter tau on the free energy landscape S_occ(tau):

      d(tau)/dt = -(1/tau_0) * dS_occ/dtau          (Eq. 1)

  where tau_0 is the microscopic relaxation time and S_occ is the
  occupied-state spectral action from s45_occ_spectral.npz.

  OCC-SPEC-45 = FAIL: S_occ(tau) is monotonically decreasing for all smooth
  cutoffs (exp, poly). No minimum exists. The LK force -dS_occ/dtau > 0
  everywhere, driving tau monotonically toward larger values.

  Despite the FAIL, this computation extracts:
    1. The LK velocity field v(tau) = d(tau)/dt at each tau
    2. The LK trajectory tau(t) by direct numerical integration
    3. The local deceleration a(tau) = dv/dtau * v = -(1/tau_0) d^2S/dtau^2 * v
    4. Whether any inflection point in S_occ produces transient slowing
       (i.e. a local maximum of |dS/dtau|^{-1}, the local dwell time)
    5. The transit time across the fold region [0.15, 0.25]
    6. N_e = H * t_transit (e-folds during transit)

  Reference: Landau & Khalatnikov, Dokl. Akad. Nauk SSSR 96, 469 (1954).
  Paper 09 in researchers/Landau/.

Session: 45
Agent: landau-condensed-matter-theorist
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import numpy as np
from scipy.interpolate import CubicSpline
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    tau_fold, H_fold, M_KK, G_DeWitt, M_ATDHFB,
    omega_att, dt_transit, v_terminal, S_fold,
    dS_fold, d2S_fold, Gamma_Langer_BCS, xi_BCS
)

# ============================================================================
#  1. Load occupied-state spectral action data
# ============================================================================

DATA_DIR = os.path.dirname(__file__)
d = np.load(os.path.join(DATA_DIR, 's45_occ_spectral.npz'), allow_pickle=True)

tau_vals = d['tau_values']       # (20,) tau grid
N_tau = len(tau_vals)

# We analyze multiple cutoff families and scales.
# Primary analysis: exponential cutoff at Lambda = 2.0 M_KK (mid-range).
# Cross-check: polynomial and sharp cutoffs at multiple Lambda.

cutoff_configs = []
for family in ['exp', 'poly', 'sharp']:
    for L in [1.5, 2.0, 3.0, 5.0, 10.0]:
        key_occ = f'S_occ_{family}_L{L}'
        key_vac = f'S_vac_{family}_L{L}'
        if key_occ in d and key_vac in d:
            cutoff_configs.append({
                'family': family, 'Lambda': L,
                'S_occ': d[key_occ], 'S_vac': d[key_vac],
                'label': f'{family}_L{L}'
            })

print(f"Loaded {len(cutoff_configs)} cutoff configurations")
print(f"tau grid: {N_tau} points, [{tau_vals[0]:.3f}, {tau_vals[-1]:.3f}]")

# Also load the total derivative decomposition
occ_change = d['occ_change_term']   # dn_k/dtau contribution
eval_change = d['eval_change_term'] # dlambda_k/dtau contribution
total_deriv = d['total_deriv']      # total dS_occ/dtau (finite difference)

# ============================================================================
#  2. Microscopic relaxation time tau_0
# ============================================================================
# In the LK equation, tau_0 is the microscopic relaxation time.
# For the spectral geometry on SU(3), the natural time scale is set by
# the modulus dynamics. Two independent estimates:
#
# (a) From the ATDHFB collective mass M and the spectral action curvature:
#     tau_0 ~ M / (d^2S/dtau^2) at the fold. This is the dissipative
#     friction coefficient in the Caldeira-Leggett sense.
#     tau_0^{(a)} = M_ATDHFB / d2S_fold = 1.695 / 317862.8 ~ 5.33e-6 M_KK^{-1}
#
# (b) From the Langer decay rate Gamma_L = 0.250 M_KK:
#     tau_0^{(b)} = 1/Gamma_L = 4.0 M_KK^{-1}
#
# (c) From the gradient stiffness Z_fold and terminal velocity:
#     tau_0^{(c)} = 1/omega_att = 1/1.430 = 0.699 M_KK^{-1}
#
# We compute for all three and report the range.

tau_0_estimates = {
    'ATDHFB/d2S': M_ATDHFB / d2S_fold,       # ~5.33e-6
    '1/Gamma_L': 1.0 / Gamma_Langer_BCS,      # ~4.0
    '1/omega_att': 1.0 / omega_att,            # ~0.699
}

print("\n--- Microscopic relaxation time tau_0 (M_KK^{-1} units) ---")
for name, val in tau_0_estimates.items():
    print(f"  {name:20s} = {val:.6e}")

# The physically motivated choice: the LK equation describes dissipative
# dynamics. The relevant friction is set by the coupling between the
# modulus (tau) and the thermal bath of KK modes. The ATDHFB mass over
# spectral curvature gives the purely geometric dissipation rate.
# But this is unreasonably fast (5e-6) — it assumes the entire spectral
# action provides the restoring force with perfect efficiency.
#
# The Langer rate is the many-body tunneling/activation rate, appropriate
# when the dynamics is dominated by BCS fluctuations.
#
# omega_att is the underdamped oscillation frequency at the fold minimum
# (if one existed). In the overdamped LK regime, 1/omega_att gives the
# damping timescale.
#
# We use 1/omega_att as the primary (it's the geometric attractor frequency
# from S38, fully determined by the spectral action), and report all three.

tau_0_primary = tau_0_estimates['1/omega_att']

# ============================================================================
#  3. Compute LK force and velocity for each cutoff config
# ============================================================================

results = {}

for cfg in cutoff_configs:
    label = cfg['label']
    S_occ = cfg['S_occ']
    S_vac = cfg['S_vac']

    # --- Spline interpolation for derivatives ---
    # Use cubic spline for smooth derivatives
    cs_occ = CubicSpline(tau_vals, S_occ)
    cs_vac = CubicSpline(tau_vals, S_vac)

    # Fine grid for analysis
    tau_fine = np.linspace(tau_vals[0] + 1e-6, tau_vals[-1] - 1e-6, 2000)

    # First and second derivatives
    dS_occ = cs_occ(tau_fine, 1)   # dS/dtau
    d2S_occ = cs_occ(tau_fine, 2)  # d^2S/dtau^2

    dS_vac = cs_vac(tau_fine, 1)
    d2S_vac = cs_vac(tau_fine, 2)

    # --- LK velocity: v(tau) = -(1/tau_0) dS_occ/dtau ---
    # Convention: dS_occ/dtau < 0 (monotonically decreasing), so v > 0
    v_lk = -(1.0 / tau_0_primary) * dS_occ

    # --- Check for monotonicity ---
    sign_changes_dS = np.sum(np.diff(np.sign(dS_occ)) != 0)
    is_monotone = (sign_changes_dS == 0)

    # --- Check for inflection points in S_occ ---
    # These are where d^2S/dtau^2 = 0, i.e., where the force changes character
    sign_changes_d2S = np.where(np.diff(np.sign(d2S_occ)) != 0)[0]
    inflection_taus = tau_fine[sign_changes_d2S] if len(sign_changes_d2S) > 0 else np.array([])

    # --- Local dwell time: proportional to 1/|dS/dtau| ---
    # Where dS/dtau is smallest in magnitude, the system moves slowest
    with np.errstate(divide='ignore'):
        local_dwell = np.abs(1.0 / dS_occ)
    # Find maximum of local_dwell (avoiding endpoints where spline extrapolation is poor)
    interior = (tau_fine > 0.02) & (tau_fine < 0.48)
    if np.any(interior & np.isfinite(local_dwell)):
        idx_max_dwell = np.argmax(np.where(interior & np.isfinite(local_dwell),
                                           local_dwell, 0))
        tau_max_dwell = tau_fine[idx_max_dwell]
        max_dwell_value = local_dwell[idx_max_dwell]
    else:
        tau_max_dwell = np.nan
        max_dwell_value = np.nan

    # --- Check for minimum in S_occ (should be FAIL for smooth cutoffs) ---
    # Look for dS/dtau = 0 with d^2S > 0
    zero_crossings = np.where(np.diff(np.sign(dS_occ)) > 0)[0]  # dS goes from - to +
    has_minimum = len(zero_crossings) > 0
    if has_minimum:
        tau_min = tau_fine[zero_crossings[0]]
        S_min = float(cs_occ(tau_min))
        # Barrier: maximum of S_occ to the right of minimum minus S at minimum
        S_right = S_occ[tau_vals > tau_min]
        if len(S_right) > 0:
            barrier = np.max(S_right) - S_min
        else:
            barrier = 0.0
    else:
        tau_min = np.nan
        S_min = np.nan
        barrier = 0.0

    # --- Integrate LK trajectory: d(tau)/dt = -(1/tau_0) dS_occ/dtau ---
    # Start at tau = 0.01 (just past origin), integrate until tau = 0.49
    def lk_rhs(t, y):
        tau_current = y[0]
        if tau_current < tau_vals[0] + 1e-4 or tau_current > tau_vals[-1] - 1e-4:
            return [0.0]
        dS = float(cs_occ(tau_current, 1))
        return [-(1.0 / tau_0_primary) * dS]

    def exit_event(t, y):
        return y[0] - 0.49  # triggers when tau reaches 0.49
    exit_event.terminal = True
    exit_event.direction = 1

    # Integration
    tau_start = 0.01
    t_span = (0.0, 10.0)  # M_KK^{-1} units; force is large so transit is fast

    sol = solve_ivp(lk_rhs, t_span, [tau_start],
                    method='RK45', dense_output=True,
                    max_step=0.01, rtol=1e-10, atol=1e-12,
                    events=[exit_event])

    # Extract trajectory
    t_traj = sol.t
    tau_traj = sol.y[0]

    # Transit time through fold region [0.15, 0.25]
    mask_fold = (tau_traj >= 0.15) & (tau_traj <= 0.25)
    if np.any(mask_fold):
        t_enter_fold = t_traj[np.argmax(mask_fold)]
        t_exit_fold = t_traj[len(mask_fold) - 1 - np.argmax(mask_fold[::-1])]
        t_transit_lk = t_exit_fold - t_enter_fold
    else:
        t_transit_lk = np.nan

    # Transit time through narrow region [0.17, 0.21] around tau_fold
    mask_narrow = (tau_traj >= 0.17) & (tau_traj <= 0.21)
    if np.any(mask_narrow):
        t_enter_narrow = t_traj[np.argmax(mask_narrow)]
        t_exit_narrow = t_traj[len(mask_narrow) - 1 - np.argmax(mask_narrow[::-1])]
        t_transit_narrow = t_exit_narrow - t_enter_narrow
    else:
        t_transit_narrow = np.nan

    # N_e during transit
    N_e_fold = H_fold * t_transit_lk if np.isfinite(t_transit_lk) else np.nan
    N_e_narrow = H_fold * t_transit_narrow if np.isfinite(t_transit_narrow) else np.nan

    # --- Force ratio: dS_occ/dtau vs dS_vac/dtau ---
    # The occupied-state force differs from vacuum force. Where?
    safe_dS_vac = np.where(np.abs(dS_vac) > 1e-10, dS_vac, np.nan)
    force_ratio = dS_occ / safe_dS_vac

    # --- Velocity at the fold ---
    idx_fold = np.argmin(np.abs(tau_fine - tau_fold))
    v_at_fold = v_lk[idx_fold]
    dS_at_fold = dS_occ[idx_fold]
    d2S_at_fold = d2S_occ[idx_fold]

    # --- Acceleration at fold: a = dv/dt = v * dv/dtau ---
    dv_dtau = -(1.0 / tau_0_primary) * d2S_occ
    accel = v_lk * dv_dtau
    accel_at_fold = accel[idx_fold]

    # --- Linearized dynamics near fold ---
    # If S_occ had a minimum at tau_fold, we'd have:
    #   omega_osc = sqrt(d2S_occ / tau_0)
    # Since d2S_occ > 0 at fold (concave up... check), this would give oscillation.
    # But S_occ has no minimum, so this is hypothetical.
    if d2S_at_fold > 0:
        omega_hyp = np.sqrt(d2S_at_fold / tau_0_primary)
        t_hyp = 2 * np.pi / omega_hyp
        N_e_hyp = H_fold * t_hyp
    else:
        omega_hyp = np.nan
        t_hyp = np.nan
        N_e_hyp = np.nan

    # Store results
    results[label] = {
        'S_occ': S_occ, 'S_vac': S_vac,
        'tau_fine': tau_fine, 'dS_occ': dS_occ, 'd2S_occ': d2S_occ,
        'v_lk': v_lk, 'dS_vac': dS_vac,
        'is_monotone': is_monotone, 'sign_changes_dS': sign_changes_dS,
        'inflection_taus': inflection_taus,
        'tau_max_dwell': tau_max_dwell, 'max_dwell_value': max_dwell_value,
        'has_minimum': has_minimum, 'tau_min': tau_min, 'S_min': S_min,
        'barrier': barrier,
        't_traj': t_traj, 'tau_traj': tau_traj,
        't_transit_lk': t_transit_lk, 't_transit_narrow': t_transit_narrow,
        'N_e_fold': N_e_fold, 'N_e_narrow': N_e_narrow,
        'v_at_fold': v_at_fold, 'dS_at_fold': dS_at_fold,
        'd2S_at_fold': d2S_at_fold, 'accel_at_fold': accel_at_fold,
        'omega_hyp': omega_hyp, 't_hyp': t_hyp, 'N_e_hyp': N_e_hyp,
        'force_ratio': force_ratio,
    }

# ============================================================================
#  4. Primary analysis: exp_L2.0
# ============================================================================

primary = results.get('exp_L2.0', results[list(results.keys())[0]])
print("\n" + "=" * 78)
print("LANDAU-KHALATNIKOV RELAXATION: PRIMARY ANALYSIS (exp, Lambda = 2.0 M_KK)")
print("=" * 78)

print(f"\ntau_0 (primary, 1/omega_att) = {tau_0_primary:.6f} M_KK^{{-1}}")
print(f"H_fold = {H_fold:.4f} M_KK")

print(f"\n--- S_occ monotonicity ---")
print(f"  Monotone (dS/dtau same sign): {primary['is_monotone']}")
print(f"  Sign changes in dS/dtau:      {primary['sign_changes_dS']}")
print(f"  Has minimum:                  {primary['has_minimum']}")
if primary['has_minimum']:
    print(f"  tau_min:                      {primary['tau_min']:.4f}")
    print(f"  Barrier:                      {primary['barrier']:.6e}")

print(f"\n--- Force at fold (tau = {tau_fold}) ---")
print(f"  dS_occ/dtau = {primary['dS_at_fold']:.6e}")
print(f"  d^2S_occ/dtau^2 = {primary['d2S_at_fold']:.6e}")
print(f"  LK velocity v = {primary['v_at_fold']:.6e} M_KK")
print(f"  LK acceleration a = {primary['accel_at_fold']:.6e} M_KK^2")

print(f"\n--- Inflection points ---")
if len(primary['inflection_taus']) > 0:
    for i, ti in enumerate(primary['inflection_taus']):
        print(f"  Inflection {i}: tau = {ti:.4f}")
else:
    print("  None found")

print(f"\n--- Transient trapping (max dwell point) ---")
print(f"  tau of max |1/dS| = {primary['tau_max_dwell']:.4f}")
print(f"  max |1/dS| value  = {primary['max_dwell_value']:.6e}")

print(f"\n--- Transit times ---")
print(f"  t_transit [0.15, 0.25] = {primary['t_transit_lk']:.6e} M_KK^{{-1}}")
print(f"  t_transit [0.17, 0.21] = {primary['t_transit_narrow']:.6e} M_KK^{{-1}}")
print(f"  N_e (fold region [0.15,0.25]) = {primary['N_e_fold']:.6e}")
print(f"  N_e (narrow [0.17,0.21])      = {primary['N_e_narrow']:.6e}")

print(f"\n--- Hypothetical oscillation (if minimum existed) ---")
print(f"  omega_hyp = sqrt(d2S/tau_0) = {primary['omega_hyp']:.4f} M_KK")
print(f"  T_hyp = 2pi/omega_hyp = {primary['t_hyp']:.6e} M_KK^{{-1}}")
print(f"  N_e_hyp = H * T_hyp = {primary['N_e_hyp']:.4f}")

# ============================================================================
#  5. Comparison across all tau_0 estimates
# ============================================================================

print("\n" + "=" * 78)
print("SENSITIVITY TO tau_0 (exp_L2.0)")
print("=" * 78)

cfg_primary = [c for c in cutoff_configs if c['label'] == 'exp_L2.0'][0]
cs_primary = CubicSpline(tau_vals, cfg_primary['S_occ'])

for tau_0_name, tau_0_val in tau_0_estimates.items():
    # Re-integrate with this tau_0
    def rhs(t, y, _tau0=tau_0_val):
        tc = y[0]
        if tc < tau_vals[0] + 1e-4 or tc > tau_vals[-1] - 1e-4:
            return [0.0]
        dS = float(cs_primary(tc, 1))
        return [-(1.0 / _tau0) * dS]

    def exit_ev2(t, y):
        return y[0] - 0.49
    exit_ev2.terminal = True
    exit_ev2.direction = 1

    # t_span scales with tau_0: slower friction = longer transit
    t_max = max(10.0, 1e5 * tau_0_val)
    sol2 = solve_ivp(rhs, (0, t_max), [0.01],
                     method='RK45', max_step=0.1, rtol=1e-10, atol=1e-12,
                     events=[exit_ev2])
    tau_tr2 = sol2.y[0]
    t_tr2 = sol2.t

    mask_f = (tau_tr2 >= 0.15) & (tau_tr2 <= 0.25)
    if np.any(mask_f):
        te = t_tr2[np.argmax(mask_f)]
        tx = t_tr2[len(mask_f) - 1 - np.argmax(mask_f[::-1])]
        dt_f = tx - te
    else:
        dt_f = np.nan

    Ne_f = H_fold * dt_f if np.isfinite(dt_f) else np.nan

    dS_fold_val = float(cs_primary(tau_fold, 1))
    v_fold_val = -(1.0 / tau_0_val) * dS_fold_val

    print(f"\n  tau_0 = {tau_0_val:.6e} M_KK^{{-1}}  ({tau_0_name})")
    print(f"    v(tau_fold) = {v_fold_val:.6e} M_KK")
    print(f"    t_transit [0.15,0.25] = {dt_f:.6e} M_KK^{{-1}}")
    print(f"    N_e = {Ne_f:.6e}")

# ============================================================================
#  6. Comparison across cutoff families
# ============================================================================

print("\n" + "=" * 78)
print("CUTOFF ROBUSTNESS")
print("=" * 78)

for label, res in sorted(results.items()):
    print(f"\n  {label:20s}  mono={res['is_monotone']}  "
          f"has_min={res['has_minimum']}  "
          f"v(fold)={res['v_at_fold']:+.4e}  "
          f"N_e(fold)={res['N_e_fold']:.4e}  "
          f"tau_max_dwell={res['tau_max_dwell']:.3f}")

# ============================================================================
#  7. Damping rate analysis
# ============================================================================
# The damping rate is the eigenvalue of the linearized LK equation:
#   Gamma_LK = (1/tau_0) * d^2S/dtau^2
# This gives the rate at which perturbations around a given tau relax.
# At a minimum (if one existed), Gamma_LK is the damping rate.
# Away from a minimum, Gamma_LK characterizes the local curvature.

print("\n" + "=" * 78)
print("DAMPING RATE PROFILE (exp_L2.0)")
print("=" * 78)

tau_fine = primary['tau_fine']
d2S = primary['d2S_occ']
Gamma_LK = (1.0 / tau_0_primary) * d2S  # M_KK units

# Sample at key tau values
for tau_sample in [0.05, 0.10, 0.15, 0.17, 0.19, 0.20, 0.22, 0.25, 0.30, 0.40]:
    idx = np.argmin(np.abs(tau_fine - tau_sample))
    print(f"  tau={tau_sample:.2f}:  Gamma_LK = {Gamma_LK[idx]:+.4e} M_KK  "
          f"  d2S = {d2S[idx]:+.4e}  "
          f"  dS = {primary['dS_occ'][idx]:+.4e}  "
          f"  v = {primary['v_lk'][idx]:+.4e}")

# ============================================================================
#  8. Occupation vs eigenvalue competition
# ============================================================================

print("\n" + "=" * 78)
print("DECOMPOSITION: dS_occ/dtau = (dn/dtau) term + (dlambda/dtau) term")
print("=" * 78)

# The total_deriv from the npz is computed at the raw tau grid
# occ_change_term: sum_k d_k * (dn_k/dtau) * f(lambda_k^2/Lambda^2)
# eval_change_term: sum_k d_k * n_k * df/dlambda * (dlambda_k/dtau)
# These are from finite differences, so endpoints may be zero

for i, tau in enumerate(tau_vals):
    if total_deriv[i] != 0:
        occ_frac = occ_change[i] / total_deriv[i] * 100 if total_deriv[i] != 0 else 0
        eval_frac = eval_change[i] / total_deriv[i] * 100 if total_deriv[i] != 0 else 0
        print(f"  tau={tau:.3f}:  total={total_deriv[i]:+.2e}  "
              f"occ={occ_change[i]:+.2e} ({occ_frac:+.1f}%)  "
              f"eval={eval_change[i]:+.2e} ({eval_frac:+.1f}%)")

# ============================================================================
#  9. Gate verdict
# ============================================================================

print("\n" + "=" * 78)
print("GATE VERDICT: LK-RELAX-45")
print("=" * 78)

# The gate asks for N_e > 10 during "dwell". Since there is no minimum,
# there is no dwell. The transit N_e is the number of e-folds while the
# system passes through the fold region.

primary_Ne = primary['N_e_fold']
primary_Ne_narrow = primary['N_e_narrow']

print(f"\nN_e (fold region [0.15, 0.25]):   {primary_Ne:.6e}")
print(f"N_e (narrow region [0.17, 0.21]): {primary_Ne_narrow:.6e}")

# Assess across all tau_0
Ne_all = {}
for tau_0_name, tau_0_val in tau_0_estimates.items():
    dS_fold_val = float(cs_primary(tau_fold, 1))
    # Estimate transit time as delta_tau / v_at_fold
    v_fold_est = -(1.0 / tau_0_val) * dS_fold_val
    dt_est = 0.10 / abs(v_fold_est) if abs(v_fold_est) > 0 else np.inf
    Ne_est = H_fold * dt_est
    Ne_all[tau_0_name] = Ne_est
    print(f"  tau_0={tau_0_name:20s}:  v_fold={v_fold_est:+.4e}  "
          f"dt_est={dt_est:.4e}  N_e_est={Ne_est:.4e}")

# Maximum N_e across all tau_0 choices
Ne_max = max(Ne_all.values())
print(f"\nMaximum N_e across tau_0 choices: {Ne_max:.4e}")

if primary_Ne > 10:
    verdict = 'PASS'
elif primary_Ne < 0.1:
    verdict = 'FAIL'
else:
    verdict = 'INFO'

# Override: check if any tau_0 gives N_e > 0.1
if Ne_max > 10:
    verdict_any = 'PASS'
elif Ne_max < 0.1:
    verdict_any = 'FAIL'
else:
    verdict_any = 'INFO'

print(f"\nVerdict (primary tau_0 = 1/omega_att): {verdict}")
print(f"Verdict (most favorable tau_0):        {verdict_any}")
print(f"\nPhysical interpretation:")
if verdict == 'FAIL':
    print("  No minimum in S_occ(tau). The LK force drives tau monotonically upward.")
    print("  The system passes through the fold without trapping or dwell.")
    print(f"  Transit velocity at fold: {primary['v_at_fold']:.4e} M_KK")
    print(f"  The occupation-number weighting does not reverse the vacuum monotonicity.")
    print(f"  The BCS-active modes (8 of 1232) contribute < 0.016% of S_occ, too few")
    print(f"  to overcome the 1224-mode geometric tide.")

# ============================================================================
#  10. Save results
# ============================================================================

save_dict = {
    # Grid
    'tau_values': tau_vals,
    'tau_fine': primary['tau_fine'],

    # Primary (exp_L2.0)
    'S_occ_primary': cfg_primary['S_occ'],
    'dS_occ_primary': primary['dS_occ'],
    'd2S_occ_primary': primary['d2S_occ'],
    'v_lk_primary': primary['v_lk'],
    'Gamma_LK_primary': Gamma_LK,

    # Trajectory
    't_traj': primary['t_traj'],
    'tau_traj': primary['tau_traj'],

    # Key scalars
    'tau_0_primary': np.array([tau_0_primary]),
    'tau_0_ATDHFB': np.array([tau_0_estimates['ATDHFB/d2S']]),
    'tau_0_Langer': np.array([tau_0_estimates['1/Gamma_L']]),
    'tau_0_omega': np.array([tau_0_estimates['1/omega_att']]),

    'v_at_fold': np.array([primary['v_at_fold']]),
    'dS_at_fold': np.array([primary['dS_at_fold']]),
    'd2S_at_fold': np.array([primary['d2S_at_fold']]),
    'accel_at_fold': np.array([primary['accel_at_fold']]),

    'N_e_fold': np.array([primary['N_e_fold']]),
    'N_e_narrow': np.array([primary['N_e_narrow']]),
    't_transit_fold': np.array([primary['t_transit_lk']]),
    't_transit_narrow': np.array([primary['t_transit_narrow']]),

    'omega_hyp': np.array([primary['omega_hyp']]),
    'N_e_hyp': np.array([primary['N_e_hyp']]),

    'is_monotone': np.array([primary['is_monotone']]),
    'has_minimum': np.array([primary['has_minimum']]),

    # Decomposition (raw grid)
    'occ_change_term': occ_change,
    'eval_change_term': eval_change,
    'total_deriv_raw': total_deriv,

    # Verdict
    'verdict': np.array([verdict]),
    'verdict_any_tau0': np.array([verdict_any]),
}

np.savez(os.path.join(DATA_DIR, 's45_lk_relax.npz'), **save_dict)
print(f"\nSaved: s45_lk_relax.npz")

# ============================================================================
#  11. Diagnostic plots
# ============================================================================

fig, axes = plt.subplots(3, 2, figsize=(14, 16))
fig.suptitle('LK-RELAX-45: Landau-Khalatnikov Relaxation Dynamics\n'
             f'(exp cutoff, Lambda = 2.0 M_KK, tau_0 = {tau_0_primary:.4f} M_KK$^{{-1}}$)',
             fontsize=13, fontweight='bold')

# (a) S_occ(tau) for multiple cutoffs
ax = axes[0, 0]
for label, res in sorted(results.items()):
    if 'exp' in label:
        ax.plot(tau_vals, res['S_occ'] / res['S_occ'][0], '-o', ms=3, label=label)
ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5, label=f'tau_fold={tau_fold}')
ax.set_xlabel('tau')
ax.set_ylabel('S_occ / S_occ(0)')
ax.set_title('(a) Occupied-state spectral action (exp cutoffs)')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# (b) LK force: -dS_occ/dtau
ax = axes[0, 1]
ax.plot(primary['tau_fine'], -primary['dS_occ'], 'b-', lw=1.5, label='$-dS_{occ}/d\\tau$ (force)')
ax.plot(primary['tau_fine'], -primary['dS_vac'], 'r--', lw=1, alpha=0.6, label='$-dS_{vac}/d\\tau$')
ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5)
ax.set_xlabel('tau')
ax.set_ylabel('Force = $-dS/d\\tau$')
ax.set_title('(b) LK driving force')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# (c) LK velocity v(tau)
ax = axes[1, 0]
ax.plot(primary['tau_fine'], primary['v_lk'], 'b-', lw=1.5)
ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5)
ax.axhline(0, color='k', lw=0.5)
ax.set_xlabel('tau')
ax.set_ylabel('$v = d\\tau/dt$ [M_KK]')
ax.set_title(f'(c) LK velocity (tau_0 = 1/omega_att)')
ax.grid(True, alpha=0.3)

# (d) LK trajectory tau(t)
ax = axes[1, 1]
ax.plot(primary['t_traj'], primary['tau_traj'], 'b-', lw=2)
ax.axhline(tau_fold, color='gray', ls='--', alpha=0.5, label=f'tau_fold')
ax.axhline(0.15, color='green', ls=':', alpha=0.5, label='fold region')
ax.axhline(0.25, color='green', ls=':', alpha=0.5)
ax.set_xlabel('t [M_KK$^{-1}$]')
ax.set_ylabel('tau(t)')
ax.set_title('(d) LK trajectory from tau_0=0.01')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# (e) Damping rate Gamma_LK(tau)
ax = axes[2, 0]
ax.plot(primary['tau_fine'], Gamma_LK, 'r-', lw=1.5)
ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5)
ax.axhline(0, color='k', lw=0.5)
ax.set_xlabel('tau')
ax.set_ylabel('$\\Gamma_{LK} = d^2S/(\\tau_0 d\\tau^2)$ [M_KK]')
ax.set_title('(e) Damping rate')
ax.grid(True, alpha=0.3)

# (f) Decomposition: occupation vs eigenvalue contributions
ax = axes[2, 1]
mask_nonzero = total_deriv != 0
tau_nz = tau_vals[mask_nonzero]
occ_nz = occ_change[mask_nonzero]
eval_nz = eval_change[mask_nonzero]
total_nz = total_deriv[mask_nonzero]

ax.plot(tau_nz, occ_nz, 'bs-', ms=4, label='$dn_k/d\\tau$ term')
ax.plot(tau_nz, eval_nz, 'r^-', ms=4, label='$d\\lambda_k/d\\tau$ term')
ax.plot(tau_nz, total_nz, 'ko-', ms=4, label='total $dS_{occ}/d\\tau$')
ax.axvline(tau_fold, color='gray', ls='--', alpha=0.5)
ax.axhline(0, color='k', lw=0.5)
ax.set_xlabel('tau')
ax.set_ylabel('dS_occ/dtau contributions')
ax.set_title('(f) Force decomposition: occupation vs eigenvalue')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig(os.path.join(DATA_DIR, 's45_lk_relax.png'), dpi=150, bbox_inches='tight')
print(f"Saved: s45_lk_relax.png")

print("\n--- DONE ---")
