# Session 115 — Wave Partition Manifest

**Built by**: `/rclab-plan --session 115` (2026-06-24), Phase 1c.
**Scope source**: `sessions/session-plan/session-115-context.md` (6 compute gates).
**Mode**: `--fanout` — per-wave plan file + per-wave WP.
**Total**: 6 compute gates / 3 waves. EVOI-ordered (structural-permanent promotions first; confirmatory/optional refinements last).

> **Session character**: SMALL focused session at the framework's completion plateau. The substantive payload is the §VII.CK SHAPE-branch genus completion (two blind Stage-2 cross-axis promotions) + the named-external-corridor lepton-PMNS residue test. W3 carries one confirmatory re-run + two OPTIONAL low-EVOI refinements (retained per `session-handoffs.md`, not dropped).

## Dependency graph

```
W1-1 (VIICK-STAGE2-VERIFY)  ──┐  (same §VII.CK slot; STAGE2-VERIFY promotes D1–D3 first)
                              └──►  W2-1 (VIICK-D4-DISCHARGE)   [re-scopes D4 → UNCONDITIONAL]
W1-2 (LEPTON-PMNS)             — independent of W2-1 (tests the corridor residue)
W3-1 / W3-2 / W3-3             — all mutually independent; no upstream dep
```

Only ONE inter-gate dependency: **W2-1 depends on W1-1** (both write the §VII.CK registry slot; STAGE2-VERIFY must land the D1–D3 → STAGE-3-PERMANENT flip before D4-DISCHARGE re-scopes D4 → UNCONDITIONAL). This registry-write sequencing is why D4-DISCHARGE is a separate wave, not a parallel W1 gate.

---

## Wave 1 — §VII.CK D1–D3 Stage-2 promotion + lepton-corridor residue

- **Theme**: complete the SHAPE-branch homogeneity-obstruction genus (the closed-class promotion) + test the named external crossed-product corridor's forced PMNS texture.
- **Owner / planner**: `gen-physicist` (the §VII.CK registry sole-writer domain + cross-domain breadth; the gate EXECUTORS are the named blind cross-reviewers / neutrino specialist, set per-gate in the gate blocks).
- **Gates (2)**:

| Item | Gate ID | Scope | Executor (agent_type in gate block) |
|:--|:--|:--|:--|
| W1-1 | `CF-S115-VIICK-STAGE2-VERIFY` | §VII.CK D1–D3 closed-class STAGE-1-CANDIDATE → STAGE-3-PERMANENT (D4-open RETAINED); 2 blind cross-reviewers, **connes + paasch + downstream excluded** | Axis-A NCG/spectral (e.g. lizzi/spectral-geometer) + Axis-B structurally-distinct (e.g. volovik/transit/kitaev) — pick 2 NON-AUTHOR axes; closeout gen-physicist |
| W1-2 | `CF-S115-LEPTON-PMNS-FORCED-TEXTURE` | construct the `A_K⋊SU(3)_R` lepton-sector circulant + `ℂ⊕ℍ` asymmetry; test forced tri-maximal `J=1/(6√3)` vs PMNS J after charged-lepton correction; quark negative control `U_mix→identity` | `neutrino-detection-specialist` (PMNS owner) + `gen-physicist` (circulant construction) |

- **Natural split candidate** (if the wave stalls): W1-1 (the §VII.CK Stage-2 verify) and W1-2 (lepton-PMNS compute) are on independent substrates → split along the NCG-promotion / particle-PMNS boundary.

---

## Wave 2 — §VII.CK D4 discharge (depends on W1-1)

- **Theme**: discharge the FOURTH door (D4 right-regular SU(3)_R) external-as-a-coupling → complete the genus UNCONDITIONALLY.
- **Owner / planner**: `gen-physicist` (§VII.CK registry domain; executors are the named cross-reviewers).
- **Gates (1)**:

| Item | Gate ID | Scope | Executor (agent_type in gate block) |
|:--|:--|:--|:--|
| W2-1 | `CF-S115-VIICK-D4-DISCHARGE-UNCONDITIONAL` | D4 external-coupling discharge → STAGE-3-PERMANENT-UNCONDITIONAL (genus COMPLETE); Axis-A lizzi/spectral-geometer × Axis-B volovik; **connes+paasch+vdd+baptista+kk excluded** | Axis-A `lizzi-spectral-functional-theorist` OR `spectral-geometer`; Axis-B `volovik-superfluid-universe-theorist`; closeout gen-physicist |

- **Dependency**: W1-1 (`CF-S115-VIICK-STAGE2-VERIFY`) must land its D1–D3 → STAGE-3-PERMANENT flip first (same registry slot). W2-1 verifies a DIFFERENT clause (D4) and re-scopes the slot to UNCONDITIONAL.
- **Natural split candidate**: single gate; no split. If W1-1 FAILs (D1–D3 not promoted), W2-1 routes to PRE-REG-INC mechanical closure (upstream-blocked per `mechanical-closure-discipline.md`) — the plan MUST pre-register this downstream decision point.

---

## Wave 3 — confirmatory + optional low-EVOI refinements

- **Theme**: mechanical due-diligence (τ_cross confirmation) + two OPTIONAL magnitude-refinement objects from the S114 closed corridors.
- **Owner / planner**: `transit-dynamics-theorist` (owns W3-1 + W3-2; W3-3 executor is hawking, set in its gate block).
- **Gates (3, all independent)**:

| Item | Gate ID | Scope | Executor (agent_type in gate block) |
|:--|:--|:--|:--|
| W3-1 | `CF-S115-S0-KNOB-CROSS-SUBSTITUTION-CONFIRM` | confirmatory τ_cross=0.191038 cross-substitution of `s101_w3_s0_knob.py` + Sage CF check; CONFIRMS-CANNOT-FLIP the W-1 verdict; small (~15 min) | `transit-dynamics-theorist` or `gen-physicist` |
| W3-2 | `CF-S115-AS-NEWAXIS-SELECTOR` (OPTIONAL, low) | maxent/Connes-distance new-axis A_s functional selector to collapse the 1.259-OOM cross-functional spread | `transit-dynamics-theorist` |
| W3-3 | `CF-S115-B5A-TFD-QES` (OPTIONAL, lowest, Tier-3 NON-BLOCKING) | two-sided island QES extremization of `S=Area/4+S_bulk` | `hawking-theorist` |

- **Optional disposition**: W3-2/W3-3 are RETAINED per `session-handoffs.md` (carried, EVOI-last) but flagged OPTIONAL. User may drop either at the Phase-3b checkpoint.
- **Natural split candidate**: by executor — {W3-1, W3-2} transit-owned vs {W3-3} hawking-owned. The QES gate (W3-3) is the heaviest (~1–2 waves) → split it out first if the wave stalls.

---

## Wave-class declaration (plan-freeze)

All 6 gates are **COMPUTE-class** (`wave-classification.md` M1: each has a numerical pre-registered PASS/FAIL/INFO predicate). The two Stage-2 verifies (W1-1, W2-1) are PASS-AND cross-axis gates with verdict lines — COMPUTE-class, NOT METHODOLOGY-class. **No `methodology-wave-allowlist.md` append owed.** No MIXED-class wave (no sub-wave decomposition needed).

## EVOI ordering check

W1 (structural-permanent promotion + zero-param observational test) ≻ W2 (structural-permanent-unconditional, gated on W1) ≻ W3 (confirmatory + OPTIONAL low/lowest). EVOI-decreasing across waves. ✓
