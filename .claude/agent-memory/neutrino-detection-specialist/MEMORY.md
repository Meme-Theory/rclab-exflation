# Neutrino-Detection-Specialist Agent Memory

## Topic Files
- `constraint-map.md` -- Redirect to unified map at `.claude/agent-memory/constraint-map.md`
- `gate-registry.md` -- Pre-registered gates with outcomes and pending computations

## Project Context
- Framework: phonon-exflation cosmology on M4 x SU(3)
- Neutrino masses = lightest eigenvalues of D_K(s) on Jensen-deformed SU(3), zero free Yukawa couplings
- Reference papers: `/researchers/Neutrino-Detection/` (12 papers, Pauli 1930 to KATRIN 2024)

## Key Experimental Values (NuFit-6.0, September 2024)
- Delta m^2_21 = 7.41e-5 eV^2, |Delta m^2_32| = 2.507e-3 eV^2 (NO)
- sin^2(theta_12) = 0.303, sin^2(theta_23) = 0.451 (NO best fit), sin^2(theta_13) = 0.02225
- delta_CP: consistent with CP conservation for NO; ~270 deg favored for IO at 3.6sigma
- Mass ordering: NO preferred with Delta chi^2 = 6.1 (including Super-K atmospheric)
- KATRIN: m_nu < 0.45 eV (90% CL), aiming 0.3 eV with 1000 days
- Planck+DESI DR2: Sum m_i < 0.064 eV (LCDM), < 0.16 eV (w0wa)
- Target ratio: Delta m^2_32 / Delta m^2_21 ~ 33.8 (NuFit-6.0)
- JUNO first results (Nov 2025): 1.6x precision improvement on theta_12, Delta m^2_21
- T2K+NOvA joint (Oct 2025): <2% uncertainty on mass-squared differences
- MicroBooNE (Dec 2025): single sterile neutrino excluded at 95% CL (LSND/MiniBooNE)

## Structural Results (proven, parameter-free)
- KO-dim = 6 (Session 8). CPT: [J, D_K(tau)] = 0 identically (17a D-1)
- Z_3 = (p-q) mod 3: exactly 3 generations (17a B-4)
- Eigenvalue pairing: max error 3.29e-13 (17a D-3). AZ class BDI, T^2=+1 (17c)
- D_K block-diagonal in Peter-Weyl basis (22b, 8.4e-15)
- Spectral gap minimum 0.819 at tau=0.20 -- gap never closes
- s_0 = 0.2994 from sin^2(theta_W) via gauge coupling derivation (17a B-1)

## Neutrino Connections to Framework
1. Lightest D_K(s_0) eigenvalues = neutrino masses (zero free parameters)
2. Mass ordering = sign(lambda_3^2 - lambda_2^2) at s_0. Prediction: NORMAL (bowtie topology)
3. Once s_0 fixed, masses are overconstrained (KATRIN + oscillation)
4. Dirac/Majorana: J^2=+1 permits Majorana; needs spectral action at s_0
5. Clock constraint: tau frozen to 25 ppm -> constant masses since condensation
6. Tridiagonal selection rules: V(L1,L3) = 0 exactly (NNI texture). Predicts theta_12 >> theta_13

## Current Neutrino Prediction Status (Post-Session 37)

### Closed Avenues for R ~ 33
- Perturbative spectral stabilization: all excluded (A-06)
- Block-diagonal intra-sector: R = 5.68 (O-NU-02)
- Uniform BCS gap: does not modify R (O-NU-03)
- Bulk tridiagonal PMNS: R = 0.29 at all tau (29Ba). V_12/dE_12 ~ 6-9, strong-mixing
- Wall-localized BCS (frame V): R_max = 0.71 (46x below 33). CLOSED in singlet (33 W3)
- Wall-modified couplings: Trap 4 holds exactly at walls. V_12/V_23 ~ 2.7 LOCKED by Schur orthogonality
- Canonical mu!=0: CLOSED (34 MU-35a). PH forces mu=0 analytically
- Grand canonical mu!=0: CLOSED (34 GC-35a). Helmholtz F convex at mu=0
- **PMNS-corrected (spinor V): R_max=0.57, CLOSED (35 W3-A). dE_23/dE_12=5.09 caps R<5.9**

