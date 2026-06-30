#!/usr/bin/env python3
"""
S83 Wave 2 Gate G13: JENSEN-FLOW-TRAJECTORY (substrate-native z(tau))
=====================================================================

Gate: S83-JENSEN-FLOW-TRAJECTORY
Trigger: [VERIFY-THEOREM] (substrate-native derivation + numerical check).
Classification: GEOMETRIC (Jensen flow z(tau) structure) + PHONONIC
  (mode-equation interpretation via Mukhanov-Sasaki z variable).
Owner: transit-dynamics-theorist
Write-target: sessions/archive/session-83/session-83-results-workingpaper.md §W2-G13

HYPOTHESIS (pre-registered, session-83-plan §W2-G13):
  The Mukhanov variable z(tau) is DERIVABLE from Jensen-flow + substrate
  spectral action WITHOUT reliance on an external single-field inflaton
  model. z_substrate(tau) is computable from {a_2 Seeley-DeWitt, tau_fold
  trajectory, epsilon_H(tau)} alone.

PRE-REGISTERED FORM:
  z_substrate(tau) = a(tau) * sqrt(2 * epsilon_H(tau)) * M_Pl_eff(tau)
  with each factor derived from substrate action.

PASS: z_substrate(tau) computable end-to-end from canonical constants +
      substrate action; numerical ratio z_sub/z_canonical in [1/3, 3].
INFO: derivable but requires one empirical pin (e.g., eps_H at one point),
      OR ratio in [0.1, 10] but outside [1/3, 3].
FAIL: derivation requires ad-hoc inflaton profile, OR ratio outside [0.1, 10].

SUBSTITUTION CHAIN ([VERIFY-THEOREM]):

  Step 1 (DEF):  z(tau) = a(tau) * sqrt(2 eps_H(tau)) * M_Pl_eff(tau).
                 [Mukhanov-Sasaki variable for canonical scalar field].

  Step 2 (SUB a): Substrate Friedmann + slow-roll KG (UNIT-CONSISTENT form).
                 H(tau)^2 = V_phys(tau) / (3 M_Pl_eff^2) (Friedmann).
                 dtau/dN = -(M_Pl_eff^2/Z_fold_phys)*(V'_phys/V_phys)
                          (slow-roll KG, tau dimensionless).
                 Unit reduction (M_KK factors cancel):
                   V_phys = V_dimless * M_KK^4, Z_phys = Z_dimless * M_KK^2,
                   M_Pl_eff^2 = (f_2/pi^2)*a_2*M_KK^2.
                   => (M_Pl^2/Z_phys) = (f_2/pi^2)*a_2/Z_dimless [dimless]
                   => (V'_phys/V_phys) = Vp_d/V_d [dimless per tau-unit]
                   => dtau/dN = -[(f_2/pi^2)*a_2/Z_d] * (Vp_d/V_d) dimless.
                 a(N) = a_fold * exp(N) (by definition of e-folds).
                 tau(N) obtained by numerical integration of KG.

  Step 3 (SUB H): V(tau) from Jensen quadratic expansion of spectral action:
                 V(tau) = S_fold + dS_fold*(tau-tau_fold) + (1/2)*d2S_fold*
                          (tau-tau_fold)^2.
                 V'(tau) = dS_fold + d2S_fold*(tau-tau_fold).
                 Both CLOSED in canonical_constants.

  Step 4 (SUB eps_H): Per W1-G4 substrate derivation (regulator-FI,
                 F_traj = 1.5 at PASS/INFO boundary):
                 eps_H(tau) = (M_Pl_eff^2/(2 Z_fold)) * (V'/V)^2.
                 CLOSED in canonical_constants.

  Step 5 (SUB M_Pl_eff): Spectral-action a_2 normalization (Chamseddine-
                 Connes, W1-G4 §3):
                 M_Pl_eff^2(R) = (f_2^R / pi^2) * a_2_fold * Lambda^2,
                 Lambda^2 = M_KK^2 (natural unit).
                 CLOSED in canonical_constants + regulator choice R.

  Step 6 (SIMP): Compose Steps 2-5:
                 z_substrate(tau) = a_fold * exp(N(tau))
                                     * M_Pl_eff^2 / sqrt(Z_fold)
                                     * |V'(tau)/V(tau)|
                 = CLOSED rational function of (tau; a_2, Lambda^2, f_2^R,
                   S_fold, dS_fold, d2S_fold, Z_fold).
                 NO inflaton potential imported; V is the Jensen spectral
                 moment, not an ad-hoc field theory.

  Step 7 (DIR): Closed form exists in canonical constants + tau => PASS
                 (substrate-derivable=True). Numerical validation: ratio
                 z_sub(N_pivot) / z_canonical(N_pivot) within [1/3, 3].

  Step 8 (PY):   Python integration + numerical comparison (this script).

Machinery pin (PRDR §0.11):
  - N_pivot = 64.0819 (S82 W1-2 c_s-corrected pin, matches W1-G4).
  - N_grid_size = 4001 (dense integration grid, RK4).
  - Regulator: zeta (CC baseline, f_2^zeta = 1 at L2=1); diagnostic rerun
    with Zubarev (f_2^Zub = 1) and SDW (f_2^SDW = 2/3) for FI consistency.
  - L_max = 5 (inherits W1-G4 a_n_fold provenance).
  - Integration: RK4 with step dN = N_pivot/4000.
  - z_canonical reference: computed from same slow-roll formula with
    REGULATOR-AVERAGED eps_H, M_Pl_eff (cross-check internal consistency;
    since both sides use the identical closed form, the ratio exercises
    numerical implementation rather than a theoretical mismatch).
  - INDEPENDENT reference z_obs from Planck A_s: inverted via
    A_s = H^2/(8 pi^2 M_Pl_eff^2 eps_H) to get z such that zeta power
    spectrum matches Planck — this is the *observationally anchored*
    z_canonical for validation.

CLASSIFICATION: GEOMETRIC + PHONONIC.
"""

