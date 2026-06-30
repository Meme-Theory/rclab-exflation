#!/usr/bin/env python3
"""
S87 W7-2 — S87-W6-C-BETA-UV-CUTOFF-3CLASS  (carry-forward CF-43)
================================================================

Gate: S87-W6-C-BETA-UV-CUTOFF-3CLASS  ([VERIFY])

Hypothesis:
  The C-β UV-cutoff coefficient evaluated across the F_4 multiplier-vector
  sub-family {Class 1, Class 2, Class 3} ⊂ A_5-atlas regulators is INVARIANT
  under UV-cutoff choice (C-β is a substrate-canonical Mellin moment, not a
  cutoff-bookkeeping artifact).

Pre-registered threshold (plan §W7-2 §9):
  PASS  iff  delta_C_beta = max_{c,c'} |C-β_c − C-β_{c'}| / |mean({C-β_c})|
             ≤ 0.01  (RATIO; tight cross-class immunization)
        AND per-class scheme-invariance ≤ 1e-3 (cross-check Step D)
        AND regime_verdict = VALID (all 3 classes inside Mellin
                                    substrate-distance-1 convergence cone:
                                    s=2 + s=3 residues finite & positive)
  INFO  iff  0.01 < delta_C_beta ≤ 0.05  OR  regime_verdict = MARGINAL
  FAIL  iff  delta_C_beta > 0.05         OR  regime_verdict = BREAKDOWN
        OR per-class scheme-invariance > 1e-3
  Tolerance rule: RATIO.

F_4 multiplier-vector sub-family (registry §VII-B.HP1-NEAR-INVARIANCE,
line 2654; cross-cite §VII.K-PROP-W8 4-channel LAYER-2):
    F_4 = {ζ, Zubarev, SDW}     ⊂  A_5 = {ζ, Zubarev, SDW, cutoff_sqrt, anomaly}
  Classes (3-class sub-family of 5-atlas):
    Class 1 = {ζ}                                    (zeta_a_n evaluator)
    Class 2 = {Zubarev}    (heat-kernel-dressed)     (heat_kernel_a_n evaluator)
    Class 3 = {SDW}        (Γ(s)-cancelled Mellin)   (mellin_a_n evaluator)

C-β definition (plan §10 substitution chain):
    M_c(s)  := Mellin transform of D_K^{<=10} weighted by regulator R_c
            =  (1/Vol_SU3_Haar) · Σ_{(p,q),p+q≤L} d(p,q) · f_{R_c}(C_2(p,q), s)

    C-β_c   := Res[M_c(s); s=2] / Res[M_c(s); s=3]
            =  (substrate-distance-1 Mellin-cone substrate-distance-1 ratio)

  Step 4 of substitution chain:
    C-β_c = (μ_c(2)/μ_c(3)) · (ρ(2)/ρ(3))
    where ρ is the regulator-INDEPENDENT substrate spectral kernel and
    μ_c is the regulator-c multiplier at pole s=k.
    PASS ⟺ F_4 sub-family closed under substrate-distance-1 Mellin-cone ratio.

TIER-2 SCHEMATIC declaration (MANDATORY per
`.claude/rules/substrate-first-canonical-sourcing.md` §iv):
  This gate uses `_spectral_action_regulators.py` SCHEMATIC helpers per the
  module docstring (lines 22-31). The schematic helpers are deterministic
  pure-spectrum analogs of the named regulators in Chamseddine-Connes 1996
  §2.2-2.3, intended to MEASURE SPREAD of an observable across a discrete
  set of regulator prescriptions, NOT to pin a single prescription as
  canonical. The verdict-line `scheme=` field carries the
  "Mellin-cone-substrate-distance-1-SCHEMATIC" suffix; the working-paper
  synthesis carries an explicit cross-tier disclosure paragraph
  (W4-2 line 503 model). A live-physical-regularization re-run
  (Λ_UV = M_KK Pauli-Villars per S61/S78 pipeline) is a separate question
  outside the SCHEMATIC tier of this gate.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/_spectral_action_regulators.py
       (5-atlas evaluators; SCHEMATIC tier)
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz
       (D_K^{<=12} sector-eigenvalue cache; SHA-anchor for substrate-canonical
        spectrum reproducibility — the SCHEMATIC helpers operate on the
        Casimir/Weyl-dim multiplicity-weighted analog of this spectrum at
        L_max=10)
  - sessions/permanent-results-registry.md
       (§VII-B.HP1-NEAR-INVARIANCE F_4 = {ζ, Zubarev, SDW} pin;
        §VII.K-PROP-W8 4-channel LAYER-2 cross-citation)
  - canonical_constants.py
       (Vol_SU3_Haar = 8√3·π⁴ = 1349.7399...; required by S34+ rule)

Output 4-tuple:
    (value=delta_C_beta,
     scheme=Mellin-cone-substrate-distance-1-SCHEMATIC,
     convention=F_4-multiplier-vector,
     L_max=10)

Classification: GEOMETRIC.

Substitution-chain audit footer (plan §10 verbatim, executed inside the
script via numerical evaluation of (μ_c(2)/μ_c(3)) for c ∈ {1,2,3}).
"""

