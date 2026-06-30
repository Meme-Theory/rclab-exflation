---
name: Spectral Results (compressed S34-S84)
description: Compressed per-session computation log for spectral-geometer (heat-kernel, eigenvalue bounds, Lichnerowicz, fabric, transit)
type: project
---

# Heat Kernel on Jensen-Deformed SU(3)

- Bi-invariant: Tr(exp(-tD^2)) = sum_rho d_rho exp(-t*C_rho)
- Jensen deformation: G_L x G_R -> G_L x U(2)_R; Casimir SPLIT by U(2) branching (B1, B2, B3)
- Block-diagonality: exact in Peter-Weyl, verified to 8.4e-15
- a_0 = (4pi)^{-4} * Vol(SU(3)) tau-independent (TT constraint)
- a_2 = (4pi)^{-4} * (1/6) integral R dV varies with tau
- a_4 involves R^2, Ric^2, Riem^2; a_4/a_2 ~ 1000:1 (V_spec monotone -- no Starobinsky)

# Strutinsky decomposition (S33)

- Total d^2(sum|lambda|)/dtau^2 = 20.43 at tau=0.20
- B1: 3.38 (16.5%, per-mode 1.689). B2: 9.44 (46.2%, per-mode 1.179). B3: 7.61 (37.3%, per-mode 1.268)
- Thouless decomposition: diagonal 16.19 + off-diagonal 4.24
- (0,0) tau_min = 0.19016, d2=1.18, 4-fold. (1,0) tau_min = 0.18616, d2=15.14. (1,1) adjoint smallest d2=0.62 (Trap 5)

# Kosmann Pairing

- Full kernel V_nm = sum_{a=0..7} |<n|K_a|m>|^2
- C^2 generators (a=3,4,5,6): V(B2,B2) = 0 EXACTLY (U(1) charge conservation)
- SU(2) (a=0,1,2): V(B2,B2) = 0.037. U(1) (a=7): V(B2,B2) = 0.250. Total V(B2,B2) = 0.287
- V(B1,B2) = 0.124-0.168 (shell-crossing). Frame V vs Spinor V INCOMMENSURABLE (Schur prevents > 0.057 in spinor basis)

# Van Hove Enhancement

- B2 fold: tau_fold = 0.190, v_B2 = dE/dtau = 0 (1D van Hove)
- Wall 2 [0.15, 0.25] straddles fold. Physical cutoff v_min = 0.012
- rho_smooth = 14.02/mode, rho_step = 5.40/mode. Enhancement 2.6x. Critical v_min for M=1: 0.085 (7.2x safety)

# Chemical-Potential / PH (S34, S56)

- Canonical mu=0 theorem (single cell): {gamma_9, D_K} = 0 -> dS/dmu|_0 = 0 EXACT
- Grand canonical: N = iK_7 ([iK_7, D_K] = 0). F(mu) convex, min at mu=0
- **S56 mu_eff = -0.201 M_KK at fold** (PASS): PH BROKEN at fabric (non-bipartite graph + Casimir disorder); 0.22% of Josephson slope (insufficient for stabilization)

# Lichnerowicz / Friedrich-Kirchberg (S46, S52)

- FK bound 5R/16 = 0.631 at fold (tightest). Actual lambda_1^2 = 0.672. Tightness 1.065 (6.5% gap)
- All bounds SATISFIED. R(0.19) = 2.018 to machine epsilon

# TT-Lichnerowicz (S48-49 PASS, PERMANENT)

- Singlet (0,0): 31 TT modes, 8 branches. lambda_min = 0.322 at fold. Tr = 15.0 exact. R(0)=2.0, R(0.19)=2.018
- Transversality: at tau=0 ALL 8 div constraints trivial (n_TT=35); at tau>0 four C^2 div constraints activate (rank=5, n_TT=31); 4 u(2) div constraints trivial at all tau
- Bi-invariant evals: 1/3 (deg 27), 3/4 (deg 8). 8-branch fold spectrum: {0.322, 0.325, 0.342, 0.342, 0.345, 0.347, 0.627, 0.939}
- Non-LI extension (S49): (1,0) and (0,1) sectors, 81 modes each, lambda_min(fold) = 1.047 (3.26x singlet floor). C_2 grows as ~(p^2+q^2+pq)/3 -- stability increases. KK graviton tower positive-definite. PERMANENT

