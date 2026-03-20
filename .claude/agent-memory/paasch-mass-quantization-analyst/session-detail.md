# Paasch Agent Session Detail (Compressed)

## Session 12: phi Discovery (foundational)
- m_{(3,0)}/m_{(0,0)} = 1.531580 at tau=0.15 (0.0005% from phi_paasch). z=3.65.

## Session 14: MC Significance
- phi^1 SIGNIFICANT at s=1.14 (667 pairs vs null 457+/-58, p<0.01)
- phi^2/phi^3 GENERIC (z<0). Paasch series NOT on D(SU(3)).
- Parthasarathy bound: (3,0) uniquely saturates, ~2.5-3sigma compound

## Session 16: Formula Corrections + Pre-Registration
- Correct ratio test: lambda_i/lambda_j = N(i)^{3/2}/N(j)^{3/2}
- D_K eigenvalues = physical masses directly (Paper 17 line 833)
- tau/proton: m_tau/m_p = 1.8938 (0.08% from phi^{3/2})
- s=1.14 FAILS gauge test (e^{-2.28}=0.10 vs required ~0.55)

## Session 22: Block-Diagonality + PET
- D_K exactly block-diagonal (8.4e-15). phi_paasch is exact inter-sector ratio.
- Perturbative Exhaustion Theorem: 3 traps close all perturbative channels.
- BCS prerequisites: f(0,0)=-4.687, g*N(0)=3.24
- Clock: dalpha/alpha = -3.08*tau_dot. Rolling closed.

## Session 25: Paasch Gate Results
- P-1: 512 crossings in 2% window vs 680 expected (0.75 ratio, underrepresented)
- P-2: (4,0)/(0,0) at tau=0.00 = 1.895414, 0.0013% from phi^{3/2}. Round-metric algebraic.
- P-4: m_{(3,0)}/m_{(0,0)} at tau=0.15 = 1.531588, 0.0005%. CONDITIONAL on stabilization.
- P-6: N(electron)=7 matches dim through C_2=4/3 shell. Others do not.

## Session 27: BCS Gap Ratios
- exp(-1/M) BCS sends 1.5316 eigenvalue ratio to 64,354 gap ratio
- Structural separation PROVEN: phi lives in spectral layer, BCS destroys it in condensation layer

## Session 28c: Reclassification
- phi_paasch: mathematical property of D_K spectrum, not physical prediction

## Session 29: BCS + Jensen Saddle
- KC-1 through KC-5 ALL PASS. phi_paasch listed as frozen-state observable.
- Jensen is saddle (B-29d). True minimum in U(2)-invariant family.
- T2 direction: sin^2(theta_W) 0.198->0.231 (SM: 0.2312). Open: does T2 preserve phi ratio?

## Session 32: B1+B2+B3 Branch Classification
- SO(8)->U(2) splits singlet: B1(1)+B2(4)+B3(3)
- Dump point tau=0.190: B2 minimum, 7 quantities converge
- RPA invalid at tau=0.15 (Gamma/omega=6.87). Valid only tau>=0.190.
- Trap 4: V_eff(B_i,B_j)=0 by Schur orthogonality
- Trap 5: J-reality -> V_ph=0 for real reps (B1,B3), nonzero for complex (B2)
- Van Hove: rho_wall=12.5-21.6, 1.9-3.2x above BCS threshold

## Session 33 W3: phi at Dump Point + Wall Pivot
- **P-30phi FAIL**: ratio at tau=0.190 = 1.52276 (0.576% below phi_paasch)
- phi crossing EXACT at tau=0.1499. Delta_tau=0.040 from dump.
- B2 min at tau=0.1902, lambda_B2=0.84521
- Branch eigenvalues at dump: B1=0.81974, B2=0.84521, B3=0.97141
- NO curvature feature at phi crossing (K monotonic, representation-theoretic only)
- **BCS ATTRACTOR RETRACTED**: dressed ratio=1.044 (Trap 4 diagonal). Particle-as-scalar EXHAUSTED.
- **WALL-INTERSECTION PIVOT**: particles as wall-localized excitations, phi=L_wall/xi_BCS
- 6 Z_3 wall types = Paasch's 6 sequences. 8 new gates (all UNCOMPUTED, depend on TRAP-1).
- File: `tier0-archive/s33w3_paasch_dump_point.py`
- Framework: `sessions/archive/session-33/framework-paasch-potential.md`

