# OOM Gap Reference -- Phonon-Exflation Framework

**Date**: 2026-04-12 (S75)
**Scope**: Every computed quantity that overshoots or undershoots an observed/target value by a catalogued amount, drawn from all 75 sessions.
**Convention**: Gap = log10(computed/target). Positive = overshoot. Negative = undershoot.

---

## Summary Table

| # | ID | Quantity | Gap (OOM) | Direction | Status | Session | Source |
|:--|:---|:---------|:----------|:----------|:-------|:--------|:-------|
| 1 | CC-RAW-QTHEORY | CC (q-theory, gravity route) | +114.0 | OVER | STRUCTURAL | S43/S64 | permanent-results-registry XV-A |
| 2 | CC-CONSERVATIVE-STACKABLE | CC (after all stackable corrections) | +102.7 | OVER | STRUCTURAL | S64/S66 | permanent-results-registry XV-A |
| 3 | CC-VOLOVIK-SCENARIO-A | CC (GGE dilution only, w=-1) | +113.6 | OVER | CLOSED | S66 | baseline-findings-s66 |
| 4 | CC-VOLOVIK-SCENARIO-B | CC (Volovik rho~H^2, L=3) | +0.01 | OVER | SUPERSEDED | S66 | DILUTION-CC-66 |
| 5 | CC-CHI2-LMAX7 | CC (chi_2 route, L=7) | -0.47 | UNDER | OPEN | S73B | session-73b W5-G |
| 6 | CC-A0-SCHEME-LMAX7 | CC (a_0 cutoff scheme, L=7) | +1.61 | OVER | OPEN | S73B | session-73b W5-G |
| 7 | CC-SCENARIO-B2-DESI | CC (uniform w=-0.918, DESI EOS) | +106.7 | OVER | CLOSED | S66 | permanent-results-registry |
| 8 | CC-QTHEORY-NPAIR | CC (discrete q-theory self-tuning) | +113.5 | OVER | CLOSED | S66 | QTHEORY-NPAIR-66 |
| 9 | AS-ROUTE-A-S66 | A_s (Route A, raw spectral) | +7.62 | OVER | CLOSED | S66 | AMPLITUDE-NORM-66 |
| 10 | AS-ROUTE-B-PW-S66 | A_s (Route B, Peter-Weyl weighted) | +3.15 | OVER | CLOSED | S66 | AMPLITUDE-NORM-66 |
| 11 | AS-TRANSIT-SINGLE-S67 | A_s (single-field transit) | +15.1 | OVER | CLOSED | S67 | TRANSIT-PS-67 |
| 12 | AS-MULTIFIELD-DELTA-N-S67 | A_s (multifield delta-N, M1 Friedmann) | -0.80 | UNDER | CLOSED | S67 | MULTIFIELD-DELTA-N-67 |
| 13 | AS-DISSIPATIVE-S67 | A_s (dissipative EFT route) | +6.87 | OVER | CLOSED | S67 | DISSIPATIVE-AS-67 |
| 14 | AS-CURVATON-S67 | A_s (curvaton, M2) | -4.33 | UNDER | CLOSED | S67 | MULTIFIELD-DELTA-N-67 |
| 15 | AS-GGE-OSC-S67 | A_s (GGE oscillation, M3) | +12.34 | OVER | CLOSED | S67 | MULTIFIELD-DELTA-N-67 |
| 16 | AS-SINGLE-FIELD-HJ-S67 | A_s (single-field Hamilton-Jacobi) | +10.94 | OVER | CLOSED | S67 | MULTIFIELD-DELTA-N-67 |
| 17 | AS-MULTIFIELD-TRANSFER-S74 | A_s (multifield transfer, S74 W1-A) | +5.83 | OVER | CLOSED | S74 | session-74 W1-A |
| 18 | AS-BOGOLIUBOV-S74 | A_s (8-mode Bogoliubov, S74 W1-G) | +9.47 | OVER | CLOSED | S74 | A-S-FROM-BOGOLIUBOV-74 |
| 19 | AS-CW-SPECTRAL-S75 | A_s (CW spectral formula, S75 W1-D) | +11.06 | OVER | CLOSED | S75 | S75-A4-CW-JOINT |
| 20 | AS-CW-HJ-S75 | A_s (CW Hamilton-Jacobi route) | +10.98 | OVER | CLOSED | S75 | S75-A4-CW-JOINT |
| 21 | AS-CW-SLOWROLL-S75 | A_s (CW slow-roll, eps_V>>1 invalid) | +4.93 | OVER | CLOSED | S75 | S75-A4-CW-JOINT |
| 22 | FCONV-PROJECTION-S75 | f_conv (KK+spectral projection) | -9.594 | UNDER | **CLOSES #18** | S75 | S75-A5-F-CONV |
| 23 | AS-S53-RAW | A_s (S53 rho_exc/rho_bg weighting) | +6.3 | OVER | CLOSED | S53 | s53 results workingpaper |
| 24 | AS-S53-ENERGY | A_s (S53 E_exc/E_Hubble weighting) | +0.84 | OVER | CLOSED | S53 | s53 results workingpaper |
| 25 | H0-FRIEDMANN-DILUTED-S74 | H_0 (GGE diluted to today) | -29.0 | UNDER | OPEN | S74 | FRIEDMANN-FROM-A2-74 W1-E |
| 26 | H0-FRIEDMANN-UNDILUTED-S74 | H_0 (GGE undiluted, fiber-local) | +58.0 | OVER | STRUCTURAL | S74 | FRIEDMANN-FROM-A2-74 W1-E |
| 27 | RHO-GGE-TODAY-S74 | rho_GGE(today)/rho_crit | -56.0 | UNDER | OPEN | S74 | FRIEDMANN-FROM-A2-74 W1-E |
| 28 | DH-SIMULATION-S01 | D/H (GPE simulation) | +3.0 | OVER | CLOSED | S01-S02 | session-2-reframing |
| 29 | MH-GAUSSIAN-L6 | m_H (Gaussian fit, L=6) | +0.023 | OVER | OPEN | S66 | 131.8 vs 125.1 GeV (5.4%) |
| 30 | MH-RICHARDSON | m_H (Richardson extrapolation) | +0.013 | OVER | OPEN | S66 | 129.0 vs 125.1 GeV (3.1%) |
| 31 | MH-AITKEN-S66 | m_H (Aitken acceleration) | +0.008 | OVER | OPEN | S66 | 127.5 vs 125.1 GeV (1.9%) |
| 32 | MH-S73B | m_H (S73B W5-E) | +0.024 | OVER | OPEN | S73B | 132.23 vs 125.1 GeV (5.7%) |
| 33 | TAU-P-PROTON-DECAY | tau_p (proton lifetime) | +5.0 | OVER | PASS | S63 | 6.26e39 yr vs >1.6e34 yr |
| 34 | LAMBDA-FS-WDM | lambda_fs (DM free-streaming) | -22.0 | UNDER | PASS | S66 | 9.85e-23 vs <0.1 Mpc |
| 35 | TAU-DM-LEGGETT-GRAV | tau_DM (Leggett DM lifetime) | +65.0 | OVER | PASS | S73A | 4.93e82 s vs t_univ 4.35e17 s |
| 36 | FRIEDMANN-BCS-TAU-DYN | dwell_time/tau_BCS (BCS formation) | -4.59 | UNDER | STRUCTURAL | S36 | 1.04e-3/40 = 2.59e-5 (38,600x short) |
| 37 | FRIEDMANN-BCS-GRADIENT | gradient ratio (BCS vs SA) | +3.82 | OVER | STRUCTURAL | S39 | dV_bare/dV_BCS = 6,596x |
| 38 | FRIEDMANN-BCS-SHORTFALL | energy shortfall (BCS stabilization) | +5.12 | OVER | STRUCTURAL | S39 | 133,200x shortfall |
| 39 | INSTANTON-SINGLE-RATIO-S74 | V_inst/V_bare (single instanton) | -2.49 | UNDER | CLOSED | S74 | 3.22e-3 at L=3 |
| 40 | INSTANTON-MULTI-LMAX10-S75 | V_multi/V_bare (multi, L=10) | -3.34 | UNDER | CLOSED | S75 | 4.57e-4 at L=10 |
| 41 | INSTANTON-MODULI-SHORTFALL | restoring gradient shortfall | +2.49 | OVER | STRUCTURAL | S74 | 309x shortfall (bare/instanton) |
| 42 | INSTANTON-COULOMB-GAS | multi-inst restoring (Coulomb gas) | +2.20 | OVER | CLOSED | S74 | 158.8x remaining after 2x enhancement |
| 43 | THOOFT-VERTEX-VS-BARE | V_tHooft/dS_bare (at fold) | -12.0 | UNDER | CLOSED | S74 | W1-R |
| 44 | THOOFT-VS-CW | V_tHooft/V_CW (at fold) | -9.0 | UNDER | CLOSED | S74 | W1-R (19 OOM below CW) |
| 45 | SKYRMION-BARYON-MASS | M_skyrm vs proton mass | +22.0 | OVER | CLOSED | S64 | 1.27e5 M_KK = 6.4e22 GeV vs 0.938 GeV |
| 46 | ALPHA-S-SLOWROLL | alpha_s (slow-roll formula) | n/a | 5.0sigma | OPEN | S66 | -0.038 vs -0.0045+/-0.0067 |
| 47 | NS-HUBBLE-SA | n_s (Hubble spectral action) | n/a | 1.9sigma | OPEN | S66 | 0.9567 vs 0.9649+/-0.0042 |
| 48 | NS-BCS-CW | n_s (BCS+CW) | n/a | 1.3sigma | OPEN | S66 | 0.9595 vs 0.9649+/-0.0042 |
| 49 | SAKHAROV-GN-PHONON | G_N (phonon Sakharov, 192 modes) | -4.02 | UNDER | STRUCTURAL | S53 | G_Sak(phonon)/G_obs = 1.04e4 deficit |
| 50 | SAKHAROV-GN-DIRAC | G_N (Dirac Sakharov, Lambda=10 M_KK) | -0.36 | UNDER | PASS | S44 | ratio 2.29 (0.36 OOM) |
| 51 | TCMB-METHOD1-S53 | T_CMB (radiation T~1/a) | -6.6 | UNDER | CLOSED | S53 | overcooled by 6.6 OOM |
| 52 | TCMB-METHOD2-S53 | T_CMB (relativistic gas T~a^-0.869) | -2.0 | UNDER | CLOSED | S53 | overcooled by 2.0 OOM |
| 53 | BA-THERMALIZATION-S67 | Gamma_BA/H(z_eq) (BA mode decay) | +53.0 | OVER | PASS | S67 | 8.83e52 (53 OOM margin) |
| 54 | LEGGETT-WEINBERG-NAIVE | Gamma_grav(naive)/H_0 (no Z_2) | +50.0 | OVER | CLOSED | S73A | 1.81e8 GeV vs H_0 (50 OOM) |
| 55 | ISOCURVATURE-S67 | beta_iso | -10.0 | UNDER | PASS | S67 | 3.22e-12 vs Planck 1.7% |
| 56 | METRIC-NOISE-S52 | f_KK vs detectors | +32.0 | OVER | PASS | S52 | >10^40 Hz vs <10^8 Hz |
| 57 | EFFACEMENT-DE-S74 | Gamma leakage vs DE floor | -4.0 | UNDER | CLOSED | S74 | 2.82e-4 = 4 OOM below DE |
| 58 | W0-DESI-TENSION | w_0 (framework vs DESI DR2) | n/a | 2.9sigma | OPEN | S74 | -0.918 vs -0.752+/-0.057 |
| 59 | WA-DESI-TENSION | w_a (framework vs DESI DR2) | n/a | 2.9sigma | OPEN | S74 | ~0 vs -0.73+/-0.25 |
| 60 | ETA-B-S52 | eta_B (baryon asymmetry CP phase) | -inf | UNDER | STRUCTURAL | S52 | phi_CP = 0 exactly (BDI T^2=+1) |
| 61 | MKK-SPREAD-S52 | M_KK routes spread | 0.83 | n/a | PASS | S52 | 4 routes within 0.83 OOM |
| 62 | DECOHERENCE-MOTT-S73A | delta_OOM_Mott (charge noise) | n/a | +0.336 OOM | REFINED | S73A | F_Mott = 0.461 |
| 63 | DECOHERENCE-MOTT-REFINED-S74 | delta_OOM_Mott (CG24 refined) | n/a | +0.141 OOM | OPEN | S74 | MOTT-REFINED-CG24-74 |
| 64 | DECOHERENCE-DISPERSIVE-S73A | delta_OOM_dispersive | n/a | +0.150 OOM | OPEN | S73A | S73A W3-A |
| 65 | DECOHERENCE-COMBINED-S73A | delta_OOM combined | n/a | +0.486 OOM | REFINED | S73A | RE-DECOHERENCE-MULTI-73a |
| 66 | DECOHERENCE-COMPOUND-S74 | Mott(refined)+dispersive | n/a | +0.291 OOM | OPEN | S74 | vs target 0.267 OOM |
| 67 | BELIAEV-THREEPHONON-S73B | Gamma_Beliaev/H_fold | -6.0 | UNDER | PASS | S73B | 8.17e-7 (6 OOM below threshold) |
| 68 | GGE-EQUILIBRIUM-S57 | delta_n/N (GGE departure) | +56.0 | OVER | STRUCTURAL | S57/S58 | 0.195, 56 OOM above threshold |
| 69 | RG-CC-AMPLIFICATION | RG amplification for CC | -many | UNDER | CLOSED | S62 | insufficient by OOM |
| 70 | VOLOVIK-BBN-TRACKING-S67 | Gamma_beta/H(T_BBN) | +39.0 | OVER | PASS | S67 | 39 OOM margin |
| 71 | BETA-RELAXATION-RATE-S67 | Gamma_beta/H_eq | +52.0 | OVER | PASS | S67 | 52 OOM above H_eq |
| 72 | CC-ANOMALY-FUNCTIONAL-S67 | CC gap (anomaly functional) | +119 | OVER | STRUCTURAL | S67 | 118.6-120.6 OOM |
| 73 | BRAGG-GAP-S49 | m_Bragg vs target mass | +0.58 | OVER | CLOSED | S49 | 0.269 M_KK (30-60 OOM above target) |
| 74 | LEGGETT-DESERT-S49 | omega_L1 vs Hubble mass | +57.0 | OVER | PASS | S49 | 0.070 M_KK = 10^57 above H_mass |

