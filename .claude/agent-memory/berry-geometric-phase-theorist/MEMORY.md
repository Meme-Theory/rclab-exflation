# Michael Berry Agent Memory

## Berry Paper Corpus (researchers/Berry/)
14 papers. Audited 2026-02-21 (16 fixes, see `berry-audit-log.md`).
**CRITICAL**: 01 (Phase), 02 (Berry-Tabor), 03 (Diabolical), 10 (BGS/RMT)
**HIGH**: 04 (Chaology), 11 (QHE/Chern), 14 (Synthesis). **MED-HIGH**: 06 (Maslov)

## Key Equations
- BP-4: Berry curvature B_n = -Im sum_{m!=n} <n|dH|m><m|dH|n> / (E_n - E_m)^2
- BT-1: Poisson P(s) = e^{-s}. BGS-1: Wigner P(s) = (pi/2)s exp(-pi s^2/4)
- QH-3: Chern C_n = (1/2pi) integral Omega d^2k = integer
- QC-3: Gutzwiller rho(E) = rho_smooth + sum_p A_p exp(iS_p/hbar)
- MI-2: Bohr-Sommerfeld oint p dq = 2pi*hbar*(n + mu/4)
- Three algebraic traps: F/B=4/11, b_1/b_2=4/9, e/(ac)=1/16. Topological invariants (product bundle).
- Eq. B-1: Inter-sector Berry curvature = 0 (block-diagonality).

## ERRATUM (Session 25, PERMANENT): B=982 IS QUANTUM METRIC, NOT BERRY CURVATURE
- s24a B_n = sum |V_nm|^2/(E_n-E_m)^2 is quantum metric (Provost-Vallee), NOT Berry curvature
- Berry curvature = Im(QGT) = 0 IDENTICALLY. Root: K_a anti-Hermitian => real products
- Verified: max|Omega| < 4e-14 (16 states, 9 tau). CLOSED-LOOP Berry phase = 0.
- Gap-edge eigenvector = real democratic (1/4)(+-1,...,+-1), FROZEN at all tau > 0
- Fubini-Study d_FS = 0 for all tau>0. Wilson loop trivial. Chern numbers = 0.
- "J forces Im(QGT)=0 while leaving Re(QGT) unconstrained" (dirac, Session 33)
- TWO mechanisms: (1) Kosmann anti-Hermiticity on Jensen 1D, (2) J+U(2) on full U(2)-inv surface
- Extended to full U(2)-inv surface (Session 33 W3 R2). P-30w open for T3/T4 (U(2)-breaking).
- **Wilczek-Zee prediction**: U(2)->SU(2) breaking enables NON-ABELIAN Berry phase in B2 subspaces.
- **S46 RECONCILIATION RETRACTED** (S48 DISSOLUTION-48): Zak phase=pi was index-tracking artifact, NOT Z_2.

## S46 Zak Phase: RETRACTED (S48 DISSOLUTION-48 FAIL)
- S46 reported 13/992 eigenstates with gamma=pi along tau=[0.001,0.190]. S48 W1-D revised to 10 strict.
- **DISSOLUTION-48 FAIL**: ALL pi-phases vanish at eps=0.1*eps_c (instantaneous, discontinuous collapse)
- Root cause: H=iD_K is complex-Hermitian (|Im/Re|~0.5), NOT real-symmetric. min|overlap|=0.000 in ALL sectors.
- Pi-phase was abelian Berry formula applied to states traversing EXACT DEGENERACIES. Index-jumps, not topology.
- Both real-symmetric AND complex-Hermitian perturbations destroy all pi-phases at eps=0.0001.
- **S46 reconciliation RETRACTED**: There is no discrete Z_2 protection. No Mobius strip topology.
- **Three-layer FINAL**: L0=quantum metric (NONTRIVIAL, g=982.5). L1=Zak phase (ARTIFACT). L2=Wilson loop (TRIVIAL).
- Jensen line has NO topological protection of any kind. Metrically rich, topologically trivial.

