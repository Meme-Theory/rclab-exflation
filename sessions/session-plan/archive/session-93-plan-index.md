# Session 93 — Plan Index (fanout)

**Generated**: 2026-05-24 (`/rclab-plan --session 93`, Phase 3c)
**Source**: S92 carry-forward (9 WP CF sections + workshop campaign W-1..W-5+S-1 + 3 ad-hoc + mack landscape synthesis); dedup/re-scope per `session-93-context.md` filter log.
**Validation**: upstream-pin 9/9 PASS; PRDR/YAML 46/46 real gates PASS (`_yaml_gate_validator.py` clean after the S93 phantom-dedup fix).

| Wave | Theme | Owner | Gates | Plan file |
|:----:|:------|:------|:-----:|:----------|
| 0 | STAGE-3 sequencing pre-reg + slot-pre-allocation lockfile (**runs FIRST**) | gen-physicist | 1 | `session-93-plan-w0.md` |
| 1 | §VII.BA Wodzicki-BCS composite bridge map | connes-ncg-theorist | 3 | `session-93-plan-w1.md` |
| 2 | §VII.AU + CF-37 Fredholm-module + STAGE-3 | connes-ncg-theorist | 4 | `session-93-plan-w2.md` |
| 3 | §VII.AV anchor reconciliation + slot-split + Stage-2 | volovik-superfluid-universe-theorist | 7 | `session-93-plan-w3.md` |
| 4 | §VII.AX PBH cluster | mack-cosmic-bridge | 6 | `session-93-plan-w4.md` |
| 5 | §VII.AY R_machine + §VII.AR FULL-tier + §VII.AW | mack-cosmic-bridge | 6 | `session-93-plan-w5.md` |
| 6 | chirality / HH^1 / Pati-Salam Stage-2 | connes-ncg-theorist | 4 | `session-93-plan-w6.md` |
| 7 | α_s transport-degree + SCHEMATIC-vs-FULL + d_s | connes-ncg-theorist | 3 | `session-93-plan-w7.md` |
| 8 | LQG narrow-path cluster | phonon-first-cosmologist | 7 | `session-93-plan-w8.md` |
| 9 | methodology / audit-scripts / cross-cutting | gen-physicist | 5 | `session-93-plan-w9.md` |

**Total**: 10 waves (W0 setup + W1-W9 compute), 46 dispatchable gates (W8 also carries a §VI Workshop-1 pre-reg YAML block, the W8-5 deliverable). Wave 0 (gate W0-1, the relocated sequencing/lockfile pre-registration) runs FIRST.

Each per-wave plan is independently dispatchable: `/rclab-coordinate session-93-plan-w{i}.md`. Full session: `/rclab-coordinate session-93-plan-index.md`.

## Cross-cutting execution constraints (mack-synthesis §V.1/§V.2)

1. **Dependency-tier ordering** — gates carry Tier tags. Dispatch order respects: Tier-1 anchor-supplying (W3-1 §VII.AV slot-split; W5-1 R_machine CF-A; W1-2 §VII.BA Stage-1) → Tier-2 value-pinning (W2-1 Fredholm-index; W3-2/W3-3 PV+8.7; W4-1 E2; W4-3 n_PBH) → Tier-3 Stage-2/STAGE-3 flips (W2-2, W3-6, W4-2/4-4/4-5, W5-2, W5-5, W6-3/6-4). Per-gate `Depends on` + per-wave Decision Points encode the chain; unmet prereqs → honest mechanical closure per `mechanical-closure-discipline.md`.
2. **STAGE-3 slot-pre-allocation lockfile** — **Wave 0** gate W0-1 (`session-93-plan-w0.md`) creates `sessions/framework/s93-slot-pre-allocation-lockfile.md` reserving §VII.AU / AW / AY / AV / AX / BB / BE for the 7 colliding STAGE-3-PERMANENT registry-write flips (avoids parallel-writer collision). The STAGE-3 gates (W2-2, W5-2, W5-5, W4-4, W6-3, W6-4) depend on this lockfile; W0-1 runs FIRST (Wave 0, before any compute wave), so the flips never serialize on a missing lockfile.
3. **Anti-inflation K-counter cross-check** (mack §V.2) — the five corpus DIRECTIVEs §18-§23 advance toward K=3 MANDATORY only on structurally-distinct Hybrid-Independence-Test instances; no two double-count. Wave 0 gate W0-1 lands the cross-check wrapper.

## Plan-freeze orchestrator actions (allowlist appends — orchestrator-only edit per recursion-attack closure)

METHODOLOGY-class gate-IDs flagged by planners for append to `sessions/framework/registry/methodology-wave-allowlist-ledger.md` at dispatch time (with `sha256_of_plan_block`): W0-1, W1-2, W2-2, W2-3, W2-4, W3-7, W5-5, W5-6, W5-3(E5-annotation), W6-2, W9-1, W9-2, W9-3, W9-4. Each carries the parallel rationale entry in `methodology-wave-instances.md` per Edit-discipline item 4.
