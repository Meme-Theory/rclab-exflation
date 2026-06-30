# An Alternative to Dark Matter and Dark Energy: Scale-Dependent Gravity in Superfluid Vacuum Theory

**Author(s):** Konstantin G. Zloshchastiev
**Year:** 2020
**Journal:** Universe 6, 180 (2020) [DOI: 10.3390/universe6100180]. Proceedings of 17th Russian Gravitational Conference (RUSGRAV-17).
**arXiv:** 2011.12565
**Relevance:** HIGH

---

## Abstract

We derive an effective gravitational potential, induced by the quantum wavefunction of a physical vacuum of a self-gravitating configuration, while the vacuum itself is viewed as the superfluid described by the logarithmic quantum wave equation. We determine that gravity has a multiple-scale pattern, to such an extent that one can distinguish sub-Newtonian, Newtonian, galactic, extragalactic and cosmological terms. The last of these dominates at the largest length scale of the model, where superfluid vacuum induces an asymptotically Friedmann-Lemaitre-Robertson-Walker-type spacetime, which provides an explanation for the accelerating expansion of the Universe. The model describes different types of expansion mechanisms, which could explain the discrepancy between measurements of the Hubble constant using different methods. On a galactic scale, our model explains the non-Keplerian behaviour of galactic rotation curves, and also why their profiles can vary depending on the galaxy. It also makes a number of predictions about the behaviour of gravity at larger galactic and extragalactic scales. We demonstrate how the behaviour of rotation curves varies with distance from a gravitating center, growing from an inner galactic scale towards a metagalactic scale: a squared orbital velocity's profile crosses over from Keplerian to flat, and then to non-flat. The asymptotic non-flat regime is thus expected to be seen in the outer regions of large spiral galaxies.

---

## Key Arguments and Derivations

### Superfluid Vacuum Theory (SVT) Foundation

SVT treats the physical vacuum as a quantum superfluid described by a condensate wavefunction $\Psi(\mathbf{r},t)$, a 3D Euclidean scalar satisfying:

$$\langle\Psi|\Psi\rangle = \int_V \rho \, dV = M$$

where $\rho = |\Psi|^2$ is the fluid mass density. The dynamics obey a U(1)-symmetric Schrodinger-type equation:

$$\left[-i\hbar\partial_t - \frac{\hbar^2}{2m}\nabla^2 + V_{\text{ext}}(\mathbf{r},t) + F(|\Psi|^2)\right]\Psi = 0$$

where $F(\rho)$ is a nonlinear self-interaction function.

### Emergent Spacetime via BEC-Spacetime Correspondence

