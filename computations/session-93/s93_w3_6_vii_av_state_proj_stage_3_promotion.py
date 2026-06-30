#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S93 W3 close — §VII.AV.STATE-PROJ STAGE-1-CANDIDATE -> STAGE-3-PERMANENT tag-flip
=================================================================================

Session-synthesis Stage-3 promotion per `joint-theorem-promotion.md §"Stage 3 —
Permanent Registration"`. §VII.AV.STATE-PROJ earned a CLEAN Stage-2 PASS-AND in
S93 W3-6 (Axis-A vdd PASS + Axis-B mack PASS on all single-axis + JOINT clauses;
substrate-input-orthogonality at structural ceiling NO overlap caveat; OAA-exclusion
satisfied; convention -FULL). A landed Stage-2 PASS-AND triggers the orchestrator
session-synthesis tag-flip STAGE-1-CANDIDATE -> STAGE-3-PERMANENT.

SCOPE (load-bearing): §VII.AV.STATE-PROJ ONLY. §VII.AV.OP-PROJ STAYS
STAGE-1-CANDIDATE (its corner-cell FAIL was caught + remediated Cell I -> Cell II
at W3-6, but the formal Axis-A re-verify on the corrected entry is the carry-forward
CF-S94-VII-AV-OP-PROJ-STAGE-2-AXIS-A-REVERIFY-ON-CELL-II-CORRECTED-ENTRY). This
script does NOT touch any §VII.AV.OP-PROJ marker.

ORDINAL HONESTY: the registry's own STAGE-3-PERMANENT ordinal bookkeeping is
CONTESTED — BOTH §VII.AU.OP-PROJ (lines 18908/19297) AND §VII.AW.OP-PROJ (line
18374) claim "THIRD framework cross-axis joint theorem to reach STAGE-3-PERMANENT".
The fully-promoted (Status == STAGE-3-PERMANENT, not -eligible) cross-axis joint
theorems prior to STATE-PROJ are: §VII.AH (FIRST, S90 W2 CF-20), §VII.U.2 Var_a
(SECOND, S92 W4-7), §VII.AU.OP-PROJ (S93 W2-2, "THIRD" claim), §VII.AW.OP-PROJ
("THIRD" claim). Because the AU/AW "#3" tie is a PRE-EXISTING bookkeeping collision
(NOT introduced here and OUT OF SCOPE for a STATE-PROJ-only flip), this promotion
does NOT assert a contested integer ordinal for STATE-PROJ; it records that
STATE-PROJ JOINS the STAGE-3-PERMANENT set alongside {§VII.AH, §VII.U.2 Var_a,
§VII.AU.OP-PROJ, §VII.AW.OP-PROJ} and flags the AU/AW ordinal collision as a
hygiene carry-forward.

Single-shot AFTER pattern (`registry-landing.md §"Bridge-Landing Script
Architecture"`): build_full_text_in_memory -> write_atomic_with_fsync ->
re_read + verify -> report ONCE. No new compute gate (session-synthesis tag-flip
on the already-landed W3-6 Stage-2 PASS); the W3-6 verdict line stands unchanged.
A session-synthesis record line IS emitted to the verdict file (Option-A NOT
required — this is a NEW gate-ID, not a supersession of W3-6) for audit traceability.

