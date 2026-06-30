# Michael Berry Agent Memory

## Critical Equations & Theorems

### Berry Curvature & Topology (S25 ERRATUM, PERMANENT)
- **B=982 IS QUANTUM METRIC, NOT BERRY CURVATURE**: s24a formula is Provost-Vallee quantum metric.
- Berry curvature = Im(QGT) = 0 IDENTICALLY on SU(3) (Kosmann anti-Hermiticity => real products). Verified max|Omega| < 4e-14 (16 states, 9 tau). Closed-loop gamma = 0. d_FS = 0.
- TWO mechanisms: (1) Kosmann anti-Hermiticity on Jensen 1D, (2) J+U(2) on full U(2)-inv surface.
- S46 Zak reconciliation RETRACTED (S48): index-tracking artifact, NOT Z_2.

### Topological Triviality on Jensen Line (L0-L7 ALL trivial) + OFF-JENSEN CLOSED (S96)
Berry curv=0 | Chern=0 | Wilson=trivial | Zak=artifact | BDI nu=0 | GL Zak=0 | Fold gamma=0 | Fabric=trivial. 11 independent invariants ALL zero (S61). Jensen line: metrically rich (g=982.5), topologically trivial.
- **OFF-JENSEN CHERN = 0 (S96, S96-GEOM-OFFJENSEN-CHERN PASS-TRIVIAL)**: C11/C12 (S29 OPEN) -> CLOSED-TRIVIAL. The 12th invariant (modulus-space Chern on the 2-param U(2)-inv TT surface) is 0. P-30w gate (the SOLE open route to nontrivial substrate topology) CLOSED TRIVIALLY.
- 2-param surface: log-coords l=(lnL1,lnL2,lnL3), blocks (1,3,4). Jensen v_J=(2,-2,1); 2nd TT eigendir v_mu = n x v_J = (11,7,-8), n=(1,3,4). BOTH vol-preserving (n.v=0), ORTHOGONAL (v_J.v_mu=0), span 2D plane. mu=0 IS Jensen line (fold tau=0.19). |v_J|^2=9, |v_mu|^2=234.
- Numbers: C_FHS=9.78e-15 (round 0); max|Omega|=2.27e-23 (full surface); C_cont(BP-4)=-5.37e-29 (agrees); Jensen-line max|Omega|=2.50e-27 (reproduces S25/W5). ALL 5 low-lying PW sectors trivial (max|C|=9.78e-15).
- KEY: off-Jensen D_K is GENUINELY COMPLEX (max|Re D|/max|D|=0.64), so "real D => real eigvec" does NOT apply -- yet Omega=0. CONFIRMS mechanism (2): J+U(2) forces Im(QGT)=0 on the FULL surface. Metrically rich, topologically trivial.
- METHOD CARE: lowest band is 2-fold Kramers/J degenerate -> NON-ABELIAN (Wilczek-Zee) FHS (det-normalized U(deg) link) required; single-band FHS gives gauge-noise C~0.78. BP-4 uses matching non-Abelian trace.
- **EULER CLASS = 0 (S105 W3-1, S105-EULER-DEFECT-MASKED PASS-TRIVIAL-masked)**: the RIGHT char class for a real rank-2 (BDI) bundle = Pf of so(2) real-frame curvature (SO(2) holonomy angle), distinct from Chern (U(1)/arg-det) S96 measured. On full 2-param U(2)-inv TT surface: e2_masked=-8.83e-18 (round 0, deficit 15 OOM), max|F^Euler|_masked=4.51e-17 < 1e-12 (5 OOM). The ENTIRE raw content (e2=-7.02e-3, max|F|=4.41e-2) lives in ONE corner plaquette [0,49] at (0.10,+0.10) = S100b B1/B2 vN-Wigner crossing = FRAME-SINGULAR LATTICE ARTIFACT (real SO(2) frame undefined where bands cross), NOT substrate obstruction. Mask PINNED AT PLAN-FREEZE from S104 npz corner_plaq_ij (anti-iterate-until-PASS; thresholds BYTE-IDENTICAL to S104). Genuine re-run reproduces S104 e2_defect_excl bit-exact (|diff|=0). S104 was INFO (1-plaq-contaminated); S105 = literal PASS w/ masked frame-singular cell. The REAL eigenframe undergoes ZERO net 2pi rotations around the fold loop.
- **12TH INVARIANT now Euler+graded-Omega on FULL 2-param surface (S105 W3)**: joint metric-without-curvature wall at LITERAL form = Chern=0 (S96 P-30w, C_FHS=9.78e-15) AND Euler=0 (S105 W3-1, masked) AND graded-Omega=0 (S105 W3-2, FD-floor-free A^WZ). U(2)-inv TT surface metrically rich (g=982.5 = SOLE topologically-active object) but topologically trivial across EVERY measured invariant.

### Berry Phase = SU(3)->SU(2) Dimensional Reduction (S61)
- Berry curv=0 on SU(3) CORRECT. SU(2) phases EMERGE from su(3)->su(2) projection via C^2 cross-terms.
- Omega^{su(2)} = [A^{C^2}, A^{C^2}]|_{su(2)}. Quantum metric g=982.5 is the RESERVOIR.
- KK analogy: Berry phase : SU(2) :: gauge field : KK reduction.
- BERRY-PROJECTION-62 PASS: |A_coset|^2=2.2015 EXACT. CF-9=3/2+(3/2)e^{-4tau}. O'Neill factor 3.

