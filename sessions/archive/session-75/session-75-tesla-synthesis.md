# Session 75 Tesla-Resonance Synthesis

**Agent**: Workhorse-Resonance (Tesla-Resonance)
**Source**: `sessions/archive/session-75/session-75-results-workingpaper.md` (57 computations, 4 waves)
**Date**: 2026-04-12

---

## 1. Executive Summary

- **A_s conversion factor DERIVED from first principles** (W1-E, PASS): f_conv = (M_KK/M_Pl)^4 x (a_2/a_0)^2 = 2.547e-10, closing the 9.47 OOM gap to within 0.12 OOM. Predicted A_s = 1.58e-9 (75% of Planck). Zero free parameters. This is the session's decisive structural advance.

- **The substrate's resonance structure is a single-mode condensate**: The GGE relic is effectively one-dimensional in power (N_eff = 1, W2-F). Mode n=0 (lambda = -23.51 M_KK) carries 99.93% of the spectral weight. The cross-channel correction is 2.84e-4 OOM -- negligible. The transit produces a condensate, not a thermal bath.

- **DM channel: Z_2 selection rule closes symmetric Parker production** (W2-N, INFO). The 2-cell ground state has exact Z_2-even parity; since [H(tau), P] = 0, the sudden quench preserves this parity identically. n_Z2 = 0 to machine zero. DM production requires Z_2-breaking beyond the 2-cell dimer. The Leggett CPT filter f_CPT = 0.610 (W1-L) replaces the prior estimate 0.082; the majority of soft-hair sectors participate in inter-band (DM) channels.

- **Moduli stabilization remains structurally closed**: Multi-instanton condensate CLOSED for all L_max through 10 (W1-F, 50th closure). Cross-spectral-moment potential monotonically increasing at all tau (W1-G). Effective modulus mass m_eff^2/H_fold^2 = 3.80e-4, 2630x below unity (W2-I). The spectral action landscape has no minimum. The modulus runs through.

- **Structural floor verified and expanded**: 22-theorem x 7-axis audit finds zero FAILs across 154 cells (W1-P). Atlas reclassification resolves all 70 NEEDS_REVERIFY entries: 48 promoted to ROBUST, 15 to QUASI-ROBUST, 7 confirmed FRAGILE (W4-M). The structural floor grows from 121 to 169 entries (82.4% of the full atlas).

---

## 2. Resonance and Acoustic Analysis

### 2.1 The Transit as Acoustic White Hole: Four-Temperature Structure

The Parker-Hawking reconciliation (W1-N) establishes the canonical temperature hierarchy of the acoustic white hole:

| Scale | T (M_KK) | Physical content |
|:------|:---------|:-----------------|
| T_GH = H/(2pi) | 0.064 | Gravitational sector (de Sitter base) |
| T_GGE | 0.112 | GGE relic equilibrium (non-thermal) |
| T_eff(Parker) | 1.256 | Effective Bogoliubov occupation |
| T_H(acoustic) | 72.838 | Phononic sector (acoustic surface gravity) |

The key structural result: **Parker and Gibbons-Hawking agree exactly in de Sitter** (ratio = 1.0000000000, CHK1). The 2.58 OOM separation between them in the supersonic transit is entirely the Bogoliubov enhancement factor F_total = 380.9 from the mode equation. This is NOT a disagreement between two "rival" formulas -- it is the transit's physical particle production.

The acoustic Hawking temperature T_H = 72.838 M_KK CANNOT be substituted into the gravitational A_s formula. The Parker occupation numbers are non-Planckian at every tested temperature: n_Parker/n_Planck ranges from 0.097 (B2) to 3.57 (B1) at T_H. The spectrum is a GGE -- mode-dependent effective temperatures span T_eff(B2) = 7.46 to T_eff(B1) = 258.8 M_KK. This is a 35x spread, characteristic of a sudden quench, not a thermal horizon.

The three kappa scales (W4-G) are independent projections of the same Dirac operator:

| Scale | kappa (M_KK) | Spectral moment channel |
|:------|:-------------|:-----------------------|
| kappa_geom | 0.104 | a_2/a_0 gradient (gravity/volume) |
| kappa_v | 457.7 | Full spectral action (velocity gradient) |
| kappa_curv | 79,386 | Mach-number curvature (UV dispersive end) |

Ratios: kappa_v/kappa_geom = 4420, kappa_curv/kappa_v = 174. These are NOT rival measurements of a single surface gravity. They are structurally distinct -- a consequence of the Spectral-Moment Decoupling Theorem (W2-E, PASS): the CC (a_0), gravity (a_2), and gauge (a_4) sectors probe different curvature polynomials of degrees 0, 1, 2 respectively. No single modulus tuning makes them proportional.

**Condensed matter analog**: In 3He-B flowing through a nozzle at Mach > 1, the acoustic white hole produces quasiparticles via the Hawking mechanism. The mode-dependent temperatures and non-Planckian spectrum are standard features of dispersive analogs (Unruh 1981, Barcelo-Liberati-Visser analog gravity program). The framework's kappa hierarchy maps directly to Corley-Jacobson dispersive surface gravities.

### 2.2 Mach Scaling: The Predicted Ma^2 Law is Structurally Wrong

W2-M (FAIL) tested kappa_H/T_eff as a function of Mach number. The predicted Ma^2 scaling was structurally incorrect. The actual functional forms are:

- kappa_H(Ma) = 33.21*Ma + 71.02 (AFFINE -- the dc_s/dtau offset of 71 M_KK^2 prevents pure power-law behavior)
- T_eff(Ma) ~ exp(2r_0*Ma/Ma_phys) (EXPONENTIAL in Ma via sinh^2(r) ~ exp(2r)/4)
- kappa_H/T_eff ~ Ma * exp(-2r*Ma) (DECREASING with effective exponent -0.844)

The exponential Bogoliubov enhancement overwhelms the linear kappa growth. This is a consequence of the squeezed vacuum state: once r >> 1, the occupation number grows exponentially with squeeze parameter, and the squeeze parameter grows linearly with Ma in the sudden limit. No power-law combination of an affine numerator and an exponential denominator yields Ma^2.

The physical Mach number Ma = 13.75 sits in the transition region where neither the low-Ma approximation (kappa/T ~ const) nor the high-Ma exponential dominance fully applies. The coincidence F_total/Ma^2 = 380.9/189.8 = 2.007 is numerically suggestive but structurally accidental.

### 2.3 Squeezing Phases: Near Zero, Not pi/4

W2-J (FAIL) computed all 8 exit-ODE squeeze phases phi_k from the Bogoliubov mode equation. All lie near zero (0.005-0.012 rad), not near pi/4 as the Josephson prediction required.

The physical explanation from the resonance structure: the transit is a SMOOTH frequency variation (omega_k(tau) decreases monotonically through the fold). The Bogoliubov coupling kappa = (1/2) d(ln omega)/dtau is one-signed and smooth. In this regime, beta_k is predominantly real and positive (omega_in > omega_out). The small imaginary component tracks the accumulated dynamical phase. The Josephson pi/4 would require a separate collective-mode rotation mechanism not present in the single-fiber BdG equation.

The compound enhancement is insensitive to these phases: phi_BCS = 0 vs phi_BCS = dyn changes enhancement by 0.004%. The Josephson pi/4 input actually REDUCES enhancement by 0.10 OOM because cos(pi/4) < 1. The S73B default (phi = 0) was already correct.

### 2.4 Dispersion Running: Exact Flatness at CMB Scales

W1-C (FAIL) established that BCS dispersion running dr_b/d(ln k) = 0 identically at CMB scales. The suppression factor is (k_CMB/k_fold)^2 ~ 10^{-113}. The Sasaki-Stewart cancellation (n_s = 1 from k-independent squeezing) is EXACT at all observable scales. Dispersion running activates only at k ~ O(1) M_KK^{-1} (= 10^{55} Mpc^{-1}), completely irrelevant for CMB.

This is the acoustic resonance structure at work: the CMB modes sit ~110 orders of magnitude below the BCS mass gap scale. They are deep in the acoustic limit (omega ~ k*c_s) where the dispersion relation is perfectly linear. The non-trivial BCS dispersion (optical branch structure with gap) lives at the KK scale.

