# Pauli's Neutrino Hypothesis (1930)

## Bibliographic Information

- **Author**: Wolfgang Pauli
- **Date**: December 4, 1930 (letter); formal publication delayed until 1933 Solvay Conference
- **Form**: Open letter to the Tubingen conference on radioactivity
- **Salutation**: "Dear Radioactive Ladies and Gentlemen" (*Liebe Radioaktive Damen und Herren*)
- **Key Proposal**: A neutral, spin-1/2 particle of very small mass emitted alongside the electron in beta decay
- **Original Name**: "neutron" (renamed "neutrino" by Fermi in 1933-34)

---

## 1. Historical Context: The Beta Decay Energy Crisis

### 1.1 The Problem of the Continuous Spectrum

By 1914, James Chadwick had demonstrated that the energy spectrum of electrons emitted
in beta decay was continuous, not discrete. This was deeply troubling. In alpha decay and
gamma emission, particles emerged with sharply defined energies corresponding to the
difference between nuclear energy levels. If beta decay were a simple two-body process:

$$A(Z, N) \to A(Z+1, N-1) + e^-$$

then conservation of energy and momentum would require the electron to carry a fixed
kinetic energy:

$$T_e = \frac{(M_i - M_f)^2 - m_e^2}{2 M_i} \approx Q$$

where $Q = M_i - M_f - m_e$ is the Q-value of the decay (in natural units). The electron
energy should be a delta function at $T_e = Q$.

Instead, experiments showed a smooth distribution from zero up to some maximum energy
$E_{\max} \approx Q$, with most electrons carrying significantly less than the maximum.

### 1.2 The Missing Energy

Ellis and Wooster (1927) performed a calorimetric measurement of the total energy
released in the beta decay of RaE (bismuth-210). They measured the heat deposited by
a known quantity of decays and found that the average energy per decay was approximately
equal to the *mean* of the beta spectrum, not the endpoint. This ruled out the possibility
that the "missing" energy was being carried away by penetrating gamma rays -- the energy
was genuinely absent from the detected products.

The energy deficit per decay was:

$$\Delta E = Q - \langle T_e \rangle \approx Q - \frac{Q}{3} = \frac{2Q}{3}$$

For RaE, with $Q \approx 1.16$ MeV, roughly 0.7 MeV per decay was unaccounted for.

### 1.3 Bohr's Radical Proposal

Niels Bohr, confronted with this crisis, proposed that energy conservation might be
violated at the nuclear level -- that it held only statistically, not in individual
processes. This was not a casual suggestion; Bohr had previously speculated (1924,
in the Bohr-Kramers-Slater theory) that conservation laws might be approximate in
individual quantum events.

Bohr wrote in 1930:

> "At the present stage of atomic theory, however, we may say that we have no argument,
> either empirical or theoretical, for upholding the energy principle in the case of
> beta-ray disintegrations."

This willingness to abandon one of physics' most fundamental principles indicates
the severity of the crisis.

---

## 2. Pauli's "Desperate Remedy"

### 2.1 The Letter

On December 4, 1930, Pauli wrote his famous letter to a meeting of the regional society
for physics in Tubingen. He could not attend in person, claiming he needed to be at a
ball in Zurich. The letter opened:

> "Dear Radioactive Ladies and Gentlemen,
>
> As the bearer of these lines, to whom I graciously ask you to listen, will explain
> to you in more detail, because of the 'wrong' statistics of the N-14 and Li-6 nuclei
> and the continuous beta spectrum, I have hit upon a desperate remedy to save the
> 'exchange theorem' of statistics and the law of conservation of energy."

### 2.2 The Proposal

Pauli proposed the existence of a new electrically neutral particle with the following
properties:

1. **Spin 1/2** (to resolve both the beta spectrum problem and the nitrogen-14 spin
   statistics anomaly simultaneously)
