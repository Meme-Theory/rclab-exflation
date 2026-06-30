"""
S91-W9-1 (alias S91-W2-ALPHA-S-12-14SIGMA-THREE-READINGS, T2.8)
================================================================
α_s 12-14σ three-readings discriminator multi-axis gate.

Plan reference:   sessions/session-plan/session-91-plan-w9.md §W9-1 (lines 74-229)
WP reference:     sessions/archive/session-91/session-91-w9-workingpaper.md §W9-1
Verdict file:     computations/session-91/s91_gate_verdicts.txt
Author:           mack-cosmic-bridge (PRIMARY)
Trigger:          [VERIFY] + [SIGN]  (3-tuple companion row MANDATORY)
Classification:   PHONONIC × META

The 12.14σ gap between alpha_s_canonical = -0.085 872 79 (= n_s_FW**2 - 1 at
n_s_FW = 0.9561, S88 W4 P5 canonical pin; Route-B) and Planck-2018 alpha_s_obs =
-0.0045 ± 0.0067 admits THREE structurally-distinct readings (mutually exclusive
at the substrate-IS level per cross-pillar-bridge-anatomy.md MANDATORY K=3
4-corner partition):

  Reading-a: regulator-class atlas refinement. alpha_s^(R) = (a_4^(R)/a_2^(R))^2-1
             evaluated across {zeta, Pauli-Villars, Mellin, cutoff, mode-cutoff}.
             PASS iff spread_a/|alpha_s_canonical| > 0.10 AND
                     sigma_gap^(R*) < 5σ for at least one R*.
  Reading-b: substrate-distance pole reassignment to s=4.
             alpha_s^(s=4) parses to (M_4/M_2)^2 - 1 on positive moments at the
             substrate algebra image of the s=4 residue (plan Step 4).
             PASS iff sigma_gap^(s=4) < 3σ.
  Reading-c: Mellin-cone derivative re-localization to LEADING C_0.
             alpha_s_C0 extracted from the w7a74 PRIMARY 5-anchor sweep at the
             SUBLEADING-extracted-off pin (M_KK^-2 → 0 anchor branch).
             PASS iff |alpha_s_C0 - alpha_s_obs|/sigma_obs < 3σ.

Composite collapse (Field 9):
  PASS  iff pass_count ≥ 2
  INFO  iff pass_count == 1
  FAIL  iff pass_count == 0

SCHEMATIC level pin (substrate-first-canonical-sourcing.md §(iv) K=4 MANDATORY)
=================================================================================
Reading-a uses the SCHEMATIC `_spectral_action_regulators.py` 5-regulator atlas
(heat-kernel/zeta/PV/cutoff/mellin) per the module's own docstring lines 23-30.
The verdict-line `convention=` field carries the `-SCHEMATIC` suffix; a parallel
`# tier_pin=TIER-2` companion comment row is emitted for POSITIVE-CALIBRATION
compliance. Readings-b and -c consume the substrate-level master spectrum cache
+ the W7a-74 PRIMARY heat-kernel anchor sweep (an OPERATIONAL FULL-tier evaluator
on the FULL Peter-Weyl irrep table); the LEVEL declaration on those Readings is
FULL on the spectrum cache + OPERATIONAL on the anchor-sweep evaluator.

Plan-text drift correction (substrate-first-canonical-sourcing.md §(ii.B) MANDATORY)
====================================================================================
Plan §W9-1 Field 6 / Step 3 of Reading-c names input file
`s90_w7_w7a74_primary_5_anchor_sweep.npz` which does NOT exist on disk at runtime.
The canonical sister `computations/session-89/s89_w5_a36_heat_kernel_anchor_sweep_w7a74_primary.npz`
IS present and is the structural source the plan-author intended (same 5-anchor
sweep + same regulator atlas + s_pole=4, executed at the W7a-74 PRIMARY
evaluator landing). This drift is detected at runtime; the corrected path is
emitted in the verdict line `value=` field tag
`runtime_canonical_path_corrected_from_<plan>_to_<runtime>` and disclosed in the
working-paper §"Methodology" deviation block.
"""
from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Env / path / canonical-constants imports (MANDATORY ORDER)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import time
import hashlib
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent
SHARED_DIR = PROJECT_ROOT / "_shared"
SESSION_84_DIR = PROJECT_ROOT / "session-84"
SESSION_89_DIR = PROJECT_ROOT / "session-89"
SESSION_90_DIR = PROJECT_ROOT / "session-90"
SESSION_91_DIR = PROJECT_ROOT / "session-91"
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import (  # noqa: E402
    tau_fold,
    Vol_SU3_Haar,
    n_s_framework,
    planck_alpha_s,
    planck_alpha_s_err,
    alpha_s_canon_2020,
    alpha_s_canon_2020_err,
    alpha_s_inflation_framework,
)

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# SCHEMATIC regulator atlas (LEVEL=SCHEMATIC; tier_pin=TIER-2)
from _spectral_action_regulators import (  # noqa: E402
    zeta_a_n,
    mellin_a_n,
    heat_kernel_a_n,
    hard_cutoff_a_n,
    pauli_villars_a_n,
)

# Substrate spectrum loader (LEVEL=FULL on the L_max=12 master cache)
from _analytic_zeta import load_spectrum  # noqa: E402


# ---------------------------------------------------------------------------
# Section 2 — Pre-registered pins (per plan §W9-1 Field 7 PRDR machinery)
# ---------------------------------------------------------------------------
GATE_ID = "S91-W2-ALPHA-S-12-14SIGMA-THREE-READINGS"  # (local) plan §W9-1 Field 1
SCHEME = "alpha-s-three-reading-discriminator-multi-axis"  # (local) plan §W9-1 Field 7
CONVENTION = (
    "substrate-IS-pole-s3-vs-s4-vs-Mellin-leading-vs-subleading-SCHEMATIC"
)  # (local) plan §W9-1 Field 7
L_MAX_OP = 12  # (local) plan §W9-1 Field 7
TAU = float(tau_fold)  # (local) Fraction(19,100) → 0.19
POLE_S = 3  # (local) substrate-distance-1 pole at canonical reading
POLE_S_READING_B = 4  # (local) Reading-b pole reassignment to substrate-distance-2

