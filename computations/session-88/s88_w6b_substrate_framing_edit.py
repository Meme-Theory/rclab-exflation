#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
S88 W6b §W6b-55 — S88-VII-U-6-SUBSTRATE-FRAMING-EDIT
======================================================

METHODOLOGY-class registry-edit gate. Edits §VII.U.6 substrate-framing prose
to satisfy `.claude/rules/phononic-framing.md` §"IS Space, Not IN Space —
Mandatory Reframe" via two targeted substitutions:

  Edit 1 (W6b-53 duplication fix; substantive in-session correction per
  `feedback_fix-in-session-never-defer.md`):
    BEFORE: "...both readings sit deep inside Zubarev's strip, deep inside
              Zubarev's strip. T5's Regime I admissibility..."
    AFTER:  "...both readings sit deep inside Zubarev's strip. T5's Regime I
              admissibility..."

  Edit 2 (substrate-framing literal-phrase augmentation):
    BEFORE: existing §"Substrate framing" sub-section (lines 13102-13111;
              already substrate-IS-compliant in spirit, but lacks the literal
              required phrases per plan §W6b-55 grep PASS criterion)
    AFTER:  same content + appended paragraph containing all 3 required
              literal phrases per plan:
              - "the substrate IS the spectral triple"
              - "d_spec_B = 5/(1−τ/(5π)) is the τ-flow-tracked Weyl-counting EXPONENT"
              - "bare manifold dim = 8 (HK-3 asymptotic binding)"

Single-shot AFTER pattern per `.claude/rules/registry-landing.md`.

Plan reference: sessions/session-plan/session-88-plan-w6b.md §W6b-55.

Verification (per plan PASS criterion):
  Forbidden phrase set (5 patterns) = 0 each in §VII.U.6
    - "d_spec=8 NCG cone apex"
    - "the substrate sits at"
    - "the substrate lives at"
    - "the substrate is located in"
    - "dimensional cone in NCG"
  Required phrase set (3 patterns) ≥ 1 each in §VII.U.6
    - "bare manifold dim = 8 (HK-3 asymptotic binding)"
    - "the substrate IS the spectral triple"
    - "d_spec_B = 5/(1−τ/(5π)) is the τ-flow-tracked Weyl-counting EXPONENT"
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
from pathlib import Path

# Canonical constants import (mandatory per .claude/rules/math-scripts.md)
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "_shared"))
from canonical_constants import tau_fold  # S12/S42 canonical fold parameter

GATE_ID = "S88-VII-U-6-SUBSTRATE-FRAMING-EDIT"
SCHEME = "substrate-IS-reframe"
CONVENTION = "phononic-framing-IS-not-IN"
L_MAX = "N/A"
SCHEMA = "S84+"
REGULATOR = "Zubarev"

REGISTRY_PATH = Path("sessions/permanent-results-registry.md")
VERDICT_PATH = Path("computations/session-88/s88_gate_verdicts.txt")

# §VII.U.6 line bounds (from plan + corrected via grep)
VII_U_6_LINE_START = 12988  # (local) ### §VII.U.6 anchor
VII_U_6_LINE_END = 13141    # (local) before §VII.K-META.COMPOSITE-60

# Plan §W6b-55 forbidden phrase set (5 patterns; verify all = 0 post-edit)
FORBIDDEN_PHRASES = [
    "d_spec=8 NCG cone apex",
    "the substrate sits at",
    "the substrate lives at",
    "the substrate is located in",
    "dimensional cone in NCG",
]

# Plan §W6b-55 required phrase set (3 patterns; verify all ≥ 1 post-edit)
REQUIRED_PHRASES = [
    "bare manifold dim = 8 (HK-3 asymptotic binding)",
    "the substrate IS the spectral triple",
    "d_spec_B = 5/(1−τ/(5π)) is the τ-flow-tracked Weyl-counting EXPONENT",
]

