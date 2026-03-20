# The Rise and Fall of Little Red Dots Could Be Driven by the Environment

**Author(s):** Rosa M. Mérida, Gaia Gaspar, Yoshihisa Asada, Marcin Sawicki, Kiyoaki Christopher Omori, Chris J. Willott, Nicholas S. Martis, Adam Muzzin, Gaël Noirot, Gregor Rihtaršič, Ghassan T. E. Sarrouh, Roberta Tripodi

**Year:** 2025

**Journal:** arXiv:2510.06408

---

## Abstract

The Little Red Dots (LRDs) discovered by JWST show strong redshift evolution—abundant at z > 5, declining at z < 4—suggesting rapid evolutionary timescales or environmental dependence. This work examines the role of local environment (galaxy density, galactic interactions, group/cluster membership) in driving the formation and disappearance of LRDs. Using deep JWST observations of the "Stingray" system (a z = 5.12 galaxy group containing three sources: an AGN, a Balmer-break galaxy, and a star-forming satellite), we identify a transitional AGN object with features intermediate between normal AGN and prototypical LRDs. The transitional object exhibits a blue UV slope (characteristic of LRDs), compact morphology, and broad H-alpha emission, yet occupies the same group environment as star-forming and quiescent systems. We argue that environmental interactions—galaxy-galaxy encounters, dynamical friction, tidal perturbations, and environmental quenching—substantially modulate the properties, prevalence, and lifetimes of LRDs beyond secular (isolated galaxy) evolution alone. The density-dependence of AGN triggering, gas supply, and black hole accretion in groups predicts that LRDs should be overabundant in the highest-density environments at high redshift and preferentially quenched in lower-density environments at lower redshift, consistent with observations. The result has implications for understanding AGN-driven feedback, environmental effects on black hole growth, and the role of galaxy interactions in driving cosmological galaxy evolution.

---

## Historical Context

The discovery of LRDs raised questions about their formation mechanisms: Why do they appear suddenly at z > 5? Why do they decline sharply at z < 4? Two broad classes of explanations emerged:

1. **Intrinsic physics**: All LRDs undergo similar evolution driven by black hole accretion, stellar feedback, or AGN feedback, independent of surroundings (Khan et al. 2026 on SMBH binaries)
2. **Environmental physics**: The prevalence and properties of LRDs depend sensitively on local galaxy density, interactions, and group dynamics

Prior work on AGN triggering in the local universe (e.g., by Kauffmann & Heckman, Silverman et al.) established that galaxy interactions enhance AGN activation on timescales of 0.1-1 Gyr. The idea that environmental effects drive LRD evolution is plausible but had not been directly tested at high redshift.

Mérida et al. 2025 provides the first evidence for environmental modulation of LRD properties via the discovery and detailed characterization of the Stingray system: a compact group at z = 5.12 containing multiple objects with different evolutionary states.

---

## Key Arguments and Derivations

### Galaxy Environment Classification

The local environment of a galaxy is characterized by density contrast $\delta$ and distance to nearest neighbor d_nn. A standard classification is:

- **Isolated**: $\delta < 1$, d_nn > 2 Mpc (comoving)
- **Field**: $1 < \delta < 5$, 0.5 Mpc < d_nn < 2 Mpc
- **Group**: $5 < \delta < 50$, 0.1 Mpc < d_nn < 0.5 Mpc
- **Cluster**: $\delta > 50$, d_nn < 0.1 Mpc

The Stingray system contains three sources within a projected separation of ~50 kpc and a velocity dispersion ~300 km/s, classifying it as a compact group.

For a group with N members and rms velocity dispersion $\sigma_v \sim 300$ km/s, the virial mass is:

$$M_{\text{vir}} \sim \frac{3 \sigma_v^2}{G} r_{\text{vir}} \sim \frac{3 \times (300 \text{ km/s})^2}{G} \times (50 \text{ kpc}) \sim 1e12 - 1e13 M_\odot$$

The corresponding overdensity relative to cosmic mean is:

$$\delta \sim \frac{\rho_{\text{group}}}{\rho_{\text{mean}}} \sim \frac{M_{\text{vir}} / (4\pi r_{\text{vir}}^3 / 3)}{\rho_{\text{mean}}} \sim 10-50$$

This confirms group-level environment.

### AGN Triggering Efficiency in Groups

The probability that a galaxy hosts an AGN depends on environmental density:

$$P_{\text{AGN}}(z, \delta) = P_0(z) \times f(\delta, \sigma_v)$$

where:
- $P_0(z)$ is the AGN fraction in the field
- $f(\delta, \sigma_v)$ is an enhancement factor that increases with density and velocity dispersion

Empirically, studies of AGN in groups find enhancements of order f ~ 1.5-3 for intermediate groups (delta ~ 10-30) and f ~ 3-10 for dense clusters (delta > 50).

The physical mechanism is tidal triggering: a close encounter with a neighbor galaxy induces a tidal disturbance in the primary galaxy's disk. The disturbance can trigger a bar, drive gas toward the nucleus, and fuel nuclear accretion:

$$\Delta M_{\text{accr}} = \epsilon_{\text{tidal}} \times M_{\text{gas}}$$

where $\epsilon_{\text{tidal}} \sim 0.01-0.1$ is the efficiency of tidal-induced gas transport. For a group member with gas mass M_gas ~ 1e9-1e10 solar masses, the induced accretion rate is:

$$\dot{M}_{\text{accr}} \sim \epsilon_{\text{tidal}} \times M_{\text{gas}} / t_{\text{dyn}} \sim 0.1 \, M_\odot/\text{yr}$$

(if t_dyn ~ 100 Myr). This is sufficient to activate an AGN with L_bol >> 1e44 erg/s, consistent with LRD luminosities.

### The Stingray System: Transitional Morphology

The Stingray system comprises:

1. **LRD-like AGN**: Compact (R_1/2 ~ 0.2 kpc), red optical color (M_5000 - M_3000 ~ 1.5 mag), broad H-alpha (FWHM ~ 3000 km/s), ionization diagnostic indicates AGN. Properties are intermediate between prototypical LRDs and normal Seyfert 2 galaxies.

2. **Balmer-break galaxy**: Compact star-forming system with H-alpha emission, young age (t ~ 50-200 Myr inferred from SED fitting), quiescent core surrounded by star-forming disk.

3. **Satellite galaxy**: Dwarf, star-forming, showing signs of tidal interaction (asymmetric morphology, kinematics consistent with tidal stripping).

The spatial arrangement and kinematics suggest the system is in the process of dynamical evolution: the satellite is being tidally stripped, and the LRD-like AGN is at the transition between AGN-active and quiescent phases.

The existence of a transitional object bridging LRD and normal AGN properties suggests that environmental processes can gradually modulate LRD characteristics on ~100 Myr timescales.

### Predicted Environmental Dependence of LRD Abundance

If LRD formation and activation are environmentally-triggered, the abundance should correlate with environment. A model prediction is:

$$n_{\text{LRD}}(z, \delta) = n_0(z) \times (1 + \delta / \delta_0)^\beta$$

where:
- $n_0(z)$ is the LRD abundance in the field (delta = 0)
- $\delta_0$ is a characteristic overdensity
- $\beta \sim 0.5-1.5$ (depends on tidal triggering efficiency)

At z ~ 5-6, galaxies preferentially occupy denser environments (driven by hierarchical structure formation). Thus, the high abundance of LRDs at z > 5 is partly due to the prevalence of group/cluster-like environments at these redshifts.

At z < 4, the universe becomes less dense on average (structures have expanded), and galaxies are more likely to be in field-like environments. The low abundance of LRDs at z < 4 reflects this environmental transition, not just intrinsic evolution of individual systems.

The predicted evolution of field LRD abundance is:

$$\frac{n_{\text{LRD}}^{\text{field}}(z=2)}{n_{\text{LRD}}^{\text{field}}(z=6)} \sim 0.5 - 0.3$$

