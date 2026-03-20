# On the Removal of Infinities in Quantum Electrodynamics (The Asymptotic Expression for the Green Function in QED)

**Authors:** Lev Landau, Alexei Abrikosov, Isaak Khalatnikov
**Year:** 1954
**Journal:** Doklady Akad. Nauk SSSR, 95, 497-500 (and subsequent longer papers 1954-1955)

---

## 1. Historical Context

By 1949, the renormalization program for quantum electrodynamics (QED) had been completed
through the independent work of Tomonaga, Schwinger, Feynman, and the synthesis by Dyson.
The procedure worked: at every order of perturbation theory, ultraviolet divergences could
be absorbed into redefinitions of the electron mass m, the electron charge e, and the field
normalizations. Physical predictions -- the anomalous magnetic moment of the electron, the
Lamb shift, vacuum polarization corrections -- agreed with experiment to extraordinary
precision.

But a question remained: what happens when you sum the perturbation series to all orders?
Is the renormalized theory self-consistent as a complete quantum field theory, or is it
merely an asymptotic expansion that breaks down at sufficiently high energies?

This was the question that Landau, together with his students Abrikosov and Khalatnikov,
addressed in a series of papers in 1954-1955 that became known as the "Moscow zero-charge"
or "Landau ghost" papers. Their answer was disturbing: QED, when pushed to all orders,
appears to be either inconsistent (the effective charge diverges at a finite energy scale)
or trivial (the physical charge is zero if the cutoff is removed).


## 2. The Leading Logarithm Approximation

The LAK approach was to identify the dominant contribution at each order of perturbation
theory and sum them. In QED, the dominant terms at high momentum transfer q are the
leading logarithms: terms of the form (alpha * ln(q^2/m^2))^n at n-th order.

These leading logarithms arise from vacuum polarization -- the screening of the bare charge
by virtual electron-positron pairs. At one loop, the vacuum polarization tensor gives:

```
Pi(q^2) = -(e^2/(3*pi)) * ln(q^2/m^2) + O(1)
```

for q^2 >> m^2. The photon propagator, dressed by vacuum polarization, becomes:

```
D(q^2) = D_0(q^2) / (1 - Pi(q^2))
       = D_0(q^2) / (1 - (e^2/(3*pi)) * ln(q^2/m^2))
```

where D_0(q^2) = 1/q^2 is the bare propagator.

At higher loops, the leading logarithm at n-th order contributes a term proportional to
(e^2 * ln(q^2/m^2))^n. Landau, Abrikosov, and Khalatnikov showed that summing these
leading logarithms to all orders yields the geometric series implicit in the dressed
propagator above.


## 3. The Effective (Running) Coupling

The dressed propagator defines an effective coupling constant that depends on the momentum
scale q^2. Since the photon propagator mediates the electromagnetic interaction, the
effective fine structure constant at momentum scale q^2 is:

```
alpha_eff(q^2) = alpha / (1 - (alpha/(3*pi)) * ln(q^2/m^2))
```

where alpha = e^2/(4*pi) ~ 1/137 is the physical fine structure constant measured at
low energies (q^2 ~ m^2).

This is the running coupling constant of QED. Its behavior is:
- At low q^2: alpha_eff ~ alpha ~ 1/137
- At moderate q^2: alpha_eff increases logarithmically (charge antiscreening is overcome)
- At very high q^2: alpha_eff -> infinity when the denominator vanishes

The effective coupling INCREASES with energy because vacuum polarization SCREENS the bare
charge: at large distances (low q^2), virtual pairs surround the bare charge and reduce the
observed charge. Probing at shorter distances (higher q^2) penetrates the screening cloud
and sees more of the bare charge.

This behavior is opposite to QCD, where the gluon self-interaction produces antiscreening
and the coupling DECREASES at high energy (asymptotic freedom).


## 4. The Landau Pole

The denominator of the running coupling vanishes at:

```
q^2 = m^2 * exp(3*pi/alpha) ~ m^2 * exp(3*pi * 137) ~ m^2 * exp(1292)
```

This is the Landau pole. At this momentum scale, the effective coupling diverges:
alpha_eff -> infinity. The energy scale is:

