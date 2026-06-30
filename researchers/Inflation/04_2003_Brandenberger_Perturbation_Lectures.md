# Lectures on the Theory of Cosmological Perturbations

**Author(s):** Robert H. Brandenberger
**Year:** 2003
**Journal:** Lecture Notes in Physics 646, 127-167 (2004)
**arXiv:** hep-th/0306071
**Relevance:** HIGH -- pedagogical overview of classical and quantum cosmological perturbation theory; covers Newtonian and relativistic treatments, gauge issues, the Mukhanov-Sasaki formalism, and quantization; includes discussion of the trans-Planckian problem and back-reaction of fluctuations

---

## Abstract

The theory of cosmological perturbations has become a cornerstone of modern quantitative cosmology since it is the framework which provides the link between the models of the very early Universe such as the inflationary Universe scenario (which yield causal mechanisms for the generation of fluctuations) and the wealth of recent high-precision data on the spectrum of density fluctuations and cosmic microwave anisotropies. In these lectures, I provide an overview of the classical and quantum theory of cosmological fluctuations.

---

## Key Arguments and Derivations

### Section 2: Newtonian Theory (pp. 4-10)

Derives the Jeans instability from first principles using continuity, Euler, and Poisson equations. In a non-expanding background, the density perturbation equation is $\ddot{\delta\rho} - c_s^2\nabla^2\delta\rho - 4\pi G\rho_0\delta\rho = \sigma\nabla^2\delta S$. The Jeans wavenumber $k_J = (4\pi G\rho_0/c_s^2)^{1/2}$ separates growing modes ($k \ll k_J$, exponential growth) from oscillating modes ($k \gg k_J$, acoustic waves). In an expanding background, the Hubble friction term $2H\dot{\delta}_\epsilon$ converts exponential growth to power-law: $\delta_k(t) = c_1 t^{2/3} + c_2 t^{-1}$ for matter domination. A scale-invariant (Harrison-Zeldovich) spectrum is defined by $(\delta M/M)^2(k, t_H(k)) = \text{const}$, corresponding to spectral index $n = 1$.

### Section 3: Relativistic Theory -- Classical (pp. 10-27)

Full general relativistic treatment of perturbations around FRW. The perturbed metric in longitudinal gauge is $ds^2 = a^2(\eta)[(1+2\Phi)d\eta^2 - (1-2\Psi)\delta_{ij}dx^i dx^j]$. For a universe without anisotropic stress, $\Phi = \Psi$. The gauge-invariant Bardeen potentials are introduced. The Sasaki-Mukhanov variable $v = a[\delta\phi + (\dot\phi/H)\Phi]$ satisfies $v'' + (k^2 - z''/z)v_k = 0$ with $z = a\dot\phi/H$. This is the Mukhanov-Sasaki equation. For tensor perturbations, $\mu_k'' + (k^2 - a''/a)\mu_k = 0$ where $\mu = ah/2$.

### Section 4: Quantum Theory of Perturbations (pp. 27-33)

Canonical quantization of the Mukhanov variable $v$. Each Fourier mode is a harmonic oscillator with time-dependent frequency. The vacuum is chosen by the Bunch-Davies prescription (positive frequency WKB modes at early times). The resulting power spectrum of the curvature perturbation is $\mathcal{P}_\mathcal{R}(k) \sim (H^2/\dot\phi)^2|_{k=aH}$, evaluated at horizon crossing.

### Section 5: Trans-Planckian Problem (pp. 33-37)

If inflation lasted sufficiently long, comoving scales of cosmological interest today had physical wavelengths smaller than the Planck length at the beginning of inflation. This is the trans-Planckian problem: the predictions of inflationary cosmology for these scales may be sensitive to unknown Planck-scale physics. Brandenberger discusses modified dispersion relations as a way to study this sensitivity, finding that for a large class of modifications the standard predictions are robust.

### Section 6: Back-Reaction (pp. 37-41)

The energy-momentum tensor of cosmological fluctuations acts as an effective source for the background equations. This back-reaction can potentially affect the background expansion rate and limit the duration of inflation. The effective energy-momentum tensor of long-wavelength fluctuations has the form of a negative cosmological constant, suggesting that fluctuations could in principle lead to a dynamical relaxation of the cosmological constant.

---

## Key Results

1. The Jeans length $\lambda_J = 2\pi/k_J$ separates gravitational collapse from acoustic oscillations.
2. In an expanding matter-dominated universe, density perturbations grow as $\delta \propto a(t) \propto t^{2/3}$.
3. The Mukhanov-Sasaki equation $v_k'' + (k^2 - z''/z)v_k = 0$ is the master equation for scalar perturbations.
4. A scale-invariant (Harrison-Zeldovich) spectrum has $n = 1$, corresponding to $P_\Phi(k) = \text{const}$.
5. The trans-Planckian problem does not generically spoil inflationary predictions for a wide class of modified dispersion relations.
6. Back-reaction of long-wavelength fluctuations produces an effective negative cosmological constant contribution.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Density perturbation (Newtonian) | $\ddot{\delta\rho} - c_s^2\nabla^2\delta\rho - 4\pi G\rho_0\delta\rho = \sigma\nabla^2\delta S$ | Eq. (5) |
| Jeans wavenumber | $k_J = (4\pi G\rho_0/c_s^2)^{1/2}$ | Eq. (9) |
| Expanding-universe perturbation | $\ddot{\delta}_\epsilon + 2H\dot{\delta}_\epsilon - \frac{c_s^2}{a^2}\nabla_q^2\delta_\epsilon - 4\pi G\rho_0\delta_\epsilon = \frac{\sigma}{\rho_0 a^2}\delta S$ | Eq. (13) |
| Matter-dominated growth | $\delta_k(t) = c_1 t^{2/3} + c_2 t^{-1}$ | Eq. (15) |
| Scale-invariant spectrum | $(\delta M/M)^2(k,t_H(k)) \sim k^{n-1}$ with $n=1$ | Eq. (19) |
| Longitudinal gauge metric | $ds^2 = a^2(\eta)[(1+2\Phi)d\eta^2 - (1-2\Psi)\delta_{ij}dx^i dx^j]$ | Sec. 3 |
| Mukhanov-Sasaki equation | $v_k'' + (k^2 - z''/z)v_k = 0$ | Sec. 3 |
| Tensor mode equation | $\mu_k'' + (k^2 - a''/a)\mu_k = 0$ | Sec. 3 |

---

## Relevance to Phonon-Exflation

Brandenberger's lectures provide two contact points with the exflation framework. (1) The trans-Planckian problem he identifies is precisely the kind of UV sensitivity that the spectral action approach resolves by construction: in noncommutative geometry, there is a natural UV cutoff provided by the spectral triple, so modes never have sub-Planckian wavelengths. The exflation transit occurs at a specific point ($\tau = 0.190$) in the Jensen deformation parameter space, not at arbitrarily high energies. (2) His discussion of back-reaction -- that long-wavelength fluctuations generate an effective negative cosmological constant -- is suggestive of the exflation framework's effacement mechanism, where the impedance mismatch at the acoustic white hole boundary produces a $0.03\%$ leakage that manifests as the observed dark energy. The Jeans instability analysis also maps directly to the GGE relic acoustic excitations in the post-transit epoch.
