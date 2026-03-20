# Cosmic-Web Paper Index

**Researcher corpus**: Volovik (superfluid cosmology), van de Weygaert (geometric analysis), Einasto (profiles and supercluster network), Khoury-Berezhiani (superfluid DM), plus observational anomaly and void physics literature
**Papers**: 39 (1965-2026)
**Primary domain**: Large-scale structure, void physics, cosmic web topology, superfluid cosmology analogs, observational anomalies
**Project relevance**: Volovik's emergent gravity is the conceptual ancestor of phonon-exflation; van de Weygaert tools define the geometric language; Einasto's empirics set the observational benchmarks; anomaly papers define the tension landscape

---

## Dependency Graph

```
SUPERFLUID COSMOLOGY FOUNDATIONS (Volovik -> Khoury-Berezhiani)
  01 (Universe in He droplet, 2003) <-- 02 (Superfluid analogies, 2001)
  02 -> 01 (book extends review)
  02 -> 30 (de Sitter thermodynamics, 2024)
  30 -> 39 (First law of de Sitter, 2025)
  01,02 -> 07 (Khoury superfluid DM, 2015)
  07 -> 18 (Berezhiani-Khoury PRD, 2015)
  07,18 -> 24 (Berezhiani-Khoury review, 2025)

COSMIC WEB GEOMETRY (van de Weygaert program)
  03 (DTFE geometric analysis, 2007) -> 04 (Connectivity & topology, 2009)
  03 -> 11 (MMF, Aragon-Calvo 2007)
  04 -> 27 (Wilding persistent homology, 2021)
  04 -> 28 (Pranav persistent Betti, 2017)
  11 -> 34 (ASTRA classification, 2024)
  03,04,11 -> 34

DENSITY PROFILES & BAO
  05 (Einasto profile, 1965) -- independent foundation
  06 (Supercluster-void network, 2001) <-- 05 (profile used in cluster analysis)
  08 (Eisenstein BAO, 2005) -- independent foundation
  06,08 -> 17 (DESI DR1, 2025)
  08 -> 19 (DESI DR2, 2025)

VOID PHYSICS (Sutter -> Hamaus -> Contarini -> Salcedo/Euclid)
  12 (Sutter VIDE, 2014) -> 13 (Hamaus void dynamics, 2016)
  12,13 -> 26 (Contarini void tensions, 2024)
  12,13 -> 33 (Contarini Euclid void size, 2022)
  12,13 -> 32 (Salcedo DESI void forecasts, 2025)
  33 -> 32 (Euclid -> DESI forecasting)

GIANT STRUCTURES & ANOMALIES
  09 (Geller-Huchra Great Wall, 1989) -> 10 (Bahcall clusters, 1988)
  14 (Horvath HCBGW, 2014) -- GRB-based, independent
  16 (Lopez Giant Arc, 2022) -> 25 (Lopez Big Ring, 2024)
  16,25 -> 21 (Sawala FLAMINGO rebuttal, 2025)
  21 <-> 22 (Lopez-Clowes counter-rebuttal, 2025)
  15 (Watkins bulk flow, 2009) -> 20 (Watkins CF4 bulk flow, 2023)
  29 (Secrest cosmic dipole, 2025) -> 35 (Dipole tensions multi-wavelength, 2025)
  31 (Haslbauer KBC void, 2020) -- connects to 20 (bulk flow) and 29 (dipole)

PERSISTENT HOMOLOGY / TDA
  03,04 -> 28 (Pranav persistent Betti, 2017)
  28 -> 27 (Wilding persistent homology, 2021)

DARK ENERGY OBSERVATIONAL CONSTRAINTS
  08 -> 17 (DESI DR1 BAO, 2025)
  17 -> 19 (DESI DR2 BAO, 2025)
  19 -> 37 (Wang-Mota skeptical assessment, 2025)
  19 -> 38 (Lascu SN systematics, 2024)
  23 (KiDS Legacy S8, 2025) -> 36 (S8 tension review, 2026)

CROSS-GROUP CONNECTIONS
  06 (Einasto supercluster spacing ~120 Mpc) <-> 08 (BAO ~150 Mpc)
  20 (CF4 bulk flow) <-> 31 (KBC void) <-> 29 (dipole anomaly)
  12,13 (void probes) <-> 17,19 (DESI constraints)
  27,28 (TDA) <-> 03,04 (van de Weygaert geometry)
  21 <-> 22 (Sawala vs Lopez: UNRESOLVED DEBATE)
  37,38 (skepticism of DESI w!=−1) <-> 19 (DESI DR2 claim)
```

### Duplicate/Overlap Pairs

| Papers | Relationship |
|:---|:---|
| 07, 18 | Khoury (2015 letter) and Berezhiani-Khoury (2015 PRD): same framework, 18 is detailed theory |
| 15, 20 | Watkins (2009) and Watkins (2023): same group, CF4 supersedes CF1-CF3 |
| 29, 35 | Secrest dipole colloquium and multi-wavelength dipole tensions: overlapping analysis |
| 21, 22 | Sawala (FLAMINGO) and Lopez-Clowes (FLAMINGO rebuttal): same simulation, opposite conclusions |

---

## Topic Map

### A. Superfluid Cosmology Foundations (2001-2025)
Papers: 01, 02, 07, 18, 24, 30, 39
Volovik's emergent gravity program: QFT as low-energy limit of a fermionic vacuum
with Fermi-point universality. Chirality, gauge fields, event horizons, Hawking radiation,
and the cosmological constant all emerge from condensed matter topology. Khoury-Berezhiani
extend this to a concrete superfluid DM model where phonons mediate MOND-like acceleration
at galactic scales while recovering LCDM at cluster scales. Volovik (2024-2025) derives
de Sitter thermodynamics and first law from emergent gravity, establishing Lambda as a
thermodynamic variable conjugate to the Hubble parameter.

### B. Cosmic Web Geometry & Classification (1988-2024)
Papers: 03, 04, 09, 10, 11, 34
Van de Weygaert's DTFE reconstructs continuous density fields from galaxy positions
without smoothing kernels; Hessian eigenvalue classification yields clusters/filaments/
walls/voids. The MMF (Aragon-Calvo) extends this to multiple scales. Geller-Huchra's
CfA survey discovered the Great Wall and established the cosmic web as observational fact.
Bahcall showed clusters are biased tracers with correlation length ~25-50 Mpc. ASTRA (2024)
introduces stochastic topological ranking for DESI-era surveys, achieving 5% agreement
with Sheth-van de Weygaert void size function.

