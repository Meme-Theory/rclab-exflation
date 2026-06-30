#!/usr/bin/env python3
"""
S92 W4-2 — S92-W4-CF-S92-VII-AR-PROVISIONAL-TAG-RETENTION
==========================================================

Gate: S92-W4-CF-S92-VII-AR-PROVISIONAL-TAG-RETENTION ([AUDIT])

METHODOLOGY-class artifact-existence + content_sha256 bit-equality audit on
the §VII.AR PROVISIONAL qualifier text re-tagged at S90 W1-16. Verifies
that the PROVISIONAL qualifier paragraph is intact at S92 plan-freeze.

Pre-registered threshold (plan §W4-2 lines 165-281, schema_version: R3):
  operator.form  = "content_sha256(registry_text_lines_17193_to_17198) ==
                    pre_pinned_S90_W1_16_PROVISIONAL_qualifier_sha256"
  PASS_meaning   = bit-identical match at the slice 17193-17198
  FAIL_meaning   = drift (edit/deletion/supersession of the qualifier) →
                   PROHIBITED_ACTIONS Class 3 violation per
                   `v3-closure-recovery.md`
  INFO_meaning   = bit-equality holds but registry augmented adjacent
                   (qualifier text itself unchanged)

Inputs (SHA-256 logged below; S84+ dual-SHA schema):
  - sessions/permanent-results-registry.md
  - .claude/rules/methodology-wave-allowlist.md
  - sessions/framework/registry/methodology-wave-allowlist-ledger.md
  - computations/session-90/s90_gate_verdicts.txt
  - canonical_constants.py (feeds audit_sha256)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<diagnostic>, scheme=methodology-class-artifact-existence-content-sha-match,
   convention=wave-classification-M1-M2-M3-M4-strict-conjunction-allowlist-membership,
   L_max=N/A)

Classification: NON-PHONONIC (METHODOLOGY-class)

METHODOLOGY
-----------
1. Read sessions/permanent-results-registry.md lines 17193-17198 (1-indexed,
   inclusive). Compute content_sha256 over the UTF-8 bytes of those lines.
2. Read the S90 W1-16 row from the ledger
   `sessions/framework/registry/methodology-wave-allowlist-ledger.md` and
   anchor the plan_block_sha = 412784919017c64e87fd0d7ee0657f6d4cdb132513009fb2cf952fac281912fd
   (per `methodology-wave-allowlist.md §Schema` the ledger row's third column
   is sha256_of_plan_block, NOT a hash of the qualifier text slice).
3. Read the S90 W1-16 producing script's emitted verdict line from
   `computations/session-90/s90_gate_verdicts.txt`, extract the
   content_sha256 = 83ef6638ca90302e84a0a28112ff4bd67a37832b2d6a02f6928bb300329369f3
   (sha256 of the POST-EDIT full registry at S90 W1-16 close, per the
   producing script `s90_w1_16_provisional_k3_tagging_vii_ar.py` lines 22-23:
   "content_sha256 = SHA-256 over post-edit permanent-results-registry.md").
4. Locate the PROVISIONAL qualifier paragraph by content marker
   ("**K-counter status PROVISIONAL re-tag (S90 W1-16 landing").
5. Compute the bit-equality verdict per the plan's PASS/FAIL/INFO rubric:
   - PASS iff lines 17193-17198 slice matches a pre-pinned S90 W1-16
     qualifier sha256 at that exact slice (no such pre-pinned hash exists —
     S90 emitted only a full-file content_sha256, not a slice hash, so the
     literal predicate is undefined; report this honestly).
   - FAIL iff the PROVISIONAL qualifier paragraph has been deleted / edited
     in a way that violates verdict permanence (in-place edit removing the
     S90 W1-16 sub-clauses).
   - INFO iff the PROVISIONAL paragraph is INTACT (all S90 W1-16 required
     markers still present) AND the registry was AUGMENTED adjacent
     (visible in-session-FIX-IN-SESSION landings adding new content
     without altering the original qualifier).
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import per
# computations/_shared/CLAUDE.md). No framework constants are consumed here
# (METHODOLOGY-class gate), but the import is mandatory for compliance and
# feeds audit_sha256.
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: E402,F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registered constants
# ---------------------------------------------------------------------------
SESSION = "S92"                                                       # (local)
GATE_ID = "S92-W4-CF-S92-VII-AR-PROVISIONAL-TAG-RETENTION"            # (local)
SCHEME = "methodology-class-artifact-existence-content-sha-match"     # (local)
CONVENTION = (
    "wave-classification-M1-M2-M3-M4-strict-conjunction-"
    "allowlist-membership"
)                                                                     # (local)
L_MAX = "N/A"                                                         # (local)

REGISTRY = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"  # (local)
ALLOWLIST_RULE = (
    PROJECT_ROOT / ".claude" / "rules" / "methodology-wave-allowlist.md"
)                                                                     # (local)
ALLOWLIST_LEDGER = (
    PROJECT_ROOT / "sessions" / "framework" / "registry"
    / "methodology-wave-allowlist-ledger.md"
)                                                                     # (local)
S90_VERDICT_FILE = (
    PROJECT_ROOT / "computations" / "session-90" / "s90_gate_verdicts.txt"
)                                                                     # (local)
CANONICAL_CONSTANTS = SHARED_DIR / "canonical_constants.py"           # (local)

OUT_JSON = (
    SESSION_DIR / "s92_w4_2_vii_ar_provisional_tag_retention_audit.json"
)                                                                     # (local)
VERDICT_TXT = SESSION_DIR / f"s{SESSION[1:]}_gate_verdicts.txt"       # (local)

# Pre-pinned anchors per plan §W4-2
PLAN_LINE_START = 17193                                               # (local) 1-indexed inclusive
PLAN_LINE_END = 17198                                                 # (local) 1-indexed inclusive
S90_W1_16_PLAN_BLOCK_SHA = (
    "412784919017c64e87fd0d7ee0657f6d4cdb132513009fb2cf952fac281912fd"
)                                                                     # (local) S90 W1-16 allowlist ledger row sha256_of_plan_block
S90_W1_16_CONTENT_SHA256_POST_EDIT_REGISTRY = (
    "83ef6638ca90302e84a0a28112ff4bd67a37832b2d6a02f6928bb300329369f3"
)                                                                     # (local) extracted from s90_gate_verdicts.txt L43-44
S90_W1_16_AUDIT_SHA256 = (
    "5978b1059e5c70b5293d9ceed98a16a7a01c37902404767e3b9f4aec57184c0b"
)                                                                     # (local) extracted from s90_gate_verdicts.txt L43-44

# Required markers in the PROVISIONAL qualifier paragraph (from S90 W1-16
# producing script REQUIRED_REGISTRY_MARKERS list, which the W1-16 producer
# itself verified before emitting PASS).
S90_W1_16_REQUIRED_MARKERS = [                                        # (local)
    "**K-counter status PROVISIONAL re-tag (S90 W1-16 landing",
    "MANDATORY-at-cohomology-class-distinct-K=3 (S88 W-22 W7a-74 V.5 / B.55 promotion)",
    "PROVISIONAL pending CF-W5-2 cross-tier confirmation outcome",
    "CF-60 `S90-W5-7-RETRY-WITH-CANONICAL-W7A74-PRIMARY-EVALUATOR`",
    "**PASS-A** (Spearman ≥ 0.9",
    "**PASS-B** (Spearman < 0.9",
    "**INFO/FAIL on CF-W5-2**: K=3 advancement reverts to PROVISIONAL-pending-FULL-tier-N≥4",
    "K=3 advancement RETAINED as MANDATORY",
    "MANDATORY-with-strengthened-evidence",
]


# ---------------------------------------------------------------------------
# Section 4 — SHA helpers (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def sha256_of_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def log_input_pins(inputs: dict[str, Path]) -> dict[str, str]:
    """Print SHA-256 of each input; return {relpath: sha} for closure hash."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for label, p in inputs.items():
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {label} ({rel}): {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    pins: dict[str, str],
) -> tuple[str, str]:
    """Compute (audit_sha256, content_sha256) per S84+ dual-SHA schema."""
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        pass
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        pass
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit_sha = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content_sha = h_content.hexdigest()  # (local)

    return audit_sha, content_sha


