"""
_nroy_cascade_audit.py

NROY-cascade audit beyond n_s
(T4-19, S86 W-10 AUDIT-W10-2).

Purpose
-------
Enumerates all FROZEN observables that depend on c_sub via
r_running-analogs. Builds a 1-parameter family table (analog of
S86 W1c-8's NROY table for n_s) showing all FROZEN observables and
their cascade shifts under any c_sub correction in the strict band

    c_sub ∈ [3.0581, 4.1375]

For each Y_i, derive

    r_i_running := d(ln Y_i) / d(ln c_sub)

and compute cascade shift

    Δln(Y_i) = r_i_running · Δln(c_sub)

at central c_sub correction; check against each Y_i's freeze
bandwidth (NROY band).

Substitution chain (cascade-shift derivation):

    Definition 1: Y_i — frozen observable depending on c_sub
    Definition 2: r_i_running := d(ln Y_i)/d(ln c_sub) — running-rate
                  analog of tensor-to-scalar r
    Definition 3: NROY band B_i = [Y_i_min, Y_i_max] — pre-registered
                  freeze bandwidth
    Substitute:   Δln(Y_i) = r_i_running · Δln(c_sub)
                          = r_i_running · ln(c_sub_corrected / c_sub_central)
    Simplify:     Y_i_shifted = Y_i_central · exp(Δln(Y_i))
                              = Y_i_central · (c_sub_corrected / c_sub_central) ** r_i_running
    Direction:    r_i_running > 0 ⇒ c_sub correction shifts Y_i
                                     in the same OOM direction
                  |r_i_running · Δln(c_sub)| > |ln(B_i_max/Y_i_central)|
                                  ⇒ NROY violation (cascade kicks Y_i
                                     out of its freeze band)

Source
------
S86 W-10 §AUDIT-W10-2 (lines 75-80).
S86 W-10 R2-A QUESTIONS Q-L8.
S86 W-10 R2-B EMERGENCE E3 closing.
S86 W-10 R3-A CONVERGENCE #6c.
S86 W-10 Q-L14 lock-in.

Provenance
----------
S86 W0c-7 housekeeping queue Tier-4 row T4-19.
Promoted from S86 W-10 AUDIT-W10-2 (connes + lizzi, 2026-04-26).

Status
------
SCAFFOLD. Major dependencies marked TODO(S87):
  - r_i_running per FROZEN observable (analytic derivatives or
    finite-difference along c_sub) requires S87 derivation chain
  - FROZEN observable enumeration (A_s, n_s known; α_s running, r,
    BBN, downstream CMB observables to be enumerated)

Usage (post-S87 wire-up)
------------------------
    python _nroy_cascade_audit.py
    python _nroy_cascade_audit.py --json
    python _nroy_cascade_audit.py --c-sub-corrected 3.5
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

# c_sub strict band (W-10 AUDIT-W10-2 spec).
C_SUB_BAND = (3.0581, 4.1375)                              # (local)
C_SUB_CENTRAL = 0.5 * (C_SUB_BAND[0] + C_SUB_BAND[1])     # (local)

# Frozen observable roster — initial known set.
# Each entry: (name, central_value, NROY band lo, NROY band hi)
FROZEN_OBSERVABLES = (                                     # (local)
    # (name,             central,    NROY_lo,    NROY_hi)
    ("A_s",              2.10e-9,    1.95e-9,    2.25e-9),
    ("n_s",              0.965,      0.957,      0.972),
    # TODO(S87): enumerate alpha_s, r, downstream BBN/CMB observables.
)


# ---------------------------------------------------------------------------
# r_i_running hooks (TODO scaffolds)
# ---------------------------------------------------------------------------

def r_i_running(observable_name: str) -> float:
    """Return r_i_running := d(ln Y_i) / d(ln c_sub) for `observable_name`.

    TODO(S87): pin per observable from analytic or finite-difference
    derivative of the canonical Y_i(c_sub) formula along the c_sub
    derivation chain.
    """
    raise NotImplementedError(
        f"TODO(S87): r_i_running({observable_name}) requires analytic "
        "or finite-difference derivative pin from S87 derivation chain."
    )


# ---------------------------------------------------------------------------
# Core audit
# ---------------------------------------------------------------------------

def cascade_shift(Y_central: float, r_run: float,
                  c_sub_central: float, c_sub_corrected: float) -> dict:
    """Compute Y_i_shifted under c_sub correction.

    Substitution chain:
        Δln(Y_i) = r_run · ln(c_sub_corr / c_sub_central)
        Y_shifted = Y_central · exp(Δln(Y_i))
                  = Y_central · (c_sub_corr / c_sub_central) ** r_run
    Direction:
        r_run > 0 ⇒ Y_shifted moves in same direction as c_sub
        r_run < 0 ⇒ Y_shifted moves opposite
    """
    delta_ln_csub = math.log(c_sub_corrected / c_sub_central)  # (local)
    delta_ln_Y = r_run * delta_ln_csub                    # (local)
    Y_shifted = Y_central * math.exp(delta_ln_Y)          # (local)
    return {
        "delta_ln_csub": delta_ln_csub,
        "delta_ln_Y": delta_ln_Y,
        "Y_shifted": Y_shifted,
    }


def cascade_audit_one(name: str, central: float,
                      nroy_lo: float, nroy_hi: float,
                      c_sub_corrected: float) -> dict:
    """Audit one observable's cascade shift."""
    try:
        r_run = r_i_running(name)                         # (local)
    except NotImplementedError as e:
        return {
            "observable": name,
            "central": central,
            "NROY_lo": nroy_lo,
            "NROY_hi": nroy_hi,
            "status": "NOT_RUN_SCAFFOLD",
            "blocked_by": str(e),
        }
    shift = cascade_shift(central, r_run, C_SUB_CENTRAL, c_sub_corrected)
    Y_shifted = shift["Y_shifted"]                         # (local)
    in_band = nroy_lo <= Y_shifted <= nroy_hi              # (local)
    return {
        "observable": name,
        "central": central,
        "r_running": r_run,
        "c_sub_central": C_SUB_CENTRAL,
        "c_sub_corrected": c_sub_corrected,
        "Y_shifted": Y_shifted,
        "NROY_lo": nroy_lo,
        "NROY_hi": nroy_hi,
        "within_NROY_band": in_band,
        **shift,
    }


