# Noncommutative Geometry, the Spectral Standpoint

**Author:** Alain Connes
**Year:** 2019
**Journal:** New Spaces in Mathematics (Cambridge University Press, 2021); also arXiv: 1910.10407
**Pages:** 44

---

## 1. The Spectral Paradigm

### 1.1 Geometry IS Spectrum

The central thesis of Connes' 40-year program, crystallized in this survey:
geometry is fundamentally SPECTRAL. The shape of a space is encoded not in
its points, coordinates, or charts, but in the spectrum of a suitable
operator -- the Dirac operator D.

The spectral data (A, H, D) -- an algebra A acting on a Hilbert space H with
a Dirac operator D -- determines a geometry. The precise content is given by
Connes' reconstruction theorem:

**Theorem (Connes, 2008/2013):** A commutative spectral triple (A, H, D) satisfying
the seven axioms of NCG reconstructs a unique compact spin Riemannian manifold
M such that A = C^inf(M), H = L^2(M, S) (spinor bundle), and D is the
Dirac operator of the Levi-Civita connection.

This is the noncommutative generalization of the Gelfand-Naimark theorem:
commutative spectral triples ARE spin manifolds, and noncommutative spectral
triples are the natural generalization.

### 1.2 Kac's Question

Mark Kac asked in 1966: "Can one hear the shape of a drum?" -- that is, does
the spectrum of the Laplacian determine the Riemannian metric?

The answer, in general, is NO: there exist isospectral but non-isometric
manifolds (Milnor 1964, Gordon-Webb-Wolpert 1992). But Connes shows that the
spectral triple (A, H, D) contains MORE information than just the spectrum
of D. It also contains:

- The algebra A (which functions act on the Hilbert space)
- The commutation relations [D, a] for a in A
- The real structure J and grading gamma

Together, this data DOES determine the geometry uniquely (the reconstruction
theorem). The answer to Kac's question in NCG is: "You can hear the shape of
a drum IF you also know the algebra of observations."

### 1.3 The Heat Kernel Bridge

The connection between spectral data and geometric invariants is mediated by
the heat kernel. For a Dirac operator D on a compact manifold M:

```
Tr(e^{-t D^2}) ~ sum_{k=0}^{inf} a_k(D^2) * t^{(k-n)/2}   as t -> 0+
```

The Seeley-DeWitt coefficients a_k(D^2) encode geometric invariants:

```
a_0 = (4*pi)^{-n/2} * rank(S) * Vol(M)
a_2 = (4*pi)^{-n/2} * (rank(S)/6) * integral_M R * dvol
a_4 = (4*pi)^{-n/2} * (1/360) * integral_M tr(5*R^2 - 2*Ric^2 + 2*Riem^2
      + 60*R*E + 180*E^2 + 30*|Omega|^2) * dvol
```

where rank(S) is the fiber dimension of the bundle (e.g. 2^{[n/2]} for spinors),
E is the endomorphism from D^2 = -(nabla^2 + E), and Omega is the curvature
of the connection on the bundle. For the standard Dirac operator, E = R/4 and
tr(Omega^2) involves |Riem|^2. The scalar Laplacian (E=0, Omega=0) gives only
the 5R^2 - 2Ric^2 + 2Riem^2 terms.

where R is the scalar curvature, Ric is the Ricci tensor, and Riem is the
Riemann tensor. The spectral action Tr(f(D^2/Lambda^2)) extracts precisely
these coefficients weighted by the moments of f.


---

## 2. Evolution of the Program: 1980-2019

### 2.1 Phase 1: Foundations (1980-1994)

- **1980**: C*-algebras and differential geometry (cyclic cohomology)
- **1985**: Full cyclic cohomology theory (IHES, 100+ pages)
- **1986**: Local index formula in NCG
- **1994**: Noncommutative Geometry (the 661-page treatise)

This phase established the mathematical infrastructure: cyclic cohomology as
the noncommutative analog of de Rham cohomology, the Chern character in
K-theory, the local index formula, and the Dixmier trace as the
noncommutative integral.

### 2.2 Phase 2: The Standard Model (1990-2007)

- **1990**: Connes-Lott model (first NCG derivation of SM)
- **1996**: Spectral action principle (Chamseddine-Connes)
- **2006**: Full SM with neutrino mixing (Chamseddine-Connes-Marcolli)
- **2007**: Classification theorem -- why A_F = C + H + M_3(C) (see Paper 12)