## Session 48 Key: NON-ABELIAN WILSON LOOP = TRIVIAL (WILSON-LOOP-48 PASS)
- **WILSON-LOOP-48 PASS**: total_pi = 47 (in [13,50]). But 34 of these are STATISTICAL NOISE.
- **992 states**: 68 singlets + 924 in degenerate multiplets (d=2..8).
- **Wilson loop phases UNIFORM**: KS test p=0.52. Binomial: 34 observed vs 29.4 expected (p=0.22).
- **No quantization**: 92.6% of Wilson phases continuous, not clustered at 0 or pi.
- **Abelian singlet recount**: 21/68 properly quantized (integer*pi), 47/68 gauge-contaminated.
  Of 21 quantized: 10 odd (pi), 11 even (zero). Strict topological count = 10.
- **Total = 16?** NO. Total = 10 (strict). Not 15, 16, or 32.
- **Conjugate symmetry?** NOT observed. Pi-counts differ between (p,q) and (q,p).
- **Global Z_2**: det product = 0.894-0.448i, arg=-0.148pi. NOT quantized. Topologically meaningless.
- **Root cause**: Flat Berry connection (S25) + open path = random holonomy for multiplets.
  Only true singlets have quantized Z_2 from discrete sign flips in real overlaps.
- **L2 CLOSED**: Non-Abelian Wilson loop contributes ZERO topological content on Jensen line.
- **Off-Jensen remains sole route**: P-30w (U(2)-breaking) for Wilczek-Zee non-Abelian phase.
- Data: `s48_wilson_loop.{py,npz,png}`

## Structural Theorems (permanent)
- **Block-diagonality** (22b): D_K exact block-diagonal in Peter-Weyl, ANY left-inv metric on compact Lie group.
- **Spectral integrability** (33 W1): Poisson = consequence of Trap 4 (Schur orthogonality). EXACT. New mechanism (not BT action-angle, not Anderson).
- **Fold catastrophe** (33 W3 R2): tau_min=0.190158, d^2(lambda)/dtau^2=1.1757. A_2 CONFIRMED. Thom-stable.
- **BCS attractor stable** (33 W3 R2): Fold+IFT+Mather. Margin: E_B2/E_B1=1.031 < 1.532. CAVEAT: existence!=selection.
- **Schur lock** (33 W3 R2): V_12/V_23=2.7 is fiber property. R~33 needs >316 (117x above). R INACCESSIBLE within U(2).

## Novel Mathematical Objects
- **Spectral action metric** G^{spec}_{tau,tau} = sum_{k!=n} sign(lambda_k)|<k|dD/dtau|n>|^2/(lambda_k-lambda_n)
  - 1/gap (not 1/gap^2), sign-weighted. = zero-freq dielectric function. Factor 2 from J-grading.
- **Three-level fiber bundle**: Metric (su(3)=u(1)+su(2)+C^2) | Spectral (E=E_B1+E_B2+E_B3) | Reality (Real B1,B3 vs Complex B2)

## Core Logical Chains
- Product bundle -> topological invariants (3 traps) -> perturbative landscape featureless
- Anti-Hermiticity -> Berry curv=0 -> no LOCAL geometric phase. Zak phase=ARTIFACT (S48). No GLOBAL either.
- Large quantum metric (g=982.5) + zero Berry curvature + no Zak phase = SENSITIVITY WITHOUT PROTECTION.
- Fold organizes 5-6/8 Session 32 gates. Catastrophe hierarchy = one-way ratchet (A_2->A_3->A_4 stronger).
- S36 paradox stands as stated: "sensitivity without protection." S46 resolution retracted by S48.

