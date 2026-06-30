# Session 93 — Results Working-Paper Index (fanout)

**Generated**: 2026-05-24 (Phase 4 close; `/rclab-plan --session 93`)
**Mode**: fanout — per-wave plan + per-wave WP shell (S87 W1b lesson)
**Plan index**: `sessions/session-plan/session-93-plan-index.md`
**Context file**: `sessions/session-plan/session-93-context.md` (46 live CF gates post-dedup across 9 waves)
**Partition manifest**: `sessions/session-plan/session-93-partition.md`

## Per-wave dispatch index

| Wave | Theme | Owner subagent_type | Gates | Plan file | WP shell |
|:----:|:------|:--------------------|:-----:|:----------|:---------|
| W0 | STAGE-3 sequencing pre-reg + slot-pre-allocation lockfile (**runs FIRST**) | gen-physicist | 1 | `session-plan/session-93-plan-w0.md` | `session-93-w0-workingpaper.md` |
| W1 | §VII.BA Wodzicki-BCS composite bridge map | connes-ncg-theorist | 3 | `session-plan/session-93-plan-w1.md` | `session-93-w1-workingpaper.md` |
| W2 | §VII.AU + CF-37 Fredholm-module + STAGE-3 | connes-ncg-theorist | 4 | `session-plan/session-93-plan-w2.md` | `session-93-w2-workingpaper.md` |
| W3 | §VII.AV anchor reconciliation + slot-split + Stage-2 | volovik-superfluid-universe-theorist | 7 | `session-plan/session-93-plan-w3.md` | `session-93-w3-workingpaper.md` |
| W4 | §VII.AX PBH cluster | mack-cosmic-bridge | 6 | `session-plan/session-93-plan-w4.md` | `session-93-w4-workingpaper.md` |
| W5 | §VII.AY R_machine + §VII.AR FULL-tier + §VII.AW | mack-cosmic-bridge | 6 | `session-plan/session-93-plan-w5.md` | `session-93-w5-workingpaper.md` |
| W6 | chirality / HH^1 / Pati-Salam Stage-2 | connes-ncg-theorist | 4 | `session-plan/session-93-plan-w6.md` | `session-93-w6-workingpaper.md` |
| W7 | α_s transport-degree + SCHEMATIC-vs-FULL + d_s | connes-ncg-theorist | 3 | `session-plan/session-93-plan-w7.md` | `session-93-w7-workingpaper.md` |
| W8 | LQG narrow-path cluster | phonon-first-cosmologist | 7 | `session-plan/session-93-plan-w8.md` | `session-93-w8-workingpaper.md` |
| W9 | methodology / audit-scripts / cross-cutting | gen-physicist | 5 | `session-plan/session-93-plan-w9.md` | `session-93-w9-workingpaper.md` |

**Totals**: 10 waves (W0 setup, runs FIRST + W1-W9 compute); 46 standalone gates (W8 also carries the §VI Workshop-1 pre-reg YAML block as the W8-5 deliverable).

## Phase 3a validation status (final)

| Validator | Result |
|:----------|:-------|
| `_plan_upstream_pin_validator.py` | 10/10 PASS (exit 0; all upstream `.npz` resolve or runtime-marked; W0 added + W9 re-validated post-relocation) |
| `_yaml_gate_validator.py` (PRDR/R3) | 46/46 real gates PASS (`yaml_FAIL=0`); phantom markdown-header double-count fixed in-session (S93 dedup) |

**WP shells**: 10/10 on disk; gate-section counts match (W0:1 / W1-W9: 3/4/7/6/6/4/3/7/5); zero banned `Runtime agent fills` stubs; every gate carries the MCP Pre-Compute Audit block + the 4-section footer.

## Cross-cutting execution constraints (carried from plan-index)

1. Dependency-tier ordering (Tier-1 anchor → Tier-2 value-pin → Tier-3 Stage-2/STAGE-3 flips); per-gate `Depends on` + per-wave Decision Points.
2. Wave 0 gate W0-1 creates `sessions/framework/s93-slot-pre-allocation-lockfile.md` reserving the 7 STAGE-3 slots (§VII.AU/AW/AY/AV/AX/BB/BE); the STAGE-3-flip gates depend on it — Wave 0 runs FIRST (before any compute wave).
3. Anti-inflation K-counter cross-check (corpus §18-§23 advance only on structurally-distinct Hybrid-Independence-Test instances).
4. Plan-freeze allowlist appends (orchestrator-only edit) for the METHODOLOGY-class gate-IDs flagged in the plan-index.

## Next step

`/rclab-coordinate sessions/session-plan/session-93-plan-index.md` (full session) OR `/rclab-coordinate sessions/session-plan/session-93-plan-w{i}.md` (selective wave dispatch).

---

**End of S93 results working-paper index v1.** All 9 wave plans + 9 WP shells + plan-index + 9 validation JSONs on disk; validation clean; ready for `/rclab-coordinate`.
