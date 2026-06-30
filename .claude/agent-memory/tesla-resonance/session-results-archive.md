---
name: Session Results Archive (S27-S75)
description: Compressed archive of Tesla-Resonance session results from S27 through S75. Permanent walls/theorems live in permanent-resonance-results.md; this is reference-only context.
type: project
---

# Session Results Archive (S27-S75)

## Early Sessions (S27-S47)

### S27-S30: Foundations
- T-1 PASS (S27): K=-Gamma_LC. mu=0 excludes BCS in ALL 9 sectors. V_nm diagonal=0 universal.
- S28 fusion (8 cross-synthesis): Pomeranchuk-van Hove inevitability, Q resolution (Q~100 -> Q_eff~1), bootstrap circularity dissolved. Closures: periodic orbits 10^{-39}, Axiom 5 fails, cubic -> first-order BCS.
- KC-3 RESOLVED (S29): n_gap=37.3. Chain complete 5/5. t_BCS=0.16/M_KK. 3-sector F_BCS=-17.22.
- S30: Static resonance CANNOT create minimum. Parker=friction. Acoustic mirror 8000x too weak. Kapitza paradigm shift: static closures irrelevant to time-averaged potentials. Instanton = nonlinear phonon (KK reduction theorem).

### S31-S32: Adversarial closures + Decisive gates
- d_s=8 GENERIC. Lambda_SA/M_KK = 10^6 at tau=0.21 (W6 wall).
- chi_full=20.43 >> chi_sep=0.728 (28x). B2 curvature dominates at dump point.
- Trap 5: J maps pos to neg eigenvalues. Real reps -> Kramers -> ME=0.
- B2 flatness: ENABLES wall trapping, DISABLES parametric amplification.
- S32 Meta-Workshop (7 findings): Quantum metric = decoupled band protection; dump point = Volovik QCP; Chladni map = conformal diagram; Bragg = rep-theory permanence (Schur); speed bump = phase boundary not potential well; violation 4.000 = magic angle mismatch.

### Key file paths (archive)
- computations/s31a_kapitza_gate, s31a_instanton_kapitza
- computations/s30b_grid_bcs.npz, s30a_df_construction.npz, s30a_dtotal_pfaffian.npz
- computations/s19a_sweep_data.npz, s23a_*.npz
- computations/r20a_*.npz (Riemann)

## S48-S52: Wall expansion + Leggett identifications

### S48 (10 closures, 4 PASSes)
Closures: Goldstone mass from SA (trace theorem), Singlet CC crossing N>=2, k-dependent gap n_s=-2.930, q-theory equilibrium runaway, Zak phase artifact, Sakharov G_N (60x short), KZ defect n_s=0.917, golden ratio in (2,2)/(0,0) 3.8% from phi, GGE Euler relation negative P, fN centroid 3.4%.
PASSes: WILSON-LOOP (10 strict Abelian pi); TT-LICH (31 modes positive); LEGGETT-MODE (omega_L1=0.0696, omega_L2=0.1074); SWAMPLAND (c=52.8 >> O(1)).

### S49 Permanent results (load-bearing)
- **Leggett = dipolar**: J_23 breaks U(1)_7 (B2 K_7-charged, B3 neutral). epsilon=0.00248.
- **m_G = omega_L1 = 0.070 M_KK**: 18% from m_req=0.059 for n_s.
- **alpha_s = n_s^2 - 1 = -0.069** (exact O-Z identity). 6.0sigma from Planck. CMB-S4 at 8sigma.
- CMPP type II locked. Penrose 4 zones. HFB backreaction 1.2%. KZ 3-component = S38 identity (0.04%).
- w_0 corrected: Zubarev -0.430. Multi-T shifts 25% toward DESI.

### S49 Cavity (INFO) + Leggett-Phi
- 111 subsonic cavities on T^2. omega_cav_min=0.800 M_KK (11.5x omega_L1). Two-scale: Hard ~0.8 vs Soft ~0.07.
- R(tau)=omega_L2/omega_L1 crosses phi_paasch=1.5316 at tau=0.2117. J_12/J_23=19.52 CONSTANT.

## S53-S58: Tight-binding + speed hierarchy

### S53 Paradigm
- N_pair = 1 EXACTLY. GL INVALID (Mott side). Single Cooper pair on 32-site lattice.
- Gamma/omega = 0 EXACTLY for all 6 bands. S52 "anti-crossings" = EXACT CROSSINGS.
- BLV: a_acoustic = a_geom * sqrt(rho/c_s). 229x hierarchy. 8D BLV formula OPEN.
- Speed bump LOCAL MAXIMUM at tau=0.2015 (PERMANENT).
- 7 closures: naive KZ blue, foam CC, topological baryogenesis, lattice Casimir, BdG det, static stabilization, BDI c_Gold.

