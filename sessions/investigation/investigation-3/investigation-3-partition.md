# Investigation 3 — Wave Partition Manifest

**Date**: 2026-06-14
**Seed**: `investigation-3-seed.md` (3-agent survey batch: berry-geometric-phase-theorist + spectral-geometer + paasch-mass-quantization-analyst)
**Shape**: fanout (4 per-wave plan files + thin plan-index)
**Source**: `investigation-3-seed.md §"Candidate gate table"` — this manifest re-buckets that table into the per-wave planner-swarm input.

Per-wave planners read this manifest's "assigned items" rows + the seed file. Owner = the wave's domain-survey author (reviewer-origin owner). Gate executors (`agent_type` in each gate block) are suggested per gate; the per-wave planner finalizes by substrate match.

---

## Wave 1 — Spectral statistics & eigenbundle topology

- **Owner-planner**: `berry-geometric-phase-theorist` (seed author; owns the spectral-statistics + catastrophe + non-Abelian-holonomy cluster)
- **Types**: compute × 4
- **Theme**: the framework has measured the *parameter-space* geometry of its eigenbundles to death while leaving the *spectral-correlation* geometry of the eigenvalues almost untouched at the discriminating level (berry "bottom line"). This wave attacks that asymmetry.

| # | Gate ID | gate_type | Suggested exec | One-line scope |
|:--|:--------|:----------|:---------------|:---------------|
| 1 | INV3-W1-1 | compute | kitaev-quantum-chaos-theorist (or berry) | SFF K(τ) + number variance Σ²(L)/Δ₃(L) at τ_fold — Poisson/RMT/arithmetic discriminator |
| 2 | INV3-W1-2 | compute | kitaev-quantum-chaos-theorist (or berry) | P(s) semi-Poisson/Berry–Robnik fit, **sector-resolved** (pooling-artifact test) |
| 3 | INV3-W1-3 | compute | berry-geometric-phase-theorist | catastrophe germ of λ_min(τ,μ): fold A₂(Airy) vs cusp A₃(Pearcey) + diabolical-point census |
| 4 | INV3-W1-4 | compute | berry-geometric-phase-theorist | second Chern c₂ of B2 bundle over 4-param C² coset (λ₄..λ₇); Yang-monopole test |

- **Natural-split candidates** (if the wave stalls): {INV3-W1-1, INV3-W1-2} statistics sub-wave (kitaev) | {INV3-W1-3, INV3-W1-4} topology sub-wave (berry).
- **Shared inputs**: L12 spectrum cache (`s84_spectrum_cache_L12_tau019.npz` or equivalent); S96/S105 off-Jensen scaffold (W1-3/W1-4); CF-S102-B2-EPS2-WZ-HOLONOMY driver (W1-4).

## Wave 2 — Heat-kernel scale-transport & spectral rigidity

- **Owner-planner**: `spectral-geometer` (seed author; heat-trace governing-structure vantage)
- **Types**: compute × 4
- **Theme**: the framework's dimensionless (intensive, R-protected) predictions are on solid heat-kernel footing; its weaknesses are all on the **dimensionful/extensive axis** (M_KK normalization, A_s amplitude, K-pivot). This wave attacks that axis with heat-kernel machinery.

