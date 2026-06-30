#!/usr/bin/env python3
"""
s74_bcs_gap_k_scale.py -- BCS-GAP-K-SCALE-74 (W4-GG, Session 74 Wave 4)
================================================================================

BCS Gap Imprint k_BCS on LSS P(k).

Substrate framing
-----------------
The BCS gap Delta_BCS = 0.4643 M_KK (S70 canonical, BCS-GAP-CANONICAL-70) is a
characteristic energy scale of the substrate's BCS pairing structure at the
fold. It defines a corresponding k-scale via the Goldstone dispersion:

    omega_Gold = c_s * k     (acoustic branch of the fiber excitations)

setting omega_Gold = Delta_BCS gives

    k_BCS^nat = Delta_BCS / c_s   (in M_KK units, natural units hbar = c = 1)

This is the inverse coherence length in the Goldstone sound channel -- the
k-scale above which pair fluctuations are gapped out of the acoustic spectrum.
It is NOT a coherence length set by xi_BCS directly (which would use the
effective pair velocity inside the fiber); it is the projection of the gap onto
the c_s = c_Gold acoustic branch that propagates into the emergent metric.

In the substrate picture, this k-scale is frozen at the fold and then redshifts
with the expansion history. The BCS gap, being a rest energy of the pair
condensate, redshifts like any comoving mode: k_physical(today) =
k_physical(fold) * a_fold/a_today. The gap thus prints a characteristic scale
onto the post-transit linear P(k) -- a potential feature at k_BCS where the
spectrum could show a break, bump, or suppression relative to pure power law.

This is Framework section 10 deferred item #10. Independent and computable now
with canonical constants alone; no new eigenvalue sweeps required.

Computation
-----------
1. Natural-units k-scale:
    k_BCS_nat = Delta_BCS / c_Gold   (dimensionless, M_KK units)

2. Physical k-scale at the fold (in GeV):
    k_BCS_fold_GeV = k_BCS_nat * M_KK_gravity

3. Expansion ratio from fold to today (radiation-dominated approximation):
    a_fold / a_today = T_CMB / M_KK_gravity
   (this is the canonical S66 two-component closure; see s66_two_component.py
    which uses exactly this N_e_total = ln(M_KK / T_CMB) for the fold-to-today
    Friedmann integration)

4. Physical k today:
    k_BCS_today_GeV = k_BCS_fold_GeV * a_fold / a_today

5. Convert to Mpc^{-1}:
    k_BCS_today_Mpc = k_BCS_today_GeV * Mpc_to_GeV_inv   (= ... * 1.563e38)

Pre-registered gate  BCS-GAP-K-SCALE-74
---------------------------------------
  PASS: k_BCS computed AND k_BCS in [1e-4, 1] Mpc^{-1}
  INFO: k_BCS computed AND outside [1e-4, 1] Mpc^{-1}
  FAIL: k_BCS undefined / NaN / inf

Agent:    landau-condensed-matter-theorist
Session:  74 Wave 4 (W4-GG)
Task:     Framework section 10 deferred #10
"""
import os
import sys
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    Delta_BCS,          # 0.4642547394830737 M_KK (S70 canonical)
    c_Gold,             # 0.915 M_KK (Goldstone sound speed)
    M_KK_gravity,       # 7.428660036284456e16 GeV (S42 gravity route)
    T_CMB_GeV,          # 2.348e-13 GeV (COBE/FIRAS, 2.7255 K)
    Mpc_to_GeV_inv,     # 1.563e38 GeV^{-1} per Mpc
    GeV_inv_to_Mpc,     # 6.39e-39 Mpc per GeV^{-1}
    H_0_GeV,            # 1.438e-42 GeV (Hubble today)
)

print("=" * 78)
print("s74_bcs_gap_k_scale.py -- BCS-GAP-K-SCALE-74 (W4-GG)")
print("BCS Gap Imprint k_BCS on LSS P(k)")
print("=" * 78)

# =============================================================================
# Step 1. Natural-units k-scale  (M_KK units)
# =============================================================================
k_BCS_nat = Delta_BCS / c_Gold          # (local) dimensionless, M_KK units

print("\n--- Step 1: Natural units (M_KK) ---")
print(f"  Delta_BCS     = {Delta_BCS:.10f} M_KK   (S70 canonical BCS gap)")
print(f"  c_Gold        = {c_Gold:.6f} M_KK         (Goldstone sound speed)")
print(f"  k_BCS_nat     = Delta_BCS / c_Gold = {k_BCS_nat:.10f}  (M_KK units)")

# Consistency: since Delta = omega_Gold = c_s * k, k_BCS_nat has units of M_KK
# when c_Gold is in M_KK units and Delta in M_KK. Dimensionally consistent.

