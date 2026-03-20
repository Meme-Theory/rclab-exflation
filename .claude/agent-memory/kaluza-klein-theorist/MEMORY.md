# KK Theorist Agent Memory

## Active Context

### Project Paths
- Main paper: `phonon_exflation_cosmology.md`
- KK papers: `researchers/Kaluza-Klein/` (12 papers). Index: `researchers/Kaluza-Klein/index.md`
- Tier 0 scripts: `tier0-computation/`. Tier 1 Dirac: `tier0-computation/tier1_dirac_spectrum.py`

### Baptista Conventions
- K=SU(3), dim 8, P=M4xK (12D). su(3)=u(2)+C^2
- Jensen: lambda_1=alpha*e^{2s} (u(1)), lambda_2=alpha*e^{-2s} (su(2)), lambda_3=alpha*e^s (C^2)
- Isometry: (SU(3)xSU(2)xU(1))/Z_6. Higgs from second fundamental form S (NOT gauge curvature F)
- R(s) = (3alpha/2)(2e^{2s}-1+8e^{-s}-e^{-4s}), eq 3.70
- V_eff = V + kappa*m^4*log(m^2/mu^2), eq 3.87. NORMALIZATION: R_K_Baptista = 6*R_K_ours

### Proven Structural Results
- NCG: KO-dim=6, SM QNs correct, A_F bimodule confirmed
- Dirac: lambda^2 = n/36 at s=0. Phi: (3,0)/(0,0)=1.531580 at s=0.15. IVT margin 0.38%.
- (3,0) UNIQUELY saturates Parthasarathy bound. Paasch series REFUTED.
- D_K Block-Diagonality Theorem (22b): C_nm=0 identically for ANY left-invariant metric on compact Lie group
- Spectral Action Monotonicity Theorem (28): Connection-independent, exact to 40+ digits. PERMANENT.

### Three Algebraic Traps (STRUCTURAL THEOREMS)
- Trap 1: F/B=16/44=4/11 (fiber DOF, tau-indep). Trap 2: b_1/b_2=4/9 (Dynkin, tau-indep).
- Trap 3: e/(ac)=1/16=1/dim(spinor) (trace factorization). ALL share tensor product root.

### Session 33 W3 R2: Einstein-Bergmann Modulus Equation (COMPLETED)
- V_eff = V_FR(tau) + eta*V_spec(tau). eta = f_4/(f_8*Lambda^4) is ONE free parameter.
- FR double-well at beta/alpha=0.28: barrier tau=0.1517, true min tau=0.4412.
- Domain walls exist for eta<0.12. Width 1.3-2.7 M_KK^{-1}.
- Dump point tau=0.19 is NOT V_eff min. BCS back-reaction REQUIRED.
- SWALLOWTAIL (A_4): At (0.28, 0.05), two derivatives vanish. Trapping unconditional for any Delta>0.
- Scripts: `s33w3_modulus_equation.py`, data: `s33w3_modulus_equation.npz`

### Session 29: BCS Mechanism
- KC-1 through KC-5: ALL PASS. Jensen saddle: 2/4 transverse eigenvalues negative (REDIRECT to off-Jensen).
- At eps_T2=0.049: sin^2(theta_W)=0.231 exactly. P-30w pre-registered.
- J_perp=1/3 (Schur). d_eff>=2. Multi-sector BCS mandated. One free parameter: M_KK.

### Session 32: Domain Wall + RPA
- RPA-32b PASS: chi=20.43, 38x margin. W-32b PASS: Van Hove at walls.
- Traps 4,5: Schur orthogonality + J-reality selection rules.
- Domain wall = spatially varying fiber metric = Einstein-Bergmann dilaton generalized to SU(3).

