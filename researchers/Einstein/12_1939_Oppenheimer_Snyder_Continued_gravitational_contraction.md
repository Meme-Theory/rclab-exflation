# On Continued Gravitational Contraction

**Authors:** J. Robert Oppenheimer, Hartland Snyder
**Year:** 1939
**Journal:** *Physical Review*, **56**, 455--459

---

## Abstract

Oppenheimer and Snyder demonstrate that a sufficiently massive star, having exhausted its nuclear fuel, will undergo continued gravitational collapse without limit, forming what is now called a black hole. By solving the Einstein field equations for a spherically symmetric, pressureless dust cloud collapsing from rest, they show that the surface of the star crosses the Schwarzschild radius in finite proper time (as measured by an observer on the surface), even though a distant observer sees the collapse asymptotically freeze at the Schwarzschild radius. This paper provides the first correct, fully relativistic description of gravitational collapse and establishes that black holes are a genuine prediction of general relativity, not merely a mathematical curiosity.

---

## Historical Context

### The Chandrasekhar Limit (1931)

Subrahmanyan Chandrasekhar showed in 1931 that a white dwarf -- a star supported against gravity by electron degeneracy pressure -- has a maximum mass of approximately $1.4\,M_\odot$ (the Chandrasekhar mass). Above this limit, electron degeneracy pressure is insufficient to support the star, and it must either collapse further or find another support mechanism.

### Neutron Stars and the Oppenheimer-Volkoff Limit (1939)

Earlier in 1939, Oppenheimer and Volkoff computed the structure of neutron stars (supported by neutron degeneracy pressure) and found a similar maximum mass, now estimated at approximately $2-3\,M_\odot$ (the Tolman-Oppenheimer-Volkoff limit). Above this mass, no known physical mechanism can prevent collapse.

### The Schwarzschild "Singularity"

The Schwarzschild metric:

$$ds^2 = -\left(1 - \frac{r_s}{r}\right)c^2 dt^2 + \left(1 - \frac{r_s}{r}\right)^{-1}dr^2 + r^2 d\Omega^2$$

where $r_s = 2GM/c^2$, has an apparent singularity at $r = r_s$: the $g_{rr}$ component diverges. For decades, this was widely believed to represent a physical singularity, and many physicists (including Einstein himself) argued that no physical process could produce a configuration with $r < r_s$.

The crucial insight that $r = r_s$ is a coordinate singularity (removable by a change of coordinates) and not a physical singularity was not widely understood until the 1950s and 1960s (Eddington-Finkelstein coordinates, 1924/1958; Kruskal-Szekeres coordinates, 1960). However, Oppenheimer and Snyder's 1939 analysis already demonstrated the physical reality of the horizon crossing, without needing these later coordinate systems.

### Einstein's Resistance

Einstein published a paper in 1939 (the same year!) arguing that the Schwarzschild singularity could not be realized in nature. He considered particles in circular orbits and showed that stable circular orbits exist only for $r > 3r_s$, concluding that matter could not reach $r = r_s$. This argument was wrong -- it assumed particles remain in circular orbits, whereas collapse involves radial infall.

---

## Key Arguments and Derivations

### I. The Model: Pressureless Dust

Oppenheimer and Snyder consider the simplest possible model of stellar collapse: a uniform-density sphere of pressureless dust (matter with zero pressure, $p = 0$). The stress-energy tensor is:

$$T^{\mu\nu} = \rho u^\mu u^\nu$$

This idealization ignores all the complex physics of real stellar collapse (pressure gradients, nuclear reactions, neutrino emission, magnetic fields, rotation) and focuses on the pure gravitational dynamics.

The justification for ignoring pressure: once the mass exceeds the Oppenheimer-Volkoff limit, no pressure can halt the collapse. The qualitative behavior -- formation of a horizon and singularity -- is independent of the equation of state.

### II. Interior Solution: Friedmann Cosmology in Reverse

The interior of the dust cloud is homogeneous and isotropic (by symmetry), and its dynamics are therefore described by a Friedmann-type solution. The metric inside the cloud is:

$$ds^2_{interior} = -c^2 d\tau^2 + a^2(\tau)\left[\frac{d\chi^2}{1 - k\chi^2} + \chi^2 d\Omega^2\right]$$

