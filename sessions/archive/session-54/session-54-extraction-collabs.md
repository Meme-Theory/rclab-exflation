# Session 54 Collaborative Review -- Computation Extraction

All computation suggestions, recommendations, and proposed calculations extracted from the 8 collaborative review documents. Numbered sequentially. No filtering, no interpretation.

---

## Master Synthesis (`session-54-master-collab.md`)

### 1. S_occ on larger lattices (64, 128 cells)
- **Source**: Master Synthesis, Section V (C1)
- **What**: Extend Casimir cutoff to higher representations, construct larger CG graphs, compute S_occ at multiple tau to test whether the S_occ minimum is a lattice artifact or convergent continuum feature.
- **Inputs**: 32-cell lattice construction pipeline; higher SU(3) irreps beyond current cutoff
- **Tests**: Whether the S_occ minimum persists, deepens, or vanishes at larger N
- **Cost**: MEDIUM-HIGH (64-cell ~4x of 32-cell; 128-cell ~16x)
- **Priority**: CRITICAL (all 7 reviewers)

### 2. Zeta-regularized one-loop effective action Gamma[tau]
- **Source**: Master Synthesis, Section V (C2)
- **What**: Compute zeta'_D(0, tau) = -sum log(lambda_k) from existing 32-cell eigenvalue data at 50 tau values. This is the Coleman-Weinberg effective potential regularized without cutoff ambiguity.
- **Inputs**: Existing 32-cell eigenvalue data at 50 tau values
- **Tests**: Whether cutoff-independent effective action has a minimum near the fold
- **Cost**: ZERO (50 determinant computations on 32x32 matrices from existing data)
- **Priority**: CRITICAL (Feynman primary, Baptista, Volovik implicit)

### 3. Cutoff function sensitivity study for S_occ
- **Source**: Master Synthesis, Section V (C3)
- **What**: Compute S_occ for a one-parameter Fermi-Dirac family f_alpha interpolating sharp to Gaussian; track barrier height vs alpha.
- **Inputs**: Existing eigenvalue data
- **Tests**: Whether the S_occ minimum persists for physically motivated cutoffs
- **Cost**: LOW (reuse existing eigenvalue data, sweep alpha parameter)
- **Priority**: CRITICAL (Baptista primary, Tesla, Feynman, Phonon-First, QA, Volovik)

### 4. Integrability breaking at N_pair = 2
- **Source**: Master Synthesis, Section V (C4)
- **What**: Compute N_pair = 2 Fock space (dim 28), include inter-pair interactions, measure integrability-breaking rate.
- **Inputs**: BCS Hamiltonian, inter-pair interaction matrix elements
- **Tests**: Whether inter-pair interactions break Richardson-Gaudin conserved integrals
- **Cost**: MEDIUM (28-dimensional exact diagonalization)
- **Priority**: CRITICAL (Volovik primary, Phonon-First, Feynman)

### 5. Phonon dispersion relation on the 32-cell lattice
- **Source**: Master Synthesis, Section V (H1)
- **What**: Diagonalize H_TB by bond type, classify eigenstates as acoustic vs optical, extract group velocities. Compare effective sound velocity to continuum c_Gold.
- **Inputs**: Existing s54_tb_hamiltonian.npz data
- **Tests**: Acoustic vs optical branch identification, effective sound velocity, comparison to continuum c_Gold
- **Cost**: LOW (reuse existing data)
- **Priority**: HIGH (Tesla primary, QA primary, Phonon-First)

### 6. Non-trivial bundle topology / O'Neill A-tensor with gauge fields
- **Source**: Master Synthesis, Section V (H2)
- **What**: Compute O'Neill A-tensor with SU(2) x U(1) gauge field background from NCG inner fluctuations. Test whether inner fluctuations or BCS U(1)_7 breaking generates nonzero A-tensor.
- **Inputs**: NCG inner fluctuation formalism, submersion formulas
- **Tests**: Whether inner fluctuations or BCS U(1)_7 breaking generates nonzero A-tensor
- **Cost**: MEDIUM
- **Priority**: HIGH (Baptista primary, SP, Phonon-First)

### 7. N_pair = 2 flat-band pairing enhancement
- **Source**: Master Synthesis, Section V (H3)
- **What**: Second pair in B2, flat-band linear-T_c formula, superfluid density tensor sweep.
- **Inputs**: B2 flat band structure, Peotta-Torma formula
- **Tests**: Whether B2 flat band at N_pair = 2 crosses the pairing collapse threshold (d/Delta -> O(1))
- **Cost**: MEDIUM
- **Priority**: HIGH (Volovik primary, Phonon-First)

### 8. Zero-point fluctuation stability of S_occ minimum
- **Source**: Master Synthesis, Section V (H4)
- **What**: Extract d^2(S_occ)/dtau^2, compute omega_0, compare barrier crossing rate to 1.
- **Inputs**: Existing S_occ data
- **Tests**: Whether zero-point energy of modulus oscillation exceeds the 5.35% barrier
- **Cost**: LOW (from existing S_occ data)
- **Priority**: HIGH (QA primary, Tesla)

### 9. Conformal diagram and energy condition audit of lattice evolution
- **Source**: Master Synthesis, Section V (H5)
- **What**: Integrate conformal time from scale factor data, compute w_eff(tau). Test particle horizon existence, SEC violation during acceleration, discrete trapped surfaces.
- **Inputs**: Connes distance data from W1-2, scale factor from W2-1
- **Tests**: Particle horizon existence, SEC violation during acceleration, discrete trapped surfaces
- **Cost**: LOW
- **Priority**: HIGH (SP primary, Feynman)

### 10. Berry phase around the Jensen fold (B2 crossing)
- **Source**: Master Synthesis, Section V (M1)
- **What**: Compute Berry phase of the B2 eigenstate around a closed loop in the (tau, sigma) parameter space to determine whether the B2 mass zero-crossing is topologically protected or accidental.
- **Inputs**: Existing eigenvector data from B2-ANGULAR-54 and OFF-JENSEN-T2-54
- **Tests**: Whether the B2 mass zero-crossing at tau* = 0.190158 is topologically protected or accidental
- **Cost**: LOW
- **Priority**: MEDIUM (Feynman)

### 11. Impedance mismatch at cutoff edge
- **Source**: Master Synthesis, Section V (M2)
- **What**: Compute acoustic impedance Z = rho * c_s at the sharp cutoff Lambda = 1.0 M_KK. Test whether the S_occ barrier height follows acoustic impedance scaling.
- **Inputs**: Existing s54_sa_latt_occ.npz data
- **Tests**: Whether the S_occ barrier height follows acoustic impedance scaling
- **Cost**: LOW
- **Priority**: MEDIUM (Tesla)

