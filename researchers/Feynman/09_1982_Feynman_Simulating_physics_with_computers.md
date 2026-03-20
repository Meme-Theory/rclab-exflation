# Simulating Physics with Computers

**Author:** Richard P. Feynman
**Year:** 1982
**Journal:** *International Journal of Theoretical Physics*, 21(6/7), 467--488 (based on a keynote address at the First Conference on Physics and Computation, MIT, May 1981)

---

## Abstract

Feynman addresses the fundamental question of whether classical computers can efficiently simulate quantum physical systems. He argues that the answer is no: the exponential growth of the quantum state space with the number of particles makes classical simulation of generic quantum systems exponentially expensive. A system of $n$ quantum bits requires $2^n$ complex amplitudes to describe its state, and the time evolution involves $2^n \times 2^n$ matrix operations. Feynman proposes that the solution is to build computers that are themselves quantum mechanical -- quantum computers -- which can simulate quantum systems with only polynomial overhead. He discusses the distinction between local and non-local hidden variable theories, the role of probability in quantum mechanics, and the connection to reversible computation. This paper is widely regarded as the foundational document for the field of quantum computing, providing the conceptual motivation that would later be realized in specific quantum algorithms and quantum hardware.

---

## Historical Context

### Classical Computation and the Church-Turing Thesis

By the early 1980s, the theory of classical computation was well-established. The Church-Turing thesis (1936) stated that any effectively computable function can be computed by a Turing machine. The extended Church-Turing thesis (a stronger, physical claim) asserted that any physically realizable computation can be efficiently simulated by a probabilistic Turing machine -- that is, with at most polynomial overhead.

### The Simulation Problem

Computational physics had made enormous strides using classical computers for simulating classical systems (fluid dynamics, molecular dynamics, stellar evolution). However, the simulation of quantum systems faced a fundamental bottleneck: the dimensionality of the Hilbert space grows exponentially with the number of particles.

Consider a system of $n$ spin-1/2 particles. The state of the system is a vector in a $2^n$-dimensional Hilbert space:

$$|\psi\rangle = \sum_{s_1, s_2, \ldots, s_n \in \{0,1\}} c_{s_1 s_2 \cdots s_n} |s_1 s_2 \cdots s_n\rangle$$

with $2^n$ complex amplitudes $c_{s_1 \cdots s_n}$. For $n = 300$ particles (a modest physical system), $2^{300} \approx 10^{90}$ -- more amplitudes than there are atoms in the observable universe. No conceivable classical computer can store, let alone manipulate, this much information.

### Reversible Computation

Bennett (1973) and Fredkin and Toffoli (1982) had shown that computation could be performed reversibly, without thermodynamic dissipation. Landauer (1961) had identified the connection between information erasure and entropy: erasing a bit of information necessarily dissipates at least $k_B T \ln 2$ of energy. Reversible computation avoids erasure and therefore avoids this energy cost. Feynman was aware of these developments and saw a connection to the unitarity (reversibility) of quantum mechanics.

### Benioff's Quantum Turing Machine

Paul Benioff (1980-82) had constructed a quantum mechanical model of a Turing machine, showing that computation could in principle be carried out by a quantum system evolving unitarily. However, Benioff's quantum Turing machine simulated a classical computation -- it did not exploit quantum parallelism for computational advantage.

---

## Key Arguments and Derivations

### 1. The Exponential Explosion

Feynman begins with the central observation. Consider simulating a quantum system on a classical computer. The state of $n$ quantum bits is described by $2^n$ complex numbers. Time evolution under a Hamiltonian $H$ requires exponentiating a $2^n \times 2^n$ matrix:

$$|\psi(t)\rangle = e^{-iHt/\hbar}|\psi(0)\rangle$$

Even if $H$ is sparse (only local interactions), the matrix exponential generically mixes all $2^n$ components. The computational cost scales exponentially in $n$.

Feynman makes this concrete with an example. Consider an Ising model on a lattice with $n$ sites and nearest-neighbor interactions:

$$H = -J\sum_{\langle i,j\rangle} \sigma_i^z \sigma_j^z - h\sum_i \sigma_i^x$$

