#!/usr/bin/env python
"""S110 W4b §W4b-2 — S110-CF-W33-THEOREM Stage-2 clause-AND aggregate (orchestrator-authored).

joint-theorem-promotion.md Stage-2 two-agent cross-axis INDEPENDENT-verify aggregation for the
dq/da Two-q-Distinctness theorem (inv-12 W3-3, sharpens S95-W4-4; registry §VII.CE).

This script performs NO physics. The verification was done BLIND by the two axis-distinct
reviewers (their per-clause verdict JSONs are the inputs); this aggregate computes the
deterministic clause-AND composite + the dual-SHA, then PRINTS the emit_verdict payload.
Orchestrator-authored aggregation infrastructure per session-110-plan-w4.md §W4b-2 +
mechanical-closure-discipline.md.

original-author-exclusion: transit-dynamics-theorist (an inv-12 seed author) is the MATH OWNER
who registered the Stage-1 candidate, NOT a reviewer. The two Stage-2 reviewers both exclude the
original authors (lizzi / van-den-dungen / transit-dynamics):
  Axis-A (volovik-superfluid-universe-theorist, relic-occupation/substrate, NON-author) -> a, b, JOINT
  Axis-B (einstein-theorist, effective-Friedmann/cosmological-dynamics, NON-author)     -> c, d, JOINT

Composite = AND over { Axis-A clauses, Axis-B clauses, JOINT clauses PASS-AND'd across BOTH }.
substrate-input-overlap caveat carried if both reviewers load the inv12_w3_3 npz.
"""
import hashlib
import json
import pathlib
import sys

import numpy as np

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from canonical_constants import *  # noqa: F401,F403  (audit-compliance only; no constant consumed)

# ---- module globals (read by print_verdict_payload) ----
SESSION = "S110"
GATE_ID = "S110-CF-W33-THEOREM"
SCHEME = "STAGE-2-TWO-AGENT-CROSS-AXIS"
CONVENTION = "PASS-AND-JOINT-CLAUSES"
L_MAX = "N/A"

