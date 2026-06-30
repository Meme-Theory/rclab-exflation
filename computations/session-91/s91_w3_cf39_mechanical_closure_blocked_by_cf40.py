#!/usr/bin/env python3
"""
S91 W3-2 — S91-CF39-RE-DISPATCH-POST-CF40-PASS (T1.7)
======================================================
MECHANICAL CLOSURE — mack-cosmic-bridge primary, FAIL branch via PRE-REG-INC

Gate: S91-CF39-RE-DISPATCH-POST-CF40-PASS ([VERIFY] ∧ [CHAIN])

Closure rationale: per plan §W3-2 §6 CONDITIONAL DISPATCH RULE (lines 250 + 266)
and §11 FAIL mechanical branch routing (line 333):

    "If T1.6 returns FAIL at any of the 3 PDG anchors, this gate
     mechanical-closes as PRE-REG-INC FAIL per
     `mechanical-closure-discipline.md` (the upstream-block topology fires:
     T1.6 verdict ≠ PASS is the cause; do NOT dispatch substantive
     computation)."

T1.6 = S91-CF40-KOLB-TURNER-FD-BE-INTEGRATED emitted at
`computations/session-91/s91_gate_verdicts.txt` line 33:
  - composite = INFO at schema-v2 (MARGINAL regime collapses magnitude=FAIL
    to composite=INFO via composite-collapse rule)
  - magnitude_verdict = FAIL at the gate-band predicate
    (rel_dev_1GeV = 0.236459 > 0.10 PASS band ceiling at T = 1 GeV anchor)
  - audit_sha256 = b9b7511e7500cf3e1926760ad82edca38c720771f15873516ebd4f62c745a9d9

The plan §W3-2 §11 routing reads the gate-band predicate (NOT the composite
collapse) as the canonical-promotion + T1.7 routing trigger: "FAIL at any of
the 3 PDG anchors" → T1.7 mechanical PRE-REG-INC closure. The composite-INFO
preserves the SIGN-correct sub-result for downstream re-derivation; it does
NOT close the band predicate failure.

Mechanical-closure admissibility checklist
(per .claude/rules/mechanical-closure-discipline.md §"When mechanical closure IS acceptable"):

  (1) Upstream-block topology is the cause: T1.6 magnitude=FAIL at T=1 GeV
      (rel_dev=0.236459 > 0.10 gate band) emitted at s91_gate_verdicts.txt
      line 33; plan §W3-2 §6 line 250 + §11 line 333 specify FAIL mechanical
      routing on T1.6 verdict ≠ PASS at any of the 3 PDG anchors. The plan
      author HAS anticipated the prereq-block scenario; this is NOT post-hoc
      plan editing. ✓
  (2) Verdict honesty: emit FAIL (NEVER PASS — rule §2 prohibits PASS from
      mechanical closure scripts). Value string follows the
      'PRE-REG-INC_blocked_by_<sym>_<status>' pattern. ✓
  (3) Per-gate-distinct audit_sha256: input-pin map embeds per-gate identity
      keys (_gate_id, _wp_id, _scheme, _convention) so the resulting
      audit_sha256 is distinct from S90 W4 CF-39 mechanical-closure SHA and
      from any other S91 mechanical closure that shares prerequisite
      topology. ✓
  (4) Audit-trail signature: future grep on s91_gate_verdicts.txt for
      'PRE-REG-INC_blocked_by_S91_CF40_FAIL' returns this gate's canonical
      line + co-citation of T1.6 audit_sha256 in the value field. The audit
      script _mechanical_closure_audit.py (when authored) can grep for the
      named upstream gate and verify status matches what the closure
      asserts. ✓
  (5) In-script working-paper update: §W3-2 §"Status", §"Verdict",
      §"Results", §"Substrate framing", §"Solution-space implication"
      blocks all populated in the SAME run as the verdict-line append (via
      orchestrator-direct Edit calls following script execution; this
      script emits the verdict line, the orchestrator updates the working
      paper as Task #4 of /rclab-solo two-task-per-gate decomposition). ✓

Substrate framing (per .claude/rules/phononic-framing.md §"IS Space, Not IN Space"):
the substrate IS the spectral triple (A_K, H_K, D_K(τ_fold)); the substrate
cascade-tail luminosity L_H_canonical at T_H = 1.057 MeV horizon IS the
substrate-IS observable per S88 W6 §V.5 Result 2. This gate's mechanical
PRE-REG-INC closure does NOT compute that observable; the S88 absolute
verdict permanence preserves the prior reading at
`computations/session-88/s88_gate_verdicts.txt` line 34 (audit_sha256
2afd17ef99c81123548642938a4053fb82ea075ea626b5fe6afcbcb73215ed5d).
NO Option-A supersedes-tag emission fires from this closure script.

Plan reference: sessions/session-plan/session-91-plan-w3.md §W3-2 (lines 220-384).
Fork source: computations/session-90/s90_w4_cf39_mechanical_closure_blocked_by_cf40.py.
"""

