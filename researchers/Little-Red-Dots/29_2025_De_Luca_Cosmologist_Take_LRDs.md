# A Cosmologist's Take on Little Red Dots

**Authors:** Valerio De Luca, Loris Del Grosso, Gabriele Franciolini, Konstantinos Kritos, Emanuele Berti, Daniel D'Orazio, Joseph Silk

**Year:** 2025

**Journal:** arXiv:2512.19666

---

## Abstract

We analyze the implications of JWST's discovery of Little Red Dots—compact, dust-reddened objects at z~4-8 hosting supermassive black holes with masses $M_{\text{BH}} \sim 10^8-10^{10} M_{\odot}$—from a cosmological perspective. We explore whether LRDs could originate from primordial black holes (PBHs) formed in the early universe, either through hierarchical mergers of lighter PBHs or through rapid gas accretion onto intermediate-mass PBH seeds. We find that direct formation of observed SMBH masses through pure PBH mechanisms is excluded by stringent CMB μ-distortion limits (Planck + COBE/FIRAS), which constrain the total density of PBHs and energy injection in the early universe. However, a viable window remains: PBHs at $M \sim 10^2-10^4 M_{\odot}$ could seed galaxies at lower redshift (z~15-20), subsequently growing via super-Eddington accretion to $M_{\text{BH}} \sim 10^9 M_{\odot}$ by z~6. We contrast this scenario with standard hierarchical LCDM predictions and discuss observational tests.

---

## Historical Context

The problem of rapid early SMBH assembly is inherently *cosmological*, not merely astrophysical. Standard LCDM predicts that structure formation proceeds hierarchically: small dark matter density perturbations collapse first (z ~ 20-100), then merge and accrete to form larger structures (z ~ 5-20). This predicts a specific merger history and gas assembly timeline.

Within this framework, black hole seeds must form from stellar collapse (Pop III stars, M ~ 100-1000 M_sun) or direct collapse (DCBH, M ~ 10^4-10^5 M_sun) at z > 15. These seeds then grow via a combination of black hole mergers (from galaxy mergers) and gas accretion. The timescale for growth from seed to $M_{\text{BH}} = 10^9 M_{\odot}$ is limited by:

1. **Age of the universe**: t(z=6) = 950 Myr, t(z=8) = 550 Myr.
2. **Eddington-limited accretion**: Standard accretion at $\lambda_{\text{Edd}} \lesssim 1$ has an e-folding timescale $t_{\text{double}} \sim 0.5$ Gyr.
3. **Merger timescales**: Black hole mergers take ~1 Gyr per merger event in dynamical friction, limiting the merger rate to ~1-2 per Hubble time per halo.

These constraints are too stringent: growing from $M_{\text{seed}} = 10^5 M_{\odot}$ to $10^9 M_{\odot}$ requires ~4-5 e-folding times with sustained $\lambda_{\text{Edd}} > 1$ (super-Eddington), or more frequent mergers than expected.

De Luca et al. (2025) propose an alternative perspective: *What if some of the SMBH seeds are primordial?* Primordial black holes formed in the early universe (before Big Bang Nucleosynthesis, z ~ 10^24) would have had 13.8 billion years to grow (rather than only ~1 Gyr), easing the assembly problem. However, primordial black holes are tightly constrained by multiple observational tests, particularly CMB μ-distortions.

---

## Key Arguments and Derivations

### Primordial Black Hole (PBH) Formation and Abundances

Primordial black holes form from the collapse of overdense regions in the very early universe (first second), before matter-radiation equality at z ~ 3000. The formation mechanism depends on the density contrast $\delta_{\text{coll}}$ required for collapse:

$$\delta_{\text{coll}} \approx 0.4-0.5 \quad \text{(for radiation-dominated universe)}$$

The mass of a PBH forming at cosmic time $t$ is approximately:

$$M_{\text{PBH}} \approx \frac{4\pi}{3} \rho_{\text{crit}}(t) \left( c t_{\text{Hubble}}(t) \right)^3 \approx 10^{15} \left( \frac{t}{10^{-24} \, \text{s}} \right) \, \text{g}$$

This means PBHs form with a specific mass at each epoch, determined by the Hubble radius at that time. A "monochromatic" distribution (all PBHs of one mass) is unphysical; realistic distributions are log-normal with peak mass $M_{\text{peak}}$ and width $\sigma_{\text{ln}M} \sim 0.5-1$.

The abundance of PBHs is parameterized by the ratio of PBH density to critical density:

$$\Omega_{\text{PBH}} h^2 \equiv \frac{\rho_{\text{PBH}}(z=0)}{\rho_{\text{crit}}(z=0)} h^2$$

Observational constraints from various sources (GW detections, microlensing, CMB μ-distortion, etc.) set upper limits on $\Omega_{\text{PBH}}$ as a function of mass. A famous "window" exists at $M \sim 10^2-10^4 M_{\odot}$ where $\Omega_{\text{PBH}} < 1$ (i.e., PBHs do not comprise all dark matter) but also where other constraints are not as stringent.

