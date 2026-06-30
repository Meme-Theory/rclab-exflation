# Investigation 13 — Wave Partition Manifest

**Date**: 2026-06-14
**Source**: `investigation-13-seed.md §"Candidate gate table"` (mechanical bucketing; no new interpretive content).
**Seed (`--from`)**: `investigation-1/gen-physicist.md` + `investigation-1/sagan-empiricist.md`.
**Mode**: INVESTIGATION (fanout). Mixed-type gates. Verdict track `computations/investigation-13/inv13_gate_verdicts.txt` (compute only; `track="investigation"`).

Bucketing rule: owner = the seed author's domain (gen items → gen owns that wave; sagan items → sagan). `gate_type` assigned by the `Investigating-Workshops.md` Q1/Q2/Q3 discriminator at plan-time. Heavy dedup against inv-2…inv-12 already applied in the seed (both seeds are cross-domain — see seed §"Dedup against inv-2…inv-12"); the single adversarial tension (A_s route) is **dedup'd to the concurrent inv-12**, so inv-13 carries 0 workshops and 2 waves (no cross-agent workshop wave).

---

## Wave 1 — Cross-domain compute: collider spectroscopy, strong-field corrections, DR3 readiness

- **Owner-planner**: `gen-physicist`
- **Theme**: the gen-distinctive survivors after dedup — the GGE cosmological-**collider** bispectrum (gen's "highest-leverage untraveled bridge"), the a₄ higher-curvature QNM/tidal-Love **correction** (the surviving leg of the compact-object overlap, complementary to inv-11 W5-2's interior), and the w₀ branch-iv truncation convergence (DR3 readiness, convergent with sagan C1). gen UB-2 / UB-3 / R1 → his Closing 1 / 3 + R1.
- **Types**: compute×3

| Gate | gate_type | Exec | One-line scope |
|:-----|:----------|:-----|:---------------|
| INV13-W1-1 | compute | transit-dynamics-theorist | GGE cosmological-collider squeezed-limit f_NL; non-analytic features at D_K eigenvalue ratios |
| INV13-W1-2 | compute | spectral-geometer | a₄→{R²,Weyl²,Gauss-Bonnet} higher-curvature correction to BH QNM + NS tidal Love; sign + M_KK-scale |
| INV13-W1-3 | compute | lizzi-spectral-functional-theorist | w₀ branch-iv evaluator pushed to L_max∈{15,16}; CAC spread vs 0.025 band (CAC binding form MANDATORY) |

- **Intra-wave pin**: none (the 3 gates are independent).
- **Convention pin (W1-3)**: DR3-class L_max-stability ⇒ CAC (canonical-anchored convention) MANDATORY per `regulator-convention-lockdown.md`; RDC is OUTSIDE the admissibility class. Planner pins `convention=CAC-Zubarev` (or scheme-anchored equivalent) in the gate block.
- **Cross-link notes (planner carries into gate blocks)**: W1-1 COMPLEMENTARY to inv-10 TRANSIT-PS bispectrum/τ_NL (collider non-analyticity vs amplitude-from-P(k)) — executor transit-dynamics, or quantum-acoustics if transit is loaded by inv-12; W1-2 DISTINCT from inv-11 W5-2 (a₄ exterior-correction vs interior v(r) construction); W1-3 DISTINCT from inv-12 W1-4/W2-2 (R_1 same-regulator / a_n pole-convergence audits — those are regulator/pole audits, not w₀ truncation).
- **Natural split candidate (if stalled)**: {W1-1 collider} (transit-dynamics) | {W1-2 a₄ QNM} (spectral-geometer) | {W1-3 w₀ truncation} (lizzi) — split along executor boundary (each gate is single-executor).

## Wave 2 — Empirical bridges: dense-matter, growth-of-structure, Bayesian re-anchor

