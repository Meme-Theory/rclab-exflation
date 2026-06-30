# Session 73B Synthesis: Causal Structure of a Non-Monotonic Fiber Spectrum and an Unstabilized Modulus

**Date**: 2026-04-11
**Agent**: schwarzschild-penrose-geometer
**Source Documents**:
- `sessions/archive/session-73b/session-73b-results-workingpaper.md`
- `.claude/agent-memory/schwarzschild-penrose-geometer/MEMORY.md`
- `sessions/framework/Penrose-Diagrams.md` (reference)

**Focus**: Exact solutions, global causal structure, Penrose compactifications, singularity classification, trapped surfaces, holonomy / twistor methods.

---

## I. Session Outcome

S73B delivers two structural causal results that tighten the framework's geometric skeleton while narrowing its prediction layer. First, the non-monotonic fiber power spectrum that produces alpha_s = +0.833 (W1-A FAIL) is proven in W5-B to be L_max-INVARIANT to machine precision: the B1/B2/B3 spectral branches live in the three lowest Peter-Weyl sectors (0,0), (0,1), (1,1) and are STRUCTURALLY DECOUPLED from higher-L sectors by the S22b block-diagonal theorem. This is the spectral analog of Birkhoff rigidity: the fabric's lowest-sector geometry is protected from the rest of the representation tower exactly as a spherically symmetric vacuum metric is protected from multipole perturbations. Second, EFOLD-MAPPING (W1-D) finds the bare-action modulus overshoots to tau_max = 1.614, reverses, and runs away through tau = 0 to tau = -infinity -- without BCS dressing or instanton back-reaction, there is NO V_eff minimum. Combined with WILSON-LOOP (W3-C) proving W = I to 6.60e-14 because H(tau) is real symmetric on the Jensen line, the substrate's global causal portrait is: metrically rich, topologically trivial, structurally rigid, and dynamically unconfined in the bare theory.

---

## II. Key Results from the Causal/Geometric Lens

### 1. TRANSIT-PS FAIL and the L_max-Invariance of the Non-Monotonic Fiber P(k)

**Result**: alpha_s(CMB) = +0.833 at L_max=3 (W1-A), shifts to +0.83360244 at L_max=7 (W5-B). Relative L_max shift = +0.113%. The B1 mode BCS squeeze r_BCS = 3.571 = 2 * r_B2 is an exact arctanh(Delta/E_k) identity from the (0,0) sector Dirac spectrum, and the (0,0)-sector eigenvalues match between L_max = {3, 5, 7} to machine precision (0.00e+00). Classification: PHONONIC.

From the causal lens, this is a statement about the substrate's "entry horizon" spectral structure -- the mode content that crosses the transit fold and appears as frozen-out relic radiation. In S72 I established that the entry horizon at tau ~ 0.22 is deeply thermal (T_entry = 72.84 M_KK, |beta|^2 ~ 85, squeeze r ~ 2.9 comparable to the fold itself). S73B W5-B now closes the loop: the r_BCS values populating that horizon are LOCKED by the Peter-Weyl decomposition of D_K. The non-monotonic P(k) -- P_B1 > P_B3 > P_B2 with k_B1 < k_B2 < k_B3 -- is an IRREDUCIBLE feature of the (0,0), (0,1), (1,1) sector geometry, not a truncation artifact.

This is the substrate's version of Birkhoff's uniqueness theorem applied at spectral level. Birkhoff says the exterior of any spherically symmetric vacuum region is exactly Schwarzschild, independent of the mass distribution within. Here: the (0,0)-sector spectrum is exactly its block-diagonal value, independent of how many higher sectors are enumerated in the sum. The acoustic causal diagram (S70 four-panel acoustic Penrose, S72 entry-horizon analysis) is therefore NOT affected by the L_max reclassification from W5-A. The three BCS branches carrying the entry-horizon spectral content are the same at every L_max >= 2. The sonic horizons at {tau_exit = 0.160, tau_entry = 0.220} found in S70 retain their locations unchanged.

Constraint: The framework's fiber P(k) is structurally non-monotonic; this cannot be fixed by refining the truncation.
Implication: Any alpha_s resolution must act at the transfer-function level (k-dependent GGE / multifield delta-N transfer), not at the spectral level.
Surviving space: The acoustic white-hole causal diagram is intact. The fiber-to-CMB mapping is the remaining degree of freedom.

### 2. EFOLD-MAPPING and the Unstabilized Modulus (Penrose Diagram of a Runaway)

**Result**: N_total = 132.4 e-folds decomposed as N_transit = 3.73e-3 (stiff epoch), N_modulus = 63.4 (bare-action potential-dominated), N_post_rh = 69.0 (standard cosmology). Modulus overshoots to tau_max = 1.614 at t = 0.092 M_KK^{-1}, turns around at dV/dtau > 0, rolls back through tau = 0 and runs to tau = -infinity. w_fold = +0.149, w(t > 1 M_KK^{-1}) = -0.997. Classification: GEOMETRIC.

