# Dirac-Antimatter-Theorist Agent Memory

## Operational Directives
- **NO PROBABILITIES**: Never state percentages or viability estimates. That is Sagan's job.
- **CONSTRAINT-MAP FRAMING**: Report what is structurally true, excluded, or survives. Stop.
- **PRE-REGISTER**: State pass/fail criteria before computing. Report against criteria after.

## Detail Files
- `proofs-and-theorems.md` — All 11 proven theorems (T1-T11), key equations, permanence hierarchy
- `s46-results.md` — S46 Berry phase topology, B3 proximity gap, tachyonic transit, SU(2,1) J-breaking
- `meta-analysis-gaps.md` — Library gaps identified 2026-03-13 (Priority A-C papers, new researchers)
- Antimatter papers: `researchers/Antimatter/` (33 documents, .md format, upgraded 2026-03-13)
- Tier 0 scripts: `tier0-computation/`
- Collab files: `sessions/session-NN/session-NN-dirac-collab.md`
- Meta-analysis output: `agent-requests/antimatter-request.md`

## Structural Theorems (permanent, see proofs-and-theorems.md for derivations)
1. **T1 (CORRECTED S43)**: C2*D_K(tau)**C2 = D_K(tau) for ALL tau (BDI T-symmetry, antilinear J=C2*K). The PLAIN commutator [C2, D_K] = -2i*Im(D_K)*C2 is NONZERO and order ||D_K||. This is a consequence of T-symmetry, not a violation. Previous statement "[J,D_K]=0" was WRONG for complex D_K.
2. {gamma_9, D_pi(s)} = 0 — spectral pairing lambda <-> -lambda
3. D_K block-diagonal in Peter-Weyl (any left-invariant metric)
4. AZ class = BDI, T=C2*K, P=C1*K, S=gamma_9. Pfaffian sign CONSTANT (trivial Z_2). PF-J-35 PASS.
5. KO-dim=6: J^2=+I, JDJ^{-1}=D (antilinear), J*gamma=-gamma*J (parameter-free)
6. Perturbative Exhaustion: all perturbative mechanisms closed
7. Spectral gap OPEN for all s in [0,2.5] (min 0.818)
8. Tr(gamma_9*f(D_K^2/Lambda^2))=0 identically (BDI pairing)
9. Trap 4: V_eff(B_i,B_j)=0 exactly (Schur, inter-branch)
10. Trap 5 partial: M_ph in iR for real reps (proven). M_ph=0 analytically OPEN for B3.
11. **T11 (S43 W5-1)**: C2*conj(D_K)*C2 = D_K for ANY left-invariant metric on SU(3). Proof: t_a=-s_a in Cl(8). Extends T1 from Jensen 1D to full 36D moduli. Closes ALL internal J-breaking baryogenesis.

## Experimental Constraints on J
- m(pbar)/m(p) = 1 +/- 16 ppt (BASE)
- mu(pbar)/mu(p) agreement to 1.5 ppb (BASE)
- 1S-2S H vs Hbar: 2 ppt (ALPHA)
- a_g/g = 0.75 +/- 0.29 (ALPHA-g, 2023)
- BCS condensate J-even: Delta_{J-odd}/Delta < 10^{-12}
- Clock constraint: dalpha/alpha = -3.08*tau_dot => |tau_dot| < 5e-18/yr

## J Constrains / Does Not Constrain
**J DOES constrain:** spectral pairing, conjugate sector equality spec(D_{(p,q)})=-spec(D_{(q,p)}), BCS condensate parity, Peter-Weyl block preservation, Kramers pairing
**J does NOT constrain:** eigenvalue magnitudes, relative sector evolution rates, Berry curvature magnitude, test function f, flow derivatives, 2-tensor bundle modes
**Walls from J:** W1 F/B=16/44, W2 Xi preserves PW blocks, W3 Kramers pairing, W4 dim_spinor=16

## Key Results by Session (compressed)

### S26-28: Foundation
- V_spec minimum at tau_0=0.15 for rho=0.000510 (Lambda=5.72)
- KO_F=6, J^2=+I for full 12D product. 6/7 NCG axioms pass; Axiom 5 fails (order-one=4.000, exact Cl(8) constant)
- Axiom 5 failure INDEPENDENT of [J,D]=0, BDI, Pfaffian — none affected
- Framework = hybrid NCG-KK: selectively uses {J, gamma, KO-dim, order-zero, spectral action}, routes around Axiom 5