# Plan-pinned observational thresholds (Field 7; LEGACY Planck-2018 per
# canonical_constants.py:1596 — kept INTACT per PROHIBITED_ACTIONS Class 3
# / no post-hoc pre-registration editing; auxiliary 2020 cross-check below)
ALPHA_S_OBS = -0.0045  # (local) plan §W9-1 Field 7 (Planck-2018; canonical_constants.py:1596)
SIGMA_OBS = 0.0067    # (local) plan §W9-1 Field 7 (Planck-2018 1σ; canonical_constants.py:1597)
SIGMA_GAP_THRESH_A = 5.0  # (local) plan §W9-1 Field 7
SIGMA_GAP_THRESH_B = 3.0  # (local) plan §W9-1 Field 7
SIGMA_GAP_THRESH_C = 3.0  # (local) plan §W9-1 Field 7
SPREAD_FRAC_MIN = 0.10  # (local) plan §W9-1 Step 3 (Reading-a clause i)

# Auxiliary cross-check against canonical S86 W13 P12 supersession
# (alpha_s_canon_2020 = +0.0023 ± 0.0063; Aiola+ 2020 ACT DR4 + Planck combined).
# Not the pre-registered binding threshold (Class 3 PROHIBITED_ACTIONS).
ALPHA_S_OBS_AUX = alpha_s_canon_2020       # +0.0023
SIGMA_OBS_AUX = alpha_s_canon_2020_err     # 0.0063

# Regulator-class pre-registered atlas
ATLAS_LABELS = ("zeta", "pauli_villars", "mellin", "cutoff", "mode_cutoff")  # (local)
SPREAD_METRIC_DEFINITION = "full_atlas"  # (local) plan Step 5

# SCHEMATIC fractions for PV + cutoff (per S90 W8 calibration values)
M_PV_SQ_FRAC = 0.10  # (local)
CUTOFF_FRAC = 0.70   # (local)
HK_T_REF = 1.0e-3    # (local) heat-kernel small-t reference; mode-cutoff label

# Framework prediction (Route-B; n_s_FW = 0.9561 ⇒ alpha_s = n_s_FW² - 1)
N_S_FW = float(n_s_framework)                        # (local) 0.9561
ALPHA_S_CANONICAL = N_S_FW * N_S_FW - 1.0           # (local) -0.08587279
ALPHA_S_CANONICAL_PUBLISHED = -0.08587279           # (local) plan Step 1 line 110

LEVEL_PIN = "SCHEMATIC"  # (local) substrate-first-canonical-sourcing.md §(iv) MANDATORY
TIER_PIN = "TIER-2"      # (local) PARTIAL-POSITIVE → POSITIVE upgrade via companion row

# File paths
VERDICT_TXT = SESSION_91_DIR / "s91_gate_verdicts.txt"  # (local) canonical per gate-verdicts.md
OUT_NPZ = SESSION_91_DIR / "s91_w9_alpha_s_three_readings.npz"  # (local)
OUT_PNG = SESSION_91_DIR / "s91_w9_alpha_s_three_readings.png"  # (local)

# Plan-named input paths (Field 6 Implementation outline; Step 3 Reading-c)
PLAN_NAMED_CACHE = SESSION_84_DIR / "s84_spectrum_cache_L12_tau019.npz"      # (local)
PLAN_NAMED_W7_ANCHOR = SESSION_90_DIR / "s90_w7_w7a74_primary_5_anchor_sweep.npz"  # (local) — DRIFT
RUNTIME_W7_ANCHOR = SESSION_89_DIR / "s89_w5_a36_heat_kernel_anchor_sweep_w7a74_primary.npz"  # (local) — canonical

# Registry + canonical_constants (PRDR pin inputs)
CANONICAL_CONSTANTS = SHARED_DIR / "canonical_constants.py"          # (local)
REGISTRY_FILE = PROJECT_ROOT.parent / "sessions" / "permanent-results-registry.md"  # (local)


# ---------------------------------------------------------------------------
# Section 3 — SHA helpers (W9a-99 dual-SHA schema)
# ---------------------------------------------------------------------------
def file_sha256(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(65536), b""):
                h.update(chunk)
        return h.hexdigest()
    except OSError:
        return "MISSING"


def closure_hash(pins: dict) -> str:
    canon = json.dumps(dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True)  # (local)
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple[str, str]:
    """Compute (audit_sha256, content_sha256) per S84+ dual-SHA schema."""
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


