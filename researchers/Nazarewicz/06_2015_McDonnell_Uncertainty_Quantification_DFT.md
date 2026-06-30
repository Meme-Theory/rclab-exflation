# Uncertainty Quantification for Nuclear Density Functional Theory and Information Content of New Measurements

**Author(s):** J.D. McDonnell, N. Schunck, D. Higdon, J. Sarich, S.M. Wild, and W. Nazarewicz
**Year:** 2015
**Journal:** Physical Review Letters 114, 122501 (2015)
**arXiv:** 1501.03572
**Relevance:** CRITICAL

---

## Abstract

Statistical tools of uncertainty quantification can be used to assess the information content of measured observables with respect to present-day theoretical models; to estimate model errors and thereby improve predictive capability; to extrapolate beyond the regions reached by experiment; and to provide meaningful input to applications and planned measurements. To showcase new opportunities offered by such tools, we make a rigorous analysis of theoretical statistical uncertainties in nuclear density functional theory using Bayesian inference methods. By considering the recent mass measurements from the Canadian Penning Trap at Argonne National Laboratory, we demonstrate how the Bayesian analysis and a direct least-squares optimization, combined with high-performance computing, can be used to assess the information content of the new data with respect to a model based on the Skyrme energy density functional approach. Employing the posterior probability distribution computed with a Gaussian process emulator, we apply the Bayesian framework to propagate theoretical statistical uncertainties in predictions of nuclear masses, two-neutron dripline, and fission barriers. Overall, we find that the new mass measurements do not impose a constraint that is strong enough to lead to significant changes in the model parameters. The example discussed in this study sets the stage for quantifying and maximizing the impact of new measurements with respect to current modeling and guiding future experimental efforts, thus enhancing the experiment-theory cycle in the scientific method.

---

## Key Arguments and Derivations

### 1. The Inverse Problem Framework

Determining model parameters from experimental data is an inverse problem. The Bayesian approach treats model parameters as random variables characterized by their joint probability distribution. The nuclear DFT model (UNEDF1) has 12 parameters optimized on binding energies, charge radii, odd-even mass differences, and fission isomer energies.

### 2. The Objective Function

The quality of the functional is measured by a composite $\chi^2$:

$$\chi^2(x) = \frac{1}{n_d - n_x}\sum_{t=1}^{n_T}\sum_{j=1}^{n_t}\left(\frac{y_{tj}(x) - d_{tj}}{\sigma_t}\right)^2$$

where $x$ denotes model parameters ($n_x = 12$), $n_T = 4$ data types, $n_d = 115$ total data points, $d_{tj}$ and $y_{tj}(x)$ are experimental and model values. Computing $\chi^2$ requires ~5 minutes of CPU time with 800+ cores.

### 3. Gaussian Process Emulator

Monte Carlo simulations require tens of thousands of $\chi^2$ evaluations -- computationally prohibitive even on supercomputers. Solution: replace the DFT model with a Gaussian Process (GP) response surface. The GP is estimated within the Bayesian formulation using an ensemble of 200 DFT runs across a Latin hypercube sample in the 12-dimensional parameter hyperrectangle centered on UNEDF1 values.

The full posterior density includes: (i) likelihood term from experimental data based on $\chi^2$, (ii) ensemble of training runs for GP, (iii) uniform prior for model parameters, (iv) priors for GP control parameters. Samples from the posterior are constructed via Markov Chain Monte Carlo.

### 4. Impact of New CPT Mass Measurements

17 new masses of neutron-rich even-even nuclei measured at the Canadian Penning Trap (CPT) at Argonne were included. These probe nuclei around $^{132}$Sn, potentially improving isovector EDF properties.

Result: the shift in the posterior is small for most parameters. The largest relative difference (weighted by standard deviations) is $0.6\sigma$ for the isovector surface coupling constant $C^{\rho\Delta\rho}_1$. The new UNEDF1_CPT functional is close to UNEDF1.

### 5. RMS Deviations

| Data class | UNEDF1 | UNEDF1_CPT |
|:-----------|:-------|:-----------|
| masses (deformed) | 0.721 | 0.578 |
| masses (spherical) | 1.461 | 1.545 |
| radii | 0.022 | 0.022 |
| OES (neutron) | 0.023 | 0.024 |
| OES (proton) | 0.079 | 0.081 |
| fission isomers | 0.190 | 0.316 |
| masses (CPT) | 1.064 | 0.479 |

Including CPT masses improves deformed mass reproduction but slightly deteriorates fission isomer and spherical mass predictions -- indicative of optimization priority shifts.

### 6. Propagation of Uncertainties

**Nuclear masses:** 90% prediction intervals for CPT masses are $\approx \pm 2$ MeV (statistical parameter uncertainty); larger when model error is included. Experimental values generally fall within the 90% interval.

