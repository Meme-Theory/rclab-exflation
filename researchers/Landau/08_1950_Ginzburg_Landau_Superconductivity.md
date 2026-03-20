# On the Theory of Superconductivity

**Authors:** Vitaly Lazarevich Ginzburg, Lev Davidovich Landau
**Year:** 1950
**Journal:** Zh. Eksp. Teor. Fiz., 20, 1064-1082
**English translation:** in "Collected Papers of L.D. Landau," ed. D. ter Haar (1965)

---

## 1. Historical Context

### 1.1 The State of Superconductivity Theory in 1950

By 1950, superconductivity had been known for 39 years (Onnes, 1911) but lacked
a microscopic theory. The known phenomenology included:

- **Zero resistance** below a critical temperature T_c (material-dependent)
- **Meissner effect** (1933): expulsion of magnetic flux from the interior
- **London equations** (1935): phenomenological electrodynamics with a
  penetration depth lambda_L
- **Critical magnetic field** H_c(T) with parabolic temperature dependence

The London theory described the electromagnetic response but said nothing about
the thermodynamic phase transition, the order parameter, or the spatial
variation of superconducting properties near boundaries and interfaces.

Ginzburg and Landau recognized that superconductivity could be cast in Landau's
general framework for second-order phase transitions (1937), with the order
parameter being a complex scalar field psi(r) -- the "effective wavefunction
of the superconducting electrons."

---

## 2. The Ginzburg-Landau Free Energy

### 2.1 The Functional

The GL free energy density is:

    f_s = f_n + alpha * |psi|^2 + (beta/2) * |psi|^4
          + (1/(2*m*)) * |(-i*hbar*nabla - (e*/c)*A) * psi|^2
          + |B|^2 / (8*pi)

The total free energy F[psi, A] = integral f_s d^3r, where psi(r) is the
complex order parameter, A(r) the magnetic vector potential with B = curl(A),
and alpha, beta, m*, e* are phenomenological coefficients.

### 2.2 The Order Parameter

Physical interpretation:

    |psi(r)|^2 = n_s(r) = local superfluid (superconducting) density
    psi(r) = sqrt(n_s(r)) * exp(i * phi(r))

The phase phi(r) determines the gauge-invariant superfluid velocity:

    v_s = (hbar / m*) * (nabla(phi) - (e*/(hbar*c)) * A)

### 2.3 Temperature Dependence

Near T_c:

    alpha(T) = alpha_0 * (T - T_c) / T_c,   beta(T) = beta_0 (constant)

For T < T_c (alpha < 0), the equilibrium order parameter is:

    |psi_0|^2 = -alpha / beta = n_s(T)

The condensation energy: f_n - f_s = alpha^2 / (2*beta) = H_c^2 / (8*pi).

---

## 3. The Two Characteristic Lengths

### 3.1 Coherence Length xi

The **coherence length** measures the scale of order parameter variations:

    xi(T) = hbar / sqrt(2 * m* * |alpha(T)|)

Near T_c: xi(T) = xi(0) / sqrt(1 - T/T_c) (diverges at T_c). It sets the
vortex core size, domain wall thickness, and the minimum scale of spatial
variation. For clean superconductors: xi(0) ~ 1000 A.

### 3.2 Penetration Depth lambda

The **magnetic penetration depth** measures field decay into the bulk:

    lambda(T) = sqrt(m* * c^2 * beta / (4*pi * e*^2 * |alpha(T)|))

Near T_c: lambda(T) = lambda(0) / sqrt(1 - T/T_c) (diverges). The Meissner
effect is B(x) ~ exp(-x/lambda). For elemental superconductors: lambda(0) ~ 200-500 A.

### 3.3 The GL Parameter kappa

The ratio kappa = lambda / xi is temperature-independent near T_c and
determines the superconductor type:

    kappa < 1/sqrt(2):  Type I  (positive surface energy)
    kappa = 1/sqrt(2):  Bogomolnyi point (zero surface energy)
    kappa > 1/sqrt(2):  Type II (negative surface energy)

Elemental superconductors (Sn, In, Al, Pb): Type I.
Alloys and compounds (NbTi, Nb3Sn, YBCO): Type II.

---

## 4. The Ginzburg-Landau Equations

### 4.1 Variational Derivation

Extremizing F[psi, A] with respect to psi* and A gives:

**First GL equation** (delta F / delta psi* = 0):

    alpha * psi + beta * |psi|^2 * psi + (1/(2*m*)) * (-i*hbar*nabla - (e*/c)*A)^2 * psi = 0

This is a nonlinear Schrodinger equation for the order parameter.

**Second GL equation** (delta F / delta A = 0):

    j = (e*/(2*m*)) * [psi* * (-i*hbar*nabla - (e*/c)*A) * psi + c.c.]

This gives the supercurrent density in terms of psi and A.