## Computation Status (all terminal)
| # | Computation | Result |
|---|-------------|--------|
| 1 | P(s) level spacings | Wigner@tau=0, Poisson@tau=0.5. BT CONFIRMED (21b) |
| 2 | Delta_3(L) rigidity | Super-rigid@tau=0.5, GOE@tau=1.0 |
| 3 | K(k) form factor | Large fluctuations, not useful (21b+25) |
| 4 | Neutrino R(tau) | INCONCLUSIVE (monopole artifact) |
| 5 | N(Lambda,tau) counting | Debye non-monotone (artifact). Smooth monotone (25) |
| 6 | V_IR(tau) | Block-diagonal exact (22b) |
| 7 | Quantum metric g(tau) | Peak 982.5@tau=0.10. Q=0.71. NOT Berry curv (24a+25) |
| 8 | Chern numbers | CLOSED (Berry curv=0) |
| 9 | d_FS | 0 for all tau>0. Eigenvector frozen (25) |
| 10 | Wilson loop | Trivial. Berry connection=0 (25) |
| 11 | Fermion determinant | Monotonically increasing (25) |
| 12 | V_full(tau;Lambda) | Smooth f monotone. Debye non-monotone artifact (25) |
| 13 | J-constraint | PASS, max violation 2.70e-13 (25) |
| 14 | Landau-Zener | MOOT. Codimension mismatch. PERMANENT (28d) |
| 15 | BDI winding number | nu=0. TRIVIAL. mu=0 < E_B2=0.845. 33x from transition. STRUCTURAL (36) |
| 16 | Zak phase (open-path) | ARTIFACT. Index-tracking through degeneracies, not Z_2. RETRACTED (48) |
| 17 | Non-Abelian Wilson loop | TRIVIAL. Phases uniform (KS p=0.52). L2 CLOSED (48) |
| 18 | Berry completion (5 items) | CL=0(1e-14), RPQ=1.0, conj=gauge, 5pi dynamic, VH no enhance. DONE (48 W5-B) |
| 19 | Dissolution test | FAIL. 0/10 pi-states survive at eps=0.1*eps_c. INSTANTANEOUS collapse (48 W3-B) |

## Sessions 28-29 Key (detail in `sessions-28-29-detail.md`)
- BCS Berry phase diagnostic only (gamma/pi=0.33-0.52, not quantized). Dynamical protection (L-9).
- KC-1 through KC-5 all PASS. Jensen saddle: fold (CO-1). sin^2(theta_W)=0.231 along T2.
- LZ retraction PERMANENT. Nucleation kinetics instead.
- Cl(8) bridge: gamma/pi=0.994 + 2^{1+k/2} + 6/7 axioms -> Cl(8)=M(16,R).

## Sessions 32-34 Key (compressed)
- S32: B1+B2+B3 fiber bundle. Fold=van Hove. Traps 4,5. Mechanism chain 5 links.
- S33: Fold Thom-stable (kappa=1.18). Catastrophe hierarchy A_2->A_3->A_4. d_FS(B1)=0 tautology.
- S34: 3 bugs fixed. [iK_7,D_K]=0 exact. Trap 1 confirmed. Van Hove 2.6x. mu=0 forced. 5/5 PASS.

