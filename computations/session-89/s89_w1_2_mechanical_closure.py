"""
S89 W1-2 Mechanical Closure Script
==================================

Per `.claude/rules/mechanical-closure-discipline.md` §"When mechanical closure
IS acceptable" — orchestrator-authored mechanical closure of an upstream-blocked
gate, with no specialist-agent dispatch and no physics computation.

Upstream-block topology
-----------------------
- Gate being closed:    S89-L-H-CANONICAL-RE-PINNING-CASCADE-TAIL-13OOM (§W1-2)
- Upstream prereq:      S89-F-M-SPECIES-MULTIPLICITY-LOOKUP-TABLE (§W1-3)
- Upstream verdict:     composite=FAIL (sign=PASS, magnitude=FAIL, regime=VALID)
                        per `computations/session-89/s89_gate_verdicts.txt`
- Plan foreclosure:     `sessions/session-plan/session-89-plan-w1.md` §W1-3 §11
                        line 931: "Forecloses §W1-2 on §W1-3-output dependency"
- User adjudication:    2026-05-10 Stage-2-routing-question; user chose
                        "Foreclose §W1-2 only; dispatch §W1-4"
- Wave-context:         covered_count=1 of wave-total 4 < N_PLANNING_DEFECT_THRESHOLD=4
                        (no planning defect; mechanical closure within rule scope)

This script
-----------
(a) extracts the FULL 64-char §W1-3 audit_sha256 from the verdict file via regex
(b) computes per-gate-distinct audit_sha256 for §W1-2 mechanical closure
(c) appends FAIL verdict line + dual-SHA companion + mechanical-closure companion
    (per `mechanical-closure-discipline.md §"Audit-trail signature"`)
(d) updates WP §W1-2 section IN THE SAME RUN with Status/Verdict/Results/
    Substrate-framing/Carry-forward blocks
(e) self-verifies: re-reads verdict file + WP, asserts presence of
    foreclosure markers; sig_5 SHA-uniqueness check against §W1-1 + §W1-3

Single-execution discipline: per `mechanical-closure-discipline.md §"Carry-forward
script-bytes immutability"`, this script SHOULD be considered immutable after
first execution; the recorded `content_sha256` is the SHA of these bytes at
the time of emission.
"""

import sys
import os
os.environ.setdefault('OMP_NUM_THREADS', '8')
import hashlib
import json
import re
from collections import OrderedDict
from datetime import datetime, timezone
from pathlib import Path

# Add canonical_constants to path (S34+ MANDATORY per math-scripts.md, even
# when the closure does not consume framework numerical constants — discipline
# enforces the import surface uniformly across compute-mode + closure-mode scripts).
sys.path.insert(0, str(Path("computations/_shared").resolve()))
from canonical_constants import *  # noqa: F401, F403

# === Paths ===
ROOT = Path(".").resolve()  # (local)
VERDICT_FILE = ROOT / "computations" / "session-89" / "s89_gate_verdicts.txt"  # (local)
WP_FILE = ROOT / "sessions" / "session-89" / "session-89-w1-workingpaper.md"  # (local)
PLAN_FILE = ROOT / "sessions" / "session-plan" / "session-89-plan-w1.md"  # (local)
THIS_SCRIPT = ROOT / "computations" / "session-89" / "s89_w1_2_mechanical_closure.py"  # (local)

# === Gate identity ===
GATE_ID = "S89-L-H-CANONICAL-RE-PINNING-CASCADE-TAIL-13OOM"  # (local)
UPSTREAM_GATE = "S89-F-M-SPECIES-MULTIPLICITY-LOOKUP-TABLE"  # (local)

print(f"Mechanical closure: {GATE_ID}")
print(f"Upstream-block source: {UPSTREAM_GATE}")
print(f"Verdict file: {VERDICT_FILE}")
print(f"Working paper: {WP_FILE}")
print()

# === Step 1: Extract FULL 64-char §W1-3 audit_sha256 from verdict file ===
verdict_text = VERDICT_FILE.read_text(encoding="utf-8")  # (local)

# Regex: gate-ID at line-start, FAIL/PASS/INFO status, then audit_sha256=<64-hex>
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

