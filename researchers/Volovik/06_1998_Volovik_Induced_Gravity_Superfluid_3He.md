# Induced Gravity in Superfluid 3He

**Author(s):** G.E. Volovik
**Year:** 1998
**Journal:** Proceedings of QFS-98 (Quantum Fluids and Solids)
**arXiv:** cond-mat/9806010
**Relevance:** CRITICAL

---

## Abstract

The gapless fermionic excitations in superfluid 3He-A have the "relativistic" spectrum close to the gap nodes. This allowed us to model the modern cosmological scenaria of baryogenesis and magnetogenesis. The same massless fermions induce another low-energy property of the quantum vacuum -- the gravitation. The effective metric of the space, in which the free quasiparticles move along geodesics, is not generally flat. Different order parameter textures correspond to curved effective space and produce many different exotic metrics, which are theoretically discussed in quantum gravity and cosmology. This includes the condensed matter analog of the black hole and event horizon, which can be realized in the moving soliton. This will allow us to simulate and thus experimentally investigate such quantum phenomena as the Hawking radiation from the horizon, the Bekenstein entropy of the black hole, and the structure of the quantum vacuum behind the horizon. One can also simulate the conical singularities produced by cosmic strings and monopoles; inflation; temperature dependence of the cosmological and Newton constants, etc.

PACS numbers: 67.57.-z, 04.60.-m, 04.70.-s, 11.27.+d, 98.80.Cq

## Key Arguments and Derivations

### 1. Condensed Matter as Guide to Planck Physics

Volovik's central thesis: the physical vacuum is a complicated substance ("Planck condensed matter") whose microscopic structure is at the Planck scale, inaccessible to current experiments. However, the low-energy properties of condensed matter systems are **robust** -- they depend on symmetry and topology, not microscopic details. The microscopic structure only provides "fundamental constants" (speed of sound, superfluid density, elastic modulus, etc.) entering the effective Lagrangian.

By this analogy, gravitation, gauge fields, and chiral fermions arise as **low-energy soft modes** of the Planck condensed matter. At high (Planck-scale) energies these modes merge with the high-energy continuum and cannot be separated. Superfluid 3He-A is the best condensed matter analog because its low-energy degrees of freedom genuinely consist of chiral fermions, gauge fields, and gravity.

### 2. Gap Nodes and Emergent Gravity (Section 2)

The key property of 3He-A is that its Bogoliubov-Nambu quasiparticles are **gapless** -- the energy spectrum E(p) has point nodes where E = 0. Near a gap node at momentum p^(0), the spectrum takes a quadratic form:

E^2(p) = g^{ik} (p_i - p^(0)_i)(p_k - p^(0)_k)

The tensor g^{ik} plays the role of an **effective metric tensor**, while A = p^(0) acts as a **vector potential** of an effective electromagnetic field. When superflow is present (v_s != 0), the Doppler shift E(p) -> E(p) + p . v_s introduces the scalar potential A_0 = p^(0) . v_s and mixed metric component g^{i0} = v_s^i. The full spectrum becomes relativistic:

g^{mu nu} (p_mu - eA_mu)(p_nu - eA_nu) = 0

where e = +/- reflects that quasiparticles near opposite nodes carry opposite charges (and opposite chiralities).

**Topological stability** of gap nodes ensures that small deformations of the vacuum do not destroy the nodes but only deform g^{mu nu} and A_mu -- making these fields **dynamical collective modes**. Near the nodes, fermions are chiral and satisfy the Weyl equations. This gives 3He-A all the ingredients of relativistic QFT: chiral fermions, gauge fields, and gravitation.

Internal symmetries (SU(2), SU(3)) arise as consequences of the number of gap nodes and symmetry relations between them. SU(2) gauge field arises naturally in 3He-A from the node structure.

### 3. Cosmological Constant Problem (Section 3)

Volovik provides a condensed matter resolution to the cosmological constant problem:

**The electroneutrality principle generalized:** An equilibrium homogeneous ground state of condensed matter has zero charge density if charges interact via long-range forces. Applied to gravity: the equilibrium vacuum must satisfy dS_vac/dg^{mu nu} = sqrt(-g) T^{mu nu}_vac = 0, meaning the cosmological term vanishes in equilibrium.

**Why zero-point calculations fail:** Estimating vacuum energy from phonon zero-point energy E_zp = (1/2) sum_k hbar omega(k) never gives the correct ground-state energy -- sometimes even the wrong sign. Phonons are soft variables defined only in the low-energy limit, but vacuum energy is determined by quantum many-body physics involving high-energy degrees of freedom. These high-energy degrees are always adjusted to provide equilibrium (e.g., electroneutrality), irrespective of low-energy physics.