This phase demonstrated that the Standard Model of particle physics -- gauge
groups, fermion representations, Higgs mechanism, Yukawa couplings -- is
the UNIQUE almost-commutative geometry satisfying the NCG axioms with
KO-dimension 6.

### 2.3 Phase 3: Resilience and Beyond (2012-2019)

- **2012**: Sigma field and Higgs mass correction (see Paper 13)
- **2014**: Mimetic gravity from spectral action
- **2017**: Quanta of geometry (quantization of volume)
- **2019**: This survey -- the current state of the art

This phase addressed the 125 GeV Higgs challenge, extended the framework to
include gravitational degrees of freedom beyond Einstein, and opened
connections to quantum gravity through the quantization of volume.


---

## 3. Classification of Finite Geometries

### 3.1 Barrett's Classification (2007)

John Barrett systematically classified all finite spectral triples. For
KO-dimension 6, working with a Hilbert space H = C^{2n}:

```
The algebra A must be a subalgebra of M_n(C) + M_n(C)
```

subject to the axioms of reality (J), grading (gamma), and Poincare duality.

For n = 16 (the SM case with 32-dimensional H_F), the maximal algebra is:

```
A_max = M_2(H) + M_4(C)  (the Pati-Salam algebra)
```

and the SM algebra C + H + M_3(C) is obtained by imposing the first-order
condition in the product geometry M^4 x F.

### 3.2 van Suijlekom's Refinement

Walter van Suijlekom (2015) refined the classification by:

- Systematic enumeration of all Krajewski diagrams for given algebra and
  KO-dimension
- Identification of the "almost-commutative" geometries that give physical
  models
- Classification of all allowed inner fluctuations and their field content

### 3.3 The Landscape of NCG Models

Beyond the SM, the classification identifies:

```
a = 1: H + M_2(C) -- electroweak sector only (no quarks)
a = 2: M_2(H) + M_4(C) -- Pati-Salam (full SM after breaking)
a = 3: M_3(H) + M_6(C) -- extends to larger representations
a = 4: M_4(H) + M_8(C) -- includes potential GUT-scale physics
```

Each a-value gives a different model. The SM corresponds to a = 2 with
first-order breaking. Models with a >= 3 predict new particles not yet
observed.


---

## 4. Quantization of Volume

### 4.1 The Quanta of Geometry (2014-2017)

One of the most striking results discussed in the survey: in NCG, volume is
QUANTIZED. Connes, Chamseddine, and Mukhanov showed that for a 4-dimensional
spectral triple:

```
Vol(M) = sum_n <psi_n | Y | psi_n> = integer  (in appropriate units)
```

where Y = D/|D| is the sign of the Dirac operator, and the sum runs over
occupied states. The volume quantization arises from the integrality of the
index.

### 4.2 The Volume Formula

More precisely, the quantized volume is:

```
integral_M gamma_5 * e^a * e^b * e^c * e^d * epsilon_{abcd} = n * Vol_Planck
```

where e^a are the vierbein forms encoded in [D, x^mu], and n is an integer
determined by the topology (specifically, the index of the Dirac operator
coupled to an auxiliary field).

### 4.3 Connection to Volume-Preserving Deformations

The Jensen TT-deformation used in the phonon-exflation framework is
volume-preserving:

```
det(g_s) / det(g_0) = 1  for all s
```

This was verified computationally in Session 12 to machine precision. In
Connes' quantization framework, this means the Jensen deformation moves within
a fixed volume sector -- it changes the SHAPE of the internal space without
changing its volume quantum number. This is precisely the "spectral exflation"
mechanism proposed in Session G3: expansion comes from shape change, not
volume change.


---

## 5. The Thermodynamic Interpretation

### 5.1 Spectral Action as Partition Function

Connes discusses a deep connection between the spectral action and
thermodynamics. The spectral action:

```
Tr(f(D^2/Lambda^2)) = sum_n f(lambda_n^2 / Lambda^2)
```

where lambda_n are the eigenvalues of D, has the form of a PARTITION FUNCTION
in statistical mechanics:

```
Z(beta) = sum_n e^{-beta * E_n}
```

