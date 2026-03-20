# Little Red Dots: The Assembly of Early SMBHs in the JWST Era

**Authors:** Fabio Pacucci, Andrea Ferrara

**Year:** 2026

**Journal:** *Frontiers in Astronomy and Space Sciences*, published February 2026

---

## Abstract

The James Webb Space Telescope has revolutionized our understanding of early supermassive black hole (SMBH) formation, revealing a population of compact, dust-reddened sources at z~4-8 with inferred black hole masses $M_{\text{BH}} \sim 10^8-10^{10} M_{\odot}$. These "Little Red Dots" pose a fundamental challenge to hierarchical black hole assembly scenarios in the Lambda-CDM paradigm. In this comprehensive review, we synthesize observations from NIRSpec, NIRCam, X-ray stacking, far-IR, and radio surveys. We discuss competing interpretations: obscured super-Eddington accretion on stellar-mass seeds, direct-collapse black hole formation, primordial black hole capture, and exotic mechanisms. We present the phenomenology of black hole stars (gas-embedded, thermalized envelopes), the role of rapid gas assembly in dense halos, the implications for reionization feedback, and outstanding questions for the next decade. This review updates and supersedes the Maiolino et al. (2023) Nature Reviews Physics overview with new data through early 2026.

---

## Historical Context

The discovery of Little Red Dots in early JWST data (November 2022 onwards) initiated a paradigm challenge to standard astrophysics. In traditional Lambda-CDM, supermassive black holes grow via a two-phase process:

1. **Seed Formation** (z ~ 20-50): Small black holes ($M_{\text{seed}} \sim 10^3-10^5 M_{\odot}$) form either from stellar mass collapse (Schwarzschild BHs from Pop III stars, ~100 M_sun) or from direct collapse of pristine gas clouds (direct-collapse black holes, DCBH, ~10^4-10^5 M_sun).

2. **Hierarchical Mergers and Accretion** (z ~ 6-0): Seeds grow via black hole mergers (mergers of host galaxies) and gas accretion (feeding via gas infall during galaxy mergers and secular evolution).

The growth rate from seed to $M_{\text{BH}} = 10^9 M_{\odot}$ at z~6 is governed by:

$$M_{\text{BH}}(z) = M_{\text{seed}} \times \left( 1 + z_{\text{seed}} \right) / \left( 1 + z \right) \times e^{\int_z^{z_{\text{seed}}} \lambda_{\text{edd}} dt}$$

where $\lambda_{\text{edd}} = \dot{M} / \dot{M}_{\text{Edd}}$ is the Eddington ratio. For a black hole that never exceeds $\lambda_{\text{edd}} = 1$, the growth is exponential with an e-folding timescale:

$$t_{\text{double}} = \frac{H_0}{(\lambda_{\text{edd}} - 1) \ln 2} \approx 400 \, \text{Myr} \quad [\lambda_{\text{edd}} = 0.3]$$

The time available from the redshift of first stellar populations (z~20, t~50 Myr) to z=6 (t~1 Gyr) is only ~950 Myr. To grow from $M_{\text{seed}} = 10^3 M_{\odot}$ to $M_{\text{BH}} = 10^9 M_{\odot}$ requires ~20 e-folding times, or sustained $\lambda_{\text{edd}} > 10$-20 (super-Eddington accretion) for the entire epoch.

JWST observations show that LRDs with $M_{\text{BH}} \sim 10^8-10^{10} M_{\odot}$ appear at z ~ 4-8 in abundances ~20% of the z>4 population. This is the "Black Hole Assembly Crisis": standard models predict far fewer, far less massive black holes at these epochs. Either:

1. Seeds form earlier and more efficiently (primordial BH, or enhanced DCBH formation), or
2. Accretion proceeds faster than standard models allow (super-Eddington flows with reduced radiative efficiency), or
3. Dark matter physics enables denser halo collapse, accelerating gas assembly (beyond-LCDM scenarios).

The Pacucci & Ferrara (2026) review consolidates the observational and theoretical landscape, providing the first comprehensive synthesis that addresses all three branches.

---

## Key Arguments and Derivations

### LRD Phenomenology: The Black Hole Star Picture

A Black Hole Star (BHS) is defined as a system where:
- A central SMBH of mass $M_{\text{BH}}$ radiates at luminosity $L_{AGN}$.
- This energy is absorbed by a surrounding envelope of neutral and ionized gas + dust.
- The envelope reaches hydrostatic equilibrium, with radiation pressure balancing gravity.
- The photosphere temperature $T_{\text{eff}}$ is determined by the radiated luminosity and the envelope's effective radius:

$$T_{\text{eff}} = \left( \frac{L_{AGN}}{4\pi \sigma_B R_{\text{env}}^2} \right)^{1/4}$$

