# Path B RQ-1 + RQ-3 Combined — Full-Cycle Substrate-Excitation Simulator

## Origin

Combined plan derived from `path-b-rq1-inner-fluctuation-simulator.md` and
`path-b-rq3-phase-transition-simulator.md`, both of which derive from the Path B D2
workshop closure (`path-b-d2-workshop.md`, 2026-04-27). The two original plans
remain on disk as reference; this combined plan **supersedes them as the primary
planning document** for the full-cycle substrate-excitation simulator. RQ-2 (CC dilaton
Λ-running) sits separately and is not folded in.

The combined plan exists because RQ-1 and RQ-3 are genuinely complementary, not
competing: RQ-1 simulates the dynamics of excitations on each side of the fold; RQ-3
simulates the impulsive transit between them. Sequenced together, they produce a single
end-to-end simulator from cosmogenesis (cold start at τ=0) through equilibrium post-fold
physics (CMB-relevant observables). All three workshop reviewers (Connes, spectral-
geometer, Volovik) supported both RQ-1 and RQ-3; the combined architecture inherits
their licenses jointly.

## Goal

A four-phase simulator that:

1. **Initializes** at the cold-big-bang vacuum (τ=0, A=0, S=0 plus quantum fluctuations)
2. **Relaxes** the substrate state quasi-statically toward `τ_fold = 0.190`, simulating
   the gauge + Higgs + KK excitation dynamics on each evolving spectral triple along
   the way (RQ-1 inner fluctuations, applied at successive τ values approaching the fold)
3. **Transits** through the fold via Bogoliubov scattering matching (RQ-3 impulsive
   boundary), connecting pre-fold mode amplitudes to post-fold mode amplitudes
4. **Equilibrates** post-fold via inner fluctuations on the fixed `D_K(τ_fold)`
   (RQ-1 main case), producing the GGE-relic occupation numbers and observable
   power spectra

The output is a self-contained simulator whose verdict-line set covers the full
framework cycle from cosmogenesis through CMB-relevant observables, with each phase
gating the next via pre-registered thresholds.

## Architecture sketch

| Phase | State variable | Evolution rule | Inner loop |
|:------|:---------------|:---------------|:-----------|
| **P1: Cold start** | `(A=0, S=0)` plus vacuum two-point fluctuations on `D_K(τ=0)` | None — initial condition | One-time spectral-mode sampling on `D_K(τ=0)` |
| **P2: Pre-fold relaxation** | `(A_μ, S, KK amplitudes)` on `D_K(τ_pre)` for `τ_pre ∈ {0.05, 0.10, 0.15, ..., 0.18}` | YM+Higgs eom under inner fluctuations (CC 0605011); quasi-static τ-slow-roll | Per-τ static `D_K` cache + per-step gauge/Higgs symplectic Verlet |
| **P3: Fold transit** | Pre-fold mode amplitudes `(α^pre, β^pre)`; post-fold amplitudes `(α^post, β^post)` | Bogoliubov scattering matrix `B`: `(α^post, β^post)^T = B · (α^pre, β^pre)^T`; matching prescription pinned by `s85_w6_acoustic_white_hole_formal.py` canonical | Single-mode Bogoliubov coefficient eval per mode |
| **P4: Post-fold equilibrium** | `(A_μ, S, KK amplitudes)` on `D_K(τ_fold)` initialized from P3 output | YM+Higgs eom under inner fluctuations on the fixed `D_K(τ_fold)` | Static `D_K(τ_fold)` cache (precomputed once) + symplectic Verlet |

**Observables emitted** at each phase boundary: P1 → vacuum spectral content;
P2 → pre-fold gauge boson masses, Higgs profile, KK frequencies along the relaxation
trajectory; P3 → Mach number, Bogoliubov coefficients per mode, transit kinematics;
P4 → equilibrium gauge masses, KK tower spectrum, GGE occupation numbers, post-fold
acoustic interference pattern, `n_s`, `n_eff`, integrability-charge drift.