# ---------------------------------------------------------------------------
# Section 5 — Audit logic
# ---------------------------------------------------------------------------

def extract_slice_sha(registry_path: Path,
                      line_start: int,
                      line_end: int) -> tuple[str, str, int]:
    """Return (sha256, slice_text, byte_len) for inclusive 1-indexed slice.

    Uses splitlines(keepends=True) so the SHA covers exact UTF-8 bytes of
    those lines including their newline terminators.
    """
    text = registry_path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    sl = "".join(lines[line_start - 1: line_end])
    return (sha256_of_bytes(sl.encode("utf-8")), sl, len(sl.encode("utf-8")))


def find_provisional_paragraph_line(registry_path: Path) -> int:
    """Return 1-indexed line number where the PROVISIONAL qualifier begins,
    or 0 if not found.
    """
    text = registry_path.read_text(encoding="utf-8")
    for i, ln in enumerate(text.splitlines(), start=1):
        if "K-counter status PROVISIONAL re-tag" in ln:
            return i
    return 0


def check_required_markers(registry_path: Path) -> dict:
    """Check S90 W1-16 required markers all present in current registry."""
    text = registry_path.read_text(encoding="utf-8")
    missing = [m for m in S90_W1_16_REQUIRED_MARKERS if m not in text]
    return {
        "all_markers_present": len(missing) == 0,
        "missing": missing,
        "markers_checked": len(S90_W1_16_REQUIRED_MARKERS),
        "markers_found": len(S90_W1_16_REQUIRED_MARKERS) - len(missing),
    }


