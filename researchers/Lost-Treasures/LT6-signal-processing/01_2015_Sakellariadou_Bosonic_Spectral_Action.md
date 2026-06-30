# Aspects of the Bosonic Spectral Action

**Author(s):** Mairi Sakellariadou
**Year:** 2015
**arXiv:** 1503.01671
**Journal:** arXiv:1503.01671 [hep-th]

---

## Abstract

A brief description of the elements of noncommutative spectral geometry as an approach to unification is presented. The physical implications of the doubling of the algebra are discussed. Some high energy phenomenological as well as various cosmological consequences are presented. A constraint in one of the three free parameters, namely the one related to the coupling constants at unification, is obtained, and the possible role of scalar fields is highlighted. A novel spectral action approach based upon zeta function regularisation, in order to address some of the issues of the traditional bosonic spectral action based on a cutoff function and a cutoff scale, is discussed.

---

## Historical Context

Noncommutative spectral geometry (NCSG) presents an alternative approach to quantum gravity and the Standard Model unification, distinct from string theory. Rather than quantizing spacetime or invoking extra dimensions in a top-down manner, NCSG proposes that the Standard Model *dictates* spacetime geometry. The theory treats the algebra of observables as fundamental: spacetime structure emerges from the spectrum of differential operators (the Dirac operator), specifically.

The spectral action principle is elegant: rather than constructing an action functional by hand, one uses the spectral properties of operators to define the theory. The action sums all frequencies of vibration in spacetime -- a signal-processing analogy that proves central to understanding Lambda_residual as a DC component.

A critical innovation in this 2015 paper is the introduction of zeta function regularization as an alternative to the cutoff-based spectral action. The traditional approach uses heat kernel expansion and a cutoff function f(x), which creates interpretive ambiguity at high energies and depends on the arbitrary choice of f. The zeta approach replaces this with purely spectral (scale-independent) regularization.

---

## Key Arguments and Derivations

### The Spectral Triple and Almost-Commutative Geometry

The core object is a spectral triple (A, H, D) where:
- A is the algebra of observables (C^∞(M) for 4D spacetime)
- H is the Hilbert space of spinors (L^2(M, S))
- D is the Dirac operator -iγ^μ ∇_μ

For almost-commutative manifolds M × F (spacetime × finite internal space), the spectral triple becomes:

M × F := (C^∞(M, A_F), L^2(M, S) ⊗ H_F, /D ⊗ I + γ_5 ⊗ D_F)

The finite algebra A_F must be A_F = M_a(H) ⊕ M_k(C) to reproduce Standard Model fermion counts.

### The Cutoff Spectral Action

The cutoff bosonic spectral action is:

S_Λ = Tr(f(D_A^2 / Λ^2))

where f is a cutoff function (e.g., f(x) = 1 for x ≤ Λ or f(x) = e^{-x}) and Λ is the energy scale. This trace sums eigenvalues of the fluctuated Dirac operator D_A below the cutoff energy.

Expanding in powers of Λ using heat kernel techniques:

Tr[f(D_A^2 / Λ^2)] ~ 2f_4 Λ^4 a_0(D_A^2) + 2f_2 Λ^2 a_2(D_A^2) + f(0) a_4(D_A^2) + O(Λ^{-2})

where:
- f_4 = ∫_0^∞ f(u) u^3 du  [related to cosmological constant]
- f_2 = ∫_0^∞ f(u) u du    [related to gravitational constant]
- f_0 = f(0)               [related to coupling constants at unification]

The three momenta f_4, f_2, f_0 are the only terms that survive the asymptotic expansion. This is a **critical insight for the DC component interpretation**: the constant term f(0) is precisely the zero-frequency (DC) contribution to the spectral integral.

### The Derived Lagrangian at Cutoff Scale Λ

After including fermionic contributions:

S_Λ = -2af_2Λ^2 + ef_0/π^2 ∫|φ|^2 √g d^4x + f_0/(2π^2) ∫a|D_μφ|^2 √g d^4x - ...

The constant term ef_0/π^2 effectively acts as a vacuum energy density - **this is where the DC (zero-frequency) contribution manifests in the Lagrangian density**.

### Gravitational Sector and Extended Gravity

The Lagrangian in Euclidean signature is:

S_E = ∫[1/(2κ_0^2) R + α_0 C_{μνρσ} C^{μνρσ} + γ_0 + τ_0 R^* R^* + (gauge + scalar terms)] √g d^4x

where:
- γ_0 = (1/π^2)[48f_4Λ^4 - f_2Λ^2 c + f_0 d/4]

The γ_0 term is the vacuum energy contribution, and it contains f_0 -- the DC component of the spectral function. The cosmological constant emerges naturally as the f(0) contribution to the heat kernel expansion.

### Signal Processing Interpretation: Power Spectral Density View

Reinterpreting the spectral action as a power spectral density analysis:

- The eigenvalue spectrum of D_A^2 acts like a PSD: each eigenvalue λ_i contributes weight to the total integral
- The cutoff function f plays the role of a filter that suppresses high-frequency modes (eigenvalues > Λ)
- The Seeley-de Witt heat kernel expansion a_n decomposes the spectrum into multipole moments:
  - a_0: total integrated spectral weight (high-frequency content)
  - a_2: next-order spectral moment (mid-frequency content)
  - a_4: zero-frequency DC component (constant background)

