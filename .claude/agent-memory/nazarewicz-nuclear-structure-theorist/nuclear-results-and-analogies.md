---
name: Nuclear-Framework Results and Analogies (consolidated S31-S78)
description: All load-bearing nuclear-structure results, confirmed/broken analogies, key ED/HFB numbers, self-corrections
type: project
---

# Consolidated Nuclear-Framework Results

## Key HFB / ED Numbers (S52-S53, permanent)
- ED N=1: E_gs=1.440, n_B2=0.600, n_B1=0.388, n_B3=0.012, gap=0.258 M_KK
- ED N=2: E_gs=3.011, n_B2=1.444, n_B1=0.504, n_B3=0.052, gap=0.219 M_KK
- S_2(N=2)=-0.131 (pair-pair REPULSIVE; N=1 singlet is true ground state)
- B1(k=4) at N=2: |u^2-v^2|=0.0075, Z_k=0.250 (PHONONIC, max). B3: >0.95 (PARTICLE)
- Off-diagonal pairing: 52.5% (N=1), 48.5% (N=2)
- HFB self-consistency: 47 iter (N=1), 54 iter (N=2). dE/E=-0.94%, -1.81%
- PBCS vs ED: +0.97% (N=1), +0.27% (N=2). BCS overestimates (Paper 03)

## Mass Problem Status (S48 MASS-SOURCE = FAIL)
- d^2S/dphi^2=0 (trace theorem). q-theory runaway. N=1 exact
- 7 GMOR routes: epsilon=1.1e-110 needed
- CLOSED: equilibrium microscopic BCS source
- OPEN: non-equilibrium cosmological dynamics

## alpha_s Persistent Tension (S49+, S62, S63, S66, S67)
- alpha_s = n_s^2 - 1 (exact identity)
- -0.069 +/- 0.008. CMB-S4 forecast 8.0 sigma. Currently 4.9-5 sigma persistent
- BMA n_s = 0.969 +/- 0.022 (S67 BAYESIAN-FUNCTIONAL PASS)

## CC Status
- Non-equilibrium CC CLOSED (Zubarev). PW extension R_cancel=1 at L>=1 (UV catastrophe)
- q = N_pair (discrete, locked). q-theory = F-theory (project insight)
- BCS-SAKHAROV-LOOP PASS (S66): a_2/a_4 channel decoupling. FUNCTIONAL-INDEPENDENT

## N_pair Blocking (NON-MONOTONIC, contradicts S56 Poisson prediction)
- <r> = 0.442, 0.412, 0.419 (N=2,3,4). Plateau ~0.42 (KAM intermediate)
- N-PAIR-3-RG-64 PASS: <r>=0.478+/-0.021. RG super-integrable at 0.21. Non-separable V breaks integrability. Paper 15
- OES min at N=5 (62.5%, S60): {0.066..0.034..0.049}. DECOUPLES from microscopic Z_k/b(N)

# Confirmed Nuclear-Framework Analogies (38 total)

## Most Load-Bearing
- **Strutinsky-NCG bridge** (S44/S53/S55/S56): SA = smooth + shell. grad_ratio=0.71 (single-cell), 0.051 (fabric, 14x below). Three-functional hierarchy
- **Chebyshev theorem** (S66): monotone-decreasing f -> Q^eff >= Q^bare. PERMANENT. Stronger than Jensen
- **HFB channel decoupling <-> a_2/a_4 decoupling** (S66): FUNCTIONAL-INDEPENDENT. Paper 02/03
- **Nuclear pair-transfer <-> S_-(N)=S_+(N-1)** (S60): BDI reality. Bosonic <1%. Paper 18
- **SD band confinement <-> CG(24) Josephson confinement** (S63): gap/Delta=60.3, BCS 225x overestimate. Paper 17
- **Anderson criterion <-> B2[0] blocking** (S63): ratio=0.0088. Paper 17
- **Nuclear Gibbs-Duhem <-> Volovik CC relaxation** (S66): P=0 at saturation. Paper 25. 0.01 OOM
- **GPV collective vs non-collective <-> Leggett (DM) vs BA phonons** (S66): Omega_DM h^2=0.120 (0.6% Planck). Paper 18
- **sd-shell onset-of-chaos <-> non-separable V breaks RG** (S64): <r>=0.478. Paper 15