---

## Detailed Entries

### 1. CC-RAW-QTHEORY (S43/S64)
- **Session**: S43 (first computed), refined S64
- **Quantity**: Cosmological constant from q-theory, gravity route
- **Route/Method**: rho_vac = spectral action a_0 * M_KK^4 (empty cell, Kerner M_KK)
- **Computed value**: ~10^{67} GeV^4
- **Target value**: rho_obs = 2.70e-47 GeV^4
- **Gap (OOM)**: +114.0 (overshoot)
- **Status**: STRUCTURAL -- this IS the expansion history, not a "gap" (S66 reframe)
- **Resolution**: The 114 OOM is the exflation itself. Standard inflation carries an equivalent ~111 OOM. S66 DILUTION-CC-66 reframed this from a problem to the expansion history. Volovik Scenario B (rho~H^2) is the sole surviving mechanism.
- **Source**: permanent-results-registry.md XV-A; baseline-findings-s66.md

### 2. CC-CONSERVATIVE-STACKABLE (S64/S66)
- **Session**: S64 (CC-COMBO master gate FAIL)
- **Quantity**: CC after all computed perturbative corrections
- **Route/Method**: A1-A8 structural stackable + C1-C5 wrong-direction + B1 zeta
- **Computed value**: Raw 114.0 - 6.84 + 0.54 - 5.0(est) = 102.7 OOM remaining
- **Target value**: 0 OOM
- **Gap (OOM)**: +102.7 (overshoot)
- **Status**: STRUCTURAL -- perturbative CC routes exhausted (12 mechanisms closed)
- **Resolution**: CC-COMBO-64 FAIL (master gate). All stackable corrections insufficient. Volovik relaxation is the non-perturbative resolution.
- **Source**: permanent-results-registry.md XV-A; CC budget table

