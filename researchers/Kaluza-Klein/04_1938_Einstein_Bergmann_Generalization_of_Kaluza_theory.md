# On a Generalization of Kaluza's Theory of Electricity

**Author(s):** Albert Einstein and Peter Bergmann
**Year:** 1938
**Journal:** Annals of Mathematics, Second Series, 39(3), 683-701

---

## Abstract

A new discussion is given of an approach toward a unified theory of the
gravitational and electromagnetic fields, based on an extension of Riemannian
geometry to five dimensions. The theory is developed from three axioms.
The first postulates a five-dimensional Riemannian space. The second requires
that the space be closed (periodic) with respect to the fifth dimension. The
third imposes a variational principle. The resulting field equations reproduce
Einstein's gravitational equations and Maxwell's electromagnetic equations in
four dimensions, together with equations for a scalar field.

---

## Historical Context

By the late 1930s, the Kaluza-Klein idea had been dormant for roughly a decade.
Kaluza's original 1921 paper had shown that five-dimensional general relativity
contains both four-dimensional gravity and electromagnetism, but his treatment
relied on the "cylinder condition" -- the ad hoc assumption that no physical
quantity depends on the fifth coordinate. Klein (1926) gave this a quantum
mechanical interpretation by compactifying the fifth dimension into a tiny circle,
relating the radius to Planck's constant and the electron charge.

Einstein himself had explored five-dimensional approaches in 1923 and 1927, before
abandoning them in favor of distant parallelism (teleparallelism). He also pursued
a different version with Walther Mayer in 1931-1932, using a fiber bundle formalism
that avoided introducing a literal fifth dimension.

The 1938 paper with Bergmann represents Einstein's RETURN to the five-dimensional
approach, now with a more modern and rigorous formulation. Peter Bergmann was
Einstein's assistant at the Institute for Advanced Study in Princeton, and would
later become one of the founders of canonical quantum gravity.

The paper is historically significant as the first to take the five-dimensional
spacetime seriously as a PHYSICAL entity, rather than merely a mathematical device
for combining the metric and electromagnetic potential. Einstein and Bergmann
insisted on complete five-dimensional symmetry -- all five coordinates are treated
on an equal footing, with the periodicity of the fifth dimension being a geometric
property (topology), not an arbitrary restriction on the fields.

A largely unknown manuscript exists (the "Washington Manuscript") in which Einstein
developed the same theory from scratch on a more axiomatic basis. Witten (2014,
arXiv:1401.8048) later wrote a commentary noting that Einstein and Bergmann's
framework is equivalent to the modern Kaluza-Klein viewpoint, but that Einstein
"drew back" from the full theory because it predicted a massless scalar field
(the dilaton) for which there was no experimental evidence.

---

## Key Arguments and Derivations

### 1. The Three Axioms

Einstein and Bergmann build their theory on three fundamental postulates:

**Axiom I (Five-dimensional Riemannian geometry):**
The physical world is described by a five-dimensional Riemannian manifold M^5
equipped with a metric tensor gamma_{AB} (A, B = 0, 1, 2, 3, 5), where x^5 is the
fifth coordinate. The metric has signature (-, +, +, +, +).

**Axiom II (Periodicity / Compactness):**
The five-dimensional space is closed with respect to the fifth dimension. That is,
the manifold M^5 has the topology M^4 x S^1, where S^1 is a circle of some
period L:

  gamma_{AB}(x^mu, x^5) = gamma_{AB}(x^mu, x^5 + L)

All fields are periodic in x^5. This replaces Kaluza's cylinder condition (which
required complete independence of x^5) with the weaker condition of periodicity.

**Axiom III (Variational principle):**
The field equations are derived from the five-dimensional Einstein-Hilbert action:

  S = integral d^5x sqrt(-gamma) R^{(5)}

where R^{(5)} is the five-dimensional Ricci scalar. The variation is taken with
respect to the full five-dimensional metric gamma_{AB}.

### 2. Decomposition of the Five-Dimensional Metric