# Spectral Flow / Eta (S60)

- eta(D_K) = 0 EXACT at all tau (pair_err 2.22e-14). 21 sectors, 6048 distinct evals, 159936 PW. N+ = N- = 79968. Spectral flow = 0
- STRUCTURAL: Clifford dim-8 pairing + conjugate sector bijection. Mechanism 5 CLOSED

# pi-sector classification (S47 PASS)

- 13 pi-phases: B1=1 (PW=15), B2=9 (PW=81), B3=3 (PW=35). Rank-based within each PW sector
- [iK_7, D_K]=0 ONLY in (0,0) sector; in higher PW ||[I tensor iK_7, D_K]||/||D_K|| = 7.5% for (0,1)
- BCS-accessible pi-phase ratio: 81/59.8 = 1.35x (B2 only) or 116/59.8 = 1.94x (B2+B3)

# Spectral Zeta / Moments / Form Factor (S46)

- a_2^{SD} = 0.728 (geometric, Gilkey-exact). zeta_D(1) = 2776.17 (spectral sum). Ratio 3812 STRUCTURAL (pole at s=1 for d=8)
- R(0.19) = 2.018. SFF: Poisson class. <r> = 0.439. t_H = 748. No GUE ramp
- Spectral current alpha_j = 4.03 (FAIL, UV-dominated). alpha_v = 0.62 (INFO)

# Weyl Verification (S61)

- Vol_heat = 1365.43 vs Vol_analytic = 1349.74 (1.16% error). C_8 = 1/(384*pi^4)
- Heat-trace a_0 extraction at t_match = 23.77. F(t) = (4 pi t)^4 K(t) = a_0 = 16*Vol(SU(3))
- N_PW/N_Weyl = 1044x (NOT in Weyl regime; need L~210). d_eff(PW) = 5.83
- VALIDATES eigenvalue data + volume normalization

# Heat-Kernel a_2 (S61 FAIL)

- a_2^{SD}(fold) = 0.728235 finite. M_Pl(geom)/M_Pl(obs) = 0.654 (shortfall 2.34x in M_Pl^2)
- H_0 = 106.6 km/s/Mpc OUTSIDE [40,100]. Gravity route only viable. Kerner overshoots 4.44x. f_2 = 2.34 would restore match
- Spin-curv ratio (PASS): K/(20R) = 0.01324 at fold; tr_S(Omega^2) = -2|Riem|^2 = -1.069. Scalar 13.454, spin -0.178. 1.3% correction; STRUCTURAL: K/(20R) < 2% for all U(2)-invariant SU(3) metrics. Simplified a_2 valid.

# One-Loop n_s (S63 PASS, MARGINAL)

- |delta(n_s)| = 0.00103 < 0.0021 threshold. n_s(tree) = 0.9567, n_s(1-loop) = 0.9557
- delta(epsilon_H) = +0.00052. Modification factor (1+beta)^2/[(1+alpha)(1+gamma)] = 1.0239
- S_1loop/S_fold = 2.3%. Gilkey n_s structurally unchanged (local geometric invariant). sigma_total = 0.0027 Runge-dominated

# Mechanism Chain Status (Post-40)

- Chain UNCONDITIONAL (S35) -> BROKEN at tau-stabilization (S36-S40)
- Structural Monotonicity Theorem: <lambda^2>(tau) monotonic => S_f(tau) monotonic for any monotone f
- HESS-40: 22/22 transverse positive, min H = +1572 (g_73), margin 1.57e7. Jensen fold = 28D local min of S_full
- Hessian hierarchy: diagonal u(2) ~20000, complement ~14000, off-diag u(1)-complement ~1572. Cond 12.87
- 27 total equilibrium closures: spectral action cannot stabilize tau in ANY direction
- FRIED-39 worsens to ~114,000x with M_ATDHFB=1.695 (SELF-CONSIST-40)