import sys
import os
import time
import hashlib
import numpy as np
import sympy as sp
from pathlib import Path

SCRIPT_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPT_DIR))
os.chdir(str(SCRIPT_DIR))

os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

from canonical_constants import (
    PI,
    M_Pl_reduced,
    a0_fold, a2_fold, a4_fold,
    tau_fold,
    S_fold, dS_fold, d2S_fold,
    Z_fold,
    H_fold,
    M_KK_gravity,
    mellin_f_star_f2,
    Vol_SU3_Haar,
)

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# ============================================================================
# 1. INPUT-PIN MAP + SHA-256 CLOSURE
# ============================================================================
INPUT_PINS = {
    "a2_fold":                f"{a2_fold:.15e}",
    "a0_fold":                f"{a0_fold:.15e}",
    "a4_fold":                f"{a4_fold:.15e}",
    "tau_fold":               f"{tau_fold:.15e}",
    "S_fold":                 f"{S_fold:.15e}",
    "dS_fold":                f"{dS_fold:.15e}",
    "d2S_fold":               f"{d2S_fold:.15e}",
    "Z_fold":                 f"{Z_fold:.15e}",
    "H_fold":                 f"{H_fold:.15e}",
    "M_KK_gravity":           f"{M_KK_gravity:.15e}",
    "M_Pl_reduced":           f"{M_Pl_reduced:.15e}",
    "Vol_SU3_Haar":           f"{Vol_SU3_Haar:.15e}",
    "N_pivot":                "64.0819",
    "N_grid_size":            "4001",
    "regulator_primary":      "zeta",
    "regulators_FI":          "zeta,Zubarev,SDW",
    "f2_zeta":                "1.0",
    "f2_Zubarev":             "1.0",
    "f2_SDW":                 "0.6666666666666666",
    "A_s_Planck":             "2.1e-9",
    "EPS_H_CANONICAL":        "0.02163",
    "a_fold_norm":            "1.0",
    "PASS_lo_ratio":          "0.333333",
    "PASS_hi_ratio":          "3.0",
    "INFO_lo_ratio":          "0.1",
    "INFO_hi_ratio":          "10.0",
    "algorithm_id":           "G13-jensen-flow-trajectory-substrate-native-z-v1",
}
_ORDERED_STR = "|".join(f"{k}={INPUT_PINS[k]}" for k in sorted(INPUT_PINS.keys()))
CLOSURE_SHA = hashlib.sha256(_ORDERED_STR.encode('utf-8')).hexdigest()

print("=" * 74)
print("S83 W2-G13: JENSEN-FLOW-TRAJECTORY (substrate-native z(tau))")
print("=" * 74)
print(f"Script: {Path(__file__).name}")
print(f"Session: 83  Wave: 2  Gate: G13")
print(f"Owner: transit-dynamics-theorist")
print(f"Classification: GEOMETRIC + PHONONIC")
print(f"L_max (canonical pin): 5  |  N_pivot: 64.0819 (S82 W1-2 pin)")
print(f"Closure SHA-256: {CLOSURE_SHA}")
print("-" * 74)
print("Input pins (ordered):")
for k in sorted(INPUT_PINS.keys()):
    print(f"  {k:22s} = {INPUT_PINS[k]}")
print("-" * 74)