with the identification:
- Energy levels E_n <-> eigenvalues lambda_n^2
- Inverse temperature beta <-> 1/Lambda^2 (up to the cutoff function f)
- Free energy -log(Z)/beta <-> the spectral action

### 5.2 Entropy from the Spectrum

The spectral entropy:

```
S_spectral = -sum_n p_n * log(p_n)
```

where p_n = f(lambda_n^2/Lambda^2) / Z, measures the "information content"
of the geometry. Geometries with many eigenvalues near the cutoff have high
entropy; geometries with a gap have low entropy.

### 5.3 Temperature and the Cutoff

The cutoff scale Lambda plays the role of temperature. At "high temperature"
(large Lambda), many eigenvalues contribute and the spectral action is
dominated by the leading Seeley-DeWitt coefficients (cosmological constant,
Einstein-Hilbert term). At "low temperature" (small Lambda), only the lowest
eigenvalues contribute and the fine structure of the spectrum matters.

This interpretation connects to the renormalization group: flowing from high
Lambda to low Lambda corresponds to a "cooling" of the spectral geometry,
revealing finer and finer geometric structure.


---

## 6. Connections to Number Theory

### 6.1 The Riemann Zeta Function

Connes describes his long-standing program connecting NCG to the Riemann
hypothesis. The key construction is the "spectral realization" of the zeros
of the Riemann zeta function:

```
zeta(s) = sum_{n=1}^{inf} n^{-s} = product_p (1 - p^{-s})^{-1}
```

The nontrivial zeros of zeta lie on the critical line Re(s) = 1/2 (the
Riemann hypothesis). Connes constructs a spectral triple whose spectrum
encodes these zeros:

```
(A, H, D) where D * psi_rho = rho * psi_rho for each zero rho of zeta
```

### 6.2 Adeles and the Arithmetic Site

The "arithmetic site" is a noncommutative space whose algebra is:

```
A = C^*(Q^*/Z^*) (the group algebra of the idele class group)
```

This space encodes the prime numbers and their distribution. The Riemann
hypothesis is equivalent to a property of the spectrum of a specific
operator on this space.

### 6.3 Relevance to Physics

While the number theory connection may seem distant from particle physics,
Connes notes that the same mathematical structures -- spectral triples,
zeta functions, heat kernels -- appear in both contexts. The spectral action
on M^4 x F involves the zeta function of the Dirac operator:

```
zeta_D(s) = Tr(|D|^{-s})
```

and the noncommutative integral is defined through the residue of this zeta
function at s = n (the dimension). The tools developed for the Riemann
hypothesis feed directly into the physics applications.


---

## 7. Quantum Information and Entropy

### 7.1 von Neumann Entropy of Spectral Data

Connes discusses the von Neumann entropy of the density matrix associated
to a spectral triple:

```
rho = e^{-beta D^2} / Tr(e^{-beta D^2})
S(rho) = -Tr(rho * log(rho))
```

This entropy measures the "geometric complexity" of the spectral triple.
For almost-commutative geometries M^4 x F, the entropy decomposes:

```
S(rho) = S_continuous(M) + S_finite(F) + S_interaction
```

where S_continuous diverges (and requires regularization), S_finite is
determined by the finite spectral triple, and S_interaction encodes the
coupling between the continuous and finite parts.

### 7.2 Entanglement in NCG

The bimodule structure of H_F introduces a natural notion of entanglement.
The Hilbert space H_F decomposes as:

```
H_F = bigoplus_{i,j} (V_i tensor V_j^0)
```

where V_i are left modules and V_j^0 are right modules. The entanglement
between left and right sectors is measured by the entanglement entropy:

```
S_ent = -Tr_L(rho_L * log(rho_L))
```

where rho_L = Tr_R(|psi><psi|) is the reduced density matrix obtained by
tracing out the right (opposite algebra) sector.

### 7.3 Topological Entanglement and KO-Dimension

Connes suggests that the KO-dimension -- which determines the topological
class of the spectral triple -- is related to topological entanglement
entropy. The KO-dimension 6 of the SM spectral triple corresponds to the
topological class BDI in the Altland-Zirnbauer classification (T^2 = +1,
verified in Session 17c), which is a chiral symmetry class. This was
independently noted and computationally verified in the phonon-exflation
project.


---

## 8. Beyond Almost-Commutative: Towards Quantum Gravity

