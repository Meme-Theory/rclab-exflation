#!/usr/bin/env python3
"""
FRICTION-INTEGRAL: Hubble Friction from ODE Trajectory Data
=============================================================

Session 77, Wave 2-I (S77-B9-FRICTION)
Agent: transit-dynamics-theorist

Gate: S77-B9-FRICTION (INFO diagnostic)
  INFO: Report F, N_osc, exp(-F). Characterize whether friction
        alone damps oscillation or decay dominates.

Physics:
--------
The modulus tau evolves in the post-fold background according to a
Klein-Gordon equation with Hubble friction:

    tau'' + 3H tau' + dV/dtau = 0                                 (1)

where prime = d/dt, H = (da/dt)/a is the Hubble parameter, and
V(tau) is the effective potential (spectral action + BCS dressing).

In efold time N = ln(a), this becomes:

    d^2 tau/dN^2 + (3 - epsilon) d tau/dN + V'(tau)/H^2 = 0      (2)

where epsilon = -dH/dN / H.

The Hubble friction integral over the post-fold trajectory is:

    F = integral_0^{N_end} (3/2) H(N') / H_ref  dN'              (3)

For a scalar oscillating in a quadratic potential with frequency
omega_tau and Hubble damping, the number of completed oscillations is:

    N_osc = delta_N * omega_tau / (2 pi H_avg)                   (4)

and the damping factor per oscillation is exp(-3 pi H / omega_tau).

IMPORTANT CONTEXT (S77 W1-A, EQUIL-TAU-77):
The bare spectral action V(tau) is monotonically increasing (S36).
BCS dressing provides |E_cond|/V_bare = 1.05e-4, too weak by 72x
to create a minimum. Consequently, the ODE trajectory shows
ZERO oscillations: tau rolls monotonically after the fold.

This computation characterizes the damping of whatever trajectory
the ODE produces -- if there were oscillations, how fast would
friction kill them? And does friction or modulus decay dominate?

Input: s73b_efold_mapping.npz, canonical_constants.py
Output: s77_friction_integral.npz
"""

import numpy as np
import sys
import os
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    tau_fold, M_KK, M_KK_gravity, H_fold, v_terminal, dt_transit,
    m_tau, omega_tau, omega_att, E_cond, d2S_fold, dS_fold,
    Delta_BCS, hbar_GeV_s
)

start = time.time()

# ============================================================
# 1. Load ODE trajectory data from S73B
# ============================================================
data = np.load('s73b_efold_mapping.npz', allow_pickle=True)

t_sol = data['t_sol']       # time in M_KK^{-1} units
tau_sol = data['tau_sol']    # Jensen deformation parameter
dtau_sol = data['dtau_sol']  # d(tau)/dt in M_KK units
N_sol = data['lna_sol']      # efolds N = ln(a)
H_sol = data['H_sol']        # Hubble parameter in M_KK units
w_sol = data['w_sol']        # equation of state w
aH_sol = data['aH_sol']      # comoving Hubble parameter a*H

N_total = float(data['N_total'])  # (local)
N_modulus = float(data['N_modulus'])  # (local)

print("=" * 72)
print("S77-B9-FRICTION: Hubble Friction Integral from ODE Data")
print("=" * 72)
print(f"\nODE trajectory: {len(t_sol)} points, N in [0, {N_sol[-1]:.2f}]")
print(f"N_total = {N_total:.4f}, N_modulus = {N_modulus:.4f}")

# ============================================================
# 2. Identify trajectory phases
# ============================================================

# Phase A: Transit / stiff (w > 0, first few efolds)
# The fold is at N=0, tau starts at tau_fold=0.19
# tau rises to max ~1.61 in first 0.08 efolds, then falls

tau_max_idx = np.argmax(tau_sol)  # (local)
tau_max_val = tau_sol[tau_max_idx]  # (local)
N_turnaround = N_sol[tau_max_idx]  # (local)

print(f"\n--- Phase identification ---")
print(f"tau turnaround: tau_max = {tau_max_val:.6f} at N = {N_turnaround:.6f}")
print(f"  (index {tau_max_idx} of {len(tau_sol)})")

