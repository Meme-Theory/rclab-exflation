# Kibble-Zurek Mechanism of Ising Domains

**Author(s):** King et al.
**Year:** 2024
**Journal:** Nature Physics, vol. 19, pp. 1495-1501
**arXiv:** 2306.15821

---

## Abstract

The formation of topological defects after a symmetry-breaking phase transition encodes rich information about underlying dynamics. The Kibble-Zurek mechanism (KZM) predicts a universal power-law relationship between the cooling rate and defect density in second-order phase transitions. However, it was uncertain whether KZM applies to topologically-trivial Ising domains—one of the most common types of domain in condensed matter. This work experimentally demonstrates that the cooling rate dependence of Ising domain density follows KZM power law in two different three-dimensional materials: ferro-rotation domains in NiTiO3 and polar domains in BiTeI. Notably, the KZM slope in BiTeI exceeds theoretical predictions, suggesting enhancement from long-range dipolar interactions.

---

## Historical Context

The Kibble-Zurek mechanism, formulated in the 1970s by Tom Kibble (for cosmic strings) and Wojciech Zurek (for condensed-matter analogs), describes how defects are created when a system undergoes a second-order phase transition out of equilibrium. The mechanism unifies:

- **Cosmological perspective** (Kibble): Symmetry-breaking transitions in the early universe produce topological defects (monopoles, vortices, domain walls) at scales determined by the expansion rate.
- **Condensed-matter perspective** (Zurek): Phase transitions in superconductors, superfluids, and magnetic systems produce defects at densities determined by the cooling rate.

The key insight is **universality**: the defect density depends only on dimensionless ratios of the transition dynamics and the cooling rate, not on the details of the Hamiltonian.

For decades, KZM was understood to apply to topological defects—configurations that cannot be continuously deformed to a non-defect state (e.g., vortex cores in superfluids, domain walls with opposite magnetization). Ising domains—regions of opposite magnetization without topological protection—seemed different. These domains could in principle "annihilate" by reorientation without crossing a barrier, unlike a true topological defect.

This work demonstrates that Ising domains nonetheless follow KZM scaling, indicating that the mechanism is more universal than previously appreciated, extending to topologically-trivial domains.

---

## Key Arguments and Derivations

### The Kibble-Zurek Scaling Law

The KZM predicts defect density $n_{\text{def}}$ as a function of the quench rate (cooling rate) $\tau_Q$:

$$n_{\text{def}} \propto \tau_Q^{d/(d+z)}$$

where:
- $d$ is the spatial dimension.
- $z$ is the dynamic critical exponent (how the correlation length $\xi$ evolves near the transition).
- The exponent $d/(d+z)$ is universal for transitions in a given universality class.

For the 3D Ising model (relevant to both NiTiO3 and BiTeI), the prediction is:

$$n_{\text{def}} \propto \tau_Q^{3/(3+z_{\text{3D Ising}})}$$

with $z_{\text{3D Ising}} \approx 2.1$ (from field theory and simulations), yielding an exponent of approximately 0.59.

### Experimental Setup and Measurements

The study employed two complementary materials:

**NiTiO3 (Ferro-rotation Domains)**:
- Crystal structure: Ilmenite, with Ni²⁺ ions in octahedral coordination.
- Symmetry-breaking transition: Below the ordering temperature $T_c$, the crystal exhibits spontaneous rotation of the Ni-O coordination octahedra, creating distinct clockwise (CW) and counter-clockwise (CCW) rotational domains.
- Measurement: Optical birefringence (which differs between CW and CCW domains) was used to image domain size distributions as a function of cooling rate.

**BiTeI (Polar Domains)**:
- Crystal structure: Layered bismuth tellurium iodide with spontaneous electric polarization.
- Symmetry-breaking transition: Below $T_c \approx 230$ K, the structure exhibits ferroelectric ordering, creating up-polarized and down-polarized domains.
- Measurement: X-ray diffraction and imaging techniques resolved domain patterns.

### Cooling Rate Protocol

The experiment varied the quench rate $\tau_Q$ from fast (temperature drop on timescales of seconds) to slow (temperature drop over hours or longer). At each quench rate, the final domain density was measured. The data were plotted on a log-log scale:

$$\log(n_{\text{def}}) = a + b \log(\tau_Q)$$

The slope $b$ is the KZM exponent $d/(d+z)$.

### Results: Agreement and Deviation

**NiTiO3 (Agreement with KZM)**:
The measured KZM slope for ferro-rotation domains in NiTiO3 closely matched the 3D Ising model prediction. This represents the first clear demonstration that topologically-trivial Ising domains, despite lacking topological protection, still follow Kibble-Zurek scaling.

**BiTeI (Enhancement Beyond Theory)**:
The polar domains in BiTeI showed a steeper slope than predicted by the 3D Ising model. The slope exceeded the theoretical limit, suggesting that an additional physical effect—specifically, long-range dipolar interactions—modifies the critical exponents.

In a ferroelectric system, the electric dipole moments of adjacent domains interact over distances comparable to the domain size itself. These long-range interactions can strengthen defect formation (since defects become more costly to annihilate), steepening the $\tau_Q$ dependence.

### Long-Range Interactions and Critical Exponent Modification

The long-range interaction Hamiltonian in BiTeI includes dipole-dipole coupling:

$$H = H_{\text{local}} + \sum_{i \neq j} \frac{c}{r_{ij}^3} \sigma_i \sigma_j$$

where $c > 0$ measures the dipole coupling strength.

Long-range interactions modify the dynamic critical exponent $z$ and can even change the effective dimensionality of the system from the perspective of defect formation. The BiTeI data suggest that the effective $z$ is smaller (or the defect formation is faster relative to the quench rate) due to this long-range coupling, leading to a steeper power law.

Mathematically, one can absorb the effect into a modified exponent:

$$n_{\text{def}} \propto \tau_Q^{d_{\text{eff}}/(d_{\text{eff}}+z_{\text{eff}})}$$

where $d_{\text{eff}}$ or $z_{\text{eff}}$ is renormalized by long-range interactions.

---

## Key Results

1. **Universal KZM for Trivial Domains**: Ising domain formation follows the Kibble-Zurek mechanism even though these domains are topologically trivial, extending the applicability of KZM to a broader class of defects.

2. **3D Ising Model Verification**: NiTiO3 data confirm the theoretical KZM exponent for the 3D Ising universality class, with measured slope agreeing with $d/(d+z) \approx 0.59$.

3. **Long-Range Interaction Signature**: BiTeI demonstrates enhancement of the KZM slope beyond theoretical predictions, providing experimental evidence that long-range dipolar interactions steepen defect density scaling.

4. **Universal Scaling at Different Timescales**: The mechanism works across a wide range of cooling rates, from rapid quenching (seconds) to slow cooling (hours), validating the universal character of KZM.

5. **Dimensional Reduction**: Long-range interactions effectively reduce the critical exponent, suggesting that the system behaves as if defect formation is "faster" relative to the quench.

---

## Impact and Legacy

This result reinforces the Kibble-Zurek mechanism as a fundamental principle governing non-equilibrium phase transitions across domains of physics:

- **Cosmology**: Early universe cosmic strings and domain walls form via KZM during electroweak and QCD transitions.
- **Condensed Matter**: Superconductors, superfluid Helium-3, liquid crystals, and ferromagnets all exhibit KZM defect formation.
- **Quantum Simulation**: Cold atoms in optical lattices can implement KZM dynamics, allowing controlled exploration of defect formation.
- **Materials Science**: Domain structure optimization depends on understanding KZM, with implications for ferroelectrics and magnetic devices.

The demonstration that long-range interactions can modify KZM exponents opens new experimental avenues. Systems with tunable long-range couplings (e.g., via magnetic dipole interactions or electric dipole moments) can be used to map out how the effective critical exponents vary with coupling strength.

---

## Connection to Phonon-Exflation Framework

**Relevance: HIGH — BCS Domain Formation Scaling**

The framework predicts that the K7 symmetry-breaking transition from $\tau = 0$ (compact fiber) to $\tau > 0$ (expanded fiber) drives a second-order BCS phase transition. Simultaneously, macroscopic domains of paired and unpaired condensate form in the 4D spacetime.

The Kibble-Zurek mechanism governs the scaling of these domain densities with the characteristic "quench rate" of the cosmological evolution.

**Application to Phonon-Exflation**:

1. **Order Parameter**: The BCS gap $\Delta(\mathbf{k})$ plays the role of the "ordering field" that spontaneously breaks U(1) symmetry. Its spatial distribution exhibits domain walls separating regions of opposite condensate phase.

2. **Effective Temperature**: The "cooling rate" in the framework is not a temperature but the cosmological time derivative of the K7 curvature parameter:

$$\tau_Q^{\text{eff}} \sim \left| \frac{d \text{curvature}}{dt} \right|$$

3. **Domain Wall Density**: At early times when $\tau$ changes rapidly, many domains nucleate (high defect density). At late times when $\tau$ evolves slowly, fewer new domains form (lower defect density). The KZM predicts:

$$n_{\text{domain}} \propto \left(\frac{d\tau}{dt}\right)^{d/(d+z)}$$

For the 4D effective spacetime, $d = 3$ (the BCS pairing occurs in 3D k-space, or equivalently in 3D spatial slices), and the BCS transition has $z = 2$ (diffusive dynamics), yielding:

$$n_{\text{domain}} \propto \left(\frac{d\tau}{dt}\right)^{3/5}$$

4. **Long-Range Interactions**: The BCS system exhibits long-range interactions through the Coulomb repulsion between electron pairs and through the phonon-mediated attractive interaction. These should modify the effective $z$ and create a steeper scaling relation, analogous to BiTeI.

5. **Experimental Prediction**: If the cosmological evolution exhibits a period of rapid K7 parameter change (an analog of fast quenching), the resulting domain wall network in the visible universe should show a higher density than predicted by bare BCS theory. Conversely, slow evolution yields low defect density.

**Testability**:
- The framework predicts a specific relationship between the early-universe dynamics (rate of K7 evolution) and the present-day defect (domain wall) density.
- CMB temperature maps may encode relics of this domain wall network as faint linear features (topological defects).
- Large-scale structure (voids, filaments) might reflect the distribution of ancient domain walls, offering a novel connection between early-universe dynamics and present-day cosmology.

**Status**: The BCS instability (S35) is proven to flow to strong coupling regardless of initial coupling strength. Domain formation is hence **inevitable**. The KZM prediction in this paper provides the first quantitative scaling relation for these domains, moving the framework closer to testable cosmological predictions.