**The cosmological constant Lambda_0 emerges from f(0), the DC (zero-frequency) component of the spectral response function.**

### Zeta Function Regularization (Innovation)

To address ultraviolet issues and scale-dependence, the zeta spectral action is proposed:

S_ζ = lim_{s→0} Tr D^{-2s} = ζ(0, D^2)

Equivalently, using the a_4 heat kernel coefficient:

S_ζ = a_4[D^2] = ∫ d^4x √g L(x), where L(x) = a_4(D^2, x)

The resulting Lagrangian density is:

L(x) = α_1 M^4 + α_2 M^2 R + α_3 M^2 H^2 + α_4 B_{μν} B^{μν} + ... + α_10 R^* R^*

where α_i are dimensionless constants. Notably, the zeta action is **independent of cutoff scale Λ** and depends only on spectral properties.

The spectral dimension D_s for the gravitational sector is:

D_s = 2 (ultraviolet), D_s^{low} = 4 (infrared)

This separation of scales aligns with signal processing concepts: high frequencies (UV) have different dimensionality than low frequencies (IR).

### Physical Implications of Algebra Doubling

The doubling of the algebra (two copies of spacetime) has profound consequences:
1. **Dissipation:** The doubled coordinate acts as a gauge reservoir, relating information loss to quantization
2. **Gauge structure:** The Y-coordinate becomes the internal gauge field to which the X-coordinate couples
3. **Neutrino mixing:** Emerges from deformed Hopf algebra structure in the doubled algebra

This doubling is essential for incorporating Standard Model gauge symmetries and is intimately related to the dissipative nature of the vacuum state.

---

## Key Results

1. **Spectral action unifies gravity with Standard Model** -- Einstein-Hilbert action plus Yang-Mills plus Higgs emerge from spectral properties of D_A

2. **Three free parameters constrained by observation** -- f_4 (CC), f_2 (gravitational constant), f_0 (coupling unification)

3. **Cosmological constant emerges as f(0)** -- the DC (zero-frequency) moment of the spectral function

4. **Zeta regularization removes cutoff ambiguity** -- action is now scale-independent and renormalisable; Lagrangian is local with only 4th-order operators

5. **Higgs mass prediction refined** -- including singlet-doublet mixing yields m_h = 125 GeV consistent with experiment (previous prediction: 167-176 GeV)

6. **GUT-scale unification predictions** -- Coupling constants meet at ~10^{16-17} GeV within few percent (big desert hypothesis approximately valid)

7. **See-saw mechanism for neutrino masses** -- predicted as consequence of spectral triple structure

8. **Gravitational wave signatures** -- Modified GR allows resonance at critical frequency ω_c = cβ = c(−α_0 G)^{-1}, detectable by LIGO/VIRGO

9. **Binary pulsar constraints** -- β >= 7.55×10^{-13} m^{-1} from orbital decay measurements

10. **Torsion balance limits** -- Strongest constraint β >= 10^4 m^{-1} from sub-mm fifth-force searches

---

## Impact and Legacy

This paper is foundational for understanding the spectral action as the correct framework for quantum gravity coupled to the Standard Model. The zeta function regularization proposal has inspired subsequent work on:

- Scale-invariant formulations of spectral geometry
- Connection to Weyl geometry and conformal properties
- Higgs inflation mechanisms
- Modified gravity phenomenology testable by current and future gravitational wave detectors

The DC component interpretation of the cosmological constant -- emerging from f(0) in the spectral expansion -- is particularly relevant for understanding vacuum energy as an infrared (zero-frequency) property of spacetime geometry.

---

## Connection to Phonon-Exflation Framework

**Direct and Profound Connection:**

The spectral action principle maps directly onto phonon-exflation cosmology. In the framework:

1. **M4 × SU(3) geometry as spectral triple** -- Spacetime coupled to internal color space is itself a spectral manifold. Particles are excitations of this combined geometry.

2. **Lambda_residual as DC component** -- The cosmological constant Lambda_residual in the framework should be identified with f(0), the zero-frequency contribution to the Dirac spectrum. In signal processing terms, this is the **DC (direct current) baseline** of the spectral density -- the constant, frequency-independent component.

3. **Finite spectral action extraction** -- The zeta function approach provides a rigorous regularization of the spectral action, eliminating the cutoff ambiguity that plagued traditional NCSG approaches. This is essential for cleanly extracting the vacuum energy contribution.

4. **Gauge field emergence from algebra doubling** -- The doubled algebra structure in NCSG mirrors the BCS pairing (particle-hole doubling) in the phonon-exflation pairing gap. Gauge fields emerge as collective modes, analogous to how phonons emerge from particle excitations.

5. **Dissipation and vacuum dynamics** -- The dissipative interpretation of the doubled algebra aligns with the framework's emphasis on non-equilibrium dynamics. The vacuum is not a static state but a dissipative, evolving medium.

6. **Higgs vacuum expectation value as internal compactification scale** -- The Higgs VEV adjusts the metric coupling in conformal coordinates, directly controlling the internal compactification radius R_K of the Kaluza-Klein fiber. This is measurable as the phonon gap scale.

This paper provides the mathematical language for discussing the phonon-exflation vacuum as a spectral manifold in which particles and cosmology both emerge from eigenvalue spectra of geometric operators.

