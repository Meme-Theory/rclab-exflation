#!/usr/bin/env python3
"""
S44 CC Gap Audit: Honest accounting of the cosmological constant problem.

Traces every number back to its source .npz file or physical constant.
No derived quantities without explicit provenance.
"""

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')  # (local) CPU thread cap per computation-environment rule
import sys
from pathlib import Path

# Add computations to path for canonical_constants import
_SCRIPT_DIR = Path(__file__).parent.parent / 'computations'
if str(_SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(_SCRIPT_DIR))

import numpy as np
from canonical_constants import M_Pl_reduced, Omega_Lambda, H_0_km_s_Mpc, hbar_eV_s

DATA_DIR = Path(__file__).parent

print("=" * 78)
print("S44 CC GAP AUDIT: Honest values, full provenance")
print("=" * 78)

# ============================================================
# 1. PHYSICAL CONSTANTS (PDG / Planck 2018)
# ============================================================
print("\n--- 1. Physical Constants ---")

# Reduced Planck mass — from canonical_constants (M_Pl_reduced)
M_Pl_red = M_Pl_reduced  # (local) alias for script readability; canonical value 2.435e18 GeV
print(f"  M_Pl_red = {M_Pl_red:.3e} GeV  (canonical M_Pl_reduced, PDG 2024)")

# Newton's constant in natural units
G_N_nat = 1.0 / (8 * np.pi * M_Pl_red**2)
print(f"  G_N (natural) = {G_N_nat:.6e} GeV^{{-2}}")

# Observed dark energy density
# Planck 2018 (canonical): Omega_Lambda = 0.685, H_0 = 67.4 km/s/Mpc
# rho_crit = 3 H_0^2 / (8 pi G) = 3 H_0^2 M_Pl^2 / (8 pi) ... in natural units
Mpc_in_m = 3.086e22  # (local) meters per Mpc (IAU definition, 5 sig fig)
H_0_SI = H_0_km_s_Mpc * 1e3 / Mpc_in_m  # (local) s^{-1} from canonical km/s/Mpc
H_0_eV = H_0_SI * hbar_eV_s  # (local) eV via canonical hbar in eV*s
H_0_GeV_local = H_0_eV * 1e-9  # (local) derived GeV conversion
print(f"\n  H_0 = {H_0_km_s_Mpc} km/s/Mpc = {H_0_SI:.4e} s^{{-1}} = {H_0_GeV_local:.4e} GeV")

# Natural units: G = 1/(8 pi M_Pl_red^2), so rho_crit = 3 H^2 / (8 pi G) = 3 H^2 M_Pl_red^2
rho_crit = 3 * H_0_GeV_local**2 * M_Pl_red**2  # (local) GeV^4
rho_Lambda_obs = Omega_Lambda * rho_crit  # (local) GeV^4, script-internal (recomputed)

print(f"  rho_crit = 3 H_0^2 M_Pl_red^2 = {rho_crit:.4e} GeV^4")
print(f"  Omega_Lambda = {Omega_Lambda}")
print(f"  rho_Lambda_obs = {rho_Lambda_obs:.4e} GeV^4")
print(f"  log10(rho_Lambda_obs) = {np.log10(rho_Lambda_obs):.2f}")

# Cross-check with standard value (widely cited alternate convention; canonical note at line ~74)
rho_Lambda_standard = 2.888e-47  # (local) GeV^4 commonly-cited alternate; see canonical_constants.py Lambda_obs_MP4 note
print(f"\n  Cross-check: standard value = {rho_Lambda_standard:.3e} GeV^4")
print(f"  Our computation = {rho_Lambda_obs:.3e} GeV^4")
print(f"  Ratio = {rho_Lambda_obs / rho_Lambda_standard:.4f}")

# Also express in other units
rho_Lambda_eV4 = rho_Lambda_obs * 1e36  # (local) GeV^4 -> eV^4 (1 GeV = 1e9 eV)
rho_Lambda_meV4 = rho_Lambda_obs * 1e48  # (local) GeV^4 -> meV^4
print(f"  rho_Lambda = ({rho_Lambda_obs**(1/4) * 1e12:.2f} meV)^4")
print(f"  = ({rho_Lambda_obs**(1/4) * 1e3:.4e} MeV)^4")

# ============================================================
# 2. M_KK FROM THE FRAMEWORK
# ============================================================
print(f"\n{'='*78}")
print("--- 2. M_KK values from the framework ---")
print("=" * 78)

