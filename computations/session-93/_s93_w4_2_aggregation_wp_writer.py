#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Atomic read-modify-write of session-93-w4-workingpaper.md §W4-2:

 (1) flip the §W4-2 header Status -> COMPLETED and Verdict -> PASS (scoped to the
     §W4-2 header block ONLY, between the §W4-2 header and the first `### Axis-A`
     subsection — does NOT touch Axis-A / Axis-B subsections or other gates);
 (2) insert an `### Aggregation result` subsection immediately BEFORE the
     `### §W4-3.` header (end of the §W4-2 block).

Concurrent-writer safe via a single atomic os.replace. Idempotent on the
Aggregation-result anchor (replaces an existing block rather than duplicating).
"""
from __future__ import annotations

import os
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent  # (local)
WP = ROOT / "sessions" / "session-93" / "session-93-w4-workingpaper.md"  # (local)

W42_HEADER = "### §W4-2. S93-W4-2-VII-AX-MULTI-PIN-ATLAS-STAGE-2-CROSS-AXIS-VERIFY"  # (local)
FIRST_SUBSECTION = "### Axis-A"  # (local) end of the §W4-2 header block
ANCHOR = "### Aggregation result"  # (local) unique anchor for the aggregation block
NEXT_HEADER = "### §W4-3."  # (local) §W4-2 block ends just before this

AGG_BLOCK = """### Aggregation result

**Status**: COMPLETED. **Verdict**: **PASS** (Stage-2 cross-axis PASS-AND).

The aggregation/emission script `s93_w4_2_vii_ax_multi_pin_atlas_stage_2_verify.py --emit` read both axis JSONs and computed the strict Stage-2 PASS-AND boundary. Composite = **PASS** ⇒ §VII.AX.MULTI-PIN-ATLAS is **STAGE-3-PERMANENT-ELIGIBLE**; the `mack-cosmic-bridge` STAGE-1-CANDIDATE → STAGE-3-PERMANENT tag-flip is licensed (executed at the wave-exit registry-write under the slot-pre-allocation lockfile W0-1).

**Per-clause PASS-AND (both axes, logical AND):**

| Clause | Type | Axis-A (connes) | Axis-B (volovik) | PASS-AND |
|:-------|:-----|:---------------:|:----------------:|:--------:|
| Element 1 | JOINT | PASS | PASS | PASS |
| Element 3 | JOINT | PASS | PASS | PASS |
| Element 5 | JOINT | PASS | PASS | PASS |
| Axis-A single-axis (Element 2 OE-form) | single-axis | PASS | — | PASS |
| Axis-B single-axis (Element 4 L⁻³ envelope) | single-axis | — | PASS | PASS |
| **Axis composite** | — | **PASS** | **PASS** | **PASS** |

**Structural-gate conjuncts (all PASS):**

- **substrate-input-orthogonality at obs_2** (MANDATORY K=3 since S90 W2 CF-20): obs_2 (n_PBH cardinality grid `s91_w5_3_cf41_upper_22_6.npz`) loaded by Axis-B (volovik) ONLY; Axis-A (connes) does NOT load it. **Floor PASS** (≥1 obs by exactly one reviewer). **Structural CEILING achieved — NO substrate-input-overlap caveat** (obs_2 is the only shared-relevant grid and it is Axis-B-exclusive; matches the S89 W4-7 §VII.AH FIRST-INSTANCE-WITHOUT-caveat precedent). The cross-pole comparison is structural: obs_2/n_PBH tracks N_eigs LINEARLY ⇒ substrate-distance-3 pole s=5 cardinality cascade, DISTINCT from the MULTI-PIN-ATLAS s=4 Mellin residue.
- **OAA-exclusion {mack-cosmic-bridge}** (Stage-1 sole-writer): satisfied (Axis-A connes + Axis-B volovik admissible; neither read the workshop transcript — downstream-inheritance reach check PASS).
- **machinery-not-self-authored** (joint-theorem-promotion §Audit item 6): PASS (shared rule-file 5-anatomy/3-level + Hybrid Independence Test machinery; not authored by either reviewer).
- **convention-ends-FULL**: PASS (FULL CM-1995 §III.4 evaluation class pin; convention suffix `…-FULL`).

**Regulator-class residues** (Level-3 triple-pin, cited from S91 §W2-1 PASS-V `audit_sha256=58671312b0aee2e7…`): R_zeta = 1.414393e+02, R_PV = 1.144577e+02, R_Mellin = 1.414393e+02 M_KK²; cross-regulator spread **26.9816 M_KK²** ≫ 1e-3 option-(iv) threshold by **4.43 OOM** = the option-(v) regulator-class-pluralism admission signature BY CONSTRUCTION. Level-3 single-pinned at R_Mellin (substrate-natural canonical); R_zeta + R_PV are Level-2-B DIAGNOSTIC sub-rows only.

**4-tuple** (per `cross-pillar-bridge-anatomy.md §"Per-pole-per-observable-class 4-tuple"`): `(pole_index = 4, regulator-invariance = RD [regulator-DEPENDENT — option (v) pluralism], observable-class = algebra-INVARIANT [Cell II spectrum-only-functional], layer = atlas-row)`.

**Emitted verdict line** (`computations/session-93/s93_gate_verdicts.txt`; sig_5-unique — 25 distinct audit_sha256 across the file, 0 duplicates):

```
S93-W4-2-VII-AX-MULTI-PIN-ATLAS-STAGE-2-CROSS-AXIS-VERIFY: PASS -- value='…stage3=STAGE-3-PERMANENT-ELIGIBLE_mack_tag_flip_licensed=True' scheme=stage-2-cross-axis-verify-MULTI-PIN-ATLAS-substrate-distance-2-pole-s4-chi-prime-restriction convention=…-FULL L_max=12 audit_sha256=ba202d1626c99c5d36a734735266a0b0541c9d87e6913f1a6f2093f7ad38451f content_sha256=c48a0dd1d9849b378b5586478d624b4fcdd1c99f6064220e646141e21f027d1b schema_version=S84+
```