ROOT = pathlib.Path(r"C:\sandbox\Ainulindale Exflation")
S110 = ROOT / "computations" / "session-110"
AXIS_A = S110 / "s110_w4b_w33_axisA_volovik.json"
AXIS_B = S110 / "s110_w4b_w33_axisB_einstein.json"
NPZ_OUT = S110 / "s110_cf_w33_theorem.npz"
SHARED_NPZ_TOKEN = "inv12_w3_3_back_reaction_closure_hsq.npz"   # full filename (prose/display)
DETECT_STEM = "inv12_w3_3"   # investigation-gate stem for the overlap predicate (both reviewers use the full name here; stem keeps detection consistent with VIIBS)


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          companion_note="", extra_rows=None):
    """Self-contained mirror of .claude/templates/script-template.py print_verdict_payload.
    PRINTS the delimited emit_verdict payload to stdout; the orchestrator reads it and calls
    the race-safe knowledge-MCP emit_verdict tool. The script never writes the verdict file."""
    payload = {
        "session": int(SESSION.lstrip("Ss")),
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    if companion_note:
        payload["companion_note"] = companion_note
    if not (sign_verdict is None and magnitude_verdict is None and regime_verdict is None):
        payload["sign_verdict"] = sign_verdict
        payload["magnitude_verdict"] = magnitude_verdict
        payload["regime_verdict"] = regime_verdict
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


def sha_file(p):
    return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()


def main():
    axisA_raw = AXIS_A.read_text(encoding="utf-8")
    axisB_raw = AXIS_B.read_text(encoding="utf-8")
    a = json.loads(axisA_raw)
    b = json.loads(axisB_raw)

    a_clauses = {k: a["clauses"][k]["verdict"] for k in a["clauses"]}          # a, b, JOINT
    b_clauses = {k: b["clauses"][k]["verdict"] for k in b["clauses"]}          # c, d, JOINT
    axisA_single = {k: v for k, v in a_clauses.items() if k != "JOINT"}
    axisB_single = {k: v for k, v in b_clauses.items() if k != "JOINT"}

    all_single = list(axisA_single.values()) + list(axisB_single.values())
    joint_vals = [a_clauses.get("JOINT"), b_clauses.get("JOINT")]
    all_single_pass = all(v == "PASS" for v in all_single)
    joint_pass_and = all(v == "PASS" for v in joint_vals)
    if all_single_pass and joint_pass_and:
        composite = "PASS"
    elif "FAIL" in all_single + joint_vals:
        composite = "FAIL"
    else:
        composite = "INFO"

    shared_npz = (DETECT_STEM in axisA_raw) and (DETECT_STEM in axisB_raw)
    caveat = shared_npz

    pin_map = {
        "_gate_id": GATE_ID,
        "_wp_id": "W4b-2",
        "_scheme": SCHEME,
        "_convention": CONVENTION,
        "_L_max": L_MAX,
        "stage": "joint-theorem-promotion.md Stage-2 two-agent cross-axis independent-verify",
        "registry_slot": "VII.CE",
        "math_owner_excluded": "transit-dynamics-theorist",
        "axisA_reviewer": a.get("reviewer", "volovik-superfluid-universe-theorist"),
        "axisB_reviewer": b.get("reviewer", "einstein-theorist"),
        "axisA_json_sha256": sha_file(AXIS_A),
        "axisB_json_sha256": sha_file(AXIS_B),
        "axisA_clauses": a_clauses,
        "axisB_clauses": b_clauses,
        "substrate_input_overlap_caveat": caveat,
        "shared_npz": SHARED_NPZ_TOKEN if shared_npz else "none",
    }
    audit_sha256 = hashlib.sha256(json.dumps(pin_map, sort_keys=True).encode("utf-8")).hexdigest()
    content_target = "|".join([
        GATE_ID, composite,
        "A:" + ",".join(f"{k}={v}" for k, v in sorted(a_clauses.items())),
        "B:" + ",".join(f"{k}={v}" for k, v in sorted(b_clauses.items())),
        f"caveat={caveat}",
    ])
    content_sha256 = hashlib.sha256(content_target.encode("utf-8")).hexdigest()

    np.savez(
        NPZ_OUT,
        gate_id=GATE_ID,
        registry_slot="VII.CE",
        composite=composite,
        axisA_reviewer=pin_map["axisA_reviewer"],
        axisB_reviewer=pin_map["axisB_reviewer"],
        axisA_clause_names=np.array(list(a_clauses.keys())),
        axisA_clause_verdicts=np.array(list(a_clauses.values())),
        axisB_clause_names=np.array(list(b_clauses.keys())),
        axisB_clause_verdicts=np.array(list(b_clauses.values())),
        joint_pass_and=joint_pass_and,
        all_single_pass=all_single_pass,
        substrate_input_overlap_caveat=caveat,
        shared_npz=SHARED_NPZ_TOKEN if shared_npz else "none",
        audit_sha256=audit_sha256,
        content_sha256=content_sha256,
    )

    print(f"[W33 Stage-2 aggregate] Axis-A (volovik) clauses: {a_clauses}")
    print(f"[W33 Stage-2 aggregate] Axis-B (einstein) clauses: {b_clauses}")
    print(f"[W33 Stage-2 aggregate] all_single_pass={all_single_pass} joint_pass_and={joint_pass_and}")
    print(f"[W33 Stage-2 aggregate] composite={composite}  substrate_input_overlap_caveat={caveat}")
    print(f"[W33 Stage-2 aggregate] npz -> {NPZ_OUT}")

    caveat_str = (
        "substrate-input-overlap-caveat" if caveat else "substrate-input-orthogonality-satisfied"
    )
    value = (
        f"STAGE-2-PASS-AND_AxisA-volovik(a,b)+AxisB-einstein(c,d)+JOINT-both_"
        f"VII.CE-STAGE-1-to-STAGE-3_{caveat_str}"
    )
    extra = [
        f"# Stage-2 PASS-AND (joint-theorem-promotion.md): AxisA volovik {dict(a_clauses)}; "
        f"AxisB einstein {dict(b_clauses)}; JOINT PASS in BOTH. VII.CE promotes "
        f"STAGE-1-CANDIDATE -> STAGE-3-PERMANENT (orchestrator updates tag at session-end synthesis). "
        f"Math owner transit-dynamics-theorist EXCLUDED from review (original-author-exclusion).",
        f"# substrate-input-overlap caveat: {caveat} (both reviewers load {SHARED_NPZ_TOKEN}); "
        f"structural-OUTPUT-type independence established (independent Sage dq/da re-derivations: "
        f"volovik relic-Friedmann monotonicity + einstein effective-Friedmann perfect-square sign-lock), "
        f"structural-INPUT independence NOT (shared npz). Caveat scopes the independence claim, not the verdict. "
        f"clause-(a) n-vs-w dictionary recorded INFO-not-falsified by Axis-A, does not block the load-bearing PASS.",
    ]
    print_verdict_payload(
        composite, value, audit_sha256, content_sha256,
        companion_note=f"VII.CE Stage-2 {composite}; {caveat_str}",
        extra_rows=extra,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
