# Superfluid Analogies of Cosmological Phenomena

**Author(s):** Grigory E. Volovik

**Year:** 2001

**Journal:** Physics Reports, Volume 351, Pages 195--348

---

## Abstract

This comprehensive review demonstrates that relativistic quantum field theory is an emergent phenomenon arising in the low-energy limit of a fermionic vacuum with topologically non-trivial electronic structure. Using superfluid 3He as the primary physical analog, Volovik shows how chirality, Weyl fermions, gauge fields, gravity, event horizons, Hawking radiation, cosmological constant, and various particle physics phenomena naturally emerge from the low-energy corner of the superfluid order parameter. The paper argues that the quantum vacuum itself is better understood as a superfluid or other condensed matter system than as a fundamental quantum field, and that many cosmological puzzles have natural resolutions in this paradigm.

---

## Historical Context

By 2001, experimental evidence for quantum effects in superfluid 3He had accumulated, and Volovik had spent the previous decade working out the detailed connection between the low-energy physics of 3He-A and relativistic quantum field theory. This review crystallized those insights for the high-energy physics and cosmology communities. The timing was significant: WMAP would launch in 2001, CMB observations were becoming precision tools, and the 1998 discovery of cosmic acceleration was reshaping cosmological thinking. Volovik's paper suggested an alternative framework: rather than adding dark energy to quantum field theory, one should reconsider whether quantum field theory itself is the right foundation.

The paper's central thesis—that QFT is emergent—challenged the bottom-up reductionism of particle physics. Instead, Volovik proposed a bottom-up emergence model: the universe emerges from a substrate with structure, and what we call particle physics is the low-energy physics of that structure.

---

## Key Arguments and Derivations

### From Fermi Liquid to Lorentz-Invariant Field Theory

In a Fermi liquid at zero temperature, the ground state consists of a filled Fermi sea of electron-like quasiparticles. At the Fermi surface, the density of states is logarithmic in energy. Near a Fermi point (a special location in momentum space where the density of states vanishes), the single-particle Green's function takes the form:

$$G(\omega, \mathbf{p}) = \frac{1}{\omega - \hbar v_F |\mathbf{p}| + i 0^+}$$

This is identical to the Green's function of a massless relativistic particle with speed $v_F$. For energies $\hbar \omega \ll E_F$ (the Fermi energy), the physics is dominated by quasiparticles near the Fermi point, and the effective theory is:

$$\mathcal{L}_{\text{eff}} = \bar{\psi} (i \gamma^\mu \partial_\mu) \psi$$

where $\psi$ is the field operator for quasiparticle excitations, and the Dirac matrices are defined with respect to the effective metric $g_{\mu\nu} = \text{diag}(-1, v_F^{-2}, v_F^{-2}, v_F^{-2})$.

The crucial insight: Lorentz invariance is not a fundamental symmetry of nature, but an **accident** of the low-energy limit. At higher energies (approaching the Fermi energy or lattice spacing), Lorentz invariance is broken. The electron-hole symmetry at the Fermi point is a consequence of the filled Fermi sea structure.

### Emergence of Gauge Fields and Chirality

In superfluid 3He-A, the order parameter is:

$$\Delta_i^a (\mathbf{r}) = \Delta_0 e^{i \phi(\mathbf{r})} m_i n^a(\mathbf{r})$$

where $a$ is a spin index, $i$ is a direction in real space, $\phi$ is the superfluid phase, and $\mathbf{n}$ is an orbital angular momentum vector. Variations in the phase couple to fermions as a U(1) gauge field:

$$A_i = \frac{\hbar}{2e} \partial_i \phi$$

Variations in the orientation of $\mathbf{n}$ induce non-Abelian gauge structure. The **chiral problem** in particle physics—why are left-handed and right-handed fermions treated differently—is solved by the fact that in superfluid 3He-A, the two Weyl points (nodes in the spectrum) occur at different locations in momentum space $\mathbf{p}_+ \ne \mathbf{p}_-$. Near $\mathbf{p}_+$:

$$E_+ (\mathbf{p}) \approx \hbar v_F [(\mathbf{p} - \mathbf{p}_+) \cdot \mathbf{n}]$$

Near $\mathbf{p}_-$:

$$E_- (\mathbf{p}) \approx - \hbar v_F [(\mathbf{p} - \mathbf{p}_-) \cdot \mathbf{n}]$$

One is left-handed, the other right-handed. They couple oppositely to the gauge field. No fine-tuning required; chirality is automatic from the geometry.

### Event Horizons in Superfluids