For a typical LRD:
- $L_{AGN} = 10^{45}$ erg/s
- $R_{\text{env}} \sim 10^{15}$ cm (resolving limit of JWST, ~1 kpc at z~6)
- $T_{\text{eff}} \sim 5000$ K

This temperature is *much cooler* than a bare accretion disk (T ~ 10^5 K), explaining the optical reddening. The envelope acts as a blanket, reducing the observed UV-optical flux while trapping energy in the dust.

Spectral energy distribution in a BHS:

$$F_\nu \propto \begin{cases}
\nu^{1/3} & \nu < \nu_{\text{Rayleigh-Jeans}} \\
B_\nu(T_{\text{eff}}) & \nu_{\text{Rayleigh-Jeans}} < \nu < \nu_{\text{peak}} \\
\text{power law} & \nu > \nu_{\text{peak}}
\end{cases}$$

This multi-component SED is well-fit by the de Graaff et al. (2025) sample and explains why LRDs appear "red"—the optical/NIR represents the Rayleigh-Jeans tail of a cool photosphere.

### Accretion Rate Diagnostics and Super-Eddington Regimes

For a black hole accreting at rate $\dot{M}$, the accretion luminosity is:

$$L_{\text{acc}} = \epsilon \dot{M} c^2$$

where $\epsilon \sim 0.1$ for thin disks, $\epsilon \sim 0.01-0.1$ for advection-dominated flows (ADF), and $\epsilon \sim 0.01$ for radiatively inefficient accretion (RIAF).

The Eddington luminosity is:

$$L_{\text{Edd}} = \frac{4\pi G M_{\text{BH}} m_p c}{\sigma_T} \approx 1.4 \times 10^{38} M_{\text{BH}} / M_{\odot} \, \text{erg/s}$$

The Eddington-limited mass accretion rate is:

$$\dot{M}_{\text{Edd}} = \frac{L_{\text{Edd}}}{\epsilon c^2}$$

For $\epsilon = 0.1$:
$$\dot{M}_{\text{Edd}} \approx 0.01 M_{\text{BH}} / M_{\odot} \, M_{\odot} \, \text{yr}^{-1}$$

The Eddington ratio is:

$$\lambda_{\text{Edd}} = \frac{\dot{M}}{\dot{M}_{\text{Edd}}}$$

Standard (optically thin) accretion has $\lambda_{\text{Edd}} \lesssim 0.3$. Super-Eddington accretion (common in LRDs) has $\lambda_{\text{Edd}} > 1$, sometimes reaching $\lambda_{\text{Edd}} \sim 10-100$ in the most extreme cases.

In super-Eddington flows, the standard thin-disk assumption (energy radiated locally at the radius where it is released) breaks down. Instead, most energy is advected inward and released closer to the event horizon, or trapped in the accretion flow, reducing the radiative efficiency:

$$\epsilon_{\text{ADF}} \sim \frac{\lambda_{\text{Edd}}^{-1}}{0.1}$$

This explains how LRDs can be optically/UV-bright but X-ray-faint: the X-ray production occurs deeper in the flow and is suppressed by the extreme super-Eddington geometry.

### Black Hole Mass Growth Timescales

The differential equation for SMBH mass growth is:

$$\frac{dM_{\text{BH}}}{dt} = \dot{M} = \lambda_{\text{Edd}} \dot{M}_{\text{Edd}} = \lambda_{\text{Edd}} \frac{L_{\text{Edd}}}{\epsilon c^2}$$

For constant $\lambda_{\text{Edd}}$:

$$\frac{dM_{\text{BH}}}{dt} = \lambda_{\text{Edd}} \frac{1.4 \times 10^{38}}{0.1 \times c^2} M_{\text{BH}} \propto \lambda_{\text{Edd}} M_{\text{BH}}$$

This is exponential growth:

$$M_{\text{BH}}(t) = M_{\text{seed}} \exp \left( \frac{\lambda_{\text{Edd}} H_0}{\ln 2} (1 - (1+z)^{-1/2}) \right)$$

For a cosmic time interval $\Delta t = 500$ Myr and $\lambda_{\text{Edd}} = 1$:

$$\frac{M_{\text{BH}}(t + \Delta t)}{M_{\text{seed}}} = e^{\Delta t / t_{\text{double}}} \approx e^{500 \, \text{Myr} / 470 \, \text{Myr}} \approx 2.8$$

Growth from $10^5 M_{\odot}$ to $10^9 M_{\odot}$ requires $\log(10^4) = 4$ e-folding times, or ~1.9 Gyr at $\lambda_{\text{Edd}} = 1$. The universe is only ~1.1 Gyr old at z=6 (using WMAP/Planck cosmology). Therefore, either:

- $\lambda_{\text{Edd}} > 1$ sustained (super-Eddington), or
- An earlier seed ($M_{\text{seed}} > 10^6 M_{\odot}$), or
- Both.

Pacucci & Ferrara discuss each option and their observational signatures.

### Direct-Collapse Black Hole (DCBH) Formation

A DCBH forms when a massive gas cloud ($M_{\text{gas}} > 10^6 M_{\odot}$) in pristine (metal-free) gas collapses directly to a black hole without forming stars. The condition is that Lyman-Werner photons (11.2-13.6 eV) from nearby stars photodissociate $H_2$ molecules, preventing the cloud from cooling below the atomic cooling limit (~8000 K). Above this temperature, the cloud is pressure-supported by hydrogen Lyman alpha recombination cooling, making it unable to cool efficiently and collapse on a dynamical timescale.

The critical conditions for DCBH are:

1. **Metal-free gas**: $Z < 10^{-3} Z_{\odot}$ (to avoid metal-line cooling below atomic limit).
2. **Low $H_2$ abundance**: $f_{H_2} < 10^{-4}$ (Lyman-Werner radiation suppresses $H_2$).
3. **High density**: $n > 10^4 \, \text{cm}^{-3}$ (to reach dynamical collapse timescale).
4. **Large mass**: $M > 10^5 M_{\odot}$ (to collapse faster than Hubble time).

The DCBH mass is set by the Jeans mass at the time of collapse:

$$M_{\text{Jeans}} = \left( \frac{\pi}{G \rho} \right)^{1/2} \left( \frac{k_B T}{m_p} \right)^{3/2}$$

At $T = 8000$ K and $n = 10^4 \, \text{cm}^{-3}$:

$$M_{\text{Jeans}} \approx 10^5 \, M_{\odot}$$

Thus, DCBH seeds are naturally $M_{\text{BH}} \sim 10^5 M_{\odot}$, intermediate between stellar and standard SMBH seeds.

Recent simulations (Barrow et al., Habouzit et al., cited in Pacucci & Ferrara) show that DCBH prevalence increases at z > 15 in pristine, dense gas pockets. The frequency at z~20 is estimated at ~1-10% of the galaxy population, providing enough seeds to explain LRDs if accretion is efficient.

### Primordial Black Holes (PBHs) as Seeds

Alternatively, if dark matter comprises a non-negligible fraction of primordial black holes (PBHs) formed in the early universe before matter-radiation equality, then PBHs at $M \sim 10^2-10^5 M_{\odot}$ could seed galaxies at lower redshifts with no need for stellar collapse or DCBH.

PBH abundance is constrained by:
- Gravitational wave limits from LIGO/Virgo on black hole mergers (rules out PBH-dominated dark matter for $M > 10 M_{\odot}$).
- Microlensing limits on compact objects in the Milky Way halo (constrains $M \sim 1-100 M_{\odot}$).
- Isocurvature perturbations in the CMB (constrains $M < 10^{-16} M_{\odot}$).

A "window" remains at $M \sim 10-100 M_{\odot}$ where PBH dark matter is not ruled out. Some researchers (De Luca, Franciolini, Silk; see Paper 29) argue that this window is precisely the mass range that, if populated at ~1 per 100,000 halos, could explain LRDs without invoking super-Eddington accretion.

Pacucci & Ferrara discuss PBHs as a minority scenario but note that it evades black hole formation physics entirely, making it difficult to test. Current limits allow PBH dark matter to be a sub-dominant but non-zero contributor.

---

## Key Results

1. **Unified BHS Phenomenology**: LRDs are best described as Black Hole Stars—young SMBHs embedded in hydrostatic, radiation-pressure-supported gas envelopes. This unifies spectroscopic properties (de Graaff et al. 2025) with SED morphology and explains optical reddening without invoking ad-hoc dust extinction laws.

2. **DCBH Pathway is Viable**: Direct-collapse black hole formation at z > 15 in pristine, metal-free gas can produce seeds at $M_{\text{BH}} \sim 10^5 M_{\odot}$. Super-Eddington accretion for ~500 Myr can grow these to $M_{\text{BH}} \sim 10^9 M_{\odot}$ by z=6, consistent with observations.

3. **Super-Eddington Accretion is Standard**: The prevalence of LRDs (~20% of z>4 galaxies) implies that super-Eddington accretion ($\lambda_{\text{Edd}} \gtrsim 1-10$) is a normal phase of early SMBH evolution, not rare. This requires revision of accretion physics models (ADF, RIAF feedback).