# =============================================================================
# Step 2. Physical k-scale at the fold (GeV)
# =============================================================================
k_BCS_fold_GeV = k_BCS_nat * M_KK_gravity   # (local) GeV

print("\n--- Step 2: Physical k at the fold ---")
print(f"  M_KK_gravity  = {M_KK_gravity:.6e} GeV")
print(f"  k_BCS_fold    = k_BCS_nat * M_KK = {k_BCS_fold_GeV:.6e} GeV")

# =============================================================================
# Step 3. Expansion history  (S66 canonical radiation redshift)
# =============================================================================
# Same convention as s66_two_component.py (line 355):
#     a_ratio_total = M_KK_gravity / T_CMB_GeV
#     N_e_total     = ln(a_ratio_total)
#
# We use the inverse: a_fold/a_today = 1/a_ratio_total = T_CMB / M_KK.
a_ratio_fold_over_today = T_CMB_GeV / M_KK_gravity   # (local) dimensionless
N_e_total_canonical = np.log(M_KK_gravity / T_CMB_GeV)  # (local) e-folds fold -> today

print("\n--- Step 3: Expansion history (S66 canonical) ---")
print(f"  T_CMB            = {T_CMB_GeV:.6e} GeV   (COBE/FIRAS, 2.7255 K)")
print(f"  a_today/a_fold   = M_KK/T_CMB = {1.0/a_ratio_fold_over_today:.6e}")
print(f"  a_fold/a_today   = T_CMB/M_KK = {a_ratio_fold_over_today:.6e}")
print(f"  N_e_total        = ln(M_KK/T_CMB) = {N_e_total_canonical:.4f}  (S66 canonical)")

# =============================================================================
# Step 4. Physical k today (redshift the comoving mode)
# =============================================================================
# k_physical redshifts as 1/a:  k_today = k_fold * (a_fold/a_today)
k_BCS_today_GeV = k_BCS_fold_GeV * a_ratio_fold_over_today   # (local) GeV

print("\n--- Step 4: Redshift to today ---")
print(f"  k_BCS_today  = k_BCS_fold * (a_fold/a_today)")
print(f"               = {k_BCS_fold_GeV:.6e} * {a_ratio_fold_over_today:.6e}")
print(f"               = {k_BCS_today_GeV:.6e} GeV")

# Cross-check: equivalently k_BCS_today_GeV = k_BCS_nat * T_CMB_GeV
#   because k_BCS_fold = k_BCS_nat * M_KK,  and  a_fold/a_today = T_CMB/M_KK
#   so the M_KK cancels: k_BCS_today_GeV = k_BCS_nat * T_CMB_GeV
k_BCS_today_GeV_check = k_BCS_nat * T_CMB_GeV   # (local) GeV
print(f"\n  Cross-check:  k_BCS_nat * T_CMB = {k_BCS_today_GeV_check:.6e} GeV")
print(f"  Difference    = {abs(k_BCS_today_GeV - k_BCS_today_GeV_check):.3e} GeV (should be 0)")

# =============================================================================
# Step 5. Convert to Mpc^{-1}
# =============================================================================
# 1 GeV = Mpc_to_GeV_inv / 1 Mpc^{-1}, i.e. k[Mpc^{-1}] = k[GeV] * Mpc_to_GeV_inv
k_BCS_today_Mpc = k_BCS_today_GeV * Mpc_to_GeV_inv   # (local) Mpc^{-1}

print("\n--- Step 5: Convert to Mpc^{-1} ---")
print(f"  Mpc_to_GeV_inv = {Mpc_to_GeV_inv:.4e} GeV^{{-1}} per Mpc")
print(f"  k_BCS_today    = {k_BCS_today_GeV:.6e} GeV * {Mpc_to_GeV_inv:.4e}")
print(f"  k_BCS_today    = {k_BCS_today_Mpc:.6e} Mpc^{{-1}}")

# =============================================================================
# Step 6. Dimensional cross-checks
# =============================================================================
print("\n--- Step 6: Dimensional cross-checks ---")

# Check 1: H_0 in Mpc^{-1} should be around 2.2e-4 Mpc^{-1}
H_0_Mpc = H_0_GeV * Mpc_to_GeV_inv   # (local) Mpc^{-1}
print(f"  H_0             = {H_0_GeV:.4e} GeV")
print(f"  H_0 / c (Mpc^-1)= {H_0_Mpc:.4e} Mpc^{{-1}}  (should be ~ 2.2e-4)")

# Check 2: Compare k_BCS to H_0 in Mpc^{-1}
ratio_kBCS_H0 = k_BCS_today_Mpc / H_0_Mpc   # (local)
log10_ratio = np.log10(ratio_kBCS_H0)       # (local)
print(f"  k_BCS / (H_0/c) = {ratio_kBCS_H0:.4e}")
print(f"  log10(ratio)    = {log10_ratio:.4f}")

