# Quantum Mechanical Computers

**Author:** Richard P. Feynman
**Year:** 1986
**Journal:** *Foundations of Physics*, 16(6), 507--531

---

## Abstract

Feynman develops a concrete theoretical framework for quantum mechanical computation, going beyond the motivational arguments of his 1982 paper to specify how a quantum computer could actually work. He constructs explicit models of reversible quantum gates, demonstrates that a universal set of quantum gates can implement any unitary transformation, analyzes the role of quantum parallelism in achieving computational speedup, discusses physical implementation considerations including error rates and decoherence, and addresses the fundamental question of whether quantum mechanics provides a genuine computational advantage over classical physics. The paper introduces several concepts that became central to the field: the decomposition of arbitrary unitary operations into elementary gates, the analysis of quantum error propagation, and the connection between quantum computation and the simulation of physical systems.

---

## Historical Context

### From Motivation to Mechanism

Feynman's 1982 paper had argued that quantum computers were needed to efficiently simulate quantum systems, but it did not specify how such a computer would work. In the interim, David Deutsch (1985) had formalized the concept of a quantum Turing machine and had shown that a quantum computer could solve certain problems (the Deutsch problem) with fewer queries than any classical computer. However, the practical architecture of a quantum computer remained largely unexplored.

### Reversible Classical Computing

The theoretical foundations of reversible classical computing had been laid by Bennett (1973), Fredkin and Toffoli (1982), and others. The Toffoli gate (a three-bit reversible gate) was known to be classically universal: any Boolean function can be computed reversibly using Toffoli gates plus ancilla bits. Feynman's paper extends these ideas to the quantum domain.

### The Computational Physics Community

By the mid-1980s, the computational physics community was grappling with the limitations of classical simulation for quantum systems. Quantum Monte Carlo methods worked for some systems but failed for fermions (sign problem) and for real-time dynamics. Feynman's proposal offered a fundamentally different approach.

---

## Key Arguments and Derivations

### 1. Quantum Bits and Quantum States

Feynman begins by defining the quantum bit (qubit) as a two-state quantum system:

$$|\psi\rangle = \alpha|0\rangle + \beta|1\rangle, \quad |\alpha|^2 + |\beta|^2 = 1$$

where $|0\rangle$ and $|1\rangle$ are the computational basis states and $\alpha, \beta \in \mathbb{C}$ are probability amplitudes. The key difference from a classical bit is that a qubit can be in a superposition of 0 and 1 simultaneously.

For $n$ qubits, the state space is $(\mathbb{C}^2)^{\otimes n} = \mathbb{C}^{2^n}$:

$$|\psi\rangle = \sum_{x \in \{0,1\}^n} c_x |x\rangle, \quad \sum_x |c_x|^2 = 1$$

This $2^n$-dimensional space is exponentially larger than the $n$-dimensional state space of $n$ classical bits. The extra capacity comes from entanglement: most states in the $2^n$-dimensional space are entangled (not separable into products of single-qubit states).

### 2. Quantum Gates

A quantum gate is a unitary transformation $U$ acting on one or more qubits. Feynman discusses several fundamental gates:

**Single-qubit gates:**

The NOT gate (Pauli X): $X|0\rangle = |1\rangle$, $X|1\rangle = |0\rangle$:

$$X = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$$

The Hadamard gate: $H|0\rangle = (|0\rangle + |1\rangle)/\sqrt{2}$, $H|1\rangle = (|0\rangle - |1\rangle)/\sqrt{2}$:

$$H = \frac{1}{\sqrt{2}}\begin{pmatrix} 1 & 1 \\ 1 & -1 \end{pmatrix}$$

The phase gate: $S|0\rangle = |0\rangle$, $S|1\rangle = i|1\rangle$:

$$S = \begin{pmatrix} 1 & 0 \\ 0 & i \end{pmatrix}$$

General single-qubit rotations:

$$R(\theta, \phi, \lambda) = \begin{pmatrix} \cos(\theta/2) & -e^{i\lambda}\sin(\theta/2) \\ e^{i\phi}\sin(\theta/2) & e^{i(\phi+\lambda)}\cos(\theta/2) \end{pmatrix}$$

**Two-qubit gates:**

The controlled-NOT (CNOT):

$$\text{CNOT} = |0\rangle\langle 0| \otimes I + |1\rangle\langle 1| \otimes X = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \end{pmatrix}$$

This gate flips the target qubit if and only if the control qubit is $|1\rangle$. It is the quantum analog of the classical XOR gate but is reversible.

The controlled-NOT creates entanglement:

$$\text{CNOT}(H|0\rangle \otimes |0\rangle) = \text{CNOT}\frac{|0\rangle + |1\rangle}{\sqrt{2}} \otimes |0\rangle = \frac{|00\rangle + |11\rangle}{\sqrt{2}}$$

This is a Bell state -- a maximally entangled two-qubit state.

### 3. Universality

Feynman argues that a finite set of gates can approximate any unitary transformation on $n$ qubits to arbitrary precision. The key result (later made precise by the Solovay-Kitaev theorem) is:

**Any unitary $U$ on $n$ qubits can be decomposed into a product of single-qubit gates and CNOT gates.**

The proof sketch:
1. Any $n$-qubit unitary can be decomposed into a product of two-level unitaries (unitaries that act non-trivially on only two basis states).
2. Each two-level unitary can be implemented using single-qubit rotations and CNOT gates.
3. The number of elementary gates required is at most $O(4^n)$ for a general $n$-qubit unitary, but for structured unitaries (like those arising from local Hamiltonians), the gate count is polynomial in $n$.

Feynman emphasizes that this universality is the quantum analog of the classical universality of the NAND gate (or the Toffoli gate for reversible computation).

### 4. Quantum Parallelism

The central computational advantage of quantum computers comes from quantum parallelism. Consider applying a function $f: \{0,1\}^n \to \{0,1\}$ to a superposition of all inputs:

$$U_f \left(\frac{1}{\sqrt{2^n}}\sum_{x=0}^{2^n - 1} |x\rangle \right)|0\rangle = \frac{1}{\sqrt{2^n}}\sum_{x=0}^{2^n - 1} |x\rangle|f(x)\rangle$$

A single application of $U_f$ computes $f$ on all $2^n$ inputs simultaneously. This is not immediately useful -- measuring the output gives a single random value of $f$ -- but combined with interference, it enables algorithms that extract global properties of $f$ (periodicity, symmetry, etc.) with exponentially fewer queries than classical algorithms.

Feynman illustrates this with the observation that a quantum computer can represent and manipulate $2^n$ amplitudes using only $n$ physical qubits and a polynomial number of gates. The exponential information content is encoded in the entanglement structure of the quantum state.

### 5. Hamiltonian Simulation Revisited

Feynman returns to his 1982 proposal for quantum simulation and makes it more concrete. To simulate a quantum system with Hamiltonian $H = \sum_{k=1}^m H_k$ (where each $H_k$ acts on a few qubits), the Trotter-Suzuki decomposition gives:

$$e^{-iHt} = \left(\prod_{k=1}^m e^{-iH_k t/r}\right)^r + O(t^2/r)$$

Each $e^{-iH_k \Delta t}$ is a local unitary gate acting on a few qubits, implementable with single-qubit rotations and CNOTs. The total number of gates is:

$$N_{\text{gates}} = O(m \cdot r) = O(m^2 t^2 / \epsilon)$$

for first-order Trotter with error $\epsilon$, or $O(m^{5/3}t^{5/3}/\epsilon^{1/3})$ for higher-order decompositions. This is polynomial in the system size $n$ (since $m = O(n)$ for local Hamiltonians), confirming that quantum simulation is efficient.

### 6. Physical Implementation Considerations

Feynman discusses the physical requirements for building a quantum computer:

**Isolation vs. control:** Qubits must be sufficiently isolated from the environment to maintain quantum coherence, yet controllable enough to perform gate operations. This tension is the central engineering challenge.

**Decoherence:** Interaction with the environment causes decoherence -- the loss of quantum coherence -- on a timescale $T_2$. The computation must be completed within this timescale, or error correction must be used to extend it.

**Error rates:** Feynman analyzes how errors propagate through a quantum circuit. If each gate has an error probability $\epsilon$, a circuit of depth $d$ has a total error probability of approximately $d\epsilon$ (for small $\epsilon$). For the computation to succeed, the number of gates times the error rate must be small: $d\epsilon \ll 1$.

**Reversibility and dissipation:** Since quantum gates are unitary (reversible), the computation itself dissipates no energy. Energy dissipation occurs only at measurement (where information is extracted) and due to decoherence (an imperfection, not a fundamental requirement). This connects to Landauer's principle: a quantum computer operating perfectly dissipates zero energy until the measurement step.

### 7. Quantum vs. Classical: The Computational Advantage

Feynman addresses the question: does quantum mechanics provide a genuine computational advantage, or can classical computers simulate quantum computers efficiently?

