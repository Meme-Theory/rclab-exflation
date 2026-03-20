# Acoustic Metamaterials and Phononic Crystals: Bandgap Engineering (2006-2010)

**Author:** Richard Craster, Sebastien Guenneau, and colleagues
**Year:** 2006-2010 (review period); foundational work 1995-2005
**Source:** Craster & Guenneau, "Acoustic metamaterials: Negative refraction, imaging, lensing and cloaking" (2013, book)

---

## Abstract

Acoustic metamaterials and phononic crystals are engineered materials designed to exhibit unusual dynamic properties—such as negative refractive index, bandgaps (frequency ranges where waves cannot propagate), and topological edge states. By arranging inclusions (masses, cavities, or resonators) in periodic or carefully designed patterns, one can control how acoustic and elastic waves propagate, achieving effects like acoustic cloaking, negative dispersion, and artificial sound barriers. Modern phononic crystals exploit Bragg scattering (interference of waves reflected from periodic structures), local resonances, and topological band structure. This review examines the physics of phononic bandgaps, the mechanisms for achieving anomalous dispersion, and applications to phononic metamaterials.

---

## Historical Context

Classical acoustics deals with sound waves propagating through homogeneous media. In the 1990s, researchers (inspired by photonic crystals, which were developed for controlling light) asked: can we design materials to control acoustic waves?

The breakthrough realization was that periodic structures at acoustic wavelengths could exhibit bandgaps—frequency ranges where waves are forbidden from propagating. This is analogous to electronic bandgaps in semiconductors (where electrons cannot exist in certain energy ranges) and photonic bandgaps (where photons cannot propagate).

Early work focused on 1D and 2D phononic crystals—periodic arrays of scatterers or cavities. Craster and Guenneau's work (2000s) showed that sophisticated bandgap engineering could achieve dramatic effects: acoustic waves with negative group velocity (waves propagate backward relative to their phase), negative bulk modulus and mass density (metamaterial properties), and acoustic cloaking (sound passing around an object without scattering).

---

## Bragg Scattering and Bandgap Formation

### Periodic Lattice and Bragg Condition

A phononic crystal is a periodic arrangement of different materials (or cavities) in a host medium. Consider a 1D chain with alternating materials: bars of material 1 (thickness $d_1$, impedance $Z_1$) and material 2 (thickness $d_2$, impedance $Z_2$).

Acoustic waves propagating in this 1D chain experience reflections at each interface. If the wavelength $\lambda$ is related to the lattice period $d = d_1 + d_2$ by:

$$\lambda = 2d / n$$

(Bragg condition, $n = 1, 2, 3, ...$), then reflections from successive interfaces interfere constructively, and the wave is strongly scattered. The wave cannot propagate coherently; it is reflected back.

At these special frequencies, a bandgap opens: waves cannot propagate at all.

### Band Diagram

For periodic structures, one can compute the dispersion relation $\omega(k)$ for a range of wavenumbers within the first Brillouin zone. Due to periodicity, the dispersion relation is periodic in $k$-space, and it suffices to consider $k \in [-\pi/d, \pi/d]$.

Unlike a homogeneous medium (where $\omega = v k$ is a straight line), the periodic structure has a banded structure: the $\omega(k)$ curve consists of several branches, separated by bandgaps (frequency ranges with no real solution for $k$).

A **phononic bandgap** is a range of frequencies $[\omega_1, \omega_2]$ where no propagating modes exist. Waves at these frequencies are evanescent (decay exponentially with distance) rather than propagating.

The width of the bandgap depends on the impedance contrast: a larger difference between $Z_1$ and $Z_2$ yields a wider bandgap.

---

## Local Resonance Metamaterials

### Resonance-Based Bandgaps

A different mechanism for creating bandgaps is local resonance. Consider a host material with embedded resonators (small masses attached to springs, or air cavities in a solid matrix). If the resonator frequency matches an acoustic frequency, the resonator absorbs energy from the wave, preventing propagation.

This mechanism can create bandgaps even when the lattice is non-periodic or the scale is much smaller than the acoustic wavelength. This is the basis of acoustic metamaterials.

### Negative Effective Mass and Bulk Modulus

A striking feature of resonance-based metamaterials is that they can exhibit negative mass density $\rho_{\text{eff}}$ and negative bulk modulus $K_{\text{eff}}$ simultaneously in certain frequency ranges.

