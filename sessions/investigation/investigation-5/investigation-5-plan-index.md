# Investigation 5 — Plan Index (fanout)

**Date**: 2026-06-14
**Seed (`--from`)**: `investigation-1/{connes-ncg-theorist, landau-condensed-matter-theorist, spectral-geometer}.md` (3-agent survey batch; spectral-geometer reused from inv-3 with explicit dedup)
**Driver**: investigation-1. **Shape**: fanout (3 per-wave plan files + this index).
**Topic**: NCG spectral-action ↔ condensed-matter order-parameter joints — converging on (i) the m_H=131.8 GeV / +5.36% Higgs-amplitude residual, (ii) the two-effective-actions tension (is Tr f(D²) the substrate's free energy? — connes & landau co-cite the same 93× BCS-wrong-sign result), (iii) the A_s amplitude on the extensive axis.
**Verdict track**: `computations/investigation-5/inv5_gate_verdicts.txt` (compute gates; `emit_verdict(session=5, track="investigation", ...)`). Workshop + review gates close by artifact-existence (no verdict line).

| Wave | Theme | Owner-planner | Types | Gates | Plan file | 3a validation |
|:----:|:------|:--------------|:------|:-----:|:----------|:--------------|
| 1 | NCG spectral-action joints | connes-ncg-theorist | compute×5 | 5 | `investigation-5-plan-w1.md` | YAML 5/5 PASS · pins EXIT=0 |
| 2 | Condensed-matter functionals | landau-condensed-matter-theorist | compute×4 | 4 | `investigation-5-plan-w2.md` | YAML 4/4 PASS · pins EXIT=0 |
| 3 | Cross-vantage joints (a₄ truncation / two-effective-actions / Higgs-residual) | gen-physicist (neutral) | compute×1, workshop×1, review×1 | 3 | `investigation-5-plan-w3.md` | YAML 3/3 PASS · pins EXIT=0 |

**Total: 12 gates** (10 compute + 1 workshop + 1 review). Honest workshop count: **1** (the two-effective-actions adjudication, INV5-W3-2 — a genuine Q1a, opposed first-principles readings, cross-rebuttal essential).

## Gate manifest (per wave)

**Wave 1 — connes-ncg-theorist (compute×5):**
- `INV5-W1-1-PS-QUADRATIC-FLUCTUATION-HIGGS-QUARTIC` — Pati-Salam quadratic-fluctuation spectral action (order-one violated) → Higgs quartic → m_H vs 131.8 (band ≤6.7 GeV). Exec: connes.
- `INV5-W1-2-A4-WEYL-TRACE-ANOMALY-CC-CHANNEL` — a₄→{YM,Higgs-quartic,Weyl²,Gauss-Bonnet}; Weyl²/anomaly non-monotone in τ + vs ρ_Λ (`a_4^{ζ}`; Riemann analytically rebuilt — npz absent). Exec: connes.
- `INV5-W1-3-CONNES-DISTANCE-LEPTON-MASS-LADDER` — per-state Connes distance on ℂ^N → lepton signature (d_e−d_μ)/(d_μ−d_τ) → 1.889035 (Sage-exact). Exec: connes.
- `INV5-W1-4-MODULAR-TWIST-MULTIPLICITY-NONSCALAR` — Tomita-Takesaki twist of A_K⋊ℝ (§VII.BZ) multiplicity-NON-scalar? (intra-substrate ε_LX). Exec: connes.
- `INV5-W1-5-ENTROPY-FUNCTIONAL-CC-A0-A2-RATIO` — CC under von Neumann entropy functional → a₀/a₂ ≠ C_Q/R? Exec: **lizzi-spectral-functional-theorist** (spectral-functional-selection question).

**Wave 2 — landau-condensed-matter-theorist (compute×4):**
- `INV5-W2-1-AS-IMPULSE-QUENCH-BOGOLIUBOV` — A_s via frozen |β_k|²/ξ̂ (canonical `xi_KZ_FW=0.0187601`, NOT the 0.808 xi_BCS-analog) → ONE OOM + frozen k̂. Exec: **transit-dynamics-theorist**.
- `INV5-W2-2-NSR-PSEUDOGAP-TWO-SCALE-DM` — NSR two-scale split D_s (Ω_DM) vs Δ_pg (170×); target r≈14.2. Exec: landau.
- `INV5-W2-3-PEKKER-VARMA-HIGGS-SELF-ENERGY` — Pekker-Varma Re Σ from B2/B3 continuum → −5.36% (=−67/1251)? Exec: landau.
- `INV5-W2-4-GOLDSTONE-MASS-FROM-DISORDER` — Imry-Ma m²~1/ξ_disorder² (J_su2=0.059, J_u1=0.038 canonical) ≫ Leggett anchor AND below edge? Exec: landau.

**Wave 3 — gen-physicist neutral planner (mixed):**
- `INV5-W3-1` (compute) — a₄ extensive-axis **L_max-convergence** (3→4→5→6 at τ_fold): +5.36% a truncation tail or a floor? (`a_4^{ζ}`; Friedrich-Bär saturation feasibility; distinct from inv-3 W2-2's τ-isospectral-rigidity). Exec: **spectral-geometer**.
- `INV5-W3-2` (workshop) — two-effective-actions adjudication, **connes ↔ landau** (EXACTLY 2, 2 rounds); STRUCTURAL VERDICT. Closes by artifact-existence → `workshops/two-effective-actions.md`.
- `INV5-W3-3` (review) — Higgs-residual synthesis (gen-physicist neutral, 1 agent); depends on W1-1 + W2-3 + W3-1. Closes by artifact-existence → `investigation-5-higgs-residual-synthesis.md`.

## Dispatch

Each per-wave plan is independently dispatchable:
```
/rclab-coordinate sessions/investigation/investigation-5/investigation-5-plan-w1.md
/rclab-coordinate sessions/investigation/investigation-5/investigation-5-plan-w2.md
/rclab-coordinate sessions/investigation/investigation-5/investigation-5-plan-w3.md
```
Full investigation (juggles compute / workshop / review dispatch):
```
/rclab-coordinate sessions/investigation/investigation-5/investigation-5-plan-index.md
```

**Wave order**: W1 ∥ W2 run independently. W3's compute (INV5-W3-1) + workshop (INV5-W3-2) are independent of W1/W2 verdicts and may run alongside; W3's review (INV5-W3-3) consumes INV5-W1-1 + INV5-W2-3 + INV5-W3-1 and is gated on them (mechanical-closure if unmet at dispatch).

**Non-gate (Q2 hygiene, session-promotion at `/rclab-investigate --investigation 5` close)**: HY1 — pin ONE canonical A_s gap number (3 named quantities → `canonical_constants.py`); routed via `mack` for any falsifier-inventory row (sole-writer). See `investigation-5-seed.md §"Non-gate items"`.
