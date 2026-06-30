#!/usr/bin/env python3
"""
S90 W2-3 — S90-VII-AH-STAGE-3-PERMANENT-PROMOTION (CF-20)
=========================================================

Gate: S90-VII-AH-STAGE-3-PERMANENT-PROMOTION ([VERIFY])

Pre-registered threshold (per plan §W2-3 §9):
  PASS iff (a) §VII.AH theorem-name line contains STAGE-3-PERMANENT AND NOT
                STAGE-1-CANDIDATE (literal grep on the heading line only)
       AND (b) Stage-2 PASS provenance annotation present with 4fcd7d29… SHA fragment
       AND (c) joint-theorem-promotion.md K=3 calibration row added with §VII.AH
       AND (d) joint-theorem-promotion.md Status line MANDATORY at K=3
  FAIL iff any of (a)-(d) absent post-write.

Inputs (S84+ dual-SHA schema):
  - sessions/permanent-results-registry.md (pre-edit)
  - .claude/rules/joint-theorem-promotion.md (pre-edit)
  - computations/session-89/s89_gate_verdicts.txt (W4-7 audit 4fcd7d29…)
  - script bytes + canonical_constants.py

Output 4-tuple (per plan §W2-3 §8):
  (value=<bool>, scheme=mack-sole-writer-single-shot-AFTER-pattern,
   convention=joint-theorem-promotion-stage-3-permanent, L_max=N/A)

Classification: METHODOLOGY (§VII.AH STAGE-1-CANDIDATE → STAGE-3-PERMANENT
tag replacement + joint-theorem-promotion calibration corpus K=2 → K=3
advancement). First framework cross-axis joint theorem to reach
STAGE-3-PERMANENT eligibility per `joint-theorem-promotion.md` 4-stage pathway.

METHODOLOGY
-----------
Single-shot AFTER-pattern with TWO file targets:
  build_promotion_text_registry → build_promotion_text_rule_file
  → write_atomic_with_fsync (both files)
  → re_read + verify_section_matches (both files)
  → emit_verdict (exactly ONE canonical line)

DISCIPLINE
----------
- `from canonical_constants import *` (S34+ MANDATORY)
- Every local/intermediate tagged `# (local)`
- Idempotency-guarded on both files
- audit_sha256 + content_sha256 (S84+ dual-SHA)
- Gate verdict to s90_gate_verdicts.txt per `.claude/rules/gate-verdicts.md` S87+
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

_SHARED_DIR = Path(__file__).resolve().parent.parent / "_shared"
sys.path.insert(0, str(_SHARED_DIR))
from canonical_constants import *  # noqa: F401,F403,E402

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import os  # noqa: E402
import time  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S90"                                                # (local)
GATE_ID = "S90-VII-AH-STAGE-3-PERMANENT-PROMOTION"             # (local)
SCHEME = "mack-sole-writer-single-shot-AFTER-pattern"          # (local)
CONVENTION = "joint-theorem-promotion-stage-3-permanent"       # (local)
L_MAX = "N/A"                                                  # (local)

REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"  # (local)
RULE_PATH = (
    PROJECT_ROOT / ".claude" / "rules" / "joint-theorem-promotion.md"
)  # (local)
S89_VERDICTS_PATH = (
    PROJECT_ROOT / "computations" / "session-89" / "s89_gate_verdicts.txt"
)  # (local)
VERDICT_TXT = SESSION_DIR / "s90_gate_verdicts.txt"  # (local)

# S89 W4-7 Stage-2 PASS audit_sha256 (per plan §W2-3 §"Hard prerequisites";
# grep-verified at s89_gate_verdicts.txt:80)
W4_7_VII_AH_AUDIT_SHA = (
    "4fcd7d29af51c56d8c6620bc2c323970b96edc053e432232e680903d8926536a"
)  # (local)

# Anchor strings for the two file targets
ANCHOR_VII_AH_HEADING_OLD = (
    "## §VII.AH — Joint F_2-Class Path-(c) Theorem "
    "(lizzi+transit S86 W-9) (STAGE-1-CANDIDATE)"
)  # (local) heading line as it stands pre-edit
ANCHOR_VII_AH_HEADING_NEW = (
    "## §VII.AH — Joint F_2-Class Path-(c) Theorem "
    "(lizzi+transit S86 W-9) (STAGE-3-PERMANENT)"
)  # (local) heading line after promotion

# Stage-2 PASS provenance annotation (verbatim per plan §6 Step 1)
STAGE_2_PASS_ANNOTATION = (
    "**Stage-2 PASS** (S89 W4-7, audit_sha256="
    + W4_7_VII_AH_AUDIT_SHA
    + "): 8/8 structural-coherence + JOINT (c)+(d) clauses PASS-AND'd across "
    "connes-ncg-theorist (axis-A) + volovik-superfluid-universe-theorist (axis-B) "
    "at substrate-input-orthogonality structural ceiling. CF-20 S90 W2 "
    "STAGE-3-PERMANENT promotion."
)  # (local)

# joint-theorem-promotion.md K-counter table: anchor on the K=2 bullet line +
# anchor on the SUGGESTION at K=2 Status line. The K=3 bullet is INSERTED
# between K=2 line and the blank line that precedes "Audit-script extension queue".
ANCHOR_RULE_K2_BULLET_PREFIX = "- **K=2**: S89 W4-7 §VII.AH Stage-2 re-dispatch"  # (local)
NEW_K3_BULLET = (
    "- **K=3**: S90 W2 CF-20 §VII.AH STAGE-3-PERMANENT promotion event "
    "(CF-20 S90 W2 LANDED, 2026-05-13); FIRST framework cross-axis joint "
    "theorem to reach STAGE-3-PERMANENT eligibility via Stage-2 PASS at "
    "substrate-input-orthogonality structural ceiling (S89 W4-7 audit_sha256="
    + W4_7_VII_AH_AUDIT_SHA
    + "). K-counter advancement K=2 → K=3 triggers Status promotion "
    "SUGGESTION → MANDATORY per `feedback_rules-compensate-missing-structure.md` "
    "K-counter threshold."
)  # (local)

ANCHOR_RULE_STATUS_OLD = (
    "Status **SUGGESTION at K=2** (promotes to MANDATORY at K=3 "
    "distinct calibration instances)."
)  # (local)
ANCHOR_RULE_STATUS_NEW = (
    "Status **MANDATORY at K=3** (promoted S90 W2 CF-20, 2026-05-13; "
    "§VII.AH STAGE-3-PERMANENT advancement is the K=3 calibration "
    "instance — FIRST framework cross-axis joint theorem to reach "
    "STAGE-3-PERMANENT eligibility)."
)  # (local)

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    REGISTRY_PATH,
    RULE_PATH,
    S89_VERDICTS_PATH,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 dual-SHA closure
# ---------------------------------------------------------------------------

def sha256_of(path):
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path, canonical_path, pins):
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True,
    ).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — build_promotion_text (pure functions; one per file target)
# ---------------------------------------------------------------------------

def build_promotion_text_registry(original_text):
    """Pure: registry text → registry with §VII.AH STAGE-1-CANDIDATE tag
    replaced by STAGE-3-PERMANENT in the heading line + Stage-2 PASS
    annotation inserted immediately below the heading. Idempotent."""
    if ANCHOR_VII_AH_HEADING_NEW in original_text:
        return original_text  # already promoted; no-op
    if ANCHOR_VII_AH_HEADING_OLD not in original_text:
        raise ValueError(
            "§VII.AH STAGE-1-CANDIDATE heading anchor not found "
            "(may already be at STAGE-3-PERMANENT, or anchor drift)"
        )
    # Step 1: replace tag in heading line
    promoted = original_text.replace(
        ANCHOR_VII_AH_HEADING_OLD,
        ANCHOR_VII_AH_HEADING_NEW,
        1,  # replace ONLY the first occurrence (heading line)
    )  # (local)
    # Step 2: insert Stage-2 PASS annotation immediately below the heading
    # (after the heading's trailing blank line). Idempotency: skip if already present.
    if "**Stage-2 PASS** (S89 W4-7, audit_sha256=" + W4_7_VII_AH_AUDIT_SHA in promoted:
        return promoted  # annotation already present
    heading_idx = promoted.find(ANCHOR_VII_AH_HEADING_NEW)  # (local)
    end_of_heading = promoted.find("\n", heading_idx)  # (local)
    # Skip blank line; insert before the next non-blank content
    if promoted[end_of_heading + 1] != "\n":
        raise ValueError(
            "Expected blank line after §VII.AH heading; structure unexpected"
        )
    insertion_point = end_of_heading + 2  # (local)
    promoted = (
        promoted[:insertion_point]
        + STAGE_2_PASS_ANNOTATION
        + "\n\n"
        + promoted[insertion_point:]
    )
    return promoted


def build_promotion_text_rule_file(original_text):
    """Pure: rule-file text → rule-file with K=3 bullet inserted after K=2
    bullet + Status line replaced. Idempotent."""
    if ANCHOR_RULE_STATUS_NEW in original_text:
        return original_text  # already promoted; no-op
    # Insert K=3 bullet immediately after the K=2 bullet line
    if NEW_K3_BULLET not in original_text:
        # Find the K=2 bullet (single line in the source); locate its end-of-line
        k2_idx = original_text.find(ANCHOR_RULE_K2_BULLET_PREFIX)  # (local)
        if k2_idx == -1:
            raise ValueError(
                "K=2 bullet anchor not found in joint-theorem-promotion.md"
            )
        end_of_k2_line = original_text.find("\n", k2_idx)  # (local)
        if end_of_k2_line == -1:
            raise ValueError("K=2 line not terminated; structure unexpected")
        # Insert "\n" + K=3 bullet right after end-of-K=2-line
        promoted = (
            original_text[:end_of_k2_line + 1]
            + NEW_K3_BULLET
            + "\n"
            + original_text[end_of_k2_line + 1:]
        )  # (local)
    else:
        promoted = original_text
    # Replace Status line
    if ANCHOR_RULE_STATUS_OLD not in promoted:
        raise ValueError(
            "Status SUGGESTION-at-K=2 anchor not found "
            "in joint-theorem-promotion.md (drift detected)"
        )
    promoted = promoted.replace(
        ANCHOR_RULE_STATUS_OLD, ANCHOR_RULE_STATUS_NEW, 1,
    )  # (local)
    return promoted


# ---------------------------------------------------------------------------
# Section 6 — write_atomic_with_fsync
# ---------------------------------------------------------------------------

def write_atomic_with_fsync(path, text):
    tmp = path.with_suffix(path.suffix + ".tmp")  # (local)
    with tmp.open("w", encoding="utf-8", newline="\n") as fp:
        fp.write(text)
        fp.flush()
        os.fsync(fp.fileno())
    os.replace(tmp, path)


# ---------------------------------------------------------------------------
# Section 7 — re_read + verify_section_matches (both files)
# ---------------------------------------------------------------------------

def verify_section_matches(registry_text, rule_text):
    checks = {
        # Registry file: §VII.AH theorem-name line carries STAGE-3-PERMANENT
        "registry_vii_ah_heading_stage_3_present": (
            ANCHOR_VII_AH_HEADING_NEW in registry_text
        ),
        "registry_vii_ah_heading_stage_1_absent": (
            ANCHOR_VII_AH_HEADING_OLD not in registry_text
        ),
        "registry_stage_2_pass_annotation_present": (
            "**Stage-2 PASS** (S89 W4-7" in registry_text
            and W4_7_VII_AH_AUDIT_SHA in registry_text
        ),
        "registry_stage_2_pass_sha_fragment_present": (
            "4fcd7d29" in registry_text
        ),
        # Rule file: K=3 bullet present + Status MANDATORY
        "rule_file_k3_bullet_present": NEW_K3_BULLET in rule_text,
        "rule_file_k3_promotion_event_text": (
            "S90 W2 CF-20 §VII.AH STAGE-3-PERMANENT promotion event" in rule_text
        ),
        "rule_file_status_mandatory_at_k3": ANCHOR_RULE_STATUS_NEW in rule_text,
        "rule_file_status_suggestion_at_k2_absent": (
            ANCHOR_RULE_STATUS_OLD not in rule_text
        ),
    }
    overall = all(checks.values())  # (local)
    return overall, checks


# ---------------------------------------------------------------------------
# Section 8 — emit_verdict
# ---------------------------------------------------------------------------

def emit_verdict(verdict, value_str, audit_sha, content_sha):
    canonical = (
        f"{GATE_ID}: {verdict} -- value={value_str!r} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S87+\n"
    )  # (local)
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )  # (local)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical)
        fp.write(companion)


# ---------------------------------------------------------------------------
# Section 9 — Main
# ---------------------------------------------------------------------------

def main():
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    print("Step 1: build_promotion_text (pure functions; both files)")
    original_registry = REGISTRY_PATH.read_text(encoding="utf-8")  # (local)
    original_rule = RULE_PATH.read_text(encoding="utf-8")  # (local)
    try:
        promoted_registry = build_promotion_text_registry(original_registry)  # (local)
        promoted_rule = build_promotion_text_rule_file(original_rule)  # (local)
    except ValueError as e:
        print(f"  ERROR in build_promotion_text: {e}")
        verdict_value = f"build_FAILED;reason={e!s};allowlist_row=pending;instances_row=pending"  # (local)
        emit_verdict("FAIL", verdict_value, audit_sha, content_sha)
        print(f"\n=== {GATE_ID}: FAIL (wall {time.time() - t0:.1f}s) ===")
        return 0

    print("Step 2: write_atomic_with_fsync (registry + rule file)")
    write_atomic_with_fsync(REGISTRY_PATH, promoted_registry)
    write_atomic_with_fsync(RULE_PATH, promoted_rule)

    print("Step 3: re_read + verify_section_matches (both files)")
    re_read_registry = REGISTRY_PATH.read_text(encoding="utf-8")  # (local)
    re_read_rule = RULE_PATH.read_text(encoding="utf-8")  # (local)
    overall, checks = verify_section_matches(re_read_registry, re_read_rule)
    for k, v in checks.items():
        print(f"  {k}: {'PASS' if v else 'FAIL'}")

    print(f"Step 4: emit_verdict ({'PASS' if overall else 'FAIL'})")
    verdict = "PASS" if overall else "FAIL"  # (local)
    n_pass = sum(1 for v in checks.values() if v)  # (local)
    verdict_value = (
        f"vii_ah_stage_3_permanent_promoted={overall};"
        f"checks_pass={n_pass}_of_{len(checks)};"
        f"stage_2_pass_audit_sha={W4_7_VII_AH_AUDIT_SHA[:16]};"
        f"k_counter_advance=K2_to_K3;"
        f"k_counter_status=MANDATORY_at_K3;"
        f"first_cross_axis_joint_theorem_to_stage_3_permanent=True;"
        f"two_file_edit_atomic=permanent-results-registry.md_and_joint-theorem-promotion.md;"
        f"after_pattern_compliance=True;"
        f"allowlist_row=pending;instances_row=pending"
    )  # (local)
    emit_verdict(verdict, verdict_value, audit_sha, content_sha)

    tag = (
        f"(value={overall!r}, scheme={SCHEME}, "
        f"convention={CONVENTION}, L_max={L_MAX})"
    )  # (local)
    print(tag)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
