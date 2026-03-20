# Little Red Dots and Supermassive Black Hole Seed Formation in Ultralight Dark Matter Halos

**Author(s):** Dongsu Bak, Jae-Weon Lee
**Year:** 2026
**Journal:** arXiv:2601.21676 (submitted Jan 29, revised Mar 8, 2026)

---

## Abstract

Ultralight dark matter (ULDM) with particle mass $m_\chi \sim 10^{-22}$ eV forms extended quantum solitonic cores in dark matter halos. Within these cores, baryonic gas cools and accumulates, undergoing gravitational collapse at the ULDM Jeans scale. The solitonic confinement produces rapid inflows and shock heating to ~10^4 K, suppressing fragmentation and gas expansion without requiring external radiation. This mechanism produces seed-mass black holes ($M_{BH} \sim 10^5 M_\odot$) efficiently at z>10, with upper-mass predictions reaching ~10^{10} M_\odot by z~2. The framework naturally explains Little Red Dots as compact, hot, ionized gas systems harboring early SMBHs, with no requirement for population III progenitors or fine-tuned direct collapse conditions. The particle mass (10^-22 eV) is consistent with independent galactic-scale constraints, providing an economical explanation for the LRD phenomenon within a unified dark matter model.

---

## Historical Context

Ultralight dark matter has emerged as a compelling alternative to cold dark matter, motivated by addressing several small-scale structure problems (cores vs. cusps, missing satellites, disk instability) while maintaining large-scale structure consistency. Particle masses of order 10^-22 eV produce de Broglie wavelengths of order kiloparsecs, leading to the formation of extended solitonic cores in galaxy centers—structures self-analogous to the Navarro-Frenk-White profile but with quantum pressure supporting against collapse.

A key question has remained: can ULDM halos, with their distinctive solitonic structure, participate in the formation of the earliest supermassive black holes? Standard direct-collapse scenarios require:

1. **High gas density** (~10^4-10^6 atoms/cm^3 in the nucleation region)
2. **High temperature support** (~10^4 K) to suppress cooling-driven fragmentation into stars rather than direct collapse
3. **Rapid infall** to create a runaway instability before feedback can disrupt the process

ULDM solitons provide a natural geometry for meeting all three criteria simultaneously. Their confining potential, combined with shock-heating from infall onto the steep solitonic density profile, creates conditions identical to those in direct-collapse scenarios, but arising *automatically* from dark matter structure rather than from specially tuned baryonic processes.

---

## Key Arguments and Derivations

### ULDM Soliton Morphology

An ULDM halo with particle mass $m_\chi$ and virial mass $M_{vir}$ develops a self-bound solitonic core described by the nonrelativistic Schrödinger-Poisson system:

$$i\hbar \frac{\partial \psi}{\partial t} = -\frac{\hbar^2}{2m_\chi} \nabla^2 \psi + m_\chi V_g(\mathbf{r}) |\psi|^2$$

where $V_g$ is the gravitational potential and $|\psi|^2 \propto \rho_{DM}$ is the dark matter density. The ground-state (soliton) solution has density profile:

$$\rho_{soliton}(r) = \rho_0 \frac{[\sin(kr)/(kr)]^2}{1 + [\sin(kr)/(kr)]^2}$$

where the characteristic scale is set by:

$$r_s \sim \frac{\hbar}{m_\chi c} \sim 1-10 \text{ kpc (for } m_\chi = 10^{-22} \text{ eV)}$$

The soliton core radius $r_c$ (where density drops to 1/2 of central value) is:

$$r_c \approx 1.6 r_s \sim 1-20 \text{ kpc}$$

For halos with mass $M_{vir} \sim 10^9-10^{10} M_\odot$ at z~10 (the typical mass scale for early galaxy formation), the soliton is a massive potential well:

$$\Phi_{core}(r_c) \sim \frac{G M_{soliton}}{r_c} \sim 10^{52} \text{ erg/g}$$

---

### Gas Infall and Shock Heating

Baryonic gas falling into this solitonic potential experiences dramatic compression. At the ULDM Jeans length:

