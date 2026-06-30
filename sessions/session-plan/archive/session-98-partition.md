# Session 98 — Wave Partition Manifest

**Date**: 2026-05-31
**Mode**: fanout
**Source**: `session-98-context.md` (11-item consolidated CF set V.1–V.11, from S97 synthesis §V + WP CFs + housekeeping §B)
**Total**: 6 waves, 11 gates.

This manifest buckets the 11 carry-forwards into waves by theme + reviewer-origin owner, EVOI-ordered (`evoi-framework.md §6`, S98 re-stamp). Single-gate waves (1, 5, 6) are justified inline (keystone isolation / distinct axis / METHODOLOGY-class separation). Concurrency ≤8 per batch — all 6 wave-planner dispatches fit one batch.

---

## Wave dependency graph

```
W1 (V.1 keystone, a(t) route-recon)
  │  delivers route-selected substrate H(τ)
  ▼
W2 (V.2 relaxation-closure ── HARD: needs W1's H(τ))
   (V.9 MK3-1 sign ── independent of W1; cheap lead) → (V.10 MK3-2 BBN ── needs V.9)

W3 (V.3 Yukawa ε_LX ── precondition §VII.BL LANDED S97) → (V.4 diag companion)
   (V.5 baryogen-uniqueness ── independent)

W4 (V.6 BF covariance ── strengthened-by W1, not blocked) ; (V.7 κ-indep ── independent)

W5 (V.8 a0a2 PV-invariance ── independent, optional robustness)

W6 (V.11 σ₈ channel-keyed pins ── METHODOLOGY-class hygiene, independent)
```

**The only HARD cross-wave ordering is W1 → W2 (V.1 gates V.2).** W3/W4/W5/W6 are independent of W1/W2 and of each other (modulo their internal companion orderings). At `/rclab-coordinate` time, W1 must close before W2's V.2 dispatches; everything else can pipeline.

---

## Wave 1 — Emergent-FRW a(t) route reconciliation (the C1 keystone)

- **Owner (planner)**: `gen-physicist` (cross-pillar keystone — one compute spanning the a(t) frontier, the CC relaxation enablement, and the BF-spine dagger; breadth owner per the reviewer-origin = combined-landscape synthesis).
- **Class**: COMPUTE.
- **Items**:
  - V.1 `S98-W1-ROUTE-RECONCILIATION` — select the canonical acoustic-frame H(τ) (AOFT by a₂-uniqueness), pin the unique τ̇ shape (from 50 admissible), re-test q_Ω route-invariance. Two-clause PASS (frame-resolution + AOFT-frame q_Ω band-membership).
- **Gate executor (per-gate `agent_type`)**: `kaluza-klein-theorist` (a₂ Seeley-DeWitt → g_M emergence is the dimensional-reduction substrate) OR `gen-physicist` — planner's call at gate-block authorship.
- **Natural split candidates** (if the planner stalls): none — single gate. If the two PASS-clauses prove to need separate machinery, split into W1a (Clause-1 frame-resolution) + W1b (Clause-2 AOFT-frame q_Ω + τ̇-shape sub-gate), same full-fidelity spec.

## Wave 2 — CC closure & C10 sign/BBN cluster

- **Owner (planner)**: `volovik-superfluid-universe-theorist` (C10 = Volovik tracking-vacuum; the cluster is the Volovik q-theory CC discharge + its sign/BBN arm).
- **Class**: COMPUTE.
- **Items**:
  - V.2 `S98-W2-2-RELAXATION-CLOSURE` — derive q~H from the substrate friction ODE (Object C; the single unconditional-CC leg). **HARD: AFTER Wave 1** (inherits route-selected H(τ)).
  - V.9 `S98-MK3-1-C10-SUBLEADING-SIGN` — q→0 type-A/B + C_meas-conditioning (cheap regression lead, independent of W1).
  - V.10 `S98-MK3-2-BBN-VACUUM-FRACTION` — propagate n_eff=1.978 into the BBN-epoch vacuum fraction (after V.9).
- **Gate executors**: V.2 → `transit-dynamics-theorist` or `volovik-superfluid-universe-theorist` (friction-ODE / cosmological relaxation); V.9/V.10 → `volovik-superfluid-universe-theorist` or `mack-cosmic-bridge` (C10/BBN cross-cut).
- **Natural split candidates**: W2a {V.9, V.10} (the C10 sign/BBN arm, independent of W1 — can run alongside W1) + W2b {V.2} (the relaxation-closure, gated on W1). This split is the recommended decomposition if the orchestrator wants to start the cheap V.9 lead before W1 closes.

## Wave 3 — Matter sector (#7 Yukawa ε_LX + #9 baryogenesis uniqueness)

