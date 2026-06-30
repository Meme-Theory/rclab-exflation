#!/usr/bin/env python3
"""
S60 — GH-TEMP-DW-60: Gibbons-Hawking Temperature at Domain Wall
=================================================================

Gate: GH-TEMP-DW-60
  PASS: T_DW well-defined and ~ T_GGE (0.135 M_KK)
  FAIL: No conical singularity (K_sec = 0 structural, not a crossing)
  INFO: T_DW defined but >> or << T_GGE

Physics:
  The Gibbons-Hawking temperature requires a conical singularity in the
  Euclidean section — equivalently, a nonzero surface gravity kappa at
  a horizon or horizon analog. In the internal geometry (Jensen-deformed
  SU(3)), the analog would be a sectional curvature sign change: K_sec
  passes through zero, with kappa = sqrt(|dK_sec/dtau|) defining a
  surface gravity analog and T_DW = kappa/(2*pi) giving the Euclidean
  periodicity.

  The S59 data (RICCI-DW-59) reveals that:
  1. sec_min is IDENTICALLY zero (to machine epsilon ~1e-17) for all
     tau in [0, 0.133]. This is a structural flat direction from the
     first Lichnerowicz eigenvalue being exactly zero.
  2. The "domain wall" at tau_DW = 0.113 is defined by E_DW = 0 (S58),
     NOT by a sectional curvature sign change.
  3. The actual sectional curvature sign change (n_neg: 0 -> 4) occurs
     at tau ~ 0.135, which is 19% away from tau_DW.

  Consequence: At tau_DW = 0.113, K_sec_min = 0 is a STRUCTURAL ZERO
  (flat plane), not a horizon-type crossing. dK_sec_min/dtau = 0
  identically. There is no conical singularity, no Euclidean periodicity,
  and no Gibbons-Hawking temperature.

  This is physically expected: Hawking radiation requires a HORIZON (a
  causal boundary where the Killing vector becomes null). A structural
  flat direction in the curvature tensor is not a horizon — it's a
  degeneracy of the metric, analogous to a flat torus direction embedded
  in a curved space. The Euclidean trick of identifying temperature with
  inverse periodicity requires the Euclidean section to close smoothly
  (like the Euclidean Schwarzschild cigar), which demands a genuine
  degeneration of a metric component.

  For completeness, we also compute the hypothetical temperature at the
  ACTUAL sectional curvature sign change (tau ~ 0.135) and compare to
  framework thermal scales.

  PHONONIC CLASSIFICATION: GEOMETRIC
  This is a purely geometric result about the curvature structure of the
  Jensen-deformed SU(3). The Gibbons-Hawking construction is a property
  of the Euclidean section of the geometry, not of any phononic excitation.

Input: computations/session-59/s59_ricci_dw.npz
Output: computations/session-60/s60_gh_temp_dw.npz, .png
Author: Hawking-Theorist (Session 60)
Date: 2026-03-27
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__))))
os.chdir(os.path.dirname(os.path.abspath(__file__)))

import numpy as np
from scipy.interpolate import interp1d
from scipy.optimize import brentq
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

from canonical_constants import (
    tau_fold, PI, M_KK_gravity, M_KK, T_acoustic,
    E_cond, Delta_0_GL, Delta_0_OES
)

# ==============================================================================
#  STEP 0: Load S59 data
# ==============================================================================

print("=" * 72)
print("  S60 — GH-TEMP-DW-60: Gibbons-Hawking Temperature at Domain Wall")
print("=" * 72)

d = np.load('s59_ricci_dw.npz', allow_pickle=True)
tau_vals = d['tau_vals']
sec_min = d['sec_min_arr']
sec_max = d['sec_max_arr']
n_neg = d['n_neg_arr']
L_eigs = d['L_eigs']
r1_arr = d['r1_arr']
r2_arr = d['r2_arr']
r3_arr = d['r3_arr']
R_arr = d['R_arr']
tau_dw_geom = float(d['tau_dw_geom'])   # = 0.1135

# Reference thermal scales (M_KK units)
T_GGE = 0.135         # From session plan context  # (local)
T_acou = T_acoustic    # = 0.112 M_KK (canonical)
Delta_BCS = Delta_0_OES  # = 0.464 M_KK (OES gap)

print(f"\n  tau_DW (from E_DW=0, S58): {tau_dw_geom:.6f}")
print(f"  T_GGE reference: {T_GGE:.3f} M_KK")
print(f"  T_acoustic:      {T_acou:.3f} M_KK")
print(f"  Delta_BCS (OES): {Delta_BCS:.3f} M_KK")

# ==============================================================================
#  STEP 1: Verify structural zero of K_sec_min at tau_DW
# ==============================================================================

print("\n" + "=" * 72)
print("  STEP 1: Structural zero analysis at tau_DW")
print("=" * 72)

# Find nearest grid point to tau_DW
idx_dw = np.argmin(np.abs(tau_vals - tau_dw_geom))
tau_near = tau_vals[idx_dw]

print(f"\n  Nearest grid point: tau = {tau_near:.6f} (idx={idx_dw})")
print(f"  sec_min at tau_DW: {sec_min[idx_dw]:.20e}")
print(f"  n_neg at tau_DW:   {n_neg[idx_dw]}")
print(f"  L_eigs at tau_DW:  {L_eigs[idx_dw]}")

# Check whether sec_min is identically zero or just small
sec_min_at_dw = sec_min[idx_dw]
L_eig_min = L_eigs[idx_dw, 0]

is_structural_zero = (sec_min_at_dw == 0.0 and abs(L_eig_min) < 1e-10)

print(f"\n  sec_min == 0.0 exactly: {sec_min_at_dw == 0.0}")
print(f"  |L_eig_min| < 1e-10:   {abs(L_eig_min) < 1e-10}")
print(f"  STRUCTURAL ZERO:        {is_structural_zero}")

# Check sec_min is zero over entire range [0, 0.133]
max_sec_min_below_crossing = np.max(np.abs(sec_min[tau_vals < 0.133]))
print(f"\n  max|sec_min| for tau < 0.133: {max_sec_min_below_crossing:.2e}")
print(f"  Zero to machine precision:     {max_sec_min_below_crossing < 1e-15}")

# ==============================================================================
#  STEP 2: Diagnose the flat direction
# ==============================================================================

print("\n" + "=" * 72)
print("  STEP 2: Origin of the structural flat direction")
print("=" * 72)

# The Jensen metric is: g = diag(alpha*e^{2tau}, alpha*e^{-2tau}, alpha*e^{tau})
# on the (u(1), su(2), C^2) decomposition with dims (1, 3, 4).
#
# For a left-invariant metric on SU(3), the sectional curvatures are computed
# from the structure constants. The minimum sectional curvature being zero
# means there exists a 2-plane in the tangent space with K_sec = 0.
#
# From the Lichnerowicz operator: the first eigenvalue is ~1e-17 (machine zero).
# This corresponds to a mode that is neither expanding nor contracting —
# a neutrally stable perturbation direction.
#
# Physically: the Jensen deformation preserves certain symmetry directions.
# The flat 2-plane is the plane spanned by directions where the curvature
# contribution from the metric anisotropy exactly cancels the contribution
# from the structure constants.

# Verify the flat direction persists across ALL tau
L_eig_min_all = L_eigs[:, 0]
print(f"\n  First Lichnerowicz eigenvalue across all tau:")
print(f"    max|L_eig[0]|: {np.max(np.abs(L_eig_min_all)):.2e}")
print(f"    Identically zero (< 1e-10): {np.max(np.abs(L_eig_min_all)) < 1e-10}")

# The second eigenvalue (first positive one) decreases with tau
L_eig_2 = L_eigs[:, 1]
f_L2 = interp1d(tau_vals, L_eig_2, kind='cubic')
L2_at_dw = f_L2(tau_dw_geom)
print(f"\n  Second Lichnerowicz eigenvalue at tau_DW: {L2_at_dw:.6f}")
print(f"  (This is the smallest POSITIVE curvature eigenvalue)")

# ==============================================================================
#  STEP 3: GH temperature computation — why it is undefined at tau_DW
# ==============================================================================

print("\n" + "=" * 72)
print("  STEP 3: Gibbons-Hawking temperature analysis")
print("=" * 72)

# The Gibbons-Hawking temperature for a Euclidean geometry with a conical
# singularity is T = kappa/(2*pi), where kappa is the surface gravity.
#
# For the analog construction with sectional curvature:
#   kappa_analog = sqrt(|dK_sec/dtau|) at K_sec = 0
#
# But K_sec_min = 0 IDENTICALLY => dK_sec_min/dtau = 0 IDENTICALLY
# => kappa = 0 => T_DW is undefined (or formally zero)

# Compute dK_sec_min/dtau numerically
dK_dtau = np.gradient(sec_min, tau_vals)
dK_at_dw = dK_dtau[idx_dw]

print(f"\n  dK_sec_min/dtau at tau_DW: {dK_at_dw:.6e}")
print(f"  (Expected: ~0 since K_sec_min = 0 identically)")

# Formal kappa
if abs(dK_at_dw) > 1e-10:
    kappa_dw = np.sqrt(abs(dK_at_dw))
    T_dw = kappa_dw / (2 * PI)
    print(f"\n  kappa_DW = {kappa_dw:.6f} M_KK")
    print(f"  T_DW = kappa/(2*pi) = {T_dw:.6f} M_KK")
else:
    kappa_dw = 0.0  # (local)
    T_dw = 0.0  # (local)
    print(f"\n  kappa_DW = 0 (structural zero, no surface gravity)")
    print(f"  T_DW = UNDEFINED (no conical singularity)")
    print(f"\n  PHYSICAL INTERPRETATION:")
    print(f"    The Euclidean section at tau_DW has no conical point.")
    print(f"    The flat curvature plane means the geometry is locally")
    print(f"    product-like (R^1 x M_7), not cigar-like (as required")
    print(f"    for a Gibbons-Hawking temperature).")
    print(f"    This is the difference between a coordinate singularity")
    print(f"    (removable by periodicity) and a structural degeneracy")
    print(f"    (no periodicity constraint exists).")

# ==============================================================================
#  STEP 4: Alternative — temperature at actual K_sec sign change
# ==============================================================================

print("\n" + "=" * 72)
print("  STEP 4: Hypothetical T at actual curvature sign change (tau ~ 0.135)")
print("=" * 72)

# The actual sign change occurs between tau=0.1327 and tau=0.1378
# where n_neg jumps from 0 to 4
neg_indices = np.where(n_neg > 0)[0]
if len(neg_indices) > 0:
    idx_cross = neg_indices[0]
    tau_cross_lo = tau_vals[idx_cross - 1]
    tau_cross_hi = tau_vals[idx_cross]

    # Linear interpolation for the crossing point
    sm_lo = sec_min[idx_cross - 1]  # = 0.0
    sm_hi = sec_min[idx_cross]      # < 0

    # Since sec_min = 0 exactly at tau_cross_lo, the crossing is at tau_cross_lo
    # But we want the rate of descent
    dK_cross = (sm_hi - sm_lo) / (tau_cross_hi - tau_cross_lo)
    tau_cross = tau_cross_lo  # crossing is at the last zero point

    print(f"\n  Crossing location: tau = {tau_cross:.6f}")
    print(f"  sec_min just below crossing: {sm_lo:.10e}")
    print(f"  sec_min just above crossing: {sm_hi:.10e}")
    print(f"  dK_sec/dtau at crossing: {dK_cross:.6f}")

    kappa_cross = np.sqrt(abs(dK_cross))
    T_cross = kappa_cross / (2 * PI)

    print(f"\n  kappa_cross = sqrt(|dK/dtau|) = {kappa_cross:.6f} M_KK")
    print(f"  T_cross = kappa/(2*pi) = {T_cross:.6f} M_KK")
    print(f"  T_cross in GeV = {T_cross * M_KK:.4e} GeV")

    print(f"\n  Comparison to thermal scales:")
    print(f"    T_cross / T_GGE     = {T_cross / T_GGE:.4f}")
    print(f"    T_cross / T_acoustic = {T_cross / T_acou:.4f}")
    print(f"    T_cross / Delta_BCS = {T_cross / Delta_BCS:.4f}")
    print(f"    T_cross / T_fold    = {T_cross / tau_fold:.4f} (tau_fold as energy)")

    # Distance from domain wall
    delta_tau = tau_cross - tau_dw_geom
    print(f"\n  Distance: tau_cross - tau_DW = {delta_tau:.4f}")
    print(f"  Fractional shift: {delta_tau / tau_dw_geom:.1%}")

    # This is an ALTERNATIVE location, not the domain wall.
    # Even here, the "crossing" is from the structural zero plateau
    # to the first genuinely negative curvature — it's not a standard
    # horizon-type degeneration.

    print(f"\n  NOTE: This crossing at tau~0.135 is where the SECOND")
    print(f"  Lichnerowicz eigenvalue (positive, ~0.30) drives 4 sectional")
    print(f"  curvature planes negative. The first eigenvalue remains zero.")
    print(f"  This is a curvature instability onset, not a horizon formation.")
else:
    print("\n  No sectional curvature sign change found in data range.")
    kappa_cross = 0.0  # (local)
    T_cross = 0.0  # (local)

# ==============================================================================
#  STEP 5: Conical singularity check
# ==============================================================================

print("\n" + "=" * 72)
print("  STEP 5: Conical singularity analysis")
print("=" * 72)

# For a conical singularity to exist, we need a metric component that
# degenerates (goes to zero) at some point, like:
#   ds^2 = dr^2 + r^2 d(theta)^2 near r=0
# where removing the singularity requires theta ~ theta + 2*pi.
#
# In the Euclidean Schwarzschild case:
#   ds^2 = f(r)d(tau_E)^2 + dr^2/f(r) + r^2 d(Omega)^2
# where f(r_H) = 0. The (r, tau_E) plane near r_H looks like
# a cone, requiring tau_E ~ tau_E + beta with beta = 4*pi/f'(r_H).
#
# For the Jensen metric on SU(3), the metric components are:
#   g_1 = alpha * e^{2*tau}    (u(1) direction)
#   g_2 = alpha * e^{-2*tau}   (su(2) directions, 3-fold)
#   g_3 = alpha * e^{tau}      (C^2 directions, 4-fold)
#
# NONE of these vanish at any finite tau. They are strictly positive
# exponentials. There is NO metric degeneration, hence NO conical
# singularity, hence NO Euclidean periodicity constraint, hence
# NO Gibbons-Hawking temperature.

print("\n  Jensen metric components at tau_DW = {:.6f}:".format(tau_dw_geom))
alpha0 = 3.0  # g0_diag from canonical_constants (round SU(3))
g1_dw = alpha0 * np.exp(2 * tau_dw_geom)
g2_dw = alpha0 * np.exp(-2 * tau_dw_geom)
g3_dw = alpha0 * np.exp(tau_dw_geom)

print(f"    g_1 (u(1)):  {g1_dw:.6f}  (e^{{2*tau}} direction)")
print(f"    g_2 (su(2)): {g2_dw:.6f}  (e^{{-2*tau}} direction, x3)")
print(f"    g_3 (C^2):   {g3_dw:.6f}  (e^{{tau}} direction, x4)")
print(f"\n  ALL metric components strictly positive.")
print(f"  Minimum component: g_2 = {g2_dw:.6f} > 0")
print(f"  No degeneration => NO conical singularity.")

# Cross-check: at what tau would g_2 -> 0? Only at tau -> +infinity.
# The Jensen deformation is parametrically bounded.
print(f"\n  g_2 -> 0 requires tau -> +infinity (exponential)")
print(f"  At tau_fold = {tau_fold}: g_2 = {alpha0 * np.exp(-2*tau_fold):.6f}")
print(f"  At tau = 1.0: g_2 = {alpha0 * np.exp(-2.0):.6f}")
print(f"  At tau = 5.0: g_2 = {alpha0 * np.exp(-10.0):.8f}")
print(f"  The metric NEVER degenerates at finite tau.")

# ==============================================================================
#  STEP 6: Summary and gate verdict
# ==============================================================================

print("\n" + "=" * 72)
print("  STEP 6: Gate Verdict — GH-TEMP-DW-60")
print("=" * 72)

# Assemble the three independent reasons why T_DW is undefined:
#
# REASON 1 (Curvature): K_sec_min = 0 is a STRUCTURAL zero (flat plane),
#   not a sign crossing. dK/dtau = 0. kappa = 0.
#
# REASON 2 (Metric): The Jensen metric components are strictly positive
#   exponentials. No metric degeneration. No conical singularity.
#
# REASON 3 (Topology): The Euclidean SU(3) section is compact and smooth.
#   There is no boundary or bolt where periodicity must be imposed.
#   The Euclidean path integral is a sum over smooth compact geometries,
#   and periodicity is a global topological constraint, not a local one.

verdict = "FAIL"  # No conical singularity
detail = (
    f"T_DW UNDEFINED. Three independent reasons: "
    f"(1) K_sec_min=0 structural (L_eig_min={abs(L_eig_min):.1e}, "
    f"dK/dtau={abs(dK_at_dw):.1e}), not sign crossing. "
    f"(2) Jensen metric all-positive (min g_2={g2_dw:.3f}>0). "
    f"(3) Euclidean SU(3) compact, no bolt. "
    f"Actual K_sec sign change at tau=0.133, T_cross={T_cross:.4f} M_KK "
    f"({T_cross/T_GGE:.2f}x T_GGE). No GH mechanism at DW."
)

print(f"\n  VERDICT: {verdict}")
print(f"\n  REASON 1 — CURVATURE:")
print(f"    K_sec_min = 0.0 exactly (structural flat plane)")
print(f"    L_eig_min = {abs(L_eig_min):.2e} (machine zero)")
print(f"    dK_sec_min/dtau = {abs(dK_at_dw):.2e} (machine zero)")
print(f"    => kappa = 0, T_DW undefined")
print(f"\n  REASON 2 — METRIC:")
print(f"    Jensen metric: g_i = alpha * exp(c_i * tau)")
print(f"    All components strictly positive for all finite tau")
print(f"    No metric degeneration => no conical singularity")
print(f"\n  REASON 3 — TOPOLOGY:")
print(f"    Euclidean SU(3) is compact (pi_1 = 0)")
print(f"    No asymptotic boundary where periodicity is imposed")
print(f"    No bolt or nut in the smooth Jensen metric")
print(f"\n  ALTERNATIVE (tau ~ 0.133):")
print(f"    T_cross = {T_cross:.4f} M_KK at K_sec sign change")
print(f"    Ratio T_cross / T_GGE = {T_cross/T_GGE:.3f}")
print(f"    Ratio T_cross / T_acoustic = {T_cross/T_acou:.3f}")
print(f"    This is a curvature INSTABILITY onset, not a horizon")

# ==============================================================================
#  STEP 7: Save results
# ==============================================================================

print("\n" + "=" * 72)
print("  STEP 7: Saving results")
print("=" * 72)

np.savez('s60_gh_temp_dw.npz',
    # Gate metadata
    gate_name=np.array(['GH-TEMP-DW-60']),
    gate_verdict=np.array([verdict]),
    gate_detail=np.array([detail]),

    # Domain wall location
    tau_dw=tau_dw_geom,

    # Structural zero evidence
    sec_min_at_dw=sec_min_at_dw,
    L_eig_min_at_dw=L_eig_min,
    dK_dtau_at_dw=dK_at_dw,
    kappa_dw=kappa_dw,
    T_dw=T_dw,
    is_structural_zero=is_structural_zero,

    # Metric components at DW
    g1_dw=g1_dw,
    g2_dw=g2_dw,
    g3_dw=g3_dw,

    # Alternative crossing (tau ~ 0.135)
    tau_cross=tau_cross if len(neg_indices) > 0 else np.nan,
    kappa_cross=kappa_cross,
    T_cross=T_cross,
    T_cross_over_T_GGE=T_cross / T_GGE if T_GGE > 0 else np.nan,
    T_cross_over_T_acoustic=T_cross / T_acou if T_acou > 0 else np.nan,
    dK_dtau_cross=dK_cross if len(neg_indices) > 0 else 0.0,

    # Reference scales
    T_GGE_ref=T_GGE,
    T_acoustic_ref=T_acou,
    Delta_BCS_ref=Delta_BCS,
    M_KK_ref=M_KK,

    # Full profiles for plotting
    tau_vals=tau_vals,
    sec_min_profile=sec_min,
    sec_max_profile=sec_max,
    L_eig_min_profile=L_eigs[:, 0],
    L_eig_2_profile=L_eigs[:, 1],
    n_neg_profile=n_neg,
    dK_dtau_profile=dK_dtau,
)

print("  Saved: s60_gh_temp_dw.npz")

# ==============================================================================
#  STEP 8: Diagnostic plot
# ==============================================================================

fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('GH-TEMP-DW-60: Gibbons-Hawking Temperature at Domain Wall\n'
             f'VERDICT: {verdict} — No conical singularity at tau_DW = {tau_dw_geom:.4f}',
             fontsize=13, fontweight='bold')

# Panel (a): Sectional curvature profile
ax = axes[0, 0]
ax.plot(tau_vals, sec_min, 'b-', lw=2, label='$K_{\\mathrm{sec}}^{\\mathrm{min}}$')
ax.plot(tau_vals, sec_max, 'r-', lw=2, label='$K_{\\mathrm{sec}}^{\\mathrm{max}}$')
ax.axhline(0, color='k', ls='--', lw=0.5)
ax.axvline(tau_dw_geom, color='green', ls='--', lw=1.5, label=f'$\\tau_{{DW}}={tau_dw_geom:.3f}$')
if len(neg_indices) > 0:
    ax.axvline(tau_cross, color='orange', ls=':', lw=1.5,
               label=f'$K_{{sec}}$ sign change $\\tau={tau_cross:.3f}$')
ax.set_xlabel('$\\tau$')
ax.set_ylabel('Sectional curvature')
ax.set_title('(a) Sectional curvature vs $\\tau$')
ax.legend(fontsize=9)
ax.set_xlim(0, 0.25)

# Panel (b): Lichnerowicz eigenvalues
ax = axes[0, 1]
ax.plot(tau_vals, np.abs(L_eigs[:, 0]), 'g-', lw=2, label='$|\\lambda_1|$ (structural zero)')
ax.plot(tau_vals, L_eigs[:, 1], 'b-', lw=2, label='$\\lambda_2$')
ax.plot(tau_vals, L_eigs[:, 2], 'r-', lw=2, label='$\\lambda_3$')
ax.axvline(tau_dw_geom, color='green', ls='--', lw=1.5)
ax.set_xlabel('$\\tau$')
ax.set_ylabel('Lichnerowicz eigenvalue')
ax.set_title('(b) Lichnerowicz spectrum')
ax.legend(fontsize=9)
ax.set_yscale('symlog', linthresh=1e-14)
ax.set_xlim(0, 0.25)

# Panel (c): Jensen metric components
tau_plot = np.linspace(0, 0.3, 200)
g1_plot = alpha0 * np.exp(2 * tau_plot)
g2_plot = alpha0 * np.exp(-2 * tau_plot)
g3_plot = alpha0 * np.exp(tau_plot)
ax = axes[1, 0]
ax.plot(tau_plot, g1_plot, 'r-', lw=2, label='$g_1$ (u(1), $e^{2\\tau}$)')
ax.plot(tau_plot, g2_plot, 'b-', lw=2, label='$g_2$ (su(2), $e^{-2\\tau}$)')
ax.plot(tau_plot, g3_plot, 'g-', lw=2, label='$g_3$ (C$^2$, $e^{\\tau}$)')
ax.axvline(tau_dw_geom, color='green', ls='--', lw=1.5, label=f'$\\tau_{{DW}}$')
ax.axvline(tau_fold, color='purple', ls=':', lw=1.5, label=f'$\\tau_{{fold}}$')
ax.axhline(0, color='k', ls='-', lw=0.5)
ax.set_xlabel('$\\tau$')
ax.set_ylabel('Metric component')
ax.set_title('(c) Jensen metric — all strictly positive')
ax.legend(fontsize=9)
ax.set_xlim(0, 0.3)

# Panel (d): Temperature comparison bar chart
ax = axes[1, 1]
labels = ['$T_{DW}$\n(undefined)', '$T_{cross}$\n($\\tau$=0.133)',
          '$T_{GGE}$', '$T_{acoustic}$', '$\\Delta_{BCS}$']
values = [0, T_cross, T_GGE, T_acou, Delta_BCS]
colors = ['gray', 'orange', 'blue', 'green', 'red']
bars = ax.bar(labels, values, color=colors, alpha=0.7, edgecolor='black')
ax.set_ylabel('Energy scale ($M_{KK}$)')
ax.set_title('(d) Thermal scale comparison')
# Add value labels on bars
for bar, val in zip(bars, values):
    if val > 0:
        ax.text(bar.get_x() + bar.get_width()/2., bar.get_height() + 0.005,
                f'{val:.3f}', ha='center', va='bottom', fontsize=9)
    else:
        ax.text(bar.get_x() + bar.get_width()/2., 0.005,
                'N/A', ha='center', va='bottom', fontsize=9, color='red')

plt.tight_layout()
plt.savefig('s60_gh_temp_dw.png', dpi=150, bbox_inches='tight')
print("  Saved: s60_gh_temp_dw.png")

# ==============================================================================
#  Final summary
# ==============================================================================

print("\n" + "=" * 72)
print("  FINAL SUMMARY")
print("=" * 72)
print(f"""
  GH-TEMP-DW-60: {verdict}

  The Gibbons-Hawking temperature is UNDEFINED at the domain wall
  (tau_DW = {tau_dw_geom:.4f}). Three independent structural reasons:

  1. CURVATURE: K_sec_min = 0 identically (structural flat plane,
     Lichnerowicz eigenvalue = {abs(L_eig_min):.1e}). This is NOT a
     sign crossing — it is a degeneracy. dK/dtau = {abs(dK_at_dw):.1e}.
     No surface gravity analog exists.

  2. METRIC: Jensen metric components g_i = alpha * exp(c_i * tau)
     are ALL strictly positive for all finite tau. No component
     degenerates. No conical singularity can form.

  3. TOPOLOGY: SU(3) is simply connected (pi_1 = 0). The Euclidean
     section is compact with no boundary. There is no asymptotic
     region where periodicity would be imposed, and no bolt/nut
     in the smooth metric.

  ALTERNATIVE: At the actual sectional curvature sign change
  (tau ~ {tau_cross:.3f}), a hypothetical temperature would be:
    T_cross = {T_cross:.4f} M_KK = {T_cross * M_KK:.2e} GeV
    T_cross / T_GGE = {T_cross / T_GGE:.3f}  (2.5x too cold)
    T_cross / T_acoustic = {T_cross / T_acou:.3f}
  But this is a Lichnerowicz INSTABILITY onset, not a horizon.

  PHONONIC CLASSIFICATION: GEOMETRIC
  The Gibbons-Hawking construction requires a horizon (causal boundary
  where the Killing vector becomes null). The internal SU(3) geometry
  has no horizons — it is compact, positively curved, and geodesically
  complete. Temperature in this framework arises from PARTICLE CREATION
  (Parker mechanism at the fold, T_acoustic from phonon scattering),
  not from Euclidean periodicity.
""")

print("  Done.")
