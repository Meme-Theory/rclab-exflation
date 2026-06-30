"""
_sr_lo_autocatalysis_bound_audit.py

SR-LO autocatalysis-bound enforcement audit (T4-15, S86 W-9 AUDIT-2).

Purpose
-------
For any future SR-LO ODE rerun citing F_2-class xi²_0 ≈ 13.6425 (or
any other xi²_0 value), audit checks the autocatalysis bound

    eps_0 · exp(2 · xi²_0 · N_max) <= eps_target

and refuses dispatch if the required eps_0 falls below the IEEE-754
float64 underflow boundary 1e-308.

Substitution chain (Step 4, S86 W-9 §T2 lines 784-801):

    Definition 1: ε(N) ≤ ε_0 · exp(2 · ξ²_0 · N)         [SR-LO autocatalysis envelope]
    Definition 2: ε_target = strict-linear cap (e.g., 0.1 or 0.5)
    Definition 3: N_max     = e-fold count to reach (e.g., 55)
    Substitute:  required ε_0 = ε_target / exp(2 · ξ²_0 · N_max)
    Simplify:    log10(req_eps_0) = log10(ε_target) − (2·ξ²_0·N_max)/ln(10)
    Direction:   xi²_0 ↑ → exponent ↑ → required ε_0 ↓ (sharper underflow risk)

For F_2-class xi²_0 = 13.6425, N_max = 55, ε_target = 0.5:
    log10(req_eps_0) = log10(0.5) − (2·13.6425·55)/ln(10)
                     = −0.301 − 1500.675/2.302585
                     ≈ −0.301 − 651.49
                     ≈ −651.79

→ required ε_0 ≈ 10^{-651.79} ≪ float64 underflow 10^{-308}. REFUSE.

Source
------
S86 W-9 §T2 substitution chain Step 4 (lines 784-801).
S86 W-9 §C-R2.1 lizzi recomputation (lines 938-963).
S86 W-9 R-6: F_2-class SR-LO autocatalysis closure clause (f).
S86 W-9 CANON-4: xi²_0_lin_crit = 0.395 at N=55, max(ε)≤0.1.

Provenance
----------
S86 W0c-7 housekeeping queue Tier-4 row T4-15.
Promoted from S86 W-9 AUDIT-2 (transit, 2026-04-26).

Usage
-----
    python _sr_lo_autocatalysis_bound_audit.py --xi2 13.6425 --N 55 --target 0.5
    python _sr_lo_autocatalysis_bound_audit.py --xi2 0.395 --N 55 --target 0.1
    python _sr_lo_autocatalysis_bound_audit.py --json --xi2 13.6425
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

# Project canonical constants (mandatory per .claude/rules/math-scripts.md S34+).
sys.path.insert(0, str(Path(__file__).parent))
from canonical_constants import *  # noqa: F401,F403


# ---------------------------------------------------------------------------
# Pinned bounds (W-9 CANON-3, CANON-4, CANON-5; IEEE-754 spec)
# ---------------------------------------------------------------------------

FLOAT64_MIN_NORMAL = 2.2250738585072014e-308              # (local) — IEEE-754 normal underflow
FLOAT64_MIN_DENORMAL = 5e-324                             # (local) — IEEE-754 denormal underflow

# Pre-pinned crit values (W-9 CANON-3..5).
XI_SQ_0_CRIT_BREAKDOWN_N1 = 2.2256                        # (local) — CANON-3
XI_SQ_0_LIN_CRIT_N55 = 0.395                              # (local) — CANON-4
XI_SQ_0_SR_LO_VALID_CRIT_N55 = 1.7                        # (local) — CANON-5

# F_2-class anchor xi²_0 (transit T2 derivation; W-9 R-6 clause (f)).
XI_SQ_0_F2_CLASS = 13.6425                                # (local)

# Default ε_target / N_max for canonical SR-LO sanity reproduction.
EPS_TARGET_DEFAULT = 0.5                                  # (local) — SR-LO validity ceiling
N_MAX_DEFAULT = 55                                        # (local) — pivot e-fold count


# ---------------------------------------------------------------------------
# Core audit logic
# ---------------------------------------------------------------------------

def required_eps_0(xi_sq_0: float, N_max: float, eps_target: float) -> float:
    """Compute required initial ε_0 to satisfy the SR-LO autocatalysis bound.

    Derivation (substitution chain in module docstring):
        eps_0 = eps_target / exp(2 · xi²_0 · N_max)

    Returns 0.0 when the exponent overflows (i.e., eps_0 below denormal floor).
    """
    exponent = 2.0 * xi_sq_0 * N_max                      # (local)
    # Use log-space to avoid overflow when exp() would > 1e308.
    log10_req = math.log10(eps_target) - exponent / math.log(10.0)  # (local)
    if log10_req < math.log10(FLOAT64_MIN_DENORMAL):
        return 0.0                                        # (local) — beyond float64 range
    return 10.0 ** log10_req                              # (local)


def log10_required_eps_0(xi_sq_0: float, N_max: float, eps_target: float) -> float:
    """Log10 of required ε_0; survives arbitrary xi²_0·N_max."""
    return math.log10(eps_target) - (2.0 * xi_sq_0 * N_max) / math.log(10.0)


def autocatalysis_audit(
    xi_sq_0: float,
    N_max: float = N_MAX_DEFAULT,
    eps_target: float = EPS_TARGET_DEFAULT,
    underflow_floor: float = FLOAT64_MIN_NORMAL,
) -> dict:
    """Run the autocatalysis-bound audit for one xi²_0 value.

    Returns
    -------
    dict with fields:
        verdict       — "PASS" if required ε_0 ≥ underflow_floor;
                        "FAIL" otherwise (refuse SR-LO ODE dispatch).
        required_eps_0 — float (may be 0.0 if log10 < log10(denormal))
        log10_required_eps_0 — exact log10 even if eps_0 underflows
        margin_log10  — log10(req_eps_0) − log10(underflow_floor)
                        (POSITIVE = safe; NEGATIVE = refuse)
        underflow_floor — pinned IEEE-754 normal-underflow boundary
    """
    log10_req = log10_required_eps_0(xi_sq_0, N_max, eps_target)  # (local)
    log10_floor = math.log10(underflow_floor)             # (local)
    margin = log10_req - log10_floor                      # (local)
    verdict = "PASS" if margin >= 0.0 else "FAIL"         # (local)

    return {
        "audit_id": "S86-W9-SR-LO-AUTOCATALYSIS-BOUND",
        "verdict": verdict,
        "inputs": {
            "xi_sq_0": xi_sq_0,
            "N_max": N_max,
            "eps_target": eps_target,
            "underflow_floor": underflow_floor,
        },
        "required_eps_0": required_eps_0(xi_sq_0, N_max, eps_target),
        "log10_required_eps_0": log10_req,
        "margin_log10": margin,
        "refuse_dispatch": (verdict == "FAIL"),
        "remediation": (
            None if verdict == "PASS" else
            "Required eps_0 below float64 underflow; SR-LO ODE rerun cannot "
            "be carried out at this (xi^2_0, N_max, eps_target). Either: "
            "(a) reduce N_max via stage-decomposition; (b) loosen eps_target; "
            "(c) reduce xi^2_0 via class restriction; (d) switch to mpmath "
            "arbitrary-precision integration; (e) accept clause-(f)-type "
            "permanent autocatalysis closure."
        ),
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _format_report(result: dict) -> str:
    inp = result["inputs"]                                # (local)
    lines = []                                             # (local)
    lines.append(f"=== {result['audit_id']} ===")
    lines.append(f"Verdict: {result['verdict']}")
    lines.append("")
    lines.append("Inputs:")
    lines.append(f"  xi^2_0          = {inp['xi_sq_0']}")
    lines.append(f"  N_max           = {inp['N_max']}")
    lines.append(f"  eps_target      = {inp['eps_target']}")
    lines.append(f"  underflow_floor = {inp['underflow_floor']:.4e}  "
                 f"(log10 = {math.log10(inp['underflow_floor']):.2f})")
    lines.append("")
    lines.append("Computed:")
    lines.append(f"  log10(required eps_0) = {result['log10_required_eps_0']:.4f}")
    lines.append(f"  required eps_0         = {result['required_eps_0']:.4e}")
    lines.append(f"  margin_log10           = {result['margin_log10']:+.4f}  "
                 f"({'SAFE' if result['margin_log10'] >= 0 else 'UNDERFLOW'})")
    lines.append("")
    if result["refuse_dispatch"]:
        lines.append("REFUSE: SR-LO ODE dispatch must not proceed at these inputs.")
        if result["remediation"]:
            lines.append(f"Remediation: {result['remediation']}")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="SR-LO autocatalysis-bound enforcement audit (T4-15)"
    )
    parser.add_argument("--xi2", type=float, default=XI_SQ_0_F2_CLASS,
                        help=f"xi^2_0 value (default: F_2-class {XI_SQ_0_F2_CLASS})")
    parser.add_argument("--N", type=float, default=N_MAX_DEFAULT,
                        help=f"N_max e-folds (default: {N_MAX_DEFAULT})")
    parser.add_argument("--target", type=float, default=EPS_TARGET_DEFAULT,
                        help=f"eps_target validity cap (default: {EPS_TARGET_DEFAULT})")
    parser.add_argument("--json", action="store_true",
                        help="emit machine-readable JSON")
    parser.add_argument("--strict", action="store_true",
                        help="exit nonzero if FAIL (refuse-dispatch mode)")
    args = parser.parse_args()

    result = autocatalysis_audit(args.xi2, args.N, args.target)  # (local)

    if args.json:
        print(json.dumps(result, indent=2, default=str))
    else:
        print(_format_report(result))

    if args.strict and result["refuse_dispatch"]:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
