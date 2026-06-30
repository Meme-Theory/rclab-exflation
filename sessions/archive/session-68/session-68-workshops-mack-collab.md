# Mack Cosmic Bridge -- Collaborative Feedback on S68 Workshops

**Author**: Mack Cosmic Bridge
**Date**: 2026-04-05
**Re**: S68 Workshop Results (Lizzi x Transit, Landau x Transit, Volovik x Mack)

---

## Section 1: Key Observations

I participated directly in WS3 (Volovik x Mack), so my primary contribution here is reviewing WS1 and WS2 through the observational cosmology lens -- specifically, what do the spectral functional and BCS condensate findings translate to in terms of observable signatures, forecast constraints, and the framework's confrontation with data?

**WS1 (Lizzi x Transit): Three structural results with observational consequences.**

1. **|T_scalar|^2 = 1 (Weinberg superhorizon conservation) is functional-independent.** This is the session's most consequential structural finding from my perspective. It means the entire observational power spectrum -- n_s, alpha_s, A_s -- is set at the fold, full stop. No post-transit dynamical process modifies it. For observational cosmology, this is a double-edged result: it localizes both the framework's successes (n_s = 0.9595 at 1.25-sigma) and its failures (A_s gap of 0.755 OOM) to the spectral action geometry at a single instant. There is no escape route through late-time dynamics or transfer-function corrections.

2. **The eps_H cancellation theorem provides a 30x suppression of BCS corrections to n_s.** This is observationally decisive because it explains why n_s is the framework's most robust CMB prediction while A_s (which is NOT protected by the theorem) carries the dominant chi^2 contribution. The theorem creates a natural partition between "shape" observables (n_s, alpha_s, r) that are structurally protected and "scale" observables (A_s, m_H, alpha_s(M_Z)) that are not. From a forecast perspective, this means future CMB experiments testing n_s (Planck, CMB-S4) are testing the spectral action curvature directly, while experiments testing A_s are testing mode physics (BCS squeeze, off-Jensen dynamics).

3. **The spectral functional reduces to three numbers at the fold.** Lizzi's emergence E1, confirmed by Transit, shows that the infinite-dimensional spectral functional choice collapses to three real numbers: z''/z, d(z''/z)/dtau, and d^2(z''/z)/dtau^2 evaluated at the fold. The 60-decade scale hierarchy between k_tach and k_CMB projects out all higher information. This is observationally powerful because it means the CMB constrains exactly three microscopic parameters -- and the cutoff f(x) = sqrt(x) either satisfies them or does not, with no room for tuning.

**WS2 (Landau x Transit): The BCS condensate budget constrains A_s gap closure.**

1. **Non-BD squeeze parameter revised downward.** Landau's variance-weighted calculation gives r_eff = 0.338 (central), producing cosh(2r_eff) = 1.237, or 0.093 OOM enhancement. This is 2-3x below the Lizzi-Transit naive estimate of 0.26 OOM, because the optical branch (50.6% of variance) has low squeeze (r ~ 0.12). Transit's reconciled range is 0.07-0.19 OOM. This matters observationally because it means the non-BD channel alone cannot close the A_s gap -- it contributes at most 25% of the needed 0.755 OOM.

2. **The two-timescale hierarchy resolves the Kibble-Zurek concern.** The ordering tau_relax ~ 2/M_KK << dt_transit ~ 663/M_KK << 1/H ~ 1000/M_KK means the BCS gap tracks equilibrium during transit (adiabatic for pairing) while cosmological modes are produced impulsively (diabatic for the Hubble flow). The KZ mechanism produces O(3) phase defects on the CG(24) graph that seed Leggett DM modes, but does NOT modify the squeeze parameter. This is observationally relevant because it connects the DM relic composition to a specific condensed matter mechanism -- the DM abundance is not just "computed" but has a physical production mechanism with testable intermediate steps.

3. **Total BCS correction budget is bounded: 0.15-0.27 OOM.** This is the honest assessment. The hard upper bound from the finite Hilbert space is 2<N_pair> + 1 = 9 (0.95 OOM), and the realistic range given the branch structure is 0.15-0.27 OOM. The remaining gap of 0.49-0.61 OOM must come from non-BCS physics (off-Jensen dynamics, normalization chain resolution). The squeeze phase phi_eff introduces an additional uncertainty: at r_eff = 0.34, the enhancement ranges from 0.89 (destructive) to 1.58 (constructive) depending on the unknown phase. This is the single most important undetermined quantity for A_s.