### C. Density Profiles & BAO (1965-2005)
Papers: 05, 06, 08
Einasto's three-parameter density profile (1965) now standard for DM halos, with variable
logarithmic slope gamma = -(2/n)(r/r_s)^{1/n} superior to NFW. The supercluster-void
network (2001) established ~100-130 Mpc quasi-periodicity and 60-70% void fraction.
Eisenstein's BAO detection (2005) established the sound horizon r_s ~ 150 Mpc as a
standard ruler, transforming dark energy measurement.

### D. Void Physics & Cosmological Probes (2014-2025)
Papers: 12, 13, 26, 32, 33
Sutter's VIDE toolkit, Hamaus's void dynamics constraining growth rate f, Contarini's
void-derived S8=0.813, Euclid void size function forecasts (FoM=17 for w0wa),
and Salcedo's DESI Y5 multi-probe forecasts (sigma_8 to 0.8%). Voids probe linear
regime cleanly. Void abundance scales as sigma_8^5. Joint void+galaxy analysis breaks
the (Omega_m, sigma_8) degeneracy.

### E. Giant Structures & Anomalies (2009-2025)
Papers: 14, 15, 16, 20, 21, 22, 25, 29, 31, 35
The anomaly landscape: HCBGW (~3 Gpc, GRB-traced), Giant Arc (~1 Gpc, MgII absorbers),
Big Ring (~400 Mpc diameter, ring morphology), bulk flow 419 km/s at 150 h^{-1} Mpc
(>4 sigma vs LCDM), cosmic dipole >5 sigma across multi-wavelength tracers, and KBC void
(delta ~ -0.46, 250 Mpc radius, 7 sigma combined with H0 tension). Giant structure debate
UNRESOLVED: Sawala (2025) argues gigaparsec structures are common in FLAMINGO-10K;
Lopez-Clowes (2025) apply clustering algorithms to same simulation and find zero such
structures. Method-dependence is the core issue.

### F. Persistent Homology / TDA (2017-2021)
Papers: 27, 28
Pranav (2017) established persistent Betti numbers as the rigorous framework for cosmic
web topology: beta_0 (clusters), beta_1 (filament tunnels), beta_2 (void cavities).
Persistence diagrams separate signal (long-lived features) from noise (short-lived).
Wilding (2021) applied this to LCDM N-body simulations, showing hierarchical formation
sequence and characteristic density scales matching gravitational collapse thresholds.
Validated against Voronoi and Soneira-Peebles synthetic models.

### G. Dark Energy Observational Constraints (2024-2026)
Papers: 17, 19, 23, 36, 37, 38
DESI DR1: w_0 = -1.016 +/- 0.035 (consistent with w=-1). DESI DR2: w_0 = -0.72 +/- 0.08,
w_a = -0.65 +/- 0.40, dynamical DE preferred at 3.1 sigma. Wang-Mota (2025) shows this
preference is driven by dataset tensions and low-z SN systematics; removing z<0.01 SNe
eliminates DDE evidence. Lascu (2024) demonstrates photometric calibration bias of
~0.03 mag in low-z samples. KiDS Legacy (2025): S8 = 0.815 +/- 0.021, resolving
S8 tension to 0.73 sigma from Planck. S8 review (2026): KiDS agrees with CMB but
DES Y6 still shows 2.6 sigma tension -- survey-specific systematics suspected.

---

## Quick Reference

### Key Observational Benchmarks

| Observable | Value | Source | Paper |
|:---|:---|:---|:---|
| BAO scale r_s | ~150 Mpc (comoving) | CMB + SDSS | 08 |
| BAO peak position | 101.6 +/- 3.3 h^{-1} Mpc | SDSS LRGs | 08 |
| Galaxy xi(r) power law | gamma ~ 1.8, r_0 ~ 5 Mpc | CfA survey | 09 |
| Cluster-cluster xi(r) | r_0 ~ 25-50 Mpc | ROSAT/optical | 10 |
| Supercluster-void spacing | ~100-130 Mpc | Einasto catalog | 06 |
| Void fraction of volume | ~60-70% | Einasto survey | 06 |
| Void density contrast | delta ~ -0.8 to -0.95 | VIDE/ZOBOV | 12 |
| Mean void radius (SDSS) | ~24 h^{-1} Mpc | ASTRA | 34 |
| Bulk flow (150 h^{-1} Mpc) | 419 +/- 36 km/s | CF4 | 20 |
| Bulk flow LCDM probability | <0.03% (>3 sigma) | CF4 vs sims | 20 |
| Cosmic dipole excess | 3-5x kinematic | Multi-wavelength | 29, 35 |
| Combined dipole significance | >5.3 sigma | Meta-analysis | 29 |
| KBC void depth | delta ~ -0.46 +/- 0.06 | Surveys | 31 |
| KBC void radius | ~250 Mpc | Surveys | 31 |
| KBC + H0 joint tension | 7.09 sigma vs LCDM | MXXL sims | 31 |
| S8 (KiDS Legacy) | 0.815 +/- 0.021 | KiDS 2025 | 23 |
| S8 (Planck CMB) | 0.834 +/- 0.016 | Planck 2018 | 23, 36 |
| S8 (DES Y6) | 0.768 +/- 0.022 | DES 2025 | 36 |
| w_0 (DESI DR1) | -1.016 +/- 0.035 | DESI BAO | 17 |
| w_0 (DESI DR2) | -0.72 +/- 0.08 | DESI BAO+CMB+SN | 19 |
| w_a (DESI DR2) | -0.65 +/- 0.40 | DESI BAO+CMB+SN | 19 |
| DDE significance (DESI DR2) | 3.1 sigma | Combined | 19 |
| DDE after SN correction | <2 sigma | Wang-Mota | 37 |
| Neutrino mass (LCDM) | < 0.064 eV (95% CL) | DESI DR2 | 19 |
| Sigma_8 (DESI DR1) | 0.777 +/- 0.020 | DESI | 17 |
| Sigma_8 Omega_m^0.6 | ~0.5 | Cluster abundance | 10 |
| Superfluid DM sound speed | ~10 km/s (galactic) | Khoury model | 07, 18 |
| Superfluid DM Jeans length | ~100 kpc | Khoury model | 18 |
| Superfluid DM T_c | ~10^{-6} K | BEC transition | 24 |