This violates intuition: a material with negative mass? Yet it is mathematically rigorous. Consider a composite with mass $m$ resonators at frequency $\omega_0$ embedded in a host. The effective impedance includes a frequency-dependent term:

$$\rho_{\text{eff}}(\omega) = \rho_0 \left(1 - \frac{\omega_p^2}{\omega(\omega + i\gamma)}\right)$$

where $\omega_p$ is the plasma frequency of the resonators, and $\gamma$ is damping.

For $\omega < \omega_p$ and $\gamma \to 0$, we have $\rho_{\text{eff}} < 0$: negative mass.

Negative mass materials exhibit anomalous behavior:
- Phase velocity and group velocity point in opposite directions
- Refraction at a boundary bends waves to the same side of the normal (negative index of refraction)
- Wave packets move backward relative to their phase fronts

---

## Acoustic Cloaking and Transformation Acoustics

### Transformation Method

Building on transformation optics (a technique for designing photonic cloaks), Guenneau and colleagues developed transformation acoustics. The idea: use coordinate transformations to design materials with spatially-varying (inhomogeneous) density and modulus that guide waves around a hidden region.

A cloak requires:
$$\rho_{\text{eff}}(r) = \rho_0 \frac{r_o^2}{(r_o - r_i)^2}$$
$$K_{\text{eff}}(r) = K_0 \frac{(r_o - r_i)^2}{r_o^2}$$

(for a spherical cloak, inner radius $r_i$, outer radius $r_o$.)

These material properties can be approximated using phononic metamaterials with spatially varying resonator properties.

### Practical Cloaking

True broadband cloaking is difficult (requires continuous material variation with frequency), but narrow-band cloaking (over a limited frequency range) has been demonstrated. Recent experiments have cloaked acoustic waves in 2D and 3D, achieving substantial wave redirection.

---

## Topological Phononic Crystals

### Berry Phase and Topological Band Structure

Recent advances in phononic crystals exploit topological properties of the band structure. Just as electrons in a quantum Hall state have topological quantum numbers protecting edge states, phononic systems can exhibit topological bands protected by symmetry.

A key concept is the Berry phase: as a band parameter (say, the wavenumber $k$) is varied around a closed loop in the Brillouin zone, the eigenstate accumulates geometric phase. This Berry phase is a topological invariant that cannot change continuously (it changes by integer multiples of $2\pi$).

Topological phononic bands are robust: they are protected against disorder and defects that would otherwise scatter waves. Edge modes in topological phononic crystals can propagate unimpeded along defects or boundaries.

---

## Connection to Phonon-Exflation Framework

Acoustic metamaterials and phononic crystals provide powerful models for how geometric structure controls wave propagation and particle excitation:

1. **Bandgaps as mass generation**: In phononic crystals, Bragg scattering creates bandgaps—frequency ranges where propagating modes cease to exist. Analogously, in the Kaluza-Klein compactified universe (M4 x SU(3)), the geometry of the internal space (SU(3) metric) determines which frequencies are allowed for the Dirac spectrum. The gap between generations (e.g., electron vs muon mass) arises from a "bandgap" in the Dirac spectrum caused by geometric structure on SU(3).

2. **Local resonance and particle mass**: Resonance-based metamaterials use embedded oscillators to create bandgaps. In the phonon-exflation framework, the Dirac operator $D_K$ on SU(3) is a resonant system. Its eigenvalues (particle masses) are analogous to the resonant frequencies of the embedded oscillators. The deformation metric (Jensen parameter $s$) shifts these resonances, changing particle masses—just as changing the spring stiffness of embedded resonators shifts the bandgap frequency.