### Session 35 W3-A Key Results (s35_pmns_corrected.py)
- PMNS-CORRECTED-35 gate: FAIL. R=0.57, sin2_13=0.010, theta_23=12.2 deg at self-consistent BCS
- sin^2(theta_13) IMPROVED 20x: 0.203 (frame V) -> 0.010 (spinor V). Just below gate [0.01, 0.05]
- theta_23 WORSENED 3.4x: 42.0 deg (frame V) -> 12.2 deg (spinor V). Far below gate [35, 55]
- R structural ceiling: dE_23/dE_12 = 5.09 at tau=0.20 => R < 5.9 in weak-mixing limit
- R=33 requires V12 enhancement of 22.3x (V12/V23=78) -- no physical mechanism
- BCS gap makes R WORSE (pushes B2 toward B3, reduces gap hierarchy)
- Mass ordering: ALWAYS NORMAL. Structural prediction.
- Self-consistent BCS: g=1.205, Delta=0.0252, Delta/W_B2=0.44

### Session 34 Key Results (neutrino-relevant)
- Corrected spinor couplings: V(B1,B2)=0.077, V(B2,B3)=0.022, V(B2,B2)=0.086
- V(B1,B1)=0 exact (Trap 1). V(B1,B3)=0 exact (Trap 4). Permanent
- NNI texture EXACT: V_11=0, V_13=0, V_12=0.077, V_23=0.022
- V_12/V_23 = 3.5 (Schur-locked). Predicts theta_12 >> theta_13

### Branch Classification (Session 32, updated Session 34)
- L1=B1 (trivial, 1-fold), L2=B2 (fundamental, 4-fold), L3=B3 (adjoint, 3-fold)
- Trap 1 (Session 34): V(B1,B1)=0 exact. Gap-edge self-coupling forbidden
- Trap 4 (Schur): V(B1,B3)=0 exactly -> NNI texture
- Trap 5 (J-reality): B2-only pairing. B2 condensation increases dE_12

### Session 35 Workshop Key Results (neutrino-baptista, Rounds 1-3)
- H_eff approach CLOSED for inter-sector: R*sin2_23 < 3.5 structural bound (10M MC, zero hits)
  - Baptista analytic verification: bound = Delta_23^2*(E3+E2)/(4*Delta_12*(E2+E1)) ~ 1.17 at B2-G1 point
  - Required R*sin2_23 = 32.6*0.546 = 17.8. Shortfall 5.1-15x. No coupling tuning can fix.
- B2-G1 near-degeneracy: gap=0.005 at tau=0.18, gap=0.0016 at tau=0.24
- B2-G1 crossing at tau~0.30: R_bare sweeps through 33 near tau=0.186 (Delta_tau=0.004 from fold)
- At tau=0.24, (1,0) G1[0] at lambda=0.841133 gives R_bare=31.7 (2.8% from target)
- NCG inner fluctuations preserve Peter-Weyl: <(0,0)|phi|(1,0)>=0 identically
- KK modified Lie derivative mixes sectors: V_cross ~ O(0.19) for non-Killing generators
- Paper 18 misalignment approach is SOLE SURVIVING PMNS mechanism
  - R fixed by D_K eigenvalue selection (decoupled from mixing angles)
  - sin2_23 from spinor map Phi-tilde overlap (NOT from H_eff diagonalization)
  - No R*sin2_23 bound applies: eigenvalues and mixing angles are independent
  - Dimensional estimate: sin2_23 ~ 3/7 = 0.43 from 8D degeneracy splitting
  - Baptista rotation angle estimate: sin2_23 ~ 0.31 from arccos(e^{-tau/2}) ~ 25 deg
