# Superluminal Correlations in Ensembles of Optical Phase Singularities

**Authors**: T. Bucher, A. Gorlach, A. Niedermayr, Q. Yan, H. Nahari, K. Wang, R. Ruimy, Y. Adiv, M. Yannai, T. L. Abudi, E. Janzen, C. Spaegele, C. Roques-Carmes, J. H. Edgar, F. H. L. Koppens, G. M. Vanacore, H. H. Sheinfux, S. Tsesses, I. Kaminer

**arXiv**: 2509.17675 (2025)
**Pages**: 20

---

## Abstract

Phase singularities -- points carrying quantized topological charge -- are universal features found across diverse wave systems from superfluids and superconductors to acoustic and optical fields. Ensembles of such singularities exhibit distance correlations resembling particles in liquids, extensively studied for their role in exotic material phases. In contrast, the full correlations in phase-space that govern the system evolution have remained unexplored and experimentally inaccessible. Here, the authors directly measure the ultrafast dynamics of optical singularity ensembles, capturing their full phase-space correlations, presenting the joint distance-velocity distribution. Their observations reveal a breakdown of the particle-singularity analogy: phase singularities exhibit acceleration to unbounded velocities before annihilation, indicated by measurements of velocities exceeding the speed of light. These superluminal velocities are paradoxically amplified by the slow group velocity of hyperbolic phonon polaritons in their material platform, hexagonal boron nitride (hBN) membranes. They demonstrate these phenomena using combined hardware and algorithmic advances in ultrafast electron microscopy, achieving spatial and temporal resolutions each an order of magnitude below the polaritonic wavelength and cycle period.

---

## 1. Introduction (pp. 1-3)

Singularities arise in nearly every branch of physics: dislocations in crystals, flux quanta in superconductors, vortex cores in fluid flows, and quantized vortices in superfluids. A strong analogy exists between phase singularities and interacting particles -- singularities carry topological charge +/-1 (characterized by +/-2pi phase winding), and a singularity annihilates only upon encountering another of opposite charge, much like particle-antiparticle pairs. Higher integer charges are possible but typically unstable.

Previous studies focused on distance-correlation functions in singularity ensembles, following Berry's foundational work on their statistical properties (Berry 1978). Extensive theoretical efforts analyzed the dynamics of singularity ensembles, including prediction of velocity distributions (Berry & Dennis 2001). However, experimental observation requires sub-cycle, sub-wavelength resolution -- a significant technical challenge.

Theory has long predicted that optical singularities can exhibit superluminal motion, particularly near creation or annihilation events, where velocities can become unbounded. This paper provides the first direct experimental observation of these dynamics.

---

## 2. Deep Sub-Wavelength and Deep Sub-Cycle Mapping (pp. 3-4)

### Experimental Platform

- **Material**: Hexagonal boron nitride (hBN) thin flake supporting hyperbolic phonon-polariton (PhP) wavepackets
- **Technique**: Ultrafast transmission electron microscope (UTEM) with photon-induced near-field electron microscopy (PINEM) extended to phase resolution via free-electron Ramsey imaging (FERI)
- **Resolution achieved**:
  - Spatial: 20 nm ~ lambda_PhP / 30 (x350 below free-space wavelength)
  - Temporal: 3 fs ~ T/8 (deep sub-cycle)
  - Field of view: 21 x 21 um^2
  - Total measurement duration: > 800 fs

### Why hBN?

Hyperbolic dispersion of PhPs provides:
- Sub-wavelength confinement: lambda_PhP ~ lambda_0 / 11 ~ 630 nm
- Slow group velocity: > 100x slower than c
- Remarkably low optical losses (lifetime > 1 ps for isotopically pure hBN)
- Phase-to-group velocity ratio: v_ph / v_g ~ 12 +/- 1

### Experimental Scheme

A femtosecond laser pulse (1030 nm, ~270 fs, 1 MHz) is split into three paths:
1. Upconverted to UV (266 nm) for electron pulse emission
2. Down-converted to mid-IR (~7 um) for reference electron modulation (PELM)
3. Down-converted to mid-IR for PhP excitation in the hBN sample

Two independent delay stages control: (i) pump-probe delay Delta_t for group dynamics, (ii) sub-cycle phase delay Delta_phi between reference and sample interactions.

---

## 3. Superluminal Singularity Annihilation (pp. 5-6)

### Key Physics

As opposite-charged singularities approach each other, their paths in space-time form a continuous curve at the annihilation point. This continuity forces acceleration to unbounded velocities right before annihilation. This is a **mathematical consequence of phase continuity**, not a violation of physical laws: phase singularities carry zero intensity and can "move" superluminally without energy or information transmission.

The phenomenon is not unique to optics. Similar pre-annihilation acceleration is observed in:
- Superfluids (vortex-antivortex pairs)
- Superconductors (magnetic vortex annihilation)
- Fluid dynamics (vortex ring collisions)

