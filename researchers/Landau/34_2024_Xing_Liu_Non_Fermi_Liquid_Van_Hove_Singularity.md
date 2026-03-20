# Non-Fermi-Liquid/Marginal-Fermi-Liquid Signatures Induced by Van Hove Singularity

**Author(s):** Yi-Hui Xing and Wu-Ming Liu

**Year:** 2024

**Journal:** arXiv:2401.10707

---

## Abstract

A two-dimensional metal coupled to critical magnons and featuring van Hove singularities on the Fermi surface exhibits non-Fermi-liquid behavior in the translationally invariant limit. The van Hove singularities suppress contributions from regions away from these special points, causing NFL signatures to dominate. Introduction of disorder causes a crossover from non-Fermi-liquid to marginal-Fermi-liquid, generating strange metal characteristics including $T \ln(1/T)$ specific heat and temperature-linear resistivity. The work identifies critical temperatures for superconductivity induced by van Hove effects and predicts emergence of pair-density-wave superconducting states.

---

## Historical Context

Since Landau's Fermi liquid theory established that normal metals can be understood as noninteracting quasiparticles, deviations from Fermi liquid behavior have become a central focus of condensed matter physics. Van Hove singularities—singularities in the density of states at critical points in the Brillouin zone—represent a canonical source of strong many-body interactions that can destabilize the Fermi liquid. Their role in high-$T_c$ superconductivity, organic conductors, and graphene-like systems has motivated decades of investigation.

This work extends the classical picture by showing that van Hove singularities coupled to critical fluctuations (here, magnons) can induce non-Fermi-liquid behavior even in clean, translationally invariant systems. The marginal-Fermi-liquid behavior that emerges with disorder provides a microscopic origin for the $T$-linear resistivity and logarithmic specific heat observed in heavy fermion materials, cuprates, and other strongly correlated systems.

Landau's framework emphasized that the effective interaction between quasiparticles becomes strongly enhanced near singularities in the density of states. This work recapitulates that insight in the context of coupled electrons and critical bosons, showing how non-Fermi-liquid scaling emerges naturally from kinetic renormalization near the van Hove point.

---

## Key Arguments and Derivations

### Van Hove Singularities and Density of States

The density of states near a van Hove singularity (vHs) in 2D exhibits a logarithmic divergence:

$$N(E) \sim |\ln|E - E_{\text{vH}}||$$

At the band maximum (or minimum), the Fermi surface nests itself locally, creating a flat region in $\mathbf{k}$-space. This high density of states naturally enhances electron-electron scattering and provides a platform for instabilities. In the presence of a coupling to a bosonic order parameter (here, critical magnons), the effective interaction becomes strongly retarded.

### Yukawa Coupling to Magnons

The electron-magnon coupling is formalized as:

$$H_{\text{int}} = \lambda \sum_{i,q} c^\dagger_{i,\sigma} c_{i+q,\sigma} b_q + \text{h.c.}$$

where $b_q$ is the magnon annihilation operator. Near a magnetic quantum critical point, magnons exhibit critical scaling with dynamical exponent $z$:

$$\omega_q \sim q^z$$

For a three-dimensional magnet undergoing a quantum phase transition, $z \sim 2$, but in 2D or in quasi-2D systems, this can be reduced. The combination of vHs and critical magnons produces non-Fermi-liquid scaling.

### Scaling Analysis and Renormalization Group

In the clean limit, the RG flow near the fixed point gives rise to scaling dimensions:

$$[\psi] = \frac{1 - d/2}{1 + \lambda N(E_F) z}$$

where $d$ is the spatial dimension and $\lambda N(E_F)$ measures the strength of coupling. For $2D$ with vHs, the effective coupling becomes marginal or irrelevant depending on the magnon exponent. The marginal case ($\lambda N(E_F) z \sim 1$) produces logarithmic corrections:

$$\sigma(\omega, T) \sim \sigma_0 \left[1 + \frac{\lambda N(E_F)}{\pi} \ln\left(\frac{\max(\omega, T)}{E_0}\right)\right]^{-1}$$

This gives $\rho(T) \sim T \ln(1/T)$ for $T \ll E_F$, characteristic of marginal Fermi liquid behavior.

### Disorder and Crossover Mechanism

Disorder in the Yukawa coupling breaks translational symmetry and shifts the fixed point. The inclusion of random potential:

$$V_{\text{disorder}} = \sum_i \xi_i c^\dagger_i c_i$$

with $\xi_i$ spatially random reduces the energy scale of the non-Fermi-liquid anomaly. In the Born approximation, disorder introduces an elastic scattering rate:

$$\gamma_{\text{el}} = \pi n_{\text{imp}} |V_0|^2 N(E_F)$$

Disorder effectively increases the threshold energy scale for observing pure NFL behavior. Below this scale, marginal-Fermi-liquid behavior dominates, with $T$-linear resistivity:

$$\rho(T) \approx \rho_0 + \alpha T$$

emerging as the dominant temperature dependence.

### Superconductivity from van Hove Points

The high density of states at the van Hove singularity enhances the pairing interaction. In BCS theory with a van Hove-enhanced density:

$$T_c \propto E_D \exp\left( - \frac{1}{\lambda N(E_F)} \right)$$

becomes sharply increased. The authors find that superconductivity can be induced by magnon-mediated pairing:

$$V_{\text{pair}} \propto \lambda^2 \frac{\chi_m(\omega)}{(\omega - v_F|\mathbf{q}|)^2}$$

where $\chi_m(\omega)$ is the magnon susceptibility. The momentum dependence of this interaction can stabilize pair-density-wave (PDW) states, where the Cooper pair momentum is non-zero (analogous to FFLO states):

$$\Delta_{\mathbf{k}} = \Delta_0 \cos(2\mathbf{Q} \cdot \mathbf{r})$$

with ordering vector $2\mathbf{Q}$ selected by the nesting properties of the van Hove point.

---

## Key Results

1. **Non-Fermi-Liquid Scaling** — Van Hove singularities coupled to critical magnons suppress standard Fermi liquid quasiparticle behavior, producing non-analytic corrections to transport and thermodynamic observables.

2. **Marginal-Fermi-Liquid Crossover** — Disorder causes a crossover from pure NFL to marginal-FL, with both temperature-linear resistivity and logarithmic specific heat $C \sim T \ln(1/T)$.

3. **Superconducting Instability** — The enhanced density of states at the vHs lowers $T_c$, and magnon-mediated pairing can stabilize pair-density-wave superconductivity with finite Cooper pair momentum.

4. **Strange Metal Phenomenology** — The marginal-FL fixed point naturally reproduces the empirical $\rho(T) \sim T$ and $C/T \sim \ln(1/T)$ observed in cuprates and heavy fermion systems.

5. **Kinetic Origin** — Non-Fermi-liquid behavior arises from kinetic (one-particle scattering) renormalization, not from emergent gauge fields or topological order, making it accessible to standard many-body perturbation theory.

---

## Impact and Legacy

This work extends Landau's insight about the fragility of the Fermi liquid near singularities in the density of states to the case where that singularity is coupled to a quantum critical boson. It provides a unified framework for understanding non-Fermi-liquid behavior in disparate materials—from organic conductors to cuprates—that share the common feature of van Hove singularities.

The prediction of pair-density-wave superconductivity offers a microscopic mechanism for exotic pairing states observed in some high-$T_c$ materials. The crossover to marginal-Fermi-liquid behavior under disorder is particularly relevant for understanding why samples with varying impurity content show different transport exponents.

The work has implications for understanding the stability of Fermi liquid theory near quantum critical points, a theme that connects to more recent work on quantum critical metals and strange metallic behavior in the disordered limit.

---

## Framework Relevance

**Framework Parallel**: The phonon-exflation framework places the SU(3) fiber at a van Hove singularity in the Dirac spectrum at the fold point (Session 35, Session 40). The present work establishes that van Hove singularities generically induce strong interactions and non-Fermi-liquid behavior. This suggests that at the fold, the Dirac sea exhibits enhanced interactions analogous to the non-Fermi-liquid regime studied here.

**Non-Fermi-Liquid in the Spectral Action**: The Dirac spectrum near the fold has a density-of-states singularity (VHS). The framework's instanton gas may be understood as the many-body response of the Dirac sea to this singularity—analogous to the non-Fermi-liquid pairing instability described by Xing-Liu. The pair-density-wave order with spatially modulated gap could provide an alternate picture for the off-Jensen condensate formation.

**Disorder-Induced Crossover**: Session 40 showed that small perturbations to the fold geometry (broken integrability via weak Jensen deformation) shift the BCS phase diagram. This parallels the disorder-induced crossover from NFL to marginal-FL in the present work. Both suggest that small symmetry breaking can stabilize an otherwise marginal phase.

**Superconductivity from vHs**: The mechanism for $T_c$ enhancement from van Hove coupling (high $N(E_F)$) directly applies to the framework's BCS gap formation at the fold, where $N(E_F) = 1.674$ (Session 35). The magnon-mediated pairing here is the CM analog of the spectral-action-mediated pairing in the framework.

---

## References

- Xing, Y.-H., & Liu, W.-M. (2024). Non-Fermi-liquid/Marginal-Fermi-liquid signatures induced by van Hove singularity. *arXiv preprint arXiv:2401.10707*.
- Landau, L. D. (1956). The theory of a Fermi liquid. *Soviet Physics JETP*, 3(12), 920-925.
- Varma, C. M., et al. (1989). Phenomenology of the normal state of high-Tc superconductors. *Physical Review Letters*, 63(19), 1996.
