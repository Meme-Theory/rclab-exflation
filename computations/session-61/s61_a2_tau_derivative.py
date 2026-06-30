#!/usr/bin/env python3
"""
s61_a2_tau_derivative.py — Heat Kernel a_2 Tau Derivative (A2-TRANSIT-61)
=========================================================================

Hawking-Theorist computation, Session 61 Wave 2.

Computes d(a_2)/d(tau) along the transit path tau in [0, 0.25].
Determines whether G_eff evolves during transit.

Physics:
  a_2^{SD}(tau) = (4pi)^{-4} * (20/3) * R(tau) * Vol(tau)

  where Vol(tau) = Vol_round * e^{-5*tau} (Jensen deformation compresses
  5 complement directions, each scaling by e^{-tau}).

  R(tau) = scalar curvature from Milnor formula on SU(3) with Jensen metric.

  Product rule:
    da_2/dtau = (4pi)^{-4} * (20/3) * [dR/dtau * Vol(tau) + R(tau) * dVol/dtau]
              = (4pi)^{-4} * (20/3) * Vol(tau) * [dR/dtau - 5*R(tau)]

  since dVol/dtau = -5 * Vol(tau).

Gate: A2-TRANSIT-61
  PASS if d(a_2)/dtau monotonic and nonzero in [0, 0.25].
  FAIL if a_2 constant (da_2/dtau = 0).
  INFO if sign change.

Reads: computations/session-61/s61_heat_kernel_a2.npz (Wave 1 data)
Writes: computations/session-61/s61_a2_tau_derivative.npz
        computations/session-61/s61_a2_tau_derivative.png
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    PI, Vol_SU3_Haar, tau_fold
)
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ============================================================================
#  Load Wave 1 data
# ============================================================================

data = np.load(os.path.join(os.path.dirname(__file__), 's61_heat_kernel_a2.npz'),
               allow_pickle=True)

tau_arr = data['tau_arr']       # 100 points, [0, 0.5]
R_arr   = data['R_arr']         # Scalar curvature R(tau) from Milnor formula
N_tau   = int(data['N_tau'])

# ============================================================================
#  Restrict to tau in [0, 0.25]
# ============================================================================

mask = tau_arr <= 0.25 + 1e-10
tau = tau_arr[mask]
R   = R_arr[mask]
N_pts = len(tau)
dtau = tau[1] - tau[0]  # uniform spacing

print(f"Working with {N_pts} tau points in [0, {tau[-1]:.4f}]")
print(f"dtau = {dtau:.8f}")
print(f"R(0) = {R[0]:.6f}, R(fold) = {R_arr[int(data['idx_fold'])]:.6f}")

# ============================================================================
#  Compute Volume and physically correct a_2
# ============================================================================

# Vol(tau) = Vol_round * e^{-5*tau}
Vol = Vol_SU3_Haar * np.exp(-5.0 * tau)

# Seeley-DeWitt prefactor
prefactor = (4.0 * PI)**(-4) * (20.0 / 3.0)

# a_2(tau) = prefactor * R(tau) * Vol(tau)
a2 = prefactor * R * Vol

print(f"\n--- Physical a_2(tau) with volume deformation ---")
print(f"a_2(0)    = {a2[0]:.8f}")
idx_fold = np.argmin(np.abs(tau - tau_fold))
print(f"a_2(fold) = {a2[idx_fold]:.8f}  (tau={tau[idx_fold]:.4f})")
print(f"a_2(max)  = {a2[-1]:.8f}  (tau={tau[-1]:.4f})")

# Also store the W1 version (without volume deformation) for comparison
a2_noVol = prefactor * R * Vol_SU3_Haar  # = W1's a2_SD_arr restricted

# ============================================================================
#  Compute dR/dtau (numerical, central differences)
# ============================================================================

dR_dtau = np.gradient(R, dtau)

# Also compute 2nd derivative for curvature analysis
d2R_dtau2 = np.gradient(dR_dtau, dtau)

print(f"\n--- dR/dtau ---")
print(f"dR/dtau(0)    = {dR_dtau[0]:.8f}")
print(f"dR/dtau(fold) = {dR_dtau[idx_fold]:.8f}")
print(f"dR/dtau(0.25) = {dR_dtau[-1]:.8f}")
print(f"dR/dtau range: [{dR_dtau.min():.8f}, {dR_dtau.max():.8f}]")

# ============================================================================
#  Compute da_2/dtau: analytical via product rule
# ============================================================================

# da_2/dtau = prefactor * Vol(tau) * [dR/dtau - 5*R(tau)]
# Two contributions:
#   (A) curvature growth:  prefactor * Vol * dR/dtau
#   (B) volume collapse:   prefactor * Vol * (-5*R) = -5 * a_2

da2_curvature = prefactor * Vol * dR_dtau         # Term (A)
da2_volume    = prefactor * Vol * (-5.0 * R)       # Term (B)
da2_analytic  = da2_curvature + da2_volume         # Total

# Cross-check: numerical derivative of a_2
da2_numerical = np.gradient(a2, dtau)

# Relative discrepancy
rel_err = np.abs(da2_analytic - da2_numerical) / (np.abs(da2_analytic) + 1e-30)

print(f"\n--- da_2/dtau ---")
print(f"da_2/dtau(0) [analytic]  = {da2_analytic[0]:.8f}")
print(f"da_2/dtau(0) [numerical] = {da2_numerical[0]:.8f}")
print(f"Max relative discrepancy = {rel_err[2:-2].max():.2e}")  # exclude edges
print()
print(f"da_2/dtau(fold) = {da2_analytic[idx_fold]:.8f}")
print(f"da_2/dtau(0.25) = {da2_analytic[-1]:.8f}")
print()

# ============================================================================
#  Sign analysis: Is da_2/dtau monotonically nonzero?
# ============================================================================

sign_arr = np.sign(da2_analytic)
sign_changes = np.sum(np.abs(np.diff(sign_arr)) > 0)
all_negative = np.all(da2_analytic < 0)
all_positive = np.all(da2_analytic > 0)
any_zero = np.any(np.abs(da2_analytic) < 1e-15)

# Check monotonicity of da_2/dtau itself
d2a2 = np.gradient(da2_analytic, dtau)
da2_monotone = np.all(d2a2[2:-2] <= 0) or np.all(d2a2[2:-2] >= 0)

# Competition ratio: |dR/dtau| vs |5*R|
competition = np.abs(dR_dtau) / (5.0 * R)

print(f"--- Sign Analysis ---")
print(f"Sign changes in da_2/dtau: {sign_changes}")
print(f"All negative: {all_negative}")
print(f"All positive: {all_positive}")
print(f"Any zero crossings: {any_zero}")
print(f"da_2/dtau monotone (interior): {da2_monotone}")
print(f"Competition ratio |dR'/dtau| / |5R| : [{competition.min():.6f}, {competition.max():.6f}]")
print(f"  -> Volume term dominates by factor 1/ratio = [{1/competition.max():.1f}, {1/competition.min():.1f}]")

# ============================================================================
#  Fractional change in a_2 across transit
# ============================================================================

a2_at_0 = a2[0]
a2_at_fold = a2[idx_fold]
a2_at_025 = a2[-1]

frac_0_to_fold = (a2_at_fold - a2_at_0) / a2_at_0
frac_0_to_025  = (a2_at_025 - a2_at_0) / a2_at_0

# G_eff ~ 1/a_2, so delta_G/G = -delta_a2/a2
delta_G_0_to_fold = -frac_0_to_fold
delta_G_0_to_025  = -frac_0_to_025

print(f"\n--- Fractional Changes ---")
print(f"a_2(0)    = {a2_at_0:.8f}")
print(f"a_2(fold) = {a2_at_fold:.8f}")
print(f"a_2(0.25) = {a2_at_025:.8f}")
print(f"Delta(a_2)/a_2 [0->fold]  = {frac_0_to_fold:.6f} = {frac_0_to_fold*100:.2f}%")
print(f"Delta(a_2)/a_2 [0->0.25]  = {frac_0_to_025:.6f} = {frac_0_to_025*100:.2f}%")
print(f"Delta(G_eff)/G [0->fold]  = {delta_G_0_to_fold:.6f} = {delta_G_0_to_fold*100:.2f}%")
print(f"Delta(G_eff)/G [0->0.25]  = {delta_G_0_to_025:.6f} = {delta_G_0_to_025*100:.2f}%")

# ============================================================================
#  Characteristic scales
# ============================================================================

# e-folding scale for a_2 decay
tau_efold = -a2 / da2_analytic  # tau scale over which a_2 drops by factor e

print(f"\n--- Characteristic Scales ---")
print(f"tau_efold(0)    = {tau_efold[0]:.6f}")
print(f"tau_efold(fold) = {tau_efold[idx_fold]:.6f}")
print(f"tau_efold(0.25) = {tau_efold[-1]:.6f}")

# ============================================================================
#  Gate Verdict
# ============================================================================

if all_negative and sign_changes == 0:
    verdict = "PASS"
    detail = (f"da_2/dtau < 0 everywhere in [0, 0.25]. "
              f"Monotonically decreasing. "
              f"Delta(a_2)/a_2 = {frac_0_to_fold*100:.1f}% at fold, "
              f"{frac_0_to_025*100:.1f}% at tau=0.25. "
              f"G_eff INCREASES during transit by {delta_G_0_to_fold*100:.1f}% to fold.")
elif all_positive and sign_changes == 0:
    verdict = "PASS"
    detail = (f"da_2/dtau > 0 everywhere in [0, 0.25]. "
              f"Monotonically increasing.")
elif sign_changes > 0:
    # Find the sign change locations
    sc_idx = np.where(np.abs(np.diff(sign_arr)) > 0)[0]
    sc_taus = 0.5 * (tau[sc_idx] + tau[sc_idx + 1])
    verdict = "INFO"
    detail = (f"Sign change(s) in da_2/dtau at tau = {sc_taus}. "
              f"a_2 has turning point(s).")
elif any_zero:
    verdict = "FAIL"
    detail = "da_2/dtau = 0 identically (a_2 constant)."
else:
    verdict = "PASS"
    detail = f"da_2/dtau nonzero and monotonic."

print(f"\n{'='*60}")
print(f"GATE: A2-TRANSIT-61")
print(f"VERDICT: {verdict}")
print(f"DETAIL: {detail}")
print(f"{'='*60}")

# ============================================================================
#  Save data
# ============================================================================

outpath = os.path.join(os.path.dirname(__file__), 's61_a2_tau_derivative.npz')
np.savez(outpath,
    # Grid
    tau=tau,
    dtau=dtau,
    N_pts=N_pts,
    idx_fold=idx_fold,
    tau_fold=tau_fold,
    # Physical a_2 (with volume deformation)
    a2_physical=a2,
    a2_noVol=a2_noVol,
    # Curvature
    R=R,
    dR_dtau=dR_dtau,
    d2R_dtau2=d2R_dtau2,
    # Volume
    Vol=Vol,
    # Derivatives
    da2_analytic=da2_analytic,
    da2_numerical=da2_numerical,
    da2_curvature=da2_curvature,
    da2_volume=da2_volume,
    # Sign analysis
    sign_changes=sign_changes,
    competition_ratio=competition,
    # Fractional changes
    frac_0_to_fold=frac_0_to_fold,
    frac_0_to_025=frac_0_to_025,
    delta_G_0_to_fold=delta_G_0_to_fold,
    delta_G_0_to_025=delta_G_0_to_025,
    # Characteristic scale
    tau_efold=tau_efold,
    # Gate
    gate_name='A2-TRANSIT-61',
    gate_verdict=verdict,
    gate_detail=detail,
)
print(f"\nSaved: {outpath}")

# ============================================================================
#  Plot
# ============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle(r'Heat Kernel $a_2(\tau)$ and $da_2/d\tau$ — A2-TRANSIT-61', fontsize=14)

# --- Panel 1: a_2(tau) with and without volume ---
ax = axes[0, 0]
ax.plot(tau, a2, 'b-', linewidth=2, label=r'$a_2(\tau)$ [physical, with Vol]')
ax.plot(tau, a2_noVol, 'r--', linewidth=1.5, label=r'$a_2(\tau)$ [W1, no Vol deform]')
ax.axvline(tau_fold, color='gray', linestyle=':', alpha=0.7, label=f'fold ({tau_fold})')
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$a_2$')
ax.set_title(r'$a_2(\tau)$: Physical vs Wave-1')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# --- Panel 2: da_2/dtau decomposition ---
ax = axes[0, 1]
ax.plot(tau, da2_analytic, 'b-', linewidth=2, label=r'$da_2/d\tau$ (total)')
ax.plot(tau, da2_curvature, 'g--', linewidth=1.5, label=r'curvature term ($dR/d\tau \cdot \mathrm{Vol}$)')
ax.plot(tau, da2_volume, 'r-.', linewidth=1.5, label=r'volume term ($-5R \cdot \mathrm{Vol}$)')
ax.axhline(0, color='k', linewidth=0.5)
ax.axvline(tau_fold, color='gray', linestyle=':', alpha=0.7)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$da_2/d\tau$')
ax.set_title(r'$da_2/d\tau$ decomposition')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# --- Panel 3: competition ratio ---
ax = axes[1, 0]
ax.semilogy(tau[1:], competition[1:], 'k-', linewidth=2)
ax.axhline(1.0, color='r', linestyle='--', alpha=0.7, label='parity')
ax.axvline(tau_fold, color='gray', linestyle=':', alpha=0.7)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel(r'$|dR/d\tau| / (5R)$')
ax.set_title(r'Competition ratio: curvature growth vs volume collapse')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# --- Panel 4: fractional a_2 decay and G_eff evolution ---
ax = axes[1, 1]
ax.plot(tau, a2 / a2[0], 'b-', linewidth=2, label=r'$a_2(\tau)/a_2(0)$')
ax.plot(tau, a2[0] / a2, 'r-', linewidth=2, label=r'$G_\mathrm{eff}(\tau)/G_\mathrm{eff}(0) = a_2(0)/a_2(\tau)$')
ax.axvline(tau_fold, color='gray', linestyle=':', alpha=0.7, label=f'fold ({tau_fold})')
ax.axhline(1.0, color='k', linewidth=0.5)
ax.set_xlabel(r'$\tau$')
ax.set_ylabel('Ratio to initial value')
ax.set_title(r'$a_2$ decay and $G_\mathrm{eff}$ evolution during transit')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plotpath = os.path.join(os.path.dirname(__file__), 's61_a2_tau_derivative.png')
fig.savefig(plotpath, dpi=150, bbox_inches='tight')
print(f"Saved: {plotpath}")

# ============================================================================
#  Summary table
# ============================================================================

print(f"\n{'='*60}")
print("SUMMARY TABLE")
print(f"{'='*60}")
print(f"{'tau':>8} | {'a_2':>12} | {'da_2/dtau':>12} | {'a_2/a_2(0)':>10} | {'G/G(0)':>10}")
print(f"{'-'*8}-+-{'-'*12}-+-{'-'*12}-+-{'-'*10}-+-{'-'*10}")
for i_show in [0, idx_fold, N_pts-1]:
    t = tau[i_show]
    print(f"{t:>8.4f} | {a2[i_show]:>12.8f} | {da2_analytic[i_show]:>12.8f} | "
          f"{a2[i_show]/a2[0]:>10.6f} | {a2[0]/a2[i_show]:>10.6f}")

# Additional key points
for t_check in [0.05, 0.10, 0.15, 0.20]:
    i_c = np.argmin(np.abs(tau - t_check))
    print(f"{tau[i_c]:>8.4f} | {a2[i_c]:>12.8f} | {da2_analytic[i_c]:>12.8f} | "
          f"{a2[i_c]/a2[0]:>10.6f} | {a2[0]/a2[i_c]:>10.6f}")

print(f"\nKey: G_eff ~ 1/a_2, so G_eff(tau)/G_eff(0) = a_2(0)/a_2(tau)")
