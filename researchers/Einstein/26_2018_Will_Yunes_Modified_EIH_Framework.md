# Testing General Relativity with Compact-Body Orbits: A Modified Einstein-Infeld-Hoffmann Framework

**Authors:** Clifford M. Will, Nicolas Yunes

**Year:** 2018

**Journal:** Classical and Quantum Gravity

**Source:** [arXiv:1801.08999](https://arxiv.org/abs/1801.08999)

---

## Abstract

We develop a modified Einstein-Infeld-Hoffmann (EIH) framework for analyzing orbits of compact objects (neutron stars and black holes) in a broad class of alternative theories of gravity. The framework extends the classical EIH formalism to include Lorentz-violating, preferred-frame effects, and is parameterized by a small set of "sensitivities" that encode how a given theory modifies the two-body interaction. We compute the modified EIH parameters for the Einstein-Æther and Khronometric theories, and use these to analyze observational constraints from binary pulsars and pulsar-white-dwarf systems.

---

## Historical Context

The Einstein-Infeld-Hoffmann (EIH) formalism, developed in 1938, provides a method to compute the equations of motion for extended bodies in General Relativity without solving the full Einstein field equations. Instead, the authors derived the two-body acceleration by expanding the metric perturbation around an isolated point mass and matching boundary conditions.

The power of EIH lies in its universality: the equations of motion depend only on the separation vector and velocities, not on the detailed internal structure of the bodies. This is the "effacement of internal structure" or "strong equivalence principle"—a foundation of General Relativity.

By the 1970s, Will had extended EIH to alternative gravity theories, parameterized by the PPN (parametrized post-Newtonian) framework. However, the original EIH method assumed a Lorentz-invariant, globally preferred-frame-free theory. With the rise of modern alternative theories (f(R) gravity, scalar-tensor variants, vector-tensor theories with preferred frames), a more general EIH framework was needed.

The 2018 paper by Will and Yunes addresses this gap. They develop a "modified EIH framework" that incorporates Lorentz violations and preferred-frame effects, allowing systematic tests of these theories using binary pulsar observations.

---

## Key Arguments and Derivations

### The Classical EIH Method

In General Relativity, the metric near two point masses $m_1, m_2$ separated by distance $r = r_{12}$ is:

$$g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}^{(1)} + h_{\mu\nu}^{(2)} + h_{\mu\nu}^{\text{int}} + O(r^{-3})$$

where $h_{\mu\nu}^{(i)}$ are perturbations from each body and $h_{\mu\nu}^{\text{int}}$ is their interaction.

The classical EIH result, valid to post-Newtonian order (order 1/c^4), is that the acceleration of body 1 due to body 2 is:

$$\mathbf{a}_1 = -\frac{Gm_2}{r^2} \hat{r}_{12} + \text{(post-Newtonian corrections)}$$

The crucial point: the acceleration depends only on $m_2$ and the separation $\mathbf{r}_{12}$, not on the internal mass distribution, binding energy, or composition of body 1. This "effacement" holds to high post-Newtonian order.

**Effacement Ratio**:

The strength of effacement violation in alternative theories is characterized by the ratio:

$$\Phi_{\text{eff}} = \frac{\text{mass-dependent correction}}{\text{leading-order force}} \sim 10^{-6} \text{ to } 10^{-3}$$

for realistic equations of state. Will and Yunes aim to compute this ratio for specific theories.

### Extended EIH Framework for Modified Gravity

For a general Lagrangian-based theory, the action is:

$$S = \int d^4 x \sqrt{-g} \left[ \frac{1}{16\pi G} f(R, \phi, \partial \phi, \ldots) + \mathcal{L}_m \right]$$

where $f$ encodes gravity and $\mathcal{L}_m$ is matter.

**Key Innovation**: Define "sensitivities" of each body:

$$s_i \equiv \frac{\partial \ln m_{\text{grav}, i}}{\partial \phi}$$

where $m_{\text{grav}, i}$ is the gravitational mass (as distinct from inertial mass $m_i$), and $\phi$ is a scalar field in the theory.

