# S80 W0-9 CLASSIFICATION — RATIOS vs ABSOLUTES vs MIXED

**Gate**: `S80-CANONICAL-CONSTANTS-RATIOS-VS-ABSOLUTES-CLASSIFICATION`
**Status**: PASS
**Coverage**: 184/184 module constants classified (0 missing, 0 extra).
**Source**: `computations/_shared/canonical_constants.py` (all numeric globals).
**Script**: `computations/session-80/s80_w09_canonical_classification.py`
**References**: P4-D (session-79 workshops/p4-d-ratios-vs-absolutes-meta.md); CC96 §2-4; CCM 2007 §1.17-1.20.

## Classification scheme

- **RATIO**: M_KK-independent (dimensionless framework observable or pure math). Dim=0 by construction.
- **ABSOLUTE**: M_KK^n (n≠0), PDG/Planck observational pin, SI/CGS unit conversion, or framework absolute built FROM M_KK^n. Mass/length/time dimension present.
- **MIXED**: ratio of two ABSOLUTEs whose dimensions cancel. Dim=0 AFTER cancellation, but both sides are M_KK-dependent. Exactly 3 entries per P4-D QR-5 (threshold ≤ 3).

## Sub-buckets

| Sub-bucket | Kind | Count |
|:---|:---|---:|
| `DK_RATIO` | RATIO | 76 |
| `PLANCK_OBS` | ABSOLUTE | 27 |
| `PDG_OBS` | ABSOLUTE | 25 |
| `UNIT_CONVERSION` | ABSOLUTE | 23 |
| `PURE_MATH` | RATIO | 15 |
| `SLOT_DEPENDENT_RATIO` | RATIO | 9 |
| `FRAMEWORK_ABS` | ABSOLUTE | 5 |
| `CANCELLATION_OF_ABSOLUTES` | MIXED | 3 |
| `PROVENANCE_META` | RATIO | 1 |

## Top-level counts

| Classification | Count |
|:---|---:|
| RATIO | 123 |
| ABSOLUTE | 58 |
| MIXED | 3 |
| **TOTAL** | **184** |

## Full table

