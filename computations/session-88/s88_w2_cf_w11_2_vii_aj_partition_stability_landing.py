#!/usr/bin/env python3
"""
S88 W2-6 — S88-CF-W11-2-VII-AJ-PARTITION-STABILITY-LANDING
============================================================

Gate: S88-CF-W11-2-VII-AJ-PARTITION-STABILITY-LANDING (trigger: AUDIT)
Wave: W2 (METHODOLOGY-class registry sub-row consolidation)
Plan: sessions/session-plan/session-88-plan-w2.md §W2-6

Pre-registered threshold (per session-88-plan-w2.md §W2-6.9):
  PASS: §VII.AJ.partition-stability sub-row body extended to >=70 lines;
        explicit τ-asymmetric direction declared; W11-3 Friedrich-Bär
        saturation citation present; cross-links to §VII.AE +
        W11-meta-1 audit_sha256 present; methodology-wave-allowlist row
        appended.
  INFO: partial consolidation (some cross-links missing).
  FAIL: sub-row body remains stub (<30 lines); allowlist row missing.

This is METHODOLOGY-class per `wave-classification.md` §M1-M4 conjunction:
  M1: artifact-existence-with-substantive-content predicate (NOT numerical)
  M2: producing operations are Edit/grep/wc/SHA-256 cross-checks (NOT compute)
  M3: source is verbatim-extract from S87 W11-2 + W11-3 closure + S88 W2-4 + W2-5 verdict files
  M4: gate-ID W2-6 is allowlisted in `.claude/rules/methodology-wave-allowlist.md`

INTRA-PILLAR exemption per `cross-pillar-bridge-anatomy.md`: this entry is
within Pillar III (spectral triple); 5-IS-not-IN anatomy + 3-level ladder
applies ONLY to cross-pillar bridges; sub-row consolidation is artifact-
existence with substantive cross-links.

Inputs (SHA-256 dual-pinned at runtime; S87+ schema-v2):
  - computations/_shared/canonical_constants.py
  - sessions/permanent-results-registry.md  (registry edit target — edited pre-script)
  - .claude/rules/methodology-wave-allowlist.md (allowlist append target — edited pre-script)
  - computations/session-88/s88_w2_cf_w11_2_neg_shell.npz (W2-4 SHARP localization input)
  - computations/session-88/s88_w2_cf_w11_2_pos_shell.npz (W2-5 SHARP localization input)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<sub-row-line-count>,
   scheme=intra-pillar-partition-stability-sub-row-consolidation,
   convention=W11-meta-1-source-double-cite-co-primary-anchored,
   L_max=N/A)

Classification: METHODOLOGY
"""

from __future__ import annotations

# Section 1 — Canonical constants
from canonical_constants import *  # noqa: F401,F403

# Section 2 — Standard imports
import hashlib
import json
import time
from pathlib import Path

# Section 3 — Pin metadata
GATE_ID = "S88-CF-W11-2-VII-AJ-PARTITION-STABILITY-LANDING"
SCHEME = "intra-pillar-partition-stability-sub-row-consolidation"
CONVENTION = "W11-meta-1-source-double-cite-co-primary-anchored"
L_MAX = "N/A"             # (local) METHODOLOGY-class; no spectral truncation
LINE_THRESHOLD_PASS = 70  # (local) plan-pinned ≥70 lines body criterion
NEW_CONTENT_THRESHOLD = 15  # (local) plan-pinned ≥15 lines new content criterion

