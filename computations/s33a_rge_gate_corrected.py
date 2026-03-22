#!/usr/bin/env python3
"""
RGE-33a CORRECTED: Gauge coupling running with Baptista's actual normalization.

CORRECTIONS vs original s33a_rge_gate.py:
  1. Physical coupling ratio is g'/g = sqrt(3) * e^{-2s}, NOT e^{-2s}.
     Source: Baptista Paper 14 eqs 2.85, 2.88 with <Y,Y>=6*lambda_1,
     <T3,T3>=2*lambda_2 (line 1423). Cross-checked by Paper 13 eq 5.25:
     M_Z/M_W = sqrt(1 + 3*lambda_1^{-1}*lambda_2).
  2. Non-GUT beta functions: b_Y = 41/6 (not b_1=41/10 from SU(5)).
     Baptista's U(1) comes from su(3) Killing form, not SU(5) embedding.
  3. sin^2(theta_W) = 3*L2/(L1+3*L2) (Formula B, Baptista Paper 14 eq 2.93),
     NOT L2/(L1+L2) (Formula A, used in original).

The sqrt(3) factor arises from:
  - Hypercharge Y = diag(-2i, i, i): eigenvalue of -iL_Y on e_L^- is -3
  - Weak isospin T3 = iota(i*sigma_3): eigenvalue of -iL_{T3} on nu_L is 1
  - g'/2 = 3*sqrt(2*M_P/<Y,Y>), g/2 = sqrt(2*M_P/<T3,T3>)
  - g'/g = sqrt(3*lambda_2/lambda_1) = sqrt(3)*e^{-2s}

Author: main agent (RGE-33a reanalysis)
Date: 2026-03-07
"""

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

# ─────────────────────────────────────────────────────────────
# 1. Constants
# ─────────────────────────────────────────────────────────────

M_Z = 91.1876  # GeV
M_KK = 1e16    # GeV

# PDG values at M_Z
sin2_W_pdg = 0.23122
alpha_em_inv_pdg = 127.951
alpha_s_pdg = 0.1180

# Derived PDG couplings at M_Z (non-GUT normalization)
# sin^2(theta_W) = g'^2/(g'^2 + g^2)
# alpha_em = alpha_Y * cos^2(theta_W) = alpha_2 * sin^2(theta_W)
# => alpha_Y = alpha_em / cos^2 = alpha_em / (1 - sin^2)
# => alpha_2 = alpha_em / sin^2
alpha_em = 1.0 / alpha_em_inv_pdg
alpha_Y_MZ = alpha_em / (1 - sin2_W_pdg)  # non-GUT hypercharge
alpha_2_MZ = alpha_em / sin2_W_pdg

g_prime_MZ = np.sqrt(4 * np.pi * alpha_Y_MZ)
g_MZ = np.sqrt(4 * np.pi * alpha_2_MZ)
ratio_pdg_MZ = g_prime_MZ / g_MZ  # = tan(theta_W)

print("=" * 70)
print("RGE-33a CORRECTED: Baptista normalization")
print("=" * 70)
print(f"\nPDG at M_Z:")
print(f"  sin^2(theta_W) = {sin2_W_pdg}")
print(f"  alpha_em^{{-1}} = {alpha_em_inv_pdg}")
print(f"  alpha_Y (non-GUT) = {alpha_Y_MZ:.6f}  (1/alpha_Y = {1/alpha_Y_MZ:.2f})")
print(f"  alpha_2            = {alpha_2_MZ:.6f}  (1/alpha_2 = {1/alpha_2_MZ:.2f})")
print(f"  g' = {g_prime_MZ:.6f},  g = {g_MZ:.6f}")
print(f"  g'/g = tan(theta_W) = {ratio_pdg_MZ:.6f}")

# ─────────────────────────────────────────────────────────────
# 2. Baptista's coupling extraction (first principles)
# ─────────────────────────────────────────────────────────────