3. **Negative refraction and emergent forces**: A striking feature of metamaterials is negative refractive index—waves bend "backward." In condensed-matter analogs of gravity (Volovik's framework), such anomalous dispersion can emerge from the background superfluid structure. The curvature of the Dirac band structure (on SU(3)) determines effective "forces" experienced by excitations (fermions). Negative curvature regions would be analogous to negative refraction in acoustics.

4. **Topological protection and particle stability**: Topological phononic bands are robust against disorder. In the Standard Model, symmetry principles (gauge invariance) protect the stability of elementary particles. The phonon-exflation framework interprets these symmetries as geometric: SU(3) internal symmetry emerges from the geometric structure of the compactified space. Topological protection suggests why particles are stable—they are protected by the topology of the Dirac band structure.

5. **Wave propagation in inhomogeneous media**: Transformation acoustics shows how spatially-varying material properties (density, modulus) guide and reshape wave propagation. In phonon-exflation, the spacetime metric is a spatially-varying inhomogeneous "medium" (from the 4D perspective). The Friedmann equations describe how waves (phonons, particles) propagate and interact in this curved spacetime. The effective potential $V_{\text{eff}}(s)$ determines the preferred deformation—the "material property"—at any cosmological epoch.

6. **Spectral engineering**: Phononic crystals are designed to achieve desired spectral properties (bandgaps, dispersion relations). In the phonon-exflation framework, the spectral action principle directly optimizes the spectral properties of the Dirac operator. The effective potential $V_{\text{eff}}(s)$ is derived by integrating over all spectral contributions, weighted by a smooth cutoff function. This is spectral engineering applied to the fundamental spectrum of particle physics.

---

## Key Equations Summary

| Concept | Equation | Meaning |
|---------|----------|---------|
| Bragg condition | $\lambda = 2d/n$ | Resonant wavelength for Bragg scattering |
| Impedance contrast | $Z = \rho v$ | Acoustic impedance (product of density and speed) |
| Effective mass (resonance) | $\rho_{\text{eff}}(\omega) = \rho_0 \left(1 - \frac{\omega_p^2}{\omega(\omega + i\gamma)}\right)$ | Frequency-dependent effective density |
| Negative refractive index | $n_{\text{eff}} = \sqrt{\mu_r \epsilon_r} < 0$ (acoustic analogs: $\rho_{\text{eff}} < 0, K_{\text{eff}} < 0$) | Backward propagation of energy |
| Acoustic cloak density | $\rho_{\text{eff}}(r) = \rho_0 \frac{r_o^2}{(r_o - r_i)^2}$ | Radial dependence for spherical cloak |
| Berry phase | $\gamma_n = i \oint \langle n(\vec{k}) | \nabla_{\vec{k}} n(\vec{k}) \rangle d\vec{k}$ | Topological phase accumulated around Brillouin zone loop |
| Bandgap width | $\Delta \omega \propto |Z_1 - Z_2| / \bar{Z}$ | Scales with impedance contrast |

---

## Critical Assessment

**What holds up**:
- Bragg scattering and bandgap formation are well-understood and experimentally verified
- Negative refractive index metamaterials have been demonstrated at acoustic, elastic, and electromagnetic frequencies
- Topological phononic bands are observed in recent experiments
- Acoustic metamaterials enable design of materials with prescribed dynamic properties

**What is challenging**:
- Broadband cloaking is difficult; most demonstrations are narrowband
- Losses in the material (damping, absorption) degrade device performance
- Scaling to subwavelength regimes requires fabrication at nanoscale
- Complex material properties (spatial variation, frequency dependence) are difficult to achieve in practice

**Ahead of its time**:
- Insight that geometric structure controls spectral properties
- Application of topological concepts to phononic systems
- Transformation methods for designing wave-control devices

---

## Legacy and Modern Applications

Phononic metamaterials are now a major research area:

1. **Acoustic noise control**: Metamaterial barriers block sound more effectively than traditional absorbers
2. **Seismic metamaterials**: Underground structures designed to protect buildings from earthquakes
3. **Thermal transport control**: Phonon engineering for thermoelectric efficiency
4. **Phononics**: Phonon analogs of photonics, using phonons for computing and sensing

---

## References

1. Craster, R.V. & Guenneau, S. (eds.) (2013). "Acoustic metamaterials: Negative refraction, imaging, lensing and cloaking." Springer.
2. Liu, Z., Zhang, X., Mao, Y., et al. (2000). "Locally resonant sonic materials." Science 289: 1734-1736.
3. Cummer, S.A. & Schurig, D. (2007). "One path to acoustic cloaking." New Journal of Physics 9: 45.
4. Pendry, J.B., Holden, A.J., Stewart, W.J., & Youngs, I. (1996). "Extremely low frequency plasmons in metallic mesostructures." Physical Review Letters 76: 4773.
5. Hussein, M.I., Maldovan, M., Lobkovsky, A.E., & Thomas, S.L. (2006). "Simultaneous reduction of phonon and photon thermal conductivity via selective scattering." Applied Physics Letters 89: 173104.
6. Volovik, G.E. (2003). "The universe in a helium droplet." Oxford University Press.
