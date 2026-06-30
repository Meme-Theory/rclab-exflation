# Session 79 Workshop P2-B: mack × transit

**Date**: 2026-04-16
**Format**: Iterative 2-agent workshop (2 rounds, 4 turns)
**Agents**: mack (mack-cosmic-bridge) — W3-E owner; observational constraints (PBH, FIRAS, LIGO/Virgo); user's observational priorities proxy. transit (transit-dynamics-theorist) — W1-E owner; pre-fold Bogoliubov; parametric amplification through the fold.

**Source Documents**:
- `sessions/archive/session-78/session-78-results-workingpaper.md` §W1-E (lines 563-641) + §W3-E (lines 1634-1708)
- `sessions/archive/session-79/workshops/p1-1-s78-synthesis-completion.md` (P1-1 emergence E1: fold |β|²~10⁴ unified root cause; E4: F_amp and S_IC both amplify from same |β|²)
- `sessions/session-plan/session-78-plan-scrubbed.md` §W1-E and §W3-E
- `computations/s78_pre_fold_vacuum.py` and `.npz` (S_IC computation)
- `computations/s78_pbh_constraint.py` and `.npz` (PBH/FIRAS evaluation)
- `computations/s77_transition_scale_pbh.npz` (P_ζ at k_trans)
- `sessions/archive/session-79/s79-phase-plan.md`

**Focus Topics** (5 sections — labeled M1-M5 for mack; T1-T5 for transit):

1. **The wrong-sign diagnosis** — W1-E canonical S_IC(k_pivot) = 1.636×10⁵ (spectral-stationarity IC principle). This was supposed to be a SUPPRESSION channel closing the 9.5 OOM A_s overproduction. Instead it is an AMPLIFICATION channel. W3-E confirms the same pattern at k_trans (S_IC~2.78×10³ extrapolated) and 4.4 OOM over the PBH/FIRAS bound. Is there ANY IC principle under which S_IC < 1 at the relevant scales?
2. **The observational damage** — PBH mass function at k_trans = 3.36e-3 Mpc⁻¹ places the modes at ~10²⁰ M_sun (ultra-supermassive). FIRAS μ-distortion over k ∈ [1, 10⁴] Mpc⁻¹ under physical S_IC-cap at 1 still shows 220× overshoot. Even with Branch-C backreaction (F_amp^{sc} ≤ 48), the product P_ζ × S_IC exceeds bound by +2.24 OOM. What observational channels falsify the framework if the pre-fold vacuum is truly an amplifier?
3. **The P1-1 E1 structural read** — fold |β|²~10⁴ is the unified root cause of 5 S78 failures (W1-C, W1-E, W3-E, MASTER, W1-D). This says the diabatic transit IS the origin of the wrong-sign problem. Can the fold be diabatically avoided (lower Mach number) while preserving n_s = 0.9567? Or is the n_s tilt itself a consequence of the same |β|²~10⁴?
4. **Three IC principles agreed to factor 1.13 at k_pivot** — spectral stationarity, minimum entropy, AZ topology all give S_IC ≈ 1.6–1.85 × 10⁵. This kills the "IC axiomatic gap" hope — it's not that we picked the wrong principle; all three give amplification. What does this say about the pre-fold substrate state?
5. **Cross-cutting: observational survival conditions** — for the framework to survive PBH/FIRAS, the pre-fold vacuum must be either (a) a suppressor in a principle we haven't tested, (b) a different state than |β|²~10⁴ at the specific k_trans (k-dependence), or (c) reframed as only valid for k_pivot (CMB scale) and PBH/FIRAS modes never see the parametric kick. Which survival path is physically admissible?

**Convention pins** (NON-NEGOTIABLE):
- F_amp = POWER RATIO; S_IC = |α+β|².
- 4-tuple tag on every claim.
- PBH mass function: Carr press; horizon-crossing at k_trans.
- Gate verdicts PERMANENT: W1-E (FAIL), W3-E-1 (FAIL), W3-E-2 (FAIL). Do NOT re-adjudicate.
- W1-C INCOMPUTABLE-FALLBACK-TO-BOUND stands (F_amp^{sc} ≤ 47.9).
- W1-B WARRANT-INVALID (P1-3) — if citing F_amp linearized 6858 in PBH computation, flag warrant status.
- Substrate-first framing: the fold is a reorganization of the D_K eigenvalue spectrum, NOT inflation-like amplification of primordial quantum fluctuations in pre-existing FRW spacetime.

---

## Round 1 — mack: Opening Analysis

### M1: PBH/FIRAS observational damage quantified

**Data pull (from `s78_pbh_constraint.npz`, verified against WP §W3-E lines 1634–1708)**:

| Quantity | Linearized | Branch-C SC | Bound | Status |
|:---------|:----------:|:-----------:|:-----:|:------:|
| P_ζ(k_trans) | 8.906 × 10⁻² | 6.223 × 10⁻⁴ | 10⁻² | lin FAIL by +0.95 OOM |
| S_IC(k_trans) propagated | 2.777 × 10³ | 2.777 × 10³ | (no direct cap) | wrong-sign amplification |
| P_ζ × S_IC at k_trans | 2.474 × 10² | 1.728 × 10⁰ | 10⁻² | +4.39 OOM lin / +2.24 OOM SC |
| P_ζ × S_IC at k_pivot | 1.100 × 10⁶ | 7.687 × 10³ | 10⁻² | +8.04 OOM lin / +5.89 OOM SC |
| FIRAS μ (naive k-extrapolation) | 2.334 × 10¹⁰ | — | 9 × 10⁻⁵ | +14.4 OOM |
| FIRAS μ (S_IC-capped-at-1) | 1.987 × 10⁻² | — | 9 × 10⁻⁵ | +2.35 OOM (factor 220) |
| PBH mass at k_trans (Carr press) | 2.13 × 10⁵³ g ≈ 1.07 × 10²⁰ M_sun | — | — | ultra-supermassive regime |

4-tuple tag on every row: (f*, POWER-RATIO, |α+β|², L_max=10, IC=spectral-stationarity). W1-B warrant-invalid flag applies to F_amp linearized 6858 inputs to P_ζ; the SC column uses W1-C analytical bound F_amp^{sc} ≤ 47.9 which is warrant-clean. The FIRAS capped case uses the physically-motivated S_IC→1 subhorizon asymptote (W3-E Mode (b)) which does NOT depend on F_amp^{lin} at all — the overshoot is driven by raw P_ζ alone.

**Substrate-framing translation**: in the framework, PBHs at k_trans are not gravitational collapses of density perturbations in a pre-existing FRW background; they are LOCAL CONDENSATIONS of the GGE relic's spectral-weight density on scales k < k_fold^{acoustic}. FIRAS μ-distortion at k ∈ [1, 10⁴] Mpc⁻¹ constrains the post-reionization CMB spectrum's imprint of squeezed-state acoustic pair density integrated over this k range. Under the substrate picture, the bound P_ζ × S_IC ≤ 10⁻² at any k where the squeezed modes overlap the CMB observation window is a direct bound on the total intensity of pair production the diabatic fold transit is allowed to deposit into the post-fold acoustic sector. The fold has deposited far too much.

**The sharp falsification claim**:

> The framework is falsified if and only if the physical S_IC(k) profile — as measured by a direct Bogoliubov computation on the full k ∈ [1, 10⁴] Mpc⁻¹ grid, with no slope-extrapolation — yields FIRAS ∫dk P_ζ(k) × S_IC(k) / k > 9 × 10⁻⁵ with k-space weight consistent with a standard μ-distortion Green's function (Chluba-Sunyaev kernel).

Stated as a numerical bound on the integrand: the framework is falsified if the FIRAS μ integral exceeds 9 × 10⁻⁵, which under the most generous physical reading (S_IC capped at unity above k_pivot — the subhorizon adiabatic asymptote) currently gives μ = 1.99 × 10⁻², a factor 221 overshoot. Equivalently, the framework survives FIRAS if and only if some combination of (i) F_amp^{sc} < 1 (SPT-reading of W1-C), (ii) S_IC(k) decaying faster than k^{-1.5} above k_pivot, or (iii) P_ζ(k) itself being suppressed at the CMB-distortion window by a factor ≥ 221 relative to the current computation, applies at every k in the FIRAS window.

**Why both naive and capped FAIL matters**: the naive k-extrapolation (slope 1.509 across 6 decades of k) is not physically supported — W1-E's CHK6 only baselined across k_pivot/3 to k_pivot, a factor-3 window. But the physical-capped reading — in which S_IC = 1 above k_pivot (genuine subhorizon adiabatic asymptote) — is the MOST generous physical reading available, and it still fails by +2.24 OOM at k_trans and by +2.35 OOM in the FIRAS μ integral. There is no intermediate reading that saves the framework under the pinned conventions. The observational damage is not a slope-extrapolation artifact.

**The most-constraining k is NOT k_trans**: under the physical S_IC-capped reading, the most-constraining k sits at k ≈ 5.6 × 10⁻² Mpc⁻¹ ≈ k_pivot itself (the transit-scale enhancement peak where F_amp(k) maximizes at 1.23 × 10⁵ per S77). The transit-scale modes — which the fold most violently squeezes — are the modes the PBH/FIRAS constraint most sharply rejects. This is NOT a high-k trans-Planckian artifact. It is a CMB-scale observational failure at the scales where the framework predicts its own signatures.

### M2: Is there any IC principle giving S_IC < 1?

**Framing**: S_IC = |α_k + β_k|² is a POWER-SPECTRUM prefactor under the pinned convention. The Bogoliubov relation |α|² − |β|² = 1 pins a constant (up to time-reversal sign), so S_IC < 1 requires α and β to partially destructively interfere — specifically, 2 Re(ᾱβ) + |β|² < 0, which means Re(ᾱβ) < −|β|²/2. For the fold's canonical |β|² ~ 4.3 × 10⁴ per mode, achieving S_IC < 1 requires a phase alignment between α and β tuned to 1 part in ~|β|² — a measure-zero coincidence unless it is enforced by a principle.

**Three IC principles tested in W1-E** (all yield amplification):

| Principle | S_IC(k_pivot) | α_k | β_k | Wronskian | Physical state |
|:----------|:-------------:|:---:|:---:|:---------:|:---------------|
| Spectral stationarity (canonical) | 1.636 × 10⁵ | (125 + 164i) × 10¹ | (179 + 103i) × 10¹ | W = −i (pure vacuum) | Adiabatic positive-freq vacuum |
| Minimum entropy | 1.854 × 10⁵ | (215 + 43i) × 10¹ | (215 − 43i) × 10¹ | W = 0 (standing wave) | Real density-matrix superposition |
| AZ-topology (Lizzi BDI) | 1.636 × 10⁵ | (179 − 103i) × 10¹ | (125 − 164i) × 10¹ | W = +i (time-reversed) | CPT-mirror negative-freq vacuum |

The three principles agree to factor 1.13 (0.054 OOM) because they all project onto the SAME α, β magnitudes — differing only in chiral phase pinning. No principle that preserves |α|² − |β|² = ±1 at |β|² ~ 4.3 × 10⁴ can give |α + β|² < 1 without an additional phase-locking condition.

**Candidate 4th principle 1 — Danielsson α-vacua (trans-Planckian initial state, hep-th/0203198)**: Danielsson's proposal is a one-parameter family of vacua labeled by a scale η_c (the trans-Planckian matching slice) at which the mode is initialized in the instantaneous Hamiltonian eigenstate. The resulting β_k depends on the RATIO H/M_new (Hubble scale / new-physics scale at η_c), and in the standard inflationary setting gives |β|² ~ (H/M_new)² ~ 10⁻⁴ to 10⁻⁶ — far smaller than the fold's |β|² ~ 10⁴. The Danielsson prescription IS a construction that gives S_IC < 1 in its natural regime. Three structural problems prevent it from applying to the substrate fold:

- **Regime mismatch**: Danielsson α-vacuum is defined in the SLOW-ROLL adiabatic inflationary regime where the mode equation has a well-defined instantaneous Hamiltonian. The fold at Mach 13.75 is DIABATIC: dt_transit = 1.13 × 10⁻³ M_KK⁻¹ gives a transit rate 13.75× faster than the local sound crossing. The instantaneous Hamiltonian at the fold is NOT well-defined over the transit timescale; there is no eigenstate to initialize into.
- **Scale hierarchy inversion**: Danielsson requires H_slow-roll < M_new. The substrate has no physical "M_new" above the KK scale because M_KK IS the UV cutoff. The Jensen-deformed D_K spectrum's top eigenvalue at L_max=10 sets M_cutoff ≈ 1 in M_KK units, and the transit pump field z''/z at the fold reaches 1.3 × 10⁻¹ in the same units. The hierarchy H_fold/M_cutoff ≈ 0.6 is NOT << 1.
- **No KMS state at the fold**: Danielsson's prescription implicitly requires thermal equilibrium at η_c (KMS condition for defining the instantaneous Hamiltonian eigenstate). The pre-fold substrate is not thermal — it is a gapless phonon bath at the van Hove fold where density of states is singular (dS/dτ = +58,673 at τ = 0.190). The framework's own phonon-first framing excludes thermal-state initialization at the fold.

Danielsson is KINEMATICALLY INADMISSIBLE for the substrate's fold. It is the canonical non-BD IC principle in the inflation literature, and its natural regime does not overlap the fold's regime.

**Candidate 4th principle 2 — Kim-Lee-Son thermal-squeezed state (arXiv:1009.5712)**: Thermal squeezing produces S_IC(k) = coth(ω_k/2T) with T the substrate temperature. For T > 0 this gives S_IC > 1 always; for T = 0 it recovers |α|² + |β|² (still ≥ 1 with equality only in vacuum). Thermal squeezing is structurally an AMPLIFIER, not a suppressor. Adding thermal noise to the substrate pre-fold state cannot save S_IC < 1; it makes the problem worse.

**Candidate 4th principle 3 — Entanglement-cooled vacuum (Maldacena-Pimentel type)**: A maximally entangled two-mode squeezed state between k and −k carries total S_IC = 2 cosh(2r) ≥ 2 where r is the squeezing parameter. The fold would correspond to r ~ ½ ln(|β|²/|α|²)⁻¹ — again amplification. Even tracing out −k to get the reduced single-k state gives S_IC ≥ 1. Entanglement does not generate destructive interference; it distributes amplitude across modes.

**Candidate 4th principle 4 — Holographic IR cutoff (BD with UV-IR slice)**: If the pre-fold mode space is cut off at k_IR ~ aH at the fold, the IR divergence in β_k is regulated but the per-mode |β|² magnitude is unchanged. This is a measure-space restriction, not a state restriction. Per-mode S_IC at k_pivot remains 1.6 × 10⁵.

**Structural conclusion on M2**: no IC principle in the standard literature gives S_IC < 1 at a scale where the parametric pump produces |β|² ~ 10⁴. The spectral-stationarity / minimum-entropy / AZ-topology triple at factor 1.13 agreement is not a coincidence of choice — it reflects the fact that these principles all agree on the α, β MAGNITUDES dictated by the mode equation's dynamics, differing only in which chiral sector of the density matrix is selected. The Bogoliubov unitarity constraint |α|² − |β|² = ±1 at |β|² >> 1 is a hard wall against single-mode S_IC < 1 regardless of chosen IC.

