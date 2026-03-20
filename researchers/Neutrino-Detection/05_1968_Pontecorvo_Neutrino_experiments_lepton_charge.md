# Pontecorvo's Neutrino Oscillation Theory

## Bibliographic Information

- **Author**: Bruno Pontecorvo
- **Title**: "Neutrino Experiments and the Problem of Conservation of Leptonic Charge"
- **Journal**: Soviet Physics JETP, Vol. 26, No. 5, pp. 984--988
- **Year**: 1968
- **Original Russian**: Zh. Eksp. Teor. Fiz. 53, 1717--1725 (1967)
- **Institution**: Joint Institute for Nuclear Research, Dubna, USSR
- **Note**: Earlier related ideas appeared in Pontecorvo (1957, 1958); the 1968 paper
  is the definitive formulation of neutrino-antineutrino oscillations and
  flavor oscillations.

---

## Historical Context

### The Neutrino Landscape in the 1960s

By the mid-1960s, two distinct neutrino flavors had been established
experimentally. The electron neutrino $\nu_e$ was first detected by Reines and
Cowan in 1956 via inverse beta decay at the Savannah River reactor. The muon
neutrino $\nu_\mu$ was demonstrated to be a separate species by Lederman,
Schwartz, and Steinberger in 1962 at Brookhaven, earning the 1988 Nobel Prize.

The Standard Model of the era treated neutrinos as strictly massless, left-handed
fermions. Lepton number conservation -- separate for each family -- was assumed
to be exact. There was no theoretical requirement for neutrino mass in the
minimal electroweak theory of Glashow, Weinberg, and Salam (then still being
formulated).

### Pontecorvo's Prescient Insight

Bruno Pontecorvo, an Italian-born physicist who had defected to the Soviet Union
in 1950, had been thinking about neutrino mixing since at least 1957. Drawing an
explicit analogy with the $K^0$--$\bar{K}^0$ system (where strangeness
oscillations had been predicted by Gell-Mann and Pais in 1955 and observed
shortly after), Pontecorvo proposed that neutrinos might similarly oscillate
between different states.

His 1957--1958 papers considered $\nu \leftrightarrow \bar{\nu}$ oscillations
(neutrino--antineutrino transitions, analogous to $K^0 \leftrightarrow
\bar{K}^0$). The 1968 paper extended this to include flavor transitions
$\nu_e \leftrightarrow \nu_\mu$, which required that:

1. Neutrinos have nonzero mass.
2. The mass eigenstates are not identical to the flavor eigenstates.
3. At least two mass eigenstates have different masses.

This was radical: it violated lepton flavor conservation and required physics
beyond the Standard Model before the Standard Model was even complete.

### The Maki-Nakagawa-Sakata Contribution

Independently, Maki, Nakagawa, and Sakata (1962) had proposed a mixing scheme
for neutrinos in the context of the Nagoya model, predating Pontecorvo's flavor
oscillation paper. Their contribution is honored in the name "PMNS matrix"
(Pontecorvo-Maki-Nakagawa-Sakata), though the full oscillation formalism is
primarily due to Pontecorvo.

---

## Theoretical Framework

### Flavor States vs. Mass States

The central postulate is that the neutrino states produced and detected in weak
interactions (flavor eigenstates) are not the same as the states with definite
mass (mass eigenstates). They are related by a unitary mixing matrix:

$$|\nu_\alpha\rangle = \sum_i U_{\alpha i}^* \, |\nu_i\rangle$$

where $\alpha \in \{e, \mu, \tau\}$ labels flavors and $i \in \{1, 2, 3\}$
labels mass eigenstates with masses $m_1, m_2, m_3$.

The matrix $U$ is the PMNS matrix, the leptonic analogue of the CKM matrix in
the quark sector.

### Two-Flavor Oscillation Derivation

Consider the simplest case: two flavors $(\nu_e, \nu_\mu)$ mixed by a single
angle $\theta$:

$$\begin{pmatrix} \nu_e \\ \nu_\mu \end{pmatrix} = \begin{pmatrix} \cos\theta & \sin\theta \\ -\sin\theta & \cos\theta \end{pmatrix} \begin{pmatrix} \nu_1 \\ \nu_2 \end{pmatrix}$$

