# Session 94 — Plan Index (fanout)

**Generated**: 2026-05-25 (`/rclab-plan --session 94 --extra include "session-x" with session-93 carry-forward grabbing`, Phase 3).
**Source**: DUAL-SOURCE carry-forward grab — session-93 (10-wave compute; per-wave WP `Carry-Forward Computations (MATH ONLY)` + `session-93-housekeeping.md §B/§D`) ∪ session-x (9-wave aggregate-expansion; W9 consolidated CFs). Dedup/scope log: `sessions/session-plan/session-94-context.md §0–§2`.
**Validation**: upstream-pin 8/8 PASS (W1 fixed in-session — 2 mis-slugged npz refs corrected per SOURCE-RECON Class-(c)); R3/YAML 25/25 gates PASS (`_yaml_gate_validator.py` FAIL=0 across all waves).

| Wave | Theme | Owner | Gates | Lines | Plan file |
|:----:|:------|:------|:-----:|:-----:|:----------|
| 1 | §VII.BA composite-bridge + α_s transport + A_s normalization | connes-ncg-theorist | 5 | 1080 | `session-94-plan-w1.md` |
| 2 | §VII.AU winding / 3He-B BDI Level-3 / α=−3 Layer-1 | connes-ncg-theorist | 3 | 799 | `session-94-plan-w2.md` |
| 3 | Pati-Salam SU(4)_PS Level-3 + module-as-canonical K3 + §VII.AZ | connes-ncg-theorist | 3 | 728 | `session-94-plan-w3.md` |
| 4 | Stage-2 joint-theorem cross-axis promotions | gen-physicist | 2 | 600 | `session-94-plan-w4.md` |
| 5 | PBH truncation/band-breach + BAO-peak observational | mack-cosmic-bridge | 3 | 725 | `session-94-plan-w5.md` |
| 6 | methodology / K-counter / audit-script / a_n-retrofit | gen-physicist | 5 | 1139 | `session-94-plan-w6.md` |
| 7 | spectral-dim v_g^B2 discriminator + LQG narrow-path cocycle | phonon-first-cosmologist | 2 | 535 | `session-94-plan-w7.md` |
| 8 | §VII.AV Stage-2 re-verify + §VII.AR PASS-A substrate-derivation | volovik-superfluid-universe-theorist | 2 | 668 | `session-94-plan-w8.md` |

**Total**: 8 waves, 25 dispatchable gates, ≈16.9 wave-equivalents.

Each per-wave plan is independently dispatchable: `/rclab-coordinate session-94-plan-w{i}.md`. Full session: `/rclab-coordinate session-94-plan-index.md`.

## Gate manifest (per wave)

- **W1**: `S94-VII-BA-STAGE-2-CROSS-AXIS-VERIFY`, `S94-VII-BA-T4-ENVELOPE-EXTENSION`, `S94-VII-Bx-T5-ALPHA-S-A4-RECOVERY`, `S94-K-CSUB-R-ABSOLUTE-CONVERGENCE`, `S94-A_S-MPL-CONVERGENCE`
- **W2**: `S94-VII-AU-WINDING-RECONCILIATION`, `S94-VII-AU-3HEB-BDI-LEVEL-3-ANCHOR` (dep on WINDING-RECONCILIATION), `S94-VII-AU-ALPHA-MINUS-3-LAYER-1`
- **W3**: `S94-VII-PS-FULL-SPECTRUM-LEVEL-3` (HEAVY ~4.0w; sparse-Lanczos OR Friedrich-Bär route — dense @ L_max=12 = 1094.7 GB INFEASIBLE), `S94-MODULE-AS-CANONICAL-K3`, `S94-VII-AZ-BAND-ADMISSIBLE-RE-EXTRACTION`
- **W4**: `S94-VII-AX-STATE-PROJ-STAGE-2-CROSS-AXIS-VERIFY`, `S94-LQG-CDT-STAGE-2`
- **W5**: `S94-N-PBH-TRUNCATION-ANCHOR`, `S94-N-PBH-BAND-BREACH-PROJECTION` (predicted L_breach=19), `S94-BAO-PEAK-BRANCH`
- **W6**: `S94-CPB-AUDIT-PENDING-VS-DEFECTIVE`, `S94-MULT-NORM-CANCELLATION-K3`, `S94-S16-AREA-FUNCTIONAL-K-ADVANCE`, `S94-NON-PROMOTION-META-TAXONOMY`, `S94-A_N-RETROFIT-C-CAUSALITY`
- **W7**: `S94-DS-GAMMA-E-RESOLUTION` (executors kk + landau), `S94-NARROW-PATH-WORKSHOP-6-COCYCLE`
- **W8**: `S94-VII-AV-OP-PROJ-STAGE-2-AXIS-A-REVERIFY`, `S94-VII-AR-PASS-A-SUBSTRATE-DERIVATION`

