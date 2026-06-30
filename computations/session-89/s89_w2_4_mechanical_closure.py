"""
S89 W2-4 Mechanical Closure Script
==================================

Per `.claude/rules/mechanical-closure-discipline.md` §"When mechanical closure
IS acceptable" — orchestrator-authored mechanical closure of an upstream-blocked
gate, with no specialist-agent dispatch and no physics computation.

Upstream-block topology
-----------------------
- Gate being closed:    S89-3HEB-EXCESS-INHERITANCE-CONNES-KAROUBI-PAIRING-CANONICAL (§W2-4)
- Upstream prereqs:     S89-CONNES-KAROUBI-PAIRING-BDG-RESTRICTED-INFRASTRUCTURE (§W2-1) — composite=FAIL
                        S89-BCS-PHYSICS-GROUNDED-R-SUBSTRATE-LANDAU-PATH (§W2-2) — composite=FAIL (mechanical closure)
- Plan foreclosure:     `sessions/session-plan/session-89-plan-w2.md` §W2-4.6 line
                        567: "PREREQUISITES: A.3 PASS verdict AND A.4 PASS verdict.
                        If EITHER ... is NOT yet in s89_gate_verdicts.txt,
                        dispatch to mechanical closure."
                        + plan §W2 §"Wave 2 Decision Point Prerequisites" item 2
                        line 24 (intra-wave dependency chain A.3 + A.4 → A.20).
- Wave-context:         covered_count=3 of wave-total 5 < N_PLANNING_DEFECT_THRESHOLD=4
                        (no planning defect; mechanical closure within rule scope).

This script
-----------
(a) extracts the FULL 64-char §W2-1 + §W2-2 audit_sha256 from the verdict file
(b) computes per-gate-distinct audit_sha256 for §W2-4 mechanical closure
(c) appends FAIL verdict line + dual-SHA companion + mechanical-closure companion
    (no 3-tuple required for [AUDIT] trigger per plan §W2-4.7)
(d) updates WP §W2-4 section IN THE SAME RUN with Status/Verdict/Results/
    Substrate-framing/Carry-forward blocks
(e) self-verifies: re-reads verdict file + WP, asserts presence of foreclosure
    markers; sig_5 SHA-uniqueness check.
"""

import sys
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
import hashlib
import json
import re
from collections import OrderedDict
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path("computations/_shared").resolve()))
from canonical_constants import *  # noqa: F401, F403

# === Paths ===
ROOT = Path(".").resolve()  # (local)
VERDICT_FILE = ROOT / "computations" / "session-89" / "s89_gate_verdicts.txt"  # (local)
WP_FILE = ROOT / "sessions" / "session-89" / "session-89-w2-workingpaper.md"  # (local)
PLAN_FILE = ROOT / "sessions" / "session-plan" / "session-89-plan-w2.md"  # (local)
THIS_SCRIPT = ROOT / "computations" / "session-89" / "s89_w2_4_mechanical_closure.py"  # (local)

# === Gate identity ===
GATE_ID = "S89-3HEB-EXCESS-INHERITANCE-CONNES-KAROUBI-PAIRING-CANONICAL"  # (local)
UPSTREAM_GATE_A3 = "S89-CONNES-KAROUBI-PAIRING-BDG-RESTRICTED-INFRASTRUCTURE"  # (local)
UPSTREAM_GATE_A4 = "S89-BCS-PHYSICS-GROUNDED-R-SUBSTRATE-LANDAU-PATH"  # (local)

print(f"Mechanical closure: {GATE_ID}")
print(f"Upstream-block sources: {UPSTREAM_GATE_A3} (A.3) + {UPSTREAM_GATE_A4} (A.4)")
print(f"Verdict file: {VERDICT_FILE}")
print(f"Working paper: {WP_FILE}")
print()

# === Step 1: Extract FULL 64-char §W2-1 + §W2-2 audit_sha256 from verdict file ===
verdict_text = VERDICT_FILE.read_text(encoding="utf-8")  # (local)