### Anomaly Status Summary (2026)

| Anomaly | Significance | Status | Papers |
|:---|:---|:---|:---|
| S8 tension | ~1 sigma (KiDS) | RESOLVED (systematic) | 23, 36 |
| S8 tension | ~2.6 sigma (DES) | OPEN (survey-specific) | 36 |
| DESI w != -1 | 3.1 sigma | CONTESTED (SN systematics) | 19, 37, 38 |
| Bulk flow | >4 sigma | CONFIRMED anomaly | 15, 20 |
| Cosmic dipole | >5 sigma | CONFIRMED anomaly | 29, 35 |
| KBC void | ~6 sigma (void alone) | CONFIRMED structure | 31 |
| KBC + H0 joint | 7.09 sigma | CONFIRMED tension | 31 |
| Giant Arc | >4 sigma | CONTESTED (method-dep) | 16, 21, 22 |
| Big Ring | ~5.2 sigma | CONTESTED (method-dep) | 25, 21, 22 |
| HCBGW | ~3-4 sigma | CONTESTED (selection) | 14 |
| Giant structures debate | -- | UNRESOLVED | 21 vs 22 |

---

## Paper Entries

### Paper 01: Volovik, Universe in a Helium Droplet (2003)
- **Type**: Monograph (Oxford University Press)
- **Key content**: Comprehensive emergent gravity program. Lorentz invariance, gauge fields,
  chirality, cosmological constant, topological defects all emerge from superfluid 3He-A
  Fermi point structure. 16-component spinor universality class.
- **Key equations**: E(p) = hbar v_F |p| (Fermi point dispersion); Dirac equation emergence;
  rho_vac = E_0/V (vacuum energy from ground state)
- **Framework tag**: V01-E1 through V01-E5. VERY HIGH relevance. Conceptual ancestor.

### Paper 02: Volovik, Superfluid Analogies of Cosmological Phenomena (2001)
- **Type**: Review (Physics Reports 351:195-348)
- **Key content**: Event horizons in transonic superfluid flow. Hawking temperature
  T_H = hbar c_B/(2 pi k_B) |dv/dr|_horizon. Axial anomaly from Fermi surface topology.
  CC as equilibrium: rho_vac = E_0/V - mu N/V.
- **Key equations**: V02-E1: Fermi point Green's function; V02-E2: 3He-A order parameter;
  V02-E3: horizon metric ds^2; V02-E4: Hawking temperature; V02-E5: quantized circulation
- **Framework tag**: VERY HIGH. Establishes the condensed matter -> cosmology bridge.

### Paper 03: van de Weygaert & Schaap, Cosmic Web Geometric Analysis (2007)
- **Type**: Lecture notes (LNP 2008/2009)
- **Key content**: DTFE algorithm. Voronoi/Delaunay duality. Betti numbers beta_0 through
  beta_3. Hessian eigenvalue morphological classification. Spine extraction. Filament
  widths 1-5 Mpc, containing ~30-50% of all matter.
- **Key equations**: W03-E1: rho_i = m/V_i^Voronoi; W03-E2: Hessian H_ij of log-density;
  W03-E3: Euler characteristic chi = beta_0 - beta_1 + beta_2 - beta_3
- **Framework tag**: MEDIUM-HIGH. Provides geometric language for testing tessellation.

### Paper 04: van de Weygaert & Schaap, Cosmic Web Connectivity & Topology (2009)
- **Type**: Monograph chapter (LNP 665:291-413)
- **Key content**: Persistent homology of cosmic web. Superlevel set filtration.
  Multiscale Morphology Filter. Filament network is small-world (degree distribution
  P(k) ~ k^{-2.5}). Void network percolation at rho ~ 0.2 mean density.
- **Key equations**: W04-E1: persistence lifetime = rho_birth - rho_death;
  W04-E2: multiscale Hessian H^(sigma); W04-E3: filament degree distribution
- **Framework tag**: MEDIUM-HIGH. Topological toolkit for cosmic web analysis.

### Paper 05: Einasto, Dark Matter Density Profile (1965/1989)
- **Type**: Foundational paper
- **Key content**: Three-parameter profile rho(r) = rho_s exp[-2n((r/r_s)^{1/n} - 1)].
  Variable logarithmic slope. Superior to NFW. Concentration-mass relation.
  Einasto-Sersic mathematical equivalence.
- **Key equations**: E05-E1: Einasto profile; E05-E2: log slope gamma = -(2/n)(r/r_s)^{1/n};
  E05-E3: c(M,z) ~ M^{-0.1}(1+z)^{-1}
- **Framework tag**: MEDIUM. DM profile universality constrains any DM model.

### Paper 06: Einasto et al., Supercluster-Void Network (2001)
- **Type**: Review/catalog
- **Key content**: Supercluster catalog. Void fraction ~60-70%. Filaments 2-5 Mpc wide,
  50-500 Mpc long, carrying 30-50% of mass. Quasi-periodicity claim: lambda_char ~100-130 Mpc
  (controversial). Tidal alignment of elongated structures.
- **Key equations**: E06-E1: delta_void ~ -0.8 to -0.95; E06-E2: lambda_char ~ 100-130 Mpc;
  E06-E3: f_void ~ 0.6-0.7; E06-E4: filament Gaussian profile
- **Framework tag**: MEDIUM-HIGH. Sets the empirical benchmarks for structure.

### Paper 07: Khoury, Dark Matter Superfluid (2015)
- **Type**: Letter (PRD 92:103510)
- **Key content**: DM as axion-like particles condensing into superfluid in galaxies.
  Phonons mediate MOND-like acceleration a_eff = sqrt(a_0 g_N) with a_0 ~ c_s^2/r_0.
  Superfluid at galactic scale, normal at cluster scale. Vortex density n_v = 2 m_phi Omega/hbar.
- **Key equations**: BK07-E1: P = lambda rho^3 (polytropic EOS); BK07-E2: a_eff = sqrt(a_0 g_N);
  BK07-E3: T_c ~ rho^{2/3}; BK07-E4: quantized circulation
- **Framework tag**: VERY HIGH. Direct phononic DM precedent.

