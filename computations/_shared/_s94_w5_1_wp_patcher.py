#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Surgical in-place replacement of the WP section '### §W5-1. ...' under a
parallel-writer race (Edit tool is mtime-conditional; this read-modify-write
with a bounded retry loop is the registry-write-hygiene-compliant alternative
per epistemic-discipline.md §"Registry-Write Hygiene under Parallel-Writer Race").

Targets ONLY the bytes between the '### §W5-1.' header and the next '\n---\n'
delimiter, leaving every other gate's section byte-untouched. Idempotent: if the
section already shows '**Status**: COMPLETED' with this gate's audit SHA, it is a
no-op.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

WP = Path(r"C:\sandbox\Ainulindale Exflation\sessions\archive\session-94\session-94-w5-workingpaper.md")
HEADER = "### §W5-1. S94-N-PBH-TRUNCATION-ANCHOR (mack-cosmic-bridge)"
AUDIT_SHA = "e310d687be9b47910c90466fd1615707513bbad10f2f84a9c3c0f30fb7f4fe98"

NEW_BLOCK = r"""### §W5-1. S94-N-PBH-TRUNCATION-ANCHOR (mack-cosmic-bridge)

**Status**: COMPLETED
**Gate ID**: `S94-N-PBH-TRUNCATION-ANCHOR`
**Trigger**: `[CHAIN]`
**Classification**: **GEOMETRIC** (the truncation anchor is a property of the D_K spectral-triple cardinality structure — the fabric itself, not an excitation)
**Agent**: `mack-cosmic-bridge`
**Hypothesis**: The L_max=14 PROVISIONAL truncation label on n_PBH_FW_central cannot be sourced from an N_eigs(L_max) eigenvalue-count plateau (W4-3 PROVED N_eigs is an unbounded quintic); the truncation must be pinned by a substrate-physical (cascade-saturation generation g_saturate) or Tier-2-dimensionless anchor, since the m⁻³ channel is Tier-2-dimensionful (dimension and L_max-divergence share the same multiplicative slot).
**Plan reference**: `sessions/session-plan/session-94-plan-w5.md` §W5-1 (machinery pin, [CHAIN] rubric, Step A-E substitution chain source).

**Output Artifacts** (closure-verification checklist; mirrors the gate-block `output_artifacts:` YAML):

| Artifact | Path | Exists | must_contain check |
|:---------|:-----|:-------|:-------------------|
| script | `computations/session-94/s94_n_pbh_truncation_anchor.py` (byte-identical copy of the canonical producing script at `computations/_shared/s94_n_pbh_truncation_anchor.py`; `content_sha256=01818a20…` matches both) | YES (38965 B) | `grep -E "from canonical_constants import"` → `from canonical_constants import (  # noqa: E402`; `grep -cE "append_verdict"` → 2 (def + call) ✓ |
| data | `computations/session-94/s94_n_pbh_truncation_anchor.npz` | YES (18434 B) | full float64 of all m⁻³ candidate values (`n_PBH_frozen_saturation_m3`, `n_PBH_linear_L14_m3`, `canonical_central_m3`) ✓ |
| plot | `computations/session-94/s94_n_pbh_truncation_anchor.png` | YES (280299 B) | 4-panel: N_eigs(L_max) quintic (no plateau) / two n_PBH channels (divergent L_max-axis vs frozen g-axis) / Tier-2 log-derivative→5 / verdict summary ✓ |
| verdict_line | `computations/session-94/s94_gate_verdicts.txt` | YES | matches `^S94-N-PBH-TRUNCATION-ANCHOR:.* audit_sha256=[a-f0-9]{64}` (`audit_sha256=e310d687be9b4791…`) + dual-SHA companion row; **no schema_v2 3-tuple row** (correct — [CHAIN], `schema_v2_3tuple_required: false`) ✓ |
| wp_section | this section | YES | `**Status**: COMPLETED`, `**Verdict**: INFO`, `**Output Artifacts**`, `**MCP Pre-Compute Audit**` ✓ |

**MCP Pre-Compute Audit**:
- `get_constant('n_PBH_FW_central')` → `7.2761e-23` m⁻³ (S93 W4-5; the contested Level-3 anchor; provenance: FWD-C5 cardinality-cascade-tail saturation; PROVISIONAL truncation per S93 W4-3 INFO). The value-pin I treat as the canonical magnitude under test.
- `search_knowledge('n_PBH cascade saturation g_saturate cardinality edge count truncation')` → equation hits: `n_PBH = n_edge_saturated · prob_form / L_pix_LRD³`; `g_saturate = 143 IS the substrate's intrinsic Peter-Weyl multiplicity`; gate `S93-W4-3-N-PBH-CANONICAL-TRUNCATION-FACTORIZATION` (INFO; w(L_max) DIVERGENT) + `S93-W4-6-…-CARDINALITY-CASCADE-SHOULDER` (n_PBH_shoulder(g)=(prob_form/L_pix_LRD³)·2^{2g}, rising).
- `search_knowledge('VII.AX OP-PROJ PBH Tier-2 dimensionful truncation divergent anchor')` → workshop `s93-vii-ax-op-proj-stage3-truncation-divergent-anchor.md`; the L=16…19 band-trajectory (L=18 last-in-band 0.982, L=19 breach 1.247) — that is the W5-2 gate, NOT this one.
- `get_constant('g_saturate' / 'L_pix_LRD' / 'prob_form' / 'n_edge_saturated')` → NOT canonical constants (registry-equation-sourced only). Treated as registry-pinned [CHAIN] derivation inputs (`permanent-results-registry.md` lines 19419-19423; S88 W1a-59 canonical), NOT promoted here.
- **NOT pre-closed**: the n_PBH m⁻³ Level-3 row is held `NOT-SATISFIED-PENDING-substrate-physical-scale-anchor`; this gate executes the re-determination, it is not covered by a prior closure.

**Verdict**: **INFO** — per the plan W5-1 `INFO_meaning`: the substrate-physical anchor (g_saturate=143 cascade-saturation) is identified as the **CORRECT AXIS** (L_max-INDEPENDENT) and the N_eigs-plateau read-off is formally **EXCLUDED**, the m⁻³ Level-3 row is correctly classified **Tier-2-dimensionful** and **HELD**, and the L_max=14 label is updated — BUT the numerical decoupling of the canonical 7.2761e-23 magnitude from L_max requires a separate saturated-tail recompute (**CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED**). The §VII.AX.OP-PROJ permanence STANDS on the theorem-STRUCTURE (Tier-2 corollary).
- 4-tuple: `(value=anchor:D1=g_saturate=143, scheme=FWD-C5-CARDINALITY-CASCADE-TAIL, convention=TIER-2-DIMENSIONFUL-HELD, L_max=N/A)`
- SHAs: `audit_sha256=e310d687be9b47910c90466fd1615707513bbad10f2f84a9c3c0f30fb7f4fe98`, `content_sha256=01818a209caf07c6fd50aa0769fa90438625682c5c4233d30d261790de6fff53`, `closure_hash(pins)=fbdbf53c4c9fa177d8fd89249f23682ade60610fd073d00d97d42d02b553626d`.
- Input SHA pins: `canonical_constants.py = 66f7b5a26050e31a…`; `s93_w4_3_…_npz = 4d21402cee974641…`.

**Results**:

**Step A — W4-3 quintic reproduced; N_eigs(L_max) is monotone UNBOUNDED (no plateau).**
The W4-3 Sage-exact quintic `N_eigs(L) = (4/15)L⁵ + (10/3)L⁴ + 16L³ + (110/3)L² + (596/15)L + 16` (QQ-exact, evaluated in `fractions.Fraction`):
- `N_eigs(14) = 323136` reproduces the W4-3 npz anchor with `rel_err = 0.00e+00` (Sage-exact; ≤ 1e-12 cross-check tolerance, PASS).
- `dN/dL = (4/3)L⁴ + (40/3)L³ + 48L² + (220/3)L + 596/15` has all positive coefficients ⇒ `dN/dL > 0 ∀ L ≥ 1` (monotone increasing); `strictly_increasing = True` over L∈{1,…,20}.
- `lim_{L→∞} N_eigs = +∞`. Probe: N_eigs(14, 20, 30, 50, 100, 200) = {323136, 1530144, 9646208, 106260336, 3016370656, 90796141296} — unbounded growth. **There is no plateau; the L_max=14 label cannot be a saturation read-off.**

**Step B — dimensional-decomposition substitution chain** (`n_PBH = n_edge · prob_form / L_pix_LRD³`; registry §VII.AX Step-4 form, lines 19419-19423):

| Channel | Form | Value (m⁻³) | L_max behavior |
|:--------|:-----|:-----------|:---------------|
| LINEAR (obs_2, **canonical**) | `A_prefactor · N_eigs(L=14)`, `A_prefactor = 1.758127e-23/78080 = 2.2517e-28 m⁻³/count` | **7.276052e-23** (= `n_PBH_FW_central`) | **DIVERGENT** (L_max-axis) |
| g-axis FROZEN-SATURATED | `C(78080,2) · prob_form / L_pix_LRD³` = `3,048,204,160 · 0.15573 / (3.0e10 m)³` | **1.758136e-23** (L=10 baseline) | **L_max-INDEPENDENT** |
| registered degree-10 | `C(N_eigs(14),2) · prob_form / L_pix_LRD³` | 3.011257e-22 | DIVERGENT (worse, degree-10) |

The dimension `[m⁻³]` sits in `L_pix_LRD³` (= `(3.0e10 m)³`); the L_max-divergence sits in the cardinality count `N_eigs(L_max)`. The canonical `7.2761e-23` is the LINEAR L=14 read — the divergent channel.

**Step C — Tier-2-dimensionful test** (per `cross-pillar-bridge-anatomy.md §"Tier-1/Tier-2 dimensional-re-anchorability gate"`):
The log-derivative that buys truncation-invariance, `d ln(A·N_eigs)/d ln L = d ln N_eigs/d ln L` (the constant `ln A` is annihilated), is **dimensionless**: `= 4.2581 at L=14`, `→ 4.9999 ≈ 5` as L→∞ (the leading-power exponent of the quintic — a dimensionless cascade exponent, matching the workshop's `→5`). The only truncation-invariant content is dimensionless; retaining the dimension `A` retains the divergence (`A·N_eigs → +∞`). Dimension and divergence occupy the **SAME multiplicative slot** ⇒ **TIER-2-DIMENSIONFUL** ⇒ the m⁻³ Level-3 magnitude row is **REGISTRY-PASS-INELIGIBLE-HELD**. §VII.AX.OP-PROJ is confirmed as the **inaugural occupant** of the Tier-2-dimensionful cell.

**Step D — anchor candidates + selection (first-principles).**
- **(D1) substrate-physical scale anchor — SELECTED**: the g-axis cascade-saturation generation `g_saturate = 143` (the substrate's intrinsic Peter-Weyl multiplicity; S88 W1a-59). Above saturation the cascade-tail edge count FREEZES at `n_edge_saturated = C(N_eigs, 2)` and `g(K) = prob_form / L_pix_LRD³` carries the `[m⁻³]` dimension. **Verified L_max-INDEPENDENT**: neither `prob_form` (Parker-pair production rate) nor `L_pix_LRD` (substrate-clock pixelation length) references L_max. The FWD-C5 cardinality bridge is built on the g-axis cascade (generation count), NOT the L_max-axis rep-ring growth; the substrate's PBH-formation physics terminates at cascade SATURATION (g_saturate=143). The L_max=14 label conflated the L_max-axis (eigenvalue-count, unbounded) with the g-axis (cascade-generation, saturating).
- **(D2) Tier-2 dimensionless re-anchoring** (the §VII.AV.STATE-PROJ route): a log-derivative functional annihilating the dimensionful prefactor — yields the dimensionless cascade exponent (→5), a SHAPE not the magnitude. Admissible but does not fix the m⁻³ number; not selected as the substrate-physical scale anchor.

**The decisive numerical finding (why INFO, not PASS).** The SELECTED substrate-physical axis (D1) is L_max-INDEPENDENT, but its frozen-N saturated form delivers the **L_max=10 baseline 1.758e-23 m⁻³**, NOT the canonical **L_max=14 7.2761e-23 m⁻³**. The two differ by exactly the **4.1385× refinement factor** `N_eigs(14)/N_eigs_base = 323136/78080` (= `canonical/baseline = 4.1385`). This 4.14× is precisely the irreducible L_max-axis dependence the Tier-2-dimensionful finding (Step C) localizes: the canonical magnitude lives in the divergent LINEAR channel, while the substrate-physical (L_max-independent) g-axis anchor lives at the L=10 baseline. So the anchor **AXIS is correctly identified**, but pinning the canonical *magnitude* at it is a separate saturated-tail recompute — **DEFERRED to CF-S95** (which must additionally source N from a substrate-singled-out point, since the S93 workshop established the L=10 cache atlas N=78,080 = analytic 80,080 − dropped (4,4) sector is itself frozen-by-fiat, not a saturation point).

**Step E — updated truncation label.** `"L_max=14 PROVISIONAL"` → `"g_saturate=143 cascade-saturation anchor (substrate-physical, L_max-INDEPENDENT g-axis); m⁻³ magnitude Level-3 row HELD Tier-2-dimensionful per cross-pillar-bridge-anatomy.md; canonical 7.2761e-23 carries irreducible L_max-axis 4.14× refinement (L=10 baseline 1.758e-23 → L=14) ⇒ magnitude pin deferred to CF-S95"`.

**Solution-space (substrate framing).** The substrate IS the spectral triple `(A_K, H_K, D_K(τ_fold=0.19))`; N_eigs(L_max) is the substrate's own cardinality cascade, unbounded because the SU(3) representation ring is infinite — a GENUINE substrate property, not model-incompleteness. The direction of explanation flows D_K eigenvalues → cardinality cascade (g-axis generation count) → n_edge saturation at g_saturate=143 → n_PBH band-edge prediction; the truncation is sourced from the substrate's PHYSICS (where the cascade physically FILLS), not from a container-side L_max cutoff. This [CHAIN] CONFIRMS the S93 W-1 workshop's HOLD-the-anchor verdict from the substrate-physical side and discharges the "which anchor" half of the open question: the anchor IS the g-axis cascade-saturation; the m⁻³ magnitude pin (1.758e-23 baseline vs 7.2761e-23 refined) is the remaining numerical corridor (CF-S95). **§VII.AX.OP-PROJ theorem-STRUCTURE remains STAGE-3-PERMANENT (Tier-2 corollary); only the dimensionful m⁻³ Level-3 scalar-inequality row stays HELD.** Verdict-line cross-references: the band-breach point L_breach (W5-2) and the §VII.AX Level-3-row discharge/canonical promotion are downstream wave-close steps, not part of this COMPUTE gate.
"""