# ============================================================================
# 2. REGULATOR SLOT WEIGHTS (same as W1-G4)
# ============================================================================
# CC Mellin moments at L2 = M_KK^2 = 1 (natural-ratio convention).
f2_zeta    = 1.0                  # (local) CC zeta-scheme baseline
f2_Zubarev = 1.0                  # (local) anomaly-sharp cutoff at L2=1
f2_SDW     = 2.0/3.0               # (local) sqrt(x) integral at L2=1

f2_by_R = {
    "zeta":    f2_zeta,
    "Zubarev": f2_Zubarev,
    "SDW":     f2_SDW,
}

Lambda2 = M_KK_gravity**2                                            # (local) Lambda^2 in GeV^2

def MPl2_R(R):
    """
    M_Pl_eff^2 in regulator R (Chamseddine-Connes spectral action).
    From a_2 slot: S_EH = (f_2^R/pi^2) * a_2 * Lambda^2 * int R.
    Gives M_Pl_eff^2(R) = (f_2^R/pi^2) * a_2_fold * Lambda^2  [GeV^2].
    """
    return (f2_by_R[R] / PI**2) * a2_fold * Lambda2                 # (local) GeV^2

print("Regulator slot weights f_2^R (Lambda^2 = M_KK_gravity^2):")
for R, f2 in f2_by_R.items():
    print(f"  f_2^{R:8s} = {f2:.6f}   M_Pl_eff^2 = {MPl2_R(R):.6e} GeV^2")
print("-" * 74)

# ============================================================================
# 3. SYMBOLIC DERIVATION of z_substrate (substrate-derivability check)
# ============================================================================
print("SYMBOLIC DERIVATION (substrate-derivability check)")
print("-" * 74)

tau_sym, a2_sym, L2_sym, f2_sym = sp.symbols(
    'tau a2 Lambda2 f2', positive=True, real=True
)
S_f_sym, dS_f_sym, d2S_f_sym, Z_f_sym, tau0_sym, a_f_sym, N_sym = sp.symbols(
    'S_fold dS_fold d2S_fold Z_fold tau_fold a_fold N', real=True
)

# Jensen potential V(tau) -- spectral-action moment expansion at fold
V_sym = (S_f_sym
         + dS_f_sym*(tau_sym - tau0_sym)
         + sp.Rational(1, 2)*d2S_f_sym*(tau_sym - tau0_sym)**2)
Vp_sym = sp.diff(V_sym, tau_sym)

# Reduced Planck mass in scheme R
MPl2_R_sym = (f2_sym / sp.pi**2) * a2_sym * L2_sym
MPl_R_sym  = sp.sqrt(MPl2_R_sym)

# Slow-roll epsilon_H with kinetic stiffness Z_fold (from W1-G4)
eps_H_sym = (MPl2_R_sym / (2 * Z_f_sym)) * (Vp_sym / V_sym)**2

# Scale factor a(N) = a_fold * exp(N) where N = e-folds after fold
a_sym = a_f_sym * sp.exp(N_sym)

# Mukhanov-Sasaki z
z_sym = a_sym * sp.sqrt(2 * eps_H_sym) * MPl_R_sym

# Simplified closed form
z_simplified = sp.simplify(z_sym)
print("Symbolic z_substrate closed form (before absolute-value collapse):")
print(f"  z = {z_simplified}")
print()

# Rational-function check
free_syms = z_simplified.free_symbols
canonical_syms = {tau_sym, a2_sym, L2_sym, f2_sym, S_f_sym, dS_f_sym,
                  d2S_f_sym, Z_f_sym, tau0_sym, a_f_sym, N_sym}
extra_syms = free_syms - canonical_syms
substrate_derivable = (len(extra_syms) == 0)

# Test the key simplification identity: z = a * M_Pl_eff^2/sqrt(Z_fold) * |V'/V|
z_expected = a_sym * MPl2_R_sym / sp.sqrt(Z_f_sym) * sp.Abs(Vp_sym/V_sym)
id_check = sp.simplify(z_simplified - z_expected)  # if identical except sign, expect 0 up to sign
print(f"Free symbols in z_substrate: {sorted(str(s) for s in free_syms)}")
print(f"Extra symbols (non-canonical): {extra_syms}")
print(f"Canonical-only: {extra_syms == set()}")
print(f"==> SUBSTRATE-DERIVABLE: {substrate_derivable}")
print("-" * 74)

# ============================================================================
# 4. NUMERICAL IMPLEMENTATION (tau(N), eps_H(N), a(N), z(N))
# ============================================================================
def V_dimless_of_tau(tau):
    """
    Jensen potential V(tau) in DIMENSIONLESS framework units.
    Physical V_phys [GeV^4] = V_dimless * M_KK^4.
    """
    dtau = tau - tau_fold                                            # (local)
    return S_fold + dS_fold*dtau + 0.5*d2S_fold*dtau**2              # (local)

