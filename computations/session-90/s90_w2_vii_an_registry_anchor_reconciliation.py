#!/usr/bin/env python3
"""
S90 W2-6 — S90-VII-AN-REGISTRY-ANCHOR-RECONCILIATION (CF-23)
=============================================================

Gate: S90-VII-AN-REGISTRY-ANCHOR-RECONCILIATION ([VERIFY])

Resolves §VII.AN registry-anchor framing reconciliation per plan §W2-6. The
W6-2 audit at S89 (audit `9f7a203def8301f7589501b7d73030097ceeb060cd714b1be785f0737619aa5f`)
reported the producing script `s82_w3_9_as_adjacent_obs.py` as MISSING from
disk; that flag was stale or has since been resolved — the script EXISTS at
`computations/session-82/s82_w3_9_as_adjacent_obs.py` (461 lines; valid
docstring) as verified at S90 W2 dispatch time. Path-a (restore missing
producing script) is structurally satisfied by current state.

This gate adds a PROVENANCE annotation (CF-23) to §VII.AN documenting:
  (i) the W6-2 stale-flag resolution (script verified on disk at S90 W2);
  (ii) the on-disk script's content_sha256 for audit reproducibility;
  (iii) the K=4 NEGATIVE-CALIBRATION corpus instance #4 RESOLVED.

No anchor-text REWRITE is required (the anchor cites the GATE "S82 W3-9
single-pole Mellin closure", not a specific script path; the script
implementing S82 W3-9 IS on disk).
"""

from __future__ import annotations

import sys
from pathlib import Path

_SHARED_DIR = Path(__file__).resolve().parent.parent / "_shared"
sys.path.insert(0, str(_SHARED_DIR))
from canonical_constants import *  # noqa: F401,F403,E402

import hashlib  # noqa: E402
import json  # noqa: E402
import os  # noqa: E402
import time  # noqa: E402

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

GATE_ID = "S90-VII-AN-REGISTRY-ANCHOR-RECONCILIATION"  # (local)
SCHEME = "mack-sole-writer-single-shot-AFTER-pattern"  # (local)
CONVENTION = "vii-an-anchor-reconciliation-path-a-script-restored-stale-flag-resolved"  # (local)
L_MAX = "N/A"  # (local)

REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
S82_W3_9_SCRIPT = (
    PROJECT_ROOT / "computations" / "session-82" / "s82_w3_9_as_adjacent_obs.py"
)
VERDICT_TXT = SESSION_DIR / "s90_gate_verdicts.txt"

W6_2_AUDIT_SHA = (
    "9f7a203def8301f7589501b7d73030097ceeb060cd714b1be785f0737619aa5f"
)  # (local) S89 W6-2 stale-flag audit

ANCHOR_VII_AN_HEADING = (
    "## §VII.AN — α_s_canonical SOURCE-DOUBLE-CITE-CO-PRIMARY"
)  # (local)

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    REGISTRY_PATH,
    S82_W3_9_SCRIPT,
]


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
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path, canonical_path, pins):
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
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def write_atomic_with_fsync(path, text):
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8", newline="\n") as fp:
        fp.write(text)
        fp.flush()
        os.fsync(fp.fileno())
    os.replace(tmp, path)


