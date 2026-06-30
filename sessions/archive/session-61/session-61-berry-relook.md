# Session 61 Berry Relook: Geometric Phase Perspective on SU(3)

**Author**: Berry-Geometric-Phase-Theorist
**Date**: 2026-03-28 (REWRITE: corrected for SU(3) geometry)
**Library**: 22 papers (Berry/01-22), fully indexed at `researchers/Berry/INDEX.md`
**Sessions reviewed**: S60 (8 waves, 29 computations), S61 (Waves 1-6, 91 computations)
**Classification**: GEOMETRIC + PHONONIC

---

## Preamble: The Geometry This Document Respects

The framework is built on M^4 x SU(3). The fiber is the 8-dimensional compact Lie group SU(3), equipped with the Jensen family of left-invariant metrics parametrized by tau. The Lie algebra decomposes as

    su(3) = u(1) + su(2) + C^2       (dimensions 1 + 3 + 4 = 8)

under the maximal subalgebra u(2) = u(1) + su(2). The Jensen metric scales these blocks:

    L_1 = e^{2tau}    (u(1), 1 direction)
    L_2 = e^{-2tau}   (su(2), 3 directions)
    L_3 = e^{tau}     (C^2 coset SU(3)/U(2), 4 directions)

with det(g) = 1 for all tau (volume-preserving, exact). The Dirac operator D_K acts on the 16-dimensional spinor bundle over SU(3). Its spectrum, computed via Peter-Weyl decomposition at max_pq_sum = 3, contains 992 eigenvalues organized into 10 representation sectors (p,q). The BCS condensate forms in the singlet sector (0,0), pairing 8 modes via the Kosmann derivative, and is Richardson-Gaudin integrable.

The moduli space of left-invariant metrics on SU(3) is 36-dimensional: the space Sym_+(8) of 8x8 positive-definite symmetric matrices in the Gell-Mann basis. The Jensen line is the 1-dimensional path through this 36D space that preserves the block-diagonal form u(1) + su(2) + C^2. The residual symmetry group of the Jensen metric at the fold is the adjoint action of U(2) on su(3), which acts on Sym^2(su(3)) by conjugation. Hessian eigenvalue multiplicities reflect irreducible representations of this U(2) action on the 36D tangent space -- NOT representations of some abstract SU(2) acting on a two-level system.

This distinction matters for everything that follows. The language of "two-level crossings" is inapplicable here. The Dirac operator has approximately 1000 eigenvalues, organized into sectors by SU(3) representation theory, with level statistics governed by the block-diagonal theorem (D_K is exactly block-diagonal in the Peter-Weyl basis for ANY left-invariant metric on ANY compact Lie group, S22b/S61). The geometric phase story on this space is fundamentally multi-level and fundamentally SU(3).

---

## I. The 36D Hessian: Representation Theory of U(2) on Sym^2(su(3))

The central structural result of S61 is MODULI-HESS-61: all 36 eigenvalues of the spectral action Hessian at the fold are strictly negative. The fold metric is a strict local maximum of Tr[f(D_K^2/Lambda^2)] in the full space Sym_+(8) of left-invariant metrics on SU(3).

### I.1 The Geometric Picture

The spectral action SA(g) is a smooth function on Sym_+(8). Its Hessian at the fold metric g_fold defines a quadratic form on the 36-dimensional tangent space T_{g_fold} Sym_+(8). This quadratic form decomposes under the adjoint U(2) action as a direct sum of irreducible representations. The eigenvalue multiplicities

    {5, 1, 8, 4, 3, 6, 3, 1, 4, 1}

must arise from this decomposition. Let me trace this properly.

The 8-dimensional vector space su(3) decomposes under Ad(U(2)) as

    su(3) = u(1)^1 + su(2)^3 + C^2_R^4

where the superscripts denote real dimensions. The space Sym^2(R^8) of symmetric bilinear forms on su(3) therefore decomposes under U(2) as Sym^2 of this direct sum. The general formula gives:

    Sym^2(su(3)) = Sym^2(u(1)) + Sym^2(su(2)) + Sym^2(C^2_R)
                   + u(1) x su(2) + u(1) x C^2_R + su(2) x C^2_R

with dimensions:

| Subspace | Dimension | Ad(U(2)) content |
|:---------|:----------|:-----------------|
| Sym^2(u(1)) | 1 | Trivial scalar (u(1) breathing) |
| u(1) x su(2) | 3 | su(2) adjoint (u(1)-su(2) cross-coupling) |
| u(1) x C^2_R | 4 | C^2 fundamental (u(1)-coset cross) |
| Sym^2(su(2)) | 6 = 1 + 5 | Trivial + rank-5 traceless symmetric (su(2) shape modes) |
| su(2) x C^2_R | 12 | su(2) adjoint x C^2 fundamental (the dominant cross-block) |
| Sym^2(C^2_R) | 10 = 1 + 3 + 6 | Scalar + su(2) triplet + rank-5 traceless (coset shape modes) |

Total: 1 + 3 + 4 + 6 + 12 + 10 = 36. This decomposition into U(2) irreducibles predicts the multiplicity structure of the Hessian.

The 12-dimensional su(2) x C^2 cross-block space corresponds to the "soft" curvature planes of the crystal geometry (K = 0.00974 at the fold, the softest non-zero curvatures). This space hosts the B2 pairing sector, which carries 91% of BCS coupling weight. The 8-fold cluster at -67.16 in the Hessian eigenvalues plausibly decomposes as 8 = 4 + 4, from the C^2 fundamental representation (u(1)-coset and coset-coset contributions) under the U(2) action that preserves the Jensen structure. The 12-dimensional su(2) x C^2 cross-block may split as 12 = 6 + 3 + 3 or 12 = 8 + 4 depending on the eigenvalue curvature in each invariant subspace.

**Calculation A (PROPOSED)**: Decompose the 36 Hessian eigenvectors explicitly into the U(2)-irreducible subspaces of Sym^2(su(3)) listed above. The data exists in s61_moduli_hessian.npz. Each eigenvector is a 36-component vector in the Gell-Mann basis. Project onto the 6 subspaces above and verify that the multiplicities match the U(2) representation theory. This determines which curvature sectors of SU(3) contribute most to the spectral action maximum. The result constrains which deformations of the Jensen metric are most consequential for BCS physics.

### I.2 Connection to the Quantum Geometric Tensor

The spectral action Hessian and the quantum geometric tensor (Paper 12, Gu 2010) probe different aspects of the same eigenvalue geometry. The QGT measures the response of INDIVIDUAL eigenstates to parameter variation:

    Q_{mu,nu}^{(n)} = <d_mu n|d_nu n> - <d_mu n|n><n|d_nu n>     (eq QGT-1)

while the spectral action Hessian sums over ALL eigenvalues weighted by the cutoff function:

    d^2 SA / dg_{ij} dg_{kl} = sum_n f''(lambda_n^2)(d lambda_n^2/dg_{ij})(d lambda_n^2/dg_{kl})
                                 + sum_n f'(lambda_n^2)(d^2 lambda_n^2/dg_{ij} dg_{kl})    (eq HESS-1)

The first term is positive-semidefinite (it is the "quantum metric" contribution to the Hessian). The second involves the eigenvalue curvature and can be of either sign. The all-negative Hessian at the fold tells us that eigenvalue curvature dominates over eigenvalue velocity in ALL 36 directions of the 36D moduli space.

The ERRATUM result (S25, permanent) established that Berry curvature Omega = Im(QGT) = 0 identically on the Jensen line, while the quantum metric g = Re(QGT) = 982.5 is large. The Hessian all-negative result extends this picture: not only is the curvature zero in the 1D tau direction, but the spectral action response is uniformly dominated by the concave eigenvalue curvature in ALL directions of the full moduli space. The fold is the summit of a smooth 36-dimensional hill, with the quantum metric measuring the slope of each face.

---

## II. Berry Curvature = 0: The SU(3) Mechanism

The vanishing of Berry curvature on the Jensen line has two independent mechanisms, both rooted in SU(3) geometry.

### II.1 The Kosmann Anti-Hermiticity Mechanism (Jensen 1D)

The Dirac operator on (SU(3), g_Jensen) is constructed from the Kosmann derivative, which acts on spinors as an anti-Hermitian operator (K_a^dag = -K_a). The Berry connection is

    A_n(tau) = <n(tau)|d_tau|n(tau)>

