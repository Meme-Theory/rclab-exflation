# Superfluid Analogies of Cosmological Phenomena

**Author(s):** G.E. Volovik

**Year:** 2001 (submitted May 21, 2000)

**Journal:** Physics Reports, vol. 351, pp. 195–348

---

## Abstract

Superfluid $^3$He exhibits a rich phenomenology that directly mirrors cosmological and particle physics: Weyl fermions, gauge fields, and gravity emerge as collective modes from the interacting Fermi sea. The superfluid vacuum provides an analog quantum field theory where relativistic properties and symmetries are emergent, not fundamental. Using this framework, the author systematically maps condensed-matter phenomena onto cosmological concepts: vortex defects become cosmic strings, topological defects become instantons, and the superfluid gap structure provides an analogue of the Dirac vacuum. The work demonstrates that quantum field theory can be understood as an effective theory valid in the low-energy corner of a more fundamental, non-relativistic fermionic vacuum. Anomalous processes (axial anomaly, baryon number violation) are reproduced in the superfluid context.

---

## Historical Context

Since Landau's seminal work on the theory of superfluids, it has been understood that collective modes in condensed-matter systems can exhibit exotic properties—superfluidity without vorticity, superfluid circulation quantization, and eventually, the prediction of exotic quasi-particles (spinons, holons, etc.). However, Volovik's insight—that the **entire framework of relativistic quantum field theory** emerges naturally from the low-energy dynamics of a superfluid—was revolutionary.

The conceptual bridge is:
- In a Fermi superfluid at low temperatures, the Dirac equation emerges for quasiparticles near the Fermi surface
- The superfluid gap plays the role of the relativistic mass gap
- Topological defects in the superfluid order parameter (vortices, domain walls) create effective gauge fields and external fields
- The entire structure of general covariance (gravity) can be encoded in the spatial geometry of the pairing state

Volovik's work synthesizes decades of earlier insights (Nambu-Goldstone, symmetry breaking in condensed matter, topological defects) into a coherent picture: **we live in a "superfluid vacuum," and the laws of particle physics are emergent symmetries.**

This has profound implications:
1. Lorentz invariance is not fundamental but emerges at low energy
2. The Planck scale is not a fundamental cutoff but a transition energy where the superfluid picture breaks down
3. Cosmology can be explored in tabletop superfluid experiments
4. Topological defects in the early universe have direct analogues in superfluid vortices

---

## Key Arguments and Derivations

### Fermi Surface Topology and Weyl Points

In a superfluid, the spectrum near the Fermi surface is gapped:

$$E(\mathbf{p}) = \sqrt{\xi(\mathbf{p})^2 + \Delta^2(\mathbf{p})}$$

where $\xi(\mathbf{p}) = p^2/(2m) - \mu$ and $\Delta(\mathbf{p})$ is the gap. For $^3$He-A phase, the gap has an anisotropic $d$-wave-like structure. Near certain points in momentum space (Weyl points), the gap vanishes and the spectrum is linear:

$$E(\mathbf{p}) \approx v_F |\mathbf{p} - \mathbf{p}_W|$$

where $\mathbf{p}_W$ is the Weyl point. The excitations near these points behave like relativistic fermions with velocity $v_F \ll c$ (the actual speed of light in vacuum). This is the **emergence of relativity**: Lorentz invariance at the low-energy scale $\hbar v_F$.

### Topological Stability

The existence of Weyl points is topologically protected. In 3D momentum space, a Weyl point is characterized by a monopole in the Berry phase:

$$\mathcal{C} = \oint_S \mathbf{A}(\mathbf{p}) \cdot d\mathbf{p} = 2\pi n$$

where $\mathbf{A}$ is the Berry connection and $n = \pm 1$ is the monopole charge. This topological protection ensures that Weyl points cannot be gapped by small perturbations—they are **robust** against disorder and interactions.

### Effective Metric from Order Parameter

In $^3$He-A, the pairing order parameter is a vector in both real space and spin space: $\Delta_i(\mathbf{r})$. The spatial structure of this order parameter defines an effective metric:

$$g_{\mu\nu}(\mathbf{r}) = \Delta_i(\mathbf{r}) \Delta^*_i(\mathbf{r}) \delta_{\mu\nu}$$

More generally, for systems with a tensorial order parameter (e.g., $p$-wave pairing), the metric can be nontrivial:

$$g_{\mu\nu} = \partial_\mu \Phi \cdot \partial_\nu \Phi$$

where $\Phi$ parameterizes the order parameter manifold. Quasiparticles move along geodesics of this effective spacetime, experiencing an effective gravitational field.

### Axionic Anomaly and Chern-Simons Action

In a fermionic superfluid with a phase twist $\Phi(\mathbf{r})$ in the order parameter (spontaneous breaking of $U(1)$ symmetry), a non-dissipative circulation is induced:

$$\mathbf{v}_\text{superfluid} = \frac{\hbar}{2m} \nabla \Phi$$

This is the London equation. However, at a topological defect (e.g., a vortex where $\Phi$ winds by $2\pi$), fermions experience an effective Chern-Simons gauge field. The associated anomalous current is:

$$\mathbf{j}_\text{anom} = \frac{e^2}{2\pi \hbar} \mathbf{E} \times \mathbf{B}$$

This is the **axial anomaly** from particle physics, reproduced exactly in the superfluid.

### Baryon Number Violation and Instanton Physics

In the weak-coupling BCS regime, the pairing wavefunction has a definite phase. However, quantum tunneling can cause the phase to slip:

$$\Phi(t) = \Phi_0 + 2\pi n(t)$$

where $n$ changes discretely. This phase slip corresponds to changing the number of Cooper pairs, i.e., **baryon number violation**. The tunneling amplitude is:

$$A \sim \exp(-S_\text{inst})$$

where $S_\text{inst}$ is the instanton action (related to the solitonic vortex energy). In the superfluid context, instantons are vortex-antivortex loops that briefly violate fermion number conservation before annihilating.

### Cosmological Defects as Vortices

A vortex in the superfluid order parameter is a topological defect where the phase winds:

$$\oint_C \nabla \Phi \cdot d\mathbf{l} = 2\pi n_v$$

The vortex core has size $\sim \xi$ (coherence length). A vortex loop (closed curve in 3D space) that contracts to a point undergoes an instanton event, violating fermion number. This is directly analogous to a cosmic string in cosmology: a topological defect whose energy density is concentrated in a line, with a core size and long-range stress.

### Effective Gravitational Action

The entire low-energy effective action can be written as:

$$S = \int d^3r \, \sqrt{|g|} \left[\frac{1}{16\pi G} R + \mathcal{L}_\text{matter}\right]$$

where $g$ is the metric induced by the order parameter and $G$ is an effective Newton's constant related to the microscopic pairing strength. This is Einstein gravity emerging from a fermionic fluid!

---

## Key Results

1. **Weyl Fermions are Emergent** — Linear dispersion and Lorentz invariance arise near Weyl points in the spectrum of superfluid quasiparticles, despite the absence of fundamental relativity.

2. **Topological Protection is Universal** — Berry-phase monopoles protect Weyl points from gap opening, explaining why they persist under perturbations.

3. **Effective Metrics Emerge** — The spatial structure of the order parameter defines an effective spacetime metric for quasiparticles, implementing general covariance.

4. **Anomalies are Reproduced** — The axial anomaly, Chern-Simons coupling, and other QFT anomalies emerge exactly in the superfluid framework.

5. **Baryon Number Violation via Instantons** — Vortex dynamics induce fermion-number-violating transitions with rate controlled by instanton actions.

6. **Cosmic Defects from Vortices** — Vortex loops and networks in superfluids directly parallel cosmic strings and other topological defects in cosmology.

7. **QFT as Effective Theory** — The entire Standard Model structure can be understood as effective low-energy symmetries of a more fundamental superfluid vacuum.

---

## Impact and Legacy

Volovik's work transformed the conceptual landscape of theoretical physics:

- **Quantum Gravity**: His framework provides a concrete model where gravity emerges from a microscopic (non-gravitational) theory—a key challenge in quantum gravity research.
- **Cosmology**: Superfluid analogues allow detailed study of early-universe physics (inflation, defect formation, baryon asymmetry) in the laboratory.
- **Condensed Matter**: The work demonstrated that exotic quantum phenomena (Weyl physics, topological order) are not confined to high-energy physics but are abundant in materials.
- **Philosophy**: The framework challenges the idea that Lorentz invariance and general covariance are fundamental, suggesting they are emergent symmetries like any other.

The work has spawned an entire subfield: "analog gravity" or "tabletop quantum gravity," with experiments on superfluid $^3$He, Bose-Einstein condensates, photonics, and other systems.

---

## Framework Relevance

**Superfluid Vacuum as Analog**: The framework treats spacetime as an emergent collective phenomenon—phononic excitations of a K_7 superfluid pair condensate. Volovik's superfluid-vacuum analogy is the DIRECT TEMPLATE: the framework's phonons ARE the Volovik quasiparticles, the SU(3) geometry induces the effective metric (analogous to order-parameter structure), and cosmological evolution (via tau) parallels defect dynamics in superfluids.

**Weyl Physics and Fold Geometry**: Volovik predicts Weyl fermions near certain points in the Brillouin zone. The framework's fold point (tau ≈ 0.2) is characterized by a van Hove singularity in the Dirac spectrum (Session 35). The generic emergence of Weyl-like physics near singularities connects Volovik's mechanism to the framework.

**Topological Protection of Critical Points**: Volovik shows that topological properties protect zero-energy modes (Weyl points). The framework's fold is topologically critical: it marks a transition between different pairing regimes. The permanence of the post-transit GGE relic (Session 38: exact integrability, never thermalizes) is analogous to Volovik's topological protection.

**Order Parameter and Metric**: In Volovik's framework, the order parameter geometry defines the metric. In the framework, the K_7 pairing tensor and the Jensen deformation on SU(3) jointly define the geometry during transit. The "metric" observed by the Dirac sea is shaped by the pairing dynamics—directly Volovik's picture.

**Instantons as Defects**: Volovik describes vortex loops as instantons (fermion-number-violating tunneling). The framework's instanton gas (Session 38) operates in this regime: pair-tunneling events in the 0D limit, creating permanent non-thermal relics. The analogy is perfect: the framework's instanton physics IS Volovik's vortex-loop physics in the deeply 0D limit.

**Emergence of c from Microscopic Parameters**: Volovik shows that the effective speed of light (velocity near Weyl points) emerges from microscopic scales. The framework predicts that the observed speed of light should match the phonon velocity in the K_7 superfluid fabric (Session 42 prediction: c_phonon = c). Volovik's framework validates this idea.

---

## References

- Volovik, G. E. (2001). Superfluid analogies of cosmological phenomena. *Physics Reports*, 351(4-5), 195-348.
- Volovik, G. E. (2000). Superfluid analogies of cosmological phenomena. arXiv preprint gr-qc/0005091.
- Volovik, G. E. (1987). Superconductivity and superfluidity. In *Exotic Properties of Superfluid* $^3$He. World Scientific.
- Mermin, N. D., & Ho, T. L. (1976). Structure of the order parameter in superfluid* $^3$He. *Physical Review Letters*, 36(11), 594.
