# Session 118 — Plan Index (fanout)

**Date**: 2026-06-29
**Built by**: `/rclab-plan --session 118` (fanout).
**Scope**: `sessions/session-plan/session-118-context.md` · **Partition**: `sessions/session-plan/session-118-partition.md`
**Dispatch**: `/rclab-coordinate sessions/session-plan/session-118-plan-index.md`

S117 closed lean (most waves "No carry-forwards"); S118 is a small, well-scoped session — **8 compute gates / 4 waves**. Phase 1c-REGISTERS.CONSUME added NO register candidate beyond the WP carry-forwards (every high-leverage register item is a standing gap; see context §"CONSUME"). EVOI-ordered: hygiene first (W0); the Q23 A_s rate-limiter is the highest-EVOI content (W1).

| Wave | Theme | Owner / planner | Gates | Plan file | Validation |
|:----:|:------|:----------------|:-----:|:----------|:----------:|
| 0 | Registry-hygiene (mack-surface patches) | mack-cosmic-bridge | 3 | `session-118-plan-w0.md` (623 ln) | pin PASS · YAML 3/3 |
| 1 | A_s amplitude closure | transit-dynamics-theorist | 2 | `session-118-plan-w1.md` (589 ln) | pin PASS · YAML 2/2 |
| 2 | Lepton-PMNS joint admissibility | neutrino-detection-specialist | 1 | `session-118-plan-w2.md` (347 ln) | pin PASS · YAML 1/1 |
| 3 | Spectral-functional + WDW residuals | gen-physicist (planner); lizzi + feynman (executors) | 2 | `session-118-plan-w3.md` (590 ln) | pin PASS · YAML 2/2 |

**Gates (8):**
- **W0** — `CF-S118-HK-ALPHAS-LABEL-CONSISTENCY` · `CF-S118-HK-VIICK-D4-SCOPE-TOKEN` · `CF-S118-HK-ROW79-DISCHARGE` (all mack-cosmic-bridge; artifact-existence registry-hygiene patches).
- **W1** — `CF-S118-AS-CS-SUBSTRATE-FIRST` (transit, PRIMARY [SIGN]; FAIL→`CF-S118-AS-PREFACTOR-SOURCE`) · `CF-S118-ALT-GREYBODY-WALL` (volovik).
- **W2** — `CF-S118-PMNS-JOINT-ADMISSIBILITY` (neutrino; 3-track non-empty/empty/narrow).
- **W3** — `CF-S118-LEMP-OQ4-VACUUM-FERMI-PIN` (lizzi, [SIGN]) · `CF-S118-WDW-S0-ONGRID` (feynman; OPTIONAL/EVOI-last/cosmetic, droppable under capacity).

**Verdict file**: `computations/session-118/s118_gate_verdicts.txt` (canonical; per `.claude/rules/gate-verdicts.md`).
**Working papers**: `sessions/session-118/session-118-w{0..3}-workingpaper.md` (per-wave; index `session-118-results-index.md`).

**Plan-freeze validation (Phase 3a)**: all 4 waves — upstream-pin validator exit 0 (every cited `.npz` on disk, pins agree); `_yaml_gate_validator.py` 8/8 gates PASS (0 FAIL, 0 phantom-markdown, cutoff_axis N/A for all — no L_max-stability gate this session).

**Standing gaps** (recorded; NOT wave gates — leverage ≠ tractability): M_KK-DERIVATION · atlas-04 C2 K_pivot · residual-3% CC + BBN-arm Q29 · τ_fold=0.190 moduli selection · Born-rule L²-weight · 170× DM-mass anchor (kinematic survival discharged S117) · branch-iv w₀(L) DR3 + DESI-WZ-LENSING-BIAS · K8 §VII.AF.1.STATE-PROJ · `CF-S94-W5-3-FWDC1-ASYMPTOTIC` · `CF-S117-STATEPROJ-SC-FROM-SUBSTRATE`. See `session-118-context.md §"CONSUME"`.

**Register maintenance (1c-REGISTERS.MAINTAIN, effected at this plan-freeze)**: EVOI currency S117→S118 + §6 S118 stamp + §5 S117 row + §EVOI.BF A_s/L_emp-cohort fold + 170× gap RESOLVED-on-kinematics (staleness audit PASS lag=0); atlas-08 S117 freshness fold + header S114→S117 + `atlas-08-freshness-S117.md`; atlas-04 no-change; open-channel-ledger §E cells.
