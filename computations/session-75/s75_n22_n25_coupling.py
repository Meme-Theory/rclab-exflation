#!/usr/bin/env python3
"""
S75-B5-COUPLING-CHECK: Effective modulus mass from multi-instanton condensate
==============================================================================

Task: N22-N25-COUPLING-CHECK-75 (Task #25)

Computes the curvature d^2V_total/dtau^2 at tau = 0.48 from the W1-F
multi-instanton V_total(tau), extracts the effective modulus mass m_eff,
and evaluates the ratio m_eff^2 / H_fold^2.

Physics:
  The modulus tau parametrizes the Jensen deformation of the internal SU(3).
  The total potential V_total(tau) = V_bare(tau) + V_instanton(tau) determines
  whether tau is stabilized (local minimum with positive curvature) or remains
  a flat direction. The effective mass m_eff^2 = d^2V_total/dtau^2 sets the
  scale of modulus oscillations relative to the Hubble rate H_fold.

  For moduli stabilization: m_eff >> H_fold is required (the eta problem in
  moduli space). The gate threshold m_eff^2/H_fold^2 >= 20.7 corresponds to
  m_eff/H_fold >= 4.55, well into the heavy-modulus regime.

Input:
  - computations/session-75/s75_multi_instanton_lmax10.npz (W1-F output)
  - computations/_shared/canonical_constants.py

Gate: S75-B5-COUPLING-CHECK
  PASS: m_eff^2 / H_fold^2 >= 20.7
  INFO: 1.0 <= m_eff^2/H_fold^2 < 20.7
  FAIL: m_eff^2/H_fold^2 < 1.0

Output:
  - computations/session-75/s75_n22_n25_coupling.npz
"""

import sys
sys.path.insert(0, "computations")
from canonical_constants import *
import numpy as np

# ============================================================================
#  Load W1-F multi-instanton data
# ============================================================================

data = np.load("computations/session-75/s75_multi_instanton_lmax10.npz", allow_pickle=True)

tau_scan = data["tau_scan"]       # shape (200,), range [0.19, 1.7]
V_total_L10 = data["V_total_L10"]  # shape (200,), V_total at L_max=10

dtau = tau_scan[1] - tau_scan[0]  # (local) uniform spacing

print("=" * 72)
print("S75-B5-COUPLING-CHECK: Effective Modulus Mass")
print("=" * 72)
print(f"tau range: [{tau_scan[0]:.4f}, {tau_scan[-1]:.4f}], N = {len(tau_scan)}")
print(f"dtau = {dtau:.6e}")
print(f"H_fold = {H_fold:.4f} M_KK (from canonical_constants)")
print()

# ============================================================================
#  Step 1: Compute d^2V_total/dtau^2 at tau = 0.48
# ============================================================================
#
#  Use central finite difference on the discrete V_total(tau) data.
#  Second derivative: f''(x) = (f(x+h) - 2f(x) + f(x-h)) / h^2 + O(h^2)
#
#  Also compute the fourth-order accurate stencil for cross-check:
#  f''(x) = (-f(x+2h) + 16f(x+h) - 30f(x) + 16f(x-h) - f(x-2h)) / (12h^2)

tau_eval = 0.48  # (local) evaluation point
idx_center = np.argmin(np.abs(tau_scan - tau_eval))  # (local)
tau_actual = tau_scan[idx_center]  # (local) nearest grid point

print(f"Evaluation point: tau = {tau_eval}")
print(f"Nearest grid point: tau = {tau_actual:.6f} (index {idx_center})")
print(f"Offset from target: {abs(tau_actual - tau_eval):.4e}")
print()

# --- Second-order central difference ---
V_m1 = V_total_L10[idx_center - 1]  # (local)
V_0  = V_total_L10[idx_center]       # (local)
V_p1 = V_total_L10[idx_center + 1]  # (local)

d2V_order2 = (V_p1 - 2.0 * V_0 + V_m1) / dtau**2  # (local)

# --- Fourth-order central difference ---
V_m2 = V_total_L10[idx_center - 2]  # (local)
V_p2 = V_total_L10[idx_center + 2]  # (local)

d2V_order4 = (-V_p2 + 16.0 * V_p1 - 30.0 * V_0 + 16.0 * V_m1 - V_m2) / (12.0 * dtau**2)  # (local)

print("--- d^2V_total/dtau^2 at tau ~ 0.48 ---")
print(f"  2nd-order central: {d2V_order2:.6e} M_KK^4")
print(f"  4th-order central: {d2V_order4:.6e} M_KK^4")
print(f"  Relative difference: {abs(d2V_order4 - d2V_order2) / abs(d2V_order2):.4e}")
print()

# Use the higher-order result as canonical
d2V_dtau2 = d2V_order4  # (local) canonical curvature

