# Session 60 Way Forward: Extracted Computation Agenda

**Date**: 2026-03-27
**Source**: S60 collab reviews (9 reviewers), 3He-B comparison (Volovik addenda), Connes zeta addenda, Van den Dungen framework review, Nazarewicz particle emergence map, Lost Treasure appendix, user-directed priorities
**Method**: Each researcher extracts their own suggestions as numbered test cases. Entries are computation-grade (inputs, outputs, gates).

---

## Wave Structure for S61+ Planning

99 entries organized into 8 waves + Lost Treasures. Three parallel lanes after W0.

### Dependency Flow

```
W0 (Foundations) ──→ W1 (a_2 cross-checks)
   │                    │
   │                    ↓
   ├──────────────→ W2a (alpha regime) ──→ W3 (CC/stabilization)
   │                    │                      │
   │                    ↓                      ↓
   ├──────────────→ W2b (GGE survival) ──→ W5 (signatures)
   │                    │
   ├──────────────→ W4 (transit + CP) ←── W1 (HAWK-9)
   │
   └──────────────→ W6 (zeta/number theory) ──→ W7a (VdD deep)

   W7b,c (benchmarks, speculative) — float, no blocking dependencies
```

**Parallelism**: W2b and W6 are fully independent of each other and of W2a. Three-lane parallel execution after W0:
- **Lane 1**: W1 → W2a → W3 → W5 (predictions that need CC)
- **Lane 2**: W2b → W5 (predictions that need GGE)
- **Lane 3**: W6 → W7a (spectral zeta → VdD deep theory)

### W0: Foundations (6 entries)
*Non-negotiable prerequisites. Everything downstream waits on these.*

| ID | Title | Why W0 |
|:---|:------|:-------|
| USER-1 | Compound Staircase Modification | User directive, independent |
| USER-2 + SP-1 | Heat Kernel a_2 Local Curvature | THE bottleneck — ~40 entries need this number |
| USER-4 + VDD-2 | O'Neill A-Tensor Cross-Terms | Validates fiber-base decomposition |
| BAP-5 | PW Data Audit (1,2) Irrep | Data integrity — which prior results stand? |
| SPEC-5 | Spin Connection Curvature in a_2 | Determines if simplified a_2 formula suffices |

### W1: a_2 Cross-Check Gauntlet (6 entries)
*Three independent routes to a_2, plus derivatives. Agreement = H_0 nailed permanently.*

| ID | Title | Method |
|:---|:------|:-------|
| HAWK-1 | Zeta Regularization a_2 | Route 2: spectral zeta residue at s=3 |
| QA-8 | Regularized Spectral Sum | Route 3: heat trace from PW eigenvalues |
| HAWK-9 | a_2 Tau Derivative | d(a_2)/dtau — feeds W4 transit SA |
| SP-2 | PW Conformal Interpretation | Does PW ever converge to local? |
| SPEC-4 | Weyl Law Verification | Eigenvalue asymptotics vs volume |
| NAZ-1 | Particle-Number Projection a_2 | BCS symmetry-breaking shift on a_2? |

### W2a: Alpha Regime (3 entries)
*Which side of alpha_crit=55? Determines stabilization mechanism.*

| ID | Title |
|:---|:------|
| PHONON-2 | Physical Alpha on Jensen Metric (consolidated from 9 agents) |
| SP-5 | Alpha_crit Conformal Selection Rule (WHY 55?) |
| BAP-6 | a_4/a_2 Ratio for Higgs Mass |

### W2b: GGE Survival — Multi-Method Assault (11 entries)
*Does the DM production mechanism survive? 8 independent methods on one question.*

| ID | Title | Method |
|:---|:------|:-------|
| TESLA-1 | Thouless Time SFF (32-cell) | Spectral form factor, full scale |
| PHONON-3 | Thouless Time CG(24) Spectral Gap | Graph Laplacian, S_4 rep theory |
| VOL-2 | GGE Thermalization Scaling Formula | Analytic E_Th scaling |
| HAWK-2 | Thouless Time Many-Body ED | Exact diag, extrapolate to 10^80 |
| NAZ-3 | Compound Nucleus Thermalization | Doorway-state + spreading width |
| SP-3 | Conformal Time Budget | Causal: is thermalization accessible? |
| PHONON-7 | Integrability Breaking Scaling | delta_k(N) power law to N=64 |
| TESLA-6 | Josephson Collective Mode Integrability | Level spacing ⟨r⟩ on CG(24) |
| LANDAU-4 | Fermi Liquid Params w/ Josephson | Pomeranchuk stability inter-cell |
| LT-3 | KAM Threshold | Dynamical systems at delta=0.33 |
| LANDAU-8 | Ginzburg Criterion | Mean-field reliability of staircase |

### W3: CC Problem & Stabilization (8 entries)
*What sets Lambda_residual? Does the staircase converge? Which stabilization survives?*

| ID | Title |
|:---|:------|
| PHONON-6 | a_4 + q-Theory Compound (sole surviving CC path) |
| LANDAU-1 | GL Free Energy Staircase (consolidated: chi_q + GL + tau scan) |
| VOL-8 | Multi-Pair Q-Theory N=5..8 |
| NAZ-2 | Bayesian CC Model Comparison |
| PHONON-12 | Nuclear Odd-Even Staggering |
| TESLA-5 | Physical Debye Cutoff PW |
| BAP-2 | Off-Jensen Screening Ratio |
| BAP-4 | Lichnerowicz Gap vs Sectional Curvature |

### W4: Transit Physics & Baryogenesis (9 entries)
*S38 paradigm shift: transit dynamics, not static minimum. Plus: can CP be violated?*

| ID | Title |
|:---|:------|
| USER-3 + VDD-6 | Transit Spectral Action (THE paradigm computation) |
| VDD-4 | Spectral Flow tau=0 to fold (includes S_inst tension) |
| HAWK-4 | Back-Reaction Corrected Parker Spectrum |
| HAWK-5 | GSL-Timescape Jensen Convexity |
| TESLA-3 | Dynamic J-Breaking Transit (sole baryogenesis escape) |
| VOL-7 | J-Breaking Mechanism Catalog (E1-E4) |
| PHONON-9 | Twisted Spectral Triple CP |
| NAZ-18 | Transit Baryogenesis Estimate |
| PHONON-8 | BCS Phase Boundary vs Soliton DW |

### W5: Observational Signatures (11 entries)
*What does the framework predict that can be measured?*

| ID | Title | Observable |
|:---|:------|:-----------|
| NAZ-14 | Yukawa Couplings from D_F | Fermion mass ratios |
| NAZ-15 | Higgs Mass Sector-Resolved | m_H with a_4/a_2 correction |
| QA-1 | Van Hove Dispersion B2 | DM spectral shape |
| QA-4 | Leggett Squeezing Spectrum | DM occupation n(k) |
| QA-5 | B2 Flat Band Robustness | Van Hove protection in fabric |
| QA-6 | Multimode Covariance | Super-Poissonian vs CDM |
| QA-3 | Acoustic Metric + Sonic Horizon | Parker vs Hawking mechanism |
| NAZ-4 | Pair Transfer CMB Propagation | delta_T/T from pair chain |
| NAZ-11 | Pair-Transfer Scaling Fabrics | Bosonic S_+(N) at 4-8 cells |
| NAZ-8 | Nuclear Pairing Chain Attenuation | Delta/E_F inheritance levels |
| VOL-4 | Dipolar Thermalization on Fabric | Leggett mode lifetime |

### W6: Spectral Zeta & Number Theory (7 entries)
*The Connes program. Independent lane — runs parallel to W1-W5.*

| ID | Title |
|:---|:------|
| CONNES-1 | Spectral Zeta Zero Location |
| CONNES-2 | Level Spacing Statistics |
| CONNES-3 | Functional Equation + J-Symmetry |
| CONNES-4 | Trace Formula Geometric Side |
| CONNES-6 | Weil Positivity Test (needs CONNES-1) |
| CONNES-7 | Zeta Residues vs Physical Constants (needs W0 a_2) |
| CONNES-8 | Connes Distance Projections (needs CONNES-1) |

### W7: Framework Extensions & Benchmarks (21 entries)
*Deepen mathematical foundations. Not blocking physics, but permanent results.*

**7a — VdD Deep Theory** (10): VDD-3, VDD-5, VDD-7, VDD-8, VDD-9, VDD-10, VDD-12, VDD-13, VDD-14, VDD-16

**7b — Benchmarks & Diagnostics** (9): NAZ-6, NAZ-7, NAZ-9, NAZ-10, NAZ-13, NAZ-16, NAZ-17, LANDAU-3, LANDAU-10

**7c — Speculative / LOW** (12): VDD-17, VDD-18, HAWK-6, HAWK-7, HAWK-8, SP-4, SP-6, VOL-6, VOL-9, PHONON-4, PHONON-5, BAP-8

### Lost Treasures (5 entries, no agents)
LT-1 (lattice SVP), LT-2 (tropical geometry), LT-4 (coding theory), LT-5 (q-series), LT-6 (signal processing)

*LT-3 (KAM threshold) promoted to W2b.*

---

### Index of Computation Entries (99 unique after deduplication)

| Section | ID | Title | Priority | Gate |
|:--------|:---|:------|:---------|:-----|
| **User** | USER-1 | Compound Staircase Modification | HIGH | COMPOUND-STAIRCASE-61 |
| | USER-2 | Heat Kernel a_2 from Milnor's Ricci Formula | HIGH | HEAT-KERNEL-A2-61 |
| | USER-3 | Van den Dungen Transit Spectral Action | HIGH | TRANSIT-SA-61 |
| | USER-4 | A-Tensor Correction to D_K | HIGH | A-TENSOR-61 |
| **SP** | SP-1 | Local Heat Kernel a_2 from Jensen Metric Scalar Curvature | HIGH | HEAT-KERNEL-A2-LOCAL-61 |
| | SP-2 | Conformal Interpretation of PW Spectral Sum Divergence | MED | PW-CONFORMAL-ZETA-61 |
| | SP-3 | Thouless Time vs Conformal Time Budget | HIGH | GGE-THERM-61 |
| | SP-4 | Penrose Inequality Analog for BCS Sector | MED | PENROSE-INEQ-BCS-61 |
| | SP-5 | Alpha_crit = 55 Conformal Selection Rule | MED | ALPHA-CRIT-CONFORMAL-61 |
| | SP-6 | Post-Superradiance State = Dump Point Identification | LOW | SUPERRAD-DUMP-61 |
| **Hawking** | HAWK-1 | Zeta-Function Regularization Cross-Check of a_2 | HIGH | ZETA-A2-61 |
| | HAWK-2 | Thouless Time for GGE Thermalization | HIGH | THOULESS-GGE-61 |
| | HAWK-4 | Back-Reaction Corrected Parker Spectrum | MED | BACKREACTION-PARKER-61 |
| | HAWK-5 | GSL-Timescape Formal Verification | MED | GSL-TIMESCAPE-61 |
| | HAWK-6 | (0,0) Sector Bekenstein Saturation -- Physical Radius | LOW | BEKENSTEIN-RADIUS-61 |
| | HAWK-7 | Volovik-Sakharov G_eff for Island Formula Rescue | LOW | VS-GEFF-ISLAND-61 |
| | HAWK-8 | Extremal GGE Quantum Stability | LOW | EXTREMAL-GGE-61 |
| | HAWK-9 | Heat Kernel a_2 Tau Derivative for Transit SA | HIGH | A2-TRANSIT-61 |
| **Volovik** | VOL-2 | GGE Thermalization via Thouless Time | HIGH | GGE-THERM-61 |
| | VOL-4 | Dipolar Thermalization on Fabric | MED | DIPOLAR-THERM-61 |
| | VOL-6 | Bekenstein Saturation through de Sitter Thermodynamics | LOW | BEKENSTEIN-HOLOGRAPHIC-61 |
| | VOL-7 | J-Breaking Mechanism Catalog for Baryogenesis | MED | J-BREAKING-CATALOG-61 |
| | VOL-8 | Multi-Pair Q-Theory at Finite N | HIGH | MULTI-PAIR-QTHEORY-61 |
| | VOL-9 | Inheritance Chain CFL Correspondence Count | LOW | CFL-CORRESPONDENCE-61 |
| **Baptista** | BAP-2 | Off-Jensen Screening Ratio on 2D Volume-Preserving Surface | HIGH | OFFJ-SCREEN-61 |
| | BAP-4 | Lichnerowicz Gap vs Sectional Curvature at Domain Wall | MED | LICH-KSEC-61 |
| | BAP-5 | PW Data Audit -- (1,2) Irrep Contamination Scope | HIGH | PW-AUDIT-61 |
| | BAP-6 | Proper Heat Kernel Ratio a_4/a_2 for Higgs Mass | MED | HK-RATIO-61 |
| | BAP-8 | Pati-Salam Spectral Action Regime at GUT Scale | LOW | PS-REGIME-61 |
| **Tesla** | TESLA-1 | Thouless Time from Fabric Spectral Form Factor | HIGH | GGE-THERM-61 |
| | TESLA-3 | Dynamic J-Symmetry Breaking During Transit | HIGH | J-DYNAMIC-61 |
| | TESLA-5 | Physical Debye Cutoff for PW Tower | MED | DEBYE-STABLE-61 |
| | TESLA-6 | Josephson Collective Mode Integrability | HIGH | JOSEPHSON-INTEG-61 |
| **QA** | QA-1 | Van Hove Dispersion -- Tau-Resolved B2 Spectrum | HIGH | VANHOVE-DISP-61 |
| | QA-3 | Acoustic Metric Construction -- Unruh Form | MED | ACOUSTIC-METRIC-61 |
| | QA-4 | Mode-Resolved Leggett Squeezing Spectrum | HIGH | LEGGETT-SPECTRUM-61 |
| | QA-5 | B2 Flat Band Robustness Under Josephson Coupling | HIGH | B2-FABRIC-61 |
| | QA-6 | Multimode Covariance of Squeezed Leggett Modes | MED | MULTIMODE-COV-61 |
| | QA-8 | Regularized Spectral Sum via Heat Kernel -- Debye Analogy | HIGH | REG-SPECTRAL-61 |
| **Landau** | LANDAU-1 | Ginzburg-Landau Free Energy for the CC Staircase | HIGH | GL-STAIRCASE-61 |
| | LANDAU-3 | BCS-BEC Crossover Diagnostic | MED | BCS-BEC-61 |
| | LANDAU-4 | Fermi Liquid Parameters with Josephson Coupling | HIGH | POMERAN-FABRIC-61 |
| | LANDAU-8 | Ginzburg Criterion for the CC Staircase | MED | GINZBURG-CC-61 |
| | LANDAU-10 | Landau Damping Threshold for the Leggett Mode | LOW | LEGGETT-DAMPING-61 |
| **Nazarewicz** | NAZ-1 | Particle-Number Projection for the Heat Kernel | HIGH | PROJ-A2-61 |
| | NAZ-2 | Bayesian Model Comparison for CC Mechanisms | MED | CC-BAYES-MODEL-61 |
| | NAZ-3 | GGE Thermalization via Compound Nucleus Formalism | HIGH | GGE-THERM-61 |
| | NAZ-4 | Pair Transfer CMB Propagation | MED | PAIR-CMB-61 |
| | NAZ-6 | SD-Shell Benchmark Comparison | HIGH | SD-SHELL-BENCH-61 |
| | NAZ-7 | PBCS Correction Scaling with Fabric Size | MED | PBCS-FABRIC-61 |
| | NAZ-8 | Nuclear Pairing Chain Attenuation | HIGH | PAIRING-CHAIN-61 |
| | NAZ-9 | Seniority Quantum Numbers on the Fabric | MED | SENIORITY-FABRIC-61 |
| | NAZ-10 | Pair-Transfer EWSR (Thouless Identity) | MED | GPV-EWSR-61 |
| | NAZ-11 | Pair-Transfer Scaling on Larger Fabrics | MED | PAIR-FABRIC-61 |
| | NAZ-13 | BDI to DIII Transition Through Compositing | LOW | BDI-DIII-CHAIN-61 |
| | NAZ-14 | Yukawa Couplings from D_F on Jensen-Deformed SU(3) | HIGH | YUKAWA-FIRST-PRINCIPLES-61 |
| | NAZ-15 | Higgs Mass from Sector-Resolved Spectral Action | MED | HIGGS-MASS-61 |
| | NAZ-16 | Heat Kernel Mode-Resolved Oscillations | MED | HK-OSCILLATION-61 |
| | NAZ-17 | Bayesian Inheritance vs Analogy Discrimination | LOW | INHERIT-BAYES-61 |
| | NAZ-18 | Cosmological Transit Baryogenesis Estimate | MED | TRANSIT-BARYOGEN-61 |
| **Phonon** | PHONON-2 | Physical Alpha Parameter on Jensen Metric | HIGH | ALPHA-REGIME-61 |
| | PHONON-3 | Thouless Time on CG(24) via Spectral Gap | HIGH | GGE-THERM-61 |
| | PHONON-4 | Superfluid Weight from Quantum Metric | MED | MEISSNER-LEGGETT-61 |
| | PHONON-5 | Spectral Dimension from Pair Return Probability | MED | SPEC-DIM-PAIR-61 |
| | PHONON-6 | a_4-Dominated Spectral Action with q-Theory Vacuum | HIGH | A4-QT-COMPOUND-61 |
| | PHONON-7 | Integrability Breaking Scaling with N_cells | HIGH | INTEG-SCALING-61 |
| | PHONON-8 | BCS Phase Boundary vs Soliton Domain Wall | LOW | DW-CLASS-61 |
| | PHONON-9 | Twisted Spectral Triple for CP Violation | LOW | TWIST-CP-61 |
| | PHONON-12 | Nuclear Odd-Even Staggering in CC Staircase | LOW | ODDEVEN-61 |
| **Connes** | CONNES-1 | Spectral Zeta Zero Location (Finite Dirichlet Series) | HIGH | ZETA-ZEROS-61 |
| | CONNES-2 | Level Spacing Statistics at the Fold | MED | LEVEL-STATS-61 |
| | CONNES-3 | Functional Equation and J-Symmetry Constraints | HIGH | FUNC-EQ-61 |
| | CONNES-4 | Heat Kernel Trace Formula -- Geometric Side | MED | TRACE-FORMULA-61 |
| | CONNES-6 | Weil Positivity Test for Jensen-Deformed SU(3) | MED | WEIL-POS-61 |
| | CONNES-7 | Spectral Zeta Residues vs Physical Constants | MED | ZETA-RESIDUES-61 |
| | CONNES-8 | Connes Distance Between Spectral Projections | LOW | CONNES-DIST-PROJ-61 |
| **VdD** | VDD-2 | Kasparov Factorization with O'Neill Cross-Terms | CRIT | A-TENSOR-61 |
| | VDD-3 | Jensen Deformation as Locally Bounded Perturbation | HIGH | K-HOMOLOGY-STABILITY-61 |
| | VDD-4 | Spectral Flow of D_K(tau) from tau=0 to tau_fold | HIGH | SPECTRAL-FLOW-61 |
| | VDD-5 | Order-One Condition vs Gauge Module Conditions | HIGH | GAUGE-MODULE-61 |
| | VDD-6 | Transit Spectral Action from Families of Spectral Triples | CRIT | TRANSIT-SA-61 |
| | VDD-7 | First Explicit Kasparov Product Verification | MED | KASPAROV-VERIFY-61 |
| | VDD-8 | Shriek Map vs Baptista Fiber Integration Equivalence | MED | SHRIEK-EQUIV-61 |
| | VDD-9 | BdG Spectral Action (Finite-Density Extension) | MED | BDG-SA-61 |
| | VDD-10 | Block-Diagonal Theorem Generality | MED | BLOCK-DIAG-GENERAL-61 |
| | VDD-12 | Jensen Moduli Space Completeness (36D Hessian) | MED | MODULI-HESS-61 |
| | VDD-13 | Paper 05 Topological Corrections from Non-Trivial Bundle | LOW | CHERN-INST-61 |
| | VDD-14 | Fredholm Complex for the BdG System | LOW | FREDHOLM-BDG-61 |
| | VDD-16 | Ruelle Zeta Function and Arithmetic Content | LOW | RUELLE-ARITH-61 |
| | VDD-17 | Pseudo-Riemannian Extension to Lorentzian ST | LOW | LORENTZ-SA-61 |
| | VDD-18 | Inheritance Kasparov Product at Each Compositing Level | LOW | INHERIT-CLASSIFY-61 |
| **Spectral** | SPEC-4 | Weyl Law Verification on Jensen SU(3) | MED | WEYL-VERIFY-61 |
| | SPEC-5 | Spin Connection Curvature Term in a_2 | HIGH | SPIN-CURV-61 |
| **Lost Treasure** | LT-1 | Lattice Basis Reduction (SVP on weight lattice) | -- | LATTICE-SVP-CC |
| | LT-2 | Tropical Geometry (tropicalized spectral action) | -- | -- |
| | LT-3 | KAM Threshold (GGE survival at delta=0.33) | -- | KAM-THRESHOLD-61 |
| | LT-4 | Coding Theory (weight lattice error correction) | -- | -- |
| | LT-5 | Combinatorial Number Theory (staircase q-series) | -- | Q-SERIES-MODULAR-61 |
| | LT-6 | Signal Processing (CC as DC residual) | -- | PSD-DC-61 |

**Duplicates merged**: 40 entries folded into 17 kept entries (clusters A-Q). Unique contributions preserved as "Cross-agent contributions" subsections.

---

## User-Directed Test Cases

### USER-1: Compound Staircase Modification
Rebuild E_GS(N) with Penrose back-reaction + Josephson-broken integrals + Bekenstein entropy constraint included self-consistently. Not "does mechanism X bridge 113 OOM?" but "what is epsilon(N_eq) in the full coupled system?"
- **Input**: s60_staircase_ext.npz, s60_penrose_superrad.npz, s60_rg_integrals.npz, s60_bekenstein_pw.npz
- **Output**: s61_compound_staircase.py/.npz/.png
- **Gate**: COMPOUND-STAIRCASE-61. PASS if epsilon differs from 0.046 by >10x. FAIL if ~0.046. INFO if 2-10x.

### USER-2: Heat Kernel a_2 from Milnor's Ricci Formula
Compute the TRUE Seeley-DeWitt a_2 from the local curvature integral on Jensen-deformed SU(3). NOT the PW spectral sum. Van den Dungen confirms: a_2 is GUARANTEED finite, computable from Milnor's formula.
- **Input**: canonical_constants.py, Jensen metric eigenvalues
- **Output**: s61_heat_kernel_a2.py/.npz
- **Gate**: HEAT-KERNEL-A2-61. PASS if a_2 gives H_0 in [60, 80] km/s/Mpc. FAIL if outside [40, 100]. INFO if H_0 well-defined but outside [60, 80].

### USER-3: Van den Dungen Transit Spectral Action (Paper 02)
Compute the spectral action ALONG the transit path using families of spectral triples. Include the d/dtau correction terms. This is the S38 paradigm shift computation that was requested 30+ times.
- **Input**: D_K(tau) eigenvalues at 50 tau points, canonical_constants.py
- **Output**: s61_transit_spectral_action.py/.npz/.png
- **Gate**: TRANSIT-SA-61. PASS if transit SA differs from static SA by >10%. FAIL if <1%. INFO if 1-10%.
- **Implementation**: See VDD-6

### USER-4: A-Tensor Correction to D_K
Van den Dungen flagged: product metric assumption may break when gauge connections are present. Compute the O'Neill A-tensor correction from SM gauge fields.
- **Input**: Jensen metric, gauge connection inner fluctuations
- **Output**: s61_a_tensor_correction.py/.npz
- **Gate**: A-TENSOR-61. PASS if correction <1% of D_K eigenvalues. FAIL if >10%. INFO if 1-10%.
- **Implementation**: See VDD-2

---

## Schwarzschild-Penrose Geometer (SP)

