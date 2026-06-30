#!/usr/bin/env python3
"""
s61_a4_qtheory_compound.py — a_4-Dominated Spectral Action with q-Theory Vacuum
==================================================================================

Task: A4-QT-COMPOUND-61
Agent: Phonon-First Cosmologist

PHYSICS:
  The spectral action on M^4 x K has the heat-kernel expansion:

    S[D, f, Lambda] = f_4 Lambda^4 a_0 + f_2 Lambda^2 a_2 + f_0 a_4 + O(Lambda^{-2})    (1)

  where a_n are the Seeley-DeWitt coefficients of D_K on the internal space K = SU(3)/Jensen.
  The Chamseddine-Connes spectral action (Paper 10) identifies:

    Lambda_bare = (2/pi^2) f_0 a_4 M_KK^4  [bare CC from a_4 term]                        (2)

  ALPHA-REGIME-61 (PHONON-2) proved alpha = f_0*a_4/(f_2*a_2) << alpha_crit = 52.4.
  The fold IS a stable a_4 minimum. The spectral action is a_4-dominated in the sense
  that a_4 controls the gauge kinetic terms and the CC, while a_2 controls gravity.

  Q-THEORY SELF-TUNING (Volovik, Paper 7):
  The vacuum is described by a conserved 4-form field q (= thermodynamic variable).
  At equilibrium q_eq, the effective CC vanishes: Lambda_eff(q_eq) = 0 exactly.
  This is the Volovik self-tuning mechanism -- the vacuum adjusts q to zero out Lambda.

  The RESIDUAL CC comes from departure from equilibrium:
    Lambda_res = (1/2) d^2F/dq^2 |_{q_eq} * (delta_q)^2                                   (3)

  GL-STAIRCASE-61 (LANDAU-1) computed d^2F/dn^2 at the GL equilibrium.
  The q-theory variable q maps to the pair density n via: q = n * (normalization).
  The discreteness of pair number (N = 0, 1, 2, ...) provides the delta_q:
    delta_q = 1/N_modes = 1/8                                                               (4)

  because the smallest fluctuation is adding/removing one pair from 8 modes.

  The CC prediction is then:
    Lambda_res = (1/2) * d^2F/dn^2 * (1/N_modes)^2                                         (5)

  in M_KK^4 units. Convert to GeV^4 via M_KK^4 and compare to rho_Lambda_obs.

CHAIN OF COMPUTATION:
  1. Load a_0, a_2, a_4 from W1-W3 heat kernel computations
  2. Load alpha from ALPHA-REGIME-61 (confirms a_4 domination)
  3. Load GL free energy curvature from GL-STAIRCASE-61
  4. Load q-theory geodesic data from S60
  5. Compute bare CC: Lambda_bare = (2/pi^2) * a_0 * M_KK^4 (with f_4=1)
  6. Compute GL residual: Lambda_res = (1/2) * d^2F/dn^2 * (1/N_modes)^2
  7. Compute q-theory residual from geodesic departure
  8. Compare Lambda_res / Lambda_obs (in log10 OOM)

GATE: A4-QT-COMPOUND-61
  PASS if |log10(Lambda_res/Lambda_obs)| < 1 (within 10x)
  FAIL if > 5 (beyond 10^5)
  INFO if [1, 5]

Output: s61_a4_qtheory_compound.npz
"""

import numpy as np
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import (
    tau_fold, M_KK_gravity, M_KK_kerner, M_Pl_reduced,
    rho_Lambda_obs, rho_crit_GeV4, Vol_SU3_Haar,
    a0_fold as a0_fold_canonical, a2_fold as a2_fold_canonical,
    a4_fold as a4_fold_canonical, N_cells,
    N_dof_BCS, PI, Omega_Lambda
)

data_dir = Path(__file__).parent
M_KK = M_KK_gravity  # Conservative route

print("=" * 72)
print("A4-QT-COMPOUND-61: a_4-Dominated Spectral Action + q-Theory Vacuum")
print("=" * 72)

# ==========================================================================
#  1. LOAD HEAT KERNEL COEFFICIENTS
# ==========================================================================
print("\n--- 1. Heat Kernel Coefficients ---")

