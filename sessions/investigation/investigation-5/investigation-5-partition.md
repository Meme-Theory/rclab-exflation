# Investigation 5 — Wave Partition Manifest

**Date**: 2026-06-14
**Seed**: `investigation-5-seed.md` (3-agent survey batch: connes-ncg-theorist + landau-condensed-matter-theorist + spectral-geometer)
**Shape**: fanout (3 per-wave plan files + thin plan-index)
**Source**: `investigation-5-seed.md §"Candidate gate table"` — this manifest re-buckets that table into the per-wave planner-swarm input.

Per-wave planners read this manifest's "assigned items" rows + the seed file. Owner = the wave's domain-survey author (reviewer-origin owner), except W3 whose owner is a NEUTRAL planner because it carries the adjudication workshop. Gate executors (`agent_type` in each gate block) are suggested per gate; the per-wave planner finalizes by substrate match.

**Cross-investigation dedup (carried from seed §"DEDUP")**: spectral-geometer's five next-steps are already inv-3 W2-1…W2-4 + inv-3 HY4/HY6 — NOT re-planned here. spectral-geometer's only new inv-5 gate is INV5-W3-1 (a₄ **L_max-convergence**, distinct from inv-3 W2-2's τ-isospectral-rigidity), and it plays the heat-kernel-adjudicator role inside W3-2/W3-3.

---

## Wave 1 — NCG spectral-action joints

- **Owner-planner**: `connes-ncg-theorist` (seed author; owns the spectral-triple / spectral-action / inner-fluctuation / Connes-distance cluster)
- **Types**: compute × 5
- **Theme**: the framework's load-bearing physics claims rest on three departures from NCG orthodoxy — D_K≡D_F with order-one BROKEN at norm 4.0 (connes G-1/C-1), f-is-physical (A-3), SA-is-the-effective-action (A-2). This wave attacks the joints where the spectral triple meets the Standard Model: the Higgs quartic with the order-one violation present, the only-uncomputed NCG CC channel (a₄ anomaly), the fermion-hierarchy ε_LX (Connes-distance + modular twist), and the unexamined entropy functional.

| # | Gate ID | gate_type | Suggested exec | One-line scope |
|:--|:--------|:----------|:---------------|:---------------|
| 1 | INV5-W1-1 | compute | connes-ncg-theorist | Pati-Salam quadratic-fluctuation spectral action (order-one VIOLATED, quadratic terms present) → Higgs quartic → m_H vs 131.8 within eps_H band |
| 2 | INV5-W1-2 | compute | connes-ncg-theorist | a₄ → {YM, Higgs-quartic, Weyl², Gauss-Bonnet}; isolate Weyl²+trace-anomaly; non-monotone in τ (escapes W4) + vs ρ_Λ |
| 3 | INV5-W1-3 | compute | connes-ncg-theorist | per-state Connes-distance fermion-mass ladder on ℂ^N; lepton signature (d_e−d_μ)/(d_μ−d_τ) → 1.89 (≠1) |
| 4 | INV5-W1-4 | compute | connes-ncg-theorist | Tomita-Takesaki modular twist of A_K⋊ℝ (§VII.BZ): is [D_K,a]_σ multiplicity-NON-scalar? (intra-substrate ε_LX) |
| 5 | INV5-W1-5 | compute | connes-ncg-theorist | CC under von Neumann entropy functional S_vN=Tr f_S(D²/β²): does a₀/a₂ ≠ C_Q/R (breaks S65 universality + W4)? |

- **Natural-split candidates** (if the wave stalls): {INV5-W1-1, INV5-W1-2, INV5-W1-5} spectral-action/CC sub-wave (Higgs quartic + a₄-anomaly + entropy functional) | {INV5-W1-3, INV5-W1-4} fermion-ε_LX sub-wave (Connes-distance + modular twist).
- **Shared inputs**: researchers/Connes/23 (CCS-2013 quadratic fluctuations) + /24 (Pati-Salam) + Paper-15 (CCvS-2019 entropy functional); S97 W5-2 PS-condensate machinery (W1-1); Riemann 147/147 (W1-2; co-machinery with INV5-W3-1 a₄ split); S88-CONNES-DISTANCE=0.980 + S100a W2-4 distance machinery (W1-3); §VII.BZ crossed product A_K⋊ℝ S105-S106 (W1-4); S65 a₀/a₂=C_Q/R universality theorem (W1-5, the wall probed).
- **Cross-track note**: INV5-W1-3's lepton mass-spacing signature (1.89) and INV5-W1-2's CC-vs-ρ_Λ touch mack's falsifier surface; any `falsifier-master-inventory.md` row is session-promotion + mack sole-writer (NOT an investigation edit). INV5-W1-3/W1-4 are ADJACENT to inv-2's off-U(2) Yukawa (same G-4 gap, different machinery) — complementary, not duplicate.

## Wave 2 — Condensed-matter functionals (impulse-quench / pseudogap / self-energy)

- **Owner-planner**: `landau-condensed-matter-theorist` (seed author; order-parameter / sudden-quench / BCS-BEC vantage)
- **Types**: compute × 4
- **Theme**: the recurring structural finding of the landau survey — "the substrate keeps reaching for an equilibrium free energy where the physics is a sudden quench." The two big live gaps (A_s amplitude, DM mass) are Landau problems attacked with the wrong functional. This wave fixes the functional: impulse-quench A_s normalization, NSR pseudogap two-scale DM mass, Pekker-Varma Higgs self-energy, Goldstone-mass-from-disorder.

| # | Gate ID | gate_type | Suggested exec | One-line scope |
|:--|:--------|:----------|:---------------|:---------------|
| 1 | INV5-W2-1 | compute | transit-dynamics-theorist (or landau) | A_s in the impulse-quench limit: frozen Bogoliubov |β_k|² / ξ_KZ; output ONE OOM number + frozen wavenumber k̂ |
| 2 | INV5-W2-2 | compute | landau-condensed-matter-theorist | NSR/pseudogap two-scale split of (0,0)-gap: D_s (phase-stiffness, Ω_DM) vs Δ_pg (structure mass, ~170×) |
| 3 | INV5-W2-3 | compute | landau-condensed-matter-theorist | Pekker-Varma Higgs |S|²-mode continuum self-energy from B2/B3 two-quasiparticle continuum → −5.36%? |
| 4 | INV5-W2-4 | compute | landau-condensed-matter-theorist | Goldstone-mass-from-disorder m²~1/ξ_disorder² (J_su2=0.059, J_u1=0.034); ≫ Leggett anchor + below pair-breaking edge? |

- **Natural-split candidates** (if the wave stalls): {INV5-W2-1, INV5-W2-3} amplitude/normalization sub-wave (A_s impulse-quench + Higgs self-energy — both Bogoliubov/continuum objects) | {INV5-W2-2, INV5-W2-4} dark-matter-mass sub-wave (pseudogap two-scale + Goldstone-disorder, both targeting the 170× shortfall).
- **Shared inputs**: T1-T4 transit data (P_exc=1.000, 59.8 pairs, ξ_KZ=0.808 sudden-quench floor, pair wavefunction 93%B2/6.3%B1/0.7%B3) (W2-1); Peotta-Törmä D_s machinery + C11 Mass_LeggettDM/Δ_BCS=11.97 + m_required/m_Leggett=170 (W2-2); (0,0)-sector amplitude-mode data (c_Br5_Higgs3=11.465, ω_H2=1.410) + B2/B3 continuum (W2-3); J_su2=0.059, J_u1=0.034, edge x_L1=0.149 (W2-4); the n_s-SELECTED functional (W2-1).
- **Cross-track note**: INV5-W2-1 is the impulse-quench A_s route — COMPLEMENTS (does not duplicate) inv-3 W2-3's near-floor-DOS/ζ'(0) route to the same wall. Its OOM output + the canonical_constants A_s-number pin (seed HY1) are session-promotion + mack, NOT an investigation edit.

## Wave 3 — Cross-vantage joints: a₄ truncation, the two-effective-actions adjudication, the Higgs-residual synthesis

- **Owner-planner**: `gen-physicist` (NEUTRAL — not a workshop participant; writes a balanced adjudication spec, no orchestrator angle per `feedback_review-dispatch-no-orchestrator-angle.md`; mirrors inv-3 W4's neutral-planner precedent for the adjudication workshop)
- **Types**: compute × 1, workshop × 1, review × 1 (mixed)
- **Theme**: the three surveys converge on two joints — the m_H +5.36% Higgs-amplitude residual (3-way: connes' Pati-Salam quartic, landau's Pekker-Varma self-energy, spectral-geometer's a₄ truncation-tail) and the two-effective-actions tension (is the spectral action the substrate's free energy? connes co-cites the 93× BCS-wrong-sign with landau). This wave supplies spectral-geometer's heat-kernel adjudication of those joints: the a₄ L_max-convergence compute, the connes↔landau adjudication workshop, and the Higgs-residual synthesis review.

| # | Gate ID | gate_type | Exec / Agents (workshop = EXACTLY 2) | One-line scope |
|:--|:--------|:----------|:-------------------------------------|:---------------|
| 1 | INV5-W3-1 | compute | spectral-geometer | a₄ extensive-axis L_max-CONVERGENCE (3→4→5→6 at τ_fold): is the +5.36% an a₄ truncation tail (resolvable) or a floor (physical)? |
| 2 | INV5-W3-2 | workshop | connes-ncg-theorist ↔ landau-condensed-matter-theorist (2 rounds) | Is Tr f(D²) the substrate's free energy? SA-authority-preserved (fix f / a₄-anomaly) vs SA-authority-rejected-for-OP-sector (Landau-Ginzburg). STRUCTURAL VERDICT. |
| 3 | INV5-W3-3 | review | gen-physicist (neutral) | Synthesize the three Higgs-residual readings (W1-1 quartic + W2-3 self-energy + W3-1 a₄-tail): sign+magnitude agreement; truncation vs physical |

- **gate_type rationale**: INV5-W3-1 is a cached-spectrum heat-kernel compute on spectral-geometer's substrate (the one genuinely-new SG contribution; planner=neutral gen-physicist, executor=spectral-geometer, planner≠executor). INV5-W3-2 is the one genuine Q1a workshop — connes and landau hold OPPOSED first-principles readings of the SAME 93×/120-OOM evidence (SA wrong functional vs SA-is-a-moment-not-an-energy), cross-rebuttal essential. INV5-W3-3 is a Q1b independent-synthesis review (1 agent; "synthesize/characterize X"), gated on the three upstream Higgs computes.
- **Natural-split candidates** (if the wave stalls): the three gates are already type-distinct and independently dispatchable; no further split needed. If W3-3's prereqs (W1-1, W2-3, W3-1) are unmet at dispatch it closes per `mechanical-closure-discipline.md` or defers to inv-5 close.
- **Shared inputs**: a₄ moment data across L_max + the m_H +5.36%/38.5σ residual (W3-1); connes C-3/A-2/R-3 + landau U-1 survey sections + spectral-geometer G4 (ζ_D(1)=2776.17 vs a_2^{SD}=0.728235, factor 3812) (W3-2); the W1-1/W2-3/W3-1 deliverables + the three surveys' Higgs sections (W3-3).
- **Independence note (workshop)**: INV5-W3-2 is an exploratory adjudication (domain advocates argue their case) — NOT a Stage-2 joint-theorem cross-check, so the no-prior-context rule does NOT apply; the two advocates are SUPPOSED to bring their domain reading. spectral-geometer is NOT a participant (its G4 is shared cited evidence both sides invoke), which is precisely why a neutral non-participant (gen-physicist) plans the spec and spectral-geometer can supply the heat-kernel evidence without taking a side.
- **Wave-order dependency**: W3 runs AFTER (or alongside) W1/W2. W3-1 (SG compute) and W3-2 (workshop) are independent of W1/W2 verdicts and may run in parallel with them; W3-3 (review) consumes W1-1 + W2-3 + W3-1 and is gated on them.

---

## Dispatch summary

| Wave | Theme | Owner-planner | Types | Gates | Plan file |
|:----:|:------|:--------------|:------|:-----:|:----------|
| 1 | NCG spectral-action joints | connes-ncg-theorist | compute×5 | 5 | investigation-5-plan-w1.md |
| 2 | Condensed-matter functionals | landau-condensed-matter-theorist | compute×4 | 4 | investigation-5-plan-w2.md |
| 3 | Cross-vantage joints (a₄ truncation / two-effective-actions / Higgs-residual) | gen-physicist (neutral) | compute×1, workshop×1, review×1 | 3 | investigation-5-plan-w3.md |

3 per-wave planners dispatched in ONE parallel batch (≤8 concurrent). Total **12 gates** (10 compute + 1 workshop + 1 review). Honest workshop count: **1** (the two-effective-actions adjudication).
