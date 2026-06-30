#!/usr/bin/env python3
"""
Z-EQ-CHECK-66: Matter-Radiation Equality from Framework Parameters
===================================================================

Gate: Z-EQ-CHECK-66
  PASS: z_eq consistent with Planck 3402 +/- 26 (< 3 sigma)
  FAIL: z_eq deviates > 3 sigma from Planck
  INFO: z_eq off but consistent with known Omega_DM h^2 overprediction

Two scenarios:
  1. Full DM: Omega_DM h^2 = 0.400 (S65 all quasiparticles)
  2. Leggett-only: Omega_DM h^2 = 0.120 (W4-D, Leggett channel only)

Physics:
  z_eq = Omega_m / Omega_r - 1
  where Omega_m = Omega_b + Omega_DM, Omega_r from Planck 2018.
  CMB first peak shift: delta_l_1 ~ sqrt(z_eq^{fwk} / z_eq^{obs}) * l_1^{obs}

Author: mack-cosmic-bridge (S66)
"""

import numpy as np
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    H_0_km_s_Mpc,
    Omega_r,
    Omega_b,
    Omega_m,
    Omega_DM,
)

# ============================================================================
# Planck 2018 reference values
# ============================================================================
h = H_0_km_s_Mpc / 100.0  # dimensionless Hubble parameter

# Planck 2018 z_eq (Table 2, base LCDM, TT,TE,EE+lowE+lensing)
z_eq_planck = 3402.0  # (local)
z_eq_planck_err = 26.0  # 1-sigma  # (local)

# CMB first acoustic peak (Planck 2018 observed)
l_1_obs = 220.0  # multipole of first peak (approximate)  # (local)

# Omega_b h^2 from Planck 2018
Omega_b_h2_planck = 0.02237  # Planck 2018 TT,TE,EE+lowE+lensing  # (local)
# Framework uses same baryons as Planck (no independent prediction)
Omega_b_h2_fwk = Omega_b * h**2  # = 0.0493 * 0.674^2

print("=" * 72)
print("Z-EQ-CHECK-66: Matter-Radiation Equality from Framework Parameters")
print("=" * 72)

# ============================================================================
# Scenario 0: Planck LCDM baseline (self-consistency check)
# ============================================================================
print("\n--- Scenario 0: Planck LCDM Baseline ---")
Omega_m_planck = Omega_m  # 0.315 from canonical_constants
z_eq_planck_calc = Omega_m_planck / Omega_r - 1.0

print(f"  Omega_m (Planck)     = {Omega_m_planck:.4f}")
print(f"  Omega_r (Planck)     = {Omega_r:.6e}")
print(f"  z_eq (calculated)    = {z_eq_planck_calc:.1f}")
print(f"  z_eq (Planck table)  = {z_eq_planck:.1f} +/- {z_eq_planck_err:.1f}")
delta_sigma_0 = abs(z_eq_planck_calc - z_eq_planck) / z_eq_planck_err
print(f"  Deviation            = {z_eq_planck_calc - z_eq_planck:.1f} = {delta_sigma_0:.2f} sigma")
print(f"  [Self-consistency: Omega_m/Omega_r - 1 vs tabulated z_eq]")

# ============================================================================
# Scenario 1: Full DM (all GGE quasiparticles)
# ============================================================================
print("\n--- Scenario 1: Full DM (Omega_DM h^2 = 0.400) ---")
Omega_DM_h2_full = 0.400  # S65 total quasiparticle abundance  # (local)
Omega_DM_full = Omega_DM_h2_full / h**2
Omega_m_full = Omega_b + Omega_DM_full
z_eq_full = Omega_m_full / Omega_r - 1.0

delta_z_full = z_eq_full - z_eq_planck
sigma_full = abs(delta_z_full) / z_eq_planck_err