- **Owner (planner)**: `connes-ncg-theorist` (the §VII.BL E1 generation-blindness obstruction is connes-authored; the ε_LX inheritance-kernel channel is NCG inner-fluctuation structure).
- **Class**: COMPUTE.
- **Items**:
  - V.3 `S98-W3-1-YUKAWA-EPS-LX-BETWEEN-GEN` — external non-LI ε_LX between-generation channel (precondition §VII.BL LANDED S97 licenses the PASS-gate).
  - V.4 `S98-W3-1-DIAG` — within-J-FIXED-sector widened diagnostic (INFO, companion to V.3).
  - V.5 `S98-W3-2-BARYOGEN-UNIQUENESS` — pin (ε_nLI, φ_CP) from a substrate principle (existence→uniqueness).
- **Gate executors**: V.3/V.4 → `connes-ncg-theorist` (NCG inner-fluctuation / multiplicity-bundle); V.5 → `dirac-antimatter-theorist` (baryogenesis/CP) or `volovik-superfluid-universe-theorist` (inheritance-falsifier kernel).
- **Natural split candidates**: W3a {V.3, V.4} (Yukawa ε_LX + diagnostic) + W3b {V.5} (baryogenesis uniqueness) — split along the #7-vs-#9 frontier boundary if the wave stalls.

## Wave 4 — Observational: BF-spine covariance + κ-determinacy

- **Owner (planner)**: `mack-cosmic-bridge` (observational surface — BF spine + CGWB are the mack-owned falsifier domain).
- **Class**: COMPUTE.
- **Items**:
  - V.6 `S98-W4-4-OQ3-COVARIANCE` — BF-spine off-diagonal covariance (rank-2 dagger licensing; strengthened if W1 lifts the {a₀,a₂} dagger).
  - V.7 `S98-KAPPA-INDEP-FROM-CGWB-FREQ` — does the CGWB peak-frequency axis supply a dimensionally-independent seconds-scale (κ "consistency-pinned" → "independently-pinned")?
- **Gate executors**: V.6 → `mack-cosmic-bridge` or `sagan-empiricist` (statistical BF / covariance); V.7 → `mack-cosmic-bridge` or `hawking-theorist` (κ-licensing, S-1 origin).
- **Natural split candidates**: W4a {V.6} + W4b {V.7} — independent observational axes; trivially separable.

## Wave 5 — Spectral-moment robustness (a₀/a₂ PV-invariance)

- **Owner (planner)**: `lizzi-spectral-functional-theorist` (a₀/a₂ PV-scheme invariance is the spectral-functional / regulator-class axis — S-3 campaign origin).
- **Class**: COMPUTE.
- **Items**:
  - V.8 `S98-A0A2-TIER2-PV-INVARIANCE` — re-evaluate §8.5 tier-2 survival under FI-anchor vs PV-anchor; verify d(survival)/d(PV-scheme)=0 numerically.
- **Single-gate justification**: distinct regulator-class axis (a_n^{regulator} discipline), optional-robustness, lizzi-owned; folding it into the Wave-2 CC cluster would mix the spectral-functional axis with the q-flow CC axis. Kept separate for clean owner + axis attribution.
- **Natural split candidates**: none (single gate).

## Wave 6 — Canonical-constants hygiene (σ₈ channel-keyed promotion)

- **Owner (planner)**: `gen-physicist` (orchestrator-default for hygiene/methodology; the σ₈ promotion is canonical-constants bookkeeping).
- **Class**: **METHODOLOGY** (PASS = artifact-existence: `get_constant` resolves both channel-keyed pins with channel-distinct PROVENANCE + cross-note). Requires M1–M4 conjunction + an **allowlist row** appended to `methodology-wave-allowlist-ledger.md` at plan-freeze (orchestrator-only, recursion-attack closure).
- **Items**:
  - V.11 `S98-HK-SIGMA8-CHANNEL-KEYED-PINS` — promote `sigma8_OZ_50=0.799` (S50 spectral-action) + `sigma8_growth_a2=0.79317` (S70/S96 a₂ growth-channel) with channel-distinct provenance + cross-note; pre-register the canonical naming + headline choice.
- **Single-gate justification**: METHODOLOGY-class cannot merge with a COMPUTE wave without becoming MIXED-class (which would force sub-decomposition anyway, per `wave-classification.md` NROY clause). Kept as its own light final wave — mirrors S97's W6 structure.
- **Natural split candidates**: none (single gate).

---

## Classification summary (for `_wave_classification_audit.py` at plan-freeze)

| Wave | Class | Gates | METHODOLOGY allowlist needed |
|:----:|:------|:------|:-----------------------------|
| 1 | COMPUTE | 1 | — |
| 2 | COMPUTE | 3 | — |
| 3 | COMPUTE | 3 | — |
| 4 | COMPUTE | 2 | — |
| 5 | COMPUTE | 1 | — |
| 6 | METHODOLOGY | 1 | **YES** — `S98-HK-SIGMA8-CHANNEL-KEYED-PINS` row to `methodology-wave-allowlist-ledger.md` (orchestrator-only) at plan-freeze, M1–M4 confirmed in the W6 plan |

**Standing gap** (NOT a wave gate): atlas-04 C2 K_pivot scale mapping — recorded in `session-98-context.md §"Standing gap"`; leverage ≠ tractability (no pre-registrable K→g_M PASS criterion this session).
