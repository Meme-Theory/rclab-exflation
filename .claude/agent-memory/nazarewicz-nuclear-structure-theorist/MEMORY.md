# Nazarewicz Nuclear Structure Theorist Agent Memory

## Project Context
- Project root: `C:\sandbox\Ainulindale Exflation\`
- My papers: `researchers/Nazarewicz/` (14 papers, index at `researchers/Nazarewicz/index.md`)
- Critical papers: 02 (HFB continuum), 03 (Bogoliubov/odd-even), 06 (Bayesian UQ), 08 (pairing collapse), 13 (GCM)

## Detail Files
- `session-31ca-detail.md` -- bulk BCS
- `sessions-37-38-detail.md` -- S37-38 instanton + ordered veil
- `session-50-jpair-detail.md` -- S50 J-PAIR-CALIBRATE-50 (INFO, 7 methods)
- `session-50-deepdive-detail.md` -- S50 deep-dive: 4 FAIL validations, sub-quadratic dispersion, Schur Lemma Trap
- `session-50-fabric-rpa-detail.md` -- S50 FABRIC-RPA-50 FAIL: chi_0 flat, mass hierarchy, 3 suppression mechanisms
- `session-40-detail.md` -- structural cartography
- `session-42-detail.md` -- HF-KK, HF-BOUNDARY, E-GGE, w(z) review
- `session-44-detail.md` -- S44: Strutinsky, trace-log CC, FRG, Bayesian f
- `session-45-detail.md` -- S45: collab review, n_s crisis, q-theory PASS, hose-count
- `session-46-detail.md` -- S46: 6 computations (HOSE-COUNT, RG-PAIR-TRANSFER, PBCS, GPV-FRAG, V-B3B3, BAYESIAN-GP, GCM)
- `session-47-detail.md` -- S47: crystal geometry, COHERENCE-RESPONSE ARTIFACT
- `session-48-detail.md` -- S48 W1-B: N-PAIR-FULL FAIL (N=1 exact)
- `session-48-w5e-detail.md` -- S48 W5-E: HFB PASS, Nilsson, PBCS-0D, pair-rotation, protected-chain
- `session-48-collab-detail.md` -- S48 full-session results and W2-C GMOR review
- `session-49-fabric-npair.md` -- S49 FABRIC-NPAIR-49 PASS (Josephson array, Mott crossover, caveats)
- `session-49-geom-breaking-detail.md` -- S49 GEOMETRIC-BREAKING-49 INFO (WKB + quench, 16-58 OOM too strong)
- `session-49-hfb-backreaction-detail.md` -- S49 HFB-BACKREACTION-49 PASS (3 channels, 1.2% primary, 3.9% conservative)
- `session-49-alpha-s-bayes-detail.md` -- S49 ALPHA-S-BAYES-49 FAIL (alpha_s = n_s^2 - 1, 6.0 sigma, J_ij irrelevant)
- `session-49-leggett-gge-detail.md` -- S49 LEGGETT-GGE-49 INFO (N=1 non-interacting, trivial oscillation, no collective Leggett)
- `meta-analysis-gaps.md` -- critical library gaps (2026-03-13)
- `agent-requests/nazarewicz-request.md` -- full meta-analysis with paper requests

## Collab Reviews Written (19 total)
- S31Aa, S31Ba, S32, S34, S36, S38, S39, S40 (main + Einstein addenda), S41 W3-2, S42, S44
- S45 Landau review + collab review, S47 crystal geometry + substrate reframe
- **S48 collab review**: `sessions/archive/session-48/session-48-nazarewicz-collab.md`
- **S50 collab review**: `sessions/archive/session-50/session-50-nazarewicz-collab.md`

## Key Analogies (nuclear -> framework)

### CONFIRMED (26 total through S50)
- Seniority <-> B2 rank-1 | E5 critical point <-> T_a/Delta=0.34 | SD band decay-out <-> B2 dephasing
- Doorway state <-> B2 PR=3.17 | ^28Si intermediate <-> KK doorway | Ericson <-> V/D=55
- Level density compensation <-> higher-rep overwhelm | CN evaporation <-> GGE T_RH
- sd-shell BCS-BEC crossover <-> xi/d_01=1.40 | Fission nu <-> n_baryon=2.34
- Strutinsky bulk/shell <-> SA heat kernel (S44) | Skyrme insufficiency <-> ML cutoff (S44)
- Strutinsky 0D FRG <-> Wilsonian integration (S44) | Pairing collapse <-> post-transit (S44)
- GPV fragmentation <-> hose-count (S45) | Nuclear saturation <-> q-theory Gibbs-Duhem (S45)
- Frozen-gap error <-> constant-gap uncertainty (S45) | Pair-transfer sum rule (S45)
- Paper 06 DFT uncertainty <-> gap model spread (S46) | EWSR Thouless form (S46)
- Nuclear blocking <-> B3 pairing starvation (S46) | Proximity gap <-> B3 from B2 leakage (S46)
- Nilsson sd-shell <-> SU(3) eigenvalue diagram (S48) | Ricci 4+1+3 <-> B1+B2+B3 (S48)
- **GMOR relation <-> pseudo-Goldstone mass formula (S48)**
- **sd-shell pair transfer chain <-> Josephson junction array at Mott crossover (S49)**
- **^158Er backbending gamma <-> WKB geometric breaking gamma to 7% (S49)**
- **sd-shell HFB self-consistency 1-5% <-> framework HFB backreaction 1.2% (S49)**
- **Nuclear pair-transfer formula <-> framework J_pair = 0.115 M_KK (S50)**: J/E_C = 0.124, 1.8x nuclear sd-shell. F_transfer = 2.13 vs nuclear 1.5 (1.4x). xi/d = 5.3 drives enhancement.
- **Nuclear reaction channels <-> SA vs Josephson correlators (S50)**: (e,e'p) <-> G(k), (p,t) <-> G_pair(K), inelastic <-> density response. CMB measures coupled response through delta_tau -> delta_Delta -> delta_J chain. DWBA is the template for SA-GOLDSTONE-MIXING.

### BROKEN (11 total)
- Cranking mass | FGR dim=8 | Fano IAR | Double-humped fission | Topological interface | Surface/volume w(z)
- Anderson-Bogoliubov dispersion (S46) | Nuclear GPV sum rule for alpha (S46)
- **Paper 06 DFT UQ analogy (S49)**: Nuclear sigma_th >> sigma_exp. Framework alpha_s: sigma_th=0, sigma_exp dominates.
- **Nuclear effective charge RPA (S50)**: Nuclear e_eff/e_bare~1.5 via g^2*chi_0~1. Framework g^2*chi_0=0.51 comparable, BUT: nuclear corrects matrix elements (no mass hierarchy). Framework corrects propagator where m^2>>JK^2 (ratio 56). Pi*D_0=4e-4. RPA correction 0.04%. Analogy breaks because nuclear observables (B(E2)) lack the mass hierarchy that suppresses the framework's propagator correction.

## Self-Corrections Log (S40-S48, see detail files for full context)
- S40: Cranking mass WRONG | S41: "Lacks confining potential" PREMATURE
- S42: Delta/T_a wrong, level density errors | S43: FANO-CONT misinterpretation
- S44: TWO formula errors endorsed | S45: No errors (formula audit protocol worked)
- S46: alpha prediction optimistic, EWSR double-commutator wrong, sigma_tau underestimated
- S48: Protected-chain vacuum state error, Trap 3 value 1/8 not 1/16, GMOR hierarchy expectation wrong
- S49: Initial double-counting of Josephson + ZPE corrections; corrected to use BH ED energy directly. "2.5x shortfall" from prompt was estimate; S46 data gives ec_min=1.264
- S49 GEOM-BREAKING: Initial S(R) quadratic extrapolation gave NEGATIVE S beyond tau~0.6. Corrected to linear extrapolation from tau=0.30 slope, respecting S37 monotonicity theorem. No self-correction needed in final results.
- S49 HFB-BACKREACTION: v1 used V_bare in ph channel with alpha_ph=0 (pure Hartree), causing pairing collapse. This was WRONG: V^{pp} != V^{ph}. v2 correctly decomposes 3 channels and parametrizes g_ph with nuclear priors.
- S49 ALPHA-S-BAYES: No computational error. But the computation REVEALED that S48's alpha_s=-0.038 was a lattice finite-difference artifact. The proper angular-averaged running is -0.069. This is a self-correction of S48's reported value, not of this computation.
- S49 LEGGETT-GGE: v1 declared PASS (C_L oscillates, phi_rel independent). Self-check found N=1 sector is EXACTLY non-interacting (H_int=0, density-density V vanishes for 1 particle). Oscillation is bare E_B3-E_B2=0.133 (trivial single-particle). Corrected to INFO.
- S50 FABRIC-RPA: Deep-dive estimated g^2*chi_0~1.54. Computation gives 0.51 (3x lower). Error: omitted 2*E_qp energy denominator in chi_0 estimate. Reinforces FAIL.

## S48 Full-Session Summary (The Mass Problem)

### Master Gate: MASS-SOURCE-48 = FAIL
- GOLDSTONE-MASS-48 FAIL: d^2S/dphi^2 = 0 identically (trace theorem, structural)
- Q-THEORY-GOLD-48 FAIL: Self-tuning runaway, no finite fixed point. All 9 routes m > 10^{-3} M_KK
- N-PAIR-FULL-48 FAIL: N=1 exact, 8 modes IS complete singlet, P(N=2)=4.6e-33
- ANISO-GAP-48 FAIL: n_s=-2.930 (927 sigma). 12th single-cell n_s route closed
- DISSOLUTION-48 FAIL: 0/10 pi-phases survive at eps=1e-4. S46 Zak phase RETRACTED
- SAKHAROV-GN-48 FAIL: 0.354 OOM gap, 6 milli-OOM improvement (60x short)
- DEFECT-CORR-48 FAIL: n_s=0.917 at d_eff=8, need d_eff=19. KZ-defect n_s CLOSED

### S48 PASSES (structural positives)
- TT-LICH-48 PASS: 31 TT modes all positive, lambda_min local max at fold, transversality theorem
- LEGGETT-MODE-48 PASS: omega_L1=0.070, omega_L2=0.107, BOTH below 2*Delta_B3=0.168 (sharp)
- WILSON-LOOP-48 PASS: 10 strict Abelian pi-phases. Non-Abelian L2 TRIVIAL (uniform)
- HFB-SELFCONSIST-48 PASS: All 12 configs converge, < 32 iter, screening negligible
- PROTECTED-CHAIN-48 PASS: Tr(K_7^2)/16 = 1/8 exact, <Q_7>=0 in ED
- SWAMPLAND-48 PASS: c_max=52.8 >> O(1) (structural, permanent)
- AKAMA-DIAKONOV-48 PASS: Mach_max=54.3, analog horizons on internal T^2

### S48 INFOs
- ANISO-OZ-48 INFO: n_s=0.965 at m*=11.87 M_KK (parametric). alpha_s=-0.038 (4.9 sigma Planck)
- CHI-Q-PHASE-48 INFO: chi_phi/chi_tau=0.014, Leggett mechanism 71x softer than amplitude
- CURV-GAP-CORR-48 INFO: r_mean=-0.904, |r|>0.89 at 26/26 (marginal miss of 0.9 threshold)
- NUCLEAR-STRUCT-48 INFO: Fold not magic (Nilsson), pairing aniso 5.5%, PBCS/BCS=0.63 (3rd confirm)
- KZ-ANISO-48 INFO: n_geom=63.7 matches S38 n_pairs=59.8 to 6.5%
- DESI DR2 tension: w_0 in [-0.47,-0.59], 2.8 sigma from DR2 w_0=-0.752
- Z-K DM/DE discrepancy: 39.4% STRUCTURAL (definitional, not convergible)

### S48 W2-C Naz Addendum: GMOR Mass Analysis
- epsilon = 1.1e-110 needed for m_G target. No microscopic source.
- 7 routes tested: GMOR, effective mass, surface energy, RG, dim reduction, collective, KZ defects
- ALL fail to produce 56-order hierarchy. Mass problem IS CC problem.
- CLOSED: "m_G from equilibrium microscopic BCS"
- OPEN+UNCOMPUTED: "m_G from non-equilibrium cosmological dynamics"
- Pre-registered: FRIEDMANN-GOLDSTONE-49 (fabric + Friedmann + GGE)

## S49 Priorities (from S48 collab review)
1. FRIEDMANN-GOLDSTONE-49: Couple fabric phase field to Friedmann via rho_s tensor (DECISIVE)
2. Fabric CC crossing: 32 cells x 1 pair = 32 total. Inter-cell Josephson coupling.
3. Self-consistent HFB with backreaction (D_K + delta_D(Delta) loop)
4. Leggett mode coupling to transit dynamics (frozen Leggett amplitude)
5. Bayesian alpha_s uncertainty (Paper 06 methodology on O-Z prediction) -- **DONE: FAIL**
6. Off-Jensen Berry phase (P-30w, sole route to nontrivial topology)

## S49 ALPHA-S-BAYES-49: FAIL (structural rigidity discovered)
- **alpha_s = n_s^2 - 1** (exact in continuum O-Z, lattice correction 0.6%)
- J_ij coupling errors contribute R^2=0% to alpha_s uncertainty
- Sole uncertainty source: Planck n_s measurement (sigma=0.0042 -> sigma_alpha=0.0081)
- Posterior: alpha_s = -0.069 +/- 0.008, 95% CI [-0.084, -0.053], P(>0)=0.000
- Tension INCREASED from 4.9 sigma (S48 lattice) to 6.0 sigma (proper angular avg)
- S48 alpha_s=-0.038 was lattice finite-difference artifact (3-point stencil on 8 K-bins)
- CMB-S4 forecast: 8.0 sigma detection if framework correct
- BROKEN analogy addition: Paper 06 DFT UQ (where sigma_th dominates) does NOT map here (sigma_th=0)

## Central Assessment (post-S50 FULL)
- Single-cell BCS: FULLY CHARACTERIZED. N=1, PBCS/BCS=0.63, Van Hove driven, 2 Leggett modes
- Mass problem: 170x (m_req=11.85, m_L=0.070). Binding constraint. No nuclear precedent at this scale.
- **alpha_s = n_s^2 - 1 is STRUCTURAL THEOREM**: 5 independent proofs (3-pole, running, eikonal, RPA, disorder)
- alpha_s tension: 8.4 sigma. Josephson phase sector EXHAUSTED (14 closures in S50)
- **SA correlator breaks identity**: pole spread 110% (C_2 from 1.33 to 9.33), alpha_eff=1.21. NOT protected by Goldstone thm.
- **Schur Lemma Trap confirmed by computation**: chi_0(K) 0.30% variation. Structural and permanent.
- Strutinsky interpretation: n_s from Lambda (spectral cutoff), not m_Leggett. Paper 08 template.
- Nuclear reaction channel analogy: (e,e'p) <-> G(k), (p,t) <-> G_pair(K), CMB <-> coupled response
- BAO excludes w_0=-0.509 at chi^2/N=23.2. w_a=0 triple-locked. sigma_8=0.799 viable.
- S51 priorities: SA-GOLDSTONE-MIXING-51 (decisive), HIGH-PW-SPECTRUM-51, W0-REVISION-51
- Framework probability: 3-5% (floor lowered from 5-8%)