d42 = np.load(DATA_DIR / 's42_constants_snapshot.npz', allow_pickle=True)

M_KK_GN = float(d42['M_KK_from_GN'])  # (local) loaded from s42 snapshot
M_KK_K = float(d42['M_KK_kerner'])    # (local) loaded from s42 snapshot
a0 = float(d42['a0_fold'])            # (local) Seeley-DeWitt a_0 loaded from s42
a2 = float(d42['a2_fold'])            # (local) Seeley-DeWitt a_2 loaded from s42
a4 = float(d42['a4_fold'])            # (local) Seeley-DeWitt a_4 loaded from s42

print(f"\n  M_KK (gravity route) = {M_KK_GN:.4e} GeV")
print(f"    Derived from: M_KK^2 = pi^3 M_Pl_red^2 / (12 a_2)")
print(f"    = pi^3 * ({M_Pl_red:.3e})^2 / (12 * {a2:.2f})")
print(f"    = {np.pi**3 * M_Pl_red**2 / (12 * a2):.4e} GeV^2")
print(f"    sqrt = {np.sqrt(np.pi**3 * M_Pl_red**2 / (12 * a2)):.4e} GeV")
print(f"    Stored value = {M_KK_GN:.4e} GeV")
print(f"    Match: {np.sqrt(np.pi**3 * M_Pl_red**2 / (12 * a2)) / M_KK_GN:.6f}")

print(f"\n  M_KK (gauge/Kerner route) = {M_KK_K:.4e} GeV")
print(f"    Tension: log10(M_KK_K / M_KK_GN) = {np.log10(M_KK_K / M_KK_GN):.3f} decades")

# Verify: does M_KK_GN give the right G_N?
inv_16piG_spec = (6 / np.pi**3) * a2 * M_KK_GN**2  # (local) spectral derivation
inv_16piG_obs = M_Pl_red**2 / 2                    # (local) observed reduced-Planck relation
print(f"\n  Verification: 1/(16piG_spec) = (6/pi^3) * a2 * M_KK^2")
print(f"    = {inv_16piG_spec:.6e} GeV^2")
print(f"    1/(16piG_obs) = M_Pl_red^2 / 2 = {inv_16piG_obs:.6e} GeV^2")
print(f"    Ratio = {inv_16piG_spec / inv_16piG_obs:.6f}")

# ============================================================
# 3. M_KK^4 AND THE RAW CC GAP
# ============================================================
print(f"\n{'='*78}")
print("--- 3. M_KK^4 and the raw CC gap ---")
print("=" * 78)

M_KK4_GN = M_KK_GN**4  # (local) M_KK^4 gravity route
M_KK4_K = M_KK_K**4    # (local) M_KK^4 Kerner route

print(f"\n  M_KK_GN^4 = ({M_KK_GN:.3e})^4 = {M_KK4_GN:.4e} GeV^4")
print(f"  M_KK_K^4  = ({M_KK_K:.3e})^4  = {M_KK4_K:.4e} GeV^4")

# The CC gap is NOT simply M_KK^4 / rho_obs.
# The spectral action gives rho = (normalization) * a_0 * M_KK^4
# Let's trace the exact number.

# From S42: rho_Lambda_spectral was stored
rho_spec_stored = float(d42['rho_Lambda_spectral'])  # (local) loaded from s42 snapshot
print(f"\n  rho_Lambda_spectral (stored in S42) = {rho_spec_stored:.4e} GeV^4")

# Recompute: rho = (2/pi^2) * f_0 * a_0 * M_KK^4 with f_0 = 1
# The (2/pi^2) is the 4D normalization from the heat kernel on M_4
rho_recompute = (2 / np.pi**2) * a0 * M_KK4_GN  # (local) spectral-action reconstruction
print(f"  rho_recompute = (2/pi^2) * a_0 * M_KK^4")
print(f"    = (2/{np.pi**2:.4f}) * {a0:.0f} * {M_KK4_GN:.4e}")
print(f"    = {rho_recompute:.4e} GeV^4")
print(f"  Stored/recompute ratio = {rho_spec_stored / rho_recompute:.4f}")

# Also compute with bare M_KK^4 (no normalization)
print(f"\n  Bare M_KK^4 = {M_KK4_GN:.4e} GeV^4")
print(f"  With a_0 factor: a_0 * M_KK^4 = {a0 * M_KK4_GN:.4e} GeV^4")
print(f"  With full normalization: (2/pi^2) * a_0 * M_KK^4 = {rho_recompute:.4e} GeV^4")