### Paper 08: Eisenstein et al., Baryon Acoustic Peak (2005)
- **Type**: ApJ 633:560-574
- **Key content**: First BAO detection in SDSS LRGs. Peak at r_BAO ~ 100 h^{-1} Mpc.
  Sound horizon r_s ~ 150 Mpc as standard ruler. 46,748 galaxies at z ~ 0.35.
- **Key equations**: E08-E1: c_s = c/sqrt(3(1+3rho_b/4rho_gamma));
  E08-E2: r_s = integral c_s dz'/H(z'); E08-E3: xi(r) with BAO peak;
  E08-E4: d_c(z) = c/H_0 integral dz'/E(z')
- **Framework tag**: MEDIUM. BAO is framework-compatible (BCS at 10^{-41}s irrelevant to recombination).

### Paper 09: Geller & Huchra, Mapping the Universe (1989)
- **Type**: Science 246:897-903
- **Key content**: CfA Redshift Survey. Discovery of the Great Wall (>500 Mpc, 15-20 Mpc thick).
  xi(r) ~ (r/5 Mpc)^{-1.8}. First high-resolution 3D map of cosmic web.
- **Key equations**: GH09-E1: xi(r) = (r/r_0)^{-gamma}, gamma ~ 1.8, r_0 ~ 5 Mpc;
  GH09-E2: d = cz/H_0 (Hubble law)
- **Framework tag**: MEDIUM-HIGH. Establishes the observational fact the framework must reproduce.

### Paper 10: Bahcall, Large-Scale Structure from Clusters (1988)
- **Type**: ARA&A 26:631-686
- **Key content**: Cluster dynamics, virial masses, X-ray emission, cluster-cluster correlation
  (r_0 ~ 25-50 Mpc), cluster abundance constraining sigma_8 Omega_m^{0.6} ~ 0.5.
  Supercluster network spacing ~50-100 Mpc.
- **Key equations**: B10-E1: M = sigma_v^2 R/G (virial); B10-E2: n(M) ~ M^{-alpha} exp(-M/M*);
  B10-E3: sigma_8 Omega_m^{0.6} ~ 0.5
- **Framework tag**: MEDIUM. Cluster-scale benchmarks.

### Paper 11: Aragon-Calvo et al., Multiscale Morphology Filter (2007)
- **Type**: A&A 474:315-338
- **Key content**: MMF algorithm. Hessian eigenvalue classification at multiple smoothing scales.
  90% cluster efficiency, 70% filament efficiency. Scale-independent, no density thresholds.
- **Key equations**: AC11-E1: H_ij = d^2 ln(rho_sigma)/dx_i dx_j; AC11-E2: eigenvalue signatures
  for clusters (+,+,+), filaments (+,+,-), walls (+,-,-), voids (-,-,-)
- **Framework tag**: MEDIUM-HIGH. Standard tool for cosmic web classification.

### Paper 12: Sutter et al., Voids as Cosmological Probes (2014)
- **Type**: MNRAS (VIDE toolkit)
- **Key content**: VIDE void finder. Void abundance n_v ~ sigma_8^5. Log-normal size distribution.
  Alcock-Paczynski test with voids. Void stacking analysis.
- **Key equations**: S12-E1: delta_v ~ -0.8 to -0.95; S12-E2: n_v ~ sigma_8^5;
  S12-E3: dR_v/dt = H(z) R_v; S12-E4: f = d ln D/d ln a
- **Framework tag**: MEDIUM. Void statistics as cosmological tool.

### Paper 13: Hamaus et al., Void Dynamics and Dark Energy (2016)
- **Type**: PRL 117:091302
- **Key content**: Void expansion constrains growth rate f(z). RSD in void-galaxy cross-correlation.
  Consistent with LCDM+GR. f(R) gravity ruled out at 2-3 sigma.
- **Key equations**: H13-E1: R_v_ddot + 2H R_v_dot = -4piG/3 rho_bar(1+3w);
  H13-E2: beta = f/b_v; H13-E3: xi(r_perp, r_par) ~ [1+beta mu^2]^2 xi_real
- **Framework tag**: MEDIUM. Void dynamics test gravity model.

### Paper 14: Horvath et al., Hercules-Corona Borealis Great Wall (2014)
- **Type**: arXiv/A&A (2015 confirmation)
- **Key content**: HCBGW: ~3 Gpc structure at z ~ 1.6-2.1 traced by GRBs.
  Significance 3-4 sigma. Multiple comparison and selection effect concerns.
- **Key equations**: H14-E1: d_c(z) = c/H_0 integral dz'/E(z'); significance calculation
- **Framework tag**: LOW-MEDIUM. Controversial. Method-dependent.

### Paper 15: Watkins et al., Cosmic Flows 100 Mpc (2009)
- **Type**: MNRAS 392-407
- **Key content**: Minimum variance bulk flow. V_bulk(100 Mpc/h) ~ 400-600 km/s,
  2-3x LCDM prediction (~200-250 km/s). Dipole analysis.
- **Key equations**: W15-E1: v_pec = v_obs - H_0 d; W15-E2: V_bulk = (1/N) sum v_pec_i;
  W15-E3: MV estimator
- **Framework tag**: MEDIUM. First bulk flow anomaly detection. Superseded by Paper 20.

### Paper 16: Lopez et al., Giant Arc (2022)
- **Type**: MNRAS 516:1557-1573
- **Key content**: ~1 Gpc arc at z ~ 0.8 via MgII absorbers. >4 sigma significance.
  Challenges homogeneity scale assumption.
- **Key equations**: L16-E1: z_abs = (lambda_obs - lambda_rest)/lambda_rest;
  L16-E2: comoving distance; L16-E3: significance sigma
- **Framework tag**: MEDIUM. Part of giant structure debate (Papers 21, 22).

### Paper 17: DESI DR1 BAO Cosmological Constraints (2025)
- **Type**: JCAP / A&A
- **Key content**: Sub-percent BAO at multiple z. Omega_m = 0.296 +/- 0.010.
  w_0 = -1.016 +/- 0.035 (consistent with w=-1). sigma_8 = 0.777 +/- 0.020.
  f(z) consistent with GR. S8 and H0 tensions persist.
- **Key equations**: D17-E1: d_c(z) integral; D17-E2: f = d ln D/d ln a ~ Omega_m^{0.55};
  D17-E3: w(z) = w_0 + w_a(1-a); D17-E4: r_BAO ~ 153.8 Mpc/h