# BdG Spectral Triple (S35, R3 complete)

- C3/C4 PASS, eta=0, spectral flow=0, Goldstone pinning by J. KO-dim convention OPEN
- Publishable JNCG: first BdG spectral triple on compact Lie group. Lichnerowicz bound RETRACTED

# Sessions 37/40/45 (compressed)

- CUTOFF-SA-37 FAIL: S_f(tau) monotonic ALL cutoffs. da_6/dtau = -1058 dominates. CLOSED
- T-ACOUSTIC-40 PASS, B2-INTEG-40 PASS, QRPA-40 FAIL(STABLE), GSL-40 PASS, CC-TRANSIT-40 PASS
- Analytic torsion CLOSED: T ~ 10^{20301} truncation artifact. T_singlet = 0.147 (physical, O(1))

# Fabric (S56)

- FABRIC-STABILIZATION-56 MASTER FAIL: F_fabric(tau) monotonically increasing. Josephson dominates
- Josephson hierarchy inversion: J_C2(tau)^2 (single eigenvalue) controls F_fabric; F_anom (all-mode) is 15% correction
- Fabric integrability PRESERVED: <r> = 0.367 (Poisson). Josephson preserves Richardson-Gaudin
- Adiabatic protection: 2-cell gap 13.04 M_KK (35x single-cell). P_exc = 6.6e-4. GGE -> GS
- CC reframing: CC = adiabaticity problem, NOT integrability problem

# Spectral Dimension (S56, S59)

- S56 d_s^peak = 1.732 at E = 1.159 M_KK (TB, 32-cell). At omega_J -> 1.656, 2*Delta -> 1.713 (rising flank). Smooth, no threshold features
- d_s^peak(TB) = 1.73 < d_H = 1.93 < d_W = 2.15. Fold invisible to d_s^max. d_s as CC probe: CLOSED (kinematic, not dynamical)
- S59 STRUCTURAL: d_s(rep graph) = rank(G) = 2 for SU(3). (p,q) lattice IS 2D triangular. d_s converges 0.93 -> 2.09 over mpq=1..8. Weighted (Josephson) 0.78 -> 1.80. Not a probe of SU(3) manifold dim 8
- S84 W9b-105 FAIL: spec dim at fiber-transition scale = 4.895, outside [2.0, 4.0]. Boundary-dominated extractor

# G_2 Viability (S59 INFO)

- G_2 score 1/3. KO-dim=6 PASS (d=14, 14 mod 8=6). SM FAIL: 128-spinor under G_2->SU(3) has ZERO singlets (12 triplets, 32 octets, 24 sextets, 60 fifteens). Van Hove not found
- STRUCTURAL: dim>8 internal spaces fail singlet test

# S52, S54

- S51: Cutoff non-universality permanent (chi_SA involves f'(x)). S52: FK bound 5R/16=0.631, tightness 1.065. Torsion 0.147
- S54: SA-LATT-OCC PASS (5.35% barrier at fold, sharp Lambda=1). S_vac monotonic; S_occ non-monotone. GUTZWILLER-SU3-54 PASS: BT osc/smooth = 1.27. Berry-Tabor required (integrable)

# Proven Structural Results (PERMANENT)

- KO-dim=6, SM quantum numbers, [J,D_K]=0 (CPT), D_K block-diagonal (PW)
- Trap 1: V(B1,B1)=0 (U(2) singlet). Trap 4: inter-branch Schur. Trap 5: M_ph imaginary
- [iK_7, D_K]=0 at all tau. PH x U(1)_7 = full symmetry algebra for tau>0
- Geodesic flow INTEGRABLE (Berry-Tabor, not Gutzwiller)
- S56: PH of D_K does NOT extend to H_TB (fabric non-bipartite). mu_eff = -0.201 at fold
- S56: Josephson hierarchy inverts SD: single J_C2 controls, spectral sums F_anom are corrections
- S56: d_s as CC probe CLOSED