- **Owner-planner**: `sagan-empiricist`
- **Theme**: the sagan-distinctive survivors — dense-matter color-superconductivity at high μ (genuinely untraveled; a NICER test orthogonal to the CMB axis), the S8 growth-suppression f·σ8(z) curve (the tension-resolution angle), and the post-S66 Bayesian re-anchor analysis (sagan's own domain). sagan UB2 / UB3 / R5 → his Closing 2 / 3 / 5.
- **Types**: compute×2, review×1

| Gate | gate_type | Exec | One-line scope |
|:-----|:----------|:-----|:---------------|
| INV13-W2-1 | compute | nazarewicz-nuclear-structure-theorist | finite-μ BCS-on-SU(3) (D_μ=D+μQ); CFL gap Δ(μ) + EoS stiffness vs 2 M_⊙ / NICER |
| INV13-W2-2 | compute | cosmic-web-theorist | GGE growth-suppression f·σ8(z) curve from −4.058% seed; S8∈[0.76,0.83]? localizes n_s→K_pivot |
| INV13-W2-3 | review | sagan-empiricist | post-S66 Bayesian re-anchor analysis: elicited P(pass) + look-elsewhere + recomposition finding |

- **Co-author note**: INV13-W2-1 may name landau-condensed-matter-theorist for the color-SC symmetry-breaking cross-check; executor remains nazarewicz. INV13-W2-2 may name transit-dynamics-theorist for the GGE acoustic-interference cross-check; executor remains cosmic-web.
- **Review closure (W2-3)**: artifact-existence-with-content — deliverable `investigation-13-bayesian-reanchor-synthesis.md`; NO verdict line. Track-local boundary: WRITES the analysis; the EVOI-register re-anchor + mack co-dispatch promote at `/rclab-investigate` close. Distinct from inv-12 W4-3 (A_s-route synthesis, not the framework-wide EVOI re-anchor).
- **Natural split candidate (if stalled)**: {W2-1 dense-matter} (nazarewicz) | {W2-2 growth-suppression} (cosmic-web) | {W2-3 re-anchor} (sagan, review) — split along executor/type boundary.

---

## Gate-type tally

| Type | Count | Closure |
|:-----|:-----:|:--------|
| compute | 5 | verdict line in `inv13_gate_verdicts.txt` + WP section |
| review | 1 | artifact-existence (`investigation-13-bayesian-reanchor-synthesis.md`) |

**Total: 6 gates across 2 waves.** Honest workshop count = **0** (`Investigating-Workshops.md`): the single Q1a adversarial tension both seeds converge on — the A_s route-reconciliation (CF21 TD/LI H̃-divergence) — is owned by the concurrently-registered **inv-12** (the dedicated A_s-wall investigation, route-owners lizzi + van-den-dungen + transit-dynamics: INV12-W3-5 CF21 H̃ reconciliation + INV12-W4-1 lizzi↔transit A_s workshop + INV12-W4-3 A_s synthesis). It is dedup'd out, not re-planned. The 5 computes are the surveys' pre-registered next-steps; the 1 review is sagan's Bayesian re-anchor analysis (Q1b — independent reading + write-up, not adversarial). "0 workshops" is a valid honest output when the one tension is owned by a concurrent dedicated investigation.

## Routed out (NOT in this plan)

- **The one adversarial tension (A_s route-reconciliation) → dedup'd to inv-12** (`seed §"Dedup against inv-2…inv-12"`, top row): INV12-W3-5 (CF21 H̃ reconciliation) + INV12-W4-1 (lizzi↔transit A_s workshop) + INV12-W4-3 (A_s three-route synthesis). The gen G4 + sagan G2/R1 A_s convergence is the cross-domain echo of inv-12's dedicated attack; no distinctive cross-domain angle survives.
- **8 session-track curated-register hygiene items** (HY1–HY8, `investigation-13-seed.md §"Non-gate items"`) — n_s multi-anchor σ-default + COMMITTED-LIVE-FIRING tag (HY1); m_H down-tag (HY2); H₀ single-number (HY3); neutrino headline cluster (HY4, mack); the substrate-PROVEN-vs-methodology-MANDATORY aggregate partition (HY5); M_KK headline consolidation (HY6); 3He-B inheritance-direction caveat (HY7, mack lab-suite); the K_pivot reconciliation note (HY8). An investigation cannot mutate curated session-track registers (track-local boundary); these route to session-promotion at `/rclab-investigate --investigation 13` close.
- **8 dedup'd-against-inv-2…inv-12 candidates** (`seed §"Dedup against inv-2…inv-12"`): A_s route → inv-12 (above); d_s(σ)-flow → inv-11 W3-2; eigenvalue rigidity → inv-3 W1-1; PBH-from-fold → inv-8; compact-object interior → inv-11 W5-2; η_B shortfall → inv-6 W3-1/W3-3; SA-as-dynamical-functional → inv-5 W3-2 + inv-12 W4-2; Volovik-BBN → inv-11 W4-1; M_KK derive-or-prove → inv-3/6/11 (standing gap).
- **5 surveyed-but-not-elevated** (`seed §"Surveyed-but-not-elevated"`): w_a prediction-definition gap; order-one partial-axiom-sufficiency proof; K_pivot mechanism; the SU(3)/Jensen/volume-preserving + τ_fold + f-physical assumption cluster; the sagan UB1 echo-spacing leg.
