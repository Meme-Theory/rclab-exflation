#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Atomic read-modify-write insert of the Axis-B (volovik) cross-review subsection
into session-93-w4-workingpaper.md §W4-2.

Keyed on the unique anchor `### Axis-B (volovik) cross-review`. Idempotent: if the
anchor is already present, the script replaces the existing Axis-B block (between
the anchor and the next `### ` heading) rather than duplicating. Does NOT touch the
§W4-2 header or the Axis-A (connes) subsection. Insertion point: immediately BEFORE
the `### §W4-3.` header (i.e., at the end of the §W4-2 block). Concurrent-writer
safe via a single atomic os.replace of a tmp file.
"""
from __future__ import annotations

import os
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent  # (local)
WP = ROOT / "sessions" / "session-93" / "session-93-w4-workingpaper.md"  # (local)

ANCHOR = "### Axis-B (volovik) cross-review"  # (local) unique anchor
NEXT_HEADER = "### §W4-3."  # (local) §W4-2 block ends just before this

AXIS_B_BLOCK = """### Axis-B (volovik) cross-review

**Reviewer**: `volovik-superfluid-universe-theorist` (Axis-B — substrate / superfluid-universe).
**Independence**: audited the REGISTERED §VII.AX.MULTI-PIN-ATLAS Stage-1 entry (registry line ~19486) + cited pins (S91 §W2-1 PASS-V `audit_sha256=58671312b0aee2e7...`) + obs_2 FROM FIRST PRINCIPLES on the substrate/superfluid axis. Did NOT read the S92 W6-1/W6-2 workshop transcript; did NOT read the Axis-A (connes) verdict during the independent audit (Axis-B per-clause verdicts formed + written to `s93_w4_2_axis_b_volovik_multi_pin_atlas_verify.json` BEFORE the aggregation step that mechanically reads both axes).
**Axis-B clause assignment** (per plan §W4-2 dispatch): Element 1 (JOINT), JOINT Element 3, JOINT Element 5, Element 4 (single-axis Axis-B: L⁻³ algebraic envelope). Loads obs_2 (substrate-input-orthogonality, Axis-B-only).

**MCP Pre-Compute Audit** (queries executed before the Axis-B audit):
- `search_knowledge("VII.AX MULTI-PIN-ATLAS regulator-class pluralism substrate-distance-2 pole s=4 chi prime")` → returns the §W6-1 STAGE-1-CANDIDATE landing gate (`S92-W6-CF-W2-1-...-MULTI-PIN-ATLAS-LANDING`, PASS) + the S91 §W2-1 source verdict (`triple_pin R_zeta=1.414393e+02 R_PV=1.144577e+02 R_Mellin=1.414393e+02; cross_reg_spread=2.698e+01`). PRE-CLOSED: STAGE-1-CANDIDATE landed; Stage-2 verify is the open step this gate executes.
- `search_knowledge("n_PBH cardinality cascade tail ... obs_2 grid upper 22.6")` → `n_PBH = n_edge_saturated · prob_form / L_pix_LRD³`; obs_2 = `s91_w5_3_cf41_upper_22_6.npz`; S91 W5-3 extended n_PBH through L_max=14 with UPPER-22.6%-conjunct PASS.
- `query_entity(gates, S92-W6-CF-W2-1-...-MULTI-PIN-ATLAS-LANDING)` → `verdict=PASS; STAGE-1-CANDIDATE_landed; 13_of_13_sub_blocks_PASS`.
- `search_knowledge("substrate-input-orthogonality clause Stage-2 structural ceiling ...")` → MANDATORY at K=3 since S90 W2 CF-20; structural ceiling = ≥1 obs loaded by exactly ONE reviewer; obs_1/obs_2 pre-registered in session-92-plan-w6.md (obs_1 Axis-A-only registry-text; obs_2 = n_PBH grid).
- `get_constant("M_KK")` → 7.428660036284456e+16; `get_constant("tau_fold")` → 0.19 (S12/S42 CONST-FREEZE-42).

