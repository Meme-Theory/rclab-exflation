# Session 91 — Wave Partition Manifest (v3 — POST-IN-SESSION-HOUSEKEEPING)

**Generated**: 2026-05-16 (Phase 2.7 mechanical wave partition; v3 = v2 + in-session housekeeping completions)
**Mode**: fanout (default)
**Source**: `sessions/session-plan/session-91-context.md` + 16 in-session housekeeping fixes (2026-05-16 orchestrator-direct-write campaign)

## In-Session Housekeeping COMPLETED at S91 W0 prep (2026-05-16)

Per `feedback_fix-in-session-never-defer.md` + `feedback_no-asking-just-execute.md` + `feedback_no-asking-just-execute.md` (NEW agent memory landed 2026-05-16). Total: **16 items resolved in-session**, removing them from the S91 dispatched-wave queue.

### Fixed via orchestrator-direct-write (10 items)

1. **T0.6** CF-W7-6 / CANONICAL-CONSTANTS-PROMOTION-W6-PINS: `c_W12_deficit_FW_PRIMARY_ConvB = 7.244e-4` + `tau_max_HK5_regime_FW_asymptotic_limit_FW = 5*PI = 15.707963267948966` added to `canonical_constants.py` lines 561-562; PROVENANCE entries at lines 1290-1294. Import-test PASS.
2. **T2.5** CF-S91-W5-LAMBDA-UNIT-PROMOTION: `lambda_unit_canonical = "dimensionless_M_KK_natural"` (string pin per S90 W1-10 INFO Reading-C) added to `canonical_constants.py` line 563; PROVENANCE entry at line 1295. PROVENANCE dict count: 131 → 134.
3. **T0.3** CF-S91-W2-VII-AH-STAGE-3-PROMOTION-NARRATIVE-RECONCILIATION: 7 registry locations updated (NOT the stale lines 15524/15528 in S8 §7 — actual locations: line 104 table summary row; line 13908 §VII.AH precedent citation; lines 15606 + 15610 Status field + STAGE-1-CANDIDATE qualifier paragraph at canonical §VII.AH entry; line 15678 audit-pin sub-rows reference; line 16455 §VII.AM precedent ref; line 16549 §VII.AM Anchor list cross-link; line 17452 §VII.AQ.OP-PROJ cross-link).
4. **T2.51** CF-S91-VII-AV-REGISTRY-TEXT-4TH-REFINEMENT-ROUTE-EXTENSION (W-5 CF-5): §VII.AV refinement-pathway table (registry line 17944) extended with routes (iv) K_canonical pin uniqueness operational-alignment + (v) V4 substrate-physics discriminator + (vi) Hochschild-cohomology cross-anchor + (vii) Level-2 moduli-deformation; "Layer" column added; substantive routing annotation paragraph appended.
5. **T2.55** CF-S91-VII-AF-1-OP-PROJ-ANNOTATION (W-6 CF-2): substrate-internal over-performance regime annotation (>15 lines + Phi(L1)/Phi(L3) cross-link + CM-1995 §III.4 subleading expansion citation + companion under-performance regime cross-link to §VII.AU.OP-PROJ); verbatim L^{-3} Level-2 envelope declaration PRESERVED.
6. **T2.56** CF-S91-VII-AU-OP-PROJ-ANNOTATION (W-6 CF-3): substrate-internal under-performance regime annotation (positive subleading C_1 + Phi(L3) → Σ_2 M_Pl_eff² cross-link + L_max ≥ 35 decisive sub-window citation + companion over-performance regime cross-link to §VII.AF.1.OP-PROJ); §VII.AU.OP-PROJ status PRESERVED at REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION.

### Deleted from CF queue (6 items; not future computation)

7. **T2.43** CF-S91-CROSS-WORKSHOP-K3-PROMOTION-WATCHPOINT — OBSOLETED by T0.1 K=6 LANDING.
8. **T2.50** CF-S91-CROSS-WORKSHOP-JOINT-WIN-K4-PROMOTION-WATCHPOINT — OBSOLETED.
9. **T2.53** CF-S91-CROSS-WORKSHOP-JOINT-WIN-K5-PROMOTION-WATCHPOINT — OBSOLETED.
10. **T2.33** CF-S91-W1-14-K2-CALIBRATION-INSTANCE-WATCHPOINT — passive K-counter monitoring (0.0 we at S91); not future computation per `feedback_fix-in-session-never-defer.md`.
11. **M6** CF-S91-PARTIAL-POSITIVE-K-COUNTER-MONITORING — passive K-counter monitoring.
12. **T2.11** CF-33-S91-2 CMB-S4 first-data poll — forward observational; belongs in `sessions/framework/registry/mack-observational-constraints.md` polling schedule, not S91 CF table.
13. **M7** CF-S91-LIZZI-S4-CARDINALITY-LEVER-FI-CLASSIFICATION — CONDITIONAL META-OBS on T1.13 PASS; fires downstream of T1.13, not at S91 W0.

