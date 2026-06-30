# An alternative to dark matter and dark energy: Scale-dependent gravity in superfluid vacuum theory

**Author(s):** Konstantin G. Zloshchastiev
**Year:** 2020
**Journal:** Universe 6, 180 (2020)
**arXiv:** 2011.12565
**Relevance:** HIGH — explicit metric from GPE

---

## Abstract

We derive an effective gravitational potential, induced by the quantum wavefunction of a physical vacuum of a self-gravitating configuration, while the vacuum itself is viewed as the superfluid described by the logarithmic quantum wave equation. We determine that gravity has a multiple-scale pattern, to such an extent that one can distinguish sub-Newtonian, Newtonian, galactic, extragalactic and cosmological terms. The last of these dominates at the largest length scale of the model, where superfluid vacuum induces an asymptotically Friedmann-Lemaitre-Robertson-Walker-type spacetime, which provides an explanation for the accelerating expansion of the Universe. The model describes different types of expansion mechanisms, which could explain the discrepancy between measurements of the Hubble constant using different methods. On a galactic scale, our model explains the non-Keplerian behaviour of galactic rotation curves, and also why their profiles can vary depending on the galaxy. It also makes a number of predictions about the behaviour of gravity at larger galactic and extragalactic scales.

---

## Key Arguments and Derivations

### Logarithmic Superfluid Vacuum (Section 2)

The physical vacuum is described by a condensate wavefunction $\Psi(\mathbf{r}, t)$ obeying a U(1)-symmetric Schrodinger equation with logarithmic nonlinearity:

$$i\hbar\partial_t\Psi = \left[-\frac{\hbar^2}{2m}\nabla^2 + V_{ext}(\mathbf{r},t) - b\ln(|\Psi|^2/\bar{\rho})\right]\Psi$$

where $m$ is the constituent particle mass, $b = b(\mathbf{r},t)$ is the nonlinear coupling, and $\bar{\rho}$ is a reference density. The equation of state and speed of sound in leading-order approximation are:

$$p = -(b/m)\rho, \quad c_s = \sqrt{|b|/m}$$

The requirement that $c_s$ should not depend on density (to recover Lorentz symmetry at low momenta) uniquely selects logarithmic nonlinearity: $F(\rho) = -b\ln(\rho/\bar{\rho})$.

### BEC-Spacetime Correspondence (Section 2)

A relativistic observer (R-observer) perceives the superfluid dynamics as curved 4D spacetime with metric:

$$g_{\mu\nu} \propto \frac{\rho}{c_s} \begin{pmatrix} -[c_s^2 - \eta^2(\nabla S)^2] & -\eta\nabla S \\ -\eta\nabla S & \mathbf{I} \end{pmatrix}$$

where $\eta = \hbar/m$ and $S$ is the phase of the condensate wavefunction in Madelung representation $\Psi = \sqrt{\rho}\exp(iS)$. Einstein field equations are reinterpreted as defining the induced stress-energy tensor: $\tilde{T}_{\mu\nu} \equiv \kappa^{-1}[R_{\mu\nu} - \frac{1}{2}g_{\mu\nu}R]$.

### Induced Gravitational Potential (Section 3)

Using the minimal inhomogeneous logarithmic model with $b(r) = b_0 - q/r^2$, the vacuum wavefunction has the form:

$$|\Psi_{vac}|^2 \approx \bar{\rho}\exp\left[-\frac{a_2}{\bar{\ell}^2}r^2 + \frac{a_1}{\bar{\ell}}r + \chi\ln(r/\bar{\ell}) + a_0\right]$$

Substituting into the gravitational potential definition $\Phi = (1/m)(b_0 - q/r^2)\ln(|\Psi_{vac}|^2/\bar{\rho})$ yields a **seven-term gravitational potential**:

$$\Phi(r) = \Phi_{smi}(r) + \Phi_{RN}(r) + \Phi_N(r) + \Phi_{gal}(r) + \Phi_{mgl}(r) + \Phi_{dS}(r) + \Phi_0$$

### Physical Interpretation of the Seven Terms (Section 4)

1. **$\Phi_N = -GM/r$** — Newtonian gravity (gravitational mass generation from superfluid parameters)
2. **$\Phi_{RN} = -\zeta a_0 q c_b^2 L_{RN}^2/r^2$** — Reissner-Nordstrom term (abelian charges)
3. **$\Phi_{smi} = -\zeta\chi q c_b^2 L_{smi}^2 \ln(r/\bar{\ell})/r^2$** — Sub-Newtonian strong gravity (logarithmic enhancement at short distances)
4. **$\Phi_{gal} = c_b^2 \chi\ln(r/\bar{\ell})$** — Galactic scale: logarithmic potential giving flat rotation curves
5. **$\Phi_{mgl} = \zeta a_1 c_b^2 r/L_{mgl}$** — Meta-galactic: linear potential
6. **$\Phi_{dS} = -c_b^2 r^2/L_{dS}^2$** — de Sitter: quadratic potential giving accelerating expansion

