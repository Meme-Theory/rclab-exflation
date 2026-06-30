# Relaxation in a Completely Integrable Many-Body Quantum System: An Ab Initio Study of the Dynamics of the Highly Excited States of 1D Lattice Hard-Core Bosons

**Author(s):** Marcos Rigol, Vanja Dunjko, Vladimir Yurovsky, Maxim Olshanii
**Year:** 2007 (submitted 2006)
**Journal:** Physical Review Letters 98, 050405 (2007)
**arXiv:** cond-mat/0604476
**Relevance:** CRITICAL — GGE prediction foundation

---

## Abstract

In this Letter we pose the question of whether a many-body quantum system with a full set of conserved quantities can relax to an equilibrium state, and, if it can, what the properties of such state are. We confirm the relaxation hypothesis through a thorough ab initio numerical investigation of the dynamics of hard-core bosons on a one-dimensional lattice. Further, a natural extension of the Gibbs ensemble to integrable systems results in a theory that is able to predict the mean values of physical observables after relaxation. Finally, we show that our generalized equilibrium carries more memory of the initial conditions than the usual thermodynamic one. This effect may have many experimental consequences, some of which having already been observed in the recent experiment on the non-equilibrium dynamics of one-dimensional hard-core bosons in a harmonic potential [T. Kinoshita, T. Wenger, D. S. Weiss, Nature (London) 440, 900 (2006)].

---

## Key Arguments and Derivations

### The Central Question

The paper poses the fundamental question: can an integrable many-body quantum system (possessing a full set of conserved quantities) relax to an equilibrium state, and if so, what characterizes that state? The context is the 2006 Kinoshita-Wenger-Weiss experiment showing that 1D hard-core bosons do not relax to standard thermal equilibrium.

### Construction of the Generalized Gibbs Ensemble

The authors conjecture that the standard prescription of statistical mechanics should be extended: maximize the many-body entropy $S = k_B \text{Tr}[\rho \ln(1/\rho)]$ subject to constraints imposed by **all** integrals of motion. This yields the density matrix:

$$\hat{\rho} = Z^{-1} \exp\left[-\sum_m \lambda_m \hat{I}_m\right]$$

where $\{\hat{I}_m\}$ is the full set of integrals of motion, $Z = \text{Tr}[\exp(-\sum_m \lambda_m \hat{I}_m)]$ is the partition function, and the Lagrange multipliers $\{\lambda_m\}$ are fixed by initial conditions: $\text{Tr}[\hat{I}_m \hat{\rho}] = \langle\hat{I}_m\rangle(t=0)$.

This reduces to the grand-canonical ensemble for generic (non-integrable) systems where the only integrals are energy, particle number, and (for periodic systems) momentum.

### The Model: Hard-Core Bosons on a Lattice

The Hamiltonian for hard-core bosons (HCB) on a 1D lattice with $L$ sites is:

$$\hat{H} = -J \sum_{i=1}^{L} (\hat{b}_i^\dagger \hat{b}_{i+1} + \text{h.c.})$$

