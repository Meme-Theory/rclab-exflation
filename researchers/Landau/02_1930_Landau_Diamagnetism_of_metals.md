# Diamagnetismus der Metalle (Diamagnetism of Metals)

**Author:** Lev Davidovich Landau
**Year:** 1930
**Journal:** Zeitschrift fur Physik, 64, 629-637

---

## 1. The Problem: Classical Theory Predicts Zero

### 1.1 The Bohr-van Leeuwen Theorem

One of the most striking results of classical statistical mechanics is the
Bohr-van Leeuwen theorem (1911/1919): a classical system of charged particles
in thermal equilibrium has ZERO magnetic susceptibility. The magnetization
vanishes identically, regardless of the applied field.

The proof is elegant. The classical partition function for a charged particle
in a magnetic field involves the canonical momentum p. The vector potential A
enters through the minimal coupling p -> p - eA/c. But the integral over all
momenta from -infinity to +infinity is invariant under this shift. Therefore
the partition function is independent of B, and the magnetization M = -dF/dB
is zero.

This theorem means that ALL magnetic phenomena -- diamagnetism, paramagnetism,
ferromagnetism -- are inherently quantum mechanical. There is no classical
explanation for magnetism.

### 1.2 The State of Affairs Before Landau

By 1930, Pauli had explained paramagnetism (1927) through the intrinsic spin of
the electron. But diamagnetism -- the weak repulsion of a material from a
magnetic field -- remained puzzling. The Larmor precession argument gave a
classical estimate for the diamagnetic susceptibility:

    chi_Larmor = -N * e^2 * <r^2> / (6 * m * c^2)

But this was an ad hoc semiclassical estimate, not derived from quantum
mechanics. And the Bohr-van Leeuwen theorem said the classical calculation
should give zero. Something was missing.

### 1.3 Landau's Insight

Landau realized that the resolution lies in the quantization of the electron's
orbital motion in the magnetic field. A free electron in a uniform magnetic field
B does not have a continuous spectrum of energies. Its transverse motion is
quantized into discrete levels -- what we now call LANDAU LEVELS.


## 2. Landau Quantization

### 2.1 The Hamiltonian

Consider an electron (charge -e, mass m) in a uniform magnetic field B = B * z_hat
along the z-axis. Using the Landau gauge A = (0, Bx, 0), the Hamiltonian is:

    H = (1/2m) * [p_x^2 + (p_y + eBx/c)^2 + p_z^2]

Since [H, p_y] = 0 and [H, p_z] = 0, both p_y and p_z are conserved. We can
replace them by their eigenvalues hbar*k_y and hbar*k_z.

### 2.2 Reduction to Harmonic Oscillator

Substituting p_y -> hbar*k_y, the Hamiltonian for the x-motion becomes:

    H_x = p_x^2/(2m) + (1/2) * m * omega_c^2 * (x - x_0)^2

where:
- omega_c = eB/(mc) is the CYCLOTRON FREQUENCY
- x_0 = -hbar*k_y*c/(eB) = -k_y * l_B^2 is the center of the orbit
- l_B = sqrt(hbar*c/(eB)) is the MAGNETIC LENGTH

This is a harmonic oscillator centered at x_0. The quantization is immediate.

### 2.3 The Energy Spectrum

The total energy eigenvalues are:

    E(n, k_z) = hbar * omega_c * (n + 1/2) + hbar^2 * k_z^2 / (2m)

where n = 0, 1, 2, ... is the Landau level index.

Key features:
- The transverse energy is QUANTIZED in units of hbar*omega_c
- The longitudinal motion (along B) remains free and continuous
- The zero-point energy hbar*omega_c/2 is present
- Each level has a MASSIVE degeneracy (see below)

### 2.4 Degeneracy of Landau Levels

The degeneracy of each Landau level is remarkable. The center x_0 of the
oscillator depends on k_y. For a system of area L_x * L_y, the allowed k_y
values span a range that maps x_0 across the sample. The number of states
per Landau level per unit area is:

    n_B = eB / (2*pi*hbar*c) = 1 / (2*pi*l_B^2)

This is the NUMBER OF FLUX QUANTA threading the sample:

    N_phi = B * A / phi_0

where phi_0 = hc/e = 4.14 * 10^{-7} G*cm^2 is the flux quantum (in Gaussian
units; phi_0 = h/e = 4.14 * 10^{-15} Wb in SI).

For B = 1 Tesla, n_B ~ 2.4 * 10^{10} cm^{-2} -- an enormous degeneracy. The
entire continuous 2D density of states is "collapsed" into discrete, highly
degenerate Landau levels.


## 3. The Diamagnetic Susceptibility

### 3.1 Free Energy Calculation

Landau computed the grand canonical free energy of a free electron gas in a
magnetic field. The density of states, normally smooth, becomes a series of
delta functions (or, at finite temperature, a series of peaks) at the Landau
level energies.

The free energy per unit volume is:

    Omega = -(k_B * T / V) * sum_{n,k_z,sigma} ln(1 + exp(beta*(mu - E_{n,k_z})))