(slower decline than observed in total population), while the environmental enhancement factor declines from f ~ 3 at z ~ 5 to f ~ 1.5 at z ~ 2, explaining the strong evolution in total LRD abundance.

---

## Key Results

1. **The Stingray galaxy group at z = 5.12 contains a transitional AGN object with features intermediate between LRDs (blue UV, compact, broad lines) and normal AGN, demonstrating continuity in AGN properties driven by environment.**

2. **The group environment (delta ~ 10-30, velocity dispersion ~ 300 km/s) exhibits enhanced AGN activation and black hole accretion due to tidal interactions and gas dynamical effects, consistent with predictions of environmental AGN triggering.**

3. **The spatial arrangement and kinematics of the Stingray system suggest ongoing tidal perturbations and dynamical evolution, implicating environmental interactions in modulating AGN properties on ~100 Myr timescales.**

4. **Models of LRD abundance predict strong environmental dependence: LRDs should be overabundant in high-density group/cluster environments at z > 5, and underabundant in low-density field environments at z < 4.**

5. **The environmental enhancement of AGN triggering (factor f ~ 2-3 in groups) combined with the evolution of mean density from z ~ 5 to z ~ 2 can explain the observed strong evolution in LRD abundance without invoking dramatic changes in intrinsic AGN physics.**

6. **Environmental quenching mechanisms (ram-pressure stripping, starvation, heating) can suppress black hole growth and AGN activity at z < 4 as galaxies fall into higher-density environments and feedback processes accelerate.**

7. **Future high-resolution JWST surveys of z > 5 galaxy groups will enable detailed tests of the environmental hypothesis and constrain the timescales of AGN triggering and quenching.**

---

## Impact and Legacy

This paper has become important for understanding LRD environmental context. Its impacts include:

- **Introducing environmental feedback loops**: The work demonstrates that galaxy interactions and group dynamics substantially modulate AGN activity at high redshift, complementing black hole mass-dependent and gas supply-dependent models.
- **Explaining the redshift evolution of LRD abundance**: By attributing the decline in LRD abundance from z > 5 to z < 4 to environmental changes (not just intrinsic evolution), the paper provides a framework for predicting LRD demographics in different cosmic environments.
- **Motivating group-level surveys**: The discovery of transitional objects and the prediction of enhanced AGN in groups drives new observational programs targeting high-z groups and proto-clusters.
- **Constraining AGN feedback efficiency**: The timescales of environmental AGN activation and subsequent quenching constrain the coupling between black holes and their surroundings.

---

## Connection to Phonon-Exflation Framework

**Indirect connection via structure formation and environmental enhancement of AGN.**

In the phonon-exflation framework, if the expansion history or power spectrum of density fluctuations differs from LCDM at high redshift, this would affect the formation and prevalence of high-density environments (groups, clusters) at z > 5.

Specifically:

1. **Modified power spectrum**: If the instanton relic enhances density fluctuations on small scales (group-scale ~ 1-10 Mpc), then groups would form earlier and more abundantly in phonon-exflation. This would increase the predicted LRD abundance at z > 5 (via enhanced environmental AGN triggering).

2. **Modified expansion rate**: If H(z) differs from LCDM at z > 6, this would change the redshift at which structures reach a given virial density, potentially shifting the predicted peak in LRD abundance.

3. **Enhanced black hole growth in groups**: If phonon-exflation enhances black hole growth globally (via faster accretion or more numerous seeds), this would further amplify the environmental effect by providing more massive black holes to activate via tidal triggering.

Currently, both frameworks are degenerate at z < 7. However, detailed measurements of group/cluster abundance at z ~ 5-7 (via JWST observations) and the correlation of AGN activity with environment could distinguish phonon-exflation from LCDM.

**Closest thematic link**: The environmental dependence of LRD abundance is a demographic signature testable against both LCDM and phonon-exflation. If future observations show that high-z groups in phonon-exflation produce more LRDs than LCDM (via enhanced power spectrum or expansion rate effects), this would provide evidence for the framework. The Stingray system serves as a local anchor for such comparisons.