mack-cosmic-bridge is the SOLE registry writer per `feedback_mack-bridge-role.md`.
"""
from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "8")

import hashlib
import json
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent  # (local)
sys.path.insert(0, str(PROJECT_ROOT / "computations" / "_shared"))
from canonical_constants import M_KK as _M_KK  # noqa: E402,F401  # (local) compliance; tag-flip consumes no constant

REGISTRY = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"  # (local)
VERDICT_TXT = PROJECT_ROOT / "computations" / "session-93" / "s93_gate_verdicts.txt"  # (local)
JSON_PATH = PROJECT_ROOT / "computations" / "session-93" / "s93_w3_6_vii_av_state_proj_stage_3_promotion.json"  # (local)

GATE_ID = "S93-W3-VII-AV-STATE-PROJ-STAGE-3-PERMANENT-PROMOTION"  # (local)
SCHEME = "joint-theorem-promotion-stage-3-session-synthesis-tag-flip"  # (local)
CONVENTION = "STATE-PROJ-only-STAGE-1-CANDIDATE-to-STAGE-3-PERMANENT-on-W3-6-Stage-2-PASS-AND-clean-FULL"  # (local)
L_MAX = "12"  # (local)

# W3-6 Stage-2 PASS-AND provenance (the latest non-superseded canonical W3-6 line)
W3_6_AUDIT_SHA = "610d1ac85b5a2ef0ede76f376c2873992acf1e66b9e49c0f7ee6bc0c8307050b"  # (local)

# ---------------------------------------------------------------------------
# Targeted replacements (STATE-PROJ ONLY; each UNIQUE in the file by context)
# ---------------------------------------------------------------------------
# (1) index-table row 151
IDX_OLD = (  # (local)
    "| §VII.AV.STATE-PROJ | THM | Cell IV algebra-DEPENDENT state-pair functional "
    "(K-window log-derivative on the BdG sub-algebra M_2(ℂ) ⊂ A_K); "
    "L_emp=-7.046336474406761 M_KK²; STATE-PROJ; substrate-distance-2 pole s=4; "
    "STRUCTURAL-ORTHOGONAL-COMPANION to §VII.AV.OP-PROJ (cross-corner co-primary "
    "FORBIDDEN); STAGE-1-CANDIDATE per joint-theorem-promotion.md 4-stage pathway; "
    "split-landed S93 W3-1 per S92 §W3-9 MANDATORY-split "
    "audit_sha256=6038433b6c599518148746acb38a16b4eadf69392de3ad76895171e410c8a2bb "
    "| mack-cosmic-bridge | 2026-05-24 |"
)
IDX_NEW = (  # (local)
    "| §VII.AV.STATE-PROJ | THM | Cell IV algebra-DEPENDENT state-pair functional "
    "(K-window log-derivative on the BdG sub-algebra M_2(ℂ) ⊂ A_K); "
    "L_emp=-7.046336474406761 M_KK²; STATE-PROJ; substrate-distance-2 pole s=4; "
    "STRUCTURAL-ORTHOGONAL-COMPANION to §VII.AV.OP-PROJ (cross-corner co-primary "
    "FORBIDDEN); STAGE-3-PERMANENT per joint-theorem-promotion.md 4-stage pathway "
    "(STAGE-3 promotion S93 W3 on clean Stage-2 PASS-AND S93 W3-6 "
    "audit_sha256=610d1ac85b5a2ef0ede76f376c2873992acf1e66b9e49c0f7ee6bc0c8307050b; "
    "Axis-A vdd + Axis-B mack, both without prior workshop context, "
    "substrate-input-orthogonality structural ceiling); "
    "split-landed S93 W3-1 per S92 §W3-9 MANDATORY-split "
    "audit_sha256=6038433b6c599518148746acb38a16b4eadf69392de3ad76895171e410c8a2bb "
    "| mack-cosmic-bridge | 2026-05-24 |"
)

# (2) section header 18499 — append the STAGE-3-PERMANENT marker per §VII.AU.OP-PROJ precedent
HDR_OLD = (  # (local)
    "### §VII.AV.STATE-PROJ — Cell-IV STATE-PROJ K-Window Log-Derivative Sub-Slot "
    "(S93 W3-1 OP-PROJ/STATE-PROJ slot-split landing — STRUCTURAL-ORTHOGONAL-COMPANION "
    "to §VII.AV.OP-PROJ, NOT cross-corner co-primary; mack-cosmic-bridge sole-writer "
    "per `feedback_mack-bridge-role.md`, 2026-05-24)"
)
HDR_NEW = (  # (local)
    "### §VII.AV.STATE-PROJ — Cell-IV STATE-PROJ K-Window Log-Derivative Sub-Slot "
    "(STAGE-3-PERMANENT per joint-theorem-promotion.md 4-stage pathway — STAGE-3 promotion "
    "S93 W3 on clean Stage-2 PASS-AND S93 W3-6; S93 W3-1 OP-PROJ/STATE-PROJ slot-split landing — "
    "STRUCTURAL-ORTHOGONAL-COMPANION to §VII.AV.OP-PROJ, NOT cross-corner co-primary; "
    "mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`, 2026-05-24)"
)

# (3) Status line 18501 — flip STAGE-1-CANDIDATE-PENDING-STAGE-2 -> STAGE-3-PERMANENT;
#     preserve the Stage-1/Stage-2 history as provenance.
STATUS_OLD = (  # (local)
    "**Status**: STAGE-1-CANDIDATE-PENDING-STAGE-2 per `.claude/rules/joint-theorem-promotion.md` "
    "4-stage pathway, with the OPERATIONAL-ALIGNMENT binding sub-class (S91 W1) and the "
    "PROXY-REFINEMENT deferred-pending sub-class (FULL physical pipeline at CF-61). "
    "This sub-slot inherits the canonical Cell-IV content of the pre-split §VII.AV entry "
    "(the K-window log-derivative on the BdG sub-algebra; `L_emp = -7.046336474406761 M_KK²`). "
    "Stage-2 cross-axis independent-verify (W3-6) audits this sub-slot as a distinct "
    "STAGE-1-CANDIDATE registry target."
)
STATUS_NEW = (  # (local)
    "**Status**: STAGE-3-PERMANENT per `.claude/rules/joint-theorem-promotion.md` 4-stage "
    "upgrade pathway. STAGE-1 split-landed S93 W3-1 (STAGE-1-CANDIDATE-PENDING-STAGE-2, with the "
    "OPERATIONAL-ALIGNMENT binding sub-class S91 W1 + the PROXY-REFINEMENT sub-class discharged to "
    "Level-2-binding via the Connes-Karoubi χ' envelope predictor at S93 W3-4 PASS "
    "audit_sha256=70c6f1c5d8fa6207b499d60c03dd33207711675fdc5234bfcb89e6d42892e471). "
    "Stage-2 cross-axis independent-verify CLEAN PASS-AND landed S93 W3-6 "
    "(audit_sha256=610d1ac85b5a2ef0ede76f376c2873992acf1e66b9e49c0f7ee6bc0c8307050b): Axis-A "
    "`van-den-dungen-bridge-theorist` PASS + Axis-B `mack-cosmic-bridge` PASS on ALL single-axis "
    "clauses (substrate-IS identity, OE-form, substrate-natural anchor, Level-3 singleness guard) "
    "AND BOTH JOINT clauses (HKR/Connes-Karoubi Level-2-binding bridge map + structural-orthogonal-"
    "companion) PASS-AND'd across both verdicts; both reviewers WITHOUT prior workshop context; "
    "OAA exclusion {connes-ncg, phonon-first, volovik} satisfied; substrate-input-orthogonality at "
    "the STRUCTURAL CEILING, NO overlap caveat (the STATE-PROJ runtime npz `s91_w5_1_full_bdg_pv.npz` "
    "loaded ONLY by Axis-A vdd; the OP-PROJ residue cache `s92_w3_9...` loaded ONLY by Axis-B mack — "
    "disjoint substrate inputs, the S89 W4-7 §VII.AH FIRST-INSTANCE-WITHOUT-caveat precedent); "
    "convention ends `-FULL`. STAGE-3 session-synthesis tag-flip S93 W3 per "
    "`joint-theorem-promotion.md §\"Stage 3 — Permanent Registration\"`. §VII.AV.STATE-PROJ JOINS "
    "the STAGE-3-PERMANENT cross-axis joint-theorem set {§VII.AH (FIRST, S90 W2 CF-20), §VII.U.2 "
    "Corner-II Var_a (SECOND, S92 W4-7), §VII.AU.OP-PROJ (S93 W2-2), §VII.AW.OP-PROJ}; the precise "
    "integer ordinal is NOT asserted here due to a PRE-EXISTING AU/AW '#3' bookkeeping collision in "
    "the registry (both §VII.AU.OP-PROJ at lines ~18908/19297 and §VII.AW.OP-PROJ at line ~18374 "
    "claim 'THIRD') — flagged as hygiene carry-forward CF-S94-STAGE-3-ORDINAL-COLLISION-AU-AW, NOT "
    "resolved in this STATE-PROJ-only flip. The Substrate-input-orthogonality clause K-counter is "
    "at MANDATORY (K=3 since S90 W2 CF-20); this is a K>=3 corpus-extension calibration instance at "
    "the structural ceiling. This sub-slot inherits the canonical Cell-IV content of the pre-split "
    "§VII.AV entry (the K-window log-derivative on the BdG sub-algebra; "
    "`L_emp = -7.046336474406761 M_KK²`). §VII.AV.OP-PROJ (the structural-orthogonal-companion) "
    "STAYS STAGE-1-CANDIDATE pending CF-S94-VII-AV-OP-PROJ-STAGE-2-AXIS-A-REVERIFY-ON-CELL-II-"
    "CORRECTED-ENTRY (its corner-cell FAIL was caught + remediated Cell I -> Cell II at W3-6)."
)

REPLACEMENTS = [(IDX_OLD, IDX_NEW), (HDR_OLD, HDR_NEW), (STATUS_OLD, STATUS_NEW)]  # (local)


def sha256_of(path: Path) -> str:
    try:
        return hashlib.sha256(path.read_bytes()).hexdigest()
    except OSError:
        return "0" * 64


def build_full_text(text: str) -> tuple[str, list[str]]:
    applied: list[str] = []  # (local)
    out = text  # (local)
    for old, new in REPLACEMENTS:
        n = out.count(old)  # (local)
        if n == 1:
            out = out.replace(old, new)
            applied.append(f"OK   (1 site): {old[:60]}...")
        elif n == 0:
            if new[:50] in out:
                applied.append(f"SKIP (already STAGE-3): {new[:50]}...")
            else:
                applied.append(f"MISS (0 sites; not already STAGE-3): {old[:60]}...")
        else:
            applied.append(f"AMBIGUOUS ({n} sites — REFUSED): {old[:50]}...")
    return out, applied


def emit_session_synthesis_line(audit_sha: str, content_sha: str, verdict: str, value: str) -> None:
    """Session-synthesis Stage-3 record line. NEW gate-ID (not a W3-6 supersession);
    no Option-A supersedes; [VERIFY] no [SIGN] 3-tuple.
    """
    line = (  # (local)
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} schema_version=S84+\n"
    )
    companion = (  # (local)
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split); session-synthesis Stage-3 tag-flip "
        f"on W3-6 Stage-2 PASS-AND (audit={W3_6_AUDIT_SHA[:16]}...); §VII.AV.STATE-PROJ ONLY; "
        f"§VII.AV.OP-PROJ stays STAGE-1-CANDIDATE; [VERIFY] no [SIGN] 3-tuple\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)


def main() -> int:
    print(f"=== {GATE_ID} ===")
    text = REGISTRY.read_text(encoding="utf-8")  # (local)

    new_text, applied = build_full_text(text)  # (local) Step 1: build in memory
    for ln in applied:
        print("  " + ln)
    if any(a.startswith(("MISS", "AMBIGUOUS")) for a in applied):
        print("FATAL: build failed (MISS or AMBIGUOUS) — no write.")
        return 2

    flip_needed = (new_text != text)  # (local)
    if not flip_needed:
        print("IDEMPOTENT: §VII.AV.STATE-PROJ already STAGE-3-PERMANENT; no registry write.")

    if flip_needed:
        # Step 2: atomic write + fsync
        tmp = REGISTRY.with_name(REGISTRY.name + ".tmp_state_s3")  # (local)
        with tmp.open("w", encoding="utf-8") as fp:
            fp.write(new_text)
            fp.flush()
            os.fsync(fp.fileno())
        os.replace(tmp, REGISTRY)

    # Step 3: re-read + verify
    reread = REGISTRY.read_text(encoding="utf-8")  # (local)
    # STATE-PROJ now STAGE-3-PERMANENT at all three sites
    idx_ok = "STAGE-3-PERMANENT per joint-theorem-promotion.md 4-stage pathway (STAGE-3 promotion S93 W3 on clean Stage-2 PASS-AND S93 W3-6" in reread  # (local)
    hdr_ok = "### §VII.AV.STATE-PROJ — Cell-IV STATE-PROJ K-Window Log-Derivative Sub-Slot (STAGE-3-PERMANENT" in reread  # (local)
    status_ok = "**Status**: STAGE-3-PERMANENT per `.claude/rules/joint-theorem-promotion.md` 4-stage upgrade pathway. STAGE-1 split-landed S93 W3-1" in reread  # (local)
    # OP-PROJ still STAGE-1-CANDIDATE (header + status untouched)
    op_proj_header_intact = "### §VII.AV.OP-PROJ — Cell-II OP-PROJ Trace-Residue Sub-Slot (S93 W3-1" in reread  # (local)
    op_proj_status_stage1 = "**Status**: STAGE-1-CANDIDATE per `.claude/rules/joint-theorem-promotion.md` 4-stage pathway. Split from the single §VII.AV slot by S93 W3-1" in reread  # (local)

    print()
    print(f"VERIFY STATE-PROJ index STAGE-3-PERMANENT : {idx_ok}")
    print(f"VERIFY STATE-PROJ header STAGE-3-PERMANENT: {hdr_ok}")
    print(f"VERIFY STATE-PROJ Status STAGE-3-PERMANENT: {status_ok}")
    print(f"VERIFY OP-PROJ header intact (Cell-II)    : {op_proj_header_intact}")
    print(f"VERIFY OP-PROJ Status stays STAGE-1-CAND  : {op_proj_status_stage1}")

    all_ok = idx_ok and hdr_ok and status_ok and op_proj_header_intact and op_proj_status_stage1  # (local)
    verdict = "PASS" if all_ok else "FAIL"  # (local)
    value = (  # (local)
        f"VII-AV-STATE-PROJ_STAGE-3-PERMANENT_flip=PASS_on_W3-6_Stage-2_clean_PASS-AND_"
        f"audit={W3_6_AUDIT_SHA[:16]}_idx={idx_ok}_hdr={hdr_ok}_status={status_ok}_"
        f"OP-PROJ_stays_STAGE-1-CANDIDATE={op_proj_status_stage1}_"
        f"ordinal_NOT_asserted_AU_AW_collision_CF=CF-S94-STAGE-3-ORDINAL-COLLISION-AU-AW"
        if all_ok else "VII-AV-STATE-PROJ_STAGE-3-flip_verify_FAILED"
    )

    # dual-SHA: content over the flipped registry section (3 markers); audit over
    # the input-pin map + W3-6 PASS sha + per-gate identity keys.
    section_marker = STATUS_NEW  # (local) the largest flipped block
    h_content = hashlib.sha256()  # (local)
    h_content.update(section_marker.encode("utf-8"))
    content_sha = h_content.hexdigest()  # (local)
    pins = {  # (local)
        "registry": sha256_of(REGISTRY),
        "w3_6_verdict_file": sha256_of(VERDICT_TXT),
        "lockfile": sha256_of(PROJECT_ROOT / "sessions" / "framework" / "s93-slot-pre-allocation-lockfile.md"),
    }
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(json.dumps(dict(sorted(pins.items())), sort_keys=True).encode("utf-8"))
    h_audit.update(f"{W3_6_AUDIT_SHA}|{GATE_ID}|{SCHEME}|{CONVENTION}|{verdict}".encode("utf-8"))
    audit_sha = h_audit.hexdigest()  # (local)

    emit_session_synthesis_line(audit_sha, content_sha, verdict, value)
    JSON_PATH.write_text(json.dumps({
        "gate_id": GATE_ID, "verdict": verdict, "value": value,
        "scheme": SCHEME, "convention": CONVENTION, "L_max": L_MAX,
        "audit_sha256": audit_sha, "content_sha256": content_sha,
        "w3_6_stage_2_pass_and_audit_sha256": W3_6_AUDIT_SHA,
        "state_proj_stage_3_permanent": all_ok,
        "op_proj_stays_stage_1_candidate": op_proj_status_stage1,
        "ordinal_assertion": "NOT-ASSERTED (pre-existing AU/AW '#3' collision; CF-S94-STAGE-3-ORDINAL-COLLISION-AU-AW)",
        "stage_3_set_joined": ["§VII.AH (FIRST)", "§VII.U.2 Var_a (SECOND)", "§VII.AU.OP-PROJ", "§VII.AW.OP-PROJ"],
    }, indent=2), encoding="utf-8")

    print()
    print(f"VERDICT: {verdict} (session-synthesis Stage-3 tag-flip; W3-6 line unchanged)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
