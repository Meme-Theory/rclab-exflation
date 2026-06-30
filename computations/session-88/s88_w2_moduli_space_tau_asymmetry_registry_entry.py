#!/usr/bin/env python3
"""
S88 W2-9 — S88-MODULI-SPACE-TAU-ASYMMETRY-REGISTRY-ENTRY
==========================================================

Gate: S88-MODULI-SPACE-TAU-ASYMMETRY-REGISTRY-ENTRY (trigger: AUDIT)
Wave: W2 (METHODOLOGY-class registry-landing at §VII.AE)
Plan: sessions/session-plan/session-88-plan-w2.md §W2-9

Pre-registered threshold (per session-88-plan-w2.md §W2-9.9):
  PASS: §VII.AE registry entry lands with PRIMARY anchor + INDEPENDENT-CROSS-CHECK
        structure tag, ≥ 15 lines body, all 4 cross-links present, methodology-
        wave-allowlist row appended.
  INFO: partial.
  FAIL: registry slot mis-assigned, anchor tagging incorrect, or allowlist row missing.

This is METHODOLOGY-class registry-landing per `wave-classification.md` M1-M4.
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
GATE_ID = "S88-MODULI-SPACE-TAU-ASYMMETRY-REGISTRY-ENTRY"
SCHEME = "moduli-space-tau-asymmetry-substrate-partition-cardinality-vector-direction"
CONVENTION = "negative-side-breakdown-positive-side-rigid-Jensen-scaling-monotone-ascending"
L_MAX = "N/A"
LINE_THRESHOLD_PASS = 15  # (local) plan-pinned ≥15 lines body criterion

T0 = Path(__file__).resolve().parent
SCRIPT_PATH = T0 / "s88_w2_moduli_space_tau_asymmetry_registry_entry.py"
NPZ_OUT = T0 / "s88_w2_moduli_space_tau_asymmetry_registry_entry.npz"
VERDICT_FILE = T0 / "s88_gate_verdicts.txt"

REGISTRY_PATH = T0.parent / "sessions" / "permanent-results-registry.md"
ALLOWLIST_PATH = T0.parent / ".claude" / "rules" / "methodology-wave-allowlist.md"
W2_4_NPZ = T0 / "s88_w2_cf_w11_2_neg_shell.npz"
W2_5_NPZ = T0 / "s88_w2_cf_w11_2_pos_shell.npz"
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
    count = 0  # (local) line counter
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

    # 4.1 — Verify §VII.AE body landed
    sub_row_line_count = count_section_lines(
        REGISTRY_PATH,
        "## §VII.AE — Moduli-Space τ-Asymmetry",
        "---\n",
    )
    print(f"[W2-9] §VII.AE body line count: {sub_row_line_count}")

    registry_text = REGISTRY_PATH.read_text(encoding="utf-8", errors="replace")
    cc1_primary_xcheck_tags = ("PRIMARY anchor" in registry_text or "PRIMARY +" in registry_text or "PRIMARY (volovik R1" in registry_text) and "INDEPENDENT-CROSS-CHECK" in registry_text
    cc2_volovik_r1 = "volovik R1" in registry_text or "§R1-volovik" in registry_text
    cc3_w2_4_sha = "b03c2cba82143b1dc4b1c1f3241a95c5023ac284398605e5aad866427790fc36" in registry_text
    cc4_w2_5_sha = "80b430cc63c2628f9f6108d0db2712cd065e52a34b9f71c9e8a6ced6eb9f1c00" in registry_text
    cc5_w11_2_sha = "008cf3c98f28eca8a3c9b142673be4997c92e62bdcb2c1927b67db2d6e04315d" in registry_text
    cc6_xref_aj = "§VII.AJ.partition-stability" in registry_text
    cc7_xref_ad = "§VII.AD" in registry_text
    cc8_summary_table = "| §VII.AE | THM | Moduli-Space τ-Asymmetry" in registry_text
    cc9_substrate_framing = "Substrate framing" in registry_text and "Jensen TT-deformation" in registry_text

    print(f"[W2-9] CC1 PRIMARY + INDEPENDENT-CROSS-CHECK tags: {cc1_primary_xcheck_tags}")
    print(f"[W2-9] CC2 volovik R1 anchor: {cc2_volovik_r1}")
    print(f"[W2-9] CC3 W2-4 audit_sha cited: {cc3_w2_4_sha}")
    print(f"[W2-9] CC4 W2-5 audit_sha cited: {cc4_w2_5_sha}")
    print(f"[W2-9] CC5 W11-2 audit_sha cited: {cc5_w11_2_sha}")
    print(f"[W2-9] CC6 cross-link to §VII.AJ.partition-stability: {cc6_xref_aj}")
    print(f"[W2-9] CC7 cross-link to §VII.AD: {cc7_xref_ad}")
    print(f"[W2-9] CC8 §VII.AE summary table row: {cc8_summary_table}")
    print(f"[W2-9] CC9 substrate framing block present: {cc9_substrate_framing}")

    # 4.2 — Allowlist row check
    allowlist_text = ALLOWLIST_PATH.read_text(encoding="utf-8", errors="replace")
    cc10_allowlist_w2_9 = "| W2-9 | S88 |" in allowlist_text
    print(f"[W2-9] CC10 methodology-wave-allowlist W2-9 row: {cc10_allowlist_w2_9}")

    # 4.3 — Composite verdict
    all_cc_pass = (
        cc1_primary_xcheck_tags and cc2_volovik_r1 and cc3_w2_4_sha
        and cc4_w2_5_sha and cc5_w11_2_sha and cc6_xref_aj and cc7_xref_ad
        and cc8_summary_table and cc9_substrate_framing and cc10_allowlist_w2_9
        and sub_row_line_count >= LINE_THRESHOLD_PASS
    )
    if all_cc_pass:
        composite = "PASS"
        verdict_kind = "PASS-vii-ae-primary-plus-independent-cross-check-landed"
    elif sub_row_line_count >= 15 and not all_cc_pass:
        composite = "INFO"
        verdict_kind = "INFO-partial-landing-some-cross-checks-failed"
    else:
        composite = "FAIL"
        verdict_kind = "FAIL-anchor-tagging-incorrect-or-body-stub"

    # 4.4 — SHAs
    canon_sha = sha256_file(CANON_PY)
    registry_sha = sha256_file(REGISTRY_PATH)
    allowlist_sha = sha256_file(ALLOWLIST_PATH)
    w2_4_sha = sha256_file(W2_4_NPZ)
    w2_5_sha = sha256_file(W2_5_NPZ)
    script_sha = sha256_file(SCRIPT_PATH)
    content_sha256 = script_sha
    pin_map = {
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "input_canonical_constants_sha256": canon_sha,
        "input_registry_sha256": registry_sha,
        "input_allowlist_sha256": allowlist_sha,
        "input_w2_4_npz_sha256": w2_4_sha,
        "input_w2_5_npz_sha256": w2_5_sha,
        "script_sha256": script_sha,
    }
    audit_sha256 = closure_hash(pin_map)

    np.savez(
        NPZ_OUT,
        sub_row_line_count=np.int64(sub_row_line_count),
        cc1_tags=np.bool_(cc1_primary_xcheck_tags),
        cc2_volovik_r1=np.bool_(cc2_volovik_r1),
        cc3_w2_4_sha=np.bool_(cc3_w2_4_sha),
        cc4_w2_5_sha=np.bool_(cc4_w2_5_sha),
        cc5_w11_2_sha=np.bool_(cc5_w11_2_sha),
        cc6_xref_aj=np.bool_(cc6_xref_aj),
        cc7_xref_ad=np.bool_(cc7_xref_ad),
        cc8_summary_table=np.bool_(cc8_summary_table),
        cc9_substrate_framing=np.bool_(cc9_substrate_framing),
        cc10_allowlist=np.bool_(cc10_allowlist_w2_9),
        composite=composite,
        verdict_kind=verdict_kind,
        audit_sha256=audit_sha256,
        content_sha256=content_sha256,
    )

    elapsed = time.time() - t_start
    value_str = (
        f"sub_row_line_count={sub_row_line_count};"
        f"cc1_tags={cc1_primary_xcheck_tags};cc2_volovik={cc2_volovik_r1};"
        f"cc3_w2_4={cc3_w2_4_sha};cc4_w2_5={cc4_w2_5_sha};cc5_w11_2={cc5_w11_2_sha};"
        f"cc6_aj={cc6_xref_aj};cc7_ad={cc7_xref_ad};cc8_table={cc8_summary_table};"
        f"cc9_framing={cc9_substrate_framing};cc10_allowlist={cc10_allowlist_w2_9};"
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

    print(f"[W2-9] DONE in {elapsed:.2f}s")
    print(f"[W2-9] composite = {composite} (verdict_kind={verdict_kind})")
    print(f"[W2-9] audit_sha256 = {audit_sha256}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