For $h \neq 0$, the $\sigma^x$ terms mix different $\sigma^z$ eigenstates, and the ground state is a superposition of exponentially many configurations. Computing the partition function $Z = \text{Tr}(e^{-\beta H})$ is, in general, a computationally hard problem (BQP-complete for quantum systems, #P-hard for certain classical models).

### 2. Can Probabilistic Classical Computers Help?

Feynman considers whether classical probabilistic (stochastic) simulation can circumvent the exponential explosion. Classical Monte Carlo methods work well for many systems: the partition function $Z = \sum_s e^{-\beta E_s}$ can be estimated by sampling configurations $s$ with probability $\propto e^{-\beta E_s}$, using Markov chain methods (Metropolis algorithm).

However, for quantum systems, the analogy fails because of the **sign problem**. The quantum partition function involves a trace over the full Hilbert space:

$$Z = \text{Tr}(e^{-\beta H}) = \sum_{\text{paths}} w_{\text{path}}$$

where the weights $w_{\text{path}}$ (obtained from a Trotter decomposition or path integral) can be negative or complex for fermionic systems or systems with frustrated interactions. The Monte Carlo sampling cannot handle negative weights efficiently -- this is the notorious "sign problem" that plagues quantum Monte Carlo simulations of fermionic systems to this day.

Feynman states this as: "the probability of the whole path...is not necessarily positive, and therein lies the great difficulty...it is not a probability, but an amplitude."

### 3. Quantum Systems Cannot Be Simulated Locally

Feynman then considers Bell's theorem and its implications for simulation. A local hidden variable model assigns probabilities to measurement outcomes based on hidden variables that propagate at most at the speed of light. Bell (1964) showed that such models satisfy inequalities (Bell inequalities) that are violated by quantum mechanics.

The CHSH inequality, for instance, states that for any local hidden variable theory:

$$|E(a,b) - E(a,b') + E(a',b) + E(a',b')| \leq 2$$

while quantum mechanics predicts a maximum violation of $2\sqrt{2}$, confirmed experimentally.

Feynman argues that any classical simulation of a quantum system must either:
1. Reproduce the Bell inequality violations (requiring non-local correlations in the simulator), or
2. Fail to correctly simulate quantum mechanics.

A local classical computer cannot produce the non-local correlations of quantum mechanics without exponential resources. This is not merely a practical difficulty but a fundamental one rooted in the structure of quantum theory.

### 4. The Quantum Computer Proposal

Feynman's central proposal is to "let the computer itself be built of quantum mechanical elements which obey quantum mechanical laws." A quantum computer would use quantum bits (qubits) as its basic elements, with the state of $n$ qubits being a vector in a $2^n$-dimensional Hilbert space -- exactly the same space as the quantum system being simulated.

The key advantages of a quantum computer for simulation:

1. **State representation:** $n$ qubits naturally represent a system of $n$ quantum particles, with no exponential overhead.

2. **Time evolution:** A local Hamiltonian $H = \sum_k H_k$ (sum of local terms) can be simulated by applying a sequence of local unitary gates:

$$e^{-iHt/\hbar} \approx \prod_k e^{-iH_k \Delta t/\hbar} + O(\Delta t^2)$$

(Trotter-Suzuki decomposition). The number of gates scales polynomially with $n$ and $t$.

3. **Entanglement:** The quantum computer naturally produces and manipulates entangled states, which are the source of the exponential classical cost. Entanglement is a resource, not an obstacle.

Feynman writes: "Nature isn't classical, dammit, and if you want to make a simulation of nature, you'd better make it quantum mechanical, and by golly it's a wonderful problem, because it doesn't look so easy."

### 5. Universal Quantum Simulation

Feynman argues for universality: a sufficiently general quantum computer should be able to simulate any local quantum system. The argument is:

1. Any local quantum system has a Hamiltonian that is a sum of terms, each acting on a bounded number of qubits.
2. The time evolution under each local term can be implemented by a quantum gate acting on those qubits.
3. The Trotter decomposition approximates the full time evolution as a product of these local gates.
4. The approximation error can be made arbitrarily small by taking smaller time steps.

This is the essence of what is now called Hamiltonian simulation, formalized rigorously by Lloyd (1996) and developed into a major subfield of quantum computing.

### 6. Reversibility and Unitarity

Feynman connects quantum computation to reversible computation. Quantum time evolution is unitary, hence reversible: given the output state, one can always recover the input state by applying $U^\dagger$. This means quantum computation is inherently reversible, satisfying the thermodynamic desiderata of Landauer and Bennett without any additional effort.

However, measurement introduces irreversibility: the projection postulate collapses the state and destroys information. Feynman notes that the computation itself can be unitary, with measurement performed only at the end to extract the answer.

### 7. The Role of Probability

Feynman makes a subtle but important point about the difference between classical probability and quantum amplitudes. A classical probabilistic computer assigns probabilities $p_i \geq 0$ to outcomes, with $\sum p_i = 1$. A quantum computer assigns amplitudes $c_i \in \mathbb{C}$ with $\sum |c_i|^2 = 1$. The key difference is interference:

$$P(A \text{ or } B) = |c_A + c_B|^2 \neq |c_A|^2 + |c_B|^2 = P(A) + P(B)$$

Interference can cause cancellations (destructive interference) or enhancements (constructive interference) that have no classical analog. Quantum algorithms exploit interference to amplify the probability of correct answers and suppress the probability of wrong answers.

---

## Physical Interpretation

### The Extended Church-Turing Thesis is Wrong

The most radical implication of Feynman's argument is that the extended Church-Turing thesis -- the claim that any physical computation can be efficiently simulated by a classical computer -- is false. Quantum systems perform computations (their own time evolution) that cannot be efficiently simulated classically. This suggests that quantum computers can solve certain problems exponentially faster than classical computers.

This implication was not fully appreciated until the development of specific quantum algorithms (Deutsch 1985, Simon 1994, Shor 1994, Grover 1996) that demonstrated exponential or polynomial speedups for well-defined computational problems.

### Computation as Physics

Feynman's paper marks a conceptual shift: computation is not merely an abstract mathematical process but a physical one, constrained by the laws of physics. The question "what can be computed efficiently?" becomes a question about the physical world. If nature is quantum mechanical, then the natural model of computation is quantum, and classical computation is a special (restricted) case.

### The Sign Problem as a Feature

The "sign problem" that prevents efficient classical simulation of quantum systems is, in Feynman's framework, not a bug but a feature -- it is the signature of genuinely quantum behavior (interference, entanglement) that a classical computer cannot capture. The quantum computer "solves" the sign problem not by computing the signs but by being a quantum system that naturally produces them.

---

## Impact and Legacy

### Birth of Quantum Computing

Feynman's paper is universally cited as the foundational motivation for quantum computing. While Benioff had earlier constructed quantum Turing machines, Feynman was the first to argue that quantum computers would be qualitatively more powerful than classical ones for simulating physics.

### Quantum Algorithms

Feynman's vision was realized by:
- **Deutsch** (1985): first quantum algorithm with a provable speedup
- **Simon** (1994): exponential speedup for a structured problem
- **Shor** (1994): polynomial-time quantum algorithm for integer factorization (exponential speedup)
- **Grover** (1996): quadratic speedup for unstructured search
- **Lloyd** (1996): universal quantum simulation algorithm (direct realization of Feynman's proposal)

### Quantum Hardware

The drive to build quantum computers, motivated by Feynman's argument, has led to multiple physical implementations: superconducting qubits (Google, IBM), trapped ions (IonQ, Quantinuum), photonic systems, topological qubits (Microsoft), and neutral atoms (Atom Computing, QuEra).

### Quantum Supremacy

Google's Sycamore processor (2019) demonstrated "quantum supremacy" -- performing a specific computation (random circuit sampling) faster than any known classical algorithm. This is a direct validation of Feynman's claim that quantum systems cannot be efficiently simulated classically.

---

## Connections to Modern Physics

1. **Quantum simulation:** Feynman's proposal has been realized: quantum simulators (both digital and analog) are used to study quantum materials, quantum chemistry, and lattice gauge theories. Trapped-ion and cold-atom systems simulate Hubbard models, spin chains, and topological phases.

2. **Quantum chemistry:** The simulation of molecular electronic structure is a leading near-term application of quantum computing. The variational quantum eigensolver (VQE) and quantum phase estimation algorithms compute molecular ground-state energies on quantum hardware.

3. **Lattice gauge theory:** Quantum computers offer a path to simulating real-time dynamics and finite-density QCD, which are inaccessible to classical Monte Carlo due to the sign problem. This directly addresses Feynman's original motivation.

4. **Quantum error correction:** The realization that quantum computers are susceptible to decoherence (interaction with the environment destroys quantum coherence) led to the development of quantum error correction (Shor 1995, Steane 1996), which allows fault-tolerant quantum computation provided the error rate per gate is below a threshold.

5. **Computational complexity and physics:** Feynman's argument has spawned a rich interchange between physics and computer science. The classification of quantum computational problems (BQP, QMA, etc.) provides a new lens on the complexity of physical systems. The question "is the universe a quantum computer?" (Lloyd, 2006) echoes Feynman's original provocation.