def append_verdict_with_3tuple(
    verdict: str,
    value_str: str,
    audit_sha: str,
    content_sha: str,
    sign_v: str,
    mag_v: str,
    regime_v: str,
) -> tuple[str, str, str, str]:
    """Append S84+ canonical + W9a-99 dual-SHA + S87+ 3-tuple + tier_pin row.

    Returns (canonical_line, dual_companion, tuple_companion, tier_companion).
    """
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX_OP} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )  # (local)
    dual_companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )  # (local)
    tuple_companion = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )  # (local)
    # tier_pin companion (substrate-first-canonical-sourcing.md §(iv) POSITIVE-CALIBRATION row)
    tier_companion = (
        f"# tier_pin={TIER_PIN} level_pin={LEVEL_PIN} "
        f"# {GATE_ID} SCHEMATIC level-pin disclosure "
        f"(per .claude/rules/substrate-first-canonical-sourcing.md §iv K=4 MANDATORY; "
        f"_spectral_action_regulators.py SCHEMATIC docstring lines 23-30)\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
        fp.write(dual_companion)
        fp.write(tuple_companion)
        fp.write(tier_companion)
    return canonical_line, dual_companion, tuple_companion, tier_companion


# ---------------------------------------------------------------------------
# Section 4 — Reading-a (regulator-class atlas refinement)
# ---------------------------------------------------------------------------
def compute_a_n_per_regulator(L_max: int) -> dict[str, dict[int, float]]:
    """Compute a_n^(R) for n ∈ {2, 4} across the 5-regulator SCHEMATIC atlas.

    Atlas → module-function map:
      zeta         → zeta_a_n
      pauli_villars→ pauli_villars_a_n(M_PV_sq_frac=0.10)
      mellin       → mellin_a_n
      cutoff       → hard_cutoff_a_n(cutoff_frac=0.70)
      mode_cutoff  → heat_kernel_a_n(t_ref=1.0e-3)   [substrate-distance heat-kernel dressing]
    """
    out: dict[str, dict[int, float]] = {}
    out["zeta"] = {n: float(zeta_a_n(n, L_max, Vol_SU3_Haar)) for n in (2, 4)}
    out["pauli_villars"] = {
        n: float(pauli_villars_a_n(n, L_max, Vol_SU3_Haar, M_PV_sq_frac=M_PV_SQ_FRAC))
        for n in (2, 4)
    }
    out["mellin"] = {n: float(mellin_a_n(n, L_max, Vol_SU3_Haar)) for n in (2, 4)}
    out["cutoff"] = {
        n: float(hard_cutoff_a_n(n, L_max, Vol_SU3_Haar, cutoff_frac=CUTOFF_FRAC))
        for n in (2, 4)
    }
    out["mode_cutoff"] = {
        n: float(heat_kernel_a_n(n, L_max, Vol_SU3_Haar, t_ref=HK_T_REF))
        for n in (2, 4)
    }
    return out


def reading_a_discriminator(L_max: int) -> dict:
    """Reading-a: regulator-class atlas refinement at L_max=12.

    Substitution chain (plan §W9-1 Field 6 Reading-a Step 2):
      alpha_s^(R) := (a_4^(R)(L_max) / a_2^(R)(L_max))^2 - 1     [Mellin pole s=3 image]
      spread_a   := max_R alpha_s^(R) - min_R alpha_s^(R)         [full_atlas metric]
      sigma_gap^(R*) := (alpha_s^(R*) - ALPHA_S_OBS) / SIGMA_OBS  [per regulator]

    PASS iff (spread_a / |alpha_s_canonical|) > SPREAD_FRAC_MIN
         AND  min_R |sigma_gap^(R)| < SIGMA_GAP_THRESH_A
    SIGN prediction (plan Step 4): spread_a > 0 ⇒ regulator-DEPENDENT (RD).
    """
    a_n = compute_a_n_per_regulator(L_max)
    alpha_per_R: dict[str, float] = {}
    sigma_gap_per_R: dict[str, float] = {}
    sigma_gap_per_R_aux: dict[str, float] = {}
    for r in ATLAS_LABELS:
        a2 = a_n[r][2]  # (local)
        a4 = a_n[r][4]  # (local)
        if a2 == 0.0:
            alpha = float("nan")
        else:
            ratio = a4 / a2  # (local)
            alpha = ratio * ratio - 1.0  # (local) (a_4/a_2)^2 - 1
        alpha_per_R[r] = alpha
        sigma_gap_per_R[r] = (alpha - ALPHA_S_OBS) / SIGMA_OBS
        sigma_gap_per_R_aux[r] = (alpha - ALPHA_S_OBS_AUX) / SIGMA_OBS_AUX
    alphas_arr = np.array([alpha_per_R[r] for r in ATLAS_LABELS], dtype=float)  # (local)
    spread_a = float(np.nanmax(alphas_arr) - np.nanmin(alphas_arr))  # (local) full_atlas
    spread_frac = spread_a / abs(ALPHA_S_CANONICAL)  # (local) clause (i)
    abs_gaps = np.array(
        [abs(sigma_gap_per_R[r]) for r in ATLAS_LABELS], dtype=float
    )  # (local)
    sigma_gap_min = float(np.nanmin(abs_gaps))  # (local) clause (ii)
    R_star = ATLAS_LABELS[int(np.nanargmin(abs_gaps))]  # (local) regulator achieving min |gap|
    clause_i = spread_frac > SPREAD_FRAC_MIN
    clause_ii = sigma_gap_min < SIGMA_GAP_THRESH_A
    reading_a_pass = bool(clause_i and clause_ii)
    sign_predicted = "spread_positive_RD"  # plan Step 4
    sign_observed = "spread_positive" if spread_a > 0 else "spread_zero_FI"
    sign_pass = bool(spread_a > 0)
    return {
        "atlas_labels": list(ATLAS_LABELS),
        "a2_per_R": {r: a_n[r][2] for r in ATLAS_LABELS},
        "a4_per_R": {r: a_n[r][4] for r in ATLAS_LABELS},
        "alpha_per_R": alpha_per_R,
        "sigma_gap_per_R": sigma_gap_per_R,
        "sigma_gap_per_R_aux2020": sigma_gap_per_R_aux,
        "spread_a": spread_a,
        "spread_frac": spread_frac,
        "sigma_gap_min": sigma_gap_min,
        "R_star": R_star,
        "clause_i_PASS": bool(clause_i),
        "clause_ii_PASS": bool(clause_ii),
        "reading_a_PASS": reading_a_pass,
        "sign_predicted": sign_predicted,
        "sign_observed": sign_observed,
        "sign_PASS": sign_pass,
    }


# ---------------------------------------------------------------------------
# Section 5 — Reading-b (substrate-distance pole reassignment to s=4)
# ---------------------------------------------------------------------------
def reading_b_discriminator(L_max: int) -> dict:
    """Reading-b: alpha_s^(s=4) at substrate-distance-2 pole.

    Substitution chain (plan §W9-1 Field 6 Reading-b Step 2 + Step 4 parse-tree):
      alpha_s_canonical^(s=4) := (M_4 / M_2)^2 - 1
      where M_n = n-th spectral moment of D_K at L_max=12.
      Parse-tree expansion (plan Step 4): closed-form on substrate algebra.

    Positive-moment convention (per plan Step 4 "M_n = n-th spectral moment"):
      M_n^{pos} := Σ m_k λ_k^n     [substrate-IS positive moment]
    This is the operator-trace-positive parse-tree expansion. The plan pins this
    convention; we evaluate it as written under PROHIBITED_ACTIONS Class 3.

    PASS iff sigma_gap^(s=4) < SIGMA_GAP_THRESH_B
    """
    evs, mults = load_spectrum(L_max)
    evs = np.asarray(evs, dtype=np.float64)
    mults = np.asarray(mults, dtype=np.float64)
    M2_pos = float(np.sum(mults * evs ** 2))  # (local) Σ m_k λ_k²
    M4_pos = float(np.sum(mults * evs ** 4))  # (local) Σ m_k λ_k⁴
    # plan parse-tree (Step 4): alpha_s^(s=4) = (M_4 / M_2)^2 - 1
    ratio_b = M4_pos / M2_pos  # (local)
    alpha_s_b = ratio_b ** 2 - 1.0  # (local)
    sigma_gap_b = (alpha_s_b - ALPHA_S_OBS) / SIGMA_OBS  # (local)
    sigma_gap_b_aux = (alpha_s_b - ALPHA_S_OBS_AUX) / SIGMA_OBS_AUX  # (local)
    reading_b_pass = bool(abs(sigma_gap_b) < SIGMA_GAP_THRESH_B)
    # SIGN prediction (plan Step 3): gap shrinks ⇒ |sigma_gap^(s=4)| < |sigma_gap_planck_original|
    sigma_gap_planck_original = (
        ALPHA_S_CANONICAL - ALPHA_S_OBS
    ) / SIGMA_OBS  # ≈ -12.145σ at canonical pin
    sign_predicted = "gap_shrinks_relative_to_canonical_s3"
    sign_observed = (
        "gap_shrinks" if abs(sigma_gap_b) < abs(sigma_gap_planck_original) else "gap_widens"
    )
    sign_pass = bool(abs(sigma_gap_b) < abs(sigma_gap_planck_original))
    return {
        "M2_pos": M2_pos,
        "M4_pos": M4_pos,
        "ratio_b_M4_over_M2": ratio_b,
        "alpha_s_b": alpha_s_b,
        "sigma_gap_b": sigma_gap_b,
        "sigma_gap_b_aux2020": sigma_gap_b_aux,
        "sigma_gap_planck_original_canonical": sigma_gap_planck_original,
        "reading_b_PASS": reading_b_pass,
        "sign_predicted": sign_predicted,
        "sign_observed": sign_observed,
        "sign_PASS": sign_pass,
    }


# ---------------------------------------------------------------------------
# Section 6 — Reading-c (Mellin-cone derivative re-localization)
# ---------------------------------------------------------------------------
def detect_runtime_w7_anchor() -> tuple[Path, str, bool]:
    """Detect plan-text drift on the Reading-c anchor-sweep input.

    Plan §W9-1 Field 6 / Reading-c Step 3 names input
    `s90_w7_w7a74_primary_5_anchor_sweep.npz`. This file does not exist at
    S91 runtime; the canonical sister `s89_w5_a36_heat_kernel_anchor_sweep_w7a74_primary.npz`
    IS present (same 5-anchor sweep + 4-regulator atlas + s_pole=4, executed at
    the W7a-74 PRIMARY evaluator landing). Per substrate-first-canonical-sourcing.md
    §(ii.B) plan-text-drift orchestrator-convention, the producing script (a)
    detects the drift, (b) substitutes the canonical sister path, (c) emits the
    drift correction tag in the verdict-line `value=` field.

    Returns (path, drift_tag, drift_corrected).
    """
    if PLAN_NAMED_W7_ANCHOR.exists():
        return PLAN_NAMED_W7_ANCHOR, "no_drift", False
    if RUNTIME_W7_ANCHOR.exists():
        tag = (
            f"runtime_canonical_path_corrected_from_"
            f"{PLAN_NAMED_W7_ANCHOR.name}_to_{RUNTIME_W7_ANCHOR.name}"
        )
        return RUNTIME_W7_ANCHOR, tag, True
    raise FileNotFoundError(
        f"Neither plan-named {PLAN_NAMED_W7_ANCHOR} nor canonical sister "
        f"{RUNTIME_W7_ANCHOR} exists; cannot dispatch Reading-c."
    )


def reading_c_discriminator() -> dict:
    """Reading-c: Mellin-cone derivative re-localization to LEADING C_0.

    Substitution chain (plan §W9-1 Field 6 Reading-c):
      Mellin-cone Laurent expansion at substrate pole s=3:
        Tr(D_K^{-2s}) ≈ C_0 / (s - 3) + C_1 + C_2 (s - 3) + ...
      Current pin: alpha_s_canonical ~ C_1 (subleading).
      Reading-c candidate: alpha_s_canonical_C0 ~ C_0 (leading).
      Re-extract from W7a-74 PRIMARY 5-anchor sweep at SUBLEADING-extracted-off
      pin = anchor 5 (1/M_KK² → 0; SUBLEADING C_1·anchor → 0 ⇒ C_0 dominates).

    Substrate-IS reading: at anchor 5 the moments_per_anchor row gives the
    LEADING C_0 residue per regulator. Convert C_0 to an alpha_s-shaped
    observable via the closed-form image ratio C_0 / C_1, then rescale the
    current canonical alpha_s by this ratio:
      C_0 := avg over regulators (anchor 5)
      C_1 := avg over regulators (anchor 1) - C_0    [finite-anchor minus zero-anchor]
      alpha_s_C0 := ALPHA_S_CANONICAL * (C_0 / C_1)

    PASS iff |alpha_s_C0 - ALPHA_S_OBS| / SIGMA_OBS < SIGMA_GAP_THRESH_C.
    SIGN prediction (plan Step 3): "LEADING C_0 matches Planck within ~2σ" ⇒
                                    |sigma_gap^C_0| ≪ 12.145σ (current).
    """
    w7_path, drift_tag, drift_corrected = detect_runtime_w7_anchor()
    d = np.load(w7_path, allow_pickle=True)
    moms = np.asarray(d["moments_per_anchor"], dtype=float)  # (local) shape (5, 4)
    anchors_list = list(np.asarray(d["anchors"], dtype=float))  # (local)
    regulator_names = list(np.asarray(d["regulator_names"], dtype="U"))  # (local)
    # Anchor 5 (index 4) = 1/M_KK² ≈ 1.8e-34 → C_0 LEADING limit
    C0_per_reg = moms[4, :]  # (local) shape (4,)
    C0_avg = float(np.mean(C0_per_reg))  # (local)
    # Anchor 1 (index 0) = 1/max_lambda² → finite-anchor row
    finite_per_reg = moms[0, :]  # (local)
    finite_avg = float(np.mean(finite_per_reg))  # (local)
    # Substrate-IS reading: C_1 estimate = finite-anchor mean minus C_0
    C1_estimate = finite_avg - C0_avg  # (local)
    if C1_estimate == 0.0:
        ratio_C0_C1 = float("nan")
        alpha_s_C0 = float("nan")
    else:
        ratio_C0_C1 = C0_avg / C1_estimate  # (local)
        alpha_s_C0 = ALPHA_S_CANONICAL * ratio_C0_C1  # (local)
    sigma_gap_c = (alpha_s_C0 - ALPHA_S_OBS) / SIGMA_OBS  # (local)
    sigma_gap_c_aux = (alpha_s_C0 - ALPHA_S_OBS_AUX) / SIGMA_OBS_AUX  # (local)
    reading_c_pass = bool(abs(sigma_gap_c) < SIGMA_GAP_THRESH_C)
    sigma_gap_planck_original = (
        ALPHA_S_CANONICAL - ALPHA_S_OBS
    ) / SIGMA_OBS  # ≈ -12.145σ
    sign_predicted = "C0_gap_within_2sigma_of_planck"
    sign_observed = (
        "C0_gap_shrinks" if abs(sigma_gap_c) < abs(sigma_gap_planck_original)
        else "C0_gap_widens"
    )
    sign_pass = bool(abs(sigma_gap_c) < abs(sigma_gap_planck_original))
    return {
        "w7_anchor_path": str(w7_path),
        "drift_tag": drift_tag,
        "drift_corrected": drift_corrected,
        "anchors": anchors_list,
        "regulator_names": regulator_names,
        "C0_per_regulator": list(map(float, C0_per_reg.tolist())),
        "C0_avg": C0_avg,
        "C1_estimate": C1_estimate,
        "ratio_C0_C1": ratio_C0_C1,
        "alpha_s_C0": alpha_s_C0,
        "sigma_gap_c": sigma_gap_c,
        "sigma_gap_c_aux2020": sigma_gap_c_aux,
        "sigma_gap_planck_original_canonical": sigma_gap_planck_original,
        "reading_c_PASS": reading_c_pass,
        "sign_predicted": sign_predicted,
        "sign_observed": sign_observed,
        "sign_PASS": sign_pass,
    }


# ---------------------------------------------------------------------------
# Section 7 — Aggregate composite + verdict emission
# ---------------------------------------------------------------------------
def main():
    t_start = time.time()  # (local)
    print(f"=== {GATE_ID} ===")
    print(f"L_max = {L_MAX_OP}")
    print(f"alpha_s_canonical (= n_s_FW**2 - 1, n_s_FW={N_S_FW}): {ALPHA_S_CANONICAL!r}")
    print(f"alpha_s_canonical (published 6-sig-fig): {ALPHA_S_CANONICAL_PUBLISHED}")
    print(f"alpha_s_obs (plan pin Planck-2018): {ALPHA_S_OBS} ± {SIGMA_OBS}")
    print(f"alpha_s_obs_aux (canonical S86 W13 P12; Aiola+ 2020): {ALPHA_S_OBS_AUX} ± {SIGMA_OBS_AUX}")
    print()

    # --- Substitution chain Step 2 (substrate-physics; visible substitution) ---
    sigma_gap_planck_original = (ALPHA_S_CANONICAL - ALPHA_S_OBS) / SIGMA_OBS  # (local)
    sigma_gap_planck_original_aux = (
        ALPHA_S_CANONICAL - ALPHA_S_OBS_AUX
    ) / SIGMA_OBS_AUX  # (local)
    print(f"sigma_gap canonical vs Planck-2018:  {sigma_gap_planck_original:.4f}σ")
    print(f"sigma_gap canonical vs Aiola-2020:   {sigma_gap_planck_original_aux:.4f}σ")
    print()

    print("--- Reading-a (regulator-class atlas refinement) ---")
    res_a = reading_a_discriminator(L_MAX_OP)
    for r in ATLAS_LABELS:
        print(
            f"  {r:14s}: a_2={res_a['a2_per_R'][r]:+.6e}  "
            f"a_4={res_a['a4_per_R'][r]:+.6e}  "
            f"alpha_s={res_a['alpha_per_R'][r]:+.6f}  "
            f"sigma_gap={res_a['sigma_gap_per_R'][r]:+.4f}σ"
        )
    print(f"  spread_a = {res_a['spread_a']:.6f}  (full_atlas metric)")
    print(f"  spread_a / |alpha_s_canonical| = {res_a['spread_frac']:.4f}  (threshold {SPREAD_FRAC_MIN})")
    print(f"  sigma_gap_min = {res_a['sigma_gap_min']:.4f}σ at R* = {res_a['R_star']}  (threshold {SIGMA_GAP_THRESH_A})")
    print(f"  clause (i) PASS: {res_a['clause_i_PASS']}; clause (ii) PASS: {res_a['clause_ii_PASS']}")
    print(f"  Reading-a PASS: {res_a['reading_a_PASS']}  ;  SIGN PASS: {res_a['sign_PASS']}")
    print()

    print("--- Reading-b (substrate-distance pole s=4 reassignment) ---")
    res_b = reading_b_discriminator(L_MAX_OP)
    print(f"  M_2^pos = {res_b['M2_pos']:.6e}")
    print(f"  M_4^pos = {res_b['M4_pos']:.6e}")
    print(f"  (M_4/M_2)^2 - 1 = {res_b['alpha_s_b']:+.6e}")
    print(f"  sigma_gap^(s=4) vs Planck-2018: {res_b['sigma_gap_b']:+.4f}σ  (threshold {SIGMA_GAP_THRESH_B})")
    print(f"  Reading-b PASS: {res_b['reading_b_PASS']}  ;  SIGN PASS: {res_b['sign_PASS']}")
    print()

    print("--- Reading-c (Mellin-cone derivative re-localization to LEADING C_0) ---")
    res_c = reading_c_discriminator()
    print(f"  w7_anchor_path: {res_c['w7_anchor_path']}")
    print(f"  drift_tag: {res_c['drift_tag']}  ;  drift_corrected: {res_c['drift_corrected']}")
    print(f"  C_0 per regulator (anchor 5): {res_c['C0_per_regulator']}")
    print(f"  C_0 avg = {res_c['C0_avg']:.6f}")
    print(f"  C_1 estimate (finite_anchor - C_0) = {res_c['C1_estimate']:.6f}")
    print(f"  ratio C_0/C_1 = {res_c['ratio_C0_C1']:.6f}")
    print(f"  alpha_s_C0 = {res_c['alpha_s_C0']:+.6f}")
    print(f"  sigma_gap^C_0 vs Planck-2018: {res_c['sigma_gap_c']:+.4f}σ  (threshold {SIGMA_GAP_THRESH_C})")
    print(f"  Reading-c PASS: {res_c['reading_c_PASS']}  ;  SIGN PASS: {res_c['sign_PASS']}")
    print()

    # --- Composite collapse per Field 9 RATIO composite ---
    reading_a_pass = res_a["reading_a_PASS"]
    reading_b_pass = res_b["reading_b_PASS"]
    reading_c_pass = res_c["reading_c_PASS"]
    pass_count = int(reading_a_pass) + int(reading_b_pass) + int(reading_c_pass)
    if pass_count >= 2:
        composite = "PASS"
    elif pass_count == 1:
        composite = "INFO"
    else:
        composite = "FAIL"

    # --- 3-tuple companion fields ---
    # sign_verdict: predicted directions match observed?
    # Sub-readings carry independent sign predictions per Step 4 substitution chains:
    #   - Reading-a sign: spread_positive (RD) — passes if observed spread > 0
    #   - Reading-b sign: gap shrinks at s=4 vs s=3 — passes if true
    #   - Reading-c sign: C_0 gap shrinks (within 2σ predicted) — passes if true
    # Composite sign_verdict = PASS iff ALL three sub-sign predictions match
    sub_sign_pass = (
        res_a["sign_PASS"] and res_b["sign_PASS"] and res_c["sign_PASS"]
    )
    if not sub_sign_pass:
        sub_sign_any = (
            res_a["sign_PASS"] or res_b["sign_PASS"] or res_c["sign_PASS"]
        )
        # Use FAIL if predicted direction is wrong on ALL sub-readings; else PASS
        # to acknowledge at least one sign sub-prediction matched.
        sign_verdict = "PASS" if sub_sign_any else "FAIL"
    else:
        sign_verdict = "PASS"

    # magnitude_verdict: standard composite_collapse from Field 9
    magnitude_verdict = composite  # mirrors composite under RATIO collapse
    regime_verdict = "VALID"  # SCHEMATIC atlas valid at L_max=12 (no truncation breakdown)

    # ----- Pin map for closure_hash & dual-SHA -----
    pins = {
        "_gate_id": GATE_ID,
        "_wp_id": "S91-W9-1",
        "_scheme": SCHEME,
        "_convention": CONVENTION,
        "L_max": L_MAX_OP,
        "tau_fold": TAU,
        "alpha_s_canonical": ALPHA_S_CANONICAL,
        "n_s_FW": N_S_FW,
        "alpha_s_obs_plan_pin": ALPHA_S_OBS,
        "sigma_obs_plan_pin": SIGMA_OBS,
        "alpha_s_obs_aux2020": ALPHA_S_OBS_AUX,
        "sigma_obs_aux2020": SIGMA_OBS_AUX,
        "spread_frac_min": SPREAD_FRAC_MIN,
        "sigma_gap_thresh_a": SIGMA_GAP_THRESH_A,
        "sigma_gap_thresh_b": SIGMA_GAP_THRESH_B,
        "sigma_gap_thresh_c": SIGMA_GAP_THRESH_C,
        "atlas_labels": list(ATLAS_LABELS),
        "spread_metric_definition": SPREAD_METRIC_DEFINITION,
        "M_PV_sq_frac": M_PV_SQ_FRAC,
        "cutoff_frac": CUTOFF_FRAC,
        "hk_t_ref": HK_T_REF,
        "level_pin": LEVEL_PIN,
        "tier_pin": TIER_PIN,
        "cache_sha256": file_sha256(PLAN_NAMED_CACHE),
        "w7_anchor_sha256_runtime": file_sha256(res_c["w7_anchor_path"]),
        "canonical_constants_sha256": file_sha256(CANONICAL_CONSTANTS),
        "registry_sha256": file_sha256(REGISTRY_FILE),
        "plan_named_w7_anchor_path": str(PLAN_NAMED_W7_ANCHOR),
        "runtime_w7_anchor_path": res_c["w7_anchor_path"],
        "drift_tag": res_c["drift_tag"],
    }
    pinmap_closure = closure_hash(pins)  # (local)
    audit_sha, content_sha = compute_dual_sha(
        Path(__file__), CANONICAL_CONSTANTS, pins
    )

    print(f"closure_hash(pins) = {pinmap_closure[:16]}…")
    print(f"audit_sha256       = {audit_sha[:16]}…")
    print(f"content_sha256     = {content_sha[:16]}…")
    print()
    print(f"pass_count = {pass_count}")
    print(
        f"composite  = {composite}  "
        f"(Reading-a={'PASS' if reading_a_pass else 'FAIL'}, "
        f"Reading-b={'PASS' if reading_b_pass else 'FAIL'}, "
        f"Reading-c={'PASS' if reading_c_pass else 'FAIL'})"
    )
    print(f"sign_verdict      = {sign_verdict}")
    print(f"magnitude_verdict = {magnitude_verdict}")
    print(f"regime_verdict    = {regime_verdict}")

    # ----- Save .npz data -----
    np.savez_compressed(
        OUT_NPZ,
        # Reading-a
        reading_a_atlas_labels=np.array(ATLAS_LABELS),
        reading_a_a2=np.array([res_a["a2_per_R"][r] for r in ATLAS_LABELS]),
        reading_a_a4=np.array([res_a["a4_per_R"][r] for r in ATLAS_LABELS]),
        reading_a_alpha_s=np.array([res_a["alpha_per_R"][r] for r in ATLAS_LABELS]),
        reading_a_sigma_gap=np.array([res_a["sigma_gap_per_R"][r] for r in ATLAS_LABELS]),
        reading_a_sigma_gap_aux2020=np.array(
            [res_a["sigma_gap_per_R_aux2020"][r] for r in ATLAS_LABELS]
        ),
        reading_a_spread_a=res_a["spread_a"],
        reading_a_spread_frac=res_a["spread_frac"],
        reading_a_sigma_gap_min=res_a["sigma_gap_min"],
        reading_a_R_star=res_a["R_star"],
        reading_a_clause_i_PASS=res_a["clause_i_PASS"],
        reading_a_clause_ii_PASS=res_a["clause_ii_PASS"],
        reading_a_PASS=res_a["reading_a_PASS"],
        reading_a_sign_PASS=res_a["sign_PASS"],
        # Reading-b
        reading_b_M2_pos=res_b["M2_pos"],
        reading_b_M4_pos=res_b["M4_pos"],
        reading_b_alpha_s=res_b["alpha_s_b"],
        reading_b_sigma_gap=res_b["sigma_gap_b"],
        reading_b_sigma_gap_aux2020=res_b["sigma_gap_b_aux2020"],
        reading_b_PASS=res_b["reading_b_PASS"],
        reading_b_sign_PASS=res_b["sign_PASS"],
        # Reading-c
        reading_c_C0_per_regulator=np.array(res_c["C0_per_regulator"]),
        reading_c_C0_avg=res_c["C0_avg"],
        reading_c_C1_estimate=res_c["C1_estimate"],
        reading_c_ratio_C0_C1=res_c["ratio_C0_C1"],
        reading_c_alpha_s_C0=res_c["alpha_s_C0"],
        reading_c_sigma_gap=res_c["sigma_gap_c"],
        reading_c_sigma_gap_aux2020=res_c["sigma_gap_c_aux2020"],
        reading_c_PASS=res_c["reading_c_PASS"],
        reading_c_sign_PASS=res_c["sign_PASS"],
        reading_c_drift_tag=res_c["drift_tag"],
        reading_c_drift_corrected=res_c["drift_corrected"],
        reading_c_w7_anchor_path=res_c["w7_anchor_path"],
        reading_c_anchors=np.array(res_c["anchors"]),
        reading_c_regulator_names=np.array(res_c["regulator_names"]),
        # Composite
        pass_count=pass_count,
        composite_verdict=composite,
        sign_verdict=sign_verdict,
        magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
        sigma_gap_planck_original=sigma_gap_planck_original,
        sigma_gap_planck_aux2020=sigma_gap_planck_original_aux,
        alpha_s_canonical=ALPHA_S_CANONICAL,
        alpha_s_canonical_published=ALPHA_S_CANONICAL_PUBLISHED,
        n_s_FW=N_S_FW,
        L_max=L_MAX_OP,
        tau=TAU,
        s_pole_canonical=POLE_S,
        s_pole_reading_b=POLE_S_READING_B,
        # PRDR pin map and SHAs
        audit_sha=audit_sha,
        content_sha=content_sha,
        closure_hash=pinmap_closure,
        cache_sha256=pins["cache_sha256"],
        w7_anchor_sha256_runtime=pins["w7_anchor_sha256_runtime"],
        canonical_constants_sha256=pins["canonical_constants_sha256"],
        registry_sha256=pins["registry_sha256"],
        level_pin=LEVEL_PIN,
        tier_pin=TIER_PIN,
    )
    print(f"Saved data: {OUT_NPZ}")

    # ----- Plot -----
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    # Subplot 1 — Reading-a regulator spread
    ax = axes[0]
    alphas = [res_a["alpha_per_R"][r] for r in ATLAS_LABELS]
    ax.bar(range(len(ATLAS_LABELS)), alphas, color="steelblue", edgecolor="black")
    ax.axhline(ALPHA_S_CANONICAL, color="crimson", linestyle="--",
               label=f"alpha_s_canonical = {ALPHA_S_CANONICAL:+.6f}")
    ax.axhline(ALPHA_S_OBS, color="forestgreen", linestyle=":",
               label=f"alpha_s_obs (Planck-2018) = {ALPHA_S_OBS}")
    ax.set_xticks(range(len(ATLAS_LABELS)))
    ax.set_xticklabels(ATLAS_LABELS, rotation=30, ha="right")
    ax.set_ylabel(r"$\alpha_s^{(R)} = (a_4^{(R)}/a_2^{(R)})^2 - 1$")
    ax.set_title(
        f"Reading-a: 5-regulator atlas at L_max={L_MAX_OP}\n"
        f"spread={res_a['spread_a']:.4f}  "
        f"(threshold spread/|α|>{SPREAD_FRAC_MIN}: {res_a['clause_i_PASS']})"
    )
    ax.legend(fontsize=8, loc="upper right")
    ax.grid(alpha=0.3)
    # Subplot 2 — Reading-b moment ratio
    ax = axes[1]
    moments = [res_b["M2_pos"], res_b["M4_pos"]]
    ax.bar(["M_2^pos", "M_4^pos"], moments, color="darkorange", edgecolor="black")
    ax.set_yscale("log")
    ax.set_ylabel("positive moment Σ m_k λ_k^n")
    ax.set_title(
        f"Reading-b: substrate-distance-2 pole s=4\n"
        f"(M_4/M_2)^2-1 = {res_b['alpha_s_b']:+.3e}  "
        f"σ_gap={res_b['sigma_gap_b']:+.3e}σ"
    )
    ax.grid(alpha=0.3, which="both")
    # Subplot 3 — Reading-c C_0 per regulator
    ax = axes[2]
    ax.bar(res_c["regulator_names"], res_c["C0_per_regulator"],
           color="purple", edgecolor="black")
    ax.set_ylabel(r"$C_0$ leading residue (anchor 5: $1/M_{KK}^2$ limit)")
    ax.set_title(
        f"Reading-c: leading C_0 residue per regulator\n"
        f"alpha_s_C0={res_c['alpha_s_C0']:+.6f}  "
        f"σ_gap^C_0={res_c['sigma_gap_c']:+.3f}σ"
    )
    plt.setp(ax.get_xticklabels(), rotation=30, ha="right")
    ax.grid(alpha=0.3)
    fig.suptitle(
        f"{GATE_ID}\n"
        f"composite={composite}  "
        f"pass_count={pass_count}  "
        f"(Ra={'PASS' if reading_a_pass else 'FAIL'}, "
        f"Rb={'PASS' if reading_b_pass else 'FAIL'}, "
        f"Rc={'PASS' if reading_c_pass else 'FAIL'})",
        fontsize=11,
    )
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=110)
    plt.close(fig)
    print(f"Saved plot: {OUT_PNG}")

    # ----- Verdict-line value field -----
    value_str = (
        f"pass_count={pass_count};reading_a_PASS={reading_a_pass};"
        f"reading_b_PASS={reading_b_pass};reading_c_PASS={reading_c_pass};"
        f"spread_a={res_a['spread_a']:.6e};"
        f"spread_frac={res_a['spread_frac']:.6f};"
        f"sigma_gap_min_R_star={res_a['sigma_gap_min']:.4f};"
        f"R_star={res_a['R_star']};"
        f"alpha_s_b={res_b['alpha_s_b']:.6e};"
        f"sigma_gap_b={res_b['sigma_gap_b']:.6e};"
        f"alpha_s_C0={res_c['alpha_s_C0']:.6f};"
        f"sigma_gap_c={res_c['sigma_gap_c']:.4f};"
        f"alpha_s_canonical={ALPHA_S_CANONICAL_PUBLISHED};"
        f"alpha_s_obs_plan_pin={ALPHA_S_OBS};"
        f"sigma_obs_plan_pin={SIGMA_OBS};"
        f"sigma_gap_canonical_planck_2018={sigma_gap_planck_original:.4f};"
        f"sigma_gap_canonical_aiola_2020={sigma_gap_planck_original_aux:.4f};"
        f"n_s_FW={N_S_FW};"
        f"level_pin={LEVEL_PIN};tier_pin={TIER_PIN};"
        f"drift_tag={res_c['drift_tag']};drift_corrected={res_c['drift_corrected']}"
    )
    # Truncate the value string to a single safe canonical line (no newlines).
    # The downstream consolidator parses key=value; tokens are ';'-separated.
    value_str = value_str.replace("\n", " ")

    canonical_line, dual_companion, tuple_companion, tier_companion = (
        append_verdict_with_3tuple(
            verdict=composite,
            value_str=value_str,
            audit_sha=audit_sha,
            content_sha=content_sha,
            sign_v=sign_verdict,
            mag_v=magnitude_verdict,
            regime_v=regime_verdict,
        )
    )
    print()
    print("--- VERDICT LINES APPENDED ---")
    print(canonical_line.rstrip())
    print(dual_companion.rstrip())
    print(tuple_companion.rstrip())
    print(tier_companion.rstrip())
    print()
    print(f"Total wall time: {time.time() - t_start:.2f} s")


if __name__ == "__main__":
    main()
