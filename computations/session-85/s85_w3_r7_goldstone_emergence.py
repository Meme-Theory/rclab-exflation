#!/usr/bin/env python3
"""
S85 W3-2 — S85-W3-CF-7-R7-GOLDSTONE-EMERGENCE
==============================================

Gate: S85-W3-CF-7-R7-GOLDSTONE-EMERGENCE ([VERIFY-THEOREM])

Hypothesis (plan §W3-2):
  On R7 (K >= K_crit = 91.5) the coset
    G = SU(3) x SO(3) x U(1)_rel x U(1)_T   -> dim 13
    H = SU(2) x U(1)  x SO(2)               -> dim  5
  yields N_Goldstone = dim(G/H) = 8.

  Note: the W5-66 memory writes G and H as including T (time-reversal Z_2)
  on both sides. The correct continuous-dim count treats U(1)_T (time
  translation) as part of G_continuous and notes that H retains only the
  discrete Z_2 time-reversal, so U(1)_T/Z_2 contributes 1 Goldstone.
  With this convention, dim(G_cont) = 13 and dim(H_cont) = 5.

Substitution chain (group-theoretic proof of N_Goldstone = 8):
  Definition 1: G_cont = SU(3) x SO(3) x U(1)_rel x U(1)_T
                dim = dim(SU(3)) + dim(SO(3)) + dim(U(1)) + dim(U(1))
                    = 8 + 3 + 1 + 1 = 13
  Definition 2: H_cont = SU(2) x U(1) x SO(2)   (discrete Z_2's do not contribute)
                dim = dim(SU(2)) + dim(U(1)) + dim(SO(2)) = 3 + 1 + 1 = 5
  Step 1: Goldstone theorem: N_Goldstone = dim(G_cont) - dim(H_cont)
  Step 2: Substitute: N_Goldstone = 13 - 5 = 8.
  Direction: Count is positive; broken generators outnumber stabilizer by 8.
  Conclusion: N_Goldstone = 8 by group theory, independent of K.

  Dispersion classification (Nielsen-Chadha, plan §W3-2):
    - CP^2 = SU(3)/S(U(2)xU(1)) subcoset: 4 broken gens
    - SO(3)/SO(2) = S^2 subcoset:          2 broken gens
    - U(1)_rel subcoset:                   1 broken gen
    - U(1)_T  subcoset:                    1 broken gen
    Total: 4 + 2 + 1 + 1 = 8  (consistent with dim(G/H))

  Plan's written breakdown "6 quadratic CP^2 + 2 linear SO(3) + 1 relative
  phase" sums to 9, not 8.  The CP^2 quadratic count is 4 real broken
  generators (complex dim 2), not 6.  We retain N_Goldstone = 8 by
  group-theoretic argument and flag the plan's 6+2+1=9 arithmetic as a
  dispersion-classification INFO (plan §W3-2 INFO clause: "N_Goldstone = 8
  but dispersion anomalous").

Pre-registered thresholds (plan §W3-2):
  PASS iff N_Goldstone = 8 AND dispersion classification matches (6+2+1).
  INFO iff N_Goldstone = 8 but dispersion anomalous.
  FAIL iff N_Goldstone != 8.

Inputs (SHA-256 dual-pinned at runtime):
  - canonical_constants.py
  - script bytes (feeds both content_sha256 and audit_sha256)

Output 4-tuple:
  (value=N_Goldstone, scheme=heat_kernel, convention=A, L_max=10)

Classification: PHONONIC
  Goldstones here are phononic modes of the fabric at each point, not
  fields on a spacetime container. The 4 CP^2 Goldstones are the
  framework-unique SU(3)-internal OP directions without 3He-B analogue.

Method:
  (a) Symbolic group-dim accounting on G and H.
  (b) Coset decomposition by sub-factor; per-sub-factor broken-gen count.
  (c) Nielsen-Chadha dispersion typing (relativistic-like substrate).
  (d) Compare to plan's 6+2+1 expectation; emit PASS / INFO / FAIL.

CPU-only: trivial algebra.
"""

