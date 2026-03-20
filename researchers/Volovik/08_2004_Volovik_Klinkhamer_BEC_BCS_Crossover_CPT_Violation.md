# Quantum Phase Transition for the BEC-BCS Crossover in Condensed Matter Physics and CPT Violation in Elementary Particle Physics

**Author(s):** Frank R. Klinkhamer and Grigory E. Volovik
**Year:** 2004
**Journal:** JETP Letters, 80(6), 343-347
**arXiv:** cond-mat/0407597

---

## Abstract

This paper identifies a remarkable analogy between a quantum phase transition in the BEC-BCS crossover (ultracold Fermi atoms) and CPT symmetry breaking in particle physics. The key results are:

- A quantum phase transition occurs at intermediate coupling strength in the BEC-BCS crossover, separating a fully gapped phase from a phase with topologically protected Fermi points.
- This transition is driven by the splitting of Fermi points: at weak coupling, four Dirac nodes annihilate pairwise; at strong coupling, new nodes appear.
- In the context of particle physics, an analogous Fermi-point splitting could induce CPT violation, neutrino oscillations, and other fundamental symmetry violations.
- The paper suggests that cosmological phase transitions in the early universe might exhibit similar Fermi-point physics, with CPT violation as a residual effect.

The work demonstrates how condensed matter analogs provide laboratories for understanding high-energy symmetry breaking phenomena otherwise inaccessible to direct experiment.

---

## Historical Context

### The BEC-BCS Crossover in Atoms

By 2004, ultracold fermion gases had achieved remarkable experimental control:

- **BCS regime** (weak coupling): Fermi atoms interact weakly; Cooper pairs form at low temperature with coherence length $\xi >> n^{-1/3}$ (dilute pairs).
- **Unitary regime** (intermediate coupling): Scattering length diverges; pair size becomes comparable to interparticle spacing; universal scaling emerges.
- **BEC regime** (strong coupling): Bound molecular states dominate; Bose-Einstein condensation of molecules occurs with coherence length $\xi << n^{-1/3}$.

The transition from BCS to BEC is a **quantum phase transition** — a singular change in ground state properties as a function of the interaction strength parameter (scattering length $a_s$).

### CPT Symmetry in Particle Physics

CPT (charge conjugation, parity inversion, time reversal) is the most fundamental discrete symmetry in the Standard Model. The CPT theorem (Lüders, Pauli, 1954) proves that **any local, Lorentz-invariant quantum field theory must conserve CPT symmetry**.

Violations of CPT would:
- Invalidate the theoretical foundation of particle physics.
- Imply non-locality or Lorentz violation at some scale.
- Have profound implications for baryon asymmetry and baryogenesis.

However, CPT violation in exotic scenarios (string theory, quantum gravity) has been conjectured (Kostelecký et al., SME framework). Direct tests via neutrino masses and oscillations, neutral meson decays, and other precision measurements constrain CPT violation stringently.

The connection to the BEC-BCS crossover was novel and unexpected.

---

## Key Arguments and Derivations

### Part I: Fermi Point Splitting in the BEC-BCS Crossover

#### The BCS Gap Equation

Consider fermions with dispersion $E_k = k^2 / 2m$ and attractive interaction (negative scattering length). The BCS gap equation determines the pairing amplitude $\Delta(T)$:

$$\frac{1}{|g|} = \sum_k \frac{1}{2 E_k^{BCS}}$$

where $E_k^{BCS} = \sqrt{\xi_k^2 + \Delta^2}$ is the quasiparticle energy and $\xi_k = k^2 / 2m - \mu$ is the kinetic energy relative to the chemical potential.

At weak coupling ($|g| \to 0$), the solution is $\Delta \to 0$ exponentially. The Fermi surface is well-defined: quasiparticles with $|\xi_k| < \Delta$ form a gapped region (the "pairing window").

#### Four Dirac Nodes at Weak Coupling

In the BCS regime with **non-s-wave pairing** (p-wave, d-wave, etc.), the gap has nodal structure. For p-wave pairing in an ultracold Fermi gas:

$$\Delta_k = \Delta_0 \, \hat{k}_i \, \sigma^i$$