# ---------------------------------------------------------------------------
# Edit 1: W6b-53 duplication fix (substantive in-session correction)
# ---------------------------------------------------------------------------
EDIT_1_FORBIDDEN = (
    "both readings sit deep inside Zubarev's strip, deep inside Zubarev's strip"
)
EDIT_1_REPLACEMENT = (
    "both readings sit deep inside Zubarev's strip"
)

# ---------------------------------------------------------------------------
# Edit 2: Substrate framing augmentation (insert all 3 required phrases)
# ---------------------------------------------------------------------------
# Match the existing §"Substrate framing" sub-section closing line + insert
# new paragraph immediately after.
EDIT_2_FORBIDDEN = (
    "##### Substrate framing (per `.claude/rules/phononic-framing.md`)\n"
    "\n"
    "The Mellin-Strip residue at s=3 IS a substrate-IS observable on the finite\n"
    "spectral triple `(A_K^{<=10}, H_K^{<=10}, D_K^{<=10})` -- not a quantity\n"
    "\"living in\" an external s-plane geometry.  The continuum strip integral is\n"
    "the laboratory-IN observable on a different platform (laboratory's\n"
    "instantiation of `D_K`).  The bridge map flows: substrate -> HKR\n"
    "`L_max -> inf` image -> laboratory.  The s-plane structure is an emergent\n"
    "description of how the substrate's spectral weight at substrate-distance-1\n"
    "distributes itself."
)

EDIT_2_REPLACEMENT = (
    "##### Substrate framing (per `.claude/rules/phononic-framing.md`)\n"
    "\n"
    "The Mellin-Strip residue at s=3 IS a substrate-IS observable on the finite\n"
    "spectral triple `(A_K^{<=10}, H_K^{<=10}, D_K^{<=10})` -- not a quantity\n"
    "\"living in\" an external s-plane geometry.  The continuum strip integral is\n"
    "the laboratory-IN observable on a different platform (laboratory's\n"
    "instantiation of `D_K`).  The bridge map flows: substrate -> HKR\n"
    "`L_max -> inf` image -> laboratory.  The s-plane structure is an emergent\n"
    "description of how the substrate's spectral weight at substrate-distance-1\n"
    "distributes itself.\n"
    "\n"
    "Further (S88 W6b-55 substrate-framing landing per `.claude/rules/phononic-framing.md`\n"
    "§\"IS Space, Not IN Space — Mandatory Reframe\"): the substrate IS the spectral triple\n"
    "`(A_K, H_K, D_K)` — not embedded in any container. The Conv-B canonical\n"
    "`d_spec_B = 5/(1−τ/(5π)) is the τ-flow-tracked Weyl-counting EXPONENT` of the\n"
    "Jensen-deformed D_can (an emergent spectral asymptotic property of the substrate,\n"
    "intrinsic to the spectral triple's finite-L convergence to the L → ∞ HKR image);\n"
    "bare manifold dim = 8 (HK-3 asymptotic binding) is the substrate's bare-D Weyl\n"
    "asymptotic exponent, NOT a spatial-container dimension. The substrate is not IN\n"
    "any 8-dimensional NCG cone; the substrate IS all there is at the fiber level."
)


def read_registry() -> str:
    with open(REGISTRY_PATH, "r", encoding="utf-8") as fh:
        return fh.read()


def slice_section(text: str, line_start: int, line_end: int) -> str:
    lines = text.split("\n")
    return "\n".join(lines[line_start - 1:line_end])


def grep_count(text: str, pattern: str) -> int:
    return text.count(pattern)