where sigma labels spin and the sum over n runs over Landau levels.

### 3.2 The Euler-Maclaurin Expansion

For weak fields (hbar*omega_c << k_B*T and hbar*omega_c << E_F), Landau used the
Euler-Maclaurin formula to convert the sum over Landau levels back to an
integral plus correction terms:

    sum_{n=0}^{inf} f(n + 1/2) = integral_0^{inf} f(x) dx
                                  + (1/24) * f'(0)
                                  - (7/5760) * f'''(0) + ...

The zeroth-order term reproduces the field-free result (consistent with
Bohr-van Leeuwen: the classical limit gives zero magnetization). The FIRST
correction gives a field-dependent contribution to the free energy:

    Delta_Omega = -(e^2 * B^2) / (24 * pi^2 * m * c^2) * g(mu, T)

where g(mu, T) involves the density of states at the Fermi level.

### 3.3 Landau Diamagnetic Susceptibility

The magnetization M = -d(Omega)/dB and the susceptibility chi = dM/dB yield:

    chi_L = -(e^2) / (12 * pi^2 * m * c^2) * g(E_F)

At T = 0:

    chi_L = -mu_B^2 * g(E_F) / 3

where mu_B = e*hbar/(2mc) is the Bohr magneton and g(E_F) is the density of
states at the Fermi energy.

This is EXACTLY -1/3 of the Pauli paramagnetic susceptibility:

    chi_Pauli = mu_B^2 * g(E_F)

So:

    chi_L = -chi_Pauli / 3

The net susceptibility chi = chi_Pauli + chi_L = (2/3) * chi_Pauli is
paramagnetic (positive), but the diamagnetic contribution is significant and
non-zero -- resolving the Bohr-van Leeuwen paradox through quantum mechanics.


## 4. De Haas-van Alphen Oscillations

### 4.1 The Oscillatory Effect

At low temperatures and strong fields, the Euler-Maclaurin expansion breaks
down. As B increases, Landau levels sweep through the Fermi energy one by one.
Each time a Landau level crosses E_F, the thermodynamic quantities oscillate.

The magnetization oscillates with period:

    Delta(1/B) = 2*pi*e / (hbar*c*A_ext)

where A_ext is an extremal cross-sectional area of the Fermi surface
perpendicular to B. This is the de Haas-van Alphen (dHvA) effect, predicted
by Landau in 1930 and experimentally confirmed by de Haas and van Alphen in
the same year for bismuth.

### 4.2 Fermi Surface Mapping

The dHvA effect became one of the most powerful tools in solid-state physics.
By measuring the oscillation frequencies for different field orientations, one
can reconstruct the ENTIRE Fermi surface of a metal. This technique revealed
the complex, multiply-connected Fermi surfaces of real metals -- information
that no other measurement could provide.

### 4.3 The Lifshitz-Kosevich Formula

Lifshitz and Kosevich (1956) derived the full temperature and field dependence
of the dHvA oscillations:

    M_osc ~ sum_p (1/p^{3/2}) * R_T * R_D * R_s * sin(2*pi*p*F/B - pi/4 + phi)

where p is the harmonic index, F = hbar*A_ext/(2*pi*e) is the dHvA frequency,
and R_T, R_D, R_s are damping factors for temperature, scattering (Dingle), and
spin-splitting respectively.


## 5. Modern Consequences: The Quantum Hall Effect

### 5.1 Integer Quantum Hall Effect (IQHE)

Landau quantization is the foundation of the quantum Hall effect, discovered
by von Klitzing in 1980. In a 2D electron gas at low temperature and high
magnetic field, the Hall conductivity is quantized:

    sigma_xy = nu * e^2/h

where nu is an integer (the filling factor -- the number of filled Landau
levels). The quantization is exact to parts in 10^9, making it a metrological
standard for resistance.

### 5.2 Fractional Quantum Hall Effect (FQHE)

Tsui, Stormer, and Gossard (1982) discovered plateaus at fractional nu
(1/3, 2/5, 2/3, ...). Laughlin (1983) explained these through strongly
correlated electron states -- a new form of quantum matter with fractional
charge excitations and anyonic statistics. This required Landau levels as the
kinetic energy scaffold on which correlations build.

### 5.3 Topological Insulators

The quantum Hall effect was the first example of a topological phase of matter.
The integer nu is a topological invariant (the first Chern number of the Berry
connection over the magnetic Brillouin zone). This insight, developed by
Thouless, Kohmoto, Nightingale, and den Nijs (TKNN, 1982), launched the field
of topological condensed matter physics.

The classification of topological insulators and superconductors (the "periodic
table" of Kitaev, Ryu-Schnyder-Furusaki-Ludwig) directly connects to the
KO-dimension that appears in the phonon-exflation NCG framework.


## 6. Landau Levels in Relativistic Systems

### 6.1 Dirac Landau Levels

For relativistic fermions (graphene, Weyl semimetals), the Dirac equation in
a magnetic field gives energy levels:

    E_n = sign(n) * v_F * sqrt(2 * e * hbar * B * |n|)

Key differences from the non-relativistic case:
- Energy scales as sqrt(n*B), not linearly in n
- There is a ZERO-MODE at E_0 = 0 (n=0 level is special)
- The zero mode is responsible for the anomalous quantum Hall effect in graphene

### 6.2 Index Theorems

The zero mode of the Dirac operator in a magnetic field is related to the
Atiyah-Singer index theorem. The number of zero modes equals the number of
flux quanta:

    index(D) = n_+ - n_- = N_phi

This connects Landau quantization to deep mathematics: characteristic classes,
K-theory, and the spectral geometry that underlies the NCG approach to particle
physics.


## 7. Connection to Phonon-Exflation Cosmology

### 7.1 Kaluza-Klein Spectrum as Internal Landau Levels

The phonon-exflation framework posits that particles arise from the spectrum of
the Dirac operator D_K on the internal space SU(3). The Jensen deformation
parameter s plays a role analogous to the magnetic field B in Landau
quantization. Specifically:

- In Landau quantization, B breaks rotational symmetry in the transverse plane,
  producing discrete levels with spacing hbar*omega_c.
- In the KK framework, s breaks the bi-invariant symmetry of SU(3), producing
  a discrete spectrum with splittings that depend on s.

The analogy is structural:

    Landau level index n  <-->  KK quantum numbers (p, q)
    Cyclotron frequency omega_c  <-->  Eigenvalue spacing of D_K(s)
    Magnetic length l_B  <-->  Internal radius R(s)
    Degeneracy per level  <-->  Multiplicity of SU(3) irreps

### 7.2 Degeneracy Lifting and Particle Identification

Just as a magnetic field lifts the degeneracy of free-electron states into
discrete Landau levels, the Jensen deformation lifts the degeneracy of the
bi-invariant (s=0) Dirac spectrum. At s=0, eigenvalues cluster by the Casimir
value (lambda^2 = n/36 for integer n). At s != 0, each cluster splits into
distinct eigenvalues corresponding to different SU(3) irreps (p,q).

This splitting is the mechanism by which distinct particle species emerge: each
(p,q) sector at the deformed point s_0 corresponds to a particle with a
specific mass. The Tier 1 computation (Session 12) found that mass ratios at
s ~ 0.15 approach phi_paasch (= 1.53158, from x = e^{-x^2}) to 0.0005%.

### 7.3 Topological Protection

Landau levels carry topological protection: the quantum Hall conductance is
quantized because the Chern number is an integer. Similarly, the KO-dimension
of the spectral triple (KO = 6, computed in Session 8) is a topological
invariant that constrains the form of the Dirac operator. The topological
classification (class BDI, T^2=+1, identified in Session 17c) means the spectral
properties of D_K have the same protection as a topological superconductor
in internal space.

### 7.4 Oscillatory Phenomena

The dHvA oscillations arise because Landau levels sweep through the Fermi
energy as 1/B varies. An analogous effect could occur as s varies: as the
deformation parameter changes, eigenvalues of D_K(s) cross threshold values,
producing oscillatory behavior in the spectral action:

    S(s) = Tr(f(D_K(s)^2 / Lambda^2))

The spectral action computed in Session 14 shows structure as a function of s,
with features that may be interpretable as "spectral oscillations" analogous
to dHvA oscillations. This connection remains to be explored quantitatively.

### 7.5 The Magnetic Length Analogy

The magnetic length l_B = sqrt(hbar*c/(eB)) sets the scale of the wave functions
in each Landau level. In the KK framework, the Jensen metric g_s defines an
analogous length scale for each internal direction:

    l_{u(1)} ~ e^{-s},  l_{su(2)} ~ e^{s},  l_{C^2} ~ e^{-s/2}

(from the metric scale factors). These "internal lengths" determine the spatial
extent of the KK wave functions (Peter-Weyl modes on deformed SU(3)), just as
l_B determines the spatial extent of Landau level wave functions.

---

## References

1. L. D. Landau, "Diamagnetismus der Metalle," Z. Phys. 64, 629-637 (1930).
2. W. J. de Haas and P. M. van Alphen, "The dependence of the susceptibility
   of diamagnetic metals upon the field," Proc. Netherlands Roy. Acad. Sci.
   33, 1106 (1930).
3. I. M. Lifshitz and A. M. Kosevich, "Theory of the de Haas-van Alphen
   effect for particles with an arbitrary dispersion law," Dokl. Akad. Nauk
   SSSR 96, 963 (1954).
4. K. von Klitzing, G. Dorda, and M. Pepper, "New method for high-accuracy
   determination of the fine-structure constant based on quantized Hall
   resistance," Phys. Rev. Lett. 45, 494 (1980).
5. R. B. Laughlin, "Anomalous quantum Hall effect: An incompressible quantum
   fluid with fractionally charged excitations," Phys. Rev. Lett. 50, 1395
   (1983).
6. D. J. Thouless, M. Kohmoto, M. P. Nightingale, and M. den Nijs, "Quantized
   Hall conductance in a two-dimensional periodic potential," Phys. Rev. Lett.
   49, 405 (1982).
