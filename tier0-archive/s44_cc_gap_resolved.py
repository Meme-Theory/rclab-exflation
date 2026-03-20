#!/usr/bin/env python3
"""
CC-GAP-RESOLVED-44: Definitive CC gap table with Vol(SU(3)) correction.

Resolves the Vol(SU(3)) discrepancy identified by the data provenance audit:
  - s42_constants_snapshot.py used Vol_unit = sqrt(3)*(4*pi^2)^3/12 = 8880.93 (WRONG)
  - s42_gradient_stiffness.py used Vol_Haar = 8*sqrt(3)*pi^4 = 1349.74 (CORRECT)
  - Weyl integration formula: Vol(SU(3)) = sqrt(n)*(2*pi)^{(n^2-1)/2} / prod(k!) for n=3

CRITICAL FINDING: The Vol(SU(3)) error does NOT contaminate M_KK_Kerner or rho_Lambda.
  - M_KK_Kerner = 5.04e17 from alpha_a = M_KK^2/(M_Pl^2*g_aa): NO Vol dependence.
  - M_KK_GN = 7.43e16 from M_KK^2 = pi^3*M_Pl^2/(12*a_2): NO Vol dependence.
  - rho_Lambda = (2/pi^2)*a_0*M_KK^4: uses M_KK directly, NO Vol dependence.
  - Vol(SU(3)) enters ONLY through M_star (higher-D Planck mass) and V_phys.

The 0.83-decade M_KK tension between gravity (7.43e16) and Kerner (5.04e17) routes
is REAL AND STRUCTURAL, not a Vol(SU(3)) artifact. However, SAKHAROV-GN-44 showed
that at Lambda_eff = 10*M_KK (effective 4D UV cutoff), G_N agrees to factor 2.3.
The resolution: the two routes use DIFFERENT formulas with DIFFERENT dependences on
the cutoff function f. They agree for G_N (second moment) but diverge for CC (zeroth).

This script produces the DEFINITIVE CC gap table.

Author: Einstein-Theorist
Session: S44 W7-2
"""

import numpy as np
from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

DATA_DIR = Path(__file__).parent

print("=" * 80)
print("CC-GAP-RESOLVED-44: Definitive CC Gap Table")
print("=" * 80)

# ============================================================
# 0. VOL(SU(3)) CORRECTION AUDIT
# ============================================================
print("\n" + "=" * 80)
print("SECTION 0: Vol(SU(3)) Correction Audit")
print("=" * 80)

PI = np.pi
PI2 = PI**2

# The WRONG formula (s42_constants_snapshot.py line 622)
Vol_wrong = np.sqrt(3) * (4 * PI2)**3 / 12
# The CORRECT formula (Weyl integration, s42_gradient_stiffness.py line 1274)
Vol_correct = 8 * np.sqrt(3) * PI**4
ratio_vol = Vol_wrong / Vol_correct

print(f"\n  WRONG:   Vol_unit = sqrt(3)*(4*pi^2)^3/12 = {Vol_wrong:.2f}")
print(f"  CORRECT: Vol_Haar = 8*sqrt(3)*pi^4 = {Vol_correct:.2f}")
print(f"  Ratio (wrong/correct) = {ratio_vol:.2f}")

# With g_0 = 3:
g0 = 3.0
Vol_code_wrong = g0**4 * Vol_wrong
Vol_code_correct = g0**4 * Vol_correct
print(f"\n  Vol_code (wrong) = 81 * {Vol_wrong:.2f} = {Vol_code_wrong:.2f}")
print(f"  Vol_code (correct) = 81 * {Vol_correct:.2f} = {Vol_code_correct:.2f}")

# Impact on M_star: M_*^10 = M_Pl^2 * M_KK^8 / Vol_code
# M_*(corrected) / M_*(wrong) = (Vol_wrong/Vol_correct)^{1/10}
M_star_ratio = ratio_vol**(1.0/10.0)
print(f"\n  M_star impact: M_*(corrected)/M_*(wrong) = {ratio_vol:.2f}^(1/10) = {M_star_ratio:.4f}")
print(f"  => M_star shifts by {(M_star_ratio-1)*100:.1f}% (21% change, sub-OOM)")

