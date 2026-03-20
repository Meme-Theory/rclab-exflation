# Unified Constraint Map — Phonon-Exflation Framework

This is a structured reference table. Query by ID for specific facts.
Do NOT recite constraint counts. Do NOT use the number of entries as an argument.
Each entry defines a boundary of the allowed region: what is proven, what is excluded, what survives.

Last updated: Session 28 (2026-02-27). Fused from 14 specialist constraint maps.

---

## A: Algebraic Constraints (permanent, tau-independent, cannot be evaded)

### A-01: F/B DOF ratio locked (Sessions 20b, 21a)
- **Constraint**: F/B = 16/44 = 4/11 for any positive-definite spectral functional on D_K. Weyl's law. Tensor product structure of (A,H,D).
- **Implication**: No positive spectral sum (Casimir, CW, heat kernel) can produce tau > 0 minimum.
- **Surviving space**: Signed functionals, non-spectral quantities (order parameters, condensates), topological terms.

### A-02: Dynkin embedding ratio locked (Sessions 21c)
- **Constraint**: b_1/b_2 = 4/9 for gauge-threshold corrections in SU(3)->SU(2)xU(1). Polynomial in structure constants.
- **Implication**: Signed gauge-threshold sums cannot produce minimum (ratio tau-independent).
- **Surviving space**: (0,0) singlet (b1=b2=0 escapes), non-perturbative.

### A-03: Trace factorization — Higgs-sigma portal (Session 22c C-1)
- **Constraint**: e/(a*c) = 1/16 = 1/dim(spinor). Exactly constant in tau.
- **Implication**: Portal coupling is tau-independent. No portal-driven stabilization.
- **Surviving space**: Non-trace couplings, momentum-dependent vertices.

### A-04: D_K block-diagonal in Peter-Weyl (Session 22b)
- **Constraint**: C_nm = 0 identically for ANY left-invariant metric on compact Lie group. Three proofs: algebraic, representation-theoretic, numerical (8.4e-15).
- **Implication**: Inter-sector coupling via D_K is exactly zero. Coupled delta_T, coupled V_IR, Stokes phenomenon, avoided crossings between sectors — all closed.
- **Surviving space**: Within-sector dynamics, couplings from non-Dirac sources (gauge fields, condensates, explicit symmetry breaking).

### A-05: S_signed structural identity (Session 21c)
- **Constraint**: Delta_b = -(5/9)*b_2 < 0 for all (p,q). Gauge-weighted signed sums are negative.
- **Implication**: Signed spectral sums (b1-b2 weighted) cannot produce a minimum via sign cancellation.
- **Surviving space**: (0,0) singlet (b1=b2=0), non-perturbative.

### A-06: Perturbative Exhaustion Theorem (Session 22c L-3)
- **Constraint**: H1-H5 verified. F_pert is not a true free energy. All perturbative spectral routes structurally closed by Traps 1-3 (A-01, A-02, A-03).
- **Implication**: ALL perturbative equilibrium mechanisms are closed. This is a theorem, not a search result.
- **Surviving space**: Non-perturbative physics only.

---

## P: Perturbative Potential Constraints

### P-01: V_tree monotone (Session 17a SP-4)
- **Constraint**: Tree-level potential V_tree(tau) monotonically decreasing for all tau >= 0.
- **Implication**: Classical stabilization of tau is impossible.
- **Surviving space**: Quantum corrections, non-perturbative.

### P-02: Coleman-Weinberg monotone (Session 18)
- **Constraint**: 1-loop CW potential monotonically decreasing. F/B = 8.4:1 (fermion-dominated).
- **Implication**: 1-loop radiative corrections reinforce runaway.
- **Surviving space**: Non-perturbative, finite-density.

### P-03: Casimir scalar+vector monotone (Session 19d D-1)
- **Constraint**: Casimir from scalar and vector modes monotone in tau. R = 9.92:1, constant.
- **Implication**: Scalar+vector Casimir cannot stabilize.
- **Surviving space**: TT 2-tensors (subsequently closed by P-04).

