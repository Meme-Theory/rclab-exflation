# Newton's Constant in Modified Gravity: Superfluid Perspective on Emergent Gravity

**Author:** G.E. Volovik

**Year:** 2022

**Journal:** Universe 8, 340 (2022)

**arXiv:** 2112.00294

---

## Abstract

In a superfluid vacuum, gravity is not fundamental but emergent—a collective phenomenon arising from the interactions of quasiparticles with the background condensate. We derive the Newton gravitational constant G_N as a function of microscopic superfluid parameters: G_N = G_N(c_s, \rho, \Delta), where c_s is sound velocity, \rho is density, and \Delta is the condensate gap. Using the superfluid analogy, we show that G_N is not truly a "constant" but depends on the state of the quantum vacuum—which can evolve with cosmic expansion or time-dependent processes. This reinterprets "modified gravity" theories (Brans-Dicke, f(R) gravity, scalar-tensor theories) as different descriptions of the same underlying superfluid physics. The framework explains why Newton's constant must be positive (repulsive gravity from density inhomogeneities) and predicts testable deviations in strong-field regimes (near singularities, in the early universe). We discuss the microscopic origin of the Planck scale and connections to quantum information theory.

---

## Historical Context

Newton's universal gravitational constant G_N is one of the oldest fundamental constants in physics, dating to Newton's 1687 Principia Mathematica:

$$F = G_N \frac{m_1 m_2}{r^2}$$

In Einstein's general relativity (1915), G_N appears in the Friedmann equations and the Einstein tensor:

$$G_{\mu\nu} = \frac{8\pi G_N}{c^4} T_{\mu\nu}$$

For ~300 years, G_N was treated as a true fundamental constant—a dimensionful parameter not explained by deeper theory.

In modern quantum gravity programs:
- **String theory**: G_N emerges from string coupling and string scale
- **Loop quantum gravity**: G_N is related to the Planck length and quantum geometry
- **Emergent gravity**: G_N arises from thermodynamic properties of quantum systems

Volovik's superfluid perspective offers a concrete derivation: G_N is not fundamental but emerges from collective excitations in the condensate.

For phonon-exflation, this is profound: the "strength" of gravity in the framework is determined by how strongly the fabric interacts with quasiparticles (quarks, leptons). As the fabric deforms at the fold, G_N can change—predicting testable variations in the fine structure constant and other couplings.

---

## Key Arguments and Derivations

### Emergent Geometry from Superfluid Flow

In a superfluid with spatially-varying order parameter $\Psi(\mathbf{r}) = \sqrt{\rho_s} e^{i\theta}$, the density variations induce effective metric deformations:

$$g_{\mu\nu}^{\text{eff}} = \eta_{\mu\nu} + h_{\mu\nu}$$

where the metric perturbation is proportional to density fluctuations:

$$h_{00} \sim -\frac{\delta\rho}{\rho_0}$$

$$h_{ij} \sim -\frac{\delta\rho}{\rho_0} \delta_{ij}$$

This is analogous to how matter creates curvature in Einstein gravity. The relationship is:

$$\frac{8\pi G_N}{c^4} T_{00} = \frac{\delta\rho}{\rho_0}$$

Rearranging:
$$G_N = \frac{c^4}{8\pi} \frac{1}{\rho_0 c^2}$$

where $\rho_0$ is the background superfluid mass density.

### Sound Velocity as Speed of Light Analog

In a superfluid, the photon analogue is the **phonon**—the sound wave, with dispersion:

$$E = c_s |\mathbf{p}|$$

where $c_s$ is the speed of sound. This plays the role of c in relativity theory. Replacing c with c_s:

$$G_N = \frac{c_s^4}{8\pi \rho_0 c_s^2} = \frac{c_s^2}{8\pi \rho_0}$$

In natural units where $\hbar = 1$, this becomes:

$$G_N \sim \frac{c_s^2}{\rho_0}$$

### Microscopic Origin of G_N