# DOES THIS AFFECT M_KK_KERNER?
print(f"\n  M_KK_Kerner formula: alpha_a = M_KK^2 / (M_Pl^2 * g_aa)")
print(f"  => NO Vol(SU(3)) dependence. M_KK_Kerner = 5.04e17 UNCHANGED.")
print(f"\n  M_KK_GN formula: M_KK^2 = pi^3 * M_Pl^2 / (12 * a_2)")
print(f"  => NO Vol(SU(3)) dependence. M_KK_GN = 7.43e16 UNCHANGED.")
print(f"\n  rho_Lambda formula: (2/pi^2) * a_0 * M_KK^4")
print(f"  => NO Vol(SU(3)) dependence. rho_Lambda UNCHANGED.")
print(f"\n  CONCLUSION: Vol(SU(3)) error affects M_star and V_phys ONLY.")
print(f"  The 0.83-decade M_KK tension is REAL, not a Vol artifact.")
print(f"  The CC gap is UNAFFECTED by this correction.")

# ============================================================
# 1. PHYSICAL CONSTANTS
# ============================================================
print("\n" + "=" * 80)
print("SECTION 1: Physical Constants")
print("=" * 80)

from canonical_constants import M_Pl_reduced as M_Pl  # GeV
from canonical_constants import G_N as G_N_SI  # m^3 kg^-1 s^-2

# Observed CC
H_0_SI = 67.36e3 / 3.086e22  # s^-1
H_0_GeV = H_0_SI * 6.582e-16 * 1e-9  # GeV
rho_crit = 3 * H_0_GeV**2 * M_Pl**2  # GeV^4
Omega_Lambda = 0.6847
rho_obs = Omega_Lambda * rho_crit
rho_obs_standard = 2.888e-47  # GeV^4, commonly cited

print(f"\n  M_Pl (reduced) = {M_Pl:.3e} GeV")
print(f"  rho_Lambda_obs = {rho_obs:.4e} GeV^4")
print(f"  Cross-check (standard): {rho_obs_standard:.3e} GeV^4")
print(f"  Ratio: {rho_obs / rho_obs_standard:.4f}")

# ============================================================
# 2. FRAMEWORK ENERGY SCALES
# ============================================================
print("\n" + "=" * 80)
print("SECTION 2: Framework Energy Scales")
print("=" * 80)

# Load stored values
d42 = np.load(DATA_DIR / 's42_constants_snapshot.npz', allow_pickle=True)
d36 = np.load(DATA_DIR / 's36_sfull_tau_stabilization.npz', allow_pickle=True)
d_eih = np.load(DATA_DIR / 's44_eih_grav.npz', allow_pickle=True)
d_tl = np.load(DATA_DIR / 's44_tracelog_cc.npz', allow_pickle=True)
d_jac = np.load(DATA_DIR / 's44_jacobson_spec.npz', allow_pickle=True)

M_KK_GN = float(d42['M_KK_from_GN'])       # 7.43e16 GeV
M_KK_K  = float(d42['M_KK_kerner'])          # 5.04e17 GeV
a0 = float(d42['a0_fold'])                    # 6440
a2 = float(d42['a2_fold'])                    # 2776.17
a4 = float(d42['a4_fold'])                    # 1350.72
S_fold = float(d36['S_fold'][0])              # 250360.68

print(f"\n  M_KK (gravity route, a_2) = {M_KK_GN:.4e} GeV  [log10 = {np.log10(M_KK_GN):.3f}]")
print(f"  M_KK (Kerner/gauge route)  = {M_KK_K:.4e} GeV  [log10 = {np.log10(M_KK_K):.3f}]")
print(f"  Tension: {np.log10(M_KK_K/M_KK_GN):.3f} decades")
print(f"\n  a_0 = {a0:.0f}  (mode count)")
print(f"  a_2 = {a2:.2f}  (spectral zeta sum, fixes G_N)")
print(f"  a_4 = {a4:.2f}  (spectral zeta sum)")
print(f"  S_fold = {S_fold:.2f}  (total spectral action at fold)")

# CHOICE OF M_KK: Use M_KK_GN because:
# 1. It is derived from G_N (observed) + a_2 (computed) -- two inputs
# 2. Sakharov formula confirms G_N to factor 2.3 at Lambda=10*M_KK (SAKHAROV-GN-44 PASS)
# 3. The Kerner route gives M_KK from alpha_GUT assumption + RGE
# 4. For CC, what matters is what gravitates -- this is G_N, hence M_KK_GN
M_KK = M_KK_GN
print(f"\n  USING M_KK = M_KK_GN = {M_KK:.4e} GeV")
print(f"  Rationale: G_N determines gravitational vacuum energy.")
print(f"  Validated by SAKHAROV-GN-44 (factor 2.3 at Lambda=10*M_KK).")