| # | Gate ID | gate_type | Suggested exec | One-line scope |
|:--|:--------|:----------|:---------------|:---------------|
| 1 | INV3-W2-1 | compute | spectral-geometer | d_s(σ) flow as K→K* scale map: ∫θ dlnσ vs ln(K/K*)≈3.1 e-folds (reuses S92) |
| 2 | INV3-W2-2 | compute | spectral-geometer | isospectral rigidity at L_max=3: τ-scan for bit-identical {a_0,a_2,a_4} differing in Kosmann V_nm |
| 3 | INV3-W2-3 | compute | spectral-geometer | A_s floor as near-floor-DOS / exp(−ζ'_D(0)) under n_s-selected functional; ONE regulator-tagged OOM |
| 4 | INV3-W2-4 | compute | spectral-geometer | Weyl-law remainder → non-variational route to τ_fold (shortest-geodesic stationarity) |

- **Natural-split candidates**: {INV3-W2-1, INV3-W2-3} dimensionful-axis sub-wave | {INV3-W2-2, INV3-W2-4} rigidity/trace-formula sub-wave.
- **Cross-track note**: INV3-W2-3 touches the A_s wall (mack's falsifier surface). The COMPUTE is a spectral-geometer investigation gate; any `falsifier-master-inventory.md` ROW update is session-promotion + mack sole-writer (NOT an investigation edit).

## Wave 3 — Mass-quantization & Paasch bridges

- **Owner-planner**: `paasch-mass-quantization-analyst` (seed author; mass-phenomenology vantage)
- **Types**: solo × 1, compute × 4 (mixed)
- **Theme**: the framework independently re-derived a Casimir-graded exponential mass function (9/5 widening) that is *structurally* Paasch's exponential mass function, in a different namespace, while Paasch's own program sits ~95% UNCOMPUTED. This wave connects the two namespaces and harvests the bridges.

| # | Gate ID | gate_type | Suggested exec | One-line scope |
|:--|:--------|:----------|:---------------|:---------------|
| 1 | INV3-W3-1 | solo | orchestrator (inline) | machine-ε Sage QQ: S₀ =? φ_paasch^{fN} (1.6942 & 95/56); hold→derive, coincidence→kill |
| 2 | INV3-W3-2 | compute | paasch-mass-quantization-analyst | W3-1: W₃ M(6,5) Z₃-Potts kink ratios (Reshetikhin-Smirnov) contain φ_paasch/fN within 2%? |
| 3 | INV3-W3-3 | compute | paasch-mass-quantization-analyst | chain-level α-dim (n3=dim(3,0)=10 throughout) + two-α reconciliation (1/137 ← 1/10.8 KK-run) |
| 4 | INV3-W3-4 | compute | paasch-mass-quantization-analyst | Casimir-graded N(j)=7n test at L_max=12, τ_fold (do 7,35,42,98,150 emerge?) — ties to M_KK |
| 5 | INV3-W3-5 | compute | paasch-mass-quantization-analyst | Koide Q=2/3 from Casimir-envelope √m vector + Z₃ wall geometry (45° Foot angle) |

- **gate_type rationale**: INV3-W3-1 is a cheap one-thread Sage QQ identity check on a coincidence the seed author FOUND → **solo** (orchestrator-inline; more independent than the finder verifying its own coincidence, per "kill it cleanly"). INV3-W3-2 needs literature retrieval (Reshetikhin-Smirnov W₃ kink masses) → **compute** (dispatched agent with paper-search/web + paasch context). The rest are cached-spectrum / Sage computes.
- **Natural-split candidates**: {INV3-W3-1, INV3-W3-2, INV3-W3-3} φ/α sub-wave | {INV3-W3-4, INV3-W3-5} Casimir-ladder/Koide sub-wave.

## Wave 4 — M_KK derivability adjudication

- **Owner-planner**: `gen-physicist` (NEUTRAL — not a workshop participant; writes a balanced adjudication spec, no orchestrator angle per `feedback_review-dispatch-no-orchestrator-angle.md`)
- **Types**: workshop × 1
- **Theme**: the framework's #1 standing gap (M_KK-DERIVATION) is read OPPOSITELY by two seed authors — spectral-geometer (scale-free spectral triple; NNU rank-1 §VII.BS confirms NO absolute scale is predicted) vs paasch (Paasch's N(j)=7n + proton-cubic is a candidate *derivation*). This is the one genuine Q1a adjudication (opposed readings, cross-rebuttal essential).

| # | Gate ID | gate_type | Agents (EXACTLY 2) | One-line scope |
|:--|:--------|:----------|:-------------------|:---------------|
| 1 | INV3-W4-1 | workshop | spectral-geometer ↔ paasch-mass-quantization-analyst (2 rounds) | Is M_KK derivable (Paasch machinery) or structurally-irreducible (NNU rank-1)? STRUCTURAL VERDICT: live corridor vs proven-impossible wall + decisive forward gate |

- **adjudication_question (a)(b)(c)**: (a) does NNU rank-1 *prove* in-principle underivability or merely confirm one external pin? (b) does Paasch's N(j)=7n + proton-cubic fix m_p (hence M_KK) WITHOUT a hidden external scale once the dead Dirac-G~1/t scaffolding is severed? (c) what single compute decides it (candidate: INV3-W3-4)?
- **Closure**: artifact-existence (Wrap-Up + Effected-In-Session + Carry-Forward Computations); NO verdict line.
- **Independence note**: this is an exploratory adjudication workshop (domain advocates argue their case) — NOT a Stage-2 joint-theorem cross-check, so the no-prior-context rule does not apply; the two advocates are SUPPOSED to bring their domain reading.

---

## Dispatch summary

| Wave | Theme | Owner-planner | Types | Gates | Plan file |
|:----:|:------|:--------------|:------|:-----:|:----------|
| 1 | Spectral statistics & eigenbundle topology | berry-geometric-phase-theorist | compute×4 | 4 | investigation-3-plan-w1.md |
| 2 | Heat-kernel scale-transport & spectral rigidity | spectral-geometer | compute×4 | 4 | investigation-3-plan-w2.md |
| 3 | Mass-quantization & Paasch bridges | paasch-mass-quantization-analyst | solo×1, compute×4 | 5 | investigation-3-plan-w3.md |
| 4 | M_KK derivability adjudication | gen-physicist (neutral) | workshop×1 | 1 | investigation-3-plan-w4.md |

4 per-wave planners dispatched in ONE parallel batch (≤8 concurrent). Total **14 gates** (12 compute + 1 solo + 1 workshop).
