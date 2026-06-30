---
name: S84 W5-54 K-FLOOR-REGULATOR-INVARIANCE result
description: K-floor is regulator-dependent. K_R5(zeta)=0.6366 vs K_R5(Zubarev)=32.40, ratio 0.980. S83 G38 WALL is zeta-specific artifact.
type: project
---

# S84 W5-54 K-FLOOR-REGULATOR-INVARIANCE: FAIL

**Gate**: S84-K-FLOOR-REGULATOR-INVARIANCE
**Trigger**: [VERIFY] [AUDIT]
**Classification**: GEOMETRIC
**SHA256**: `91b214f00df91826ae8d0df859e647525962d0e06f891e48074790acedf5e88c`

## Result

Two independent FAIL triggers:
1. `|K_R5(Zub) - K_R5(zeta)| / K_R5(Zub) = 0.9804` ≫ 0.10 FAIL threshold.
2. `K_R5(zeta) = 0.6366 < 1` crosses positivity wall (FAIL clause b).

## Key numbers (L_max=5, 6048 modes, sum(d_k)=159936)

| Quantity | zeta | Zubarev |
|---|---|---|
| xi(R) = S_R_E / S_zeta_E | 1.000000 | 0.019646 |
| A_s_base(R) | 3.299e-9 | 6.481e-11 |
| K_match(R) = K_R5(R) | 0.6366 | 32.4021 |

xi(Zubarev) matches S84 W1a SV1 anchor 0.019646 to |diff| = 4.6e-7 (CC2).

## Why: the math

- f_zeta(λ) = 1; f_Zub(λ) = exp(-λ²/M_KK²).
- For every λ>0 (min λ=0.820, max λ=2.803 M_KK in L≤5 cache), exp(-λ²)<1.
- ⇒ xi(Zubarev) strictly < 1 ⇒ A_s_base(Zub) < A_s_base(zeta) ⇒ K_match(Zub) > K_match(zeta).
- Separation factor = 1/xi_Zub ≈ 50.9×.

## Structural consequences

- **S83 G38 K_match_WALL = 0.6366** is exactly `K_match(zeta)` (machine epsilon). G38 WALL is zeta-specific, NOT regulator-agnostic.
- R5 convention (K=1.922) cannot be elevated to "structural" on Zubarev alone.
- Under zeta: corridor cluster {1.922 ≤ K ≤ 15.95} OVER-shoots Planck by ~3-17×.
- Under Zubarev: same cluster UNDER-shoots Planck by 17×-169×.
- Cluster-width (factor 8.3 across R1-R5) dwarfed by regulator shift (factor 50.9).

## 3He-B correspondence (Volovik)

The factor-50 suppression of energy-weighted vs flat first moment under Zubarev IR mollification mirrors the BCS coherence factor (u² − v²) suppression of thermodynamic densities vs band-theoretical DoS in 3He-B. Δ/ε_F ~ 1.76 k_B T_c / ε_F ≪ 1 in the superfluid analog. Structurally expected, not pathological.

## Cross-checks (all PASS)

- CC1: xi(zeta)=1 identity. OK.
- CC2: xi(Zub) vs SV1 anchor: |diff|=4.6e-07. OK.
- CC3: K_match·A_base=A_Planck. Machine-exact. OK.
- CC4: torch (ROCm cuda) vs numpy first moment. rel=2.77e-16. OK.
- CC5: A_s(K) linearity. ratio-deviation=0. OK.

## Open for S85

Two remediation paths:
1. Construct regulator-invariant A_s_base via ratios of same-regulator moments (requires re-derivation of UNIFIED-AS-79).
2. Rule out zeta axiomatically (promote S83 G3 to L1-exclusive).

## Files

- Script: `computations/s84_w5_k_floor_regulator_invariance.py`
- Data: `computations/s84_w5_54_data.npz`
- Plot: `computations/s84_w5_54_plot.png`
- WP: `sessions/archive/session-84/session-84-w5-workingpaper.md` §W5-54