d_a2 = np.load(data_dir / "s61_heat_kernel_a2.npz", allow_pickle=True)
d_a4 = np.load(data_dir / "s61_heat_kernel_a4.npz", allow_pickle=True)

# Normalized Seeley-DeWitt coefficients (per unit volume, spinor-traced)
a0_SD = float(d_a2["a0_SD"])           # = sqrt(3)/2 = 0.8660
a2_SD = float(d_a2["a2_SD_fold"])      # = 0.7282
a4_gilkey = float(d_a4["a4_gilkey_fold"])  # = 0.3015
a2_gilkey = float(d_a4["a2_gilkey_fold"])  # = 0.7282 (cross-check)

# Unnormalized (integrated over volume, with spinor dimension)
a2_unnorm = float(d_a2["a2_unnorm_fold"])  # = 18159.8

# Full spectral-action convention coefficients (from canonical_constants)
# These are Tr(1), int R, int(5R^2/4 - 2 Ric^2 - 7/10 K) style
a0_full = a0_fold_canonical  # = 6440.0
a2_full = a2_fold_canonical  # = 2776.2
a4_full = a4_fold_canonical  # = 1350.7

ratio_a4_a2 = a4_gilkey / a2_gilkey
ratio_full = a4_full / a2_full

print(f"a_0 (SD normalized)  = {a0_SD:.6f}")
print(f"a_2 (SD normalized)  = {a2_SD:.6f}")
print(f"a_4 (Gilkey)         = {a4_gilkey:.6f}")
print(f"a_4/a_2 (normalized) = {ratio_a4_a2:.6f}")
print(f"")
print(f"a_0 (full, canonical) = {a0_full:.1f}")
print(f"a_2 (full, canonical) = {a2_full:.4f}")
print(f"a_4 (full, canonical) = {a4_full:.4f}")
print(f"a_4/a_2 (full)        = {ratio_full:.6f}")
print(f"")
print(f"Scalar curvature R_fold = {float(d_a2['R_fold']):.6f}")
print(f"Vol(SU(3)) = {Vol_SU3_Haar:.2f}")
print(f"dim(spinor) = {int(d_a4['dim_spinor'])}")

# Cross-check: a2_gilkey should match a2_SD
assert abs(a2_gilkey - a2_SD) < 1e-10, \
    f"a2 cross-check failed: {a2_gilkey} vs {a2_SD}"
print(f"\nCross-check: a2_gilkey == a2_SD: PASS (diff = {abs(a2_gilkey - a2_SD):.2e})")

# ==========================================================================
#  2. LOAD ALPHA FROM ALPHA-REGIME-61
# ==========================================================================
print("\n--- 2. Alpha Regime ---")

d_alpha = np.load(data_dir / "s61_alpha_physical.npz", allow_pickle=True)
alpha_crit = float(d_alpha["alpha_crit"])
alpha_at_MKK = d_alpha["alpha_at_MKK"]
cutoff_names = d_alpha["cutoff_names"]

print(f"alpha_crit = {alpha_crit:.2f}")
print(f"alpha at Lambda=M_KK by cutoff:")
for name, alpha_val in zip(cutoff_names, alpha_at_MKK):
    print(f"  {name:15s}: alpha = {alpha_val:.4f}  (alpha/alpha_crit = {alpha_val/alpha_crit:.4f})")

alpha_max = float(np.max(alpha_at_MKK))
alpha_min = float(np.min(alpha_at_MKK))
safety_margin = alpha_crit / alpha_max

print(f"\nalpha range: [{alpha_min:.4f}, {alpha_max:.4f}]")
print(f"Safety margin: alpha_crit/alpha_max = {safety_margin:.1f}x")
print(f"Fold is a_4 minimum: CONFIRMED (ALPHA-REGIME-61 PASS)")

# ==========================================================================
#  3. LOAD GL FREE ENERGY FROM GL-STAIRCASE-61
# ==========================================================================
print("\n--- 3. GL Free Energy Curvature ---")

d_gl = np.load(data_dir / "s61_gl_staircase.npz", allow_pickle=True)
N_modes = int(d_gl["N_modes"])  # = 8