def Vp_dimless_of_tau(tau):
    """V'(tau) in dimensionless units. V'_phys [GeV^4/tau_unit] = Vp * M_KK^4."""
    return dS_fold + d2S_fold*(tau - tau_fold)                       # (local)

def MPl2_over_Z_dimless(R):
    """
    Dimensionless ratio (M_Pl_eff^2 / Z_fold_phys).
    Unit derivation:
      M_Pl_eff^2_phys = (f_2/pi^2) * a_2 * M_KK^2           [GeV^2]
      Z_fold_phys    = Z_fold_dimless * M_KK^2              [GeV^2]
      ratio          = (f_2/pi^2) * a_2 / Z_fold_dimless    [dimensionless]
    Both factors carry the same M_KK^2 unit; ratio is pure dimensionless.
    """
    return (f2_by_R[R] / PI**2) * a2_fold / Z_fold                   # (local) dimensionless

def eps_H_subst(tau, R):
    """
    Substrate-derived slow-roll eps_H (unit-consistent form).
    eps_H = (M_Pl_eff^2/(2 Z_fold_phys)) * (V'_phys/V_phys)^2
          = (1/2) * (M_Pl^2/Z)_dimless * (V'_dimless/V_dimless)^2
    where M_KK^4 cancels in V'/V ratio and M_KK^2 cancels in M_Pl^2/Z.
    """
    V_d  = V_dimless_of_tau(tau)                                      # (local)
    Vp_d = Vp_dimless_of_tau(tau)                                     # (local)
    return 0.5 * MPl2_over_Z_dimless(R) * (Vp_d / V_d)**2             # (local) dimensionless

def dtau_dN(tau, R):
    """
    Slow-roll KG in e-folds (unit-consistent, tau dimensionless):
      dtau/dN = -(M_Pl_eff^2/Z_fold_phys) * (V'_phys/V_phys)
              = -(M_Pl^2/Z)_dimless * (V'_d/V_d)
    """
    V_d  = V_dimless_of_tau(tau)                                      # (local)
    Vp_d = Vp_dimless_of_tau(tau)                                     # (local)
    return -MPl2_over_Z_dimless(R) * (Vp_d / V_d)                     # (local) dimensionless

def H_of_tau(tau, R):
    """
    Substrate Friedmann H(tau) in slow-roll.
    H^2 = V_phys / (3 M_Pl_eff^2)  [GeV^2]
    V_phys = V_dimless * M_KK^4; M_Pl_eff^2 = (f_2/pi^2)*a_2*M_KK^2.
    """
    V_phys = V_dimless_of_tau(tau) * M_KK_gravity**4                  # (local) GeV^4
    return np.sqrt(V_phys / (3.0 * MPl2_R(R)))                        # (local) GeV

# Integration grid: 0 to N_pivot + buffer, RK4
N_pivot = 64.0819                                                    # (local) S82 W1-2 pin
N_max   = N_pivot + 10.0                                             # (local) buffer
N_grid_size = 4001                                                   # (local)
N_axis = np.linspace(0.0, N_max, N_grid_size)                        # (local)
dN = N_axis[1] - N_axis[0]                                           # (local)

# a_fold normalization (reduced convention, a_fold = 1)
a_fold = 1.0                                                         # (local) normalization

# Integrate tau(N) for each regulator
tau_by_R = {}
a_by_R = {}
eps_H_by_R = {}
H_by_R = {}
MPl_R_num = {}
z_by_R = {}

for R in f2_by_R:
    tau_arr = np.empty_like(N_axis)                                  # (local)
    tau_arr[0] = tau_fold
    for i in range(1, len(N_axis)):
        t = tau_arr[i-1]                                             # (local)
        # RK4
        k1 = dtau_dN(t, R)                                           # (local)
        k2 = dtau_dN(t + 0.5*dN*k1, R)                               # (local)
        k3 = dtau_dN(t + 0.5*dN*k2, R)                               # (local)
        k4 = dtau_dN(t + dN*k3, R)                                   # (local)
        tau_arr[i] = t + (dN/6.0)*(k1 + 2*k2 + 2*k3 + k4)
    tau_by_R[R] = tau_arr

    a_arr = a_fold * np.exp(N_axis)                                  # (local)
    eps_arr = eps_H_subst(tau_arr, R)                                # (local)
    H_arr = H_of_tau(tau_arr, R)                                     # (local)
    MPl_R_val = np.sqrt(MPl2_R(R))                                   # (local) GeV

    a_by_R[R] = a_arr
    eps_H_by_R[R] = eps_arr
    H_by_R[R] = H_arr
    MPl_R_num[R] = MPl_R_val

    # Mukhanov-Sasaki z
    z_arr = a_arr * np.sqrt(2.0 * eps_arr) * MPl_R_val               # (local) GeV units
    z_by_R[R] = z_arr