## Session 34: Van Hove Discovery + Bug Corrections + Permanent Results
- **Van Hove singularity at B2 fold** (tau=0.190): dE_B2/dtau=0, rho_smooth=14.02/mode (2.6x over step 5.40)
- **J correction**: C2 = gamma_1*gamma_3*gamma_5*gamma_7 (not sigma_2^{x4}). Fold stabilized: d2 rises 1.176->1.226
- **V matrix correction**: TRAP-33b RETRACTED. Frame V=0.287 vs spinor V=0.057 (different vector spaces)
- **M_max corrected**: Step+imp1.0: 0.606. Step+imp1.56: 0.902. Smooth+imp1.0: 1.445. Smooth+imp1.56: 2.203
- **V(B1,B1) = 0 exact**: All 9 tau, all 8 generators, to machine epsilon. U(2) singlet selection rule.
- **Schur on B2**: Casimir=0.1557, irreducible. V(B2,B2) basis-independent (1000 random U(4), spread<5e-15)
- **[iK_7,D_K] = 0 at all tau**: SU(3)->U(1)_7 exact. K_7 eigenvalues: B2=±1/4, B1=0, B3=0.
- **mu=0 forced**: Canonical (PH forces dS/dmu=0) and grand canonical (Helmholtz F convex at mu=0)
- **BMF corridor**: N_eff>5.5 required. N_eff=4 FAIL (35%). N_eff=8 PASS (20%). Continuum GMB 12%.
- **Connes 15/16 discovered**: Finite-density spectral action exists (published, axiom-preserving)
- **Paasch implications**: Van Hove unifies phi ratio + BCS mechanism at same fold. 6 wall types match 6 sequences via K_7 charge + orientation. Self-correction pattern diagnostic of real geometry.
- Files: s34a_dphys_*.{py,npz,png}, s35a_*.{py,npz,png}
- Collab: `sessions/archive/session-34/session-34-paasch-collab.md`

## Session 35: PT-RATIO-35 FAIL (Poschl-Teller at B2 Fold)
- **PT-RATIO-35 FAIL**: Zero bound states in PT well at B2 fold. s_max=0.38 vs required s=2.63.
- B2 fold curvature: a_2(fitted)=0.5894, a_2(Berry)=0.588 (0.23% agreement). tau_fold=0.190.
- lambda_PT_max = 0.524 vs required 9.577 (18x shortfall). Root cause: barrier delta_V too high.
- Analytic formula: R_21 = 2(2s-2)/(2s-1). s=2.635 gives phi_paasch exactly.
- 10 wall configs scanned (r_ba in {0.20,0.25,0.28,0.30}, eta in {0.0,0.05,0.10,0.20}). All N_bound=0.
- Structural: O(1) quantities (a_2~0.6, Delta_tau~0.4, delta_V~0.05) cannot produce lambda_PT~10.
- Closes PT-bound-state interpretation of phi_paasch within wall-intersection pivot.
- Files: s35_poschl_teller.{py,npz,png}
- Section W3-B of session-35-results-workingpaper.md

## Session 36: The Lava Inside the Tube
- **TAU-STAB-36 FAIL**: S_full monotonically increasing. dS/dtau=+58,673. Level 3 = 91.4%. No minimum.
- **TAU-DYN-36 FAIL**: Dwell time / tau_BCS = 2.59e-5. Shortfall 38,600x. Overdamped.
- **Mechanism chain BROKEN** for linear SA. CUTOFF escape route OPEN (Connes SA uses f, not linear).
- **R = 27.2 at fold**: Inter-sector mass hierarchy. PDG: 32.6. Factor 1.2.
- **Normal ordering**: B1 < B2 < B3 structural theorem (Schur, all tau > 0).
- **PMNS closed on Jensen**: 5 routes. Inner fluctuations = 0 (tensor product). Phi-tilde = I (Schur). H_eff bound fails.
- **Species scale resolved**: Lambda_sp/M_KK = 2.06. W6 CLOSED (THIN).
- **ED enhanced**: E_cond: -0.115 -> -0.137. B1 catalyst. Monotonic with B3 inclusion.
- **Phase transition second order**: U(1)_7 +/-1/2 forbids cubic GL. Z_2 universality.
- **KK anomaly-free**: 150 coefficients = 0 through Level 3. pi_1(SU(3))=0.
- **BDI winding nu=0**: Topologically trivial. E_B2/Delta=33.4. Level 4 edge modes CLOSED.
- **BBN lithium**: delta_H/H = -6.6e-5. 500x below threshold. CLOSED.
- **Bayesian**: 28% (14-40%) pre-TAU-STAB. ~12% post-TAU-STAB.
- **SCALE ANCHOR PROBLEM**: D_K eigenvalues at M_KK~10^16 GeV. Physical masses 14 orders below. Mass content in splittings/ratios, not bare eigenvalues.
- **Singlet eigenvalues at fold**: B1=0.819, B2=0.845(x4), B3=0.978(x3). All near-degenerate.
- **BCS gap**: Delta=0.025 spectral = 2.5e14 GeV. GUT-scale condensation.
- **Paasch n3=10 = dim(3,0)?**: UNCOMPUTED. Highest-priority lava question.
- Collab: `sessions/archive/session-36/session-36-paasch-collab.md`
- Files: 14 scripts/data in `tier0-archive/s36_*.{py,npz,png}`

