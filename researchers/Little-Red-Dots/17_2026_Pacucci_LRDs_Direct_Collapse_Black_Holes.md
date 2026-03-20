# The Little Red Dots Are Direct Collapse Black Holes

**Author(s):** Fabio Pacucci, Andrea Ferrara, Dale D. Kocevski
**Year:** 2026
**Journal:** Submitted (preprint)
**arXiv:** 2601.14368
**Submitted:** January 20, 2026

---

## Abstract

Pacucci, Ferrara & Kocevski propose that the "little red dots" discovered by JWST are
accreting Direct Collapse Black Holes (DCBHs). Using radiation-hydrodynamic simulations,
they demonstrate that DCBHs accreting from pristine atomic-cooling haloes naturally reproduce
the observed spectral features of LRDs: the V-shaped SED, broad Balmer emission, Balmer
break/absorption features, weak X-ray emission, and compactness. The model predicts accretion
episodes lasting $> 100$ Myr per DCBH, explaining the abundance of LRDs across the redshift
range $z \sim 4$--$8$. The authors argue that LRDs represent the long-sought observational
signature of massive black hole seed formation occurring in pristine atomic-cooling haloes,
and that DCBH formation was widespread in the early universe. The paper ties together
theoretical DCBH physics, radiation-hydrodynamic modeling, and the observational LRD dataset
into a unified interpretive framework.

---

## Historical Context

### The Black Hole Seed Problem

The existence of quasars with $M_{\rm BH} > 10^9 M_\odot$ at $z > 6$ (Fan et al. 2006;
Banados et al. 2018) poses a fundamental challenge to black hole growth models. Starting from
a "light" Population III remnant seed of $M_0 \sim 10^2 M_\odot$, continuous Eddington-limited
accretion over 700 Myr yields:

$$M_{\rm BH}(t) = M_0 \exp\!\left(\frac{(1-\epsilon)}{\epsilon} \frac{t}{t_{\rm Edd}}\right)$$

where $\epsilon \sim 0.1$ is the radiative efficiency and $t_{\rm Edd} \approx 45$ Myr is the
Eddington time. For $t = 700$ Myr, $M/M_0 \sim e^{15.5} \sim 5 \times 10^6$ -- so a $100
M_\odot$ seed grows to only $5 \times 10^8 M_\odot$, barely enough even with continuous
Eddington-rate accretion. Any interruption drops the final mass below observed values.

Heavy seeding via DCBHs starts from $M_0 \sim 10^5$--$10^6 M_\odot$, giving a 3--4 dex head
start and allowing modest sub-Eddington growth to reach quasar masses. The DCBH scenario thus
solves the seed problem by construction -- IF DCBH formation is sufficiently common.

### Pacucci and Ferrara's Previous Theoretical Work

Pacucci and Ferrara have been leading theoretical architects of the DCBH paradigm since the
2010s. Pacucci et al. (2015, 2016, 2017) showed that accreting DCBHs would be bright in the
infrared and detectable by JWST, that they would appear "compact" and "red" due to the dense
Compton-thick gas envelope, and that their broad emission lines would mimic classical AGN but
with higher Eddington ratios. When JWST discovered LRDs in 2022--2024, these predictions were
immediately recognized as potentially matching observed properties.

Kocevski et al. (from his role at the Space Telescope Science Institute) provided the
observational LRD census from CEERS and other legacy fields, cataloguing hundreds of objects
and characterizing their SEDs. This paper unites the theoretical (Pacucci, Ferrara) and
observational (Kocevski) perspectives.

---

## Key Arguments and Derivations

### 1. The DCBH Accretion Model

A DCBH in a pristine atomic-cooling halo accretes from a reservoir of nearly pure
hydrogen+helium gas. The accretion rate in the early phase is set by the infall from the
halo:

$$\dot{M}_{\rm acc} \approx \frac{M_{\rm halo}}{t_{\rm ff}} \sim \frac{10^8 M_\odot}{30 \, \rm Myr}
\sim 3 \, M_\odot \, \rm yr^{-1}$$

where $t_{\rm ff}$ is the halo free-fall time at $z \sim 6$. This significantly exceeds the
Eddington accretion rate:

$$\dot{M}_{\rm Edd} = \frac{L_{\rm Edd}}{\epsilon c^2} = \frac{4\pi G M_{\rm BH} m_p}{\epsilon \sigma_T c}
\approx 2 \times 10^{-3} \left(\frac{M_{\rm BH}}{10^5 M_\odot}\right) M_\odot \, \rm yr^{-1}$$

so early-phase DCBHs are super-Eddington by factors of $10^3$ or more. In the super-Eddington
regime, standard thin-disk accretion breaks down. The authors use a slim-disk + outflow model
where the photon trapping radius:

$$r_{\rm trap} = \frac{\dot{M}}{\dot{M}_{\rm Edd}} r_S$$

(with $r_S = 2GM/c^2$ the Schwarzschild radius) grows to stellar scales, trapping most
radiation and reducing the effective luminosity to a few times $L_{\rm Edd}$. The result is
an object that looks sub-Eddington photometrically but is actually super-Eddington in mass
accretion rate.

### 2. Spectral Predictions from Radiation-Hydrodynamics

The authors use the radiation-hydrodynamic code GAMESH (adapted from previous work) to follow
the coupled evolution of the accreting DCBH, its surrounding gas, and the emergent radiation
field. Key model ingredients:

- Compton-thick column density: $N_H \sim 10^{24}$--$10^{25}$ cm$^{-2}$ surrounding the nucleus
- Temperature structure: hot corona ($T \sim 10^9$ K) + warm scattering layer ($T \sim 10^4$ K)
- Geometry: spherical inner cocoon + disk-wind outflow