# ============================================================
# 3. VACUUM ENERGY AT EACH STAGE
# ============================================================
print("\n" + "=" * 80)
print("SECTION 3: Vacuum Energy Ladder")
print("=" * 80)

M_KK4 = M_KK**4

# Stage 1: Textbook M_Pl^4
rho_Pl = M_Pl**4
gap_Pl = np.log10(rho_Pl / rho_obs)
print(f"\n  1. M_Pl^4 (textbook)")
print(f"     rho = {rho_Pl:.4e} GeV^4")
print(f"     Gap = {gap_Pl:.2f} orders")

# Stage 2: Bare M_KK^4
gap_bare = np.log10(M_KK4 / rho_obs)
print(f"\n  2. M_KK^4 (bare)")
print(f"     rho = {M_KK4:.4e} GeV^4")
print(f"     Gap = {gap_bare:.2f} orders")
print(f"     Bought: {gap_Pl - gap_bare:.2f} orders from (M_KK/M_Pl)^4")

# Stage 3: Spectral action polynomial
rho_spec = (2.0 / PI2) * a0 * M_KK4
gap_spec = np.log10(rho_spec / rho_obs)
print(f"\n  3. Spectral action polynomial: (2/pi^2) * a_0 * M_KK^4")
print(f"     = (2/{PI2:.4f}) * {a0:.0f} * {M_KK4:.3e}")
print(f"     rho = {rho_spec:.4e} GeV^4")
print(f"     Gap = {gap_spec:.2f} orders")
print(f"     Change from bare: {gap_spec - gap_bare:+.2f} orders (a_0 mode counting adds)")

# Stage 4: S_fold normalization
rho_Sfold = S_fold * M_KK4 / (16 * PI2)
gap_Sfold = np.log10(rho_Sfold / rho_obs)
print(f"\n  4. S_fold * M_KK^4 / (16pi^2)")
print(f"     S_fold = {S_fold:.2f}")
print(f"     rho = {rho_Sfold:.4e} GeV^4")
print(f"     Gap = {gap_Sfold:.2f} orders")

# ============================================================
# 4. S44 SUPPRESSION FACTORS
# ============================================================
print("\n" + "=" * 80)
print("SECTION 4: S44 Structural Suppressions")
print("=" * 80)

# Factor A: Trace-log replacement (W1-4, TRACE-LOG-CC-44)
# Polynomial SA -> trace-log functional. Volovik (2005): correct gravitating
# vacuum energy is Tr ln(D_K^2), not Tr f(D_K^2/Lambda^2).
tl_ratio = float(d_tl['ratio_logvspoly'])  # 3.09e-3
Tr_ln_DK = float(d_tl['tracelog_DK'])  # 386.73 (half-spectrum)
Tr_ln_full = float(d_tl['tracelog_DK_full'])  # 773.46
orders_poly_to_log = -np.log10(tl_ratio)

print(f"\n  A. TRACE-LOG REPLACEMENT (W1-4)")
print(f"     Tr ln(D_K) (half) = {Tr_ln_DK:.2f}")
print(f"     Tr ln(D_K) (full) = {Tr_ln_full:.2f}")
print(f"     Ratio ln/poly = {tl_ratio:.4e}")
print(f"     Suppression: {orders_poly_to_log:.2f} orders")
print(f"     Source: s44_tracelog_cc.npz, key='ratio_logvspoly'")

# Geometric CC (post-transit, BCS contribution = 0)
rho_geometric = Tr_ln_full * M_KK4 / (16 * PI2)
gap_geometric = np.log10(rho_geometric / rho_obs)
print(f"\n     Post-transit geometric CC:")
print(f"     rho_geometric = |Tr ln(D_K)| * M_KK^4 / (16pi^2)")
print(f"     = {Tr_ln_full:.2f} * {M_KK4:.3e} / {16*PI2:.2f}")
print(f"     = {rho_geometric:.4e} GeV^4")
print(f"     Gap = {gap_geometric:.2f} orders")

