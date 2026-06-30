#!/usr/bin/env python3
"""
S90 W2-1 — S90-VII-AAU-VII-AV-WITHDRAWN-IN-FAVOR-OF-S90-LANDING-CLEANUP (CF-18)
==============================================================================

Gate: S90-VII-AAU-VII-AV-WITHDRAWN-IN-FAVOR-OF-S90-LANDING-CLEANUP ([VERIFY])

Pre-registered threshold:
  PASS iff all three header annotations present after atomic write:
    - §VII.AAU.OP-PROJ: **Status**: WITHDRAWN-IN-FAVOR-OF-S90-LANDING + c857179040b40224
    - §VII.AU.OP-PROJ: **Provenance annotation (CF-18)** + f1fae96aae6d401b
    - §VII.AV.OP-PROJ: **Status**: WITHDRAWN-IN-FAVOR-OF-S90-LANDING + cc18126581ddd9a1
  FAIL iff any of the three insertions missing post-write.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - sessions/permanent-results-registry.md (pre-edit content; feeds audit_sha256)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)
  - canonical_constants.py (feeds audit_sha256)
  - computations/session-89/s89_gate_verdicts.txt (W7c SHA cross-reference; feeds audit_sha256)

Output 4-tuple:
  (value=<bool>, scheme=mack-sole-writer-single-shot-AFTER-pattern,
   convention=registry-hygiene-cleanup, L_max=N/A)

Classification: METHODOLOGY (registry-text WITHDRAWN-IN-FAVOR-OF cleanup of
W7c three-emission supersedes chain; PASS predicate is artifact-existence-
with-substantive-content).

METHODOLOGY
-----------
Single-shot AFTER-pattern per `.claude/rules/registry-landing.md
§"Bridge-Landing Script Architecture (single-shot pattern)"`:

    build_promotion_text → write_atomic_with_fsync → re_read + verify → emit

No BEFORE-pattern conditional rewrites. Anchor-text matching used in place
of plan-asserted line numbers (which drifted due to today's W1-15
deferred-pending re-tag at line 17265 of permanent-results-registry.md).

DISCIPLINE
----------
- `from canonical_constants import *` (S34+ MANDATORY)
- Every local/intermediate tagged `# (local)`
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- 4-tuple printed as the final non-verdict line
- Gate verdict appended atomically to s90_gate_verdicts.txt with dual-SHA
  companion comment row per `.claude/rules/gate-verdicts.md` S87+ schema-v2.
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
GATE_ID = "S90-VII-AAU-VII-AV-WITHDRAWN-IN-FAVOR-OF-S90-LANDING-CLEANUP"  # (local)
SCHEME = "mack-sole-writer-single-shot-AFTER-pattern"          # (local)
CONVENTION = "registry-hygiene-cleanup"                        # (local)
L_MAX = "N/A"                                                  # (local)

REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"  # (local)
S89_VERDICTS_PATH = (
    PROJECT_ROOT / "computations" / "session-89" / "s89_gate_verdicts.txt"
)  # (local)
VERDICT_TXT = SESSION_DIR / "s90_gate_verdicts.txt"  # (local)

# W7c three-emission supersedes chain (pinned in plan §"Hard prerequisites"
# line 55; verified to exist in s89_gate_verdicts.txt via Grep at landing).
W7C_SHA_AAU = (
    "c857179040b40224d8e8484cbb3b0ced077b380c3be4a3d9758ecb9c58e44dff"
)  # (local) emission #1 (lexical wrong-slot §VII.AAU)
W7C_SHA_AU = (
    "f1fae96aae6d401bb8bfa6ffa9525d61eb1b2dfe9d0014de775867ad089e97d0"
)  # (local) emission #2 (§VII.AU correct slot, Element 2 regex fail)
W7C_SHA_AV = (
    "cc18126581ddd9a1ea0fa9f92e4d881219773fc363f749be082c8f2b429cc61d"
)  # (local) emission #3 (latest non-superseded; §VII.AV rerouted)

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    REGISTRY_PATH,
    S89_VERDICTS_PATH,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema, W9a-99 split)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
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
    """audit_sha256 = sha256(script || canonical || pinmap_json);
    content_sha256 = sha256(script)."""
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
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
# Section 5 — build_promotion_text (pure function; AFTER-pattern step 1)
# ---------------------------------------------------------------------------

ANCHOR_AAU = "### §VII.AAU.OP-PROJ — FWD-C1 Pillar I↔II Bridge Theorem Candidate"  # (local)
ANCHOR_AU = "### §VII.AU.OP-PROJ — FWD-C1 Pillar I↔II Bridge Theorem Candidate"  # (local)
ANCHOR_AV = "### §VII.AV.OP-PROJ — FWD-C1 Pillar I↔II Bridge Theorem Candidate"  # (local)

STATUS_AAU = (
    "**Status**: WITHDRAWN-IN-FAVOR-OF-S90-LANDING (CF-18 cleanup; "
    "emission #1 of W7c supersedes chain; lexical-construction wrong-slot; "
    f"supersedes_audit_sha256={W7C_SHA_AAU}; "
    "canonical content host pending CF-64 is §VII.AU.OP-PROJ)"
)  # (local)

PROVENANCE_AU = (
    "**Provenance annotation (CF-18)**: emission #2 of W7c supersedes "
    f"chain (audit_sha256={W7C_SHA_AU}); canonical content host pending "
    "CF-64 single-shot lexical-form retry with regex-compliant Element 2 "
    "OE-form."
)  # (local)

STATUS_AV = (
    "**Status**: WITHDRAWN-IN-FAVOR-OF-S90-LANDING (CF-18 cleanup; "
    "emission #3 of W7c supersedes chain; parallel-writer-race rerouted "
    f"slot; supersedes_audit_sha256={W7C_SHA_AV}; substrate-physics "
    "content intact but registry-slot identity superseded by CF-64 "
    "§VII.AU.OP-PROJ retry)"
)  # (local)


def insert_after_heading_blank(text, anchor, insertion):
    """Insert `insertion` right after the heading line and its trailing
    blank line. Idempotent guard: if the heading is followed by the
    insertion already, return text unchanged."""
    idx = text.find(anchor)  # (local)
    if idx == -1:
        raise ValueError(f"Anchor not found: {anchor[:60]}...")
    end_of_heading = text.find("\n", idx)  # (local)
    if end_of_heading == -1:
        raise ValueError(f"Heading line not terminated: {anchor[:60]}...")
    # Heading is followed by \n + blank line (\n).
    if text[end_of_heading + 1] != "\n":
        raise ValueError(
            f"Expected blank line after heading: {anchor[:60]}..."
        )
    insertion_point = end_of_heading + 2  # (local) start of next content block
    # Idempotency check
    leading_snippet = text[insertion_point:insertion_point + len(insertion) + 8]  # (local)
    if leading_snippet.startswith(insertion):
        return text  # already inserted; no-op (idempotent)
    return text[:insertion_point] + insertion + "\n\n" + text[insertion_point:]


def build_promotion_text(original_text):
    """Pure function: original registry text → promoted registry text with
    three insertions at the three §VII.A* slots (CF-18 cleanup)."""
    t = insert_after_heading_blank(original_text, ANCHOR_AAU, STATUS_AAU)  # (local)
    t = insert_after_heading_blank(t, ANCHOR_AU, PROVENANCE_AU)  # (local)
    t = insert_after_heading_blank(t, ANCHOR_AV, STATUS_AV)  # (local)
    return t


# ---------------------------------------------------------------------------
# Section 6 — write_atomic_with_fsync (AFTER-pattern step 2)
# ---------------------------------------------------------------------------

def write_atomic_with_fsync(path, text):
    """Atomic write via tempfile + rename; fsync the tempfile before rename."""
    tmp = path.with_suffix(path.suffix + ".tmp")  # (local)
    with tmp.open("w", encoding="utf-8", newline="\n") as fp:
        fp.write(text)
        fp.flush()
        os.fsync(fp.fileno())
    os.replace(tmp, path)  # atomic rename on Win + POSIX


# ---------------------------------------------------------------------------
# Section 7 — re_read + verify_section_matches (AFTER-pattern step 3)
# ---------------------------------------------------------------------------

def find_window_after_anchor(text, anchor, window_chars=600):
    """Return a `window_chars`-wide window of text starting at the anchor."""
    idx = text.find(anchor)  # (local)
    if idx == -1:
        return ""
    return text[idx:idx + window_chars]


def verify_section_matches(text):
    """Return (bool overall, dict per-slot) of artifact-existence verifies."""
    window_aau = find_window_after_anchor(text, ANCHOR_AAU)  # (local)
    window_au = find_window_after_anchor(text, ANCHOR_AU)  # (local)
    window_av = find_window_after_anchor(text, ANCHOR_AV)  # (local)
    checks = {
        "aau_status_present": "WITHDRAWN-IN-FAVOR-OF-S90-LANDING" in window_aau,
        "aau_sha_present": W7C_SHA_AAU[:16] in window_aau,
        "au_provenance_present": "Provenance annotation (CF-18)" in window_au,
        "au_sha_present": W7C_SHA_AU[:16] in window_au,
        "av_status_present": "WITHDRAWN-IN-FAVOR-OF-S90-LANDING" in window_av,
        "av_sha_present": W7C_SHA_AV[:16] in window_av,
    }
    overall = all(checks.values())  # (local)
    return overall, checks


# ---------------------------------------------------------------------------
# Section 8 — emit_verdict (AFTER-pattern step 4; exactly one canonical line)
# ---------------------------------------------------------------------------

def emit_verdict(verdict, value_str, audit_sha, content_sha):
    """Append a single canonical line + dual-SHA companion row to s90_gate_verdicts.txt."""
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
# Section 9 — Main (AFTER-pattern composition)
# ---------------------------------------------------------------------------

def main():
    t0 = time.time()  # (local)

    # Step 0: input pin SHAs + dual-SHA
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # Step 1: build promotion text in memory (pure)
    print("Step 1: read registry + build_promotion_text (pure function)")
    original_text = REGISTRY_PATH.read_text(encoding="utf-8")  # (local)
    try:
        promoted_text = build_promotion_text(original_text)  # (local)
    except ValueError as e:
        print(f"  ERROR in build_promotion_text: {e}")
        verdict_value = (
            f"build_promotion_text_FAILED;reason={e!s};"
            "allowlist_row=pending;instances_row=pending"
        )  # (local)
        emit_verdict("FAIL", verdict_value, audit_sha, content_sha)
        print(f"\n=== {GATE_ID}: FAIL (wall {time.time() - t0:.1f}s) ===")
        return 0  # exit 0 — FAIL is a valid scientific result

    # Step 2: write atomically with fsync
    print("Step 2: write_atomic_with_fsync to permanent-results-registry.md")
    write_atomic_with_fsync(REGISTRY_PATH, promoted_text)

    # Step 3: re-read + verify
    print("Step 3: re-read + verify_section_matches")
    re_read_text = REGISTRY_PATH.read_text(encoding="utf-8")  # (local)
    overall, checks = verify_section_matches(re_read_text)
    for k, v in checks.items():
        print(f"  {k}: {'PASS' if v else 'FAIL'}")

    # Step 4: emit_verdict (exactly ONE canonical line per AFTER-pattern)
    print(f"Step 4: emit_verdict ({'PASS' if overall else 'FAIL'})")
    verdict = "PASS" if overall else "FAIL"  # (local)
    n_checks_pass = sum(1 for v in checks.values() if v)  # (local)
    verdict_value = (
        f"all_three_slots_verified={overall};"
        f"checks_pass={n_checks_pass}_of_{len(checks)};"
        f"aau_supersedes_sha={W7C_SHA_AAU[:16]};"
        f"au_provenance_sha={W7C_SHA_AU[:16]};"
        f"av_supersedes_sha={W7C_SHA_AV[:16]};"
        f"line_drift_handled_via_anchor_text_matching=True;"
        f"after_pattern_compliance=True;"
        f"allowlist_row=pending;instances_row=pending"
    )  # (local)
    emit_verdict(verdict, verdict_value, audit_sha, content_sha)

    # 4-tuple final non-verdict line
    tag = (
        f"(value={overall!r}, scheme={SCHEME}, "
        f"convention={CONVENTION}, L_max={L_MAX})"
    )  # (local)
    print(tag)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0  # exit 0 regardless of PASS/FAIL — verdict is data, not script-health


if __name__ == "__main__":
    sys.exit(main())
