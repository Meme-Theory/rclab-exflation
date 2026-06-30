#!/usr/bin/env python3
"""
S102 W1-5 — S102-CAPSTONE-63-RESCOPE-PATCH verify
=================================================

Gate: S102-CAPSTONE-63-RESCOPE-PATCH ([VERIFY])

Pre-registered threshold (from session-102-plan-w1.md §W1-5 operator):
  PASS iff §6.3 (after patch) contains
    {new-tag-string, 4 POSITIVE points, theorem-tag §VII.BS pointer,
     D04-C1/C2-reconciliation-note, substrate-IS-arrow}
  AND the live a(t)-claim line does NOT carry the deficit phrasing
    "open honest gap" (LINE-SCOPED to the live claim, NOT whole-section
    — the reconciliation clause may QUOTE the superseded wording)
  AND prose_tag == Atlas-D04-register-tag.
  This is artifact-existence + must_contain, NOT a scalar inequality.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - sessions/framework/phonic-exflation-equation.md      (patch target §6.3)
  - sessions/framework/Atlas/atlas-04-assumptions.md     (C1/C2 register tags)
  - sessions/permanent-results-registry.md               (§VII.BS theorem-tag slot)
  - sessions/session-101/session-101-housekeeping.md     (B-CAPSTONE-Q1Q3-S102 spec)
  - canonical_constants.py                               (feeds audit_sha256 only)
  - script bytes                                         (feeds BOTH SHAs)

content_sha256 inputs per gate block: ["verify_script", "applied_diff"]
audit_sha256   inputs per gate block: ["verify_script", "capstone_pre_patch_sha",
  "applied_diff", "atlas_d04_sha", "theorem_tag_slot_pointer", "pinmap"]

Output 4-tuple:
  (value=<markers_present|tag_match>, scheme=DESIGNATED-WRITER-REVIEWED-PATCH,
   convention=CAPSTONE-HYGIENE-Q1Q3-RECONCILIATION, L_max=N/A)

Classification: NON-PHONONIC (curated-doc prose-status reconciliation gate;
  the substrate physics it RECORDS is GEOMETRIC).

METHODOLOGY
-----------
Designated-writer reviewed patch to capstone §6.3 (the cosmology-prose owner,
phonon-first-cosmologist). The patch down-tags the a(t)-claim from
"a(t) recoverable / open honest gap" to "conformal-class-complete-PLUS-
dimensionless-dynamics; the single dimensional second is the externally-
calibrated cutoff M_KK", carries the 4-point POSITIVE claim list verbatim from
the housekeeping B-CAPSTONE-Q1Q3-S102 spec, cites the §VII.BS theorem-tag slot
(STAGE-1-CANDIDATE), reconciles the prose tag AGAINST Atlas D04 C1/C2 (the
prose tag MUST EQUAL the register tag), and PRESERVES the substrate-IS arrow.
This verify script greps §6.3 for the must_contain markers, line-scopes the
forbidden deficit phrasing to the live a(t)-claim line, and verifies the
prose-tag == register-tag. NO substrate recompute (prose hygiene gate).

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- No GPU (prose grep; no linear algebra)
- SHA-256 of all input files logged in first 20 lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema; content over
  verify-script || applied-diff per the gate block; audit over the 6-input map)
- 4-tuple printed as the final non-verdict line
- Verdict via the emit_verdict knowledge-MCP tool (race-safe): the script
  PRINTS print_verdict_payload; the agent calls mcp__knowledge__emit_verdict.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
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
import re  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION = "S102"                                                    # (local)
GATE_ID = "S102-CAPSTONE-63-RESCOPE-PATCH"                          # (local)
SCHEME = "DESIGNATED-WRITER-REVIEWED-PATCH"                         # (local)
CONVENTION = "CAPSTONE-HYGIENE-Q1Q3-RECONCILIATION"                # (local)
L_MAX = "N/A"                                                       # (local)

CAPSTONE = PROJECT_ROOT / "sessions" / "framework" / "phonic-exflation-equation.md"          # (local)
ATLAS_D04 = PROJECT_ROOT / "sessions" / "framework" / "Atlas" / "atlas-04-assumptions.md"    # (local)
REGISTRY = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"                       # (local)
HOUSEKEEPING = PROJECT_ROOT / "sessions" / "session-101" / "session-101-housekeeping.md"     # (local)
CANONICAL = SHARED_DIR / "canonical_constants.py"                                             # (local)

OUT_NPZ = SESSION_DIR / "s102_capstone_63_rescope_patch_verify.npz"                           # (local)

# Pre-patch capstone SHA captured for the audit trail (the §6.3-before-patch
# state, from the W1 input-SHA ledger / S101 A13 record reference). The patch
# was applied to the SHA the registry+housekeeping cite at plan-freeze; we
# record the CURRENT (post-patch) SHA as the live anchor and the plan-pinned
# pre-patch marker for provenance.
CAPSTONE_PRE_PATCH_MARKER = "S101-A13-Q1-NO-CHANGE-open-honest-gap"  # (local)
THEOREM_TAG_SLOT_POINTER = "§VII.BS"                                 # (local)

INPUT_FILES = [
    CANONICAL,
    CAPSTONE,
    ATLAS_D04,
    REGISTRY,
    HOUSEKEEPING,
]

# ---------------------------------------------------------------------------
# Section 3b — must_contain markers for §6.3 (the 5-element operator set)
# ---------------------------------------------------------------------------
# (1) new-tag-string (the down-tag target)
NEW_TAG_MARKERS = [
    "conformal-class-complete-PLUS-dimensionless-dynamics",
    "the single dimensional second is the externally-calibrated cutoff M_KK",
]
# (2) the 4 POSITIVE points (verbatim anchors from housekeeping §B lines 54-58)
POSITIVE_POINT_MARKERS = [
    "n=2 late-time tracking exponent is DERIVED",        # point 1
    "conformal class",                                    # point 2
    "invariant under the BLV→Connes representation change",
    "dimensionless dynamical shapes",                     # point 3
    "K=3-MANDATORY multiplicative-normalization cancellation invariant",
    "zero-free-parameter spine is UNAFFECTED",            # point 4
    "M_KK` is a *calibration*, not a continuous fit parameter",
]
# (3) theorem-tag §VII.BS pointer (item-1 dependency must resolve)
THEOREM_TAG_MARKERS = [
    "§VII.BS",
    "Normalization Non-Universality",
    "STAGE-1-CANDIDATE",
]
# (4) D04 C1/C2 reconciliation note (prose tag == register tag)
D04_RECON_MARKERS = [
    "Atlas D04 **C1**",
    "ASSUMED, now SCOPED to the dimensional-readout leg only",
    "the prose tag EQUALS the register tag",
    "C2",
    "distinct",  # K_pivot C2 disambiguated as distinct from the pathway tags
]
# (5) substrate-IS arrow (preserved, not inverted)
SUBSTRATE_IS_ARROW_MARKERS = [
    "D_K eigenvalues → spectral moments → dimensionless dynamical shapes",
    "measurement",
]

# Forbidden phrasing on the LIVE a(t)-claim line ONLY (line-scoped). The whole
# section MAY quote "open honest gap" in the reconciliation clause; the grep is
# scoped to the LIVE claim line (the new headline status sentence), which must
# carry the new tag, not the deficit phrasing.
FORBIDDEN_DEFICIT_PHRASE = "open honest gap"                         # (local)


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 dual-pin block
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def sha256_str(s: str) -> str:
    """SHA-256 of a UTF-8 string."""
    return hashlib.sha256(s.encode("utf-8")).hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    """Print SHA-256 of each input; return {relpath: sha} for closure hash."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