# Check 3: Compare k_BCS to LSS observational window k_obs ~ 0.01-1 Mpc^{-1}
k_LSS_low = 1e-4   # (local) Mpc^-1, bottom of LSS window
k_LSS_high = 1.0   # (local) Mpc^-1, top of LSS window / gate upper
print(f"\n  LSS observational window: [{k_LSS_low:.1e}, {k_LSS_high:.1e}] Mpc^{{-1}}")
print(f"  k_BCS / k_LSS_high = {k_BCS_today_Mpc/k_LSS_high:.3e}")
print(f"  log10(k_BCS/1 Mpc^-1) = {np.log10(k_BCS_today_Mpc):.3f}")

# Check 4: the k-scale should naturally be around T_CMB * (dimensionless number)
# -> k_BCS_today is of order T_CMB in GeV, convert: T_CMB * 1.563e38 ~ 3.7e25 Mpc^-1
k_from_TCMB = T_CMB_GeV * Mpc_to_GeV_inv   # (local) Mpc^-1
print(f"\n  T_CMB in Mpc^-1 = {k_from_TCMB:.4e} Mpc^{{-1}}")
print(f"  k_BCS / T_CMB   = {k_BCS_today_Mpc/k_from_TCMB:.6f}  (should equal k_BCS_nat = {k_BCS_nat:.6f})")

dim_residual = abs(k_BCS_today_Mpc/k_from_TCMB - k_BCS_nat)  # (local)
print(f"  Dimensional residual = {dim_residual:.3e}  (machine epsilon -> exact)")

# =============================================================================
# Step 7. Gate verdict
# =============================================================================
print("\n" + "=" * 78)
print("GATE BCS-GAP-K-SCALE-74")
print("=" * 78)
print(f"  Threshold:  PASS if k_BCS in [1e-4, 1] Mpc^{{-1}}")
print(f"              INFO if outside")
print(f"              FAIL if undefined")
print(f"  Computed:   k_BCS = {k_BCS_today_Mpc:.4e} Mpc^{{-1}}")

if not np.isfinite(k_BCS_today_Mpc):
    verdict = "FAIL"
    reason = "k_BCS is NaN or inf"
elif 1e-4 <= k_BCS_today_Mpc <= 1.0:
    verdict = "PASS"
    reason = f"k_BCS = {k_BCS_today_Mpc:.3e} Mpc^-1 is inside [1e-4, 1]"
else:
    verdict = "INFO"
    side = "above" if k_BCS_today_Mpc > 1.0 else "below"
    reason = (f"k_BCS = {k_BCS_today_Mpc:.3e} Mpc^-1 is {side} the LSS "
              f"observational window [1e-4, 1]. This is the k-scale of the "
              f"BCS gap as a rest-frame energy; redshifted as k ~ 1/a, it "
              f"lies in the ultra-UV of today's P(k). The gap imprints no "
              f"feature in the observable LSS window -- it is far above any "
              f"k scanned by BOSS/DESI/Euclid. The same redshift argument "
              f"explains why BCS physics at the fold is invisible to LSS "
              f"today: the fold scales redshift by M_KK/T_CMB ~ 3.16e29.")

print(f"  Verdict:    {verdict}")
print(f"  Reason:     {reason}")

# =============================================================================
# Step 8. Save data
# =============================================================================
out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "s74_bcs_gap_k_scale.npz")

np.savez(
    out_path,
    # Inputs (canonical)
    Delta_BCS=Delta_BCS,
    c_Gold=c_Gold,
    M_KK_gravity=M_KK_gravity,
    T_CMB_GeV=T_CMB_GeV,
    Mpc_to_GeV_inv=Mpc_to_GeV_inv,
    H_0_GeV=H_0_GeV,
    # Intermediate results
    k_BCS_nat=k_BCS_nat,
    k_BCS_fold_GeV=k_BCS_fold_GeV,
    a_ratio_fold_over_today=a_ratio_fold_over_today,
    N_e_total_canonical=N_e_total_canonical,
    k_BCS_today_GeV=k_BCS_today_GeV,
    # Main result
    k_BCS_today_Mpc=k_BCS_today_Mpc,
    # Cross-checks
    H_0_Mpc=H_0_Mpc,
    ratio_kBCS_H0=ratio_kBCS_H0,
    log10_ratio_kBCS_H0=log10_ratio,
    dim_residual=dim_residual,
    # Gate
    gate_threshold_low=1e-4,
    gate_threshold_high=1.0,
    gate_verdict=verdict,
)
print(f"\n  Saved: {out_path}")
print("=" * 78)
print(f"RESULT: k_BCS = {k_BCS_today_Mpc:.4e} Mpc^{{-1}}   (verdict: {verdict})")
print("=" * 78)
