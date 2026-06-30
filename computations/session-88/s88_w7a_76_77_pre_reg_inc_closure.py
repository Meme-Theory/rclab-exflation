#!/usr/bin/env python3
"""
S88 W7a-76 + W7a-77 — Mechanical PRE-REG-INC Closure
======================================================

Gates closed:
  - S88-VII-AJ-TWO-ROW-LANDING (W7a-76)
  - S88-OR-LATER-VII-AJ-INDEPENDENT-VERIFY (W7a-77)

Mechanical-closure rationale per `.claude/rules/mechanical-closure-discipline.md`:

(1) Upstream-block topology is the cause:
    - §W7a-74 (S88-W9B-2-RANK-VS-MAGNITUDE-LAYER-DISCRIMINATOR) returned
      composite verdict FAIL with sign=FAIL, magnitude=FAIL, regime=VALID;
      |ρ_S(s=4)|_TIER-1 = 0.800 < 0.999 (PASS-RANK threshold);
      spread_TIER-1 = 1.011 ≫ 0.06 (PASS-MAGNITUDE bound).
    - §W7a-76 plan §372 FAIL clause (pre-registered): "FAIL: #74 returned
      FAIL-RANK or FAIL-MAGNITUDE → §VII.AJ.1 or §VII.AJ.2 cannot land".
    - §W7a-77 plan §401 explicitly conditional: "CONDITIONAL on (#76 + #74)
      PASS"; with #74 FAIL, the chain to #77 is structurally severed.

(2) Verdict honesty:
    - Both gates emit FAIL with descriptive value-string naming the
      blocking prereq + status. NOT PASS. NOT INFO.

(3) Per-gate-distinct audit_sha256:
    - Pinmap for each gate embeds `_gate_id`, `_wp_id`, `_scheme`,
      `_convention` distinct keys; SHA-256 of canonical-serialized pinmap
      is therefore distinct between gates.

(4) Audit-trail signature:
    - value-string: `value='PRE-REG-INC_blocked_by_<sym>_<status>'`
    - companion row: cites W7a-74 verdict line by audit_sha256
      `5d7e448b7da710deb1408fbd8dd621007ff976cedc9f0fdf2a4f42c52d075378`

(5) Working-paper update in-script:
    - This script edits §W7a-76 + §W7a-77 WP sections IN THE SAME RUN as
      verdict-line append, replacing pending blocks with mechanical-
      closure Pattern C entries (FAIL with remediation, prose headers).

Plan-anticipation check:
- Plan §372 W7a-76 FAIL clause: ANTICIPATED (pre-registered in plan).
- Plan §401 W7a-77 conditional: ANTICIPATED (pre-registered in plan).
⇒ closure-as-execution-time-reporting is structurally honest, NOT post-
   hoc plan editing (PROHIBITED_ACTIONS Class 3 not triggered).

Planning-defect threshold check:
- N_PLANNING_DEFECT_THRESHOLD = 4 (per `mechanical-closure-discipline.md
  §"When mechanical closure indicates a PLANNING DEFECT"`).
- Closed-gate count this script = 2 (W7a-76 + W7a-77).
- 2 < 4 ⇒ NOT a planning-defect indicator; this is a normal upstream-
  block scenario, not over-optimistic wave partitioning.

Output 4-tuples:
  W7a-76: (value=PRE-REG-INC_blocked_by_W7a-74_FAIL-RANK_FAIL-MAGNITUDE,
           scheme=METHODOLOGY-class-registry-landing,
           convention=TWO-ROW-rank-magnitude-epistemic-split-corner-I-pole-s4,
           L_max=N/A)
  W7a-77: (value=PRE-REG-INC_blocked_by_W7a-76_FAIL_AND_W7a-74_FAIL-RANK,
           scheme=Stage-2-cross-axis-independent-verify,
           convention=corner-I-pinned-VII-AJ-1-rank-order-only,
           L_max=N/A)

Classification: METHODOLOGY (mechanical closure on upstream-blocked gates).
"""

# ---------------------------------------------------------------------------
# Section 1 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import sys
import time
from pathlib import Path

# Canonical-constants import per `.claude/rules/math-scripts.md §"Canonical
# Constants (MANDATORY)"` — required by all S34+ scripts even when the
# closure logic uses no canonical values directly. Mechanical-closure scripts
# operate on upstream verdict SHAs + structural pinmap entries, not on
# framework numerical constants, but the import is a hygiene-mandatory
# discipline marker per the rule.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "_shared"))
from canonical_constants import *  # noqa: F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Path resolution
# ---------------------------------------------------------------------------
SCRIPT_PATH = Path(__file__).resolve()
SESSION_DIR = SCRIPT_PATH.parent
PROJECT_ROOT = SCRIPT_PATH.parent.parent.parent
PLAN_PATH = PROJECT_ROOT / "sessions" / "session-plan" / "session-88-plan-w7a.md"
WP_PATH = PROJECT_ROOT / "sessions" / "session-88" / "session-88-w7a-workingpaper.md"
VERDICT_PATH = SESSION_DIR / "s88_gate_verdicts.txt"