### 4.2 Gauge Invariance

The GL equations are invariant under:

    psi -> psi * exp(i * e* * chi / (hbar * c)),    A -> A + nabla(chi)

This local U(1) gauge symmetry is spontaneously broken by <psi> != 0. This was
one of the first examples of what would later be called spontaneous symmetry
breaking and the Higgs mechanism.

---

## 5. Surface Energy and the Type I/II Classification

### 5.1 The N-S Interface

At a planar normal-superconducting interface with applied field H = H_c, the
order parameter psi(x) rises from 0 to psi_0 over distance ~xi, while B(x)
decays from H_c to 0 over distance ~lambda.

### 5.2 Type I (kappa < 1/sqrt(2))

When xi > lambda*sqrt(2), psi rises slowly while B decays quickly. The surface
energy is POSITIVE. The superconductor minimizes interfaces -- complete Meissner
effect up to H_c, then a first-order transition to normal.

### 5.3 Type II (kappa > 1/sqrt(2))

When lambda > xi/sqrt(2), B penetrates further than psi is suppressed. The
surface energy is NEGATIVE. The superconductor creates interfaces spontaneously
-- partial flux penetration via quantized vortices (Abrikosov, 1957).

### 5.4 The Bogomolnyi Point

At kappa = 1/sqrt(2), the GL equations reduce to first-order equations with
zero vortex-vortex interaction. This mathematical structure reappears in gauge
field theory (BPS monopoles, instantons) and string theory.

---

## 6. Critical Fields and Abrikosov Vortices

### 6.1 Upper Critical Field H_{c2}

Near H_{c2}, |psi| is small and the GL equation linearizes to the Schrodinger
equation for Landau levels. The lowest level gives:

    H_{c2} = Phi_0 / (2 * pi * xi^2)

where Phi_0 = h*c/e* is the flux quantum. For strong Type II, H_{c2} >> H_c.

### 6.2 Lower Critical Field and Mixed State

    H_{c1} = (Phi_0 / (4*pi*lambda^2)) * (ln(kappa) + 0.50)

The three regimes:
- H < H_{c1}: complete Meissner effect
- H_{c1} < H < H_{c2}: Abrikosov vortex lattice (mixed state)
- H > H_{c2}: normal state

### 6.3 Abrikosov Vortex Lattice (1957)

Abrikosov showed that the mixed state consists of a triangular array of
quantized vortices, each carrying flux quantum Phi_0, with core size ~xi,
flux tube diameter ~lambda, and phase winding 2*pi per vortex. Abrikosov
shared the 2003 Nobel Prize with Ginzburg and Leggett for this work.

---

## 7. Microscopic Justification and Topological Structure

### 7.1 Gor'kov's BCS Derivation (1959)

Gor'kov showed the GL equations derive from BCS theory near T_c, with:

    psi(r) ~ Delta(r) (BCS gap),  e* = 2*e,  m* = 2*m_e (Cooper pair)

The GL coefficients in terms of BCS parameters:

    alpha = N(0) * (T - T_c) / T_c
    beta = 7 * zeta(3) * N(0) / (48 * pi^2 * (k_B * T_c)^2)

GL works near T_c because: (1) the order parameter is small (Taylor expansion
valid), (2) spatial variations are slow (gradient expansion valid), and (3) the
theory is universal -- depending on symmetry, not microscopic details.

### 7.2 Quantized Magnetic Flux

The single-valuedness of psi = |psi| * exp(i*phi) requires:

    oint_C nabla(phi) . dl = 2 * pi * n    (n = integer)

For a loop deep in the superconductor (v_s = 0):

    Phi = n * Phi_0,    Phi_0 = h / (2*e) = 2.07 x 10^{-7} G*cm^2

The factor of 2 in e* = 2e confirmed BCS pairing (Deaver & Fairbank 1961).

### 7.3 The Higgs Mechanism

GL theory provides the simplest physical realization of what became the Higgs
mechanism (Anderson 1963, Higgs 1964):

1. U(1) gauge symmetry is spontaneously broken by <psi> != 0
2. The phase mode (would-be Goldstone) is "eaten" by the gauge field
3. The gauge field acquires mass: m_photon = hbar / (lambda * c)
4. The amplitude mode has mass: m_Higgs = hbar / (xi * c)

The Meissner effect IS the photon acquiring mass inside the superconductor.
The electroweak Higgs mechanism is mathematically identical in structure.

---

## 8. Connection to Phonon-Exflation Cosmology

### 8.1 The GL Functional IS the GPE Energy

The Ginzburg-Landau free energy (dropping gauge field):

    F = integral [alpha*|psi|^2 + (beta/2)*|psi|^4 + (hbar^2/(2*m*))*|nabla psi|^2] d^3r

