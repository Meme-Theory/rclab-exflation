# DESI DR2 Results II: Measurements of Baryon Acoustic Oscillations and Cosmological Constraints

**Author(s):** DESI Collaboration (M. Abdul Karim et al.)
**Year:** 2025
**Journal:** [INCOMPLETE - not extractable from PDF, likely submitted to a journal]
**arXiv:** 2503.14738
**Relevance:** CRITICAL

---

## Abstract

We present baryon acoustic oscillation (BAO) measurements from more than 14 million galaxies and quasars drawn from the Dark Energy Spectroscopic Instrument (DESI) Data Release 2 (DR2), based on three years of operation. For cosmology inference, these galaxy measurements are combined with DESI Lyman-alpha forest BAO results presented in a companion paper. The DR2 BAO results are consistent with DESI DR1 and SDSS, and their distance-redshift relationship matches those from recent compilations of supernovae (SNe) over the same redshift range. The results are well described by a flat LCDM model, but the parameters preferred by BAO are in mild, 2.3 sigma tension with those determined from the cosmic microwave background (CMB), although the DESI results are consistent with the acoustic angular scale theta_* that is well-measured by Planck. This tension is alleviated by dark energy with a time-evolving equation of state parametrized by w_0 and w_a, which provides a better fit to the data, with a favored solution in the quadrant with w_0 > -1 and w_a < 0. This solution is preferred over LCDM at 3.1 sigma for the combination of DESI BAO and CMB data. When also including SNe, the preference for a dynamical dark energy model over LCDM ranges from 2.8-4.2 sigma depending on which SNe sample is used. We present evidence from other data combinations which also favor the same behavior at high significance. From the combination of DESI and CMB we derive 95% upper limits on the sum of neutrino masses, finding sum m_nu < 0.064 eV assuming LCDM and sum m_nu < 0.16 eV in the w_0 w_a model. Unless there is an unknown systematic error associated with one or more datasets, it is clear that LCDM is being challenged by the combination of DESI BAO with other measurements and that dynamical dark energy offers a possible solution.

---

## Key Arguments and Derivations

### Section I-II: DESI Instrument and Data

DESI is a spectroscopic survey instrument on the 4-m Mayall Telescope at Kitt Peak, deploying 5000 fibers via a robotic focal plane assembly. DR2 encompasses three years of operation (May 2021 through April 2024), containing over 30 million galaxy and quasar redshifts, of which ~14 million are used in this analysis. The survey observes four tracer classes: Bright Galaxy Sample (BGS, z = 0.1-0.4), Luminous Red Galaxies (LRG, z = 0.4-1.1), Emission Line Galaxies (ELG, z = 0.8-1.6), and Quasars (QSO, z = 0.8-3.5), plus the Lyman-alpha forest (z = 1.8-4.2).

DR2 represents a significant increase over DR1: ELG sample grew by factor 2.7, LRG and QSO by factors 2.1 and 1.7 respectively. The total effective volume of the combined samples exceeds 42 Gpc^3.

### Section III: BAO Measurements

BAO measurements are derived from the two-point correlation function (2PCF) using the Landy-Szalay estimator. The scaling parameters alpha_parallel and alpha_perpendicular relate the BAO features to cosmology via alpha_||(z) = D_H(z) r_d^fid / (D_H^fid(z) r_d) and alpha_perp(z) = D_M(z) r_d^fid / (D_M^fid(z) r_d). The acoustic feature is detected with statistical significance ranging from 5.6 sigma (QSO) to 14.7 sigma (LRG3+ELG1), the latter being the strongest BAO detection from a galaxy survey to date.

### Section VI: LCDM Constraints

Within flat LCDM, DESI BAO alone constrains Omega_m = 0.295 +/- 0.015 (with BBN prior). Combined with CMB, the constraints tighten considerably. However, the BAO-preferred parameters show a mild 2.3 sigma tension with CMB parameters, though consistency with the acoustic angular scale theta_* is maintained.

### Section VII: Dark Energy

In the w_0 w_a CDM model (w(a) = w_0 + w_a(1-a)), the data favor w_0 > -1 and w_a < 0 (the "Quintom B" quadrant). Key constraints:

- DESI + CMB: 3.1 sigma preference for dynamical DE over LCDM
- DESI + CMB + PantheonPlus: 2.8 sigma
- DESI + CMB + Union3: 3.8 sigma
- DESI + CMB + DESY5: 4.2 sigma

The dark energy density increases from its high-redshift value toward the present, crossing w = -1 at intermediate redshifts.