### Galactic Rotation Curves (Section 6)

The squared orbital velocity from the full potential is:

$$v^2(r) = r\frac{\partial\Phi}{\partial r} = \frac{GM}{r} + c_b^2\chi + \frac{\zeta a_1 c_b^2 r}{L_{mgl}} - \frac{2c_b^2 r^2}{L_{dS}^2} + \cdots$$

At galactic scales, the dominant terms are Newtonian ($\propto 1/r$) plus the logarithmic term ($c_b^2\chi = \text{const}$). The transition from Keplerian to flat gives:

$$v^2(r) \approx \frac{GM}{r} + c_b^2\chi$$

For $r \gg GM/(c_b^2\chi)$, the orbital velocity becomes asymptotically constant: $v_\infty^2 = c_b^2\chi$. This explains flat rotation curves without introducing dark matter. The variation of rotation curve profiles between galaxies comes from different values of the parameters $\chi$, $a_1$, etc., determined by each galaxy's vacuum state.

### Accelerating Expansion (Section 7)

At cosmological scales, the de Sitter term $\Phi_{dS} = -c_b^2 r^2/L_{dS}^2$ dominates, inducing an asymptotically FLRW-type spacetime. The model naturally produces accelerating expansion without dark energy. The expansion rate and its measurement may depend on the observation method (distance ladder vs CMB), potentially explaining the Hubble tension through different effective metrics probed by different observations.

---

## Key Results

1. Logarithmic nonlinearity in the wave equation is uniquely selected by requiring density-independent speed of sound (Lorentz symmetry recovery)
2. The induced gravitational potential has 7 physically distinct terms spanning sub-Newtonian to cosmological scales
3. Flat rotation curves emerge from the logarithmic galactic term $\Phi_{gal} = c_b^2\chi\ln(r/\bar{\ell})$
4. Gravitational mass is a composite quantum phenomenon induced by superfluid dynamics
5. Accelerating expansion arises from the de Sitter term without dark energy
6. Gravity becomes naturally stronger at shorter scales (hierarchy problem resolution)
7. Electrical charge emerges as a composite phenomenon from the Reissner-Nordstrom term
8. Only 4 parameters ($m$, $\bar{\rho}$, $b_0$, $q$), with 2 fixed a priori

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Logarithmic wave equation | $i\hbar\partial_t\Psi = [-\frac{\hbar^2}{2m}\nabla^2 + V_{ext} - b\ln(\lvert\Psi\rvert^2/\bar{\rho})]\Psi$ | Eq. (9) |
| Equation of state | $p = -(b/m)\rho$, $c_s = \sqrt{\lvert b\rvert/m}$ | Eq. (10) |
| BEC-spacetime metric | $g_{\mu\nu} \propto (\rho/c_s)\text{diag}(-[c_s^2 - \eta^2(\nabla S)^2], \mathbf{I})$ | Eq. (5) |
| Inhomogeneous coupling | $b(r) = b_0 - q/r^2$ | Eq. (11) |
| Induced grav. potential | $\Phi(r) = \frac{1}{m}(b_0 - q/r^2)\ln(\lvert\Psi_{vac}\rvert^2/\bar{\rho})$ | Eq. (15) |
| Seven-term potential | $\Phi = \Phi_{smi} + \Phi_{RN} + \Phi_N + \Phi_{gal} + \Phi_{mgl} + \Phi_{dS} + \Phi_0$ | Eq. (20) |
| Newtonian term | $\Phi_N = -GM/r$ | Eq. (23) |
| Galactic term | $\Phi_{gal} = c_b^2\chi\ln(r/\bar{\ell})$ | Eq. (24) |
| de Sitter term | $\Phi_{dS} = -c_b^2 r^2/L_{dS}^2$ | Eq. (26) |
| Effective coupling | $G_{eff} \approx G[1 + \zeta_{\chi q}L_\chi\ln(r/\bar{\ell})/r]$ | Eq. (40) |
| Gravitational mass | $GM = a_1 q/(m\bar{\ell})$ | Eq. (28) |
| Schwarzschild radius | $r_H = 2a_1 q/(mc_{(0)}^2\bar{\ell})$ | Eq. (31) |

---

## Relevance to Phonon-Exflation

This paper provides the most explicit demonstration of how a superfluid vacuum described by a wave equation (GPE) induces an emergent gravitational metric and a multi-scale gravitational potential. The BEC-spacetime correspondence in Eq. (5) is the direct mechanism by which the framework's internal SU(3) geometry could induce effective 4D spacetime. The logarithmic nonlinearity's unique selection by Lorentz symmetry recovery parallels the framework's requirement that the spectral action reproduce relativistic physics. The seven-term potential structure suggests that the framework's single SU(3) fold could produce distinct gravitational effects at different scales without separate dark matter or dark energy components — consistent with the bottom-up emergence philosophy.