is identical to the Gross-Pitaevskii energy:

    E = integral [(hbar^2/(2*m))*|nabla Psi|^2 + V_ext*|Psi|^2 + (g/2)*|Psi|^4] d^3r

with alpha <-> V_ext, beta <-> g, m* <-> m, psi <-> Psi. The GPE simulation
in `phonon-exflation-sim/` solves exactly this class of equation.

### 8.2 Order Parameter as Vacuum Wavefunction

In phonon-exflation:
- The BEC wavefunction Psi(x, t) plays the role of the GL order parameter
- The vacuum is the "superconducting" state (|Psi| != 0)
- Particle excitations are fluctuations of the order parameter
- The healing length xi = hbar/sqrt(2*m*g*n_0) maps to the compactification
  scale l_K of K = SU(3)

### 8.3 Penetration Depth and Gauge Boson Mass

The penetration depth lambda^{-1} <-> m_gauge * c / hbar. The Meissner effect
(exponential decay of B) corresponds to the finite range of the weak force
(exponential decay of the W/Z potential). If the GPE were extended to include
gauge coupling, the W/Z mass would emerge from the healing length and coupling.

### 8.4 The GL Parameter and the Electroweak Scale

In particle physics, the analog of kappa is:

    kappa_EW = m_W / m_H ~ 80.4 / 125 ~ 0.64

This is close to 1/sqrt(2) ~ 0.707 -- the Bogomolnyi point. Whether this
near-coincidence has physical significance in phonon-exflation (where both
scales emerge from the condensate) is an open question.

### 8.5 Vortices and Topological Defects

| GL/Superconductor | Phonon-Exflation |
|:-------------------|:-----------------|
| Quantized vortex (pi_1) | Cosmic string |
| Flux quantum Phi_0 | Quantized gauge flux |
| Vortex core (size xi) | String core (size l_K) |
| Abrikosov lattice | Cosmic string network |
| Vortex nucleation at H_{c1} | Defect production at phase transition |
| Core energy ~ n^2 | Topological charge additivity |

The GPE simulation directly produces quantized vortices (detected by
vortex_detection.py), and their statistics during simulated expansion provide
predictions for cosmic string abundance.

### 8.6 Type I vs Type II and the Vacuum

The Type I/II distinction maps to cosmology:
- Type I (kappa < 1/sqrt(2)): vacuum with no stable topological defects
- Type II (kappa > 1/sqrt(2)): vacuum where cosmic strings are stable

The electroweak sector's proximity to kappa ~ 1/sqrt(2) would place our vacuum
near the Type I/II boundary -- potentially a deep structural feature.

---

## 9. Summary

The Ginzburg-Landau theory established:

1. The complex order parameter psi(r) for the superconducting state
2. The GL free energy functional with |psi|^2, |psi|^4, and gauge-covariant
   gradient terms
3. Two characteristic lengths: coherence length xi and penetration depth lambda
4. The GL parameter kappa = lambda/xi classifying Type I vs Type II
5. The GL equations as variational equations of the free energy
6. The surface energy sign change at kappa = 1/sqrt(2)
7. The upper critical field H_{c2} = Phi_0 / (2*pi*xi^2)
8. Quantized magnetic flux Phi_0 = h/(2e)

For phonon-exflation cosmology, the GL theory provides the most direct
mathematical bridge: the GL functional IS the GPE energy functional, the
order parameter IS the condensate wavefunction, and the Higgs mechanism IS
the Meissner effect. Every feature of GL theory (coherence length, penetration
depth, vortices, topological classification) has a cosmological counterpart.

---

## References

- V.L. Ginzburg, L.D. Landau, "On the Theory of Superconductivity," Zh. Eksp. Teor. Fiz. 20, 1064 (1950)
- F. London, H. London, "The Electromagnetic Equations of the Supraconductor," Proc. Roy. Soc. A 149, 71 (1935)
- L.D. Landau, "On the Theory of Phase Transitions," Zh. Eksp. Teor. Fiz. 7, 19 (1937)
- A.A. Abrikosov, "On the Magnetic Properties of Superconductors of the Second Group," Sov. Phys. JETP 5, 1174 (1957)
- L.P. Gor'kov, "Microscopic Derivation of the Ginzburg-Landau Equations," Sov. Phys. JETP 9, 1364 (1959)
- J. Bardeen, L.N. Cooper, J.R. Schrieffer, "Theory of Superconductivity," Phys. Rev. 108, 1175 (1957)
- B.S. Deaver, W.M. Fairbank, "Experimental Evidence for Quantized Flux," Phys. Rev. Lett. 7, 43 (1961)
- P.W. Anderson, "Plasmons, Gauge Invariance, and Mass," Phys. Rev. 130, 439 (1963)
- P.W. Higgs, "Broken Symmetries and the Masses of Gauge Bosons," Phys. Rev. Lett. 13, 508 (1964)