```
Lambda_Landau = m * exp(3*pi/(2*alpha)) ~ 10^{280} GeV
```

This is an astronomically large energy, vastly exceeding the Planck scale (~10^{19} GeV).
In practical terms, the Landau pole is never reached in any conceivable experiment.

However, the Landau pole has profound theoretical implications:

1. **QED is not UV-complete**: The theory cannot be extrapolated to arbitrarily high
   energies. At or before the Landau pole, new physics must intervene.

2. **The bare charge is infinite (or QED is trivial)**: If one attempts to take the UV
   cutoff Lambda -> infinity while keeping the physical charge alpha fixed, the bare
   charge alpha_0 must diverge. Conversely, if one insists that the bare charge is finite,
   the physical charge is driven to zero as Lambda -> infinity.

3. **Perturbation theory breaks down**: Near the Landau pole, alpha_eff >> 1 and the
   perturbative expansion is meaningless. The leading logarithm sum itself becomes
   unreliable.


## 5. The Moscow Zero-Charge Conjecture

Landau and his collaborators drew a radical conclusion: QED with a removed cutoff
(Lambda -> infinity) has zero physical charge. The argument runs as follows.

The relation between bare charge alpha_0 (at the cutoff Lambda) and physical charge
alpha (at the electron mass m) is:

```
1/alpha = 1/alpha_0 + (1/(3*pi)) * ln(Lambda^2/m^2)
```

As Lambda -> infinity, the logarithm diverges, and:
- If alpha_0 is held fixed (finite), then 1/alpha -> infinity, i.e., alpha -> 0
- If alpha is held fixed (at 1/137), then alpha_0 -> infinity before Lambda reaches
  Lambda_Landau

Landau concluded that the only self-consistent QED with no cutoff has alpha = 0 -- a
free, non-interacting theory. This is the "zero-charge" or "Moscow zero" result.

The conjecture extended beyond QED: Landau and Pomeranchuk (1955) argued that ANY quantum
field theory with a positive beta function (coupling increasing with energy) would suffer
the same fate. Only theories with a negative beta function -- what would later be called
asymptotically free theories -- could be consistent at all energies.

This was remarkably prescient. Twenty years later, Gross, Wilczek, and Politzer (1973)
discovered that non-abelian gauge theories (like QCD with sufficiently few quark flavors)
ARE asymptotically free, and that QCD's negative beta function is precisely what makes it
a consistent theory at all scales.


## 6. The Beta Function and Renormalization Group

The LAK result can be expressed in the language of the renormalization group (developed
independently by Gell-Mann and Low in 1954, and by Bogoliubov and Shirkov in 1955-1956):

```
beta(alpha) = mu * d(alpha)/d(mu) = (2*alpha^2)/(3*pi) + O(alpha^3)
```

where mu is the renormalization scale. The positive sign of the leading coefficient means
alpha increases with mu (energy scale).

For QCD with SU(3) gauge group and N_f quark flavors:

```
beta_QCD(g) = -(g^3/(16*pi^2)) * (11 - (2/3)*N_f) + O(g^5)
```

The coefficient (11 - (2/3)*N_f) is positive for N_f < 16.5, making beta negative and the
theory asymptotically free. For the physical value N_f = 6: 11 - 4 = 7 > 0.

The sign difference between QED (beta > 0) and QCD (beta < 0) is one of the most important
distinctions in quantum field theory. It determines:
- QED: charge screening, Landau pole, triviality
- QCD: charge antiscreening, asymptotic freedom, confinement


## 7. Triviality and Lattice Verification

The zero-charge conjecture was tested non-perturbatively using lattice gauge theory,
beginning in the 1980s with the work of Wilson and others.

For lattice QED (U(1) gauge theory in 4D), extensive numerical simulations have confirmed
that the theory is TRIVIAL in the technical sense: the renormalized coupling goes to zero
as the lattice spacing a -> 0 (continuum limit) at fixed physical volume. There is no
interacting continuum limit.

The evidence includes:
- Monte Carlo simulations showing alpha_R -> 0 as a -> 0
- The absence of a non-trivial UV fixed point in the beta function
- Mean-field-like behavior of critical exponents at the phase transition