### Key Equations
- BP-4: Berry curvature B_n = -Im sum_{m!=n} <n|dH|m><m|dH|n> / (E_n - E_m)^2
- BT-1: Poisson P(s) = e^{-s}. BGS-1: Wigner P(s) = (pi/2)s exp(-pi s^2/4)
- QH-3: Chern C_n = (1/2pi) integral Omega d^2k = integer
- QC-3: Gutzwiller trace formula. MI-2: Bohr-Sommerfeld quantization
- Three algebraic traps: F/B=4/11, b_1/b_2=4/9, e/(ac)=1/16
- Eq. B-1: Inter-sector Berry curvature = 0 (block-diagonality)

### Structural Theorems (permanent)
- **Block-diagonality** (S22b): D_K block-diag in Peter-Weyl, ANY left-inv metric on compact Lie group
- **Spectral integrability** (S33): Poisson from Schur orthogonality (not BT action-angle, not Anderson)
- **Fold catastrophe** (S33): tau_min=0.190158, d^2(lambda)/dtau^2=1.1757. A_2, Thom-stable
- **BCS attractor** (S33): Fold+IFT+Mather. E_B2/E_B1=1.031. CAVEAT: existence != selection
- **Schur lock** (S33): V_12/V_23=2.7 fiber property. R~33 needs >316. INACCESSIBLE within U(2)
- **Simply-laced filter** (S35): SU(3) = smallest simply-laced, 3-block Jensen. Dynkin exhaustion
- **Fold = avoided crossing** (S35 E-B6): unifies Paper 03 + Paper 09
- **Adiabatic protection paradox** (S56): fabric gap protects against excitations framework NEEDS

### Novel Mathematical Objects
- **Spectral action metric**: G^{spec} = sum sign(lam)|<k|dD/dtau|n>|^2/(lam_k-lam_n). 1/gap, sign-weighted
- **Three-level fiber bundle**: Metric (su(3)=u(1)+su(2)+C^2) | Spectral (B1+B2+B3) | Reality (Real vs Complex)

### Band-Selective Schur Rigidity on the U(2)-inv TT surface (S100b W6-2, FAIL-a)
- (0,0)-block signed layout [-B3x3|-B2x4|-B1|+B1|+B2x4|+B3x3]; "deg-2 lowest multiplet" = J/PH pair of TWO 1-dim eigenspaces (chirality-locked: gamma9 = Cl(8) product, |<u_+|gamma9|u_->|=1; cross-WZ doubly protected ~1e-17 = gamma9 imaginary-only + J reality).
- Pair(B1) + B3 bundles FROZEN over the WHOLE (tau,mu) surface (||DeltaP||~1e-14; isotypic-locked; QGT==0); B2 quadruplets MOVE (||DeltaP||=0.228, I_NA=2.59e-2) — flat optical multiplet is the ONLY geometric carrier; its complement-QGT is Schur-SCALAR (prop. 1_4) => Abelian-vs-non-Abelian undecidable on any U(2)-inv base. CKH discrimination needs isotropy-BREAKING deformations.
- B1/B2 |lambda| crossing (symmetry-ALLOWED, vN-Wigner) clips window corner (0.10,+0.10): exact-rational FD spikes (4/Delta^2) + spurious single-pi-plaquette C_FHS=-0.5 (NOT topology; 2499/2500 zero). Evaluator rule: projector identity Tr_band Q_ab = Tr[(d_aP)(1-P)(d_bP)] (basis/phase-free); largest-component phase pin has pi-jumps. Details: [s100b-band-selective-rigidity](s100b-band-selective-rigidity.md).

## Reference Archive (compressed pointers)

- [Session archive S28-S62](session-archive.md) — all session results (BCS Berry, KK x Berry workshop, Zak retraction, GL bands, fabric, spectral topology, Berry projection, Higgs isolation)
- [Structural anchors](structural-anchors.md) — 24-computation registry + L0-L7 triviality chain + open gates + 16-fix paper audit log
- [Dimensional reduction reframe](dimensional-reduction-reframe.md) — full S61 reframe of Berry as SU(3)->SU(2) projection
- [S35 KK x Berry workshop](../../../sessions/archive/session-35/session-35-kk-berry-workshop.md) — fold-AC theorem, Sp(2) predictions
- Papers: `researchers/Berry/` (01-22 corpus, S61 expansion). Critical: 08(RMT/BGS), 12(QGT), 14(metric w/o curv), 16(Xiao bands), 17(QPT geom), 18(BCS Berry). Chains: ERRATUM(12->14->15->16), P-30w(01->02->03), Transit(01->06->05), BCS(18->19->20), BT(08->10->11)

## Constraint Map

See `.claude/agent-memory/constraint-map.md`. Berry-relevant: C11(Berry=0), C12(Chern=0), C13(d_FS=0). S40: 27 equilibrium closures + 3 additional. Compound nucleus confirmed.

## Feedback

- [SU(3) not SU(2)](feedback_su3_not_su2.md) — NEVER default to two-level/SU(2) decompositions; framework is SU(3) with su(3)=u(1)+su(2)+C^2