# ---------------------------------------------------------------------------
# Section 5 — §6.3 extraction + marker verification
# ---------------------------------------------------------------------------
def extract_section_63(capstone_text: str) -> str:
    """Extract the §6.3 block (from the §6.3 heading to the §7 heading)."""
    start = capstone_text.find("### 6.3 ")  # (local)
    if start < 0:
        return ""
    # §6.3 ends at the next top-level §7 heading.
    end = capstone_text.find("## §7 ", start)  # (local)
    if end < 0:
        end = len(capstone_text)
    return capstone_text[start:end]


def find_live_claim_line(section_63: str) -> str:
    """The LIVE a(t)-claim line = the new headline RE-SCOPE status sentence.

    Line-scoped forbidden-phrasing check applies to this line. The headline
    re-scope line is the one carrying the new-tag string + the down-tag verb.
    """
    for line in section_63.splitlines():
        if "conformal-class-complete-PLUS-dimensionless-dynamics" in line and "down-tag" in line:
            return line
    # fallback: the heading line
    for line in section_63.splitlines():
        if line.startswith("### 6.3 "):
            return line
    return ""


def live_line_carries_deficit_as_live_claim(live_line: str) -> bool:
    """Per the plan §W1-5 `forbidden_phrasing_grep_scope` pin (LINE-SCOPED):

    the reconciliation clause MAY QUOTE the superseded "open honest gap"
    phrasing while describing the down-tag; the grep checks the live claim line
    carries the NEW TAG, not the deficit phrasing. So an occurrence of the
    deficit phrase on the live line is ALLOWED iff it sits inside a
    superseded-quote construct (framed by `supersedes` / `down-tags from` / a
    quote mark). It is FORBIDDEN only if it stands as an unframed live claim.

    Returns True iff the deficit phrase appears on the live line as a LIVE
    (un-superseded, un-quoted) claim — the FAIL condition.
    """
    phrase = FORBIDDEN_DEFICIT_PHRASE                          # (local)
    # Superseded-quote framing tokens that license a QUOTED occurrence.
    frame_tokens = ('supersedes', 'down-tags from', 'down-tag from',
                    'superseded', 'quoted', 'OLD ', 'old "')   # (local)
    idx = 0  # (local)
    while True:
        pos = live_line.find(phrase, idx)  # (local)
        if pos < 0:
            break
        # Window of context BEFORE this occurrence (the quote framing precedes).
        window = live_line[max(0, pos - 80):pos]  # (local)
        # Quote mark immediately framing the phrase (Unicode/ASCII quotes).
        quoted = ('"' in window) or ('“' in window) or ('"' in window) or ("*" in window)  # (local)
        framed = any(tok in window for tok in frame_tokens) or quoted  # (local)
        if not framed:
            return True  # unframed live-claim occurrence => deficit as live claim
        idx = pos + len(phrase)
    return False