print(f"\n{'=' * 70}")
print("BAPTISTA COUPLING EXTRACTION (Paper 14 eqs 2.85, 2.88)")
print(f"{'=' * 70}")

s_dump = 0.190
lam1 = np.exp(2 * s_dump)   # u(1)/Y block
lam2 = np.exp(-2 * s_dump)  # su(2)/W block

# Trace norms (Paper 14 line 1423)
Y_norm_sq = 6 * lam1   # <Y, Y> = 6*lambda_1
T3_norm_sq = 2 * lam2  # <T3, T3> = 2*lambda_2

# Physical coupling ratio (Paper 14 eqs 2.85, 2.88)
# g'/2 = 3*sqrt(2*M_P/<Y,Y>)  [eigenvalue -3 on e_L^-]
# g/2  = sqrt(2*M_P/<T3,T3>)  [eigenvalue 1 on nu_L]
# g'/g = 3*sqrt(<T3,T3>/<Y,Y>) = 3*sqrt(2*lam2/(6*lam1))
#      = 3*sqrt(lam2/(3*lam1)) = sqrt(3*lam2/lam1) = sqrt(3)*e^{-2s}
ratio_baptista = np.sqrt(3 * lam2 / lam1)
ratio_baptista_direct = np.sqrt(3) * np.exp(-2 * s_dump)

# Cross-check: M_Z/M_W = sqrt(1 + 3*lam2/lam1) (Paper 13 eq 5.25)
MZ_over_MW = np.sqrt(1 + 3 * lam2 / lam1)
MZ_over_MW_SM = 1 / np.cos(np.arcsin(np.sqrt(sin2_W_pdg)))

# Old B-1 formula (metric ratio, missing sqrt(3))
ratio_old_B1 = np.exp(-2 * s_dump)

print(f"\n  Jensen metric at s = {s_dump}:")
print(f"    lambda_1 (u(1)) = e^{{2*{s_dump}}} = {lam1:.6f}")
print(f"    lambda_2 (su(2)) = e^{{-2*{s_dump}}} = {lam2:.6f}")
print(f"    <Y,Y> = 6*lambda_1 = {Y_norm_sq:.6f}")
print(f"    <T3,T3> = 2*lambda_2 = {T3_norm_sq:.6f}")
print(f"\n  Coupling ratios:")
print(f"    OLD B-1 (metric only):  g1/g2 = e^{{-2s}} = {ratio_old_B1:.6f}")
print(f"    CORRECTED (physical):   g'/g  = sqrt(3)*e^{{-2s}} = {ratio_baptista:.6f}")
print(f"    Direct formula:         sqrt(3*lam2/lam1) = {ratio_baptista_direct:.6f}")
print(f"    Consistency check:      {abs(ratio_baptista - ratio_baptista_direct):.2e}")
print(f"\n  Cross-checks:")
print(f"    M_Z/M_W (Baptista eq 5.25) = {MZ_over_MW:.6f}")
print(f"    M_Z/M_W (SM, PDG)          = {MZ_over_MW_SM:.6f}")
print(f"    g'/g implied by eq 5.25    = sqrt(MZ/MW^2 - 1) = {np.sqrt(MZ_over_MW**2 - 1):.6f}")
print(f"    Matches g'/g = {ratio_baptista:.6f}? {abs(np.sqrt(MZ_over_MW**2 - 1) - ratio_baptista) < 1e-10}")

# sin^2(theta_W) at KK scale (Formula B)
sin2_KK = 3 * lam2 / (lam1 + 3 * lam2)
# Formula A (wrong, for comparison)
sin2_KK_A = ratio_old_B1**2 / (1 + ratio_old_B1**2)

print(f"\n  Weinberg angle at KK scale (tree-level):")
print(f"    Formula B (correct): sin^2 = 3*L2/(L1+3*L2) = {sin2_KK:.6f}")
print(f"    Formula A (wrong):   sin^2 = r^2/(1+r^2)     = {sin2_KK_A:.6f}")

