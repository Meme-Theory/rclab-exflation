# Thermodynamics of Spacetime: The Einstein Equation of State

**Author:** Ted Jacobson
**Year:** 1995
**Journal:** Physical Review Letters, Vol. 75, No. 5, pp. 1260–1263

---

## Abstract

This landmark paper demonstrates that Einstein's field equations—the foundation of general relativity—can be derived from thermodynamic principles rather than postulated as fundamental laws. The key insight: the Einstein equation emerges as an "equation of state" when demanding that the first law of thermodynamics ($\delta Q = T dS$) hold for all local Rindler causal horizons passing through each spacetime point, with entropy proportional to horizon area and temperature given by the Unruh temperature. The derivation reveals a profound connection between gravity and thermodynamics, suggesting that gravitational dynamics may be a collective, statistical phenomenon—emergent rather than fundamental. The paper opens new perspectives on quantum gravity, holography, and the nature of spacetime itself.

---

## Historical Context

Einstein's field equations stand at the foundation of 20th-century physics:

$$G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G T_{\mu\nu}$$

For 80 years, these were understood as fundamental axioms—postulated based on physical intuition (equivalence principle, covariance) but not derived from anything deeper. Several threads converged to prompt Jacobson's investigation:

1. **Hawking radiation (1974)**: Hawking showed that black holes emit radiation with temperature $T_H = \hbar \kappa / (2\pi k_B)$, where $\kappa$ is surface gravity. Coupled with the Bekenstein entropy $S_{\text{BH}} = k_c A / (4 l_p^2)$ (area proportional to entropy), gravity and thermodynamics became intimately linked.

2. **Unruh effect (1976)**: Unruh showed that an accelerated observer detects a thermal bath of particles at temperature $T_U = \hbar a / (2\pi k_B c)$, where $a$ is acceleration. This suggested that temperature is observer-dependent and tied to horizons.

3. **Holographic principle (1990s)**: 't Hooft and Susskind proposed that all physics in a volume can be encoded on its boundary—a radical idea suggesting that gravity is fundamentally lower-dimensional, emergent from boundary data.

4. **Thermodynamic interpretation of gravity (1990s)**: Multiple researchers (Verlinde later, Jacobson here) began exploring whether gravitational dynamics could emerge from thermodynamic constraints rather than be fundamental.

Jacobson's 1995 paper crystallized these ideas into a concrete derivation: Einstein's equation follows inevitably from thermodynamics.

---

## Key Arguments and Derivations

### Rindler Horizons and Thermodynamic Relation

Consider a spacetime point $p$ and an infinitesimal boost in any direction. This defines a local Rindler horizon—a null surface that acts as a causal boundary for an accelerated observer. Every spacetime point is surrounded by a family of such horizons, one for each boost direction.

The fundamental thermodynamic relation is:

$$\delta Q = T dS$$

where:
- $\delta Q$ is heat absorbed
- $T$ is temperature
- $dS$ is entropy change

Jacobson demands this holds for each Rindler horizon. The key identifications are:

1. **Entropy**: Proportional to horizon area,
$$S = \frac{k_B c^3}{4 \hbar G} A$$

where $A$ is the area of a small patch of the horizon near point $p$. This is Bekenstein's formula, derived from black hole thermodynamics.

2. **Temperature**: The Unruh temperature seen by the accelerated observer,
$$T = \frac{\hbar a}{2\pi k_B c}$$

where $a$ is the proper acceleration of the observer.

3. **Heat flux**: Energy crossing the horizon. For a small patch with area $A$, the energy flux is,
$$\delta Q = T^{\mu\nu} \xi_\mu \hat{n}_\nu A$$

where $T^{\mu\nu}$ is the stress-energy tensor, $\xi^\mu$ is the acceleration 4-vector, and $\hat{n}^\mu$ is the horizon's normal.

### Derivation of the Einstein Equation

Requiring the first law $\delta Q = T dS$ to hold at point $p$ for all local Rindler horizons, Jacobson performs a perturbative analysis. To linear order in the horizon's proper acceleration:

$$\delta Q = \int_{\text{small region}} T^{\mu\nu} \xi_\mu \hat{n}_\nu dA$$

The entropy change as the horizon deforms is:

$$dS = \frac{k_B c^3}{4\hbar G} dA$$

where $dA$ is the change in area. For a small deformation of the horizon (changing the acceleration $a$),

$$dA = \mathcal{O}(a^2)$$

Equating $\delta Q = T dS$:

$$\int T^{\mu\nu} \xi_\mu \hat{n}_\nu dA = T \frac{k_B c^3}{4\hbar G} dA$$

Substituting $T = \hbar a / (2\pi k_B c)$:

$$T^{\mu\nu} \xi_\mu \hat{n}_\nu = \frac{\hbar a}{2\pi k_B c} \cdot \frac{k_B c^3}{4\hbar G} \equiv \text{const} \times a$$

Expanding the stress-energy tensor and horizon normal to first order in acceleration, this constraint yields:

$$\xi_\mu = \left( G_\mu^\nu - \frac{1}{2} \delta_\mu^\nu R + \frac{\Lambda}{3} \delta_\mu^\nu \right) T_{\nu\rho} \xi^\rho$$

