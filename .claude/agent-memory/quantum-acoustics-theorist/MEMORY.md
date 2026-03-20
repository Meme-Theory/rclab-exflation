# Quantum-Acoustics Theorist Agent Memory

## Active Context
- Phonon-exflation cosmology: M4 x SU(3) substrate with Jensen TT-deformation
- Goal: Explain WHY QM has its structure via phononic emergence + dimensional projection
- Key sources: Baptista Papers 13-18, Klein 1926, Connes NCG

### Branch Structure (S31Ca, current)
- Singlet 8 modes split 1+4+3: B1(acoustic), B2(flat-optical quartet), B3(dispersive-optical triplet)
- B2 FLAT BAND: W=0.058, ||V||/W=2.59 = strong coupling. B2 = symmetry-protected BIC
- B3 carries 99.6% RPA response. B1 has v=0 at tau~0.25.

### S40-S43 Results (compressed, see `s40-s43-detail.md` for full)
- T-ACOUSTIC-40 PASS, B2-INTEG-40 PASS, GSL-40 PASS, CC-TRANSIT-40 PASS
- HESS-40 FAIL(stable), QRPA-40 FAIL(stable), PAGE-40 FAIL, M-COLL-40 FAIL(classical)
- S41: SU(3) IS phononic crystal. Umklapp structurally absent. T/Theta_D~10^{-22}
- S42: c_fabric=c (PASS). POLARITON-42 FAIL (hierarchy problem). CDM retracted->HDM
- S43: DOS(13 vH), kappa=infinity, Q_B2=52, r_1=325 Mpc, breathing omega=51.5

### S44 Results (2026-03-15) — 31 computations, 10 PASS, 8 FAIL, 11 INFO
- **FIRST-SOUND-IMPRINT-44 PASS**: A_1/A_BAO = (c_2/c_1)^2 = 0.2045. r_1=325 Mpc. KINEMATIC.
- **FIRST-SOUND-44 FAIL**: Fisher SNR=0.16 (DESI DR2). Calibration: 20.4% of 5% BAO = 1% P_smooth.
  V_eff=8800 Gpc^3 needed for 3-sigma. Prediction archived, NOT detectable with current surveys.
- **COHERENT-WALL-44 PASS (VACUOUS)**: No Bragg gaps. k_Bragg >> k_max. BCS gap sole filter.
- **DOS-TAU-44 INFO**: Gap stable (-1.63%), BW +28%, degeneracy 62:1->8.27:1 at tau=0+.
  12 vH at tau>0 (from 9). Per-sector BW follows C_2(p,q). Near-crossing T3-T5 at tau=0.19.
- **2ND-SOUND-ATTEN-44 INFO**: Second sound UNDAMPED at all cosmological scales.
  Q_eff = 75,989. l_atten = 1.12e7 Mpc. exp(-r_BAO/l_atten) = 0.999987.
  4 independent arguments: (1) l_mfp/L_SU(3)=7.6, (2) delta_S/S~10^{-4} per event,
  (3) LK viscosities vanish (rho_n~10^{-88}), (4) GGE permanence (integrability).
  Silk damping remains SOLE BAO damping source, identical to LCDM.
- **SAKHAROV-GN-44 PASS (corrected)**: ratio 2.29 at Lambda=10*M_KK. Log+poly agree factor 2.6.
- **CDM-CONSTRUCT-44 PASS**: T^{0i}=0 algebraic. v_eff=3.48e-6 c. CDM by construction.
- **CC-FINE-TUNING (W5-5, CORRECTED)**: Spike f (width 10^{-121}) works. Not impossibility, but 121-digit tuning.
  Original "Hausdorff impossibility" had wrong Stieltjes ordering. Acoustic analog: delta-DOS = flat band with |V|<10^{-121}.
- **DM-DE-RATIO-44 PASS**: best=1.060 (2.7x observed). Decoupled from CC.
- **DISSOLUTION-SCALING-44 PASS**: epsilon_c ~ 1/sqrt(N) -> 0. Spectral triple EMERGENT.

