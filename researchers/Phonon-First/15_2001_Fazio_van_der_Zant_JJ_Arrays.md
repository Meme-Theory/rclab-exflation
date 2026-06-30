# Quantum Phase Transitions and Vortex Dynamics in Superconducting Networks

**Author(s):** Rosario Fazio, Herre van der Zant
**Year:** 2001
**Journal:** Physics Reports (review article)
**arXiv:** cond-mat/0011152
**Relevance:** HIGH

---

## Abstract

Josephson-junction arrays are ideal model systems to study a variety of phenomena such as phase transitions, frustration effects, vortex dynamics and chaos. In this review, we focus on the quantum dynamical properties of low-capacitance Josephson-junction arrays. The two characteristic energy scales in these systems are the Josephson energy, associated with the tunneling of Cooper pairs between neighboring islands, and the charging energy, which is the energy needed to add an extra electron charge to a neutral island. The phenomena described in this review stem from the competition between single-electron effects with the Josephson effect. They give rise to (quantum) Superconductor-Insulator phase transitions that occur when the ratio between the coupling constants is varied or when the external fields are varied. We describe the dependence of the various control parameters on the phase diagram and the transport properties close to the quantum critical points. On the superconducting side of the transition, vortices are the topological excitations. In low-capacitance junction arrays these vortices behave as massive particles that exhibit quantum behavior. We review the various quantum-vortex experiments and theoretical treatments of their quantum dynamics.

---

## Key Arguments and Derivations

### 1. Josephson-Junction Arrays as Model Systems
JJAs were first fabricated at IBM twenty years prior (circa 1980). They provide controlled platforms for studying classical phase transitions (BKT transition), frustration, vortex dynamics, nonlinear dynamics, and chaos. The quantum regime became accessible when submicron fabrication (100 x 100 nm$^2$ junctions) enabled charging energies $E_C$ comparable to temperatures.

### 2. Phase-Number Uncertainty Relation
The fundamental interplay between phase $\phi$ and charge $Q$ on each island:
$$[\phi_i, Q_j] = 2ei\delta_{ij}$$
Phase and charge are canonically conjugated variables. This underpins all quantum behavior in JJAs. Demonstrated by the "Heisenberg transistor" experiment.

### 3. The Quantum Phase Model
The Hamiltonian for a JJA in second quantized form:
$$H = \frac{1}{2}\sum_{i,j}(Q_i - Q_{x,i})C^{-1}_{ij}(Q_j - Q_{x,j}) - E_J\sum_{\langle i,j\rangle}\cos(\phi_i - \phi_j - A_{ij})$$
where $C^{-1}_{ij}$ is the inverse capacitance matrix, $Q_{x,i}$ are offset charges (gate voltages), and $A_{ij} = \frac{2\pi}{\Phi_0}\int_i^j \mathbf{A}\cdot d\mathbf{l}$ encodes the magnetic frustration.

### 4. Two Limiting Regimes
- **$E_J \gg E_C$ (classical limit)**: Phase fluctuations are weak $\to$ global phase coherence $\to$ **superconductor**. System described by 2D XY model. BKT transition.
- **$E_J \ll E_C$**: Charges localized on each island $\to$ Coulomb blockade $\to$ **Mott insulator**. Activation energy $\sim E_C$ for charge transport.

### 5. Superconductor-Insulator (S-I) Quantum Phase Transition
A zero-temperature phase transition driven by the ratio $E_J/E_C$. The quantum critical point occurs at $E_J/E_C \sim z \times 5.8/4 \approx 1$ (z = coordination number), analogous to the Bose-Hubbard model.

### 6. Charge and Magnetic Frustration
- **Magnetic frustration** ($f = \Phi/\Phi_0$): At rational $f = p/q$, the ground state develops a $q \times q$ unit cell. At $f = 1/2$, a fully frustrated lattice with checkerboard vortex patterns.
- **Charge frustration** ($n_x = Q_x/2e$): At $n_x = 1/2$, a "supersolid" phase can appear where both charge order and phase coherence coexist.

### 7. Dissipation Effects
Quasiparticle tunneling, ohmic shunts, and electromagnetic environment coupling modify the phase diagram. Dissipation can stabilize or destroy superconductivity depending on geometry. For ohmic dissipation with resistance $R_s$, the critical coupling becomes: the S-I transition is driven by $\alpha = R_Q/R_s$ where $R_Q = h/4e^2 = 6.45$ k$\Omega$.

