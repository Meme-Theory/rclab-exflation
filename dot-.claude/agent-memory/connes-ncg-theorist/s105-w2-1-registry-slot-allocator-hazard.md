---
name: s105-w2-1-registry-slot-allocator-hazard
description: Registry §VII next-free-slot allocator MUST exclude out-of-sequence NAMED slots (§VII.PROP, §VII.AAU) — naive bijective-base-26 max mis-allocates. Plus the S105 W2-1 BDI-Horizon-Faithfulness §VII.BZ Stage-1 landing.
metadata:
  type: project
---

# S105 W2-1 — BDI Horizon-Faithfulness Stage-1 landing + the registry slot-allocator hazard

## The landing (gate `S105-W2-1-BDI-HORIZON-FAITHFULNESS-STAGE1`)
- Registered the S104 S2-1 (connes×volovik) workshop-FROZEN **BDI Horizon-Faithfulness Protection** candidate as **STAGE-1-CANDIDATE** at **§VII.BZ** (registration of frozen Stage-0 text, NOT re-derivation).
- Theorem: on the emergent horizon crossed product `A_hor = A_K ⋊_{σ^ω} ℝ`, the GGE relic modular weight `ω|_{A_hor}` is FAITHFUL, protected by the 3He-B (BDI, N₃=0) universality class — the 3He-A Weyl zero `E_n=−n·ω_0` does NOT inherit through `χ:A_K→M₂(ℂ)`; the inherited CdGM ladder `E_n=−(n+1/2)·ω_0` is gapped at +1/2; the +1/2 minigap = bosonic Wightman floor `W_GGE=n_k+1/2`, so ONE BDI datum fixes BOTH the Type-II semifinite trace AND faithfulness (EMERGENCE-1).
- Clause attribution (frozen, VERBATIM transcription, workshop lines 573-576): (a) volovik-axis [BDI/N₃=0 + CdGM-vs-Weyl + χ inheritance + P_exc=1.000]; (b) connes-axis [Type-II trace + Tomita-Takesaki modular operator]; (c) JOINT [+1/2 identification] = the **Stage-2 PASS-AND target**.
- **Stage-2 promotion gate** (per the workshop, NOT this session): `S105-OMEGA-FAITHFUL-NORMAL` per-block PASS + a future two-agent cross-axis verify on JOINT clause (c). Stage-0 authors connes/volovik + successors EXCLUDED from Stage-2.
- Verdict = **FAIL-with-remediation** (registry-write-HYGIENE outcome, NOT physics) — landed+verified but plan-pinned slot drifted. audit_sha256 `dc4221eeca101e02…`.

## The slot-allocator hazard (REUSABLE — applies to EVERY registry-landing gate)
**Trap**: a naive next-free-§VII-letter allocator that matches `^#+ §VII\.([A-Z]+)` and takes the bijective-base-26 MAX is WRONG. The registry carries OUT-OF-SEQUENCE NAMED slots whose post-`§VII.` identifier is a WORD, not a letter run:
- `§VII.PROP` (registry line ~16231; S87 W1a-7 "Routing-Layer Two-Principle Landing") → base-26 value 11244
- `§VII.AAU.OP-PROJ` (line ~18063; S89 W7c FWD-C1) → base-26 value 723
Both dominate the real sequence frontier (BY=77), so the naive allocator mis-allocates `§VII.PROQ`. I hit this live in S105 W2-1: first run wrote §VII.PROQ, I had to remove it and restore the registry to §VII.BY, patch the allocator, re-run → correct §VII.BZ.

**FIX**: the framework's monotone slot SEQUENCE is letter-runs of LENGTH ≤ 2 ONLY (single A..Z, then two-letter AA..AZ, BA..BY). Restrict the frontier-max computation to `len(letters) ≤ 2`; exclude named slots (>2 chars). Keep named slots in the raw set ONLY for the genuinely-absent defensive check on the chosen successor. Canonical impl: `find_next_free_slot()` in `computations/session-105/s105_w2_1_bdi_horizon_faithfulness_stage1_landing.py`.

**Frontier as of 2026-06-11**: documented §VII sequence frontier = §VII.BY (S103 W1-5); §VII.BZ now occupied (this landing). Next sequence letter after BZ is CA (NOT "PROQ"-style). Named slots live OUTSIDE the sequence and are never the frontier.

## Slot-drift FAIL convention (cross-ref)
Per plan §W2-1 + `epistemic-discipline.md §"Registry-Write Hygiene under Parallel-Writer Race"` item 3: when the PLAN-pinned slot is occupied at runtime, reroute to next-free AND emit **FAIL-with-remediation** (not PASS) so the drift is auditable. The entry still lands+verifies; the FAIL is bookkeeping. Precedent: §VII.BK (S97 W5-1, plan §VII.BH occupied → §VII.BK). NB: §VII.AZ.OP-PROJ (S91 W8-3) emitted PASS with `slot_rerouting_triggered=True` — that was a SIBLING-reservation reroute, not a stale-plan-pin collision; the plan's explicit FAIL_meaning governs.
