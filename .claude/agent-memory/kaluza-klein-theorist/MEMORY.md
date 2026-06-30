# KK Theorist Agent Memory

## Project Paths
- Main paper: `phonon_exflation_cosmology.md`
- KK papers: `researchers/Kaluza-Klein/` (33 papers); index `researchers/Kaluza-Klein/index.md`
- Computation: `computations/`. Dirac spectrum: `computations/dirac_spectrum.py`

## Proven Structural Results (PERMANENT)
- NCG: KO-dim=6, SM QNs correct, A_F bimodule, AZ class BDI
- Dirac: lambda^2=n/36 at s=0. Phi: (3,0)/(0,0)=1.531580 at s=0.15. (3,0) UNIQUELY saturates Parthasarathy
- Spectral Action Monotonicity (S28): connection-independent, exact to 40+ digits. Single-particle SF cannot stabilize modulus on SU(3)
- D_K Block-Diagonality (S22b): C_nm=0 for ANY left-invariant metric on compact Lie group
- Cartan Trace Identity (S63): T_SU3=T_SU2=T_U1/12 for ALL (p,q). DDG non-differential on SU(3)
- Frobenius Kinetic Identity (S63): G_ab=Vol(K)*delta_ab in Frobenius basis. Universal Z
- [iK_7, D_K]=0 at ALL tau. Jensen breaks SU(3)->U(1)_7 EXACTLY (S34)
- Schur on B2: Casimir=0.1557, irreducible, V(B2,B2) basis-independent to 5e-15 (S34)
- Trap 1: V(B1,B1)=0 exact (U(2) singlet). All 32 KK modes dE/dtau<0 at fold (S56)
- Fold Universality (S35): A_2 folds GENERIC on compact Lie groups w/ 3-block or 2-block+nonvanishing bracket. SU(3) smallest simply-laced group with 3-block Jensen
- 12D Modulus ODE: 5*d^2(tau)/dt^2 + 15H*d(tau)/dt + V_total'(tau) = 0. G_tt=5
- Spinor Norm sqrt(16)=4 (S100a, Q27 RESOLVED): Delta_12=Delta_4(x)Delta_8, 64=4x16 Clifford mult; EH = a_2^M*a_0^K cross-term carries Tr(Delta_8)=16; graviton retains Delta_4 (4 of 64) => M_Pl,eff/M_Pl,unred=sqrt(16)=4 EXACT. Empirical 3.92 = PW-truncation-dressed 4 (rel=1/49; implied a_2 deficit 99/2500=3.96% ~ S59 measured 4.1% at max(p+q)=3). spinor_norm_factor_FW=4.0 canonical; grounds H0=65.4. Same 1/16 root as Trap 3
- Gauge-sourcing route (S96 W5-6, FAIL=isometry!=SM): TWO routes give DIFFERENT groups. (A) NCG inner-fluctuation = unimodular unitaries of A_K=C+H+M3(C): 1+3+8+1=13 raw (S61 13/13 PROVEN), 12 SM after unimodularity; SU(3)=colour(right M3), SU(2)_L on H (chiral LEFT). (B) KK-isometry = Killing stabilizer of g_tau: Isom(SU3,biinv)=(SU3_L x SU3_R)/Z3 dim16 at tau=0 -> Jensen tau>0 breaks SU3_R->U(2)_R, residual SU(3)_L x U(2)_R dim12. KK SU(2) is RIGHT (inside U2_R) != chiral SU(2)_L. DECISION: S61 used route A (NCG), matched NOT overturned. Chiral SM charges live in PROVEN Psi+=C16 Peter-Weyl branching (S7); KK-isometry supplies LEFT (p,q) LABELS, NOT the gauge group. Capstone "gauge from pure geometry" scoped to NCG route. session-31Aa line478 + session-19d line85 corroborate.

