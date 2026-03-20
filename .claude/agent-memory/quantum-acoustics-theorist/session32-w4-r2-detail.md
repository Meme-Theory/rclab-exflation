# Session 32 W4-R2: QA x Landau Workshop Detail

## Workshop Context
- Date: 2026-03-06
- Team: qa (quantum-acoustics), landau (condensed matter), coordinator
- Mission: Build on R1 (Feynman x Nazarewicz) findings, stress-test W-32b margin, resolve Turing/wall BCS

## R1 Key Inputs (must engage with)
- 100-500x trapping margin RETRACTED -> actual ~1x (M_max = 0.92-2.20 at wall)
- Delta is SLAVED — no independent dynamics. Turing killed.
- Shell-crossing pairing (B1-B2) is physical channel, not intra-B2. V = 0.0799-0.311.
- Swallowtail vertex (eta = 0.04592) essential — trapping unconditional there
- LANDAU-SECTOR test elevated to highest priority

## QA's Six Novel Results

### 1. Z_wall = 1/pi Universality
- At 1D van Hove: Z = rho*v = [1/(pi*v)]*v = 1/pi (FINITE, universal)
- Impedance mismatch Z_wall/Z_bulk ~ 4, reflection R ~ 0.36
- PARTIAL reflection — good for BCS coherence across wall
- Status: ENDORSED by Landau (no contest)

### 2. Superfluid Weight Saturation (Peotta-Torma)
- D_s = D_s^{conv} + D_s^{geom}. For flat B2: D_s^{conv} -> 0.
- D_s^{geom} = 2*g_B2 = 8.48 at flat-band center, INDEPENDENT OF DELTA
- Wall enhanced: D_s^{wall} ~ 2*g_B2*(rho_wall/rho_bulk) ~ 21
- Condensate stiffness from quantum metric, not gap magnitude
- Status: ENDORSED

### 3. Clean-Limit Hierarchy
- xi_BCS = v_eff/(pi*Delta) = 0.026/(pi*0.015) = 0.55 M_KK^{-1}
- w_wall = 1.3-2.7 M_KK^{-1}
- l_imp = w_wall/(-ln(1-R)) = 2.0/0.45 = 4.4 M_KK^{-1}
- Hierarchy: xi_BCS (0.55) < w_wall (2.0) < l_imp (4.4)
- BCS in CLEAN LIMIT. Mean-field reliable. Consistent with Gi ~ 0.005 (Landau).
- Status: CONVERGENT

### 4. Slaved Gap = Local Resonance (Metamaterial)
- Delta(x) is local resonance whose frequency is set by tau(x)
- Mass-in-mass system analog (Liu et al. 2000)
- DISPLACIVE limit, not order-disorder
- Pattern formation by first-order nucleation at band-edge-enhanced phase boundary
- Status: CONVERGENT with Landau's LK equation

### 5. v_eff = Shell Gap Coincidence
- v_eff = sqrt(v_B1*v_B2) = sqrt(0.055*0.012) = 0.026
- Shell gap = lambda_B2 - lambda_B1 = 0.026
- Same algebraic origin: B1-B2 eigenvalue separation
- Status: Not contested

### 6. Impedance Correction to M_max
- Multiple reflections enhance effective DOS by 1/(1-R) = 1.56
- M_max lower bound: 0.92 * 1.56 = 1.44 (now PASSES)
- Caveat: sharp-wall assumption; WKB good for B2 wavelengths
- Status: Superseded by Landau's more comprehensive stress test (self-consistency 2-3x)

## Landau's Key Results (QA-endorsed)

### LK Relaxation with Reverse Critical Slowing
- tau_LK -> 0 at dump point (system ACCELERATES into BCS minimum)
- Domain size L_domain ~ 0.35 << w_wall (sharp phase boundaries)
- QA: B3 modes provide dissipation (99.6% RPA weight), Gamma_tau smooth

### NUC-1: Nucleation -> Spinodal at Swallowtail
- B_3D = 0 at swallowtail (barrier-free = spinodal decomposition)
- NUC-1 PASSES TRIVIALLY at swallowtail
- QA: spinodal wavelength lambda_s ~ 11 M_KK^{-1} (initial domain size)
- Generic eta: marginal (B_3D ~ O(10-50) in weak coupling)