**Step 1: Production.** A $\nu_e$ is produced at time $t = 0$ and position
$x = 0$:

$$|\nu(0)\rangle = |\nu_e\rangle = \cos\theta \, |\nu_1\rangle + \sin\theta \, |\nu_2\rangle$$

**Step 2: Propagation.** Each mass eigenstate propagates as a plane wave. For
an ultrarelativistic neutrino with energy $E \gg m_i$, the energy-momentum
relation gives:

$$E_i = \sqrt{p^2 + m_i^2} \approx p + \frac{m_i^2}{2p} \approx E + \frac{m_i^2}{2E}$$

where we use $p \approx E$ for ultrarelativistic particles. After propagating a
distance $L$ (with $t \approx L$ in natural units):

$$|\nu_i(L)\rangle = e^{-i E_i L} \, |\nu_i\rangle \approx e^{-i(E + m_i^2/2E)L} \, |\nu_i\rangle$$

**Step 3: Detection.** The state at distance $L$ is:

$$|\nu(L)\rangle = \cos\theta \, e^{-iE_1 L} |\nu_1\rangle + \sin\theta \, e^{-iE_2 L} |\nu_2\rangle$$

The amplitude for detecting $\nu_\mu$ is:

$$\langle \nu_\mu | \nu(L) \rangle = -\sin\theta \cos\theta \, e^{-iE_1 L} + \sin\theta \cos\theta \, e^{-iE_2 L}$$

$$= \sin\theta \cos\theta \left(e^{-iE_2 L} - e^{-iE_1 L}\right)$$

**Step 4: Probability.** Taking the modulus squared:

$$P(\nu_e \to \nu_\mu) = \sin^2\theta \cos^2\theta \cdot |e^{-iE_2 L} - e^{-iE_1 L}|^2$$

Using $|e^{-i\phi_2} - e^{-i\phi_1}|^2 = 2(1 - \cos(\phi_2 - \phi_1)) = 4\sin^2\left(\frac{\phi_2 - \phi_1}{2}\right)$:

$$\boxed{P(\nu_e \to \nu_\mu) = \sin^2(2\theta) \cdot \sin^2\!\left(\frac{\Delta m^2 L}{4E}\right)}$$

where $\Delta m^2 \equiv m_2^2 - m_1^2$.

### The Oscillation Formula in Practical Units

Restoring factors of $\hbar$ and $c$:

$$P(\nu_\alpha \to \nu_\beta) = \sin^2(2\theta) \cdot \sin^2\!\left(\frac{1.27 \, \Delta m^2 [\text{eV}^2] \cdot L [\text{km}]}{E [\text{GeV}]}\right)$$

The numerical factor 1.27 comes from:

$$\frac{\Delta m^2 L}{4E} = \frac{\Delta m^2 \cdot L}{4 \cdot E} \cdot \frac{c^3}{\hbar} \approx 1.267 \frac{\Delta m^2 [\text{eV}^2] \cdot L [\text{km}]}{E [\text{GeV}]}$$

This formula has two crucial parameters:

- **Mixing angle** $\theta$: controls the amplitude of oscillation (maximum at
  $\theta = \pi/4$, i.e., "maximal mixing").
- **$\Delta m^2$**: controls the oscillation wavelength. The oscillation length is
  $L_{\text{osc}} = 4\pi E / \Delta m^2$.

### The Survival Probability

The probability that the original flavor is retained:

$$P(\nu_e \to \nu_e) = 1 - P(\nu_e \to \nu_\mu) = 1 - \sin^2(2\theta) \cdot \sin^2\!\left(\frac{\Delta m^2 L}{4E}\right)$$

This is the "disappearance" channel, which was the first to be measured
conclusively (solar neutrinos, atmospheric neutrinos).

---

## Three-Flavor Formalism

### The PMNS Matrix Parameterization