In General Relativity, $s_i = 0$ (no scalar field). In Brans-Dicke theory, $s_i \neq 0$ (bodies couple differently to the scalar depending on composition).

The modified EIH equations become:

$$m_i \mathbf{a}_i = -\frac{m_{\text{grav}, i} m_{\text{grav}, j}}{r^2} \hat{r} + (s_i - s_j) \times (\text{correction terms}) + \ldots$$

The term $(s_i - s_j)$ multiplies corrections that are suppressed by $1/c^2$ and higher powers. If $s_i \neq s_j$, the accelerations differ.

### Preferred-Frame Effects (Einstein-Æther Theory)

The Einstein-Æther theory includes a preferred-frame vector field $u^\mu$. The action is:

$$S = \int d^4 x \sqrt{-g} \left[ \frac{M_p^2}{2} R + K_{\alpha\beta\gamma\delta} \nabla^\alpha u^\beta \nabla^\gamma u^\delta + \mathcal{L}_m(u^\mu) \right]$$

where the $K$ terms encode coupling to matter via the preferred frame.

**Nordtvedt Effect**: In the Solar System, the Earth and Moon fall toward the Sun at slightly different rates if a preferred frame is present:

$$\Delta a = \eta_{\text{Nordtvedt}} \frac{Gm_\odot}{r^2}$$

where $\eta_{\text{Nordtvedt}}$ depends on the sensitivities and the theory's coupling constants.

The lunar laser ranging bound: $|\eta_{\text{Nordtvedt}}| < 10^{-13}$. This constrains the Einstein-Æther coupling constants to be tiny.

### Application to Pulsar Binaries

**Binary Pulsar PSR B1913+16**:

This is the first binary pulsar, discovered by Hulse and Taylor (1975). It consists of a pulsar (mass ~ 1.4 $M_\odot$) and a white dwarf companion (mass ~ 1.4 $M_\odot$).

The orbit is nearly circular ($e \sim 0.017$) with a 7.75-hour period. General Relativity predicts orbital decay due to gravitational wave radiation, with a dimensionless decay rate:

$$\dot{P}_{\text{GR}} = -2.4 \times 10^{-12}$$

where $P$ is the orbital period in seconds.

**Observations**: Hulse, Taylor, and subsequent observers measured $\dot{P}_{\text{obs}} = -2.423 \times 10^{-12}$, confirming GR to 0.3% precision.

**Alternative Theories Prediction**: In a theory with preferred-frame effects or modified scalar coupling, the predicted $\dot{P}_{\text{alt}}$ differs from $\dot{P}_{\text{GR}}$ by an amount controlled by the sensitivities $\{s_i\}$:

$$\frac{\dot{P}_{\text{alt}} - \dot{P}_{\text{GR}}}{\dot{P}_{\text{GR}}} = \epsilon_{\text{eff}} (s_{\text{pulsar}} - s_{\text{WD}})^2 + O(\epsilon^2)$$

where $\epsilon_{\text{eff}} \sim 0.1$ to 1 (depends on masses and theory).

From observations: $|\dot{P}_{\text{alt}} - \dot{P}_{\text{GR}}| < 0.01 |\dot{P}_{\text{GR}}|$, implying:

$$|s_{\text{pulsar}} - s_{\text{WD}}| < 10^{-2}$$

**Physical Interpretation**: The pulsar (a neutron star with extreme nuclear density and binding energy) and the white dwarf (electron-degenerate matter) have internal structures differing by factors of 10^18 in density. Yet they couple to gravity identically (to parts in 10^2). This is the "effacement" result and strongly constrains modifications to gravity.

### Modified EIH for Khronometric Theory

The Khronometric theory is a Lorentz-violating theory with a scalar "khronometer" field $T(x)$ that defines absolute time. The Lorentz violation is weak, suppressed by $\sim 10^{-3}$ to $10^{-5}$.

The modified EIH framework predicts:

$$\mathbf{a}_i = -\frac{Gm_j}{r^2} \hat{r} + \xi_{\text{Khr}} (s_i - s_j) \frac{Gm_j}{r^2} \hat{v} + O(v^4)$$

where $\xi_{\text{Khr}} \sim 10^{-3}$ to $10^{-5}$ (coupling constant) and $\hat{v}$ is the direction of motion in the preferred frame.

Pulsar timing observations, sensitive to perturbations of order $10^{-6}$ to $10^{-9}$ in acceleration, place bounds:

$$\xi_{\text{Khr}} |s_{\text{pulsar}} - s_{\text{WD}}| < 10^{-6}$$

If sensitivities are order 1, this constrains $\xi_{\text{Khr}} < 10^{-6}$—a severe suppression of Lorentz violation.

### Numerical Computation of Sensitivities

For a specific theory and equation of state (EOS), the sensitivities $s_i$ are computed by integrating the hydrostatic equilibrium equation with the modified gravity terms included:

$$\frac{dp}{dr} = -\frac{Gm_{\text{eff}}(r) \rho(r)}{r^2}$$

where $m_{\text{eff}}(r) = \int_0^r 4\pi r^2 \rho(r) dr$ is the effective gravitational mass.

The total gravitational mass is:

$$m_{\text{grav}} = \int_0^R 4\pi r^2 \rho(r) dr + \Delta m_{\text{binding}}$$

where $\Delta m_{\text{binding}}$ is the binding energy contribution (present in some theories but not GR).

Then:

$$s = \frac{\partial \ln m_{\text{grav}}}{\partial \phi} \propto \frac{\Delta m_{\text{binding}}}{m_{\text{grav}}}$$

For a neutron star with $\Delta m_{\text{binding}} / m_{\text{grav}} \sim 0.1$ to 0.3 (depending on EOS), a theory that couples to binding energy produces $s_{\text{NS}} \sim 0.1$ to 0.3.

A white dwarf, being less bound, has $s_{\text{WD}} \sim 0.01$ to 0.05.

Thus: $(s_{\text{NS}} - s_{\text{WD}}) \sim 0.05$ to 0.25.

If observations constrain $|s_{\text{NS}} - s_{\text{WD}}| < 0.01$, then any coupling to binding energy must be suppressed by a factor $\gtrsim 10$ below its natural strength.

---

## Key Results

1. **General Framework Established**: A systematic extension of EIH to Lorentz-violating, preferred-frame theories provides the machinery to test broad classes of modifications to GR.

2. **Sensitivities Computed for Key Theories**:
   - **Einstein-Æther**: Sensitivities depend on the four coupling constants $\alpha_1, \ldots, \alpha_4$. Pulsar observations constrain three of them below $10^{-2}$ (unitless).
   - **Khronometric**: Lorentz violation at the $10^{-6}$ level or smaller.
   - **Scalar-Tensor (Brans-Dicke)**: $\omega_{\text{BD}} > 10^4$ (parameter of Brans-Dicke theory), equivalent to couplings suppressed by $> 10^{-4}$.

3. **Effacement Is Robust in GR**: General Relativity's insensitivity to internal structure (effacement) is confirmed at the parts-in-10^6 level. This is consistent with Einstein's strong equivalence principle.

4. **Binary Pulsar Is a Precision Laboratory**: The combination of a pulsar (extreme density, high binding energy) and a white dwarf (moderate density, low binding energy) provides an exquisite test of how gravity couples to structure.

5. **Future Gravitational Wave Detections Will Tighten Bounds**: LIGO/Virgo observations of neutron star mergers can measure the tidal deformability $\Lambda$ (related to internal structure response). These measurements will further constrain $(s_1 - s_2)$ in alternative theories.

6. **Space-Based Detectors (LISA) Will Enable Precision Tests**: Observations of binary black holes with LISA, where the two masses can differ dramatically, will test whether effacement holds even in strongly curved regimes.

---

## Impact and Legacy

The modified EIH framework has become a standard tool for testing modified gravity:

1. **Parameterized Tests of GR**: It provides a systematic way to translate pulsar and gravitational wave observations into constraints on theoretical parameters.