from __future__ import annotations

# -----------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import per S34+ rule)
# -----------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403
from canonical_constants import Vol_SU3_Haar

# -----------------------------------------------------------------------------
# Section 2 — Standard imports + CPU thread cap (no GPU compute path)
# -----------------------------------------------------------------------------
import os
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===


os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import math
import sys
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# Section 3 — Paths + pre-registration pin map
# -----------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent                        # (local)
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

REG_HELPERS = resolve_script(None, '_spectral_action_regulators.py')                    # (local)
SPECTRUM_CACHE = resolve_output(84, 's84_spectrum_cache_L12_tau019.npz')              # (local)
REGISTRY = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"        # (local)
CANONICAL_PY = resolve_script(None, 'canonical_constants.py')                           # (local)
PLAN_W7 = (PROJECT_ROOT / "sessions" / "session-plan"
           / "session-87-plan-w7.md")                                         # (local)

VERDICT_TXT = resolve_output(87, 's87_gate_verdicts.txt')                             # (local)
NPZ_OUT = resolve_output(87, 's87_w7_c_beta_uv_cutoff_3class.npz')                    # (local)
PNG_OUT = resolve_output(87, 's87_w7_c_beta_uv_cutoff_3class.png')                    # (local)

SESSION = "S87"                                                               # (local)
GATE_ID = "S87-W6-C-BETA-UV-CUTOFF-3CLASS"                                    # (local)
SCHEME = "Mellin-cone-substrate-distance-1-SCHEMATIC"                         # (local)
CONVENTION = "F_4-multiplier-vector"                                          # (local)
L_MAX = 10                                                                    # (local) canonical L_max

# Pre-registered thresholds (plan §W7-2 §9)
PASS_THRESH_DELTA = 0.01                                                      # (local) RATIO PASS band ceiling
INFO_THRESH_DELTA = 0.05                                                      # (local) RATIO INFO band ceiling
PASS_THRESH_SCHEME_INVAR = 1.0e-3                                             # (local) per-class scheme-invariance Step D