# Mechanical closure is ONLY admissible when upstream verdict ≠ PASS per
# mechanical-closure-discipline.md clause 1.
assert upstream_status != "PASS", (
    f"Mechanical closure of §W1-2 NOT admissible: upstream {UPSTREAM_GATE} "
    f"reports PASS, so §W1-2 should dispatch normally rather than foreclose."
)
print(f"Upstream §W1-3 verdict: {upstream_status}")
print(f"Upstream audit_sha256 (full 64-char): {upstream_audit_sha}")
print()

# === Step 2: Build per-gate-distinct input-pin map for §W1-2 closure ===
input_pin_map = OrderedDict([  # (local)
    ("_gate_id", GATE_ID),
    ("_wp_id", "W1-2"),
    ("_session", "S89"),
    ("_closure_type", "mechanical_upstream_block"),
    ("_upstream_gate", UPSTREAM_GATE),
    ("_upstream_status", upstream_status),
    ("_upstream_audit_sha", upstream_audit_sha),
    ("_plan_clause", "session-89-plan-w1.md §W1-3 §11 line 931 (explicit foreclosure on §W1-3 FAIL)"),
    ("_user_adjudication_date", "2026-05-10"),
    ("_user_adjudication_choice", "Foreclose §W1-2 only; dispatch §W1-4"),
    ("_dispatched", False),
    ("_scheme", "substrate-pinned-T_H-1.057-MeV-SM-species"),
    ("_convention", "multi-species-stefan-boltzmann-with-supersedes-token"),
    ("_L_max", 10),
    ("_carry_forward_S90", "CF-W1-3-RETRY (§W1-3 refined cross-check) + CF-W1-2-DEFERRED (§W1-2 re-execution)"),
])
audit_sha = hashlib.sha256(  # (local)
    json.dumps(input_pin_map, sort_keys=False).encode("utf-8")
).hexdigest()
audit_sha_short = audit_sha[:16]  # (local)

# Content SHA over closure-script bytes (verdict-permanence audit trail)
this_script_bytes = THIS_SCRIPT.read_bytes() if THIS_SCRIPT.exists() else b""  # (local)
content_sha = hashlib.sha256(this_script_bytes).hexdigest()  # (local)
content_sha_short = content_sha[:16]  # (local)

print(f"§W1-2 closure audit_sha256:   {audit_sha}")
print(f"§W1-2 closure content_sha256: {content_sha}")
print()

# === Step 3: Sig_5 SHA-uniqueness check against existing verdict-file entries ===
existing_shas = set(re.findall(r"audit_sha256=([0-9a-f]{64})", verdict_text))  # (local)
assert audit_sha not in existing_shas, (
    f"Sig_5 collision: §W1-2 closure audit_sha256={audit_sha} duplicates an "
    f"existing entry in {VERDICT_FILE}. Mechanical closure ABORTED. "
    f"Investigate per .claude/rules/v3-closure-recovery.md sig_5 sub-section."
)
print(
    f"Sig_5 SHA-uniqueness check: PASS "
    f"(closure SHA distinct from {len(existing_shas)} existing entries)"
)
print()

# === Step 4: Construct verdict-line triple ===
value_str = f"PRE-REG-INC_blocked_by_{UPSTREAM_GATE}_{upstream_status}"  # (local)
canonical_line = (  # (local)
    f"{GATE_ID}: FAIL -- value='{value_str}' "
    f"scheme=substrate-pinned-T_H-1.057-MeV-SM-species "
    f"convention=multi-species-stefan-boltzmann-with-supersedes-token "
    f"L_max=10 "
    f"audit_sha256={audit_sha} "
    f"content_sha256={content_sha} "
    f"schema_version=S84+"
)
dual_sha_companion = (  # (local)
    f"# audit_sha256_short={audit_sha_short} "
    f"content_sha256_short={content_sha_short} "
    f"# {GATE_ID} dual-SHA companion row (W9a-99 split)"
)
mechanical_companion = (  # (local)
    f"# {GATE_ID} mechanical closure: PRE-REG-INC per "
    f"session-89-plan-w1.md §W1-3 §11 line 931 (forecloses §W1-2 on §W1-3 FAIL); "
    f"deferred to S90 (CF-W1-3-RETRY + CF-W1-2-DEFERRED); "
    f"required prereqs: [{UPSTREAM_GATE}=PASS_or_INFO]; "
    f"closure_script=computations/session-89/s89_w1_2_mechanical_closure.py; "
    f"upstream_audit_sha256={upstream_audit_sha}; "
    f"user_adjudication=2026-05-10_Foreclose-W1-2-only-dispatch-W1-4"
)