## Three-Coupling KK Running FAIL (INV6-W1-3, investigation track)
- Gate INV6-W1-3-KK-THRESHOLD-RUNNING: FAIL (audit_sha 6c2fb858...). First assembled 3-coupling KK-threshold running M_KK->m_Z. Corridor CLOSED.
- Cartan Trace Identity (T10) VERIFIED on L12 cache: T_eig(p,q)=T_eig(q,p) max rel 8.68e-16 over 42 conj pairs; Dynkin T_U1/T_SU2=12 (=5/3 GUT); Delta_sin2thetaW[C2]=0 EXACT carried (S84 W9-106). Leading machinery PERFECT.
- FAIL reason (STRUCTURAL, not precision): no-threshold skeleton from alpha_unif^-1=47.856 @ M_KK, lever ln(M_KK/m_Z)=34.33, SM (b1,b2,b3)=(41/10,-19/6,-7) gives sin2thetaW=0.6057 (obs 0.231, 162% off), a_em^-1=107.58 (16%), a_s=0.0116 (90%). Cartan threshold is COMMON to all 3 (Delta_3=Delta_2=Delta_1 by T10) => CANNOT differentiate. Best free common Delta over [-40,40] floors at max_rel=1.12 (112%), 0/3 within 2%. The (p,q) subleading differentiation too small to bridge.
- Two readings (both pre-reg FAIL_meaning): (a) M_KK->m_Z lacks SM intermediate-scale matter (cached tower = SU(3) fiber PW ladder, NOT SM spectrum); (b) alpha_unif^-1=47.856 is the SU(2) gauge coupling read off the fiber, NOT a GUT-scale unified value (canonical SM/MSSM unification ~24-25 @ 1e16). Cartan identity UNSCATHED; phenom bridge fails.
- m_H collapse: route band [127.5,131.8]->131.8+/-2.15 GeV single value (KK-threshold route, a4^zeta leg: lam_h(tree)=(4/3)g3^2(M_KK)*a4/a2=0.1703); +5.36% vs obs 125.1 (exact 67/1251), outside 2%. BCS -7% (S62) is the 134->125 route.
- Threshold sum Lambda-scheme-sensitive (Delta_common: -1.16 @ Lam=1, -14.4 @ 1.5, -43.7 @ 2.05 tower-top) and NOT L_max-saturated (L10 vs L12 63.8% shift) -- best-common-Delta gate observable robust to both.
- DIRECTION (verified): common negative Delta RAISES sin2thetaW AND RAISES a_s (a_s=1/a3^-1, Delta<0 => a3^-1 down => a_s up).

## S100b tau=0 Canonicity (workshop-adjudicated; machine-eps re-pin = CF-S101-TAU0-OPERATOR-CANONICITY)
- Framework tau=0 operator = LEVI-CIVITA member t=1/2 of Lai-Teh torsion family (W3-2 PERMANENT, 28/28 sectors 8.947e-15; alpha=-1/8 exact). Workshop verdict LC-CANONICAL under METRIC-COMPLETENESS + SA TORSION STATIONARITY (gravity+YM grades exact at ALL tau). t NOT a second empirical modulus — first bare-operator modulus closed by the SA (contrast S95 tau_fold FAIL: kinetic field vs frozen coupling)
- sigma-dial CONVENTION (do not re-import the category error): t is a tau=0-ONLY label. At tau>0 the invariant torsion space is a 3-dim polytope; cite sigma-lines with c(s)=(e^{-2s}, 1, 2e^{-2s}-e^{s}); t=(1-sigma)/2 at endpoint only; {sigma=0,1/3,1} -> {t=1/2 LC, 1/3 Kostant, 0 trivialization}
- Jensen line = D'Atri-Ziller naturally reductive w.r.t. SU(3)xU(2) at every s; realization FORCED unique at s!=0 (K-R2.4). Kostant line D_{T_tau/3} EXISTS, limits to t=1/3 exactly — the kill is SOURCING-ONLY (one datum sigma=1/3; H-flux role unfilled; torsion not in Omega^1_D)
- Jensen|S5-block = unique volume-compensated Tanno D-homothety of embedded Sasakian S5 (Reeb=transverse^2 <=> w1=2w3; su(2) scale = volume compensator). Structure-grade, no §VII slot by design
- a2(sigma;tau) even in sigma at ALL tau (trace parity); a4 sigma^1 == 0 at all tau (trace-parity + Bianchi + (3,0)-divergence kills); first open sigma-odd coeff = c1 at a6. Antidiagonal landmark s=(ln2)/3=0.2310 (su(2)^3 torsion zero, embed a2=1/2): INERT under LC; A-K8 bands FROZEN
- K4 PIN (mine, adopted verbatim): emergent-gravity dictionary on ANY torsion member = HEAT-KERNEL form a2^{zeta}(D_sigma^2); Einstein-Cartan split DIAGNOSTIC-only. Workshop: sessions/session-100b/workshops/tau0-operator-canonicity-workshop.md