The five-dimensional metric gamma_{AB} is parameterized in terms of four-dimensional
fields. In modern notation (which differs slightly from Einstein-Bergmann's original),
the Kaluza-Klein ansatz for the metric is:

  ds^2_5 = gamma_{AB} dx^A dx^B

        = g_{mu nu} dx^mu dx^nu + phi^2 (dx^5 + A_mu dx^mu)^2

where:
- g_{mu nu}(x, x^5) is the four-dimensional metric (10 components)
- A_mu(x, x^5) is a vector field (4 components)
- phi(x, x^5) is a scalar field (1 component)

This accounts for all 15 independent components of the symmetric 5x5 tensor
gamma_{AB}.

When the fields are expanded in Fourier modes on S^1:

  g_{mu nu}(x, x^5) = sum_n g_{mu nu}^{(n)}(x) exp(2 pi i n x^5 / L)

and similarly for A_mu and phi, the n = 0 modes give:

- g_{mu nu}^{(0)}: the four-dimensional gravitational field
- A_mu^{(0)}: the electromagnetic potential
- phi^{(0)}: a scalar field (later called the "dilaton" or "radion")

The higher Fourier modes (n != 0) represent massive Kaluza-Klein excitations with
masses m_n = |n| / R, where R = L / (2 pi) is the radius of the circle.

### 3. Field Equations

From the variational principle (Axiom III), the five-dimensional Einstein equations
are:

  R_{AB}^{(5)} - (1/2) gamma_{AB} R^{(5)} = 0

(vacuum equations -- no matter source in five dimensions).

Upon dimensional reduction (keeping only the n = 0 modes), these decompose into:

**Gravitational equations** (from R_{mu nu} components):

  G_{mu nu}^{(4)} = (8 pi G / c^4) T_{mu nu}^{EM} + T_{mu nu}^{scalar}

where T_{mu nu}^{EM} is the electromagnetic stress-energy tensor and T_{mu nu}^{scalar}
involves the scalar field phi.

**Maxwell equations** (from R_{mu 5} components):

  nabla_nu (phi^3 F^{mu nu}) = 0

where F_{mu nu} = partial_mu A_nu - partial_nu A_mu. The factor phi^3 couples the
electromagnetic field to the scalar.

**Scalar field equation** (from R_{55} component):

  Box phi = (phi / 4) F_{mu nu} F^{mu nu}

The scalar field is sourced by the electromagnetic field strength squared.

### 4. The Scalar Field Problem

The scalar field phi (the 15th component of the 5D metric) was the central difficulty
that Einstein and Bergmann confronted. In their analysis:

(a) If phi = constant (frozen scalar), the theory reduces exactly to Einstein-Maxwell
    theory in four dimensions. This is the Kaluza result.

(b) If phi is allowed to vary, it introduces a NEW long-range force (a massless
    scalar field coupled to electromagnetism). In 1938, there was no experimental
    evidence for such a field.

Einstein and Bergmann chose to SET phi = constant by hand, thereby BREAKING the
five-dimensional symmetry. As Witten (2014) noted, this was a step backward --
they "drew back, modifying the theory in a way that spoiled the five-dimensional
symmetry." The more symmetric version of the theory (with dynamical phi) is actually
the correct modern Kaluza-Klein theory.

The scalar phi is now understood as the "dilaton" or "radion" -- it controls the
radius of the compact dimension. Jordan (1947) and Brans-Dicke (1961) later
rehabilitated the scalar field in their scalar-tensor theories of gravity.

### 5. Charge Quantization

Einstein and Bergmann noted (following Klein) that electric charge is quantized in
the five-dimensional theory because it corresponds to the momentum along the compact
fifth dimension:

  p_5 = n hbar / R    (n = 0, +/- 1, +/- 2, ...)

This gives the electric charge:

  e_n = n e

where e is the elementary charge, related to the radius R by:

  e = sqrt(16 pi G hbar / c) / R

This fixes R ~ 10^{-33} cm (the Planck length), explaining why the fifth dimension
is unobservable.

### 6. The Geodesic Equation

A free particle in five dimensions follows a geodesic:

  d^2 x^A / d tau^2 + Gamma^A_{BC} (dx^B / d tau)(dx^C / d tau) = 0

When projected to four dimensions, this becomes the Lorentz force law:

  m d^2 x^mu / d tau^2 = e F^{mu}_{nu} dx^nu / d tau

The electric charge e arises from the fifth component of the five-velocity:

  e ~ dx^5 / d tau

This is the original Kaluza miracle: the Lorentz force law is simply the geodesic
equation in five dimensions.

---

## Key Results

1. The five-dimensional Kaluza-Klein theory is formulated rigorously from three
   axioms, with the periodicity condition replacing the cylinder condition.

2. The 15-component 5D metric decomposes into: 4D metric (10), electromagnetic
   potential (4), and scalar field (1).

3. The five-dimensional vacuum Einstein equations reproduce 4D gravity + Maxwell
   theory + scalar field equation upon dimensional reduction.

4. The scalar field (dilaton/radion) couples to electromagnetism and introduces a
   new long-range force. Einstein and Bergmann suppressed it by setting phi = const.

5. Electric charge is quantized as momentum in the fifth dimension, fixing the
   compactification radius at the Planck scale.

6. The Lorentz force law is the four-dimensional projection of the five-dimensional
   geodesic equation.

---

## Impact and Legacy

Einstein and Bergmann's 1938 paper occupies a unique position in the history of
Kaluza-Klein theory:

- **Modern viewpoint**: It introduced the modern perspective of treating the fifth
  dimension as physically real (compact topology) rather than as a mathematical
  device. This is the viewpoint adopted by ALL subsequent work in extra dimensions.

- **The dilaton problem**: Their identification (and suppression) of the scalar field
  foreshadowed a central issue in string theory, where the dilaton plays a crucial
  role and its stabilization is a major challenge.

- **Bergmann's legacy**: Peter Bergmann went on to become a pioneer of canonical
  quantum gravity (the Bergmann-Dirac constraint analysis). His training with
  Einstein on five-dimensional theory informed his later work on the Hamiltonian
  formulation of general relativity.

- **Einstein's persistence**: Despite the scalar field difficulty, Einstein continued
  working on five-dimensional theories until 1943 (with Bergmann and Bargmann,
  1941). He only abandoned the approach when he became convinced that the quantum
  aspects could not be captured by classical geometry alone.

- **Witten's 2014 commentary** (arXiv:1401.8048) rehabilitated the paper, noting
  that the more symmetric version (with dynamical phi) is precisely the modern
  Kaluza-Klein theory, and that Einstein's retreat was premature.

---

## Connection to Phonon-Exflation Framework

The Einstein-Bergmann paper connects to the phonon-exflation framework in several
ways:

1. **Periodicity and compactness**: Einstein-Bergmann's Axiom II (periodicity of the
   fifth dimension) is the prototype for the compactness of the internal manifold K
   in the phonon-exflation framework. The key difference is that K = SU(3) is an
   8-dimensional Lie group, not a circle -- but the PRINCIPLE is the same.

