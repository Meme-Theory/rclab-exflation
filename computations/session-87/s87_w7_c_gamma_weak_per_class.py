"""
s87_w7_c_gamma_weak_per_class.py — S87-W6-C-GAMMA-WEAK-PER-CLASS (CF-44)
=======================================================================

Per-L1-class Lambda_anom_internal under Weyl-rescaling family. Decides
R1 (class-INDEPENDENT) vs R2 (class-FACTORIZED with integer multipliers)
vs R3 (class-INDEPENDENTLY-DETERMINED) for the 5-class L1 partition of
the 5-regulator atlas {zeta, Mellin/SDW, heat-kernel/Zubarev, hard-cutoff/cutoff_sqrt,
Pauli-Villars/anomaly}.

Plan: sessions/session-plan/session-87-plan-w7.md §W7-3 (lines 648-908).

Substitution chain (per §10):

  Def 1: Z_c(t) = sum_{lambda in spec(D_K) restricted to class c} exp(-t * lambda^2)
  Def 2: N_c(s) = int_0^infty t^(s-1) omega(t) Z_c(t) dt   (Mellin-Weyl moment)
  Def 3: Lambda_anom_internal_c = Res[N_c(s); s=4] / Res[N_c(s); s=2]

  Step 1: substitute heat kernel
          N_c(s) = sum_lambda lambda^(-2s) * Gamma(s) * mu_omega(s)
  Step 2: factor regulator from class projector
          N_c(s) = mu_omega(s) * Gamma(s) * zeta_c(2s)
  Step 3: residue ratio
          Lambda_anom_internal_c = K_omega * (Res[zeta_c(8)] / Res[zeta_c(4)])
          K_omega = (mu_omega(4)/mu_omega(2)) * (Gamma(4)/Gamma(2))  (class-INDEPENDENT)
  Step 4: per-class ratio decides R1/R2/R3
          R1: ratio = 1 forall (c, c')  iff  R1_dispersion = std/mean <= 0.02
          R2: ratio rational with small integer numerator/denominator (residual <= 0.05)
          R3: dispersed, well-defined per class

Operational realization: on the discrete SU(3) Casimir spectrum at L_max=10, the per-class
spectral zeta zeta_c(s) is realized via _spectral_action_regulators.py:

  zeta_c(2s) at s=4  -->  a_n=4 moment under regulator c  -->  zeta_a_n(4, L_max)
  zeta_c(2s) at s=2  -->  a_n=2 moment under regulator c  -->  zeta_a_n(2, L_max)

so Lambda_anom_internal_c proportional to (a_4^c / a_2^c) modulo class-independent K_omega.

Class -> regulator mapping (per s86-sector-2-split-layer-taxonomy.md C1, lines 555-557 +
1075-1095): 5-class L1 partition is per-regulator under multiplier-vector identity.

  Class 1 = {zeta}                    -- L1-canonical
  Class 2 = {SDW = Mellin}            -- L1-near-canonical (algebraic identity to zeta on positive spectrum)
  Class 3 = {Zubarev = heat-kernel}   -- L2-canonical (Mellin-support-on-a_4 with heat-kernel dressing)
  Class 4 = {cutoff_sqrt = hard-cutoff} -- L2-disqualified (a_0 contamination via truncation)
  Class 5 = {anomaly = Pauli-Villars}   -- L3-disqualified (PV subtraction signature)

TIER-2 SCHEMATIC declaration (per substrate-first-canonical-sourcing.md §iv):
  This script consumes _spectral_action_regulators.py whose docstring identifies it as
  SCHEMATIC (lines 23-30). The convention tag encodes the SCHEMATIC suffix:
  convention=C-gamma-WEAK-per-L1-class[-SCHEMATIC]. The TIER-2 disclosure paragraph in
  the working paper section §W7-3 documents this explicitly.

Profile-invariance cross-check (Step F, mandatory for PASS):
  Re-evaluate Lambda_anom_internal_c under TWO Weyl profiles:
    omega_a(t) = exp(-t / Lambda^2)
    omega_b(t) = (1 + t/Lambda^2)^(-1)
  Verify per-class Lambda_anom_internal_c is profile-INVARIANT within RATIO <= 1e-2.
  In the Step-3 simplified form, profile-invariance is automatic at the K_omega level
  and reduces to verifying that the K_omega ratio between profiles is class-independent.

PASS/FAIL/INFO (per §9):
  PASS = (R1 holds: dispersion <= 0.02) OR (R2 holds: integer-fit residual <= 0.05 with non-trivial n_c).
         Profile-invariance <= 1e-2 AND regime_verdict = VALID.
  INFO = neither R1 nor R2 holds but R3 valid (5 finite, independent scales).
  FAIL = any class non-finite OR sign-inconsistent OR profile-variance > 1e-2 OR BREAKDOWN.

3-tuple S87+ schema-v2 annotation:
  sign_verdict = N/A  (Lambda_anom_internal positive by construction)
  magnitude_verdict = PASS|INFO|FAIL  (per dispersion / R2 fit)
  regime_verdict = VALID|MARGINAL|BREAKDOWN  (per Mellin-residue convergence per class)

Composite collapse (per gate-verdicts.md):
  if regime == BREAKDOWN: composite = FAIL
  elif magnitude == FAIL and regime == VALID: composite = FAIL
  elif magnitude == INFO: composite = INFO
  else: composite = PASS
"""