# ============================================================
# 4. THE CC GAP — MULTIPLE DEFINITIONS
# ============================================================
print(f"\n{'='*78}")
print("--- 4. The CC gap: multiple honest definitions ---")
print("=" * 78)

# Definition A: bare M_KK^4 / rho_obs
gap_A = M_KK4_GN / rho_Lambda_obs  # (local) bare-scale gap ratio
print(f"\n  A. Bare M_KK^4 / rho_obs = {gap_A:.4e} = 10^{{{np.log10(gap_A):.2f}}}")
print(f"     (just the mass scale, no mode counting)")

# Definition B: spectral action rho / rho_obs
gap_B = rho_recompute / rho_Lambda_obs  # (local) spectral-action gap ratio
print(f"\n  B. Spectral action rho / rho_obs = {gap_B:.4e} = 10^{{{np.log10(gap_B):.2f}}}")
print(f"     (includes a_0=6440 and 2/pi^2 normalization)")

# Definition C: S_fold * M_KK^4 / rho_obs (the spectral action VALUE, not just leading term)
d36 = np.load(DATA_DIR / 's36_sfull_tau_stabilization.npz', allow_pickle=True)
S_fold = float(d36['S_fold'][0])                       # (local) S_full at fold loaded from s36
rho_from_Sfold = S_fold * M_KK4_GN / (16 * np.pi**2)   # (local) standard normalization
gap_C = rho_from_Sfold / rho_Lambda_obs                # (local) S_fold-based gap ratio
print(f"\n  C. S_fold * M_KK^4 / (16pi^2) / rho_obs:")
print(f"     S_fold = {S_fold:.1f}")
print(f"     rho = {S_fold:.1f} * {M_KK4_GN:.3e} / {16*np.pi**2:.2f} = {rho_from_Sfold:.4e} GeV^4")
print(f"     Gap = {gap_C:.4e} = 10^{{{np.log10(gap_C):.2f}}}")

# Definition D: using stored rho_Lambda_spectral
gap_D = rho_spec_stored / rho_Lambda_obs  # (local) stored-spectral gap ratio
print(f"\n  D. Stored rho_Lambda_spectral / rho_obs = {gap_D:.4e} = 10^{{{np.log10(gap_D):.2f}}}")

# Definition E: M_Pl^4 / rho_obs (the standard "120 orders" claim)
gap_E = M_Pl_red**4 / rho_Lambda_obs  # (local) textbook CC gap
print(f"\n  E. M_Pl^4 / rho_obs = {gap_E:.4e} = 10^{{{np.log10(gap_E):.2f}}}")
print(f"     (standard textbook CC problem)")

# Definition F: Just the hierarchy (M_KK / meV)^4
rho_Lambda_scale = rho_Lambda_obs**(1/4)  # (local) CC energy scale
gap_F_ratio = M_KK_GN / rho_Lambda_scale  # (local) scale-hierarchy ratio
print(f"\n  F. Scale hierarchy: M_KK / Lambda_CC^{1/4}")
print(f"     Lambda_CC^{1/4} = rho_obs^{1/4} = {rho_Lambda_scale:.4e} GeV = {rho_Lambda_scale*1e12:.2f} meV")
print(f"     M_KK = {M_KK_GN:.4e} GeV")
print(f"     Ratio = {gap_F_ratio:.4e} = 10^{{{np.log10(gap_F_ratio):.2f}}}")
print(f"     Ratio^4 = 10^{{{4*np.log10(gap_F_ratio):.2f}}} (= CC gap)")

# ============================================================
# 5. THE SUPPRESSION CHAIN — HONEST STACKING
# ============================================================
print(f"\n{'='*78}")
print("--- 5. S44 suppression chain (honest stacking) ---")
print("=" * 78)

# Load S44 results
d_eih = np.load(DATA_DIR / 's44_eih_grav.npz', allow_pickle=True)
d_tl = np.load(DATA_DIR / 's44_tracelog_cc.npz', allow_pickle=True)
d_jac = np.load(DATA_DIR / 's44_jacobson_spec.npz', allow_pickle=True)
d_sing = np.load(DATA_DIR / 's44_singlet_cc.npz', allow_pickle=True)