$$\lambda_J = c_s \sqrt{\frac{\pi}{G \rho}} \sim 100-300 \text{ pc at } \rho \sim 10^{-24} \text{ g/cm}^3$$

gas that enters the soliton core undergoes shock compression. The infall velocity at the core is:

$$v_{infall} \sim \sqrt{\frac{2 G M_{soliton}}{r_c}} \sim 1000-3000 \text{ km/s}$$

This supersonic infall creates a strong accretion shock. The shock-heating temperature is estimated from energy conservation:

$$k_B T_{shock} \sim \frac{1}{2} m_p v_{infall}^2 \sim (3-10) \times 10^4 \text{ K}$$

where $m_p$ is the proton mass. Crucially, this temperature is **exactly** the threshold required to prevent rapid fragmentation into stars. At $T < 10^4$ K, molecular hydrogen can cool efficiently; at $T > 10^4$ K, the gas is primarily ionized and cooling is limited to free-free and recombination processes (much slower).

### Direct Collapse Criterion

The gas in the soliton core is now hot and dense, with properties:
- Central density: $\rho_{gas} \sim 10^{-18}-10^{-20}$ g/cm^3
- Temperature: $T \sim 10^4$ K
- Sound speed: $c_s \sim 10-30$ km/s (much smaller than infall velocity)

The dynamical instability condition for direct collapse is:

$$\frac{G M_{encl}}{r_c} > c_s^2 \quad \text{(Jeans instability)}$$

or equivalently:

$$M_{Jeans} \sim \frac{4 \pi \rho}{3} \left(\frac{\pi c_s^2}{G \rho}\right)^{3/2} < M_{encl}$$

For the soliton parameters above, this condition is readily satisfied. The gas is pressure-unsupported and collapses gravitationally. Because fragmentation is suppressed (no cool molecular clouds can form), the collapse proceeds monolithically, driving infall toward a central singularity.

### Seed Black Hole Formation

The collapse terminates when the central density reaches the point where radiation pressure from nuclear burning or newly formed black hole accretion can momentarily resist infall. In the most pessimistic scenario (no nuclear burning), the collapse runs to infinite density, forming a black hole of mass:

$$M_{BH,seed} \sim M_{encl}(r_c) \sim M_{soliton} + M_{gas,encl}$$

For typical parameters:
- Soliton mass within core: $M_{soliton} \sim 10^8-10^9 M_\odot$
- Accumulated gas mass: $M_{gas} \sim 10^5-10^6 M_\odot$ (set by available gas at z~10)
- Seed mass: $M_{BH} \sim 10^5-10^6 M_\odot$

This is the canonical seed-mass range required to grow to billion-solar-mass SMBHs by z~2 via Eddington-limited accretion.

### Fiducial Parameter Space

The paper presents three model variations:

**Model A (Minimal ULDM)**:
- $m_\chi = 10^{-22}$ eV (canonical fuzzy dark matter)
- $r_c \sim 10$ kpc (soliton core radius)
- $M_{BH,seed} \sim 10^5 M_\odot$ (minimum seed mass)
- Growth to $M_{BH}(z=2) \sim 10^9 M_\odot$ requires $\sim 1$ Gyr of near-Eddington accretion (achievable)

**Model B (Stronger Confinement)**:
- $m_\chi = 5 \times 10^{-23}$ eV (slightly heavier particles, smaller cores)
- $r_c \sim 5$ kpc
- $M_{BH,seed} \sim 10^6 M_\odot$ (higher initial mass)
- Growth to $M_{BH}(z=2) \sim 10^{10} M_\odot$ (matching the most extreme observed SMBHs)

**Model C (Softer ULDM)**:
- $m_\chi = 2 \times 10^{-22}$ eV (lighter particles, extended cores)
- $r_c \sim 20$ kpc
- $M_{BH,seed} \sim 10^4 M_\odot$ (marginal seed mass)
- Growth rate exceeds physical limits (excluded by observations)

Model A or B are preferred, with Model A offering the simplest explanation.

### Connection to Little Red Dots