### Session 34: Corrections + Structural Consolidation
- TRAP-33b RETRACTED: A_antisym (frame V=0.287) != K_a_matrix (spinor V=0.057). Different vector spaces.
- J correction: C2 = gamma_1*gamma_3*gamma_5*gamma_7. No upstream chain impact.
- Van Hove at fold: rho_smooth=14.02/mode (2.6x over step 5.40). v_B2=0 at tau_fold=0.190.
- [iK_7, D_K]=0 at ALL tau. Jensen breaks SU(3)->U(1)_7 EXACTLY in Dirac spectrum. PERMANENT.
- Schur on B2: Casimir=0.1557, irreducible, V(B2,B2) basis-independent to 5e-15. PERMANENT.
- Trap 1 confirmed: V(B1,B1)=0 exact (U(2) singlet, all 8 generators). PERMANENT.
- mu=0 forced: PH canonical + Helmholtz grand canonical. Both routes CLOSED.
- M_max=1.445 (spinor V + smooth wall + imp 1.0). KK validated: `s35a_kk_validation.{py,npz}`
- BMF corridor: N_eff>5.5 required. N_eff=4 gives FAIL (35% suppression). DECISIVE OPEN.
- Connes 15/16 discovered: finite-density spectral action EXISTS, axiom-preserving.

### Session 36 Results (KK-authored + cross-session)
- ANOM-KK-36 PASS: 150 anomaly coefficients = 0 exactly across 10 sectors, 5 tau values, levels 0-3
- Structural theorem: pi_1(SU(3))=0 + complex conjugation pairing + adjoint reality
- Level 3 dominance: 91.4% of S_full, 91.1% of gradient. (2,1)+(1,2) sectors dominate
- W6-SPECIES-36 PASS: Lambda_sp/M_KK = 2.06 (d=4). Self-consistent counting N ~ 10^4
- TAU-STAB-36 FAIL: S_full(tau) monotonically increasing. dS/dtau = +58,673 at fold. ALL 10 sectors monotonic
- TAU-DYN-36 FAIL: tau rolls through fold in 10^{-3} spectral time. BCS needs tau_BCS = 40. Shortfall 38,600x
- SC-HFB-36 FAIL (unconstrained): M_max(GCM,B2) = 0.646. BCS pocket (-0.156) < gradient (+0.374)
- Mechanism chain: UNCONDITIONAL(S35) -> CONDITIONAL(S36 W2-B) -> BROKEN for linear SA (S36 W4)
- Escape route: CUTOFF-SA-37. Connes spectral action uses cutoff f(D^2/Lambda^2), NOT linear sum
- Sagan probability: 32%(S35) -> 28%(S36 pre-W4) -> ~12%(S36 post-W4)
- Collab file: `sessions/archive/session-36/session-36-kk-collab.md`

### Session 40 Results (KK-relevant)
- HESS-40 FAIL: 22/22 transverse Hessian eigenvalues positive at fold. Min H=+1572 (g_73, u(1)-complement). Max H=+20233 (diagonal su(2)). Condition number 12.87. 27th closure.
- Hessian hierarchy encodes Jensen algebra: diagonal u(2) hardest (H~18-20k), complement medium (H~14-15k), off-diagonal u(1)-complement softest (H~1572)
- M-COLL-40: M_ATDHFB=1.695 (0.34x G_mod=5). NOT 50-170x. Van Hove velocity zero + large gap. B1 dominates 71% of cranking mass.
- T-ACOUSTIC-40: T_a/T_Gibbs = 0.993 (acoustic metric, 0.7% agreement). T_acoustic/Delta_pair = 0.34 (nuclear backbending range)
- GSL-40: Structural v_min=0. All 3 entropy terms individually non-decreasing.
- CC-TRANSIT-40: delta_Lambda/S_fold = 2.85e-6. Transit decoupled from CC by 5.5 orders.
- SELF-CONSIST-40: Transit ACCELERATES (1.72x), M_coll < G_mod. FRIED shortfall worsens to ~114,000x.
- B2 weight corrected: 81.8% (not 93.0%). Prior gates unaffected.
- Collab file: `sessions/archive/session-40/session-40-kk-collab.md`