where $\tau$ is the proper time of a comoving dust particle, $a(\tau)$ is the scale factor, and $k > 0$ for a cloud that starts from rest (the "closed" Friedmann solution, but in reverse -- contracting instead of expanding).

The Friedmann equation for pressureless dust is:

$$\left(\frac{\dot{a}}{a}\right)^2 = \frac{8\pi G\rho}{3} - \frac{kc^2}{a^2}$$

With the initial condition $\dot{a}(0) = 0$ (starting from rest) at $a(0) = a_0$, and using the conservation law $\rho a^3 = \rho_0 a_0^3$, the solution is a cycloid:

$$a(\eta) = \frac{a_0}{2}(1 + \cos\eta)$$

$$\tau(\eta) = \frac{a_0}{2c\sqrt{k}}(\eta + \sin\eta)$$

where $\eta$ is the conformal time parameter, running from $\eta = 0$ (maximum expansion) to $\eta = \pi$ (collapse to $a = 0$).

The surface of the cloud has comoving coordinate $\chi_0$, and its areal radius is:

$$R(\tau) = a(\tau)\chi_0$$

This decreases monotonically from $R_0 = a_0\chi_0$ to $R = 0$.

### III. Exterior Solution: Schwarzschild

By Birkhoff's theorem, the spacetime outside the spherically symmetric dust cloud must be the Schwarzschild geometry, regardless of the details of the interior dynamics. The exterior metric is:

$$ds^2_{exterior} = -\left(1 - \frac{r_s}{r}\right)c^2 dt^2 + \left(1 - \frac{r_s}{r}\right)^{-1}dr^2 + r^2 d\Omega^2$$

where $r_s = 2GM/c^2$ and $M$ is the total mass of the cloud.

### IV. Matching at the Surface

The interior and exterior metrics must be matched at the surface of the cloud ($\chi = \chi_0$). This matching determines the relationship between the interior time $\tau$ and the exterior Schwarzschild time $t$:

$$\frac{dt}{d\tau} = \frac{\sqrt{1 - \frac{r_s}{R_0}} \cdot \frac{R}{R_0}}{1 - \frac{r_s}{R}}$$

### V. The Two Perspectives

**Comoving observer (on the surface):** The surface radius $R(\tau)$ passes through $r_s$ smoothly in finite proper time $\tau$. The observer notices nothing special at $r = r_s$ -- no infinite tidal forces, no divergent curvature. The collapse continues to $R = 0$ (the physical singularity) in additional finite proper time.

The total proper time from the start of collapse ($R = R_0$) to the singularity ($R = 0$) is:

$$\tau_{total} = \frac{\pi R_0}{2c}\sqrt{\frac{R_0}{r_s}} = \frac{\pi}{2}\sqrt{\frac{R_0^3}{2GM}}$$

For a star with $R_0 = 10^6$ m and $M = 3M_\odot$: $\tau_{total} \sim 0.06$ s. The collapse to a singularity takes a fraction of a second.

**Distant observer:** As the surface approaches $r_s$, the Schwarzschild coordinate time $t$ diverges:

$$t \to \infty \quad \text{as} \quad R \to r_s$$

The distant observer sees the collapsing surface asymptotically approach $r_s$ but never quite reach it. Light signals from the surface are progressively redshifted:

$$\frac{\lambda_{observed}}{\lambda_{emitted}} = \frac{1}{\sqrt{1 - r_s/R}} \to \infty$$

The star dims exponentially on a timescale $\Delta t \sim r_s/c$ and effectively vanishes. The distant observer never sees the horizon form -- but the star fades from view, leaving a dark region from which no light escapes.

### VI. The Singularity

At $R = 0$ (equivalently, $a = 0$), the density diverges: $\rho \to \infty$. The Kretschmann scalar (a coordinate-invariant measure of curvature) diverges:

$$K = R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma} \propto \frac{1}{R^6} \to \infty$$

This is a genuine physical singularity, not a coordinate artifact. The singularity theorems of Penrose (1965) and Hawking (1966-67) later showed that singularity formation is generic under much weaker assumptions than those used by Oppenheimer and Snyder.

---

## Physical Interpretation

### The Event Horizon

The surface $r = r_s$ is the event horizon -- a one-way membrane that light and matter can cross inward but not outward. Inside the horizon, all future-directed timelike and null paths lead to the singularity. The horizon is a global concept defined by the causal structure of the spacetime, not by any local measurement.

