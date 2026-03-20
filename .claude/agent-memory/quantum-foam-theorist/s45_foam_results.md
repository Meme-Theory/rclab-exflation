---
name: S45 Foam Computation Results
description: SAKHAROV-UV-DISSOLUTION-45 INFO. Dissolution and Sakharov point in opposite directions. No self-consistent emergence scale. Correct PW mode-count scaling.
type: project
---

## SAKHAROV-UV-DISSOLUTION-45 (S45, W5-1)

### Gate Verdict: INFO

Quantitative relationship exists between Sakharov UV cutoff and dissolution scale, but they point in OPPOSITE directions. No self-consistent "emergence scale" where both crystallization and correct G_N coincide.

### Input Data
- S44 Sakharov audit (Formula B): Lambda_cross = 5.09e17 GeV = 6.86 M_KK (G_Sak = G_obs)
- S44 Dissolution: epsilon_c = 0.188 * N^{-0.457}, R^2 = 0.957

### Key Results

**R1: Mode-count scaling (CORRECTED)**
- N_Hilbert ~ 1.93 * L^{4.53} (asymptotic, L>10)
- a_0 (PW-weighted) ~ 0.17 * L^{7.30} (asymptotic)
- The claim N ~ (Lambda/M_KK)^8 is WRONG for PW truncation
- Discrete Weyl coefficient c_W = a_0/lambda_max^8 = 19.8

**R2: Foam-strength scenarios**

| Foam model | epsilon | N_crit | L_crit | Lambda_match/M_KK |
|:-----------|:--------|:-------|:-------|:------------------|
| Effacement (7.8e-8) | 7.8e-8 | 9.5e13 | ~1050 | 1.1e-8 |
| Left-invariant (1e-4) | 1e-4 | 1.5e7 | ~33 | 0.0035 |
| Generic (0.014) | 0.014 | ~300 | ~3 | 21.3 |
| Holographic@KK (0.033) | 0.033 | ~45 | ~2 | 96.7 |

**R3: Structural tension**
- More modes -> lower epsilon_c (more fragile) AND lower Lambda_match (too much gravity)
- Fewer modes -> higher epsilon_c (more robust) AND higher Lambda_match (natural UV cutoff)
- These trends ANTI-CORRELATE: no single scale serves both purposes

**R4: Sakharov crossover (L=3, Formula B)**
- Lambda_cross = 5.09e17 GeV = 6.86 M_KK
- At M_Pl: 26.8x overshoot (1.43 dex)
- At 10*M_KK: 2.29x overshoot (0.36 dex)
- At 3*M_KK: 0.132x undershoot (-0.88 dex)

**R5: Self-consistent fixed point (Weyl + holographic)**
- Lambda_emergence = 0.85 M_KK (below compactification scale!)
- N_emergence = 5.3 modes (too few for anything)
- G_Sak 4.8 dex below observed
- Fixed-point exponent: 2/3 + 8*alpha = 4.32

**R6: Prompt's question answered**
- epsilon_c(10^8) = 4.2e-5 (close to 10^{-4}, factor 2.4)
- But N^8 scaling wrong; left-invariant foam gives eps=1e-4 at L~33, not N~10^8

### Physical Interpretation
The spectral triple at L=3 survives left-invariant foam (eps_foam=1e-4 << eps_c=0.007) but is dissolved by generic foam (eps_foam=0.014 > eps_c=0.007). The Sakharov formula at L=3 gives G_obs at Lambda ~ 7 M_KK -- a natural scale one decade above compactification.

The dissolution and Sakharov scales bracket M_KK from opposite sides (0.85 and 6.86 M_KK), separated by 0.91 dex. This is structural, not a coincidence: both phenomena depend on the same spectral data but through different functionals.

### Corrections to Previous Claims
- MEMORY.md line "Lambda_eff from Sakharov = dissolution scale" was WRONG. They are structurally independent.
- N ~ L^5 was rough; correct asymptotic is L^{4.53} for N_Hilbert.
- The "10 M_KK" estimate in S44 was the leading-term-only approximation; full Formula B gives 6.86 M_KK.

### Files
- Script: `tier0-archive/s45_sakharov_dissolution.py`
- Data: `tier0-archive/s45_sakharov_dissolution.npz`
- Plot: `tier0-archive/s45_sakharov_dissolution.png`
