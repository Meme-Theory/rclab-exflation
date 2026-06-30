"""
_analytic_continuation_channel_3bc_probe.py

Analytic-continuation probe for channel-3b vs channel-3c distinction
(T4-13, S86 W-8 AUDIT-2).

# NEEDS-ORCHESTRATOR-FOLLOWUP: NEEDS-DECISION readiness — orchestrator
# must approve the probe's pre-registered specification (probe-points
# in the right half-plane, holomorphic-extension acceptance criterion,
# numerical-derivative tolerance) BEFORE deployment. Default
# specification below is provisional; freeze in S87 plan-block.

Purpose
-------
Evaluate f(z) for z ∈ ℂ with Re(z) > 0 outside the natural support
boundary; check whether a holomorphic extension exists past the
natural support boundary (channel-3c) or whether f(z) terminates at
the boundary (channel-3b).

Channel-3b: f admits NO holomorphic extension past natural support
            (singularity / branch cut at boundary).
Channel-3c: f admits holomorphic extension past natural support
            (single-valued analytic continuation).

Substitution chain (analytic-continuation existence):

    Definition 1: f(s) — Mellin-cone residue function on Re(s) ≤ s_0
    Definition 2: support boundary s_0 — natural support edge per
                  channel-3 classification
    Definition 3: probe set Z = {z_k : Re(z_k) > s_0, k = 1..N}
    Substitute:   if f admits analytic continuation, f(z_k) is
                  smooth in z_k and satisfies Cauchy-Riemann to
                  numerical precision
    Simplify:     test |∂f/∂z̄|(z_k) < cr_tol on probe set ⇒
                  channel-3c (extension exists)
                  test divergence / branch jump at z_k → s_0+ ⇒
                  channel-3b (no extension)
    Direction:    smooth probe values ⇒ extension exists (3c)
                  divergence / non-smooth ⇒ no extension (3b)

Source
------
S86 W-8 §AUDIT-2 (lines 41-42).
S86 W-8 Open Question 4 (lines 1951-1953).
S86 W-8 §1 verdict trace: "SDW channel-3b INFO (Bernstein 1928 /
Sage MCP M_6 = 1/168); ζ channel-3d FAIL at s ≥ 1; anomaly
channel-3e TBD".

Provenance
----------
S86 W0c-7 housekeeping queue Tier-4 row T4-13.
Promoted from S86 W-8 AUDIT-2 (connes-ncg + lizzi, 2026-04-26).

Status
------
SCAFFOLD. Major dependencies marked TODO(S87):
  - f(z) callable per regulator (load via Sage MCP closed form
    where available)
  - Natural support boundary s_0 per regulator (load from
    `cutoff-sqrt-adjudication.md` channel-3 sub-classification)

Usage (post-S87 wire-up)
------------------------
    python _analytic_continuation_channel_3bc_probe.py --regulator anomaly
    python _analytic_continuation_channel_3bc_probe.py --json
"""

from __future__ import annotations

import argparse
import json
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
# Pinned probe parameters
# ---------------------------------------------------------------------------

# Default probe distance into the right half-plane past s_0.
PROBE_DELTA_DEFAULT = 0.1                                  # (local)

# Default number of probe points along Im(z).
PROBE_N_DEFAULT = 16                                       # (local)

# Default Im(z) range for probe ring around z_0 = s_0 + delta.
PROBE_IM_RADIUS_DEFAULT = 0.5                              # (local)

# Cauchy-Riemann tolerance for "smooth" / channel-3c declaration.
CR_TOL_DEFAULT = 1e-6                                      # (local)

# Numerical-derivative step size.
NUM_DERIV_H_DEFAULT = 1e-6                                 # (local)


# ---------------------------------------------------------------------------
# Hooks (TODO scaffolds)
# ---------------------------------------------------------------------------

def load_residue_function(regulator: str):
    """Load the Mellin-cone residue function f(z) for `regulator`.

    TODO(S87): integrate with Sage MCP closed-form access. For some
    regulators (anomaly, SDW, Zubarev), W-8 references closed-form
    M_6 expressions from which f(z) can be reconstructed.
    """
    raise NotImplementedError(
        f"TODO(S87): load_residue_function({regulator}) requires Sage MCP "
        "closed-form access per W-8 lines 16-17 (regulator residue trace)."
    )


def load_natural_support_boundary(regulator: str) -> float:
    """Load natural support boundary s_0 per regulator.

    TODO(S87): pin from `sessions/framework/registry/cutoff-sqrt-adjudication.md`
    channel-3 sub-classification table.
    """
    raise NotImplementedError(
        f"TODO(S87): load_natural_support_boundary({regulator}) requires "
        "cutoff-sqrt-adjudication.md channel-3 sub-classification."
    )


# ---------------------------------------------------------------------------
# Core probe
# ---------------------------------------------------------------------------

