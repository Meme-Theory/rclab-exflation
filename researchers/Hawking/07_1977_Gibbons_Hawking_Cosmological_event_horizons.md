# Cosmological Event Horizons, Thermodynamics and Particle Creation

**Authors**: G. W. Gibbons, S. W. Hawking
**Year**: 1977
**Journal**: *Physical Review D*, **15**, 2738--2751

---

## Abstract (Analytical Summary)

Gibbons and Hawking extend the thermodynamics of black holes to cosmological horizons. In a de Sitter universe (positive cosmological constant $\Lambda > 0$), every observer is surrounded by a cosmological event horizon at radius $r_H = \sqrt{3/\Lambda}$. They show that this horizon radiates with temperature $T = \hbar H / 2\pi k_B$, where $H = \sqrt{\Lambda/3}$ is the Hubble parameter, and carries entropy $S = A / 4\ell_P^2$, where $A = 4\pi r_H^2$ is the horizon area. The derivation introduces the **Euclidean path integral** method: the thermal Green's functions are obtained by analytically continuing de Sitter space to Euclidean signature, where it becomes a four-sphere $S^4$, and the periodicity of Euclidean time gives the temperature. This Euclidean approach becomes Hawking's preferred method for quantum gravity and is the foundation for the Hartle--Hawking no-boundary proposal.

---

## Historical Context

### From Black Holes to Cosmology

By 1977, Hawking radiation for black holes was established. The natural question was whether other horizons also radiate. The Unruh effect (1976) showed that a uniformly accelerating observer in flat spacetime sees thermal radiation at temperature $T = \hbar a / 2\pi k_B c$, suggesting that the thermal effect is associated with *horizons in general*, not just black hole horizons specifically.

De Sitter space is the maximally symmetric solution of Einstein's equations with positive cosmological constant $\Lambda$. It describes an exponentially expanding universe. An observer at rest sees a cosmological event horizon at the Hubble radius -- causally disconnected regions exist, and information can be permanently lost to the observer. This horizon is structurally similar to a black hole horizon.

### The Euclidean Turn

This paper marks Hawking's pivot toward the Euclidean approach to quantum gravity. Rather than computing Bogoliubov coefficients in Lorentzian signature (as in the 1975 black hole paper), Gibbons and Hawking use the Euclidean path integral. This method is technically simpler and conceptually more elegant, and it becomes the dominant approach in Hawking's subsequent work.

---

## Key Arguments and Derivations

### De Sitter Space: Geometry

The de Sitter metric in static coordinates is:

$$ds^2 = -\left(1 - \frac{r^2}{r_H^2}\right) dt^2 + \left(1 - \frac{r^2}{r_H^2}\right)^{-1} dr^2 + r^2 d\Omega^2$$

where $r_H = \sqrt{3/\Lambda}$ is the cosmological horizon radius. This is structurally identical to the Schwarzschild metric with the replacement $2M/r \to r^2/r_H^2$.

The horizon is at $r = r_H$, where $g_{tt} = 0$. The surface gravity is:

$$\kappa = \left|\frac{1}{2} \frac{d}{dr}\left(1 - \frac{r^2}{r_H^2}\right)\right|_{r=r_H} = \frac{1}{r_H} = H$$

where $H = \sqrt{\Lambda/3}$ is the Hubble constant.

### The Euclidean Method

**Step 1: Wick rotation.** Set $\tau = it$ (Euclidean time). The metric becomes:

$$ds_E^2 = \left(1 - \frac{r^2}{r_H^2}\right) d\tau^2 + \left(1 - \frac{r^2}{r_H^2}\right)^{-1} dr^2 + r^2 d\Omega^2$$

**Step 2: Regularity at the horizon.** Near $r = r_H$, define $\rho^2 = 4r_H^2(1 - r/r_H)$. The metric becomes:

$$ds_E^2 \approx d\rho^2 + \frac{\rho^2}{r_H^2} d\tau^2 + r_H^2 d\Omega^2$$

This is the metric of $\mathbb{R}^2 \times S^2$ in polar coordinates $(\rho, \tau/r_H)$. For the metric to be regular at $\rho = 0$ (no conical singularity), $\tau/r_H$ must be periodic with period $2\pi$:

$$\tau \sim \tau + 2\pi r_H = \tau + \frac{2\pi}{\kappa}$$