# ─────────────────────────────────────────────────────────────
# 3. SM RGE running (non-GUT normalization)
# ─────────────────────────────────────────────────────────────

print(f"\n{'=' * 70}")
print("SM RGE RUNNING (non-GUT normalization)")
print(f"{'=' * 70}")

# Beta function coefficients
# Non-GUT: b_Y = 41/6 for U(1)_Y (standard hypercharge)
# SU(2):   b_2 = -19/6
# SU(3):   b_3 = -7
b_Y = 41.0 / 6.0
b_2 = -19.0 / 6.0
b_3 = -7.0

# GUT-normalized for comparison
b_1_GUT = 41.0 / 10.0

L = np.log(M_KK / M_Z)
print(f"  ln(M_KK/M_Z) = {L:.4f}")
print(f"  Beta coefficients:")
print(f"    b_Y (non-GUT) = {b_Y:.4f}   [b_1_GUT = {b_1_GUT:.4f}]")
print(f"    b_2            = {b_2:.4f}")

# Run PDG values UP to M_KK to get SM requirement
inv_aY_MZ = 1.0 / alpha_Y_MZ
inv_a2_MZ = 1.0 / alpha_2_MZ

# 1/alpha_i(M_KK) = 1/alpha_i(M_Z) - b_i/(2*pi) * ln(M_KK/M_Z)
inv_aY_KK_SM = inv_aY_MZ - b_Y / (2 * np.pi) * L
inv_a2_KK_SM = inv_a2_MZ - b_2 / (2 * np.pi) * L

aY_KK_SM = 1.0 / inv_aY_KK_SM
a2_KK_SM = 1.0 / inv_a2_KK_SM

ratio_SM_KK = np.sqrt(aY_KK_SM / a2_KK_SM)  # g'/g at M_KK from SM

print(f"\n  SM requirement at M_KK = {M_KK:.0e} GeV (running PDG up):")
print(f"    1/alpha_Y(M_KK) = {inv_aY_KK_SM:.4f}")
print(f"    1/alpha_2(M_KK) = {inv_a2_KK_SM:.4f}")
print(f"    alpha_Y/alpha_2 = {aY_KK_SM/a2_KK_SM:.6f}")
print(f"    g'/g (SM at M_KK) = {ratio_SM_KK:.6f}")

# ─────────────────────────────────────────────────────────────
# 4. Framework prediction at dump point
# ─────────────────────────────────────────────────────────────

print(f"\n{'=' * 70}")
print("FRAMEWORK vs SM at M_KK")
print(f"{'=' * 70}")

print(f"\n  Framework (Baptista at s={s_dump}):")
print(f"    g'/g = sqrt(3)*e^{{-2*{s_dump}}} = {ratio_baptista:.6f}")
print(f"    alpha_Y/alpha_2 = 3*e^{{-4*{s_dump}}} = {3*np.exp(-4*s_dump):.6f}")

print(f"\n  SM requirement (from PDG running):")
print(f"    g'/g = {ratio_SM_KK:.6f}")
print(f"    alpha_Y/alpha_2 = {aY_KK_SM/a2_KK_SM:.6f}")

dev_corrected = abs(ratio_baptista - ratio_SM_KK) / ratio_SM_KK * 100
dev_old = abs(ratio_old_B1 - ratio_SM_KK) / ratio_SM_KK * 100

print(f"\n  Deviations:")
print(f"    CORRECTED: |{ratio_baptista:.4f} - {ratio_SM_KK:.4f}| / {ratio_SM_KK:.4f} = {dev_corrected:.1f}%")
print(f"    OLD (B-1): |{ratio_old_B1:.4f} - {ratio_SM_KK:.4f}| / {ratio_SM_KK:.4f} = {dev_old:.1f}%")

# ─────────────────────────────────────────────────────────────
# 5. Run framework ratio down to M_Z
# ─────────────────────────────────────────────────────────────

