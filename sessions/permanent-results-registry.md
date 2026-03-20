# Permanent Results Registry

## Complete Catalog of Proven Theorems, Closed Mechanisms, Gate Verdicts, and Structural Identities

**Generated**: 2026-02-28
**Source**: 303 session files, 50+ tier0 computation files, knowledge index (10 exploration agents)
**Scope**: Sessions 1–28, Giants G1–G3, tier0-computation, framework files

---

## I. Publishable Standalone Mathematics

These survive regardless of the framework's physical fate. Publishable at JGP/CMP/JMP/PRD level.

| # | Result | Session | Precision | Target |
|:--|:-------|:--------|:----------|:-------|
| 1 | **D_K Block-Diagonality Universality** — D_K exactly block-diagonal in Peter-Weyl for ANY left-invariant metric on ANY compact semisimple Lie group. Three independent proofs (algebraic, representation-theoretic, numerical). | 22b | 8.4e-15 | JGP/CMP |
| 2 | **Spectral Action Monotonicity Theorem** — a_{2k} monotone for k=0,1,2,3. Spectral action monotone under both connections, all smooth cutoffs, all temperatures, all Lambda > 0. Periodic orbit corrections bounded at 10^{-39} (E-3). | 24a+28c | 10^{-39} | JGP/CMP |
| 3 | **Three Algebraic Traps** — F/B = 4/11 (Weyl, fiber dim 44 vs 16), b_1/b_2 = 4/9 (Dynkin index), e/(ac) = 1/16 = 1/dim(spinor) (trace factorization). All from tensor product structure of spectral triple (A,H,D). | 20b, 21c, 22c | Exact algebraic | CMP |
| 4 | **LZ Retraction / Codimension Classification** — BCS transition on compact manifold is codimension-1 bifurcation, not codimension-2 avoided crossing. Landau-Zener inapplicable to BCS. Berry phase = 0 at second-order boundaries by definition. | 28 | Exact | JMP |
| 5 | **Van Hove Zero-Critical-Coupling on Compact Manifolds** — Discrete spectra on compact Riemannian manifolds produce 1D band structures where BCS pairing has no critical coupling threshold. g(omega) ~ 1/sqrt(omega - omega_min). Enhancement 43-51x over flat DOS. | 28c | Exact | CMP/PRL |
| 6 | **Cl(8) Three-Way Bridge** — Berry phase gamma/pi ~ 1, order-one violation hierarchy 2^{1+k/2}, 6/7 NCG axioms — all trace to Spin(8) on C^16. New connection between Berry geometry and NCG axiom structure through Clifford algebra. | 28 | — | JMP |
| 7 | **Berry Curvature Vanishing on Compact Lie Groups** — K_a anti-Hermitian (||K_a + K_a^dag|| < 1.12e-16, structural) implies Berry curvature Omega = 0 identically for ALL eigenstates, ALL sectors, ALL tau. Extends to ANY compact Lie group with left-invariant metric. | 25 | 1.12e-16 | JGP/CMP |
| 8 | **Spectral Bianchi Identity** — Gauge invariance of spectral action under SU(3)_L constrains sector-weighted spectral derivatives: Sum d_{(p,q)} * dV_{(p,q)}/dtau * M_a^{(p,q)} = 0. Analog of nabla_mu G^{mu nu} = 0. | 25 | Theoretical | CMP |
| 9 | **8D Petrov Classification of Jensen-Deformed SU(3)** — Type D at tau=0 (Einstein manifold), algebraically general with 8 distinct eigenvalues at all tau > 0. Stable multiplicity structure {3,4,1,2,4,3,3,8}. | 25 | Machine epsilon | GRG |
| 10 | **Spectral Flow = 0 Theorem** — R_K(tau) >= 12 > 0 for ALL tau >= 0 (proven analytically). Lichnerowicz bound: lambda^2 >= R_K/4 >= 3 > 0. No eigenvalue crosses zero. Eta invariant = 0. Five independent confirmations. | 25 | Exact | JGP |
| 11 | **Grading Theorem** — Tr(gamma_9 * f(D_K^2/Lambda^2)) = 0 identically for all f, all tau. D_K^2 commutes with gamma_9 and Tr(gamma_9) = 0. Confirmed by 8 independent researchers. | 25 | Exact | JMP/CMP |
| 12 | **Perturbative Exhaustion Theorem** — If H1-H5 hold (all verified), F_pert is not the true free energy. True free energy has branch structure F_true = min{F_pert, F_cond}. Transition is first-order (by H3). Barrier is non-perturbative. | 22c L-3 | H1-H5 verified | — |