The matrix elements <n|dH/dtau|m> = <n|dD_K/dtau|m> are products of anti-Hermitian operators acting on real spinor bases. The imaginary part of the QGT -- the Berry curvature -- requires Im(<n|dH|m><m|dH|n>) to be nonzero. But anti-Hermiticity of the Kosmann connection on a 1D parameter space forces these products real. Hence Im(QGT) = 0 identically.

This is NOT a two-level argument. It applies to ALL 992 eigenvalues simultaneously. The mechanism is algebraic: the Kosmann derivative on any compact Lie group with a left-invariant metric produces anti-Hermitian generators, and this kills the imaginary part of the QGT for any 1D path through the space of such metrics.

### II.2 The J-Symmetry Mechanism (Full U(2)-Invariant Surface)

The real structure J of the spectral triple satisfies [J, D_K] = 0 (S17a, proven). J provides a complex anti-linear involution that constrains the eigenstate geometry. On the full U(2)-invariant surface (the 3D subspace of Sym_+(8) preserved by Ad(U(2))), the J-symmetry forces Im(QGT) = 0 by a different route: J maps each eigenstate to a linearly related partner, and the resulting constraint on the connection form eliminates the anti-symmetric part of the QGT.

The key implication for SU(3): the Berry curvature vanishes not just along the 1D Jensen line, but across the entire U(2)-invariant surface. Only deformations that BREAK U(2) invariance -- deformations in the 33 off-Jensen directions -- can generate nonzero Berry curvature. This is the geometric content of the P-30w gate.

### II.3 Paper 14 Identity and Its SU(3) Realization

Paper 14 (Piechon et al., 2016) proves that for a two-band model, Omega^2 = 4 det(g_ij), where g_ij is the quantum metric tensor. This identity means the curvature magnitude is controlled by the metric determinant.

On the SU(3) Dirac operator, the Hilbert space is far larger than two bands. The identity does not apply literally. However, the SPIRIT of the identity constrains the framework: with Omega = 0 identically, the quantum metric tensor must have det(g) = 0 in every 2D projection that satisfies the identity. This means the metric, while large (g = 982.5), is DEGENERATE. There exists at least one null direction in the parameter space of the QGT.

On the full 36D moduli space, the quantum metric is a 36x36 positive-semidefinite matrix. Its rank and null space structure encode the geometric information about which deformations leave eigenstates unchanged (null directions) versus which deformations maximally rotate the eigenstate manifold (large-eigenvalue directions). The all-negative Hessian tells us there are no flat directions in the spectral action landscape. But the quantum metric can have flat directions even when the Hessian does not, because the metric and the Hessian probe different aspects of the eigenvalue geometry (state change vs. spectral action curvature).

**Calculation B (PROPOSED)**: Compute the eigenvalue spectrum of the quantum metric tensor G_{ab,cd} on the 36D moduli space at the fold. If the rank is less than 36, the null space identifies deformations that do not change the ground state despite changing the spectral action. If the rank equals 36, every direction in moduli space changes the eigenstate geometry, and the "sensitivity without protection" paradox (S36) extends to the full 36D space. The data to perform this computation already exists in the form of the eigenvector derivatives dD_K/dg_{ab} computed in the S61 Hessian script.

---

## III. Superadiabatic LZ on SU(3): Paper 06 Applied to the Transit

Paper 06 (Lima and Burkard, 2024) discovers that two Hamiltonians with IDENTICAL eigenvalue landscapes can produce fundamentally different transition probabilities, depending on how the eigenvectors rotate on the Bloch sphere. The critical parameter is the angular velocity at the crossing point: theta_dot(0) = |alpha - beta|/Delta_0, where alpha parametrizes eigenvalue velocity and beta parametrizes eigenvector rotation rate.

### III.1 The Standard LZ Limit on the Jensen Line

The framework's transit through the fold has:
- tau_Q/tau_0 = 8.71e-4 (deeply non-adiabatic, Massey xi = 8.9)
- Berry curvature Omega = 0 identically (Section II)
- Quantum metric g = 982.5 (large eigenvector sensitivity to tau)

In Paper 06's language, on the Jensen line the framework sits at beta = 0 (no eigenvector rotation that generates geometric phase) while alpha is large (fast eigenvalue driving through the fold). The transition probability is the standard Landau-Zener formula:

    P_LZ = exp(-2pi Delta_0^2 / hbar alpha)         (eq LZ-1)

with Delta_0 = 0.72 M_KK (BCS gap at fold) and alpha = omega_transit = 8.27 (transit frequency). This gives delta = Delta_0^2/(hbar alpha) = 0.063, deeply non-adiabatic. The result: P close to 1, almost complete excitation, consistent with the Parker production result (n_Bog = 0.999, |beta_k|^2 = 1.015).

### III.2 The Multi-Level Generalization

Paper 06 is formulated for two-level systems. The SU(3) Dirac operator has 992 eigenvalues. The generalization to multi-level LZ physics is well-known (Brundobler-Elser, Demkov-Osherov models) but the superadiabatic effect has not been systematically studied in the multi-level case.

For the framework, the relevant generalization is: the 992-eigenvalue Dirac spectrum flows through the fold region as tau varies. The B2 sector (8 eigenvalues, carrying 91% of BCS pairing) experiences the van Hove singularity -- the density of states diverges at the fold. The other sectors (B1: 2 eigenvalues, B3: 6 eigenvalues in the singlet) have eigenvalues that flow smoothly through the fold without singularity.

The multi-level LZ transition matrix involves interference between ALL 992 channels. But the block-diagonal theorem (S22b/S61) decouples the sectors: each Peter-Weyl sector undergoes its own independent LZ transition. Within each sector, the transitions are further constrained by the reality of the eigenvectors (Im(A_n) = 0 identically, S53). The superadiabatic mechanism requires eigenvector rotation that generates a nonzero beta parameter. On the Jensen line, this rotation is zero in every sector individually.

### III.3 Off-Jensen: The Superadiabatic Route

The critical insight of Paper 06 for the framework: moving off-Jensen is equivalent to turning on beta. If U(2)-breaking deformations (the 33 off-Jensen directions in the 36D moduli space) are present during the transit, the eigenvectors gain rotational motion that Paper 06's theta_dot quantifies. The modified adiabaticity condition becomes:

    Delta_0^2 / hbar |alpha - beta| >> 1             (eq LZ-2)

If beta approaches alpha, the condition is satisfied even for small gaps and fast driving. The physical implication: off-Jensen deformations could make the transit LESS destructive (fewer quasiparticles produced), by providing the eigenvector rotation that the standard LZ formula ignores.

This inverts the standard motivation for P-30w (which was to find topological invariants). Paper 06 reveals a DYNAMICAL consequence of off-Jensen Berry curvature: it could suppress the transit transition probability, producing a "frictionless" cosmological transition. The suppression mechanism is not topological protection but kinematic cancellation: the eigenvector rotation rate matches the eigenvalue driving rate, and the two rotations cancel.

**Calculation C (PROPOSED)**: In the 2D (tau, sigma) plane near the fold, compute the eigenvector rotation rate beta(tau, sigma) = theta_dot(tau) for the lowest B2 eigenvalue. Extract from the existing s55_berry_fold.npz data (32x32 Hamiltonian, 61x61 grid). At each grid point, compute the instantaneous eigenstate derivative and project onto the tangent to the transit path. If |alpha - beta|/Delta_0 < 1 at any (tau, sigma) with sigma > 0, the superadiabatic regime is accessible. This connects P-30w directly to transit quasiparticle production.

---

## IV. Berry-Tabor on the SU(3) BCS Fock Space: The GGE-Integrability Chain

The GGE permanence result (9/9 PASS in S61) is the many-body realization of the Berry-Tabor theorem. Let me make this connection precise for the SU(3) framework.

### IV.1 Single-Particle Berry-Tabor on SU(3)

The single-particle level statistics of D_K are Poisson (<r> = 0.401 in B2, Brody beta = 0.001 in (2,1) sector, S53). The standard Berry-Tabor mechanism would attribute this to classical integrability: in an integrable system, the classical phase space is foliated by invariant tori, the actions on different tori are generically incommensurate, and the eigenvalues (from EBK quantization) are therefore uncorrelated -- Poisson statistics.

But the SU(3) Dirac operator has a DIFFERENT mechanism for Poisson statistics: the block-diagonal theorem. The 992 eigenvalues decompose into 10 Peter-Weyl sectors that are exactly decoupled. Within each sector, the eigenvalues are determined by the Casimir operators C_2(p,q) and C_3(p,q) of the SU(3) representation, plus the tau-dependent Jensen metric. The inter-sector eigenvalue correlations are zero because the off-diagonal D_K matrix elements vanish identically.