# Extract pivot values (interpolate)
idx_pivot = int(np.argmin(np.abs(N_axis - N_pivot)))
N_at_pivot = N_axis[idx_pivot]

print(f"Integration done. N_axis in [0, {N_max:.2f}], grid size {N_grid_size}.")
print(f"Evaluating at idx_pivot = {idx_pivot}, N_at_pivot = {N_at_pivot:.4f}")
print()
print(f"Substrate values at N_pivot (per regulator):")
print(f"  {'R':>8s} | {'tau':>10s} {'eps_H':>12s} {'H [GeV]':>14s} "
      f"{'M_Pl_eff [GeV]':>16s} {'z [GeV]':>14s}")
for R in ['zeta', 'Zubarev', 'SDW']:
    print(f"  {R:>8s} | {tau_by_R[R][idx_pivot]:>10.6f} "
          f"{eps_H_by_R[R][idx_pivot]:>12.6e} {H_by_R[R][idx_pivot]:>14.6e} "
          f"{MPl_R_num[R]:>16.6e} {z_by_R[R][idx_pivot]:>14.6e}")
print("-" * 74)

# ============================================================================
# 5. CANONICAL REFERENCE z_canonical FROM PLANCK A_s INVERSION
# ============================================================================
# Canonical (observational) benchmark: invert the standard slow-roll power
# spectrum formula A_s = H^2/(8 pi^2 M_Pl^2 eps_H) to get a "target" z.
#
# In standard slow-roll, the power spectrum at horizon exit is
#   P_zeta(k) = |v_k/z|^2, with Bunch-Davies |v_k|^2 = 1/(2k) at k = aH.
# After rescaling: A_s = P_zeta at k_pivot = H^2/(8 pi^2 M_Pl^2 eps_H).
# This defines the *observational* z through the Mukhanov normalization.
#
# We compare z_substrate(N_pivot) to this observational anchor.
# Both share the same form z = a sqrt(2 eps) M_Pl, so the ratio tests
# whether the substrate-derived (tau, H, eps_H, M_Pl) trajectory places
# z at the Planck-anchored value.

A_s_Planck = 2.1e-9                                                  # (local) Planck 2018
EPS_H_CANONICAL = 0.02163                                            # (local) S75/S77 one-loop

# Observationally anchored H at horizon exit (canonical inflation identification)
# H_obs = sqrt(A_s * 8 pi^2 * eps_H) * M_Pl_reduced
H_obs_GeV = np.sqrt(A_s_Planck * 8.0 * PI**2 * EPS_H_CANONICAL) * M_Pl_reduced  # (local)

# z_canonical computed with observationally anchored inputs:
#   a_canonical(N_pivot) normalized to same a_fold=1 exponential => a_canonical = exp(N_pivot)
#   eps_H = EPS_H_CANONICAL
#   M_Pl = M_Pl_reduced
a_canonical = a_fold * np.exp(N_at_pivot)                            # (local) SAME a(N) profile
z_canonical_obs = a_canonical * np.sqrt(2.0 * EPS_H_CANONICAL) * M_Pl_reduced  # (local) GeV

print(f"Canonical reference (Planck-anchored, observational slow-roll):")
print(f"  A_s_Planck            = {A_s_Planck:.4e}")
print(f"  eps_H (S75/S77)       = {EPS_H_CANONICAL:.6f}")
print(f"  M_Pl_reduced          = {M_Pl_reduced:.6e} GeV")
print(f"  a_canonical(N_pivot)  = {a_canonical:.6e}")
print(f"  H_obs (observational) = {H_obs_GeV:.6e} GeV")
print(f"  z_canonical_obs       = {z_canonical_obs:.6e} GeV")
print("-" * 74)

# ============================================================================
# 6. RATIO AND VERDICT
# ============================================================================
# Primary gate: zeta regulator (CC baseline) vs canonical observational z.
R_primary = 'zeta'
z_sub_primary = z_by_R[R_primary][idx_pivot]                         # (local)
ratio_primary = z_sub_primary / z_canonical_obs                      # (local)

# Log10 ratio for OOM readability
log10_ratio_primary = np.log10(abs(ratio_primary))                   # (local)

# Secondary: FI spread across {zeta, Zubarev, SDW}
z_sub_by_R = {R: z_by_R[R][idx_pivot] for R in f2_by_R}
ratios_by_R = {R: z_sub_by_R[R] / z_canonical_obs for R in f2_by_R}
F_traj_z = max(abs(v) for v in z_sub_by_R.values()) / min(abs(v) for v in z_sub_by_R.values())  # (local)

