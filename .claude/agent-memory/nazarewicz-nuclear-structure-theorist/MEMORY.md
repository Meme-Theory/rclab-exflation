# Nazarewicz Nuclear Structure Theorist Agent Memory

## Project Context
- Project root: `C:\sandbox\Ainulindale Exflation\`
- My papers: `researchers/Nazarewicz/` (26 papers, index at `researchers/Nazarewicz/index.md`)
- Critical papers: 02 (HFB continuum), 03 (Bogoliubov/odd-even), 06 (Bayesian UQ), 15 (Richardson-Gaudin), 16 (ATDHFB), 17 (ultrasmall BCS), 18 (pair transfer)
- High papers: 01, 04, 07, 08, 12, 13, 19, 20, 22, 24

## Memory Files
- [nuclear-results-and-analogies.md](nuclear-results-and-analogies.md) -- consolidated S31-S78: all key HFB/ED numbers, 38 confirmed + 15 broken analogies, recurring self-corrections, 24 collab reviews, session headline summary

## Headline State (post-S67/S78)
- **CC redirected to q-theory**. Non-equilibrium CC CLOSED (Zubarev). q=N_pair discrete
- **BCS sector fully characterized**. ED N=1: E_gs=1.440, gap=0.258 M_KK. ED N=2: E_gs=3.011, gap=0.219, S_2=-0.131 (repulsive)
- **Mass problem**: equilibrium microscopic CLOSED; non-equilibrium cosmological OPEN
- **alpha_s = n_s^2-1 (exact)**: -0.069+/-0.008. 4.9-5 sigma persistent. CMB-S4 forecast 8 sigma
- **N_pair blocking NON-MONOTONIC**: <r>={0.442, 0.412, 0.419} (KAM intermediate plateau ~0.42)
- **B1 PHONONIC** (Z_k=0.250 max), **B3 PARTICLE** (>0.95). Off-diagonal pairing ~50%

## M_KK BCS dimensional-transmutation (S110 CV2A / S111 W2-1)
- CV2A (S110): R = exp(-1/(lambda_eff*N0)) at tau_fold. lambda_eff=0.038935 (Kosmann V-matrix per coset = ||K_a||^2_C2/13.782), N0=14.0233 (rho_B2_per_mode, FINITE-enhanced fold DOS), g=0.5459, R=0.16017. M_KK=R*M_Pl_reduced=3.900e17 (OOM 0.72 from CONST-FREEZE-42)
- **S111-CF-MKK-RG-INVARIANCE: FAIL (BARE-IMPORT)**. tau-scan of R(tau): Delta_rel=8.19 >> 5e-2. R is tau-FLOWING, NOT a Lambda_QCD-style fixed-point. M_KK is fold-PINNED (tau_fold=0.190), not flow-invariant
- WHY: van Hove DOS pile-up N0(tau) is FOLD-LOCALIZED (exists only where B2-band v=dE_B2/dtau=0); off-fold N0 collapses 14->0.67, g collapses, R->0. No beta-function compensation (unlike QCD). lambda_eff(tau) from Kosmann norm grows mildly; N0(tau) dominates
- TAU-DERIVABLE MACHINERY (reusable): D_K(tau) via dirac_spectrum.extract_singlet_eigensystem (s=tau, Jensen param). B2 band = 4-fold fold band of 8 lowest positive (0,0)-singlet modes (B1x1+B2x4+B3x3 under U(2)). Kosmann K_a(tau) via s23a_kosmann_singlet (Baptista Paper17 eq4.1, deterministic fn of Gamma(tau)). N0(tau)=windowed van-Hove DOS (s35a construction, v=dE_B2/dtau)
- Both legs FAIL: leg-1 (Delta_rel) AND leg-2 (Lambda_cutoff=M_Pl_reduced via a2/EH IS the CODATA cutoff). Confirms constructive-O3; sec-6.3 a(t)/Friedmann M_KK-magnitude leg stays external pin

## Most Load-Bearing Analogies (full list in detail file)
- Strutinsky-NCG bridge (S44/S55/S56): SA = smooth + shell. grad_ratio=0.71 single-cell, 0.051 fabric
- Chebyshev theorem (S66): monotone-decreasing f -> Q^eff >= Q^bare. PERMANENT
- HFB channel decoupling <-> a_2/a_4 decoupling (S66): FUNCTIONAL-INDEPENDENT
- SD band confinement <-> CG(24) Josephson confinement (S63): BCS 225x overestimate
- GPV collective vs non-collective <-> Leggett (DM) vs BA phonons (S66): Omega_DM h^2=0.120
- Nuclear Gibbs-Duhem <-> Volovik CC relaxation (S66): P=0 at saturation. 0.01 OOM

## Recurring Self-Correction Lessons
- Never report fractional changes of collapsed BCS quantities
- Never conflate bulk thermodynamic (OES) and microscopic (Z_k, b(N)) signatures
- tau IS substrate, not dynamical variable -- never apply "particle in potential" thinking
- Formula audit protocol (S45+) before endorsing equations
- Bayesian UQ discipline (Paper 06 §III): scoring function fixed BEFORE evaluating posterior
