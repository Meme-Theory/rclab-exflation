---
name: Session Results Consolidated
description: Gate verdicts and key results from sessions 29-63 relevant to KK theory, organized by topic
type: reference
---

# Modulus Equation (S33 W3 R2)

- V_eff = V_FR(tau) + eta*V_spec(tau). eta = f_4/(f_8*Lambda^4), ONE free parameter.
- FR double-well at beta/alpha=0.28: barrier tau=0.1517, true min tau=0.4412.
- Domain walls for eta<0.12. Width 1.3-2.7 M_KK^{-1}. Dump point tau=0.19 NOT V_eff min.
- SWALLOWTAIL (A_4): At (0.28, 0.05), two derivatives vanish. Trapping unconditional for any Delta>0.
- Scripts: `s33w3_modulus_equation.{py,npz}`

# BCS + Domain Wall (S29, S32)

- KC-1 through KC-5: ALL PASS. Jensen saddle: 2/4 transverse eigenvalues negative.
- At eps_T2=0.049: sin^2(theta_W)=0.231 exactly.
- J_perp=1/3 (Schur). d_eff>=2. Multi-sector BCS mandated. One free parameter: M_KK.
- RPA-32b PASS: chi=20.43, 38x margin. W-32b PASS: Van Hove at walls.
- Domain wall = spatially varying fiber metric = Einstein-Bergmann dilaton on SU(3).

# Corrections + Structural (S34)

- TRAP-33b RETRACTED: A_antisym (frame) != K_a_matrix (spinor). Different vector spaces.
- Van Hove at fold: rho_smooth=14.02/mode (2.6x over step). v_B2=0 at tau_fold=0.190.
- [iK_7, D_K]=0 at ALL tau. Jensen breaks SU(3)->U(1)_7 EXACTLY. PERMANENT.
- Schur on B2: Casimir=0.1557, irreducible, V(B2,B2) basis-independent to 5e-15. PERMANENT.
- Trap 1 confirmed: V(B1,B1)=0 exact (U(2) singlet). PERMANENT.
- mu=0 forced: PH canonical + Helmholtz grand canonical. Both routes CLOSED.
- M_max=1.445. BMF corridor: N_eff>5.5 required.
- Connes 15/16 discovered: finite-density spectral action EXISTS.

# Spectral Action + Tau Dynamics (S36)

- ANOM-KK-36 PASS: 150 anomaly coefficients = 0 exactly across 10 sectors, 5 tau values, levels 0-3.
- Structural theorem: pi_1(SU(3))=0 + complex conjugation pairing + adjoint reality.
- Level 3 dominance: 91.4% of S_full, 91.1% of gradient. (2,1)+(1,2) dominate.
- W6-SPECIES-36 PASS: Lambda_sp/M_KK = 2.06. N ~ 10^4.
- TAU-STAB-36 FAIL: S_full monotonically increasing. dS/dtau = +58,673 at fold. All sectors monotonic.
- TAU-DYN-36 FAIL: tau rolls through fold in 10^{-3} spectral time. Shortfall 38,600x.
- SC-HFB-36 FAIL: M_max(GCM,B2) = 0.646. BCS pocket < gradient.
- Mechanism chain: UNCONDITIONAL(S35) -> CONDITIONAL(S36) -> BROKEN for linear SA (S36 W4).
- Escape: Connes spectral action uses cutoff f(D^2/Lambda^2), NOT linear sum.

# Hessian + Collective (S40)

- HESS-40 FAIL: 22/22 transverse Hessian eigenvalues positive at fold. Min H=+1572, max H=+20233.
- Hessian hierarchy: diagonal u(2) hardest (~18-20k), complement medium (~14-15k), off-diagonal u(1)-complement softest (~1572).
- M-COLL-40: M_ATDHFB=1.695 (0.34x G_mod=5). B1 dominates 71% of cranking mass.
- T-ACOUSTIC-40: T_a/T_Gibbs = 0.993. T_acoustic/Delta_pair = 0.34.
- GSL-40: Structural v_min=0. All entropy terms non-decreasing.
- CC-TRANSIT-40: delta_Lambda/S_fold = 2.85e-6. Transit decoupled from CC by 5.5 orders.
- SELF-CONSIST-40: Transit ACCELERATES (1.72x). FRIED shortfall worsens to ~114,000x.

