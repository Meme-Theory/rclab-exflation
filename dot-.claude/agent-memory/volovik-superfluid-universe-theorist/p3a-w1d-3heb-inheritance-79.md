---
name: p3a-w1d-3heb-inheritance-79
description: S79 P3-A workshop R1 Turn B. W1-D τ_min=0.1878 at τ_fold is SUBSTRATE-UNIQUE (Khodel-Shaginyan flat-band mechanism, NOT 3He-B smooth-Fermi-surface). Framework is inheritance-hybrid: 3He-B topology (BDI, N_K=2) + Paper 16/17 condensation (flat-band, T_c ∝ λ) + SU(3) Casimir algebra (framework-unique) + 0D (framework-unique). Fold Triple Coincidence: §VII.II session-observation-class. Leggett mode SURVIVES under s++ at substrate level (phase-mode, not magnitude-mode). ω_L(multi,s++)/ω_L1 uncomputed — pre-registered S80 priority.
type: project
---

## S79 P3-A Workshop R1 Turn B Summary

**Date**: 2026-04-16
**Partner**: landau (W1-D gate owner)
**File**: sessions/archive/session-79/workshops/p3-a-w1d-tau-min-at-fold.md

## Key results from my R1 Turn B

### 3He-B inheritance (Q-V1 through Q-V5)

The framework is an INHERITANCE-HYBRID:
- Topology: 3He-B (BDI, N_K=2 analog, fully gapped). Paper 05, 10, 26.
- Condensation: Khodel-Shaginyan flat-band (T_c ∝ λ linear, divergent DoS). Paper 16, 17.
- Algebraic constraint: SU(3) Casimir block-diagonality (S22b). Framework-unique.
- Thermodynamic limit: 0D, N_pair=1. Framework-unique.

There is NO SINGLE VOLOVIK-PAPER BLUEPRINT for the framework. It is a SYNTHESIS.

### τ_min = τ_fold inheritance route

**Q-V3 ANSWER**: τ_min=τ_fold does NOT inherit from 3He-B. 3He-B has smooth Fermi surface, finite ρ(ε_F), no van Hove. The framework's DoS-peak condensation routes through Khodel-Shaginyan (Papers 16, 17). This is a SUBSTRATE-UNIQUE combination of 3He-B topology with flat-band condensation.

### 3He-B's actual 2-gap structure (critical for DM sector)

**L5 MISSED correction**: 3He-B is NOT a 2-gap superfluid in MgB₂/iron-pnictide sense. 3He-B is FULLY-GAPPED with N_K=2 (topological invariant). Its "2-ness" comes from J=0 vs J=2 decomposition of the p-wave triplet order parameter (internal to SO(3)_s), coupled by the dipolar interaction.

The framework's "2-ness" is different: (0,0) ⊕ (1,1) Casimir-selected PW sectors with χ_a > Thouless at τ_fold. Different group (SU(3) vs SO(3)_s), different mechanism (DoS-peak vs dipolar).

### Leggett-mode survival under s++ (Q-V2 ANSWER — LOAD-BEARING)

**YES, Leggett mode survives under s++.** Reason: Leggett is a PHASE mode (not a magnitude mode). s++ and s+− both have well-defined relative phases (0 and π); both support Leggett oscillations.

**UNCOMPUTED**: ω_L(multi, s++) / ω_L1 ratio (where ω_L1 = 0.070 M_KK from S53). The .npz has `omega_L_multi` and `leggett_ratio` variables but cross-check 5 was flagged "not applicable" because s+− was not diagonalized-preferred.

**Pre-registered S80 gate** (my priority-1 recommendation): compute ω_L(multi, s++)/ω_L1; if ∈ [0.5, 2.0] DM sector survives; if outside, DM abundance needs re-derivation.

### Fold Triple Coincidence — §VII.II harvest

**Three S78 observables are 3 response-function readouts of one spectral feature ρ(ε→0, τ_fold)**:
1. W1-E's |β|² ≈ 4.3×10⁴ (mode dynamics)
2. W2-A's mu_eff slow mode on B1 (Laplacian kinetics)
3. W1-D's τ_min = τ_fold with χ_a peak (condensation susceptibility)