def extract_status_and_sha(gate_name: str) -> tuple[str, str]:
    pat = re.compile(  # (local)
        r"^" + re.escape(gate_name) + r":\s+(\w+).*?audit_sha256=([0-9a-f]{64})",
        re.MULTILINE | re.DOTALL,
    )
    m = pat.search(verdict_text)  # (local)
    assert m is not None, (
        f"Upstream gate {gate_name} not found in {VERDICT_FILE} — "
        f"cannot proceed with mechanical closure"
    )
    return m.group(1), m.group(2)


a3_status, a3_sha = extract_status_and_sha(UPSTREAM_GATE_A3)
a4_status, a4_sha = extract_status_and_sha(UPSTREAM_GATE_A4)

assert a3_status != "PASS" or a4_status != "PASS", (
    f"Mechanical closure of §W2-4 NOT admissible: BOTH upstream gates report PASS, "
    f"so §W2-4 should dispatch normally rather than foreclose. "
    f"({UPSTREAM_GATE_A3}={a3_status}; {UPSTREAM_GATE_A4}={a4_status})"
)
print(f"Upstream §W2-1 verdict: {a3_status}")
print(f"Upstream §W2-1 audit_sha256: {a3_sha}")
print(f"Upstream §W2-2 verdict: {a4_status}")
print(f"Upstream §W2-2 audit_sha256: {a4_sha}")
print()

# === Step 2: Build per-gate-distinct input-pin map for §W2-4 closure ===
input_pin_map = OrderedDict([  # (local)
    ("_gate_id", GATE_ID),
    ("_wp_id", "W2-4"),
    ("_session", "S89"),
    ("_closure_type", "mechanical_dual_upstream_block"),
    ("_upstream_gate_a3", UPSTREAM_GATE_A3),
    ("_upstream_status_a3", a3_status),
    ("_upstream_audit_sha_a3", a3_sha),
    ("_upstream_gate_a4", UPSTREAM_GATE_A4),
    ("_upstream_status_a4", a4_status),
    ("_upstream_audit_sha_a4", a4_sha),
    ("_plan_clause", "session-89-plan-w2.md §W2-4.6 line 567 (PREREQUISITES A.3 PASS AND A.4 PASS) + §W2 \"Wave 2 Decision Point Prerequisites\" item 2 line 24"),
    ("_dispatched", False),
    ("_designated_agent", "sagan-empiricist (PRIMARY); connes + volovik CO-AUTHORS — NOT DISPATCHED"),
    ("_scheme", "Sagan-revised-dual-prior-3-track-structure"),
    ("_convention", "Element-3-fiducial-anchor-binding-discipline-S88-W15-V7-compliant"),
    ("_L_max", 10),
    ("_carry_forward_S90", "CF-W2-1-RETRY (re-pin xc1 tolerance per Class-8.3 publication-precision; clarify xc1 vs xc2 observable identity) + CF-W2-2-DEFERRED (re-execute landau path post-A.3 PASS) + CF-W2-4-DEFERRED (Sagan dual-prior JSON post-A.3 + A.4 PASS); §VII.AH STAGE-1-CANDIDATE → STAGE-3-PERMANENT promotion remains BLOCKED on (A.20 PASS AND A.39 Stage-2 PASS)"),
])
audit_sha = hashlib.sha256(  # (local)
    json.dumps(input_pin_map, sort_keys=False).encode("utf-8")
).hexdigest()
audit_sha_short = audit_sha[:16]  # (local)

this_script_bytes = THIS_SCRIPT.read_bytes() if THIS_SCRIPT.exists() else b""  # (local)
content_sha = hashlib.sha256(this_script_bytes).hexdigest()  # (local)
content_sha_short = content_sha[:16]  # (local)

print(f"§W2-4 closure audit_sha256:   {audit_sha}")
print(f"§W2-4 closure content_sha256: {content_sha}")
print()

# === Step 3: Sig_5 SHA-uniqueness check ===
existing_shas = set(re.findall(r"audit_sha256=([0-9a-f]{64})", verdict_text))  # (local)
assert audit_sha not in existing_shas, (
    f"Sig_5 collision: §W2-4 closure audit_sha256={audit_sha} duplicates an "
    f"existing entry. Mechanical closure ABORTED."
)
print(
    f"Sig_5 SHA-uniqueness check: PASS "
    f"(closure SHA distinct from {len(existing_shas)} existing entries)"
)
print()