### Session 41 Results (KK-relevant)
- B2-OFFJ-41 PASS: BCS gap within 0.17% at eps=0.1. Topologically robust under transverse deformation
- SF-TRANSIT-41 FAIL: S_F^Connes = 0 identically (BDI T-symmetry). S_F^Pfaff monotonic
- LOG-SIGNED-41 CONDITIONAL PASS: gap-edge weighted (Variant E) has min at tau~0.15. Needs B/F assignment from CSDR
- M_KK ambiguity: Conv A (10^9 GeV) vs Conv C (10^13 GeV). Conv B EXCLUDED (sqrt(3) overcorrects)
- N_eff step function: 32->240 at infinitesimal tau. NOT gradual. Spectral refinement falsified

### Session 42 Results (KK-relevant)
- Z-FABRIC-42 PASS: Z_spectral=74,731. Z/|dS/dtau|=1.27. Fabric spatially rigid, c_fabric=c (Lorentz)
- HF-KK-42 FAIL: ALL 992 KK modes massive at fold. min=0.819, max=2.077 M_KK. ZERO massless modes
- TAU-DYN-REOPEN-42 FAIL: 35,393x shortfall survives. TV correction 2.6e-6 (c_fabric^3 suppression)
- W-Z-42 FAIL: w_0=-1+O(10^{-29}). Effacement 10^{-6} + expansion 10^{-22}. Framework = geometric Lambda-CDM
- C-FABRIC-42 PASS: m_tau=2.062 M_KK. Stable gapped fabric at ALL tau. CDM-like DM prediction
- DM-PROFILE-42 PASS: NFW 1/r cusp from collisionless GGE. sigma/m=5.7e-51 cm^2/g

### Pipeline Priorities (post-Session 42 meta-analysis)
1. CSDR branching rules for B/F assignment (resolves LOG-SIGNED-41 conditional pass)
2. DDG power-law running with full 992-mode tower (resolves M_KK ambiguity)
3. Casimir energy on SU(3) monotonicity check (alternative to spectral action stabilization)
4. Witten bubble of nothing on SU(3) with BDI spinors (vacuum stability)
5. Swampland dS conjecture applied to monotonic spectral action (adversarial test)

### Key Equations
- |omega_3|^2(tau) = (1/2)e^{-4tau} + 1/2 + (1/3)e^{6tau} (EXACT)
- FR critical ratio: beta/alpha = 0.313. Below -> true min at tau_0 > 0.
- beta/alpha from Baptista = 6*r_ours. Critical ratio 0.31292, agreement 0.03%.
- Modulus equation: G_tt*Box(tau) + dV_eff/dtau = 0, G_tt=5

## Reference Index
- `ncg_bridge_reference.md` — Sessions 6-11: A_F derivation, order-one, chirality resolution
- `closure_chain_reference.md` — Sessions 13-20b: V_eff closure chain (all perturbative closed)
- `session21b_cartan_flux.md` — Cartan 3-form, FR double-well, Weinberg angle chain
- `session21c_results.md` — T''(0)=7969, S_signed closure, algebraic traps, monopole structure
- `session28_synthesis_d.md` — Monotonicity theorem, modulus ODE, sector sharpening
- `session13b_phi_recheck.md` — Phi IVT, Parthasarathy, eigenvalue data table
- `baptista_analysis.md` — Baptista paper summaries and key equations
- `tier1_dirac_spectrum_results.md` — Dirac pipeline, conventions, phi search
- `tier0_branching_result.md` — Branching computation (End_U2 != A_F)
- `session_details_16_21.md` — Sessions 16-21 key details