| Name | Value | Classification | Sub-bucket | Dim (M_KK^n) | Session | Note |
|:---|---:|:---:|:---|:---:|:---:|:---|
| `PI` | 3.14159 | **RATIO** | PURE_MATH | 0 | - | pi = 3.14159...  mathematical constant |
| `M_Pl_reduced` | 2.4350e+18 | **ABSOLUTE** | PDG_OBS | obs | S7 | M_Pl_red = sqrt(hbar c / 8 pi G) -- CODATA |
| `M_Pl_unreduced` | 1.2209e+19 | **ABSOLUTE** | PDG_OBS | obs | S7 | M_Pl = sqrt(hbar c / G) -- CODATA |
| `G_N` | 6.6743e-11 | **ABSOLUTE** | PDG_OBS | obs | - | Newton constant, SI |
| `c_light` | 2.9979e+08 | **ABSOLUTE** | PDG_OBS | obs | - | speed of light, SI exact |
| `hbar_SI` | 1.0546e-34 | **ABSOLUTE** | PDG_OBS | obs | - | reduced Planck constant, CODATA |
| `h_planck_SI` | 6.6261e-34 | **ABSOLUTE** | PDG_OBS | obs | - | Planck constant, SI exact |
| `k_B` | 8.6173e-05 | **ABSOLUTE** | PDG_OBS | obs | - | Boltzmann constant, eV/K |
| `k_B_SI` | 1.3806e-23 | **ABSOLUTE** | PDG_OBS | obs | - | Boltzmann constant, SI exact |
| `eV_SI` | 1.6022e-19 | **ABSOLUTE** | UNIT_CONVERSION | conv | - | 1 eV = 1.602e-19 J |
| `eV_per_GeV` | 1.0000e+09 | **ABSOLUTE** | UNIT_CONVERSION | conv | - | 1 GeV = 1e9 eV |
| `A_Bohr` | 5.2918e-11 | **ABSOLUTE** | PDG_OBS | obs | - | Bohr radius, CODATA |
| `arcsec_to_rad` | 4.8481e-06 | **ABSOLUTE** | UNIT_CONVERSION | conv | - | pi/(180*3600) |
| `alpha_em_MZ_inv` | 127.955 | **RATIO** | PDG_OBS | 0 | S42 | 1/alpha_em at M_Z -- dimensionless |
| `sin2_thetaW_MSbar` | 0.23122 | **RATIO** | PDG_OBS | 0 | - | sin^2 theta_W -- dimensionless |
| `M_Z` | 91.1876 | **ABSOLUTE** | PDG_OBS | obs | S42 | Z mass, PDG |
| `M_W` | 80.3692 | **ABSOLUTE** | PDG_OBS | obs | - | W mass, PDG |
| `G_N_cgs` | 6.6743e-08 | **ABSOLUTE** | UNIT_CONVERSION | conv | - | G_N * 1000 |
| `c_light_cgs` | 2.9979e+10 | **ABSOLUTE** | UNIT_CONVERSION | conv | - | c_light * 100 |
| `c_light_km_s` | 299792 | **ABSOLUTE** | UNIT_CONVERSION | conv | - | c_light / 1000 |
| `hbar_c_GeV_fm` | 0.197327 | **ABSOLUTE** | UNIT_CONVERSION | conv | - | hbar c in GeV*fm |
| `hbar_c_GeV_m` | 1.9733e-16 | **ABSOLUTE** | UNIT_CONVERSION | conv | - | hbar c in GeV*m |
| `hbar_c_GeV_cm` | 1.9733e-14 | **ABSOLUTE** | UNIT_CONVERSION | conv | - | hbar c in GeV*cm |
| `hbar_eV_s` | 6.5821e-16 | **ABSOLUTE** | UNIT_CONVERSION | conv | - | hbar in eV*s |
| `hbar_GeV_s` | 6.5821e-25 | **ABSOLUTE** | UNIT_CONVERSION | conv | - | hbar in GeV*s |
| `l_Planck` | 1.6163e-35 | **ABSOLUTE** | PDG_OBS | obs | - | Planck length, CODATA |
| `l_Planck_cm` | 1.6163e-33 | **ABSOLUTE** | UNIT_CONVERSION | conv | - | l_Planck * 100 |
| `t_Planck` | 5.3912e-44 | **ABSOLUTE** | PDG_OBS | obs | - | Planck time, CODATA |
| `H_0_km_s_Mpc` | 67.4 | **ABSOLUTE** | PLANCK_OBS | obs | - | Hubble parameter, Planck 2018 |
| `H_0_inv_s` | 2.1840e-18 | **ABSOLUTE** | PLANCK_OBS | obs | - | H_0 in s^{-1} |
| `H_0_GeV` | 1.4380e-42 | **ABSOLUTE** | PLANCK_OBS | obs | - | H_0 in GeV |
| `T_CMB` | 2.7255 | **ABSOLUTE** | PLANCK_OBS | obs | - | CMB temperature, COBE/FIRAS (K) |
| `T_CMB_GeV` | 2.3487e-13 | **ABSOLUTE** | PLANCK_OBS | obs | - | T_CMB * k_B / 1e9 |
| `rho_Lambda_obs` | 2.7000e-47 | **ABSOLUTE** | PLANCK_OBS | obs | S42 | Lambda in GeV^4, Planck |
| `Lambda_obs_MP4` | 2.8880e-122 | **MIXED** | CANCELLATION_OF_ABSOLUTES | 0 | - | Lambda/M_Pl^4: [GeV^4]/[GeV^4] -> dim=0; two external absolutes canceling to the observed CC number. |
| `A_s_CMB` | 2.1000e-09 | **RATIO** | PLANCK_OBS | 0 | - | Scalar amplitude -- dimensionless |
| `Omega_r` | 9.1500e-05 | **RATIO** | PLANCK_OBS | 0 | - | Omega_r -- dimensionless |
| `Omega_m` | 0.315 | **RATIO** | PLANCK_OBS | 0 | - | Omega_m -- dimensionless |
| `Omega_b` | 0.0493 | **RATIO** | PLANCK_OBS | 0 | - | Omega_b -- dimensionless |
| `Omega_DM` | 0.2657 | **RATIO** | PLANCK_OBS | 0 | - | Omega_DM = Omega_m - Omega_b -- dimensionless |
| `Omega_Lambda` | 0.685 | **RATIO** | PLANCK_OBS | 0 | - | Omega_Lambda -- dimensionless |
| `sigma_8` | 0.811 | **RATIO** | PLANCK_OBS | 0 | - | sigma_8 amplitude -- dimensionless |
| `rho_crit_GeV4` | 4.0800e-47 | **ABSOLUTE** | PLANCK_OBS | obs | - | 3 H_0^2 / (8 pi G), GeV^4 |
| `rho_crit_cgs` | 1.8780e-29 | **ABSOLUTE** | PLANCK_OBS | obs | - | g/cm^3 |
| `eta_BBN_obs` | 6.1200e-10 | **RATIO** | PLANCK_OBS | 0 | - | n_B/n_gamma -- dimensionless |
| `eta_BBN_err` | 4.0000e-12 | **RATIO** | PLANCK_OBS | 0 | - | 1-sigma on eta_BBN -- dimensionless |
| `T_BBN_GeV` | 0.001 | **ABSOLUTE** | PLANCK_OBS | obs | - | T at BBN ~ 1 MeV |
| `T_recomb_GeV` | 2.6000e-10 | **ABSOLUTE** | PLANCK_OBS | obs | - | T at recombination ~ 0.26 eV |
| `z_BBN` | 4.0000e+08 | **RATIO** | PLANCK_OBS | 0 | - | BBN redshift -- dimensionless |
| `t_universe_s` | 4.3500e+17 | **ABSOLUTE** | PLANCK_OBS | obs | - | Age of universe, s |
| `sigma_FIRAS` | 1.0000e-06 | **RATIO** | PLANCK_OBS | 0 | - | FIRAS delta_mu bound -- dimensionless |
| `FIRAS_dT_bound` | 3.0000e-06 | **RATIO** | PLANCK_OBS | 0 | - | FIRAS delta_T/T -- dimensionless |
| `GeV_to_inv_s` | 1.5193e+24 | **ABSOLUTE** | UNIT_CONVERSION | conv | - | 1 GeV -> s^-1 |
| `GeV_to_inv_m` | 5.0677e+15 | **ABSOLUTE** | UNIT_CONVERSION | conv | - | 1 GeV -> m^-1 |
| `GeV_inv_to_Mpc` | 6.3949e-39 | **ABSOLUTE** | UNIT_CONVERSION | conv | - | GeV^-1 -> Mpc |
| `Mpc_to_GeV_inv` | 1.5637e+38 | **ABSOLUTE** | UNIT_CONVERSION | conv | - | Mpc -> GeV^-1 |
| `GeV_to_kg` | 1.7827e-27 | **ABSOLUTE** | UNIT_CONVERSION | conv | - | 1 GeV/c^2 -> kg |
| `GeV_to_g` | 1.7827e-24 | **ABSOLUTE** | UNIT_CONVERSION | conv | - | 1 GeV/c^2 -> g |
| `Mpc_to_fm` | 3.0857e+38 | **ABSOLUTE** | UNIT_CONVERSION | conv | - | 1 Mpc -> fm |
| `Mpc_to_m` | 3.0857e+22 | **ABSOLUTE** | UNIT_CONVERSION | conv | - | 1 Mpc -> m |
| `Mpc_to_cm` | 3.0857e+24 | **ABSOLUTE** | UNIT_CONVERSION | conv | - | 1 Mpc -> cm |
| `Gpc_to_m` | 3.0857e+25 | **ABSOLUTE** | UNIT_CONVERSION | conv | - | 1 Gpc -> m |
| `kpc_to_cm` | 3.0857e+21 | **ABSOLUTE** | UNIT_CONVERSION | conv | - | 1 kpc -> cm |
| `tau_fold` | 0.19 | **RATIO** | DK_RATIO | 0 | S12/S42 | Jensen deformation parameter at van Hove singularity -- dimensionless |
| `phi_paasch` | 1.53158 | **RATIO** | DK_RATIO | 0 | - | Paasch spectral ratio -- dimensionless identity |
| `T_GGE_B2` | 0.668 | **ABSOLUTE** | FRAMEWORK_ABS | 1 | - | B2 GGE temp in M_KK units; value 0.668 = T_GGE / M_KK |
| `Vol_SU3_Haar` | 1349.74 | **RATIO** | PURE_MATH | 0 | S44 | 8*sqrt(3)*pi^4 -- exact Weyl integration |
| `Vol_SU3_WRONG` | 8880.93 | **RATIO** | PURE_MATH | 0 | S42 | kept for audit -- do not use |
| `g0_diag` | 3 | **RATIO** | PURE_MATH | 0 | - | Killing normalization, integer 3 |
| `M_KK_gravity` | 7.4287e+16 | **ABSOLUTE** | FRAMEWORK_ABS | 1 | S42 | AXIOMATIC pin, gravity route; n=1 by definition |
| `M_KK_kerner` | 5.0417e+17 | **ABSOLUTE** | FRAMEWORK_ABS | 1 | S42 | AXIOMATIC pin, Kerner route; n=1 by definition |
| `M_KK` | 7.4287e+16 | **ABSOLUTE** | FRAMEWORK_ABS | 1 | - | alias for M_KK_gravity; THE external pin |
| `OOM_diff_MKK` | 0.831665 | **MIXED** | CANCELLATION_OF_ABSOLUTES | 0 | - | log10(M_KK_kerner/M_KK_gravity): RATIO of two ABSOLUTE pins; M_KK cancels. Two-route tension metric. |
| `E_cond_ED_8mode` | -0.136851 | **RATIO** | DK_RATIO | 0 | S36 | E_cond / M_KK (M_KK units); ED eigenvalue ratio |
| `E_cond_ED_5mode` | -0.115077 | **RATIO** | DK_RATIO | 0 | S35 | superseded; same unit structure |
| `E_cond_GL` | -0.156 | **RATIO** | DK_RATIO | 0 | S37 | GL free-energy density / M_KK^4 integrated, dimensionless |
| `E_cond` | -0.136851 | **RATIO** | DK_RATIO | 0 | S36 | alias for E_cond_ED_8mode |
| `E_exc_ratio` | 443 | **RATIO** | DK_RATIO | 0 | - | E_exc / |E_cond| -- ratio of D_K spectral quantities |
| `E_exc` | 60.6248 | **RATIO** | DK_RATIO | 0 | - | = E_exc_ratio * |E_cond|, M_KK units |
| `n_pairs` | 59.8 | **RATIO** | DK_RATIO | 0 | - | pair count -- integer/real count |
| `N_dof_BCS` | 8 | **RATIO** | PURE_MATH | 0 | - | Fock dimension = 8 (integer) |
| `T_compound` | 7.5781 | **RATIO** | DK_RATIO | 0 | - | E_exc/8 in M_KK units |
| `Delta_0_GL` | 0.770435 | **RATIO** | DK_RATIO | 0 | S37 | GL order parameter in M_KK units |
| `Delta_0_OES` | 0.464255 | **RATIO** | DK_RATIO | 0 | S37 | OES gap in M_KK units -- eigenvalue ratio |
| `Delta_BCS` | 0.464255 | **RATIO** | DK_RATIO | 0 | S70 | alias; R-PROTECTED eigenvalue ratio (drift 0%) |
| `Delta_B3` | 0.176 | **RATIO** | DK_RATIO | 0 | - | B3 gap in M_KK units |
| `M_max_thouless` | 1.674 | **RATIO** | DK_RATIO | 0 | S35 | Thouless parameter max, dimensionless |
| `S_inst` | 0.0686037 | **RATIO** | DK_RATIO | 0 | S37/S38 | instanton action S_inst / hbar -- dimensionless |
| `xi_BCS` | 0.808347 | **RATIO** | DK_RATIO | 0 | S37 | xi_BCS * M_KK -- dimensionless; length in M_KK^-1 |
| `xi_GL` | 0.976321 | **RATIO** | DK_RATIO | 0 | S37 | xi_GL * M_KK -- dimensionless |
| `xi_BCS_over_BW` | 13.9523 | **RATIO** | DK_RATIO | 0 | - | xi in bandwidth units -- pure ratio |
| `a_GL` | -0.524548 | **RATIO** | DK_RATIO | 0 | S37 | GL a coefficient, dimensionless in M_KK units |
| `b_GL` | 0.441858 | **RATIO** | DK_RATIO | 0 | S37 | GL b coefficient, dimensionless in M_KK units |
| `barrier_0d` | 0.00467034 | **RATIO** | DK_RATIO | 0 | - | 0D barrier in M_KK units |
| `barrier_1d` | 0.155678 | **RATIO** | DK_RATIO | 0 | - | 1D barrier in M_KK units |
| `omega_PV` | 0.791659 | **RATIO** | DK_RATIO | 0 | S37 | omega_PV in M_KK units |
| `omega_split` | 1.33718 | **RATIO** | DK_RATIO | 0 | - | omega_split in M_KK units |
| `ratio_Evac_Econd` | 28.7562 | **RATIO** | DK_RATIO | 0 | - | pure ratio E_vac/E_cond |
| `Gamma_Langer_BCS` | 0.249736 | **RATIO** | DK_RATIO | 0 | S38 | Langer rate in M_KK units |
| `Kapitza_ratio` | 0.0302001 | **RATIO** | DK_RATIO | 0 | S38 | pure ratio -- Kapitza resistance ratio |
| `a0_fold` | 6440 | **RATIO** | SLOT_DEPENDENT_RATIO | 0 | S42 | zeta_D(0) half-mode-count at L=3, zeta-slot pinned; dim=0 in zeta, mass-dim d in SDW (cross-scheme) |
| `a2_fold` | 2776.17 | **RATIO** | SLOT_DEPENDENT_RATIO | 0 | S42 | zeta_D(1) half-sum 1/lam^2, zeta-slot pinned; dim=0 in zeta, mass-dim d-2 in SDW |
| `a4_fold` | 1350.72 | **RATIO** | SLOT_DEPENDENT_RATIO | 0 | S42 | zeta_D(2) half-sum 1/lam^4, zeta-slot pinned; dim=0 in zeta, mass-dim d-4 in SDW |
| `R_protected_fold` | 1.12865 | **RATIO** | DK_RATIO | 0 | S73B/S74 | a_0 * a_4 / a_2^2 -- Baptista B2, Vol(K) cancels identically |
| `Lizzi_signature` | 1.12865 | **RATIO** | DK_RATIO | 0 | S74 | = R_1 identity; (m_H/v)^2 * (Lambda/M_Pl^2) collapses |
| `S_fold` | 250361 | **RATIO** | DK_RATIO | 0 | S42 | spectral action at fold in f_n-moments (zeta slot, L=3) |
| `m_tau` | 2.062 | **RATIO** | DK_RATIO | 0 | - | modulus mass in M_KK units |
| `omega_att` | 1.43 | **RATIO** | DK_RATIO | 0 | - | attractor freq in M_KK units |
| `omega_tau` | 8.27 | **RATIO** | DK_RATIO | 0 | - | transit freq d(tau)/dt * M_KK^-1 |
| `M_ATDHFB` | 1.695 | **RATIO** | DK_RATIO | 0 | S40 | collective mass in M_KK units |
| `Z_fold` | 74730.8 | **RATIO** | DK_RATIO | 0 | - | gradient stiffness in f_n-moments |
| `G_DeWitt` | 5 | **RATIO** | PURE_MATH | 0 | S42 | DeWitt moduli-kinetic coefficient = 5 (normalization) |
| `dS_fold` | 58672.8 | **RATIO** | DK_RATIO | 0 | - | dS/dtau at fold, dimensionless in zeta slot |
| `d2S_fold` | 317863 | **RATIO** | DK_RATIO | 0 | - | d^2 S/dtau^2 at fold, dimensionless |
| `c_fabric` | 209.974 | **RATIO** | DK_RATIO | 0 | - | fabric sound speed -- dimensionless ratio (c_fabric / c_light) |
| `H_fold` | 586.527 | **RATIO** | DK_RATIO | 0 | S38 | Hubble at fold, M_KK units |
| `v_terminal` | 26.545 | **RATIO** | DK_RATIO | 0 | S38 | modulus terminal velocity, dimensionless |
| `dt_transit` | 0.00113016 | **RATIO** | DK_RATIO | 0 | - | transit duration in M_KK^-1 |
| `P_exc_kz` | 1 | **RATIO** | PURE_MATH | 0 | - | probability = 1 exactly |
| `n_Bog` | 0.998633 | **RATIO** | DK_RATIO | 0 | - | Bogoliubov fraction, dimensionless |
| `g_SU2_fold` | 2.05158 | **RATIO** | DK_RATIO | 0 | - | SU(2)^2 coupling -- dimensionless |
| `g_U1_fold` | 4.38685 | **RATIO** | DK_RATIO | 0 | - | U(1) coupling squared -- dimensionless |
| `alpha2_MKK_inv` | 47.856 | **RATIO** | DK_RATIO | 0 | - | 1/alpha_2 = 4pi/g_SU2 -- dimensionless |
| `sin2_thetaW_fold` | 0.583853 | **RATIO** | DK_RATIO | 0 | - | Weinberg angle at fold -- dimensionless |
| `mellin_f_star_f0` | 0.08832 | **RATIO** | SLOT_DEPENDENT_RATIO | 0 | S78 | f* Mellin moment dim=0; f*-slot pinned |
| `mellin_f_star_f2` | 214.973 | **RATIO** | SLOT_DEPENDENT_RATIO | 0 | S78 | f* Mellin moment dim=0; f*-slot pinned, X_MAX=50 regulator |
| `mellin_f_star_f4` | 6446.64 | **RATIO** | SLOT_DEPENDENT_RATIO | 0 | S78 | f* Mellin moment dim=0; f*-slot pinned, X_MAX=50 regulator |
| `rho_Lambda_spectral` | 8.4317e+73 | **ABSOLUTE** | FRAMEWORK_ABS | 4 | - | rho_Lambda_SA = (2/pi^2) a_0 M_KK^4 -- dim 4 |
| `CC_ratio` | 3.1229e+120 | **MIXED** | CANCELLATION_OF_ABSOLUTES | 0 | - | rho_spectral/rho_obs: [GeV^4]/[GeV^4] -> dim=0. Framework-vs-observation ratio; the CC problem itself. |
| `clock_coeff` | -3.08 | **RATIO** | DK_RATIO | 0 | - | d alpha / alpha = clock_coeff * dtau -- dimensionless |
| `N_cells` | 32 | **RATIO** | PURE_MATH | 0 | S42 | Voronoi count = 32 (integer combinatorial) |
| `L_over_xi` | 0.031 | **RATIO** | DK_RATIO | 0 | - | system/coherence length -- dimensionless |
| `J_C2` | 0.933 | **RATIO** | DK_RATIO | 0 | - | Josephson coupling, M_KK units |
| `J_su2` | 0.059 | **RATIO** | DK_RATIO | 0 | - | Josephson coupling, M_KK units |
| `J_u1` | 0.038 | **RATIO** | DK_RATIO | 0 | - | Josephson coupling, M_KK units |
| `T_acoustic` | 0.112 | **RATIO** | DK_RATIO | 0 | - | GGE acoustic T in M_KK units |
| `rho_B2_per_mode` | 14.0233 | **RATIO** | DK_RATIO | 0 | S37 | DOS per mode, dimensionless |
| `E_B1` | 0.81914 | **RATIO** | DK_RATIO | 0 | S38 | B1 eigenvalue in M_KK units |
| `E_B2_mean` | 0.845269 | **RATIO** | DK_RATIO | 0 | S38 | B2 mean eigenvalue |
| `E_B3_mean` | 0.978224 | **RATIO** | DK_RATIO | 0 | S38 | B3 mean eigenvalue |
| `c_Gold` | 0.915 | **RATIO** | DK_RATIO | 0 | - | Goldstone sound speed / c_substrate, dimensionless |
| `c_Gold_over_c_fabric` | 0.00436 | **RATIO** | DK_RATIO | 0 | S52 | R-PROTECTED ratio, drift 0% |
| `omega_L1` | 0.138 | **RATIO** | DK_RATIO | 0 | - | Leggett-1 freq in M_KK units |
| `omega_L2` | 0.192 | **RATIO** | DK_RATIO | 0 | - | Leggett-2 freq in M_KK units |
| `omega_H1` | 0.38 | **RATIO** | DK_RATIO | 0 | - | Higgs-1 freq in M_KK units |
| `omega_H2` | 1.41 | **RATIO** | DK_RATIO | 0 | - | Higgs-2 freq in M_KK units |
| `omega_H3` | 11.465 | **RATIO** | DK_RATIO | 0 | - | Higgs-3 freq in M_KK units |
| `alpha_QM` | -0.579 | **RATIO** | DK_RATIO | 0 | - | quantum metric K^4 coefficient -- dimensionless |
| `N_e_classical` | 0.1734 | **RATIO** | DK_RATIO | 0 | - | classical e-fold ceiling -- dimensionless theorem |
| `J_12_over_J_23` | 19.52 | **RATIO** | DK_RATIO | 0 | - | tau-independent Josephson ratio |
| `phi_CP` | 0 | **RATIO** | PURE_MATH | 0 | - | CP phase = 0 structural zero |
| `gamma_RP` | 0.0398 | **RATIO** | DK_RATIO | 0 | - | Ruelle-Pollicott gap in M_KK units |
| `t_deph_over_t_transit` | 139729 | **RATIO** | DK_RATIO | 0 | - | decoherence/transit ratio -- dimensionless |
| `F_BCS_over_V_KK` | 0.0071 | **RATIO** | DK_RATIO | 0 | - | BCS/V_KK probe ratio -- dimensionless |
| `IBO_ratio` | 1118 | **RATIO** | DK_RATIO | 0 | - | geom fast/BCS slow ratio |
| `S2_HFB` | -0.131 | **RATIO** | DK_RATIO | 0 | - | HFB pair correlation, dimensionless |
| `a_scatter` | -0.00158 | **RATIO** | DK_RATIO | 0 | - | scattering length in M_KK^-1 |
| `M_Bog_max` | 0.02273 | **RATIO** | DK_RATIO | 0 | - | Bogoliubov amplitude, dimensionless |
| `AUDIT_SESSION_FLOOR` | 34 | **RATIO** | PROVENANCE_META | 0 | - | session floor -- integer, not physical |
| `v_ew` | 246 | **ABSOLUTE** | PDG_OBS | obs | - | LATENT PIN RISK -- v_ew = 246 GeV, S80-CF-4 audit |
| `m_H_obs` | 125.1 | **ABSOLUTE** | PDG_OBS | obs | - | Higgs mass, PDG |
| `m_t_pole` | 172.69 | **ABSOLUTE** | PDG_OBS | obs | - | top pole, PDG |
| `m_b_pole` | 4.78 | **ABSOLUTE** | PDG_OBS | obs | - | bottom pole, PDG |
| `m_b_1S` | 4.18 | **ABSOLUTE** | PDG_OBS | obs | - | bottom 1S, PDG |
| `m_mu` | 0.105658 | **ABSOLUTE** | PDG_OBS | obs | - | muon mass, PDG |
| `alpha_s_MZ_obs` | 0.118 | **RATIO** | PDG_OBS | 0 | - | alpha_s(M_Z), dimensionless |
| `g_star_SM` | 106.75 | **RATIO** | PDG_OBS | 0 | - | SM dof count -- dimensionless |
| `g_star_BBN` | 10.75 | **RATIO** | PDG_OBS | 0 | - | BBN dof count -- dimensionless |
| `N_eff_SM` | 3.044 | **RATIO** | PDG_OBS | 0 | - | SM N_eff -- dimensionless |
| `b1_SM` | 4.1 | **RATIO** | PURE_MATH | 0 | - | SM one-loop 41/10 -- exact rational |
| `b2_SM` | -3.16667 | **RATIO** | PURE_MATH | 0 | - | SM one-loop -19/6 -- exact rational |
| `b3_SM` | -7 | **RATIO** | PURE_MATH | 0 | - | SM one-loop -7 -- exact integer |
| `w0_FW` | -0.918 | **RATIO** | DK_RATIO | 0 | - | w_0 prediction -- dimensionless |
| `wa_FW` | 0 | **RATIO** | PURE_MATH | 0 | - | wa = 0 structural zero |
| `w0_LCDM` | -1 | **RATIO** | PURE_MATH | 0 | - | LCDM reference w_0 = -1 (by definition) |
| `wa_LCDM` | 0 | **RATIO** | PURE_MATH | 0 | - | LCDM reference w_a = 0 (by definition) |
| `planck_ns` | 0.9649 | **RATIO** | PLANCK_OBS | 0 | - | n_s, Planck 2018 -- dimensionless |
| `planck_ns_err` | 0.0042 | **RATIO** | PLANCK_OBS | 0 | - | 1-sigma on n_s |
| `planck_alpha_s` | -0.0045 | **RATIO** | PLANCK_OBS | 0 | - | dn_s/d ln k, dimensionless |
| `planck_alpha_s_err` | 0.0067 | **RATIO** | PLANCK_OBS | 0 | - | 1-sigma on alpha_s |
| `Q_Leggett` | 670000 | **RATIO** | DK_RATIO | 0 | - | Leggett Q factor = 6.7e5, dimensionless |
| `f_0_sharp` | 1 | **RATIO** | SLOT_DEPENDENT_RATIO | 0 | S78 | f_0 = 1 numeric (sharp cutoff, Theta(1-x)), dim=0; anomaly-slot PROVENANCE note f_0=1/2 forced |
| `f_2_default` | 2.34 | **RATIO** | SLOT_DEPENDENT_RATIO | 0 | S62 | Gaussian-cutoff f_2 = 2.34, dim=0; slot-pinned |
| `f_4_default` | 0.558 | **RATIO** | SLOT_DEPENDENT_RATIO | 0 | S62 | Gaussian-cutoff f_4 = 0.558, dim=0; slot-pinned |