## Three Algebraic Traps
- Trap 1: F/B=16/44=4/11 (fiber DOF, tau-indep). Trap 2: b_1/b_2=4/9 (Dynkin, tau-indep)
- Trap 3: e/(ac)=1/16=1/dim(spinor) (trace factorization). Common tensor product root.

## Baptista Conventions
- K=SU(3), dim 8, P=M4xK (12D). su(3)=u(2)+C^2. Isometry (SU(3)xSU(2)xU(1))/Z_6
- Jensen: lambda_1=alpha*e^{2s} (u(1)), lambda_2=alpha*e^{-2s} (su(2)), lambda_3=alpha*e^s (C^2)
- Higgs from second fundamental form S (NOT gauge curvature F)
- R(s) = (3alpha/2)(2e^{2s}-1+8e^{-s}-e^{-4s}), eq 3.70. R_K_Baptista = 6*R_K_ours
- V_eff = V + kappa*m^4*log(m^2/mu^2), eq 3.87

## Key Equations
- |omega_3|^2(tau) = (1/2)e^{-4tau} + 1/2 + (1/3)e^{6tau} (EXACT, verified <2e-13)
- FR critical ratio: beta/alpha = 0.313. Critical 0.31292, 0.03% agreement
- V_eff = V_FR(tau) + eta*V_spec(tau). eta = f_4/(f_8*Lambda^4), ONE free parameter
- Casimir ladder @ tau_fold (S100a W2-3): lam^2_min floors NOT C2-linear on (1,0)/(1,1)/(3,0) — chord-slope ratio 6.979 (bi-invariant tau=0: 1.0, W=9/5 exact by Peter-Weyl). |s(h)|^2 overlap diagonal SIGN-INVERTED (adjoint d_(1,1)=max > fund; W=-4.6635 FAIL vs bands {9/5,4/3,3.0}). C2 grading survives ONLY in whole-block traces (W_permode=1.7819, -1.0%) + scalar-Lambda channel (9/5 by constr.). Do NOT re-propose Dirac-floor/overlap-diagonal Casimir routes for the generation envelope.

## Current State Summary
- All 7 perturbative mechanisms CLOSED (S13-20b). NP physics required
- Mechanism chain UNCONDITIONAL(S35) -> BROKEN for linear SA (S36 W4)
- FRIED shortfall: 35,393x (S42), worsens to ~114,000x with self-consistency (S40)
- Three surviving channels: anisotropic Josephson, domain walls, finite-rate inhomogeneous transit
- Josephson gap = KK Casimir eigenvalue DRESSED by BCS coherence factors
- Framework = geometric Lambda-CDM: w_0=-1+O(10^{-29})

## Pipeline Priorities (post-S63)
1. ANISO-J-57: Mode-dependent J_kl from quasiparticle tunneling
2. DW-FABRIC-57: Modulus equation on 32-cell graph with per-cell tau_i(t)
3. CASIMIR-SU3-57: Zeta-regularized Casimir on Jensen-deformed SU(3)
4. ~~CSDR branching~~ COMPLETE (S63). ~~DDG power-law~~ CLOSED by Cartan Trace Identity