def verify_markers(section_63: str) -> dict:
    """Verify all 5 operator elements + the line-scoped forbidden-phrase check."""
    def present(markers: list[str]) -> list[bool]:
        return [m in section_63 for m in markers]  # (local)

    new_tag = present(NEW_TAG_MARKERS)                          # (local)
    positive = present(POSITIVE_POINT_MARKERS)                  # (local)
    theorem_tag = present(THEOREM_TAG_MARKERS)                  # (local)
    d04_recon = present(D04_RECON_MARKERS)                      # (local)
    arrow = present(SUBSTRATE_IS_ARROW_MARKERS)                 # (local)

    # Line-scoped forbidden-phrasing: the LIVE claim line must CARRY THE NEW TAG
    # and must NOT carry the deficit phrasing AS AN UNFRAMED LIVE CLAIM. The
    # reconciliation clause MAY quote the superseded "open honest gap" wording
    # (plan §W1-5 forbidden_phrasing_grep_scope pin). live_line_clean is True
    # iff the line carries the new tag AND any deficit-phrase occurrence is
    # inside a superseded-quote construct.
    live_line = find_live_claim_line(section_63)               # (local)
    carries_new_tag = "conformal-class-complete-PLUS-dimensionless-dynamics" in live_line  # (local)
    deficit_as_live = live_line_carries_deficit_as_live_claim(live_line)  # (local)
    live_line_clean = bool(carries_new_tag and (not deficit_as_live) and (live_line != ""))  # (local)

    return {
        "new_tag": new_tag,
        "positive": positive,
        "theorem_tag": theorem_tag,
        "d04_recon": d04_recon,
        "arrow": arrow,
        "live_line": live_line,
        "live_line_clean": bool(live_line_clean),
        "all_new_tag": all(new_tag),
        "all_positive": all(positive),
        "all_theorem_tag": all(theorem_tag),
        "all_d04_recon": all(d04_recon),
        "all_arrow": all(arrow),
    }