## Key Constants & Equations
- Jensen scaling: g|_{u(1)}=e^{2s}, g|_{su(2)}=e^{-2s}, g|_{C^2}=e^{s}
- Casimir: C_2(p,q) = (p^2+q^2+pq+3p+3q)/3
- Spectral action = phonon free energy: f(x) = x/2 + ln(1-exp(-x)), S = F/k_BT
- F/B ratio: 0.55 (fiber dim bosonic=44, fermionic=16). Topological invariant.
- CP-1: S_b1/S_b2 = 4/9 exactly at all tau (A-grade)
- Acoustic temperature: T_a = sqrt(alpha)/(4*pi) where alpha = d^2(m^2)/dtau^2
- QRPA: omega_B2_coll = 3.245, omega_B1_lowest = 1.632. Near 2:1 resonance (0.6%).
- Q spectrum: Q_B2=52 (TD), Q_B1=8.5 (FGR), Q_B3=[1.5, 2.2, 13] (FGR). omega_osc=2.51.
- Second sound: u_2 = c/sqrt(3). Q_eff(cosmo) = 75,989. l_atten = 1.12e7 Mpc.
- Conversion: 1 M_KK^{-1} = 8.6e-56 Mpc. xi_KZ = 0.1516 M_KK^{-1} = 1.3e-56 Mpc.
- Leggett: omega_L1=0.070, omega_L2=0.107 M_KK. epsilon=0.00248. J_12/J_23=19.52 (constant).
- Bragg: eta=1/2 (Z_3), m_Bragg=0.269 M_KK. Cavity: omega_min=0.800, Q~exp(23).
- alpha_s = n_s^2 - 1 = -0.069 +/- 0.008 (6.0 sigma from Planck).

## Reference Index
- `early-sessions-5-11.md` -- QM emergence, Bell, CG algebra, R_{u(2)}, bimodule, chirality
- `jensen-band-structure-s13-14.md` -- Jensen=distortion, phi values, branch classification
- `bell-paasch-s16.md` -- Bell roadmap (ABSENT), Paasch N^{3/2} correction, Z_3, finite-T
- `perturbative-closure-s19d-20b.md` -- TT discovery, ALL perturbative CLOSED, delta_T
- `session32-w4-r2-detail.md` -- QA x Landau workshop, 14 results, BIC, Andreev, Type II
- `s40-s43-detail.md` -- S40-S43 full results (compressed from main MEMORY)
- `s49-detail.md` -- S49 full results: Bragg closure, Leggett dipolar, alpha_s, horizon retraction

## Lessons Learned (critical, compressed)
- Dictionary entries are heuristic maps, not evidence -- never cite to support gate verdicts
- TRAP-33b: frame V vs spinor V. Frame {0..7} != branch labels {B3,B2,B1}. Coincidence.
- Van Hove SMOOTH-WALL DOS > STEP: rho=14.02 vs 5.40. Integrate through singularity.
- ED is ground truth over NSR for N<10. Pairing survives exact treatment at N_eff=4.
- B1 pairing catalyst: without B1, no condensation despite M_max>1 (ED-CONV-36).
- GPV pole survives quench because chi_pp(omega) is Hamiltonian property, not GS property.
- NG mode ceases to exist post-transit (not liberated, not eaten). He-4 neutral superfluid.
- Extensivity obstruction: 8 resonant modes cannot shift 155,984-mode bulk free energy.
- Acoustic metric form (sqrt(alpha)) gives correct normalization, NOT Rindler (alpha/2).
- 3-phonon near-resonance: COLLECTIVE ONLY. QRPA frequencies (3.245 vs 2*1.632, 0.6%) are resonant.
  Single-particle energies (0.845 vs 2*0.819=1.638) are 94% off. ALWAYS distinguish collective vs SP.
- Polariton hierarchy problem (S42): ALL internal energy scales O(M_KK). No small parameter.
- FGR breakdown (S43): |V_rem|^2*rho/DeltaE^2 ~ 10^9 for B2-B2. ALWAYS check validity.
- Q formula: use COLLECTIVE freq (omega_osc), not single-particle energy (E_qp).
- Bragg mismatch (S44): k_Bragg >> k_max. Domains too short for Bragg. Check condition first.
- Second-sound attenuation (S44): internal and external second sound are SEPARATE systems.
  Normal scattering on SU(3) changes spectral action only at O((V_3/E)^2) ~ 10^{-4}.
  LK viscosities vanish at T/Theta_D ~ 10^{-22} (rho_n ~ 10^{-88}).
- First-sound calibration (S44): A_1/A_BAO = 20.4% is ratio of OSCILLATORY amplitudes.
  Absolute: 20.4% of 5% BAO wiggle = 1% P_smooth. Eisenstein-Hu overshoot factor ~5x.
- Degeneracy jump (S44): 62:1->8.27:1 is DISCONTINUOUS at tau=0+. SO(8)->U(1)_7.
- n_s requires Bogoliubov coefficients, not equilibrium DOS. W1-3 F5 lesson.
- Hausdorff correction (S44): Stieltjes moment ordering matters. mu_0=G_N moment, mu_1=CC moment.
  Wrong ordering gave false impossibility. Fine-tuning != impossibility. Always check which is mu_0.