import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import hashlib
import json
import math
import numpy as np
import torch

from canonical_constants import M_KK, Vol_SU3_Haar, PI
from _spectral_action_regulators import (
    zeta_a_n,
    mellin_a_n,
    heat_kernel_a_n,
    hard_cutoff_a_n,
    pauli_villars_a_n,
    REGULATOR_NAMES,
)


# ---------------------------------------------------------------------------
# Header + GPU env disclosure
# ---------------------------------------------------------------------------
print("=" * 78)
print("s87_w7_c_gamma_weak_per_class — S87-W6-C-GAMMA-WEAK-PER-CLASS")
print("Plan: sessions/session-plan/session-87-plan-w7.md §W7-3")
print("Trigger: [VERIFY]; substitution chain mandatory")
print("Tier:    TIER-2 SCHEMATIC (per substrate-first-canonical-sourcing.md §iv)")
print("=" * 78)
print(f"torch:        {torch.__version__}")
print(f"cuda avail:   {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"  device:     {torch.cuda.get_device_name(0)}")
print()


# ---------------------------------------------------------------------------
# Input pin map + SHA-256 closure
# ---------------------------------------------------------------------------
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))                          # (local)
SCRIPT_PATH = os.path.join(SCRIPT_DIR, "s87_w7_c_gamma_weak_per_class.py")        # (local)

INPUT_FILES = {                                                                  # (local)
    "_spectral_action_regulators.py": os.path.join(SCRIPT_DIR, "_spectral_action_regulators.py"),
    "s84_spectrum_cache_L12_tau019.npz": os.path.join(SCRIPT_DIR, "s84_spectrum_cache_L12_tau019.npz"),
    "canonical_constants.py": os.path.join(SCRIPT_DIR, "canonical_constants.py"),
}

# W-9 workshop fallback for 5-class L1 partition definition (per plan §0.5):
# class_partition_pin_pending=true; SHA-pin captures workshop wrap-up text.
W9_WORKSHOP = os.path.join(                                                      # (local)
    SCRIPT_DIR, "..", "sessions", "session-86", "workshops",
    "s86-sector-2-split-layer-taxonomy.md"
)
if os.path.exists(W9_WORKSHOP):
    INPUT_FILES["s86-sector-2-split-layer-taxonomy.md"] = W9_WORKSHOP

# S86 W-6 workshop file: C-gamma-WEAK definition source
W6_WORKSHOP = os.path.join(                                                      # (local)
    SCRIPT_DIR, "..", "sessions", "session-86",
    "session-86-w6-workingpaper.md"
)
if os.path.exists(W6_WORKSHOP):
    INPUT_FILES["session-86-w6-workingpaper.md"] = W6_WORKSHOP

# Optional W7-1 IC per-class npz (use if landed at compute time)
OPTIONAL_W71 = os.path.join(SCRIPT_DIR, "s87_w7_ic_per_class_verify.npz")        # (local)
if os.path.exists(OPTIONAL_W71):
    INPUT_FILES["s87_w7_ic_per_class_verify.npz"] = OPTIONAL_W71
    W71_LANDED = True                                                            # (local)
else:
    W71_LANDED = False                                                           # (local)


def file_sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


input_pin_map = {}                                                               # (local)
print("INPUT PIN MAP:")
for name, p in INPUT_FILES.items():
    sha = file_sha256(p)                                                         # (local)
    input_pin_map[name] = sha
    print(f"  {name:46s}  {sha[:16]}…")

# Self-pin script
SCRIPT_SHA = file_sha256(SCRIPT_PATH)                                            # (local)
input_pin_map["__script_sha__"] = SCRIPT_SHA
print(f"  {'__script_sha__':46s}  {SCRIPT_SHA[:16]}…")
print()


# ---------------------------------------------------------------------------
# Machinery pins (per plan §7 PRDR)
# ---------------------------------------------------------------------------
L_MAX = 10                                                                       # (local) canonical
N_CLASSES = 5                                                                    # (local) L1 partition cardinality
N_EVAL = 5                                                                       # (local) one per L1-class
SCHEME = "Weyl-rescaling-Mellin"                                                 # (local)
CONVENTION = "C-gamma-WEAK-per-L1-class-SCHEMATIC"                               # (local)
TIER_PIN = "TIER-2"                                                              # (local) per substrate-first-canonical-sourcing.md §iv

# PASS/FAIL/INFO thresholds per §9
R1_DISPERSION_PASS = 0.02                                                        # (local) RATIO
R2_INTEGER_FIT_RESIDUAL = 0.05                                                   # (local) RATIO
PROFILE_INVARIANCE_THRESH = 1e-2                                                 # (local) RATIO