# Factor B: EIH singlet projection (W2-3, EIH-GRAV-44)
# Only the (0,0) singlet gravitates in 4D (EIH effacement, 4.25 orders)
singlet_frac = float(d_eih['gate_ratio'])  # 5.684e-5
S_singlet = float(d_eih['S_singlet'])  # 14.23
orders_eih = -np.log10(singlet_frac)

print(f"\n  B. EIH SINGLET PROJECTION (W2-3)")
print(f"     S_singlet / S_fold = {singlet_frac:.4e}")
print(f"     S_singlet = {S_singlet:.2f}")
print(f"     Suppression: {orders_eih:.2f} orders")
print(f"     Source: s44_eih_grav.npz, key='gate_ratio'")
print(f"     Physics: Only (0,0) sector gravitates in 4D (EIH effacement)")
print(f"     tau-independent to 0.05% (verified at 16 tau values)")

# Factor C: Jacobson GGE energy (W5-1, JACOBSON-SPEC-44)
E_GGE = float(d_jac['E_GGE'])  # 1.688 M_KK
ratio_GGE_Sfold = float(d_jac['ratio_EGGE_Sfold'])
orders_jacobson = -np.log10(ratio_GGE_Sfold)

print(f"\n  C. JACOBSON GGE ENERGY (W5-1)")
print(f"     E_GGE = {E_GGE:.4f} M_KK")
print(f"     E_GGE / S_fold = {ratio_GGE_Sfold:.4e}")
print(f"     Suppression: {orders_jacobson:.2f} orders")
print(f"     Source: s44_jacobson_spec.npz, key='ratio_EGGE_Sfold'")
print(f"     Physics: GGE energy replaces spectral action at equilibrium")

# Factor D: Post-transit BCS = 0 (W1-4)
E_cond_old = 0.115  # S35
E_cond_new = float(d_tl['E_cond_MKK'])  # 0.137 (S40 correction: ED enhancement)
print(f"\n  D. BCS CONDENSATION ENERGY: ZERO POST-TRANSIT")
print(f"     E_cond (S35) = {E_cond_old:.3f} M_KK")
print(f"     E_cond (S40 corrected) = {E_cond_new:.3f} M_KK (ED-CONV-40: +18.9%)")
print(f"     Post-transit: condensate DESTROYED (P_exc = 1.000)")
print(f"     BCS contribution to CC = 0 exactly post-transit")

# ============================================================
# 5. E_COND IMPACT CHECK
# ============================================================
print("\n" + "=" * 80)
print("SECTION 5: E_cond Discrepancy Impact (0.115 vs 0.137)")
print("=" * 80)

# The trace-log CC is: |Tr ln(D_K^2/mu^2)| (the Casimir energy of the Dirac operator)
# The BCS condensation modifies this through:
#   delta_casimir = Casimir(paired) - Casimir(normal)
delta_casimir = float(d_tl['delta_casimir'])  # -1.94
casimir_normal = float(d_tl['casimir_normal'])  # -386.73
casimir_paired = float(d_tl['casimir_paired'])  # -388.67

print(f"\n  Casimir (normal)  = {casimir_normal:.2f}")
print(f"  Casimir (paired)  = {casimir_paired:.2f}")
print(f"  delta_Casimir     = {delta_casimir:.2f}")
print(f"  |delta/normal|    = {abs(delta_casimir/casimir_normal):.4e} = {abs(delta_casimir/casimir_normal)*100:.3f}%")

print(f"\n  E_cond changes 0.115 -> 0.137 (19% shift)")
print(f"  Impact on delta_Casimir: proportional to Delta^2, so delta_Casimir")
print(f"  would scale as (0.137/0.115)^2 * delta = {(E_cond_new/E_cond_old)**2 * delta_casimir:.2f}")
print(f"  vs normal Casimir = {casimir_normal:.2f}")
print(f"  Fractional change in CC = {abs((E_cond_new/E_cond_old)**2 * delta_casimir / casimir_normal):.4e}")
print(f"  => 0.7% effect on the trace-log CC. NEGLIGIBLE for gap counting.")
print(f"\n  POST-TRANSIT: BCS contribution = 0 anyway. E_cond irrelevant.")
print(f"  The E_cond discrepancy (0.115 vs 0.137) does NOT affect the CC gap.")

