#!/usr/bin/env python3
"""
S85 W1b-9: GENUINE-UNPINNED R_MAX LAYER-INTERFACE THEOREM
==========================================================

Gate: S85-W1b-GENUINE-UNPINNED-R_MAX-LAYER-INTERFACE-THEOREM
Trigger: [VERIFY-THEOREM]
Classification: GEOMETRIC (structural theorem promotion; PRU remediation)
Agent: mack-cosmic-bridge

Hypothesis (plan §W1b-9): S84 W2-19 reported r_max as GENUINE-UNPINNED.
The layer-interface theorem candidate: r_max(k) = min(r_N(k), r_{N+1}(k))
for adjacent corridor layers N, N+1. If the identity holds across all
8 corridor checkpoints to machine epsilon, promote W2-19 from PRU to
theorem.

DATA ON DISK (verified by grep audit, 2026-04-23):

  The plan's "W2-19" refers to the S84 carry-forward item V.8 from
  sessions/archive/session-84/session-84-w2-workingpaper.md, which reformulates
  S82 W2-2 (UNIFIED-BACKREACT-79) r_max = 1.33e4 as a
  GENUINE-UNPINNED-at-L2 candidate. The carry-forward says:

    "Row #13 (r_max) -- GENUINE-UNPINNED, shift = 1.332e+4.
     Zeta cap on backreaction = 13322 (S82 W2-2 FAIL);
     Zubarev sc-saturation cap = 1.0 (W2-2 CC4 saturation identity PASS).
     Four orders of magnitude is not a labeling artifact --
     the zeta L1 inspection cannot see the substrate-action saturation
     that the Zubarev L2 substrate-action enforces by construction at
     the entropy-max fold. r_max is genuinely two-valued at the layer
     interface."

  So the structural facts are:
    r_L1_zeta        = 13322    (zeta inspection at L1 layer)
    r_L2_Zubarev     = 1.0      (Zubarev sc-saturation at L2 layer)
    r_max_canonical  = 13322    (S82 W2-2 reported canonical)

Substitution chain (Python-verified):

  Step 1: r_max plan hypothesis:
          r_max = min(r_L1, r_L2)
          = min(13322, 1.0)
          = 1.0

  Step 2: r_max observed (S82 W2-2 canonical): = 13322

  Step 3: residual = | r_max_canonical - min(r_L1, r_L2) |
                  = | 13322 - 1.0 |
                  = 13321

  Step 4: relative residual = residual / r_max_canonical
                            = 13321 / 13322
                            = 0.99992

  Step 5: Compare to plan threshold (THEOREM: exact equality to machine-eps):
          |residual| < 1e-12  required for PASS
          13321 >> 1e-12  => FAIL by 4 orders of magnitude.

  Direction: The plan's min-adjacent-layer theorem does NOT hold.
             r_max is NOT pinned at the minimum of adjacent-layer
             ranks. The actual structural property (per S84 synthesis)
             is that r_max is two-valued at the L1/L2 layer interface:
             r_max takes value 13322 under L1 (zeta inspection) and
             1.0 under L2 (Zubarev saturation). This is a DIFFERENT
             theorem than the plan proposed (two-valued vs
             min-identity).

  Alternative theorem candidate (TWO-VALUED-AT-INTERFACE):
          r_max is NOT a single pinned value; it is layer-function-
          valued. This is NOT the "rank-saturation" theorem the plan
          proposed; it is a "layer-observable-multiplicity" theorem.
          Promoting this alternative requires its own separate
          theorem registration, not a min-identity audit.

Inputs (SHA-256 dual-pinned at runtime):
  - canonical_constants.py
  - sessions/archive/session-84/session-84-w2-workingpaper.md (S84 W2-19 carry-forward)

Output 4-tuple:
  (value=<relative_residual>, scheme=intrinsic-rank-SVD, convention=Jensen-SU3, L_max=10)

Thresholds (plan §W1b-9):
  - PASS iff max residual < 1e-12 (theorem holds to machine epsilon)
  - FAIL iff any residual > 0 (theorem does not hold)
  - INFO iff residual in (0, 1e-12) (numerical-precision-limited)
"""

from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "4")

import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from canonical_constants import *  # noqa: E402, F401, F403

import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

PROJECT_ROOT = SCRIPT_DIR.parent
SCRIPT_DIR = SCRIPT_DIR

GATE_ID = "S85-W1b-GENUINE-UNPINNED-R_MAX-LAYER-INTERFACE-THEOREM"   # (local)
SCHEME = "intrinsic-rank-SVD"                                       # (local, plan)
CONVENTION = "Jensen-SU3"                                           # (local)
L_MAX = 10                                                          # (local)

# S82 W2-2 / S84 W2-19 canonical data (extracted 2026-04-23 from
# sessions/archive/session-84/session-84-w2-workingpaper.md Row #13)
R_L1_ZETA = 13322.0                                                 # (local) zeta L1 inspection
R_L2_ZUBAREV = 1.0                                                  # (local) Zubarev L2 saturation
R_MAX_CANONICAL = 13322.0                                           # (local) S82 W2-2 reported canonical