## Pre-registered gates (six gates, sequential dependency)

The gates fire in physical order. Each gate's PASS unblocks the next phase's
verdict-line emission; FAIL surfaces a structural problem at the indicated phase
without invalidating prior gates.

**Combined-G1 (P3 kinematic) — Mach-13.75 transit kinematics.** The supersonic transit
profile (per `project_substrate-not-c-limited.md` + `s85_w6_acoustic_white_hole_formal.py`)
must reproduce canonical Mach number 13.75 ± 5%. Inherits from RQ3-G3. Gates the
kinematic match independently of dynamics. FAIL means pre-fold and post-fold sound
speeds + transit velocity are internally inconsistent.

**Combined-G2 (P3 Bogoliubov) — `n_eff` from GGE occupation numbers.** Bogoliubov-matched
post-transit GGE occupation numbers must reproduce the framework's canonical `n_eff`
within 2%. Inherits from RQ3-G1. Gates the dynamic transit calculation against existing
`s37`/`s38` predictions. FAIL is informative either way.

**Combined-G3 (P4 static equilibrium) — gauge / Higgs / running-coupling recovery.** At
P4 equilibrium (after relaxation from the P3 hand-off), inferred values of
`(m_H, m_W, m_Z, α_s(M_Z))` must match canonical constants within 5%. Inherits from
RQ1-G1 minus `n_s` (which becomes Combined-G6). Gates the dynamical layer's
faithfulness to the spectral side. FAIL surfaces simulator/static disagreement.

**Combined-G4 (P4 KK tower) — KK frequency spectrum.** Fundamental + first KK frequencies,
plus ratios to higher KK modes, must match canonical `M_KK = 7.43×10¹⁶ GeV` and the
structural ratios within 2%. Inherits from RQ1-G2. Tests inner-fluctuation construction
beyond the zero-mode sector.

**Combined-G5 (P4 GGE permanence) — integrability-charge conservation.** Post-quench
relaxation in P4 must show NO thermalization on simulator timescales: integrability
charges (BCS+Leggett locally-conserved quantities) conserved within 10⁻³ relative drift
over `~10³` characteristic times. Inherits from RQ1-G3 — the discriminating gate.
**FAIL would surface a contradiction between simulator dynamics and S38 GGE-permanence
theorem, or expose finite-mode-truncation breakdown.**

**Combined-G6 (P4 power spectrum) — `n_s = 0.9561` from post-fold acoustic interference.**
Post-fold acoustic interference pattern, computed from GGE relic occupations + Bogoliubov
phases (joint product of P3 + P4), must reproduce `n_s = 0.9561` within tolerance of
0.005 (0.5% — tight gate appropriate for canonical precision; 1% acceptable as fallback).
Inherits from RQ3-G2. **This is the simulator's most observationally-relevant output
and the one most directly checked against external data (Planck CMB).**

Sequential structure: G1 → G2 → G3 → G4 → G5 → G6. Each gate's failure mode points to a
specific simulator component; passing G1-G6 in sequence delivers a verified end-to-end
substrate-excitation cycle.

## Research questions (open) — combined and deduplicated