### P-04: TT Casimir constant-ratio trap (Session 20b L-3/L-4)
- **Constraint**: F/B = 0.548-0.558 (1.8% variation) including all 741,648 TT DOF. Weyl's law enforces constant ratio.
- **Implication**: ALL perturbative Casimir channels closed. UV structural.
- **Surviving space**: Low-mode (IR) effects where F/B varies 10-37% (N=20-200). Fermions dominate first 14k-25k modes. Gap-edge separation: bos 4/9, ferm 5/6 at tau=0.

### P-05: Seeley-DeWitt a_2/a_4 imbalance (Session 20a SD-1)
- **Constraint**: a_4/a_2 = 1000:1 at tau=0. dim_spinor=16 inflates Gilkey a_4 traces. R^2 dominates R from the start.
- **Implication**: No Starobinsky-type R + R^2 competition on compact positively-curved SU(3).
- **Surviving space**: Different geometry (negative curvature), non-spectral-action functionals.

### P-06: Spectral back-reaction monotone (Session 19d)
- **Constraint**: Back-reaction from scalar+vector modes monotone.
- **Implication**: Self-consistent spectral back-reaction cannot stabilize.
- **Surviving space**: Non-perturbative.

### P-07: Fermion condensate insufficient (Session 19a S-4)
- **Constraint**: Fermion condensate (bilinear) does not produce stabilizing potential.
- **Implication**: Bilinear fermionic channels closed.
- **Surviving space**: BCS (4-fermion, not bilinear), finite-density.

### P-08: V'' > 0 everywhere — no spinodal (Session 21a Landau)
- **Constraint**: Second derivative of perturbative potential positive at all tau.
- **Implication**: No spinodal decomposition. First-order transition requires non-perturbative barrier.
- **Surviving space**: Non-perturbative barrier (instantons, BCS condensate energy).

### P-09: Positive spectral sums all monotonic (Session 21a Connes 8-cutoff)
- **Constraint**: Every positive-definite spectral sum tested (8 cutoff shapes) is monotone. AM-GM inequality proof.
- **Implication**: No positive spectral functional can stabilize tau.
- **Surviving space**: Signed sums, non-spectral functionals.

### P-10: Single-field slow-roll excluded (Session 19b R-1)
- **Constraint**: Slow-roll conditions not met for tau as inflaton.
- **Implication**: No standard single-field inflation from modulus.
- **Surviving space**: Multi-field, non-perturbative tunneling.

### P-11: a_6 also monotone (Session 26 P3)
- **Constraint**: a_6_raw(tau) monotonically increasing, same as a_4. In physical regime (sigma >= 0), V_spec^(6) monotone.
- **Implication**: Including next-order Seeley-DeWitt does not help.
- **Surviving space**: Unphysical sigma (negative f_{-2}), sharp cutoff, non-spectral-action.

---

## S: Spectral Action Constraints

### S-01: V_spec monotonically increasing for all cutoffs (Session 24a V-1)
- **Constraint**: V_spec(tau; rho) monotonically increasing for all rho in [0.001, 0.5]. Both D_K and D_can.
- **Implication**: Spectral action potential cannot stabilize tau. Round metric is global minimum.
- **Surviving space**: Non-spectral-action functionals (condensate free energy, order parameters).

### S-02: S_can monotone — torsion does not help (Session 28 C-1)
- **Constraint**: Canonical spectral action with torsion also monotone. Connection-independent on SU(3).
- **Implication**: Neither Levi-Civita nor canonical connection's spectral action stabilizes.
- **Surviving space**: Torsionful corrections to OTHER functionals, BCS energy.

### S-03: Thermal spectral action monotone at all T (Session 28 L-1)
- **Constraint**: Finite-temperature spectral action monotone at all temperatures tested.
- **Implication**: Thermal population does not create stabilizing minimum. Matsubara stiffening.
- **Surviving space**: Non-thermal injection (Parker parametric, BCS condensation). L-1 does not constrain BCS at non-thermal distributions.

### S-04: Periodic orbit corrections negligible (Session 28 E-3)
- **Constraint**: Non-perturbative corrections to Seeley-DeWitt expansion suppressed by factor 10^{-39}.
- **Implication**: SD expansion is exact for all practical purposes. No oscillatory corrections rescue a minimum.
- **Surviving space**: None within spectral action framework. This constraint is total.

