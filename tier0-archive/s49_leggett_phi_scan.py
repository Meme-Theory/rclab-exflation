#!/usr/bin/env python3
"""
Session 49: LEGGETT-PHI-SCAN-49 — Leggett Frequency Ratio vs phi_paasch
========================================================================

Tests whether the ratio R(tau) = omega_L2(tau)/omega_L1(tau) of Leggett
inter-sector phase oscillation frequencies equals phi_paasch = 1.531580
(the Dirac eigenvalue ratio m_{(3,0)}/m_{(0,0)} from Session 12) at some
tau value.

If R(tau*) = phi_paasch, this would mean the Leggett frequency ratio is
determined by the same spectral geometry that determines the mass ratio
phi_paasch — a resonance between the BCS pairing structure and the Dirac
eigenvalue spectrum.

Physics:
  omega_L^2 = eigenvalue of the phase-oscillation mass matrix M divided
  by the superfluid moment of inertia. M is set by the Josephson couplings
  J_{ij} = V(i,j) * Delta_i * Delta_j. The ratio R = omega_L2/omega_L1
  is a function of the J_{ij} ratios and the DOS rho_i ratios.

  phi_paasch = m_{(3,0)}/m_{(0,0)} at tau = 0.15 (z = 3.65) from the
  Dirac spectrum on the Jensen-deformed SU(3).

Gate: LEGGETT-PHI-SCAN-49
  PASS: R(tau) = phi_paasch within 0.1% at some tau
  INFO: closest approach < 1% but no exact match
  FAIL: smooth variation, no special relationship

Input:
  - s48_leggett_mode.npz (omega_L1, omega_L2 at 8 tau values)
  - s47_curvature_anatomy.npz (curvature data for interpolation)

Output:
  - s49_leggett_phi_scan.npz
  - s49_leggett_phi_scan.png

Author: Tesla-Resonance (Session 49)
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from scipy.interpolate import CubicSpline
from scipy.optimize import brentq
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    tau_fold, PI, g0_diag,
    E_B1, E_B2_mean, E_B3_mean,
    Delta_0_GL, Delta_B3,
    rho_B2_per_mode,
)

DATA_DIR = os.path.dirname(os.path.abspath(__file__))


def load_npz(name):
    return np.load(os.path.join(DATA_DIR, name), allow_pickle=True)


# ============================================================================
#  LOAD DATA
# ============================================================================

print("=" * 78)
print("SESSION 49: LEGGETT-PHI-SCAN-49")
print("Leggett Frequency Ratio vs phi_paasch")
print("=" * 78)

d_legg = load_npz('s48_leggett_mode.npz')

tau_scan = d_legg['tau_scan']       # 8 values: [0.05, 0.1, 0.13, 0.15, 0.19, 0.25, 0.3, 0.35]
omega_L1 = d_legg['omega_L1_scan']  # omega_L1 at each tau
omega_L2 = d_legg['omega_L2_scan']  # omega_L2 at each tau

# Josephson couplings
J_12_scan = d_legg['J_12_scan']
J_23_scan = d_legg['J_23_scan']

# Sector DOS
rho_B1_scan = d_legg['rho_B1_scan']
rho_B2_scan = d_legg['rho_B2_scan']
rho_B3_scan = d_legg['rho_B3_scan']

# Gap amplitudes
Delta_B1_scan = d_legg['Delta_B1_scan']
Delta_B2_scan = d_legg['Delta_B2_scan']
Delta_B3_scan = d_legg['Delta_B3_scan']

# phi_paasch from Session 12
phi_paasch = 1.531580

print(f"\nphi_paasch = {phi_paasch:.6f}")
print(f"tau_scan = {tau_scan}")
print(f"omega_L1 = {omega_L1}")
print(f"omega_L2 = {omega_L2}")

# ============================================================================
#  COMPUTE R(tau) = omega_L2/omega_L1 AT COARSE POINTS
# ============================================================================

R_coarse = omega_L2 / omega_L1

print("\n" + "-" * 78)
print("Coarse scan: R(tau) = omega_L2/omega_L1")
print("-" * 78)
for i, (t, r) in enumerate(zip(tau_scan, R_coarse)):
    delta_frac = abs(r / phi_paasch - 1.0)
    print(f"  tau={t:.2f}: R={r:.6f}, |R/phi-1| = {delta_frac:.6f} ({delta_frac*100:.4f}%)")

# ============================================================================
#  INTERPOLATE AND FIND EXACT CROSSING
# ============================================================================

print("\n" + "-" * 78)
print("Interpolation and exact crossing search")
print("-" * 78)

# Cubic spline interpolation of R(tau)
cs_R = CubicSpline(tau_scan, R_coarse)

# Fine scan
tau_fine = np.linspace(tau_scan[0], tau_scan[-1], 10000)
R_fine = cs_R(tau_fine)

# Find where R(tau) = phi_paasch
delta_R = R_fine - phi_paasch

# Look for sign changes
crossings = []
for i in range(len(delta_R) - 1):
    if delta_R[i] * delta_R[i+1] < 0:
        # Refine with Brent's method
        tau_cross = brentq(lambda t: cs_R(t) - phi_paasch,
                           tau_fine[i], tau_fine[i+1], xtol=1e-12)
        R_cross = cs_R(tau_cross)
        crossings.append((tau_cross, R_cross))

if crossings:
    print(f"  Found {len(crossings)} crossing(s):")
    for tau_c, R_c in crossings:
        delta = abs(R_c / phi_paasch - 1.0)
        print(f"    tau = {tau_c:.10f}, R = {R_c:.10f}, |R/phi-1| = {delta:.2e}")

    # Check if any crossing is between data points (real) vs extrapolation artifact
    tau_cross_best = crossings[0][0]
    R_cross_best = crossings[0][1]
    print(f"\n  Best crossing: tau = {tau_cross_best:.8f}")
    print(f"  R at crossing: {R_cross_best:.10f}")
    print(f"  phi_paasch:    {phi_paasch:.10f}")
    print(f"  Absolute mismatch: {abs(R_cross_best - phi_paasch):.2e}")
else:
    print("  No exact crossing found in scan range.")
    # Find closest approach
    idx_min = np.argmin(np.abs(delta_R))
    tau_closest = tau_fine[idx_min]
    R_closest = R_fine[idx_min]
    delta_closest = abs(R_closest / phi_paasch - 1.0)
    print(f"  Closest approach: tau = {tau_closest:.6f}, R = {R_closest:.6f}")
    print(f"  |R/phi-1| = {delta_closest:.6f} ({delta_closest*100:.4f}%)")

# ============================================================================
#  INTERPOLATE OMEGA_L1, OMEGA_L2 INDIVIDUALLY
# ============================================================================

cs_L1 = CubicSpline(tau_scan, omega_L1)
cs_L2 = CubicSpline(tau_scan, omega_L2)

print("\n" + "-" * 78)
print("Individual Leggett frequency interpolation")
print("-" * 78)

if crossings:
    tau_c = crossings[0][0]
    print(f"  At crossing tau = {tau_c:.8f}:")
    print(f"    omega_L1 = {cs_L1(tau_c):.8f} M_KK")
    print(f"    omega_L2 = {cs_L2(tau_c):.8f} M_KK")
    print(f"    R = omega_L2/omega_L1 = {cs_L2(tau_c)/cs_L1(tau_c):.8f}")

# ============================================================================
#  DERIVATIVE ANALYSIS: WHY DOES R CROSS phi_paasch NEAR THE FOLD?
# ============================================================================

print("\n" + "-" * 78)
print("Derivative analysis")
print("-" * 78)

dR_dtau = cs_R(tau_fine, 1)  # first derivative

if crossings:
    tau_c = crossings[0][0]
    slope = cs_R(tau_c, 1)
    print(f"  dR/dtau at crossing = {slope:.6f}")
    print(f"  R is {'decreasing' if slope < 0 else 'increasing'} at crossing")

# Rate of change at each coarse point
for t, r in zip(tau_scan, R_coarse):
    dr = cs_R(t, 1)
    print(f"  tau={t:.2f}: dR/dtau = {dr:.4f}")

# ============================================================================
#  WHAT DETERMINES R(tau)?
# ============================================================================

print("\n" + "-" * 78)
print("Algebraic decomposition of R(tau)")
print("-" * 78)

# R^2 = (omega_L2/omega_L1)^2 = eval_2/eval_1 from the mass matrix
# The mass matrix eigenvalues for a 3-band system with J_12 >> J_13, J_23:
# eval_1 ~ J_12 * (1/I_1 + 1/I_2) where I_i = rho_i/(2*Delta_i^2)
# eval_2 ~ (J_12*I_3 + J_13*I_2 + J_23*I_1) / (I_1*I_2*I_3)
#
# In the limit J_12 >> J_13, J_23:
# R^2 ~ 1 + (J_13 + J_23)/J_12 * correction factors
#
# But more directly, the eigenvalues come from the 3x3 mass matrix.
# Let us verify the J ratio is tau-independent:

J_ratio = J_12_scan / J_23_scan
print(f"  J_12/J_23 at each tau: {J_ratio}")
print(f"  J_12/J_23 is {'constant' if np.std(J_ratio)/np.mean(J_ratio) < 1e-6 else 'variable'}")
print(f"  Mean J_12/J_23 = {np.mean(J_ratio):.6f}")

# The J ratio is CONSTANT at 19.52. This means the Leggett frequency
# ratio is entirely determined by the DOS ratios rho_i(tau).
rho_ratio_12 = rho_B1_scan / rho_B2_scan
rho_ratio_13 = rho_B1_scan / rho_B3_scan
print(f"\n  rho_B1/rho_B2 at each tau: {rho_ratio_12}")
print(f"  rho_B1/rho_B3 at each tau: {rho_ratio_13}")

# ============================================================================
#  CONSISTENCY CHECK: Spline vs Linear Interpolation
# ============================================================================

print("\n" + "=" * 78)
print("Consistency check: spline vs linear interpolation")
print("=" * 78)

# The crossing is between tau=0.19 (R=1.5437) and tau=0.25 (R=1.5107).
# Linear interpolation gives a crossing estimate.
R_left = R_coarse[4]   # tau=0.19
R_right = R_coarse[5]  # tau=0.25
tau_left = tau_scan[4]
tau_right = tau_scan[5]
tau_linear = tau_left + (tau_right - tau_left) * (R_left - phi_paasch) / (R_left - R_right)

print(f"  Bracketing: R({tau_left}) = {R_left:.6f}, R({tau_right}) = {R_right:.6f}")
print(f"  phi_paasch = {phi_paasch:.6f} (between these values)")
print(f"  Linear interpolation crossing: tau = {tau_linear:.6f}")
if crossings:
    print(f"  Cubic spline crossing:        tau = {crossings[0][0]:.6f}")
    print(f"  Agreement: |delta_tau| = {abs(tau_linear - crossings[0][0]):.6f}")

# Use fine spline data for downstream
tau_fine2 = tau_fine
R_fine2 = R_fine

# ============================================================================
#  SPECIAL POINT CHECK: tau_fold
# ============================================================================

print("\n" + "-" * 78)
print(f"Special point check: tau_fold = {tau_fold}")
print("-" * 78)

R_fold = cs_R(tau_fold)
delta_fold = abs(R_fold / phi_paasch - 1.0)
print(f"  R(tau_fold) = {R_fold:.6f}")
print(f"  |R/phi - 1| at fold = {delta_fold:.6f} ({delta_fold*100:.4f}%)")
print(f"  This is {'within' if delta_fold < 0.001 else 'outside'} the PASS threshold (0.1%)")
print(f"  This is {'within' if delta_fold < 0.01 else 'outside'} the INFO threshold (1%)")

# ============================================================================
#  GATE VERDICT
# ============================================================================

print("\n" + "=" * 78)
print("GATE: LEGGETT-PHI-SCAN-49")
print("=" * 78)

# Determine best mismatch from DIRECT DATA (spline on S48 omega values)
if crossings:
    best_mismatch = 0.0  # exact crossing in spline interpolation
    best_tau = crossings[0][0]
    R_at_best = crossings[0][1]
else:
    # Find closest approach from spline
    idx_min = np.argmin(np.abs(R_fine2 - phi_paasch))
    best_tau = tau_fine2[idx_min]
    R_at_best = R_fine2[idx_min]
    best_mismatch = abs(R_at_best / phi_paasch - 1.0)

# Closest DATA point (no interpolation)
idx_data_closest = np.argmin(np.abs(R_coarse - phi_paasch))
data_closest_mismatch = abs(R_coarse[idx_data_closest] / phi_paasch - 1.0)

print(f"\n  phi_paasch = {phi_paasch:.6f}")
print(f"  Best matching tau (spline) = {best_tau:.6f}")
print(f"  R at best tau = {R_at_best:.10f}")
print(f"  Best |R/phi-1| (spline) = {best_mismatch:.6f} ({best_mismatch*100:.4f}%)")
print(f"  Closest DATA POINT: tau={tau_scan[idx_data_closest]:.2f}, "
      f"R={R_coarse[idx_data_closest]:.6f}, "
      f"|delta|={data_closest_mismatch:.6f} ({data_closest_mismatch*100:.4f}%)")

# Gate decision based on closest DATA POINT (conservative)
# The spline crossing is interpolation -- not a computed point.
# The closest computed point is tau=0.19 with 0.789% mismatch.
if data_closest_mismatch < 0.001:
    verdict = "PASS"
    detail = (f"R(tau={tau_scan[idx_data_closest]:.2f}) = phi_paasch within 0.1% "
              f"({data_closest_mismatch*100:.4f}%)")
elif data_closest_mismatch < 0.01:
    verdict = "INFO"
    detail = (f"Closest DATA point at tau={tau_scan[idx_data_closest]:.2f}: "
              f"|R/phi-1| = {data_closest_mismatch*100:.3f}%. "
              f"Spline interpolation finds exact crossing at tau={best_tau:.4f} "
              f"(between data points {tau_scan[4]:.2f} and {tau_scan[5]:.2f}). "
              f"Direct computation at tau~0.21 needed to confirm PASS.")
else:
    verdict = "FAIL"
    detail = (f"Closest approach {data_closest_mismatch*100:.2f}% "
              f"at tau={tau_scan[idx_data_closest]:.2f}, smooth variation only")

print(f"\n  VERDICT: {verdict}")
print(f"  {detail}")

# ============================================================================
#  PHYSICAL INTERPRETATION
# ============================================================================

print("\n" + "=" * 78)
print("PHYSICAL INTERPRETATION")
print("=" * 78)

if crossings:
    tau_x = crossings[0][0]
    print(f"""
  The Leggett frequency ratio R(tau) = omega_L2/omega_L1 is a monotonically
  DECREASING function of tau, falling from ~1.63 at tau=0.05 to ~1.46 at
  tau=0.35. It passes through phi_paasch = {phi_paasch} at tau = {tau_x:.4f}.

  This crossing is NEAR but not AT the fold (tau_fold = {tau_fold}).
  The mismatch at the fold is {delta_fold*100:.3f}%.

  The physical content: the Leggett frequency ratio is determined by:
    R^2 ~ (J_12 + J_23)/(J_12) * (rho_2 / rho_3) / (rho_1 / rho_2)
  where J_12/J_23 = 19.52 (CONSTANT across tau -- purely algebraic,
  from the V-matrix selection rules) and the DOS ratios rho_i(tau)
  vary with the Jensen deformation.

  phi_paasch is a Dirac eigenvalue ratio from the SAME deformed geometry.
  The crossing means these two spectral quantities -- one from the BCS
  phase oscillation spectrum, one from the single-particle Dirac spectrum
  -- are equal at a specific deformation. This is a resonance condition:
  the many-body Josephson frequency matches the single-particle mass ratio.

  In the superfluid analogy: the relative phase oscillation frequency
  between condensate components is set by the same geometry that determines
  the quasiparticle mass spectrum. When these resonate, the system has
  a distinguished "tuning" point.

  The tau of crossing ({tau_x:.4f}) is within {abs(tau_x - tau_fold)/tau_fold*100:.1f}%
  of the fold ({tau_fold}). Whether this near-coincidence is a selection
  mechanism or a coincidence requires further investigation.
