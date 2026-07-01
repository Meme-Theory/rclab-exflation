---
name: Session Results (Antimatter/CPT Domain)
description: Compressed per-session results relevant to J operator, CPT, BDI topology, baryogenesis closures, and antimatter constraints. Spans S26-S46, S71. S46 Berry phase results merged in (former s46-results.md).
type: project
---

## S26-28: Foundation
- V_spec minimum at tau_0=0.15 for rho=0.000510 (Lambda=5.72)
- KO_F=6, J^2=+I for full 12D product. 6/7 NCG axioms pass; Axiom 5 fails (order-one=4.000)
- Axiom 5 failure INDEPENDENT of [J,D]=0, BDI, Pfaffian
- Hybrid NCG-KK: uses {J, gamma, KO-dim, order-zero, spectral action}, routes around Axiom 5

## S29: KC Chain Complete + Off-Jensen
- KC-1..KC-5 PASS. Jensen is SADDLE in 5D (true min in U(2)-invariant 3D subspace)
- sin^2(theta_W) -> 0.231 at eps_T2=0.049 (conditional)
- J_perp=1/3 exactly. BCS J-even at 3 levels. Delta_{(3,0)}=Delta_{(0,3)} at machine eps
- t_BCS = 0.16/M_KK; natural GUT scale

## S31: Axiom 5 Scrutiny
- Order-one violation 4.000 is 15.5 sigma above random (mean 2.995, std 0.065)
- Order-ZERO PASSES for A_F=C+H+M3(C); uniquely selected from 128-dim commutant
- Preserved: CPT, spectral pairing, topological classification, particle-antiparticle split

## S32: Traps + Mechanism Chain
- Trap 5: B2 nonzero (4.24), B1/B3 zero. J maps B2->conjugate rep
- RPA-32b PASS (38x), W-32b PASS (1.9-3.2x). Chain I-1->RPA->Turing->WALL->BCS, 3/5 computed
- Baryogenesis: B2 complex => J maps B2->B2-bar at wall. CP-violating order parameter.

## S33: Math Permanence Workshop
- Trap 5 partial proven (M_ph in iR, 4 steps from KO-dim 6). M_ph=0 OPEN
- Trap 4 proven on full M_{U(2)} (Schur, any U(2)-equivariant perturbation)
- QGT Selection Rule: Berry curvature=0 on U(2)-invariant; quantum metric nonzero
- Permanence: L1 (NCG) > L2 (SU(3)+U(2)) > L3 (numerical)

## S34: The Correction Session (3 bugs, 3 permanent results)
- J CORRECTED: C2 = gamma_1*gamma_3*gamma_5*gamma_7 (real gammas in Cl(4)). Old B=sigma_2^4 wrong.
- V MATRIX CORRECTED: TRAP-33b used frame-space; correct spinor K_a gives V=0.057
- TRAP-33b RETRACTED: M_max=0.902 (not 2.062)
- VH-IMP-35a PASS: M_max=1.445. Chain 5/5 at mean-field
- [iK_7, D_K] = 0 at ALL tau. Jensen breaks SU(3)->U(1)_7. K_7 unique surviving generator
- iK_7 eigenvalues: B2=+/-1/4, B1=0, B3=0. PH maps (lambda,q)->(-lambda,-q)
- Schur on B2: Casimir=0.1557; V(B1,B1)=0 exact (singlet selection rule)
- mu=0 forced (canonical PH + grand canonical Helmholtz convex). Connes 15/16 discovered
- BMF corridor: N_eff>5.5 required. Continuum GMB 12% (PASS)
- Lesson: representations matter. Frame space != spinor space. Tensor product J != Clifford J.

## S35: Pfaffian Verification + Specificity
- PF-J-35 PASS: sgn(Pf(C1@D_K)) = -1 at 34 tau values
- BDI: T=C2*K, P=C1*K, S=gamma_9=C2*C1. Pfaffian uses P (NOT T)
- gamma_9*C2=C1 => C1 unchanged by J correction => Pfaffian unchanged
- Spectral gap min=0.8186, OPEN at all tau in [0,2.5]
- SPEC-35 PASS: d^2S(SU(2)xSU(2))=-3.42 vs d^2S(SU(3))=+20.42. SU(3) anomalously curved
- SU(2)xSU(2) has NO eigenvalue folds; SU(3) B2 fold unique