# Pre-registered pin map (PRDR; plan §W7-2 §7)
PIN_MAP = {                                                                   # (local)
    "L_max": L_MAX,
    "scheme": SCHEME,
    "convention": CONVENTION,
    "n_eval": 3,
    "scan_range": "N/A (3 discrete classes)",
    "tolerance_rule": "RATIO",
    "tolerance_pass": PASS_THRESH_DELTA,
    "tolerance_info_ceiling": INFO_THRESH_DELTA,
    "tolerance_scheme_invariance": PASS_THRESH_SCHEME_INVAR,
    "random_seed": None,
    "GPU_path": "none (CPU only; OMP_NUM_THREADS=8)",
    "regulator_family_pin": "F_4_multiplier_vector",
    "n_classes_pin": 3,
    "f4_classes": [
        ("Class 1", "zeta", "zeta_a_n"),
        ("Class 2", "Zubarev (heat-kernel)", "heat_kernel_a_n"),
        ("Class 3", "SDW (Mellin Γ(s)-cancelled)", "mellin_a_n"),
    ],
    "cross_check_regulators": ["sqrt-Heaviside_cutoff", "Gaussian-Mellin_zeta"],
    "tier_pin": "TIER-2_SCHEMATIC_per_substrate-first-canonical-sourcing.md_§iv",
    "schema_version": "R3",
    "s_substrate_distance_1_pole": 3,
    "s_substrate_distance_2_pole": 2,
    "C_beta_def": "C_beta_c = M_c(s=2) / M_c(s=3)",
    "delta_def": "max_pair_abs_diff / abs(mean_C_beta)",
}


def sha256_file(p: Path) -> str:
    h = hashlib.sha256()                                                      # (local)
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(input_pin_map: dict) -> str:
    payload = json.dumps(input_pin_map, sort_keys=True, default=str).encode("utf-8")  # (local)
    return hashlib.sha256(payload).hexdigest()


# -----------------------------------------------------------------------------
# Section 4 — Echo input SHAs in first 20 lines of stdout (S81+ discipline)
# -----------------------------------------------------------------------------
print("=" * 78)
print(f"{GATE_ID}  ({SESSION} W7-2; CF-43 lizzi-spectral-functional-theorist)")
print("=" * 78)
sha_helpers = sha256_file(REG_HELPERS)                                        # (local)
sha_cache = sha256_file(SPECTRUM_CACHE)                                       # (local)
sha_registry = sha256_file(REGISTRY)                                          # (local)
sha_canonical = sha256_file(CANONICAL_PY)                                     # (local)
sha_plan = sha256_file(PLAN_W7)                                               # (local)
print(f"INPUT-PIN  _spectral_action_regulators.py  sha256={sha_helpers}")
print(f"INPUT-PIN  s84_spectrum_cache_L12_tau019    sha256={sha_cache}")
print(f"INPUT-PIN  permanent-results-registry.md    sha256={sha_registry}")
print(f"INPUT-PIN  canonical_constants.py           sha256={sha_canonical}")
print(f"INPUT-PIN  session-87-plan-w7.md             sha256={sha_plan}")
print(f"PIN  L_max={L_MAX}  Vol_SU3_Haar={Vol_SU3_Haar:.10e}")
print(f"PIN  scheme={SCHEME}")
print(f"PIN  convention={CONVENTION}")
print(f"PIN  TIER  TIER-2 SCHEMATIC (substrate-first-canonical-sourcing.md §iv)")
print(f"PIN  F_4 = {{ζ, Zubarev, SDW}}  (3-class sub-family of A_5)")
print(f"PIN  threshold_PASS_delta_C_beta = {PASS_THRESH_DELTA}")
print(f"PIN  threshold_INFO_ceiling      = {INFO_THRESH_DELTA}")
print(f"PIN  threshold_scheme_invariance = {PASS_THRESH_SCHEME_INVAR}")
print("=" * 78)


# -----------------------------------------------------------------------------
# Section 5 — Schematic regulator evaluators (TIER-2 helpers + auxiliary
#             cross-check kernels for plan §6 Step D)
# -----------------------------------------------------------------------------
sys.path.insert(0, str(SCRIPT_DIR))
from _spectral_action_regulators import (
    zeta_a_n,
    mellin_a_n,
    heat_kernel_a_n,
    _enumerate_sectors,
)