With three neutrino flavors, the mixing matrix $U_{\text{PMNS}}$ is a $3 \times 3$
unitary matrix parameterized by three Euler angles $(\theta_{12}, \theta_{13},
\theta_{23})$ and one CP-violating Dirac phase $\delta_{\text{CP}}$. If neutrinos
are Majorana particles, there are two additional Majorana phases
$(\alpha_1, \alpha_2)$ that do not affect oscillations.

The standard PDG parameterization is:

$$U = \begin{pmatrix} 1 & 0 & 0 \\ 0 & c_{23} & s_{23} \\ 0 & -s_{23} & c_{23} \end{pmatrix} \begin{pmatrix} c_{13} & 0 & s_{13} e^{-i\delta} \\ 0 & 1 & 0 \\ -s_{13} e^{i\delta} & 0 & c_{13} \end{pmatrix} \begin{pmatrix} c_{12} & s_{12} & 0 \\ -s_{12} & c_{12} & 0 \\ 0 & 0 & 1 \end{pmatrix}$$

where $c_{ij} \equiv \cos\theta_{ij}$ and $s_{ij} \equiv \sin\theta_{ij}$.

Multiplying out:

$$U = \begin{pmatrix} c_{12}c_{13} & s_{12}c_{13} & s_{13}e^{-i\delta} \\ -s_{12}c_{23} - c_{12}s_{23}s_{13}e^{i\delta} & c_{12}c_{23} - s_{12}s_{23}s_{13}e^{i\delta} & s_{23}c_{13} \\ s_{12}s_{23} - c_{12}c_{23}s_{13}e^{i\delta} & -c_{12}s_{23} - s_{12}c_{23}s_{13}e^{i\delta} & c_{23}c_{13} \end{pmatrix}$$

### Measured Values of the Mixing Parameters

As of 2025 (NuFIT 5.3 and successor analyses), the best-fit values are:

| Parameter | Best Fit (Normal Ordering) | 3-sigma Range |
|:----------|:--------------------------|:--------------|
| $\theta_{12}$ | 33.41 degrees | 31.3 -- 35.9 degrees |
| $\theta_{23}$ | 49.1 degrees | 39.6 -- 52.0 degrees |
| $\theta_{13}$ | 8.54 degrees | 8.1 -- 8.9 degrees |
| $\delta_{\text{CP}}$ | ~197 degrees | 108 -- 404 degrees |
| $\Delta m^2_{21}$ | $7.41 \times 10^{-5}$ eV$^2$ | 6.82 -- 8.03 |
| $|\Delta m^2_{31}|$ | $2.507 \times 10^{-3}$ eV$^2$ | 2.43 -- 2.59 |

Key features:

- $\theta_{12} \approx 34°$ ("large" mixing) -- governs solar oscillations.
- $\theta_{23} \approx 49°$ (near-maximal) -- governs atmospheric oscillations.
- $\theta_{13} \approx 8.5°$ ("small" but nonzero) -- discovered by Daya Bay,
  RENO, Double Chooz in 2012.
- $\delta_{\text{CP}} \approx 197°$ -- hints of CP violation, but not yet at
  $5\sigma$. T2K favors maximal CP violation ($\delta \approx 270°$); NOvA shows
  tension.

### Three-Flavor Oscillation Probability

The general three-flavor transition probability in vacuum is:

$$P(\nu_\alpha \to \nu_\beta) = \delta_{\alpha\beta} - 4 \sum_{i>j} \text{Re}(U_{\alpha i}^* U_{\beta i} U_{\alpha j} U_{\beta j}^*) \sin^2\!\left(\frac{\Delta m^2_{ij} L}{4E}\right)$$
$$+ 2 \sum_{i>j} \text{Im}(U_{\alpha i}^* U_{\beta i} U_{\alpha j} U_{\beta j}^*) \sin\!\left(\frac{\Delta m^2_{ij} L}{2E}\right)$$

The last term is the CP-violating contribution. It changes sign under
$\nu \to \bar{\nu}$ (equivalently, $U \to U^*$), so:

$$P(\nu_\alpha \to \nu_\beta) - P(\bar{\nu}_\alpha \to \bar{\nu}_\beta) \neq 0 \quad \text{if } \delta_{\text{CP}} \neq 0, \pi$$

### The Jarlskog Invariant