**WS3 (Volovik x Mack): ISW tracking as observational discovery.**

The workshop's most significant output was the identification of the ISW tracking signature: the Volovik tracking vacuum (rho_vac ~ H^2) produces induced DE perturbations with c_s^2_DE(eff) = 0, which modifies the ISW-galaxy cross-correlation relative to LCDM by an estimated 7.6-12.3%. This was computed post-workshop as ISW-TRACKING-68 PASS. I treat this in detail in Section 2.

---

## Section 2: Assessment of Key Findings

### Finding 1: phi_eff as the A_s bottleneck

Transit's exact solution (Tr1, Eq. Tr1.19) shows the enhancement factor is not simply cosh(2r_eff) but:

P(non-BD)/P(BD) = cosh(2r_eff) + (sqrt(2)/3) sinh(2r_eff) cos(phi_eff)

At r_eff = 0.34: enhancement ranges from 0.89 (phi_eff = pi) to 1.58 (phi_eff = 0). The squeeze phase phi_eff is the relative phase between the BCS condensate and the transit Bogoliubov transformation. It is a computable quantity that has not been computed.

**Observational consequence**: The A_s gap (0.755 OOM, factor 5.69x) is the framework's dominant chi^2 contributor (3466 of 3938.5 total). Whether the non-BD channel helps or hurts depends entirely on phi_eff. If phi_eff ~ pi, the non-BD correction makes the gap WORSE, and the total BCS budget drops below 0.1 OOM. If phi_eff ~ 0, the non-BD correction contributes 0.20 OOM, and the combined BCS budget reaches ~0.27 OOM. This single phase angle determines whether the A_s gap is "closing" or "opening."

**Forecast implication**: Until phi_eff is computed, the A_s tension reported in the joint observational table (S68 W4-A) carries an unquantified systematic. The chi^2 = 3938.5 is computed assuming A_s = 3.691e-10. If phi_eff = 0 (constructive), A_s rises to ~5.83e-10, reducing the gap from 0.755 to 0.56 OOM. If phi_eff = pi (destructive), A_s falls to ~3.29e-10, increasing the gap to 0.81 OOM. The chi^2 range is approximately [2500, 4500].

### Finding 2: The three-number reduction and n_s structural limit

Lizzi's A-T5 proves that no smooth cutoff functional pushes n_s to the Planck central value 0.9649. The maximum achievable is n_s ~ 0.961-0.963. The 1.25-sigma gap (n_s = 0.9595 vs 0.9649) is structural within the smooth cutoff family.

**Observational consequence**: CMB-S4 will measure n_s to sigma ~ 0.002 (combining temperature, polarization, and lensing). If the true n_s = 0.9649 (Planck central), CMB-S4 will measure n_s = 0.9649 +/- 0.002. The framework's prediction n_s = 0.9595 would be 2.7-sigma from CMB-S4's measurement -- moving from "comfortable" to "tension." If Planck's own central value shifts downward (as some analyses with extended models suggest), the tension could ease. The n_s test sharpens from a 1.25-sigma Planck result to a potential 2.7-sigma CMB-S4 result within the decade.

### Finding 3: ISW tracking as the framework's nearest unique discriminant

The WS3 discovery that the Volovik tracking vacuum produces c_s^2_DE(eff) = 0 (perturbation slaved to matter) is the workshop's observational contribution. This differs from LCDM (delta_DE = 0 exactly) and from quintessence (c_s^2 = 1).

**Observational consequence**: The ISW-TRACKING-68 computation (performed post-workshop) gives:
- FW vs quintessence (c_s^2 = 0 vs c_s^2 = 1): 7.6% difference in ISW-galaxy C_l at l < 30
- FW vs LCDM: 12.3% difference
- Euclid sensitivity: 2.5-sigma detection (6 tomographic bins)
- 21cm (l_max ~ 10^5): 7.9-sigma detection

This is the ONLY substrate-specific signature detectable with planned instruments on a < 15-year timeline that is not degenerate with a generic w_0CDM model. It upgrades the framework's prediction surface from 6D to 7D by adding c_s^2_DE(eff) = 0 as a testable dimension.

### Finding 4: Four-fold w_a lock

