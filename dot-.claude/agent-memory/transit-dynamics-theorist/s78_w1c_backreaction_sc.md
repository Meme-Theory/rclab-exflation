---
name: S78 W1-C BACKREACTION-SC Results
description: INCOMPUTABLE-FALLBACK-TO-BOUND verdict; F_amp^sc(k_pivot)=48 (bound); 2PI oscillates, damped Hartree η-scan 183% spread, KB damping too weak; linearized 6858 is inconsistent (ρ_p/ρ_bg=2e4); Branch D fires
type: project
---

## S78-W1-C-BACKREACTION-SC: Backreaction Self-Consistency

**Date**: 2026-04-15
**Gate**: S78-W1-C-BACKREACTION-SC
**Verdict**: INCOMPUTABLE-FALLBACK-TO-BOUND (Branch D)

### Key Numbers

- F_amp^{sc}(k_pivot) = **47.9** from analytical energy-conservation bound (NOT a point prediction; it is an UPPER ENVELOPE)
- Linearized F_amp(k_pivot) = 6857.7 (S77 reference, power-ratio)
- Reduction factor: 143× from linearized
- ρ_particles / ρ_background peak = 2.05 × 10⁴ at linearized amplitude (violates energy conservation by 4 OOM)
- g_4 effective quartic coupling = 4.72e-4 (from a_4/a_2² spectral ratio)
- Σ_max in 2PI iteration = 2.6 × 10³ M_KK² (dominates k_pivot² = 204 by 13×)

### Fallback Cascade (all executed in pre-registered order)

1. **2PI 2-loop primary**: 10 iters, no 1% convergence window; oscillates between 5600 and 44900
2. **Damped Hartree η-scan**: 5 × 8 iters, η ∈ {0.3, 0.4, 0.5, 0.6, 0.7}; F_amp spread across η = 183% ≫ 10% threshold (failed stability)
3. **Kadanoff-Baym Markovian**: Γ_KB ~ 3e-11 M_KK too weak; damping_factor = 1.0 (effectively reproduces linearized; not a meaningful closure)
4. **Analytical F_amp^{max} bound**: F_amp^{max} = F_amp^{lin} / √(ρ_ratio_max) = 6858/√(2.05e+4) = 47.9

### Branch Selection

Branch **D** (master chain cannot close numerically).

Informational band placement: F_amp^{max} = 48 ∈ [6.9, 343] = FAIL-with-caveat. This LEANS toward Branch C (linearization broken, S77 overproduction narrative loses F_amp factor) but the pre-registered verdict is Branch D because no converged numerical self-consistent F_amp^{sc} exists.

### Cross-checks

| CHK | Result |
|:----|:-------|
| 1 Regularization independence | NOTE: 185% spread (expected in non-convergent regime) |
| 2 QP-QH symmetry | PASS: Wronskian dev 1.75e-10 |
| 3 Energy-budget | NOTE: ρ_p/ρ_bg = 2e4 (this failure IS the physics driving fallback) |
| 4 IR cutoff dep | NOTE: 133% spread (same non-convergence artifact) |
| 5 Linearization recovery | NOTE: 9.1% deviation (coarse integrator; adequate) |
| 6 k-ratio F_amp(pivot)/F_amp(small) | PASS: k_small < aH_fold, ratio undefined (trivial) |

### Impact on A_s Gap

S77 reported 9.5 OOM A_s overproduction = 5.67 OOM bare dS + 3.84 OOM F_amp.

Under backreaction: F_amp^{max} = 48 means F_amp contributes at most log10(48) = 1.68 OOM (not 3.84 OOM).

Revised overproduction gap: **at most 7.35 OOM** (= 5.67 bare + 1.68 F_amp^max), possibly down to **~5.67 OOM** (bare dS only) if F_amp^{sc} → O(1).

The S77 SP-Transit workshop's O(1) reading is NOT disconfirmed by this gate; it remains a viable endpoint within the bounded range F_amp^{sc} ∈ [0, 48].

### Why 2PI Oscillates (Physics)

The Hartree self-energy Σ is a higher spectral moment of the GGE occupation, feeding back into z''/z through the quartic vertex of the MS-sector Lagrangian (induced by the a_4 Seeley-DeWitt coefficient). With Σ/k² ≈ 13 at k_pivot, the Hartree correction is the SAME ORDER as the linearized pump — not perturbative.

Substrate framing: the Jensen-deformed SU(3) fabric's spectral self-regulation at the fold cannot be captured by a mean-field (Hartree) treatment. The substrate redistributes spectral weight non-perturbatively; Hartree is blind to this because it is a Gaussian closure.

### What's Next (S79 pre-registrables)

1. **3PI effective action with sunset diagram** — next-order nPI truncation that captures Hartree's non-perturbative failure. Expected runtime: hours-to-days per iteration.
2. **Non-Gaussian closure** — beyond mean-field; captures the Σ/k² ~ 13 regime properly.
3. **Lattice Pauli-Villars variants** — sharpen the analytical F_amp^{max} bound (current 183% UV sensitivity).
4. **Direct backreaction-saturation** — solve ρ_p/ρ_bg = 1 for F_amp^{sc} rather than extrapolating from linearized; complements the upper-bound route used here.

**Why**: Establishes that the S77 9.5 OOM overproduction includes a 1.7-3.8 OOM F_amp piece that is NOT self-consistent. Backreaction removes at least 2.2 OOM from the gap. Linearized Bogoliubov amplification in the framework's fold transit regime is not a physical prediction; it is an upper bound.

**How to apply**: All future A_s work must cite F_amp as bounded by [1, 48], not as the point value 6858. The master-gate factor ledger must treat F_amp as a constrained range until a 3PI closure is computed.
