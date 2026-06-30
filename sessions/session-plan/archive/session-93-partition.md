# Session 93 — Wave Partition Manifest

**Generated**: 2026-05-24 (orchestrator, `/rclab-plan --session 93`, Phase 1c)
**Mode**: fanout — per-wave plan + per-wave WP
**Scope source**: `sessions/session-plan/session-93-context.md` (deduplicated CF table + 4-field specs + filter log)
**Totals**: 10 waves (W0 setup, runs FIRST + W1-W9 compute), 46 gates (S92 carry-forward, post-dedup/re-scope)

## Partition rationale

Waves are grouped by §VII-slot theme + reviewer-origin owner (the `/rclab-plan` partition discipline). The S92 mack-synthesis §V.1 dependency-tier ordering (anchor-supplying → value-pinning → Stage-2/STAGE-3 flips) is encoded WITHIN and ACROSS waves via per-gate `Depends on` fields + per-wave Decision Points — NOT as a separate wave. Each per-gate Tier tag (T1/T2/T3) is carried in the context file.

## Wave dependency graph

```
Wave 0 (runs FIRST):  W0-1 — slot-pre-allocation lockfile + sequencing record; prereq for ALL Tier-3 flips

Tier-1 (anchor-supplying / decision-closing):   W1-2 (BA Stage-1)   W3-1 (AV slot-split)   W5-1 (R_machine CF-A)
                                                      |                    |                      |
Tier-2 (value-pinning compute):     W2-1 (Fredholm)  W3-2/3-3 (PV+8.7)  W4-1 (E2)  W4-3 (n_PBH)   |
                                                      |                    |                      |
Tier-3 (Stage-2 + STAGE-3 flips):  W2-2 (AU S3)  W3-6 (AV S2)  W4-2/4-4/4-5 (AX S2+land)  W5-2 (AY S3)  W5-5 (AW S3)  W6-3/6-4 (BB/BE S2)
```

**Wave 0 runs FIRST** (gate W0-1): it lands the slot-pre-allocation lockfile + sequencing record that every Tier-3 STAGE-3 flip depends on. Waves W1, W7, W8 are otherwise largely independent (own internal sequencing). W6-1 (Pati-Salam SU(4)) is heavy/gated and may defer to S94 at the 3b checkpoint. Cross-wave STAGE-3 registry-write flips (AU/AW/AY/AV/AX/BB/BE) require the Wave-0 slot-pre-allocation lockfile (pattern `sessions/framework/s90-slot-pre-allocation-lockfile.md`).

---

## Wave 0 — STAGE-3 sequencing pre-registration + slot-pre-allocation lockfile (runs FIRST)
- **Owner**: gen-physicist
- **Gates (1)**: W0-1 — STAGE-3-promotion sequencing record (mack §V.1) + anti-inflation K-counter check (mack §V.2) + create `s93-slot-pre-allocation-lockfile.md` reserving the 7 colliding STAGE-3 slots (§VII.AU/AW/AY/AV/AX/BB/BE). **Upstream prereq for all 7 Tier-3 STAGE-3-flip gates; dispatched FIRST.** (Relocated from the W9 grouping 2026-05-24 to fix a run-order dependency inversion.)
- **Split candidate**: none (1 gate)

## Wave 1 — §VII.BA Wodzicki-BCS composite bridge map
- **Owner**: connes-ncg-theorist
- **Gates (3)**: deep-pole masquerade discriminator (W1-1); §VII.BA Stage-1 registration (W1-2, Tier-1, mack-leg); F-functor non-scalar reconstruction T3/T4/T5 (W1-3)
- **Split candidate**: none (cohesive; 3 gates)

## Wave 2 — §VII.AU + CF-37 Fredholm-module + STAGE-3
- **Owner**: connes-ncg-theorist
- **Gates (4)**: Fredholm-index integer triple (W2-1, Tier-2, GPU); §VII.AU.OP-PROJ STAGE-3 promotion (W2-2, Tier-3, mack); canonical_constants sub-class-keyed α promotion (W2-3); module-as-canonical corpus row (W2-4, mack)
- **Split candidate**: W2a (compute: W2-1) + W2b (mack registry/promotion: W2-2/2-3/2-4) if mack-leg congestion

## Wave 3 — §VII.AV anchor reconciliation + slot-split + Stage-2
- **Owner**: volovik-superfluid-universe-theorist
- **Gates (7)**: slot-split landing (W3-1, Tier-1); PV-bottom-K restriction (W3-2, Tier-2); Class-8.7 degeneracy-witness (W3-3, Tier-2); PROXY-REFINEMENT Connes-Karoubi (W3-4); STATE-PROJ/OP-PROJ registry landing (W3-5, mack); Stage-2 per sub-slot (W3-6, Tier-3, vdd+mack); multiplicative-normalization K=2 rule extension (W3-7, METHODOLOGY)
- **Split candidate**: W3a (substrate-physics compute: W3-2/3-3/3-4) + W3b (mack registry + Stage-2 + rule: W3-1/3-5/3-6/3-7) along reviewer-origin boundary