### 8.1 The Problem

Almost-commutative geometries M^4 x F (where M is a smooth manifold and F
is a finite spectral triple) describe CLASSICAL gravity coupled to the SM.
For QUANTUM gravity, one needs a framework where spacetime itself is
noncommutative -- not just the internal space.

### 8.2 Spectral Triples for Quantum Spacetimes

Connes discusses several approaches:

**Fuzzy spaces:** Replace M by a sequence of matrix approximations
M_N(C) that converge to C^inf(M) as N -> infinity. The "fuzzy sphere" is
the prototype:

```
A_N = M_N(C)  with  [X_i, X_j] = i * epsilon_{ijk} * X_k / sqrt(N)
```

The Dirac operator on the fuzzy sphere is well-defined and its spectrum
converges to the round sphere spectrum as N -> infinity.

**Random NCG:** Treat the Dirac operator D as a random matrix. The
"gravitational functional integral" becomes:

```
Z = integral dD * e^{-S(D)}
```

where S(D) = Tr(f(D^2/Lambda^2)) is the spectral action. This is a
well-defined matrix integral for finite spectral triples and can be studied
by random matrix theory techniques.

**Topos approach:** Use Connes' arithmetic site or related constructions to
define a "quantum arithmetic" spacetime where the prime numbers play the role
of quantum gravitational degrees of freedom.

### 8.3 The Spectral Action as Gravitational Action

The spectral action Tr(f(D^2/Lambda^2)) already contains gravitational
degrees of freedom. For the product geometry M^4 x F:

```
Tr(f(D^2/Lambda^2)) = integral_M d^4x sqrt(g) * L(g_mu_nu, A_mu, H, sigma)
```

where L contains the Einstein-Hilbert term, cosmological constant, Weyl
tensor squared, and all SM field Lagrangians. Gravity is NOT added by hand --
it EMERGES from the spectral geometry.


---

## 9. Status of Predictions (as of 2019)

### 9.1 Confirmed

- **Higgs exists and is elementary:** Predicted by NCG-SM; confirmed 2012.
- **Higgs mass in [120, 130] GeV:** Predicted after sigma correction (2012);
  confirmed at 125.09 GeV.
- **Gauge coupling unification (approximate):** The spectral action boundary
  conditions are CONSISTENT with approximate unification at Lambda ~ 10^{17} GeV,
  though not exact unification.
- **Neutrino masses nonzero:** Required by the Majorana sector of D_F; confirmed
  by oscillation experiments.

### 9.2 Untested

- **Sigma field existence:** A massive neutral scalar coupling to the Higgs
  via portal interaction. Could be dark matter.
- **Proton stability:** NCG does not predict proton decay (unlike SU(5) GUTs).
  Consistent with experimental null results.
- **Right-handed neutrinos:** Required by the spectral triple. At least one
  per generation, with Majorana mass near the seesaw scale.

### 9.3 Open Problems

- **Three generations:** Not derived from NCG axioms.
- **Mass hierarchy:** The Yukawa entries of D_F are free parameters.
- **Cosmological constant:** 120 orders of magnitude too large.
- **Strong CP problem:** Not addressed by NCG.
- **Dark energy:** Not explained.

### 9.4 The Decisive Tests

Connes identifies two classes of decisive tests:

1. **The sigma field:** If found at the LHC or future colliders, it would be
   strong evidence for NCG-SM. If excluded in the relevant mass range, the
   Resilience mechanism would need modification.

2. **The spectral action coefficients:** The ratios of Seeley-DeWitt
   coefficients a_0 : a_2 : a_4 are determined by the finite spectral triple.
   Measuring these ratios (through coupling constants, Newton's constant, and
   the cosmological constant) tests the NCG framework directly.


---

## 10. Connection to Phonon-Exflation

### 10.1 The Spectral Standpoint IS the Phonon Thesis

Connes' "spectral standpoint" -- that geometry is fundamentally encoded in the
spectrum of the Dirac operator -- is LITERALLY the phonon-exflation thesis.
The framework claims that:

```
Physical reality = spectral data of D_K on M^4 x SU(3)
```

All particle physics (masses, couplings, mixing angles) is determined by the
eigenvalues and eigenvectors of D_K on the Jensen-deformed SU(3). This is
Connes' program applied to a SPECIFIC internal geometry.