### SP-1: Local Heat Kernel a_2 from Jensen Metric Scalar Curvature
**Computation**: Compute the Seeley-DeWitt coefficient a_2(D_K^2) as a local curvature integral over Jensen-deformed SU(3), bypassing the divergent PW mode sum entirely. The scalar curvature R(tau) is analytically known from the structure constants of su(3) and the Jensen metric eigenvalues. The integral is over a compact manifold with smooth integrand -- finite by construction, no truncation needed. This is the SP geometric method specification for USER-2.
**Method**: (1) Compute Ricci tensor R_{ab}(tau) from structure constants and Jensen metric via Milnor's formula for left-invariant metrics on Lie groups. (2) Contract to scalar curvature R(tau) = sum_a g^{aa} R_{aa}. (3) Compute spin connection curvature F from the Riemann tensor of the Jensen metric. (4) Evaluate a_2 = (4pi)^{-4} * int_{SU(3)} tr_S(R/6 * id_S + F) * dvol_g, where dvol_g = Vol(SU(3),g(tau)) * omega (normalized Haar measure). (5) Extract a_2(tau) as an analytic function of tau -- should be a rational function of exponentials e^{k*tau}. (6) Compare with PW truncated sums at L = 1,...,7 to demonstrate the finite local integral vs divergent mode sum discrepancy.
**Input**: canonical_constants.py (structure constants C^a_{bc}, Jensen eigenvalues), Baptista Paper 13 eq 2.85 (metric ansatz), Paper 14 eq 2.85/2.88 (curvature formulas)
**Output**: s61_heat_kernel_a2_local.py, s61_heat_kernel_a2_local.npz (a_2(tau) at 100 tau points, R(tau), F(tau), Vol(tau), comparison with PW partial sums), s61_heat_kernel_a2_local.png
**Gate**: HEAT-KERNEL-A2-LOCAL-61. PASS if a_2(tau_fold) is finite and yields H_0 in [60, 80] km/s/Mpc. FAIL if H_0 outside [40, 100]. INFO if finite and well-defined but H_0 depends on additional parameters not yet fixed.
**Priority**: HIGH (SP review identifies this as "the single most important uncomputed quantity" -- Section 3.1 and Q1)
**Est. Cost**: CPU only, <1 min. Analytic formula evaluation, no eigenvalue computation needed.
**Paper Reference**: SP review Section 3.1 and Q1. Gilkey 1975 (a_2 formula). Milnor (curvature of left-invariant metrics). Baptista Paper 13 eq 2.85.
**Depends On**: none
**Cross-agent contributions**:
- VOL-10: Superfluid-vacuum formulation — vacuum energy from microscopic Hamiltonian directly (finite) vs summing zero-point energies (divergent), Paper 03 Section 3
- BAP-1: Lichnerowicz-Weitzenboeck identity D_K^2 = -nabla^2 + R/4 determines E; evaluate at 50 tau points in [0, 0.5]
- PHONON-1: PW divergence = analogue gravity UV catastrophe (Pillar I, Paper 01 Section 3.4); Strutinsky structurally inapplicable (no Fermi surface, no natural regulator); heat kernel IS the NCG density functional
- VDD-1: VdD Paper 01 factorization guarantees a_2 finite; Paper 06 Section 3.2 Seeley-DeWitt formula
- LANDAU-9: Milnor formula for R(tau) on left-invariant metrics; complement to USER-2
- SPEC-1: Lichnerowicz gives E=R/4, so a_2 = (4pi)^{-4}*(5R/12)*16*Vol(SU(3)); single closed-form number in seconds

### SP-2: Conformal Interpretation of PW Spectral Sum Divergence
**Computation**: Make precise the analogy between the PW spectral sum divergence (Tr|D_K| ~ L^{6.2}) and the divergence of total energy integrated over uncompactified Minkowski space. Test whether the heat kernel suppression factor exp(-lambda^2/Lambda^2) plays the role of the conformal factor Omega^2 in compactifying the PW sum.
**Method**: (1) From existing PW eigenvalue data at L = 0 through L = 7, compute partial zeta sums zeta_L(s) = sum_{lambda in PW level <= L} |lambda|^{-2s} for s = 1, 2, 3, 4, 5 (convergent regime). (2) Fit the L-dependence to extract the analytic continuation to s = -1/2 via Richardson extrapolation or Shanks transformation. (3) Compare the analytically continued value with SP-1 result for a_2. (4) If they agree up to a computable factor, the PW sum and local integral are related by "conformal compactification" of the spectral domain.
**Input**: s60_pw_h0_conv.npz (PW eigenvalues by level, divergence exponent 6.2), SP-1 output (local a_2)
**Output**: s61_pw_conformal_zeta.py, s61_pw_conformal_zeta.npz (zeta_L(s) at multiple s values, analytic continuation, ratio to local a_2), s61_pw_conformal_zeta.png
**Gate**: PW-CONFORMAL-ZETA-61. PASS if zeta-regularized sum agrees with local a_2 to <10%. FAIL if disagree by >100% or analytic continuation fails to converge. INFO if agree up to a computable factor (10-100% off).
**Priority**: MED (independent cross-check on USER-2/SP-1 heat kernel; conceptual bridge between divergent PW sum and finite geometric integral)
**Est. Cost**: CPU, ~5 min. Reprocessing existing eigenvalue data at multiple zeta exponents.
**Paper Reference**: SP review Section 3.2. Penrose conformal compactification (Paper 03). Minakshisundaram-Pleijel zeta function. Connes spectral zeta function.
**Depends On**: SP-1 (needs local a_2 for comparison target)
**Cross-agent contributions**:
- PHONON-11: r_2(L) = a_2(local)/a_2(PW,L) and r_4(L) at L=1..5; convergence classification: if r_2 -> 0 only local physical, if r_2 -> constant PW converges

### SP-3: Thouless Time vs Conformal Time Budget (GGE Thermalization Window)
**Computation**: Determine whether Josephson-broken RG integrals (delta_k = 0.328 from RG-INTEGRALS-60) have time to thermalize the GGE relic within the causal domain of the physical universe. The S56 coherence desert (tau in [0.08, 0.49]) established Josephson is dynamically inert during transit (Mach 2700). The S57 fragmentation showed all-or-nothing connectivity. The geometric question: is the Thouless time for the Josephson fabric shorter or longer than the conformal time between the BCS transition and the horizon re-entry?
**Method**: (1) From S55 conformal diagram data, extract conformal time eta(tau) at tau = 0.22 and at the particle horizon crossing. Compute Delta_eta_available = eta(tau_freeze) - eta(tau_BCS). (2) Compute Thouless time t_Th = hbar / E_J from the Josephson coupling (S56: E_J/H_min = 0.235 at tau = 0.388), or equivalently from the spectral gap lambda_1 of the CG(24) graph Laplacian. (3) From the coherence desert boundaries, compute the proper time spent in the desert. (4) Compare t_Th with Delta_eta_available. (5) Check whether S57 fragmentation (first-order at tau = 0.1048) further restricts the thermalization window.
**Input**: s55_conformal_diagram.npz (eta(tau), horizon radii, w_eff), s60_rg_integrals.npz (delta_k = 0.328), s57_percolation_cc.npz (fragmentation tau = 0.1048), canonical_constants.py
**Output**: s61_gge_therm_window.py, s61_gge_therm_window.npz (t_Th(tau), Delta_eta_available, ratio t_Th/Delta_eta, desert time budget, fragmentation restriction), s61_gge_therm_window.png
**Gate**: GGE-THERM-61. PASS if t_Th / Delta_eta > 10 (breaking irrelevant -- thermalization impossible within causal domain). FAIL if t_Th / Delta_eta < 0.1 (breaking thermalizes GGE, permanence lost). INFO if ratio in [0.1, 10] (marginal).
**Priority**: HIGH (determines whether the S60 RG integral breaking actually threatens GGE permanence or is causally inaccessible)
**Est. Cost**: CPU, <1 min. Uses existing data from S55, S56, S57, S60. Graph Laplacian is 24x24.
**Paper Reference**: SP review Section 3.3 and Q5. Penrose conformal diagram (Paper 03, S55). S56 coherence desert. S57 fragmentation.
**Depends On**: none (uses existing computed data)

### SP-4: Penrose Inequality Analog for BCS Sector
**Computation**: Test the Penrose inequality analog M_ADM >= sqrt(A/16pi) translated to the BCS framework: E_BCS >= C * sqrt(S_BCS), where C = sqrt(1/(16pi * G_eff)) and G_eff = 1/(16pi * a_2). Evaluate for the (0,0) sector (Bekenstein-saturated with S_max/S_Bek = 6.44) and all higher sectors. Determine whether the (0,0) saturation corresponds to extremality (dump point analog) or a holographic anomaly. Test two interpretations from the review: (1) holographic saturation = maximally dense information state, (2) confinement radius underestimate via R_vol = Vol(SU(3))^{1/8}/M_KK vs R = 1/M_KK.
**Method**: (1) From SP-1 output, obtain G_eff(tau_fold) = 1/(16pi * a_2(tau_fold)). (2) For each BCS sector (p,q), compute E_BCS and S_BCS from s60_bekenstein_pw.npz. (3) Evaluate Penrose inequality ratio E_BCS / (C * sqrt(S_BCS)) per sector. (4) Plot ratio vs sector size. (5) For (0,0), check whether E_BCS / sqrt(S_BCS) = C exactly (saturation = extremality). (6) Recompute Bekenstein bound using R_vol to test interpretation (2).
**Input**: s60_bekenstein_pw.npz (E_BCS, S_BCS per sector, Bekenstein ratio 6.44), s60_entangle_cg24.npz (area/bulk = 1.36e6), SP-1 output (a_2 for G_eff), canonical_constants.py (dump point: tau = 0.19, K = 0.535)
**Output**: s61_penrose_inequality_bcs.py, s61_penrose_inequality_bcs.npz (inequality ratio per sector, extremality test, R_vol correction, dump comparison), s61_penrose_inequality_bcs.png
**Gate**: PENROSE-INEQ-BCS-61. PASS if (0,0) saturates to <5% (extremal, dump analog). FAIL if violates by >2x with no resolution from either interpretation. INFO if holds without saturation (ratio > 1.05), or R_vol correction resolves Bekenstein excess.
**Priority**: MED (tests dump = extremal horizon identification from S49 against Bekenstein saturation from S60)
**Est. Cost**: CPU, <1 min. Algebraic from existing data.
**Paper Reference**: SP review Section 3.4 and Q4. Penrose inequality (Paper 05: M >= sqrt(A/16pi)). S49 dump = extremal horizon. S60 BEKENSTEIN-PW-60.
**Depends On**: SP-1 (needs a_2 for G_eff)

### SP-5: Alpha_crit = 55 Conformal Selection Rule
**Computation**: Determine whether there is a conformal invariance argument or physical principle that selects alpha < 55 (where the fold is a stable minimum via a_4 dominance) versus alpha > 55 (where a_2 dominance makes the fold a maximum). The two regimes see different parts of the Penrose-Rindler curvature decomposition: a_2 sees scalar curvature R (fold maximizes), a_4 sees the Gauss-Bonnet combination including |C|^2 (fold minimizes, per S49 WCH). Determine whether alpha_crit is a ratio of conformal anomaly coefficients in 8D, constituting a conformal selection of the UV completion.
**Method**: (1) Decompose the Riemann tensor at the fold into Weyl C_{abcd}, traceless Ricci S_{ab}, and scalar Lambda using known eigenvalues (|C|^2 = 0.386, |Ric|^2 = 0.5). (2) Express a_2 and a_4 in terms of these three Penrose-Rindler components using Gilkey coefficients for 8D: a_2 = c_R * int R * tr(id), a_4 = c_1 * int |C|^2 + c_2 * int |S|^2 + c_3 * int R^2 + cross terms. (3) Evaluate the ratio a_4/a_2 as a function of tau. (4) Identify what sets alpha_crit = 55 geometrically -- is it a_4(fold)/a_2(fold)? (5) Check if the 8D conformal anomaly provides a natural selection.
**Input**: s60_hessian_3d.npz (alpha_crit = 55, Hessian eigenvalues for a_2 and a_4), canonical_constants.py (curvature invariants at fold), Penrose-Rindler Paper 09 (curvature decomposition)
**Output**: s61_alpha_crit_conformal.py, s61_alpha_crit_conformal.npz (Penrose-Rindler decomposition at fold, conformal weights, alpha_crit geometric origin, ratio vs tau), s61_alpha_crit_conformal.png
**Gate**: ALPHA-CRIT-CONFORMAL-61. PASS if alpha_crit has conformal invariance origin (ratio of anomaly coefficients or universal SU(3) geometric constant). FAIL if alpha_crit is accidental (non-universal numerical coefficients). INFO if relates to known geometric ratio without clear physical selection.
**Priority**: MED (determines whether the fold-stable a_4 regime is physically selected by conformal symmetry)
**Est. Cost**: CPU, <5 min. Analytic decomposition with numerical verification.
**Paper Reference**: SP review Section 2 (HESSIAN-3D-60 assessment: "ALPHA-CRIT-SPECTRAL-61") and Q2. Penrose-Rindler (Paper 09). Gilkey 1975.
**Depends On**: SP-1 (needs explicit a_2 decomposition into curvature components)

### SP-6: Post-Superradiance State = Dump Point Identification
**Computation**: Test whether the terminal state of the analog Penrose process (alpha -> alpha_crit, all superradiant modes saturated at lambda_alpha = 0) is precisely the dump point (tau = 0.19, kappa = 0, T_H = 0). The Kerr analog: after maximal energy extraction (M - M_irr ~ 0.293M for maximal spin), the BH reaches the extremal limit. Here delta_F = 0.482 M_KK is O(1) -- does the post-spindown state have the same thermodynamic characterization (zero temperature, BPS saturation) as the dump?
**Method**: (1) From s60_penrose_superrad.npz, extract post-spindown Lagrange multipliers lambda_alpha and effective angular velocity Phi_7 at terminal state. (2) Compare terminal GGE with dump point GGE ((0,0) sector from s60_bekenstein_pw.npz). (3) Compute analog surface gravity kappa_analog = d(E_eff)/d(alpha)|_{alpha_crit} and verify kappa -> 0. (4) Check BPS bound E = |Q| as established for the dump in S49. (5) Compare extraction efficiency delta_F/E_total with the Kerr geometric bound 0.293.
**Input**: s60_penrose_superrad.npz (3 superradiant modes, alpha_crit, spindown time 5e-42 s, delta_F = 0.482 M_KK), s60_bekenstein_pw.npz ((0,0) sector BCS state), canonical_constants.py (dump point: tau = 0.19, K = 0.535, |C|^2 = 0.386, kappa = 0)
**Output**: s61_superrad_dump_id.py, s61_superrad_dump_id.npz (terminal state parameters, kappa_analog, BPS ratio, dump comparison table, extraction efficiency), s61_superrad_dump_id.png
**Gate**: SUPERRAD-DUMP-61. PASS if post-superradiance state matches dump point to <5% (kappa -> 0, BPS saturated, same GGE). FAIL if differs by >20% in any thermodynamic variable. INFO if partial match.
**Priority**: LOW (interpretive -- strengthens dump = extremal horizon identification, does not constrain new physics)
**Est. Cost**: CPU, <1 min. Reprocessing existing S60 data.
**Paper Reference**: SP review Q3. Paper 05 (Penrose process, M_irr^2 = A/16pi). S49 dump = extremal horizon (kappa = 0, T_H = 0, BPS).
**Depends On**: none (uses existing S60 data)

**Source files**: `sessions/archive/session-60/session-60-sp-collab.md`

---

## Hawking Theorist

### HAWK-1: Zeta-Function Regularization Cross-Check of a_2
**Computation**: Compute the spectral zeta function zeta_{D_K^2}(s) = sum_n lambda_n^{-2s} using PW eigenvalues at the fold (tau=0.190), analytically continue to s=3, and extract the residue Res(zeta, s=3) which gives a_2 by the Minakshisundaram-Pleijel theorem. Independent cross-check of the Gilkey-Seeley curvature integral (USER-2).
**Method**: (1) Compute zeta_{D_K^2}(s) for Re(s) > 4 from the known PW eigenvalues at L_max = 3,4,5,6. (2) Fit the analytic structure (poles at s = d/2, d/2-1, ...) using Pade approximants or Richardson extrapolation. (3) Extract the residue at s = 3 (= d/2 - 1 for d=8). (4) Cross-check: Res(zeta, s=4) = a_0 = Vol(SU(3)) * dim(Delta_8) / (4*pi)^4 (known analytically). The Minakshisundaram-Pleijel zeta function provides a regularization of the divergent PW sum independent of the heat kernel.
**Input**: `computations/s60_pw_h0_conv.npz` (eigenvalue lists at each L), `computations/canonical_constants.py` (SU(3) volume, dim(Delta_8) = 16)
**Output**: `computations/s61_zeta_regularization.py`, `computations/s61_zeta_regularization.npz`, `computations/s61_zeta_regularization.png`
**Gate**: ZETA-A2-61. PASS if Res(zeta, s=3) agrees with Gilkey-Seeley a_2 (USER-2) to <5%. FAIL if they disagree by >20% (systematic error in one method). INFO if USER-2 not yet computed (standalone result).
**Priority**: HIGH
**Est. Cost**: ~30 min CPU. PW eigenvalues already computed; zeta summation + analytic continuation is O(N_eigenvalues * N_s_points).
**Paper Reference**: Minakshisundaram-Pleijel (1949); Paper 37 (Traschen 2000) Section 4; Gilkey (1975) invariance theory. Collab Section 3C.
**Depends On**: USER-2 (for cross-check target, but computable independently)
**Cross-agent contributions**:
- BAP-3: 48 irreps at L<=7; PW sum converges as L^{8-4s}; Richardson extrapolation or Shanks transformation
- SPEC-2: Shanks/Pade/Richardson to s=3; third independent a_2 route

### HAWK-2: Thouless Time for GGE Thermalization on the Josephson Fabric
**Computation**: Compute the Thouless time t_Th = hbar / delta_E for the multi-cell Josephson-coupled BCS system, where delta_E is the many-body level spacing near the Fermi surface. Determine whether the GGE permanence survives the integral-breaking (delta_k = 0.33 from RG-INTEGRALS-60) on cosmological timescales.
**Method**: (1) Construct the N_cell Hilbert space (N_cell = 2,4,8) with Josephson coupling E_J between cells. (2) Diagonalize the many-body Hamiltonian H = sum_i H_BCS(i) + E_J * sum_{<ij>} Delta_i^dag Delta_j. (3) Extract the many-body level spacing delta_E near E_F. (4) Compute t_Th = hbar / delta_E. (5) For diffusive transport (system is NOT chaotic per S38 ORDERED diagnostics): t_Th(N) ~ N^2 / D where D = E_J * xi^2 / hbar. (6) Extrapolate to N_cell ~ 10^{80}. Compare t_Th to t_Hubble ~ 4.3e17 s and t_transit ~ 1/omega_tau. The thermodynamic limit question (does delta_k ~ 1/N_cells?) is decisive for the DM production mechanism.
**Input**: `computations/s60_rg_integrals.npz` (delta_k = 0.33, Josephson coupling), `computations/s59_page_curve.npz` (fabric topology), `computations/canonical_constants.py`
**Output**: `computations/s61_thouless_time.py`, `computations/s61_thouless_time.npz`, `computations/s61_thouless_time.png`
**Gate**: THOULESS-GGE-61. PASS if t_Th > 10^3 * t_transit (GGE survives transit, relic forms). FAIL if t_Th < t_transit (relic thermalizes before forming, DM mechanism must be reconsidered). INFO if t_Th / t_transit in [1, 10^3] (marginal regime requiring finer analysis).
**Priority**: HIGH
**Est. Cost**: ~1 hr GPU. ED of N_cell x 256 Hilbert space; N_cell=2 is 65,536 states (tractable); N_cell=4 requires truncation.
**Paper Reference**: Paper 39 (Harlow 2014) Section 2.3 (scrambling vs diffusion timescales); Paper 15 (Parker 1969) Section IV. Collab Section 3B.
**Depends On**: none (uses existing S60 data)

### HAWK-4: Back-Reaction Corrected Parker Spectrum
**Computation**: Solve the time-dependent Bogoliubov-de Gennes equation with self-consistent back-reaction. The mode occupation n_k(tau) feeds back into the effective potential V_eff(tau) that drives the transit, modifying subsequent particle creation. S38 found n_Bog = 0.999 per mode with 3.7% back-reaction. Test whether self-consistency preserves or alters this result.
**Method**: (1) Use the BdG Hamiltonian H_BdG(tau) with eigenvalues from D_K(tau). (2) At each tau step, compute the instantaneous Bogoliubov coefficients alpha_k(tau), beta_k(tau). (3) Compute the back-reaction energy E_br(tau) = sum_k omega_k |beta_k|^2. (4) Modify the transit velocity: d(tau)/dt' = d(tau)/dt * (1 - E_br / E_transit). (5) Iterate to self-consistency. (6) Extract the converged n_k^{(sc)} and compare to n_k^{(1)} = 0.999. Alternative method: solve the semiclassical equation G_mu_nu = 8*pi*G * <T_mu_nu>_ren (Paper 15 eq 4.12) in the KK context: d^2(tau)/dt^2 = -dV/d(tau) + (back-reaction from created pairs).
**Input**: `computations/s59_bogoliubov_coeff.npz` (one-pass Bogoliubov coefficients), `computations/s60_transplanckian_bogo.npz` (mode data), `computations/canonical_constants.py`
**Output**: `computations/s61_backreaction_parker.py`, `computations/s61_backreaction_parker.npz`, `computations/s61_backreaction_parker.png`
**Gate**: BACKREACTION-PARKER-61. PASS if n_Bog^{(sc)} in [0.95, 1.00] (back-reaction perturbative, S38 result survives). FAIL if n_Bog^{(sc)} < 0.5 (back-reaction quenches particle creation). INFO if n_Bog^{(sc)} in [0.5, 0.95] (moderate back-reaction, transit character changes).
**Priority**: MED
**Est. Cost**: ~2 hr GPU. Iterative BdG solve at ~50 tau points, convergence ~5 iterations; each iteration is one full spectrum solve.
**Paper Reference**: Paper 15 (Parker 1969) Section IV (back-reaction); Paper 19 (Ford 2021) Section 5 (semiclassical back-reaction review); Paper 05 (Hawking 1975) Section 3 (stress-energy renormalization). Collab Section 3E.
**Depends On**: none (uses existing S38/S59 data)

### HAWK-5: GSL-Timescape Formal Verification (Jensen Convexity Argument)
**Computation**: Verify that the convexity of S_spec(tau) guarantees Delta_S_gen > 0 under any spatial inhomogeneity in tau, via Jensen's inequality. S59 pre-computation (memory line 37) states "Convex S_spec => Jensen guarantees Delta_S_gen > 0 for any inhomogeneity. No thermodynamic closure." Formalize and verify explicitly. Carries forward the unfinished GSL-TIMESCAPE-60 gate.
**Method**: (1) Compute d^2 S_spec / d(tau)^2 at 100 tau points in [0, 0.25]. (2) Verify convexity: d^2 S_spec / d(tau)^2 > 0 everywhere. (3) Construct the Jensen bound: for any partition {tau_1, ..., tau_N} with weights w_i, sum_i w_i S_spec(tau_i) >= S_spec(sum_i w_i tau_i). (4) Compute the minimum excess entropy Delta_S = <S_spec> - S_spec(<tau>) for representative inhomogeneity amplitudes delta_tau/tau = {0.01, 0.1, 0.5}. (5) Verify that S_gen = S_spec + A/(4G_eff) is monotonically non-decreasing for each inhomogeneous configuration.
**Input**: `computations/s60_gsl_timescape.npz` (if populated), `computations/s60_sector_dim_reduct.npz` (tau variance), D_K eigenvalues at 100 tau points, `computations/canonical_constants.py`
**Output**: `computations/s61_gsl_timescape_jensen.py`, `computations/s61_gsl_timescape_jensen.npz`, `computations/s61_gsl_timescape_jensen.png`
**Gate**: GSL-TIMESCAPE-61. PASS if convexity holds at all tau and Jensen bound is positive (timescape closure confirmed on thermodynamic grounds -- GSL satisfied, no independent thermodynamic objection to timescape). FAIL if S_spec is non-convex in some interval (Jensen argument inapplicable, timescape thermodynamics remains open). INFO if convexity is marginal (d^2 S/d(tau)^2 ~ 0 at some tau, requiring higher-order analysis).
**Priority**: MED -- completes the unfinished W6-3 gate from S60
**Est. Cost**: ~30 min CPU. Eigenvalue sweeps already exist; second derivative is numerical differentiation.
**Paper Reference**: Paper 22 (Wald 1993) generalized second law; GSL-QTHEORY-46 (prior PASS, 35,983x margin); S59 memory (convexity pre-computation). Collab Section 3E and Q3.
**Depends On**: none