### S-05: Smooth-vs-sharp dichotomy (Session 25)
- **Constraint**: ALL smooth-cutoff spectral functionals are monotone (W1+W4). Sharp-cutoff functionals are not.
- **Implication**: The structural distinction determining which avenues remain.
- **Surviving space**: Gap-edge BEC (partition function minimum at 12.1% depth, beta->inf), sharp-cutoff constructions.

### S-06: f-dependence in spectral action ratio (Session 28)
- **Constraint**: beta/alpha contains free parameter f_4/(f_8*Lambda^4).
- **Implication**: Zero-parameter prediction (P2a) from spectral action is not achievable.
- **Surviving space**: f as modulus of theory, or additional principle to fix f. P2b (finite-density) remains open.

---

## B: BCS / Condensate Constraints

### B-01: BCS at mu=0 subcritical (Session 23a K-1e)
- **Constraint**: BdG M_max = 0.077-0.149, needs > 1.0. Factor 7-13x below threshold. Spectral gap 2*lambda_min = 1.644 prevents Cooper pairing.
- **Implication**: BCS condensation impossible at zero chemical potential. No Fermi surface.
- **Surviving space**: Finite-density (mu != 0). Van Hove singularity enhancement (43-51x, KC-5).

### B-02: Gap-edge self-coupling zero (Session 23a)
- **Constraint**: V(gap,gap) = 0 exactly. Selection rule (anti-Hermiticity of K_a), not numerical accident.
- **Implication**: 2-mode BCS at gap edge has zero pairing interaction.
- **Surviving space**: Multi-mode BCS, nearest-neighbor coupling (V=0.093 at tau=0.30). Van Hove BCS shows Delta/lambda_min = 0.84 with ANY V > 0.

### B-03: Torsionful BCS at mu=0 still subcritical (Session 28)
- **Constraint**: M_max(mu=0, D_can) = 0.529. Still 1.9x below threshold.
- **Implication**: Torsion enhances (4.83x over D_K) but does not reach criticality at mu=0.
- **Surviving space**: Finite mu, backreaction self-consistency, Gaussian fluctuation corrections (xi/r_inj ~ 0.51).

### B-04: F_cond reinforces tau=0 (Session 26 P-1)
- **Constraint**: BCS condensation free energy F_cond most negative at tau=0 (round metric). Local MAX at tau~0.20. F_cond 500x larger than V_spec barrier.
- **Implication**: BCS condensation EXISTS at finite mu (M_max = 6.3-9.7, Delta = 0.17-0.28) but DESTABILIZES any tau != 0 minimum.
- **Surviving space**: Multi-sector condensation, cooling trajectory at high mu, tau=0 as physical vacuum.

### B-05: g*Delta^2 too small (Session 26 P-1)
- **Constraint**: g*Delta^2 = 0.008-0.010. 11-13x below bound-state threshold (0.109), 5000x below cosmological stability.
- **Implication**: BCS condensate too weak to create bound state in modulus potential.
- **Surviving space**: Stronger pairing from multi-sector or density-enhanced mechanisms.

### B-06: BCS transition is second-order (Session 26 P-1)
- **Constraint**: Ginzburg-Landau b = +0.41 (positive). Transition is second-order.
- **Implication**: Hawking-Page first-order analogy does not hold for standard BCS.
- **Surviving space**: L-9 cubic invariant in (3,0)/(0,3) produces first-order. Non-BCS transitions.

### B-07: Sector convergence failure (Session 28 L-8)
- **Constraint**: 482% variation between sectors at current truncation (p+q <= 6).
- **Implication**: Raw Peter-Weyl sum for BCS free energy does not converge. Absolute values unreliable.
- **Surviving space**: Minimum LOCATION at tau=0.35 is stable. NCG-regularized BCS needed for quantitative claims.

### B-08: BCS Berry phase not quantized (Session 28 S-4)
- **Constraint**: gamma/pi = 0.33-0.52. Smooth crossovers, not topological transitions.
- **Implication**: No topological protection of BCS condensate via Berry phase.
- **Surviving space**: Dynamical protection (first-order L-9, metastable supercooling + nucleation).

