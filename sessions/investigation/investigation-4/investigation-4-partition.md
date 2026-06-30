# Investigation 4 — Wave Partition Manifest

**Date**: 2026-06-14
**Source**: `investigation-4-seed.md §"Candidate gate table"` (mechanical bucketing; no new interpretive content).
**Seed (`--from`)**: `investigation-1/hawking-theorist.md` + `investigation-1/schwarzschild-penrose-geometer.md`.
**Mode**: INVESTIGATION (fanout). Mixed-type gates. Verdict track `computations/investigation-4/inv4_gate_verdicts.txt` (compute only; `track="investigation"`).

Bucketing rule: owner = the seed author's domain (hawking items → hawking owns that wave; sp items → sp; cross-cluster → gen-physicist neutral, per inv-3 W4 precedent). `gate_type` assigned by the `Investigating-Workshops.md` Q1/Q2/Q3 discriminator at plan-time.

---

## Wave 1 — Horizon thermodynamics, entropy & information

- **Owner-planner**: `hawking-theorist`
- **Theme**: the area law as a microstate count (not an identity); the 1/4 coefficient from D_K; the A_s greybody filter. hawking's UB1/UB2/UB3/UB5 → his Highest-Leverage Next Steps 1/2/3/5.
- **Types**: compute×4

| Gate | gate_type | Exec | One-line scope |
|:-----|:----------|:-----|:---------------|
| INV4-W1-1 | compute | hawking-theorist | GGE-relic Page curve + microstate count S=ln∏(1+n_k) vs A_horizon_FW/4 |
| INV4-W1-2 | compute | hawking-theorist | Euclidean replica S=(1−n∂_n)lnZ(n) → reproduce A_horizon_FW/4 (the 1/4 coefficient) |
| INV4-W1-3 | compute | hawking-theorist | Bousso/Bekenstein bound falsifier on the GGE relic (S_GGE ≤ A/4G) |
| INV4-W1-4 | compute | transit-dynamics-theorist | exit-horizon greybody Γ(ω); A_s=\|β_fold\|²·∫Γdω vs the 3.15-OOM AMPLITUDE-NORM-66 FAIL |

- **Intra-wave pin**: INV4-W1-3 consumes INV4-W1-1's microstate count (forward-pinned, same wave — validation disposition (b)).
- **Natural split candidate (if stalled)**: {W1-1+W1-3 entropy/microstate} (hawking) | {W1-2 replica} (hawking) | {W1-4 greybody} (transit-dynamics) — split along executor boundary.

## Wave 2 — Causal structure, censorship & the metric lift

- **Owner-planner**: `schwarzschild-penrose-geometer`
- **Theme**: the white-hole zero-count (resolve C-1 from the substrate); the τ↔t map via Raychaudhuri; censorship at the extremal horizon; GL stability as the first compact-object channel. sp's B-1/B-2/B-3 + C-1 → his Highest-Leverage Next Steps 1/2/3/4.
- **Types**: compute×4

| Gate | gate_type | Exec | One-line scope |
|:-----|:----------|:-----|:---------------|
| INV4-W2-1 | compute | schwarzschild-penrose-geometer | c_s(τ) re-derived from a₂(τ); zero-count of (v−c_s), pre-register N_zeros∈{1,2} |
| INV4-W2-2 | compute | schwarzschild-penrose-geometer | Raychaudhuri focusing for (a(t),τ(t)); τ̇→3H closure; which moment sources it |
| INV4-W2-3 | compute | schwarzschild-penrose-geometer | Christodoulou SCC on extremal Σ_dump: inextendible (sealed) vs extendible |
| INV4-W2-4 | compute | schwarzschild-penrose-geometer | Gregory-Laflamme stability of M⁴×SU(3); KK-bubble mode below λ_GL |

- **Co-author note**: INV4-W2-4 names connes-ncg-theorist for the SU(3) bundle structure (sp step 3); executor remains sp.
- **Natural split candidate (if stalled)**: {W2-1 zero-count, W2-2 Raychaudhuri} (the τ↔t/causal pair) | {W2-3 censorship, W2-4 GL} (the off-trajectory-robustness pair).

## Wave 3 — Cross-cluster bridges

- **Owner-planner**: `gen-physicist` (neutral — workshop wave, per inv-3 W4 precedent; balanced spec, no orchestrator angle)
- **Theme**: the one item bridging hawking's thermodynamics to sp's clock gap (de Sitter a₀ horizon → CC tracking), plus the one genuine adversarial workshop (Level-3 magnitude divergence).
- **Types**: compute×1, workshop×1

| Gate | gate_type | Exec / Agents | One-line scope |
|:-----|:----------|:--------------|:---------------|
| INV4-W3-1 | compute | hawking-theorist | de Sitter a₀ first law dE=−T_dS dS_dS ≡ Volovik tracking ρ_vac∼M_Pl²H²; clock in a₀ |
| INV4-W3-2 | workshop | schwarzschild-penrose-geometer ↔ lizzi-spectral-functional-theorist (2 rounds) | Level-3 magnitude convergent-vs-divergent: geometric (apex-dim) vs spectral (regulator/pole) reading |

- **Cross-check note**: INV4-W3-1 names mack-cosmic-bridge for the Volovik tracking-law side; executor remains hawking-theorist.
- **Workshop discipline**: EXACTLY 2 agents (sp ↔ lizzi); closes by artifact-existence (NO verdict line).
- **Not split** (2 gates).

---

## Gate-type tally

| Type | Count | Closure |
|:-----|:-----:|:--------|
| compute | 8 | verdict line in `inv4_gate_verdicts.txt` + WP section |
| workshop | 1 | artifact-existence (workshop md: Wrap-Up + Effected-In-Session + Carry-Forward) |

**Total: 9 gates across 3 waves.** Honest workshop count = 1 (Investigating-Workshops.md): the Level-3-divergence adjudication is the only genuine Q1a tension (competing structural readings, cross-rebuttal essential). The other 8 are compute carry-forwards of the surveys' pre-registered next-steps.

## Routed out (NOT in this plan)

6 session-track curated-register hygiene items (HY1–HY6, `investigation-4-seed.md §"Non-gate items"`) + 4 surveyed-but-not-elevated bridges (sp B-4/B-5, hawking R4/C3) are quarantined — an investigation cannot mutate curated session-track registers (track-local boundary). HY1–HY6 route to session-promotion at `/rclab-investigate --investigation 4` close.