### S29: KC Chain Complete + Off-Jensen
- KC-1 through KC-5 all PASS. First mechanism to survive full constraint chain.
- Jensen is SADDLE in 5D (2/4 negative eigenvalues). REDIRECT, not closure.
- True minimum in U(2)-invariant 3D subspace. All structural theorems survive off-Jensen.
- sin^2(theta_W) -> 0.231 at eps_T2=0.049 (conditional). Pre-registered gate P-30w.
- J_perp=1/3 exactly (Schur). J/Delta=1.17-4.52 (strong Josephson). Mean-field justified.
- BCS J-even at 3 levels: mean-field, Gaussian, Josephson. Delta_{(3,0)}=Delta_{(0,3)} at machine eps.
- J indirectly selects geometry: J constrains condensate parity, condensate selects geometry (F_BCS 1000x V_spec)
- t_BCS = 0.16/M_KK. One free parameter. Natural GUT scale.

### S31: Axiom 5 Scrutiny
- Order-one violation 4.000 is 15.5 sigma above random (mean 2.995, std 0.065)
- Order-ZERO [a,b^0]=0 PASSES for A_F=C+H+M3(C). A_F uniquely selected from 128-dim commutant.
- Loss: classification uniqueness, inner fluctuation gauge fields, Higgs as discrete distance
- Preserved: CPT, spectral pairing, topological classification, spectral action, particle-antiparticle split

### S32: Traps + Mechanism Chain
- Trap 5: B2 nonzero (4.24), B1/B3 zero. J maps B2->conjugate rep (exits multiplet).
- RPA-32b PASS (38x): spectral action curvature d^2/dtau^2=20.43. Wall 4 circumvented.
- W-32b PASS (1.9-3.2x): van Hove LDOS at domain walls. Wall 3 bypassed.
- Mechanism chain: I-1 -> RPA -> Turing -> WALL -> BCS. 3/5 links computed.
- Baryogenesis: B2 complex => J maps B2->B2-bar at wall. Relative phase = CP-violating order parameter.

### S33: Math Permanence Workshop
- Trap 5 partial proven (M_ph in iR, 4 steps from KO-dim 6). Full M_ph=0 OPEN.
- Trap 4 proven on full M_{U(2)} (Schur, any U(2)-equivariant perturbation)
- QGT Selection Rule: Berry curvature=0 on U(2)-invariant, quantum metric nonzero, SA curvature from QM only, restricted to B2
- Permanence layers: L1 (NCG) > L2 (SU(3)+U(2)) > L3 (numerical)
- Open: Clifford structure beyond U(2) rep theory needed for B2 M_ph != 0

## Three-Monopole Topology (Session 21c)
- M0 (tau=0): (0,0)/(1,1) degeneracy. M1 (tau~0.10): Z3 crossing. M2 (tau~1.58): gap=8e-6
- Physical window [0.10, 1.58]: (0,0) singlet controls gap edge

### S34: The Correction Session (3 bugs, 3 permanent results)
- J CORRECTED: C2 = gamma_1*gamma_3*gamma_5*gamma_7 (product of real gammas in Cl(4)). Old B=sigma_2^{x4} wrong.
- V MATRIX CORRECTED: TRAP-33b used frame-space A_antisym (V=0.287). Correct spinor K_a_matrix gives V=0.057.
- TRAP-33b RETRACTED: M_max=2.062 was wrong kernel. Correct spinor M_max=0.902 at step wall.
- Wall DOS corrected: van Hove singularity at fold tau=0.190. rho_smooth=14.02/mode (2.6x over step 5.40).
- VH-IMP-35a PASS: M_max=1.445 (smooth wall + imp 1.0 + spinor V). Chain 5/5 at mean-field.
- [iK_7, D_K] = 0 at ALL tau. Jensen breaks SU(3)->U(1)_7. K_7 = unique surviving generator.
- iK_7 eigenvalues: B2=+/-1/4, B1=0, B3=0. PH maps (lambda,q)->(-lambda,-q).
- Schur on B2: Casimir=0.1557, irreducible, V(B2,B2) basis-independent (1000 U(4) rotations).
- Trap 1 confirmed: V(B1,B1)=0 exact (singlet selection rule, all 8 generators, all tau).
- mu=0 forced: canonical (PH) and grand canonical (Helmholtz convex). Connes 15/16 discovered.
- BMF corridor: N_eff>5.5 required. N_eff=4 gives 35% suppression (FAIL). Continuum GMB 12% (PASS).
- Lesson: representations matter. Frame space != spinor space. Tensor product J != Clifford J.

