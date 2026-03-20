# Axial Anomaly in 3He-A: Simulation of Baryogenesis and Generation of Primordial Magnetic Fields

**Author(s):** Grigory E. Volovik
**Year:** 1998
**Journal:** Physica B, 255(3), 86-95
**arXiv:** cond-mat/9802091

---

## Abstract

This paper demonstrates that superfluid 3He-A simulates the **chiral anomaly** — the quantum mechanical non-conservation of baryon (or lepton) number in the presence of a background axial gauge field. The key findings are:

- The gapless fermions (quasiparticles) in 3He-A with a quantized vortex experience an effective axial gauge field, similar to the electroweak gauge bosons in the early universe.
- The chiral anomaly induces the conversion of charge from the superfluid condensate to the quasiparticles, violating naive baryon number conservation.
- In the high-energy physics context, this mechanism is analogous to the **electroweak baryogenesis** — the generation of the baryon asymmetry of the universe through CP-violating fermion interactions in the presence of sphaleron processes.
- The paper shows that quantized vortices in 3He-A can be used to simulate baryogenesis and test the dynamics of charge creation.
- The analogy extends to the generation of primordial magnetic fields via anomalous fermionic current interactions.

This work provides the first direct condensed matter analog of baryogenesis, allowing tabletop experiments on processes relevant to early-universe physics.

---

## Historical Context

### The Baryon Asymmetry Puzzle

One of the greatest mysteries in cosmology is the **baryon asymmetry of the universe** (BAU). Observations show:

$$n_B - n_{\bar{B}} \approx 6 \times 10^{-10} \, n_\gamma$$

where $n_B$ is the baryon density, $n_{\bar{B}}$ is the antibaryon density, and $n_\gamma$ is the photon density.

This tiny but nonzero asymmetry has profound consequences:
- Without it, all matter and antimatter would have annihilated in the early universe.
- No galaxies, stars, planets, life would exist.

Yet the initial conditions of the Big Bang should have produced equal numbers of particles and antiparticles. How did the asymmetry arise?

Sakharov (1967) identified three necessary conditions:
1. Baryon number violation
2. CP violation (matter-antimatter asymmetry)
3. Departure from thermal equilibrium

### The Electroweak Baryogenesis Scenario

In the Standard Model, baryon number is violated via **sphaleron processes** — nonperturbative electroweak anomalies at temperatures $T > 100$ GeV. The sphaleron rate is related to the **axial anomaly**:

$$\partial_\mu j_A^\mu = \frac{N_f \alpha_W}{2\pi} \mathbf{E} \cdot \mathbf{B}$$

where $j_A^\mu$ is the axial current, $\alpha_W$ is the weak coupling, and $\mathbf{E} \cdot \mathbf{B}$ is the Chern-Simons invariant of the electroweak field.

This non-conservation of axial charge implies baryon number non-conservation in the presence of an axial current source.

### Volovik's Analog: 3He-A Vortices

By 1998, it was clear that 3He-A provides a remarkable condensed matter analog of relativistic quantum field theory. Volovik proposed that **quantized vortices in 3He-A simulate the sphaleron-like processes** that produce baryogenesis.

The key insight: gapless fermions bound to a vortex in 3He-A experience an effective **topological gauge field** (the "texture field"). This field induces the anomaly.

---

## Key Arguments and Derivations

### Part I: Gapless Fermions in 3He-A and Chiral Symmetry

#### The 3He-A Superfluid Structure

Superfluid 3He-A has order parameter:

$$\Delta_{\alpha i}({\bf r}) = d_\alpha \ell_i({\bf r})$$

where $\alpha \in \{\uparrow, \downarrow\}$ is the spin and $i \in \{1,2,3\}$ is the orbital angular momentum direction.

The superfluid has **three gap nodes** — lines in momentum space where the quasiparticle energy vanishes. Near these nodes, the spectrum is:

$$E(\mathbf{p}) \approx v_F \, p_\perp$$

where $p_\perp$ is the momentum perpendicular to the node. This is a **linear, relativistic spectrum** — exactly like the Dirac equation for a massless fermion.