### B-09: P2 cooling trajectory — 0/184 locked (Session 26 P2)
- **Constraint**: 184 trajectories, 0 locked. Timescale separation: tau settles before mu enters BCS window.
- **Implication**: Dynamical BCS locking via cosmological cooling trajectory does not occur with Kosmann spectrum.
- **Surviving space**: Torsionful spectrum, modified initial conditions, non-cosmological mu source.

---

## D: Dynamical Constraints

### D-01: Clock constraint — rolling modulus closed (Session 22d E-3)
- **Constraint**: dalpha/alpha = -3.08 * tau_dot. Any rolling produces 15,000x violation of alpha-variation bounds.
- **Implication**: tau cannot roll continuously at any cosmologically relevant rate. Quintessence closed. DESI-compatible dynamical DE closed.
- **Surviving space**: tau frozen by phase transition. First-order jump only. w = -1 exact.

### D-02: FR potential too shallow (Session 22d E-1)
- **Constraint**: Settling time ~232 Gyr >> universe age.
- **Implication**: Classical rolling cannot reach any minimum in cosmic time.
- **Surviving space**: Quantum tunneling, first-order phase transition.

### D-03: DNP instability (Session 22a SP-5)
- **Constraint**: lambda_L/m^2 < 3 for tau in [0, 0.285]. Round metric is TT-unstable.
- **Implication**: tau=0 is NOT a stable equilibrium. Deformation away from round metric is dynamically favored.
- **Surviving space**: FAVORABLE — system naturally moves away from round metric. But requires a non-perturbative mechanism to STOP it at some tau > 0.

### D-04: LZ formula inapplicable (Session 28d)
- **Constraint**: Codimension mismatch — Landau-Zener requires codim-2 (avoided crossing), BCS phase boundary is codim-1.
- **Implication**: Landau-Zener survival calculation at BCS phase boundary is mathematically invalid.
- **Surviving space**: Nucleation kinetics (Arrhenius, first-order only).

---

## N: NCG Axiom Constraints

### N-01: Order-one condition failure for D_K (Session 28b)
- **Constraint**: [[D_K, a], b^o] != 0. Max violation 3.897. Factor-pair hierarchy: (H,H)=4.000, (C,H)=2.828, (C,C)=2.000. (0,0) singlet passes trivially.
- **Implication**: 12D product triple does NOT satisfy NCG Axiom 5 (first-order condition). Not a strict Connes spectral triple.
- **Surviving space**: Unitary rotation U in U(16), graded relaxation, twisted spectral triples, accept as Kerner-type KK with 6/7 NCG features.

### N-02: Order-one condition failure for D_can (Session 28b C-3)
- **Constraint**: [[D_can, a], b^o] != 0. Max violation 3.117. Purely Clifford, tau-independent.
- **Implication**: Torsionful connection does not cure order-one. Violation is structural.
- **Surviving space**: Same as N-01. 20% smaller violation but still O(1).

### N-03: 6/7 NCG axioms pass (Session 28c C-6)
- **Constraint**: 12D product triple passes KO-dim, regularity, finiteness, reality, orientability, Poincare duality. Only Axiom 5 fails.
- **Implication**: Construction is "almost NCG." The single failure is order-one.
- **Surviving space**: If order-one can be circumvented, full NCG axiomatics are recovered.

---

## T: Topological / Structural Constraints

### T-01: Pfaffian Z_2 trivial (Session 17c D-2)
- **Constraint**: Z_2 = +1 for all tau. Spectral gap never closes. Pfaffian sign constant.
- **Implication**: No topological phase transition in D_K. No Majorana zero modes from geometry.
- **Surviving space**: D_total = D_K + D_F (Yukawa may change topology).

### T-02: Berry curvature = 0 identically (Session 25 W5)
- **Constraint**: True Berry curvature Omega = 0. B=982.5 is quantum metric, not Berry curvature.
- **Implication**: No Berry-phase-driven stabilization. No holonomy. Island formula closed.
- **Surviving space**: May not hold at finite density (BCS breaks isometry group).

### T-03: Chern numbers = 0 (Session 25)
- **Constraint**: Chern numbers vanish.
- **Implication**: No Chern-number-based stabilization.
- **Surviving space**: Non-topological mechanisms.