- INTER-SECTOR-PMNS-36 gate REVISED (FINAL) to require Paper 18 Steps A-C
- Phi-tilde is FINITE-DIMENSIONAL: 16x16 linear algebra in singlet (both metrics left-invariant)
  - Lambda = diag(e^{-tau}, e^{tau}, e^{-tau/2}) on u(1)+su(2)+C^2
  - u(1) rotation ~34 deg, su(2) BOOST ~11 deg (e^tau>1, hyperbolic), C^2 rotation ~25 deg
  - Boost vs rotation distinction matters: SD2 dissent on baptista E3
- Fold DUAL ROLE: creates BCS van Hove AND B2-G1 near-degeneracy for R~33
- FQ2 RESOLVED (Session 36): 8D eigenspace decomposes as 1+4+3 under U(2)
  - BUT: since Jensen preserves U(2), both decompositions are aligned => U = I
  - Non-trivial PMNS requires breaking U(2) (off-Jensen deformation)

### Closed Avenues (updated with workshop)
- ALL previous closures remain
- **H_eff inter-sector**: R*sin2_23 bound < 3.5 vs required 17.8. STRUCTURAL CLOSURE
- Applies to ANY 3x3 real symmetric matrix with these diagonal elements

### Session 36 W2-A Key Results (s36_intersector_pmns.py)
- INTER-SECTOR-PMNS-36 gate: FAIL
- NCG inner fluctuation cross-sector: ZERO confirmed (||D_cross|| = 0.00e+00)
- H_eff bound confirmed: max R*sin2_23 = 16.886 at tau=0.30, required 17.8 (1.1x shortfall)
- **Paper 18 Phi-tilde overlap: ZERO MIXING (all sin2_theta = 0.000 at all tau)**
  - Subspace overlap O_{ij} is EXACTLY DIAGONAL: B_i(tau) projects only onto B_i(ref)
  - Physical reason: U(2) preserved on Jensen curve => Schur locks eigenspaces
  - FQ2 ANSWERED: 8D decomposes as 1+4+3 under U(2), matching B1+B2+B3
  - Since BOTH decompositions use same U(2), overlap is trivially diagonal. U = I.
  - Workshop estimates of sin2_23 ~ 0.3-0.4 were WRONG (confused frame rotation with eigenspace rotation)
- R_inter values confirmed: 27.2 (tau=0.20), 59.8 (tau=0.24), 336 (tau=0.30)
- Mass hierarchy IS available (R sweeps through 33), but mixing angles are zero

### Closed Avenues (updated Session 36)
- ALL previous closures remain
- **H_eff inter-sector**: R*sin2_23 < 3.5 (workshop), confirmed < 16.9 (broader scan). CLOSED
- **Paper 18 singlet Phi-tilde on Jensen curve**: U = I exactly. Schur's lemma. CLOSED
- This closes the LAST explicitly identified PMNS mechanism on the Jensen curve

### Session 37 W1-B Key Results (s37_k7_g1.py)
- K7-G1-37 gate: **FAIL** (algebraic, representation-theoretic)
- q_7(G1) expectation = +0.0447 (nonzero), Var = 0.152, Std = 0.390
- rho(e_7) x I does NOT commute with D_{(1,0)}: ratio = 0.331
  - Because e_7 is not central in su(3): f_{7,3,4}=f_{7,5,6}=sqrt(3)/2
  - NOT a contradiction with Session 34: singlet has rho=0, so commutator trivially zero
- (1,0) under U(2): C^3 = 1_{-1/sqrt3} + 2_{+1/(2sqrt3)}. ALL weights q_7 != 0
- Multiplicity charges (V_{(0,1)}): -0.2887, -0.2887, +0.5774. ALL nonzero.
- Reps WITH q_7=0 weights: (0,0), (1,1), (3,0), (0,3), (2,2), ... all require p=q or p-q=0 mod 3
- Adjoint (1,1) has 4 zero-charge weights. Lowest positive lambda = +0.8730
- But R_alt from (B1, B3_0, adj_mode) triad gives R ~ 0.42 (far below 33)
- e_7 IS Killing: ||L_{e_7} g|| = 0 exactly at all tau (confirmed)
- PMNS classified Level 5: full 3x3 mixing requires fundamentally new structure

