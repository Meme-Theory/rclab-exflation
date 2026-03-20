# Born in the Dark: Fuzzy DM Soliton Collapse as Origin of LRDs

**Author(s):** Tak-Pong Woo
**Year:** 2026
**Journal:** arXiv:2601.00044 (submitted Dec 31, 2025)

---

## Abstract

Fuzzy dark matter (FDM) with particle mass $m_\chi \sim 10^{-22}$ eV forms macroscopic quantum soliton cores in high-density environments. During the merger and relaxation of proto-galactic dark matter halos at z>5, these solitons undergo catastrophic gravitational collapse triggered by the accumulation of ordinary baryonic matter into the soliton core. The collapse produces extreme column densities ($N_H > 10^{24}$ cm^-2) and enables rapid infall of gas. This mechanism naturally explains the compact morphologies, extreme infrared obscuration, and inferred black hole masses of JWST Little Red Dots without requiring baryonic direct collapse or population III progenitors. Schrödinger-Poisson simulations demonstrate that soliton collapse produces seed-mass black holes in ~10^6-10^7 M_sun range with number densities and redshift evolution consistent with observations. The model predicts distinctive soliton halo signatures detectable via future line-of-sight velocity dispersion measurements and gravitational lensing.

---

## Historical Context

Fuzzy dark matter—bosonic dark matter with de Broglie wavelength $\lambda_{dB} \sim 1-10$ kpc at galactic scales—was originally motivated by galactic dynamics concerns (core-cusp problem, too-many-satellites problem). The quantum pressure associated with FDM's wave nature was proposed to suppress small-scale structure formation and create extended cores in galaxy centers, providing a gentler alternative to self-interacting dark matter.

However, subsequent work recognized that FDM, when coupled to gravity in high-density regions, naturally produces solitonic structures—self-bound quantum states with compactness determined by the de Broglie wavelength:

$$r_{soliton} \sim \frac{\hbar}{m_\chi c} \sim 1-100 \text{ pc (for } m_\chi \sim 10^{-22} \text{ eV)}$$

These solitons are gravitationally bound but pressure-supported by quantum mechanics. They represent a form of "dark matter core collapse" distinct from the gravothermal catastrophe in self-interacting dark matter or the dynamical friction collapse in cold dark matter.

The JWST LRD discoveries—compact, highly obscured, apparently harboring billion-solar-mass black holes at z>5—present a natural target for soliton collapse models. If solitons can collapse on cosmological timescales in the densest environments, they provide a mechanism for seed formation that operates entirely within the dark sector, yet produces exactly the compact morphologies and extreme column densities observed in LRDs.

---

## Key Arguments and Derivations

### FDM Soliton Structure

A self-gravitating quantum system with wave function $\psi$ obeys the Gross-Pitaevskii-Poisson equations:

$$i\hbar \frac{\partial \psi}{\partial t} = -\frac{\hbar^2}{2m_\chi} \nabla^2 \psi + m_\chi \Phi(\mathbf{r}) |\psi|^2$$

$$\nabla^2 \Phi = 4\pi G m_\chi |\psi|^2 + 4\pi G \rho_B$$

where $\Phi$ is the gravitational potential, $\rho_B$ is the baryonic density distribution, and the second equation includes both dark matter and baryonic contributions to the gravitational field.

In the absence of baryons, a bound state (soliton) exists with radial profile:

$$\rho_{soliton}(r) \sim M_{sol} \left[1 + \left(\frac{r}{r_c}\right)^2\right]^{-1/2}$$

where the core radius $r_c$ depends on mass and particle properties:

$$r_c \sim \frac{1.6 \hbar^2}{G m_\chi^3 M_{sol}}$$

For particle mass $m_\chi = 10^{-22}$ eV and soliton mass $M_{sol} \sim 10^8 M_\odot$ (a typical proto-galactic core mass at z~6), this gives:

$$r_c \sim 100 \text{ pc}$$

This is remarkably close to the observed compact sizes of LRDs (~50-200 pc), providing the first hint that solitons might be relevant.

### Soliton-Baryon Coupling

