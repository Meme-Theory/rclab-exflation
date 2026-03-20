# On the Fate of Little Red Dots

**Author(s):** Escala et al.
**Year:** 2025
**Journal:** arXiv:2509.20453

---

## Abstract

Little Red Dots represent a new dynamical regime in stellar systems: compact, massive stellar clusters at z~5-7 with dynamical timescales shorter than the age of the universe at those epochs. Numerical simulations of LRD dynamics show that these systems are gravitationally unstable and undergo runaway collisional merging of their stellar populations, producing a central supermassive object within 10^7-10^8 years. This mechanism naturally explains key LRD observational characteristics: their transient nature (they do not persist to lower redshift as identifiable LRDs), their typical X-ray faintness (most lack sufficient mass concentration to power AGN at observable X-ray levels), and their apparent black hole masses (which grow from stellar mergers rather than gas accretion). The framework unifies LRDs as a distinct evolutionary phase in the formation of the first supermassive black holes, predicting that LRD descendants populate the z~2-3 quasar population and that contemporaneous z~5-7 systems with longer dynamical timescales should not produce runaway mergers. Testing predictions requires spectroscopic redshift and morphological follow-up of z>4 galaxies.

---

## Historical Context

The JWST discovery of LRDs initially prompted a crisis interpretation: if these objects are indeed harboring billion-solar-mass black holes at z>5, how can such massive objects form so quickly? This led to a proliferation of exotic mechanisms: ultra-strongly self-interacting dark matter (uSIDM), fuzzy dark matter solitons, extreme direct collapse, and others.

However, an alternative perspective emerged: what if LRDs are not long-lived systems hosting stable supermassive black holes, but rather a *transient phase* in the assembly of black hole seeds? In this picture, LRDs are young stellar clusters or galactic nuclei in which stellar mergers and collisional interactions naturally produce a massive central object. The object may not be a black hole in the sense of harboring an event horizon, but rather a massive star, a quasi-star (a mass-inflated object with quasi-stellar envelope), or a black hole in the early stages of formation.

The evolutionary timescale becomes critical. If the dynamical time of an LRD is comparable to or shorter than the age of the universe at z~5-7, then collisional runaway is inevitable, and the system cannot remain a stable stellar cluster—it must evolve rapidly toward a more compact configuration.

---

## Key Arguments and Derivations

### Dynamical Timescale in LRDs

The characteristic dynamical timescale for a self-gravitating system is:

$$\tau_{dyn} = \sqrt{\frac{3\pi}{32 G \rho_c}} \approx \frac{r_{half}}{v_{disp}}$$

where $\rho_c$ is the central density, $r_{half}$ is the half-light radius, and $v_{disp}$ is the velocity dispersion.

For an LRD with:
- Half-light radius: $r_{half} \sim 100-300$ pc
- Velocity dispersion: $v_{disp} \sim 100-300$ km/s
- Central density: $\rho_c \sim 10^4 M_\odot / \text{pc}^3$

we get:

$$\tau_{dyn} \sim \frac{100-300 \text{ pc}}{100-300 \text{ km/s}} \sim 10^7 \text{ Myr} \sim 0.1-1 \text{ Gyr}$$

Meanwhile, the age of the universe at z~5-7 is:

$$t_{univ}(z=5) \sim 1.1 \text{ Gyr}$$
$$t_{univ}(z=7) \sim 0.76 \text{ Gyr}$$

**This is a remarkable coincidence**: the dynamical timescale of an LRD is comparable to or *shorter* than the age of the universe at the epoch it is observed. This is an "unexplored regime" in stellar dynamics—most observed stellar systems (globular clusters, galactic nuclei) have dynamical times much shorter than their age (allowing them to reach quasi-equilibrium) or longer than their age (allowing them to appear collisionless). LRDs occupy a unique middle ground.

### Collisional Runaway Mechanism

In systems where $\tau_{dyn} \gtrsim t_{age}$, collisional interactions become important. The collision rate in a stellar system is:

$$\Gamma_{collision} = \int n(\mathbf{r}) \sigma_{collision}(v) v d^3v d^3\mathbf{r}$$

