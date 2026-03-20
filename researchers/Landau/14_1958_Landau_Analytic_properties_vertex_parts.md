# On Analytic Properties of Vertex Parts in Quantum Field Theory

**Author:** Lev Davidovich Landau
**Year:** 1958
**Journal:** Nucl. Phys., 13, 181-192 (also Zh. Eksp. Teor. Fiz., 37, 62-70)

---

## 1. Historical Context: The Crisis of Quantum Field Theory in the 1950s

### 1.1 Renormalization and Its Discontents

By the late 1950s, quantum electrodynamics (QED) had been spectacularly
confirmed by the Lamb shift and the anomalous magnetic moment of the electron.
The renormalization program of Tomonaga, Schwinger, and Feynman had tamed the
infinities of perturbation theory: physical quantities could be computed to
any desired order by absorbing divergences into a finite number of redefined
parameters (mass, charge, field strength).

But the FOUNDATIONS were troubled. The perturbation series was known to
diverge (Dyson, 1952). The renormalized charge e(Lambda) exhibited a Landau
pole: at finite energy Lambda_L, the effective coupling diverges:

    alpha(Lambda) = alpha(0) / (1 - (alpha(0)/(3*pi)) * ln(Lambda^2/m_e^2))

This diverges at Lambda_L ~ m_e * exp(3*pi/(2*alpha)) ~ 10^{286} eV.
Landau himself (with Abrikosov and Khalatnikov, 1954) had discovered this
"zero charge" problem: in the exact theory, the renormalized charge vanishes
at any finite energy, or the theory is inconsistent.

### 1.2 The S-Matrix Alternative

Disillusioned with the Lagrangian/Hamiltonian framework, several physicists
-- prominently including Landau -- pursued an alternative: determine the
physical scattering amplitudes directly from their ANALYTIC PROPERTIES,
without reference to any particular dynamical framework.

The idea was that the S-matrix (the complete set of scattering amplitudes)
should satisfy:

1. **Unitarity**: SS^dagger = 1 (probability conservation)
2. **Crossing symmetry**: particle-antiparticle exchange
3. **Analyticity**: the S-matrix elements are analytic functions of the
   kinematic invariants (energies, momenta), with singularities only where
   physically required

If these constraints were strong enough, they might DETERMINE the S-matrix
uniquely, rendering the underlying Lagrangian irrelevant. This was the
analytic S-matrix program, pursued intensely from 1958 to the mid-1970s.

### 1.3 Landau's Contribution

Landau's 1958 paper addressed a precise mathematical question: WHERE are the
singularities of Feynman diagram amplitudes located in the space of external
momenta? The answer -- the Landau equations -- provided the foundation for
the entire analytic S-matrix program.


## 2. Feynman Diagrams and Their Integrals

### 2.1 The Feynman Amplitude

A Feynman diagram with L loops, I internal lines, and V vertices contributes
an amplitude of the form:

    A(p_1, ..., p_E) = integral [product_{l=1}^{L} d^4 k_l / (2*pi)^4]
                       * [product_{i=1}^{I} 1 / (q_i^2 - m_i^2 + i*epsilon)]
                       * N(k, p)

where:
- p_1, ..., p_E are the external momenta
- k_1, ..., k_L are the loop momenta
- q_i = q_i(k, p) is the momentum of the i-th internal line (a linear
  combination of loop and external momenta, determined by momentum
  conservation at each vertex)
- m_i is the mass of the particle on the i-th internal line
- N(k, p) is a numerator factor from vertex couplings and spin structure

### 2.2 Parametric Representation

Landau's analysis begins with the Feynman parametric representation. Using
the identity:

    1 / (A_1 * A_2 * ... * A_I)
        = (I-1)! * integral_0^1 [product d(alpha_i)]
          * delta(sum alpha_i - 1) / [sum alpha_i * A_i]^I

the amplitude becomes (after completing the square in the loop momenta and
integrating over them):

    A = C * integral [product d(alpha_i)] * delta(sum alpha_i - 1)
        * [alpha_i >= 0] / D(alpha, p)^{I - 2L}

where D(alpha, p) is a polynomial in the Feynman parameters alpha_i and
the external momenta p_j. The function D encodes the topology of the diagram.

The singularities of A as a function of the external momenta p_j occur when
the denominator D(alpha, p) vanishes within the integration region.


