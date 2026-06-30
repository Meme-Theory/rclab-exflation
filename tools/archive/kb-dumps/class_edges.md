# class_edges (104 entries)

| type | srcType | src | tgtType | tgt | role | comment |
|---|---|---|---|---|---|---|
| contains | classes | CC | constants | CC_ratio | PRIMARY | Headline ratio rho_Lambda_spectral / rho_Lambda_obs (~10^120) |
| contains | classes | CC | constants | rho_Lambda_obs | PRIMARY | Observed CC density (Planck 2018, GeV^4) |
| contains | classes | CC | constants | R_protected_fold | PRIMARY | L_max-invariant ratio a_0*a_4/a_2^2; SOLE Chamseddine-Connes observable tying CC (a_0) to GR (a_2) and YM (a_4); Vol(SU(3)) cancels (Baptista B2). S73B/S74. |
| contains | classes | CC | constants | Lambda_obs_MP4 | DERIVED | Dimensionless Lambda/M_Pl^4 form (= rho_Lambda_obs scaled) |
| contains | classes | CC | constants | Omega_Lambda | RELATED | Dark-energy density parameter (Planck 2018) |
| contains | classes | CC | constants | Omega_DE_obs | RELATED | Planck 2020 DR2 update of Omega_Lambda |
| contains | classes | CC | constants | Gamma_effacement | RELATED | Acoustic-white-hole impedance; (1-Gamma) = effacement residual |
| contains | classes | KK | constants | M_KK | PRIMARY | Canonical alias = M_KK_gravity (conservative route) |
| contains | classes | KK | constants | M_KK_gravity | PRIMARY | Gravity route: spectral zeta / Newton's constant (S42) |
| contains | classes | KK | constants | M_KK_kerner | PRIMARY | Kerner route: gauge-metric extraction (S42) |
| contains | classes | KK | constants | OOM_diff_MKK | DERIVED | log10(M_KK_kerner / M_KK_gravity) = 0.83 decades |
| parent_of | classes | alpha_s | classes | alpha_s_QCD |  | QCD strong coupling subtree |
| parent_of | classes | alpha_s | classes | alpha_s_inflation |  | Inflationary spectral-index running subtree |
| contains | classes | alpha_s_QCD | constants | alpha_s_MZ_obs | PRIMARY | PDG 2024 anchor: alpha_s(M_Z) = 0.1180 |
| contains | classes | alpha_s_inflation | constants | planck_alpha_s | PRIMARY | Planck 2018 central value (legacy, superseded by alpha_s_canon_2020) |
| contains | classes | alpha_s_inflation | constants | planck_alpha_s_err | DERIVED | Planck 2018 1-sigma on alpha_s |
| contains | classes | alpha_s_inflation | constants | alpha_s_canon_2020 | PRIMARY | ACT DR4 + Planck combined (Aiola+ 2020); post-2018 canonical pin |
| contains | classes | alpha_s_inflation | constants | alpha_s_canon_2020_err | DERIVED | Aiola+ 2020 1-sigma on alpha_s |
| contains | classes | alpha_s_inflation | constants | alpha_s_inflation_framework | PRIMARY | Framework prediction: n_s^2 - 1 (S50 identity) |
| contains | classes | alpha_s_inflation | constants | alpha_s_framework_central | DERIVED | Canonical handle alias for alpha_s_inflation_framework (S85 W1c-1) |
| contains | classes | alpha_s_inflation | constants | alpha_s_cmb_central | RELATED | CMB-pivot identity using planck_ns=0.9649 (S50/S85 W13-2) |
| contains | classes | alpha_s_inflation | constants | planck_ns | RELATED | n_s anchor that the framework's alpha_s prediction depends on |
| contains | classes | fold | constants | tau_fold | PRIMARY | Jensen deformation parameter at the fold (= 0.19) |
| contains | classes | fold | constants | S_fold | PRIMARY | Spectral action at the fold (S42) |
| contains | classes | fold | constants | dS_fold | PRIMARY | dS/dtau at the fold = +58,672 (drives transit) |
| contains | classes | fold | constants | d2S_fold | PRIMARY | d^2 S/dtau^2 at the fold (curvature of action) |
| contains | classes | fold | constants | Z_fold | DERIVED | Gradient stiffness at fold (= G_DeWitt-weighted) |
| contains | classes | fold | constants | H_fold | DERIVED | Hubble parameter at fold (M_KK units) |
| contains | classes | fold | constants | v_terminal | DERIVED | Terminal velocity of modulus during transit |
| contains | classes | fold | constants | dt_transit | DERIVED | Transit duration (M_KK^-1 units) |
| contains | classes | fold | constants | P_exc_kz | DERIVED | Kibble-Zurek excitation probability (= 1 exactly) |
| contains | classes | fold | constants | n_Bog | DERIVED | Bogoliubov fraction per mode |
| contains | classes | fold | constants | n_pairs | DERIVED | Bogoliubov quasiparticle pairs from transit (= 59.8) |
| contains | classes | fold | constants | c_fabric | RELATED | Substrate sound speed (sets Mach number for transit) |
| contains | classes | fold | constants | phi_paasch | RELATED | Paasch spectral ratio at s=0.15 (PROVEN, related to fold geometry) |
| contains | classes | fold | constants | m_tau | RELATED | Modulus mass at the fold (M_KK units) |
| contains | classes | fold | constants | omega_tau | RELATED | Transit frequency d(tau)/dt |
| contains | classes | Higgs | constants | m_H_obs | PRIMARY | Observed Higgs mass (PDG 2024, 125.1 GeV) |
| contains | classes | Higgs | constants | v_ew | PRIMARY | Electroweak VEV (= 246 GeV) |
| contains | classes | Higgs | constants | m_t_pole | RELATED | Top pole mass (PDG 2024); dominates Higgs-sector running |
| contains | classes | Higgs | constants | m_b_pole | RELATED | Bottom pole mass (PDG 2024); secondary Yukawa contributor |
| contains | classes | GR | constants | a2_fold | PRIMARY | Second Seeley-DeWitt coefficient at fold; sole source of EH action 1/(16 pi G_N) = f_2 a_2 M_KK^2 (S44 SAKHAROV-GN-44) |
| contains | classes | GR | constants | M_KK | PRIMARY | KK scale fixes dimensional anchor of a_2 channel; KK class owns extraction, GR uses as input |
| contains | classes | GR | constants | f_2_default | PRIMARY | f_2 spectral cutoff moment (S62 W1 Gaussian-cutoff = 2.34); regulator-pinned prefactor in EH dictionary |
| contains | classes | GR | constants | c_S_canon | PRIMARY | Canonical spectral-action scale normalization (Chamseddine-Connes 1997) |
| contains | classes | GR | constants | Lambda_Planck | PRIMARY | Planck-scale regulator in M_KK units (= 1.0 default, S85 W6-3) |
| contains | classes | GR | constants | d_spec | PRIMARY | Classical spectral dimension of D_K = 3 (Connes-Moscovici); gates which SDW term carries EH content |
| contains | classes | GR | constants | R_protected_fold | PRIMARY | L_max-invariant ratio a_0*a_4/a_2^2; ties GR (a_2) to CC (a_0) and YM (a_4) channels |
| contains | classes | GR | constants | G_N | EMERGENT_FROM | Newton's constant from 1/(16 pi G_N) = f_2 a_2 M_KK^2; substrate-level emergence (S44 SAKHAROV-GN-44 PASS, 3-route check) |
| contains | classes | GR | constants | M_Pl_reduced | EMERGENT_FROM | Reduced Planck mass = 1/sqrt(8 pi G_N); inherits substrate-emergence from G_N |
| contains | classes | GR | constants | M_Pl_unreduced | EMERGENT_FROM | Unreduced Planck mass = sqrt(hbar c / G_N); inherits substrate-emergence |
| contains | classes | GR | constants | l_Planck | EMERGENT_FROM | Planck length sqrt(hbar G_N / c^3); inherits substrate-emergence |
| contains | classes | GR | constants | t_Planck | EMERGENT_FROM | Planck time sqrt(hbar G_N / c^5); inherits substrate-emergence |
| contains | classes | GR | constants | rho_crit_GeV4 | EMERGENT_FROM | Critical density 3 H_0^2 / (8 pi G); equation-of-motion of emergent EH action |
| contains | classes | GR | constants | G_N_cgs | DERIVED | G_N in CGS units (= G_N * 1000); pure unit conversion |
| contains | classes | GR | constants | l_Planck_cm | DERIVED | Planck length in cm (= l_Planck * 100); pure unit conversion |
| contains | classes | GR | constants | rho_crit_cgs | DERIVED | Critical density in CGS (= rho_crit_GeV4 in g/cm^3); pure unit conversion |
| contains | classes | GR | constants | eps_baseline | DERIVED | Substrate slow-roll-equivalent = (1 - planck_ns)/2; algebraic from Planck n_s |
| contains | classes | GR | constants | tau_fold | RELATED | Jensen evaluation point of a_2; PRIMARY in fold class, RELATED here (per user-confirmed taxonomy) |
| contains | classes | GR | constants | H_0_km_s_Mpc | RELATED | Hubble constant 67.4 km/s/Mpc (Planck 2018); Friedmann observational anchor |
| contains | classes | GR | constants | H_0_GeV | RELATED | H_0 in GeV; unit conversion of H_0_km_s_Mpc |
| contains | classes | GR | constants | H_0_inv_s | RELATED | H_0 in s^-1; unit conversion |
| contains | classes | GR | constants | Omega_m | RELATED | Matter density 0.315 (Planck 2018); Friedmann boundary condition |
| contains | classes | GR | constants | Omega_b | RELATED | Baryon density 0.0493 (Planck 2018); matter-sector BC |
| contains | classes | GR | constants | Omega_DM | RELATED | Dark matter density 0.266; BC (S44 CDM-CONSTRUCT-44 gives DM by construction) |
| contains | classes | GR | constants | Omega_Lambda | RELATED | Dark-energy density 0.685; value lives in CC class (a_0), Friedmann observable here |
| contains | classes | GR | constants | Omega_r | RELATED | Radiation density 9.15e-5; cosmological boundary condition |
| contains | classes | GR | constants | T_CMB | RELATED | CMB temperature 2.7255 K (COBE/FIRAS); BC for Friedmann-radiation era |
| contains | classes | GR | constants | t_universe_s | RELATED | Age of universe 4.35e17 s (Planck 2018); Friedmann observable |
| contains | classes | GR | constants | clock_coeff | RELATED | Atomic-clock variation coefficient -3.08 (S22d); tests emergent equivalence-principle behavior |
| contains | classes | Exflation | constants | dS_fold | PRIMARY | Spectral action gradient at fold = +58,672; substrate-driver of cascade (the 'inflaton field' in container language) |
| contains | classes | Exflation | constants | S_fold | PRIMARY | Spectral action at fold = 250,360.7; absolute energy scale of cascade event |
| contains | classes | Exflation | constants | Mach_max_framework | PRIMARY | Mach number at fold = 13.75; defining property — supersonic transit IS the acoustic white hole |
| contains | classes | Exflation | constants | v_terminal | PRIMARY | Terminal velocity of modulus = 26.545 (M_KK units); kinematic state at fold |
| contains | classes | Exflation | constants | dt_transit | PRIMARY | Transit duration = 1.13e-3 M_KK^-1; impulsiveness defines KZ freezing window |
| contains | classes | Exflation | constants | H_fold | PRIMARY | Hubble parameter at fold = 586.5 (M_KK units); expansion rate during transit |
| contains | classes | Exflation | constants | P_exc_kz | PRIMARY | Kibble-Zurek excitation probability = 1.0 exactly; saturation (no Landau-Zener adiabaticity) |
| contains | classes | Exflation | constants | n_Bog | PRIMARY | Bogoliubov fraction per mode = 0.9986; pins per-mode GGE distribution shape |
| contains | classes | Exflation | constants | T_acoustic | PRIMARY | GGE acoustic temperature = 0.112 M_KK; relic's effective acoustic temperature on substrate (algebraic GGE permanence) |
| contains | classes | Exflation | constants | Gamma_effacement | PRIMARY | Acoustic-white-hole impedance = 0.99970; (1-Gamma)=3e-4 = effacement residual |
| contains | classes | Exflation | constants | c_fabric | PRIMARY | Substrate sound speed = 209.97; Mach denominator (Mach=v_terminal/c_fabric) |
| contains | classes | Exflation | constants | c_BLV | PRIMARY | BLV post-fold scalar sound speed = 0.485 (S64); GGE-relic phonon sector |
| contains | classes | Exflation | constants | d2S_fold | DERIVED | Curvature of spectral action at fold; characterizes width of fold transit |
| contains | classes | Exflation | constants | Z_fold | DERIVED | Gradient stiffness at fold; G_DeWitt-weighted moduli-space stiffness |
| contains | classes | Exflation | constants | omega_tau | DERIVED | Transit frequency d(tau)/dt; algebraic from v_terminal + modulus mass |
| contains | classes | Exflation | constants | omega_att | DERIVED | Post-fold attractor frequency = 1.430; geometric from spectral action curvature at attractor |
| contains | classes | Exflation | constants | E_exc_ratio | DERIVED | Excitation/condensation ratio = 443.0; Schwinger-instanton-duality measure |
| contains | classes | Exflation | constants | E_exc | DERIVED | Total excitation energy from BCS transit quench (= E_exc_ratio * \|E_cond\|) |
| contains | classes | Exflation | constants | T_compound | DERIVED | Microcanonical post-fold compound temperature (= E_exc / 8 across BCS Fock modes) |
| contains | classes | Exflation | constants | N_pivot | DERIVED | CMB pivot e-fold count = 64.08 = 55 + ln(c/c_s); substrate-c_s correction to LCDM |
| contains | classes | Exflation | constants | n_pairs | CONSEQUENCE | Bogoliubov pairs from transit = 59.8; produced BY cascade, becomes PRIMARY in any future GGE-relic class |
| contains | classes | Exflation | constants | w0_FW | OBSERVABLE_OUTPUT | Framework dark-energy EOS w_0 = -0.918 (Volovik vacuum + effacement); DESI/Euclid testable |
| contains | classes | Exflation | constants | n_s_framework | OBSERVABLE_OUTPUT | Framework scalar spectral index at CMB pivot = 0.9561 (S84 T6); Planck/CMB-S4 testable |
| contains | classes | Exflation | constants | tau_fold | RELATED | Cascade transits THROUGH this tau locus; PRIMARY in fold, RELATED here (per user-confirmed taxonomy) |
| contains | classes | Exflation | constants | phi_paasch | RELATED | Paasch spectral ratio (PROVEN, S12); substrate-static identity pre-dating cascade |
| contains | classes | Exflation | constants | m_tau | RELATED | Modulus mass at fold = 2.062; inertial response to dS_fold gradient |
| contains | classes | Exflation | constants | Q_Leggett | RELATED | Leggett mode quality factor 6.7e5 (S50); cascade-survivor DM candidate |
| contains | classes | Exflation | constants | T_BCS | RELATED | BCS canonical temperature 0.640; substrate-pairing scale partially surviving transit |
| contains | classes | Exflation | constants | T_c_BCS | RELATED | BCS critical temperature 0.083; post-fold residual-pairing scale |
| contains | classes | Exflation | constants | kappa_BCS | RELATED | BCS surface-gravity analog 4.019 (S69); white-hole side characterization |
| contains | classes | Exflation | constants | tau_phase_trans | RELATED | C^2 sectional K=0 phase transition (S48); second tau-landmark beyond tau_fold |
| contains | classes | Exflation | constants | tau_overshoot | RELATED | Overshoot turnaround at K=53.35 (S77); post-fold modulus dynamics first turnaround |
| contains | classes | Exflation | constants | v_crit | RELATED | Censorship critical velocity = 219.3; transit just barely satisfies v_terminal < v_crit |
| contains | classes | Exflation | constants | eps_H_W6 | RELATED | Slow-roll bound from S80 dS/dtau at fold; interface between substrate and slow-roll-equivalent observables |