## Pairing & BCS (12 total)
- sd-shell BCS-BEC crossover <-> xi/d_01=1.40 (S40)
- sd-shell Fermi-surface coherence <-> B1 phononic mode (S53)
- Nuclear blocking <-> N_pair blocking non-monotonic (S56/S60)
- Doubly-magic rigidity <-> off-Jensen insensitivity (S58): E_gap/delta_eps~1800
- Nuclear pair-transfer formula <-> J_pair=0.115 M_KK (S50): F_transfer=2.13

## Collective Modes & Reactions (6)
- Seniority <-> B2 rank-1 (S40); E5 critical <-> T_a/Delta=0.34
- SD band decay-out <-> B2 dephasing; Doorway <-> B2 PR=3.17
- GPV fragmentation <-> hose-count (S45); EWSR Thouless (S46)
- Nuclear reaction channels <-> SA vs Josephson correlators (S50)

## Shell Structure & Strutinsky (7)
- Strutinsky bulk/shell <-> SA heat kernel (S44)
- Coulomb gradient swamping shell <-> Josephson swamping TB shell (S56): 32x
- Strutinsky gamma/d separation <-> SA cutoff vs shell (S62): 25x. CS=1.076
- Nilsson sd-shell <-> SU(3) eigenvalue diagram (S48); Ricci 4+1+3 <-> B1+B2+B3

## DFT, UQ & Self-Consistency (5)
- Paper 06 DFT UQ <-> spectral functional UQ (S66 RESTORED): sigma_th=0.16 >> sigma_exp
- Skyrme insufficiency <-> ML cutoff (S44)
- Nuclear correlation energy <-> one-loop quantum depletion (S62): |E_corr/E_HF|~30-40%
- Gilkey cross-terms <-> Skyrme t0-t3 (S62): 5R/12 correction
- HFB self-consistency 1-5% <-> framework HFB backreaction 1.2% (S49)

## Thermodynamics & CC (4)
- Level density compensation <-> higher-rep overwhelm (S40); CN evaporation <-> GGE T_RH
- Nuclear fission dissipation <-> transit qp excitation (S56/S57): P_exc=0.081

## Other (4)
- Fission nu <-> n_baryon=2.34 (S40); Pairing collapse <-> post-transit
- GMOR <-> pseudo-Goldstone mass formula (S48)
- 158Er backbending gamma <-> WKB geometric breaking gamma (S49): 7%
- Many-body Z vs IP Z <-> fabric Z vs single-cell Z (S55). Paper 17
- Fabric projected moments (S67): correction 1.34%, combined 12.9%

## BROKEN (15 total — provenance)
- Cranking mass | FGR dim=8 | Fano IAR | Double-humped fission | Topological interface | Surface/volume w(z)
- Anderson-Bogoliubov dispersion (S46) | Nuclear GPV sum rule for alpha (S46)
- Paper 06 DFT UQ for alpha_s (S49, partially RESTORED S66 for n_s only)
- Substrate compaction w_a sign (S66): +1.121 vs DESI -0.73
- Nuclear effective charge RPA (S50): mass hierarchy breaks analogy
- Doubly-magic shell on fabric (S56): Josephson swamps
- Nuclear SPE splittings for Yukawa (S62): rank-1 Yukawa theorem closes

# Self-Corrections (recurring lessons)

- **Never report fractional changes of collapsed BCS quantities** (S58)
- **Never conflate bulk thermodynamic (OES) and microscopic (Z_k, b(N)) signatures** (S60)
- **Never apply "particle in potential" thinking to substrate parameter tau** (S61). tau IS substrate, not dynamical variable
- **Formula audit protocol (S45+) prevents endorsing wrong equations** (S44 had TWO endorsed errors)
- **Bayesian UQ discipline (Paper 06 §III)**: scoring function fixed BEFORE evaluating posterior; retrofitting after seeing outcome inflates favored region (S79 P1-3 W1-B audit)

## Specific Errors Closed
- S40 cranking mass 50-170x WRONG (actual M_ATDHFB=1.695)
- S44 TWO formula errors endorsed (pre-audit)
- S48 Trap 3 = 1/8 not 1/16; protected-chain vacuum error; GMOR hierarchy
- S49 FABRIC-NPAIR (double-counting), GEOM-BREAKING (sign), HFB-BACKREACTION (V_bare in ph), ALPHA-S-BAYES (-0.038 was lattice artifact)
- S50 FABRIC-RPA: chi_0 g^2 ~1.54 -> actual 0.51 (omitted 2*E_qp denom)
- S52 N-PAIR-FULL: separable V N-linear artifact, corrected to INFO
- S58 OFF-JENSEN-BCS: 8.37% noise -> ED 0.057%
- S60 BLOCKING-N3: <r> tracks b(N), not OES

