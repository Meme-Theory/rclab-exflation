#!/usr/bin/env python3
"""
S88 W2-10 — S88-PHONONIC-FRAMING-MODULI-DEFORMATION-EXTENSION
==============================================================

Gate: S88-PHONONIC-FRAMING-MODULI-DEFORMATION-EXTENSION (trigger: AUDIT)
Wave: W2 (METHODOLOGY-class rule-file diff to phononic-framing.md)
Plan: sessions/session-plan/session-88-plan-w2.md §W2-10

Pre-registered threshold (per session-88-plan-w2.md §W2-10.9):
  PASS: rule-file diff lands at correct insertion point; new sub-section ≥30 lines;
        calibration corpus block present (W-8 R3 + W-2 §VII.U.2 OR equivalent);
        methodology-wave-allowlist row appended.
  INFO: partial.
  FAIL: rule-file diff at wrong location; sub-section <15 lines; allowlist missing.
"""

from __future__ import annotations

# Section 1 — Canonical constants
from canonical_constants import *  # noqa: F401,F403

# Section 2 — Imports
import hashlib
import json
import time
from pathlib import Path

# Section 3 — Pin metadata
GATE_ID = "S88-PHONONIC-FRAMING-MODULI-DEFORMATION-EXTENSION"
SCHEME = "phononic-framing-two-level-substrate-IS-extension"
CONVENTION = "level-1-single-tau-slice-vs-level-2-moduli-deformation"
L_MAX = "N/A"
LINE_THRESHOLD_PASS = 30  # (local) plan-pinned ≥30 lines new sub-section criterion

T0 = Path(__file__).resolve().parent
SCRIPT_PATH = T0 / "s88_w2_phononic_framing_moduli_deformation_extension.py"
NPZ_OUT = T0 / "s88_w2_phononic_framing_moduli_deformation_extension.npz"
VERDICT_FILE = T0 / "s88_gate_verdicts.txt"

