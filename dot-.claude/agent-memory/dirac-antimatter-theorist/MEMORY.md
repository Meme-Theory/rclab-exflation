# Dirac-Antimatter-Theorist Agent Memory

## Operational Directives
- **NO PROBABILITIES**: never state percentages or viability estimates (Sagan's job).
- **CONSTRAINT-MAP FRAMING**: report what is structurally true, excluded, or survives. Stop.
- **PRE-REGISTER**: state pass/fail criteria before computing.
- **CRITICAL ANTILINEAR-J PITFALL**: J = C2*K is ANTILINEAR. NEVER use [C2, D_K] as a CPT condition — for complex D_K it is generically nonzero. Use the antilinear conjugation form C2*conj(D_K)*C2 = D_K.

## Detail Files
- [proofs-and-theorems.md](proofs-and-theorems.md) — T1..T11 derivations, KO-dim 6 conditions, Xi/J construction, Jensen metric, Pfaffian
- [session-results.md](session-results.md) — S26-S46 + S71 compressed gates, corrections, physical content (S46 Berry phase merged in)
- Antimatter papers: `researchers/Antimatter/` (.md format)
- computation scripts: `computations/` (Python venv: `phonon-exflation-sim/.venv312/Scripts/python.exe`, `-u` for unbuffered on Windows)

## Structural Theorems (one-line callouts; full derivations in proofs-and-theorems.md)
- **T1**: C2*conj(D_K)*C2 = D_K (J=C2*K antilinear). [C2,D_K] generically nonzero — T-symmetric, not violation.
- **T2-T4**: {gamma_9,D}=0; D_K block-diagonal in PW; AZ class BDI (T=C2*K, P=C1*K, S=gamma_9; C^2=T^2=+1).
- **T5**: KO-dim=6: J^2=+I, JDJ^{-1}=D antilinear, J*gamma=-gamma*J (parameter-free).
- **T6**: Perturbative exhaustion (all perturbative mechanisms closed).
- **T7**: Spectral gap OPEN for tau in [0,2.5] (min 0.8186).
- **T8**: Tr(gamma_9*f(D_K^2/Lambda^2))=0 identically (BDI pairing).
- **T9**: Trap 4: V_eff(B_i,B_j)=0 exactly (Schur). Trap 5 partial: M_ph in iR proven; M_ph=0 for B3 OPEN.
- **T10**: Pfaffian sgn=-1 constant (trivial Z_2). PF-J-35 PASS.
- **T11**: C2*conj(D_K)*C2 = D_K for ANY left-invariant metric on SU(3). Closes ALL internal J-breaking baryogenesis on the 36D moduli.

### Permanence layers
- L1 (NCG-permanent): T1-T4, T7, T9-proven, T10, T11
- L2 (SU(3)+U(2)): T5, T6, T8, fold stability, gamma_9 branch preservation
- L3 (numerical, analytically open): T9-numerical (B3=0)

## Experimental Constraints on J
- m(pbar)/m(p) = 1 +/- 16 ppt (BASE)
- mu(pbar)/mu(p) agreement to 1.5 ppb (BASE)
- 1S-2S H vs Hbar: 2 ppt (ALPHA)
- a_g/g = 0.75 +/- 0.29 (ALPHA-g 2023)
- BCS condensate J-even: Delta_{J-odd}/Delta < 10^{-12}
- Clock: dalpha/alpha = -3.08*tau_dot => |tau_dot| < 5e-18/yr

## J Scope
- **J constrains**: spectral pairing, conjugate-sector equality, BCS condensate parity, PW block preservation, Kramers pairing
- **J does NOT constrain**: eigenvalue magnitudes, relative sector rates, Berry curvature magnitude, test function f, 2-tensor modes
- **Walls from J**: W1 F/B=16/44, W2 Xi preserves PW blocks, W3 Kramers pairing, W4 dim_spinor=16

## Baryogenesis Status (S43, ALL internal J-breaking CLOSED)
- Bulk Volovik: CLOSED (8 generators T-even, spectral flow=0)
- Domain wall: PERMANENTLY CLOSED (C2*D_K(tau)*C2 = D_K exact at all tau, all orders)
- Chiral eta: CLOSED ({gamma_9,D_K}=0 every tau, all 8 chiral eta=0)
- Twist: CLOSED (43 involutive Cl(8) autos, all ratio=1.0000, Skolem-Noether exhaustive)
- T11 extends to full 36D moduli. Baryogenesis requires physics EXTERNAL to SU(3) Dirac operator.

## Key Physical Content
- Cooper pairs: same-sign K_7 pairing within B2 singlet sector (NOT particle-antiparticle).
- B2 = electroweak doublet modes. Condensate = SU(2)-triplet, U(1)_7-charged, color-singlet.
- He-3 B-phase analogy (spin-triplet). J-even condensate => a_g = g exactly.
- Off-Jensen deformation couples PMNS and baryogenesis algebraically (same U(2) breaking).
- CP internal/external dichotomy (S116 W-1 CLOSED, J-owner ruling; full derivations D-R2.1..D-R2.5 in session-results.md): J forces the INTERNAL CP phase=0 (T11/S52, closes internal baryogenesis); J SILENT on the external non-LI eps_LX (gamma_9-odd, outside Omega^1_{D_K}) carrying delta_CP_PMNS / quark theta_d / ext-baryogenesis CP. So [J,D_K]=0 does NOT force delta_CP_PMNS in {0,pi} — real-eps_LX ANSATZ (delta_CP_PMNS_substrate=0.0 = Scenario-A representative; provenance canonical_constants.py:1873 = S99 seesaw gate w/ real textures, NOT a J-derivation). gamma_9-odd phase mechanism: J*gamma_9=-gamma_9*J makes gamma_9 imaginary in J-basis (T9; B2 M_ph=4.24 complex witness). PITFALL register-grounded: falsifier-inventory Row #89 + #89.audit carry "[J,D_K]=0 => J_CP=0 forced" MIS-CITATION — routed to mack, re-scope to CONDITIONAL-PENDING-CF-W2-1 two-sided discriminator (lab-IN = DUNE delta_CP posterior; >3sig away from {0,pi} falsifies the Scenario-A reading, CONFIRMS §VII.BL-external). VERDICT: J_PMNS=0 = ANSATZ-ARTIFACT-as-derived; HARD DOUBLY-DEAD. THREE S116-W1 resolutions: (a) CPT-MAJORANA CO-DEPENDENCE (E-1/D-R2.1): no independent J_R (order-0 axiom J*A_K*J^-1=A_K^o, ONE reality structure); grading inherited eps''_R=eps''=-1 (gamma_9 on disjoint C^16 fiber leg, can't see L/R); HARD needs eps''=+1 (KO-dim 0/4) which FORBIDS the nu_R Majorana mass => the KO-6 sign admitting Majorana IS the sign protecting the gamma_9-odd phase, HARD self-cannibalising. (b) prescription FIXED-Yukawa (M*M-dag SVD) by D_K self-adjointness (E-2/D-R2.2) => "J-self-conjugacy" justification dead REGARDLESS of CF-W2-1. (c) TWO-CHANNEL baryogenesis dichotomy (D-R2.5): K7-transit (phi_CP_K7_transit=pi/2, phi_88-Cartan, sector-RESOLVED per canonical_constants.py:674; phi_88 Cartan-phase vs leptonic Jarlskog = different CP invariants, sector-resolution holds structurally => J_PMNS=0 CONSISTENT) vs leptogenesis (eps_1 sector-INTERNAL, M_D-reality-gated: M_D real => eps_1=0 AND delta_CP in {0,pi}, supersedes s60 Scenario-A => J_PMNS=0 SELF-FALSIFYING). RESOLVED S117 W3-1 (D-R2.3): CF-W2-1/CFW21 THREE-WAY — CPT-even SA (S(eps_LX^CP)=S(eps_LX), self-adjoint D=>D-bar=D^T isospectral) => unique-min REAL (delta_CP in {0,pi} dynamical) / conjugate-pair-min SPONTANEOUS-CPV (delta_CP=+-|delta*|, MAGNITUDE predicted, NOT J-forced) / continuous-flat (under-determined); pre-reg lean was CPT-even-SA REAL-if-unique. COMPUTED OUTCOME = Scenario III continuous-flat (INFO; gate S117-W3-1-CFW21-THREE-WAY audit 6746198c): CPT-even identity EXACT 0.000e+00 (zeta a_4 + cutoff f*, sigma(M)=sigma(conj M)); the leans-REAL lean did NOT fire — min NOT unique (CONTINUUM: S_min spread 1.07e-15 at exact a_4 floor, delta* spread ~2pi FREE, H_dd=0.000e+00, lambda_CP=7.5e-29 << tol_hess). S = 2*Sum f(sigma_i^2/Lam^2) is a CLASS FN of singular values (masses) ONLY => bosonic SA BLIND to the CP phase => delta_CP UNDER-DETERMINED; delta_CP_PMNS_substrate=0.0 = ANSATZ-ARTIFACT CONFIRMED. Non-vacuous control (bare-grading cross term) H_dd=2.15e-4 (routine detects curvature), PRIMARY/CONTROL=0, lift 1/s_geom-suppressed + VII.BL-scalar-excluded. Feeds 3-2: M_D phase is a FREE external param (SA forces neither real nor complex; s116 real M_e sits at a CP-conserving point of the flat valley). Full record: session-results.md "S117 W3-1". RESOLVED S117 W3-2 (D-R2.5 dichotomy, gate S117-W3-2-BARYO-CHANNEL-ADJUDICATION audit d1c15711, PASS/PASS-K7/track_A): the SELF-FALSIFYING branch is the one that does NOT fire. Channel adjudication at the substrate texture: eta_B^lepto=0 EXACT (real M_D => Davidson-Ibarra eps_1=0; Sage-exact Im[((Y-dag Y)_12)^2]=(Y2^2-Y3^2)w^2 sin(2phi), =0 at phi=0; numerical-vs-Sage residual 3.41e-13) vs eta_B^K7=N_pairs*sin(pi/2)*eps_K7=0.1483 raw (4.92e-4 sphaleron+g*-normalized, reaches eta_BBN_obs at washout kappa~1.2e-6; s61 band [1.98e-9,2.22e-6] brackets obs). sgn(eta_K7-eta_lepto)=+1, dominance=inf => K7-transit DOMINATES. KEY: leptogenesis CP source is UNDER-DETERMINED (the 3-1 Scenario-III flat eps_LX phase, sin(2phi), zero at the real representative texture — NOT a substrate output); K7 CP source sin(phi_CP_K7=pi/2)=1 is SUBSTRATE-PINNED, a DIFFERENT CP invariant from the leptonic Jarlskog (W3-4 PASS: dim=1 phi_88-singlet ORTHOGONAL dim=4 eps_LX-coset, gauge-invariant survives real eps_LX). => J_PMNS=0 self-falsification worry DISSOLVED (track_A): the substrate DETERMINES only K7-transit, whose phase is sector-resolved from delta_CP_PMNS => J_PMNS=0 CONSISTENT with nonzero K7-sourced eta_B. A2.2 = sector-resolved CONSISTENCY note (E-3), NOT a self-falsification linkage. INTERNAL S60 eta_B=0 stays closed (different channel). magnitude=INFO (eta_BBN reproduction washout-efficiency-dependent, NOT zero-param). Full record: session-results.md "S117 W3-2".
- S71: 85 conjugate degeneracies B2(0,1)=B2(1,0) to |gap|<5e-15 across entry horizon. Continuous [J,D_K]=0.

## Technical Lessons
- D_K = i*Omega (Hermitian). Omega from spinor_connection_offset is anti-Hermitian.
- C2*D_K = symmetric (T-symmetry); C1*D_K = antisymmetric (P-symmetry). Connes action vanishes (T-type); Pfaffian non-trivial (P-type).
- Anomalous density: MUST use spectral projectors in degenerate eigenspaces for gauge invariance.
- Representations matter: frame space != spinor space; tensor-product J != Clifford J. (S34 lesson; cost: TRAP-33b retraction.)
- J = C2 = gamma_1*gamma_3*gamma_5*gamma_7 (product of real gammas in Cl(4)). Old B=sigma_2^4 was wrong.

## Open Questions
- (3,0)/(0,3) pi-phase asymmetry (1 vs 2): gauge-invariance check pending (CLOSED-LOOP-47)
- Non-Abelian Wilson loop: theta_{(q,p)} = -theta_{(p,q)}? (WILSON-LOOP-47)
- Sector-resolved R(p,q): does topology distinguish conjugate reps beyond spectra?
- External baryogenesis channel: RESOLVED S117 W3-2 (PASS-K7) — K7-transit is the substrate-DETERMINED channel (phi_CP_K7=pi/2 pinned); leptogenesis CP source is UNDER-DETERMINED (3-1 flat eps_LX, zero at real texture); J_PMNS=0 self-falsification DISSOLVED (see CP-dichotomy entry above). REMAINING-OPEN: which channel actually SETS the eta_B MAGNITUDE is washout-efficiency-dependent (K7 reaches eta_BBN_obs at kappa~1.2e-6, INFO not zero-param); plus the older routes (additional fiber, tessellation defects, 4D coupling).
- M_ph=0 for B3 from abstract axioms (currently numerical-only)