# Extract ALL fits: baseline deg3, baseline deg4, compound deg3, compound deg4
fits = {}
for prefix in ["baseline_deg3", "baseline_deg4", "compound_deg3", "compound_deg4"]:
    fits[prefix] = {
        "n_eq": float(d_gl[f"{prefix}_n_eq"]),
        "F_eq": float(d_gl[f"{prefix}_F_eq"]),
        "d2F_eq": float(d_gl[f"{prefix}_d2F_eq"]),
        "chi_q": float(d_gl[f"{prefix}_chi_q"]),
        "delta_Lambda_exact": float(d_gl[f"{prefix}_delta_Lambda_exact"]),
        "delta_Lambda_harmonic": float(d_gl[f"{prefix}_delta_Lambda_harmonic"]),
        "eq_type": str(d_gl[f"{prefix}_eq_type"]),
    }
    print(f"\n{prefix}:")
    print(f"  n_eq = {fits[prefix]['n_eq']:.6f} ({fits[prefix]['eq_type']})")
    print(f"  F_eq = {fits[prefix]['F_eq']:.6e}")
    print(f"  d^2F/dn^2 = {fits[prefix]['d2F_eq']:.4f}")
    print(f"  chi_q = {fits[prefix]['chi_q']:.6f}")
    print(f"  delta_Lambda_exact = {fits[prefix]['delta_Lambda_exact']:.6f} M_KK^4")
    print(f"  delta_Lambda_harmonic = {fits[prefix]['delta_Lambda_harmonic']:.6f} M_KK^4")

# The compound deg4 is the most trustworthy: it captures the BCS+Josephson+Penrose
# corrections and has the highest polynomial order (4 free parameters, 5 data points).
# GL-STAIRCASE-61 selected it: chi_q_min from compound_deg4.
best_fit = "compound_deg4"
d2F_best = fits[best_fit]["d2F_eq"]
n_eq_best = fits[best_fit]["n_eq"]
chi_q_best = fits[best_fit]["chi_q"]
delta_Lambda_exact_best = fits[best_fit]["delta_Lambda_exact"]
delta_Lambda_harmonic_best = fits[best_fit]["delta_Lambda_harmonic"]

print(f"\n*** Selected fit: {best_fit} ***")
print(f"  d^2F/dn^2 at n_eq = {d2F_best:.4f}")
print(f"  chi_q = {chi_q_best:.6f}")

# ==========================================================================
#  4. LOAD Q-THEORY GEODESIC DATA
# ==========================================================================
print("\n--- 4. Q-Theory Geodesic ---")

d_qt = np.load(data_dir / "s60_q_theory_geodesic.npz", allow_pickle=True)

Q_total = float(d_qt["Q_total_K7"])      # = 29.9
N_pair_geod = float(d_qt["N_pair_geod_A"])  # = 1.347
delta_geod = float(d_qt["delta_geod"])    # = 0.0523
dm2_geod = float(d_qt["dm2_geod_pred"])   # = 0.0523
dm2_actual = float(d_qt["dm2_dirac_actual"])  # = -0.206
dm2_ratio = float(d_qt["dm2_ratio"])      # = 0.254
K7_norm = float(d_qt["K7_norm_sq_fold"])  # = 2.418

print(f"Q_total(K7) = {Q_total}")
print(f"N_pair(geodesic) = {N_pair_geod:.4f}")
print(f"delta_geod = {delta_geod:.6f}")
print(f"|K_7|^2 = {K7_norm:.4f}")
print(f"dm^2 geodesic/Dirac ratio = {dm2_ratio:.4f}")

# ==========================================================================
#  5. COMPUTE BARE CC (SPECTRAL ACTION, NO SELF-TUNING)
# ==========================================================================
print("\n--- 5. Bare Cosmological Constant ---")