Via the Jordan-Wigner transformation $\hat{b}_i^\dagger = \hat{c}_i^\dagger \prod_{i'=1}^{i-1} e^{-i\pi \hat{c}_{i'}^\dagger \hat{c}_{i'}}$, this maps to free fermions:

$$\hat{H} = -J \sum_{i=1}^{L} (\hat{c}_i^\dagger \hat{c}_{i+1} + \text{h.c.})$$

### Conserved Quantities

The system possesses $L$ conserved quantities — the fermionic quasi-momentum distribution operators:

$$\hat{I}_k = \hat{f}_F(k) = \frac{1}{L} \sum_{i,i'} \sigma_{i-i'}(\hat{N}) e^{-i2\pi k(i-i')/L} \hat{c}_{i'}^\dagger \hat{c}_i$$

When expressed through bosonic fields, these become complicated many-body operators (e.g., the fourth moment $\hat{I}_4$ is a two-body operator in the bosonic representation).

### Fully Constrained Ensemble

The density matrix becomes:

$$\hat{\rho}_{f.c.} = Z_{f.c.}^{-1} \exp\left[-\sum_k \lambda_k \hat{f}_F(k)\right]$$

with $Z_{f.c.} = \prod_k (1 + e^{-\lambda_k})$ and Lagrange multipliers $\lambda_k = \ln\left(\frac{1 - f_F(k)}{f_F(k)}\right)$.

### Numerical Tests

**Test 1 (Free expansion)**: $N=30$ HCB initially in ground state of a box of size $L_{in} = 150$, expanded to $L = 600$. The momentum distribution converges to a time-independent distribution. The GGE prediction is virtually indistinguishable from the dynamical result; the grand-canonical prediction fails.

**Test 2 (Superlattice release)**: Initial ground state with a period-4 superlattice, released to a flat box. The four characteristic peaks in the momentum distribution remain well-resolved even after very long propagation ($t_{fin} = 3000\hbar/J$). The GGE predicts this memory effect; the grand-canonical ensemble does not.

### Memory of Initial Conditions

The GGE carries more memory of the initial conditions than the standard thermodynamic ensemble. If the initial momentum distribution has several well-separated peaks, the GGE prevents them from overlapping regardless of propagation time. This explains the Kinoshita-Wenger-Weiss experimental observation that the two-peaked momentum distribution of 1D hard-core bosons failed to relax to a single-bell distribution.

---

## Key Results

1. Integrable many-body quantum systems DO relax to equilibrium states, but these are NOT described by standard statistical mechanics
2. The Generalized Gibbs Ensemble (GGE), obtained by maximizing entropy subject to all conserved quantities, correctly predicts observables after relaxation
3. The GGE reduces to the grand-canonical ensemble for non-integrable systems
4. The GGE prediction is virtually exact (within line width) for the bosonic momentum distribution after relaxation
5. The generalized equilibrium retains significantly more memory of initial conditions than thermal equilibrium
6. Multi-peaked initial momentum distributions retain their peak structure indefinitely — peaks never merge
7. The GGE explains the non-equilibration observed in the Kinoshita-Wenger-Weiss quantum Newton's cradle experiment

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| GGE density matrix | $\hat{\rho} = Z^{-1} \exp\left[-\sum_m \lambda_m \hat{I}_m\right]$ | Eq. (1) |
| Initial-value constraint | $\text{Tr}[\hat{I}_m \hat{\rho}] = \langle\hat{I}_m\rangle(t=0)$ | Eq. (2) |
| HCB Hamiltonian | $\hat{H} = -J\sum_{i=1}^{L}(\hat{b}_i^\dagger \hat{b}_{i+1} + \text{h.c.})$ | Eq. (3) |
| Momentum distribution | $\hat{f}(k) = \frac{1}{L}\sum_{i,i'} e^{-i2\pi k(i-i')/L} \hat{b}_{i'}^\dagger \hat{b}_i$ | Eq. (4) |
| Free fermion form | $\hat{H} = -J\sum_{i=1}^{L}(\hat{c}_i^\dagger \hat{c}_{i+1} + \text{h.c.})$ | Eq. (5) |
| Conserved quantities | $\hat{I}_k = \frac{1}{L}\sum_{i,i'} \sigma_{i-i'}(\hat{N}) e^{-i2\pi k(i-i')/L} \hat{c}_{i'}^\dagger \hat{c}_i$ | Eq. (6) |
| Fully constrained ensemble | $\hat{\rho}_{f.c.} = Z_{f.c.}^{-1}\exp\left[-\sum_k \lambda_k \hat{f}_F(k)\right]$ | Eq. (8) |
| Lagrange multipliers | $\lambda_k = \ln\left(\frac{1 - f_F(k)}{f_F(k)}\right)$ | Text below Eq. (8) |
| Superlattice potential | $\hat{V}_{ext} = A\sum_i \cos\frac{2\pi i}{T} \hat{b}_i^\dagger \hat{b}_i$, $T=4$ | Eq. (9) |

---

## Relevance to Phonon-Exflation

This is the founding paper of the GGE concept, which is a central prediction of the phonon-exflation framework. In Session 38, the post-transit state of the BCS condensate on SU(3) was identified as a GGE with 8 Richardson-Gaudin conserved integrals. The framework predicts that this GGE NEVER thermalizes — it retains permanent non-thermal character protected by exact integrability and the block-diagonal theorem ($D_K$ block-diagonality, Session 22b). Rigol's key insight — that the GGE carries more memory of initial conditions than thermal equilibrium — is precisely what makes the framework's GGE a unique cosmological prediction: the relic particle spectrum is determined by the ground state + unitary evolution + integrability, stronger than the no-boundary proposal.