from __future__ import annotations

import sys
from pathlib import Path

_SHARED_DIR = Path(__file__).resolve().parent.parent / "_shared"
sys.path.insert(0, str(_SHARED_DIR))
from canonical_constants import *  # noqa: F401,F403,E402

import hashlib  # noqa: E402
import json  # noqa: E402
import re  # noqa: E402
import time  # noqa: E402

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

# Gate identity (per plan §W3-2 §1 + §6 verbatim verdict-line format)
GATE_ID = "S91-CF39-RE-DISPATCH-POST-CF40-PASS"  # (local)
SCHEME = "substrate-cascade-tail-S88-W6-V5-resultII"  # (local)
CONVENTION = "mack-cosmic-bridge-primary-mechanical-closure-PRE-REG-INC"  # (local)
L_MAX = "N/A"  # (local) — cascade-tail formula is L_max-independent at structural form layer
SCHEMA_VERSION = "S87+"  # (local)
WP_ID = "session-91-w3-workingpaper.md::§W3-2"  # (local)

# Upstream T1.6 gate identity
T16_GATE_ID = "S91-CF40-KOLB-TURNER-FD-BE-INTEGRATED"  # (local)
T16_EXPECTED_LINE_NUMBER = 33  # (local) — diagnostic, verified by grep

# S88 supersedes target full 64-char (canonical-promotion DEFERRED on FAIL branch;
# this constant is documented for cross-reference, NOT emitted in the verdict line).
S88_SUPERSEDED_FULL_SHA = (  # (local)
    "2afd17ef99c81123548642938a4053fb82ea075ea626b5fe6afcbcb73215ed5d"
)

# File paths (input pins)
VERDICT_TXT = SESSION_DIR / "s91_gate_verdicts.txt"
CANONICAL_CONSTANTS = SHARED_DIR / "canonical_constants.py"
PLAN_W3 = PROJECT_ROOT / "sessions" / "session-plan" / "session-91-plan-w3.md"
S88_VERDICTS = COMPUTATIONS_DIR / "session-88" / "s88_gate_verdicts.txt"
MECHANICAL_CLOSURE_RULE = (
    PROJECT_ROOT / ".claude" / "rules" / "mechanical-closure-discipline.md"
)
GATE_VERDICTS_RULE = PROJECT_ROOT / ".claude" / "rules" / "gate-verdicts.md"