### CMB μ-Distortion Constraints

CMB μ-distortions arise from energy injection in the early universe. When photons are scattered by free electrons (via Compton scattering), they can either:

1. Thermalize to a new Planck spectrum (black-body with new temperature T') at low frequencies ($\nu < \nu_{\text{switching}} \sim 1$ GHz), or
2. Accumulate as a non-thermal "μ-distortion" at high frequencies ($\nu > \nu_{\text{switching}}$).

The μ-distortion parameter is defined as:

$$\mu = \int_0^\infty \frac{d\rho_{\text{inj}}}{c^2 dT} (z) \frac{dz}{1+z}$$

where $\rho_{\text{inj}}$ is the injected energy density (from PBH evaporation, early decay processes, etc.).

Planck + COBE/FIRAS observations constrain:

$$|\mu| < 9 \times 10^{-5} \quad \text{(2-sigma)}$$

This is an extremely tight limit. To translate to PBH constraints, De Luca et al. use:

$$\mu \propto \Omega_{\text{PBH}} \times \left( \frac{M_{\text{PBH}}}{10^{15} \, \text{g}} \right)^{-1/2}$$

(heavier PBHs inject less energy per unit mass, since they evaporate more slowly). For a monochromatic distribution at $M_{\text{PBH}} = 10^4 M_{\odot} = 2 \times 10^{31}$ g:

$$\Omega_{\text{PBH}} < 10^{-2}$$

This means PBHs cannot comprise more than ~1% of the dark matter if they are to satisfy μ-distortion limits. This is far below the requirement for PBHs to serve as *all* dark matter, but allows for a sub-dominant population.

### Hierarchical Mergers vs. Gas Accretion for PBH Growth

**Scenario 1: PBH Mergers**

If LRD black holes are assembled through mergers of lighter PBHs, the process would be:

1. Form a population of intermediate-mass PBHs (IMBHs) at M ~ 10^3-10^4 $M_{\odot}$ at z > 25.
2. Allow these to merge (via gravitational waves or dynamical friction in dense halos) over cosmic time.
3. Reach $M_{\text{BH}} \sim 10^9 M_{\odot}$ by z~6 through repeated mergers.

The merger timescale via gravitational wave emission is:

$$t_{\text{merge}} = \frac{12}{19} \frac{c^5}{G^3 m_1 m_2 (m_1 + m_2)} \quad \text{[GW coalescence timescale]}$$

For equal-mass binaries of M ~ 10^4 $M_{\odot}$:

$$t_{\text{merge}} \sim 10^{11} \text{ s} \sim 3000 \, \text{Gyr}$$

This is *much longer* than the Hubble time (13.8 Gyr), so PBH mergers are negligibly slow. Hierarchical mergers do not work unless PBHs are captured into extremely tight binaries in very dense clusters (stellar density ~ 10^6 per pc^3), which is rare. **Conclusion**: Pure PBH mergers cannot explain LRDs.

**Scenario 2: Gas Accretion on PBH Seeds**

Alternatively, if PBHs at M ~ 10^3-10^4 $M_{\odot}$ form at high-z and then accrete gas:

$$\frac{dM_{\text{BH}}}{dt} = \lambda_{\text{Edd}} \dot{M}_{\text{Edd}} = \lambda_{\text{Edd}} \frac{L_{\text{Edd}}}{c^2 \epsilon}$$

For exponential growth:

$$M_{\text{BH}}(t) = M_{\text{seed}} \exp \left( \frac{\lambda_{\text{Edd}} H_0}{\ln 2} \int_z^{\infty} \frac{dz'}{(1+z') H(z')} \right)$$

With $\lambda_{\text{Edd}} = 10$ and integrating from z=20 to z=6:

$$M_{\text{BH}}(z=6) = 10^4 M_{\odot} \times \exp \left( 10 \times \frac{0.4}{470 \text{ Myr}} \times 700 \text{ Myr} \right) \approx 10^4 \times e^6 \approx 4 \times 10^6 M_{\odot}$$

This is still a factor of ~100-1000 short of observed LRD masses. **Conclusion**: Even with aggressive super-Eddington accretion ($\lambda_{\text{Edd}} = 10$), PBH seeds struggle to reach $M_{\text{BH}} > 10^8 M_{\odot}$ by z~6. A combination of early PBH formation + frequent mergers at high-z (before z~20) would be required.

De Luca et al. argue that this scenario is possible but requires:
1. A significant PBH population at z > 25 (not yet observationally confirmed).
2. Efficient gas accretion at super-Eddington rates for sustained periods.
3. A specific realization of the dark matter halo merger history to supply dense enough environments for frequent mergers and rapid gas infall.

---

## Key Results

1. **Direct PBH Formation Rules Out**: Pure primordial formation of $M_{\text{BH}} \sim 10^8-10^{10} M_{\odot}$ objects at early times is excluded by CMB μ-distortion limits. The energy injection from early PBH evaporation or radiation would distort the CMB spectrum beyond observed limits.

2. **Viable PBH Window**: A sub-dominant PBH population at M ~ 10^2-10^4 $M_{\odot}$ is allowed by μ-distortions (provided $\Omega_{\text{PBH}} < 10^{-2}$). This population could contribute to LRD seeds at z~15-20.

3. **Merger Timescales Too Long**: Hierarchical mergers of PBHs proceed on timescales >> Hubble time. They cannot build up SMBH masses on their own.

4. **Super-Eddington Gas Accretion is Required**: Any viable PBH scenario requires sustained accretion at $\lambda_{\text{Edd}} > 1$, at least episodically, to grow PBHs from ~10^4 to ~10^9 $M_{\odot}$ in <1 Gyr.

5. **LCDM Alternatives Remain Viable**: Standard hierarchical DCBH formation with standard seeds (Pop III, stellar collapse) can also explain LRDs if super-Eddington accretion is invoked. The data do not strongly favor PBH over standard seeds.

6. **Smoking Gun Tests**: Future observations could distinguish:
   - **PBH signature**: A population of isolated black holes unassociated with star-forming galaxies (PBHs do not form with galactic hosts). None have been found to date.
   - **Seed formation age**: If PBH seeds form at z > 100 and grow thereafter, they should show different co-evolution with their host galaxies (older stars, more compact) than standard z~20 seeds. Spectroscopic ages are inconclusive so far.

7. **Conclusion**: While PBHs are not ruled out as *a* component of LRD formation, they are not required and do not solve the assembly crisis more elegantly than standard mechanisms. The most likely scenario remains DCBH formation at z~20 + super-Eddington accretion.

---

## Impact and Legacy

The De Luca et al. (2025) paper is significant for:

1. **Cosmological Rigor**: It brought rigorous cosmological constraints (CMB μ-distortions) to bear on the LRD problem, which had been dominated by astrophysical (AGN, accretion) discussions. This expanded the framework for understanding the crisis.

2. **PBH Constraints Updated**: The paper provided the tightest limits on PBH abundance as a function of mass, incorporating recent Planck and COBE/FIRAS data. This superseded earlier (pre-2024) PBH constraints.

3. **Cross-Disciplinary Perspective**: By treating LRDs as a cosmological test (not just an AGN puzzle), the paper highlighted connections to early-universe physics, inflation, phase transitions, and dark matter models.

4. **Foundation for Future Tests**: The paper outlined observational predictions (isolation of PBHs, spectroscopic ages, clustering properties) that guide future JWST, Vera Rubin, and radio (VLA, SKA) surveys.

---

## Connection to Phonon-Exflation Framework

**Relevance**: MODERATE—cosmological alternative test, not direct mechanism test.

Phonon-exflation predicts CDM-like dark matter (σ/m ~ 10^{-51}, w = -1 + O(10^{-29})) and is degenerate with LCDM at z < 10^28. The De Luca et al. analysis of PBH scenarios is orthogonal to phonon-exflation: both frameworks are silent on whether primordial black holes exist or comprise dark matter.

However, there is an *indirect* connection through early-universe physics:

**Inflation and Density Perturbations**: Phonon-exflation predicts a specific spectrum of primordial density perturbations (inherited from the pre-exflation phonon field). This spectrum determines the abundance and mass distribution of PBHs that form (if any). If phonon-exflation predicts *fewer* high-mass PBHs than standard single-field inflation, then PBH scenarios for explaining LRDs become less viable within the phonon-exflation framework.

**Example**: Standard slow-roll inflation predicts a Harrison-Zeldovich spectrum with scalar spectral index $n_s \approx 0.96-0.97$. This produces PBHs primarily at M ~ 10^15 g (Planck-mass relics). Phonon-exflation, if it has a running spectral index or a feature in the primordial power spectrum, could suppress or enhance PBH formation at specific mass scales.

**Closest thematic link**: Early-universe cosmology and the primordial power spectrum. If observational tests (e.g., future CMB-S4 or primordial gravitational waves from LISA) constrain the primordial spectrum, phonon-exflation's predictions on PBH abundance could be tested indirectly.

**Summary**: The De Luca et al. analysis of PBH scenarios provides important context for understanding LCDM alternatives and their observational signatures. However, phonon-exflation is agnostic on PBH abundance and makes no specific predictions that distinguish PBH scenarios from standard DCBH formation. Both frameworks remain consistent with LRD observations.

---

**Key Citation**:
De Luca, V., Del Grosso, L., Franciolini, G., Kritos, K., Berti, E., D'Orazio, D., & Silk, J. (2025). "A Cosmologist's Take on Little Red Dots." arXiv:2512.19666.
