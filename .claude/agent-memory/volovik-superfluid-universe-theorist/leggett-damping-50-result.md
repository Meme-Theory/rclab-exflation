---
name: leggett-damping-50-result
description: S50 LEGGETT-DAMPING-50 PASS (Q=6.7e5). Beliaev forbidden by 25.9x (quasiparticle gap >> order parameter gap). Raman forbidden (0D). Leggett mode is exact eigenstate. Mass concept valid. S49 ratio corrected (0.414 was misleading, true ratio 0.039).
type: project
---

## LEGGETT-DAMPING-50 Result (Session 50 W1-D)

### Gate: PASS (2026-03-20)

**Q = 6.7e5 >> 10** (formally infinite at T=0; finite Q from gravitational radiation only)

### Critical Correction

S49 wayforward framed omega_L/(2*Delta_B3) = 0.414 as marginal for Beliaev damping. This was WRONG because it used the order parameter gap Delta_B3, not the quasiparticle gap E_k = sqrt(eps_k^2 + Delta_k^2). Since eps_k ~ O(1) >> Delta_k ~ O(0.01-0.7), the true pair-breaking threshold is 2*E_min = 1.800 M_KK (not 2*Delta_B3 = 0.168). omega_L sits at 3.9% of the true threshold.

### Key Numbers

| Quantity | Value |
|:---------|:------|
| omega_L1 | 0.06955 M_KK |
| E_min (BdG) | 0.9001 M_KK |
| min(E_k + E_k') | 1.8002 M_KK |
| omega_L1 / min(E+E') | 0.0386 |
| Gamma_Beliaev(T=0) | 0 (exact) |
| Gamma_Raman(T=0) | 0 (forbidden in 0D) |
| Gamma_grav | 5.2e-8 M_KK |
| Q_total | 6.7e5 |
| Re[Sigma] mass shift | -0.096% |
| N_osc during transit | 1.3e-5 |

### Three Forbidden Channels

1. **Beliaev** (Leggett -> 2 quasiparticles): omega_L = 0.070 << min(E+E') = 1.800 by 25.9x. Kinematically forbidden.
2. **Raman** (Leggett -> 2 Goldstone): 0D system, no momentum-carrying Goldstone modes. Structurally forbidden.
3. **GGE thermal**: Leggett exists only pre-transit. GGE has no condensate, no Leggett mode.

### 3He Comparison

In 3He-B: eps_k measured from Fermi surface, so E_k ~ Delta and omega_L/(2*Delta) ~ 10^{-3}. Framework: eps_k = |lambda_k| >> Delta_k, so E_k ~ eps_k. The framework is MORE protected than 3He (discrete spectrum, 0D, no continuum).

**Why:** The conflation of order parameter gap with quasiparticle gap was a conceptual error in the S49 task framing. In condensed matter, these gaps are comparable near the Fermi surface. On the discrete Dirac spectrum, they differ by 10x.

**How to apply:** The Leggett mass m_G = 0.070 M_KK is valid. The 18% overshoot from m_req = 0.059 is a real quantitative tension but not invalidated by damping. The Leggett mode is the only surviving mass generation mechanism.

Files: s50_leggett_damping.py, s50_leggett_damping.npz, s50_leggett_damping.png