**Classification**: SESSION-OBSERVATION-CLASS (§VII.II), pre-theorem. Not §VII.I because:
- Requires per-functional computation (not exact identity from D_K definition)
- Different scheme-dependencies (f*, scheme-independent, multi-scheme)
- Consequences are sector-partitioned (block-diagonal theorem still applies)

**Promotion path to §VII.I**: a 4th independent functional also concentrating at τ_fold. Candidates: χ_N (fermion number), dS_inst/dτ, Z_s elastic-tetrad (Nissinen-Volovik Papers 20, 21).

### Multi-band bootstrap permanent closure (L4 CONCURRED)

**CLOSED 2026-04-16.** Three reasons:
1. Block-diagonal theorem S22b (8.4×10⁻¹⁵) forbids inter-sector V-mixing.
2. PW 4-sector structure (not 72).
3. Per-sector Thouless (only (0,0) and (1,1) pair at calibrated V0).

**V_inter = 0 exact at all orders** (S60 inter-sector-zubarev-60-result). The OPERATOR needed for the 72× mechanism does not exist in the framework's Hilbert space.

**Q-V5**: 3He-B has NO 72× analog. Closure is strengthened by inheritance, not weakened. Parent and child both lack the mechanism.

**A_s closure paths remaining**: f_conv, isocurvature (W2-A), Leggett-GGE (W2-H), S_IC sub-horizon cap, multi-pair (N_pair=2 within-sector). Multi-pair is NOT multi-band — it is a higher-excitation sector of (0,0)⊕(1,1), NOT foreclosed by block-diagonality. Proposed S80 computation.

### Jensen-deformation-as-flat-band-generator — V2 harvest

**Substrate-unique statement**: The Jensen deformation of D_K acts as a parameter-driven flat-band generator. At τ = τ_fold, ρ(ε=0, τ) is singular (ρ_smooth = 14.02). This generates Khodel-Shaginyan-class condensation at the spectral-triple level.

**Three distinctive features vs 3He-B**:
1. Parameter-driven (τ) not momentum-driven (k)
2. Located at ε=0 (flat-band), not at gap edge (ε = Δ_B)
3. First-order in dS_bare/dτ (discontinuous at τ_fold)

**Q-V4 ANSWER**: Jensen breaks 3He-B's smooth-Fermi-surface DoS structure at τ_fold, replacing with singular-DoS flat-band. Analog of 3He-B μ=0 topological transition (N_K=2 ↔ N_K=0).

## Pre-registered questions for landau R2 Turn A

- **Q-L1**: Best 4th functional for Fold Triple Coincidence theorem-class promotion.
- **Q-L2**: ω_L(multi, s++)/ω_L1 numerical value (load-bearing for DM sector).
- **Q-L3**: N_pair=2 excitation support at W1-D ground state (alternative A_s path).
- **Q-L4**: B1 soft at τ_fold = deformation-driven flat band? If yes, framework has TWO flat-band mechanisms (topological B2 + deformation-driven B1).
- **Q-L5**: s++ vs s+− sign discipline under beyond-uniform-gap computation.

## Convention pins held

- f* scheme canonical (W1-D 72× threshold).
- Block-diagonal theorem PERMANENT (machine epsilon).
- Gate verdict W1-D FAIL stands.
- Substrate-first framing: fold = DoS singularity + dS_bare/dτ discontinuity (first-order transition in Jensen deformation).
- Substrate-first, not 3He-B-by-analogy. Framework inherits from Volovik corpus as a SYNTHESIS, not a single-paper child.

**Why**: P3-A was the 3He-B inheritance test workshop. R1 Turn B answered 5 direct substrate questions (Q-V1 to Q-V5) and established the Fold Triple Coincidence as §VII.II harvest. The Leggett-mode-survives-under-s++ answer is load-bearing for the DM sector; ω_L(multi, s++)/ω_L1 computation is pre-registered as S80 priority-1.
**How to apply**: When questions about 3He-B inheritance or flat-band physics arise, cite this memory and the hybrid inheritance table (V1 Part 2). The framework is NOT a pure 3He-B analog; it is a 3He-B-topology + Khodel-Shaginyan-condensation + SU(3)-Casimir + 0D synthesis.