**Per-clause Axis-B verdicts** (formed from first principles; `s93_w4_2_axis_b_volovik_multi_pin_atlas_verify.json`):

| Clause | Type | Axis-B verdict | Basis |
|:-------|:-----|:--------------:|:------|
| **Element 1** | JOINT | **PASS** | `Res_{s=4}[Tr(D_K⁻²ˢ)]` at χ′ restriction on `(A_K,H_K,D_K(τ_fold=0.19))` is a Level-1 single-τ-slice substrate-IS observable — a higher Mellin spectral-moment of `D_K` (superfluid-universe analog: a higher-order order-parameter-texture gradient-energy density), intrinsic to the spectral triple, NOT a container coordinate. Level-1 tag present; direction-of-explanation flows substrate → emergent (no container inversion). |
| **JOINT Element 3** | JOINT | **PASS** | Bridge map explicitly named (Connes-Moscovici 1995 §III.4 residue formula ∘ HKR `L_max→∞` image at d=4 substrate-distance-2 pole s=4; NOT "analogous to"). Element-3 binding type (iii) joint-hypersurface: lab discrimination is 2D in (regulator-class R, observable value). Independent check: genuine 2D discrimination (distinct image values = 2: R_zeta = R_Mellin exact, R_PV outlier; cross-reg spread 26.9816 M_KK² > 1e-3 option-(iv) threshold). Bridge-map-scheme suffix discipline satisfied per fiducial sub-row (-ZETA-/-PV-/-MELLIN-). |
| **JOINT Element 5** | JOINT | **PASS** | Triple-pin empirical anchor at canonical L_max=12 via S91 §W2-1 PASS-V (`audit_sha256=58671312b0aee2e7...`). Cross-regulator spread **26.9816 M_KK²** (bit-reproduced from the registered triple-pin) ≫ 1e-3 option-(iv) threshold by **4.43 OOM** IS the option-(v) admission signature BY CONSTRUCTION. Level-3 single-pinned at R_Mellin (substrate-natural canonical); R_zeta + R_PV are Level-2-B DIAGNOSTIC sub-rows only (cross-corner co-primary FORBIDDEN). |
| **Element 4** | single-axis Axis-B | **PASS** | `L⁻³` algebraic envelope at d=4 substrate-distance-2 pole s=4; **Level-2-BINDING** sub-class — the HKR-image of the χ′ Hochschild moment binds Level-1 (pluralism THEOREM) to lab-IN continuum images (c_continuum defined per regulator class at Pillar IV/II/V projections). Three structurally INDEPENDENT envelopes (Hybrid Independence Test clause (iv) YES), NOT numerical refinements of one another. |

#### Axis-B substrate-input-orthogonality at obs_2 (the cross-pole comparison; structural ceiling)

I (Axis-B) load **obs_2** = the n_PBH cardinality grid `s91_w5_3_cf41_upper_22_6.npz` (sha256 `26262e146e670d2e...`, matching the plan pin). Axis-A (connes) does NOT load it (plan dispatch `axis_a.loads_obs_2=false`).

- **obs_2 is structurally DISTINCT from the MULTI-PIN-ATLAS observable**: the n_PBH grid (`[7.276e-23, 9.775e-23, 1.292e-22]` at L_max ∈ {14,15,16}) tracks `N_eigs` (`[323136, 434112, 573648]`) **LINEARLY** (ratio-of-ratios = 1.0 EXACT) ⇒ a cardinality-cascade observable at substrate-distance-3 pole s=5, NOT the s=4 Mellin residue. Cross-pole ladder: s=3 (`α_s_canonical = -0.085873`) / s=4 (MULTI-PIN-ATLAS residue) / s=5 (n_PBH cardinality cascade); obs_2 anchors the s=5 end, non-fungible w.r.t. the s=4 atlas.
- **Floor (MANDATORY K=3)**: ≥1 obs loaded by exactly ONE reviewer — obs_2 is Axis-B-exclusive. **PASS**.
- **Structural CEILING (NO substrate-input-overlap caveat)**: obs_2 is the only shared-relevant grid and it is Axis-B-exclusive ⇒ the PASS-AND is structural-input-independent, matching the S89 W4-7 §VII.AH FIRST-INSTANCE-WITHOUT-caveat precedent. **PASS**.