Once baryonic matter accumulates in a soliton core (via ordinary accretion, cooling from the virial-temperature gas), the coupled system becomes unstable. The baryon contribution to the gravitational potential increases the inward pull, destabilizing the quantum pressure-supported equilibrium.

The criterion for instability is that the baryon mass in the core exceeds the critical "Oppenheimer-Volkoff" mass for a quantum system:

$$M_B > M_{crit} \sim \frac{\hbar^2}{G m_\chi^3}$$

For $m_\chi = 10^{-22}$ eV, this gives $M_{crit} \sim 10^5-10^6 M_\odot$. In proto-galactic cores undergoing rapid cooling and infall, this threshold is readily exceeded. Once crossed, the soliton cannot support its configuration against the combined gravity of itself and the accumulated baryons. It collapses.

### Collapse Dynamics and Opacity Crisis

During collapse, the system undergoes a phase transition from quantum pressure-dominated to gravity-dominated. The collapse is not free-fall (which would require purely baryonic dynamics) but quantum-pressure-assisted. The effective collapse timescale is:

$$\tau_{collapse} \sim \frac{r_c}{c_s^{quantum}} \sim \frac{r_c}{\hbar m_\chi / m_e} \sim 10-100 \text{ Myr}$$

where $c_s^{quantum} \sim \hbar m_\chi / m_e \sim 10^{-3} c$ is the quantum sound speed in the dark matter medium.

A critical feature discovered in this work is the "Opacity Crisis": as gas rapidly cools and accumulates in the soliton core, the column density rises dramatically:

$$N_H \sim \int_0^{r_c} n_H(r) dr \sim M_B / (\pi r_c^2)$$

For $M_B \sim 10^6 M_\odot$ and $r_c \sim 100$ pc:

$$N_H \sim 10^{24}-10^{25} \text{ cm}^{-2}$$

This is extraordinary—far exceeding the column density of the Milky Way (~10^{21} cm^-2). At these densities, dust becomes optically thick to virtually all radiation except X-rays, producing the "red" colors and X-ray faintness characteristic of LRDs.

Crucially, this opacity is a *consequence* of soliton collapse, not a separate fine-tuning. The geometry (compact core radius) and dynamics (rapid infall) naturally produce the observed obscuration.

### Seed Black Hole Mass

Once the soliton collapses, the dynamical friction of accumulated gas drives the system to runaway gravitational contraction. If the core contracts to sub-Schwarzschild dimensions, an event horizon forms. The seed mass is essentially the total mass in the core at collapse time:

$$M_{BH} \sim M_{soliton} + M_{baryon}$$

For typical values:
- Soliton mass: $M_{sol} \sim 10^7 M_\odot$
- Accumulated baryon mass at collapse: $M_B \sim 10^5-10^6 M_\odot$
- Total seed mass: $M_{BH,seed} \sim 10^6-10^7 M_\odot$

This mass can then grow via Eddington-limited accretion to billion-solar-mass scales by z~2-3, matching the observed quasar population.

### Population Statistics

The number density of soliton-collapse events depends on:

1. **Number density of solitons** at high redshift: determined by the dark matter power spectrum and halo abundance, typically $\sim 0.1-1$ Gpc^-3 for FDM mass $m_\chi = 10^{-22}$ eV
2. **Probability of baryon accumulation**: galaxy formation efficiency in dense environments is high (~10-30% of available gas cools into the central region)
3. **Collapse fraction**: not all solitons reach the instability threshold; only those with sufficient baryon infall collapse

The net prediction is:

$$n_{collapse}(z) \sim n_{soliton}(z) \times P_{baryon} \times f_{collapse}$$

With reasonable parameter choices, this yields:

$$n_{LRD}(z=5) \sim 0.1-1 \text{ Gpc}^{-3}$$

consistent with JWST observations.

### Schrödinger-Poisson Simulations

The paper presents numerical solutions to the coupled Gross-Pitaevskii-Poisson system using spectral methods and finite-difference time-stepping. Key findings include:

1. **Stability threshold**: Solitons with $M_B / M_{sol} > 0.1-0.3$ are unstable and collapse within a dynamical time
2. **Collapse morphology**: The core density profile steepens from the initial soliton profile $\rho \propto r^{-2}$ to a steeper cusp approaching $\rho \propto r^{-3}$ during collapse
3. **Density amplification**: Central density increases by factors 100-1000 during the final collapse phase
4. **Infall kinematics**: Velocities in the core reach 1000-3000 km/s, consistent with broad emission line widths observed in some LRDs

---

## Key Results

1. **Soliton core size matches LRD compactness**: For $m_\chi = 10^{-22}$ eV, soliton core radii are 50-200 pc, identical to JWST LRD morphologies.

2. **Baryon accumulation triggers collapse**: Once baryonic mass exceeds ~10% of soliton mass, quantum pressure can no longer support the system; gravitational collapse ensues on ~10-100 Myr timescales.

3. **Column density naturally extreme**: Soliton collapse produces $N_H > 10^{24}$ cm^-2 *automatically*, explaining LRD infrared obscuration without ad-hoc fine-tuning.

4. **Seed masses in right range**: Core collapse produces $M_{BH} \sim 10^6-10^7 M_\odot$ seeds, which grow to 10^9 M_sun by z~2 via standard Eddington accretion.

5. **Number density and redshift evolution**: Predicted $n_{LRD}(z) \propto (1+z)^{2-3}$ matches observed LRD evolution from z~7 to z~5.

6. **Opacity Crisis explanation**: Extreme column densities are a geometric + dynamic consequence of soliton collapse, not a separate ingredient. This provides a unified origin for the obscured, compact phenotype.

---

## Impact and Legacy

This paper elevated solitonic fuzzy dark matter from a galactic-scale curiosity to a potentially significant early-universe mechanism. It demonstrated that quantum effects in dark matter, often dismissed as irrelevant at cosmological scales, can produce dramatic consequences (seeds for billion-solar-mass black holes) when coupled to baryon physics.

The work has inspired follow-up studies on:
- Stability of solitons in cosmological simulations
- Spectral signatures of soliton-collapse-seeded AGN (emission line widths, continuum slopes)
- Gravitational wave signals from soliton merger and collapse
- Consistency of FDM with Milky Way structure given solitons' role in early black hole seeding

The paper also crystallizes a key question: does JWST data favor fuzzy dark matter (soliton collapse) or ultra-strongly self-interacting dark matter (gravothermal collapse) or standard CDM (baryonic direct collapse/mergers)? The answer will likely require deeper spectroscopic follow-up and modeling of individual LRDs, not just morphological surveys.

---

## Connection to Phonon-Exflation Framework

**CRITICAL TENSION**: Fuzzy dark matter with particle mass $m_\chi \sim 10^{-22}$ eV is fundamentally **bosonic in nature**, arising from a scalar or vector field. The phonon-exflation framework, by contrast, predicts **fermionic** dark particles (quasi-holes in the BCS condensate of the pairing mechanism) with effective mass $m_{eff} \sim 1$ GeV and contact interactions (phononic), not field-theoretic solitons.

**Incompatibility**: Solitonic fuzzy dark matter and fermionic phonons cannot coexist as the dominant dark sector. They represent mutually exclusive mechanisms for dark matter structure.

**Empirical discriminant**: If LRDs are indeed products of soliton collapse:
- **Signature A**: Gravitational lensing will reveal distinctive soliton halo profiles (flat cores, $\rho \propto r^{-2}$ inner regions)
- **Signature B**: Line-of-sight velocity dispersion in soliton cores scales as $\sigma \propto (M_{sol} / r_c)^{1/2} \sim 10-100$ km/s for $m_\chi = 10^{-22}$ eV
- **Signature C**: Soliton-soliton merger rates and gravitational wave signals are detectable by LISA if mergers occurred at z>10

If these signatures appear, phonon-exflation (with its fermionic, contact-interaction dark matter) is excluded. If they do not appear, and LRDs are instead CDM-seeded, phonon-exflation's ultralight particle prediction faces constraints but is not falsified.

**Verdict**: This paper defines the **fuzzy dark matter boundary** of the LRD discriminant. Solitons vs. phonons is a fundamental split in dark sector physics.
