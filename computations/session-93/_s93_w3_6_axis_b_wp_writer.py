#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Atomic read-modify-write of the §W3-6 WP Axis-B (mack) cross-review subsection.

Keyed on a UNIQUE Axis-B anchor; idempotent; does NOT touch the Axis-A subsection
or the §W3-6 header. Per `epistemic-discipline.md §"Registry-Write Hygiene"`:
append-only Python writer (atomic os.replace), not Edit-tool round-trip; safe under
the concurrent Axis-A writer. One-shot helper for the W3-6 Axis-B dispatch.
"""
import os
import re
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent  # (local)
WP = PROJECT_ROOT / "sessions" / "session-93" / "session-93-w3-workingpaper.md"  # (local)
HEADER = "### §W3-6. S93-W3-6-VII-AV-STAGE-2-CROSS-AXIS-VERIFY-PER-SUB-SLOT"  # (local)
AXISB_ANCHOR = "#### Axis-B (mack) cross-review"  # (local)

SUBSECTION = r"""
#### Axis-B (mack) cross-review

**Status**: COMPLETED (Axis-B independent audit + producing-script authorship; final W3-6 verdict line NOT emitted — awaiting orchestrator-triggered aggregation step once both axis JSONs are consumed).
**Verdict**: PASS (Axis-B side, BOTH sub-slots) — see PASS-AND composition note below.
**Reviewer**: `mack-cosmic-bridge` (Axis-B, cosmological-bridge / substrate side). Admissible: registry sole-writer who transcribed the workshop VERDICT, NOT a W-3 workshop AUTHOR; OAA exclusion set {connes-ncg, phonon-first, volovik} excludes the actual authors.

**MCP Pre-Compute Audit** (per `knowledge-index-usage.md`):
- `search_knowledge("VII.AV OP-PROJ STATE-PROJ Cell I Cell IV slot split")` -> confirms B_LAYER_A=375.227 (Cell I), B_LAYER_B=-7.046336 (Cell IV); cross-corner co-primary FORBIDDEN; structural-orthogonal-companion.
- `search_knowledge("VII.AV STATE-PROJ L_emp K-window log-derivative substrate-distance-2 pole s=4")` -> L_emp=-7.046336474406761 M_KK^2; `S89-CORNER-IV-K-WINDOW-LOG-DERIVATIVE-RECOMPUTE` PASS (sign=PASS mag=PASS reg=VALID).
- `trace_entity("B_LAYER_A layer attribution disambiguation")` -> gate `S92-W3-CF-S92-W5-1-C-VII-AV-LAYER-ATTRIBUTION-DISAMBIGUATION`: B_LAYER_A=3.752271e+02, B_LAYER_B=-7.046336, F_image=7.046336, Phi_consistency_ratio=52.2514.
- `get_constant("tau_fold")`=0.19 (CONST-FREEZE-42); `get_constant("M_KK")`=7.428660036284456e+16 (gravity route). NOT PRE-CLOSED (Stage-2 verify of STAGE-1-CANDIDATE sub-slots is a new gate).

