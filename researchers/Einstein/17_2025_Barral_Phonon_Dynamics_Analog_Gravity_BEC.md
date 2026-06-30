# Phonon Dynamics in Spherically-Curved Analog-Gravity Bose-Einstein Condensates

**Author(s):** J. Austin Chunn, Ruotong Zhai, Daniel E. Sheehy
**Year:** 2025
**Journal:** [INCOMPLETE - not extractable from PDF]
**arXiv:** 2508.03683
**Relevance:** HIGH

---

## Abstract

We study the low energy phonon dynamics of a Bose-Einstein condensate (BEC) with a density profile that is equivalent, via a coordinate transformation, to phonons traveling in a "spherical" curved spacetime that realizes the Friedman-Lemaitre-Robertson-Walker (FLRW) metric. The metric of this BEC is characterized by its curvature $\kappa$ and a time-dependent scale factor $a(t)$, with an increase in the latter corresponding to an expansion of the analog FLRW universe. We study the propagation of classical phonons in such BECs, finding that a sudden change in the scale factor induces ripples in the wave motion. In addition, we study quantum phonon creation (or vacuum amplification) due to the scale-factor modification and quantify their entanglement.

---

## Key Arguments and Derivations

### BEC Hamiltonian and Gross-Pitaevskii Equation

The starting point is a 2D trapped interacting boson gas Hamiltonian:

$$\hat{H} = \int d^2r \left[\hat{\Phi}^\dagger\hat{h}\hat{\Phi} + \frac{1}{2}U(t)\hat{\Phi}^\dagger\hat{\Phi}^\dagger\hat{\Phi}\hat{\Phi}\right]$$

with single-particle Hamiltonian $\hat{h} = -\frac{\hbar^2}{2m}\nabla^2 + V(\mathbf{r},t) - \mu$. The Gross-Pitaevskii equation for the condensate mean field $\varphi_0$ gives, in the Thomas-Fermi approximation, the local density:

$$n_0(\mathbf{r}) = \frac{\mu - V(\mathbf{r},t)}{U(t)}$$

With a specially chosen potential $V(\mathbf{r},t) = \frac{1}{2}m\omega^2(t)f(r)$ where $f(r) = -2r^2 - r^4/R^2$, the density profile becomes:

$$n_0(r) = \bar{n}_0\left(1 + \frac{r^2}{R^2}\right)^2$$

### Emergent FLRW Metric from BEC Fluctuations

Linearized fluctuations $\delta\hat{\Phi}$ around the condensate mean obey coupled equations that, in the long-wavelength (phononic) limit, reduce to a Klein-Gordon equation:

$$-\partial_t\left[\frac{1}{c_s^2(\mathbf{r})}\partial_t\hat{\varphi}\right] + \nabla^2\hat{\varphi} = 0$$

where $c_s(\mathbf{r}) = \sqrt{U(t)n_0(\mathbf{r})/m}$ is the local sound speed. This is equivalent to a massless scalar field in curved spacetime:

$$\partial_\mu\left[\sqrt{|g|}g^{\mu\nu}\partial_\nu\hat{\varphi}\right] = 0$$

Under the coordinate transformation $u = r/(1+r^2/R^2)$ and $u = \sin\theta/\sqrt{\kappa}$, the line element becomes the 2D FLRW metric:

$$ds^2 = -dt^2 + a^2(t)\left[\frac{du^2}{1-\kappa u^2} + u^2 d\varphi^2\right]$$

with curvature $\kappa = 4/R^2$ and scale factor $a^2(t) = m/(\bar{n}_0 U(t))$.

### Wave Equation and Green's Function

The wave equation in spherical coordinates with scale factor $a(t)$ is:

$$\partial_t\left[a^2(t)\partial_t\hat{\varphi}\right] - \Delta\hat{\varphi} = 0$$

where $\Delta$ is the Laplace-Beltrami operator on the 2-sphere:

$$\Delta = \kappa\left[\frac{1}{\sin\theta}\partial_\theta(\sin\theta\partial_\theta) + \frac{1}{\sin^2\theta}\partial^2_\varphi\right]$$

The eigenfunctions are modified spherical harmonics $Y_{\ell m}(\theta,\varphi)$ with eigenvalues $h(k) = -k(k+\sqrt{\kappa})$ and $k = \sqrt{\kappa}\ell$.

The Green's function is expanded as:

$$G = \sum_\ell \frac{\ell+1/2}{2\pi} F_k(t) P_\ell(\cos L)$$

where $L$ is the comoving geodesic distance and $F_k(t)$ satisfies:

$$\partial_t\left[a^2(t)\partial_t F_k(t)\right] + |h(k)|F_k(t) = \delta(t)$$

### Classical Wave Propagation: Static Spacetime

For constant $a(t) = a_i$, the time-dependent coefficients are:

$$F_k(t) = \frac{\Theta(t)}{a_i\sqrt{|h(k)|}}\sin(\omega^i_k t)$$

with $\omega^i_k = \sqrt{|h(k)|}/a_i$. Wavefronts propagate along curves of equal comoving distance from the source, as expected for a curved 2D sphere.

### Expanding Spacetime: de Sitter Analog

The scale factor is modeled as:

$$a(t) = \begin{cases} a_i & t \leq t_i \\ a_i e^{H(t-t_i)} & t_i \leq t \leq t_f \\ a_f & t \geq t_f \end{cases}$$

During expansion, the mode equation becomes:

$$\partial_t\left[e^{2H(t-t_i)}\partial_t p^{II}_k(t)\right] + \left(\frac{\sqrt{|h(k)|}}{a_i}\right)^2 p^{II}_k(t) = 0$$

with solutions in terms of Bessel functions $J_1$ and $Y_1$.

**Backward-propagating ripples:** Sudden changes in the scale factor (at $t_i$ and $t_f$) create backward-traveling ripples. The particle horizon determines the main wave edge:

$$h(t) = \int_0^t \frac{dt'}{a(t')}$$

The first ripple location is:

$$h_{r,1}(t) = -\frac{1}{Ha_i}\left(1 - e^{-H(t-t_i)}\right) + \frac{t_i}{a_i}$$

The second ripple (from expansion end):

$$h_{r,2}(t) = -\frac{1}{a_i e^{-H(t_f-t_i)}}(t-t_f) + \frac{1}{Ha_i}(1-e^{-H(t_f-t_i)}) + \frac{t_i}{a_i}$$

### Quantum Particle Production

The field operator is expanded in mode functions:

$$\hat{\varphi} = \sum_{\ell,m} \frac{\ell+1/2}{2\pi}\left[\hat{a}_{km}Y_{\ell m}v_k(t) + \hat{a}^\dagger_{km}Y^*_{\ell m}v^*_k(t)\right]$$

Mode functions satisfy $\ddot{v}_k + 2\frac{\dot{a}}{a}\dot{v}_k + \frac{|h|}{a^2}v_k = 0$ with Wronskian normalization $a^2(v_k\dot{v}^*_k - \dot{v}_k v^*_k) = i$.

In the initial static region: $v^I_k(t) = e^{-i\omega^i_k t}/(a_i\sqrt{2\omega^i_k})$.

After expansion, the mode functions contain both positive and negative frequency components via Bogoliubov coefficients $\alpha_k$ and $\beta_k$ satisfying $|\alpha_k|^2 - |\beta_k|^2 = 1$:

$$v^{III}_k(t) = \frac{\alpha^*_k e^{-i\omega^f_k t}}{a_f\sqrt{2\omega^f_k}} + \frac{\beta_k e^{i\omega^f_k t}}{a_f\sqrt{2\omega^f_k}}$$

The number of created particles is $N_{km} = |\beta_k|^2$. The Bogoliubov coefficient $\beta$ is given explicitly in terms of Bessel functions evaluated at $\omega^i_k/H$ before and after expansion.

Using experimental parameters from Viermann et al. (potassium-39 BEC, $\bar{n}_0 = 1.3 \times 10^9/\text{cm}^2$, $R_{TF} = 25\,\mu\text{m}$), with $a_i = 331\,\text{s/m}$ and $H = 240\,\text{s}^{-1}$, particle production is maximal at $\ell = 1$ and decreases with increasing $\ell$.

### Entanglement of Produced Pairs

Particle production is a two-mode squeezing operation: $\hat{b}_{km} = \alpha^*_k\hat{a}_{km} + \beta^*_k\hat{a}^\dagger_{k\bar{m}}$. The logarithmic negativity for an initial thermal state at temperature $T$ is:

$$E_N[\ell] = \max\left\{0, -\log_2\left[(1+2n_B)\left(\sqrt{1+|\beta_\ell|^2} - |\beta_\ell|\right)^2\right]\right\}$$