### T-04: Fubini-Study distance = 0 for all tau > 0 (Session 25)
- **Constraint**: Eigenvectors do not rotate with tau.
- **Implication**: Eigenvector rotation effects absent. Eigenvalue-only physics.
- **Surviving space**: Eigenvalue-based mechanisms.

### T-05: Fermion determinant monotonically increasing (Session 25)
- **Constraint**: det(D) is monotone in tau.
- **Implication**: No det(D)-based stabilization.
- **Surviving space**: Beyond single-operator determinant.

### T-06: Stokes phenomenon absent (Session 22c)
- **Constraint**: Block-diagonality (A-04) implies exact crossings, not avoided crossings.
- **Implication**: No Stokes-type non-perturbative contribution at level crossings.
- **Surviving space**: Effects in torsionful (D_can) spectrum where crossings may be avoided.

---

## TH: Thermodynamic / Entropy Constraints

### TH-01: GSL anti-selects tau != 0 (Session 25 H-2)
- **Constraint**: S_spec monotonically decreasing at all T. tau=0 has HIGHEST spectral entropy.
- **Implication**: Entropy cost of moving to tau != 0 must be paid. Second law says stay at tau=0.
- **Surviving space**: Free energy balance where condensation energy exceeds entropy cost.

### TH-02: Euclidean action no saddle competition (Session 25 H-1)
- **Constraint**: I_E monotonically decreasing for all f, all Lambda. No Hawking-Page transition.
- **Implication**: 3-monopole Hawking-Page scenario falsified. I_E runaway = negative specific heat.
- **Surviving space**: Non-perturbative resolution. BCS condensation.

### TH-03: Global adiabaticity (Session 25 H-3)
- **Constraint**: Adiabaticity parameter epsilon < 0.5 everywhere for smooth tau evolution.
- **Implication**: No cosmological particle creation from smooth modulus evolution.
- **Surviving space**: Gap-edge Bogoliubov (KC-1: B_k = 0.023, non-adiabatic at gap edge). Phase transition (sudden tau change).

### TH-05: Entropy balance SATISFIED (Session 29a)
- **Constraint**: R = dS_particles/|dS_spec| ranges 1.53 to 3.67 at all tau in [0, 0.50]. Minimum R = 1.53 at tau = 0.20. Cumulative Delta S_total > 0 everywhere.
- **Implication**: Ordinary second law is satisfied. Bogoliubov particle creation (sum_k B_k*omega_k*ln(1/B_k)) produces MORE entropy than the spectral entropy loss (Bose-Einstein at T=1.0). No thermodynamic barrier to tau evolution.
- **Surviving space**: All mechanisms permitted. This removes entropy as a potential hard stop.

### TH-06: Bogoliubov spectrum non-thermal (Session 29Ac)
- **Constraint**: T_eff/T_GH = 3.33 at tau = 0.35. R^2 = -0.69 (worse than constant). Ratio grows monotonically from 1.47 (tau=0) to 569 (tau=2.0).
- **Implication**: Particle creation is parametric (Parker), not equilibrium thermal (Gibbons-Hawking). The CMB temperature is NOT T_GH^{internal} redshifted. Claim A (CMB = GH radiation) NOT SUPPORTED in strong form.
- **Surviving space**: Weak form: CMB = surface of BCS phase boundary with T_eff (not T_GH) setting initial bath temperature.

### TH-07: CDL bounce inapplicable — stability by trapping (Session 29Ac)
- **Constraint**: V_total monotonically decreasing. No potential barrier exists. CDL bounce B = 0.016 (tiny barrier on 156K background). Stability by KE/L < 1 (classical trapping) + Arrhenius exp(28) ~ 10^12 (thermal suppression).
- **Implication**: CDL tunneling is not the stability criterion. The BCS well is a dynamical trap (first-order transition + latent heat), not a potential minimum.
- **Surviving space**: Condensate IS stable. The correct criterion is KE < latent heat at first-order transition point.