where $\hat{k}_i = k_i / |\mathbf{k}|$ is the direction of the momentum and $\sigma^i$ are Pauli matrices (spin structure).

The quasiparticle energy is:

$$E(k, \hat{k}) = \sqrt{\xi_k^2 + |\Delta_k|^2}$$

The nodes occur at points where both $\xi_k = 0$ (chemical potential) and $\Delta_k = 0$ (gap vanishes). For p-wave, the gap vanishes at four points on the Fermi sphere (corresponding to the four roots of a cubic equation in solid angle).

These four **Dirac nodes** are topologically protected by discrete symmetries. Each node has chirality $\nu = \pm 1$ (winding number).

#### Transition to Molecular BEC

As coupling strength increases, the individual Fermi points are affected. The transition occurs when the scattering length $a_s$ exceeds a critical value. Experimentally, this is parametrized by:

$$\frac{1}{k_F a_s} = 0$$

where $k_F$ is the Fermi wavevector. The point $1 / (k_F a_s) = 0$ is the **unitary point** (resonance).

In the BEC regime ($1 / (k_F a_s) > 0$), the four Fermi points **split**. Specifically:

- At weak coupling: Four isolated nodes with total winding number $W = 0$ (two with $\nu = +1$, two with $\nu = -1$).
- At intermediate coupling: The nodes approach and interact.
- At strong coupling: New topological structures emerge (e.g., Fermi arcs, reconnected bands).

The **topological invariant changes discontinuously** across the transition, signaling a quantum phase transition.

### Part II: CPT Violation Connection

#### Fermi Point Splitting and Parity Violation

In particle physics, a Fermi point at zero energy represents a **massless fermion state** (like a neutrino or left-handed electron in the electroweak theory).

A **splitting** of a fourfold-degenerate Fermi point corresponds to a **mass splitting** or **mixing** between states with opposite chirality.

In the Standard Model, CPT symmetry relates:
- Particles to antiparticles
- Left-handed to right-handed (via the CPT transformation $\mathbf{p} \to -\mathbf{p}$, along with C and T)

If the four Fermi nodes split asymmetrically, the CPT transformations $C$, $P$, and $T$ may not be symmetries of the low-energy spectrum, implying **CPT violation**.

#### Neutrino Oscillations and Majorana Masses

In the Standard Model, neutrino masses arise from Yukawa couplings to the Higgs. A neutrino mass term breaks the chiral symmetry $L \leftrightarrow R$ and can lead to CP and CPT violation.

If the Fermi-point splitting is driven by a Higgs-like mechanism analogous to the electroweak transition, then:

- The gap structure changes (Fermi points split).
- Chiral symmetry breaks.
- Masses are generated for fermions.
- CPT may be violated in the massive sector.

The Klinkhamer-Volovik model suggests that a condensed matter experiment on the BEC-BCS crossover could **mimic the consequences of CPT violation in particle physics**.

#### Neutrino Oscillation Signatures

CPT violation modifies the neutrino oscillation probability:

$$P(\nu_e \to \nu_\mu) = \sin^2(2\theta) \sin^2\left(\frac{\Delta m^2 L}{4E_\nu}\right) + \Delta_{CPT} \sin(2\theta) \cos(2\theta) \sin\left(\frac{2\Delta m^2 L}{4E_\nu}\right)$$

The CPT-violating term $\Delta_{CPT}$ appears with a different $L$ dependence (linear, not quadratic). Current neutrino experiments (Super-Kamiokande, NOvA, T2K) constrain $|\Delta_{CPT}| < 10^{-3}$ eV$^2$ — setting upper limits on CPT violation strength.

### Part III: Cosmological Implications

#### Phase Transition in the Early Universe

Volovik and Klinkhamer propose that the primordial universe underwent a phase transition analogous to the BEC-BCS crossover:

- At very high temperature (early universe): All fermions are massless (Fermi points, no mixing).
- At intermediate temperature (electroweak scale): The universe undergoes a transition; Fermi points split; masses are generated.
- At low temperature (today): Fully gapped sector; massive fermions and bosons.

The **residual asymmetry** between particles and antiparticles (baryon asymmetry) might be encoded in the Fermi-point splitting structure.

#### Spontaneous CPT Violation Mechanism

If the phase transition in the early universe involved Fermi-point physics, it could generate:

1. **Neutrino masses** (from Fermi-point splitting).
2. **CP violation** (from asymmetric splitting of nodes).
3. **CPT violation** (from chiral asymmetry in the gap structure).
4. **Baryon asymmetry** (from CPT violation in the leptonic sector affecting baryon-number conservation via sphalerons).

This is speculative but provides a concrete condensed matter analog for testing high-energy physics mechanisms.

---

## Key Results

1. **BEC-BCS crossover in p-wave fermions exhibits Fermi-point splitting**: A quantum phase transition separates a phase with four topologically protected nodes from a phase with different nodal structure.

2. **Fermi-point physics can induce CPT violation**: In particle physics language, similar splitting of chiral fermion states would violate CPT symmetry and induce neutrino oscillations.

3. **The transition is characterized by topological invariant change**: The winding number or other topological invariants change discontinuously across the transition, defining the phase boundary.

4. **Cosmological connection**: A phase transition in the early universe with similar Fermi-point physics could explain the origin of fermion masses, CP violation, and CPT violation.

5. **Neutral meson mixing and CPT bounds**: Current constraints on CPT violation from kaon and B meson mixing limit the strength of Fermi-point splitting at the high scale to $< 10^{-3}$ eV$^2$.

---

## Impact and Legacy

This 2004 paper connected two seemingly disparate fields:

- **Ultracold atoms**: The BEC-BCS crossover is now routine in laboratories worldwide (MIT, Innsbruck, JILA, etc.). Fermi-point physics can be studied directly.

- **Neutrino physics**: CPT violation remains an active search area. The paper provided a concrete mechanism linking condensed matter phase transitions to particle physics symmetry breaking.

- **Quantum simulation**: The BEC-BCS crossover became a paradigm for quantum simulation — using one controllable quantum system to simulate another. The CPT violation connection suggested that quantum simulators could test fundamental physics.

- **String theory landscape**: Swampland constraints and CPT violation scenarios in string theory have renewed interest in condensed matter analogs of fundamental symmetry breaking.

---

## Connection to Phonon-Exflation Framework

The BEC-BCS crossover mechanism directly models phonon-exflation's central physics:

1. **K_7 condensate as a p-wave pairing state**: The phonon-exflation BCS condensate on SU(3) is topologically analogous to p-wave superfluid 3He-A. The Cooper pairs carry K_7 charge ±1/2.

2. **Fermi-point splitting = particle mass generation**: In phonon-exflation, the BCS condensate has Fermi points near the gap. As the internal geometry evolves (scale of SU(3) changes), these Fermi points split, generating masses for the phononic excitations.

3. **Topological phase transition at phase boundary**: The framework predicts a sharp transition between the BCS phase (all particles massless) and the BEC phase (particles acquire mass). This is a topological phase transition in the Klinkhamer-Volovik sense.

4. **Chiral structure and baryogenesis**: The K_7 condensate's chiral properties may induce CP and CPT violation, providing a microscopic origin for the baryon asymmetry (as suggested by the Klinkhamer-Volovik mechanism).

5. **Neutrino masses from condensate structure**: Just as CPT violation generates neutrino masses in the Klinkhamer-Volovik model, the phonon-exflation condensate structure determines neutrino mass matrices through the spectral action.

6. **Cosmological evolution as phase transition**: The expansion of the universe corresponds to a changing scale in the internal geometry, driving the system continuously through the BCS-BEC crossover. The observable universe samples a particular phase of this transition.

---

## References

- Klinkhamer, F. R., & Volovik, G. E. (2004). "Quantum phase transition for the BEC-BCS crossover in condensed matter physics and CPT violation in elementary particle physics." *JETP Letters*, 80(6), 343-347. arXiv:cond-mat/0407597.

- Regal, C. A., Greiner, M., & Jin, D. S. (2004). "Observation of resonance condensation of fermionic atom pairs." *Physical Review Letters*, 92(4), 040403.

- Kostelecký, V. A., & Lane, C. D. (2005). "Constraints on Lorentz violation from clock-comparison experiments." *Physical Review D*, 60(11), 116006.

- Horava, P. (2009). "Quantum gravity at a Lifshitz point." *Physical Review D*, 79(8), 084008.