### 12. Volovik thermodynamic identity applied to GGE
- **Source**: Master Synthesis, Section V (M3)
- **What**: Quantify the departure from Volovik equilibrium. Compute delta_eq = max_k |T_k - T_mean| / T_mean for the GGE temperatures.
- **Inputs**: GGE temperature data (T_B2, T_B1, T_B3)
- **Tests**: Quantifies the GGE departure from Volovik equilibrium as a CC estimate
- **Cost**: LOW
- **Priority**: MEDIUM (Tesla)

### 13. PL dual Connes distance / T-duality test
- **Source**: Master Synthesis, Section V (M4)
- **What**: Compute Connes distances on the AN dual graph and test whether d_Connes(AN) * d_Connes(SU(3)) = constant (spectral T-duality criterion).
- **Inputs**: AN dual graph, PL cross-pairing matrix P, 32-cell lattice data
- **Tests**: Whether d_Connes(AN) * d_Connes(SU(3)) = constant (spectral T-duality)
- **Cost**: MEDIUM
- **Priority**: MEDIUM (Phonon-First)

### 14. Post-transit EFT: Feynman rules and power counting
- **Source**: Master Synthesis, Section V (M5)
- **What**: Write explicit Lagrangian from 8 lattice eigenvalues and V_kl matrix, derive Feynman rules, compute tree-level cross sections and one-loop self-energies, classify operators by relevance.
- **Inputs**: Lattice single-particle spectrum, lattice V_kl
- **Tests**: Renormalizability, effective coupling g*M_KK^2, decay rates for lattice quasiparticles
- **Cost**: MEDIUM
- **Priority**: MEDIUM (Feynman)

### 15. Acoustic impedance matching at KZ domain boundaries
- **Source**: Master Synthesis, Section V (M6)
- **What**: Compute phonon transmission coefficient at boundary between two 32-cell domains with different tau values. Use Fisher-Lee relation on coupled Green's functions.
- **Inputs**: H_TB at two different tau values
- **Tests**: Phonon transmission across tau-mismatched domains (inter-cell GGE communication)
- **Cost**: MEDIUM
- **Priority**: MEDIUM (QA)

### 16. Lichnerowicz stability (Lauret-Schwahn) at the fold
- **Source**: Master Synthesis, Section V (M7)
- **What**: Compute Casimir operator on G-invariant TT tensors to determine whether the Jensen metric at the fold is dynamically stable under linearized gravity.
- **Inputs**: Lauret-Schwahn universal formula, Jensen metric data
- **Tests**: Whether the Jensen metric at the fold is dynamically stable under linearized gravity
- **Cost**: MEDIUM-HIGH
- **Priority**: MEDIUM (Baptista)

### 17. Kretschner scalar on the Poisson-Lie dual
- **Source**: Master Synthesis, Section V (M8)
- **What**: Compute K* = |Riem*|^2 on the AN subgroup at multiple tau values to determine regularity.
- **Inputs**: Milnor formula structure constants from W3-2 script
- **Tests**: Whether the PL dual geometry is regular (bounded K*) or singular at finite tau
- **Cost**: LOW-MEDIUM
- **Priority**: MEDIUM (SP)

### 18. Kibble-Zurek domain wall density prediction
- **Source**: Master Synthesis, Section V (M9)
- **What**: Apply KZ defect density formula with known quench parameters (tau_Q, tau_0, d_s, nu, z) on the 32-cell graph.
- **Inputs**: omega_tau = 8.27, omega_PV = 0.792, d_s = 2, BCS mean-field nu = 1/2, z = 2
- **Tests**: n_defect ~ 1-2 on 32-cell graph from KZ formula
- **Cost**: LOW
- **Priority**: MEDIUM (Phonon-First)

### 19. 8D BLV formula for acoustic scale factor
- **Source**: Master Synthesis, Section V (M10)
- **What**: Compute the BLV conformal factor in d=7 or d=8 spatial dimensions. The dimensional exponent changes from 1/2 to 1/7 in the N_e formula.
- **Inputs**: c_s(tau) from existing S53 data
- **Tests**: Whether the dimensional exponent changes N_e_cs from 2.72 to 0.78 (decisive for N_e)
- **Cost**: LOW (single equation)
- **Priority**: MEDIUM (Tesla)

### 20. Optical theorem on lattice scattering amplitudes
- **Source**: Master Synthesis, Section V (M11)
- **What**: Compute the T-matrix on the 8-mode system using ED eigenstates from W1-1. Verify optical theorem Im M(k,k;E) = -(1/2) sum_f |M(k,f;E)|^2 * rho_f.
- **Inputs**: ED eigenstates from W1-1
- **Tests**: Unitarity of lattice BCS Hamiltonian, lattice scattering lengths vs continuum
- **Cost**: LOW (8x8 T-matrix)
- **Priority**: MEDIUM (Feynman)

### 21. Quantum metric / Peotta-Torma superfluid weight
- **Source**: Master Synthesis, Section V (M12)
- **What**: Compute geometric Berry curvature contribution to D_s from the quantum metric of the lattice eigenstates.
- **Inputs**: 32-cell lattice eigenstates
- **Tests**: Whether geometric Berry curvature contribution to D_s bypasses the DOS-based pairing collapse
- **Cost**: MEDIUM
- **Priority**: MEDIUM (Phonon-First)

### 22. Off-Jensen sin^2(theta_W) correction
- **Source**: Master Synthesis, Section V (M13)
- **What**: Compute sin^2(theta_W) at the valley floor sigma* = 0.0148 rather than at sigma = 0.
- **Inputs**: Paper 13 eq 5.25, valley floor displacement data from W3-6
- **Tests**: Whether the 12.5% C^2 enhancement at valley floor shifts the Weinberg angle
- **Cost**: LOW
- **Priority**: MEDIUM (Baptista)

### 23. Floquet analysis of the pair walker (Leggett mode)
- **Source**: Master Synthesis, Section V (M14)
- **What**: Apply Floquet theory to the 8-mode Hamiltonian driven at frequency omega_d near the Leggett mode. Compute quasienergy spectrum and Mathieu stability diagram.
- **Inputs**: 8-mode Hamiltonian from W0-1, Leggett mode omega_L1 = 0.070 M_KK
- **Tests**: Parametric instability tongues near fold, Mathieu stability diagram for 8-mode system
- **Cost**: MEDIUM
- **Priority**: MEDIUM (Tesla)

### 24. Off-Jensen full trajectory dynamics in (tau, sigma) plane
- **Source**: Master Synthesis, Section V (L1)
- **What**: Integrate equations of motion in the (tau, sigma) plane with DeWitt metric and KK potential. Test whether trajectory remains within sigma < 0.02 through transit.
- **Inputs**: DeWitt metric G_ij, KK potential, initial conditions from terminal velocity
- **Tests**: Whether trajectory remains within sigma < 0.02 through transit
- **Cost**: MEDIUM
- **Priority**: LOW (Baptista)

