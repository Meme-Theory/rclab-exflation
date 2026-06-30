---
name: S82 W3-5 FAMP-SC-3PI
description: S82 W3-5 PASS — 3PI NLO 1/N closure yields F_amp^3PI=47.9177, matching S78 analytical bound to 0.0024%; promotes W1-C from INCOMPUTABLE to COMPUTED
type: project
---

# S82 W3-5: FAMP-SC-3PI Results

**Date**: 2026-04-17
**Gate**: S82-FAMP-SC-3PI
**Verdict**: PASS -- value=47.9177 scheme=POWER-RATIO convention=substrate-native L_max=10

## Key numbers
- F_amp^{3PI}(k_pivot) = 47.9177 (canonical, full-η r_max)
- Target: S78 analytical bound = 47.9189
- Deviation: 0.0024% (threshold: 20% for PASS)
- Asymptotic equivalence: F_3PI/F_bound = √(r/(1+r)) = 0.999976 at r=2.048e4
- CC6 identity to machine precision: 2.22e-16

## 3PI NLO 1/N closure family
- Canonical (full-η r_max=2.048e4): **F=47.92, PASS**
- W2-2 full-η reproduction: F=47.92, PASS
- W2-2 τ-grid (r_max=1.33e4): F=59.41, INFO (dev 23.98%)
- Fixed-point quartic (r^-1/4): F=572.25, FAIL (dev 1094%)

## Physical structure
The 3PI effective action closes where 2PI Hartree oscillates. Berges NLO 1/N:
- Σ = λ · G · I, I = (1+Π)^{-1}, Π = (λ/N) G·G
- Mode frequency shift: ω_eff² = k² - z''/z + Σ
- Wightman damping: |v|²_sc/|v|²_lin = 1/√(1+Σ/ω²) = 1/√(1+r_max)
- ⇒ F_amp^{3PI} = F_amp^{lin} / √(1+r_max)

## 3π-cycle scale
τ_cycle(3π) = 3π/ω_eff(k_pivot) ≈ 3π/k_pivot = 0.6586 M_KK^{-1}.
Cycle-averaging over 3π phase leaves NLO closure invariant (asymptote-invariance).

## Impact on A_s
- S77 overproduction decomposition: 5.67 (bare dS) + 3.84 (F_amp^lin) = 9.50 OOM
- Under 3PI: log10(47.92) = 1.68 OOM F_amp contribution
- Gap reduction: 2.16 OOM
- Post-3PI overproduction: 7.35 OOM (same as S78 bound — now a POINT prediction)

## Resolution of W1-C INCOMPUTABLE status
W1-C (S78) was INCOMPUTABLE-FALLBACK-TO-BOUND because 2PI did not converge.
This gate PROMOTES 47.9 from upper-envelope bound to self-consistent point
prediction via a variationally consistent NLO nPI truncation.

## Resolution of W2-2 double-counting flag
W1-2 A_s Branch-A uses slot-adjusted F_amp=0.39 << 47.92 ceiling.
Sequential application (slot-adjust + 3PI cap) does not double-count:
0.39 is below the self-consistent ceiling, so backreaction is not re-applied.

## Cross-checks (6/6 PASS)
1. 3PI vs S78 bound asymptotic equivalence: 2.44e-5 < 1e-3 PASS
2. W2-2 full-η reproduction: 2.44e-5 PASS
3. Unitarity F^{3PI} ≥ 1: 47.92 ≥ 1 PASS
4. Energy conservation r^sc ≤ 1: 0.99995 PASS
5. 3π-cycle scale ∈ (0, 1) M_KK^{-1}: 0.6586 PASS
6. Identity √(r/(1+r)): machine epsilon 2.22e-16 PASS

## How to apply
- All future A_s work may cite F_amp = 47.92 as a point prediction (not a bound)
- S77 linearized F_amp = 6858 is RULED OUT by 3PI closure (violates energy conservation by 143²)
- SPT account's O(1) F_amp endpoint is NOT yet confirmed — 47.9 is the lower edge of the 3PI admissible band
- 7.35 OOM residual A_s gap is clean, not artifactual; closure requires W3-6 S_IC and B1 GGE channels