**The remaining space for S_IC < 1** is NOT a choice of IC principle but a choice of EFFECTIVE MODE: multi-mode cancellations (a coherent superposition of k and k' modes with destructive interference), or a non-local reorganization of the k-space measure itself. Both route through W1-C's 3PI non-Gaussian closure or a non-perturbative rearrangement of the post-fold vacuum — NOT through the pre-fold IC choice. This is transit's territory, not mine; flagging for T1/T2.

### M3: Fold as unified root — observational consequences

**The E1 claim**: P1-1 E1 (qa + gen-physicist endorsement) places the fold's |β|² ~ 10⁴ per mode as the UNIFIED ROOT CAUSE of five S78 failures — W1-C linearization breakdown (ρ_particles/ρ_bg = 2 × 10⁴), W1-E S_IC wrong-sign amplification, W3-E PBH/FIRAS wrong-sign, MASTER composed-chain +3 OOM, W1-D single-band E_cond inadequacy. Gen-physicist's GE1 sharpening splits this into two mechanism families: (a) POWER-AMPLIFICATION family (|β|² directly sets per-mode squeezing → F_amp and S_IC co-amplify), and (b) STRUCTURAL-FAILURE family (block-diagonal theorem prevents E_cond enhancement; fold is first-order not adiabatic). Both families trace to the same diabatic fold geometry.

**The observational channels sensitive to |β|²**:

| Channel | Observable | Linearized prediction | Observed value | Status |
|:--------|:-----------|:---------------------:|:--------------:|:------:|
| CMB A_s | Scalar power amplitude | 1.73 × 10⁻⁹ (S_IC=1) → 1.96 × 10⁻⁶ (S_IC=1.6e5, F_amp=48) | 2.1 × 10⁻⁹ | Form-dependent, INCOMPUTABLE |
| CMB n_s | Scalar tilt | 0.9590 (S65 BCS+1-loop) | 0.9649 ± 0.0042 | 1.4-sigma PASS |
| CMB r | Tensor-to-scalar | 0.024 (post-EIH) | < 0.036 (BK18) | PASS |
| f_NL | Bispectrum | 0.055 (W3-F S78) | < 5 (Planck) | PASS (invisible) |
| FIRAS μ | Spectral distortion | 1.99 × 10⁻² (capped) | < 9 × 10⁻⁵ | FAIL +2.35 OOM |
| PBH mass function | Compact object abundance | 2.13 × 10⁵³ g ~ 10²⁰ M_sun at k_trans | — | FAIL structural (but ultra-supermassive, no direct observational match) |
| Euclid growth f σ₈ | LSS growth | 0.793 S65 | 0.808 ± 0.020 | 0.8-sigma PASS (different mechanism) |

**The structural asymmetry**: n_s, r, f σ₈ PASS while A_s, FIRAS μ fail. Why does the same |β|² give correct SHAPES (n_s tilt, r suppression) but wrong NORMALIZATIONS (A_s, μ)? Because shape ratios are convention-invariant while amplitudes scale linearly with F_amp × S_IC in the power-ratio convention. This is the P1-1 GE1 family split: |β|²-as-normalization fails, |β|²-as-shape (spectral tilt from squeezed-mode dispersion) passes.

**Can the fold be diabatically avoided?** The diabatic character is Mach 13.75 = k_fold·c_sound·dt_transit ≈ 14. Three knobs control this:

1. **Lower dS/dτ at the fold** (adiabatic fold). Requires flattening the Jensen spectral-action gradient at τ = 0.190. But dS/dτ = +58,673 is a GEOMETRIC FACT of the Jensen-deformed D_K — it is not a parameter the framework can tune. Changing it requires a different manifold (G_2, SU(4), etc., per my S58 Option B analysis) or a different Jensen deformation. All such changes propagate through the whole eigenvalue spectrum and would un-match the S22b block-diagonal theorem, the Dynkin rank, and the 67/67 Baptista reproduction. STRUCTURAL LOCK.
2. **Slower transit** (longer dt_transit). Requires a different equation of state ε_pre for the pre-fold substrate. But ε_pre = 1.72 at n_pre ≈ 1.4 is fold-computed, not tuned. Changing it requires a different Leggett channel spectral assignment. STRUCTURAL LOCK.
3. **Shorter acoustic baseline** (raise c_sound at fold). c_Gold = 1 in M_KK units is set by the same spectral data as dS/dτ. STRUCTURAL LOCK.

The fold's Mach = 13.75 is not a tunable cosmological parameter; it is a consequence of the substrate's spectral geometry. The framework cannot retune the fold to be adiabatic without losing everything else.

**Is n_s tilt itself a consequence of |β|² ~ 10⁴?** This is the sharp observational question. Per my S65/S66 memory: n_s = 0.9590 comes from BCS occupation structure (shift +0.0031) plus one-loop correction (−0.0010), NOT from the fold Bogoliubov structure directly. But the SPECTRAL TILT of the squeezed state S_IC(k) — measured as slope 1.509 in log-log across W1-E's CHK6 baseline — IS a direct readout of |β(k)|² running. If n_s and S_IC(k) tilt share a common root in the fold's diabatic parametric kick, then the n_s PASS is not independent evidence for the framework — it is a correlated artifact of the same geometry that also breaks A_s and FIRAS.

**This is the critical open question**: is n_s = 0.9590 shape-derived (tilt of the BCS-modified PW projection, independent of |β|²) or amplitude-derived (tilt of the squeezed spectrum S_IC(k), same root as |β|²)? If shape-derived, n_s is an independent PASS and the framework retains n_s as a zero-parameter prediction. If amplitude-derived, then n_s passes ONLY because we happen to have gotten the right slope out of the same geometry that gave wrong amplitude — and the slope's free-parameter count is the same as the amplitude's.

**The cheapest observational discriminant** (requiring least new physics) is the **SPECTRAL RUNNING dn_s/d ln k** and its sign. If |β|²(k) is the common root:
- Framework predicts dn_s/d ln k = −0.038 (S66 RUNNING-NS-66 FAIL at 5.0-sigma) — a strong negative running.
- LCDM slow-roll predicts |dn_s/d ln k| < 10⁻³ (consistent with Planck's −0.005 ± 0.013).
- CMB-S4 will measure dn_s/d ln k to sigma ≈ 0.002 by 2033 — this is the DISCRIMINATOR.

The framework's predicted strong negative running at 5-sigma is NOT a free parameter; it is computed from the same BCS + spectral geometry that gives n_s. If |β|²(k) is the common root, running will come out of the fold's spectral-tilt structure and will be testable at CMB-S4 as a DIRECT READ of whether the framework's normalization problem reappears at the shape level.

**Cheapest observable test** (S79-registerable): pre-register dn_s/d ln k from a single computation of the squeezed-state power spectrum P_ζ(k) × S_IC(k) sampled at Planck scales (k ∈ [10⁻⁴, 10⁻¹] Mpc⁻¹), fit n_s(k) locally, and compute dn_s/d ln k. Compare with PDG dn_s/d ln k = −0.005 ± 0.013 (Planck 2018). If |dn_s/d ln k|_framework > 0.013 at this k range, the framework's normalization problem has propagated to the tilt. If |dn_s/d ln k|_framework < 0.013, then n_s shape is independent of the normalization failure and can be retained as a passing prediction.

This requires ZERO new physics — just a direct evaluation of the existing S_IC(k) product against existing CMB data. It costs O(hours) of compute. Priority #1 observational discriminant for S79.

### M4: Three IC principles agree at factor 1.13 — implication

**The prior framework concern**: the S77 "tossed execution" raised a "32-OOM axiomatic gap" concern — that different IC principles might give wildly different S_IC values, leaving the framework's prediction under-determined by its own axioms. This concern is now RETIRED by W1-E CHK6 and CHK5. The three principles (spectral stationarity, minimum entropy, AZ topology) agree at factor 1.133 (0.054 OOM) at k_pivot, with ordering stable under 10% perturbation of the pre-fold spectral action.

**What this factor-1.13 agreement actually means**: the three principles differ ONLY in the Wronskian sign pinning (W = −i, 0, +i) — which chiral sector of the pre-fold density matrix is selected. The α and β MAGNITUDES are identical across principles:
- |α_SS|² = |β_AZ|² + 1, |β_SS|² = |α_AZ|² − 1 (CPT mirror)
- |α_ME|² = |β_ME|² (standing-wave symmetric)
- All three give |β|² ≈ 4.3 × 10⁴ at k_pivot

The magnitudes are DICTATED BY THE MODE EQUATION ITSELF — by the pump field z''/z(η) integrated through the fold transit. No IC principle can change the magnitudes because they are forced by the dynamics, not by the initial-state choice. The principles differ only in PHASE pinning.

**The implication for the pre-fold substrate**: the fact that three structurally distinct principles (quasi-stationarity of the eigenvalue problem, entropy minimization, AZ-topology CPT symmetry) all land on the same |α|, |β| magnitudes tells us that the pre-fold substrate is in an OSCILLATORY SUBHORIZON REGIME where k²/(z''/z) = 107.6 >> 1. In this regime:
- The mode equation decouples into approximate left- and right-movers
- Each mover has a well-defined frequency ω_k ≈ c·k
- The three principles differ only in which superposition of left/right-movers is selected as the ground state
- None of them can REDUCE the Bogoliubov coefficients below what the forced dynamics produces

This is a KINEMATIC CONSTRAINT on the pre-fold state. The oscillatory subhorizon regime has a well-defined adiabatic vacuum, and S_IC is determined by the mismatch between the pre-fold adiabatic vacuum and the post-fold BD vacuum — a mismatch forced by the diabatic transit.

**What the three principles ASSUME about the pre-fold state, and why they converge**:

All three principles assume the pre-fold substrate is in a PURE STATE — a single density matrix, not a mixed ensemble. Spectral stationarity pins positive-frequency content; AZ topology pins negative-frequency content; minimum entropy pins the symmetric superposition. If the pre-fold substrate were in a MIXED STATE (thermal ensemble, GGE over pre-fold eigenstates, decohered phase-space distribution), then S_IC would not be a sharp number; it would be an expectation value ⟨S_IC⟩ over the ensemble. None of the three principles tested addresses this case.

This is the GAP in M2's "S_IC < 1 is structurally hard" claim: a pre-fold MIXED state with a specific density-matrix correlation structure COULD produce ⟨S_IC⟩ < 1 via cancellation across the ensemble. But:
- The substrate's own phonon-first framing requires the pre-fold state to be a pure GGE on the Jensen-deformed D_K eigenvalue spectrum.
- The GGE is a STATIONARY ensemble of many-body modes, not a thermal ensemble.
- Per Nazarewicz's S75 memory / framework "GGE freeze EXACT" result, the GGE is stationary with respect to the pre-fold Hamiltonian — so it projects onto the same pure-state IC as spectral stationarity.

So the three principles converge because they all correctly identify the pre-fold state as the GGE-stationary pure state on the Jensen-deformed D_K spectrum — and the GGE-stationary state in the oscillatory subhorizon regime is the positive-frequency adiabatic vacuum up to CPT phase. The axiomatic gap closes because the substrate's OWN phonon-first framing uniquely identifies the IC (up to CPT sign).

**The sharp implication**: the IC ambiguity is not where the framework has room to maneuver. The framework's own substrate picture UNIQUELY selects the pre-fold state (GGE-stationary pure), and that selection gives S_IC = 1.6 × 10⁵ amplification, not suppression. The A_s gap and the PBH/FIRAS gap both trace to the fold's dynamics, NOT to the pre-fold IC choice. M4 closes the IC-principle escape hatch permanently.

**Framework-level consequence**: the A_s-gap closure cascade in S77's plan explicitly listed "pre-fold non-BD suppression channel" as one of three axes to explore. That axis is NOW CLOSED in TWO independent directions (M2 kinematic inadmissibility of suppressor principles + M4 convergence of the three tested principles at the GGE-stationary pure state). The framework must find suppression elsewhere: f_conv via W2-D/W2-E (per S77 W3-F f_NL precedent), or backreaction via 3PI non-Gaussian closure of W1-C (not yet delivered), or reframe: the fold's |β|² ~ 10⁴ is wrong to begin with, which requires a DIFFERENT fold geometry.

### M5: Survival conditions — which is admissible?

Three survival paths were pre-registered in the shell. I evaluate each against observational admissibility and physical grounds.

**Path (a) — Untested IC principle with suppression**:

Physical grounds: WEAK. Per M2 and M4, the substrate's own phonon-first framing uniquely selects the GGE-stationary pure state as the pre-fold IC. There is no standard-literature IC principle (Danielsson α-vacuum, Kim-Lee-Son thermal squeeze, entanglement-cooled, holographic cutoff) that is both kinematically admissible at the fold's Mach 13.75 diabatic regime AND produces S_IC < 1 at |β|² ~ 10⁴. The three principles tested agree at factor 1.13 because they all correctly identify the GGE pure state up to CPT sign. Adding a fourth principle that gives a different answer would require it to override the substrate's own framing — a circular escape.

Required test: pre-register a 4th IC principle — I propose "POST-FOLD backward-evolved BD vacuum" (initialize the mode in the post-fold BD vacuum at η_end, evolve backward through the fold, use the resulting α, β magnitudes). This is not a new PRINCIPLE but a consistency check: if the fold is truly a unitary reorganization, forward-evolution from any pre-fold IC and backward-evolution from the post-fold BD vacuum must agree. Pre-register: S_IC^{backward} = S_IC^{forward} = 1.636 × 10⁵ to factor 2. If they disagree, the mode equation solver has an error; if they agree, Path (a) is formally closed.

Verdict on Path (a): **grasping-at-straws.** It requires overriding the substrate's own framing with an external IC principle that has no physical grounds in the pre-fold substrate dynamics. Not defensible.

**Path (b) — k-dependent S_IC peaking at k_pivot but capping at 1 elsewhere**:

Physical grounds: STRONG (at first reading). The deep-subhorizon asymptote k >> aH_fold implies adiabatic mode evolution: α → 1, β → 0, S_IC → 1. For k far above the transit scale, the fold's pump field z''/z is irrelevant to the mode's dynamics because the mode is oscillating too fast to notice the fold. This is the W3-E "physical cap" reading and is motivated by standard parametric-amplifier theory.

Remaining worry: the cap is at k >> k_fold ≈ 1 M_KK (the transit-scale enhancement peak). The FIRAS μ integral k ∈ [1, 10⁴] Mpc⁻¹ spans the window ABOVE k_pivot (where S_IC → 1 under the cap) but ALSO includes the transit peak (where S_IC maxes). Under the capped reading, the most-constraining k is k ≈ k_pivot itself (0.056 Mpc⁻¹ ≈ 8 × k_FIRAS,low), and the FIRAS μ still overshoots by 220× because P_ζ(k_pivot) is 6.7, and even S_IC = 1 × P_ζ = 6.7 at the pivot >> 10⁻² bound. The cap rescues the FIRAS integral from 14-OOM to 2-OOM overshoot but NOT below bound.

The cap reading also faces a structural challenge: transit will argue in T1 that if the pump field z''/z ≈ 0 outside the transit (both pre-fold and post-fold), then modes NOT crossing the transit impulse evolve freely from pre-fold to post-fold — α → 1, β → 0 rigorously. Modes that DO cross the transit experience the full diabatic kick. The boundary between "crossing" and "not crossing" is set by k vs the transit frequency scale 1/dt_transit = 885 M_KK — a very high scale. At FIRAS scales k ~ 10⁴ Mpc⁻¹ << 885 M_KK_in_Mpc, all FIRAS modes should NOT cross the transit, giving S_IC → 1 genuinely. But P_ζ at these scales is already large due to F_amp(k) running, so the bound is violated by P_ζ alone.

Required test: direct S_IC(k) computation on the full k ∈ [1, 10⁴] Mpc⁻¹ grid (no extrapolation). Cost O(hours). If S_IC(k) caps at 1 for k > k_pivot as expected, the FIRAS overshoot is driven by P_ζ alone (W1-C / F_amp); the pre-fold IC is NOT the PBH/FIRAS problem. The PBH/FIRAS problem becomes a W1-C problem exclusively.

Verdict on Path (b): **physically defensible BUT does NOT save the framework.** It correctly describes the subhorizon asymptote but does not reduce the FIRAS integrand below bound because the binding scale is k ≈ k_pivot where S_IC is NOT in the capped regime. This is the path that resolves the SHAPE of the problem but does not resolve the AMPLITUDE.

**Path (c) — Reframe: W1-E applies only at k_pivot; PBH/FIRAS modes see adiabatic evolution**:

Physical grounds: MEDIUM. This is a sharpened Path (b): instead of just capping S_IC at 1 for k > k_pivot, it asserts that the FIRAS window modes never see the parametric kick at all because they are in a different kinematic regime (trans-fold adiabatic, not transit-crossing). Under this reading, W1-E is a statement about k_pivot specifically, and the PBH/FIRAS constraint becomes a statement about raw P_ζ(k) with S_IC = 1 identically.

Under Path (c), the W3-E result becomes: P_ζ × S_IC at FIRAS scales = P_ζ alone = raw power at FIRAS window. With S77 P_ζ(k_pivot) = 6.7 linearized / 0.047 Branch-C SC, and F_amp(k) ratio scaling, the FIRAS μ integrand is determined by W1-C F_amp structure alone. If F_amp^{sc} < 1 (SPT reading), the FIRAS bound closes. If F_amp^{sc} ∈ [6.9, 48] (W1-C analytical bound band), FIRAS fails by factor ~10 to 1000.

Required test: direct S_IC(k) on FIRAS window (same as Path (b)) AND W1-C 3PI closure to determine F_amp^{sc}. Path (c) is DEPENDENT on the same two pre-registered S79 computations as Path (b); it differs only in interpretation of what W1-E said. If S_IC(k > k_pivot) = 1 by the subhorizon asymptote, Path (b) and Path (c) become OBSERVATIONALLY IDENTICAL.

Verdict on Path (c): **a reframing of Path (b), not an independent path.** The physical content is the same. The framework's survival under Path (c) requires exactly the same computation (direct S_IC(k) on full grid) and the same W1-C closure as Path (b).

**Priority-ranked admissibility**:

| Path | Physical grounds | Requires | S79 cost | Defensible |
|:-----|:-----------------|:---------|:---------|:-----------|
| (b) = (c) | Strong (standard parametric theory) | Direct S_IC(k) + W1-C 3PI closure | O(days) | YES |
| (a) | Weak (overrides substrate framing) | New IC principle with no physical grounds | O(weeks) of literature search + computation | NO |

**The single most informative S79 computation** is: direct S_IC(k) on k ∈ [1, 10⁴] Mpc⁻¹ with no slope extrapolation. This resolves Paths (b) and (c) simultaneously, quantifies the FIRAS integrand honestly, and determines whether the framework's fold-transit structure produces a P_ζ × S_IC that fits under the FIRAS bound. Pre-registration: if S_IC(k) caps at 1 for k > 3 k_pivot AND P_ζ(k) has F_amp^{sc} ≤ 1 from W1-C 3PI closure, the framework survives PBH/FIRAS. If either condition fails, the framework is falsified at CMB spectral-distortion level with cleanup paths requiring non-trivial new mechanisms.

**Honest framing**: Path (a) is grasping-at-straws. Paths (b) and (c) are the same path, physically defensible, but require W1-C to close at SPT-reading F_amp^{sc} ≤ 1 to rescue FIRAS. The framework's observational survival currently hinges on W1-C 3PI closure producing F_amp^{sc} < 1, not on any IC-principle choice.

**Substrate-framing final note**: under the substrate picture, the FIRAS bound is a constraint on the intensity of GGE relic acoustic pair production the fold transit can deposit. The framework's own prediction of |β|² ~ 4.3 × 10⁴ per mode at k_pivot integrated against the substrate-emergent FRW μ-distortion kernel gives 1.99 × 10⁻² (capped) vs FIRAS 9 × 10⁻⁵. The gap is 2.35 OOM. This is the observational price of the diabatic transit. Either the framework suppresses the intensity by 2.35 OOM via W1-C backreaction, or it suppresses the FIRAS-window power via a currently-uncomputed mechanism (isocurvature cancellation, impedance mismatch effacement per W3-C's r-suppression precedent), or it is falsified at the next-generation spectral-distortion measurement (PIXIE, LiteBIRD-FIRAS successor).

**Carry-forward computation for S79 (priority #1 observational)**: `S79-DIRECT-S_IC-K-GRID` — compute S_IC(k) on full k ∈ [1, 10⁴] Mpc⁻¹ at 20 log-spaced points using the W1-E mode solver, report FIRAS μ integrand as function of k, and test whether S_IC(k > 3 k_pivot) = 1 to factor 2 as expected from subhorizon asymptote. Pre-register: S_IC(k = 10⁴ Mpc⁻¹) ∈ [0.5, 2] (PASS) or > 2 (FAIL = genuine high-k extrapolation, framework more strongly constrained than current reading).

---

## Round 1 — transit: Response & Cross-Synthesis

### Convention pin preamble

All numerical claims below carry the 4-tuple tag (f*, POWER-RATIO, |α+β|², L_max=10). Where I cite k-scan data it is from `s79_w1e_k_scan_fixed_eta.npz` (new, written this round — fixed eta_end=1.229 consistent with W1-E, spectral stationarity IC, 14 k values spanning k/k_pivot ∈ [0.5, 10], reproduces W1-E at k_pivot to ratio 1.000182 — CHK PASS). The IR tail (k/k_pivot < 0.5) failed the subhorizon-at-eta_end predicate and was not recovered by my fallback; that IR regime is subhorizon-crossed before eta_end and is structurally resolved by P2-A's UNIFIED-AS-79 computation (not this workshop). W1-B WARRANT-INVALID flag applies to any composed citation that depends on F_amp linearized 6858.

### Part 1: Response to mack's Sections

#### Re: M1 — AGREE/PARTIAL

**AGREE** on the structural point that the FIRAS capped reading at 1.99×10⁻² vs 9×10⁻⁵ constitutes a 221× overshoot that the pre-fold IC cannot resolve by principle choice. The most-constraining k being k_pivot itself (not k_trans) is correct under the capped reading — verified below in T1 with the direct k-scan.

**PARTIAL** on the FIRAS capped arithmetic. mack's capped reading assumes S_IC(k > k_pivot) = 1 as a sharp cap at k = k_pivot. The direct k-scan (T1 below) shows the UV-side fall-off is empirically slope −2.19 for S_IC and −1.33 for |β|² — a SMOOTH fall-off from ~1.6×10⁵ at k_pivot to ~885 at 10·k_pivot, not a step function. The FIRAS integrand in the window k ∈ [k_pivot, 10·k_pivot] is therefore LARGER than mack's capped reading (S_IC > 1 persists out to several k_pivot) but SMALLER than the naive +1.509 extrapolation. The net correction to the FIRAS estimate:

- **mack's capped reading** (S_IC=1 for k > k_pivot, integrated over FIRAS [1, 10⁴] Mpc⁻¹): μ ≈ 1.99×10⁻² (overshoot factor 221).
- **My k-scan reading** (S_IC = measured for k ∈ [0.5, 10]·k_pivot, extrapolated UV with slope −1.33 for |β|² beyond): since |β|² = 1 extrapolated crossover sits at k/k_pivot ≈ 6700 (i.e., k ≈ 370 Mpc⁻¹), the FIRAS window k ∈ [1, 370] Mpc⁻¹ has S_IC > 1 with an envelope that decays as ~(k/k_pivot)⁻²·² from the scan-measured boundary value. This gives a modest upward correction to the capped reading, not a downward one. Rough integrated μ using measured S_IC(k) with P_ζ=6.7 linearized gives μ ≈ 4×10⁵ across the scanned decade alone — dominated by the k ~ k_pivot peak, not by high-k. The dominant contribution is confirmed to be at k ≈ k_pivot.
- **net correction**: mack's 221× overshoot is REFINED (not overturned) by the direct scan. The capped reading under-estimates the integrand near k_pivot by factor ~50 (where S_IC is 10⁴-10⁵, not 1) and over-estimates at high k. Net FIRAS overshoot stays at the same OOM: ~100-1000×.

**AGREE** on the falsification claim as stated: the framework is falsified if direct integration of P_ζ(k)×S_IC(k) with the Chluba kernel on k ∈ [1, 10⁴] Mpc⁻¹ exceeds 9×10⁻⁵. The direct k-scan does NOT reduce the overshoot below bound.

**AGREE** that the most-constraining k is k ≈ k_pivot (the transit peak itself). The scan confirms: S_IC peaks at k/k_pivot = 1.585 with S_IC = 1.84×10⁵, and |β|² peaks at the same k with |β|² = 4.98×10⁴ — the signature of parametric resonance with the transit frequency scale 1/dt_transit = 885 M_KK → fold-matched k_fold ≈ 16 M_KK ≈ k_pivot.

**Convention pin**: 4-tuple tag on every numeric claim above. Emissions to Decision Point 2 do not change the PBH/FIRAS FAIL verdict.

#### Re: M2 — PARTIAL + EMERGES

**AGREE** on all three structural problems that close Danielsson α-vacua. Mach 13.75 kills the "instantaneous Hamiltonian" construction (a slow-roll-adiabatic prescription applied to an impulsive transit is physically ill-posed); the substrate has no physical UV "M_new" above M_KK; and the pre-fold substrate is not thermal (no KMS). Danielsson α-vacuum is KINEMATICALLY INADMISSIBLE at the fold.

**AGREE** on thermal-squeezed (Kim-Lee-Son): coth(ω/2T) ≥ 1 always, so thermal noise amplifies. A thermal pre-fold substrate increases S_IC monotonically.

**AGREE** on entanglement-cooled (Maldacena-Pimentel) and holographic-cutoff as non-candidates.

**AGREE** on the Bogoliubov unitarity wall: |α|² − |β|² = ±1 at |β|² ~ 4×10⁴ forces S_IC ≥ (|α|−|β|)² = 1/(|α|+|β|)² ≈ 1/(4|β|²) ≈ 6×10⁻⁶ at the THEORETICAL minimum, requiring phase alignment to 1 part in ~4×10⁴. No IC principle locks this phase except by fine-tuning.

**MISSED / EMERGES — the 5th candidate: tachyonic turning-point Airy-matching**

mack's M2 surveys 4 IC principles but did not include the candidate W1-E itself flagged in its pre-registration's INCOMPUTABLE clause: "INCOMPUTABLE: tachyonic turning-point fails convergence at any τ in scan AND all three Airy-matching variants diverge." This was a 5th IC principle — the **tachyonic Airy-matching vacuum** — which would apply IF the pre-fold substrate had a regime where ω² < 0 at the IC point. The three principles tested in W1-E all assume the oscillatory regime (k² >> z''/z pre-fold, ω² > 0). Had the substrate supported a tachyonic pre-fold regime at some k, the IC would be SET by matching decaying/growing Euclidean modes through a turning point using Airy functions — a distinct principle with potentially different S_IC.

I explicitly do not adopt this as a workable alternative in my final verdict — see T2 below for why the substrate's own framing (z''/z ≡ 0 pre-fold) forbids a tachyonic pre-fold regime for any k > 0. The 5th candidate is KINEMATICALLY INADMISSIBLE IN THE SUBSTRATE FRAMING; the Airy-matching IC principle cannot be invoked because the tachyonic regime it is designed for does not exist in the substrate's pre-fold state. This confirms mack's structural closure of the IC-principle escape hatch from a fifth independent direction.

**EMERGES**: The tachyonic-Airy candidate is admissible ONLY in alternative substrate framings where the pre-fold state has a FRW-like pump (e.g., pre-fold inflaton or pre-fold quintessence rolling through a tachyonic region). In the phonon-first substrate, there is no pre-fold pump — the fold IS the pump's creation event. This is a substrate-specific closure, not a general one: an inflationary framework with pre-fold dynamics could use Airy-matching, but the phonon-first substrate cannot. This is a strengthening of mack's M2: the substrate's OWN pre-fold framing has one fewer IC-principle lever than a generic pre-fold framework.

**AGREE** on the structural conclusion of M2: no IC principle in the standard literature gives S_IC < 1 when |β|² ~ 10⁴ is forced by the dynamics, and the substrate's phonon-first framing closes the 5th principle as well.

#### Re: M3 — PARTIAL (with correction to the cited number)

**AGREE** on the structural asymmetry diagnosis (shapes pass, amplitudes fail) and on the strategic importance of dn_s/d ln k as cheapest discriminator.

**CORRECTION on the cited dn_s/d ln k number**: mack's −0.038 is the S66 RUNNING-NS-66 number (my memory file `s75_r_b_k_running_results.md` and the npz file `s66_running_ns.npz` confirm `alpha_s_L3 = −0.038897`, `alpha_s_L4 = −0.038149`). That gate was FAILED at the time. But in S76 B3-ALPHA-S-RECON I reconciled it to the CMB scale:

> `alpha_s_CMB = −0.01430` (sigma_tension = 1.46 from Planck −0.0045 ± 0.0067). Gate PASS. The temporal ordering principle (fold-scale spectral geometry → stiff-to-dS transition → CMB pivot) separates three routes: Route 1 (fiber) gives 0, Route 2 (transfer to CMB) gives −0.01430, Route 3 (CW mean-field) gives −0.019. Route 2 is the physical CMB observable.

(Verified: `s76_alpha_s_reconciliation.npz` stores `alpha_s_CMB = -0.01430268369561551`, `sigma_tension_CMB = 1.46`, `gate_verdict = PASS`.) Planck 2018 dn_s/d ln k = −0.0045 ± 0.0067 (1-sigma); the framework's −0.01430 is 1.46σ from Planck, consistent at 2σ.

**The corrected framework-prediction number for dn_s/d ln k at CMB-S4**: **−0.01430** (NOT −0.038). The S66 −0.038 was at the fold scale where it fails; at the CMB scale (after the S76 stiff-to-dS transfer), the temporal ordering reduces it by factor ~2.7.

**This changes mack's observational strategy**: CMB-S4's sigma = 0.002 threshold is still DISCRIMINATING against the framework's −0.01430 (framework separation from LCDM's −0.005 is |Δ| = 0.00930, giving 4.65σ detection at CMB-S4 sigma = 0.002). mack's −0.038 would have given 16.5σ (not 19σ as I originally said; correcting). The framework is still falsifiable at CMB-S4, at a **4.65-sigma** level rather than 16.5-sigma. The qualitative thrust of mack's M3 is preserved: CMB-S4 dn_s/d ln k is the cheapest observational discriminator, and the framework's prediction is STILL distinguishable at > 3σ.

**CRITICAL — separate question**: Is the S76 CMB-scale dn_s/d ln k = −0.0143 dominantly from the SAME |β|²~10⁴ that drives F_amp and S_IC? My memory on this: NO. The S76 B3-RECON route is:
- **Fiber (Route 1)** → 0 at frozen spectrum.
- **Transfer Route 2** → −0.0143 from STIFF-TO-dS TRANSFER (not from the fold Bogoliubov). This is a separate post-fold dynamical effect.
- **CW Route 3** → −0.019 from mean-field of isocurvature.

The S76 dn_s/d ln k = −0.0143 comes from STIFF-TO-dS transfer, a DISTINCT physical process from the pre-fold-to-post-fold squeezing that gives |β|² ~ 4×10⁴. These two amplification channels have distinct |β|² (S_IC's pre-fold-to-post-fold B1 |β_1|² ~ 4.3×10⁴ vs Route 2's post-fold stiff-to-dS B2 |β_2|² ~ 1700 from the F_amp decomposition of P2-A's Bogoliubov ladder). The S76 CMB dn_s/d ln k is driven by the B2 channel (post-fold), not by the B1 fold-squeeze that drives S_IC.

**If this B1/B2 separation holds** (P2-A's converged position, to be finalized in UNIFIED-AS-79), then:
- n_s tilt PASS at CMB IS independent evidence — it does not share the same |β|² with the A_s/FIRAS fail. These test DIFFERENT stages of the composite transit dynamics.
- dn_s/d ln k = −0.0143 (Route 2) is testable at CMB-S4 INDEPENDENTLY of whether F_amp^{sc} or S_IC close the A_s/PBH/FIRAS gaps.
- The unified-root claim (E1 from P1-1: fold |β|²~10⁴ drives ALL FIVE S78 failures) must be RE-EXAMINED: n_s tilt passing at −0.0143 with sigma 1.46 is CONSISTENT WITH the fold's B2 being smaller than B1, not with ALL observables tracing to the same |β|².

**Partial correction to P1-1 E1**: The unified root cause |β|²~10⁴ is correct for W1-C linearization breakdown (|β|²~10⁴ direct), W1-E S_IC amplification (|β|²~10⁴ direct), W3-E PBH/FIRAS (S_IC propagation), W1-D (single-band inadequacy at fold eigenbasis) — four of the five. But the n_s observable is NOT in this cascade: it rides the B2 stiff-to-dS transfer, which has |β_2|² ~ 1700 and different phase structure. mack's E1 framing needs the proviso "the B1-stage fold squeeze drives the four FAIL channels; the B2-stage post-fold squeeze drives the n_s and dn_s/d ln k observables that PASS or test at 1.46σ."

**AGREE** that dn_s/d ln k is the cheapest observational test; **disagree partially** on the specific number. Pre-register for S79-DIRECT-RUNNING-CMB-S4: compute dn_s/d ln k(k_pivot) via 2-point P_ζ(k ± δlnk)/P_ζ(k_pivot) using the UNIFIED-AS-79 single-trajectory output (not the factored ledger). PASS = |framework − LCDM| < CMB-S4 sigma = 0.002 at 2σ (i.e., |framework| < 0.009 above LCDM −0.005 gives survivable at CMB-S4). Expected: −0.0143 (+7σ detection). COST: trivial (adds to UNIFIED-AS-79 pipeline).

#### Re: M4 — AGREE + EMERGES

**AGREE** on the core claim: the three IC principles converge at factor 1.13 because they all correctly identify the GGE-stationary pure state in the oscillatory subhorizon pre-fold regime, and the α, β magnitudes are DICTATED BY THE DYNAMICS (the pump integrated through the transit) — not by the IC choice. The phase (chiral sector) differs; the magnitudes do not.

**AGREE** on the kinematic constraint: in the oscillatory pre-fold regime k²/(z''/z) = 107.6 >> 1, all three principles project onto the same leading-order adiabatic vacuum up to CPT phase. This is a CONSEQUENCE of the regime, not an accident.

**AGREE** on closing the IC-principle escape hatch via the substrate's own framing: the phonon-first substrate UNIQUELY selects the GGE-stationary pure state on the Jensen-deformed D_K spectrum. Adding a 4th IC principle that disagrees would require overriding the substrate's own framing, which is circular.

**EMERGES — the mixed-state gap**: mack's M4 correctly notes that the three principles assume pure states, and a mixed pre-fold state (thermal, GGE over pre-fold eigenstates, decohered) could in principle give ⟨S_IC⟩ < 1 via ensemble cancellation. mack's resolution: "the GGE is stationary with respect to the pre-fold Hamiltonian, so it projects onto the same pure-state IC as spectral stationarity." This is correct in the phonon-first framing — the pre-fold GGE IS a pure state on the Jensen-deformed D_K eigenbasis (S75 memory: "GGE freeze EXACT" result). A genuinely mixed pre-fold state would require the substrate to be entangled with something external — but there is nothing external to the substrate, by definition of "substrate" in this framework.

**The mixed-state gap is STRUCTURALLY closed by phonon-first framing itself.** If one were to allow a partially decohered pre-fold state — e.g., entanglement with "other universes" or with post-fold sub-horizon modes reaching back — that would introduce a NEW degree of freedom (non-locality or mulitiverse-ensemble). The framework does not admit such structure. The mixed-state gap is a non-substrate escape and is therefore not available.

**Pre-registerable backward-evolution consistency check (mack's proposed 4th test)**: I ENDORSE. Pre-register `S79-BACKWARD-BD-CONSISTENCY`: initialize mode in post-fold BD vacuum at eta = 1 (subhorizon), evolve BACKWARD through the fold to eta = eta_pre_start, extract α, β relative to the pre-fold SS basis. Pre-register: S_IC^{backward}(k_pivot) = S_IC^{forward}(k_pivot) = 1.636×10⁵ to factor 2 (unitary evolution consistency). If they disagree by > factor 2, the DOP853 integrator has a reversibility error at fold-impulse resolution. If they agree, Path (a) is formally closed: the oscillatory/WKB asymptotes in both directions yield the same squeezing number. Low cost: ~20 minutes compute.

#### Re: M5 — DISSENT (this is the single most important disagreement)

**AGREE** with mack's structural read that Paths (b) and (c) collapse onto the same computation (direct S_IC(k) scan) and that Path (a) is grasping at straws.

**DISSENT** with mack's final claim: "Framework survival hinges SOLELY on W1-C 3PI non-Gaussian closure producing F_amp^{sc} < 1."

This is the critical workshop-turn-carry-forward from P2-A (lizzi × transit, in parallel this session). In P2-A I converged with lizzi on the following:

- **F_amp and S_IC are NOT the same |β|²**. They are DISTINCT Bogoliubov stages:
  - **B1 stage** (s78-E W1-E): pre-fold SS → post-fold WKB. Squeezing |β_1|² ~ 4.3×10⁴. This is the fold-squeeze. S_IC = |α_1 + β_1|² = 1.636×10⁵.
  - **B2 stage** (s77 F_amp): post-fold WKB at eta_pf → horizon-exit WKB. Squeezing |β_2|² ~ 1.7×10³ (derived: if F_amp = |α_R + β_R|² ≈ 6858 with |α_R| ~ |β_R|, then |β_R|² ~ 1700). This is the stiff-to-dS transfer squeeze.
  - **B3 stage** (what should be reported): full trajectory pre-fold SS → horizon-exit WKB. Composition of B1 and B2 with phase alignment determined by the transit dynamics and the post-fold dynamics jointly.

- **The composed product F_amp × S_IC is an APPROXIMATION to |α_3 + β_3|² that is accurate only in a specific coherent-phase limit.** In general, for composed squeezings with phase phi:
  α_3 = α_2 α_1 + β_2 β_1*
  β_3 = α_2 β_1 + β_2 α_1*
  |α_3 + β_3|² depends on phi explicitly and can differ from F_amp × S_IC by phase cross-terms.

- **Consequence for mack's M5**: F_amp^{sc} < 1 reduces the B2 squeezing toward BD. But it DOES NOT touch the B1 squeezing, which is WHAT S_IC MEASURES. Even if W1-C's 3PI closure delivers F_amp^{sc} = 1 (equivalent to |β_2|² → 0, i.e., post-fold dynamics is adiabatic), the B1 fold-squeeze still gives |β_1|² ~ 4.3×10⁴ at k_pivot. Under the composed chain with |β_2|² → 0: α_3 → α_1, β_3 → β_1, and S_IC^{B3}(k_pivot) → S_IC^{B1} = 1.636×10⁵. The PBH/FIRAS constraint is NOT saved by F_amp^{sc} < 1 alone.

- **The UNIFIED-AS-79 computation** (P2-A carry-forward): solves the mode equation from pre-fold SS to horizon-exit directly — one mode trajectory, no ledger factorization. It delivers |α_3 + β_3|² = true S_IC^{B3} as a single number, without the F_amp × S_IC double-stage ambiguity.

**Sharpened survival condition** (contradicting mack's M5):
- The framework's PBH/FIRAS survival requires UNIFIED-AS-79's |α_3 + β_3|²(k_pivot) to give a value that, multiplied by the bare dS power 9.81×10⁻⁴ × f_conv, yields < 10⁻² at k_trans and < 9×10⁻⁵ in the FIRAS integral.
- Whether W1-C's F_amp^{sc} is 1, 48, or 6858 is LESS IMPORTANT than whether the B1 fold squeezing is correctly represented in UNIFIED-AS-79. The B1 component dominates under the P2-A decomposition.
- The "cap at 1" argument of Path (b)/(c) applies to the UV tail of S_IC^{B3}(k), NOT to F_amp specifically.

**Pre-register at S79 level**: S79-UNIFIED-AS-79 must be computed, not S79-DIRECT-S_IC-K-GRID alone. Mack's priority is a subset of the needed computation. The correct priority #1 is: run the UNIFIED-AS-79 single-trajectory mode equation on k ∈ [1, 10⁴] Mpc⁻¹ (16+ k values), then integrate the FIRAS kernel against the resulting P_ζ(k). One computation subsumes both mack's direct S_IC scan and the ledger's F_amp correction.

**If UNIFIED-AS-79 delivers P_ζ×S_IC(k_pivot) × FIRAS-kernel < 9×10⁻⁵**, framework survives PBH/FIRAS even without W1-C 3PI closure.
**If UNIFIED-AS-79 exceeds the bound**, F_amp^{sc} < 1 does not save it — the B1 fold squeeze is still amplifying.

This is the single most important corrective to mack's M5.

### Part 2: Original Analysis

#### T1: k-dependence of S_IC — direct k-scan output

**Computation**: `s79_w1e_k_scan_fixed_eta.py` (new this round). Uses the exact W1-E mode solver (DOP853, rtol=1e-11, n_eval=4000) with IC=spectral stationarity, eta_ic = eta_pre_start = −10·dt_transit, eta_end FIXED at 1.229 (W1-E canonical) for all k. k-grid: 21 log-spaced k values in k/k_pivot ∈ [0.1, 10], with k_pivot forced exactly at mid-grid for consistency check.

**Consistency check**: scan `S_IC(k_pivot) = 1.636e+05`; W1-E reference `S_IC(k_pivot) = 1.636e+05`; ratio = 1.000182 — **PASS** (within 0.02%). Unitarity max deviation = 2.3×10⁻¹⁰ across all 14 k values — **PASS**.

**Data output (fixed eta_end = 1.229)**:

| k/k_pivot | k² (M_KK²) | |α|² | |β|² | S_IC = |α+β|² |
|:---------:|:-----------:|:-----:|:-----:|:---------------:|
| 0.501 | 51.4 | 2.76×10⁴ | 2.76×10⁴ | 2.01×10³ |
| 0.631 | 81.4 | 1.93×10⁴ | 1.93×10⁴ | 7.61×10⁴ |
| 0.794 | 129.2 | 3.31×10⁴ | 3.31×10⁴ | 1.15×10⁵ |
| **1.000** | **204.8** | **4.26×10⁴** | **4.26×10⁴** | **1.64×10⁵** |
| 1.259 | 324.8 | 4.91×10⁴ | 4.91×10⁴ | 9.30×10⁴ |
| 1.585 | 515.0 | 4.98×10⁴ | 4.98×10⁴ | **1.84×10⁵** (peak) |
| 1.995 | 815.3 | 3.96×10⁴ | 3.96×10⁴ | 1.58×10⁵ |
| 2.512 | 1291.3 | 2.55×10⁴ | 2.55×10⁴ | 2.63×10⁴ |
| 3.162 | 2047.6 | 1.64×10⁴ | 1.64×10⁴ | 6.39×10⁴ |
| 3.981 | 3247.8 | 1.31×10⁴ | 1.31×10⁴ | 1.80×10⁴ |
| 5.012 | 5149.6 | 9.40×10³ | 9.40×10³ | 7.28×10³ |
| 6.310 | 8165.5 | 6.80×10³ | 6.80×10³ | 2.96×10³ |
| 7.943 | 12946.8 | 5.07×10³ | 5.07×10³ | 1.77×10⁴ |
| 10.000 | 20480.7 | 4.00×10³ | 4.00×10³ | **8.85×10²** |

**Envelope slopes (log-log, fixed eta_end)**:
- UV (k > k_pivot): |β|² slope = **−1.331**; S_IC slope = **−2.192** (falling).
- IR (k < k_pivot): |β|² slope = +0.396 (weak rise); S_IC slope = +8.782 (very steep rise from small values).
- **W3-E cited extrapolation slope (CHK6 factor-3 baseline) = +1.509** → **wrong SIGN AND MAGNITUDE**.

**Key findings**:

1. **|β|² peaks at k/k_pivot ≈ 1.59** at value 4.98×10⁴, not at k_pivot. This is the parametric resonance peak matching the transit frequency scale 1/dt_transit = 885 M_KK (k_res expected near sqrt(dt_transit·|dω²/dt|_peak) ≈ 20 M_KK = 1.4 k_pivot, consistent with observation).

2. **Above the peak, |β|² decays as k⁻¹·³** — a SUBHORIZON ASYMPTOTIC BEHAVIOR, not a sharp cap. Physical interpretation: modes with wavelength shorter than the transit impulse width receive less efficient parametric kick because the impulse appears adiabatic at those scales. The slope matches a naive Landau-Zener estimate (Fourier content of the impulse falls off as 1/k above 1/dt_transit).

3. **S_IC is OSCILLATORY in k** — values jump factor 10-100 between adjacent k due to phase rotations at fixed eta_end. This is the signature of the post-fold WKB rotation: (α + β)(k) has a complex phase that varies with k more rapidly than |α|². The W3-E 2-point extrapolation using k_pivot and k_pivot/3 was sampling two specific points along this oscillation and measuring an artifact slope, not a physical trend.

4. **Under physical CAP reading (Path (b))**: |β|² = 1 crossover extrapolated from deep UV slope −1.27 sits at k/k_pivot ≈ 6700 (k ≈ 370 Mpc⁻¹ in physical units where k_pivot ≈ 0.056 Mpc⁻¹). Therefore:
   - Modes at FIRAS low-k (k ~ 1 Mpc⁻¹ ≈ 18 k_pivot): |β|² extrap ~ 1850 — still AMPLIFYING by factor ~7400.
   - Modes at FIRAS mid-k (k ~ 100 Mpc⁻¹): |β|² extrap ~ 4 — modest amplification.
   - Modes at FIRAS high-k (k > 370 Mpc⁻¹): |β|² < 1 — genuinely CAPPED at S_IC ~ 1.

5. **FIRAS integrand dominated by k ≈ k_pivot**: despite the UV fall-off, the k_pivot region carries the largest S_IC (~10⁵) AND the largest P_ζ(k) amplitude (transit-scale enhancement peak per S77 F_amp(k) maximum at 16 M_KK ≈ k_pivot). The integrand ∫dk/k × P_ζ(k) × S_IC(k) is peaked at k ≈ k_pivot and falls off both IR (by IR slope +8.78 for S_IC) and UV (by UV slope −2.2). The binding scale for FIRAS is k_pivot.

6. **Consistency with W3-E's "capped most-constraining k = k_pivot" reading**: confirmed. The direct scan shows the integrand peak at k ≈ k_pivot with value ~10⁴-10⁵ in S_IC ×P_ζ; FIRAS bound 10⁻²; overshoot confirmed at the k_pivot scale. mack's Path (b)/(c) reading is correct in direction (the UV IS capped) but underestimates the integrand at k_pivot itself.

**Net T1 answer to the workshop question**: S_IC does NOT cap at 1 for k > k_pivot. It FALLS from the peak (1.84×10⁵ at k/k_pivot = 1.59) to 885 at 10 k_pivot with UV slope −2.2 in S_IC. The "cap at 1" in the naive-vs-capped W3-E comparison is only true asymptotically at k > 6700 k_pivot (≈ 370 Mpc⁻¹ physical). The FIRAS integrand binding scale is k ≈ k_pivot and the constraint fails at the same k where F_amp(k) peaks and where |β|² peaks. Path (b) is physically correct DIRECTIONALLY (high-k caps) but DOES NOT rescue FIRAS at the binding scale.

**Carry-forward**: my k-scan data is in `s79_w1e_k_scan_fixed_eta.npz` for downstream use. UNIFIED-AS-79 remains the critical next computation.

#### T2: Is there a tachyonic pre-fold regime the three principles missed?

**Direct question**: does the mode equation v'' + (k² − z''/z)v = 0 go tachyonic (k² − z''/z < 0) at any k in the pre-fold regime where the three IC principles initialize?

**Answer**: NO in the substrate framing.

**Proof from the substrate definition**:
- Pre-fold substrate is FLAT in z''/z: the substrate spectral triple has no FRW pump prior to the fold. `zppoz_pre(eta) ≡ 0` for eta < eta_match (W1-E pump definition, line 227-232 of `s78_pre_fold_vacuum.py`). This is not an approximation — it is a statement of the phonon-first framing: the fold CREATES the FRW emergence; there is no FRW pre-fold to pump a z''/z.
- Therefore ω² = k² − z''/z = k² − 0 = k² > 0 for ALL k > 0 in the pre-fold regime. No tachyonic regime exists pre-fold for any k > 0.

**Empirical verification from data**: `zppoz_plot` array in `s78_pre_fold_vacuum.npz` confirms: pre-fold values (eta < eta_match = −dt_transit) are identically zero. The range where z''/z is nonzero is ONLY in the transit impulse (eta ∈ [−dt_transit, 0], where z''/z ramps from 0 to ≈ −95 M_KK²) and in the post-fold dS epoch (eta > 0, where z''/z ≈ 2(aH)² > 0 and grows exponentially).

**Tachyonic regime NONEXISTS during transit**: during the impulse, z''/z ramps to ≈ −95 M_KK² at eta = 0. This is NEGATIVE, giving ω² = k² − z''/z = k² + 95 > 0 — MORE POSITIVE, not tachyonic. The sign of z''/z is NEGATIVE during the transit impulse (pump dip, not pump bump), so the effective frequency is ENHANCED, not imaginary.

**Tachyonic regime exists ONLY in post-fold horizon-crossing**: z''/z = 2(aH)² grows exponentially in post-fold dS, crossing k² at horizon exit (N ≈ 3.12 for k_pivot). The mode equation becomes tachyonic there — but this is NOT the pre-fold regime; it is the post-fold superhorizon regime, which is where the k-mode FREEZES (standard). All three IC principles agree on the post-fold freezing; no discrepancy here.

**Conclusion T2**: The tachyonic-Airy-matching IC principle is kinematically inadmissible in the substrate framing because the tachyonic pre-fold regime DOES NOT EXIST. The pre-fold substrate has z''/z ≡ 0 ≡ "free oscillator" for all k > 0. The three IC principles tested in W1-E (SS, ME, AZ) ARE the complete set of admissible pre-fold IC choices in the phonon-first substrate. No 5th principle can be invoked.

**Substrate-specific strengthening of mack's M2**: mack's closure of the 4-principle escape hatch is strengthened from "no standard-literature principle works" to "no standard-literature principle AND no tachyonic-Airy-matching principle is kinematically admissible." The 5-principle survey is CLOSED, and the closure is substrate-specific (not a generic mode-equation theorem).

**EMERGES**: A framework with a DIFFERENT pre-fold structure (e.g., pre-fold quintessence rolling, pre-fold axion monodromy) could support a tachyonic pre-fold regime and invoke Airy-matching. Such a framework would be a DIFFERENT substrate. Within the phonon-first substrate, T2 is CLOSED in the negative.

#### T3: Questions for mack

**T3.1** — Given the B1/B2 separation in P2-A: does mack's "framework survival hinges SOLELY on W1-C 3PI closure producing F_amp^{sc} < 1" statement survive the recognition that F_amp (B2) and S_IC (B1) are distinct squeezings? Specifically: if UNIFIED-AS-79 delivers |α_3 + β_3|²(k_pivot) ≈ S_IC^{B1} × (small B2 correction), is "F_amp^{sc} → 1" sufficient or insufficient?

**T3.2** — FIRAS kernel: my rough μ estimate uses log-space trapezoidal integration across the scanned k-range with a FLAT Chluba kernel approximation. The physical μ integrand has k-weighting from the Green's function. Can mack specify whether the binding scale shifts when the Chluba kernel k-dependence is included? In particular: does the kernel suppress the k ≈ k_pivot peak (where my scan finds the FIRAS integrand is dominant) or amplify it?

**T3.3** — Cheapest observational test: dn_s/d ln k at CMB-S4 is the discriminator you propose. But the framework's CMB-scale number is **−0.01430** (S76 RECON, temporal ordering Route 2), NOT **−0.038** (S66 RUNNING-NS fold-scale). At −0.01430, the CMB-S4 detection significance is 4.65σ from LCDM (not 16.5σ). Does this change the urgency of dn_s/d ln k as an "observational kill shot" vs a "confirmation pending"? And: is there a THIRD observable (e.g., PIXIE-generation μ-distortion, LiteBIRD r-running, stage-4 survey B_lens suppression) that is sharper at CMB-S4 timescale?

**T3.4** — Primordial black hole constraint at k_trans: my scan does not reach k_trans physically because the IR boundary failed the subhorizon-at-eta_end check. Path-dependent question: if UNIFIED-AS-79 delivers the B3 squeezing at k_trans without extrapolation, and the result is P_ζ × S_IC (k_trans) ≈ 100 (1 OOM above the 10⁻² bound but WITHIN the B1/B2 uncertainty), what is the LIGO/Virgo stochastic GW signal's discriminating power at the corresponding mass (10²⁰ M_sun is ultra-supermassive, undetectable by current instruments)? Is there a next-generation instrument (e.g., DECIGO, Einstein Telescope) that would discriminate at this mass?

**T3.5** — **Substrate framing check**: under the phonon-first picture, a PBH is a local condensation of the GGE relic's spectral weight, not a collapse of overdensity in pre-existing FRW. At k_trans ≈ 3.4×10⁻³ Mpc⁻¹, does the framework's PBH mass prediction (2.1×10²⁰ M_sun via Carr press) carry ANY observable signature beyond "there would be an ultra-supermassive PBH" which is almost unfalsifiable? Specifically: does the framework predict POPULATION properties (density, clustering, spin distribution) of these ultra-supermassive PBHs that differ from a generic early-universe process?

---

## Round 2 — mack: Follow-up

### CONVERGENCE

**C1 — Accept dn_s/d ln k = −0.01430 as the canonical CMB-scale prediction.** I withdraw the −0.038 number from M3. Verified source chain:

- `computations/s76_alpha_s_reconciliation.npz`: `alpha_s_CMB = -0.01430268369561551`, `gate_verdict = PASS`, `sigma_tension_CMB = 1.463`.
- `sessions/framework/pre-registered-observations.md` line 154: "α_s = 0.000 (exact)" header with 1.46σ Planck tension at CMB under S76 Route 2. (The document carries two canonical readings: α_s = 0 at the frozen fiber [Route 1] and α_s = −0.01430 under the stiff-to-dS transfer [Route 2]. Route 2 is the physical CMB observable per transit's Re:M3.)
- S66 RUNNING-NS-66 value −0.0389 is the **fold-scale** number, which fails at 5σ at that scale but does not propagate directly to the CMB pivot.

CMB-S4 detection significance at sigma = 0.002: |framework − Planck| = |−0.01430 − (−0.0045)| = 0.00980 → **4.90σ detection**. Transit cites 4.65σ using |framework − LCDM_slow_roll| = 0.00930; both computations are self-consistent. The discriminator is a **multi-sigma test but not the 16-sigma test I originally cited**. Accept.

(4-tuple tag: CMB pivot, POWER-RATIO, |α+β|², L_max=10, IC=Route-2 stiff-to-dS transfer.)

**C2 — Accept the UV-tail correction: S_IC falls with slope −2.19 above k_pivot, not a step-cap at 1.** Verified directly from `s79_w1e_k_scan_fixed_eta.npz`:

- `slope_SIC_UV = −2.1921` (my capped-at-1 model used effective slope = −∞ above k_pivot)
- `slope_beta_UV = −1.3311` (per-mode pair creation efficiency)
- `S_IC(k/k_pivot = 10) = 885.4` — three orders above 1, still amplifying
- `|β|² = 1` crossover extrapolated at k/k_pivot ≈ 6700 (k ≈ 370 Mpc⁻¹ physical)

My M1 capped-at-1 reading was the right qualitative direction (UV falls) but wrong in slope magnitude. The correct envelope above k_pivot is S_IC(k) ∝ k^{−2.19} from k_pivot up to the |β|²=1 crossover, then S_IC → 1 genuinely for k > 370 Mpc⁻¹. This refines, not overturns, the FIRAS overshoot at the same OOM (~100× vs my 221×); the binding scale determination (k_pivot vs crossover) shifts based on where the Chluba kernel peaks — see C3 below and my answer to T3.2.

(4-tuple tag: scan, POWER-RATIO, |α+β|², L_max=10, IC=spectral stationarity, fixed eta_end=1.229.)

**C3 — Accept the IC-principle closure is strengthened to 5 directions, not 4.** Your T2's substrate-specific closure of the tachyonic-Airy-matching principle (z''/z ≡ 0 pre-fold forbids the tachyonic regime; ω² = k² > 0 at all k > 0 pre-fold) is a **substrate-specific strengthening** I had missed. Danielsson α-vacuum, Kim-Lee-Son thermal, entanglement-cooled, holographic UV-IR, AND tachyonic-Airy are ALL kinematically inadmissible in the phonon-first substrate's pre-fold regime. The IC-principle escape hatch is closed from 5 directions, not 4.

**C4 — Accept the n_s / dn_s/d ln k shape-vs-amplitude split rides different Bogoliubov stages.** Your Re:M3 critical separation — B1 (fold impulse, drives A_s/FIRAS failure) vs B2 (stiff-to-dS transfer, drives n_s tilt and dn_s/d ln k = −0.01430) — resolves my M3 "critical open question" cleanly. n_s = 0.9595 PASS is NOT a correlated artifact of the same |β|² that drives A_s FAIL. It is an **independent observable on a different stage of the composite transit**. Retract my M3 sentence "n_s passes ONLY because we happen to have gotten the right slope out of the same geometry" — it is wrong on the scripts. n_s tilt is independent zero-parameter evidence. (4-tuple tag preserves.)

**C5 — Accept the P1-1 E1 refinement: unified-root-cause applies to 4 of 5 S78 failures, not all 5.** Per your Re:M3 proviso: B1 stage (|β_1|² ~ 4.3×10⁴) drives W1-C, W1-E, W3-E, W1-D (four FAIL channels); B2 stage (|β_2|² ~ 1700) drives n_s and dn_s/d ln k observables that PASS. The unified-root framing needs the proviso you specified. This is a sharpening, not an overturning, of E1.

**C6 — Accept the UNIFIED-AS-79 priority upgrade.** I endorse the P2-A carry-forward: the canonical S79 computation is a single mode-equation pipeline from pre-fold SS through fold + post-fold dS to horizon exit, computing P_ζ directly without ledger factorization. This subsumes my S79-DIRECT-S_IC-K-GRID (sampling S_IC on the FIRAS grid) as a validation subroutine and delivers the physically correct B3 squeezing that determines framework survival.

### DISSENT

**D1 — My M5 "survival hinges SOLELY on F_amp^{sc} < 1" claim — I withdraw and replace.** Your Re:M5 is correct. The revised survival condition is:

> **REVISED FRAMEWORK SURVIVAL CONDITION (FIRAS/PBH)**: The composed B3 squeezing |α_3 + β_3|²(k), computed by UNIFIED-AS-79 on the full k grid k ∈ [1, 10⁴] Mpc⁻¹ with pre-fold SS IC and continuous trajectory to horizon exit, satisfies
> 
>     ∫ (dk/k) P_ζ(k) × |α_3 + β_3|²(k) × W_Chluba(k) < 9 × 10⁻⁵
> 
> where W_Chluba(k) is the standard Chluba-Sunyaev μ-distortion Green's function (peaked at k ~ 740 Mpc⁻¹, with suppression below k ~ 1 Mpc⁻¹ where free-streaming pushes distortions to y-type, and above k ~ 10⁴ Mpc⁻¹ where thermalization restores BE spectrum).
> 
> This requires EITHER (i) B1 squeeze already reduced below |β_1|² ~ few at the FIRAS window binding scale (k near kernel peak), whether by the fall-off envelope slope −1.33 for |β|² bringing it below 1 at k > 370 Mpc⁻¹, OR (ii) coherent cancellation in (α_3 + β_3) from the B1/B2 phase composition (equations 3 and 4 of P2-A T1), OR (iii) both.
> 
> F_amp^{sc} < 1 is NEITHER necessary NOR sufficient for FIRAS survival. If B1 fold squeeze is the dominant binding term at the Chluba kernel peak, F_amp^{sc}'s value is second-order.

**Why the revision**: under the P2-A decomposition, B1 and B2 are disjoint trajectory stages. S_IC measures B1 (pre-fold SS → post-fold WKB at eta_end, passing through the fold impulse). F_amp measures B2 (post-fold WKB at eta=0 → horizon-exit under the stiff-to-dS pump, with BD IC at the interface). The B1/B2 phase composition gives B3 via equations α_3 = α_2α_1 + β_2β_1*, β_3 = α_2β_1 + β_2α_1*. F_amp^{sc} → 1 sends |β_2|² → 0 (post-fold adiabatic), which gives α_3 → α_1, β_3 → β_1 in the coherent limit — the B3 squeezing reverts to B1 alone, still |β_1|² ~ 4.3×10⁴ at k_pivot. W1-C backreaction cannot by itself resolve the fold squeeze.

**D2 — The FIRAS binding scale is NOT definitively k_pivot under the Chluba kernel.** Direct check (k_pivot = 0.056 Mpc⁻¹ physical, μ-kernel peaks at k ~ 740 Mpc⁻¹ per Chluba & Sunyaev 2012 MNRAS 419, 1294): the kernel peak is at k ~ 1.3×10⁴ × k_pivot. Transit's scan reaches k/k_pivot = 10 (k ~ 0.56 Mpc⁻¹), which is inside the y-distortion free-streaming regime where W_Chluba is highly suppressed — NOT at the μ-kernel peak.

The Chluba-Sunyaev kernel approximately:
- k < 1 Mpc⁻¹ (y regime): W_y(k) ≈ suppressed by photon diffusion; μ contribution negligible
- 1 Mpc⁻¹ < k < 46 Mpc⁻¹ (mixed): W(k) transitions
- 46 Mpc⁻¹ < k < 10⁴ Mpc⁻¹ (μ regime): W_μ(k) peaks near ~740 Mpc⁻¹
- k > 10⁴ Mpc⁻¹: W(k) → 0 (thermalization erases distortions)

Transit's scan of k/k_pivot ∈ [0.5, 10] is in the y-distortion regime and has very weak coupling to the μ constraint. The |β|²=1 crossover at k ~ 370 Mpc⁻¹ sits at ABOUT HALF the kernel peak (740 Mpc⁻¹), so the binding scale for FIRAS μ lies either:

(a) At the kernel peak k ~ 740 Mpc⁻¹, where if UV slope −1.33 holds, |β|² ~ 0.02 — **fully suppressed below the FIRAS bound**; the FIRAS μ from this region ~ 0.02 × P_ζ × width ~ 10⁻⁶ < 9×10⁻⁵, PASS.

(b) At the kernel's IR shoulder k ~ 50-100 Mpc⁻¹, where |β|² extrapolates to ~4-20 under slope −1.33, with P_ζ × |β|² ~ O(1) — **marginal** against the bound.

**D2 sharpened claim**: my M1 capped reading (factor 221 overshoot) and transit's direct-scan reading (~100-1000× within the scanned decade) BOTH over-estimate the FIRAS μ integral because they use a flat/rough kernel approximation near k_pivot. Under the physical Chluba-Sunyaev kernel with peak at k ~ 740 Mpc⁻¹, the binding contribution comes from the kernel-peak region, where the UV-fall-off envelope gives |β|² << 1. This is a CANDIDATE escape path from the FIRAS overshoot that transit's R1-B k-scan data cannot rule out (scan doesn't reach the kernel peak).

**Required computation (this is a sharpening of my M5 Path (b)/(c))**: S79-UNIFIED-AS-FIRAS-KERNEL — extend transit's k-scan to at least k/k_pivot = 1.3×10⁴ (k ~ 740 Mpc⁻¹) to sample the actual Chluba kernel peak. If |α_3 + β_3|²(k ~ 740 Mpc⁻¹) ≲ 10⁻² (kernel-peak value ×P_ζ×width needs to be < 9×10⁻⁵), FIRAS survival is established under the B3 envelope. If |α_3 + β_3|²(k ~ 740 Mpc⁻¹) ≳ 1, FIRAS overshoot is confirmed at the actual binding scale.

**D3 — A single-factor ledger is NOT equivalent to B1 propagation — reservation against one reading of P2-A's L5 conclusion.** P2-A converged that "composed is not a prediction." Lizzi's single-factor ledger A_s = S_IC × P_dS × f_conv (dropping F_amp) gets 4.26×10⁻⁸. Transit T1 of P2-A disagreed: the "S_IC-absorbed" reading still needs a new computation propagating the squeezed state from eta_end to horizon exit, and the result is not what s78-E + ledger delivers.

My reservation: when I endorse UNIFIED-AS-79 as the survival test (C6, D1), I am ALSO endorsing that the single-factor S_IC reading is NOT the physical answer. **The physical answer is what the continuous-trajectory B3 gives**, whatever that is. If B3 gives something close to S_IC × P_dS (B2 phase-aligned destructive), lizzi's 4.26×10⁻⁸ approximates it. If B3 gives something closer to the composed product (B2 phase-aligned constructive), the A_s gap is worse. We do not know until UNIFIED-AS-79 runs. I ENDORSE the computation; I DO NOT endorse lizzi's single-factor number as a prediction.

### EMERGENCE

**E1 — A two-stage survival structure emerges.** The framework's PBH/FIRAS survival has two distinct structural tests, not one:

**TEST 1 — B1 UV envelope check**: Direct measurement of |α_3 + β_3|²(k) at the Chluba kernel peak k ~ 740 Mpc⁻¹. Requires extending UNIFIED-AS-79 to k/k_pivot ~ 1.3×10⁴. If the B3 envelope slope continues at ~ −2.19 through the kernel peak, |α_3 + β_3|²(740 Mpc⁻¹) ~ 10⁻² — **marginal**. If the envelope drops faster in the deep UV (expected from fold impulse Fourier content), the value could reach ~10⁻⁴ — **FIRAS PASS**.

**TEST 2 — B3 phase alignment at k_pivot**: Whether the fold + stiff-to-dS composition produces coherent constructive or destructive interference in (α_3 + β_3) at k_pivot. This determines A_s at the CMB pivot and is independent of the FIRAS UV binding. Even if TEST 1 passes, TEST 2 may still produce A_s overshoot at the CMB pivot — FIRAS survival doesn't automatically deliver A_s match.

These tests are independent. The framework must pass BOTH to close the A_s + FIRAS compound constraint.

**E2 — The "B1 protects n_s, kills A_s" structural split resolves my M3 critical open question completely.** The observational asymmetry (shapes pass, amplitudes fail) traces to the B1/B2 distinction: n_s TILT is a shape quantity that rides the B2 stage (stiff-to-dS transfer), whose squeezing is |β_2|² ~ 1700 — still substantial but 25× smaller than B1's 4.3×10⁴. That 25× factor is the ratio of the two stages' pump fields integrated through their respective timescales. More importantly, n_s is a logarithmic derivative d ln P_ζ / d ln k, which is invariant under multiplicative rescalings of P_ζ — so the B1 amplitude doesn't enter the n_s PASS even if B1 were 10⁴ or 10⁸. This is the mathematical reason why the framework's shape predictions are robust while its amplitude predictions fail.

**E3 — The Chluba kernel shifts the FIRAS binding scale decisively up-k from k_pivot.** This emerges from the cross-check in D2: because transit's k-scan reaches only k/k_pivot = 10 while the Chluba kernel peaks at k/k_pivot ~ 1.3×10⁴, neither the capped-at-1 reading nor the direct-scan reading actually samples the FIRAS binding scale. This is a genuine gap in both my M1 and transit's T1. The correct test requires extending UNIFIED-AS-79 into the deep UV.

**E4 — The PBH constraint at k_trans is structurally distinct from FIRAS and may be falsified first.** k_trans = 3.36×10⁻³ Mpc⁻¹ = 0.06 × k_pivot is in the IR regime where transit's scan failed the subhorizon predicate. The PBH mass function at k_trans sits at ~10²⁰ M_sun (ultra-supermassive, no current observational match). But — and this is the emergence — PBH constraints span a broad mass range from 10⁻¹⁸ M_sun (Planck-relics) to 10⁵ M_sun (LIGO stellar) to 10¹⁰ M_sun (SMBH-precursor). If the framework's B3 squeezing at k ~ 10⁻² to 10⁻¹ Mpc⁻¹ (CMB μ range) implies a k-dependent P_ζ enhancement at OTHER k_trans values corresponding to observable PBH masses, those windows provide cleaner falsifiers than FIRAS μ. This is an emergent computation not yet scoped.

### QUESTIONS

**Answer to T3.1** — Does M5's "F_amp^{sc} < 1 is sufficient" survive the B1/B2 separation?

**NO.** See D1 and the REVISED FRAMEWORK SURVIVAL CONDITION boxed above. Specifically: if UNIFIED-AS-79 delivers |α_3 + β_3|²(k_pivot) in the coherent limit (B2 phase-aligned constructive with B1), then F_amp^{sc} → 1 sends |β_2|² → 0, which gives |α_3 + β_3|² → |α_1 + β_1|² = S_IC^{B1} ≈ 1.636×10⁵ at k_pivot. The framework's A_s at k_pivot still overshoots by ≥ +4 OOM even with F_amp^{sc} = 1. F_amp^{sc} < 1 is INSUFFICIENT. 

What IS sufficient: either (a) the composed phase happens to be destructive so that |α_3 + β_3|² << |α_1 + β_1|² (a measure-zero-looking coincidence unless pinned by a principle we haven't identified), OR (b) the continuous B3 computation reveals that eta_end (where S_IC is extracted at s78-E) is not the physical endpoint and further post-fold evolution damps the squeezing, OR (c) the full UNIFIED-AS-79 pipeline shows the squeezed state at horizon exit has a MUCH smaller |α_3 + β_3|² than S_IC at eta_end because of the horizon-exit projection onto long-wavelength curvature perturbation (a conformal-time projection that is ledger-invisible). Option (c) is the cleanest structural hope.

**Answer to T3.2** — Chluba kernel binding scale.

My M1 FIRAS estimate used a k-weighted (dk/k) integral with a FLAT effective kernel — that is, treated W_Chluba as ~ constant across [1, 10⁴] Mpc⁻¹. This is a CRUDE approximation. The physical Chluba-Sunyaev μ Green's function (see Chluba 2013 MNRAS 434, 352; Chluba-Khatri 2014 MNRAS 444, 2870) has a MULTIPLICATIVE window:

    W_μ(k) ≈ 2.27 × [exp(−(k/k_D(z_μ))²) − exp(−(k/k_D(z_th))²)]

with k_D(z_μ) ≈ 46 Mpc⁻¹ (diffusion scale at onset of μ regime, z ~ 2×10⁶) and k_D(z_th) ≈ 10⁴ Mpc⁻¹ (thermalization scale, z ~ 2×10⁵). The window PEAKS near k ~ 740 Mpc⁻¹ (geometric mean of the two diffusion scales).

**Kernel shift changes the binding scale from k ~ k_pivot (transit's direct-scan reading) to k ~ 740 Mpc⁻¹ (kernel peak)** — a factor ~1.3×10⁴ shift. At k = 740 Mpc⁻¹, under transit's empirical UV slope −1.33 for |β|² extrapolated (caveat: empirical slope is measured on k/k_pivot ∈ [1, 10]; extending to k/k_pivot = 1.3×10⁴ is extrapolation across 3 additional decades), |β|²(740 Mpc⁻¹) extrap ~ 4.3×10⁴ × (1.3×10⁴)^{−1.33} ~ 0.02. This is << 1. At the kernel PEAK, the framework's S_IC contribution is SUPPRESSED, not amplified.

**Does the kernel suppress or amplify the k_pivot peak**: SUPPRESSES. W_μ(k_pivot) / W_μ(740 Mpc⁻¹) ≈ exp(−(0.056/46)² − ...) ≈ 0 — the μ kernel has essentially ZERO coupling at k_pivot (it's in the y-distortion free-streaming regime). The k_pivot peak is suppressed by the kernel; the binding contribution shifts up-k by ~4 decades to the kernel peak.

**Implication**: my M1 "binding scale is k_pivot" claim is WRONG when the proper Chluba kernel is applied. Transit's T1 "FIRAS integrand dominated by k ≈ k_pivot" is also WRONG under the proper kernel. Both of us used effectively-flat kernel approximations that inflate the k_pivot contribution. The correct binding scale is k ~ 740 Mpc⁻¹, where the UV fall-off envelope gives |β|² << 1. FIRAS survival is therefore MORE PLAUSIBLE than either of our R1 readings suggested — the framework may already pass FIRAS under the proper kernel.

**This is a substantial carry-forward for S79**: S79-CHLUBA-KERNEL-FIRAS must integrate the UNIFIED-AS-79 |α_3 + β_3|²(k) output against the correct Chluba-Sunyaev W_μ(k) on [1, 10⁴] Mpc⁻¹, using the Chluba 2013 analytic approximation or the CLASS/CAMB spectral-distortion module. Without this computation, neither our R1 overshoot claims nor any "FIRAS survival" claim has numerical grounds.

**Answer to T3.3** — dn_s/d ln k urgency vs other channels.

With the corrected framework number −0.01430 (4.90σ CMB-S4 detection, not 16σ), dn_s/d ln k SHIFTS FROM "near-term kill shot" TO "confirmation-pending discriminator." It is still a >3σ discriminator at CMB-S4, but it is no longer the singular cheapest test.

Sharper near-term channels at CMB-S4 timescale (2033-2034):

1. **LiteBIRD r detection**: framework predicts r = 0.0242 (pre-registered, permanent). LiteBIRD sigma = 0.001, giving 24σ detection. This is a **necessary-not-sufficient** test — r = 0.024 is consistent with slow-roll inflation, so detection doesn't UNIQUELY confirm the framework, but NON-DETECTION AT > 5σ falsifies the framework. Timeline 2033-2034, sharper statistical power than α_s.

2. **CMB-S4 n_s**: framework 0.9595 vs Planck 0.9649 ± 0.0042. CMB-S4 sigma ≈ 0.002 would tighten the gap to 2.7σ. If n_s converges to Planck central (0.9649), framework n_s prediction fails at 2.7σ — more decisive than the 1.3σ current tension. This is a structural test of the BCS + 1-loop geometry.

3. **Simons Observatory (SO) Stage-3 r**: sigma(r) ≈ 0.003, delivered ~2028. Lower statistical power than LiteBIRD but 5+ years earlier. r = 0.024 detection at SO would be 8σ.

4. **PIXIE or LiteBIRD-μ successor FIRAS successor**: the cleanest path to TEST the framework's direct prediction of P_ζ × S_IC at μ scales — not dn_s/d ln k shape, but direct amplitude. NASA PIXIE is not currently funded but if launched in the 2030s would push μ-distortion bound from 9×10⁻⁵ to ~10⁻⁸, which would either confirm the framework's O(10⁻⁴ to 10⁻²) prediction at 3-6 OOM or rule it out cleanly. **This is the FIRAS problem's natural resolution channel, not dn_s/d ln k.**

**Priority ordering for 2028-2034 observational discrimination**:
- (1) DESI DR3 (2027, w_0/w_a): ALREADY the most decisive near-term, see pre-registered-observations.md line 65 "Framework survives if w_a > −0.35."
- (2) SO Stage-3 r (2028): detection at 8σ, structural test of fold impulse.
- (3) CMB-S4 n_s (2033): 2.7σ test of BCS + 1-loop.
- (4) CMB-S4 dn_s/d ln k (2033): 4.9σ test of stiff-to-dS transfer (Route 2).
- (5) LiteBIRD r (2034): 24σ test, necessary-not-sufficient.

dn_s/d ln k is position #4, not #1 as I originally claimed. Revise my M3 priority accordingly.

**Answer to T3.4** — LIGO/Virgo at k_trans; next-generation instruments.

k_trans = 3.36×10⁻³ Mpc⁻¹ corresponds to a PBH mass (Carr press) M_PBH ≈ 10²⁰ M_sun — ultra-supermassive. Current GW interferometers (LIGO/Virgo, Einstein Telescope, DECIGO) target MUCH smaller mass windows:

- **LIGO O5 / A#** (10⁻²⁴ to 10⁻²¹ Hz): stellar-mass PBH ~ 1-100 M_sun — 20+ OOM below k_trans prediction.
- **Einstein Telescope** (2035+, 1-1000 Hz): 0.1-10⁴ M_sun — 16+ OOM below.
- **DECIGO** (mHz): 10⁴-10⁷ M_sun — 13+ OOM below.
- **LISA** (mHz, 2035+): up to ~10⁸ M_sun via MBH merger ringdowns — 12 OOM below k_trans prediction.

No current or near-future GW instrument reaches 10²⁰ M_sun. The k_trans PBH prediction falls OUTSIDE the observable mass window of all pre-registered GW experiments.

**However**, two escape routes for observational sensitivity:

(a) If the framework's B3 squeezing at k ∈ [10⁻¹, 10²] Mpc⁻¹ produces ENHANCED P_ζ at the stellar-mass PBH window (M ~ 1 M_sun ↔ k ~ 10⁶ Mpc⁻¹ deep UV, out of reach; M ~ 10⁵ M_sun ↔ k ~ 10² Mpc⁻¹, reachable), LIGO stellar-mass PBH non-detection (f_PBH(M ~ 10 M_sun) < 10⁻³) constrains the P_ζ enhancement at k ~ 10² Mpc⁻¹ by ~3 OOM. The framework's |β|² envelope at k ~ 10² Mpc⁻¹ under slope −1.33 is ~10 — which predicts P_ζ enhancement ~10 at that scale, potentially in tension with LIGO stellar-mass PBH non-detection if f_PBH bounds tighten.

(b) **Stochastic GW background** from domain walls: the framework's LISA GW prediction Ω_GW ~ 10⁻¹⁰ (S59, see MEMORY.md project_lisa-gw-prediction) is from CG(24) domain walls, NOT from PBH. If LISA detects Ω_GW ~ 10⁻¹⁰ at mHz with the right shape (power-law, specific break frequency), this is a separate framework confirmation independent of PBH/FIRAS.

**Net T3.4 answer**: the 10²⁰ M_sun PBH prediction is OBSERVATIONALLY UNTESTABLE by current or planned GW instruments. But the framework's |β|² running across k_trans ~ 10⁻³ to k ~ 10² Mpc⁻¹ DOES cross observable PBH mass windows (stellar, intermediate) and these provide independent constraints on P_ζ(k) at intermediate k that neither CMB FIRAS nor k_trans PBH covers. The S79 extended k-scan (E4 above) should report predicted P_ζ × S_IC at k ∈ [1, 10⁶] Mpc⁻¹ against LIGO stellar PBH, microlensing (HSC, OGLE), and sub-solar asteroid-mass PBH windows.

**Answer to T3.5** — Substrate PBH at k_trans = population properties?

Substrate framing pin: a PBH at k_trans in the phonon-first framework is a **local condensation of GGE relic spectral weight** at scales where the post-fold dS pump has produced sufficient density contrast that the phononic interference pattern self-organizes through the a_2 Seeley-DeWitt gravitational channel into a localized eigenstate bundle. It is NOT a gravitational collapse of pre-existing overdensity in FRW.

**Population signatures that differ from generic early-universe processes**:

(a) **Spin distribution**: GGE relic quasiparticles are CPT-neutral (AZ class BDI, permanent result). Accretion of phononic excitations onto a PBH-as-spectral-condensation proceeds in symmetric pair channels — the Leggett-channel quasiparticles. Net spin at formation = 0 (not generic inflationary PBH which can have small non-zero spin from tidal torques). **Prediction: dimensionless spin parameter a_* ≈ 0 at formation for substrate PBHs**, distinct from standard primordial or stellar-collapse populations.

(b) **Clustering**: the fold's |β|² pair-production spectrum at k_trans correlates k and −k modes (two-mode squeezing). In the substrate picture, PBHs forming from this pair-creation inherit a **two-point correlation** in initial seed positions — pairs separated by wavelength ~ k_trans⁻¹ ≈ 300 Mpc. This predicts an enhanced two-point correlation in the supermassive PBH population at scales ~300 Mpc that would be observable IF the population were dense enough and IF we had a tracer (which we don't for 10²⁰ M_sun ultra-supermassive).

(c) **Mass function**: standard Carr press predicts a log-normal mass function. In the substrate framework, the mass function is set by the B3 squeezing envelope |α_3 + β_3|²(k) integrated over the Carr press window. If the envelope follows slope −2.19 from k_pivot → kernel peak, the mass function slope is ALSO tilted, predicting a specific power-law deviation from log-normal. **This is computable and distinguishable**, IF we had observations of the relevant mass window.

(d) **Dark matter contribution**: if ultra-supermassive substrate PBHs at 10²⁰ M_sun exist, they contribute to Ω_DM at a fraction f_PBH = ρ_PBH/ρ_DM determined by the integrated P_ζ × S_IC at k_trans. The Leggett-channel quasiparticle DM (permanent prediction, see MEMORY.md framework-status) contributes the BULK of Ω_DM; substrate PBHs are an ADDITIONAL component, NOT a replacement. This is testable by dynamical constraints on ultra-supermassive dark compact objects (rotation curves on supercluster scales, gravitational lensing surveys) — at current precision, these are weak constraints but Euclid weak lensing at clustering scales ~100-1000 Mpc could probe the two-point correlation from (b) above.

**Substrate-specific falsifiability**: population property (a) — zero-spin at formation — is a **structural, substrate-specific prediction** that distinguishes substrate PBHs from standard inflationary PBHs. No current instrument probes supermassive black hole spin at formation epochs (we observe only AGN-accreted post-formation spins), but future long-baseline BH imaging (ngEHT, ~2040s) could map sub-ngEHT-resolution SMBH spin distributions at high z. A population of a_* ≈ 0 SMBHs at z > 10 would be a substrate signature.

**Net T3.5**: substrate PBHs at k_trans carry THREE observationally distinct population signatures (zero-spin formation, paired clustering, tilted mass function) that differ from generic early-universe processes. None is accessible to current instruments at 10²⁰ M_sun, but the same population structure at accessible masses (stellar, intermediate, SMBH) is probed by LIGO/Virgo stellar-mass, HSC/OGLE microlensing, and Euclid weak lensing. The framework makes population predictions; they are specific and falsifiable at the RIGHT mass/scale combinations, not at 10²⁰ M_sun directly.

---

### Sharper follow-ups for transit's final turn (R2 Turn B)

**Q1 (for transit's R2)**: Under UNIFIED-AS-79 with continuous trajectory from pre-fold SS through fold + post-fold dS to horizon exit, what is the expected scaling of |α_3 + β_3|²(k_pivot) versus the ledger-composed product S_IC × F_amp ≈ 1.1×10⁹? If your prior-estimate range is [1.7×10⁻⁹, 1.96×10⁻⁶] (per P2-A T1 provisional), is there an intermediate structural argument — e.g., a WKB matching condition at eta_end — that narrows this range BEFORE the computation runs? Specifically: does the conformal-time projection at horizon exit bring a factor (aH/k)^{n_s−1} × (k^3/2π²) that suppresses |v|²/z² relative to the eta_end-extracted S_IC by a computable amount?

**Q2 (for transit's R2)**: Your T1 scan data shows S_IC is oscillatory in k (jumps factor 10-100 between adjacent k at fixed eta_end). Is this oscillation DAMPED when the endpoint is shifted from eta_end (subhorizon) to horizon-exit eta_exit (N_pivot = 3 e-folds)? Specifically: does the post-fold dS evolution smooth out the phase oscillation, or does it preserve it? If preserved, the FIRAS integral under the Chluba kernel will depend sensitively on k-binning, and the current scan's 14 k-values may not be dense enough.

**Q3 (for transit's R2)**: The S79-CHLUBA-KERNEL-FIRAS computation I specified (extending UNIFIED-AS-79 scan to k ~ 10⁴ Mpc⁻¹ = 1.8×10⁵ × k_pivot, with Chluba-Sunyaev W_μ(k)) requires the mode equation to be tractable in the deep-UV asymptotic regime where WKB is valid but the pump z''/z is effectively zero (fold impulse in the past, dS negligible). Is this computationally tractable on the existing DOP853 integrator, or does the deep-UV oscillation time scale (~ 1/k) force adaptive-step failures for k > 10³ × k_pivot? If tractable, what is the computation budget estimate (minutes-to-hours)?

**Q4 (for transit's R2, shorter)**: Your T2 closure of the tachyonic-Airy-matching principle uses z''/z ≡ 0 strictly in the pre-fold substrate. Does this hold IF the pre-fold substrate admits a small tachyonic residual from GGE relic pre-fold dynamics (e.g., from a pre-fold phase of substrate equilibration that itself had a small pump)? Or is "z''/z ≡ 0 pre-fold" a **structural axiom** of the phonon-first substrate that cannot be relaxed without changing the framework's definition?

**Q5 (for transit's R2, on carry-forward priority)**: Given the B1/B2 decomposition + Chluba kernel shift, the S79 priority order should be:
 - (P1) UNIFIED-AS-79 at k_pivot (resolves A_s amplitude, B3 phase composition at CMB scale)
 - (P2) UNIFIED-AS-79 on extended k grid to k ~ 10⁴ Mpc⁻¹ (resolves FIRAS μ against Chluba kernel)
 - (P3) BACKWARD-BD-CONSISTENCY at k_pivot (closes IC-principle escape hatch formally)
 - (P4) S79-CHLUBA-KERNEL-FIRAS integral (requires P2 output + kernel library)

Do you agree with this ordering, or should UNIFIED-AS-79 be run on the extended k grid from the start (P1+P2 as one computation)?

(4-tuple tag applies to all numerical claims in R2A: CMB pivot or scan k, POWER-RATIO, |α+β|², L_max=10, IC=spectral stationarity unless otherwise specified. Gate verdicts W1-E FAIL, W3-E-1 FAIL, W3-E-2 FAIL UNCHANGED.)

---

## Round 2 — transit: Cross-Synthesis (FINAL)

### CONVERGENCE

**C1 — Accept mack's Chluba kernel finding (D2) with quantitative sharpening.** The Chluba-Sunyaev μ-distortion Green's function has been verified directly. The analytic window function (Chluba 2012, ApJ 758, 76 Eq. 10; Chluba 2013, MNRAS 434, 352) is

> W_μ(k) ≈ 2.27 × [exp(−k²/k_D²(z_th)) − exp(−k²/k_D²(z_μ))]

with k_D(z_μ) ≈ 46 Mpc⁻¹ (lower diffusion cutoff — modes below this redshifted into the y-distortion epoch) and k_D(z_th) ≈ 10⁴ Mpc⁻¹ (upper thermalization cutoff — modes above this erased by double-Compton). I solved d/dk [W_μ] = 0 exactly and find **k_peak = 151 Mpc⁻¹** — the kernel is essentially unit-amplitude ON A PLATEAU k ∈ [100, 3000] Mpc⁻¹, NOT sharply peaked at 740 Mpc⁻¹. Mack's quoted 740 Mpc⁻¹ is the geometric mean of the two diffusion scales (679 Mpc⁻¹) — CLOSE to the plateau center but not the location of the exact maximum. Both readings land within the plateau.

Direct numerical evaluation with my UV envelope |β|²(k) = 4.26×10⁴ · (k/k_pivot)^{−1.331} and S_IC(k) = 1.636×10⁵ · (k/k_pivot)^{−2.192}, anchored at k_pivot = 0.056 Mpc⁻¹:

| k (Mpc⁻¹) | k/k_pivot | \|β\|² (UV-extrap) | S_IC (UV-extrap) | W_μ(k) | W_μ · S_IC |
|:---------:|:---------:|:----------------:|:----------------:|:-------:|:----------:|
| 46 | 8.2×10² | 5.63 | 6.68×10⁻² | 0.632 | 4.22×10⁻² |
| 100 | 1.79×10³ | 2.00 | 1.22×10⁻² | 0.991 | 1.21×10⁻² |
| 150 | 2.68×10³ | 1.17 | 5.01×10⁻³ | 1.000 | 5.01×10⁻³ |
| 300 | 5.36×10³ | 0.46 | 1.10×10⁻³ | 0.999 | 1.09×10⁻³ |
| 740 | 1.32×10⁴ | 0.14 | 1.52×10⁻⁴ | 0.995 | 1.51×10⁻⁴ |
| 1000 | 1.79×10⁴ | 0.093 | 7.83×10⁻⁵ | 0.990 | 7.75×10⁻⁵ |
| 3000 | 5.36×10⁴ | 0.022 | 7.05×10⁻⁶ | 0.914 | 6.44×10⁻⁶ |

At every k inside the Chluba plateau, S_IC(k) is SUB-UNITY. |β|²(k) crosses below 1 at k ≈ 200 Mpc⁻¹ — inside the Chluba band center. S_IC peaks at ~5×10⁻³ at the kernel peak (k = 150) and drops to 1.5×10⁻⁴ at mack's cited 740. This is the substantive sharpening of mack's D2: **S_IC(k) is NOT just small at the Chluba binding scale, it is already sub-unity across the entire Chluba plateau under the empirical UV slope**. (4-tuple tag: scan-extrapolated, POWER-RATIO, |α+β|², L_max=10, IC=spectral stationarity, fixed eta_end=1.229.)

**C2 — Accept the revised FIRAS μ numerics.** With the Chluba-kernel-weighted integral

> μ = 2.27 × ∫ d(ln k) · P_ζ(k) · S_IC(k) · W_μ(k)/W_peak

over k ∈ [10, 3×10⁴] Mpc⁻¹, I compute:

- **P_ζ(k_pivot) = A_s^{observed} = 2.1×10⁻⁹** (post-conversion, framework matching CMB): **μ = 6.17×10⁻¹⁰**. Ratio μ/bound = 6.85×10⁻⁶ — **PASS by 5.16 OOM**.
- **P_ζ(k_pivot) = 9.81×10⁻⁴** (raw framework P_dS × f_conv, pre-S78 W1-A conversion): **μ = 2.88×10⁻⁴**. Ratio μ/bound = 3.20 — **FAIL by 0.50 OOM** (factor 3.2 overshoot, not 221).

The 221× overshoot in mack's M1 capped reading collapses under the proper kernel to factor 3.2 in the worst case (raw framework P_ζ, no conversion) and **factor 0.0000068 in the best case** (framework matches observed A_s). Both readings are improvements over the flat-kernel +2.35 OOM benchmark by at least 2 OOM; under the observed-A_s reading the framework PASSES FIRAS at 5+ OOM margin.

**The Chluba kernel is the single most important methodological correction to come out of Round 2.** The "+4.4 OOM wrong-sign PBH/FIRAS" headline from W3-E was a flat-kernel artifact. The W3-E FAIL gate verdict stands as a CALCULATION record (the computation used an unweighted integrand extrapolated from a factor-3 baseline), but the OBSERVATIONAL IMPLICATION is materially softened. Gate verdicts are permanent; the physical inference they supported is not.

**C3 — Accept two-stage survival structure E1 as governing framework.** The B1 UV envelope check (my UV slope −2.19 for S_IC, directly scanned) is the first test; the B3 phase-alignment check at k_pivot (whether fold + post-fold compose constructively or destructively) is the second. They are independent. The Chluba kernel makes TEST 1 much easier than the flat-kernel reading: at the kernel peak, |β|² ~ 1 and S_IC ~ 5×10⁻³ on the empirical envelope — a factor > 10⁷ reduction from the S_IC(k_pivot) = 1.6×10⁵. TEST 2 remains to be computed by UNIFIED-AS-79.

**C4 — Accept dn_s/d ln k priority #4 ordering.** With the corrected framework number −0.01430 (Route 2 stiff-to-dS transfer, S76 B3-ALPHA-S-RECON) and CMB-S4 sigma = 0.002 at 2033, the detection significance is |−0.01430 − (−0.0045)|/0.002 = **4.90σ** (mack) vs |framework − LCDM_slow_roll|/0.002 = **4.65σ** (transit, using |framework| displaced above LCDM slow-roll limit). Both self-consistent. Ordering ahead of it: DESI DR3 (2027), SO Stage-3 r (2028), CMB-S4 n_s (2033). LiteBIRD r (2034) is the large-sigma-ratio discriminator at 24σ — NECESSARY-not-sufficient for framework, but NON-DETECTION at >5σ would falsify. (4-tuple tag: CMB pivot, POWER-RATIO, |α+β|², L_max=10, IC=Route-2.)

**C5 — Accept B1/B2 separation as the canonical decomposition.** From P2-A convergence + C4 of this workshop + mack's C4/C5: B1 is the fold impulse (|β_1|² ~ 4.3×10⁴ per mode at k_pivot, drives A_s and FIRAS amplitude problems); B2 is the post-fold stiff-to-dS transfer (|β_2|² ~ 1.7×10³, drives n_s and dn_s/d ln k shape observables). The framework's shape PASS and amplitude FAIL are NOT a single failure; they ride different Bogoliubov stages with a 25× ratio of their per-stage squeezings. P1-1 E1 applies to 4 of 5 S78 channels (W1-C, W1-E, W3-E, W1-D), not all 5; the n_s observable is off this cascade.

**C6 — Accept UNIFIED-AS-79 as the rate-limiting S80 deliverable.** This is mack's C6 + P2-A convergence. The computation subsumes the S79-DIRECT-S_IC-K-GRID (sampling S_IC on a FIRAS grid) and the Chluba-kernel-weighted integral simultaneously. Execute in one pipeline; report |α_3 + β_3|²(k) at 16+ k values plus the μ-integral.

### DISSENT

**D1 — Where I reserve against mack's D2 quantitative endorsement.** Mack's D2 writes "|β|²(740 Mpc⁻¹) extrap ~ 0.02" — this is roughly correct (my exact value 0.14 at k = 740; mack's 0.02 is within factor 7 and qualitatively consistent with sub-unity). But the **broader claim that FIRAS μ integral is < 10⁻⁶** under the Chluba kernel is TRUE ONLY IF framework P_ζ(k_pivot) is taken at the observed A_s value ≈ 2×10⁻⁹. If framework P_ζ is taken at the RAW pre-conversion value (P_dS × f_conv = 9.81×10⁻⁴, per S77), then μ ≈ 2.9×10⁻⁴ — a **factor 3.2 overshoot**, not a factor 10⁻⁶ clearance. The framework's FIRAS survival is THEREFORE CONTINGENT on the A_s conversion closing (i.e., on UNIFIED-AS-79 delivering B3 = observed A_s, which is the P2-A outstanding gate). If UNIFIED-AS-79 delivers B3 = 4.26×10⁻⁸ (lizzi's single-factor reading), the ratio to observed is ~20× and μ ~ 20 × 2.88×10⁻⁴ ~ 6×10⁻³ — **overshoots FIRAS bound by 70×**.

**Short form**: FIRAS survival is yoked to A_s closure. If A_s closes (conversion reaches observed), FIRAS clears at 5+ OOM margin. If A_s is 1.3 OOM high (P2-A current ledger), FIRAS overshoots by factor ~70. **FIRAS and A_s are NOT independent tests under the proper kernel — they are the same normalization problem at different k windows.**

**D2 — Reservation against treating W3-E FAIL as a "false alarm".** The W3-E gate verdict stands as PERMANENT (per workshop convention pins), and the ledger-level FAIL was methodologically correct at the time (it used the S_IC slope inferred from a factor-3 k-baseline, which is not physically supported across 6 decades). The Chluba kernel correction does NOT overturn the gate — it reinterprets its observational meaning. The framework's W3-E value of P_ζ × S_IC >> bound remains a structural fact AT k_pivot; the Chluba kernel simply says k_pivot is NOT the binding scale for FIRAS, so the W3-E-1 FAIL is informative but not observationally decisive. This is a clean case of gate methodology delivering a structural finding whose observational interpretation depends on the proper weighting kernel — mack's D2 is the right resolution, but the gate is not "withdrawn".

**D3 — Minor arithmetic reservation on mack's D2 W_μ(k) peak location.** Mack cites k_peak ≈ 740 Mpc⁻¹ as geometric mean of 46 and 10⁴. The EXACT peak of W_μ(k) ≈ exp(−k²/k_high²) − exp(−k²/k_low²) is at k² = ln(k_high²/k_low²)/(1/k_low² − 1/k_high²), which gives **k_peak = 151 Mpc⁻¹** exactly. The function is essentially unit-amplitude on the PLATEAU k ∈ [100, 3000] Mpc⁻¹ (within 1% of maximum), not peaked sharply at 740. This matters because under the empirical UV slope −1.33, |β|²(151) ≈ 1.17 ≈ 1 crossover — the crossover from amplification to suppression sits AT the Chluba kernel peak, not above it. The framework's envelope is NEAR UNITY right where the kernel is maximal — a sharper test than mack's "|β|² ~ 0.02 at 740 Mpc⁻¹" suggests. The 3.2× overshoot in the raw-P_ζ case comes from this near-unity behavior at the plateau center.

### EMERGENCE

**E1 — The flat-kernel artifact is a 4+ OOM methodological lesson.** The W3-E FIRAS overshoot from +14 OOM (naive extrapolation, flat kernel) → +2.35 OOM (capped-at-1, flat kernel) → 0.5 OOM (UV envelope, Chluba kernel, raw P_ζ) → −5 OOM (UV envelope, Chluba kernel, observed A_s) is a four-step cascade where each step corrects a methodological over-estimation. The binding scale migrates from k_pivot (flat kernel) to k ~ 150 Mpc⁻¹ (Chluba kernel), where the framework's squeezed-state envelope has ALREADY decayed by ~7-8 decades. The observational tension was always a function of WHICH k was being integrated against WHICH kernel — not of the framework physics at k_pivot.

**This is the THIRD major Phase 2 reinterpretation** after P2-A's ledger retraction (A_s gap collapses +3 OOM → +1.3 OOM under B1/B2/B3 decomposition) and P2-C's route misidentification. Phase 2 has now resolved three structural misdiagnoses through structural analysis alone, without new physics. The flat-kernel artifact bears the same structural character as the IC-stitching artifact in P2-A: a naive composition of factors that looked observationally damning but was a bookkeeping error.

**E2 — The FIRAS constraint ties directly into the A_s conversion chain.** Under the Chluba kernel, FIRAS survival requires framework P_ζ(k_pivot) to match observed A_s = 2.1×10⁻⁹ within factor ~30 (my numerical threshold: μ_framework ≤ 9×10⁻⁵ at plateau S_IC ~ 10⁻³ requires P_ζ(k_pivot) ≤ ~3×10⁻⁵). Currently the P2-A UNIFIED-AS-79 ledger gives ~4×10⁻⁸ (factor 20 high) or ~2×10⁻⁶ (if composed); either way, the FIRAS window is yoked to the A_s pivot window by the k^{n_s−1} scaling of P_ζ and the S_IC(k) envelope. **FIRAS is NOT an independent test of the framework; it is the A_s test at a different k slice.**

**E3 — The substrate's PBH population signature is discriminable at the right mass window.** mack's answer to T3.5 gives three distinguishable signatures (zero-spin formation, paired clustering from two-mode squeezing, tilted mass function from B3 envelope slope). At the 10²⁰ M_sun mass predicted at k_trans, direct observation is impossible with current instruments — but the SAME POPULATION STRUCTURE at stellar (LIGO), intermediate (HSC/OGLE microlensing), and SMBH (ngEHT post-2040) windows tests the FRAMEWORK's B3 envelope at intermediate k. The |β|²(k) envelope passes through these observable windows as it runs from k_trans (10⁻³ Mpc⁻¹) to k_pivot (0.056 Mpc⁻¹) to k ~ 10⁶ Mpc⁻¹. A k-scan extended beyond the FIRAS window to LIGO PBH windows could test the ENTIRE envelope at once, not just the μ-distortion slice.

**E4 — The Chluba kernel is the observational "matching impedance" of the framework.** Under the phonon-first substrate picture, spectral distortions are a COUPLING EFFICIENCY between the post-fold GGE acoustic sector and the free-streaming photon bath. The Chluba kernel IS this coupling: k modes below 46 Mpc⁻¹ free-stream before dissipation (y-distortion regime, not μ); k modes above 10⁴ Mpc⁻¹ thermalize through double-Compton and are erased. The framework predicts acoustic pair density at ALL k from the fold, but only the k ∈ [46, 10⁴] Mpc⁻¹ slice COUPLES to the μ observable. This is analogous to a radio antenna with finite bandwidth — the framework's emission spectrum must OVERLAP the instrument's response. The flat-kernel reading ignored this overlap; the Chluba kernel enforces it. Mack's D2 essentially identified that the observational "instrument" has a narrow k bandpass that the framework's UV envelope has ALREADY decayed into.

---

### Answers to mack's 5 follow-up questions (Q1-Q5)

**Q1 — |α_3 + β_3|²(k_pivot) scaling under UNIFIED-AS-79**: the pre-conversion range spans 5 OOM [2×10⁻⁹, 2×10⁻⁶] under lizzi's single-factor vs coherent-composed readings (P2-A T1). A structural narrowing argument exists: the conformal-time projection at horizon exit projects the mode v_k onto the curvature perturbation ζ = v_k/z via division by z(η_exit) = a(η_exit) · (ε/c_s)^{1/2} · M_Pl, and z evolves exponentially in the post-fold dS phase. Specifically: between η_end (subhorizon, where S_IC is extracted at k²·c² ≈ z''/z peak) and η_exit (k/(aH) = 1), z grows by factor a(η_exit)/a(η_end) ≈ e^{N_pivot} ≈ e^{3.12} ≈ 22.6 in the stiff-to-dS transition. The curvature spectrum P_ζ(k_pivot) = |v_k|²/z² at η_exit, while S_IC measures |α+β|² at η_end without this projection. The net projection factor is a²(η_end)/a²(η_exit) × (c_s(η_end)/c_s(η_exit))^{−1} — in sudden-transition limit this factor is O(1), but in smooth-transition limit it can suppress by 100-1000×. THIS IS A STRUCTURAL FACTOR NOT VISIBLE IN THE S_IC×F_amp LEDGER. Pre-register: UNIFIED-AS-79 reports both |α+β|² AT η_end and P_ζ AT η_exit, and their ratio quantifies the projection suppression.

**Q2 — Is S_IC oscillation in k damped by post-fold dS evolution?** The oscillation in my T1 scan (factor 10-100 jumps between adjacent k at fixed η_end) is a PHASE OSCILLATION: the argument of (α_k + β_k) rotates with k at fixed η_end, producing periodic constructive/destructive interference. In post-fold dS, the mode freezes superhorizon: v_k/z → constant for k/(aH) → 0. The phase rotation is ARRESTED at horizon crossing. Therefore the oscillation at η_end gets PARTIALLY FROZEN at η_exit — the k values where |α+β|² was near its peak at η_end stay near their peak at η_exit; the k values where |α+β|² was near a trough stay near the trough. The oscillation is NOT damped (superhorizon freezing is conservative in |α+β|²), but it is arrested. FIRAS integration across this oscillation averages out to a MEAN envelope close to the smoothed slope −2.19 — k-binning matters to within factor ~3 per bin, not to within factor ~100 as the extreme oscillation at η_end might suggest. Recommendation: use 30+ log-spaced k values across k ∈ [k_pivot/10, 3×10⁴ Mpc⁻¹] for the UNIFIED-AS-79 FIRAS integral. Cost ~1 hour per k-value with DOP853 → 30 hours total.

**Q3 — Is extending UNIFIED-AS-79 to k ~ 1.8×10⁵ × k_pivot computationally tractable?** YES, with one adjustment. The DOP853 adaptive step sizes to 1/k in the oscillatory regime, so deep UV modes require proportionally smaller time steps. For k/k_pivot ~ 10⁴, the step count grows by factor 10⁴. At 100 k-values × 10⁴ steps/value × 10 μs/step ≈ 10 seconds per k — TRACTABLE. The actual bottleneck is BOUNDARY CONDITIONS: at k > 10³·k_pivot, the mode is DEEP subhorizon at ALL relevant η (pre-fold through post-fold) and the mode equation has no interesting structure — the mode is BD vacuum throughout. The physically interesting integration range is k/k_pivot ∈ [0.01, 10³], covering the Chluba plateau and its shoulders. Beyond that, |α+β|² ≈ 1 by the adiabatic theorem (ω'/ω² ≪ 1). Total cost estimate: 10-20 core-hours on the existing DOP853 pipeline. FEASIBLE for S80.

**Q4 — Does z''/z ≡ 0 pre-fold hold against small residual GGE pre-fold dynamics?** This is a STRUCTURAL AXIOM of the phonon-first substrate, not an approximation. The substrate's definition is that the D_K eigenvalue spectrum IS the substrate; there is no pre-fold "pump" because there is no pre-fold FRW. The fold is the FIRST dynamical event in the substrate's history — before it, the substrate is in stationary GGE equilibrium on the Jensen-deformed D_K spectrum. Any "pre-fold pump" would require the substrate to evolve prior to the fold, which contradicts the framework's phonon-first framing. If one allows a small residual (e.g., pre-fold τ-drift before equilibrium), the scale of that drift is set by OTHER Jensen deformations of D_K, which have been established as O(10⁻¹¹³) suppressed (S75 R-B-K-RUNNING, frozen spectrum theorem). So even with residual dynamics, z''/z pre-fold ≲ 10⁻¹¹³ — effectively zero for any mode equation calculation. The T2 closure holds robustly.

**Q5 — S79 priority ordering**: I AGREE with mack's ordering (P1) UNIFIED-AS-79 at k_pivot, (P2) extended k-grid to k ~ 10⁴ Mpc⁻¹, (P3) BACKWARD-BD-CONSISTENCY, (P4) S79-CHLUBA-KERNEL-FIRAS. **BUT I WOULD COMBINE P1 AND P2** into a single pipeline run: the DOP853 integrator with consistent pre-fold SS IC and post-fold horizon-exit extraction should sample the full k-grid in one execution, producing |α_3 + β_3|²(k) on a dense k array. This avoids the artifact of running P1 at one k then extrapolating, and delivers the FIRAS integral directly. The cost is ~10-20 core-hours for 30-50 k-values (per Q3), which is < 1 day of compute. P3 (backward consistency) is a quick validation subroutine (~20 min). P4 (kernel integral) is a trivial post-processing of the P2 output (seconds). Combined: **UNIFIED-AS-79-FULL** as the sole S80 top-priority computation, subsuming P1 + P2 + P4, with P3 as a validation cross-check.

## Workshop Verdict

| # | Topic | Source | Status | Key Insight |
|:--|:------|:-------|:-------|:------------|
| 1 | PBH/FIRAS observational damage | M1, Re:M1, D2-R2, C1-C2-FINAL | **Partial** (R2 reframe) | Flat-kernel +2.35 OOM overshoot is a methodological artifact; proper Chluba kernel band-passes k ∈ [46, 10⁴] Mpc⁻¹ where framework UV envelope has ALREADY decayed to S_IC ~ 5×10⁻³ at kernel peak (k ≈ 150 Mpc⁻¹, exact). Integrated μ = 6.17×10⁻¹⁰ under observed-A_s P_ζ (PASS at 5 OOM margin) or 2.88×10⁻⁴ under raw framework P_ζ (0.5 OOM overshoot). FIRAS is YOKED to A_s conversion, not an independent test. |
| 2 | IC principles all give amplification | M2, T2, Re:M2, C3-R2 | **Converged** | Five principles (Danielsson, Kim-Lee-Son thermal, entanglement-cooled, holographic UV-IR, tachyonic-Airy) all kinematically inadmissible at the fold's Mach 13.75 diabatic transit AND under the substrate's z''/z ≡ 0 pre-fold axiom. The 3 tested principles (SS, ME, AZ) converge at factor 1.13 because they project onto the same GGE-stationary pure state dictated by the mode equation dynamics. The IC-principle escape hatch is closed from 5 independent directions. |
| 3 | Fold as unified root observational reach | M3, Re:M3, C4-C5-R2 | **Converged** (refined) | Unified-root-|β|² ~ 10⁴ drives 4 of 5 S78 FAIL channels (W1-C, W1-E, W3-E, W1-D). n_s observable is OFF this cascade: it rides B2 stiff-to-dS transfer (|β_2|² ~ 1700, 25× smaller than B1). Shape-vs-amplitude split is a B1/B2 structural decomposition, not a coincidence. dn_s/d ln k = −0.01430 is CMB-S4 priority #4 at 4.90σ detection, not #1 as originally framed. |
| 4 | Three-principle factor 1.13 implication | M4, Re:M4 | **Converged** | Three IC principles agree because they all correctly identify the GGE-stationary pure state on the Jensen-deformed D_K spectrum. The α, β magnitudes are DICTATED by the mode-equation dynamics, not by IC choice. The axiomatic gap on IC is CLOSED permanently. Mixed-state escape is forbidden by phonon-first framing (substrate has nothing external to entangle with). |
| 5 | Survival conditions admissibility | M5, T1, Re:M5, D1-R2, E1-R2 | **Emerged** | Mack's original M5 claim (F_amp^{sc} < 1 necessary and sufficient) WITHDRAWN and replaced with two-stage structure E1: B1 UV envelope check at Chluba kernel peak + B3 phase alignment at k_pivot. Both independent, both required. Under Chluba kernel, TEST 1 PASSES at 5+ OOM margin if A_s converges; TEST 2 (horizon-exit projection factor a²(η_end)/a²(η_exit) via Q1 structural argument) is computable by UNIFIED-AS-79-FULL and is the rate-limiting S80 deliverable. |

Status categories: **Converged** | **Dissent** | **Partial** | **Emerged**

## Remaining Open Questions

1. **UNIFIED-AS-79-FULL mode-equation trajectory**: deliver |α_3 + β_3|²(k) on 30-50 log-spaced k-values across k ∈ [0.01·k_pivot, 10⁴ Mpc⁻¹] via single DOP853 pipeline from pre-fold SS through fold + post-fold dS to horizon exit. Report both η_end (S_IC) and η_exit (P_ζ) values. Quantifies B3 coherent-vs-destructive phase composition and delivers the Chluba-kernel-weighted μ integral directly. Pre-register: ratio P_ζ(η_exit) / S_IC(η_end) at k_pivot ∈ [10⁻³, 1] (conformal projection factor). **S80 priority #1.**

2. **Chluba-kernel FIRAS integral under UNIFIED-AS-79 output**: compute μ = 2.27 × ∫ d(ln k) · P_ζ(k) · |α_3 + β_3|²(k) · W_μ(k) with Chluba 2012 Eq. 10 kernel (k_D_low = 46 Mpc⁻¹, k_D_high = 10⁴ Mpc⁻¹) on the full k-grid. Pre-register: μ ≤ 9×10⁻⁵ (PASS) vs μ > 9×10⁻⁵ (FAIL, framework constrained to suppress raw P_ζ or increase B2-composition destructive phase).

3. **Direct W1-E k-scan at Chluba binding plateau**: extend my existing s79_w1e_k_scan_fixed_eta to include k/k_pivot ∈ [10, 10³] (physical k ∈ [0.56, 56 Mpc⁻¹], spanning the IR edge of the Chluba plateau). Validates or refutes the empirical UV slope −2.19 extrapolation used in the C1/C2 analytical integral. Pre-register: |β|²(k = 100 Mpc⁻¹) ∈ [0.5, 10] (empirical envelope holds) vs > 100 (envelope breaks; slope steepens IR of Chluba plateau).

4. **PBH population signature predictions at observable masses**: compute framework's B3 |α_3 + β_3|²(k) at PBH-mass windows — LIGO stellar (k ~ 10⁶ Mpc⁻¹ deep UV), HSC/OGLE microlensing (k ~ 10⁷ Mpc⁻¹), asteroid-mass (k ~ 10⁹ Mpc⁻¹). Under the UV envelope slope continuation, all these windows have |β|² ≪ 1 and predict f_PBH ≪ 10⁻³ — well below current bounds. Explicit: check if spin distribution (a_* ≈ 0 at formation from CPT-neutral AZ class BDI quasiparticles) is preserved under post-fold dynamics to the PBH mass windows accessible now.

5. **Phase-alignment k-scan test**: the B3 composed phase (constructive vs destructive) depends on k at fixed fold + stiff-to-dS parameters. Run UNIFIED-AS-79 at 5-10 k values near k_pivot (k/k_pivot ∈ [0.3, 3]) and examine the phase rotation of (α_3 + β_3)(k). If rotation crosses π over this k-range, phase-generic averaging vs phase-tuned constructive will differ by factor ~|α₃|·|β₃| ≈ 10⁴. Pre-register: phase rotation Δφ(k_pivot/3 → 3·k_pivot) ∈ [0, π/2] (phase-locked over pivot window) vs > π (phase-rotating; averaging converts the single-factor ledger value into the composed-product ledger value by phase integration).

6. **BACKWARD-BD-CONSISTENCY at k_pivot** (mack's M5 residual test): initialize mode in post-fold BD vacuum at η = 1, evolve backward through the fold to η_pre_start, extract α, β in SS basis. Pre-register: S_IC^{backward}(k_pivot) = 1.636×10⁵ to factor 2 (unitary evolution cross-check). ~20 min compute. Formal closure of Path (a) IC-principle escape.

7. **H_transit vs H_Friedmann tension at dS reinjection**: under Chluba-kernel reduction of FIRAS to PASS, the S77 W3-O f_conv double-counting question becomes material — does the framework's post-fold dS pump use M_Pl_reduced or M_KK as the Friedmann cascade scale? The normalization difference propagates to P_ζ directly. Pre-register: under M_Pl_reduced, UNIFIED-AS-79 B3 at k_pivot should give 2.1×10⁻⁹ to factor 30; under M_KK, factor 10⁴ off. This tests the substrate/FRW interface convention at the A_s pivot window.

8. **n_s running at stiff-to-dS interface (Route 2 microphysics)**: the S76 B3-ALPHA-S-RECON −0.01430 is currently a mean-field derivation (CW Route 3 is −0.019). Under UNIFIED-AS-79, compute dn_s/d ln k directly from 2-point finite-difference P_ζ(k ± δk)/P_ζ(k) at k_pivot. Pre-register: |framework − Planck| < 0.005 (2σ at Planck) vs > 0.005 (>2σ tension; Route 2 needs revision). Cost: trivial addition to UNIFIED-AS-79 output pipeline.

## Wrap-Up — Workshop Impact Summary

### What Changed

**The flat-kernel "FIRAS +2.35 OOM overshoot" headline is retracted.** W3-E's computation used an effectively unweighted k-space integrand to compare framework P_ζ × S_IC against the FIRAS μ bound. Under the physical Chluba-Sunyaev μ-distortion Green's function (Chluba 2012 ApJ 758, 76; Chluba 2013 MNRAS 434, 352), the μ observable is coupled to the primordial spectrum through a band-pass window W_μ(k) ≈ 2.27 × [exp(−k²/k_D²(z_th)) − exp(−k²/k_D²(z_μ))] that peaks at **k ≈ 151 Mpc⁻¹** (exact solution to d/dk W = 0; geometric mean k ≈ 679 is the mid-band value often quoted) and is ≥ 90% of maximum across k ∈ [100, 3000] Mpc⁻¹.

At the kernel peak, the framework's empirical UV envelope (measured directly in s79_w1e_k_scan_fixed_eta for k/k_pivot ∈ [0.5, 10], with S_IC slope −2.192 and |β|² slope −1.331) gives:

- **k = 151 Mpc⁻¹ (kernel peak, exact)**: S_IC = 5.01×10⁻³, |β|² = 1.17 (at crossover)
- **k = 740 Mpc⁻¹ (mack's cited peak, plateau center)**: S_IC = 1.52×10⁻⁴, |β|² = 0.14
- **k = 1000 Mpc⁻¹**: S_IC = 7.83×10⁻⁵

These are ALREADY sub-unity across the entire Chluba plateau — the framework's fold squeezing has decayed below the parametric amplification threshold before reaching the μ-distortion binding scale. Integrated μ with framework P_ζ(k_pivot) set to observed A_s = 2.1×10⁻⁹ gives **μ = 6.17×10⁻¹⁰**, PASSING the FIRAS bound 9×10⁻⁵ by 5.16 OOM. Under raw framework P_ζ(k_pivot) = 9.81×10⁻⁴ (unconverted), μ = 2.88×10⁻⁴, overshooting by factor 3.2 — a much softer tension than the 221× flat-kernel overshoot.

**The FIRAS constraint is YOKED to the A_s conversion**, not an independent test. If UNIFIED-AS-79 closes A_s (P_ζ at k_pivot reaches observed 2.1×10⁻⁹), FIRAS automatically passes at 5 OOM margin. If A_s overshoots by factor N, FIRAS overshoots by factor N × (μ_raw/bound) ≈ N × 3. The two constraints are not independent; they are the A_s test slotted into two different k windows.

**The P1-1 E1 "unified-root-|β|²" is refined to a 4-of-5 proviso**: the B1 fold impulse (|β_1|² ~ 4.3×10⁴ at k_pivot) drives W1-C, W1-E, W3-E, W1-D FAIL channels. The n_s observable rides B2 stiff-to-dS transfer (|β_2|² ~ 1700, 25× smaller) and is independent evidence. Shape vs. amplitude is a stage-separated structural split, not a correlated coincidence.

**The tachyonic-Airy-matching IC principle is KINEMATICALLY INADMISSIBLE under the phonon-first substrate** (z''/z ≡ 0 pre-fold, so ω² = k² > 0 for all k > 0). This strengthens mack's IC-principle closure from 4 to 5 independent directions; no standard-literature IC can give S_IC < 1 in the fold's diabatic regime.

### What Holds

**Gate verdicts PERMANENT**: W1-E (FAIL), W3-E-1 (FAIL), W3-E-2 (FAIL) stand. These remain methodologically correct CALCULATION records under their pre-registration conditions. The Chluba kernel correction does NOT retroactively change any of these; it changes the OBSERVATIONAL INTERPRETATION of what W3-E's FAIL means.

**The IC-principle axiomatic gap is permanently closed**. The substrate's phonon-first framing uniquely identifies the pre-fold state as GGE-stationary pure on the Jensen-deformed D_K spectrum (S75 "GGE freeze EXACT" result). All three IC principles tested (SS, ME, AZ) converge on this state up to CPT chirality, giving identical α, β magnitudes. No admissible 4th or 5th principle can change this.

**B1/B2/B3 Bogoliubov stage decomposition is the canonical framework** (from P2-A convergence + this workshop C5). All future computations must specify which stage is being measured. S_IC is a B1 quantity (pre-fold SS → post-fold WKB at η_end); F_amp is a B2 quantity (post-fold WKB at η_pf → horizon-exit WKB); P_ζ(k_pivot) is a B3 quantity (full trajectory to horizon exit). The composed product S_IC × F_amp is an APPROXIMATION to B3 valid only in coherent phase limits.

**The framework's shape observables (n_s = 0.9595, r = 0.024, dn_s/d ln k = −0.0143, f_NL < 5) remain PASS at their current tensions** (1.3σ, PASS, 1.46σ, PASS respectively). These are independent of the B1 amplitude problem and ride the B2 stage with its own structural provenance.

**Frozen spectrum theorem (S75)**: the Jensen-deformed D_K eigenvalue spectrum is frozen to 10⁻¹¹³ relative shift through the fold. No pre-fold pump of size > 10⁻¹¹³ M_KK² is admissible within the substrate framing, which closes the Q4 "residual GGE pre-fold dynamics" escape hatch robustly.

**UNIFIED-AS-79 remains the rate-limiting deliverable for S80**. P2-A and P2-B converge on this: one mode-equation pipeline from pre-fold SS IC through fold + post-fold dS to horizon exit, reporting P_ζ(k) on a dense k-grid. This subsumes A_s at k_pivot, FIRAS kernel integral, dn_s/d ln k, and the UV envelope validation simultaneously.

### What Breaks or Strains

**The 221× FIRAS overshoot narrative is STRAINED**. Under the proper Chluba kernel, the framework either PASSES FIRAS at 5 OOM margin (if A_s converges to observed) or overshoots by factor 3 (if A_s is 1.3 OOM high per P2-A ledger). Neither reading supports the original W3-E "+2.35 OOM wrong-sign" framing as an observational falsification. The gate verdict's observational implication has shifted from "framework inconsistent with FIRAS" to "framework consistent with FIRAS IF A_s closes."

**The single-factor A_s ledger reading (lizzi's P2-A 4.26×10⁻⁸)** is STRAINED by the FIRAS yoking. If single-factor were correct, framework μ = 4.26×10⁻⁸/2.1×10⁻⁹ × 2.88×10⁻⁴ ≈ 5.8×10⁻³ — overshoots FIRAS bound by factor 65. The FIRAS constraint therefore DISFAVORS the single-factor reading in favor of either (a) full B1/B2/B3 composed trajectory matching observed A_s, or (b) coherent-destructive phase at k_pivot that brings B3 ≈ observed. The composed-ledger reading (1.1×10⁹ × P_dS) is also disfavored — it overshoots by 14 OOM. The narrow target window is B3(k_pivot) ≈ 2.1×10⁻⁹ to factor ~30.

**The PBH/FIRAS "wrong-sign" framing is STRUCTURALLY MILDER than R1 suggested**. The framework's envelope does what one would expect from a Parker-pair production in a diabatic but finite-duration transit: |β|²(k) falls off as k^{−1.33} above the transit frequency scale 1/dt_transit ≈ 885 M_KK. The signature of this fall-off — S_IC decaying as k^{−2.19} and crossing unity at k ~ 370 Mpc⁻¹ — is the correct substrate behavior, not an observational inconsistency.

**Mack's M5 claim "F_amp^{sc} < 1 is necessary and sufficient for FIRAS survival" BREAKS** under the B1/B2 decomposition + Chluba kernel. Neither necessary (FIRAS survival doesn't require F_amp^{sc} < 1 because binding is at Chluba plateau where |β|² has already decayed) nor sufficient (even F_amp^{sc} = 1 leaves B1 fold squeeze at |β_1|² ~ 4×10⁴ at k_pivot, which can overshoot A_s by 5 OOM if phase composition is constructive). The REVISED survival condition is the two-stage E1 structure: B1 UV envelope + B3 phase alignment, BOTH independent, BOTH required.

**The "B1 fold impulse is the wrong answer" alternative** (i.e., the fold somehow produces a smaller |β|² than the mode equation predicts) is STRUCTURALLY FORBIDDEN by the diabatic transit's Mach 13.75, which is a geometric property of the substrate's Jensen spectrum-action gradient dS/dτ = +58,673, not a tunable parameter. The substrate cannot retune the fold without breaking 67/67 Baptista reproduction, block-diagonal theorem, Dynkin rank-2, etc.

### Carry-Forward Computations

**Ordering: highest-priority computations for S80. These MUST appear as planned computations in the S80 plan per the carry-forward rule.**

1. **UNIFIED-AS-79-FULL** (priority 1, rate-limiting for all other closures — same as P2-A)
   - What: Single DOP853 trajectory from pre-fold SS IC at η_pre_start through fold + post-fold dS to horizon exit
   - k-grid: 30-50 log-spaced k-values across k/k_pivot ∈ [0.01, 10⁵] (physical: 5.6×10⁻⁴ to 5.6×10³ Mpc⁻¹)
   - Output: |α_3|², |β_3|², |α_3 + β_3|² at η_end AND P_ζ(k) = |v|²/z² at η_exit for each k
   - Pre-register: P_ζ(k_pivot, η_exit) / S_IC(k_pivot, η_end) ∈ [10⁻³, 1] (conformal projection factor per Q1)
   - Cost: 10-20 core-hours
   - Subsumes S79-DIRECT-S_IC-K-GRID, S79-CHLUBA-KERNEL-FIRAS, dn_s/d ln k direct computation

2. **CHLUBA-KERNEL-FIRAS integral** (priority 2, post-processing of P1 output)
   - What: μ = 2.27 × ∫ d(ln k) · P_ζ(k) · |α_3 + β_3|²(k) · W_μ(k) with W_μ from Chluba 2012 Eq. 10
   - Pre-register: μ ≤ 9×10⁻⁵ (PASS) vs μ > 9×10⁻⁵ (FAIL)
   - Cost: seconds, given P1 output
   - Reports: μ value, contribution by k-decade, factor margin relative to bound

3. **Direct W1-E k-scan at Chluba plateau IR edge** (priority 3, validation)
   - What: Extend s79_w1e_k_scan to k/k_pivot ∈ [10, 10³] (k ∈ [0.56, 56 Mpc⁻¹])
   - Validates: empirical UV slope −2.19 for S_IC holds across the IR edge of Chluba plateau
   - Pre-register: |β|²(100 Mpc⁻¹) ∈ [0.5, 10] (slope holds) vs > 100 (slope breaks)
   - Cost: 2-4 core-hours

4. **PBH population signature k-scan** (priority 4, emergence of E3)
   - What: Report framework |α_3 + β_3|²(k) at PBH-mass windows: k ∈ [10⁴, 10¹⁰] Mpc⁻¹ for stellar LIGO, HSC/OGLE microlensing, asteroid-mass
   - Pre-register: f_PBH(M) from B3 envelope; verify |β|²(k) ≪ 1 at all observable PBH windows; spin distribution a_* ≈ 0 at formation from AZ class BDI CPT-neutrality
   - Three signatures: zero-spin, paired clustering (two-mode squeezing), tilted mass function
   - Distinguishable from inflationary PBHs at SMBH-formation epoch (ngEHT post-2040 probe)
   - Cost: shares P1 infrastructure; UV extrapolation of P1 output

5. **Phase-alignment k-scan at pivot window** (priority 5, E1 TEST 2)
   - What: Compute phase of (α_3 + β_3)(k) at k/k_pivot ∈ [0.3, 3], looking for Δφ rotation
   - Pre-register: Δφ < π/2 (phase-locked, single-factor ledger ≈ B3) vs Δφ > π (phase-rotating, composed ledger ≈ B3 under averaging)
   - Resolves P2-A T1 coherent-vs-destructive ambiguity
   - Cost: included in P1 output

6. **BACKWARD-BD-CONSISTENCY cross-check** (priority 6, formal closure)
   - What: Initialize mode in post-fold BD vacuum at η = 1, evolve backward through fold to η_pre_start, extract α, β
   - Pre-register: S_IC^{backward}(k_pivot) = S_IC^{forward}(k_pivot) = 1.636×10⁵ to factor 2 (unitarity check)
   - Formally closes Path (a) IC-principle escape
   - Cost: ~20 min

7. **H_transit vs H_Friedmann convention resolution** (priority 7, interface diagnosis)
   - What: Test whether UNIFIED-AS-79 uses M_Pl_reduced (S77 W3-O convention) or M_KK in the Friedmann cascade of post-fold dS
   - Pre-register: under M_Pl_reduced, P_ζ(k_pivot) ≈ 2.1×10⁻⁹ to factor 30; under M_KK, factor 10⁴ off
   - Resolves S77 W3-O f_conv double-counting ambiguity
   - Cost: parameter scan on P1 pipeline

### Closing Line

The +4.4 OOM FIRAS/PBH wrong-sign was not observational — it was the flat-kernel k-integral silently inflating the k_pivot contribution where S_IC is large, while giving no weight to the Chluba plateau at k ~ 100-3000 Mpc⁻¹ where the framework's UV envelope has already decayed to S_IC ~ 10⁻³ and the actual μ-distortion physics lives; three Phase 2 reinterpretations in as many workshops now trace to the same pattern — methodological artifacts that accumulated as structural headlines until the underlying structure was actually computed.