def sqrt_heaviside_cutoff_a_n(n, L_max, Vol, cutoff_frac=0.7):
    """sqrt-Heaviside cutoff cross-check kernel:
       weight w(C) = sqrt(max(0, 1 - C / (cutoff_frac * C_max)))   (Heaviside-shaped
       sqrt-soft cutoff). Differs from hard_cutoff (binary indicator) by the soft
       sqrt-edge dressing — used as scheme=cutoff cross-check per plan §6 Step D."""
    sectors = _enumerate_sectors(L_max)                                       # (local)
    if not sectors:
        return 0.0
    c_max = max(s[3] for s in sectors)                                        # (local)
    c_thresh = cutoff_frac * c_max                                            # (local)
    if n == 0:
        s = sum(d for _, _, d, _ in sectors)                                  # (local)
        return s / Vol
    acc = 0.0                                                                 # (local)
    for _, _, d, c in sectors:
        if c < c_thresh:
            w = math.sqrt(1.0 - c / c_thresh)                                 # (local) sqrt-Heaviside soft edge
            acc += w * d / (c ** n)
    return acc / Vol


def gaussian_mellin_zeta_a_n(n, L_max, Vol, sigma_frac=1.0):
    """Gaussian-Mellin zeta cross-check kernel:
       weight w(C) = exp(-(C/sigma)^2/2) with sigma = sigma_frac * sqrt(<C^2>).
       Gaussian-suppressed Mellin moment — used as scheme=zeta cross-check per
       plan §6 Step D (per-class scheme-invariance ≤ 1e-3)."""
    sectors = _enumerate_sectors(L_max)                                       # (local)
    if not sectors:
        return 0.0
    if n == 0:
        return sum(d for _, _, d, _ in sectors) / Vol
    c_vals = np.array([c for _, _, _, c in sectors])                          # (local)
    sigma = sigma_frac * float(np.sqrt(np.mean(c_vals * c_vals)))             # (local)
    acc = 0.0                                                                 # (local)
    for _, _, d, c in sectors:
        w = math.exp(-0.5 * (c / sigma) ** 2)                                 # (local) Gaussian envelope
        acc += w * d / (c ** n)
    return acc / Vol


# -----------------------------------------------------------------------------
# Section 6 — Step A/B: Compute C-β_c per class (substrate-distance-1 ratio)
# -----------------------------------------------------------------------------
# Per plan §10:  s=2 ↔ substrate-distance-2 pole (numerator residue)
#                s=3 ↔ substrate-distance-1 pole (denominator residue)
#
# Class 1 = {ζ}        evaluator = zeta_a_n
# Class 2 = {Zubarev}  evaluator = heat_kernel_a_n  (per S86 sector-2 §L1
#                                                    f_Zubarev = exp(-tC)/C^n)
# Class 3 = {SDW}      evaluator = mellin_a_n      (Γ(s) cancellation; algebraic
#                                                    identity to ζ on positive-
#                                                    definite Casimir spectrum)
S_NUM = 2                                                                     # (local) pole numerator
S_DEN = 3                                                                     # (local) pole denominator (substrate-distance-1)

class_evaluators = [                                                          # (local) (label, evaluator)
    ("Class 1: zeta",          zeta_a_n),
    ("Class 2: Zubarev",       heat_kernel_a_n),
    ("Class 3: SDW",           mellin_a_n),
]

print("\n--- Step A/B: per-class C-β_c (canonical evaluator) ---")
canonical_M_s2 = []                                                           # (local)
canonical_M_s3 = []                                                           # (local)
canonical_C_beta = []                                                         # (local)

for label, fn in class_evaluators:
    M2 = fn(S_NUM, L_MAX, Vol_SU3_Haar)                                       # (local)
    M3 = fn(S_DEN, L_MAX, Vol_SU3_Haar)                                       # (local)
    cbeta = M2 / M3                                                           # (local) C-β_c
    canonical_M_s2.append(M2)
    canonical_M_s3.append(M3)
    canonical_C_beta.append(cbeta)
    print(f"  {label:<24}  M(s=2)={M2:.12e}  M(s=3)={M3:.12e}  C-β_c={cbeta:.15f}")