In flowing superfluid, if the flow velocity exceeds the Bogoliubov speed of sound $c_B$, an event horizon forms—a surface beyond which information cannot propagate back out. In 3He-A, the Bogoliubov sound speed is:

$$c_B = \sqrt{\frac{\partial P}{\partial \rho} + \frac{\Delta^2}{\rho m^*}} \sim 1 \text{ cm/s}$$

In a convergent flow with velocity $v > c_B$, the trajectory of a quasiparticle becomes lightlike, and causality is inverted. This is mathematically identical to the event horizon of a black hole:

$$ds^2 = - (v^2 - c_B^2) dt^2 + 2 v \, dr \, dt + dr^2$$

At the horizon $r = r_h$ where $v(r_h) = c_B$, the metric becomes null. A quasiparticle cannot escape back past $r_h$ into the region where $v > c_B$.

### Hawking Radiation from the Superfluid Perspective

Near the event horizon, the density of states for quasiparticles is enhanced. Volovik showed that virtual pair production (quasiparticle-hole pairs) at the horizon leads to a thermal spectrum of emitted radiation, identical in form to Hawking's calculation:

$$T_{\text{Hawking}} = \frac{\hbar c_B}{2\pi k_B} \left| \frac{d v}{dr} \bigg|_{\text{horizon}} \right|$$

This is not merely an analogy: the microscopic mechanism (pair production in a condensed medium) is the same in both the black hole and the superfluid. Hawking radiation is an inevitable consequence of the quantum structure of the vacuum, emergent from the Bogoliubov spectrum.

### Cosmological Constant and Vacuum Energy

The cosmological constant problem asks: why is the vacuum energy density so small? In quantum field theory, the answer is that we must fine-tune coupling constants to many decimal places. In the condensed matter view:

$$\rho_{\text{vac}} = \frac{1}{V} \left( E_0 - \mu N \right)$$

where $E_0$ is the ground state energy, $\mu$ is the chemical potential, and $N$ is the number of particles. This is not zero by accident; it is zero (or small) because the system has reached **equilibrium**. The ground state is the lowest energy state compatible with conservation laws.

If the universe's vacuum is a superfluid in a state analogous to 3He at the A-B phase transition, different phases have different vacuum energies. Cosmological evolution might correspond to the system moving between phases or regimes, explaining the change in vacuum energy over cosmic history without invoking quintessence.

### Magnetic Monopoles and Topological Defects

In superfluid 3He, topological defects arise naturally from the structure of the order parameter. The most famous example is the **quantized vortex**: a one-dimensional line defect around which the phase winds by $2\pi n$:

$$\oint \nabla \phi \cdot d\mathbf{l} = 2\pi n, \quad n \in \mathbb{Z}$$

The vortex carries a quantum of circulation:

$$\kappa = \oint \mathbf{v}_s \cdot d\mathbf{l} = \frac{h}{m}$$

In cosmology, analogous topological defects (cosmic strings, domain walls, monopoles) form whenever a spontaneous symmetry is broken in the early universe. Volovik argues that these are not exotic addenda to cosmology; they are inevitable, arising from the same topological structure that gives rise to particles and forces.

### The Axial Anomaly

In the standard model, the axial current is not conserved:

$$\partial_\mu j_5^\mu = \frac{N_f N_c}{16\pi^2} F \tilde{F}$$

where $F$ is the field strength tensor and $\tilde{F}$ is its dual. In superfluid 3He-A, Volovik showed that the axial anomaly arises from the topological structure of the Fermi surface. There is a one-to-one correspondence between anomaly coefficients and the winding number of the order parameter around the Fermi point.

$$\text{Anomaly coefficient} \sim \text{Monopole charge in momentum space}$$

The anomaly is not an artifact of renormalization; it is a topological fact: particle creation/annihilation is unavoidable whenever the vacuum geometry supports a topological charge.

---

## Key Results

1. **Lorentz invariance is emergent**: Not a fundamental symmetry, but an accident of low-energy physics near a Fermi point. At higher energies or in different regimes, Lorentz invariance is broken.

2. **Gauge fields emerge from order parameter symmetries**: The electromagnetic field, weak isospin, and color are collective degrees of freedom describing variations in the superfluid order parameter, not fundamental interactions.

3. **Chirality and particle generations emerge from Weyl point geometry**: The existence of left-handed and right-handed particles reflects the spatial separation of Weyl points in momentum space. Multiple generations correspond to multiple Weyl point pairs.

4. **Event horizons and black holes are real in superfluids**: Flowing superfluids exhibit genuine event horizons where causality is inverted, providing a physical realization of black hole thermodynamics.

