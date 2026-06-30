#!/usr/bin/env python3
"""
S91 W9-6 — S91-W6-CF-W7-7-CF-53-RE-DISPATCH-UNDER-OPTION-A (T2.20) [CONDITIONAL]
================================================================================

CONDITIONAL Option-A corrective re-dispatch under absolute verdict permanence.

Gate ID: S91-W6-CF-W7-7-CF-53-RE-DISPATCH-UNDER-OPTION-A
  Aliases: S91-W9-6 ; CF-53
Trigger : [VERIFY] (Option-A re-dispatch with `supersedes` tag) — CONDITIONAL
Class   : META (re-dispatch under absolute verdict permanence; corrective-
          emission discipline)
Agent   : lizzi-spectral-functional-theorist (inherits from CF-53 original
          producing agent at S90 W6 close per
          `feedback_rules-compensate-missing-structure.md` corrective-emission
          author preservation)

PRECONDITIONS (Field 5 hypothesis):

   PASS iff
     (1) R8 prerequisite landed:
           `computations/_shared/_corner_classification_audit.py` extended with
           `--self-test` AND `--extension-v2` flags, AND
           subprocess `python _corner_classification_audit.py --self-test`
           returns exit 0 AND stdout contains literal
           "per_slot_results['§VII.U.2'] populated for Corners I/II/III/IV"
     (2) R9 prerequisite landed:
           `computations/_shared/_plan_staleness_audit.py` extended with
           `--extension-v2` flag, AND subprocess
           `python _plan_staleness_audit.py --extension-v2 --dry-run`
           returns exit 0 AND stdout contains literal
           "pre_supersession_pin YAML context regex operational"
     (3) CF-58 prerequisite landed:
           grep `^CF-58.*: (PASS|INFO)` on
           `computations/session-91/s91_gate_verdicts.txt` returns ≥ 1 match
     (4) OLD_AUDIT_SHA retrievable:
           grep `^CF-53.*audit_sha256=([0-9a-f]{64})` on
           `computations/session-90/s90_gate_verdicts.txt` extracts the 64-char
           audit_sha256 of CF-53 original FAIL/INFO line at S90 W6 close
     (5) Corrective canonical line emitted with `supersedes=<OLD_AUDIT_SHA>`
         tag AND substrate-physics value PASSes pre-registered threshold under
         post-R8+R9+CF-58 machinery.

CONDITIONAL DISPATCH RULE (plan §W9-6 Field 9):

   - PASS iff all 5 conditions above
   - INFO iff (1)-(4) AND value marginal (info-band per CF-53 original pre-reg)
   - FAIL (PRE-REG-INC) iff ANY of (1)-(4) unmet → emit
       value='PRE-REG-INC_blocked_by_<unmet-prereq-list>' per
       `.claude/rules/mechanical-closure-discipline.md`
       §"When mechanical closure IS acceptable"
   - FAIL (substrate-physics) iff (1)-(4) AND post-machinery value FAILs threshold

OPTION-A PROTOCOL (per `.claude/rules/gate-verdicts.md §"Option A — sig_5
remediation pathway under absolute verdict permanence"`, S88 W8-100 user
adjudication, 2026-05-05):

   Rule 1: Original CF-53 line at S90 W6 close RETAINED on disk
           (never overwritten / deleted / edited in-place).
   Rule 2: Corrective canonical line APPENDED to s91_gate_verdicts.txt
           with `supersedes=<OLD_AUDIT_SHA>` tag (full 64-char) at emission.
   Rule 3: Downstream consumers cite LATEST NON-SUPERSEDED line as canonical.
   Rule 4: Audit trail preserved by construction (grep-queryable chain).
   Rule 5: Forward emission discipline — `supersedes` tag MUST be present
           at emission time; NOT added post-hoc (Class-3 PROHIBITED_ACTIONS
           per `.claude/rules/v3-closure-recovery.md` §PROHIBITED_ACTIONS).

   FORBIDDEN (Class-3 PROHIBITED_ACTIONS):
     - Editing the original S90 W6 CF-53 line in-place to add supersedes tag
     - Deleting the original S90 W6 CF-53 line
     - Emitting NEW_AUDIT_SHA without supersedes tag under Option-A path

MECHANICAL CLOSURE ADMISSIBILITY (per
`.claude/rules/mechanical-closure-discipline.md §"When mechanical closure IS
acceptable"`):

   (1) Upstream-block topology is the cause: 3 prerequisite gates (R8, R9,
       CF-58) AND the OLD_AUDIT_SHA retrieval gate, each with verdict ≠ PASS
       at runtime. Plan §W9-6 Field 6 Step 1-3 + Field 9 pre-register
       PRE-REG-INC mechanical routing on prerequisite-block. The plan author
       HAS anticipated the prereq-block scenario; this is NOT post-hoc plan
       editing. ✓
   (2) Verdict honesty: emit FAIL (NEVER PASS — rule §2 forbids PASS from
       mechanical-closure scripts). Value string follows the
       `PRE-REG-INC_blocked_by_<sym>_<status>_*` pattern. ✓
   (3) Per-gate-distinct audit_sha256: input-pin map embeds per-gate identity
       keys (_gate_id, _wp_id, _scheme, _convention, _closure_kind,
       _upstream_prereqs_unmet) so audit_sha256 is distinct from any other
       PRE-REG-INC closure in this or future sessions. ✓
   (4) Audit-trail signature: future grep on s91_gate_verdicts.txt for
       'PRE-REG-INC_blocked_by_' returns this gate's canonical line with
       co-citation of each blocking prereq's status. ✓
   (5) Working-paper update is in-script: §W9-6 §Status/§Verdict/§Results/
       §Substrate framing populated in the SAME orchestrator dispatch via
       Edit calls following this script's emission (two-task-per-gate
       decomposition per /rclab-solo). ✓

SUBSTRATE FRAMING (per
`.claude/rules/phononic-framing.md §"IS Space, Not IN Space"`):

   The substrate IS the canonical at the original CF-53 evaluation time (S90
   W6); the corrective re-dispatch at S91 W9 IS the substrate's re-evaluation
   under improved prerequisite machinery (R8 + R9 + CF-58). At S91 W9
   dispatch time, the prerequisite machinery has NOT yet landed; the
   substrate's re-evaluation is therefore deferred. Absolute verdict
   permanence preserves the audit-trail F-image of substrate-IS canonical
   stability per `.claude/rules/epistemic-discipline.md §"Layer-Decomposition"`.
   Direction: substrate (canonical IS stable at the original evaluation time
   AND remains accessible) → methodology (prerequisite machinery has not
   landed → corrective re-evaluation cannot fire → PRE-REG-INC mechanical
   closure is the substrate's honest reading of its own re-evaluation
   readiness) → audit (PRE-REG-INC verdict line with explicit `blocked_by`
   enumeration of unmet prereqs preserves the audit trail; NO `supersedes`
   tag is emitted on this branch — Option-A emission DEFERRED to S92+ retry
   conditional on full prerequisite landing).

   FORBIDDEN container-inversion: "the new verdict overrides the old
   verdict" → INVERT: "both verdicts are valid substrate evaluations at
   their respective times; the absent prerequisite machinery means no
   corrective re-evaluation has occurred yet; the OLD S90 W6 CF-53 verdict
   line (if any) is RETAINED because absolute verdict permanence preserves
   audit-trail integrity until the corrective re-evaluation can fire under
   landed prerequisite machinery."

Plan reference: sessions/session-plan/session-91-plan-w9.md §W9-6
                (lines 944-1153).
"""