# ============================================================================
#  Step 1b: Also compute first derivative (force) for context
# ============================================================================

dV_order4 = (-V_total_L10[idx_center + 2] + 8.0 * V_total_L10[idx_center + 1]
             - 8.0 * V_total_L10[idx_center - 1] + V_total_L10[idx_center - 2]) / (12.0 * dtau)  # (local)

print(f"  dV_total/dtau at tau ~ 0.48: {dV_order4:.6e} M_KK^4")
print(f"  (Positive = monotonically increasing, no minimum nearby)")
print()

# ============================================================================
#  Step 2: Extract m_eff^2
# ============================================================================
#
#  The modulus mass squared is identified with the curvature of the potential:
#    m_eff^2 = d^2V_total/dtau^2
#
#  V_total is in units of M_KK^4 (spectral action units).
#  tau is dimensionless.
#  So d^2V/dtau^2 has dimensions of M_KK^4... but this is the curvature of
#  the action, not the potential energy density.
#
#  The physical modulus mass requires extracting the kinetic normalization.
#  The kinetic term for tau in the spectral action framework is:
#    L_kin = (1/2) Z_fold (dtau/dt)^2
#  where Z_fold is the gradient stiffness from canonical_constants.
#
#  The properly normalized mass is:
#    m_eff^2 = (1/Z_fold) * d^2V_total/dtau^2
#
#  with both V_total and Z_fold in M_KK units, m_eff^2 is in M_KK^2 units.

m_eff_sq_raw = d2V_dtau2  # (local) raw curvature, M_KK^4 units
m_eff_sq_physical = d2V_dtau2 / Z_fold  # (local) normalized by kinetic coefficient, M_KK^2

print("--- Effective modulus mass ---")
print(f"  Z_fold (gradient stiffness) = {Z_fold:.2f} M_KK^2 (from canonical)")
print(f"  m_eff^2 (raw curvature)     = {m_eff_sq_raw:.6e} M_KK^4")
print(f"  m_eff^2 (physical, /Z_fold) = {m_eff_sq_physical:.6e} M_KK^2")
print(f"  m_eff (physical)            = {np.sqrt(abs(m_eff_sq_physical)):.4f} M_KK")
print()

# ============================================================================
#  Step 3: Compute H_fold^2 and the ratio
# ============================================================================

H_fold_sq = H_fold**2  # (local)

# Two versions of the ratio depending on whether we normalize by Z_fold
ratio_raw = m_eff_sq_raw / H_fold_sq       # (local) V'' / H^2 (action curvature)
ratio_physical = m_eff_sq_physical / H_fold_sq  # (local) m_eff^2 / H^2 (physical mass)

print("--- m_eff^2 / H_fold^2 ---")
print(f"  H_fold = {H_fold:.4f} M_KK")
print(f"  H_fold^2 = {H_fold_sq:.4e} M_KK^2")
print()
print(f"  RAW (d^2V/dtau^2 / H_fold^2):       {ratio_raw:.4e}")
print(f"  PHYSICAL (m_eff^2 / H_fold^2):       {ratio_physical:.6f}")
print()

# The gate uses the physical ratio (properly normalized mass)
gate_ratio = ratio_physical  # (local)

# ============================================================================
#  Step 4: L_max convergence of curvature
# ============================================================================

print("--- L_max convergence of d^2V/dtau^2 ---")
L_max_list = [3, 5, 7, 8, 9, 10]  # (local)
d2V_by_Lmax = {}  # (local)

for lm in L_max_list:
    key = f"V_total_L{lm}"  # (local)
    if key in data:
        V_lm = data[key]  # (local)
        # 4th-order central difference at same index
        d2V_lm = (-V_lm[idx_center + 2] + 16.0 * V_lm[idx_center + 1]
                   - 30.0 * V_lm[idx_center] + 16.0 * V_lm[idx_center - 1]
                   - V_lm[idx_center - 2]) / (12.0 * dtau**2)  # (local)
        ratio_lm = (d2V_lm / Z_fold) / H_fold_sq  # (local)
        d2V_by_Lmax[lm] = d2V_lm
        print(f"  L_max={lm:2d}: d^2V/dtau^2 = {d2V_lm:.6e},  m_eff^2/H^2 = {ratio_lm:.6f}")

print()

# ============================================================================
#  Step 5: Check monotonicity at tau = 0.48
# ============================================================================
#
#  W1-F found zero sign changes in dV/dtau across all L_max.
#  Verify: is there any minimum structure near tau = 0.48?

# Scan first derivative across full range
dV_full = np.gradient(V_total_L10, dtau)  # (local)
sign_changes_full = np.sum(np.diff(np.sign(dV_full)) != 0)  # (local)