## KK Paper Index (33 papers, updated 2026-03-14)
- CRITICAL: Kaluza(02), Klein(03), Einstein-Bergmann(04), DeWitt(05), Kerner(06), Witten-SM(09), Freund-Rubin(10), Witten-bubble(13), DNP-PhysRep(14), Forgacs-Manton(17)
- HIGH: Nahm(07), CJS(08), DNP-2025(11), Appelquist-Chodos(15), DDG(16), RSS(18), ADD(19), RS(20), GW(21), Manton(23), Cremmer-Scherk(29)
- MEDIUM: Nordstrom(01), Overduin-Wesson(12), Servant-Tait(22), Montero-Vafa(24), ACD(25), Anchordoqui(28), Batakis-Kehagias(30), Pope(31), CJR(32), Scherk-Schwarz(33)
- LOW: CMS/ATLAS(26), Low-reheating(27)
- Index file: `researchers/Kaluza-Klein/index.md` (33 papers, full dependency graph + equation concordance)

### Session 35 Workshop: kk x berry (Specificity Deepening) — 3 ROUNDS COMPLETE
- A_2 folds are GENERIC (codim-1) on any compact Lie group with 3-block or 2-block+nonvanishing bracket. PERMANENT.
- Fold absence on product spaces (SU(2)xSU(2)) is codim-infinity obstruction (convex composition). PERMANENT.
- Specificity is QUANTITATIVE not qualitative: three-tier hierarchy (UNIVERSAL/GROUP-SPECIFIC/SU(3)-ONLY).
- Sp(2) Jensen-type: blocks (1,3,6), deformation (3tau,-3tau,tau). Driving force 2x SU(3).
- Pre-registered: a_2(Sp2) in [1.5, 3.0] (kk) / [0.8, 2.5] (berry). Overlap [1.5, 2.5].
- G_2 (2-block) fold: UPGRADED from "unlikely" to "PREDICTED" by Wigner-von Neumann + brackets (R2 E-B4).
- Pre-registered: a_2(G_2) in [0.3, 1.5].
- Lichnerowicz at fold: R_ours=2.018, margin 29.3%. Fold uses only 14.6% of allowed depth. PERMANENT.
- SU(3) is SMALLEST simply-laced group with 3-block Jensen deformation. PERMANENT (proved by Dynkin exhaustion).
- Kill criterion revised: requires ALL of fold + DOS + SM gauge group + BCS. UNFALSIFIABLE by Sp(2)/G_2. PERMANENT.
- FOLD = AVOIDED CROSSING UNIFICATION (berry E-B6): fold IS lower branch of avoided crossing between h-type and m-type families. Connects Thom (A_2), Wigner-vN (avoided crossing), QGT (quantum metric). PERMANENT.
- Mather stability: a_2 bounded away from zero. Cusp (A_3) required to destroy fold, codim-2, non-generic in 1-param. PERMANENT.
- Quantum metric scaling: INTENSIVE (not dim^1 or dim^2). Controlled by gap delta_gap. PERMANENT.
- N >= 3 branches required for 2-block fold (berry E-B5). G_2 (128 branches) vastly exceeds this.
- Pure-math specificity tuple: T_math = (a_2, delta_gap, V, n_fold, kappa). Physics tuple: T_phys = (a_2, delta_gap, V, gauge_group).
- Sp(2) fold count uncertain: 1-3 depending on U(1) charge structure of coset Sym^2(fund_SU(2)) under U(2).
- Fold-Avoided Crossing Correspondence theorem proposed (G1, R3). Publishable in JGP/CMP.
- Workshop file: `sessions/archive/session-35/session-35-kk-berry-workshop.md`

## Debugging Notes
- center_dim=0 bug: complex structure constants + real null space. Fix: vectorize as [Re;Im]
- Ricci tensor sign: ALWAYS match contraction convention. R>0 for compact groups.
- ricci_tensor_ON argument order: ft FIRST, Gamma SECOND
- Lichnerowicz != R_endo + Ric_endo (rough Laplacian nonzero via Christoffel on constant tensors)
- Koiso-Besse: CONFORMAL only, not TT. Do not conflate.
- F/B ratio set by fiber DOF (geometric not dynamical). Constant-ratio trap.
- WRITE SIMPLE SCRIPTS in team sessions. Physics first, write-up second.
- kk1_bosonic_spectrum.npz stores mult=dim(p,q)^2 (WRONG). Code API returns dim(p,q) (CORRECT).