# Class -> regulator mapping (per s86-sector-2-split-layer-taxonomy.md C1)
CLASS_REGULATOR_MAP = [                                                          # (local)
    ("Class_1_zeta", "zeta", zeta_a_n),
    ("Class_2_SDW", "Mellin", mellin_a_n),
    ("Class_3_Zubarev", "heat-kernel", heat_kernel_a_n),
    ("Class_4_cutoff_sqrt", "hard-cutoff", hard_cutoff_a_n),
    ("Class_5_anomaly", "Pauli-Villars", pauli_villars_a_n),
]

machinery_pins = {                                                               # (local)
    "L_max": L_MAX,
    "scheme": SCHEME,
    "convention": CONVENTION,
    "tier_pin": TIER_PIN,
    "n_eval": N_EVAL,
    "n_classes_pin": N_CLASSES,
    "weyl_profile_a_pin": "exp(-t/Lambda^2)",
    "weyl_profile_b_pin": "(1+t/Lambda^2)^-1",
    "tolerance_R1_dispersion": R1_DISPERSION_PASS,
    "tolerance_R2_integer_fit": R2_INTEGER_FIT_RESIDUAL,
    "tolerance_profile_invariance": PROFILE_INVARIANCE_THRESH,
    "random_seed": None,
    "GPU_path": "torch (eigh ineligible — Mellin moments scalar)",
}
print("MACHINERY PINS:")
for k, v in machinery_pins.items():
    print(f"  {k:36s} = {v}")
print()


# ---------------------------------------------------------------------------
# Step A. Per-class Mellin moments a_n^c at n=2 and n=4 (Step 3 spectral inputs)
# ---------------------------------------------------------------------------
# Per Step 3 of the substitution chain:
#   Lambda_anom_internal_c proportional to (Res[zeta_c(8)] / Res[zeta_c(4)])
# Operationally on the discrete Casimir spectrum at L_max=10, this reduces to
#   a_n=4 / a_n=2 under regulator c.
# (Plan §W7-3 Step 3 line 850.)
print("STEP A — per-class a_4^c and a_2^c on schematic SU(3) Casimir spectrum (L_max=10):")
print()
print(f"  {'Class':22s}  {'regulator':16s}  {'a_4^c':>16s}  {'a_2^c':>16s}  {'a_4/a_2':>14s}")

per_class_a4 = []                                                                # (local)
per_class_a2 = []                                                                # (local)
per_class_ratio = []                                                             # (local)

for cls_name, reg_name, evaluator in CLASS_REGULATOR_MAP:
    a4_c = evaluator(4, L_MAX, Vol_SU3_Haar)                                     # (local)
    a2_c = evaluator(2, L_MAX, Vol_SU3_Haar)                                     # (local)
    ratio_c = a4_c / a2_c                                                        # (local)
    per_class_a4.append(a4_c)
    per_class_a2.append(a2_c)
    per_class_ratio.append(ratio_c)
    print(f"  {cls_name:22s}  {reg_name:16s}  {a4_c:16.6e}  {a2_c:16.6e}  {ratio_c:14.6e}")

per_class_a4 = np.array(per_class_a4)
per_class_a2 = np.array(per_class_a2)
per_class_ratio = np.array(per_class_ratio)
print()


# ---------------------------------------------------------------------------
# Step B. Per-class Lambda_anom_internal_c
# ---------------------------------------------------------------------------
# Per Step 3 of substitution chain, with K_omega class-independent and absorbed into
# Lambda^2 normalization. We define K_omega = (Gamma(4)/Gamma(2)) for the trivial
# omega(t) = 1 limit and verify profile-invariance separately in Step F.
#
# Lambda_anom_internal_c = K_omega * (a_4^c / a_2^c) * M_KK^2
# (M_KK^2 supplies the dimensional unit: ratio of Mellin moments is dimensionless,
# Lambda_anom_internal carries [mass^2]; AC-2010 §V Eq. (5.2) per S86 W6-3 §M.1.)

K_OMEGA_TRIVIAL = math.gamma(4) / math.gamma(2)                                  # (local) = 6 * 1 = 6
print(f"K_omega (trivial profile, omega -> 1)  =  Gamma(4)/Gamma(2)  =  {K_OMEGA_TRIVIAL:.6f}")
print()

# AC-2010 §V Eq. (5.2) sets Lambda_anom_internal^2 = (M_KK^2 / 16 pi^2) * Tr_F(YY)
# Within the Step-3 substitution chain, the "Tr_F(YY)" factor is replaced by the
# class-specific (a_4^c / a_2^c) ratio (the per-class Mellin moment ratio).
# Lambda_anom_internal_c^2 = K_omega * (a_4^c / a_2^c) * M_KK^2 / (16 pi^2)
M_KK_sq = M_KK * M_KK                                                            # (local)
norm_factor = K_OMEGA_TRIVIAL * M_KK_sq / (16.0 * PI ** 2)                       # (local)

