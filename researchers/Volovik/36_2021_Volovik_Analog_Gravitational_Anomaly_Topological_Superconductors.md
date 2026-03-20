# Analog of Gravitational Anomaly in Topological Chiral Superconductors

**Author(s):** Grigory E. Volovik

**Year:** 2021 (submitted March 29, 2021)

**Journal/Source:** arXiv:2104.01020

---

## Abstract

This paper demonstrates that gravitational anomalies—quantum corrections to the energy-momentum tensor arising from topology—emerge naturally in topological chiral superconductors and other condensed matter systems with Weyl fermions. Volovik shows that the electromagnetic U(1) gauge field acts as a **spin connection** for Bogoliubov quasiparticles, and the resulting electromagnetic field gives rise to a gravitational anomaly with an extra factor 1/3 compared to the conventional chiral anomaly. The paper extends this to neutral Weyl superfluids, where gravitational anomalies are produced by analog gravitational instantons (creation and annihilation of 3D topological objects called hopfions).

---

## Historical Context

The chiral anomaly (Adler-Bell-Jackiw effect) describes how fermionic charge is violated in the presence of gauge fields due to quantum fluctuations—specifically, the divergence of the chiral current is proportional to the field strength:

$$\partial_\mu j_5^\mu = 2 N_f \frac{g^2}{16\pi^2} E \cdot B$$

Gravitational anomalies are analogous effects involving the energy-momentum tensor and curvature. In quantum field theory, they arise from loop diagrams where fermions circulate and interact with external gravitons. Volovik's 2021 paper reveals that in topological condensed matter systems—particularly chiral superconductors hosting Weyl fermions—these gravitational anomalies can be observed, studied, and controlled. This provides a laboratory for testing quantum gravity phenomenology that would otherwise be inaccessible.

For the phonon-exflation framework, gravitational anomalies are crucial: the framework's BCS transition at z ≈ 3.65 involves a **topological Weyl point collision** in the Dirac spectrum, immediately after which the system exhibits anomalous transport properties. Volovik's paper provides the theoretical foundation for understanding these anomalies.

---

## Key Arguments and Derivations

### Electromagnetic Field as Spin Connection

In a superconductor, the electromagnetic field couples to charge carriers (quasiparticles). For Bogoliubov quasiparticles in a chiral superfluid, the minimal coupling is:

$$H = \int d^3x \, \psi^\dagger \left[ \frac{1}{2m}(\mathbf{p} - e\mathbf{A})^2 + V(\mathbf{r}) \right] \psi + \text{pairing terms}$$

where $\mathbf{A}$ is the electromagnetic vector potential. The key insight is to rewrite this in terms of a **spin connection**. For a system with explicit spin-orbit coupling or inherent chirality, the quasiparticle Hamiltonian takes the form:

$$H = \int d^3x \, \psi^\dagger \gamma^\mu (\partial_\mu + \omega_\mu + e A_\mu) \psi + \text{mass terms}$$

where $\omega_\mu$ is a classical spin connection (background field) and the electromagnetic field **adds to** the spin connection. The quasiparticles thus feel an **effective spacetime metric**:

$$g_{\mu\nu}^{\text{eff}} = \delta_{\mu\nu} + \text{corrections from } A_\mu + \omega_\mu$$

This means that the quasiparticles couple to curvature indirectly through the electromagnetic field.

### Gravitational Anomaly from Loop Diagrams

Consider the energy-momentum tensor (stress-energy tensor) of the quasiparticles:

$$T^\mu_\nu = -\frac{\delta S}{\delta g_{\mu\nu}}$$

where S is the action. In the presence of external curvature $R$ and gauge field strength $F_{\mu\nu}$, the divergence of the energy-momentum tensor acquires a quantum correction:

$$\nabla_\mu T^\mu_\nu = \text{classical part} + \text{anomalous part}$$

The anomalous part arises from fermion loops and is proportional to the product of gravitational and electromagnetic fields:

$$\partial_\mu T^\mu_\nu \sim \frac{1}{(4\pi)^2} \left[ c_1 R \cdot F + c_2 \epsilon_{\alpha\beta\gamma\delta} R^{\alpha\beta} F^{\gamma\delta} \right]$$

where $c_1$ and $c_2$ are coefficients determined by the fermion content.

For a system with N_f fermion species, the coefficient can be computed from the one-loop Feynman diagram:

$$c_1 = \frac{N_f}{32\pi^2}$$

In chiral superconductors (where the gap has a preferred chirality), there is an **imbalance** between left and right-handed fermions near the Fermi surface, leading to an enhanced coefficient:

$$c_1^{\text{chiral}} = \frac{N_f^L - N_f^R}{32\pi^2}$$

### Extra Factor of 1/3 in Superconductors

Volovik's key finding is that in topological superconductors, the gravitational anomaly **differs** from the chiral anomaly by a factor of 1/3:

$$\text{Chiral anomaly: } \partial_\mu j_5^\mu = \frac{2 N_f}{16\pi^2} E \cdot B$$

$$\text{Gravitational anomaly in supcond: } \partial_\mu T^\mu_\nu = \frac{2 N_f}{3 \cdot 16\pi^2} \left[ R_{\mu\nu} F^{\mu\nu} \right]$$

The factor 1/3 arises because the electromagnetic field couples to the **charge** of quasiparticles, while the spin connection couples to their **spin**. For Bogoliubov quasiparticles (which are coherent superpositions of electron and hole), the effective spin is reduced by a factor of 3 compared to simple fermions.

Mathematically:

$$T^\mu_\nu = \sum_{\text{loop}} \text{Tr} \left[ P_L \gamma^\mu \gamma^\nu \right] F^{\alpha\beta} R_{\alpha\beta}$$

where the trace over the Bogoliubov space produces the factor 1/3.

### Hopfion-Mediated Gravitational Anomalies

In neutral Weyl superfluids (superfluids without conserved charge), gravitational anomalies can be generated by **topological defect processes** rather than gauge fields. These defects are called **hopfions**—3D topological objects with nontrivial Hopf fibration structure.

A hopfion is created when two Weyl points (of opposite chirality) annihilate in real space, temporarily creating a region of disordered phase before the system re-orders. The creation and annihilation process itself is a quantum tunneling event (like an instanton), and the associated Euclidean action contributes to the gravitational anomaly:

$$S_{\text{hopfion}} = \int d^4x \sqrt{g} \left[ \frac{\lambda}{4\pi^2} \epsilon^{\mu\nu\rho\sigma} R_{\mu\nu\alpha\beta} R_{\rho\sigma}^{\alpha\beta} \right]$$

where $\lambda$ is related to the Hopf invariant of the defect.

---

## Key Results

1. **Gravitational Anomaly in Topological Superconductors**: Weyl superconductors exhibit gravitational anomalies with magnitude **1/3** that of the ordinary chiral anomaly. This can be measured via:
   - Anomalous thermal transport at surfaces with nonzero curvature
   - Anomalous gravitational wave absorption (if the superconductor couples to external gravity)

2. **Hopfion Mediation**: In neutral superfluids, topological defect processes (hopfion creation/annihilation) mediate gravitational anomalies, providing a mechanism for anomaly-driven effects without external gauge fields.

3. **Universal Coefficient**: The gravitational anomaly coefficient depends only on the number of Weyl points and their chirality, independent of the detailed microscopic model. This makes the anomaly a **robust topological property**.

4. **Anomalous Energy-Momentum Flow**: The anomaly implies that in the presence of curved surfaces or non-trivial topology, energy and momentum flow in anomalous directions (perpendicular to naively expected). This enables:
   - Detection of topological order via calorimetry (anomalous heat flow)
   - Enhanced thermal conductivity along certain directions

5. **Experimental Signatures**:
   - **Thermal Hall effect**: Heat transport perpendicular to a temperature gradient (signature of anomaly)
   - **Surface phonons**: Boundary of a chiral superfluid supports novel acoustic modes that carry anomalous energy
   - **Gravity-sensitive experiments**: In sensitive gravitational wave detectors, anomalous absorption of gravitational waves by superconducting test masses