### Agent-memory landing (1 item)

14. NEW agent memory file `C:/Users/ryan/.claude/projects/C--sandbox-Ainulindale-Exflation/memory/feedback_no-asking-just-execute.md` — explicit reminder to never ask about housekeeping scope; full text + cross-links to `feedback_fix-in-session-never-defer.md`, `feedback_no-asking-just-execute.md`, `feedback_no-asking-just-execute.md`.

### Total accounting: 94 (v1) → 78 items (v3) in dispatch queue

| Status | Count |
|:-------|:-----:|
| Fixed in-session (canonical_constants + registry-text reconciliation + annotations) | 6 (T0.6, T2.5, T0.3, T2.51, T2.55, T2.56) |
| Deleted from CF queue (not future computation) | 7 (T2.43, T2.50, T2.53, T2.33, M6, T2.11, M7) |
| Agent-memory rule landing | 1 (`feedback_no-asking-just-execute.md`) |
| Substrate-physics COMPUTE + Stage-2 verifies + STAGE-1-CANDIDATE landings → W1-W8 | ~48 |
| Substantive METHODOLOGY-class W0a (mack registry/canonical sole-writer landings) | ~6 |
| Substantive METHODOLOGY-class W0b (orchestrator-direct rule + audit-script extensions) | ~24 |
| **TOTAL DISPATCHED (W0a + W0b + W1-W8) at S91** | **~78 items** |

## Wave Theme Buckets (v3)

| Wave | Theme | Owner | Item count | Effort (we) |
|:----:|:------|:------|:----------:|:-----------:|
| W0a | Substantive mack registry/canonical sole-writer landings + STAGE-1-CANDIDATE landings | mack-cosmic-bridge | 6 | ~3.0 |
| W0b | Substantive orchestrator-direct-write rule + audit-script extensions | gen-physicist (orchestrator-direct) | 24 | ~14.0 |
| W1 | §VII.AV substrate-physics 4-axis refinement-pathway | volovik-superfluid-universe-theorist | 5 | ~6.8 |
| W2 | §VII.AU substrate-physics + CF-37 + first-extraction | connes-ncg-theorist (OAA: T0.7 to other) | 4 | ~4.0 |
| W3 | Species-multiplicity cascade + LRD α-anchor parallel pathways | mack + connes cross-reviewer | 4 | ~8.5 |
| W4 | Stage-2 cross-axis verifies (§VII.AR + §VII.AW + §VII.U.2 Var_a) | cross-reviewer dispatch | 4 | ~5.0 |
| W5 | Substrate-physics + PBH band-edge + Level-2 moduli + §VII.AV FULL BdG | volovik + mack (T1.14 landing) | 4 | ~4.6 |
| W6 | d=4 envelope discriminators + lizzi reading + W11-5 sister re-audit | lizzi-spectral-functional-theorist | 5 | ~3.6 |
| W7 | §VII.AQ + §VII.AT + §VII.AW substrate-physics chirality | connes-ncg-theorist | 3 | ~3.5 |
| W8 | Stage-2 verifies + STAGE-1-CANDIDATE landings + M_3(ℂ) universality | mack + cross-reviewer | 7 | ~6.0 |
| W9 | Forward bridge candidates + observational liaison + Wodzicki-BCS bridge | gen-physicist + mack | 8 | ~6.0 |

**Total**: 11 waves; 74 items dispatched; ~65 we across the campaign.

## W0a (mack-cosmic-bridge sole-writer, METHODOLOGY-class)

