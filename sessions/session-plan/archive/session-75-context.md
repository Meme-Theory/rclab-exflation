# Session 75 Context Package: Refinement

**Assembled**: 2026-04-12
**Topic**: Refinement
**Planner**: transit-dynamics-theorist
**Format**: compute (parallel independent agents)

---

## 1. Framework Status (from MEMORY.md)

### PROVEN (16+ results, machine epsilon)
KO-dim=6 | SM quantum numbers | [J,D_K]=0 CPT | g1/g2=e^{-2tau} | 67/67 Baptista | Volume-preserving TT | Riemann 147/147 | TT stability | phi_paasch=1.531580 | AZ class BDI | D_K block-diagonal | Trap 3 | Perturbative Exhaustion | DNP instability | Pomeranchuk | Clock constraint

### Current State
- 25+ CLOSED mechanisms (all perturbative + instanton averaging)
- PARADIGM: Transit physics, not equilibrium. Instanton gas, not potential well
- THE ORDERED VEIL: integrable, not chaotic. GGE relic, never thermalizes
- Mechanism chain UNCONDITIONAL (S35): I-1, RPA, Turing, WALL, BCS all PASS
- Open: FRIEDMANN-BCS-38 (coupled dynamics), A_s gap (+9.47 OOM from S74 W1-G)

### S74 Highlights (84 computations, 4 waves)
- **alpha_s = 0 structural identity** (W1-A + W4-C): H_b^2 cancellation in multifield delta-N, resolves S73B 125-sigma tension
- **A_s gap +9.47 OOM** (W1-G): Bogoliubov-amplitude channel CLOSED; A_s closure requires conversion mechanism
- **Moduli stabilization 0/4** (W1-B): All sub-gates FAIL; perturbative/single-instanton CLOSED; cross-moment and multi-instanton survive
- **Effacement 2.82e-4** (W1-F): 4 OOM below DE floor; local impedance NOT a DE mechanism
- **n_bar triple (315.7, 8.4, 12.2)** (W2-A): B1 acoustic dominates 37x over B2 flat; "flat-band rides longest" refuted
- **Lefschetz n*=60 = N_pair** (W3-N): 10^26665 suppression; candidate 5th structural theorem
- **f_NL = 0.8535** (W4-D): Senatore-Zaldarriaga recovered exactly from c_BLV = 0.4849
- **T_H = 72.838 M_KK** (W3-B): Hawking surface gravity at entry horizon, self-consistent to machine zero
- **Three kappa scales**: kappa_geom=0.104, kappa_v=457.66, kappa_curv=79386 M_KK (definitional, not discrepancy)
- **L_max audit** (W4-W): S66 a_0-scheme CC demoted PASS->INFO; f*-scheme chi_2 sole survivor at -0.47 OOM
- **Omega_k = 0 exact** (W1-H): Block-diagonality of a_2 forces spatial flatness; no inflation needed
- **N_eff = 3.1744** (W4-R): Partition rigidity from (n_b,n_f)=(20,16) under U(2); zero-parameter
- **12 new permanent theorems** (W4-V): Framework at 33x historical hardening rate
- **T_rh = 1.37e10 GeV** (W4-E): Reheating via instanton tunneling; 13 OOM above BBN floor
- **Non-perturbative J-invariance** (W4-H): |Z_J/Z - 1| = 5.8e-11; BCS subspace rigorously closed

---

## 2. EVOI Priority Table (S73B Reset, updated through S74 closures)

### Level 1: CRITICAL (EVOI > 10%)

| ID | Computation | P(pass) | EVOI | Status after S74 |
|:---|:-----------|:--------|:-----|:-----------------|
| N1 | TRANSFER-FUNCTION-74 | 0.45 | 18.2% | **DONE** (W1-A INFO: alpha_s=0, n_s=1.000) |
| N2 | MODULI-STABILIZATION-74 | 0.40 | 12.0% | **DONE** (W1-B FAIL: 0/4 sub-gates) |
| N3 | L-MAX-BIDIRECTIONAL-73B-W5 | 0.30 | 10.5% | **PARTIAL** (W4-W + W4-G audit done; explicit L=5/7 reverify pending) |
| N4 | E_C-RESOLUTION-74 | 0.55 | 10.2% | **DONE** (W1-D: E_C=0.4643 M_KK canonical, Method A) |