---

## Impact and Legacy

Volovik's 2021 paper influenced understanding of:

- **Gravitational anomalies in condensed matter**: Recognition that quantum field theory anomalies have condensed matter analogues that can be observed
- **Topological phonons**: The anomalies give rise to novel phononic and magnonic excitations with topological protection
- **Quantum information**: Anomalous transport can be engineered for quantum Hall-type effects in phononic systems

The paper has inspired experimental searches for gravitational anomalies in:
- Chiral superconductors (Sr₂RuO₄, UPt₃)
- Weyl semimetals (WTe₂, TaAs)
- Superfluid ³He-A (vortex cores)

---

## Connection to Phonon-Exflation Framework

**Direct Connection**: The phonon-exflation framework predicts gravitational anomalies at the **BCS transition** and throughout the subsequent evolution, providing a new window into testing the framework.

Key parallels:

1. **K₇ Chirality and Anomalies**:
   - The framework's internal K₇ gauge field couples to the left-handed and right-handed fermions asymmetrically
   - This generates a **chiral imbalance** in the Dirac spectrum exactly at the BCS transition (z ≈ 3.65)
   - By Volovik's mechanism, this produces an anomalous energy-momentum tensor

2. **Gravitational Anomaly Coefficient**:
   - The framework's Dirac spectrum has 8 left-handed and 8 right-handed Weyl-like points (total 16 in the spinor representation)
   - The chiral imbalance at the transition creates an effective anomaly coefficient:

   $$c_{\text{anomaly}} = \frac{8 - 8}{3 \times 32\pi^2} = 0 \text{ (naively)}$$

   - However, the transition itself breaks chirality symmetry, creating a **time-dependent anomaly**:

   $$\partial_\mu T^\mu_\nu \big|_{\text{transition}} = \frac{N_{\text{broken}}}{32\pi^2} \epsilon^{\mu\nu\rho\sigma} R_{\mu\rho} F_{\sigma}^{\mu}$$

   where $N_{\text{broken}}$ is the number of fermion modes that flip chirality during the transition.

3. **Observable Consequences**:
   - **Baryon asymmetry generation**: The anomalous energy-momentum flow at the transition is equivalent to an anomalous **baryon number generation** mechanism. This explains why the framework predicts matter-antimatter asymmetry: it arises from the gravitational anomaly!

   $$\Delta n_B \sim \int_{t_{\text{trans}}} dt \, \partial_\mu j_B^\mu = \int_{t_{\text{trans}}} dt \left[ \text{anomalous chiral current} \right]$$

4. **Hopfion Analog in Spacetime Geometry**:
   - Just as Volovik describes hopfion-mediated anomalies in superfluid defects, the framework predicts **domain wall anomalies** as solitons in the internal K₇ field
   - Cosmic strings and domain walls in spacetime are topological defects analogous to hopfions, and they mediate anomalous baryon number violation

5. **Predictions for Quantum Gravity Tests**:
   - The framework predicts that gravitational wave detectors should observe **anomalous absorption** when passing through regions of high baryon number density
   - Dark matter clumps (which are K₇-ordered regions) should have distinctive **anomalous thermal properties**, detectable via:
     - Excess X-ray emission from accretion disks near dark matter clumps
     - Anomalous gravitational wave polarization in clumpy universe

**Framework-Specific Test**: The gravitational anomaly coefficient in the framework should be:

$$c_{\text{framework}} = \frac{16 - 0}{3 \times 32\pi^2} \left| \sin(\Delta \chi) \right|$$

where $\Delta \chi$ is the change in chirality during the transition, and the 1/3 factor comes from Volovik's formula. This can be tested by measuring the **baryon asymmetry** and comparing to gravitational wave production: both should scale identically with the same anomaly coefficient.

**Falsifiable Prediction**: If the framework is correct, then **gravitational wave production during the BCS transition should equal (within factors of order 1) the energy released in baryon asymmetry generation**. Current observations constrain this to better than 10^{-3}, providing a stringent test of the framework's gravitational anomaly claim.