### Section VIII: Neutrino Masses

From DESI + CMB: sum m_nu < 0.064 eV (LCDM, 95% CL) and sum m_nu < 0.16 eV (w_0 w_a CDM). The LCDM constraint is particularly tight and in tension with the minimum mass from neutrino oscillation experiments (sum m_nu > 0.06 eV for normal ordering).

## Key Results

1. DESI DR2 BAO measurements from 14+ million galaxies/quasars provide the most precise distance measurements to date, with the strongest individual BAO detection at 14.7 sigma.
2. Flat LCDM fits the BAO data well individually but shows 2.3 sigma tension with CMB parameters.
3. Dynamical dark energy with w_0 > -1 and w_a < 0 is preferred over LCDM at 3.1 sigma (DESI+CMB) to 4.2 sigma (DESI+CMB+DESY5).
4. The preference for evolving dark energy does not diminish from DR1 to DR2 despite increased statistical power.
5. Sum of neutrino masses constrained to < 0.064 eV in LCDM, creating tension with oscillation minimum mass.
6. The DR2 distance-redshift relation is consistent with SDSS and with all three major SNe compilations.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Sound horizon | $r_d = \int_\infty^{z_d} \frac{c_s(z)}{H(z)} dz$ | Eq. 1 |
| Sound horizon (numerical) | $r_d = 147.05\,{\rm Mpc}\times\left(\frac{\omega_b}{0.02236}\right)^{-0.13}\left(\frac{\omega_{bc}}{0.1432}\right)^{-0.23}\left(\frac{N_{\rm eff}}{3.04}\right)^{-0.1}$ | Eq. 2 |
| Comoving distance | $D_M(z) = \frac{c}{H_0}\int_0^z \frac{dz'}{H(z')/H_0}$ (flat) | Eq. 4 |
| Hubble distance | $D_H(z) = c/H(z)$ | Eq. 5 |
| Friedmann equation | $\frac{H(z)}{H_0} = \left[\Omega_{bc}(1+z)^3 + \Omega_\gamma(1+z)^4 + \Omega_K(1+z)^2 + \Omega_\nu\frac{\rho_\nu(z)}{\rho_{\nu,0}} + \Omega_{DE}\frac{\rho_{DE}(z)}{\rho_{DE,0}}\right]^{1/2}$ | Eq. 6 |
| Neutrino density | $\Omega_\nu h^2 = \sum m_\nu / (93.14\,{\rm eV})$ | Eq. 7 |
| DE density evolution | $\rho_{DE}(z)/\rho_{DE,0} = \exp\left[3\int_0^z \frac{1+w(z')}{1+z'} dz'\right]$ | Eq. 8 |
| CPL parametrization | $w(a) = w_0 + w_a(1-a)$ | Eq. 9 |
| DE density (CPL) | $\rho_{DE}(a)/\rho_{DE,0} = a^{-3(1+w_0+w_a)} e^{-3w_a(1-a)}$ | Eq. 10 |
| BAO scaling (parallel) | $\alpha_\parallel(z) = \frac{D_H(z)\,r_d^{\rm fid}}{D_H^{\rm fid}(z)\,r_d}$ | Eq. 11 |
| BAO scaling (perp.) | $\alpha_\perp(z) = \frac{D_M(z)\,r_d^{\rm fid}}{D_M^{\rm fid}(z)\,r_d}$ | Eq. 11 |
| Isotropic BAO distance | $D_V(z) \equiv \left[z\,D_M(z)^2\,D_H(z)\right]^{1/3}$ | Sec. III A |

## Relevance to Phonon-Exflation

This is a primary falsification gate for the phonon-exflation framework. The DESI DR2 results favor w_0 = -0.75 +/- 0.08 and w_a = -1.05 +/- 0.45 (when combined with CMB and SNe), representing a 2.8-4.2 sigma departure from LCDM (w_0 = -1, w_a = 0). The framework predicts w = -1 + O(10^{-29}) from the tau modulus dynamics, which is observationally indistinguishable from a cosmological constant. If the DESI signal for dynamical dark energy is confirmed at >5 sigma by forthcoming data, this would either falsify the framework's CC prediction or require identifying the observed w(z) variation with the framework's substrate compaction mechanism (the Wiltshire-type clock variance from tau tracking local matter density, as identified in S59). The "Quintom B" behavior (w crossing -1 from below) is particularly challenging for single-field models, but the framework's instanton-gas transit could in principle produce such crossing behavior during the cosmological epoch when the condensate dissolves.