### 25. Three-parameter volume-preserving landscape
- **Source**: Master Synthesis, Section V (L2)
- **What**: Map the full 3D volume-preserving landscape V(tau, sigma_2, sigma_3) in the U(2)-invariant metric moduli space.
- **Inputs**: Paper 15 Section 3.5, full 3-parameter family structure
- **Tests**: Whether Jensen trajectory is minimum-energy path in full 3D moduli space
- **Cost**: HIGH
- **Priority**: LOW (Baptista)

### 26. Anharmonic phonon lifetime on the lattice
- **Source**: Master Synthesis, Section V (L3)
- **What**: Compute cubic and quartic anharmonic corrections to H_TB. Use Fermi's golden rule for decay rates.
- **Inputs**: H_TB expanded to 3rd and 4th order in tau
- **Tests**: Quality factor of each mode, dynamical accessibility of S_occ minimum
- **Cost**: MEDIUM-HIGH
- **Priority**: LOW (QA)

### 27. Continuum Connes distance at max_pq_sum = 6
- **Source**: Master Synthesis, Section V (L4)
- **What**: Compute continuum Connes distances using SDP formulation at max_pq_sum=6 (full 992-mode spectrum).
- **Inputs**: 992-mode Dirac spectrum
- **Tests**: Bridge lattice (2.117x) and continuum (~1.1x) Connes distance discrepancy
- **Cost**: HIGH (992-mode SDP)
- **Priority**: LOW (Baptista)

### 28. Two-fluid Landau-Khalatnikov cosmological cooling trajectory
- **Source**: Master Synthesis, Section V (L5)
- **What**: Solve d(rho_q)/dt = -3H(rho_q + P_q) + Gamma(rho_q - rho_eq) with Gamma from N_pair = 2 results. Track CC decay from 10^115 to 10^0.
- **Inputs**: N_pair = 2 integrability-breaking rate (depends on C4 results)
- **Tests**: CC decay from 10^{115} to 10^0 with Gamma from N_pair = 2
- **Cost**: MEDIUM (depends on C4 results)
- **Priority**: LOW (Volovik)

---

## Tesla Resonance Theorist (`session-54-tesla-collab.md`)

### 29. Dispersion relation of the 32-cell lattice (phononic, zero-cost diagnostic)
- **Source**: Tesla, Section 3 (S-1)
- **What**: Extract the full phonon dispersion omega(k) by projecting 32 eigenstates onto C-even and C-odd Z_2 conjugation sectors, then plotting eigenvalue vs Casimir C_2(p,q) of the dominant cell. Identify acoustic vs optical branches, extract effective sound velocity c_eff.
- **Inputs**: s54_tb_hamiltonian.npz (32 eigenvalues + eigenvectors at 50 tau values)
- **Tests**: Acoustic branch slope gives c_eff on the lattice; compare to continuum c_Gold from S53
- **Cost**: ZERO (existing data)
- **Priority**: Not stated

### 30. Impedance mismatch at the cutoff edge
- **Source**: Tesla, Section 3 (S-2)
- **What**: Compute acoustic impedance Z(tau) = n_below(tau) * mean_occupation_below(tau) at the sharp cutoff Lambda = 1.0 M_KK. Test barrier height scaling as reflection coefficient from impedance theory.
- **Inputs**: s54_sa_latt_occ.npz (eigenvalue spectrum and occupation weights at 50 tau values)
- **Tests**: Whether barrier is impedance-controlled (quantitative scaling prediction). Discriminates between two mechanisms for the S_occ minimum
- **Cost**: LOW (existing data)
- **Priority**: Not stated

### 31. Floquet analysis of the pair walker
- **Source**: Tesla, Section 3 (S-3)
- **What**: Apply Floquet theory to the 8-mode BCS Hamiltonian with periodically modulated Josephson couplings J -> J(1 + epsilon * cos(omega_d * tau)) near the Leggett mode omega_L1 = 0.070 M_KK. Compute quasienergy spectrum and parametric instability tongues.
- **Inputs**: 8-mode Hamiltonian from W0-1, Leggett mode frequency
- **Tests**: Whether the pair walker has a parametric instability tongue near the fold; Mathieu stability diagram for 8-mode system
- **Cost**: MEDIUM
- **Priority**: Not stated (carry-forward from S53 LEGGETT-AMP-53)

### 32. 8-dimensional BLV formula for the acoustic scale factor
- **Source**: Tesla, Section 3 (S-4)
- **What**: Compute the BLV acoustic metric conformal factor in 8D: exponent changes from 1/2 (4D) to 1/7 (8D). Single equation: N_e_cs = (1/7) ln(229.48) = 0.78 vs 2.72 in 4D.
- **Inputs**: c_s(tau) from existing S53 data
- **Tests**: Whether the dimensional exponent changes N_e_cs from 2.72 to 0.78 (decisive for N_e)
- **Cost**: LOW (single equation, 10 minutes)
- **Priority**: Not stated

### 33. Volovik thermodynamic identity applied to W3-8
- **Source**: Tesla, Section 3 (S-5)
- **What**: Quantify GGE departure from Volovik equilibrium: delta_eq = max_k |T_k - T_mean| / T_mean. Apply Volovik's thermodynamic identity (Paper 10 eq 29.4) to compute non-zero vacuum pressure from GGE temperature structure.
- **Inputs**: GGE temperatures T_B2 = 0.668, T_B1 = 0.435, T_B3 = 0.178
- **Tests**: Whether the Volovik framework correctly predicts the non-zero P_vac from the GGE departure from equilibrium; CC estimate from non-equilibrium contribution
- **Cost**: LOW
- **Priority**: Not stated

### 34. Acoustic cavity resonance frequency of the S_occ well
- **Source**: Tesla, Section 3 (S-6)
- **What**: Compute omega_well = sqrt(S_occ'' / M_modulus) from the S_occ minimum, where M_modulus = G_DeWitt = 5.0. Compare to the Leggett mode omega_L1 = 0.070 M_KK.
- **Inputs**: S_occ data (second derivative at minimum), G_DeWitt = 5.0
- **Tests**: Whether omega_well ~ omega_L1 (internal resonance between geometric stabilization and phononic pair oscillation)
- **Cost**: LOW
- **Priority**: Not stated

### 35. Vary Lambda continuously from 0.5 to 3.0 M_KK
- **Source**: Tesla, Section 5 (Q1)
- **What**: Sweep the cutoff Lambda from 0.5 to 3.0 M_KK and track the location of the S_occ minimum tau_min. If tau_min tracks Lambda, it is an edge effect. If tau_min is pinned near the fold regardless of Lambda, it is a standing wave.
- **Inputs**: Existing eigenvalue data at 50 tau values
- **Tests**: Discriminates standing wave (physical) vs edge effect (artifact) origin of S_occ minimum
- **Cost**: LOW (reuse existing data)
- **Priority**: Not stated