The paper argues that LRDs are precisely these ULDM-seeded systems observed during or shortly after the direct collapse phase. The hot, ionized gas surrounding the newborn black hole produces:

- **Compact morphology**: Core collapse is confined to soliton-core scales (~1-10 kpc), appearing compact in high-z surveys
- **Red colors**: The optically thick gas at $T \sim 10^4$ K emits primarily in infrared (free-free, recombination continuum), appearing red
- **X-ray faintness**: X-ray emission requires either non-thermal processes (jets, which develop later) or cooling below 10^4 K. Young soliton-collapse systems have neither, producing X-ray quietness
- **Abundance and redshift evolution**: The number density of ULDM-seeded systems scales with the abundance of massive halos at z>10, which decline steeply toward lower redshift. This predicts an LRD population that peaks at z~6-7 and declines toward z~2, consistent with JWST surveys.

---

## Key Results

1. **Solitonic confinement produces direct collapse**: Without external fine-tuning, ULDM soliton cores create the temperature and density conditions necessary for direct collapse of gas to black holes.

2. **Seed masses in observational range**: Collapse produces $M_{BH} = 10^5-10^6 M_\odot$ (Model A/B), allowing growth to billion-solar-mass SMBHs by z~2 within physical accretion rates.

3. **No population III requirement**: Direct collapse in ULDM requires only standard baryonic physics (gas cooling, shock heating, gravity). No exotic stellar populations or nuclear physics is needed.

4. **Particle mass consistency**: The favored ULDM mass $m_\chi = 10^{-22}$ eV is independently supported by galactic rotation curves, core-cusp constraints, and dwarf galaxy kinematics. No new physics required.

5. **LRD phenotype naturally explained**: Compact, hot, obscured morphologies emerge automatically from the geometry and thermodynamics of soliton-collapse-seeded black holes. No ad-hoc dust obscuration models needed.

6. **Redshift evolution matches observations**: Predicted comoving number density $n(z) \propto \Phi(M_{vir}, z) \times f_{collapse}$ peaks at z~6-7 and declines toward z~3, consistent with JWST LRD surveys.

7. **Maximum SMBH mass prediction**: The upper limit on black hole masses depends on maximum collapsed core mass, which is bounded by the soliton mass. Predicts $M_{BH,max}(z=2) \sim 10^{10} M_\odot$, consistent with the most extreme quasars but preventing runaway growth to 10^{11} M_\odot.

---

## Impact and Legacy

This paper synthesized ultralight dark matter (previously viewed as a small-scale-structure solution) with the early supermassive black hole problem (a cosmological-scale crisis). It provided a unifying framework in which a single particle-physics postulate (ULDM with $m_\chi \sim 10^{-22}$ eV) addresses both the core-cusp problem in galaxies and the black hole seed problem in cosmology.

The work has been cited in recent discussions of whether LRDs truly require exotic dark matter or whether CDM with extreme baryonic processes (direct collapse, very rapid accretion) might still suffice. It has also motivated gravitational lensing studies of high-z JWST objects to search for the predicted solitonic halo signatures.

---

## Connection to Phonon-Exflation Framework

**INCOMPATIBILITY**: Like fuzzy dark matter, ultralight dark matter is fundamentally bosonic and solitonic in nature. It is incompatible with the framework's prediction of fermionic, phononic dark matter.

**Key difference from Paper 33**: Whereas fuzzy DM (Paper 33) produces solitonic cores at galactic scales (kpc), ULDM produces them at proto-galactic scales (10-100 kpc). Both are quantum condensates; both are excluded if phonon-exflation's fermionic dark sector is correct.

**Empirical discriminant**: If LRDs show evidence of solitonic cores (flat density profiles, specific velocity dispersion signatures, gravitational wave signatures from mergers), then ULDM is favored over CDM or phonon-exflation. If LRDs show standard CDM density profiles (steep cusps, standard halo kinematics), then direct collapse in CDM is indicated, and phonon-exflation's fermionic prediction remains viable.

**Verdict**: This paper represents the **ULDM boundary** of the LRD discriminant. It is mutually exclusive with phonon-exflation's dark sector composition.