# Phase B: Post-turnaround roll-down
# Find where w transitions to near de Sitter
idx_w_neg = np.where(w_sol < 0)[0]  # (local)
if len(idx_w_neg) > 0:
    N_w_cross = N_sol[idx_w_neg[0]]  # (local)
    print(f"w < 0 first at N = {N_w_cross:.6f}")

idx_w_dS = np.where(w_sol < -0.99)[0]  # (local)
if len(idx_w_dS) > 0:
    N_dS_onset = N_sol[idx_w_dS[0]]  # (local)
    print(f"w < -0.99 first at N = {N_dS_onset:.6f}")
else:
    N_dS_onset = N_sol[-1]  # (local)

# ============================================================
# 3. Check for oscillations in tau
# ============================================================
# An oscillation requires dtau to change sign.
# After the turnaround, dtau should go from + to -.
# A second oscillation requires dtau to return to +.

# Use the post-turnaround segment
post_turn_start = max(tau_max_idx + 5, tau_max_idx)  # (local) skip the peak itself
dtau_post = dtau_sol[post_turn_start:]  # (local)
N_post = N_sol[post_turn_start:]  # (local)

# Count sign changes in dtau
sign_dtau = np.sign(dtau_post)  # (local)
sign_changes = np.where(np.diff(sign_dtau) != 0)[0]  # (local)

# Filter out numerical noise: require |dtau| > threshold at sign change
dtau_thresh = 0.01 * abs(dtau_sol[0])  # (local) 1% of initial velocity
real_sign_changes = []  # (local)
for sc in sign_changes:
    if abs(dtau_post[sc]) > dtau_thresh or abs(dtau_post[sc+1]) > dtau_thresh:
        real_sign_changes.append(sc)

n_oscillations = len(real_sign_changes) // 2  # (local) each full oscillation = 2 sign changes

print(f"\n--- Oscillation analysis ---")
print(f"Sign changes in dtau (post-turnaround): {len(sign_changes)} raw, {len(real_sign_changes)} above threshold")
print(f"Number of complete oscillations: {n_oscillations}")
if len(real_sign_changes) > 0:
    for i, sc in enumerate(real_sign_changes[:6]):
        abs_idx = post_turn_start + sc  # (local)
        print(f"  Sign change {i}: N = {N_sol[abs_idx]:.6f}, "
              f"dtau = {dtau_sol[abs_idx]:.4e} -> {dtau_sol[abs_idx+1]:.4e}")

# ============================================================
# 4. Compute the Hubble friction integral
# ============================================================
# F = integral (3/2) H(N') dN'
# This is the exponent that damps the modulus amplitude.
#
# For a damped oscillator: x(t) ~ exp(-F) cos(omega t)
# where F accumulates as the mode evolves.
#
# We compute F over the entire post-fold trajectory.

# Use trapezoidal integration over the ODE grid
dN = np.diff(N_sol)  # (local)
H_mid = 0.5 * (H_sol[:-1] + H_sol[1:])  # (local) midpoint H values

# Full friction integral
F_full = np.cumsum(1.5 * H_mid * dN)  # (local)
F_total = F_full[-1]  # (local)

print(f"\n--- Hubble friction integral ---")
print(f"F_total = integral (3/2)H dN' = {F_total:.6f}")
print(f"exp(-F_total) = {np.exp(-F_total):.6e}")

# F over specific intervals
# First 1 efold
idx_1ef = np.searchsorted(N_sol, 1.0)  # (local)
F_1ef = F_full[min(idx_1ef, len(F_full)-1)]  # (local)
print(f"F(first 1 efold) = {F_1ef:.6f}, exp(-F) = {np.exp(-F_1ef):.6e}")

# First 10 efolds
idx_10ef = np.searchsorted(N_sol, 10.0)  # (local)
F_10ef = F_full[min(idx_10ef, len(F_full)-1)]  # (local)
print(f"F(first 10 efolds) = {F_10ef:.6f}, exp(-F) = {np.exp(-F_10ef):.6e}")

# Over the full modulus epoch
idx_mod = np.searchsorted(N_sol, N_modulus)  # (local)
F_modulus = F_full[min(idx_mod, len(F_full)-1)]  # (local)
print(f"F(modulus epoch, {N_modulus:.2f} efolds) = {F_modulus:.6f}, exp(-F) = {np.exp(-F_modulus):.6e}")