print(f"\n{'=' * 70}")
print("RUNNING FRAMEWORK RATIO DOWN TO M_Z")
print(f"{'=' * 70}")

# We need absolute couplings. Use alpha_2(M_KK) from SM running,
# then set alpha_Y from Baptista's ratio.
alpha_2_KK = a2_KK_SM  # anchor to SM alpha_2 at M_KK
alpha_Y_KK = 3 * np.exp(-4 * s_dump) * alpha_2_KK  # Baptista ratio

print(f"\n  At M_KK (anchored to SM alpha_2):")
print(f"    alpha_2(M_KK) = {alpha_2_KK:.6f}")
print(f"    alpha_Y(M_KK) = {alpha_Y_KK:.6f}  [from 3*e^(-4s)*alpha_2]")

# Run down: 1/alpha_i(M_Z) = 1/alpha_i(M_KK) + b_i/(2*pi) * ln(M_KK/M_Z)
inv_aY_MZ_pred = 1.0/alpha_Y_KK + b_Y/(2*np.pi) * L
inv_a2_MZ_pred = 1.0/alpha_2_KK + b_2/(2*np.pi) * L

aY_MZ_pred = 1.0 / inv_aY_MZ_pred
a2_MZ_pred = 1.0 / inv_a2_MZ_pred

g_prime_pred = np.sqrt(4 * np.pi * aY_MZ_pred)
g_pred = np.sqrt(4 * np.pi * a2_MZ_pred)
ratio_MZ_pred = g_prime_pred / g_pred
sin2_MZ_pred = aY_MZ_pred / (aY_MZ_pred + a2_MZ_pred)

print(f"\n  After running to M_Z (non-GUT beta functions):")
print(f"    alpha_Y(M_Z) = {aY_MZ_pred:.6f}  (PDG: {alpha_Y_MZ:.6f})")
print(f"    alpha_2(M_Z) = {a2_MZ_pred:.6f}  (PDG: {alpha_2_MZ:.6f})")
print(f"    g'/g(M_Z)    = {ratio_MZ_pred:.6f}  (PDG: {ratio_pdg_MZ:.6f})")
print(f"    sin^2(theta_W) = {sin2_MZ_pred:.6f}  (PDG: {sin2_W_pdg:.6f})")

dev_sin2 = abs(sin2_MZ_pred - sin2_W_pdg) / sin2_W_pdg * 100
dev_ratio_MZ = abs(ratio_MZ_pred - ratio_pdg_MZ) / ratio_pdg_MZ * 100
print(f"\n  Deviation at M_Z:")
print(f"    sin^2 deviation: {dev_sin2:.1f}%")
print(f"    g'/g deviation:  {dev_ratio_MZ:.1f}%")

# Also run with WRONG normalization for comparison (original RGE-33a)
print(f"\n  --- COMPARISON: Original RGE-33a (wrong normalization) ---")
# Original used g1/g2 = e^{-2s} with GUT beta b1=41/10
alpha_1_GUT_KK_old = ratio_old_B1**2 * alpha_2_KK  # old: alpha_1/alpha_2 = r^2
inv_a1_MZ_old = 1.0/alpha_1_GUT_KK_old + b_1_GUT/(2*np.pi) * L
inv_a2_MZ_old = 1.0/alpha_2_KK + b_2/(2*np.pi) * L
a1_MZ_old = 1.0 / inv_a1_MZ_old
a2_MZ_old = 1.0 / inv_a2_MZ_old
ratio_MZ_old = np.sqrt(a1_MZ_old / a2_MZ_old)
sin2_MZ_old = a1_MZ_old / (a1_MZ_old + (5.0/3.0)*a2_MZ_old)
print(f"    g1/g2(M_Z) [GUT norm] = {ratio_MZ_old:.6f}")
print(f"    sin^2 [GUT formula]   = {sin2_MZ_old:.6f}")

# ─────────────────────────────────────────────────────────────
# 6. Sensitivity scan: s vs sin^2(theta_W)(M_Z)
# ─────────────────────────────────────────────────────────────