print(f"  h                    = {h:.3f}")
print(f"  Omega_DM h^2 (fwk)  = {Omega_DM_h2_full:.3f}")
print(f"  Omega_DM             = {Omega_DM_full:.4f}")
print(f"  Omega_b              = {Omega_b:.4f}")
print(f"  Omega_m (fwk)        = {Omega_m_full:.4f}")
print(f"  Omega_r              = {Omega_r:.6e}")
print(f"  z_eq (full DM)       = {z_eq_full:.1f}")
print(f"  z_eq (Planck)        = {z_eq_planck:.1f} +/- {z_eq_planck_err:.1f}")
print(f"  Deviation            = {delta_z_full:.1f} = {sigma_full:.2f} sigma")

# CMB first peak shift
l_1_full = np.sqrt(z_eq_full / z_eq_planck) * l_1_obs
delta_l_full = l_1_full - l_1_obs
print(f"  l_1 (shifted)        = {l_1_full:.1f}")
print(f"  delta_l_1            = {delta_l_full:+.1f} (observed: {l_1_obs:.0f})")

# ============================================================================
# Scenario 2: Leggett-only DM
# ============================================================================
print("\n--- Scenario 2: Leggett-only DM (Omega_DM h^2 = 0.120) ---")
Omega_DM_h2_leggett = 0.120  # W4-D Leggett-only result  # (local)
Omega_DM_leggett = Omega_DM_h2_leggett / h**2
Omega_m_leggett = Omega_b + Omega_DM_leggett
z_eq_leggett = Omega_m_leggett / Omega_r - 1.0

delta_z_leggett = z_eq_leggett - z_eq_planck
sigma_leggett = abs(delta_z_leggett) / z_eq_planck_err

print(f"  Omega_DM h^2 (fwk)  = {Omega_DM_h2_leggett:.3f}")
print(f"  Omega_DM             = {Omega_DM_leggett:.4f}")
print(f"  Omega_b              = {Omega_b:.4f}")
print(f"  Omega_m (fwk)        = {Omega_m_leggett:.4f}")
print(f"  Omega_r              = {Omega_r:.6e}")
print(f"  z_eq (Leggett-only)  = {z_eq_leggett:.1f}")
print(f"  z_eq (Planck)        = {z_eq_planck:.1f} +/- {z_eq_planck_err:.1f}")
print(f"  Deviation            = {delta_z_leggett:.1f} = {sigma_leggett:.2f} sigma")

# CMB first peak shift
l_1_leggett = np.sqrt(z_eq_leggett / z_eq_planck) * l_1_obs
delta_l_leggett = l_1_leggett - l_1_obs
print(f"  l_1 (shifted)        = {l_1_leggett:.1f}")
print(f"  delta_l_1            = {delta_l_leggett:+.1f} (observed: {l_1_obs:.0f})")

# ============================================================================
# Detailed diagnostic: Omega_DM h^2 back-calculation from z_eq
# ============================================================================
print("\n--- Diagnostic: What Omega_DM h^2 reproduces z_eq = 3402? ---")
# z_eq + 1 = Omega_m / Omega_r => Omega_m = (z_eq + 1) * Omega_r
Omega_m_from_zeq = (z_eq_planck + 1) * Omega_r
Omega_DM_from_zeq = Omega_m_from_zeq - Omega_b
Omega_DM_h2_from_zeq = Omega_DM_from_zeq * h**2

print(f"  Omega_m required     = {Omega_m_from_zeq:.5f}")
print(f"  Omega_DM required    = {Omega_DM_from_zeq:.5f}")
print(f"  Omega_DM h^2 needed  = {Omega_DM_h2_from_zeq:.5f}")
print(f"  Planck Omega_DM h^2  = {Omega_DM * h**2:.5f}")
print(f"  Full DM Omega_DM h^2 = {Omega_DM_h2_full:.3f} (ratio: {Omega_DM_h2_full / Omega_DM_h2_from_zeq:.2f}x)")
print(f"  Leggett Omega_DM h^2 = {Omega_DM_h2_leggett:.3f} (ratio: {Omega_DM_h2_leggett / Omega_DM_h2_from_zeq:.2f}x)")

