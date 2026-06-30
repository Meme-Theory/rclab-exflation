"""
s88_w13_w7_3_c_gamma_weak_tier1_lift.py — S88-W7-3-C-GAMMA-WEAK-PRIMARY-LIFT
============================================================================

Gate: S88-W7-3-C-GAMMA-WEAK-PRIMARY-LIFT  ([VERIFY])
Plan: sessions/session-plan/session-88-plan-w13.md §W13-159
Trigger: [VERIFY]
Classification: COMPUTE-class

PRIMARY full-physical Pauli-Villars (per `substrate-first-canonical-sourcing.md`
§iv) lift of the W7-3 SCHEMATIC C-γ-WEAK per-L1-class evaluation
(`s87_w7_c_gamma_weak_per_class.py`, S87-W6-C-GAMMA-WEAK-PER-CLASS PASS at
audit_sha256=0eb96f0536...). Operates on the 155,984-eigenvalue L_max=10
sub-spectrum filtered from `s84_spectrum_cache_L12_tau019.npz` master cache.

Hypothesis: PRIMARY full-physical Pauli-Villars regularization with mass-scale
running per Connes-Chamseddine 1996 §2.2-2.3 reproduces the W7-3 SCHEMATIC
integer-graded anomaly multiplier signature {n_c} = (10, 10, 10, 11, 13) AND
the global anomaly scale Λ_global = 5.326e+14 GeV ≈ 7.169e-03 · M_KK with
profile-invariance ≤ 1.49e-16.

PASS criterion (plan §W13-159 thresholds):
  PASS  iff {n_c}_TIER1 = (10, 10, 10, 11, 13)
        AND |Λ_global_TIER1 − 5.326e+14| / 5.326e+14 < 1.49e-16
        AND profile-invariance ≤ 1.49e-16
  FAIL  iff any deviation beyond profile-invariance bound
  INFO  iff deviation within factor-of-2 of bound

Substitution chain (PRIMARY-vs-SCHEMATIC propagation; per math-scripts.md
§"Double-Check Logic Before Compute"):

  Step 1 (definitions):
    K_c(t)   = Σ_{k in class c} m_k exp(-t λ_k²)         (heat-kernel restricted to class c)
    M_R^c(s) = Σ_{k in class c} m_k · w_R(λ_k², s) · λ_k^{-2s}    (Mellin moment under regulator R)
    Λ_anom_int_c² = K_ω · (M_R^c(s=4) / M_R^c(s=2)) · M_KK² / (16 π²)
                                                          (per AC-2010 §V Eq. 5.2 / W7-3 Step 3)
    {n_c}    = round(Λ_anom_int_c / Λ_global)             where Λ_global = min(Λ_anom_int_c) / k

    Class -> regulator multiplier w_R:
      Class 1 (zeta):           w_R = 1                     (bare moment)
      Class 2 (SDW = Mellin):   w_R = 1                     (= zeta on positive spectrum)
      Class 3 (Zubarev = HK):   w_R = exp(-t_ref · λ²)      (heat-kernel dressing)
      Class 4 (cutoff_sqrt):    w_R = 1[λ² ≤ 0.7·λ²_max]    (hard truncation)
      Class 5 (anomaly = PV):
        SCHEMATIC: w_R = 1 - (M_PV²/(λ²+M_PV²))^s            (single subtraction; M_PV²=0.1·λ²_max)
        PRIMARY:   w_R = 1 - Σ_{r=1,2} c_r · (m_r²/(λ²+m_r²))^s  (2-point PV with mass-scale running
                                                                  per Connes-Chamseddine 1996 §2.2-2.3;
                                                                  c_1=+2, c_2=-1, m_1=1, m_2=√2)

  Step 2 (substitution):
    For classes 1-4: no PV factor → ratio_PRIM_c = ratio_SCH_c IDENTICALLY.
    For class 5:    ratio_PRIM_5 = M_PRIM(s=4) / M_PRIM(s=2)
                    differs from ratio_SCH_5 = M_SCH(s=4) / M_SCH(s=2)
                    by the PRIMARY-vs-SCHEMATIC propagation factor δ.

  Step 3 (simplification):
    Define (a_4^c / a_2^c)_R := ratio_R^c. Then
      Λ_anom_int_c = sqrt(K_ω · M_KK² · ratio_R^c / (16 π²))
    Per W7-3 PASS-R2: anchoring at min-class with k_anchor = 6 yields
      Λ_global = Λ_min / 6
    and {n_c} = round(Λ_anom_int_c / Λ_global).
    The class-5 ratio shift Δratio_5 = ratio_PRIM_5 − ratio_SCH_5 propagates
    to Λ_anom_int_5 by half-power: ΔΛ_5/Λ_5 ≈ (1/2)·Δratio_5/ratio_5.

  Step 4 (direction):
    PASS iff
      (a) the 4 bare classes' ratios are unchanged (TRUE BY CONSTRUCTION
          since w_R = 1, exp(-tλ²), or 1[λ²≤cutoff] do not invoke PV);
      (b) the class-5 PRIMARY ratio is sufficiently close to SCHEMATIC
          that the integer-fit residual < R2_INTEGER_FIT_RESIDUAL = 0.05
          AND n_5_PRIM = round(Λ_anom_int_5_PRIM / Λ_global_PRIM) = 13.

Tier-1 PRIMARY pin per `substrate-first-canonical-sourcing.md` §iv:
  scheme = pauli-villars-level-1-mass-scale-running-connes-chamseddine-1996
  convention = per-L1-class-evaluation-profile-invariance-1p49e-16
  L_max = 10 (operational; cache filtered)
  CLASS pin = TIER-1 PRIMARY (full-physical, NOT SCHEMATIC)

Profile-invariance cross-check (Step F): re-evaluate ratio_R^c under TWO
Weyl profiles ω_a(t) = exp(-t/Λ²) and ω_b(t) = (1+t/Λ²)^(-1); per Step 3
of the substitution chain the K_ω class-independent normalization cancels,
so the per-class Λ_anom_int_c rescales by a CONSTANT factor across all 5
classes — the structural 5-class signature is profile-invariant by
construction.

Output 4-tuple:
  (value=R1_dispersion_TIER1, scheme=pauli-villars-level-1-mass-scale-running-connes-chamseddine-1996,
   convention=per-L1-class-evaluation-profile-invariance-1p49e-16, L_max=10)
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import math
import json
import hashlib
import time
from pathlib import Path

import numpy as np

# Project paths
SCRIPT_PATH = Path(__file__).resolve()                                          # (local)
SCRIPT_DIR = SCRIPT_PATH.parent                                                  # (local)
PROJECT_ROOT = SCRIPT_DIR.parent.parent                                          # (local)
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"                           # (local)
COMPUTATIONS_DIR = PROJECT_ROOT / "computations"                                 # (local)

# Add canonical_constants on path
sys.path.insert(0, str(SHARED_DIR))
sys.path.insert(0, str(COMPUTATIONS_DIR))

from canonical_constants import M_KK, Vol_SU3_Haar, PI                            # noqa: E402
from _pauli_villars_subtraction import (                                          # noqa: E402
    pv_mellin_moment_primary,
    pv_mellin_moment_schematic,
    bare_mellin_moment,
    heat_kernel_mellin_moment,
    hard_cutoff_mellin_moment,
    PV_PRIMARY_C,
    PV_PRIMARY_M_DIMLESS,
)

# ---------------------------------------------------------------------------
# Pre-registration pins
# ---------------------------------------------------------------------------
GATE_ID = "S88-W7-3-C-GAMMA-WEAK-PRIMARY-LIFT"                                   # (local)
SCHEME = "pauli-villars-level-1-mass-scale-running-connes-chamseddine-1996"      # (local)
CONVENTION = "per-L1-class-evaluation-profile-invariance-1p49e-16"               # (local)
L_MAX = 10                                                                       # (local)
N_CLASSES = 5                                                                    # (local) L1 partition cardinality
TIER_PIN = "TIER-1 PRIMARY"                                                      # (local) per substrate-first-canonical-sourcing.md §iv

# Pre-registered W7-3 SCHEMATIC reference values (frozen at plan-freeze)
N_C_REFERENCE = (10, 10, 10, 11, 13)                                              # (local)
LAMBDA_GLOBAL_REFERENCE = 5.326e+14                                              # (local) [GeV]
PROFILE_INVARIANCE_REFERENCE = 1.49e-16                                           # (local)

# PASS thresholds (plan §W13-159)
N_C_PASS_TUPLE = (10, 10, 10, 11, 13)                                             # (local) integer-tuple match
LAMBDA_REL_DEV_PASS = 1.49e-16                                                    # (local) relative deviation pass
PROFILE_INV_PASS = 1.49e-16                                                       # (local) profile-invariance pass
PROFILE_INV_INFO = 2.0 * PROFILE_INV_PASS                                         # (local) factor-of-2 INFO band
LAMBDA_REL_DEV_INFO = 2.0 * LAMBDA_REL_DEV_PASS                                   # (local) factor-of-2 INFO band

# R2 integer-fit residual (from W7-3 SCHEMATIC; for n_c reproduction)
R2_INTEGER_FIT_RESIDUAL = 0.05                                                    # (local) RATIO

# Heat-kernel reference time for Zubarev class
T_REF_ZUBAREV = 1.0e-3                                                            # (local) [M_KK^-2 dimensionless]

# Hard-cutoff fraction for cutoff_sqrt class
HARD_CUTOFF_FRAC = 0.7                                                            # (local)

# SCHEMATIC PV mass-fraction (matches `_spectral_action_regulators.pauli_villars_a_n` default)
M_PV_SQ_FRAC_SCH = 0.1                                                            # (local)

# Print header
print("=" * 78)
print(f"{GATE_ID}")
print(f"Plan: sessions/session-plan/session-88-plan-w13.md §W13-159")
print(f"Tier: {TIER_PIN}  (per substrate-first-canonical-sourcing.md §iv)")
print("=" * 78)
print()


# ---------------------------------------------------------------------------
# Section 1 — SHA-256 input pin map
# ---------------------------------------------------------------------------
def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


CACHE_PATH = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"  # (local)
PV_HELPER_PATH = COMPUTATIONS_DIR / "_pauli_villars_subtraction.py"                 # (local)
CANONICAL_PATH = SHARED_DIR / "canonical_constants.py"                              # (local)
W7_3_VERDICT_PATH = COMPUTATIONS_DIR / "session-87" / "s87_gate_verdicts.txt"       # (local)

INPUT_PIN_MAP = {                                                                   # (local)
    "s84_spectrum_cache_L12_tau019.npz": file_sha256(CACHE_PATH),
    "_pauli_villars_subtraction.py": file_sha256(PV_HELPER_PATH),
    "canonical_constants.py": file_sha256(CANONICAL_PATH),
    "s87_gate_verdicts.txt": file_sha256(W7_3_VERDICT_PATH),
    "_script_sha__": file_sha256(SCRIPT_PATH),
    "_gate_id_": GATE_ID,
    "_scheme_": SCHEME,
    "_convention_": CONVENTION,
    "_L_max_": str(L_MAX),
    "_tier_pin_": TIER_PIN,
}

print("INPUT PIN MAP:")
for k, v in INPUT_PIN_MAP.items():
    if isinstance(v, str) and len(v) >= 32:
        print(f"  {k:48s}  {v[:16]}…")
    else:
        print(f"  {k:48s}  {v}")
print()


# ---------------------------------------------------------------------------
# Section 2 — Load L_max=10 spectrum from L_max=12 master cache
# ---------------------------------------------------------------------------
print(f"Loading L_max={L_MAX} spectrum from {CACHE_PATH.name} ...")
data = np.load(CACHE_PATH, allow_pickle=True)
sectors = data["sector_evals"].item()                                               # (local)

lambdas_list = []                                                                   # (local)
mults_list = []                                                                     # (local)
n_lines = 0                                                                         # (local)
n_sectors = 0                                                                       # (local)
n_weighted = 0                                                                      # (local)
for (p, q), v in sectors.items():
    if (p, q) == (0, 0):
        continue
    if v["level"] > L_MAX:
        continue
    ev = np.asarray(v["abs_evals"], dtype=np.float64)
    dim = int(v["dim"])
    lambdas_list.append(ev)
    mults_list.append(np.full_like(ev, dim, dtype=np.float64))
    n_lines += len(ev)
    n_sectors += 1
    n_weighted += len(ev) * dim

lambdas_full = np.concatenate(lambdas_list)                                         # (local)
mults_full = np.concatenate(mults_list)                                             # (local)

lam_min = float(np.min(lambdas_full))                                               # (local)
lam_max = float(np.max(lambdas_full))                                               # (local)

print(f"  sectors loaded:        {n_sectors}")
print(f"  distinct eigenvalue lines: {n_lines}")
print(f"  weighted total m_k counted: {n_weighted}")
print(f"  λ_min:                {lam_min:.6f}")
print(f"  λ_max:                {lam_max:.6f}")
print()


# ---------------------------------------------------------------------------
# Section 3 — PRIMARY 2-point PV consistency self-check
# ---------------------------------------------------------------------------
sum_c = float(np.sum(PV_PRIMARY_C))                                                 # (local)
sum_cm2 = float(np.sum(PV_PRIMARY_C * PV_PRIMARY_M_DIMLESS ** 2))                   # (local)
print("PV PRIMARY consistency:")
print(f"  c_arr = {PV_PRIMARY_C.tolist()}")
print(f"  m_arr = {PV_PRIMARY_M_DIMLESS.tolist()}")
print(f"  Σ c_r          = {sum_c:.16e}  (target 1.0)")
print(f"  Σ c_r · m_r²   = {sum_cm2:.16e}  (target 0.0)")
assert abs(sum_c - 1.0) < 1e-15
assert abs(sum_cm2) < 1e-15
print()


# ---------------------------------------------------------------------------
# Section 4 — Per-class PRIMARY Mellin moments at s=2 and s=4
# ---------------------------------------------------------------------------
# 5-class L1 partition (per W7-3 / s86-sector-2-split-layer-taxonomy.md C1):
#   Class 1: zeta              -- bare moment
#   Class 2: SDW = Mellin      -- bare moment (algebraic identity to zeta)
#   Class 3: Zubarev = HK      -- heat-kernel dressed (exp(-t·λ²))
#   Class 4: cutoff_sqrt       -- hard truncation (λ² ≤ 0.7·λ²_max)
#   Class 5: anomaly = PV      -- PRIMARY 2-point Pauli-Villars (this gate)

CLASS_NAMES = [                                                                     # (local)
    "Class_1_zeta",
    "Class_2_SDW",
    "Class_3_Zubarev",
    "Class_4_cutoff_sqrt",
    "Class_5_anomaly_PV_PRIMARY",
]
REGULATOR_NAMES = [                                                                 # (local)
    "zeta",
    "Mellin",
    "heat-kernel",
    "hard-cutoff",
    "Pauli-Villars-PRIMARY",
]


def class_moment_primary(class_idx, s, lambdas, mults):
    """Mellin moment per class at index s, using PRIMARY full-physical regulators."""
    if class_idx in (0, 1):  # zeta or SDW: bare
        return bare_mellin_moment(s, lambdas, mults)
    if class_idx == 2:        # Zubarev / heat-kernel
        return heat_kernel_mellin_moment(s, lambdas, mults, T_REF_ZUBAREV)
    if class_idx == 3:        # cutoff_sqrt
        return hard_cutoff_mellin_moment(s, lambdas, mults, cutoff_frac=HARD_CUTOFF_FRAC)
    if class_idx == 4:        # PV PRIMARY (Connes-Chamseddine 1996 §2.2-2.3 mass-scale running)
        return pv_mellin_moment_primary(s, lambdas, mults)
    raise ValueError(f"class_idx={class_idx} out of range")


def class_moment_schematic(class_idx, s, lambdas, mults):
    """SCHEMATIC reference (for SCHEMATIC-vs-PRIMARY propagation comparison)."""
    if class_idx in (0, 1):
        return bare_mellin_moment(s, lambdas, mults)
    if class_idx == 2:
        return heat_kernel_mellin_moment(s, lambdas, mults, T_REF_ZUBAREV)
    if class_idx == 3:
        return hard_cutoff_mellin_moment(s, lambdas, mults, cutoff_frac=HARD_CUTOFF_FRAC)
    if class_idx == 4:
        # SCHEMATIC matches `_spectral_action_regulators.pauli_villars_a_n`:
        # M_PV² = 0.1 · max(λ²) on the L_max=10 cache spectrum.
        c_max_sq = float(np.max(lambdas * lambdas))
        return pv_mellin_moment_schematic(s, lambdas, mults, M_PV_sq=M_PV_SQ_FRAC_SCH * c_max_sq)
    raise ValueError(f"class_idx={class_idx} out of range")


print("STEP A — per-class Mellin moments under PRIMARY (and SCHEMATIC for comparison):")
print()
print(f"  {'Class':28s}  {'M_PRIM(s=2)':>16s}  {'M_PRIM(s=4)':>16s}  "
      f"{'ratio_PRIM':>14s}  {'ratio_SCH':>14s}")

per_class_M2_prim = np.zeros(N_CLASSES)                                             # (local)
per_class_M4_prim = np.zeros(N_CLASSES)                                             # (local)
per_class_ratio_prim = np.zeros(N_CLASSES)                                          # (local)
per_class_M2_sch = np.zeros(N_CLASSES)                                              # (local)
per_class_M4_sch = np.zeros(N_CLASSES)                                              # (local)
per_class_ratio_sch = np.zeros(N_CLASSES)                                           # (local)

for ci in range(N_CLASSES):
    m2_p = class_moment_primary(ci, 2.0, lambdas_full, mults_full)
    m4_p = class_moment_primary(ci, 4.0, lambdas_full, mults_full)
    m2_s = class_moment_schematic(ci, 2.0, lambdas_full, mults_full)
    m4_s = class_moment_schematic(ci, 4.0, lambdas_full, mults_full)
    per_class_M2_prim[ci] = m2_p
    per_class_M4_prim[ci] = m4_p
    per_class_ratio_prim[ci] = m4_p / m2_p
    per_class_M2_sch[ci] = m2_s
    per_class_M4_sch[ci] = m4_s
    per_class_ratio_sch[ci] = m4_s / m2_s
    print(f"  {CLASS_NAMES[ci]:28s}  "
          f"{m2_p:16.6e}  {m4_p:16.6e}  "
          f"{per_class_ratio_prim[ci]:14.6e}  {per_class_ratio_sch[ci]:14.6e}")
print()


# ---------------------------------------------------------------------------
# Section 5 — Per-class Λ_anom_internal under PRIMARY
# ---------------------------------------------------------------------------
# Per W7-3 Step 3:
#   Λ_anom_int_c² = K_ω · M_KK² · (a_4^c / a_2^c) / (16 π²)
# K_ω = (Γ(4)/Γ(2)) = 6 for the trivial (omega → 1) profile.
K_OMEGA_TRIVIAL = math.gamma(4) / math.gamma(2)                                     # (local) = 6
M_KK_SQ = M_KK * M_KK                                                               # (local)
NORM_FACTOR = K_OMEGA_TRIVIAL * M_KK_SQ / (16.0 * PI ** 2)                          # (local)

per_class_Lambda_sq_prim = NORM_FACTOR * per_class_ratio_prim                       # (local) [GeV^2]
per_class_Lambda_prim = np.sqrt(np.abs(per_class_Lambda_sq_prim))                   # (local) [GeV]

print("STEP B — per-class Λ_anom_internal_c (PRIMARY):")
print(f"  K_ω (trivial profile)     = Γ(4)/Γ(2) = {K_OMEGA_TRIVIAL:.6f}")
print(f"  M_KK                       = {M_KK:.6e}  GeV")
print(f"  norm_factor (K_ω·M_KK²/(16π²)) = {NORM_FACTOR:.6e}  GeV²")
print()
print(f"  {'Class':28s}  {'Λ²_anom_int_c [GeV²]':>22s}  "
      f"{'Λ_anom_int_c [GeV]':>22s}  {'Λ/M_KK':>14s}")
for ci in range(N_CLASSES):
    print(f"  {CLASS_NAMES[ci]:28s}  "
          f"{per_class_Lambda_sq_prim[ci]:22.6e}  "
          f"{per_class_Lambda_prim[ci]:22.6e}  "
          f"{per_class_Lambda_prim[ci]/M_KK:14.6e}")
print()


# ---------------------------------------------------------------------------
# Section 6 — R2 integer-fit on PRIMARY: best Λ_global + {n_c}
# ---------------------------------------------------------------------------
# R2: Λ_anom_int_c = Λ_global · n_c, n_c ∈ ℤ_+.
# Strategy (matches W7-3 SCHEMATIC): pick anchor = min(Λ_anom_int_c),
# candidate Λ_global = anchor / k for k=1..15; compute n_c = round(Λ/Λ_global);
# residual = max_c |actual - integer·Λ_global| / Λ.
print("STEP C — READING R2 (class-FACTORIZED with integer multipliers):")

best_R2_residual = float("inf")                                                     # (local)
best_R2_n_c = None                                                                  # (local)
best_R2_Lambda_global = None                                                        # (local)
best_R2_anchor_k = None                                                             # (local)

Lambda_min_prim = float(np.min(per_class_Lambda_prim))                              # (local)
for k_anchor in range(1, 16):
    Lg_candidate = Lambda_min_prim / k_anchor                                       # (local)
    if Lg_candidate <= 0:
        continue
    n_c_float = per_class_Lambda_prim / Lg_candidate                                # (local)
    n_c_int = np.round(n_c_float).astype(int)                                       # (local)
    if np.any(n_c_int <= 0):
        continue
    fitted = n_c_int * Lg_candidate                                                 # (local)
    residual_per_class = np.abs(per_class_Lambda_prim - fitted) / per_class_Lambda_prim  # (local)
    max_residual = float(np.max(residual_per_class))                                # (local)
    if max_residual < best_R2_residual:
        best_R2_residual = max_residual
        best_R2_n_c = n_c_int.copy()
        best_R2_Lambda_global = Lg_candidate
        best_R2_anchor_k = k_anchor

n_c_TIER1 = tuple(int(x) for x in best_R2_n_c) if best_R2_n_c is not None else None
Lambda_global_TIER1 = best_R2_Lambda_global

print(f"  anchor k                   = {best_R2_anchor_k}")
print(f"  Λ_global_TIER1             = {Lambda_global_TIER1:.6e}  GeV")
print(f"  Λ_global_TIER1 / M_KK      = {Lambda_global_TIER1 / M_KK:.6e}")
print(f"  {{n_c}}_TIER1               = {n_c_TIER1}")
print(f"  R2 residual (max)          = {best_R2_residual:.6e}")
print(f"  R2 PASS threshold          = {R2_INTEGER_FIT_RESIDUAL}")
print()
print(f"  Reference (W7-3 SCHEMATIC):")
print(f"    {{n_c}}_REF               = {N_C_REFERENCE}")
print(f"    Λ_global_REF             = {LAMBDA_GLOBAL_REFERENCE:.6e}  GeV")
print()


# ---------------------------------------------------------------------------
# Section 7 — Reproduction tests (n_c match + Λ_global relative deviation)
# ---------------------------------------------------------------------------
n_c_match = (n_c_TIER1 == N_C_PASS_TUPLE)                                           # (local)
Lambda_rel_dev = abs(Lambda_global_TIER1 - LAMBDA_GLOBAL_REFERENCE) / LAMBDA_GLOBAL_REFERENCE  # (local)
Lambda_match_PASS = (Lambda_rel_dev < LAMBDA_REL_DEV_PASS)                          # (local)
Lambda_match_INFO = (Lambda_rel_dev < LAMBDA_REL_DEV_INFO)                          # (local)

print("STEP D — Reproduction tests:")
print(f"  n_c_TIER1 == n_c_REF?       = {n_c_match}")
print(f"    n_c_TIER1                = {n_c_TIER1}")
print(f"    n_c_REF                  = {N_C_PASS_TUPLE}")
print(f"  |Λ_TIER1 − Λ_REF|/Λ_REF    = {Lambda_rel_dev:.6e}")
print(f"  PASS threshold (1.49e-16)  = {LAMBDA_REL_DEV_PASS:.6e}")
print(f"  INFO threshold (2× PASS)   = {LAMBDA_REL_DEV_INFO:.6e}")
print(f"  Λ match PASS                = {Lambda_match_PASS}")
print(f"  Λ match INFO                = {Lambda_match_INFO}")
print()


# ---------------------------------------------------------------------------
# Section 8 — Profile-invariance Step F (PRIMARY)
# ---------------------------------------------------------------------------
# Per Step 3 of W7-3 substitution chain, K_ω(profile_a) and K_ω(profile_b)
# enter as a class-INDEPENDENT scalar normalization. The per-class ratio
# (Λ_b / Λ_a) is therefore CONSTANT across all 5 classes, and the structural
# {n_c} signature is profile-INVARIANT by construction.
#
# Operationally we evaluate K_ω under two profiles:
#   ω_a(t) = exp(-t / Λ²)   →   M[ω_a; s] = Λ^{2s} · Γ(s)
#   ω_b(t) = (1 + t/Λ²)^{-1} →  M[ω_b; s] via numerical Mellin
# and verify dispersion of (Λ_b / Λ_a) across the 5 classes is ≤ 1.49e-16.

print("STEP F — PROFILE-INVARIANCE cross-check (PRIMARY):")
print()


def mellin_omega_a(s, Lambda_val):
    """M[exp(-t/Λ²); s] = Λ^{2s} · Γ(s)."""
    return (Lambda_val ** (2.0 * s)) * math.gamma(s)


def mellin_omega_b_numeric(s, Lambda_val, n_pts=20000, t_max_factor=200.0):
    """M[(1+t/Λ²)^{-1}; s] via log-trapezoidal numerical quadrature."""
    t_min = 1e-6 * Lambda_val ** 2
    t_max = t_max_factor * Lambda_val ** 2
    log_t = np.linspace(np.log(t_min), np.log(t_max), n_pts)
    t = np.exp(log_t)
    omega_b = 1.0 / (1.0 + t / (Lambda_val ** 2))
    integrand = np.power(t, s - 1.0) * omega_b * t  # extra t for log-jacobian
    return float(np.trapezoid(integrand, log_t))


Lambda_ref_profile = M_KK                                                           # (local)
mu_a_s4 = mellin_omega_a(4.0, Lambda_ref_profile)                                   # (local)
mu_a_s2 = mellin_omega_a(2.0, Lambda_ref_profile)                                   # (local)
K_omega_a = (mu_a_s4 / mu_a_s2) * (math.gamma(4) / math.gamma(2))                   # (local)

mu_b_s4 = mellin_omega_b_numeric(4.0, Lambda_ref_profile)                           # (local)
mu_b_s2 = mellin_omega_b_numeric(2.0, Lambda_ref_profile)                           # (local)
K_omega_b = (mu_b_s4 / mu_b_s2) * (math.gamma(4) / math.gamma(2))                   # (local)

print(f"  K_ω(profile_a, exp(-t/Λ²))    = {K_omega_a:.6e}")
print(f"  K_ω(profile_b, (1+t/Λ²)^-1)   = {K_omega_b:.6e}")
print()

norm_a = K_omega_a * M_KK_SQ / (16.0 * PI ** 2)                                     # (local)
norm_b = K_omega_b * M_KK_SQ / (16.0 * PI ** 2)                                     # (local)
Lambda_per_class_a = np.sqrt(np.abs(norm_a * per_class_ratio_prim))                 # (local)
Lambda_per_class_b = np.sqrt(np.abs(norm_b * per_class_ratio_prim))                 # (local)

ratio_b_over_a = Lambda_per_class_b / Lambda_per_class_a                            # (local)
mean_ratio_ba = float(np.mean(ratio_b_over_a))                                      # (local)
profile_dispersion = float(np.std(ratio_b_over_a) / abs(mean_ratio_ba)) if mean_ratio_ba != 0 else float("inf")  # (local)

print(f"  per-class Λ(ω_a)/M_KK         = {(Lambda_per_class_a / M_KK).tolist()}")
print(f"  per-class Λ(ω_b)/M_KK         = {(Lambda_per_class_b / M_KK).tolist()}")
print(f"  per-class ratio (b/a)         = {ratio_b_over_a.tolist()}")
print(f"  profile_dispersion (std/|mean|)= {profile_dispersion:.6e}")
print(f"  PASS threshold (1.49e-16)     = {PROFILE_INV_PASS:.6e}")
print(f"  INFO threshold (2× PASS)      = {PROFILE_INV_INFO:.6e}")
print()

profile_invariance_PASS = profile_dispersion <= PROFILE_INV_PASS                    # (local)
profile_invariance_INFO = profile_dispersion <= PROFILE_INV_INFO                    # (local)


# ---------------------------------------------------------------------------
# Section 9 — Composite verdict
# ---------------------------------------------------------------------------
# PASS criterion (plan §W13-159):
#   {n_c}_TIER1 = (10,10,10,11,13)  AND
#   |Λ_global_TIER1 - Λ_REF|/Λ_REF < 1.49e-16  AND
#   profile-invariance ≤ 1.49e-16
#
# FAIL: any deviation beyond profile-invariance bound.
# INFO: deviation within factor-of-2.

# R1 dispersion (reported as `value` per W7-3 lineage)
mean_Lambda = float(np.mean(per_class_Lambda_prim))                                 # (local)
std_Lambda = float(np.std(per_class_Lambda_prim, ddof=0))                           # (local)
R1_dispersion = std_Lambda / mean_Lambda if mean_Lambda > 0 else float("inf")       # (local)

if n_c_match and Lambda_match_PASS and profile_invariance_PASS:
    composite = "PASS"
elif n_c_match and Lambda_match_INFO and profile_invariance_INFO:
    composite = "INFO"
else:
    composite = "FAIL"

# Magnitude verdict per gate-verdicts.md schema-v2
magnitude_verdict = composite                                                       # (local)

# Regime verdict: VALID if all class moments are finite + positive
all_finite = bool(np.all(np.isfinite(per_class_Lambda_prim)))                       # (local)
all_positive = bool(np.all(per_class_Lambda_prim > 0))                              # (local)
if all_finite and all_positive:
    regime_verdict = "VALID"
else:
    regime_verdict = "BREAKDOWN"

# Sign verdict: N/A (no [SIGN] trigger in plan)
sign_verdict = "N/A"

# Composite collapse rule (per gate-verdicts.md)
if regime_verdict == "BREAKDOWN":
    composite = "FAIL"


# ---------------------------------------------------------------------------
# Section 10 — Closure SHA-256 (audit_sha256 + content_sha256)
# ---------------------------------------------------------------------------
ordered_pin_map = {                                                                 # (local)
    "input_files": INPUT_PIN_MAP,
    "_gate_id": GATE_ID,
    "_scheme": SCHEME,
    "_convention": CONVENTION,
    "_L_max": L_MAX,
    "_tier_pin": TIER_PIN,
    "_n_classes": N_CLASSES,
    "_pv_c_arr": PV_PRIMARY_C.tolist(),
    "_pv_m_arr": PV_PRIMARY_M_DIMLESS.tolist(),
    "_t_ref_zubarev": T_REF_ZUBAREV,
    "_hard_cutoff_frac": HARD_CUTOFF_FRAC,
    "_M_PV_sq_frac_SCH": M_PV_SQ_FRAC_SCH,
    "_n_c_REF": list(N_C_REFERENCE),
    "_Lambda_global_REF": LAMBDA_GLOBAL_REFERENCE,
}
audit_payload = json.dumps(ordered_pin_map, sort_keys=True, default=str).encode("utf-8")  # (local)
audit_sha256 = hashlib.sha256(audit_payload).hexdigest()                             # (local)

content_pin_map = {                                                                 # (local)
    "per_class_M2_prim": per_class_M2_prim.tolist(),
    "per_class_M4_prim": per_class_M4_prim.tolist(),
    "per_class_ratio_prim": per_class_ratio_prim.tolist(),
    "per_class_M2_sch": per_class_M2_sch.tolist(),
    "per_class_M4_sch": per_class_M4_sch.tolist(),
    "per_class_ratio_sch": per_class_ratio_sch.tolist(),
    "per_class_Lambda_prim": per_class_Lambda_prim.tolist(),
    "Lambda_per_class_omega_a": Lambda_per_class_a.tolist(),
    "Lambda_per_class_omega_b": Lambda_per_class_b.tolist(),
    "n_c_TIER1": list(n_c_TIER1),
    "Lambda_global_TIER1": Lambda_global_TIER1,
    "best_R2_residual": best_R2_residual,
    "best_R2_anchor_k": best_R2_anchor_k,
    "Lambda_rel_dev": Lambda_rel_dev,
    "n_c_match": n_c_match,
    "Lambda_match_PASS": Lambda_match_PASS,
    "Lambda_match_INFO": Lambda_match_INFO,
    "profile_dispersion": profile_dispersion,
    "profile_invariance_PASS": profile_invariance_PASS,
    "profile_invariance_INFO": profile_invariance_INFO,
    "K_omega_a": K_omega_a,
    "K_omega_b": K_omega_b,
    "K_omega_trivial": K_OMEGA_TRIVIAL,
    "R1_dispersion": R1_dispersion,
    "sign_verdict": sign_verdict,
    "magnitude_verdict": magnitude_verdict,
    "regime_verdict": regime_verdict,
    "composite": composite,
    "M_KK": M_KK,
    "L_max": L_MAX,
}
content_payload = json.dumps(content_pin_map, sort_keys=True, default=str).encode("utf-8")  # (local)
content_sha256 = hashlib.sha256(content_payload).hexdigest()                         # (local)

print("=" * 78)
print(f"VERDICT 3-TUPLE + COMPOSITE")
print("=" * 78)
print(f"  R1_dispersion (value)      = {R1_dispersion:.6e}")
print(f"  n_c_TIER1                   = {n_c_TIER1}")
print(f"  Λ_global_TIER1              = {Lambda_global_TIER1:.6e} GeV")
print(f"  |Λ_TIER1 − Λ_REF|/Λ_REF     = {Lambda_rel_dev:.6e}")
print(f"  profile_dispersion          = {profile_dispersion:.6e}")
print(f"  sign_verdict                = {sign_verdict}")
print(f"  magnitude_verdict           = {magnitude_verdict}")
print(f"  regime_verdict              = {regime_verdict}")
print(f"  composite                   = {composite}")
print()
print(f"  audit_sha256                = {audit_sha256}")
print(f"  content_sha256              = {content_sha256}")
print()


# ---------------------------------------------------------------------------
# Section 11 — Save NPZ
# ---------------------------------------------------------------------------
NPZ_PATH = SCRIPT_DIR / "s88_w13_w7_3_c_gamma_weak_tier1_lift.npz"                  # (local)
np.savez(
    NPZ_PATH,
    class_names=np.array(CLASS_NAMES),
    regulator_names=np.array(REGULATOR_NAMES),
    per_class_M2_prim=per_class_M2_prim,
    per_class_M4_prim=per_class_M4_prim,
    per_class_ratio_prim=per_class_ratio_prim,
    per_class_M2_sch=per_class_M2_sch,
    per_class_M4_sch=per_class_M4_sch,
    per_class_ratio_sch=per_class_ratio_sch,
    per_class_Lambda_sq_prim=per_class_Lambda_sq_prim,
    per_class_Lambda_prim=per_class_Lambda_prim,
    Lambda_per_class_omega_a=Lambda_per_class_a,
    Lambda_per_class_omega_b=Lambda_per_class_b,
    profile_ratio_b_over_a=ratio_b_over_a,
    profile_dispersion=np.array([profile_dispersion]),
    profile_invariance_PASS=np.array([profile_invariance_PASS]),
    profile_invariance_INFO=np.array([profile_invariance_INFO]),
    n_c_TIER1=np.array(n_c_TIER1),
    Lambda_global_TIER1=np.array([Lambda_global_TIER1]),
    best_R2_residual=np.array([best_R2_residual]),
    best_R2_anchor_k=np.array([best_R2_anchor_k]),
    Lambda_rel_dev=np.array([Lambda_rel_dev]),
    n_c_match=np.array([n_c_match]),
    Lambda_match_PASS=np.array([Lambda_match_PASS]),
    Lambda_match_INFO=np.array([Lambda_match_INFO]),
    R1_dispersion=np.array([R1_dispersion]),
    K_omega_a=np.array([K_omega_a]),
    K_omega_b=np.array([K_omega_b]),
    K_omega_trivial=np.array([K_OMEGA_TRIVIAL]),
    n_c_REF=np.array(N_C_REFERENCE),
    Lambda_global_REF=np.array([LAMBDA_GLOBAL_REFERENCE]),
    sign_verdict=np.array([sign_verdict]),
    magnitude_verdict=np.array([magnitude_verdict]),
    regime_verdict=np.array([regime_verdict]),
    composite=np.array([composite]),
    audit_sha256=np.array([audit_sha256]),
    content_sha256=np.array([content_sha256]),
    M_KK=np.array([M_KK]),
    L_max=np.array([L_MAX]),
    tier_pin=np.array([TIER_PIN]),
    pv_primary_c=PV_PRIMARY_C,
    pv_primary_m=PV_PRIMARY_M_DIMLESS,
    n_lines_loaded=np.array([n_lines]),
    n_sectors_loaded=np.array([n_sectors]),
    n_weighted_loaded=np.array([n_weighted]),
    lambda_min=np.array([lam_min]),
    lambda_max=np.array([lam_max]),
)
print(f"NPZ saved: {NPZ_PATH}")


# ---------------------------------------------------------------------------
# Section 12 — Plot
# ---------------------------------------------------------------------------
import matplotlib                                                                    # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt                                                      # noqa: E402

fig, axes = plt.subplots(1, 3, figsize=(20, 6))

ax = axes[0]
x_pos = np.arange(N_CLASSES)
class_short = [
    "zeta", "SDW", "Zubarev", "cutoff_sqrt", "PV_PRIMARY"
]
ax.bar(x_pos - 0.2, per_class_Lambda_prim / M_KK, width=0.4,
       label="PRIMARY (this gate)", alpha=0.85, edgecolor="black", color="C0")
# Overlay {n_c}·Λ_global guides
if n_c_TIER1 is not None and Lambda_global_TIER1 is not None:
    for i, n in enumerate(n_c_TIER1):
        ax.axhline(y=(n * Lambda_global_TIER1) / M_KK, linestyle=":", color="C2",
                   alpha=0.4, linewidth=1)
ax.set_xticks(x_pos)
ax.set_xticklabels(class_short, rotation=20, fontsize=10)
ax.set_ylabel(r"$\Lambda_{\rm anom,int}^{c} / M_{KK}$")
ax.set_yscale("log")
ax.set_title(f"(A) Per-class $\\Lambda_{{\\rm anom,int}}$ PRIMARY  (composite={composite})")
ax.legend(loc="best", fontsize=9)
ax.grid(True, alpha=0.3)

ax = axes[1]
ax.bar(x_pos - 0.2, per_class_ratio_prim, width=0.4, label="PRIMARY", alpha=0.85, color="C0")
ax.bar(x_pos + 0.2, per_class_ratio_sch, width=0.4, label="SCHEMATIC (W7-3)",
       alpha=0.85, color="C3")
ax.set_xticks(x_pos)
ax.set_xticklabels(class_short, rotation=20, fontsize=10)
ax.set_ylabel(r"ratio $a_4^c / a_2^c$")
ax.set_yscale("log")
ax.set_title(f"(B) PRIMARY vs SCHEMATIC ratio per class")
ax.legend(loc="best", fontsize=9)
ax.grid(True, alpha=0.3)

ax = axes[2]
n_c_arr_TIER1 = np.array(n_c_TIER1) if n_c_TIER1 is not None else np.zeros(N_CLASSES)
n_c_arr_REF = np.array(N_C_REFERENCE)
ax.bar(x_pos - 0.2, n_c_arr_TIER1, width=0.4, label=f"TIER1 = {n_c_TIER1}", alpha=0.85, color="C0")
ax.bar(x_pos + 0.2, n_c_arr_REF, width=0.4, label=f"REF (W7-3 SCH) = {N_C_REFERENCE}",
       alpha=0.85, color="C3")
ax.set_xticks(x_pos)
ax.set_xticklabels(class_short, rotation=20, fontsize=10)
ax.set_ylabel(r"$n_c$ (integer multiplier)")
ax.set_title(f"(C) Integer signature  (n_c_match={n_c_match})")
ax.legend(loc="best", fontsize=9)
ax.grid(True, alpha=0.3)

fig.suptitle(
    f"S88 W13-159 W7-3 C-γ-WEAK PRIMARY Lift  --  composite={composite}  "
    f"--  {TIER_PIN}  --  Λ_global_TIER1 / M_KK = {Lambda_global_TIER1 / M_KK:.4e}",
    fontsize=12,
)
plt.tight_layout()
PNG_PATH = SCRIPT_DIR / "s88_w13_w7_3_c_gamma_weak_tier1_lift.png"                  # (local)
plt.savefig(PNG_PATH, dpi=120, bbox_inches="tight")
plt.close(fig)
print(f"PNG saved: {PNG_PATH}")
print()


# ---------------------------------------------------------------------------
# Section 13 — Append verdict line + dual-SHA companion
# ---------------------------------------------------------------------------
VERDICT_FILE = COMPUTATIONS_DIR / "session-88" / "s88_gate_verdicts.txt"             # (local)

verdict_value = R1_dispersion                                                        # (local) reported value
canonical_line = (                                                                   # (local)
    f"{GATE_ID}: {composite} -- "
    f"value={verdict_value:.6e} "
    f"scheme={SCHEME} "
    f"convention={CONVENTION} "
    f"L_max={L_MAX} "
    f"audit_sha256={audit_sha256} "
    f"content_sha256={content_sha256} "
    f"schema_version=S87+\n"
)
companion_dual_sha = (                                                               # (local)
    f"# audit_sha256_short={audit_sha256[:16]} "
    f"content_sha256_short={content_sha256[:16]} "
    f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
)

with open(VERDICT_FILE, "a", encoding="utf-8") as f:
    f.write(canonical_line)
    f.write(companion_dual_sha)

print(f"Verdict appended to: {VERDICT_FILE}")
print()
print(canonical_line.strip())
print(companion_dual_sha.strip())
print()


# ---------------------------------------------------------------------------
# Section 14 — 4-tuple OUTPUT
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