## 3. The Landau Equations

### 3.1 Conditions for Singularity

Landau derived the conditions under which D(alpha, p) = 0 for alpha_i within
the physical integration region (alpha_i >= 0, sum alpha_i = 1). The result
is a set of algebraic equations:

**Landau equations:**

For each internal line i:

    alpha_i * (q_i^2 - m_i^2) = 0                      ... (L1)

For each independent loop l:

    sum_{i in loop l} alpha_i * q_i^mu = 0               ... (L2)

with alpha_i >= 0.

### 3.2 Interpretation of the Conditions

Equation (L1) says: for each internal line, EITHER alpha_i = 0 (the line is
"contracted" -- removed from the diagram) OR q_i^2 = m_i^2 (the internal
particle is ON SHELL -- it satisfies the mass-shell condition).

Equation (L2) says: the momenta of the on-shell internal particles, weighted
by the Feynman parameters alpha_i, sum to zero around each loop.

Together: a singularity of the amplitude occurs when a subset of internal
particles are simultaneously on-shell and their momenta satisfy a
"conservation" condition (L2) at each vertex.

### 3.3 The alpha_i as Schwinger Proper Times

The Feynman parameters alpha_i have a physical interpretation: they are
proportional to the PROPER TIME that each internal particle propagates.
Equation (L2) then becomes:

    sum alpha_i * q_i = 0  <=>  sum (proper time)_i * (velocity)_i = 0

This means the internal particles, propagating classically (on-shell) for
their respective proper times, form a CLOSED LOOP in spacetime. The
singularity occurs when the Feynman diagram can be interpreted as a
CLASSICAL PROCESS: all internal particles propagate on-shell along
classical trajectories that close upon themselves.


## 4. Physical Interpretation: Classical Propagation

### 4.1 The Coleman-Norton Theorem

Coleman and Norton (1965) proved: a Feynman diagram has a leading Landau
singularity if and only if the diagram can be interpreted as a CLASSICAL
SCATTERING PROCESS -- each internal line is a real on-shell particle
propagating along a classical trajectory, with future-directed 4-velocities,
consistent spacetime separations, and energy-momentum conservation at each
vertex.

### 4.2 Example: The Triangle Diagram

Consider the triangle diagram with three internal lines of masses m_1, m_2,
m_3 and three external momenta p_1, p_2, p_3 (with p_1 + p_2 + p_3 = 0).

The Landau equations are:

    alpha_1 * (q_1^2 - m_1^2) = 0
    alpha_2 * (q_2^2 - m_2^2) = 0
    alpha_3 * (q_3^2 - m_3^2) = 0
    alpha_1 * q_1 + alpha_2 * q_2 + alpha_3 * q_3 = 0

(one loop equation). Setting all alpha_i > 0 (leading singularity), all
three particles must be on-shell, and the weighted sum of momenta must
vanish. This determines a surface in the space of external invariants
(p_1^2, p_2^2, p_3^2) -- the Landau surface for the triangle diagram.

The physical interpretation: three real particles form a triangle in
spacetime, each propagating classically from one vertex to the next. The
singularity occurs at the precise external momenta where this classical
process is kinematically possible.

The box diagram (four lines, four vertices) is analogous: the leading
singularity is a rectangle of classical particles in spacetime, giving a
codimension-1 surface in the Mandelstam (s, t) plane.


## 5. Leading, Subleading Singularities, and the Landau Surface

When ALL alpha_i > 0, the singularity is LEADING (all particles on-shell).
When some alpha_i = 0, those lines are contracted, producing SUBLEADING
singularities from reduced diagrams. The hierarchy of contractions organizes
the full singularity structure.

The Landau surface is the algebraic variety in kinematic space where
solutions exist. The amplitude is analytic away from this surface, with branch
cuts or poles on it. Normal thresholds (e.g., s = (m_1 + m_2)^2) are
boundaries of the physical region; anomalous thresholds can lie inside it.


## 6. Connection to Dispersion Relations and Unitarity

### 6.1 Dispersion Relations