**NON-LOAD-BEARING registry-text hygiene note** (Axis-B flagged; do NOT edit registry — `mack-cosmic-bridge` is registry sole-writer; route to a mack gate or session-end): registry §VII.AX.MULTI-PIN-ATLAS Element 3/5 + provenance state "33% relative divergence" for the cross-regulator spread. Independent Axis-B check: spread/R_Mellin = 26.9816/141.4393 = **19.08%**; spread/R_PV = 23.58%; neither is exactly 33%. The load-bearing claim (spread ≫ 1e-3 ⇒ option (v) pluralism) holds robustly at 4.43 OOM excess, and the spread magnitude itself (26.98 M_KK²) is bit-reproduced from the registered triple-pin — so this is purely a registry-prose imprecision, not a structural defect. Recommend the "33%" annotation be corrected to "≈ 19% of R_Mellin (≈ 24% of R_PV)" in a future mack-authored registry-text hygiene pass; **does NOT affect the W4-2 PASS verdict**.

**Output Artifacts** (all on disk):
- `computations/session-93/s93_w4_2_vii_ax_multi_pin_atlas_stage_2_verify.py` (aggregation/producing script; contains `from canonical_constants import` + `append_verdict`).
- `computations/session-93/s93_w4_2_axis_a_connes_multi_pin_atlas_verify.json` (Axis-A verdicts; composite PASS).
- `computations/session-93/s93_w4_2_axis_b_volovik_multi_pin_atlas_verify.json` (Axis-B verdicts; composite PASS).
- `computations/session-93/s93_w4_2_vii_ax_multi_pin_atlas_stage_2_verify.json` + `.npz` (aggregation sidecar).
- Verdict line + dual-SHA companion in `s93_gate_verdicts.txt` (`audit_sha256=ba202d1626c99c5d…`; sig_5-unique).

"""  # noqa: E501


def main() -> int:
    text = WP.read_text(encoding="utf-8")  # (local)
    lines = text.splitlines(keepends=True)  # (local)

    # locate the §W4-2 header + the first subsection that ends the header block
    w42_idx = None  # (local)
    for i, ln in enumerate(lines):
        if ln.startswith(W42_HEADER):
            w42_idx = i
            break
    if w42_idx is None:
        raise SystemExit(f"FATAL: §W4-2 header anchor not found")

    first_sub_idx = None  # (local)
    for j in range(w42_idx + 1, len(lines)):
        if lines[j].startswith(FIRST_SUBSECTION) or lines[j].startswith(NEXT_HEADER):
            first_sub_idx = j
            break
    if first_sub_idx is None:
        first_sub_idx = len(lines)

    # (1) flip Status -> COMPLETED + Verdict -> PASS, scoped to the header block
    #     [w42_idx, first_sub_idx). Replace the FIRST '**Status**:' and the
    #     '**Verdict**:' + its pending line within the header block only.
    status_done = False  # (local)
    verdict_done = False  # (local)
    for k in range(w42_idx, first_sub_idx):
        if not status_done and lines[k].startswith("**Status**:"):
            lines[k] = "**Status**: COMPLETED\n"
            status_done = True
        if not verdict_done and lines[k].startswith("**Verdict**:"):
            lines[k] = "**Verdict**: **PASS** (Stage-2 cross-axis PASS-AND; §VII.AX.MULTI-PIN-ATLAS STAGE-3-PERMANENT-ELIGIBLE)\n"
            # blank the immediately-following pending placeholder line if present
            if k + 1 < first_sub_idx and lines[k + 1].lstrip().startswith("*(pending"):
                lines[k + 1] = "\n"
            verdict_done = True

    # (2) insert/replace the Aggregation-result block immediately before §W4-3.
    #     Re-scan indices after the in-place header edits (lengths unchanged here).
    next_idx = None  # (local)
    for i, ln in enumerate(lines):
        if ln.startswith(NEXT_HEADER):
            next_idx = i
            break
    if next_idx is None:
        raise SystemExit(f"FATAL: next-header anchor {NEXT_HEADER!r} not found")

    anchor_idx = None  # (local)
    for i, ln in enumerate(lines):
        if ln.startswith(ANCHOR):
            anchor_idx = i
            break

    block_lines = [l + "\n" if not l.endswith("\n") else l
                   for l in AGG_BLOCK.splitlines()]  # (local)
    if block_lines and block_lines[-1].strip():
        block_lines.append("\n")

    if anchor_idx is not None:
        end_idx = next_idx  # (local)
        for j in range(anchor_idx + 1, len(lines)):
            if lines[j].startswith("### "):
                end_idx = j
                break
        new_lines = lines[:anchor_idx] + block_lines + lines[end_idx:]  # (local)
        mode = "REPLACED existing Aggregation-result block"  # (local)
    else:
        new_lines = lines[:next_idx] + block_lines + lines[next_idx:]  # (local)
        mode = "INSERTED new Aggregation-result block before §W4-3"  # (local)

    fd, tmp = tempfile.mkstemp(dir=str(WP.parent), suffix=".tmp")  # (local)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fp:
            fp.write("".join(new_lines))
        os.replace(tmp, WP)
    except BaseException:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise

    print(f"Status flip: {'OK' if status_done else 'MISSED'}; "
          f"Verdict flip: {'OK' if verdict_done else 'MISSED'}")
    print(f"{mode}: {WP}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