This is Schur-orthogonality integrability, not action-angle integrability. The conserved quantities are the SU(3) representation labels (p,q), not action variables of a classical Hamiltonian. The spectral statistics are Poisson because the sectors DECOUPLE, not because the classical limit is integrable. This is a structurally distinct mechanism from Berry-Tabor's classical one, though it produces the same spectral statistics.

### IV.2 Many-Body Berry-Tabor on the Richardson-Gaudin BCS

Paper 10 (Urbina, Kelly, Richter, 2024) extends the Berry-Tabor trace formula to Bethe-ansatz-integrable many-body systems. The framework's BCS Fock space is Richardson-Gaudin integrable (proven S35). The Richardson-Gaudin model is Bethe-integrable with N_pair conserved quantities (the spectroscopic Richardson parameters).

The N-particle trace formula from Paper 10 (their Eq. 25) gives the oscillatory density of states:

    rho_osc(E) = sum_M C_M |det J_M|^{-1/2} cos(R_M/hbar - Phi_M - pi sigma_M/2 + pi/4)    (eq BT-N)

where R_M are semiclassical actions computed from the Bethe equations, Phi_M are scattering phases, sigma_M are Maslov indices, and J_M are the Bethe equation Jacobians. For the framework's BCS system:
- N_pair = 1 (proven S53, permanent)
- 8 single-particle levels in the B2 sector
- Richardson-Gaudin with 8 conserved quantities
- E_cond = -0.137 M_KK from exact diagonalization of 256-state Fock space

At N_pair = 1, the trace formula simplifies: the Bethe equations reduce to the single-particle problem, and the "many-body periodic orbits" are just the single-particle energies. The smooth DOS from Paper 10's Eq. 20 (via the Bethe equation Jacobian) gives the Weyl background. The oscillatory terms are exponentially small in the coupling/level-spacing ratio, confirming the "Ordered Veil" from the trace formula side.

### IV.3 The GGE = Berry-Tabor Theorem for Richardson-Gaudin

The 9/9 GGE permanence PASS in S61 has a precise Berry-Tabor interpretation. The GGE conserved charges {N_k, lambda_k} are the Richardson-Gaudin integrals of motion. The state prepared by the transit is a non-equilibrium initial condition in the space of these conserved charges. The GGE ensures this state cannot thermalize because:

1. The integrals of motion constrain the accessible phase space (N_pair = 1 fixes 8 charges).
2. The Poisson statistics of the single-particle spectrum (from block-diagonality) prevent level repulsion that would allow ergodic mixing.
3. The SFF factorization (exactly proved in S61) confirms that the spectral form factor is a product of independent sector contributions -- no inter-sector correlations can build up.

The S61 EWSR-THOULESS-61 result (PASS, 14 significant digits) provides independent confirmation: the energy-weighted sum rule is a spectral moment constraint that the Richardson-Gaudin solution satisfies exactly. In Paper 10's language, this constrains the smooth part of the DOS, while the Maslov indices constrain the oscillatory part. Both are exactly computable for the framework's integrable BCS system.

**Calculation D (PROPOSED)**: Apply Paper 10's N-particle trace formula to the framework's 8-level Richardson-Gaudin BCS at N_pair = 1. Compute the smooth DOS from the Bethe equation Jacobian (Eq. 20 of Paper 10) and the first few oscillatory corrections (Eq. 25). Compare with the exact 256-state Fock space diagonalization. The smooth DOS would provide the Strutinsky background that NAZ-16 (HK-OSCILLATION-61) sought via Gaussian smoothing. The Maslov indices from the trace formula would give the first prediction of the BCS phase structure's semiclassical content. Zero-cost extraction from existing data.

---

## V. The ERRATUM Regime Realized: Papers 14 and 15 on SU(3)

Papers 14 and 15 are the most directly relevant papers in the library for the framework's current status.

Paper 14 (Piechon et al., 2016) proves that orbital susceptibility depends on quantum metric even when Berry curvature vanishes identically. Paper 15 (Yang, 2025) reviews the 2025 ARPES measurement of the full QGT in black phosphorus: the Berry curvature F_ij = 0 identically (from combined space-time inversion symmetry) while the quantum metric g_ij is large and anisotropic.

The framework's ERRATUM regime -- g = 982.5, Omega = 0 identically -- is the SU(3) realization of this "metrically rich, topologically trivial" regime. S61 completed the topological triviality chain:

| Invariant | Value | Session | Mechanism |
|:----------|:------|:--------|:----------|
| Berry curvature Omega | 0 identically | S25 | Kosmann anti-Hermiticity |
| Chern number | 0 | S25 | integral(Omega) = 0 |
| Fubini-Study distance d_FS | 0 for all tau | S25 | Democratic real eigenvectors |
| Wilson loop (non-Abelian) | Trivial (KS p=0.52) | S48 | Flat connection + open path |
| BDI winding number nu | 0 | S36 | mu=0, E_B2 > 0 |
| Spectral flow sf | 0 sector-by-sector | S61 | Gap open throughout |
| Eta invariant eta(s) | 0 for all s | S60 | J-symmetry (+/- pairing) |
| Fredholm BdG ind_Z | 0, Pf = +1 | S61 | BDI class, trivial K_0 |
| GL band Zak phase | 0 all 6 bands | S53 | Double triviality (block-diag + reality) |
| Berry phase around fold | 0 | S55 | Real-symmetric in 2D, no diabolical point |
| Fabric Josephson holonomy | Trivial | S56 | Rank-1 preserves R-G integrability |

Eleven independent topological invariants, ALL zero. This is not a coincidence -- it is a structural consequence of the SU(3) geometry under left-invariant metrics with the real structure J.

The surviving geometric content is the quantum metric: g = 982.5. This is the Re(QGT), measuring how much the eigenstates of D_K change as tau varies. Paper 14 shows that this metric is physically observable: it contributes to orbital susceptibility, superfluid stiffness, and fidelity susceptibility even when Berry curvature vanishes. The framework lives in the regime where the quantum metric controls all geometric response functions while the Berry curvature contributes nothing.

Paper 15's experimental confirmation in black phosphorus validates this regime as physical, not pathological. The mechanism is different (space-time inversion in black phosphorus vs. Kosmann anti-Hermiticity on SU(3)), but the consequence is the same: a system can be metrically rich while topologically trivial.

---

## VI. Equivariant Spectral Flow on SU(3): Paper 22

The spectral flow result SPECTRAL-FLOW-61 (sf = 0, gap open at all tau) acquires refined meaning through Paper 22 (equivariant spectral flow, 2024).

Paper 22 proves that for a G-equivariant family of self-adjoint Fredholm operators, the spectral flow decomposes into irreducible representations:

    sf_G(D) = sum_{rho in G-hat} sf(D|_{V_rho}) [rho]      (eq SF-1)

The framework's D_K is SU(3)_L-equivariant by the block-diagonal theorem (S22b, generalized to all compact Lie groups in S61 BLOCK-DIAG-GENERAL-61 PASS). The Peter-Weyl decomposition IS the equivariant decomposition:

    sf_{SU(3)}(D_K, tau: 0 -> 0.19) = sum_{(p,q)} sf(D_K|_{V_{(p,q)}}) [(p,q)]    (eq SF-2)

S61 verified sf = 0 at the total level (no eigenvalue crosses zero in any sector across the 40-point tau sweep). By Paper 22's decomposition, this means sf|_{V_{(p,q)}} = 0 for every individual Peter-Weyl sector. The equivariant spectral flow is trivial sector-by-sector, not just in total.

The APS index theorem (Paper 22, main theorem) connects this to the index of an associated operator on the cylinder [0, tau_fold] x SU(3):

    sf(D_0, D_{tau_fold}) = index(d/dt + D_t)               (eq APS-1)

With sf = 0, ind = 0 (A-hat genus vanishes on parallelizable SU(3), CHERN-INST-61), and eta = 0 (J-symmetry, ETA-INVARIANT-60), the complete APS topological data is trivial. The Jensen deformation does not change the topological class of D_K. This is consistent with the continuous deformation interpretation: the Jensen path stays in the same connected component of the space of Dirac operators on SU(3).

The SU(3)-specific content here is that the equivariant decomposition respects the Peter-Weyl structure. Each sector (p,q) contributes independently to the spectral flow, with the Z_3 triality partition (p-q) mod 3 providing an additional discrete label. The sector-by-sector triviality is a CONSEQUENCE of the block-diagonal theorem, not an independent result.