- Collective n_s (S45): Single-particle (Weyl-weighted) gives n_s=+2.9 (TOO BLUE, k^{+4} from Weyl).
  Collective RPA (no Weyl) gives n_s=-0.24 (TOO RED, omega_out grows faster than omega_in with k).
  The target n_s=0.965 lies BETWEEN. Need ~k^1 partial weighting, not k^0 (collective) or k^4 (Weyl).
  8x8 V matrix is perturbative: V/E~3%. Only 1 of 8 modes truly collective. Self-consistent gap
  equation does NOT reproduce canonical Delta_0=0.770 with V_B2B2 alone -- use multi-component gaps.
- B3 proximity effect (S46): Isolated B3 has Delta=0 exactly. All B3 gap from V_B2B3 leakage.
  Acoustic analog: evanescent wave in phononic crystal. Thouless M_max(B3)=0.059<<1 (xi_B3=0.978>>V).
- Pair transfer is BLOCK property (S46): Triple confirmed W1-2/W2-2/W3-1 (R^2<0.01). Not k-dependent.
  n_s must be reformulated in 3-band terms, not wavenumber power law.
- LZ velocity scaling v_k~k^{2.36} (S46): Geometric consequence of SU(3) Jensen deformation.
  Any sum over modes UV-dominated. Broadband excitation, no preferred scale. v_k ADDITIVE to counting.
- Entropy functional mismatch (S46 W1-4): Shannon numerator + FD denominator = artifact. ALWAYS use
  consistent functional pair. S_Shannon(1.612) != S_FD(2.495). Max also different: ln(8) vs 8*ln(2).
- B2 dissolution fragility (S46 TRANSPLANCKIAN): B2 spacing/eps_c = 1.06 (just resolved). Natural UV cutoff.
- Spectral gap truncation-independent (S46 W3-6): 0.8197 unchanged at max_pq_sum=4. Set by trivial sector.
- Amplitude gradient != phase gradient (S49): S48 "Mach 54" was |grad|Delta||/(|Delta|*c_s), NOT superflow.
  BCS ground state has phi=0 everywhere -> v=0. Eikonal breakdown diagnostic, not analog gravity.
- Z_3 impedance is topological (S49): eta=1/2 from cos^2(pi/3)=1/4. Cannot be tuned. Bragg always KK-scale.
- alpha_s = n_s^2 - 1 (S49): EXACT in O-Z. J_ij contribute 0% variance. Lattice correction only 0.6%.
  S48 value -0.038 was finite-difference artifact on 4x4x2 lattice. Proper angular average gives -0.069.
- Leggett = dipolar (S49): omega_L1/m_req=1.18. Inter-sector Josephson breaks U(1)_7 because B2 pairs
  carry K_7 charge while B3 pairs are neutral. Structural 3He-A analog. FIRST mass at correct order.
