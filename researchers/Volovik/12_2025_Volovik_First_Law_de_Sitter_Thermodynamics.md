# First Law of de Sitter Thermodynamics

**Author(s):** Grigory E. Volovik
**Year:** 2025
**Journal:** JETP Letters, 121(11), 766-770
**arXiv:** 2504.05763

---

## Abstract

This recent paper examines the thermodynamic structure of de Sitter spacetime, establishing that both local and horizon-based perspectives yield consistent thermodynamic descriptions. The key results are:

- **Local thermodynamics in de Sitter**: Every point in de Sitter space is equivalent (homogeneity), so the thermodynamic description is **local** — defined within a Hubble volume with local temperature, entropy density, and energy density.

- **Local temperature of de Sitter**: $T_{local} = \frac{H}{2\pi}$ (in units where $\hbar = k_B = c = 1$), which is **twice** the Gibbons-Hawking temperature $T_{GH} = \frac{H}{4\pi}$.

- **First law consistency**: The first law of thermodynamics holds in both local formulation (within a Hubble volume) and horizon formulation (for the event horizon), with the same temperature.

- **Holographic relation**: The total entropy integrated over a Hubble volume equals the horizon entropy: $\int S_{local} dV = S_{horizon} = \frac{A}{4G}$.

- **Contracting de Sitter**: The framework extends to contracting de Sitter spacetime (time-reversed cosmological evolution), where the entropy density becomes negative in certain regions, indicating a transition to a contracting phase.

- **Implications for dark energy**: The thermodynamic structure suggests that dark energy (driving cosmic acceleration) is a manifestation of the degrees of freedom in the de Sitter vacuum, organized by thermodynamic principles.

The paper reconciles apparent tensions between local and global descriptions of de Sitter thermodynamics, providing a unified framework applicable to cosmology.

---

## Historical Context

### The Cosmological Constant Problem Revisited

Since 1998, observations of accelerating cosmic expansion (Riess, Perlmutter, 2011 Nobel Prize) have established that $\sim 68\%$ of the universe's energy density is in the form of dark energy, consistent with a **cosmological constant** $\Lambda$ (or a slowly-varying dark energy with equation of state $w \approx -1$).

The mysterious aspects:

1. **Why is $\rho_\Lambda$ so small?** The QFT prediction is $10^{113}$ J/m$^3$; observations give $10^{-9}$ J/m$^3$ — a $10^{122}$ discrepancy.

2. **Why now?** Why are we living at the epoch when $\rho_\Lambda \sim \rho_m$ (the coincidence problem)?

3. **What is dark energy microscopically?** Is it a scalar field (quintessence)? A modification of gravity? An emergent phenomenon?

### De Sitter Space as Vacuum Solution

De Sitter spacetime is the solution of Einstein's equations with constant positive cosmological constant:

$$R_{\mu\nu} - \frac{1}{2} R g_{\mu\nu} + \Lambda g_{\mu\nu} = 0$$

The metric in expanding (FRW) coordinates is:

$$ds^2 = -dt^2 + e^{2Ht} (dx^2 + dy^2 + dz^2)$$

where $H = \sqrt{\Lambda / 3}$ is the Hubble parameter (in natural units).

Key property: **De Sitter is maximally symmetric** — it has 10 Killing vectors (like Minkowski space, which also has 10). This means every point is equivalent to every other point; there are no preferred locations.

### Hawking and Gibbons-Hawking Temperature

Hawking (1974) showed that black hole horizons have a temperature:

$$T_{BH} = \frac{\hbar c}{4\pi k_B} \frac{\kappa}{c^2}$$

where $\kappa$ is surface gravity.

For de Sitter space, the cosmological horizon (boundary of the observable universe) also has surface gravity. Gibbons and Hawking (1977) computed:

$$T_{GH} = \frac{H \hbar}{2\pi k_B}$$

in units where $c = 1$.

However, this "temperature" is puzzling: it's not clear what it measures locally, inside the de Sitter space. The horizon is causally disconnected from any observer — how can they measure its temperature?

Volovik's 2025 paper resolves this tension.

---

## Key Arguments and Derivations

### Part I: Local Thermodynamics in Homogeneous Spacetime

#### Energy and Entropy Densities

In a spatially homogeneous spacetime (like de Sitter with expansion factor $a(t) = e^{Ht}$), define the energy density and entropy density as:

$$\rho_E = \rho_{vac} + \rho_m + \rho_r + \ldots$$

where $\rho_{vac}$ is the vacuum energy density (driving cosmic acceleration), and $\rho_m$, $\rho_r$ are matter and radiation densities.

The entropy density per comoving volume is:

$$s = \frac{S}{V_{comoving}} = \frac{d(\rho_E / T)}{d(1/T)}$$

(in thermodynamic equilibrium).

For pure de Sitter (no matter, no radiation):

$$\rho_E = \rho_{vac} = \text{const} = \Lambda / (8\pi G)$$

$$s = s(\rho_{vac}, H)$$

The entropy density depends on both the vacuum energy density and the expansion rate.

#### Thermodynamic First Law (Local Form)

For a small volume $\delta V$ in a Hubble volume, the first law is:

$$d(\rho_E \delta V) = T d(s \delta V) - p d(\delta V)$$

where $T$ is local temperature and $p$ is pressure.

In an expanding background, work is done by cosmic expansion ($p d(\delta V) > 0$ as the volume expands). The first law becomes:

$$d(\rho_E) = T d(s) - (p + \rho_E) \frac{dV}{V} = T d(s) - \rho_E H dt$$

where $H = \dot{a} / a$ is the Hubble parameter.

#### Local Temperature Determination

From the first law, the local temperature is:

$$T = \frac{\partial(\rho_E / s)}{\partial(1/s)}$$

For de Sitter with a quantum vacuum, the entropy per unit volume scales with the Hubble parameter:

$$s \propto H^3 / G$$

(dimensional analysis: entropy is dimensionless times $(1/G)$ times a volume element times $H^3$).

The vacuum energy density is:

$$\rho_E = \frac{\Lambda}{8\pi G} = \frac{3H^2}{8\pi G}$$

Taking the derivative:

$$T = \frac{d(\rho_E / s)}{d(1/s)} = \frac{H}{2\pi}$$

This is **twice** the Gibbons-Hawking temperature $T_{GH} = H / (4\pi)$.

### Part II: Horizon Thermodynamics

#### Apparent Horizon and Event Horizon

In de Sitter, the event horizon is at proper distance:

$$r_H = \frac{1}{H}$$

(the Hubble radius).

The horizon area is:

$$A_H = 4\pi r_H^2 = \frac{4\pi}{H^2}$$

By the Bekenstein-Hawking relation, the horizon entropy is:

$$S_H = \frac{A_H}{4G} = \frac{\pi}{G H^2}$$

#### Entropy Integrated Over Hubble Volume

The local entropy density is $s \propto H^3 / G$. Integrated over a Hubble volume of size $\sim 1/H^3$:

$$S_{total} = \int_V s \, d^3 r \sim (H^3 / G) \times (1 / H^3) \sim 1/G$$

More precisely:

$$S_{total} = \frac{\pi}{G H^2} = S_H$$

**The total entropy within a Hubble volume equals the event horizon entropy.** This is a holographic relation.

#### Consistency of Two Formulations

Local thermodynamics (within a Hubble volume) gives:

- Local temperature: $T_{local} = H / (2\pi)$
- Entropy: $S_{total} = \pi / (GH^2)$
- Energy: $E_{total} = \rho_E \times V = \frac{3H^2}{8\pi G} \times \frac{\pi}{H^3} = \frac{3}{8GH}$

Horizon thermodynamics (using Gibbons-Hawking horizon) gives:

- Temperature: $T_{GH} = H / (4\pi)$
- Entropy: $S_H = \pi / (GH^2)$ [same!]
- ...but the temperature differs by a factor of 2.

The resolution: **The local temperature and Gibbons-Hawking horizon temperature are two different observables.** The local temperature is what an observer within the de Sitter volume measures; the horizon temperature is a theoretical quantity related to the event horizon.

Both satisfy the first law:

$$dE = T d S$$

with appropriate definitions of $E$, $T$, $S$ for each formulation.

### Part III: Contracting de Sitter and Entropy Flow

#### Time-Reversed Cosmology

Consider the time-reverse of cosmic expansion: a contracting universe. The metric becomes:

$$ds^2 = -dt^2 + e^{-2|H|t} (dx^2 + dy^2 + dz^2)$$

Here, $H < 0$ (contracting), and as $t$ increases, the scale factor decreases.

#### Entropy in Contracting Phase

As the universe contracts, the Hubble radius $r_H = 1/|H|$ decreases. The event horizon entropy:

$$S_H = \frac{\pi}{G H^2} \to \infty \quad \text{as } |H| \to 0$$

decreases as $H^{-2}$.

But locally, the entropy density $s \propto H^3$ increases (becomes more negative as $|H|$ grows). This signals a **transition** — at some point, the entropic budget changes sign.

The physical interpretation: as the universe contracts, the degrees of freedom freeze out, and the vacuum state transitions to a different phase (e.g., from dominated by dark energy to dominated by matter or radiation).

### Part IV: Implications for Dark Energy