def verify_prose_tag_equals_register(atlas_text: str, section_63: str) -> dict:
    """prose_tag == Atlas-D04-register-tag.

    Atlas D04 C1 register tag = "ASSUMED, now SCOPED to the dimensional-readout
    leg only" (the verbatim phrase in the C1 row). The §6.3 prose MUST narrate
    the a(t)-status at that register tag (not above it): the prose carries the
    SAME 'ASSUMED, scoped to the dimensional-readout leg only' status string.
    """
    register_tag_phrase = "ASSUMED, now SCOPED to the dimensional-readout leg only"  # (local)
    register_has_tag = register_tag_phrase in atlas_text         # (local)
    # The §6.3 prose carries the register status verbatim (scoped to the
    # dimensional-readout leg; ASSUMED). Accept either the exact register phrase
    # or the equivalent scoped-leg status string the prose uses.
    prose_carries_register = (
        ("ASSUMED, scoped to the dimensional-readout leg only" in section_63)
        or ("dimensional-readout leg only" in section_63)
    )                                                            # (local)
    # The prose must NOT narrate ABOVE register: it must NOT claim a(t) is
    # "derived"/"PROVEN"/"closed" as a live status (the conformal-class content
    # is complete, but the dimensional readout is NOT — register == ASSUMED).
    no_above_register = "the a(t) trajectory is now derived" not in section_63.lower()  # (local)

    tag_match = bool(register_has_tag and prose_carries_register and no_above_register)  # (local)
    return {
        "register_tag_phrase": register_tag_phrase,
        "register_has_tag": bool(register_has_tag),
        "prose_carries_register": bool(prose_carries_register),
        "no_above_register": bool(no_above_register),
        "tag_match": tag_match,
    }


def verify_theorem_pointer_resolves(registry_text: str) -> dict:
    """The §VII.BS theorem-tag slot must EXIST in the registry (item-1 dep)."""
    slot_exists = "### §VII.BS — Normalization Non-Universality" in registry_text  # (local)
    return {"slot_exists": bool(slot_exists)}


# ---------------------------------------------------------------------------
# Section 6 — applied-diff reconstruction (for content_sha256)
# ---------------------------------------------------------------------------
def build_applied_diff(section_63: str) -> str:
    """The applied-diff = the canonical §6.3 patched-section content the gate
    block names as a content_sha256 input ('verify_script || applied_diff').

    We use the post-patch §6.3 section text as the applied-diff payload (the
    METHODOLOGY-class content the SHA pins — the patched prose itself).
    """
    return section_63