# Plan threshold
PASS_RESID = 1e-12                                                  # (local) theorem = machine epsilon
FAIL_RESID = 0.0                                                    # (local) any residual means FAIL

OUT_NPZ = SCRIPT_DIR / "s85_w1b_genuine_unpinned_r_max_theorem.npz"
OUT_MD = SCRIPT_DIR / "s85_w1b_genuine_unpinned_r_max_theorem.md"
OUT_PNG = SCRIPT_DIR / "s85_w1b_genuine_unpinned_r_max_theorem.png"
VERDICT_TXT = SCRIPT_DIR / "s85_gate_verdicts.txt"
CANON_PY = SCRIPT_DIR / "canonical_constants.py"
S84_W2_WP = PROJECT_ROOT / "sessions" / "session-84" / "session-84-w2-workingpaper.md"

INPUT_FILES = [CANON_PY]
if S84_W2_WP.exists():
    INPUT_FILES.append(S84_W2_WP)


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                            # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins: dict[str, str] = {}                                       # (local)
    for p in inputs:
        sha = sha256_of(p)                                          # (local)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = p.name                                            # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    script_bytes = script_path.read_bytes() if script_path.exists() else b""
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")
    h_audit = hashlib.sha256()                                      # (local)
    h_audit.update(script_bytes); h_audit.update(canonical_bytes); h_audit.update(pinmap_json)
    h_content = hashlib.sha256()                                    # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def compute() -> dict:
    # Plan hypothesis: r_max = min(r_L1, r_L2) over adjacent layers
    min_of_layers = min(R_L1_ZETA, R_L2_ZUBAREV)                    # (local) = 1.0

    # Residual: |canonical - predicted_by_theorem|
    abs_residual = abs(R_MAX_CANONICAL - min_of_layers)             # (local) = 13321.0
    rel_residual = abs_residual / R_MAX_CANONICAL                    # (local) ~0.99992

    # OOM gap between L1 and L2
    oom_gap = np.log10(R_L1_ZETA / R_L2_ZUBAREV)                    # (local) = 4.124
    is_two_valued = (R_L1_ZETA != R_L2_ZUBAREV)                     # (local) True

    return {
        "value": rel_residual,
        "r_L1_zeta": R_L1_ZETA,
        "r_L2_Zubarev": R_L2_ZUBAREV,
        "r_max_canonical": R_MAX_CANONICAL,
        "min_of_layers": min_of_layers,
        "abs_residual": abs_residual,
        "rel_residual": rel_residual,
        "oom_gap_L1_L2": oom_gap,
        "is_two_valued_at_interface": is_two_valued,
    }


def evaluate_gate(res: dict) -> str:
    r = res["abs_residual"]                                         # (local)
    if r < PASS_RESID:
        return "PASS"
    # Plan threshold: any residual > 0 means FAIL (THEOREM discipline)
    return "FAIL"


def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def append_verdict(verdict: str, value, audit_sha: str, content_sha: str) -> None:
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


def write_disposition_md(res: dict, audit_sha: str, content_sha: str,
                         out_path: Path) -> None:
    text = f"""# r_max layer-interface theorem candidate — disposition

**Gate**: {GATE_ID}

## Source data (S84 W2-19 carry-forward; S82 W2-2 canonical)

Row #13 r_max from S82 UNIFIED-BACKREACT-79 is layer-dependent:

| Layer | Regulator / role | r_max value |
|:------|:-----------------|:------------|
| L1 (inspection) | zeta regulator, backreaction cap | {res['r_L1_zeta']:,.0f} |
| L2 (substrate action) | Zubarev, sc-saturation cap | {res['r_L2_Zubarev']:.1f} |
| Canonical (as reported in S82 W2-2) | zeta L1 | **{res['r_max_canonical']:,.0f}** |

OOM gap between L1 and L2: **{res['oom_gap_L1_L2']:.3f}** (four orders of magnitude).

## Plan's layer-interface theorem candidate

**Claim**: r_max(k) = min(r_N(k), r_{{N+1}}(k)) across adjacent corridor layers, to machine epsilon.

**Test**:
- min(r_L1, r_L2) = min({res['r_L1_zeta']:,.0f}, {res['r_L2_Zubarev']:.1f}) = **{res['min_of_layers']:.1f}**
- r_max_canonical = **{res['r_max_canonical']:,.0f}**
- |r_max − min| = **{res['abs_residual']:,.1f}**
- relative residual = {res['rel_residual']:.5f}

Threshold: PASS iff |residual| < 1e-12 (THEOREM = machine epsilon). Fails by **13321** (4 OOM).

## Verdict: **FAIL** (plan's theorem candidate does not hold)

The min-adjacent-layer identity is NOT the correct structural statement
for r_max. The actual structural property (per S84 W2-19 synthesis):

> "r_max is genuinely two-valued at the layer interface."

That is: r_max takes DIFFERENT values under L1 (zeta inspection → 13322)
vs L2 (Zubarev substrate-action saturation → 1.0). It is NOT a pinned
scalar obeying a min-identity; it is a **layer-observable-multiplicity**.
Promoting this TRUE statement to a theorem requires its own registration
with the "two-valued at interface" phrasing, NOT the plan's min-identity.

## Structural inference

The S84 synthesis-collation already documents this:
> "The §VII.N theorem is anchored as L_max-independent and substrate-
> independent in scope, but with two structural exceptions
> (r_max layer-interface, a_2-cluster meta-observable)."

r_max is one of the two STRUCTURAL EXCEPTIONS to the three-layer
regulator theorem — explicitly flagged as an interface observable,
not a universal invariant. The plan's min-identity hypothesis was
trying to collapse the two-valuedness into a single invariant; the
audit shows that collapse fails by 4 OOM.

## Carry-forward

- Register the ALTERNATIVE theorem: "r_max is two-valued at L1/L2
  layer interface; canonical depends on layer choice" — a
  convention-dependent observable, not a universal invariant.
- Downstream: any gate consuming r_max must pin layer choice (L1 or L2)
  in its machinery pin.

## Provenance

- audit_sha256:   {audit_sha}
- content_sha256: {content_sha}
- schema_version: S84+
"""
    out_path.write_text(text, encoding="utf-8")
    print(f"  MD written: {out_path.name}")