Each of the three gap nodes has **chirality**: the fermionic states carry a well-defined helicity (spin aligned or anti-aligned with momentum).

#### Axial Current

The axial current density is:

$$j_A^{\mu} = \bar{\psi} \gamma^\mu \gamma^5 \psi$$

where $\gamma^\mu$ are gamma matrices and $\gamma^5 = \gamma_1 \gamma_2 \gamma_3 \gamma_4$ is the chiral projector.

In vacuum (no interaction), this current is conserved: $\partial_\mu j_A^\mu = 0$.

However, in the presence of a **background gauge field** (like the electroweak field in particle physics), the divergence is nonzero — this is the **chiral (or axial) anomaly**.

### Part II: The Anomaly in 3He-A Vortices

#### Vortex Texture as Topological Field

A quantized vortex in 3He-A is a singular solution of the order parameter where the phase winds around the core:

$$\ell_i({\bf r}) = \hat{z} \quad \text{(far from core)}$$

$$\phi({\bf r}) = \theta \quad \text{(azimuthal angle around vortex axis)}$$

The order parameter phase varies as $e^{i\theta}$ around the core. This phase variation acts like a **gauge field** for the fermionic quasiparticles.

The effective Hamiltonian for a quasiparticle near the vortex core is:

$$H = v_F (-i\nabla + \mathbf{A}) \cdot {\boldsymbol \sigma} + \text{gap terms}$$

where $\mathbf{A} = \nabla \theta$ is the "gauge field" induced by the vortex phase winding.

#### Bound States and Anomalous Current

Inside the vortex core, there are **zero-energy bound states** (Andreev or Majorana-like states) due to the topological structure.

The presence of these states means the vacuum energy (Fermi level) inside the vortex is shifted. This creates an **imbalance between left- and right-handed fermions**:

$$N_L - N_R \neq 0$$

in the vortex core region.

Crucially, the bound state carries a finite charge (or baryon number):

$$Q = \int d^3 r \, \rho({\bf r})$$

This charge is **topological** — it depends only on the winding number of the vortex, not on microscopic details.

#### Chiral Anomaly Formula

The anomaly relates the divergence of the axial current to the Chern-Simons form of the gauge field:

$$\partial_\mu j_A^\mu = \frac{1}{2\pi} \epsilon^{\mu\nu\rho\sigma} \text{Tr}(A_\mu \partial_\nu A_\rho \partial_\sigma A_\sigma + \ldots)$$

In the vortex background, the gauge field $\mathbf{A} = \nabla \theta$ winds. The integral of the right-hand side gives:

$$\int d^3 r \, \partial_\mu j_A^\mu = \text{winding number} \times (\text{fundamental charge})$$

This is a **quantized anomaly** — the total "baryon number violation" is an integer multiple of the fundamental unit.

### Part III: Momentum Creation by Vortices

#### Momentum Conservation and Vortex

A remarkable experimental prediction: as a vortex moves through the superfluid, it carries **momentum** (or more precisely, angular momentum). This is the analog of baryon number creation.

The momentum carried by a vortex of circulation quantum $n_0$ is:

$$\mathbf{L}_{vortex} = n_0 (\mathbf{r} \times \mathbf{v})$$

where $\mathbf{v}$ is the vortex velocity.

This momentum is **transferred to the quasiparticles** — creating a net imbalance in the fermionic momentum distribution.

In the baryon-number language of particle physics, this is equivalent to **spontaneous baryon number violation**: a topological defect (vortex = sphaleron) creates asymmetry between particles and antiparticles.

### Part IV: Primordial Magnetic Field Generation

#### Anomalous Fermionic Current

The chiral anomaly also produces an anomalous current in the presence of a pseudoscalar background field. If the vortex carries not just phase but also **spin texture**, an anomalous current develops:

$$\mathbf{j}_{anom} \propto (\nabla \times \ell_i) \times (\text{fermionic polarization})$$

This current acts like a **magnetic current** (or more precisely, a monopole current in 3+1 dimensions).

#### Primordial Magnetic Fields

In cosmology, primordial magnetic fields can arise from:
1. Electroweak baryogenesis with magnetic field sources (hypermagnetic fields).
2. Anomalous fermionic currents in the presence of background textures.

