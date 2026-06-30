# Superfluidity in topologically nontrivial flat bands

**Author(s):** Sebastiano Peotta, Paivi Torma
**Year:** 2015
**Journal:** Nature Communications (based on format)
**arXiv:** 1506.02815
**Relevance:** CRITICAL

---

## Abstract

Topological invariants built from the periodic Bloch functions characterize new phases of matter, such as topological insulators and topological superconductors. The most important topological invariant is the Chern number that explains the quantized conductance of the quantum Hall effect. Here, we provide a general result for the superfluid weight $D_s$ of a multiband superconductor that is applicable to topologically nontrivial bands with nonzero Chern number $C$. We find that the integral over the Brillouin zone of the quantum metric, an invariant calculated from the Bloch functions, gives the superfluid weight in a flat band, with the bound $D_s \geq |C|$. Thus, even a flat band can carry finite superfluid current, provided the Chern number is nonzero. As an example, we provide $D_s$ for the time-reversal invariant attractive Harper-Hubbard model that can be experimentally tested in ultracold gases. In general, our results establish that a topologically nontrivial flat band is a promising concept for increasing the critical temperature of the superconducting transition.

---

## Key Arguments and Derivations

### 1. The Flat Band Paradox
BCS theory predicts $T_c \propto \exp(-1/(Un_0(E_F)))$. Since $n_0(E_F)$ is maximal for vanishing bandwidth (flat band), $T_c$ should be maximized: in the flat-band limit $U/J \gg 1$, the exponential suppression disappears and $T_c \propto Un_0(E_F) \propto U/J$. However, within the **single-band** effective Hamiltonian approximation, the superfluid weight vanishes ($D_s \propto J$) because Cooper pairs localize on individual lattice sites. This is the central paradox: high $T_c$ but zero superfluid weight.

### 2. Multiband Resolution: The Quantum Metric
The authors resolve this paradox using a **multiband BCS framework**. The superfluid weight depends not only on the energy dispersion but also on the **Bloch functions** of the lattice Hamiltonian. In the flat-band limit, the superfluid weight is controlled by the **quantum geometric tensor** -- an invariant constructed from the Bloch functions alone.

### 3. Superfluid Weight Formalism
The superfluid weight is defined via the grand potential:
$$[D_s]_{i,j} = \frac{1}{V\hbar^2}\frac{\partial^2 \Omega}{\partial q_i \partial q_j}\bigg|_{\mu, \Delta, q=0}$$
where $q$ is the supercurrent wavevector.

The total superfluid weight consists of three terms: $D_s = D_{s,1} + D_{s,2} + D_{s,3}$.

**Conventional term** (vanishes for flat bands):
$$[D_{s,1}]_{i,j} = \frac{2}{V\hbar^2}\sum_k \text{Tr}\left[V_k V_k^\dagger \partial_{k_i}\partial_{k_j}\varepsilon_k\right]$$

**Interband terms** (survive in flat bands):
$$[D_{s,2}]_{i,j} = \frac{2}{V\hbar^2}\sum_k \text{Tr}\left[V_k U_k^\dagger \partial_{q_i}\partial_{q_j}D_k(q=0)\right]$$

$$[D_{s,3}]_{i,j} = \frac{2}{V\hbar^2}\sum_k \sum_{n,n'}\frac{[B_{k,i}]_{n,n'}[B_{k,j}]_{n',n}}{E_{nk} + E_{n'k}}$$

### 4. Flat Band Result: Quantum Metric Controls Superfluid Weight
In the flat-band limit, $D_{s,1} = 0$ and the surviving terms give:
$$[D_s]_{i,j} = \frac{2Un_\phi}{\pi\hbar^2}\nu(1-\nu) M^R_{ij}$$
where $\nu$ is the filling factor and $M^R_{ij}$ is the **quantum metric** -- the real part of the Hermitian matrix:
$$M_{ij} = \frac{1}{2\pi}\int_{B.Z.} d^2k\, B_{ij}(k)$$
with the quantum geometric tensor:
$$B_{ij}(k) = 2\text{Tr}\left[(\partial_{k_i}\bar{G}_k^\dagger)(\partial_{k_j}\bar{G}_k)\right] + 2\text{Tr}\left[\bar{G}_k^\dagger(\partial_{k_i}\bar{G}_k)\bar{G}_k^\dagger(\partial_{k_j}\bar{G}_k)\right]$$