### S35: Pfaffian Verification + Specificity Test
- PF-J-35 PASS: sgn(Pf(C1@D_K)) = -1 at all 34 tau (9 stored + 25 first-principles)
- BDI: T=C2*K ([T,D]=0, T^2=+1), P=C1*K ({P,D}=0, P^2=+1), S=gamma_9=C2*C1
- Pfaffian uses P (particle-hole), NOT T (time-reversal). Session 34 corrected T only.
- gamma_9*C2=C1 exactly => C1 unchanged by J correction => Pfaffian unchanged
- Old B=sigma_2^{x4} was neither C1 nor C2 and gave non-antisymmetric M. Corrected.
- Spectral gap min=0.8186, OPEN at all tau in [0,2.5]
- Key insight: Pfaffian matrix M=C1@D_K, antisymmetric because {P,D}=0 + C1 real symmetric + C1^2=I
- SPEC-35 PASS: d^2S(SU(2)xSU(2))=-3.42 vs d^2S(SU(3))=+20.42. Ratio=-0.168. SU(3) anomalously curved.
- SU(2)xSU(2) has NO eigenvalue folds (all monotonic decreasing). SU(3) B2 fold unique.
- Bug fix: D_j on SU(2) is anti-hermitian in Peter-Weyl rep. Physical eigenvalues = imag parts.
- Bug fix: npz total_d2 shape (1,) needs .item() not float().

### S36: The Needle Hole + Physical Content
- GL-CUBIC-36 PASS: Second-order transition. U(1)_7 charges +/-1/2 forbid all cubic GL. Z_2 universality.
- ANOM-KK-36 PASS: 150/150 anomaly coefficients = 0. Levels 0-3 all vector-like. pi_1(SU(3))=0.
- COLL-36 PASS: chi/chi_sp = 12.1 W.u. Vibrational.
- MMAX-AUTH-36 PASS: M_max in [1.351, 1.674]. "1.445" superseded (rho_B1=1.0 artifact).
- W6-SPECIES-36 PASS: Lambda_sp/M_KK = 2.06. Species wall RESOLVED.
- ED-CONV-36 PASS: E_cond enhanced -0.115 -> -0.137. B1 catalyst. B2-only gives E_cond=0!
- INTER-SECTOR-PMNS-36 FAIL: All 3 routes closed on Jensen (Schur). R=27.2, normal ordering survive.
- SC-HFB-36 FAIL: M_max(GCM)=0.646 unconstrained.
- WIND-36 FAIL: nu=0 trivial. E_B2/Delta=33.4 deep trivial. mu=0 blocks topological transition.
- BBN-LITHIUM-36 FAIL: delta_H/H = -6.6e-5, 500x below threshold. UV-dominated spectral sums.
- TAU-STAB-36 FAIL: S_full monotonic. dS/dtau=+58,673 at fold. 376,000x E_BCS.
- TAU-DYN-36 FAIL: Fast roll. t_dwell/tau_BCS = 2.59e-5. Shortfall 38,600x. Overdamped regime.
- Chain status: UNCONDITIONAL (S35) -> CONDITIONAL -> BROKEN (linear SA). Cutoff escape route OPEN.
- PHYSICAL CONTENT (lava analysis, S36 collab):
  - Cooper pairs are NOT particle-antiparticle pairs. Same-sign K_7 pairing within B2 singlet sector.
  - B2 = electroweak doublet modes. Condensate = SU(2)-triplet, U(1)_7-charged, color-singlet.
  - Analogy: He-3 superfluid B-phase (spin-triplet). NOT conventional BCS (spin-singlet).
  - J-even condensate: identical in particle/antiparticle sectors. a_g = g exactly.
  - Pfaffian sgn=-1 protects spectral gap and Kramers pairing of normal state.
  - Off-Jensen deformation couples PMNS and baryogenesis algebraically (same U(2) breaking).