# === Step 5: Append to verdict file (POSIX O_APPEND single-shot write + fsync) ===
with open(VERDICT_FILE, "a", encoding="utf-8") as f:
    f.write(canonical_line + "\n")
    f.write(dual_sha_companion + "\n")
    f.write(mechanical_companion + "\n")
    f.flush()
    os.fsync(f.fileno())

print("Appended 3 lines to verdict file:")
print(f"  [1] Canonical:   {canonical_line[:100]}...")
print(f"  [2] Dual-SHA:    {dual_sha_companion[:80]}...")
print(f"  [3] Mech-clos:   {mechanical_companion[:80]}...")
print()

# === Step 6: Update WP §W1-2 section IN THE SAME RUN ===
wp_text = WP_FILE.read_text(encoding="utf-8")  # (local)
TIMESTAMP = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")  # (local)

new_section = (
    f"### §W1-2. S89-L-H-CANONICAL-RE-PINNING-CASCADE-TAIL-13OOM (mack-cosmic-bridge — FORECLOSED)\n"
    f"\n"
    f"**Status**: FORECLOSED (mechanical closure orchestrator-direct via "
    f"`computations/session-89/s89_w1_2_mechanical_closure.py`; no specialist-agent dispatch; no physics computation)\n"
    f"**Gate ID**: `{GATE_ID}`\n"
    f"**Trigger**: `[VERIFY]` + `[AUDIT]` (composite; pre-registered but NOT exercised due to upstream-block foreclosure)\n"
    f"**Classification**: **PHONONIC + cosmological-observable** (substrate-pinned multi-species Stefan-Boltzmann correction to Hawking-radiation luminosity; cascade-tail closure leverage on §W1c-69 13-OOM gap)\n"
    f"**Agent**: NOT DISPATCHED (mechanical closure per `.claude/rules/mechanical-closure-discipline.md`)\n"
    f"**Hypothesis**: NOT TESTED — gate foreclosed; see Verdict block.\n"
    f"**Plan reference**: `sessions/session-plan/session-89-plan-w1.md` §W1-2; foreclosure routing at `sessions/session-plan/session-89-plan-w1.md` §W1-3 §11 line 931 (FAIL branch: \"Forecloses §W1-2 on §W1-3-output dependency\").\n"
    f"\n"
    f"**Substrate framing** (verbatim from plan §W1-2 §13; declarative for documentation, not exercised at compute-time):\n"
    f"\n"
    f"> T_H = 1.057 MeV is SUBSTRATE-PINNED (per S88 W6 §V.1; the substrate's spectral-action moment ratio at horizon-spanning Peter-Weyl sectors fixes T_H structurally, NOT externally). The Hawking-radiation luminosity L_H is an EMERGENT cosmological observable from the substrate's emergent area-theorem (a_2 Seeley-DeWitt coefficient → emergent gravity → emergent BH thermodynamics). FORBIDDEN: 'BH evaporates IN spacetime emitting Hawking radiation'. REQUIRED direction: substrate spectral moments → emergent area-theorem → emergent T_H → emergent L_H. The species-multiplicity factor g_*(T_H_substrate) IS the substrate's emergent count of phononic excitation channels at T_H_substrate, derived through the substrate's T_H(g) cooling cascade traversing SM-species mass thresholds (§W1-3 lookup table).\n"
    f"\n"
    f"**Single-τ-slice level**: §W1-2 was pre-registered at Level 1 single-τ-slice substrate-IS at τ_fold = 0.190 (cascade-tail evaluation point fixed at the §W1c-69 mass scale). Foreclosed; not exercised.\n"
    f"\n"
    f"**MCP Pre-Compute Audit**: NOT EXECUTED (no compute dispatched; the mechanical closure is orchestrator-direct).\n"
    f"\n"
    f"**Verdict**: **FAIL** — composite=FAIL via mechanical closure. Per `.claude/rules/mechanical-closure-discipline.md §\"Audit-trail signature\"`, the canonical verdict-line triple emitted to `computations/session-89/s89_gate_verdicts.txt`:\n"
    f"\n"
    f"```\n"
    f"{canonical_line}\n"
    f"{dual_sha_companion}\n"
    f"{mechanical_companion}\n"
    f"```\n"
    f"\n"
    f"**Mechanical closure justification** (per `mechanical-closure-discipline.md §\"When mechanical closure IS acceptable\"` clauses 1-5):\n"
    f"\n"
    f"1. **Upstream-block topology**: §W1-3 (`{UPSTREAM_GATE}`) closed composite=FAIL with `audit_sha256={upstream_audit_sha}`. §W1-2 reads `g_eff_at_T_H_substrate` and `T_H_initial` from §W1-3's .npz output as intra-wave dependency (plan §W1-2 §6 step 1, line 543). §W1-3's cross-check at T=1 MeV deviated 12.48% (vs the 10% RATIO tolerance), and the cross-check at T=100 GeV deviated 13.87%; the §W1-3 verdict is composite=FAIL per the pre-registered rule \"≤ 1 anchor PASS\" (1/3 anchors PASS). Plan §W1-3 §11 line 931 (FAIL branch) explicitly: *\"Forecloses §W1-2 on §W1-3-output dependency (§W1-2 cannot use the lookup table; routes back to single-species L_H_eq1 fallback or alternative species-multiplicity model).\"*\n"
    f"2. **Verdict honesty**: emitted as FAIL with `value='PRE-REG-INC_blocked_by_{UPSTREAM_GATE}_FAIL'` per the canonical pattern; never PASS.\n"
    f"3. **Per-gate-distinct audit_sha256**: closure `audit_sha256={audit_sha}` is structurally distinct from §W1-1 (`6db37f7c...`), §W1-3 (`6d6607fa...`), and (forthcoming) §W1-4 entries. Sig_5 SHA-uniqueness is preserved by construction via `_gate_id`/`_wp_id`/`_scheme`/`_convention` identity keys in the input-pin map.\n"
    f"4. **Audit-trail signature**: canonical `value=` field names the blocking prereq + status; the upstream §W1-3 audit_sha256 is recorded in the mechanical-closure companion row for full audit-trail traceability (a downstream auditor can grep the verdict file for `upstream_audit_sha256={upstream_audit_sha}` to identify the §W1-3 verdict line that triggered the foreclosure).\n"
    f"5. **Working-paper update IS in-script**: this WP §W1-2 section is updated by the same script execution (`s89_w1_2_mechanical_closure.py`) that emits the verdict-line triple; no S82/S84 task-complete-lie pattern.\n"
    f"\n"
    f"**User-adjudicated routing** (Stage-2 decision point 2026-05-10): \"Foreclose §W1-2 only; dispatch §W1-4\". The user chose Option (a) of the orchestrator's AskUserQuestion routing, honoring the explicit plan-pinned §W1-2 foreclosure while permitting §W1-4 dispatch (plan §11 §W1-3 FAIL branch is silent on §W1-4; §W1-4's PASS criterion is on n_PBH band-edge tension at §W1c-69 posterior, structurally orthogonal to §W1-3's lookup-table cross-check validity).\n"
    f"\n"
    f"**Results**: NOT COMPUTED. The §W1-2 producing script `s89_w1_l_h_canonical_repinning_cascade_tail.py` was NOT created. No L_H_canonical, L_H_eq1, log10_ratio, f_M_at_W1c69, |delta_log10|, Step5_residual_pre/post_correction, g_eff_at_T_H_substrate consumption, supersedes-token grep-extraction from S88 verdict file, dual-SHA emission, or `L_H_canonical_FW` canonical_constants promotion was performed.\n"
    f"\n"
    f"**What FORECLOSE means for solution space**:\n"
    f"\n"
    f"- The §W1c-69 13-OOM cascade-tail underflow corridor remains UNCLOSED at the substrate-multi-species L_H correction level in S89. §W1-1's FAIL (substrate-IS NCG-axiomatic horizon-microstate count via single-pole leading-order CM-1995 §III.4 with naive `Tr − R_CM` normalization) closed one corridor; the §W1-2 mechanical foreclosure leaves the multi-species-L_H corridor open for S90 evaluation contingent on §W1-3 PASS or INFO with refined threshold-suppression treatment.\n"
    f"- Per `.claude/rules/epistemic-discipline.md` \"Pre-registered gates are the evidence — everything else is commentary\": the foreclosure honors the pre-registered routing for §W1-3 FAIL, and overriding it would be a Class-3 PROHIBITED_ACTIONS adjacency (post-hoc routing-table editing). Honoring the foreclosure preserves the framework's pre-registration discipline.\n"
    f"- The agent's structural-explanation argument (§W1-3 deviations are Boltzmann threshold-suppression at near-threshold species, NOT cascade-form structural failures) IS substantive substrate-physics knowledge that informs the next-session plan revision (CF-W1-3-RETRY) — but does NOT retroactively modify the pre-registered foreclosure routing for THIS session.\n"
    f"\n"
    f"**Carry-forward to S90 (4-field specs per `feedback_fix-in-session-never-defer.md`)**:\n"
    f"\n"
    f"| Field | CF-W1-3-RETRY | CF-W1-2-DEFERRED |\n"
    f"|:------|:---------------|:------------------|\n"
    f"| **What** | Refine §W1-3 species-multiplicity lookup with lattice-QCD-corrected g_*(T) near Λ_QCD AND finer Boltzmann threshold-suppression at m_e (T=1 MeV) and m_W/m_top (T=100 GeV) boundaries | Re-execute §W1-2 with refined §W1-3 lookup; verify L_H_canonical = (π²/60) · g_*(T_H=1.057 MeV) · A_horizon · T_H⁴ within 0.5 log-OOM ABSOLUTE of f(M_at_W1c69) |\n"
    f"| **Inputs** | S88 W6 §V.5 cascade form (already substrate-pinned); refined Boltzmann factor `exp(-m/T)` for species near threshold (within factor 5 of T); lattice-QCD g_*(T) tables near Λ_QCD ≈ 200 MeV; PDG/Planck cross-check anchors at T ∈ {{100 GeV, 1 GeV, 1 MeV}} | S90 §W1-3 lookup .npz (PASS or INFO); S88 §W1c-69 source `sessions/archive/session-88/workshops/s88-w6-w1c-69-page1976-13oom.md`; S88 verdict file (Option A `supersedes` token grep-extraction) |\n"
    f"| **Gate** | All 3 cross-check anchors PASS within 10% RATIO at T=100 GeV, 1 GeV, 1 MeV; CF-W1-3-RETRY upgrades §W1-3 from FAIL to PASS or INFO | `|log10(L_H_canonical / L_H_eq1) − log10(f(M_at_W1c69))| < 0.5` ABSOLUTE log-OOM AND `Step5_residual_post_correction` shrinks by ≥ 1 log-OOM AND supersedes-token correctly emitted as full 64-char form |\n"
    f"| **Effort** | 1.0 wave-equiv (matches original §W1-3 estimate; refinement-only) | 0.5 wave-equiv (matches original §W1-2 estimate) |\n"
    f"\n"
    f"**4-tuple output** (declarative; not computed):\n"
    f"\n"
    f"`(value='PRE-REG-INC_blocked_by_{UPSTREAM_GATE}_FAIL', scheme=substrate-pinned-T_H-1.057-MeV-SM-species, convention=multi-species-stefan-boltzmann-with-supersedes-token, L_max=10)`\n"
    f"\n"
    f"**Files NOT produced** (foreclosed):\n"
    f"\n"
    f"| Artifact | Path | Status |\n"
    f"|:---------|:-----|:-------|\n"
    f"| Script | `computations/session-89/s89_w1_l_h_canonical_repinning_cascade_tail.py` | NOT created |\n"
    f"| Data | `computations/session-89/s89_w1_l_h_canonical_repinning_cascade_tail.npz` | NOT created |\n"
    f"| Plot | `computations/session-89/s89_w1_l_h_canonical_repinning_cascade_tail.png` | NOT created |\n"
    f"| Inventory row | `sessions/framework/registry/falsifier-master-inventory.md` (mack PRIMARY) | NOT updated |\n"
    f"| Canonical promotion | `L_H_canonical_FW` in `canonical_constants.py` | NOT promoted (FAIL path; PASS-conditional) |\n"
    f"| Mechanical closure script | `computations/session-89/s89_w1_2_mechanical_closure.py` | CREATED (this script; see audit-trail signature above) |\n"
    f"\n"
    f"**Direction of explanation** (per `phononic-framing.md`): the foreclosure is a routing decision driven by upstream-block topology, NOT a substrate-physics statement about L_H itself. L_H_canonical at substrate-pinned T_H = 1.057 MeV remains a well-defined emergent cosmological observable; the foreclosure pertains to the AVAILABILITY of substrate-IS species-multiplicity input from §W1-3, not to the L_H formula or its substrate-IS derivation.\n"
    f"\n"
    f"**Closure timestamp**: {TIMESTAMP}.\n"
    f"\n"
)