## KK Paper Index (33 papers)
- CRITICAL: Kaluza(02), Klein(03), Einstein-Bergmann(04), DeWitt(05), Kerner(06), Witten-SM(09), Freund-Rubin(10), Witten-bubble(13), DNP-PhysRep(14), Forgacs-Manton(17)
- HIGH: Nahm(07), CJS(08), DNP-2025(11), Appelquist-Chodos(15), DDG(16), RSS(18), ADD(19), RS(20), GW(21), Manton(23), Cremmer-Scherk(29)
- MEDIUM+LOW: Nordstrom(01), Overduin-Wesson(12), Servant-Tait(22), Montero-Vafa(24), ACD(25), CMS/ATLAS(26), Low-reheating(27), Anchordoqui(28), Batakis-Kehagias(30), Pope(31), CJR(32), Scherk-Schwarz(33)

## Debugging Notes
- center_dim=0 bug: complex structure constants + real null space. Fix: vectorize as [Re;Im]
- Ricci tensor sign: ALWAYS match contraction convention. R>0 for compact groups
- ricci_tensor_ON argument order: ft FIRST, Gamma SECOND
- Lichnerowicz != R_endo + Ric_endo (rough Laplacian nonzero via Christoffel on constant tensors)
- Koiso-Besse: CONFORMAL only, not TT. F/B ratio set by fiber DOF (geometric). Constant-ratio trap
- kk1_bosonic_spectrum.npz stores mult=dim(p,q)^2 (WRONG); code API returns dim(p,q) (CORRECT)
- A_F is the algebra; gauge group = U(A_F). End_{U(2)_LR}(Psi+) is NOT A_F (S6-11 branching)
- collect_spectrum() line 1328: eigvals(D) -> eigh(1j*D)
- WRITE SIMPLE SCRIPTS in team sessions. Physics first, write-up second
- gamma_E DOS fit at sparse fold (S93 W7-3): a 5-riser one-sided log-log slope measures NO band-edge exponent. Center scan (cache L12 tau019): all-points gamma_E swings -1.19..+0.59 over +-1*w_fit (chaotic, not biased); distinct-level gives OUT-OF-[0,1] (-1.25,+1.03); a TRUE n=2 sqrt-edge control is EQUALLY center-sensitive (0.50->-2.62). => center-sensitivity diagnoses ORIGIN PLACEMENT not van-Hove order; BOTH DOS estimators are fixed-tau artifacts. Clean channel = band dispersion E_B2(k;tau): read n from v_g~n*a*|k-k0|^{n-1}, no origin to misplace. S94 PRIMARY = SCALAR v_g^{B2}(tau) trajectory across >=7 tau (->0 at fold = vH; O(1)=KK), immune to sparseness AND origin chaos. E_B2 fold: 5 distinct levels in +-2wf, weighted mult {2,12,24,8,16}, pile-24 at offset -0.169*w_fit (NOT 0.318)

## Reference Files
- [early_sessions_reference.md](early_sessions_reference.md) — S6-21: NCG bridge, V_eff closure chain, phi recheck, Cartan flux, traps, branching detail
- [session_results_consolidated.md](session_results_consolidated.md) — S29-63: gate verdicts (modulus, BCS, spectral, fabric, DDG)
- [s35_fold_workshop.md](s35_fold_workshop.md) — Fold universality, avoided crossing, group classification
- [baptista_analysis.md](baptista_analysis.md) — Baptista paper summaries and key equations
- [dirac_spectrum_results.md](dirac_spectrum_results.md) — Dirac pipeline, conventions, eigenvalue table, phi search
- [chi_shriek_foreclosure.md](chi_shriek_foreclosure.md) — chi:A_K->M_2(C) is Wedderburn DELETION not Kasparov shriek of SU(3)->CP2 (§VII.CI; my Axis-B Stage-2 PASS)
- [modulus_kinetic_provenance.md](modulus_kinetic_provenance.md) — G_DeWitt=5 provenance map: GCR/W6-25 DERIVES it (w-indep by vol-preservation); S74/S41/S64/S96 CONSUME it; a4 correction (K_total~7.07) is the open piece (S116-W4/Q8)