This means QED is not a fundamental theory but an effective field theory, valid below some
cutoff scale. The cutoff is provided by the electroweak unification scale (~100 GeV),
above which QED is subsumed into the SU(2) x U(1) electroweak theory.

The same triviality issue affects:
- Scalar phi^4 theory in 4D (Higgs sector of the Standard Model)
- The Yukawa sector
- Any U(1) gauge theory in 4D

Asymptotically free theories (QCD, non-abelian gauge theories) do NOT suffer from
triviality and have well-defined continuum limits.


## 8. The Electron Propagator and Vertex

LAK also analyzed the electron propagator and the electron-photon vertex in the leading
logarithm approximation. The electron propagator:

```
G(p) = Z_2(p^2) / (gamma_mu * p^mu - m)
```

has a wave function renormalization Z_2 that depends on the gauge parameter xi (Landau
gauge, Feynman gauge, etc.). In the Landau gauge (xi = 0), Z_2 has no leading logarithmic
correction, simplifying the analysis.

The Ward-Takahashi identity constrains the vertex:

```
q_mu * Gamma^mu(p, p+q) = G^{-1}(p+q) - G^{-1}(p)
```

This identity ensures that the charge renormalization is determined entirely by the
photon propagator (vacuum polarization), not the vertex or electron propagator separately.
LAK used this to argue that the leading logarithm sum for the running coupling is exact
in the leading-log approximation.

The Landau gauge (xi = 0) played a special role in the LAK analysis. In this gauge, the
photon propagator is transverse:

```
D_mu_nu(q) = (g_mu_nu - q_mu*q_nu/q^2) * D(q^2)
```

and the electron propagator has particularly simple analytic properties. Landau argued
that xi = 0 is the only physical gauge -- a position that remains debated but has
been influential in the development of gauge theory.


## 9. Landau Pole in the Standard Model