**Two consequences:**
1. The zero cosmological term in equilibrium is dictated by Planckian/trans-Planckian degrees of freedom. The equilibrium homogeneous vacuum does not gravitate. Only **deviations** from equilibrium can gravitate -- e.g., in the presence of matter, a small cosmological term of order the matter energy density is possible.
2. Quantizing low-energy modes (gravity) and adding their zero-point energy constitutes **double counting**. The total energy is already determined by the full quantum many-body problem. Gravity is a low-frequency, classical result of quantization of high-energy degrees of freedom -- one should not quantize it again.

### 4. Gravitational Constant in 3He-A (Section 4)

The effective gravitational constant is extracted by comparing the energy density of the "clapping mode" (a spin-2 mode in 3He-A) with the graviton energy density:

T^0_0 = (1/16 pi G) [(dz h_xy)^2 + (1/4)(dz(h_xx - h_yy))^2]

The clapping mode has the same structure, yielding a **temperature-dependent** gravitational constant:

G(T) = 12 pi / [K(T) Delta^2(T)]

where Delta is the gap amplitude (playing the role of Planck energy) and K(T) = 1 - T^2/T_c^2 near T_c. The temperature dependence comes from two sources: (1) the traditional screening of gravity by thermal fermions (through K(T)), and (2) the temperature dependence of the Planck energy cutoff Delta(T), which is determined by trans-Planckian physics.

Important insight: Delta^2(T) ~ Delta^2(0)(1 - T^2/T_c^2), showing how corrections of order T^2/E_P^2 from Planckian physics can appear even at low T.

### 5. Event Horizon in Moving Domain Wall (Section 5)

A moving topological soliton (domain wall) in thin-film 3He-A creates an analog event horizon. The domain wall separates regions with opposite l-hat directions. The "speed of light" in the x-direction changes sign across the wall:

c_x(x) = c_perp tanh(x/d)

For a wall moving with velocity v, the effective metric is:

ds^2 = -(1 - v^2/c_x^2) dt^2 - (2v/c_x^2) dx dt + dx^2/c_x^2 + dy^2/c_perp^2 + dz^2/v_F^2

Two event horizons appear at x = +/- x_h where tanh(x_h/d) = v/c_perp:
- x = +x_h: black hole horizon (particles cannot escape outward)
- x = -x_h: white hole horizon (particles cannot enter inward)

The singularity sits at x = 0. Both past and future horizons are physical -- a key distinction from extended black hole descriptions.

### 5.1. Hawking Temperature and Bekenstein Entropy

No equilibrium thermodynamic state exists in the presence of a horizon -- the local pressure diverges. The dissipative state produces Hawking radiation at temperature:

T_H = (hbar / 2 pi k_B) kappa, where kappa = (dc_x/dx)|_h

For the domain wall:

T_H(v) = T_H(v=0) (1 - v^2/c_perp^2), with T_H(v=0) = hbar c_perp / (2 pi k_B d)

Hawking radiation causes deceleration, shrinking the distance between horizons until they merge (wall stops). The entropy approaches one degree of quasiparticle freedom per Planck area -- the Bekenstein entropy, arising from fermion zero modes (topologically dictated bound states at zero energy).

### 6. Vortices as Cosmic Strings (Section 6)

A quantized vortex in a 3He-A film produces an effective metric:

ds^2 = -(1 - v_s^2/c_perp^2) dt^2 - (hbar N / m_3 c_perp^2) dphi dt + (1/c_perp^2)(dr^2 + r^2 dphi^2) + dz^2/v_F^2

Far from the core (v_s << c_perp), this is the metric of a **cosmic spinning string**, leading to the gravitational Aharonov-Bohm effect and the Iordanskii lifting force.

### 6.1. Ergoregion Instability

For r < r_e = hbar N / (2 m_3 c_perp), the superflow exceeds the speed of light (v_s > c_perp) and g^{00} > 0, creating an ergoregion with negative quasiparticle energy. For large winding number N >> 1, the vacuum is unstable in the ergoregion. The instability erases the ergoregion: a normal-state shell forms, separating two superfluid vacua without ergoregions. This demonstrates that **equilibrium vacuum does not sustain ergoregions**.

The development of vacuum instability can simulate inflation, including exponential or power-law decay of the speed of light.

## Key Results

1. **Emergent gravity from topology:** The effective metric g^{mu nu} and gauge fields A_mu arise as dynamical collective modes from topologically stable gap nodes in the fermionic spectrum of 3He-A. Near nodes, fermions are chiral and obey Weyl equations.

2. **Cosmological constant = 0 in equilibrium:** The 3He analog shows that the equilibrium vacuum does not gravitate (dS_vac/dg^{mu nu} = 0 is a thermodynamic equilibrium condition). Only deviations from equilibrium produce a cosmological term. The 120-order discrepancy arises from illegitimate zero-point energy calculations.

3. **Do not quantize gravity:** Gravity is a classical low-frequency result of high-energy quantum degrees of freedom. Quantizing it separately is double-counting. The vacuum energy is determined by the full many-body problem.

4. **Temperature-dependent G:** The effective gravitational constant G(T) = 12 pi / [K(T) Delta^2(T)] receives corrections from both thermal fermion screening and trans-Planckian physics through Delta(T).

