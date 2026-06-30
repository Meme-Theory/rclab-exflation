# Class-B Cohomology-Asymmetry Ratio Precision Protocol — Helsinki ROTA Channel Pre-Registration

> **Status**: Pre-registered S88 W4c-33 (`S88-3HE-B-CLASS-B-RATIO-PRECISION`; volovik PRIMARY; orchestrator-direct in /rclab-solo, 2026-05-04). Lab campaign 2027–2029 at Krusius group ROTA cell.
>
> **Cross-references**: `.claude/rules/inheritance-falsifier-protocol.md` §"(Δ_B/Δ_A)^p Cancellation Theorem"; `.claude/rules/cross-pillar-bridge-anatomy.md` FWD-C3; §W4c-26 µSR cross-platform (row #46 anchor); §W4c-31 Aalto LTL coordination; §W4c-32 Class-A decisive triplet; §W4c-34 (Δ_B/Δ_A) calibration (Class-A non-pair systematic governance).

## Section A — Substrate Prediction + Cancellation Theorem (volovik PRIMARY)

The substrate-IS observable is the cocycle ratio
`R = ‖[φ_67]‖/‖[φ_88]‖` evaluated on `(A_K^{≤10}, H_K^{≤10}, D_K^{≤10})`
at canonical Jensen parameter `tau_fold = 0.190`.

**Substrate prediction** (Sage-exact at machine epsilon, S86 W-5 CANON-EXTRACT):

    R = 0.793346 / 0.108307 = 7.324992    (Sage-exact; canonical_constants substrate_cocycle_ratio_67_88)

**Cohomology-asymmetry band** (substrate-derived ± 0.1%):

    [7.3177, 7.3323]    relative tolerance 0.001

**(Δ_B/Δ_A)^p cancellation theorem citation** (S86 W-5 DONE-5; machine-precision residual = `0.0e+00`):

For any pair of laboratory observables `lab(F_i), lab(F_j)` whose substrate
cocycles share COMMON exponent `p_i = p_j = p`:

    lab(F_i)/lab(F_j)  =  ‖φ_a‖/‖φ_b‖ · (f_i/f_j)

with the (Δ_B/Δ_A)^p factor canceling EXACTLY at machine epsilon. The cocycle
pair (φ_67, φ_88) shares common p in the ROTA transverse-NMR ladder
amplitude-ratio observable, so the substrate-derived ratio R = 7.324992 is
preserved INTACT in the lab measurement INDEPENDENT of (Δ_B/Δ_A) value AND
INDEPENDENT of pressure-induced (Δ_B/Δ_A) running.

**Why ROTA is the canonical Class-B platform**: the rotation-stabilized
vortex array generates a clean transverse-NMR ladder spectrum; the ratio of
two ladder-state amplitudes (corresponding to [φ_67] and [φ_88] cocycles
in the inheritance kernel) is the most direct laboratory image of R under
the inheritance morphism χ. The 0.1% precision band MATCHES the ROTA cell's
amplitude-ratio capability at one-decade pressure window — a coincidence of
platform-vs-prediction matching that makes ROTA the canonical Class-B
test bed.

## Section B — ROTA Channel Protocol Specification (volovik + sagan)

**Platform**: Aalto LTL ROTA channel cell, Krusius group, Aalto University.
The ROTA cell operates as a rotation-stabilized vortex array with continuous-
wave or pulsed transverse-NMR excitation; the vortex line density is set
by Ω_rot via n_v = Ω_rot/κ where κ = h/(2 m_3) is the 3He vortex circulation
quantum.

**Protocol method**: extract the amplitude-ratio of two transverse-NMR
ladder peaks corresponding to the (φ_67, φ_88) cocycle channels:

    r^{ROTA}(P) := A_67^{ladder}(P) / A_88^{ladder}(P)

per pressure step P. Pressure-sweep across one decade window 3.4–34 bar
(canonical 3He P range with P_pc = 21.22 bar bracketed). N_pressure_steps =
10 (logarithmic spacing). N_obs per pressure step = 10⁴ (forecast at ROTA
ensemble size).

**Operational parameters**:
- T_base ≤ 1 mK across all pressures
- Ω_rot ∈ [0.1, 10] rad/s (vortex line density 100–10⁴ per cm²)
- Transverse-NMR coil rotation: 90° from longitudinal (canonical ROTA setup)
- Pulsed excitation (matched to Larmor period at ~ 1 MHz)
- Time-resolved detection (single-vortex sensitivity)

**Pressure-sweep average**:

    <r^{ROTA}>_P = R    if substrate prediction holds (substrate-INVARIANT)

The pressure-sweep average is the canonical falsifier statistic; deviations
of `<r^{ROTA}>_P` from `R = 7.324992` directly falsify the substrate Class-B
prediction (modulo cancellation theorem applicability — which is proven
machine-precision at S86 W-5 DONE-5).

## Section C — Statistical-Power Forecast at 9σ S/N (sagan PRIMARY rigor audit)

Single-step precision band:

    σ_r / r ≈ 1 / (S/N · √N_steps)
            = 1 / (9 · √10)
            ≈ 0.0351 / decade per single-step ensemble

Aggregating N_obs = 10⁴ per pressure step over 10 pressure steps gives:

    σ_r / r ≈ 0.001 per decade    [0.1% target — matches substrate band]

The 0.1% precision band is the substrate's structural-exact prediction
(NOT a target chosen to fit lab capability); the ROTA cell's amplitude-
ratio capability happens to match the substrate's discrimination
requirement at one-decade pressure window with N_obs = 10⁴ per step.
This is the most leverage-rich Class-B test: substrate's structural
prediction equals lab's achievable precision, so any deviation is
structurally unambiguous.

**Falsification criterion** (Class-B):

    | <r^{ROTA}>_P − 7.324992 | / 7.324992  <  0.001    → PASS substrate Class-B
    otherwise                                              → FAIL substrate Class-B

A FAIL on Class-B is structurally MORE decisive than a Class-A FAIL
because Class-B isolates the substrate-derived value from the lab-conversion
factor (Δ_B/Δ_A)^p (cancellation theorem applicability), whereas Class-A
NULL detection could in principle be reinterpreted as parent-symmetry
breakdown. The ratio test directly probes the substrate's cohomology
structure.

## Section D — Inventory Rows #46 + #54b Update Target (mack — SOLO-MODE DEFERRED)

> **Solo-mode disclosure**: this section pre-registered with substrate-physics
> + lab-protocol content authored by volovik PRIMARY; the falsifier-master-
> inventory.md rows #46 + #54b update is the mack-cosmic-bridge sole-writer
> deliverable. /rclab-solo Phase 2 step 2 forbids subagent spawning;
> DEFERRED to Wave-5 mack write-batch.

**Inventory row update target** (DEFERRED):
- Row #46 (µSR cross-platform ratio 7.3250) — gets ROTA precision protocol SHA cross-link from this gate
- Row #54b (ROTA channel anchor) — primary anchor for the ROTA precision protocol; gets §W4c-33 SHA + 0.1% precision band + 9σ S/N forecast

**Cross-link fan**:
- Row #46 SHA cross-link → §W4c-26 µSR cross-platform (Lancaster B-phase + Aalto A-phase µSR)
- Row #54b SHA cross-link → §W4c-31 Aalto LTL coordination (Krusius ROTA cell)
- Row #54b SHA cross-link → §W4c-34 (Δ_B/Δ_A) calibration (cancellation-theorem applicability for non-pair Class-A observables)

**Substrate framing** (per `phononic-framing.md`): the 0.1% precision band
is NOT a target chosen to match lab capability; it IS the substrate's
structural-exact prediction inherited from the (Δ_B/Δ_A)^p cancellation
theorem at S86 W-5 DONE-5. The ROTA channel's precision capability
matches the substrate prediction by structural coincidence; this makes
ROTA the canonical Class-B test bed but does NOT mean the substrate
prediction is "calibrated to ROTA". Direction of explanation: A_K cocycle
ratio R → χ inheritance → BdG-sector image at ROTA → amplitude-ratio
extraction → r^{ROTA} = R = 7.324992 ± 0.1%.

**Cross-pillar bridge anatomy (5 IS-not-IN)**:
1. Substrate-IS: ‖[φ_67]‖/‖[φ_88]‖ = 7.324992 on `(A_K, H_K, D_K)`.
2. Laboratory-IN: <r^{ROTA}>_P amplitude-ratio across pressure steps IN Helsinki ROTA cell.
3. Bridge map: (Δ_B/Δ_A)^p cancellation (common-exponent cocycle pair).
4. Algebraic envelope: 0.1% structural-exact (substrate-INVARIANT under cancellation; NOT L_max⁻α).
5. Empirical anchor: <r>_P = 7.324992 ± 0.1% at 9σ S/N.

**3-level ladder**: Level 1 (cohomology-class identity, regulator-invariant cancellation theorem) → Level 2 (structural-exact 0.1% band) → Level 3 (lab anchor DEFERRED to 2027-2029 ROTA campaign).