# === Step 4: Construct verdict-line triple (no 3-tuple — [AUDIT] trigger) ===
value_str = (  # (local)
    f"PRE-REG-INC_blocked_by_{UPSTREAM_GATE_A3}_{a3_status}"
    f"_AND_{UPSTREAM_GATE_A4}_{a4_status}"
)
canonical_line = (  # (local)
    f"{GATE_ID}: FAIL -- value='{value_str}' "
    f"scheme=Sagan-revised-dual-prior-3-track-structure "
    f"convention=Element-3-fiducial-anchor-binding-discipline-S88-W15-V7-compliant "
    f"L_max=10 "
    f"audit_sha256={audit_sha} "
    f"content_sha256={content_sha} "
    f"schema_version=S87+"
)
dual_sha_companion = (  # (local)
    f"# audit_sha256_short={audit_sha_short} "
    f"content_sha256_short={content_sha_short} "
    f"# {GATE_ID} dual-SHA companion row (W9a-99 split)"
)
mechanical_companion = (  # (local)
    f"# {GATE_ID} mechanical closure: PRE-REG-INC per "
    f"session-89-plan-w2.md §W2-4.6 line 567 (PREREQUISITES A.3 PASS AND A.4 PASS); "
    f"deferred to S90 (CF-W2-1-RETRY + CF-W2-2-DEFERRED + CF-W2-4-DEFERRED); "
    f"required prereqs: [{UPSTREAM_GATE_A3}=PASS, {UPSTREAM_GATE_A4}=PASS]; "
    f"closure_script=computations/session-89/s89_w2_4_mechanical_closure.py; "
    f"upstream_audit_sha256_a3={a3_sha}; "
    f"upstream_audit_sha256_a4={a4_sha}"
)

# === Step 5: Append to verdict file ===
with open(VERDICT_FILE, "a", encoding="utf-8") as f:
    f.write(canonical_line + "\n")
    f.write(dual_sha_companion + "\n")
    f.write(mechanical_companion + "\n")
    f.flush()
    os.fsync(f.fileno())

print("Appended 3 lines to verdict file:")
print(f"  [1] Canonical:    {canonical_line[:100]}...")
print(f"  [2] Dual-SHA:     {dual_sha_companion[:80]}...")
print(f"  [3] Mech-clos:    {mechanical_companion[:80]}...")
print()

# === Step 6: Update WP §W2-4 section ===
wp_text = WP_FILE.read_text(encoding="utf-8")  # (local)
TIMESTAMP = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")  # (local)