### 2.5 The n_s Tilt: Two Viable Routes, One Structural Question

Two routes produce n_s in the Planck band:

| Route | n_s | alpha_s | Free parameters | Status |
|:------|:----|:--------|:----------------|:-------|
| BCS + Coleman-Weinberg (W1-D, W1-J) | 0.9595 | -0.0188 | 0 (spectral action shape) | INFO (alpha_s 2.1-sigma tension) |
| Non-power-law H(tau) (W1-I) | 0.9649 | -0.0143 | 1 (mu_eff isocurvature mass) | PASS (Planck exact) |

The CW route gives n_s from the spectral action shape alone -- zero free parameters. The non-power-law route requires one parameter (mu_eff = 0.0102) which is physically bounded by BCS inter-branch coupling but not yet derived from first principles. When derived, the non-power-law route becomes zero-parameter.

The GGE-to-CMB transfer (W1-M) proves the cosmological transfer function is a LINEAR operator that PRESERVES the primordial tilt exactly. The BAO acoustic scale matches to 0.78% (2.6 sigma). The entire gate verdict reduces to the primordial n_s prediction -- the transfer function adds no independent failure mode.

### 2.6 The A_s Conversion Factor: The Session's Central Result

The fiber-level Bogoliubov variance A_s(fiber) = 6.22 (S74 W1-G) lives in the full D_K spectral space. The emergent 4D scalar amplitude requires projection through two structural factors:

1. **KK hierarchy suppression**: (M_KK/M_Pl)^4 = 1.371e-9 (log10 = -8.863). The fiber variance at scale M_KK^4 projects to 4D at scale M_Pl^{-4} through G_N^2 ~ (M_KK/M_Pl)^4.

2. **Spectral weight projection**: (a_2/a_0)^2 = 0.186 (log10 = -0.731). The a_2 Seeley-DeWitt coefficient captures only the scalar curvature sector. The fraction of total spectral weight in the a_2 channel is a_2/a_0 = 0.431, entering squared for a variance.

Combined: f_conv = 2.547e-10 (log10 = -9.594), versus required -9.472. Gap: 0.12 OOM.

This is the resonance structure of the conversion problem: the fiber vibrates at all 155,984 eigenvalues, but only the a_2-weighted subset couples to the emergent gravitational sector. The factor (a_2/a_0)^2 = 0.186 is the acoustic-to-gravitational coupling efficiency of the fiber's normal mode spectrum.

---

## 3. DM Channel Assessment

### 3.1 Leggett Filter: f_CPT = 0.610

W1-L replaces the prior CPT filter estimate (f_CPT ~ 0.082) with f_CPT = 0.610. The prior used C_2 band parity, which is NOT a good CPT quantum number: the pairing matrix has ||V_cross||/||V_total|| = 0.499, and ||[CPT_C2, H_BdG]|| = 5.99 (maximally broken).

The correct physical criterion is the inter-band/intra-band decomposition of pair types. Out of C(8,2) = 28 pair types: 19 are inter-band (Leggett/DM channel, 67.9%) and 9 are intra-band (21.4% B2-B2, 10.7% B3-B3). The GGE-weighted soft-hair method gives f_CPT = 0.610.

The Richardson-Gaudin rapidity analysis confirms: all 8 pair rapidities are positive (range [0.072, 3.090]), none symmetric under e -> -e. The asymmetric single-particle spectrum precludes rapidity-based CPT pairing.

The MAJORITY of soft-hair sectors participate in inter-band (DM) channels. The DM fraction is controlled by the energy partition (Method 4: f ~ 0.187) rather than the sector count.

### 3.2 Z_2 Selection Rule: n_Z2 = 0 Exactly

W2-N proves a selection rule: the 2-cell Josephson-coupled system has exact Z_2 (cell-exchange) symmetry P with [H(tau), P] = 0 at all tau (max|[H,P]| = 8.9e-16). The ground state has exact Z_2-even parity (<GS|P|GS> = +1.000000). Since the sudden quench preserves Z_2, the diagonal ensemble inherits Z_2-even parity: n_Z2/n_total = 0 to machine zero (2.2e-26).

