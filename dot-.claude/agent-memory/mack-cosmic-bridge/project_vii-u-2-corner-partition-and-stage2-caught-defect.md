---
name: vii-u-2-corner-partition-and-stage2-caught-defect
description: §VII.U.2 4-corner partition is (algebra-axis)×(Mellin pole) — Cell I=INVARIANT×s=3, Cell II=INVARIANT×s=4, Cell III=DEPENDENT×s=3, Cell IV=DEPENDENT×s=4; plus the Stage-2-caught-corner-cell-defect→INFO adjudication pattern
metadata:
  type: project
---

## §VII.U.2 four-corner partition (convention-translation fact)

The 4-corner cell of any `(A_K, H_K, D_K)` observable is the cross-product **(algebra-axis ∈ {INVARIANT, DEPENDENT}) × (Mellin pole ∈ {s=3, s=4})**, NOT algebra-axis alone. Source: `permanent-results-registry.md:12994` (clause (d) partition table), rows at `:12998-13001`:

- **Cell I = algebra-INVARIANT × s=3** (substrate-distance-1 pole). E.g. §VII.U.1 Mellin-Dirichlet identity; `α_s_canonical = n_s²−1` at s=3.
- **Cell II = algebra-INVARIANT × s=4** (substrate-distance-2 pole). E.g. Var_a(n_a^GGE); §VII.AV.OP-PROJ trace-residue B_LAYER_A=375.227.
- **Cell III = algebra-DEPENDENT × s=3**. E.g. full M_n(ℂ) Connes distance.
- **Cell IV = algebra-DEPENDENT × s=4**. E.g. §VII.AV.STATE-PROJ K-window log-derivative L_emp=-7.046336.

**Trap (S93 W3-6):** an algebra-INVARIANT spectrum-only `Tr` functional at **s=4** is **Cell II**, NOT Cell I. The parse-tree `Tr` terminus only fixes the ALGEBRA-axis (INVARIANT); the Mellin pole (s=4) is the OTHER axis and pins II vs I. §VII.AV.OP-PROJ was mislabeled Cell I at S93 W3-1/W3-5 and corrected to Cell II at S93 W3-6.

**Direct precedent:** Var_a Cell I→Cell II retraction, **CF-25 S90 W2** (`permanent-results-registry.md:13043`) — same reason (algebra-INVARIANT × s=4 ⇒ Cell II). When classifying an INVARIANT observable, ALWAYS check the pole: s=3→Cell I, s=4→Cell II. Cross-corner co-primary FORBIDDEN; the GENERIC "Cell I (INVARIANT × substrate-distance-1)" boilerplate in cross-corner-FORBIDDEN clauses is the s=3 canonical and must NOT be flipped when remediating an s=4 entry.

## Stage-2-caught-corner-cell-defect → INFO adjudication (reusable pattern)

When a Stage-2 cross-axis verify's Axis-A FAIL is driven SOLELY by a `corner_cell_classification` clause (a CLASSIFICATION defect, not a substrate-physics refutation), and (a) the defect is remediated in-session, (b) all OTHER clauses (single-axis + JOINT) PASS on both axes, (c) the companion sub-slot is a clean PASS-AND:

- **Composite verdict = INFO** (NOT FAIL). The clean sub-slot is STAGE-3-ELIGIBLE; the defect sub-slot stays **STAGE-1-CANDIDATE-PENDING-S{N+1}-REVERIFY**.
- **Why:** per `joint-theorem-promotion.md §"Stage 2"`, a FAIL on ANY clause blocks Stage-2→3 — so the as-registered FAIL still blocks promotion (requires a re-verify on the corrected entry). But the FAIL is a caught classification defect, and the INFO criterion ("the other sub-slot may still PASS independently") + the clean companion route the COMPOSITE to INFO, not FAIL. Distinguish `composite_hard_fail` (Axis-B FAIL / JOINT not PASS-AND / non-corner-cell Axis-A FAIL / structural-gate FAIL) from `composite_info` (corner-cell-remediated). The Stage-2 verify CATCHING the defect IS its purpose — report it as a successful catch, not a refutation.
- **PASS-CONDITIONAL resolution:** a reviewer's `PASS-CONDITIONAL` clause (PASS gated on a condition, e.g. a witness gate) resolves to PASS iff the condition is MET — read the condition's verdict from the verdict file; record `conditional_upgraded=true`. Not a silent override.

## STAGE-3-PERMANENT cross-axis-joint-theorem ordinal is CONTESTED (do NOT assert a bare integer)

When recording a NEW STAGE-3-PERMANENT cross-axis joint theorem, do NOT assert "the Nth" without re-verifying — the registry's own ordinal bookkeeping has a **pre-existing collision**: BOTH §VII.AU.OP-PROJ (`permanent-results-registry.md:18908`/`:19297`) AND §VII.AW.OP-PROJ (`:18374`) claim "THIRD framework cross-axis joint theorem to reach STAGE-3-PERMANENT." Confirmed FIRST=§VII.AH (S90 W2 CF-20, `:15785`), SECOND=§VII.U.2 Var_a (S92 W4-7, `:13095`); then AU/AW both claim #3. §VII.AV.STATE-PROJ (S93 W3) joined the set as ≥5th but the integer is contested. **Discipline:** record membership in the STAGE-3-PERMANENT set + cite the prior members, but flag the ordinal as a hygiene carry-forward (CF-S94-STAGE-3-ORDINAL-COLLISION-AU-AW) rather than propagating a guessed number. "STAGE-3-PERMANENT" (Status line, fully promoted) is DISTINCT from "STAGE-3-PERMANENT-eligible" (e.g. §VII.AZ.OP-PROJ `:19625`, tag-flip pending) — count only the former.

Stage-3 session-synthesis flip = single-shot AFTER pattern at THREE markers (index row, section header, `**Status**:` line); preserve Stage-1/Stage-2 history as provenance (§VII.AH/§VII.AU.OP-PROJ precedent). It is a NEW gate-ID record line (no Option-A supersedes — not a supersession of the W3-6 Stage-2 verdict, which stays unchanged).

Cross-link: [[phi-correspondence-consistency-metric]] (the F-image-consistency discriminator that drove the §VII.AV split); `joint-theorem-promotion.md §"Stage 2"` / §"Stage 3" / §"Substrate-input-orthogonality clause" (structural-ceiling, S89 W4-7 §VII.AH FIRST-INSTANCE-WITHOUT-caveat precedent). Implementation: `computations/session-93/s93_w3_6_vii_av_stage_2_cross_axis_verify.py` (Stage-2 aggregation) + `s93_w3_6_vii_av_state_proj_stage_3_promotion.py` (Stage-3 flip).
