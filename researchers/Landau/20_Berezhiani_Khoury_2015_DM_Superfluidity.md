# Theory of Dark Matter Superfluidity

**Author(s):** Lasha Berezhiani, Justin Khoury
**Year:** 2015 (v2: March 2016)
**Journal:** Physical Review D 92, 103510 (2015)
**arXiv:** 1507.01019
**Relevance:** MEDIUM — structural parallel

---

## Abstract

We propose a novel theory of dark matter (DM) superfluidity that matches the successes of the LCDM model on cosmological scales while simultaneously reproducing the MOdified Newtonian Dynamics (MOND) phenomenology on galactic scales. The DM and MOND components have a common origin, representing different phases of a single underlying substance. DM consists of axion-like particles with mass of order eV and strong self-interactions. The condensate has a polytropic equation of state $P \propto \rho^3$ giving rise to a superfluid core within galaxies. Instead of behaving as individual collisionless particles, the DM superfluid is more aptly described as collective excitations. Superfluid phonons, in particular, are assumed to be governed by a MOND-like effective action and mediate a MONDian acceleration between baryonic matter particles. Our framework naturally distinguishes between galaxies (where MOND is successful) and galaxy clusters (where MOND is not): due to the higher velocity dispersion in clusters, and correspondingly higher temperature, the DM in clusters is either in a mixture of superfluid and normal phase, or fully in the normal phase. The rich and well-studied physics of superfluidity leads to a number of observational signatures: array of low-density vortices in galaxies, merger dynamics that depend on the infall velocity vs phonon sound speed; distinct mass peaks in bullet-like cluster mergers, corresponding to superfluid and normal components; interference patterns in super-critical mergers. Remarkably, the superfluid phonon effective theory is strikingly similar to that of the unitary Fermi gas, which has attracted much excitement in the cold atom community in recent years.

---

## Key Arguments and Derivations

### Motivation: CDM vs MOND

CDM succeeds on cosmological scales (CMB, LSS, cluster abundances) but faces challenges on galactic scales (BTFR scatter, too-big-to-fail, planar satellites). MOND succeeds on galactic scales (rotation curves, BTFR as exact consequence) but fails on cluster scales and for the CMB. The authors propose unification: DM and MOND are different phases of one substance.

### Superfluid Phonon EFT (Section 2)

In the non-relativistic regime, superfluid phonons are described by:

$$\mathcal{L} = P(X), \quad X = \dot{\theta} - m\Phi - \frac{(\nabla\theta)^2}{2m}$$

where $\theta$ is the phonon field, $\Phi$ is the gravitational potential, and $m$ is the DM particle mass. The type of superfluid is encoded in the choice of $P$. The authors postulate:

$$P(X) \propto X\sqrt{|X|}$$

corresponding to a superfluid with equation of state $P \propto \rho^3$. This non-analytic $X^{3/2}$ power is the non-relativistic MOND scalar action. The phonon-baryon coupling $\mathcal{L}_{int} \propto \theta\,\rho_b/M_{Pl}$ mediates a MONDian force.

The $P \propto \rho^3$ equation of state implies 3-body interactions dominate (2-body negligible), analogous to the Unitary Fermi Gas where $\mathcal{L}_{UFG} \propto X^{5/2}$ (fixed by 4D scale invariance).

### DM Particle Requirements (Section 3)

- **Mass**: $m \sim$ eV (de Broglie wavelength must overlap in galaxies: $\lambda_{dB} \sim 1/(mv) \gtrsim$ interparticle spacing)
- **Self-interaction**: $\sigma/m \gtrsim 0.1\,\text{cm}^2/\text{g}$ (thermalization within galaxies)
- **Critical temperature**: $T_c \sim$ mK (comparable to cold atom BEC temperatures)
- **Coupling**: $\Lambda \sim$ meV (to reproduce MOND critical acceleration $a_0$)

### Superfluid Halo Profile (Section 4)

Assuming hydrostatic equilibrium with $P \propto \rho^3$, the condensate density profile is cored:

$$\rho(r) \propto \frac{\sin(kr)}{kr}$$

The condensate size is $\sim 100$ kpc for Milky-Way mass galaxies. In the inner region, baryonic motion is dominated by the phonon-mediated MOND force; in the outer region, the DM condensate provides the dominant gravitational force.

### Phase Structure (Section 5)

At finite temperature, the Landau two-fluid description applies: the superfluid fraction decreases with temperature. Galaxy clusters have higher velocity dispersion and thus higher DM temperature, pushing them into mixed phase or normal phase — naturally explaining why MOND fails for clusters.

### Observational Signatures (Sections 9-11)

- Quantized vortices in galaxy halos (inter-vortex spacing $\sim$ mm for $m \sim$ eV)
- Merger dynamics sensitive to phonon sound speed
- Bullet-cluster-like separations between superfluid and normal DM components
- Interference patterns in supercritical mergers

---

## Key Results

1. DM superfluidity unifies CDM (cosmological scales) and MOND (galactic scales) as different phases of one substance
2. The phonon EFT $P(X) \propto X^{3/2}$ reproduces the MOND force law through phonon-baryon coupling
3. The equation of state $P \propto \rho^3$ implies dominance of 3-body interactions
4. DM particle parameters: $m \sim$ eV, $\Lambda \sim$ meV, $T_c \sim$ mK
5. Cored density profiles arise naturally from hydrostatic equilibrium
6. Galaxy clusters are in the normal phase, explaining MOND's failure there
7. The phonon EFT is strikingly similar to the Unitary Fermi Gas

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Phonon EFT | $\mathcal{L} = P(X)$, $X = \dot{\theta} - m\Phi - (\nabla\theta)^2/(2m)$ | Eq. (4) |
| MOND phonon action | $P(X) \propto X\sqrt{\lvert X\rvert}$ | Eq. (5) |
| Phonon-baryon coupling | $\mathcal{L}_{int} \propto \theta\,\rho_b/M_{Pl}$ | Eq. (6) |
| BTFR | $M_b = v_c^4/(G_N a_0)$ | Eq. (3) |
| Equation of state | $P \propto \rho^3$ | Eq. (7) |
| MOND force law | $a = \sqrt{a_N a_0}$ for $a_N \ll a_0$ | Sec. 1.1 |
| Critical acceleration | $a_0 \simeq \frac{1}{6}H_0 \simeq 1.2 \times 10^{-8}\,\text{cm/s}^2$ | Eq. (2) |

---

## Relevance to Phonon-Exflation

This paper provides a structural parallel to the phonon-exflation framework: both propose that macroscopic phenomena (dark matter/MOND here, particle spectrum/expansion there) emerge from phononic excitations of a condensed state. The key difference is that Berezhiani-Khoury work with a real superfluid in 3+1D, while the framework works with a BCS condensate on the internal SU(3) manifold. The $P \propto \rho^3$ equation of state from 3-body interactions has a possible connection to the framework's instanton gas (dense 3-body processes dominating the pairing dynamics). The phase structure (superfluid inside galaxies, normal in clusters) mirrors the framework's transit picture (condensed at early times, excited post-transit).