1. **Time-discretization on the noncommutative SU(3) fiber.** [RQ-1 #1] Mode-truncation
   using static D_K eigenmodes is the natural fit, but the truncation-error vs.
   mode-count tradeoff is uncharacterized. Affects P2 and P4.

2. **Initial-condition class for cold start.** [RQ-1 #2 + RQ-3 #2 merged] The pre-fold
   vacuum specification feeds P1 directly AND determines the input to the P3 matching.
   What's the right characterization of vacuum two-point functions on the noncommutative
   SU(3) fiber? Volovik #25 cold-start picture and S58 partition give the macroscopic
   equation-of-state (`w_0 = -0.842`); microscopic mode amplitudes need separate spec.

3. **Matching prescription at the τ_fold boundary.** [RQ-3 #1] Multiple junction-condition
   alternatives (Israel, Andreev, Painlevé-Gullstrand). Pre-register
   `s85_w6_acoustic_white_hole_formal.py`'s prescription as canonical; treat alternatives
   as variants whose disagreement with the canonical gates is informative. Affects P3
   and propagates to G2, G6.

4. **Mapping P4 simulator-output to canonical constants.** [RQ-1 #3] The framework's
   canonical `m_H` etc. are derived from spectral moments of `D_K(τ_fold)` directly.
   Does P4's inner-fluctuation evolution reproduce these from time-resolved dynamics, or
   are they purely static-spectral results that the simulator merely re-confirms? The
   answer determines whether G3 is non-trivial or tautological.

5. **GGE-permanence on truncated mode counts.** [RQ-1 #4] S38's proof assumes full
   integrability; the simulator runs on truncated mode count. At what mode-count
   threshold does approximate integrability survive? Affects G5 directly. Worth
   numerical study before G5 is interpreted.

6. **Post-fold evolution timescale.** [RQ-3 #3] Over what timescale should G2 and G6
   be evaluated? The natural choice is Mack-bridge-relevant (CMB freeze-out epoch),
   but this needs framework-canonical pinning. Affects G2 and G6 evaluation timing.

7. **Phase-coupling fidelity at P2→P3 and P3→P4 hand-offs.** [NEW — combined-only] The
   joint architecture introduces hand-offs that the standalone plans don't. Specifically:
   (a) P2 relaxes through a sequence of `D_K(τ_pre)` slices; the final pre-fold state
   feeds P3's Bogoliubov input. The "pre-fold ground state" must be defined consistently
   between the dynamic P2 endpoint and the static P3 input. (b) P3 outputs Bogoliubov
   amplitudes that initialize P4's gauge/Higgs phase space; the translation from
   mode-amplitude language to field-configuration language must be specified. Both
   hand-offs are research-level decisions that don't exist in the standalone plans.

## Development tasks (combined timeline)

| Task | Status | Effort | Phase |
|:-----|:-------|:------|:-----|
| Multi-τ static D_K caches (`τ ∈ {0.00, 0.05, 0.10, ..., 0.18, 0.190, 0.20}`) + spectral-mode basis exporters | Existing infra; needs per-τ persistence | ~2 days | P1, P2, P3, P4 |
| YM+Higgs eom solver in torch on emergent 4D × SU(3) phase space | New | ~5-7 days | P2, P4 |
| Symplectic integrator with energy/charge monitoring | New (standard physics) | ~2-3 days | P2, P4 |
| Quasi-static τ-slow-roll driver (P2 phase loop over τ values) | New | ~2 days | P2 |
| Bogoliubov scattering matrix `B` calculator + matching prescription enforcer | Partial (`s52_bogoliubov_amp.npz` exists) | ~3-4 days | P3 |
| Mach-number profile extractor | Existing (`s85_w6_acoustic_white_hole_formal.py`) | ~1 day | P3 |
| GGE integrability-charge tracker | New | ~2-3 days | P4 |
| GGE occupation extractor + `n_eff` aggregator | Partial | ~1-2 days | P3, P4 |
| Post-fold acoustic-interference → `n_s` mapper | Partial | ~2-3 days | P4 |
| Observable extractors (gauge masses, Higgs profile, KK frequencies) | Partial | ~2-3 days | P2, P4 |
| Phase-coupling hand-off layer (P2→P3, P3→P4) | New (research question #7) | ~3-4 days | between phases |
| Quench-and-relax driver script | New | ~1-2 days | P4 |
| Pre-registered gates G1-G6 implementation + verdict-line emission | New | ~3-4 days | all phases |

**Total estimated effort**: 4-6 dev-weeks for working prototype + first pass at all six
gates. ~2-3 months including iteration on whichever gates fail first time. The
combined-only items (multi-τ caches, P2 driver, phase-coupling hand-off) add ~1-1.5
dev-weeks beyond the simple union of RQ-1 + RQ-3 effort.

## Effort + risk (combined)

**Risk 1 — Static / dynamical disagreement at P4 equilibrium (probability moderate).** [from
RQ-1 Risk 1] If G3 fails, triage by comparing per-mode contributions in static vs.
dynamical settings.

**Risk 2 — KK tower mode-count truncation artifacts (probability moderate).** [from RQ-1
Risk 2] Mitigation: convergence test L_max=8 vs. L_max=10 for KK observables. Affects
G4 directly.

**Risk 3 — GGE-permanence gate too strong (probability low-moderate).** [from RQ-1 Risk 3]
Mitigation: pre-register 10⁻³ relative-drift threshold; treat smaller drift as confirming
GGE-permanence, larger drift as informative.

**Risk 4 — NCG dynamics mathematical infrastructure gaps (probability moderate).** [from
RQ-1 Risk 4] Specific implementation details of YM+Higgs eom on noncommutative manifold
require workshops with `connes-ncg-theorist`. Budget 1-2 mid-stream workshops.

**Risk 5 — Re-skinning of existing infrastructure for P3 (probability moderate-high).**
[from RQ-3 Risk 1] P3 overlaps with S37/S38/S52/S85 work. The combined architecture
mitigates this naturally because P3 must hand off to P4 in the integrated form, which
existing scattered work does not — the integration itself adds value beyond re-skinning.

**Risk 6 — Matching-prescription ambiguity (probability moderate).** [from RQ-3 Risk 2]
Pre-register canonical from `s85_w6_acoustic_white_hole_formal.py`; alternative
prescriptions become variants that surface in G2/G6 disagreements.

**Risk 7 — Pre-fold vacuum specification gaps (probability moderate).** [from RQ-3 Risk 3]
Workshop with `transit-dynamics-theorist` + `hawking-theorist` + `volovik-superfluid-
universe-theorist` to scope; affects RQ #2 directly.

**Risk 8 — `n_s` gate too tight (probability low-moderate).** [from RQ-3 Risk 4]
Pre-register 1% with 0.5% as stretch; report both.

**Risk 9 — Phase-coupling hand-off fidelity (probability moderate, COMBINED-ONLY).** The
P2→P3 and P3→P4 hand-offs introduce two new translation layers that don't exist in
standalone RQ-1 or RQ-3. If the hand-offs lose physical content, the integrated
simulator could pass each phase's gates individually while failing at the seam.
Mitigation: phase-boundary diagnostics (energy budget conservation across hand-off,
mode-occupation continuity check, integrability-charge transfer audit) added as
non-gating diagnostics during development.

## Dependencies (combined)

- **Static infrastructure**: `computations/` D_K caches at multiple τ values
  (0.00, 0.05, ..., 0.20), spectral-mode basis exporters per τ.
- **Existing scripts**: `s85_w6_acoustic_white_hole_formal.py`, `s52_bogoliubov_amp.npz`,
  S37/S38 GGE-relic outputs, `s58_volovik_partition.py` analog, S77 monotonicity result.
- **Framework canonicals**:
  - From RQ-1: `m_H = 131.8 GeV`, `M_KK = 7.43×10¹⁶ GeV`, `m_W`, `m_Z`, `α_s(M_Z)`.
  - From RQ-3: `n_eff` (canonical), `n_s = 0.9561`, Mach-13.75, `w_0 = -0.842` (S86-migrated).
- **Existing closures**: S38 GGE-permanence (input to G5), S77 monotonicity (cross-check
  on P2 quasi-static relaxation).
- **Other RQs**: RQ-2 (CC dilaton Λ-running) is independent. RQ-2 could in principle be
  layered on top of the combined simulator as a Λ-running modifier, but that's a future
  extension, not a baseline dependency.

## Recommended next-action

Assuming the combined plan is approved, the recommended sequence is:

**Step 0 (workshop, ~2 days)**: combined-scope pre-implementation workshop with
`connes-ncg-theorist` + `spectral-geometer` + `transit-dynamics-theorist` + `volovik-
superfluid-universe-theorist` to close research questions #1 (NC fiber discretization),
#2 (cold-start vacuum), #3 (matching prescription), #7 (phase-coupling hand-off
fidelity). Output: an architecture spec freeze document that the implementation phase
can build against without further theory decisions.

**Step 1 (infrastructure, ~1 dev-week)**: multi-τ static D_K cache + spectral-mode
basis exporters + symplectic integrator skeleton. This is reusable infrastructure
that survives even if the combined simulator is later restructured.

**Step 2 (P3 first, ~1.5 dev-weeks)**: implement P3 (Bogoliubov matching) and gates
G1, G2 first. P3 is the smallest standalone unit and the one with the most existing
infrastructure overlap. Passing G1, G2 validates the transit-physics layer
independently of P2 / P4.

**Step 3 (P4 second, ~1.5-2 dev-weeks)**: implement P4 (post-fold inner-fluctuation
equilibrium) initialized from a pre-pinned post-fold state (skipping P3's hand-off
for development). Implement and run gates G3, G4. Then connect P3 output → P4
initialization and run G3, G4 against the integrated hand-off (Risk 9 surfaces here).

**Step 4 (G5 + P2, ~1-1.5 dev-weeks)**: implement P2 (pre-fold quasi-static relaxation)
and G5 (GGE-permanence verification). G5's evaluation needs sufficient post-fold
simulation time, so it sits naturally after P4 is stable.

**Step 5 (G6, ~3-4 days)**: post-fold acoustic interference → `n_s` mapping. Final gate.

**Step 6 (mid-stream workshop budget, ~2 days)**: 1-2 mid-implementation workshops
with `connes-ncg-theorist` to resolve any NCG-specific implementation questions
that arise (Risk 4).

**Total**: ~4-6 dev-weeks excluding workshops; ~5-7 weeks including. Six gates emit
six verdict lines in `computations/sNN_gate_verdicts.txt` per session-naming
convention.

The Connes-Landi NC two-torus toy from Round 2 Item 4 (~2 weeks) remains an OPTIONAL
infrastructure-validation pre-step. It validates the GPU eigenvalue inner loop +
spectral-mode basis manipulation in a setting with analytic ground truth. Recommended
if there's any hesitation on the GPU inner-loop scaling or torch-eigh convergence at
L_max=10; skip if confident in the existing infrastructure.

## Combined plan vs. standalone RQ-1 / RQ-3 plans

The combined plan is **not** a strict superset of effort-summed standalone plans. The
overlap savings come from: (a) shared static D_K cache infrastructure (one task, not
two), (b) shared symplectic integrator (one task, not two), (c) shared observable
extractors (one set, not two). The combined plan's added cost (vs. simple effort sum)
comes from: (a) multi-τ caches for P2's quasi-static relaxation, (b) phase-coupling
hand-off layer, (c) P2 driver script.

| Path | Effort | Gates emitted | Coverage |
|:-----|:-------|:--------------|:---------|
| RQ-1 alone | 3-4 dev-weeks | 3 (RQ1-G1, G2, G3) | Equilibrium physics on `D_K(τ_fold)` |
| RQ-3 alone | 2-3 dev-weeks | 3 (RQ3-G1, G2, G3) | Transit physics across `τ_fold` |
| Combined | 4-6 dev-weeks | 6 (Combined-G1 through G6) | Full cycle: cosmogenesis → equilibrium |

The combined plan is **the right unit** for the framework's dynamical-side ↔ spectral-side
loop closure: it produces the end-to-end substrate-excitation cycle from cold start to
CMB observables in one self-consistent simulator, rather than two independently-validated
fragments that the framework would have to integrate later anyway.