def cauchy_riemann_residual(f, z: complex,
                            h: float = NUM_DERIV_H_DEFAULT) -> float:
    """Return |∂f/∂z̄|(z) ≈ 0.5·|∂_x f + i·∂_y f| via finite differences.

    Substitution chain:
        f(z) = u(x,y) + i v(x,y)
        ∂f/∂z̄ = 0.5 · (∂_x f + i · ∂_y f)
        Cauchy-Riemann: f holomorphic ⇔ ∂f/∂z̄ = 0
        Direction: holomorphic ⇒ residual → 0; non-holomorphic ⇒ residual ≠ 0
    """
    fxp = f(complex(z.real + h, z.imag))                  # (local)
    fxm = f(complex(z.real - h, z.imag))                  # (local)
    fyp = f(complex(z.real, z.imag + h))                  # (local)
    fym = f(complex(z.real, z.imag - h))                  # (local)
    df_dx = (fxp - fxm) / (2 * h)                         # (local)
    df_dy = (fyp - fym) / (2 * h)                         # (local)
    df_dzbar = 0.5 * (df_dx + 1j * df_dy)                 # (local)
    return abs(df_dzbar)                                  # (local)


def probe_analytic_continuation(f, s_0: float,
                                delta: float = PROBE_DELTA_DEFAULT,
                                n_points: int = PROBE_N_DEFAULT,
                                im_radius: float = PROBE_IM_RADIUS_DEFAULT,
                                cr_tol: float = CR_TOL_DEFAULT) -> dict:
    """Run the analytic-continuation probe at z_k = (s_0 + delta) + i·y_k
    where y_k uniformly samples [-im_radius, +im_radius].

    Returns classification: channel-3c (extension) or channel-3b (no extension).
    """
    y_grid = np.linspace(-im_radius, im_radius, n_points) # (local)
    rows = []                                              # (local)
    blew_up = False                                        # (local)
    max_residual = 0.0                                     # (local)

    for y in y_grid:
        z = complex(s_0 + delta, float(y))                # (local)
        try:
            f_val = f(z)                                  # (local)
        except (OverflowError, ValueError, ZeroDivisionError) as e:
            rows.append({"z": (z.real, z.imag), "error": str(e),
                         "diverged": True})
            blew_up = True
            continue
        if not np.isfinite(complex(f_val).real) or not np.isfinite(complex(f_val).imag):
            rows.append({"z": (z.real, z.imag), "value": "non-finite",
                         "diverged": True})
            blew_up = True
            continue
        cr_resid = cauchy_riemann_residual(f, z)          # (local)
        max_residual = max(max_residual, cr_resid)
        rows.append({
            "z": (z.real, z.imag),
            "f_value": [float(np.real(f_val)), float(np.imag(f_val))],
            "cr_residual": cr_resid,
            "smooth": cr_resid < cr_tol,
        })

    if blew_up:
        classification = "channel-3b"   # divergence/branch ⇒ no extension
    elif max_residual < cr_tol:
        classification = "channel-3c"   # smooth ⇒ extension exists
    else:
        classification = "channel-3b_marginal"  # mixed signal

    return {
        "s_0": s_0,
        "delta": delta,
        "n_probe_points": n_points,
        "max_cr_residual": max_residual,
        "cr_tol": cr_tol,
        "classification": classification,
        "probe_rows": rows,
    }


def run_audit(regulator: str, **kwargs) -> dict:
    """Top-level audit: probe channel-3b vs channel-3c distinction."""
    try:
        f = load_residue_function(regulator)              # (local)
        s_0 = load_natural_support_boundary(regulator)    # (local)
    except NotImplementedError as e:
        return {
            "audit_id": "S86-W8-ANALYTIC-CONTINUATION-CHANNEL-3BC",
            "verdict": "INFO_SCAFFOLD",
            "regulator": regulator,
            "blocked_by": str(e),
        }

    probe = probe_analytic_continuation(f, s_0, **kwargs) # (local)
    cls = probe["classification"]                          # (local)
    verdict = (
        "PASS" if cls == "channel-3c"
        else "FAIL" if cls == "channel-3b"
        else "INFO"
    )

    return {
        "audit_id": "S86-W8-ANALYTIC-CONTINUATION-CHANNEL-3BC",
        "verdict": verdict,
        "regulator": regulator,
        **probe,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Analytic-continuation probe channel-3b/3c (T4-13 / S86 W-8 AUDIT-2)"
    )
    parser.add_argument("--regulator", type=str, required=True,
                        help="regulator name (anomaly, SDW, Zubarev, ...)")
    parser.add_argument("--delta", type=float, default=PROBE_DELTA_DEFAULT)
    parser.add_argument("--n-points", type=int, default=PROBE_N_DEFAULT)
    parser.add_argument("--im-radius", type=float, default=PROBE_IM_RADIUS_DEFAULT)
    parser.add_argument("--cr-tol", type=float, default=CR_TOL_DEFAULT)
    parser.add_argument("--json", action="store_true",
                        help="emit machine-readable JSON")
    args = parser.parse_args()

    result = run_audit(args.regulator,
                       delta=args.delta,
                       n_points=args.n_points,
                       im_radius=args.im_radius,
                       cr_tol=args.cr_tol)                # (local)

    if args.json:
        print(json.dumps(result, indent=2, default=str))
    else:
        print("=== S86 W-8 Analytic-Continuation channel-3bc Probe (T4-13) ===")
        print(f"Verdict: {result['verdict']}")
        print(f"Regulator: {result.get('regulator')}")
        if "blocked_by" in result:
            print(f"Blocked by: {result['blocked_by']}")
        else:
            print(f"s_0 (support boundary): {result.get('s_0')}")
            print(f"Probe delta: {result.get('delta')}")
            print(f"Max CR residual: {result.get('max_cr_residual')}")
            print(f"Classification: {result.get('classification')}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