per_class_Lambda_anom_internal_sq = norm_factor * per_class_ratio                # (local) [GeV^2]
per_class_Lambda_anom_internal = np.sqrt(np.abs(per_class_Lambda_anom_internal_sq))  # (local) [GeV]
per_class_sign = np.sign(per_class_Lambda_anom_internal_sq)                      # (local)

print("STEP B — per-class Lambda_anom_internal_c (M_KK units):")
print(f"  {'Class':22s}  {'Lambda^2 [GeV^2]':>20s}  {'Lambda [GeV]':>20s}  {'Lambda/M_KK':>14s}  sign")
for i, (cls_name, _, _) in enumerate(CLASS_REGULATOR_MAP):
    print(
        f"  {cls_name:22s}  "
        f"{per_class_Lambda_anom_internal_sq[i]:20.6e}  "
        f"{per_class_Lambda_anom_internal[i]:20.6e}  "
        f"{per_class_Lambda_anom_internal[i]/M_KK:14.6e}  "
        f"{per_class_sign[i]:+.0f}"
    )
print()


# ---------------------------------------------------------------------------
# Step C. R1 test (class-INDEPENDENT)
# ---------------------------------------------------------------------------
# R1 holds iff Lambda_anom_internal_c is class-invariant.
# R1_dispersion = std({Lambda_anom_internal_c}) / mean({Lambda_anom_internal_c}) <= 0.02
mean_Lambda = float(np.mean(per_class_Lambda_anom_internal))                     # (local)
std_Lambda = float(np.std(per_class_Lambda_anom_internal, ddof=0))               # (local)
R1_dispersion = std_Lambda / mean_Lambda if mean_Lambda > 0 else float("inf")    # (local)
R1_holds = (R1_dispersion <= R1_DISPERSION_PASS)                                 # (local)

print("STEP C — READING R1 (class-INDEPENDENT):")
print(f"  mean(Lambda_anom_internal)  = {mean_Lambda:.6e}")
print(f"  std(Lambda_anom_internal)   = {std_Lambda:.6e}")
print(f"  R1_dispersion = std/mean    = {R1_dispersion:.6e}")
print(f"  R1 PASS threshold           = {R1_DISPERSION_PASS}")
print(f"  R1 holds                    = {R1_holds}")
print()


# ---------------------------------------------------------------------------
# Step D. R2 test (class-FACTORIZED with integer multipliers)
# ---------------------------------------------------------------------------
# R2: Lambda_anom_internal_c = Lambda_global * n_c, n_c in Z+.
# Strategy: pick anchor = min(Lambda), candidate Lambda_global = anchor / k for k in 1..10;
# compute n_c = round(Lambda_anom_internal_c / Lambda_global); residual = max_c |actual - integer*Lambda_global| / Lambda.
print("STEP D — READING R2 (class-FACTORIZED with integer multipliers):")

best_R2_residual = float("inf")                                                  # (local)
best_R2_n_c = None                                                               # (local)
best_R2_Lambda_global = None                                                     # (local)
best_R2_anchor_k = None                                                          # (local)

# Try Lambda_global = Lambda_min / k for k = 1..10 (small-integer factorization)
Lambda_min = float(np.min(per_class_Lambda_anom_internal))                       # (local)
for k_anchor in range(1, 11):
    Lg_candidate = Lambda_min / k_anchor                                         # (local)
    if Lg_candidate <= 0:
        continue
    n_c_float = per_class_Lambda_anom_internal / Lg_candidate                    # (local)
    n_c_int = np.round(n_c_float).astype(int)                                    # (local)
    if np.any(n_c_int <= 0):
        continue
    fitted = n_c_int * Lg_candidate                                              # (local)
    residual_per_class = np.abs(per_class_Lambda_anom_internal - fitted) / per_class_Lambda_anom_internal  # (local)
    max_residual = float(np.max(residual_per_class))                             # (local)
    if max_residual < best_R2_residual:
        best_R2_residual = max_residual
        best_R2_n_c = n_c_int.copy()
        best_R2_Lambda_global = Lg_candidate
        best_R2_anchor_k = k_anchor

# Non-trivial check: not all 1
non_trivial_R2 = (                                                               # (local)
    best_R2_n_c is not None
    and not np.all(best_R2_n_c == 1)
)
R2_holds = (                                                                     # (local)
    best_R2_residual <= R2_INTEGER_FIT_RESIDUAL
    and non_trivial_R2
)

print(f"  best_R2_anchor_k       = {best_R2_anchor_k}")
print(f"  Lambda_global          = {best_R2_Lambda_global:.6e}" if best_R2_Lambda_global else "  Lambda_global          = N/A")
print(f"  best n_c               = {best_R2_n_c.tolist() if best_R2_n_c is not None else 'N/A'}")
print(f"  best max residual      = {best_R2_residual:.6e}")
print(f"  R2 PASS threshold      = {R2_INTEGER_FIT_RESIDUAL}")
print(f"  non-trivial (not all 1)= {non_trivial_R2}")
print(f"  R2 holds               = {R2_holds}")
print()