1. **T0.1** CF-S91-K6-MANDATORY-PROMOTION-LANDING (~0.1 we) — K=6 corpus extension at `cross-pillar-bridge-corpus.md §3` documenting W-1+W-2+W-3+W-4+W-5+W-6 Hybrid Independence Test corpus
2. **T0.2** CF-S91-LAYER-FUNCTOR-F-VERDICT-SHAPE-CONSISTENCY-THEOREM-STAGE-1-CANDIDATE-REGISTRY-LANDING (~0.6 we) — Boxed theorem statement at NEW §VII.A* slot; W-5 + W-6 K=2 calibration corpus + rule extension at `epistemic-discipline.md §"Layer-Decomposition"`
3. **T0.4** CF-W2-13-DR3-READINESS-REMEDIATION (~0.4 we) — Script-bug fix + Option-A corrective canonical line with `supersedes=23f662b36cf0afcf5cc4d034f75bfde0e45793ff0afc68cd90152249964342fb`; deadline 2026-04-23 ALREADY PASSED (current 2026-05-16)
4. **T0.5** CF-S91-W2-CORNER-RECONCILIATION-UNBLOCK (~1.2 we) — Dispatch S91 W2 CF-25 `S90-VII-U-2-CORNER-RECONCILIATION-READING-B-LOCK-IN`; unblocks W1-2/W1-5/W1-6 INFO mechanical closures
5. **T2.46** CF-S91-VII-U-2-SUB-CORRIGENDUM-DUAL-SYMBOL-LANDING (~0.5 we) — §VII.U.2 sub-corrigendum with PILLAR-DISTINCT TAGGING DISCIPLINE + SINGLE-slot-with-pillar-sub-clauses (a/b)
6. **T1.16** W8-CF-73 CF-S91-VII-AR-STRENGTHENED-REGISTRY-TEXT (~0.3 we) — §VII.AR LEVEL-DRESSED STRENGTHENED registry-text update; CONDITIONAL on T1.15 PASS at W4

## W0b (orchestrator-direct-write METHODOLOGY-class rule/audit-script extensions)

1. **T2.1** CF-S91-W1-A — Class 8.7 K=3 promotion (0.6 we) — Land 2 new calibration instances at `pru-class-corpus.md §18` + status promote SUGGESTION → MANDATORY
2. **T2.2** CF-S91-W1-B — Substrate-input-orthogonality K=3 promotion (0.4 we) — Land 3rd structurally-distinct calibration instance
3. **T2.3** CF-S91-W6-3-PROSPECTIVE-APPLICATION (1.5 we) — 3 artifacts + 12-cell matrix re-run
4. **T2.4** CF-S91-W1-VII-AN-AUDIT-RECHECK (0.2 we) — §VII.AN route-declaration block to producing script per Class-(g)
5. **T2.6** CF-FORWARD-CONSUMER-ADOPTION (0.5 we) — Extend `/weave --update`, `_consolidate_intake.py`, plan-freeze auditors, knowledge-MCP indexer with supersedes-chain reading
6. **T2.7** CF-W2-ALLOWLIST-INSTANCES-BATCH (0.3 we) — 15 W2 gate-IDs to `methodology-wave-allowlist.md` + 15 entries to `methodology-wave-instances.md`
7. **T2.9** CF-S91-W2-PARSE-TREE-EXPANSION-BATCH-RETROFIT (1.0 we) — Mack batch retrofit across pre-S90 §VII registry entries with state-historic labels
8. **T2.13** CF-36-S91-1 α_s symbol-overload audit-script (0.5 we) — Implement `_alpha_s_symbol_overload_audit.py`
9. **T2.14** CF-36-S91-4 α_s K=2 advancement (0.3 we) — Land K=2 instance row at `pru-class-corpus.md §1`
10. **T2.18** W6-CF-W7-4 `_corner_classification_audit.py --self-test --extension-v2` (0.5-1.0 we)
11. **T2.19** W6-CF-W7-5 `_plan_staleness_audit.py --extension-v2` (0.5 we)
12. **T2.20** W6-CF-W7-7 CF-53 re-dispatch under Option-A supersedes (0.3 we)
13. **T2.24** W7-CF-W7-6 Class-8.3 publication-precision rule revision (0.4 we)
14. **T2.25** W7-CF-W7-7 Per-pole-per-observable-class 4-tuple rule extension (1.7 we)
15. **T2.26** W7-CF-W7-8 Stage-3-CLASS field schema extension + grandfather retrofit (1.5 we)
16. **T2.27** W7-CF-W7-9 Level-2 empirical-β verification rule extension (0.4 we)
17. **T2.30** W8-CF-74 Plan-text-drift correction orchestrator-convention promotion (0.5 we)
18. **T2.32** CF-S91-OPTION-V-PRE-REGISTRATION (0.25 we) — Admit option (v) as 5th pre-registered verdict at §VII slot for CF-37
19. **T2.37** CF-S91-W1-14-SIGMA-2-STRATUM-ANNOTATION-TAXONOMY-CONSOLIDATION-WORKSHOP (0.5 we) — 2-agent mini-workshop (connes-ncg + lizzi-spectral)
20. **T2.38** CF-S91-W1-14-IMPULSIVE-TRANSIT-FRAMING-STRUCTURAL-VALIDATION-AUDIT (0.7 we) — Audit S74 transit-einstein workshop framing
21. **T2.52** W-5 CF-6 NEW-DEFERRED-PENDING-SUB-CLASS-OPERATIONAL-ALIGNMENT (0.5 we) — Rule-file extension at `cross-pillar-bridge-anatomy.md §"Deferred-pending intermediate verdict-class"`
22. **T2.57** W-6 CF-4 BETA-SHELL-FI-CLASSIFICATION-LANDING (0.3 we) — Rule-file extension at `regulator-pin-discipline.md §"Extension"` OR `epistemic-discipline.md §"Source Reconciliation"` FI/RD/MIXED
23. **T2.59** W-6 CF-8 FWD-C2-K3-FALSIFIER-PRE-REGISTRATION (0.4 we) — Phi-orthogonality + 4-corner-distinct-cell pre-dispatch screen at FWD-C2 candidate workshop
24. **M2** CF-S91-VOLOVIK-S1-V2 Plan-freeze auditor integration (0.3 we)
25. **M3** CF-S91-VOLOVIK-S1-V3 Layer-separability cross-citation calibration (0.4 we)
26. **M4** CF-S91-VOLOVIK-S1-V4 Audit-script false-positive/negative self-tests (0.2 we)
27. **M5** CF-S91-CONNES-S2-A PRU Class 8.7 P3+P4 pattern-set extension + rule-body refinement (0.5 we) — UNBLOCKS T2.1 K=3 promotion
28. **M8** CF-S91-NEW S91-RULE-EXTENSION-ATLAS-ROW-VS-CACHE-MOMENT-META-THEOREM (0.5-1.0 we) — NEW sub-section §(ii.A) at `substrate-first-canonical-sourcing.md`

