# Unscrambling the Physics of Out-of-Time-Order Correlators

**Author(s):** Brian Swingle
**Year:** 2018
**Journal:** Nature Physics, Vol. 14, p. 988
**arXiv:** 1810.07961

---

## Abstract

Brian Swingle provides a comprehensive perspective article on out-of-time-ordered correlators (OTOCs) and their physical meaning. Rather than focusing on a single model or calculation, Swingle unifies diverse applications of OTOCs: from black hole information dynamics and quantum information scrambling, to thermalization in many-body systems, to experimental measurements in trapped ions and superconducting qubits. The perspective clarifies that OTOCs measure "how much" information initially localized in one subsystem spreads throughout the whole system. He explains the connection between OTOCs and operator growth, showing that exponential growth of F(t) ~ exp(lambda_L*t) indicates that operators initially simple become exponentially complex (in the sense of spreading their support across more and more Fock-space basis elements). The review synthesizes results from quantum chaos, condensed matter physics, and quantum gravity into a unified framework.

---

## Historical Context

By 2018, the field of quantum information scrambling was rapidly expanding. Maldacena, Shenker, and Stanford (2016) had established the chaos bound. Kitaev and Suh (2018) had introduced the scramblon. Yet there was still no clear pedagogical explanation of what OTOCs actually measure in physical terms.

Swingle's Nature Physics perspective filled this gap by:

1. **Operationalizing Scrambling**: Explaining how and why OTOCs measure information spread
2. **Connecting to Familiar Physics**: Showing that scrambling occurs in systems ranging from black holes to magnets to quantum spin models
3. **Bridging Theory and Experiment**: Clarifying what measurements in quantum simulators would reveal about information dynamics

The article became the canonical reference for experimental groups designing OTOC measurements.

---

## Key Arguments and Derivations

### Defining Scrambling and Information Spread

Swingle begins with a simple operational definition: Suppose you create a localized quantum state on subsystem A of a bipartite system A+B:

```
|psi_A> = |excited_state> ⊗ |0_B>
```

The question: **After the system evolves, is this excitation still concentrated in A, or has it spread to B?**

The OTOC quantifies this by inserting a unitary operator U(t) that represents time evolution:

```
F(t) = Tr[rho_A ⊗ rho_B * [W(t), V(0)]^2] / normalization
```

where V(0) acts on A (the initial excitation) and W(t) acts on B (a probe operator).

If F(t) decays as ~ exp(-lambda_L*t), it means the commutator [W(t), V(0)] is growing, indicating that the support of V has spread from A to B.

### Connection to Out-of-Equilibrium Dynamics

In a closed quantum system initialized in state rho(0), the OTOC evolves under Hamiltonian dynamics:

```
F(t) = Tr[rho(0) U^dag(t) W^dag U(t) V^dag(0) U^dag(t) W U(t) V(0)]
```

(up to normalization). The structure [W(t), V(0)] indicates that we are asking: **"How much do the observables interfere?"**

At early times (t << 1/lambda_L):

```
F(t) ~ 1 - C*t^2  (quadratic early-time decay, typical of short-range interactions)
```

At late times (t >> 1/lambda_L):

```
F(t) ~ decay_rate(system_size)  (approaches system-size-dependent floor)
```

### Operator Complexity and Weight Spreading

Swingle explains that OTOC growth is intimately related to **operator complexity**: how "complicated" an operator becomes under Hamiltonian evolution.

Define the weight of an operator in basis elements:

```
A(t) = sum_i c_i(t) sigma_i(t)
```

where sigma_i are Pauli strings. At t=0, V has weight on ~ 1 Pauli string. At late times, V(t) has weight spread over ~ exp(lambda_L*t) Pauli strings in the SYK model.

The OTOC measures the **total number of Pauli-string terms** to which V has spread:

```
sum_i |c_i(t)| ~ 1 / F(t)
```

### SYK Model as Exemplar

In the SYK model, Swingle emphasizes that scrambling saturates the MSS bound because:

```
lambda_L = 2*pi*T  (maximal)
```

This means operators grow in complexity as:

```
N_terms ~ exp(2*pi*T*t)
```

reaching the maximum allowed by quantum information theory.

### Four-Point Function Structure

Swingle clarifies the interpretation of the four-point function. Define:

```
G_4(t1,t2,t3,t4) = Tr[rho * O_1(t1) O_2(t2) O_3(t3) O_4(t4)]
```

Different time-orderings give different physics:

- **Standard ordering** (t1>t2>t3>t4): Regular response function, measures linear response
- **Out-of-time ordering** (t1>t3>t2>t4): Measures scrambling and chaos

The distinction is crucial for interpreting experimental measurements.

### Thermalization and Scrambling

Swingle connects scrambling to thermalization. A system thermalizes when:

1. **Local observables approach thermal values** (equilibration)
2. **Global information spreads** (scrambling)

A system can equilibrate without scrambling (if integrable), and can scramble without equilibrating (if there are conserved charges). But typically, in chaotic systems, the two go hand-in-hand.

The OTOC provides a measure of **global information spreading**, distinct from and complementary to local thermalization.

---

## Key Results

1. **OTOC = Information Spread Measure**: The OTOC quantifies how much information initially local to subsystem A has spread to subsystem B.

2. **Exponential Growth = Operator Complexity Growth**: F(t) ~ exp(-lambda_L*t) implies V(0) grows in complexity as ~ exp(lambda_L*t) basis elements.

3. **Scrambling ≠ Thermalization**: Global scrambling and local thermalization are related but distinct. A system can have one without the other.

4. **MSS Bound Universality**: The bound lambda_L <= 2*pi*T is universal and applies to systems ranging from black holes to magnets.

5. **Experimental Accessibility**: OTOCs can be measured in trapped ions, superconducting qubits, and other quantum simulators via pulse sequences.

6. **SYK Examplearity**: The SYK model saturates the bound and serves as the canonical example of a maximally scrambling system.

---

## Impact and Legacy

Swingle's perspective transformed OTOC from an abstract theoretical construct to a tool for experimental investigation:

- **Experimental Blueprints**: His explanation of how to measure OTOCs in quantum systems guided the Google Willow team and others.
- **Condensed Matter Applications**: Motivated searches for scrambling in magnets, superconductors, and ultracold atoms.
- **Pedagogical Foundation**: Became the standard reference for explaining scrambling to newcomers.

---

## Connection to Phonon-Exflation Framework

Swingle's **information-spread interpretation of OTOCs** directly illuminates the instanton transit problem in the Ainulindale framework.

In the fold-crossing scenario:
- Initial state: pair condensate with definite Cooper pair wavefunction, localized in pair-addition space
- Perturbation: van Hove singularity (soft mode at the fold)
- Probe: pair-vibration excitation (85.5% of spectral strength)

The OTOC:

```
F(t) = <[pair-vibration(t), pair-condensate(0)]^2>
```

measures **how much the condensate information spreads** during van Hove crossing. If F(t) ~ exp(lambda_L*t):

1. The condensate order parameter becomes exponentially complex in Fock space
2. Information about the initial condensate wavefunction becomes inaccessible at short times
3. The fold crossing is a **scrambling event** in pair-addition space

**New prediction for S38**: Measure F(t) directly in the MC simulation of the instanton gas during fold transit. If lambda_L ~ 0.79 au^{-1} (pair-vibration frequency), the fold crossing exhibits **Swingle-type information scrambling**, transforming the framework from "equilibrium spectral action" to "far-from-equilibrium chaos and decoherence."