The WS3 workshop strengthened the w_a = 0 protection from three independent locks (integrability, Josephson, frozen texture) to four, adding the thermalization coincidence argument: even if integrability breaks, Gamma_therm/H_0 ~ 10^{59} (from M_KK ~ 10^16 GeV and <r> = 0.41), meaning the system has already thermalized. Producing w_a requires Gamma_therm ~ H_0, which demands 59 OOM of suppression -- either MBL with disorder W/J ~ 10^3 (vs framework W/J ~ 2) or a BCS scale 59 OOM lower than computed. Both are physically excluded.

**Observational consequence**: The w_a = 0 prediction is as rigid as it gets. DESI DR3 is a clean pass/fail test with no escape routes within the framework.

---

## Section 3: Collaborative Suggestions

### Suggestion 1: ISW tracking as the priority forecast computation

The ISW-TRACKING-68 computation was performed post-workshop and registered PASS (7.6% FW/Quint, 12.3% FW/LCDM). The next step is a full CLASS/CAMB Boltzmann integration comparing the three models (tracking, LCDM, smooth w_0CDM) against the Planck 2018 ISW-galaxy cross-correlation data. This is the only computation that could produce a detection with EXISTING data. Priority: HIGHEST for S69.

### Suggestion 2: Cross-correlation of ISW tracking with f*sigma_8

The ISW tracking signature (c_s^2 = 0) and the f*sigma_8 suppression (2-3% below LCDM) are not independent -- both arise from w_0 = -0.918 and the tracking vacuum. Their JOINT constraint power exceeds the sum of individual constraints because they probe different redshift ranges (ISW peaks at z ~ 0.5, f*sigma_8 is measured at z = 0.3-1.3) and different modes (ISW is l < 30, RSD is k ~ 0.1 h/Mpc). A combined Fisher forecast for Euclid (ISW + RSD + lensing) would quantify whether the framework can be distinguished from w_0CDM at > 3-sigma with a single survey.

### Suggestion 3: phi_eff computation from the coupled BCS-Bogoliubov system

The squeeze phase phi_eff is the largest single systematic in the A_s prediction. It determines whether the non-BD correction contributes +0.20 OOM (constructive) or -0.05 OOM (destructive). The computation requires solving the BCS gap equation and the Mukhanov-Sasaki mode equation simultaneously at the fold, extracting the relative phase between the condensate formation and the Bogoliubov transformation. This is a well-defined problem with no free parameters. Priority: HIGH for S69.

### Suggestion 4: Normalization chain resolution (W1-A mismatch)

Transit's Tr3 identifies a factor 12.9 mismatch (1.11 OOM) between the direct amplitude chain and the delta-N chain. This exceeds the A_s gap itself. Until this is resolved, the sign of the A_s problem is uncertain: the framework might be undershooting Planck (current assessment) or overshooting it (if the direct chain is correct). Resolution does not require new physics, only careful bookkeeping of normalization conventions between the mode equation and the delta-N formalism. Priority: HIGH.

### Suggestion 5: Pre-register the CMB-S4 n_s test

The structural limit n_s < 0.963 within the smooth cutoff family means CMB-S4 (sigma ~ 0.002) will produce a 2.7-sigma test if Planck's central value holds. Pre-register: framework predicts n_s in [0.955, 0.963]. PASS if CMB-S4 measures n_s in this range. FAIL if n_s > 0.970 (above smooth cutoff maximum). The gate is clean, zero-parameter, and on a ~2030 timeline.

---

## Section 4: Connections to Framework

The three workshops collectively advance the framework's observational position in complementary ways:

1. **WS1 localizes the observational interface.** By proving |T|^2 = 1 and reducing the spectral functional to three numbers at the fold, WS1 establishes that the framework's CMB confrontation depends on exactly three microscopic quantities. This is the tightest parameterization of any model I have encountered -- standard slow-roll inflation has two free parameters (V and V') from an infinite-dimensional potential, while the framework has three numbers from a finite spectral action.

2. **WS2 bounds the production-sector contribution.** The BCS correction budget (0.15-0.27 OOM) is now structurally bounded, with a hard ceiling of 0.95 OOM from the finite Hilbert space. This removes BCS physics from the list of potentially large unknowns and identifies the geometric sector (off-Jensen, atlas Q9) as the sole remaining source of O(1) corrections to A_s. The connection to observational cosmology is direct: the A_s gap is the framework's dominant chi^2 contributor, and its resolution requires specific computations (phi_eff, normalization chain, off-Jensen) rather than new physics.