### HAWK-6: (0,0) Sector Bekenstein Saturation -- Physical Radius Determination
**Computation**: Determine whether the (0,0) sector Bekenstein saturation (S_vN/S_Bek = 1.21 from BEKENSTEIN-PW-60) is a physical holographic signal or an artifact of using R = 1/M_KK as the confinement radius. The Bekenstein bound S <= 2*pi*R*E assumes an asymptotically flat background; whether it applies to a BCS state on a compact fiber bundle is not established. The BCS wavefunction extends over the full SU(3) volume, not a ball of radius 1/M_KK.
**Method**: (1) Compute the diameter of SU(3) under the Jensen metric: d_J = max_{g1,g2 in SU(3)} dist_J(g1, g2). For the round metric this is pi; for the Jensen deformation, compute numerically. (2) Compute R_rms = sqrt(integral |psi_BCS|^2 r^2 dV / integral |psi_BCS|^2 dV) where r is geodesic distance from the identity. (3) Compute R_IPR from the inverse participation ratio of the BCS ground state on SU(3). (4) Recompute S_Bek = 2*pi*R_eff * |E_BCS| for each radius definition {1/M_KK, d_J, R_rms, R_IPR}. (5) Report the corrected S_vN/S_Bek ratio for each.
**Input**: `computations/s60_bekenstein_pw.npz` (S_vN, E_BCS per sector), `computations/canonical_constants.py` (Jensen metric parameters)
**Output**: `computations/s61_bekenstein_radius.py`, `computations/s61_bekenstein_radius.npz`
**Gate**: BEKENSTEIN-RADIUS-61. PASS if corrected S_vN/S_Bek < 1 for ALL sectors including (0,0) (no saturation, Bekenstein bound respected with correct radius). FAIL if S_vN/S_Bek > 1 persists with the physically correct radius (genuine holographic saturation -- first Bekenstein saturation in a non-gravitational system). INFO if the ratio is within [0.8, 1.2] (marginal, interpretation-dependent).
**Priority**: LOW
**Est. Cost**: ~20 min CPU. Geodesic computations on SU(3), no diagonalization needed.
**Paper Reference**: Paper 11 (Bekenstein 1981) universal entropy bound; Paper 07 (Chamseddine-Connes 1996) spectral action on compact groups. Collab Section 2 (BEKENSTEIN-PW-60 self-correction) and Q2.
**Depends On**: none (uses existing BEKENSTEIN-PW-60 data)
**Cross-agent contributions**:
- TESLA-4: BCS coherence length xi = hbar*v_F/(pi*Delta); Fermi velocity from Dirac spectrum dispersion in (0,0) sector near gap edge

### HAWK-7: Volovik-Sakharov G_eff for Island Formula Rescue
**Computation**: Recompute the effective Newton constant G_eff using the Volovik-Sakharov trace-log formula G_eff^{-1} = (1/48*pi) * sum_n ln(Lambda^2/lambda_n^2) instead of the Seeley-DeWitt a_2 coefficient. Test whether this alternative G_eff changes the area/bulk ratio in ENTANGLE-CG24-60 sufficiently to allow a quantum extremal surface. Sole identified escape route for the island mechanism (collab Section 2, ENTANGLE-CG24-60 assessment).
**Method**: (1) Compute G_VS^{-1} = (1/48*pi) * sum_{n=1}^{N_PW} ln(Lambda^2/lambda_n^2) at the fold, with Lambda = M_KK. (2) Check convergence as L_max increases (the logarithm regularizes the UV divergence that afflicts the raw PW sum). (3) Form the ratio G_VS / G_SDW where G_SDW is from the a_2 coefficient (USER-2). (4) Recompute Area/Bulk using G_VS in the area term A(partial I)/(4*G_VS). (5) Determine if any bipartition of CG(24) has Area/Bulk < 1 (required for a nontrivial QES).
**Input**: `computations/s60_entangle_cg24.npz` (bipartition data, area-law fit, s_0 = 0.180), `computations/s60_pw_h0_conv.npz` (PW eigenvalues), `computations/canonical_constants.py`
**Output**: `computations/s61_volovik_sakharov_geff.py`, `computations/s61_volovik_sakharov_geff.npz`
**Gate**: VS-GEFF-ISLAND-61. PASS if G_VS differs from G_SDW by <1 OOM and Area/Bulk remains >> 1 (island permanently excluded). FAIL if G_VS is 6+ OOM larger, making Area/Bulk ~ 1 (island formula becomes active, entanglement channel reopens). INFO if G_VS is 2-5 OOM larger (partial reduction, requires finer bipartition analysis).
**Priority**: LOW -- sole identified escape route for ENTANGLE-CG24-60
**Est. Cost**: ~20 min CPU. Log-sum over known eigenvalues, no new diagonalization.
**Paper Reference**: Paper 21 (AHMST 2020) island formula; Paper 24 (Engelhardt-Wall 2014) quantum extremal surface; Volovik (2003) Universe in a Helium Droplet Ch 10 (Sakharov induced gravity). Collab Section 2 (ENTANGLE-CG24-60 assessment).
**Depends On**: USER-2 (for G_SDW cross-comparison)

### HAWK-8: Extremal GGE Quantum Stability (lambda_min = 0)
**Computation**: Test the stability of the marginal GGE state (lambda_min = 0) reached after the superradiance analog spindown (PENROSE-SUPERRAD-60, alpha -> alpha_crit = 0.523). In black hole physics, extremal Kerr (a = M) has a near-horizon AdS_2 x S^2 throat with distinct quantum properties. Determine whether the framework's "extremal" GGE has analogous enhanced fluctuations or a phase transition at the marginal point.
**Method**: (1) Construct the GGE density matrix rho_GGE = exp(-sum_k lambda_k I_k) / Z with one lambda set to 0. (2) Compute the variance <(delta I_min)^2> = d^2 ln Z / d(lambda_min)^2 evaluated at lambda_min = 0. (3) Compare to the mean: <I_min>. If <(delta I_min)^2> / <I_min>^2 >> 1, the integral is not self-averaging and the GGE is unstable. (4) Compute the susceptibility chi = -d<I_min>/d(lambda_min) at lambda_min = 0. Divergent chi signals a phase transition at the marginal point.
**Input**: `computations/s60_penrose_superrad.npz` (alpha_crit, lambda values, spindown timescale), `computations/s60_andreev_omega.npz`, GGE lambda_k values from S39 ({1.459, 2.771, 6.007}), `computations/canonical_constants.py`
**Output**: `computations/s61_extremal_gge.py`, `computations/s61_extremal_gge.npz`
**Gate**: EXTREMAL-GGE-61. PASS if fluctuations are O(1) and chi is finite (marginal GGE is stable, superradiance endpoint well-defined). FAIL if chi diverges (phase transition at lambda_min = 0, superradiance triggers structural change in the post-transit state). INFO if fluctuations are large but chi finite (marginal but stable).
**Priority**: LOW
**Est. Cost**: ~30 min CPU. GGE partition function derivatives are analytic for 8 modes; no diagonalization.
**Paper Reference**: Paper 03 (Bardeen-Carter-Hawking 1973) Section 5 (Penrose process endpoint); PENROSE-SUPERRAD-60 (t_spindown = 5e-42 s, alpha_crit = 0.523). Collab Q5.
**Depends On**: none (uses existing PENROSE-SUPERRAD-60 data)

### HAWK-9: Heat Kernel a_2 Tau Derivative for Transit Spectral Action
**Computation**: Compute d(a_2)/d(tau) along the transit trajectory tau in [0, 0.25]. The Gilkey-Seeley a_2 involves the Ricci scalar R(g_Jensen(tau)), which varies with tau. The derivative d(a_2)/d(tau) determines whether the gravitational coupling G_eff(tau) changes during transit, and its sign determines whether gravity strengthens or weakens as the fiber geometry deforms. Feeds directly into USER-3 (transit spectral action).
**Method**: (1) Compute R(g_Jensen(tau)) at 50 tau points in [0, 0.25] using the analytic Milnor-type formula from Paper 13 for the Ricci scalar of left-invariant metrics on SU(3). (2) Integrate: a_2(tau) = (4*pi)^{-4} * integral_{SU(3)} [R(tau)/6 * 16] * sqrt(g(tau)) * d^8x. The volume form sqrt(g(tau)) depends on tau through the Jensen deformation. (3) Compute the tau-derivative numerically and analytically (if the Ricci scalar formula permits closed form). (4) Identify any zeros or sign changes of d(a_2)/d(tau) -- these mark stationary points of the gravitational coupling.
**Input**: Jensen metric eigenvalues as function of tau (from `computations/canonical_constants.py` or Paper 13 formulas)
**Output**: `computations/s61_a2_tau_derivative.py`, `computations/s61_a2_tau_derivative.npz`, `computations/s61_a2_tau_derivative.png`
**Gate**: A2-TRANSIT-61. PASS if d(a_2)/d(tau) is monotonic and nonzero (gravitational coupling evolves smoothly during transit, supporting USER-3). FAIL if a_2(tau) is constant in tau (no gravitational evolution, transit spectral action = static spectral action). INFO if d(a_2)/d(tau) changes sign (non-monotonic G_eff evolution, requiring phase-by-phase analysis in USER-3).
**Priority**: HIGH (feeds USER-2 and USER-3)
**Est. Cost**: ~1 hr CPU. Ricci scalar computation at 50 tau points; analytic if using Milnor formula for left-invariant metrics.
**Paper Reference**: Paper 07 (Chamseddine-Connes 1996) spectral action; Paper 37 (Traschen 2000) heat kernel on group manifolds; Paper 13 (Baptista) Jensen metric parameterization. Collab Section 3A.
**Depends On**: USER-2 (for a_2 normalization at the fold)

**Source files**: `sessions/archive/session-60/session-60-hawking-collab.md`

---

## Volovik Superfluid Universe Theorist

### VOL-2: GGE Thermalization via Thouless Time (GGE-THERM-61)
**Computation**: Compute the Thouless time t_Th = hbar/E_Th for the Josephson fabric at N_cells = 2, 4, 8, 16, 32. Compare to the transit timescale omega_tau^{-1} = 1/8.27 (S38 units). E_Th ~ E_J (a/L)^2 where a is the cell spacing and L = N^{1/3} a is the system size. The 3He-B expectation is FAIL (E_J = 655 M_KK >> Delta, so thermalization is fast). If t_Th >> t_transit at N_cells = 32, the GGE survives for the bulk. 3He-B analog: spin diffusion t_D ~ L^2/D where D ~ v_F * l_mfp.
**Method**: Thouless energy scaling E_Th(N) = E_J / N^{2/3} for d=3. Compare t_Th(N) = 1/E_Th(N) to omega_tau^{-1}. Also compute the Fermi golden rule quasiparticle scattering rate Gamma_qp from the Josephson coupling to cross-check.
**Input**: E_J = 655 M_KK (S55), omega_tau = 8.27 (S38), s60_rg_integrals.npz (delta_k = 0.33 at N=2), canonical_constants.py
**Output**: s61_gge_therm.py/.npz/.png (t_Th vs t_transit for N=2..32, Gamma_qp, thermalization verdict)
**Gate**: GGE-THERM-61. PASS if t_Th > 10 * t_transit at N=32 (GGE survives). FAIL if t_Th < 0.1 * t_transit (GGE thermalizes). INFO otherwise.
**Priority**: HIGH (critical for DM production mechanism -- if GGE thermalizes, framework loses its unique DM channel)
**Est. Cost**: CPU only, minutes. Scaling formula evaluation.
**Paper Reference**: Volovik Paper 01 Section II.G (equilibrium theorem), Paper 25 Section 3 (de Sitter thermodynamics). Collab Section 3.3, Addendum A Section V.2. 3He-B analog: spin diffusion timescale.
**Depends On**: RG-INTEGRALS-60 (completed S60, delta_k = 0.33). Couples to TESLA-1 (same gate, different method -- spectral form factor vs scaling formula). Independent of USER-1.

### VOL-4: Dipolar Thermalization on Fabric (DIPOLAR-THERMALIZATION-61)
**Computation**: Compute the damping rate of the Leggett mode (m_G = 0.070 M_KK, S49 DIPOLAR-CATALOG-49) in the Josephson fabric. In 3He-B, the Leggett mode thermalizes through spin diffusion on timescale t_D ~ L^2/D. The question: does the Leggett mode thermalize on the fabric while the BCS gap survives? If so, the framework retains BCS structure but loses the Leggett mode as a low-energy degree of freedom.
**Method**: Fermi golden rule for Leggett mode decay into Josephson-coupled quasiparticle pairs. Rate Gamma_L = (2pi/hbar) |<f|V_J|i>|^2 rho(E_L) where V_J is the Josephson coupling and rho is the 2-cell density of states at E_L = m_G = 0.070 M_KK. Compare to the S50 single-cell result (Q = 6.7e5, Beliaev forbidden).
**Input**: m_G = 0.070 M_KK (S49), E_J = 655 M_KK (S55), BCS spectrum from canonical_constants.py, LEGGETT-DAMPING-50 baseline
**Output**: s61_dipolar_thermalization.py/.npz (Gamma_L on fabric, Q factor, comparison to single-cell)
**Gate**: DIPOLAR-THERM-61. INFO (characterization of Leggett mode lifetime in fabric).
**Priority**: MED
**Est. Cost**: CPU only, minutes. Golden rule matrix element evaluation.
**Paper Reference**: Volovik Paper 10 (Josephson arrays), Paper 19 (Leggett mode). Addendum A Section V.5. 3He-B analog: spin diffusion damping of Leggett frequency.
**Depends On**: LEGGETT-DAMPING-50 (completed S50), DIPOLAR-CATALOG-49 (completed S49). Independent of VOL-2.

### VOL-6: Bekenstein Saturation through de Sitter Thermodynamics (BEKENSTEIN-HOLOGRAPHIC-61)
**Computation**: BEKENSTEIN-PW-60 found S_max/S_Bek = 6.44 for the (0,0) sector, exceeding the Bekenstein bound. Evaluate whether this is a genuine holographic saturation or an artifact of the effective confinement radius. Use the de Sitter thermodynamic framework (Paper 11, Paper 35) to compute the de Sitter entropy S_dS at the (0,0) sector's energy scale and compare to S_max. Apply the first law of de Sitter thermodynamics (Paper 11 eq.2.7).
**Method**: Compute S_dS = pi * R_H^2 / G_eff where R_H = sqrt(3/Lambda_eff). Use G_eff from SAKHAROV-GN-44 (G_Sak/G_obs = 2.29). In the two-fluid description (Paper 35), separate the vacuum energy into normal and superfluid components. Test whether the superfluid fraction f_s = rho_s / rho determines the saturation ratio.
**Input**: BEKENSTEIN-PW-60 results (S_max/S_Bek = 6.44), SAKHAROV-GN-44 (G_Sak), s60_staircase_ext.npz, canonical_constants.py
**Output**: s61_bekenstein_holographic.py/.npz (S_dS, comparison to S_max and S_Bek, first law check)
**Gate**: BEKENSTEIN-HOLOGRAPHIC-61. INFO (characterization). Subsidiary: PASS if S_dS / S_BCS = O(1) (scales match). FAIL if >> 1 or << 1.
**Priority**: LOW
**Est. Cost**: CPU only, seconds. Algebraic.
**Paper Reference**: Volovik Paper 11 (de Sitter first law, eq.2.7), Paper 35 (Luttinger-Kohn two-fluid de Sitter). Collab Q3.
**Depends On**: BEKENSTEIN-PW-60 (completed S60), SAKHAROV-GN-44 (completed S44).

### VOL-7: J-Breaking Mechanism Catalog for Baryogenesis (J-BREAKING-CATALOG-61)
**Computation**: The W_J wall (LEPTO-CP-60, ETA-B-52) forces all interaction matrices from D_K to be real, giving epsilon_1 = 0 exactly. CP violation requires T-breaking. Catalog all mechanisms that could break [J, D_K] = 0 at finite tau, with quantitative estimates of CP violation strength. In 3He-B, T-breaking comes from rotation (angular momentum) or magnetic field (Zeeman). Framework analogs: (E1) UV completion beyond NCG axioms, (E2) twisted spectral triple (Connes-Devastato-Lizzi-Martinetti), (E3) cosmological CPT violation during transit (Berry phase of D_K eigenstates), (E4) gravitational CP anomaly (Paper 34).
**Method**: For E3 (most promising): compute [J, D_K(tau(t))] during the quench. If the Berry phase introduces an imaginary component, J-breaking is dynamical. For E2: evaluate whether the twisted order-one condition produces nonzero Im(M_R). For each mechanism, evaluate epsilon_1 = Im(sum M_ij) / |sum M_ij| and estimate eta_B. Compare to observed eta_B ~ 6e-10.
**Input**: D_K(tau) eigenvalues and eigenvectors at 50 tau points, J operator, LEPTO-CP-60 (epsilon_1 = 0 exact), canonical_constants.py
**Output**: s61_j_breaking_catalog.py/.npz/.md (mechanism table, epsilon_1 per mechanism, eta_B estimate)
**Gate**: J-BREAKING-CATALOG-61. PASS if any mechanism gives eta_B within 3 orders of 6e-10. FAIL if all mechanisms give eta_B < 10^{-20}. INFO otherwise.
**Priority**: MED (baryogenesis requires J-breaking; all current channels CLOSED -- Addendum A Prediction 3)
**Est. Cost**: Minutes for E3 (Berry phase computation). E2 requires new operator construction.
**Paper Reference**: Volovik Paper 05 Section 3 (T-breaking in topological superfluids), Paper 08 (chiral anomaly baryogenesis -- inapplicable but sets scale), Paper 34 (gravitational anomaly). Collab Q5, Addendum A Prediction 3.
**Depends On**: LEPTO-CP-60 (completed S60), ETA-B-52 (completed S52). Couples to TESLA-3 (parallel dynamic J-breaking computation).

### VOL-8: Multi-Pair Q-Theory at Finite N (MULTI-PAIR-QTHEORY-61)
**Computation**: The CC problem reduces to computing whether Lambda_residual oscillation amplitude decreases with N (approaching 3He thermodynamic limit) or remains O(1) (discrete q-theory locked). STAIRCASE-EXT-60 showed Lambda_residual oscillates with N (0.360, 0.293, 0.368 at N=1,2,3) -- shell-filling, not convergence. Extend the staircase to N = 5, 6, 7, 8 and determine the asymptotic envelope. Also compute the continuous equilibrium point N_eq where d(epsilon)/dN = 0 at each PW level.
**Method**: Exact diagonalization of the N-pair BCS Hamiltonian in the 8-mode system for N = 1..8. Extract E_GS(N), Lambda_residual(N), and N_eq from quadratic interpolation. At N=4 (half-filling), max Fock space dim = C(8,4) = 70.
**Input**: BCS Hamiltonian from canonical_constants.py, STAIRCASE-EXT-60 results (N = 0..4)
**Output**: s61_multi_pair_qtheory.py/.npz/.png (E_GS(N), Lambda(N), oscillation analysis, N_eq)
**Gate**: MULTI-PAIR-QTHEORY-61. PASS if oscillation amplitude decreases as 1/N or faster (CC solvable at large N). FAIL if amplitude remains O(1) at N = 8 (CC locked by discreteness). INFO if non-monotone behavior.
**Priority**: HIGH (directly addresses the CC problem through q-theory -- Addendum A Predictions 1 and 5)
**Est. Cost**: CPU, minutes. Exact diag in Fock space of dimension C(8,N) per N.
**Paper Reference**: Volovik Paper 13 eq.3.6 (q-theory self-tuning), Paper 14 Section V (discrete q-variable). Addendum A Predictions 1, 5. Q-VARIABLE-59.
**Depends On**: STAIRCASE-EXT-60 (completed S60). Strongly couples to LANDAU-1 (GL-STAIRCASE-61, which includes CHI-Q).

### VOL-9: Inheritance Chain CFL Correspondence Count (CFL-CORRESPONDENCE-61)
**Computation**: Addendum B identified the CFL phase of dense QCD as the most direct theoretical descendant of the substrate (2 compositing levels vs 5 for 3He-B), scoring 5/6 on the condensate ranking. The inheritance framing predicts CFL should show MORE correspondences than 3He-B (22); the analogy framing predicts the SAME number. Systematically evaluate the 22-correspondence scorecard for the CFL phase using published CFL literature (Alford-Rajagopal-Wilczek 1999, Alford 2008 review). This is the discriminating test between inheritance and analogy (Addendum B Section B4).
**Method**: For each of the 22 framework-3He-B correspondences, determine whether the CFL phase exhibits the same correspondence. Score as CONFIRMED / PARTIAL / ABSENT. Compare total to 3He-B's 14 CONFIRMED.
**Input**: 22-correspondence scorecard (framework-3HeB-comparison.md Section VI), CFL review literature, Volovik Paper 05 (topological classification of CFL)
**Output**: s61_cfl_correspondence.md (scorecard, comparison, inheritance vs analogy verdict)
**Gate**: CFL-CORRESPONDENCE-61. INFO (theoretical evaluation, not computation sensu stricto). Report CFL correspondence count and whether it exceeds 3He-B count (inheritance prediction) or matches (analogy prediction).
**Priority**: LOW (theoretical, not computationally gated)
**Est. Cost**: Literature evaluation, no GPU.
**Paper Reference**: Volovik Paper 05 Table 1, Paper 10. Addendum B Sections B3 (condensate ranking), B4 (testable consequences).
**Depends On**: None. Independent of all other VOL entries.

**Source files**: `sessions/archive/session-60/session-60-vol-collab.md`, `sessions/archive/session-60/framework-3HeB-comparison.md` (Addenda A & B)

---

## Baptista Spacetime Analyst

### BAP-2: Off-Jensen Screening Ratio on 2D Volume-Preserving Surface
**Computation**: Compute the screening ratio $R_{\mathrm{screen}}(\sigma, \delta_1) = |\delta N/N| / |\delta\alpha/\alpha|$ on the 2D volume-preserving surface within the 3-parameter metric space $(\lambda_1, \lambda_2, \lambda_3)$. SECTOR-DIM-REDUCT-60 established $R_{\mathrm{screen}} = 16.1$ on the Jensen line (a fold constant, $\delta\tau$ cancels). Determine whether any off-Jensen direction achieves $R_{\mathrm{screen}} > 10^4$, which would allow timescape-viable decoupling of $G$ and $\alpha$.
**Method**: Use the general 3-parameter left-invariant metric from Paper 13 eq 2.37 with volume-preserving constraint $\lambda_1 \lambda_2^3 \lambda_3^4 = 1$. This gives a 2D parameter surface. At each point, compute $da_2/d\lambda_i$ (mode count proxy for $\delta N/N$) and the clock coefficient $d\alpha/d\lambda_i$ (fine-structure constant dependence on internal curvature). Take the ratio. Scan a grid of at least 100x100 points. Repurpose HESSIAN-3D-60 eigenvalue data at the 125 existing grid points.
**Input**: s60_hessian_3d.npz (12,880 eigenvalues at 125 grid points in 3D), s60_sector_dim_reduct.npz (Jensen-line screening result $R_{\mathrm{screen}} = 16.1$), canonical_constants.py
**Output**: s61_offjensen_screening.py, s61_offjensen_screening.npz (containing $R_{\mathrm{screen}}(\sigma, \delta_1)$ surface, gradient vectors, maximum $R_{\mathrm{screen}}$ and location), s61_offjensen_screening.png (contour plot)
**Gate**: OFFJ-SCREEN-61. PASS if $\max(R_{\mathrm{screen}}) > 10^4$. FAIL if $\max(R_{\mathrm{screen}}) < 100$ everywhere. INFO if between 100 and $10^4$.
**Priority**: HIGH (determines whether timescape mechanism survives off-Jensen; only escape route identified in Section 1.4)
**Est. Cost**: Moderate -- eigenvalue diagonalization at 10,000 grid points. GPU ~minutes. Can reuse s60_hessian_3d.npz for 125 existing points.
**Paper Reference**: Baptista Paper 13 eq 2.37 (3-parameter metric), Paper 15 eq 3.70 (general scalar curvature). Collab review Section 3.2 and Q3.
**Depends On**: none (s60_hessian_3d.npz already exists)

