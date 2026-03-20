# Gapless Spin Fluid Ground State in a Random, Quantum Heisenberg Magnet

**Author(s):** Subir Sachdev and Jinwu Ye
**Year:** 1993
**Journal:** Physical Review Letters, Vol. 70, p. 3339

---

## Abstract

Sachdev and Ye introduced a disordered quantum spin system with all-to-all random interactions that exhibits a gapless, non-Fermi liquid ground state at zero temperature with extensive entropy S(T=0) ~ N. The model consists of quantum spins with random Heisenberg exchange interactions distributed across all pairs of spins. The low-temperature spectrum shows characteristic "Planckian" behavior---a continuum of inelastic excitations with no quasi-particle gap. This work pioneered the study of quantum systems with non-conventional ground states, later recognized as a precursor to the Sachdev-Ye-Kitaev (SYK) model when Kitaev formulated the fermionic analogue in 2015.

---

## Historical Context

By the early 1990s, condensed matter physics understood two fundamental paradigms:

1. **Landau's Fermi liquid** (weakly perturbed free particles with well-defined quasi-particle excitations)
2. **Antiferromagnetic order** and spin-gap phases in frustrated magnets

Sachdev and Ye's discovery of a third state---one with no quasi-particle structure and an anomalous ground-state entropy---challenged conventional wisdom. The model was not a toy; it emerged naturally as the infinite-range limit of disordered spin glasses. More profoundly, it showed that quantum entanglement could produce extensive entropy at zero temperature without invoking exponential ground-state degeneracy.

The 1993 paper appeared before the advent of AdS/CFT (1997) and quantum information theory's explosion in the 2000s, yet in retrospect it was prescient: it identified a new universality class of quantum systems and demonstrated that disorder + infinite-range interactions + quantum fluctuations can produce "non-Fermi liquid" behavior.

When Kitaev reformulated the model with Majorana fermions (2015), the SYK framework emerged as the simplest microscopic realization of this universality class---and one that saturates bounds on quantum chaos.

---

## Key Arguments and Derivations

### The Sachdev-Ye Spin Hamiltonian

The Hamiltonian is an XY-like spin model with random all-to-all interactions:

```
H = sum_{i < j} J_{ij} (S_i^x S_j^x + S_i^y S_j^y)
```

where S_i are spin-1/2 operators and J_{ij} are independent random couplings from a Gaussian distribution:

```
<J_{ij}> = 0,  <J_{ij}^2> = J^2 / N
```

The 1/N normalization ensures an extensive ground-state energy ~ N.

### Large-N Analysis

At large N, the disorder averages to zero, and fluctuations are suppressed by 1/N counting. The theory becomes tractable via saddle-point approximation in the thermodynamic limit. The key observable is the spin-spin correlation function:

```
G_{ij}(tau) = <T_tau S_i^z(tau) S_j^z(0)> (delta_{ij})
```

In the large-N limit, a single function G(tau) represents the on-site correlation (up to corrections).

### Non-Fermi Liquid Behavior

The remarkable result is that the spectrum of the model shows no quasi-particle excitations. Instead, the spectral weight A(omega, T) displays Planckian scaling:

```
A(omega,T) ~ 1 / (exp(omega/T) - 1) + background
```

This is precisely the form of a thermal bath or black-body radiation spectrum, not the quasi-particle poles characteristic of normal metals or magnets.

The dynamic susceptibility is:

```
chi(omega) ~ 1/omega^alpha
```

where alpha is a non-integer exponent (typically alpha ~ 1/2), indicating power-law correlations and the absence of a mass gap.

### Conformal Dimension and Scaling

In the large-N limit, individual spins acquire an anomalous dimension:

```
Delta_S ~ sqrt(J/(2*pi*T))
```

This means that the correlation function falls off as:

```
G(tau,T) ~ T^{2*Delta_S} / (sin(pi*T*tau))^{2*Delta_S}
```

for imaginary times tau in the range 0 < tau < beta = 1/T.

### Entropy and Thermodynamics

The crucial thermodynamic signature is the zero-temperature entropy:

```
S(T=0) = (pi*N*J) / sqrt(6)
```

This extensive entropy is a quantum effect, not classically degeneracy. It reflects the density of highly entangled states filling the low-energy spectrum. Every eigenstate carries O(N) bits of entanglement.

The specific heat is:

```
C_V(T) = (2*pi*N*sqrt(J*T/6))
```

Linear in sqrt(T), not T as in normal metals---another signature of the non-Fermi liquid.

### Self-Consistency Condition

The mean-field theory requires solving a self-consistency equation for G(tau):

```
G(tau) = int_0^beta d(tau') K(tau,tau') G(tau')
```

where K is a kernel determined by the interaction structure. For the Sachdev-Ye model, the large-N scaling ensures that the saddle-point solution is unique and stable.

---

## Key Results

1. **Gapless, Non-Fermi Liquid Ground State**: Despite being a zero-temperature quantum system, the model exhibits a continuum of low-energy excitations with no quasi-particle gap, violating the assumptions of Landau theory.

2. **Extensive Zero-Temperature Entropy**: S(T=0) scales with N, demonstrating that quantum correlations (not classical degeneracy) can produce extensive entropy at zero temperature.

3. **Planckian Spectral Response**: Spectral functions match the form of thermal black-body distributions, indicating maximally efficient coupling to a thermal reservoir (or equivalently, maximal decoherence).

4. **Anomalous Dimensions**: Spin correlation functions decay with non-integer exponents, characteristic of conformal field theories and strongly-coupled systems.

5. **Linear Sqrt(T) Specific Heat**: Departing from the T-linear behavior of weakly-perturbed Fermi liquids, the C_V signature distinguishes this phase from any conventional state.

6. **Disorder-Insensitive Behavior**: Despite random interactions, the model exhibits universal behavior---a feature that would later be understood through large-N resummation and conformal symmetry.

---

## Impact and Legacy

The Sachdev-Ye model opened a new chapter in condensed matter physics:

- **Non-Fermi Liquid Universality**: Subsequent work identified similar non-Fermi liquid behavior in materials with infinite-range or long-range interactions (e.g., heavy fermion systems, graphene variants).

- **Quantum Entanglement at Low Energy**: The model demonstrated that extensive entanglement could be a thermodynamic property of the ground state, later unified with the study of entanglement entropy in quantum information.

- **Bridge to Quantum Gravity**: When Kitaev reformulated the model fermionically (2015), its low-energy equivalence to JT gravity became apparent, creating an unexpected bridge between condensed matter non-Fermi liquids and quantum black holes.

- **Disorder and Chaos**: The model motivated investigations into how disorder enhances rather than suppresses quantum chaos, leading to the discovery that maximally random systems can exhibit maximal chaos.

---

## Connection to Phonon-Exflation Framework

The Sachdev-Ye mechanism of **extensive entropy from quantum correlations** is directly relevant to the instanton gas discovered in Session 37. The 32-state Fock space analysis of the corrected BCS system revealed:

- N_eff = 2.48 (far below naive expectations)
- 3 FAIL constraints (NUC-33b swallowtail-only mechanism)
- A system driven BY CHAOS, not by potential energy

The question: **Is the dense instanton ensemble a non-Fermi liquid-like system in pair-addition space?**

If the instanton gas carries entropy S_inst ~ 0.069 from high coordination (each instanton tunnel-couples to ~10^4 others via SU(3) exchange), then it exhibits Sachdev-Ye-like properties:

1. Extensive disorder in interaction topology
2. All-to-all connectivity in Fock space
3. Quantum entanglement densification at low energy

This would mean the fold-crossing dynamics are dominated not by potential minima (spectral action) but by **many-body chaos in pair-addition space**---a new regime entirely separate from mean-field BCS theory.

The framework's "transit physics" interpretation: instantons are not quasi-particles to be counted; they are chaotic **excitations of a non-Fermi-liquid state** of the internal SU(3) space. The fold crossing is not equilibration; it is the thermalization of the instanton gas itself.