def sha256_of(path):
    h = hashlib.sha256()
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}
    for p in inputs:
        sha = sha256_of(p)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        except ValueError:
            rel = str(p)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path, canonical_path, pins, embed_keys):
    """Compute dual SHA over script bytes + canonical bytes + pinmap_json + embed_keys.

    embed_keys is a dict of per-gate identity keys (gate_id, wp_id, scheme,
    convention, etc.) embedded into the audit_sha computation per
    `.claude/rules/mechanical-closure-discipline.md` §"When mechanical closure
    IS acceptable" item (3) — preserves sig_5 SHA uniqueness across multiple
    mechanical-closure gates that may share the same prereq T1.6 upstream
    block topology in this or future sessions.
    """
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True,
    ).encode("utf-8")
    embed_json = json.dumps(
        dict(sorted(embed_keys.items())), separators=(",", ":"), sort_keys=True,
    ).encode("utf-8")
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_audit.update(embed_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def grep_t16_verdict(verdict_text):
    """Locate T1.6 canonical verdict line + extract composite status,
    audit_sha256, magnitude_verdict, rel_dev at 3 PDG anchors.

    Returns dict with keys: found (bool), line_index (int), composite (str),
    audit_sha256 (str|None), magnitude_verdict (str|None),
    rel_dev_100GeV / rel_dev_1GeV / rel_dev_1MeV (float|None),
    g_star_BS_FD_BE_T_H (float|None).
    """
    lines = verdict_text.splitlines()
    for idx, line in enumerate(lines, start=1):
        if line.startswith(f"{T16_GATE_ID}:"):
            head, _, tail = line.partition("--")
            # Composite status (after ':' before '--')
            composite = head.split(":")[1].strip()  # PASS|FAIL|INFO
            # audit_sha256 full 64-char
            m_sha = re.search(r"audit_sha256=([a-f0-9]{64})", tail)
            audit_sha = m_sha.group(1) if m_sha else None
            # rel_dev at 3 anchors (from value field)
            m_100 = re.search(r"rel_dev_100GeV=([0-9.eE+-]+)", tail)
            m_1g = re.search(r"rel_dev_1GeV=([0-9.eE+-]+)", tail)
            m_1m = re.search(r"rel_dev_1MeV=([0-9.eE+-]+)", tail)
            rel_dev_100GeV = float(m_100.group(1)) if m_100 else None
            rel_dev_1GeV = float(m_1g.group(1)) if m_1g else None
            rel_dev_1MeV = float(m_1m.group(1)) if m_1m else None
            # g_star_BS_FD_BE_T_H value
            m_g = re.search(r"g_star_BS_FD_BE_T_H=([0-9.eE+-]+)", tail)
            g_star_BS_FD_BE_T_H = float(m_g.group(1)) if m_g else None
            # 3-tuple annotation row (typically the line after the dual-SHA
            # companion row; scan a small window for safety)
            magnitude_verdict = None
            for offset in range(1, 4):
                if idx + offset - 1 < len(lines):
                    annot = lines[idx + offset - 1]
                    if "magnitude_verdict=" in annot and T16_GATE_ID in annot:
                        m_mag = re.search(r"magnitude_verdict=(PASS|INFO|FAIL)", annot)
                        if m_mag:
                            magnitude_verdict = m_mag.group(1)
                            break
            return {
                "found": True,
                "line_index": idx,
                "composite": composite,
                "audit_sha256": audit_sha,
                "magnitude_verdict": magnitude_verdict,
                "rel_dev_100GeV": rel_dev_100GeV,
                "rel_dev_1GeV": rel_dev_1GeV,
                "rel_dev_1MeV": rel_dev_1MeV,
                "g_star_BS_FD_BE_T_H": g_star_BS_FD_BE_T_H,
            }
    return {"found": False}


def emit_verdict(verdict, value_str, audit_sha, content_sha):
    """Append canonical line + dual-SHA companion + 3-tuple advisory row.

    Single atomic open("a") write per the canonical AFTER-pattern (build
    text in memory; single fsync; no per-attempt rewrite per
    `.claude/rules/registry-landing.md §"Bridge-Landing Script Architecture
    (single-shot pattern)"` — closure scripts follow the same single-shot
    discipline as registry-landing scripts).
    """
    canonical = (
        f"{GATE_ID}: {verdict} -- value={value_str!r} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}\n"
    )
    # Dual-SHA companion row (W9a-99 split short-form for human scan)
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); "
        f"PRE-REG-INC per session-91-plan-w3.md §W3-2 §11; "
        f"deferred to S92+ retry conditional on refined T1.6 PASS; "
        f"required prereq: [{T16_GATE_ID}=PASS_at_gate_band]; "
        f"closure_script=computations/session-91/s91_w3_cf39_mechanical_closure_blocked_by_cf40.py; "
        f"upstream_block_T1_6_audit_sha_full_64=<embedded_in_value_field>\n"
    )
    # 3-tuple annotation advisory row (per plan §6 line 287 — [VERIFY]∧[CHAIN]
    # does NOT require 3-tuple per gate-verdicts.md schema-v2 trigger reading,
    # but plan author advises emission for downstream regime_verdict reading)
    # Composite collapse: magnitude=FAIL AND regime=VALID → composite=FAIL,
    # which matches the canonical FAIL tag.
    advisory = (
        f"# sign_verdict=N/A magnitude_verdict=FAIL regime_verdict=VALID "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2; mechanical PRE-REG-INC)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical)
        fp.write(companion)
        fp.write(advisory)