# Collab Reviews Written (24 total)
- Pre-S48: S31Aa, S31Ba, S32, S34, S36, S38, S39, S40 (+Einstein addenda), S41 W3-2, S42, S44, S45 (+Landau), S47
- S48+: S48, S50, S55, S56 (+final-synthesis), S59, S60, S61 (W8), S62, S66, S78
- Locations: `sessions/archive/session-NN/` (pre-S52) or `sessions/session-NN/` (S52+)

## S78 (2026-04-15) Headline Suggestions
- 2PI or constrained HFB for W1-C (cured linear-Hartree divergence is nuclear-HFB-standard Paper 02/03/05/20)
- BMA for chi_2(inf) with AIC-weights replacing median (Paper 06 §III)
- Reframe W1-E 32-OOM "FAIL" as BMA over (IC, scheme) cross-product with FIRAS first constraint
- Wynn-epsilon acceleration tightens W3-A from 0.017 to 0.005
- Verdict: Branch C under-uncertaintied by ~0.5 OOM; true A_s posterior band spans 3-4 OOM straddling Planck after nuclear-UQ quality treatment

# Session Headline Summary (S31-S67)

| S | Headline Result |
|:---|:---|
| S31Ca | Bulk BCS closure: ZERO enhancement, 7-10x below threshold. ALL bulk routes CLOSED |
| S37 | F5-ONELOOP FAIL (any S=Tr f(D^2) with f'>0 penalizes pairing); INST-MC PASS (dense gas) |
| S38 | Paradigm shift: instantons + ordered veil. CC-INST <Delta^2>/Delta_0^2 >= 0.831. P_exc=1.000 sudden quench |
| S39 | FRIED-39 FAIL (133,200x); GGE permanence retracted (Brody 0.633 weakly chaotic) |
| S40 | Structural cartography 11 gates: HESS 22/22 positive (compound nucleus); QRPA stable |
| S42 | E-GGE PASS T_RH=1.098, eta=3.44e-9; W-Z FAIL w_0=-1+O(10^{-29}) |
| S44 | STRUTINSKY-DIAG plateau 2.54 dec, BCS=10^{-4} of shell. TRACE-LOG-CC 5.11 orders reduction |
| S48 | Mass problem CLOSED equilibrium / OPEN cosmological. 7 PASSES W5-E |
| S49 | FABRIC-NPAIR PASS (Mott crossover); HFB-BACKREACTION 1.2%; ALPHA-S-BAYES -0.069 (6 sigma) |
| S50 | J-PAIR-CALIBRATE 0.115 M_KK; FABRIC-RPA FAIL (mass hierarchy 56) |
| S52 | HFB-FULL PASS (canonical ED N=1, N=2 numbers above) |
| S53 | HFB-SPECTRAL: B1 Z_k=0.250 phononic max, B3 >0.95 particle |
| S55 | STRUTINSKY-992 grad_ratio=0.71 (S53 1.30 INVALID) |
| S56 | STRUTINSKY-FABRIC R=0.051 (Josephson dominates); shell minimum CLOSED on fabric |
| S57 | FINITE-RATE-TRANSIT P_exc=0.081 (LZ overestimates 12x; Josephson protection) |
| S58 | OFF-JENSEN-BCS: ED gap 0.057% change at sigma=0.01 |
| S60 | PAIR-TRANSFER-N4 PASS S_+(1)=0.936 BDI; BAYESIAN-H0 FAIL (truncation 99.7%) |
| S61 | GPV-EWSR PASS (3.1e-14); HIGGS m_H=134.0 GeV; YUKAWA Jensen O(1) vs O(10^5) needed |
| S63 | RICHARDSON-GAUDIN: BCS 225x overestimate; BLOCKING-GGE 113x asymmetry |
| S64 | N-PAIR-3-RG PASS <r>=0.478 (Paper 15) |
| S66 | Scheme-dependence n_s SIGN REVERSAL; Leggett-only DM Omega_DM h^2=0.120; Chebyshev theorem PERMANENT |
| S67 | BAYESIAN-FUNCTIONAL PASS BMA n_s=0.969+/-0.022; FABRIC-PROJECTED-MOMENTS 12.9% combined |