### Proposed Papers (Einstein E-6, Session 24b)

- **Pure math**: "Spectral Anatomy of D_K on Jensen-Deformed SU(3): Block-Diagonality, Selection Rules, and Algebraic Traps" — JGP or CMP
- **No-go**: "Spectral action potential on Jensen-deformed SU(3) is monotonically increasing for all cutoff parameters rho > 0" — PRD or JHEP

---

## II. Machine-Epsilon Verified Infrastructure

| Result | Count | Precision | Session | Script |
|:-------|:------|:----------|:--------|:-------|
| KO-dim = 6 mod 8 (parameter-free) | 10 checks | < 1e-15 | 7-8 | `branching_computation_32dim.py` |
| SM quantum numbers from Psi_+ = C^16 | 6 multiplets | Exact | 7 | `branching_computation.py` |
| J^2 = +I (epsilon = +1) | — | < 1e-15 | 8 | `branching_computation_32dim.py` |
| J*rho = rho*J (epsilon' = +1) | — | < 1e-15 | 8 | `branching_computation_32dim.py` |
| J*gamma = -gamma*J (epsilon'' = -1) | — | < 1e-15 | 8 | `branching_computation_32dim.py` |
| [J, D_K(tau)] = 0 (CPT hardwired) | 79,968 pairs | max 3.29e-13 | 17a | `d1_d3_j_compatibility.py` |
| g_1/g_2 = e^{-2tau} structural identity | Derived | Exact | 17a B-1 | `gauge_coupling_derivation.py` |
| Baptista geometry checks | 67/67 | Machine epsilon | 17b | `b2_baptista_verification.py` |
| D_K correctness audit | 39/39 | Exact zeros | 17b | `b3_dk_correctness_audit.py` |
| Riemann tensor R_{abcd}(tau) | 147/147 | Machine epsilon | 20a | `r20a_riemann_tensor.py` |
| Volume-preserving TT-deformation | det = 1.000000000 | Exact | 12 | `tier1_dirac_spectrum.py` |
| 4 curvature invariants (analytic) | Exact formulas | Rational coefficients | 17b | `sp2_analytic_derivation.py` |
| Dirac pipeline (8 validations) | All < 10^{-10} | Machine epsilon | 12 | `tier1_dirac_spectrum.py` |
| AZ class BDI, T^2 = +1 | — | Exact | 17c | `d4_bdg_classification.py` |
| lambda^2 = n/36 algebraic spectrum | 16 integers | Exact algebraic | 12 | `tier1_dirac_spectrum.py` |
| Pfaffian Z_2 = +1 throughout | 100+ tau | Binary | 17c | `d2_pfaffian_computation.py` |
| Gauss-Bonnet chi(SU(3)) = 0 | 21 tau | 1.24e-15 | 21c | — |
| TT stability: no tachyons | all tau in [0,2] | Positive | 20b | `l20_lichnerowicz.py` |
| Lichnerowicz code audit | 10 modules, 8/8 | Zero bugs | 20b | `l20_lichnerowicz.py` |
| D_can = M_Lie identity | — | C1=0.00e+00, C2=0.00e+00, C3=1.11e-16 | 27 | — |
| Spectral pairing lambda <-> -lambda | — | 5.5e-15 | 26 | — |

---

## III. Four Curvature Invariants (Exact Analytic, Session 17b)

All verified at machine epsilon (< 10^{-15}) across 51 tau-values. Rational coefficients.

**Scalar curvature:**
R(tau) = -(1/4)e^{-4tau} + 2e^{-tau} - 1/4 + (1/2)e^{2tau}; R(0) = 2

**Ricci squared:**
|Ric|^2(tau) = (1/12)e^{-8tau} - (1/2)e^{-5tau} + (1/8)e^{-4tau} + (13/12)e^{-2tau} - (1/2)e^{-tau} + 1/8 + (1/12)e^{4tau}

**Kretschner scalar:**
K(tau) = (23/96)e^{-8tau} - e^{-5tau} + (5/16)e^{-4tau} + (11/6)e^{-2tau} - (3/2)e^{-tau} + 17/32 + (1/12)e^{4tau}

**Weyl squared:**
|C|^2(tau) = (377/2016)e^{-8tau} - (5/7)e^{-5tau} + (79/336)e^{-4tau} + (325/252)e^{-2tau} - (17/14)e^{-tau} + 101/224 + (2/21)e^{tau} - (1/84)e^{2tau} + (5/126)e^{4tau}

---

## IV. Four Structural Walls

All 21 closed mechanisms are blocked by one or more of these walls.

| Wall | Name | Content | Scope |
|:-----|:-----|:--------|:------|
| W1 | Weyl Asymptotic F/B Ratio | F/B = 4/11 (fiber dim bosonic 44 vs fermionic 16). Tau-independent. | UV, tau-independent |
| W2 | Peter-Weyl Block-Diagonality | D_K exactly block-diagonal for ANY left-invariant metric on compact Lie group | Exact, 8.4e-15 |
| W3 | Spectral Gap at mu = 0 | lambda_min > 0 prevents spontaneous BCS (no Fermi surface) | Exact |
| W4 | Spectral Action Monotonicity | Tr f(D^2/Lambda^2) monotone in tau, both connections, all cutoffs, all T | Exact to 10^{-39} |

Additional walls from Session 25:

| Wall | Name | Content |
|:-----|:-----|:--------|
| W5 | Berry Curvature Vanishing | K_a anti-Hermitian => Berry curvature = 0 identically. Closes all topological mechanisms. |
| W6 | Thermodynamic Stabilization | Smooth functional trap + Matsubara stiffening. Closes GSL, Shannon, random NCG. |

---

## V. Closed Mechanisms (21 Total)

| # | Mechanism | Session | Closure Reason | Wall |
|:--|:----------|:--------|:---------------|:-----|
| 1 | V_tree minimum | 17a SP-4 | Monotonically decreasing; V'''(0) = -7.2 | W4 |
| 2 | 1-loop Coleman-Weinberg | 18 | Monotonic; F/B = 8.4:1 (Trap 1) | W1 |
| 3 | Casimir scalar + vector | 19d D-1 | Constant-ratio trap; R = 9.92:1 | W1 |
| 4 | Spectral back-reaction (scal+vec) | 19d | Same sign as V_CW; reinforces runaway | W1 |
| 5 | Fermion condensate (Banks-Casher) | 19a S-4 | Gap > 0.818 always; algebraically forbidden | W3 |
| 6 | D_K Pfaffian Z_2 transition | 17c D-2 | Z_2 = +1 throughout; no sign change | — |
| 7 | NCG spectral action (Seeley-DeWitt) | 20a SD-1 | da_2/dtau > 0 AND da_4/dtau > 0; structural | W4 |
| 8 | Casimir with TT 2-tensors | 20b L-3/L-4 | Constant-ratio trap; F/B = 0.55; monotonic | W1 |
| 9 | Single-field slow-roll | 19b R-1 | epsilon ~ 2.1 >> 1 everywhere | W4 |
| 10 | Connes 8-cutoff positive sums | 21a | All monotonic; AM-GM proof | W4 |
| 11 | V''_total spinodal | 21a Landau | V'' > 0 everywhere; exponentially convex | W4 |
| 12 | S_signed gauge-threshold | 21c | Monotonic; Delta_b < 0 algebraic (Trap 2) | W1 |
| 13 | Coupled delta_T crossing | 22b PB-3 | Block-diagonal exactly; C_{nm} = 0 | W2 |
| 14 | Coupled V_IR minimum | 22b PB-2 | Block-diagonal exactly | W2 |
| 15 | Higgs-sigma portal | 22c C-1 | Exactly constant (Trap 3); e/(ac) = 1/16 | W1 |
| 16 | Rolling modulus quintessence | 22d E-3 | Clock closure; 15,000x violation | — |
| 17 | Kosmann-BCS condensate (mu=0) | 23a K-1e | M_max 6.5-12.9x below threshold | W3 |
| 18 | Gap-edge self-coupling | 23a | V(gap,gap) = 0 EXACTLY (selection rule) | W3 |
| 19 | V_spec(tau; rho) monotone | 24a V-1 | Monotonically increasing ALL rho; a_4/a_2 = 1000:1 | W4 |
| 20 | BCS cooling trajectories | 26 P2 | 184/184 trajectories fail; timescale separation | — |
| 21 | Kerner bridge (a_4 truncation) | 26 P3 | a_6 destroys minimum; zero minima for sigma >= 0 | W4 |

### Wall Attribution Summary

| Wall | Closures | Sessions |
|:-----|:---------|:---------|
| W4 (Spectral action monotonicity) | 9-10 | 17a, 20a, 21a, 24a, 26 |
| W1 (Weyl asymptotic F/B) | 6-7 | 18, 19d, 20b, 21c, 22c |
| W2 (Block-diagonality) | 4 | 22b, 22c, 25 |
| W3 (Spectral gap) | 3 | 19a, 23a |

### Sagan Correlation Correction (Session 25 Redux)

21 mechanisms group into only 4 independent structural topics:
- **Topic A**: Perturbative potential (10 mechanisms, 1 root cause — W1/W4)
- **Topic B**: Inter-sector coupling (4 mechanisms, 1 root cause — W2)
- **Topic C**: BCS at mu=0 (3 mechanisms, 1 root cause — W3)
- **Topic D**: Rolling modulus (1 mechanism, 1 root cause — clock)

---

## VI. Gate Verdicts (Complete Battery)

### PASS Gates

| Gate | Result | Key Number | Session |
|:-----|:-------|:-----------|:--------|
| KC-1 | Bogoliubov injection | B_k(gap) = 0.023, Gamma = 29,643 | 28a |
| KC-2 | Phonon T-matrix | W/Gamma = 0.52, max|T| = 4.71 | 28c |
| KC-4 | Luttinger K < 1 | K < 1 in 21/24 combinations | 28c |
| KC-5 | BCS Van Hove | Delta/lambda_min = 0.84, 43-51x enhancement | 28c |
| L-9 | First-order BCS | c = 0.006-0.007 in (3,0)/(0,3) | 28b |
| S-3 | BCS Hessian | 3 genuine minima, lambda_1, lambda_2 > 0 | 28b |
| T-1 | Torsion gap | gap weakened 33-78%, K = -Gamma_LC exactly | 27 |
| K-0 | Kosmann nonzero | ||K_a|| = 0.77-1.76 | 23a |
| T''(0) | Sign gate | T''(0) = +7,969 (POSITIVE) | 21c |
| B-2 | Baptista geometry | 24/24 PASS | 17b |
| B-3 | D_K audit | 39/39 PASS | 17b |
| EDE | Omega_tau bound | 1.6e-3 << 0.02 threshold | 22d |

### CLOSED Gates

| Gate | Result | Session |
|:-----|:-------|:--------|
| V-1 | V_spec monotone, ALL rho | 24a |
| K-1e | BCS mu=0 decisive | 23a |
| L-1 | Thermal spectral action | 28a |
| C-1 | S_can monotone (torsion-independent) | 28a |
| D-1 | Casimir scalar+vector | 19d |
| SD-1 | Seeley-DeWitt a_2/a_4 | 20a |
| PB-2 | Coupled V_IR | 22b |
| PB-3 | Coupled delta_T | 22b |

### FAIL Gates

| Gate | Result | Session |
|:-----|:-------|:--------|
| V-3 | No minimum at any tau | 24a |
| R-1 | Neutrino R ~ 10^14 / 5.68 (gate [17,66]) | 24a |
| C-3 | Order-one norm = 3.117 | 28b |
| C-6 | 6/7 NCG axioms (axiom 5 fails at 4.000) | 28c |
| L-8 | Sector convergence 482% (threshold 10%) | 28c |

### CONDITIONAL (The Decisive Gate)

| Gate | Result | Session |
|:-----|:-------|:--------|
| **KC-3** | Steady-state mu_eff: validated at tau <= 0.35, required at tau >= 0.50 | 28c |

**Closure-to-pass ratio: 10:1** (Session 28c extended)

---

## VII. Structural Identities & Exact Constants

| Identity | Value | Session | Source |
|:---------|:------|:--------|:-------|
| g_1/g_2 = e^{-2tau} | Derived from Jensen metric eq 3.71 | 17a B-1 | Structural |
| sin^2(theta_W) = e^{-4tau}/(1+e^{-4tau}) | tau_0 = 0.2994 from experiment | 17a | Structural |
| phi_paasch: m_{(3,0)}/m_{(0,0)} | 1.531580 at tau = 0.15 (0.5 ppm) | 12, 22a QA-4 | Numerical |
| F/B fiber ratio | 16/44 → ~0.55 spectral-weighted | 20b | Weyl's law |
| b_1/b_2 = 4/9 | Triple confirmed (branching, flux, acoustic) | 21c, 22a, CP-1 | Algebraic |
| e/(ac) = 1/dim(spinor) = 1/16 | Trace factorization | 22c C-1 | Algebraic |
| V(gap,gap) = 0 | Exact selection rule (~10^{-29}) | 23a | Anti-Hermiticity |
| dalpha/alpha = -3.08 * tau_dot | From g_1/g_2 identity | 22d E-3 | Derived |
| a_4/a_2 ~ 985:1 at tau = 0 | Why Starobinsky fails on SU(3) | 24a | Structural |
| Torsion/curvature ratio | 2/3 (tau=0) → 4/3 (tau large) exact | 26 T-2 | Algebraic |
| Bosonic gap (tau=0) | 4/9 = 0.4444 | 21a | Algebraic |
| Fermionic gap (tau=0) | 5/6 = 0.8333 | 21a | Algebraic |
| Gap ratio (tau=0) | 15/8 = 1.875 | 21a | Algebraic |
| chi(SU(3)) | 0 (max |S| = 1.24e-15) | 21c | Topological |
| R_K(0) | 2.000000 (7e-15 error) | 17b | Exact |
| u(1) Ricci eigenvalue | 1/4 for ALL tau | 17b | Geometric invariant |
| |C|^2(0)/K(0) | 5/7 (SU(3) NOT conformally flat) | 17b | Exact rational |
| Jensen metric diagonal | g_tau = 3*diag(e^{2tau}x3, e^{-2tau}x4, e^{tau}) | 17a | Exact |
| V_tree formula | 1 - (1/10)[2e^{2tau} - 1 + 8e^{-tau} - e^{-4tau}] | 17a SP-4 | Bitwise match |
| N_species at Lambda = 1.0 | 104 (SM fermionic DOF = 90, overshoot 16%) | 17 | Computed |
| Spectral gap minimum | 0.8191 at tau = 0.20, sector (0,0) | 19a | Computed |
| NEC violation | tau = 0.778 | 17 SP-3 | Computed |
| a_4_geom(0) | 1970 exactly | 23c | Exact |
| V'''(0) | 1.11e9 | 22c | Computed |
| f(0,0) Pomeranchuk | -4.687 (threshold -3) | 22c F-1 | Computed |
| g*N(0) singlet | 3.24 | 22c | Computed |
| DNP crossing | tau = 0.285 | 22a SP-5 | Computed |
| FR settling time | ~232 Gyr >> universe age | 22d E-1 | Computed |
| Berry curvature peak | B = 982.5 at tau = 0.10 (quantum metric, NOT Berry) | 24a/25 | Erratum |

---

## VIII. Selection Rules (Session 23a, Permanent)

| Pair | Coupling | Precision |
|:-----|:---------|:----------|
| V(Level 1 - Level 1) | 0 exactly | 7.1e-29 |
| V(Level 1 - Level 2) | 0.07-0.13 (grows with tau) | 2 sig figs |
| V(Level 1 - Level 3) | 0 exactly | 1.1e-29 |
| V(Level 2 - Level 2) | 0 exactly | 1.1e-28 |
| V(Level 2 - Level 3) | 0.01-0.03 | 2 sig figs |
| V(Level 3 - Level 3) | 0 exactly | 3.8e-30 |

Level degeneracies in (0,0) singlet: 2, 8, 6 (16 modes total).
Mechanism: Anti-Hermiticity of K_a + orthogonality of degenerate eigenstates.
Extended to ALL 9 sectors (p+q <= 3) in Session 27.

---

## IX. Probability Trajectory

```
Prior (theoretical):                     2-5%
After KO-dim=6 (Sessions 7-8):         10-15%
After SM quantum numbers (Session 7):   25-35%
After Baptista geometry (Session 17b):  40-50%
After Session 19d (TT discovery):       45-52%    <-- PEAK
After Session 20b (TT Casimir closed):  32-40%
After Session 21a (Ainur panel):        43% (panel), 36% (Sagan)
After Session 21c R2:                   38% (panel), 28% (Sagan)
After Session 22a:                      46% (panel), 33% (Sagan)
After Session 22b (block-diagonal):     38% (panel), 27% (Sagan)
After Session 22c:                      44% (panel), 27% (Sagan)
After Session 22d (clock closure):      40% (panel), 27% (Sagan)
=== K-1e DECISIVE CLOSURE (Session 23a) ===
After Session 23a:                       8% (panel),  5% (Sagan)
=== V-1 CLOSED (Session 24a) ===
After Session 24a/24b:                   5% (panel),  3% (Sagan)
After Sagan Redux (Session 25):         12-18% (panel), 8-12% (Sagan)
After Session 26 P1/P2/P3:              3-5% (panel),  2-4% (Sagan)
After Session 27 T-1 PASS:              5-8% (panel),  3-5% (Sagan)
After Session 28 (KC chain):            7-10% (panel), 4-7% (Sagan)
  If KC-3 PASSES:                      12-18% (panel), 8-12% (Sagan)
  If KC-3 FAILS:                        3% (panel),    2-3% (Sagan)
```

---

## X. Corrections & Retractions

| What | Original | Corrected | Session |
|:-----|:---------|:----------|:--------|
| AZ class | DIII (T^2 = -1) | BDI (T^2 = +1) — chiral, not Kramers | 17c |
| "4-5x coupling" | Inter-sector D_K coupling | RETRACTED: was Kosmann norm, not matrix elements | 22b |
| Berry curvature B=982.5 | Berry curvature | ERRATUM: was quantum metric (Provost-Vallee). Berry = 0 exactly (W5). | 25 |
| a_6 "theorem" | All a_{2n} monotone | Downgraded to conjecture beyond a_6. Individual a_0-a_6 proven. | 27 |
| Baptista P_LZ = 0.97 | LZ transition probability | Retracted: LZ inapplicable (codim-1, not codim-2) | 28 |
| phi_paasch status | Physical prediction (BF=5) | Mathematical property (BF=2). Tau mismatch: BCS at 0.35, phi at 0.15. | 28 |
| Tesla g*N(0) ~ 8-10 | Cross-sector modes counted | Corrected to 3.24 by block-diagonality (N=2 singlet only) | 22c |

---

## XI. Session Productivity Ranking

| Rank | Session | Key Permanent Results |
|:-----|:--------|:---------------------|
| 1 | 7-8 | KO-dim=6, SM quantum numbers, commutant structure |
| 2 | 22b | Block-diagonality theorem, b_1/b_2 triple confirmation |
| 3 | 17a | CPT hardwired, g_1/g_2 identity, 79,968 pairs |
| 4 | 22c | Pomeranchuk, Trap 3, Perturbative Exhaustion Theorem |
| 5 | 28 | Fusion: 7 publishable results, 4 walls, KC chain 4/5 PASS |
| 6 | 25 | 5 new closes, 2 new walls (W5/W6), 4 new publishable results |
| 7 | 20a/b | 147/147 Riemann, constant-ratio trap proven |
| 8 | 23a | K-1e Venus moment, selection rules |
| 9 | 17b | 67/67 Baptista, 39/39 D_K audit, 4 curvature invariants |
| 10 | 12 | phi_paasch found, lambda^2 = n/36, TT volume preservation |

---

## XII. Knowledge Index Gaps

Results in Session 28 fusion Section IX NOT yet indexed:
1. LZ Retraction / Codimension Classification
2. Van Hove Zero-Critical-Coupling on Compact Manifolds
3. Cl(8) Three-Way Bridge
4. J-Coherence Across Physical Regimes (five-fold)

Deduplication error: `rolling modulus quintessence` appears in both theorems and closed_mechanisms.

---

## XIII. BCS Constraint Chain Status (Session 28 Final)

| Link | Gate | Result | Key Number | Confidence |
|:-----|:-----|:-------|:-----------|:-----------|
| KC-1 | Bogoliubov injection | **PASS** | B_k(gap) = 0.023, 2.3x above threshold | HIGH |
| KC-2 | Phonon T-matrix | **PASS** | W/Gamma = 0.52, max|T| = 4.71 | MODERATE |
| KC-3 | Steady-state mu_eff | **CONDITIONAL** | Validated at tau <= 0.35; uncomputed at tau >= 0.50 | THE DECISIVE GATE |
| KC-4 | Luttinger K < 1 | **PASS** | K < 1 in 21/24 sector-tau combinations | HIGH |
| KC-5 | BCS gap Delta/lambda_min | **PASS** | 0.84, van Hove 43-51x enhancement | HIGH |

**The framework lives or dies on KC-3.** One computation decides.

---

*Registry compiled from 10 parallel exploration agents searching 303 session files, 50+ tier0-computation files, and the knowledge index. Cross-referenced against Sagan verdicts (canonical authority), fusion synthesis (Session 28), and MEMORY.md.*