### BAP-4: Lichnerowicz Gap vs Sectional Curvature at Domain Wall
**Computation**: Investigate the near-coincidence ($\Delta\tau = 0.0025$) between the Lichnerowicz spectral gap minimum ($\lambda_{\min}^{\mathrm{Lich}} = 0.3150$ at $\tau = 0.116$) and the domain wall $\tau_{DW} = 0.1135$ (sectional curvature sign change $K_{\mathrm{sec}}^{\min} = 0$). Test whether a geometric mechanism links Lichnerowicz spectral gaps to sectional curvature transitions.
**Method**: Refine the tau grid near $\tau_{DW}$ to $\Delta\tau = 0.0001$ (200 points in $[0.10, 0.12]$). Track all 31 TT eigenvalues AND the minimum sectional curvature $K_{\mathrm{sec}}^{\min}(\tau)$ simultaneously. Fit the gap minimum location and the $K_{\mathrm{sec}}^{\min} = 0$ crossing independently. Test whether $\partial\lambda_{\min}/\partial K_{\mathrm{sec}}^{\min} > 0$ (monotonic relationship). The HARD(su2) mode (degeneracy 5) carries the minimum -- track it specifically.
**Input**: s60_lichnerowicz_dw.npz (31 TT eigenvalues at 41 tau points), Jensen metric curvature formulas from Paper 13 eq 2.40
**Output**: s61_lichnerowicz_kmin.py, s61_lichnerowicz_kmin.npz (refined gap profile, $K_{\mathrm{sec}}^{\min}(\tau)$, cross-correlation, gap-curvature derivative), s61_lichnerowicz_kmin.png
**Gate**: LICH-KSEC-61. PASS if $|\tau_{\mathrm{gap\,min}} - \tau_{DW}| < 0.001$ on refined grid (geometric connection confirmed). FAIL if $> 0.01$ (coincidence). INFO if between 0.001 and 0.01.
**Priority**: MED (structural geometry result, permanent if confirmed; extends Lauret Paper 28)
**Est. Cost**: Low -- 31x31 matrix diagonalization at 200 tau points. CPU seconds.
**Paper Reference**: Baptista Paper 28 (Lauret G-instability of Einstein metrics), S59 RICCI-DW-59. Collab review Section 3.4 and Q4.
**Depends On**: none

### BAP-5: PW Data Audit -- (1,2) Irrep Contamination Scope
**Computation**: Determine which S27-S60 results are contaminated by the missing $(1,2)$ irrep in the S44 eigenvalue data. The missing contribution is $a_2 = 87{,}376$, which is 54% of the incomplete total. Classify every computation that used full PW spectral sums as SAFE (singlet-only or per-sector, unaffected) or CONTAMINATED (used cross-sector PW sums).
**Method**: Inventory all computation scripts S27-S60 that load s44_dos_tau.npz or related eigenvalue data. For each, determine whether it uses (a) singlet $(0,0)$ sector only (SAFE), (b) individual sector results that never sum across sectors (SAFE), or (c) full PW spectral sums $\sum_{(p,q)} \dim(p,q)^2 \cdot f(\lambda_i^{(p,q)})$ (CONTAMINATED). For CONTAMINATED results, quantify the fractional correction from including $(1,2)$.
**Input**: s44_dos_tau.npz, s60_pw_h0_conv.npz (corrected $N(L=3) = 4.859$), s60_a4_trace.npz, all computation scripts S27-S60 referencing eigenvalue data
**Output**: s61_pw_audit.md (table: script name, SAFE/CONTAMINATED status, impact magnitude), s61_pw_audit.py (automated scanner)
**Gate**: PW-AUDIT-61. INFO (audit -- no pass/fail; contaminated results flagged for recomputation or retraction).
**Priority**: HIGH (data integrity -- must know which prior results stand before S61 computations build on them)
**Est. Cost**: Low -- file scanning and inventory, no physics computation. CPU seconds.
**Paper Reference**: PW-H0-CONV-60 (divergence discovery, missing irrep identification). Collab review Section 2.1.
**Depends On**: none

### BAP-6: Proper Heat Kernel Ratio a_4/a_2 for Higgs Mass
**Computation**: Compute the ratio of true Seeley-DeWitt coefficients $a_4^{\mathrm{Gilkey}} / a_2^{\mathrm{Gilkey}}$ from local curvature integrals. A4-TRACE-60 found $N_{a_4}/N_{a_2} = 1.823$ from truncated PW sums, giving a 35% Higgs mass shift ($\sqrt{1.823} = 1.35$). Determine whether the proper heat kernel ratio confirms or overturns this systematic.
**Method**: Extend SP-1 method to compute $a_4(D_K^2)$ from the Gilkey $a_4$ formula, which involves $R^2$, $R_{\mu\nu}R^{\mu\nu}$, $R_{\mu\nu\rho\sigma}R^{\mu\nu\rho\sigma}$, and $\nabla^2 R$ terms. All curvature components are known analytically from Paper 15 eq 3.70 for the Jensen metric. Integrate over SU(3). Compare $a_4^{\mathrm{Gilkey}}/a_2^{\mathrm{Gilkey}}$ against the truncated PW ratio 1.823 from s60_a4_trace.npz.
**Input**: s60_a4_trace.npz (PW ratio benchmark $N_{a_4}/N_{a_2} = 1.823$), SP-1 output ($a_2^{\mathrm{Gilkey}}$), Paper 15 curvature tensors, canonical_constants.py
**Output**: s61_heat_kernel_a4.py, s61_heat_kernel_a4.npz (containing $a_4^{\mathrm{Gilkey}}(\tau)$, ratio $a_4/a_2$, derived Higgs mass correction factor)
**Gate**: HK-RATIO-61. PASS if $|a_4^{\mathrm{Gilkey}}/a_2^{\mathrm{Gilkey}} - 1.823| / 1.823 < 0.1$ (PW ratio confirmed within 10%). FAIL if ratio differs by >50%. INFO if 10-50%.
**Priority**: MED (resolves Higgs mass systematic from trace factor non-cancellation)
**Est. Cost**: Moderate -- $a_4$ involves fourth-order curvature invariants. Analytic but lengthy. CPU minutes.
**Paper Reference**: Baptista Paper 19 eq 2.14-2.16, Gilkey 1975 ($a_4$ formula). Collab review Section 2.3.
**Depends On**: SP-1 (need $a_2^{\mathrm{Gilkey}}$ method and validation first)

### BAP-8: Pati-Salam Spectral Action Regime at GUT Scale
**Computation**: Determine the effective $\alpha = f_2 \Lambda^2 / f_0$ in the spectral Pati-Salam model (Paper 23) at the GUT unification scale $\Lambda_{\mathrm{GUT}} \sim 10^{16}$ GeV. Classify whether standard NCG particle physics predictions are in the mode-counting or topological regime relative to $\alpha_{\mathrm{crit}} = 55$. This contextualizes the HESSIAN-3D-60 regime transition.
**Method**: Extract the test function moments $f_0$, $f_2$ from the spectral action literature (Chamseddine-Connes-van Suijlekom, Paper 23). Evaluate $\alpha$ at $\Lambda = \Lambda_{\mathrm{GUT}}$. The standard heat kernel cutoff $f(x) = e^{-x}$ gives $f_0 = 1$, $f_2 = 1$, so $\alpha = \Lambda^2$, but physical cutoff functions may differ. Check whether the Higgs mass prediction ($\sim 170$ GeV pre-RG) corresponds to $\alpha > 55$ or $\alpha < 55$.
**Input**: s60_hessian_3d.npz, Paper 23 (spectral Pati-Salam parameters), canonical_constants.py
**Output**: s61_patisalam_regime.py, s61_patisalam_regime.npz
**Gate**: PS-REGIME-61. INFO (classification -- determines which regime standard NCG operates in, contextualizes $\alpha_{\mathrm{crit}} = 55$).
**Priority**: LOW (interpretive context; does not directly constrain framework)
**Est. Cost**: Minimal -- literature extraction + arithmetic. CPU seconds.
**Paper Reference**: Baptista Paper 23 (spectral Pati-Salam). Collab review Section 1.3 and Q5.
**Depends On**: none

**Source files**: `sessions/archive/session-60/session-60-bap-collab.md`


---

## Tesla Resonance

### TESLA-1: Thouless Time from Fabric Spectral Form Factor
**Computation**: Compute the Thouless energy E_Th and Thouless time t_Th of the 32-cell Josephson fabric. Compare t_Th / t_transit to determine whether the GGE survives or thermalizes during the transit.
**Method**: Diagonalize the full fabric Hamiltonian (BCS + Josephson on CG(24) graph with degree 6). Compute the spectral form factor K(t) = |Tr(e^{-iHt})|^2 / |Tr(1)|^2. Extract t_Th from the ramp-plateau transition in K(t). Cross-check against diffusion estimate: D ~ E_J * a^2 / hbar, t_Th ~ L^2 / D where L ~ 32^{1/3} * a. Rough estimate gives t_Th / t_transit ~ 14,000.
**Input**: s60_rg_integrals.npz (E_J = 3.4 M_KK, delta_k = 0.328), s60_pair_transfer.npz, canonical_constants.py
**Output**: s61_thouless_time.py/.npz/.png (K(t) plot, t_Th extraction, t_Th/t_transit ratio)
**Gate**: GGE-THERM-61. PASS if t_Th / t_transit > 100 (GGE survives). FAIL if t_Th / t_transit < 1 (GGE thermalizes). INFO if ratio in [1, 100].
**Priority**: HIGH — determines whether the DM production mechanism (permanent non-thermal GGE relic) survives fabric coupling
**Est. Cost**: ~minutes CPU. 32-cell Fock space is 2^32 but truncated to pair sector (binomial(32,N_pair)). At N_pair=1 per cell, Hilbert space ~ 32 choose 8 = 10^6 — tractable.
**Paper Reference**: Superfluid 3He textural dynamics (Paper 09/10 in Tesla library), Kibble-Zurek mechanism (Paper 24). Spectral form factor: standard RMT diagnostic.
**Depends On**: USER-1 (compound staircase defines the fabric Hamiltonian parameters)
**Cross-agent contributions**:
- QA-2: 2-cell (dim=120) and 4-cell systems; scaling t_Th(N_cells); Lanczos for 4-cell
- LANDAU-2: P=+1 sector 64 states; unfolded SFF; Claeys estimate t_Th ~ t_H / (g_eff * delta_k)^2 ~ 120 * t_H

### TESLA-3: Dynamic J-Symmetry Breaking During Transit
**Computation**: Test whether [J, D_K(tau(t))] acquires a nonzero time-dependent component during the transit, enabling transient CP violation for baryogenesis. The static result [J, D_K] = 0 at every fixed tau is proven (S17a). The question is whether the non-equilibrium quench dynamics introduce terms not captured by the instantaneous Hamiltonian.
**Method**: Compute the Berry connection A_tau = <psi_n(tau)| d/dtau |psi_m(tau)> for the D_K eigenstates near the fold. The effective Hamiltonian during the transit includes a geometric velocity term: H_eff = D_K(tau) + i * tau_dot * A_tau. Evaluate [J, A_tau] at 50 tau points through the transit. If [J, A_tau] != 0, the effective Hamiltonian breaks J-symmetry during the quench even though the instantaneous D_K preserves it. The CP-violating amplitude is proportional to tau_dot * ||[J, A_tau]||.
**Input**: D_K(tau) eigenvectors at 50 tau points (requires eigenvector computation, not just eigenvalues), canonical_constants.py
**Output**: s61_dynamic_j_breaking.py/.npz/.png (||[J, A_tau]|| vs tau, CP-violating amplitude vs tau_dot)
**Gate**: J-DYNAMIC-61. PASS if max ||[J, A_tau]|| > 0.01 (transient CP violation exists, baryogenesis channel opens). FAIL if ||[J, A_tau]|| = 0 to machine precision at all tau (J-wall is absolute, including during transit). INFO if nonzero but < 0.01 (exists but may be too weak for observed baryon asymmetry).
**Priority**: HIGH — all baryogenesis and leptogenesis channels were closed by J-wall in S60. This is the only identified escape route.
**Est. Cost**: ~minutes. Requires eigenvector derivatives (finite difference d/dtau of eigenvectors at 50 points). Eigenvector computation at each tau is the bottleneck (~10s per point at max_pq=6).
**Paper Reference**: Superfluid 3He texture dynamics during quench (Paper 10 Section 3.4 in Tesla library); Berry phase on parameter-dependent Hamiltonians (standard); LEPTO-CP-60 escape route E3
**Depends On**: none (uses existing D_K(tau) eigenvalue infrastructure; eigenvectors are a new output)
**Cross-agent contributions**:
- PHONON-10: Non-equilibrium eta(t) = sum_n sign(E_n(t))*|<n(t)|psi(t)>|^2; KZ quench IS the external T-breaking field (3He-B analog: rotation or magnetic field)

### TESLA-5: Physical Debye Cutoff for PW Tower
**Computation**: Determine the maximum physically meaningful PW level L_max by analogy with the Debye cutoff in crystal acoustics. On SU(3), PW levels correspond to harmonic modes with wavelength lambda ~ 1/(p+q). Modes with wavelength shorter than the physical resolution scale of the spectral action are unphysical. Compute L_max from: (1) the spectral action cutoff Lambda (modes with eigenvalue > Lambda are suppressed by f), (2) the geometric criterion that the mode wavelength must exceed the compactification scale, (3) the Weyl law eigenvalue growth rate.
**Method**: From the alpha_{a_2} = 9.14 growth exponent (S60), the L-th PW level contributes eigenvalues scaling as L^{9.14/8} ~ L^{1.14}. The Debye cutoff corresponds to the L where the eigenvalue equals Lambda. Invert: L_max = (Lambda/M_KK)^{8/9.14}. For Lambda = M_KK, L_max ~ 1. For Lambda = 10 M_KK, L_max ~ 7. Map L_max(Lambda) and compute the regularized Tr(|D_K|) and Tr(D_K^2) as functions of L_max. Determine which L_max (if any) gives stable physical predictions.
**Input**: PW eigenvalue data from existing scripts (all L levels), alpha_{a_2} = 9.14, canonical_constants.py
**Output**: s61_debye_cutoff_pw.py/.npz/.png (L_max vs Lambda curve, regularized traces vs L_max, convergence analysis)
**Gate**: DEBYE-STABLE-61. PASS if regularized traces converge to within 5% for L_max >= L_crit (a physical cutoff exists). FAIL if traces never converge (no meaningful Debye cutoff, must use heat kernel exclusively). INFO if convergence is cutoff-function-dependent.
**Priority**: MED — diagnostic that bridges the PW and heat kernel descriptions; determines whether any PW-based prediction can be salvaged
**Est. Cost**: ~minutes. Reprocesses existing eigenvalue data with L-dependent truncation.
**Paper Reference**: Debye model (Paper 05 in Tesla library); Weyl's law on compact manifolds; S60 PW divergence analysis (alpha_{a_2} = 9.14)
**Depends On**: PHONON-2 (alpha-critical determines what cutoff regime is physical)

### TESLA-6: Josephson Collective Mode Integrability
**Computation**: Determine whether the collective modes of the Josephson-coupled fabric are themselves integrable (and hence protect the GGE) or chaotic (and hence thermalize it). This is the deeper version of TESLA-1: the Thouless time measures the diffusion rate, but the integrability of the collective modes determines whether diffusion leads to thermalization or merely to coherent redistribution.
**Method**: Construct the Josephson Hamiltonian on the CG(24) graph: H_J = sum_{<ij>} E_J * (a_i^dag a_j + h.c.) where a_i = pair annihilation on cell i. Compute the level spacing statistics of H_J: Poisson (integrable) vs GOE (chaotic). Also compute the nearest-neighbor spacing ratio <r>. Cross-check with the CHAOS-1 methodology from S38 applied to the fabric Hamiltonian rather than the single-cell Hamiltonian.
**Input**: CG(24) adjacency matrix (degree 6, 32 vertices), E_J = 3.4 M_KK, V_pairing = 0.081 M_KK (from s60_pair_transfer.npz)
**Output**: s61_josephson_integrability.py/.npz/.png (level spacing histogram, <r> value, spectral form factor)
**Gate**: JOSEPHSON-INTEG-61. PASS if <r> < 0.45 (Poisson, integrable — GGE protected by collective-mode integrability). FAIL if <r> > 0.50 (GOE, chaotic — GGE thermalizes via collective mode scattering). INFO if <r> in [0.45, 0.50] (crossover regime).
**Priority**: HIGH — directly determines GGE fate, complementary to TESLA-1
**Est. Cost**: ~minutes. CG(24) has 32 sites; pair-sector Hilbert space is manageable. Level statistics require full diagonalization.
**Paper Reference**: Richardson-Gaudin integrability breaking (S60 RG-INTEGRALS-60); CHAOS-1 methodology (S38); Landau two-fluid model (Paper 09 in Tesla library)
**Depends On**: none

**Source files**: `sessions/archive/session-60/session-60-tesla-collab.md`

---

## Quantum Acoustics Theorist

### QA-1: Van Hove Dispersion — Tau-Resolved B2 Spectrum
**Computation**: Compute the full dispersion relation omega(k, tau) for B2 along the Jensen path, resolving the van Hove singularity at each tau value. Extract: (a) group velocity dE/dk near the flat point, (b) effective mass m* = (d^2E/dk^2)^{-1} entering the Landau-Zener formula, (c) density of states rho(E) at the van Hove energy. Determine the bandwidth of the van Hove protection as a function of tau.
**Method**: Diagonalize D_K(tau) at 50 tau points, project onto B2 sector, compute numerical derivatives of eigenvalues with respect to CG(24) graph wavevector k. DOS via adaptive-binning eigenvalue histogram at the van Hove energy.
**Input**: canonical_constants.py, D_K(tau) eigenvalue solver, B2 sector projection (S32/S34)
**Output**: s61_vanhove_dispersion.py/.npz/.png (omega(k,tau) surface, m*(tau), rho_vH(tau))
**Gate**: VANHOVE-DISP-61. PASS if dE/dtau = 0 at van Hove point for all tau (flat-band protection survives transit). FAIL if dE/dtau > 0.01 at any tau (protection lost). INFO if dE/dtau < 0.01 but nonzero (partial smearing).
**Priority**: HIGH
**Est. Cost**: ~10 min GPU (50 tau points x 8-mode diag per point)
**Paper Reference**: S32 BIC analysis; Steinhauer 2016 (analog Hawking); S60 TRANSPLANCKIAN-BOGO-60 (van Hove protection delta=0% for B2)
**Depends On**: none

### QA-3: Acoustic Metric Construction — Unruh Form from Phonon Dispersion
**Computation**: Construct the Unruh-form acoustic metric from the framework's phonon dispersion omega(k, tau). Compute acoustic Ricci scalar R_acoustic. Evaluate Parker temperature T_Parker = hbar * sqrt(|R_acoustic|) / (2 pi) and compare to Bogoliubov squeezing temperature T_squeeze = omega_f * <n_exc> / k_B. Test whether a sonic horizon forms during the transit (sweep velocity = local sound speed c_BA(tau)).
**Method**: From c_BA(tau) = 0.399 (S56) and sweep rate d(omega)/d(tau), construct 1+1D acoustic metric ds^2 = (rho/c)[-(c^2 - v^2)dt^2 - 2v dt dx + dx^2]. Compute Christoffel symbols and Ricci scalar at 50 tau points. Sonic horizon condition: v_sweep(tau) = c_BA(tau).
**Input**: s56_ba_spectrum.npz (c_BA, F_BA), s57_bogoliubov.npz (<n_exc>=0.05-0.48), canonical_constants.py
**Output**: s61_acoustic_metric.py/.npz/.png (g_mu_nu(tau), R_acoustic(tau), T_Parker(tau), horizon location if any)
**Gate**: ACOUSTIC-METRIC-61. PASS if T_Parker agrees with T_squeeze within factor 3 (acoustic picture consistent). FAIL if disagrees by >10x (acoustic metric not applicable). INFO if no sonic horizon forms (purely parametric amplification, consistent with S60 GH closure).
**Priority**: MED
**Est. Cost**: ~5 min CPU (analytic + numerical differentiation)
**Paper Reference**: Unruh 1981 (acoustic metric); Barcelo, Liberati, Visser 2005 (analog gravity review); S60 GH-TEMP-DW-60 FAIL
**Depends On**: none
**Cross-agent contributions**:
- QA-9: Explicit v_sweep(tau)/c_BA(tau) at 50 tau points; S57 Desert Mach=2700; gate SONIC-HORIZON-61: PASS if v_sweep/c_BA < 1 everywhere

### QA-4: Mode-Resolved Leggett Squeezing Spectrum
**Computation**: Compute |beta_L(k)|^2 for the Leggett branch as a function of wavevector k on CG(24) graph (24 k-points). Use tau-dependent Leggett dispersion omega_L(k, tau) = sqrt(omega_L0^2 + 4*J_L(tau)*sin^2(k/2)) with omega_L0 = 0.049 M_KK, J_L(tau) = epsilon*E_J(tau). Determine whether DM occupation spectrum n(k) is thermal, non-thermal, or structured.
**Method**: For each k-point, solve BdG equation with tau-dependent omega_L(k, tau). Squeezing parameter r(k) = integral of d(omega_L)/d(tau) / (2*omega_L) dtau. |beta(k)|^2 = sinh^2(r(k)). Compare n(k) to Bose-Einstein distribution at best-fit temperature.
**Input**: s59_epsilon_canonical.npz (epsilon=0.00374, omega_L0=0.049), s55_fabric_coupling.npz (E_J(tau)), CG(24) graph spectrum
**Output**: s61_leggett_squeezing_spectrum.py/.npz/.png (|beta(k)|^2 vs k, n(k) vs k, thermal comparison)
**Gate**: LEGGETT-SPECTRUM-61. PASS if n(k) is non-thermal (chi^2/dof > 3 vs Bose-Einstein fit). FAIL if thermal (chi^2/dof < 1.5). INFO if intermediate.
**Priority**: HIGH (determines DM observational signature)
**Est. Cost**: ~3 min CPU (24 k-points x ODE integration)
**Paper Reference**: S57 mode-independent BA theorem (|beta|^2=1.015 for BA); S59 epsilon canonical; Parker 1969 (cosmological particle creation)
**Depends On**: none

### QA-5: B2 Flat Band Robustness Under Josephson Coupling
**Computation**: Compute B2 bandwidth W_fabric in the Josephson fabric for N_cells = 2, 4, 8, 16, 24, 32. Single-cell B2 bandwidth W = 0.058 (S31Ca). Inter-cell coupling adds W_J = 4*J_L*epsilon. Compare W_fabric to sweep rate d(omega)/d(tau) at van Hove point. If W_fabric > d(omega)/d(tau), van Hove singularity is smeared and Landau-Zener receives corrections.
**Method**: Construct tight-binding Hamiltonian for B2 sector on CG(N_cells) graph with inter-cell hopping J_L = epsilon*E_J. Diagonalize. Extract bandwidth of B2-derived band as N_cells grows.
**Input**: s54_tb_hamiltonian.npz (CG graph), s59_epsilon_canonical.npz (epsilon=0.00374), s55_fabric_coupling.npz (E_J=7.042)
**Output**: s61_b2_fabric_bandwidth.py/.npz/.png (W_fabric(N_cells), W_fabric vs d(omega)/d(tau))
**Gate**: B2-FABRIC-61. PASS if W_fabric < d(omega)/d(tau) for all N_cells (van Hove protection survives in fabric). FAIL if W_fabric > d(omega)/d(tau) (protection smeared). INFO if marginal (within factor 2).
**Priority**: HIGH
**Est. Cost**: ~2 min CPU (small matrix diag per N_cells)
**Paper Reference**: S31Ca B2 flat band (W=0.058); S56 LEGGETT-FABRIC-56 (J_L, two-speed hierarchy); S60 TRANSPLANCKIAN-BOGO-60
**Depends On**: none

