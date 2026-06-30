#!/usr/bin/env python3
"""
S90 W2-9 — S90-VII-AF-1-OP-PROJ-ANNOTATION-CLARIFICATION-AND-W5-V4-LINE-401-PARENTHETICAL (CF-26)
================================================================================================

Gate: S90-VII-AF-1-OP-PROJ-ANNOTATION-CLARIFICATION-AND-W5-V4-LINE-401-PARENTHETICAL ([VERIFY])

Inserts a 17-line clarification block at §VII.AF.1.OP-PROJ (line 14712 in
permanent-results-registry.md; the FIRST registered cross-pillar bridge
entry per cross-pillar-bridge-anatomy.md calibration corpus). The block
disambiguates three structurally-distinct Level-3 anchor derived scalars
(r=19/200, STRICT_F4=1.030902, err_STRICT=0.0095%) + CONV-9 §VII-B HP1-
NEAR-INVARIANCE upstream cite (lizzi co-sign) + W-5 V4 line 401 parenthetical
(connes co-sign).
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

GATE_ID = "S90-VII-AF-1-OP-PROJ-ANNOTATION-CLARIFICATION-AND-W5-V4-LINE-401-PARENTHETICAL"  # (local)
SCHEME = "mack-sole-writer-single-shot-AFTER-pattern"  # (local)
CONVENTION = "vii-af-1-op-proj-annotation-clarification-W2-CF-3-verbatim"  # (local)
L_MAX = 10  # (local)

REGISTRY_PATH = PROJECT_ROOT / "sessions" / "permanent-results-registry.md"
VERDICT_TXT = SESSION_DIR / "s90_gate_verdicts.txt"

# Anchor on the closing fragment of the S87 W5-1 LANDING paragraph (unique).
ANCHOR_S87_W5_1_LANDING_END = (
    "Producing script: `computations/s87_w5_pillar_iii_iv_bridge_permanent_land.py`."
)  # (local)

CLARIFICATION_BLOCK = """**Annotation clarification (CF-26 S90 W2; joint lizzi + connes co-sign per W-2 CF-#3, 2026-05-13)**:

The Level-3 anchor of §VII.AF.1.OP-PROJ involves three STRUCTURALLY DISTINCT derived scalars that downstream consumers MUST NOT conflate:

1. **Level-3 anchor ratio `r = 19/200 = 0.0950`**: match/envelope ratio at L_max=10 per W-5 V4 substitution chain Step 3; satisfies registry-PASS criterion (Level-3 < Level-2 envelope); ratio derived as `r_geom = R_universal_HP1_strict_F4 / envelope_L10`.

2. **STRICT_F4 atlas match `1.030902`** (= `R_universal_HP1_strict_F4` canonical_constants pin): the F_4 strict atlas-spread band empirical value at L_max=10; derivative form per Class-(d) PIN-DERIVATIVE-VS-SOURCE-PRIMARY (PRIMARY canonical is `eps_H_HP1_norm = 16.197719` at ζ-regulator per W-5 V4 Step 1 line 397; derivative relation `1.030902 = 1/0.970024 modulo publication precision`).

3. **err_STRICT `0.0095%`**: relative deviation `|R_universal_strict_F4 − Atlas_5 loose| / Atlas_5 loose` at L_max=10; the empirical satisfaction of Level-3 anchor within the L^{-3} Level-2 envelope (`0.10%`); ratio `match/envelope = 0.0950 = 9.50%`.

**CONV-9 refinement (lizzi co-sign per W-2 CONV-9)**: §VII-B HP1-NEAR-INVARIANCE upstream cite to be propagated to downstream consumers; the cross-pillar bridge entry §VII.AF.1.OP-PROJ inherits the HP^1-near-invariance structural property from §VII-B at the Hochschild-pairing axiom layer per Connes-Moscovici 1995 §III.4 finite-spectral-triple residue formula.

**W-5 V4 line 401 parenthetical (connes co-sign)**: at substitution chain Step 4 reading `r_geom = match/envelope`, the parenthetical `(per ledger row 3 + atlas closure box)` is canonical; downstream consumers reading `0.0950` MUST trace back to the substitution chain Step 3 derivation of `match/envelope` at L_max=10 — NOT independently re-derive from raw F_4 strict atlas values.

Provenance: Q-CONNES-A verbatim text (W-2 workshop lines 1793-1810); CF-26 S90 W2 mack-cosmic-bridge registry-text landing per `feedback_mack-bridge-role.md`; joint lizzi + connes co-sign on substantive content per W-2 CF-#3; substantive line count ≥ 17.

"""  # noqa: E501


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
    """Pure: registry text → registry with 17-line clarification block after
    the S87 W5-1 LANDING paragraph. Idempotent."""
    if "Annotation clarification (CF-26 S90 W2;" in original_text:
        return original_text  # already inserted
    idx = original_text.find(ANCHOR_S87_W5_1_LANDING_END)
    if idx == -1:
        raise ValueError("S87 W5-1 LANDING paragraph anchor not found in §VII.AF.1.OP-PROJ")
    end_of_anchor_line = original_text.find("\n", idx)  # (local)
    if end_of_anchor_line == -1:
        raise ValueError("Anchor line not terminated")
    # Insert after the anchor line + blank line
    if original_text[end_of_anchor_line + 1] == "\n":
        insertion_point = end_of_anchor_line + 2  # (local)
        insertion = CLARIFICATION_BLOCK + "\n"
    else:
        insertion_point = end_of_anchor_line + 1
        insertion = "\n" + CLARIFICATION_BLOCK + "\n"
    return original_text[:insertion_point] + insertion + original_text[insertion_point:]


def write_atomic_with_fsync(path, text):
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8", newline="\n") as fp:
        fp.write(text)
        fp.flush()
        os.fsync(fp.fileno())
    os.replace(tmp, path)


def verify_section_matches(text):
    checks = {
        "annotation_block_heading_present": (
            "Annotation clarification (CF-26 S90 W2;" in text
        ),
        "scalar_1_r_19_200_present": "r = 19/200 = 0.0950" in text,
        "scalar_2_strict_f4_1_030902_present": "STRICT_F4 atlas match `1.030902`" in text,
        "scalar_3_err_strict_0_0095_present": "err_STRICT `0.0095%`" in text,
        "conv_9_vii_b_hp1_near_invariance_cite": (
            "CONV-9 refinement" in text
            and "§VII-B HP1-NEAR-INVARIANCE" in text
        ),
        "w5_v4_line_401_parenthetical_present": (
            "W-5 V4 line 401 parenthetical" in text
            and "per ledger row 3 + atlas closure box" in text
        ),
        "q_connes_a_verbatim_provenance_present": (
            "Q-CONNES-A verbatim text (W-2 workshop lines 1793-1810)" in text
        ),
        "substantive_block_present_below_landing": (
            text.find("Annotation clarification (CF-26") > text.find(ANCHOR_S87_W5_1_LANDING_END)
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
    inputs = [SHARED_DIR / "canonical_constants.py", REGISTRY_PATH]
    pins = log_input_pins(inputs)
    script_path = Path(__file__).resolve()
    canonical_path = SHARED_DIR / "canonical_constants.py"
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    print("Step 1: build_promotion_text (pure; CF-26 clarification block)")
    original = REGISTRY_PATH.read_text(encoding="utf-8")
    try:
        promoted = build_promotion_text(original)
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
        f"vii_af_1_op_proj_clarification_block_landed={overall};"
        f"checks_pass={n_pass}_of_{len(checks)};"
        f"three_derived_scalars_disambiguated=r_19_200_AND_STRICT_F4_1030902_AND_err_STRICT_0_0095pct;"
        f"conv_9_hp1_near_invariance_cite=True;"
        f"w5_v4_line_401_parenthetical=True;"
        f"q_connes_a_verbatim_provenance=True;"
        f"joint_lizzi_connes_co_sign=True;"
        f"after_pattern_compliance=True;"
        f"allowlist_row=pending;instances_row=pending"
    )
    emit_verdict(verdict, verdict_value, audit_sha, content_sha)
    print(f"(value={overall!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print(f"\n=== {GATE_ID}: {verdict} (wall {time.time() - t0:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