- **Framework tag**: MEDIUM-HIGH. DR1 consistent with framework w=-1 prediction.

### Paper 18: Berezhiani & Khoury, Theory of DM Superfluidity (2015)
- **Type**: PRD 92:103510 (detailed theory)
- **Key content**: Full Lagrangian for self-interacting axion-like DM. Bogoliubov dispersion
  omega(k) = c_s k sqrt(1 + k^2 l_q^2/4). Jeans length lambda_J ~ 100 kpc.
  MOND emerges from phonon-baryon drag. Phase diagram detailed.
- **Key equations**: BK18-E1: L = |d_mu phi|^2 - m^2|phi|^2 - lambda|phi|^4;
  BK18-E2: c_s = sqrt(3 lambda rho^2); BK18-E3: rho_s(T) = rho[1-(T/T_c)^{2/3}];
  BK18-E4: Bogoliubov dispersion; BK18-E5: lambda_J = c_s sqrt(pi/G rho);
  BK18-E6: MOND formula; BK18-E7: vortex density
- **Framework tag**: VERY HIGH. Detailed superfluid DM precedent.

### Paper 19: DESI DR2 BAO Dark Energy (2025)
- **Type**: PRD 112(8), arXiv:2503.14738
- **Key content**: 14M+ objects. 0.24% BAO precision. w_0 = -0.72 +/- 0.08, w_a = -0.65 +/- 0.40.
  DDE preferred at 3.1 sigma over LCDM. Phantom crossing near z ~ 0.5.
  Neutrino mass < 0.064 eV (LCDM), < 0.16 eV (w0wa).
- **Key equations**: D19-E1: xi(r) = integral P(k) j_0(kr) dk; D19-E2: alpha_par, alpha_perp
  dilation parameters; D19-E3: w(a) = w_0 + w_a(1-a)
- **Framework tag**: CRITICAL. 3.1 sigma tension with framework w=-1 prediction.
  ACTIVE THREAT to Tier 4. Contested by Papers 37, 38.

### Paper 20: Watkins et al., CosmicFlows-4 Bulk Flow (2023)
- **Type**: MNRAS, arXiv:2302.02028
- **Key content**: 46,322 galaxies. V_bulk = 419 +/- 36 km/s at 150 h^{-1} Mpc.
  Direction (l,b) = (278,-17), shifted ~20 deg from CMB dipole. P(<0.03%) at 150 Mpc,
  P(<0.003%) at 200 Mpc. >4 sigma LCDM tension. H0-independent method.
- **Key equations**: CF20-E1: V_bulk = integral v(r) d^3r / integral d^3r;
  CF20-E2: chi^2 = sum w_i [d_i^obs - d_i^model(V_bulk)]^2
- **Framework tag**: POST HOC (cannot cite as evidence). Confirmed anomaly.

### Paper 21: Sawala et al., Emperor's New Arc (2025)
- **Type**: MNRAS, arXiv:2502.03515
- **Key content**: FLAMINGO-10K (10,240 Mpc/h box). Gigaparsec structures occur in ~1-5%
  of LCDM realizations. Reconstruction bias inflates overdensities 3-5x.
  No new physics required. Argues giant structures are expected in LCDM.
- **Key equations**: S21-E1: D(a) growth function; S21-E2: density reconstruction via
  Gaussian smoothing + DisPerSE
- **Framework tag**: LOW. Tests LCDM, not the framework directly.
  Contradicted by Paper 22.

### Paper 22: Lopez & Clowes, No Gigaparsec Structures in LCDM (2025)
- **Type**: arXiv:2504.14940
- **Key content**: Reanalyzes FLAMINGO-10K with 3 clustering algorithms (SLHC, CHMS, MST).
  Zero structures > 1 Gpc. Distribution consistent with Poisson (KS p=0.63).
  Argues Sawala's detection was algorithm-dependent false positive.
- **Key equations**: L22-E1: N(>L) for Poisson; SLHC/CHMS/MST linking lengths
- **Framework tag**: LOW. Same simulation, opposite conclusion. DEBATE UNRESOLVED.

### Paper 23: KiDS Legacy, S8 Cosmic Shear (2025)
- **Type**: A&A submitted, arXiv:2503.19441
- **Key content**: S8 = 0.815 +/- 0.021 from 1,347 deg^2. 0.73 sigma from Planck.
  S8 tension RESOLVED. Photo-z improved to sigma_z ~ 0.02. Shear bias |m| < 0.003.
- **Key equations**: K23-E1: S8 = sigma_8 sqrt(Omega_m/0.3); K23-E2: P_gamma(l) lensing
  power spectrum; K23-E3: xi_pm(theta) shear correlation
- **Framework tag**: MEDIUM. S8 resolution removes one anomaly motivation. Framework
  predicts S8 = LCDM (by w=-1 identity theorem), consistent with KiDS.

### Paper 24: Berezhiani et al., Superfluid DM Review (2025)
- **Type**: Living Reviews in GR (forthcoming), arXiv:2505.23900
- **Key content**: Comprehensive 2010-2025 review. Core-cusp resolved. Missing satellites
  reduced 30-50%. SDM mergers 2-5x faster. Lyman-alpha constraint m > 10^{-23} eV.
  Vortex signatures elusive. SDM vs framework: orthogonal hypotheses, simultaneous testing
  possible via rotation curves + LSS + P(k).
- **Key equations**: BK24-E1: GPE for SDM; BK24-E2: phonon dispersion;
  BK24-E3: core density profile; BK24-E4: vortex core radius
- **Framework tag**: HIGH. Distinguishes SDM (bosonic, galactic) from framework (fermionic pairs, cosmological).

### Paper 25: Lopez et al., Big Ring (2024)
- **Type**: arXiv:2402.07591
- **Key content**: ~400 Mpc diameter ring at z ~ 0.8 from MgII absorbers. 5.2 sigma.
  Only ~12 deg from Giant Arc at same z. Ring morphology distinct from filaments/walls.
  Co-location with GA suggests common origin.
- **Key equations**: L25-E1: CHMS convex hull; L25-E2: ring density profile
  rho ~ exp[-(r-R_0)^2/(2w^2)] with R_0 ~ 200 Mpc, w ~ 40 Mpc
