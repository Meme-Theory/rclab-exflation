# Session 100a — Wave Partition Manifest (`/rclab-plan` Phase 1c)

**Generated**: 2026-06-03 | **Mode**: fanout | **Waves**: 6 | **Gates**: 19
**EVOI ordering source**: `sessions/evoi-framework.md` §6 (S100a re-stamp, audit PASS lag=0). Wave 1 = the Tier-1/Tier-2 cosmology queue; Waves 2–4 = the rank-9b-graduated fermion-mass texture cluster in dependency order; Waves 5–6 = neutrino + Stage-2 cohort (independent).

## Cross-wave dependency graph

```
W1 (cosmology: independent of all)            W5 (neutrino: independent)
W2 (texture) ──hard──> W3 (freeze-in/envelope: consumes |w| seed [SOFT] + within-W3 S₀ chain)
   └─────────soft────> W4 item EPSLX-FOAM (needs ε_LX operator); other W4 items independent
W6 (Stage-2 cohort: independent; reviewer-exclusion constraints pinned in context file)
```

## Wave 1 — Cosmology keystone successors + register-sourced Tier-2 (4 gates)

**Theme**: a(t)/C10 Tier-1 successors + the two EVOI Tier-2 register-sourced observational gates.
**Owner (planner)**: `gen-physicist` (cross-reviewer wave: transit + volovik + register origins).
**Plan file**: `session-100a-plan-w1.md`

| # | Gate ID | One-line scope | Likely executor |
|:--|:--------|:---------------|:----------------|
| 1 | S100a-SF54-MAPPING | a_eff(a₂-channel)→SF54 band map re-derivation; band-membership under corrected map | transit-dynamics-theorist |
| 2 | S100a-QEQ-DRIVE | substrate-internal q_eq(H) drive (Gibbs-Duhem μ-shift / back-reaction closure); unforced slope=1 re-test | volovik-superfluid-universe-theorist |
| 3 | S100a-NS-NLO | n_s second-order slow-variation; \|Δn_s\| < 0.003 | transit-dynamics-theorist or lizzi |
| 4 | S100a-SIGMA-DM-NUCLEON | σ_DM-nucleon from Leggett-channel GGE quasiparticle coupling | landau-condensed-matter-theorist (mack lands row) |

Natural split: {1,3} (a₂-channel/CMB) vs {2,4} (q-theory/DM) on a stall.

## Wave 2 — Fermion-mass texture cluster (4 gates; panel consensus)