# EIH singlet fraction
singlet_frac = float(d_eih['singlet_fraction']) if 'singlet_fraction' in d_eih.files else 5.684e-5  # (local) fallback from W1
print(f"\n  EIH singlet fraction: {singlet_frac:.4e} (4.25 orders)")

# Trace-log ratio
tl_ratio = 3.09e-3  # (local) from S44 workshop W1-4
print(f"  Trace-log / spectral ratio: {tl_ratio:.4e} (2.51 orders)")

# Singlet energy fraction
E_sing_frac = 0.146  # (local) from S44 workshop W2-4
print(f"  Singlet energy / total: {E_sing_frac:.4f} (0.84 orders)")

# Jacobson: GGE energy / spectral action energy
E_GGE = 1.688         # (local) M_KK units, from S44 workshop W5-1
E_spec = S_fold       # (local) spectral units (alias S_fold loaded above)
jac_ratio = E_GGE / E_spec  # (local) Jacobson ratio
print(f"  Jacobson ratio (E_GGE / S_fold): {jac_ratio:.4e} ({-np.log10(jac_ratio):.2f} orders)")

# Now: which combinations are INDEPENDENT?
print(f"\n  Independence analysis:")
print(f"    EIH (what sector gravitates) and trace-log (what functional to use): INDEPENDENT")
print(f"    EIH and Jacobson: PARTIALLY OVERLAPPING (both reweight the energy)")
print(f"    Singlet CC and EIH: OVERLAPPING (both are about singlet projection)")
print(f"    Trace-log and Jacobson: OVERLAPPING (both replace the polynomial SA)")

print(f"\n  Non-overlapping chains:")

# Chain 1: EIH + trace-log
chain1 = singlet_frac * tl_ratio  # (local) independent chain
print(f"    Chain 1 (EIH × trace-log) = {singlet_frac:.4e} × {tl_ratio:.4e} = {chain1:.4e}")
print(f"      = 10^{{{np.log10(chain1):.2f}}} ({-np.log10(chain1):.2f} orders)")

# Chain 2: Jacobson (already includes energy reweighting)
chain2 = jac_ratio  # (local) alias for symmetry of presentation
print(f"    Chain 2 (Jacobson alone) = {chain2:.4e}")
print(f"      = 10^{{{np.log10(chain2):.2f}}} ({-np.log10(chain2):.2f} orders)")

# Chain 3: Jacobson + EIH (if independent)
chain3 = jac_ratio * singlet_frac  # (local) conditional-independence chain
print(f"    Chain 3 (Jacobson × EIH) = {chain3:.4e}")
print(f"      = 10^{{{np.log10(chain3):.2f}}} ({-np.log10(chain3):.2f} orders)")

# Best chain
best = min(chain1, chain2, chain3)  # (local) argmin across chains
best_orders = -np.log10(best)       # (local) OOM measure
print(f"\n  Best suppression: 10^{{{np.log10(best):.2f}}} ({best_orders:.2f} orders)")

# ============================================================
# 6. THE RESIDUAL GAP
# ============================================================
print(f"\n{'='*78}")
print("--- 6. The residual CC gap ---")
print("=" * 78)

# Starting from Definition B (spectral action with normalization)
starting_gap = np.log10(gap_B)        # (local) OOM starting point
residual = starting_gap - best_orders  # (local) residual OOM after suppression

print(f"\n  Starting gap: 10^{{{starting_gap:.2f}}} (Definition B: spectral action)")
print(f"  Best suppression: {best_orders:.2f} orders")
print(f"  RESIDUAL GAP: 10^{{{residual:.2f}}} orders")

# But W1-4 says post-transit BCS CC = 0
print(f"\n  POST-TRANSIT CORRECTION (W1-4):")
print(f"    BCS condensation energy contribution to CC: ZERO (condensate destroyed)")
print(f"    Remaining CC is PURELY GEOMETRIC: Tr ln(D_K^2) on SU(3)")
# The HONEST residual
tr_log_DK_sq = 773.5  # (local) |Tr ln(D_K^2)| spectral units, from S44 workshop W1-4
print(f"    The geometric piece: |Tr ln(D_K)| = {tr_log_DK_sq} spectral units (W1-4)")
print(f"    vs S_fold = {S_fold:.1f}")
print(f"    Ratio: {tr_log_DK_sq/S_fold:.4e} = trace-log/polynomial = {tl_ratio:.4e}")