### 36. Lattice acoustic branch slope vs continuum c_Gold
- **Source**: Tesla, Section 5 (Q2)
- **What**: Extract effective sound velocity on the lattice from the acoustic branch dispersion (proposed in S-1) and compare to continuum c_Gold = 0.444 M_KK from S53.
- **Inputs**: Dispersion relation from S-1
- **Tests**: Measures lattice discretization error in the phononic sector
- **Cost**: LOW (depends on S-1)
- **Priority**: Not stated

### 37. Direct GGE quasiparticle distribution from Massey parameters
- **Source**: Tesla, Section 5 (Q3)
- **What**: Compute the quasiparticle distribution n_k(tau_final) directly from the 1378 Massey parameters and crossing energies, without the full ED. Test whether the GGE can be derived independently from the crossing cascade alone.
- **Inputs**: Massey parameters and crossing energies from MASSEY-FOLD-54
- **Tests**: Whether the GGE is fully determined by the crossing cascade (independent derivation of post-transit state)
- **Cost**: Not stated
- **Priority**: Not stated

### 38. Self-consistency check: S_occ minimum vs Connes expansion coexistence
- **Source**: Tesla, Section 5 (Q4)
- **What**: Determine whether the S_occ minimum (modulus wants to sit at tau = 0.194) and the Connes expansion (monotonic through tau = 0.194) are self-consistent. If modulus stabilizes, expansion stops at a = 2.117. Test whether the S_occ minimum is a late-time stabilization mechanism.
- **Inputs**: S_occ data, Connes distance data
- **Tests**: Whether the two results coexist self-consistently; whether S_occ minimum is late-time stabilization (after kinetic expansion)
- **Cost**: LOW (analysis)
- **Priority**: Not stated

---

## Feynman Theorist (`session-54-feynman-collab.md`)