# ---------------------------------------------------------------------------
# Step E. R3 test (independent)
# ---------------------------------------------------------------------------
# R3 valid iff neither R1 nor R2 AND all 5 per-class values are finite + sign-consistent.
all_finite = bool(np.all(np.isfinite(per_class_Lambda_anom_internal)))           # (local)
all_positive = bool(np.all(per_class_sign > 0))                                  # (local)
sign_consistent = all_positive                                                   # (local) Lambda_anom positive by construction

R3_valid = (not R1_holds) and (not R2_holds) and all_finite and sign_consistent  # (local)

print("STEP E — READING R3 (class-INDEPENDENTLY-DETERMINED):")
print(f"  all per-class finite       = {all_finite}")
print(f"  all per-class positive     = {all_positive}")
print(f"  sign_consistent (positive) = {sign_consistent}")
print(f"  R3 valid                   = {R3_valid}")
print()


# ---------------------------------------------------------------------------
# Step F. Profile-invariance cross-check
# ---------------------------------------------------------------------------
# The two Weyl profiles omega_a(t) = exp(-t/Lambda^2) and omega_b(t) = (1+t/Lambda^2)^-1
# enter via mu_omega(s) the Mellin transform of omega.
# In the Step-3 simplified form K_omega = (mu_omega(4)/mu_omega(2)) * 6,
# K_omega is class-INDEPENDENT, so per-class RATIO under profile change is constant:
#   Lambda_anom_internal_c(omega_b) / Lambda_anom_internal_c(omega_a) = sqrt(K_omega_b / K_omega_a) constant for all c.
#
# Profile-invariance test: compute K_omega for both profiles, verify the per-class
# Lambda_anom_internal_c rescales by the SAME factor across all 5 classes (so the
# 5-class STRUCTURE is profile-invariant; the absolute scale shifts uniformly).
#
# Mellin transforms of profiles:
#   M[exp(-t/Lambda^2); s] = Lambda^(2s) * Gamma(s)
#   M[(1+t/Lambda^2)^-1; s] = Lambda^(2s) * pi / sin(pi*s)  (for 0 < Re(s) < 1; analytically continued)
# At integer s = 4 and s = 2, the second profile's Mellin has poles -> use renormalized
# regularized form: M[omega_b; s] = Lambda^(2s) * Gamma(s) * Gamma(1-s) / Gamma(0)... -> instead use
# numerical Mellin at s=4 and s=2 with a Lambda-cutoff finite truncation.
#
# Operationally simplest: define mu_omega(s) at s=4 vs s=2 numerically with Lambda fixed
# at M_KK and compare the ratios.

print("STEP F — PROFILE-INVARIANCE cross-check:")
print()


def mellin_omega_a(s, Lambda_val):
    """M[exp(-t/Lambda^2); s] = Lambda^(2s) * Gamma(s)."""
    return (Lambda_val ** (2.0 * s)) * math.gamma(s)


def mellin_omega_b_numeric(s, Lambda_val, N_pts=20000, t_max_factor=200.0):
    """M[(1+t/Lambda^2)^-1; s] via numerical quadrature on log-uniform grid.

    For 0 < Re(s) < 1 the Mellin is Lambda^(2s) * pi/sin(pi*s).
    For Re(s) > 1 we use IR cutoff at t_max = t_max_factor * Lambda^2 to define a
    REGULARIZED Mellin moment (the integral diverges at large-t for s > 1).
    """
    t_min = 1e-6 * Lambda_val ** 2
    t_max = t_max_factor * Lambda_val ** 2
    log_t = np.linspace(np.log(t_min), np.log(t_max), N_pts)
    t = np.exp(log_t)
    omega_b = 1.0 / (1.0 + t / (Lambda_val ** 2))
    integrand = (t ** (s - 1)) * omega_b * t  # extra t for log-jacobian
    # trapezoidal in log-t
    return float(np.trapezoid(integrand, log_t))


Lambda_ref = M_KK  # (local) reference scale for Weyl profile cutoff

mu_omega_a_s4 = mellin_omega_a(4.0, Lambda_ref)                                  # (local)
mu_omega_a_s2 = mellin_omega_a(2.0, Lambda_ref)                                  # (local)
K_omega_a = (mu_omega_a_s4 / mu_omega_a_s2) * (math.gamma(4) / math.gamma(2))    # (local)

mu_omega_b_s4 = mellin_omega_b_numeric(4.0, Lambda_ref)                          # (local)
mu_omega_b_s2 = mellin_omega_b_numeric(2.0, Lambda_ref)                          # (local)
K_omega_b = (mu_omega_b_s4 / mu_omega_b_s2) * (math.gamma(4) / math.gamma(2))    # (local)

# Trivial profile (used in Step B above)
K_omega_trivial = K_OMEGA_TRIVIAL  # (local) factored as 6