### S40-S42: Structural Cartography + LCDM (compressed)
- J commutes with D_K through entire transit. BCS, pair creation, GGE, Gibbs all J-symmetric. T_acoustic same for matter/antimatter.
- S41: (C2*D_K)^T = C2*D_K (PERMANENT). S_F^Connes = 0 identically. Pfaffian = only non-trivial fermionic bilinear.
- S42: eta is KINEMATIC envelope, NOT baryon excess. [J,D_K]=0 => equal B and Bbar. epsilon_CP ABSENT.
- GGE is J-symmetric: DM prediction CPT-exact. a_g = g structural. w = -1 + O(10^{-29}).

### S43: Baryogenesis Closures (all J-breaking paths on Jensen closed)
- BARYO-K7-43: All 8 generators T-EVEN (antilinear). Spectral flow = 0. Bulk Volovik: CLOSED.
- JODD-WALL-43: C2*D_K(tau)*C2 = D_K(tau) EXACT at ALL tau + ALL orders. Domain wall J-breaking: PERMANENTLY CLOSED.
- CHIRAL-ETA-43: {gamma_9, D_K(tau)}=0 at EVERY tau. All 8 chiral eta = 0. No chirality asymmetry.
- TWIST-43: 43 involutive Cl(8) autos, ALL ratio=1.0000. Skolem-Noether exhaustive.
- T11 (W5-1): C2*conj(D_K)*C2 = D_K for ANY left-invariant metric on SU(3). Closes ALL internal J-breaking baryogenesis.

### S46: Berry Phase Topology + CPT (see s46-results.md for detail)
- 13 pi Berry phases, Z_2 = -1 (nontrivial Zak phase, reconciles with Omega=0)
- (3,0)/(0,3) pi-count asymmetry (1 vs 2): needs gauge-invariance check (CLOSED-LOOP-47)
- B3 gap proximity-induced by J-even B2 condensate. SU(2,1) breaks [J,D]: CLOSED as direct replacement.
- All 279 scalar fluctuations tachyonic (J-invariant). Gram PSD theorem PERMANENT.
- Non-singlet dissipation 3.8x shortfall (J-even). 38 total closures.

## Open Questions / Next Gates (post-S46)
- Off-Jensen T-symmetry: T11 proven for all left-invariant metrics. Internal baryogenesis via J-breaking: CLOSED.
- Baryogenesis requires physics EXTERNAL to SU(3) Dirac operator (epsilon_CP absent).
- (3,0)/(0,3) pi-phase asymmetry: gauge-dependent or physical? (CLOSED-LOOP-47)
- Non-Abelian Wilson loop: theta_{(q,p)} = -theta_{(p,q)}? (WILSON-LOOP-47)
- Sector-resolved R(p,q): does topology distinguish conjugate reps beyond spectra?

## Technical Lessons
- Always use venv Python: `"phonon-exflation-sim/.venv312/Scripts/python.exe"`
- branching_computation_32dim.py runs Phase 2 on import (~10s overhead)
- Python -u flag needed for unbuffered output in background tasks (Windows)
- Spectral gap equivalence theorem sidesteps tensor product complications for Pfaffian
- D_K = i*Omega (Hermitian). Omega from spinor_connection_offset is anti-Hermitian. Physical eigenvalues = evals of i*Omega.
- Anomalous density in BCS: within degenerate eigenspaces, MUST use spectral projectors Pi = evecs@diag(indicator)@evecs^dag for gauge invariance. Individual eigenvector pairing gives gauge-dependent results.
- C2*D_K = symmetric (T-symmetry), C1*D_K = antisymmetric (P-symmetry). Connes action uses T-type => vanishes. Pfaffian uses P-type => non-trivial.
- **CRITICAL (S43 W3-3)**: J = C2*K is ANTILINEAR. NEVER use [C2, D_K] as CPT condition. Use C2*conj(D_K)*C2 = D_K. The plain commutator [C2, D_K] = -2i*Im(D_K)*C2 is nonzero for complex D_K and measures nothing about CPT violation. D_K on SU(3) is always complex.