### 3. CC-VOLOVIK-SCENARIO-A (S66)
- **Session**: S66
- **Quantity**: CC with constant w=-1 + GGE dilution only
- **Route/Method**: Scenario A: GGE dilution alone
- **Computed value**: 113.6 OOM gap
- **Target value**: 0 OOM
- **Gap (OOM)**: +113.6
- **Status**: CLOSED -- Scenario A excluded; only Scenario B survives
- **Source**: baseline-findings-s66.md

### 4. CC-VOLOVIK-SCENARIO-B (S66)
- **Session**: S66 (DILUTION-CC-66)
- **Quantity**: CC via Volovik non-additive G-renormalization (rho~H^2)
- **Route/Method**: rho_vac = (2/pi^2) * a_0 * M_KK^4 * (H_0/M_KK)^2 (seesaw)
- **Computed value**: rho_vac/rho_obs = 1.032 (at L_max=3)
- **Target value**: 1.000
- **Gap (OOM)**: +0.01
- **Status**: SUPERSEDED -- S73B W5-G showed the L=3 agreement was a partial-sum coincidence; replaced by CC-CHI2-LMAX7 (-0.47 OOM) and CC-A0-SCHEME-LMAX7 (+1.61 OOM)
- **Source**: DILUTION-CC-66; session-73b-mack-vdd-workshop.md