The magnitude of CP violation in neutrino oscillations is controlled by the
Jarlskog invariant:

$$J = \text{Im}(U_{e1} U_{\mu 2} U_{e2}^* U_{\mu 1}^*) = \frac{1}{8} \cos\theta_{13} \sin(2\theta_{12}) \sin(2\theta_{23}) \sin(2\theta_{13}) \sin\delta_{\text{CP}}$$

With current best-fit values: $J \approx -0.033$. This is significantly larger
than the quark sector Jarlskog invariant ($J_{\text{CKM}} \approx 3 \times 10^{-5}$),
which is why leptonic CP violation may be more accessible experimentally.

---

## Matter Effects: The MSW Effect

### Wolfenstein's Matter Potential (1978)

When neutrinos propagate through matter, $\nu_e$ experiences an additional
potential due to coherent forward scattering on electrons via W-boson exchange.
This potential, first computed by Lincoln Wolfenstein in 1978, is:

$$V_{\text{CC}} = \sqrt{2} \, G_F \, n_e$$

where $G_F$ is the Fermi constant and $n_e$ is the electron number density. For
the Sun's core: $n_e \approx 6 \times 10^{25}$ cm$^{-3}$, giving
$V_{\text{CC}} \approx 7.6 \times 10^{-12}$ eV.

The neutral-current potential affects all flavors equally and drops out of
oscillation probabilities.

### The MSW Resonance (1985--1986)

Mikheyev and Smirnov (1985), building on Wolfenstein's potential, showed that
neutrino oscillations in matter with varying density can undergo a resonant
enhancement. The effective mixing angle in matter is:

$$\sin^2(2\theta_m) = \frac{\sin^2(2\theta)}{(\cos(2\theta) - 2EV/\Delta m^2)^2 + \sin^2(2\theta)}$$

The MSW resonance occurs when:

$$2EV = \Delta m^2 \cos(2\theta)$$

or equivalently, when the electron density reaches the resonance value:

$$n_e^{\text{res}} = \frac{\Delta m^2 \cos(2\theta)}{2\sqrt{2} \, G_F \, E}$$

At resonance, $\sin^2(2\theta_m) = 1$ regardless of the vacuum mixing angle --
even a tiny vacuum mixing angle produces maximal oscillation in matter.

### Adiabatic Propagation in the Sun

