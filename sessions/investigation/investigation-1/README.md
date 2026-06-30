# Investigation 1 — Wholesale Open-Ended Survey at the S108/S109 Plateau

**Opened:** 2026-06-14
**Charge author:** orchestrator (dispatch only — no per-agent angle injected, per `feedback_review-dispatch-no-orchestrator-angle.md`)
**Mode:** exploratory survey. NOT a compute gate, NOT a workshop. No pre-registered thresholds, no PASS/FAIL.

## The conceit

Session ~108 is a plateau. What was once a tsunami of activity has ebbed into a (hopefully) solid
framework — but **solid and exhaustive are not the same**. The whole conceit of this project is a
willingness to explore other known findings and use them as springboards, or "through the mirror
darkly" iterations of known physics mysteries that are just waiting for a concrete substrate to fill
cement.

## What each agent was asked to determine (identical charge to all)

1. **Biggest gaps** — where the framework is silent, hand-wavy, or has a hole a load-bearing claim depends on.
2. **Critical contradictions** — internal tensions; two results that can't both be right as stated; prose outrunning register status; stale claims.
3. **Unsupported load-bearing assumptions** — things leaned on hard but not earned (post-hoc stipulations, conventions treated as derivations, "by construction" hiding a choice).
4. **Areas needing refinement** — real but coarse, OOM-only, schematic-not-physical, or mis-precision-pinned.
5. **Untraveled bridges (most important)** — known physics findings / open mysteries in the agent's own domain the framework has NOT engaged, which could become springboards to bridge items 1–4.

## Roster (31 research agents → one file each)

**Batch 1 — NCG / spectral / geometry core**
`connes-ncg-theorist` · `lizzi-spectral-functional-theorist` · `spectral-geometer` · `van-den-dungen-bridge-theorist` · `baptista-spacetime-analyst` · `kaluza-klein-theorist` · `berry-geometric-phase-theorist` · `gen-physicist`

**Batch 2 — condensed-matter / superfluid / transit**
`volovik-superfluid-universe-theorist` · `landau-condensed-matter-theorist` · `transit-dynamics-theorist` · `quantum-acoustics-theorist` · `phonon-first-cosmologist` · `kitaev-quantum-chaos-theorist` · `tesla-resonance` · `paasch-mass-quantization-analyst`

**Batch 3 — gravity / cosmology / high-energy**
`einstein-theorist` · `hawking-theorist` · `schwarzschild-penrose-geometer` · `loop-quantum-gravity-theorist` · `string-theory-theorist` · `quantum-foam-theorist` · `kaku-speculative-theorist` · `feynman-theorist`

**Batch 4 — observational / particle / empirical**
`mack-cosmic-bridge` · `cosmic-web-theorist` · `little-red-dots-jwst-analyst` · `neutrino-detection-specialist` · `dirac-antimatter-theorist` · `nazarewicz-nuclear-structure-theorist` · `sagan-empiricist`

## Output convention

Each agent is the **sole writer** of `sessions/investigation/investigation-1/<agent-type>.md`.

## Status: COMPLETE — 31/31 on disk (2026-06-14)

All 31 research agents delivered (~157K words total). Read **`_synthesis.md`** first — it cross-indexes
all 31 reports, ranks the convergence themes, the highest-leverage untraveled bridges, the live
contradictions, and the curated-doc hygiene drifts, with a per-agent one-line index in §5.
`_dispatch-tracker.md` is the dispatch audit trail (concurrency, resume protocol). Dispatch note:
the first 8-wide batch tripped a transient server rate-limit; concurrency was dropped to 3 and
rate-limited/socket-dropped agents were RESUMED via SendMessage (context intact), not re-run fresh.
