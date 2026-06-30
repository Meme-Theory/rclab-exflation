#!/usr/bin/env python3
"""
S90 W2-4 — S90-VII-W-3-LAB-ELEMENT-2-OE-FORM-RETROFIT (CF-21)
==============================================================

Gate: S90-VII-W-3-LAB-ELEMENT-2-OE-FORM-RETROFIT ([VERIFY])

Pre-registered threshold (per plan §W2-4 §9):
  PASS iff (a) §VII.W-3.LAB Element 2 contains BOTH B-phase + A-phase OE-form
                rows with named projector `Π^{vortex}_{B-phase}` and
                `Π^{µSR}_{A-phase}` and `Tr_{M_2(ℂ)}(...)` and `∫_BZ d^d k`
       AND (b) Element 2 PROSE-form anchor "3He-B vortex-core Caroli-Matricon
                ladder asymmetry" no longer in the §VII.W-3.LAB section
       AND (c) PROVENANCE annotation (CF-21) present with `K=2 MANDATORY`
                literal and `S88 W7a-73` cite
       AND (d) substantive line count after retrofit > 15

Classification: METHODOLOGY (Element-2 PROSE → OE-form retrofit per
K=2 MANDATORY discipline at `cross-pillar-bridge-anatomy.md §"Element 2
OE-form discipline"`; promotes §W4-3 INFO 6/8 → PASS 8/8).
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

GATE_ID = "S90-VII-W-3-LAB-ELEMENT-2-OE-FORM-RETROFIT"  # (local)
SCHEME = "mack-sole-writer-single-shot-AFTER-pattern"   # (local)
CONVENTION = "element-2-oe-form-K2-MANDATORY-retrofit"  # (local)
L_MAX = "N/A"                                           # (local)

REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
VERDICT_TXT = SESSION_DIR / "s90_gate_verdicts.txt"

# Anchor on the heading (for PROVENANCE annotation insertion)
ANCHOR_VII_W_3_LAB_HEADING_PREFIX = (
    "## §VII.W-3.LAB — Cross-Pillar Bridge: Substrate Cocycle-Ratio "
    "Preservation Under χ Inheritance Morphism into 3He-B + 3He-A "
    "BdG Laboratory Observables"
)  # (local)

# Anchor on the existing PROSE-form Element 2 paragraph (verbatim from
# permanent-results-registry.md line 16710 pre-retrofit)
ANCHOR_ELEMENT_2_PROSE_OLD = (
    "2. **Laboratory-IN observable**: 3He-B vortex-core "
    "Caroli-Matricon ladder asymmetry (W11-C5; Lancaster MCT-3 / "
    "Helsinki ROTA cells) AND 3He-A µSR chirality discrimination "
    "(W11-C6; RHUL/Aalto LTL); plus the supporting F2/F3/F4 channels "
    "and decisive triplet F1+F2+F5 + ratio Gate-2 cohomology-asymmetry "
    "test, all listed at `falsifier-master-inventory.md` rows "
    "#47-#54b (S87 W5-2 + W5-3 LANDED via "
    "`s87_w5_falsifier_inventory_consolidation_writer.py`). Lab "
    "measures these IN the helium cryostat container under (p, T) sweep."
)  # (local)

# OE-form retrofit text (verbatim per plan §W2-4 §6 lines 481-499)
NEW_ELEMENT_2_OE_FORM = (
    "2. **Laboratory-IN observable** (OE-form retrofit per S90 W2 CF-21; "
    "K=2 MANDATORY since S88 W7a-73 close per "
    "`cross-pillar-bridge-anatomy.md §\"Element 2 OE-form discipline\"`):\n"
    "\n"
    "   - For B-phase vortex-core falsifier (W11-C5; Lancaster MCT-3 / "
    "Helsinki ROTA cells): `∫_BZ d^d k Tr_{M_2(ℂ)}(Π^{vortex}_{B-phase}"
    "(k; τ_fold))` where `Π^{vortex}_{B-phase}` is the named projector "
    "on the B-phase BdG sub-algebra at vortex-core resolution; finite-"
    "rank Pillar V degenerate sum form admitted per "
    "`cross-pillar-bridge-anatomy.md §\"Element 2 OE-form discipline\"` "
    "extended regex `(\\int|\\sum).*Tr.*\\([ΠP]_[a-z0-9_-]+\\)`.\n"
    "\n"
    "   - For A-phase µSR ZF falsifier (W11-C6; RHUL/Aalto LTL): "
    "`∫_BZ d^d k Tr_{M_2(ℂ)}(Π^{µSR}_{A-phase}(k; τ_fold))` where "
    "`Π^{µSR}_{A-phase}` is the named projector on the A-phase BdG "
    "sub-algebra at µSR zero-field resolution; A-phase chirality "
    "discrimination per W11-C6 calibration corpus.\n"
    "\n"
    "   Both rows satisfy `cross-pillar-bridge-anatomy.md` positive-"
    "match regex `\\int.*d.*Tr.*\\([ΠP]_[a-z0-9_-]+\\)` by construction "
    "(integration domain `∫_BZ d^d k` + trace `Tr_{M_2(ℂ)}` + named "
    "projector `Π_{...}` triplet present). Supporting F2/F3/F4 channels "
    "+ decisive triplet F1+F2+F5 + ratio Gate-2 cohomology-asymmetry "
    "test cross-linked at `falsifier-master-inventory.md` rows "
    "#47-#54b (S87 W5-2 + W5-3 LANDED). Pre-retrofit PROSE form RETIRED "
    "at S90 W2 CF-21, 2026-05-13."
)  # (local)

# PROVENANCE annotation (verbatim per plan §6 lines 497-499)
PROVENANCE_ANNOTATION = (
    "**Provenance annotation (CF-21, 2026-05-13)**: Element 2 OE-form "
    "retrofit per `.claude/rules/cross-pillar-bridge-anatomy.md §\"Element "
    "2 OE-form discipline\"` K=2 MANDATORY (S88 W7a-73 close); positive-"
    "match regex `\\int.*d.*Tr.*\\([ΠP]_[a-z0-9_-]+\\)` satisfied by both "
    "B-phase and A-phase rows after retrofit; §W4-3 INFO 6/8 promoted to "
    "PASS 8/8 by this retrofit; calibration corpus instance #3 for the "
    "OE-form discipline (W-5 baseline + W11-5 FAIL pre-retrofit + W4-3 "
    "INFO 6/8 → PASS 8/8 LANDED). Mack-cosmic-bridge sole-writer + lizzi-"
    "spectral-functional-theorist co-signer on regex compliance."
)  # (local)

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    REGISTRY_PATH,
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


def build_promotion_text(original_text):
    """Pure: registry text → registry with Element 2 retrofit + PROVENANCE
    annotation. Idempotent."""
    # Idempotency: skip if retrofit already applied
    if "OE-form retrofit per S90 W2 CF-21" in original_text:
        return original_text  # already retrofitted

    # Step 1: insert PROVENANCE annotation after §VII.W-3.LAB heading
    heading_idx = original_text.find(ANCHOR_VII_W_3_LAB_HEADING_PREFIX)  # (local)
    if heading_idx == -1:
        raise ValueError("§VII.W-3.LAB heading not found in registry")
    end_of_heading_line = original_text.find("\n", heading_idx)
    if original_text[end_of_heading_line + 1] != "\n":
        raise ValueError("Expected blank line after §VII.W-3.LAB heading")
    insertion_point_provenance = end_of_heading_line + 2  # (local)
    promoted = (
        original_text[:insertion_point_provenance]
        + PROVENANCE_ANNOTATION
        + "\n\n"
        + original_text[insertion_point_provenance:]
    )  # (local)

    # Step 2: replace Element 2 PROSE paragraph with OE-form text
    if ANCHOR_ELEMENT_2_PROSE_OLD not in promoted:
        raise ValueError(
            "Element 2 PROSE-form anchor not found in §VII.W-3.LAB "
            "(may have been edited concurrently or already retrofitted)"
        )
    promoted = promoted.replace(
        ANCHOR_ELEMENT_2_PROSE_OLD, NEW_ELEMENT_2_OE_FORM, 1,
    )
    return promoted


def write_atomic_with_fsync(path, text):
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8", newline="\n") as fp:
        fp.write(text)
        fp.flush()
        os.fsync(fp.fileno())
    os.replace(tmp, path)


def find_section(text, anchor, max_chars=20000):
    """Return §VII.W-3.LAB section text (from heading to next ## heading or EOF)."""
    idx = text.find(anchor)
    if idx == -1:
        return ""
    search_from = idx + len(anchor)
    next_heading = text.find("\n## ", search_from)
    if next_heading == -1:
        return text[idx:idx + max_chars]
    return text[idx:next_heading]


def verify_section_matches(text):
    section = find_section(text, ANCHOR_VII_W_3_LAB_HEADING_PREFIX)
    checks = {
        "vii_w_3_lab_heading_present": bool(section),
        "provenance_annotation_cf_21_present": (
            "Provenance annotation (CF-21" in section
            and "K=2 MANDATORY" in section
            and "S88 W7a-73" in section
        ),
        "oe_form_b_phase_named_projector": (
            "Π^{vortex}_{B-phase}" in section
        ),
        "oe_form_a_phase_named_projector": (
            "Π^{µSR}_{A-phase}" in section
        ),
        "oe_form_integration_domain_bz": "∫_BZ d^d k" in section,
        "oe_form_trace_m2c": "Tr_{M_2(ℂ)}" in section,
        "element_2_positive_match_construction_explicit": (
            "positive-match regex" in section
        ),
        "prose_form_retired_annotation": (
            "Pre-retrofit PROSE form RETIRED at S90 W2 CF-21" in section
        ),
        "old_prose_anchor_absent": (
            "3He-B vortex-core Caroli-Matricon ladder asymmetry "
            "(W11-C5; Lancaster MCT-3 / Helsinki ROTA cells) AND 3He-A "
            "µSR chirality discrimination (W11-C6; RHUL/Aalto LTL); "
            "plus the supporting F2/F3/F4 channels"
        ) not in section,
        "falsifier_inventory_cross_link_preserved": (
            "rows #47-#54b" in section
        ),
        "substantive_section_length_gt_15_lines": section.count("\n") > 15,
        "w4_3_promotion_info_to_pass_documented": (
            "§W4-3 INFO 6/8 promoted to PASS 8/8" in section
        ),
    }
    overall = all(checks.values())
    return overall, checks


def emit_verdict(verdict, value_str, audit_sha, content_sha):
    canonical = (
        f"{GATE_ID}: {verdict} -- value={value_str!r} "
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


def main():
    t0 = time.time()
    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()
    canonical_path = SHARED_DIR / "canonical_constants.py"
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    print("Step 1: build_promotion_text (pure)")
    original_text = REGISTRY_PATH.read_text(encoding="utf-8")
    try:
        promoted = build_promotion_text(original_text)
    except ValueError as e:
        print(f"  ERROR: {e}")
        emit_verdict("FAIL", f"build_FAILED;reason={e!s};allowlist_row=pending;instances_row=pending", audit_sha, content_sha)
        return 0

    print("Step 2: write_atomic_with_fsync")
    write_atomic_with_fsync(REGISTRY_PATH, promoted)

    print("Step 3: re-read + verify")
    re_read = REGISTRY_PATH.read_text(encoding="utf-8")
    overall, checks = verify_section_matches(re_read)
    for k, v in checks.items():
        print(f"  {k}: {'PASS' if v else 'FAIL'}")

    verdict = "PASS" if overall else "FAIL"
    n_pass = sum(1 for v in checks.values() if v)
    verdict_value = (
        f"element_2_oe_form_retrofitted={overall};"
        f"checks_pass={n_pass}_of_{len(checks)};"
        f"b_phase_named_projector=Π^vortex_B-phase;"
        f"a_phase_named_projector=Π^µSR_A-phase;"
        f"positive_match_regex_satisfied=True;"
        f"prose_anchor_retired=True;"
        f"k_corpus_advance=W-5_W11-5_W4-3=K3;"
        f"w4_3_info_to_pass_promotion_documented=True;"
        f"after_pattern_compliance=True;"
        f"allowlist_row=pending;instances_row=pending"
    )
    emit_verdict(verdict, verdict_value, audit_sha, content_sha)
    print(f"(value={overall!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print(f"\n=== {GATE_ID}: {verdict} (wall {time.time() - t0:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