### TH-04: [V, J] != 0 permanent (Session 26 P-1)
- **Constraint**: Kosmann pairing potential does not commute with angular momentum. ||[V,J]||/||V|| = 0.14-0.30.
- **Implication**: BCS pairing is structurally non-trivial (not a selection-rule accident).
- **Surviving space**: This characterizes pairing nature, not a constraint on mechanisms. Publishable as math result.

---

## O-NU: Neutrino-Specific Constraints

### O-NU-01: R from H_eff ~ 10^14 — Kramers artifact (Session 24a R-1)
- **Constraint**: H_eff = diag(lambda) + V_nm gives R ~ 10^14 due to Kramers degeneracy (BDI, T^2=+1) suppressing splittings to noise.
- **Implication**: Kramers pairing prevents perturbative lifting from producing physical mass splittings.
- **Surviving space**: Kramers-breaking effects, external fields.

### O-NU-02: K_a cross-check R = 5.68 (Session 24a R-1)
- **Constraint**: Antisymmetric Kosmann coupling gives R = 5.68, below [17, 66] gate.
- **Implication**: Kosmann coupling does not reproduce neutrino mass hierarchy ratio.
- **Surviving space**: Mode-dependent BCS, tridiagonal PMNS extraction.

### O-NU-03: R_BCS = R_bare for uniform gap (Session 28)
- **Constraint**: Uniform BCS gap Delta cancels in R ratio identically. R_BCS = R_bare = 5.68.
- **Implication**: Uniform BCS condensation does not modify mass-squared ratio.
- **Surviving space**: Mode-dependent gap (anisotropic pairing). But V_12 > V_23 means gap DECREASES R (wrong direction). Effectively closed.

### O-NU-04: R(tau) = 33 only at tau = 1.556 (Sessions 21c, 22b)
- **Constraint**: Mass-squared ratio passes through 33 only at tau = 1.556, outside physical window [0.15, 1.55], at monopole artifact (width delta_tau ~ 4e-6).
- **Implication**: Block-diagonal intra-sector eigenvalues do not reproduce atmospheric/solar ratio at physical tau.
- **Surviving space**: Mode-dependent BCS gaps, inter-sector generation assignment.

---

## O-PHI: Phi-Specific Constraints

### O-PHI-01: phi^n series absent (Session 14 MC analysis)
- **Constraint**: phi^2, phi^3 have z < 0 (generic, not significant) in consecutive eigenvalue ratios.
- **Implication**: Paasch's geometric mass series does not hold on Jensen-deformed SU(3).
- **Surviving space**: phi^1 as isolated spectral feature at tau=0.15 (5 ppm match, pre-registered).

### O-PHI-02: phi is inter-sector only (Session 24a)
- **Constraint**: Zero phi_paasch crossings in (0,0) singlet. All phi matches are m_{(3,0)}/m_{(0,0)}.
- **Implication**: phi cannot be universal intra-sector mass quantization factor.
- **Surviving space**: Inter-sector ratio at specific tau. Algebraic property of (3,0) vs (0,0) Casimirs.

### O-PHI-03: BCS destroys phi structure (Session 27)
- **Constraint**: exp(-1/M) BCS map sends ratio 1.5316 to gap ratio 64,354 (4.8 orders amplification).
- **Implication**: If physical masses are BCS gaps, phi CANNOT be a direct mass ratio.
- **Surviving space**: Phi lives in algebraic/spectral layer, not condensation layer. Strong-coupling BEC-side preserves ratios but numbers show mixed regime.

### O-PHI-04: phi underrepresented statistically (Session 25 P-1)
- **Constraint**: 512 crossings within 2% of targets, vs 680 expected randomly. Observed/expected = 0.75.
- **Implication**: No statistical excess of Paasch-quantized ratios across full tau range.
- **Surviving space**: Individual match at tau=0.15 (5 ppm) survives trial factor (pre-registered).

### O-PHI-05: phi reclassified as mathematical property (Session 28c)
- **Constraint**: BCS minimum at tau=0.35 gives ratio ~1.455 (5% from phi, outside 1% tolerance).
- **Implication**: phi at tau=0.15 is a mathematical property of D_K spectrum, not a physical prediction. Kepler-without-Newton.
- **Surviving space**: Publishable as pure spectral geometry (Einstein E-6 paper).

