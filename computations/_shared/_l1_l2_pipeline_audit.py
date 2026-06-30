"""
_l1_l2_pipeline_audit.py

L1↔L2 audit script for F_amp / c_sub / f_conv derivation chain
(T4-18, S86 W-10 AUDIT-W10-1).

Purpose
-------
Audit S52-S77 derivation chain for the three multiplicative
ledger components (target values per W-10 AUDIT-W10-1):

    target F_amp  : approx 1.0166
    target c_sub  : approx 2.238
    target f_conv : approx 9.3 × 10⁻⁴

to identify whether any internal stage carries an explicit Γ(s/2)
call at the L1 zeta-image. Tests two competing options:

  Option (a): Γ-EXACT-at-non-canonical-s_eff
              (one of the three is ≡ Γ(s_eff/2) for some
               well-defined s_eff outside the canonical
               Sd = {8, 6, 4, 2, 0})
  Option (b): non-Γ-but-Γ-numerically-near
              (all three are non-Γ functional forms that
               happen to land near Γ(s/2) values numerically)

Includes test of the s_eff = 11/2 candidate

    Γ(11/4) ≈ A_s_framework / A_s_Planck  at sub-1% threshold
    Γ(11/4) ≈ 11/7  per W-10 R3-B EMERGENCE E1

Substitution chain (Γ-EXACT vs Γ-NEAR test):

    Definition 1: F_amp_target = 1.0166 (S77 anchor)
    Definition 2: Γ(s/2) callable as scipy.special.gamma(s/2)
    Substitute:  for each candidate s_eff in
                   {-2, -1, 0, 1, 2, 11/2, ...},
                   compute Γ(s_eff/2) and test
                   |F_amp_target − Γ(s_eff/2)| / |F_amp_target| < 1e-3
    Direction:   exact match (rel < 1e-12) ⇒ Option (a) for s_eff
                 sub-1% but > 1e-12        ⇒ Option (b) Γ-numerically-near
                 > 1e-2                    ⇒ no match for that s_eff
    Repeat for c_sub and f_conv targets.

Source
------
S86 W-10 §AUDIT-W10-1 (lines 69-73).
S86 W-10 R2-A DISSENT item 1, R2-B DISSENT (co-sign).
S86 W-10 R3-A QUESTIONS Q-L10 + R3-B DISSENT item 1.
S86 W-10 Carry-Forward 1 spec.
S86 W-10 REG-W10-5: s_eff = 11/2 candidate (Γ(11/4) ≈ 11/7 at 2.35%).

Provenance
----------
S86 W0c-7 housekeeping queue Tier-4 row T4-18.
Promoted from S86 W-10 AUDIT-W10-1 (lizzi-spectral, 2026-04-26).

Status
------
SCAFFOLD with ACTIVE Γ-NUMERICAL-NEAR TESTING. Stage requiring S52-S77
derivation-chain code-grep marked TODO(S87).

Usage
-----
    python _l1_l2_pipeline_audit.py                  # default scan
    python _l1_l2_pipeline_audit.py --json
    python _l1_l2_pipeline_audit.py --sub-pct 1.0    # tighter test
"""

from __future__ import annotations

import argparse
import json
import math
import os
import sys
from pathlib import Path

# Cap CPU threads for parallel-agent friendliness.
os.environ.setdefault("OMP_NUM_THREADS", "8")

import numpy as np                                         # noqa: E402

# Project canonical constants (mandatory per .claude/rules/math-scripts.md S34+).
sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import *  # noqa: E402, F401, F403


# ---------------------------------------------------------------------------
# Pinned audit parameters
# ---------------------------------------------------------------------------

# Targets per W-10 AUDIT-W10-1.
TARGETS = {                                                # (local)
    "F_amp":  1.0166,
    "c_sub":  2.238,
    "f_conv": 9.3e-4,
}

# Candidate s_eff values to scan against Γ(s/2).
S_EFF_CANDIDATES = (                                       # (local)
    -2.0, -1.0, 0.0, 0.5, 1.0, 1.5, 2.0,
    2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5,
    11.0 / 2.0,    # W-10 REG-W10-5 candidate
    6.0, 7.0, 8.0,
)

# Match thresholds.
EXACT_REL_TOL_DEFAULT = 1e-12                              # (local)
NEAR_PCT_DEFAULT = 1.0                                     # (local) — sub-1% per W-10 spec

# S52-S77 derivation chain script roster (TODO scaffold).
DERIV_CHAIN_SCRIPTS = (                                    # (local)
    # TODO(S87): pin from W-10 AUDIT-W10-1 Carry-Forward 1 list:
    "computations/session-52/s52_*.py",
    "computations/session-67/s67_bcs_4pt_wilson.py",
    "computations/session-77/s77_*.py",
)


# ---------------------------------------------------------------------------
# Core test
# ---------------------------------------------------------------------------