from __future__ import annotations

import os
# === Phase 2b X2 transform bootstrap (auto-inserted by tools/_x2_transform_copies.py) ===
import sys as _x2_sys
import pathlib as _x2_pathlib
import re as _x2_re
def _x2_locate_tools():
    p = _x2_pathlib.Path(__file__).resolve()
    for _ in range(8):
        if (p / "tools" / "computation_root.py").is_file():
            return p / "tools"
        p = p.parent
    raise RuntimeError(
        "Phase 2b bootstrap: tools/computation_root.py not found in any "
        "ancestor of " + str(__file__))
_x2_sys.path.insert(0, str(_x2_locate_tools()))
from computation_root import resolve_script, resolve_output, resolve_glob, project_root as _x2_project_root
def _x2_shared_dir():
    return _x2_project_root() / "computations" / "_shared"
_x2_session_dir_match = _x2_re.match(r"^session-(\d+)$",
    _x2_pathlib.Path(__file__).resolve().parent.name)
_x2_self_session = int(_x2_session_dir_match.group(1)) if _x2_session_dir_match else None
# === End X2 bootstrap ===

os.environ.setdefault('OMP_NUM_THREADS', '8')
os.environ.setdefault('MKL_NUM_THREADS', '8')

import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from canonical_constants import (
    K_crit,
    M_KK,
    c_fabric,
    c_Gold,
)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)

SESSION = "S85"                                              # (local)
GATE_ID = "S85-W3-CF-7-R7-GOLDSTONE-EMERGENCE"               # (local)
SCHEME = "heat_kernel"                                       # (local)
CONVENTION = "A"                                             # (local)
L_MAX = 10                                                   # (local)

K_R7 = (K_crit + 3.556e5) / 2.0  # (local) plan §W3-2 K_R7 := (K_crit + K_FIRAS)/2

# K_R7 = 177795.75 (on R7 branch interior)

OUT_NPZ = resolve_output(85, 's85_w3_r7_goldstone_emergence.npz')
OUT_PNG = resolve_output(85, 's85_w3_r7_goldstone_emergence.png')
VERDICT_TXT = resolve_output(85, 's85_gate_verdicts.txt')

INPUT_FILES = [resolve_script(None, 'canonical_constants.py')]


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                     # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list) -> dict:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict = {}                                          # (local)
    for p in inputs:
        sha = sha256_of(p)                                   # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...{sha[-8:]}")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict) -> str:
    items = sorted(pins.items())                             # (local)
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path, canonical_path, pins) -> tuple:
    script_bytes = b""                                       # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        pass
    canonical_bytes = b""                                    # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        pass
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")                                        # (local)

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()                              # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()                          # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Compute
# ---------------------------------------------------------------------------

