---
name: Permanent Structural Results
description: All proven theorems, permanent structural constraints, and algebraic identities from KK geometry on SU(3). Includes constraint landscape and selection rules.
type: project
---

# Permanent Structural Results

## Proven Theorems (Machine Epsilon)

1. **KO-dim = 6 mod 8**: (epsilon, epsilon', epsilon'') = (+1, +1, -1). Parameter-free. [S7-8, foundations-detail.md]
2. **Block-diagonality**: D_K exactly block-diagonal in Peter-Weyl. ANY left-invariant metric on compact semisimple Lie group. [S21]
3. **[J, D_K] = 0**: CPT invariance. J = charge conjugation on Cliff(R^8). Promoted to non-perturbative polynomial spectral sum (S74 BDSPT). [S21, S74]
4. **[R_g, D_K] = 0**: Right-invariance of left-invariant metric Dirac. Logically independent from [J,D_K]=0. [S73B]
5. **Spectral pairing**: D_K anticommutes with gamma_9 => Tr(D_K)=0 identically. [S32]
6. **Trap 4 (Schur)**: dDK/dtau U(2)-equivariant; B1/B2/B3 inequivalent irreps => inter-branch matrix elements vanish. Holds on full U(2) 3-param family. [S33]
7. **Trap 5 (J-reality)**: Particle-hole matrix elements vanish for real reps (B1, B3). Numerically machine-precision; analytic proof for c'' in iR complete, c''=0 open. [S33]
8. **g1/g2 = e^{-2tau}**: 67/67 Baptista equations verified. [S33a]
9. **Volume-preserving TT stability**: All 31 TT Lichnerowicz eigenvalues positive at all tau. [S55, S60]
10. **phi_paasch = 1.531580**: [S12]
11. **AZ class BDI**: [S24]
12. **Perturbative exhaustion**: All perturbative stabilization routes closed. [S20]
13. **DNP instability**: Product Einstein + R>0 always G-unstable. [S59, Paper 28 Sec 7]
14. **Pomeranchuk f(0,0) = -4.687** (MATH ONLY): Perturbative identity permanent. Physical instability RETRACTED per S75 W4-K — fabric Pomeranchuk-STABLE at z=6. [S28, reclassified S75/S76]
15. **Clock constraint**: g_1/g_2 = e^{-2tau} gives 15,000x clock violation, closes rolling quintessence. [S33a]
16. **Jensen line = attractor valley**: dS/d(eps_perp) = 0 on Jensen line (Schur's lemma, U(2) invariance). [S69]

## Permanent Spectral/Geometric Results

- **f_conv = (M_KK/M_Pl)^4*(a_2/a_0)^2 = pi^4/(9216*a_0^2)**: Analytically derived from spectral perturbation theory on D_K. R-protected (4.4% drift). BCS-immune. Cutoff-independent. PROMOTABLE TO PERMANENT. [S76 W1-F, W2-A]
- **f_conv family monotone decreasing**: f_conv^{(0)}=1.371e-9, f_conv^{(2)}=2.547e-10, f_conv^{(4)}=6.030e-11. f^{(4)}/f^{(2)}=(a_4/a_2)^2=0.2367. [S76 W2-B]
- **Jensen ridge structure**: 35/35 off-Jensen Hessian eigenvalues negative [-148.69, -17.35]. Fold = strict local max of S(g). Ridge: roll along Jensen (dS/dtau>0), confined transversely (all V-eigenvalues positive). [S76 W2-J]
- **Instanton liquid closure**: |V_liquid/V_bare| bounded by N_BCS/N_total ~ 8/6440 ~ 10^{-3}. V_eff monotonic regardless of instanton treatment. [S76 W3-D]
- **JLO/CM closure**: CM_factor = 1 exactly for finite spectral triples. eta(D_K)=0, ind(D_K)=0. [S76 W3-C]
- **Modulus decay gravity-dominated**: Lambda_eff = 37*M_Pl from sqrt(Z_fold)=273. SM channel = 0.8% of total. [S76 W2-E]
- **Level 0/1 separation**: f_conv applies to perturbations only. Background Friedmann uses (M_KK/M_Pl)^2 directly. [S76 W3-B]
- **sin^2(theta_W)|_{M_KK} = 0.5839** = 3*exp(-4*tau)/(3*exp(-4*tau)+1). Formula from Paper 13 eq 5.21. [S33a, S72]
- **A-tensor formula**: |A_coset|^2 = 3/2 + (3/2)e^{-4tau}. ALL U(2)-invariant metrics. [S55]
- **A-tensor correction to CORE**: eps_AT = (H_0/M_KK)^2 = 3.7e-118. Flat-base justified to 1 part in 10^116. [S74]
- **H_f(Lambda) = H_f(1)/Lambda EXACTLY for f(x)=sqrt(x)**. Lambda_crit = 5.033 M_KK. [S66]
- **a_2^{bos}/a_2^{Dirac} = 61/20 = 3.05 exactly**, tau-independent. [S44]
- **K(u(1), su(2)) = 0 at ALL tau**. K(u(1), C^2) = 1/16 at ALL tau. [S47]
- **Sigma scaling = sigma^{-1/8} exactly** (Casimir energy). No exponential corrections at one-loop. [S63]
- **R_protected_fold = (c_0 c_4/c_2^2) * |Riem|^2/R^2**: Pure curvature invariant on d=8. Vol(K) cancels exactly. Value = 1.1287. [S73B]
- **Partition rigidity**: Sym^2(su(3)^*) under U(2) gives (n_b, n_f)=(20, 16) uniquely. [S74 N-EFF]
- **Hessian Ad(U(2)) decomposition**: 36 eigenvectors in 6 C_2 eigenspaces: dims {5,6,8,6,8,3}. [S63]
- **Threshold ratios exact**: T_2/T_3=1, T_Y/T_3=4/3 for ALL SU(3) irreps. delta_2/delta_3=1, delta_1/delta_3=20/9. [S73a]
- **L=7 sign reversal**: ALL omega_min(L=7) > Lambda=2.048 M_KK. Sum oscillates. [S70]
- **CCM matching**: lambda=(4/3)*g3^2*(a4/a2) couples alpha_s and m_H through single DOF g3^2(M_KK). [S70]
- **Cheung EFT violated at fold**: H/Lambda_strong = 8.89. Spectral action IS the UV completion. [S67]
- **Fold metastability <=> CC cancellation**: S_B = 24*pi^2*M_Pl^4/V. [S62]

## Permanent Theorems from Yukawa/Chirality

- **Tr(gamma_9 dD^a dD^b) = 0 identically**: Quadratic chiral trace structural zero. [S65]
- **C^2 coset degeneracy on Jensen line**: All 4 non-Killing dirs give identical Yukawa. [S65]
- **Y = lambda*I_4 for ALL U(2)-invariant metrics** (Schur lemma). Generation hierarchy REQUIRES off-Jensen. [S66]
- **C^2 selection rule**: Coset contribution to d(m^2_B2)/dtau = 0 exactly. Mass variation = u(1) vs su(2) only. [S54]

## Permanent Closures

- **a_0/a_2 = 6/R for ALL left-invariant metrics**: CC landscape closed within left-invariant geometry. [S65]
- **FUNCTIONAL-SELECT FAIL PERMANENT**: Peter-Weyl/Schur orthogonality of trivial vs non-trivial reps. [S73B]
- **Unimodular gravity cannot emerge from EH on M^4 x K via fiber volume preservation**: [S60]
- **Paper 13 tree-level three-coupling fit forces lambda_3 < 0**: Metric positivity FAIL scheme-independent. [S74 HETEROTIC-LR]
- **sin^2(M_Z)=-0.046 from universal thresholds**: U(1) threshold 2.22x too large. [S73a]
- **L-R threshold correction makes Weinberg angle WORSE**: sin^2=-0.308 with L-R direct (delta*L_a). Sign problem: L_1>1 amplifies delta_1. Tree-level L-R route CLOSED. [S77]

## Selection Rules (Complete, S33)

delta_D_K nonzero ONLY: (a) same (p,q) sector (block-diag), (b) same branch (Trap 4), (c) particle-hole of complex reps (Trap 5). Active DOF: off-diagonal B2-to-B2 particle-hole.

## J/gamma_9/CPT Decomposition

- J: eigenvalue-PRESERVING, chirality-REVERSING
- gamma_9: eigenvalue-REVERSING, chirality-REVERSING
- J*gamma_9: eigenvalue-REVERSING, chirality-PRESERVING (full CPT)
- Fold/anti-fold pair related by GAMMA_9 (not J). BCS pairs (psi+, gamma_9*psi+).

## Constraint Landscape

- **F/B=0.55** (Trap 1), **b_1/b_2=4/9** (Trap 2), **e/(ac)=1/16** (Trap 3)
- **V_spec monotone** (all smooth cutoffs, both connections)
- **Mechanism chain**: I-1, RPA, Turing, WALL, BCS all PASS at mean-field; broken at self-consistent level (TAU-STAB-36)
- **S_full monotone**: dS/dtau=+58,673, d2S/dtau2=+317,862. BCS shortfall ~376,000x
- **[iK_7, D_K] = 0**: U(1)_7 exact. K_7 unique surviving Killing. q_B2=+-1/4, q_B1=q_B3=0
- **Gap protected by Schur**: B2/B3 cannot mix on U(2) surface. Closure requires breaking U(2)
- **N_e = 0.1734**: Saturation theorem (structural, tau/velocity/M_KK independent)

## Geometric Conjecture (Baptista-Berry, OPEN)

"On compact Lie group K with left-invariant metric g_K and residual right-isometry H, ph matrix elements of dD_K/dtau vanish for ad(H)-submodules (B1, B3) and are generically nonzero for coset branches (B2)."