- **Framework tag**: MEDIUM. BR + GA co-location at ~400 Mpc separation matches
  32-cell Voronoi cell scale prediction. Requires confirmation.

### Paper 26: Contarini et al., Voids and Cosmology Tensions (2024)
- **Type**: A&A, arXiv:2212.07438
- **Key content**: First void-derived S8 = 0.813 +/- 0.093 from BOSS DR12.
  H0 = 67.3 +/- 10.0 km/s/Mpc. Consistent with Planck, weakly favors lower S8.
  Void number counts + void-galaxy cross-correlation.
- **Key equations**: C26-E1: dn/dR void size function; C26-E2: xi_vg(s,mu) with RSD;
  C26-E3: f(z) = d ln D+/d ln a
- **Framework tag**: MEDIUM. Void-derived cosmological constraints.

### Paper 27: Wilding et al., Persistent Homology of Cosmic Web (2021)
- **Type**: MNRAS, arXiv:2011.12851
- **Key content**: TDA applied to LCDM N-body. Betti curves beta_i(delta) track
  hierarchical formation. Persistence separates signal from noise without thresholds.
  Clusters form at delta > 200, filaments at delta ~ 10-50, voids at delta < 5.
- **Key equations**: Wi27-E1: H_n = ker(d_n)/im(d_{n+1}) (homology);
  Wi27-E2: persistence = d_i - b_i; Wi27-E3: chi = beta_0 - beta_1 + beta_2
- **Framework tag**: HIGH. Provides the tool to test 32-cell tessellation topology
  via persistence diagram comparison.

### Paper 28: Pranav et al., Topology of Cosmic Web via Persistent Betti Numbers (2017)
- **Type**: MNRAS, arXiv:1608.04519
- **Key content**: Framework for persistent Betti numbers applied to cosmic density fields.
  Distinctive persistence diagram signatures for clusters, filaments, walls, voids.
  Voronoi and Soneira-Peebles validation. Automated morphology classification.
- **Key equations**: Pr28-E1: K_t = {x : rho(x) >= t} (superlevel set);
  Pr28-E2: beta_0, beta_1, beta_2 at each threshold;
  Pr28-E3: Voronoi synthetic: rho ~ exp[-d^2/sigma^2]
- **Framework tag**: VERY HIGH. The ideal tool for testing 32-cell prediction.
  No prior work has computed persistence diagrams for regular polytope projections.

### Paper 29: Secrest et al., Cosmic Dipole Anomaly (2025)
- **Type**: arXiv:2505.23526 (RvMP)
- **Key content**: Matter dipole exceeds kinematic expectation by 3-5x.
  Combined >5.3 sigma. Directional consistency across radio, infrared, GRB tracers.
  No LCDM explanation (local voids, perturbations) fully resolves the anomaly.
- **Key equations**: Se29-E1: z_obs = z_rest(1+beta.n); Se29-E2: d_kin ~ v/c ~ 1.2e-3;
  Se29-E3: d_combined = 0.0051 +/- 0.0007
- **Framework tag**: POST HOC. >5 sigma anomaly. Framework's 32-cell tessellation
  naturally predicts anisotropy, but this is post hoc.

### Paper 30: Volovik, de Sitter Thermodynamics and Decay (2024)
- **Type**: Symmetry 16(6):763
- **Key content**: Lambda as emergent from vacuum symmetry. De Sitter is metastable.
  Symmetry breaking -> Lambda reduction. Tunneling rate ~ exp(-S_Euclidean/4).
  Connects inflation and dark energy as different phases of same vacuum condensate.
- **Key equations**: V30-E1: w = 1/2 - 2alpha/3; V30-E2: S_vac ~ (L/l_P)^2;
  V30-E3: Gamma ~ exp[-S_Euclidean/(4 hbar c)]
- **Framework tag**: HIGH. CC as emergent, metastable. Direct ancestor of
  framework's spectral action interpretation of Lambda.

### Paper 31: Haslbauer et al., KBC Void and Hubble Tension (2020)
- **Type**: MNRAS, arXiv:2009.11292
- **Key content**: KBC void delta ~ -0.46, R ~ 250 Mpc. Void WORSENS H0 tension
  (wrong direction: reduces local H0). Combined KBC + H0 at 7.09 sigma vs LCDM.
  MOND + sterile neutrinos reduces to 2.53 sigma.
- **Key equations**: Ha31-E1: rho(r) = rho_0[1 + delta exp(-r/r_void)];
  Ha31-E2: a_void = -4piG/3 Delta_rho r; Ha31-E3: P_joint ~ 10^{-7}
- **Framework tag**: HIGH. KBC void at 6 sigma vs LCDM. Framework's QP depletion
  channel predicts local void from Voronoi cell boundary proximity.

### Paper 32: Salcedo et al., DESI Y5 Void Statistics Forecasts (2025)
- **Type**: arXiv:2504.08221 (PRD submitted)
- **Key content**: DESI Y5 forecasts: sigma(Omega_m)=1.5%, sigma(sigma_8)=0.8% from
  void+galaxy combined. Voids contribute 30% Omega_m info, 50% sigma_8 info.
  Assembly bias increases errors by 8-12%. HOD-based forward modeling.
- **Key equations**: Sa32-E1: n(R_v) void size function; Sa32-E2: Fisher matrix F_ij;
  Sa32-E3: degeneracy reduction r: 0.87 -> 0.34
- **Framework tag**: MEDIUM. Future void precision tests.

### Paper 33: Contarini et al., Euclid Void Size Function (2022)
- **Type**: A&A 668:A169
- **Key content**: Euclid forecasts. Volume-conserving (Vdn) void model. sigma(w) < 10%
  from voids alone. FoM(w0,wa) = 17 from voids; 50 joint with clustering+lensing.
  Void bias b_void ~ 0.2-0.3.
- **Key equations**: Co33-E1: n_Vdn(R_v) = C_0(R_v/R*)^{-3} exp[-(R_v/R*)^{1/2}];
  Co33-E2: b_void(R_v,z) = b_0 + b_1 R_v + b_2 z; Co33-E3: FoM formula
- **Framework tag**: MEDIUM. Euclid void forecasts for dark energy constraints.

### Paper 34: ASTRA Cosmic Web Classification (2024)
- **Type**: RASTI, arXiv:2404.01124
- **Key content**: Stochastic topological ranking using random tracers + Voronoi cells.
  No density interpolation needed. Void size function matches SvdW to 5%.
  Applied to DESI DR2: 7M galaxies, 8,500+ voids. Runs in ~1 min per 1M galaxies.