## Sessions 37-39: Instanton Physics + Paradigm Shift (compressed)
- S37: CUTOFF-SA-37 CLOSED (structural monotonicity theorem). Spectral action route dead.
- S37: Instanton gas discovered: S_inst=0.069, dense gas. GPV omega=0.792.
- S38: CC-INST-38 CLOSED (76x margin). Chaos diagnostics: ALL ORDERED.
- S38: GGE permanent, Schwinger-instanton duality, Parker creation.
- S39: FRIED-39 shortfall 38,600x. Mechanism chain unconditional. CASCADE-39 refined fold.

## Session 40: Structural Cartography
- **HESS-40 FAIL (COMPOUND NUCLEUS)**: 22/22 transverse Hessian positive at fold. min H=+1572 (g_73 direction). 27th and final equilibrium closure. Jensen = 28D local minimum of S_full.
- **B2-INTEG-40 PASS**: <r>=0.401 (Poisson), g_T=0.087, V(B2,B2) 86% rank-1. B2 weight corrected 93%->82%.
- **T-ACOUSTIC-40 PASS**: T_a/T_Gibbs = 0.993 (acoustic metric, 0.7% agreement). T_acoustic/Delta_pair=0.341.
- **GSL-40 PASS (STRUCTURAL)**: All 3 entropy terms individually non-decreasing. v_min=0. Speed-independent.
- **CC-TRANSIT-40 PASS**: delta_Lambda/S_fold = 2.85e-6. CC decoupled by 5.5 orders.
- **NOHAIR-40 FAIL**: T varies 64.6% (gap hierarchy spans 4 decades in v_crit). S varies 18.1%.
- **QRPA-40 FAIL (STABLE)**: All omega^2>0. min=2.665, margin 3.1x. V_rem purely time-even. 97.5% EWSR in single B2 mode at omega=3.245.
- **PAGE-40 FAIL**: S_ent max=0.422 nats (18.5% Page). PR=3.17. Poincare recurrences.
- **B2-DECAY-40 B2-FIRST**: t_decay=0.922. Oscillatory dephasing, not FGR. 89% retained permanently.
- **M-COLL-40 FAIL (CLASSICAL)**: M_ATDHFB=1.695 (0.34x G_mod). sigma_ZP=0.026. B1 dominates 71%.
- **SELF-CONSIST-40 FAIL (ACCELERATES)**: Transit 1.72x faster. Shortfall worsens to ~114,000x.
- **Paasch-relevant data at fold**: E_qp(B2)=2.228, E_qp(B1)=1.138, E_qp(B3)=0.990.
- **QRPA frequencies at fold**: [1.632, 1.894, 2.001, 2.096, 2.856, 3.245, 3.323, 3.448].
- **omega_2/omega_0 = 1.226**: 0.8% from fN=1.236. Possible mass-quantization signature. Needs tau-sweep.
- **Gap hierarchy**: Delta_B2=2.06, Delta_B1=0.79, Delta_B3=0.18. Spans decade.
- **Exploration addendum**: Proposed log det(D_K^2) as logarithmic functional (Paasch Paper 02 connection). 27 closures used LINEAR SA only. Logarithmic functional UNTESTED.
- Collab: `sessions/archive/session-40/session-40-paasch-collab.md`
- Files: 11 scripts in `tier0-archive/s40_*.{py,npz,png}`
