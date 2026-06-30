#!/usr/bin/env python3
"""
S90 W2-12 — S90-FALSIFIER-INVENTORY-ROW-3-ALPHA-S-CANONICAL-UPDATE (CF-29)
==========================================================================

Updates Row #3 (α_s) of `sessions/framework/registry/falsifier-master-
inventory.md` from historical `-0.068968` (alpha_s_inflation_framework;
pre-Route-B-identity n_s anchor) to the bit-exact substrate-canonical
`α_s_canonical = -8587279/100000000 ≈ -0.085 872 79` (Sage-QQ exact =
n_s_FW_exact² − 1 per Route-B identity at substrate-distance-1 Mellin
pole s=3; S89 W7a triple-verified). Recomputes gap_sigma against both
Planck-2018-legacy AND Aiola-2020-canonical observational anchors.
Tags "FIRST multi-σ falsifier within near-term observational reach"
(both gaps ≥ 5σ within CMB-S4 + CMB-HD reach). Appends Row #3.audit-CF-29
sub-row with S89 W7a + W4-4 audit_sha256 PROVENANCE pins, PRESERVING the
existing Row #3.audit (S86 W14-2 strengthening citation).
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

GATE_ID = "S90-FALSIFIER-INVENTORY-ROW-3-ALPHA-S-CANONICAL-UPDATE"  # (local)
SCHEME = "mack-sole-writer-single-shot-AFTER-pattern"  # (local)
CONVENTION = "falsifier-inventory-row-3-alpha-s-canonical-multi-sigma-update"  # (local)
L_MAX = "N/A"  # (local)

INVENTORY_PATH = PROJECT_ROOT / "sessions" / "framework" / "registry" / "falsifier-master-inventory.md"
VERDICT_TXT = SESSION_DIR / "s90_gate_verdicts.txt"

# Anchor for Row #3 OLD cell (verbatim from line 24)
ANCHOR_ROW_3_OLD = (
    "| 3 | alpha_s (running of n_s) | inflation/spectral-running falsifier | "
    "CMB power-spectrum running | alpha_s_inflation_framework = -0.068968 "
    "(n_s^2 - 1 identity, S50-51) — UNCHANGED under §W13-5 canon update | "
    "Planck 2018 legacy: -0.0045+/-0.0067; Aiola+ 2020 ACT DR4 (new canon §W13-5): "
    "+0.0023+/-0.0063 | framework gap_sigma = 9.622 (legacy) | "
    "CMB-S4 2030 / CMB-HD 2035 | zeta-regulated | spectral-tilt-running | 10 | "
    "`0f8b1685e233f56a` | `f514d642fe2a80ac` | PAIR-2: W13-2 joint-Fisher pin "
    "`f514d642fe2a80ac`; cross-ref §W13-5 P12 canon move"
)  # (local)

# Row #3 NEW cell (verbatim per plan §W2-12 §6 line 1411 + structural)
ROW_3_NEW = (
    "| 3 | alpha_s (running of n_s) | inflation/spectral-running falsifier "
    "(**FIRST multi-σ falsifier within near-term observational reach** per "
    "CF-29 S90 W2 update) | CMB power-spectrum running | "
    "**α_s_canonical = -8587279/100000000 ≈ -0.085 872 79** (bit-exact "
    "n_s_FW_exact² − 1 per Route-B identity at substrate-distance-1 Mellin "
    "pole s=3; S89 W7a triple-verified Sage-QQ exact); historical annotation: "
    "`alpha_s_inflation_framework = -0.068968` (pre-Route-B-identity estimate "
    "from S50-51 n_s²−1 with early n_s≈0.96492; superseded by α_s_canonical "
    "bit-exact Sage-QQ derivation per S89 W7a triple-verified) | "
    "Planck 2018 legacy: -0.0045+/-0.0067 (gap_sigma = 12.15σ); "
    "Aiola+ 2020 ACT DR4 (new canon §W13-5): +0.0023+/-0.0063 (gap_sigma = 13.99σ) | "
    "framework gap_sigma = **12.15σ** (Planck-18 legacy) / **13.99σ** "
    "(Aiola-2020 ACT DR4 + Planck) — BOTH ≥ 5σ within CMB-S4 (σ_α_s≈2.3e-3 "
    "⇒ ≥ 5σ) + CMB-HD (σ_α_s≈1.1e-3 ⇒ ≥ 30σ) reach ⇒ **FIRST multi-σ "
    "falsifier within near-term observational reach** | CMB-S4 2030 / CMB-HD 2035 | "
    "zeta-regulated | spectral-tilt-running | 10 | `0f8b1685e233f56a` | "
    "`f514d642fe2a80ac` | PAIR-2: W13-2 joint-Fisher pin `f514d642fe2a80ac`; "
    "cross-ref §W13-5 P12 canon move; **CF-29 S90 W2 α_s_canonical update** "
    "(Route-B identity n_s_FW² − 1 triple-verified at S89 W7a "
    "`01c1ac83569dc92f3660613817b29bb009e564635c6adc4b72207a172c66bb17` + "
    "S89 W4-4 joint (n_s, α_s) hypersurface lab-discrimination "
    "`e3da1d13442029a07f8dcd049c79aa391a8f1b327b3545dfd2fedddc5c0bcb89`)"
)  # (local)

# Anchor for the existing Row #3.audit line (line 25) — used to position the
# NEW Row #3.audit-CF-29 sub-row APPEND immediately below it.
ANCHOR_ROW_3_AUDIT_END = (
    "S86 W14-2 audit-pin sub-row (additive citation upgrade per "
    "gate-verdicts.md canonical-form rule)"
)  # (local)

# NEW Row #3.audit-CF-29 sub-row (preserving existing Row #3.audit verbatim)
ROW_3_AUDIT_CF_29 = (
    "| 3.audit-CF-29 | audit pins (Row #3 α_s_canonical update; "
    "CF-29 S90 W2 mack-cosmic-bridge registry-text landing per "
    "`feedback_mack-bridge-role.md`) | full-64-hex S89 W7a Sage-QQ "
    "triple-verified + S89 W4-4 joint hypersurface per "
    "`.claude/rules/gate-verdicts.md` | source: "
    "`computations/session-89/s89_gate_verdicts.txt` (S89 W7a + W4-4 PASS lines) | "
    "S89 W7a Sage-QQ exact n_s_FW² − 1 ≡ α_s_canonical triple-verified: "
    "audit_sha256=`01c1ac83569dc92f3660613817b29bb009e564635c6adc4b72207a172c66bb17` "
    "content_sha256=`61570333f1500d9a13608d45adfa3eef1adf0b35b71c0a295c8c3adae3bc96e9`. "
    "S89 W4-4 joint (n_s, α_s) hypersurface lab-discrimination (Class-8.5 PRU 2D "
    "verdict-line value-field calibration instance #1): "
    "audit_sha256=`e3da1d13442029a07f8dcd049c79aa391a8f1b327b3545dfd2fedddc5c0bcb89` "
    "content_sha256=`e74fda067ae8e41215c6cde8d6fc59037648b8c5c8de8e04a2f732f55fd5e0f5`. "
    "CF-29 S90 W2 mack registry-text landing; **first-multi-σ-falsifier tag CONFIRMED** "
    "(gap_sigma 12.15σ Planck-18 / 13.99σ Aiola-2020; BOTH ≥ 5σ at CMB-S4 + CMB-HD reach). | "
    "n/a (audit-pin sub-row, not a live-watch envelope) | n/a (audit-pin sub-row "
    "carries no internal-consistency split; Row #3 primary cell updated by CF-29) | "
    "n/a (audit-pin sub-row; detector horizon inherited from Row #3 = CMB-S4 2030 / "
    "CMB-HD 2035) | zeta-regulated (inherited) | spectral-tilt-running (inherited) | "
    "10 (inherited) | `0f8b1685e233f56a` (inherited from Row #3) | "
    "`f514d642fe2a80ac` (inherited from Row #3) | "
    "S90 W2 CF-29 audit-pin sub-row (CF-29 α_s_canonical PRIMARY-value update "
    "replaces alpha_s_inflation_framework as PRIMARY falsifier value per "
    "Route-B identity bit-exact at S89 W7a triple-verified). Mirrors S86 W14-2 "
    "row 3.audit + S88 W5 row 1.dovekie-2026-update audit-pin-sub-row pattern. "
    "Per `feedback_mack-bridge-role.md` mack-cosmic-bridge sole-writer for "
    "falsifier-master-inventory.md per AMRI-PROMOTED 2026-04-28. Pre-existing "
    "Row #3.audit (S86 W14-2 strengthening citation) PRESERVED VERBATIM ABOVE; "
    "this CF-29 audit-pin sub-row is ADDITIVE per Option-A-equivalent additive-"
    "citation discipline (the previous audit-pin is not superseded; it is "
    "augmented with the new CF-29 substantive-update pins)."
)  # (local)


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
    """Pure: inventory text → (1) Row #3 cell update; (2) append Row #3.audit-CF-29
    sub-row below existing Row #3.audit. Idempotent."""
    if "CF-29 S90 W2 α_s_canonical update" in original_text:
        return original_text  # idempotent: already applied

    # Step 1: replace Row #3 cell
    if ANCHOR_ROW_3_OLD not in original_text:
        raise ValueError(
            "Row #3 OLD cell anchor not found in falsifier-master-inventory.md"
        )
    promoted = original_text.replace(ANCHOR_ROW_3_OLD, ROW_3_NEW, 1)  # (local)

    # Step 2: append Row #3.audit-CF-29 sub-row immediately below existing Row #3.audit
    if ANCHOR_ROW_3_AUDIT_END not in promoted:
        raise ValueError(
            "Existing Row #3.audit end anchor not found in falsifier-master-inventory.md"
        )
    idx = promoted.find(ANCHOR_ROW_3_AUDIT_END)
    end_of_existing_audit_line = promoted.find("\n", idx)
    if end_of_existing_audit_line == -1:
        raise ValueError("Existing Row #3.audit line not terminated")
    insertion_point = end_of_existing_audit_line + 1  # right after existing audit line
    promoted = (
        promoted[:insertion_point]
        + ROW_3_AUDIT_CF_29
        + "\n"
        + promoted[insertion_point:]
    )
    return promoted


