---
name: running-gn-45-result
description: S45 RUNNING-GN-45 INFO. G_Sak(tau) across [0,0.5] at Lambda=10*M_KK. MONOTONE, 2.5% total variation, G_Sak/G_obs=0.436 (0.36 OOM). S44 confirmed to 0.19%. Quadratic 35x worse. a_0=6440 constant.
type: project
---

## RUNNING-GN-45 Result (Session 45 W4-R1)

### Gate: INFO (as pre-registered)

### Key Numbers
- Lambda = 10 * M_KK = 7.43e17 GeV
- a_0 = 6440 at ALL tau (species count constant throughout transit)
- G_Sak/G_obs at 9 tau points across [0, 0.5]:
  - tau=0.000: 0.4344
  - tau=0.050: 0.4345
  - tau=0.190 (fold): 0.4359
  - tau=0.500: 0.4454
- Total variation: 2.53% (MONOTONE increasing)
- |log10(G_Sak/G_obs)| = 0.361 (0.36 OOM) at fold -- S44 confirmed to 0.19%

### Quadratic Formula Comparison
- G_Q/G_obs at fold: 15.47 (1.19 OOM)
- Sakharov/Quadratic ratio: 35.5x
- Quadratic formula misses the UV-dominant Lambda^2 term
- Sakharov ALWAYS closer to observed than quadratic

### Decomposition
- Leading term: a_0 * Lambda^2 / (48pi^2) = 7.50e36 GeV^2 (CONSTANT)
- Subleading: -sum d_k m_k^2 ln(1+Lambda^2/m_k^2) / (48pi^2) varies -6.77e35 to -8.46e35
- Subleading is 9.0-11.3% of leading (modest correction)
- ALL tau-dependence in G_N comes from the subleading mass-log correction

### Physical Interpretation
- Sakharov induced gravity is dominated by the species-counting (a_0) term
- a_0 = 6440 is the number of PW-weighted positive Dirac modes -- TOPOLOGICALLY FIXED
- This is the condensed matter analog: 1/G ~ N_F * p_F^2, where N_F (species near Fermi surface) is constant
- The Jensen deformation changes eigenvalue magnitudes (effective masses) but not mode count
- G_N running is negligibly small (~2.5%) because topology protects the mode count
- This is consistent with Volovik Paper 07: induced gravity is robust against perturbations that don't change the Fermi-point topology

### Convention Clarification
- G_Sak/G_obs = 0.436 means Sakharov gives STRONGER gravity (G smaller)
- S44 reported f_2 = 2.29 = G_obs/G_Sak (inverse convention), NOT G_Sak/G_obs
- Both give 0.36 OOM, both PASS the < 2 OOM gate

**Why:** Running G_N test: does the Sakharov formula give tau-dependent gravity? Answer: NO, G_N is essentially constant (2.5% variation) because the leading term is topologically protected.
**How to apply:** G_N from Sakharov is nearly constant across the transit. Any dynamical-G scenario would require a mechanism that changes the mode count (a_0), which would require topology change in the KK spectrum. The 0.36 OOM proximity to observed is genuine but the quadratic formula fails (1.19 OOM).