# Replace the §W1-2 stub block in WP (from "### §W1-2." to but not including
# the next "### §W1-3." line). The trailing "---" separator before §W1-3
# remains in the WP; the new section ends with a blank line that flows into it.
section_pattern = re.compile(  # (local)
    r"### §W1-2\..*?(?=\n### §W1-3\.)",
    re.DOTALL,
)
match2 = section_pattern.search(wp_text)  # (local)
assert match2 is not None, (
    f"Could not find §W1-2 section in {WP_FILE} — mechanical closure ABORTED. "
    f"Investigate WP structure (expected '### §W1-2.' heading)."
)
# match2.end() points to the position OF the "\n" before "### §W1-3." (lookahead
# pre-consumption); therefore +1 to start the slice at "### §W1-3.". The
# new_section ends with "\n\n" and we prepend "---\n\n" so the joined text
# reproduces the canonical inter-section separator "...timestamp.\n\n---\n\n### §W1-3. ...".
new_wp_text = wp_text[:match2.start()] + new_section + "---\n\n" + wp_text[match2.end()+1:]  # (local)
WP_FILE.write_text(new_wp_text, encoding="utf-8")

# === Step 7: Self-verify (re-read both files; assert presence of foreclosure markers) ===
verdict_after = VERDICT_FILE.read_text(encoding="utf-8")  # (local)
assert canonical_line in verdict_after, (
    f"Self-verify FAIL: canonical line not present in {VERDICT_FILE} after append"
)
assert audit_sha in verdict_after, (
    f"Self-verify FAIL: audit_sha256={audit_sha} not present after append"
)