### 5. The Topological Bound
The imaginary part of $B_{ij}(k)$ is the Berry curvature; its BZ integral gives the Chern number: $\text{Im}(M_{ij}) = \epsilon_{ij}C$. The positive semidefiniteness of $M_{ij}$ implies:
$$\det(M^R) \geq \det(M^I) = C^2$$
For isotropic systems, this yields the bound:
$$D_s \geq |C|$$
A topologically nontrivial flat band ($C \neq 0$) is **guaranteed** to have finite superfluid density.

### 6. Connection to Wannier Functions
The non-localizability of Wannier functions for $C \neq 0$ bands is intimately connected to finite superfluid weight. The trace $\text{Tr}\, M$ equals the gauge-invariant part of the Marzari-Vanderbilt localization functional $F$, and Eq. (23) implies $F \geq \frac{A_\Omega}{2\pi}|C|$.

### 7. Harper-Hubbard Model Example
For the time-reversal invariant attractive Harper-Hubbard model with commensurate flux $n_\phi = 1/Q$, the BCS solution in the flat-band limit yields:
$$M = \begin{pmatrix} 2\bar{n}+1 & -i \\ i & 2\bar{n}+1 \end{pmatrix}$$
The superfluid weight is proportional to $2\bar{n}+1$ (the Landau level index). The bound $D_s \geq |C|$ is **saturated** for the lowest Landau level ($|C| = 1$).

### 8. Critical Temperature
At half filling, $T_c = \frac{1}{2}\Delta_{T=0} = \frac{Un_\phi}{4}$. The BKT temperature is close: $T_{BKT} \approx 0.25, 0.61, 0.75\, T_c$ for $\bar{n} = 0, 1, 2$.

## Key Results