In all these other platforms, velocities remained subluminal. The hBN PhP platform is the first to observe superluminal singularity motion directly.

### Dataset

- 285 phase-resolved frames (each from 15 sub-cycle frames)
- ~50 singularities tracked per frame
- Entire sample area (21 x 21 um^2) monitored over 800 ps

---

## 4. Distance and Velocity Correlations (pp. 6-8)

### Distance Correlations

Same-charge g_{+|+}(R) = g_{-|-}(R) and opposite-charge g_{+|-}(R) = g_{-|+}(R) correlation functions measured experimentally match the Gaussian random wave model predictions. The distance correlations resemble those of particles in liquids (spatial short-range order from interactions).

### Velocity Distribution -- Breakdown of Particle Analogy

The velocity distribution of phase singularities:

$$P_{\pm}(|v|) = \frac{8\pi^2 \langle v \rangle^2 |v|}{(\pi^2 |v|^2 + 4\langle v \rangle^2)^2}$$

(Eq. 4, analytically derived from Berry & Dennis 2001)

**Key experimental result**: The average singularity velocity is:

> **<v> = 3.12 x 10^8 m/s ~ 1.04 c**

This is in close agreement with the theoretical prediction:

> <v> = c * (pi / sqrt(2)) * (Delta_k / k) / sqrt(1 + (Delta_k / k)^2)

where Delta_k / k ~ (v_ph * Delta_lambda) / (v_g * lambda_0). The slow group velocity of hBN PhPs (v_ph / v_g ~ 12) amplifies the effective spectral spread, pushing the average singularity velocity to ~c.

### Comparison: hBN vs Free Space

| Property | hBN PhPs | Free space |
|:---------|:---------|:-----------|
| v_ph / v_g | ~12 | 1 |
| <v> | ~1.04 c | ~0.1 c |
| Fraction > c | **29%** | 0.4% |

The PhP platform makes superluminal events 70x more frequent.

---

## 5. Full Phase-Space Correlations (pp. 8-10)

### Velocity Pair Correlations

The relative velocity correlation between singularity pairs:

$$P_{\sigma|\sigma'}(v) = \frac{1}{N_{\sigma\sigma'}} \langle \sum_{a \in \sigma, b \in \sigma'} \delta(v - (\mathbf{v}_a - \mathbf{v}_b) \cdot \hat{\mathbf{R}}_{ab}) \rangle$$

(Eq. 5)

where sigma, sigma' in {+, -} specify charge types, R_hat_{ab} is the unit vector along the connecting line.

For large enough sample sizes, correlations become charge-independent: P_{+|+}(v) = P_{+|-}(v).

### Joint Distance-Velocity Distribution

The full phase-space correlation:

$$P_{\sigma|\sigma'}(v, R) = \frac{1}{N_{\sigma\sigma'}(R)} \langle \sum_{a \in \sigma, b \in \sigma'} \delta(v - (\mathbf{v}_a - \mathbf{v}_b) \cdot \hat{\mathbf{R}}_{ab}) \delta(R - |\mathbf{r}_a - \mathbf{r}_b|) \rangle$$

(Eq. 6)

**Key findings from P(v, R)**:
- At small distances (R < lambda_0): opposite-charge singularities (P_{+|-}) are more common and exhibit higher velocities (acceleration before annihilation/after creation)
- Same-charge singularities (P_{+|+}) are less likely at small distances (instability of higher charges)
- At larger distances: narrower velocity distributions (no creation/annihilation events)
- Maximum observable velocity is limited by microscopy resolution, not by the material

Theory-experiment agreement is good across the full (v, R) phase space.

---

## 6. Conclusion and Outlook (p. 10)

### Main Results
1. First experimental observation of dynamical correlations among ensembles of optical singularities using ultrafast electron microscopy
2. Deep sub-cycle (3 fs ~ T/8) creation/annihilation events captured with deep sub-wavelength resolution (20 nm ~ lambda_PhP / 30)
3. Long-standing predictions about singularity velocity distributions and unbounded velocities confirmed
4. Joint distance-velocity distributions reveal acceleration of opposite-charge singularities before annihilation

### Connections to Superoscillations
The unbounded singularity velocities are a direct manifestation of superoscillatory field gradients undergoing temporal evolution. Conversely, rapid creation/annihilation of singularities inherently generate superoscillations.

### Future Directions
- Extension to other 2D materials and heterostructures with tunable optical properties
- Materials with strong nonlinear responses could break the Gaussian random wave model
- Free electrons can be modified through interactions with singularities, generating novel electronic states
- Analytical approaches could address the "bee-swarm" effect in electron cryomicroscopy

---

## Methods Summary (pp. 11-13)

### UTEM Setup
- JEOL JEM-2100 Plus with LaB6 gun at 200 kV
- Low-magnification mode (objective lens off, convergence < 1 mrad)
- Post-column EELS (0.1 eV dispersion)
- Gatan K2 Summit direct-detection camera
- Zero-loss peak FWHM: ~1.4 eV

### Laser System
- 40 W, 1030 nm, ~270 fs, 1 MHz (Carbide laser)
- Three optical paths: UV cathode excitation, mid-IR PELM reference, mid-IR sample excitation
- Mid-IR: TM-polarized, focused to ~100 um (sample, 4-12 mW) and ~500 um (reference, 4-20 mW)

### Data Acquisition
- 285 raw frames over ~855 fs with 3 fs sub-cycle sampling
- Each reconstruction from 15 sequential raw measurements (14-frame overlap)
- Semi-automated drift correction via affine transforms
- Linear interpolation to 0.2 fs time steps

### Sample
- Isotopically pure h11BN crystals, mechanically exfoliated
- Thickness: 40-50 nm (EELS log-ratio analysis)
- On 20 nm SiN membranes (Norcada)
- Field of view: 21 x 21 um^2
- Sharp flake edges as near-field couplers for PhP launching

### Singularity Detection & Tracking
- Phase winding evaluation around pixel loops
- Connected-component clustering for centroids
- Hungarian algorithm for inter-frame association
- Velocities from finite differences along tracks

---

## References

1. Embon et al., Nature Communications 8, 85 (2017) -- superconducting vortex dynamics
2. Fiorino & Elsberry, J. Atmos. Sci. 46, 975-990 (1989) -- tropical cyclone vortices
3. Sachkou et al., Science 366, 1480-1485 (2019) -- superfluid vortices on silicon chip
4. Bliokh et al., J. Optics 25, 103001 (2023) -- structured waves roadmap
5. Dennis et al., Nature Physics 6, 118-121 (2010) -- optical vortex knots
6. Berry, J. Phys. A 11, 27 (1978) -- wavefront dislocation statistics
7. De Angelis et al., PRL 117, 093901 (2016) -- phase singularity spatial distribution
8. Berry & Dennis, Proc. Roy. Soc. A 456, 2059-2079 (2001) -- phase singularities in random waves
9. Hansen & McDonald, Theory of Simple Liquids (Academic Press, 2013)
10. Toulouse & Kleman, J. Phys. Lett. 37.6 (1976) -- defect classification
11. Blatter et al., Rev. Mod. Phys. 66, 1125-1388 (1994) -- vortices in HTS
12. Drori et al., Science 381, 193-198 (2023) -- quantum vortices of photons
13. Sugic et al., Nature Communications 12, 6785 (2021) -- particle-like topologies in light
14. Indebetouw, J. Mod. Opt. 40, 73-87 (1993) -- optical vortex propagation
15. Freund, Opt. Commun. 181, 19-33 (2000) -- optical vortex trajectories
16. Maleev & Swartzlander, J. Opt. Soc. Am. B 20, 1169-1176 (2003) -- composite vortices
17. Bekshaev et al., Opt. Commun. 397, 72-83 (2017) -- singular skeleton evolution
18. Li et al., Nature Communications 6, 7507 (2015) -- hyperbolic PhPs in hBN
19. Yoxall et al., Nature Photonics 9, 674-678 (2015) -- ultraslow PhP propagation
20. Caldwell et al., Nature Reviews Materials 4, 552-567 (2019) -- photonics with hBN
21. Kurman et al., Science 372, 1181-1186 (2021) -- spatiotemporal 2D polariton imaging
22. Giles et al., Nature Materials 17, 134-139 (2018) -- ultralow-loss polaritons in isotopic BN
23. Barwick et al., Nature 462, 902 (2009) -- PINEM
24. Piazza et al., Nature Communications 6, 6407 (2015) -- plasmonic near-field quantization
25. Feist et al., Nature 521, 200-203 (2015) -- quantum coherent optical phase modulation
26. Wang et al., Nature 582, 50-54 (2020) -- free electron-photonic cavity interaction
27. Kfir et al., Nature 582, 46-49 (2020) -- controlling free electrons with WGMs
28. Nabben et al., Nature 619, 63-67 (2023) -- attosecond electron microscopy
29. Bucher et al., Science Advances 9, eadi5729 (2023) -- FERI
30. Bucher et al., Nature Photonics 18, 809-815 (2024) -- coherently amplified ultrafast imaging
31. Gaida et al., Nature Photonics 18, 509-515 (2024) -- attosecond electron microscopy by homodyne
32. Poincare, J. Math. Pures Appl. 4(1), 167-244 (1885) -- hairy ball theorem origin
33. Nye & Berry, Proc. Roy. Soc. A 336, 165-190 (1974) -- dislocations in wave trains
34-81. [See original paper for remaining references]