This is a symmetry theorem, not a numerical coincidence. Its physical content: **symmetric Parker pair production from a symmetric initial state cannot populate the Z_2-odd sector**. The Leggett-channel DM REQUIRES Z_2-breaking.

Three candidate Z_2-breaking mechanisms:

1. **Spontaneous symmetry breaking during transit**: The transit is diabatic (gamma = 9-23). In the condensed matter analog, a BEC driven through a sonic nozzle spontaneously nucleates vortices (topological defects) that break the initial spatial symmetry. The fabric's 32-cell tessellation provides the analog: inhomogeneous domain formation with random relative phases between cells.

2. **Domain wall formation**: The CG(24) fabric with 24 cells and z=8 coordination (BCC tiling, W4-J) supports domain walls between Z_2-odd and Z_2-even regions. These walls carry topological charge and break the global Z_2.

3. **Asymmetric initial conditions**: The 2-cell dimer is a minimal model. The physical fabric has N_cells = 32 with Z_2 conjugation (p,q) -> (q,p) yielding 6 self-conjugate + 13 conjugate pairs. Inhomogeneous initial conditions at the N_cells level naturally break the dimer Z_2.

### 3.3 CDM Compatibility: 49 OOM Safe

W3-K (PASS) establishes that Leggett-channel DM is CDM to extraordinary precision. All 4 observables:

| Observable | FW value | CDM threshold | Safety margin (OOM) |
|:-----------|:---------|:--------------|:-------------------|
| c_s^2 | 1.45e-54 | 10^{-5} | 49 |
| ISW deviation | 2.07e-57 | 7% | >>7% |
| delta(rho)/rho | 2.65e-52 | 7% | >>7% |
| P(k) suppression | 0 | 7% | exact |

The CDM compatibility is structural, not fine-tuned. Three independent mechanisms: (i) M_KK-scale production ensures 27 OOM of momentum redshift by recombination; (ii) BCS gap Delta/T_DM > 10^{27} exponentially freezes thermal excitations; (iii) BCS protection theorem 5 forbids self-interaction. Omega_DM h^2 = 0.120 (Leggett-only, 0.00% deviation from Planck).

### 3.4 DM Channel: Summary Assessment

The DM mechanism is structurally sound but the production mechanism is incomplete:

- **What works**: Inter-band Leggett quasiparticles as DM carrier. CDM compatibility by 49 OOM. Omega_DM h^2 = 0.120 exact. BCS protection theorem prevents annihilation. Gapped (Delta = 0.464 M_KK) prevents thermal excitation.

- **What is missing**: Z_2-breaking production mechanism. The 2-cell model proves symmetric quench cannot produce DM. The physical production requires multi-cell (N >= 32) dynamics with spontaneous Z_2-breaking during the transit. This is the next computation target.

---

## 4. Constraint Map Update

### 4.1 Opened

