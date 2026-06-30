# Generalized Gibbs ensemble in integrable lattice models

**Author(s):** Lev Vidmar and Marcos Rigol
**Year:** 2016
**Journal:** Journal of Statistical Mechanics: Theory and Experiment (2016) 064007
**arXiv:** 1604.03990
**Relevance:** HIGH — GGE universality

---

## Abstract

The generalized Gibbs ensemble (GGE) was introduced ten years ago to describe observables in isolated integrable quantum systems after equilibration. Since then, the GGE has been demonstrated to be a powerful tool to predict the outcome of the relaxation dynamics of few-body observables in a variety of integrable models, a process we call generalized thermalization. This review discusses several fundamental aspects of the GGE and generalized thermalization in integrable systems. In particular, we focus on questions such as: which observables equilibrate to the GGE predictions and who should play the role of the bath; what conserved quantities can be used to construct the GGE; what are the differences between generalized thermalization in noninteracting systems and in interacting systems mappable to noninteracting ones; why is it that the GGE works when traditional ensembles of statistical mechanics fail. Despite a lot of interest in these questions in recent years, no definite answers have been given. We review results for the XX model and for the transverse field Ising model. For the latter model, we also report original results and show that the GGE describes spin-spin correlations over the entire system. This makes apparent that there is no need to trace out a part of the system in real space for equilibration to occur and for the GGE to apply. In the past, a spectral decomposition of the weights of various statistical ensembles revealed that generalized eigenstate thermalization occurs in the XX model (hard-core bosons). Namely, eigenstates of the Hamiltonian with similar distributions of conserved quantities have similar expectation values of few-spin observables. Here we show that generalized eigenstate thermalization also occurs in the transverse field Ising model.

---

## Key Arguments and Derivations

### Models and Mappings (Section 2)

The review focuses on two paradigmatic models: the XX model (hard-core bosons) and the transverse field Ising model (TFIM), both mappable to noninteracting fermions via Jordan-Wigner transformation.

**XX model**: $\hat{H}_{XX} = -\tilde{J}\sum_j (\hat{b}_j^\dagger \hat{b}_{j+1} + \text{h.c.}) + \sum_j V_j \hat{b}_j^\dagger \hat{b}_j$

Maps to free fermions: $\hat{H}_{XX} = -\tilde{J}\sum_j (\hat{f}_j^\dagger \hat{f}_{j+1} + \text{h.c.}) + \sum_j V_j \hat{f}_j^\dagger \hat{f}_j$

**Transverse field Ising model**: Obtained from the XY model with anisotropy $\gamma = 1$:

$$\hat{H}_{TFI} = -J\sum_j \hat{S}_j^x \hat{S}_{j+1}^x - h\sum_j \hat{S}_j^z$$

Diagonalized via Jordan-Wigner + Fourier + Bogoliubov transformation to $\hat{H}_{TFI} = \sum_k \epsilon_k (\hat{\gamma}_k^\dagger \hat{\gamma}_k + \hat{\gamma}_{-k}^\dagger \hat{\gamma}_{-k} - 1)$ with $\epsilon_k = \sqrt{h^2 + 2hJ\cos k + J^2}$.

A crucial distinction: hard-core bosons are **interacting** (due to the local constraint forbidding multiple occupancy) despite being mappable to free fermions. The mapping is nonlocal. This means observables that equilibrate for hard-core bosons may NOT equilibrate for the fermions, and vice versa.

### Quantum Quenches and Ensembles (Section 2.3)

After a quantum quench, the time-evolved state $|\psi(t)\rangle = \sum_n c_n e^{-iE_n t} |n\rangle$ gives time-averaged observables described by the **diagonal ensemble**: $\langle\hat{O}\rangle_{DE} = \sum_n |c_n|^2 \langle n|\hat{O}|n\rangle$.

Three ensembles are compared:
- **Diagonal ensemble** (DE): exact time average, requires full knowledge of $|c_n|^2$
- **Grand canonical ensemble** (GE): thermal prediction, uses only energy and particle number
- **Generalized Gibbs ensemble** (GGE): uses all conserved quantities, $\hat{\rho}_{GGE} = Z^{-1}\exp(-\sum_m \lambda_m \hat{I}_m)$

### Conserved Quantities (Section 2.4)

For the XX model: the occupations of single-particle eigenstates $\hat{m}_k^f = \hat{f}_k^\dagger \hat{f}_k$ are the conserved quantities.

For the TFIM: the occupations of Bogoliubov quasiparticle modes $\hat{n}_k = \hat{\gamma}_k^\dagger \hat{\gamma}_k$ are conserved. For quenches starting from an eigenstate, the conserved quantities $\hat{n}_k$ are related to the initial parameters through the overlap $\mu_k = |v_k u_k^{(0)} - u_k v_k^{(0)}|^2$ and $\langle\hat{n}_k\rangle_0 = \mu_k$.

### Dynamics and Generalized Thermalization (Section 3)

Numerical simulations of hard-core bosons confirm:
1. The momentum distribution $m_k(t)$ relaxes to a time-independent distribution
2. The GGE prediction matches the relaxed state to within numerical precision
3. The grand-canonical prediction fails dramatically
4. Multi-peaked initial distributions retain their peak structure indefinitely