## Cross-cutting execution constraints

1. **Stage-2 cross-axis gates** — `S94-VII-BA-STAGE-2-CROSS-AXIS-VERIFY` (W1), `S94-VII-AX-STATE-PROJ-STAGE-2-CROSS-AXIS-VERIFY` + `S94-LQG-CDT-STAGE-2` (W4), `S94-VII-AV-OP-PROJ-STAGE-2-AXIS-A-REVERIFY` (W8) each dispatch TWO axis-distinct cross-reviewers without prior workshop context, neither an original author (downstream-inheritance-reach test), JOINT clauses PASS-AND'd + substrate-input-orthogonality, per `joint-theorem-promotion.md §"Stage-2 Axis-B Selection Protocol"`. Reviewer assignments are pinned in each gate block.
2. **Internal dependency** — W2: `S94-VII-AU-3HEB-BDI-LEVEL-3-ANCHOR` depends on `S94-VII-AU-WINDING-RECONCILIATION` (the winding pairing must be identified first); honest mechanical closure per `mechanical-closure-discipline.md` if WINDING-RECONCILIATION FAILs.
3. **Feasibility wall** — W3 `S94-VII-PS-FULL-SPECTRUM-LEVEL-3` is dense-infeasible (1094.7 GB); the gate pins Route-A sparse-Lanczos block-by-block (`torch.linalg.eigvalsh`, <0.5×VRAM per block) with Route-B Friedrich-Bär analytic-saturation fallthrough; verdict scheme tags the route taken.
4. **session-x gate-ID re-namespacing** — session-x `SX-NEXT-*` CFs are re-namespaced `S94-*` (provenance CF-ID retained in-block). Verified collision-free against `computations/session-93/s93_gate_verdicts.txt` + `computations/session-x/sx_gate_verdicts.txt`.

## Plan-freeze orchestrator actions (effect at `/rclab-coordinate` dispatch time — orchestrator-only edits)

### (a) METHODOLOGY-class allowlist appends (`methodology-wave-allowlist-ledger.md`, orchestrator-only per recursion-attack closure; 3-col row + `methodology-wave-instances.md` rationale, with `sha256_of_plan_block`)

- W6 (all 5, METHODOLOGY-class M1∧M2∧M3∧M4 verified by the planner): `S94-CPB-AUDIT-PENDING-VS-DEFECTIVE`, `S94-MULT-NORM-CANCELLATION-K3`, `S94-S16-AREA-FUNCTIONAL-K-ADVANCE`, `S94-NON-PROMOTION-META-TAXONOMY`, `S94-A_N-RETROFIT-C-CAUSALITY`.
- W3 (conditional): `S94-MODULE-AS-CANONICAL-K3` — flag for append IFF it lands a corpus §19 row (else COMPUTE-class).
- W4 gates are COMPUTE-class (they dispatch reviewer agents + aggregation scripts; M2 fails for METHODOLOGY) — NO allowlist append.

### (b) canonical_constants.py promotions-before-use (W7 `S94-NARROW-PATH-WORKSHOP-6-COCYCLE` prerequisites)

`W_BG` (= cosh(2r) = 1462.30), `R_BG`, `s_CS`, `N_e` are cited non-canonically in W7; promote each to `canonical_constants.py` (with PROVENANCE) BEFORE the gate executes, per `math-scripts.md` canonical-constants discipline.

### (c) audit-script scope extension (W6 `S94-A_N-RETROFIT-C-CAUSALITY` prerequisite)

`_a_n_regulator_pin_audit.py` currently scans only `*.py` under `computations/`; extend its scan scope to the target `.md` doc (`sessions/framework/Phononic-C-Causality.md`) so the gate's `--new-only == 0` PASS criterion is verifiable. 193-citation retrofit scope (115 `a_2` + 58 `a_0` + 20 `a_4`; 11 already `a_2^{ζ}`-tagged) pinned in the W6 plan.

## Next step

`/rclab-coordinate sessions/session-plan/session-94-plan-index.md` (full session) or per-wave. Working-paper shells (`sessions/archive/session-94/session-94-w{i}-workingpaper.md`) are generated by `/rclab-plan` Phase 4 (this run).