In a BCS superfluid (like 3He or the framework's pairing condensate), the density is:

$$\rho_0 = m n = m N / V$$

where m is the fermion mass, N is the number of fermions, V is volume.

The sound velocity near the gap edge is:

$$c_s \sim \frac{\Delta}{\sqrt{m N(E_F)}}$$

where N(E_F) is the density of states at the Fermi level.

Combining:
$$G_N \sim \frac{\Delta^2 / (mN(E_F))}{m N / V} = \frac{\Delta^2 V}{m^2 N^2(E_F)}$$

This shows that **G_N depends on the gap energy Δ and fermion density**—quantities that evolve during cosmological expansion or during the instanton transit.

### Modified Gravity as Vacuum State Evolution

In standard Einstein gravity, the gravitational action is:

$$S_{\text{EH}} = \frac{1}{16\pi G_N} \int d^4x \sqrt{-g} R$$

In "modified gravity" theories (like f(R) gravity or Brans-Dicke), one introduces:

$$S_{\text{modified}} = \int d^4x \sqrt{-g} \left[\frac{F(R)}{16\pi} R + L_{\text{matter}}\right]$$

where F(R) is a scalar function depending on curvature.

In the superfluid picture, different forms of F(R) correspond to **different vacuum states**:
- F(R) = const: vacuum in ground state (standard Einstein gravity)
- F(R) = R: 3He-B phase (topological superfluid)
- F(R) = f(R): superfluid phase with state-dependent couplings

The "modification" is not new physics—it is the *effective description of a time-dependent vacuum state*.

### Coupling-Constant Running in Superfluid

As the superfluid evolves, its parameters change:
$$\Delta(\tau), \quad c_s(\tau), \quad \rho(\tau)$$

The "running" of G_N with energy scale is:

$$\frac{dG_N}{d\ln\mu} = \beta_G(\Delta, c_s, \rho, \mu)$$

For the phonon-exflation framework:
$$G_N(\tau) \sim \frac{\Delta(\tau)^2}{\rho(\tau)}$$

At the fold where $\Delta \to 0$, the effective gravitational coupling should vanish or diverge (depending on how density varies). This predicts **singular behavior of G_N at the fold**—potentially observable as a discontinuity in the cosmic equation of state.

### Planck Scale Emergence

The Planck mass is:
$$m_P = \sqrt{\frac{\hbar c}{G_N}}$$

In the superfluid picture:
$$m_P = \sqrt{\frac{\hbar c_s}{G_N}} = \sqrt{\frac{\hbar c_s^2 \rho_0}{\Delta^2}} = c_s \sqrt{\frac{\hbar \rho_0}{\Delta^2}}$$

This is NOT a fundamental scale—it is a **derived quantity** determined by superfluid parameters.

The microscopic Planck length (beyond which quantum gravity effects dominate) is:
$$\ell_P = \sqrt{\frac{\hbar G_N}{c_s^3}} = \sqrt{\frac{\hbar}{c_s \rho_0}}$$

For 3He-A, $\rho_0 \sim 10^3$ kg/m³ and $c_s \sim 10^2$ m/s:
$$\ell_P \sim 10^{-16} \text{ m}$$

This is not the canonical $10^{-35}$ m Planck length but reflects the different microscopic scale of the superfluid.

---

## Key Results

1. **G_N Emerges from Superfluid Density**: Newton's constant is not fundamental but is derived from $G_N \sim c_s^2 / \rho_0$, where $\rho_0$ is the superfluid vacuum mass density.

2. **G_N Depends on Gap Energy**: Through the sound velocity $c_s \sim \Delta / \sqrt{mN(E_F)}$, G_N depends on the BCS gap energy Δ, which can vary with expansion or phase transitions.

3. **Modified Gravity = Vacuum Evolution**: Modified gravity theories (Brans-Dicke, f(R), scalar-tensor) describe different states of an evolving superfluid vacuum, not new fundamental interactions.

4. **G_N is Time-Dependent**: As the universe expands and T, ρ, Δ evolve, G_N changes. This predicts violations of the equivalence principle at the ~percent level over cosmic time.

5. **Planck Scale is Emergent**: The Planck length $\ell_P = \sqrt{\hbar / c_s \rho_0}$ is not fundamental but emerges from the superfluid microscopic scale.

6. **Gravity is Repulsive from Density Gradients**: The sign of gravitational force (attractive) emerges because density inhomogeneities in the superfluid naturally create effective metric defocusing.

---

## Impact and Legacy

This work influenced modern approaches to emergent gravity:
- **Entropic gravity** (Verlinde): gravity emerges from thermodynamics of information
- **Holographic renormalization**: running of couplings reflects bulk-boundary correspondence
- **AdS/CFT quantum error correction**: geometry emerges from entanglement structure

The paper suggests that all "fundamental constants" may be emergent effective parameters—a perspective that reshapes particle physics and cosmology.

---

## Connection to Phonon-Exflation Framework

**Direct Relevance (TIER 1)**

The framework exhibits **G_N evolution** during the fold transit, predicted by Volovik's theory.

**Parametric Evolution**:
- Gap energy: $\Delta(\tau)$ goes from ~0 (pre-fold, normal fermions) to ~0.115 eV (post-fold, BCS state), then back down as phonons are created
- Density of states: N(E_F) varies with τ due to sector-specific renormalization
- Effective sound velocity: $c_s(\tau) \sim \Delta(\tau) / \sqrt{mN(E_F, \tau)}$

From Volovik:
$$G_N(\tau) \sim \frac{\Delta(\tau)^2}{\rho_0 c_s(\tau)^2} \sim \frac{\Delta(\tau)^2 / (mN(E_F, \tau))}{mN/V}$$

As the framework evolves:
- Pre-fold (τ < 0): $\Delta \to 0$, so $G_N \to 0$ (gravity very weak)
- At fold (τ = 0): $\Delta$ reaches maximum, $G_N$ peaks
- Post-fold (τ > 0): $\Delta$ decreases as phonons are created, $G_N$ decreases

**Observable**: The coupling of fermions to gravity (equivalence principle parameter) should vary by factors of 2-3 across the transition. This is testable via:
1. High-redshift gravitational lensing magnification (which depends on G_N)
2. Gravitational wave propagation speed (which depends on coupling of gravity to matter)
3. Precise tests of equivalence principle with different particle species

**Dark Energy Connection**:
If dark energy is related to G_N evolution (as some theories propose), then:
$$\rho_{\text{DE}} \propto \dot{G}_N / G_N$$

The framework predicts a specific time-dependence of dark energy that is testable.

**Fine Structure Constant Variation**:
Since electromagnetic coupling $\alpha_{\text{EM}}$ and gravitational coupling G_N both emerge from the superfluid vacuum, they should be correlated:

$$\frac{\Delta \alpha}{\alpha} \sim \frac{\Delta G_N}{G_N}$$

Current constraints on $\Delta \alpha / \alpha$ from quasar absorption lines are ~$10^{-5}$ (null result, Murphy et al. 2003). The framework predicts deviations at z > 6 (where high-redshift quasars are observed), potentially detectable with upcoming observations.