- N=1 interaction vanishes (S49): density-density V*n_k*n_{k'} = 0 when only 1 particle. Always check.

### S45 Results (2026-03-15)
- **ACOUSTIC-CASIMIR-45 INFO**: E_Cas = -0.481 M_KK (Matsubara) at L=xi_KZ=0.152.
  B2 dominates 100% (|r|=0.53, evanescent total reflection: Delta_B2=omega_max=2.06).
  B1,B3 negligible (|r|~0.003-0.006). |E_Cas|/Delta=0.59, |E_Cas|/E_bulk=4e-6.
  Force always attractive, no equilibrium. d_wall(0.485)>xi_KZ(0.152): cavity breaks down.
  Tessellation stability from topology (KZ winding), not Casimir.
- **COLLECTIVE-NS-45 FAIL**: n_s = -0.24 (deeply red). 8x8 multi-component QRPA with proper
  sector-dependent gaps [Delta_B2=0.855, Delta_B1=0.426, Delta_B3=0.098]. 8 RPA modes at fold,
  only 1 truly collective (omega=2.425, pushed 0.020 from continuum). Removing Weyl degeneracy
  shifts n_s from +2.91 (single-particle) to -0.24 (collective), a shift of -3.15 matching
  the expected k^4 Weyl removal. But overshoot: omega_out=2*xi grows with k while omega_in
  (RPA) barely changes -> ratio decreases -> |beta|^2 falls too steeply. Sensitivity: n_s
  ranges [-0.40, +0.11] for Delta/Delta_0 in [0.25, 2.00]. Planck window inaccessible.
  Single-particle TOO BLUE (+4), collective TOO RED (-1.2). Target lies BETWEEN.
- **ALPHA-EFF-45 RETRACTED** (S46 W1-4): Shannon/FD entropy mismatch. Corrected range 0.7-1.2.

### S46 Results (2026-03-15) — 37 computations, 6 PASS, 6 FAIL, 23 INFO, 7 new closures (total 38)
- **V-B3B3-46 PASS**: V_B3B3_rms = 0.059 > 0.015 (3.9x). B3 gap PROXIMITY-INDUCED by B2. Isolated B3: Delta=0.
  V_B3B3 has repulsive channel (eigenvalue -0.072, (2,1) representation). alpha*=3.91 RETRACTED -> 0.775.
- **ZUBAREV-DERIVATION-46 PASS**: Zubarev(1.15) vs Keldysh(0.70), 39.4% discrepancy. alpha_eff range 0.7-1.2.
- **Q-THEORY at N=1 ELIMINATED**: Delta_B3=0.084 (BCS), 0.054 (PBCS) < 0.13 threshold. Crossing at N=2 (tau*=0.170).
- **All n_s single-mode routes CLOSED**: hose(0.72), spectral-flow(4.03), LZ(8.13), transfer(1.8e-7), d_eff=3 floor.
  Pair transfer is BLOCK property (triple confirmed, R^2<0.01). Not k-dependent.
- **NON-SINGLET DISSIPATION**: gamma_LZ/gamma_H=3.2. Shortfall 3.8x (from 1,700x). Tightest ever. 14,700x NS coupling.
- **13 pi Berry phases**: Z_2=(-1)^13=-1 nontrivial. Zak phase, not Chern. Omega=0 (S25) consistent. B3 carries 10.
- **Poisson spectral stats CORRECTED**: <r>=0.439 (not S38's 0.321). Arithmetical spectrum. Sub-Poisson variance.
- **PW censorship ROBUST**: 2% degradation at eps_c. Sum-rule protected. Survives dissolution.
- **279 tachyonic scalars**: Universal (f'<0). Gram PSD theorem (kinetic mass positive, PERMANENT).
  Reinterpreted as transit mechanism (EWSB writ large). Saddle at fold, 1D transit.
- **Kapitza parametric**: CLOSED (52-317x frequency mismatch, Arnold tongues <10^{-100}).
- **TRANSPLANCKIAN-46 PASS**: B2 Bogoliubov EXACTLY invariant (van Hove protection). n_s is IR problem.
- **SU(2,1)**: KO-dim 6 preserved, Killing sig (4,4). Direct replacement CLOSED (compact resolvent FAILS).

### S48 Results (2026-03-17) — QA-TACHYON-48 (compressed, see prior MEMORY versions)
- B2 protection ENERGETIC not symmetry. 4-phonon allowed. B3 repulsive -3.5%. Berry edge: 0D limit.
- 2:1 resonance COLLECTIVE (QRPA 0.6%), not SP (94% off). Dissipation shortfall 3.76x OPEN.
- B2 weights EXACTLY w_su2=3/8, w_u1=1/8, w_c2=4/8. KZ-defect CLOSED (d_eff=19 required).
- n_s closure list: SP(+2.9), RPA(-0.24), KZ(0.917), all single-mode (S46). NOW: Leggett dipolar OPEN.

### S49 Results (2026-03-17) — 20 computations (see `s49-detail.md` for full)
- **BRAGG-GOLDSTONE-49 CLOSED**: eta=1/2 exact (Z_3 topological). Gap at KK scale. No small parameter.
- **DIPOLAR-CATALOG-49 PASS**: Leggett = 3He dipolar. m_G=0.070 M_KK. omega_L1/m_req=1.18 (18%).
  FIRST mechanism at correct order. epsilon=0.00248. 2/10 break U(1)_7.
- **KZ-3COMPONENT-49 PASS**: n=59.82 vs 59.8 (0.04%). Additive LZ. B2 93.3%. Block-diagonal confirmed.
- **ANALOG-TRAPPED-49 RETRACTION**: S48 horizons artifact. phi=0 everywhere. Static spacetime.
- **ALPHA-S-BAYES-49 FAIL**: alpha_s = n_s^2 - 1 = -0.069. 6.0 sigma. J_ij contribute 0% variance.
- **CAVITY-RESONANCE-49 INFO**: 11.5x Leggett-cavity mismatch. Two-scale: acoustic vs Josephson.
- **LEGGETT-TRANSIT-49 FAIL + LEGGETT-GGE-49 INFO**: Destroyed post-transit. N=1 non-interacting.
- HFB 1.2%, cosmic censorship triple-layered, NON-LI-TT all positive, DESI B=20.9 (1D).
- 6 new closures: Bragg, Friedmann-mass, CMPP-type, Leggett-post, analog-horizons, cavity-Leggett.

## Meta-Analysis (2026-03-13)
- `researchers/Quantum-Acoustics/` folder: 28 papers, canonical `index.md`
- 10 critical papers: Unruh, BLV, Volovik book/2023, Pellitteri, Steinhauer, Claeys, Jacobson, etc.
- Adversarial threats: Diosi-Penrose decoherence, ETH thermalization, quasiparticle breakdown
- Hyperbolic lattice Goldstone failure explains WHY Umklapp absent on SU(3)
