# S90 Slot Pre-Allocation Lockfile

> **Provenance**: S90 W7 CF-45 (mack-cosmic-bridge sole-writer per `feedback_mack-bridge-role.md`, 2026-05-15). Slot pre-allocation lockfile per `.claude/rules/epistemic-discipline.md §"Registry-Write Hygiene under Parallel-Writer Race"` slot-allocation lockfile discipline (multi-slot pre-allocation; canonical pattern: `sessions/framework/s87-slot-pre-allocation-lockfile.md`). This lockfile pre-allocates registry slots in `sessions/permanent-results-registry.md` for S90 workshop landings to prevent parallel-writer race collisions.

## Purpose

When a single workshop produces MULTIPLE registry-landings whose slot-identity must remain non-colliding across waves, the orchestrator pre-allocates the slot-letter assignments at plan-freeze time and records them here. Producing scripts consult this lockfile to confirm their planned slot is RESERVED to them; on runtime occupancy by an intervening landing, they reroute to the next-free-letter and emit FAIL-with-remediation per `epistemic-discipline.md §"Registry-Write Hygiene"` item 3.

## Allocations

### RESERVED-FOR-WORKSHOP-W7-CF-45-VII-AT

- **Reserved for**: `S90-CF-A40-FAIL-ALTERNATIVE-CHIRALITY-RESCOPE` gate (S90 W7 CF-45)
- **Slot**: `§VII.AT.OP-PROJ`
- **Workshop**: W-5 candidate (a) bi-chirality `γ_5 ⊕ γ_F` direct-sum
- **Next-free-letter basis**: §VII.AR (W-22 W7a-74) + §VII.AS (W-18 W6a-51) occupied → §VII.AT is next-free at S90 W7 CF-45 dispatch time
- **Provenance**: Spawn-prompt §"OPERATION C" Step 5; plan reference `sessions/session-plan/session-90-plan-w7.md §W7-6` lines 1167-1171
- **Sponsors**: mack-cosmic-bridge (sole writer); gen-physicist (5-anatomy completeness audit co-sign per `cross-pillar-bridge-anatomy.md §"Audit at plan-freeze"`); volovik-superfluid-universe-theorist (Level-1 declaration discipline co-sign per VOLOVIK V.2 refinement)
- **Anchor list**: §VII.AQ.OP-PROJ (parent) + §VII.AW.OP-PROJ (sibling); CF-A40 FAIL diagnostic (S89 §W2-5); W-5 CF-W5-3 + CF-W5-5 substrate-physics deferred to S91+

### RESERVED-FOR-WORKSHOP-W7-CF-45-VII-AW

- **Reserved for**: `S90-CF-A40-FAIL-ALTERNATIVE-CHIRALITY-RESCOPE` gate (S90 W7 CF-45)
- **Slot**: `§VII.AW.OP-PROJ` → **RENAMED `§VII.BF` at S93 W5-6** (the SU(3)-coloured chirality entry moved off `§VII.AW.OP-PROJ` to resolve the label-collision with SUBSTRATE-CLOCK-UNIQUENESS-THEOREM [S90 W2 CF-19]; the original `§VII.AW.OP-PROJ` reservation below records the pre-rename allocation and is SUPERSEDED-BY-RENAME)
- **Workshop**: W-5 candidate (b) SU(3)-coloured chirality `γ_F^c` per Connes-Marcolli 2008 §11
- **Next-free-letter basis**: §VII.AU (CF-63 REGISTRY-INCOMPLETE-PENDING-FIRST-EXTRACTION) + §VII.AV (CF-W7-1 W7c rerouted emission #3) occupied → §VII.AW is next-free at S90 W7 CF-45 dispatch time (skipping §VII.AU + §VII.AV)
- **Provenance**: Spawn-prompt §"OPERATION C" Step 5; plan reference `sessions/session-plan/session-90-plan-w7.md §W7-6` lines 1213-1216
- **Sponsors**: mack-cosmic-bridge (sole writer); gen-physicist (5-anatomy completeness audit co-sign); volovik-superfluid-universe-theorist (Level-1 declaration discipline co-sign)
- **Anchor list**: §VII.AQ.OP-PROJ (parent) + §VII.AT.OP-PROJ (sibling); CF-A40 FAIL diagnostic (S89 §W2-5); W-5 CF-W5-3 + CF-W5-5 substrate-physics deferred to S91+

## Cross-link to canonical slot-allocation lockfile precedent

- `sessions/framework/s87-slot-pre-allocation-lockfile.md` (S87 precedent for the lockfile pattern)
- `.claude/rules/epistemic-discipline.md §"Registry-Write Hygiene under Parallel-Writer Race"` item 3 (FAIL-with-remediation discipline on runtime occupancy)
- `.claude/rules/registry-landing.md §"Bridge-Landing Script Architecture (single-shot pattern)"` (single-shot AFTER-pattern emission, no in-place edits)

## Lockfile updates

| Date | Operation | Slot | Status |
|:-----|:----------|:-----|:-------|
| 2026-05-15 | Initial allocation per S90 W7 CF-45 | §VII.AT.OP-PROJ | RESERVED |
| 2026-05-15 | Initial allocation per S90 W7 CF-45 | §VII.AW.OP-PROJ | RESERVED |
| 2026-05-24 | S93 W5-6 RENAME §VII.AW.OP-PROJ → §VII.BF (label-collision resolution; the SU(3)-coloured chirality entry [S90 W7 CF-45] moved off §VII.AW.OP-PROJ, which is now uniquely SUBSTRATE-CLOCK-UNIQUENESS-THEOREM [S90 W2 CF-19]; label-only, content/gate-ID/SHA UNCHANGED) | §VII.AW.OP-PROJ → §VII.BF | RENAMED (SUPERSEDES the W7-CF-45-VII-AW RESERVED allocation) |