# Off-Jensen + Spectral Functional (S41)

- B2-OFFJ-41 PASS: BCS gap within 0.17% at eps=0.1. Topologically robust.
- SF-TRANSIT-41 FAIL: S_F^Connes = 0 (BDI T-symmetry). S_F^Pfaff monotonic.
- LOG-SIGNED-41 CONDITIONAL PASS: gap-edge weighted (Variant E) min at tau~0.15. Needs CSDR.
- M_KK ambiguity: Conv A (10^9 GeV) vs Conv C (10^13 GeV). Conv B EXCLUDED.
- N_eff step function: 32->240 at infinitesimal tau. NOT gradual.

# Fabric + DM (S42)

- Z-FABRIC-42 PASS: Z_spectral=74,731. Z/|dS/dtau|=1.27. c_fabric=c (Lorentz).
- HF-KK-42 FAIL: ALL 992 KK modes massive at fold. min=0.819, max=2.077 M_KK.
- TAU-DYN-REOPEN-42 FAIL: 35,393x shortfall survives. TV correction 2.6e-6.
- W-Z-42 FAIL: w_0=-1+O(10^{-29}). Framework = geometric Lambda-CDM.
- C-FABRIC-42 PASS: m_tau=2.062 M_KK. Stable gapped fabric at ALL tau.
- DM-PROFILE-42 PASS: NFW 1/r cusp. sigma/m=5.7e-51 cm^2/g.

# Josephson + Fabric (S56)

- FABRIC-FREE-ENERGY-56 FAIL: F_fabric monotonically increasing. dF_J/dtau=+1711 >> dF_BA/dtau=-131.
- INTEGRABILITY-56 FAIL: <r>=0.367 (Poisson). NPAIR3-ED-56 FAIL: <r>=0.414, decreases with N_pair.
- MU-SHIFT-56 PASS: mu_eff=-0.201 M_KK. PH broken. But 460x too small.
- E_J=7.042 +/- 0.497 M_KK. Superfluid at 14 sigma above SIT.
- All 32 KK modes dE/dtau<0 at fold. Universal downflow. PERMANENT.
- Josephson gap = KK Casimir eigenvalue DRESSED by BCS coherence factors.
- Three surviving channels: (1) anisotropic Josephson, (2) domain walls, (3) finite-rate inhomogeneous transit.
- Velocities: c_Gold(0.915) > c_BA(0.399) > c_eff(0.338) > c_Leggett(0.019-0.032).

# DDG + CSDR Branching (S63)

- DDG-POWER-LAW-63 INFO: SM 1-loop unification 51.7% at M_KK. KK tower NARROW (96.2% above M_KK, 2.7% log range).
- CSDR-BRANCHING-63 INFO: 28 sectors branched via Gelfand-Tsetlin weights.
- Cartan Trace Identity PROVEN: T_SU3=T_SU2=T_U1/12 for ALL (p,q). DDG non-differential. PERMANENT.
- adj(SU(3))=(0)_0+(1)_0+(1/2)_{+3}+(1/2)_{-3}. u(2):4 gauge, C^2:4 Higgs.
- Spinor Delta_8: (0)_{-3}+2x(1/2)_{-3/2}+2x(1)_0+2x(1/2)_{+3/2}+(0)_{+3}=16.
- A_eff=0.020 (below LOG-SIGNED-41 window [0.025,0.295]).
- Scripts: `s63_ddg_power_law.{py,npz,png}`, `s63_csdr_branching.{py,npz}`

# Library Gaps (S42 Meta-Analysis)

- Missing papers (all now added): DNP PhysRep, Appelquist-Chodos, Witten bubble, DDG, Forgacs-Manton, RSS.
- S41/S42 connections: LOG-SIGNED-41 needs CSDR (Forgacs-Manton); M_KK ambiguity needs DDG.
- Z/|dS/dtau|=1.27 is spectral analog of DeWitt metric, 15,000x larger.
- Effacement ratio 10^{-6} is STRUCTURAL bottleneck for w != -1.
