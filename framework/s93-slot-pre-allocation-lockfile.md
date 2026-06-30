# S93 Slot Pre-Allocation Lockfile

> **Provenance**: S93 W0-1 `S93-W0-1-STAGE-3-PROMOTION-SEQUENCING-PREREG` (gen-physicist DRAFT author; mack-cosmic-bridge sole-writer confirms landing per `feedback_mack-bridge-role.md`, 2026-05-24). Slot pre-allocation lockfile per `.claude/rules/epistemic-discipline.md §"Registry-Write Hygiene under Parallel-Writer Race"` (multi-slot pre-allocation; canonical pattern: `sessions/framework/s90-slot-pre-allocation-lockfile.md`). This lockfile pre-allocates the 7 colliding STAGE-3-PERMANENT registry slots in `sessions/permanent-results-registry.md` for the S93 §VII Stage-3 program (mack-synthesis §V.1 sequencing) to prevent parallel-writer race collisions across the 7 Tier-3 STAGE-3-flip gates (W2-2, W3-6, W4-2, W5-2, W5-5, W6-3, W6-4).

## Purpose

The S93 §VII STAGE-3-PERMANENT-promotion program lands MULTIPLE registry-writes whose slot-identity must remain non-colliding across waves. The orchestrator pre-allocates the slot assignments at plan-freeze time (Wave 0, before any compute wave) and records them here. Each Tier-3 producing script consults this lockfile to confirm its planned slot is RESERVED to it; on runtime occupancy by an intervening landing, it reroutes to the next-free-letter and emits FAIL-with-remediation per `epistemic-discipline.md §"Registry-Write Hygiene"` item 3. W0-1 runs FIRST so every colliding STAGE-3 registry-write has its RESERVED-FOR block before any Tier-3 gate fires; a Tier-3 gate that fires before this lockfile lands honestly closes PRE-REG-INC (`value='PRE-REG-INC_blocked_by_s93_slot_lockfile_NOT-LANDED'`) and re-runs after W0-1 per `mechanical-closure-discipline.md`.

## Allocations (7 RESERVED-FOR blocks — one per colliding STAGE-3 flip)

### RESERVED-FOR-S93-W2-2-VII-AU-OP-PROJ-STAGE-3-PERMANENT-PROMOTION

- **Reserved for**: `S93-W2-2-VII-AU-OP-PROJ-STAGE-3-PERMANENT-PROMOTION gate (S93 W2)`
- **Slot**: `§VII.AU.OP-PROJ`
- **Workshop**: W-2 §VII.AU CF-37 Fredholm-module + STAGE-3 cascade (connes-ncg-theorist)
- **Next-free-letter basis**: §VII.AU.OP-PROJ is an EXISTING occupied slot (STAGE-1-CANDIDATE, S91 W5/W6 landing); W2-2 is an in-place STAGE-3-PERMANENT tag-flip, NOT a new-letter allocation -- the RESERVED-FOR block protects the slot identity against a concurrent next-free-letter writer claiming §VII.AU during the W2-2 write-window.
- **Provenance**: session-93-plan-w2.md §W2-2; mack-synthesis V.1 Tier-3; cites §W5-4 audit 4a95a276... + §W5-5 audit 64d45d71... Stage-2 PASS-AND-AND-PASS chain
- **Sponsors**: mack-cosmic-bridge (sole writer); connes-ncg-theorist (Fredholm-index value-pin co-sign, W2-1); gen-physicist (5-anatomy + sequencing audit co-sign, W0-1)
- **Anchor list**: §VII.AU.OP-PROJ parent (STAGE-1-CANDIDATE); §VII.AU CF-37 Fredholm-module-as-canonical corpus §19; CORRIDOR-CONFIRMED-NUMERICAL-DEFERRED sub-class tag preserved

### RESERVED-FOR-S93-W5-5-VII-AW-OP-PROJ-STAGE-3-PERMANENT-PROMOTION