def build_promotion_text(original: str) -> str:
    """Apply Edit 1 (duplication fix) + Edit 2 (substrate-framing augmentation),
    both targeted in §VII.U.6 region with uniqueness verification.
    """
    # Edit 1 verification
    n_edit1 = grep_count(original, EDIT_1_FORBIDDEN)
    if n_edit1 != 1:
        raise RuntimeError(
            f"Expected 1 occurrence of EDIT_1_FORBIDDEN; got {n_edit1}"
        )
    # Edit 2 verification
    n_edit2 = grep_count(original, EDIT_2_FORBIDDEN)
    if n_edit2 != 1:
        raise RuntimeError(
            f"Expected 1 occurrence of EDIT_2_FORBIDDEN; got {n_edit2}"
        )
    promoted = original.replace(EDIT_1_FORBIDDEN, EDIT_1_REPLACEMENT, 1)
    promoted = promoted.replace(EDIT_2_FORBIDDEN, EDIT_2_REPLACEMENT, 1)
    return promoted


def write_atomic_with_fsync(text: str, path: Path) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp_w6b_55")
    with open(tmp, "w", encoding="utf-8") as fh:
        fh.write(text)
        fh.flush()
        os.fsync(fh.fileno())
    os.replace(tmp, path)


def closure_hash(input_pin_map: dict) -> str:
    canonical = json.dumps(input_pin_map, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def emit_verdict_line(verdict, value, audit_sha, content_sha):
    canonical = (
        f"{GATE_ID}: {verdict} -- value='{value}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version={SCHEMA}\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    VERDICT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(VERDICT_PATH, "a", encoding="utf-8") as fh:
        fh.write(canonical)
        fh.write(companion)


def main() -> int:
    original = read_registry()

    # Pre-edit grep counts
    vii_u_6 = slice_section(original, VII_U_6_LINE_START, VII_U_6_LINE_END)

    pre_forbidden = {p: grep_count(vii_u_6, p) for p in FORBIDDEN_PHRASES}
    pre_required = {p: grep_count(vii_u_6, p) for p in REQUIRED_PHRASES}
    pre_edit1 = grep_count(original, EDIT_1_FORBIDDEN)

    print("PRE-EDIT GREP (in §VII.U.6 lines 12988-13141):")
    print("  Forbidden phrases:")
    for p, c in pre_forbidden.items():
        marker = "✓" if c == 0 else "FAIL"
        print(f"    {marker} '{p[:60]}...': {c}")
    print("  Required phrases:")
    for p, c in pre_required.items():
        marker = "✓" if c >= 1 else "MISSING"
        print(f"    {marker} '{p[:60]}...': {c}")
    print(f"  W6b-53-introduced duplication 'deep inside Zubarev's strip, deep inside Zubarev's strip': {pre_edit1} (target = 1 to fix)")
    print()

    # IDEMPOTENCY DETECTION
    all_forbidden_zero = all(c == 0 for c in pre_forbidden.values())
    all_required_present = all(c >= 1 for c in pre_required.values())
    no_duplication = pre_edit1 == 0
    if all_forbidden_zero and all_required_present and no_duplication:
        print("IDEMPOTENT: registry already shows post-edit state; verdict INFO.")
        info_value = (
            f"idempotent_no_edit;forbidden_all_zero=True;required_all_geq_1=True;"
            f"duplication_already_fixed=True"
        )
        content_sha = file_sha256(REGISTRY_PATH)
        input_pin_map = {
            "gate_id": GATE_ID, "branch": "idempotent_no_edit",
            "tau_fold": tau_fold,
        }
        audit_sha = closure_hash(input_pin_map)
        emit_verdict_line("INFO", info_value, audit_sha, content_sha)
        print(f"VERDICT: INFO -- value={info_value}")
        return 0

    # Build promotion text (Edit 1 + Edit 2)
    promoted = build_promotion_text(original)

    # Write atomic + fsync
    write_atomic_with_fsync(promoted, REGISTRY_PATH)

    # Re-read + verify
    actual = read_registry()
    matches = (actual == promoted)

    # Post-edit grep (on disk)
    vii_u_6_post = slice_section(actual, VII_U_6_LINE_START, VII_U_6_LINE_END + 16)  # +16 for line drift from Edit 2 paragraph addition
    post_forbidden = {p: grep_count(vii_u_6_post, p) for p in FORBIDDEN_PHRASES}
    post_required = {p: grep_count(vii_u_6_post, p) for p in REQUIRED_PHRASES}
    post_edit1 = grep_count(actual, EDIT_1_FORBIDDEN)

    print("POST-EDIT GREP (in §VII.U.6 expanded for line-drift):")
    print("  Forbidden phrases:")
    for p, c in post_forbidden.items():
        marker = "✓" if c == 0 else "FAIL"
        print(f"    {marker} '{p[:60]}...': {c}")
    print("  Required phrases:")
    for p, c in post_required.items():
        marker = "✓" if c >= 1 else "MISSING"
        print(f"    {marker} '{p[:60]}...': {c}")
    print(f"  W6b-53 duplication remaining: {post_edit1} (target = 0)")
    print(f"  verify match (strict eq):     {matches}")
    print()

    pass_predicate = (
        matches
        and all(c == 0 for c in post_forbidden.values())
        and all(c >= 1 for c in post_required.values())
        and post_edit1 == 0
    )
    verdict = "PASS" if pass_predicate else "FAIL"

    forbidden_summary = ";".join(f"{p[:30]}={c}" for p, c in post_forbidden.items())
    required_summary = ";".join(f"{p[:30]}={c}" for p, c in post_required.items())
    value_str = (
        f"forbidden_post_edit_all_zero={all(c==0 for c in post_forbidden.values())};"
        f"required_post_edit_all_geq_1={all(c>=1 for c in post_required.values())};"
        f"w6b_53_duplication_fixed={post_edit1 == 0};"
        f"edit_1_duplication_fix_applied={pre_edit1 == 1};"
        f"edit_2_substrate_framing_paragraph_appended=True"
    )

    content_sha = file_sha256(REGISTRY_PATH)
    input_pin_map = {
        "gate_id": GATE_ID,
        "registry_path": str(REGISTRY_PATH),
        "vii_u_6_lines_pre_edit": [VII_U_6_LINE_START, VII_U_6_LINE_END],
        "edit_1_forbidden_sha": hashlib.sha256(EDIT_1_FORBIDDEN.encode("utf-8")).hexdigest(),
        "edit_1_replacement_sha": hashlib.sha256(EDIT_1_REPLACEMENT.encode("utf-8")).hexdigest(),
        "edit_2_forbidden_sha": hashlib.sha256(EDIT_2_FORBIDDEN.encode("utf-8")).hexdigest(),
        "edit_2_replacement_sha": hashlib.sha256(EDIT_2_REPLACEMENT.encode("utf-8")).hexdigest(),
        "forbidden_phrases_count": len(FORBIDDEN_PHRASES),
        "required_phrases_count": len(REQUIRED_PHRASES),
        "tau_fold": tau_fold,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "regulator": REGULATOR,
        "schema_version": SCHEMA,
    }
    audit_sha = closure_hash(input_pin_map)
    emit_verdict_line(verdict, value_str, audit_sha, content_sha)

    print(f"VERDICT: {verdict} -- value={value_str}")
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")

    sidecar = Path("computations/session-88/s88_w6b_substrate_framing_edit.json")
    sidecar.write_text(json.dumps({
        "gate_id": GATE_ID, "verdict": verdict, "value": value_str,
        "audit_sha256": audit_sha, "content_sha256": content_sha,
        "scheme": SCHEME, "convention": CONVENTION, "L_max": L_MAX,
        "regulator": REGULATOR, "schema_version": SCHEMA,
        "pre_edit_grep": {"forbidden": pre_forbidden, "required": pre_required,
                          "w6b_53_duplication": pre_edit1},
        "post_edit_grep": {"forbidden": post_forbidden, "required": post_required,
                           "w6b_53_duplication": post_edit1},
    }, indent=2), encoding="utf-8")
    print(f"  sidecar: {sidecar}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
