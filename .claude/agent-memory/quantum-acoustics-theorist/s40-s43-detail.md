---
name: S40-S43 Detailed Results
description: Full results from sessions 40-43 (structural cartography, phononic crystal, fabric speed, polariton, DOS, thermal conductivity, quality factors)
type: project
---

## S40 Results (2026-03-11, STRUCTURAL CARTOGRAPHY)
- **T-ACOUSTIC-40 PASS**: T_a/T_Gibbs = 0.993. Acoustic metric with conformal factor correct.
  alpha_B2 = 1.9874 at tau=0.190. alpha_B1 = 2.6788 at tau=0.231.
- **B2-INTEG-40 PASS**: <r>=0.401 (Poisson), g_T=0.087, V(B2,B2) 86% rank-1.
  B2 weight CORRECTED: 81.8% (not 93%).
- **GSL-40 PASS (STRUCTURAL)**: v_min=0. All 3 entropy terms non-decreasing.
- **CC-TRANSIT-40 PASS**: dL/S_fold = 2.85e-6. Transit decouples from CC by 5.5 orders.
- **HESS-40 FAIL (COMPOUND NUCLEUS)**: 22/22 transverse H positive. 28D local minimum.
- **QRPA-40 FAIL (STABLE)**: All omega^2>0. 97.5% EWSR in B2 collective mode (omega=3.245).
  Near-resonance: omega_B2 ~ 2*omega_B1 (0.6% detuning).
- **PAGE-40 FAIL**: S_ent max = 0.422 nats (18.5% Page). Poincare recurrences.
- **B2-DECAY-40 B2-FIRST**: t_decay=0.922. 93%->89%. 89% permanently retained.
- **M-COLL-40 FAIL (CLASSICAL)**: M_ATDHFB=1.695. B1 dominates 71%.
- **SELF-CONSIST-40 FAIL**: Transit 1.72x FASTER.

## S41 Results (2026-03-12, CMB PHONONIC CRYSTAL)
- SU(3) under Jensen IS a phononic crystal: Bloch modes, band structure, van Hove, BZ
- Hard spectral gap 0 to 0.820 M_KK. Crystal purely optical post-transit.
- Acoustic branch (NG mode) exists ONLY during BCS transit, absent before/after.
- T/Theta_D ~ 10^{-22}: crystal transcendently quantum at CMB temperature.
- **Umklapp structurally absent**: rep lattice infinite, non-periodic.
- Q_B2 CORRECTED from S41's Q~10 to Q~52 (S43). Wrong frequency used.
- Digamma notation ENDORSED.

## S42 Results (2026-03-13)
- **C-FABRIC-42 PASS**: c_fabric = c (Lorentz invariant), m_tau = 2.062 M_KK
- **POLARITON-42 FAIL**: Min gap = 0.063 M_KK (3.7e13x too large for Higgs).
  Phononic hierarchy problem: crystal has no small parameter.
- CDM retracted -> lambda_fs = 89 Mpc (HDM). B2 flat band may restore CDM.

## S43 Results (2026-03-14)
- DOS-43: 992 eigenvalues, gap=0.8191, BW=1.258, 13 van Hove singularities.
- IMP-FILTER-43: DR=1.48 decades (structural). Combined HF+imp=2.99.
- BREATHE-43: omega=51.5 M_KK. K_BCS=-1.80 (0.016% softening). Stable.
- THERM-COND-43: kappa=infinity (Peierls-Boltzmann). Ballistic. u_2=c/sqrt(3).
- Q-SPECTRUM-43: Q_B2=52, Q_B1=8.5, Q_B3=[1.5,2.2,13]. No bell modes.
- KK-CMB-TF-43: First-sound ring r_1=325 Mpc, A_FS/A_BAO=0.204.