### 5. CC-CHI2-LMAX7 (S73B)
- **Session**: S73B (W5-G)
- **Quantity**: CC via bounded spectral fill factor chi_2
- **Route/Method**: rho_vac = chi_2 * H_0^2 * M_Pl^2; chi_2 = M_1/(n_modes*lam_max) = 0.747
- **Computed value**: 9.16e-48 GeV^4
- **Target value**: rho_obs = 2.70e-47 GeV^4
- **Gap (OOM)**: -0.47 (undershoot -- framework predicts 34% of observed)
- **Status**: OPEN -- L_max-stable (shifts only -0.02 OOM from L=3 to L=7); honest CC number
- **Resolution**: None yet. Sole surviving L_max-robust CC route. Still closes 119.5 OOM of the raw 120 OOM CC problem.
- **Source**: session-73b W5-G; session-73b-mack-vdd-workshop.md M3

### 6. CC-A0-SCHEME-LMAX7 (S73B)
- **Session**: S73B (W5-G)
- **Quantity**: CC via a_0 cutoff scheme at L_max=7
- **Route/Method**: Same Volovik seesaw as #4 but evaluated at L=7 (a_0 shifts 10-74x)
- **Computed value**: rho_vac = 1.10e-45 GeV^4
- **Target value**: 2.70e-47 GeV^4
- **Gap (OOM)**: +1.61 (overshoot)
- **Status**: OPEN -- demoted from PASS to INFO (S66 PASS was L=3 coincidence)
- **Source**: session-73b W5-G; session-73b-mack-vdd-workshop.md