# ============================================================
# 6. INDEPENDENCE ANALYSIS & CHAIN STACKING
# ============================================================
print("\n" + "=" * 80)
print("SECTION 6: Suppression Chain (Independence Analysis)")
print("=" * 80)

print(f"\n  INDEPENDENCE MATRIX:")
print(f"    A (trace-log) and B (EIH singlet): INDEPENDENT")
print(f"      A = what functional to use (Volovik thermodynamic argument)")
print(f"      B = what sector gravitates (Peter-Weyl decomposition)")
print(f"    A and C (Jacobson): OVERLAPPING (both reweight the energy)")
print(f"    B and C: PARTIALLY OVERLAPPING (both involve sector projection)")

# Chain 1: trace-log + EIH (INDEPENDENT, stacks multiplicatively)
chain1 = tl_ratio * singlet_frac
orders_chain1 = -np.log10(chain1)
print(f"\n  CHAIN 1: trace-log x EIH singlet (independent)")
print(f"    = {tl_ratio:.4e} x {singlet_frac:.4e} = {chain1:.4e}")
print(f"    = {orders_chain1:.2f} orders of suppression")

# Chain 2: Jacobson + EIH (partially overlapping -- conservative)
chain2 = ratio_GGE_Sfold * singlet_frac
orders_chain2 = -np.log10(chain2)
print(f"\n  CHAIN 2: Jacobson x EIH singlet (partially overlapping)")
print(f"    = {ratio_GGE_Sfold:.4e} x {singlet_frac:.4e} = {chain2:.4e}")
print(f"    = {orders_chain2:.2f} orders of suppression")

# The HONEST combined suppression: trace-log x EIH
# This is the MAXIMUM justified suppression from independent factors
print(f"\n  HONEST COMBINED: {orders_chain1:.2f} orders (from independent chain 1)")

# ============================================================
# 7. DEFINITIVE TABLE
# ============================================================
print("\n" + "=" * 80)
print("SECTION 7: DEFINITIVE CC GAP TABLE")
print("=" * 80)

# Compute all values
stages = [
    ("M_Pl^4 (textbook)",
     rho_Pl, gap_Pl),
    ("M_KK^4 (bare, gravity route)",
     M_KK4, gap_bare),
    ("Spectral action polynomial",
     rho_spec, gap_spec),
    ("Trace-log geometric (post-transit)",
     rho_geometric, gap_geometric),
    ("+ EIH singlet projection",
     rho_geometric * singlet_frac,
     np.log10(rho_geometric * singlet_frac / rho_obs)),
    ("HONEST RESIDUAL",
     rho_geometric * singlet_frac,
     np.log10(rho_geometric * singlet_frac / rho_obs)),
]

# Print header
hdr = f"  {'Stage':<45s}  {'rho (GeV^4)':>14s}  {'Orders above obs':>18s}"
print(f"\n{hdr}")
print(f"  {'='*82}")
print(f"  {'Observed rho_Lambda':<45s}  {rho_obs:>14.4e}  {'0.00 (TARGET)':>18s}")
print(f"  {'':<45s}  {'':>14s}  {'':>18s}")

for name, rho, gap in stages:
    if name == "HONEST RESIDUAL":
        print(f"  {'-'*82}")
    print(f"  {name:<45s}  {rho:>14.4e}  {gap:>18.2f}")

# Additional: what the Kerner route would give
rho_spec_kerner = (2.0 / PI2) * a0 * M_KK_K**4
gap_spec_kerner = np.log10(rho_spec_kerner / rho_obs)
print(f"\n  {'--- FOR REFERENCE (Kerner M_KK) ---':<45s}")
print(f"  {'Spectral action (Kerner M_KK=5.04e17)':<45s}  {rho_spec_kerner:>14.4e}  {gap_spec_kerner:>18.2f}")

# The "bought" at each stage
print(f"\n  SUPPRESSION BREAKDOWN:")
print(f"    M_Pl -> M_KK: {gap_Pl - gap_bare:.2f} orders [(M_KK/M_Pl)^4 = {(M_KK/M_Pl)**4:.2e}]")
print(f"    Bare -> SA:   {gap_spec - gap_bare:+.2f} orders [mode counting x normalization]")
print(f"    SA -> trace-log: {orders_poly_to_log:.2f} orders [Volovik, correct functional]")
print(f"    trace-log -> + EIH: {orders_eih:.2f} orders [singlet projection]")
print(f"    TOTAL suppression from M_Pl^4: {gap_Pl - np.log10(rho_geometric * singlet_frac / rho_obs):.2f} orders")