### Level 2: HIGH (EVOI 5-10%)

| ID | Computation | Status after S74 |
|:---|:-----------|:-----------------|
| N5 | GGE-TRANSFER-74 | OPEN (not attempted) |
| N6 | SIN2-LR-NORMALIZATION-74 | OPEN |
| N7 | EC-UNIFIED-74 | **DONE** (W1-D three-method split resolved) |
| N8 | CC-M1-REGULARIZATION-74 | **DONE** (W2-Q: Scheme B PASS +0.12 OOM) |
| N9 | INSTANTON-STABILIZATION-74 | **DONE** (W1-B sub-gate a FAIL) |
| N10 | B1-WEIGHT-AUDIT-74 | **DONE** (W4-C: mode/branch P_s identical to 3e-16) |
| N11 | DC-PERMANENCE-74 | OPEN |
| N17 | FRAMEWORK-RESCALE-74 | **DONE** (W4-G: log stable 0.47%, linear 72% drift) |

### Level 3-4: Remaining

| ID | Status |
|:---|:-------|
| N5 GGE-TRANSFER | OPEN |
| N6 SIN2-LR-NORMALIZATION | OPEN |
| N11 DC-PERMANENCE | OPEN |
| N12 DEGENERACY-LIFT | **DONE** (W4-C) |
| N13 GGE-BISPECTRUM | **DONE** (W4-D: f_NL=0.8535 PASS) |
| N14 BAYESIAN-FUNCTIONAL | OPEN (updated: only c=0.126 and pure sqrt survive) |
| N15 MODULUS-DECAY | **DONE** (W4-E: T_rh=1.37e10 GeV PASS) |
| N16 RATIO-OF-RATIOS-PROTECTED | **DONE** (W4-F: 4/20 STRICT R-family) |
| N19 BA-LIFETIME-FABRIC | OPEN |

---

## 3. S74 Gate Verdicts (from transit synthesis + working paper)

| Gate | Verdict | Key Number |
|:-----|:--------|:-----------|
| TRANSFER-FUNCTION-74 | INFO | alpha_s=8.4e-15, n_s=1.000 |
| MODULI-STABILIZATION-74 | FAIL | 0/4 sub-gates |
| A-S-FROM-BOGOLIUBOV-74 | FAIL | +9.47 OOM |
| GGE-PARTITION-74 | FAIL | E_eff/E_total=2.82e-4 |
| NS-1LOOP-SPECTRAL-74 | FAIL | delta_n_s=-0.000389 (wrong direction) |
| BRANCH-NBAR-D-K-74 | INFO | <n_bar>=48.23 |
| PHASE-COVARIANCE-3X3-74 | PASS | delta_OOM=0.1495 |
| HFB-HORIZON-BACKREACTION-74 | FAIL | delta_kappa=0.49% |
| BDI-MORSE-STABILITY-74 | INFO | Morse index 0 in 35D |
| LEFSCHETZ-GAUSSIAN-74 | FAIL (structural PASS) | E_zp/V_CW=0.211 |
| BRANCH-KAPPA-74 | INFO | k^2 fit R^2=1.000 |
| T-ENTRY-D-K-74 | PASS | T_H=72.838 M_KK |
| ENTRY-TH-DERIV-74 | FAIL (route-split) | c_spec kappa=0.104 |
| LEFSCHETZ-MEASURE-74 | PASS | n*=60=N_pair, 10^26665 |
| N12-DEGENERACY-LIFT-74 | PASS | mode/branch identical |
| N13-GGE-BISPECTRUM-74 | PASS | f_NL=0.8535 |
| CC-M1-REGULARIZATION-74 | SPLIT | Scheme A +123 OOM / Scheme B +0.12 OOM |
| FRAMEWORK-RESCALE-74 | FAIL (linear) / PASS (log) | 72%/0.47% |
| JOINT-AUDIT-ATLAS-74 | PASS | 205 entries, 119 L_max-INDEPENDENT |
| SOFT-HAIR-FDM-74 | INFO/PASS(CG24) | R_soft/f_DM=12.15/8.19 |
| LEGGETT-JEANS-74 | PASS | k_J=5.97e-3 Mpc^-1 |
| N-EFF-MORSE-BOTT-74 | PASS | N_eff=3.1744 |
| MOTT-GAP-RENORM-74 | PASS | E_C_today=1.04e-32 eV |
| MODULUS-DECAY-74 | PASS | T_rh=1.37e10 GeV |
| BDSPT-ANOMALY-74 | PASS | |Z_J/Z-1|=5.8e-11 |
| FOUNDATIONAL-AUDIT-75-SPEC | PASS (spec generated) | 22 theorems x 7 axes |