- **Key equations**: A34-E1: V_i = Voronoi cell definition; A34-E2: rank percentile;
  A34-E3: n_SvdW(R_v) ~ R_v^{-3} exp(-pi R_v^2/R*^2)
- **Framework tag**: MEDIUM. DESI void catalogs available for tessellation test.

### Paper 35: Cosmic Dipole Tensions Multi-Wavelength (2025)
- **Type**: MNRAS 543:3229, arXiv:2509.18689
- **Key content**: Bayesian analysis of 5 datasets: Planck, CatWISE, NVSS, RACS, WISE-5GHz.
  5.1 sigma Planck-CatWISE tension. CatWISE-NVSS concordance. RACS discordant.
  O(10^6) SKA sources needed for 5 sigma test.
- **Key equations**: Di35-E1: I(n) = I_0[1 + sum a_l P_l(cos theta)]; Di35-E2: dipole vector;
  Di35-E3: Bayesian tension via Bayes factor
- **Framework tag**: POST HOC. Confirms and quantifies Paper 29 anomaly.

### Paper 36: S8 Tension Review (2026)
- **Type**: arXiv:2602.12238 (A&A submitted)
- **Key content**: Combined CMB baseline S8 = 0.836 +/- 0.013. KiDS Legacy agrees (0.1 sigma).
  DES Y6 tension 2.6 sigma. eROSITA+SPT clusters 1.4 sigma. KiDS-DES split at 2.4 sigma.
  ~70% of KiDS-DES discrepancy attributable to identified systematics.
- **Key equations**: S8 definitions and weak lensing power spectrum formalism
- **Framework tag**: MEDIUM. S8 tension landscape. Framework survives via KiDS agreement.

### Paper 37: Wang & Mota, DESI DR2 Skeptical Assessment (2025)
- **Type**: EPJC, arXiv:2504.15222
- **Key content**: Individual datasets yield DDE preference < 2 sigma each.
  Combined 3.1 sigma driven by dataset tensions. Removing low-z SNe (z<0.01)
  eliminates DDE preference. Bayesian suspiciousness parameter identifies
  artificial amplification. LCDM compatible when datasets analyzed independently.
- **Key equations**: WM37-E1: Bayesian suspiciousness S = sqrt(Delta chi^2_max);
  WM37-E2: individual Delta chi^2 values (CMB:1.2, BAO:2.8, SNe:3.1);
  WM37-E3: combined Delta chi^2 = 9.4 (exceeds sum of parts by 2.3)
- **Framework tag**: HIGH. Directly supports framework w=-1 prediction.

### Paper 38: Lascu et al., Dark Energy or Supernovae Systematics (2024)
- **Type**: MNRAS 538:875, arXiv:2502.04212
- **Key content**: Low-z SN photometric calibration bias ~0.03 mag. Heterogeneous
  sample composition with sigma_calib ~ 0.08-0.12 mag (2-3x worse than required).
  After correction: DDE preference drops from 3.1 sigma to < 2 sigma.
  Photometrically classified low-z contain ~15% contamination.
- **Key equations**: La38-E1: mu_obs = m_B - M_B = 5 log d_L + 25;
  La38-E2: M_B = M_0 + alpha(s-1) - beta c (standardization);
  La38-E3: Delta mu(z) ~ 0.03 + 0.08z (systematic trend)
- **Framework tag**: HIGH. Identifies SN systematics driving DESI w!=1 claim.

### Paper 39: Volovik, First Law of de Sitter (2025)
- **Type**: JETP Letters 121:766-770, arXiv:2504.05763
- **Key content**: Local thermodynamic formulation of de Sitter. T_local = H/pi (twice
  Gibbons-Hawking). Local entropy density s = pi/(4GH^2). First law dE = TdS + PdV holds
  for arbitrary volumes. Holographic connection: volume-integrated entropy ~ horizon entropy.
- **Key equations**: V39-E1: T_local = H/pi; V39-E2: s = pi/(4GH^2);
  V39-E3: rho = 3H^2/(8piG); V39-E4: S_GH = pi/(GH^2)
- **Framework tag**: HIGH. Thermodynamic foundation for de Sitter as emergent.
  Local temperature formulation connects to framework's spectral action interpretation.

---

## Cross-Paper Equation Concordance

### Dispersion Relations
| Equation | Context | Papers |
|:---|:---|:---|
| E = hbar v_F \|p\| | Fermi point (emergent Lorentz) | 01, 02 |
| omega = c_s k | Phonon long-wavelength | 07, 18, 24 |
| omega = c_s k sqrt(1+k^2 l_q^2/4) | Bogoliubov full | 18, 24 |
| c_s^2 = 3 lambda rho^2 | Polytropic superfluid | 07, 18 |
| c_s = c/sqrt(3(1+3rho_b/4rho_gamma)) | Baryon-photon plasma | 08 |

### Density Profiles
| Equation | Context | Papers |
|:---|:---|:---|
| rho = rho_s exp[-2n((r/r_s)^{1/n}-1)] | Einasto halo profile | 05 |
| rho_NFW = rho_s / [(r/r_s)(1+r/r_s)^2] | NFW (comparison) | 05 |
| rho_fil ~ exp(-r_perp^2/(2sigma^2)) | Filament transverse | 03, 06 |
| rho_void ~ rho_0[1-(r/r_void)^2]^alpha | Void interior | 26 |
| rho_KBC ~ rho_0[1+delta exp(-r/r_void)] | KBC void | 31 |
| rho_ring ~ exp[-(r-R_0)^2/(2w^2)] | Big Ring annulus | 25 |

### Correlation Functions
| Equation | Context | Papers |
|:---|:---|:---|
| xi(r) = (r/r_0)^{-gamma} | Galaxy power law | 09, 10 |
| xi_cluster(r) = (r/r_0)^{-gamma}, r_0~25-50 | Cluster-cluster | 10 |
| xi(r) = xi_smooth + A_BAO exp[-(r-r_s)^2/(2sigma_v^2)] | BAO peak | 08 |
| xi_vg(s,mu) = xi_0(s)[1+beta mu^2] | Void-galaxy RSD | 13, 26 |

