# Generalized Gibbs ensemble in integrable lattice models

**Author(s):** Lev Vidmar, Marcos Rigol
**Year:** 2016
**Journal:** J. Stat. Mech. (review article, special issue on Quantum Integrability)
**arXiv/DOI:** arXiv:1604.03990v3
**Relevance:** CRITICAL

---

## Abstract

The generalized Gibbs ensemble (GGE) was introduced ten years ago to describe observables in isolated integrable quantum systems after equilibration. Since then, the GGE has been demonstrated to be a powerful tool to predict the outcome of the relaxation dynamics of few-body observables in a variety of integrable models, a process we call generalized thermalization. This review discusses several fundamental aspects of the GGE and generalized thermalization in integrable systems. In particular, we focus on questions such as: which observables equilibrate to the GGE predictions and who should play the role of the bath; what conserved quantities can be used to construct the GGE; what are the differences between generalized thermalization in noninteracting systems and in interacting systems mappable to noninteracting ones; why is it that the GGE works when traditional ensembles of statistical mechanics fail. Despite a lot of interest in these questions in recent years, no definite answers have been given. We review results for the XX model and for the transverse field Ising model. For the latter model, we also report original results and show that the GGE describes spin-spin correlations over the entire system. This makes apparent that there is no need to trace out a part of the system in real space for equilibration to occur and for the GGE to apply. In the past, a spectral decomposition of the weights of various statistical ensembles revealed that generalized eigenstate thermalization occurs in the XX model (hard-core bosons). Namely, eigenstates of the Hamiltonian with similar distributions of conserved quantities have similar expectation values of few-spin observables. Here we show that generalized eigenstate thermalization also occurs in the transverse field Ising model.

---

## Key Arguments and Derivations

**Section 1: Introduction.** Historical context: Lieb–Schulz–Mattis 1961 exact solution; Mazur's nonergodicity in XY model; Barouch et al. quench studies; conserved quantities in 1D spin chains; Kinoshita–Wenger–Weiss experiment showing 1D Bose gas fails to thermalize to standard Gibbs. GGE introduced in Refs. [35, 36] for hard-core bosons, obtained via Jaynes entropy maximization with extensive set of integrability-enforced conserved quantities. Successful in: Luttinger liquids, 1/r Hubbard, sine-Gordon, transverse field Ising, hard-core bosons/anyons, Lieb-Liniger bosons, QFTs, XXZ chains.

**Section 2.1: XY model.** Hamiltonian $\hat{H}_{XY} = -J\sum_j[(1+\gamma)\hat{S}^x_j\hat{S}^x_{j+1} + (1-\gamma)\hat{S}^y_j\hat{S}^y_{j+1}] - h\sum_j\hat{S}^z_j$ (Eq. 1). Hard-core boson form Eq. 2.

**2.1.1 XX model** ($\gamma=0$): particle-number conserving, mapped via Jordan-Wigner (Eq. 4) to free spinless fermions $\hat{H}_{XX} = -2\tilde{J}\sum_k \cos(k)\hat{f}^\dagger_k\hat{f}_k$. Hard-core boson quasi-momentum distribution $\hat{m}_k = (1/L)\sum_{j,l}e^{-i(l-j)k}\hat{b}^\dagger_j\hat{b}_l$ (Eq. 6).

**Crucial distinction.** Hard-core bosons and noninteracting fermions differ fundamentally in equilibration. The JW mapping is nonlocal; the one-body sector of noninteracting fermions evolves unitarily, while hard-core bosons (interacting) do not preserve one-body unitarity. For noninteracting fermions, extensive sets of one-body observables may fail to equilibrate; hard-core bosons equilibrate (in absence of disorder-driven localization).

**2.1.2 Transverse field Ising model** ($\gamma=1$): non-number-conserving. Translationally invariant case Eqs. 7 yields even (+) and odd (-) sectors with different boundary conditions and wave-vector sets $\mathcal{K}^{(\pm)}$. Bogoliubov transform $\hat{f}_k = u_k\hat\eta_k - v^*_{-k}\hat\eta^\dagger_{-k}$ diagonalizes Eqs. 8 with quasiparticle energies $\epsilon_k = \sqrt{h^2 + 2hJ\cos k + J^2}$ (Eq. 9). Quantum phase transition at $h = 1$; ground state doubly-degenerate for $h < 1$ ferromagnetic, nondegenerate for $h > 1$ paramagnetic.

Eigenstates $|n\rangle = \otimes_j |p^{[n]}_{k_j}, p^{[n]}_{-k_j}\rangle$ (Eq. 11), each $\{k,-k\}$ subspace 4-dim. Bogoliubov occupations are constants of motion.

**Section 2.3: Ensembles.** Quantum quench: $|\psi_0\rangle$ ground state of pre-quench Hamiltonian; $|\psi(t)\rangle = e^{-i\hat{H}t}|\psi_0\rangle = \sum_n e^{-iE_n t}c_n|n\rangle$ (Eq. 13). Observables after relaxation described by diagonal ensemble $\hat\rho_{DE} = \sum_n |c_n|^2|n\rangle\langle n|$ (Eq. 15).

**Grand canonical** for XX: $\hat\rho^{(XX)}_{GE} = Z^{-1}e^{-\beta(\hat{H}-\mu\hat{N})}$ (Eq. 16). For TFI: $\hat\rho^{(TFI)}_{GE} = Z^{-1}e^{-\beta\hat{H}}$ (Eq. 17).

**GGE** (Eq. 18): $\hat\rho_{GGE} = Z_{GGE}^{-1}\exp[-\sum_k\lambda_k\hat{I}_k]$ with Lagrange multipliers fixed by $\langle\psi_0|\hat{I}_k|\psi_0\rangle = \text{Tr}[\hat\rho_{GGE}\hat{I}_k]$. The set $\{\hat{I}_k\}$ are the integrability-protected conserved quantities.