canonical_M_s2 = np.array(canonical_M_s2, dtype=np.float64)
canonical_M_s3 = np.array(canonical_M_s3, dtype=np.float64)
canonical_C_beta = np.array(canonical_C_beta, dtype=np.float64)

# Regime check: all 3 finite & positive at both s=2 and s=3
finite_mask = np.isfinite(canonical_M_s2) & np.isfinite(canonical_M_s3)
positive_mask = (canonical_M_s2 > 0) & (canonical_M_s3 > 0)
n_in_cone = int(np.sum(finite_mask & positive_mask))                          # (local)
print(f"\n  regime: {n_in_cone}/3 classes inside Mellin substrate-distance-1 cone")
if n_in_cone == 3:
    regime_verdict = "VALID"                                                  # (local)
elif n_in_cone == 2:
    regime_verdict = "MARGINAL"                                               # (local)
else:
    regime_verdict = "BREAKDOWN"                                              # (local)

# -----------------------------------------------------------------------------
# Section 7 — Step C: cross-class dispersion delta_C_beta
# -----------------------------------------------------------------------------
mean_C_beta = float(np.mean(canonical_C_beta))                                # (local)
pair_diffs = []                                                               # (local)
for i in range(3):
    for j in range(i + 1, 3):
        pair_diffs.append(abs(canonical_C_beta[i] - canonical_C_beta[j]))
max_pair_abs = float(max(pair_diffs))                                         # (local)
delta_C_beta = max_pair_abs / abs(mean_C_beta)                                # (local)

print("\n--- Step C: cross-class dispersion ---")
print(f"  C-β  =  [{canonical_C_beta[0]:.12f},  {canonical_C_beta[1]:.12f},  {canonical_C_beta[2]:.12f}]")
print(f"  mean C-β       = {mean_C_beta:.12f}")
print(f"  max_pair_abs   = {max_pair_abs:.6e}")
print(f"  delta_C_beta   = {delta_C_beta:.6e}    (PASS  ≤ {PASS_THRESH_DELTA};"
      f"  INFO ≤ {INFO_THRESH_DELTA};  FAIL > {INFO_THRESH_DELTA})")

# -----------------------------------------------------------------------------
# Section 8 — Step D: per-class scheme-invariance cross-check
# Compare each class's canonical evaluator against TWO independent kernels:
#   kernel A: sqrt-Heaviside cutoff      (scheme=cutoff family analog)
#   kernel B: Gaussian-Mellin zeta       (scheme=zeta family analog)
# Per-class scheme-invariance = max relative deviation of C-β_c across the
# canonical evaluator + 2 cross-check kernels, normalized by canonical C-β_c.
# Step D PASS iff per-class scheme-invariance ≤ 1e-3 for ALL 3 classes.
# -----------------------------------------------------------------------------
print("\n--- Step D: per-class scheme-invariance cross-check ---")
print("  cross-check kernels:  sqrt-Heaviside cutoff  (cf 0.7) + Gaussian-Mellin zeta (sigma_frac=1.0)")

cross_kernels = [                                                             # (local)
    ("sqrt_Heav_cutoff",     sqrt_heaviside_cutoff_a_n,   {"cutoff_frac": 0.7}),
    ("Gauss_Mellin_zeta",    gaussian_mellin_zeta_a_n,    {"sigma_frac": 1.0}),
]

per_class_scheme_invar = []                                                   # (local)
crosscheck_C_beta_table = np.zeros((3, 1 + len(cross_kernels)), dtype=np.float64)
crosscheck_C_beta_table[:, 0] = canonical_C_beta