### QA-6: Multimode Covariance of Squeezed Leggett Modes
**Computation**: Determine whether squeezed Leggett modes at different k-points on CG(24) are correlated or independent. Compute covariance matrix C_{ij} = <n_i n_j> - <n_i><n_j> for Leggett modes i, j at different wavevectors after transit. Extract Mandel Q parameter Q = (Var(N_total) - <N_total>) / <N_total> to quantify departure from Poisson statistics.
**Method**: Evolve multimode squeezed state through transit. Common driver omega_L(k, tau) introduces correlations when squeezing is simultaneous across k-modes. Full covariance from multimode Bogoliubov transformation.
**Input**: s61_leggett_squeezing_spectrum.npz (from QA-4), CG(24) graph Laplacian, omega_L(k, tau)
**Output**: s61_multimode_covariance.py/.npz/.png (C_{ij} matrix, Q parameter, eigenvalue spectrum of C)
**Gate**: MULTIMODE-COV-61. PASS if Q > 0.1 (super-Poissonian, distinguishable from CDM). FAIL if |Q| < 0.01 (indistinguishable from Poisson). INFO if 0.01 < |Q| < 0.1.
**Priority**: MED
**Est. Cost**: ~10 min CPU (24x24 covariance from multimode ODE)
**Paper Reference**: S57 Bogoliubov squeezing; Kiefer, Polarski, Starobinsky 1998 (multimode cosmological squeezing)
**Depends On**: QA-4

### QA-8: Regularized Spectral Sum via Heat Kernel — Debye Analogy
**Computation**: Replace divergent PW sum Tr(|D_K|) with heat-kernel-regularized Tr(|D_K|*exp(-t*D_K^2)). Evaluate at physical scale t = 1/Lambda_KK^2. Compare to raw PW sum at L_max = 2..6. Verify regularized sum converges and reproduces Seeley-DeWitt expansion a_0 + a_2*t + a_4*t^2 + ... to numerical precision.
**Method**: Use D_K eigenvalue data at tau=fold. Compute Tr(|D_K|*exp(-t*lambda_n^2)) summed over all eigenvalues with PW multiplicities, at 20 values of t from 10^{-4} to 10. Fit to polynomial in t to extract a_0, a_2, a_4. Compare a_2 to USER-2 result.
**Input**: D_K eigenvalue files (corrected to include (1,2) irrep), canonical_constants.py
**Output**: s61_regularized_spectral_sum.py/.npz/.png (convergence plot, extracted SD coefficients, raw PW comparison)
**Gate**: REG-SPECTRAL-61. PASS if regularized sum converges (relative change < 1% from L_max=5 to 6) and a_2 agrees with USER-2 to 10%. FAIL if still divergent or disagrees. INFO if converges but a_2 unavailable.
**Priority**: HIGH (validates Debye analogy and correct computational approach)
**Est. Cost**: ~5 min CPU (eigenvalue data exists, reweighting only)
**Paper Reference**: S60 PW-H0-CONV-60 (L^{6.2} divergence); Gilkey 1975 (heat kernel expansion); QA collab Section 4 (phonon UV catastrophe = Debye resolution)
**Depends On**: USER-2 (for cross-validation of a_2)
**Cross-agent contributions**:
- SPEC-6: Third a_2 route via t^{-3} coefficient of Tr(exp(-t*D_K^2)); t in {0.01,0.1,1.0,10.0}; verify L-convergence

**Source files**: `sessions/archive/session-60/session-60-qa-collab.md`


---

## Landau Condensed Matter Theorist

### LANDAU-1: Ginzburg-Landau Free Energy for the CC Staircase
**Computation**: Fit the staircase E_GS(N) = {0, -0.046, +0.268, +0.875, +1.850} to a Landau polynomial F(n) = F_0 + a*n + b*n^2 + c*n^3 in the pair density n = N/8. Extract the equilibrium n_eq, the vacuum compressibility chi_q = (d^2F/dn^2)^{-1} at n_eq, and the CC gap Lambda ~ F(n_eq)/chi_q. Repeat at 10 tau values across the fold region [0.10, 0.25] to establish tau-dependence of {a, b, c, chi_q}.
**Method**: Polynomial regression on the 5-point staircase at each tau. Exact diagonalization of the 8-mode BCS Hamiltonian at each tau to generate E_GS(N). Compute chi_q from the curvature of the fitted F(n).
**Input**: s60_staircase_ext.npz, canonical_constants.py, D_K eigenvalues at 10 tau points
**Output**: s61_gl_staircase.py/.npz/.png (F(n) curves at each tau, chi_q(tau) plot)
**Gate**: GL-STAIRCASE-61. PASS if chi_q(tau) develops a minimum <0.1 at any tau (extreme softening). FAIL if chi_q > 0.5 at all tau (structurally stiff, confirming BEC character). INFO if chi_q in [0.1, 0.5].
**Priority**: HIGH
**Est. Cost**: ~30 min CPU (5 ED per tau x 10 tau points, dim 120 each)
**Paper Reference**: Landau Paper 04 (phase transitions); Volovik Paper 18 (q-theory vacuum compressibility); Landau collab S-1
**Depends On**: none (extends S60 staircase data)
**Cross-agent contributions**:
- VOL-1: Sector independence test (same chi_q for all PW sectors sharing N_pair, or sector-dependent); 3He-B analog: compressibility diverges at liquid-gas transition; chi_q ~ 1.2 at N=1 (CC-DIM-ANALYSIS-60)
- LANDAU-7: chi_q(tau) at 20 tau steps in [0.05, 0.30]; chi_q^{-1} = E_GS(2) - 2*E_GS(1) + E_GS(0)