Contracting with $\xi^\mu$ and using the equivalence principle to set $\xi = (1, 0, 0, 0)$ locally, one obtains:

$$G_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G T_{\mu\nu}$$

This is exactly Einstein's equation. The derivation is remarkably compact: impose the first law at every point for every direction, and out pops the field equation.

### Rindler Horizon as Local Thermodynamic System

The physical picture is as follows: Consider a small patch of spacetime around point $p$, and a local Rindler horizon passing through $p$. The horizon acts as a thermodynamic boundary between the "inside" (causally connected to $p$) and "outside" (beyond the horizon).

Matter and fields have energy that crosses this horizon. From the accelerated observer's perspective, this energy appears as heat flow into a thermal bath at Unruh temperature $T$. The horizon area encodes entropy. By the first law, the energy flow, temperature, and entropy change are related thermodynamically.

If spacetime is to be in "thermodynamic equilibrium" (stable), this relationship must be satisfied. If Einstein's equation is violated at some point, the thermodynamic relation fails, creating a non-equilibrium state. Nature "adjusts" the metric (curvature) to restore thermodynamic balance.

Thus, gravity is the mechanism by which spacetime maintains thermodynamic equilibrium.

### Cosmological Constant as Thermodynamic Parameter

The cosmological constant $\Lambda$ appears in the thermodynamic derivation as a parameter ensuring the first law holds. Its value is not determined by the derivation—it is an additional piece of data. Physically, $\Lambda$ can be thought of as related to the "vacuum energy density":

$$\rho_{\text{vac}} = \frac{\Lambda c^2}{8\pi G}$$

For our universe, observations suggest $\Lambda > 0$ (accelerating expansion). In Jacobson's framework, this corresponds to a positive "thermodynamic pressure" on the vacuum—a non-zero dark energy. The value is a boundary condition, not derived from thermodynamics alone.

### Entropy and Area: Black Hole Thermodynamics

The formula $S = k_c A / (4 l_p^2)$ (Bekenstein entropy) is central to the derivation. This says that a black hole's entropy is proportional to its event horizon area, not its volume—a counterintuitive result. It suggests:

1. **Information is encoded on the surface**: The entire information content of the black hole is encoded on its 2D boundary (the event horizon), not in its 3D interior. This is the holographic principle.

2. **Entropy per unit area is universal**: All black holes have the same entropy density on their horizons: $S/A = k_B c^3 / (4\hbar G)$, independent of the black hole's mass or charge. This universality suggests it is a fundamental constant of nature, not derived from microphysics.

3. **Gravity prevents maximum entropy**: If gravitational curvature violates the first law at some point, entropy would increase unboundedly (second law violation). Spacetime curves to prevent this, enforcing Einstein's equation.

---

## Key Results

1. **Einstein equation derived from thermodynamics**: The Einstein field equations, including the cosmological constant term, are shown to be a direct consequence of requiring the first law of thermodynamics to hold for all local Rindler horizons in spacetime.

2. **Gravity as emergent phenomenon**: The derivation suggests that gravity is not a fundamental force but an emergent statistical effect, analogous to temperature and pressure in gases (which emerge from molecular collisions). Einstein's equation is an "equation of state."

3. **Quantum gravity hint**: If gravity is emergent like thermodynamics, then quantizing the Einstein equation may be inappropriate—just as one does not quantize the hydrodynamic equations for sound waves in air (sound emerges from molecular motion, not vice versa). This suggests that quantum gravity should be a theory of the microscopic degrees of freedom underlying spacetime, not a quantized gravitational field.

4. **Thermodynamic interpretation of black holes confirmed**: Black hole thermodynamics (Hawking radiation, Bekenstein entropy) is not a special property of black holes but a fundamental feature of horizons in any spacetime. Every accelerated observer has a thermal bath and entropy.

5. **Holography and AdS/CFT**: The derivation provides motivation for holographic duality (AdS/CFT), where gravity in a higher-dimensional space emerges from thermodynamics of a lower-dimensional boundary theory.

6. **Entropic gravity concept validated**: The paper opens the door to "entropic gravity"—the idea that gravitational attraction is an entropic force, similar to how osmotic pressure arises from entropy (Brownian motion of particles). Gravity may be fundamentally different in nature from electromagnetism.

---

## Impact and Legacy

Jacobson's 1995 paper has been enormously influential:

1. **Foundational reframe**: It shifted perspectives on gravity from a fundamental force to an emergent phenomenon. This has inspired decades of research on emergent gravity, entropic gravity, and gravity from entanglement.

2. **Holographic principle validation**: The paper provided theoretical support for 't Hooft and Susskind's holographic principle. If Einstein's equation emerges from surface thermodynamics (of the horizon), then 3D gravity emerges from 2D information—a holographic relationship.

3. **AdS/CFT and gauge/gravity duality**: Maldacena's AdS/CFT correspondence (1997, two years after Jacobson) can be understood as a concrete realization of holography. Jacobson's work provided conceptual motivation.