**Two-neutron dripline:** Uncertainty is 15-20 nucleons across the chart, comparable to systematic uncertainties from different Skyrme functionals. Including CPT masses does not shift the predicted dripline.

**Fission barrier of $^{240}$Pu:** Large theoretical uncertainty in the static fission barrier. Since 1 MeV barrier shift translates to many orders of magnitude in SF half-life, this highlights the urgent need for better constraining deformation properties of EDFs.

### 7. Statistical vs. Systematic Uncertainty

The uncertainties are estimated statistically, reflecting parameter uncertainty and model misfit. The misfit error is most likely due to the unknown form of the nuclear EDF itself -- additional measurements will never reduce this source of uncertainty. Adding missing physics is the major challenge.

---

## Key Results

1. Bayesian posterior for UNEDF1 parameters is consistent with covariance analysis estimates
2. 17 new neutron-rich mass measurements produce only minor impact on the model -- the data are insufficiently constraining
3. The isovector surface coupling constant $C^{\rho\Delta\rho}_1$ shows the largest shift ($0.6\sigma$)
4. Theoretical mass uncertainties are $\approx \pm 2$ MeV (90% CI)
5. Two-neutron dripline uncertainty: 15-20 nucleons
6. Fission barrier uncertainties are large enough to change SF half-lives by many orders of magnitude
7. Model error (unknown EDF form) dominates statistical parameter uncertainty

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Composite $\chi^2$ | $\chi^2(x) = \frac{1}{n_d-n_x}\sum_t\sum_j\left(\frac{y_{tj}(x)-d_{tj}}{\sigma_t}\right)^2$ | Eq. (1) |
| Parameter count | $n_x = 12$, $n_d = 115$ | Text |
| GP training | 200-point Latin hypercube in $n_x$-dimensional space | Text |
| MCMC posterior | Full posterior = likelihood $\times$ GP prior $\times$ parameter prior | Text, Ref. [37] |
| Modified Hamiltonian kernel | $H'(r;q,q';\Omega) = H - \lambda_p[Z-Z_0] - \lambda_n[N-N_0]$ | Supplemental |
| UNEDF1 parameters | 12 coupling constants (see Table II in supplemental) | Supplemental |

---

## UNEDF Coupling Constants (from Supplemental Material)

| Parameter | UNEDF0 | UNEDF1 | UNEDF1_CPT |
|:----------|:-------|:-------|:-----------|
| $\rho_c$ (fm$^{-3}$) | 0.1605 | 0.1587 | 0.1589 |
| $E_{NM}/A$ (MeV) | -16.056 | -15.800 | -15.800 |
| $K_{NM}$ (MeV) | 230.0 | 220.0 | 220.0 |
| $a^{NM}_{sym}$ (MeV) | 30.543 | 28.936 | 29.345 |
| $L^{NM}_{sym}$ (MeV) | 45.080 | 40.015 | 40.714 |
| $1/M^*_s$ | 0.900 | 0.992 | 0.969 |
| $C^{\rho\Delta\rho}_0$ (MeV fm$^5$) | -55.261 | -45.129 | -43.980 |
| $C^{\rho\Delta\rho}_1$ (MeV fm$^5$) | -55.623 | -145.318 | -114.292 |
| $V^n_0$ (MeV fm$^3$) | -170.374 | -186.066 | -182.237 |
| $V^p_0$ (MeV fm$^3$) | -199.202 | -206.580 | -203.981 |
| $C^{\rho\nabla J}_0$ (MeV fm$^5$) | -79.531 | -74.026 | -72.417 |
| $C^{\rho\nabla J}_1$ (MeV fm$^5$) | 45.630 | -35.658 | -32.921 |

---

## Relevance to Phonon-Exflation

This paper provides the methodological template for the framework's probability trajectory. The Bayesian inference approach -- GP emulator for computationally expensive model evaluations, MCMC posterior sampling, propagation of uncertainties through predictions -- is directly applicable to the framework's gate system. Specific connections: (1) The framework maintains a probability trajectory (40% -> 5-8% -> TBD) based on gate verdicts. This paper shows how to formalize such assessments using posterior distributions over model parameters. (2) The finding that 17 new measurements produce only minor impact parallels the framework's experience that individual computations rarely shift the overall probability -- structural results (theorems, closures) dominate. (3) The distinction between statistical (parameter) and systematic (model form) uncertainty maps onto the framework's distinction between computational uncertainty and the question of whether the SU(3)-fiber model itself is correct. (4) The GP emulator approach could be applied to the framework's spectral action evaluations, which are computationally expensive ($\sim 8.7$s per $\tau$-value) and need to be sampled across parameter space.