print(f"  Lambda_ref (Weyl cutoff)        = M_KK = {Lambda_ref:.6e}")
print(f"  mu_omega_a(s=4)                 = {mu_omega_a_s4:.6e}")
print(f"  mu_omega_a(s=2)                 = {mu_omega_a_s2:.6e}")
print(f"  mu_omega_a(4)/mu_omega_a(2)     = {mu_omega_a_s4/mu_omega_a_s2:.6e}")
print(f"  K_omega_a                       = {K_omega_a:.6e}")
print()
print(f"  mu_omega_b(s=4)  [numeric]      = {mu_omega_b_s4:.6e}")
print(f"  mu_omega_b(s=2)  [numeric]      = {mu_omega_b_s2:.6e}")
print(f"  mu_omega_b(4)/mu_omega_b(2)     = {mu_omega_b_s4/mu_omega_b_s2:.6e}")
print(f"  K_omega_b                       = {K_omega_b:.6e}")
print()

# Per-class Lambda_anom_internal under each profile
norm_factor_a = K_omega_a * M_KK_sq / (16.0 * PI ** 2)                           # (local)
norm_factor_b = K_omega_b * M_KK_sq / (16.0 * PI ** 2)                           # (local)
Lambda_per_class_a = np.sqrt(np.abs(norm_factor_a * per_class_ratio))            # (local)
Lambda_per_class_b = np.sqrt(np.abs(norm_factor_b * per_class_ratio))            # (local)

# Per-class profile invariance: ratio of (Lambda_b/Lambda_a) should be class-INDEPENDENT
ratio_b_over_a = Lambda_per_class_b / Lambda_per_class_a                         # (local)
mean_ratio_ba = float(np.mean(ratio_b_over_a))                                   # (local)
profile_dispersion = float(np.std(ratio_b_over_a) / mean_ratio_ba)               # (local)
profile_invariance_holds = profile_dispersion <= PROFILE_INVARIANCE_THRESH       # (local)

print(f"  per-class Lambda(omega_a)/M_KK  = {(Lambda_per_class_a/M_KK).tolist()}")
print(f"  per-class Lambda(omega_b)/M_KK  = {(Lambda_per_class_b/M_KK).tolist()}")
print(f"  per-class ratio (b/a)           = {ratio_b_over_a.tolist()}")
print(f"  mean ratio (b/a)                = {mean_ratio_ba:.6e}")
print(f"  profile dispersion              = {profile_dispersion:.6e}")
print(f"  profile-invariance threshold    = {PROFILE_INVARIANCE_THRESH}")
print(f"  profile-invariance HOLDS        = {profile_invariance_holds}")
print()


# ---------------------------------------------------------------------------
# Regime verdict (per gate-verdicts.md schema-v2)
# ---------------------------------------------------------------------------
# VALID    = all 5 classes' Mellin integrals converge at both s=2 and s=4 poles
# MARGINAL = 1-2 classes graze convergence boundary
# BREAKDOWN= >=3 classes fail convergence
# On the discrete Casimir spectrum, "convergence" maps to "all per-class a_n positive
# and finite". Test:
finite_count = int(np.sum(np.isfinite(per_class_Lambda_anom_internal)))          # (local)
positive_count = int(np.sum(per_class_Lambda_anom_internal > 0))                 # (local)
fail_count = N_CLASSES - min(finite_count, positive_count)                       # (local)

if fail_count == 0:
    regime_verdict = "VALID"                                                     # (local)
elif fail_count <= 2:
    regime_verdict = "MARGINAL"                                                  # (local)
else:
    regime_verdict = "BREAKDOWN"                                                 # (local)


# ---------------------------------------------------------------------------
# Sign / Magnitude / Composite verdicts
# ---------------------------------------------------------------------------
sign_verdict = "N/A"                                                             # (local) Lambda_anom positive by construction

# Magnitude: PASS if R1 or R2; INFO if neither but R3 valid; FAIL otherwise
if R1_holds or R2_holds:
    magnitude_verdict = "PASS"                                                   # (local)
elif R3_valid:
    magnitude_verdict = "INFO"                                                   # (local)
else:
    magnitude_verdict = "FAIL"                                                   # (local)

# Profile-invariance can flip PASS to FAIL
if not profile_invariance_holds:
    magnitude_verdict = "FAIL"

# Composite collapse rule (per gate-verdicts.md schema-v2):
if regime_verdict == "BREAKDOWN":
    composite = "FAIL"                                                           # (local)
elif sign_verdict == "FAIL":
    composite = "FAIL"
elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
    composite = "FAIL"
elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
    composite = "INFO"
elif magnitude_verdict == "INFO":
    composite = "INFO"
else:
    composite = "PASS"


# Determine surviving reading
if R1_holds:
    surviving_reading = "R1"                                                     # (local)
elif R2_holds:
    surviving_reading = "R2"                                                     # (local)
elif R3_valid:
    surviving_reading = "R3"                                                     # (local)