where $n_B = 1/(e^{\beta\hbar\omega^i_k}-1)$ is the Bose distribution. Increasing temperature suppresses entanglement for low-$\ell$ modes.

---

## Key Results

1. A 2D BEC with tailored density profile $n_0(r) = \bar{n}_0(1+r^2/R^2)^2$ realizes a spherical FLRW metric with curvature $\kappa = 4/R^2$.
2. The phonon wave equation is exactly the Klein-Gordon equation for a massless scalar field in 2+1D FLRW spacetime.
3. Sudden changes in the scale factor create backward-propagating classical ripples whose positions are predicted by particle horizon formulas.
4. Quantum particle production (vacuum amplification) via Bogoliubov mixing produces $|\beta_k|^2$ phonon pairs per mode, maximal at $\ell=1$.
5. Produced pairs are quantum entangled, with logarithmic negativity $E_N[\ell]$ that is suppressed by thermal fluctuations at low $\ell$.
6. The setup is experimentally accessible using parameters from the Viermann et al. potassium-39 BEC experiment.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| BEC Hamiltonian | $\hat{H} = \int d^2r[\hat{\Phi}^\dagger\hat{h}\hat{\Phi} + \frac{1}{2}U(t)\hat{\Phi}^\dagger\hat{\Phi}^\dagger\hat{\Phi}\hat{\Phi}]$ | Eq. (1) |
| Thomas-Fermi density | $n_0(r) = (\mu - V)/U(t)$ | Eq. (4) |
| Engineered density | $n_0(r) = \bar{n}_0(1+r^2/R^2)^2$ | Eq. (6) |
| Klein-Gordon equation | $-\partial_t[c_s^{-2}\partial_t\hat{\varphi}] + \nabla^2\hat{\varphi} = 0$ | Eq. (11) |
| FLRW metric | $ds^2 = -dt^2 + a^2(t)[du^2/(1-\kappa u^2) + u^2 d\varphi^2]$ | Eq. (15) |
| Wave equation | $\partial_t[a^2(t)\partial_t\hat{\varphi}] - \Delta\hat{\varphi} = 0$ | Eq. (17) |
| Laplace-Beltrami | $\Delta = \kappa[\frac{1}{\sin\theta}\partial_\theta(\sin\theta\partial_\theta) + \frac{1}{\sin^2\theta}\partial^2_\varphi]$ | Eq. (18) |
| Green's function | $G = \sum_\ell \frac{\ell+1/2}{2\pi}F_k(t)P_\ell(\cos L)$ | Eq. (28) |
| Scale factor model | $a(t) = a_i e^{H(t-t_i)}$ during expansion | Eq. (33) |
| Particle horizon | $h(t) = \int_0^t dt'/a(t')$ | Eq. (39) |
| Mode equation | $\ddot{v}_k + 2\frac{\dot{a}}{a}\dot{v}_k + \frac{|h|}{a^2}v_k = 0$ | Eq. (44) |
| Bogoliubov mixing | $\hat{b}_{km} = \alpha^*_k\hat{a}_{km} + \beta^*_k\hat{a}^\dagger_{k\bar{m}}$ | Eq. (53) |
| Particle number | $N_{km} = |\beta_k|^2$ | Eq. (54) |
| Logarithmic negativity | $E_N[\ell] = \max\{0, -\log_2[(1+2n_B)(\sqrt{1+|\beta_\ell|^2}-|\beta_\ell|)^2]\}$ | Eq. (64) |

---

## Relevance to Phonon-Exflation

This paper provides the most direct laboratory analog of the phonon-exflation creation mechanism. The framework posits that particles are phononic excitations of the M4 $\times$ SU(3) substrate, and that cosmological particle creation occurs via Bogoliubov mixing during the tau-transit (identified in Session 38 as Parker-type, not Hawking). Chunn et al. demonstrate precisely this physics in a BEC: (1) an engineered density profile creates an emergent FLRW metric for phonons, (2) a sudden quench of the scale factor produces entangled phonon pairs via Bogoliubov coefficients $\alpha_k, \beta_k$, and (3) the creation is a two-mode squeezing operation. The backward-propagating ripples from scale-factor discontinuities are a testable prediction that maps directly onto the framework's sudden-quench scenario ($P_{\text{exc}} = 1.000$ from Session 38). The entanglement structure (logarithmic negativity $E_N[\ell]$) provides a quantitative template for the GGE relic state predicted by the framework.