#### Axis-B composite + honesty note

- **Axis-B composite: PASS** (E1 JOINT ∧ JE3 ∧ JE5 ∧ E4 single-axis all PASS; substrate-input-orthogonality at obs_2 PASS at structural ceiling; machinery-not-self-authored PASS — the 5-anatomy/3-level + Hybrid Independence Test machinery is shared-rule-file canonical, not authored by volovik).
- **Honesty note (non-load-bearing annotation imprecision)**: registry Element 3/5 + provenance state "33% relative divergence" for the cross-regulator spread. Independent Axis-B check: spread/R_Mellin = 26.9816/141.4393 = **19.08%**; spread/R_PV = 23.58%; neither is exactly 33%. This is a NON-LOAD-BEARING annotation imprecision — the load-bearing claim (spread ≫ 1e-3 ⇒ option (v) pluralism) holds robustly at 4.43 OOM excess, and the spread magnitude itself (26.98 M_KK²) is bit-reproduced. Flagged for a future registry-text hygiene pass; does NOT affect any clause verdict.

**Aggregation status (this dispatch)**: the producing/aggregation script `s93_w4_2_vii_ax_multi_pin_atlas_stage_2_verify.py` is authored and ready-to-run with `--emit`. Dry-run (no `--emit`) reads both axis JSONs and computes the strict PASS-AND boundary = **PASS** (`axis_A_connes=PASS ∧ axis_B_volovik=PASS ∧ JOINT-clause PASS-AND ∧ substrate-input-orthogonality obs_2 floor+ceiling ∧ OAA-exclusion {mack} ∧ machinery-not-self-authored ∧ convention-ends-FULL`) ⇒ `STAGE-3-PERMANENT-ELIGIBLE`, `mack_tag_flip_licensed=True`. **The final W4-2 verdict line is NOT emitted in this dispatch** — the orchestrator triggers `--emit` once both axis JSONs are confirmed on disk.

"""  # noqa: E501


def main() -> int:
    text = WP.read_text(encoding="utf-8")  # (local)
    lines = text.splitlines(keepends=True)  # (local)

    # locate insertion point: just before the §W4-3 header
    next_idx = None  # (local)
    for i, ln in enumerate(lines):
        if ln.startswith(NEXT_HEADER):
            next_idx = i
            break
    if next_idx is None:
        raise SystemExit(f"FATAL: next-header anchor {NEXT_HEADER!r} not found in WP")

    # idempotent: if the Axis-B anchor already exists, replace its block
    anchor_idx = None  # (local)
    for i, ln in enumerate(lines):
        if ln.startswith(ANCHOR):
            anchor_idx = i
            break

    block_lines = [l + "\n" if not l.endswith("\n") else l
                   for l in AXIS_B_BLOCK.splitlines()]  # (local)
    # ensure trailing blank separation before §W4-3
    if block_lines and block_lines[-1].strip():
        block_lines.append("\n")

    if anchor_idx is not None:
        # find end of existing Axis-B block (next `### ` heading at/after anchor)
        end_idx = next_idx  # (local) default: up to §W4-3
        for j in range(anchor_idx + 1, len(lines)):
            if lines[j].startswith("### "):
                end_idx = j
                break
        new_lines = lines[:anchor_idx] + block_lines + lines[end_idx:]  # (local)
        mode = "REPLACED existing Axis-B block"  # (local)
    else:
        new_lines = lines[:next_idx] + block_lines + lines[next_idx:]  # (local)
        mode = "INSERTED new Axis-B block before §W4-3"  # (local)

    # atomic write (concurrent-writer safe): tmp + os.replace
    fd, tmp = tempfile.mkstemp(dir=str(WP.parent), suffix=".tmp")  # (local)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as fp:
            fp.write("".join(new_lines))
        os.replace(tmp, WP)
    except BaseException:
        if os.path.exists(tmp):
            os.unlink(tmp)
        raise

    print(f"{mode}: {WP}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