print(f"\n{'=' * 70}")
print("SENSITIVITY SCAN: s -> sin^2(theta_W)(M_Z)")
print(f"{'=' * 70}")

s_range = np.linspace(0.01, 1.0, 500)
sin2_vs_s = np.zeros_like(s_range)
ratio_vs_s = np.zeros_like(s_range)

for i, s in enumerate(s_range):
    r_KK = 3 * np.exp(-4 * s)  # alpha_Y/alpha_2 at M_KK (Baptista)
    aY_KK = r_KK * alpha_2_KK

    inv_aY_low = 1.0/aY_KK + b_Y/(2*np.pi) * L
    inv_a2_low = 1.0/alpha_2_KK + b_2/(2*np.pi) * L

    if inv_aY_low > 0 and inv_a2_low > 0:
        aY_low = 1.0/inv_aY_low
        a2_low = 1.0/inv_a2_low
        sin2_vs_s[i] = aY_low / (aY_low + a2_low)
        ratio_vs_s[i] = np.sqrt(aY_low / a2_low)
    else:
        sin2_vs_s[i] = np.nan
        ratio_vs_s[i] = np.nan

# Find s_0 where sin^2 = 0.231
try:
    # Find crossing
    for k in range(len(sin2_vs_s) - 1):
        if np.isnan(sin2_vs_s[k]) or np.isnan(sin2_vs_s[k+1]):
            continue
        if (sin2_vs_s[k] - sin2_W_pdg) * (sin2_vs_s[k+1] - sin2_W_pdg) < 0:
            frac = (sin2_W_pdg - sin2_vs_s[k]) / (sin2_vs_s[k+1] - sin2_vs_s[k])
            s_match = s_range[k] + frac * (s_range[k+1] - s_range[k])
            print(f"\n  sin^2(theta_W)(M_Z) = 0.231 achieved at s = {s_match:.4f}")
            print(f"  Dump point: s = {s_dump}")
            print(f"  Gap: Delta_s = {s_match - s_dump:.4f}")

            # What phi_paasch would be at this s?
            # phi = m_(3,0)/m_(0,0) -- need to estimate (varies with s)
            print(f"\n  At s = {s_match:.4f}:")
            print(f"    g'/g (KK) = sqrt(3)*e^{{-2*{s_match:.4f}}} = {np.sqrt(3)*np.exp(-2*s_match):.6f}")
            print(f"    sin^2 (tree, Formula B) = {3*np.exp(-2*s_match)/(np.exp(2*s_match)+3*np.exp(-2*s_match)):.6f}")
            break
except Exception as e:
    print(f"  Could not find crossing: {e}")

# Also find where g'/g crosses 1 (hierarchy crossover)
s_cross = np.log(np.sqrt(3)) / 2  # sqrt(3)*e^{-2s} = 1 => e^{-2s} = 1/sqrt(3)
print(f"\n  g'/g = 1 crossover at s = ln(sqrt(3))/2 = {s_cross:.4f}")
print(f"  For s < {s_cross:.3f}: g' > g (wrong hierarchy)")
print(f"  For s > {s_cross:.3f}: g' < g (right hierarchy)")
print(f"  Dump point s = {s_dump} is {'BELOW' if s_dump < s_cross else 'ABOVE'} crossover")

# Print table
print(f"\n  {'s':>6s}  {'g\'/g(KK)':>10s}  {'sin2(KK)':>10s}  {'sin2(MZ)':>10s}  {'g\'/g(MZ)':>10s}")
print(f"  {'-'*52}")
for s_val in [0.0, 0.10, 0.15, 0.190, 0.275, 0.30, 0.35, 0.40, 0.50, 0.575, 0.70, 1.0]:
    idx = np.argmin(np.abs(s_range - s_val))
    r_kk = np.sqrt(3) * np.exp(-2*s_val)
    s2_kk = 3*np.exp(-2*s_val)/(np.exp(2*s_val)+3*np.exp(-2*s_val))
    marker = " <-- dump" if abs(s_val - 0.190) < 0.001 else ""
    if not np.isnan(sin2_vs_s[idx]):
        print(f"  {s_val:6.3f}  {r_kk:10.6f}  {s2_kk:10.6f}  {sin2_vs_s[idx]:10.6f}  {ratio_vs_s[idx]:10.6f}{marker}")
    else:
        print(f"  {s_val:6.3f}  {r_kk:10.6f}  {s2_kk:10.6f}  {'NaN':>10s}  {'NaN':>10s}{marker}")