# ============================================================
# 5. Compute hypothetical oscillation count
# ============================================================
# Even though the ODE shows no oscillations (monotonic V),
# compute how many oscillations WOULD occur if there were
# a quadratic minimum with frequency omega_tau.
#
# N_osc = delta_N * omega_tau / (2 pi H_avg)
#
# omega_tau = 8.27 M_KK (S38 transit frequency)
# m_tau = 2.062 M_KK (modulus mass at fold)
# omega_att = 1.430 M_KK (attractor frequency, fully geometric)

H_avg_post = np.mean(H_sol[tau_max_idx:])  # (local) average H over post-fold
delta_N_post = N_sol[-1] - N_turnaround  # (local)

# Use all three frequency scales
for name, omega in [("omega_tau (transit)", omega_tau),
                    ("m_tau (modulus mass)", m_tau),
                    ("omega_att (attractor)", omega_att)]:
    N_osc_hyp = delta_N_post * omega / (2 * np.pi * H_avg_post)  # (local)
    damp_per_osc = np.exp(-3 * np.pi * H_avg_post / omega)  # (local)
    print(f"\n  Hypothetical with {name} = {omega:.3f} M_KK:")
    print(f"    N_osc = {N_osc_hyp:.2f} (over {delta_N_post:.2f} efolds)")
    print(f"    Damping per oscillation: exp(-3 pi H/{omega:.3f}) = {damp_per_osc:.6e}")
    print(f"    Amplitude after 1 osc: {damp_per_osc:.6e}")
    print(f"    omega/H_avg = {omega/H_avg_post:.4f}")
    print(f"    H/omega = {H_avg_post/omega:.4f} {'(overdamped)' if H_avg_post > omega else '(underdamped)'}")

# ============================================================
# 6. Critical ratio: H vs omega
# ============================================================
# The critical damping condition for a KG field in FRW:
#   tau'' + 3H tau' + omega^2 tau = 0
# is overdamped when 3H/2 > omega, underdamped when 3H/2 < omega.
# (This is the standard result for a massive scalar in expanding spacetime.)
#
# At fold: H = H_sol[0] (from ODE), omega = m_tau
# Post-fold: H settles to H_sol ~ 0.633

H_at_fold = H_sol[0]  # (local)
H_late = H_sol[-1]  # (local)

print(f"\n--- Critical damping analysis ---")
print(f"H at fold = {H_at_fold:.6f} M_KK (ODE)")
print(f"H late = {H_late:.6f} M_KK (ODE)")
print(f"H_fold (canonical) = {H_fold:.2f} M_KK (from S38 = {H_fold:.2f})")
print(f"  NOTE: ODE H ({H_at_fold:.4f}) << canonical H_fold ({H_fold:.2f})")
print(f"  This is because ODE uses normalized units where H ~ O(1)")

print(f"\nCritical damping condition: 3H/2 vs omega")
for name, omega in [("m_tau", m_tau), ("omega_att", omega_att), ("omega_tau", omega_tau)]:
    ratio = 1.5 * H_at_fold / omega  # (local)
    regime = "OVERDAMPED" if ratio > 1 else "UNDERDAMPED"  # (local)
    print(f"  3H/2 / {name} = {ratio:.4f} -> {regime}")
    ratio_late = 1.5 * H_late / omega  # (local)
    regime_late = "OVERDAMPED" if ratio_late > 1 else "UNDERDAMPED"  # (local)
    print(f"  3H_late/2 / {name} = {ratio_late:.4f} -> {regime_late}")

# ============================================================
# 7. Modulus decay timescale comparison
# ============================================================
# From S76: tau_decay = 4.44e-40 s (gravity-dominated decay to SM)
# Also: tau_decay = 1.63e-37 s (alternative estimate)
# Convert to efold time using H

tau_decay_s = 4.44e-40  # (local) seconds, from S76 W1-B
tau_decay_alt_s = 1.63e-37  # (local) seconds, from S76 transit synthesis