- **Reserved for**: `S93-W5-5-VII-AW-OP-PROJ-STAGE-3-PERMANENT-PROMOTION gate (S93 W5)`
- **Slot**: `§VII.AW.OP-PROJ`
- **Workshop**: W-5 §VII.AW STAGE-3 + canonical_constants promotion (mack-cosmic-bridge)
- **Next-free-letter basis**: §VII.AW.OP-PROJ is an EXISTING occupied slot (S90 W7 CF-45 reservation, STAGE-1-CANDIDATE since S91 W4); W5-5 is an in-place STAGE-3-PERMANENT tag-flip (framework's THIRD). NOTE: a SEPARATE S93 W5-6 slot-rename moves the rejected SU(3)-Coloured-Chirality entry to a free slot (>= §VII.BF); §VII.AW.OP-PROJ retains the SUBSTRATE-CLOCK-UNIQUENESS-THEOREM and is reserved here for W5-5.
- **Provenance**: session-93-plan-w5.md §W5-5; mack-synthesis V.1 Tier-3; cites §W4-5 Stage-2 composite PASS-AND 6/6 (audit 4bd3017e...) + S91 W4-3 Axis-A hawking (69df5fa7...)
- **Sponsors**: mack-cosmic-bridge (sole writer); hawking (S91 W4-3 Axis-A inherited PASS); gen-physicist (sequencing audit co-sign, W0-1)
- **Anchor list**: §VII.AW.OP-PROJ SUBSTRATE-CLOCK-UNIQUENESS-THEOREM (STAGE-1-CANDIDATE); §VII.AQ.OP-PROJ parent; §VII.AT.OP-PROJ sibling; S90 W7 CF-45 RESERVED-FOR-WORKSHOP-W7-CF-45-VII-AW origin

### RESERVED-FOR-S93-W5-2-VII-AY-ELEMENT-5-TOLERANCE-STAGE-2-STAGE-3

- **Reserved for**: `S93-W5-2-VII-AY-ELEMENT-5-TOLERANCE-STAGE-2-STAGE-3 gate (S93 W5)`
- **Slot**: `§VII.AY.OP-PROJ`
- **Workshop**: W-5 §VII.AY R_machine Element-5 tolerance Stage-2/Stage-3 (mack-cosmic-bridge)
- **Next-free-letter basis**: §VII.AY.OP-PROJ is an EXISTING occupied slot (STAGE-1-CANDIDATE); W5-2 flips it to STAGE-3-PERMANENT on the 3-axis PASS-AND vs the CF-A substrate-sourced R_machine pin. ORDERED AFTER CF-A (W5-1, MANDATORY upstream arbiter). RESERVED-FOR protects the slot against concurrent claim during the tolerance-driven re-emission.
- **Provenance**: session-93-plan-w5.md §W5-2; mack-synthesis V.1 Tier-3 + corpus §21.0 R1/R2/R3; DEPENDS ON CF-A R_machine recompute (W5-1); DEFERRED-to-R_machine tag (corpus §21)
- **Sponsors**: mack-cosmic-bridge (sole writer); van-den-dungen-bridge-theorist (Axis-A PASS); cross-pillar spectral-geometer (Axis-B PASS); gen-physicist (sequencing audit, W0-1)
- **Anchor list**: §VII.AY.OP-PROJ Element-5 cocycle-ratio R=(dE_6.dE_7)/(dE_8)^2 (STAGE-1-CANDIDATE); Element-3(iii) K=1->K=2; corpus §21 K=1 calibration instance; canonical pin substrate_cocycle_ratio_67_88 re-pinned at CF-A

### RESERVED-FOR-S93-W3-6-VII-AV-STAGE-2-CROSS-AXIS-VERIFY-PER-SUB-SLOT

- **Reserved for**: `S93-W3-6-VII-AV-STAGE-2-CROSS-AXIS-VERIFY-PER-SUB-SLOT gate (S93 W3)`
- **Slot**: `§VII.AV (per sub-slot: §VII.AV.OP-PROJ + §VII.AV.STATE-PROJ)`
- **Workshop**: W-3 §VII.AV anchor reconciliation + slot-split + Stage-2 (volovik-superfluid-universe-theorist)
- **Next-free-letter basis**: §VII.AV is split by W3-1 (Tier-1) into §VII.AV.OP-PROJ (Cell I) + §VII.AV.STATE-PROJ (Cell IV) STRUCTURAL-ORTHOGONAL-COMPANION; cross-corner co-primary FORBIDDEN. W3-6 Stage-2 verifies per sub-slot. RESERVED-FOR protects BOTH sub-slot identities against concurrent next-free-letter claim during the per-sub-slot write-window.
- **Provenance**: session-93-plan-w3.md §W3-6 (CHAINED on W3-1 split); mack-synthesis V.1 Tier-3; corpus §22 three-object reconciliation; substrate-input-orthogonality MANDATORY K=3
- **Sponsors**: mack-cosmic-bridge (sole writer for registry-text); van-den-dungen-bridge-theorist (Axis-A); volovik via OAA-exclusion {connes, phonon-first, volovik}; gen-physicist (sequencing audit, W0-1)
- **Anchor list**: §VII.AV.OP-PROJ (Cell I; B_LAYER_A=3.752271e+02 M_KK^2; gated by W3-3 Class-8.7 witness); §VII.AV.STATE-PROJ (Cell IV; L_emp=-7.046336474406761 M_KK^2 single Level-3 anchor); FULL-PV -527.97 regulator-class diagnostic sub-row

### RESERVED-FOR-S93-W4-2-VII-AX-MULTI-PIN-ATLAS-STAGE-2-CROSS-AXIS-VERIFY

- **Reserved for**: `S93-W4-2-VII-AX-MULTI-PIN-ATLAS-STAGE-2-CROSS-AXIS-VERIFY gate (S93 W4)`
- **Slot**: `§VII.AX.OP-PROJ (MULTI-PIN-ATLAS)`
- **Workshop**: W-4 §VII.AX PBH cluster (mack-cosmic-bridge)
- **Next-free-letter basis**: §VII.AX.OP-PROJ.MULTI-PIN-ATLAS is an EXISTING occupied STAGE-1-CANDIDATE slot; W4-2 Stage-2 cross-axis verifies it. A SEPARATE W4-4 lands a NEW §VII.AX.STATE-PROJ companion (Cell IV) and W4-5 promotes n_PBH_FW_central -- those are distinct slots. RESERVED-FOR protects the MULTI-PIN-ATLAS identity during the Stage-2 write-window.
- **Provenance**: session-93-plan-w4.md §W4-2; mack-synthesis V.1 Tier-3; cites §W6-1 PASS (a006b809...) + §W6-2 K=2 corpus rows §3/§10/§17; CHAINED on W4-1 E2 re-emission + W4-3
- **Sponsors**: mack-cosmic-bridge EXCLUDED as reviewer (slot owner); Axis-A in {connes, lizzi}; Axis-B in {volovik, gen-physicist}; gen-physicist (sequencing audit, W0-1)
- **Anchor list**: §VII.AX.OP-PROJ MULTI-PIN-ATLAS (STAGE-1-CANDIDATE); n_PBH grid obs_2 (s91_w5_3_cf41_upper_22_6.npz, L=14/15/16); §W6-1 PASS a006b809...; E2 re-emission W4-1

### RESERVED-FOR-S93-W6-3-VII-BB-STAGE-2-CROSS-AXIS-VERIFY-REGIME-IDENTITY

- **Reserved for**: `S93-W6-3-VII-BB-STAGE-2-CROSS-AXIS-VERIFY-REGIME-IDENTITY gate (S93 W6)`
- **Slot**: `§VII.BB`
- **Workshop**: W-6 chirality / HH^1 / Pati-Salam Stage-2 (connes-ncg-theorist)
- **Next-free-letter basis**: §VII.BB is an EXISTING occupied STAGE-1-CANDIDATE slot (HH^1 s=5; FIRST-EXTRACTION DISCHARGED at S92 W9-8, alpha(s=5,d=4)=0 saturating). W6-3 Stage-2 verifies + adjudicates the composite-vs-licensed-FB DEGENERATE-pole regime-IDENTITY; STAGE-1->STAGE-3 eligible iff PASS-AND. Subsumes CF-S93-W7-4.
- **Provenance**: session-93-plan-w6.md §W6-3; mack-synthesis V.1 Tier-3; cites §W9-8 npz + vii_bb_element_5_empirical_anchor_FW=11.763253530952039 + FB min eta_FB=0.4465
- **Sponsors**: connes-ncg-theorist (Axis-A); landau-condensed-matter-theorist (Axis-B); volovik EXCLUDED; mack-cosmic-bridge (sole writer for registry-text); gen-physicist (sequencing audit, W0-1)
- **Anchor list**: §VII.BB (STAGE-1-CANDIDATE; HH^1 s=5); Level-3 anchor 11.763253530952039; 3 candidate-regime R^2 fits (composite 0.992 / log 0.953 / FB 0.865); FB-saturation predicate

### RESERVED-FOR-S93-W6-4-FWD-C4-PATI-SALAM-STAGE-2-CROSS-AXIS-VERIFY-LEVEL-3

- **Reserved for**: `S93-W6-4-FWD-C4-PATI-SALAM-STAGE-2-CROSS-AXIS-VERIFY-LEVEL-3 gate (S93 W6)`
- **Slot**: `§VII.BE`
- **Workshop**: W-6 FWD-C4 Pati-Salam Stage-2 cross-axis verify + Level-3 (connes-ncg-theorist)
- **Next-free-letter basis**: §VII.BE is an EXISTING occupied STAGE-1-CANDIDATE slot (FWD-C4 Pati-Salam, S91 W9-12 derivation + S92 W7-9 registry landing; occupied §VII.B letters A-B-C-D-E). W6-4 Stage-2 cross-axis verifies the JOINT clauses + Level-3 anchor. RESERVED-FOR protects the §VII.BE identity during the Stage-2 write-window.
- **Provenance**: session-93-plan-w6.md §W6-4; mack-synthesis V.1 Tier-3; cites §VII.BE STAGE-1-CANDIDATE text + S91 W9-12 derivation (chi_PS:A_K->A_PS; audit e16af0ba...)
- **Sponsors**: connes-ncg-theorist (Axis-A); volovik-superfluid-universe-theorist OR landau-condensed-matter-theorist (Axis-B); mack-cosmic-bridge (sole writer); gen-physicist (sequencing audit, W0-1)
- **Anchor list**: §VII.BE FWD-C4 Pati-Salam (STAGE-1-CANDIDATE); A_K_PS=C+M_2(C)_L+M_2(C)_R+M_4(C)_PS rank-4; SU(4)_C decomposition M_4(C)->C+M_2(C)+M_2(C); Level-3 empirical anchor at canonical L_max

## Cross-link to canonical slot-allocation lockfile precedent

- `sessions/framework/s90-slot-pre-allocation-lockfile.md` (S90 precedent; this lockfile's 7-field RESERVED-FOR block template)
- `sessions/framework/s87-slot-pre-allocation-lockfile.md` (S87 origin of the lockfile pattern)
- `.claude/rules/epistemic-discipline.md §"Registry-Write Hygiene under Parallel-Writer Race"` item 3 (FAIL-with-remediation discipline on runtime occupancy)
- `.claude/rules/registry-landing.md §"Bridge-Landing Script Architecture (single-shot pattern)"` (single-shot AFTER-pattern emission, no in-place edits)
- `sessions/archive/session-92/session-92-mack-synthesis.md §V.1` (the dependency-ordered Stage-3 sequencing record this lockfile backs)

## Lockfile updates

| Date | Operation | Slot | Status |
|:-----|:----------|:-----|:-------|
| 2026-05-24 | Initial allocation per S93 W0-1 (mack-synthesis §V.1 Tier-3) | §VII.AU.OP-PROJ | RESERVED |
| 2026-05-24 | Initial allocation per S93 W0-1 (mack-synthesis §V.1 Tier-3) | §VII.AW.OP-PROJ | RESERVED |
| 2026-05-24 | Initial allocation per S93 W0-1 (mack-synthesis §V.1 Tier-3) | §VII.AY.OP-PROJ | RESERVED |
| 2026-05-24 | Initial allocation per S93 W0-1 (mack-synthesis §V.1 Tier-3) | §VII.AV (per sub-slot: §VII.AV.OP-PROJ + §VII.AV.STATE-PROJ) | RESERVED |
| 2026-05-24 | Initial allocation per S93 W0-1 (mack-synthesis §V.1 Tier-3) | §VII.AX.OP-PROJ (MULTI-PIN-ATLAS) | RESERVED |
| 2026-05-24 | Initial allocation per S93 W0-1 (mack-synthesis §V.1 Tier-3) | §VII.BB | RESERVED |
| 2026-05-24 | Initial allocation per S93 W0-1 (mack-synthesis §V.1 Tier-3) | §VII.BE | RESERVED |
| 2026-05-24 | S93 W5-5 STAGE-3-PERMANENT CONFIRMED on-disk (branch (a) verification-only; S92 in-session promotion verified, NO duplicate flip); AU/AW '#3' ordinal collision recorded NOT renumbered -> CF-S94-STAGE-3-ORDINAL-COLLISION-AU-AW | §VII.AW.OP-PROJ | STAGE-3-PERMANENT-CONFIRMED |