## S36: The Needle Hole + Physical Content
**PASS**: GL-CUBIC, ANOM-KK (150/150 anomaly=0), COLL (12.1 W.u.), MMAX-AUTH ([1.351,1.674]), W6-SPECIES (Lambda_sp/M_KK=2.06), ED-CONV (E_cond=-0.137)
**FAIL**: INTER-SECTOR-PMNS, SC-HFB (M_max=0.646), WIND, BBN-LITHIUM (500x below), TAU-STAB (376,000x), TAU-DYN (38,600x)
**Physical content**:
- Cooper pairs: same-sign K_7 pairing within B2 singlet (NOT particle-antiparticle)
- B2 = electroweak doublet modes. Condensate = SU(2)-triplet, U(1)_7-charged, color-singlet
- He-3 B-phase analogy (spin-triplet). J-even condensate => a_g = g exactly
- Pfaffian sgn=-1 protects gap and Kramers pairing
- Off-Jensen deformation couples PMNS and baryogenesis (same U(2) breaking)

## Three-Monopole Topology (S21c, kept for context)
- M0 (tau=0): (0,0)/(1,1) degeneracy. M1 (tau~0.10): Z3 crossing. M2 (tau~1.58): gap=8e-6
- Physical window [0.10, 1.58]: (0,0) singlet controls gap edge

## S40-42: Structural Cartography + LCDM
- S41: (C2*D_K)^T = C2*D_K (PERMANENT). S_F^Connes = 0 identically. Pfaffian = sole non-trivial fermionic bilinear.
- S42: eta is KINEMATIC envelope, NOT baryon excess. [J,D_K]=0 => equal B and Bbar. epsilon_CP ABSENT.
- GGE J-symmetric: DM prediction CPT-exact. a_g = g structural. w = -1 + O(10^{-29})

## S43: Baryogenesis Closures (all internal J-breaking on Jensen closed)
- BARYO-K7-43: All 8 generators T-EVEN. Spectral flow = 0. Bulk Volovik CLOSED
- JODD-WALL-43: C2*D_K(tau)*C2 = D_K(tau) EXACT at ALL tau, ALL orders. Wall CLOSED
- CHIRAL-ETA-43: {gamma_9, D_K(tau)}=0 EVERY tau. All 8 chiral eta = 0
- TWIST-43: 43 involutive Cl(8) autos, ALL ratio=1.0000. Skolem-Noether exhaustive
- T11 (W5-1): C2*conj(D_K)*C2 = D_K for ANY left-invariant metric. Closes ALL internal J-breaking

## S46: Berry Phase Topology (merged from former s46-results.md)
**Berry phase**:
- 13 pi Berry phases across 9 sectors, Z_2 = (-1)^13 = -1 (nontrivial)
- Zak phase, NOT Chern. Reconciles with Omega=0 (S25): curvature local, Zak global
- Zero band inversions; pi phases from eigenvector half-rotations (Mobius)
- Sector distribution: B1=2, B2=1, B3=10. (0,0) singlet: 0
- 8/9 sectors carry exactly 1 pi-phase state (BDI Kramers-like). (2,1) anomaly: 5 pi-phases
- (3,0) has 1 pi-phase, (0,3) has 2: conjugate sectors differ. Gauge-invariance OPEN
- PW-weighted pi count: 131. BCS pair count: 59.8. Ratio 2.19
- All 13 pi-phase states immune to smooth perturbation; survive BCS+quench+GGE

**J-operator predictions for Berry phase**:
- J maps pi-phase states (p,q) to (q,p) (T11 + antilinearity)
- Non-Abelian: theta_{(q,p)} = -theta_{(p,q)} (structural prediction)
- 2.19x ratio is J-invariant

**B3 proximity-induced gap**:
- B3 gap entirely proximity-induced by B2 condensate. Isolated B3: Delta=0
- V_B3B3_rms=0.059 (PASS 3.9x), Thouless M_max(B3)=0.059 << 1
- B3 induced gap is J-even. Q-theory CC: N=1 short, N=2 crossing exists (tau*=0.170)