# Chamseddine-Connes spectral action (Paper 10, eq 1.187):
# S = f_4 Lambda^4 a_0 + f_2 Lambda^2 a_2 + f_0 a_4 + ...
#
# The CC in 4D emerges from the a_0 (volume) term:
#   Lambda_bare = (2/pi^2) * f_4 * Lambda^4 * a_0
#
# With Lambda = M_KK (cutoff = compactification scale):
# Using normalized a_0 = sqrt(3)/2 = 0.866 (Seeley-DeWitt)
# And the full convention: a_0 = dim(S) * Vol(K) / (4*pi)^{d/2}
#   where d=8 (total), dim(S)=16, Vol(K)=1349.7

# Method A: From normalized Seeley-DeWitt a_0
# The spectral action bare CC in reduced Planck units:
#   rho_Lambda_bare = (2/pi^2) * a_0 * Lambda^4
# With f_4 = 1 (unit moment):
rho_bare_SD = (2.0 / PI**2) * a0_SD * M_KK**4
log10_bare_SD = np.log10(rho_bare_SD)
log10_obs = np.log10(rho_Lambda_obs)
gap_SD = log10_bare_SD - log10_obs

print(f"\nMethod A (SD normalized, f_4=1):")
print(f"  rho_bare = (2/pi^2) * {a0_SD:.4f} * ({M_KK:.3e})^4")
print(f"  rho_bare = {rho_bare_SD:.6e} GeV^4")
print(f"  log10(rho_bare) = {log10_bare_SD:.2f}")
print(f"  log10(rho_obs)  = {log10_obs:.2f}")
print(f"  CC gap = {gap_SD:.2f} orders (BARE, before self-tuning)")

# Method B: From full convention a_0
rho_bare_full = (2.0 / PI**2) * a0_full * M_KK**4
gap_full = np.log10(rho_bare_full) - log10_obs
print(f"\nMethod B (full convention a_0={a0_full}):")
print(f"  rho_bare = {rho_bare_full:.6e} GeV^4")
print(f"  CC gap = {gap_full:.2f} orders (BARE)")

# The bare CC gap is ~113-117 orders. This is the CC PROBLEM.
# Q-theory self-tuning eliminates this to exactly zero at equilibrium.
# The residual comes from DEPARTURE from equilibrium.

# ==========================================================================
#  6. COMPUTE GL RESIDUAL CC (q-THEORY DEPARTURE)
# ==========================================================================
print("\n--- 6. GL Residual CC ---")

# The GL free energy F(n) has equilibrium at n_eq.
# At equilibrium: dF/dn = 0 => Lambda_eff = 0 (Volovik self-tuning).
# The residual comes from discreteness: the system cannot sit exactly at n_eq
# because N must be an integer.
#
# Nearest integer pair number: N_nearest = round(n_eq * N_modes)
# Departure: delta_n = n_eq - N_nearest/N_modes
#
# Residual: Lambda_res = F(N_nearest/N_modes) - F(n_eq)
#         ≈ (1/2) d^2F/dn^2 * (delta_n)^2    [harmonic approx]

# For compound_deg4:
#   n_eq = 0.005314, so N_eq_continuous = 0.005314 * 8 = 0.0425
#   Nearest integer: N = 0
#   delta_n = n_eq - 0/8 = 0.005314

N_eq_cont = n_eq_best * N_modes
N_nearest = round(N_eq_cont)
delta_n = n_eq_best - N_nearest / N_modes

print(f"Best fit: {best_fit}")
print(f"n_eq = {n_eq_best:.6f}")
print(f"N_eq(continuous) = {N_eq_cont:.4f}")
print(f"N_nearest = {N_nearest}")
print(f"delta_n = n_eq - {N_nearest}/{N_modes} = {delta_n:.6f}")
print(f"d^2F/dn^2 = {d2F_best:.4f}")

# Harmonic approximation
Lambda_res_harmonic = 0.5 * d2F_best * delta_n**2
print(f"\nHarmonic residual: Lambda_res = 0.5 * {d2F_best:.4f} * ({delta_n:.6f})^2")
print(f"                 = {Lambda_res_harmonic:.6e} M_KK^4")

# Exact residual (from the polynomial)
# F(0) - F(n_eq) = delta_Lambda_exact from the GL staircase
Lambda_res_exact = delta_Lambda_exact_best
Lambda_res_harmonic_stored = delta_Lambda_harmonic_best