A dispersion relation expresses the real part of a scattering amplitude in
terms of an integral over its imaginary part (the discontinuity across a
branch cut):

    Re A(s) = (1/pi) * P.V. integral ds' * Im A(s') / (s' - s) + subtractions

The Landau singularities determine WHERE the branch cuts are. Without knowing
the singularity structure, one cannot write down the correct dispersion
relation.

For forward scattering amplitudes, the optical theorem relates the imaginary
part to the total cross section:

    Im A(s, t=0) = s * sigma_total(s)

Combining with the dispersion relation gives Kramers-Kronig-type sum rules
connecting different physical observables.

### 6.2 Cutkosky Rules

Cutkosky (1960) showed that the discontinuity of a Feynman amplitude across a
normal threshold can be computed by a simple rule: REPLACE each internal
propagator that goes on-shell by a delta function:

    1 / (q_i^2 - m_i^2 + i*epsilon) --> -2*pi*i * delta(q_i^2 - m_i^2) * theta(q_i^0)

and integrate over the remaining loop momenta. This is the generalized optical
theorem.

The Cutkosky rules are DUAL to the Landau equations: the Landau equations say
where the singularity is; the Cutkosky rules say what the discontinuity is at
that singularity.

### 6.3 Unitarity and Hermitian Analyticity

The unitarity of the S-matrix (SS^dagger = 1) imposes:

    2 * Im T = T^dagger * T     (optical theorem for the T-matrix, S = 1 + iT)

Combined with crossing symmetry and analyticity, this is enormously
constraining. The Mandelstam representation (double dispersion relation in s
and t) was proposed as a complete characterization of the amplitude's analytic
structure, with the Landau singularities as the only allowed discontinuities.


## 7. The Russian School and Subsequent Developments

Landau and colleagues (Abrikosov, Khalatnikov, Ter-Martirosian, Sudakov)
pursued the view that the S-matrix -- constrained by analyticity, unitarity,
and crossing -- might be more fundamental than any Lagrangian. This merged
with Regge theory (1959-1960), where analytic continuation to complex angular
momentum l yields Regge poles that determine high-energy cross sections:

    sigma_total(s) ~ s^{alpha(0) - 1}

Chew's bootstrap (1961-1966) pushed this to the extreme: all hadrons are
self-consistently determined by S-matrix axioms, with no fundamental
Lagrangian. The bootstrap had real successes (Veneziano amplitude, duality)
but was supplanted by QCD (1973), which generates the correct analytic
structure from a Lagrangian framework.

Since ~2005, Landau's ideas have revived. Modern amplitude methods (BCFW
recursion, generalized unitarity, amplituhedron) use analyticity as a
COMPUTATIONAL tool. Landau singularity analysis is now applied to multi-loop
LHC phenomenology.


## 8. Singularity Classification and Limitations

### 8.1 Normal and Anomalous Thresholds

Normal thresholds are the simplest Landau singularities: for a two-particle
intermediate state with masses m_1 and m_2, the branch point is at
s = (m_1 + m_2)^2. Anomalous thresholds arise when three or more internal
particles are simultaneously on-shell, and can lie BELOW the normal threshold
(first identified by Karplus, Neuman, and Sturm for the triangle diagram).

### 8.2 Pinch Singularities and Second-Type Singularities

Mathematically, a Landau singularity is a PINCH: the integration contour is
trapped between two singularities of the integrand approaching from opposite
sides. Second-type singularities occur when alpha_i -> infinity, corresponding
to zero proper time (ultraviolet effects related to renormalization).

### 8.3 Limitations

The Landau equations are NECESSARY but not sufficient: cancellations from
numerators can eliminate potential singularities. Full sufficient conditions
require Picard-Lefschetz theory (Pham). The Landau analysis is perturbative
-- non-perturbative singularities (instantons, renormalons) and infrared
divergences in massless theories lie beyond its scope.


## 9. Connection to Phonon-Exflation Cosmology

### 10.1 Analyticity of the Spectral Action

The spectral action of the phonon-exflation framework is:

    S(s) = Tr(f(D_K(s)^2 / Lambda^2))

where D_K(s) is the Dirac operator on the Jensen-deformed SU(3) and s is the
deformation parameter. This is a function of s (and the cutoff Lambda). The
question: what is the analytic structure of S(s)?

Landau's singularity analysis provides a framework for answering this. The
eigenvalues lambda_n(s) of D_K(s) are analytic functions of s except at
points where eigenvalues cross (level crossings). At a crossing, the spectral
action can have a non-analytic point (kink, cusp, or branch point) depending
on the nature of the crossing.

