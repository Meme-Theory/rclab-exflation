---
name: stage3-promotion-cohort-planning
description: Authoring a §VII registry-completion / STAGE-3-promotion cohort plan wave (parallel-compute Q3, four INDEPENDENT registry-landing gates each closing the ONE held leg of a prior blind Stage-2 PASS-AND)
metadata:
  type: feedback
---

When a wave plans a §VII STAGE-1→STAGE-3 promotion cohort (each gate closes the single completeness/provenance gap that HELD a prior-session blind Stage-2 PASS-AND), the structure is **parallel-compute Q3** (`Investigating-Workshops.md`): N INDEPENDENT registry-landing gates, each its OWN PASS criterion, **NO wave-level AND**. Per-gate agent attribution = derivation-author tag, NOT workshop-participant — no adversarial round protocol (the legs are structurally orthogonal: a Mellin-poleconv resolution, two Element-2 OE-form retrofits on different pillars, a SHA-harvest verification do not rebut one another).

**Why:** S108 W2 — the four S107 INFO composites (K2/K11/K7/K9) all PASS-AND'd blind on EVERY structural clause; the INFO was a HELD registry-completeness leg, NOT a structural FAIL. The promotion is genuinely-owed bookkeeping (per `joint-theorem-promotion.md §Stage 3`), but each gate still does real substrate-physics determination ⇒ COMPUTE/registry-landing-class, NOT METHODOLOGY (FAILS M3 "no new derivation"); NO allowlist append owed.

**How to apply (the load-bearing moves):**

1. **VERIFY the "promotion is owed" claim on disk before pinning it.** The context-file 4-field spec said §VII.AG.1 → STAGE-3; trace_entity showed it was ALREADY STAGE-3 (promoted S105 W6-2) ⇒ that gate is Element-2 OE-form HYGIENE only, NO promotion. ALWAYS `trace_entity` each entry's current Status; the CF spec may be stale.

2. **The "N of 6 anchors" diagnostic is often STALE.** §VII.X.2-NECESSITY entry text said "2 of 6 available" (S87-era); the S88 LAMBDA-SA-{S46,S64,S65,S77,C9}-SUCCESSOR-EMISSION family RE-EMITTED 5 anchors at S88 + the S82/S87 primary ⇒ 6/6 ARE on disk. The S88 promote-gate even reported `anchor_presence=6/6=TRUE` but DEFERRED promotion ONLY because Stage-2 was solo-mode (couldn't satisfy independence); the blind two-axis Stage-2 PASS-AND landed later (S107 `4d98f916`). The harvest-verification gate's value = grep `audit_sha256=[0-9a-f]{64}` on the named anchor lines. WATCH: the S88-script enumeration ("anchor 6" = the S87 aggregation gate `fa225aac` ITSELF) can name a DIFFERENT 6-set than the registered table (anchor-5 = S82 MP-Exclusion `98267d63`); both are on disk ⇒ PASS, but pre-register an INFO branch for the enumeration reconciliation.

3. **Mellin poleconv resolution is a Sage-exact substitution chain, not an assertion.** `regulator-pin-discipline.md §"Mellin Pole-Set Labeling"`: Conv-A `n=d-2s`, Conv-B `n=d-s`; {0,2,4,6,8} is ALWAYS the curvature grade n. To reconcile THREE non-reconcilable pole tokens {s=3, substrate-distance-1, a_4^ζ↔n=4}: solve for the UNIQUE (d, conv) yielding s=3 with an even non-negative grade. Result: (d=8 SU(3) spectral-triple dim, poleconv-A-double) ⇒ n=2 (a_2 channel) — matching the §VII.CB/§VII.U.6/§VII.T/§VII.AF.1/§VII.AU sibling family. The registered `a_4^ζ` (n=4) is the MIS-LABEL (n=4 sits at s=2 A-double / s=4 B-single at d=8, NOT s=3). PIN the candidate; let the executor confirm-or-document-which-token-is-mislabel as a Class-1 disclosure (NOT convention-shopping).

4. **Block-level Element-2 audit ≠ per-cell completeness.** `_cross_pillar_bridge_audit.py` grades §VII.X.W4-1 Element-2 as block-level PASS (the q=IV cells carry the band-projector OE-form, satisfying ANY-match regex), but the S107 reviewer's HELD leg is the granular per-q=II-cell check (the 6 q=II cells lack the named projector). Write the gate PASS criterion as "all 6 q=II cells" (the stricter Stage-2 granularity), NOT "block-level regex PASS". The genuinely-defective-count==0 cross-check (W2-3 §VII.AG.1) IS reliable at block level.

5. **All four gates = bridge-landing single-shot AFTER-pattern** (`registry-landing.md`): each writes a registry/atlas edit + emits a verdict in the same run ⇒ `build_promotion_text → write_atomic_with_fsync → re_read+verify_section_matches → emit ONE line`. Pin `build_promotion_text`+`write_atomic_with_fsync`+`verify_section_matches` in `output_artifacts.script.must_contain` to enforce at the artifact layer. Match registry blocks by SECTION HEADER not line number (registry drifts across waves).

**Validators that must clear at plan-freeze:** `_yaml_gate_validator.py` (4/4 R3 PASS, cutoff_axis N/A), `_pru_cardinality_audit.py` (self-test PASS), gate-ID no-collision vs prior-session space, 0 forbidden verdict-path variants. Pin per-gate-distinct `audit_sha256` via distinct gate_id + distinct registered-entry-block input (sig_5 by construction; `emit_verdict` rejects reuse at write-time).
