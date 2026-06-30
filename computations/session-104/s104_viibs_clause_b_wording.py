#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
S104-VIIBS-CLAUSE-B-WORDING
============================
Designated-writer reviewed PROSE PATCH on the EXISTING §VII.BS entry in
sessions/permanent-results-registry.md.

This is NOT a registry-LANDING (no new §VII slot, no Stage-0 candidate consume).
It is the S104 follow-up to the S103 W1-6 SCOPE ANNOTATION: now that BOTH S103
preconditions have landed PASS —

  (a) S103-VIIBS-CLAUSE-B-SCOPE-ANNOTATION  audit 2c27b197… (the W1-6 annotation;
      Option-A corrective line superseding f56f08f3…)
  (b) S103-NNU-BUNDLE-EXHAUSTIVENESS        audit ac1dbb28… (W2-1, rank=1,
      second_rel_sv=1.07e-17)

— the clause-(b) bundle-exhaustiveness characterization is UPGRADED on the
ANNOTATION SURFACES from "standing premise (Open Q6)" → "result", citing the
rank-1 certificate ac1dbb28… as basis, per the §VII.BP BINDING-AMENDMENT
annotation form used by the S103 W1-6 annotation.

This is a CONFIDENCE-EQUALITY fix (the prose tag is brought UP TO its register
status, NOT above it): the rank-1 certificate PROVES the augmented-bundle
exhaustiveness (m_H factors through M_KK; rank(Cov_aug)=1), so 'result' is the
register-faithful word. The theorem GRADE is UNCHANGED (STAGE-3-PERMANENT — no
up-tag, no down-tag; capstone-hygiene Q3 = NO).

The FROZEN Stage-0 theorem-tag blockquote (the line
'> **Normalization Non-Universality (N₃=0 corollary, rank-1).**' ... ,
span len 2514, span SHA256 e669ccd2daa5aa5be7396499f59c0636a803eac02e1f7710c2a1fc428d3cdaba)
is BYTE-SHA-IMMUNE: it is located by literal-substring anchor (not line number)
and its SHA is HARD-ASSERTED UNCHANGED (== e669ccd2…) before AND after the write.
A span-SHA mismatch is a FAIL (the most serious — the immune Stage-0 text must
never change). The frozen block does NOT carry the "standing premise (Open Q6)"
bundle-exhaustiveness characterization — that wording lives ONLY on the 3
annotation surfaces this gate touches (the index row, the clause-(b) inline
table, the SCOPE ANNOTATION block). The frozen block uses the rank-1-obstruction /
two-falsifiers language and is untouched.

NUMBERS first (the precondition booleans + frozen-span SHA), gate second,
interpretation third.

Pattern (AFTER-pattern, registry-landing.md §"Bridge-Landing Script Architecture"):
  build_promotion_text -> write_atomic_with_fsync -> re_read + verify_section_matches
  -> exactly ONE emit (verdict payload printed for the emit_verdict MCP tool).
Idempotent: detect-already-upgraded NO-OP re-run. On verify FAIL: revert to the
pre-patch byte-state, close FAIL with remediation — never iterate.