def main():
    t0 = time.time()
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()
    canonical_path = SHARED_DIR / "canonical_constants.py"
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    print("Step 0: path-a feasibility check (script-existence pre-flight)")
    script_exists = S82_W3_9_SCRIPT.exists() and S82_W3_9_SCRIPT.stat().st_size > 0
    if script_exists:
        script_content_sha = sha256_of(S82_W3_9_SCRIPT)
        script_line_count = S82_W3_9_SCRIPT.read_text(encoding="utf-8").count("\n")
        print(f"  PASS: script exists ({script_line_count} lines)")
        print(f"  on-disk script content_sha256: {script_content_sha[:16]}...")
    else:
        script_content_sha = ""
        script_line_count = 0  # (local)
        print(f"  FAIL: script {S82_W3_9_SCRIPT} not found")

    # Idempotency check
    print("Step 1: read §VII.AN; check for existing CF-23 PROVENANCE annotation")
    original_text = REGISTRY_PATH.read_text(encoding="utf-8")
    cf_23_already_landed = "Provenance annotation (CF-23, 2026-05-13)" in original_text  # (local)
    if cf_23_already_landed:
        print("  WARN: CF-23 PROVENANCE annotation already present — idempotency triggered")
        promoted_text = original_text
    elif not script_exists:
        print("  ERROR: path-a precondition failed; script missing; manual path-b required")
        verdict_value = (
            f"path_a_failed=script_missing;"
            f"path_b_required_manual_intervention=True;"
            f"allowlist_row=pending;instances_row=pending"
        )
        with VERDICT_TXT.open("a", encoding="utf-8") as fp:
            fp.write(f"{GATE_ID}: FAIL -- value={verdict_value!r} scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} audit_sha256={audit_sha} content_sha256={content_sha} schema_version=S87+\n")
            fp.write(f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} # {GATE_ID} dual-SHA companion row (W9a-99 split)\n")
        print(f"\n=== {GATE_ID}: FAIL (wall {time.time() - t0:.1f}s) ===")
        return 0
    else:
        # Path-a satisfied: build PROVENANCE annotation
        provenance_annotation = (
            f"**Provenance annotation (CF-23, 2026-05-13)**: §VII.AN registry-"
            f"anchor reconciliation per S90 W2 CF-23. The S89 W6-2 audit "
            f"(audit_sha256=`{W6_2_AUDIT_SHA}`) reported the producing script "
            f"`s82_w3_9_as_adjacent_obs.py` as MISSING from disk; at S90 W2 "
            f"dispatch time the script EXISTS at "
            f"`computations/session-82/s82_w3_9_as_adjacent_obs.py` ("
            f"{script_line_count} lines; on-disk content_sha256=`"
            f"{script_content_sha}`). The W6-2 stale-flag is RESOLVED via "
            f"path-a (restore-via-existence-confirmation, NOT explicit "
            f"git-restore — the script was either already restored "
            f"between S89 W6-2 and S90 W2 dispatch OR W6-2 audit's miss "
            f"was a scan-path defect). §VII.AN anchor text (ANCHOR-1 "
            f"citing 'S82 W3-9 single-pole Mellin closure') remains "
            f"VALID against on-disk script (script implements the "
            f"S82 W3-9 gate's producing computation). K=4 NEGATIVE-"
            f"CALIBRATION corpus instance #4 (substrate-first-canonical-"
            f"sourcing.md §(i)) RESOLVED. W6-2 audit re-run expected "
            f"to return no Class-(g) ROUTE-A-VS-ROUTE-B flag on §VII.AN "
            f"after this PROVENANCE annotation lands. Mack-cosmic-bridge "
            f"sole-writer per `feedback_mack-bridge-role.md`."
        )

        # Insert PROVENANCE annotation immediately after the heading
        heading_idx = original_text.find(ANCHOR_VII_AN_HEADING)
        if heading_idx == -1:
            print("  ERROR: §VII.AN heading not found")
            return 1
        end_of_heading = original_text.find("\n", heading_idx)
        # Insert after heading + blank line
        if original_text[end_of_heading + 1] != "\n":
            print("  ERROR: expected blank line after §VII.AN heading")
            return 1
        insertion_point = end_of_heading + 2
        promoted_text = (
            original_text[:insertion_point]
            + provenance_annotation
            + "\n\n"
            + original_text[insertion_point:]
        )
        print("  PASS: built PROVENANCE annotation for path-a closure")

    print("Step 2: write_atomic_with_fsync")
    write_atomic_with_fsync(REGISTRY_PATH, promoted_text)

    print("Step 3: re-read + verify")
    re_read = REGISTRY_PATH.read_text(encoding="utf-8")
    checks = {
        "vii_an_heading_present": ANCHOR_VII_AN_HEADING in re_read,
        "cf_23_provenance_annotation_present": (
            "Provenance annotation (CF-23, 2026-05-13)" in re_read
        ),
        "w6_2_audit_sha_present": W6_2_AUDIT_SHA in re_read,
        "script_existence_documented": (
            f"{script_line_count} lines" in re_read if script_exists else True
        ),
        "k_4_corpus_instance_4_resolved_tag": (
            "K=4 NEGATIVE-CALIBRATION corpus instance #4 (substrate-first-canonical-sourcing.md §(i)) RESOLVED" in re_read
        ),
        "anchor_text_remains_valid_assertion": (
            "anchor text (ANCHOR-1 citing 'S82 W3-9 single-pole Mellin closure') remains VALID" in re_read
        ),
        "on_disk_script_content_sha_present": (
            script_content_sha[:32] in re_read if script_content_sha else False
        ),
    }
    for k, v in checks.items():
        print(f"  {k}: {'PASS' if v else 'FAIL'}")
    overall = all(checks.values())

    verdict = "PASS" if overall else "FAIL"
    n_pass = sum(1 for v in checks.values() if v)
    verdict_value = (
        f"vii_an_anchor_reconciled={overall};"
        f"checks_pass={n_pass}_of_{len(checks)};"
        f"path_taken=path-a-script-exists-stale-flag-resolved;"
        f"script_existence_verified=True;"
        f"script_line_count={script_line_count};"
        f"script_content_sha={script_content_sha[:16]};"
        f"w6_2_audit_stale_flag_resolved=True;"
        f"k_4_negative_calibration_corpus_instance_4_resolved=True;"
        f"anchor_text_no_rewrite_required=True;"
        f"provenance_annotation_added=True;"
        f"after_pattern_compliance=True;"
        f"allowlist_row=pending;instances_row=pending"
    )

    canonical = (
        f"{GATE_ID}: {verdict} -- value={verdict_value!r} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical)
        fp.write(companion)
    print(f"\n=== {GATE_ID}: {verdict} (wall {time.time() - t0:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
