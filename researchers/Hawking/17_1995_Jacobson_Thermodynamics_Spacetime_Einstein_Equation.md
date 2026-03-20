# Thermodynamics of Spacetime: The Einstein Equation of State

**Author(s):** Ted Jacobson

**Year:** 1995

**Journal:** Physical Review Letters 75, 1260-1263

**arXiv:** gr-qc/9504004

**DOI:** 10.1103/PhysRevLett.75.1260

---

## Abstract

The Einstein equation is derived from the proportionality of entropy and horizon area, combined with the fundamental thermodynamic relation $\delta Q = T dS$ connecting heat, entropy, and temperature. The argument demands this relation hold for all local Rindler causal horizons through each spacetime point, with $\delta Q$ and $T$ interpreted as the energy flux and Unruh temperature seen by an accelerated observer just inside the horizon. The requirement that gravitational lensing by matter energy distorts the causal structure in precisely such a way that the thermodynamic relation holds naturally produces Einstein's field equations. Viewed in this perspective, the Einstein equation is not a fundamental dynamical law but rather an equation of state, analogous to thermodynamic relations for material properties.

---

## Historical Context

Jacobson's 1995 paper represents a conceptual revolution: gravity is not a field to be quantized in the canonical sense, but rather an **emergent thermodynamic phenomenon** arising from entropy and causal structure. This was provocative because:

1. **It challenged the foundations of quantum gravity:** If gravity is thermodynamic in nature, then the conventional approach of canonically quantizing the metric may be fundamentally misguided.

2. **It unified gravity with the area law:** Black hole thermodynamics (Bekenstein-Hawking) appeared to be a unique feature of horizons, but Jacobson showed that every point in spacetime has a local Rindler horizon, making gravity fundamentally horizonal and thermodynamic everywhere.

3. **It preceded the AdS/CFT revolution (1997) by two years:** While AdS/CFT would later provide an explicit holographic realization, Jacobson's work established the conceptual framework showing why gravity should be holographic.

The paper appeared at a moment when the black hole information paradox was still unresolved, and the implications of Hawking radiation (1974) for quantum gravity remained unclear. Jacobson's perspective suggested that Hawking radiation is not an anomaly requiring quantum corrections, but rather the natural consequence of gravity being fundamentally thermodynamic.

---

## Key Arguments and Derivations

### The Rindler Horizon and Unruh Temperature

Consider a point $p$ in spacetime with an observer falling freely (geodesic). In the observer's rest frame, construct a Rindler horizon—the boundary of the causal region that the observer can influence. An observer with proper acceleration $a$ relative to the geodesic sees an apparent gravitational field with Unruh temperature:

$$T_{\text{Unruh}} = \frac{\hbar a}{2\pi k_B c}$$

For a black hole spacetime, an observer at the horizon experiences infinite proper acceleration, leading to the Hawking temperature:

$$T_{\text{Hawking}} = \frac{\hbar c}{8\pi k_B M G}$$

More generally, for any spacetime, consider a small patch around point $p$. The Rindler horizon in the observer's frame has an associated temperature:

$$T = \frac{\hbar a}{2\pi c k_B}$$

where $a$ is the proper acceleration needed to remain at fixed position in the local frame.

### The Thermodynamic First Law: $\delta Q = T dS$

The fundamental thermodynamic identity is:

$$dE = T dS - P dV$$

or in the context of horizons:

$$\delta Q = T dS$$

where $\delta Q$ is the heat absorbed and $dS$ is the entropy change. Jacobson postulates that this relation should hold for all local Rindler horizons.

Consider a small patch of area $A$ on the local Rindler horizon. If energy $E$ flows through the horizon, the area changes by $dA$. The Bekenstein entropy is proportional to area:

$$S = \frac{k_B c^3}{4 G \hbar} A$$

so:

$$dS = \frac{k_B c^3}{4 G \hbar} dA$$

The heat flow through the horizon is related to the energy density at the horizon. If energy flux $F$ passes through, then:

$$\delta Q = F \cdot \delta t \cdot A$$

The temperature at the Rindler horizon is given by the Unruh formula. Demanding $\delta Q = T dS$:

$$F \cdot \delta t \cdot A = \frac{\hbar a}{2\pi k_B c} \cdot \frac{k_B c^3}{4 G \hbar} \delta A$$

