# On the Theory of Superfluidity of Helium II (Second Paper)

**Author:** Lev Davidovich Landau
**Year:** 1947
**Journal:** J. Phys. USSR, 11, 91-92; also Zh. Eksp. Teor. Fiz., 17, 91 (1947)

---

## 1. Context: Why a Sequel?

Landau's 1941 paper established the two-fluid model and predicted the
phonon-roton excitation spectrum. By 1946-47, new experimental data demanded
quantitative refinement:

- Peshkov (1944, 1946) had confirmed second sound but the velocity disagreed
  with the 1941 roton parameters at intermediate temperatures
- Andronikashvili (1946) measured the normal fluid fraction rho_n/rho via
  torsional oscillator experiments, providing direct thermodynamic data
- The 1941 roton parameters (Delta/k_B ~ 9.6 K, p_0/hbar ~ 2 A^{-1}) needed
  recalibration against the new measurements

The 1947 paper, though short (essentially a letter), contains the revised
excitation spectrum parameters that became the standard reference for three
decades, until neutron scattering provided direct measurements.

---

## 2. The Revised Excitation Spectrum

### 2.1 Phonon Branch (Unchanged)

The low-momentum excitations remain acoustic phonons:

    epsilon(p) = c * p    for p -> 0

with c = 238 m/s (first sound velocity). This branch is model-independent --
it IS the sound mode of the liquid.

### 2.2 Roton Parameters (Revised)

Landau revised the roton minimum parametrization:

    epsilon(p) = Delta + (p - p_0)^2 / (2 * mu*)

The 1947 parameters, obtained by fitting thermodynamic data:

| Parameter | 1941 Value | 1947 Value | Modern (neutron) |
|:----------|:-----------|:-----------|:-----------------|
| Delta/k_B | 9.6 K | 8.6 K | 8.64 K |
| p_0/hbar | 2.0 A^{-1} | 1.92 A^{-1} | 1.92 A^{-1} |
| mu* | ~ 0.77 m_He | 0.16 m_He | 0.16 m_He |

The revised roton gap Delta/k_B = 8.6 K is 10% lower than the 1941 estimate,
and the effective mass mu* dropped dramatically from ~0.77 to 0.16 helium
masses. These revised values agree with modern neutron scattering measurements
to within experimental uncertainty -- a remarkable achievement given that Landau
extracted them purely from thermodynamic fits without any microscopic theory.

### 2.3 The Maxon Region

Between the phonon branch and the roton minimum lies the "maxon" peak (a term
coined later). Modern neutron data give the maxon at p/hbar ~ 1.1 A^{-1} with
epsilon/k_B ~ 13.9 K. The maxon is less important thermodynamically than the
roton minimum because the density of states is lower at the maximum.

The complete spectrum epsilon(p) between phonon and roton regions has no simple
analytic form. Landau suggested a smooth interpolation. Modern treatments use
the experimentally measured S(k) (dynamic structure factor) directly.

---

## 3. Temperature Dependence of the Superfluid Density

### 3.1 Phonon Contribution

The normal fluid density splits into phonon and roton parts:

    rho_n(T) = rho_n^{ph}(T) + rho_n^{rot}(T)

The phonon gas contributes:

    rho_n^{ph}(T) = (2 * pi^2 / 45) * (k_B * T)^4 / (hbar^3 * c^5)

This Debye T^4 law dominates at very low temperatures (T < 0.6 K). At T = 1.0 K,
rho_n^{ph}/rho ~ 7.7 x 10^{-5} (tiny).

### 3.2 Roton Contribution

The roton gas contributes:

    rho_n^{rot}(T) = (2 * p_0^4) / (3 * (2*pi)^{3/2} * hbar^3 * mu*^{1/2}) *
                      (k_B * T)^{-1/2} * exp(-Delta / (k_B * T))

The exponential activation factor exp(-Delta/(k_B*T)) makes rotons negligible
below ~0.6 K but dominant above ~1 K:

- T = 1.5 K: rho_n^{rot}/rho ~ 0.05 (rotons carry 5% of the mass)
- T = 2.0 K: rho_n^{rot}/rho ~ 0.4 (rotons carry 40%)

### 3.3 Crossover and Superfluid Density

The phonon-roton crossover temperature T_cross ~ 0.6 K, where the two
contributions are equal. The superfluid fraction:

    rho_s(T) / rho = 1 - rho_n(T) / rho

At T = 0: rho_s/rho = 1 (fully superfluid).
At T = T_lambda: rho_s/rho -> 0 (lambda transition).

