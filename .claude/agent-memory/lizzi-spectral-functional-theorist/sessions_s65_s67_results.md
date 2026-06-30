---
name: S65-S67 Foundational Spectral Functional Results
description: First-engagement classification + S66 functional comparison gates + S67 anomaly exclusion theorem. Compressed merge of S65 engagement, S66 plan/zeta/anomaly/dim/mott/collab, S67 functional-select/Higgs-zeta.
type: project
---

## S65 Foundational Classification (2026-04-03)

**FUNCTIONAL-INDEPENDENT (structural)**: a_0/a_2=6/R for SU(3); block-diagonal (Peter-Weyl); B/F asymmetry=0; U(2)-preservation; BCS BDI Z_2 protection; Richardson-Gaudin integrability; conjugate pairing.

**SCHEME-DEPENDENT**: CC gap (117 OOM cutoff, ~113 OOM zeta); n_s=0.9590 (sqrt only); structural monotonicity; eps_H=0.02163; transit-as-relaxation viability.

**Key spectral data (canonical_constants.py)**: a_0=6440.0, a_2=2776.17, a_4=1350.72; S_fold=250,360.68 M_KK, dS/dtau=+58,672.80; M_KK=7.429e16 GeV; Delta_BCS=0.464 M_KK=3.45e16 GeV.

## S66 Gates

**ZETA-SA-66 FAIL**: n_s^{zeta}(a_4)=1.0897 BLUE tilt, eps_H^{zeta}=-0.04485 (NEGATIVE), eps_H^{cutoff}=+0.02163. eps_H ratio zeta/cutoff=-2.07 (SIGN FLIP). S_cutoff INCREASES with tau (UV-dominated), S_zeta(a_4) DECREASES (IR-dominated). Cutoff CC gap 120.5 OOM; zeta CC gap 117.3 OOM (3.2 OOM improvement, NOT solved).

**ANOMALY-CONSTRAINT-66 INFO**: f_0/f_2=(1/4)(e^{2phi}+1) FIXED by anomaly (not free). V(phi)=S_anom MONOTONICALLY INCREASING (no minimum). Discriminant a_2^2-2*a_0*a_4=-9,690,200<0. phi_critical~10^{-118} gravity, 10^{-121} Kerner. eps_H INDEPENDENT of CC (a_0 tau-independent).

**SPECTRAL-DIM-66 INFO**: Internal D_s~6 (Weyl): gravity=3.38, matter=6.03, full=6.08. FUNCTIONAL-INDEPENDENT. 4D effective D_s SCHEME-DEPENDENT: Zeta D_s(matter)=4, D_s(gravity)=2 (Weyl^2); Cutoff pathological. CC gap=111.9 OOM in BOTH schemes at M=M_KK.

**MOTT-ACCESS-66 PASS**: E_J/E_C=8.57 (zeta a_4), 4.98 (a_6), 8.18 (anomaly phi=-0.5), 200.25 (cutoff sqrt). MAXIMALLY SCHEME-DEPENDENT. alpha=|grad S_func|/|grad S_cutoff| determines E_J/E_C; cutoff alpha=1.0 UV-dominated, zeta a_4 alpha=0.0104 IR-dominated.

## S67 Gates

**FUNCTIONAL-SELECT-67 FAIL (structural)**: Anomaly family STRUCTURALLY EXCLUDED from red tilt. n_s NEVER enters Planck [0.955, 0.975]; n_s minimum=1.000005 at phi=5.0; n_s maximum=1.037 at phi->0+. Joint constraint: 0 points satisfy BOTH n_s and m_H. **Permanent theorem**: dS/dtau=c_2(phi)*da_2/dtau+c_4(phi)*da_4/dtau<0 for ALL phi>0; therefore eps_H<0, n_s>1 (blue tilt) UNIVERSALLY in anomaly family. Cutoff f(x)=sqrt(x) NOT in anomaly family.

**HIGGS-ZETA-67 INFO**: m_H^{zeta}=138.5 GeV (79 sigma exclusion). Route A (moment ratio) lambda_zeta/lambda_cutoff=a_4^2/(a_0*a_4-a_2^2)=1.840, naive m_H=172.9 GeV. Route B (2-loop RG, primary): lambda_cutoff(M_KK)=0.0830, scaled to lambda_zeta(M_KK)=0.1527, run to M_Z gives 138.5 GeV. RG attenuates UV quartic enhancement; tripling UV ratio only gives 147.5 GeV. Independent particle-physics exclusion of zeta.

**Joint exclusion table**: n_s=0.957(2.0sigma cutoff)/1.090(29.7sigma zeta); m_H=127.5(13.9sigma cutoff)/138.5(79sigma zeta). Both observables independently select cutoff.

## Permanent classification protocol (S66 origin)
Every CC-sensitive computation reported in 3+ spectral functionals: cutoff sqrt(x), cutoff exp(-x), zeta, entropy. Classification table -> STRUCTURAL vs SCHEME-DEPENDENT.

Files: `computations/s66_zeta_sa.{py,npz,png}`, `s66_anomaly_constraint.*`, `s66_spectral_dim.*`, `s66_mott_access.*`, `s67_functional_select.*`, `s67_higgs_zeta.*`.