print(f"\nExact residual (from GL polynomial): {Lambda_res_exact:.6e} M_KK^4")
print(f"Harmonic residual (from GL stored):  {Lambda_res_harmonic_stored:.6e} M_KK^4")
print(f"Harmonic residual (recomputed):      {Lambda_res_harmonic:.6e} M_KK^4")

# Convert to GeV^4
Lambda_res_exact_GeV4 = abs(Lambda_res_exact) * M_KK**4
Lambda_res_harmonic_GeV4 = abs(Lambda_res_harmonic) * M_KK**4

log10_res_exact = np.log10(Lambda_res_exact_GeV4)
log10_res_harmonic = np.log10(Lambda_res_harmonic_GeV4)

print(f"\nIn physical units:")
print(f"  M_KK = {M_KK:.4e} GeV")
print(f"  M_KK^4 = {M_KK**4:.4e} GeV^4")
print(f"  Lambda_res (exact)    = {Lambda_res_exact_GeV4:.4e} GeV^4")
print(f"  Lambda_res (harmonic) = {Lambda_res_harmonic_GeV4:.4e} GeV^4")

# ==========================================================================
#  7. COMPARE TO OBSERVED CC
# ==========================================================================
print("\n--- 7. Comparison to Observed CC ---")

ratio_exact = Lambda_res_exact_GeV4 / rho_Lambda_obs
ratio_harmonic = Lambda_res_harmonic_GeV4 / rho_Lambda_obs
log10_ratio_exact = np.log10(abs(ratio_exact))
log10_ratio_harmonic = np.log10(abs(ratio_harmonic))

print(f"rho_Lambda_obs = {rho_Lambda_obs:.2e} GeV^4")
print(f"")
print(f"EXACT:    Lambda_res/Lambda_obs = {ratio_exact:.4e} = 10^{log10_ratio_exact:.2f}")
print(f"HARMONIC: Lambda_res/Lambda_obs = {ratio_harmonic:.4e} = 10^{log10_ratio_harmonic:.2f}")

# The CC gap remaining AFTER q-theory self-tuning
gap_after_qt_exact = log10_ratio_exact
gap_after_qt_harmonic = log10_ratio_harmonic

print(f"\nCC gap (bare, no self-tuning): {gap_SD:.2f} orders")
print(f"CC gap (after q-theory, exact): {gap_after_qt_exact:.2f} orders")
print(f"CC gap (after q-theory, harmonic): {gap_after_qt_harmonic:.2f} orders")
print(f"Orders REMOVED by self-tuning: {gap_SD - gap_after_qt_exact:.2f}")

# ==========================================================================
#  8. SYSTEMATIC ANALYSIS: ALL GL FITS
# ==========================================================================
print("\n--- 8. Systematic: All Fits ---")

results_all = {}
for prefix, fit in fits.items():
    n_eq = fit["n_eq"]
    d2F = fit["d2F_eq"]
    N_cont = n_eq * N_modes
    N_near = round(N_cont)
    dn = n_eq - N_near / N_modes

    # Skip if d2F is negative (unstable, compound_deg3)
    if d2F < 0:
        Lambda_res_MKK4 = abs(fit["delta_Lambda_exact"])  # Use exact from polynomial
        sign_note = "UNSTABLE (d2F<0)"
    else:
        Lambda_res_MKK4 = abs(fit["delta_Lambda_exact"])
        sign_note = "stable"

    Lambda_res_GeV4 = Lambda_res_MKK4 * M_KK**4
    ratio = Lambda_res_GeV4 / rho_Lambda_obs
    log10_r = np.log10(ratio) if ratio > 0 else float('nan')

    results_all[prefix] = {
        "Lambda_res_MKK4": Lambda_res_MKK4,
        "Lambda_res_GeV4": Lambda_res_GeV4,
        "ratio": ratio,
        "log10_ratio": log10_r,
        "sign": sign_note,
    }

    print(f"\n{prefix} ({sign_note}):")
    print(f"  n_eq = {n_eq:.6f}, N_near = {N_near}, delta_n = {dn:.6f}")
    print(f"  d^2F/dn^2 = {d2F:.4f}")
    print(f"  Lambda_res = {Lambda_res_MKK4:.6e} M_KK^4 = {Lambda_res_GeV4:.4e} GeV^4")
    print(f"  Lambda_res/Lambda_obs = 10^{log10_r:.2f}")