5. **Event horizon analog:** A moving domain wall in 3He-A thin film creates black hole and white hole horizons with Hawking radiation at T_H = (hbar/2pi k_B)(dc_x/dx)|_h, Bekenstein entropy from fermion zero modes, and merger dynamics as Hawking radiation decelerates the wall.

6. **Vortex = spinning cosmic string:** Quantized vortices produce cosmic-string metrics with gravitational Aharonov-Bohm effect and Iordanskii force.

7. **Ergoregion instability:** The superfluid vacuum is unstable when v_s > c_perp. For large-N vortices, the ergoregion is erased by core reconstruction. Equilibrium vacuum cannot sustain ergoregions. This instability can simulate inflation.

8. **Internal symmetries from node structure:** SU(2) and SU(3) gauge symmetries emerge from the number and symmetry relations of gap nodes, not from fundamental postulates.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Gap node spectrum | E^2(p) = g^{ik}(p_i - p^(0)_i)(p_k - p^(0)_k) | Eq. (1) |
| Relativistic dispersion | g^{mu nu}(p_mu - eA_mu)(p_nu - eA_nu) = 0 | Eq. (2) |
| Graviton energy density | T^0_0 = (1/16piG)[(dz h_xy)^2 + (1/4)(dz(h_xx-h_yy))^2] | Eq. (3) |
| Effective G(T) | G(T) = 12 pi / [K(T) Delta^2(T)] | Eq. (4) |
| K(T) near T_c | K(T) = 1 - T^2/T_c^2 | Eq. (5) |
| Domain wall spectrum | E^2 = c_z^2(p_z -/+ p_F)^2 + c_x^2 p_x^2 + c_y^2 p_y^2 | Eq. (6) |
| Speed of light profile | c_x(x) = c_perp tanh(x/d) | Eq. (7) |
| Moving wall metric | ds^2 = -(1-v^2/c_x^2)dt^2 - 2v/c_x^2 dx dt + ... | Eq. (9) |
| Horizon location | tanh(x_h/d) = v/c_perp | Eq. (10) |
| Hawking temperature | T_H = (hbar/2pi k_B) kappa, kappa = (dc_x/dx)|_h | Eq. (12) |
| T_H(v) explicit | T_H(v) = T_H(0)(1 - v^2/c_perp^2) | Eq. (13) |
| Vortex metric | ds^2 = -(1-v_s^2/c_perp^2)dt^2 - (hbar N/m_3 c_perp^2)dphi dt + ... | Eq. (14) |

## Relevance to Phonon-Exflation

This paper is a **direct blueprint** for the emergent gravity program in phonon-exflation cosmology. Key connections:

1. **Gravity from topology, not postulate:** Volovik's derivation of g^{mu nu} as a collective mode of topologically stable gap nodes is exactly the mechanism the framework needs. The metric emerges from the same fermionic substrate that produces matter -- gravity and matter share a common origin. This parallels the framework's derivation of effective spacetime from the Dirac spectrum on M4 x SU(3).

2. **Cosmological constant resolution:** The equilibrium-zero argument (dS_vac/dg^{mu nu} = 0 as a thermodynamic condition) is the condensed-matter version of the framework's CC mechanism. Volovik shows that vacuum energy calculations using zero-point sums are illegitimate double-counting -- the CC problem is an artifact of treating gravity as fundamental rather than emergent. This directly supports the instanton-gas approach where CC arises from non-equilibrium deviations.

3. **Temperature-dependent constants:** G(T) depending on both thermal screening and trans-Planckian physics (through Delta(T)) provides a concrete model for how fundamental constants evolve during the tau-transit. The framework's tau-dependent couplings are the direct analog.

4. **Event horizon from domain wall:** The moving soliton creating a black-hole/white-hole pair is a condensed matter realization of horizon physics with no singularity at the microscopic level. The Hawking temperature and Bekenstein entropy emerge from fermion zero modes, not from fundamental quantum gravity. This supports the framework's Parker-type particle creation during transit.

5. **Ergoregion instability as inflation analog:** Volovik explicitly notes that the vacuum instability when v_s > c_perp can simulate inflation, with the "speed of light" decaying exponentially. This is directly relevant to the exflation mechanism where the internal geometry change drives expansion.

6. **Internal symmetries from gap-node structure:** The emergence of SU(2) and SU(3) from the number and symmetry of gap nodes mirrors the framework's derivation of SM gauge groups from the spectral geometry of the internal space. Both programs arrive at the same conclusion: gauge symmetries are consequences of vacuum topology, not axioms.

7. **Universality class argument:** Volovik's proposal that the "Planck condensed matter" belongs to the same universality class as 3He-A is the conceptual foundation for the entire phonon-exflation program. If the vacuum is in this universality class, then chiral fermions, gauge fields, and gravity are **guaranteed** low-energy outputs regardless of microscopic details.