### S54
- LATTICE-SPECTRAL-TRIPLE-54 PASS 2/3: SA-LATT-OCC min tau=0.194, 5.35% barrier; CONNES-LATT a(fold)=2.117; ED-SWEEP FAIL.
- Berry-Tabor INTEGRABLE (BT ratio 1.266). C^2 selection rule: dm^2_B2/dtau=0 exactly. 1378 avoided crossings ALL diabatic.
- P_vac = 1 - E_GGE (Euler tautology). Threshold corrections CLOSED (4 OOM mismatch).

### S56-S58 Resonance results
- omega_J=0.715 sub-gap, Mattis-Bardeen protected.
- Two-speed: c_BA=0.399, c_L=0.019-0.032 (12-21x ratio).
- Impedance Gamma=0.85 BA-Leggett. Adiabatic gap hierarchy: Delta_BCS < omega_J < Josephson_bonding.
- BKT: T_GH/T_BKT < 0.17 everywhere. Fabric ordered.
- Strutinsky gradient DECREASED 14x on fabric. Josephson swamps shell.
- **omega_J = omega_att = 1.429 M_KK (S57)**: Attractor IS plasma mode. STRUCTURAL.
- DM bracket [0.017, 0.188]. CC sign PASS (Lambda_eff=+1.709, w=-0.408). 114 OOM gap.
- Gap scaling Delta_N ~ N^{-1.84}. Desert Mach 2700. Percolation tau=0.105.
- GGE universality (theorem): all cells identical post-quench. E_DW=0 exact.
- IMPEDANCE-BOUNDARY (S58): TRANSPARENT. <T_local>=0.969. TAU-INDEPENDENT.

## S60-S65: Heat kernel, sound speed, BCS protection

### S60 (H_0 retracted)
- **H_0 = 68.8 RETRACTED**: Tr(|D_K|) diverges as L^{6.2}. S44 (1,2) irrep bug. Heat kernel a_2 = THE path. UNCOMPUTED.
- HESSIAN-3D-60: Fold = SA maximum in 3D.
- Rough Thouless: t_Th/t_transit ~ 14,000.

### S61 (J-dynamic + SFF)
- **J-DYNAMIC-61 FAIL CLOSED**: [J, H(tau)] = 0 for all tau. No CP from transit. Berry phase impossible.
- **JOSEPHSON-INTEG-61**: Mode-diagonal on CG(24). Eigenvalues {+6,+2,0,-2,-6}.
- **SFF FACTORIZATION (PERMANENT)**: K(t) = K_BCS(t) * K_CG24(t) EXACT (1.5e-15). No ramp.

### S62 Hessian + cavity + crystal
- HESSIAN-ONELOOP: ALL 36 eigenvalues positive at 1-loop. Q_eff~1.9.
- KZ-NS-62 PASS conditional: n_s=0.9567 via Hubble SA. eps_H=0.0216.
- MEISSNER-GGE-62: D_s(GGE) = 98.85% of fold. Type-I. Permanent gauge mass.
- 45-mode 3-sector phononic crystal. 16 hybridization gaps. Max delta 0.248 M_KK.
- **CAUCHY-SCHWARZ-62 PERMANENT**: F_0*F_2 >= F_1^2 for any spectral triple.

### S63-S65
- SOUND-SPEED-63: c_s=0.4849, v/c_s=13.75 SUPERSONIC. Acoustic horizon EXISTS. r=0.168 ABOVE BICEP/Keck (S64 W3-A Bogoliubov r=0.033 PASSES).
- PHONON-DOS-63: 202 VHS, 0 true band gaps, 104 pseudo-gaps. d_eff=4.94.
- **S64 Three-speed**: c_mod=1.0 > c_BLV=0.485 > c_BA=0.399 > c_L=0.019-0.032. He-3B four-sound exact match.
- IMPEDANCE-65: BLV-BA WEAK (R=0.94%). BA|L STRONG (R=77.4%). A_s modulation ~2.5%.
- LEGGETT-RPA-65: Q_L1=28.2, Q_L2=10.2. Underdamped. Mattis-Bardeen ESSENTIAL. AB Goldstone Q->inf.

## S66-S75: Spectral functional, BCS protection, A_s closure