# ============================================================================
# Gate verdict
# ============================================================================
print("\n" + "=" * 72)
print("GATE VERDICTS")
print("=" * 72)

# Full DM scenario
if sigma_full <= 3.0:
    verdict_full = "PASS"
elif sigma_full > 3.0:
    verdict_full = "FAIL"
print(f"\n  Full DM (Omega_DM h^2 = 0.400):")
print(f"    z_eq = {z_eq_full:.1f}, deviation = {sigma_full:.2f} sigma")
print(f"    Verdict: {verdict_full}")
if verdict_full == "FAIL":
    print(f"    CMB first peak at l ~ {l_1_full:.0f} vs observed 220")
    print(f"    Peak shift {delta_l_full:+.0f} would be catastrophically excluded by Planck")

# Leggett-only scenario
if sigma_leggett <= 3.0:
    verdict_leggett = "PASS"
elif sigma_leggett > 3.0:
    verdict_leggett = "FAIL"
print(f"\n  Leggett-only (Omega_DM h^2 = 0.120):")
print(f"    z_eq = {z_eq_leggett:.1f}, deviation = {sigma_leggett:.2f} sigma")
print(f"    Verdict: {verdict_leggett}")
if abs(delta_l_leggett) < 5:
    print(f"    CMB first peak shift {delta_l_leggett:+.1f} -- negligible")

# Combined gate verdict
print(f"\n  Combined Z-EQ-CHECK-66 verdict:")
if verdict_full == "FAIL" and verdict_leggett == "PASS":
    print(f"    Full DM: FAIL ({sigma_full:.1f} sigma)")
    print(f"    Leggett-only: PASS ({sigma_leggett:.1f} sigma)")
    print(f"    This CONFIRMS the W4-D finding: BA phonons must NOT contribute to DM.")
    print(f"    Only Leggett channel preserves CMB peak structure.")
    combined_verdict = "INFO"
elif verdict_full == "PASS" and verdict_leggett == "PASS":
    combined_verdict = "PASS"
    print(f"    Both scenarios pass. Full DM: {sigma_full:.1f} sigma. Leggett-only: {sigma_leggett:.1f} sigma.")
elif verdict_full == "FAIL" and verdict_leggett == "FAIL":
    combined_verdict = "FAIL"
    print(f"    Both scenarios fail. Framework DM abundance excluded.")
else:
    combined_verdict = "INFO"
    print(f"    Mixed result.")

print(f"\n  GATE Z-EQ-CHECK-66: {combined_verdict}")

# ============================================================================
# Save results
# ============================================================================
outfile = os.path.join(os.path.dirname(os.path.abspath(__file__)), "s66_z_eq_check.npz")
np.savez(
    outfile,
    # Planck reference
    z_eq_planck=z_eq_planck,
    z_eq_planck_err=z_eq_planck_err,
    z_eq_planck_calc=z_eq_planck_calc,
    Omega_r=Omega_r,
    Omega_m_planck=Omega_m_planck,
    h=h,
    l_1_obs=l_1_obs,
    # Full DM scenario
    Omega_DM_h2_full=Omega_DM_h2_full,
    Omega_DM_full=Omega_DM_full,
    Omega_m_full=Omega_m_full,
    z_eq_full=z_eq_full,
    sigma_full=sigma_full,
    l_1_full=l_1_full,
    delta_l_full=delta_l_full,
    verdict_full=verdict_full,
    # Leggett-only scenario
    Omega_DM_h2_leggett=Omega_DM_h2_leggett,
    Omega_DM_leggett=Omega_DM_leggett,
    Omega_m_leggett=Omega_m_leggett,
    z_eq_leggett=z_eq_leggett,
    sigma_leggett=sigma_leggett,
    l_1_leggett=l_1_leggett,
    delta_l_leggett=delta_l_leggett,
    verdict_leggett=verdict_leggett,
    # Diagnostic
    Omega_DM_h2_from_zeq=Omega_DM_h2_from_zeq,
    # Combined
    combined_verdict=combined_verdict,
)
print(f"\nSaved: {outfile}")
print("=" * 72)