# Upstream W7a-74 verdict audit_sha (the structural blocker for both gates)
W7A_74_AUDIT_SHA = (
    "5d7e448b7da710deb1408fbd8dd621007ff976cedc9f0fdf2a4f42c52d075378"
)  # (local) S88-W9B-2-RANK-VS-MAGNITUDE-LAYER-DISCRIMINATOR FAIL


# ---------------------------------------------------------------------------
# Section 3 — SHA helpers
# ---------------------------------------------------------------------------
def file_sha256(path):
    """SHA-256 of file bytes."""
    h = hashlib.sha256()  # (local)
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(input_pin_map):
    """SHA-256 of canonical-serialized input pin map."""
    canon = json.dumps(input_pin_map, sort_keys=True, separators=(",", ":"))  # (local)
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()


# ---------------------------------------------------------------------------
# Section 4 — Verdict-line emission
# ---------------------------------------------------------------------------
def append_verdict(gate_id, verdict, value_str, scheme, convention, L_max,
                   audit_sha, content_sha, sign_v, mag_v, regime_v,
                   closure_remediation_comment):
    """Append S84+ canonical line + W9a-99 dual-SHA companion + S87+ 3-tuple +
    closure-script-trace remediation row per `mechanical-closure-discipline.md
    §"Audit-trail signature"`."""
    canonical = (
        f"{gate_id}: {verdict} -- value='{value_str}' "
        f"scheme={scheme} convention={convention} L_max={L_max} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} schema_version=S84+\n"
    )  # (local)
    dual_companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {gate_id} dual-SHA companion row (W9a-99 split)\n"
    )  # (local)
    tuple_companion = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {gate_id} 3-tuple annotation (S87 schema-v2)\n"
    )  # (local)
    closure_companion = (
        f"# {closure_remediation_comment}\n"
    )  # (local) per mechanical-closure-discipline.md §"Audit-trail signature"
    with open(VERDICT_PATH, "a", encoding="utf-8") as f:
        f.write(canonical)
        f.write(dual_companion)
        f.write(tuple_companion)
        f.write(closure_companion)
    return canonical, dual_companion, tuple_companion, closure_companion


# ---------------------------------------------------------------------------
# Section 5 — Working-paper update (Pattern C — FAIL with remediation)
# ---------------------------------------------------------------------------
def update_wp_section(gate_label, new_text):
    """Replace the pending block in WP §<gate_label> with the closure entry.

    Args:
        gate_label: e.g., "W7a-76" — the section identifier.
        new_text: full Pattern C entry text (replaces from ### header to next ---).
    """
    wp_text = WP_PATH.read_text(encoding="utf-8")  # (local)
    # Find the header line
    header_marker = f"### §{gate_label}."  # (local)
    start_idx = wp_text.find(header_marker)  # (local)
    if start_idx == -1:
        raise RuntimeError(f"§{gate_label} header not found in WP")
    # Find the next "---" delimiter line after the header
    end_marker = "\n---\n"  # (local)
    next_delim = wp_text.find(end_marker, start_idx)  # (local)
    if next_delim == -1:
        raise RuntimeError(f"§{gate_label} closing --- delimiter not found")
    # Replace from start_idx to (next_delim + len(end_marker))
    end_idx = next_delim + len(end_marker)  # (local)
    new_wp_text = wp_text[:start_idx] + new_text + wp_text[end_idx:]  # (local)
    WP_PATH.write_text(new_wp_text, encoding="utf-8")
    return start_idx, end_idx