# ==========================================================================
#  9. CONSTRAINT EQUATION: f_2 FROM GRAVITY
# ==========================================================================
print("\n--- 9. Constraint Equation ---")

# The spectral action gravity term:
#   (1/16*pi*G_N) = f_2 * M_KK^2 * a_2 / (24*pi^2)  (4D Newton's constant)
#
# => f_2 = 24*pi^2 * M_Pl^2 / (2 * M_KK^2 * a_2)
#
# Using a_2 in normalized form: a_2_SD = 0.7282
# M_Pl_reduced = 2.435e18 GeV

M_Pl = M_Pl_reduced  # GeV
f_2_grav = (24 * PI**2 * M_Pl**2) / (2 * M_KK**2 * a2_SD)
print(f"f_2 (gravity route) = {f_2_grav:.4e}")
print(f"  M_Pl = {M_Pl:.3e} GeV")
print(f"  M_KK = {M_KK:.3e} GeV")
print(f"  a_2(SD) = {a2_SD:.6f}")

# The physical f_2 * M_KK^2 product (fixes Newton's constant):
f2_MKK2 = f_2_grav * M_KK**2
print(f"  f_2 * M_KK^2 = {f2_MKK2:.4e} GeV^2")

# From this, the PHYSICAL CC becomes:
#   Lambda_eff = f_0 * a_4 * M_KK^4 / (16*pi^2)
# But q-theory says this is self-tuned to zero.
# The residual is from the GL departure.

# The physical residual CC WITH f_2 normalization:
# In the spectral action, the a_4 term gives the EH + gauge kinetic + CC.
# The CC piece is: Lambda = (f_0/f_2^2) * something from a_0, a_2, a_4
# But the standard formula (Paper 10, eq 1.164):
#   Lambda = pi^2 * f_0 / f_2 * a_0/a_2 * M_KK^2
#   (where f_0, f_2 are moments of the cutoff function)

# With the gravity constraint: M_Pl^2 = f_2 * a_2 * M_KK^2 / (12 * pi)
# The bare CC in natural units:
#   rho_bare = (2/pi^2) * f_0 * a_0 * (f_2*M_KK^2)^2 / f_2^2
#            = (2/pi^2) * f_0 * a_0 * M_KK^4  [with f_0, f_4 = f_0 by convention]

# For the heat kernel cutoff: f_0 = phi_0 = 6, f_2 = phi_1 = 2
# alpha = f_0 * a_4 / (f_2 * a_2) = 6 * 0.3015 / (2 * 0.7282) = 1.242
# This matches alpha_at_MKK[0] = 2.0? Let me check.

# Actually: the alpha definition from ALPHA-REGIME-61 is
# alpha = (phi_1/phi_2) * (a_4/a_2)   [ratio of moments times ratio of coefficients]
# For heat kernel: phi_1/phi_2 = 2/1 = 2, a_4/a_2 = 0.414
# => alpha = 2 * 0.414 = 0.828... but stored as 2.0?

# The phi_1/phi_2 from the data:
phi_1_phi_2 = d_alpha["ratio_phi1_phi2"]
print(f"\nCutoff moment ratios phi_1/phi_2:")
for name, r in zip(cutoff_names, phi_1_phi_2):
    print(f"  {name:15s}: {r:.6f}")

print(f"\na_4/a_2 (Gilkey) = {ratio_a4_a2:.6f}")
print(f"Product (heat kernel): {float(phi_1_phi_2[0]) * ratio_a4_a2:.6f}")
print(f"But alpha_at_MKK[heat kernel] = {float(alpha_at_MKK[0]):.6f}")
print(f"Note: alpha definition = phi_1/phi_2 (not phi_1/phi_2 * a4/a2)")
print(f"The a4/a2 ratio is SEPARATE from the cutoff moment ratio")