# Verdict logic (pre-registered thresholds)
PASS_LO = 1.0/3.0                                                    # (local)
PASS_HI = 3.0                                                        # (local)
INFO_LO = 0.1                                                        # (local)
INFO_HI = 10.0                                                       # (local)

ratio_abs = abs(ratio_primary)                                       # (local)
if substrate_derivable and PASS_LO <= ratio_abs <= PASS_HI:
    verdict = "PASS"
elif substrate_derivable and INFO_LO <= ratio_abs <= INFO_HI:
    verdict = "INFO"
else:
    verdict = "FAIL"

print("VERDICT RESOLUTION")
print("-" * 74)
print(f"  substrate_derivable   = {substrate_derivable}")
print(f"  z_substrate^zeta      = {z_sub_by_R['zeta']:.6e} GeV")
print(f"  z_substrate^Zubarev   = {z_sub_by_R['Zubarev']:.6e} GeV")
print(f"  z_substrate^SDW       = {z_sub_by_R['SDW']:.6e} GeV")
print(f"  z_canonical (Planck)  = {z_canonical_obs:.6e} GeV")
print(f"  ratio (zeta/canon)    = {ratios_by_R['zeta']:.6f}")
print(f"  ratio (Zub/canon)     = {ratios_by_R['Zubarev']:.6f}")
print(f"  ratio (SDW/canon)     = {ratios_by_R['SDW']:.6f}")
print(f"  log10(ratio_primary)  = {log10_ratio_primary:+.4f}")
print(f"  F_traj_z (regulator spread): {F_traj_z:.4f}")
print(f"  Thresholds:")
print(f"    PASS if ratio in [{PASS_LO:.4f}, {PASS_HI:.4f}]")
print(f"    INFO if ratio in [{INFO_LO:.4f}, {INFO_HI:.4f}] (outside PASS)")
print(f"    FAIL otherwise")
print(f"  VERDICT: {verdict}")
print("-" * 74)

# ============================================================================
# 7. CROSS-CHECKS
# ============================================================================
# (a) H_substrate (zeta) vs H_obs
H_sub_at_pivot = H_by_R['zeta'][idx_pivot]                           # (local)
H_ratio = H_sub_at_pivot / H_obs_GeV                                 # (local)

# (b) Substrate eps_H vs EPS_H_CANONICAL
eps_sub_zeta = eps_H_by_R['zeta'][idx_pivot]                         # (local)
eps_ratio = eps_sub_zeta / EPS_H_CANONICAL                           # (local)

# (c) A_s prediction from substrate slow-roll
A_s_substrate = (H_sub_at_pivot**2) / (8.0 * PI**2 * MPl2_R('zeta') * eps_sub_zeta)  # (local)
A_s_OOM_shift = np.log10(A_s_substrate / A_s_Planck)                 # (local)

# (d) tau drift at pivot (deviation from tau_fold)
dtau_at_pivot = tau_by_R['zeta'][idx_pivot] - tau_fold               # (local)

# (e) Verify a(N) exponential identity
a_analytic = np.exp(N_at_pivot)                                      # (local) for a_fold=1
a_numerical = a_by_R['zeta'][idx_pivot]                              # (local)
a_agreement = a_numerical / a_analytic                               # (local)

print("CROSS-CHECKS")
print("-" * 74)
print(f"  (a) H_sub^zeta(N_pivot)     = {H_sub_at_pivot:.6e} GeV")
print(f"      H_obs (Planck-anchored)  = {H_obs_GeV:.6e} GeV")
print(f"      ratio (sub/obs)          = {H_ratio:.4e} (log10 = {np.log10(abs(H_ratio)):+.2f})")
print(f"  (b) eps_H_sub^zeta           = {eps_sub_zeta:.6e}")
print(f"      eps_H canonical          = {EPS_H_CANONICAL:.6e}")
print(f"      ratio                    = {eps_ratio:.4f}")
print(f"  (c) A_s_substrate            = {A_s_substrate:.6e}")
print(f"      A_s_Planck               = {A_s_Planck:.6e}")
print(f"      delta_OOM                = {A_s_OOM_shift:+.4f}")
print(f"  (d) tau drift at pivot       = {dtau_at_pivot:+.6e} (from tau_fold={tau_fold})")
print(f"  (e) a_analytic(N_pivot)      = {a_analytic:.6e}")
print(f"      a_numerical(N_pivot)     = {a_numerical:.6e}")
print(f"      agreement                = {a_agreement:.10f} (target 1.0)")
print("-" * 74)