def patch_once() -> str:
    """Read-modify-write the §W5-1 block. Returns a status string."""
    text = WP.read_text(encoding="utf-8")
    # Idempotency: if my section already shows COMPLETED + my audit SHA, no-op.
    h_idx = text.find(HEADER)
    if h_idx == -1:
        return "ERR_HEADER_NOT_FOUND"
    # Find the end of MY section: the next '\n---\n' after the header.
    end_rel = text.find("\n---\n", h_idx)
    if end_rel == -1:
        return "ERR_DELIM_NOT_FOUND"
    current_block = text[h_idx:end_rel]
    if "**Status**: COMPLETED" in current_block and AUDIT_SHA in current_block:
        return "NOOP_ALREADY_DONE"
    # Replace exactly [h_idx, end_rel) with NEW_BLOCK (NEW_BLOCK ends with one '\n';
    # the preserved '\n---\n' delimiter follows). Everything else byte-untouched.
    new_text = text[:h_idx] + NEW_BLOCK + text[end_rel:]
    WP.write_text(new_text, encoding="utf-8")
    return "PATCHED"


def main() -> None:
    for attempt in range(1, 9):  # bounded retry under parallel-writer race
        before = WP.read_bytes()
        status = patch_once()
        if status in ("PATCHED", "NOOP_ALREADY_DONE"):
            # verify the write landed and was not clobbered by a concurrent writer
            after = WP.read_text(encoding="utf-8")
            h_idx = after.find(HEADER)
            blk_end = after.find("\n---\n", h_idx)
            blk = after[h_idx:blk_end] if (h_idx != -1 and blk_end != -1) else ""
            if "**Status**: COMPLETED" in blk and AUDIT_SHA in blk:
                print(f"attempt {attempt}: {status} + verified on disk")
                return
            print(f"attempt {attempt}: {status} but verify failed (clobbered?), retrying")
            time.sleep(0.4)
            continue
        print(f"attempt {attempt}: {status}")
        if status.startswith("ERR"):
            sys.exit(2)
        time.sleep(0.4)
    print("FAILED to land §W5-1 after retries")
    sys.exit(1)


if __name__ == "__main__":
    main()