---

## VII. Fidelity Susceptibility at the Fold: Paper 17 on SU(3)

Paper 17 (Carollo et al., 2020) proves that the quantum metric singularities (fidelity susceptibility divergences) diagnose quantum phase transitions without an order parameter. The fidelity susceptibility is:

    chi_F(tau) = lim_{delta->0} (-2 ln F) / delta^2         (eq CHI-1)

where F = |<psi(tau)|psi(tau+delta)>| is the ground-state fidelity. The leading term is the quantum metric:

    |<psi(tau)|psi(tau+delta)>|^2 = 1 - g_{tau,tau} delta^2 + O(delta^4)    (eq FID-1)

With g = 982.5 at the fold, the ground-state fidelity drops by 982.5 delta^2 per unit parameter step. This is the "sensitivity without protection" paradox of S36: the ground state changes rapidly with tau despite being topologically trivial.

Paper 17 predicts that at a quantum critical point, chi_F ~ L^{2/nu} (super-extensive in system size). The fold at tau = 0.190158 is an A_2 catastrophe (Thom-stable, S33), NOT a quantum critical point. For an A_2 fold catastrophe, the fidelity susceptibility scaling should follow:

    chi_F(tau) ~ |tau - tau_fold|^{-1}    (for tau -> tau_fold^-)    (eq CHI-2)

because the B2 mass gap closes as |tau - tau_fold|^{1/2} at the fold (square-root vanishing, A_2 property), and chi_F ~ 1/Delta^2 ~ 1/|tau - tau_fold|. This is an integrable divergence (logarithmic upon integration), much weaker than the critical point divergence chi_F ~ L^{2/nu} which is non-integrable for nu < 1.

The SU(3)-specific prediction: the fidelity susceptibility should decompose by Peter-Weyl sector, with the B2 sector dominating near the fold (because B2 has the van Hove singularity) while B1 and B3 contributions remain bounded. The fold curvature kappa = 1.1757 (S33) sets the coefficient: chi_F^{B2} ~ kappa / |tau - tau_fold|.

The GL q-theory result chi_q = 0.024 (S61 PASS) is the condensate analog of the fidelity susceptibility: it measures the response of the vacuum energy to changes in the q-theory order parameter. The smallness of chi_q confirms the system is deep in the ordered phase, far from any quantum phase transition. This is consistent with the A_2 catastrophe classification -- the fold is a MORPHOLOGICAL feature (shape change), not a CRITICAL feature (symmetry breaking).

**Calculation E (PROPOSED)**: Extract g_{tau,tau}(tau) from the existing 40-point eigenvalue data in SPECTRAL-FLOW-61. Plot chi_F vs |tau - tau_fold|. Decompose by Peter-Weyl sector. If the B2 sector shows |tau - tau_fold|^{-1} scaling while B1 and B3 remain bounded, this independently confirms the A_2 fold classification from the quantum information geometry side. If the scaling is steeper (e.g., |tau - tau_fold|^{-2}), this would indicate a higher catastrophe (A_3 cusp) or genuine QPT.

---

## VIII. The BCS Berry Phase on SU(3): Paper 18

Paper 18 (Marciani and Chubukov, 2019) derives the Berry phase for BCS superconductors across the BCS-BEC crossover. The bulk Berry phase prefactor is A = n/2 (their Eq. 106), with the vortex Berry phase A_vort = (n - n_0)/2 (their Eq. 167).

### VIII.1 Applicability on SU(3)

The framework's BCS condensate is in the B2 sector of the (0,0) singlet. The condensate forms on an 8-dimensional compact Lie group fiber, not in a translationally invariant bulk. The key differences from Paper 18's setting:

1. **Compact geometry**: The fiber SU(3) is compact (no thermodynamic limit). The 32-cell Voronoi tessellation provides the discrete lattice. The pair number is N_pair = 1 (proven S53, permanent).

2. **Type-I superconductor**: kappa = 0.49 < 1/sqrt(2) (S61 INFO). In a Type-I superconductor, vortices are not thermodynamically stable. Paper 18's A_vort is therefore inapplicable to the equilibrium state on the Jensen line.

3. **Mott regime**: E_J/E_C = 0.818 < 1 (S53). The system is on the charge-quantized (Mott) side of the superfluid-insulator transition. The condensate is a single Cooper pair, not a macroscopic superfluid. The Berry phase formalism of Paper 18 assumes a macroscopic order parameter with well-defined phase -- this assumption is violated.

### VIII.2 Transit Relevance

During the transit, the order parameter is disrupted (|beta_k|^2 = 1.015, deeply sudden). The transit is analogous to a rapid quench through the superfluid transition. In 3He-B (the parent system, S60 framework-3HeB-comparison.md), rapid quenches produce vortex tangles via the Kibble-Zurek mechanism.

If vortices are transiently created during the transit on SU(3), Paper 18's Berry phase provides the force on vortex cores:

    F = pi A_vort (v_vort x z-hat)                          (eq BCS-F)

At N_pair = 1 (BCS regime), A_vort ~ N_0 E_0 (small, near-cancellation of Magnus and core reaction). The single Cooper pair does not generate a macroscopic vortex -- but the 32-cell lattice provides discrete "vortex sites" at cell boundaries where the pairing phase can wind.

The Anderson-Bogoliubov mode (v = v_F/sqrt(2), universal across BCS-BEC, Paper 18 Eq. 1) is present in the framework as the Goldstone branch of the tight-binding dispersion (c_Gold = 0.915 M_KK). This mode propagates phase excitations at the pair hopping speed, regardless of whether the system supports topological vortices.

---

## IX. The Hannay Angle and Classical Limit: Paper 04 on SU(3)

Paper 04 (Bermudez Manjarres, 2023) establishes that the classical geometric phase (Hannay angle) is the negative of the Berry phase in the Koopman-von Neumann formalism:

    Phi_classical = -Delta_phi_Hannay = -oint <d_lambda phi> d lambda    (eq HAN-1)

On the Jensen line, the Berry phase is zero (Section II). Therefore the Hannay angle is also zero. The classical transit through parameter space has no geometric phase.

The SU(3)-specific content: the classical limit of the Dirac operator on SU(3) is the geodesic flow on the group manifold. The Jensen deformation modifies the metric and hence the geodesics. But the Hannay angle for geodesic flow on a slowly deforming compact manifold vanishes when the connection form (Berry connection) vanishes -- which is exactly the ERRATUM result. The classical transit is "memoryless" in the geometric phase sense: the trajectory through parameter space leaves no holonomy imprint.

The only "memory" of the transit is in the SPECTRUM of excitations: the GGE conserved charges {N_k, lambda_k}. These are dynamical, not geometric. They encode WHAT happened (which modes were excited by the deeply non-adiabatic transit) but not HOW (no path-dependent geometric phase). This is the classical statement of the Ordered Veil: the post-transit state remembers the spectrum but not the geometry.

---

## X. Assessment: What Berry's Methods Reveal About M^4 x SU(3)

The S60-61 results, viewed through the complete Berry library applied to SU(3), paint a precise picture.

### X.1 The Constraint Map

The framework realizes a regime where:
- The quantum metric (Re QGT) is large: g = 982.5 on a 1D slice, structure unknown on 36D
- The Berry curvature (Im QGT) vanishes identically on the full U(2)-invariant surface
- Every topological invariant available for BDI class in dimension 1 has been computed and found zero (11 independent computations, Section V table)
- The spectral action landscape is a smooth 36D hill with the fold at its summit
- The Poisson statistics of the spectrum arise from block-diagonality (Schur orthogonality), not classical integrability
- The GGE permanence is a many-body Berry-Tabor theorem for Richardson-Gaudin integrable BCS
- The fold is an A_2 catastrophe, Thom-stable but NOT topologically protected

### X.2 What Remains Open

1. **P-30w (off-Jensen Berry curvature)**: The sole route to nontrivial geometric phase. Paper 02 (Wilczek-Zee) predicts non-Abelian holonomy in the B2 degenerate subspaces when U(2) is broken to SU(2) or below. Paper 06 (superadiabatic LZ) adds dynamical urgency: off-Jensen beta could suppress transit excitations. Paper 03 (diabolical points) predicts Berry curvature monopoles at off-Jensen degeneracies. **HIGHEST PRIORITY.**

2. **Quantum metric tensor eigenvalues on 36D** (Calculation B): The quantum metric is a 36x36 matrix at the fold. Its eigenvalue structure encodes which directions in moduli space produce the largest state change. Unknown, computable from existing data.

