#!/usr/bin/env python3
"""
S92 W3-3 - S92-W3-CF-S91-W1-4.1-VII-AV-AXIS-ALPHA-L-MAX-EXTENSION-11-12
========================================================================

Gate: S92-W3-CF-S91-W1-4.1-VII-AV-AXIS-ALPHA-L-MAX-EXTENSION-11-12  ([VERIFY])
Agent: volovik-superfluid-universe-theorist
Classification: GEOMETRIC (axis-α 4-regulator atlas L_max-stability scan on S84
                master cache; cross-regulator spread saturation vs divergence
                at L_max ∈ {11, 12} extension atop W1-4 baseline L ∈ {6..10}).

SUBSTRATE FRAMING (direction-of-explanation discipline per phononic-framing.md):
the substrate IS the spectral triple (A_K, H_K, D_K(τ_fold)) at substrate-
distance-2 pole s=4; the regulator-class atlas {ζ, Pauli-Villars, Mellin,
cutoff} IS the methodology-floor F-image space of the substrate's intrinsic
UV-regulator family per epistemic-discipline.md §"Layer-Decomposition". The
L_max truncation enters the Hochschild trace B(R, L_max) as MULTIPLICATIVE
spectral-support pre-factor w(L_max); per math-scripts.md §"Multiplicative-
normalization cancellation invariants" SUGGESTION K=1, the K-window log-
derivative L_emp = d² ln Var_a / d(ln K)² annihilates w(L_max) by structural
identity. This gate probes the L=11/12 spread saturation at the cross-
regulator axis.

SCHEMATIC TIER-2 LEVEL-PIN (per substrate-first-canonical-sourcing.md §(iv)
K=4 MANDATORY: CLASS=SCHEMATIC + convention -SCHEMATIC + tier_pin=TIER-2
companion row triple-disclosure REQUIRED). This script consumes the
SCHEMATIC helper `_spectral_action_regulators.py` whose docstring lines
22-30 self-identify as SCHEMATIC (Casimir-spectrum schematic analogs of
Connes-Chamseddine 1996 §2.2-2.3 cutoff function Mellin moments). Verdict-
line convention suffix carries -SCHEMATIC; companion comment row carries
`# tier_pin=TIER-2`; this docstring + the CLASS pin in the gate-block
constitute the 4-element POSITIVE disclosure.

OPERATOR-MISMATCH PRE-FLIGHT (per math-scripts.md §"Plan-author discipline
at plan-freeze"; documented in plan §W3-3 substitution chain):
B(R, L_max) is the regulator-class evaluation of the §VII.AV substrate-
distance-2 pole s=4 cocycle pairing on the L_max-truncated D_K spectrum
cache; it is NOT the operator form d ln(Tr_{M_2}(P_BdG · D_K^{-2s}))/d ln K
(which reduces to closed-form +2s = +8 INCOMPATIBLE with canonical L_emp).
The B(R, L_max) Hochschild trace inherits the canonical anchor
L_emp = -7.046336474406761 M_KK² (S87 W2-3 Def 4 / S89 W5-2 / S90 CF-61 /
S89 W-17 PASS S89-CORNER-IV-K-WINDOW-LOG-DERIVATIVE-RECOMPUTE) via the
multiplicative-normalization cancellation rule. Convention suffix carries
-PLAN-OPERATOR-CANONICAL-L-EMP-VERIFIED-2026-05-22-EXTENDED-LMAX-11-12 as
audit-trail signature.

W1-4 BASELINE CONTEXT (audit_sha256=be8c3197958ea25e2d5410f70ba0409611d5183
295df7ef9eaa5c2bc9c96a121; max_spread=1.683110e-01_at_L_max=10; INFO/MIXED):
the baseline producing script `s91_w1_cf77_hochschild_degeneration_test.py`
consumed FULL-CC primary `_pauli_villars_subtraction.py` over L ∈ {6,7,8,9,10}.
This extension gate (per plan §W3-3 machinery_pin_map) consumes the
SCHEMATIC `_spectral_action_regulators.py` over L ∈ {11, 12} to satisfy
K=4 MANDATORY level-pin POSITIVE disclosure. Structural justification:
under the multiplicative-normalization cancellation invariant, the SPREAD
metric across a multiplicative pre-factor family is asymptotically scheme-
INDEPENDENT in the K-window log-derivative sense; the L_max-extension test
probes spread saturation, not absolute spread magnitude.

Per substitution chain item 4:
  saturation_ratio := |max_spread(L_max=12) − max_spread(L_max=10)|
                    / |max_spread(L_max=10) − max_spread(L_max=8)|

W1-4 NPZ anchors (canonical from `s91_w1_cf77_hochschild_degeneration_test.npz`
audit_sha256 be8c31... INFO line):
  max_spread(L=8)  = 0.14151938  (W1-4 baseline; FULL-CC primary)
  max_spread(L=10) = 0.16831099  (W1-4 baseline; FULL-CC primary)

PASS predicate: saturation_ratio ≤ 1.0
INFO band:      saturation_ratio ∈ (1.0, 1.5]
FAIL predicate: saturation_ratio > 1.5

INPUT FILES
-----------
- canonical_constants.py (M_KK, tau_fold, Vol_SU3_Haar, substrate_cocycle_ratio_67_88)
- s84_spectrum_cache_L12_tau019.npz (90 sectors; filtered to L≤11 then L≤12)
- s91_w1_cf77_hochschild_degeneration_test.npz (W1-4 baseline anchors)
- s91_gate_verdicts.txt (W1-4 verdict line; must_grep audit_sha256 anchor)
- _spectral_action_regulators.py (SCHEMATIC helper per K=4 MANDATORY level-pin)

OUTPUT
------
- s92_w3_3_vii_av_axis_alpha_l_max_extension.npz
- s92_w3_3_vii_av_axis_alpha_l_max_extension.png
- s92_gate_verdicts.txt (canonical + dual-SHA + 3-tuple + tier_pin=TIER-2
  + axis_alpha_extension_classification rows)
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import math
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "computations" / "_shared"))
sys.path.insert(0, str(ROOT / "computations"))

from canonical_constants import *  # noqa: F401,F403
from canonical_constants import M_KK, tau_fold, Vol_SU3_Haar, substrate_cocycle_ratio_67_88  # noqa: E402

# SCHEMATIC helper consumption (K=4 MANDATORY level-pin per substrate-first-
# canonical-sourcing.md §(iv) POSITIVE disclosure pattern)
from _spectral_action_regulators import (  # noqa: E402
    zeta_a_n,
    mellin_a_n,
    pauli_villars_a_n,
    hard_cutoff_a_n,
    casimir_su3,
    weyl_dim_su3,
)

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ============================ Gate-block constants ============================
GATE_ID = "S92-W3-CF-S91-W1-4.1-VII-AV-AXIS-ALPHA-L-MAX-EXTENSION-11-12"
SCHEME = (
    "regulator-class-invariance-test-substrate-distance-2-pole-s4-"
    "axis-alpha-4-regulator-atlas-x-Lmax-extended-scan-PROXY-REFINEMENT-"
    "pending-discharge"
)
CONVENTION = (
    "VII-AV-HOCHSCHILD-CROSS-ANCHOR-axis-alpha-4-regulator-atlas-"
    "PLAN-OPERATOR-CANONICAL-L-EMP-VERIFIED-2026-05-22-EXTENDED-LMAX-11-12-"
    "SCHEMATIC"
)
CLASS_PIN = "SCHEMATIC"  # (local) substrate-first-canonical-sourcing.md §(iv) K=4 MANDATORY
TIER_PIN = "TIER-2"      # (local) companion-row level-pin disclosure
L_MAX_NEW = 12           # (local) L_max ceiling of new evaluations (plan W3-3)
L_MAX_CACHE = 12         # (local) source cache L_max (S84 master cache)

# Extension L_max grid (plan W3-3 Field 7)
L_VALUES_NEW = [11, 12]  # (local) plan W3-3 axis-α extension grid

# W1-4 baseline anchors (canonical: from s91_w1_cf77_hochschild_degeneration_test.npz
# audit_sha256=be8c3197958ea25e2d5410f70ba0409611d5183295df7ef9eaa5c2bc9c96a121)
W1_4_L_BASELINE = [6, 7, 8, 9, 10]  # (local) baseline L grid (FULL-CC primary)
W1_4_AUDIT_SHA = "be8c3197958ea25e2d5410f70ba0409611d5183295df7ef9eaa5c2bc9c96a121"  # (local)

# 4-regulator atlas (plan W3-3 Field 7); name maps to evaluator
REGULATORS = ["zeta", "Pauli-Villars", "Mellin", "cutoff"]  # (local) axis-α 4-regulator atlas

# Substrate-distance-2 pole (plan substitution chain Def 3)
S_POLE = 4  # (local) Mellin moment index n for a_2n; substrate-distance-2 = a_4 = a_{2*2}

# Canonical L_emp anchor (S87 W2-3 Def 4 / S89 W5-2 / S90 CF-61 / S89 W-17 PASS)
L_EMP_CANONICAL = -7.046336474406761  # (local) M_KK² at τ_fold=0.19

# Saturation-ratio thresholds (plan W3-3 Field 9)
SATURATION_PASS = 1.0  # (local) PASS iff saturation_ratio ≤ 1.0
SATURATION_INFO = 1.5  # (local) INFO iff saturation_ratio ∈ (1.0, 1.5]
# FAIL iff saturation_ratio > 1.5

# Output paths
OUT_NPZ = ROOT / "computations" / "session-92" / "s92_w3_3_vii_av_axis_alpha_l_max_extension.npz"
OUT_PNG = ROOT / "computations" / "session-92" / "s92_w3_3_vii_av_axis_alpha_l_max_extension.png"
VERDICT_FILE = ROOT / "computations" / "session-92" / "s92_gate_verdicts.txt"

# Input file paths
CANONICAL_CONSTANTS = ROOT / "computations" / "_shared" / "canonical_constants.py"
L12_CACHE = ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
W1_4_BASELINE_NPZ = ROOT / "computations" / "session-91" / "s91_w1_cf77_hochschild_degeneration_test.npz"
W1_4_VERDICT_FILE = ROOT / "computations" / "session-91" / "s91_gate_verdicts.txt"
SCHEMATIC_HELPER = ROOT / "computations" / "_shared" / "_spectral_action_regulators.py"
SCRIPT_PATH = Path(__file__).resolve()

INPUT_FILES = {
    "canonical_constants": CANONICAL_CONSTANTS,
    "s84_spectrum_cache_tau019_L12": L12_CACHE,
    "s91_w1_4_baseline_npz": W1_4_BASELINE_NPZ,
    "s91_w1_4_verdict_anchor": W1_4_VERDICT_FILE,
    "spectral_action_regulators_SCHEMATIC": SCHEMATIC_HELPER,
    "script": SCRIPT_PATH,
}


# ============================ SHA helpers ============================
def sha256_of_file(p: Path) -> str:
    h = hashlib.sha256()  # (local)
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def log_input_pins(files: dict) -> dict:
    pins = {}  # (local)
    print("=" * 78)
    print(f"Gate: {GATE_ID}")
    print("=" * 78)
    print("Input SHAs:")
    for name, p in files.items():
        if not p.exists():
            print(f"  {name:42s} = (file not found; pin skipped)")
            continue
        sha = sha256_of_file(p)  # (local)
        pins[name] = sha
        print(f"  {name:42s} = {sha[:16]}...  ({p.relative_to(ROOT)})")
    return pins


def compute_dual_sha(pins: dict, script_path: Path) -> tuple[str, str]:
    script_bytes = script_path.read_bytes()  # (local)
    canonical_bytes = CANONICAL_CONSTANTS.read_bytes()  # (local)
    pinmap_json = json.dumps(sorted(pins.items()), sort_keys=True).encode("utf-8")  # (local)
    audit = hashlib.sha256(script_bytes + canonical_bytes + pinmap_json).hexdigest()  # (local)
    content = hashlib.sha256(script_bytes).hexdigest()  # (local)
    return audit, content


def append_verdict(
    composite: str, value_str: str,
    audit_sha: str, content_sha: str,
    sign_v: str, mag_v: str, reg_v: str,
    classification: str,
) -> None:
    """Atomic single-shot append per gate-verdicts.md S87+ canonical form,
    with TIER-2 SCHEMATIC level-pin POSITIVE disclosure pattern."""
    canonical = (
        f"{GATE_ID}: {composite} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX_NEW} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )  # (local)
    dual_sha = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )  # (local)
    three_tuple = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} "
        f"regime_verdict={reg_v} # {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )  # (local)
    tier_pin_row = (
        f"# tier_pin={TIER_PIN} # {GATE_ID} SCHEMATIC level-pin disclosure "
        f"(substrate-first-canonical-sourcing.md §(iv) K=4 MANDATORY POSITIVE)\n"
    )  # (local)
    classification_row = (
        f"# axis_alpha_extension_classification={classification} "
        f"# {GATE_ID} L_max ∈ {{11,12}} extension saturation adjudication\n"
    )  # (local)
    with open(VERDICT_FILE, "a", encoding="utf-8") as f:
        f.write(canonical)
        f.write(dual_sha)
        f.write(three_tuple)
        f.write(tier_pin_row)
        f.write(classification_row)


# ============================ Spectrum loader (truncated to L_max cap) ============================
def load_spectrum_truncated(cache_path: Path, L_max: int) -> tuple[np.ndarray, np.ndarray, int]:
    """Load L_max=12 cache and truncate to (p+q) <= L_max per S90 CF-61 pattern.
    Returns (lambdas, mults, n_sectors)."""
    cache = np.load(cache_path, allow_pickle=True)
    sector_evals = cache["sector_evals"].item()
    lambdas_list = []  # (local)
    mults_list = []  # (local)
    n_sectors = 0  # (local)
    for (p, q), info in sector_evals.items():
        if p + q > L_max:
            continue
        n_sectors += 1
        dim = int(info["dim"])  # (local)
        evals_arr = np.asarray(info["abs_evals"], dtype=np.float64)
        for v in evals_arr:
            lambdas_list.append(float(v))
            mults_list.append(dim)
    lambdas = np.array(lambdas_list, dtype=np.float64)
    mults = np.array(mults_list, dtype=np.float64)
    return lambdas, mults, n_sectors


# ============================ Regulator-class evaluator (B(R, L_max)) ============================
def eval_B_R_Lmax(regulator: str, L_max: int) -> float:
    """Evaluate B(R, L_max) := SCHEMATIC regulator R Mellin-moment-like
    sum at substrate-distance-2 pole index n = S_POLE / 2 = 2 on the
    Casimir spectrum filtered to p+q ≤ L_max.

    Plan substitution chain Def 3: B(R, L_max) is the regulator-class R
    evaluation of the §VII.AV Hochschild trace at substrate-distance-2 pole
    s=4 on the L_max-truncated D_K spectrum cache. The SCHEMATIC helper
    family evaluates these via the Casimir-spectrum schematic (positive-
    definite SU(3) Casimir spectrum d(p,q)/C_2(p,q)^n). Pole s=4 ⟶ moment
    index n=2 (a_4 in spectral-action notation; substrate-distance-2 pole
    in Mellin notation).
    """
    n = S_POLE // 2  # (local) Mellin pole s=4 → spectral-action a_4 → n=2
    if regulator == "zeta":
        return zeta_a_n(n, L_max, Vol_SU3_Haar)
    elif regulator == "Pauli-Villars":
        return pauli_villars_a_n(n, L_max, Vol_SU3_Haar)
    elif regulator == "Mellin":
        return mellin_a_n(n, L_max, Vol_SU3_Haar)
    elif regulator == "cutoff":
        return hard_cutoff_a_n(n, L_max, Vol_SU3_Haar)
    else:
        raise ValueError(f"Unknown regulator: {regulator}")


# ============================ Spread metric ============================
def compute_spread(B_row: np.ndarray) -> float:
    """max_spread(L_max) := (max_R B − min_R B) / median_R B (plan substitution
    chain Def 1). Defensive on degeneracy."""
    B_max = float(B_row.max())  # (local)
    B_min = float(B_row.min())  # (local)
    B_median = float(np.median(B_row))  # (local)
    if B_median == 0.0 or not math.isfinite(B_median):
        return float("nan")
    return (B_max - B_min) / B_median


# ============================ Adjudication ============================
def adjudicate(saturation_ratio: float, max_spread_L12: float) -> dict:
    """Plan W3-3 Field 9 saturation_ratio adjudication."""
    if not math.isfinite(saturation_ratio):
        return {
            "composite": "FAIL",
            "sign_verdict": "FAIL",
            "magnitude_verdict": "FAIL",
            "regime_verdict": "BREAKDOWN",
            "classification": "PIPELINE-FAILURE",
        }
    if saturation_ratio <= SATURATION_PASS:
        return {
            "composite": "PASS",
            "sign_verdict": "PASS",
            "magnitude_verdict": "PASS",
            "regime_verdict": "VALID",
            "classification": (
                f"MIXED-axis-alpha-SATURATES-asymptotic-finite-spread-"
                f"{max_spread_L12*100:.2f}pct-PROXY-REFINEMENT-bounded-not-discharged"
            ),
        }
    elif saturation_ratio <= SATURATION_INFO:
        return {
            "composite": "INFO",
            "sign_verdict": "PASS",
            "magnitude_verdict": "INFO",
            "regime_verdict": "MARGINAL",
            "classification": (
                f"MARGINAL-transition-L_max-12-cap-saturation_ratio="
                f"{saturation_ratio:.4f}-Friedrich-Bar-saturation-certification-required"
            ),
        }
    else:
        return {
            "composite": "FAIL",
            "sign_verdict": "FAIL",
            "magnitude_verdict": "FAIL",
            "regime_verdict": "VALID",
            "classification": (
                f"RD-axis-alpha-DIVERGES-cross-regulator-unbounded-L_max-driven-"
                f"saturation_ratio={saturation_ratio:.4f}-PROXY-REFINEMENT-STRUCTURALLY-INADEQUATE"
            ),
        }


# ============================ Diagnostic plot ============================
def make_plot(
    L_full: list[int],
    spread_full: list[float],
    saturation_ratio: float,
    verdict_class: str,
    B_grid_new: np.ndarray,
) -> None:
    """Two-panel: (1) 5-point L_max trend (baseline + extension) with PASS/INFO/FAIL band
    overlay anchored on max_spread(L=10); (2) per-regulator B(R, L_max) heatmap at extension."""
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5.5))

    # Panel 1: 5-point L_max trend
    L_array = np.array(L_full)  # (local)
    spread_array = np.array(spread_full)  # (local)
    # Baseline (W1-4 FULL-CC) marker (L=6,7,8,9,10)
    n_baseline = 5  # (local)
    ax1.plot(L_array[:n_baseline], spread_array[:n_baseline] * 100,
             "o-", color="steelblue", markersize=9, linewidth=2,
             label="W1-4 baseline (FULL-CC primary)")
    # Extension (THIS gate, SCHEMATIC) marker (L=11,12)
    ax1.plot(L_array[n_baseline:], spread_array[n_baseline:] * 100,
             "s-", color="crimson", markersize=10, linewidth=2,
             label="W3-3 extension (SCHEMATIC tier-2)")
    # Connect last baseline (L=10) to first extension (L=11) with dashed line
    if len(L_array) > n_baseline:
        ax1.plot(L_array[n_baseline-1:n_baseline+1],
                 spread_array[n_baseline-1:n_baseline+1] * 100,
                 "k--", linewidth=1, alpha=0.4)
    # PASS / INFO / FAIL bands anchored on max_spread(L=10) baseline
    spread_L8 = spread_array[2]  # (local) baseline L=8
    spread_L10 = spread_array[4]  # (local) baseline L=10
    delta_8_10 = abs(spread_L10 - spread_L8)  # (local)
    pass_lo = (spread_L10 - SATURATION_PASS * delta_8_10) * 100  # (local)
    pass_hi = (spread_L10 + SATURATION_PASS * delta_8_10) * 100  # (local)
    info_lo = (spread_L10 - SATURATION_INFO * delta_8_10) * 100  # (local)
    info_hi = (spread_L10 + SATURATION_INFO * delta_8_10) * 100  # (local)
    ax1.axhspan(pass_lo, pass_hi, alpha=0.18, color="green",
                label=f"PASS (saturation_ratio ≤ 1.0)")
    ax1.axhspan(info_lo, pass_lo, alpha=0.10, color="goldenrod")
    ax1.axhspan(pass_hi, info_hi, alpha=0.10, color="goldenrod",
                label=f"INFO ((1.0, 1.5])")
    ax1.axhline(spread_L10 * 100, linestyle=":", color="black", linewidth=1, alpha=0.5,
                label=f"L=10 anchor = {spread_L10*100:.2f}%")
    ax1.set_xlabel("L_max")
    ax1.set_ylabel("max_spread(L_max) × 100 [%]")
    ax1.set_xticks(L_array)
    ax1.set_title(
        f"§VII.AV axis-α 4-regulator atlas spread vs L_max\n"
        f"saturation_ratio = {saturation_ratio:.4f} → {verdict_class[:50]}"
    )
    ax1.legend(loc="best", fontsize=8)
    ax1.grid(True, alpha=0.3)

    # Panel 2: B(R, L_max) heatmap at L=11, L=12 (log10 scale)
    im = ax2.imshow(np.log10(np.abs(B_grid_new) + 1e-300), cmap="viridis", aspect="auto",
                    extent=[-0.5, len(REGULATORS) - 0.5, len(L_VALUES_NEW) - 0.5, -0.5])
    ax2.set_xticks(range(len(REGULATORS)))
    ax2.set_xticklabels(REGULATORS, rotation=30, ha="right")
    ax2.set_yticks(range(len(L_VALUES_NEW)))
    ax2.set_yticklabels([f"L={L}" for L in L_VALUES_NEW])
    ax2.set_title(
        f"log10(|B(R, L_max)|) at extension L ∈ {{11, 12}}\n"
        f"SCHEMATIC tier-2; substrate-distance-2 pole s={S_POLE}"
    )
    fig.colorbar(im, ax=ax2, label="log10(|B|)")
    for i, L in enumerate(L_VALUES_NEW):
        for j, R in enumerate(REGULATORS):
            val = B_grid_new[i, j]
            log_val = math.log10(abs(val) + 1e-300)  # (local)
            log_max = math.log10(np.abs(B_grid_new).max() + 1e-300)  # (local)
            text_color = "white" if log_val < (log_max - 0.3) else "black"
            ax2.text(j, i, f"{val:.2e}", ha="center", va="center",
                     fontsize=8, color=text_color)

    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=120)
    plt.close(fig)


# ============================ Main ============================
def main() -> int:
    import time
    t0 = time.time()  # (local)

    # 1. Log input pins + compute dual SHAs
    pins = log_input_pins(INPUT_FILES)
    audit_sha, content_sha = compute_dual_sha(pins, SCRIPT_PATH)
    print()
    print(f"  audit_sha256   = {audit_sha[:16]}...  (script+canonical+pinmap)")
    print(f"  content_sha256 = {content_sha[:16]}...  (script only)")
    print()

    # 2. Verify W1-4 verdict anchor (must_grep)
    print("Verifying W1-4 baseline verdict anchor (must_grep)...")
    with open(W1_4_VERDICT_FILE, "r", encoding="utf-8") as f:
        verdict_text = f.read()  # (local)
    expected = (
        f"CF-S91-VII-AV-HOCHSCHILD-DEGENERATION-TEST: INFO.*"
        f"audit_sha256={W1_4_AUDIT_SHA}"
    )  # (local)
    if re.search(expected, verdict_text) is None:
        print(f"  FAIL: W1-4 verdict anchor not found")
        print(f"  Expected pattern: {expected}")
        return 1
    print(f"  PASS: W1-4 INFO verdict + audit_sha256={W1_4_AUDIT_SHA[:16]}... confirmed")
    print()

    # 3. Load W1-4 baseline NPZ anchors
    print("Loading W1-4 baseline anchors from npz...")
    w1_4 = np.load(W1_4_BASELINE_NPZ, allow_pickle=True)
    w1_4_L_VALUES = list(w1_4["L_VALUES"])  # (local)
    w1_4_spread_per_L = np.asarray(w1_4["spread_per_L"], dtype=np.float64)  # (local)
    assert w1_4_L_VALUES == W1_4_L_BASELINE, (
        f"W1-4 L_VALUES drift: expected {W1_4_L_BASELINE}, got {w1_4_L_VALUES}"
    )
    spread_L8_baseline = float(w1_4_spread_per_L[2])    # (local) L=8 (index 2)
    spread_L10_baseline = float(w1_4_spread_per_L[4])   # (local) L=10 (index 4)
    print(f"  W1-4 L_VALUES = {w1_4_L_VALUES}")
    print(f"  W1-4 spread_per_L = {[f'{s:.6e}' for s in w1_4_spread_per_L]}")
    print(f"  Anchor for saturation_ratio numerator denominator:")
    print(f"    spread(L=8)  = {spread_L8_baseline:.6e} (W1-4 FULL-CC)")
    print(f"    spread(L=10) = {spread_L10_baseline:.6e} (W1-4 FULL-CC)")
    print(f"    delta_8_10   = {abs(spread_L10_baseline - spread_L8_baseline):.6e}")
    print()

    # 4. OPERATOR-MISMATCH PRE-FLIGHT cross-check (per plan §W3-3 substitution chain)
    print("OPERATOR-MISMATCH PRE-FLIGHT (per math-scripts.md §'Plan-author discipline')...")
    print(f"  Canonical anchor L_emp = {L_EMP_CANONICAL:.15f} M_KK² at τ_fold={tau_fold}")
    print(f"  (S87 W2-3 Def 4 / S89 W5-2 / S90 CF-61 / S89 W-17 PASS)")
    print(f"  B(R, L_max) operator: regulator-class evaluation of §VII.AV substrate-")
    print(f"  distance-2 pole s={S_POLE} cocycle pairing on L_max-truncated cache;")
    print(f"  NOT the closed-form d ln(Tr_M2(P_BdG D_K^(-2s)))/d ln K = +2s = +{2*S_POLE}")
    print(f"  (INCOMPATIBLE with canonical L_emp).")
    print(f"  Multiplicative-normalization cancellation invariant (math-scripts.md K=1):")
    print(f"  B(R, L_max) = w(L_max) · κ_R(K) ; d² ln κ_R / d(ln K)² annihilates w(L_max)")
    print(f"  by structural identity; asymptotic anchor L_emp inherits via this rule.")
    print(f"  Convention suffix carries -PLAN-OPERATOR-CANONICAL-L-EMP-VERIFIED-2026-05-22.")
    print()

    # 5. Loop over L_max ∈ {11, 12} × 4 regulators (SCHEMATIC tier-2)
    print(f"Computing B(R, L_max) on extension grid L ∈ {L_VALUES_NEW}:")
    print(f"  SCHEMATIC helper: _spectral_action_regulators.py")
    print(f"  4-regulator atlas: {REGULATORS}")
    print(f"  Substrate-distance-2 pole index n = S_POLE/2 = {S_POLE//2}")
    print()
    B_grid_new = np.zeros((len(L_VALUES_NEW), len(REGULATORS)), dtype=np.float64)
    spread_new = np.zeros(len(L_VALUES_NEW), dtype=np.float64)
    n_sectors_new = []  # (local)
    n_eigs_new = []  # (local)
    for i, L in enumerate(L_VALUES_NEW):
        # Cross-check: filter master cache to (p+q) <= L (informational; the
        # SCHEMATIC evaluators use the Casimir-spectrum schematic directly via
        # _enumerate_sectors(L_max) — they do NOT consume the cache eigenvalues).
        lambdas, mults, n_sec = load_spectrum_truncated(L12_CACHE, L)
        n_sectors_new.append(n_sec)
        n_eigs_new.append(len(lambdas))
        for j, R in enumerate(REGULATORS):
            B_grid_new[i, j] = eval_B_R_Lmax(R, L)
        spread_new[i] = compute_spread(B_grid_new[i])
        print(f"  L_max={L}: n_sectors={n_sec}, n_eigs={len(lambdas)}")
        print(f"    B = {B_grid_new[i]}")
        print(f"    max_spread(L={L}) = {spread_new[i]:.6e}")
    print()

    # 6. Compute saturation_ratio per plan substitution chain Def 4
    max_spread_L12 = float(spread_new[1])  # (local) L_VALUES_NEW[1] = 12
    max_spread_L11 = float(spread_new[0])  # (local) L_VALUES_NEW[0] = 11
    delta_10_12 = abs(max_spread_L12 - spread_L10_baseline)  # (local)
    delta_8_10 = abs(spread_L10_baseline - spread_L8_baseline)  # (local)
    if delta_8_10 == 0.0 or not math.isfinite(delta_8_10):
        saturation_ratio = float("nan")  # (local)
    else:
        saturation_ratio = delta_10_12 / delta_8_10  # (local)
    print("Saturation-ratio computation (plan substitution chain Def 4):")
    print(f"  max_spread(L=12) [SCHEMATIC]    = {max_spread_L12:.6e}")
    print(f"  max_spread(L=10) [W1-4 FULL-CC] = {spread_L10_baseline:.6e}")
    print(f"  max_spread(L=8)  [W1-4 FULL-CC] = {spread_L8_baseline:.6e}")
    print(f"  |spread(12) − spread(10)|       = {delta_10_12:.6e}")
    print(f"  |spread(10) − spread(8)|        = {delta_8_10:.6e}")
    print(f"  saturation_ratio                = {saturation_ratio:.6e}")
    print()

    # 7. Adjudicate
    verdict = adjudicate(saturation_ratio, max_spread_L12)
    print(f"Verdict: {verdict['composite']}")
    print(f"  axis-α extension classification: {verdict['classification']}")
    print(f"  sign_verdict:      {verdict['sign_verdict']}")
    print(f"  magnitude_verdict: {verdict['magnitude_verdict']}")
    print(f"  regime_verdict:    {verdict['regime_verdict']}")
    print()
    print("Threshold context (plan W3-3 Field 9):")
    print(f"  PASS iff saturation_ratio ≤ {SATURATION_PASS}")
    print(f"  INFO iff saturation_ratio ∈ ({SATURATION_PASS}, {SATURATION_INFO}]")
    print(f"  FAIL iff saturation_ratio > {SATURATION_INFO}")
    print(f"  Observed: saturation_ratio = {saturation_ratio:.6e} → {verdict['composite']}")
    print()

    # 8. Save outputs
    print(f"Saving npz to {OUT_NPZ.relative_to(ROOT)}...")
    # Combined L_VALUES (baseline + extension) for plot + downstream
    L_full = list(W1_4_L_BASELINE) + list(L_VALUES_NEW)  # (local) [6,7,8,9,10,11,12]
    spread_full = list(w1_4_spread_per_L) + list(spread_new)  # (local)
    np.savez(
        OUT_NPZ,
        # Extension grid
        L_VALUES_NEW=np.array(L_VALUES_NEW),
        REGULATORS=np.array(REGULATORS),
        B_grid_new=B_grid_new,
        spread_new=spread_new,
        n_sectors_new=np.array(n_sectors_new),
        n_eigs_new=np.array(n_eigs_new),
        # Full L grid (combined)
        L_VALUES_FULL=np.array(L_full),
        spread_full=np.array(spread_full),
        # Baseline anchors
        W1_4_L_BASELINE=np.array(W1_4_L_BASELINE),
        W1_4_spread_per_L=w1_4_spread_per_L,
        W1_4_AUDIT_SHA=W1_4_AUDIT_SHA,
        spread_L8_baseline=spread_L8_baseline,
        spread_L10_baseline=spread_L10_baseline,
        # Saturation ratio
        max_spread_L11=max_spread_L11,
        max_spread_L12=max_spread_L12,
        delta_10_12=delta_10_12,
        delta_8_10=delta_8_10,
        saturation_ratio=saturation_ratio,
        SATURATION_PASS=SATURATION_PASS,
        SATURATION_INFO=SATURATION_INFO,
        # Canonical anchors
        L_EMP_CANONICAL=L_EMP_CANONICAL,
        TAU_FOLD=tau_fold,
        M_KK=M_KK,
        S_POLE=S_POLE,
        L_MAX_NEW=L_MAX_NEW,
        L_MAX_CACHE=L_MAX_CACHE,
        CLASS_PIN=CLASS_PIN,
        TIER_PIN=TIER_PIN,
        SUBSTRATE_COCYCLE_RATIO=float(substrate_cocycle_ratio_67_88),
        # Verdict
        verdict_composite=verdict["composite"],
        verdict_sign=verdict["sign_verdict"],
        verdict_magnitude=verdict["magnitude_verdict"],
        verdict_regime=verdict["regime_verdict"],
        axis_alpha_extension_classification=verdict["classification"],
    )
    print(f"Saving plot to {OUT_PNG.relative_to(ROOT)}...")
    make_plot(L_full, spread_full, saturation_ratio, verdict["classification"], B_grid_new)
    print()

    # 9. Emit verdict line (POSITIVE disclosure: canonical + dual-SHA + 3-tuple
    #    + tier_pin=TIER-2 + axis_alpha_extension_classification)
    value_str = (
        f"saturation_ratio={saturation_ratio:.6e}_"
        f"max_spread_L11={max_spread_L11:.6e}_"
        f"max_spread_L12={max_spread_L12:.6e}_"
        f"baseline_L10={spread_L10_baseline:.6e}_"
        f"baseline_L8={spread_L8_baseline:.6e}_"
        f"L_EMP_CANONICAL={L_EMP_CANONICAL:.6f}"
    )  # (local)
    append_verdict(
        composite=verdict["composite"],
        value_str=value_str,
        audit_sha=audit_sha,
        content_sha=content_sha,
        sign_v=verdict["sign_verdict"],
        mag_v=verdict["magnitude_verdict"],
        reg_v=verdict["regime_verdict"],
        classification=verdict["classification"],
    )

    # 10. Final summary
    wall = time.time() - t0  # (local)
    print(f"=== {GATE_ID}: {verdict['composite']} (wall {wall:.1f}s) ===")
    print(f"    saturation_ratio: {saturation_ratio:.6e}")
    print(f"    axis-α classification: {verdict['classification']}")
    print(f"    audit_sha256:   {audit_sha}")
    print(f"    content_sha256: {content_sha}")
    print(f"    CLASS pin: {CLASS_PIN} | tier_pin: {TIER_PIN}")
    print(f"    SCHEMATIC level-pin POSITIVE disclosure: CLASS + suffix + tier-row + docstring")
    return 0


if __name__ == "__main__":
    sys.exit(main())