---

## O-LSS: Large-Scale Structure / Observational Constraints

### O-LSS-01: P(k) requires bubble nucleation (Session 28 Synthesis B)
- **Constraint**: Smooth BCS transition onto P(k) was structurally incorrect (Hawking correction). Correct mechanism is first-order bubble nucleation.
- **Implication**: P(k) feature shape depends on nucleation rate beta/H, not smooth gap evolution. Quantitative prediction requires backreaction computation.
- **Surviving space**: Prediction chain: drive rate (E-1) -> backreaction (E-2) -> k_transition -> DESI/Euclid test.

### O-LSS-02: S8, bulk flow, void statistics are post hoc (Session 28)
- **Constraint**: Framework has NOT pre-registered quantitative predictions for S8 or bulk flow.
- **Implication**: These cannot be cited as evidential support until a quantitative prediction is stated and tested.
- **Surviving space**: Pre-register specific prediction, then test. Until then: exploratory only.

### O-LSS-03: k_transition = 9.4e23 h/Mpc — UNOBSERVABLE (Session 29Ac)
- **Constraint**: k_transition = a(t_BCS) * H(t_BCS) = 9.39e23 h/Mpc at M_KK = 10^16 GeV. Scales linearly: k ~ M_KK. At ALL physical M_KK values (10^14 to 10^18 GeV), k_transition >> 10^20 h/Mpc. DESI/Euclid range: 0.01-0.3 h/Mpc.
- **Implication**: The BCS transition at GUT epoch imprints features at microscopic scales, 24 orders above observable range. P(k) spectral feature is REAL but UNOBSERVABLE. No M_KK value brings k into survey range.
- **Surviving space**: Secondary later-epoch transition (speculative, not computed). The framework's observational predictions escape current technology.

### O-LSS-04: BAO compatibility gate (Session 29 Plan)
- **Constraint**: If t_BCS falls in recombination window, delta(r_s)/r_s < 0.5% required.
- **Implication**: BCS transition must not significantly alter baryon-photon sound speed.
- **Surviving space**: Dark-sector-only transitions. Sub-0.5% backreaction.

### O-LSS-05: CC problem inherited (Session 28 E-5)
- **Constraint**: Cosmological constant 10^113 orders too large at GUT scale.
- **Implication**: Framework inherits CC problem. Does not solve it.
- **Surviving space**: Known open problem in all frameworks.

---

## O-PREM: Paasch Premise Constraints

### O-PREM-01: Dirac Large Number Hypothesis excluded
- **Constraint**: |G-dot/G| < 7e-13 yr^-1 (LLR). Dirac 1/t requires ~5e-11 yr^-1. Excluded by ~100x.
- **Implication**: Paasch's assumption G(t) ~ 1/t is observationally excluded.
- **Surviving space**: Mathematical structure (mass integers, golden ratio, phi derivation) stands independently.

---

## O-GEN: Generation / Sector Structure Constraints

### O-GEN-01: Z_3 uniform perturbatively (Session 21c)
- **Constraint**: All three triality classes contribute ~1/3 each (0.3324-0.3338) in delta_T.
- **Implication**: No Z_3 symmetry breaking perturbatively. Koide shortcut pushed to Tier 2.
- **Surviving space**: Non-perturbative Z_3 breaking.

### O-GEN-02: Nearest-neighbor selection rules (Session 23a)
- **Constraint**: V(L1,L1)=0, V(L1,L3)=0, V(L2,L2)=0, V(L3,L3)=0. Only V(L1,L2) and V(L2,L3) nonzero.
- **Implication**: Tight-binding nearest-neighbor hopping on eigenvalue ladder. Explains phi^1 survival + phi^n absence.
- **Surviving space**: Anderson localization in spectral domain, 1D tight-binding models.

---

## Structural Theorems (permanent, established, not constraints on mechanisms)