### 10.2 Thermodynamic Identification

The thermodynamic interpretation discussed by Connes (Section 5 above)
corresponds exactly to the phonon-exflation identification:

```
Spectral action = phonon free energy of the condensate
```

This was noted by Feynman in Session G3 as a "mathematical identity, not
analogy." The spectral action Tr(f(D^2/Lambda^2)) IS the free energy of a
bosonic system with energy levels lambda_n^2 at inverse temperature 1/Lambda^2.

The phonon-exflation framework makes this identification PHYSICAL: the
"condensate" is the M^4 x SU(3) background, the "phonons" are particles
(inner fluctuations of D), and the "temperature" is the energy scale Lambda.

### 10.3 The Dirac Spectrum Computations

The project's Tier 1 computations (Sessions 12-14) are direct implementations
of Connes' program:

- **Dirac spectrum on SU(3):** 672x672 matrices from Peter-Weyl decomposition
  with p+q <= 6. All 8 validation checks pass at machine epsilon.
- **Jensen deformation:** The metric g_s parameterized by s deforms D_K(s),
  changing the spectrum. The volume-preserving property connects to Connes'
  quantization of volume.
- **Spectral action:** Tr(f(D_s^2/Lambda^2)) computed as a function of s.
  The r = 0.96 correlation with Baptista V_eff validates the computational
  pipeline.
- **Phi emergence:** The ratio lambda_{(3,0)}/lambda_{(0,0)} = 1.531588 at
  s = 0.15 (0.0005% from phi_paasch = 1.53158) is a spectral invariant of
  the Jensen-deformed SU(3).

### 10.4 Quantization of Volume and Spectral Exflation

Connes' quantization of volume (Section 4) connects directly to the "spectral
exflation" mechanism proposed in Session G3. The key insight:

- The Jensen deformation is volume-preserving: det(g_s)/det(g_0) = 1
- Therefore, the volume quantum number is FIXED during the deformation
- All physical changes (particle masses, couplings, cosmological expansion)
  come from changes in SHAPE, not volume
- This is "spectral exflation": the universe expands because the internal
  space changes shape, not because it inflates

In Connes' language: the spectral action Tr(f(D_s^2/Lambda^2)) varies with s
because the SPECTRUM of D changes, even though the VOLUME is fixed. The
variation of the spectral action with s drives the dynamics.

### 10.5 Random NCG and the Path Integral

Connes' discussion of random NCG (Section 8.2) connects to the
phonon-exflation simulation. The GPE simulation evolves a "wavefunction"
psi(x, t) whose phononic excitations represent particles. In the NCG
language, this is a specific PATH in the space of spectral triples:

```
t |-> (A, H, D(t))   (a family of Dirac operators parameterized by time)
```

The "random NCG" approach would average over all such paths -- the
gravitational path integral. The phonon-exflation simulation computes one
specific path (the classical trajectory), while quantum gravity would require
the full integral.

### 10.6 The KO-Dimension Connection

Session 8 verified computationally that the KO-dimension of the internal
spectral triple is 6 -- the EXACT value required by the Chamseddine-Connes
classification theorem. In Connes' survey, this is emphasized as the key
constraint that determines the algebra A_F. The phonon-exflation verification
of KO-dimension 6 is therefore not just a consistency check -- it is the
FOUNDATION of the entire framework's claim to derive the Standard Model.

### 10.7 What Connes' Survey Implies for the Project

Reading the survey in the context of the phonon-exflation program:

1. **The program is on the right track:** The project's computational approach
   -- computing the Dirac spectrum, spectral action, and V_eff from the
   Jensen-deformed SU(3) -- is a direct implementation of Connes' vision.

2. **V_eff(s) is the decisive computation:** Connes' thermodynamic
   interpretation says that V_eff(s) = free energy of the geometry at
   deformation parameter s. Finding s_0 that minimizes V_eff determines ALL
   physical predictions. This was the UNANIMOUS conclusion of the Giants
   (Session G3).

3. **The sigma field is a mode of s:** The Resilience paper's sigma field
   should emerge as a specific excitation of the s parameter. Computing
   V_eff''(s_0) gives the sigma mass.

4. **Three generations may come from Z_3 x Z_3:** Connes notes that the
   number of generations is not derived from NCG axioms. But the Jensen
   deformation on SU(3) has a natural Z_3 triality (verified in Session 17a,
   deliverable B-4). If this Z_3 acts on the generation index, it could
   provide the missing derivation.