PHONONIC_FRAMING = T0.parent / ".claude" / "rules" / "phononic-framing.md"
ALLOWLIST_PATH = T0.parent / ".claude" / "rules" / "methodology-wave-allowlist.md"
CANON_PY = T0 / "canonical_constants.py"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(pin_map: dict) -> str:
    canon = json.dumps(pin_map, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()


def count_section_lines(file_path: Path, start_anchor: str, end_anchor: str) -> int:
    text = file_path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()
    in_section = False
    count = 0  # (local)
    for line in lines:
        if start_anchor in line:
            in_section = True
            continue
        if in_section and end_anchor in line:
            break
        if in_section:
            count += 1
    return count


def main() -> int:
    t_start = time.time()
    import numpy as np

    pf_text = PHONONIC_FRAMING.read_text(encoding="utf-8", errors="replace")
    sub_section_line_count = count_section_lines(
        PHONONIC_FRAMING,
        "## Single-τ-slice vs moduli-deformation substrate-IS levels",
        "## Cross-pillar bridge anatomy",
    )
    print(f"[W2-10] new sub-section line count: {sub_section_line_count}")

    cc1_insertion_correct = "## Single-τ-slice vs moduli-deformation substrate-IS levels" in pf_text and pf_text.index("## Single-τ-slice") < pf_text.index("## Cross-pillar bridge anatomy")
    cc2_level1_present = "Level 1 — Single-τ-slice substrate-IS" in pf_text
    cc3_level2_present = "Level 2 — Moduli-deformation substrate-IS" in pf_text
    cc4_calibration_corpus = "calibration corpus" in pf_text and ("§VII.AE" in pf_text or "§VII.AJ.partition-stability" in pf_text)
    cc5_w8_r3_provenance = "W-8 R3 closure" in pf_text or "S87 W-8 R3" in pf_text
    cc6_orthogonality_xref = "algebra-axis orthogonality K-counter" in pf_text
    cc7_forward_enforcement = "Forward-looking enforcement" in pf_text and "5-anatomy" in pf_text

    print(f"[W2-10] CC1 insertion correct (between IS Space and Cross-pillar): {cc1_insertion_correct}")
    print(f"[W2-10] CC2 Level 1 sub-block present: {cc2_level1_present}")
    print(f"[W2-10] CC3 Level 2 sub-block present: {cc3_level2_present}")
    print(f"[W2-10] CC4 calibration corpus block present: {cc4_calibration_corpus}")
    print(f"[W2-10] CC5 W-8 R3 provenance block: {cc5_w8_r3_provenance}")
    print(f"[W2-10] CC6 cross-link to algebra-axis orthogonality K-counter: {cc6_orthogonality_xref}")
    print(f"[W2-10] CC7 Forward-looking enforcement clause: {cc7_forward_enforcement}")

    allowlist_text = ALLOWLIST_PATH.read_text(encoding="utf-8", errors="replace")
    cc8_allowlist = "| W2-10 | S88 |" in allowlist_text
    print(f"[W2-10] CC8 methodology-wave-allowlist W2-10 row: {cc8_allowlist}")

    all_cc_pass = (
        cc1_insertion_correct and cc2_level1_present and cc3_level2_present
        and cc4_calibration_corpus and cc5_w8_r3_provenance
        and cc6_orthogonality_xref and cc7_forward_enforcement and cc8_allowlist
        and sub_section_line_count >= LINE_THRESHOLD_PASS
    )
    if all_cc_pass:
        composite = "PASS"
        verdict_kind = "PASS-rule-file-diff-landed-with-two-level-distinction"
    elif sub_section_line_count >= 15 and not all_cc_pass:
        composite = "INFO"
        verdict_kind = "INFO-partial-some-cross-checks-failed"
    else:
        composite = "FAIL"
        verdict_kind = "FAIL-rule-file-diff-incomplete"

    canon_sha = sha256_file(CANON_PY)
    pf_sha = sha256_file(PHONONIC_FRAMING)
    allowlist_sha = sha256_file(ALLOWLIST_PATH)
    script_sha = sha256_file(SCRIPT_PATH)
    content_sha256 = script_sha
    pin_map = {
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "input_canonical_constants_sha256": canon_sha,
        "input_phononic_framing_sha256": pf_sha,
        "input_allowlist_sha256": allowlist_sha,
        "script_sha256": script_sha,
    }
    audit_sha256 = closure_hash(pin_map)

    np.savez(
        NPZ_OUT,
        sub_section_line_count=np.int64(sub_section_line_count),
        cc1_insertion=np.bool_(cc1_insertion_correct),
        cc2_level1=np.bool_(cc2_level1_present),
        cc3_level2=np.bool_(cc3_level2_present),
        cc4_calibration=np.bool_(cc4_calibration_corpus),
        cc5_provenance=np.bool_(cc5_w8_r3_provenance),
        cc6_orthogonality=np.bool_(cc6_orthogonality_xref),
        cc7_enforcement=np.bool_(cc7_forward_enforcement),
        cc8_allowlist=np.bool_(cc8_allowlist),
        composite=composite,
        verdict_kind=verdict_kind,
        audit_sha256=audit_sha256,
        content_sha256=content_sha256,
    )

    elapsed = time.time() - t_start
    value_str = (
        f"sub_section_line_count={sub_section_line_count};"
        f"cc1_insertion={cc1_insertion_correct};cc2_level1={cc2_level1_present};"
        f"cc3_level2={cc3_level2_present};cc4_calibration={cc4_calibration_corpus};"
        f"cc5_provenance={cc5_w8_r3_provenance};cc6_orthogonality={cc6_orthogonality_xref};"
        f"cc7_enforcement={cc7_forward_enforcement};cc8_allowlist={cc8_allowlist};"
        f"verdict_kind={verdict_kind}"
    )
    canonical_line = (
        f"{GATE_ID}: {composite} -- value='{value_str}' "
        f"scheme={SCHEME} convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha256} content_sha256={content_sha256} schema_version=S87+\n"
    )
    companion_line = (
        f"# audit_sha256_short={audit_sha256[:16]} "
        f"content_sha256_short={content_sha256[:16]} "
        f"# {GATE_ID} dual-SHA companion row (W9a-99 split)\n"
    )
    sign_v = "N/A"
    mag_v = composite
    regime_v = "VALID"
    tuple_line = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} "
        f"regime_verdict={regime_v} # {GATE_ID} 3-tuple annotation (S87 schema-v2)\n"
    )

    with open(VERDICT_FILE, "a", encoding="utf-8") as f:
        f.write(canonical_line)
        f.write(companion_line)
        f.write(tuple_line)

    print(f"[W2-10] DONE in {elapsed:.2f}s")
    print(f"[W2-10] composite = {composite} (verdict_kind={verdict_kind})")
    print(f"[W2-10] audit_sha256 = {audit_sha256}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