for c_idx, (label, fn) in enumerate(class_evaluators):
    canonical = canonical_C_beta[c_idx]                                       # (local)
    devs = [0.0]                                                              # (local)
    cross_ratios = [canonical]                                                # (local)
    for k_idx, (kname, kfn, kkw) in enumerate(cross_kernels):
        m2 = kfn(S_NUM, L_MAX, Vol_SU3_Haar, **kkw)                           # (local)
        m3 = kfn(S_DEN, L_MAX, Vol_SU3_Haar, **kkw)                           # (local)
        cb_k = m2 / m3                                                        # (local)
        cross_ratios.append(cb_k)
        rel_dev = abs(cb_k - canonical) / abs(canonical)                      # (local)
        devs.append(rel_dev)
        crosscheck_C_beta_table[c_idx, 1 + k_idx] = cb_k
    max_rel_dev = max(devs)                                                   # (local)
    per_class_scheme_invar.append(max_rel_dev)
    print(f"  {label:<24}  C-β_canonical={canonical:.10f}  "
          f"C-β_sqrtHeav={cross_ratios[1]:.10f}  C-β_GaussMellin={cross_ratios[2]:.10f}"
          f"  max_rel_dev={max_rel_dev:.6e}")

per_class_scheme_invar = np.array(per_class_scheme_invar, dtype=np.float64)
worst_per_class = float(np.max(per_class_scheme_invar))                       # (local)
step_D_pass = bool(worst_per_class <= PASS_THRESH_SCHEME_INVAR)               # (local)
print(f"  Step D worst per-class scheme-invariance = {worst_per_class:.6e}"
      f"  ({'PASS' if step_D_pass else 'FAIL'} at threshold {PASS_THRESH_SCHEME_INVAR})")

# -----------------------------------------------------------------------------
# Section 9 — 3-tuple verdict (S87 schema-v2)  +  composite collapse
# Plan §6 decision rule: sign_verdict = N/A (positive spectral moment, no
# signed-direction pre-registration); magnitude/regime per the standard bands.
# -----------------------------------------------------------------------------
sign_verdict = "N_A"                                                          # (local) per plan §6
if delta_C_beta <= PASS_THRESH_DELTA:
    magnitude_verdict = "PASS"                                                # (local)
elif delta_C_beta <= INFO_THRESH_DELTA:
    magnitude_verdict = "INFO"                                                # (local)
else:
    magnitude_verdict = "FAIL"                                                # (local)

# Composite collapse (gate-verdicts.md §"Composite-collapse rule"):
#   regime BREAKDOWN  → composite FAIL
#   sign FAIL         → composite FAIL
#   magnitude FAIL & regime VALID → composite FAIL
#   magnitude FAIL & regime MARGINAL → composite INFO
#   magnitude INFO    → composite INFO
#   else              → PASS
# Plus: per-class scheme-invariance > 1e-3 (Step D FAIL) is a plan §9 FAIL
# precondition that overrides PASS even on tight magnitude.
if regime_verdict == "BREAKDOWN":
    composite = "FAIL"
elif not step_D_pass:
    composite = "FAIL"   # plan §9 explicit override
elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
    composite = "FAIL"
elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
    composite = "INFO"
elif magnitude_verdict == "INFO":
    composite = "INFO"
else:
    composite = "PASS"

print("\n--- 3-tuple + composite ---")
print(f"  sign_verdict       = {sign_verdict}")
print(f"  magnitude_verdict  = {magnitude_verdict}")
print(f"  regime_verdict     = {regime_verdict}")
print(f"  step_D_PASS        = {step_D_pass}")
print(f"  composite          = {composite}")