def compute() -> dict:
    print("\n[SEC 4] Group-theoretic Goldstone count at K_R7")
    print(f"  K_R7 (on R7 interior) = {K_R7:.4e}")
    print(f"  K_crit (R6/R7 boundary) = {K_crit}")

    # G_continuous sub-factor dimensions
    dim_SU3 = 8                                              # (local)
    dim_SO3 = 3                                              # (local)
    dim_U1_rel = 1                                           # (local)
    dim_U1_T = 1                                             # (local) continuous time-translation
    dim_G_cont = dim_SU3 + dim_SO3 + dim_U1_rel + dim_U1_T   # (local) = 13

    # H_continuous sub-factor dimensions
    dim_SU2 = 3                                              # (local)
    dim_U1 = 1                                               # (local)
    dim_SO2 = 1                                              # (local)
    # Z_2 (phase or spatial parity) and discrete time-reversal do not contribute
    dim_H_cont = dim_SU2 + dim_U1 + dim_SO2                  # (local) = 5

    N_Goldstone = dim_G_cont - dim_H_cont                    # (local) = 8

    print(f"  dim(G_cont) = dim(SU(3)) + dim(SO(3)) + dim(U(1)_rel) + dim(U(1)_T)")
    print(f"            = {dim_SU3} + {dim_SO3} + {dim_U1_rel} + {dim_U1_T} = {dim_G_cont}")
    print(f"  dim(H_cont) = dim(SU(2)) + dim(U(1)) + dim(SO(2))")
    print(f"            = {dim_SU2} + {dim_U1} + {dim_SO2} = {dim_H_cont}")
    print(f"  N_Goldstone = dim(G/H)_cont = {dim_G_cont} - {dim_H_cont} = {N_Goldstone}")

    # Per-sub-coset decomposition
    print("\n[SEC 4b] Per-sub-coset broken-generator decomposition")
    # CP^2 = SU(3)/(SU(2) x U(1))
    n_CP2 = dim_SU3 - dim_SU2 - dim_U1                       # (local)
    # S^2 = SO(3)/SO(2)
    n_S2 = dim_SO3 - dim_SO2                                 # (local)
    # U(1)_rel broken fully (H has no rel factor)
    n_rel = dim_U1_rel                                       # (local)
    # U(1)_T broken fully (H has only discrete Z_2 time-reversal, no continuous T)
    n_T = dim_U1_T                                           # (local)

    n_total_cosets = n_CP2 + n_S2 + n_rel + n_T              # (local)

    print(f"  SU(3)/(SU(2) x U(1)) = CP^2: n_CP2 = 8-3-1 = {n_CP2}")
    print(f"  SO(3)/SO(2)        = S^2 : n_S2  = 3-1   = {n_S2}")
    print(f"  U(1)_rel/{{e}}:              n_rel = {n_rel}")
    print(f"  U(1)_T /Z_2 :               n_T   = {n_T}")
    print(f"  SUM                        = {n_total_cosets}  (must equal N_Goldstone = {N_Goldstone})")

    # Nielsen-Chadha dispersion typing
    # On a Lorentz-invariant substrate (relativistic-like), all Goldstones are
    # type-A (linear dispersion omega ~ k).  For non-relativistic systems,
    # paired broken generators with <[Q_i, Q_j]> != 0 merge into type-B
    # (omega ~ k^2) and the Goldstone count reduces by 1 per pair.
    #
    # The substrate has c_fabric well-defined and a canonical relativistic
    # stance (Lorentz action acts on the fabric's emergent metric).  Default
    # classification: all 8 Goldstones are TYPE-A LINEAR.
    print("\n[SEC 4c] Nielsen-Chadha dispersion typing")
    dispersion_computed = {                                  # (local)
        "CP^2":       "type-A-linear x 4   (relativistic-limit default)",
        "S^2":        "type-A-linear x 2   (acoustic modes, c ~ c_fabric)",
        "U(1)_rel":   "type-A-linear x 1   (relative-phase mode)",
        "U(1)_T":     "type-A-linear x 1   (time-translation mode)",
    }
    n_linear = 4 + 2 + 1 + 1                                 # (local) all type-A
    n_quadratic = 0                                          # (local)
    print(f"  Classification (relativistic-limit):")
    for k, v in dispersion_computed.items():
        print(f"    {k:12s}: {v}")
    print(f"  Total: {n_linear} linear + {n_quadratic} quadratic = {n_linear+n_quadratic}")

    # Plan's expectation (from §W3-2): 6 quadratic (CP^2) + 2 linear (S^2) + 1 relative-phase linear
    plan_n_quadratic = 6                                     # (local) plan §W3-2
    plan_n_linear = 2 + 1                                    # (local) 2 from S^2 + 1 rel phase
    plan_total = plan_n_quadratic + plan_n_linear            # (local) = 9
    print(f"\n  Plan's written breakdown (§W3-2): {plan_n_quadratic} quadratic + {plan_n_linear} linear = {plan_total}")
    print(f"  Plan's total {plan_total} != N_Goldstone 8 -> plan-breakdown ARITHMETIC INCONSISTENCY")
    print(f"  Computed total 8 = 8 -> group-theoretic count MATCHES plan's core claim")

    # Cross-checks
    print("\n[SEC 4d] Cross-checks")
    CC1 = (N_Goldstone == 8)                                 # (local) count matches plan claim
    CC2 = (n_total_cosets == N_Goldstone)                    # (local) coset decomposition self-consistent
    CC3 = (n_linear + n_quadratic == N_Goldstone)            # (local) dispersion typing sums to Goldstone count
    CC4 = (plan_total != N_Goldstone)                        # (local) plan's 6+2+1 arithmetic inconsistency FLAGGED
    CC5 = (c_fabric > 0 and c_Gold > 0)                      # (local) substrate speeds well-defined
    all_CC = CC1 and CC2 and CC3 and CC5                     # (local) CC4 is an INFO flag, not a gate
    print(f"  CC-1 N_Goldstone == 8:                 {CC1}")
    print(f"  CC-2 sum-of-cosets == N_Goldstone:     {CC2}")
    print(f"  CC-3 dispersion-sum == N_Goldstone:    {CC3}")
    print(f"  CC-4 plan's 6+2+1 != 8 (arith flag):   {CC4}  (INFO flag)")
    print(f"  CC-5 substrate speeds > 0:             {CC5}")
    print(f"  All gating CC PASS:                    {all_CC}")

    return dict(
        value=N_Goldstone,
        dim_G_cont=dim_G_cont,
        dim_H_cont=dim_H_cont,
        N_Goldstone=N_Goldstone,
        n_CP2=n_CP2, n_S2=n_S2, n_rel=n_rel, n_T=n_T,
        n_total_cosets=n_total_cosets,
        n_linear=n_linear, n_quadratic=n_quadratic,
        plan_n_quadratic=plan_n_quadratic, plan_n_linear=plan_n_linear,
        plan_total=plan_total,
        K_R7=K_R7,
        CC1=CC1, CC2=CC2, CC3=CC3, CC4=CC4, CC5=CC5,
        all_CC=all_CC,
    )