### 10.2 Seeley-DeWitt as Asymptotic Expansion

The Seeley-DeWitt expansion of the spectral action is:

    S(s) ~ sum_{n=0}^{N} f_n * a_n(s) * Lambda^{d-2n} + O(Lambda^{d-2N-2})

where d is the dimension and a_n(s) are the Seeley-DeWitt coefficients. This
is an ASYMPTOTIC expansion in Lambda^{-2} -- it diverges for any finite
Lambda. The precise sense in which it approximates S(s) depends on the
analytic structure of S as a function of Lambda^{-2}.

Landau's singularity analysis for the spectral zeta function:

    zeta_D(z) = Tr(|D_K(s)|^{-2z}) = sum_n |lambda_n(s)|^{-2z}

would reveal the poles and branch cuts of zeta_D in the complex z-plane.
These correspond to the Seeley-DeWitt coefficients:

    a_n(s) = Res_{z=(d-2n)/2} zeta_D(z)

The convergence or divergence of the Seeley-DeWitt series is thus controlled
by the spacing and nature of the poles of zeta_D -- which is a Landau
singularity analysis applied to the spectral action rather than to a
scattering amplitude.

### 10.3 Phase Transitions in s-Space

The most physically important question for phonon-exflation is: does the
spectral action S(s) have singularities (or near-singularities) at specific
values of s that could drive phase transitions?

If S(s) has a cusp at s = s_0, this could indicate:
- A first-order transition in the internal geometry
- A spontaneous breaking of the SU(3) isometry to a subgroup
- A change in the number of light modes (Kaluza-Klein threshold)

These are the PHYSICAL analogs of Landau singularities: the internal momenta
(eigenvalues of D_K) go on-shell (cross zero or each other) at specific
values of the external parameter (s), causing non-analyticities in the
integrated quantity (spectral action).

### 10.4 Landau Singularities and the Spectral Zeta Function

The spectral zeta function zeta_D(z, s) depends on TWO complex variables.
Its singularity structure encodes the UV theory (poles in z), the geometric
phase structure (branch cuts in s at level crossings), and the interplay
between them (how a_n(s) behaves near geometric transitions). Mapping this
structure is a Landau analysis for the spectral action.

The Coleman-Norton analog: S(s) has a singularity when multiple eigenvalues
of D_K(s) simultaneously satisfy a resonance condition -- corresponding to
enhanced symmetry points where the deformed metric has accidental degeneracies.
These may select preferred values of s where gauge couplings unify or the phi_paasch
ratio appears in the mass spectrum.

---

## References

1. L. D. Landau, "On analytic properties of vertex parts in quantum field
   theory," Nucl. Phys. 13, 181-192 (1959) [submitted 1958]; also Zh.
   Eksp. Teor. Fiz. 37, 62-70 (1959).
2. S. Coleman and R. E. Norton, "Singularities in the physical region,"
   Nuovo Cim. 38, 438-442 (1965).
3. R. E. Cutkosky, "Singularities and discontinuities of Feynman
   amplitudes," J. Math. Phys. 1, 429-433 (1960).
4. R. J. Eden, P. V. Landshoff, D. I. Olive, and J. C. Polkinghorne,
   The Analytic S-Matrix (Cambridge University Press, 1966).
5. V. V. Sudakov, "Vertex parts at very high energies in quantum
   electrodynamics," Zh. Eksp. Teor. Fiz. 30, 87 (1956) [Sov. Phys.
   JETP 3, 65 (1956)].
6. T. Regge, "Introduction to complex orbital momenta," Nuovo Cim. 14,
   951-976 (1959).
7. G. F. Chew, S-Matrix Theory of Strong Interactions (Benjamin, 1961).
8. N. Arkani-Hamed, J. L. Bourjaily, F. Cachazo, A. B. Goncharov,
   A. Postnikov, and J. Trnka, "Scattering amplitudes and the positive
   Grassmannian," arXiv:1212.5605 (2012).
9. R. P. Feynman, "Space-time approach to quantum electrodynamics,"
   Phys. Rev. 76, 769-789 (1949).
10. F. Pham, Introduction a l'etude topologique des singularites de
    Landau (Gauthier-Villars, 1967).