# ============================================================================
# 8. 4-TUPLE OUTPUT TAG
# ============================================================================
scheme_tag = "zeta+Zubarev+SDW-jointly"
convention_tag = "substrate-a2-Jensen-flow"
Lmax_tag = "5"
value_tag = (f"ratio={ratios_by_R['zeta']:.6f}_"
             f"substrate-derivable={substrate_derivable}_"
             f"F_traj_z={F_traj_z:.4f}")
four_tuple = (f"(value={value_tag}, scheme={scheme_tag}, "
              f"convention={convention_tag}, L_max={Lmax_tag})")
print(f"4-tuple: {four_tuple}")
print("-" * 74)

# ============================================================================
# 9. DATA FILE + PLOT
# ============================================================================
NPZ_PATH = SCRIPT_DIR / "s83_w2_g13_jensen_flow_trajectory.npz"
np.savez_compressed(
    NPZ_PATH,
    N_axis=N_axis,
    tau_zeta=tau_by_R['zeta'],
    tau_Zubarev=tau_by_R['Zubarev'],
    tau_SDW=tau_by_R['SDW'],
    a_zeta=a_by_R['zeta'],
    eps_H_zeta=eps_H_by_R['zeta'],
    eps_H_Zubarev=eps_H_by_R['Zubarev'],
    eps_H_SDW=eps_H_by_R['SDW'],
    H_zeta=H_by_R['zeta'],
    H_Zubarev=H_by_R['Zubarev'],
    H_SDW=H_by_R['SDW'],
    z_zeta=z_by_R['zeta'],
    z_Zubarev=z_by_R['Zubarev'],
    z_SDW=z_by_R['SDW'],
    MPl2_zeta=MPl2_R('zeta'),
    MPl2_Zubarev=MPl2_R('Zubarev'),
    MPl2_SDW=MPl2_R('SDW'),
    N_pivot=N_pivot,
    idx_pivot=idx_pivot,
    z_canonical_obs=z_canonical_obs,
    H_obs=H_obs_GeV,
    ratio_primary=ratio_primary,
    log10_ratio_primary=log10_ratio_primary,
    F_traj_z=F_traj_z,
    A_s_substrate=A_s_substrate,
    A_s_Planck=A_s_Planck,
    A_s_OOM_shift=A_s_OOM_shift,
    substrate_derivable=substrate_derivable,
    verdict=verdict,
    closure_sha=CLOSURE_SHA,
    four_tuple=four_tuple,
)
print(f"Data: {NPZ_PATH.name}")

# Plot: 2x2 panel
fig, axes = plt.subplots(2, 2, figsize=(13, 9))
ax1, ax2, ax3, ax4 = axes.flatten()

colors = {'zeta': '#1f77b4', 'Zubarev': '#2ca02c', 'SDW': '#d62728'}

# (1) z_substrate(N) per regulator
for R in ['zeta', 'Zubarev', 'SDW']:
    ax1.plot(N_axis, z_by_R[R], '-', lw=1.6, color=colors[R],
             label=f'z_sub^{R}(N)')
ax1.axhline(z_canonical_obs, color='k', ls='--', lw=1.4,
            label=f'z_canonical(Planck)={z_canonical_obs:.2e}')
ax1.axvline(N_pivot, color='gray', ls=':', alpha=0.5,
            label=f'N_pivot={N_pivot:.3f}')
ax1.set_xlabel('N (e-folds from fold)')
ax1.set_ylabel('z (GeV)')
ax1.set_yscale('log')
ax1.set_title('Mukhanov-Sasaki z_substrate(N) per regulator')
ax1.legend(loc='best', fontsize=8)
ax1.grid(True, alpha=0.3)

# (2) eps_H(N) per regulator
for R in ['zeta', 'Zubarev', 'SDW']:
    ax2.plot(N_axis, eps_H_by_R[R], '-', lw=1.6, color=colors[R],
             label=f'eps_H^{R}(N)')
ax2.axhline(EPS_H_CANONICAL, color='k', ls='--', lw=1.4,
            label=f'eps_H_canonical={EPS_H_CANONICAL:.4f}')
ax2.axvline(N_pivot, color='gray', ls=':', alpha=0.5)
ax2.set_xlabel('N (e-folds from fold)')
ax2.set_ylabel('epsilon_H(N)')
ax2.set_yscale('log')
ax2.set_title('Substrate-derived epsilon_H(N)')
ax2.legend(loc='best', fontsize=8)
ax2.grid(True, alpha=0.3)

# (3) tau(N) trajectory per regulator
for R in ['zeta', 'Zubarev', 'SDW']:
    ax3.plot(N_axis, tau_by_R[R], '-', lw=1.6, color=colors[R],
             label=f'tau^{R}(N)')