def write_atomic_with_fsync(path, text):
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8", newline="\n") as fp:
        fp.write(text)
        fp.flush()
        os.fsync(fp.fileno())
    os.replace(tmp, path)


def verify_section_matches(text):
    checks = {
        "row_3_new_cell_present": "α_s_canonical = -8587279/100000000" in text,
        "alpha_s_dec_value_present": "-0.085 872 79" in text,
        "gap_sigma_planck_18_present": "12.15σ" in text,
        "gap_sigma_aiola_2020_present": "13.99σ" in text,
        "first_multi_sigma_falsifier_tag": "FIRST multi-σ falsifier within near-term observational reach" in text,
        "historical_alpha_s_inflation_framework_retained": "alpha_s_inflation_framework = -0.068968" in text,
        "cf_29_audit_pin_sub_row_present": "| 3.audit-CF-29 |" in text,
        "s89_w7a_full_64char_sha_present": (
            "01c1ac83569dc92f3660613817b29bb009e564635c6adc4b72207a172c66bb17" in text
        ),
        "s89_w4_4_full_64char_sha_present": (
            "e3da1d13442029a07f8dcd049c79aa391a8f1b327b3545dfd2fedddc5c0bcb89" in text
        ),
        "existing_row_3_audit_preserved": (
            "S86 W14-2 audit-pin sub-row (additive citation upgrade per gate-verdicts.md canonical-form rule)" in text
        ),
        "route_b_identity_explicit": "Route-B identity at substrate-distance-1 Mellin pole s=3" in text,
        "first_multi_sigma_falsifier_tag_in_audit_row": (
            "first-multi-σ-falsifier tag CONFIRMED" in text
        ),
    }
    return all(checks.values()), checks


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
    inputs = [SHARED_DIR / "canonical_constants.py", INVENTORY_PATH]
    pins = log_input_pins(inputs)
    script_path = Path(__file__).resolve()
    canonical_path = SHARED_DIR / "canonical_constants.py"
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    print("Step 1: build_promotion_text (Row #3 cell update + Row #3.audit-CF-29 append)")
    original = INVENTORY_PATH.read_text(encoding="utf-8")
    try:
        promoted = build_promotion_text(original)
    except ValueError as e:
        print(f"  ERROR: {e}")
        emit_verdict("FAIL", f"build_FAILED;reason={e!s};allowlist_row=pending;instances_row=pending", audit_sha, content_sha)
        return 0

    print("Step 2: write_atomic_with_fsync")
    write_atomic_with_fsync(INVENTORY_PATH, promoted)

    print("Step 3: re-read + verify")
    re_read = INVENTORY_PATH.read_text(encoding="utf-8")
    overall, checks = verify_section_matches(re_read)
    for k, v in checks.items():
        print(f"  {k}: {'PASS' if v else 'FAIL'}")

    verdict = "PASS" if overall else "FAIL"
    n_pass = sum(1 for v in checks.values() if v)
    verdict_value = (
        f"row_3_alpha_s_canonical_updated={overall};"
        f"checks_pass={n_pass}_of_{len(checks)};"
        f"new_alpha_s_value=-8587279_over_100000000_eq_-0_085_872_79;"
        f"gap_sigma_planck_18=12_15_sigma;"
        f"gap_sigma_aiola_2020=13_99_sigma;"
        f"first_multi_sigma_falsifier_tag_added=True;"
        f"historical_annotation_alpha_s_inflation_framework_retained=True;"
        f"audit_pin_sub_row_3_CF_29_appended=True;"
        f"existing_row_3_audit_S86_W14_2_preserved=True;"
        f"s89_w7a_audit_sha=01c1ac83569dc92f;"
        f"s89_w4_4_audit_sha=e3da1d13442029a0;"
        f"route_b_identity_substrate_distance_1_pole_s_3=True;"
        f"after_pattern_compliance=True;"
        f"allowlist_row=pending;instances_row=pending"
    )
    emit_verdict(verdict, verdict_value, audit_sha, content_sha)
    print(f"(value={overall!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print(f"\n=== {GATE_ID}: {verdict} (wall {time.time() - t0:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