**Step 3: Temperature.** The periodicity of Euclidean time is the inverse temperature in quantum statistical mechanics (the KMS condition):

$$\beta = \frac{1}{k_B T} = \frac{2\pi}{\kappa}$$

Therefore:
$$T = \frac{\hbar \kappa}{2\pi k_B} = \frac{\hbar H}{2\pi k_B}$$

For the current universe with $H_0 \approx 70$ km/s/Mpc:
$$T_{\text{dS}} \approx 2.4 \times 10^{-30} \text{ K}$$

This is absurdly small -- about 30 orders of magnitude below the CMB temperature. It would only be relevant in the far future when the universe has diluted all matter and radiation.

**Step 4: The Euclidean geometry is $S^4$.** The complete Euclidean de Sitter space is a four-sphere of radius $r_H$. This can be seen by writing de Sitter space as a hyperboloid in 5D Minkowski space and analytically continuing. The four-sphere is compact and has no boundary, which will be crucial for the no-boundary proposal.

### Entropy of the Cosmological Horizon

The entropy is obtained from the Euclidean action. The gravitational action is:

$$I = -\frac{1}{16\pi G} \int d^4x \sqrt{g} (R - 2\Lambda) + \text{boundary terms}$$

For the Euclidean four-sphere:
- Volume: $\text{Vol}(S^4) = \frac{8\pi^2}{3} r_H^4$
- Ricci scalar: $R = 4\Lambda = 12/r_H^2$
- Action: $R - 2\Lambda = 2\Lambda$

$$I_E = -\frac{1}{16\pi G} \cdot 2\Lambda \cdot \frac{8\pi^2}{3} r_H^4 = -\frac{\pi r_H^2}{G} = -\frac{A}{4G}$$

The partition function is $Z = e^{-I_E}$, and the entropy is:

$$S = \beta \langle E \rangle + \ln Z = \frac{A}{4G} = \frac{\pi r_H^2}{G}$$

(The energy term vanishes for de Sitter by the maximal symmetry.) This gives:

$$S_{\text{dS}} = \frac{A}{4\ell_P^2} = \frac{3\pi}{\Lambda \ell_P^2}$$

For the observed cosmological constant, $S_{\text{dS}} \sim 10^{122}$, which is the largest entropy in the observable universe.

### Schwarzschild--de Sitter: Two Horizons

Gibbons and Hawking also analyze the Schwarzschild--de Sitter spacetime (a black hole in a de Sitter background). The metric is:

$$ds^2 = -f(r) dt^2 + f(r)^{-1} dr^2 + r^2 d\Omega^2, \quad f(r) = 1 - \frac{2M}{r} - \frac{\Lambda r^2}{3}$$

There are two horizons:
- The black hole horizon at $r_+$ (inner)
- The cosmological horizon at $r_{++}$ (outer)

Each has its own surface gravity ($\kappa_+$ and $\kappa_{++}$) and temperature:

$$T_+ = \frac{\hbar \kappa_+}{2\pi k_B}, \qquad T_{++} = \frac{\hbar \kappa_{++}}{2\pi k_B}$$

In general $T_+ \neq T_{++}$, so the system is *not* in thermal equilibrium. There is a steady heat flow from the hotter horizon to the cooler one. The system reaches equilibrium only in the Nariai limit ($r_+ \to r_{++}$), where both temperatures are equal.

The first law for the Schwarzschild--de Sitter black hole involves both horizons:

$$dM = T_+ \, dS_+ = -T_{++} \, dS_{++}$$

The total entropy satisfies $dS_{\text{total}} = dS_+ + dS_{++} \geq 0$.

### The Path Integral and Thermal Green's Functions

The Euclidean path integral provides the thermal propagator directly. The Euclidean Green's function for a scalar field on the four-sphere is:

$$G_E(x, x') = \langle \phi(x) \phi(x') \rangle_\beta$$

This is automatically periodic in Euclidean time with period $\beta = 2\pi/\kappa$, which is the KMS condition for a thermal state. The Lorentzian thermal Green's function is obtained by analytic continuation back to real time.

---

## Physical Interpretation

### The Observer-Dependence of Temperature