1. **Central theorem**: Superfluid weight in a flat band is proportional to the quantum metric (BZ average of the quantum geometric tensor), not the band dispersion
2. **Topological bound**: $D_s \geq |C|$ -- nonzero Chern number guarantees finite superfluid weight even in a perfectly flat band
3. **Linear scaling**: $D_s \propto U$ in flat bands (vs. $D_s \propto J$ independent of $U$ in ordinary superconductors)
4. **$T_c$ scaling**: $T_c \propto U$ (linear, not exponentially suppressed) in the flat-band limit
5. **Two current components**: conventional (from group velocity, $\propto J$) and geometric (from Bloch functions, $\propto \Delta$); only the latter survives in flat bands
6. Exact result for Harper-Hubbard model: $D_s \propto (2\bar{n}+1)$ in the $\bar{n}$-th Landau level
7. The BCS wavefunction is the **exact** ground state in the continuum limit of the Harper-Hubbard model

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| Superfluid weight definition | $[D_s]_{i,j} = \frac{1}{V\hbar^2}\frac{\partial^2 \Omega}{\partial q_i \partial q_j}\big|_{q=0}$ | Eq. (1) |
| Peierls substitution | $K_{i,j} \to K_{i,j} e^{iq\cdot(r_i - r_j)}$ | Eq. (2) |
| Lattice Hamiltonian | $\hat{H} - \mu\hat{N} = \sum_{i\alpha,j\beta}\sum_\sigma \hat{c}^\dagger_{i\alpha\sigma} K^\sigma_{i\alpha,j\beta} e^{iq\cdot(r_{i\alpha}-r_{j\beta})} \hat{c}_{j\beta\sigma} - U\sum_{i,\alpha,\sigma}\hat{c}^\dagger_{i\alpha\uparrow}\hat{c}_{i\alpha\uparrow}\hat{c}^\dagger_{i\alpha\downarrow}\hat{c}_{i\alpha\downarrow} - \mu\hat{N}$ | Eq. (3) |
| Band structure diagonalization | $\tilde{K}^\sigma(k) = G_{k\sigma}\varepsilon_{k\sigma}G^\dagger_{k\sigma}$ | Eq. (4) |
| BdG Hamiltonian | $H_k(q) = \begin{pmatrix}\varepsilon_{k-q} - \mu\mathbf{1} & G^\dagger_{k-q}\Delta G_{k+q} \\ G^\dagger_{k+q}\Delta G_{k-q} & -(\varepsilon_{k+q} - \mu\mathbf{1})\end{pmatrix}$ | Eq. (6) |
| Grand potential | $\Omega(q) = -\frac{1}{2}\sum_k \text{Tr}[\|H_k(q)\|] + \ldots$ | Eq. (10) |
| Supercurrent | $J(q) = -\frac{1}{2V\hbar}\sum_k \text{Tr}[\text{sign}(E_k(q))W^\dagger_k(q)\partial_q H_k(q)W_k(q)]$ | Eq. (11) |
| Conventional $D_s$ | $[D_{s,1}]_{i,j} = \frac{2}{V\hbar^2}\sum_k \text{Tr}[V_kV_k^\dagger \partial_{k_i}\partial_{k_j}\varepsilon_k]$ | Eq. (12) |
| Interband $D_s$ (term 2) | $[D_{s,2}]_{i,j} = \frac{2}{V\hbar^2}\sum_k \text{Tr}[V_kU_k^\dagger \partial_{q_i}\partial_{q_j}D_k(q=0)]$ | Eq. (13) |
| Interband $D_s$ (term 3) | $[D_{s,3}]_{i,j} = \frac{2}{V\hbar^2}\sum_k \sum_{n,n'}\frac{[B_{k,i}]_{n,n'}[B_{k,j}]_{n',n}}{E_{nk}+E_{n'k}}$ | Eq. (14) |
| Flat-band $D_s$ | $[D_s]_{i,j} = \frac{2Un_\phi}{\pi\hbar^2}\nu(1-\nu)M^R_{ij}$ | Eq. (20) |
| Quantum geometric tensor | $B_{ij}(k) = 2\text{Tr}[(\partial_{k_i}\bar{G}_k^\dagger)(\partial_{k_j}\bar{G}_k)] + 2\text{Tr}[\bar{G}_k^\dagger(\partial_{k_i}\bar{G}_k)\bar{G}_k^\dagger(\partial_{k_j}\bar{G}_k)]$ | Eq. (22) |
| Topological bound | $\det(M^R) \geq \det(M^I) = C^2$ | Eq. (23) |
| BCS flat-band gap | $\Delta = Un_\phi\sqrt{\nu(1-\nu)}$ | Eq. (17) |
| Mean-field $T_c$ | $T_c = \frac{1}{2}\Delta_{T=0} = \frac{Un_\phi}{4}$ | Eq. (27) |
| Harper-Hubbard $M$ | $M = \begin{pmatrix}2\bar{n}+1 & -i \\ i & 2\bar{n}+1\end{pmatrix}$ | Eq. (26) |

## Relevance to Phonon-Exflation

This paper is foundational for the framework's BCS mechanism. The Dirac spectrum on SU(3) produces bands that are approximately flat near the fold point (tau ~ 0.15--0.20), and the key question is whether such flat bands can support superfluid transport. Peotta-Torma answer this definitively: **the quantum metric, not kinetic energy, controls superfluidity in flat bands**. The framework's SU(3) fiber has nonzero Chern number (established in the BDI classification, Session 17c), which guarantees $D_s \geq |C| > 0$ by the topological bound. The linear scaling $D_s \propto U$ and $T_c \propto U$ (not exponentially suppressed) is precisely what makes the framework's BCS condensation at the van Hove point viable: even though the gap-edge modes have near-zero dispersion (the constant-ratio trap), the geometric contribution from interband coupling ensures finite superfluid weight. This resolves what would otherwise be a fatal objection to BCS on a compact manifold.