2. **Mass comparable to or smaller than the electron mass** ("the mass of the neutrons
   should be of the same order of magnitude as the electron mass and in any event not
   larger than 0.01 proton masses")
3. **Electrically neutral** (hence the name "neutron")
4. **Emitted alongside the electron** in beta decay, carrying the balance of energy
   and momentum
5. **Penetrating power far exceeding gamma rays**, explaining why it had not been
   detected

The three-body decay scheme:

$$n \to p + e^- + \bar{\nu}_e$$

naturally produces a continuous electron spectrum because the available energy $Q$ is
shared among three bodies, with the kinematics allowing a continuous distribution.

### 2.3 Resolution of the Continuous Spectrum

With the neutrino included, the beta decay kinematics become:

$$T_e = Q - T_\nu - T_{\text{recoil}}$$

The electron energy spectrum (Fermi's later result) takes the form:

$$\frac{dN}{dT_e} = C \cdot F(Z, T_e) \cdot p_e \cdot E_e \cdot (Q - T_e)^2$$

where:
- $F(Z, T_e)$ is the Fermi function (Coulomb correction)
- $p_e = \sqrt{E_e^2 - m_e^2}$ is the electron momentum
- $E_e = T_e + m_e$ is the total electron energy
- $(Q - T_e)^2$ is the neutrino phase space factor (for $m_\nu = 0$)

The endpoint $T_e = Q$ is reached only when the neutrino carries zero kinetic energy --
a set of measure zero in phase space, explaining the suppression near the endpoint.

### 2.4 The Nitrogen-14 Puzzle

Pauli's letter also addressed a second anomaly: the spin of nitrogen-14. If the nucleus
contained 14 protons and 7 electrons (the prevailing model before Chadwick's 1932
neutron discovery), it would contain 21 fermions, giving half-integer total spin. But
band spectroscopy showed N-14 obeyed Bose-Einstein statistics (integer spin). Pauli's
neutral particle, if present in the nucleus, could resolve the counting.

This particular motivation became moot after Chadwick discovered the (actual) neutron
in 1932, which resolved the N-14 puzzle independently.

---

## 3. The Naming Question

### 3.1 From "Neutron" to "Neutrino"

Pauli initially called his hypothetical particle the "neutron." When Chadwick discovered
the massive neutral nucleon in 1932, the name "neutron" was reassigned to that particle.
Enrico Fermi, at the 1933 Solvay Conference and in his 1934 theory paper, coined
"neutrino" -- Italian for "little neutral one" -- to distinguish Pauli's light particle
from Chadwick's heavy one.

### 3.2 Pauli's Doubts

Pauli himself was deeply uneasy about his proposal. He reportedly said:

> "I have done a terrible thing. I have postulated a particle that cannot be detected."

He wagered a case of champagne that no one would ever observe it. (He lost this bet
in 1956 when Cowan and Reines detected it.)

---

## 4. Fermi's 1934 Theory: Making the Neutrino Concrete

### 4.1 The Four-Fermion Interaction

In 1933-1934, Enrico Fermi constructed the first quantitative theory of beta decay,
treating it as a point interaction between four fermion fields. Inspired by QED and
Pauli's neutrino hypothesis, Fermi wrote the interaction Hamiltonian as:

$$H_{\text{int}} = \frac{G_F}{\sqrt{2}} \int d^3x \, [\bar{\psi}_p \gamma^\mu \psi_n][\bar{\psi}_e \gamma_\mu \psi_\nu] + \text{h.c.}$$

where $G_F$ is Fermi's coupling constant (today measured as $G_F \approx 1.166 \times 10^{-5}$ GeV$^{-2}$).

### 4.2 The Beta Spectrum Derivation

From this interaction, Fermi derived the electron energy spectrum using golden-rule
perturbation theory:

$$\frac{d\Gamma}{dT_e} = \frac{G_F^2 |M_{fi}|^2}{2\pi^3} F(Z, E_e) \, p_e \, E_e \, p_\nu \, E_\nu$$

For massless neutrinos ($m_\nu = 0$):
- $E_\nu = Q - T_e$
- $p_\nu = E_\nu$

This gives the famous result:

$$\frac{d\Gamma}{dT_e} \propto F(Z, E_e) \, p_e \, E_e \, (Q - T_e)^2$$

The shape matched the observed continuous spectra beautifully.

### 4.3 The Kurie Plot

Kurie, Richardson, and Paxton (1936) introduced the linearization now called the
Kurie plot. Defining:

$$K(T_e) = \sqrt{\frac{d\Gamma/dT_e}{F(Z, E_e) \, p_e \, E_e}}$$

For $m_\nu = 0$, one obtains $K(T_e) = C(Q - T_e)$, a straight line intercepting the
$T_e$ axis at $Q$. For $m_\nu > 0$, the plot curves downward near the endpoint:

$$K(T_e) = C \sqrt{(Q - T_e)^2 - m_\nu^2}$$

This distortion near the endpoint remains the primary method for direct neutrino mass
measurement (KATRIN experiment: $m_\nu < 0.45$ eV at 90% CL as of 2024).

### 4.4 Cross-Section Estimate

Fermi's theory also allowed the first estimate of the neutrino interaction cross-section.
Bethe and Peierls (1934) calculated:

$$\sigma(\bar{\nu}_e + p \to n + e^+) \sim \frac{G_F^2 E_\nu^2}{\pi} \sim 10^{-44} \text{ cm}^2$$

for MeV-scale neutrinos. This is extraordinarily small -- a neutrino at these energies
could traverse a light-year of lead with only a 50% chance of interacting. Bethe and
Peierls concluded: "there is no practically possible way of observing the neutrino."

### 4.5 Fermi's Rejected Paper

Fermi first submitted his beta decay theory to *Nature* in 1933. The journal rejected
it as "too speculative" and "too remote from physical reality." He then published it
in *Zeitschrift fur Physik* (in German) and *Nuovo Cimento* (in Italian) in 1934.
It is now regarded as one of the most important papers in 20th century physics.

---

## 5. Mass Constraints from the Beta Spectrum Endpoint

### 5.1 The Endpoint Method

The shape of the beta spectrum near its endpoint is sensitive to the neutrino mass.
The differential rate near $T_e \to Q$ behaves as:

$$\frac{d\Gamma}{dT_e} \propto (Q - T_e) \sqrt{(Q - T_e)^2 - m_\nu^2} \quad \text{for } T_e \leq Q - m_\nu$$

and is zero for $T_e > Q - m_\nu$. This means:
- The true endpoint shifts from $Q$ to $Q - m_\nu$
- The spectrum vanishes with a vertical tangent rather than the quadratic vanishing of the $m_\nu = 0$ case

### 5.2 Historical Mass Bounds

| Year | Experiment | Isotope | Upper Bound on $m_\nu$ |
|:-----|:-----------|:--------|:----------------------|
| 1934 | Fermi estimate | Various | $\lesssim m_e$ (~511 keV) |
| 1948 | Curran et al. | $^3$H | < 10 keV |
| 1972 | Bergkvist | $^3$H | < 60 eV |
| 1991 | Los Alamos | $^3$H | < 9.3 eV |
| 2001 | Mainz/Troitsk | $^3$H | < 2.2 eV |
| 2022 | KATRIN | $^3$H | < 0.8 eV (90% CL) |
| 2024 | KATRIN (final) | $^3$H | < 0.45 eV (90% CL) |

Tritium ($^3$H) is preferred because its low Q-value (18.6 keV) maximizes the fraction
of decays near the endpoint where the mass effect is visible.

---

## 6. Legacy and Significance

Pauli's 1930 letter represents one of the most consequential acts of theoretical
physics in the 20th century:

1. **Saved energy conservation** -- a principle that has survived every subsequent test
2. **Predicted a new fundamental particle** 26 years before its detection
3. **Introduced the concept** of particles that interact only via the weak force
4. **Opened the door** to Fermi's theory of weak interactions
5. **Established** the methodology of "desperate remedies" -- postulating new physics
   when conservation laws appear violated

The neutrino has since become central to:
- The Standard Model (three generations of leptons)
- Solar and stellar astrophysics
- Supernova dynamics (SN 1987A)
- Neutrino oscillations and the discovery of neutrino mass
- Cosmological constraints (sum of neutrino masses < 0.12 eV from Planck)

---

## 7. Connection to Phonon-Exflation Framework

### 7.1 Neutrino Masses from Geometry

In the phonon-exflation framework, the internal Dirac operator $D_K$ on $M^4 \times SU(3)$
generates a discrete spectrum of eigenvalues $\lambda_n(s)$ that depend on the Jensen
deformation parameter $s$. The physical particle masses arise from these eigenvalues
through the spectral action principle:

$$S = \text{Tr}\, f(D^2/\Lambda^2)$$

The neutrino masses correspond to the *lightest* non-zero eigenvalues of $D_K$. In the
framework's Peter-Weyl decomposition, these fall in specific $(p,q)$ irreducible
representations of $SU(3)$, with masses determined by:

$$m_\nu^{(i)} \propto \lambda_i(s_0)$$

where $s_0$ is the value of the deformation parameter selected by the effective potential
$V_{\text{eff}}(s)$.

### 7.2 The Mass Hierarchy from Geometry

The normal vs. inverted mass hierarchy -- one of the central open questions in neutrino
physics -- is determined in this framework by the ordering of the lightest Dirac
eigenvalues at $s = s_0$. The Jensen deformation lifts degeneracies present at $s = 0$
(the bi-invariant, round metric), creating a hierarchical spectrum. Session 12
computations showed that 147 eigenvalue pairs fall within 1% of phi_paasch
($\phi_P = 1.53158$, from $x = e^{-x^2}$) at $s \approx 1.14$, suggesting deep
geometric structure in the mass ratios.

### 7.3 Relevance of Pauli's Insight

Pauli's hypothesis established that the neutrino exists and carries definite mass
(or at least, a mass consistent with zero to the precision of his era). The entire
program of neutrino mass measurement -- from Pauli's original bound of $\lesssim m_e$
to KATRIN's sub-eV constraint -- progressively tightens the target that any
fundamental theory must hit. The phonon-exflation framework claims to predict these
masses from the geometry of the internal space, with zero free parameters once $s_0$
is determined. The experimental constraints reviewed here define the empirical
envelope: $m_{\nu_e} < 0.45$ eV, $\sum m_\nu < 0.12$ eV (cosmological).

### 7.4 Fermi's Theory as Effective Low-Energy Limit

Fermi's four-fermion interaction emerges naturally in the spectral action framework.
The gauge bosons $W^\pm$ and $Z^0$ arise from the fluctuated Dirac operator
$D_A = D + A + JAJ^{-1}$, and integrating them out at energies $E \ll M_W$ reproduces
Fermi's contact interaction with:

$$G_F = \frac{g_2^2}{4\sqrt{2} M_W^2}$$

where $g_2(s)$ is the $SU(2)_L$ coupling at the deformation parameter $s$. Session 17a
derived $g_1/g_2 = e^{-2s}$, fixing the weak mixing angle at $s_0$.

---

## References

1. Pauli, W. (1930). Letter to the Physical Society of Tubingen, December 4, 1930.
   Reprinted in Brown, L.M. (1978). *Physics Today* 31(9), 23.
2. Ellis, C.D. and Wooster, W.A. (1927). "The average energy of disintegration of
   radium E." *Proc. Roy. Soc. A* 117, 109-123.
3. Chadwick, J. (1914). "Intensitatsverteilung im magnetischen Spektrum der
   beta-Strahlen von Radium B + C." *Verh. Dtsch. Phys. Ges.* 16, 383-391.
4. Fermi, E. (1934). "Versuch einer Theorie der beta-Strahlen. I." *Zeitschrift fur
   Physik* 88, 161-177.
5. Bethe, H. and Peierls, R. (1934). "The 'neutrino'." *Nature* 133, 532.
6. KATRIN Collaboration (2024). "Direct neutrino-mass measurement based on 259 days
   of KATRIN data." *Science* 386, eadq9592.
7. Bohr, N. (1930). "Atomic stability and conservation laws." *Faraday Lecture*,
   reprinted in *Collected Works*, Vol. 9.