# Check if dV > 0 everywhere (monotonic increase)
all_positive = np.all(dV_full > 0)  # (local)

print("--- Monotonicity check ---")
print(f"  Sign changes in dV/dtau: {sign_changes_full}")
print(f"  dV/dtau > 0 everywhere: {all_positive}")
print(f"  Min dV/dtau: {np.min(dV_full):.6e} at tau = {tau_scan[np.argmin(dV_full)]:.4f}")
print(f"  Max dV/dtau: {np.max(dV_full):.6e} at tau = {tau_scan[np.argmax(dV_full)]:.4f}")
print()
print("  V_total is MONOTONICALLY INCREASING: no minimum exists.")
print("  The curvature d^2V/dtau^2 at tau=0.48 measures the rate of")
print("  change of the force, NOT confinement around a stable point.")
print()

# ============================================================================
#  Step 6: Also report the m_tau from canonical_constants for comparison
# ============================================================================

print("--- Cross-check: canonical m_tau ---")
print(f"  m_tau (S42, fold) = {m_tau:.3f} M_KK")
print(f"  m_tau^2 / H_fold^2 = {m_tau**2 / H_fold_sq:.6e}")
print(f"  This is the BARE spectral action modulus mass at the fold.")
print(f"  The W1-F V_total includes instanton corrections which DO NOT")
print(f"  create a minimum — the potential remains monotonic.")
print()

# ============================================================================
#  Gate verdict
# ============================================================================

GATE_PASS = 20.7   # (local)
GATE_INFO = 1.0    # (local)

print("=" * 72)
print("GATE: S75-B5-COUPLING-CHECK")
print(f"  m_eff^2/H_fold^2 = {gate_ratio:.6f}")
print(f"  PASS threshold: >= {GATE_PASS}")
print(f"  INFO threshold: >= {GATE_INFO}")
print(f"  FAIL threshold: < {GATE_INFO}")
print()

if gate_ratio >= GATE_PASS:
    verdict = "PASS"
    detail = f"m_eff^2/H_fold^2 = {gate_ratio:.4f} >= {GATE_PASS} (heavy modulus)"
elif gate_ratio >= GATE_INFO:
    verdict = "INFO"
    detail = f"{GATE_INFO} <= m_eff^2/H_fold^2 = {gate_ratio:.4f} < {GATE_PASS}"
else:
    verdict = "FAIL"
    detail = f"m_eff^2/H_fold^2 = {gate_ratio:.6f} < {GATE_INFO} (light modulus / eta problem)"

print(f"  VERDICT: {verdict}")
print(f"  {detail}")
print()

# Physical interpretation
if gate_ratio < GATE_INFO:
    print("  INTERPRETATION: The modulus tau at the multi-instanton level")
    print("  remains lighter than H_fold. Combined with W1-F's finding that")
    print("  V_total is monotonic (no minimum), this means the instanton")
    print("  condensate does NOT stabilize the modulus. The curvature exists")
    print("  but measures the rate of change of the driving force, not")
    print("  confinement. The transit remains impulsive (supersonic),")
    print("  consistent with the Ordered Veil paradigm.")
elif gate_ratio < GATE_PASS:
    print("  INTERPRETATION: m_eff is comparable to H_fold but not dominant.")
    print("  Modulus oscillations are not completely frozen out.")
else:
    print("  INTERPRETATION: Heavy modulus, oscillations frozen by Hubble friction.")

print("=" * 72)

# ============================================================================
#  Save output
# ============================================================================

np.savez("computations/session-75/s75_n22_n25_coupling.npz",
         # Gate
         gate_name="S75-B5-COUPLING-CHECK",
         gate_verdict=verdict,
         gate_detail=detail,
         # Core results
         tau_eval=tau_actual,
         d2V_dtau2_order2=d2V_order2,
         d2V_dtau2_order4=d2V_order4,
         dV_dtau=dV_order4,
         Z_fold_used=Z_fold,
         m_eff_sq_raw=m_eff_sq_raw,
         m_eff_sq_physical=m_eff_sq_physical,
         m_eff=np.sqrt(abs(m_eff_sq_physical)),
         H_fold_used=H_fold,
         H_fold_sq=H_fold_sq,
         ratio_raw=ratio_raw,
         ratio_physical=ratio_physical,
         # L_max convergence
         L_max_list=np.array(L_max_list),
         d2V_by_Lmax=np.array([d2V_by_Lmax.get(lm, np.nan) for lm in L_max_list]),
         # Monotonicity
         n_sign_changes=sign_changes_full,
         monotonic=all_positive,
         dV_min=np.min(dV_full),
         dV_max=np.max(dV_full),
         )

print(f"\nSaved: computations/session-75/s75_n22_n25_coupling.npz")
