# Session 112 — Plan Index (fanout)

**Built by** `/rclab-plan --session 112 --extra "include a workshop-schedule to dive into EVOI items again (similar to session 110)"` (2026-06-22).
**Source**: `session-112-context.md` (8 S111 carry-forwards + register consumption) + `session-112-partition.md`. **Mode**: fanout (per-wave plan + per-wave WP).
**Verdict file**: `computations/session-112/s112_gate_verdicts.txt`.

## Compute waves

| Wave | Theme | Owner / planner | Gates | Plan file | 3a upstream-pin | 3a YAML |
|:--|:--|:--|:--|:--|:--|:--|
| W1 | M_KK keystone + H0 closure (Tier-1, highest leverage) | volovik-superfluid-universe-theorist | 2 | `session-112-plan-w1.md` | PASS | PASS (2/2) |
| W2 | Stage-2 cross-axis verify cohort (§VII.CG/CH/CI/CJ) | gen-physicist | 4 | `session-112-plan-w2.md` | PASS | PASS (4/4) |
| W3 | compact-object + Floquet precision (Tier-3, non-blocking) | gen-physicist | 2 | `session-112-plan-w3.md` | PASS | PASS (2/2) |

**Total: 8 gates, 3 waves. Validation: 6/6 PASS (3 upstream-pin + 3 YAML).**

### Gate roster
- **W1**: CF-S112-MKK-SUBSTRATE-ANCHOR (volovik) · CF-S112-H0-BAND-CLOSURE (mack; ⇐ upstream W1-1)
- **W2**: CF-S112-CLOCKLOC3-STAGE2 (§VII.CG) · CF-S112-NOHOLOFLUX-STAGE2 (§VII.CH) · CF-S112-M1-INTERTWINER-STAGE2 (§VII.CI) · CF-S112-VIICJ-STAGE2 (§VII.CJ) — each 2 NON-AUTHOR cross-reviewers, PASS-AND
- **W3**: CF-S112-B5A-BRACKETED (hawking) · CF-S112-FLOQUET3-HPAR-TIGHTEN (transit-dynamics)

### Wave dependency graph
```
W1-1 (MKK-SUBSTRATE-ANCHOR) ──► W1-2 (H0-BAND-CLOSURE)   [intra-wave; H0 conditional on M_KK]
W2 (4 Stage-2 verifies) ── independent, parallel ── no cross-wave dependency
W3 (B5A, FLOQUET3) ── independent, terminal Tier-3 ── no downstream consumer
```
W2 and W3 may run in parallel with W1; only W1-2 waits on W1-1.

## Workshop track (`--extra`, separate stream)

`sessions/session-112/session-112-workshop-schedule.md` — 7 EVOI-frontier workshops (KPIVOT · TAUFOLD · CCRESID · DMMASS · AS-HTILDE · OBSAXIS · YUKSHAPE) on the high-leverage standing gaps with no tractable compute gate. Routes via `/rclab-review`/`/rclab-workshop`, NOT this compute index.

## Next step
`/rclab-coordinate sessions/session-plan/session-112-plan-index.md` (compute waves) · then `/rclab-review` or `/rclab-workshop` per the workshop schedule.