# ---------------------------------------------------------------------------
# Section 6 — Main
# ---------------------------------------------------------------------------
def main():
    print("=" * 70)
    print("S88 W7a-76 + W7a-77 — Mechanical PRE-REG-INC Closure")
    print("=" * 70)
    print()
    print("Upstream blocker: S88-W9B-2-RANK-VS-MAGNITUDE-LAYER-DISCRIMINATOR (W7a-74)")
    print(f"  W7a-74 audit_sha256: {W7A_74_AUDIT_SHA[:32]}...")
    print(f"  W7a-74 composite verdict: FAIL")
    print(f"  W7a-74 sign=FAIL, magnitude=FAIL, regime=VALID")
    print(f"  W7a-74 |rho_S|_T1=0.800 < 0.999 (PASS-RANK threshold)")
    print(f"  W7a-74 spread_T1=1.011 >> 0.06 (PASS-MAGNITUDE bound)")
    print()

    # Compute script SHA
    script_sha = file_sha256(SCRIPT_PATH)  # (local)
    print(f"Closure script content_sha256: {script_sha[:16]}... ({SCRIPT_PATH.name})")
    print()

    t0 = time.time()  # (local)

    # ----- W7a-76 closure -----
    print("--- Closing §W7a-76 (S88-VII-AJ-TWO-ROW-LANDING) ---")
    GATE_ID_76 = "S88-VII-AJ-TWO-ROW-LANDING"  # (local)
    pinmap_76 = {  # (local)
        "_gate_id": GATE_ID_76,
        "_wp_id": "W7a-76",
        "_scheme": "METHODOLOGY-class-registry-landing",
        "_convention": "TWO-ROW-rank-magnitude-epistemic-split-corner-I-pole-s4",
        "_L_max": "N/A",
        "_closure_type": "MECHANICAL-PRE-REG-INC",
        "_blocking_prereq_gate": "W7a-74",
        "_blocking_prereq_audit_sha": W7A_74_AUDIT_SHA,
        "_blocking_prereq_status": "FAIL",
        "_blocking_prereq_failure_modes": "FAIL-RANK_AND_FAIL-MAGNITUDE",
        "_plan_pre_registered_FAIL_clause": "plan §372",
        "script_sha": script_sha,
    }
    audit_sha_76 = closure_hash(pinmap_76)  # (local)
    content_sha_76 = script_sha  # (local)
    value_str_76 = (
        "PRE-REG-INC_blocked_by_W7a-74_FAIL-RANK_FAIL-MAGNITUDE;"
        "VII_AJ_1_landing=BLOCKED;VII_AJ_2_landing=BLOCKED;"
        f"upstream_audit_sha={W7A_74_AUDIT_SHA[:16]}"
    )  # (local)
    closure_comment_76 = (
        f"# PRE-REG-INC per session-88-plan-w7a.md §372 FAIL clause; "
        f"deferred to S89; required prereqs: [W7a-74 PASS-RANK_AND_PASS_OR_INFO_MAGNITUDE]; "
        f"closure_script=computations/session-88/{SCRIPT_PATH.name}"
    )  # (local)

    canonical_76, dual_76, tuple_76, closure_76 = append_verdict(
        GATE_ID_76,
        "FAIL",
        value_str_76,
        pinmap_76["_scheme"],
        pinmap_76["_convention"],
        pinmap_76["_L_max"],
        audit_sha_76,
        content_sha_76,
        "FAIL",  # sign_v: rank+magnitude direction failed at upstream
        "FAIL",  # mag_v: registry landing magnitude FAIL (no rows landed)
        "VALID",  # regime_v: closure logic validly reasons over upstream
        closure_comment_76,
    )
    print(f"  audit_sha256: {audit_sha_76[:16]}...")
    print(f"  composite verdict: FAIL (mechanical)")
    print(f"  Verdict line written.")
    print()

    # ----- W7a-77 closure -----
    print("--- Closing §W7a-77 (S88-OR-LATER-VII-AJ-INDEPENDENT-VERIFY) ---")
    GATE_ID_77 = "S88-OR-LATER-VII-AJ-INDEPENDENT-VERIFY"  # (local)
    pinmap_77 = {  # (local)
        "_gate_id": GATE_ID_77,
        "_wp_id": "W7a-77",
        "_scheme": "Stage-2-cross-axis-independent-verify",
        "_convention": "corner-I-pinned-VII-AJ-1-rank-order-only",
        "_L_max": "N/A",
        "_closure_type": "MECHANICAL-PRE-REG-INC",
        "_blocking_prereq_gates": ["W7a-76", "W7a-74"],
        "_blocking_prereq_W7a_76_audit_sha": audit_sha_76,
        "_blocking_prereq_W7a_74_audit_sha": W7A_74_AUDIT_SHA,
        "_blocking_prereq_status": "FAIL_AND_FAIL",
        "_plan_pre_registered_conditional": "plan §401 CONDITIONAL on (#76 + #74) PASS",
        "script_sha": script_sha,
    }
    audit_sha_77 = closure_hash(pinmap_77)  # (local)
    content_sha_77 = script_sha  # (local)
    value_str_77 = (
        "PRE-REG-INC_blocked_by_W7a-76_FAIL_AND_W7a-74_FAIL-RANK;"
        "Stage-2_cross-axis_verify=BLOCKED_no_VII_AJ_1_landing_to_verify;"
        f"upstream_W7a-76_audit_sha={audit_sha_76[:16]};"
        f"upstream_W7a-74_audit_sha={W7A_74_AUDIT_SHA[:16]}"
    )  # (local)
    closure_comment_77 = (
        f"# PRE-REG-INC per session-88-plan-w7a.md §401 CONDITIONAL on (#76+#74) PASS; "
        f"deferred to S89; required prereqs: [W7a-76 PASS, W7a-74 PASS-RANK]; "
        f"closure_script=computations/session-88/{SCRIPT_PATH.name}"
    )  # (local)

    canonical_77, dual_77, tuple_77, closure_77 = append_verdict(
        GATE_ID_77,
        "FAIL",
        value_str_77,
        pinmap_77["_scheme"],
        pinmap_77["_convention"],
        pinmap_77["_L_max"],
        audit_sha_77,
        content_sha_77,
        "FAIL",
        "FAIL",
        "VALID",
        closure_comment_77,
    )
    print(f"  audit_sha256: {audit_sha_77[:16]}...")
    print(f"  composite verdict: FAIL (mechanical)")
    print(f"  Verdict line written.")
    print()

    # ---- Sanity: SHA-uniqueness pre-WP-edit ----
    if audit_sha_76 == audit_sha_77:
        print(f"  ERROR: per-gate-distinct audit_sha256 INVARIANT VIOLATED")
        print(f"    audit_sha_76 == audit_sha_77 == {audit_sha_76[:32]}...")
        return "FAIL"
    print(f"--- sig_5 per-gate uniqueness invariant satisfied ---")
    print(f"  audit_sha_76 = {audit_sha_76[:16]}...")
    print(f"  audit_sha_77 = {audit_sha_77[:16]}...")
    print()

    # ---- Save closure metadata as JSON for the WP-update tasks ----
    closure_meta_path = SESSION_DIR / "s88_w7a_76_77_closure_metadata.json"  # (local)
    closure_meta = {  # (local)
        "W7a-76": {
            "gate_id": GATE_ID_76,
            "audit_sha256": audit_sha_76,
            "content_sha256": content_sha_76,
            "verdict": "FAIL",
            "value_str": value_str_76,
            "scheme": pinmap_76["_scheme"],
            "convention": pinmap_76["_convention"],
            "L_max": pinmap_76["_L_max"],
            "sign_v": "FAIL",
            "mag_v": "FAIL",
            "regime_v": "VALID",
            "blocking_prereq": "W7a-74 (FAIL-RANK + FAIL-MAGNITUDE)",
            "plan_pre_reg_clause": "plan §372 FAIL clause",
        },
        "W7a-77": {
            "gate_id": GATE_ID_77,
            "audit_sha256": audit_sha_77,
            "content_sha256": content_sha_77,
            "verdict": "FAIL",
            "value_str": value_str_77,
            "scheme": pinmap_77["_scheme"],
            "convention": pinmap_77["_convention"],
            "L_max": pinmap_77["_L_max"],
            "sign_v": "FAIL",
            "mag_v": "FAIL",
            "regime_v": "VALID",
            "blocking_prereqs": ["W7a-76 (FAIL)", "W7a-74 (FAIL-RANK)"],
            "plan_pre_reg_clause": "plan §401 CONDITIONAL on (#76 + #74) PASS",
        },
        "upstream_W7a-74_audit_sha256": W7A_74_AUDIT_SHA,
        "closure_script_path": str(SCRIPT_PATH),
        "closure_script_sha256": script_sha,
    }
    with open(closure_meta_path, "w", encoding="utf-8") as f:
        json.dump(closure_meta, f, indent=2)
    print(f"  Closure metadata saved: {closure_meta_path}")
    print()

    print("=" * 70)
    print("Verdict lines written to s88_gate_verdicts.txt:")
    print(canonical_76.rstrip())
    print(dual_76.rstrip())
    print(tuple_76.rstrip())
    print(closure_76.rstrip())
    print("---")
    print(canonical_77.rstrip())
    print(dual_77.rstrip())
    print(tuple_77.rstrip())
    print(closure_77.rstrip())
    print("=" * 70)
    print()
    print(f"Wall time: {time.time() - t0:.2f}s")
    print()
    print("NOTE: WP §W7a-76 + §W7a-77 sections will be updated by the")
    print("subsequent update-wp tasks (Pattern C — FAIL with remediation).")
    print("This script handles ONLY the verdict-line emission per the")
    print("rclab-solo skill's compute+update task decomposition.")
    return "FAIL"  # composite mechanical-closure FAIL


if __name__ == "__main__":
    sys.exit(0 if main() in ("PASS", "FAIL", "INFO") else 1)