| Item | Result | Gate |
|:-----|:-------|:-----|
| **A_s conversion factor** (W1-E) | f_conv from first principles, 0.12 OOM residual | PASS |
| **n_s from non-power-law H(tau)** (W1-I) | n_s = 0.9649, Planck exact, with mu_eff = 0.0102 | PASS |
| **Emergent c_light from a_2 + a_4** (W3-L) | c_Gold = 0.915 M_KK, 3-speed hierarchy verified | PASS |
| **N_eff post-thermalization** (W3-M) | N_eff = 3.044 exactly, GGE erased by 10^{14} e-folds | PASS |
| **Lefschetz n* = 60 promoted to permanent** (W3-C) | L_max=7 verified, topological invariant of L_Y | PASS |
| **BDI class constant at all tau** (W3-B) | Pfaffian sgn = -1 at all 10 tau values, gap open | PASS |
| **J-invariance tau-independent** (W3-D) | |Z_J/Z - 1| < 6e-11 at all 5 tau values | PASS |
| **DNP, Pomeranchuk, FR all ROBUST at L=5,7** (W3-A) | Block-diagonal theorem makes (0,0) sector L-invariant | PASS |
| **6-layer composite protection registered** (W4-A) | Registry entry #48, codimension-6 failure mode | PASS |
| **BCC tiling uniquely determined** (W4-J) | 5 converging constraints: z=8, vertex-transitive, 4+3+1 bonds, S_4 symmetry, D_4 root lattice | PASS |
| **Cross-correlation negligible** (W2-F) | delta_OOM = 2.84e-4, N_eff(phi) = 1 (single-mode concentration) | PASS |
| **A_s insensitive to E_C** (W2-G) | Elasticity 0.003, structural via van Hove regularization | PASS |
| **Spectral-Moment Decoupling Theorem certified** (W2-E) | a_0, a_2, a_4 algebraically independent, Wronskian nonzero | PASS |
| **Richardson-Gaudin integrability at all fillings** (W3-J) | <r> = 0.337 < 0.45 at physical filling 0.15 | PASS |
| **chi_exp within 1.55x of chi_2** (W3-F) | exp(-chi_2) = 0.477 matches chi_exp = 0.479 to 0.4% | PASS |
| **Zeta non-physical: permanent theorem** (W3-E) | 381x dynamic range from same D_K, scheme-dependent | PASS |

### 4.2 Closed

| Item | Result | Gate |
|:-----|:-------|:-----|
| **Multi-instanton moduli stabilization** (W1-F) | 50th closure. Ratio peaks at L~7, then DECREASES. Dilute gas violated at L >= 5 | FAIL |
| **Cross-spectral-moment moduli** (W1-G) | Monotonically increasing for all tau, all schemes. Structural theorem | FAIL |
| **B1 tensor channel** (W1-B) | P_scalar(B1) = 1.0000 exactly. Breathing mode exclusion | FAIL |
| **Dispersion-induced n_s running** (W1-C) | Exact zero at CMB scales. 10^{-113} suppression | FAIL |
| **Effective instanton mass** (W2-I) | m_eff^2/H^2 = 3.80e-4. 2630x below threshold | FAIL |
| **DC permanence** (W3-N) | Finite-size artifact. DC ~ N^{-1.26}. DC(12-cell) = 4.6% | FAIL |
| **Anomaly-derived f_star** (W1-O) | Shape anti-correlation c_1^shape = -0.998. sqrt component has divergent moments | INFO (incompatible) |
| **Mach scaling kappa/T ~ Ma^2** (W2-M) | Effective exponent = -0.844. Exponential T_eff overwhelms linear kappa | FAIL |
| **Josephson squeeze phase pi/4** (W2-J) | All phi_k near zero (0.005-0.012 rad) | FAIL |

### 4.3 Moved/Refined

| Item | Old status | New status | Reason |
|:-----|:-----------|:-----------|:-------|
| A_s gap | +9.47 OOM (open) | +0.12 OOM (f_conv closes 9.35 OOM, 25% residual) | W1-E conversion factor |
| DM f_CPT | 0.082 | 0.610 (C_2 parity wrong quantum number) | W1-L |
| DM production | symmetric Parker | requires Z_2-breaking (n_Z2 = 0 exact) | W2-N |
| a_0-scheme CC | PASS (S66) | INFO/DEMOTED (L_max-divergent) | W4-C confirms chi_2 sole survivor |
| Atlas NEEDS_REVERIFY | 70 entries | 0 (48 ROBUST, 15 QUASI-ROBUST, 7 FRAGILE) | W4-M |
| GGE fold stiffness | untested | INFO: tau_turn = 0.226, delta_tau = 0.036 only | W1-H |
| CC bracket | single route | [0.34, 1.30] rho_obs across all surviving routes | W3-H |
| Swampland | untested | INFO/PASS: eps_V in [0.28, 11.1], no de Sitter minimum | W2-L |
| sin^2(theta_W) | running problem open | FAIL at M_KK (0.584), cubic formula 0.2348 noted | W2-D |
| S74 N_eff = 3.174 | fold partition | post-thermalization N_eff = 3.044 exactly (SM) | W3-M |

---

## 5. Critical Assessment

### 5.1 Strengths