### Cosmological Distances and Expansion
| Equation | Context | Papers |
|:---|:---|:---|
| d_c(z) = c/H_0 integral dz'/E(z') | Comoving distance | 08, 14, 16, 17, 19 |
| H(z) = H_0 sqrt(Omega_m(1+z)^3 + Omega_Lambda) | LCDM Hubble | 08, 17 |
| r_s = integral c_s dz'/H(z') | Sound horizon | 08, 17, 19 |
| w(a) = w_0 + w_a(1-a) | CPL parameterization | 17, 19, 33, 37 |

### Structure Growth
| Equation | Context | Papers |
|:---|:---|:---|
| f = d ln D/d ln a | Growth rate | 12, 13, 17, 26 |
| f ~ Omega_m^{0.55} | LCDM approximation | 13, 17 |
| sigma_8 Omega_m^{0.6} ~ 0.5 | Cluster normalization | 10 |
| S8 = sigma_8 sqrt(Omega_m/0.3) | Lensing-optimized | 23, 26, 36 |
| n_v ~ sigma_8^5 | Void abundance scaling | 12 |

### Topological Invariants
| Equation | Context | Papers |
|:---|:---|:---|
| chi = beta_0 - beta_1 + beta_2 | Euler characteristic | 03, 04, 27, 28 |
| persistence = d_i - b_i | Feature lifetime | 04, 27, 28 |
| H_n = ker(d_n)/im(d_{n+1}) | Homology groups | 27, 28 |

### Superfluid/Condensate
| Equation | Context | Papers |
|:---|:---|:---|
| psi = sqrt(rho_s) exp(i phi) | Condensate order parameter | 07, 18, 24 |
| A_i = hbar/(2e) d_i phi | Gauge field from phase | 01, 02 |
| circulation = h/m (quantized) | Vortex quantization | 01, 02, 07, 18 |
| n_v = 2 m_phi Omega/hbar | Vortex density | 07, 18, 24 |
| T_c ~ rho^{2/3} | Critical temperature | 07, 18, 24 |
| rho_vac = E_0/V - mu N/V | CC from equilibrium | 02 |
| T_local = H/pi | de Sitter local temp | 39 |
| s = pi/(4GH^2) | de Sitter entropy density | 39 |
| S_GH = pi/(GH^2) | Gibbons-Hawking entropy | 39 |

### Kinematic/Dipole
| Equation | Context | Papers |
|:---|:---|:---|
| v_pec = v_obs - H_0 d | Peculiar velocity | 15, 20 |
| d_kin ~ v/c ~ 1.2e-3 | Expected kinematic dipole | 29, 35 |
| d_matter = sum w_i n_i / sum w_i | Matter dipole vector | 29, 35 |

---

## Notation Conventions

| Symbol | Meaning | Typical value |
|:---|:---|:---|
| r_s (profiles) | Scale radius of Einasto/NFW | 10-100 kpc |
| r_s (BAO) | Sound horizon at recombination | ~150 Mpc |
| sigma_8 | RMS density fluctuation in 8 Mpc/h spheres | 0.77-0.83 |
| S8 | sigma_8 sqrt(Omega_m/0.3) | 0.77-0.84 |
| xi(r) | Two-point correlation function | -- |
| P(k) | Power spectrum | -- |
| beta_i | Betti numbers (i=0,1,2) | -- |
| f(z) | Growth rate d ln D/d ln a | 0.4-0.5 at z~0 |
| w, w_0, w_a | Dark energy EOS parameters | w=-1 (CC) |
| delta | Density contrast (rho-rho_bar)/rho_bar | -- |
| c_s | Sound speed (context-dependent) | -- |
| h | Dimensionless Hubble H_0/(100 km/s/Mpc) | 0.67-0.73 |
| Mpc | Megaparsec (comoving unless stated) | 3.086e22 m |
| All distances | Comoving unless explicitly stated "proper" | -- |
| Assumed cosmology | Planck 2018 LCDM unless stated otherwise | Omega_m=0.31, h=0.68 |

---

## Computational Verification Status

| Paper | Computation type | Verified? | Notes |
|:---|:---|:---|:---|
| 01, 02 | Analytic (emergent field theory) | N/A | Theoretical framework |
| 03, 04 | DTFE algorithm | [OK] | Standard in cosmology codes |
| 05 | Einasto profile fits | [OK] | Validated against Millennium, Bolshoi |
| 08 | BAO peak extraction | [OK] | Reproduced by BOSS, DESI |
| 11 | MMF algorithm | [OK] | Validated on N-body sims |
| 12 | VIDE void finder | [OK] | Public code, multi-survey |
| 13 | Void RSD analysis | [OK] | SDSS data, consistent with sims |
| 17 | DESI DR1 BAO | [OK] | Collaboration-level validation |
| 19 | DESI DR2 BAO | [OK] | Collaboration-level, but see 37, 38 |
| 20 | CF4 bulk flow | [OK] | 46,322 galaxies, MV method |
| 23 | KiDS shear | [OK] | 1,347 deg^2, multi-validation |
| 27, 28 | Persistent homology | [OK] | GUDHI/CubicalRipser libraries |
| 29, 35 | Dipole estimation | [OK] | Multi-wavelength cross-check |
| 31 | KBC void | [OK] | Multi-survey confirmation |
| 34 | ASTRA classifier | [OK] | Public code, DESI-applied |
| 37 | Dataset tension analysis | [OK] | Independent reanalysis |
| 38 | SN calibration bias | [OK] | Cross-survey photometry |

### Framework-Specific Gates

| Gate | Paper(s) | Status | Notes |
|:---|:---|:---|:---|
| S8-FABRIC-42 | 23, 36 | MOOT | S8 tension resolved. Framework = LCDM by w=-1 |
| DESI w=-1 | 17, 19, 37, 38 | ACTIVE THREAT | DR2 3.1 sigma, but SN-systematic-driven |
| GIANT-VORONOI-42 | 21, 22, 25 | LOW POWER | Predicted ~4700 Mpc vs observed ~1000 Mpc |
| Bulk flow | 15, 20 | POST HOC | >4 sigma, framework predicts but post hoc |
| Cosmic dipole | 29, 35 | POST HOC | >5 sigma, tessellation predicts but post hoc |
| KBC void | 31 | POST HOC | 6 sigma, QP depletion channel predicts but post hoc |