### 8. Transport Properties Near the QPT
At the quantum critical point, the dc conductivity is predicted to be universal: $\sigma_{dc} = \sigma_Q = (2e)^2/h$ in the self-dual theory. Finite-temperature corrections give $\sigma(T) \propto T^{1/z}$ with dynamical exponent $z$.

### 9. Quantum Vortex Dynamics
On the superconducting side, vortices are massive particles:
- **Vortex mass**: $M_v \sim \hbar^2/(E_C a^2)$ where $a$ is lattice spacing (from phonon-like spin-wave modes)
- **Ballistic motion**: vortices propagate coherently in underdamped arrays
- **Macroscopic quantum tunneling**: vortices tunnel through barriers
- **Aharonov-Casher effect**: interference of vortex paths encircling a charge (dual of Aharonov-Bohm)
- **Bloch oscillations**: vortex analog of electron Bloch oscillations in a periodic potential
- **Mott insulator of vortices**: at commensurate filling, vortices localize (dual to charge Mott insulator)
- **Anderson localization of vortices**: disorder can localize quantum vortices

### 10. 1D Arrays as Luttinger Liquids
One-dimensional JJAs realize Luttinger liquid physics. The S-I transition occurs at the self-dual point. Lutitnger parameter $K$ controls the transition.

### 11. Quantum Computation
The review concludes with a discussion of quantum computation using Josephson junctions: charge qubits ($E_C \gg E_J$), flux qubits ($E_J \gg E_C$), and their coupling into quantum gates.

## Key Results

1. Complete phase diagram of quantum JJAs as function of $E_J/E_C$, magnetic frustration $f$, and charge frustration $n_x$
2. S-I quantum phase transition driven by competition between Josephson coupling and charging energy
3. Universal conductivity $\sigma_Q = (2e)^2/h$ at the quantum critical point
4. Vortices in quantum JJAs behave as massive quantum particles with mass $M_v \propto \hbar^2/(E_C a^2)$
5. Observation of macroscopic quantum tunneling, Aharonov-Casher effect, and Bloch oscillations of vortices
6. Charge-vortex duality: insulator of charges $\leftrightarrow$ superfluid of vortices and vice versa
7. Supersolid phase at half charge-frustration
8. Dissipation-driven S-I transition controlled by $R_Q/R_s$

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Phase-number commutator | $[\phi_i, Q_j] = 2ei\delta_{ij}$ | Sec. I.B |
| JJA Hamiltonian | $H = \frac{1}{2}\sum_{i,j}(Q_i - Q_{x,i})C^{-1}_{ij}(Q_j - Q_{x,j}) - E_J\sum_{\langle i,j\rangle}\cos(\phi_i - \phi_j - A_{ij})$ | Sec. II.A |
| Charging energy | $E_C = e^2/(2C)$ | Sec. I.A |
| Josephson energy | $E_J = \hbar I_c/(2e)$ | Sec. II.A |
| Resistance quantum | $R_Q = h/4e^2 = 6.45$ k$\Omega$ | Sec. I.A |
| Flux quantum | $\Phi_0 = h/2e$ | Sec. I.B |
| Vortex mass | $M_v \sim \hbar^2/(E_C a^2)$ | Sec. III.A |
| Critical ratio (mean-field) | $(E_J/E_C)_c = z/5.8$ | Sec. II.B |
| Universal conductivity | $\sigma_Q = (2e)^2/h$ | Sec. II.F |
| Magnetic frustration | $f = \Phi/\Phi_0$ | Sec. II.C |
| Charge frustration | $n_x = Q_x/(2e)$ | Sec. II.D |
| Dissipation parameter | $\alpha = R_Q/R_s$ | Sec. II.E |

## Relevance to Phonon-Exflation

The framework's BCS condensate on SU(3) at the fold point is a lattice-like system with Cooper pairs on a compact manifold -- an internal-space analog of a Josephson-junction array. The S-I phase transition driven by $E_J/E_C$ maps onto the framework's competition between pairing energy $|E_{cond}|$ and charging-like terms from the Dirac spectrum. The charge-vortex duality is particularly relevant: the framework's instanton gas (dense, $S_{inst} = 0.069$) can be understood as vortex-like excitations in the pair field, and the Mott insulator of vortices provides a template for understanding why the post-transit GGE state is non-thermal. The $N_{pair} = 1$ regime of JJAs (few Cooper pairs per site, strong quantum fluctuations) is the closest laboratory analog to the framework's BCS on a compact SU(3) fiber with small pairing window ($L/\xi_{GL} = 0.031$).
