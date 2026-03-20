# Is the Lightest Kaluza-Klein Particle a Viable Dark Matter Candidate?

**Author(s):** Geraldine Servant, Tim M.P. Tait

**Year:** 2003

**Journal:** Nuclear Physics B 650:391–419; arXiv:hep-ph/0206071

---

## Abstract

We investigate whether the lightest Kaluza-Klein particle (LKP) from Universal Extra Dimensions (UED) can account for the observed relic dark matter abundance. In models with all Standard Model fields propagating in 5D or 6D compact extra dimensions, a conserved KK parity (discrete symmetry) ensures the stability of the LKP. We calculate the relic abundance of the LKP through thermal freeze-out in the early universe, accounting for all relevant annihilation and coannihilation processes with heavier KK modes. We find that both KK photons and KK neutrinos, with masses at the TeV scale, naturally achieve the observed dark matter density $\Omega_{\text{DM}} h^2 \approx 0.12$ without requiring additional parameters beyond those in the UED model. The KK particles couple to Standard Model particles with electroweak strength, providing numerous collider signatures and indirect detection pathways through precision electroweak measurements and astrophysical gamma-ray observations.

---

## Historical Context

By the early 2000s, several extra-dimensional models had been proposed (ADD, RS, UED), but it was unclear whether they could address the dark matter problem. Servant and Tait's 2003 paper showed that Universal Extra Dimensions—where all Standard Model fields live in 5D or 6D—naturally provide a weakly interacting dark matter candidate: the LKP.

This was significant because:

1. **Dark matter from geometry**: It demonstrated that extra dimensions could simultaneously solve the hierarchy problem and provide dark matter, unifying two major problems in physics.

2. **KK parity as discrete symmetry**: The conservation of KK parity (a discrete gauge symmetry in UED) ensures the LKP is stable, analogous to R-parity in supersymmetry.

3. **Thermal relic**: The LKP achieves the correct abundance through standard freeze-out, no exotic mechanisms required.

The paper opened a major research avenue: using collider searches, precision electroweak tests, and indirect dark matter searches to constrain UED models and potentially discover KK states.

---

## Key Arguments and Derivations

### Universal Extra Dimensions Setup

In UED, all Standard Model fields—quarks, leptons, gauge bosons, Higgs—propagate in the bulk of a 5D or 6D spacetime with compact extra dimensions. The metric is:

$$ds^2 = \eta_{\mu\nu} dx^\mu dx^\nu + dy^2 \quad \text{(for 5D)}$$

where $y \in [0, 2\pi R]$ is compactified on a circle.

Kaluza-Klein decomposition of the fields yields:

$$\Psi(x, y) = \sum_{n=-\infty}^{\infty} \psi_n(x) \exp(iny/R)$$

Each 4D field $\psi_n$ is a KK mode with mass:

$$m_n = \sqrt{m_0^2 + (n/R)^2}$$

where $m_0$ is the 5D bulk mass of the field and $n$ is the KK level number.

### KK Parity Conservation

A crucial feature of UED is conservation of **KK parity**, defined as:

$$P_{KK} = (-1)^n$$

where $n$ is the KK level. This is an automatic discrete symmetry in the model (arising from the $\mathbb{Z}_2$ symmetry of the compact dimension).

KK parity conservation implies:

- Odd-level KK particles (n=1, 3, 5, ...) interact via vertices involving an odd number of KK particles.
- Even-level KK particles (n=0, 2, 4, ...) (the zero mode is the Standard Model) interact via vertices with an even number of KK particles.
- The lightest odd-level KK particle is absolutely stable.

The LKP (typically the KK photon $\gamma^{(1)}$ or KK neutrino $\nu^{(1)}$) cannot decay into Standard Model particles, making it a viable DM candidate.

### Relic Abundance Calculation

In the early universe, KK particles are produced in the thermal bath at temperature $T > m_{\text{LKP}}$. As the universe cools, the KK particle becomes non-relativistic and annihilates into Standard Model particles. The freeze-out occurs when the annihilation rate falls below the Hubble expansion rate.

The relic abundance is calculated from the Boltzmann equation:

$$\frac{dn_{\chi}}{dt} + 3H n_\chi = -\langle \sigma v \rangle (n_\chi^2 - n_\chi^{\text{eq},2})$$

where $n_\chi$ is the number density of the LKP, $H$ is the Hubble parameter, $\sigma$ is the annihilation cross section, and $n_\chi^{\text{eq}}$ is the equilibrium abundance.

Integrating from high temperatures down to $T_f$ (freeze-out temperature, when $\Omega_\chi h^2$ becomes constant):

$$\Omega_\chi h^2 = \frac{x_f}{3 \times 10^7 \text{ GeV}} \left\langle \frac{\sigma v}{c} \right\rangle^{-1}$$

where $x_f = m_\chi / T_f \approx 20-30$ for weak-scale interactions, and $\langle \sigma v / c \rangle$ is the thermally averaged annihilation cross section.

### Annihilation Channels

For KK photon LKP ($\gamma^{(1)}$), the dominant annihilation processes are:

1. **Annihilation to Standard Model fermions**: $\gamma^{(1)} \gamma^{(1)} \to f \bar{f}$

2. **Annihilation to SM gauge bosons**: $\gamma^{(1)} \gamma^{(1)} \to W^+ W^-, ZZ, \gamma\gamma$

3. **Coannihilation with heavier KK states**: $\gamma^{(1)} g^{(1)} \to $ SM states, etc.

The cross section for s-channel annihilation is:

$$\sigma(s) = \frac{\alpha^2}{s} \sum_f N_c^f Q_f^2 \beta_f$$

where $\alpha$ is the fine structure constant, $N_c^f$ is the color factor (3 for quarks, 1 for leptons), $Q_f$ is the electric charge in units of $e$, and $\beta_f = \sqrt{1 - 4m_f^2/s}$ is the velocity factor.

For $m_\gamma \sim 1$ TeV, the cross section gives:

$$\langle \sigma v \rangle \sim 10^{-26} \text{ cm}^3 / \text{s}$$

which is precisely the "WIMP miracle" cross section, yielding the observed relic abundance.

### Coannihilation Effects

Heavier KK states (e.g., $Z^{(1)}$, $W^{(1)}$, $g^{(1)}$) are typically within 10–20% of the LKP mass due to the mass spacing from $n/R$ terms. At freeze-out temperatures $T_f \sim 50-100$ GeV, these heavier states are still in thermal equilibrium, and processes like $\gamma^{(1)} Z^{(1)} \to f \bar{f}$ contribute to the effective annihilation rate.

Servant and Tait find that coannihilation increases the annihilation rate, thereby increasing the relic abundance. The effect is significant but can be precisely calculated given the UED spectrum.

### Direct Detection

The LKP scatters elastically off nuclei through t-channel Z exchange:

$$\gamma^{(1)} N \to \gamma^{(1)} N$$

The spin-independent scattering cross section is:

$$\sigma_{\text{SI}} \sim \frac{\alpha m_N}{m_Z^2} \times (\text{overlap factors})$$

For $m_\gamma \sim 1$ TeV, predictions for direct detection are in the $10^{-45}$ cm$^2$ range, accessible to next-generation experiments.

---

## Key Results

1. **Viable WIMP**: The LKP naturally achieves the observed dark matter relic abundance $\Omega_{\text{DM}} h^2 \approx 0.12$ through standard thermal freeze-out with weak-scale couplings.

2. **KK parity protection**: Discrete KK parity ensures absolute LKP stability, analogous to R-parity in SUSY.

3. **Mass scale**: The LKP mass is naturally in the 500 GeV – few TeV range, matching electroweak scale expectations.

4. **Collider signatures**: KK particles are produced at hadron colliders (Tevatron, LHC) with visible signatures: missing energy, kinky jets, etc.

5. **Precision constraints**: Electroweak precision data (S, T parameters) place bounds on the KK scale: $1/R > 300$ GeV for 5D UED.

6. **Indirect detection**: The LKP annihilation in galactic centers produces gamma rays, neutrinos, and positrons detectable by gamma-ray telescopes and neutrino observatories.

---

## Impact and Legacy

The Servant-Tait paper made KK dark matter a major research topic:

- **Collider searches**: Experiments at Tevatron and LHC searched for KK quark and gluon resonances, setting bounds on $1/R > 600$ GeV (LHC).
- **Dark matter direct searches**: Experiments like XENON, LUX, and others tested KK dark matter predictions.
- **Precision electroweak**: Measurements of the S and T parameters from Z-pole precision data constrained KK models.
- **Indirect detection**: Fermi, IceCube, and other astrophysical experiments looked for annihilation/decay signals.
- **Extensions**: Warped KK dark matter (in RS), little Higgs models, and other variants explored.

The paper demonstrated that extra dimensions could be simultaneously a solution to hierarchy and dark matter—a major theoretical achievement.

---

## Connection to Phonon-Exflation Framework

**DM from internal structure**: Whereas KK dark matter arises from geometry of extra dimensions (KK parity conservation), phonon-exflation proposes that dark matter arises from the quasiparticle excitation spectrum of the internal SU(3) fiber—a phononic or exciton-like degree of freedom.

**Spectral origin**: KK DM is a kinematic consequence of compactification; phonon-exflation DM emerges from the density-of-states near the Fermi surface of the BCS ground state, with particle mass scales determined by the spectral action on SU(3).

**Relic abundance**: KK DM achieves the correct relic abundance through weak-scale annihilation cross sections. Phonon-exflation's mechanism is through creation in the early universe (instanton gas, Kibble-Zurek), not thermal freeze-out, providing a different (potentially testable) abundance prediction.

**Discrete symmetry**: KK parity is a discrete gauge symmetry protecting LKP stability. The phonon-exflation framework has exact U(1)_7 symmetry on the SU(3) fiber, with Cooper pairs carrying K_7 charge ±1/2, implying the DM phonon (K_7-neutral) is stable.

**Mass scale**: KK DM mass $\sim$ TeV; phonon-exflation DM arises from the gap scale (soft dynamics) and may have a different mass profile, potentially detectable through precision structure observations (void shapes, matter power spectrum).

**Relevance**: The Servant-Tait paper validates the viability of geometrically-sourced DM. Phonon-exflation extends this insight by coupling internal geometry evolution (tau dynamics) to the early universe particle creation process, with DM abundance set by the GGE (Generalized Gibbs Ensemble) rather than thermal equilibrium.

---

## References

- Servant, Tait. "Is the Lightest Kaluza-Klein Particle a Viable Dark Matter Candidate?" Nucl. Phys. B 650 (2003) 391–419.
- Cheng, Dobrescu, Tait. "Cosmological and Astrophysical Constraints on Kaluza-Klein Masses." Phys. Rev. D 60 (1999) 075015.
- Later reviews: Dobrescu, Morrissey. "Universal Extra Dimensions and the Higgs Boson Mass." JHEP 0704 (2007) 053.