---

## 4. S71 Gate Verdicts (most recent prior gate file)

Key results: DECOHERENCE-BAND-71 PASS (SU(1,1) compound exact), CHIRP-UNIVERSALITY-71 PASS (geometric invariant), THREE-CELL-GSL-71 PASS, BCS-BACKREACTION-a4-71 PASS (delta=2.02e-8), CC-FROM-GGE-RESIDUAL-71 FAIL (110 OOM gap), WEYL-TWO-LOOP-71 FAIL (marginal 0.3%), BH-THIRD-LAW-71 FAIL (category error).

---

## 5. Transit-Dynamics-Theorist Agent Memory Summary

Key sessions: S66 (first engagement, mode equation), S67 (TRANSIT-PS solved, z''/z dominates 2.67x, A_s gap=15 OOM is CONVERSION problem), S68 (acoustic transfer |T|^2=1, alpha_s primordial=0 EXACT, Lizzi-Transit workshop, Landau-Transit workshop), S74 (TGF v2 reframing, narrowed 54 to 7 OOM).

Critical insights carried:
- alpha_s(primordial) = 0 EXACT (Bogoliubov saturation)
- A_s gap is CONVERSION not PRODUCTION
- z''/z pump field dominates by 2.67x
- phi_eff phase (Josephson pi/4) discovered in S68 Landau workshop
- Stochastic dN bounded 0.003-0.015 OOM
- Non-BD initial state contributes ~0.3-0.6 OOM for A_s

---

## 6. Permanent Results Registry Summary

112+ proven mathematical results across S7-S66:
- 12 original (S7-S28): block-diagonality, monotonicity, traps, LZ retraction, van Hove, Cl(8) bridge, Berry vanishing, Bianchi, Petrov, spectral flow, grading, perturbative exhaustion
- 17 additions (S29-S62): structural monotonicity, Lorentzian CMPP, alpha_s=n_s^2-1, Anderson-Higgs impossibility, etc.
- 17 S63 theorems (T1-T17): zero first-order tensor, breathing mode exclusion, scalar-tensor decoupling, etc.
- 18 S64-S66 results: R-monotonicity, Fermi-surface lock, a_0/a_2 trap, frustration triangle, etc.

S74 candidates for promotion: Omega_k=0 structural, non-perturbative J-invariance, Lefschetz measure factorization, three-kappa decomposition, E_C/H alignment, partition rigidity, six-layer composite protection.

---

## Carry-Forward Computations (from structured wrap-ups)

**Sources**: 8 syntheses + 4 workshops from session-74

### Deduplicated Table (90 unique items, grouped by topic)

#### A. A_s Gap Closure (the #1 open problem after W1-G +9.47 OOM FAIL)