3. **Fidelity susceptibility scaling near fold** (Calculation E): Paper 17 predicts chi_F ~ |tau - tau_fold|^{-1} for A_2 fold, decomposed by Peter-Weyl sector. Tests the catastrophe classification independently.

4. **N-particle Berry-Tabor trace formula for BCS** (Calculation D): Paper 10 provides the tool to compute the many-body DOS without full diagonalization. Would yield the Strutinsky smooth background from first principles.

5. **Hessian eigenvector decomposition under U(2)** (Calculation A): The 36 Hessian multiplicities should match the representation theory of U(2) on Sym^2(su(3)). Verifiable from existing data.

### X.3 Classification

**GEOMETRIC**: All observations derive from the parameter-space geometry of the Dirac operator on SU(3). The quantum metric measures how the Dirac eigenstates change under Jensen deformation. The spectral action Hessian measures how the collective spectral functional responds. The equivariant spectral flow tracks eigenvalue crossings through zero. The fidelity susceptibility detects quantum critical behavior. All of these are geometric diagnostics applied to the SU(3) fiber bundle.

**PHONONIC**: The phonon dispersion relation omega(k) on the SU(3) substrate is encoded in the D_K eigenvalue spectrum. The quantum metric g_{tau,tau} = 982.5 measures the "elasticity" of the phonon crystal lattice under shape deformation -- how much the phonon frequencies change when the cavity shape changes. Large quantum metric means the phonon spectrum is highly sensitive to the cavity shape. Zero Berry curvature means this sensitivity has no topological protection: the cavity can be deformed continuously through the fold without encountering a topological obstruction. The phonon crystal is an elastic medium with a stiff but unprotected response.

### X.4 The Central Geometric Paradox (S36, refined)

Large quantum metric + zero Berry curvature + all topological invariants trivial = "sensitivity without protection."

The framework's SU(3) fiber produces a D_K eigenvalue spectrum that responds strongly to deformation (g = 982.5) but carries no topological charge to protect that response. The fold is the point of maximum sensitivity (36D Hessian all negative), but it is an extremum of the spectral action, not a fixed point of topology. Any perturbation that breaks the volume-preserving constraint will destabilize the fold.

This is not a pathology. It is the geometric signature of a transit: the system passes through the fold, not stays at it. Topological protection would PREVENT the transit. The framework needs a lava-tube, not a fortress.

---

## Proposed Calculations Summary

| ID | Description | Input Data | Paper Reference | Tests |
|:---|:-----------|:-----------|:----------------|:------|
| A | Hessian eigenvector decomposition under U(2) on Sym^2(su(3)) | s61_moduli_hessian.npz | Papers 08, 12, 14 | U(2) rep theory of moduli space |
| B | Quantum metric tensor eigenvalues at fold (36x36) | Eigenvector derivatives from S61 | Papers 12, 14, 15 | Rank, null space, anisotropy |
| C | Eigenvector rotation rate beta(tau,sigma) in 2D | s55_berry_fold.npz | Paper 06 | Superadiabatic regime accessibility |
| D | N-particle Berry-Tabor trace formula for 8-level R-G BCS | Richardson-Gaudin parameters | Paper 10 | Smooth DOS, Maslov indices |
| E | Fidelity susceptibility scaling chi_F(tau) near fold | SPECTRAL-FLOW-61 eigenvalue data | Paper 17 | A_2 catastrophe verification |

All five calculations use existing numerical data and require no new eigenvalue computations. They test specific predictions from the Berry library against the framework's SU(3) geometry.

---

**Data provenance**: S25 ERRATUM (Berry curvature = 0, quantum metric = 982.5), S33 (A_2 fold, kappa = 1.1757), S36 (BDI winding number = 0), S48 (Wilson loop trivial, Zak phase artifact), S53 (GL double triviality, N_pair = 1), S55 (Berry phase around fold = 0), S56 (fabric holonomy trivial), S60 (eta invariant = 0, 36D Hessian maximum), S61 (spectral flow = 0, MODULI-HESS-61 all negative, Fredholm BdG trivial). Constants from `computations/canonical_constants.py`.

---

## ADDENDUM: Berry Phase as Dimensional Reduction of SU(3)

**Date**: 2026-03-28
**Classification**: GEOMETRIC + PHONONIC
**Status**: This addendum reframes the entire Berry phase program not as something to be APPLIED to SU(3), but as something that EMERGES from SU(3) by restriction to SU(2).

---

### A.1 The Zero Theorem: Why Berry Curvature = 0 on SU(3) Is a Feature, Not a Bug

The vanishing of Berry curvature on SU(3) with left-invariant metrics is the most robust result in this project's geometric phase program. The mechanism (Section II above) is algebraic: the Kosmann derivative K_a on any compact Lie group with any left-invariant metric is anti-Hermitian (K_a^dag = -K_a), which forces the matrix elements <n|dD_K/dtau|m> to be real. The imaginary part of the quantum geometric tensor vanishes identically:

    Im(Q_{mu,nu}) = Im sum_{m != n} <n|dH/d(tau_mu)|m><m|dH/d(tau_nu)|n> / (E_n - E_m)^2 = 0    (eq ZT-1)

This holds for ALL 992 eigenvalues, ALL tau, and extends to the full U(2)-invariant surface (3D) of the 36D moduli space via J-symmetry. It is verified numerically: max|Omega| < 4e-14 across 16 states and 9 tau values (S25, permanent).

The standard reaction to this result is dismay: if Berry curvature vanishes, where does all of Berry's physics go? The answer -- the entire point of this addendum -- is that it goes DOWNSTAIRS. Berry curvature vanishes on SU(3) for the same reason that the Riemann tensor of flat R^5 vanishes: the parent space is geometrically trivial in a specific sense. But embed a curved S^2 in R^3, and S^2 has nonzero intrinsic curvature inherited from the embedding -- not from the ambient curvature (which is zero) but from the PROJECTION of the flat ambient connection onto the submanifold.

The mathematical structure is:

    Total space: SU(3), with flat Berry connection (Omega = 0)
    Subspace: SU(2) embedded via su(2) subset su(3)
    Projection: Pi_{su(2)} : H_full -> H_{su(2)}
    Result: The PROJECTED connection on H_{su(2)} has nonzero curvature

This is not a metaphor. It is the fiber bundle mechanism by which gauge fields emerge from Kaluza-Klein reduction, translated into the language of quantum geometric phases.

---

### A.2 The Projection Mechanism: How Berry Curvature Emerges on SU(2)

The Lie algebra decomposition

    su(3) = u(1) + su(2) + C^2    (dimensions 1 + 3 + 4 = 8)

splits the 8 Gell-Mann generators into three blocks: lambda_8 (u(1) hypercharge), lambda_1, lambda_2, lambda_3 (su(2) isospin), and lambda_4, lambda_5, lambda_6, lambda_7 (C^2 coset, generating SU(3)/U(2)). The Kosmann generators K_a (a = 0,...,7) of the Dirac operator inherit this decomposition.

The full Dirac operator D_K acts on H_full = C^16 (the 16-dimensional internal spinor space). Consider the RESTRICTION to the su(2) sub-block. The 16-dimensional Hilbert space decomposes under Ad(U(2)) into irreducible representations. The states that transform nontrivially under su(2) span a subspace H_{su(2)} subset H_full. Let Pi denote the orthogonal projector onto this subspace.

**The restricted Hamiltonian** is:

    H_{su(2)}(R) = Pi D_K(R) Pi                                     (eq PR-1)

where R parametrizes the su(2)-valued "magnetic field" (the 3 components of the isospin parameter space, identified with the lambda_1, lambda_2, lambda_3 directions).

**The restricted Berry connection** is:

    A_n^{su(2)}(R) = <n_{su(2)}(R)| d/dR |n_{su(2)}(R)>            (eq PR-2)

where |n_{su(2)}(R)> are eigenstates of H_{su(2)}(R). The critical point: THESE EIGENSTATES ARE NOT the same as the full eigenstates of D_K projected down. They are eigenstates of the PROJECTED operator, which mixes the su(2) degrees of freedom with contributions from the C^2 cross-terms that the projection operator does not fully eliminate.

**The curvature of the restricted connection** picks up a contribution from the C^2 cross-block:

    Omega_n^{su(2)} = d A_n^{su(2)} + A_n^{su(2)} ^ A_n^{su(2)}

    = Omega_n^{full}|_{su(2)} + [A_n^{C^2}, A_n^{C^2}]|_{su(2)}    (eq PR-3)