# ─────────────────────────────────────────────────────────────
# 7. Gate re-evaluation
# ─────────────────────────────────────────────────────────────

print(f"\n{'=' * 70}")
print("GATE RE-EVALUATION: RGE-33a CORRECTED")
print(f"{'=' * 70}")

print(f"\n  ORIGINAL RGE-33a (Session 33a):")
print(f"    Input: g1/g2 = e^{{-2*0.190}} = {ratio_old_B1:.6f} (metric ratio)")
print(f"    Beta: b_1 = 41/10 (GUT normalized)")
print(f"    Result: g1/g2(M_Z) = 0.326, sin^2 = 0.060")
print(f"    Deviation: 54%")
print(f"    Verdict: FAIL ('wrong-sign hierarchy')")

print(f"\n  CORRECTED RGE-33a:")
print(f"    Input: g'/g = sqrt(3)*e^{{-2*0.190}} = {ratio_baptista:.6f} (physical ratio)")
print(f"    Beta: b_Y = 41/6 (non-GUT, Baptista normalization)")
print(f"    Result: g'/g(M_Z) = {ratio_MZ_pred:.6f}, sin^2 = {sin2_MZ_pred:.6f}")
print(f"    Deviation (sin^2): {dev_sin2:.1f}%")
print(f"    Deviation (g'/g vs SM at M_KK): {dev_corrected:.1f}%")

if dev_sin2 < 5:
    verdict = "SOFT PASS"
elif dev_sin2 < 10:
    verdict = "PASS"
else:
    verdict = "FAIL"

print(f"\n  >>> CORRECTED VERDICT: {verdict} ({dev_sin2:.1f}% sin^2 deviation) <<<")

print(f"\n  KEY CORRECTIONS:")
print(f"    1. 'Wrong-sign hierarchy' RETRACTED.")
print(f"       Direction of e^{{-2s}} is CORRECT (suppresses g' relative to g).")
print(f"       Actual issue: sqrt(3) factor from eigenvalue ratio means g'>g")
print(f"       at s=0.190 (need s>{s_cross:.3f} for g'<g).")
print(f"    2. Physical coupling ratio: g'/g = sqrt(3)*e^{{-2s}}, not e^{{-2s}}.")
print(f"       Source: Baptista Paper 14 eq 2.85/2.88, Paper 13 eq 5.25.")
print(f"    3. Deviation: {dev_sin2:.0f}%, not 54%.")
print(f"    4. Root cause: dump point s=0.190 vs Weinberg-angle-compatible")
print(f"       s ~ 0.35 (Phi-Weinberg anti-correlation, Session 30 [30Bb-1]).")

# ─────────────────────────────────────────────────────────────
# 8. Comparison table
# ─────────────────────────────────────────────────────────────