## MIXED entries (the exactly-3 cancellation cases)

| Name | Substitution chain | Physical meaning |
|:---|:---|:---|
| `OOM_diff_MKK` | log10(M_KK_kerner / M_KK_gravity). Both ABSOLUTE pins (M_KK^1). Ratio cancels M_KK dimension -> dim=0. | Two-route tension metric. |M_i| > 1 warning: 0.83 OOM gap between gravity and Kerner routes. |
| `CC_ratio` | rho_Lambda_spectral / rho_Lambda_obs. Both [GeV^4] -> dim=0. Spectral side = (2/pi^2) a_0 M_KK^4. | The CC problem itself: ratio ~ 10^120. Cancellation exposes the gap. |
| `Lambda_obs_MP4` | Lambda_obs / M_Pl^4. Both [GeV^4] -> dim=0. | Observed CC in Planck units ~ 2.888e-122. External-absolute ratio. |

## Slot-dependent RATIOs (9)

Dim=0 in their pinned scheme slot, but VALUE shifts between slots. Tagged SLOT_DEPENDENT_RATIO (sub-bucket of RATIO):

- `a0_fold`: zeta_D(0) half-mode-count at L=3, zeta-slot pinned; dim=0 in zeta, mass-dim d in SDW (cross-scheme)
- `a2_fold`: zeta_D(1) half-sum 1/lam^2, zeta-slot pinned; dim=0 in zeta, mass-dim d-2 in SDW
- `a4_fold`: zeta_D(2) half-sum 1/lam^4, zeta-slot pinned; dim=0 in zeta, mass-dim d-4 in SDW
- `mellin_f_star_f0`: f* Mellin moment dim=0; f*-slot pinned
- `mellin_f_star_f2`: f* Mellin moment dim=0; f*-slot pinned, X_MAX=50 regulator
- `mellin_f_star_f4`: f* Mellin moment dim=0; f*-slot pinned, X_MAX=50 regulator
- `f_0_sharp`: f_0 = 1 numeric (sharp cutoff, Theta(1-x)), dim=0; anomaly-slot PROVENANCE note f_0=1/2 forced
- `f_2_default`: Gaussian-cutoff f_2 = 2.34, dim=0; slot-pinned
- `f_4_default`: Gaussian-cutoff f_4 = 0.558, dim=0; slot-pinned

## Verdict

Gate **S80-CANONICAL-CONSTANTS-RATIOS-VS-ABSOLUTES-CLASSIFICATION**: **PASS**

- 184/184 classified; 0 missing, 0 extra.
- RATIO = 123 (67% of total)
- ABSOLUTE = 58 (32% of total)
- MIXED = 3 (≤ 3 threshold per P4-D QR-5)
- No ambiguous dimensional behavior detected.
- Single-pin {M_KK} verified across all FRAMEWORK_ABS entries (n∈{1,4}); v_ew remains on audit list per CF-4 (S80-FRAMEWORK-SINGLE-PIN-VERIFICATION).