## Wave 4 — §VII.AX PBH cluster
- **Owner**: mack-cosmic-bridge
- **Gates (6)**: E2 verdict-artifact re-emission (W4-1, Tier-2, connes); MULTI-PIN-ATLAS Stage-2 (W4-2, Tier-3); n_PBH canonical-truncation factorization (W4-3, Tier-2, volovik+connes); STATE-PROJ companion landing (W4-4, Tier-3, CHAINED); n_PBH_FW_central promotion (W4-5, Tier-3, CHAINED); FWD-C5 K=2 cardinality-cascade-shoulder (W4-6, CHAINED)
- **Split candidate**: W4a (E2 + factorization compute: W4-1/4-3) + W4b (CHAINED landings: W4-2/4-4/4-5/4-6)

## Wave 5 — §VII.AY R_machine + §VII.AR + §VII.AW
- **Owner**: mack-cosmic-bridge
- **Gates (6)**: R_machine recompute CF-A (W5-1, Tier-1, MANDATORY arbiter); §VII.AY Element-5 tolerance + Stage-2 + STAGE-3 CF-B (W5-2, Tier-3, CHAINED on W5-1); §VII.AR FULL-tier N4 retry + reclassification rule (W5-3, compute executor nazarewicz/connes); §VII.AR filter-geometry audit (W5-4); §VII.AW STAGE-3 promotion (W5-5, Tier-3, mack); §VII.AW slot-rename (W5-6, mack)
- **Split candidate**: W5a (§VII.AY R_machine: W5-1/5-2) + W5b (§VII.AR/§VII.AW: W5-3/5-4/5-5/5-6)

## Wave 6 — chirality / HH^1 / Pati-Salam Stage-2
- **Owner**: connes-ncg-theorist
- **Gates (4)**: §VII.AQ STAGE-3 via Pati-Salam SU(4) (W6-1, heavy ~3 we, gated on D_K_PS feasibility — defer-to-S94 candidate at 3b); §VII.AZ Element 4 tag replacement (W6-2, mack); §VII.BB Stage-2 + DEGENERATE-pole regime-identity (W6-3, Tier-3, connes+landau); FWD-C4 Pati-Salam Stage-2 + Level-3 (W6-4, Tier-3, connes+volovik/landau)
- **Split candidate**: none (4 gates; W6-1 may drop at checkpoint)

## Wave 7 — α_s transport-degree + SCHEMATIC-vs-FULL + spectral-dimension
- **Owner**: connes-ncg-theorist (gate executors per-item)
- **Gates (3)**: α_s w·κ factorization → deg(T_BZ→pivot) (W7-1, connes+transit); K_csub_R FULL-physical retry (W7-2); fold-energy windowed d_s gate discharging S34 [F-4] (W7-3, kk+landau)
- **Split candidate**: none (3 gates, distinct executors but coherent "SCHEMATIC-vs-FULL / first-principles substrate" theme)

## Wave 8 — LQG narrow-path cluster
- **Owner**: phonon-first-cosmologist
- **Gates (7)**: eigenvalue inventory (W8-1); Casimir table (W8-2); Cauchy-Schwarz joint preflight (W8-3, highest-EVOI); dimensional-prefactor pin (W8-4); Workshop-1 gate prereg (W8-5); pre-post-Bogoliubov ratio (W8-6); Workshop-6 dispatch (W8-7, gated on W8-3)
- **Split candidate**: W8a (pre-flights W8-1..W8-4, <0.3 we total) + W8b (gate-prereg + workshop W8-5..W8-7)

## Wave 9 — methodology / audit-scripts / cross-cutting
- **Owner**: gen-physicist
- **Gates (5)**: plan-line-anchor validator (W9-1); plan-corpus section-number drift detector (W9-2); bridge-map-scheme suffix K=3 MANDATORY (W9-3); per-Bulletin-per-pole K=3 (W9-4, OPTIONAL/EVOI-gated); Layer-Functor F reformulation workshop (W9-5, /rclab-workshop). (The STAGE-3-promotion sequencing + anti-inflation K-counter + slot-pre-allocation lockfile gate relocated to **Wave 0** as W0-1.)
- **Split candidate**: none (5 gates; W9-4 optional may drop at checkpoint)

---

## Dispatch batching (planner swarm; ≤8 concurrent per `feedback_dispatch-discipline.md`)

- **Batch 1** (5 planners): W1, W2, W3, W4, W5
- **Batch 2** (4 planners): W6, W7, W8, W9

Each planner writes ONE `session-93-plan-w{i}.md` per `.claude/templates/plan-compute.md` per-wave shape + full-fidelity R3 YAML gate blocks. Stalls → split along the listed split candidate, re-dispatch with SAME full-fidelity spec (no degradation).