def run_audit(c_sub_corrected: float | None = None) -> dict:
    """Top-level audit dispatch."""
    if c_sub_corrected is None:
        c_sub_corrected = C_SUB_BAND[1]                   # (local) — upper edge default

    rows = [
        cascade_audit_one(name, central, lo, hi, c_sub_corrected)
        for (name, central, lo, hi) in FROZEN_OBSERVABLES
    ]

    blocked = [r for r in rows if r.get("status") == "NOT_RUN_SCAFFOLD"]
    nroy_violations = [r for r in rows if r.get("within_NROY_band") is False]

    if blocked:
        verdict = "INFO_SCAFFOLD"
    elif nroy_violations:
        verdict = "FAIL"   # any cascade kicks an observable out of its band
    else:
        verdict = "PASS"

    return {
        "audit_id": "S86-W10-NROY-CASCADE",
        "verdict": verdict,
        "c_sub_band": list(C_SUB_BAND),
        "c_sub_central": C_SUB_CENTRAL,
        "c_sub_corrected": c_sub_corrected,
        "rows": rows,
        "scaffold_blocker_count": len(blocked),
        "nroy_violation_count": len(nroy_violations),
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="NROY-cascade audit beyond n_s (T4-19 / S86 W-10 AUDIT-W10-2)"
    )
    parser.add_argument("--c-sub-corrected", type=float, default=None,
                        help=f"corrected c_sub (default: upper band edge {C_SUB_BAND[1]})")
    parser.add_argument("--json", action="store_true",
                        help="emit machine-readable JSON")
    args = parser.parse_args()

    result = run_audit(args.c_sub_corrected)              # (local)

    if args.json:
        print(json.dumps(result, indent=2, default=str))
    else:
        print("=== S86 W-10 NROY-Cascade Audit (T4-19) ===")
        print(f"Verdict: {result['verdict']}")
        print(f"c_sub band: [{C_SUB_BAND[0]}, {C_SUB_BAND[1]}]")
        print(f"c_sub central → corrected: {result['c_sub_central']:.4f} → {result['c_sub_corrected']:.4f}")
        print(f"Scaffold blockers: {result['scaffold_blocker_count']}")
        print(f"NROY violations  : {result['nroy_violation_count']}\n")
        for r in result["rows"]:
            if r.get("status") == "NOT_RUN_SCAFFOLD":
                print(f"  {r['observable']:12s}: SCAFFOLD ({r['blocked_by'][:60]}...)")
            else:
                flag = "IN-BAND" if r["within_NROY_band"] else "VIOLATION"
                print(f"  {r['observable']:12s}: r_run={r['r_running']:+.3f}  "
                      f"Y_shifted={r['Y_shifted']:.4e}  [{flag}]")

    return 0


if __name__ == "__main__":
    sys.exit(main())