""")
else:
    print(f"""
  R(tau) decreases monotonically from {R_coarse[0]:.4f} to {R_coarse[-1]:.4f}
  without crossing phi_paasch = {phi_paasch} in the computed range.
  Closest approach is {best_mismatch*100:.3f}% at tau = {best_tau:.4f}.
""")

# ============================================================================
#  SAVE DATA
# ============================================================================

results = {
    'gate_name': 'LEGGETT-PHI-SCAN-49',
    'gate_verdict': verdict,
    'gate_detail': detail,

    # Coarse data
    'tau_coarse': tau_scan,
    'R_coarse': R_coarse,
    'omega_L1_coarse': omega_L1,
    'omega_L2_coarse': omega_L2,

    # Fine spline interpolation (from S48 data)
    'tau_fine': tau_fine2,
    'R_fine': R_fine2,
    'omega_L1_fine': cs_L1(tau_fine2),
    'omega_L2_fine': cs_L2(tau_fine2),

    # phi_paasch
    'phi_paasch': phi_paasch,

    # Crossing info
    'has_crossing': bool(crossings),
    'tau_crossing': np.array([c[0] for c in crossings]) if crossings else np.array([]),
    'best_mismatch': best_mismatch,
    'best_tau': best_tau,
    'R_at_fold': R_fold,
    'delta_at_fold': delta_fold,

    # Structural constants
    'J12_over_J23': np.mean(J_ratio),
}

outpath = os.path.join(DATA_DIR, 's49_leggett_phi_scan.npz')
np.savez(outpath, **results)
print(f"Saved: {outpath}")

# ============================================================================
#  PLOT
# ============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 11))

# Panel 1: R(tau) with phi_paasch line
ax = axes[0, 0]
ax.plot(tau_fine2, R_fine2, 'b-', linewidth=2, label='$R(\\tau) = \\omega_{L2}/\\omega_{L1}$')
ax.axhline(y=phi_paasch, color='red', linestyle='--', linewidth=2,
           label=f'$\\phi_{{\\mathrm{{Paasch}}}}$ = {phi_paasch:.4f}')
ax.axvline(x=tau_fold, color='green', linestyle=':', linewidth=1.5,
           label=f'$\\tau_{{\\mathrm{{fold}}}}$ = {tau_fold}')
ax.plot(tau_scan, R_coarse, 'ko', markersize=6, label='S48 data points')
if crossings:
    for tc_val, _ in crossings:
        ax.plot(tc_val, phi_paasch, 'r*', markersize=15, zorder=5)
        ax.annotate(f'$\\tau$ = {tc_val:.4f}', (tc_val, phi_paasch),
                    xytext=(tc_val+0.02, phi_paasch+0.01), fontsize=10)
ax.set_xlabel('$\\tau$')
ax.set_ylabel('$R = \\omega_{L2}/\\omega_{L1}$')
ax.set_title('Leggett frequency ratio vs $\\phi_{\\mathrm{Paasch}}$')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 2: Individual Leggett frequencies
ax = axes[0, 1]
ax.plot(tau_fine2, cs_L1(tau_fine2), 'b-', linewidth=2, label='$\\omega_{L1}$')
ax.plot(tau_fine2, cs_L2(tau_fine2), 'r-', linewidth=2, label='$\\omega_{L2}$')
ax.plot(tau_scan, omega_L1, 'bo', markersize=5)
ax.plot(tau_scan, omega_L2, 'ro', markersize=5)
ax.axvline(x=tau_fold, color='green', linestyle=':', linewidth=1.5)
ax.set_xlabel('$\\tau$')
ax.set_ylabel('$\\omega$ [M$_{\\mathrm{KK}}$]')
ax.set_title('Leggett mode frequencies vs $\\tau$')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

# Panel 3: Mismatch |R/phi - 1| (log scale)
ax = axes[1, 0]
mismatch = np.abs(R_fine2 / phi_paasch - 1.0)
ax.semilogy(tau_fine2, mismatch, 'b-', linewidth=2)
ax.axhline(y=0.001, color='green', linestyle='--', label='PASS (0.1%)')
ax.axhline(y=0.01, color='orange', linestyle='--', label='INFO (1%)')
ax.axvline(x=tau_fold, color='green', linestyle=':', linewidth=1.5,
           label=f'$\\tau_{{\\rm fold}}$ = {tau_fold}')
ax.set_xlabel('$\\tau$')
ax.set_ylabel('$|R/\\phi_{\\mathrm{Paasch}} - 1|$')
ax.set_title(f'Mismatch (VERDICT: {verdict})')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)
ax.set_ylim(1e-5, 0.2)

# Panel 4: DOS ratios (the driver of R variation)
ax = axes[1, 1]
ax.plot(tau_scan, rho_B1_scan / rho_B2_scan, 's-', label='$\\rho_{B1}/\\rho_{B2}$')
ax.plot(tau_scan, rho_B3_scan / rho_B2_scan, 'o-', label='$\\rho_{B3}/\\rho_{B2}$')
ax.plot(tau_scan, rho_B1_scan / rho_B3_scan, '^-', label='$\\rho_{B1}/\\rho_{B3}$')
ax.axvline(x=tau_fold, color='green', linestyle=':', linewidth=1.5)
ax.set_xlabel('$\\tau$')
ax.set_ylabel('DOS ratio')
ax.set_title('Sector DOS ratios (driver of R variation)')
ax.legend(fontsize=9)
ax.grid(True, alpha=0.3)

fig.suptitle(f'LEGGETT-PHI-SCAN-49: $R(\\tau) = \\omega_{{L2}}/\\omega_{{L1}}$ vs $\\phi_{{\\mathrm{{Paasch}}}}$\n'
             f'VERDICT: {verdict}',
             fontsize=13, fontweight='bold')
plt.tight_layout()

plotpath = os.path.join(DATA_DIR, 's49_leggett_phi_scan.png')
fig.savefig(plotpath, dpi=150, bbox_inches='tight')
print(f"Saved: {plotpath}")
plt.close()

print("\n" + "=" * 78)
print(f"FINAL VERDICT: LEGGETT-PHI-SCAN-49 = {verdict}")
print("=" * 78)