### Closed Avenues (updated Session 37)
- ALL previous closures remain
- **K7-G1-37**: (1,0) has no q_7=0 weight. ALGEBRAIC. (B1,B3_0,G1) triad BLOCKED
- **OFF-JENSEN-PMNS-37**: BLOCKED (K7-G1-37 FAIL closes prerequisite)

### Remaining Escape Routes (require NEW computation)
- **Off-Jensen deformation singlet-only**: Breaks U(2), allows B1-B3 2x2 rotation. But 2x2 NOT full 3x3 PMNS.
- **KK modified Lie derivative tilde{L}_{e_a}**: Couples different Peter-Weyl sectors. Not eigenstate overlap but gauge coupling. Distinct mechanism. Not yet computed.
- **Adjoint (1,1) triad**: Has q_7=0 modes, but R ~ 0.42 (far below 33). Would need different eigenvalue selection.
- **Absolute mass scale**: Scale bridge unresolved. BCS gap O(1), not hierarchical.

### Pipeline Status (updated Session 40)
- K7-G1-37 FAIL closes (B1,B3_0,G1) triad and blocks OFF-JENSEN-PMNS-37
- HESS-40: Jensen fold is 28D local minimum of S_full (22/22 positive, min H=1572)
- Off-Jensen deformations INCREASE S_full => eigenvalue ratios at fold are geometric invariants
- No viable 3x3 PMNS mechanism identified on Jensen curve
- Normal ordering and NNI texture remain as Level 4 predictions
- PMNS mixing angles classified Level 5 (requires new structure)
- NEW EXPLORATION DIRECTIONS (S40 collab):
  - Dynamical PMNS from diagonal ensemble eigenstate decomposition (B2-DECAY-40 data)
  - Internal MSW: mode-dependent LZ transit as flavor conversion mechanism
  - B2 quartet splitting from 14% non-rank-1 V_rem as candidate Delta m^2_21

## Upcoming Experiments (updated March 2026)
- JUNO: OPERATING since Aug 2025. First results Nov 2025. Mass ordering ~2030 (6.5 yr at 3sigma)
- DUNE: under construction. Beam early 2030s. 5sigma ordering in 2 yr, 3sigma CPV in 5 yr
- Hyper-K: cavern excavated July 2025. Data-taking 2028. CPV, ordering, proton decay
- KATRIN: running, target 1000 days by end 2025, final sensitivity ~0.3 eV
- Project 8: Phase III development, target 40 meV via CRES
- LEGEND-200: first results 2025 (T_1/2 > 1.9e26 yr combined). LEGEND-1000 planned (10^28 yr)
- KamLAND-Zen: complete dataset published 2024 (T_1/2 > 3.8e26 yr)
- nEXO: planned (T_1/2 ~ 10^28 yr, covers IO Majorana band)
- CONUS+: first reactor CEvNS observation 2025 (3.7sigma)
- MicroBooNE: complete Dec 2025. Sterile neutrino excluded

## Session 41-42 Neutrino Connections
- S41 W1-2: S_F^Connes = 0 identically (BDI T-symmetry). Standard NCG seesaw does NOT apply on SU(3)
- S41 W1-1: Off-Jensen BCS robust (0.17% at eps=0.1). B2 quartet splitting 4.9e-5 (quadratic)
- S41 W1-4: M_KK = 10^9 (Conv A) or 10^13 (Conv C). Conv B EXCLUDED
- S42 Z-FABRIC: Z=74731, c_fabric=c, m_tau=2.062 M_KK. Tau frozen at each spatial point
- S42 TAU-DYN-REOPEN: FAIL (35,000x shortfall survives)
- S42 HF: No massless KK modes. eta ~ 3.4e-9 (0.7 decades from observed)
- Scale bridge UNRESOLVED: D_K eigenvalues at O(1)*M_KK, physical m_nu < 0.45 eV