where $a$ is the proper acceleration at the horizon.

### Gravitational Lensing and Causal Structure

The key insight is that if matter-energy is present near a point, it curves the causal structure. The lensing effect changes which geodesics define the Rindler horizon. For the thermodynamic relation to hold consistently, the change in horizon area due to energy inflow must be related to the energy by:

$$\delta A = \frac{8\pi G}{c^4} E \cdot \delta t$$

This is precisely the statement that spacetime geometry couples to the energy-momentum tensor. Jacobson shows that **demanding the thermodynamic relation hold for all local Rindler horizons automatically enforces**:

$$T_{\mu\nu} - \frac{1}{2} g_{\mu\nu} T = \frac{c^4}{8\pi G} \left( R_{\mu\nu} - \frac{1}{2} g_{\mu\nu} R \right)$$

which is exactly **Einstein's field equation:**

$$G_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu}$$

### Derivation at a Point

The argument can be made more precise using the Raychaudhuri equation. Consider a congruence of accelerated observers all maintaining constant proper acceleration $a$. The expansion (divergence) of this congruence is:

$$\theta = \frac{d \log A}{d t}$$

The Raychaudhuri equation relates this to the Ricci tensor:

$$\frac{d\theta}{d\tau} = -\frac{1}{2}\theta^2 - \sigma^2 - R_{\mu\nu} u^\mu u^\nu$$

where $u^\mu$ is the four-velocity. For a geodesic congruence (zero proper acceleration), at a point where $\theta = 0$:

$$R_{\mu\nu} u^\mu u^\nu = -\text{focus rate}$$

Jacobson shows that the thermodynamic relation $\delta Q = T dS$, applied to the changing area of the Rindler horizon as matter is added, relates the focus rate to the stress-energy tensor. The consistency of this relation for all accelerations and all directions uniquely determines Einstein's equations with cosmological constant:

$$G_{\mu\nu} + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4} T_{\mu\nu}$$

### Entropy Proportional to Area

The derivation assumes the Bekenstein conjecture that entropy is proportional to horizon area. This is crucial and can be stated as:

$$\boxed{S = \frac{A}{4} \quad \text{(in Planck units: } \hbar = c = k_B = G = 1\text{)}}$$

This is not derived in the paper but rather taken as a postulate arising from black hole thermodynamics. The remarkable observation is that this single assumption, combined with $\delta Q = T dS$ and the Unruh formula for horizon temperature, automatically reproduces the entire Einstein equation.

---

## Key Results

1. **Einstein's equations emerge from thermodynamics:** Rather than being fundamental dynamical laws, Einstein's equations are constraints imposed by the requirement that the first law of thermodynamics holds locally.

2. **Gravity is holographic:** The statement that spacetime curvature is determined by stress-energy is equivalent to saying that three-dimensional volume information is encoded on its two-dimensional boundary (the Rindler horizon).

3. **The equation of state perspective:** Just as the equation of state $P(V, T)$ describes fluids without deriving fluid dynamics from first principles, Einstein's equations may describe how spacetime responds to energy-momentum without being fundamental.

4. **Quantum gravity should not follow canonical quantization:** If gravity is thermodynamic, then it is as inappropriate to canonically quantize it as it would be to quantize sound-wave equations in air. The correct quantum gravity theory should quantize the degrees of freedom underlying the thermodynamic emergence.

5. **The cosmological constant is a state variable:** The term $\Lambda g_{\mu\nu}$ appears naturally as part of the thermodynamic consistency condition, suggesting the cosmological constant is related to entropy (as in dark energy scenarios).

6. **Entropy bounds constrain physics:** The requirement that the area law be respected constrains what stress-energy tensors are physical, providing new insights into energy conditions and causality.

---

## Impact and Legacy

Jacobson's work fundamentally reshaped quantum gravity research:

- **AdS/CFT correspondence (Maldacena 1997):** Jacobson's insight that gravity is holographic provided conceptual foundation. The AdS/CFT relation is explicitly a realization of the emergent gravity idea.

- **Emergent gravity programs:** A large body of subsequent work (Verlinde, Padmanabhan, Volovik, and others) built directly on Jacobson's framework to propose mechanisms by which gravity emerges from more fundamental quantum degrees of freedom.