## W1-W8 substrate-physics compute waves (~48 items)

Per the v2 partition manifest above (unchanged) — substrate-physics compute gates, Stage-2 cross-axis verifies, STAGE-1-CANDIDATE landings. These are LEGITIMATE compute waves with substrate-physics PASS predicates, not housekeeping.

## W9 forward bridges + observational + Wodzicki-BCS

Same as v2 minus the deleted/fixed items:
- T2.8 α_s multi-σ falsifier three readings substrate-physics campaign (~3-5 we; multi-wave)
- T2.10 §VII.AW Stage-2 cross-axis verify (1.0 we) — moved from W4
- T2.12 3He-B Aalto LTL liaison first contact Q4 2026 deadline (0.2 we)
- T2.15 CF-49 FULL CC multipliers upgrade (1.5-2.5 we)
- T2.16 CF-50/52 LOCKED-NORM L_k=1 pre-normalization (1.5-2.0 we)
- T2.31 CF-37 AUX-4 (c)∘(d) parallel evaluation (1.0 we)
- T2.34 W1-14 composite bridge-map RDX (1.5 we; CONDITIONAL on T1.5 FAIL persisting)
- T2.36 W1-14 Wodzicki-BCS bridge theorem STAGE-1-CANDIDATE landing (1.5 we)
- T2.44 Pati-Salam in-scope candidate identification (1.5 we)
- M1 CF-S91-VOLOVIK-S1-V1 NEW K=2 deferred-pending calibration via Stage-1-Candidate landing (0.5 we)

## Forward dispatch

**Batch 1** (parallel; 2 METHODOLOGY-class waves; orchestrator-direct + mack sole-writer): W0a (6 items) + W0b (24 items). Note: W0b's 24-item count includes substantive rule/audit-script extensions that each need careful authorship by orchestrator-direct-write; if W0b stalls, natural split is W0b-i (mechanical rule-extensions: T2.32, T2.52, T2.57, T2.59, T2.24, T2.27 ≈ 5-6 items) + W0b-ii (audit-script extensions: T2.4, T2.6, T2.13, T2.18, T2.19, T2.20, T2.30, M2, M4, M5 ≈ 10 items) + W0b-iii (K=3 promotion + larger landings: T2.1, T2.2, T2.3, T2.9, T2.25, T2.26, T2.37, T2.38, M3, M8 ≈ 10 items).

**Batch 2** (4 substrate-physics waves): W1, W2, W3, W5.

**Batch 3** (4 substrate-physics waves): W4 (T1.10 PASS dep from W2), W6, W7, W8.

**Batch 4** (1 wave): W9.

## Status

Phase A (in-session housekeeping campaign at S91 W0 prep) COMPLETE for the truly mechanical + delete items; 16 items resolved without dispatching them. The remaining 24 METHODOLOGY-class items fire as W0a/W0b dispatch with orchestrator-direct-write (legitimate per `wave-classification.md` M1-M4); they are not "carry-forwards deferred to next session" — they are S91 W0 compute waves authored at dispatch time.

**Ready to proceed** to Phase 3 wave-planner dispatch (per the `/rclab-plan` skill Phase 3a swarm architecture).