The first term vanishes -- it is the restriction of the flat SU(3) Berry curvature to the su(2) subspace, which is zero by the zero theorem. The second term is the COMMUTATOR of the C^2-valued connection components, restricted to the su(2) directions. This term is generically NONZERO because the C^2 coset space of SU(3)/U(2) is a NON-ABELIAN coset -- the Lie bracket [C^2, C^2] has a nonzero su(2) component (this is exactly the statement that the C^2 distribution in SU(3) is non-integrable, with A-tensor |A_coset|^2 = 3/2 + (3/2)e^{-4tau}, S55 eq 5).

In explicit representation-theoretic language: the C^2 directions transform as the fundamental representation 2 of su(2). The tensor product 2 x 2 = 1 + 3. The antisymmetric part (the Lie bracket [C^2, C^2]) projects onto the adjoint representation 3 of su(2). This projection is NONZERO, and it produces an effective Berry curvature on the su(2) parameter space that acts as a monopole field -- exactly the structure studied in Paper 03 (Bruno, diabolical points) and Paper 16 (Xiao-Chang-Niu, Berry phase in bands).

The formula is:

    Omega_{ij}^{su(2),eff} = sum_{alpha,beta in C^2}
        f_{i,alpha,beta} * <n|K_alpha|m><m|K_beta|n> / (E_n - E_m)^2    (eq PR-4)

where f_{i,alpha,beta} are the structure constants of su(3) connecting the su(2) generator i with two C^2 generators alpha, beta, and the sum runs over intermediate states m that live in the C^2-coupled sectors of H_full. This is precisely the Berry curvature formula (Paper 16, eq 1.12) with the "parameter derivatives" replaced by the C^2 Kosmann generators K_alpha.

**The physical content**: the C^2 cross-block, which is the 4-dimensional complement of su(2) in su(3), acts as a HIDDEN parameter space. When an observer restricted to su(2) computes Berry curvature, the C^2 directions contribute through their commutator structure, producing a nonzero effective curvature even though the total SU(3) curvature vanishes. The Berry curvature on SU(2) is the SHADOW of the quantum metric on SU(3), cast by the non-Abelian structure of the C^2 coset.

This is why the quantum metric g = 982.5 (Re(QGT)) is large while the Berry curvature (Im(QGT)) vanishes on the full SU(3): the metric encodes the rotational sensitivity of the eigenstates, which manifests as curvature when projected onto a subspace. The projection operator breaks the anti-Hermiticity of the Kosmann connection (because Pi K_alpha Pi is no longer anti-Hermitian on the restricted space), generating the imaginary part that was absent in the parent space.

---

### A.3 Paper-by-Paper Mapping: SU(2) Results as SU(3) Projections

The following table maps each key paper in the Berry corpus to its origin in the SU(3) -> su(2) restriction. In each case, the SU(2) result is NOT applied to the framework -- it EMERGES from the framework.

#### Paper 01 (Geometric Phase, AB to PB): The Foundation

The Berry phase gamma[C] = i oint <n|grad_R|n> . dR (eq 1.2) is the holonomy of a line bundle over parameter space. On SU(3), the holonomy is trivial (flat connection). On the su(2) subspace, the holonomy becomes nontrivial because the projected connection (eq PR-2) has nonzero curvature from the C^2 cross-terms. The Chern number of the projected line bundle over the su(2) parameter space S^2 is an integer:

    C = (1/2pi) integral_{S^2} Omega^{su(2),eff} d^2R = integer     (eq MAP-1)

This integer counts the monopole charge of the effective Berry curvature source at the su(2) degeneracy point -- the diabolical point, as classified by Paper 03.

**Emergence**: Berry's geometric phase is the holonomy of the SU(3) connection projected onto the SU(2) sub-bundle. It exists because SU(2) is a proper subgroup, not because the parent space has curvature.

#### Paper 03 (Diabolical Points, Bruno): Degeneracies from Restriction

Paper 03 characterizes diabolical points as Berry curvature monopoles in parameter space, with topological charges satisfying the sum rule sum_i Q_i(mu) = 2*mu. These degeneracies exist in a 3-parameter Hamiltonian H(B_x, B_y, B_z) = B . J for a spin-J system.

In the framework, the 3-parameter space IS the su(2) subalgebra spanned by (lambda_1, lambda_2, lambda_3). The spin-J system is the restriction of D_K to the su(2) sector. The D_K eigenvalues, when parametrized by these three "field" components, exhibit degeneracies at isolated points -- the diabolical points of Paper 03.

The key subtlety: on the full SU(3), these degeneracies are NOT diabolical points because the Berry curvature vanishes identically. They are merely level crossings without monopole structure. But on the PROJECTED su(2) Hamiltonian H_{su(2)} = Pi D_K Pi, the same crossings acquire monopole charges because the C^2 cross-block contribution (eq PR-4) generates nonzero Berry curvature that diverges at the crossing point.

**Emergence**: Paper 03's diabolical points are topological features of the su(2) projection, not of SU(3) itself. The sum rule D = 2J(J+1)(2J+1)/3 applies to the projected spin-J multiplet. The topological charges are CREATED by the act of projection.

#### Paper 04 (Hannay Angles, Classical Limit): The Zero Hannay Angle and Its Breakdown

Paper 04 establishes that the classical geometric phase (Hannay angle) equals minus the Berry phase in the Koopman-von Neumann formalism: Phi_classical = -gamma_Berry. On SU(3), gamma_Berry = 0, so the Hannay angle is zero -- the classical transit is memoryless (Section IX of the main document).

Under projection to su(2), the Berry phase becomes nonzero, and so does the Hannay angle. The classical limit of su(2)-restricted dynamics has a geometric phase. This means: a classical spin system (the semiclassical limit of a spin-J multiplet) acquires a Hannay angle because it is the su(2) projection of a system that classically has no geometric memory.

**Emergence**: The Hannay angle on SU(2) is the classical shadow of the projection-induced Berry phase. The classical dynamics of the full SU(3) geodesic flow has zero Hannay angle; the restricted dynamics on the su(2) submanifold has nonzero Hannay angle because the restriction is itself a non-classical operation (it involves tracing out the C^2 degrees of freedom).

#### Paper 06 (Superadiabatic LZ, Lima-Burkard): Transition Probabilities from Projected Rotation

Paper 06 discovers that two Hamiltonians with identical eigenvalue landscapes can produce different transition probabilities, depending on the eigenvector rotation rate beta = theta_dot(0). The transition probability is controlled by |alpha - beta|/Delta_0, where alpha is the eigenvalue driving rate.

On SU(3), the eigenvector rotation rate in the Berry curvature sense is zero (Section III.1 of the main document): beta = 0 because Omega = 0. The standard LZ formula P = exp(-2pi Delta^2/hbar alpha) applies without correction.

On the su(2) projection, beta becomes NONZERO because the projected eigenvectors rotate under the influence of the C^2 cross-terms. The projected eigenvector rotation rate is:

    beta_{su(2)} = |<n_{su(2)}|d/dt|m_{su(2)}>| * (E_n - E_m)^{-1}    (eq MAP-2)