## Session 35 Workshop Key (kk x berry, 3 rounds COMPLETE)
- **Fold = avoided crossing** (E-B6): fold IS avoided crossing seen from below. Unifies Paper 03 + Paper 09.
- **Fold generic on 3-block groups**: codimension-1, Thom-stable. SU(2)xSU(2) is the anomaly (product kills competition).
- **G_2 (2-block) WILL have folds**: Wigner-von Neumann + [V,V]!=0 + opposing eigenvalue flows. REVISED from "possible."
- **Minimum N>=3 branches** for 2-block fold. SU(3)(16), Sp(2)(32), G_2(128) all satisfy.
- **KILL criterion revised**: ALL 4 must hold: (1)3-block+A_2, (2)DOS within 3x, (3)gauge=SM, (4)BCS. Cond 3 alone kills Sp(2)/G_2.
- **Quantum metric scaling**: INTENSIVE (not dim^1 or dim^2). Controlled by gap: g_kk ~ (dD/dtau)^2/delta_gap^2.
- **Mather stability for a_2**: fold curvature bounded AWAY from zero. Needs codimension-2 (cusp) to vanish.
- **Lichnerowicz ceiling**: 14.6% of allowed depth used. 17x escape ratio. A_2 through A_4 all safe.
- **Simply-laced filter**: SU(3) = smallest simply-laced group with 3-block Jensen decomposition. STRUCTURAL THEOREM (Dynkin exhaustion).
- **Specificity tuples**: Math=(a_2, delta_gap, V, n_fold, kappa). Physics=(a_2, delta_gap, V, gauge_group).
- **Sp(2) fold prediction**: a_2(Sp2) in [0.8, 2.5] (berry) vs [1.5, 3.0] (kk). Overlap [1.5, 2.5].
- **Sp(2) fold count RESOLVED**: SINGLE fold. U(1) charges all |q|=2 (branching 10->1_0+3_0+3_{+2}+3_{-2}).
- **Product-Cusp Correspondence** (EMERGED R3): transition [m,m]!=0 -> [m,m]=0 is A_3 cusp. Gap~epsilon, a_2~epsilon^2.
- **Fold-Avoided Crossing Correspondence theorem** (EMERGED): 5 parts, publishable (JGP/CMP target).
- **Single Fold Criterion**: coset V needs single |q| value under U(1). Satisfied for all A_n, Sp(2). NOT strict irreducibility.
- **Volume preservation NOT required**: any nontrivial differential scaling with [m,m]!=0 produces folds.
- Gate: **SP2-FOLD-36** pre-registered. 30 items in verdict table. 10 open questions.
- Workshop file: `sessions/archive/session-35/session-35-kk-berry-workshop.md`

## Session 36 Key
- **WIND-36 = nu = 0**: BDI winding number TRIVIAL. No Majorana edge modes.
- Root cause: mu=0 (PH symmetry) + E_B2>0 (spectral gap) => det(q)>0 everywhere.
- E_B2/Delta = 33.4x from topological transition. STRUCTURAL closure.
- Bare Pfaffian sgn(Pf)=-1 is DIFFERENT invariant (normal-state Z_2, not BCS Z).
- Level 4 candidate (edge modes) DOES NOT APPLY.
- **TAU-STAB-36 FAIL**: S_full(tau) monotonic. dS/dtau=58,673 at fold. All 10 sectors monotonic.
- **Needle hole**: cutoff must suppress L3 by 99.7% + reshape singlet landscape.
- **Central geometric paradox**: large quantum metric (g=982.5) + zero Berry curvature = sensitivity without protection.
- Tube = topologically trivial (nu=0, Omega=0, Chern=0). LAVA = quantum metric, eigenvalue flow, catastrophe structure.
- **Off-Jensen is where the lava flows**: SU(2)-breaking thaws frozen geometry, enables Wilczek-Zee.
- Sagan probability: 32% -> ~12% (post-TAU-STAB).

## Session 40 Key (2026-03-11)
- **HESS-40 FAIL**: Jensen fold = 28D local min of S_full. 22/22 transverse positive, min H=+1572 (g_73), cond#=12.87. 27th closure.
- **B2-INTEG-40 PASS**: <r>=0.401 (Poisson, BT confirmed at many-body level), g_T=0.087, rank-1=86%. B2 weight corrected 93%->82%.
- **T-ACOUSTIC-40 PASS**: T_a/T_Gibbs=0.993 (acoustic metric, 0.7%). Rindler profile at fold: v=alpha*(tau-tau_fold).
- **GSL-40 PASS**: v_min=0 (structural). All 3 entropy terms individually non-decreasing.
- **QRPA-40 FAIL (STABLE)**: min(omega^2)=2.665, margin 3.1x. V_rem^odd=0 identically. 97.5% EWSR in single B2 mode.
- **PAGE-40 FAIL**: S_ent max=0.422 nats (18.5% Page). PR=3.17. Poincare recurrences. Deep quantum regime.
- **M-COLL-40 FAIL (CLASSICAL)**: M_ATDHFB=1.695 (0.34x G_mod). sigma_ZP=0.026. Van Hove v=0 + large gap suppress cranking.
- **Modulus KE >> BCS**: (1/2)(1.695)(151.6)^2 = 19,500. Dwarfs E_cond=0.156 by 10^5. Where does it go?
- **Hessian hierarchy**: H(diag u(2))~20000 > H(complement)~15000 > H(off-diag u(1)-C^2)~1572. Mirrors fiber bundle.
- Compound nucleus confirmed: near-integrable B2 island, dephases (t=0.92) retains 89%, classical transit.