# Convert physical seconds to M_KK^{-1} time units
# t_physical = t_MKK / M_KK  where M_KK is in natural units (GeV, hbar=c=1)
# t_physical = t_MKK * hbar / (M_KK * c^2)  but in natural units hbar=c=1
# So t_MKK = t_physical * M_KK_GeV / hbar_GeV_s
# hbar_GeV_s = 6.582e-25 GeV*s

t_decay_MKK = tau_decay_s * M_KK / hbar_GeV_s  # (local)
t_decay_alt_MKK = tau_decay_alt_s * M_KK / hbar_GeV_s  # (local)

print(f"\n--- Modulus decay comparison ---")
print(f"tau_decay = {tau_decay_s:.2e} s = {t_decay_MKK:.4e} M_KK^{{-1}}")
print(f"tau_decay_alt = {tau_decay_alt_s:.2e} s = {t_decay_alt_MKK:.4e} M_KK^{{-1}}")

# Compare with ODE time range
t_end_MKK = t_sol[-1]  # (local)
print(f"ODE time range: [0, {t_end_MKK:.2f}] M_KK^{{-1}}")
print(f"Ratio t_decay / t_ODE_end = {t_decay_MKK / t_end_MKK:.4e}")

# How many efolds does the modulus survive?
# N_decay = H * t_decay (rough estimate)
H_avg_full = np.mean(H_sol)  # (local)
N_decay_est = H_avg_full * t_decay_MKK  # (local)
N_decay_alt_est = H_avg_full * t_decay_alt_MKK  # (local)

print(f"H_avg = {H_avg_full:.4f} M_KK")
print(f"N_decay ~ H_avg * t_decay = {N_decay_est:.4e} efolds")
print(f"N_decay_alt ~ H_avg * t_decay_alt = {N_decay_alt_est:.4e} efolds")

# Friction integral accumulated by decay time
# Find the ODE index closest to t_decay
if t_decay_MKK < t_end_MKK:
    idx_decay = np.searchsorted(t_sol, t_decay_MKK)  # (local)
    if idx_decay < len(N_sol):
        N_at_decay = N_sol[idx_decay]  # (local)
        F_at_decay = F_full[min(idx_decay-1, len(F_full)-1)]  # (local)
        print(f"\nAt t_decay: N = {N_at_decay:.6f}, F = {F_at_decay:.6f}, exp(-F) = {np.exp(-F_at_decay):.6e}")
    else:
        print(f"\nt_decay beyond ODE grid")
        N_at_decay = None  # (local)
        F_at_decay = None  # (local)
else:
    print(f"\nt_decay = {t_decay_MKK:.4e} >> t_ODE_end = {t_end_MKK:.2f}")
    print(f"Modulus decay occurs AFTER the ODE integration window")
    N_at_decay = None  # (local)
    F_at_decay = None  # (local)

# ============================================================
# 8. Velocity damping profile
# ============================================================
# Track how |dtau/dt| evolves -- this is the "amplitude" of the modulus motion

dtau_abs = np.abs(dtau_sol)  # (local)
dtau_init = dtau_abs[0]  # (local) = v_terminal

# Compute effective damping: dtau(N) / dtau(0)
dtau_ratio_1ef = dtau_abs[idx_1ef] / dtau_init if idx_1ef < len(dtau_abs) else 0  # (local)
dtau_ratio_10ef = dtau_abs[idx_10ef] / dtau_init if idx_10ef < len(dtau_abs) else 0  # (local)
dtau_ratio_end = dtau_abs[-1] / dtau_init  # (local)

print(f"\n--- Velocity damping profile ---")
print(f"|dtau/dt| at N=0: {dtau_init:.4f} M_KK (= v_terminal)")
print(f"|dtau/dt| at N=1: {dtau_abs[idx_1ef]:.4e}, ratio = {dtau_ratio_1ef:.4e}")
print(f"|dtau/dt| at N=10: {dtau_abs[idx_10ef]:.4e}, ratio = {dtau_ratio_10ef:.4e}")
print(f"|dtau/dt| at N_end: {dtau_abs[-1]:.4e}, ratio = {dtau_ratio_end:.4e}")