### S66 (spectral functional = physical DOF)
- eps_H SIGN REVERSAL: sqrt(x) red tilt (+0.022), exp/zeta blue (-0.013 to -0.045). n_s spread 0.164.
- **DILUTION-CC-66 PASS (0.01 OOM)**: Volovik q-theory rho_vac ~ H(t)^2 closes 114 OOM. Volovik seesaw 0.45x rho_obs.
- rho_geom/rho_GGE = 106.2 at fold. CC entirely in geometric sector.
- **Leggett-only DM (3 confirmations)**: Omega_DM h^2 = 0.120 (0.6%); Q=18.6 Lorentzian; z_eq=3425 (0.88 sigma).
- Integrability closure: ALL levels tested (single-particle, many-body N=1-4, classical 36D). ALL integrable. Bertini-Essler vs ADH: t_therm ~ 10^580 t_universe.
- alpha_s tension confirmed intrinsic (Richardson L->inf alpha_s=-0.0372, 4.9 sigma).
- m_H Aitken: 190 -> 162.6 -> 146.8 -> 136.1 -> 131.8 -> 127.5. Zero parameters. 1.9% from observed 125.1.
- Tensor tilt LOCALIZED: Blue n_T=+0.468 at k~10^52 Mpc^-1 (54 decades above CMB). CMB n_T=-0.003. r=0.024.
- Higgs Yukawa: U(2)-invariant Y=lambda*I (Schur). Hierarchy 21.5 from breaking. Spectral dim D_s(SU(3)) ~ 6.

### S67 (joint falsification)
- 1/5 spectral functionals survive all 4 constraints. **CC cutoff f(x) = sqrt(x) sole survivor**.
- Discriminant: SIGN of dS_f/dtau at fold. Increasing f -> red tilt; decreasing -> blue.
- Constraints (ii)-(iv) all FUNCTIONAL-INDEPENDENT.

### S69 (BCS protection)
- A_s gap budget: 0.485 OOM remaining (BCS dressing +0.046, non-BD squeeze +0.226, phi_eff +0.043).
- 7 BCS protection theorems all PASS: eps_H cancellation 10^4x margin; conformal anomaly 8e6x; spectral dim 0.094%; Hessian 36 pos; off-Jensen Schur theorem (PERMANENT); f_NL 0.0018<0.013; Petrov D/G preserved.
- Off-Jensen gradient (PERMANENT): dS/d(eps_perp) = 0 by Schur. Numerical max 7.96e-15.
- Four-speed hierarchy IDENTICAL to 3He-B. cosine similarity 0.996. 3He-B: c_1=183 m/s, v_F=59.0, c_BA=34.1, c_L=0.053.
- 7 observables -> 5 independent predictions. CR-1: alpha_s=0 (Bogoliubov saturation, 60-decade hierarchy).
- LISA RETRACTED: f_peak~10^12 Hz, Omega(LISA)=8.3e-58. Transit GW CLOSED for all detectors.
- FW PREFERRED: f*sigma_8 (chi^2 0.761 vs 0.893), Pantheon+ (1.025 vs 1.149).

### S70 (PERMANENT structural constraints)
- **CHIRP-PENUMBRA-70 (PERMANENT)**: WKB inapplicable to van Hove transit. Mach=54.73, gamma>1 for 93.4% modes. Zero turning points. Sudden approx required. k_tach(fold)=1974.5; k(gamma=1)=33,150.
- **CAVITY-BCS-HORIZON-70**: Compound barrier z''/z + Delta^2*a^2 monotonic. No Fabry-Perot. BCS/geo ratio 5.9e-08. dk/k(BCS)=1.3e-07 negligible.

### S71 (chirp universality + SU(1,1))
- **Chirp universality (PERMANENT)**: k_chirp = v^2*kappa_n frame-independent to 8.1e-10. Van Hove kills connection terms. All 8 modes stationary.
- SU(1,1) compound squeeze: S_eff = S_spatial * S_Leggett * S_BCS exact BCH. r_eff weighted = 2.247. delta_OOM = 2.074 RAW (overcorrects 8x). Decoherence IS regulator.
- BCS dominates 89%. Leggett 7%. spatial 4%.
- BCS a_4 protection: delta(a_4)/a_4 = 2.02e-8 (6 OOM below threshold). 8/156,000 modes.
- BEC analog: ^39K Feshbach quench, T_eff=7.7uK, Mach_BEC=5.73. Currently accessible.
- Weyl two-loop: delta_2=1.003e-3 marginal FAIL. Three-loop 3.70e-9. All-orders <1.16e-3.