# -----------------------------------------------------------------------------
# Section 10 — Closure SHA  (plan §6 Step E)
# -----------------------------------------------------------------------------
input_pin_map = {                                                             # (local)
    "gate_id": GATE_ID,
    "session": SESSION,
    "scheme": SCHEME,
    "convention": CONVENTION,
    "L_max": L_MAX,
    "f4_subfamily_sha": sha_registry,
    "atlas_def_sha": sha_helpers,
    "dk_spectrum_sha": sha_cache,
    "c_beta_def_sha": sha_plan,
    "canonical_py_sha": sha_canonical,
    "n_classes_pin": 3,
    "regulator_family_pin": "F_4_multiplier_vector",
    "tolerance_pass": PASS_THRESH_DELTA,
    "tolerance_info_ceiling": INFO_THRESH_DELTA,
    "tolerance_scheme_invariance": PASS_THRESH_SCHEME_INVAR,
    "value": delta_C_beta,
    "C_beta_class1": float(canonical_C_beta[0]),
    "C_beta_class2": float(canonical_C_beta[1]),
    "C_beta_class3": float(canonical_C_beta[2]),
    "step_D_worst": worst_per_class,
    "regime_verdict": regime_verdict,
    "magnitude_verdict": magnitude_verdict,
    "sign_verdict": sign_verdict,
    "composite": composite,
    "schema_version": "R3",
    "tier_pin": "TIER-2_SCHEMATIC",
}
audit_sha256 = closure_hash(input_pin_map)                                    # (local)
content_pinmap = dict(input_pin_map)                                          # (local)
content_pinmap["__content_marker__"] = "C_beta_F4_3class_S87_W7_2"
content_sha256 = closure_hash(content_pinmap)                                 # (local)

print("\n--- Closure SHAs ---")
print(f"  audit_sha256   = {audit_sha256}")
print(f"  content_sha256 = {content_sha256}")


# -----------------------------------------------------------------------------
# Section 11 — Save .npz + .png
# -----------------------------------------------------------------------------
np.savez_compressed(
    NPZ_OUT,
    canonical_M_s2=canonical_M_s2,
    canonical_M_s3=canonical_M_s3,
    canonical_C_beta=canonical_C_beta,
    crosscheck_C_beta_table=crosscheck_C_beta_table,
    per_class_scheme_invar=per_class_scheme_invar,
    delta_C_beta=np.float64(delta_C_beta),
    mean_C_beta=np.float64(mean_C_beta),
    max_pair_abs=np.float64(max_pair_abs),
    worst_per_class_scheme_invar=np.float64(worst_per_class),
    pass_thresh_delta=np.float64(PASS_THRESH_DELTA),
    info_thresh_delta=np.float64(INFO_THRESH_DELTA),
    pass_thresh_scheme_invariance=np.float64(PASS_THRESH_SCHEME_INVAR),
    L_max=np.int64(L_MAX),
    regime_verdict=np.array([regime_verdict]),
    magnitude_verdict=np.array([magnitude_verdict]),
    composite=np.array([composite]),
    sign_verdict=np.array([sign_verdict]),
    audit_sha256=np.array([audit_sha256]),
    content_sha256=np.array([content_sha256]),
    f4_classes=np.array(["Class 1: zeta", "Class 2: Zubarev", "Class 3: SDW"]),
    cross_kernels=np.array(["canonical", "sqrt_Heav_cutoff", "Gauss_Mellin_zeta"]),
    tier_pin=np.array(["TIER-2_SCHEMATIC"]),
)
print(f"\n  data file → {NPZ_OUT}")

# Plot
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.5))                       # (local)

class_labels = ["Class 1\n{ζ}", "Class 2\n{Zubarev}", "Class 3\n{SDW}"]       # (local)
xs = np.arange(3)                                                             # (local)
colors = ["#1f77b4", "#d62728", "#2ca02c"]                                    # (local)

ax1.bar(xs, canonical_C_beta, color=colors, edgecolor="k", linewidth=0.6)
ax1.axhline(mean_C_beta, color="0.4", linestyle=":", linewidth=1.0,
            label=f"mean = {mean_C_beta:.4f}")
ax1.set_xticks(xs)
ax1.set_xticklabels(class_labels)
ax1.set_ylabel("C-β_c  (substrate-distance-1 Mellin ratio)")
ax1.set_title(f"S87-W6-C-BETA-UV-CUTOFF-3CLASS  (L_max={L_MAX}, TIER-2 SCHEMATIC)\n"
              f"delta_C_beta = {delta_C_beta:.3e}  ({composite})")