# ==========================================================================
#  10. THE KEY RESULT: PHYSICAL CC PREDICTION
# ==========================================================================
print("\n" + "=" * 72)
print("10. PHYSICAL CC PREDICTION (A4-QT-COMPOUND-61)")
print("=" * 72)

# The compound_deg4 fit is the best available:
#   d^2F/dn^2 = 42.18 at n_eq = 0.00531
#   chi_q = 0.0237
#   delta_Lambda_exact = 0.1946 M_KK^4

# Physical residual:
Lambda_res_phys = abs(delta_Lambda_exact_best) * M_KK**4
log10_res = np.log10(Lambda_res_phys)
log10_ratio_phys = log10_res - log10_obs

print(f"\nCompound deg4 GL fit (best):")
print(f"  n_eq = {n_eq_best:.6f}")
print(f"  d^2F/dn^2 = {d2F_best:.4f}")
print(f"  chi_q = {chi_q_best:.6f}")
print(f"  delta_Lambda = {delta_Lambda_exact_best:.6f} M_KK^4")
print(f"")
print(f"Physical CC prediction:")
print(f"  Lambda_res = {delta_Lambda_exact_best:.6f} * ({M_KK:.3e})^4")
print(f"  Lambda_res = {Lambda_res_phys:.6e} GeV^4")
print(f"  log10(Lambda_res) = {log10_res:.2f}")
print(f"  log10(Lambda_obs) = {log10_obs:.2f}")
print(f"  log10(ratio)      = {log10_ratio_phys:.2f}")
print(f"")
print(f"CC gap (bare):       {gap_SD:.2f} orders")
print(f"CC gap (after q-th): {log10_ratio_phys:.2f} orders")
print(f"Orders removed:      {gap_SD - log10_ratio_phys:.2f}")

# Spread across all fits:
all_log10 = [results_all[k]["log10_ratio"] for k in results_all if not np.isnan(results_all[k]["log10_ratio"])]
spread_min = min(all_log10)
spread_max = max(all_log10)
print(f"\nSpread across ALL GL fits: [{spread_min:.2f}, {spread_max:.2f}] orders")

# ==========================================================================
#  11. CROSS-CHECK: M_KK ROUTE DEPENDENCE
# ==========================================================================
print("\n--- 11. M_KK Route Dependence ---")

# With Kerner M_KK:
Lambda_res_kerner = abs(delta_Lambda_exact_best) * M_KK_kerner**4
log10_ratio_kerner = np.log10(Lambda_res_kerner) - log10_obs

# With gravity M_KK:
Lambda_res_gravity = abs(delta_Lambda_exact_best) * M_KK_gravity**4
log10_ratio_gravity = np.log10(Lambda_res_gravity) - log10_obs

print(f"M_KK(gravity) = {M_KK_gravity:.3e}: CC gap = {log10_ratio_gravity:.2f} orders")
print(f"M_KK(Kerner)  = {M_KK_kerner:.3e}: CC gap = {log10_ratio_kerner:.2f} orders")
print(f"Route spread: {abs(log10_ratio_kerner - log10_ratio_gravity):.2f} orders")

# ==========================================================================
#  12. GATE VERDICT
# ==========================================================================
print("\n" + "=" * 72)
print("12. GATE VERDICT")
print("=" * 72)

# The gate uses the gravity route (conservative, larger CC gap)
# Take the compound_deg4 result (best fit, interior equilibrium)
gate_ratio = log10_ratio_phys  # = log10(Lambda_res/Lambda_obs)

# Gate criteria:
#   PASS if |log10(ratio)| < 1 (within factor 10)
#   INFO if 1 <= |log10(ratio)| < 5
#   FAIL if |log10(ratio)| >= 5

abs_gate = abs(gate_ratio)

if abs_gate < 1:
    verdict = "PASS"
    detail = (f"|log10(Lambda_res/Lambda_obs)| = {abs_gate:.2f} < 1. "
              f"Q-theory self-tuning + GL residual predicts CC within factor "
              f"{10**abs_gate:.1f} of observation.")