### LANDAU-3: BCS-BEC Crossover Diagnostic
**Computation**: Extract the BCS-BEC crossover parameter 1/(k_F * a_s) from the pair wavefunction spatial extent in mode space at each N_pair = {1, 2, 3, 4}. Compute the condensate fraction n_0/N and the pair correlation length xi_pair. Place each N_pair on the BCS-BEC phase diagram (condensate fraction vs 1/k_F*a_s).
**Method**: From exact ground state wavefunctions at each N_pair, compute the pair correlation function C(k,k') = <c_k c_{-k} c_{-k'}^dag c_{k'}^dag>. Compute condensate fraction from largest eigenvalue of the pair density matrix. Map to the Nozieres-Schmitt-Rink crossover parameter. The BEC regime has xi_pair ~ 1 (localized pair); the BCS regime has xi_pair >> 1 (spread across Fermi surface).
**Input**: s60_staircase_ext.npz, s60_blocking_n3.npz (ground state wavefunctions and occupation numbers at N=1..4)
**Output**: s61_bcs_bec_crossover.py/.npz/.png (phase diagram placement, xi_pair(N), condensate fraction(N))
**Gate**: BCS-BEC-61. PASS if N=1 is BEC (condensate fraction > 0.8, 1/k_F*a_s > 1) and N=4 is crossover (condensate fraction < 0.5). FAIL if all N_pair are in the same regime. INFO if crossover occurs but at unexpected N.
**Priority**: MED
**Est. Cost**: ~20 min CPU (pair density matrix from stored wavefunctions, 8x8 matrix per N_pair)
**Paper Reference**: Strinati review Paper 25 (BCS-BEC crossover); Landau Paper 11 (quasiparticle framework); Landau collab S-3
**Depends On**: none (uses S60 data)

### LANDAU-4: Fermi Liquid Parameters with Josephson Coupling
**Computation**: Extract Landau parameters F_l^{s,a} from the quasiparticle interaction vertex of the full 2-cell Hamiltonian H_full, including the inter-cell Josephson coupling. Compare with the S58 intra-cell Pomeranchuk result (F_0 = +0.060, all stable). Decompose into Landau harmonics on the Josephson phase. Check all Pomeranchuk stability conditions F_l^s > -(2l+1) and F_l^a > -(2l+1).
**Method**: Diagonalize 2-cell H_full. Extract quasiparticle energies and two-body scattering amplitudes from the low-energy spectrum. Compute the forward scattering amplitude f(theta) where theta is the relative Josephson phase between cells. Decompose f(theta) into angular harmonics to get F_l. Check stability for l = 0, 1, 2.
**Input**: s60_rg_integrals.npz (H_full), s58_pomeranchuk_gge.npz (intra-cell F_l for comparison)
**Output**: s61_fabric_landau_params.py/.npz (F_l^{s,a} for l=0,1,2 with and without Josephson)
**Gate**: POMERAN-FABRIC-61. PASS if all F_l stable (GGE quasiparticle description survives inter-cell coupling). FAIL if any F_l violates Pomeranchuk bound (thermalization mechanism identified). INFO if marginal (|F_l + (2l+1)| < 0.1 for any l).
**Priority**: HIGH
**Est. Cost**: ~30 min CPU (120x120 diagonalization + scattering amplitude extraction)
**Paper Reference**: Landau Paper 11 (Fermi liquid theory, Pomeranchuk criteria); Landau Paper 06 (Landau damping); Landau collab S-4
**Depends On**: none (uses S60 data, extends S58 Pomeranchuk)

### LANDAU-8: Ginzburg Criterion for the CC Staircase
**Computation**: Compute Gi = (delta F / F_0)^2 where delta F = inter-cell fluctuation amplitude from Josephson coupling, F_0 = |E_GS(1) - E_GS(0)| = 0.046. For d_eff = 1, Gi > 1 means mean-field staircase unreliable.
**Method**: delta F ~ E_J * S_+(1)^2 / N_modes with E_J = 3.40, S_+(1) = 0.936. If Gi > 1, recompute staircase with second-order perturbation theory on 2-cell system.
**Input**: s60_staircase_ext.npz, s60_pair_transfer_n4.npz, s60_rg_integrals.npz
**Output**: s61_ginzburg_staircase.py/.npz
**Gate**: GINZBURG-CC-61. PASS if Gi < 0.1 (mean-field reliable). FAIL if Gi > 10 (qualitatively modified). INFO if [0.1, 10].
**Priority**: MED
**Est. Cost**: ~15 min CPU
**Paper Reference**: Landau Paper 08 (Ginzburg-Landau); Landau Paper 04; Landau collab Q6
**Depends On**: none

### LANDAU-10: Landau Damping Threshold for the Leggett Mode
**Computation**: Compare omega_L(N_pair) with pair-breaking threshold 2*Delta(N_pair) at N = {1,2,3,4}. Determine if Leggett mode enters quasiparticle continuum (Landau damping) or stays gap-protected.
**Method**: Extract omega_L from LEGGETT-MASS-N2-60. Compute Delta_min = min_k sqrt(epsilon_k^2 + Delta_k^2) at each N. Gap-protected if omega_L < 2*Delta_min.
**Input**: s60_leggett_mass.npz, s60_staircase_ext.npz
**Output**: s61_leggett_damping.py/.npz/.png
**Gate**: LEGGETT-DAMPING-61. PASS if omega_L < 2*Delta at N=1,2. FAIL if omega_L > 2*Delta at N=1. INFO if crossing at N=3,4 only.
**Priority**: LOW
**Est. Cost**: ~10 min CPU
**Paper Reference**: Landau Paper 06 (damping); Landau Paper 11 (quasiparticle continuum); Landau collab Section 4.3
**Depends On**: none

**Source files**: `sessions/archive/session-60/session-60-landau-collab.md`

---

## Nazarewicz Nuclear Structure Theorist

### NAZ-1: Particle-Number Projection for the Heat Kernel
**Computation**: Compute a_2(D_K^2) in the number-projected BCS state (PBCS) and compare to the unprojected BCS result. BCS breaks U(1)_7 gauge symmetry; PAV restores it. Determine whether heat kernel coefficients shift under number restoration.
**Method**: Exact number projection via gauge-angle integral P_N = (1/2pi) integral_0^{2pi} e^{i*phi*(N_hat - N)} d_phi applied to BCS density matrix. Lipkin-Nogami as cheaper alternative. Compute a_2 from projected density using local curvature integral on Jensen-deformed SU(3).
**Input**: S52 data (s52_hfb_full.npz), canonical_constants.py, Jensen metric curvature from Milnor's formula
**Output**: s61_proj_a2.py/.npz -- a_2^{PBCS} vs a_2^{BCS}, fractional deviation
**Gate**: PROJ-A2-61. PASS if |a_2^{PBCS} - a_2^{BCS}| / a_2^{BCS} < 5%. FAIL if > 20%. INFO if 5-20%.
**Priority**: HIGH (accompanies USER-2 HEAT-KERNEL-A2-61)
**Est. Cost**: Moderate -- angular integral over existing ED ground state
**Paper Reference**: Paper 03 (Dobaczewski, Nazarewicz 2013) Sec. V (PAV/VAP); Paper 15 (Dukelsky, Pittel, Sierra 2004) Sec. V, Fig. 12; naz-collab Sec. 3.1
**Depends On**: USER-2 (HEAT-KERNEL-A2-61 provides the unprojected a_2)

### NAZ-2: Bayesian Model Comparison for CC Mechanisms
**Computation**: Formal Bayes factor comparison of surviving CC mechanisms: (a) q-theory with Lambda_eq = 0, (b) proper heat kernel a_0, (c) a_4-dominated regime alpha < 55. Compute B_{a/b}, B_{b/c}, B_{a/c} using 60 sessions of gate verdicts as data.
**Method**: Define priors for each model's free parameters. Compute marginal likelihoods P(data|model) = integral P(data|theta,model) P(theta|model) d_theta. Report Bayes factors. Same methodology as Paper 06 for UNEDF0 vs UNEDF1 vs SLy4.
**Input**: Gate verdict history (tools/knowledge-index.json), S60 HESSIAN-3D-60 (alpha_crit=55), S60 BAYESIAN-H0-60 variance decomposition
**Output**: s61_cc_bayes_comparison.py/.npz -- Bayes factors, model ranking, posterior probabilities
**Gate**: CC-BAYES-MODEL-61. INFO (characterization). Upgrade to PASS if B > 10 for one model.
**Priority**: MEDIUM
**Est. Cost**: Low -- analytic computation over existing verdicts, no eigenvalue solves
**Paper Reference**: Paper 06 (McDonnell et al. 2015) Bayesian model comparison for nuclear DFT; naz-collab Sec. 3.2
**Depends On**: None

### NAZ-3: GGE Thermalization via Compound Nucleus Formalism
**Computation**: Compute the Thouless time t_Th for the Josephson-coupled fabric using the compound nucleus doorway-state formalism (Paper 22). Determine spreading width D_spread. Compare t_Th to t_transit to determine whether GGE survives fabric thermalization.
**Method**: Hauser-Feshbach averaging over RG quasi-integrals (treated as resonances). Ericson fluctuation width from pair hopping rate. Mapping: resonances -> RG quasi-integrals, Ericson fluctuations -> pair hopping rate, Gamma_CN -> 1/t_Th.
**Input**: S60 RG-INTEGRALS-60 data (delta_k=0.328), S49 fabric ED, E_J from canonical_constants.py, t_transit
**Output**: s61_gge_thermalization.py/.npz -- D_spread, t_Th, t_Th/t_transit ratio
**Gate**: GGE-THERM-61. PASS if t_Th > 10*t_transit (GGE survives). FAIL if t_Th < 0.1*t_transit. INFO if 0.1 < t_Th/t_transit < 10.
**Priority**: HIGH (determines whether DM production mechanism survives)
**Est. Cost**: Moderate -- doorway state coupling matrix from existing Josephson ED
**Paper Reference**: Paper 22 (compound nucleus, Hauser-Feshbach, Ericson fluctuations); naz-collab Sec. 3.3; 3HeB naz-collab Sec. 5.3
**Depends On**: None (uses S60 RG-INTEGRALS data)
**Cross-agent contributions**:
- NAZ-12: Microscopic golden-rule spreading width D_spread = 2*pi*|<doorway|H_J|compound>|^2*rho_compound; gate COMPOUND-SPREAD-61: PASS if D_spread < 0.1*E_J

### NAZ-4: Pair Transfer CMB Propagation
**Computation**: Propagate the bosonic pair-transfer scaling S_+(N) = (N+1)(1-N/16)/2 through the full chain delta_N_pair -> delta_Delta -> delta_J -> delta_T to obtain CMB temperature anisotropy delta_T/T as a function of N_pair.
**Method**: Chain of derivatives: dDelta/dN from ED pairing gaps, dJ/dDelta from Josephson relation, dT/dJ from CMB transfer. Use mode-resolved S_+(N) structure (max/min=1.35 uniformity) as initial condition.
**Input**: S60 s60_pair_transfer_n4.npz, S52 ED gaps, canonical_constants.py
**Output**: s61_pair_cmb.py/.npz/.png -- delta_T/T(N_pair), comparison to Planck
**Gate**: PAIR-CMB-61. PASS if delta_T/T has N-dependent structure in [10^{-6}, 10^{-4}]. FAIL if flat or outside [10^{-8}, 10^{-2}]. INFO if structure exists but below Planck sensitivity.
**Priority**: MEDIUM
**Est. Cost**: Low-moderate -- chain of analytic derivatives
**Paper Reference**: Paper 18 (pair transfer review); Paper 19 (GPV experimental prospects); naz-collab Sec. 3.4
**Depends On**: None

### NAZ-6: SD-Shell Benchmark Comparison
**Computation**: Solve the Richardson-Gaudin exactly solvable pairing model for the 6-level nuclear sd-shell at N_pair=1-3. Compare OES, blocking parameter b(N), coherence factors |u^2-v^2|, spectroscopic factors Z_k, and pair-transfer S_+(N) directly to the framework's 8-mode results.
**Method**: Richardson-Gaudin exact solution (Paper 15 Eq. 9) for sd-shell single-particle energies (d_{5/2}, s_{1/2}, d_{3/2} from Paper 07 Woods-Saxon). Extract 5 observables at each N_pair. Quantitative comparison table.
**Input**: Paper 15 RG equations, Paper 07 sd-shell energies, S52-S60 framework data (s52_hfb_full.npz, s53_hfb_spectral.npz, s60_pair_transfer_n4.npz, s60_blocking_n3.npz)
**Output**: s61_sdshell_benchmark.py/.npz -- nuclear sd-shell vs framework: OES, b(N), |u^2-v^2|, Z_k, S_+(N)
**Gate**: SD-SHELL-BENCH-61. INFO (calibration, no pass/fail -- quantifies proximity of 8-mode framework to 6-level nuclear sd-shell)
**Priority**: HIGH (sd-shell is the closest physical analog)
**Est. Cost**: Moderate -- Richardson-Gaudin solver + comparison
**Paper Reference**: Paper 15 Sec. III; Paper 07 (WS shell structure); Paper 03 (OES, blocking); Paper 18 (pair transfer); 3HeB naz-collab Sec. 3.1, 6 (#1)
**Depends On**: None

### NAZ-7: PBCS Correction Scaling with Fabric Size
**Computation**: Compute PBCS correction for the 2-cell Josephson system at N=1 and compare to single-cell PBCS (S52: +0.97%). If PBCS/ED decreases with fabric size, BCS improves toward thermodynamic limit. If it increases, projection becomes MORE important on the fabric.
**Method**: Exact diagonalization of 2-cell Hamiltonian in N=1 sector. Compute BCS and PBCS ground state energies. Compare PBCS/ED ratios: 1-cell vs 2-cell.
**Input**: S52 data (s52_hfb_full.npz, PBCS/ED = +0.97%), 2-cell Josephson ED Hamiltonian
**Output**: s61_pbcs_fabric.py/.npz -- PBCS/ED ratio at N=1 for 1-cell and 2-cell
**Gate**: PBCS-FABRIC-61. PASS if ratio decreases (BCS improves). FAIL if ratio increases. INFO if change < 10%.
**Priority**: MEDIUM
**Est. Cost**: Moderate -- 2-cell ED in N=1 sector manageable
**Paper Reference**: Paper 03 Sec. V (PAV/VAP); Paper 15 Sec. V, Fig. 12; Paper 17 (generalized variational BCS); 3HeB naz-collab Sec. 3.2, 6 (#2)
**Depends On**: None

### NAZ-8: Nuclear Pairing Chain Attenuation
**Computation**: Compute dimensionless pairing ratio Delta/E_F at each inheritance level where BCS occurs: Level 0 (substrate), Level 3 (nuclear), Level 5 (3He-B). Plot vs level number. Check for systematic attenuation through the chain.
**Method**: Collect: (a) framework Delta from S35 E_cond, E_F from S53 B2 eigenvalues; (b) nuclear Delta_n from Paper 02 HFB in medium-mass nuclei, E_F from nuclear mean field; (c) 3He-B experimental Delta/E_F ~ 10^{-3}. Compute ratios, plot.
**Input**: S35 BCS data (E_cond=-0.137 M_KK), S53 spectrum, Paper 02 nuclear pairing, 3He-B literature
**Output**: s61_pairing_chain.py/.npz/.png -- Delta/E_F at 3 levels, attenuation trend
**Gate**: PAIRING-CHAIN-61. INFO (characterization -- monotonic decrease supports inheritance, non-monotonic constrains the claim)
**Priority**: HIGH (quantitative test of the inheritance claim)
**Est. Cost**: Low -- data collection and ratio computation
**Paper Reference**: Paper 02 (HFB continuum, nuclear pairing); Paper 03 (pairing systematics); 3HeB naz-collab Sec. 3.1, 6 (#3)
**Depends On**: None

### NAZ-9: Seniority Quantum Numbers on the Fabric
**Computation**: Compute seniority quantum numbers for 2-cell Josephson ED eigenstates. Determine whether seniority is approximately conserved (supports residual integrability) or strongly mixed (supports thermalization). Addresses whether Josephson coupling introduces new approximate conservation laws.
**Method**: Construct seniority operator v from pair-creation/annihilation algebra (Paper 23). Compute <v^2> (seniority purity) and <Delta_v> (mixing width) for all eigenstates.
**Input**: S60 2-cell ED eigenvectors, Paper 23 seniority algebra
**Output**: s61_seniority_fabric.py/.npz -- <v^2>, <Delta_v>, purity distribution
**Gate**: SENIORITY-FABRIC-61. INFO (high purity -> integrability survives, low purity -> thermalization)
**Priority**: MEDIUM
**Est. Cost**: Low-moderate -- seniority operator on existing eigenvectors
**Paper Reference**: Paper 23 (seniority isomers); Paper 15 (RG and seniority); 3HeB naz-collab Sec. 6 (#5); naz-collab Sec. 5.2
**Depends On**: None

### NAZ-10: Pair-Transfer EWSR (Thouless Identity)
**Computation**: Verify the Thouless identity for the pair-transfer energy-weighted sum rule: m_1 = (1/2)<[S_+,[H,S_-]]>. Compare to m_1 from explicit sum over excited states. Framework should satisfy this exactly for an exact Hamiltonian.
**Method**: S_+ = sum_k c_{k,up}^dag c_{k,down}^dag. Evaluate double commutator [S_+,[H,S_-]] in ED ground state. Compare to m_1 = sum_n (E_n-E_0)|<n|S_+|0>|^2 from S60 pair-transfer data.
**Input**: S60 PAIR-TRANSFER-N4-60 data (matrix elements, excitation energies), framework H
**Output**: s61_gpv_ewsr.py/.npz -- EWSR from double commutator vs explicit sum, ratio
**Gate**: GPV-EWSR-61. PASS if ratio within 5% of unity. FAIL if > 20%. INFO if 5-20%.
**Priority**: MEDIUM
**Est. Cost**: Low -- double commutator in existing ED basis
**Paper Reference**: Paper 18 (pair transfer, Thouless theorem); Paper 19 (GPV sum rule); 3HeB naz-collab Sec. 6 (#6)
**Depends On**: None

### NAZ-11: Pair-Transfer Scaling on Larger Fabrics
**Computation**: Test whether bosonic scaling S_+(N) = (N+1)(1-N/N_slots)/2 survives at 4-cell and 8-cell fabric sizes. S60 established this for 2 cells (N_slots=16). Does bosonic enhancement (N+1) survive pair delocalization?
**Method**: ED of 4-cell and 8-cell Josephson Hamiltonians at N_pair=1-4. Compute S_+(N), test against bosonic scaling. Track mode uniformity (max/min ratio) vs fabric size.
**Input**: S60 s60_pair_transfer_n4.npz (2-cell baseline), 4-cell/8-cell Hamiltonians, canonical_constants.py
**Output**: s61_pair_transfer_fabric.py/.npz/.png -- S_+(N) at 2,4,8 cells; scaling comparison
**Gate**: PAIR-FABRIC-61. PASS if scaling holds to <10% at 8 cells. FAIL if (N+1) suppressed below (N+1)/2. INFO if intermediate.
**Priority**: MEDIUM
**Est. Cost**: High -- 8-cell ED Fock space grows rapidly, may need truncation
**Paper Reference**: Paper 18 (delocalization sensitivity); Paper 19 (GPV on extended systems); naz-collab Sec. 5.4
**Depends On**: None
**Cross-agent contributions**:
- PHONON-13: J-wall constructive instance (J-symmetry guarantees exact time-reversal of pair transfer); xi/d=5.3 so pair extends over most cells (CG(24) diameter=3)

### NAZ-13: BDI to DIII Transition Through Compositing
**Computation**: Trace T^2 eigenvalue through the inheritance chain. Verify BDI -> DIII transition occurs at Level 4->5 (atom formation, odd-A nucleus). Check: is 3He the UNIQUE path to DIII, or does any odd-A nucleus produce DIII descendants?
**Method**: At each level compute T^2 from total angular momentum: substrate (BDI, T^2=+1) -> quarks -> nucleons (spin-1/2) -> nucleus (A-dependent) -> atom -> superfluid. Even-A stays BDI. Odd-A shifts to DIII via Kramers pairs.
**Input**: S34 BDI classification, Paper 07 nuclear spin assignments, Volovik 3He-B DIII
**Output**: s61_bdi_diii_chain.py/.npz -- T^2 at each level, critical step identification
**Gate**: BDI-DIII-CHAIN-61. INFO (characterization)
**Priority**: LOW
**Est. Cost**: Low -- representation theory, no heavy numerics
**Paper Reference**: Paper 08 (pairing, time-reversal); S34 BDI; 3HeB naz-collab Sec. 5.2
**Depends On**: None

### NAZ-14: Yukawa Couplings from D_F on Jensen-Deformed SU(3)
**Computation**: Construct the finite Dirac operator D_F from the L-homomorphism failure on the framework's SU(3) with Jensen deformation. Extract Yukawa matrices Y_u, Y_d, Y_e, Y_nu. Compare predicted fermion mass ratios to observed values. Single highest-impact Level 4 prediction.
**Method**: Compute LEFT action L_{su(3)} on Psi_+ for C^2 coset directions at tau_fold. L-homomorphism failure terms define D_F (Session 16 result #3). Extract 3x3 Yukawa matrices. Diagonalize for mass eigenvalues and CKM/PMNS angles.
**Input**: Session 16 L-action matrices, Jensen metric at tau_fold=0.19, canonical_constants.py
**Output**: s61_yukawa_first_principles.py/.npz -- Y_u, Y_d, Y_e, Y_nu; mass ratios; mixing angles
**Gate**: YUKAWA-FIRST-PRINCIPLES-61. PASS if any mass ratio matches observation to <30%. FAIL if all off by >OOM. INFO if structure correct but magnitudes require RG running.
**Priority**: HIGH (Level 4 prediction)
**Est. Cost**: Moderate -- D_F construction from L-action matrices + diagonalization
**Paper Reference**: Baptista Papers 17-18 (D_F structure); Session 16 result #3; particle emergence map Sec. IX.1
**Depends On**: None

### NAZ-15: Higgs Mass from Sector-Resolved Spectral Action
**Computation**: Predict m_H from the spectral action with correct PW sector decomposition. S60 A4-TRACE-60 found N_{a_4}/N_{a_2}=1.823 (35% systematic). Does this bring the CCM prediction (~170 GeV) toward observed m_H=125.1 GeV?
**Method**: m_H^2 = 2*lambda*v^2 with lambda from a_4/a_2 and Yukawa couplings. Include sector correction sqrt(N_{a_4}/N_{a_2})=1.35. Apply CCM Higgs mass formula with framework's a_2, a_4.
**Input**: S60 A4-TRACE-60 (N_{a_4}/N_{a_2}=1.823), USER-2 heat kernel a_2/a_4, Yukawa couplings (NAZ-14 or CCM standard)
**Output**: s61_higgs_mass.py/.npz -- m_H prediction, comparison to 125.1 GeV
**Gate**: HIGGS-MASS-61. PASS if m_H in [110, 140] GeV. FAIL if outside [80, 200]. INFO if [80,200] but outside [110,140].
**Priority**: MEDIUM
**Est. Cost**: Low once a_2, a_4 available
**Paper Reference**: CCM Higgs mass formula; S60 A4-TRACE-60; particle emergence map Sec. IX.5
**Depends On**: USER-2 (HEAT-KERNEL-A2-61), optionally NAZ-14

### NAZ-16: Heat Kernel Mode-Resolved Oscillations
**Computation**: Determine whether the properly regularized CC (heat kernel or zeta function) exhibits oscillatory corrections to its smooth value. STRUTINSKY-PW-60 poly3 captures 99.9999% of Lambda_eff(L); residuals decrease 5-14x per level. Do these survive regularization?
**Method**: Compute heat kernel K(t,D_K^2) = sum_n exp(-t*lambda_n^2) at several t. Extract smooth part (Seeley-DeWitt) and oscillatory residual. Check finite limit as t -> 0.
**Input**: D_K eigenvalue spectrum (all PW levels), S60 STRUTINSKY-PW-60 (poly3, oscillatory residuals)
**Output**: s61_hk_oscillations.py/.npz/.png -- smooth vs oscillatory decomposition, residual vs regularization
**Gate**: HK-OSCILLATION-61. PASS if oscillatory residual finite and ~ Lambda_obs. FAIL if residual -> 0. INFO if finite but >> Lambda_obs.
**Priority**: MEDIUM
**Est. Cost**: Moderate -- heat kernel trace at multiple t values
**Paper Reference**: Paper 08 (shell correction, Strutinsky); S55 STRUTINSKY-992-55; S60 STRUTINSKY-PW-60 (Gaussian zero theorem); naz-collab Sec. 5.3
**Depends On**: USER-2 (HEAT-KERNEL-A2-61 baseline)

### NAZ-17: Bayesian Inheritance vs Analogy Discrimination
**Computation**: Bayesian model comparison between M_inherit (correspondences from parent-child compositing) and M_analogy (from shared BCS universality class). Use Volovik's condensate ranking (3He-B:6/6, CFL:5/6, n-star 3P2:5/6, 3He-A:4/6, cuprates:3/6, SC:3/6, 4He:2/6).
**Method**: Under M_inherit: P(match) decreases with compositing distance. Under M_analogy: P(match) constant. Discriminant: CFL should score higher than 3He-B under M_inherit (fewer levels). Compute Bayes factor.
**Input**: 3He-B comparison rankings, compositing level assignments
**Output**: s61_inheritance_bayes.py/.npz -- Bayes factor, model posterior, prior sensitivity
**Gate**: INHERIT-BAYES-61. INFO (expected indeterminate -- CFL theory incomplete; Paper 06: model form error dominates)
**Priority**: LOW
**Est. Cost**: Low -- analytic Bayesian computation
**Paper Reference**: Paper 06 (Bayesian model comparison); 3HeB naz-collab Sec. 3.3
**Depends On**: None

### NAZ-18: Cosmological Transit Baryogenesis Estimate
**Computation**: Estimate whether the transit (tau=0 to tau_fold) provides sufficient T-breaking for baryogenesis. W_J blocks CP violation from D_K, but the time derivative d(D_K)/dt during transit breaks T. Compute effective epsilon_CP from transit dynamics.
**Method**: Time-dependent D_K(tau(t)) produces pair-creation/annihilation amplitudes. Their interference generates CP violation (nuclear analog: particle production in time-dependent mean fields, ATDHFB Paper 16). Compute asymmetry between forward/backward pair amplitudes.
**Input**: D_K(tau) eigenvalues at 50 tau points, S57 FINITE-RATE-TRANSIT rate, Paper 16 ATDHFB
**Output**: s61_transit_baryogenesis.py/.npz -- epsilon_CP, eta_B, comparison to observed 6e-10
**Gate**: TRANSIT-BARYOGEN-61. PASS if eta_B within 3 OOM of 6e-10. FAIL if < 10^{-20}. INFO if [10^{-20}, 10^{-7}].
**Priority**: MEDIUM
**Est. Cost**: Moderate -- ATDHFB-style computation along transit path
**Paper Reference**: Paper 16 (ATDHFB); S60 LEPTO-CP-60 (W_J wall); S57 FINITE-RATE-TRANSIT; particle emergence map Sec. VII.2
**Depends On**: USER-3 (TRANSIT-SA-61 transit dynamics)

**Source files**: `sessions/archive/session-60/session-60-naz-collab.md` (Secs. 3.1-3.4, 5.1-5.4), `sessions/archive/session-60/framework-3HeB-comparison-naz-collab.md` (Secs. 3.1-3.3, 5.1-5.5, 6), `sessions/archive/session-60/framework-particle-emergence.md` (Secs. IX, XI)

---

## Phonon-First Cosmologist

### PHONON-2: Physical Alpha Parameter on Jensen Metric (Pillar III x VIII)
**Computation**: Determine alpha = f_2 * Lambda^2 / f_0 on the Jensen metric. HESSIAN-3D-60 found alpha_crit = 55: H_a2 all-negative (fold unstable, mode-counting) vs H_a4 all-positive (fold stable, index-counting). This transition appears in three pillars independently: acoustic-to-dispersive (Pillar I), CDT d_s flow 4->2 (Pillar VII, Paper 28), NCG cutoff-dependent content (Pillar III, Paper 13 Section 4.3). The regime alpha < 55 is where the spectral action functions as a topological invariant (Connes argument, Paper 10). Zero-parameter test: if alpha_phys < 55, fold is stable a_4 minimum, BCS stabilization unnecessary.
**Method**: For each cutoff choice — heat kernel f(x)=e^{-x} (f_0=1, f_2=1); sharp cutoff (f_0=1, f_2=1/2); Chamseddine-Connes optimal — compute alpha = f_2*Lambda^2/f_0 with Lambda in {M_KK, Delta_BCS, M_Pl}. Compare to alpha_crit = 55.
**Input**: canonical_constants.py (M_KK), BCS gap Delta, Connes conventions (Paper 10 eq. 1.1), HESSIAN-3D-60 alpha_crit = 55
**Output**: s61_alpha_physical.py/.npz — alpha(Lambda) for each cutoff, regime identification, alpha_crit overlay
**Gate**: ALPHA-REGIME-61. PASS if alpha_phys < 55 (fold stable, index regime). FAIL if alpha_phys > 55 (fold unstable, mode regime). INFO if within factor 2 of 55.
**Priority**: HIGH (determines stabilization mechanism; constrains PHONON-6; single most decisive uncomputed quantity per Section 5 Q1)
**Est. Cost**: CPU-only, algebraic. Minutes.
**Paper Reference**: Paper 10 (Connes spectral action), Paper 13 Section 4.3, Paper 28 (CDT d_s). Collab Section 1 Pattern 3, Section 4, Section 5 Q1.
**Depends On**: SP-1 (a_2 local value feeds into f_2 identification)
**Cross-agent contributions**:
- HAWK-3: Gaussian exp(-x^2) cutoff; map (f, Lambda) parameter space
- TESLA-2: Three cutoff choices explicitly; overlay Hessian eigenvalue trajectories; ghost-freedom check; phononic bandgap transition (Paper 06)
- QA-7: Positivity, unitarity, ghost-freedom check for each cutoff; chi8 cutoff
- LANDAU-6: erfc(x-1) cutoff; scan Lambda_UV/M_KK from 1 to 100
- NAZ-5: Planck-to-KK hierarchy gives alpha ~ 2.7e4 >> 55; nuclear analog: shell correction vs liquid drop
- VOL-5: f_4/f_0 ratio (when a_4 dominates) changes moment problem from Hausdorff-impossible f_4/f_2 = 1.4e-121 (CUTOFF-F-44)
- VDD-15: Chamseddine-Connes 1996 cutoff ambiguity
- SPEC-3: chi8 cutoff; seconds computation
- BAP-7: Riemann zeta test function from Paper 21 entropy-spectral action duality; f_0, f_2 extraction; alpha_zeta comparison to alpha_crit=55

### PHONON-3: Thouless Time on CG(24) via Spectral Gap (Pillar V x VII)
**Computation**: Compute the Thouless time for pair diffusion across CG(24) = Cayley(S_4, {all 6 transpositions}). GGE permanence is the second decisive gate: t_Th >> t_transit (GGE survives, DM intact) or t_Th << t_transit (thermalizes, DM gone). This is the Josephson version of ETH (Pillar V): integrable systems violate ETH and thermalize to GGE; non-integrable satisfy ETH and thermalize to Gibbs. delta_k = 0.33 (RG-INTEGRALS-60) puts system in intermediate regime. The Thouless time determines which side wins. Estimated t_Th ~ d^2/E_J ~ 9/7 ~ 1.3 M_KK^{-1}, comparable to transit timescale — genuine race condition.
**Method**: (1) CG(24) normalized Laplacian eigenvalues: lambda_pi = 1 - (1/6)*sum_{s} chi_pi(s)/dim(pi) for all 5 S_4 irreps. (2) Spectral gap = smallest nonzero eigenvalue. (3) t_Th = 1/(E_J*lambda_1). (4) Compare to t_transit. (5) Spectral dimension cross-check: return probability P(t) on CG(24), d_s(t) = -2 d(ln P)/d(ln t). If d_s < 2 at short times (CDT-like, Paper 28), Thouless time extended (walkers confined). Connects Delta_N ~ N^{-1.84} (S57) to thermalization directly.
**Input**: S_4 character table (exact), E_J = 7 M_KK (canonical_constants.py), t_transit from S38
**Output**: s61_thouless_cayley.py/.npz/.png — lambda_1, t_Th/t_transit ratio, d_s(t) on CG(24), CDT comparison
**Gate**: GGE-THERM-61. PASS if t_Th/t_transit > 10 (GGE survives). FAIL if < 0.1 (thermalizes). INFO if [0.1, 10].
**Priority**: HIGH (second decisive gate — DM mechanism survival)
**Est. Cost**: CPU-only, 24x24 exact diag + S_4 rep theory. Seconds.
**Paper Reference**: Paper 19 (Fazio-van der Zant JJ arrays), Paper 22 (Haviland 1D QPT), Paper 27 (Calcagni-Oriti spectral dimension), Paper 28 (CDT d_s). Collab Section 2(c), 3.3, 5 Q2.
**Depends On**: none

### PHONON-4: Superfluid Weight from Quantum Metric (Pillar IV x V)
**Computation**: Compute D_s of Josephson fabric via Peotta-Torma (Paper 18). The bosonic scaling S_+(N) ~ (N+1)(1-N/16)/2 is the exact BCS-BEC crossover interpolation (pure BEC: S_+=N+1; Pauli blocking reduces). Josephson dominance (E_J/|V| = 42:1) forces all modes to participate — condensed matter analogue of superfluid with coherence length > system (Pillar V, Paper 19). D_s = 2*E_J*S_+(N_eq)/V_cell. If D_s > 0, U(1)_7 breaking is genuine superfluid (Anderson-Bogoliubov mode exists in fabric). Meissner mass m_M vs Leggett mass m_L from LEGGETT-MASS-N2-60 is the Pillar IV-V consistency test.
**Method**: (1) S_+(1) = 0.936 from PAIR-TRANSFER-N4-60. (2) D_s = 2*E_J*S_+(1)/V_cell. (3) m_M = sqrt(D_s*M_KK^2). (4) Compare to omega_L = 0.138 M_KK (S52). (5) Verify Peotta-Torma: quantum metric g_{mu,nu} from Bloch state overlaps.
**Input**: s60_pair_transfer_n4.npz, s60_leggett_mass_n2.npz, canonical_constants.py, D_K eigenstates at fold
**Output**: s61_superfluid_weight.py/.npz — D_s, m_M, m_M/m_L ratio, quantum metric components
**Gate**: MEISSNER-LEGGETT-61. PASS if D_s > 0 AND |m_M - omega_L|/omega_L < 20%. FAIL if D_s = 0 or mismatch > 100%. INFO if 20-100%.
**Priority**: MED (connects two PASS results; tests Peotta-Torma on SU(3))
**Est. Cost**: CPU-only, algebraic + small matrix diag. Minutes.
**Paper Reference**: Paper 18 (Peotta-Torma), Paper 19 (Fazio-van der Zant). Collab Section 2(b), 3.4, 5 Q5.
**Depends On**: none

### PHONON-5: Spectral Dimension from Pair Return Probability (Pillar VII)
**Computation**: Compute d_s(t) of BCS Fock space from P(t) = |<GS|e^{-iHt}|GS>|^2. Gap scaling Delta_N ~ N^{-1.84} (S57) implies anomalous z = 3.68 for d_s = 2 — unexplained (S57 memory). BEKENSTEIN-PW-60: (0,0) sector Bekenstein-saturated (S_max/S_Bek = 6.44). Holographic saturation = d_s = 2 for bulk (Bekenstein bound = holographic dimensional reduction d->d-1). The BCS ground state saturating Bekenstein for the singlet sector is a holographic signature; the spectral dimension of the pair sector may unlock the gap scaling exponent.
**Method**: (1) From BCS eigenvalues at N = 2,4,8,16,32, compute P(t). (2) d_s(t) = -2 d(ln P)/d(ln t). (3) Check d_s -> 2 at short times (CDT UV, Paper 28). (4) d_s at long times. (5) Extract z from d_s = 2*d_eff/z. (6) Compare z to alpha = -1.84.
**Input**: BCS eigenvalues/eigenstates at N = 2..32 from existing computation, S57 gap scaling
**Output**: s61_spectral_dimension_pair.py/.npz/.png — d_s(t) flow, z extraction, CDT + S57 comparison
**Gate**: SPEC-DIM-PAIR-61. PASS if d_s(short) = 2.0 +/- 0.2 (CDT UV match). FAIL if d_s constant. INFO if flows but d_s(short) != 2.
**Priority**: MED (connects gap scaling anomaly to CDT — potential structural breakthrough)
**Est. Cost**: CPU at N=2,4,8; GPU for N=16,32. Minutes to hours.
**Paper Reference**: Paper 27 (Calcagni-Oriti), Paper 28 (CDT d_s), Paper 26 (Lauscher-Reuter). Collab Section 3.5.
**Depends On**: none

### PHONON-6: a_4-Dominated Spectral Action with q-Theory Vacuum (Pillar III x II)
**Computation**: Test the productive compound from Section 3.2: a_4 Hessian stability (alpha < 55, HESSIAN-3D-60 all-positive) + q-theory vacuum selection (Lambda_eq = 0 per sector, Pillar II Papers 06/09). The a_4 Gauss-Bonnet term is the NCG Euler characteristic correction (Paper 10 eq. 1.1). If alpha < 55, fold IS stable, CC set by a_0 in INDEX regime. BCS free energy provides departure from Lambda_eq = 0 at topological charge Q = +/-29.9 (Q-THEORY-GEODESIC-60 proven topological). The problem reduces to: why Lambda_obs rather than Lambda_eq = 0? — the cosmological version of the condensed matter "measure problem" (in 3He, Paper 06, vacuum energy = 0 at equilibrium; departures ~ T^4 match observation).
**Method**: (1) a_0 = Vol(SU(3))*16/(4pi)^4. (2) Lambda_eff = a_0*f_0/(a_4*f_4) in a_4-dominated regime. (3) q-theory departure: delta_Lambda = d(rho)/dq|_{q=Q}, Q=29.9. (4) Lambda_residual = Lambda_eff + delta_Lambda. (5) Compare to Lambda_obs.
**Input**: s60_hessian_3d.npz, s60_pw_h0_conv.npz (a_0), Q=29.9 from s60_qtheory_geodesic.npz, E_BCS from s60_staircase_ext.npz, canonical_constants.py
**Output**: s61_a4_qtheory_compound.py/.npz — Lambda_residual, Lambda_obs comparison, regime diagram
**Gate**: A4-QT-COMPOUND-61. PASS if |Lambda_residual/Lambda_obs - 1| < 10. FAIL if > 10^5. INFO if 10 < ratio < 10^5.
**Priority**: HIGH (sole surviving CC path + new stabilization regime)
**Est. Cost**: CPU-only, algebraic. Minutes.
**Paper Reference**: Paper 10 (spectral action a_0), Paper 06 (Volovik q-theory), Paper 09 (vacuum energy). Collab Section 2(d), 3.2.
**Depends On**: PHONON-2 (alpha regime must be identified first)

### PHONON-7: Integrability Breaking Scaling with N_cells (Pillar V)
**Computation**: RG-INTEGRALS-60: delta_k = 0.328 at N_cells = 32. The Josephson term acts as COLLECTIVE perturbation — mode-independent (nearly identical for all 8 integrals), standard JJ array QPT (Paper 19, Fazio-van der Zant). At E_J/E_C = 194 (deep superfluid), system maximally delocalized. GGE survival depends on scaling: delta_k ~ N^{-beta}. beta > 0: integrability restored in thermodynamic limit, GGE permanent. beta = 0: Josephson is relevant perturbation, thermalizes to Gibbs.
**Method**: (1) For each N_cells = 2,4,8,16,32,64, construct Richardson-Gaudin integrals I_k. (2) Add H_J. (3) delta_k = ||[I_k, H_J]||/||I_k||. (4) Fit delta_k(N) ~ N^{-beta}.
**Input**: BCS Hamiltonian from canonical_constants.py, E_J = 7 M_KK, Richardson-Gaudin integrals from S57
**Output**: s61_integrability_scaling.py/.npz/.png — delta_k(N), scaling exponent beta
**Gate**: INTEG-SCALING-61. PASS if beta > 0.5. FAIL if beta < 0.1. INFO if 0.1-0.5.
**Priority**: HIGH (directly determines GGE/DM survival — complements PHONON-3)
**Est. Cost**: GPU for N=32,64. Hours.
**Paper Reference**: Paper 19 (Fazio-van der Zant), Paper 22 (Haviland), Paper 20 (Fisher Mott). Collab Section 2(c), 5 Q2.
**Depends On**: none (cross-checks PHONON-3)
**Cross-agent contributions**:
- LANDAU-5: Lanczos for N=8 (dim ~4.4e9); power-law fit; Claeys Paper 24; Dukelsky-Pittel-Sierra Paper 17
- VOL-3: 3He-B analog: bulk relaxation rate scales as inverse sample volume (surface scattering dominates at low T); integrability threshold crossing

### PHONON-8: BCS Phase Boundary vs Soliton Domain Wall (Pillar II x VI)
**Computation**: With fold = SA maximum (S60), DW at tau_DW = 0.1135 is NOT between two SA minima. In soliton theory (Paper 23), DWs form at potential saddles; solitons interpolate between minima. If fold is maximum, DW and fold not separated by a_2 barrier. The relevant wall may be a BCS phase boundary (Lifshitz transition, Paper 08), a topological Dirac spectrum transition, or an A-B interface analog (Paper 07, Jacobson-Volovik). Lichnerowicz near-minimum (0.0025) is geometric near-criticality. The instability is NOT in the TT sector — where is it?
**Method**: (1) At tau_DW, BCS Delta(tau) and d^2 Delta/dtau^2 — discontinuity = 2nd-order Lifshitz. (2) D_K eigenvalue zero crossings through tau_DW (topological transition). (3) Pfaffian Z_2 on both sides (S35 data). (4) Compare to 3He A-B interface (Paper 07).
**Input**: D_K eigenvalues at 50+ tau bracketing tau_DW, BCS Delta(tau), Pfaffian data from S35
**Output**: s61_dw_classification.py/.npz/.png — Lifshitz/topological/A-B classification, eigenvalue flow, Pfaffian comparison
**Gate**: DW-CLASS-61. PASS if cleanly classifiable. FAIL if no transition (artifact). INFO if ambiguous.
**Priority**: LOW (structural classification)
**Est. Cost**: CPU-only, existing data. Minutes.
**Paper Reference**: Paper 07 (Jacobson-Volovik), Paper 08 (Lifshitz), Paper 23 (kinks), Paper 25 (Z_N walls). Collab Section 4, 5 Q4.
**Depends On**: none

### PHONON-9: Twisted Spectral Triple for CP Violation (Pillar III)
**Computation**: The J-wall (BDI, T^2=+1) is the cosmological Mermin-Ho constraint (3He-B, Paper 06 Ch. 7): T^2=+1 forces real symmetric spectrum, eta = 0 identically. Eta vanishing, leptogenesis closure, baryogenesis closure = three projections of one structural fact. NCG escape: twisted spectral triples (Connes-Devastato-Lizzi-Martinetti). Does the Jensen deformation generate a twist sigma with nonzero eta?
**Method**: (1) Check if a->a(tau) defines twist with [D,a]_sigma bounded. (2) sigma-twisted J-reality. (3) T^2 under twist. (4) If T^2 != +1, compute eta at fold.
**Input**: D_K(tau) matrix, J operator, algebra A, tau
**Output**: s61_twisted_triple.py/.npz — sigma(tau), modified T^2, eta if T^2 != +1
**Gate**: TWIST-CP-61. PASS if nonzero eta. FAIL if no twist or eta=0. INFO if eta exponentially small.
**Priority**: LOW (exploratory CP channel)
**Est. Cost**: CPU-only, algebraic. Hours (conceptual difficulty).
**Paper Reference**: Paper 14 (BDI), Paper 10 (axioms), arXiv:1304.7007. Collab Section 1 Pattern 2, Section 4.
**Depends On**: none

### PHONON-12: Nuclear Odd-Even Staggering in CC Staircase (Pillar IV)
**Computation**: STAIRCASE-EXT-60 oscillation of |Lambda_residual| with N_pair = nuclear odd-even staggering (Paper 03): pairing gap oscillates with particle number. Delta^{(3)}(N) = (-1)^N * [E(N+1)-2E(N)+E(N-1)]/2. Oscillation rules out monotone CC convergence but expected from BCS. Amplitude O(M_KK^4) not O(Lambda_obs) — staircase steps 113 OOM too tall. The staggering pattern classifies BCS-BEC crossover position.
**Method**: (1) E_GS(N=0..8) from s60_staircase_ext.npz. (2) Delta^{(3)}(N). (3) Compare to Delta_BCS. (4) Nuclear systematics: 12/A^{1/2} MeV -> ? * M_KK. (5) Weak = smooth stagger; strong = large.
**Input**: s60_staircase_ext.npz, Delta_BCS
**Output**: s61_oddeven_stagger.py/.npz/.png — Delta^{(3)}(N), nuclear comparison, BCS-BEC classification
**Gate**: ODDEVEN-61. INFO (diagnostic — classifies pairing, validates nuclear analogy).
**Priority**: LOW (cross-domain diagnostic)
**Est. Cost**: CPU-only, arithmetic. Seconds.
**Paper Reference**: Paper 03 (nuclear BCS odd-even). Collab Section 2(d).
**Depends On**: none

**Source files**: `sessions/archive/session-60/session-60-phonon-collab.md`


---

## Connes NCG Theorist

### CONNES-1: Spectral Zeta Zero Location (Finite Dirichlet Series)
**Computation**: Construct zeta_{D_K}(s) = sum_{n=1}^{N} |lambda_n|^{-s} from the Peter-Weyl eigenvalue data at the fold (tau=0.19, 10 sectors, 9280 eigenvalues). This is a finite Dirichlet series. Locate ALL nontrivial zeros in the critical strip 0 < Re(s) < 8 using numerical root-finding. Classify the result as: (a) zeros scatter broadly (no GRH structure), (b) zeros cluster near Re(s)=4 (GRH-type, functional equation prediction), or (c) zeros cluster near Re(s)=sigma_0 != 4 (non-standard functional equation from broken bi-invariance). This is the single computation identified in Addendum D5 as the natural terminus of the 0D spectral perspective.
**Method**: Evaluate the finite sum sum_n |lambda_n|^{-s} on a grid in the complex s-plane (Re(s) in [0,8], Im(s) in [-50,50], grid spacing 0.1). Use Newton-Raphson or Muller's method to refine zeros from grid candidates where |zeta| drops below threshold. Verify by checking |zeta(s_0)| < 1e-10 at each root. Repeat at 3+ truncation levels (5, 7, 10 sectors) to test convergence of the zero distribution as PW sectors are added.
**Input**: Existing D_K eigenvalue data at tau=0.19 from computation-archive (s24a_vspec.npz or equivalent PW eigenvalues). canonical_constants.py.
**Output**: s61_zeta_zeros.py, s61_zeta_zeros.npz (zero locations, truncation level, Re/Im parts), s61_zeta_zeros.png (zero scatter plot in s-plane with Re(s)=4 line marked).
**Gate**: ZETA-ZEROS-61. PASS if >80% of zeros lie within |Re(s)-4| < 0.5 AND the fraction increases with truncation level. FAIL if zeros scatter uniformly across the strip at all truncation levels. INFO if clustering occurs near a line Re(s)=sigma_0 != 4.
**Priority**: HIGH
**Est. Cost**: Minutes (CPU). Finite sum evaluation + root-finding on ~10^4 terms. No eigenvalue recomputation needed.
**Paper Reference**: Addendum C section C7 item 1, Addendum D section D5 (the central computation). Functional equation predicts critical line at Re(s)=d/4=2 for D_K^2, equivalently Re(s)=4 for D_K, from Poincare duality (C5, D4).
**Depends On**: None (uses existing eigenvalue data)

### CONNES-2: Level Spacing Statistics at the Fold (GUE/GOE/Poisson)
**Computation**: Compute the nearest-neighbor spacing distribution P(s) of the D_K eigenvalues at the fold (tau=0.19) after unfolding to unit mean spacing. Compare against GUE (Montgomery-Odlyzko universality class for Riemann zeros), GOE (expected for time-reversal-invariant BDI class), and Poisson (integrable). Compute the number variance Sigma^2(L) and spectral rigidity Delta_3(L) as secondary diagnostics.
**Method**: Unfold the spectrum via the staircase function N(lambda). Compute the spacing ratios r_n = (lambda_{n+1} - lambda_n) / (lambda_n - lambda_{n-1}). Histogram P(s) and fit to Wigner surmise for GOE (P ~ s*exp(-pi*s^2/4)), GUE (P ~ s^2*exp(-4*s^2/pi)), or Poisson (P ~ exp(-s)). Use sectors separately and combined.
**Input**: D_K eigenvalues at tau=0.19, all 10 PW sectors.
**Output**: s61_level_spacing.py, s61_level_spacing.npz (unfolded spacings, P(s) histogram, Sigma^2(L), Delta_3(L)), s61_level_spacing.png.
**Gate**: LEVEL-STATS-61. INFO (classification only). Report which universality class (GOE/GUE/Poisson) best fits each sector and the combined spectrum. If GUE: flag for zeta connection follow-up. If GOE: consistent with BDI time-reversal symmetry, no direct prime connection. If Poisson: integrable regime confirmed (consistent with CHAOS-1 from S38).
**Priority**: MED
**Est. Cost**: Minutes (CPU). Statistical analysis of existing eigenvalue data.
**Paper Reference**: Addendum C section C7 item 3. Montgomery-Odlyzko conjecture for Riemann zeros (GUE universality). CHAOS-1 from S38 found <r>=0.321 (sub-Poisson).
**Depends On**: None (uses existing eigenvalue data)

### CONNES-3: Functional Equation and J-Symmetry Constraints on Zeros
**Computation**: (a) Verify that the eta function eta(s) = sum_n sign(lambda_n)|lambda_n|^{-s} vanishes IDENTICALLY (not just at s=0) by evaluating at 50+ complex s values with Re(s) > 4 and checking |eta(s)| < epsilon. This is forced by J-symmetry pairing +lambda_n with -lambda_n at identical multiplicity (Addendum D4, new observation). (b) Construct the functional equation of zeta_{D_K^2}(s) numerically: compute zeta_{D_K^2}(s) and zeta_{D_K^2}(4-s) at 100+ points and verify the functional relation zeta(s) = C(s)*zeta(4-s) for an explicit C(s). (c) Test whether the Poincare duality pairing of the spectral triple imposes additional constraints beyond the standard heat kernel functional equation.
**Method**: Direct evaluation of finite Dirichlet series for eta(s) and zeta_{D_K^2}(s). For the functional equation, compute the ratio zeta(s)/zeta(4-s) and check whether it matches the Gamma-function form predicted by the heat kernel (Seeley 1967). For Poincare duality constraints, compute the intersection form on K_0(A_F) = Z^3 and verify its effect on the spectral zeta symmetry.
**Input**: D_K eigenvalues (all tau), D_K^2 eigenvalues. K_0 generators from A_F = C + H + M_3(C).
**Output**: s61_functional_eq.py, s61_functional_eq.npz (eta(s) values, functional equation ratio C(s), Poincare duality pairing matrix), s61_functional_eq.png.
**Gate**: FUNC-EQ-61. PASS if (a) |eta(s)| < 1e-12 at all tested points AND (b) functional equation holds to machine precision with identifiable C(s). FAIL if functional equation breaks at deformed tau (would indicate Jensen deformation spoils standard spectral symmetry). INFO if C(s) has non-standard form.
**Priority**: HIGH
**Est. Cost**: Minutes (CPU). Finite sum evaluation at complex points.
**Paper Reference**: Addendum C section C7 item 5 and C5 (physical consistency constrains analytic structure). Addendum D section D4 (eta identically zero observation, chain: J-symmetry -> spectral pairing -> Weil positivity -> zeros on critical line). Seeley 1967, ETA-INVARIANT-60.
**Depends On**: None (uses existing eigenvalue data). Results inform interpretation of CONNES-1.

### CONNES-4: Heat Kernel Trace Formula -- Geometric Side (Conjugacy Class Integrals)
**Computation**: Compute the GEOMETRIC SIDE of the trace formula for D_K on Jensen-deformed SU(3). The spectral side (sum over eigenvalues weighted by a test function h) is known from PW data. The geometric side involves integrals over conjugacy classes of SU(3) with the Jensen metric. For bi-invariant SU(3) (tau=0), the conjugacy classes are parametrized by the maximal torus T^2 and the integral is elementary via the Weyl integration formula. For the Jensen-deformed case, the broken bi-invariance modifies the integral kernel. Compute for tau=0 (verification) and tau=0.19 (fold). The geometric side gives the "geometric primes" -- the closed geodesics and their lengths -- which are the SU(3) analog of the rational primes.
**Method**: Parametrize conjugacy classes of SU(3) by the maximal torus T^2 = {diag(e^{i*theta_1}, e^{i*theta_2}, e^{-i*(theta_1+theta_2)})}. For the bi-invariant metric, use the Weyl integration formula with the Weyl denominator delta(t)^2. For the Jensen metric, compute the modified volume factor from the metric tensor restricted to conjugacy classes. Evaluate K(t,g,g) integrated over each conjugacy class. Compare spectral side sum d(p,q)^2 * h(lambda_{(p,q)}) against geometric side at both tau values.
**Input**: Jensen metric tensor components at tau=0 and tau=0.19. PW eigenvalues. SU(3) root system and Weyl group data.
**Output**: s61_trace_formula_geometric.py, s61_trace_formula_geometric.npz (conjugacy class integrals, geometric primes list with lengths, spectral-geometric side comparison), s61_trace_formula_geometric.png.
**Gate**: TRACE-FORMULA-61. PASS if spectral and geometric sides agree to <1% at tau=0 (verification) AND the geometric side is computable at tau=0.19 (fold). FAIL if agreement >5% at tau=0 (indicates error in either side). INFO if geometric side is computable but lists fewer than 50 primitive geodesics at the fold.
**Priority**: MED
**Est. Cost**: Hours (CPU). Conjugacy class parametrization + numerical integration over T^2 for each test function.
**Paper Reference**: Addendum C section C3 (trace formula on Lie groups, explicit SU(3) formula with Weyl denominator), C7 item 4. Duistermaat-Guillemin 1975, Fried 1986.
**Depends On**: None, but results feed into VDD-16 (geometric primes required for Ruelle construction).

### CONNES-6: Weil Positivity Test for Jensen-Deformed SU(3)
**Computation**: Test the Weil positivity criterion Tr(f * f-tilde) >= 0 for the spectral triple on Jensen-deformed SU(3). In Connes' formulation (1999), the GRH for zeta_{D_K}(s) is equivalent to this positivity. Evaluate the Weil distribution W(f) = sum_rho f-hat(rho) + (smooth terms) for a family of test functions f. This bridges the gap in the chain: J-symmetry -> spectral pairing -> [GAP] -> Weil positivity -> zeros on critical line (Addendum D4).
**Method**: (1) Construct the Weil distribution from the spectral zeta zeros (CONNES-1). (2) Evaluate W(f) for Hermite functions and Gaussians of varying width. (3) Minimize W(f) over the test function space. If minimum >= 0, positivity holds numerically.
**Input**: Spectral zeta zeros from CONNES-1. Test function basis (Hermite functions up to order 50).
**Output**: s61_weil_positivity.py, s61_weil_positivity.npz (W(f) values, minimum over test functions, convergence with basis size), s61_weil_positivity.png.
**Gate**: WEIL-POS-61. PASS if min W(f) >= 0 for all tested f (100+ functions). FAIL if min W(f) < 0 for any f (GRH violated). INFO if positivity holds but margin <1% of |W| scale.
**Priority**: MED
**Est. Cost**: Minutes (CPU) after CONNES-1 zeros are available.
**Paper Reference**: Addendum C section C1 (Weil positivity = RH equivalence, Connes 1999). Addendum D section D4 (the chain with the gap).
**Depends On**: CONNES-1 (requires spectral zeta zeros)

### CONNES-7: Spectral Zeta Residues vs Physical Constants (Self-Consistency)
**Computation**: Verify that the residues of zeta_{D_K^2}(s) at poles s=4,3,2 (Seeley-DeWitt coefficients a_0, a_2, a_4) yield consistent physical constants: (a) positive G_N from Res_{s=3}, (b) gauge coupling ratios from Res_{s=2}/Res_{s=3}, (c) bounded-below Higgs potential from Res_{s=2}. Cross-check a_2 against USER-2 (Milnor formula). Test whether these residue constraints combined with the functional equation (CONNES-3) restrict zero locations beyond generic compact manifold expectations. The relation a_k = Res_{s=(d-k)/2} Gamma(s)*zeta_{D_K^2}(s) was established in Addendum C2.
**Method**: Compute Res_{s=k} zeta_{D_K^2}(s) = lim_{s->k} (s-k)*zeta_{D_K^2}(s) numerically at each pole. Convert to a_0, a_2, a_4. Derive G_N, gauge couplings, Higgs parameters via Chamseddine-Connes-Marcolli dictionary.
**Input**: D_K^2 eigenvalues at fold (tau=0.19) and round (tau=0). canonical_constants.py.
**Output**: s61_zeta_residues.py, s61_zeta_residues.npz (residues at s=2,3,4; derived physical constants; comparison with USER-2).
**Gate**: ZETA-RESIDUES-61. PASS if a_2 from zeta residue matches USER-2 Milnor result to <5% AND G_N > 0. FAIL if a_2 disagrees by >20%. INFO if residues consistent but gauge couplings remain 54% off (reconfirms RGE-33a closure).
**Priority**: MED
**Est. Cost**: Minutes (CPU). Pole extraction from finite Dirichlet series.
**Paper Reference**: Addendum C section C2 (zeta residues = Seeley-DeWitt coefficients), C5 (physical consistency constrains analytic structure). Chamseddine-Connes-Marcolli 2007.
**Depends On**: USER-2 (for a_2 cross-check). CONNES-3 (for functional equation context).

### CONNES-8: Connes Distance Between Spectral Projections (Eigenvalues as Points)
**Computation**: Compute the Connes distance d(P_m, P_n) = sup{|phi_m(a) - phi_n(a)| : ||[D,a]|| <= 1} between spectral projections of D_K at the fold, formalizing Addendum D3: "eigenvalues ARE points" in the noncommutative geometry. Map the distance matrix d(P_m, P_n) for the first 50 eigenvalue pairs. Determine whether fine structure of these distances correlates with zeta_{D_K}(s) zeros from CONNES-1 -- zeros control counting function deviation from Weyl asymptotics, which determines eigenvalue clustering and hence inter-eigenvalue Connes distances (Addendum D2).
**Method**: For each pair (m,n), solve the SDP: maximize |<psi_m, a*psi_m> - <psi_n, a*psi_n>| subject to ||[D,a]|| <= 1 over a in A_F. Use CLARABEL SDP solver (validated S54, 0.16s/pair). Compare distance matrix against eigenvalue gaps |lambda_m - lambda_n| and against oscillatory contributions from spectral zeta zeros.
**Input**: D_K eigenvalues and eigenvectors at tau=0.19. A_F generators. CLARABEL solver.
**Output**: s61_connes_distance_projections.py, s61_connes_distance_projections.npz (50x50 distance matrix, correlation with eigenvalue gaps, correlation with zeta zero oscillations), s61_connes_distance_projections.png.
**Gate**: CONNES-DIST-PROJ-61. INFO (characterization). Report whether d(P_m, P_n) is monotone in |lambda_m - lambda_n| (reduces to eigenvalue gap) or non-monotone (genuine noncommutative metric beyond spectral axis). Report correlation coefficient between distance matrix and zeta-zero oscillation pattern.
**Priority**: LOW
**Est. Cost**: Hours (CPU). 1225 SDP solves at ~0.16s each.
**Paper Reference**: Addendum D section D3 (eigenvalues as points, J-paired real points), D2 (explicit formula: fine structure controlled by zeta zeros). S46 CONNES-DISTANCE-46, S54 CONNES-LATT-54 for SDP methodology.
**Depends On**: CONNES-1 (for zeta zero locations to test correlation)

**Source files**: `sessions/archive/session-60/framework-3HeB-comparison.md` (Addenda C & D)

---

## Van den Dungen Bridge Theorist

### VDD-2: Kasparov Factorization Verification with O'Neill Cross-Terms
**Computation**: Verify that the spectral action on M^4 x SU(3) correctly decomposes into base + fiber contributions by computing the O'Neill A-tensor and T-tensor of the submersion pi: M^4 x SU(3) -> M^4. For product metric, confirm A = T = 0 (exact factorization). Then re-check when gauge connections are introduced via inner fluctuations A_gauge = sum a_i [D, b_i], determining whether the effective metric acquires off-diagonal terms that make A, T non-zero and produce cross-terms in the spectral action.
**Method**: (1) For product metric g_{M^4} + g_K(tau): verify horizontal vector fields have horizontal Lie brackets (A = 0) and fibers {x} x SU(3) are totally geodesic (T = 0). (2) Introduce inner fluctuations (NCG gauge connection) and recompute the effective metric on the total space. (3) If A or T become non-zero, compute the cross-term corrections to the spectral action decomposition a_2(D_total^2) = a_2(D_M^2)*a_0(D_K^2) + a_0(D_M^2)*a_2(D_K^2) + cross-terms.
**Input**: Jensen metric g_K(tau), product metric on M^4 x SU(3), inner fluctuation formula from Paper 06
**Output**: s61_oneill_crossterms.py/.npz -- A-tensor, T-tensor values; cross-term magnitude relative to direct terms
**Gate**: A-TENSOR-61 (shared with USER-4). PASS if cross-term corrections < 1% of direct terms. FAIL if > 10%. INFO if 1-10%.
**Priority**: CRITICAL (validates entire fiber-base decomposition)
**Est. Cost**: CPU only, ~1 hr. Symbolic computation of O'Neill tensors on product manifold.
**Paper Reference**: VdD Paper 01 (1811.07824) Main Theorem -- Kasparov product on submersions; O'Neill 1966 -- A-tensor, T-tensor definitions
**Depends On**: SP-1 (needs a_2 values for relative comparison)

### VDD-3: Jensen Deformation as Locally Bounded Perturbation (K-Homology Stability)
**Computation**: Verify that D_K(tau) - D_K(0) satisfies the locally bounded perturbation conditions of VdD Paper 10: ||(D_K(tau) - D_K(0)) * phi|| <= C * (||D_K(0) * phi|| + ||phi||) for all phi in Dom(D_K(0)) and all tau in [0, tau_fold]. If verified, then [D_K(tau)] = [D_K(0)] in K-homology for all tau, meaning KO-dimension 6, Pfaffian Z_2 = -1, and all topological invariants are preserved along the entire Jensen path.
**Method**: (1) Express D_K(tau) - D_K(0) as a first-order differential operator with tau-dependent coefficients on (SU(3), g_K(0)). (2) Bound the coefficients using compactness of SU(3) and smoothness of the Jensen deformation in tau. (3) Find explicit constant C(tau) and verify it is finite for all tau in [0, 0.19]. (4) Alternatively, verify numerically using PW eigenvalue data: check that |lambda_n(tau) - lambda_n(0)| / (|lambda_n(0)| + 1) is bounded uniformly in n for each tau.
**Input**: D_K eigenvalue data at tau = 0 and multiple tau values from existing PW computations, canonical_constants.py
**Output**: s61_perturbation_bound.py/.npz -- bound constant C(tau), verification at each tau point, K-homology stability verdict
**Gate**: K-HOMOLOGY-STABILITY-61. PASS if C(tau) < infinity for all tau in [0, 0.19]. FAIL if unbounded. INFO if bounded but C > 100.
**Priority**: HIGH (proves topological invariance along Jensen path)
**Est. Cost**: CPU, ~30 min. Uses existing eigenvalue data for numerical check; analytic argument for formal proof.
**Paper Reference**: VdD Paper 10 (1608.02506) Theorem 3.4 -- K-homology invariance under locally bounded perturbations
**Depends On**: none (uses existing PW eigenvalue data)

### VDD-4: Spectral Flow of D_K(tau) from tau = 0 to tau_fold
**Computation**: Compute the spectral flow sf(D_K(tau)) as tau varies from 0 to tau_fold = 0.19. The spectral flow counts the net number of eigenvalues crossing zero (with signs). This is an INTEGER by Paper 12's APS index theorem. Compare with S_inst = 0.069 from S37-38. Paper 13's Callias endpoint theorem: sf depends ONLY on the tau = 0 and tau = tau_fold spectra, not on the path.
**Method**: (1) From existing PW eigenvalue data at multiple tau values, track each eigenvalue as a function of tau. (2) Count eigenvalue zero-crossings: +1 for upward crossing, -1 for downward crossing. (3) Sum over all sectors to get total sf(D_K). (4) Verify endpoint dependence by computing sf directly from the tau = 0 and tau_fold spectra.
**Input**: D_K eigenvalue data at dense tau sampling (existing PW data from 60 sessions)
**Output**: s61_spectral_flow.py/.npz -- sf(D_K) integer value, eigenvalue crossing plot, comparison with S_inst = 0.069
**Gate**: SPECTRAL-FLOW-61. PASS if sf = 0 (consistent with S_inst not being topological). FAIL if sf != 0 but inconsistent with S_inst interpretation. INFO if sf != 0 and provides new topological invariant.
**Priority**: HIGH (resolves tension between integer spectral flow and non-integer S_inst = 0.069)
**Est. Cost**: CPU, ~20 min. Eigenvalue tracking from existing data.
**Paper Reference**: VdD Paper 12 (2004.01085) -- APS index = spectral flow; Paper 13 (2312.17600) -- endpoint dependence theorem
**Depends On**: none (uses existing PW eigenvalue data)
**Cross-agent contributions**:
- VDD-11: If sf=0: reinterpret S_inst=0.069 as WKB semiclassical tunneling amplitude exp(-S_inst)=0.933 (93% tunneling probability). Gate: SF-SINST-61

### VDD-5: Order-One Condition vs Paper 05 Gauge Module Conditions
**Computation**: Check whether D_K on Jensen-deformed SU(3) defines a gauge module in the sense of VdD Paper 05, even though the standard order-one condition [[D_F, a], JbJ^{-1}] = 0 fails at 4.000 for the (H,H) sub-block. Gauge modules (Paper 05 with van Suijlekom) have different compatibility conditions from the order-one condition and can support legitimate NCG gauge theories on non-trivial principal bundles.
**Method**: (1) Extract the gauge module conditions from Paper 05 Section 3: compatibility of representation with gauge structure + anomaly cancellation. (2) Evaluate these conditions for the algebra A_F (commutant of right U(2) action on C^16), the Hilbert space H_F = C^16, and D_K(tau) at multiple tau values. (3) Determine whether D_K defines a gauge module (principal module is a proper superset of gauge module). (4) If yes, determine the gauge group of the gauge module and compare with SU(3) x SU(2) x U(1).
**Input**: A_F algebra structure (from Sessions 6-10), D_K matrix representation in the C^16 spinor basis, J_C (Connes real structure) matrix
**Output**: s61_gauge_module_check.py/.npz -- gauge module verdict, comparison with order-one, gauge group identification
**Gate**: GAUGE-MODULE-61. PASS if D_K defines a gauge module with SM gauge group. FAIL if gauge module conditions also fail. INFO if gauge module exists but with different gauge group.
**Priority**: HIGH (determines whether framework is legitimate NCG gauge theory despite order-one failure)
**Est. Cost**: CPU, ~1 hr. Algebraic verification on C^16 space.
**Paper Reference**: VdD Paper 05 (1405.5368) Section 3 -- gauge modules on non-trivial principal bundles; Paper 06 (1204.0328) Section 2.5 -- order-one condition
**Depends On**: none

### VDD-6: Transit Spectral Action from Families of Spectral Triples (Paper 02)
**Computation**: Compute the spectral action ALONG the transit path tau in [0, tau_fold] using Paper 02's Product Spectral Triple Theorem. The total Dirac operator is D_transit = d/dtau tensor 1 + 1 tensor D_K(tau), and the spectral action factorizes as Tr(f(D_transit)) = integral_0^{tau_fold} Tr(f(D_K(tau))) dtau + correction terms from d/dtau. This is the S38 paradigm shift computation: transit dynamics, not static minimum.
**Method**: (1) Compute Tr(f(D_K(tau)^2/Lambda^2)) at 50 tau points using existing eigenvalue data and a smooth cutoff function f. (2) Integrate over tau to get the leading term. (3) Compute the d/dtau correction terms from the rate of change of the eigenvalues: d lambda_n / d tau at each point. (4) Compare total transit spectral action with static spectral action at tau_fold.
**Input**: D_K(tau) eigenvalues at 50 tau points, canonical_constants.py, cutoff function choice
**Output**: s61_transit_spectral_action.py/.npz/.png -- transit SA vs static SA, correction term magnitude, tau-resolved plot
**Gate**: TRANSIT-SA-61 (shared with USER-3). PASS if transit SA differs from static SA by > 10%. FAIL if < 1%. INFO if 1-10%.
**Priority**: CRITICAL (implements S38 paradigm shift)
**Est. Cost**: GPU recommended for eigenvalue computation at 50 tau points; ~30 min total.
**Paper Reference**: VdD Paper 02 (1711.07299) Theorem 3.1 -- Product Spectral Triple from families; Section 4 -- spectral action factorization along time-slices
**Depends On**: SP-1 (needs a_2 for calibration)

### VDD-7: First Explicit Kasparov Product Verification on Non-Trivial Fiber
**Computation**: Use the PW eigenvalue dataset for D_K(tau) on Jensen-deformed SU(3) to perform the FIRST computational verification of the Kasparov factorization theorem [D_M] = pi_! tensor [D_B] on a non-trivial compact fiber. "Non-trivial" = Jensen deformation breaks bi-invariance while preserving U(2) symmetry. This is a mathematical result independent of the physical framework.
**Method**: (1) Compute the K-homology class [D_K] from the spectral data (index, kernel dimension, spectral asymmetry). (2) Compute the Kasparov product [D_K] tensor [D_{M^4}] using the intersection product in KK-theory. (3) Compare with the direct computation of [D_{M^4 x SU(3)}] for the product Dirac operator. (4) Verify agreement as required by Paper 01 Main Theorem.
**Input**: Full PW eigenvalue dataset across 10 sectors and multiple tau values, D_{M^4} spectral data (standard Dirac on flat torus or S^4)
**Output**: s61_kasparov_product_verification.py/.npz -- K-homology classes, Kasparov product computation, agreement verification
**Gate**: KASPAROV-VERIFY-61. PASS if factorization holds to numerical precision. FAIL if factorization violated. INFO if partial verification (subset of sectors).
**Priority**: MED (mathematically significant independent result, not blocking other computations)
**Est. Cost**: CPU, ~2 hr. K-theory computation from spectral data is algebraic but multi-step.
**Paper Reference**: VdD Paper 01 (1811.07824) Main Theorem and Fundamental Class Factorization
**Depends On**: VDD-2 (O'Neill cross-terms must be computed first)

### VDD-8: Shriek Map vs Baptista Fiber Integration Equivalence
**Computation**: Verify that VdD's shriek map pi_! (K-theoretic pushforward via Kasparov product) and Baptista's fiber integration (Paper 13 eq 3.41, integration of differential forms along fibers using g_K volume form) implement the same mathematical operation for the Jensen-deformed SU(3) fiber. Standard in the commutative case via Atiyah-Singer, but specific verification needed for Jensen-deformed metric.
**Method**: (1) Compute the K-homology class of D_K and its pushforward pi_! via the Kasparov product. (2) Compute Baptista's fiber integration of the Dirac index density using vol_{g_K(tau)}. (3) Compare the resulting objects on the base M^4. (4) Verify the three conditions for equivalence: fiber compact (yes), D_K self-adjoint (yes), submersion Riemannian (yes, g_K positive definite for all tau).
**Input**: D_K spectral data, vol_{g_K(tau)} (Haar measure * det(g_K)^{1/2}), Baptista Paper 13 eq 3.41
**Output**: s61_shriek_vs_fiberint.py/.npz -- pushforward comparison, equivalence verification
**Gate**: SHRIEK-EQUIV-61. PASS if shriek map = fiber integration to numerical precision. FAIL if they differ. INFO if agreement on index but not on full K-homology class.
**Priority**: MED (validates the bridge between Baptista and Connes formalisms)
**Est. Cost**: CPU, ~1 hr. Algebraic/analytic comparison.
**Paper Reference**: VdD Paper 01 (1811.07824) Fundamental Class Factorization; Baptista Paper 13 eq 3.41
**Depends On**: VDD-7 (Kasparov product computation provides the shriek map data)

### VDD-9: BdG Spectral Action (Finite-Density Extension)
**Computation**: Compute the Seeley-DeWitt coefficients a_n(D_K^{BdG}) for the Bogoliubov-de Gennes Dirac operator D_K^{BdG} (BCS condensate modifies D_K). Compare with a_n(D_K) to quantify the back-reaction of the condensate on the spectral geometry. This is the FIRST application of the NCG spectral action to a BCS system.
**Method**: (1) Construct D_K^{BdG} from D_K and the BCS pairing potential Delta in the B2 sector. (2) Compute the BdG eigenvalue spectrum via diagonalization. (3) Compute a_0, a_2, a_4 for D_K^{BdG} using the heat kernel formula (same Gilkey-Seeley formula but with modified operator). (4) Compare delta_a_n = a_n(D_K^{BdG}) - a_n(D_K) -- this is the condensate's back-reaction on spacetime geometry.
**Input**: D_K eigenvalues (existing), BCS pairing potential from S34-38 (E_cond = -0.137 M_KK), BdG matrix from S34
**Output**: s61_bdg_spectral_action.py/.npz -- a_n(D_K^{BdG}), delta_a_n, back-reaction magnitude
**Gate**: BDG-SA-61. PASS if delta_a_2/a_2 < 0.01 (condensate perturbative on geometry). FAIL if delta_a_2/a_2 > 1 (condensate dominates geometry). INFO if 0.01-1.
**Priority**: MED (connects instanton gas physics of S37-38 to spectral action)
**Est. Cost**: GPU recommended, ~1 hr. BdG diagonalization + heat kernel computation.
**Paper Reference**: VdD Paper 01 (1811.07824) -- factorization extends to modified operators; Paper 06 (1204.0328) Section 3 -- Seeley-DeWitt expansion
**Depends On**: SP-1 (needs baseline a_2 for comparison)

### VDD-10: Block-Diagonal Theorem Generality (Left-Invariance vs SU(3)-Specific)
**Computation**: Determine whether the exact block-diagonality of D_K in PW sectors (S22b, verified to 8.4e-15) is a consequence of left-invariance of the Jensen metric alone, or requires the specific SU(3) representation theory. If left-invariance alone suffices, the result generalizes to ANY left-invariant metric on ANY compact Lie group. If SU(3)-specific, it constrains which groups can replace SU(3) in the framework.
**Method**: (1) Write the general proof for left-invariant metrics: if g is left-invariant, does the Dirac operator commute with the PW projection operators P_{(p,q)}? (2) Test on SU(2) with a left-invariant but non-bi-invariant metric (Berger sphere) as a simpler verification. (3) If the proof requires specific properties of SU(3) (e.g., the specific form of the Clebsch-Gordan decomposition), identify the minimal algebraic condition.
**Input**: D_K block-diagonal data from S22b, su(3) structure constants, SU(2) structure constants for comparison
**Output**: s61_block_diagonal_generality.py/.md -- proof or counterexample, SU(2) verification, minimal conditions identified
**Gate**: BLOCK-DIAG-GENERAL-61. PASS if left-invariance alone suffices (universal result). FAIL if SU(3)-specific. INFO if true for semisimple groups but not all compact groups.
**Priority**: MED (mathematical generalization -- determines which groups are compatible with framework)
**Est. Cost**: CPU, ~2 hr. Algebraic proof + SU(2) numerical verification.
**Paper Reference**: VdD Paper 01 (1811.07824) -- sector decomposition in K-homology; S22b D_K block-diagonality theorem
**Depends On**: none

### VDD-12: Jensen Moduli Space Completeness (36-Dimensional Hessian)
**Computation**: HESSIAN-3D-60 found the fold is a maximum in the 3D subspace (tau, sigma, delta_1). The full moduli space of left-invariant metrics on SU(3) is 36-dimensional (positive-definite symmetric 8x8 matrix on Lie algebra). Determine whether the fold is a maximum in ALL 36 directions or becomes a saddle/minimum in some unexplored direction. NCG axioms (KO-dim 6, reality condition) impose constraints on admissible metrics -- the effective moduli space is a constrained submanifold.
**Method**: (1) Parametrize the 36D space of left-invariant metrics on su(3). (2) Identify constraints from KO-dim 6, J^2 = +1, volume preservation. (3) Compute the restricted Hessian of the spectral action on the constrained moduli space at the fold point. (4) Determine the index (number of negative eigenvalues) of the restricted Hessian.
**Input**: Jensen metric at tau_fold = 0.19, su(3) structure constants, HESSIAN-3D-60 results
**Output**: s61_moduli_hessian.py/.npz -- 36D Hessian eigenvalues at fold, constraint surface dimension, index
**Gate**: MODULI-HESS-61. PASS if fold is maximum on full constraint surface (all Hessian eigenvalues <= 0). FAIL if fold is saddle (some positive eigenvalues). INFO if degenerate (some zero eigenvalues indicating flat directions).
**Priority**: MED (determines whether Jensen family captures the true extremum or is a restricted artifact)
**Est. Cost**: GPU recommended, ~4 hr. Requires D_K eigenvalue computation along 36 independent perturbation directions.
**Paper Reference**: VdD Paper 10 (1608.02506) -- perturbation stability on connected components of moduli space; S60 HESSIAN-3D-60
**Depends On**: VDD-3 (K-homology stability determines which moduli directions are topologically equivalent)

### VDD-13: Paper 05 Topological Corrections from Non-Trivial Bundle
**Computation**: When gauge fields are present, M^4 x SU(3) as a principal SU(3)-bundle has a non-trivial connection. Paper 05 shows non-trivial bundles produce topological corrections to the spectral action: Chern classes, instanton numbers, anomaly terms. Verify whether the S37 instanton number S_inst = 0.069 is related to the topological charge via ind(D_total) = integral of second Chern class.
**Method**: (1) Compute the second Chern class c_2 of the principal SU(3)-bundle M^4 x SU(3) with the gauge connection from inner fluctuations. (2) Evaluate the integral of c_2 over M^4. (3) Compare with ind(D_total) from the Kasparov product. (4) Relate to S_inst = 0.069.
**Input**: Gauge connection from inner fluctuations, SU(3) bundle topology, S37 instanton data
**Output**: s61_chern_topological.py/.npz -- c_2 integral, index comparison, S_inst relation
**Gate**: CHERN-INST-61. PASS if ind(D_total) = integer and relates to S_inst via WKB. FAIL if contradicts S_inst interpretation. INFO if ind = 0 (trivial topology).
**Priority**: LOW (connects instanton physics to bundle topology -- mathematically important but not blocking)
**Est. Cost**: CPU, ~1 hr. Topological computation on product bundle.
**Paper Reference**: VdD Paper 05 (1405.5368) -- topological corrections from non-trivial principal bundles; Paper 09 (1710.09206) -- ind(D+V) = Kasparov product
**Depends On**: VDD-2, VDD-4

### VDD-14: Fredholm Complex for the BdG System (Paper 14)
**Computation**: Apply Paper 14's generalized Fredholm theory (cochain complexes) to the BdG system on SU(3). The BdG naturally forms a 2-term complex 0 -> H_particle -> H_hole -> 0. Compute the K_0(A)-valued index of this complex. Determine whether it provides topological protection beyond the Z_2 Pfaffian computed in S35.
**Method**: (1) Formulate D_K^{BdG} as a morphism in a 2-term Fredholm complex. (2) Compute the K_0-valued index using Paper 14's generalized index theorem. (3) Compare with the Z_2 Pfaffian invariant (Pf = -1 at all 34 tau, from S35). (4) Determine if additional topological content exists.
**Input**: D_K^{BdG} matrix from S34, BCS pairing data, S35 Pfaffian data
**Output**: s61_fredholm_complex_bdg.py/.npz -- K_0 index, comparison with Z_2, additional invariants
**Gate**: FREDHOLM-BDG-61. PASS if K_0 index non-trivial (additional protection beyond Z_2). FAIL if K_0 index trivial (Z_2 captures all topology). INFO if computation reveals unexpected structure.
**Priority**: LOW (refines topological classification of BCS condensate)
**Est. Cost**: CPU, ~2 hr. Algebraic computation in K-theory.
**Paper Reference**: VdD Paper 14 (2505.07568) -- Fredholm complexes of unbounded operators; S35 Pfaffian data
**Depends On**: VDD-9 (BdG spectral action provides the operator data)

### VDD-16: Ruelle Zeta Function and Arithmetic Content (Speculative)
**Computation**: Compute the Ruelle zeta function of the geodesic flow on (SU(3), g_K(tau_fold)). Determine whether it factors as an Euler product over primitive closed geodesics. If it does, compare its zeros with the zeros of the spectral zeta function zeta_{D_K}(s) to test for arithmetic content. This probes whether the Connes agent's "tunnel" between spectral geometry and number theory (Addendum C/D of 3He-B comparison) is closer than expected.
**Method**: (1) Enumerate primitive closed geodesics on (SU(3), g_K(tau_fold)) using the exponential map and conjugacy class structure. (2) Construct the Ruelle zeta function Z_R(s) = prod_{gamma primitive} (1 - e^{-s*l(gamma)})^{-1}. (3) Find zeros of Z_R(s) numerically. (4) Compare with zeros of zeta_{D_K}(s) = sum_n lambda_n^{-s} (from PW eigenvalue data). (5) Statistical test for zero correlation.
**Input**: PW eigenvalue data (existing), geodesic data on SU(3) from exponential map, Jensen metric
**Output**: s61_ruelle_zeta.py/.npz/.png -- Ruelle zeros, spectral zeta zeros, correlation analysis
**Gate**: RUELLE-ARITH-61. PASS if zeros show statistically significant correlation (p < 0.01). FAIL if no correlation. INFO if correlation exists but significance marginal.
**Priority**: LOW (speculative but well-posed; mathematically significant if positive)
**Est. Cost**: CPU, ~4 hr. Geodesic enumeration + root-finding for two zeta functions.
**Paper Reference**: VdD Paper 01 (1811.07824) -- trace formula factors through shriek map; Addendum C/D of S60 3He-B comparison
**Depends On**: SP-1 (needs calibrated spectral data)
**Cross-agent contributions**:
- CONNES-5: Fried 1986 verification at tau=0; shooting method for closed geodesics; Euler product factorization relation log(Z_R(s)) vs zeta_{D_K}(s)

### VDD-17: Pseudo-Riemannian Extension to M^{3,1} x SU(3) (Lorentzian Spectral Triple)
**Computation**: Apply Papers 02-04 formalism to construct the Lorentzian spectral triple on M^{3,1} x SU(3). The indefinite Kasparov module decomposes as <indefinite, classical> = <E_+, classical> - <E_-, classical> (Paper 03 Pairing Reversibility), giving the physical spectral action as a DIFFERENCE of two Euclidean spectral actions. The SU(3) factor remains Riemannian while the M^{3,1} factor introduces the Krein space structure.
**Method**: (1) Construct the Krein space K = L^2(M^{3,1}) with Krein involution J_K (distinct from Connes' J_C). (2) Decompose into E_+ and E_- subspaces. (3) Compute <E_+, [D_K]> and <E_-, [D_K]> separately using the SU(3) spectral data. (4) Take the difference to get the physical Lorentzian spectral action. (5) Compare with the Euclidean spectral action (current framework).
**Input**: D_K spectral data (existing), Lorentzian Dirac operator on M^{3,1} (standard), Krein involution construction from Paper 03
**Output**: s61_lorentzian_spectral_triple.py/.npz -- Lorentzian SA vs Euclidean SA, Krein decomposition, correction magnitude
**Gate**: LORENTZ-SA-61. PASS if Lorentzian SA within 10% of Euclidean SA (Wick rotation valid). FAIL if > 50% difference (Wick rotation invalid). INFO if 10-50%.
**Priority**: LOW (Lorentzian extension is future work; current Euclidean framework may suffice)
**Est. Cost**: CPU, ~2 hr. Krein space construction + spectral action difference.
**Paper Reference**: VdD Paper 02 (1711.07299) Section 5 -- Lorentzian spectral triples; Paper 03 (1503.06916) -- indefinite Kasparov modules; Paper 04 (1207.2112) -- pseudo-Riemannian spectral triples
**Depends On**: SP-1 (needs Euclidean a_2 for comparison), VDD-6 (transit SA provides the baseline)

### VDD-18: Inheritance Kasparov Product at Each Compositing Level
**Computation**: The 3He-B comparison claims 22 correspondences between the substrate (SU(3) fiber) and 3He-B (Level 5 superfluid). The Kasparov product is functorial: [D_{Level N}] = [C_N] tensor ... tensor [C_1] tensor [D_0]. Compute the compositing classes [C_i] at each level (quarks, hadrons, nuclei, atoms, superfluid) and determine which of the 22 correspondences are K-theoretic inheritance vs BCS universality.
**Method**: (1) Model each compositing step as a Kasparov product with a compositing class [C_i]. (2) Track K-theoretic invariants (KO-dim mod 8, index, Z_2) through the chain. (3) For each of the 22 correspondences, classify as: (a) inherited via K-theory, (b) universal BCS property, or (c) coincidental. (4) Verify the BDI-to-DIII shift (KO-dim change by 4) at Level 5 as a consequence of the Kramers compositing class.
**Input**: 22 correspondences from framework-3HeB-comparison.md, compositing chain: substrate -> quarks -> hadrons -> nuclei -> atoms -> 3He-B
**Output**: s61_inheritance_kasparov.md -- classification of all 22 correspondences, compositing chain K-theory computation
**Gate**: INHERIT-CLASSIFY-61. PASS if >= 15/22 correspondences classified as inherited or universal (not coincidental). FAIL if >= 10/22 coincidental. INFO if classification reveals unexpected pattern.
**Priority**: LOW (theoretical -- validates the inheritance vs analogy distinction but not blocking)
**Est. Cost**: CPU, ~4 hr. Algebraic K-theory computation at each compositing level.
**Paper Reference**: VdD Paper 01 (1811.07824) -- functoriality of Kasparov product; S60 3He-B comparison Addendum B (inheritance section)
**Depends On**: VDD-7, VDD-8 (Kasparov product and shriek map provide the computational machinery)

**Source files**: `sessions/archive/session-60/session-60-vdd-framework-review.md`

---

## Spectral Geometer

### SPEC-4: Weyl Law Verification on Jensen SU(3)
**Computation**: Verify eigenvalue asymptotics N(lambda) ~ C_8*Vol*lambda^8. Independent volume measurement.
**Method**: From 48-irrep data, compute N(lambda), fit Weyl term. Compare Weyl volume to analytic Vol(SU(3)).
**Input**: s60_pw_h0_conv.npz, Vol(SU(3))
**Output**: s61_weyl_law.py/.npz/.png
**Gate**: WEYL-VERIFY-61. PASS if match within 5%. FAIL if >20%. INFO if 5-20%.
**Priority**: MED -- internal consistency check
**Est. Cost**: ~minutes.
**Paper Reference**: PW-H0-CONV-60; Weyl 1911
**Depends On**: none

### SPEC-5: Spin Connection Curvature Term in a_2
**Computation**: Compute spin connection curvature (1/12)*tr(Omega^2) in Gilkey a_2. Determine significance vs R/6*tr(id).
**Method**: omega^a_{bc} from SU(3) structure constants + Jensen metric. Omega = d_omega + omega^omega. Compare tr(Omega^2) to R^2/36.
**Input**: SU(3) structure constants, Jensen metric at fold
**Output**: s61_spin_curvature.py/.npz
**Gate**: SPIN-CURV-61. PASS if |tr(Omega^2)| < 0.1*R^2/36. FAIL if > R^2/36. INFO if 0.1-1.0.
**Priority**: HIGH -- determines whether simplified a_2 formula suffices
**Est. Cost**: ~minutes.
**Paper Reference**: Gilkey 1975; Branson-Orsted 1986
**Depends On**: none (parallel to SP-1)

**Source files**: `sessions/archive/session-60/framework-3HeB-comparison-spectral-collab.md` (if recoverable), S60 collab review completion summary

---

## Lost Treasure Cross-Domain Approaches

### LT-1: Lattice Basis Reduction (SVP on SU(3) weight lattice)
- **Input**: SU(3) weight lattice coordinates, BCS energies per sector
- **Output**: s61_lattice_svp.py/.npz
- **Gate**: LATTICE-SVP-CC. PASS if epsilon_SVP < 0.001. FAIL if ~0.046. INFO if (0.001, 0.046).
- **Who**: Cryptography / lattice reduction specialist (no agent yet)

### LT-2: Tropical Geometry (staircase as tropicalized spectral action)
- **Who**: Tropical geometry specialist (no agent yet)

### LT-3: KAM Threshold (GGE survival at delta=0.33)
- **Input**: 8-mode BCS Hamiltonian, Josephson perturbation
- **Output**: s61_kam_threshold.py/.npz
- **Gate**: KAM-THRESHOLD-61. PASS if delta < delta_KAM. FAIL if delta > delta_KAM.
- **Who**: Dynamical systems / ergodic theory (no agent yet — could use gen-physicist)

### LT-4: Coding Theory (weight lattice error correction)
- **Who**: Algebraic coding theory (no agent yet)

### LT-5: Combinatorial Number Theory (staircase q-series)
- **Input**: {E_GS(0)...E_GS(4)} from s60_staircase_ext.npz
- **Output**: s61_staircase_qseries.py/.npz
- **Gate**: Q-SERIES-MODULAR-61. PASS if Z(q) has modular properties. FAIL if not. INFO if mock modular.
- **Who**: Analytic number theory (no agent yet)

### LT-6: Signal Processing (CC as DC residual)
- **Input**: Dirac eigenvalue spectrum, spectral action filter
- **Output**: s61_signal_psd.py/.npz
- **Gate**: PSD-DC-61. PASS if DC component determined by band structure. FAIL if not.
- **Who**: Acoustic physics / phononic crystal specialist (quantum-acoustics-theorist)

---

## Entry Format for Researcher Extraction

Each PENDING entry should be filled with:

```
### [RESEARCHER]-[#]: [Computation Title]
**Computation**: [What to compute — specific, actionable]
**Method**: [Algorithm, formula, approach]
**Input**: [Specific .npz files, constants, or data]
**Output**: [Script name, data file, plot]
**Gate**: [Gate ID]. PASS if [criterion]. FAIL if [criterion]. INFO if [criterion].
**Priority**: HIGH / MED / LOW
**Est. Cost**: [GPU time, complexity estimate]
**Paper Reference**: [Which research paper motivates this — equation number]
**Depends On**: [Other test cases that must complete first, or "none"]
```