### 39. One-loop effective action for tau via zeta regularization
- **Source**: Feynman, Section 3 (Suggestion 1)
- **What**: Compute Gamma_1loop[tau] = -(1/2) zeta'_D(0, tau) from the existing 992-mode Dirac spectrum at multiple tau values. This is zeta-function regularization with no cutoff ambiguity. zeta'_D(0) = -sum log(lambda_k). If monotone, S_occ minimum is cutoff artifact. If minimum exists, stabilization established.
- **Inputs**: Existing eigenvalue data at 50 tau values (992-mode continuum or 32-cell lattice)
- **Tests**: Whether the cutoff-independent effective action has a minimum near the fold; settles the functional identity question
- **Cost**: ZERO (sum over known eigenvalues)
- **Priority**: CRITICAL (Feynman's top priority)

### 40. Optical theorem for lattice scattering amplitudes
- **Source**: Feynman, Section 3 (Suggestion 2)
- **What**: Extract the lattice T-matrix from the 256-state ED spectrum using the Feynman-Goldberger formula. Verify Im M(k,k;E) = -(1/2) sum_f |M(k,f;E)|^2 * rho_f. Compare lattice scattering lengths to continuum.
- **Inputs**: ED eigenstates from W1-1, lattice pairing interaction V
- **Tests**: Unitarity of lattice BCS Hamiltonian; lattice scattering lengths vs continuum values
- **Cost**: LOW (T-matrix is matrix inversion on 8x8 space)
- **Priority**: Not stated

### 41. Post-transit EFT: Feynman rules and power counting
- **Source**: Feynman, Section 3 (Suggestion 3)
- **What**: Write explicit action S = sum_k [psi_bar_k (i gamma d - m_k) psi_k] + sum_{k,l} g_{kl} (psi_bar_k psi_k)(psi_bar_l psi_l) with m_k from 8 lattice eigenvalues and g_{kl} from lattice V matrix. Derive Feynman rules, tree-level cross-sections, one-loop self-energies, Wilsonian operator classification.
- **Inputs**: 8 lattice eigenvalues at fold, lattice V matrix from S52
- **Tests**: Effective expansion parameter g*M_KK^2 (~0.02, perturbative?); renormalizability; relevant/marginal/irrelevant operators; decay rates
- **Cost**: MEDIUM
- **Priority**: Not stated (carry-forward from S40 Computation C)

### 42. Zeta-regularized spectral action vs sharp-cutoff diagnostic
- **Source**: Feynman, Section 3 (Suggestion 4)
- **What**: Compute S_zeta(tau) = -(1/2) zeta'_H(0, tau) = (1/2) sum_{k=1}^{31} log(lambda_k) from the 32-cell graph Laplacian at 50 tau values. Compare directly to S_occ(tau) with sharp cutoff.
- **Inputs**: 32-cell lattice eigenvalues at 50 tau values
- **Tests**: If S_zeta monotone while S_occ has minimum, the minimum is a regulator artifact. This is literally log det(H_TB).
- **Cost**: ZERO (50 determinant computations on 32x32 matrix, under a second)
- **Priority**: Not stated (subsidiary to Suggestion 1)

### 43. Berry phase around the Jensen fold
- **Source**: Feynman, Section 3 (Suggestion 5)
- **What**: Compute gamma_B2 = oint <psi_B2|d/d(theta)|psi_B2> d(theta) around a small loop enclosing the B2 mass zero-crossing point in the 2D (tau, sigma) parameter space. Detect topological protection of the crossing.
- **Inputs**: Eigenvectors from B2-ANGULAR-54 (multiple tau) and OFF-JENSEN-T2-54 (multiple sigma)
- **Tests**: If gamma_B2 is quantized (pi or 2pi), crossing is topologically protected (structural fold-crossing coincidence). If zero, coincidence is parametric.
- **Cost**: ZERO (existing eigenvector data, requires interpolation and overlap integral)
- **Priority**: Not stated

### 44. Two-loop sigma-tau mixing
- **Source**: Feynman, Section 5 (Q2)
- **What**: Compute two-loop (tau-loop) corrections to the sigma propagator to test whether the sigma-tau decoupling (xi = 1.41e-7) is preserved beyond the GL level.
- **Inputs**: GL Hamiltonian from W3-3, sigma and tau propagators
- **Tests**: Whether higher-loop diagrams preserve the sigma-tau decoupling
- **Cost**: Not stated
- **Priority**: Not stated

### 45. Mixed a_4(M^4 x K) heat kernel cross-terms
- **Source**: Feynman, Section 5 (Q3)
- **What**: Compute the R_4 * R_K cross-terms in the heat kernel factorization (off-diagonal contributions to a_4(M^4 x K) beyond the product decomposition). Test whether these produce additional R^2 terms that soften the scalaron mass.
- **Inputs**: Heat kernel coefficients, Paper 33 factorization
- **Tests**: Whether off-diagonal contributions could soften the scalaron mass from 0.1085 M_KK
- **Cost**: Not stated
- **Priority**: Not stated

### 46. Periodic orbit tori identification with phonon modes
- **Source**: Feynman, Section 5 (Q4)
- **What**: Use the Berry-Tabor trace formula to relate invariant tori on (SU(3), g_Jensen) to specific phonon modes or physical observables (spectral form factor, scattering cross-sections).
- **Inputs**: Berry-Tabor formula, periodic orbit data, Casimir dispersion on maximal torus
- **Tests**: Whether the BT oscillating/smooth ratio has predictive power for phonon spectrum observables
- **Cost**: Not stated
- **Priority**: Not stated

### 47. Integrability-breaking mechanisms survey
- **Source**: Feynman, Section 5 (Q5)
- **What**: Identify and compute the effects of candidate integrability-breaking mechanisms: coupling to 4D gravity, spatial inhomogeneity across fabric, multi-cell effects, non-BCS interactions.
- **Inputs**: Richardson-Gaudin conserved integrals, coupling constants
- **Tests**: Which physical mechanisms could break integrability and allow thermalization (resolving 115-order CC)
- **Cost**: Not stated
- **Priority**: Not stated

---

## Schwarzschild-Penrose Geometer (`session-54-sp-collab.md`)

### 48. Conformal diagram of the lattice spectral triple
- **Source**: SP, Section 3 (Computation 1)
- **What**: Construct the conformal diagram from Connes distance data. Define conformal time eta by d(eta) = d(tau)/a(tau). Determine whether the lattice evolution has a particle horizon (finite eta at tau = 0), event horizon (finite eta at tau -> inf), or both.
- **Inputs**: a(tau) = 1.014 exp(3.651 tau), q(tau) data, H(tau) data from W1-2 and W2-1
- **Tests**: Does a lattice particle horizon exist? Given a ~ exp(3.65 tau), integral converges, predicting finite particle horizon.
- **Cost**: LOW
- **Priority**: Not stated

### 49. Trapped surface analysis on the lattice
- **Source**: SP, Section 3 (Computation 2)
- **What**: Define discrete expansion theta_k at each node k as rate of change of Connes distance ball volume. Test if theta_k < 0 for all nodes at some tau (discrete trapped surface).
- **Inputs**: Distance matrix from W1-2 (32x32, at 10 tau values)
- **Tests**: Whether the Penrose singularity theorem has a discrete analog on the Voronoi lattice
- **Cost**: LOW
- **Priority**: Not stated

### 50. Kretschner scalar on the Poisson-Lie dual
- **Source**: SP, Section 3 (Computation 3)
- **What**: Compute K*(tau) = |Riem*|^2 on the AN subgroup at multiple tau. If K* diverges at finite tau, PL dual has curvature singularity. If bounded, dual is regular. Extend Milnor formula structure constants to full Riemann tensor via structure constant contractions.
- **Inputs**: Structure constants from W3-2 script, Milnor formula
- **Tests**: Whether the PL dual geometry is regular or singular at finite tau; whether the minimum at tau = 0.19 occurs in smooth geometry
- **Cost**: LOW-MEDIUM (finite algebraic computation, no PDEs)
- **Priority**: Not stated

### 51. Energy condition audit at the Connes acceleration-deceleration transition
- **Source**: SP, Section 3 (Computation 4)
- **What**: Compute effective equation of state w_eff(tau) = -1 - 2 dot(H)/(3H^2) from lattice H(tau) data. Verify whether SEC is violated during accelerating phase and satisfied during decelerating phase.
- **Inputs**: H(tau) data from W2-1, q(tau) transition data
- **Tests**: SEC violation during acceleration (q < 0) and satisfaction during deceleration (q > 0); consistency with Hawking-Penrose theorem
- **Cost**: LOW
- **Priority**: Not stated

### 52. Gauss-Codazzi constraint on the sigma-tau saddle
- **Source**: SP, Section 3 (Computation 5)
- **What**: Compute the Gauss curvature K_G of the 2D potential surface V(tau, sigma). At the saddle, K_G < 0. The magnitude quantifies how strongly the saddle channels the trajectory along the Jensen line. Provides invariant characterization of the 7-degree deflection from W3-6.
- **Inputs**: 2D landscape data from W3-6
- **Tests**: Invariant characterization of the 7-degree deflection; transition from K_G < 0 (saddle) to K_G > 0 (valley)
- **Cost**: LOW
- **Priority**: Not stated

### 53. PL dual spectral action at the species scale
- **Source**: SP, Section 5 (Q3)
- **What**: Compute the PL dual spectral action at Lambda = 2.06 M_KK (AT the species scale) rather than at the minimum Lambda = 2.703. Check whether the minimum persists below the species scale.
- **Inputs**: PL dual spectral action data from W3-2
- **Tests**: Whether the dual minimum is an artifact of EFT breakdown above the species scale or a genuine feature visible from below
- **Cost**: LOW
- **Priority**: Not stated

### 54. Conformal completion of the lattice spectral triple
- **Source**: SP, Section 5 (Q1)
- **What**: Determine whether the conformal compactification of the discrete 32-node Connes metric space has well-defined null and timelike infinities (Penrose diagram in the strict sense).
- **Inputs**: Connes distance metric on 32 points, a(tau) data
- **Tests**: Whether the lattice has a Penrose diagram in the strict sense or only an analog
- **Cost**: Not stated
- **Priority**: Not stated

### 55. Geodesic integration in full 12D Lorentzian metric with quantum correction
- **Source**: SP, Section 5 (Q5)
- **What**: Integrate geodesics in the full 12D Lorentzian metric including the quantum Raychaudhuri correction F_Q to determine whether the 12D spacetime during transit is geodesically complete.
- **Inputs**: 12D Lorentzian metric from S50, quantum Fisher information F_Q from W2-4
- **Tests**: Whether persistent SEC violation from F_Q > 0 resolves the cosmological singularity (geodesic completeness)
- **Cost**: Not stated (significant extension of S49 analysis)
- **Priority**: Not stated

---

## Phonon-First Cosmologist (`session-54-phonon-collab.md`)

### 56. Josephson-spectral action correspondence quantitative test
- **Source**: Phonon-First, Section 3 (3.1)
- **What**: Test whether the SA-LATT-OCC minimum satisfies E_C = Lambda^2 / (2 * number of modes below cutoff). At Lambda = 1.0, 13 of 32 modes below cutoff gives E_C ~ 0.038 M_KK. Compare to framework E_C = 1.222 M_KK. The ratio 32x is exactly the mode count.
- **Inputs**: SA-LATT-OCC data, mode count below cutoff, Josephson array parameters from S53
- **Tests**: Quantitative test of the Josephson-spectral action formal correspondence
- **Cost**: LOW
- **Priority**: Not stated

### 57. Bures-Connes failure dimensional analysis
- **Source**: Phonon-First, Section 3 (3.2)
- **What**: Test whether Martinetti-Mercati proportionality is restored at larger N_modes. Predict critical crossover at N_modes > d_s(graph) * N_pair. Analyze whether the monotonic decrease in g_B/g_C is a curvature issue (not mode-count).
- **Inputs**: Bures metric data from W2-3, Connes metric data, graph spectral dimension d_s = 2
- **Tests**: Whether the failure is a curvature mismatch rather than mode count; dimensional mismatch signature
- **Cost**: LOW-MEDIUM
- **Priority**: Not stated

### 58. PL dual Connes distance / T-duality test
- **Source**: Phonon-First, Section 3 (3.3)
- **What**: Compute Connes distance on the AN dual graph (same 32 nodes, dual metric weights). Test d_Connes(AN, tau) * d_Connes(SU(3), tau) = constant (product of dual distances is tau-independent).
- **Inputs**: AN dual graph with dual metric weights, 32-cell lattice Connes distances
- **Tests**: First evidence for T-duality-like correspondence in the framework (spectral T-duality criterion)
- **Cost**: MEDIUM
- **Priority**: Not stated

### 59. Kibble-Zurek domain wall density prediction
- **Source**: Phonon-First, Section 3 (3.4)
- **What**: Apply KZ defect density formula n_defect ~ (tau_Q/tau_0)^{-d*nu/(1+z*nu)} with tau_Q = 0.121, tau_0 = 1.27, d_s = 2, nu = 1/2, z = 2. Predicts ~1-2 topological defects (domain walls/kinks) on the lattice, which would be Jackiw-Rebbi structures.
- **Inputs**: omega_tau = 8.27 (S38), omega_PV = 0.792, d_s = 2, BCS mean-field exponents
- **Tests**: Prediction of 1-2 domain walls on 32-cell graph; identification as Z_2 kinks in pair phase
- **Cost**: LOW
- **Priority**: Not stated

### 60. Quantum metric / Peotta-Torma superfluid weight on the 32-cell graph
- **Source**: Phonon-First, Section 3 (3.5)
- **What**: Compute the Peotta-Torma superfluid weight D_s from the quantum metric g_ij of the lattice eigenstates (Bloch/graph Fourier basis). Test whether D_s is nonzero even in the flat-band limit, providing a route to BCS pairing that bypasses ED-SWEEP-54 failure.
- **Inputs**: 32-cell lattice eigenstates in graph Fourier basis
- **Tests**: Whether geometric Berry curvature contribution to D_s bypasses the DOS-based pairing collapse; whether E_J/E_C = 0.818 (Mott side) can be understood via D_s
- **Cost**: MEDIUM
- **Priority**: Not stated

### 61. Compact quotient Gamma\AN regularization
- **Source**: Phonon-First, Section 5 (5.4)
- **What**: Determine whether there is a natural choice of lattice Gamma in AN from the framework's SU(3) lattice, to regularize the spectral action on the non-compact AN dual space.
- **Inputs**: SU(3) lattice structure, AN group structure
- **Tests**: Whether the PL dual can be regulated by a compact quotient with natural choice of Gamma
- **Cost**: Not stated
- **Priority**: Not stated

### 62. sin^2(theta_W) from normed division algebras
- **Source**: Phonon-First, Section 5 (5.5)
- **What**: Compute sin^2(theta_W) from the normed division algebra R tensor C tensor H tensor O (Boyle-Farnsworth approach) rather than from the Jensen metric eigenvalues.
- **Inputs**: Division algebra structure, Boyle-Farnsworth formulas (Paper 14)
- **Tests**: Whether the weak mixing angle is a division-algebraic invariant rather than a running parameter
- **Cost**: Not stated
- **Priority**: Not stated

---

## Volovik Superfluid Universe Theorist (`session-54-volovik-collab.md`)

### 63. Integrability breaking at N_pair = 2 (detailed)
- **Source**: Volovik, Section 3 (3.1)
- **What**: Compute the N_pair = 2 Fock space (dim 28) including inter-pair interactions (pair-pair scattering, three-body forces). Measure integrability-breaking rate from off-diagonal matrix elements of inter-pair Hamiltonian. Apply 3He-A orbital relaxation analog.
- **Inputs**: BCS Hamiltonian, inter-pair interaction terms
- **Tests**: Whether inter-pair interactions break Richardson-Gaudin conserved integrals and allow thermalization; integrability-breaking rate computation
- **Cost**: MEDIUM
- **Priority**: Not stated (identified as most important S55 computation)

### 64. Two-fluid Landau-Khalatnikov cooling trajectory
- **Source**: Volovik, Section 3 (3.2)
- **What**: Solve d(rho_q)/dt = -3H(rho_q + P_q) + Gamma_dissip(rho_q - rho_eq) with Gamma = Gamma(N_pair, V_pair-pair) extracted from N_pair = 2 Fock space. Track CC from 10^115 to 10^0 over cosmological time.
- **Inputs**: Gamma_dissip from N_pair = 2 computation, w = -0.408, initial CC
- **Tests**: Cosmological history of vacuum energy; whether observed CC at 10^{-47} GeV^4 corresponds to specific elapsed relaxation time t_relax (q-theory prediction)
- **Cost**: MEDIUM (depends on integrability breaking results)
- **Priority**: Not stated

### 65. Flat-band enhancement of pairing at N_pair >= 2
- **Source**: Volovik, Section 3 (3.3)
- **What**: Compute Delta_eff ~ g * N_flat ~ g * 4 (B2 degeneracy) using flat-band linear-T_c formula (Paper 18 eq 7). At N_pair = 2, second pair enters B2, pairing energy scales as sqrt(N_pair). Test d/Delta transition from 42 to O(1).
- **Inputs**: B2 flat band structure, pairing interaction g, N_pair = 2 Fock space
- **Tests**: Whether flat-band enhancement makes pairing competitive with level spacing (d/Delta from 42 to O(1)); pairing collapse threshold crossing
- **Cost**: MEDIUM
- **Priority**: Not stated

### 66. Superfluid density tensor sweep as order parameter
- **Source**: Volovik, Section 3 (3.4)
- **What**: Sweep N_pair from 1 to 4 and track rho_s^{ij}(N_pair) using Peotta-Torma. At N_pair = 1, rho_s = 0 (Mott). If rho_s > 0 at N_pair = 2, Mott-to-superfluid transition occurs.
- **Inputs**: Peotta-Torma formula, lattice eigenstates, N_pair = 1-4 Fock spaces
- **Tests**: Whether Mott insulator transitions to superfluid at N_pair = 2; resolves S53 objections (no condensate, no ODLRO, no phonons)
- **Cost**: Not stated
- **Priority**: Not stated

### 67. Self-consistent Delta(tau) for q-theory crossing
- **Source**: Volovik, Section 3 (3.5)
- **What**: Compute self-consistent BCS gap Delta(tau) and determine whether it modifies the q-theory crossing location (S45 Q-THEORY-BCS-45: tau* = 0.209) toward the fold.
- **Inputs**: BCS gap equation, q-variable = dS/d(Lambda^4)|_{tau_eq}
- **Tests**: Whether the BCS gap shifts the q-theory crossing location toward the fold
- **Cost**: Not stated
- **Priority**: Not stated

### 68. Microscopic Hamiltonian derivation of S_occ
- **Source**: Volovik, Section 2 (assessment of SA-LATT-OCC) and Section 4
- **What**: Derive S_occ from a microscopic energy functional rather than postulating it. Until S_occ can be derived from a microscopic Hamiltonian, the result is provisional.
- **Inputs**: BCS Hamiltonian, spectral action formalism
- **Tests**: Whether S_occ has a microscopic derivation (required condition for physical significance per Volovik)
- **Cost**: Not stated
- **Priority**: Not stated (identified as one of two conditions for S_occ to be physical)

---

## Quantum Acoustics Theorist (`session-54-qa-collab.md`)

### 69. Phonon dispersion relation on the 32-cell lattice
- **Source**: QA, Section 3 (3.1)
- **What**: Compute full dispersion relation omega(k) on the CG graph. Diagonalize H_TB restricted to each bond type separately. Compute overlap matrix between full H eigenstates and bond-type-restricted Laplacian eigenstates. Classify modes as "coset phonons" (C^2) or "stabilizer phonons" (su(2), u(1)). Extract effective group velocities from eigenvalue spacing.
- **Inputs**: H_TB data, bond-type decomposition (50 C^2 + 24 su(2) + 19 u(1))
- **Tests**: Acoustic vs optical branch identification, sub-band structure, sound speed per bond type
- **Cost**: LOW (reuse existing data)
- **Priority**: Not stated

### 70. Phonon density of states on the lattice vs continuum
- **Source**: QA, Section 3 (3.2)
- **What**: Compute phonon DOS g(omega) on 32-cell lattice at multiple tau via kernel density estimation. Compute integrated DOS N(omega), differentiate. Compare van Hove singularity count: continuum has 13, lattice should have far fewer.
- **Inputs**: 32 eigenvalues at each tau, continuum Dirac DOS from S44
- **Tests**: Quantifies spectral information loss in discretization; identifies tau values where lattice best approximates continuum
- **Cost**: LOW
- **Priority**: Not stated

### 71. Acoustic impedance matching at KZ domain boundaries
- **Source**: QA, Section 3 (3.3)
- **What**: Construct two copies of H_TB at tau_1 and tau_2, couple at a boundary node, compute Green's function across junction, extract transmission coefficient via Fisher-Lee relation.
- **Inputs**: H_TB at two different tau values
- **Tests**: Whether phonons transmit or reflect at grain boundary; whether GGE non-thermality is communicated between domains
- **Cost**: MEDIUM
- **Priority**: Not stated

### 72. Anharmonic phonon lifetime on the lattice
- **Source**: QA, Section 3 (3.4)
- **What**: Compute cubic (V_3 = d^3H/dtau^3) and quartic (V_4 = d^4H/dtau^4) anharmonic corrections to H_TB projected onto phonon eigenstates. Use Fermi's golden rule for decay rate.
- **Inputs**: H_TB expanded to 3rd and 4th order in tau
- **Tests**: Quality factor Q of each mode; whether selection rules differ on graph vs regular crystal; dynamical accessibility of S_occ minimum
- **Cost**: MEDIUM-HIGH
- **Priority**: Not stated

### 73. Connes distance group velocity (expansion anisotropy)
- **Source**: QA, Section 3 (3.5)
- **What**: For each of 496 node pairs, compute d(d_D)/dtau by finite differences across 10 tau points. Classify by bond type and compute mean expansion rate per bond type. Extract anisotropy tensor (acoustic birefringence).
- **Inputs**: Connes distance data (10 tau points, 496 pairs), bond type classification
- **Tests**: Anisotropy of expansion; which SU(3) directions expand preferentially
- **Cost**: LOW
- **Priority**: Not stated

### 74. Zero-point fluctuations in the S_occ minimum
- **Source**: QA, Section 3 (3.6)
- **What**: Extract d^2(S_occ)/dtau^2 at minimum. Compute omega_0 = sqrt(d^2S/dtau^2 / G_DeWitt). Compare barrier crossing rate exp(-S_barrier/omega_0) to 1.
- **Inputs**: S_occ data from SA-LATT-OCC-54
- **Tests**: Whether zero-point energy omega_0/2 exceeds the 5.35% barrier; whether minimum is quantum-mechanically stable
- **Cost**: LOW
- **Priority**: Not stated

### 75. Sensitivity of E_GGE to excited phonon modes and quench protocol
- **Source**: QA, Section 5 (5.4)
- **What**: Compute how E_GGE = 1.688 depends on the number of excited phonon modes (currently 8), pairing strength, and quench protocol. Determines robustness of the w = -0.408 prediction.
- **Inputs**: GGE state data, BCS spectrum parameters
- **Tests**: Sensitivity of w = -0.408 equation of state to parameter variations
- **Cost**: Not stated
- **Priority**: Not stated

### 76. Spectral dimension d_s = 2 and its role in pairing collapse
- **Source**: QA, Section 5 (5.5)
- **What**: Analyze whether the graph Laplacian spectral dimension d_s = 2 (not 8) explains the pairing collapse better than the simple DOS argument. In 2D: stronger thermal fluctuations (Mermin-Wagner), logarithmic sound propagation, BCS crossover rather than phase transition.
- **Inputs**: Graph Laplacian spectral dimension data, BCS theory in 2D
- **Tests**: Whether d_s = 2 provides a deeper explanation for pairing collapse than d/Delta = 42
- **Cost**: Not stated
- **Priority**: Not stated

### 77. Acoustic metric and spectral metric unification condition
- **Source**: QA, Section 5 (5.3)
- **What**: Determine conditions under which the BLV acoustic metric a_BLV and the Connes spectral metric a_Connes agree. Their ratio is a_BLV/a_Connes ~ sqrt(rho * J_{C^2} / c_s).
- **Inputs**: BLV acoustic metric from S53, Connes spectral metric from S54
- **Tests**: Under what conditions the geometry seen by phonons equals the geometry defined by the Dirac operator (acoustic version of spectral action principle)
- **Cost**: Not stated
- **Priority**: Not stated

---

## Baptista Spacetime Analyst (`session-54-baptista-collab.md`)

### 78. Non-trivial bundle topology for A-tensor (from NCG inner fluctuations)
- **Source**: Baptista, Section 3 (S55-1)
- **What**: Compute O'Neill A-tensor with background SU(2) x U(1) gauge field from NCG inner fluctuations. Extend submersion to principal bundle P -> M^4 with fiber SU(3). A-tensor for principal bundles: A_X Y = (1/2) F_A(X,Y)^vert, giving |A|^2 = (1/4)|F_A|^2. Test whether BCS U(1)_7 breaking generates effective gauge field via Higgs mechanism.
- **Inputs**: NCG inner fluctuation formalism (Paper 15 eq 2.33), S35 U(1)_7 breaking result
- **Tests**: Whether inner fluctuations or spontaneous U(1)_7 breaking produces nonzero A-tensor; whether this provides missing geometric expansion channel through F_A contributions
- **Cost**: MEDIUM
- **Priority**: IMMEDIATE (Baptista's top priority)

### 79. Cutoff function family for S_occ (Fermi-Dirac interpolation)
- **Source**: Baptista, Section 3 (S55-2)
- **What**: Compute S_occ for f_alpha(x) = [1 + e^{alpha(x-1)}]^{-1} family, with alpha -> inf recovering sharp and alpha ~ 1 approximating smooth. Track barrier height as function of alpha.
- **Inputs**: Existing eigenvalue data
- **Tests**: If barrier vanishes at finite alpha, minimum is lattice artifact. If persists for alpha >= 5, mechanism has a chance.
- **Cost**: LOW
- **Priority**: IMMEDIATE (Baptista)

### 80. S_occ on 64 and 128-cell lattices
- **Source**: Baptista, Section 3 (S55-3)
- **What**: Construct 64 and 128-cell lattices by extending Casimir cutoff to higher representations. Compute S_occ. Track whether barrier grows with N (convergent) or shrinks as 1/N (finite-size effect).
- **Inputs**: Higher SU(3) irreps, extended CG graph construction
- **Tests**: Whether barrier persists, grows (convergent), or shrinks (1/N finite-size effect)
- **Cost**: MEDIUM-HIGH
- **Priority**: IMMEDIATE (Baptista)

### 81. Continuum Connes distance at max_pq_sum = 6
- **Source**: Baptista, Section 3 (S55-4)
- **What**: Compute continuum Connes distances at max_pq_sum=6 (full 992-mode spectrum) using SDP formulation from W1-2. Bridge lattice (2.117x) and continuum (~1.1x at max_pq_sum=3) discrepancy.
- **Inputs**: 992-mode Dirac spectrum, SDP formulation
- **Tests**: Whether lattice and continuum Connes distances converge as resolution increases
- **Cost**: HIGH (992-mode SDP)
- **Priority**: Not stated (deeper geometric computation)

### 82. Off-Jensen full trajectory dynamics
- **Source**: Baptista, Section 3 (S55-5)
- **What**: Integrate equations of motion G_ij ddot(q^j) + Gamma^i_jk dot(q^j) dot(q^k) = -dV/dq^i in (tau, sigma) plane with DeWitt metric and KK potential. Start from tau=0, dot(tau)=v_terminal, sigma=dot(sigma)=0.
- **Inputs**: DeWitt metric G_ij, KK potential, nonlinear cross-coupling H_{tau sigma} = -309.8
- **Tests**: Whether trajectory remains within sigma < 0.02 through transit; nonlinear dynamics at speed bump
- **Cost**: MEDIUM
- **Priority**: Not stated

### 83. Three-parameter volume-preserving landscape
- **Source**: Baptista, Section 3 (S55-6)
- **What**: Map full 3D volume-preserving landscape V(tau, sigma_2, sigma_3) in U(2)-invariant metric moduli space. Third direction T3 has largest positive eigenvalue (+1775 from S29Bb).
- **Inputs**: Paper 15 Section 3.5, full 3-parameter family structure
- **Tests**: Whether Jensen trajectory is minimum-energy path in full 3D moduli space
- **Cost**: HIGH
- **Priority**: Not stated

### 84. Off-Jensen sin^2(theta_W) at valley floor
- **Source**: Baptista, Section 3 (S55-7)
- **What**: Compute sin^2(theta_W) at valley floor sigma* = 0.0148 using Paper 13 eq 5.25 with the 12.5% C^2 enhancement from W3-6.
- **Inputs**: Paper 13 eq 5.25, valley floor displacement sigma* = 0.0148, C^2 enhancement data
- **Tests**: Whether off-Jensen displacement improves the Weinberg angle from 0.584 toward observed 0.231
- **Cost**: LOW
- **Priority**: Not stated

### 85. Lichnerowicz stability (Lauret-Schwahn) at the fold
- **Source**: Baptista, Section 4 (4.4)
- **What**: Apply Lauret I universal formula (Paper 37) via Casimir operators on G-invariant TT tensors. Determine whether Jensen metric at fold is dynamically stable under linearized gravity. Schwahn (Paper 39) found 51 new stable examples. Test whether Jensen metric is in stable or unstable class.
- **Inputs**: Lauret-Schwahn universal formula, Jensen metric data, G-invariant TT tensor decomposition
- **Tests**: Whether the Jensen deformation endpoint is dynamically stable (decisive for geometric interpretation)
- **Cost**: MEDIUM-HIGH
- **Priority**: Not stated (described as "single most important uncomputed gate from Baptista library")

### 86. Connes distance with inner fluctuations (fluctuated Dirac operator)
- **Source**: Baptista, Section 5 (5.2)
- **What**: Extend SDP formulation to the fluctuated Dirac operator D -> D + A + JAJ^{-1}. Determine whether inner fluctuations suppress or enhance Connes distance growth.
- **Inputs**: Fluctuated Dirac operator, SDP formulation from W1-2
- **Tests**: Sign of inner fluctuation effect on Connes distance expansion (bounded modification, sign matters)
- **Cost**: Not stated
- **Priority**: Not stated

---

## Summary

**Total suggestions extracted: 86 from 8 documents (7 individual reviewers + 1 master synthesis)**

Reviewer breakdown:
- Master Synthesis: 28 suggestions (C1-C4, H1-H5, M1-M14, L1-L5)
- Tesla Resonance Theorist: 10 suggestions (#29-38)
- Feynman Theorist: 9 suggestions (#39-47)
- Schwarzschild-Penrose Geometer: 8 suggestions (#48-55)
- Phonon-First Cosmologist: 7 suggestions (#56-62)
- Volovik Superfluid Universe Theorist: 6 suggestions (#63-68)
- Quantum Acoustics Theorist: 9 suggestions (#69-77)
- Baptista Spacetime Analyst: 9 suggestions (#78-86)

Note: Many suggestions from individual reviewers overlap with or are more detailed versions of the master synthesis entries. The master synthesis consolidated suggestions from multiple reviewers into its priority-ordered list (C1-C4 CRITICAL, H1-H5 HIGH, M1-M14 MEDIUM, L1-L5 LOW). Individual reviewer entries preserve the original framing, additional detail, and distinct emphasis not captured in the master synthesis.
