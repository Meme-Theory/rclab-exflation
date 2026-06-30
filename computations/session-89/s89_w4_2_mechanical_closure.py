"""
S89 W4-2 Mechanical Closure Script
==================================

Per `.claude/rules/mechanical-closure-discipline.md` §"When mechanical closure
IS acceptable" — orchestrator-authored mechanical closure of an upstream-blocked
gate, with no specialist-agent dispatch and no physics computation.

Upstream-block topology
-----------------------
- Gate being closed:    S89-FOUR-CORNER-STAGE-2-CROSS-AXIS-VERIFY-DUAL-BASIS (§W4-2, A.10)
- Upstream prereq:      S89-CONNES-KAROUBI-PAIRING-BDG-RESTRICTED-INFRASTRUCTURE (W2 A.3)
- Upstream verdict:     composite=FAIL (sign=N/A, magnitude=FAIL, regime=VALID)
                        per `computations/session-89/s89_gate_verdicts.txt`
- Plan foreclosure:     `sessions/session-plan/session-89-plan-w4.md`
                          §W4-2 Method step 2 line 196: "If A.3 PASS verdict
                          absent, route A.10 to PRE-REG-INC mechanical-closure
                          with `value='PRE-REG-INC_blocked_by_A.3_<status>'`."
                        + §"Wave 4 → Waves 2/7 Decision Point" line 1205:
                          "A.10 dispatch BLOCKED until A.3 verdict ∈ {PASS, INFO}"
- Intra-wave dep:       §W4-1 (A.11) S89-SUBSTRATE-CANONICAL-14-STATE-BASIS-RE-RUN
                        verdict = PASS — INTRA-WAVE PREREQ SATISFIED. A.10 still
                        routes to PRE-REG-INC because A.3 (cross-wave from W2)
                        FAILs, blocking the lizzi-axis cross-reviewer's
                        Connes-Karoubi pairing canonical infrastructure
                        consumption (per plan §W4-2 sub-test (ii) PASS criterion).
- Wave-context:         covered_count=1 of wave-total 7 < N_PLANNING_DEFECT_THRESHOLD=4
                        (no planning defect; mechanical closure within rule scope).

This script
-----------
(a) extracts the FULL 64-char A.3 audit_sha256 from the verdict file via regex
(b) computes per-gate-distinct audit_sha256 for §W4-2 mechanical closure
(c) appends FAIL verdict line + dual-SHA companion + 3-tuple companion
    + mechanical-closure companion (4 lines total)
(d) updates WP §W4-2 section IN THE SAME RUN with Status/Verdict/Results/
    Substrate-framing/Carry-forward blocks
(e) self-verifies: re-reads verdict file + WP, asserts presence of
    foreclosure markers; sig_5 SHA-uniqueness check against A.3.

Single-execution discipline: per `mechanical-closure-discipline.md §"Carry-
forward script-bytes immutability"`, this script SHOULD be considered immutable
after first execution; the recorded `content_sha256` is the SHA of these bytes
at the time of emission.
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
WP_FILE = ROOT / "sessions" / "session-89" / "session-89-w4-workingpaper.md"  # (local)
PLAN_FILE = ROOT / "sessions" / "session-plan" / "session-89-plan-w4.md"  # (local)
THIS_SCRIPT = ROOT / "computations" / "session-89" / "s89_w4_2_mechanical_closure.py"  # (local)

# === Gate identity ===
GATE_ID = "S89-FOUR-CORNER-STAGE-2-CROSS-AXIS-VERIFY-DUAL-BASIS"  # (local)
UPSTREAM_GATE = "S89-CONNES-KAROUBI-PAIRING-BDG-RESTRICTED-INFRASTRUCTURE"  # (local)
INTRA_WAVE_PREREQ = "S89-SUBSTRATE-CANONICAL-14-STATE-BASIS-RE-RUN"  # (local) §W4-1 A.11

print(f"Mechanical closure: {GATE_ID}")
print(f"Upstream-block source: {UPSTREAM_GATE} (W2 cross-wave)")
print(f"Intra-wave prereq:     {INTRA_WAVE_PREREQ} (§W4-1 A.11)")
print(f"Verdict file: {VERDICT_FILE}")
print(f"Working paper: {WP_FILE}")
print()

# === Step 1: Extract FULL 64-char A.3 audit_sha256 from verdict file ===
verdict_text = VERDICT_FILE.read_text(encoding="utf-8")  # (local)

sha_pattern_a3 = re.compile(  # (local)
    r"^" + re.escape(UPSTREAM_GATE) + r":\s+(\w+).*?audit_sha256=([0-9a-f]{64})",
    re.MULTILINE | re.DOTALL,
)
match_a3 = sha_pattern_a3.search(verdict_text)  # (local)
assert match_a3 is not None, (
    f"Upstream gate {UPSTREAM_GATE} not found in {VERDICT_FILE} — "
    f"cannot proceed with mechanical closure"
)
upstream_status = match_a3.group(1)  # (local)
upstream_audit_sha = match_a3.group(2)  # (local)
upstream_audit_sha_short = upstream_audit_sha[:16]  # (local)

assert upstream_status != "PASS", (
    f"Mechanical closure of §W4-2 NOT admissible: upstream {UPSTREAM_GATE} "
    f"reports PASS, so §W4-2 should dispatch normally rather than foreclose."
)
print(f"Upstream A.3 verdict: {upstream_status}")
print(f"Upstream A.3 audit_sha256 (full 64-char): {upstream_audit_sha}")

# Also verify A.11 PASS (intra-wave prereq) — informational; not blocking
sha_pattern_a11 = re.compile(  # (local)
    r"^" + re.escape(INTRA_WAVE_PREREQ) + r":\s+(\w+).*?audit_sha256=([0-9a-f]{64})",
    re.MULTILINE | re.DOTALL,
)
match_a11 = sha_pattern_a11.search(verdict_text)  # (local)
if match_a11 is not None:
    a11_status = match_a11.group(1)  # (local)
    a11_audit_sha = match_a11.group(2)  # (local)
    print(f"Intra-wave A.11 verdict: {a11_status}")
    print(f"Intra-wave A.11 audit_sha256 (full 64-char): {a11_audit_sha}")
else:
    a11_status = "NOT_FOUND"  # (local)
    a11_audit_sha = ""  # (local)
    print(f"Intra-wave A.11 verdict: NOT FOUND in verdict file (warning)")
print()

# === Step 2: Build per-gate-distinct input-pin map for §W4-2 closure ===
input_pin_map = OrderedDict([  # (local)
    ("_gate_id", GATE_ID),
    ("_wp_id", "W4-2"),
    ("_session", "S89"),
    ("_closure_type", "mechanical_upstream_block_cross_wave"),
    ("_upstream_gate", UPSTREAM_GATE),
    ("_upstream_status", upstream_status),
    ("_upstream_audit_sha", upstream_audit_sha),
    ("_intra_wave_prereq_gate", INTRA_WAVE_PREREQ),
    ("_intra_wave_prereq_status", a11_status),
    ("_intra_wave_prereq_audit_sha", a11_audit_sha),
    ("_plan_clause", "session-89-plan-w4.md §W4-2 Method step 2 line 196 (PREREQUISITE A.3 PASS) + §\"Wave 4 → Waves 2/7 Decision Point\" line 1205 (A.10 BLOCKED until A.3 ∈ {PASS, INFO})"),
    ("_dispatched", False),
    ("_designated_agents", "lizzi-spectral-functional-theorist (Axis-A; CROSS pattern audits connes-axis-14state) + connes-ncg-theorist (Axis-B; CROSS pattern audits lizzi-axis-Pad16) — NOT DISPATCHED"),
    ("_scheme", "joint-theorem-promotion-stage-2-PASS-AND"),
    ("_convention", "four-corner-dual-basis-stage-2-cross-axis-verify"),
    ("_L_max", 10),
    ("_carry_forward_S90", "CF-W4-2-DEFERRED (re-dispatch 4-corner dual-basis Stage-2 post-A.3 PASS; reuses A.11 PASS verdict from S89 §W4-1 + A.3 forthcoming PASS verdict)"),
])
audit_sha = hashlib.sha256(  # (local)
    json.dumps(input_pin_map, sort_keys=False).encode("utf-8")
).hexdigest()
audit_sha_short = audit_sha[:16]  # (local)

this_script_bytes = THIS_SCRIPT.read_bytes() if THIS_SCRIPT.exists() else b""  # (local)
content_sha = hashlib.sha256(this_script_bytes).hexdigest()  # (local)
content_sha_short = content_sha[:16]  # (local)

print(f"§W4-2 closure audit_sha256:   {audit_sha}")
print(f"§W4-2 closure content_sha256: {content_sha}")
print()

# === Step 3: Sig_5 SHA-uniqueness check ===
existing_shas = set(re.findall(r"audit_sha256=([0-9a-f]{64})", verdict_text))  # (local)
assert audit_sha not in existing_shas, (
    f"Sig_5 collision: §W4-2 closure audit_sha256={audit_sha} duplicates an "
    f"existing entry in {VERDICT_FILE}. Mechanical closure ABORTED."
)
print(
    f"Sig_5 SHA-uniqueness check: PASS "
    f"(closure SHA distinct from {len(existing_shas)} existing entries)"
)
print()

# === Step 4: Construct verdict-line triple + 3-tuple + mech-closure companion ===
value_str = f"PRE-REG-INC_blocked_by_{UPSTREAM_GATE}_{upstream_status}"  # (local)
canonical_line = (  # (local)
    f"{GATE_ID}: FAIL -- value='{value_str}' "
    f"scheme=joint-theorem-promotion-stage-2-PASS-AND "
    f"convention=four-corner-dual-basis-stage-2-cross-axis-verify "
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
three_tuple_companion = (  # (local)
    f"# sign_verdict=N/A magnitude_verdict=FAIL regime_verdict=VALID "
    f"# {GATE_ID} 3-tuple annotation (S87 schema-v2; foreclosure under [VERIFY] trigger)"
)
mechanical_companion = (  # (local)
    f"# {GATE_ID} mechanical closure: PRE-REG-INC per "
    f"session-89-plan-w4.md §W4-2 Method step 2 line 196 (PREREQUISITE A.3 PASS); "
    f"deferred to S90 (CF-W4-2-DEFERRED); "
    f"required prereqs: [{UPSTREAM_GATE}=PASS]; "
    f"intra_wave_prereq_satisfied: [{INTRA_WAVE_PREREQ}={a11_status}]; "
    f"closure_script=computations/session-89/s89_w4_2_mechanical_closure.py; "
    f"upstream_audit_sha256={upstream_audit_sha}"
)

# === Step 5: Append to verdict file ===
with open(VERDICT_FILE, "a", encoding="utf-8") as f:
    f.write(canonical_line + "\n")
    f.write(dual_sha_companion + "\n")
    f.write(three_tuple_companion + "\n")
    f.write(mechanical_companion + "\n")
    f.flush()
    os.fsync(f.fileno())

print("Appended 4 lines to verdict file:")
print(f"  [1] Canonical:    {canonical_line[:100]}...")
print(f"  [2] Dual-SHA:     {dual_sha_companion[:80]}...")
print(f"  [3] 3-tuple:      {three_tuple_companion[:80]}...")
print(f"  [4] Mech-clos:    {mechanical_companion[:80]}...")
print()

# === Step 6: Update WP §W4-2 section IN THE SAME RUN ===
wp_text = WP_FILE.read_text(encoding="utf-8")  # (local)
TIMESTAMP = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")  # (local)

new_section = (
    f"### §W4-2. S89-FOUR-CORNER-STAGE-2-CROSS-AXIS-VERIFY-DUAL-BASIS (lizzi-spectral-functional-theorist + connes-ncg-theorist — FORECLOSED)\n"
    f"\n"
    f"**Status**: FORECLOSED (mechanical closure orchestrator-direct via "
    f"`computations/session-89/s89_w4_2_mechanical_closure.py`; no specialist-agent dispatch; no physics computation)\n"
    f"**Gate ID**: `{GATE_ID}`\n"
    f"**Trigger**: `[VERIFY]` (pre-registered Stage-2 cross-axis independent-verify; 4-cell joint AND across dual-basis × dual-axis; NOT exercised due to upstream-block foreclosure)\n"
    f"**Classification**: **GEOMETRIC** (Stage-2 cross-axis verify of single-τ-slice substrate-IS observable; 4-cell joint AND across dual-basis × dual-axis per §VII.U.2 parse-tree decision procedure + algebra-axis orthogonality MANDATORY-at-K=3 per `cross-pillar-bridge-anatomy.md`)\n"
    f"**Agent**: NOT DISPATCHED (mechanical closure per `.claude/rules/mechanical-closure-discipline.md`; designated cross-reviewers were lizzi-spectral-functional-theorist [Axis-A; CROSS pattern audits connes-axis-14state] + connes-ncg-theorist [Axis-B; CROSS pattern audits lizzi-axis-Pad16])\n"
    f"**Hypothesis**: NOT TESTED — gate foreclosed; see Verdict block.\n"
    f"**Plan reference**: `sessions/session-plan/session-89-plan-w4.md` §W4-2; foreclosure routing at Method step 2 line 196 (PREREQUISITE A.3 PASS clause; redirects to mechanical closure on A.3 ≠ PASS) + §\"Wave 4 → Waves 2/7 Decision Point\" line 1205 (A.10 dispatch BLOCKED until A.3 ∈ {{PASS, INFO}}).\n"
    f"\n"
    f"**MCP Pre-Compute Audit**:\n"
    f"- Skill Phase 2 step 4 mandates MCP query before computation. Operationally, the upstream-block topology check supersedes the MCP query: `S89-CONNES-KAROUBI-PAIRING-BDG-RESTRICTED-INFRASTRUCTURE` has verdict FAIL on disk (audit_sha256={upstream_audit_sha}); plan §W4-2 Method step 2 line 196 specifies PRE-REG-INC routing on this condition. Mechanical closure dispatched.\n"
    f"- Intra-wave prereq §W4-1 ({INTRA_WAVE_PREREQ}) verdict={a11_status} (audit_sha256={a11_audit_sha[:16]}...). A.11 PASS confirms substrate-canonical 14-state basis is structurally robust; this prerequisite is satisfied. The cross-wave A.3 FAIL is the sole foreclosure trigger.\n"
    f"\n"
    f"**Verdict** (verbatim from `computations/session-89/s89_gate_verdicts.txt`):\n"
    f"\n"
    f"```\n"
    f"{canonical_line}\n"
    f"{dual_sha_companion}\n"
    f"{three_tuple_companion}\n"
    f"{mechanical_companion}\n"
    f"```\n"
    f"\n"
    f"**Results** (PRE-REG-INC, no physics computation):\n"
    f"\n"
    f"(a) **Foreclosure topology**: A.10 (4-corner dual-basis Stage-2 cross-axis verify) requires the lizzi-axis cross-reviewer to consume A.3 Connes-Karoubi pairing canonical infrastructure (per plan §W4-2 Method step 3 dispatch: lizzi receives A.3 npz and audits the connes-axis 14-state operationalization under the spectral-functional axis criterion). With A.3 FAIL on disk, the lizzi-axis cross-reviewer cannot perform sub-test (ii) (Connes-Karoubi pairing residue at L_max=10 within Class-B 0.1%). Composite Stage-2 PASS-AND across all 4 cells therefore cannot be evaluated.\n"
    f"\n"
    f"(b) **Intra-wave prereq satisfaction**: §W4-1 (A.11) `{INTRA_WAVE_PREREQ}` verdict = `{a11_status}` (rank_natural=11 ≤ rank_W5b50_Pad=18; null_natural_dim=0; sub-tests (a)/(b)/(c) all PASS). The substrate-canonical 14-state basis is structurally robust; A.10's dual-basis dispatch (P_+-projected-16state vs substrate-canonical-14state) HAS the natural-rep basis available. The block on A.10 is exclusively the cross-wave A.3 dependency.\n"
    f"\n"
    f"(c) **4-tuple** (pre-registered, NOT exercised at compute-time):\n"
    f"   - `value = '{value_str}'`\n"
    f"   - `scheme = joint-theorem-promotion-stage-2-PASS-AND`\n"
    f"   - `convention = four-corner-dual-basis-stage-2-cross-axis-verify`\n"
    f"   - `L_max = 10`\n"
    f"\n"
    f"(d) **3-tuple annotation**: sign_verdict=N/A (PASS-AND aggregation non-signed); magnitude_verdict=FAIL (foreclosure); regime_verdict=VALID (foreclosure topology well-posed under `mechanical-closure-discipline.md`).\n"
    f"\n"
    f"(e) **Solution-space implication** (foreclosure-side, not the substrate-physics PASS/FAIL the gate would have produced if dispatched):\n"
    f"   - **FAIL (foreclosure)** ⟹ §VII.U.2 STAGE-1-CANDIDATE → STAGE-3-PERMANENT promotion is DEFERRED to S90+. The §W5b-50 4-corner classification of the rank-deficiency observable remains at STAGE-1-CANDIDATE; one of the 4 cells (lizzi-axis Connes-Karoubi pairing residue evaluation) cannot be evaluated at this session.\n"
    f"   - The §W4-1 PASS verdict (rank-deficiency natural-rep robust) constructively confirms the substrate-IS reading of W-16 §IV.5 ANNOTATION-1 (the (H ⊕ M_3, 7-state) sub-block restriction); but Stage-3-PERMANENT eligibility under the dual-basis × dual-axis 4-cell joint AND requires A.3 PASS for the lizzi-axis cell, which is absent.\n"
    f"\n"
    f"(f) **Carry-forward to S90 plan**: CF-W4-2-DEFERRED — re-dispatch 4-corner dual-basis Stage-2 verify post-A.3 PASS. Reuses §W4-1 PASS verdict (A.11 audit_sha256={a11_audit_sha[:16]}...) + S90's forthcoming A.3 PASS verdict. 4-field spec: What = re-dispatch §W4-2 Stage-2 verify with both A.3 PASS + A.11 PASS prereqs. Inputs = §VII.U.2 STAGE-1-CANDIDATE entry text + A.3 PASS npz (S90) + A.11 14-state SDP npz (S89 §W4-1 `s89_w4_substrate_canonical_14state_sdp.npz`) + §W5b-50 16-state Pad npz (`s88_w5b_connes_distance_16x16_grid.npz`). Gate = composite PASS-AND across 4 cells per plan §W4-2 substitution chain. Effort = 1.0 wave-equivalents (matches plan §W4-2 estimate).\n"
    f"\n"
    f"(g) **Artifacts**:\n"
    f"   - Closure script: `computations/session-89/s89_w4_2_mechanical_closure.py` (this script; content_sha256={content_sha})\n"
    f"   - No data file (.npz) emitted (no physics computation)\n"
    f"   - No plot (.png) emitted (no physics computation)\n"
    f"\n"
    f"**Substrate framing** (verbatim from plan §W4-2 substrate framing block, declarative for documentation):\n"
    f"\n"
    f"The 4-corner classification at `permanent-results-registry.md §VII.U.2` IS the substrate's parse-tree decision procedure for SDP rank-deficiency observables on `A_F = ℂ ⊕ ℍ ⊕ M_3(ℂ)`. The §W5b-50 rank-deficiency observable IS a substrate-IS structural property of `A_F`; its corner assignment IS substrate-IS. The dual-basis dispatch (P_+-projected-16state vs substrate-canonical-14state) tests whether basis choice is a representation artifact OR a substrate-IS property; the dual-axis dispatch (lizzi-axis vs connes-axis) tests whether the spectral-functional / NCG-axiomatic structural readings agree on the substrate-IS corner assignment. Direction-of-explanation: substrate algebra IS the 14-real-dimensional Hermitian elements ⟶ SDP rank-deficiency IS a substrate-IS property ⟶ 4-corner classification IS the substrate's parse-tree decision procedure ⟶ Stage-2 cross-axis verify IS the structural test that the corner assignment is stable.\n"
)

# Replace the §W4-2 pending block in WP. The pending block in WP starts at
# "### §W4-2." and continues through to the next "---" separator.
old_section_pattern = re.compile(  # (local)
    r"### §W4-2\. S89-FOUR-CORNER-STAGE-2-CROSS-AXIS-VERIFY-DUAL-BASIS.*?(?=\n---\n)",
    re.DOTALL,
)
match_wp = old_section_pattern.search(wp_text)  # (local)
assert match_wp is not None, (
    "WP §W4-2 section not found via regex; cannot perform mechanical-closure WP update"
)

new_wp_text = (  # (local)
    wp_text[:match_wp.start()]
    + new_section
    + wp_text[match_wp.end():]
)

with open(WP_FILE, "w", encoding="utf-8") as f:
    f.write(new_wp_text)
    f.flush()
    os.fsync(f.fileno())

print(f"Updated WP §W4-2 section in {WP_FILE}")
print(f"  old section length: {match_wp.end() - match_wp.start()} chars")
print(f"  new section length: {len(new_section)} chars")
print()

# === Step 7: Self-verify (re-read both files) ===
verdict_text_after = VERDICT_FILE.read_text(encoding="utf-8")  # (local)
assert GATE_ID in verdict_text_after, "Verdict file missing GATE_ID after write"
assert audit_sha in verdict_text_after, "Verdict file missing closure audit_sha256"
assert "PRE-REG-INC_blocked_by" in verdict_text_after, "Verdict file missing PRE-REG-INC marker"

wp_text_after = WP_FILE.read_text(encoding="utf-8")  # (local)
assert "FORECLOSED" in wp_text_after, "WP missing FORECLOSED status marker after write"
assert audit_sha in wp_text_after, "WP missing closure audit_sha256 after write"
assert upstream_audit_sha in wp_text_after, "WP missing upstream A.3 audit_sha256 after write"

print("Self-verification PASS:")
print(f"  - verdict file contains GATE_ID + audit_sha + PRE-REG-INC marker")
print(f"  - WP contains FORECLOSED + closure audit_sha + upstream audit_sha")
print()
print("=== §W4-2 mechanical closure complete ===")
print(f"composite verdict: FAIL (PRE-REG-INC; foreclosed by {UPSTREAM_GATE} FAIL)")