4. **Quantum information and entanglement**: Recent developments (Van Raamsdonk 2010, others) have shown that spacetime entanglement structure encodes the metric. Jacobson's thermodynamic connection to entropy makes this link explicit.

5. **Modified gravity and dark energy**: Alternative theories of gravity (MOND, scalar-tensor theories) can be tested by checking whether they maintain thermodynamic consistency. Jacobson's framework provides a new paradigm for evaluating gravity theories.

6. **Cosmological implications**: The connection between thermodynamics and gravity has implications for early universe cosmology, inflation, and dark energy. Thermodynamic constraints on horizon dynamics limit possible cosmological models.

---

## Connection to Phonon-Exflation Framework

**Relevance: THERMODYNAMIC FOUNDATION FOR 4D EMERGENCE**

Jacobson's thermodynamics-of-spacetime provides the theoretical framework for understanding how 4D gravity emerges from the phonon-exflation geometry:

1. **Spectral action as equation of state**: The spectral action $S_{\text{spec}}[\tau]$ (computed in Sessions 20-24) plays the role of Jacobson's thermodynamic relation. The spectral action is a functional of the Dirac spectrum—the microscopic "information content" of the compactified geometry. The 4D Einstein-Hilbert action emerges from $S_{\text{spec}}$ in the limit of large cutoff, just as thermodynamic macroscopic equations emerge from microscopic statistical mechanics.

2. **Entropy and compactification area**: The K_7 pairing condensate can be assigned an entropy (following Landau/Boltzmann conventions). The condensate entropy is proportional to the "area" of the K_7 Fermi surface (the manifold of paired states). This mirrors Bekenstein's entropy-area relation for black holes. The framework predicts that compactification entropy is encoded on the 3D sphere at the boundary of the SU(3) space.

3. **Unruh temperature and BCS gap**: The BCS gap $\Delta(\tau)$ computed in Sessions 35-38 has dimensions of temperature/energy. In Jacobson's framework, this corresponds to the Unruh temperature $T_U = \hbar a / (2\pi k_B c)$. The analog relationship is:

$$\Delta(\tau) \leftrightarrow T_U \quad \text{(both measure thermal/quantum scales)}$$

The emergence of a gap during the geometric transit is analogous to the emergence of a "horizon temperature" as spacetime becomes curved.

4. **Heat flow and spectral back-reaction**: Jacobson's heat flux $\delta Q = T^{\mu\nu} \xi_\mu \hat{n}_\nu$ represents energy crossing the horizon. In phonon-exflation, the analogous "heat flux" is the energy dissipated during BCS cooling and the spectral action's back-reaction on the metric $\tau$. Sessions 36-38 computed the backreaction magnitude (~3.7%, underdamped). Jacobson's thermodynamic constraint implies this backreaction should maintain a specific relationship to the "horizon temperature" (BCS gap).

5. **First law and geometric evolution**: Jacobson's first law ($\delta Q = T dS$) demands thermodynamic consistency at every spacetime point. Similarly, the framework's geometric evolution equation

$$\frac{d\tau}{dt} = \nabla_\tau \left( \frac{\delta S_{\text{spec}}}{\delta \tau} \right)$$

(Sessions 22-36) enforces consistency between spectral action and metric evolution. Both are expressions of the principle that dynamics maintain thermodynamic balance.

6. **Cosmological constant as dark energy**: Jacobson shows that $\Lambda$ is a thermodynamic parameter related to vacuum pressure. In phonon-exflation, the observed dark energy may be:
   - **Equilibrium contribution**: The cosmological constant arising from the ground state energy of the K_7 condensate (spectral action at minimum)
   - **Non-equilibrium contribution**: Dark energy from the instanton gas (Sessions 37-38), which is a non-equilibrium state with entropy and temperature

This provides a new angle on the cosmological constant problem: is it the equilibrium ground state, or a non-equilibrium relic of the geometric transit?

7. **Information and holography**: Jacobson's insight that information is encoded on horizons (holographic principle) suggests that the 4D physics (SM particles, couplings) is encoded in the topology of the compactification. Sessions 7-17 verified that the K_7 Dirac spectrum contains all SM quantum numbers—a concrete realization of holography at the physics level.

8. **Emergent metric from entropy gradient**: Just as Einstein's equation specifies how $g_{\mu\nu}$ evolves to maintain thermodynamic balance, the framework predicts that the 4D metric emerges from the entropy gradient of the K_7 condensate:

$$G_{\mu\nu}^{\text{4D}} \propto \nabla_\tau S_{\text{BCS}}(\tau)$$

This is a testable prediction: the cosmological evolution (4D Friedmann equations) should be determinable from the BCS entropy landscape (Sessions 35-38 computed this partially; full computation is pending).

**Specific application**: The Jacobson-derived relationship between thermodynamic parameters and gravitational curvature can be inverted: measure the 4D Einstein tensor $G_{\mu\nu}$ (from cosmological observations of expansion rate, curvature, etc.), and read off the thermodynamic "equation of state" of the K_7 compactification. If 4D gravity emerges from K_7 thermodynamics, the SM particle masses and couplings should match this derived equation of state—a quantitative test of the framework (Session 39+).