For noninteracting fermions, some one-body observables (specifically the fermionic momentum distribution) do NOT equilibrate — they remain time-independent by construction. However, their time averages are still correctly predicted by the GGE. This is a fundamental difference from interacting hard-core bosons.

### Ensembles in the TFIM (Section 4)

The authors report original results showing:
- Energy distributions in the GGE and GE are qualitatively different (GGE is much broader)
- The GGE entropy $S_{GGE}/L = -\sum_k [\mu_k \ln\mu_k + (1-\mu_k)\ln(1-\mu_k)]/L$ is always less than the GE entropy
- Spin-spin correlations $\langle\hat{S}_j^x \hat{S}_{j+d}^x\rangle$ over the **entire system** are described by the GGE
- The trace distance between DE and GGE correlation matrices vanishes in the thermodynamic limit

This last result is significant: there is no need to trace out part of the system for the GGE to apply.

### Generalized Eigenstate Thermalization (Section 5)

The paper demonstrates that "generalized eigenstate thermalization" occurs: eigenstates with similar distributions of conserved quantities have similar expectation values of observables. This provides a microscopic explanation for why the GGE works — it is the integrable-system analog of the eigenstate thermalization hypothesis (ETH) for non-integrable systems.

---

## Key Results

1. The GGE describes spin-spin correlations over the ENTIRE system, not just subsystems — no real-space tracing is needed
2. There is a fundamental difference between noninteracting systems and interacting systems mappable to noninteracting ones regarding equilibration
3. Generalized eigenstate thermalization occurs in the transverse field Ising model (new result)
4. The GGE entropy is always less than the grand-canonical entropy (the GGE carries more information)
5. The trace distance between diagonal and GGE correlations vanishes in the thermodynamic limit
6. For the TFIM, a complete analytical framework for computing observables in all ensembles exists
7. Hard-core boson observables equilibrate; the corresponding fermionic observables may not

---

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| XY Hamiltonian | $\hat{H}_{XY} = -J\sum_j [(1+\gamma)\hat{S}_j^x\hat{S}_{j+1}^x + (1-\gamma)\hat{S}_j^y\hat{S}_{j+1}^y] - h\sum_j \hat{S}_j^z$ | Eq. (1) |
| HCB Hamiltonian | $\hat{H}_{XX} = -\tilde{J}\sum_j(\hat{b}_j^\dagger\hat{b}_{j+1}+\text{h.c.}) + \sum_j V_j\hat{b}_j^\dagger\hat{b}_j$ | Eq. (3) |
| Jordan-Wigner map | $\hat{S}_j^+ = \hat{f}_j^\dagger e^{i\pi\sum_{l<j}\hat{f}_l^\dagger\hat{f}_l}$ | Eq. (4) |
| TFIM diag. form | $\hat{H}_{TFI}^{(+)} = \sum_{k\in K^{(+)}} [\epsilon_k(\hat{\gamma}_k^\dagger\hat{\gamma}_k + \hat{\gamma}_{-k}^\dagger\hat{\gamma}_{-k}) - \epsilon_k]$ | Eq. (8) |
| Bogoliubov energies | $\epsilon_k = \sqrt{h^2 + 2hJ\cos k + J^2}$ | Eq. (9) |
| Diagonal ensemble | $\langle\hat{O}\rangle_{DE} = \sum_n |c_n|^2\langle n|\hat{O}|n\rangle$ | Eq. (15) |
| Grand canonical | $\hat{\rho}_{GE} = Z_{GE}^{-1}\exp(-\beta\hat{H} - \alpha\hat{N})$ | Eq. (16) |
| GGE density matrix | $\hat{\rho}_{GGE} = Z_{GGE}^{-1}\exp\left(-\sum_m \lambda_m \hat{I}_m\right)$ | Eq. (18) |
| HCB momentum distrib. | $\hat{m}_k = \frac{1}{L}\sum_{j,l} e^{-i(l-j)k} \hat{b}_j^\dagger \hat{b}_l$ | Eq. (6) |
| GGE entropy (TFIM) | $S_{GGE}/L = -\frac{1}{L}\sum_k[\mu_k\ln\mu_k + (1-\mu_k)\ln(1-\mu_k)]$ | Sec. 4.2 |
| Observable decomposition | $\langle\hat{O}\rangle = \sum_{k\in K^{(+)}} \sum_{\nu=0}^{3} w_{k,\nu}^{(\pm)} O_{k}^{(\nu)}$ | Eq. (40) |

---

## Relevance to Phonon-Exflation

This paper establishes the universality of the GGE across different integrable models (XX, TFIM, XXZ), which is essential for the framework's claim that the post-transit GGE on SU(3) is a robust prediction. The demonstration that the GGE describes correlations over the ENTIRE system (not just subsystems) strengthens the framework's identification of the GGE relic as a genuinely global state. The generalized eigenstate thermalization result provides the microscopic mechanism for why the framework's 8 Richardson-Gaudin conserved quantities determine the final state. The distinction between interacting systems and their free-fermion images is directly relevant: the BCS on SU(3) is an interacting system (in the original SU(3) basis) that maps to free quasiparticles via Bogoliubov transformation, exactly the structure analyzed here.