# Effective number of e-folds to damp by factor e
# |dtau| ~ |dtau_0| * exp(-gamma_eff * N)
# Find gamma_eff from fit over first 10 efolds
mask_fit = (N_sol > 0.5) & (N_sol < 10.0) & (dtau_abs > 0)  # (local) avoid transit region
if np.sum(mask_fit) > 10:
    log_dtau_fit = np.log(dtau_abs[mask_fit])  # (local)
    N_fit = N_sol[mask_fit]  # (local)
    # Linear fit: log|dtau| = a + b*N
    coeffs = np.polyfit(N_fit, log_dtau_fit, 1)  # (local)
    gamma_eff = -coeffs[0]  # (local) effective damping rate per efold
    N_edamp = 1.0 / gamma_eff if gamma_eff > 0 else np.inf  # (local)
    print(f"\nEffective damping rate: gamma_eff = {gamma_eff:.6f} per efold")
    print(f"e-folding scale for damping: {N_edamp:.4f} efolds")
    print(f"Expected from 3H/2: {1.5 * np.mean(H_sol[mask_fit]):.4f}")
else:
    gamma_eff = 0  # (local)
    N_edamp = np.inf  # (local)

# ============================================================
# 9. Kinetic energy fraction profile
# ============================================================
# KE = (1/2) dtau^2 / H^2  (in dimensionless form)
# eps_KE = 3(1+w)/2  = kinetic fraction of energy density

eps_KE = 1.5 * (1 + w_sol)  # (local)

print(f"\n--- Kinetic energy fraction (epsilon_KE) ---")
print(f"eps_KE at N=0: {eps_KE[0]:.6f} (stiff: should be ~3)")
print(f"eps_KE at N=1: {eps_KE[idx_1ef]:.6e}")
print(f"eps_KE at N=10: {eps_KE[idx_10ef]:.6e}")
print(f"eps_KE at N_end: {eps_KE[-1]:.6e}")

# ============================================================
# 10. Summary and gate verdict
# ============================================================

print(f"\n{'=' * 72}")
print(f"GATE S77-B9-FRICTION: VERDICT")
print(f"{'=' * 72}")

print(f"\n1. Friction integral:")
print(f"   F_total = {F_total:.4f} over {N_sol[-1]:.2f} efolds")
print(f"   exp(-F_total) = {np.exp(-F_total):.4e}")
print(f"   F(1 efold) = {F_1ef:.4f}, exp(-F) = {np.exp(-F_1ef):.4e}")
print(f"   F(10 efolds) = {F_10ef:.4f}, exp(-F) = {np.exp(-F_10ef):.4e}")

print(f"\n2. Oscillation count:")
print(f"   N_osc = {n_oscillations} (ZERO -- monotonic roll, no oscillation phase)")
print(f"   Hypothetical N_osc(m_tau) = {delta_N_post * m_tau / (2*np.pi*H_avg_post):.2f}")
print(f"   But: 3H/2 / m_tau = {1.5*H_at_fold/m_tau:.4f} at fold -> ", end="")
print(f"{'OVERDAMPED' if 1.5*H_at_fold/m_tau > 1 else 'UNDERDAMPED'}")

print(f"\n3. Damping factor:")
print(f"   exp(-F_total) = {np.exp(-F_total):.4e}")
print(f"   Velocity damping |dtau/dt|(end) / |dtau/dt|(0) = {dtau_ratio_end:.4e}")
if gamma_eff > 0:
    print(f"   Effective damping rate: {gamma_eff:.4f} per efold")

print(f"\n4. Decay timescale comparison:")
print(f"   tau_decay = {tau_decay_s:.2e} s = {t_decay_MKK:.2e} M_KK^{{-1}}")
if t_decay_MKK > t_end_MKK:
    print(f"   Modulus OUTLIVES the ODE integration window ({t_end_MKK:.0f} M_KK^{{-1}})")
    print(f"   Hubble friction completely dominates over particle decay")
else:
    if N_at_decay is not None:
        print(f"   At decay time: F = {F_at_decay:.4f}, exp(-F) = {np.exp(-F_at_decay):.4e}")