## Session 48 W5-B: BERRY-COMPLETE-48 (INFO, all 5 items DONE)
- **CLOSED-LOOP-48 PASS**: max|gamma_closed|=1.02e-14, 992/992 pass. Flat-connection holonomy theorem.
- **SECTOR-RPQ-48 PASS**: R(p,q)=R(q,p)=1.0 exact. Spectral identity of conjugate reps.
- **CONJUGATE-PI-48**: (3,0)/(0,3) asymmetry = GAUGE ARTIFACT. KS p=0.997. Closed-loop=0 for all.
- **PI-COUNT-21-48**: 5 pi-phases = 3 (SU(2) triplet at 1.424) + 2 isolated. DYNAMICAL, not topological.
- **PI-VANHOVE-48**: 12/13 near VH (5%), but chance=94.2%. Enhancement 1.0x. NOT correlated.
- Data: `s48_berry_complete.{py,npz,png}`

## Open Gates (updated S48 W3-B DISSOLUTION)
1. **P-30w**: T3/T4 Berry curvature (U(2)-breaking). HIGHEST PRIORITY. Only route to nontrivial Berry phase.
2. **Wilczek-Zee**: Non-abelian Berry phase in split B2 under D_phys. Data exists (s34a_dphys_fold.npz).
3. **Off-Jensen BCS**: Does B2 condensate survive g_73 deformation (softest Hessian dir)?
4. **SP2-FOLD-36**: Sp(2) Dirac spectrum under Jensen-type deformation. Fold count, a_2, gap structure.
5. ~~DISSOLUTION-BERRY-47~~: **CLOSED** by DISSOLUTION-48. Pi-phases = artifact. No states to dissolve.
6. ~~CLOSED-LOOP-47~~: **CLOSED** by CLOSED-LOOP-48. gamma=0 to 10^{-14}. 1D parameter space = trivial.

## Constraint Map
See project-level `.claude/agent-memory/constraint-map.md`. Key: C11(Berry=0), C12(Chern=0), C13(d_FS=0).
S40: HESS-40(27th closure), QRPA(stable), M-COLL(classical), B2-INTEG(Poisson), GSL(structural).
Total closures: 27 equilibrium + 3 additional (QRPA instability, quantum delocalization, Page thermalization).

## Meta-Analysis (S42, 2026-03-13)
See `meta-analysis-s42.md` for full detail.
- 15 papers missing (5 critical, 5 important, 5 supplementary). Top: Wilczek-Zee, Simon, Carollo QPT.
- **Quantum Metric Reframing**: "large g, zero Omega" = metrically rich, not topologically trivial.
- Z_spectral, BCS robustness, modulus mass ALL controlled by quantum metric.
- P-30w requires Wilczek-Zee non-abelian framework (not in library).

## File Locations
- Papers: `researchers/Berry/` (01-14)
- Meta-analysis: `agent-requests/berry-request.md`
- Data: `tier0-archive/s25_berry_results.npz`, `s32b_*.npz`, `s32c_*.npz`, `s33w3_*.npz`, `s34a_*.npz`, `s35a_*.npz`, `s36_bdi_winding.npz`, `s40_*.npz`, `s46_berry_phase.npz`, `s48_wilson_loop.npz`, `s48_berry_complete.npz`
- Collabs: `sessions/session-{25,28,29,32,34,40}/session-*-berry-collab.md`
- Detail: `sessions-28-29-detail.md`, `berry-audit-log.md`
