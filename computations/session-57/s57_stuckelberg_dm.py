#!/usr/bin/env python3
"""
s57_stuckelberg_dm.py — STUCKELBERG-DM-57 (W3-10)
====================================================
Gate: INFO — does Stuckelberg interference at intermediate tau
produce a new DM channel?

Method:
  1. Load 2-cell TB eigenvalues (32 levels, 50 tau points)
  2. Identify all level quasi-crossings in [0.10, 0.40]
  3. For consecutive quasi-crossings on same level pair:
     compute Stuckelberg phase phi_S = integral(Delta(tau') dtau')
  4. Compute P_Stuckelberg = 4*P_LZ*(1-P_LZ)*sin^2(phi_S/2 + phi_Stokes)
  5. Map enhanced/suppressed P_exc vs tau

Input:
  - s54_tb_hamiltonian.npz (32 TB eigenvalues at 50 tau)
  - canonical_constants.py

Output:
  - s57_stuckelberg_dm.npz
  - Console results for working paper

Session 57, Task W3-10 (Kaku)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from scipy.integrate import trapezoid
from scipy.signal import argrelmin
from canonical_constants import (
    tau_fold, E_cond, H_fold, v_terminal, dt_transit,
    omega_tau, S_inst, PI
)

# ============================================================================
#  1. Load TB eigenvalues
# ============================================================================

data = np.load(os.path.join(os.path.dirname(__file__), 's54_tb_hamiltonian.npz'),
               allow_pickle=True)

tau_all = data['tau_values']       # (50,)
eig_all = data['eigenvalues']      # (50, 32) — sorted ascending at each tau
N_tau = len(tau_all)
N_levels = eig_all.shape[1]

print(f"Loaded: {N_tau} tau points, {N_levels} levels")
print(f"tau range: [{tau_all[0]:.4f}, {tau_all[-1]:.4f}]")
print(f"dtau = {tau_all[1]-tau_all[0]:.6f}")

# ============================================================================
#  2. Compute all pairwise gaps and identify quasi-crossings
# ============================================================================

# Focus on tau in [0.10, 0.40] where the fold dynamics occur
tau_min, tau_max = 0.10, 0.40
mask = (tau_all >= tau_min) & (tau_all <= tau_max)
tau_sel = tau_all[mask]
eig_sel = eig_all[mask]
idx_sel = np.where(mask)[0]
N_sel = len(tau_sel)

print(f"\nFocal region: tau in [{tau_min}, {tau_max}], {N_sel} points")

# Compute gaps between ALL consecutive levels at each tau
# gap[t, k] = E_{k+1}(tau_t) - E_k(tau_t)
gaps = np.diff(eig_sel, axis=1)  # (N_sel, 31)

print(f"\nGap matrix: {gaps.shape}")
print(f"Min gap anywhere: {gaps.min():.6f}")
print(f"Max gap anywhere: {gaps.max():.6f}")

# A quasi-crossing between levels k and k+1 occurs where gap[t,k] has a local minimum
# We look at every level pair
quasi_crossings = []

for k in range(N_levels - 1):
    gap_k = gaps[:, k]  # gap between level k and k+1 over tau

    # Find local minima using argrelmin (with order=1, nearest neighbors)
    # Also check endpoints
    local_mins = argrelmin(gap_k, order=1)[0]

    for idx in local_mins:
        gap_min_val = gap_k[idx]
        tau_cross = tau_sel[idx]

        # Record all quasi-crossings (we'll filter by strength later)
        quasi_crossings.append({
            'level_lo': k,
            'level_hi': k + 1,
            'tau_idx_sel': idx,      # index in the selected tau array
            'tau_idx_all': idx_sel[idx],  # index in full tau array
            'tau': tau_cross,
            'gap_min': gap_min_val,
            'E_lo': eig_sel[idx, k],
            'E_hi': eig_sel[idx, k+1],
        })

print(f"\nTotal quasi-crossings found: {len(quasi_crossings)}")

# Also look for non-adjacent level pairs with small gaps
# These are relevant for multi-level Stuckelberg interference
non_adj_crossings = []
for k in range(N_levels):
    for l in range(k+2, min(k+5, N_levels)):  # up to 4 levels apart
        gap_kl = eig_sel[:, l] - eig_sel[:, k]
        local_mins = argrelmin(gap_kl, order=1)[0]
        for idx in local_mins:
            gap_min_val = gap_kl[idx]
            if gap_min_val < 1.0:  # only record if gap is reasonably small
                non_adj_crossings.append({
                    'level_lo': k,
                    'level_hi': l,
                    'tau_idx_sel': idx,
                    'tau': tau_sel[idx],
                    'gap_min': gap_min_val,
                })

print(f"Non-adjacent quasi-crossings (gap < 1.0): {len(non_adj_crossings)}")

# Sort by gap size (smallest = closest approach)
quasi_crossings.sort(key=lambda x: x['gap_min'])

print(f"\n{'='*70}")
print(f"TOP 20 QUASI-CROSSINGS (sorted by gap size)")
print(f"{'='*70}")
print(f"{'Rank':>4} {'Levels':>8} {'tau':>8} {'gap_min':>10} {'E_lo':>10} {'E_hi':>10}")
print(f"-" * 60)
for i, qc in enumerate(quasi_crossings[:20]):
    print(f"{i+1:4d} ({qc['level_lo']:2d},{qc['level_hi']:2d}) "
          f"{qc['tau']:8.5f} {qc['gap_min']:10.6f} "
          f"{qc['E_lo']:10.5f} {qc['E_hi']:10.5f}")

# ============================================================================
#  3. Landau-Zener parameters at each quasi-crossing
# ============================================================================

# The LZ formula: P_LZ = exp(-2*pi*gamma)
# where gamma = Delta^2 / (4 * |d(E_hi - E_lo)/dt|)
# and d/dt = (d/dtau) * (dtau/dt)
#
# From the transit: dtau/dt ~ omega_tau = 8.27 M_KK (from canonical constants)
# But for the TB Hamiltonian, eigenvalues are in M_KK units, tau is dimensionless
# So the velocity is v = |dDelta/dtau| * omega_tau

dtau = tau_all[1] - tau_all[0]

print(f"\n{'='*70}")
print(f"LANDAU-ZENER ANALYSIS")
print(f"{'='*70}")
print(f"Transit rate: omega_tau = {omega_tau:.3f} M_KK")
print(f"dtau = {dtau:.6f}")

lz_results = []

for qc in quasi_crossings:
    k = qc['level_lo']
    l = qc['level_hi']
    idx = qc['tau_idx_sel']

    # Compute d(gap)/dtau at the crossing using finite differences
    gap_series = eig_sel[:, l] - eig_sel[:, k]

    # Numerical derivative of gap at the crossing point
    if idx > 0 and idx < N_sel - 1:
        dgap_dtau = (gap_series[idx+1] - gap_series[idx-1]) / (2 * dtau)
    elif idx == 0:
        dgap_dtau = (gap_series[idx+1] - gap_series[idx]) / dtau
    else:
        dgap_dtau = (gap_series[idx] - gap_series[idx-1]) / dtau

    # For LZ, what matters is the slope of the DIABATIC levels.
    # At a quasi-crossing, the gap minimum gives:
    #   Delta_min = gap_min (the adiabatic gap)
    #   The diabatic level velocity difference can be estimated from the
    #   second derivative of the gap (curvature at minimum)
    #
    # More directly: LZ parameter gamma = (pi * Delta^2) / (2 * hbar * v_slope)
    # where v_slope = |d(E_diabatic_hi - E_diabatic_lo)/dt|
    #
    # For the adiabatic spectrum near a quasi-crossing:
    #   E_gap(tau) ~ sqrt(Delta_min^2 + (v_slope * (tau - tau_0))^2)
    #
    # So d^2(gap)/dtau^2 |_min = v_slope^2 / Delta_min
    # => v_slope = sqrt(Delta_min * d2gap/dtau2)

    # Second derivative of gap at crossing
    if 1 <= idx <= N_sel - 2:
        d2gap_dtau2 = (gap_series[idx+1] - 2*gap_series[idx] + gap_series[idx-1]) / dtau**2
    else:
        d2gap_dtau2 = 0.0  # (local)

    Delta_min = qc['gap_min']

    # Diabatic slope: v_slope (in tau-derivative units)
    if d2gap_dtau2 > 0 and Delta_min > 0:
        v_slope_tau = np.sqrt(Delta_min * d2gap_dtau2)
    else:
        # Not a proper avoided crossing if curvature is non-positive
        v_slope_tau = abs(dgap_dtau) if abs(dgap_dtau) > 1e-10 else 1e-10

    # Convert to time derivative: v_slope_t = v_slope_tau * omega_tau
    v_slope_t = v_slope_tau * omega_tau

    # LZ parameter: gamma = pi * Delta_min^2 / (2 * v_slope_t)
    # (In natural units with hbar = 1, energies in M_KK)
    gamma_LZ = PI * Delta_min**2 / (2.0 * v_slope_t) if v_slope_t > 1e-20 else 1e20

    P_LZ = np.exp(-2 * PI * gamma_LZ)

    lz_results.append({
        **qc,
        'dgap_dtau': dgap_dtau,
        'd2gap_dtau2': d2gap_dtau2,
        'v_slope_tau': v_slope_tau,
        'v_slope_t': v_slope_t,
        'gamma_LZ': gamma_LZ,
        'P_LZ': P_LZ,
    })

# Sort by P_LZ descending (most likely transitions first)
lz_results.sort(key=lambda x: -x['P_LZ'])

print(f"\nTOP 20 CROSSINGS BY P_LZ (descending)")
print(f"{'Rank':>4} {'Levels':>8} {'tau':>8} {'gap_min':>10} {'gamma_LZ':>10} {'P_LZ':>12}")
print(f"-" * 65)
for i, r in enumerate(lz_results[:20]):
    print(f"{i+1:4d} ({r['level_lo']:2d},{r['level_hi']:2d}) "
          f"{r['tau']:8.5f} {r['gap_min']:10.6f} "
          f"{r['gamma_LZ']:10.4f} {r['P_LZ']:12.6e}")

# ============================================================================
#  4. Stuckelberg interference: consecutive crossings on same level pair
# ============================================================================

print(f"\n{'='*70}")
print(f"STUCKELBERG INTERFERENCE ANALYSIS")
print(f"{'='*70}")

# Group crossings by level pair
from collections import defaultdict
crossings_by_pair = defaultdict(list)
for r in lz_results:
    pair_key = (r['level_lo'], r['level_hi'])
    crossings_by_pair[pair_key].append(r)

# Sort each group by tau
for key in crossings_by_pair:
    crossings_by_pair[key].sort(key=lambda x: x['tau'])

# Find consecutive crossing pairs
stuckelberg_pairs = []

for pair_key, crossings in crossings_by_pair.items():
    if len(crossings) < 2:
        continue

    k, l = pair_key
    gap_series = eig_sel[:, l] - eig_sel[:, k]

    for i in range(len(crossings) - 1):
        c1 = crossings[i]
        c2 = crossings[i + 1]

        idx1 = c1['tau_idx_sel']
        idx2 = c2['tau_idx_sel']

        # Stuckelberg phase: phi_S = integral of gap between the two crossings
        # Use the full resolution tau grid for integration
        if idx2 > idx1:
            tau_segment = tau_sel[idx1:idx2+1]
            gap_segment = gap_series[idx1:idx2+1]

            # phi_S = integral(Delta(tau') dtau', tau_1, tau_2) / omega_tau
            # Wait — phi_S in time units. The phase accumulated is:
            # phi_S = integral(Delta(t') dt', t_1, t_2) = integral(Delta(tau')/omega_tau dtau', tau_1, tau_2) * omega_tau
            # Actually: phi_S = integral(Delta(tau') dtau') / (dtau/dt)
            # where dtau/dt is the transit velocity
            # So phi_S = omega_tau * integral(Delta(tau') dtau') ... no.
            #
            # Correct formulation:
            # phi_S = (1/hbar) * integral(Delta(t) dt) from t1 to t2
            # = (1/hbar) * integral(Delta(tau) * dt/dtau * dtau) from tau1 to tau2
            # In M_KK natural units (hbar=1), dtau/dt = omega_tau
            # => dt = dtau / omega_tau
            # => phi_S = integral(Delta(tau) dtau) / omega_tau

            phi_S_raw = trapezoid(gap_segment, tau_segment)  # in M_KK * dtau units
            phi_S = phi_S_raw / omega_tau  # convert to dimensionless phase (hbar=1, M_KK units)

            # Actually wait. Let me be more careful.
            # Energy gap Delta is in M_KK units. tau is dimensionless.
            # Time t is in M_KK^{-1} units.
            # dtau/dt = omega_tau (M_KK units)
            # Phase = integral(Delta * dt) = integral(Delta/omega_tau * dtau)
            # But Delta is in M_KK and dtau is dimensionless, so
            # integral has units of M_KK (which is correct for a phase when hbar=1 and time in M_KK^{-1})
            #
            # Actually: phase = integral(E * dt / hbar). With hbar=1 and E in M_KK, t in M_KK^{-1}:
            # phase = integral(E(t) dt) dimensionless.
            # E(tau) in M_KK, dt = dtau/omega_tau where omega_tau in M_KK.
            # So phase = integral(E(tau)/omega_tau dtau) — E/omega_tau dimensionless, dtau dimensionless.
            # = phi_S_raw / omega_tau. YES, this is correct and dimensionless.

            # Stokes phase (for a parabolic level crossing model)
            # phi_Stokes = -gamma*(ln(gamma) - 1) + pi/4
            # where gamma is the LZ parameter at the first crossing
            gamma_1 = c1['gamma_LZ']
            gamma_2 = c2['gamma_LZ']

            if gamma_1 > 1e-20:
                phi_Stokes_1 = -gamma_1 * (np.log(gamma_1) - 1) + PI/4
            else:
                phi_Stokes_1 = PI/4

            P_LZ_1 = c1['P_LZ']
            P_LZ_2 = c2['P_LZ']

            # Geometric mean P_LZ for the double-pass
            P_LZ_avg = np.sqrt(P_LZ_1 * P_LZ_2)

            # Stuckelberg formula for double-pass:
            # P_Stuck = 4 * P_LZ * (1 - P_LZ) * sin^2(phi_S/2 + phi_Stokes)
            # Maximum: P_Stuck_max = 4 * P_LZ * (1 - P_LZ)  (when sin^2 = 1)
            # Minimum: P_Stuck_min = 0  (when sin^2 = 0)

            total_phase = phi_S / 2 + phi_Stokes_1
            sin2_phase = np.sin(total_phase)**2

            P_Stuck = 4 * P_LZ_avg * (1 - P_LZ_avg) * sin2_phase
            P_Stuck_max = 4 * P_LZ_avg * (1 - P_LZ_avg)

            stuckelberg_pairs.append({
                'pair': pair_key,
                'tau_1': c1['tau'],
                'tau_2': c2['tau'],
                'gap_min_1': c1['gap_min'],
                'gap_min_2': c2['gap_min'],
                'gamma_1': gamma_1,
                'gamma_2': gamma_2,
                'P_LZ_1': P_LZ_1,
                'P_LZ_2': P_LZ_2,
                'P_LZ_avg': P_LZ_avg,
                'phi_S': phi_S,
                'phi_S_raw': phi_S_raw,
                'phi_Stokes': phi_Stokes_1,
                'total_phase': total_phase,
                'sin2_phase': sin2_phase,
                'P_Stuck': P_Stuck,
                'P_Stuck_max': P_Stuck_max,
            })

print(f"\nLevel pairs with >=2 crossings: {len(crossings_by_pair)}")
print(f"Stuckelberg interference pairs found: {len(stuckelberg_pairs)}")

if len(stuckelberg_pairs) > 0:
    stuckelberg_pairs.sort(key=lambda x: -x['P_Stuck_max'])

    print(f"\n{'='*70}")
    print(f"STUCKELBERG PAIRS — SORTED BY MAX P_exc ENHANCEMENT")
    print(f"{'='*70}")
    print(f"{'Rank':>4} {'Levels':>8} {'tau_1':>8} {'tau_2':>8} {'gap1':>8} {'gap2':>8} "
          f"{'P_LZ':>10} {'phi_S':>8} {'P_Stuck':>10} {'P_max':>10}")
    print(f"-" * 100)
    for i, sp in enumerate(stuckelberg_pairs[:30]):
        print(f"{i+1:4d} ({sp['pair'][0]:2d},{sp['pair'][1]:2d}) "
              f"{sp['tau_1']:8.5f} {sp['tau_2']:8.5f} "
              f"{sp['gap_min_1']:8.5f} {sp['gap_min_2']:8.5f} "
              f"{sp['P_LZ_avg']:10.4e} {sp['phi_S']:8.3f} "
              f"{sp['P_Stuck']:10.4e} {sp['P_Stuck_max']:10.4e}")

# ============================================================================
#  5. Map P_exc vs tau for strongest quasi-crossings
# ============================================================================

print(f"\n{'='*70}")
print(f"EXCITATION PROBABILITY MAP vs TAU")
print(f"{'='*70}")

# For each tau point, accumulate P_exc from all crossings that have occurred
# up to that point
P_exc_map = np.zeros(N_sel)

for r in lz_results:
    idx = r['tau_idx_sel']
    P_exc_map[idx] = max(P_exc_map[idx], r['P_LZ'])

print(f"\nP_exc(tau) from individual LZ crossings:")
print(f"  Max P_LZ = {max(r['P_LZ'] for r in lz_results):.6e}")
print(f"  at tau = {max(lz_results, key=lambda x: x['P_LZ'])['tau']:.5f}")
print(f"  levels = ({max(lz_results, key=lambda x: x['P_LZ'])['level_lo']}, "
      f"{max(lz_results, key=lambda x: x['P_LZ'])['level_hi']})")

# Cumulative P_exc (independent crossing model)
# P_total = 1 - prod(1 - P_LZ_i)
P_exc_cum = np.zeros(N_sel)
for t_idx in range(N_sel):
    crossings_at_t = [r for r in lz_results if r['tau_idx_sel'] == t_idx]
    for r in crossings_at_t:
        P_exc_cum[t_idx] = P_exc_cum[t_idx] + r['P_LZ'] * (1 - P_exc_cum[t_idx])

print(f"\nCumulative P_exc at each tau (independent crossings):")
nonzero = P_exc_cum > 0
if np.any(nonzero):
    print(f"  Max cumulative P_exc = {P_exc_cum.max():.6e}")
    print(f"  at tau = {tau_sel[np.argmax(P_exc_cum)]:.5f}")

# ============================================================================
#  6. Global P_exc through entire transit
# ============================================================================

print(f"\n{'='*70}")
print(f"GLOBAL TRANSIT P_exc")
print(f"{'='*70}")

# Total P_exc from ALL crossings during transit (independent crossing approx)
P_total = 0.0  # (local)
n_significant = 0  # crossings with P_LZ > 1e-100
for r in lz_results:
    P_total = P_total + r['P_LZ'] * (1 - P_total)
    if r['P_LZ'] > 1e-100:
        n_significant += 1

print(f"Total crossings: {len(lz_results)}")
print(f"Significant crossings (P_LZ > 1e-100): {n_significant}")
print(f"Total P_exc (independent crossing model): {P_total:.6e}")

# With Stuckelberg enhancement
P_total_stuck = 0.0  # (local)
if len(stuckelberg_pairs) > 0:
    for sp in stuckelberg_pairs:
        P_total_stuck = P_total_stuck + sp['P_Stuck'] * (1 - P_total_stuck)
    print(f"Total P_exc (Stuckelberg enhanced): {P_total_stuck:.6e}")
    if P_total > 0:
        enhancement = P_total_stuck / P_total if P_total > 1e-300 else float('inf')
        print(f"Stuckelberg enhancement factor: {enhancement:.2f}x")

# ============================================================================
#  7. Detailed analysis of the smallest gaps
# ============================================================================

print(f"\n{'='*70}")
print(f"DETAILED GAP ANALYSIS — SMALLEST 10 QUASI-CROSSINGS")
print(f"{'='*70}")

for i, r in enumerate(lz_results[:10]):
    k, l = r['level_lo'], r['level_hi']
    print(f"\n--- Crossing #{i+1}: levels ({k}, {l}) at tau = {r['tau']:.5f} ---")
    print(f"  gap_min = {r['gap_min']:.8f} M_KK")
    print(f"  E_lo = {r['E_lo']:.6f}, E_hi = {r['E_hi']:.6f}")
    print(f"  dgap/dtau = {r['dgap_dtau']:.6f}")
    print(f"  d2gap/dtau2 = {r['d2gap_dtau2']:.4f}")
    print(f"  v_slope (tau) = {r['v_slope_tau']:.6f}")
    print(f"  v_slope (time) = {r['v_slope_t']:.6f} M_KK^2")
    print(f"  gamma_LZ = {r['gamma_LZ']:.6f}")
    print(f"  P_LZ = {r['P_LZ']:.6e}")

    # Thermal comparison
    # T_GH = H/(2*pi) is the Gibbons-Hawking temperature during transit
    T_GH = H_fold / (2 * PI)
    thermal_P = np.exp(-r['gap_min'] / T_GH) if T_GH > 0 else 0
    print(f"  Thermal comparison: T_GH = {T_GH:.4f} M_KK")
    print(f"  P_thermal = exp(-gap/T_GH) = {thermal_P:.6e}")

# ============================================================================
#  8. Near-degenerate level tracking (for potential DM channel)
# ============================================================================

print(f"\n{'='*70}")
print(f"NEAR-DEGENERATE LEVEL PAIRS — DM CHANNEL CANDIDATES")
print(f"{'='*70}")

# DM channel requires: long-lived excited states created by LZ transitions
# during transit. These must be:
#  a) Created with non-negligible P_exc
#  b) Stable after transit (gap reopens, no further decay channel)
#  c) Carrying conserved quantum number that prevents decay

# Check gap behavior AFTER the fold: does gap reopen?
fold_idx_sel = np.argmin(np.abs(tau_sel - tau_fold))
print(f"Fold at tau = {tau_fold:.2f} (index {fold_idx_sel} in selection)")

post_fold_gap_min = {}
for r in lz_results:
    k, l = r['level_lo'], r['level_hi']
    if r['tau_idx_sel'] <= fold_idx_sel:
        # Crossing before/at fold: check gap after fold
        gap_after = eig_sel[fold_idx_sel:, l] - eig_sel[fold_idx_sel:, k]
        gap_asymptotic = gap_after[-1] if len(gap_after) > 0 else 0
        post_fold_gap_min[(k, l)] = {
            'gap_at_crossing': r['gap_min'],
            'gap_post_fold': gap_asymptotic,
            'gap_ratio': gap_asymptotic / r['gap_min'] if r['gap_min'] > 0 else 0,
            'P_LZ': r['P_LZ'],
            'tau_cross': r['tau'],
        }

for pair, info in sorted(post_fold_gap_min.items(), key=lambda x: x[1]['gap_at_crossing']):
    print(f"  Levels ({pair[0]:2d},{pair[1]:2d}): "
          f"gap_cross={info['gap_at_crossing']:.6f}, "
          f"gap_post={info['gap_post_fold']:.6f}, "
          f"ratio={info['gap_ratio']:.2f}, "
          f"P_LZ={info['P_LZ']:.4e}")
    if len(post_fold_gap_min) > 15:
        break  # truncate output

# ============================================================================
#  9. Compare to W1-1 sudden quench result
# ============================================================================

print(f"\n{'='*70}")
print(f"COMPARISON TO W1-1 SUDDEN QUENCH")
print(f"{'='*70}")

P_exc_W1 = 0.081  # From W1-1  # (local)
print(f"W1-1 sudden quench P_exc = {P_exc_W1:.3f}")
print(f"Stuckelberg max P_exc = {P_total_stuck:.6e}")
print(f"Individual LZ max P_exc = {max(r['P_LZ'] for r in lz_results):.6e}")

# The key question: is Stuckelberg interference a viable DM production channel?
# DM requires P_exc * n_modes ~ Omega_DM / Omega_M ~ 0.85
from canonical_constants import Omega_DM, Omega_m
DM_ratio = Omega_DM / Omega_m  # ~0.84

print(f"\nDM requirement: P_exc * n_modes ~ Omega_DM/Omega_m = {DM_ratio:.3f}")
print(f"With 32 modes: need P_exc ~ {DM_ratio/32:.4f} per mode")
print(f"With Stuckelberg: P_total = {P_total_stuck:.6e}")

viable = P_total_stuck > DM_ratio / 32
print(f"\nStuckelberg DM channel viable? {'YES' if viable else 'NO'}")

if P_total_stuck > 0 and P_total_stuck < 1:
    log_shortfall = np.log10(DM_ratio / 32) - np.log10(P_total_stuck) if P_total_stuck > 0 else float('inf')
    print(f"Log10 shortfall: {log_shortfall:.1f} orders of magnitude")

# ============================================================================
#  10. Save results
# ============================================================================

# Prepare arrays for saving
n_qc = len(quasi_crossings)
n_lz = len(lz_results)
n_sp = len(stuckelberg_pairs)

qc_tau = np.array([qc['tau'] for qc in quasi_crossings[:n_qc]])
qc_gap = np.array([qc['gap_min'] for qc in quasi_crossings[:n_qc]])
qc_levels = np.array([[qc['level_lo'], qc['level_hi']] for qc in quasi_crossings[:n_qc]])

lz_tau = np.array([r['tau'] for r in lz_results[:n_lz]])
lz_gap = np.array([r['gap_min'] for r in lz_results[:n_lz]])
lz_gamma = np.array([r['gamma_LZ'] for r in lz_results[:n_lz]])
lz_P = np.array([r['P_LZ'] for r in lz_results[:n_lz]])
lz_levels = np.array([[r['level_lo'], r['level_hi']] for r in lz_results[:n_lz]])

if n_sp > 0:
    sp_tau1 = np.array([sp['tau_1'] for sp in stuckelberg_pairs])
    sp_tau2 = np.array([sp['tau_2'] for sp in stuckelberg_pairs])
    sp_phi_S = np.array([sp['phi_S'] for sp in stuckelberg_pairs])
    sp_P_stuck = np.array([sp['P_Stuck'] for sp in stuckelberg_pairs])
    sp_P_max = np.array([sp['P_Stuck_max'] for sp in stuckelberg_pairs])
    sp_levels = np.array([list(sp['pair']) for sp in stuckelberg_pairs])
else:
    sp_tau1 = np.array([])
    sp_tau2 = np.array([])
    sp_phi_S = np.array([])
    sp_P_stuck = np.array([])
    sp_P_max = np.array([])
    sp_levels = np.array([]).reshape(0, 2)

outpath = os.path.join(os.path.dirname(__file__), 's57_stuckelberg_dm.npz')
np.savez(outpath,
    # Full spectrum
    tau_values=tau_all,
    eigenvalues=eig_all,
    tau_selected=tau_sel,

    # Quasi-crossings
    qc_tau=qc_tau,
    qc_gap=qc_gap,
    qc_levels=qc_levels,
    n_quasi_crossings=n_qc,

    # Landau-Zener
    lz_tau=lz_tau,
    lz_gap=lz_gap,
    lz_gamma=lz_gamma,
    lz_P=lz_P,
    lz_levels=lz_levels,

    # Stuckelberg pairs
    sp_tau1=sp_tau1,
    sp_tau2=sp_tau2,
    sp_phi_S=sp_phi_S,
    sp_P_stuck=sp_P_stuck,
    sp_P_max=sp_P_max,
    sp_levels=sp_levels,
    n_stuckelberg_pairs=n_sp,

    # P_exc maps
    P_exc_map=P_exc_map,
    P_exc_cumulative=P_exc_cum,
    P_total_indep=P_total,
    P_total_stuckelberg=P_total_stuck,

    # Gate
    gate_name=np.array(['STUCKELBERG-DM-57']),
    gate_verdict=np.array(['INFO']),
    gate_detail=np.array([
        f'n_crossings={n_qc}, n_stuck_pairs={n_sp}, '
        f'P_total_LZ={P_total:.4e}, P_total_stuck={P_total_stuck:.4e}, '
        f'min_gap={qc_gap[0]:.6f} at ({qc_levels[0,0]},{qc_levels[0,1]}), '
        f'viable_DM={viable}'
    ]),
)

print(f"\nSaved: {outpath}")
print(f"DONE")