The de Sitter temperature is fundamentally observer-dependent -- different observers in de Sitter space see different horizons and, in principle, different temperatures. However, the maximally symmetric (Bunch--Davies) vacuum state is the unique de Sitter-invariant state, and in this state, every geodesic observer sees the same temperature $T = H/2\pi$. This is the analogue of the Unruh effect: a static observer in de Sitter is "accelerating" relative to the cosmological flow (maintaining fixed comoving distance requires acceleration).

### The Meaning of De Sitter Entropy

The entropy $S = A/4\ell_P^2$ of the cosmological horizon is puzzling. For a black hole, the entropy counts microstates (in string theory, this can be done explicitly). For the cosmological horizon, the entropy is observer-dependent and seems to represent the number of degrees of freedom accessible to a single observer in de Sitter space. This is connected to the "holographic principle for de Sitter" and remains an open problem.

Banks and Fischler have proposed that the de Sitter entropy bounds the total Hilbert space dimension of quantum gravity in de Sitter space: $\dim \mathcal{H} = e^{S_{\text{dS}}}$. This has radical implications for the nature of quantum gravity with positive $\Lambda$.

### Connection to Inflation

During inflation, the universe is approximately de Sitter with Hubble parameter $H_{\text{inf}} \sim 10^{13}$ GeV (for high-scale inflation). The Gibbons--Hawking temperature is:

$$T_{\text{GH}} = \frac{H_{\text{inf}}}{2\pi} \sim 10^{12} \text{ GeV}$$

The quantum fluctuations that seed the CMB anisotropies can be understood as thermal fluctuations at this temperature. More precisely, the power spectrum of scalar perturbations is $P_s \propto H^2 / \dot{\phi}^2$, which is related to the Gibbons--Hawking temperature.

---

## Impact and Legacy

### The Euclidean Program

This paper established the Euclidean path integral as a tool for quantum gravity. Subsequent developments include:

- **Hawking--Page transition** (1983): phase transition between thermal AdS and large AdS black holes
- **Hartle--Hawking no-boundary proposal** (1983): the wave function of the universe is defined by a Euclidean path integral over compact geometries
- **Gravitational instantons**: Euclidean solutions (Eguchi--Hanson, Taub-NUT, etc.) as saddle points of the gravitational path integral

### De Sitter Holography

The entropy $S_{\text{dS}} = 3\pi / G\Lambda$ is the starting point for attempts at a "dS/CFT" correspondence (Strominger, 2001). Unlike AdS/CFT, de Sitter holography remains poorly understood, in part because the boundary is spacelike (future infinity) rather than timelike.

### The Cosmological Constant Problem

The de Sitter entropy $S \propto 1/\Lambda$ means that states with smaller $\Lambda$ have more entropy (and hence more microstates). In a landscape picture, this gives a mild preference for small $\Lambda$, though not nearly enough to explain the observed value $\Lambda \sim 10^{-122} \ell_P^{-2}$.

---

## Connections to Modern Physics

1. **Inflation and the trans-Planckian problem**: During inflation, modes are stretched from sub-Planckian to super-Hubble scales. The Gibbons--Hawking temperature provides the thermal "seed" for the inflationary perturbation spectrum. The trans-Planckian problem for inflation is the cosmological version of the same problem for black holes.

2. **Dark energy and horizons**: If dark energy is a true cosmological constant, our universe will asymptotically approach de Sitter space. The Gibbons--Hawking temperature will eventually dominate the thermal environment, but not for $\sim 10^{100}$ years.

3. **Entanglement entropy in de Sitter**: The de Sitter entropy can be understood as entanglement entropy between the degrees of freedom inside and outside the cosmological horizon (analogous to the Hawking radiation calculation). This connects to the Ryu--Takayanagi formula in de Sitter space.

4. **Swampland conjectures**: The "de Sitter swampland conjecture" (Obied, Ooguri, Spodyneiko, Vafa, 2018) claims that consistent quantum gravity theories do not admit stable de Sitter vacua. If true, this would imply that the Gibbons--Hawking analysis applies only approximately, and the true cosmological state is a slowly evolving quintessence.

5. **For the exflation framework**: The Gibbons--Hawking temperature is $T = H/2\pi$, where $H$ is determined by the energy density. In the exflation model, the Hubble expansion is driven by internal compactification energy. The de Sitter temperature would then be related to the rate of change of the internal geometry: $T \propto \dot{\sigma}/\sigma$. The entropy of the cosmological horizon would encode the information content of the internal space visible to a single observer.
