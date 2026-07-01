---
name: S78 W1-E Pre-Fold Vacuum S_IC Results
description: S78-W1-E-PRE-FOLD-VACUUM gate verdict FAIL; S_IC(k_pivot)=1.636e+05 amplification not suppression; spread factor 1.133 between 3 IC principles (no axiomatic gap); Gen-Physicist "same-rho-in-ground-state-limit" vindicated at k_pivot
type: project
---

## S78 W1-E Pre-Fold Vacuum Gate — Final Results

**Date**: 2026-04-15
**Gate**: S78-W1-E-PRE-FOLD-VACUUM
**Verdict**: **FAIL** — pre-fold vacuum is an AMPLIFICATION channel (S_IC ≫ 1), not a suppression channel as the original gate hypothesis required.

### Headline Numbers (4-tuple tag: f*, |α+β|², L_max=10)

| IC Principle | S_IC(k_pivot) | Wronskian | \|α\|²−\|β\|² |
|:-------------|:-------------:|:---------:|:-------------:|
| **Spectral stationarity** (CANONICAL) | **1.6357e+05** | W = −i | +1.0 to 6e-10 |
| Minimum entropy | 1.8540e+05 | W = 0 | 0.0 |
| AZ-topology | 1.6357e+05 | W = +i | −1.0 to 6e-10 |

**Cross-check spread (max/min) = 1.133** (0.054 OOM) — no axiomatic gap.

### Physical Interpretation
- Pre-fold "vacuum" in substrate framing: flat D_K spectrum before Jensen deformation; modeled as z″/z = 0 for η < −dt_transit. No FRW background yet.
- Fold: tanh ramp of z″/z from 0 to post-fold dS value (2(aH)²) over dt_transit = 1.13e-3 M_KK⁻¹.
- Post-fold: dS (H ≈ 0.633 M_KK, ε ≈ 4.8e-3).
- k_pivot² = 204.8 M_KK², k²/(z″/z)_fold = 107.6 — **deep subhorizon at transit**. The fold is a SUDDEN (diabatic) parametric kick.
- |β|² ≈ 4.3e+4 per mode → massive squeezing (pair production) through the fold.

### Key Finding: The Three Principles Agree
In the oscillatory subhorizon regime at k_pivot, spectral stationarity (positive-freq vacuum, W=−i), minimum-entropy (standing wave, W=0), and AZ-topology (negative-freq CPT mirror, W=+i) all give nearly identical S_IC (factor 1.13 spread). This **vindicates Gen-Physicist's independence-of-principles skepticism** from the DISAGREEMENT BLOCK: all three principles DO select essentially the same ρ when the mode is in the free-oscillator regime. The "32-OOM spread" concern from the tossed S78 execution was an artifact of NON-PHYSICAL IC normalizations (comparing unitary-equivalent vacua under different Wronskian conventions).

### Why FAIL (not INFO)
The original hypothesis was that pre-fold non-BD suppression would close the S66 A_s gap by providing S_IC ∈ [10^-10, 10^-9] (9-10 OOM suppression). Result: S_IC = 1.6e+5 (ENHANCEMENT by 5 OOM). The channel runs the WRONG DIRECTION. Combined with S77's OVERPRODUCTION finding (A_s gap inverted to +9.5 OOM) and S78-W1-C BACKREACTION reducing F_amp from 6858 to 48 (143× reduction), the A_s closure path now requires **conversion (f_conv)** and **backreaction**, NOT pre-fold IC selection.

### Cross-Checks (6 required)
1. **Adiabatic recovery**: PARTIAL — SS/AZ → 0.9999, ME → 1.94 (the factor-2 is the W=0 normalization artifact of ME, a known feature)
2. **First-order PT signature**: PASS (dS pre-fold 58,673 vs post-fold ~359)
3. **Level-crossing vs n_pairs**: PASS (structural — different basis from substrate BCS; just verifies |β|²>0)
4. **Non-BD squeeze FI**: PASS (18.3% drift for 10% scheme shift, within S69 Lizzi FI tolerance)
5. **Ordering stability**: PASS (ordering preserved under 10% pre-fold perturbation)
6. **S_IC(k_pivot)/S_IC(k_lo)**: 5.25 at k_lo = k_pivot/3 — squeezing concentrated at higher k

### Why this applies
- Any future A_s computation should IGNORE pre-fold non-BD vacuum as a suppression mechanism
- The DISAGREEMENT BLOCK (axiomatic gap concern) is LATENT — only matters in tachyonic pre-fold regimes, not at k_pivot
- Default to spectral-stationarity as the canonical IC (user decision default; no re-selection needed)
- The MASSIVE |β|² ≈ 4.3e+4 per mode is a STRUCTURAL feature of the subsonic-to-dS fold: suppressing it requires breaking the sudden approximation (making dt_transit longer than 1/omega_k), which is NOT within the framework's degrees of freedom

### Files
- Script: `computations/s78_pre_fold_vacuum.py`
- Data: `computations/s78_pre_fold_vacuum.npz`
- Plot: `computations/s78_pre_fold_vacuum.png`
- Log: `computations/s78_pre_fold_vacuum_output.txt`
- Verdict line: `computations/s78_gate_verdicts.txt`