where $n(\mathbf{r})$ is the number density and $\sigma_{collision}$ is the geometric cross-section for close approaches.

For stars with stellar radius $R_\star$ and relative velocity $v_{rel}$:

$$\sigma_{collision} \approx \pi (2 R_\star)^2 \approx 10^{-22} \text{ cm}^2 \quad \text{(for } R_\star \sim 10^{11} \text{ cm, giant stars)}$$

In a dense LRD nucleus with $n \sim 10^{3-4}$ stars/pc^3:

$$\Gamma_{collision} \sim 10^{-4}-10^{-3} \text{ yr}^{-1}$$

meaning **one stellar collision occurs every 10,000-100,000 years** in the LRD core. Over the 1-Gyr observation epoch, hundreds to thousands of collisions accumulate.

Each collision produces:
1. **Mass concentration**: Two stars merge into a single, more massive object
2. **Energy release**: Orbital kinetic energy ~0.1-1 M_sun c^2 is converted to heat and radiation, expelled as ejecta
3. **Shrinkage of system**: Energy loss via collisional ejecta causes the system to contract, increasing density and collision rate

### Runaway Cascade

Once a sufficiently massive central object forms (through the first few collisions), dynamical friction becomes important. This object (which may be a supermassive star) sinks toward the system center, accreting additional stars via tidal disruption and/or direct collision. The process is runaway because:

- As the central mass $M_c$ increases, the dynamical friction timescale $\tau_{fric} \propto 1/M_c$ decreases
- Decreasing friction timescale accelerates the rate of accretion
- Accretion rate increases, leading to faster mass growth
- The system enters a runaway regime where a single object rapidly dominates the system mass

The growth timescale for the central object is:

$$\frac{dM_c}{dt} \sim \int \rho(r) v(r) \sigma(r) dr$$

For LRD parameters, numerical simulations find:

$$\tau_{runaway} \sim 10^7-10^8 \text{ years}$$

i.e., the system reaches runaway and forms a quasi-black-hole object within ~10-100 Myr.

### Formation of Massive Objects

The result of collisional runaway is a central object with mass:

$$M_{central} \sim 0.01-0.1 \times M_{LRD,tot} \sim 10^5-10^7 M_\odot$$

depending on the initial total mass of the LRD.

This object is not necessarily a black hole in the classical sense. If the mass is below the nuclear burning limit (~10^6 M_sun), it forms a **supermassive star**—a quasi-equilibrium object supported by radiation pressure and non-Newtonian effects. For masses above this threshold, the object rapidly contracts to black hole densities on dynamical timescales, forming an event horizon.

### X-ray Faintness Explanation

A key puzzle in LRD observations is that many show no detectable X-ray emission, despite hosting apparently massive black holes. Standard AGN models predict copious X-ray emission from accretion disks around black holes.

The collisional runaway model explains this naturally: during the collision phase, the system is dynamically violent but does not yet have a stable accretion disk. Gas is shredded and dispersed in collisions; accretion is chaotic and intermittent. X-ray emission (which requires a coherent accretion flow with strong shock heating) is suppressed.

Only after the runaway phase completes and the system settles into a quasi-stable configuration does a classical accretion disk form, producing bright X-ray and infrared emission. Thus, the youngest LRDs (those caught in the midst of runaway) appear X-ray faint; older remnants (z~2-3 systems descended from LRDs) show strong AGN signatures.

### Evolutionary Pathways

The paper traces several possible evolutionary outcomes:

**Pathway A: Rapid Merger to Black Hole (most common)**
- LRD at z~5-6 undergoes runaway in ~100 Myr
- Forms ~10^6-10^7 M_sun black hole or supermassive star
- Begins Eddington-limited gas accretion (L ~ L_E)
- Grows to ~10^8-10^9 M_sun by z~3
- Becomes observable quasar with normal AGN properties by z~2
- Descendants: Type 2 (obscured) and Type 1 (unobscured) AGN at z~2-3