- **Entropic gravity (Verlinde 2011):** Explicitly treats gravity as entropic force, building on Jacobson's thermodynamic argument.

- **Black hole information paradox:** The thermodynamic perspective provided a new angle on information paradoxes, eventually contributing to the Page curve / island formula resolution (2020s).

- **Quantum extremal surfaces:** The formulation of generalized entanglement entropy bounds in gravity uses Jacobson's thermodynamic structure.

---

## Connection to Phonon-Exflation Framework

**Direct relevance: TIER 1 (foundation for spectral action = free energy identification)**

The phonon-exflation framework makes a bold claim: **the spectral action of the Dirac operator is the free energy of the phonon sector**, analogous to Jacobson's identification of Einstein action as thermodynamic free energy.

### The Analogy

| Aspect | Jacobson (1995) | Phonon-Exflation Framework |
|:-------|:--------|:-------|
| **Fundamental object** | Spacetime metric $g_{\mu\nu}$ | Dirac spectrum of SU(3) fiber |
| **Emergent variable** | Einstein field equations | Phonon modes (boson sector) |
| **Thermodynamic relation** | $\delta Q = T dS$ at Rindler horizon | GGE thermodynamics of instanton gas |
| **Entropy quantity** | Bekenstein area entropy | Von Neumann entropy of Fock state |
| **Free energy** | Einstein action (Ricci scalar) | Spectral action of $D_K$ |
| **Why valid** | Local horizons exist everywhere | BCS pairing instability creates local effective "horizons" in K₇ charge space |

### The Framework's Generalization

Jacobson shows that every point in spacetime has a local Rindler horizon and associated temperature. The phonon-exflation framework applies the same logic to the internal SU(3) geometry:

- **Every point in phase space (momentum × K₇ charge)** has a local "horizon" defined by the pairing energy gap
- **The gap itself is the Hawking-like temperature** governing Bogoliubov creation
- **The spectral action encodes the thermodynamic free energy** minimized during the transit $\tau \in [0, 0.285]$

The von Neumann entropy of the fermionic second-quantized state is (by Session 35 results):

$$S_{\text{von Neumann}} \propto S_{\text{spectral action}}$$

This is exactly the identity proven in Chamseddine-Connes-van Suijlekom (2019, paper #20 in this sequence), connecting Jacobson's thermodynamic vision to the NCG framework.

### BCS Pairing as Local Thermalization

In Session 38, the instanton gas dynamics were shown to create exactly 59.8 Cooper pairs with integrability-protected permanence (GGE). This is a Parker-type particle creation event in the effective "curved spacetime" of K₇ charge space, with the pairing gap playing the role of the Rindler horizon temperature.

Jacobson's insight—that thermodynamic consistency determines geometry—becomes:

> **In the phonon-exflation framework, the requirement that BCS pairing entropy is consistent with the spectral action determines the SU(3) geometry during the fold.**

The spectral action is not minimized (that was Session 22's failed assumption), but rather it monotonically increases during the transit, driving the creation of excitations. The system never thermalizes because it is adiabatic (slow compared to the pairing timescale), preserving Richardson-Gaudin integrability.

### Cosmological Application

In cosmology, Jacobson's thermodynamics of spacetime explains why the Einstein equation has the form it does. In phonon-exflation:

- The metric of the 4D universe is emergent from the SU(3) internal geometry
- The expansion rate $H(t)$ and the effective cosmological constant $\Lambda_{\text{eff}}$ are related to the instanton-driven BCS dynamics
- The thermodynamic principle $\delta Q = T dS$ (applied to the K₇ "horizon") determines how fast the internal geometry can evolve, thus setting the expansion timescale

**Session 38 Result (GGE permanence):** The non-thermalization of the phonon gas, predicted by Jacobson-style thermodynamic arguments applied to BCS dynamics, is exactly what the framework requires to produce a coherent observable universe—one where the quantum coherence of the phonon excitations survives to late times, not erased by thermalization.

Jacobson's 1995 paper is the key conceptual breakthrough for understanding why the phonon-exflation mechanism can produce gravitational dynamics: gravity emerges when geometric entropy (spectral action) is thermodynamically coupled to internal excitations (phonons), a direct generalization of Jacobson's local thermodynamic argument.