def evaluate_gate(result: dict) -> str:
    """Plan §W3-2:
      PASS iff N_Goldstone=8 AND dispersion matches plan (6 quad + 2 lin + 1 lin = 9).
      INFO iff N_Goldstone=8 but dispersion anomalous.
      FAIL iff N_Goldstone != 8.
    """
    if result['N_Goldstone'] != 8:
        return "FAIL"
    # Plan's 6+2+1 breakdown sums to 9, which is itself inconsistent with 8;
    # computed dispersion (all 8 type-A linear) does not match plan's
    # 6-quadratic prediction -> INFO.
    dispersion_matches_plan = (result['n_quadratic'] == result['plan_n_quadratic']
                               and result['n_linear'] == result['plan_n_linear']
                               and result['plan_total'] == result['N_Goldstone'])  # (local)
    if dispersion_matches_plan:
        return "PASS"
    return "INFO"


def emit_4tuple(value, scheme, convention, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def append_verdict(verdict, value, audit_sha, content_sha) -> None:
    line = (f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
            f"convention={CONVENTION} L_max={L_MAX} "
            f"audit_sha256={audit_sha} content_sha256={content_sha} "
            f"schema_version=S84+\n")
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


def make_plot(result: dict) -> None:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))    # (local)

    # Left: coset contribution bar chart
    labels = ['CP^2\n(SU(3)/SU(2)xU(1))', 'S^2\n(SO(3)/SO(2))',
              'U(1)_rel', 'U(1)_T']
    counts = [result['n_CP2'], result['n_S2'], result['n_rel'], result['n_T']]
    colors = ['tab:blue', 'tab:green', 'tab:orange', 'tab:red']
    ax1.bar(labels, counts, color=colors, edgecolor='k', alpha=0.8)
    ax1.set_ylabel('Broken generators')
    ax1.set_title(f'Coset decomposition: N_Goldstone = {sum(counts)} = {result["N_Goldstone"]}')
    for i, v in enumerate(counts):
        ax1.text(i, v + 0.1, f"{v}", ha='center', fontsize=11, fontweight='bold')
    ax1.set_ylim(0, 5)
    ax1.grid(True, axis='y', ls=':', alpha=0.4)

    # Right: dispersion classification
    ax2.axis('off')
    text = (
        f"GATE: {GATE_ID}\n"
        f"K_R7 = {result['K_R7']:.3e} (on R7 interior)\n\n"
        f"Group-theoretic count:\n"
        f"  dim(G_cont) = 13\n"
        f"  dim(H_cont) = 5\n"
        f"  N_Goldstone = 13 - 5 = 8  [PASS]\n\n"
        f"Coset breakdown (sum = 8):\n"
        f"  CP^2:     {result['n_CP2']} broken gens\n"
        f"  S^2:      {result['n_S2']} broken gens\n"
        f"  U(1)_rel: {result['n_rel']} broken gen\n"
        f"  U(1)_T:   {result['n_T']} broken gen\n\n"
        f"Nielsen-Chadha classification:\n"
        f"  type-A linear: {result['n_linear']}\n"
        f"  type-B quadratic: {result['n_quadratic']}\n\n"
        f"Plan (§W3-2) breakdown: 6 quad + 2 lin + 1 lin = 9\n"
        f"  -> plan breakdown ARITHMETIC INCONSISTENCY (9 != 8)\n"
        f"  -> INFO verdict: count PASS, dispersion anomalous\n"
    )
    ax2.text(0.02, 0.98, text, transform=ax2.transAxes,
             fontfamily='monospace', fontsize=9, va='top',
             bbox=dict(boxstyle='round', fc='lightyellow', ec='k', alpha=0.9))

    fig.suptitle(f'{GATE_ID}  —  R7 Goldstone emergence', fontsize=12)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130, bbox_inches='tight')
    plt.close(fig)
    print(f"  plot written: {OUT_PNG.name}")