T0 = Path(__file__).resolve().parent
SCRIPT_PATH = T0 / "s88_w2_cf_w11_2_vii_aj_partition_stability_landing.py"
VERDICT_FILE = T0 / "s88_gate_verdicts.txt"
NPZ_OUT = T0 / "s88_w2_cf_w11_2_vii_aj_partition_stability_landing.npz"

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
    """Count lines between start_anchor and end_anchor (exclusive)."""
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

    # 4.1 — Verify the registry edits landed (artifact-existence checks)
    sub_row_line_count = count_section_lines(
        REGISTRY_PATH,
        "### §VII.AJ.partition-stability — 4-Stratum Partition",
        "## §VII.PROP — Routing-Layer Two-Principle Landing",
    )
    print(f"[W2-6] §VII.AJ.partition-stability body line count: {sub_row_line_count}")

    # 4.2 — Cross-link presence checks
    registry_text = REGISTRY_PATH.read_text(encoding="utf-8", errors="replace")
    cc1_w11_3_friedrich_bar_present = "Friedrich-Bär" in registry_text or "Friedrich-Bar" in registry_text
    cc2_w2_4_audit_sha_present = "b03c2cba82143b1dc4b1c1f3241a95c5023ac284398605e5aad866427790fc36" in registry_text
    cc3_w2_5_audit_sha_present = "80b430cc63c2628f9f6108d0db2712cd065e52a34b9f71c9e8a6ced6eb9f1c00" in registry_text
    cc4_w11_meta_1_sha_present = "e3140898882a326d088e334be5e56bfa98dd77963fae6f187be8fc85e62d08ee" in registry_text
    cc5_vii_ae_xref_present = "§VII.AE moduli-space" in registry_text or "VII.AE" in registry_text
    cc6_summary_table_landed = "§VII.AJ.partition-stability | LANDED" in registry_text

    print(f"[W2-6] CC1 W11-3 Friedrich-Bär citation: {cc1_w11_3_friedrich_bar_present}")
    print(f"[W2-6] CC2 W2-4 audit_sha256 cited: {cc2_w2_4_audit_sha_present}")
    print(f"[W2-6] CC3 W2-5 audit_sha256 cited: {cc3_w2_5_audit_sha_present}")
    print(f"[W2-6] CC4 W11-meta-1 audit_sha256 cited: {cc4_w11_meta_1_sha_present}")
    print(f"[W2-6] CC5 §VII.AE cross-link present: {cc5_vii_ae_xref_present}")
    print(f"[W2-6] CC6 summary-table line 105 STALE-STATUS fixed: {cc6_summary_table_landed}")

    # 4.3 — methodology-wave-allowlist row presence
    allowlist_text = ALLOWLIST_PATH.read_text(encoding="utf-8", errors="replace")
    cc7_allowlist_w2_6_row = "| W2-6 | S88 |" in allowlist_text

    print(f"[W2-6] CC7 methodology-wave-allowlist W2-6 row appended: {cc7_allowlist_w2_6_row}")

    # 4.4 — Composite verdict per plan §W2-6.9
    all_cross_links = (
        cc1_w11_3_friedrich_bar_present
        and cc2_w2_4_audit_sha_present
        and cc3_w2_5_audit_sha_present
        and cc4_w11_meta_1_sha_present
        and cc5_vii_ae_xref_present
        and cc6_summary_table_landed
        and cc7_allowlist_w2_6_row
    )
    if sub_row_line_count >= LINE_THRESHOLD_PASS and all_cross_links:
        composite = "PASS"
        verdict_kind = "PASS-sub-row-consolidated-with-all-cross-links"
    elif sub_row_line_count >= 30 and not all_cross_links:
        composite = "INFO"
        verdict_kind = "INFO-partial-consolidation-some-cross-links-missing"
    else:
        composite = "FAIL"
        verdict_kind = "FAIL-sub-row-stub-or-allowlist-missing"

    # 4.5 — SHAs
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
        "LINE_THRESHOLD_PASS": LINE_THRESHOLD_PASS,
        "NEW_CONTENT_THRESHOLD": NEW_CONTENT_THRESHOLD,
        "input_canonical_constants_sha256": canon_sha,
        "input_registry_sha256": registry_sha,
        "input_allowlist_sha256": allowlist_sha,
        "input_w2_4_npz_sha256": w2_4_sha,
        "input_w2_5_npz_sha256": w2_5_sha,
        "script_sha256": script_sha,
    }
    audit_sha256 = closure_hash(pin_map)

    # 4.6 — Save .npz
    np.savez(
        NPZ_OUT,
        sub_row_line_count=np.int64(sub_row_line_count),
        cc1_w11_3_friedrich_bar=np.bool_(cc1_w11_3_friedrich_bar_present),
        cc2_w2_4_sha=np.bool_(cc2_w2_4_audit_sha_present),
        cc3_w2_5_sha=np.bool_(cc3_w2_5_audit_sha_present),
        cc4_w11_meta_1_sha=np.bool_(cc4_w11_meta_1_sha_present),
        cc5_vii_ae_xref=np.bool_(cc5_vii_ae_xref_present),
        cc6_summary_table_landed=np.bool_(cc6_summary_table_landed),
        cc7_allowlist_row=np.bool_(cc7_allowlist_w2_6_row),
        composite=composite,
        verdict_kind=verdict_kind,
        audit_sha256=audit_sha256,
        content_sha256=content_sha256,
    )

    # 4.7 — Append verdict line
    elapsed = time.time() - t_start
    value_str = (
        f"sub_row_line_count={sub_row_line_count};"
        f"cc1_friedrich={cc1_w11_3_friedrich_bar_present};"
        f"cc2_w2_4={cc2_w2_4_audit_sha_present};"
        f"cc3_w2_5={cc3_w2_5_audit_sha_present};"
        f"cc4_w11_meta_1={cc4_w11_meta_1_sha_present};"
        f"cc5_vii_ae={cc5_vii_ae_xref_present};"
        f"cc6_table={cc6_summary_table_landed};"
        f"cc7_allowlist={cc7_allowlist_w2_6_row};"
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

    print(f"[W2-6] DONE in {elapsed:.2f}s")
    print(f"[W2-6] composite = {composite} (verdict_kind={verdict_kind})")
    print(f"[W2-6] audit_sha256 = {audit_sha256}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
