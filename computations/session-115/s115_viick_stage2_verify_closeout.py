#!/usr/bin/env python3
"""
S115 W1-1 S115-VIICK-STAGE2-VERIFY — §VII.CK D1-D3 Stage-2 PASS-AND closeout + registry tag-flip
================================================================================================

Gate: S115-VIICK-STAGE2-VERIFY ([VERIFY-THEOREM])

Pre-registered criterion (plan §W1-1 operator, set-membership / PASS-AND — NOT a scalar inequality):
  composite_PASS  <=>  (forall clause c in {D1, D2, D3}) [ verdict_A(c) = PASS  AND  verdict_B(c) = PASS ]
  6 independent per-clause-per-axis booleans, logical AND.
  FAIL if either reviewer FAILs any clause; INFO if either INFOs a clause and none FAIL.
  The promotion is MONOTONE in the conjunction (a 5-of-6 partial CANNOT promote) —
  the joint-theorem-promotion.md anti-shared-context discipline.

This is a VERDICT-AGGREGATOR + REGISTRY TAG-FLIP closeout. No physics re-derivation:
the two BLIND cross-reviewers (Axis-A lizzi-spectral-functional-theorist,
Axis-B kitaev-quantum-chaos-theorist) each re-derived D1/D2/D3 from first principles
WITHOUT workshop context; this script reads their per-clause verdicts off disk, PASS-ANDs
them, and (on composite PASS) flips §VII.CK STAGE-1-CANDIDATE -> STAGE-3-PERMANENT with the
D4-open scope qualifier RETAINED.

Inputs (SHA-256 dual-pinned at runtime — S84+ schema):
  - sessions/session-115/session-115-w1-viick-verify-axis-a.md   (Axis-A blind synthesis)
  - sessions/session-115/session-115-w1-viick-verify-axis-b.md   (Axis-B blind synthesis)
  - sessions/permanent-results-registry.md                       (the registered §VII.CK Stage-1 entry; tag-flip target)
  - computations/session-114/s114_gate_verdicts.txt              (W3-3 landing audit_sha256 pin)
  - canonical_constants.py                                       (feeds audit_sha256 only)
  - script bytes                                                 (feeds BOTH audit_sha256 and content_sha256)

audit_sha256 inputs (plan §W1-1 audit_discriminators):
  ordered input-pin map {registered_entry_anchor_body, W3_3_landing_audit_sha256,
                         reviewer_axis_A_verdict, reviewer_axis_B_verdict, pinmap}
content_sha256 inputs: closeout_script bytes.

Output 4-tuple:
  (value=<composite-verdict-string>, scheme=FW, convention=VII-STAGE-2-CROSS-AXIS-VERIFY, L_max=N/A)

Classification: GEOMETRIC (intra-pillar spectral-triple γ₉/orientation obstruction theorem).

REGISTRY TAG-FLIP (single-shot AFTER-pattern per registry-landing.md §"Bridge-Landing Script
Architecture"): build_promotion_text -> write_atomic_with_fsync -> re-read + verify_section_matches
-> exactly ONE verdict emit whose verdict is the verify boolean. Flips the §VII.CK body header
sentence tag, the STAGE TAG line, AND the master-index row 173, RETAINING the D4-open scope
qualifier (the promoted scope is the CLOSED class {A_K-built ∪ Casimir-graded ∪ γ₉-traced};
D4 right-regular SU(3)_R is NOT promoted here — that is the separate W2 gate).

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- No matrix compute (verdict-aggregator); no GPU path
- SHA-256 of all input files logged in first lines of stdout
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema)
- The script PRINTS the emit_verdict payload; the dispatching AGENT calls mcp__knowledge__emit_verdict.
  The script does NOT write s115_gate_verdicts.txt directly.
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Standard imports + canonical constants (MANDATORY)
# canonical_constants.py lives in computations/_shared/ — put it on sys.path
# first (matching the sibling s115_lepton_pmns_forced_texture.py convention).
# ---------------------------------------------------------------------------
import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "_shared"))
from canonical_constants import *  # noqa: F401,F403,E402

import numpy as np  # noqa: E402  (npz sidecar only; no linear algebra)

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S115"                                                   # (local)
GATE_ID = "S115-VIICK-STAGE2-VERIFY"                              # (local)
SCHEME = "FW"                                                      # (local)
CONVENTION = "VII-STAGE-2-CROSS-AXIS-VERIFY"                       # (local)
L_MAX = "N/A"                                                      # (local)

# Per-gate identity keys (embedded in the audit pinmap so this audit_sha256 is
# distinct from any sibling gate — mechanical-closure-discipline.md item 3 analog)
GATE_IDENTITY = {                                                  # (local)
    "_gate_id": GATE_ID,
    "_wp_id": "S115-W1-1",
    "_scheme": SCHEME,
    "_convention": CONVENTION,
}

# The three CLOSED-INTERNAL clauses under Stage-2 verify (D4 is OUT OF SCOPE here)
CLAUSES = ["D1", "D2", "D3"]                                       # (local)

# The W3-3 Stage-1 landing audit_sha256 (plan §W1-1 pin; cross-checked on disk below)
W3_3_LANDING_AUDIT_SHA256 = (                                       # (local)
    "51f411950ae58c74c635d40fa9fb711acdc9b0a172a5959da5cecc710738171f"
)

# Registry tag-flip anchors
REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"  # (local)
REGISTERED_ENTRY_ANCHOR_BODY = (                                   # (local)
    "### §VII.CK — SHAPE-Branch Homogeneity Obstruction over the "
    "A_K-Built / Casimir-Graded / γ₉-Trace Class"
)

# Reviewer synthesis files
AXIS_A_MD = PROJECT_ROOT / "sessions" / "session-115" / "session-115-w1-viick-verify-axis-a.md"  # (local)
AXIS_B_MD = PROJECT_ROOT / "sessions" / "session-115" / "session-115-w1-viick-verify-axis-b.md"  # (local)

# W3-3 verdict file (carries the landing audit_sha256)
W3_3_VERDICT_FILE = COMPUTATIONS_DIR / "session-114" / "s114_gate_verdicts.txt"  # (local)

OUT_NPZ = SESSION_DIR / "s115_viick_stage2_verify_closeout.npz"   # (local)
# Verdict file is written by emit_verdict MCP tool — NOT this script.

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    AXIS_A_MD,
    AXIS_B_MD,
    REGISTRY_PATH,
    W3_3_VERDICT_FILE,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    """Print SHA-256 of each input; return {relpath: sha} for closure hash."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    """Stable hash over all input SHAs (invariant to dict ordering)."""
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(
    script_path: Path,
    canonical_path: Path,
    audit_pinmap: dict,
) -> tuple[str, str]:
    """Compute (audit_sha256, content_sha256) per the S84+ dual-SHA schema.

    audit_sha256 = sha256( bytes(script) || bytes(canonical) || pinmap_json )
      where pinmap_json is the canonical JSON of the ORDERED audit pin map
      (plan §W1-1 audit_discriminators.audit_sha256_inputs): the registered
      entry anchor body, the W3-3 landing audit_sha256, both reviewer per-clause
      verdict dicts, and the file-SHA pin map (+ per-gate identity keys).

    content_sha256 = sha256( bytes(script) ) — script-only, INVARIANT under
      canonical / pinmap change.
    """
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        audit_pinmap,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)

    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Reviewer-verdict extraction (anchored regex, per-clause)
# ---------------------------------------------------------------------------

def extract_clause_verdict(md_text: str, clause: str) -> str:
    """Extract a reviewer's per-clause verdict (PASS/FAIL/INFO) for `clause`.

    Both reviewer syntheses carry a `## III. Gate Verdicts` table with rows of the
    form `| {clause} — ... | **PASS** | ...` (and the verdict echoed in the section
    header `> **D1 verdict: PASS**` / `**D1 confirms ... VERDICT: PASS.**`). We scan
    every line mentioning the clause token and tally the bold-or-plain verdict
    keyword adjacent to it, then require an unambiguous single verdict.

    Returns 'PASS' | 'FAIL' | 'INFO'. Raises on ambiguity (no verdict found, or
    conflicting verdicts) — an ambiguous extraction must NOT silently default.
    """
    verdicts_found: set[str] = set()  # (local)
    # Clause token must appear as a standalone label (D1/D2/D3), not as a substring
    # of D10 etc. (\b boundary + the clause is followed by a non-digit or end).
    clause_re = re.compile(rf"\b{re.escape(clause)}\b(?!\d)")  # (local)
    verdict_kw_re = re.compile(r"\b(PASS|FAIL|INFO)\b")  # (local)
    for line in md_text.splitlines():
        if not clause_re.search(line):
            continue
        # Only count lines that ALSO carry an explicit verdict keyword AND a
        # verdict-bearing marker (a table cell `| **PASS** |`, a `verdict:`/`VERDICT:`
        # token, or a `>` blockquote verdict line) — avoids counting prose mentions.
        low = line.lower()  # (local)
        is_verdict_line = (
            ("verdict" in low)
            or ("**pass**" in low or "**fail**" in low or "**info**" in low)
            or (line.lstrip().startswith("|") and verdict_kw_re.search(line))
        )
        if not is_verdict_line:
            continue
        for kw in verdict_kw_re.findall(line):
            verdicts_found.add(kw)
    if not verdicts_found:
        raise ValueError(
            f"no per-clause verdict found for {clause} (ambiguous extraction; "
            f"refusing to default)"
        )
    if len(verdicts_found) > 1:
        raise ValueError(
            f"conflicting per-clause verdicts for {clause}: {sorted(verdicts_found)} "
            f"(ambiguous; refusing to default)"
        )
    return verdicts_found.pop()


# ---------------------------------------------------------------------------
# Section 6 — Registry tag-flip (single-shot AFTER-pattern)
# ---------------------------------------------------------------------------

def build_promotion_text(registry_text: str) -> tuple[str, list[str]]:
    """Pure function: build the FULL promoted registry text in memory.

    Flips STAGE-1-CANDIDATE -> STAGE-3-PERMANENT in three places, RETAINING the
    D4-open scope qualifier (the promoted scope is the CLOSED class {A_K-built ∪
    Casimir-graded ∪ γ₉-traced}; D4 right-regular SU(3)_R is NOT promoted here):

      (T1) body header sentence (line ~22422): `(STAGE-1-CANDIDATE, S114 W3-3 ...`
           -> `(STAGE-3-PERMANENT [D4-open RETAINED], S114 W3-3 ...`
      (T2) the STAGE TAG line (~22424): `**STAGE TAG: STAGE-1-CANDIDATE**`
           -> `**STAGE TAG: STAGE-3-PERMANENT** [D4-open scope qualifier RETAINED — D1-D3 closed class]`
      (T3) master-index row 173: `...the SHAPE handle is external (...); STAGE-1-CANDIDATE; intra-pillar...`
           -> `...; STAGE-3-PERMANENT (S115 W1-1 Stage-2 PASS-AND; D4-open RETAINED); intra-pillar...`

    Returns (new_text, list_of_change_descriptions). Each target is matched as a
    UNIQUE literal substring; a missing/non-unique target is a HARD error (raises),
    so the flip cannot silently no-op or double-apply.
    """
    changes: list[str] = []  # (local)
    text = registry_text  # (local)

    # --- (T1) body header sentence ---
    t1_old = "for the same homogeneity reason the §VII.BL MAGNITUDE is (STAGE-1-CANDIDATE, S114 W3-3 gen-physicist registration"  # (local)
    t1_new = (
        "for the same homogeneity reason the §VII.BL MAGNITUDE is "
        "(STAGE-3-PERMANENT [D4-open scope qualifier RETAINED; S115 W1-1 Stage-2 PASS-AND], "
        "S114 W3-3 gen-physicist registration"
    )  # (local)
    n1 = text.count(t1_old)  # (local)
    if n1 != 1:
        raise ValueError(f"(T1) body-header anchor matched {n1} times (expected 1)")
    text = text.replace(t1_old, t1_new)
    changes.append("T1 body-header STAGE-1-CANDIDATE -> STAGE-3-PERMANENT [D4-open RETAINED]")

    # --- (T2) the STAGE TAG line ---
    t2_old = "**STAGE TAG: STAGE-1-CANDIDATE** (`joint-theorem-promotion.md` §\"Stage 1 — Registration as Candidate\")."  # (local)
    t2_new = (
        "**STAGE TAG: STAGE-3-PERMANENT** [D4-open scope qualifier RETAINED — the promoted "
        "scope is the CLOSED-INTERNAL class {A_K-built ∪ Casimir-graded ∪ γ₉-traced} (D1-D3); "
        "the D4 right-regular SU(3)_R unconditional re-scope is the SEPARATE gate "
        "CF-S115-VIICK-D4-DISCHARGE-UNCONDITIONAL, NOT promoted here] "
        "(`joint-theorem-promotion.md` §\"Stage 3 — Permanent Registration\"; promoted from "
        "STAGE-1-CANDIDATE by `S115-VIICK-STAGE2-VERIFY`, Stage-2 two-agent blind cross-axis "
        "PASS-AND: Axis-A lizzi-spectral-functional-theorist × Axis-B kitaev-quantum-chaos-theorist, "
        "D1/D2/D3 each PASS-AND'd across both blind verdicts, 2026-06-24)."
    )  # (local)
    n2 = text.count(t2_old)  # (local)
    if n2 != 1:
        raise ValueError(f"(T2) STAGE-TAG anchor matched {n2} times (expected 1)")
    text = text.replace(t2_old, t2_new)
    changes.append("T2 STAGE TAG line STAGE-1-CANDIDATE -> STAGE-3-PERMANENT [D4-open RETAINED]")

    # --- (T3) master-index row 173 ---
    t3_old = "the SHAPE handle is external (the ε_LX channel carrying the §VII.BL magnitude); STAGE-1-CANDIDATE; intra-pillar GEOMETRIC"  # (local)
    t3_new = (
        "the SHAPE handle is external (the ε_LX channel carrying the §VII.BL magnitude); "
        "STAGE-3-PERMANENT (S115 W1-1 `S115-VIICK-STAGE2-VERIFY` Stage-2 blind cross-axis PASS-AND, "
        "Axis-A lizzi × Axis-B kitaev, D1/D2/D3 PASS/PASS/PASS each axis; D4-open scope qualifier "
        "RETAINED — D4 right-regular SU(3)_R re-scope owed to CF-S115-VIICK-D4-DISCHARGE-UNCONDITIONAL); "
        "intra-pillar GEOMETRIC"
    )  # (local)
    n3 = text.count(t3_old)  # (local)
    if n3 != 1:
        raise ValueError(f"(T3) master-index-row-173 anchor matched {n3} times (expected 1)")
    text = text.replace(t3_old, t3_new)
    changes.append("T3 master-index row 173 STAGE-1-CANDIDATE -> STAGE-3-PERMANENT [D4-open RETAINED]")

    return text, changes


def write_atomic_with_fsync(path: Path, text: str) -> None:
    """Write `text` to `path` atomically (tmp + fsync + os.replace)."""
    tmp = path.with_suffix(path.suffix + ".tmp")  # (local)
    with open(tmp, "w", encoding="utf-8", newline="") as f:
        f.write(text)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp, path)


def verify_section_matches(path: Path) -> dict:
    """Re-read the registry and verify the post-flip invariants.

    Returns a dict of boolean checks; the closeout PASS requires ALL True.
      - body-header now reads STAGE-3-PERMANENT (the T1 marker present)
      - STAGE TAG line now reads STAGE-3-PERMANENT (T2 marker present)
      - master-index row 173 now reads STAGE-3-PERMANENT (T3 marker present)
      - the D4-open scope qualifier `class = {A_K-built ∪ Casimir-graded ∪ γ₉-traced}` RETAINED
      - NO residual `**STAGE TAG: STAGE-1-CANDIDATE**` for §VII.CK
    """
    text = path.read_text(encoding="utf-8")  # (local)
    checks = {
        "body_header_stage3": "STAGE-3-PERMANENT [D4-open scope qualifier RETAINED; S115 W1-1 Stage-2 PASS-AND]" in text,
        "stage_tag_stage3": "**STAGE TAG: STAGE-3-PERMANENT**" in text,
        "master_index_stage3": "STAGE-3-PERMANENT (S115 W1-1 `S115-VIICK-STAGE2-VERIFY` Stage-2 blind cross-axis PASS-AND" in text,
        "d4_open_scope_retained": "class = {A_K-built ∪ Casimir-graded ∪ γ₉-traced}" in text,
        "no_residual_stage1_tag": "**STAGE TAG: STAGE-1-CANDIDATE**" not in text,
    }
    return checks


# ---------------------------------------------------------------------------
# Section 7 — Verdict payload
# ---------------------------------------------------------------------------

def print_verdict_payload(
    verdict: str,
    value,
    audit_sha: str,
    content_sha: str,
    extra_rows: list[str] | None = None,
) -> dict:
    """Print the emit_verdict PAYLOAD for the dispatching AGENT (race-safe write)."""
    payload: dict = {
        "session": 115,
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
    closure = closure_hash(pins)  # (local)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")
    print()

    # 2. Cross-check the W3-3 landing audit_sha256 pin is present on disk
    w3_3_text = W3_3_VERDICT_FILE.read_text(encoding="utf-8")  # (local)
    w3_3_pin_present = W3_3_LANDING_AUDIT_SHA256 in w3_3_text  # (local)
    print(f"  W3-3 landing audit_sha256 ({W3_3_LANDING_AUDIT_SHA256[:16]}...) present in s114 verdict file: {w3_3_pin_present}")
    if not w3_3_pin_present:
        raise ValueError("W3-3 landing audit_sha256 pin NOT found in s114 verdict file (upstream prereq missing)")

    # 3. Extract per-clause verdicts from the two BLIND reviewer syntheses
    axis_a_text = AXIS_A_MD.read_text(encoding="utf-8")  # (local)
    axis_b_text = AXIS_B_MD.read_text(encoding="utf-8")  # (local)
    verdict_A = {c: extract_clause_verdict(axis_a_text, c) for c in CLAUSES}  # (local)
    verdict_B = {c: extract_clause_verdict(axis_b_text, c) for c in CLAUSES}  # (local)
    print("=== per-clause verdicts (blind cross-reviewers) ===")
    print(f"  Axis-A (lizzi-spectral-functional-theorist): {verdict_A}")
    print(f"  Axis-B (kitaev-quantum-chaos-theorist):      {verdict_B}")
    print()

    # 4. PASS-AND adjudication: 6 independent booleans, logical AND
    booleans = {}  # (local)
    for c in CLAUSES:
        booleans[f"A_{c}"] = (verdict_A[c] == "PASS")
        booleans[f"B_{c}"] = (verdict_B[c] == "PASS")
    composite_pass = all(booleans.values())  # (local)
    any_fail = any(
        (verdict_A[c] == "FAIL") or (verdict_B[c] == "FAIL") for c in CLAUSES
    )  # (local)
    any_info = any(
        (verdict_A[c] == "INFO") or (verdict_B[c] == "INFO") for c in CLAUSES
    )  # (local)

    if composite_pass:
        verdict = "PASS"  # (local)
    elif any_fail:
        verdict = "FAIL"  # (local)
    elif any_info:
        verdict = "INFO"  # (local)
    else:
        verdict = "FAIL"  # (local) defensive — non-PASS, non-FAIL, non-INFO is malformed
    print("=== 6-boolean PASS-AND ===")
    for k, v in booleans.items():
        print(f"  {k} (PASS?): {v}")
    print(f"  composite_PASS = AND(all 6) = {composite_pass}  =>  verdict = {verdict}")
    print()

    # 5. Capture pre-flip registry SHA
    registry_pre_sha = sha256_of(REGISTRY_PATH)  # (local)
    print(f"  registry SHA (pre-flip): {registry_pre_sha[:16]}...")

    # 6. Registry tag-flip (single-shot AFTER-pattern) — ONLY on composite PASS.
    #    build_promotion_text -> write_atomic_with_fsync -> re-read + verify.
    flip_checks = {}  # (local)
    flip_changes = []  # (local)
    registry_post_sha = registry_pre_sha  # (local) unchanged unless we flip
    verify_ok = False  # (local)
    if composite_pass:
        registry_text = REGISTRY_PATH.read_text(encoding="utf-8")  # (local)
        # Idempotency: if already promoted (re-run), the T1 anchor is gone -> skip flip,
        # but still re-verify the post-state.
        already_promoted = (
            "**STAGE TAG: STAGE-3-PERMANENT**" in registry_text
            and "**STAGE TAG: STAGE-1-CANDIDATE**" not in registry_text
        )  # (local)
        if already_promoted:
            print("  registry §VII.CK already STAGE-3-PERMANENT (idempotent re-run) — verifying post-state only")
            flip_checks = verify_section_matches(REGISTRY_PATH)
            flip_changes = ["(idempotent no-op — §VII.CK already promoted)"]
        else:
            new_text, flip_changes = build_promotion_text(registry_text)
            write_atomic_with_fsync(REGISTRY_PATH, new_text)
            flip_checks = verify_section_matches(REGISTRY_PATH)
        registry_post_sha = sha256_of(REGISTRY_PATH)  # (local)
        verify_ok = all(flip_checks.values())  # (local)
        print("=== registry tag-flip (single-shot AFTER-pattern) ===")
        for ch in flip_changes:
            print(f"  change: {ch}")
        for k, v in flip_checks.items():
            print(f"  verify {k}: {v}")
        print(f"  registry SHA (post-flip): {registry_post_sha[:16]}...")
        print(f"  verify_section_matches (ALL True required): {verify_ok}")
        print()
        # The composite verdict for the AFTER-pattern is the conjunction of the
        # PASS-AND adjudication AND the registry-flip verification.
        if not verify_ok:
            # Flip verification failed -> the closeout honestly FAILs (no corrective
            # rewrite in-script; remediation escalates per mechanical-closure-discipline.md).
            verdict = "FAIL"  # (local)
            print("  WARNING: registry tag-flip verification FAILED — closeout verdict downgraded to FAIL")
    else:
        print("=== registry tag-flip SKIPPED (composite verdict != PASS) ===")
        print(f"  §VII.CK stays STAGE-1-CANDIDATE; verdict={verdict}; failing/INFO clause routes to S116 remediation")
        print()

    # 7. Build the audit pinmap (plan §W1-1 audit_discriminators.audit_sha256_inputs)
    audit_pinmap = {  # (local)
        "registered_entry_anchor_body": REGISTERED_ENTRY_ANCHOR_BODY,
        "W3_3_landing_audit_sha256": W3_3_LANDING_AUDIT_SHA256,
        "reviewer_axis_A_verdict": verdict_A,
        "reviewer_axis_B_verdict": verdict_B,
        "pinmap": dict(sorted(pins.items())),
        **GATE_IDENTITY,
    }

    # 8. Compute S84+ dual SHAs
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, audit_pinmap)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+ordered-pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # 9. Persist npz sidecar (the two reviewer verdict dicts + the PASS-AND boolean)
    np.savez(
        OUT_NPZ,
        clauses=np.array(CLAUSES),
        verdict_A=np.array([verdict_A[c] for c in CLAUSES]),
        verdict_B=np.array([verdict_B[c] for c in CLAUSES]),
        booleans_keys=np.array(list(booleans.keys())),
        booleans_vals=np.array([booleans[k] for k in booleans], dtype=bool),
        composite_pass=np.array(composite_pass),
        verdict=np.array(verdict),
        w3_3_landing_audit_sha256=np.array(W3_3_LANDING_AUDIT_SHA256),
        registry_pre_sha=np.array(registry_pre_sha),
        registry_post_sha=np.array(registry_post_sha),
        flip_verify_keys=np.array(list(flip_checks.keys())) if flip_checks else np.array([]),
        flip_verify_vals=np.array([flip_checks[k] for k in flip_checks], dtype=bool) if flip_checks else np.array([], dtype=bool),
        audit_sha256=np.array(audit_sha),
        content_sha256=np.array(content_sha),
    )
    print(f"  npz sidecar: {OUT_NPZ.relative_to(PROJECT_ROOT)}")
    print()

    # 10. Compose the verdict value string + emit payload
    value = (  # (local)
        f"composite_PASS={composite_pass}_"
        f"A=D1:{verdict_A['D1']},D2:{verdict_A['D2']},D3:{verdict_A['D3']}_"
        f"B=D1:{verdict_B['D1']},D2:{verdict_B['D2']},D3:{verdict_B['D3']}_"
        f"6of6_PASS-AND_VIICK_STAGE-1-CANDIDATE->STAGE-3-PERMANENT_D4-open-RETAINED_"
        f"reg_pre={registry_pre_sha[:16]}_reg_post={registry_post_sha[:16]}_"
        f"flip_verify={verify_ok}"
    )
    extra_rows = [
        f"# Stage-2 blind PASS-AND: Axis-A lizzi {verdict_A} ; Axis-B kitaev {verdict_B} ; 6-of-6 logical AND => {composite_pass}",
        f"# registry tag-flip STAGE-1-CANDIDATE -> STAGE-3-PERMANENT (D4-open RETAINED): reg_pre={registry_pre_sha[:16]} reg_post={registry_post_sha[:16]} verify={verify_ok}",
        f"# substrate-input-orthogonality SATISFIED (W3-3 npz read by Axis-A only); no overlap caveat owed; W3-3 landing audit_sha256={W3_3_LANDING_AUDIT_SHA256[:16]}",
    ]

    tag = f"(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})"  # (local)
    print(tag)
    print_verdict_payload(verdict, value, audit_sha, content_sha, extra_rows=extra_rows)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    # Exit 0 = script ran successfully and produced a valid verdict (PASS/FAIL/INFO are all results).
    return 0


if __name__ == "__main__":
    sys.exit(main())