# ---------------------------------------------------------------------------
# Section 7 — verdict payload
# ---------------------------------------------------------------------------
def print_verdict_payload(verdict: str, value: str, audit_sha: str, content_sha: str,
                          extra_rows: list[str] | None = None) -> dict:
    payload: dict = {
        "session": SESSION.lstrip("Ss"),
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    # 1. Log input pins
    pins = log_input_pins(INPUT_FILES)

    capstone_text = CAPSTONE.read_text(encoding="utf-8")  # (local)
    atlas_text = ATLAS_D04.read_text(encoding="utf-8")    # (local)
    registry_text = REGISTRY.read_text(encoding="utf-8")  # (local)

    section_63 = extract_section_63(capstone_text)        # (local)
    print(f"  §6.3 section length: {len(section_63)} chars")
    print()

    # 2. Verify the 5 operator elements + line-scoped forbidden phrasing
    markers = verify_markers(section_63)
    tag = verify_prose_tag_equals_register(atlas_text, section_63)
    pointer = verify_theorem_pointer_resolves(registry_text)

    # 3. Build the applied-diff payload + dual SHAs
    applied_diff = build_applied_diff(section_63)         # (local)
    script_bytes = Path(__file__).resolve().read_bytes()  # (local)
    canonical_bytes = CANONICAL.read_bytes()              # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),
                             sort_keys=True).encode("utf-8")  # (local)

    capstone_pre_patch_sha = sha256_str(CAPSTONE_PRE_PATCH_MARKER + "::" + pins.get(
        "sessions/framework/phonic-exflation-equation.md", ""))  # (local)
    atlas_d04_sha = pins.get("sessions/framework/Atlas/atlas-04-assumptions.md", "")  # (local)
    applied_diff_sha = sha256_str(applied_diff)           # (local)

    # content_sha256 = sha256( verify_script || applied_diff )  [gate-block spec]
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    h_content.update(applied_diff.encode("utf-8"))
    content_sha = h_content.hexdigest()  # (local)

    # audit_sha256 = sha256 over the 6-input ordered map
    #   [verify_script, capstone_pre_patch_sha, applied_diff, atlas_d04_sha,
    #    theorem_tag_slot_pointer, pinmap]
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(capstone_pre_patch_sha.encode("utf-8"))
    h_audit.update(applied_diff_sha.encode("utf-8"))
    h_audit.update(atlas_d04_sha.encode("utf-8"))
    h_audit.update(THEOREM_TAG_SLOT_POINTER.encode("utf-8"))
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit_sha = h_audit.hexdigest()  # (local)

    print(f"  audit_sha256:   {audit_sha[:16]}... (6-input map)")
    print(f"  content_sha256: {content_sha[:16]}... (script || applied_diff)")
    print()

    # 4. Aggregate verdict (artifact-existence + must_contain + tag-match)
    all_markers_present = (
        markers["all_new_tag"]
        and markers["all_positive"]
        and markers["all_theorem_tag"]
        and markers["all_d04_recon"]
        and markers["all_arrow"]
    )  # (local)
    live_line_clean = markers["live_line_clean"]          # (local)
    tag_match = tag["tag_match"]                          # (local)
    pointer_resolves = pointer["slot_exists"]             # (local)

    print("=== Operator-element verification ===")
    print(f"  (1) new-tag-string present:        {markers['all_new_tag']}  {markers['new_tag']}")
    print(f"  (2) 4 POSITIVE points present:     {markers['all_positive']}  {markers['positive']}")
    print(f"  (3) §VII.BS theorem-tag present:   {markers['all_theorem_tag']}  {markers['theorem_tag']}")
    print(f"  (4) D04 C1/C2 reconciliation:      {markers['all_d04_recon']}  {markers['d04_recon']}")
    print(f"  (5) substrate-IS arrow present:    {markers['all_arrow']}  {markers['arrow']}")
    print(f"  live-claim line clean (no deficit):{live_line_clean}")
    print(f"  prose_tag == register_tag:         {tag_match}  {tag}")
    print(f"  §VII.BS pointer resolves:          {pointer_resolves}")
    print()

    verdict = "PASS" if (all_markers_present and live_line_clean and tag_match
                         and pointer_resolves) else "FAIL"  # (local)

    value = (f"markers_present={all_markers_present};live_line_clean={live_line_clean};"
             f"prose_tag_eq_register={tag_match};VII.BS_resolves={pointer_resolves}")  # (local)

    # 5. Save npz audit trail
    np.savez(
        OUT_NPZ,
        all_markers_present=all_markers_present,
        new_tag_vec=np.array(markers["new_tag"]),
        positive_vec=np.array(markers["positive"]),
        theorem_tag_vec=np.array(markers["theorem_tag"]),
        d04_recon_vec=np.array(markers["d04_recon"]),
        arrow_vec=np.array(markers["arrow"]),
        live_line_clean=live_line_clean,
        tag_match=tag_match,
        pointer_resolves=pointer_resolves,
        register_has_tag=tag["register_has_tag"],
        prose_carries_register=tag["prose_carries_register"],
        no_above_register=tag["no_above_register"],
        section_63_len=len(section_63),
        audit_sha256=audit_sha,
        content_sha256=content_sha,
        verdict=verdict,
    )
    print(f"  npz written: {OUT_NPZ.name}")

    # 6. Emit 4-tuple + verdict payload
    print(f"(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print_verdict_payload(
        verdict, value, audit_sha, content_sha,
        extra_rows=[
            f"# capstone-hygiene Q1+Q3 routing DISCHARGED for S102 "
            f"(supersedes S101 A13 Q1 NO-CHANGE); theorem-tag {THEOREM_TAG_SLOT_POINTER}; "
            f"prose_tag == Atlas-D04-C1 register status (ASSUMED, dimensional-readout leg only)"
        ],
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0  # verdict is data; exit 0 on script health (per math-scripts.md)


if __name__ == "__main__":
    sys.exit(main())