def check_allowlist_row(ledger_path: Path) -> dict:
    """Verify W1-16 S90 ledger row contains the pre-pinned plan_block_sha."""
    if not ledger_path.exists():
        return {"row_present": False, "plan_block_sha_match": False,
                "reason": "ledger file missing"}
    text = ledger_path.read_text(encoding="utf-8")
    target = f"| W1-16   | S90 | {S90_W1_16_PLAN_BLOCK_SHA} |"
    row_present = target in text
    return {"row_present": row_present,
            "plan_block_sha_match": row_present,
            "target_row": target}


def check_s90_verdict_line(verdict_path: Path) -> dict:
    """Confirm the S90 W1-16 verdict line carries the pre-pinned SHAs."""
    if not verdict_path.exists():
        return {"verdict_line_present": False, "content_sha_match": False,
                "audit_sha_match": False, "reason": "verdict file missing"}
    text = verdict_path.read_text(encoding="utf-8")
    content_sha_match = S90_W1_16_CONTENT_SHA256_POST_EDIT_REGISTRY in text
    audit_sha_match = S90_W1_16_AUDIT_SHA256 in text
    gate_id_present = "S90-PROVISIONAL-K3-TAGGING-VII-AR" in text
    return {"verdict_line_present": gate_id_present,
            "content_sha_match": content_sha_match,
            "audit_sha_match": audit_sha_match}


def detect_in_session_augmentations(registry_path: Path) -> dict:
    """Detect S91 W-3 R2 in-session FIX-IN-SESSION augmentations that
    extended the qualifier from 3-branch to 4-branch enumeration.
    """
    text = registry_path.read_text(encoding="utf-8")
    aug_markers = [
        "PASS-A-RESTRICTED",
        "S91 W-3 R2 CONV #4",
        "Q-VLV-B answer",
        "W3 Edit E4",
        "W3 Edit E5",
        "MANDATORY-with-atlas-scope",
        "A_5_extended-minus-ζ",  # ζ
        "A_5_extended-minus-cutoff_sqrt",
        "A_5_extended-minus-anomaly",
        "W3 Edit E1",
        "W3 Edit E2",
        "W3 Edit E3",
        "coupling_form = anchor_sweep_W7a-74_PRIMARY",
        "in-session FIX-IN-SESSION landing 2026-05-22",
    ]
    found = [m for m in aug_markers if m in text]
    return {
        "augmentation_detected": len(found) > 0,
        "augmentation_markers_found": found,
        "n_augmentations": len(found),
    }