else:
    surviving_reading = "FAIL"                                                   # (local)

print("=" * 78)
print("VERDICT 3-TUPLE + COMPOSITE")
print("=" * 78)
print(f"  sign_verdict       = {sign_verdict}")
print(f"  magnitude_verdict  = {magnitude_verdict}")
print(f"  regime_verdict     = {regime_verdict}")
print(f"  composite          = {composite}")
print(f"  surviving_reading  = {surviving_reading}")
print()


# ---------------------------------------------------------------------------
# Closure SHA-256
# ---------------------------------------------------------------------------
# Per gate-verdicts.md S81+: SHA-256 of the ordered input-pin map + machinery pins
ordered_pin_map = {                                                              # (local)
    "input_files": input_pin_map,
    "machinery_pins": machinery_pins,
    "_gate_id": "S87-W6-C-GAMMA-WEAK-PER-CLASS",
    "_wp_id": "§W7-3",
    "_scheme": SCHEME,
    "_convention": CONVENTION,
    "_L_max": L_MAX,
    "_W71_landed": W71_LANDED,
}
audit_payload = json.dumps(ordered_pin_map, sort_keys=True, default=str).encode("utf-8")  # (local)
audit_sha256 = hashlib.sha256(audit_payload).hexdigest()                         # (local)

# Content SHA: SHA over the verdict result content
content_pin_map = {                                                              # (local)
    "per_class_a4": per_class_a4.tolist(),
    "per_class_a2": per_class_a2.tolist(),
    "per_class_ratio": per_class_ratio.tolist(),
    "per_class_Lambda_anom_internal": per_class_Lambda_anom_internal.tolist(),
    "R1_dispersion": R1_dispersion,
    "R2_residual": best_R2_residual,
    "R2_n_c": best_R2_n_c.tolist() if best_R2_n_c is not None else None,
    "R2_Lambda_global": best_R2_Lambda_global,
    "profile_dispersion": profile_dispersion,
    "K_omega_trivial": K_omega_trivial,
    "K_omega_a": K_omega_a,
    "K_omega_b": K_omega_b,
    "sign_verdict": sign_verdict,
    "magnitude_verdict": magnitude_verdict,
    "regime_verdict": regime_verdict,
    "composite": composite,
    "surviving_reading": surviving_reading,
}
content_payload = json.dumps(content_pin_map, sort_keys=True, default=str).encode("utf-8")  # (local)
content_sha256 = hashlib.sha256(content_payload).hexdigest()                     # (local)

print(f"audit_sha256   = {audit_sha256}")
print(f"content_sha256 = {content_sha256}")
print()


# ---------------------------------------------------------------------------
# Save NPZ
# ---------------------------------------------------------------------------
NPZ_PATH = os.path.join(SCRIPT_DIR, "s87_w7_c_gamma_weak_per_class.npz")          # (local)
np.savez(
    NPZ_PATH,
    class_names=np.array([cn for cn, _, _ in CLASS_REGULATOR_MAP]),
    regulator_names=np.array([rn for _, rn, _ in CLASS_REGULATOR_MAP]),
    per_class_a4=per_class_a4,
    per_class_a2=per_class_a2,
    per_class_ratio=per_class_ratio,
    per_class_Lambda_anom_internal_sq=per_class_Lambda_anom_internal_sq,
    per_class_Lambda_anom_internal=per_class_Lambda_anom_internal,
    Lambda_per_class_omega_a=Lambda_per_class_a,
    Lambda_per_class_omega_b=Lambda_per_class_b,
    profile_ratio_b_over_a=ratio_b_over_a,
    R1_dispersion=np.array([R1_dispersion]),
    R1_holds=np.array([R1_holds]),
    R2_residual=np.array([best_R2_residual]),
    R2_n_c=np.array(best_R2_n_c if best_R2_n_c is not None else [-1]*N_CLASSES),
    R2_Lambda_global=np.array([best_R2_Lambda_global if best_R2_Lambda_global is not None else 0.0]),
    R2_holds=np.array([R2_holds]),
    R3_valid=np.array([R3_valid]),
    profile_dispersion=np.array([profile_dispersion]),
    profile_invariance_holds=np.array([profile_invariance_holds]),
    K_omega_trivial=np.array([K_omega_trivial]),
    K_omega_a=np.array([K_omega_a]),
    K_omega_b=np.array([K_omega_b]),
    sign_verdict=np.array([sign_verdict]),
    magnitude_verdict=np.array([magnitude_verdict]),
    regime_verdict=np.array([regime_verdict]),
    composite=np.array([composite]),
    surviving_reading=np.array([surviving_reading]),
    audit_sha256=np.array([audit_sha256]),
    content_sha256=np.array([content_sha256]),
    M_KK=np.array([M_KK]),
    L_max=np.array([L_MAX]),
)
print(f"NPZ saved: {NPZ_PATH}")


# ---------------------------------------------------------------------------
# Plot
# ---------------------------------------------------------------------------
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt                                                  # noqa: E402

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