The Landau theory gives an excellent description for T < 1.8 K. Near T_lambda,
the quasi-particle picture breaks down and critical phenomena (power-law
behavior with exponent nu ~ 0.67) take over.

---

## 4. Comparison with Andronikashvili's Data

Andronikashvili's torsional oscillator experiment (1946) uses a stack of
closely spaced discs suspended in He II. The normal fluid (viscous) is dragged
by the discs; the superfluid (inviscid) does not rotate. The oscillation period
directly measures rho_n(T).

Landau's 1947 roton parameters give quantitative agreement:

| T (K) | rho_n/rho (expt) | rho_n/rho (Landau 1947) | Deviation |
|:-------|:-----------------|:-----------------------|:----------|
| 0.8 | 0.001 | 0.001 | < 10% |
| 1.0 | 0.006 | 0.006 | ~ 5% |
| 1.2 | 0.024 | 0.025 | ~ 4% |
| 1.4 | 0.074 | 0.078 | ~ 5% |
| 1.6 | 0.17 | 0.18 | ~ 6% |
| 1.8 | 0.35 | 0.39 | ~ 10% |
| 2.0 | 0.60 | 0.70 | ~ 17% |

Agreement is excellent below 1.6 K and degrades near T_lambda as expected.

---

## 5. Viscosity of the Normal Component

At low temperatures where phonons dominate, the phonon mean free path l_ph
grows as T^{-5}, so the viscosity eta_ph ~ T^{-5} -- paradoxically, He II
becomes MORE viscous (in its normal component) at lower temperatures.

Above T_cross ~ 0.6 K, roton-roton scattering dominates:

    eta_rot ~ p_0 / (3 * sigma_rot) = approximately constant

The two-component viscosity produces distinctive behavior:
- T < 0.6 K: eta is very large (ballistic normal fluid)
- T ~ 1-2 K: eta ~ 10^{-5} Pa*s (roton-dominated, gas-like)
- Near T_lambda: critical divergence (not captured by Landau theory)

---

## 6. Second Sound and Specific Heat (Revised)

### 6.1 Second Sound Velocity

With the revised roton parameters, the second sound velocity:

    u_2^2 = (rho_s / rho_n) * (s^2 * T / c_p)

At low T (phonon regime): u_2 -> c / sqrt(3) ~ 137 m/s (phonon gas result).
At intermediate T (roton regime): u_2 ~ 20-30 m/s (decreasing with T).
At T -> T_lambda: u_2 -> 0 (because rho_s -> 0).

Peshkov's measurements confirmed agreement to within a few percent for T < 1.8 K.

### 6.2 Specific Heat

Phonon contribution: C_ph ~ T^3 (Debye law).
Roton contribution: C_rot ~ (Delta/(k_B*T))^2 * exp(-Delta/(k_B*T)).

The lambda anomaly at T_lambda (C ~ |T - T_lambda|^{-alpha}, alpha ~ -0.013)
is a critical phenomenon not captured by the quasi-particle model, requiring
renormalization group theory (Wilson, Fisher).

---

## 7. Comparison with Later Microscopic Theory

### 7.1 Feynman's Approach (1954-56)

Feynman showed the excitation energy can be expressed as:

    epsilon(k) = hbar^2 * k^2 / (2 * m * S(k))

where S(k) is the liquid structure factor. Since S(k) has a peak at
k ~ 2*pi/d (d = interparticle spacing), epsilon(k) has a minimum -- the roton.
This gives Delta/k_B ~ 14 K (too high by 60%). With backflow corrections
(Feynman-Cohen 1956): Delta/k_B ~ 11 K (still 25% too high).

### 7.2 Neutron Scattering Confirmation (1961)

Henshaw and Woods measured epsilon(p) directly via inelastic neutron scattering:

    Delta/k_B = 8.64 +/- 0.04 K    (Landau: 8.6 K)
    p_0/hbar = 1.92 +/- 0.01 A^{-1} (Landau: 1.92 A^{-1})
    mu* = 0.16 +/- 0.01 m_He        (Landau: 0.16 m_He)

Agreement to three significant figures from thermodynamic fitting alone --
one of the great achievements of theoretical physics.

---

## 8. Connection to Phonon-Exflation Cosmology

### 8.1 The Roton Minimum as Massive Particle Mode

The refined roton spectrum:

    epsilon_roton(p) = Delta + (p - p_0)^2 / (2 * mu*)

Compare with the relativistic dispersion of a massive particle:

    E(p) = sqrt(m^2*c^4 + p^2*c^2) ~ m*c^2 + p^2/(2*m) for p << m*c