4. **Reionization-Driven Assembly**: LRD AGN luminosities ($L_{\text{bol}} \sim 10^{45}$ erg/s) and abundance (~20% at z>5) suggest that LRDs contribute ~10-30% of ionizing photons during reionization. AGN feedback from LRDs (quasar winds, radiation pressure) helps quench star formation in early galaxies.

5. **Outstanding Challenges**:
   - **Accretion Rate Ambiguity**: Optical diagnostics (virial masses, Hα luminosity) degenerate with dust obscuration and outflow contamination. X-ray constraints (Simmonds et al. 2025) rule out some models but leave others unconstrained.
   - **Seed Formation Rates**: DCBH and stellar collapse models differ in predicted seed abundance by 10-100×. High-z observations (z > 15) are needed.
   - **Halo Mass-Black Hole Mass Relation**: LRDs show $M_{\text{BH}} / M_{\text{host}} \sim 1-10\%$ at high-z, 10-100× higher than z=0 galaxies. Is this evolution in the $M_{\text{BH}} - M_{\text{host}}$ relation, or is it a redshift-dependent selection effect (JWST detecting only the over-massive LRDs)?

6. **New Spectroscopic Data**: NIRSpec has now characterized >200 LRDs with sufficient spectral resolution to measure [O III], [N II], [S II], and other density/ionization diagnostics (2025-2026 data). This enables detailed emission-line mapping and gas dynamics.

7. **Far-IR and Radio Follow-Up**: ALMA 1.3 mm surveys and upcoming SPICA 50 μm observations will measure dust masses and FIR luminosities, constraining the fraction of AGN luminosity absorbed by dust.

---

## Impact and Legacy

The Pacucci & Ferrara (2026) review is a watershed for three reasons:

1. **Synthesis of Disparate Threads**: By Feb 2026, LRD papers numbered >400, with contradictory conclusions from different teams. The review integrates X-ray stacking (non-detections), spectroscopy (de Graaff 116-source sample), far-IR (ALMA limits), and radio data (faint detections) into a coherent narrative.

2. **Theoretical Consolidation**: The Black Hole Star model and DCBH pathway, combined with super-Eddington accretion physics, provide a defensible mechanism for rapid SMBH assembly. This partially assuages the "black hole assembly crisis" by showing that standard (but extreme) physics can explain LRDs without new dark matter or exotic seeds.

3. **Roadmap for 2026-2030**: The review identifies missing pieces: high-z (z>15) seed formation rates, detailed gas dynamics (IFU spectroscopy), host halo masses (gravitational lensing), and the $M_{\text{BH}}-M_{\text{host}}$ evolution.

4. **Influence on Subsequent Reviews**: It superseded the Maiolino et al. (2023) Nature Reviews Physics overview by incorporating 100+ new papers and shifting emphasis from "How do massive black holes grow?" to "What is the phase space (DCBH, super-Eddington, feedback) that permits rapid assembly?"

---

## Connection to Phonon-Exflation Framework

**Relevance**: MODERATE—cosmological structure test, not fundamental physics mechanism.

Phonon-exflation predicts CDM-like dark matter (σ/m ~ 10^{-51}, w = -1 + O(10^{-29})) and thus is *degenerate with LCDM at all z < 10^28*. The LRD assembly problem is a *challenge to LCDM*, but phonon-exflation inherits the same challenge.

However, there are two indirect connections:

1. **Halo Collapse Timescales**: If phonon-exflation predicts a different dark matter halo collapse rate (e.g., via a different equation of state or self-interaction cross-section), then the efficiency of gas assembly in the first ~500 Myr changes. The prevalence of LRDs (~20% at z>4) tests whether early halo collapse is *fast enough* to sustain DCBH formation + super-Eddington accretion.

2. **Feedback Coupling**: LRD AGN drive reionization feedback (quasar winds, radiative heating). The coupling between AGN feedback and dark matter halo dynamics depends on the sound speed of dark matter. Phonon-exflation predicts c_s ~ 10^{-5} c (CDM-like), implying standard halo dynamics. SIDM alternatives with large cross-sections would predict different feedback responses.

**Closest thematic link**: Dark matter halo profiles in z~6 galaxies. If LRD host galaxies have halo density profiles that can be inferred from gravitational lensing or X-ray surface brightness, the slope (cuspy vs core) would test whether phonon-exflation's CDM prediction is correct.

**Summary**: The Pacucci & Ferrara review is essential context for understanding early universe SMBH assembly, a key probe of high-z structure formation. However, it provides no direct discriminant between phonon-exflation and LCDM, since both frameworks predict CDM-like behavior at z~6.

---

**Key Citation**:
Pacucci, F., Ferrara, A. (2026). "Little Red Dots: The Assembly of Early SMBHs in the JWST Era." *Frontiers in Astronomy and Space Sciences*, February 2026, arXiv:2601.00089.