new_section = (
    f"### §W2-4. S89-3HEB-EXCESS-INHERITANCE-CONNES-KAROUBI-PAIRING-CANONICAL (sagan-empiricist — FORECLOSED)\n"
    f"\n"
    f"**Status**: FORECLOSED (mechanical closure orchestrator-direct via "
    f"`computations/session-89/s89_w2_4_mechanical_closure.py`; no specialist-agent dispatch; no physics computation)\n"
    f"**Gate ID**: `{GATE_ID}`\n"
    f"**Trigger**: `[AUDIT]` (pre-registered but NOT exercised due to upstream-block foreclosure)\n"
    f"**Classification**: **GEOMETRIC** (Sagan-revised dual-prior 3-track structure pre-registration on §VII.AH STAGE-1-CANDIDATE; Element 3 fiducial-anchor binding discipline)\n"
    f"**Agent**: NOT DISPATCHED (mechanical closure per `.claude/rules/mechanical-closure-discipline.md`; designated PRIMARY = sagan-empiricist; CO-AUTHORs = connes-ncg-theorist + volovik-superfluid-universe-theorist)\n"
    f"**Hypothesis**: NOT TESTED — gate foreclosed; see Verdict block.\n"
    f"**Plan reference**: `sessions/session-plan/session-89-plan-w2.md` §W2-4; foreclosure routing at §W2-4.6 line 567 (PREREQUISITES A.3 PASS AND A.4 PASS) + §W2 \"Wave 2 Decision Point Prerequisites\" item 2 line 24.\n"
    f"\n"
    f"**Substrate framing** (verbatim from plan §W2-4.13; declarative for documentation, not exercised at compute-time):\n"
    f"\n"
    f"> The Sagan-revised dual-prior 3-track structure IS the substrate-IS pre-registration object on the §VII.AH 3HeB-excess-inheritance theorem candidate; it is NOT \"a probability distribution in a probability container.\" The 3 tracks (substrate-self-consistent / external-observation / joint-hypersurface) ARE 3 distinct structural readings of the substrate-IS observable; they are NOT \"3 possible realities the substrate might inhabit.\" The track-discriminator gate criterion IS the substrate-IS deterministic posterior re-allocation rule; it is NOT \"a Bayesian update in a probability space.\" The §VII.AH 3HeB-excess-inheritance theorem candidate IS the substrate-IS structural prediction at the cross-pillar-bridge layer (substrate Pillar I ↔ laboratory Pillar V 3HeB); it is NOT \"a 3HeB observable.\" Direction of explanation: D_K eigenvalues → Connes-Karoubi pairing infrastructure (A.3) → BCS-physics-grounded R_substrate (A.4) → Sagan-revised dual-prior 3-track pre-registration (this gate) → Stage-2 dispatch on §VII.AH (FUTURE, A.39 in W4) → eventual STAGE-3-PERMANENT promotion of §VII.AH iff PASS-AND across 3 tracks.\n"
    f"\n"
    f"**Single-τ-slice level**: §W2-4 was pre-registered at Level 1 single-τ-slice substrate-IS (the dual-prior is registered against τ_fold = 0.190 R-PROTECTED canonicals; the 3 tracks are intrinsic to the spectral triple at the fixed τ-anchor). Foreclosed; not exercised.\n"
    f"\n"
    f"**MCP Pre-Compute Audit**: NOT EXECUTED (no compute dispatched; the mechanical closure is orchestrator-direct).\n"
    f"\n"
    f"**Verdict**: **FAIL** — composite=FAIL via mechanical closure. Per `.claude/rules/mechanical-closure-discipline.md §\"Audit-trail signature\"`, the canonical verdict-line emitted to `computations/session-89/s89_gate_verdicts.txt`:\n"
    f"\n"
    f"```\n"
    f"{canonical_line}\n"
    f"{dual_sha_companion}\n"
    f"{mechanical_companion}\n"
    f"```\n"
    f"\n"
    f"**Mechanical closure justification** (per `mechanical-closure-discipline.md §\"When mechanical closure IS acceptable\"` clauses 1-5):\n"
    f"\n"
    f"1. **Upstream-block topology (DUAL)**: §W2-4 reads BOTH §W2-1's npz output (A.3 R_canonical_value) AND §W2-2's npz output (A.4 R_substrate_BCS_grounded_corrected) as input pins per plan §W2-4.7 lines 683-689 (input_pin_map). §W2-1 closed composite=FAIL with `audit_sha256={a3_sha}`; §W2-2 closed composite=FAIL via mechanical closure with `audit_sha256={a4_sha}`. Plan §W2-4.6 line 567 (verbatim): *\"PREREQUISITES: A.3 PASS verdict AND A.4 PASS verdict. If EITHER `S89-CONNES-KAROUBI-PAIRING-BDG-RESTRICTED-INFRASTRUCTURE: PASS` OR `S89-BCS-PHYSICS-GROUNDED-R-SUBSTRATE-LANDAU-PATH: PASS` is NOT yet in `computations/session-89/s89_gate_verdicts.txt`, dispatch to mechanical closure ... with verdict `value='PRE-REG-INC_blocked_by_A.3_pending_or_A.4_pending'`. Do NOT proceed.\"* Both prereqs FAIL ⇒ foreclosure required.\n"
    f"2. **Verdict honesty**: emitted as FAIL with `value='PRE-REG-INC_blocked_by_{UPSTREAM_GATE_A3}_{a3_status}_AND_{UPSTREAM_GATE_A4}_{a4_status}'` per the canonical pattern (extended to dual-block); never PASS.\n"
    f"3. **Per-gate-distinct audit_sha256**: closure `audit_sha256={audit_sha}` is structurally distinct from §W2-1, §W2-2, §W2-3 entries. Sig_5 SHA-uniqueness preserved by construction.\n"
    f"4. **Audit-trail signature (DUAL)**: canonical `value=` field names BOTH blocking prereqs + statuses; the upstream §W2-1 AND §W2-2 audit_sha256 values are recorded in the mechanical-closure companion row (`upstream_audit_sha256_a3={a3_sha}`, `upstream_audit_sha256_a4={a4_sha}`) for full audit-trail traceability.\n"
    f"5. **Working-paper update IS in-script**: this WP §W2-4 section is updated by the same script execution (`s89_w2_4_mechanical_closure.py`).\n"
    f"\n"
    f"**Results**: NOT COMPUTED. The §W2-4 producing script `s89_w2_a20_3heb_excess_inheritance_dual_prior.py` was NOT created. No dual-prior JSON, prior-mass distribution {{A:0.50, B:0.30, C:0.20}}, posterior re-allocation rules, or rule-compliance verification (W-15 V.7 + T1-11) was performed.\n"
    f"\n"
    f"**What FORECLOSE means for solution space**:\n"
    f"\n"
    f"- The Sagan-revised dual-prior 3-track structure pre-registration on the §VII.AH STAGE-1-CANDIDATE remains UNREGISTERED at the §W2-4 level in S89. §W2-4 is the substrate-IS pre-registration object; without it, the future Stage-2 dispatch on §VII.AH (A.39 in W4) has no track-discriminator gate criterion to map PASS/FAIL/INFO outcomes to posterior re-allocations.\n"
    f"- Element 3 fiducial-anchor binding discipline K-counter (W-15 V.7 K=1 advisory) does NOT advance this session — A.20 PASS would have advanced K=1 → K=2; the foreclosure leaves it at K=1.\n"
    f"- Dual-prior pre-registration as track-discriminator pattern (T1-11 K=1 advisory) does NOT advance this session — A.20 PASS would have advanced K=1 → K=2 (the second instance after S87-W5A-P3-IC-PER-CLASS-VERIFY); the foreclosure leaves it at K=1.\n"
    f"- §VII.AH STAGE-1-CANDIDATE → STAGE-3-PERMANENT promotion remains BLOCKED on (A.20 PASS in this wave) AND (A.39 PASS Stage-2 multi-observable re-dispatch in W4). Per `joint-theorem-promotion.md` 4-stage pathway: §VII.AH stays at STAGE-1-CANDIDATE.\n"
    f"\n"
    f"**Carry-forward to S90 (4-field specs per `feedback_fix-in-session-never-defer.md`)**:\n"
    f"\n"
    f"| Field | CF-W2-4-DEFERRED |\n"
    f"|:------|:------------------|\n"
    f"| **What** | Re-execute Sagan-revised dual-prior 3-track pre-registration JSON post-(A.3 + A.4) PASS; verify prior-mass distribution {{A:0.50, B:0.30, C:0.20}} sums to 1.000 ± 1e-10; verify posterior re-allocation rules sum to 1.000 ± 1e-10 for each of PASS-AND/FAIL/INFO outcomes; rule-compliance check against W-15 V.7 + T1-11 |\n"
    f"| **Inputs** | S90 §W2-1 PASS or INFO npz (R_canonical_value); S90 §W2-2 PASS npz (R_substrate_BCS_grounded_corrected); `cross-pillar-bridge-anatomy.md §\"Element 3 fiducial-anchor binding discipline\"` (S88 W-15 V.7); `epistemic-discipline.md §\"Dual-prior pre-registration as track-discriminator pattern\"` (T1-11) |\n"
    f"| **Gate** | JSON well-formed; sum_of_prior_masses = 1.000 ± 1e-10; per-outcome posterior sums = 1.000 ± 1e-10; all rule-compliance fields = \"compliant\"; tracks STRUCTURALLY DISTINCT (no conflation per W-15 V.7) |\n"
    f"| **Effort** | 0.3 wave-equiv (matches original §W2-4 estimate; plan §W2-4.12) |\n"
    f"\n"
    f"**4-tuple output** (declarative; not computed):\n"
    f"\n"
    f"`(value='PRE-REG-INC_blocked_by_{UPSTREAM_GATE_A3}_{a3_status}_AND_{UPSTREAM_GATE_A4}_{a4_status}', scheme=Sagan-revised-dual-prior-3-track-structure, convention=Element-3-fiducial-anchor-binding-discipline-S88-W15-V7-compliant, L_max=10)`\n"
    f"\n"
    f"**Files NOT produced** (foreclosed):\n"
    f"\n"
    f"| Artifact | Path | Status |\n"
    f"|:---------|:-----|:-------|\n"
    f"| Producing script | `computations/session-89/s89_w2_a20_3heb_excess_inheritance_dual_prior.py` | NOT created |\n"
    f"| Dual-prior JSON | `computations/session-89/s89_w2_a20_3heb_excess_inheritance_dual_prior.json` | NOT created |\n"
    f"| Mechanical closure script | `computations/session-89/s89_w2_4_mechanical_closure.py` | CREATED (this script) |\n"
    f"\n"
    f"**Direction of explanation** (per `phononic-framing.md`): the foreclosure is a routing decision driven by DUAL upstream-block topology, NOT a substrate-physics statement about the §VII.AH theorem candidate itself. The substrate-IS dual-prior 3-track structure remains a well-defined pre-registration object; the foreclosure pertains to the AVAILABILITY of substrate-IS Connes-Karoubi pairing infrastructure (§W2-1) AND BCS-physics-grounded R_substrate at polycritical pressure (§W2-2), both of which the literal-tolerance FAIL of §W2-1 (and consequent mechanical foreclosure of §W2-2) made unavailable for this session.\n"
    f"\n"
    f"**Closure timestamp**: {TIMESTAMP}.\n"
    f"\n"
)