The correspondence:
- Delta <-> m*c^2 (rest mass energy = excitation gap)
- p_0 <-> internal quantum number (KK momentum)
- mu* <-> effective mass (renormalized by medium interactions)

The roton minimum occurs at FINITE p_0, not at p = 0. In the KK picture, this
maps to massive particles carrying nonzero internal quantum numbers -- which is
precisely the case for all SM fermions (hypercharge, isospin, color).

### 8.2 Condensate Fraction and Cosmological Evolution

The formula rho_s(T)/rho = 1 - rho_n(T)/rho has a direct cosmological analog:

    Psi_cond(T) / Psi_total = 1 - n_particles(T) / n_total

During exflation, the expansion parameter s evolves, changing the condensate-
to-particle ratio. This is the mechanism by which matter is created:

- Early (high T / small s): rho_s ~ rho, few excitations, almost all condensate
- Intermediate: excitations proliferate (particle creation epoch)
- Late (low T / large s): freeze-out, final particle abundances set

### 8.3 The Exponential Activation Factor

The roton contribution rho_n^{rot} ~ exp(-Delta/(k_B*T)) is a Boltzmann
suppression for massive excitations. In phonon-exflation, this maps to:

    n_particle ~ exp(-m*c^2 / (k_B * T_eff))

This is exactly the freeze-out mechanism used in the GPE simulation's D/H
ratio calculation, where the deuterium-to-hydrogen ratio is determined by the
Boltzmann factor at the freeze-out temperature.

### 8.4 Phonon-Roton Crossover and the QCD Transition

The crossover at T_cross ~ 0.6 K between phonon-dominated and roton-dominated
normal fluid has a structural parallel with the QCD crossover:
- Below T_QCD ~ 170 MeV: hadrons (massive, like rotons) dominate
- Above T_QCD: gluons and quarks (massless/light, like phonons) dominate

The phonon-exflation framework suggests both represent the crossover between
gapped and gapless excitation branches of the same underlying condensate.

### 8.5 The GPE Simulation Bridge

The GPE solver implements the Bogoliubov spectrum refining Landau's curve:

    epsilon_Bog(k) = sqrt[(hbar*k)^2/(2*m) * ((hbar*k)^2/(2*m) + 2*g*n_0)]

At low k: epsilon ~ c*k (phonon, c = sqrt(g*n_0/m)).
At high k: epsilon ~ hbar^2*k^2/(2*m) + g*n_0 (free particle + mean field).

The healing length xi = hbar/sqrt(2*m*g*n_0) sets the crossover scale, playing
the role of the compactification length l_K.

---

## 9. Summary

Landau's 1947 sequel, though only two pages, established:

1. Revised roton parameters: Delta/k_B = 8.6 K, p_0/hbar = 1.92 A^{-1},
   mu* = 0.16 m_He -- confirmed to 3 significant figures by neutron scattering
   14 years later
2. Quantitative rho_n(T) from phonon + roton contributions
3. Agreement with Andronikashvili's torsional oscillator data to ~5% for T < 1.6 K
4. Revised second sound velocity u_2(T) matching Peshkov's measurements
5. The phonon-roton crossover temperature T_cross ~ 0.6 K

The extraordinary accuracy of Landau's thermodynamic extraction of microscopic
parameters -- without any microscopic theory or direct spectroscopic
measurement -- remains one of the most impressive feats of theoretical physics
in the 20th century.

---

## References

- L.D. Landau, "On the Theory of Superfluidity of Helium II," J. Phys. USSR 11, 91 (1947)
- L.D. Landau, "The Theory of Superfluidity of Helium II," J. Phys. USSR 5, 71 (1941)
- E.L. Andronikashvili, "A Direct Observation of Two Kinds of Motion in Helium II," J. Phys. USSR 10, 201 (1946)
- V. Peshkov, "Determination of the Velocity of Propagation of the Second Sound in Helium II," J. Phys. USSR 10, 389 (1946)
- R.P. Feynman, "Atomic Theory of the Two-Fluid Model of Liquid Helium," Phys. Rev. 94, 262 (1954)
- R.P. Feynman, M. Cohen, "Energy Spectrum of the Excitations in Liquid Helium," Phys. Rev. 102, 1189 (1956)
- D.G. Henshaw, A.D.B. Woods, "Modes of Atomic Motions in Liquid Helium by Inelastic Scattering of Neutrons," Phys. Rev. 121, 1266 (1961)
