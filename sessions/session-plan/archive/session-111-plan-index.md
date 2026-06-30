# Session-111 — Plan Index (fanout, COMPUTE)

**Session:** 111.  **Prior:** 110.  **Date:** 2026-06-21.  **Theme:** harvest the S110 M_KK-keystone session. The a(t)/effective-Friedmann FORM is now MONOTONE-robust (S110 WS-ATFORM) ⇒ the §6.3 residual = {M_KK magnitude (W2 MKK-RG decider) + the clock-triple well-posedness (W1)}.
**Scope:** S110 per-wave WP `## Carry-Forward Computations` (`session-110-w{2,3,4}-workingpaper.md`) + the 8 W1 workshop Wrap-Ups + the housekeeping mirror. 22 deduplicated carry-forwards → 23 gate blocks (AS3 split AS3a/AS3b).
**Context:** `session-111-context.md`.  **Partition:** `session-111-partition.md`.
**Verdict file (compute gates):** `computations/session-111/s111_gate_verdicts.txt` (created at `/rclab-coordinate`).

## Waves

| Wave | Theme | Type | Gates | Plan file | 3a upstream-pin | 3a YAML/PRDR |
|:--|:--|:--|:--|:--|:--|:--|
| **W1** | a(t) / clock theorems — the Tier-1 #1 effective-Friedmann spine (clock-triple leg of the §6.3 residual) | COMPUTE (+2 Stage-1 registrations) | 6 | `session-111-plan-w1.md` | PASS | 6/6 PASS |
| **W2** | M_KK keystone + H-sector + CC — the M_KK-DERIVATION τ-RG-invariance decider (PRIME Topic-1) | COMPUTE | 5 | `session-111-plan-w2.md` | PASS | 5/5 PASS |
| **W3** | fermion-mass / Yukawa / NCG-categorical — full-flavor Yukawa + C²-coset Weinberg + M1 intertwiner | COMPUTE | 4 | `session-111-plan-w3.md` | PASS | 4/4 PASS |
| **W4** | compact-object / black-hole — white-hole island, 12D GL bubble, LRD-T transport | COMPUTE | 3 | `session-111-plan-w4.md` | PASS | 3/3 PASS |
| **W5** | Floquet confirmatory + Stage-2 verify (§VII.CF κ-sign-lock∧Wodzicki-parity) | COMPUTE (+1 Stage-1, +1 Stage-2) | 5 | `session-111-plan-w5.md` | PASS | 5/5 PASS |

**Totals:** 23 compute gate blocks (W1–W5), all validators PASS. Working papers: `session-111-w{1..5}-workingpaper.md`. (3a upstream-pin validator was extended this plan-freeze to parse R3-YAML structured `path:` pins — it previously no-op'd on R3 gate blocks; now 21/23 gates actively cross-check their upstream npz, all present, no drift; 2 registration gates correctly NO-UPSTREAM.)

## Run order (`/rclab-coordinate`)

1. **Tier-1 spine first** — **W1** (a(t)/clock) + **W2** (M_KK keystone) are the highest-EVOI waves; parallelizable. The a(t)/Friedmann residual = {W2 M_KK magnitude + W1 clock-triple}.
2. **Intra-wave** — sequence **CLOCKLOC2 → CLOCKLOC1** in W1 (the monotone corridor scopes the (C,E,D)-triple domain).
3. **W3 → W4 → W5** — the fermion-mass, compact-object, and Floquet/Stage-2 cohorts (EVOI MED/structural; no hard cross-wave data dependency).

## Run-order + dependency flags (applied at gate-block authoring)

- **Upstream-landed (ready):** MKK-RG-INVARIANCE gated on `S110-CF-CV2A` (`s110_cf_cv2a_mkk_transmut_promote.npz`, on disk); KSIGN-PARITY-STAGE2 gated on the §VII.CF Stage-1 entry (landed S110). Both ready.
- **Independent axes:** CF3-H0-RESIDUAL ∥ MKK-RG-INVARIANCE (volovik a₀-orthogonality audit) — no sequencing.
- **Stage-2 reviewer exclusion:** KSIGN-PARITY-STAGE2 reviewers MUST NOT be connes/mack (the §VII.CF authors); axis-A lizzi / axis-B volovik, parallel, without the connes-mack workshop file.
- **Sharpenings folded:** CO34B-LRDT (pin deg=+1, κ-sign predicate, `convention=…-DA-1-PARITY-odd`) + CF3-H0-RESIDUAL (49/800 honest partial, dimensionless-slot) carry the connes-mack workshop sharpenings; CLOCKLOC1 PRDR carries the V_spec-monotone + Level-2-clock tags.

## Separate stream — NOT part of this compute plan

S111 also carries a **workshop schedule** (`sessions/session-110/session-110-s111-workshop-schedule.md`), run via `/rclab-coordinate` workshop-mode. `/rclab-plan` does not author it (per `Investigating-Workshops.md §"Cross-references"`); its outcomes feed back as future-session carry-forwards.

## Forward-register maintenance (1c-REGISTERS, done at this plan-freeze)

EVOI re-stamped S110→S111 (staleness audit PASS, lag 0; §6 queue refreshed with the 22 CFs, S110 W2–W4 results folded); atlas-08 S110 compute-wave freshness bullet added; atlas-04 verified-current (S110 in-session A15); open-channel-ledger current (A39). CONSUME confirmed no additional tractable register candidate beyond the 22 CFs; standing gaps (C2 K_pivot, 170× DM mass-anchor, τ_fold, DESI-lensing/branch-iv) recorded as leverage-high-but-gate-less. Register-semantics HOLD: HK-SA-RETAG (atlas-04 S3 retag) pending an S111 Q2 adjudication.

## Next step
`/rclab-coordinate sessions/session-plan/session-111-plan-index.md`