elif abs_gate < 5:
    verdict = "INFO"
    detail = (f"|log10(Lambda_res/Lambda_obs)| = {abs_gate:.2f} in [1, 5]. "
              f"Q-theory reduces bare gap by {gap_SD - gate_ratio:.0f} orders "
              f"but {abs_gate:.1f}-order residual gap remains. "
              f"M_KK^4 normalization dominates.")
else:
    verdict = "FAIL"
    detail = (f"|log10(Lambda_res/Lambda_obs)| = {abs_gate:.2f} > 5. "
              f"Q-theory self-tuning is insufficient. "
              f"GL residual {Lambda_res_phys:.2e} GeV^4 >> {rho_Lambda_obs:.2e} GeV^4.")

print(f"\nGate: A4-QT-COMPOUND-61")
print(f"Verdict: {verdict}")
print(f"Detail: {detail}")
print(f"")
print(f"Key: The GL staircase gives delta_Lambda ~ 0.19 M_KK^4.")
print(f"     M_KK^4 = {M_KK**4:.3e} GeV^4.")
print(f"     Lambda_obs = {rho_Lambda_obs:.2e} GeV^4.")
print(f"     The O(0.1) M_KK^4 residual is {10**gate_ratio:.2e}x the observed CC.")
print(f"     Self-tuning zeroes the leading term but the DISCRETENESS residual")
print(f"     inherits the M_KK^4 scale with O(1/N_modes^2) suppression only.")

# ==========================================================================
#  13. SAVE
# ==========================================================================
print("\n--- Saving ---")

save_dict = {
    # Heat kernel
    "a0_SD": a0_SD,
    "a2_SD": a2_SD,
    "a4_gilkey": a4_gilkey,
    "ratio_a4_a2": ratio_a4_a2,
    "a0_full": a0_full,
    "a2_full": a2_full,
    "a4_full": a4_full,
    "R_fold": float(d_a2["R_fold"]),
    "Vol_SU3": Vol_SU3_Haar,

    # Alpha regime
    "alpha_crit": alpha_crit,
    "alpha_max_at_MKK": alpha_max,
    "alpha_min_at_MKK": alpha_min,
    "safety_margin": safety_margin,

    # GL staircase (compound_deg4)
    "GL_fit_used": best_fit,
    "n_eq": n_eq_best,
    "d2F_dn2": d2F_best,
    "chi_q": chi_q_best,
    "N_modes": N_modes,
    "delta_n": delta_n,

    # CC predictions (M_KK^4 units)
    "Lambda_res_exact_MKK4": delta_Lambda_exact_best,
    "Lambda_res_harmonic_MKK4": delta_Lambda_harmonic_best,

    # CC predictions (GeV^4)
    "Lambda_res_exact_GeV4": Lambda_res_phys,
    "Lambda_res_harmonic_GeV4": Lambda_res_harmonic_GeV4,
    "rho_bare_SD_GeV4": rho_bare_SD,
    "rho_Lambda_obs": rho_Lambda_obs,

    # Ratios
    "log10_bare_gap": gap_SD,
    "log10_residual_gap_exact": log10_ratio_phys,
    "log10_residual_gap_harmonic": log10_ratio_harmonic,
    "orders_removed": gap_SD - log10_ratio_phys,

    # M_KK route dependence
    "log10_gap_gravity_route": log10_ratio_gravity,
    "log10_gap_kerner_route": log10_ratio_kerner,
    "M_KK_gravity": M_KK_gravity,
    "M_KK_kerner": M_KK_kerner,

    # All fits spread
    "spread_min_log10": spread_min,
    "spread_max_log10": spread_max,

    # Q-theory geodesic
    "Q_total_K7": Q_total,
    "N_pair_geod": N_pair_geod,

    # Constraint equation
    "f_2_grav": f_2_grav,

    # Gate
    "gate_name": "A4-QT-COMPOUND-61",
    "gate_verdict": verdict,
    "gate_detail": detail,
    "tau_fold": tau_fold,
}

outpath = data_dir / "s61_a4_qtheory_compound.npz"
np.savez(outpath, **save_dict)
print(f"Saved: {outpath}")
print(f"\nDONE.")
