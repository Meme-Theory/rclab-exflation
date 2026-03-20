# Quasiclassical Method in the Theory of Superconductivity

**Author(s):** A.I. Larkin and Y.N. Ovchinnikov
**Year:** 1969
**Journal:** Soviet Physics JETP, Vol. 28, p. 1200

---

## Abstract

Larkin and Ovchinnikov introduced the out-of-time-ordered correlator (OTOC) in the context of quasiclassical perturbation theory for disordered superconductors. They studied how quasiparticle trajectories in momentum space become unstable under small perturbations due to impurity scattering. The formalism relates the growth of perturbations to a four-point correlation function of electron operators at different times:

```
Delta f ~ <[W(t), V(0)]^2>
```

This measures how an initial momentum-space displacement grows under the classical equations of motion perturbed by quantum disorder. The analysis was quantitative for weak-disorder systems, establishing that quasiclassical trajectories have exponential instability timescales set by the disorder strength. This pioneering work laid the foundation for modern OTOC studies, though its significance was not widely recognized until 2016 when Maldacena, Shenker, and Stanford revived the OTOC formalism in the context of black holes and quantum chaos.

---

## Historical Context

In 1969, the field of superconductivity was dominated by the BCS theory (1957) and its extensions to impure systems. Larkin and Ovchinnikov were studying a concrete problem: how does impurity scattering affect the energy spectrum of Bogoliubov quasiparticles in superconductors?

Their innovation was to connect classical instability of trajectories (familiar from classical chaos) to quantum correlation functions. This was ahead of its time---the field of quantum chaos did not really exist as a discipline in 1969. The OTOC formalism they introduced was highly technical and confined to a specialist audience.

It took until the 2010s, when Maldacena and others discovered that OTOCs provide the key diagnostic of quantum chaos in strongly-coupled systems, that Larkin-Ovchinnikov's work was recognized as foundational.

---

## Key Arguments and Derivations

### Quasiclassical Equations of Motion

In a disordered superconductor, the quasiparticle state is described by the Bogoliubov de Gennes equations:

```
i*hbar*d/dt |psi_k(t)> = H_eff |psi_k(t)>
```

where H_eff includes kinetic energy + impurity potential + pairing gap Delta:

```
H_eff = epsilon_k + V_impurity(x,y,z) - Delta(x,y,z) (with spin structure)
```

In the quasiclassical limit (weak scattering, energies near the gap), this can be approximated by a phase-space trajectory in momentum space:

```
dk/dt = F(k)   (where F encodes the impurity force)
```

### Stability Analysis and Perturbation Growth

Consider a trajectory k(t) in momentum space. A small perturbation delta k(t) evolves according to:

```
d(delta k)/dt = (dF/dk) delta k + perturbation_noise
```

In the presence of random impurity scattering, the perturbation grows or decays depending on the Lyapunov exponent of the classical trajectory. Larkin and Ovchinnikov computed this growth by evaluating:

```
<(delta k(t))^2> = <[W(t), V(0)]^2>
```

where W, V are momentum-space operators and the average is over impurity configurations.

### OTOC in Superconductor Context

The four-point correlator they considered was:

```
F(t) = Tr[ rho_beta/2 V(t) W(0) V(t) W(0)^dagger ]
```

with V(t) and W(t) being creation/annihilation operators for quasiparticles.

In the weak-disorder limit, this grows as:

```
F(t) ~ exp(2*Gamma_imp*t)
```

where Gamma_imp is the impurity scattering rate (inverse elastic mean free path / hbar).

For intermediate disorder:

```
F(t) ~ exp(lambda_L*t)   where lambda_L ~ sqrt(J_impurity)
```

### Connection to Classical Chaos

Larkin and Ovchinnikov noted that their result parallels classical chaos in Hamiltonian systems, where nearby trajectories diverge exponentially:

```
|delta x(t)| ~ |delta x(0)| * exp(lambda_Lyapunov*t)
```

In their quantum system, the "trajectories" are quasiparticle paths in momentum space, and the "chaos" comes from random impurity scattering. The rate of divergence is the classical Lyapunov exponent, but now computed quantum-mechanically via the OTOC.

### Connection to Superconductivity

The practical relevance to superconductivity was in understanding disorder effects on:

1. **Elastic scattering rate**: Gamma_1 ~ pi*N_imp*V^2 (Born approximation)
2. **Inelastic scattering rate** (quasiparticle-quasiparticle interactions): Gamma_2 ~ N_imp * (typical energy scale)^2
3. **Gapless excitations in dirty superconductors**: The Larkin-Ovchinnikov mechanism of instability was relevant to Anderson's theorem on gap robustness

---

## Key Results

1. **Introduction of OTOC**: The four-point correlator [W(t), V(0)]^2 was formalized as the quantum-mechanical measure of trajectory instability in disordered systems.

2. **Exponential Instability**: Quasiparticle trajectories grow perturbations exponentially with a rate set by the impurity strength: lambda_L ~ Gamma_imp or sqrt(J_imp).

3. **Disorder-Induced Chaos**: Random disorder acts as a source of classical-like chaos in quantum systems, a phenomenon later generalized to many-body systems.

4. **Quantitative Predictions**: For weakly disordered superconductors, the instability timescale is ~ hbar/Gamma_imp ~ 10 fs for realistic disorder, making it a genuine effect.

5. **Connection to Transport**: The trajectory instability relates to conductivity and lifetime broadening in the superconducting spectrum.

---

## Impact and Legacy

Though initially confined to superconductor physics, Larkin-Ovchinnikov's OTOC formalism became central to:

- **Quantum Chaos Theory** (2010s onwards): Rediscovery in the context of black holes and many-body chaos
- **Out-of-Equilibrium Dynamics**: The framework extended to study how perturbations spread in isolated quantum systems
- **Experimental Quantum Systems**: Trapped ion systems, superconducting qubits, and ultra-cold atoms now routinely measure OTOCs

---

## Connection to Phonon-Exflation Framework

The **Larkin-Ovchinnikov mechanism of disorder-induced trajectory instability** is directly relevant to the dense instanton ensemble in the internal SU(3) space.

In the framework, the instanton gas has:
- S_inst = 0.069 (extensive entropy from disorder in instanton positions)
- BCS-BEC crossover regime (E_vac/E_cond = 28.8, near unitarity)
- Pair vibrations with ω = 0.792 au^{-1} (characteristic instability timescale)

**Interpretation**: The instantons constitute a "disordered fermion system" in pair-addition Fock space, analogous to a dirty superconductor. Their OTOC growth via Larkin-Ovchinnikov mechanism:

```
lambda_L,inst ~ sqrt(J_inst)  where J_inst ~ disorder strength in instanton tunneling matrix elements
```

**Test for S38**: If lambda_L,inst ~ 0.8 au^{-1} (matching the pair-vibration frequency), then the instanton ensemble exhibits Larkin-Ovchinnikov-type chaos, and the fold transit is **disorder-driven chaos** in the internal space.

This connects the modern quantum chaos (SYK) perspective back to the 1969 superconductor origin of OTOC theory, completing a 45-year circle.