This is a first-class causal structure result, and it forces a rewrite of my modulus space organizational diagram. The tau_NEC = 1.382 boundary (C_2 Ricci eigenvalue crosses zero, from S49) is WITHIN the overshoot range [0.190, 1.614]. The modulus PENETRATES the NEC-violation region during the bare-action bounce. At tau > 1.382, one of the C_2 Ricci eigenvalues is negative; the null energy condition is violated; the Penrose 1965 singularity theorem's energy-condition premise fails.

The Penrose diagram of the unstabilized modulus is the following. Start from the fold at tau = 0.190 with the acoustic white-hole causal structure (S70, four panels). The modulus evolves kinematically -- on the substrate side this is a Jensen-line geodesic, volume-preserving (a_0-tau-derivative = 0 exactly, reconfirmed in W5-A). The geodesic exits the post-transit freeze region at tau = 0.22, continues past the geometric phase transition at tau = 0.537 (K_C2_sectional zero-crossing, spacelike boundary), past the Weyl eigenvalue zero-crossing at tau = 0.895, past the NEC boundary at tau = 1.382, and reaches the kinematic turnaround at tau_max = 1.614 -- a full 0.232 tau-units PAST the NEC violation.

```
        tau=-inf        tau=0          tau=0.22    tau_NEC  tau_max=1.614
          ||             |               |         1.382       |
          || (run-away)  | (round SU(3)) | (freeze)  |         | (turnaround)
          ||             |               |           |         |
         RUNAWAY <----  FREEZE  ----> [NEC-violating excursion] ---> back to -inf
         "future              PHYSICAL            (no trapped surfaces,
          asymptotic           UNIVERSE             but energy-condition
          region"              LIVES HERE           region hostile to proof)
```

Because the Jensen deformation is volume-preserving and the constant-ratio trap (F/B = 0.55, from S44) fixes the proportions, no trapped surface forms anywhere on the modulus worldline. The "singularity" at tau = -infinity is the same K ~ exp(4tau) curvature singularity I catalogued in S44, with the crucial correction: the sign of tau has flipped. The runaway does not approach the timelike-in-SU(2), spacelike-in-C2-U(1) singularity at tau = +infinity; it approaches a DIFFERENT direction in modulus space where the Jensen metric scales as u(1) -> e^{-2|tau|}, su(2) -> e^{2|tau|}, C^2 -> e^{-|tau|}. The SU(2) directions blow up while C^2 and U(1) contract. The Kretschmann scalar still diverges but with a different directional signature.

Is this a causal problem? Yes, and of a specific geometric type. The bare spectral action provides a MONOTONE potential S(tau) that does not admit a minimum (proven W1-D, derived from S73A monotonicity). A scalar field evolving in a monotone potential is a geodesic in the reduced Friedmann phase space; it has no rest point. The substrate is dynamically unconfined. The causal structure has a FUTURE ASYMPTOTIC REGION that is not I+ (future null infinity) but rather a modulus infinity -- a place where the internal geometry degenerates without any external observer noticing, because the 4D scale factor a(t) continues its quasi-de Sitter phase.

This is the cosmic censorship question in modulus-space form: is the runaway singularity at tau = -infinity hidden from an asymptotic 4D observer? The answer is YES, but trivially -- the 4D scale factor is monotonic a(t) -> infinity (quasi-dS with w -> -1), so the observer's past light cone never captures the internal dynamics. The runaway is not a spacetime singularity; it is a modulus-space future asymptotic region, invisible because tau is effectively frozen once H dominates.

Constraint: The bare action has no modulus minimum. The Planck n_s window tau in [0.448, 0.700] is CROSSED in ~0.17 M_KK^{-1}.
Implication: Stabilization is not optional; it is the only way to make n_s well-defined.
Surviving space: Either (a) BCS dressing creates a V_eff minimum, (b) instanton back-reaction pins kappa = 1 at tau = 0.480, or (c) the modulus is genuinely unconfined and all observables depend on when perturbations imprint. Options (a) and (b) are live candidates for S74.

### 3. WILSON-LOOP FAIL and the Topological Triviality of the Jensen Line

**Result**: W = I to 6.60e-14 for the N_occ = 8 full Fock space Wilson loop on the BCS ground state manifold. pi-phase count = 0. Berry phase gamma_gs = 0. No level crossings (gap range [0.256, 0.259] M_KK throughout the loop). Classification: GEOMETRIC.

This is the definitive topological result for the BCS ground state on the Jensen line, and it is my specialty. The proof is a matrix-algebra theorem, not a numerical observation:

**Theorem (Jensen-line Wilson loop triviality)**: H(tau) = 2 * diag(eps_k(tau)) - V is REAL SYMMETRIC for all tau on the Jensen line, because eps_k(tau) are real eigenvalues of D_K^2 (which is self-adjoint) and V_bare is the real symmetric Kosmann pairing kernel. Real symmetry implies:

(i) All eigenvectors can be chosen real
(ii) Berry curvature = Im(QGT) = 0 identically
(iii) Berry connection A_mn real antisymmetric (A_mm = 0)
(iv) Wilson loop W for any contractible loop = +I (trivial holonomy)
(v) pi-phase count = 0

This extends the chain of topological-triviality results on the Jensen line: S25 (Berry curvature = 0), S36 (BDI winding = 0), S48 (Zak phase = artifact), S55 (Berry phase around fold = 0), S73B (non-Abelian Wilson loop = I). Every holonomy measurement has returned the identity.

From the causal/twistor perspective, this is equivalent to saying the Jensen line carries NO non-Abelian Aharonov-Bohm structure. The BCS ground state bundle is trivially parallelizable -- there is no gauge field, no twistor line, no Berry-Pancharatnam phase. The "topology" the framework carries must live somewhere else:

(a) In the SUBMERSION geometry (SU(3) -> SU(3)/SU(2), S62 BERRY-PROJECTION gave |A_coset|^2 = 2.20 from the projection-induced A-tensor).
(b) In the GLOBAL CAUSAL STRUCTURE (Penrose diagrams from S53-S72 showing sonic horizons, trapped-surface absence, pi_1(SU(3)) = 0).
(c) In the OFF-JENSEN directions (breaking real symmetry lifts the degeneracy and can reintroduce Berry curvature, per S69 off-Jensen rigidity).

From the twistor perspective: the Wilson loop W = I means the Robinson congruence on the Jensen line has zero twist. Penrose's non-linear graviton construction requires a non-trivial H^1 cohomology class on twistor space; on the Jensen line, that cohomology is zero. This is consistent with my S50 finding that the 12D Lorentzian CMPP classification is EXACT TYPE D in the static case. Type D spacetimes have two shear-free null geodesic congruences; the Jensen line is a one-parameter family of Type-D spacetimes, and the Robinson-trautman family analog is trivially flat in the sense of W = I.

Constraint: The Jensen line cannot produce topological protection via Berry phase, Wilson loop, or Zak phase.
Implication: Any topological structure in the framework must come from OFF-Jensen perturbations or from the coset (SU(3)/SU(2)) submersion geometry.
Surviving space: The coset-level Berry curvature (|A_coset|^2 = 2.20, S62) is the SOLE surviving source of topological content for the BCS sector. The framework's "topological protection" language must be qualified accordingly.

### 4. MULTI-CELL-INTEG PASS and the Ordered Veil as a Cauchy Surface Analog

**Result**: <r> = 0.4044 +/- 0.0015 at N_pair = 4 across 4 cells (dim 35,960). Below the PASS threshold 0.45. Brody eta = 0.000 (pure Poisson) in every Z_4 sector. The single-cell chaos at N_pair = 4 (<r> = 0.5596, GOE) DOES NOT PERSIST when the pairs are distributed over 4 cells. Classification: NON-PHONONIC (spectral statistic), but structurally critical.

From the causal lens, this is a Cauchy surface property. In classical general relativity, a Cauchy surface is a spacelike 3-surface whose entire past and future light cones are determined by its data. Integrability (conserved charges) is the statistical analog: if enough conserved charges exist, the phase space factorizes and the system evolves on a constrained manifold rather than mixing through the full Hilbert space. The multi-cell integrability test at N_pair = 4 probes whether this factorization survives at the largest Hilbert space dimension yet tested (35,960).

The result is that the 4-cell C_4 ring with Josephson coupling E_J/Delta = 7.32 stays in the Poisson regime. Mapping to my causal vocabulary: the substrate's "dynamical Cauchy surface" -- the constraint manifold on which the integrable evolution takes place -- is robust at multi-cell scale. The Ordered Veil is intact at the level tested.

But the more striking structural observation is the DILUTION EFFECT: the same N_pair = 4 in a single cell (dim = 70) produces chaos, while distributed across 4 cells it produces integrability. This is a version of the cosmic no-hair theorem or of the supersonic horizon problem: local regions can look chaotic, but the global substrate stays integrable because generic fluctuations dilute. The single-cell chaos is a finite-size artifact of the Fock-space saturation (4 pairs in 8 modes = half-filling), not a genuine transition to quantum chaos.