print(f"\n{'=' * 70}")
print("COMPARISON: ORIGINAL vs CORRECTED")
print(f"{'=' * 70}")
print(f"\n  {'Quantity':<35s} {'Original':>12s} {'Corrected':>12s} {'PDG':>12s}")
print(f"  {'-'*71}")
print(f"  {'g ratio at M_KK':<35s} {ratio_old_B1:>12.6f} {ratio_baptista:>12.6f} {ratio_SM_KK:>12.6f}")
print(f"  {'sin^2 (tree-level, KK)':<35s} {sin2_KK_A:>12.6f} {sin2_KK:>12.6f} {'N/A':>12s}")
print(f"  {'sin^2(theta_W)(M_Z)':<35s} {'0.060':>12s} {sin2_MZ_pred:>12.6f} {sin2_W_pdg:>12.6f}")
print(f"  {'g ratio at M_Z':<35s} {'0.326':>12s} {ratio_MZ_pred:>12.6f} {ratio_pdg_MZ:>12.6f}")
print(f"  {'Deviation (sin^2)':<35s} {'74%':>12s} {f'{dev_sin2:.1f}%':>12s} {'---':>12s}")
print(f"  {'Beta coeff (U(1))':<35s} {'41/10=4.10':>12s} {f'41/6={b_Y:.2f}':>12s} {'---':>12s}")
print(f"  {'Normalization':<35s} {'GUT (SU(5))':>12s} {'Baptista':>12s} {'---':>12s}")
print(f"  {'Verdict':<35s} {'FAIL':>12s} {verdict:>12s} {'---':>12s}")
print(f"  {'Wrong-sign claim':<35s} {'Yes':>12s} {'RETRACTED':>12s} {'---':>12s}")

# ─────────────────────────────────────────────────────────────
# 9. Plot
# ─────────────────────────────────────────────────────────────

fig, axes = plt.subplots(2, 2, figsize=(14, 10))

# Panel 1: sin^2(theta_W)(M_Z) vs s
ax = axes[0, 0]
valid = ~np.isnan(sin2_vs_s)
ax.plot(s_range[valid], sin2_vs_s[valid], 'b-', linewidth=2, label="Corrected (Baptista)")
ax.axhline(sin2_W_pdg, color='green', linestyle=':', linewidth=2, label=f'PDG: {sin2_W_pdg}')
ax.axvline(s_dump, color='red', linestyle='--', alpha=0.7, label=f's_dump = {s_dump}')
ax.axvline(s_cross, color='orange', linestyle='--', alpha=0.7, label=f"g'=g crossover: {s_cross:.3f}")
ax.axhspan(0.20, 0.25, alpha=0.1, color='green')
ax.set_xlabel('Jensen parameter s')
ax.set_ylabel("sin^2(theta_W) at M_Z")
ax.set_title("Corrected: sin^2 vs Jensen parameter")
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3)

# Panel 2: g'/g ratio at M_KK vs s
ax = axes[0, 1]
s_fine = np.linspace(0.01, 1.0, 200)
gp_over_g = np.sqrt(3) * np.exp(-2 * s_fine)
ax.plot(s_fine, gp_over_g, 'b-', linewidth=2, label="Framework: sqrt(3)*e^{-2s}")
ax.axhline(ratio_SM_KK, color='green', linestyle=':', linewidth=2, label=f'SM at M_KK: {ratio_SM_KK:.3f}')
ax.axhline(1.0, color='gray', linestyle='-', alpha=0.3, label="g' = g")
ax.axhline(ratio_old_B1, color='red', linestyle=':', alpha=0.5, label=f'Old B-1: e^{{-2s}} = {ratio_old_B1:.3f}')
ax.axvline(s_dump, color='red', linestyle='--', alpha=0.7, label=f's_dump = {s_dump}')
ax.fill_between(s_fine, 0, 1, where=gp_over_g > 1, alpha=0.05, color='red')
ax.fill_between(s_fine, 0, 1, where=gp_over_g <= 1, alpha=0.05, color='green')
ax.set_xlabel('Jensen parameter s')
ax.set_ylabel("g'/g at M_KK")
ax.set_title("Coupling ratio at compactification scale")
ax.legend(fontsize=7, loc='upper right')
ax.set_ylim(0, 2)
ax.grid(True, alpha=0.3)

# Panel 3: Original vs Corrected comparison
ax = axes[1, 0]
categories = ['g_ratio\n(M_KK)', 'sin^2\n(M_Z)', 'Deviation\n(%)']
old_vals = [ratio_old_B1, 0.060, 54]
new_vals = [ratio_baptista, sin2_MZ_pred, dev_sin2]
pdg_vals = [ratio_SM_KK, sin2_W_pdg, 0]