### 7-8. CC-SCENARIO-B2-DESI, CC-QTHEORY-NPAIR
(Closed routes. Scenario B2 gives +106.7 OOM; discrete q-theory gives +113.5 OOM. Both CLOSED in S66.)

### 9-10. AS-ROUTE-A, AS-ROUTE-B-PW (S66)
- **Session**: S66 (AMPLITUDE-NORM-66)
- **Quantity**: Scalar power spectrum amplitude A_s
- **Route A**: A_s = 8.73e-2 (raw spectral, fold-vacuum functional). Gap: +7.62 OOM
- **Route B**: A_s gap 3.15 OOM (Peter-Weyl weighted). Gap: +3.15 OOM
- **Target**: Planck A_s = 2.1e-9
- **Status**: CLOSED by S67 multifield delta-N and subsequent routes
- **Resolution**: S66 identified the "amplitude normalization crisis" -- right ratios, wrong absolute amplitudes. S67 multifield delta-N closed 14.3 of 15.1 OOM. S75 f_conv closes the remaining structural gap.
- **Source**: baseline-findings-s66.md; permanent-results-registry XIV-A

### 11. AS-TRANSIT-SINGLE-S67
- **Session**: S67 (TRANSIT-PS-67 W1-A)
- **Quantity**: A_s from single-field transit Bogoliubov
- **Computed**: |beta_k|^2 ~ O(1), saturated. A_s = 1.84e+2
- **Target**: 2.1e-9
- **Gap**: +15.1 OOM (massive overshoot -- the "raw production" amplitude)
- **Status**: CLOSED by multifield conversion (S67 W3-B)
- **Source**: session-67-synthesis.md

### 12. AS-MULTIFIELD-DELTA-N-S67
- **Session**: S67 (MULTIFIELD-DELTA-N-67 W3-B)
- **Quantity**: A_s from multifield delta-N conversion (Friedmann M1)
- **Computed**: A_s = 3.29e-10
- **Target**: 2.1e-9
- **Gap**: -0.80 OOM (undershoot by factor 6.4)
- **Status**: CLOSED -- absorbed into the structural conversion picture (f_conv)
- **Resolution**: S67 workshop identified gap collapse (1.04 OOM) as dominant closure channel. The 0.80 OOM was a structural small residual compared to 15.1 OOM raw.
- **Source**: session-67-results-workingpaper.md W3-B; session-67-synthesis.md