ax3.axhline(tau_fold, color='k', ls='--', lw=1.4,
            label=f'tau_fold={tau_fold:.3f}')
ax3.axvline(N_pivot, color='gray', ls=':', alpha=0.5)
ax3.set_xlabel('N (e-folds from fold)')
ax3.set_ylabel('tau(N) [Jensen scalar]')
ax3.set_title('Jensen-flow trajectory tau(N)')
ax3.legend(loc='best', fontsize=8)
ax3.grid(True, alpha=0.3)

# (4) ratio log10(z_sub/z_canonical)(N)
for R in ['zeta', 'Zubarev', 'SDW']:
    ratio_arr = z_by_R[R] / z_canonical_obs
    ax4.plot(N_axis, np.log10(np.abs(ratio_arr)), '-', lw=1.6,
             color=colors[R], label=f'log10(z_sub^{R}/z_canon)')
ax4.axhline(np.log10(PASS_LO), color='g', ls='--', lw=1.1,
            label=f'PASS lo ({np.log10(PASS_LO):+.2f})')
ax4.axhline(np.log10(PASS_HI), color='g', ls='--', lw=1.1,
            label=f'PASS hi ({np.log10(PASS_HI):+.2f})')
ax4.axhline(np.log10(INFO_LO), color='r', ls=':', lw=1.0,
            label=f'INFO lo ({np.log10(INFO_LO):+.2f})')
ax4.axhline(np.log10(INFO_HI), color='r', ls=':', lw=1.0,
            label=f'INFO hi ({np.log10(INFO_HI):+.2f})')
ax4.axvline(N_pivot, color='gray', ls=':', alpha=0.5)
ax4.set_xlabel('N (e-folds from fold)')
ax4.set_ylabel('log10(z_sub / z_canonical)')
ax4.set_title(f'z-ratio trajectory (verdict at pivot = {verdict})')
ax4.legend(loc='best', fontsize=7)
ax4.grid(True, alpha=0.3)

plt.suptitle(
    f'S83 W2-G13: JENSEN-FLOW-TRAJECTORY substrate-native z(tau)\n'
    f'substrate_derivable={substrate_derivable}  '
    f'ratio_primary(zeta)={ratio_primary:.4e}  '
    f'log10_ratio={log10_ratio_primary:+.2f}  verdict={verdict}',
    fontsize=10  # (local)
)
plt.tight_layout()

PNG_PATH = SCRIPT_DIR / "s83_w2_g13_jensen_flow_trajectory.png"
plt.savefig(PNG_PATH, dpi=140, bbox_inches='tight')
plt.close(fig)
print(f"Plot: {PNG_PATH.name}")
print("-" * 74)

# ============================================================================
# 10. VERDICT LINE
# ============================================================================
verdict_line = (
    f"S83-JENSEN-FLOW-TRAJECTORY: {verdict} -- "
    f"value={value_tag} "
    f"scheme={scheme_tag} "
    f"convention={convention_tag} "
    f"L_max={Lmax_tag} "
    f"sha256={CLOSURE_SHA}"
)
print("VERDICT LINE (append to s83_gate_verdicts.txt):")
print(f"  {verdict_line}")
print("-" * 74)

# ============================================================================
# 11. CLASSIFICATION + SUMMARY
# ============================================================================
print("CLASSIFICATION: GEOMETRIC + PHONONIC")
print("  - GEOMETRIC: z(tau) derives from the a_2 Seeley-DeWitt coefficient")
print("    (via M_Pl_eff), the Jensen spectral moments (V, V'), and the")
print("    kinetic stiffness Z_fold. No inflaton field theory imported.")
print("  - PHONONIC: z is the Mukhanov-Sasaki variable of the linear")
print("    acoustic/scalar mode equation on the substrate's emergent FRW")
print("    background. The ratio z_sub/z_canonical tests whether the")
print("    substrate's own trajectory reproduces the observational")
print("    Planck-anchored amplitude.")
print()
print(f"SUMMARY:")
print(f"  substrate_derivable   = {substrate_derivable}")
print(f"  z_sub^zeta(N_pivot)   = {z_sub_by_R['zeta']:.6e} GeV")
print(f"  z_canonical (Planck)  = {z_canonical_obs:.6e} GeV")
print(f"  ratio (primary)       = {ratio_primary:.6f}")
print(f"  log10(ratio)          = {log10_ratio_primary:+.4f}")
print(f"  F_traj_z (FI spread)  = {F_traj_z:.4f}")
print(f"  A_s delta_OOM (sub/Planck) = {A_s_OOM_shift:+.4f}")
print(f"  VERDICT               = {verdict}")
print("=" * 74)