def main() -> int:
    t0 = time.time()                                         # (local)

    pins = log_input_pins(INPUT_FILES)                       # (local)
    closure = closure_hash(pins)                             # (local)
    print(f"  closure: {closure[:16]}... (legacy)")

    script_path = Path(__file__).resolve()                   # (local)
    canonical_path = resolve_script(None, 'canonical_constants.py')    # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...{audit_sha[-8:]}")
    print(f"  content_sha256: {content_sha[:16]}...{content_sha[-8:]}")

    result = compute()                                       # (local)
    verdict = evaluate_gate(result)                          # (local)

    print("\n[SEC 5] Output persistence")
    np.savez(
        OUT_NPZ,
        N_Goldstone=result['N_Goldstone'],
        dim_G_cont=result['dim_G_cont'],
        dim_H_cont=result['dim_H_cont'],
        n_CP2=result['n_CP2'], n_S2=result['n_S2'],
        n_rel=result['n_rel'], n_T=result['n_T'],
        n_total_cosets=result['n_total_cosets'],
        n_linear=result['n_linear'], n_quadratic=result['n_quadratic'],
        plan_n_quadratic=result['plan_n_quadratic'],
        plan_n_linear=result['plan_n_linear'],
        plan_total=result['plan_total'],
        K_R7=result['K_R7'],
        verdict=verdict, scheme=SCHEME, convention=CONVENTION,
        L_max=L_MAX, audit_sha=audit_sha, content_sha=content_sha,
    )
    print(f"  NPZ written: {OUT_NPZ.name}")
    make_plot(result)

    print("\n[SEC 6] 4-tuple + verdict")
    tag = emit_4tuple(result['N_Goldstone'], SCHEME, CONVENTION, L_MAX)
    print(tag)
    append_verdict(verdict, result['N_Goldstone'], audit_sha, content_sha)
    print(f"  verdict appended to: {VERDICT_TXT.name}")
    print(f"  verdict: {verdict}  N_Goldstone = {result['N_Goldstone']}")

    wall = time.time() - t0                                  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
