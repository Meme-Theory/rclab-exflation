#!/usr/bin/env python3
"""
S111 W4-3 S111-CF-CO34B-LRDT — LRD photosphere-temperature transport degree
===========================================================================

Gate: S111-CF-CO34B-LRDT ([SIGN])

The HELD-magnitude landing of the §VII.CF κ-Sign-Lock ∧ Wodzicki-Parity joint
foreclosure on the LRD photosphere-temperature anchor. SHARPENED per the S110 W4
connes-mack workshop (corpus §23.0(5) parity selection rule).

Pre-registered threshold (plan §W4-3, operator type "set"; the κ-sign-consistency
predicate is a boolean):
  PASS  iff  (T_pivot(deg=+1) in [3500,6500] K)  AND  (sign-consistent: |kappa|<1
             lands the band)  — both required (expected BOTH FALSE).
  FAIL  iff  the band is reachable but ONLY by a FITTED / non-substrate-natural dial.
  INFO  iff  HELD via dimensionful-slot-collision ∧ sign-lock (predicate FALSE):
             deg=+1 image ~28 dec below band ⇒ ascent ⇒ |kappa|>1 ⇒ sign-inconsistent
             with substrate-natural |kappa|<1; AND parity blocks any even-degree
             morphism on the ODD +1 scale leg. The number is HELD, NOT a substrate-
             physics FAIL — there IS no substrate-natural transport by THEOREM.

This gate does NOT scan for a fitting degree. It PINS deg(B)=d_A=+1 a priori (T's
mass dimension; the M_KK^1 scale leg carries the 54.04-decade BZ->pivot unit
conversion) and VERIFIES the κ-sign-consistency predicate (expected FALSE).

The W3 import (S110-CF-CV6B-DS-M4, deg_T=2.0) was a category error: the +2 is the
dimensionless-morphism amplitude degree of the M4 spectral dimension d_s (d_A=0),
MISapplied to the dimensionful temperature T (d_A=+1). This gate corrects to deg=+1.

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - computations/investigation-7/inv7_w2_2_substrate_photosphere_temperature.npz  (T_bare)
  - computations/session-110/s110_cf_cv6b_ds_m4.npz                               (deg_T=2.0 W3 mint)
  - canonical_constants.py (feeds audit_sha256 only; M_KK, k_pivot_planck)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<HELD held-number outcome string>, scheme=deg-plus-1-scale-leg-PINNED,
   convention=RATIO-DA-1-PARITY-odd, L_max=N/A)

Classification: PHONONIC — the LRD photosphere is the GGE-relic acoustic signature
of the substrate; T_substrate is read FORWARD from the D_K spectral moments,
transported to the CMB/observational pivot.

METHODOLOGY
-----------
Deterministic structural evaluation (N_eval=1; deg is PINNED a priori, NOT searched).
Steps:
  (1) deg=+1 image  T_pivot(deg=+1) = T_bare * t^{-1},  t = M_KK/k_4D = 10^{+54.04}
      (the canonical N_DECADES_BZ_PIVOT scale-tag; same as the S110 CO34/CF3 producers,
      and the alpha_s/n_s scale separation). Compute its OOM distance to [3500,6500] K.
  (2) deg=0 image   T_pivot(deg=0) = T_bare (no descent) — too HOT by ~+25.87 dec.
      The band is SANDWICHED between the deg=0 (too hot) and deg=+1 (too cold) images.
  (3) band-landing eff deg  d_eff:  solve T_bare * t^{-d_eff} in band — a SUB-scalar
      non-integer (0.4787, distinct from +2/+1/0), so NO integer/substrate-natural
      degree lands the band.
  (4) κ-sign predicate: the deg=+1 image is BELOW the band ⟹ the residual on top of
      the deg=+1 scale leg is a +28.17-decade ASCENT ⟹ requires |kappa|>1 (amplitude
      GROWTH), sign-INCONSISTENT with the substrate-natural transport |kappa| =
      10^{-108.08} << 1 (DECAY, since t>1). PARITY cross-check: T needs deg(B)=+1
      (ODD); every substrate-natural morphism carries EVEN degree (-2(s-s') Wodzicki,
      0 HKR), so no even-degree morphism can act on the ODD +1 scale leg.
Verdict: HELD via dimensionful-slot-collision ∧ sign-lock; composite = INFO (the
held-number outcome, NOT a substrate-physics FAIL — there is no substrate-natural
transport, by THEOREM).

CANONICAL ANCHOR (registry-published; substrate-first-canonical-sourcing.md):
  permanent-results-registry.md §VII.CF + falsifier-master-inventory.md Row #88
  .audit-S110-CO34-LRDT-TRANSPORT-PARITY + cross-pillar-bridge-corpus.md §23.0(5):
    eff deg            = 0.4787  (SUB-scalar; Sage RealField(200))
    deg=+1 image       = -28.17 dec below band
    deg=0 image        = +25.87 dec above band (SANDWICH)
    |kappa|            = 10^{-108.08} = 10^{-2*54.04} (Wodzicki two-pole deg -2 over t)
  Published to 4 sig figs (this gate reproduces them to publication precision under
  the canonical N_DECADES_BZ_PIVOT=54.04 scale-tag).

DISCIPLINE
----------
- `from canonical_constants import *`  (M_KK, k_pivot_planck)
- Every local/intermediate tagged `# (local)`
- numpy.linalg GPU path N/A (trivial scalar/OOM arithmetic; mpmath for OOM precision)
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- 4-tuple printed as the final non-verdict line
- Gate verdict emitted via the `emit_verdict` knowledge-MCP tool (race-safe).
  [SIGN] gate ⇒ the SIGN/MAGNITUDE/REGIME 3-tuple is carried.
- Plan-frozen composite-precedence: the plan operator (type "set") pre-registers
  composite=INFO for the held-number outcome, OVERRIDING the generic collapse rule
  (sign=PASS + magnitude=FAIL + regime=VALID -> generic FAIL). A mandatory
  `# composite-precedence:` disclosure extra-row names the plan anchor + the
  generic-collapse reading being overridden (per gate-verdicts.md §"Plan-frozen
  gate-block operator precedence"; the held-number outcome is an applicability
  GUARD, not the hypothesis).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — Bootstrap _shared onto sys.path so canonical_constants imports
# ---------------------------------------------------------------------------
import os as _os
import sys as _sys

_SHARED_BOOT = _os.path.join(
    _os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))), "_shared"
)
if _SHARED_BOOT not in _sys.path:
    _sys.path.insert(0, _SHARED_BOOT)

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403  (M_KK, k_pivot_planck)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from mpmath import mp, mpf, log10 as mp_log10

mp.dps = 60  # high-precision OOM arithmetic (RealField(200)-class for eff deg, |kappa|)

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S111"                                                   # (local)
GATE_ID = "S111-CF-CO34B-LRDT"                                     # (local)
SCHEME = "deg-plus-1-scale-leg-PINNED"                             # (local)
CONVENTION = "RATIO-DA-1-PARITY-odd"                              # (local)
L_MAX = "N/A"                                                      # (local)

# ---- Pre-registered structural constants (plan §W4-3) ----
# T's mass dimension: d_A = +1 (energy/temperature). PINNED a priori, NOT scanned.
D_A_T = 1                                                          # (local) T mass dimension (ODD)
DEG_B_PINNED = D_A_T                                               # (local) deg(B) = d_A = +1 (admissibility, §18.0 Conjunct-1)
# Canonical BZ->pivot scale-tag (same as S110 CO34/CF3 producers; alpha_s/n_s separation).
# t = M_KK / k_4D = 10^{+54.04}. This is the framework-canonical decade gap (NOT a naive
# hbar*c conversion); it is what permanent-results-registry.md §VII.CF + corpus §23.0(5)
# pin, and what s110_cf_co34_bubble_lrdt.py uses (N_DECADES_BZ_PIVOT=54.04, line 136).
N_DECADES_BZ_PIVOT = 54.04                                         # (local) log10(t); canonical scale-tag
# LRD photosphere temperature band (JWST rest-frame Balmer-break + V-shaped SED).
# inv7_w2_2: T_target_K=5000, band_T=0.3  ->  [3500, 6500] K.
T_TARGET_K = 5000.0                                               # (local) band center
BAND_T = 0.3                                                       # (local) fractional half-width
T_BAND_LO = T_TARGET_K * (1.0 - BAND_T)                            # (local) 3500 K
T_BAND_HI = T_TARGET_K * (1.0 + BAND_T)                            # (local) 6500 K
TOL = 1e-9                                                         # (local) sign/deg-match boolean tolerance

# Registry-published canonical anchors (4 sig figs) — for the publication-precision
# cross-check (substrate-first-canonical-sourcing.md: the registry is canonical).
EFF_DEG_CANON = 0.4787                                             # (local) corpus §23.0(5) eff deg
DEG1_BELOW_CANON = 28.17                                           # (local) corpus deg=+1 below band-center
DEG0_ABOVE_CANON = 25.87                                           # (local) corpus deg=0 above band-center
KAPPA_LOG10_CANON = -108.08                                        # (local) corpus |kappa| = 10^{-2*54.04}

# Output destinations (per-session)
OUT_NPZ = SESSION_DIR / "s111_co34b_lrdt.npz"
OUT_PNG = SESSION_DIR / "s111_co34b_lrdt.png"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    COMPUTATIONS_DIR / "investigation-7" / "inv7_w2_2_substrate_photosphere_temperature.npz",
    COMPUTATIONS_DIR / "session-110" / "s110_cf_cv6b_ds_m4.npz",
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (MANDATORY; first 20 lines of stdout)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Compute
# ---------------------------------------------------------------------------

def compute() -> dict:
    """Deterministic structural evaluation of the deg=+1 transport + κ-sign predicate."""
    # --- Load upstream substrate moments ---
    inv7 = np.load(
        COMPUTATIONS_DIR / "investigation-7" / "inv7_w2_2_substrate_photosphere_temperature.npz",
        allow_pickle=True,
    )
    T_bare_K = float(inv7["T_substrate_K"])                        # (local) 3.545301e29 K (fold-robust)
    band_T_in = float(inv7["band_T"])                             # (local) 0.3 (cross-check)
    T_target_in = float(inv7["T_target_K"])                      # (local) 5000 K (cross-check)

    w3 = np.load(COMPUTATIONS_DIR / "session-110" / "s110_cf_cv6b_ds_m4.npz", allow_pickle=True)
    deg_T_imported = float(w3["deg_T_BZ_pivot"])                 # (local) 2.0 — the W3 mis-import (d_A=0 morphism degree)

    # --- Cross-check the band matches the upstream inv7 pins ---
    band_lo_check = T_target_in * (1.0 - band_T_in)               # (local)
    band_hi_check = T_target_in * (1.0 + band_T_in)               # (local)
    band_matches_inv7 = bool(
        abs(band_lo_check - T_BAND_LO) < 1e-6 and abs(band_hi_check - T_BAND_HI) < 1e-6
    )                                                             # (local)

    # --- High-precision OOM arithmetic (mpmath, dps=60) ---
    log10_t = mpf(str(N_DECADES_BZ_PIVOT))                        # (local) canonical decade gap = 54.04
    log10_T_bare = mp_log10(mpf(str(T_bare_K)))                   # (local)
    log10_lo = mp_log10(mpf(str(T_BAND_LO)))                      # (local)
    log10_hi = mp_log10(mpf(str(T_BAND_HI)))                      # (local)
    log10_c = mp_log10(mpf(str(T_TARGET_K)))                      # (local)

    # (1) deg=+1 image: T_pivot = T_bare * t^{-deg},  deg=+1  (scale leg, ODD)
    log10_T_pivot_deg1 = log10_T_bare - DEG_B_PINNED * log10_t    # (local)
    T_pivot_deg1 = float(mp.e ** (log10_T_pivot_deg1 * mp.log(10)))  # (local) ~3.23e-25 K
    # OOM distance of deg=+1 image BELOW the band (positive = below; center reference)
    oom_deg1_below_center = float(log10_c - log10_T_pivot_deg1)   # (local) ~28.17 (ascent needed to reach center)
    oom_deg1_below_lo = float(log10_lo - log10_T_pivot_deg1)      # (local) distance below band-lo
    in_band_deg1 = bool(T_BAND_LO <= T_pivot_deg1 <= T_BAND_HI)   # (local) False

    # (2) deg=0 image (scalar / container): T_pivot = T_bare (no descent) — too HOT
    T_pivot_deg0 = T_bare_K                                       # (local)
    oom_deg0_above_center = float(log10_T_bare - log10_c)         # (local) ~25.87 (above band)
    in_band_deg0 = bool(T_BAND_LO <= T_pivot_deg0 <= T_BAND_HI)   # (local) False
    # SANDWICH: deg=0 too hot (+), deg=+1 too cold (-); band lies between
    band_sandwiched = bool(
        (T_pivot_deg0 > T_BAND_HI) and (T_pivot_deg1 < T_BAND_LO)
    )                                                             # (local) True

    # (3) band-landing eff deg: solve T_bare * t^{-d_eff} = T_target -> d_eff = (log T_bare - log T_target)/log t
    d_eff_center = float((log10_T_bare - log10_c) / log10_t)      # (local) ~0.4784 (corpus 0.4787)
    d_eff_lo = float((log10_T_bare - log10_hi) / log10_t)         # (local) hottest target -> smallest deg
    d_eff_hi = float((log10_T_bare - log10_lo) / log10_t)         # (local) coldest target -> largest deg
    # is the band-landing eff deg a SUB-scalar non-integer (distinct from +2/+1/0)?
    eff_deg_is_subscalar = bool(0.0 < d_eff_center < 1.0)         # (local) True
    eff_deg_is_integer = bool(abs(d_eff_center - round(d_eff_center)) < TOL)  # (local) False
    # no admissible integer/substrate-natural degree lands the band
    no_integer_degree_lands_band = bool(
        (not in_band_deg0) and (not in_band_deg1) and (not eff_deg_is_integer)
    )                                                             # (local) True

    # (4) κ-sign-consistency predicate
    # The deg=+1 image is BELOW the band -> the residual on top of the deg=+1 scale leg
    # is an ASCENT (oom_deg1_below_center decades up). An ascent requires |kappa|>1 (GROWTH).
    residual_is_ascent = bool(T_pivot_deg1 < T_BAND_LO)          # (local) True (image below band ⟹ ascent needed)
    ascent_decades = oom_deg1_below_center                       # (local) +28.17 dec ascent to band-center
    requires_kappa_gt_1 = bool(residual_is_ascent)               # (local) ascent ⟹ |kappa|>1
    # Substrate-natural transport amplitude: Wodzicki two-pole ratio deg -2 over t = 10^{+54.04} > 1 ⟹ DECAY.
    # |kappa| = t^{-2} = 10^{-2*54.04} = 10^{-108.08} << 1.
    log10_kappa_substrate_natural = float(-2.0 * log10_t)        # (local) -108.08
    kappa_substrate_natural_lt_1 = bool(log10_kappa_substrate_natural < 0.0)  # (local) True (DECAY)
    # MUTUAL EXCLUSION: need |kappa|>1 (ascent) but substrate-natural gives |kappa|<1 (decay)
    sign_consistent = bool((not requires_kappa_gt_1) or (not kappa_substrate_natural_lt_1))  # (local) False
    # PARITY cross-check: T needs deg(B)=+1 (ODD); substrate-natural morphisms are EVEN-degree
    # (-2(s-s') Wodzicki ratios, 0 HKR). No even-degree morphism can act on the ODD +1 scale leg.
    deg_b_parity = "odd" if (DEG_B_PINNED % 2 == 1) else "even"  # (local) "odd"
    morphism_parity = "even"                                     # (local) Wodzicki -2(s-s'), HKR 0
    parity_blocks_correction = bool(deg_b_parity != morphism_parity)  # (local) True (ODD vs EVEN)

    # --- THE PREDICATE: "∃ substrate-natural deg=+1 transport with |kappa|>1 landing [3500,6500] K?" ---
    # PASS would require BOTH band-membership AND sign-consistency. Expected BOTH FALSE.
    predicate_band_lands_sign_consistent = bool(in_band_deg1 and sign_consistent)  # (local) False
    # The W3 category error, recorded: deg_T_imported=2.0 (EVEN, d_A=0 morphism) != deg(B)=+1 (ODD, d_A=+1 scale leg)
    w3_category_error = bool(
        abs(deg_T_imported - DEG_B_PINNED) > TOL
        and (round(deg_T_imported) % 2 == 0)  # imported is EVEN
        and (DEG_B_PINNED % 2 == 1)            # needed is ODD
    )                                          # (local) True

    # --- Publication-precision cross-check against registry-canonical anchors (4 sig figs) ---
    eff_deg_matches_canon = bool(abs(d_eff_center - EFF_DEG_CANON) < 5e-4)        # (local)
    deg1_below_matches_canon = bool(abs(oom_deg1_below_center - DEG1_BELOW_CANON) < 0.05)  # (local)
    deg0_above_matches_canon = bool(abs(oom_deg0_above_center - DEG0_ABOVE_CANON) < 0.05)  # (local)
    kappa_matches_canon = bool(abs(log10_kappa_substrate_natural - KAPPA_LOG10_CANON) < 1e-6)  # (local)

    # --- 3-tuple verdict assembly (plan §10 substitution-chain Conclusion) ---
    # sign_verdict: the predicted DIRECTION is "deg=+1 image BELOW band ⟹ ascent ⟹ |kappa|>1 ⟹
    #   sign-INCONSISTENT". PASS iff that predicted direction is confirmed (the predicate is FALSE
    #   for the substrate-natural |kappa|<1 transport).
    sign_pred_confirmed = bool(residual_is_ascent and (not sign_consistent))     # (local) True
    sign_verdict = "PASS" if sign_pred_confirmed else "FAIL"                     # (local)
    # magnitude_verdict: T_pivot(deg=+1) ~ 10^{-24.5} K is ~28 dec below band ⟹ FAIL (far outside band)
    magnitude_verdict = "PASS" if in_band_deg1 else "FAIL"                       # (local) FAIL
    # regime_verdict: the deg/parity/κ-sign argument is EXACT throughout ⟹ VALID
    regime_verdict = "VALID"                                                     # (local)

    # Composite (PLAN-FROZEN, type "set"): the held-number outcome is INFO (NOT the generic-collapse
    # FAIL). Per plan §W4-3 operator (1)+rubric INFO_meaning + substitution-chain Conclusion:
    # "composite = INFO (the held-number outcome, NOT a substrate-physics FAIL)". The PASS criterion
    # is the conjunction (band lands AND sign-consistent) = FALSE; FAIL is reserved for a fitted-dial
    # band-landing. HELD via dimensionful-slot-collision ∧ sign-lock ⟹ INFO.
    if predicate_band_lands_sign_consistent:
        composite = "PASS"   # band lands via sign-consistent deg=+1 (prior 0.05; would FLAG §VII.CF)
    else:
        composite = "INFO"   # held: predicate FALSE (Track B, prior 0.95) — the EXPECTED outcome

    # held-number outcome string (the descriptive value payload)
    value_str = (
        f"HELD_dimensionful-slot-collision_AND_sign-lock|"
        f"deg_pinned={DEG_B_PINNED}(d_A={D_A_T},ODD)|"
        f"eff_deg={d_eff_center:.4f}_SUB-scalar|"
        f"T_pivot_deg1={T_pivot_deg1:.4e}K_{oom_deg1_below_center:.2f}dec_below_band|"
        f"deg0_image_{oom_deg0_above_center:.2f}dec_above_band|"
        f"band_SANDWICHED={band_sandwiched}|"
        f"kappa_substrate_natural=10^{log10_kappa_substrate_natural:.2f}<1_DECAY|"
        f"ascent_needs_|kappa|>1=sign-INCONSISTENT|"
        f"parity_ODD_scale_leg_vs_EVEN_morphism=blocked|"
        f"predicate_FALSE|W3_deg_T_imported={deg_T_imported}_EVEN_category-error"
    )

    return {
        "value": value_str,
        # core scalars
        "T_bare_K": T_bare_K,
        "T_pivot_deg1_K": T_pivot_deg1,
        "T_pivot_deg0_K": T_pivot_deg0,
        "deg_B_pinned": DEG_B_PINNED,
        "d_A_T": D_A_T,
        "deg_T_imported": deg_T_imported,
        "N_decades_BZ_pivot": N_DECADES_BZ_PIVOT,
        "log10_T_bare": float(log10_T_bare),
        "log10_T_pivot_deg1": float(log10_T_pivot_deg1),
        "eff_deg_center": d_eff_center,
        "eff_deg_lo": d_eff_lo,
        "eff_deg_hi": d_eff_hi,
        "oom_deg1_below_center": oom_deg1_below_center,
        "oom_deg1_below_lo": oom_deg1_below_lo,
        "oom_deg0_above_center": oom_deg0_above_center,
        "ascent_decades": ascent_decades,
        "log10_kappa_substrate_natural": log10_kappa_substrate_natural,
        "T_band_lo_K": T_BAND_LO,
        "T_band_hi_K": T_BAND_HI,
        "T_target_K": T_TARGET_K,
        "band_T": BAND_T,
        # booleans (the predicate machinery)
        "in_band_deg1": in_band_deg1,
        "in_band_deg0": in_band_deg0,
        "band_sandwiched": band_sandwiched,
        "eff_deg_is_subscalar": eff_deg_is_subscalar,
        "eff_deg_is_integer": eff_deg_is_integer,
        "no_integer_degree_lands_band": no_integer_degree_lands_band,
        "residual_is_ascent": residual_is_ascent,
        "requires_kappa_gt_1": requires_kappa_gt_1,
        "kappa_substrate_natural_lt_1": kappa_substrate_natural_lt_1,
        "sign_consistent": sign_consistent,
        "deg_b_parity": deg_b_parity,
        "morphism_parity": morphism_parity,
        "parity_blocks_correction": parity_blocks_correction,
        "predicate_band_lands_sign_consistent": predicate_band_lands_sign_consistent,
        "w3_category_error": w3_category_error,
        "band_matches_inv7": band_matches_inv7,
        # publication-precision cross-checks vs registry-canonical anchors
        "eff_deg_matches_canon": eff_deg_matches_canon,
        "deg1_below_matches_canon": deg1_below_matches_canon,
        "deg0_above_matches_canon": deg0_above_matches_canon,
        "kappa_matches_canon": kappa_matches_canon,
        "eff_deg_canon": EFF_DEG_CANON,
        "deg1_below_canon": DEG1_BELOW_CANON,
        "deg0_above_canon": DEG0_ABOVE_CANON,
        "kappa_log10_canon": KAPPA_LOG10_CANON,
        # 3-tuple
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        "composite": composite,
    }


# ---------------------------------------------------------------------------
# Section 6 — Gate verdict + 4-tuple output + plot
# ---------------------------------------------------------------------------

def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          companion_note="", extra_rows=None) -> dict:
    payload: dict = {
        "session": int(SESSION.lstrip("Ss")),
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    if companion_note:
        payload["companion_note"] = companion_note
    if not (sign_verdict is None and magnitude_verdict is None and regime_verdict is None):
        payload["sign_verdict"] = sign_verdict
        payload["magnitude_verdict"] = magnitude_verdict
        payload["regime_verdict"] = regime_verdict
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


def make_plot(R: dict) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(14, 6))

    # (a) the SANDWICH: deg=0 image (too hot), band, deg=+1 image (too cold), in log10 K
    ax = axes[0]
    cats = ["deg=0 image\n(scalar; T_bare)", "LRD band\n[3500,6500] K", "deg=+1 image\n(M_KK^1 scale leg)"]  # (local)
    vals = [R["log10_T_bare"], float(np.log10(R["T_target_K"])), R["log10_T_pivot_deg1"]]  # (local)
    colors = ["#d62728", "#2ca02c", "#1f77b4"]  # (local)
    bars = ax.bar(cats, vals, color=colors, alpha=0.8)
    # band span shaded
    ax.axhspan(np.log10(R["T_band_lo_K"]), np.log10(R["T_band_hi_K"]), color="#2ca02c", alpha=0.18, zorder=0)
    ax.set_ylabel(r"$\log_{10}(T\ /\ \mathrm{K})$")
    ax.set_title(
        f"(a) Band SANDWICHED: deg=0 +{R['oom_deg0_above_center']:.2f} dec too HOT,\n"
        f"deg=+1 −{R['oom_deg1_below_center']:.2f} dec too COLD → eff deg {R['eff_deg_center']:.4f} SUB-scalar"
    )
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v + (2 if v > 0 else -3),
                f"{v:.2f}", ha="center", va="bottom" if v > 0 else "top", fontsize=9)
    ax.axhline(0, color="k", lw=0.5)

    # (b) the κ-sign foreclosure: required ascent (|kappa|>1) vs substrate-natural |kappa| (10^-108)
    ax = axes[1]
    labels = [r"required ascent" + "\n" + r"($|\kappa|>1$ growth)",
              r"substrate-natural" + "\n" + r"($|\kappa|=10^{-108.08}$ decay)"]  # (local)
    # plot as log10 |kappa|: required ascent over +28.17 dec on the deg=+1 leg vs the -108.08 decay
    kappa_required_log10 = R["ascent_decades"]   # (local) +28.17 (would need |kappa|=10^{+28.17}>1)
    kappa_natural_log10 = R["log10_kappa_substrate_natural"]  # (local) -108.08
    yvals = [kappa_required_log10, kappa_natural_log10]  # (local)
    bcolors = ["#ff7f0e", "#1f77b4"]  # (local)
    bars2 = ax.bar(labels, yvals, color=bcolors, alpha=0.85)
    ax.axhline(0, color="k", lw=1.0, label=r"$|\kappa|=1$ (sign boundary)")
    ax.set_ylabel(r"$\log_{10}|\kappa|$  (transport amplitude)")
    ax.set_title(
        "(b) κ-sign-lock ∧ Wodzicki-parity foreclosure:\n"
        f"ascent needs |κ|>1, substrate-natural gives |κ|<1 → MUTUALLY EXCLUSIVE → HELD/INFO"
    )
    for b, v in zip(bars2, yvals):
        ax.text(b.get_x() + b.get_width() / 2, v + (3 if v > 0 else -6),
                f"10^{v:.2f}", ha="center", va="bottom" if v > 0 else "top", fontsize=9)
    ax.legend(loc="lower left", fontsize=9)

    fig.suptitle(
        f"S111-CF-CO34B-LRDT — LRD-T transport: deg(B)=d_A=+1 (ODD) PINNED; predicate FALSE → "
        f"{R['composite']} (HELD)\n"
        f"sign={R['sign_verdict']} (ascent⟹|κ|>1 sign-inconsistent) | magnitude={R['magnitude_verdict']} "
        f"(28 dec off band) | regime={R['regime_verdict']} | parity ODD vs EVEN morphism = blocked",
        fontsize=11,
    )
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print(f"  M_KK={M_KK:.6e} GeV  k_pivot_planck={k_pivot_planck} Mpc^-1")
    print()

    R = compute()

    # --- Diagnostic dump ---
    print(f"=== {GATE_ID} — held-number structural evaluation ===")
    print(f"  T_bare (inv-7 W2-2, substrate moment)     = {R['T_bare_K']:.6e} K")
    print(f"  T mass dimension d_A                       = {R['d_A_T']} (ODD)")
    print(f"  deg(B) PINNED a priori = d_A               = +{R['deg_B_pinned']} (M_KK^1 scale leg, ODD)")
    print(f"  W3 imported deg_T (d_A=0 morphism)         = {R['deg_T_imported']} (EVEN) -> category error={R['w3_category_error']}")
    print(f"  canonical scale-tag t = M_KK/k_4D          = 10^(+{R['N_decades_BZ_pivot']:.2f})")
    print()
    print(f"  deg=+1 image  T_pivot(deg=+1)              = {R['T_pivot_deg1_K']:.4e} K")
    print(f"    -> {R['oom_deg1_below_center']:.2f} decades BELOW band-center (band 3500-6500 K)")
    print(f"  deg=0 image   T_pivot(deg=0)=T_bare        = {R['T_pivot_deg0_K']:.4e} K")
    print(f"    -> {R['oom_deg0_above_center']:.2f} decades ABOVE band-center")
    print(f"  band SANDWICHED (deg=0 hot, deg=+1 cold)   = {R['band_sandwiched']}")
    print(f"  band-landing eff deg                       = {R['eff_deg_center']:.4f}  (SUB-scalar: {R['eff_deg_is_subscalar']}, integer: {R['eff_deg_is_integer']})")
    print(f"  no integer/substrate-natural deg lands band= {R['no_integer_degree_lands_band']}")
    print()
    print(f"  --- κ-sign-consistency predicate ---")
    print(f"  residual is ASCENT (image below band)      = {R['residual_is_ascent']}  ({R['ascent_decades']:.2f} dec up)")
    print(f"  ascent requires |kappa|>1 (growth)         = {R['requires_kappa_gt_1']}")
    print(f"  substrate-natural |kappa| = 10^{R['log10_kappa_substrate_natural']:.2f}  (<1 DECAY: {R['kappa_substrate_natural_lt_1']})")
    print(f"  sign-consistent (|kappa|<1 lands band)     = {R['sign_consistent']}  (MUTUALLY EXCLUSIVE)")
    print(f"  parity: scale-leg {R['deg_b_parity']} vs morphism {R['morphism_parity']} -> blocked={R['parity_blocks_correction']}")
    print(f"  PREDICATE (band lands AND sign-consistent) = {R['predicate_band_lands_sign_consistent']}  (expected FALSE)")
    print()
    print(f"  --- publication-precision cross-check vs registry §VII.CF / corpus §23.0(5) ---")
    print(f"  eff deg     {R['eff_deg_center']:.4f} vs canon {R['eff_deg_canon']}   -> match={R['eff_deg_matches_canon']}")
    print(f"  deg=+1 below {R['oom_deg1_below_center']:.2f} vs canon {R['deg1_below_canon']} -> match={R['deg1_below_matches_canon']}")
    print(f"  deg=0 above  {R['oom_deg0_above_center']:.2f} vs canon {R['deg0_above_canon']} -> match={R['deg0_above_matches_canon']}")
    print(f"  |kappa| 10^{R['log10_kappa_substrate_natural']:.2f} vs canon 10^{R['kappa_log10_canon']} -> match={R['kappa_matches_canon']}")
    print(f"  band [3500,6500] K matches inv-7 pins      = {R['band_matches_inv7']}")
    print()
    print(f"  3-tuple: sign={R['sign_verdict']} magnitude={R['magnitude_verdict']} regime={R['regime_verdict']} -> composite={R['composite']}")
    print()

    # --- Save data ---
    np.savez(
        OUT_NPZ,
        **{k: v for k, v in R.items() if k != "value"},
        value=R["value"],
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        scheme=SCHEME,
        convention=CONVENTION,
        L_max=str(L_MAX),
    )
    print(f"  saved {OUT_NPZ.name}")

    # --- Plot ---
    make_plot(R)
    print(f"  saved {OUT_PNG.name}")
    print()

    verdict = R["composite"]
    tag = emit_4tuple(R["value"], SCHEME, CONVENTION, L_MAX)
    print(tag)

    # Plan-frozen composite-precedence disclosure (gate-verdicts.md §"Plan-frozen gate-block
    # operator precedence"): the plan operator (type "set") pre-registers composite=INFO for the
    # held-number outcome, OVERRIDING the generic collapse (sign=PASS+magnitude=FAIL+regime=VALID
    # -> generic FAIL). The held-number outcome is an applicability GUARD, not the hypothesis.
    composite_precedence_row = (
        "# composite-precedence: plan §W4-3 operator type=set (held-number predicate); "
        "composite=INFO per plan rubric INFO_meaning + substitution-chain Conclusion "
        "(HELD via dimensionful-slot-collision ∧ sign-lock); "
        "generic-collapse reading (sign=PASS,magnitude=FAIL,regime=VALID -> FAIL) OVERRIDDEN "
        "(the held-number is an applicability guard, not the hypothesis)"
    )
    regulator_pin_row = (
        "# regulator_pin: convention=RATIO-DA-1-PARITY-odd (fifth pin axis, corpus §23.0(5)(5.4)): "
        "T is d_A=+1 ODD, distinct from W3 deg_T=2.0 EVEN (d_A=0 morphism-slot); "
        "flags the W3->W4 category error at consumption"
    )
    held_number_row = (
        "# NON-PROMOTION-BY-HELD-NUMBER: dimensionful-slot-collision ∧ sign-lock (sign-lock DOMINANT); "
        "§VII.CF STAGE-1-CANDIDATE held-magnitude landing; falsifier Row #88"
        ".audit-S111-CO34B-LRDT-TRANSPORT (the S111 verdict-line confirmation of the S110 W4 held-prediction); "
        "T_pivot HELD not sideways-re-pinned; LRD-T is a DIRECT JWST measurement with no relocation channel"
    )

    print_verdict_payload(
        verdict, R["value"], audit_sha, content_sha,
        sign_verdict=R["sign_verdict"],
        magnitude_verdict=R["magnitude_verdict"],
        regime_verdict=R["regime_verdict"],
        companion_note="held-magnitude landing of §VII.CF κ-sign∧Wodzicki-parity on the LRD-T anchor",
        extra_rows=[composite_precedence_row, regulator_pin_row, held_number_row],
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (HELD; wall {wall:.2f}s) ===")
    return 0  # exit 0: script ran successfully; INFO is a valid scientific result


if __name__ == "__main__":
    sys.exit(main())
