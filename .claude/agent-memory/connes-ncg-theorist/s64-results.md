---
name: S64 All Results
description: S64 consolidated -- CC walls mapped, Hessian descent PASS, GGE-KMS INFO, r=0.033, BdG foundation, 26 gates, 7 permanent theorems
type: project
---

## S64 Overview
Master Gate CC-COMBO-64 = FAIL. 26 computations, 8 waves, 7 permanent theorems.

## HESSIAN-DESCENT-64: PASS
- R-Hessian on 35D vol-preserving: signature (8+,27-). Fold is saddle of R(g).
- Round metric is LOCAL MAXIMUM of R (d^2R/da^2=-2, d^2R/db^2=-8).
- Anti-Jensen: steepest R-decrease = expand SU(2), shrink C^2+U(1). R: 2.018->0.578.
- a_0 constant under VP => a_0/a_2 INCREASES (CC worsens off-Jensen). PERMANENT.

## GGE-KMS-64: INFO (COMPATIBLE)
4 theorems proven:
1. GGE-KMS compatibility: rho_GGE satisfies generalized KMS with beta_k=lambda_k, H_k=R_k.
2. Modular decomposition: Delta_GGE = prod Delta_k (exact, from [R_j,R_k]=0).
3. Multi-periodicity: 8 frequencies, Connes spectrum dense in R. Type III_1 in thermo limit.
4. Entropy decomposition: S_GGE = sum S_k, each = spectral action per CCSvS 2019.
- lambda_B2=-0.053 < 0 compatible with Tomita-Takesaki.

## Other Permanent Results (S64)
- **R(tau) monotonicity on Jensen**: dR/dtau >= 0 by AM-GM. Path C CLOSED.
- **Lambda_SA = Lambda_J**: Spectral action fixes Jacobson integration constant. 114-OOM gap real.
- **Spectral moment decoupling**: CC (F_{-1}) vs NEC (F_{+1}) independent channels.
- **BdG heat kernel factorization**: K_BdG(t) = exp(-Delta^2 t)*K_bare(t) to 2.2e-16. 31.2% of Sakharov.
- **Fermi-surface lock**: v^2(B2[0]) = 1/2 identically when eps=0.
- **Chirality non-cancellation**: {gamma_9, dD_K/dtau}=0 => chiral pairs ADD.

## CLOSED Mechanisms (S64)
- CC Path C, CC category error, CC VP off-Jensen, CC Jacobson multi-T, CC 12D Jacobson-Kasparov
- All 5 baryogenesis channels

## PASS Results
- r = 0.033 (two independent methods). n_s = 0.9557 +/- 0.0036 (2.2 sigma).
- VAB rank=5 (room for 3 generations). GSL monotone. Transfer Bogoliubov universal.