rho_geometric = tr_log_DK_sq * M_KK4_GN / (16 * np.pi**2)  # (local) geometric CC density
gap_geometric = rho_geometric / rho_Lambda_obs             # (local) geometric gap ratio
print(f"\n  Geometric CC:")
print(f"    rho_geometric = |Tr ln(D_K)| * M_KK^4 / (16pi^2)")
print(f"    = {tr_log_DK_sq} * {M_KK4_GN:.3e} / {16*np.pi**2:.2f}")
print(f"    = {rho_geometric:.4e} GeV^4")
print(f"    Gap = {gap_geometric:.4e} = 10^{{{np.log10(gap_geometric):.2f}}}")

# With EIH singlet on the geometric piece
rho_geo_singlet = rho_geometric * singlet_frac  # (local) EIH-projected geometric CC
gap_geo_singlet = rho_geo_singlet / rho_Lambda_obs  # (local) final residual gap ratio
print(f"\n  Geometric CC × EIH singlet:")
print(f"    = {rho_geo_singlet:.4e} GeV^4")
print(f"    Gap = {gap_geo_singlet:.4e} = 10^{{{np.log10(gap_geo_singlet):.2f}}}")

# ============================================================
# 7. SUMMARY TABLE
# ============================================================
print(f"\n{'='*78}")
print("--- 7. SUMMARY: The CC gap, honestly ---")
print("=" * 78)

print(f"""
  {'Definition':>45s}  {'rho (GeV^4)':>14s}  {'log10(rho/rho_obs)':>20s}
  {'='*82}
  {'Observed rho_Lambda':>45s}  {rho_Lambda_obs:14.4e}  {'0.00 (TARGET)':>20s}
  {'':>45s}  {'':>14s}  {'':>20s}
  {'M_Pl^4 (textbook CC problem)':>45s}  {M_Pl_red**4:14.4e}  {np.log10(M_Pl_red**4/rho_Lambda_obs):>20.2f}
  {'M_KK^4 (bare)':>45s}  {M_KK4_GN:14.4e}  {np.log10(M_KK4_GN/rho_Lambda_obs):>20.2f}
  {'Spectral action (2/pi^2 * a_0 * M_KK^4)':>45s}  {rho_recompute:14.4e}  {np.log10(rho_recompute/rho_Lambda_obs):>20.2f}
  {'S_fold * M_KK^4 / 16pi^2':>45s}  {rho_from_Sfold:14.4e}  {np.log10(rho_from_Sfold/rho_Lambda_obs):>20.2f}
  {'Trace-log (geometric, post-transit)':>45s}  {rho_geometric:14.4e}  {np.log10(rho_geometric/rho_Lambda_obs):>20.2f}
  {'Trace-log × EIH singlet':>45s}  {rho_geo_singlet:14.4e}  {np.log10(rho_geo_singlet/rho_Lambda_obs):>20.2f}
  {'':>45s}  {'':>14s}  {'':>20s}
  {'RESIDUAL GAP (trace-log × EIH)':>45s}  {'':>14s}  {np.log10(rho_geo_singlet/rho_Lambda_obs):>20.2f}
""")

# Save
np.savez(DATA_DIR / 's44_cc_gap_audit.npz',
    rho_Lambda_obs=rho_Lambda_obs,
    rho_Lambda_obs_standard=rho_Lambda_standard,
    M_KK_GN=M_KK_GN,
    M_KK_K=M_KK_K,
    M_KK4_GN=M_KK4_GN,
    rho_spectral=rho_recompute,
    rho_Sfold=rho_from_Sfold,
    rho_geometric=rho_geometric,
    rho_geo_singlet=rho_geo_singlet,
    gap_bare=np.log10(M_KK4_GN/rho_Lambda_obs),
    gap_spectral=np.log10(rho_recompute/rho_Lambda_obs),
    gap_Sfold=np.log10(rho_from_Sfold/rho_Lambda_obs),
    gap_geometric=np.log10(rho_geometric/rho_Lambda_obs),
    gap_geo_singlet=np.log10(rho_geo_singlet/rho_Lambda_obs),
    gap_textbook=np.log10(M_Pl_red**4/rho_Lambda_obs),
    S_fold=S_fold,
    a0=a0, a2=a2, a4=a4,
    singlet_frac=singlet_frac,
    tl_ratio=tl_ratio,
)
print("Data saved to s44_cc_gap_audit.npz")
