# Spectral Geometry Detailed Results

## Heat Kernel on Jensen-Deformed SU(3)

### Peter-Weyl Decomposition
- Bi-invariant: Tr(exp(-tD^2)) = sum_rho d_rho exp(-t C_rho)
- Jensen-deformed: breaks G_L x G_R -> G_L x U(2)_R
- Casimir eigenvalues SPLIT by U(2) branching (B1, B2, B3)
- Block-diagonality theorem: exact in Peter-Weyl, verified to 8.4e-15

### Seeley-DeWitt Coefficients
- a_0 = (4pi)^{-4} * Vol(SU(3)) -- tau-independent (TT constraint)
- a_2 = (4pi)^{-4} * (1/6) integral R dV -- varies with tau
- a_4 involves R^2, Ric^2, Riem^2 -- a_4/a_2 = 1000:1 (V_spec monotone)
- V_spec monotone closure: no Starobinsky minimum from Seeley-DeWitt

### Strutinsky Decomposition of RPA-32b Curvature
- Total: d^2(sum|lambda|)/dtau^2 = 20.43 at tau=0.20
- B1: 3.38 (16.5%), per-mode d2 = 1.689
- B2: 9.44 (46.2%), per-mode d2 = 1.179
- B3: 7.61 (37.3%), per-mode d2 = 1.268
- Thouless decomposition (orthogonal): diagonal 16.19 + off-diagonal 4.24

### Sector Universality (SECT-33a)
- (0,0): tau_min = 0.19016, d2 = 1.18, 4-fold
- (1,0): tau_min = 0.18616, d2 = 15.14, 3-fold cluster
- (0,1): identical to (1,0) by conjugation (1e-16)
- d2 does NOT correlate with Casimir C_2 (correlation 0.54)
- (1,1) adjoint has SMALLEST d2 = 0.62 (Trap 5 suppression)

## Kosmann Pairing Kernel
- Full kernel: V_nm = sum_{a=0..7} |<n|K_a|m>|^2
- C^2 generators (a=3,4,5,6): V(B2,B2) = 0 EXACTLY (U(1) charge conservation)
- SU(2) generators (a=0,1,2): V(B2,B2) = 0.037
- U(1) generator (a=7): V(B2,B2) = 0.250 (doublet pairing)
- Total: V(B2,B2) = 0.287
- V(B1,B2) = 0.124-0.168 (shell-crossing channel)

## Lichnerowicz Bound Check (proposed, still uncomputed)
- Dirac on 8-dim: lambda_1^2 >= (2/7) R_min
- At fold: lambda_B1_min ~ 0.819, so R_min <= (7/2)*0.819^2 = 2.35
- Should verify against explicit R(tau=0.190) from Baptista Paper 15

## Spectral Flow
- No zero-crossings along Jensen curve (all branches positive for tau > 0)
- SF(D_0, D_tau) = 0 for all tau
- Eta invariant preserved along deformation (PH forces eta = 0)
- D_phys spectral flow: UNCOMPUTED. eta(D_phys) likely nonzero at phi > 0

## Session 34 V-Matrix Analysis
- Frame V: V_nm = sum_a |A^a_{nm}|^2 in 8x8 tangent space. V(B2,B2)_max = 0.287
- Spinor V: V_nm = sum_a |<psi_n|K_a|psi_m>|^2 in 16x16 spinor space. V(B2,B2)_max = 0.057
- Relationship: K_a = (1/8) sum_{rs} A^a_{rs} gamma_r gamma_s
- Tr(V_spinor(B2)) != 0, Tr(V_frame(B2)) = 0 (antisymmetry). INCOMMENSURABLE
- Optimization over U(4): max V_offdiag ~ 0.057 (Schur's lemma prevents improvement)
- Tesla proof: Casimir eigenvalues on B2 all = 0.1557 (irreducible)
- Frame V exceeds spectral upper bound of sum_a K_a^dag K_a -> cannot exist in spinor space

## Session 34 Chemical Potential Closure
- Canonical: PH symmetry {gamma_9, D_K}=0 -> eigenvalue pairing -> dS/dmu|_0 = 0
- Grand canonical: N = iK_7 (conserved, [iK_7, D_K]=0). Helmholtz F(mu) convex, min at mu=0
- dF/dmu = mu * d<N>/dmu -> vanishes at mu=0 trivially. d^2F/dmu^2 > 0 strictly
- Connes 15 (arXiv:1809.02944): entropy = spectral action
- Connes 16 (arXiv:1903.09624): grand canonical spectral action. Bessel coefficients. JNCG 2022

## Van Hove Enhancement Details
- B2 fold: tau_fold=0.190, v_B2=dE/dtau=0 (1D van Hove singularity)
- Wall 2 [0.15, 0.25] straddles the fold
- Physical cutoff v_min = 0.012 (from eigenvalue variation across wall)
- rho_smooth = integral 1/(pi*max(|v|,v_min)) dtau = 14.02/mode
- Step-function rho = 5.40/mode. Enhancement factor = 2.6x
- Critical v_min for M=1: 0.085 (7.2x safety margin)
- CAVEAT: Multi-sector fold misalignment (delta_tau=0.004) may broaden peak
