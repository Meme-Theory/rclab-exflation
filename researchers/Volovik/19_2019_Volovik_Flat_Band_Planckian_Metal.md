# Flat Band and Planckian Metal

**Author:** Grigory E. Volovik
**Year:** 2019
**Journal:** JETP Letters 110, 352 (2019)
**arXiv:** 1907.11515

---

## Abstract

The paper discusses the extension of the Sachdev-Ye-Kitaev (SYK) microscopic model demonstrating the characteristic features of the Khodel-Shaginyan fermion condensate—the existence of a finite region of momenta where the energy of electrons is exactly zero (the flat band). A microscopic derivation provides theoretical support for the flat band concept, validating the original phenomenological approach. The flat band is proposed to be responsible for explaining the linear temperature dependence of resistivity observed in "strange metals"—a long-standing puzzle in condensed matter physics. The work builds upon the Patel-Sachdev extension of the SYK model and demonstrates how microscopic interactions naturally produce flat band features within an analytically tractable framework.

---

## Historical Context

"Strange metals" observed in high-temperature cuprate superconductors and heavy fermion systems exhibit a transport anomaly: their electrical resistivity $\rho(T)$ increases linearly with temperature over an extended range, violating the Bloch-Grüneisen law $\rho \propto T^5$ expected for normal Fermi liquids. This Planckian behavior—where the mean free path becomes comparable to the de Broglie wavelength—has remained unexplained for three decades.

Volovik's 2019 paper provides a unified explanation: the strange metal behavior arises from a flat band in the electron dispersion. Such a band creates a flat Fermi surface where the density of states is constant up to a UV scale, leading to temperature-independent scattering rate that couples linearly to temperature through thermodynamic effects.

The paper extends flat-band physics beyond superconductivity (Paper 18) to normal-state transport, revealing a deeper geometric origin for both superconductivity and strange metal anomalies. The SYK model provides a theoretical foundation for understanding how microscopic dynamics (all-to-all interactions in a many-body system) naturally produce flat bands.

---

## Key Arguments and Derivations

### The Sachdev-Ye-Kitaev Model

The SYK Hamiltonian involves $N$ fermions with random all-to-all four-body interactions:

$$H_{SYK} = \sum_{i<j<k<l} J_{ijkl} \psi_i^\dagger \psi_j \psi_k^\dagger \psi_l$$

where the couplings $J_{ijkl}$ are random variables drawn from a Gaussian distribution. Despite disorder, the model has remarkable properties:

1. **Conformal symmetry:** At low energy, the model exhibits emergent conformal symmetry, analogous to holographic duality.
2. **Black hole entropy:** The ground state entropy matches the Bekenstein-Hawking entropy of a black hole, $S \sim N^2$.
3. **Out-of-time-order correlator (OTOC):** The model exhibits maximal chaos with Lyapunov exponent $\lambda_L = 2\pi T$ (saturating bound).

### Khodel-Shaginyan Fermion Condensate

The Khodel-Shaginyan (KS) picture describes a different phase of matter: a Fermi liquid with an occupation singularity (zero-momentum singularity in the Fermi surface). A finite range of momenta near the Fermi surface—the "flat band"—has zero quasiparticle energy:

$$\epsilon_F(\vec{k}) = 0, \quad \vec{k} \in [k_F - \Delta k, k_F]$$

Outside this range, the dispersion is normal. This creates a density of states that is:

- **Constant within the flat band:** $N(E) = N_0$ for $|E| < E_0$ (some UV cutoff)
- **Vanishes outside:** $N(E) = 0$ for $|E| > E_0$

This flat region in $N(E)$ is fundamentally different from normal Fermi liquids or BCS superconductors, both of which have $N(E) \to 0$ as $E \to E_F$.

### Patel-Sachdev Extension of SYK

Patel and Sachdev extended the SYK model to include a lattice structure and quenched disorder leading to fermion spectral functions with frequency scaling:

$$A(\omega, T) = \frac{\Gamma(T)}{\omega^2 + \Gamma(T)^2}$$

where the scattering rate $\Gamma(T) \propto T$ at low temperatures. This frequency dependence is characteristic of a metal with energy-dependent scattering. The remarkable result is that microscopic SYK-type interactions (all-to-all couplings) naturally produce this behavior without fine-tuning.

More remarkably, when the scattering becomes very strong ($\Gamma \sim \omega$), the spectral function flattens:

$$A(\omega, T) \approx \text{const} \quad \text{for} \quad \omega \ll \Gamma(T)$$

This flattening in $\omega$ is the SYK realization of the KS flat band.

### Resistivity in Planckian Metals

The electrical conductivity in the Drude approximation is:

$$\sigma(\omega) = \frac{n e^2}{m(\omega + i\Gamma(T))}$$

where $n$ is the carrier density, $e$ the electron charge, $m$ the effective mass, and $\Gamma(T)$ the scattering rate. The DC resistivity is:

$$\rho = \frac{1}{\sigma(0)} = \frac{m \Gamma(T)}{n e^2}$$

For a conventional metal, $\Gamma(T) \propto T^2$ (electron-electron scattering) or $\Gamma(T) \propto T^5$ (phonon scattering), giving $\rho \propto T^2$ or $T^5$.

However, for a KS fermion condensate with flat band, the scattering rate is **temperature-independent within the flat band**, but quantum fluctuations couple the flat band to the thermal bath. The effective scattering rate becomes:

$$\Gamma(T) = \alpha T$$

where $\alpha$ is a dimensionless coupling. This produces:

$$\rho(T) = \frac{m \alpha T}{n e^2} \propto T$$

Linear resistivity at all measured temperatures below a characteristic scale.

### Planck Length Connection

The term "Planckian" arises from the universal bound on the coupling constant. The thermal diffusivity is:

$$D = \frac{\hbar}{m \Gamma(T)} = \frac{\hbar}{m \alpha T}$$

At the Planckian limit, the mean free path equals the de Broglie wavelength:

$$\ell = \frac{\hbar}{p_F} \sim \frac{\hbar}{m v_F}$$

Setting $\ell \sim D t_{scattering}$ gives:

$$\frac{\hbar}{m v_F} \sim \frac{\hbar}{m \alpha T} \times \frac{\alpha T}{\hbar}$$

Solving: $v_F \sim \alpha T / \hbar$, confirming that Planckian behavior (mean free path $\sim$ wavelength) corresponds to the flat band regime where scattering is maximal.

### Why SYK Produces Flat Bands

The SYK all-to-all interaction structure has a unique property: every fermion interacts equally with all others. This creates a highly degenerate density of states—many electronic configurations have nearly the same energy. In the thermodynamic limit, this degeneracy produces a flat region in the spectrum.

Intuitively: in a normal band, each electronic state is localized in momentum space with a unique energy. In SYK, due to disorder, states become mixed, and many different momentum configurations yield the same energy. The density of states becomes flat.

---

## Key Results

1. **Microscopic Derivation of Flat Bands:** The SYK model provides a first-principles understanding of how all-to-all interactions produce flat bands, validating the KS phenomenology.

2. **SYK-Flat Band Connection:** The Patel-Sachdev extension explicitly shows that SYK-like models generate Khodel-Shaginyan fermion condensate features (flat bands) in their spectral functions.

3. **Planckian Metal Explanation:** The linear temperature dependence of resistivity in strange metals—$\rho \propto T$—arises from the flat band's constant density of states coupled to temperature.

4. **Maximal Scattering Bound:** The scattering rate in a Planckian metal saturates at $\Gamma \sim T$, representing maximal dissipation consistent with causality and unitarity bounds.

5. **Disorder is Essential:** Unlike conventional superconductivity where disorder suppresses pairing, in SYK-type models, disorder (the random all-to-all interactions) is essential for creating flat bands.

6. **Holographic Duality:** The SYK model exhibits properties of holographic systems (black hole entropy, maximal chaos), suggesting Planckian metals may have dual descriptions in terms of quantum gravity.

---

## Impact and Legacy

This paper unified two major puzzle areas in condensed matter physics:
- Superconductivity in flat bands (Paper 18)
- Strange metal transport in cuprates and heavy fermions (Paper 19)

The work inspired extensive subsequent research on:
- Disorder-driven flat bands in real materials
- Holographic descriptions of strange metals
- Connections between chaos (OTOC) and transport
- Quantum critical points and Planckian limits

The SYK-flat band connection has become a paradigm for understanding non-Fermi-liquid behavior in strongly correlated systems.

---

## Connection to Phonon-Exflation Framework

Paper 19 extends the flat-band paradigm from superconductivity to transport, providing critical insight into the **BCS-instability and GGE thermalization gates**. Specifically:

- **Richardson-Gaudin integrability in phonon-exflation:** Just as SYK produces flat bands through disorder and all-to-all interactions, the Jensen deformation of the SU(3) geometry introduces interactions that produce near-degeneracies in the K_7 sector. These are the 8 conserved integrals of the Richardson-Gaudin system (Session 34-35).

- **Planckian scattering in the GGE:** The GGE relic (S38 W3) cannot thermalize because the 8 conservation laws make it integrable. Its effective "resistivity" would be infinite (no thermalization), analogous to SYK's maximal dissipation but mediated by integrability instead of chaos.

- **Maximal entropy production without thermalization:** Paper 19 shows that Planckian metals achieve maximum entropy production subject to causality constraints. Session 38 shows that the GGE relic achieves maximum entropy (generalized ensemble) while remaining infinitely far from thermal equilibrium. Both saturate bounds.

- **Flat band in Dirac spectrum:** The M_max = 1.674 Van Hove point (Sessions 32, 34-35) represents a flat band in the internal Dirac spectrum. The spectral flatness creates a singular DOS that enhances both BCS pairing (Paper 18) and suppresses thermalization (Paper 19). The flat portion of the Dirac spectrum is "invisible" to thermal bath couplings—it remains coherent.

- **Disorder and geometric deformation:** SYK shows that random all-to-all interactions (disorder) create flat bands. Phonon-exflation shows that geometric deformation (the fold, Sessions 22-24) creates similar singular DOS features without randomness. The geometric fold is a "deterministic disorder"—a highly degenerate set of states.

- **Implications for observational signals:** If the GGE relic carries the phononic excitation spectrum of the internal geometry, its scattering properties should mimic a strange metal: it couples to external radiation with a Planckian resistivity that depends on coupling strength, not temperature. This predicts DESI data should show a "fossil" strange-metal transport signature (non-thermal velocity autocorrelation) in the CMB bispectrum or polarization patterns.

The phonon-exflation framework thus predicts that the universe's dark sector (GGE + unthermalized instanton gas) exhibits both superconducting properties (perfect internal boson transport via GPV coherence, S38 W1) and strange-metal transport properties (perfect external fermion dissipation via integrability, S38 W3). Paper 19's Planckian metal insight provides the transport theoretical foundation for this dual character.

---

## References

- [1907.11515] Flat band and Planckian metal (arXiv)
- Volovik, G.E., JETP Lett. 110, 352 (2019)
- Sachdev, S. and Ye, J., Phys. Rev. Lett. 70, 3339 (1993) [SYK origins]
- Patel, A.A. and Sachdev, S., Proc. Natl. Acad. Sci. U.S.A. 114, 1844 (2017) [PS extension]
- Khodel, V.A. and Shaginyan, V.R., Phys. Rev. Lett. 65, 2507 (1990) [KS fermion condensate]