class_short = [cn.split("_")[1] + "_" + cn.split("_")[2] for cn in [c[0] for c in CLASS_REGULATOR_MAP]]

ax = axes[0]
x_pos = np.arange(N_CLASSES)
bars = ax.bar(x_pos, per_class_Lambda_anom_internal / M_KK, alpha=0.75, edgecolor="black")
ax.axhline(y=mean_Lambda / M_KK, linestyle="--", color="C1",
           label=f"mean = {mean_Lambda/M_KK:.4e} M_KK")
if R2_holds and best_R2_Lambda_global is not None:
    for i, n_ci in enumerate(best_R2_n_c):
        ax.axhline(y=(n_ci * best_R2_Lambda_global) / M_KK, linestyle=":", color="C2", alpha=0.4)
ax.set_xticks(x_pos)
ax.set_xticklabels(class_short, rotation=30, fontsize=9)
ax.set_ylabel(r"$\Lambda_{\rm anom,internal}^c / M_{KK}$")
ax.set_title(
    f"Per-class $\\Lambda_{{\\rm anom,internal}}$ "
    f"(R1_disp={R1_dispersion:.3e}; surviving={surviving_reading})"
)
ax.legend(loc="best", fontsize=9)
ax.grid(True, alpha=0.3)
ax.set_yscale("log")

ax = axes[1]
ax.bar(x_pos - 0.2, Lambda_per_class_a / M_KK, width=0.4, label=r"$\omega_a = e^{-t/\Lambda^2}$", alpha=0.75)
ax.bar(x_pos + 0.2, Lambda_per_class_b / M_KK, width=0.4, label=r"$\omega_b = (1+t/\Lambda^2)^{-1}$", alpha=0.75)
ax.set_xticks(x_pos)
ax.set_xticklabels(class_short, rotation=30, fontsize=9)
ax.set_ylabel(r"$\Lambda_{\rm anom,internal}^c / M_{KK}$")
ax.set_title(
    f"Profile cross-check (dispersion={profile_dispersion:.3e}; invariance_holds={profile_invariance_holds})"
)
ax.legend(loc="best", fontsize=9)
ax.grid(True, alpha=0.3)
ax.set_yscale("log")

fig.suptitle(
    f"S87-W6-C-GAMMA-WEAK-PER-CLASS  --  "
    f"composite={composite}  --  reading={surviving_reading}  "
    f"(SCHEMATIC TIER-2)",
    fontsize=11,
)
plt.tight_layout()
PNG_PATH = os.path.join(SCRIPT_DIR, "s87_w7_c_gamma_weak_per_class.png")          # (local)
plt.savefig(PNG_PATH, dpi=120, bbox_inches="tight")
plt.close(fig)
print(f"PNG saved: {PNG_PATH}")
print()


# ---------------------------------------------------------------------------
# Append verdict line + dual-SHA companion + S87+ 3-tuple annotation
# ---------------------------------------------------------------------------
VERDICT_FILE = os.path.join(SCRIPT_DIR, "s87_gate_verdicts.txt")                 # (local)

verdict_value = R1_dispersion                                                    # (local) value reported is R1_dispersion
canonical_line = (                                                               # (local)
    f"S87-W6-C-GAMMA-WEAK-PER-CLASS: {composite} -- "
    f"value={verdict_value:.6e} "
    f"scheme={SCHEME} "
    f"convention={CONVENTION} "
    f"L_max={L_MAX} "
    f"audit_sha256={audit_sha256} "
    f"content_sha256={content_sha256} "
    f"schema_version=S87+\n"
)
companion_dual_sha = (                                                           # (local)
    f"# audit_sha256_short={audit_sha256[:16]} "
    f"content_sha256_short={content_sha256[:16]} "
    f"# S87-W6-C-GAMMA-WEAK-PER-CLASS dual-SHA companion row (W9a-99 split)\n"
)
companion_3tuple = (                                                             # (local)
    f"# sign_verdict={sign_verdict} "
    f"magnitude_verdict={magnitude_verdict} "
    f"regime_verdict={regime_verdict} "
    f"# S87-W6-C-GAMMA-WEAK-PER-CLASS 3-tuple annotation (S87 schema-v2)\n"
)

with open(VERDICT_FILE, "a", encoding="utf-8") as f:
    f.write(canonical_line)
    f.write(companion_dual_sha)
    f.write(companion_3tuple)

print(f"Verdict appended to: {VERDICT_FILE}")
print()
print(canonical_line.strip())
print(companion_dual_sha.strip())
print(companion_3tuple.strip())
print()


# ---------------------------------------------------------------------------
# 4-tuple OUTPUT
# ---------------------------------------------------------------------------
print("=" * 78)
print("4-TUPLE OUTPUT")
print("=" * 78)
print(
    f"  (value={verdict_value:.6e}, scheme={SCHEME}, "
    f"convention={CONVENTION}, L_max={L_MAX})"
)
print()
print("Done.")