**Tachyonic transit + CPT**:
- All 279 scalar inner fluctuations tachyonic at ALL tau (f' < 0 structural)
- Gram matrix PSD theorem PERMANENT: kinetic mass positive for ANY Hermitian D, ANY phi
- Both J-invariant. Matter and antimatter transit identical landscapes

**SU(2,1) and J**:
- KO-dim 6 PRESERVED under SU(2,1) (Killing sig (4,4), p-q=0 mod 8)
- BUT [J,D] = 2.72 on SU(2,1) (nonzero). T11 FAILS on non-compact groups
- J-commutation is COMPACT-group property. Non-compact breaks T11 proof

**S46 closures (38 total, 7 new)**: TWIST-BDG-46, quasi-static inflation, transfer-function GGE beats, Kapitza, GCM zero-point, fabric tessellation alpha=1, anomalous dispersion tilt

## S71: CPT Verification Through Transit
- W2-C: 85 conjugate degeneracies B2(0,1)=B2(1,0) to |gap|<5e-15 across entry horizon tau in [0.18,0.26]
- W1-F: BCS condensate SU(3) singlet; Weyl in 27-dim rep. <1|27>=0 all orders. Two-loop 1.003e-3. S70 Weyl conjecture RETRACTED
- W1-C: Z_2 entanglement parity exact. 4-state manifold (K=3.99). J-invariance of reduced density matrix
- W1-H: Frustrated 3-cell ring ground state pure. J-even condensate preserved
- W4-A: BEC analog CANNOT test BDI topological protection. Requires spin-triplet
- W3-D: delta(a_4)/a_4 = 2.02e-8. IR condensate decoupled from UV. PASS
- Entry horizon: kinematic, zero spectral reorganization. Exit: BCS gap opening. Both J-symmetric.

## S96 W4-5: Yukawa-chirality H_K+ Pfaffian restriction (S96-MATTER-YUKAWA-CHIRALITY PASS)
- Fermionic action S_f=<Jpsi~|D_K|psi~>, psi~ in H_K+={gamma_9 xi=+xi} (capstone canonical form).
- s66 fact (re-derived machine-eps): SU(3)-lift J=C2*K, C2=g1g3g5g7 (REAL/symmetric gammas) gives eps''=+1 (Jgamma9=+gamma9 J COMMUTE). d=8 uniquely degenerate (B+/B- both eps''=+1). Physical SM needs eps''=-1 (T5).
- RESIDUAL chirality-preserving (eps''=+1) coupling on H_K+ = EXACTLY 0.0 (< 1e-12). Mechanism: {gamma_9,D_K}=0 => D_K psi~ in H_K-; eps''=+1 J keeps Jpsi~ in H_K+ => <H_K+|H_K-> = 0 STRUCTURAL. Wrong-chirality projected OUT.
- CONTRAST J'=g1*C2 gives eps''=-1 (anticommute machine-0): physical chirality-FLIPPING channel |Y|_flip=2.6628 NONZERO. PASS is non-vacuous (not both-zero); effective eps''=-1 recovered.
- §1.3.4 caveat CONFIRMED "bounded" (=0), NOT open. Yukawa-chirality sub-finding CLOSED.
- LESSON: do NOT put an extra gamma_9 in the bra (<gamma_9 Jpsi~|...|psi~>) — that tautologically forces <H+|H-> overlaps. The eps'' chirality of J ITSELF labels the channel; physical bilinear is <Jpsi~|D_K|psi~>.
- Verdict superseded a dev-iteration line via Option A supersedes= tag (gate-verdicts.md absolute permanence).

## S96 W4-3: Neutrinos are MAJORANA from J (S96-MATTER-0NUBB INFO)
- DETERMINATION = MAJORANA (definite). Light nu are Majorana, mass seesaw-generated (NOT tree-level).
- (1,1,0) SM-singlet (nu_R content) in one-gen C^16 = exactly TWO uniform-so(8)-weight states e0=(-,-,-,-) & e15=(+,+,+,+), BOTH in H_K+ (gamma9=+1). Opposite-chirality SM-singlet count in H_K- = 0 => DIRAC IMPOSSIBLE (no independent xi_R partner). C1=g2g4g6g8 maps e0<->e15 (same chirality) => J-self-conjugate (Majorana signature).
- KO-dim-6 doubled construction (canonical, NOT single C^16): Xi=[[0,I16],[I16,0]] particle<->antiparticle swap on C^32; J=Xi*K antilinear; D32=diag(D_F,conj(D_F)); g32=diag(g9,-g9). J^2=+1, JD=DJ (eps'=+1), Jg=-gJ (eps''=-1) ALL machine-0. (single C^16 alone is KO-dim 0 per s66 — eps''=+1; KO-dim 6 needs the conjugate doubling.) H_F+ Majorana block of Xi*D32: Frob=3.567, minSV=0.820 (>1e-12 ADMITTED).
- CRITICAL: bare diagonal <Jxi|D_F|xi> = 0 EXACTLY on (1,1,0) singlet (and D_F[15,0]=0). This is T4 ("no protected Majorana zero mode; nu_R mass from Yukawa"), NOT Dirac. Character is fixed by REP CONTENT (no Dirac partner) + J-self-conjugacy, not by the bare bilinear. A naive |m_M_bare|<1e-12 => Dirac reading is WRONG (conflates no-topological-zero-mode with Dirac-character).
- T1 antilinear discipline held: ||C2 conj(D_F) C2 - D_F||=0 (correct T-sym); ||[C2,D_F]||=0.663 (PITFALL, T-sym not CPT-viol, NOT used).
- m_bb = |sum U_ei^2 m_i| = 8.27 meV (W4-2 U_ei + NuFit-NO scale, m_light->0, no phase), range [4.96,8.27] meV over Majorana phases. Below KamLAND-Zen (<122meV), within next-gen (~6-20meV). W4-2 m_i RAW M_KK-unit quasi-degenerate (spread 0.12) => scale SET EXTERNALLY (NuFit dm2). Verdict INFO (Majorana solid; m_bb on INFO PMNS prereq + external scale).
- PASS-only registration: m_betabeta_FW NOT promoted (INFO). Added NuFit dm2_21/31 + 0nubb-bound comparison anchors to canonical_constants.py.
- CONNECTS: S60 seesaw M_R=1.004 M_KK (the heavy Majorana the determination predicts); open_channel "Majorana sector of D_F" now has a DEFINITE answer (Majorana).

## INV6 W3-4: Antimatter-domain horizon — metric single-domain mechanism CLOSED; tau-simultaneity is the real mechanism (investigation track, FAIL)
- GATE INV6-W3-4-ANTIMATTER-DOMAIN-HORIZON: pre-transit acoustic sound-horizon vs c/H_0. R_horizon = r_acoustic/(c/H_0) = 8.89e-32 (log10=-31.05) << 1 => FAIL (sign FAIL: chain predicted R>1; magnitude FAIL; regime VALID). audit 198255d7.
- DECISIVE: substrate's OWN integrated expansion history (S53 s53_phonon_eos_output.txt Section 8) N_e^total=2.9205 (acoustic-metric driven; N_e^geom=0.1734, N_e^acoustic_only=0.0282); q(tau) -0.97->+0.81 (S54 SCALE-FACTOR-54). N_required for R=1 = 74.36 e-folds => shortfall 71.4 e-folds (31 dex).
- SUBSTRATE-FIRST LESSON: exflation = SPECTRAL COMPLEXIFICATION, NOT metric expansion (phononic-framing). The acoustic sound horizon CANNOT grow super-Hubble because there is essentially NO metric inflation (2.92 << ~60). The plan's track_A "white hole makes pre-transit patch super-Hubble like inflation" (prior 0.80) is FALSIFIED by the substrate's own a(tau).
- WHITE-HOLE PROVEN S85 (s85_w6_acoustic_white_hole_formal; pre/post-fold causally separated) is REAL but only prevents post-fold RE-connection; does NOT grow the PRE-fold comoving horizon to super-Hubble size.
- Fermi-LAT <1e-5 single-domain SURVIVES via a STRUCTURALLY DISTINCT mechanism: tau-SIMULTANEITY (substrate has ONE Jensen slice; fold at one tau value for whole substrate — tau_pivot canonical provenance S87/S88). S41: "Horizon problem AMELIORATED by tau-simultaneity, NOT eliminated." Single-domain = INTERNAL (fiber) coherence, NOT a 4D metric causal patch. delta_A spatial coherence = tau-simultaneity, NOT R_horizon>1.
- COROLLARY for baryogenesis: delta_A is single-domain by tau-simultaneity (the W3-1/W3-2/W3-3 amplitude gates' implicit "delta_A coherent across the patch" assumption HOLDS, but the coherence is internal-space, not metric). G-3 antimatter face filled.
- UNITS DISCIPLINE: comoving sound horizon numeric integral = (c_s/H_f)(e^N-1) [COMOVING-rel-fold]; PROPER closed form = (c_s/H_f)(1-e^-N); differ by factor e^N (~18.5, 1.27 dex) — both legit, must be labeled distinctly (cross-check ratio 1.000001 for matched forms). Verdict robust to proper-vs-comoving (1.27 dex vs 31-dex deficit). 1+z_fold = M_KK/T_CMB = 3.16e29 (entropy-conserving).
- ROUTING: a(t)-map carries K_pivot/a(t) gap (atlas-04 C1/C2) but no refinement closes 31 dex => magnitude FAIL not INFO. No registry/falsifier write (investigation track-local; HY1/HY2/HY3 at investigation-close).

## S116 W-1: J_PMNS=0 forced-vs-artifact (connes×dirac workshop CLOSED; verdict ANSATZ-ARTIFACT-as-derived, HARD doubly-dead)
Context: adjudicate whether [J,D_K]=0 FORCES delta_CP_PMNS in {0,pi}. Converged with connes (NCG): KO-6 [J,D_K]=0 NECESSARY but NOT sufficient (SM finite triple has KO-6 + J_F and is CP-violating; sector-uniform J coexists with measured J_CKM=3.08e-5; Majorana CP cancels from the Jarlskog — only real-eps_LX ansatz gives J=0). The five domain results:
- **D-R2.1 (CPT-MAJORANA CO-DEPENDENCE; closes my old "is there a J_R with eps''_R=+1 => HARD" open-Q).** No independent J_R on the SU(3)_R commutant: order-zero axiom [a,Jb*J^-1]=0 <=> J*pi_L(A_K)*J^-1 = A_K^o, so the commutant (where the generation texture lives) IS J*A_K*J^-1 — ONE reality structure, "J_R" = J on the commutant. Grading INHERITED: KO-dim is a property of the pair (J,gamma_9); gamma_9 acts on the SM-fiber C^16 leg, tensor-disjoint from BOTH carrier (SU(3)_L) and multiplicity (SU(3)_R) leg, so it can't distinguish L from R => eps''_R = eps'' = -1. To force eps_LX real you need K*gamma_9=+gamma_9*K (eps''=+1) => KO-dim 0/4, which FORBIDS the nu_R Majorana mass (Majorana M_R is the J-symmetric part of D_F, admissible only at eps''=-1, KO-dim 2/6; cf. S96 W4-3, CCM-2007 fermion-doubling resolution). So the KO-6 sign eps''=-1 SIMULTANEOUSLY (i) protects the gamma_9-odd CP phase (T9: gamma_9 imaginary in J-basis re-injects i into the off-diagonal mass) AND (ii) admits the Majorana neutrino. HARD-via-reality-structure is self-cannibalising: it would delete the Dirac/Majorana asymmetry that is the whole premise of treating leptons != quarks. HARD DOUBLY DEAD (R1: existing KO-6 J insufficient; E-1: no alternative reality structure rescues without destroying the Majorana sector).
- **D-R2.2 (prescription FIXED-Yukawa by D_K self-adjointness).** Mass operator is the gamma_9-odd block of D_K=[[0,M],[M-dag,0]]; D_K self-adjoint => physical left-handed mixing is the SVD of M (eigenvectors of M*M-dag), NOT a similarity-diag of M (the "normal-operator" J=0.0962 reading, non-physical — a mass is not a Hamiltonian; gauge currents couple to LH fields). Real circulant C => C*C-dag real-symmetric => real-orthogonal U_eL => J=0 (the gamma_9-EVEN reality of M*M-dag = SKELETON, carries NO gamma_9-odd phase). So the "KO-dim-6 J-self-conjugacy forces J_PMNS=0" justification is dead REGARDLESS of CF-W2-1 (even an SA-real outcome is a spectral-action MINIMIZATION prediction, not a J-forcing).
- **D-R2.3 (CF-W2-1 is THREE-WAY; spontaneous-CPV is a NEW outcome).** S(eps_LX)=Tr f((D_K+eps_LX)^2/Lambda^2) is CP-EVEN: S(eps_LX^CP)=S(eps_LX) since CP sends D->D-bar=D^T (self-adjoint) and D,D^T isospectral. A CP-even real function with a UNIQUE min (up to gauge) has that min at a CP-fixed (REAL) point. So the SA minimiser is: (I) unique => REAL => delta_CP in {0,pi} (DYNAMICAL, not J-forced); (II) CP-conjugate-pair {eps*, eps*-bar} gauge-inequiv => SPONTANEOUS CP violation, delta_CP=+-|delta*|, MAGNITUDE predicted (Lee-1973 analog), sign Z_2-broken; (III) continuous-flat => under-determined. DISSENT vs connes: his uniform-measure genericity (CP-conserving locus measure-zero => leans complex) is the WRONG prior — a critical point is itself measure-zero, so the operative genericity is on the SELECTION FUNCTIONAL (CPT-even SA, leans REAL-if-unique), not the moduli measure. Degeneracy is itself non-generic in function space.
- **D-R2.4 (leptogenesis-PMNS sector-internal lock; supersedes s60 Scenario A).** With M_R spectrum-pinned real-diagonal (VII.BL) there is NO free Casas-Ibarra R — the only phase source is the external M_D=eps_LX^nu off-diagonal, gating BOTH: eps_1 ∝ Sum_j Im[(Y-dag Y)_{1j}^2] f(...) (Y=M_D/v, Davidson-Ibarra) AND delta_CP^PMNS from phases of m_nu=M_D^T M_R^-1 M_D. M_D real-rephasable => eps_1=0 AND delta_CP in {0,pi} (both CP-conserving); M_D complex => both !=0 generically (different functions of the same M_D phases, no numerical lock-step, ONE shared condition = M_D reality). Supersedes s60 §3 Scenario A ("[J,D_K]=0 => M_R real => eps_1=0 EXACT" assumed M_R-INTERNAL-real / D_K≡D_F, the over-strong promotion VII.BL refutes). Sector-internal (no off-Jensen U(2) sharing needed): J_PMNS=0-forced (=> real M_D) => eps_1=0 => leptogenesis dead.
- **D-R2.5 (TWO-CHANNEL baryogenesis dichotomy — the load-bearing CF).** K7-transit (phi_CP_K7_transit=pi/2, phi_88-Cartan, canonical_constants.py:674, "non-leptophilic" sector-RESOLVED; my Q-conn-R2-3 ruling: a Cartan phase vs a Jarlskog off-diagonal phase are DIFFERENT CP invariants, no rephasing couples them, so sector-resolution holds STRUCTURALLY at the J level — honest boundary: whether the off-Jensen U(2) feeds both from one parameter is a quantitative CF): J_PMNS=0-forced CONSISTENT. vs leptogenesis (D-R2.4, sector-INTERNAL): J_PMNS=0-forced SELF-FALSIFYING. WHICH channel sources eta_B sets the A2.2 baryogenesis-annotation strength.
Register-grounding (verified this turn): canonical_constants.py:674 phi_CP_K7_transit=pi/2 (phi_88 non-leptophilic), :675 delta_CP_PMNS_substrate=0.0 (provenance :1873 = S99 seesaw gate, NOT a J-derivation), :1873; falsifier-master-inventory.md:2206/2213/2219 Row #89 + #89.audit carry the "[J,D_K]=0=>J_CP=0 forced" MIS-CITATION (routed to mack for re-scope, RETAIN-and-supersede); s60_lepto_cp_log.txt §1 (M_R free complex-symmetric in CCM-2007 NCG-SM) / §3 (Scenario A eps_1=0 EXACT).
Effected: WP session-116-w2-workingpaper.md:167 "What holds" down-tagged; canonical_constants.py:675 comment scope-corrected (value 0.0 unchanged); A2.2/Row #89 routed to mack. New CFs: CFW21-THREE-WAY, BARYO-CHANNEL-ADJUDICATION, LEPTO-PMNS-JOINT-IMAGE, OFFJENSEN-U2-SHARING (S117).

## S117 W3-1: CFW21-THREE-WAY COMPUTED — Scenario III (CONTINUOUS-FLAT), INFO. The D-R2.3 three-way RESOLVED.
- Gate S117-W3-1-CFW21-THREE-WAY (audit 6746198c429eee3f). Finite lepton Dirac D_F=[[0,M_lep],[M_lep-dag,0]] (6x6); S=Tr f(D_F^2/Lambda^2)=2*Sum_i f(sigma_i^2/Lambda^2) is a CLASS FUNCTION of the singular-value spectrum (= the s116 charged-lepton masses [3.19e-5,6.60e-3,0.111]) ONLY. The U_eL orbit at fixed masses (real angles + CP phase delta) is therefore EXACTLY flat.
- **CPT-evenness identity [SIGN] = PASS, EXACTLY 0.000e+00** (200 CP-violating textures, zeta a_4 AND cutoff f*; structural reason sigma(M)=sigma(conj M)=0.0). S is Z2 CP-EVEN, functional-independent. This is D-R2.3 Step 3 NUMERICALLY CONFIRMED (conj(D_K)=D_K^T isospectral).
- **Scenario III, not I**: multistart N=64 -> S_min spread/<S> = 1.072e-15 (all at exact a_4 floor 2*Sum m_i^4=3.03e-4); delta* spread 6.07 rad (~2pi, FREE); multiplicity CONTINUUM (64/64). SA Hessian along CP: H_dd=0.000e+00, lambda_CP=7.5e-29 (<< tol_hess=1e-8). NULL direction.
- **KEY REFINEMENT of D-R2.3**: my pre-registered "CPT-even-SA leans REAL-if-unique" lean toward Scenario I DOES NOT FIRE — the minimiser is NOT unique (continuum/flat valley), so there is no unique min to force real. The bosonic SA is MORE under-determining than the "leans-real" prior: it is BLIND to the lepton CP phase (the phase lives in the unitary orbit at fixed singular values). delta_CP UNDER-DETERMINED by the bosonic spectral action; delta_CP_PMNS_substrate=0.0 CONFIRMED as ANSATZ-ARTIFACT-as-derived (S116 W-1 down-tag stands). "[J,D_K]=0 => J_CP=0 forced" struck; J exact-CPT silent on external gamma_9-odd eps_LX.
- **Non-vacuous control** (the Hessian routine is not dead): bare-grading cross term a_2^lift(delta)=Tr((s_geom*G+M_herm(delta))^2), G=diag(sqrt(C2_E)) fixed, gives H_dd^control=2.15e-4 at s_geom=O(1) (genuine CP curvature) while PRIMARY/CONTROL=0.0. Lift is 1/s_geom physical-scale-suppressed (delta-spread 0.0 at s_geom~M_KK/m_tau) AND excluded by VII.BL multiplicity-SCALAR theorem (G ∝ I => Tr(G M)=G0 Tr(M) invariant).
- Feeds 3-2 BARYO-CHANNEL: SA neither selects M_D real nor forces it complex; the s116 representative texture (M_e REAL) sits at a CP-conserving point of the flat valley (eps_1=0 there), complex M_D equally SA-admissible. So 3-2's K7-vs-lepto adjudication is NOT pre-decided by 3-1 — the M_D phase is a free external parameter, consistent with the D-R2.5 dichotomy.

## S117 W3-2: BARYO-CHANNEL-ADJUDICATION COMPUTED — PASS / channel=PASS-K7 / track_A. The D-R2.5 dichotomy RESOLVED.
- Gate S117-W3-2-BARYO-CHANNEL-ADJUDICATION (audit d1c15711a51db3ef, content 59e7557796c215c3). [SIGN] composite PASS via plan-frozen two-branch channel-adjudication operator (S95 non-compute, strict_PASS_boundary=N/A); 3-tuple sign=PASS/magnitude=INFO/regime=VALID. Reads 3-1=Scenario III (INFO) at runtime => proceeds (not PRE-REG-INC). Inputs: s116 npz (M_D=eps_LX^nu, M_R B-branch real-diag), s60 Davidson-Ibarra machinery, canonical phi_CP_K7_transit/eta_BBN_obs/n_pairs/epsilon_K7/g_star_SM.
- **M_D construction bit-exact**: M_D=yukawa_block_real(Y_nu_diag=[0,4.7936,11.9276], w23=2.8085) = real-symmetric rank-2 (Y_1=0 EXACT => m_1=0); seesaw cross-check max|M_nu(recon)-M_nu(npz)|=0.000e+00 (M_nu=M_D M_R^-1 M_D^T).
- **Channel (b) leptogenesis = 0 EXACT at substrate texture** (load-bearing): Davidson-Ibarra eps_DI=[0,0,0] (real M_D); CP-source max_i|Sum_j Im[((Y-dag Y)_ij)^2]|=0.000e+00 (<1e-12). eta_B^lepto=(28/79)*eps_1*kappa/g_*=0 EXACT (any kappa). Im[(real)^2]=0 — the Dirac exact-vanishing discipline.
- **3-1 flat-direction consequence (M_D-phase scan, 360 pts)**: CP source = 0 at phi=0 (REAL texture), rises to max 9.409e+02 generic phi. Numerical scan matches **Sage-exact Im[((Y-dag Y)_12)^2] = (Y2^2-Y3^2) w^2 sin(2phi)** (amplitude 940.92) to residual 3.41e-13. Leptogenesis CP source ∝ sin(2phi): ODD, zero at CP-conserving {0,pi/2,pi}, FREE elsewhere = the 3-1 Scenario-III flat eps_LX phase. NOT a substrate output; substrate does not pin it.
- **Channel (a) K7-transit = substrate-PINNED**: eps_CP=sin(phi_CP_K7=pi/2)=1.000000 EXACT (MAXIMAL, reality-independent). eta_B^K7_raw=N_pairs*1*eps_K7=59.8*0.00248=0.1483; sphaleron(28/79)+g*-normalized 4.9240e-04; reaches eta_BBN_obs=6.12e-10 at washout kappa~1.243e-6 (strong washout). s61 TRANSIT-BARYOGEN-61 band [1.98e-9,2.22e-6] brackets obs (conservative within ~factor 3).
- **Adjudication**: sgn(eta_K7-eta_lepto)=+1, dominance ratio=inf (eta_lepto=0 EXACT >> x3 threshold) => K7-transit DOMINATES. sign=PASS. magnitude=INFO (eta_BBN reproduction washout-efficiency-dependent, kappa free, NOT zero-param). composite=PASS-K7 via plan operator (overrides generic magnitude=INFO=>INFO collapse, which would misread as plan INFO_meaning "comparable channels" — FALSE; K7 dominates absolutely). composite-precedence row emitted.
- **D-R2.5 RESOLVED — the SELF-FALSIFYING branch does not fire**: the substrate DETERMINES only K7-transit; leptogenesis CP source is under-determined (3-1 flat), zero at the real texture. K7's phi_88-Cartan phase is a DIFFERENT CP invariant from the leptonic Jarlskog (W3-4 OFFJENSEN-U2-SHARING PASS, audit 1d6b5db3: dim=5=1[phi_88 lam8 U(2)-center singlet]+4[eps_LX CP^2 coset], no-linking, gauge-invariant survives real eps_LX). => J_PMNS=0 CONSISTENT with nonzero K7-sourced eta_B (sector-resolved E-3). A2.2 = sector-resolved CONSISTENCY note, NOT self-falsification linkage. Routes to mack Row #89.
- **Internal/external separation**: NOT the S60 eta_B=0 result (INTERNAL [J,D_K]=0 => internal M_R real => internal eps_1=0, STAYS CLOSED). Here M_R real-diag by spectrum-pinning, external phase M_D=eps_LX^nu set by 3-1 (FLAT), NOT by J. J exact-CPT, silent on external gamma_9-odd eps_LX (outside Omega^1_{D_K}).
- Feeds 3-3 LEPTO-PMNS-JOINT-IMAGE: leptogenesis is NOT the substrate-determined channel; 3-3 may map the (eps_1,delta_CP_PMNS) joint image over the free phase as a CONDITIONAL DUNE-testable falsifier, but the substrate's own eta_B answer is K7-transit.