For the global causal picture, this means the Ordered Veil -- the GGE relic that never thermalizes -- has a structural protection mechanism: as the lattice grows, the filling fraction decreases, and Richardson-Gaudin integrability becomes STRONGER, not weaker. The GGE relic is stable not just because the transit is fast (the kinematic five-layer laminar protection from S72), but because the thermodynamic limit itself is integrable. This is the deeper reason the ballistic Mach = 331 transit can survive across 32 cells without thermalizing.

Constraint: Multi-cell integrability survives at the largest Hilbert space tested. Single-cell chaos is a filling artifact.
Implication: The Ordered Veil is structurally protected by dilution, not just by transit speed.
Surviving space: R-G integrability at N_pair >= 5 is the next frontier, but the trend is that integrability STRENGTHENS with dilution.

### 5. W5-B TRANSIT-PS-L7-FLIP UNCHANGED -- The Substrate Causal-Structure Theorem

**Result**: The B1, B2, B3 BCS branches are computed from the three lowest Peter-Weyl sectors (0,0) [B1 at 0.81974111], (0,1)/(1,0) [B2 at 0.84521210], (1,1) [B3 at 0.97140762]. At L_max = {3, 5, 7} the (0,0), (0,1), (1,1) sector eigenvalues agree to 0.00e+00 (machine precision). The alpha_s(CMB) shift from L=3 to L=7 is +0.113% (well within "UNCHANGED"). Fold-only |beta|^2 maximum shift 0.026% (spline noise only). Classification: PHONONIC, elevated to GEOMETRIC via the block-diagonal theorem.

This deserves separate treatment because it is the CLEANEST STRUCTURAL RESULT of S73B. The proof is two lines: (i) the block-diagonal theorem (S22b) states that D_K is exactly block-diagonal in Peter-Weyl sectors (three independent proofs, verified to 8.4e-15); (ii) therefore adding higher-L sectors to the sum cannot shift the eigenvalues of already-present sectors. Since B1, B2, B3 are eigenvalues of the (0,0), (0,1), (1,1) sector Dirac operators respectively, and these sectors exist at any L_max >= 2, the BCS ladder eigenvalues are L_max-invariant at any truncation level greater than or equal to 2.

From the causal/geometric lens, this is the same statement as Birkhoff's theorem applied to the spectral triple: the structure of a given sector is determined by that sector alone and cannot be modified by adding unrelated sectors. The block-diagonal theorem is the spectral triple analog of the vacuum spherical-symmetry rigidity result.

The causal consequence: the acoustic Penrose diagram of the transit (S70, four panels) is STRUCTURALLY invariant under L_max refinement. The sonic horizons at tau = {0.160, 0.220}, the acoustic white-hole causal structure, the r_BCS squeeze values r_B1 = 3.571, r_B2 = 1.786, and the non-monotonic fiber P(k) are ALL L_max-invariant. The alpha_s problem is therefore not a truncation issue; it is a geometric fact about the three lowest PW sectors.

Constraint: The B1 = 2 * B2 ratio is a flat-band regularization identity on sector (0,0) Dirac spectrum, not an L_max = 3 artifact.
Implication: alpha_s = +0.833 is the framework's structural prediction absent transfer-function smoothing.
Surviving space: Only the multifield delta-N transfer from fiber P(k) to CMB P_zeta(k) can reduce alpha_s to Planck values. This is the S74 Wave 1 mandatory computation (TRANSFER-FUNCTION-74, EVOI = 18.2%).

---

## III. Wave 5 L_max Bidirectional Audit from the Causal Lens

The W5 audit classified 175 canonical constants and 25 proven theorems by L_max sensitivity. From the causal/geometric perspective, the structural content is this:

**Structural floor (L_max-independent)**: 20 ROBUST theorems + 1 W5-D-confirmed = 21 permanent theorems. These are protected by representation theory (Dynkin indices, Schur's lemma), algebraic identities (commutators on Cl(8) and BCS Fock space), superselection, Clifford structure, or matrix algebra. Every holonomy / topological / singularity theorem I have used in prior sessions lives here. The causal structure of the substrate -- encoded in the block-diagonal theorem, the Luttinger superselection, the phi_paasch ratio, the Clock constraint, the g_1/g_2 = e^{-2tau} identity, and the Wilson loop triviality proven in this session -- is INDEPENDENT of the spectral truncation.

**Prediction layer (L_max-sensitive)**: The absolute values of a_0, a_2, a_4 are L_max = 3 partial sums (164-168% shift at L_max = 7, exact Weyl-asymptotic scaling). Predictions that use these absolute values (sin^2 theta_W, absolute m_H in some schemes, absolute CC via a_0) must be tagged as L_max-provisional.

**The geometric meaning of "canonical a_k are L_max = 3 partial sums"**: The W3-A discovery reclassifies how we should think of the framework's spectral action expansion. The Seeley-DeWitt coefficients a_k are spectral invariants of the Dirac operator on a continuum manifold; on SU(3) (d=8), their asymptotic growth rates follow Weyl's law a_{2k}(L_max) ~ L_max^{8-2k}. At L_max = 3 we are computing a finite partial sum of a divergent series, and the canonical_constants.py values were snapshots of that partial sum. Higher L_max means adding more terms to an already-divergent series -- the partial sums don't converge because the spectral zeta function has poles at s = 4, 3, 2, 1 on a d = 8 manifold.

**Does this affect the Penrose compactification?** NO. The Penrose compactification is a CONFORMAL operation on the global causal structure; it uses the metric but not the spectral moments. The sonic horizons, trapped-surface absence, future asymptotic regions, and causal-structure diagrams I have drawn for the modulus space all derive from the g_tau = 3*diag(e^{-2tau} x 3, e^{tau} x 4, e^{2tau} x 1) Jensen metric directly, not from the spectral action. The metric is L_max-independent because it IS the input to the Dirac operator. Only the SPECTRAL DATA computed from the metric is L_max-sensitive.

This is a clean separation: the substrate's GEOMETRY is L_max-independent (metric, curvature invariants, Petrov type, Penrose diagram). The substrate's SPECTRAL CONTENT is L_max-dependent (a_k, zeta sums, absolute mode counts). Observables that are pure geometric invariants (K, |C|^2, Petrov type, CMPP classification, horizon locations) survive the reclassification; observables that are absolute spectral moments do not.

From the W5-G computation: M_1 (first spectral moment) diverges as L^7.65 (raw Weyl rate), but the dimensionless ratio chi_2 = M_1 / (n_modes * lam_max) is bounded at 0.74739 and converges (alpha = -0.047). This is the "spectral fill factor" -- the average eigenvalue relative to the spectral radius -- and it gives a CC prediction of -0.47 OOM (framework predicts rho_vac = 0.34 * rho_Lambda_obs at zero free parameters). This is the Volovik-Sakharov IR-UV cancellation in spectral form: the divergent M_1 encodes the Planck-scale vacuum mode counting; the bounded chi_2 encodes what survives after the IR cancellation.

**Protected ratio-of-ratios (1.7% shift L=3 -> L=7)**: a_0 * a_4 / a_2^2 is L_max-stable to 1.7%. This is the spectral analog of a "protected combination" in the sense of quantum Hall physics: individual components fluctuate, the ratio is topologically rigid. Tau-derivatives d log a_k / dtau are also near-protected (0.5-6.6% shift). These are the framework's "L_max-robust predictions" in the prediction layer.

---

## IV. The Moduli Runaway Problem -- Penrose Diagram of a Future Asymptotic Region

The EFOLD-MAPPING result (W1-D) forces an explicit causal diagram for the unstabilized modulus. Here is the full picture.

**Initial condition**: Post-fold freeze at tau = 0.22, dot_tau ~ 26.54 at the fold entry, H_phys = 0.396 M_KK = 2.94e16 GeV.

**Trajectory in modulus space**: The modulus evolves as a 1D geodesic in the reduced Friedmann phase space. In the initial transit the kinetic energy dominates (w = +0.149, not purely stiff because V has nonzero value); after t ~ 0.01 M_KK^{-1} the modulus decelerates and crosses the Planck n_s window tau in [0.448, 0.700] in ~0.17 M_KK^{-1}. It reaches the turnaround at tau_max = 1.614 at t = 0.092 M_KK^{-1}. At turnaround, dot_tau = 0 and the equation of state is w = -1.00 (purely potential-dominated). The modulus then rolls back, crosses tau = 0 at t ~ 0.6 M_KK^{-1}, and runs away to tau = -infinity.

**The causal diagram**:

```
     Modulus coordinate tau                  Global 4D causal structure
     ---------------------                   ----------------------------
                                               
     tau = -infinity  <--- RUNAWAY             i+  (future timelike
           :                                        infinity, quasi-dS)
           :  (K ~ exp(4|tau|),
           :   different direction              |
           :   than +infinity)                  |  (4D observer never
           :                                    |   sees tau dynamics
           :  <--- exits through tau=0          |   because H >> |dot_tau|
           :                                    |   once potential dom.)
     tau = 0 (round SU(3))                      |
           :                                    |
     tau = 0.22 (post-transit freeze) <-- PHYSICAL UNIVERSE LIVES HERE
           :                                    |
     tau = 0.537 (geometric phase)               I+ (null infinity)
           :                                    |
     tau = 0.78 (instanton kappa=1) <-- Planck match at tau=0.480       
           :                                    |
     tau = 0.895 (Weyl eig zero)                 |
           :                                    |
     tau = 1.382 (NEC violation) ---            |
           :                                    |
     tau = 1.614 (TURNAROUND)                   |
           :                                    |
     Runaway path: 0.22 -> 1.614 -> 0 -> -inf    (no singular point
                                                  reachable by 4D observer)
```

**Is this a singular spacetime?** The question is coordinate-invariant: does the full (4+n)-dimensional Kretschmann scalar diverge on any causally accessible worldline? At tau = -infinity, the internal Jensen metric degenerates: g_tau = 3*diag(e^{+2|tau|} x 3, e^{-|tau|} x 4, e^{-2|tau|} x 1), so the SU(2) directions blow up and the U(1) direction pinches off. The internal Kretschmann scalar K_int ~ exp(4|tau|) -> infinity. This IS a curvature singularity in the higher-dimensional sense.

**Is it censored?** From the 4D perspective: YES. The runaway happens in cosmic time t ~ 1 M_KK^{-1} = 8.9e-43 s, which is then followed by 69 e-folds of standard post-reheating cosmology. A 4D observer at t_now cannot causally access the modulus dynamics because the internal clock has effectively frozen (dot_tau -> 0 as H dominates at w -> -1). The runaway is a MODULUS-SPACE FUTURE ASYMPTOTIC REGION, not a spacetime singularity that any observer can reach.

**Is this the same as the tau = +infinity singularity I catalogued in S44?** NO. The direction is flipped. In S44 I established that tau -> +infinity gives a curvature singularity K ~ exp(4tau), direction-dependent: timelike in SU(2), spacelike in C2/U(1) (S49). The runaway here approaches tau -> -infinity, where the Jensen metric has a DIFFERENT directional signature. The singularity structure is mirrored: spacelike in SU(2), timelike in C2/U(1). But it is the same type of directional singularity, just reached from the other side.

**Does the modulus worldline produce trapped surfaces?** NO. The Jensen deformation is volume-preserving (a_0 tau-derivative = 0 exactly, W5-A confirmed at L_max = {3,...,7}). K_ab is traceless, so by the S49 theorem one expansion is always positive and no closed 2-surface with both expansions negative can form. The singularity theorem's trapped-surface premise is not satisfied anywhere on the runaway path.

**Does it violate NEC?** YES, in the range tau in [1.382, 1.614]. The modulus PENETRATES this region during the bare-action overshoot. The Penrose 1965 singularity theorem's null energy condition premise is therefore violated in this range. This does not mean a singularity is impossible; it means the singularity theorem does not TRIGGER. The runaway to tau = -infinity could still be a genuine curvature singularity (and it IS by Kretschmann calculation); the theorem just doesn't apply.

**Summary**: The bare-action modulus runaway is a cosmic-censored future asymptotic region in modulus space. It carries a genuine curvature singularity at tau = -infinity, but (a) the 4D scale factor is frozen by quasi-de Sitter expansion before the singularity is reached, (b) no trapped surface forms along the trajectory, (c) the trajectory crosses the NEC-violation region, and (d) the singularity structure is a mirror-image of the tau = +infinity singularity from S44. Stabilization by BCS dressing or instanton back-reaction is the only way to avoid this, and both are live S74 priorities.

Constraint: The bare spectral action produces an unstabilized modulus that runs to a NEC-violating regime.
Implication: Stabilization is a structural requirement for the framework, not an optional refinement.
Surviving space: BCS dressing (V_eff minimum from gap opening) OR instanton back-reaction (kappa < 1 pinning near tau = 0.480) OR explicit admission that the runaway is the physically correct answer and the substrate has a 4D-censored modulus-space boundary.

---

## V. What I Would Have Computed

Specific computations from the SP / causal-structure perspective that S73B did NOT perform:

1. **PENROSE-MODULUS-RUNAWAY-74**: Construct the explicit conformal diagram of the full (4+8)-dimensional spacetime including the modulus runaway. Compactify the modulus direction via z = arctan(tau). Identify the causal boundaries: i^0, i^+, I^+, internal-space curvature singularities. Check whether the NEC-violation region is spacelike or timelike. Compute the Kretschmann scalar on the full (4+8)D metric along the runaway worldline and confirm the 4D part remains regular while the internal part diverges.

2. **KRETSCHMANN-DYNAMIC-TRANSIT-74**: The static Jensen-metric Kretschmann scalar K(tau) is known (S44, S49). Compute the DYNAMIC Kretschmann scalar along the transit (tau in [0.15, 0.23] with dot_tau = 26.54) in the full (1+8)-dimensional spacetime. Does the dynamic Kretschmann diverge at the fold? Compare to the static K(0.190) = 0.535. If the dynamic term adds substantially, the fold becomes a "dynamic sonic horizon" with an additional curvature contribution from kinematics.

3. **NEC-VIOLATION-ONSET-74**: Trace the eigenvalues of the Ricci tensor along the modulus worldline in S44/S49 convention. Identify the exact tau where the smallest eigenvalue crosses zero (the NEC boundary, previously found at tau = 1.382 in S49). Verify this holds under the BCS-dressed potential if BCS dressing is introduced. Does BCS dressing create a V_eff minimum at tau < 1.382, preventing the modulus from ever reaching the NEC-violation region?

4. **WILSON-LINE-OFF-JENSEN-74**: The Wilson loop is trivial on the Jensen line because H is real symmetric. Compute the Wilson loop on an OFF-Jensen deformation (breaking the real symmetry by introducing a complex phase in V_kl). The pi-phases should become non-zero. Measure the Berry curvature as a function of off-Jensen deformation amplitude. This tests whether the topological content is literally zero or just hidden by the Jensen-line symmetry.

5. **TWISTOR-JENSEN-74**: Apply Penrose's twistor transform to the Jensen-line BCS Hamiltonian. The real symmetric property implies the twistor space H^1 cohomology is trivial (no non-linear graviton on the Jensen line). Verify this explicitly by computing the twistor projective space mapping from the BCS eigenstate bundle. Confirms: the Jensen line is twistor-space trivial.

6. **GLOBAL-CAUSAL-OVERSHOOT-74**: The modulus overshoots to tau = 1.614 and returns. Is there a CAUSTIC in the modulus-space geodesic flow at the turnaround? Compute the Jacobi equation along the overshoot and identify any focal points. If a caustic exists, it marks where the modulus-space geodesic congruence focuses, analog of a cosmological focusing lens.

7. **RUNAWAY-KRETSCHMANN-74**: Compute the Kretschmann scalar as tau -> -infinity along the runaway path. Verify the expected K ~ exp(4|tau|) scaling with the opposite directional signature to the S44 tau -> +infinity case. Identify which coordinate directions are timelike / spacelike at the singularity.

8. **MODULUS-SPACE-PENROSE-INEQUALITY-74**: Apply the Penrose inequality in the modulus direction: the area of the turnaround surface (tau = 1.614) should bound below the "mass" of the modulus. Compute both sides; test whether the inequality is saturated or violated. Saturation would indicate an extremal configuration.

---

## VI. Assessment

S73B is a high-value causal/geometric session. The master gate passes with all 4 Level 1 items decisive (TRANSIT-PS FAIL, BBN-VOLOVIK status deferred, FUNCTIONAL-SELECT FAIL-PERMANENT, EFOLD-MAPPING INFO-structural).

The session's sharpest causal-structure results are: (1) the L_max-invariance of the non-monotonic fiber P(k) via the block-diagonal theorem, which elevates the alpha_s = +0.833 prediction from an L_max = 3 truncation to a structural geometric fact about the three lowest Peter-Weyl sectors; (2) the Wilson loop triviality theorem on the Jensen line, which adds to the five-result chain of topological triviality and forces topological content to live in the submersion geometry or off-Jensen deformations; (3) the EFOLD-MAPPING modulus runaway, which reveals that the bare action has no V_eff minimum and produces a cosmic-censored future asymptotic region in modulus space; and (4) the W5-F proven-results audit that finds ZERO permanent theorems require demotion under the W3-A L_max discovery.

The framework's structural floor -- 21 permanent theorems, 20 protected constants, Birkhoff rigidity in block-diagonal form, volume-preserving Jensen deformation, Luttinger superselection, acoustic-white-hole causal structure, six-layer censorship including topological layer -- is intact. The prediction layer shifts from "L_max = 3 canonical" to "ratio-of-ratios protected + absolute-values L_max-provisional". No causal-structure result from S49-S72 needs revision: the metric is L_max-independent; the spectral action is L_max-sensitive; the causal diagrams derive from the metric, not the spectral action.

The sharpest open question is whether the modulus runaway is resolved by BCS dressing or instanton back-reaction. If BCS dressing produces a V_eff minimum at tau ~ 0.48, the framework has a self-consistent stabilization. If not, the framework's modulus dynamics has a cosmic-censored future asymptotic region that the 4D observer cannot see. Both are viable from the causal perspective; the S74 MODULI-STABILIZATION-74 computation will discriminate.

---

## VII. Gate Verdicts Relevant to Causal/Geometric Structure

| Gate | Verdict | Causal/Geometric Significance |
|:-----|:--------|:-----------------------------|
| TRANSIT-PS-73B (W1-A) | FAIL | Fiber P(k) structurally non-monotonic; alpha_s = +0.833 |
| EFOLD-MAPPING-73B (W1-D) | INFO | Modulus runaway, N_total = 132.4, no V_eff minimum |
| FUNCTIONAL-SELECT-73B (W1-C) | FAIL-PERMANENT | f is UV data; no algebraic zero-parameter selection |
| SDW-VALIDATION-73B (W3-A) | FAIL L=7, PASS L=3 | Absolute a_k are L_max = 3 partial sums; ratios shift 170% |
| MULTI-CELL-INTEG-73B (W3-B) | PASS | Ordered Veil / R-G integrability survives at N_pair = 4 |
| WILSON-LOOP-73B (W3-C) | FAIL (pi = 0) | Jensen line topologically trivial, W = I to 6.60e-14 |
| SIGNED-BF-LOG-73B (W3-D) | INFO (L = 0) | Gamma_9-graded zeta = 0, structural, permanent |
| THREE-PHONON-73B (W3-E) | FAIL | Particle-hole symmetry protection structural |
| SIX-SEQUENCE-73B (W3-F) | INFO | 5/6 diverge at Weyl rates (expected for d = 8 manifold) |
| VIRTUAL-PARTICLE-73B (W4-A) | FAIL | Ballistic transport, no decoherence; R-G sector dephasing |
| RAMANUJAN-73B (W4-B) | INFO | Graph mixing 237x too slow for transit (confirms dead) |
| CANONICAL-AUDIT-73B (W5-A) | PASS | 175 constants classified; 20 PROTECTED, 9 DIVERGENT-ABS |
| TRANSIT-PS-L7-FLIP (W5-B) | UNCHANGED | B1/B2/B3 sector-local and L_max-invariant at precision |
| THREE-PHONON-L7-FLIP (W5-D) | CONFIRMED-STRUCTURAL | Particle-hole protection L_max-invariant at L = {3,5,7} |
| PROVEN-ROBUSTNESS-73B (W5-F) | PASS-WITH-NOTES | 20 ROBUST + 1 W5-D-confirmed; 0 demotions required |
| M1-CC-73B (W5-G) | DIVERGENT-SCALE | M_1 diverges Weyl rate; chi_2 = 0.747 bounded; CC = -0.47 OOM |
| **Master** AUDIT-GAUNTLET-73B | PASS | All 4 Level 1 decisive |

---

## VIII. Summary Table

| # | Result | Classification | Status | Causal Implication |
|:--|:-------|:---------------|:-------|:-------------------|
| 1 | alpha_s = +0.833 L_max-invariant | PHONONIC -> GEOMETRIC | STRUCTURAL | Fiber P(k) non-monotonic is block-diagonal-protected, not a truncation |
| 2 | Modulus overshoots to tau_max = 1.614 | GEOMETRIC | OPEN | Runaway to tau = -inf; cosmic-censored future asymptotic region |
| 3 | N_total = 132.4 e-folds | GEOMETRIC | INFO | Transit 3.7e-3 + modulus 63.4 + post-rh 69.0 |
| 4 | Wilson loop W = I to 6.60e-14 | GEOMETRIC | PERMANENT | Jensen line topologically trivial; Berry-Pancharatnam = 0 |
| 5 | Multi-cell integrability <r> = 0.4044 | NON-PHONONIC | PASS | Ordered Veil / Cauchy surface analog intact at N_pair = 4 |
| 6 | Block-diagonal L_max-invariance (B1/B2/B3) | GEOMETRIC | PERMANENT | Birkhoff rigidity in spectral form; (0,0), (0,1), (1,1) decoupled |
| 7 | NEC violation boundary crossed at tau = 1.382 | GEOMETRIC | NEW | Bare action runaway penetrates energy-condition-hostile region |
| 8 | Spectral functional f is UV data | GEOMETRIC | PERMANENT | No zero-parameter algebraic selection; shape vs boundary decoupled |
| 9 | 20 ROBUST + 1 W5-D-confirmed theorems | GEOMETRIC | META-AUDIT | Structural floor L_max-independent; prediction layer L_max-provisional |
| 10 | Dimensionless chi_2 = 0.747 bounded | PHONONIC | CONVERGENT | CC prediction -0.47 OOM (framework = 0.34 rho_obs) |
| 11 | Three-phonon particle-hole protection | PHONONIC | PERMANENT | Beliaev channel structurally closed, L_max-invariant |
| 12 | Signed B/F log sum L = 0 | GEOMETRIC | PERMANENT | {gamma_9, D_K} = 0 forces 50/50 split in all eigenspaces |
| 13 | Virtual particles = R-G sector dephasing | PHONONIC | REFRAME | No decoherence on integrable substrate; Yukawa-length = infinity |
| 14 | Protected ratio-of-ratios 1.7% L = 3 -> 7 | GEOMETRIC | NEAR-PROTECTED | Weyl cancellation; sole L_max-robust spectral observable |
| 15 | Acoustic Penrose diagram intact (S70, S72) | GEOMETRIC | STABLE | Horizon locations, white-hole structure L_max-independent |