He argues that the advantage is genuine, based on the following logic:
1. Quantum systems (e.g., $n$ interacting spins) cannot be efficiently simulated by classical computers (exponential blowup of the Hilbert space).
2. Quantum computers can efficiently simulate quantum systems (Trotter decomposition, polynomial gate count).
3. Therefore, quantum computers can solve problems (quantum simulation) that are intractable for classical computers.

This does not prove that quantum computers can solve all problems faster than classical computers -- only that there exist problems (quantum simulation, and later, factoring) where quantum computers have an exponential advantage.

---

## Physical Interpretation

### Quantum Information as a Physical Resource

Feynman's paper establishes that quantum information -- the information encoded in the amplitudes and entanglement structure of a quantum state -- is a physical resource fundamentally different from classical information. A quantum state of $n$ qubits contains exponentially more information than $n$ classical bits, but this information is accessible only through carefully designed measurements (algorithms) that exploit interference.

### The Measurement Problem in Computation

The transition from quantum amplitudes to classical outcomes (measurement) is the bottleneck of quantum computation. The computer can represent $2^n$ amplitudes simultaneously, but measurement projects onto a single outcome. The art of quantum algorithm design is to arrange the amplitudes so that useful information is concentrated in a small number of measurement outcomes.

### Computation as a Physical Process

Feynman reinforces the message of his 1982 paper: computation is physics, and the limits of computation are set by the laws of physics. If we want to compute the properties of quantum systems, we need quantum hardware. Classical computation is not wrong -- it is merely a special case of quantum computation, restricted to the commutative (diagonal) sector of the full quantum state space.

---

## Impact and Legacy

### Quantum Error Correction

Feynman's analysis of error rates was prescient. The development of quantum error correction codes (Shor 1995, Steane 1996, Calderbank-Shor-Steane codes, surface codes) showed that arbitrarily long quantum computations can be performed reliably provided the physical error rate per gate is below a threshold (approximately $10^{-2}$ for surface codes). This is the quantum fault-tolerance threshold theorem.

### Gate Model Quantum Computing

The gate model introduced by Feynman (and formalized by Deutsch) became the standard model for quantum computation. The decomposition of algorithms into sequences of one- and two-qubit gates is the basis for all current quantum hardware platforms.

### Quantum Complexity Theory

The question "what problems can quantum computers solve efficiently?" spawned the field of quantum complexity theory. The class BQP (bounded-error quantum polynomial time) contains all problems solvable by a quantum computer in polynomial time with bounded error. The relationship between BQP and classical complexity classes (P, NP, PSPACE) remains an open problem, but it is believed that $\text{P} \subsetneq \text{BQP} \subseteq \text{PSPACE}$.

### Quantum Information Theory

Feynman's treatment of quantum bits as information-carrying entities contributed to the development of quantum information theory (Bennett, Schumacher, Nielsen, Chuang, Preskill, and many others), which studies the capacity of quantum channels, quantum entropy, quantum teleportation, quantum key distribution, and other information-theoretic tasks.

---

## Connections to Modern Physics

1. **NISQ era:** Current quantum computers (50-1000+ qubits, error rates $\sim 10^{-3}$) are in the "noisy intermediate-scale quantum" (NISQ) regime. They can perform quantum simulations of small systems (a few dozen qubits) but cannot yet reach the fault-tolerant regime for large-scale computation.

2. **Quantum advantage demonstrations:** Beyond Google's Sycamore (2019), experiments with photonic systems (Jiuzhang, 2020) and superconducting circuits have demonstrated quantum advantage for specific tasks, validating Feynman's core argument.

3. **Hamiltonian simulation algorithms:** Feynman's Trotter-based approach has been improved dramatically. Product formulas (higher-order Trotter-Suzuki), linear combination of unitaries (LCU), quantum signal processing, and qubitization achieve near-optimal simulation complexity: $O(\text{poly}(n) \cdot t \cdot \text{polylog}(1/\epsilon))$.

4. **Quantum chemistry and materials science:** Variational quantum eigensolver (VQE), quantum phase estimation (QPE), and tensor network methods on quantum hardware are being applied to electronic structure problems, catalyst design, and strongly correlated materials -- exactly the applications Feynman envisioned.

5. **Topological quantum computing:** The proposal to use topological states of matter (anyons) as qubits provides intrinsic protection against decoherence, addressing one of Feynman's central concerns. The non-Abelian anyons in certain fractional quantum Hall states or engineered topological superconductors could provide a hardware platform with naturally low error rates.

6. **Quantum-classical hybrid algorithms:** Modern approaches often use quantum processors for the quantum-hard parts of a computation and classical processors for optimization and post-processing. This hybrid architecture was implicit in Feynman's discussion of using quantum computers specifically for the problems where classical computers fail.