def gamma_exact_or_near(target: float,
                        s_eff_set: tuple[float, ...] = S_EFF_CANDIDATES,
                        exact_rel_tol: float = EXACT_REL_TOL_DEFAULT,
                        near_pct: float = NEAR_PCT_DEFAULT) -> dict:
    """Test target against Γ(s_eff / 2) for each s_eff in candidate set.

    Returns the best (lowest rel-diff) match plus classification:
        "exact"        if rel < exact_rel_tol
        "near_sub_pct" if rel < near_pct/100
        "no_match"     otherwise
    """
    rows = []                                              # (local)
    for s_eff in s_eff_set:
        try:
            g_val = math.gamma(s_eff / 2.0)               # (local)
        except (ValueError, OverflowError):
            rows.append({"s_eff": s_eff, "gamma_value": None,
                         "rel_diff": None})
            continue
        rel = abs(target - g_val) / abs(target) if target != 0 else float("inf")
        rows.append({
            "s_eff": s_eff,
            "gamma_s_over_2": g_val,
            "rel_diff": rel,
        })

    valid = [r for r in rows if r.get("rel_diff") is not None]
    if not valid:
        return {"target": target, "rows": rows, "best": None,
                "classification": "no_match"}

    best = min(valid, key=lambda r: r["rel_diff"])         # (local)
    if best["rel_diff"] < exact_rel_tol:
        cls = "exact_gamma_at_s_eff"
    elif best["rel_diff"] < near_pct / 100:
        cls = "near_gamma_sub_pct"
    else:
        cls = "no_gamma_match"

    return {
        "target": target,
        "rows": rows,
        "best": best,
        "classification": cls,
    }


# ---------------------------------------------------------------------------
# S52-S77 derivation chain code-grep (TODO scaffold)
# ---------------------------------------------------------------------------

def deriv_chain_gamma_call_grep() -> dict:
    """Grep S52-S77 derivation chain scripts for explicit Γ(s/2) calls.

    TODO(S87): implement grep across DERIV_CHAIN_SCRIPTS for
    `gamma(s/2)`, `scipy.special.gamma`, `mpmath.gamma`, etc.
    Returns list of (script, line_no, snippet) for any explicit
    Γ-call at the L1 zeta-image.
    """
    raise NotImplementedError(
        "TODO(S87): deriv_chain_gamma_call_grep — code-grep across "
        "DERIV_CHAIN_SCRIPTS roster pending S87 Carry-Forward 1."
    )


# ---------------------------------------------------------------------------
# Top-level audit
# ---------------------------------------------------------------------------

def run_audit(near_pct: float = NEAR_PCT_DEFAULT) -> dict:
    """Run the L1↔L2 pipeline audit."""
    target_results = {}                                    # (local)
    for name, val in TARGETS.items():
        target_results[name] = gamma_exact_or_near(val, near_pct=near_pct)

    # Deriv-chain code-grep (scaffold).
    try:
        grep_results = deriv_chain_gamma_call_grep()
    except NotImplementedError as e:
        grep_results = {"status": "TODO_S87", "blocked_by": str(e)}

    # Verdict logic:
    #   PASS = at least one target is exact_gamma_at_s_eff (Option a)
    #   INFO = at least one is near_gamma_sub_pct (Option b)
    #   FAIL = no Γ matches (neither option supported)
    classifications = [r["classification"] for r in target_results.values()]
    if "exact_gamma_at_s_eff" in classifications:
        verdict = "PASS"
        winning_option = "a_gamma_exact_at_non_canonical_s_eff"
    elif "near_gamma_sub_pct" in classifications:
        verdict = "INFO"
        winning_option = "b_non_gamma_but_numerically_near"
    else:
        verdict = "FAIL"
        winning_option = None

    return {
        "audit_id": "S86-W10-L1-L2-PIPELINE",
        "verdict": verdict,
        "winning_option": winning_option,
        "near_pct": near_pct,
        "targets": target_results,
        "deriv_chain_grep": grep_results,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="L1↔L2 pipeline audit for F_amp/c_sub/f_conv (T4-18 / S86 W-10 AUDIT-W10-1)"
    )
    parser.add_argument("--sub-pct", type=float, default=NEAR_PCT_DEFAULT,
                        help=f"Γ-near threshold percent (default: {NEAR_PCT_DEFAULT})")
    parser.add_argument("--json", action="store_true",
                        help="emit machine-readable JSON")
    args = parser.parse_args()

    result = run_audit(args.sub_pct)                      # (local)

    if args.json:
        print(json.dumps(result, indent=2, default=str))
    else:
        print("=== S86 W-10 L1↔L2 Pipeline Audit (T4-18) ===")
        print(f"Verdict       : {result['verdict']}")
        print(f"Winning option: {result['winning_option']}")
        print(f"Near threshold: {result['near_pct']}%\n")
        for name, r in result["targets"].items():
            print(f"Target {name} = {r['target']}:  classification = {r['classification']}")
            if r.get("best"):
                b = r["best"]
                print(f"  best s_eff = {b['s_eff']}, "
                      f"Γ(s/2) = {b['gamma_s_over_2']:.6e}, "
                      f"rel_diff = {b['rel_diff']:.3e}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