| # | Computation | Sources | Priority | Effort |
|:--|:-----------|:--------|:---------|:-------|
| A1 | **H-PHYS-REDUCTION-75**: H_phys reduction by +4.74 OOM at perturbation epoch. Gate: specific mechanism drops H by ~5 OOM fold→CMB | Transit | HIGH | 1 session |
| A2 | **B1-TENSOR-MIXING-75**: Does B1 (r=3.57) route into tensor channel? Removes +1.73 OOM squeeze enhancement. Gate: quantified (p,p)-sector assignment | Transit | HIGH | 1 session |
| A3 | **R-B-K-RUNNING-75**: Non-trivial r_b(k) dispersion running breaks H_b^2 cancellation. Gate: Delta(tau_cross(k)) variation across Planck band | Transit | HIGH | 1 session |
| A4 | **A_S-FROM-COLEMAN-WEINBERG-75**: Joint A_s + n_s from BCS-dressed CW potential. Gate: n_s in [0.955,0.975] AND |log10(A_s/A_s_obs)| < 1.0 | Tesla, Hawking (H-75-7), Naz (#6) | HIGH | 1 session |
| A5 | **EIH-CC-PROJECTION-75 / F_CONV-75**: Derive f_conv from spectral triple. Gate: f_conv in [10^-3, 10^3] from first principles | Einstein, SP | HIGH | 1 session |
| A6 | **N25-CROSS-CORRELATION-CHECK-75**: Full-spectrum phase-diffusion with a_2 weight. Gate: cross-term < 0.01 OOM | Mack-Landau | MEDIUM | 1 session |
| A7 | **E-C-OBSERVABLE-MAPPING-75**: A_s as function of E_C(A). Gate: monotone dependence with < 0.05 shift | Mack-Landau | MEDIUM | 1 session |

#### B. Moduli Stabilization (W1-B 0/4 FAIL → surviving channels)

| # | Computation | Sources | Priority | Effort |
|:--|:-----------|:--------|:---------|:-------|
| B1 | **MULTI-INSTANTON-LMAX10-75**: Extend L_max to {8,9,10} sectors. Gate: dS/dtau sign changes in [0.45,0.70] | Hawking (H-75-2), Tesla | HIGH | 4-8h CPU |
| B2 | **CROSS-SPECTRAL-MOMENT-MODULI-75**: a_2 + a_4 contributions to V_eff(tau). Gate: restoring gradient >= 400 M_KK^4 at tau=0.48 | Einstein (#3), Hawking (H-75-1), Tesla | HIGH | 1 session |
| B3 | **FOLD-STIFFNESS-RENORMALIZATION-75**: ATDHFB collective mass M(tau) under GGE backreaction. Gate: tau_overshoot in [0.45,0.70] | Hawking (H-75-3) | HIGH | 1 session |
| B4 | **MORSE-BOTT-MULTI-LMAX-75**: Repeat 36D Hessian at L_max {3,5,7}. Gate: signature (36+,0-,0) at all L_max | Naz (#4) | MEDIUM | LOW |
| B5 | **N22-N25-COUPLING-CHECK-75**: m_eff from multi-instanton condensate at L_max=10. Gate: m_eff^2/H_fold^2 >= 20.7 | Mack-Landau | MEDIUM | 1 session |

#### C. n_s Red Tilt (n_s=1.000 from transfer → need separate mechanism)

| # | Computation | Sources | Priority | Effort |
|:--|:-----------|:--------|:---------|:-------|
| C1 | **N_S-FROM-NON-POWER-LAW-H-75**: Modified H(tau) with quasi-de Sitter phase. Gate: n_s in [0.9607,0.9691] | Hawking (H-75-4) | HIGH | 1 session |
| C2 | **ALPHA-S-FROM-DRESSED-POTENTIAL-75**: n_s + alpha_s from BCS-dressed CW directly. Gate: n_s in [0.955,0.975] | Naz (#6) | HIGH | 1 session |
| C3 | **LAYER-1-LAYER-2-DIFF-75**: c_b^(1) vs c_b^(2) for 8 BCS branches at tau_exit. Decides D-R2-2 dissent | Transit-Einstein | HIGH | LOW |
| C4 | **PHASES-BD-75**: Squeezing phases phi_k alongside magnitudes r_k for all 8 branches | Transit-Einstein | MEDIUM | LOW |

#### D. CC / Dark Energy (effacement CLOSED, chi_2 route surviving)

| # | Computation | Sources | Priority | Effort |
|:--|:-----------|:--------|:---------|:-------|
| D1 | **CC-VARIANCE-75**: Spectral variance sigma_lam^2 as independent 2nd moment. Gate: within 1 OOM of rho_obs | Volovik (#2), Lizzi (LF-5) | HIGH | LOW |
| D2 | **CC-M2-SPECTRAL-75**: Exp-component moment M_exp. Gate: M_exp/M_exp_max within factor 3 of chi_2 | Volovik (#1) | MEDIUM | LOW |
| D3 | **NONLOCAL-SA-CC-75**: Leading nonlocal SA correction. Gate: log-scale CC shift >= 10 OOM | Transit, Einstein | MEDIUM | 1 session |
| D4 | **EFFACEMENT-CHANNEL-REBUILD-75**: Reassign 3-channel partition. Gate: Omega_Lambda in [0.343,1.000] | Volovik (#5), Lizzi (LF-6) | MEDIUM | 1 session |
| D5 | **CC-SCHEME-REPORT-75**: Update framework docs to chi_2 * H_0^2 * M_Pl^2 = 0.33*rho_obs | Volovik (#7), Lizzi (LF-4) | LOW (bookkeeping) | LOW |
| D6 | **M1-L11-CONVERGENCE-75**: Extend sqrt-moment to L_max=11. Gate: drift < 15% | Volovik (#4) | MEDIUM | HIGH (CPU) |
| D7 | **CC-DOUBLE-INDEX-75**: (chi_2, n_b/n_f) joint L_max-robust indices. Gate: drift < 3% | Mack-Landau | LOW | LOW |
| D8 | **JACOBSON-LAMBDA-CONSTRAINT-75**: Multi-T GGE thermodynamic identity pins normalization. Gate: unique normalization | Einstein (#4) | MEDIUM | 1 session |
| D9 | **SOFT-HAIR-DE-VERIFICATION-75**: Soft-hair as DE via a_2 vacuum energy. Gate: f_DE in [0.10,0.30] | Mack-Landau | MEDIUM | LOW |

#### E. Dark Matter (Leggett channel + soft-hair + dimer Z_2)

| # | Computation | Sources | Priority | Effort |
|:--|:-----------|:--------|:---------|:-------|
| E1 | **SOFT-HAIR-LEGGETT-FILTER-75**: CPT-parity surviving fraction of 196.2 R-G sectors. Gate: fraction ≈ 0.082 | Volovik, SP, Tesla | HIGH | LOW |
| E2 | **DIMER-Z2-PAIR-PRODUCTION-75**: Parker pair production in Z_2-odd sector. Gate: n_Z2/n_pair in [0.1,0.5] | Tesla, Mack-Landau | MEDIUM | 0.75 session |
| E3 | **MULTI-CHANNEL-DM-CDM-COMPAT-75**: Z_2 Parker + dispersion + c_s + ISW at recomb. Gate: all match CDM at 0.07 | Mack-Landau | MEDIUM | 1 session |

#### F. Structural Floor / Foundational Audit

| # | Computation | Sources | Priority | Effort |
|:--|:-----------|:--------|:---------|:-------|
| F1 | **FOUNDATIONAL-AUDIT-75**: 22 theorems x 7 axes (F1-F7). Gate: all ROBUST/QUASI-ROBUST | Lizzi (LF-10), SP, QA-VDD | HIGH | 1 session |
| F2 | **L-MAX-BIDIRECTIONAL-75 / NEEDS_REVERIFY-BATCH-75**: Explicit L=5/7 verify of 3 W5-F theorems (DNP, Pomeranchuk, FR) | Volovik, Lizzi (LF-9) | MEDIUM | LOW |
| F3 | **BDI-CLASS-ALL-TAU-VERIFICATION-75**: Pfaffian Z_2 at all tau in [0,tau_fold]. Gate: Pfaffian=+1 at all 10 tau | Einstein (#7) | MEDIUM | LOW |
| F4 | **LEFSCHETZ-PERMANENT-75**: Verify n*=60 independence under L_max=7 variation. Gate: promote to permanent | Transit | MEDIUM | LOW |
| F5 | **BDSPT-TAU-SCAN-75**: W4-H non-perturbative J-invariance at tau={0.00,0.10,0.19,0.25,0.30} | QA-VDD, Hawking (H-75-6) | MEDIUM | MEDIUM |
| F6 | **STRUCTURAL-REGISTRY-ENTRY-48**: W4-X six-layer composite → registry #48 | Tesla | LOW | LOW |

#### G. Spectral Functional / L_max Convergence

| # | Computation | Sources | Priority | Effort |
|:--|:-----------|:--------|:---------|:-------|
| G1 | **ANOMALY-DERIVED-F-STAR-75**: Lizzi 2011 anomaly→bosonic action f*. Gate: c_1 > 0.9 | Lizzi (LF-1) | HIGH | 1 session |
| G2 | **M_H-FROM-KASPAROV-75**: Higgs mass without f(0) weighting. Gate: m_H within 2 GeV | Lizzi (LF-2) | HIGH | 1 session |
| G3 | **ZETA-IS-NOT-PHYSICAL-75**: Formal permanent theorem. Gate: 3 routes share common obstruction | Lizzi (LF-3) | MEDIUM | LOW |
| G4 | **R-PROTECTED-DEFINITIONS-75**: Add convention flags to canonical_constants.py | Lizzi (LF-7) | LOW (bookkeeping) | LOW |
| G5 | **LIZZI-OBSERVABLE-EMPIRICAL-75**: (m_H/v_EW)^2*(Lambda/M_Pl^2) = R_1. Gate: observed within 1% | Lizzi (LF-8) | HIGH | LOW |

#### H. Observational / Pre-registration

| # | Computation | Sources | Priority | Effort |
|:--|:-----------|:--------|:---------|:-------|
| H1 | **GGE-TRANSFER-74 (N5)**: Transfer from GGE relic to CMB C_l. Gate: delta_n_s < 0.005 | EVOI | HIGH | 1 session |
| H2 | **SIN2-LR-NORMALIZATION-74 (N6)**: Baptista eq 3.41 L/R asymmetry. Gate: sin^2 in [0.230,0.233] | EVOI | HIGH | 1 session |
| H3 | **W4-Z-W-A-REGISTRATION-75**: Pre-register w_a falsifier [+0.10,+0.22]. Gate: registration | Mack-Landau | LOW | LOW |
| H4 | **LEGGETT-JEANS-FALSIFIER-75-SPEC**: Pre-register joint (rho_L, c_L) constraint | QA-VDD | LOW | LOW |
| H5 | **SWAMPLAND-SUBSTRATE-75**: de Sitter swampland conjecture test. Gate: |V'|/V >= O(1) | Einstein (#6) | MEDIUM | 1 session |

#### I. Parker / Hawking-Unruh Reconciliation + Transit Refinement

| # | Computation | Sources | Priority | Effort |
|:--|:-----------|:--------|:---------|:-------|
| I1 | **PARKER-HAWKING-RECONCILIATION-75**: Which formulation is canonical for A_s? Gate: identify canonical | Transit | HIGH | 1 session |
| I2 | **KAPPA-DEFINITION-75**: Formalize 3 kappa scales as permanent definitional constraint | Transit, SP, Tesla, Naz | LOW (bookkeeping) | LOW |
| I3 | **WHITE-HOLE-NO-HAWKING-75**: Verify acoustic white hole has no Hawking radiation beyond squeeze | Transit-Einstein | LOW | LOW |
| I4 | **MACH-SHARPNESS-SCALING-75**: kappa_H/T_eff = Mach^2*(M_KK/Delta)^2*N_geom. Gate: scales as Mach^2 | QA-VDD | MEDIUM | MEDIUM |

#### J. Nuclear-DFT / BCS Refinement

| # | Computation | Sources | Priority | Effort |
|:--|:-----------|:--------|:---------|:-------|
| J1 | **BMA-EC-CHOICE-75**: Bayesian model averaging for E_C three-method split. Gate: BF(A:B) > 10 | Naz (#2) | MEDIUM | LOW |
| J2 | **PCK-LARGE-N-PAIR-75**: R-G integrability at filling 0.10, 0.15, 0.20. Gate: <r> < 0.45 to 0.15 | Naz (#3) | MEDIUM | MEDIUM |
| J3 | **BCS-DRESSED-W2C-75**: Full self-consistent BCS-dressed backreaction. Gate: delta_kappa_pp < 0.03 | Naz (#5) | LOW | 1 session |
| J4 | **THREE-METHOD-DECOMPOSITION-75**: Generalize to Leggett, Mott, BKT, Pomeranchuk | Mack-Landau | MEDIUM | 1.5 session |

#### K. Lorentz / Speed Hierarchy / Dispersion

| # | Computation | Sources | Priority | Effort |
|:--|:-----------|:--------|:---------|:-------|
| K1 | **EMERGENT-LORENTZ-FROM-A2-75**: c_light_emergent/c_substrate from a_2 structure. Gate: consistent with 3-speed hierarchy | Einstein (#8) | MEDIUM | 1 session |
| K2 | **SPECTRAL-DECOUPLING-CERT-75**: Register Spectral-Moment Decoupling Theorem with Gilkey proof | Transit-Einstein | HIGH | LOW |
| K3 | **LV-NLO-75**: c_photon/c_Gold to NLO from a_4 correction. Gate: structural prediction at O(10^-34) | Transit-Einstein | LOW | LOW |

#### L. N_eff / BBN / Thermalization

| # | Computation | Sources | Priority | Effort |
|:--|:-----------|:--------|:---------|:-------|
| L1 | **N-EFF-POST-THERMALIZATION-75**: Parker weighting + decoupling trace fold→BBN. Gate: exact SM match | Tesla | MEDIUM | 1 session |
| L2 | **DC-PERMANENCE-74 (N11)**: 20% DC component on 8-cell, 12-cell. Gate: DC > 10% | EVOI | MEDIUM | 1 session |

#### M. Geometry / Topology

| # | Computation | Sources | Priority | Effort |
|:--|:-----------|:--------|:---------|:-------|
| M1 | **KOSMANN-KERNEL-TAU-SCAN-75**: dim Ker(K_a) at 5 tau values. Gate: constant | QA-VDD | LOW | LOW |
| M2 | **KOSMANN-KERNEL-GENERALIZATION-75**: dim Ker for SU(2), SU(3), SU(4), G_2, Sp(2) | QA-VDD | MEDIUM | MEDIUM |
| M3 | **CHERN-NOETHER-DUAL-75**: c_1(L_BCS, D_K) via Lefschetz thimble. Gate: c_1 = 60 | QA-VDD | MEDIUM | MEDIUM |
| M4 | **PLANCHEREL-INVARIANCE-1-7-2-75**: Ratio 1:7:2 at L_max {3,5,7,10} | QA-VDD | LOW | LOW |
| M5 | **TWO-MANIFOLD-NEMB-75**: Two-Manifold Non-Embedding Theorem. Gate: re-derives 86 OOM bracket | Transit-Einstein | MEDIUM | MEDIUM |

#### N. Condensed-Matter / Multi-Cell

| # | Computation | Sources | Priority | Effort |
|:--|:-----------|:--------|:---------|:-------|
| N1 | **CG24-COSMO-TILING-RULE-75**: How CG(24) replicates. Gate: exactly one candidate | Mack-Landau | MEDIUM | LOW |
| N2 | **POMERAN-N-SCAN-75**: Pomeranchuk instability at N_cells = 4, 8, 12 | Mack-Landau | MEDIUM | 1 session |
| N3 | **LUTTINGER-TIME-ORDER-75**: Extend to time-ordered correlators. Gate: 80/20 preserved | Mack-Landau | LOW | 1 session |
| N4 | **SYM-N-ENUMERATION-75**: Sym^4(su(3)^*) J_C2 parity partition | Mack-Landau | LOW | LOW |

#### O. Methodology / Bookkeeping

| # | Computation | Sources | Priority | Effort |
|:--|:-----------|:--------|:---------|:-------|
| O1 | **ATLAS-RECLASSIFY-75**: Classify 70 NEEDS_REVERIFY entries. Gate: >= 40 classified | Mack-Landau | LOW | 1 session |
| O2 | **STEP-0-ALGORITHM-ADOPT-75**: Apply 6-step c-classification to pre-S75 computations | Transit-Einstein | LOW | MEDIUM |
| O3 | **W4-V-RETRACT-REGISTER-75**: Replace single-threshold meta-gate with rolling window | Mack-Landau | LOW | LOW |
| O4 | **SCORECARD-ADD-HORIZON-ALIGN-75**: Add STR entry #24 | Mack-Landau | LOW | LOW |
| O5 | **CROSS-CHECK-T-74B**: t_functional vs t_structural comparison | Mack-Landau | MEDIUM | LOW |

#### P. Lab-Scale / Experimental Pre-registration (Tesla-Mack-Bells)

| # | Computation | Sources | Priority | Effort |
|:--|:-----------|:--------|:---------|:-------|
| P1 | **JENSEN-EFF-GAP-75**: Bogoliubov projection to lab BCS boundary | Tesla-Mack-Bells | MEDIUM | 2-4 weeks |
| P2 | **LEGGETT-Q-FACTOR-75**: Leggett branch Q on lab embedding | Tesla-Mack-Bells | MEDIUM | 1-2 weeks |
| P3 | **JENSEN-COUPLING-SCALING-75**: Lab Jensen-to-acoustic coupling | Tesla-Mack-Bells | MEDIUM | 1 week |
| P4 | **JENSEN-KERR-75**: Kerr coefficient for JPA-analog | Tesla-Mack-Bells | MEDIUM | 2-3 weeks |
| P5 | **MACK-BOGOLIUBOV-BOUNDARY-75**: a_0→a_2 Bogoliubov mediation at boundaries | Tesla-Mack-Bells | HIGH | 2-3 weeks |

---

## Additional Mined Suggestions (from grep fallback)

All significant recommendations have been captured in the structured carry-forward tables above. The S74 session was comprehensive with 12 structured wrap-up sections (8 syntheses + 4 workshops) that cover all open channels.

### Key Structural Open Questions

1. **The A_s gap is the #1 open problem**: +9.47 OOM (Bogoliubov amplitude CLOSED), conversion mechanism required
2. **Moduli stabilization is the #2 open problem**: 0/4 sub-gates FAIL, cross-moment and multi-instanton survive
3. **n_s red tilt mechanism**: Transfer gives exactly 1.000; sole surviving route is S66 BCS-dressed CW
4. **CC closure**: chi_2 * H_0^2 * M_Pl^2 = 0.33*rho_obs is L_max-robust, but WHY H_0^2*M_Pl^2 is the prefactor remains open (q-theory)
5. **Spectral functional**: FUNCTIONAL-SELECT FAIL-PERMANENT; f is genuine UV input
6. **L_max convergence**: absolute sums Weyl-divergent; only ratios and log-scale observables stable

---

## Plan Templates

The planner should read `.claude/templates/plan-compute.md` for the mandatory compute-format plan structure.