5. **Hawking radiation emerges from pair production**: The thermal spectrum of emitted radiation is produced by virtual pair creation near the event horizon, the same mechanism in both superfluid and gravitational settings.

6. **Cosmological constant is vacuum ground state energy**: Not a mysterious fine-tuned constant, but the equilibrium energy density of the system. Phase transitions or transitions between regimes change the vacuum energy.

7. **Topological defects are inevitable**: Cosmic strings, monopoles, and domain walls form whenever the order parameter winds around topological charges, making their existence natural rather than exotic.

8. **Axial anomaly reflects Fermi surface topology**: The non-conservation of axial current is a consequence of the monopole charge in the momentum space structure of the Fermi surface.

---

## Connection to Phonon-Exflation Framework

**Direct relevance: VERY HIGH**

This paper is arguably the most important precedent for phonon-exflation. The entire conceptual framework rests on Volovik's insight that quantum field theory is emergent. For phonon-exflation:

- **Particles as quasiparticles**: The electrons, quarks, neutrinos, and photons of the standard model are quasiparticles of a geometric condensate on M4 x SU(3), not fundamental objects. Their masses and couplings are determined by the Dirac spectrum and spectral action of the NCG structure, analogous to how quasiparticle properties emerge from the Fermi surface in a metal.

- **Gauge symmetries from geometry**: Rather than imposing SU(3) x SU(2) x U(1) as a fundamental gauge group, it emerges from the symmetries of the base space SU(3). This is a major simplification: gauge groups are not fundamental, they are consequences of vacuum geometry.

- **Cosmological constant from NCG ground state**: The spectral action $S_{\text{spectral}} = \text{Tr}(f(D_K / \Lambda))$ computes the effective action of the vacuum itself. The constant term in this expansion is the cosmological constant, now understood as the ground state energy of a geometric system.

- **Superfluid phonons and particles**: In phonon-exflation, particles are phononic excitations. Their interactions (mediated by spectral geometry) are described by an effective phonon Hamiltonian, exactly as Volovik describes for 3He-A.

- **Topological defects in the cosmic web**: If particles are excitations of a geometric substrate, the large-scale structure of the universe (filaments, walls, voids, superclusters) might reflect topological defects in the substrate itself. This connects to the cosmic web via condensed matter topological structure.

---

## Key Equations

1. **Fermi point dispersion and relativistic emergences**:
   $$E = \hbar v_F |\mathbf{p} - \mathbf{p}_0|$$

2. **Dirac equation from superfluid**:
   $$i \hbar \gamma^\mu \partial_\mu \psi = m \psi$$

3. **U(1) gauge field from phase variation**:
   $$A_i = \frac{\hbar}{e} \partial_i \phi$$

4. **Event horizon in flowing superfluid**:
   $$v(r) = c_B \quad \text{at horizon}$$

5. **Hawking temperature**:
   $$k_B T_H = \frac{\hbar c_B}{2\pi} \left| \frac{dv}{dr} \right|_{\text{horizon}}$$

6. **Cosmological constant as equilibrium energy**:
   $$\rho_{\text{vac}} = \frac{E_0}{V} - \mu \frac{N}{V}$$

7. **Quantized vortex circulation**:
   $$\oint \mathbf{v}_s \cdot d\mathbf{l} = \frac{h}{m}$$

---

## Legacy and Significance

This 2001 review became foundational reading for anyone interested in quantum gravity, analog gravity, or fundamental physics from a condensed matter perspective. It influenced the development of:

- **Analogue gravity** as a research program (now several hundred papers per year)
- **Topological insulators and superconductors** (recognizing that relativistic physics can emerge in condensed matter)
- **Hawking radiation debates** (some physicists now interpret Hawking's prediction as a universal consequence of any event horizon, not specific to gravitational black holes)
- **Vacuum structure** in quantum field theory (questioning whether the vacuum is truly fundamental)

For cosmology and the cosmic web specifically, the paper implies:

1. The large-scale structure (filaments, walls, voids) may reflect the topological properties of the underlying vacuum condensate.

2. Galaxy clusters, if understood as topological defects or vortex lattices in the condensate, would naturally form filamentary structures.

3. The cosmological constant's present value, and its evolution, should be understood not as the behavior of a mysterious dark energy field, but as a consequence of the vacuum's phase structure and topology.

4. Superfluid turbulence (Kelvin vortex tangles, turbulent cascades) might have analogs in the dynamics of the cosmic structure formation.

---

## References

[Search results integrated; full citations available in search output above.]