The 3He-A model shows that a network of vortices (or texture defects) can generate **persistent currents** that resemble magnetic field generation.

These currents are topological — they depend on the vortex winding numbers and do not decay away. The analogy suggests that primordial magnetic fields in the early universe may arise from topological defects via anomalous current mechanisms.

---

## Key Results

1. **Gapless fermions in 3He-A vortices exhibit the chiral anomaly**: The axial current is not conserved, analogous to electroweak baryogenesis.

2. **Vortices create baryon-number-like asymmetry**: Quantized vortices bind zero modes that carry topological charge, acting like baryon creation operators.

3. **Momentum can be generated spontaneously**: The motion of vortices through the superfluid transfers momentum to quasiparticles, analogous to sphaleron-induced baryon number violation.

4. **Anomalous currents generate topological fields**: The chiral anomaly induces effective magnetic-like currents that persist due to topological protection.

5. **Primordial magnetic fields can arise from defect networks**: The analogy with 3He-A vortices suggests that topological defects in the early universe generate primordial fields.

6. **Laboratory simulation of baryogenesis is possible**: 3He-A vortices can be observed directly in experiments, allowing tests of anomaly physics in a controlled setting.

---

## Impact and Legacy

This 1998 paper was ahead of its time in proposing analog experiments for cosmological physics:

- **Experimental vortex observations** (1990s-2000s): Direct observation of quantized vortices in 3He and BEC, confirming theoretical predictions.

- **Topological defect networks**: The physics of vortex lattices and strings has become central to understanding phase transitions in cosmology, superfluids, and superconductors.

- **Quantum simulation of QCD**: The idea that condensed matter systems can simulate QCD thermodynamics and phase transitions has been explored extensively (e.g., cold atoms in optical lattices).

- **Anomaly-induced transport**: Recent discoveries of anomalous Hall effect, chiral magnetic effect, and other anomaly-induced phenomena in condensed matter validate Volovik's insights about the universality of anomalies.

---

## Connection to Phonon-Exflation Framework

The chiral anomaly in 3He-A provides a direct model for baryogenesis in phonon-exflation:

1. **K_7 defects as vortex analogs**: Just as 3He-A vortices carry topological charge, the K_7 condensate on SU(3) may have topological defects (instantons, monopoles, etc.) that bind chiral fermion zero modes.

2. **Baryon number violation from condensate structure**: The chiral anomaly mechanism shows how fermionic number conservation can be violated in a topologically nontrivial condensate. This is the key to understanding baryon asymmetry in phonon-exflation.

3. **Spontaneous charge creation**: Volovik's mechanism of momentum/charge creation by vortices parallels phonon-exflation's prediction that particle-antiparticle pairs can be created asymmetrically during expansion.

4. **GGE as anomalous state**: The permanent non-thermal GGE relic produced during cosmic transition may be a manifestation of the chiral anomaly — an irreversible, topologically protected creation of fermionic asymmetry.

5. **CP violation from textures**: The internal geometry (SU(3)) and its defects are sources of CP violation, analogous to the electroweak CP violation in conventional baryogenesis.

6. **Testable predictions**: Just as 3He-A vortex experiments can measure anomaly-induced currents, phonon-exflation predicts observable signatures of baryon asymmetry production (e.g., constraints from nucleosynthesis, gravitational waves from defect networks).

---

## References

- Volovik, G. E. (1998). "Axial anomaly in 3He-A: Simulation of baryogenesis and generation of primordial magnetic fields in Manchester and Helsinki." *Physica B*, 255(3), 86-95. arXiv:cond-mat/9802091.

- Volovik, G. E. (1998). "Baryon asymmetry of the Universe: View from superfluid 3He." *Journal of Low Temperature Physics*, 113(3/4), 667-684.

- Volovik, G. E., & Kravtsov, V. E. (1995). "Momentum creation by vortices in superfluid 3He as a model of primordial baryogenesis." *JETP Letters*, 61(8), 633-637.

- Sakharov, A. D. (1967). "Violation of CP invariance, C asymmetry, and baryon asymmetry of the universe." *JETP Letters*, 5, 24-27.