The key physical point is that the horizon is not a material surface -- nothing dramatic happens at $r = r_s$ from the infalling observer's perspective. It is defined by the global inability of signals to escape to infinity.

### Gravitational Redshift and Frozen Stars

The Soviet school of physics (Zeldovich, Novikov) initially called these objects "frozen stars" because of the apparent freezing of the collapse as seen by distant observers. The term "black hole" was popularized by John Wheeler in 1967 and more accurately captures the physics: the star has not frozen but has collapsed past the point of no return. The apparent freezing is an artifact of the Schwarzschild coordinate time.

### The Inevitability of Collapse

The Oppenheimer-Snyder solution demonstrates that gravitational collapse is an inevitable consequence of GR for sufficiently massive objects. There is no static equilibrium beyond the neutron star limit. This was deeply uncomfortable for many physicists -- Einstein, Eddington, and others spent years trying to find mechanisms that could prevent collapse. The Penrose singularity theorem (1965) ended these hopes by proving that once a trapped surface forms, a singularity is inevitable (under reasonable energy conditions).

---

## Impact and Legacy

### The Long Delay

The Oppenheimer-Snyder paper was largely ignored for over two decades. World War II diverted physicists' attention, and the result was considered a mathematical idealization with no astrophysical relevance. The revival came in the 1960s:

- **Kruskal-Szekeres coordinates (1960):** Demonstrated that the Schwarzschild "singularity" at $r = r_s$ is merely a coordinate artifact.
- **Quasars (1963):** The discovery of quasars (enormously luminous, compact objects at cosmological distances) demanded an energy source that only gravitational collapse could provide.
- **Penrose's singularity theorem (1965):** Proved that singularity formation is generic, not an artifact of perfect spherical symmetry.
- **Kerr solution (1963):** The rotating black hole solution, more astrophysically realistic than Schwarzschild.
- **Hawking radiation (1974):** Black holes are not entirely black -- they emit thermal radiation with temperature $T = \hbar c^3/(8\pi G M k_B)$.

### Observational Confirmation

Black holes are now confirmed through multiple lines of evidence:
- **X-ray binaries:** Compact objects accreting from companion stars, with masses exceeding the neutron star limit.
- **Galactic center:** The orbits of stars around Sgr A* imply a mass of $\sim 4\times10^6\,M_\odot$ within $\sim 10$ AU (Ghez, Genzel; Nobel 2020).
- **Gravitational waves:** LIGO/Virgo detections of binary black hole mergers, confirming the existence and dynamics of horizons.
- **Event Horizon Telescope (2019):** Direct imaging of the shadow of M87's central black hole.

---

## Connections to Modern Physics

### The Information Paradox

Hawking's discovery that black holes evaporate raises a fundamental question: what happens to the information that fell into the black hole? If the black hole evaporates completely into thermal radiation, the evolution is non-unitary -- pure states evolve into mixed states, violating quantum mechanics. This "information paradox" remains one of the central open problems in quantum gravity. Recent progress (island formula, Page curve from replica wormholes) suggests information is preserved, but the mechanism involves radical modifications to our understanding of spacetime geometry.

### Numerical Relativity and Binary Black Holes

The Oppenheimer-Snyder solution describes a single collapsing object. The merger of two black holes requires numerical solution of the full Einstein equations. The breakthrough simulations of 2005-2006 (Pretorius; Baker et al.; Campanelli et al.) solved this problem and provided the waveform templates essential for LIGO detections.

### Gravitational Collapse and the Cosmic Censorship Conjecture

Penrose's cosmic censorship conjecture (1969) states that singularities formed by gravitational collapse are always hidden behind event horizons -- there are no "naked singularities" visible from infinity. This conjecture remains unproven in full generality, though it holds for the Oppenheimer-Snyder solution and for all known astrophysically realistic collapse scenarios.

### Analog Black Holes

In condensed matter systems, acoustic horizons can be created by flowing fluids that exceed the local speed of sound. Phonons in the supersonic region cannot escape to the subsonic region, creating an analog event horizon. Unruh (1981) proposed that these analog black holes should exhibit analog Hawking radiation -- a prediction confirmed in BEC experiments (Steinhauer, 2016). These analog systems provide a laboratory testing ground for quantum effects in curved spacetime, connecting the gravitational physics of this paper to quantum fluid dynamics.