# The honest number
residual_gap = np.log10(rho_geometric * singlet_frac / rho_obs)
print(f"\n  *** THE NUMBER: {residual_gap:.1f} orders ***")
print(f"  = {residual_gap:.2f} precisely")

# ============================================================
# 8. M_KK TENSION RESOLUTION
# ============================================================
print("\n" + "=" * 80)
print("SECTION 8: M_KK Tension Status")
print("=" * 80)

tension = np.log10(M_KK_K / M_KK_GN)
print(f"\n  M_KK_GN (gravity) = {M_KK_GN:.4e} GeV")
print(f"  M_KK_K (Kerner)   = {M_KK_K:.4e} GeV")
print(f"  Tension: {tension:.3f} decades")
print(f"\n  Vol(SU(3)) correction: DOES NOT AFFECT either M_KK value.")
print(f"  The wrong Vol(SU(3)) = 8880.9 enters M_star only.")
print(f"  Correcting Vol(SU(3)) to 1349.7:")
print(f"    M_star shifts by {(M_star_ratio-1)*100:.1f}%")
print(f"    M_KK_GN: UNCHANGED (derived from a_2 and M_Pl only)")
print(f"    M_KK_K:  UNCHANGED (derived from alpha_a and M_Pl only)")
print(f"\n  The 0.83-decade tension is REAL.")
print(f"  Resolution (SAKHAROV-GN-44): Both routes agree for G_N to factor 2.3")
print(f"  at effective cutoff Lambda_eff = 10*M_KK = 7.4e17 GeV.")
print(f"  The tension reflects the difference between:")
print(f"    - Route A: spectral zeta a_2 (sums 1/lambda^2 with multiplicities)")
print(f"    - Route B: Kerner metric g_aa (geometric, from Jensen metric eigenvalue)")
print(f"  These are different descriptions of the same one-loop physics,")
print(f"  agreeing for G_N (quadratic moment) but not for CC (quartic moment).")

# ============================================================
# 9. SUMMARY & PLOT
# ============================================================
print("\n" + "=" * 80)
print("SECTION 9: Summary")
print("=" * 80)

summary = f"""
The CC gap is {residual_gap:.1f} orders of magnitude.

Starting from M_Pl^4 (the textbook {gap_Pl:.1f}-order CC problem), the framework provides:
  - {gap_Pl - gap_bare:.1f} orders from M_KK << M_Pl (compactification scale hierarchy)
  - {orders_poly_to_log:.1f} orders from trace-log replacement (Volovik correct functional)
  - {orders_eih:.1f} orders from EIH singlet projection (only (0,0) gravitates)
  Total structural suppression: {gap_Pl - residual_gap:.1f} orders (of {gap_Pl:.1f} needed).

The M_KK tension was NOT an artifact of Vol(SU(3)). The wrong Vol (8880.9 vs 1349.7)
affects only M_star (higher-dimensional Planck mass), not M_KK or rho_Lambda. The
0.83-decade tension between gravity and Kerner routes is structural. However,
SAKHAROV-GN-44 showed that both routes agree for G_N to factor 2.3, validating the
M_KK = 7.43e16 GeV used here.

The E_cond discrepancy (0.115 vs 0.137) is irrelevant: post-transit BCS contribution
is exactly zero, and even during transit the effect is 0.7% of the trace-log Casimir.

The residual {residual_gap:.1f}-order gap is the standard hierarchy problem for the
framework: M_KK^4 vs rho_obs, reduced by ~{gap_Pl - residual_gap:.0f} orders of structural suppression.
"""
print(summary)

# ============================================================
# PLOT
# ============================================================
fig, ax = plt.subplots(1, 1, figsize=(10, 7))

labels = [
    r'$M_{\rm Pl}^4$ (textbook)',
    r'$M_{\rm KK}^4$ (bare)',
    r'Spectral action',
    r'Trace-log (post-transit)',
    r'+ EIH singlet',
]
gaps = [
    gap_Pl,
    gap_bare,
    gap_spec,
    gap_geometric,
    residual_gap,
]
colors = ['#cc3333', '#cc6633', '#cc9933', '#339933', '#336699']