**Pathway B: Slower Merger with Subsequent Growth**
- LRD at z~6 has longer dynamical time (lower density)
- Runaway extends to ~500 Myr; central object reaches only ~10^5 M_sun
- Remains sub-Eddington or super-Eddington for extended period
- Grows slowly to ~10^8 M_sun by z~2
- Observable as luminous JWST sources at z~4-5 with different spectral properties

**Pathway C: Disruption / No Merger**
- LRD in lower-density environment has $\tau_{dyn} \gg t_{age}(z)$
- Collisional interactions insufficient to trigger runaway
- System remains a stellar cluster or disperses
- No black hole forms; system merges into larger galaxy via hierarchical assembly
- Descendants: normal z~2-3 galaxies without central black hole excess

---

## Key Results

1. **Dynamical timescales unexpectedly short**: LRDs exhibit $\tau_{dyn} \sim 0.1-1$ Gyr, comparable to the age of the universe at z~5-7. This is unique among observed stellar systems.

2. **Collisional runaway is inevitable**: Given the short dynamical time and dense stellar population, hundreds to thousands of stellar collisions occur before z~4. A runaway cascade naturally develops.

3. **Supermassive object forms rapidly**: Central object reaches $M_c \sim 10^5-10^7 M_\odot$ within 10^7-10^8 years, explaining the presence of massive objects at very high redshift without extreme accretion.

4. **X-ray faintness explained**: Young LRDs (in the runaway phase) lack stable accretion disks, producing little X-ray emission. X-ray bright AGN emerge only after system settles.

5. **LRDs are transient**: The LRD phase lasts ~0.1-0.5 Gyr. Objects either evolve to lower-redshift AGN (Pathway A) or disperse (Pathway C). No LRDs should persist as identifiable systems to z~2.

6. **Descendants are high-z quasars**: LRD descendants are the unobscured and obscured AGN populations at z~3-4, with black hole masses consistent with collisional growth predictions.

7. **Criterion for runaway**: Systems with velocity dispersion $v_{disp} > 100$ km/s and size $r < 1$ kpc are vulnerable to runaway. Redshift-z systems with gentler profiles avoid runaway.

---

## Impact and Legacy

This paper shifted the conceptual framing of LRDs from "black hole seed formation problem" to "stellar dynamics and collision cascade problem." It motivated deeper investigation into the morphologies, kinematics, and spectral properties of LRDs, with the goal of identifying which systems are in the midst of collisional runaway.

The work has inspired:
- Detailed N-body simulations of LRD-like systems with realistic stellar mass functions
- Spectroscopic searches for signs of stellar collisions (blue horizontal-branch stars, unusual chemical abundances)
- Models of the spectral energy distribution (SED) of runaway-phase systems, distinct from both normal stellar clusters and mature AGN
- Gravitational wave searches for merging black holes descended from LRD collisions

---

## Connection to Phonon-Exflation Framework

**INDIRECT RELEVANCE**: This paper addresses the *fate* and *evolutionary timescale* of LRDs, rather than their initial seed formation mechanism. Its discriminant value is secondary to Papers 32-34, which directly challenge the framework's CDM prediction.

**Mechanism compatibility**: Regardless of whether LRDs form via CDM (direct collapse), uSIDM (gravothermal collapse), or ULDM (solitonic collapse), the collisional runaway dynamics apply. The paper is agnostic about seed origin.

**Observational implications**: If LRDs are confirmed to be short-lived transients evolving to z~2-3 AGN, this constrains the formation redshift of LRD precursors and reduces tension between black hole masses at z~5 and z~2. This is *consistent* with phonon-exflation's CDM-based predictions (which naturally produce a staggered assembly timescale). If, conversely, some LRDs persist as identifiable systems to z~3, this argues for immediate (z~5) seed formation and rapid growth, potentially favoring exotic dark matter models over CDM.

**Verdict**: This paper is a **redshift evolution chronometer** for the LRD population. It does not directly falsify phonon-exflation but constrains the allowed assembly pathway. If LRDs are confirmed short-lived, CDM-based phonon-exflation is reinforced. If long-lived or static, exotic dark matter (and thus challenges to phonon-exflation) are favored.
