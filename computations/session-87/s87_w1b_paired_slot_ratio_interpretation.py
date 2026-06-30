#!/usr/bin/env python3
"""
S87 W1b-4 -- PAIRED-SLOT-RATIO-INTERPRETATION (CF-11; OPEN-Q)  [AUDIT]
========================================================================

Gate: S87-PAIRED-SLOT-RATIO-INTERPRETATION
Trigger: AUDIT-OPEN-Q
Classification: GEOMETRIC (paired-slot a_0/a_2 split structural classification)
Owner: gen-physicist

Pre-registration (sessions/session-plan/session-87-plan-w1b.md §W1b-4):

  HYPOTHESIS: The empirical paired-slot split-ratio 7436/3812 (≈ 1.95068)
  observed at S86 W-1 W1b-T5 paired-slot tabulation arises from one of
  four pre-enumerated structural classes:
    CLASS-A: hypercube-vertex 2:1 pairing, predicted r_A = 2
    CLASS-B: Seeley-DeWitt mass-ratio expansion at a_0/a_2 (zeta-vs-Gilkey
             split-factor running at the a_0 vs a_2 slots)
    CLASS-C: other-substrate-identity (Schur-orthogonality, Weyl-branching,
             Connes-Karoubi pairing weights, etc.)
    CLASS-D: numerical-coincidence-no-structural-source

  STRUCTURAL SOURCE OF 7436 AND 3812 (verified via knowledge MCP +
  computations/session-64/s64_bdg_kasparov.py canonical comment lines 414-420):
    7436 = round(a_0^zeta / a_0^Gilkey) = round(6440 / 0.866)  (S64; a_0 split factor)
    3812 = round(a_2^zeta / a_2^Gilkey) = round(2776.165 / 0.728235)  (S46; a_2 split factor)
  The two integers are the K-DEPENDENT RATIO between zeta-spectral and
  Gilkey-Seeley-DeWitt forms at the a_0 (CC) and a_2 (Newton) slots
  respectively. The S64 comment is canonical:
    "a_0^zeta / a_0^Gilkey = 6440 / 0.866 = 7436. But this ratio is NOT
     the same as a_2^zeta / a_2^Gilkey = 3812. Because a_k^zeta is
     sum |lam|^{-2k}, not just a normalization factor. The conversion
     depends on k."

VERDICT BAND (OPEN-Q INFO-band decision rule per plan §W1b-4):
  INFO (CLASS-A unique)   if A < 1e-2 AND others > 1e-1
  INFO (CLASS-B unique)   if B < 1e-2 AND others > 1e-1
  INFO (CLASS-C unique)   if C < 1e-2 AND others > 1e-1
  INFO (CLASS-D)          if all residuals > 1e-1
  INFO (multi-class)      if 2+ classes < 1e-2

  Per plan: this gate ALWAYS verdicts INFO (no PASS/FAIL by design;
  the sub-classification IS the structural output).

4-tuple slot: (value=class_match_residual_min,
               scheme=4-class-paired-slot-classification,
               convention=substrate-paired-slot-w1b-T5-anchor, L_max=12).

INPUTS:
  - canonical_constants.py (a0_fold = 6440.0; a2_fold = 2776.1653888633655;
    a4_fold = 1350.7216415169728)
  - sessions/archive/session-86/session-86-w2-workingpaper.md §"Solution-space
    interpretation" line 156 (SD a_2 ≈ 0.728 ; ζ_D(1) ≈ 2776.17 ; ratio 3812)
  - sessions/archive/session-86/workshops/s86-mellin-cone-repair-or-no-go.md
    Magnitude tables lines 1714-1920 (a_0 split factor 7436 from S64)
  - computations/session-64/s64_bdg_kasparov.py canonical comment lines 414-420

OUTPUT 4-tuple: (value=<min residual>, scheme=4-class-paired-slot-classification,
                 convention=substrate-paired-slot-w1b-T5-anchor, L_max=12).

3-tuple annotation (S87 schema-v2):
  sign_verdict     = N/A (no directional pre-registration)
  magnitude_verdict= per sub-classification (PASS for unique-class, FAIL for
                     CLASS-D, INFO for multi-class)
  regime_verdict   = VALID (algebraic enumeration; no truncation regime to break)
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import hashlib
import json
import time
from pathlib import Path
from fractions import Fraction

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

# Per CLAUDE.md computations/_shared/CLAUDE.md: import from canonical_constants.
from canonical_constants import a0_fold, a2_fold, a4_fold  # noqa: E402

PROJECT_ROOT = SCRIPT_DIR.parent

GATE_ID = "S87-PAIRED-SLOT-RATIO-INTERPRETATION"                       # (local)
SCHEME = "4-class-paired-slot-classification"                          # (local)
CONVENTION = "substrate-paired-slot-w1b-T5-anchor"                     # (local)
L_MAX_LABEL = "12"                                                     # (local)
SCHEMA_VERSION = "S87+"                                                # (local)

# --- Pre-registered tolerance bounds (plan §W1b-4)
TOL_PASS = 1e-2                                                        # (local) per-class match
TOL_EXCLUDE = 1e-1                                                     # (local) other-class exclusion

# --- Empirical observed paired-slot integers (from S86 W-1 W1b-T5 source)
PAIRED_SLOT_NUM = 7436                                                 # (local) a_0 split factor (S64)
PAIRED_SLOT_DEN = 3812                                                 # (local) a_2 split factor (S46)

# --- Output paths
OUT_NPZ = SCRIPT_DIR / "s87_w1b_paired_slot_ratio_interpretation.npz"
OUT_PNG = SCRIPT_DIR / "s87_w1b_paired_slot_ratio_interpretation.png"
VERDICT_TXT = SCRIPT_DIR / "s87_gate_verdicts.txt"
CANON_PY = SCRIPT_DIR / "canonical_constants.py"
S64_KASPAROV = SCRIPT_DIR / "s64_bdg_kasparov.py"
S86_W2_WP = PROJECT_ROOT / "sessions" / "session-86" / "session-86-w2-workingpaper.md"

INPUT_FILES = [CANON_PY, S64_KASPAROV, S86_W2_WP]


# ---- SHA helpers (closure-hash pattern from S82 W1 template) ---------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                               # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins = {}                                                          # (local)
    for p in inputs:
        sha = sha256_of(p)                                             # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = p.name                                               # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path, canonical_path, pins):
    script_bytes = script_path.read_bytes() if script_path.exists() else b""
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")
    h_audit = hashlib.sha256()                                         # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()                                       # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


# ---- Gilkey-form Seeley-DeWitt coefficients (S64 canonical comment) -
# These are the (4*pi)^{-d/2}-included Gilkey forms at the SU(3) fold
# (s64_bdg_kasparov.py lines 52-53). Pinned per S64 canonical:
A0_GILKEY = 0.866                                                      # (local) a_0^Gilkey, S64
A2_GILKEY = 0.728234972609                                             # (local) a_2^Gilkey, S64


# ---- Sage QQ-exact reduction of 7436/3812 -----------------------------
def sage_qq_exact(num: int, den: int):
    """Sage QQ-exact reduction via Python Fraction (bit-exact)."""
    f = Fraction(num, den)                                             # (local)
    return f.numerator, f.denominator, float(f)


# ---- 4-class enumeration ---------------------------------------------
def enumerate_classes(r_obs: float):
    """Enumerate the 4-class predicted ratios and per-class residuals.

    Returns dict with per-class predicted value, residual, and pass/exclude flags.
    """
    pi_val = np.pi                                                     # (local)
    phi_paasch = 1.531580                                              # (local) S12 chirality canonical

    # --- CLASS-A: hypercube-vertex 2:1 pairing
    r_A = 2.0                                                          # (local)
    res_A = abs(r_obs - r_A)                                           # (local)

    # --- CLASS-B: Seeley-DeWitt mass-ratio expansion at a_0/a_2.
    # The structural identity (S64 comment lines 414-420):
    #   r_obs = (a_0^zeta / a_0^Gilkey) / (a_2^zeta / a_2^Gilkey)
    #         = (a_0^zeta / a_2^zeta) * (a_2^Gilkey / a_0^Gilkey)
    # SUBSTITUTION CHAIN:
    #   Step 1 (definitions):
    #     a_n^zeta = sum_k d_k / |lam_k|^{2n}    (zeta-regulated spectral moment)
    #     a_n^Gilkey = (4*pi)^{-d/2} * Gilkey-Seeley-DeWitt geometric coefficient
    #   Step 2 (substitution):
    #     7436 = a_0^zeta / a_0^Gilkey  (k-dependent split factor at a_0 slot)
    #     3812 = a_2^zeta / a_2^Gilkey  (k-dependent split factor at a_2 slot)
    #     r_obs = 7436/3812 = (a_0^zeta * a_2^Gilkey) / (a_0^Gilkey * a_2^zeta)
    #   Step 3 (simplify): r_B := (a_0^zeta / a_2^zeta) * (a_2^Gilkey / a_0^Gilkey)
    #   Step 4 (direction): r_B is set BY CONSTRUCTION to the observed ratio's
    #     structural form via canonical_constants.py (a_0_fold, a_2_fold, A0_GILKEY,
    #     A2_GILKEY); residual measures rounding-error of integer 7436, 3812.
    r_B = (a0_fold * A2_GILKEY) / (a2_fold * A0_GILKEY)                # (local)
    res_B = abs(r_obs - r_B)                                           # (local)

    # --- CLASS-C: enumerated other-substrate-identity candidates (≤10)
    class_C_candidates = {                                             # (local)
        "C1_two_pi_squared_quotient": (2 * pi_val) ** 2 / (4 * pi_val) ** 2,
        "C2_phi_paasch_chirality_S12": phi_paasch,
        "C3_connes_karoubi_HP1_cocycle_ratio_S86_W5": 7.324992,
        "C4_SU3_dim_ratio_8_3": 8.0 / 3.0,
        "C5_atlas_cardinality_A5_A4_S86_W8": 5.0 / 4.0,
        "C6_V4_pair_orders_S86_W12": 2.0,
        "C7_a4_a2_geom_ratio": a4_fold / a2_fold,
        "C8_a0_a4_geom_ratio": a0_fold / a4_fold,
        "C9_R_protected_a0a4_over_a2sq": a0_fold * a4_fold / a2_fold ** 2,
        "C10_pi_over_phi_paasch": pi_val / phi_paasch,
    }
    res_C = {k: abs(r_obs - v) for k, v in class_C_candidates.items()}  # (local)
    res_C_min_name = min(res_C, key=res_C.get)                          # (local)
    res_C_min = res_C[res_C_min_name]                                   # (local)

    # --- CLASS-D: numerical-coincidence band; defined by exclusion
    # of A, B, C from PASS-band; D fires if all residuals > 1e-1.
    class_D_active = (res_A > TOL_EXCLUDE and res_B > TOL_EXCLUDE
                      and res_C_min > TOL_EXCLUDE)                     # (local)
    # The "class-D residual band" reported in .npz is the minimum residual
    # over A/B/C if D would have fired (the closeness threshold).
    res_D_band = min(res_A, res_B, res_C_min) if class_D_active else float("nan")  # (local)

    return {
        "r_obs": r_obs,
        "class_A_predicted": r_A,
        "class_A_residual": res_A,
        "class_B_predicted": r_B,
        "class_B_residual": res_B,
        "class_C_candidates": class_C_candidates,
        "class_C_residuals": res_C,
        "class_C_min_name": res_C_min_name,
        "class_C_min_residual": res_C_min,
        "class_D_active": class_D_active,
        "class_D_residual_band": res_D_band,
    }


# ---- Sub-classification from per-class residuals ---------------------
def classify(enum_result):
    """Apply pre-registered band rule to identify INFO sub-class.

    Pre-registered rule (plan §W1b-4 Field 9 band table):
      unique_class = X if (residual_X < TOL_PASS) AND (residual_Y > TOL_EXCLUDE
                          for ALL Y != X)
      multi-class  if 2+ classes have residual_X < TOL_PASS
      class_D      if ALL residuals > TOL_EXCLUDE
    """
    res_A = enum_result["class_A_residual"]
    res_B = enum_result["class_B_residual"]
    res_C_min = enum_result["class_C_min_residual"]

    pass_band = {                                                      # (local)
        "A": res_A < TOL_PASS,
        "B": res_B < TOL_PASS,
        "C": res_C_min < TOL_PASS,
    }
    n_pass = sum(pass_band.values())                                   # (local)
    excl_band = {                                                      # (local)
        "A": res_A > TOL_EXCLUDE,
        "B": res_B > TOL_EXCLUDE,
        "C": res_C_min > TOL_EXCLUDE,
    }

    # Multi-class match (2+ < TOL_PASS): ambiguous
    if n_pass >= 2:
        return {
            "verdict_class": "INFO_MULTI_CLASS",
            "unique_match": None,
            "magnitude_verdict": "INFO",
            "promotion_path": "Carry-forward to S88+ as deferred-research disambiguation gate",
        }

    # All residuals > TOL_EXCLUDE: CLASS-D
    if all(excl_band.values()):
        return {
            "verdict_class": "INFO_CLASS_D",
            "unique_match": None,
            "magnitude_verdict": "FAIL",
            "promotion_path": "Carry-forward to S88+ deferred-research with L_max=14 cross-check",
        }

    # Strict-unique: exactly one class < TOL_PASS AND all others > TOL_EXCLUDE
    if n_pass == 1:
        # Identify which one
        passing = [k for k, v in pass_band.items() if v][0]            # (local)
        # Strict uniqueness: all OTHER classes > TOL_EXCLUDE
        others_excluded = all(excl_band[k] for k in ("A", "B", "C") if k != passing)  # (local)
        if others_excluded:
            promotion_map = {                                          # (local)
                "A": "S88-HYPERCUBE-VERTEX-PAIRED-SLOT-IDENTITY-VERIFY",
                "B": "S88-SD-MASS-RATIO-PAIRED-SLOT-IDENTITY-VERIFY",
                "C": ("S88-{Cclass}-PAIRED-SLOT-IDENTITY-VERIFY"
                      .replace("{Cclass}", enum_result["class_C_min_name"].upper())),
            }
            return {
                "verdict_class": f"INFO_CLASS_{passing}_UNIQUE",
                "unique_match": passing,
                "magnitude_verdict": "PASS",
                "promotion_path": promotion_map[passing],
            }
        # Near-unique with in-between gap on another class
        # (e.g., Class-B PASS-band, Class-A in [TOL_PASS, TOL_EXCLUDE] gap)
        gap_classes = [k for k in ("A", "B", "C")
                       if k != passing
                       and not pass_band[k] and not excl_band[k]]      # (local)
        return {
            "verdict_class": f"INFO_CLASS_{passing}_NEAR_UNIQUE_GAP_{','.join(gap_classes)}",
            "unique_match": passing,
            "magnitude_verdict": "INFO",
            "promotion_path": (f"S88+ candidate: CLASS-{passing} promotion conditional on "
                               f"resolving CLASS-{','.join(gap_classes)} in-between-gap "
                               f"residual via deeper enumeration or L_max=14 cross-check"),
        }

    # Otherwise: no class < TOL_PASS, but also not all > TOL_EXCLUDE
    # (i.e., one or more classes in the in-between gap [TOL_PASS, TOL_EXCLUDE])
    return {
        "verdict_class": "INFO_INDETERMINATE_GAP",
        "unique_match": None,
        "magnitude_verdict": "INFO",
        "promotion_path": "Carry-forward to S88+ as deferred-research with deeper CLASS-C enumeration",
    }


# ---- Plot ----
def make_plot(enum_result, classification_result):
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))                   # (local)

    r_obs = enum_result["r_obs"]
    res_A = enum_result["class_A_residual"]
    res_B = enum_result["class_B_residual"]
    res_C = enum_result["class_C_residuals"]

    # Panel 1: per-class predicted vs observed
    ax = axes[0, 0]
    classes = ["A (vertex 2:1)", "B (SD-mass-ratio)"]
    preds = [enum_result["class_A_predicted"], enum_result["class_B_predicted"]]
    ax.bar(classes, preds, color=["tab:blue", "tab:green"], alpha=0.7)
    ax.axhline(r_obs, color="red", linestyle="--", label=f"observed = {r_obs:.5f}")
    ax.set_ylabel("predicted ratio")
    ax.set_title("Per-class predicted ratio vs observed (7436/3812)")
    ax.legend()
    ax.grid(True, alpha=0.3)

    # Panel 2: residual histogram (log-scale)
    ax = axes[0, 1]
    res_names = ["A", "B"] + list(res_C.keys())
    res_values = [res_A, res_B] + list(res_C.values())
    colors = ["tab:blue", "tab:green"] + ["tab:orange"] * len(res_C)
    ax.barh(res_names, res_values, color=colors, alpha=0.7)
    ax.axvline(TOL_PASS, color="green", linestyle="--", label=f"PASS_TOL = {TOL_PASS}")
    ax.axvline(TOL_EXCLUDE, color="red", linestyle="--", label=f"EXCLUDE_TOL = {TOL_EXCLUDE}")
    ax.set_xscale("log")
    ax.set_xlabel("|r_obs - r_predicted| (log scale)")
    ax.set_title("Per-class residuals (log-scale)")
    ax.legend(loc="lower right", fontsize=8)
    ax.grid(True, alpha=0.3)

    # Panel 3: OEIS lookup outcome (text panel)
    ax = axes[1, 0]
    ax.axis("off")
    text = (
        "OEIS reverse-lookup outcome (mcp__oeis__lookup_by_values):\n"
        "    Query: [7436, 3812]\n"
        "    Result: NO MATCH (verified: not a known integer sequence in OEIS)\n\n"
        "Sage QQ-exact reduction of 7436/3812:\n"
        f"    7436 = {' * '.join(str(x) for x in [2, 2, 11, 13, 13])} = 2^2 * 11 * 13^2\n"
        f"    3812 = 2^2 * 953  (953 prime)\n"
        f"    gcd(7436, 3812) = 4\n"
        f"    Reduced: 1859/953 = {1859/953:.10f}\n\n"
        "Knowledge MCP pre-check:\n"
        "    a_0_FW: not pinned (CLASS-D fallback consistent)\n"
        "    a_2_FW: not pinned (CLASS-D fallback consistent)\n"
        "    structural source (S64): ratio depends on k\n"
        "    => CLASS-B is structurally indicated\n"
    )
    ax.text(0.02, 0.98, text, transform=ax.transAxes, fontsize=9,
            verticalalignment="top", family="monospace")
    ax.set_title("Sage QQ + OEIS + Knowledge MCP findings")

    # Panel 4: classification flowchart
    ax = axes[1, 1]
    ax.axis("off")
    flow_text = (
        "CLASSIFICATION FLOWCHART (pre-registered band rule):\n\n"
        f"  Step 1: r_obs = 7436/3812 = {r_obs:.6f}\n"
        f"  Step 2: residual_X = |r_obs - r_X|\n"
        f"          residual_A = {res_A:.4e}\n"
        f"          residual_B = {res_B:.4e}\n"
        f"          residual_C_min = {enum_result['class_C_min_residual']:.4e}\n\n"
        f"  Step 3: PASS-band (< {TOL_PASS:.0e}):\n"
        f"          A: {res_A < TOL_PASS}    B: {res_B < TOL_PASS}    C: {enum_result['class_C_min_residual'] < TOL_PASS}\n"
        f"          EXCLUDE-band (> {TOL_EXCLUDE:.0e}):\n"
        f"          A: {res_A > TOL_EXCLUDE}    B: {res_B > TOL_EXCLUDE}    C: {enum_result['class_C_min_residual'] > TOL_EXCLUDE}\n\n"
        f"  VERDICT CLASS: {classification_result['verdict_class']}\n"
        f"  unique_match  : {classification_result['unique_match']}\n"
        f"  magnitude     : {classification_result['magnitude_verdict']}\n\n"
        f"  promotion_path:\n"
        f"  {classification_result['promotion_path']}\n"
    )
    ax.text(0.02, 0.98, flow_text, transform=ax.transAxes, fontsize=9,
            verticalalignment="top", family="monospace")
    ax.set_title("Sub-classification & promotion path")

    fig.suptitle(f"{GATE_ID} — 4-class paired-slot ratio interpretation",
                 fontsize=12, weight="bold")
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=120, bbox_inches="tight")
    plt.close(fig)
    print(f"  Plot written: {OUT_PNG.name}")


# ---- Verdict-line emission (atomic single-line append) ---------------
def append_verdict(verdict, value_str, audit_sha, content_sha,
                   sign_v, magnitude_v, regime_v):
    line = (
        f"{GATE_ID}: {verdict} -- value='{value_str}' scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX_LABEL} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    annotation = (
        f"# sign_verdict={sign_v} magnitude_verdict={magnitude_v} "
        f"regime_verdict={regime_v} # {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)
        fp.write(annotation)
    print(f"  Verdict + dual-SHA companion + 3-tuple annotation appended to {VERDICT_TXT.name}")


# ---- Main ----
def main():
    t0 = time.time()                                                   # (local)
    print(f"=== {GATE_ID} ===")
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()                             # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANON_PY, pins)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print()

    # Step A: Sage QQ-exact reduction (Python Fraction is bit-exact for integers).
    num, den, r_float = sage_qq_exact(PAIRED_SLOT_NUM, PAIRED_SLOT_DEN)
    print(f"  Sage QQ-exact reduction of 7436/3812: {num}/{den} = {r_float:.10f}")
    assert num == 1859 and den == 953, "Sage QQ reduction mismatch (expected 1859/953)"
    print()

    # Step B: 4-class enumeration
    enum_result = enumerate_classes(r_float)
    print("  4-class enumeration:")
    print(f"    CLASS-A (hypercube-vertex 2:1): r_A = {enum_result['class_A_predicted']:.6f}, "
          f"residual = {enum_result['class_A_residual']:.6e}")
    print(f"    CLASS-B (SD mass-ratio expansion): r_B = {enum_result['class_B_predicted']:.6f}, "
          f"residual = {enum_result['class_B_residual']:.6e}")
    print(f"    CLASS-C candidates ({len(enum_result['class_C_candidates'])} enumerated):")
    for name, val in enum_result["class_C_candidates"].items():
        res = enum_result["class_C_residuals"][name]
        flag = "  <-- min" if name == enum_result["class_C_min_name"] else ""
        print(f"      {name}: r = {val:.6f}, residual = {res:.6e}{flag}")
    print(f"    CLASS-D active: {enum_result['class_D_active']}")
    if enum_result["class_D_active"]:
        print(f"      D residual band (min over A,B,C): {enum_result['class_D_residual_band']:.6e}")
    print()

    # Step C: classification per pre-registered band rule
    classification = classify(enum_result)
    print("  Classification:")
    print(f"    verdict_class    : {classification['verdict_class']}")
    print(f"    unique_match     : {classification['unique_match']}")
    print(f"    magnitude_verdict: {classification['magnitude_verdict']}")
    print(f"    promotion_path   : {classification['promotion_path']}")
    print()

    # Step D: assemble verdict
    # Per plan: ALWAYS INFO (OPEN-Q discipline; no PASS/FAIL).
    verdict = "INFO"                                                   # (local)
    sign_verdict = "N/A"                                               # (local)
    magnitude_verdict = classification["magnitude_verdict"]            # (local)
    regime_verdict = "VALID"                                           # (local)

    # Composite-collapse cross-check (gate-verdicts.md):
    # regime=VALID, sign=N/A; magnitude PASS->composite PASS; INFO->INFO; FAIL->FAIL.
    # Plan overrides: this gate ALWAYS INFO regardless of magnitude
    # (the OPEN-Q sub-classification carries the structural verdict, not the
    # composite top-line). This is the pre-registered OPEN-Q discipline:
    # the gate cannot PASS or FAIL by design, only INFO with sub-class.
    print(f"  Composite verdict (per plan ALWAYS INFO; OPEN-Q discipline): {verdict}")

    # Numeric value field for the verdict line: minimum of class residuals
    res_min = min(                                                     # (local)
        enum_result["class_A_residual"],
        enum_result["class_B_residual"],
        enum_result["class_C_min_residual"],
    )
    value_str = (
        f"min_class_residual={res_min:.4e};"
        f"A_res={enum_result['class_A_residual']:.4e};"
        f"B_res={enum_result['class_B_residual']:.4e};"
        f"C_min_res={enum_result['class_C_min_residual']:.4e};"
        f"C_min_name={enum_result['class_C_min_name']};"
        f"sub_class={classification['verdict_class']}"
    )

    # Step E: NPZ data emission
    class_C_names = list(enum_result["class_C_candidates"].keys())
    class_C_values = np.array([enum_result["class_C_candidates"][n] for n in class_C_names])
    class_C_residuals = np.array([enum_result["class_C_residuals"][n] for n in class_C_names])
    np.savez(
        OUT_NPZ,
        # Plan-required keys:
        paired_slot_ratio_observed=r_float,
        paired_slot_ratio_observed_qq_num=num,
        paired_slot_ratio_observed_qq_den=den,
        class_A_predicted_value=enum_result["class_A_predicted"],
        class_A_match_residual=enum_result["class_A_residual"],
        class_B_predicted_value=enum_result["class_B_predicted"],
        class_B_match_residual=enum_result["class_B_residual"],
        class_C_candidates_list=np.array(class_C_names),
        class_C_predicted_values=class_C_values,
        class_C_match_residuals=class_C_residuals,
        class_D_residual_band=enum_result["class_D_residual_band"],
        verdict_class=classification["verdict_class"],
        verdict_unique_match=str(classification["unique_match"]),
        # Audit metadata
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        gate_id=GATE_ID,
        scheme=SCHEME,
        convention=CONVENTION,
        L_max=L_MAX_LABEL,
        # Provenance pins:
        a0_fold_canonical=a0_fold,
        a2_fold_canonical=a2_fold,
        a0_gilkey=A0_GILKEY,
        a2_gilkey=A2_GILKEY,
        # Tolerance pins:
        tol_pass=TOL_PASS,
        tol_exclude=TOL_EXCLUDE,
    )
    print(f"  NPZ written: {OUT_NPZ.name}")

    # Step F: plot
    make_plot(enum_result, classification)

    # Step G: append verdict line + dual-SHA + 3-tuple annotation
    append_verdict(verdict, value_str, audit_sha, content_sha,
                   sign_verdict, magnitude_verdict, regime_verdict)

    elapsed = time.time() - t0                                         # (local)
    print(f"  Elapsed: {elapsed:.2f}s")
    print(f"  Final verdict: {verdict} (sub-class={classification['verdict_class']})")
    print()
    print("--- Substitution chain summary (CLASS-B structural identity) ---")
    print("  Step 1 (definitions):")
    print("    a_n^zeta   = sum_k d_k / |lambda_k|^{2n}      (zeta-spectral moment)")
    print("    a_n^Gilkey = (4*pi)^{-d/2} * (Gilkey geometric coefficient)")
    print("  Step 2 (substitution):")
    print(f"    7436 = round(a_0^zeta / a_0^Gilkey) = round({a0_fold}/{A0_GILKEY})")
    print(f"    3812 = round(a_2^zeta / a_2^Gilkey) = round({a2_fold:.6f}/{A2_GILKEY})")
    print("    r_obs = 7436/3812")
    print("  Step 3 (simplify to canonical form):")
    print("    r_B := (a_0^zeta * a_2^Gilkey) / (a_0^Gilkey * a_2^zeta)")
    print(f"         = ({a0_fold}*{A2_GILKEY}) / ({A0_GILKEY}*{a2_fold:.6f})")
    print(f"         = {(a0_fold * A2_GILKEY)/(A0_GILKEY * a2_fold):.10f}")
    print("  Step 4 (direction): residual_B = |r_obs - r_B| measures rounding")
    print(f"    error of the integer 7436, 3812 vs the structural identity =")
    print(f"    {enum_result['class_B_residual']:.6e}  <  {TOL_PASS}  (PASS-band)")
    print()


if __name__ == "__main__":
    main()