| ID | Statement | Session |
|----|-----------|---------|
| ST-01 | KO-dim = 6 (parameter-free, the SM value) | 7-8 |
| ST-02 | [J, D_K(tau)] = 0 identically: CPT hardwired | 17a |
| ST-03 | {gamma_9, D_K(tau)} = 0: spectral pairing lambda <-> -lambda | 17a |
| ST-04 | AZ class BDI, T^2 = +1, Z invariant = 0 (trivial) | 17c |
| ST-05 | g_1/g_2 = e^{-2tau}: structural identity | 17a |
| ST-06 | Volume-preserving TT-deformation | 12 |
| ST-07 | Riemann tensor 147/147 checks | 20a |
| ST-08 | 67/67 Baptista geometry checks at machine epsilon | 17b |
| ST-09 | phi_paasch: m_{(3,0)}/m_{(0,0)} = 1.531580 at tau=0.15 (5 ppm from phi) | 12, 22a |
| ST-10 | Trans-Planckian universality: Spearman rho >= 0.93 | 25 |
| ST-11 | Z_3 = (p-q) mod 3: exactly 3 generations | 7 |
| ST-12 | Spectral gap never closes: minimum 0.819 at tau=0.20 | 17c |
| ST-13 | Mass ordering: NORMAL (bowtie topology, (0,0) singlet lightest in [0.11, 1.58]) | 21c |
| ST-14 | Lambda_min turnaround at tau=0.23: root cause of ALL non-monotone signals | 21a |

---

## Active Channels (surviving solution space, post-Session 28)

| ID | Mechanism | Status | Key Constraint Survived |
|----|-----------|--------|------------------------|
| AC-01 | Van Hove BCS at finite mu | KC-1/2/4/5 PASS, KC-3 CONDITIONAL | B-01 (43-51x enhancement) |
| AC-02 | First-order BCS via cubic invariant | L-9 nonzero in (3,0)/(0,3) | D-01 (jump, not roll) |
| AC-03 | D_total Pfaffian (D_K + D_F) | NOT YET COMPUTED | T-01 (D_K alone trivial) |
| AC-04 | Torsionful D_can enhancement | 4.83x over D_K | B-03 (still subcritical at mu=0) |
| AC-05 | Finite-density spectral action | B-1 PASS (S26): min at tau=0.15 for rho=0.000510 | S-01 (smooth SA monotone) |
| AC-06 | Free energy comparison F_cond vs F_normal | Not yet computed at finite mu | B-04 (round metric attractor) |
| AC-07 | d(tau)/dt from 12D Einstein equations | Structural gap — not computed | D-01, D-02 |

---

## Unvalidated Gates (pre-registered, awaiting computation)

| Gate | What It Tests | PASS condition | FAIL implication |
|------|--------------|----------------|------------------|
| KC-3 | Scattering at tau >= 0.50 | T-matrix well-defined | Van Hove enhancement invalidated |
| Adiabatic | dtau/dt * d(Delta)/dtau << Delta^2 at tau=0.35 | Ratio << 1 | Adiabatic transport fails |
| V_total | Gradient balance with NCG regularization | Non-monotone V_total | No stabilization even with NP |
| T_eff vs T_BCS | Thermal safety of condensate | T_eff < T_BCS for relevant sectors | Condensate thermally destroyed |
| CDL bounce | CDL tunneling action | B >> 400 | Tunneling cosmologically irrelevant |

---

## Observational Benchmarks (reference values, not arguments)

| Observable | Value | Source |
|:-----------|:------|:-------|
| BAO scale (r_s) | 147.09 +/- 0.26 Mpc | Planck 2018 |
| S8 (Planck) | 0.834 +/- 0.016 | Planck 2018 |
| S8 (weak lensing) | 0.759 +/- 0.024 | KiDS-1000 |
| Bulk flow (100 Mpc/h) | ~250 km/s | kSZ measurements |
| LCDM bulk flow prediction | ~110 km/s (1-sigma) | N-body simulations |
| DESI P(k) precision | sub-percent at k=0.05-0.15 h/Mpc | DESI DR1 |
| k_BAO | ~0.04 h/Mpc | BAO wiggles |
| Neutrino Delta m^2_32/Delta m^2_21 | ~33 (gate: [17, 66]) | PDG |
| ALPHA antihydrogen | 2 ppt on 1S-2S | ALPHA collaboration |
| |G-dot/G| upper bound | 7e-13 yr^-1 | Lunar Laser Ranging |