# Replace the §W2-4 stub block
section_pattern = re.compile(  # (local)
    r"### §W2-4\..*?(?=\n### §W2-5\.)",
    re.DOTALL,
)
match2 = section_pattern.search(wp_text)  # (local)
assert match2 is not None, (
    f"Could not find §W2-4 section in {WP_FILE} — mechanical closure ABORTED."
)
new_wp_text = wp_text[:match2.start()] + new_section + "---\n\n" + wp_text[match2.end()+1:]  # (local)
WP_FILE.write_text(new_wp_text, encoding="utf-8")

# === Step 7: Self-verify ===
verdict_after = VERDICT_FILE.read_text(encoding="utf-8")  # (local)
assert canonical_line in verdict_after
assert audit_sha in verdict_after

wp_after = WP_FILE.read_text(encoding="utf-8")  # (local)
assert "FORECLOSED" in wp_after
assert f"PRE-REG-INC_blocked_by_{UPSTREAM_GATE_A3}_{a3_status}_AND_{UPSTREAM_GATE_A4}_{a4_status}" in wp_after
assert "CF-W2-4-DEFERRED" in wp_after

print(f"WP §W2-4 section updated: {WP_FILE}")
print(f"  'FORECLOSED' status present:                   True")
print(f"  Dual-foreclosure value-string present:         True")
print(f"  CF-W2-4-DEFERRED 4-field spec present:         True")
print()

# === Final summary ===
print("=" * 72)
print(f"§W2-4 mechanical closure COMPLETE.")
print(f"  Verdict:                  FAIL (PRE-REG-INC blocked by §W2-1 FAIL AND §W2-2 FAIL)")
print(f"  Closure audit_sha256:     {audit_sha}")
print(f"  Closure content_sha256:   {content_sha}")
print(f"  Upstream §W2-1 audit_sha: {a3_sha}")
print(f"  Upstream §W2-2 audit_sha: {a4_sha}")
print(f"  Sig_5 SHA-uniqueness:     PASS (vs {len(existing_shas)} existing entries)")
print(f"  WP §W2-4 section:         UPDATED in-script")
print(f"  Carry-forward:            CF-W2-4-DEFERRED → S90")
print("=" * 72)

sys.exit(0)