3. **WS3 discovers a new observable.** The ISW tracking signature upgrades the prediction surface from 6D to 7D and provides the framework's nearest unique discriminant on a < 15-year timeline. The connection to the Volovik q-theory vacuum program is structural: the tracking relation rho_vac ~ H^2 is FUNCTIONAL-INDEPENDENT (Lizzi-Transit E1), meaning the ISW signature survives regardless of the spectral functional choice. This makes it the most robust substrate-specific prediction in the framework's observational portfolio.

The three workshops also converge on the framework's constraint structure: one genuine pressure point (DESI w_a, 3.0-sigma), one dominant precision gap (A_s, 0.755 OOM), and one new observational discovery (ISW tracking, potentially detectable now). The Leggett DM paradox that I elevated to "most critical internal contradiction" in WS3 was resolved by the S67 Z_2 parity selection rule (Volovik's Round 3 correction), leaving DESI DR3 as the sole existential threat.

---

## Section 5: Open Questions

1. **Is the ISW tracking modification partially canceled in the full Boltzmann integration?** My crude estimate (M-R2.5) gives ~20% modification; the post-workshop computation (ISW-TRACKING-68) gives 7.6-12.3%. The difference suggests partial cancelation from the tracking vacuum adjusting to reduce potential decay. A full Boltzmann integration with matter-DE coupling at the perturbation level is needed to confirm the amplitude.

2. **What is the Euclid ISW-galaxy cross-correlation covariance matrix?** The 2.5-sigma Euclid forecast for ISW tracking assumes independent multipoles. The actual ISW-galaxy covariance includes mode coupling from nonlinear growth and survey geometry. The degradation from idealized to realistic covariance could reduce the significance by 30-50%.

3. **Does the tracking-induced delta_DE modify the CMB lensing potential?** The induced DE perturbation (c_s^2 = 0) modifies the Weyl potential at late times, which contributes to CMB lensing through the convergence power spectrum C_l^{kappa kappa}. The modification would be at the ~1% level on C_l^{kappa kappa} at l ~ 100-500, potentially detectable by CMB-S4 lensing reconstruction (sigma ~ 0.5% per bandpower). This is a separate test from the ISW cross-correlation.

4. **How does the 7D prediction surface compare to the EDE (Early Dark Energy) model family?** EDE models modify the expansion history at z ~ 3000-5000, affecting r_d and thereby the BAO distances. If DESI DR3 shifts toward w_a ~ 0 (Scenario B), the remaining w_0 discrimination is between the framework (w_0 = -0.918 derived) and EDE variants that produce w_0 > -1 with w_a ~ 0 from early-time modification. The 7D surface may not discriminate against EDE in the dark energy dimensions, but the n_s and r dimensions would differ (EDE shifts the CMB peak structure).

5. **Can the folded bispectrum amplitude bound be improved before 21cm?** The CMB-S4 sensitivity for the folded shape is sigma = 6.9, far above f_NL^folded = 0.129. But LSS bispectrum from Euclid spectroscopic data at z = 0.9-1.8 could in principle constrain the galaxy bispectrum folded template. The galaxy-bias uncertainty is the limiting systematic. A forecast for the Euclid galaxy bispectrum folded shape would determine if there is any intermediate path between CMB-S4 (insufficient) and 21cm (2040s).

---

## Section 6: Computation Suggestions Summary