bars = ax.barh(range(len(labels)), gaps, color=colors, edgecolor='black', linewidth=0.8)
ax.set_yticks(range(len(labels)))
ax.set_yticklabels(labels, fontsize=11)
ax.set_xlabel('Orders of magnitude above observed $\\rho_\\Lambda$', fontsize=12)
ax.set_title('CC Gap: Definitive Table (CC-GAP-RESOLVED-44)', fontsize=13, fontweight='bold')

# Add value annotations
for i, (bar, gap) in enumerate(zip(bars, gaps)):
    ax.text(gap + 1, i, f'{gap:.1f}', va='center', fontsize=10, fontweight='bold')

# Add the observed line
ax.axvline(x=0, color='green', linestyle='--', linewidth=2, label=r'$\rho_\Lambda^{\rm obs}$')

# Suppression annotations
ax.annotate('', xy=(gap_bare, 0.3), xytext=(gap_Pl, 0.3),
            arrowprops=dict(arrowstyle='<->', color='blue', lw=1.5))
ax.text((gap_Pl + gap_bare)/2, 0.5, f'{gap_Pl-gap_bare:.1f} orders\n(compactification)',
        ha='center', va='bottom', fontsize=8, color='blue')

ax.annotate('', xy=(residual_gap, 3.3), xytext=(gap_geometric, 3.3),
            arrowprops=dict(arrowstyle='<->', color='purple', lw=1.5))
ax.text((gap_geometric + residual_gap)/2, 3.5, f'{orders_eih:.1f} orders\n(EIH)',
        ha='center', va='bottom', fontsize=8, color='purple')

ax.set_xlim(-5, gap_Pl + 10)
ax.legend(fontsize=10, loc='upper right')
ax.grid(axis='x', alpha=0.3)
plt.tight_layout()
plt.savefig(DATA_DIR / 's44_cc_gap_resolved.png', dpi=150, bbox_inches='tight')
print(f"Plot saved: tier0-computation/s44_cc_gap_resolved.png")
plt.close()

# ============================================================
# SAVE DATA
# ============================================================
np.savez(DATA_DIR / 's44_cc_gap_resolved.npz',
    # Vol(SU(3)) audit
    Vol_SU3_wrong=Vol_wrong,
    Vol_SU3_correct=Vol_correct,
    Vol_ratio=ratio_vol,
    M_star_shift_pct=(M_star_ratio - 1) * 100,
    vol_affects_MKK=False,
    vol_affects_rho_Lambda=False,
    # M_KK values
    M_KK_GN=M_KK_GN,
    M_KK_K=M_KK_K,
    M_KK_tension_decades=tension,
    M_KK_used=M_KK,
    # Spectral data
    a0=a0, a2=a2, a4=a4, S_fold=S_fold,
    # Observed
    rho_obs=rho_obs,
    # Vacuum energy ladder
    rho_Pl=rho_Pl,
    rho_bare=M_KK4,
    rho_spec=rho_spec,
    rho_geometric=rho_geometric,
    rho_singlet=rho_geometric * singlet_frac,
    # Gap table
    gap_textbook=gap_Pl,
    gap_bare=gap_bare,
    gap_spectral=gap_spec,
    gap_geometric=gap_geometric,
    gap_residual=residual_gap,
    # Suppression factors
    tl_ratio=tl_ratio,
    singlet_frac=singlet_frac,
    orders_poly_to_log=orders_poly_to_log,
    orders_eih=orders_eih,
    orders_total_suppression=gap_Pl - residual_gap,
    # E_cond impact
    E_cond_old=E_cond_old,
    E_cond_new=E_cond_new,
    E_cond_CC_impact_pct=abs((E_cond_new/E_cond_old)**2 * delta_casimir / casimir_normal) * 100,
    # Independence
    chain1_orders=orders_chain1,
    chain2_orders=orders_chain2,
    # Gate
    gate_name='CC-GAP-RESOLVED-44',
    gate_verdict='INFO',
    gate_detail=f'Residual CC gap = {residual_gap:.1f} orders. Vol(SU(3)) error does not affect CC.',
)
print(f"Data saved: tier0-computation/s44_cc_gap_resolved.npz")

print(f"\n{'='*80}")
print(f"CC-GAP-RESOLVED-44: COMPLETE")
print(f"{'='*80}")
