# Black Hole Explosions?

**Authors**: Stephen W. Hawking
**Year**: 1974
**Journal**: *Nature*, **248**, 30--31

---

## Abstract (Analytical Summary)

In this brief but revolutionary letter to *Nature*, Hawking announces that black holes are not truly black: quantum mechanical effects cause them to emit thermal radiation at a temperature inversely proportional to their mass. This *Hawking radiation* has temperature $T = \hbar \kappa / 2\pi k_B c$, where $\kappa$ is the surface gravity. For a Schwarzschild black hole, $T = \hbar c^3 / 8\pi G M k_B$. The radiation causes the black hole to lose mass, shrink, heat up (negative heat capacity), and ultimately evaporate completely in a catastrophic final burst -- a "black hole explosion." This two-page paper is arguably the most important result in theoretical physics of the latter half of the twentieth century, as it sits at the intersection of general relativity, quantum mechanics, and thermodynamics, and gives rise to the information paradox.

---

## Historical Context

### The Bekenstein Challenge

By 1973, Bekenstein had proposed that black holes carry entropy proportional to their horizon area. Hawking had resisted this idea: classically, a black hole at temperature $T > 0$ should radiate, but nothing can escape a black hole, so $T = 0$. If $T = 0$ and $S > 0$, the third law of thermodynamics is violated. Hawking set out to refute Bekenstein by performing a careful calculation of quantum field theory in the curved spacetime of a collapsing black hole.

### The Calculation That Backfired

Hawking's calculation was motivated by discussions with Zel'dovich and Starobinsky (1971--1973), who had argued that rotating black holes should amplify certain modes of quantum fields (superradiant scattering). This is the wave analogue of the Penrose process. Zel'dovich even argued that a rotating black hole should spontaneously emit particles in the superradiant modes.

Hawking set out to compute the particle creation rigorously using the formalism of quantum field theory on curved spacetime. To his surprise, the result was not limited to rotating black holes or superradiant modes: *all* black holes emit thermal radiation, at a temperature set by the surface gravity. The very calculation meant to disprove Bekenstein ended up confirming that black hole entropy is real and given by:

$$S_{\text{BH}} = \frac{k_B c^3 A}{4 G \hbar} = \frac{A}{4 \ell_P^2} k_B$$

with the precise coefficient $1/4$ that Bekenstein had left undetermined.

---

## Key Arguments and Derivations

### The Nature Letter: Qualitative Argument

The 1974 *Nature* letter is short (two pages) and presents the result qualitatively. The full derivation appeared in 1975 (see next analysis). The key arguments in the letter are:

**1. Pair creation near the horizon**: In the quantum vacuum, virtual particle-antiparticle pairs are constantly being created and annihilated. Near a black hole horizon, the tidal gravitational field can separate the pair before they recombine. One particle falls into the black hole (with effectively negative energy as measured at infinity), while the other escapes to infinity as real radiation. The black hole loses mass by the amount of energy carried away.

**2. Thermal spectrum**: Hawking claims (and demonstrates in the 1975 paper) that the spectrum of emitted particles is *exactly thermal* -- a Planck/blackbody spectrum. The temperature is:

$$T_H = \frac{\hbar \kappa}{2\pi k_B c}$$

For a Schwarzschild black hole with surface gravity $\kappa = c^4/(4GM)$:

$$T_H = \frac{\hbar c^3}{8\pi G M k_B}$$

In SI units, for a solar-mass black hole:
$$T_H = \frac{1.227 \times 10^{23} \text{ kg}}{M} \text{ K} \approx 6 \times 10^{-8} \text{ K} \quad (M = M_\odot)$$

This is absurdly cold -- far below the CMB temperature of 2.725 K. Astrophysical black holes are net *absorbers*, not emitters.

**3. Negative heat capacity and evaporation**: Since $T \propto 1/M$, as the black hole radiates and loses mass, it gets *hotter*. This is a negative heat capacity: $C = dE/dT = -8\pi G M^2 k_B / \hbar c$. The process is thermodynamically unstable -- a runaway. The evaporation accelerates, and in the final moments, the black hole becomes very hot and very small, releasing its remaining energy in a burst.

**4. Evaporation timescale**: The Stefan--Boltzmann law gives the luminosity:

$$L = \sigma A T^4 \cdot \Gamma$$

where $\sigma$ is the Stefan--Boltzmann constant, $A = 16\pi G^2 M^2/c^4$ is the horizon area, and $\Gamma$ is a greybody factor (the fraction of radiation that escapes to infinity rather than being reflected back by the spacetime curvature). Combining:

$$\frac{dM}{dt} = -\frac{L}{c^2} \propto -\frac{1}{M^2}$$

Integrating:
$$t_{\text{evap}} = \frac{5120 \pi G^2 M_0^3}{\hbar c^4} \approx 2 \times 10^{67} \left(\frac{M_0}{M_\odot}\right)^3 \text{ years}$$

For a solar-mass black hole, this is $\sim 10^{67}$ years -- vastly longer than the age of the universe. But for a primordial black hole of mass $M \sim 10^{12}$ kg (mountain-mass), the evaporation time is comparable to the age of the universe, and such objects would be exploding *now*. Hawking noted this as a potentially observable signature.

**5. The final state problem**: What happens at the very end? When $M \to 0$, $T \to \infty$, and quantum gravity effects must become important (at $M \sim M_P = \sqrt{\hbar c/G} \approx 2.2 \times 10^{-8}$ kg). Hawking noted this as an open question -- it remains open.

### Temperature from Surface Gravity

The key formula $T = \hbar \kappa / 2\pi k_B$ deserves unpacking. The surface gravity $\kappa$ for a general stationary black hole is:

- Schwarzschild: $\kappa = \frac{1}{4M}$ (geometrized units)
- Kerr: $\kappa = \frac{\sqrt{M^2 - a^2}}{2M(M + \sqrt{M^2 - a^2})}$
- Reissner--Nordstrom: $\kappa = \frac{\sqrt{M^2 - Q^2}}{(M + \sqrt{M^2 - Q^2})^2}$
- Kerr--Newman: combines both

For extremal black holes ($a = M$ or $Q = M$), $\kappa = 0$ and $T = 0$: extremal black holes do not radiate. This is consistent with the third law of black hole mechanics.

### The Information Problem (Seeds)

Though the information paradox is only implicit in the 1974 letter, its seeds are clearly present. If the radiation is exactly thermal, it carries no information about what fell into the black hole (beyond total mass, charge, and angular momentum). If the black hole evaporates completely, the initial pure quantum state of the collapsing matter has been converted into a mixed thermal state -- a violation of unitarity. Hawking would make this argument explicit in 1976.

---

## Physical Interpretation

### Particle Creation in Curved Spacetime

The fundamental mechanism is not "virtual particles becoming real" (which is a heuristic), but rather the non-uniqueness of the vacuum state in curved spacetime. In flat spacetime, all inertial observers agree on the vacuum. In curved spacetime, the vacuum defined by an observer at early times (before the black hole forms) is different from the vacuum defined by an observer at late times (after the horizon has formed). The early-time vacuum, when decomposed into late-time modes, contains particles -- and these particles have a thermal spectrum.

### Why Thermal?

The thermal nature of the radiation is deeply connected to the structure of the event horizon. The horizon is a Killing horizon, and the Killing vector that generates it has the structure of a boost (Lorentz transformation) in the near-horizon region. The vacuum state restricted to one side of a Rindler horizon is a thermal state (this is the Unruh effect, discovered by Unruh in 1976 partly inspired by Hawking's result). The Hawking temperature is the black hole's version of the Unruh temperature:

$$T_{\text{Unruh}} = \frac{\hbar a}{2\pi c k_B}$$

where $a$ is the proper acceleration. For an observer hovering at the horizon, $a \to \infty$ but the redshift factor exactly compensates, yielding the finite Hawking temperature at infinity.

### Negative Heat Capacity and the Microcanonical Ensemble

The negative heat capacity $C = dE/dT < 0$ means that black holes cannot be in stable thermal equilibrium with a heat bath (in asymptotically flat spacetime). This is characteristic of self-gravitating systems generally (Lynden-Bell and Wood, 1968). In a canonical ensemble (fixed temperature), a black hole is unstable. In a microcanonical ensemble (fixed energy), a black hole can be a stable maximum-entropy state -- but only if confined (as in AdS space, leading to the Hawking--Page transition).

---

## Impact and Legacy

### Immediate Impact

The paper was initially met with skepticism. DeWitt recalled that most relativists were "stunned." The result was independently checked by Parker, Wald, and others using different methods, and all confirmed the thermal spectrum.

### Bekenstein--Hawking Entropy

Combining the first law $dM = (\kappa/8\pi) dA + \ldots$ with the temperature $T = \hbar\kappa/2\pi$:

$$dM = T \cdot \frac{dA}{4\hbar} + \ldots$$

identifies $S = A / 4\ell_P^2$ (in natural units). This is the *Bekenstein--Hawking entropy*, one of the most important formulas in physics:

$$S_{\text{BH}} = \frac{k_B c^3}{4 G \hbar} A = \frac{A}{4 \ell_P^2}$$

For a solar-mass black hole: $S \sim 10^{77} k_B$.

### Primordial Black Holes

Hawking noted that primordial black holes (PBHs) of mass $\sim 10^{12}$ kg would be evaporating today. The non-detection of gamma-ray bursts from PBH explosions constrains the PBH abundance, which in turn constrains the density fluctuations in the early universe. This remains an active area of research.

### The Information Paradox

The most profound legacy is the information paradox, which has driven theoretical physics for 50 years and led to the holographic principle, AdS/CFT, the firewall argument, and the island formula. See analyses of the 1976 and 2005 papers.

---

## Connections to Modern Physics

1. **Analogue Hawking radiation**: In 2016--2019, Steinhauer reported observation of correlated pairs of phonons in a BEC analogue black hole, consistent with Hawking's prediction. The phononic analogue confirms the kinematic (non-gravitational) nature of the effect.

2. **Hawking radiation and the Schwinger effect**: Particle creation by the horizon is mathematically analogous to Schwinger pair creation in a strong electric field ($T_{\text{Schwinger}} \sim eE\hbar/m^2c^3$). Both are tunneling phenomena.

3. **Black hole information**: The thermal spectrum implies information loss if taken at face value. Resolution attempts include: remnants (information stored in Planck-mass relics), baby universes, complementarity (Susskind), firewalls (AMPS, 2012), and the island formula (2019). The last of these, combining quantum extremal surfaces with the replica trick, appears to derive the Page curve from semiclassical gravity, suggesting information is preserved.

4. **Trans-Planckian problem**: The outgoing Hawking quanta, when traced back to the horizon, are exponentially blueshifted to trans-Planckian frequencies. This means the prediction relies on physics at arbitrarily high energies. Unruh and others have shown that the thermal spectrum is robust against modifications of the dispersion relation at high energies (universality), which is precisely the analogue gravity insight -- the details of the UV physics do not matter.

5. **For the exflation framework**: In a Kaluza--Klein context, the Hawking temperature would depend on the internal geometry through the surface gravity. If the internal dimensions evolve (exflation), the effective 4D Hawking temperature of primordial black holes would change over cosmological time, potentially providing a distinctive observational signature compared to standard evaporation.