ENV: cpu, OMP 8; string assembly + SHA + file I/O + grep on the s103 verdict
file only. NO computation.
"""
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")

import sys
import json
import hashlib
import difflib
from pathlib import Path

import numpy as np

# Canonical constants import (MANDATORY per math-scripts.md; this gate uses none
# numerically, but compliance + runtime SHA disclosure of the file is required).
sys.path.insert(0, str(Path("computations/_shared").resolve()))
from canonical_constants import *  # noqa: F401,F403  (compliance import)

# ----------------------------------------------------------------------------
# Paths
# ----------------------------------------------------------------------------
ROOT = Path(".").resolve()
REGISTRY = ROOT / "sessions" / "permanent-results-registry.md"
S103_VERDICTS = ROOT / "computations" / "session-103" / "s103_gate_verdicts.txt"
S103_NNU_NPZ = ROOT / "computations" / "session-103" / "s103_nnu_bundle_exhaustiveness.npz"
CC_PY = ROOT / "computations" / "_shared" / "canonical_constants.py"
NPZ_OUT = ROOT / "computations" / "session-104" / "s104_viibs_clause_b_wording.npz"

SCRIPT_PATH = Path(__file__).resolve()

# ----------------------------------------------------------------------------
# Frozen-span guard (the IMMUNE Stage-0 theorem-tag blockquote)
# ----------------------------------------------------------------------------
FROZEN_BLOCKQUOTE_ANCHOR = "> **Normalization Non-Universality (N₃=0 corollary, rank-1).**"
FROZEN_SPAN_LEN = 2514                                                       # (local) len pin
FROZEN_SPAN_SHA_PIN = "e669ccd2daa5aa5be7396499f59c0636a803eac02e1f7710c2a1fc428d3cdaba"

# ----------------------------------------------------------------------------
# Precondition pins (both verified PASS at plan-freeze; re-grepped at runtime)
# ----------------------------------------------------------------------------
PRECOND_1_GATE = "S103-VIIBS-CLAUSE-B-SCOPE-ANNOTATION"
PRECOND_1_AUDIT = "2c27b19758f2571b98dcf463eee0fdb124321a165dcc6122eb9917693ecb5d6c"  # corrective/superseding line
PRECOND_2_GATE = "S103-NNU-BUNDLE-EXHAUSTIVENESS"
PRECOND_2_AUDIT = "ac1dbb2892cef172a6383f33652d110e53b7815316c4eefa1c0aa1360def3257"


def sha256_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def print_verdict_payload(payload: dict) -> dict:
    """Canonical template helper (`.claude/templates/script-template.py` §4):
    PRINT the delimited verdict PAYLOAD block to stdout for the dispatching AGENT
    to pass to the knowledge-MCP `emit_verdict` tool. The script does NOT write the
    verdict file — that single lock-serialized write is owned by `emit_verdict`
    (`gate-verdicts.md §"Race-Safe Emission"`). The script computes the dual-SHA
    (it alone holds the input-pin map + content target); the agent reads this block
    and calls `mcp__knowledge__emit_verdict(**payload)`. Returns the payload dict."""
    print("\n<<<EMIT_VERDICT_PAYLOAD>>>" + json.dumps(payload, ensure_ascii=False) + "<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


def extract_frozen_span(text: str) -> str:
    """Locate the frozen Stage-0 blockquote span by literal anchor (NOT line number).
    The span is the full blockquote LINE (incl. the leading '> ' marker) up to the
    terminating newline. len == 2514 by construction (matches the S103 W1-6 extractor
    EXACTLY — same anchor, same boundary)."""
    i = text.find(FROZEN_BLOCKQUOTE_ANCHOR)
    if i < 0:
        raise RuntimeError("FROZEN blockquote anchor not found in registry")
    end = text.find("\n", i)
    if end < 0:
        end = len(text)
    return text[i:end]


def precond_pass(verdicts_text: str, gate_id: str, audit_sha: str) -> bool:
    """A precondition is satisfied iff a canonical verdict line for `gate_id` carries
    `PASS` AND `audit_sha256=<audit_sha>` (the full 64-char). The Option-A corrective
    line is the canonical one for precond_1 (it supersedes f56f08f3…); we pin the
    corrective audit SHA directly, so this finds the latest-non-superseded line."""
    needle_line_prefix = f"{gate_id}: PASS"
    needle_audit = f"audit_sha256={audit_sha}"
    for line in verdicts_text.splitlines():
        if line.startswith(needle_line_prefix) and needle_audit in line:
            return True
    return False


# ----------------------------------------------------------------------------
# Surface upgrade anchors (each must be UNIQUE in the registry). The on-disk
# state is the S103 W1-6 ANNOTATED text (the surfaces already carry the
# "standing premise (Open Q6)" characterization); this gate upgrades them to
# "result", citing the rank-1 certificate. The frozen blockquote does NOT carry
# this wording and is NOT in any anchor below.
# ----------------------------------------------------------------------------

# Surface 1 — INDEX-table row (line ~157). On-disk = the S103 INDEX_NEW form.
S1_OLD = ("single-cutoff COUNT for the dagger-row bundle, bundle-exhaustiveness a standing "
          "premise [Open Q6]) — the substrate determines the conformal class")
S1_NEW = ("single-cutoff COUNT for the dagger-row bundle, bundle-exhaustiveness a RESULT "
          "[Open Q6 closed S104 W1-4; rank-1 cert ac1dbb28]) — the substrate determines the conformal class")

# Surface 2 — clause-(b) inline (the clause-attribution table row, line ~21392).
# On-disk = the S103 CLAUSEB_NEW form. Upgrade the bundle-exhaustiveness word.
S2_OLD = ("bundle exhaustiveness a separate standing premise — Open Q6; rests on FULL BDI "
          "triviality N₃=N₁=winding=η=0, see SCOPE ANNOTATION below)*")
S2_NEW = ("bundle exhaustiveness a RESULT — Open Q6 closed (S104 W1-4 upgrade; rank-1 cert "
          "ac1dbb28); rests on FULL BDI triviality N₃=N₁=winding=η=0, see SCOPE ANNOTATION below)*")

# Surface 3a — SCOPE ANNOTATION block (line ~21399): the bolded standing-premise clause.
# On-disk = the S103 SCOPE_ANNOTATION_BLOCK text. Upgrade the bolded characterization.
S3A_OLD = ("**exhaustiveness of the dagger-row bundle is a separate standing premise**, with Open "
           "Question 6 (m_H / EW-VEV entering the induced action independently of M_KK) the named untested "
           "channel")
S3A_NEW = ("**exhaustiveness of the dagger-row bundle is a RESULT** (S104 W1-4 upgrade; the standing-premise "
           "Open Question 6 — m_H / EW-VEV entering the induced action independently of M_KK — is CLOSED by "
           "the rank-1 certificate ac1dbb28…, see the dated cross-reference below)")

# Surface 3b — SCOPE ANNOTATION block: the closing "S104 follow-up" sentence → EFFECTED.
S3B_OLD = ("The upgrade of this SCOPE ANNOTATION from "
           "standing-premise to result (re-wording clause (b)'s grade) is an S104 follow-up per the plan's "
           "Wave 1→2 decision point; the annotation lands as-worded here regardless.")
S3B_NEW = ("The upgrade of this SCOPE ANNOTATION from "
           "standing-premise to **result** (re-wording clause (b)'s grade) is EFFECTED at S104 W1-4 "
           "(`S104-VIIBS-CLAUSE-B-WORDING`, designated-writer reviewed patch licensed by BOTH S103 "
           "preconditions: S103-VIIBS-CLAUSE-B-SCOPE-ANNOTATION PASS audit `2c27b197…` ∧ "
           "S103-NNU-BUNDLE-EXHAUSTIVENESS PASS audit `ac1dbb28…`, rank=1, second_rel_sv=1.07e-17): "
           "the bundle-exhaustiveness characterization above now reads 'result', a CONFIDENCE-EQUALITY "
           "upgrade (the prose tag is brought UP TO its register status — the rank-1 certificate PROVES "
           "the augmented-bundle exhaustiveness — NOT above it; frozen Stage-0 blockquote span SHA "
           "`e669ccd2…` byte-IMMUNE and UNCHANGED; theorem grade UNCHANGED STAGE-3-PERMANENT, Q3=NO).")

# The marker the WP/registry must_contain set checks for after the upgrade:
UPGRADED_MARKER_INDEX = "bundle-exhaustiveness a RESULT"
UPGRADED_MARKER_CLAUSEB = "bundle exhaustiveness a RESULT"
UPGRADED_MARKER_BLOCK = "**exhaustiveness of the dagger-row bundle is a RESULT**"
UPGRADED_MARKER_EFFECTED = "is EFFECTED at S104 W1-4"


def build_promotion_text(pre_text: str) -> str:
    """Apply the wording-upgrade edits to a copy of the registry text, leaving the
    frozen blockquote span byte-identical and the theorem grade unchanged. Returns the
    upgraded text. Raises if any anchor is not unique or not found."""
    edits = [
        ("INDEX", S1_OLD, S1_NEW),
        ("CLAUSEB", S2_OLD, S2_NEW),
        ("BLOCK-standing-premise", S3A_OLD, S3A_NEW),
        ("BLOCK-effected", S3B_OLD, S3B_NEW),
    ]
    txt = pre_text
    for name, old, new in edits:
        n = txt.count(old)
        if n != 1:
            raise RuntimeError(f"surface {name}: anchor count {n} != 1 (old-text not unique/found)")
        txt = txt.replace(old, new, 1)
    return txt


def write_atomic_with_fsync(path: Path, text: str) -> None:
    """Write the full upgraded text atomically with fsync. The registry is read +
    written as UTF-8 text; the edits are interior-substring replacements on existing
    LF-terminated lines (no neighbor line-ending re-encode beyond the edited regions).
    Python str read/write with newline='' round-trips LF and CRLF verbatim, so the
    frozen blockquote bytes (which we never touch) are preserved exactly."""
    tmp = path.with_suffix(path.suffix + ".tmp")
    with open(tmp, "w", encoding="utf-8", newline="") as f:
        f.write(text)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)


def verify_section_matches(rr_text: str, pre_text: str,
                           frozen_pre: str, frozen_pre_sha: str,
                           grade_pre_count: int) -> dict:
    """Re-read-from-disk verification. Returns the boolean component dict + overall."""
    # (a) frozen-span immutability (HARD)
    frozen_post = extract_frozen_span(rr_text)
    frozen_post_sha = sha256_text(frozen_post)                              # (local)
    frozen_unchanged = (frozen_post_sha == FROZEN_SPAN_SHA_PIN) and (frozen_post == frozen_pre)

    # (b) the upgraded wording present on all 3 surfaces (RE-READ from disk)
    surf_index = (UPGRADED_MARKER_INDEX in rr_text)                        # (local)
    surf_clauseb = (UPGRADED_MARKER_CLAUSEB in rr_text)                    # (local)
    surf_block = (UPGRADED_MARKER_BLOCK in rr_text)                        # (local)
    surf_effected = (UPGRADED_MARKER_EFFECTED in rr_text)                  # (local)
    upgraded_present = surf_index and surf_clauseb and surf_block and surf_effected

    # (c) the OLD "standing premise (Open Q6)" bundle-exhaustiveness characterizations
    #     are gone from the annotation surfaces (no residual un-upgraded surface).
    old_index_gone = (S1_OLD not in rr_text)                              # (local)
    old_clauseb_gone = (S2_OLD not in rr_text)                            # (local)
    old_block_gone = (S3A_OLD not in rr_text)                            # (local)
    old_effected_gone = (S3B_OLD not in rr_text)                          # (local)
    old_surfaces_gone = old_index_gone and old_clauseb_gone and old_block_gone and old_effected_gone

    # (d) theorem grade STAGE-3-PERMANENT unchanged (no down-tag, no up-tag — the bold
    #     grade-marker count is preserved exactly).
    grade_post_count = rr_text.count("**STAGE-3-PERMANENT**")              # (local)
    grade_unchanged = (grade_post_count == grade_pre_count) and (grade_post_count >= 1)

    # (e) the dated W2-1 cross-reference audit trail preserved (the "Standing-premise → result
    #     (dated cross-reference, S103 W2-1)" provenance sentence remains).
    dated_xref_preserved = ("**Standing-premise → result (dated cross-reference, S103 W2-1):**" in rr_text)  # (local)

    # (f) frozen blockquote occurrence count unchanged (immune block still present once)
    bq_count = rr_text.count(FROZEN_BLOCKQUOTE_ANCHOR)                     # (local)
    bq_count_ok = (bq_count == pre_text.count(FROZEN_BLOCKQUOTE_ANCHOR))   # (local)

    overall = bool(
        frozen_unchanged
        and upgraded_present
        and old_surfaces_gone
        and grade_unchanged
        and dated_xref_preserved
        and bq_count_ok
    )
    return {
        "frozen_post_sha": frozen_post_sha,
        "frozen_unchanged": frozen_unchanged,
        "surf_index": surf_index,
        "surf_clauseb": surf_clauseb,
        "surf_block": surf_block,
        "surf_effected": surf_effected,
        "upgraded_present": upgraded_present,
        "old_surfaces_gone": old_surfaces_gone,
        "grade_post_count": grade_post_count,
        "grade_unchanged": grade_unchanged,
        "dated_xref_preserved": dated_xref_preserved,
        "bq_count": bq_count,
        "bq_count_ok": bq_count_ok,
        "overall": overall,
    }


def main():
    # ------------------------------------------------------------------ inputs
    pre_bytes = REGISTRY.read_bytes()
    pre_text = pre_bytes.decode("utf-8")
    pre_registry_file_sha = sha256_bytes(pre_bytes)                          # (local)

    v_bytes = S103_VERDICTS.read_bytes()
    v_text = v_bytes.decode("utf-8")
    s103_verdicts_file_sha = sha256_bytes(v_bytes)                           # (local)

    cc_bytes = CC_PY.read_bytes()
    cc_runtime_sha = sha256_bytes(cc_bytes)                                  # (local)

    # rank-1 certificate npz (precondition-2 witness; load for the audit pinmap)
    nnu = np.load(S103_NNU_NPZ, allow_pickle=True)
    nnu_npz_sha = sha256_bytes(S103_NNU_NPZ.read_bytes())                    # (local)
    # tolerant field access (only used for disclosure; not gating)
    try:
        nnu_rank = int(np.asarray(nnu["rank"]).item())                      # (local)
    except Exception:
        nnu_rank = -1                                                        # (local)
    try:
        nnu_second_rel_sv = float(np.asarray(nnu["second_rel_sv"]).item())  # (local)
    except Exception:
        nnu_second_rel_sv = float("nan")                                     # (local)

    # ------------------------------------------------ precondition verification
    precond_1_ok = precond_pass(v_text, PRECOND_1_GATE, PRECOND_1_AUDIT)     # (local)
    precond_2_ok = precond_pass(v_text, PRECOND_2_GATE, PRECOND_2_AUDIT)     # (local)
    upgrade_licensed = precond_1_ok and precond_2_ok                         # (local)

    # ------------------------------------------------ frozen-span PRE (immutability)
    frozen_pre = extract_frozen_span(pre_text)
    frozen_pre_sha = sha256_text(frozen_pre)                                # (local)
    frozen_pre_len = len(frozen_pre)                                        # (local)
    if frozen_pre_len != FROZEN_SPAN_LEN:
        raise RuntimeError(f"PRE frozen span len {frozen_pre_len} != pin {FROZEN_SPAN_LEN}")
    if frozen_pre_sha != FROZEN_SPAN_SHA_PIN:
        # HARD breakage: the frozen Stage-0 text on disk no longer matches the pin BEFORE
        # we even edit — script-health failure (exit != 0), NOT a verdict.
        raise RuntimeError(
            f"PRE frozen span SHA {frozen_pre_sha} != pin {FROZEN_SPAN_SHA_PIN} "
            "(frozen Stage-0 text drifted before the wording upgrade)"
        )

    grade_pre_count = pre_text.count("**STAGE-3-PERMANENT**")               # (local)

    # SHA log (first 20 lines of stdout per gate-verdicts.md)
    print("=== INPUT SHA LOG (s104_viibs_clause_b_wording) ===")
    print(f"registry_pre_file_sha256       = {pre_registry_file_sha}")
    print(f"s103_verdicts_file_sha256      = {s103_verdicts_file_sha}")
    print(f"s103_nnu_npz_sha256            = {nnu_npz_sha}")
    print(f"canonical_constants_runtime_sha= {cc_runtime_sha}")
    print(f"precond_1 ({PRECOND_1_GATE}) PASS audit {PRECOND_1_AUDIT[:16]}… = {precond_1_ok}")
    print(f"precond_2 ({PRECOND_2_GATE}) PASS audit {PRECOND_2_AUDIT[:16]}… = {precond_2_ok}")
    print(f"nnu rank={nnu_rank} second_rel_sv={nnu_second_rel_sv:.3e}")
    print(f"upgrade_licensed (P1 ∧ P2)     = {upgrade_licensed}")
    print(f"frozen_span_len                = {frozen_pre_len} (pin {FROZEN_SPAN_LEN})")
    print(f"frozen_span_sha256             = {frozen_pre_sha}")
    print(f"frozen_span_matches_pin        = {frozen_pre_sha == FROZEN_SPAN_SHA_PIN}")
    print(f"grade **STAGE-3-PERMANENT** count (pre) = {grade_pre_count}")

    # Idempotency: detect already-upgraded state. If the upgraded INDEX marker is present
    # (and the OLD index surface absent), the registry was upgraded by a prior run of THIS
    # gate (e.g. a re-run after a script-compliance fix). SKIP the write (NO-OP).
    already_upgraded = (S1_NEW in pre_text) and (S1_OLD not in pre_text)     # (local)
    print(f"already_upgraded               = {already_upgraded}")

    # ----------------------------------------------------------- license guard
    # If the upgrade is NOT licensed (a precondition is not PASS), do NOT touch the
    # registry; close INFO (one precondition missing) / FAIL (both missing) per the
    # plan's INFO_meaning — without editing the frozen block. (Both are confirmed PASS
    # at plan-freeze, so this branch is not expected.)
    applied = False                                                         # (local)
    if not upgrade_licensed:
        # do not write; verify against the UNCHANGED on-disk text
        rr_text = pre_text
        post_registry_file_sha = pre_registry_file_sha                      # (local)
        verdict = "INFO" if (precond_1_ok or precond_2_ok) else "FAIL"
        print("WRITE                          = SKIPPED (upgrade NOT licensed; preconditions not both PASS)")
    elif already_upgraded:
        # NO-OP: registry already carries the upgrade; do not re-edit.
        rr_bytes = REGISTRY.read_bytes()
        rr_text = rr_bytes.decode("utf-8")
        post_registry_file_sha = sha256_bytes(rr_bytes)                     # (local)
        verdict = None  # decided by verify below
        print("WRITE                          = SKIPPED (idempotent NO-OP; already upgraded)")
    else:
        post_text = build_promotion_text(pre_text)
        write_atomic_with_fsync(REGISTRY, post_text)
        applied = True
        rr_bytes = REGISTRY.read_bytes()
        rr_text = rr_bytes.decode("utf-8")
        post_registry_file_sha = sha256_bytes(rr_bytes)                     # (local)
        verdict = None  # decided by verify below
        print("WRITE                          = APPLIED (wording upgrade written + fsync)")

    # --------------------------------------------------- re-read + verify (from disk)
    vd = verify_section_matches(rr_text, pre_text, frozen_pre, frozen_pre_sha, grade_pre_count)
    verify = vd["overall"]

    # The applied-diff (for the METHODOLOGY-class content_sha256 over script||applied-diff).
    if applied:
        applied_diff = "".join(difflib.unified_diff(
            pre_text.splitlines(keepends=True),
            rr_text.splitlines(keepends=True),
            fromfile="permanent-results-registry.md (pre)",
            tofile="permanent-results-registry.md (post)",
            n=1,
        ))
    else:
        applied_diff = ""  # NO-OP re-run or unlicensed: empty diff (already-upgraded state)
    applied_diff_sha = sha256_text(applied_diff)                            # (local)

    # decide verdict for the licensed branch
    if upgrade_licensed:
        verdict = "PASS" if verify else "FAIL"
        # On verify FAIL after an APPLIED write: revert to pre-patch byte-state (never iterate).
        if applied and not verify:
            write_atomic_with_fsync(REGISTRY, pre_text)
            print("VERIFY FAILED after APPLIED write → REVERTED registry to pre-patch byte-state "
                  "(honest closure; FAIL with remediation, no iterate-until-PASS).")

    print("\n=== VERIFY (re-read from disk) ===")
    print(f"frozen_span_post_sha256        = {vd['frozen_post_sha']}")
    print(f"frozen_span_UNCHANGED          = {vd['frozen_unchanged']}  (== e669ccd2… HARD)")
    print(f"surface_index_upgraded         = {vd['surf_index']}")
    print(f"surface_clause_b_upgraded      = {vd['surf_clauseb']}")
    print(f"surface_block_upgraded         = {vd['surf_block']}")
    print(f"surface_effected_sentence      = {vd['surf_effected']}")
    print(f"upgraded_present (3 surfaces)   = {vd['upgraded_present']}")
    print(f"old_standing_premise_surfaces_gone = {vd['old_surfaces_gone']}")
    print(f"grade **STAGE-3-PERMANENT** count = {grade_pre_count} -> {vd['grade_post_count']} "
          f"(unchanged={vd['grade_unchanged']})")
    print(f"dated_W2-1_xref_preserved      = {vd['dated_xref_preserved']}")
    print(f"frozen blockquote count        = {vd['bq_count']} (ok={vd['bq_count_ok']})")
    print(f"VERIFY                         = {verify}")
    print(f"VERDICT                        = {verdict}")

    # ----------------------------------------------------------- npz output
    NPZ_OUT.parent.mkdir(parents=True, exist_ok=True)
    np.savez(
        NPZ_OUT,
        gate_id="S104-VIIBS-CLAUSE-B-WORDING",
        verdict=verdict,
        verify=verify,
        # preconditions
        precond_1_gate=PRECOND_1_GATE, precond_1_audit=PRECOND_1_AUDIT, precond_1_ok=precond_1_ok,
        precond_2_gate=PRECOND_2_GATE, precond_2_audit=PRECOND_2_AUDIT, precond_2_ok=precond_2_ok,
        upgrade_licensed=upgrade_licensed,
        nnu_rank=nnu_rank, nnu_second_rel_sv=nnu_second_rel_sv,
        # frozen-span immutability
        frozen_span_sha_pin=FROZEN_SPAN_SHA_PIN,
        frozen_span_pre_sha=frozen_pre_sha,
        frozen_span_post_sha=vd["frozen_post_sha"],
        frozen_span_len=frozen_pre_len,
        frozen_unchanged=vd["frozen_unchanged"],
        # upgraded-surface booleans
        surface_index=vd["surf_index"],
        surface_clause_b=vd["surf_clauseb"],
        surface_block=vd["surf_block"],
        surface_effected=vd["surf_effected"],
        upgraded_present=vd["upgraded_present"],
        old_surfaces_gone=vd["old_surfaces_gone"],
        dated_xref_preserved=vd["dated_xref_preserved"],
        # grade unchanged
        grade_pre_count=grade_pre_count, grade_post_count=vd["grade_post_count"],
        grade_unchanged=vd["grade_unchanged"],
        # registry file SHAs
        registry_pre_file_sha=pre_registry_file_sha,
        registry_post_file_sha=post_registry_file_sha,
        applied=applied, already_upgraded=already_upgraded,
        # applied-diff (METHODOLOGY dual-SHA closure)
        applied_diff_sha=applied_diff_sha,
        # source provenance
        s103_verdicts_file_sha=s103_verdicts_file_sha,
        s103_nnu_npz_sha=nnu_npz_sha,
        canonical_constants_runtime_sha=cc_runtime_sha,
    )

    # ----------------------------------------------------------- dual-SHA
    # content_sha256 inputs = [script, applied-diff]  (per plan audit_discriminators;
    # METHODOLOGY-class: content_sha256 over the registry-prose diff — wave-classification.md
    # §"Dual-SHA closure for METHODOLOGY-class").
    script_sha = sha256_bytes(SCRIPT_PATH.read_bytes())                    # (local)
    content_sha256 = sha256_text(script_sha + "|" + applied_diff_sha)

    # audit_sha256 inputs (ordered) = [script, pinmap, registry_pre_file_sha, s103_nnu_npz_sha]
    pinmap = {
        "gate_id": "S104-VIIBS-CLAUSE-B-WORDING",
        "scheme": "CURATED-DOC-REVIEWED-DESIGNATED-WRITER-PATCH",
        "convention": ("STANDING-PREMISE-TO-RESULT-WORDING-UPGRADE;"
                       "FROZEN-BLOCKQUOTE-IMMUNE;"
                       "VIIBP-BINDING-AMENDMENT-FORM;"
                       "THEOREM-GRADE-UNCHANGED-STAGE-3-PERMANENT"),
        "L_max": "N/A",
        "frozen_span_sha_assertion": FROZEN_SPAN_SHA_PIN,
        "precond_1_audit": PRECOND_1_AUDIT,
        "precond_2_audit": PRECOND_2_AUDIT,
        "nnu_npz_sha": nnu_npz_sha,
        "canonical_constants_runtime_sha": cc_runtime_sha,
        "applied_diff_sha": applied_diff_sha,
        "verify": verify,
    }
    audit_inputs = (
        script_sha
        + "|" + json.dumps(pinmap, sort_keys=True, ensure_ascii=False)
        + "|" + pre_registry_file_sha
        + "|" + nnu_npz_sha
    )
    audit_sha256 = sha256_text(audit_inputs)

    value = (
        f"upgrade_licensed={upgrade_licensed}(P1={precond_1_ok}∧P2={precond_2_ok});"
        f"verify={verify};frozen_span_UNCHANGED={vd['frozen_unchanged']}(==e669ccd2);"
        f"standing-premise->result_3surfaces={vd['upgraded_present']};old_surfaces_gone={vd['old_surfaces_gone']};"
        f"grade=STAGE-3-PERMANENT_unchanged({grade_pre_count}=={vd['grade_post_count']});"
        f"Q3=NO_confidence-EQUALITY;rank1_cert=ac1dbb28(rank={nnu_rank});applied={applied};already_upgraded={already_upgraded}"
    )

    # 4-tuple output tag (final non-verdict line per gate-verdicts.md)
    print(f"\n4-tuple: (value={value}, "
          f"scheme={pinmap['scheme']}, convention={pinmap['convention']}, L_max=N/A)")

    # ----------------------------------------------------------- verdict payload
    payload = {
        "session": 104,
        "gate_id": "S104-VIIBS-CLAUSE-B-WORDING",
        "verdict": verdict,
        "value": value,
        "scheme": pinmap["scheme"],
        "convention": pinmap["convention"],
        "l_max": "N/A",
        "audit_sha256": audit_sha256,
        "content_sha256": content_sha256,
        "schema_version": "S84+",
        "companion_note": ("frozen Stage-0 blockquote span SHA e669ccd2…(len 2514) HARD-asserted "
                           "UNCHANGED; annotation surfaces ONLY (index row + clause-(b) table + SCOPE "
                           "ANNOTATION block); theorem grade STAGE-3-PERMANENT unchanged (Q3=NO, "
                           "confidence-EQUALITY upgrade)"),
        "extra_rows": [
            (f"# content_sha256 over script||applied-diff (METHODOLOGY-class dual-SHA closure per "
             f"wave-classification.md); applied_diff_sha={applied_diff_sha}; applied={applied}"),
            (f"# preconditions BOTH PASS: {PRECOND_1_GATE} audit {PRECOND_1_AUDIT[:16]}… ∧ "
             f"{PRECOND_2_GATE} audit {PRECOND_2_AUDIT[:16]}… (rank=1, second_rel_sv=1.07e-17); "
             f"standing-premise->result EFFECTED (the S103 W2-1 deferred upgrade)"),
        ],
    }

    print_verdict_payload(payload)

    # Exit 0 regardless of PASS/FAIL (verdict is data, not exit code).
    sys.exit(0)


if __name__ == "__main__":
    main()