**Independence protocol (Axis-B)**: audited ONLY the registered Stage-1 entries §VII.AV.OP-PROJ (lines ~18445-18496) + §VII.AV.STATE-PROJ (lines ~18499-18553); did NOT read the W-3 / S91 / S92 workshop transcripts; did NOT read the Axis-A (vdd) verdict during my independent audit (the Axis-A JSON appeared on disk mid-dispatch but was NOT opened for verdict content — only its top-level KEY SCHEMA was inspected afterward, to make the aggregation reader schema-robust). Substrate-input orthogonality (Axis-B side): loaded ONLY the OP-PROJ residue cache (`s93_w3_3_..._witness.npz` + `s92_w3_9_..._disambiguation.npz`); did NOT load the STATE-PROJ runtime npz `s91_w5_1_full_bdg_pv.npz` (Axis-A's orthogonal input). Structural-ceiling orthogonality on the Axis-B side satisfied.

**Substrate framing** (per `phononic-framing.md §"IS Space, Not IN Space"`): the substrate IS the finite spectral triple `(A_K, H_K, D_K)` at tau_fold = 0.19. The two sub-slots are its algebra-axis-ORTHOGONAL observables — OP-PROJ (Cell I, algebra-INVARIANT spectrum-only trace-residue; the KK-tower/Casimir spectral structure, Greene-compactification heritage [Mack-corpus 19 Casimir stabilization, 22 KK-tower splitting]) and STATE-PROJ (Cell IV, algebra-DEPENDENT state-pair K-window log-derivative on the BdG sub-algebra; the Leggett-channel GGE quasiparticle = CPT-neutral, gapped, non-annihilating hidden-sector-DM analog [Mack-corpus 15/16 hidden-sector DM; underlying s52 8-mode Bogoliubov amplitude = Greene 25/26 Bogoliubov-production-as-brane-transit]). Direction-of-explanation preserved: substrate IS the observable -> HKR/Connes-(Moscovici/Karoubi) bridge -> laboratory-IN continuum image; NOT inverted.

**Axis-B per-clause verdicts** (formed FIRST, from first principles, before any aggregation):

*§VII.AV.OP-PROJ (Cell I) — Axis-B:*
- **AxisB-OP-1** (substrate-IS cosmological-bridge identity) = **PASS** — spectrum-only Tr terminus, NO state-pair dependence, single-tau-slice tag at tau_fold=0.19; the algebra-INVARIANT KK/Casimir spectral family.
- **AxisB-OP-2** (laboratory-IN OE-form) = **PASS** — `int_BZ d^d k Tr_{A_K}(P_a*rho_BZ(k;tau_fold))` satisfies the OE-form positive regex (int domain + Tr + named projector P_a).
- **AxisB-OP-5** (empirical anchor) = **PASS** — B_LAYER_A = 3.752271e+02 M_KK^2 INDEPENDENTLY RE-DERIVED on Axis-B from the per-sector contributions (0,2)=85.48551 + (1,1)=204.25607 + (2,0)=85.48551 = **375.2270869158** (matches recorded to <1e-6); the conjugate pair (0,2)/(2,0) contributions coincide to <1e-6 (Class-8.7 degeneracy: n_deg=1, mult=2).
- **AxisB-OP-L3** (Level-3 eligibility gated by W3-3) = **PASS** — W3-3 Class-8.7 witness PASS (`cross_reg_spread_rel=0.190765` ~19% within heat-kernel-moment-ratio ub=0.30; NOT a direct-sum tautology); the ~375 anchor is Level-3-ELIGIBLE.
- **JOINT-OP-3** (bridge map HKR/Connes-Moscovici) = **PASS** (Axis-B side) — explicitly named map (not "analogous"), Element-3 binding type (i) substrate-self-consistent declared; PASS-AND with Axis-A computed at aggregation.
- **JOINT-OP-ORTHO** (structural-orthogonal-companion; cross-corner FORBIDDEN) = **PASS** (Axis-B side) — INDEPENDENTLY CONFIRMED: Phi-correspondence consistency metric `|375.2271/7.046336 - 1| = 52.2514` (re-derived; matches recorded 52.25137) >> phi_info_ceiling=0.3 by >2 OOM => F_IMAGE_INCONSISTENT => the two observables are genuinely distinct objects on orthogonal cells, NOT two regulator-class F-images of one observable. Split robust to the metric definition (bare ratio 53.25 OR deviation 52.25, both >> 0.3).

*§VII.AV.STATE-PROJ (Cell IV) — Axis-B:*
- **AxisB-SP-1** (substrate-IS cosmological-bridge identity) = **PASS** — state-pair functional (Var_a / d(ln)/d(ln K)) on a gapped occupation distribution; the Leggett-channel GGE quasiparticle; gap `|Delta_a|=0.4642547 M_KK` = the hidden-sector mass gap that IR-self-regularizes the observable.
- **AxisB-SP-2** (laboratory-IN OE-form) = **PASS** — `int_{BZ-BdG} d^d k Tr_{M_2(C)}(P_BdG*rho_BZ(k;tau_fold))*(d ln*/d ln K)` satisfies the OE-form regex; laboratory-IN = Pillar V 3He-B BdG-sector mutual-friction (the 3He-B inheritance morphism).
- **AxisB-SP-5** (empirical anchor) = **PASS** — L_emp(L_max=12) = -7.046336474406761 M_KK^2 (SOLE Cell-IV anchor), substrate-natural-binding; verified from registered entry + cited input (s92_w3_9 `L_emp_canonical` key) WITHOUT loading the Axis-A runtime BdG npz; sign negative by BdG curvature (physically correct).
- **AxisB-SP-SINGLE** (Level-3 singleness guard) = **PASS** — the FULL-PV value -527.966919 M_KK^2 (m_PV=M_KK) is a Level-2-B regulator-class DIAGNOSTIC sub-row on the m_PV-flow, NOT a Level-3 co-primary (Hybrid Independence Test FAILS for any split of THIS pair: identical pillars + identical HKR bridge-map class); singleness guard correctly forbids co-primary.
- **JOINT-SP-3** (bridge map HKR/Connes-Karoubi; Level-2-binding) = **PASS** (Axis-B side) — Level-2-binding certified by W3-4 (`L_CK_12=-7.046054`, `residual_L12=2.82e-04 < tol=1e-03`, prefactor 8/9 exact, c_continuum=L_emp, Connes-Karoubi chi'-K0 pairing); the bridge BINDS (NOT a non-binding bare-decomposition rate). PASS-AND with Axis-A at aggregation.
- **JOINT-SP-ORTHO** (structural-orthogonal-companion) = **PASS** (Axis-B side) — same Phi discriminator (52.25 >> 0.3) confirms Cell IV != Cell I; sibling caveat independently verified: `substrate_cocycle_ratio_67_88`=7.324992 (§VII.AY) != |L_emp|=7.046336 (§VII.AV) — distinct objects, shared cohomology-class character only.

**Axis-B sub-slot summary**: §VII.AV.OP-PROJ = **PASS** (Axis-B); §VII.AV.STATE-PROJ = **PASS** (Axis-B). All Axis-B single-axis clauses + both JOINT clauses (OP/SP x bridge-map/ortho) PASS on the Axis-B side.

**PASS-AND composition (deferred to aggregation step)**: the final W3-6 composite is `(Axis-A_vdd AND Axis-B_mack AND JOINT PASS-AND)` per sub-slot AND substrate-input-orthogonality AND OAA-exclusion AND convention-ends-`-FULL`. The producing script `s93_w3_6_vii_av_stage_2_cross_axis_verify.py` is authored and READS both axis JSONs with a schema-robust reader (the two axes wrote schematically different JSONs — different sub-slot key spelling, different clause-group names, different JOINT-clause key strings; the reader pairs JOINT clauses by SEMANTIC identity and walks substrate-input keys key-path-aware). Dry-run (no `--emit`) confirms on the Axis-B side: substrate-input-orthogonality structural ceiling = TRUE (STATE-PROJ npz loaded only by Axis-A; OP-PROJ cache loaded only by Axis-B — NO overlap caveat, S89 W4-7 §VII.AH precedent), OAA-exclusion satisfied, convention ends `-FULL`. The final composite verdict + emission (Option-A `supersedes=d6f990a70111774af2314a814602e510b36154e2c24ff52761bd688c4274771c`) is the SEPARATE orchestrator-triggered step.

**Output Artifacts** (Axis-B dispatch; NOT the emission step):
- `computations/session-93/s93_w3_6_axis_b_mack_verdicts.json` — Axis-B per-clause verdicts (PRESENT).
- `computations/session-93/s93_w3_6_vii_av_stage_2_cross_axis_verify.py` — producing/aggregation script (PRESENT; must_contain `from canonical_constants import`, `append_verdict`, `PASS-AND`, `substrate_input_orthogonality`, `supersedes=d6f99...4274771c`, `-FULL` ALL present; compiles; ready-to-run with `--emit`).
- `computations/session-93/s93_w3_6_vii_av_stage_2_cross_axis_verify.json` — dry-run aggregation sidecar (`verdict_line_emitted=false`).
- W3-6 verdict line in `s93_gate_verdicts.txt`: **NOT emitted** in this dispatch (awaiting aggregation step).
"""


def main() -> int:
    text = WP.read_text(encoding="utf-8")  # (local)
    if AXISB_ANCHOR in text:
        print("IDEMPOTENT: Axis-B subsection already present; no re-insertion.")
        return 0
    if HEADER not in text:
        raise SystemExit(f"FATAL: §W3-6 header not found: {HEADER!r}")

    hdr_idx = text.index(HEADER)  # (local)
    rest = text[hdr_idx:]  # (local)
    # Insert BEFORE the first section-closing delimiter line ('---' on its own line)
    # that follows the §W3-6 header — i.e. at the end of the §W3-6 block, after any
    # Axis-A subsection. Keeps the header + Axis-A subsection + closing '---' intact.
    m = re.search(r"\n---\n", rest)  # (local)
    if m:
        insert_at = hdr_idx + m.start() + 1  # (local) keep the leading '\n'
        new_text = text[:insert_at] + SUBSECTION + text[insert_at:]  # (local)
    else:
        new_text = text + SUBSECTION  # (local)

    tmp = WP.with_name(WP.name + ".tmp_axisb")  # (local)
    tmp.write_text(new_text, encoding="utf-8")
    os.replace(tmp, WP)
    print("WROTE Axis-B subsection into §W3-6 (atomic os.replace).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