The emergent spectrum has:

$$F_\nu(\nu) \propto \begin{cases}
\nu^{1/3} & \text{UV-optical (disk)} \\
\nu^{0} & \text{near-IR (scattered + warm dust)} \\
e^{-\tau_{\rm ff}(\nu)} & \text{soft X-ray (suppressed)}
\end{cases}$$

The V-shaped SED (blue UV-optical peak + red near-IR rise) emerges naturally from this model
without invoking a coincidental combination of AGN and stellar components.

Broad Balmer emission arises from the warm scattering layer. The column of warm gas produces
Balmer absorption (high $n$ Lyman series photons absorbed before escaping) and a Balmer break
in continuum, consistent with the Balmer absorption features seen in many LRD spectra by
Kocevski et al. (2023) and Greene et al. (2024).

### 3. Duration of the LRD Phase

The accretion episode in the simulation lasts $\sim 100$--$300$ Myr before the growing black
hole feedback disrupts the surrounding cocoon. During this time, the DCBH appears as an LRD.
The fraction of cosmic time between $z \sim 4$ and $z \sim 8$ that corresponds to 100--300 Myr
intervals is roughly 30--50%, consistent with LRDs being a common but not ubiquitous class
at those redshifts. The duty cycle:

$$f_{\rm duty} = \frac{t_{\rm LRD}}{t_{\rm Hubble}(z)} \sim \frac{100 \, \rm Myr}{500 \, \rm Myr} \sim 0.2$$

combined with the inferred DCBH formation rate per comoving volume gives a number density
prediction consistent (within a factor 3) with the observed LRD census.

### 4. X-ray and Radio Suppression

In the DCBH model, the Compton-thick cocoon absorbs essentially all soft X-rays:

$$\tau_X(E) = N_H \sigma_{ph}(E) \approx N_H \cdot 2 \times 10^{-22} \left(\frac{E}{1 \, \rm keV}
\right)^{-3} \, \rm cm^2$$

For $N_H = 10^{24}$ cm$^{-2}$, $\tau_X(1 \, \rm keV) \approx 200$ -- i.e., soft X-rays are
suppressed by $e^{-200}$, essentially absent. Hard X-rays above 10 keV escape more easily, but
JWST-detected LRDs are far enough away that current X-ray telescopes cannot detect them at
those energies. Radio: free-free absorption from the dense ionized inner region provides
$\tau_{\rm ff}(\nu) \gg 1$ at GHz frequencies (consistent with Rusakov et al. 2025 analysis).

---

## Key Results

1. Radiation-hydrodynamic simulations show DCBHs accreting from pristine haloes naturally
   produce V-shaped SEDs, broad Balmer emission, and Balmer absorption -- matching LRD spectra.
2. Super-Eddington mass accretion ($\dot{M}/\dot{M}_{\rm Edd} \sim 10^3$) with photon trapping
   keeps the apparent luminosity near $L_{\rm Edd}$ while hiding the true accretion rate.
3. Compton-thick columns ($N_H \sim 10^{24}$--$10^{25}$ cm$^{-2}$) suppress X-ray and radio
   emission by orders of magnitude, explaining multi-wavelength non-detections.
4. LRD phase duration: 100--300 Myr per DCBH, producing duty cycles consistent with observed
   LRD number counts at $z \sim 4$--$8$.
5. DCBH formation was widespread in the early universe -- LRDs are the long-sought
   observational signature of massive black hole seed formation.

---

## Impact and Legacy

This paper provides the most complete theoretical framework for LRDs as DCBHs to date,
combining radiation-hydrodynamic simulations with detailed spectral predictions. Together
with Baggen et al. (2026, arXiv:2602.02702), which provides the observational environmental
evidence, and Rusakov et al. (2025, arXiv:2503.16595), which revises the virial mass estimates
downward into the DCBH range, this paper anchors one of the three leading interpretive
frameworks for LRDs at the start of 2026.

The paper's specific, quantitative predictions (SED shape, Balmer absorption depth, X-ray
flux upper limits, LRD duty cycle) are testable with next-generation observatories including
Athena (X-ray) and the ngVLA (radio), providing a roadmap for definitive discrimination
between the DCBH model and alternatives such as compact star-forming galaxies or
electron-scattering-broadened low-mass AGN.

---

## Connection to Phonon-Exflation Framework

The DCBH model requires the existence of pristine atomic-cooling haloes ($T_{\rm vir}
\gtrsim 10^4$ K, no metals, no $H_2$) as the birth environments of the first massive black
holes. In the phonon-exflation framework, the spectral action at high redshift ($z \sim 5$--$8$,
corresponding to tau > 0.3 in the model's parametrization) governs the effective field content
of the early universe. The requirement of pristine gas (zero metallicity) at DCBH formation
sites is a constraint on early nucleosynthesis and stellar feedback -- processes that in
principle depend on the particle mass spectrum set by the Dirac operator $D_K$.

The super-Eddington accretion phase ($\dot{M}/\dot{M}_{\rm Edd} \gg 1$) and photon trapping
raise questions about whether the effective gravitational constant in the early universe
(which would be modified by any rolling of the compactification radius in phonon-exflation)
alters the Eddington threshold and thus the black hole growth history. Since V_spec has been
shown monotone (killing rolling quintessence), this would require a mechanism outside the
perturbative sector -- consistent with the P2b rescue route (finite-density spectral action)
being the primary remaining theoretical option.