wp_after = WP_FILE.read_text(encoding="utf-8")  # (local)
assert "FORECLOSED" in wp_after, "Self-verify FAIL: 'FORECLOSED' status not in WP §W1-2"
assert (
    f"PRE-REG-INC_blocked_by_{UPSTREAM_GATE}_FAIL" in wp_after
), "Self-verify FAIL: foreclosure value-string not in WP §W1-2"
assert "CF-W1-3-RETRY" in wp_after, "Self-verify FAIL: CF-W1-3-RETRY carry-forward not in WP §W1-2"
assert "CF-W1-2-DEFERRED" in wp_after, "Self-verify FAIL: CF-W1-2-DEFERRED carry-forward not in WP §W1-2"

print(f"WP §W1-2 section updated: {WP_FILE}")
print(f"  'FORECLOSED' status present:        True")
print(f"  Foreclosure value-string present:   True")
print(f"  CF-W1-3-RETRY 4-field spec present: True")
print(f"  CF-W1-2-DEFERRED 4-field spec:      True")
print()

# === Final summary ===
print("=" * 72)
print(f"§W1-2 mechanical closure COMPLETE.")
print(f"  Verdict:                  FAIL (PRE-REG-INC blocked by §W1-3 FAIL)")
print(f"  Closure audit_sha256:     {audit_sha}")
print(f"  Closure content_sha256:   {content_sha}")
print(f"  Upstream §W1-3 audit_sha: {upstream_audit_sha}")
print(f"  Sig_5 SHA-uniqueness:     PASS (vs {len(existing_shas)} existing entries)")
print(f"  WP §W1-2 section:         UPDATED in-script")
print(f"  Carry-forward:            CF-W1-3-RETRY + CF-W1-2-DEFERRED → S90")
print("=" * 72)

sys.exit(0)