| # | Computation | Input Data | Output | Pre-Registered Gate | Priority |
|:--|:-----------|:-----------|:-------|:-------------------|:---------|
| 1 | ISW-TRACKING-BOLTZMANN-69: Full CLASS/CAMB Boltzmann ISW for tracking vs LCDM vs quintessence | w_0=-0.918, c_s^2=0(FW)/1(quint), Planck ISW-galaxy data | C_l^{Tg} at l=2-30, SNR vs Planck + Euclid projections | PASS if Delta>5% at l<30 (Euclid threshold); FAIL if Delta<1% | HIGHEST |
| 2 | PHI-EFF-BCS-BOGOL-69: Squeeze phase from coupled BCS gap + mode equation | D_K spectrum, Delta(tau), z''/z(tau) at fold | phi_eff, full A_s enhancement factor including interference | PASS if enhancement in [1.3,4.0]; INFO if [1.0,1.3]; FAIL if <1.0 | HIGH |
| 3 | AS-NORMALIZATION-CHAIN-69: Resolve factor 12.9 mismatch between direct and delta-N chains | W1-A amplitude chain, S67 delta-N chain, normalization conventions | Consistent A_s from both chains, or identification of physics gap | INFO (diagnostic, not pass/fail) | HIGH |
| 4 | EUCLID-ISW-RSD-JOINT-69: Combined Fisher forecast for Euclid ISW + RSD + lensing vs w_0CDM | ISW-TRACKING-68, FSIGMA8-65, sigma_8 from growth factor | Joint chi^2 for FW vs w_0CDM at Euclid sensitivity | INFO: report sigma for FW/w_0CDM discrimination | MEDIUM-HIGH |
| 5 | CMB-S4-NS-PREREGISTER-69: Pre-register n_s structural limit test for CMB-S4 | n_s=0.9595, sigma(CMB-S4)~0.002, cutoff family max n_s~0.963 | Decision rules for CMB-S4 n_s measurement | PASS if n_s in [0.955,0.963]; FAIL if n_s>0.970 | MEDIUM |
| 6 | EUCLID-LENSING-TRACKING-69: Tracking-induced modification to CMB lensing C_l^{kk} | c_s^2_DE=0, w_0=-0.918, Planck lensing bandpowers | Delta(C_l^{kk})/C_l^{kk} at l=100-500 | PASS if Delta>0.5% (CMB-S4 detectable); FAIL if <0.1% | MEDIUM |
| 7 | EUCLID-GALAXY-FOLDED-69: Galaxy bispectrum folded shape forecast from Euclid spectroscopic | f_NL^folded=0.129, Euclid spec survey at z=0.9-1.8, galaxy bias model | sigma(f_NL^folded) from galaxy bispectrum | INFO: report sigma and whether intermediate path exists | LOW-MEDIUM |

---

## Closing Assessment

The three S68 workshops collectively sharpen the framework's observational position from "interesting zero-parameter model with some tensions" to a quantified constraint map. The key outcomes by workshop:

- **WS1** establishes that the CMB interface depends on three numbers at the fold, with n_s protected (30x suppression) and A_s unprotected (full BCS correction propagates). The spectral functional question is settled: cutoff with f(x) = sqrt(x) is the sole survivor, and the 1.25-sigma n_s gap is structural within the smooth cutoff family.

- **WS2** bounds the BCS contribution to A_s at 0.15-0.27 OOM (hard ceiling 0.95 OOM), identifies phi_eff as the critical unknown, and establishes the two-timescale hierarchy that simultaneously permits adiabatic gap formation and impulsive mode production.

- **WS3** discovers the ISW tracking signature (c_s^2_DE(eff) = 0), upgrades the prediction surface to 7D, strengthens the w_a = 0 lock to four-fold, and resolves the Leggett DM paradox via the S67 Z_2 selection rule.

The framework's observational fate concentrates on three timescales: DESI DR3 (~2027, w_a pass/fail), Euclid (~2030, ISW tracking + f*sigma_8 + lensing), and LiteBIRD (~2034, r = 0.024). The 21cm folded bispectrum (~2040s+) remains the sole unique confirmation channel. The next 12-18 months (DESI DR3) carry the highest information density. The ISW tracking computation is the one new test that could produce results with existing data and should be the top S69 priority.

---

## Wrap-Up

### What Changed

- **A new observable entered the prediction surface.** The ISW tracking signature (c_s^2_DE(eff) = 0 from the Volovik tracking vacuum) upgrades the framework's discriminant surface from 6D to 7D. This is the only substrate-specific signature detectable with planned instruments on a < 15-year timeline that is not degenerate with generic w_0CDM. It is also potentially testable against existing Planck ISW-galaxy data.
- **The A_s gap acquired a sign ambiguity.** The squeeze phase phi_eff (undetermined) controls whether BCS corrections contribute +0.20 OOM (constructive, phi_eff ~ 0) or -0.05 OOM (destructive, phi_eff ~ pi) to the dominant chi^2 contributor. Until phi_eff is computed, the framework's A_s prediction carries an unquantified systematic spanning chi^2 ~ [2500, 4500].
- **The CMB interface collapsed to three numbers.** Lizzi's three-number reduction (z''/z and its first two tau-derivatives at the fold) means the entire observational power spectrum is set by exactly three microscopic quantities evaluated at a single instant. No post-transit dynamics modify the shapes. This is the tightest parameterization of any inflationary-class model I have encountered.