x = np.arange(len(categories))
w = 0.25
bars1 = ax.bar(x - w, old_vals, w, label='Original RGE-33a', color='salmon')
bars2 = ax.bar(x, new_vals, w, label='Corrected', color='steelblue')
bars3 = ax.bar(x + w, pdg_vals, w, label='PDG/Target', color='green', alpha=0.7)
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.set_title('Original vs Corrected RGE-33a')
ax.legend(fontsize=8)
ax.grid(True, alpha=0.3, axis='y')

# Panel 4: Summary text
ax = axes[1, 1]
ax.axis('off')
summary = (
    f"RGE-33a CORRECTED GATE SUMMARY\n"
    f"{'=' * 45}\n"
    f"Baptista normalization (Paper 14 eqs 2.85/2.88):\n"
    f"  g'/g = sqrt(3) * e^{{-2s}}\n"
    f"  sin^2 = 3*L2/(L1 + 3*L2)  [Formula B]\n"
    f"{'─' * 45}\n"
    f"At dump point s = {s_dump}:\n"
    f"  g'/g(M_KK) = {ratio_baptista:.6f}\n"
    f"  SM needs:    {ratio_SM_KK:.6f}\n"
    f"{'─' * 45}\n"
    f"After RGE to M_Z (b_Y=41/6, b_2=-19/6):\n"
    f"  sin^2 = {sin2_MZ_pred:.5f}  (PDG: {sin2_W_pdg})\n"
    f"  Deviation: {dev_sin2:.1f}%\n"
    f"{'─' * 45}\n"
    f"VERDICT: {verdict}\n"
    f"'Wrong-sign hierarchy': RETRACTED\n"
    f"Direction correct; magnitude insufficient\n"
    f"Root cause: Phi-Weinberg anti-correlation\n"
    f"  (s_dump=0.190 vs s_Weinberg~0.35)"
)
ax.text(0.05, 0.95, summary, transform=ax.transAxes, fontsize=9.5,
        verticalalignment='top', fontfamily='monospace',
        bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.suptitle('RGE-33a CORRECTED: Baptista Normalization (sqrt(3) factor)',
             fontsize=13, fontweight='bold')
plt.tight_layout()
plt.savefig('tier0-computation/s33a_rge_gate_corrected.png', dpi=150, bbox_inches='tight')
print(f"\nPlot saved: tier0-computation/s33a_rge_gate_corrected.png")

# ─────────────────────────────────────────────────────────────
# 10. Save data
# ─────────────────────────────────────────────────────────────

np.savez('tier0-computation/s33a_rge_gate_corrected.npz',
         # Baptista coupling extraction
         s_dump=np.array([s_dump]),
         ratio_baptista=np.array([ratio_baptista]),
         ratio_old_B1=np.array([ratio_old_B1]),
         ratio_SM_KK=np.array([ratio_SM_KK]),
         sin2_KK_formulaB=np.array([sin2_KK]),
         sin2_KK_formulaA=np.array([sin2_KK_A]),
         # RGE results
         sin2_MZ_pred=np.array([sin2_MZ_pred]),
         ratio_MZ_pred=np.array([ratio_MZ_pred]),
         dev_sin2_pct=np.array([dev_sin2]),
         dev_ratio_pct=np.array([dev_corrected]),
         verdict=np.array([verdict]),
         # Scan data
         s_range=s_range,
         sin2_vs_s=sin2_vs_s,
         ratio_vs_s=ratio_vs_s,
         # Constants
         b_Y=np.array([b_Y]),
         b_2=np.array([b_2]),
         M_KK=np.array([M_KK]),
         s_crossover=np.array([s_cross]),
         )
print(f"Data saved: tier0-computation/s33a_rge_gate_corrected.npz")