**Section 2.4: Conserved quantities.** For XX, natural choice is mode-occupation operators $\hat{m}^f_k = \hat{f}^\dagger_k\hat{f}_k$. For TFI, Bogoliubov quasiparticle occupations form the GGE charges. Statistical independence of macroscopic subsystems discussed.

**Sections 3–4: Dynamics and ensembles.** Hard-core boson momentum distribution relaxes to GGE (not grand canonical). Trace distances between subsystem density matrices vanish in thermodynamic limit.

**Section 4.3 (new result).** For TFI, spin-spin correlations computed across the entire system in diagonal ensemble and GGE; trace distance vanishes in thermodynamic limit. Demonstrates GGE applies without tracing out real-space subsystems.

**Section 5: Generalized eigenstate thermalization.** Eigenstates with similar conserved-quantity distributions have similar expectation values of few-body observables. Extension of ETH to integrable systems; supports microscopic origin of GGE success.

## Key Results

1. Review of 10 years of GGE research establishing GGE as powerful tool for equilibrated observables in integrable systems.
2. Fundamental distinction between hard-core bosons (interacting, equilibrate to GGE) and noninteracting fermions (may fail to equilibrate) despite JW mapping.
3. New result: GGE describes spin-spin correlations over the entire transverse-field Ising system; no need for real-space tracing.
4. New result: generalized eigenstate thermalization in TFI (previously shown for XX/hard-core bosons).
5. GGE construction: maximize entropy subject to integrability-enforced conserved charges $\hat{I}_k$.
6. Lagrange multipliers $\lambda_k$ fixed by matching conserved-charge expectation values to initial state.

## Key Equations

| Label | Equation | Reference |
|:------|:---------|:----------|
| XY Hamiltonian | $\hat{H}_{XY} = -J\sum_j[(1+\gamma)\hat{S}^x_j\hat{S}^x_{j+1} + (1-\gamma)\hat{S}^y_j\hat{S}^y_{j+1}] - h\sum_j\hat{S}^z_j$ | Eq. 1 |
| Jordan-Wigner | $\hat{S}^+_j = \hat{f}^\dagger_j e^{-i\pi\sum_{l<j}\hat{f}^\dagger_l\hat{f}_l}$, $\hat{S}^z_j = \hat{f}^\dagger_j\hat{f}_j - 1/2$ | Eq. 4 |
| XX fermionic | $\hat{H}_{XX} = -\tilde{J}\sum_j(\hat{f}^\dagger_j\hat{f}_{j+1} + \text{h.c.}) + \sum_j V_j\hat{f}^\dagger_j\hat{f}_j$ | Eq. 5 |
| Boson momentum distrib. | $\hat{m}_k = (1/L)\sum_{j,l}e^{-i(l-j)k}\hat{b}^\dagger_j\hat{b}_l$ | Eq. 6 |
| TFI Bogoliubov energy | $\epsilon_k = \sqrt{h^2 + 2hJ\cos k + J^2}$ | Eq. 9 |
| TFI vacuum | $\|0\rangle = \prod_{k\in\mathcal{K}^{(+)}}(1/\|v_k\|)\hat\eta_k\hat\eta_{-k}\|\emptyset\rangle$ | Eq. 10 |
| Quench state | $\|\psi(t)\rangle = e^{-i\hat{H}t}\|\psi_0\rangle = \sum_n e^{-iE_n t}c_n\|n\rangle$ | Eq. 13 |
| Observable evolution | $\mathcal{O}(t) = \sum^{E_n\ne E_m}_{n,m}e^{-i(E_n-E_m)t}c^*_m c_n\langle m\|\hat{\mathcal{O}}\|n\rangle + \sum^{E_n=E_m}_{n,m}c^*_m c_n\langle m\|\hat{\mathcal{O}}\|n\rangle$ | Eq. 14 |
| Diagonal ensemble | $\hat\rho_{DE} = \sum_n \|c_n\|^2\|n\rangle\langle n\|$ | Eq. 15 |
| XX grand canonical | $\hat\rho^{(XX)}_{GE} = Z^{-1}e^{-\beta(\hat{H}_{XX}-\mu\hat{N})}$ | Eq. 16 |
| TFI grand canonical | $\hat\rho^{(TFI)}_{GE} = Z^{-1}e^{-\beta\hat{H}_{TFI}}$ | Eq. 17 |
| **GGE density matrix** | $\hat\rho_{GGE} = Z^{-1}_{GGE}\exp[-\sum_k \lambda_k\hat{I}_k]$ | **Eq. 18** |
| GGE matching | $\langle\psi_0\|\hat{I}_k\|\psi_0\rangle = \text{Tr}[\hat\rho_{GGE}\hat{I}_k]$ | §2.3 |

## Relevance to Phonon-Exflation

CRITICAL to the project's S38 permanent result. The Ordered Veil — integrable GGE relic that never thermalizes — IS the GGE construct of this review applied to the Richardson-Gaudin BCS system. Eq. 18 is the mathematical object underlying the project's claim of integrability-protected non-thermal relic (59.8 quasiparticle pairs, $P_{\text{exc}} = 1.000$). The TFI review's demonstration of GGE describing spin-spin correlations over the entire system (without real-space tracing) supports the project's claim that the post-transit substrate's coherent state persists globally rather than requiring subsystem decoherence. Generalized eigenstate thermalization underpins the microscopic justification for the transit-physics interpretation (compound nucleus dissolution, not equilibrium). Direct support for S38 paradigm shift: transit physics, not thermal equilibrium.
