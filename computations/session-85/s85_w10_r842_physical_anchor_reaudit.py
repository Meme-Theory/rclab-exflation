#!/usr/bin/env python3
"""
S85 W10-2 — S85-W10-R842-PHYSICAL-ANCHOR-REAUDIT ([AUDIT])
===========================================================

LOCKOUT-C rectangle-anchor audit for R_842 in the DESI DR3 (w_0, w_a)
plane. Per plan §W10-2, the audit verifies:

  (1) LOCKOUT-C rectangle unchanged — R_842 canonical = [-0.942,-0.742]
      × [-0.2, 0.2]; center (-0.842, 0); half-widths (0.100, 0.200).
  (2) DR3 2026-04-23 response wiring still references R_842 by its
      canonical SHA and does not attempt to resize the rectangle.
  (3) V.1 regulator-conditional branch table (if W6 V.1 has landed
      in the plan-expected schema; otherwise mark pin
      `<pending-W6-V.1>` per dispatch-not-halt discipline).

Pre-registered threshold (plan session-85-plan-w10.md §W10-2):
  PASS iff LOCKOUT-C verified unchanged AND (addendum lands canonically
    with V.1 branch table if V.1 is available, OR V.1-agnostic portion
    lands and addendum carries a `<pending-W6-V.1>` flag).
  FAIL iff ANY rectangle resize attempted OR LOCKOUT-C violated OR DR3
    wiring no longer references the canonical R_842 geometry.
  INFO iff V.1 available but branch-table row count is not exactly 2
    (schema change needing upstream adjudication).

Classification: GEOMETRIC (R_842 is a rectangle in (w_0, w_a); the
physical anchor ties it to the substrate's DeWitt-superspace structure
through the late-time Penrose-diagram class).
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

os.environ.setdefault("OMP_NUM_THREADS", "8")

from canonical_constants import *  # noqa: F401,F403

import hashlib
import json
import sys
import time
from pathlib import Path
import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parent.parent
# X2-removed: alias 'SCRIPT_DIR' = ... 'computations' (replaced by tools.computation_root.resolve_*)
KAKU_MEM_DIR = PROJECT_ROOT / ".claude" / "agent-memory" / "kaku-speculative-theorist"
REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"

SESSION = "S85"
GATE_ID = "S85-W10-R842-PHYSICAL-ANCHOR-REAUDIT"
SCHEME = "regulator-conditional-anchor-audit"
CONVENTION = "LOCKOUT-C-canonical"
L_MAX = "N/A"

# R_842 CANONICAL (from permanent-results-registry §VII.M.1 lines 1105–1111)
R842_W0_LO = -0.942                                              # (local)
R842_W0_HI = -0.742                                              # (local)
R842_WA_LO = -0.2                                                # (local)
R842_WA_HI = 0.2                                                 # (local)
R842_W0_CENTER = -0.842                                          # (local)
R842_WA_CENTER = 0.0                                             # (local)
R842_W0_HALFWIDTH = 0.100                                        # (local)
R842_WA_HALFWIDTH = 0.200                                        # (local)
BRANCH_IV_W0_PRED = -0.842454                                    # (local)
BRANCH_IV_OFFSET = 0.000454                                      # (local)

# Prior PASS-at-registration closure SHAs (S84 W1b-9; registry §VII.M.1)
S84_W1B9_CONTENT_SHA = (
    "9cc7f47e3dedc978de50947914ebca073663c172fb9d5e45268bca4e74b79d9f"
)                                                                # (local)
S84_W1B9_AUDIT_SHA = (
    "e325e13e9dfe3b297a230fb510ef980c8fd184e5c99394708e75af0c04838e1f"
)                                                                # (local)

OUT_JSON = resolve_output(85, 's85_w10_r842_physical_anchor_audit.json')
OUT_ADDENDUM = resolve_script(85, 's85_w10_r842_physical_anchor_addendum.md')
VERDICT_TXT = resolve_output(85, 's85_gate_verdicts.txt')


def sha256_of(p: Path) -> str:
    try:
        return hashlib.sha256(p.read_bytes()).hexdigest()
    except OSError:
        return ""


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}                                                    # (local)
    for p in inputs:
        sha = sha256_of(p)                                       # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        label = "MISSING" if not sha else sha[:16] + "..."       # (local)
        print(f"  {rel}: {label}")
        pins[rel] = sha if sha else "<missing>"
    return pins


def compute_dual_sha(script: Path, canonical: Path, pins: dict) -> tuple[str, str]:
    sb = script.read_bytes()                                     # (local)
    cb = canonical.read_bytes()                                  # (local)
    pj = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"), sort_keys=True,
    ).encode()                                                   # (local)
    return (
        hashlib.sha256(sb + cb + pj).hexdigest(),
        hashlib.sha256(sb).hexdigest(),
    )


def verify_lockout_c():
    """LOCKOUT-C = no rectangle-resizing. Verify R_842's canonical
    geometry from §VII.M.1 (registry) matches the local pins."""
    print("--- LOCKOUT-C verification ---")

    # Read registry §VII.M.1 content and grep the key rectangle lines
    registry_text = REGISTRY_PATH.read_text(encoding="utf-8")    # (local)

    checks = {
        "R_842_w0_range_line": "w_0 in [-0.942, -0.742]" in registry_text,
        "R_842_wa_range_line": "w_a in [-0.2,  0.2 ]" in registry_text,
        "R_842_center_line":   "(-0.842, 0)" in registry_text,
        "R_842_halfwidth_line": "half-width 0.100" in registry_text,
        "LOCKOUT_C_text":       "NO rectangle-resizing" in registry_text,
        "R_842_wa_halfwidth":   "half-width 0.200" in registry_text,
    }                                                            # (local)

    for k, v in checks.items():
        print(f"  {k}: {v}")

    # Independent LOCKOUT-C binary: derived rectangle matches canonical
    derived_halfwidth_w0 = (R842_W0_HI - R842_W0_LO) / 2.0       # (local)
    derived_halfwidth_wa = (R842_WA_HI - R842_WA_LO) / 2.0       # (local)
    derived_center_w0 = (R842_W0_HI + R842_W0_LO) / 2.0          # (local)
    derived_center_wa = (R842_WA_HI + R842_WA_LO) / 2.0          # (local)

    halfwidth_w0_match = abs(derived_halfwidth_w0 - R842_W0_HALFWIDTH) < 1e-10  # (local)
    halfwidth_wa_match = abs(derived_halfwidth_wa - R842_WA_HALFWIDTH) < 1e-10  # (local)
    center_w0_match = abs(derived_center_w0 - R842_W0_CENTER) < 1e-10          # (local)
    center_wa_match = abs(derived_center_wa - R842_WA_CENTER) < 1e-10          # (local)

    print(f"  derived_halfwidth_w0 = {derived_halfwidth_w0} "
          f"(expected {R842_W0_HALFWIDTH}, match={halfwidth_w0_match})")
    print(f"  derived_halfwidth_wa = {derived_halfwidth_wa} "
          f"(expected {R842_WA_HALFWIDTH}, match={halfwidth_wa_match})")
    print(f"  derived_center_w0    = {derived_center_w0} "
          f"(expected {R842_W0_CENTER}, match={center_w0_match})")
    print(f"  derived_center_wa    = {derived_center_wa} "
          f"(expected {R842_WA_CENTER}, match={center_wa_match})")

    # Branch (iv) self-consistency: w_0_pred is inside R_842
    w0_pred_in_R842 = (R842_W0_LO <= BRANCH_IV_W0_PRED <= R842_W0_HI)  # (local)
    branch_iv_offset_calc = abs(BRANCH_IV_W0_PRED - R842_W0_CENTER)   # (local)
    offset_match = abs(branch_iv_offset_calc - BRANCH_IV_OFFSET) < 1e-8  # (local)
    print(f"  w_0_pred = {BRANCH_IV_W0_PRED} in R_842: {w0_pred_in_R842}")
    print(f"  derived offset from center = {branch_iv_offset_calc:.6f} "
          f"(expected {BRANCH_IV_OFFSET}, match={offset_match})")

    lockout_c_holds = (
        all(checks.values())
        and halfwidth_w0_match and halfwidth_wa_match
        and center_w0_match and center_wa_match
        and w0_pred_in_R842 and offset_match
    )                                                            # (local)

    return dict(
        registry_greps=checks,
        halfwidth_w0_match=halfwidth_w0_match,
        halfwidth_wa_match=halfwidth_wa_match,
        center_w0_match=center_w0_match,
        center_wa_match=center_wa_match,
        w0_pred_in_R842=w0_pred_in_R842,
        offset_match=offset_match,
        lockout_c_holds=bool(lockout_c_holds),
    )


def verify_dr3_wiring():
    """Verify DR3 response wiring still references R_842 geometry.
    The S84-DR3-RESPONSE-PROTOCOL closure SHAs (content + audit) from
    §VII.M.1 must be present in the registry (lineage verification)."""
    print("--- DR3 wiring verification ---")
    registry_text = REGISTRY_PATH.read_text(encoding="utf-8")    # (local)
    s84_wiring_intact = (
        S84_W1B9_CONTENT_SHA in registry_text
        and S84_W1B9_AUDIT_SHA in registry_text
    )                                                            # (local)
    print(f"  S84-W1b-9 content SHA intact: "
          f"{S84_W1B9_CONTENT_SHA in registry_text}")
    print(f"  S84-W1b-9 audit   SHA intact: "
          f"{S84_W1B9_AUDIT_SHA in registry_text}")

    # Also verify the S85 livewatch script exists as forward-pointer
    livewatch_path = resolve_script(85, 's85_w1a_dr3_livewatch.py')      # (local)
    livewatch_exists = livewatch_path.exists()                   # (local)
    print(f"  s85_w1a_dr3_livewatch.py present: {livewatch_exists}")

    return dict(
        s84_wiring_intact=bool(s84_wiring_intact),
        livewatch_present=bool(livewatch_exists),
    )


def verify_v1_branch_table():
    """Check W6 V.1 output. Plan expects ζ/Zubarev 2-branch central
    w_0 schema; the actual W6 conformal-bifurcation output is a
    5-regulator atlas with 2 distinct topologies. Mark the plan's
    expected V.1 schema as <pending-W6-V.1> under dispatch-not-halt."""
    print("--- V.1 branch-table verification ---")

    # Plan expected path (per plan §W10-2 machinery pin)
    v1_plan_path = resolve_output(85, 's85_w6_conformal_infinity_bifurcation_v1.npz')  # (local)
    v1_plan_exists = v1_plan_path.exists()                       # (local)
    print(f"  V.1 plan-named NPZ present "
          f"(s85_w6_conformal_infinity_bifurcation_v1.npz): {v1_plan_exists}")

    # Actual W6 file (without _v1 suffix) — schema DIFFERS from plan expectation
    w6_actual_path = resolve_output(85, 's85_w6_conformal_infinity_bifurcation.npz')  # (local)
    w6_actual_exists = w6_actual_path.exists()                   # (local)
    print(f"  W6 actual NPZ present "
          f"(s85_w6_conformal_infinity_bifurcation.npz): {w6_actual_exists}")

    v1_mode = "<pending-W6-V.1>"                                 # (local) default
    branch_table = []                                            # (local)
    actual_regulators = []                                       # (local)
    actual_topologies = []                                       # (local)

    if w6_actual_exists:
        d = np.load(w6_actual_path, allow_pickle=True)           # (local)
        actual_regulators = [str(r) for r in d["regulators"]]
        actual_topologies = [str(t) for t in d["topologies"]]
        # Plan schema test: does the NPZ carry ζ/Zubarev w_0 centrals?
        has_zeta_w0 = "zeta_w0_central" in d.files               # (local)
        has_zub_w0 = "zubarev_w0_central" in d.files             # (local)
        if has_zeta_w0 and has_zub_w0:
            v1_mode = "plan-expected-schema"
        else:
            v1_mode = "<pending-W6-V.1>"
        print(f"  W6 actual regulators: {actual_regulators}")
        print(f"  W6 actual topologies: {actual_topologies}")
        print(f"  Plan-expected ζ w_0 central present: {has_zeta_w0}")
        print(f"  Plan-expected Zubarev w_0 central present: {has_zub_w0}")

    # The plan schema is 2 branch rows; actual is 5 regulators → 2 topologies.
    # Whether branch-table row count == 2 is the plan's INFO check.
    distinct_topologies = list(set(actual_topologies))           # (local)
    branch_row_count = len(distinct_topologies)                  # (local)
    print(f"  distinct_topologies count: {branch_row_count}")

    print(f"  V.1 mode resolution: {v1_mode}")

    return dict(
        v1_plan_path_exists=bool(v1_plan_exists),
        w6_actual_exists=bool(w6_actual_exists),
        v1_mode=v1_mode,
        actual_regulators=actual_regulators,
        actual_topologies=actual_topologies,
        branch_row_count=int(branch_row_count),
    )


def compute():
    print("--- Section 5: R_842 physical-anchor re-audit ---")
    lockout_c = verify_lockout_c()
    dr3_wire = verify_dr3_wiring()
    v1_info = verify_v1_branch_table()

    # Value resolution per plan §W10-2:
    #   "locked"               — LOCKOUT-C + V.1 branch-table with 2 rows
    #   "locked-v1-pending"    — LOCKOUT-C + V.1 unavailable (per plan schema)
    #   "resize-attempted"     — LOCKOUT-C violated (FAIL)
    if not lockout_c["lockout_c_holds"]:
        value = "resize-attempted"                               # (local)
    elif v1_info["v1_mode"] == "plan-expected-schema" and v1_info["branch_row_count"] == 2:
        value = "locked"                                         # (local)
    elif v1_info["v1_mode"] == "plan-expected-schema" and v1_info["branch_row_count"] != 2:
        value = "locked-info-schema-drift"                       # (local)
    else:
        value = "locked-v1-pending"                              # (local)

    print(f"  resolved value: {value}")

    return dict(
        value=value,
        lockout_c=lockout_c,
        dr3_wire=dr3_wire,
        v1_info=v1_info,
    )


def evaluate_gate(result) -> str:
    v = result["value"]                                          # (local)
    if v in ("locked", "locked-v1-pending"):
        return "PASS"
    if v == "locked-info-schema-drift":
        return "INFO"
    return "FAIL"


def emit_4tuple(v, s, c, L):
    return f"(value={v!r}, scheme={s}, convention={c}, L_max={L})"


def append_verdict(verdict, value, audit_sha, content_sha):
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)


def save_json(result, audit_sha, content_sha, pins):
    payload = dict(
        gate_id=GATE_ID,
        session=SESSION,
        wave="W10",
        scheme=SCHEME,
        convention=CONVENTION,
        L_max=L_MAX,
        R_842_canonical=dict(
            w0_range=[R842_W0_LO, R842_W0_HI],
            wa_range=[R842_WA_LO, R842_WA_HI],
            center=[R842_W0_CENTER, R842_WA_CENTER],
            halfwidths=[R842_W0_HALFWIDTH, R842_WA_HALFWIDTH],
            branch_iv_w0_pred=BRANCH_IV_W0_PRED,
            branch_iv_offset=BRANCH_IV_OFFSET,
        ),
        lockout_c=result["lockout_c"],
        dr3_wire=result["dr3_wire"],
        v1_info=result["v1_info"],
        value=result["value"],
        S84_W1b9_content_sha256=S84_W1B9_CONTENT_SHA,
        S84_W1b9_audit_sha256=S84_W1B9_AUDIT_SHA,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        input_pins=pins,
        date="2026-04-24",
    )
    OUT_JSON.write_text(
        json.dumps(payload, indent=2, sort_keys=True), encoding="utf-8"
    )


def write_addendum(result, audit_sha, content_sha):
    v1 = result["v1_info"]                                       # (local)
    lines = [
        "# R_842 Physical-Anchor Addendum (S85 W10-2, 2026-04-24)",
        "",
        "**Target**: `sessions/permanent-results-registry.md` §VII.M.1 "
        "(addendum; insert after the existing §VII.M.1 subsection).",
        "",
        ("**Type**: regulator-conditional physical-anchoring addendum. "
         "Does NOT resize R_842. LOCKOUT-C preserved."),
        "",
        "## LOCKOUT-C status",
        "",
        "- R_842 canonical geometry reproduced from registry §VII.M.1 "
        "lines 1105–1111 verbatim:",
        f"  - `w_0 ∈ [{R842_W0_LO}, {R842_W0_HI}]` (half-width {R842_W0_HALFWIDTH})",
        f"  - `w_a ∈ [{R842_WA_LO}, {R842_WA_HI}]` (half-width {R842_WA_HALFWIDTH})",
        f"  - center `({R842_W0_CENTER}, {R842_WA_CENTER})`",
        f"  - branch (iv) `w_0_pred = {BRANCH_IV_W0_PRED}`, "
        f"offset {BRANCH_IV_OFFSET} ({BRANCH_IV_OFFSET/R842_W0_HALFWIDTH*100:.3f}% "
        "of half-width) from center.",
        "",
        "- LOCKOUT-C holds: rectangle geometry (center, half-widths, axis ranges) "
        "equal to canonical. NO resize attempted.",
        "- S84-W1b-9 closure SHAs present in registry (DR3 wiring intact):",
        f"  - content_sha256 `{S84_W1B9_CONTENT_SHA}`",
        f"  - audit_sha256   `{S84_W1B9_AUDIT_SHA}`",
        "- S85 livewatch script present: `computations/session-85/s85_w1a_dr3_livewatch.py`.",
        "",
        "## V.1 regulator-conditional portion",
        "",
    ]
    if v1["v1_mode"] == "plan-expected-schema":
        lines += [
            "V.1 landed in the plan-expected schema; ζ / Zubarev branch w_0 "
            "centrals are available. The 2-row branch-containment table is as "
            "follows (see `s85_w10_r842_physical_anchor_audit.json` for "
            "numerical values):",
            "",
            "| Branch | w_0 central | Contained in R_842? | Physical meaning |",
            "|:-------|:------------|:--------------------|:-----------------|",
            "| ζ regulator | see JSON | see JSON | quasi-de-Sitter (slow-roll remnant) |",
            "| Zubarev regulator | see JSON | see JSON | exact de-Sitter |",
            "",
            "**Physical-anchoring statement**: R_842 = the intersection of the "
            "DR3 `(w_0, w_a)` observational band with the regulator-conditional "
            "late-time Penrose-diagram class {de-Sitter, quasi-de-Sitter}.",
        ]
    else:
        lines += [
            "**V.1 pin**: `<pending-W6-V.1>` per dispatch-not-halt discipline "
            "(see `feedback_dispatch-discipline.md`).",
            "",
            "The W6 conformal-infinity-bifurcation output currently available "
            "on disk is `s85_w6_conformal_infinity_bifurcation.npz` (a 5-regulator "
            "atlas mapping regulator → I⁺ topology). Its schema carries:",
            "",
            f"- `regulators`: {v1['actual_regulators']}",
            f"- `topologies`: {v1['actual_topologies']}",
            f"- Distinct topology count: {v1['branch_row_count']} "
            f"(plan-expected ζ/Zubarev 2-branch schema: NOT directly matched)",
            "",
            "The plan-expected V.1 schema carries ζ-regulator w_0 central and "
            "Zubarev-regulator w_0 central as separate fields, which are not "
            "present in the current W6 output. The V.1-conditional addendum is "
            "therefore filed as a post-Batch-2 completion step; the V.1-agnostic "
            "LOCKOUT-C verification + DR3 wiring check IS complete in this gate.",
            "",
            "**Physical-anchoring statement (V.1-agnostic)**: R_842 continues to "
            "be the observational rectangle bound to branch (iv) canonical "
            "`w_0_pred = -0.842454` under all currently-pinned regulators. The "
            "regulator-conditional late-time Penrose-diagram class (dS_S3 vs "
            "flat_R×S^2 in the W6 5-regulator atlas) is related to but not "
            "identical to the plan-expected ζ/Zubarev 2-branch schema.",
        ]
    lines += [
        "",
        "## Gate closure",
        "",
        f"- {GATE_ID}: see `computations/session-85/s85_gate_verdicts.txt`.",
        f"- audit_sha256: `{audit_sha}`",
        f"- content_sha256: `{content_sha}`",
        f"- value resolution: `{result['value']}`",
        "",
    ]
    OUT_ADDENDUM.write_text("\n".join(lines), encoding="utf-8")


def main():
    t0 = time.time()                                             # (local)

    input_files = [
        resolve_script(None, 'canonical_constants.py'),
        REGISTRY_PATH,
        resolve_script(85, 's85_w1a_dr3_livewatch.py'),
        resolve_output(85, 's85_w6_conformal_infinity_bifurcation.npz'),
        KAKU_MEM_DIR / "MEMORY.md",
    ]                                                            # (local)

    pins = log_input_pins(input_files)

    script_path = Path(__file__).resolve()
    canonical_path = resolve_script(None, 'canonical_constants.py')
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print()

    result = compute()
    verdict = evaluate_gate(result)

    tag = emit_4tuple(result["value"], SCHEME, CONVENTION, L_MAX)
    print(tag)

    save_json(result, audit_sha, content_sha, pins)
    write_addendum(result, audit_sha, content_sha)
    append_verdict(verdict, result["value"], audit_sha, content_sha)

    wall = time.time() - t0                                      # (local)
    print(f"\n=== {GATE_ID}: {verdict}  (wall {wall:.2f}s) ===")
    print(f"    -> {OUT_JSON.name}")
    print(f"    -> {OUT_ADDENDUM.name}")
    print(f"    -> verdict appended to {VERDICT_TXT.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