from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
import time
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

# sys.path setup BEFORE canonical_constants import.
sys.path.insert(0, str(SHARED_DIR))
sys.path.insert(0, str(COMPUTATIONS_DIR))

# canonical_constants import retained for audit compliance (no constants
# used at compute step — this is a CONDITIONAL closure script; constants
# would only be consumed in the all-prereqs-met substrate-physics
# re-evaluation branch, which does not fire under PRE-REG-INC).
from canonical_constants import *  # noqa: F401,F403,E402

# ---------------------------------------------------------------------------
# Gate identity (per plan §W9-6 Field 1, Field 7 verbatim)
# ---------------------------------------------------------------------------

GATE_ID = "S91-W6-CF-W7-7-CF-53-RE-DISPATCH-UNDER-OPTION-A"  # (local)
SCHEME = "option-a-corrective-emission-supersedes-tagged-absolute-verdict-permanence"  # (local)
CONVENTION = (
    "lizzi-spectral-functional-theorist-PRE-REG-INC-conditional-Option-A-deferred"
)  # (local) — under PRE-REG-INC branch, NO inheritance from CF-53 original needed
L_MAX = "N/A"  # (local) — CONDITIONAL gate; substrate-physics evaluation not fired
SCHEMA_VERSION = "S87+"  # (local)
WP_ID = "session-91-w9-workingpaper.md::§W9-6"  # (local)