**Theme**: the S99 fermion-mass panel's ε_LX texture computes — envelope + off-diagonal w + two independent routes.
**Owner (planner)**: `baptista-spacetime-analyst` (panel consensus lead is baptista's compute; 5-synthesis convergence).
**Plan file**: `session-100a-plan-w2.md`

| # | Gate ID | One-line scope | Likely executor |
|:--|:--------|:---------------|:----------------|
| 5 | S100a-DUAL-Z3-PHI-POINTS | **RUN FIRST** — closed-form 3×3 Ω^b_g at Z₃ φ-points; c(φ)={1/9,1/3,1/3}; quark φ-independence | baptista-spacetime-analyst |
| 6 | S100a-YUKAWA-OVERLAP-OFFDIAG | **CONSENSUS LEAD** — per-sector \|s(h)\|² overlap + t1↔t2 off-diagonal w at L_max=12, τ_fold | baptista-spacetime-analyst |
| 7 | S100a-CASIMIR-WIDENING | 9/5=1.800 widening from the ACTUAL weighted integral; 1.800/1.333/3.0 discriminator | kaluza-klein-theorist |
| 8 | S100a-CONNES-DISTANCE-LADDER | Connes d_i on the multiplicity bundle; mass=e^{−d_i/ℓ}; independent route to the same envelope | connes-ncg-theorist |

Within-wave order: 5 → 6 → {7, 8}. Natural split: {5,6} vs {7,8}.

## Wave 3 — Freeze-in / envelope dynamics (3 gates; SOFT-after W2)

**Theme**: transit freeze-in over-constrained predictor + the two-route envelope over-determination.
**Owner (planner)**: `transit-dynamics-theorist`.
**Plan file**: `session-100a-plan-w3.md`

| # | Gate ID | One-line scope | Likely executor |
|:--|:--------|:---------------|:----------------|
| 9 | S100a-FREEZEIN-OVERCONSTRAINED | fit {S₀,\|w\|,arg w} → predict 6 quark ratios + CKM + J_CP (3 inputs → ~12 predictions) | transit-dynamics-theorist |
| 10 | S100a-ENVELOPE-OVERDETERMINE | greybody κ_SONIC=0.7048 M_KK vs transit S₀ — exponent derived twice | hawking-theorist |
| 11 | S100a-S0-THRESHOLD-JOINT | is S₀ = (ε_LX-split)/(horizon κ) a KK-threshold quantity (joint magnitude+slope closure)? | phonon-first-cosmologist |

Within-wave order: 9 → {10, 11}. SOFT cross-wave: 9 consumes the W2 |w| as cross-check seed (fit is PDG-self-contained — planner pre-registers the no-W2 branch).

## Wave 4 — Scale / functional sensitivity + foam + spinor factor (4 gates)

**Theme**: the functional-dependence characterization of the SCALE (vs the functional-independent ratios) + foam-survival + the Q27 spinor factor.
**Owner (planner)**: `lizzi-spectral-functional-theorist`.
**Plan file**: `session-100a-plan-w4.md`

| # | Gate ID | One-line scope | Likely executor |
|:--|:--------|:---------------|:----------------|
| 12 | S100a-M0-FUNCTIONAL-SENSITIVITY | M₀^{sector}/m_H under zeta vs cutoff action; INFO-by-design; ratios must be bit-identical | lizzi-spectral-functional-theorist |
| 13 | S100a-M0-MH-INHERITANCE | does M₀ inherit the m_H 5–7% residual; report-only provenance trace | mack-cosmic-bridge |
| 14 | S100a-EPSLX-FOAM-SURVIVAL | [H_foam, ε_LX] commutator + N-scaling; topological-vs-geometric dichotomy (soft-after W2) | quantum-foam-theorist |
| 15 | S100a-H0-SPINOR-FACTOR | derive M_Pl,eff/M_Pl,unred = 3.92 ≈ √16 from the d_spec=8 spinor normalization (atlas-08 Q27) | kaluza-klein-theorist |

Natural split: {12,13} (scale) vs {14,15} (foam/spinor).

## Wave 5 — Neutrino sector (2 gates)

**Theme**: zero-free-parameter Σm_ν firming + the D5 0νββ Majorana-vs-Dirac compute leg.
**Owner (planner)**: `neutrino-detection-specialist`.
**Plan file**: `session-100a-plan-w5.md`

| # | Gate ID | One-line scope | Likely executor |
|:--|:--------|:---------------|:----------------|
| 16 | S100a-MD-NORMALIZATION | substrate-pin the bottom-triple→Y_i map; re-gate Σm_ν zero-free-parameter | neutrino-detection-specialist |
| 17 | S100a-D5-0NUBB-MAJORANA | m_ββ from the KO-dim-6 Pfaffian Majorana texture vs KamLAND-Zen/LEGEND | neutrino-detection-specialist (dirac cross-axis; mack lands row) |

## Wave 6 — Stage-2 verification cohort (2 gates)

**Theme**: joint-theorem Stage-2 promotions from the ledger §C ready-to-execute queue, under the S99 E1 reviewer-exclusion lesson.
**Owner (planner)**: `gen-physicist` (procedural cross-reviewer wave).
**Plan file**: `session-100a-plan-w6.md`

| # | Gate ID | One-line scope | Reviewer constraints (MANDATORY; from registry authorship lines) |
|:--|:--------|:---------------|:----------------------------------------------------------------|
| 18 | S100a-VIIW3LAB-STAGE2-VERIFY | §VII.W-3.LAB cocycle-ratio χ-inheritance bridge → Stage-2 PASS-AND | EXCLUDED: volovik, connes, mack (Stage-0 authors). Eligible: vdd/lizzi (axis-A spectral) + landau (axis-B substrate/BdG) |
| 19 | S100a-VIIAM-STAGE2-VERIFY | §VII.AM Universal Lock Condition → THREE-axis Stage-2 PASS-AND (atlas-09 retraction-route on clause FAIL) | EXCLUDED: hawking, transit-dynamics, connes (Stage-0 authors). Eligible: lizzi (spectral-functional) + volovik/quantum-acoustics (dynamics) + schwarzschild-penrose (semiclassical-gravity) |

## Standing gaps (recorded, NOT planned — leverage ≠ tractability)

K_pivot/C2 mapping (atlas-04; largest observational gap) · τ_fold relaxation (Tier-2 #4) · CF21 TD/LI H̃ (workshop-class) · A_s floor (permanent wall) · W1-1 frame-covariance Q1 seed + Q44 Sagan re-anchor (→ `/rclab-investigate`).
