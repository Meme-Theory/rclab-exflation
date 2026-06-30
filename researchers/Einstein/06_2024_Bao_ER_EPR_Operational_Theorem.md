# ER = EPR is an Operational Theorem

**Author(s):** Chris Fields, James F. Glazebrook, Antonino Marciano, and Emanuele Zappala
**Year:** 2024
**Journal:** [INCOMPLETE - not extractable from PDF; arXiv preprint]
**arXiv:** 2410.16496
**Relevance:** MEDIUM

---

## Abstract

We show that in the operational setting of a two-agent, local operations, classical communication (LOCC) protocol, Alice and Bob cannot operationally distinguish monogamous entanglement from a topological identification of points in their respective local spacetimes, i.e. that ER = EPR can be recovered as an operational theorem. Our construction immediately implies that in this operational setting, the local topology of spacetime is observer-relative. It also provides a simple demonstration of the non-traversability of ER bridges. As our construction does not depend on an embedding geometry, it generalizes previous geometric approaches to ER = EPR.

---

## Key Arguments and Derivations

### 1. LOCC Protocols and Quantum Channels

The paper works within the framework of LOCC (Local Operations, Classical Communication) protocols. Two agents Alice and Bob are: (i) mutually separable and conditionally statistically independent, (ii) separated from their joint environment $E$ by a holographic screen $B$, (iii) implement read/write quantum reference frames (QRFs) $Q_A$ and $Q_B$, and (iv) communicate via classical and quantum channels implemented by $E$.

A **quantum channel** exists if there are distinct collections of qubits $q_A$ and $q_B$ accessible only to Alice and Bob respectively, with $|q_A q_B\rangle \neq |q_A\rangle|q_B\rangle$. A **classical channel** exists if there are causal processes $f$ and $g$ implemented by $E$ such that $q'_B = f(q'_A)$ and $q'_A = g(q'_B)$.

A quantum instrument is a family of completely positive maps $\mathcal{E}_j : B(\mathcal{H}) \to B(\mathcal{H})$ with trace-preserving sum. LOCC protocols are defined recursively from local instruments.

### 2. Zero-Decoherence Limit

The key physical argument: as decoherence in the quantum channel approaches zero, the channel approaches a pure entangled state $|q_A q_B\rangle$. In this limit:
- The interaction $H_{Q\bar{Q}}$ between channel degrees of freedom $Q$ and non-channel degrees of freedom $\bar{Q}$ of the environment approaches zero.
- $Q$ and $\bar{Q}$ become decoupled.
- Alice can obtain no information about the dimension of $Q$ by observing boundary qubits outside $q_A$.

This is the topological transformation depicted in Diagram (2): the environmental degrees of freedom implementing the quantum channel shrink to zero, leaving only the boundary state $|q_A q_B\rangle$.

### 3. Main Theorem (Theorem 1)

**Theorem 1.** In any LOCC protocol in which all systems are finite, and in which the boundary $B$ between the communicating agents $A$ and $B$ and their joint environment $E$ is a holographic screen, as the entanglement made available to $A$ and $B$ by the quantum channel approaches pairwise monogamy, and hence the decoherence in the quantum channel detectable by $A$ or $B$ decreases to zero, the number of environmental degrees of freedom of $E$ required to implement the quantum channel becomes operationally indistinguishable, by $A$ or $B$, from zero in the limit of monogamous entanglement.

**Proof sketch:** Alice can estimate decoherence by comparing joint measurement statistics to the Tsirelson bound. Information about the channel's degrees of freedom $Q$ is accessible to Alice only via $H_E$'s action on boundary qubits other than $q_A$. But as $H_{Q\bar{Q}} \to 0$, the action of $H_{\bar{Q}}$ on $B$ transfers no information about $Q$. Alice cannot determine that dim($Q$) $\neq 0$.

### 4. Corollary: ER = EPR

**Corollary 2.** In any LOCC protocol with finite systems and holographic screen boundary, a quantum channel implementing a shared, monogamously-entangled pair of qubits ("EPR") is operationally indistinguishable from a topological identification of the locally-measured locations $x_A$ and $x_B$ of the qubits accessed by $A$ and $B$ respectively ("ER").

This recovers ER = EPR as an operational theorem without assuming an embedding geometry, generalizing the original Maldacena-Susskind conjecture (which relied on AdS/CFT and geometric arguments).

### 5. Non-Traversability of ER Bridges

The construction provides a simple proof: Alice cannot "jump into" the channel because dim(Alice) > dim($q_A$), and she cannot determine her own complete state by observation. No firewall is required. "Exotic" modifications of the channel do not affect this negative outcome.

### 6. Observer-Relativity of Spacetime Topology

Since entanglement is known to be observer/QRF-relative, Corollary 2 immediately implies that the local topology of spacetime is observer/QRF-relative. This follows because the topological identification $x_A \leftrightarrow x_B$ depends on the QRFs employed by Alice and Bob, which are freely and independently chosen.

---

## Key Results

1. ER = EPR derived as an operational theorem from LOCC + holographic principle, without embedding geometry.
2. Monogamous entanglement is operationally indistinguishable from topological identification of boundary points.
3. Codespace dimension of a perfect QECC is operationally indistinguishable from the code dimension (Corollary 1).
4. Non-traversability of ER bridges follows without firewalls.
5. Local topology of spacetime is observer/QRF-relative.
6. Construction generalizes geometric formulations of ER = EPR (Maldacena-Susskind).

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Entangled channel condition | $\|q_A q_B\rangle \neq \|q_A\rangle\|q_B\rangle$ | Sec. 1 |
| Hamiltonian decomposition | $H_E = H_Q + H_{\bar{Q}} + H_{Q\bar{Q}}$ | Proof of Thm. 1 |
| Decoherence limit | $H_{Q\bar{Q}} \to 0 \implies Q, \bar{Q}$ decouple | Proof of Thm. 1 |
| Holographic boundary | $\mathcal{H}_B = \bigotimes_{i=1}^N \mathcal{H}_{q_i}$ | Sec. 4.2 |
| Quantum instrument | $\sum_j \mathcal{E}_j$ is trace-preserving; $\rho \mapsto \sum_j \mathcal{E}_j(\rho) \otimes \|j\rangle\langle j\|$ | Sec. 2.1 |
| Separability requirement | $\|AB\rangle = \|A\rangle\|B\rangle$ (for free choice in LOCC) | Sec. 3 |

---

## Relevance to Phonon-Exflation

This paper provides a rigorous operational derivation of ER = EPR that is relevant to the framework's treatment of inter-sector entanglement and spacetime topology. The result that spacetime topology is observer-relative resonates with the framework's finding that the GGE relic state (produced by the transit through the fold) is integrability-protected and observer-inaccessible from 4D. The topological identification implied by ER = EPR could connect to the framework's fiber bundle structure, where the SU(3) fiber provides a "channel" between different sectors of the Dirac spectrum. The paper's use of holographic screens and QECC language is relevant to the framework's use of the holographic principle in relating bulk SU(3) geometry to boundary observables.