def make_plot(res: dict, out_path: Path) -> None:
    fig, ax = plt.subplots(figsize=(9.0, 5.4))                      # (local)
    labels = ["L1 (zeta)", "L2 (Zubarev)", "r_max_canonical", "min(L1,L2)\n(plan hypothesis)"]
    vals = [res["r_L1_zeta"], res["r_L2_Zubarev"],
            res["r_max_canonical"], res["min_of_layers"]]
    colors = ["#b03030", "#2a7a2a", "#1a5fb4", "#b06530"]
    ax.bar(labels, vals, color=colors, alpha=0.85)
    ax.set_yscale("log")
    ax.set_ylabel(r"$r_{\max}$ (backreaction amplitude ratio)")
    ax.set_title(rf"{GATE_ID}: plan hypothesis FAILS (|r_max - min| = "
                 rf"{res['abs_residual']:,.0f}, {res['oom_gap_L1_L2']:.1f} OOM gap)")
    for i, v in enumerate(vals):
        ax.text(i, v * 1.25, f"{v:,.1f}" if v >= 1 else f"{v:.3f}",
                ha="center", fontsize=9)
    ax.grid(True, alpha=0.3, axis="y", which="both")
    fig.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)
    print(f"  PNG written: {out_path.name}")


def main() -> int:
    t0 = time.time()                                                # (local)

    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()                          # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANON_PY, pins)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print()

    res = compute()
    verdict = evaluate_gate(res)

    print("=== Substitution chain (Python-verified) ===")
    print(f"  Step 1: S82 W2-2 / S84 W2-19 layer values:")
    print(f"          r_L1 (zeta inspection)        = {res['r_L1_zeta']}")
    print(f"          r_L2 (Zubarev substrate-action) = {res['r_L2_Zubarev']}")
    print(f"          r_max_canonical (S82 W2-2 reported) = {res['r_max_canonical']}")
    print(f"  Step 2: Plan theorem candidate: r_max = min(r_L1, r_L2)")
    print(f"          min = min({res['r_L1_zeta']}, {res['r_L2_Zubarev']}) = {res['min_of_layers']}")
    print(f"  Step 3: residual = |{res['r_max_canonical']} - {res['min_of_layers']}| = {res['abs_residual']}")
    print(f"          relative = {res['rel_residual']:.5f}")
    print(f"  Step 4: OOM gap L1/L2: {res['oom_gap_L1_L2']:.3f}")
    print(f"  Step 5: Threshold PASS < {PASS_RESID:.0e} (machine eps).")
    print(f"          {res['abs_residual']} > {PASS_RESID:.0e} ==> {verdict}")
    print()

    np.savez(
        OUT_NPZ,
        r_L1_zeta=np.float64(res["r_L1_zeta"]),
        r_L2_Zubarev=np.float64(res["r_L2_Zubarev"]),
        r_max_canonical=np.float64(res["r_max_canonical"]),
        min_of_layers=np.float64(res["min_of_layers"]),
        abs_residual=np.float64(res["abs_residual"]),
        rel_residual=np.float64(res["rel_residual"]),
        oom_gap_L1_L2=np.float64(res["oom_gap_L1_L2"]),
        is_two_valued_at_interface=np.array(res["is_two_valued_at_interface"]),
        audit_sha256=np.array(audit_sha),
        content_sha256=np.array(content_sha),
    )
    print(f"  NPZ written: {OUT_NPZ.name}")

    write_disposition_md(res, audit_sha, content_sha, OUT_MD)
    make_plot(res, OUT_PNG)

    tag = emit_4tuple(res["rel_residual"], SCHEME, CONVENTION, L_MAX)
    print(tag)
    append_verdict(verdict, res["rel_residual"], audit_sha, content_sha)

    wall = time.time() - t0                                         # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