# Determine which dominates: friction or decay
# Friction rate: gamma_friction ~ 3H/2
# Decay rate: Gamma_decay = 1/tau_decay (in physical units)
Gamma_decay_MKK = 1.0 / t_decay_MKK if t_decay_MKK > 0 else 0  # (local) in M_KK units
gamma_friction_MKK = 1.5 * H_avg_full  # (local) 3H/2 in M_KK units

print(f"\n5. Rate comparison:")
print(f"   gamma_friction = 3H/2 = {gamma_friction_MKK:.6f} M_KK")
print(f"   Gamma_decay = 1/tau_decay = {Gamma_decay_MKK:.6e} M_KK")
print(f"   gamma_friction / Gamma_decay = {gamma_friction_MKK / Gamma_decay_MKK:.4e}")
if gamma_friction_MKK > Gamma_decay_MKK:
    dominance = "FRICTION DOMINATES"
    ratio_dom = gamma_friction_MKK / Gamma_decay_MKK  # (local)
    print(f"   >> {dominance} by factor {ratio_dom:.2e}")
else:
    dominance = "DECAY DOMINATES"
    ratio_dom = Gamma_decay_MKK / gamma_friction_MKK  # (local)
    print(f"   >> {dominance} by factor {ratio_dom:.2e}")

print(f"\n6. Physical picture:")
print(f"   The bare potential is monotonically increasing (S36).")
print(f"   BCS dressing too weak by 72x to create a minimum (S77 W1-A).")
print(f"   tau rolls monotonically downhill after the fold (N_osc = 0).")
print(f"   Hubble friction continuously decelerates the roll.")
print(f"   The modulus motion is effectively a SLOW ROLL INTO OBLIVION,")
print(f"   not an oscillation about a minimum.")

gate_verdict = "INFO"  # (local)
print(f"\nGate S77-B9-FRICTION: {gate_verdict}")
print(f"  N_osc = {n_oscillations}")
print(f"  F_total = {F_total:.4f}")
print(f"  exp(-F_total) = {np.exp(-F_total):.4e}")
print(f"  {dominance}")

# ============================================================
# Save results
# ============================================================
np.savez('s77_friction_integral.npz',
         # Gate metadata
         gate_name='S77-B9-FRICTION',
         gate_verdict=gate_verdict,
         gate_detail=(f"N_osc={n_oscillations}, F_total={F_total:.4f}, "
                      f"exp(-F)={np.exp(-F_total):.4e}, {dominance}"),
         # Core results
         F_total=F_total,
         F_1ef=F_1ef,
         F_10ef=F_10ef,
         F_modulus=F_modulus,
         exp_neg_F=np.exp(-F_total),
         n_oscillations=n_oscillations,
         # Trajectory characterization
         tau_max_val=tau_max_val,
         N_turnaround=N_turnaround,
         N_dS_onset=N_dS_onset,
         # Damping profile
         gamma_eff=gamma_eff,
         N_edamp=N_edamp,
         dtau_ratio_end=dtau_ratio_end,
         # Critical damping ratios
         ratio_3H2_mtau_fold=1.5 * H_at_fold / m_tau,
         ratio_3H2_mtau_late=1.5 * H_late / m_tau,
         # Rate comparison
         gamma_friction_MKK=gamma_friction_MKK,
         Gamma_decay_MKK=Gamma_decay_MKK,
         dominance=dominance,
         ratio_friction_decay=gamma_friction_MKK / Gamma_decay_MKK,
         # Decay timescales
         tau_decay_s=tau_decay_s,
         t_decay_MKK=t_decay_MKK,
         # Velocity profile
         dtau_init=dtau_init,
         dtau_ratio_1ef=dtau_ratio_1ef,
         dtau_ratio_10ef=dtau_ratio_10ef,
         # Cumulative friction
         F_cumulative=F_full,
         N_cumulative=N_sol[1:],
         # Kinetic energy fraction
         eps_KE_at_fold=eps_KE[0],
         eps_KE_at_1ef=eps_KE[idx_1ef],
         eps_KE_at_10ef=eps_KE[idx_10ef],
         )

elapsed = time.time() - start
print(f"\nElapsed: {elapsed:.2f}s")
print(f"Output: s77_friction_integral.npz")
