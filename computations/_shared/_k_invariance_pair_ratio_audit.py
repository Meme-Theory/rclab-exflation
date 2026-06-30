"""
_k_invariance_pair_ratio_audit.py

K-invariance pair-ratio verification audit (T4-14, S86 W-9 AUDIT-1).

Purpose
-------
Python reproduction of the K-invariance pair-ratio metric

    pair_ratio(F_2, R) = |M_F2 - M_R| / M_F2

across the A_5 5-tuple of Mellin multipliers at the substrate-distance-1
pole (s=3), at the W4-2 P5 multiplier precision. Verifies that the
registered margin claims (924x suppression / 298x truncation / 798x
subtraction over PASS_thresh = 1e-3; corresponding 92.4x / 29.8x / 79.9x
over FAIL_thresh = 1e-2) reproduce to 4 sig figs.

The script is READY-TO-INSTALL; all numerical inputs are pinned in
W-9 CANON-1 (Mellin 5-tuple at s=3) and CANON-7 (pair-ratio margins).

Source
------
S86 W-9 §T-CR3.1 (Python verification, lines 2035-2090).
S86 W-9 CANON-1 (Mellin multiplier 5-tuple at s=3).
S86 W-9 CANON-7 (pair-ratio quantitative margins for clause (e)).

Provenance
----------
S86 W0c-7 housekeeping queue Tier-4 row T4-14.
Promoted from S86 W-9 AUDIT-1 (lizzi+transit, 2026-04-26).

Usage
-----
    python _k_invariance_pair_ratio_audit.py             # report mode
    python _k_invariance_pair_ratio_audit.py --json      # machine-readable
    python _k_invariance_pair_ratio_audit.py --strict    # nonzero exit on any mismatch >4 sig figs
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

# Project canonical constants (mandatory per .claude/rules/math-scripts.md S34+).
sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import *  # noqa: F401,F403


# ---------------------------------------------------------------------------
# Pinned Mellin multipliers at s=3 (W-9 CANON-1; W4-2 P5 inheritance)
# ---------------------------------------------------------------------------

MELLIN_MULTIPLIERS_S3 = {                               # (local) — W-9 CANON-1
    "zeta":         1.581e-1,                           # (local)
    "SDW":          1.581e-1,                           # (local) (= M_zeta at s=3)
    "Zubarev":      1.201e-2,                           # (local)
    "cutoff_sqrt":  1.110e-1,                           # (local)
    "anomaly":      3.185e-2,                           # (local)
}

# F_2 = {zeta, SDW} disambiguated from W14-plan F_4 = {zeta, Zubarev, SDW}.
F_2_CLASS = ("zeta", "SDW")                              # (local)

# Pre-registered K-invariance thresholds (W-9 CANON-2;
# `s86_w4_p5_sector_2_k_invariant.py` line 9).
PASS_THRESH = 1e-3                                       # (local)
FAIL_THRESH = 1e-2                                       # (local)

# Expected pair-ratio values (W-9 CANON-7; §T-CR3.1 lines 2050-2063).
EXPECTED_PAIR_RATIOS = {                                 # (local)
    "F_2_vs_suppression":  9.2404e-01,
    "F_2_vs_truncation":   2.9791e-01,
    "F_2_vs_subtraction":  7.9854e-01,
}

# Class-vs-class mapping (W-9 §T-CR3.1):
# - suppression  ↔ Zubarev (M smallest)
# - truncation   ↔ cutoff_sqrt
# - subtraction  ↔ anomaly
CLASS_PARTNER = {                                        # (local)
    "suppression":  "Zubarev",
    "truncation":   "cutoff_sqrt",
    "subtraction":  "anomaly",
}

# Expected margin multiplets (W-9 CANON-7).
EXPECTED_MARGINS = {                                     # (local)
    "suppression":  {"over_PASS": 924.0,  "over_FAIL": 92.4, "OOM_safety": 2.97},
    "truncation":   {"over_PASS": 298.0,  "over_FAIL": 29.8, "OOM_safety": 2.47},
    "subtraction":  {"over_PASS": 798.0,  "over_FAIL": 79.9, "OOM_safety": 2.90},
}

# 4-sig-fig comparison tolerance (rel_tol).
SIG_FIG_REL_TOL = 5e-4                                   # (local) — half-ulp at 4 sig figs


# ---------------------------------------------------------------------------
# Core audit logic
# ---------------------------------------------------------------------------

def pair_ratio(M_F2: float, M_R: float) -> float:
    """K-invariance pair-ratio.

    pair_ratio(F_2, R) = |M_F2 − M_R| / M_F2
    """
    return abs(M_F2 - M_R) / M_F2                        # (local)


def f2_aggregate_multiplier() -> float:
    """F_2-class aggregate Mellin multiplier (geometric mean for ratio)."""
    # F_2 = {zeta, SDW}; both equal at s=3 → aggregate = M_zeta = M_SDW.
    m_zeta = MELLIN_MULTIPLIERS_S3["zeta"]               # (local)
    m_sdw  = MELLIN_MULTIPLIERS_S3["SDW"]                # (local)
    if abs(m_zeta - m_sdw) > SIG_FIG_REL_TOL * abs(m_zeta):
        raise RuntimeError(
            f"F_2 class members must agree at s=3 within 4 sig figs; "
            f"got M_zeta={m_zeta}, M_SDW={m_sdw}"
        )
    return m_zeta                                        # (local)


def compute_pair_ratios() -> dict:
    """Compute pair-ratio for each F_2-vs-class entry."""
    M_F2 = f2_aggregate_multiplier()                     # (local)
    out = {}                                             # (local)
    for class_name, partner in CLASS_PARTNER.items():
        M_R = MELLIN_MULTIPLIERS_S3[partner]             # (local)
        pr = pair_ratio(M_F2, M_R)                       # (local)
        out[f"F_2_vs_{class_name}"] = {
            "value": pr,
            "M_F2": M_F2,
            "M_partner": M_R,
            "partner_name": partner,
        }
    return out


def compute_margins(pair_ratios: dict) -> dict:
    """Compute over_PASS, over_FAIL, OOM_safety multipliers per class."""
    out = {}                                             # (local)
    for class_name in CLASS_PARTNER:
        key = f"F_2_vs_{class_name}"                     # (local)
        pr_val = pair_ratios[key]["value"]               # (local)
        # Margin = ratio relative to threshold. Pair-ratio above PASS_thresh
        # means F_2 distinguishable from R; suppression of partner R relative
        # to F_2 yields pair_ratio close to 1 (R ≪ F_2). The "margin" is the
        # OOM by which pair_ratio overshoots the PASS criterion.
        # Per §T-CR3.1: margin_PASS = pr_val / PASS_thresh.
        over_pass = pr_val / PASS_THRESH                 # (local)
        over_fail = pr_val / FAIL_THRESH                 # (local)
        # OOM safety: log10(over_PASS) for compactness
        import math                                      # (local)
        oom = math.log10(over_pass) if over_pass > 0 else float("-inf")
        out[class_name] = {
            "pair_ratio": pr_val,
            "over_PASS": over_pass,
            "over_FAIL": over_fail,
            "OOM_safety": oom,
        }
    return out


def compare_to_expected(
    pair_ratios: dict,
    margins: dict,
    rel_tol: float = SIG_FIG_REL_TOL,
) -> dict:
    """Compare computed values against W-9 CANON-7 expected values."""
    diffs = {}                                            # (local)
    # Pair-ratio comparison.
    for key, expected in EXPECTED_PAIR_RATIOS.items():
        computed = pair_ratios[key]["value"]             # (local)
        rel = abs(computed - expected) / abs(expected) if expected else 0.0
        diffs[key] = {
            "computed": computed,
            "expected": expected,
            "rel_diff": rel,
            "within_4sf": rel < rel_tol,
        }
    # Margin comparison (over_PASS only; over_FAIL is derived).
    for class_name, ref in EXPECTED_MARGINS.items():
        computed = margins[class_name]["over_PASS"]      # (local)
        expected = ref["over_PASS"]
        rel = abs(computed - expected) / abs(expected) if expected else 0.0
        diffs[f"margin_{class_name}_over_PASS"] = {
            "computed": computed,
            "expected": expected,
            "rel_diff": rel,
            "within_4sf": rel < rel_tol,
        }
    return diffs


def run_audit(strict: bool = False) -> dict:
    """Execute the full K-invariance pair-ratio audit."""
    pair_ratios = compute_pair_ratios()                  # (local)
    margins = compute_margins(pair_ratios)               # (local)
    diffs = compare_to_expected(pair_ratios, margins)    # (local)

    all_within = all(d["within_4sf"] for d in diffs.values())  # (local)
    verdict = "PASS" if all_within else "FAIL"           # (local)

    return {
        "audit_id": "S86-W9-K-INVARIANCE-PAIR-RATIO",
        "verdict": verdict,
        "pair_ratios": pair_ratios,
        "margins": margins,
        "diffs": diffs,
        "rel_tol": SIG_FIG_REL_TOL,
        "thresholds": {
            "PASS_thresh": PASS_THRESH,
            "FAIL_thresh": FAIL_THRESH,
        },
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _format_report(result: dict) -> str:
    lines = []                                            # (local)
    lines.append(f"=== {result['audit_id']} ===")
    lines.append(f"Verdict: {result['verdict']}")
    lines.append("")
    lines.append("Pair ratios (computed vs expected):")
    for key, exp in EXPECTED_PAIR_RATIOS.items():
        d = result["diffs"][key]
        flag = "PASS" if d["within_4sf"] else "FAIL"
        lines.append(
            f"  {key:30s}  computed={d['computed']:.4e}  "
            f"expected={d['expected']:.4e}  rel={d['rel_diff']:.2e}  [{flag}]"
        )
    lines.append("")
    lines.append("Margins over PASS threshold (1e-3):")
    for class_name in CLASS_PARTNER:
        m = result["margins"][class_name]
        lines.append(
            f"  {class_name:14s}  over_PASS={m['over_PASS']:7.2f}x  "
            f"over_FAIL={m['over_FAIL']:6.2f}x  OOM={m['OOM_safety']:.2f}"
        )
    lines.append("")
    lines.append(f"Tolerance: rel_tol = {result['rel_tol']:.1e} (4 sig figs)")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="K-invariance pair-ratio verification audit (T4-14)"
    )
    parser.add_argument("--json", action="store_true",
                        help="emit machine-readable JSON")
    parser.add_argument("--strict", action="store_true",
                        help="exit nonzero if any value drifts beyond 4 sig figs")
    args = parser.parse_args()

    result = run_audit(strict=args.strict)               # (local)

    if args.json:
        print(json.dumps(result, indent=2, default=str))
    else:
        print(_format_report(result))

    if args.strict and result["verdict"] == "FAIL":
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