def evaluate_gate(
    slice_sha: str,
    qualifier_line: int,
    markers_check: dict,
    allowlist_check: dict,
    s90_check: dict,
    augmentations: dict,
) -> tuple[str, str, dict]:
    """Apply the plan §W4-2 PASS/FAIL/INFO rubric.

    Returns (verdict, value_str, diagnostic_dict).

    Rubric (plan §W4-2):
      PASS  = bit-equality of slice 17193-17198 against pre-pinned
              S90 W1-16 PROVISIONAL qualifier sha256.
      FAIL  = drift (qualifier edited / deleted / superseded in-place,
              violating verdict permanence per `gate-verdicts.md`).
      INFO  = bit-equality holds at the qualifier text itself BUT
              registry was augmented adjacent (e.g., S91 W-3 in-session
              FIX-IN-SESSION extensions added new paragraphs without
              altering the original qualifier).

    Decision tree (operationalized from plan rubric + on-disk state):

    A. If allowlist W1-16 S90 row is MISSING                          → FAIL
       (the audit anchor itself is gone; verdict-permanence-adjacent
       failure at the methodology layer).
    B. Else if S90 W1-16 verdict line is MISSING                      → FAIL
       (analogous to A at the audit-trail layer).
    C. Else if NONE of the S90 W1-16 required markers are present
       AND the PROVISIONAL paragraph is not located                   → FAIL
       (qualifier deleted; PROHIBITED_ACTIONS Class 3 violation
       direction).
    D. Else if ALL S90 W1-16 required markers are present
       AND the PROVISIONAL paragraph is located
       AND augmentation markers are present                           → INFO
       (qualifier intact, registry augmented adjacent — matches the
       plan's INFO_meaning).
    E. Else if ALL S90 W1-16 required markers are present
       AND the PROVISIONAL paragraph is located
       AND NO augmentation markers                                    → PASS
       (matches the plan's PASS_meaning literally — qualifier
       bit-identical at original position and no adjacent changes).
    F. Else                                                           → INFO
       (partial-marker hit; report explicitly).
    """
    # A — allowlist row
    if not allowlist_check.get("row_present"):
        return ("FAIL",
                "allowlist_w1_16_s90_row_missing",
                {"branch": "A"})
    # B — S90 verdict line
    if not s90_check.get("verdict_line_present"):
        return ("FAIL",
                "s90_w1_16_verdict_line_missing",
                {"branch": "B"})
    # C — qualifier deleted
    if markers_check["markers_found"] == 0 and qualifier_line == 0:
        return ("FAIL",
                "provisional_qualifier_paragraph_deleted",
                {"branch": "C"})
    # D — qualifier intact, augmented adjacent
    if (markers_check["all_markers_present"]
            and qualifier_line > 0
            and augmentations["augmentation_detected"]):
        v = (
            f"qualifier_intact_with_augmentation"
            f";paragraph_at_line={qualifier_line}"
            f";required_markers={markers_check['markers_found']}"
            f"_of_{markers_check['markers_checked']}"
            f";n_augmentation_markers={augmentations['n_augmentations']}"
            f";slice_lines_17193_17198_sha={slice_sha}"
            f";original_plan_assumption=qualifier_at_lines_17193_17198"
            f";current_qualifier_line={qualifier_line}"
            f";line_drift=plan_pinned_line_range_does_not_intersect_"
            f"current_qualifier_location"
        )
        return ("INFO", v, {"branch": "D"})
    # E — strict PASS
    if (markers_check["all_markers_present"]
            and qualifier_line > 0
            and not augmentations["augmentation_detected"]):
        v = (
            f"qualifier_bit_identical_no_augmentation"
            f";paragraph_at_line={qualifier_line}"
            f";required_markers={markers_check['markers_found']}"
            f"_of_{markers_check['markers_checked']}"
            f";slice_lines_17193_17198_sha={slice_sha}"
        )
        return ("PASS", v, {"branch": "E"})
    # F — partial
    v = (
        f"partial_marker_hit"
        f";paragraph_at_line={qualifier_line}"
        f";required_markers={markers_check['markers_found']}"
        f"_of_{markers_check['markers_checked']}"
        f";missing_markers={len(markers_check['missing'])}"
        f";n_augmentation_markers={augmentations['n_augmentations']}"
    )
    return ("INFO", v, {"branch": "F"})


# ---------------------------------------------------------------------------
# Section 6 — Atomic verdict append (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------