### What Holds

- **n_s remains the framework's most robust CMB prediction.** The eps_H cancellation theorem (WS1) provides 30x suppression of BCS corrections, explaining why n_s = 0.9595 (1.25-sigma) is structurally protected while A_s is not. The n_s structural limit (< 0.963 within smooth cutoffs) is a permanent wall.
- **w_a = 0 is locked four-fold.** Integrability, Josephson quantization, frozen texture, and thermalization coincidence (Gamma_therm/H_0 ~ 10^59) each independently enforce w_a = 0. DESI DR3 remains a clean pass/fail with no escape routes within the framework.
- **The ISW tracking signature is functional-independent.** The tracking relation rho_vac ~ H^2 and its perturbation consequence c_s^2_DE(eff) = 0 survive regardless of which spectral functional is chosen (Lizzi-Transit E1). This makes it the most robust substrate-specific prediction in the observational portfolio.

### What Breaks or Strains

- **A_s gap dominates total chi^2.** The 0.755 OOM gap (factor 5.69x) accounts for 3466 of 3938.5 total chi^2 across 18 observables. The BCS correction budget (0.15-0.27 OOM) covers at most 36% of the gap. The remaining 0.49-0.61 OOM requires non-BCS physics (off-Jensen dynamics, normalization chain resolution) that is currently uncomputed.
- **The normalization chain mismatch (factor 12.9) is unresolved.** Transit's Tr3 identifies a 1.11 OOM discrepancy between the direct amplitude chain and the delta-N chain -- larger than the A_s gap itself. Until reconciled, the sign of the A_s problem is uncertain: the framework may undershoot or overshoot Planck.
- **CMB-S4 will sharpen n_s from comfort to tension.** The structural limit n_s < 0.963 means CMB-S4 (sigma ~ 0.002) will push the current 1.25-sigma Planck gap to a potential 2.7-sigma test if the central value holds. The framework has no mechanism to reach n_s = 0.9649.

### Carry-Forward Computations

1. **ISW-TRACKING-BOLTZMANN-69**: Full CLASS/CAMB Boltzmann ISW for tracking (c_s^2=0) vs LCDM vs quintessence (c_s^2=1). Input: w_0=-0.918, Planck ISW-galaxy data. Gate: PASS if Delta > 5% at l < 30 (Euclid threshold); FAIL if Delta < 1%. Priority: HIGHEST.
2. **PHI-EFF-BCS-BOGOL-69**: Squeeze phase from coupled BCS gap + Mukhanov-Sasaki mode equation at the fold. Input: D_K spectrum, Delta(tau), z''/z(tau). Gate: PASS if enhancement in [1.3, 4.0]; INFO if [1.0, 1.3]; FAIL if < 1.0. Priority: HIGH.
3. **AS-NORMALIZATION-CHAIN-69**: Resolve factor 12.9 mismatch between direct and delta-N amplitude chains. Input: W1-A chain, S67 delta-N chain, normalization conventions. Gate: INFO (diagnostic). Priority: HIGH.
4. **EUCLID-ISW-RSD-JOINT-69**: Combined Fisher forecast for Euclid ISW + RSD + lensing vs w_0CDM. Input: ISW-TRACKING-68, FSIGMA8-65, sigma_8. Gate: INFO (report sigma for FW/w_0CDM discrimination). Priority: MEDIUM-HIGH.
5. **CMB-S4-NS-PREREGISTER-69**: Pre-register n_s structural limit test. Gate: PASS if n_s in [0.955, 0.963]; FAIL if n_s > 0.970. Priority: MEDIUM.
6. **EUCLID-LENSING-TRACKING-69**: Tracking-induced modification to CMB lensing C_l^{kk} at l = 100-500. Gate: PASS if Delta > 0.5% (CMB-S4 detectable); FAIL if < 0.1%. Priority: MEDIUM.
7. **EUCLID-GALAXY-FOLDED-69**: Galaxy bispectrum folded shape forecast from Euclid spectroscopic survey. Gate: INFO (report sigma and intermediate detection path). Priority: LOW-MEDIUM.

### Closing Line

The three S68 workshops reduced the framework's observational interface to three computable numbers, discovered the ISW tracking discriminant as the nearest unique test, and concentrated the entire precision crisis on a single undetermined phase -- phi_eff -- whose computation is the gateway to knowing whether the A_s gap is closing or widening.