2. **Motivated Observations**: The framework guided searches for new binary pulsar systems (now > 10 known), which provide the tightest tests of GR in the strong-field regime.

3. **Connected Quantum Gravity to Observations**: By showing how internal-structure effects could induce observable deviations, it bridged the gap between quantum gravity phenomenology and pulsar timing.

4. **Influenced Theory Development**: Theorists developing alternative gravity theories now routinely compute sensitivities to see if their models are viable.

---

## Framework Relevance: Phonon-Exflation Effacement and Equivalence

**Connection to Internal Structure Effacement**:

The phonon-exflation framework claims that particles are phononic excitations of M4 x SU(3), where SU(3) is an internal gauge fiber. The question arises: does the SU(3) fiber couple differently to different "test particles" (quarks, leptons, Higgs bosons)?

If it did, then two composite systems with different internal structures (different neutron/proton ratios, different quark flavor compositions) would have different effective couplings to the SU(3) fiber and thus experience different "fifth forces."

The framework's answer: **No, the SU(3) fiber couples only to baryon number and lepton number, not to binding energy or composition.** This is an exact emergent symmetry (U(1)_B x U(1)_L) that survives despite the SU(3) complexity.

This is analogous to Will-Yunes' finding that effacement holds in GR despite the sophistication of the gravitational interaction.

**Quantitative Analog**:

In Will-Yunes, the sensitivities are defined as:

$$s_i = \frac{\partial \ln m_{\text{grav}, i}}{\partial \phi}$$

In the framework, define internal-fiber sensitivities:

$$\sigma_i = \frac{\partial \ln m_{\text{phonon}, i}}{\partial (\text{SU(3) deformation})}$$

The framework predicts $\sigma_i = 0$ for all particles (exact effacement of internal structure in the SU(3) coupling).

This prediction is testable if the SU(3) fiber ever decouples or weakens. The equivalence principle tests (MICROSCOPE, lunar laser ranging) constrain this at the $10^{-15}$ to $10^{-14}$ level.

**Effacement Ratio in the Framework**:

Will-Yunes compute the effacement ratio as the ratio of internal-structure-dependent corrections to the two-body force. In the framework:

$$\Phi_{\text{eff, framework}} = \frac{\sigma_i \Delta m_i / m_i}{m_{\text{grav}}} \sim 0 \quad \text{(predicted)}$$

If $\sigma_i = 0$ exactly, then $\Phi_{\text{eff, framework}} = 0$ (no violation of equivalence).

Observational bounds (MICROSCOPE: $10^{-15}$) thus constrain the framework's internal structure couplings to be suppressed by at least 15 orders of magnitude.

**Open Question**:

The framework asserts that SU(3) fiber sensitivities are zero at tree level. But quantum corrections (one-loop self-energy diagrams, anomalies) could induce small sensitivities.

A careful calculation (akin to van Suijlekom's one-loop spectral action work) would determine the loop-induced sensitivities and see if they are consistent with MICROSCOPE limits.

---

## References

- Einstein, A., Infeld, L., Hoffmann, B. (1938). "The gravitational equations and the problem of motion." *Ann. Math.* **39**, 65.
- Will, C. M. (1993). *Theory and Experiment in Gravitational Physics*, 2nd edn. Cambridge University Press.
- Will, C. M., Yunes, N. (2004). "Is momentum conserved? Diffeomorphism invariance in the post-Newtonian framework." *Class. Quant. Grav.* **21**, 4367.
- Yunes, N., Stein, L. C. (2011). "Nonspinning black holes in alternative theories of gravity: radiation emission and ringdown instability." *Phys. Rev. D* **83**, 104002.
- Hulse, R. A., Taylor, J. H. (1975). "Discovery of a pulsar in a binary system." *Astrophys. J. Lett.* **195**, L51.
- Damour, T., Esposito-Farèse, G. (1992). "Tensor-scalar gravity and binary-pulsar experiments." *Phys. Rev. D* **46**, 4128.