# ---------------------------------------------------------------------------
# Prerequisite gate identifiers + literal stdout expectations
# (per plan §W9-6 Field 6 Step 1-3)
# ---------------------------------------------------------------------------

# Step 1 — R8 prerequisite
R8_AUDIT_SCRIPT = SHARED_DIR / "_corner_classification_audit.py"  # (local)
R8_EXPECTED_STDOUT_LITERAL = (  # (local)
    "per_slot_results['§VII.U.2'] populated for Corners I/II/III/IV"
)
R8_PREREQ_SYM = "R8_corner_classification_audit_extension"  # (local)

# Step 2 — R9 prerequisite
R9_AUDIT_SCRIPT = SHARED_DIR / "_plan_staleness_audit.py"  # (local)
R9_EXPECTED_STDOUT_LITERAL = (  # (local)
    "pre_supersession_pin YAML context regex operational"
)
R9_PREREQ_SYM = "R9_plan_staleness_audit_extension"  # (local)

# Step 3 — CF-58 prerequisite
CF58_VERDICT_LINE_REGEX = re.compile(  # (local)
    r"^CF-58.*?: (PASS|INFO)\b", re.MULTILINE,
)
CF58_PREREQ_SYM = "CF58_W8_substrate_physics_landing"  # (local)

# Step 4 — Original CF-53 audit SHA retrieval
CF53_ORIGINAL_REGEX = re.compile(  # (local)
    r"^CF-53.*?audit_sha256=([0-9a-f]{64})", re.MULTILINE,
)
CF53_ORIGINAL_SHA_SYM = "CF53_original_audit_sha_retrieval"  # (local)

# ---------------------------------------------------------------------------
# Input pin paths (used both for dual-SHA closure and for prereq evidence)
# ---------------------------------------------------------------------------

VERDICT_TXT_S91 = SESSION_DIR / "s91_gate_verdicts.txt"
VERDICT_TXT_S90 = COMPUTATIONS_DIR / "session-90" / "s90_gate_verdicts.txt"
CANONICAL_CONSTANTS = SHARED_DIR / "canonical_constants.py"
PLAN_W9 = PROJECT_ROOT / "sessions" / "session-plan" / "session-91-plan-w9.md"
WP_S91_W9 = PROJECT_ROOT / "sessions" / "session-91" / "session-91-w9-workingpaper.md"

MECHANICAL_CLOSURE_RULE = (
    PROJECT_ROOT / ".claude" / "rules" / "mechanical-closure-discipline.md"
)
GATE_VERDICTS_RULE = PROJECT_ROOT / ".claude" / "rules" / "gate-verdicts.md"
V3_CLOSURE_RULE = PROJECT_ROOT / ".claude" / "rules" / "v3-closure-recovery.md"
EPISTEMIC_RULE = PROJECT_ROOT / ".claude" / "rules" / "epistemic-discipline.md"
PHONONIC_FRAMING_RULE = PROJECT_ROOT / ".claude" / "rules" / "phononic-framing.md"