The Landau pole problem extends to the full Standard Model through the U(1)_Y hypercharge
coupling g_1 (or equivalently, g' or alpha_1):

```
beta(g_1) = (1/(16*pi^2)) * (41/6) * g_1^3 + ...
```

The positive beta function means g_1 increases with energy and hits a Landau pole at:

```
Lambda_1 ~ M_Z * exp(16*pi^2 / ((41/6)*g_1^2(M_Z)))  ~  10^{42} GeV
```

This is far below the QED Landau pole but still above the Planck scale. However, it
signals that the Standard Model as written cannot be the ultimate theory -- grand
unification or new physics must intervene.

The SU(2)_L coupling g_2 and SU(3)_C coupling g_3 both have negative beta functions
(asymptotically free), so they do not develop Landau poles. The running of all three
couplings toward approximate unification at ~10^{16} GeV is the basis for grand unified
theories (GUTs).


## 10. The LAK Method and Modern RG

The LAK leading-logarithm summation was an early form of what became the renormalization
group (RG). The relationship between the approaches:

| LAK (1954) | Modern RG |
|:-----------|:----------|
| Sum leading logs | Solve RG equation |
| Geometric series | Exponentiate beta function |
| Landau pole | UV fixed point (trivial) |
| Zero charge | Triviality / Gaussian fixed point |
| Cutoff-dependent bare charge | Running coupling alpha(mu) |

The modern perspective, due to Wilson (1971-1974), reinterprets the Landau pole not as a
catastrophe but as a signal: QED is an effective field theory with a natural UV cutoff.
Below the cutoff, the theory makes precise predictions. Above the cutoff, new degrees of
freedom (W, Z bosons, ultimately strings or whatever) take over.

Wilson's insight resolved the philosophical tension in LAK: one does not NEED to take
Lambda -> infinity. Physics at scale mu is described by the effective theory at that scale,
with the effects of higher scales encoded in the coupling constants.


## 11. Connection to Phonon-Exflation Framework

The LAK analysis of running couplings connects to the phonon-exflation framework in
several ways:

**Running couplings from geometry**: In the phonon-exflation framework, the gauge
couplings g_1, g_2, g_3 are determined by the geometry of the internal space K = SU(3).
The Jensen TT-deformation parameter s controls the internal metric, and the gauge
couplings run with s according to the geometric formulas derived in Session 17a (B-1):

```
g_1^2 ~ e^{2s}    (U(1) sector)
g_2^2 ~ e^{-2s}   (SU(2) sector, from su(2) subalgebra)
g_3^2 = const      (SU(3) sector, volume-preserving)
```

This is NOT the perturbative running of QED/QCD (which depends on loop corrections from
matter fields) but rather a GEOMETRIC running from the shape of the internal manifold. The
Landau pole problem asks: why do the couplings have the values they do at low energy? The
spectral action on deformed SU(3) provides a candidate answer: the couplings are fixed by
the equilibrium geometry at the V_eff minimum s = s_0.

**Triviality and UV completion**: The LAK triviality result for U(1) means that the
hypercharge sector of the Standard Model requires UV completion. In the phonon-exflation
framework, the UV completion is provided by the full Kaluza-Klein spectrum on M4 x SU(3):
above the compactification scale, the theory is a higher-dimensional geometric theory, not
a 4D gauge theory. The Landau pole is never reached because the effective 4D description
breaks down first.

**The spectral action and coupling unification**: The spectral action Tr(f(D^2/Lambda^2))
evaluated on the deformed SU(3) produces a classical action whose gauge kinetic terms
encode the coupling constants. The question of whether the couplings unify at some
scale -- the GUT motivation -- becomes the question of whether there exists an s value
where the spectral action has enhanced symmetry. The bi-invariant point s = 0 has
SU(3) x SU(3) symmetry and equal gauge kinetic coefficients for all generators, which is
the geometric analog of coupling unification.

**The Weinberg angle from geometry**: The ratio g_1/g_2 = e^{-2s} determines the Weinberg
angle through sin^2(theta_W) = g_1^2/(g_1^2 + g_2^2). The observed value
sin^2(theta_W) ~ 0.231 fixes s_0 ~ 0.299 (Session 17a, B-1). This is a geometric
prediction -- the Weinberg angle is determined by the shape of the internal space at
its equilibrium configuration.


## 12. The Abrikosov Connection

Alexei Abrikosov, Landau's student and co-author on the LAK papers, went on to discover
the mixed state (Abrikosov vortex lattice) of type-II superconductors in 1957, for which
he received the Nobel Prize in 2003. The vortices in the GPE simulation of
phonon-exflation are direct descendants of Abrikosov vortices -- topological defects in
the complex order parameter carrying quantized circulation.

The LAK paper thus connects two threads that converge in the phonon-exflation framework:
the running of gauge couplings (from QED renormalization) and the topology of the order
parameter (from Abrikosov's subsequent work on superconductivity). Both are aspects of the
same condensed-matter-to-cosmology dictionary.


## 13. Legacy and Influence

The LAK papers of 1954-1955 had lasting impact:

1. **Identified the Landau pole**: The first signal that QED is not UV-complete
2. **Predicted triviality of QED**: Confirmed by lattice calculations 30 years later
3. **Introduced running couplings**: Independently of Gell-Mann and Low, established the
   concept of scale-dependent coupling constants
4. **Motivated asymptotic freedom**: The search for theories WITHOUT Landau poles led
   directly to the discovery of asymptotic freedom in 1973
5. **Weinberg's theorem**: The hierarchy of divergences (leading, subleading logs)
   formalized by Weinberg (1960) built on the LAK classification
6. **Effective field theory philosophy**: The recognition that QED needs a cutoff
   anticipated Wilson's effective field theory framework by two decades

The Moscow school's work on QED, though initially controversial (especially the zero-charge
conjecture), has been vindicated by the modern understanding of quantum field theory as an
effective description valid below a cutoff, with the values of coupling constants at low
energies determined by the UV completion.

---

**Key equations:**
- Running coupling: alpha_eff(q^2) = alpha / (1 - (alpha/(3*pi)) * ln(q^2/m^2))
- Landau pole: Lambda = m * exp(3*pi/(2*alpha))
- QED beta function: beta(alpha) = (2*alpha^2)/(3*pi)
- Zero-charge: alpha -> 0 as cutoff Lambda -> infinity at fixed alpha_0