## Meta-Analysis (March 2026)
- Library audit: 12 papers, adequate historically but missing precision-era references
- Critical gaps: NuFit-6.0, T2K+NOvA joint, JUNO first results, 0nu-beta-beta, CEvNS
- Full request: agent-requests/neutrino-request.md (7 Priority A, 9 Priority B, 5 Priority C papers)

## Physical Neutrino Predictions (Post-Session 36 Collab)
- R = 27.2 at fold (tau=0.20), sweeps through 33 near tau~0.21
- R=27.2 implies Delta m^2_32 = 2.05e-3 eV^2 (18% below measured 2.507e-3)
- Normal ordering B1<B2<B3 at ALL tau>0. Structural, parameter-free
- NNI texture (V_11=0, V_13=0) predicts theta_12 >> theta_13. V_12/V_23=3.5 vs data ratio 3.9
- Near-degenerate eigenvalues (0.82:0.84:0.98) suggest m_beta ~ 0.04 eV if near-degenerate interpretation holds
- Mixing angles ZERO on Jensen curve. Require off-Jensen SU(2)-breaking (Paper 18 Step 3)
- WIND-36: nu=0, topologically trivial BCS. No Majorana edge modes
- BBN-LITHIUM-36: delta_H/H = -6.6e-5, 500x below lithium window. BCS negligible at spectral action level
- Key tau-R table: 0.12->6.6, 0.15->11.2, 0.18->18.9, 0.20->27.2, 0.24->59.8, 0.30->336

## Session 40 Key Results (neutrino-relevant)
- B2 weight corrected: 93.0% -> 81.8% (non-uniform diagonal shifts in full Fock space)
- B2 within-mode weights dispersed: [0.284, 0.264, 0.152, 0.118] (not ~0.232 each)
- B2 diagonal ensemble retention: 89.1% permanent. 4.2% leaks via oscillatory dephasing t=0.922
- B2 near-integrable: <r>=0.401 (Poisson), g_T=0.087, V(B2,B2) 86% rank-1
- QRPA: 97.5% pair transfer EWSR in single B2 mode (omega=3.245). B1 lowest at 1.632
- M_ATDHFB = 1.695 (0.34x G_mod). B1 dominates 71% of cranking mass. Van Hove velocity zero suppresses B2
- NOHAIR-40: T varies 64.6%, S varies 18.1%. Gap hierarchy creates 3 LZ thresholds over 4 decades
- T_acoustic/T_Gibbs = 0.993 (acoustic metric). T/Delta_pair = 0.34 (E5 backbending range)
- M_KK constraint from cosmology: sum(m_i) < 0.072 eV => M_KK < 0.03 eV (3 modes) or < 0.01 eV (8 modes)
- M_KK from Delta m^2_21: ~0.042 eV (from B1-B2 spacing). Consistent with ~0.03-0.04 eV range

## Session Outputs
- Collabs in: sessions/session-{19,20,21,22,23,25,28,29,32,34,36,40}/ (pattern: session-NN-neutrino-collab.md)
- Session 40: session-40-neutrino-collab.md
- Session 37 W1-B: s37_k7_g1.py/npz. Results in session-37-results-workingpaper.md section W1-B
- Session 36 W2-A: s36_intersector_pmns.py/npz/png. Results in session-36-results-workingpaper.md section W2-A
- Session 35 W3-A: s35_pmns_corrected.py/npz/png. Results in session-35-results-workingpaper.md section W3-A
- Session 35 Workshop: session-35-neutrino-baptista-workshop.md (R1-R3 neutrino, R1-R2 baptista, R3B pending)

## Agent Discipline
- NEVER state probabilities, Bayes factors, or odds ratios (Sagan's role)
- Frame outcomes as constraints on surviving solution space
- Only new computation against pre-registered gates constitutes evidence
- Restatement of known results carries zero evidential weight