5. **The cosmological constant problem persists:** Connes' spectral action
   gives Lambda_cosmo ~ Lambda^4, which is 120 orders too large. The
   phonon-exflation framework does not resolve this unless the spectral action
   is computed at the CORRECT scale (not the Planck scale).


---

## 11. Open Problems for the Next Generation

Connes concludes the survey with a list of open problems. Several are
directly relevant to the phonon-exflation program:

### 11.1 Compute the FULL Dirac Spectrum

Not just the low-lying eigenvalues, but the full spectrum of D_K on a specific
internal geometry. The project's Tier 1 computation (p+q <= 6, 672x672
matrices) is a major step but still truncated. Convergence of Seeley-DeWitt
coefficients at p+q = 5-6 is in progress.

### 11.2 Derive the Number of Generations

Find a geometric or topological invariant that fixes N = 3. The Z_3 triality
of SU(3) (or Z_3 x Z_3 from the root lattice) is a candidate.

### 11.3 Solve the Cosmological Constant Problem

Within the spectral action framework, understand why Lambda_cosmo is so
much smaller than Lambda^4.

### 11.4 Quantum Gravity from Spectral Triples

Construct a well-defined "path integral over spectral triples" that includes
fluctuations of the metric, the Dirac operator, and the algebra simultaneously.

### 11.5 Connect to Observation

Derive NUMERICAL PREDICTIONS (mass ratios, mixing angles) from the spectral
data of a specific internal geometry. This is the explicit goal of the
phonon-exflation Tier 1-2 computation program.


---

## 12. Broader Perspective

### 12.1 NCG as a Language

Connes emphasizes that NCG is not a specific physical theory but a LANGUAGE
for expressing geometric ideas. Just as differential geometry provides the
language for general relativity, NCG provides the language for quantum
spacetime physics. The phonon-exflation framework is one specific THEORY
written in this language.

### 12.2 The Unreasonable Effectiveness

The fact that the NCG axioms -- motivated by pure mathematics (K-theory,
index theory, cyclic cohomology) -- produce EXACTLY the Standard Model
is what Connes calls an instance of the "unreasonable effectiveness of
mathematics." The axioms were not designed to give the SM. They were
designed to capture the minimal requirements for a geometry. That the SM
emerges is either a deep truth about nature or a remarkable coincidence.

### 12.3 The Next 40 Years

Connes' survey is implicitly a call to the next generation: the mathematical
framework is mature; the physics remains to be extracted. The decisive
computations -- V_eff, mass ratios, mixing angles, cosmological predictions --
require SPECIFIC internal geometries and NUMERICAL computation. This is
precisely the program that the phonon-exflation project is executing.


---

## References

1. Connes, A. (2019). "Noncommutative Geometry, the Spectral Standpoint."
   arXiv: 1910.10407. Published in New Spaces in Mathematics, Cambridge UP, 2021.
2. Connes, A. (2013). "On the spectral characterization of manifolds."
   J. Noncommut. Geom. 7, 1-82. arXiv: 0810.2088 (2008).
3. Connes, A. (1994). Noncommutative Geometry. Academic Press.
4. Chamseddine, A.H. and Connes, A. (1997). "The Spectral Action Principle."
   Commun. Math. Phys. 186, 731-750.
5. Chamseddine, A.H., Connes, A., and Mukhanov, V. (2015). "Quanta of Geometry:
   Noncommutative Aspects." Phys. Rev. Lett. 114, 091302.
6. Barrett, J.W. (2007). "A Lorentzian version of the non-commutative geometry
   of the Standard Model of particle physics." J. Math. Phys. 48, 012303.
7. van Suijlekom, W.D. (2015). Noncommutative Geometry and Particle Physics.
   Springer.
8. Kac, M. (1966). "Can one hear the shape of a drum?" Amer. Math. Monthly,
   73, 1-23.
9. Gordon, C., Webb, D., and Wolpert, S. (1992). "One cannot hear the shape of
   a drum." Bull. AMS 27, 134-138.
10. Coldea, R. et al. (2010). "Quantum Criticality in an Ising Chain: An
    Experimental Realization of E_8 Symmetry." Science 327, 177-180.