### S72 (laminar flow workshop, BCS = universal ancestor)
- SPECTRAL-FUNCTIONAL-FIT: f*(x) = 0.912*sqrt(x) + 0.088*exp(-x). NON-PERTURBATIVE (SDW diverges for sqrt). t*=0.0883, kappa=2.37e-8.
- DUAL-DECOHERENCE: delta_OOM=1.692 at t_dec/t_transit=6.73. BCS channel 99.8%.
- W1-A gap monotonicity: dDelta/dtau=-0.245 M_KK. Gap amplitude channel DEAD (t_dec/t_transit=5.5e9). Decoherence MUST be PHASE dynamics.
- **Laminar flow**: Ma_L=331. Re_GGE=0 EXACT. l_mfp=infinity from R-G integrability.
- **Five-layer protection**: R-G integrability (algebraic), BDI Z_2 gap (topological), CG(24)+S_4 (kinematic 1%), 0D cell geometry (t_J/t_transit=949), 16 hybridization gaps. Combined Gamma_eff ~ 10^{-72} M_KK.
- **Two-fluid mapping RETRACTED**: Volovik partition != Landau two-fluid. Correct: BCS spectral function A(k,omega).
- **BCS = universal ancestor**: 6 predictions (Ordered Veil, CC dilution, C_V ratio, pair creation, DM stability, laminar protection) from single algebraic structure.
- C_V ratio = 2.20 non-universal (specific to van Hove quench).
- BISPECTRUM: f_NL = -0.313, 80x below Planck. Intrinsically Gaussian (1/sqrt(N) CLT).
- Acoustic cavity Q ~ 85 (T_k ~ 0.012 at exit horizon). Phase spread ~1080 rad after 85 bounces.

### S75 (refinement)
- A_s f_conv DERIVED (PASS): f_conv = (M_KK/M_Pl)^4 * (a_2/a_0)^2 = 2.547e-10. Closes 9.47 -> 0.12 OOM. A_s=1.58e-9 (75% Planck). Caveat: M_Pl(physical), not (spectral).
- Z_2 selection rule: n_Z2/n_total = 0 exactly. DM REQUIRES Z_2-breaking (multi-cell).
- DM f_CPT = 0.610 (was 0.082). 19/28 pair types inter-band.
- Moduli ALL closed: multi-instanton 50th, cross-moment monotonic, m_eff^2/H^2=3.80e-4.
- Structural floor 82.4% (169 entries). Atlas 48 ROBUST + 15 QUASI + 7 FRAGILE.
- chi_2 sole CC route: rho = 0.337 rho_obs. a_0-scheme DEMOTED (L_max-divergent).
- Parker-Hawking exact in de Sitter (ratio 1.0000000000). 2.58 OOM in transit = Bogoliubov F=380.9.
- POMERAN-N-SCAN FAIL: no instability at any N {4,8,12}. Pomeranchuk theorem RECLASSIFIED -> "Spectral-flow f(0,0)<-3" (math identity, not physical instability).

## Collab files index
- S62: sessions/archive/session-62/session-62-tesla-collab.md (+ VdD-Tesla workshop)
- S60, S57, S56, S54, S53, S52: sessions/session-NN/session-NN-tesla-collab.md
- S49, S48: sessions/archive/session-NN/session-NN-tesla-collab.md
- S33 workshops: sessions/archive/session-33/session-33-w1-*.md
- S32 collab: sessions/archive/session-32/session-32-tesla-collab.md
- Framework: sessions/framework/framework-mechanism-discussion-tesla-collab.md
- Primer: sessions/framework/Collabs/Primer-tesla-framework-hypothesis.md (post-S53, 12 sections, P-1..P-10)

## Key load-bearing lessons
- Route A CLOSED (c_net=+0.444, S25). Route B only survivor.
- Always COMPUTE before predicting (torsion S26, cranking mass S40). f-dependence = Debye cutoff. Emergent theories cannot predict modulus from low-energy (S23c).
- SA BLIND to U(1)_7 phase (trace theorem, S48). Mass from non-SA physics.
- 2-band Leggett 4.3x wrong; use 3-band generalized eigenvalue.
- Two-functional architecture: SA (geometry, trace-blind) vs Josephson (mass, U(1)_7-breaking).
- Amplitude gradient != phase gradient. Always check phi before claiming analog horizons.
- Van Hove > CdGM: continuous enhancement > isolated peaks for BCS.
- Two-fluid mapping RETRACTED (S72). Correct: BCS spectral function A(k,omega).
- Flat bands SQUEEZE LESS (S64+S74 fallacy correction): B1 acoustic dominates Parker squeezing factor 37 over B2 flat.