#### Dark Energy as Vacuum Degrees of Freedom

If dark energy arises from the thermodynamic degrees of freedom of the quantum vacuum, then:

$$\rho_\Lambda = \text{thermodynamic function of } (T, s, H)$$

The observed small value of $\rho_\Lambda$ reflects the vacuum's low entropy density or the particular value of local temperature.

#### Evolution of Dark Energy Equation of State

The equation of state parameter:

$$w = \frac{p}{\rho_E}$$

can vary with time if the thermodynamic structure of the vacuum evolves (e.g., due to quantum transitions or change in the number of effective degrees of freedom).

Current data (DESI 2025) show hints of $w \neq -1$ (dynamical dark energy), with evolution favoring $w_0 \sim -0.72$ at $z = 0$ and possible crossing of $w = -1/3$ at intermediate redshift.

Volovik's framework predicts such evolution naturally: if the vacuum state is thermodynamic, its properties evolve with cosmic history.

#### Testable Predictions

The framework predicts:

1. **Local temperature signature**: Quantum fields in an expanding de Sitter background should exhibit features (energy shifts, decay rates) corresponding to $T_{local} = H / (2\pi)$, not the Gibbons-Hawking temperature.

2. **Entropy flow during transitions**: If the universe undergoes phase transitions (e.g., inflation -> reheating, matter domination -> dark energy domination), the entropy density should exhibit discontinuities or rapid changes, observable in gravitational wave spectra.

3. **Dark energy variations**: If dark energy is thermodynamic, small perturbations in the vacuum state (coupled to matter) should produce observable variations in $w(z)$.

---

## Key Results

1. **De Sitter space has well-defined local thermodynamics**: Every point has local temperature $T = H / (2\pi)$, entropy density, and energy density.

2. **Local and horizon thermodynamics are dual**: The total entropy in a Hubble volume equals the horizon entropy; both perspectives are consistent.

3. **First law applies locally and globally**: The thermodynamic first law is satisfied in both formulations.

4. **Local temperature differs from horizon temperature**: $T_{local} = 2 T_{GH}$. Both are physical but describe different observables.

5. **Contracting de Sitter has negative entropy flow**: A contracting universe exhibits entropy changes signaling phase transitions.

6. **Dark energy is thermodynamic**: The framework suggests dark energy arises from vacuum thermodynamics, not a fundamental constant.

---

## Impact and Legacy

This 2025 paper updates Volovik's thermodynamic understanding of de Sitter space in light of recent cosmological data (DESI 2025 hints at dynamical dark energy). It opens new directions:

- **Quantum thermodynamics**: Extension of the framework to quantum field theory in curved spacetime.

- **Holographic dark energy**: Connection to AdS/CFT and holographic principles.

- **Inflation models**: Reinterpreting inflation as a thermodynamic transition.

- **Observational tests**: Using DESI, Planck, and future surveys to measure $w(z)$ and test thermodynamic predictions.

---

## Connection to Phonon-Exflation Framework

De Sitter thermodynamics directly parallels phonon-exflation's mechanism:

1. **Spectral action as thermodynamic potential**: The spectral action on SU(3) is a thermodynamic function, analogous to Volovik's local temperature and entropy.

2. **Expansion as thermodynamic process**: The expansion of the internal geometry drives evolution along a thermodynamic trajectory, changing the effective dark energy density.

3. **GGE as vacuum state**: The permanent non-thermal GGE relic produced during the cosmological transition is a frozen vacuum state, thermodynamically distinct from the initial BCS phase.

4. **Local temperature and particle creation**: The local temperature $T = H / (2\pi)$ (or the phonon-exflation analog) sets the scale for particle creation at the cosmological horizon — determining the GGE spectrum.

5. **Entropy conservation through transition**: The GGE's 8 Richardson-Gaudin conserved quantities prevent entropy increase during the expansion-driven transition, maintaining an integrated entropy equal to the initial state (holographic relation).

6. **Dark energy time variation**: If phonon-exflation's dark energy is the spectral action's monotonic dependence on the scale of SU(3), then $w(z)$ should vary as the internal geometry evolves — testable by DESI.

---

## References

- Volovik, G. E. (2025). "First law of de Sitter thermodynamics." *JETP Letters*, 121(11), 766-770. arXiv:2504.05763.

- Gibbons, G. W., & Hawking, S. W. (1977). "Cosmological event horizons, thermodynamics, and particle creation." *Physical Review D*, 15(10), 2738.

- Hawking, S. W. (1974). "Black hole explosions?" *Nature*, 248(5443), 30-31.

- Dvali, G., Kahri, S., & Salvio, A. (2020). "Black hole-black hole transitions." arXiv preprint arXiv:2009.10118.