### GL Coefficients Revised
- L/E_kin = 1.2 (weak coupling V=0.08) to 2.5 (BEC V=0.31)
- Delta_jump ~ 0.11-0.24 (14-29% of lambda_min)
- Transition weakly first-order: c^2/(4b) ~ 5e-4

### M_max Stress Tests
- Van Hove SURVIVES BCS self-consistency (coherence peak reinforces)
- Gi ~ 0.005 (mean-field reliable, comparable to MgB2)
- Flat-band comparison: SU(3) B2 in same M_max range as MATBG, Kagome

## Novel Cross-Talk Results (emerged from interaction)

### CROSS-1: B2 = Symmetry-Protected BIC
- B2 energy WITHIN B3 continuum, ZERO coupling (Trap 4, Schur)
- Infinite Q-factor, Schur-protected
- BCS condensation of BIC = "BIC lasing" concept
- Would become Fano resonance under phi (inner fluctuation)

### CROSS-2: Reverse Critical Slowing + Acoustic Absorber
- Landau: LK relaxation accelerates toward dump
- QA: dump is acoustic absorber, not reflector
- B3 provides dissipation (smooth), singularity from V_eff^{sc}

### CROSS-3: Andreev Mirror Self-Confinement
- BCS gap creates R_BCS = tanh^2(Delta*w/(2*v_B2)) ~ 1.0 (perfect mirror)
- Positive feedback: BCS -> gap -> Andreev mirror -> more trapping -> stronger BCS
- Condensate is SELF-CONFINING once formed

### CROSS-4: Type I/II Classification (kappa = 3.6)
- kappa_wall = L_wall/xi_BCS = 2.0/0.55 = 3.6 >> 1/sqrt(2)
- DEEPLY TYPE II: negative surface energy, wall proliferation
- Z_3 + Abrikosov optimization = honeycomb wall network (graphene topology)
- QA confirmed: Z_wall/Z_bulk ~ 4 ~ kappa ~ 3.6 (structural connection)

### Landau Refinements (from endorsement review)
- v_eff = shell gap is ALGEBRAIC IDENTITY (trace identity for 2x2 near fold)
- D_s saturation + swallowtail trapping share COMMON ROOT in g_B2
- Clean-limit matches drip-line halo nuclei (11Li: surface-localized pairing)
- Impedance correction valid for band-edge modes (k->0, exp(-2kw)->1)

## Constraint Map Entries
- W4-R2-A: Z_wall = 1/pi (structural, universal)
- W4-R2-B: D_s = 2*g_B2 = 8.48 (Peotta-Torma, Delta-independent)
- W4-R2-C: Clean-limit hierarchy (convergent QA+Landau)
- W4-R2-D: NUC-1 trivial PASS at swallowtail (spinodal)
- W4-R2-E: L/E_kin = 1.2-2.5 (quantitative)
- W4-R2-F: B2 = symmetry-protected BIC (new cross-talk)
- W4-R2-G: Andreev mirror self-confinement (new cross-talk)
- W4-R2-H: kappa = 3.6, deeply Type II (new cross-talk)

## Dictionary Updates (7 new/refined)
- B2 at dump = symmetry-protected BIC in B3 continuum (NEW, Parallel B)
- BCS gap at wall = Andreev mirror / acoustic band gap (NEW, Parallel B)
- LK relaxation at dump = acoustic absorber (NEW, Parallel B)
- Swallowtail vertex = spinodal decomposition point (NEW, Parallel B)
- Delta(x) slaved = local resonance in metamaterial (REFINED from Turing, Parallel B)
- kappa_wall = Type II GL parameter (NEW, Parallel B)
- Z/Z_bulk ~ kappa = acoustic-GL self-consistency (NEW, Parallel B)

## Final: 14 results (6 QA + 4 Landau + 4 cross-talk), 0 divergences
## Open: V_pair normalization (TRAP-1), spinodal coarsening, BIC->Fano under phi