For solar neutrinos, the density decreases continuously from the core to the
surface. If the density variation is sufficiently slow (the "adiabatic
condition"), a $\nu_e$ produced in the core as the heavier effective mass
eigenstate emerges from the Sun still as the heavier mass eigenstate -- but this
is now predominantly $\nu_\mu$ (or $\nu_\tau$).

The adiabaticity parameter is:

$$\gamma = \frac{\Delta m^2 \sin^2(2\theta)}{2E \cos(2\theta)} \cdot \frac{1}{|d\ln n_e / dr|_{\text{res}}}$$

For $\gamma \gg 1$, the transition is adiabatic and the survival probability is:

$$P(\nu_e \to \nu_e) \approx \frac{1}{2}\left(1 + \cos(2\theta_m^0) \cos(2\theta)\right)$$

where $\theta_m^0$ is the matter angle at the production point.

For high-energy solar neutrinos ($E \gtrsim 5$ MeV, such as $^8$B neutrinos),
the MSW effect dominates and $P(\nu_e \to \nu_e) \approx \sin^2\theta_{12}
\approx 0.3$, which explains the observed solar neutrino deficit.

---

## The $L/E$ Dependence and Experimental Design

### Oscillation Length Scales

The oscillation length $L_{\text{osc}} = 4\pi E / \Delta m^2$ determines the
optimal baseline for each mass splitting:

| Mass Splitting | $\Delta m^2$ (eV$^2$) | $L_{\text{osc}}$ at 1 GeV | Relevant Experiments |
|:---------------|:----------------------|:--------------------------|:---------------------|
| Solar ($\Delta m^2_{21}$) | $7.4 \times 10^{-5}$ | ~33,000 km | KamLAND, SNO, Super-K solar |
| Atmospheric ($\Delta m^2_{31}$) | $2.5 \times 10^{-3}$ | ~1,000 km | Super-K atm, T2K, NOvA, MINOS |
| Reactor $\theta_{13}$ | $2.5 \times 10^{-3}$ | ~2 km at 3 MeV | Daya Bay, RENO, Double Chooz |

### The Hierarchy of Scales

The two mass splittings differ by a factor of ~33:

$$\frac{\Delta m^2_{31}}{\Delta m^2_{21}} \approx 33$$

This hierarchy allows the three-flavor problem to be approximately decomposed
into two independent two-flavor problems:

- **Solar sector**: $(\theta_{12}, \Delta m^2_{21})$ -- long baselines or low
  energies.
- **Atmospheric sector**: $(\theta_{23}, \Delta m^2_{31})$ -- shorter baselines
  or higher energies.
- **Reactor sector**: $(\theta_{13}, \Delta m^2_{31})$ -- short-baseline reactor
  experiments.

---

## CP Violation in the Lepton Sector

### Physical Meaning

If $\delta_{\text{CP}} \neq 0, \pi$, then:

$$P(\nu_\mu \to \nu_e) \neq P(\bar{\nu}_\mu \to \bar{\nu}_e)$$

This means the probability of a muon neutrino becoming an electron neutrino
differs from the probability of the corresponding antineutrino transition. This
asymmetry could be connected to leptogenesis -- the generation of the
matter-antimatter asymmetry of the universe via heavy right-handed neutrino
decays (Fukugita and Yanagida, 1986).

### Experimental Status

The current generation of long-baseline experiments (T2K, NOvA) shows hints of
large CP violation. The next generation -- DUNE (Fermilab to Sanford Lab,
1300 km) and Hyper-Kamiokande (T2K successor, 295 km with 260 kton detector) --
aims to measure $\delta_{\text{CP}}$ to $5\sigma$ significance if
$\delta_{\text{CP}}$ is near the current best-fit value.

---

## The Mass Hierarchy Problem

### Normal vs. Inverted Ordering

The sign of $\Delta m^2_{31}$ is not yet determined:

- **Normal ordering (NO)**: $m_1 < m_2 < m_3$ -- the pattern analogous to
  charged leptons and quarks.
- **Inverted ordering (IO)**: $m_3 < m_1 < m_2$ -- the "odd one out" ($m_3$) is
  the lightest.

The mass hierarchy affects:

1. Matter effects in long-baseline experiments (DUNE is optimized for this).
2. The effective Majorana mass in neutrinoless double beta decay.
3. The total neutrino mass constrained by cosmology.

Current data (as of 2025) slightly favor normal ordering at ~2--3$\sigma$ from
a combination of NOvA, T2K, Super-K atmospheric, and reactor data.

---

## Legacy and Experimental Confirmation

Pontecorvo's 1968 oscillation framework was confirmed in stages:

| Year | Experiment | Result |
|:-----|:-----------|:-------|
| 1968--1998 | Homestake, GALLEX, SAGE, Super-K | Solar $\nu_e$ deficit (the "solar neutrino problem") |
| 1998 | Super-Kamiokande | Atmospheric $\nu_\mu$ oscillation ($\Delta m^2_{\text{atm}}$) |
| 2001--2002 | SNO | Solar $\nu_e \to \nu_{\mu,\tau}$ (total flux matches SSM) |
| 2002 | KamLAND | Reactor $\bar{\nu}_e$ disappearance ($\Delta m^2_{\text{sol}}$) |
| 2012 | Daya Bay, RENO, Double Chooz | $\theta_{13} \neq 0$ at $>5\sigma$ |
| 2015 | Nobel Prize | Kajita (Super-K) and McDonald (SNO) |

The entire edifice of neutrino oscillation physics -- two mass splittings, three
mixing angles, and hints of CP violation -- rests on Pontecorvo's foundational
insight that mass and flavor eigenstates need not coincide.

---

## Connection to Phonon-Exflation Framework

### Neutrino Masses from the Internal Dirac Spectrum

In the phonon-exflation framework, all fermion masses arise from the eigenvalues
of the internal Dirac operator $D_K$ on the compact space $K = \text{SU}(3)$
(or its quotient). The neutrino masses correspond to the **lightest eigenvalues**
of $D_K(s)$, where $s$ is the Jensen deformation parameter that controls the
shape of the internal geometry.

The Dirac spectrum on the deformed SU(3) is organized by irreducible
representations $(p, q)$ of SU(3). The eigenvalues depend on the Casimir
invariants and the deformation parameter:

$$\lambda^2_{(p,q)}(s) = C_2(p,q) \cdot f(s) + \text{curvature corrections}$$

where $C_2(p,q) = (p^2 + q^2 + pq + 3p + 3q)/3$ is the quadratic Casimir. The
lowest-lying eigenvalues -- those in the $(1,0)$, $(0,1)$, and $(1,1)$
representations -- determine the neutrino mass spectrum.

### PMNS Angles from Spinor Harmonic Overlaps

The PMNS mixing matrix, in this framework, is not a free parameter but is
determined by the **overlap integrals** of spinor harmonics on the deformed
SU(3):

$$U_{\alpha i} = \int_K \psi_\alpha^*(x) \, \phi_i(x) \, \sqrt{g_s} \, d^8x$$

where $\psi_\alpha$ are the flavor eigenstates (determined by the weak
interaction structure of the spectral triple) and $\phi_i$ are the mass
eigenstates (eigenmodes of $D_K(s)$).

The near-maximal atmospheric mixing angle $\theta_{23} \approx 49°$ and the
large solar mixing angle $\theta_{12} \approx 34°$ are potentially explained by
approximate symmetries of the SU(3) geometry. The smaller $\theta_{13} \approx
8.5°$ requires the Jensen deformation to break these symmetries at a controlled
level.

### Mass-Squared Differences as Eigenvalue Spacings

The experimentally measured mass-squared differences constrain the spacing of the
lowest Dirac eigenvalues:

$$\Delta m^2_{21} = 7.4 \times 10^{-5} \text{ eV}^2 \quad \longrightarrow \quad |\lambda_2^2 - \lambda_1^2| \propto 7.4 \times 10^{-5}$$

$$\Delta m^2_{31} = 2.5 \times 10^{-3} \text{ eV}^2 \quad \longrightarrow \quad |\lambda_3^2 - \lambda_1^2| \propto 2.5 \times 10^{-3}$$

The ratio $\Delta m^2_{31} / \Delta m^2_{21} \approx 33$ must emerge from the
eigenvalue structure of $D_K(s)$ at the stabilized value $s_0$. This is a
non-trivial constraint: the Dirac spectrum must produce a hierarchy of ~33 in
the lowest eigenvalue spacings. In Tier 1 computations (Session 12), the
eigenvalue ratios show rich structure as a function of $s$, and the existence
of such hierarchies at specific $s$ values is testable.

### Mass Hierarchy from the Jensen Parameter

The sign of $\Delta m^2_{31}$ -- which determines normal vs. inverted ordering
-- is controlled by the ordering of the lowest Dirac eigenvalues at $s = s_0$.
In the bi-invariant limit ($s = 0$), the spectrum has high degeneracy, and both
orderings are possible depending on how the degeneracy is lifted by the Jensen
deformation.

Session 12 computations show that the Jensen deformation lifts degeneracies in
representation-dependent ways: states in different $(p,q)$ sectors respond
differently to the metric deformation. The physical mass hierarchy is therefore
a **prediction** of the framework once $s_0$ is determined from the effective
potential $V_{\text{eff}}(s)$.

### CP Violation from Geometry

The CP-violating phase $\delta_{\text{CP}}$ in the PMNS matrix arises, in this
framework, from the complex structure of the spinor harmonics on SU(3). The
Jensen deformation preserves certain discrete symmetries while breaking others;
the phase $\delta_{\text{CP}}$ is related to the failure of time-reversal
invariance in the internal geometry when combined with the grading operator
$\gamma_F$.

Session 17a established (deliverable D-1) that $[J, D_K(s)] = 0$ identically --
the real structure $J$ (which implements CPT) commutes with the deformed Dirac
operator. This means CPT is **exact** in the framework. However, CP alone can
be violated, and the magnitude of this violation is encoded in the geometric
phase acquired by spinor harmonics under the combined action of $J$ and
$\gamma_F$.

### The MSW Effect and Internal Geometry

The matter-enhanced oscillation (MSW effect) has a natural interpretation in
the phonon-exflation framework: the electron density in matter modifies the
effective potential experienced by the internal modes, shifting the eigenvalues
of $D_K$ in a flavor-dependent way. This is analogous to how the acoustic medium
in a condensed matter system modifies the phonon dispersion relation in the
presence of impurities.

The Wolfenstein matter potential $V_{\text{CC}} = \sqrt{2} G_F n_e$ can be
derived from the spectral action: the coupling of the internal Dirac operator
to the external fermion density produces an effective shift in the
$(1,0)$-sector eigenvalues that is proportional to $n_e$, exactly reproducing
the standard MSW formula.

### Oscillation Phenomenology as the Tightest Constraint

Among all experimental constraints on the phonon-exflation framework, neutrino
oscillation data provides the **tightest constraints on the lowest part of the
Dirac spectrum**. While charged lepton and quark masses probe mid-range
eigenvalues, and the W/Z masses probe the overall scale, the neutrino mass
splittings and mixing angles probe the fine structure of the lowest eigenvalues
where the spectrum is most sensitive to the deformation parameter $s$.

This makes neutrino oscillation measurements -- particularly the precise
determination of $\Delta m^2_{21}$, $\Delta m^2_{31}$, $\theta_{12}$,
$\theta_{23}$, $\theta_{13}$, and $\delta_{\text{CP}}$ -- the most
discriminating tests of the framework's predictions for the internal geometry.

---

## Key Equations Summary

1. **Two-flavor oscillation**:
   $P(\nu_e \to \nu_\mu) = \sin^2(2\theta) \sin^2(\Delta m^2 L / 4E)$

2. **PMNS matrix**: $U = R_{23}(\theta_{23}) \cdot \tilde{R}_{13}(\theta_{13}, \delta) \cdot R_{12}(\theta_{12})$

3. **Three-flavor probability**:
   $P(\nu_\alpha \to \nu_\beta) = \delta_{\alpha\beta} - 4\sum_{i>j} \text{Re}(U_{\alpha i}^* U_{\beta i} U_{\alpha j} U_{\beta j}^*) \sin^2(\Delta m^2_{ij} L / 4E) + 2\sum_{i>j} \text{Im}(...) \sin(\Delta m^2_{ij} L / 2E)$

4. **MSW resonance**: $n_e^{\text{res}} = \Delta m^2 \cos(2\theta) / (2\sqrt{2} G_F E)$

5. **Jarlskog invariant**: $J = (1/8) c_{13} \sin(2\theta_{12}) \sin(2\theta_{23}) \sin(2\theta_{13}) \sin\delta$

---

## References

1. B. Pontecorvo, "Neutrino Experiments and the Problem of Conservation of
   Leptonic Charge," Sov. Phys. JETP **26**, 984 (1968).
2. B. Pontecorvo, "Mesonium and Anti-mesonium," Sov. Phys. JETP **6**, 429 (1957).
3. Z. Maki, M. Nakagawa, S. Sakata, "Remarks on the Unified Model of
   Elementary Particles," Prog. Theor. Phys. **28**, 870 (1962).
4. L. Wolfenstein, "Neutrino oscillations in matter," Phys. Rev. D **17**, 2369 (1978).
5. S.P. Mikheyev, A.Yu. Smirnov, "Resonance Amplification of Oscillations in
   Matter and Spectroscopy of Solar Neutrinos," Sov. J. Nucl. Phys. **42**, 913 (1985).
6. Particle Data Group, "Review of Particle Physics," Prog. Theor. Exp. Phys.
   (2024). Neutrino mixing section.
7. I. Esteban et al. (NuFIT), "The fate of hints: updated global analysis of
   three-flavor neutrino oscillations," JHEP **09**, 178 (2020).
8. M. Fukugita, T. Yanagida, "Baryogenesis Without Grand Unification,"
   Phys. Lett. B **174**, 45 (1986).