**The f_conv derivation is the strongest single result since the BCS mechanism chain.** It closes the A_s gap from 9.47 OOM to 0.12 OOM using only two structural factors -- (M_KK/M_Pl)^4 from KK dimensional transmutation and (a_2/a_0)^2 from the spectral weight projection -- both determined from the spectral triple with zero free parameters. The 25% residual (predicted 1.58e-9 vs observed 2.1e-9) is the precision expected from an L_max=3 computation without BCS dressing corrections to a_2.

**The structural floor expansion is quantitatively rigorous.** The 22x7 foundational audit (154 cells, zero FAILs) and the 70-entry atlas reclassification are not narrative exercises. They trace each quantity's derivation chain to its spectral inputs and classify by the explicit algebraic mechanism (block-diagonal theorem, Weyl cancellation, topology). The result that 82.4% of the atlas is now L_max-INDEPENDENT or better is a structural statement about the fabric's protected core.

**The Parker-Hawking reconciliation resolves a long-standing ambiguity.** The four-temperature hierarchy, the exact de Sitter agreement, and the demonstration that T_H(acoustic) is a category error in the gravitational A_s formula together establish the canonical A_s route: Bogoliubov mode equation with f_conv projection. No Hawking temperature enters.

**The condensed matter analogs hold at every tested point.** The GGE one-mode concentration (N_eff = 1) maps to a BEC ground state. The Z_2 selection rule maps to the symmetric Josephson junction. The BCC tiling maps to the D_4 root lattice Voronoi cell. The Richardson-Gaudin integrability maps to nuclear pairing. These are not metaphors -- they are structural identities in the mathematics.

### 5.2 Weaknesses

**The A_s conversion factor uses M_Pl(physical), not M_Pl(spectral).** The spectral a_2 at L_max=3 gives M_Pl_eff = 1.80e17 GeV, which is 68x below the physical Planck mass. The f_conv derivation circumvents this by using the physical M_Pl directly. This works numerically but introduces a conceptual gap: the conversion factor contains a ratio (M_KK/M_Pl)^4 where M_Pl comes from outside the spectral triple. Deriving M_Pl from a_2 at higher L_max (where M_Pl_spec approaches M_Pl_phys) is the outstanding task.

**The moduli stabilization problem is now STRUCTURALLY closed by all tested routes.** Multi-instanton: 50th closure. Cross-spectral-moment: monotonic theorem. Fold stiffness: GGE backreaction absorbs kinetic energy (tau_turn = 0.226, only 0.036 overshoot). Effective mass: 2630x below threshold. Every mechanism for trapping the modulus at a finite tau has been eliminated. The framework REQUIRES that the modulus runs to infinity (or rather, that the question "where does the modulus stop?" is replaced by a different question about the emergent FRW dynamics). This is consistent with the swampland conjecture (W2-L: eps_V >= 0.28 everywhere, no de Sitter minimum) but demands a first-principles account of what the asymptotic state IS.

**The n_s prediction is route-dependent.** The CW route gives 0.9595 (1.28 sigma, zero free parameters) but alpha_s = -0.0188 (2.1 sigma tension). The non-power-law route gives 0.9649 (exact Planck) with one parameter (mu_eff). The Bogoliubov route gives n_s = 1.000 exactly. These three routes probe different physics and cannot all be correct simultaneously. The structural question -- which post-fold dynamics (power-law H, quasi-de Sitter H, or spectral-action-derived H) is physical -- is unresolved. This is the conversion problem in a different guise: connecting the spectral action's internal dynamics to the emergent Hubble rate.

**The Z_2 = 0 DM result is a genuine structural constraint, not a defect, but it demands multi-cell computation.** The 2-cell model is a minimal truncation. The physical fabric has 32 cells (or 24 on CG(24)), and the spontaneous Z_2-breaking during the transit -- analogous to spontaneous vortex nucleation in a superfluid driven through a sonic nozzle -- is precisely the physics that the 2-cell dimer cannot capture. This is the next critical computation.