2. **The scalar field as modulus**: Einstein-Bergmann's scalar phi controls the
   radius of the circle. In the phonon-exflation framework, the Jensen deformation
   parameter s controls the SHAPE of SU(3). Both are moduli of the internal
   geometry. The V_eff(s) computation is the modern version of asking what
   stabilizes phi.

3. **Geodesics and phonons**: The Einstein-Bergmann result that charged particles
   follow 5D geodesics is the classical precursor to the phonon-exflation claim
   that particles are excitations (phonons) of the internal geometry. In both
   cases, the particle content of 4D physics originates from the structure of the
   compact space.

4. **From U(1) to SU(3) x SU(2) x U(1)**: The Einstein-Bergmann theory produces
   only U(1) (electromagnetism) because the internal space is S^1 with isometry
   U(1). The phonon-exflation framework obtains the full Standard Model gauge
   group because the internal space is SU(3), whose isometry group (under Jensen
   deformation) breaks to U(1) x SU(2) x SU(3). This is the non-abelian
   generalization that DeWitt (1964), Kerner (1968), and Witten (1981)
   progressively developed.

5. **The variational principle**: Axiom III (derive field equations from a 5D action)
   is generalized in the phonon-exflation framework to the spectral action
   principle: S = Tr f(D^2/Lambda^2), where D is the Dirac operator on M4 x K.
   This is the Connes-Chamseddine spectral action, which the Baptista program
   computes explicitly.
