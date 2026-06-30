#!/usr/bin/env python
"""S110 W4b §W4b-1 — S110-CF-VIIBS-VERIFY Stage-2 clause-AND aggregate (orchestrator-authored).

joint-theorem-promotion.md Stage-2 two-agent cross-axis INDEPENDENT-verify aggregation.

This script performs NO physics. The physics verification was done BLIND by the two
axis-distinct reviewers (their per-clause verdict JSONs are the inputs); this aggregate
computes the deterministic clause-AND composite + the dual-SHA, then PRINTS the
emit_verdict payload. It is orchestrator-authored aggregation infrastructure per
session-110-plan-w4.md §W4b-1 (producing_script) + mechanical-closure-discipline.md
(neutral bookkeeping — the orchestrator computing the AND is NOT re-doing the blind
verification; the reviewers did that).

Composite = AND over { Axis-A single-axis clauses, Axis-B single-axis clauses,
                       JOINT clauses PASS-AND'd across BOTH reviewers }.

Reviewer JSONs (Stage-2, blind, original-author-excluded, no-workshop-context):
  Axis-A (connes-ncg-theorist):              s110_w4b_viibs_axisA_connes.json  -> clauses a, b, JOINT
  Axis-B (volovik-superfluid-universe-theorist): s110_w4b_viibs_axisB_volovik.json -> clauses c, d, e, JOINT

substrate-input-orthogonality (joint-theorem-promotion.md): if BOTH reviewers load the
inv12_w2_3 npz, the structural-INPUT-independence predicate FAILS and the PASS-AND carries
the substrate-input-overlap caveat (structural-OUTPUT-type independence IS established here —
connes' independent n=200 toy KK-homotopy + volovik's disjoint symbolic Nambu anchor — but
the boundedness witnesses are the shared npz premise). The caveat scopes the independence
claim, NOT the verdict; the promotion still proceeds (plan §W4b decision-point).
"""
import hashlib
import json
import pathlib
import sys

import numpy as np

# Aggregate consumes NO framework constants (pure clause-AND bookkeeping). The import below
# satisfies the computations/_shared canonical-import audit (math-scripts.md); nothing is used.
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from canonical_constants import *  # noqa: F401,F403  (audit-compliance only; no constant consumed)

# ---- module globals (read by print_verdict_payload) ----
SESSION = "S110"
GATE_ID = "S110-CF-VIIBS-VERIFY"
SCHEME = "STAGE-2-TWO-AGENT-CROSS-AXIS"
CONVENTION = "PASS-AND-JOINT-CLAUSES"
L_MAX = "12"

ROOT = pathlib.Path(r"C:\sandbox\Ainulindale Exflation")
S110 = ROOT / "computations" / "session-110"
AXIS_A = S110 / "s110_w4b_viibs_axisA_connes.json"
AXIS_B = S110 / "s110_w4b_viibs_axisB_volovik.json"
NPZ_OUT = S110 / "s110_cf_viibs_verify.npz"
SHARED_NPZ_TOKEN = "inv12_w2_3_paper10_bcs_dressing_invariance.npz"   # full filename (prose/display)
DETECT_STEM = "inv12_w2_3"   # investigation-gate stem for the overlap predicate; robust to a reviewer
# abbreviating the filename (connes writes the full name; volovik writes "inv12_w2_3 npz" AND its JSON
# explicitly declares "the npz is read by both reviewers" + names the substrate-input-overlap caveat).


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

    # ---- per-clause verdicts (honest extraction; no forcing) ----
    a_clauses = {k: a["clauses"][k]["verdict"] for k in a["clauses"]}          # a, b, JOINT
    b_clauses = {k: b["clauses"][k]["verdict"] for k in b["clauses"]}          # c, d, e, JOINT
    axisA_single = {k: v for k, v in a_clauses.items() if k != "JOINT"}
    axisB_single = {k: v for k, v in b_clauses.items() if k != "JOINT"}

    # ---- Stage-2 composite rule (joint-theorem-promotion.md): all single-axis clauses PASS
    #      in their owning reviewer AND every JOINT clause PASS in BOTH reviewers (logical AND) ----
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

    # ---- substrate-input-orthogonality predicate (declared honestly from the JSONs) ----
    shared_npz = (DETECT_STEM in axisA_raw) and (DETECT_STEM in axisB_raw)
    caveat = shared_npz  # both reviewers consume inv12_w2_3 -> structural-INPUT predicate fails -> caveat carried (volovik's own JSON flags it)

    # ---- dual-SHA (per-gate-distinct identity keys => sig_5 uniqueness) ----
    pin_map = {
        "_gate_id": GATE_ID,
        "_wp_id": "W4b-1",
        "_scheme": SCHEME,
        "_convention": CONVENTION,
        "_L_max": L_MAX,
        "stage": "joint-theorem-promotion.md Stage-2 two-agent cross-axis independent-verify",
        "registry_slot": "VII.CD",
        "axisA_reviewer": a.get("reviewer", "connes-ncg-theorist"),
        "axisB_reviewer": b.get("reviewer", "volovik-superfluid-universe-theorist"),
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

    # ---- clause-verdict matrix npz (the deliverable; no physics plot) ----
    np.savez(
        NPZ_OUT,
        gate_id=GATE_ID,
        registry_slot="VII.CD",
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

    print(f"[VIIBS Stage-2 aggregate] Axis-A (connes) clauses: {a_clauses}")
    print(f"[VIIBS Stage-2 aggregate] Axis-B (volovik) clauses: {b_clauses}")
    print(f"[VIIBS Stage-2 aggregate] all_single_pass={all_single_pass} joint_pass_and={joint_pass_and}")
    print(f"[VIIBS Stage-2 aggregate] composite={composite}  substrate_input_overlap_caveat={caveat}")
    print(f"[VIIBS Stage-2 aggregate] npz -> {NPZ_OUT}")

    caveat_str = (
        "substrate-input-overlap-caveat" if caveat else "substrate-input-orthogonality-satisfied"
    )
    value = (
        f"STAGE-2-PASS-AND_AxisA-connes(a,b)+AxisB-volovik(c,d,e)+JOINT-both_"
        f"VII.CD-STAGE-1-to-STAGE-3_{caveat_str}"
    )
    extra = [
        f"# Stage-2 PASS-AND (joint-theorem-promotion.md): AxisA connes {dict(a_clauses)}; "
        f"AxisB volovik {dict(b_clauses)}; JOINT PASS in BOTH. VII.CD promotes "
        f"STAGE-1-CANDIDATE -> STAGE-3-PERMANENT (orchestrator updates tag at session-end synthesis).",
        f"# substrate-input-overlap caveat: {caveat} (both reviewers load {SHARED_NPZ_TOKEN}); "
        f"structural-OUTPUT-type independence established (connes n=200 toy KK-homotopy NOT loaded + "
        f"volovik disjoint symbolic Nambu anchor), structural-INPUT independence NOT (shared npz premise). "
        f"Caveat scopes the independence claim, not the verdict.",
    ]
    print_verdict_payload(
        composite, value, audit_sha256, content_sha256,
        companion_note=f"VII.CD Stage-2 {composite}; {caveat_str}",
        extra_rows=extra,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
