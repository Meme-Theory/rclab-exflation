"""
S89 W2-2 Mechanical Closure Script
==================================

Per `.claude/rules/mechanical-closure-discipline.md` §"When mechanical closure
IS acceptable" — orchestrator-authored mechanical closure of an upstream-blocked
gate, with no specialist-agent dispatch and no physics computation.

Upstream-block topology
-----------------------
- Gate being closed:    S89-BCS-PHYSICS-GROUNDED-R-SUBSTRATE-LANDAU-PATH (§W2-2)
- Upstream prereq:      S89-CONNES-KAROUBI-PAIRING-BDG-RESTRICTED-INFRASTRUCTURE (§W2-1)
- Upstream verdict:     composite=FAIL (sign=N/A, magnitude=FAIL, regime=VALID)
                        per `computations/session-89/s89_gate_verdicts.txt`
- Plan foreclosure:     `sessions/session-plan/session-89-plan-w2.md` §W2-2.6 line
                        228: "PREREQUISITE: A.3 PASS verdict. If `S89-CONNES-
                        KAROUBI-PAIRING-BDG-RESTRICTED-INFRASTRUCTURE: PASS` is
                        NOT yet in `s89_gate_verdicts.txt`, dispatch to
                        mechanical closure."
                        + plan §W2 §"Wave 2 Decision Point Prerequisites" item 1
                        line 23 (intra-wave dependency chain A.3 → A.4)
- Wave-context:         covered_count=2 of wave-total 5 < N_PLANNING_DEFECT_THRESHOLD=4
                        (no planning defect; mechanical closure within rule scope).

This script
-----------
(a) extracts the FULL 64-char §W2-1 audit_sha256 from the verdict file via regex
(b) computes per-gate-distinct audit_sha256 for §W2-2 mechanical closure
(c) appends FAIL verdict line + dual-SHA companion + mechanical-closure companion
    + 3-tuple companion ([SIGN]+[VERIFY] composite trigger requires it)
(d) updates WP §W2-2 section IN THE SAME RUN with Status/Verdict/Results/
    Substrate-framing/Carry-forward blocks
(e) self-verifies: re-reads verdict file + WP, asserts presence of
    foreclosure markers; sig_5 SHA-uniqueness check against §W2-1.

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
WP_FILE = ROOT / "sessions" / "session-89" / "session-89-w2-workingpaper.md"  # (local)
PLAN_FILE = ROOT / "sessions" / "session-plan" / "session-89-plan-w2.md"  # (local)
THIS_SCRIPT = ROOT / "computations" / "session-89" / "s89_w2_2_mechanical_closure.py"  # (local)

# === Gate identity ===
GATE_ID = "S89-BCS-PHYSICS-GROUNDED-R-SUBSTRATE-LANDAU-PATH"  # (local)
UPSTREAM_GATE = "S89-CONNES-KAROUBI-PAIRING-BDG-RESTRICTED-INFRASTRUCTURE"  # (local)

print(f"Mechanical closure: {GATE_ID}")
print(f"Upstream-block source: {UPSTREAM_GATE}")
print(f"Verdict file: {VERDICT_FILE}")
print(f"Working paper: {WP_FILE}")
print()

# === Step 1: Extract FULL 64-char §W2-1 audit_sha256 from verdict file ===
verdict_text = VERDICT_FILE.read_text(encoding="utf-8")  # (local)

sha_pattern = re.compile(  # (local)
    r"^" + re.escape(UPSTREAM_GATE) + r":\s+(\w+).*?audit_sha256=([0-9a-f]{64})",
    re.MULTILINE | re.DOTALL,
)
match = sha_pattern.search(verdict_text)  # (local)
assert match is not None, (
    f"Upstream gate {UPSTREAM_GATE} not found in {VERDICT_FILE} — "
    f"cannot proceed with mechanical closure"
)
upstream_status = match.group(1)  # (local)
upstream_audit_sha = match.group(2)  # (local)
upstream_audit_sha_short = upstream_audit_sha[:16]  # (local)

assert upstream_status != "PASS", (
    f"Mechanical closure of §W2-2 NOT admissible: upstream {UPSTREAM_GATE} "
    f"reports PASS, so §W2-2 should dispatch normally rather than foreclose."
)
print(f"Upstream §W2-1 verdict: {upstream_status}")
print(f"Upstream audit_sha256 (full 64-char): {upstream_audit_sha}")
print()

# === Step 2: Build per-gate-distinct input-pin map for §W2-2 closure ===
input_pin_map = OrderedDict([  # (local)
    ("_gate_id", GATE_ID),
    ("_wp_id", "W2-2"),
    ("_session", "S89"),
    ("_closure_type", "mechanical_upstream_block"),
    ("_upstream_gate", UPSTREAM_GATE),
    ("_upstream_status", upstream_status),
    ("_upstream_audit_sha", upstream_audit_sha),
    ("_plan_clause", "session-89-plan-w2.md §W2-2.6 line 228 (PREREQUISITE A.3 PASS) + §W2 \"Wave 2 Decision Point Prerequisites\" item 1 line 23 (intra-wave dep chain)"),
    ("_dispatched", False),
    ("_designated_agent", "landau-condensed-matter-theorist (PRIMARY); volovik + connes CO-AUTHORS — NOT DISPATCHED"),
    ("_scheme", "Cohomology-asymmetry-test-class-B"),
    ("_convention", "BCS-physics-grounded-R-substrate-Volovik-2003-7.2-polycritical"),
    ("_L_max", 10),
    ("_carry_forward_S90", "CF-W2-1-RETRY (re-pin xc1 tolerance per Class-8.3 publication-precision; clarify xc1 vs xc2 observable identity) + CF-W2-2-DEFERRED (re-execute landau path post-A.3 PASS)"),
])
audit_sha = hashlib.sha256(  # (local)
    json.dumps(input_pin_map, sort_keys=False).encode("utf-8")
).hexdigest()
audit_sha_short = audit_sha[:16]  # (local)

this_script_bytes = THIS_SCRIPT.read_bytes() if THIS_SCRIPT.exists() else b""  # (local)
content_sha = hashlib.sha256(this_script_bytes).hexdigest()  # (local)
content_sha_short = content_sha[:16]  # (local)

print(f"§W2-2 closure audit_sha256:   {audit_sha}")
print(f"§W2-2 closure content_sha256: {content_sha}")
print()

# === Step 3: Sig_5 SHA-uniqueness check ===
existing_shas = set(re.findall(r"audit_sha256=([0-9a-f]{64})", verdict_text))  # (local)
assert audit_sha not in existing_shas, (
    f"Sig_5 collision: §W2-2 closure audit_sha256={audit_sha} duplicates an "
    f"existing entry in {VERDICT_FILE}. Mechanical closure ABORTED."
)
print(
    f"Sig_5 SHA-uniqueness check: PASS "
    f"(closure SHA distinct from {len(existing_shas)} existing entries)"
)
print()

# === Step 4: Construct verdict-line triple + 3-tuple (SIGN+VERIFY trigger) ===
value_str = f"PRE-REG-INC_blocked_by_{UPSTREAM_GATE}_{upstream_status}"  # (local)
canonical_line = (  # (local)
    f"{GATE_ID}: FAIL -- value='{value_str}' "
    f"scheme=Cohomology-asymmetry-test-class-B "
    f"convention=BCS-physics-grounded-R-substrate-Volovik-2003-7.2-polycritical "
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
    f"# {GATE_ID} 3-tuple annotation (S87 schema-v2; foreclosure under [SIGN]+[VERIFY] composite trigger)"
)
mechanical_companion = (  # (local)
    f"# {GATE_ID} mechanical closure: PRE-REG-INC per "
    f"session-89-plan-w2.md §W2-2.6 line 228 (PREREQUISITE A.3 PASS); "
    f"deferred to S90 (CF-W2-1-RETRY + CF-W2-2-DEFERRED); "
    f"required prereqs: [{UPSTREAM_GATE}=PASS]; "
    f"closure_script=computations/session-89/s89_w2_2_mechanical_closure.py; "
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

# === Step 6: Update WP §W2-2 section ===
wp_text = WP_FILE.read_text(encoding="utf-8")  # (local)
TIMESTAMP = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")  # (local)

new_section = (
    f"### §W2-2. S89-BCS-PHYSICS-GROUNDED-R-SUBSTRATE-LANDAU-PATH (landau-condensed-matter-theorist — FORECLOSED)\n"
    f"\n"
    f"**Status**: FORECLOSED (mechanical closure orchestrator-direct via "
    f"`computations/session-89/s89_w2_2_mechanical_closure.py`; no specialist-agent dispatch; no physics computation)\n"
    f"**Gate ID**: `{GATE_ID}`\n"
    f"**Trigger**: `[SIGN]` + `[VERIFY]` (composite; pre-registered but NOT exercised due to upstream-block foreclosure)\n"
    f"**Classification**: **GEOMETRIC** (BCS spectral-action moments at polycritical pressure; (Δ_B/Δ_A)^p cancellation theorem; Cell I algebra-INVARIANT — pre-registered classification)\n"
    f"**Agent**: NOT DISPATCHED (mechanical closure per `.claude/rules/mechanical-closure-discipline.md`; designated PRIMARY = landau-condensed-matter-theorist; CO-AUTHORs = volovik-superfluid-universe-theorist + connes-ncg-theorist)\n"
    f"**Hypothesis**: NOT TESTED — gate foreclosed; see Verdict block.\n"
    f"**Plan reference**: `sessions/session-plan/session-89-plan-w2.md` §W2-2; foreclosure routing at §W2-2.6 line 228 (PREREQUISITE A.3 PASS clause; redirects to mechanical closure on A.3 ≠ PASS) + §W2 \"Wave 2 Decision Point Prerequisites\" item 1 line 23 (intra-wave dependency chain A.3 → A.4).\n"
    f"\n"
    f"**Substrate framing** (verbatim from plan §W2-2.13; declarative for documentation, not exercised at compute-time):\n"
    f"\n"
    f"> The BCS spectral-action moments Σ_BdG_A and Σ_BdG_B ARE the substrate-IS observables at the polycritical-pressure point of the Volovik 2003 §7.2 framework; they are NOT \"BCS observables in a 3He-B container.\" The polycritical pressure P_pc IS the substrate's intrinsic SC-factor degeneracy point; it is NOT a coordinate in a 3He-B-laboratory-container. The (Δ_B/Δ_A)^p cancellation theorem IS the substrate-IS structural identity that preserves the cocycle ratio under inheritance-morphism restriction; it is NOT a \"comparison between A-phase and B-phase containers.\" A_K^BdG_preimage IS the substrate algebra restricted to the BdG-inheritance-morphism image (per A.3); it is NOT \"the BdG sector of 3He-B.\" Direction of explanation: D_K eigenvalues → Hochschild cocycle norms ‖φ_67‖_BdG / ‖φ_88‖_BdG → substrate cocycle ratio canonical 7.324992 → BCS-physics-grounded R_substrate at polycritical pressure.\n"
    f"\n"
    f"**Single-τ-slice level**: §W2-2 was pre-registered at Level 1 single-τ-slice substrate-IS at τ_fold = 0.190 (R-PROTECTED). Foreclosed; not exercised.\n"
    f"\n"
    f"**MCP Pre-Compute Audit**: NOT EXECUTED (no compute dispatched; the mechanical closure is orchestrator-direct).\n"
    f"\n"
    f"**Verdict**: **FAIL** — composite=FAIL via mechanical closure. Per `.claude/rules/mechanical-closure-discipline.md §\"Audit-trail signature\"`, the canonical verdict-line emitted to `computations/session-89/s89_gate_verdicts.txt`:\n"
    f"\n"
    f"```\n"
    f"{canonical_line}\n"
    f"{dual_sha_companion}\n"
    f"{three_tuple_companion}\n"
    f"{mechanical_companion}\n"
    f"```\n"
    f"\n"
    f"**Mechanical closure justification** (per `mechanical-closure-discipline.md §\"When mechanical closure IS acceptable\"` clauses 1-5):\n"
    f"\n"
    f"1. **Upstream-block topology**: §W2-1 (`{UPSTREAM_GATE}`) closed composite=FAIL with `audit_sha256={upstream_audit_sha}`. §W2-2 reads `R_canonical_value`, `cocycle_phi67_BdG_restriction`, and `cocycle_phi88_BdG_restriction` from §W2-1's .npz output (plan §W2-2.7 input_pin_map line 294-296: `s89_w2_a3_connes_karoubi_pairing.npz` is **CRITICAL: A.3 PASS prereq**). Plan §W2-2.6 line 228 (verbatim): *\"PREREQUISITE: A.3 PASS verdict. If `S89-CONNES-KAROUBI-PAIRING-BDG-RESTRICTED-INFRASTRUCTURE: PASS` is NOT yet in `computations/session-89/s89_gate_verdicts.txt`, dispatch to mechanical closure ... with verdict `value='PRE-REG-INC_blocked_by_A.3_pending'`. Do NOT proceed with computation.\"*\n"
    f"2. **Verdict honesty**: emitted as FAIL with `value='PRE-REG-INC_blocked_by_{UPSTREAM_GATE}_FAIL'` per the canonical pattern; never PASS.\n"
    f"3. **Per-gate-distinct audit_sha256**: closure `audit_sha256={audit_sha}` is structurally distinct from §W2-1 (`{upstream_audit_sha_short}...`) and any other entries. Sig_5 SHA-uniqueness preserved by construction via `_gate_id`/`_wp_id`/`_scheme`/`_convention` identity keys in the input-pin map.\n"
    f"4. **Audit-trail signature**: canonical `value=` field names the blocking prereq + status; the upstream §W2-1 audit_sha256 is recorded in the mechanical-closure companion row for full audit-trail traceability (a downstream auditor can grep the verdict file for `upstream_audit_sha256={upstream_audit_sha}` to identify the §W2-1 verdict line that triggered the foreclosure).\n"
    f"5. **Working-paper update IS in-script**: this WP §W2-2 section is updated by the same script execution (`s89_w2_2_mechanical_closure.py`) that emits the verdict-line block; no S82/S84 task-complete-lie pattern.\n"
    f"\n"
    f"**Results**: NOT COMPUTED. The §W2-2 producing script `s89_w2_a4_bcs_physics_grounded_r_substrate.py` was NOT created. No R_substrate_BCS_grounded_corrected, R_substrate_BCS_grounded_original_ledger_form, Σ_BdG_A, Σ_BdG_B, polycritical_pressure_pin, or substitution chain Step 5 + Step 5' corrected derivation was performed.\n"
    f"\n"
    f"**What FORECLOSE means for solution space**:\n"
    f"\n"
    f"- The convergence of the BCS-physics-grounded path (landau path) and the NCG-axiomatic path (connes path) at the substrate cocycle ratio canonical 7.324992 remains UNVERIFIED at the §W2-2 level in S89. §W2-1's FAIL closed the Connes-Karoubi pairing infrastructure corridor for THIS session at literal pre-registered tolerances; the §W2-2 mechanical foreclosure leaves the landau-path corridor open for S90 evaluation contingent on §W2-1 PASS or INFO with refined Class-8.3-aware threshold.\n"
    f"- Per `epistemic-discipline.md` \"Pre-registered gates are the evidence — everything else is commentary\": the foreclosure honors the pre-registered routing for §W2-1 FAIL, and overriding it would be a Class-3 PROHIBITED_ACTIONS adjacency (post-hoc routing-table editing).\n"
    f"- The substrate-IS substitution chain analysis at plan-author time (§W2-2.6 Step 5 reveals the original ledger form `(Σ_A − Σ_B)/(Σ_A + Σ_B)` collapses to 0 at polycritical pressure; Step 5' corrects to `‖φ_67‖_BdG / ‖φ_88‖_BdG = 7.324992`) is preserved in the plan as substantive substrate-physics knowledge informing the next-session re-execution.\n"
    f"\n"
    f"**Carry-forward to S90 (4-field specs per `feedback_fix-in-session-never-defer.md`)**:\n"
    f"\n"
    f"| Field | CF-W2-1-RETRY | CF-W2-2-DEFERRED |\n"
    f"|:------|:--------------|:------------------|\n"
    f"| **What** | Re-author §W2-1 with (a) Class-8.3-aware xc1 tolerance ≥ 1e-5 (publication-precision floor of 6-sig-fig pins); (b) clarify xc1 vs xc2 observable identity — is `R_canonical` the cocycle ratio (7.324992) OR the HP^1 universal F_4 anchor (1.030902)? Cannot be both. | Re-execute §W2-2 landau path post-A.3 PASS; substitution chain Step 5 + Step 5' corrected derivation; Class-B 0.1% match against 7.324992 |\n"
    f"| **Inputs** | Plan §W2-1 method spec; canonical_constants pins (cocycle_norm_phi67/88, substrate_cocycle_ratio_67_88, R_universal_HP1_strict_F4); `epistemic-discipline.md §\"Publication-Precision Pre-Registration (Class 8.3)\"` MANDATORY at K=4 | S90 §W2-1 PASS or INFO npz output; substrate-pinned polycritical_pressure derivation (substrate-natural form); `inheritance-falsifier-protocol.md §\"(Δ_B/Δ_A)^p Cancellation Theorem\"` |\n"
    f"| **Gate** | xc1 PASSes at refined tolerance ≥ 1e-5 against the cocycle ratio observable; xc2 explicitly disambiguated (separate gate or removed) | `\\|R_substrate_BCS_grounded_corrected / 7.324992 − 1\\| ≤ 0.001` (Class-B 0.1% RATIO) AND sign_verdict=PASS AND regime_verdict=VALID |\n"
    f"| **Effort** | 0.5 wave-equiv (re-authoring §W2-1 with Class-8.3-aware threshold + observable disambiguation) | 3.0 wave-equiv (matches original §W2-2 estimate) |\n"
    f"\n"
    f"**4-tuple output** (declarative; not computed):\n"
    f"\n"
    f"`(value='PRE-REG-INC_blocked_by_{UPSTREAM_GATE}_FAIL', scheme=Cohomology-asymmetry-test-class-B, convention=BCS-physics-grounded-R-substrate-Volovik-2003-7.2-polycritical, L_max=10)`\n"
    f"\n"
    f"**Files NOT produced** (foreclosed):\n"
    f"\n"
    f"| Artifact | Path | Status |\n"
    f"|:---------|:-----|:-------|\n"
    f"| Producing script | `computations/session-89/s89_w2_a4_bcs_physics_grounded_r_substrate.py` | NOT created |\n"
    f"| Data | `computations/session-89/s89_w2_a4_bcs_physics_grounded_r_substrate.npz` | NOT created |\n"
    f"| Plot | `computations/session-89/s89_w2_a4_bcs_physics_grounded_r_substrate.png` | NOT created |\n"
    f"| Mechanical closure script | `computations/session-89/s89_w2_2_mechanical_closure.py` | CREATED (this script) |\n"
    f"\n"
    f"**Direction of explanation** (per `phononic-framing.md`): the foreclosure is a routing decision driven by upstream-block topology, NOT a substrate-physics statement about R_substrate_BCS-grounded itself. The substrate cocycle ratio canonical 7.324992 remains a well-defined substrate-IS observable; the foreclosure pertains to the AVAILABILITY of substrate-IS Connes-Karoubi pairing infrastructure from §W2-1 (which the literal-tolerance FAIL of §W2-1 made unavailable for this session), not to the cocycle-ratio formula or its substrate-IS derivation.\n"
    f"\n"
    f"**Closure timestamp**: {TIMESTAMP}.\n"
    f"\n"
)

# Replace the §W2-2 stub block in WP
section_pattern = re.compile(  # (local)
    r"### §W2-2\..*?(?=\n### §W2-3\.)",
    re.DOTALL,
)
match2 = section_pattern.search(wp_text)  # (local)
assert match2 is not None, (
    f"Could not find §W2-2 section in {WP_FILE} — mechanical closure ABORTED."
)
new_wp_text = wp_text[:match2.start()] + new_section + "---\n\n" + wp_text[match2.end()+1:]  # (local)
WP_FILE.write_text(new_wp_text, encoding="utf-8")

# === Step 7: Self-verify ===
verdict_after = VERDICT_FILE.read_text(encoding="utf-8")  # (local)
assert canonical_line in verdict_after
assert audit_sha in verdict_after

wp_after = WP_FILE.read_text(encoding="utf-8")  # (local)
assert "FORECLOSED" in wp_after
assert f"PRE-REG-INC_blocked_by_{UPSTREAM_GATE}_FAIL" in wp_after
assert "CF-W2-1-RETRY" in wp_after
assert "CF-W2-2-DEFERRED" in wp_after

print(f"WP §W2-2 section updated: {WP_FILE}")
print(f"  'FORECLOSED' status present:        True")
print(f"  Foreclosure value-string present:   True")
print(f"  CF-W2-1-RETRY 4-field spec present: True")
print(f"  CF-W2-2-DEFERRED 4-field spec:      True")
print()

# === Final summary ===
print("=" * 72)
print(f"§W2-2 mechanical closure COMPLETE.")
print(f"  Verdict:                  FAIL (PRE-REG-INC blocked by §W2-1 FAIL)")
print(f"  Closure audit_sha256:     {audit_sha}")
print(f"  Closure content_sha256:   {content_sha}")
print(f"  Upstream §W2-1 audit_sha: {upstream_audit_sha}")
print(f"  Sig_5 SHA-uniqueness:     PASS (vs {len(existing_shas)} existing entries)")
print(f"  WP §W2-2 section:         UPDATED in-script")
print(f"  Carry-forward:            CF-W2-1-RETRY + CF-W2-2-DEFERRED → S90")
print("=" * 72)

sys.exit(0)