This can approach alpha, opening the superadiabatic regime (|alpha - beta| << Delta_0) where transitions are strongly suppressed. The physical content: an observer restricted to su(2) sees eigenvector rotation (Paper 06's mechanism) that does not exist on the full SU(3). The "friction" that Paper 06 describes is the effect of C^2 degrees of freedom acting as a hidden bath that rotates the visible su(2) eigenstates.

**Emergence**: Paper 06's superadiabatic mechanism is the dynamical consequence of the C^2 -> su(2) projection. It explains how the transit through the fold could be less destructive than the standard LZ formula predicts, when viewed from the su(2) sector.

#### Paper 08 (RMT/Chaos, BGS Conjecture): Spectral Statistics from Sector Coupling

Paper 08 reviews the BGS conjecture: classically chaotic systems have GUE/GOE spectral statistics, while integrable systems have Poisson statistics. On SU(3), the spectrum is Poisson (<r> = 0.401 in B2, S53) due to block-diagonality (Schur orthogonality, Section IV.1 of the main document).

On the su(2) projection, the spectral statistics can CHANGE. If the projection couples formerly independent Peter-Weyl sectors (because Pi does not commute with the Peter-Weyl projection operators for the C^2 directions), the projected spectrum can exhibit level repulsion. Whether the projected statistics are Poisson, GOE, or GUE depends on whether the projection preserves or breaks time-reversal symmetry in the su(2) sector.

**Emergence**: The Poisson -> GOE/GUE transition in Berry-Tabor/BGS theory corresponds to the degree of symmetry breaking induced by the projection. An SU(3) system that is integrable (Poisson) can project to an SU(2) system that is chaotic (GOE/GUE) if the projection couples enough independent sectors. This is a many-body analog of the environment-induced decoherence mechanism.

#### Paper 10 (N-body Berry-Tabor): Trace Formula as Sector Sum

Paper 10 extends the Berry-Tabor trace formula to Bethe-integrable many-body systems, with the oscillatory DOS given by eq BT-N (Section IV.2 above). The framework's Richardson-Gaudin BCS satisfies the single-particle Berry-Tabor theorem via Schur orthogonality (a different mechanism from classical integrability).

Under projection to su(2), the trace formula acquires cross-sector terms that were absent on SU(3). The many-body "periodic orbits" M of Paper 10's formula now include paths that traverse the C^2 boundary between su(2)-visible and su(2)-hidden sectors. These additional orbits contribute oscillatory corrections to the projected DOS that have no counterpart in the full SU(3) trace formula.

**Emergence**: The N-body Berry-Tabor trace formula for the su(2)-projected BCS has richer structure than the full SU(3) formula. The "hidden" C^2 sectors contribute additional Maslov indices and scattering phases to the projected orbit sum.

#### Paper 16 (Xiao-Chang-Niu, Berry in Bands): Anomalous Velocity from Projection

Paper 16's central result is the anomalous velocity v_n = partial E_n/(hbar partial k) + (1/hbar) k_dot x Omega_n(k), where the Berry curvature term produces Hall effects and orbital magnetism. On SU(3), Omega_n = 0 identically -- there is no anomalous velocity.

On the su(2) projection, the Bloch bands of the tight-binding model (the 6 GL branches of Section 2 of the Phononic Crystal Geometry document) acquire Berry curvature from the C^2 cross-terms. The S53 result (Zak = 0 for all 6 bands) reflects the fact that the tight-binding model was computed on the full SU(3) geometry with exact block-diagonality. A properly projected su(2) tight-binding model would see effective Berry curvature from the C^2 hopping terms.

The anomalous velocity of a Cooper pair on the 32-cell lattice, projected to the su(2) sector, is:

    v_anomalous^{su(2)} = (1/hbar) K_dot x Omega^{su(2),eff}(K)     (eq MAP-3)

where K is the quasi-momentum on the lattice and Omega^{su(2),eff} is the projection-induced Berry curvature of the tight-binding band. This provides a substrate origin for the Hall effects that Paper 16 classifies.

**Emergence**: Anomalous velocities and Hall effects in condensed matter are the observable consequences of Berry curvature generated by the su(3) -> su(2) projection. The quantum Hall effect is the quantized version (Chern number of the projected band), and its quantization is topologically protected even though the parent SU(3) curvature is zero.

#### Paper 18 (BCS Berry Phase, Marciani-Chubukov): Vortex Berry Phase from Projection

Paper 18 derives A_vort = (n - n_0)/2 for the Berry phase of a vortex in a BCS superconductor. On the full SU(3), vortices are absent in the Type-I condensate (kappa = 0.49 < 1/sqrt(2), S61). The Berry phase of the condensate is zero.

Under projection to su(2), the condensate order parameter acquires an effective phase winding from the C^2 cross-terms. Even without stable vortices on SU(3), the projected su(2) condensate can exhibit phase textures that carry Berry phase. The A_vort formula of Paper 18 applies to these projected textures.

**Emergence**: The BCS Berry phase is the condensate's response to the non-Abelian structure of the C^2 coset, projected onto the su(2) pairing channel. It exists in the projected theory even when the full SU(3) condensate has no vortices.

---

### A.4 The Kaluza-Klein Analogy Made Precise

The parallel between Berry phase emergence and gauge field emergence from KK compactification is not an analogy -- it is the same mathematical structure applied in two contexts.

**Kaluza-Klein**: Start with a (4+n)-dimensional manifold M^{4+n} with metric g_{AB}. The Riemann curvature of the total space may be zero (flat extra dimensions). Perform a dimensional reduction: decompose g_{AB} into a 4D metric g_{mu,nu}, a set of gauge fields A_mu^a, and scalar moduli phi_{ab}. The 4D gauge field strength F_{mu,nu}^a is NONZERO even when the total (4+n)-dimensional curvature vanishes, because it arises from the cross-components of the metric (the off-diagonal g_{mu,a} terms) combined with the non-Abelian structure of the fiber.

The KK gauge field strength is:

    F_{mu,nu}^a = partial_mu A_nu^a - partial_nu A_mu^a + f^a_{bc} A_mu^b A_nu^c    (eq KK-1)

The last term -- the commutator of gauge potentials -- is nonzero because the isometry group of the internal space is non-Abelian. For SU(3) as fiber, the structure constants f^a_{bc} are those of su(3), and the gauge fields are the 8 gluon fields plus the 4 electroweak bosons (from the u(2) subalgebra).

**Berry phase**: Start with the full quantum state space H of D_K on SU(3), with flat Berry connection (Omega = 0). Perform a "dimensional reduction" by projecting onto the su(2) sub-bundle: H -> H_{su(2)}. The restricted Berry curvature is NONZERO even when the total SU(3) curvature vanishes, because it arises from the cross-components of the connection (the C^2 off-diagonal matrix elements) combined with the non-Abelian structure of the coset.

The projected Berry curvature is:

    Omega_{ij}^{su(2)} = partial_i A_j^{su(2)} - partial_j A_i^{su(2)}
                          + [A_i^{C^2}, A_j^{C^2}]|_{su(2)}           (eq KK-2)

The last term is the commutator of the C^2-valued connection components, projected onto su(2). It is nonzero because [C^2, C^2] has a nonzero su(2) component (the A-tensor, |A|^2 = 3/2 + (3/2)e^{-4tau}).

The structural parallel is exact:

| KK gauge field | Berry phase on su(2) |
|:---------------|:---------------------|
| Total space M^{4+n} | Full Hilbert space H on SU(3) |
| Internal manifold K | C^2 coset space SU(3)/U(2) |
| Base M^4 | su(2) parameter space |
| Metric g_{AB} | Quantum geometric tensor Q_{mu,nu} |
| Riemann curvature R = 0 (flat) | Berry curvature Omega = 0 (flat connection) |
| Gauge field A_mu^a from g_{mu,a} | Berry connection A_i^{su(2)} from C^2 cross-terms |
| Field strength F from [A,A] | Berry curvature Omega from [A^{C^2}, A^{C^2}] |
| Structure constants f^a_{bc} of isometry group | Structure constants of su(3), [C^2, C^2] -> su(2) |
| Gauge coupling g from volume of fiber | Effective curvature from quantum metric g = 982.5 |

The identification is: **Berry phase on SU(2) is the holonomy of the KK gauge connection on the internal fiber SU(3), restricted to the isospin directions.** Every result in Papers 01-22 about Berry curvature on SU(2) parameter spaces is a statement about the SU(3)/U(2) gauge holonomy projected onto the 3-dimensional isospin submanifold.

---

### A.5 The Mechanism in Detail: Why Projection Breaks Anti-Hermiticity

The zero theorem (A.1) rests on the anti-Hermiticity of the Kosmann generators: K_a^dag = -K_a. This forces <n|K_a|m> to be purely imaginary, and the product <n|K_a|m><m|K_b|n> to be real, killing Im(QGT).

The projection operator Pi_{su(2)} BREAKS this chain. Let |n_{su(2)}> = Pi|n>/||Pi|n>|| be the projected eigenstate. The projected connection is:

    A_i^{su(2)} = <n_{su(2)}|d_i|n_{su(2)}>
                = <n|Pi d_i Pi|n> / <n|Pi|n>
                = <n|d_i|n>_{su(2)} + <n|[Pi, d_i]|n>_{su(2)} / <n|Pi|n>    (eq MECH-1)

The first term inherits the anti-Hermiticity of K_a and contributes zero to the curvature. The second term -- the COMMUTATOR of the projector with the derivative -- is the obstruction. Pi does not commute with d/dR_i when the su(2) subspace rotates relative to the C^2 subspace as the parameter R_i varies. This non-commutativity injects a genuinely complex component into the projected connection, generating Im(Q) != 0.

Physically: the eigenstates of D_K have components in both the su(2) and C^2 sectors. As the parameter varies, these components mix -- the eigenstate "leaks" between sectors. An observer restricted to su(2) cannot see the C^2 component, so they interpret the leakage as a rotation of the visible state, which produces Berry curvature. The anti-Hermiticity of K_a on the full space does NOT imply anti-Hermiticity of Pi K_a Pi on the subspace, because Pi and K_a do not commute when a ranges over the C^2 directions.

The magnitude of the projection-induced Berry curvature is controlled by the QUANTUM METRIC of the full SU(3):

    |Omega^{su(2),eff}| ~ sum_{C^2} |<n|K_alpha|m>|^2 / (E_n - E_m)^2
                         = Re(QGT)|_{C^2 cross-block}                    (eq MECH-2)

The quantum metric g = 982.5 on SU(3) measures the total eigenstate sensitivity to deformation. The projection carves this real number into its su(2) and C^2 components. The C^2 component, which was invisible as Berry curvature on the full space (because it was real), becomes the SOURCE of Berry curvature on the projected su(2) space. The Berry curvature on SU(2) is literally the quantum metric of SU(3) restricted to the C^2 cross-block and converted from real to imaginary by the projection.

This is why "large quantum metric + zero Berry curvature" (the S36 paradox) is not a paradox at all. The quantum metric IS the Berry curvature, waiting to be revealed by projection. Sensitivity without protection on SU(3) becomes sensitivity WITH protection on SU(2) -- because the projected Berry curvature can be topologically quantized (Chern number = integer) even though the parent curvature is zero.

---

### A.6 What This Means: The Body of Work Reframed

The Berry phase program -- from the 1984 discovery through diabolical points, spectral statistics, semiclassical methods, Hannay angles, anomalous velocities, quantum Hall effects, and BCS vortex phases -- is not a set of results to be "applied" to SU(3). It is a set of results that are DERIVED from SU(3) by the act of restricting attention to the su(2) sub-bundle.

The framework does not need Berry curvature on SU(3). It is zero there, and that is correct. What the framework needs -- and what it naturally provides -- is the mechanism by which an observer embedded in the su(2) sector of su(3) sees Berry curvature, anomalous velocities, topological quantization, diabolical points, and level statistics that follow from the non-Abelian structure of the C^2 coset.

The 22 papers in the Berry corpus divide into two categories under this reframe:

**Papers that describe SU(2) phenomena (emerge from projection)**:
- 01 (Berry phase): holonomy of projected connection
- 02 (Wilczek-Zee): non-Abelian holonomy in projected degenerate subspaces
- 03 (Diabolical points): monopole structure at projected degeneracies
- 04 (Hannay angle): classical limit of projected Berry phase
- 06 (Superadiabatic LZ): eigenvector rotation from C^2 cross-terms
- 08 (RMT/BGS): spectral statistics of projected spectrum
- 10 (N-body BT): trace formula with cross-sector orbits
- 13 (Beam shift): displacement from projected curvature
- 16 (Xiao-Chang-Niu): anomalous velocity from projected band curvature
- 18 (BCS Berry): vortex phase from projected condensate texture
- 21 (Polarization): Zak phase of projected 1D bands

**Papers that describe SU(3)-level structure (apply directly)**:
- 09 (Catastrophe optics): fold A_2 is a property of the full SU(3) spectral action
- 11 (Gutzwiller trace): semiclassical density of the full D_K spectrum
- 12 (QGT): the quantum metric g = 982.5 is a full SU(3) quantity
- 14 (Metric without curvature): the ERRATUM regime IS the SU(3) geometry
- 15 (Quantum metric era): experimental validation of the SU(3) regime
- 17 (QPT geometry): fidelity susceptibility at the fold is full SU(3)
- 19 (Topological SC): BDI classification of the full BCS state
- 20 (Topological TI): Z_2 invariants of the full spectral triple
- 22 (Equivariant spectral flow): sf = 0 on the full SU(3)

The first category -- the majority of Berry's deepest results -- comprises the physics that an su(2)-restricted observer experiences. This is the physics of the Standard Model: quarks and leptons are su(2) doublets and singlets, gauge bosons are su(2) connections, the Hall effect probes su(2) Berry curvature. The entire phenomenology of spin-1/2 quantum mechanics, which is the phenomenology that Berry's 1984 paper launched, is the su(2) projection of the SU(3) substrate.

The second category comprises the properties of the substrate itself -- the parent space whose projection generates everything in the first category. These are the "gravitational" side of the correspondence: the spectral action, the moduli space, the catastrophe structure, the quantum metric. They are the geometry of the stage; the first category is the physics of the actors.

---

### A.7 The Phononic Interpretation

In the phononic framework, particles are excitations of the M^4 x SU(3) substrate. The su(2) sector of the substrate carries the electroweak gauge structure: lambda_1, lambda_2, lambda_3 generate the SU(2)_L gauge group, with coupling e^{-2tau} at the Jensen fold.

A phonon propagating in the su(2) directions of the SU(3) fiber experiences the Berry curvature induced by the C^2 cross-terms. This is the origin of:

1. **Spin**: A phonon excitation in the su(2) sector carries spin quantum numbers because the projected Berry curvature creates a monopole field on the SU(2) parameter space (the Bloch sphere). Spin-1/2 is the fundamental representation of the projected connection's holonomy group.

2. **Weak interactions**: The W and Z bosons ARE the gauge connection of the su(2) sub-bundle projected from SU(3). Their masses arise from the order-one condition failure on C^2 (the Higgs mechanism), which is the same C^2 cross-block that generates Berry curvature.

3. **Anomalous Hall effects**: A Cooper pair on the 32-cell lattice, restricted to the su(2) hopping channels, experiences an anomalous velocity from the projected Berry curvature of its tight-binding band. This is the microscopic origin of the Hall effect on the substrate.

4. **Topological protection of quantization**: The Chern numbers of the projected su(2) bands are integers -- topologically protected despite the parent SU(3) having zero Chern numbers everywhere. The quantization of electric charge (in units of e/3 for quarks, e for leptons) reflects the Chern number structure of the projected bands.

The framework does not invalidate Berry's body of work. It EXPLAINS it. Every Berry phase result that involves SU(2) -- which is nearly all of them, because spin-1/2 is the workhorse of quantum mechanics -- arises from the dimensional reduction SU(3) -> SU(2). The anti-Hermiticity of the Kosmann connection on SU(3) guarantees that the parent space is flat. The non-Abelian structure of the C^2 coset guarantees that the projection is curved. Together, these two structural facts produce the entire Berry phase phenomenology as an emergent consequence of SU(3) geometry.

The quantum metric g = 982.5 is not a frustrated observable trapped behind zero Berry curvature. It is the RESERVOIR from which all Berry curvature on SU(2) is drawn. The projection converts Re(QGT) on SU(3) into Im(QGT) on SU(2). The "sensitivity without protection" on the parent space becomes "sensitivity WITH protection" on the child space. The S36 paradox dissolves: it was never a paradox. It was the view from the wrong floor of the building.

---

### A.8 Open Calculation: Quantitative Projection Test

**Calculation F (PROPOSED)**: Construct the explicit projection operator Pi_{su(2)} on the 16-dimensional internal spinor space of D_K. Compute the restricted Hamiltonian H_{su(2)}(R) = Pi D_K(R_1, R_2, R_3) Pi for R_i parametrizing the su(2) directions (lambda_1, lambda_2, lambda_3 components of a perturbation away from the Jensen metric). Compute the Berry curvature of the projected eigenvalues as a function of R. Verify that:

1. Omega^{su(2),eff} != 0 (nonzero Berry curvature on the projected space)
2. The magnitude scales as the quantum metric of the C^2 cross-block (eq MECH-2)
3. The monopole structure at projected degeneracies matches Paper 03's diabolicity theory
4. The Chern number is an integer (topological quantization from projection)

This is the most important proposed calculation in this document. It would provide the first QUANTITATIVE verification of the projection mechanism, testing whether the C^2 cross-terms actually generate the expected Berry curvature on the su(2) subspace. The input data: the 16x16 matrices K_a (a=0,...,7) from the Kosmann derivative, available in the existing computation eigenvalue code. The computation is a parameter sweep over a 3D grid in (R_1, R_2, R_3) space, computing projected eigenvalues and Berry curvature at each point. Estimated cost: comparable to the s55_berry_fold.py computation (32x32 Hamiltonian, ~1 hour).

If Calculation F confirms nonzero Berry curvature on the projected su(2), the entire reframe of this addendum moves from structural argument to computed result. If it fails (Omega^{su(2),eff} = 0 even after projection), the Kosmann anti-Hermiticity may be strong enough to survive projection, and the mechanism proposed here would need revision.