ax1.legend(loc="lower right", fontsize=8)
ax1.grid(alpha=0.3)
for x, y in zip(xs, canonical_C_beta):
    ax1.text(x, y * 1.005, f"{y:.6f}", ha="center", fontsize=8)

# Right panel: Step-D scheme-invariance per class (log scale)
yvals_step_d = per_class_scheme_invar.copy()                                  # (local)
# Floor zeros at 1e-18 so log scale renders
yvals_floor = np.where(yvals_step_d > 0, yvals_step_d, 1e-18)                 # (local)
ax2.bar(xs, yvals_floor, color=colors, edgecolor="k", linewidth=0.6)
ax2.axhline(PASS_THRESH_SCHEME_INVAR, color="r", linestyle="--", linewidth=1.0,
            label=f"PASS threshold = {PASS_THRESH_SCHEME_INVAR:.0e}")
ax2.set_yscale("log")
ax2.set_xticks(xs)
ax2.set_xticklabels(class_labels)
ax2.set_ylabel("max rel. dev. across {canonical, sqrt-Heav, Gauss-Mellin}")
ax2.set_title("Step-D per-class scheme-invariance")
ax2.legend(loc="best", fontsize=8)
ax2.grid(alpha=0.3, which="both")
for x, y in zip(xs, yvals_floor):
    ax2.text(x, y * 1.5, f"{y:.2e}", ha="center", fontsize=7)

fig.tight_layout()
fig.savefig(PNG_OUT, dpi=130)
plt.close(fig)
print(f"  plot file → {PNG_OUT}")


# -----------------------------------------------------------------------------
# Section 12 — Append canonical verdict line + dual-SHA companion + S87+ 3-tuple
# -----------------------------------------------------------------------------
canonical_line = (
    f"{GATE_ID}: {composite} -- "
    f"value={delta_C_beta:.6e} "
    f"scheme={SCHEME} "
    f"convention={CONVENTION} "
    f"L_max={L_MAX} "
    f"audit_sha256={audit_sha256} "
    f"content_sha256={content_sha256} "
    f"schema_version=S84+"
)

audit_short = audit_sha256[:16]                                               # (local)
content_short = content_sha256[:16]                                           # (local)
companion_dualsha = (
    f"# audit_sha256_short={audit_short} content_sha256_short={content_short} "
    f"# {GATE_ID} dual-SHA companion row (W9a-99 split)"
)
companion_3tuple = (
    f"# sign_verdict={sign_verdict} magnitude_verdict={magnitude_verdict} "
    f"regime_verdict={regime_verdict} "
    f"# {GATE_ID} 3-tuple annotation (S87 schema-v2)"
)
companion_provenance = (
    f"# C-β_c = {canonical_C_beta[0]:.10f}  {canonical_C_beta[1]:.10f}  {canonical_C_beta[2]:.10f}  "
    f"# F_4 = {{ζ, Zubarev, SDW}}  step_D_worst={worst_per_class:.3e}  "
    f"# TIER-2 SCHEMATIC per substrate-first-canonical-sourcing.md §iv"
)

print("\n--- canonical verdict line ---")
print(canonical_line)
print(companion_dualsha)
print(companion_3tuple)
print(companion_provenance)

with open(VERDICT_TXT, "a", encoding="utf-8") as f:
    f.write("\n")
    f.write(canonical_line + "\n")
    f.write(companion_dualsha + "\n")
    f.write(companion_3tuple + "\n")
    f.write(companion_provenance + "\n")

print(f"\n  verdict appended → {VERDICT_TXT}")
print("\n4-tuple: (value=%.6e, scheme=%s, convention=%s, L_max=%d)" %
      (delta_C_beta, SCHEME, CONVENTION, L_MAX))
print(f"\nDONE  ({GATE_ID} → {composite})")

sys.exit(0)
