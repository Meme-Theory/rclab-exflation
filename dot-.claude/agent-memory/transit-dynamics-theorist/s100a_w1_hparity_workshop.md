---
name: s100a-w1-hparity-workshop
description: S100a W-1 workshop outcome (H-parity theorem scope) — transit-side lessons, frozen Stage-0 candidate, sibling gate CF-S101-W1-QEQ-RELIC-ODDFLOOR, clock-blind/clock-keyed taxonomy, Mathieu width-vs-throughput correction
metadata:
  type: project
---

# S100a W-1 H-Parity Scope Workshop (volovik × transit) — outcome record

**Why:** the S100a-W1-2-QEQ-DRIVE FAIL (audit e31d45cf5309b32c..., PERMANENT) needed its SCOPE adjudicated; I steelmanned Reading B (non-equilibrium odd-in-H candidates) and the workshop converged fully. Canonical texts live in `sessions/session-100a/workshops/s100a-w1-hparity-scope-workshop.md` (E1 citation paragraph lines 937–941; E2 Stage-0 FROZEN 943–957; sibling spec in Carry-Forward block) — NOT here.

**How to apply:** cite the workshop file's E-blocks for any downstream text; apply the transit-side lessons below when designing resonance gates, clock conversions, or relic-bath couplings.

## Transit-side permanent lessons

1. **Mathieu width vs throughput (my Re:V4 error, D-2 corrected).** Parametric-instability tongue WIDTH is set by the FULL modulation depth h_par = q_osc/(λ_k² + q̄) — principal half-width δω/ω_d = h_par/4 at ω_d = 2ω₀ — NOT by the suppressed amplitude (φ_k) of whichever force component rectifies through the window. φ_k governs THROUGHPUT only. Never use amplitude suppression as the width parameter in a resonance guard. Adopted guard form: `Δ_res ≥ max(0.1, 5·h_par/4)`. n-th zone: 2E_k = n·ω_q^phys, width ∝ h_par^n (principal widest for h < 1; n=2 throughput extra-h-suppressed → report-only).
2. **Clock-blind vs clock-keyed observable taxonomy.** Under t = γτ (constant γ): every log-derivative slope is EXACTLY γ-invariant (time-axis instance of the math-scripts multiplicative-cancellation rule; the S97 `t_relax = 1.0 # sets units; cancels in slope` disclosure IS this identity; candidate K=4 corroborating corpus row, routed to orchestrator). Spectral POSITIONS (resonance 2E_k vs ω_q^phys = 59.888/γ) are the lineage's first clock-KEYED observables. Derived clock caveat: χ_I(q) gives weak τ-dependence; late tail q → 0⁺ ⟹ χ_I → const ⟹ asymptotic invariance holds.
3. **(q, ln a) geometric magnetism, closed by bath structure.** A fixed backbone promotes ln a to a second slow parameter — the gyroscopic class is NOT emptied by 1-dof counting (that algebra closes only the q̇-odd workless class). Closure: Berry curvature ≡ 0 EXACT for frequency-only modulation (X = E_k², Y = 0, Z = 1 slice — BdG anomalous terms are X–Z axis); squeeze-phase leakage O(φ_k) = 0.005–0.012 rad, pair-band rotation ≥ 2λ_min = 1.63948 M_KK (tighter than 2Δ_BCS ≈ 0.93), 1/√59.8 stacking; Iordanskii dies by C7 T^{0i}=0 EXACT + homogeneity.
4. **Pincer pattern (tail repeats the fold).** One shared parameter (γ) controls BOTH resonance position and window duration ⟹ regime corners self-delete: below-band forces γ ≥ 36.53 M_KK⁻¹ ⟹ Δt(window) ≈ 4.8–9.5 vs t_therm ≈ 6 M_KK⁻¹ ⟹ thermalized double-lock. Two self-consistent end-states only: {above-band & frozen} XOR {in-band: live}. Same logical shape as R_therm = 5251.82 classifying the fold.
5. **Three-selector slope rule (permanent record form).** Equilibrium analyticity → even integers; amplitude self-consistency → 1 (|H| non-analytic-even); SECULARITY suppresses everything else, failure window = parametric resonance. Pre-filter: parity + analyticity + secularity, three lines before any ODE.

## Pre-registered forward gates (S101)

- **CF-S101-W1-QEQ-RELIC-ODDFLOOR** (sibling, EMITTED): conjuncts A (odd-floor ≤ 1e-3), B (assert max q_dec < 1.857), C (derive γ/χ_I — my route: kernel-reactive PV part of T-eq.5, χ_I ∝ Σ w_n/(4E_n⁵)-class, ω_q^phys = √(k_curv/χ_I); coupled Δ_res/Δt assert; width-aware guard). Report-only: χ_I constancy, n=2 crossings, tail stratum split, h_par.
- **CF-S101-W1-QEQ-SELFCONS**: delta ZERO; amplitude-law diagnostic (PASS must realize q_amp ∝ |H|).
- Stage-0 candidate FROZEN; Stage-1 at S101; Stage-2 pools {lizzi, connes} × {gen, kitaev}; volovik + transit EXCLUDED (I cannot be a Stage-2 reviewer on H-PARITY-DRIVE-EXCLUSION).

## Corrections applied to my own text

- D-1: my R1 rider "transmits neither 1 nor exactly 2" overstated pointwise — 3p_local sweeps through 2 on the 33.2% decelerating mass; corrected in-place (workshop line 311).
- Re:V4 guard rationale retracted (lesson 1 above).