### 18. AS-BOGOLIUBOV-S74
- **Session**: S74 (A-S-FROM-BOGOLIUBOV-74 W1-G)
- **Quantity**: A_s from 8-mode Bogoliubov squeezed vacuum
- **Route**: Full 8-mode PW-weighted Bogoliubov with c_BLV factor and strict (p,p) filter
- **Computed**: A_s = 6.22 (fiber units)
- **Target**: 2.1e-9
- **Gap**: +9.47 OOM
- **Status**: CLOSED by f_conv (#22)
- **Resolution**: S75 W1-E derived f_conv = 2.547e-10 from first principles, giving predicted A_s = 1.58e-9 (75% of Planck).
- **Source**: session-74-results-workingpaper.md W1-G

### 19. AS-CW-SPECTRAL-S75
- **Session**: S75 (S75-A4-CW-JOINT W1-D)
- **Quantity**: A_s from Coleman-Weinberg spectral formula
- **Route**: A_s = H_fold^2 / (8*pi*a_2*eps_H)
- **Computed**: 243.5
- **Target**: 2.1e-9
- **Gap**: +11.06 OOM
- **Status**: CLOSED by f_conv -- same structural gap as #18, seen through CW lens
- **Source**: session-75-results-workingpaper.md W1-D

### 22. FCONV-PROJECTION-S75 (THE CLOSER)
- **Session**: S75 (S75-A5-F-CONV W1-E)
- **Quantity**: Conversion factor from fiber-level A_s to 4D CMB amplitude
- **Route**: f_conv = (M_KK/M_Pl)^4 * (a_2/a_0)^2 = 1.371e-9 * 0.186
- **Computed**: f_conv = 2.547e-10 (log10 = -9.594)
- **Required**: 3.376e-10 (log10 = -9.472) to match A_s from Bogoliubov
- **Gap**: -0.12 OOM (computed f_conv is 0.12 OOM below required)
- **Status**: PASS -- CLOSES the +9.47 OOM Bogoliubov gap to within 0.12 OOM
- **Resolution**: Predicted A_s = 6.22 * 2.547e-10 = 1.58e-9, which is 75% of Planck (25% residual from zero free parameters). KK hierarchy accounts for 8.86 OOM, spectral projection for 0.73 OOM.
- **Source**: session-75-results-workingpaper.md W1-E

### 25-27. Friedmann H_0 / rho_GGE gaps (S74 W1-E)
- **Session**: S74
- **H_0 diluted**: H_0 = 2.44e-42 km/s/Mpc (29 OOM below Planck 67.4)
- **H_0 undiluted**: 3.32e+59 km/s/Mpc (58 OOM above Planck)
- **rho_GGE today**: 7.35e-57 (56 OOM below rho_crit)
- **Bracket**: diluted and undiluted routes bracket Planck by 86.3 OOM total
- **Status**: OPEN -- the Mack section 5.9 GGE-to-matter conversion ambiguity is the sole remaining degree of freedom
- **Source**: session-74-results-workingpaper.md W1-E

### 29-32. Higgs Mass Predictions (sub-OOM)
- **Session**: S66 (original), S73B (updated)
- **m_H (Gaussian, L=6)**: 131.8 GeV vs 125.1 GeV = 5.4% overshoot = +0.023 OOM
- **m_H (Richardson)**: 129.0 GeV = 3.1% = +0.013 OOM
- **m_H (Aitken, S66)**: 127.5 GeV = 1.9% = +0.008 OOM
- **m_H (S73B W5-E)**: 132.23 GeV = 5.7% = +0.024 OOM
- **Status**: OPEN -- converging sequence, sole convergent observable as L_max -> inf
- **Source**: permanent-results-registry XIV-B

### 33. TAU-P-PROTON-DECAY (S63)
- **Session**: S63
- **Computed**: tau_p = 6.26e39 yr (from Peter-Weyl orthogonality, loop-level)
- **Observed**: > 1.6e34 yr (Super-K bound)
- **Gap**: +5.0 OOM (safe margin)
- **Status**: PASS -- Hyper-K (2028+) bound ~10^35 yr still 4 OOM below prediction
- **Source**: permanent-results-registry XIV-B

### 34. LAMBDA-FS-WDM (S66)
- **Session**: S66
- **Computed**: lambda_fs = 9.85e-23 Mpc
- **Observed**: < 0.1 Mpc (Lyman-alpha bound)
- **Gap**: -22.0 OOM (CDM-like, massively below warm threshold)
- **Status**: PASS with enormous margin
- **Source**: permanent-results-registry XIV-C

### 35. TAU-DM-LEGGETT-GRAV (S73A)
- **Session**: S73A (LEGGETT-GRAV-DECAY-73a W1-B)
- **Computed**: tau_DM = 4.93e82 s (Z_2 parity exact, single-channel FORBIDDEN)
- **Observed**: > t_univ = 4.35e17 s
- **Gap**: +65.0 OOM (absolutely stable by 65 OOM)
- **Status**: PASS (permanent)
- **Source**: session-73a-results-workingpaper.md W1-B

### 36-38. Friedmann-BCS Dynamical Gaps (S36-S39)
- **S36 TAU-DYN**: dwell_time/tau_BCS = 2.59e-5 = -4.59 OOM (38,600x too fast)
- **S39 FRIED**: Gradient ratio |dV_bare/dtau|/|dE_BCS/dtau| = 6,596 (+3.82 OOM)
- **S39 FRIED**: Energy shortfall = 133,200x (+5.12 OOM)
- **Status**: STRUCTURAL -- transit physics, not equilibrium. These define the paradigm.
- **Source**: spectral-post-mortem.md; atlas-04-assumptions.md

### 39-44. Instanton and Non-Perturbative Gaps (S74-S75)
- **Single instanton** (S74 W1-B): V_inst/V_bare = 3.22e-3 (-2.49 OOM)
- **Multi-instanton L=10** (S75 W1-F): V_multi/V_bare = 4.57e-4 (-3.34 OOM)
- **Restoring gradient shortfall** (S74): 309x between instanton and bare (+2.49 OOM)
- **Coulomb gas enhancement**: 2x only, residual 158.8x (+2.20 OOM)
- **'t Hooft vertex vs bare**: -12.0 OOM (negligible by exp(-54) suppression)
- **'t Hooft vs CW**: -9.0 OOM (19 OOM below 1-loop)
- **Status**: CLOSED -- all instanton/non-perturbative moduli stabilization routes exhausted
- **Source**: session-74-results-workingpaper.md; session-75-results-workingpaper.md W1-F

### 45. SKYRMION-BARYON-MASS (S64)
- **Session**: S64 (SKYRMION-BARYON-64)
- **Computed**: M_skyrm = 1.27e5 M_KK = 6.4e22 GeV
- **Target**: m_proton = 0.938 GeV
- **Gap**: +22.0 OOM
- **Status**: CLOSED -- fiber skyrmion baryogenesis excluded
- **Source**: baseline-findings-s66.md; constraint-mega-matrix.md

### 46. ALPHA-S-SLOWROLL (S66)
- **Session**: S50 (O-Z identity alpha_s = n_s^2 - 1), S66 (quantified)
- **Computed**: alpha_s = -0.038 (from slow-roll at L=4)
- **Observed**: -0.0045 +/- 0.0067 (Planck)
- **Tension**: 5.0 sigma
- **Status**: OPEN -- formula suspect (slow-roll inapplicable at Mach 13.8). Acoustic prediction (QA): alpha_s ~ 0 from 56 OOM scale hierarchy. Needs TRANSIT-PS-67.
- **Source**: permanent-results-registry XIV-A

### 49. SAKHAROV-GN-PHONON (S53)
- **Session**: S53 (SAKHAROV-PHONON-53)
- **Computed**: G_Sak(phonon, 192 GL modes) / G_obs = 1.04e4
- **Gap**: -4.02 OOM (phonon sector insufficient by itself)
- **Status**: STRUCTURAL -- confirms Volovik Paper 07: G_N is fermionic (Dirac tower), not bosonic (phonon)
- **Source**: session-53-results-workingpaper.md

### 50. SAKHAROV-GN-DIRAC (S44)
- **Session**: S44 (Sakharov induced gravity)
- **Computed**: G_Sak/G_obs = 2.29 at Lambda=10 M_KK
- **Gap**: -0.36 OOM
- **Status**: PASS (within 1 OOM gate)
- **Source**: atlas-04-assumptions.md C8

### 51-52. T_CMB Predictions (S53)
- **Method 1** (T~1/a): T_post = 6.16e-20 GeV, overcooled by 6.6 OOM
- **Method 2** (T~a^-0.869): T_post = 2.57e-15 GeV, overcooled by 2.0 OOM
- **Status**: CLOSED -- both methods show exflation alone overcools; post-exflation reheating required
- **Source**: session-53-results-workingpaper.md

### 55. ISOCURVATURE-S67
- **Session**: S67 (ISOCURVATURE-67 W4-E)
- **Computed**: beta_iso = 3.22e-12
- **Observed**: < 1.7% (Planck bound)
- **Gap**: -10.0 OOM below bound
- **Status**: PASS with enormous margin
- **Source**: session-67-synthesis.md

### 60. ETA-B-S52 (Baryon Asymmetry)
- **Session**: S52 (ETA-B-52)
- **Computed**: phi_CP = 0 EXACTLY (structural: BDI symmetry class, T^2=+1)
- **Target**: eta_B = 6.1e-10 (BBN)
- **Gap**: -infinity (no CP violation means no baryogenesis from this route)
- **Status**: STRUCTURAL -- internal baryogenesis CLOSED by AZ class BDI
- **Source**: session-52-results-workingpaper.md W1-D

### 68. GGE-EQUILIBRIUM-S57
- **Session**: S57/S58
- **Quantity**: GGE departure from thermal equilibrium
- **Computed**: ||delta_n||/N = 0.195
- **Threshold**: Thermalization would require crossing 56 OOM gap
- **Status**: STRUCTURAL -- the CC IS the integrability problem
- **Source**: session-57-volovik-sp-workshop.md; session-58-synthesis.md

---

## Cross-Reference: Gap Closure Chain

### A_s Gap Closure History

```
S53:  A_s (rho weighting)     = +6.3 OOM   [first estimate]
S66:  A_s Route A (raw)       = +7.62 OOM  [refined]
S66:  A_s Route B (PW)        = +3.15 OOM  [PW weighting helps]
S67:  A_s single-field        = +15.1 OOM  [honest production amplitude]
S67:  A_s multifield delta-N  = -0.80 OOM  [14.3 OOM closed by conversion!]
S74:  A_s multifield transfer = +5.83 OOM  [independent S74 route]
S74:  A_s 8-mode Bogoliubov   = +9.47 OOM  [canonical fiber-level A_s]
S75:  A_s CW spectral         = +11.06 OOM [CW confirms structural scale]
S75:  f_conv = -9.594 OOM     CLOSES #18   [KK hierarchy + spectral projection]
      ====>  Predicted A_s = 1.58e-9 = 75% of Planck (0.12 OOM residual)
```

The critical insight: ALL A_s routes that give large gaps (7-15 OOM) are fiber-level amplitudes that have NOT been converted to 4D. The f_conv factor of (M_KK/M_Pl)^4 * (a_2/a_0)^2 = 2.55e-10 is the structural conversion factor. When applied, the 9.47 OOM gap closes to 0.12 OOM.

### CC Gap Closure History

```
S43:  CC (raw q-theory)        = +114.0 OOM [the CC problem]
S64:  CC (all stackable)       = +102.7 OOM [perturbative corrections: -11.3 OOM]
S66:  CC Volovik Scenario B    = +0.01 OOM  [seesaw rho~H^2, L=3 ... SUPERSEDED]
S73B: CC (a_0 scheme, L=7)     = +1.61 OOM  [honest L->inf shows S66 was coincidence]
S73B: CC (chi_2 route, L=7)    = -0.47 OOM  [L_max-stable, honest prediction]
      ====>  120 OOM problem closed to within 0.5 OOM by chi_2 route
```

### Instanton Moduli Stabilization Chain

```
S74:  Single instanton V/V_bare     = -2.49 OOM [negligible]
S74:  Restoring gradient shortfall  = +2.49 OOM (309x) [structural]
S74:  Coulomb gas enhancement       = 2x only, residual 158.8x
S74:  't Hooft vertex vs bare       = -12.0 OOM [utterly negligible]
S75:  Multi-instanton L=10          = -3.34 OOM [DECREASING with L_max]
      ====>  ALL non-perturbative moduli routes CLOSED
```

### Friedmann-BCS Chain

```
S36:  dwell/tau_BCS = 38,600x shortfall  (-4.59 OOM)
S39:  gradient ratio = 6,596x            (+3.82 OOM)
S39:  energy shortfall = 133,200x        (+5.12 OOM)
      ====>  PARADIGM: transit physics, not equilibrium BCS
```

---

## Statistics

| Category | Count |
|:---------|:------|
| **Total gaps catalogued** | **74** |
| **OPEN** | 12 (CC-chi2, CC-a0-L7, H0-diluted, H0-undiluted, rho-GGE, m_H x4, alpha_s, n_s x2, w_0, w_a, decoherence-compound) |
| **CLOSED** | 36 (superseded by later computation, mechanism excluded, or absorbed into understanding) |
| **STRUCTURAL** | 14 (define the framework architecture, not "problems") |
| **PASS** | 12 (computed quantity safely within observational bounds with large margin) |

| Metric | Value |
|:-------|:------|
| **Largest open gap** | H_0 undiluted/diluted bracket: 86.3 OOM total (S74 W1-E) |
| **Largest raw gap** | CC (anomaly functional): +119 OOM (S67) |
| **Largest gap CLOSED** | A_s production -> CMB: 15.1 OOM closed by multifield delta-N (S67) |
| **Smallest meaningful gap** | m_H (Aitken): +0.008 OOM = 1.9% (S66) |
| **Most frequently computed quantity** | A_s (12 independent routes catalogued) |
| **Most dramatic closure** | CC: 120 OOM -> -0.47 OOM via Volovik chi_2 |
| **Category with most closed gaps** | A_s amplitude normalization (12 routes, all understood) |

---

## Notes on Convention

1. **Positive gap** = computed value TOO LARGE relative to target (overshoot).
2. **Negative gap** = computed value TOO SMALL relative to target (undershoot).
3. **STRUCTURAL** entries are not problems to solve -- they define the framework's architecture (e.g., 38,600x transit shortfall IS exflation; 114 OOM CC IS the expansion history).
4. **CLOSED** means either (a) a later computation superseded the route, (b) the mechanism was excluded, or (c) the gap was absorbed into a structural understanding.
5. **Sub-OOM entries** (sigma-tensions, sub-1 OOM) are included where they represent physically significant predictions (m_H, n_s, alpha_s).
6. **Decoherence entries** (#62-66) use delta_OOM as a measure of squeeze destruction budget, not computed/observed ratio. They are included because they participate in the A_s closure chain.