Massless excitations propagate at velocity $c_s \propto \sqrt{|p'(\rho)|}$. The emergent 4D pseudo-Riemannian metric seen by a relativistic (R-)observer is:

$$g_{\mu\nu} \propto \frac{\rho}{c_s}\begin{pmatrix} -[c_s^2 - \eta^2(\nabla S)^2] & \cdots & -\eta\nabla S \\ \vdots & \ddots & \vdots \\ -\eta\nabla S & \cdots & I \end{pmatrix}$$

where $\eta = \hbar/m$ and $S$ is the condensate phase. The condition $|c_s| > \eta|\nabla S|$ maintains correct metric signature.

### Logarithmic Nonlinearity

Requiring the speed of sound $c_s$ to be density-independent (Lorentz symmetry in the phononic limit) yields the differential equation $\rho|F'(\rho)| = mc_s^2 \approx \text{const}$, whose solution is logarithmic:

$$F(\rho) = -b\ln(\rho/\bar{\rho})$$

leading to the logarithmic Schrodinger equation:

$$i\hbar\partial_t\Psi = \left[-\frac{\hbar^2}{2m}\nabla^2 + V_{\text{ext}} - b\ln(|\Psi|^2/\bar{\rho})\right]\Psi$$

with equation of state $p = -(b/m)\rho$ (barotropic) and $c_s = \sqrt{|b|/m}$.

### Inhomogeneous Logarithmic Model

The minimal inhomogeneous model uses spatially varying nonlinear coupling:

$$b(r) = b_0 - q/r^2$$

where $b_0$ and $q$ are functions of quantum temperature $T_\Psi$ (thermodynamic conjugate of Everett-Hirschman information entropy).

### Induced Gravitational Potential

For a self-gravitating vacuum state with wavefunction amplitude:

$$|\Psi_{\text{vac}}|^2 \approx \bar{\rho}\exp\left[-\frac{a_2}{\bar{\ell}^2}r^2 + \frac{a_1}{\bar{\ell}}r + \chi\ln\left(\frac{r}{\bar{\ell}}\right) + a_0\right]$$

the induced gravitational potential decomposes into seven terms:

$$\Phi(r) = \Phi_{\text{smi}}(r) + \Phi_{\text{RN}}(r) + \Phi_N(r) + \Phi_{\text{gal}}(r) + \Phi_{\text{mgl}}(r) + \Phi_{\text{dS}}(r) + \Phi_0$$

### The Seven Terms

| Term | Formula | Physical Meaning | Scale |
|:-----|:--------|:-----------------|:------|
| $\Phi_{\text{smi}}$ | $-\chi q \ln(r/\bar{\ell})/(mr^2)$ | Strong gravity (ln/r$^2$) | Sub-Newtonian |
| $\Phi_{\text{RN}}$ | $-a_0 q/(mr^2)$ | Reissner-Nordstrom (1/r$^2$) | Sub-Newtonian |
| $\Phi_N$ | $-a_1 q/(m\bar{\ell}r) = -GM/r$ | Newtonian gravity | Newtonian |
| $\Phi_{\text{gal}}$ | $\chi b_0 \ln(r/\bar{\ell})/m$ | Flat rotation curves | Galactic |
| $\Phi_{\text{mgl}}$ | $a_1 b_0 r/(m\bar{\ell})$ | Linear potential | Metagalactic |
| $\Phi_{\text{dS}}$ | $-a_2 b_0 r^2/(m\bar{\ell}^2)$ | de Sitter expansion | Cosmological |
| $\Phi_0$ | $(a_0 b_0 + a_2 q/\bar{\ell}^2)/m$ | Additive constant | -- |

### Gravitational Mass Generation

The Newtonian mass $M = a_1 q/(m\bar{\ell})$ is not fundamental but a composite phenomenon from: superfluid dynamics ($m$, $\bar{\rho}$), quantum temperature ($q$), and condensate wavefunction exponential ($a_1$). This is a quantum-mechanical Mach principle.

### Running Gravitational Coupling

The $\Phi_{\text{smi}}$ term induces a scale-dependent effective coupling:

$$G_{\text{eff}} \approx G\left[1 + \frac{\zeta_{\chi q}L_\chi\ln(r/\bar{\ell})}{r}\right]$$

Gravity naturally becomes stronger at shorter scales ($\ln r / r^3$), suggesting a resolution of the hierarchy problem.

### Galactic Rotation Curves

Combining $\Phi_N$, $\Phi_{\text{gal}}$, and $\Phi_{\text{mgl}}$:

$$v(R) = \sqrt{v_N^2 + v_{\text{gal}}^2 + \Phi_{\text{mgl}}(R)}$$

where $v_N^2 = GM/R$ (Keplerian) and $v_{\text{gal}}^2 = \chi b_0/m = \text{const}$ (flat plateau). The flat velocity $v_{\text{gal}}$ depends on parameters $\chi$ and $b_0$ which vary with the environment, explaining why different galaxies have different flat velocities.

At extragalactic scales ($R \gtrsim 10$ kpc):

$$v(R) \approx v_{\text{gal}}\sqrt{1 + R/L_\chi}$$

predicting deviation from flat to rising rotation curves in outer regions of large spiral galaxies (M31, M33).

### Cosmological Implications

**de Sitter spacetime:** $\Phi_{\text{dS}}$ induces asymptotically de Sitter spacetime with radius:

$$R_{\text{dS}} = \bar{\ell}\sqrt{mc_{(0)}^2/(2a_2 b_0)}$$

relating to the cosmological constant $\Lambda$ via $R_{\text{dS}}^{(\text{cos})} = \sqrt{3/\Lambda}$.

**Two expansion mechanisms:**
1. **Global:** Laminar flow of background superfluid induces FLRW spacetime via BEC-spacetime correspondence. Seen by R-observer as scalar-tensor gravity with action:
$$\tilde{S}[g, \not\phi] \propto \int d^D x \sqrt{-g} e^{\tilde{D}\phi}[R + \tilde{D}(\tilde{D}+1)(\nabla\phi)^2]$$
where $\phi = \ln(|\Psi_{(0)}|^2/\bar{\rho})$ is an induced dilaton.

2. **Local:** Cumulative effect from non-vanishing terms ($\Phi_{\text{gal}}$, $\Phi_{\text{mgl}}$, $\Phi_{\text{dS}}$) around a gravitating body.

These mechanisms have generally different expansion rates, potentially explaining the Hubble tension.

### Cosmological Coincidence Resolution

DM and DE are both manifestations of the same superfluid vacuum, so their densities are necessarily correlated. The cosmological coincidence $\tilde{\Omega}_{\text{DM}}/\tilde{\Omega}_{\text{DE}} \sim O(1)$ is trivially satisfied when DM-attributed ($\Phi_{\text{gal}}$, $\Phi_{\text{mgl}}$) and DE-attributed ($\Phi_{\text{mgl}}$, $\Phi_{\text{dS}}$) effects share the metagalactic term $\Phi_{\text{mgl}}$.

---

## Key Results

1. Physical vacuum modeled as a logarithmic superfluid induces a gravitational potential with seven distinct terms spanning sub-Newtonian to cosmological scales.
2. Flat galactic rotation curves arise from the logarithmic potential $\Phi_{\text{gal}} \propto \ln(r)$, with galaxy-dependent flat velocity determined by environment-dependent parameters.
3. Prediction: rotation curves become non-flat at extragalactic scales, $v^2 \propto 1 + R/L_\chi$.
4. The cosmological constant is not fundamental but a combination of superfluid parameters: $a_2 b_0/(m\bar{\ell}^2) \approx \Lambda c^2/6$.
5. Two distinct expansion mechanisms (global flow vs. local induced potential) can explain the Hubble tension.
6. Dark matter and dark energy are related phenomena from the same superfluid vacuum, resolving the cosmological coincidence problem.
7. Gravitational mass is emergent: $M = a_1 q/(m\bar{\ell})$, a quantum-mechanical Mach principle.

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Normalization | $\langle\Psi|\Psi\rangle = \int_V \rho \, dV = M$ | Eq. (1) |
| Wave equation | $[i\hbar\partial_t - \frac{\hbar^2}{2m}\nabla^2 + V_{\text{ext}} + F(|\Psi|^2)]\Psi = 0$ | Eq. (2) |
| Induced metric | $g_{\mu\nu} \propto \frac{\rho}{c_s}\begin{pmatrix} -(c_s^2 - \eta^2(\nabla S)^2) & -\eta\nabla S \\ -\eta\nabla S & I \end{pmatrix}$ | Eq. (5) |
| Logarithmic $F(\rho)$ | $F(\rho) = -b\ln(\rho/\bar{\rho})$ | Eq. (8) |
| Log-Schrodinger eq | $i\hbar\partial_t\Psi = [-\frac{\hbar^2}{2m}\nabla^2 + V_{\text{ext}} - b\ln(|\Psi|^2/\bar{\rho})]\Psi$ | Eq. (9) |
| Equation of state | $p = -(b/m)\rho, \quad c_s = \sqrt{|b|/m}$ | Eq. (10) |
| Inhomogeneous coupling | $b(r) = b_0 - q/r^2$ | Eq. (11) |
| Induced potential | $\Phi(r) = \frac{1}{m}(b_0 - q/r^2)\ln(|\Psi_{\text{vac}}|^2/\bar{\rho})$ | Eq. (15) |
| Seven-term decomposition | $\Phi = \Phi_{\text{smi}} + \Phi_{\text{RN}} + \Phi_N + \Phi_{\text{gal}} + \Phi_{\text{mgl}} + \Phi_{\text{dS}} + \Phi_0$ | Eq. (20) |
| Newtonian term | $\Phi_N = -GM/r$ with $GM = a_1 q/(m\bar{\ell})$ | Eq. (23) |
| Galactic (flat) term | $\Phi_{\text{gal}} = \chi b_0\ln(r/\bar{\ell})/m = c_b^2\chi\ln(r/\bar{\ell})$ | Eq. (24) |
| de Sitter term | $\Phi_{\text{dS}} = -c_b^2 r^2/L_{\text{dS}}^2$ | Eq. (26) |
| Running $G_{\text{eff}}$ | $G_{\text{eff}} \approx G[1 + \zeta_{\chi q}L_\chi\ln(r/\bar{\ell})/r]$ | Eq. (40) |
| Rotation curve | $v(R) = \sqrt{GM/R + \chi b_0/m + a_1 b_0 R/(m\bar{\ell})}$ | Eq. (63) |
| Non-flat asymptotic | $v(R) \approx v_{\text{gal}}\sqrt{1 + R/L_\chi}$ | Eq. (66) |
| Cosmological constant | $a_2 b_0/(m\bar{\ell}^2) \approx \Lambda c^2/6 \sim 10^{-36}\text{s}^{-2}$ | Eq. (73) |
| Dilaton action | $\tilde{S} \propto \int d^Dx\sqrt{-g}e^{\tilde{D}\phi}[R + \tilde{D}(\tilde{D}+1)(\nabla\phi)^2]$ | Eq. (71) |

---

## Relevance to Phonon-Exflation

This paper is a close cousin to the phonon-exflation framework. Both treat the vacuum as a superfluid/BEC substrate whose excitations are the particles of physics, with spacetime emerging from the condensate dynamics via the BEC-spacetime correspondence. Zloshchastiev's key result -- that a logarithmic superfluid vacuum induces a seven-term gravitational potential spanning all scales from sub-Newtonian to cosmological -- maps onto the framework's program where DM arises from quasiparticle dispersion and DE from spectral mixing across the M4 $\times$ SU(3) fabric (the PI prediction, `memory/project_pi-fabric-prediction.md`). The logarithmic potential $\Phi_{\text{gal}} = c_b^2\chi\ln(r/\bar{\ell})$ producing flat rotation curves is the SVT analog of the framework's claim that DM effects emerge from the substrate without exotic matter. The two expansion mechanisms (global flow + local induced) parallel the framework's finding that the cosmological constant arises from instanton gas dynamics (Session 38) while local Hubble rates depend on fiber complexity $\tau$ (the substrate compaction/timescape insight from Session 59). The emergent mass formula $M = a_1 q/(m\bar{\ell})$ is a concrete realization of the phonon-exflation claim that particle masses are phononic eigenvalues of the internal geometry.