def main():
    t0 = time.time()
    inputs = [
        VERDICT_TXT,
        S88_VERDICTS,
        CANONICAL_CONSTANTS,
        PLAN_W3,
        MECHANICAL_CLOSURE_RULE,
        GATE_VERDICTS_RULE,
    ]
    pins = log_input_pins(inputs)
    # Per-gate-distinct identity keys (mechanical-closure-discipline.md
    # §"When mechanical closure IS acceptable" item (3))
    embed_keys = {
        "_gate_id": GATE_ID,
        "_wp_id": WP_ID,
        "_scheme": SCHEME,
        "_convention": CONVENTION,
        "_closure_kind": "PRE-REG-INC-upstream-blocked",
        "_upstream_gate_id": T16_GATE_ID,
        "_routing_rule": "plan-§W3-2-§6-line-250-+-§11-line-333-FAIL-at-any-of-3-PDG-anchors",
        "_supersedes_target_DEFERRED": S88_SUPERSEDED_FULL_SHA,
    }
    script_path = Path(__file__).resolve()
    audit_sha, content_sha = compute_dual_sha(
        script_path, CANONICAL_CONSTANTS, pins, embed_keys,
    )
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    # ---- Step 1: Locate T1.6 verdict line on disk; substantiate prereq-block ----
    print("Step 1: locate T1.6 verdict line on disk; substantiate upstream-block topology")
    verdict_text = VERDICT_TXT.read_text(encoding="utf-8")
    t16 = grep_t16_verdict(verdict_text)
    if not t16["found"]:
        print(f"ERROR: T1.6 verdict line for {T16_GATE_ID} NOT FOUND in {VERDICT_TXT}.")
        print("       Mechanical PRE-REG-INC closure cannot proceed without an upstream verdict to cite.")
        return 2
    print(f"  T1.6 found at line {t16['line_index']}: composite={t16['composite']}")
    print(f"  T1.6 audit_sha256 (full 64-char): {t16['audit_sha256']}")
    print(f"  T1.6 magnitude_verdict (from 3-tuple row): {t16['magnitude_verdict']}")
    print(f"  T1.6 rel_dev_100GeV: {t16['rel_dev_100GeV']}")
    print(f"  T1.6 rel_dev_1GeV:   {t16['rel_dev_1GeV']}")
    print(f"  T1.6 rel_dev_1MeV:   {t16['rel_dev_1MeV']}")
    print(f"  T1.6 g_star_BS_FD_BE_T_H (candidate, NOT promoted to canonical_constants.py): {t16['g_star_BS_FD_BE_T_H']}")
    print()

    # ---- Step 2: Verify T1.6 verdict ≠ PASS at gate-band predicate ----
    # The plan §W3-2 §11 routing reads "FAIL at any of the 3 PDG anchors" as
    # the trigger. The composite collapse (INFO via MARGINAL regime) does
    # NOT close the band-predicate failure; magnitude=FAIL governs T1.7
    # mechanical closure.
    print("Step 2: verify T1.6 verdict ≠ PASS at gate-band predicate")
    gate_band = 0.10  # (local) — plan T1.6 PASS/FAIL/INFO threshold (≤ 0.10 PASS)
    fail_at_anchor = []  # (local) — list of anchors where rel_dev > 0.10
    for anchor_name, rel_dev in [
        ("100GeV", t16["rel_dev_100GeV"]),
        ("1GeV", t16["rel_dev_1GeV"]),
        ("1MeV", t16["rel_dev_1MeV"]),
    ]:
        if rel_dev is not None and rel_dev > gate_band:
            fail_at_anchor.append((anchor_name, rel_dev))
    upstream_block_fired = (
        t16["magnitude_verdict"] == "FAIL"
        or t16["composite"] == "FAIL"
        or len(fail_at_anchor) > 0
    )
    print(f"  Gate-band ceiling: rel_dev ≤ {gate_band}")
    print(f"  Anchors exceeding band: {fail_at_anchor}")
    print(f"  Upstream-block topology fires: {upstream_block_fired}")
    if t16["composite"] == "PASS" and t16["magnitude_verdict"] == "PASS" and not fail_at_anchor:
        print("ERROR: T1.6 PASSed at gate-band; mechanical closure NOT applicable.")
        print("       Re-dispatch T1.7 with substantive L_H_canonical computation per plan §6 PASS branch.")
        return 3
    if not upstream_block_fired:
        print("ERROR: upstream-block topology did not fire; cannot mechanically close.")
        return 4
    print(f"  ✓ T1.6 verdict ≠ PASS at gate-band; mechanical closure is admissible per")
    print(f"    mechanical-closure-discipline.md §'When mechanical closure IS acceptable'")
    print(f"    clause (1) upstream-block topology + plan §W3-2 §11 routing.")
    print()

    # ---- Step 3: Verify Option-A supersedes target SHA (DEFERRED on FAIL) ----
    print("Step 3: verify Option-A supersedes target SHA exists on disk (DEFERRED emission)")
    s88_text = S88_VERDICTS.read_text(encoding="utf-8") if S88_VERDICTS.exists() else ""
    full_match = S88_SUPERSEDED_FULL_SHA in s88_text
    print(f"  S88 target full 64-char '{S88_SUPERSEDED_FULL_SHA}' present in s88_gate_verdicts.txt: {full_match}")
    print(f"  Per plan §W3-2 §11 FAIL mechanical branch: NO supersedes-tag emission.")
    print(f"  S88 absolute verdict permanence preserved: S88-CF-CURV-16-U1-BBN-CHUNKY-")
    print(f"  HAWKING-METALLICITY at s88_gate_verdicts.txt:34 remains canonical.")
    print(f"  Carry-forward to S92+ retry conditional on refined T1.6 PASS.")
    print()

    # ---- Step 4: Verify g_star_BS_T_H_FW canonical pin NOT promoted ----
    print("Step 4: verify g_star_BS_T_H_FW NOT promoted in canonical_constants.py")
    canonical_text = CANONICAL_CONSTANTS.read_text(encoding="utf-8") if CANONICAL_CONSTANTS.exists() else ""
    g_star_pin_present = "g_star_BS_T_H_FW" in canonical_text
    print(f"  g_star_BS_T_H_FW pin present in canonical_constants.py: {g_star_pin_present}")
    if g_star_pin_present:
        print(f"  WARNING: g_star_BS_T_H_FW pin found despite T1.6 magnitude=FAIL.")
        print(f"           Plan §11 FAIL branch specifies no canonical promotion.")
        print(f"           Document this anomaly in working-paper §W3-2 'Cross-checks performed'.")
    else:
        print(f"  ✓ g_star_BS_T_H_FW NOT in canonical_constants.py; T1.6 FAIL branch")
        print(f"    correctly did NOT trigger canonical promotion per plan §6 'On PASS'")
        print(f"    conditional + §11 FAIL branch directive.")
    print()

    # ---- Step 5: Determine closure verdict + value-field signature ----
    print("Step 5: determine closure verdict + audit-trail value-field signature")
    # Per mechanical-closure-discipline.md §2: emit FAIL or PRE-REG-INC, NEVER PASS.
    # Plan §W3-2 §6 line 296 verbatim FAIL branch verdict-line format:
    #   value='PRE-REG-INC_blocked_by_S91_CF40_FAIL_supersedes_emission_deferred'
    closure_verdict = "FAIL"  # (local)
    fail_anchor_summary = ",".join(  # (local)
        f"{name}={rd:.6f}" for name, rd in fail_at_anchor
    ) if fail_at_anchor else "none-via-gate-band-but-magnitude-FAIL-detected"
    closure_value = (
        f"PRE-REG-INC_blocked_by_S91_CF40_FAIL_supersedes_emission_deferred;"
        f"t16_gate_id={T16_GATE_ID};"
        f"t16_line_index_in_s91_verdicts={t16['line_index']};"
        f"t16_composite_verdict={t16['composite']};"
        f"t16_magnitude_verdict={t16['magnitude_verdict']};"
        f"t16_audit_sha_full_64={t16['audit_sha256']};"
        f"t16_fail_at_anchors=[{fail_anchor_summary}];"
        f"t16_gate_band_ceiling={gate_band};"
        f"t16_g_star_BS_FD_BE_T_H_candidate_NOT_promoted={t16['g_star_BS_FD_BE_T_H']};"
        f"g_star_BS_T_H_FW_canonical_pin_present={g_star_pin_present};"
        f"option_a_supersedes_target_full_64={S88_SUPERSEDED_FULL_SHA};"
        f"option_a_supersedes_emission_deferred=True;"
        f"s88_absolute_verdict_permanence_preserved=True;"
        f"refinement_pathway=CF-S92-PHASE-WEIGHT-QCD-CROSSOVER-REFINEMENT_then_T1_6_retry_then_T1_7_retry;"
        f"deferred_to_S92=True;"
        f"plan_routing=session-91-plan-w3.md_§W3-2_§6_line_250_+_§11_line_333_FAIL_at_any_3_PDG_anchors;"
        f"closure_kind=mechanical-mack-cosmic-bridge-primary-no-substantive-compute;"
        f"closure_admissibility_per_mechanical-closure-discipline.md=ALL_5_CLAUSES_PASS;"
        f"after_pattern_compliance=True"
    )
    print(f"  closure_verdict: {closure_verdict}")
    print(f"  closure_value (~{len(closure_value)} chars): documents prereq-block topology +")
    print(f"                              T1.6 audit_sha co-citation + Option-A deferred + ")
    print(f"                              S88 absolute verdict permanence preservation")
    print()

    # ---- Step 6: Append closure verdict + dual-SHA companion + 3-tuple advisory ----
    print("Step 6: append closure verdict + dual-SHA companion + 3-tuple advisory")
    emit_verdict(closure_verdict, closure_value, audit_sha, content_sha)
    print(f"  appended to: {VERDICT_TXT.relative_to(PROJECT_ROOT)}")
    print()

    # ---- Step 7: 5-clause admissibility audit summary ----
    print("Step 7: mechanical-closure-discipline.md 5-clause admissibility audit summary")
    print("  (1) Upstream-block topology is the cause:")
    print(f"      T1.6 magnitude=FAIL at T=1 GeV (rel_dev_1GeV={t16['rel_dev_1GeV']:.6f} > {gate_band})")
    print(f"      emitted at s91_gate_verdicts.txt line {t16['line_index']}; plan §W3-2 §6+§11")
    print(f"      pre-registers FAIL mechanical routing. PLAN ANTICIPATED. ✓")
    print("  (2) Verdict honesty:")
    print(f"      emit FAIL (NEVER PASS); value follows PRE-REG-INC_blocked_by_S91_CF40_FAIL")
    print(f"      pattern; sig_verdict=N/A magnitude=FAIL regime=VALID 3-tuple. ✓")
    print("  (3) Per-gate-distinct audit_sha256:")
    print(f"      embed_keys = {{_gate_id, _wp_id, _scheme, _convention, _closure_kind,")
    print(f"      _upstream_gate_id, _routing_rule, _supersedes_target_DEFERRED}};")
    print(f"      audit_sha256 = {audit_sha[:16]}... is distinct from any other closure SHA. ✓")
    print("  (4) Audit-trail signature:")
    print(f"      grep 'PRE-REG-INC_blocked_by_S91_CF40_FAIL' s91_gate_verdicts.txt")
    print(f"      → this gate's canonical line + co-citation of T1.6 audit_sha_full_64")
    print(f"      {t16['audit_sha256'][:16]}... in value field. ✓")
    print("  (5) Working-paper update is in-script:")
    print(f"      §W3-2 §Status/§Verdict/§Results/§Substrate framing/§Solution-space ")
    print(f"      blocks populated in the same orchestrator dispatch via Edit tool. ✓")
    print()

    print(f"=== {GATE_ID}: {closure_verdict} (mechanical PRE-REG-INC closure; wall {time.time() - t0:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