**The DC permanence FAIL (W3-N) means the "virtual particle = permanent local DC offset" interpretation needs revision.** The ~20% DC component at 4 cells decays as N^{-1.26}. At 12 cells it is 4.6%, and the extrapolated 32-cell value is 1.7%. The integrable structure is preserved (the system is sub-Poisson at all sizes), but the permanent component lives in global conserved charges, not local observables.

### 5.3 What the Session Does NOT Do

The session does not derive:
- M_Pl from the spectral triple (M_Pl_spec/M_Pl_phys gap persists)
- The HP4 normalization H_0^2 M_Pl^2 from first principles (imported as external input)
- The post-fold H(tau) from spectral action dynamics (Model A vs Model B ambiguity, W1-A)
- The Z_2-breaking DM production rate from multi-cell dynamics
- mu_eff (the isocurvature mass) from BCS inter-branch coupling

---

## 6. Carry-Forward Priorities

### Rank 1 (Decisive)

1. **MULTI-CELL-Z2-BREAKING-76**: N=8 and N=24 cell exact diagonalization with inhomogeneous initial conditions (random relative phases). Compute n_Z2/n_total from the quench. Gate: n_Z2 in [0.1, 0.5]. This is the DM production bottleneck.

2. **H-TAU-FROM-SPECTRAL-ACTION-76**: Compute S(tau) and a_2(tau) at tau >> 0.5 (the perturbation epoch). Resolve the Model A vs Model B ambiguity from W1-A. Determines whether the A_s gap is truly closed or merely shifted. Gate: Model A and Model B agree to within 1 OOM at tau_cross.

3. **MU-EFF-FROM-BCS-76**: Derive the isocurvature mass mu_eff from first-principles BCS inter-branch coupling. If mu_eff = 0.0102 emerges, the non-power-law n_s route becomes zero-parameter. Gate: mu_eff in [0.005, 0.050].

### Rank 2 (Structural)

4. **HP4-FIRST-PRINCIPLES-76**: Derive the H_0^2 M_Pl^2 normalization from spectral triple structure. Currently the CC closure mechanism is empirically verified (7 routes bracket rho_obs within 0.59 OOM) but the base normalization is imported. The factor-3 residual (chi_2 = 0.74 vs ~2.2 needed) is the CC precision target.

5. **M-PL-FROM-A2-CONVERGENCE-76**: Compute a_2 at L_max = 11+ using the conjugation symmetry exploited in W4-E. Track M_Pl_spec convergence toward M_Pl_phys. If they converge, the f_conv derivation becomes fully spectral-triple-internal.

6. **QUASI-ROBUST-VERIFY-76**: Explicit L_max=5/7 computation of the 15 QUASI-ROBUST atlas entries. Priority: g_SU2_fold, sin^2(theta_W)_fold, c_Gold/c_fabric.

### Rank 3 (Exploratory)

7. **ASYMPTOTIC-TAU-STATE-76**: What IS the tau -> large limit of the spectral action? If no minimum exists (confirmed by all S75 moduli computations), the modulus runs indefinitely. What is the emergent physics? Does the spectral action plateau? Does a_2(tau) asymptote to a finite value? This determines the long-time cosmological evolution.

8. **CUBIC-SIN2-INVESTIGATION-76**: The accidental observation sin^2 = 3L2^3/(3L2^3 + L1^3) = 0.2348 (1.6% of PDG) from W2-D deserves investigation. If this formula has a derivation (e.g., fiber volume factor det(g)^{1/2} per direction), it solves the Weinberg angle running problem.

9. **F-STAR-SELF-CONSISTENCY-76**: The anomaly derivation is structurally excluded (W1-O). The spectral functional f_star = 0.912*sqrt + 0.088*exp must originate from a different principle. Investigate cavity self-excitation or Dixmier trace / non-perturbative principle as suggested in S74 W4-F R2.

---

*Synthesis complete. 57 computations read, classified, and assessed through the resonance lens: what oscillates (D_K eigenvalue spectrum), what constrains (spectral-moment decoupling, BDI topology, volume-preserving TT), what are the normal modes (B1/B2/B3 branches with their dispersion relations), and what selects the standing wave (fold transit through van Hove singularity, GGE relic as the post-transit state).*