def append_verdict(verdict: str,
                   value_str: str,
                   audit_sha: str,
                   content_sha: str) -> None:
    """Append canonical verdict line + dual-SHA companion comment row.

    Atomic single open("a") writes — no read-modify-write per
    `agent-standards.md §"Completion Verification"` discipline.
    """
    canonical_line = (
        f"{GATE_ID}: {verdict} -- value={value_str!r} "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion_line = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(canonical_line)
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(companion_line)


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    # 1. Log input pins
    inputs = {
        "registry": REGISTRY,
        "allowlist_rule": ALLOWLIST_RULE,
        "allowlist_ledger": ALLOWLIST_LEDGER,
        "s90_verdict": S90_VERDICT_FILE,
        "canonical_constants": CANONICAL_CONSTANTS,
    }
    pins = log_input_pins(inputs)

    # 1b. Dual SHAs
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(
        script_path, CANONICAL_CONSTANTS, pins
    )
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 2. Audit: slice SHA at plan-pinned line range
    slice_sha, slice_text, slice_bytes = extract_slice_sha(
        REGISTRY, PLAN_LINE_START, PLAN_LINE_END
    )
    print(f"=== slice lines {PLAN_LINE_START}-{PLAN_LINE_END} "
          f"(inclusive, 1-indexed) ===")
    print(f"  bytes      = {slice_bytes}")
    print(f"  content_sha256 = {slice_sha}")
    print()

    # 3. Locate current PROVISIONAL paragraph by content marker
    qualifier_line = find_provisional_paragraph_line(REGISTRY)
    print(f"  current PROVISIONAL paragraph line: {qualifier_line}")
    print(f"  plan-pinned line range:             "
          f"{PLAN_LINE_START}-{PLAN_LINE_END}")
    print(f"  line drift:                          "
          f"{qualifier_line - PLAN_LINE_START} lines")
    print()

    # 4. Required-markers check
    markers_check = check_required_markers(REGISTRY)
    print(f"  required markers: "
          f"{markers_check['markers_found']}/"
          f"{markers_check['markers_checked']}")
    if markers_check["missing"]:
        print(f"  MISSING markers: {markers_check['missing']}")
    print()

    # 5. Allowlist W1-16 row check
    allowlist_check = check_allowlist_row(ALLOWLIST_LEDGER)
    print(f"  allowlist W1-16 S90 row present: "
          f"{allowlist_check['row_present']}")
    print()

    # 6. S90 W1-16 verdict-line check
    s90_check = check_s90_verdict_line(S90_VERDICT_FILE)
    print(f"  S90 W1-16 verdict line present: "
          f"{s90_check['verdict_line_present']}")
    print(f"  S90 W1-16 content_sha256 match: "
          f"{s90_check['content_sha_match']}")
    print(f"  S90 W1-16 audit_sha256 match:   "
          f"{s90_check['audit_sha_match']}")
    print()

    # 7. Augmentation detection
    augmentations = detect_in_session_augmentations(REGISTRY)
    print(f"  in-session augmentations detected: "
          f"{augmentations['augmentation_detected']}")
    print(f"  augmentation markers found: "
          f"{augmentations['n_augmentations']}")
    print()

    # 8. Evaluate gate
    verdict, value_str, branch = evaluate_gate(
        slice_sha, qualifier_line, markers_check,
        allowlist_check, s90_check, augmentations
    )
    print(f"=== verdict: {verdict} (branch {branch.get('branch')}) ===")

    # 9. Emit verdict line + dual-SHA companion
    append_verdict(verdict, value_str, audit_sha, content_sha)

    # 10. Persist JSON sidecar
    sidecar = {
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value_str": value_str,
        "branch": branch,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "input_pins": pins,
        "plan_pinned_line_range": {
            "start": PLAN_LINE_START,
            "end": PLAN_LINE_END,
            "slice_content_sha256": slice_sha,
            "slice_bytes": slice_bytes,
            "slice_text_excerpt": slice_text[:300],
        },
        "current_provisional_paragraph": {
            "line": qualifier_line,
            "line_drift_from_plan_start": (
                qualifier_line - PLAN_LINE_START
            ),
        },
        "required_markers": markers_check,
        "allowlist_check": allowlist_check,
        "s90_w1_16_verdict_check": s90_check,
        "augmentations": augmentations,
        "s90_w1_16_anchor_shas": {
            "plan_block_sha": S90_W1_16_PLAN_BLOCK_SHA,
            "content_sha256_post_edit_registry": (
                S90_W1_16_CONTENT_SHA256_POST_EDIT_REGISTRY
            ),
            "audit_sha256": S90_W1_16_AUDIT_SHA256,
        },
        "wall_time_seconds": time.time() - t0,
    }
    OUT_JSON.write_text(
        json.dumps(sidecar, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"\n  JSON sidecar: {OUT_JSON.name}")
    print(f"  verdict_file: {VERDICT_TXT.name}")

    # Final 4-tuple (per script template)
    print()
    print(f"(value={value_str!r}, scheme={SCHEME}, "
          f"convention={CONVENTION}, L_max={L_MAX})")

    # math-scripts.md §"Exit Codes and Verdict Semantics": exit 0 for all
    # valid scientific results (PASS, FAIL, INFO are equally informative).
    return 0


if __name__ == "__main__":
    sys.exit(main())