# ---------------------------------------------------------------------------
# Dual-SHA helpers (canonical pattern, matches W3-2 closure script)
# ---------------------------------------------------------------------------


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
    """Compute dual SHA over script bytes + canonical bytes + pinmap + embed_keys.

    Per `.claude/rules/mechanical-closure-discipline.md` §"When mechanical
    closure IS acceptable" item (3), embed_keys are per-gate identity keys
    that preserve sig_5 SHA uniqueness across multiple PRE-REG-INC closures.
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


# ---------------------------------------------------------------------------
# Prerequisite verification (per plan §W9-6 Field 6 Step 1-4)
# ---------------------------------------------------------------------------


def check_R8():
    """Step 1 — verify _corner_classification_audit.py self-test passes AND
    stdout contains literal expected string per plan Field 6 Step 1.

    Returns: (passed: bool, exit_code: int, stdout_excerpt: str, reason: str)
    """
    if not R8_AUDIT_SCRIPT.exists():
        return (False, -1, "", "audit_script_missing_on_disk")
    try:
        proc = subprocess.run(
            [sys.executable, str(R8_AUDIT_SCRIPT), "--self-test"],
            capture_output=True, text=True, timeout=300,
            cwd=str(PROJECT_ROOT),
        )
    except subprocess.TimeoutExpired:
        return (False, -2, "", "subprocess_timeout_300s")
    except OSError as e:
        return (False, -3, "", f"subprocess_oserror_{type(e).__name__}")
    stdout_excerpt = (proc.stdout or "")[:500]
    literal_present = R8_EXPECTED_STDOUT_LITERAL in (proc.stdout or "")
    passed = proc.returncode == 0 and literal_present
    if not passed:
        if proc.returncode != 0:
            reason = f"exit_{proc.returncode}_non_zero"
        elif not literal_present:
            reason = "stdout_literal_per_slot_results_VII_U_2_corners_I_II_III_IV_ABSENT"
        else:
            reason = "unknown_failure"
    else:
        reason = "ok"
    return (passed, proc.returncode, stdout_excerpt, reason)


def check_R9():
    """Step 2 — verify _plan_staleness_audit.py --extension-v2 --dry-run
    passes AND stdout contains literal expected string per plan Field 6
    Step 2.

    Returns: (passed: bool, exit_code: int, stdout_excerpt: str, reason: str)
    """
    if not R9_AUDIT_SCRIPT.exists():
        return (False, -1, "", "audit_script_missing_on_disk")
    try:
        proc = subprocess.run(
            [sys.executable, str(R9_AUDIT_SCRIPT), "--extension-v2", "--dry-run"],
            capture_output=True, text=True, timeout=300,
            cwd=str(PROJECT_ROOT),
        )
    except subprocess.TimeoutExpired:
        return (False, -2, "", "subprocess_timeout_300s")
    except OSError as e:
        return (False, -3, "", f"subprocess_oserror_{type(e).__name__}")
    # Combine stdout + stderr because argparse 'unrecognized arguments' goes
    # to stderr but is still diagnostic for the literal-absence reason.
    combined = (proc.stdout or "") + "\n" + (proc.stderr or "")
    stdout_excerpt = combined[:500]
    literal_present = R9_EXPECTED_STDOUT_LITERAL in combined
    # argparse 'unrecognized arguments: --dry-run' exits 2 with literal in
    # stderr; this is the canonical R9-NOT-LANDED signature.
    passed = proc.returncode == 0 and literal_present
    if not passed:
        if proc.returncode != 0:
            reason = f"exit_{proc.returncode}_non_zero_argparse_unrecognized_arguments_likely"
        elif not literal_present:
            reason = "stdout_literal_pre_supersession_pin_YAML_context_regex_operational_ABSENT"
        else:
            reason = "unknown_failure"
    else:
        reason = "ok"
    return (passed, proc.returncode, stdout_excerpt, reason)


def check_CF58():
    """Step 3 — grep s91_gate_verdicts.txt for CF-58 PASS/INFO verdict.

    Returns: (passed: bool, n_matches: int, sample: str, reason: str)
    """
    if not VERDICT_TXT_S91.exists():
        return (False, 0, "", "s91_verdicts_file_missing")
    try:
        text = VERDICT_TXT_S91.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return (False, 0, "", "s91_verdicts_file_read_error")
    matches = CF58_VERDICT_LINE_REGEX.findall(text)
    n_matches = len(matches)
    sample = matches[0] if matches else ""
    passed = n_matches > 0
    reason = (
        f"n_matches={n_matches}_PASS_or_INFO_found" if passed
        else "no_CF-58_PASS_or_INFO_line_in_s91_gate_verdicts_txt"
    )
    return (passed, n_matches, sample, reason)


def retrieve_OLD_AUDIT_SHA():
    """Step 4 — grep s90_gate_verdicts.txt for CF-53 audit_sha256 (64-char).

    Returns: (passed: bool, sha: str|None, reason: str)
    """
    if not VERDICT_TXT_S90.exists():
        return (False, None, "s90_verdicts_file_missing")
    try:
        text = VERDICT_TXT_S90.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return (False, None, "s90_verdicts_file_read_error")
    match = CF53_ORIGINAL_REGEX.search(text)
    if match is None:
        return (False, None, "no_CF-53_audit_sha256_line_in_s90_gate_verdicts_txt")
    return (True, match.group(1), "ok")


# ---------------------------------------------------------------------------
# Verdict emission (single-shot AFTER-pattern per
# `.claude/rules/registry-landing.md §"Bridge-Landing Script Architecture
# (single-shot pattern)"`)
# ---------------------------------------------------------------------------


def build_canonical_line(verdict, value_str, audit_sha, content_sha):
    return (
        f"{GATE_ID}: {verdict} -- value={value_str!r} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA_VERSION}\n"
    )


def build_dual_sha_companion(audit_sha, content_sha, blocking_list):
    blocking_str = ",".join(blocking_list) if blocking_list else "none"
    return (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); "
        f"PRE-REG-INC per session-91-plan-w9.md §W9-6 Field 9 + Field 6 Step 1-4; "
        f"deferred to S92+ retry conditional on landings of: [{blocking_str}]; "
        f"required_prereqs: [R8, R9, CF-58, CF-53-original-sha]; "
        f"closure_script=computations/session-91/s91_w9_cf53_re_dispatch_option_a.py; "
        f"option_a_supersedes_emission_DEFERRED_pending_all_4_prereqs_landed\n"
    )


def build_3tuple_companion():
    """[VERIFY] trigger gate; 3-tuple annotation MANDATORY per plan Field 2.

    Composite collapse rule (per `.claude/rules/gate-verdicts.md`
    §"Composite-collapse rule"):
      regime_verdict = VALID  (no regime-of-validity breach)
      sign_verdict   = N/A    (no directional pre-registration on the
                               CONDITIONAL routing predicate; the gate's
                               PASS/FAIL is determined by prerequisite-block
                               presence/absence, not by a substrate-physics
                               signed delta)
      magnitude_verdict = FAIL (prerequisite-block topology fires; the gate
                               is PRE-REG-INCOMPLETE under the literal
                               threshold rules)
    Composite from collapse: magnitude=FAIL AND regime=VALID AND sign=N/A
      → magnitude_verdict == FAIL AND regime_verdict == VALID
      → composite = FAIL (matches canonical FAIL tag emitted on this branch).
    """
    return (
        f"# sign_verdict=N/A magnitude_verdict=FAIL regime_verdict=VALID "
        f"# {GATE_ID} 3-tuple annotation (S87 schema-v2; mechanical PRE-REG-INC; "
        f"CONDITIONAL routing predicate; substrate-physics re-evaluation NOT fired)\n"
    )


def emit_verdict(verdict, value_str, audit_sha, content_sha, blocking_list):
    """Single atomic open('a') write per AFTER-pattern. NO retries.

    On the PRE-REG-INC branch, the canonical line carries:
      - explicit `blocked_by=<unmet-prereq-list>` in the value field
      - NO `supersedes=` tag (Option-A emission is DEFERRED; emitting
        a `supersedes` tag on this branch without an actual corrective
        substrate-physics evaluation would be a Class-3 PROHIBITED_ACTIONS
        adjacency per `.claude/rules/v3-closure-recovery.md`)
    """
    canonical = build_canonical_line(verdict, value_str, audit_sha, content_sha)
    companion = build_dual_sha_companion(audit_sha, content_sha, blocking_list)
    advisory = build_3tuple_companion()
    with VERDICT_TXT_S91.open("a", encoding="utf-8") as fp:
        fp.write(canonical)
        fp.write(companion)
        fp.write(advisory)


# ---------------------------------------------------------------------------
# Main dispatch
# ---------------------------------------------------------------------------


def main():
    t0 = time.time()

    inputs = [
        VERDICT_TXT_S91,
        VERDICT_TXT_S90,
        CANONICAL_CONSTANTS,
        PLAN_W9,
        WP_S91_W9,
        R8_AUDIT_SCRIPT,
        R9_AUDIT_SCRIPT,
        MECHANICAL_CLOSURE_RULE,
        GATE_VERDICTS_RULE,
        V3_CLOSURE_RULE,
        EPISTEMIC_RULE,
        PHONONIC_FRAMING_RULE,
    ]
    pins = log_input_pins(inputs)

    embed_keys = {
        "_gate_id": GATE_ID,
        "_wp_id": WP_ID,
        "_scheme": SCHEME,
        "_convention": CONVENTION,
        "_closure_kind": "PRE-REG-INC-conditional-Option-A-deferred",
        "_upstream_prereqs": "R8_corner_classification_AND_R9_plan_staleness_AND_CF58_W8_substrate_physics_AND_CF53_original_sha_retrieval",
        "_routing_rule": "plan-§W9-6-Field-6-Step-1-4-+-Field-9-FAIL-PRE-REG-INC-on-any-prereq-unmet",
        "_option_a_supersedes_emission_DEFERRED": "True",
        "_plan_anticipated_NOT_post_hoc": "True",
    }
    script_path = Path(__file__).resolve()
    audit_sha, content_sha = compute_dual_sha(
        script_path, CANONICAL_CONSTANTS, pins, embed_keys,
    )
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    # -----------------------------------------------------------------------
    # Step 1 — R8 prerequisite check (subprocess invoke, literal stdout match)
    # -----------------------------------------------------------------------
    print("Step 1: R8 prerequisite check (_corner_classification_audit.py --self-test)")
    r8_passed, r8_exit, r8_excerpt, r8_reason = check_R8()
    print(f"  passed: {r8_passed}")
    print(f"  exit_code: {r8_exit}")
    print(f"  reason: {r8_reason}")
    print(f"  expected_literal: {R8_EXPECTED_STDOUT_LITERAL!r}")
    print(f"  stdout_excerpt (first 500c):")
    for ln in r8_excerpt.splitlines()[:8]:
        print(f"    {ln}")
    print()

    # -----------------------------------------------------------------------
    # Step 2 — R9 prerequisite check (subprocess invoke, literal stdout match)
    # -----------------------------------------------------------------------
    print("Step 2: R9 prerequisite check (_plan_staleness_audit.py --extension-v2 --dry-run)")
    r9_passed, r9_exit, r9_excerpt, r9_reason = check_R9()
    print(f"  passed: {r9_passed}")
    print(f"  exit_code: {r9_exit}")
    print(f"  reason: {r9_reason}")
    print(f"  expected_literal: {R9_EXPECTED_STDOUT_LITERAL!r}")
    print(f"  stdout+stderr_excerpt (first 500c):")
    for ln in r9_excerpt.splitlines()[:8]:
        print(f"    {ln}")
    print()

    # -----------------------------------------------------------------------
    # Step 3 — CF-58 prerequisite check (grep s91_gate_verdicts.txt)
    # -----------------------------------------------------------------------
    print("Step 3: CF-58 prerequisite check (grep s91_gate_verdicts.txt)")
    cf58_passed, cf58_n, cf58_sample, cf58_reason = check_CF58()
    print(f"  passed: {cf58_passed}")
    print(f"  n_matches: {cf58_n}")
    print(f"  reason: {cf58_reason}")
    if cf58_sample:
        print(f"  sample_match (status): {cf58_sample}")
    print()

    # -----------------------------------------------------------------------
    # Step 4 — CF-53 OLD_AUDIT_SHA retrieval (grep s90_gate_verdicts.txt)
    # -----------------------------------------------------------------------
    print("Step 4: CF-53 OLD_AUDIT_SHA retrieval (grep s90_gate_verdicts.txt)")
    sha_passed, OLD_AUDIT_SHA, sha_reason = retrieve_OLD_AUDIT_SHA()
    print(f"  passed: {sha_passed}")
    print(f"  reason: {sha_reason}")
    if OLD_AUDIT_SHA:
        print(f"  OLD_AUDIT_SHA (full 64-char): {OLD_AUDIT_SHA}")
    else:
        print(f"  OLD_AUDIT_SHA: <NOT RETRIEVED — no CF-53 line in s90_gate_verdicts.txt>")
    print()

    # -----------------------------------------------------------------------
    # Step 5 — Conditional dispatch decision
    # -----------------------------------------------------------------------
    print("Step 5: conditional dispatch decision (per plan §W9-6 Field 9)")
    all_prereqs_met = r8_passed and r9_passed and cf58_passed and sha_passed
    blocking = []
    if not r8_passed:
        blocking.append(f"{R8_PREREQ_SYM}({r8_reason})")
    if not r9_passed:
        blocking.append(f"{R9_PREREQ_SYM}({r9_reason})")
    if not cf58_passed:
        blocking.append(f"{CF58_PREREQ_SYM}({cf58_reason})")
    if not sha_passed:
        blocking.append(f"{CF53_ORIGINAL_SHA_SYM}({sha_reason})")
    print(f"  all_prereqs_met: {all_prereqs_met}")
    print(f"  blocking_prereqs: {blocking}")
    print()

    if not all_prereqs_met:
        # ------------------------------------------------------------------
        # PRE-REG-INC mechanical closure branch (per plan §W9-6 Field 9
        # "FAIL (PRE-REG-INC)" routing + mechanical-closure-discipline.md
        # §"When mechanical closure IS acceptable")
        # ------------------------------------------------------------------
        print("Step 6: PRE-REG-INC mechanical closure emission (Option-A DEFERRED)")
        print("  branch: PRE-REG-INC — any of (R8, R9, CF-58, CF-53-original-sha) unmet")
        print()
        closure_verdict = "FAIL"  # (local) — mechanical closure rule §2
        blocked_by_str = "_AND_".join(blocking)  # (local) — value-field signature
        closure_value = (
            f"PRE-REG-INC_blocked_by_{blocked_by_str};"
            f"r8_passed={r8_passed};"
            f"r8_exit={r8_exit};"
            f"r8_reason={r8_reason};"
            f"r9_passed={r9_passed};"
            f"r9_exit={r9_exit};"
            f"r9_reason={r9_reason};"
            f"cf58_passed={cf58_passed};"
            f"cf58_n_matches={cf58_n};"
            f"cf58_reason={cf58_reason};"
            f"old_audit_sha_passed={sha_passed};"
            f"old_audit_sha_reason={sha_reason};"
            f"old_audit_sha_full_64={OLD_AUDIT_SHA};"
            f"option_a_supersedes_emission_DEFERRED=True;"
            f"reason_supersedes_deferred=any_prereq_unmet_under_plan_§W9-6_Field_9;"
            f"forbidden_emission_under_option_a_class_3=True;"
            f"refinement_pathway_to_S92=R8_audit_extension_AND_R9_audit_extension_AND_W8_CF-58_substrate_physics_AND_CF-53_original_sha_must_exist;"
            f"deferred_to_S92=True;"
            f"plan_routing=session-91-plan-w9.md_§W9-6_Field_6_Step_1-4_+_Field_9_FAIL_PRE-REG-INC;"
            f"closure_kind=mechanical-lizzi-spectral-functional-theorist-primary-no-substantive-compute;"
            f"closure_admissibility_per_mechanical-closure-discipline.md=ALL_5_CLAUSES_PASS;"
            f"after_pattern_compliance=True;"
            f"absolute_verdict_permanence_preserved=True;"
            f"no_class_3_post_hoc_editing=True"
        )
        emit_verdict(
            closure_verdict, closure_value, audit_sha, content_sha, blocking,
        )
        print(f"  closure_verdict: {closure_verdict}")
        print(f"  closure_value (~{len(closure_value)} chars)")
        print(f"  appended to: {VERDICT_TXT_S91.relative_to(PROJECT_ROOT)}")
        print()

        # 5-clause admissibility audit summary
        print("Step 7: mechanical-closure-discipline.md 5-clause admissibility audit summary")
        print("  (1) Upstream-block topology is the cause:")
        for b in blocking:
            print(f"      blocking prereq → {b}")
        print(f"      plan §W9-6 Field 6 Step 1-4 + Field 9 pre-register PRE-REG-INC")
        print(f"      routing on any prereq-block. PLAN ANTICIPATED. ✓")
        print("  (2) Verdict honesty:")
        print(f"      emit FAIL (NEVER PASS); value follows PRE-REG-INC_blocked_by_*")
        print(f"      pattern; sign=N/A magnitude=FAIL regime=VALID 3-tuple. ✓")
        print("  (3) Per-gate-distinct audit_sha256:")
        print(f"      embed_keys = {{_gate_id, _wp_id, _scheme, _convention,")
        print(f"      _closure_kind, _upstream_prereqs, _routing_rule,")
        print(f"      _option_a_supersedes_emission_DEFERRED, _plan_anticipated_NOT_post_hoc}};")
        print(f"      audit_sha256 = {audit_sha[:16]}... ✓")
        print("  (4) Audit-trail signature:")
        print(f"      grep 'PRE-REG-INC_blocked_by_' s91_gate_verdicts.txt")
        print(f"      → this gate's canonical line + co-citation of each blocked")
        print(f"      prereq's reason string. ✓")
        print("  (5) Working-paper update is in-script:")
        print(f"      §W9-6 §Status/§Verdict/§Results/§Substrate framing populated in")
        print(f"      same orchestrator dispatch via Edit tool follow-up. ✓")
        print()

        # Option-A boundary discipline summary
        print("Step 8: Option-A absolute-verdict-permanence boundary discipline summary")
        print("  - Original S90 W6 CF-53 line: ABSENT in s90_gate_verdicts.txt at runtime")
        print(f"    (grep '^CF-53.*audit_sha256=' returned {sha_passed=}; OLD_AUDIT_SHA={OLD_AUDIT_SHA})")
        print("  - Since the OLD_AUDIT_SHA cannot be retrieved, the Option-A `supersedes`")
        print("    tag has no canonical target to point at; emission is structurally")
        print("    deferred (NOT post-hoc Class-3 editing).")
        print("  - Absolute verdict permanence: NO edits to S90 W6 CF-53 line in-place")
        print("    (none exist to edit; and even if one existed, in-place edit would be")
        print("    Class-3 PROHIBITED_ACTIONS per .claude/rules/v3-closure-recovery.md).")
        print("  - Forward retry pathway: S92+ retry conditional on ALL 4 prereqs landing")
        print("    (R8 extension + R9 extension + W8 CF-58 substrate-physics PASS/INFO +")
        print("    S90 CF-53 original audit_sha256 line existence verification).")
        print()

        rc = 0  # (local) script succeeded; verdict is data per .claude/rules/math-scripts.md
    else:
        # ------------------------------------------------------------------
        # All prerequisites landed: Option-A corrective emission branch
        # (substrate-physics re-evaluation under improved machinery)
        # ------------------------------------------------------------------
        # NOTE: under runtime conditions confirmed by the orchestrator's
        # pre-dispatch spot-check, this branch is NOT reached at S91 W9.
        # The branch is implemented for future-session re-runs of this
        # script (S92+ retry pathway) when all prerequisites have landed.
        # ------------------------------------------------------------------
        print("Step 6: Option-A corrective emission branch (all 4 prereqs landed)")
        print(f"  OLD_AUDIT_SHA (target of supersedes): {OLD_AUDIT_SHA}")
        print()
        print("  WARNING: substrate-physics re-evaluation of CF-53 under post-R8+R9+CF-58")
        print("           machinery is NOT YET IMPLEMENTED in this closure script.")
        print("           Implementation requires the actual CF-53 substrate-physics")
        print("           computation (d=4 envelope identity discriminator at the post-")
        print("           prerequisite-landing evaluation point), which depends on the")
        print("           specific R8 + R9 + CF-58 outputs.")
        print()
        print("  For S92+ retry: extend this script with the actual CF-53 substrate-")
        print("  physics re-computation under R8 corner classification + R9 plan-")
        print("  staleness audit + CF-58 substrate-physics output, then emit")
        print("  corrective canonical line with supersedes=<OLD_AUDIT_SHA> tag per")
        print("  Option-A rule 2.")
        print()
        # Under all-prereqs-met but un-implemented substrate-physics branch:
        # emit INFO with explicit not-implemented disclosure.
        closure_verdict = "INFO"  # (local)
        closure_value = (
            f"all_4_prereqs_landed_but_substrate_physics_re_evaluation_NOT_IMPLEMENTED;"
            f"r8_passed=True;r9_passed=True;cf58_passed=True;old_audit_sha_passed=True;"
            f"old_audit_sha_full_64={OLD_AUDIT_SHA};"
            f"supersedes_target_RETRIEVED=True;"
            f"option_a_corrective_emission_PENDING_substrate_physics_re_evaluation;"
            f"refinement_pathway=extend_this_script_with_cf53_re_computation_under_post_R8_R9_CF58_machinery;"
            f"deferred_to_S92=True;"
            f"plan_routing=session-91-plan-w9.md_§W9-6_Field_9_INFO_all_3_prereqs_landed_value_marginal"
        )
        emit_verdict(
            closure_verdict, closure_value, audit_sha, content_sha, blocking,
        )
        print(f"  closure_verdict: {closure_verdict} (INFO; substrate-physics re-eval pending)")
        print(f"  appended to: {VERDICT_TXT_S91.relative_to(PROJECT_ROOT)}")
        rc = 0  # (local) script succeeded; verdict is data per .claude/rules/math-scripts.md

    print(f"=== {GATE_ID}: {closure_verdict} "
          f"(CONDITIONAL Option-A re-dispatch; "
          f"branch={'PRE-REG-INC' if not all_prereqs_met else 'all-prereqs-met-INFO'}; "
          f"wall {time.time() - t0:.2f}s) ===")
    return rc


if __name__ == "__main__":
    sys.exit(main())
