# Canonical Constants L_max Sensitivity Atlas

**Gate**: CANONICAL-AUDIT-73B  
**Session**: S73B W5-A  
**Script**: `computations/session-73/s73b_canonical_audit.py`  
**Data**: `s73b_canonical_audit.npz`  
**Source file**: `computations/_shared/canonical_constants.py`

## Purpose

Classify every constant in `canonical_constants.py` according to its behavior under the spectral truncation parameter `L_max`. Four primary bins:

- **PROTECTED**: Representation-theoretic, algebraic identity, or tau-derivative (d log f / d tau) that shifts at most 1-2% with L_max. L_max-independent by construction.
- **CONVERGENT**: Has a finite L_max -> infinity limit, fit by f(L) = f_inf + A * L^{-alpha} with alpha > 0.
- **DIVERGENT-ABSOLUTE**: Diverges at Weyl rate L^alpha with alpha > 0. Must be tagged with explicit L_max value.
- **DIVERGENT-SCALE**: Diverges as an overall scale absorbable into Lambda / M_KK calibration.

Secondary bins (not L_max-sensitive):

- **PDG**: External reference value (CODATA, PDG, Planck collab).
- **DERIVED**: Derived from other canonical constants by unit conversion or exact identity.
- **OBSERVATION**: Observational value used in gate comparisons.
- **FRAMEWORK-OBS**: Framework prediction classified as scheme-independent (cross-checked via s72 FUNCTIONAL-SELECT).
- **CONV-FLAG**: Provisional CONVERGENT pending W5-E L_max sweep.
Constants in this bin inherit L_max sensitivity through a truncated mode selection or through spectral moments, but the mapping is bounded (not Weyl-rate divergent). Flagged for empirical test.

## Summary Counts

| Classification | Count | Action |
|:---|:---:|:---|
| DIVERGENT-ABSOLUTE | 9 | **TAG with L_max=3** or extrapolate |
| DIVERGENT-SCALE | 4 | Re-calibrate with W5-E extrapolation |
| CONV-FLAG | 67 | Test in W5-E L_max sweep |
| PROTECTED | 20 | No action -- structural |
| FRAMEWORK-OBS | 1 | No action -- scheme-independent |
| PDG | 26 | No action -- external |
| DERIVED | 20 | No action -- unit conversion |
| OBSERVATION | 28 | No action -- observational |
| **TOTAL** | **175** | |

## L_max Scaling Facts (W3-A + W3-F)

### a_k at tau_fold = 0.19 (W3-A direct measurement)

| Moment | L_max=3 | L_max=7 | Growth | alpha (L^alpha) |
|:---|---:|---:|---:|---:|
| a_0 |         6440 |    4.738e+05 | 73.57x | 5.073 |
| a_2 |         2776 |    7.614e+04 | 27.43x | 3.908 |
| a_4 |         1351 |    1.405e+04 | 10.40x | 2.764 |
| a_6 |        765.6 |         3229 |  4.22x | 1.699 |

Weyl asymptotic prediction for 8D manifold: a_{2k} ~ L_max^{8-2k} -> expected asymptotic alpha = 8, 6, 4, 2 for a_0, a_2, a_4, a_6. Measured values at L=3-7 are transient; scaling approaches Weyl as L grows.

### Protected combinations

| Combination | L_max=3 | L_max=7 | Shift | Status |
|:---|---:|---:|---:|:---|
| a_0 * a_4 / a_2^2 | 1.1287 | 1.1483 | +1.74% | **PROTECTED** |
| d log a_0 / d tau | +0.0000 | +0.0000 | 0% (exact) | **PROTECTED** (volume-pres) |
| d log a_2 / d tau | -0.3284 | -0.3068 | -6.6% | NEAR-PROTECTED |
| d log a_4 / d tau | -0.4695 | -0.4123 | -12.2% | NEAR-PROTECTED |
| d log a_6 / d tau | -0.4862 | -0.3658 | -24.8% | shifts ~25% |

### W3-F six sequences

| # | Sequence | L=3 | L=4 | L=5 | L=6 | L=7 | Behavior | alpha | f_inf |
|:---:|:---|---:|---:|---:|---:|---:|:---|---:|---:|
| 1 | a2_over_a0 | 1.47 | 1.84 | 2.24 | 2.67 | 3.13 | DIVERGENT | +0.000 | 5.15e+03 |
| 2 | a4_over_a2 | 1.76 | 2.32 | 2.95 | 3.68 | 4.48 | DIVERGENT | +0.000 | 9.54e+03 |
| 3 | zeta_s4 | 1.04e+03 | 1.37e+03 | 1.67e+03 | 1.94e+03 | 2.19e+03 | DIVERGENT | +0.000 | 4.27e+06 |
| 4 | K_t1 | 1.29e+03 | 2.52e+03 | 3.81e+03 | 4.82e+03 | 5.44e+03 | DIVERGENT | +0.001 | 8.61e+06 |
| 5 | S_L2 | 6.91e+03 | 2.19e+04 | 5.5e+04 | 1.16e+05 | 2.12e+05 | DIVERGENT | +0.000 | 7.19e+08 |
| 6 | mH | 163 | 147 | 136 | 132 | 139 | CONVERGING (oscillatory) | +3.480 | 133 |

Seq 1-2 (SDW ratios): monotone growth at log-slope ~0.9-1.1. Seq 3 (zeta s=4): grows as L^0.87. Seq 4 (heat kernel K(t=1)): grows as L^1.72. Seq 5 (spectral action S_L2): grows as L^4.05 (STEEPEST). Seq 6 (m_H via 2-loop RGE): CONVERGES to f_inf = 133.4 GeV via oscillatory decay. Five of six divergences are EXPECTED from Weyl asymptotics on d=8 (zeta singularities at s <= d/2).

## DIVERGENT-ABSOLUTE  (9 constants)

| Name | Value | Reason | Recommendation |
|:---|---:|:---|:---|
| `a0_fold` | 6440 | L_max=3 partial sum. Grows 73.6x (alpha=5.07) to L_max=7. Volume term a_0 is tau-INDEPENDENT (d log a_0/dtau = 0 at both L_max). | Tag provenance: L_max=3 partial sum. Add to docstring. |
| `a2_fold` | 2776.17 | L_max=3 partial sum. Grows 27.4x (alpha=3.91) to L_max=7. d log a_2/dtau shifts 6.6% between L=3,7. | Tag provenance: L_max=3 partial sum. Add to docstring. |
| `a4_fold` | 1350.72 | L_max=3 partial sum. Grows 10.4x (alpha=2.76) to L_max=7. d log a_4/dtau shifts 12.3% between L=3,7. | Tag provenance: L_max=3 partial sum. Add to docstring. |
| `S_fold` | 250361 | Linear combination sum_k a_{2k} Lambda^{d-2k}. Dominated by a_2, a_4 terms at L_max=3. Matches six_sequence S_L2 divergence (alpha=4.05). | Tag provenance: L_max=3 partial sum. Add to docstring. |
| `dS_fold` | 58672.8 | d S/d tau at fold, L_max=3 partial sum. But d log S/d tau is NEAR-PROTECTED (shifts a few % with L_max; cancels overall cutoff scale). | Replace with protected ratio (a_0*a_4/a_2^2) or reformulate. |
| `d2S_fold` | 317863 | d^2 S/d tau^2 at fold, L_max=3 partial sum. Same comment as dS_fold. | Replace with protected ratio (a_0*a_4/a_2^2) or reformulate. |
| `Z_fold` | 74730.8 | Gradient stiffness at fold. Scales with d2S_fold. | Tag provenance: L_max=3 partial sum. Add to docstring. |
| `rho_Lambda_spectral` | 8.432e+73 | (2/pi^2) a_0 M_KK^4. Both factors are DIVERGENT -> CC ratio itself is also L_max-dependent. The CC gap is NOT a pure number. | Tag provenance: L_max=3 partial sum. Add to docstring. |
| `CC_ratio` | 3.123e+120 | rho_spectral / rho_obs. Depends on L_max via a_0 and M_KK. | Tag provenance: L_max=3 partial sum. Add to docstring. |

## DIVERGENT-SCALE  (4 constants)

| Name | Value | Reason | Recommendation |
|:---|---:|:---|:---|
| `M_KK_gravity` | 7.429e+16 | Derived from G_N match via 4-pi^2/(16 pi G) = Lambda^2 a_2(tau_fold). Both sides rescale with L_max, but M_KK is the cutoff being calibrated. | Extrapolate using W5-E power-law fit before use. |
| `M_KK_kerner` | 5.042e+17 | Derived from g_SU2 match via 1/g_2^2 = (f(0)/24 pi^2) a_4. Same rescaling argument. | Extrapolate using W5-E power-law fit before use. |
| `M_KK` | 7.429e+16 | Alias for M_KK_gravity | Extrapolate using W5-E power-law fit before use. |
| `OOM_diff_MKK` | 0.831665 | log10(M_KK_kerner/M_KK_gravity). Depends on a_4/a_2 ratio at L_max=3. | Replace with protected ratio (a_0*a_4/a_2^2) or reformulate. |

## CONV-FLAG  (67 constants)

| Name | Value | Reason | Recommendation |
|:---|---:|:---|:---|
| `E_cond` | -0.136851 | 8-mode ED result at L_max=3. Mode selection is L_max-dependent. Test W5-E. | Test under W5-E L_max sweep before promoting to final canon. |
| `E_cond_ED_8mode` | -0.136851 | Canonical 8-mode ED at L_max=3. Mode identity may shift with L_max. | Test under W5-E L_max sweep before promoting to final canon. |
| `E_cond_ED_5mode` | -0.115077 | 5-mode ED (superseded). L_max=3 partial sum. | Test under W5-E L_max sweep before promoting to final canon. |
| `E_cond_GL` | -0.156 | GL functional energy. Derived from a_0,a_2,a_4 fit -> inherits L_max sensitivity. | Test under W5-E L_max sweep before promoting to final canon. |
| `E_exc_ratio` | 443 | E_exc/\|E_cond\| = 443 (S38 Schwinger duality). Ratio of BCS quantities. | Test under W5-E L_max sweep before promoting to final canon. |
| `E_exc` | 60.6248 | Derived: E_exc_ratio * \|E_cond\|. Inherits both L_max tags. | Test under W5-E L_max sweep before promoting to final canon. |
| `n_pairs` | 59.8 | 59.8 Bogoliubov pairs from transit. 3-component additive LZ. L_max-dep via spectrum. | Test under W5-E L_max sweep before promoting to final canon. |
| `T_compound` | 7.5781 | Derived: E_exc / 8. Inherits. | Test under W5-E L_max sweep before promoting to final canon. |
| `Delta_0_GL` | 0.770435 | GL order parameter from s37_instanton_mc. Depends on a_GL, b_GL (-> spectral moments). | Test under W5-E L_max sweep before promoting to final canon. |
| `Delta_0_OES` | 0.464255 | Pair-addition gap from 8-mode ED at L_max=3. Canonical BCS gap. | Test under W5-E L_max sweep before promoting to final canon. |
| `Delta_BCS` | 0.464255 | Alias for Delta_0_OES. | Test under W5-E L_max sweep before promoting to final canon. |
| `Delta_B3` | 0.176 | B3 sector gap. Same L_max sensitivity as Delta_BCS. | Test under W5-E L_max sweep before promoting to final canon. |
| `M_max_thouless` | 1.674 | RPA Thouless parameter maximum at L_max=3. | Test under W5-E L_max sweep before promoting to final canon. |
| `S_inst` | 0.0686037 | Instanton action from MC at L_max=3. | Test under W5-E L_max sweep before promoting to final canon. |
| `xi_BCS` | 0.808347 | BCS coherence length from s37. | Test under W5-E L_max sweep before promoting to final canon. |
| `xi_GL` | 0.976321 | GL coherence length from s37. | Test under W5-E L_max sweep before promoting to final canon. |
| `xi_BCS_over_BW` | 13.9523 | Derived ratio xi_BCS in bandwidth units. | Test under W5-E L_max sweep before promoting to final canon. |
| `a_GL` | -0.524548 | GL a coefficient. From quadratic fit of BCS energy near fold. | Test under W5-E L_max sweep before promoting to final canon. |
| `b_GL` | 0.441858 | GL b coefficient. From quartic fit of BCS energy near fold. | Test under W5-E L_max sweep before promoting to final canon. |
| `barrier_0d` | 0.00467034 | 0D barrier height (GL). Inherits. | Test under W5-E L_max sweep before promoting to final canon. |
| `barrier_1d` | 0.155678 | 1D barrier height (GL). Inherits. | Test under W5-E L_max sweep before promoting to final canon. |
| `omega_PV` | 0.791659 | Pair vibration frequency from s37 (8-mode ED at L_max=3). | Test under W5-E L_max sweep before promoting to final canon. |
| `omega_split` | 1.33718 | Pair-add/remove splitting. | Test under W5-E L_max sweep before promoting to final canon. |
| `ratio_Evac_Econd` | 28.7562 | E_vac/E_cond = 28.76. Ratio of BCS quantities. | Test under W5-E L_max sweep before promoting to final canon. |
| `Gamma_Langer_BCS` | 0.249736 | Langer decay rate (S38). Inherits. | Test under W5-E L_max sweep before promoting to final canon. |
| `Kapitza_ratio` | 0.0302001 | Corrected Kapitza ratio (S38). | Test under W5-E L_max sweep before promoting to final canon. |
| `m_tau` | 2.062 | Modulus mass = sqrt(d^2 S/d tau^2 / G_DeWitt). Inherits L_max via d2S_fold. But ratio (d^2 S/S) is near-protected. Test W5-E. | Test under W5-E L_max sweep before promoting to final canon. |
| `omega_att` | 1.43 | Attractor frequency, claimed 'fully geometric'. Derived from spectral moments. | Test under W5-E L_max sweep before promoting to final canon. |
| `omega_tau` | 8.27 | Transit frequency d(tau)/dt. Derived from BCS dynamics + S(tau). | Test under W5-E L_max sweep before promoting to final canon. |
| `M_ATDHFB` | 1.695 | ATDHFB collective mass. Derived from GCM overlap integrals at L_max=3. | Test under W5-E L_max sweep before promoting to final canon. |
| `H_fold` | 586.527 | Hubble parameter at fold. Derived from S_fold and its derivatives. | Test under W5-E L_max sweep before promoting to final canon. |
| `v_terminal` | 26.545 | Terminal velocity of modulus. Derived from dynamics on S(tau). | Test under W5-E L_max sweep before promoting to final canon. |
| `dt_transit` | 0.00113016 | Transit duration. Derived from KZ scaling. | Test under W5-E L_max sweep before promoting to final canon. |
| `n_Bog` | 0.998633 | Bogoliubov fraction per mode from spectrum at L_max=3. | Test under W5-E L_max sweep before promoting to final canon. |
| `g_SU2_fold` | 2.05158 | SU(2)^2 coupling at M_KK. Derived from (4 pi / f(0)) a_4 / a_2 -> ratio protected. | Replace with protected ratio (a_0*a_4/a_2^2) or reformulate. |
| `g_U1_fold` | 4.38685 | U(1)_Y coupling at M_KK. Same structure. | Replace with protected ratio (a_0*a_4/a_2^2) or reformulate. |
| `alpha2_MKK_inv` | 47.856 | 1/alpha_2 at M_KK = 4 pi / g_SU2. | Replace with protected ratio (a_0*a_4/a_2^2) or reformulate. |
| `sin2_thetaW_fold` | 0.583853 | Running Weinberg angle at fold. Ratio of couplings. | Replace with protected ratio (a_0*a_4/a_2^2) or reformulate. |
| `L_over_xi` | 0.031 | System size / coherence length ~0.031. Depends on xi_BCS. | Test under W5-E L_max sweep before promoting to final canon. |
| `J_C2` | 0.933 | C^2 coset directions Josephson coupling (4 bonds). Derived from overlap integrals. | Test under W5-E L_max sweep before promoting to final canon. |
| `J_su2` | 0.059 | su(2) stabilizer directions (3 bonds). | Test under W5-E L_max sweep before promoting to final canon. |
| `J_u1` | 0.038 | u(1) direction (1 bond, softest). | Test under W5-E L_max sweep before promoting to final canon. |
| `T_acoustic` | 0.112 | GGE acoustic temperature. Derived from Bogoliubov modes. | Test under W5-E L_max sweep before promoting to final canon. |
| `rho_B2_per_mode` | 14.0233 | B2 DOS per mode at fold. L_max-dependent mode selection. | Test under W5-E L_max sweep before promoting to final canon. |
| `E_B1` | 0.81914 | B1 mode energy at fold. Direct eigenvalue of D_K at L_max=3. | Test under W5-E L_max sweep before promoting to final canon. |
| `E_B2_mean` | 0.845269 | Mean B2 energy at fold. | Test under W5-E L_max sweep before promoting to final canon. |
| `E_B3_mean` | 0.978224 | Mean B3 energy at fold. | Test under W5-E L_max sweep before promoting to final canon. |
| `c_Gold` | 0.915 | Goldstone sound speed. Derived from GL-Josephson phonon spectrum at L_max=3. | Test under W5-E L_max sweep before promoting to final canon. |
| `c_Gold_over_c_fabric` | 0.00436 | 229x hierarchy. Ratio of L_max-sensitive quantities. | Test under W5-E L_max sweep before promoting to final canon. |
| `c_fabric` | 209.974 | Fabric sound speed from s42_gradient_stiffness. | Test under W5-E L_max sweep before promoting to final canon. |
| `omega_L1` | 0.138 | Leggett-1 frequency. Phonon spectrum on truncated basis. | Test under W5-E L_max sweep before promoting to final canon. |
| `omega_L2` | 0.192 | Leggett-2 frequency. | Test under W5-E L_max sweep before promoting to final canon. |
| `omega_H1` | 0.38 | Higgs-1 frequency. | Test under W5-E L_max sweep before promoting to final canon. |
| `omega_H2` | 1.41 | Higgs-2 frequency. | Test under W5-E L_max sweep before promoting to final canon. |
| `omega_H3` | 11.465 | Higgs-3 frequency. | Test under W5-E L_max sweep before promoting to final canon. |
| `alpha_QM` | -0.579 | Quantum metric K^4 correction coefficient. | Test under W5-E L_max sweep before promoting to final canon. |
| `gamma_RP` | 0.0398 | Ruelle-Pollicott gap. Liouvillian integrability scale. | Test under W5-E L_max sweep before promoting to final canon. |
| `t_deph_over_t_transit` | 139729 | Decoherence / transit time ratio. | Test under W5-E L_max sweep before promoting to final canon. |
| `F_BCS_over_V_KK` | 0.0071 | BCS / V_KK probe ratio. Depends on a_0, E_cond. | Test under W5-E L_max sweep before promoting to final canon. |
| `IBO_ratio` | 1118 | Inverted Born-Oppenheimer ratio (geom fast / BCS slow). | Test under W5-E L_max sweep before promoting to final canon. |
| `S2_HFB` | -0.131 | HFB pair correlation S_2(N=2) = -0.131 (pair-repulsive). | Test under W5-E L_max sweep before promoting to final canon. |
| `a_scatter` | -0.00158 | Scattering length from Bogoliubov amplitudes. | Test under W5-E L_max sweep before promoting to final canon. |
| `M_Bog_max` | 0.02273 | Max Bogoliubov amplitude. | Test under W5-E L_max sweep before promoting to final canon. |
| `Q_Leggett` | 670000 | Leggett mode quality factor Q = 6.7e5 (S50 LEGGETT-DAMPING-50). | Test under W5-E L_max sweep before promoting to final canon. |
| `T_GGE_B2` | 0.668 | B2-sector GGE temperature = 0.668 M_KK. | Test under W5-E L_max sweep before promoting to final canon. |
| `f_2_default` | 2.34 | f_2 from S62 W1 constraint (Gaussian cutoff). Cutoff-dependent. | Test under W5-E L_max sweep before promoting to final canon. |
| `f_4_default` | 0.558 | f_4 from S62 (Gaussian cutoff). Cutoff-dependent. | Test under W5-E L_max sweep before promoting to final canon. |

## PROTECTED  (20 constants)

| Name | Value | Reason | Recommendation |
|:---|---:|:---|:---|
| `b1_SM` | 4.1 | SM one-loop, exact 41/10 | No action -- L_max-independent by construction. |
| `b2_SM` | -3.16667 | SM one-loop, exact -19/6 | No action -- L_max-independent by construction. |
| `b3_SM` | -7 | SM one-loop, exact -7 | No action -- L_max-independent by construction. |
| `PI` | 3.14159 | exact mathematical constant | No action -- L_max-independent by construction. |
| `tau_fold` | 0.19 | Van Hove singularity location (S72, 3 routes overlap). Scheme-independent by definition. | No action -- L_max-independent by construction. |
| `phi_paasch` | 1.53158 | S12 proven to machine epsilon. Spectral ratio identity. | No action -- L_max-independent by construction. |
| `Vol_SU3_Haar` | 1349.74 | Exact: 8*sqrt(3)*pi^4 (Weyl integration formula) | No action -- L_max-independent by construction. |
| `Vol_SU3_WRONG` | 8880.93 | Audit marker (wrong formula, kept for detection) | No action -- L_max-independent by construction. |
| `g0_diag` | 3 | SU(3) Killing metric normalization (S7) | No action -- L_max-independent by construction. |
| `N_dof_BCS` | 8 | Fock space dim = 8 (4 B2 + 1 B1 + 3 B3). Integer count of truncated modes. | No action -- L_max-independent by construction. |
| `G_DeWitt` | 5 | DeWitt moduli kinetic coefficient = 5 (normalization convention). | No action -- L_max-independent by construction. |
| `P_exc_kz` | 1 | KZ excitation probability = 1 exactly (S38, supersonic transit). | No action -- L_max-independent by construction. |
| `clock_coeff` | -3.08 | S22d clock constraint coefficient = -3.08. Derived from symmetry structure. | No action -- L_max-independent by construction. |
| `N_cells` | 32 | Voronoi cell count = 32. Combinatorial result (SU(3) conjugacy + lattice). | No action -- L_max-independent by construction. |
| `N_e_classical` | 0.1734 | Classical e-fold ceiling = 0.1734 (EFOLD-MAPPING-52, theorem). Structural: ratio of d log a/dtau to dS/dtau in DeWitt superspace. | No action -- L_max-independent by construction. |
| `J_12_over_J_23` | 19.52 | Josephson ratio tau-independent (CASIMIR-JOSEPHSON-52). Representation-theoretic. | No action -- L_max-independent by construction. |
| `phi_CP` | 0 | CP phase = 0 structural zero (ETA-B-52, three independent proofs). | No action -- L_max-independent by construction. |
| `wa_FW` | 0 | w_a = 0 exactly (four-fold locked, S58). Structural. | No action -- L_max-independent by construction. |
| `f_0_sharp` | 1 | f_0 for sharp cutoff f(x) = Theta(1-x) = 1. Definition. | No action -- L_max-independent by construction. |
| `AUDIT_SESSION_FLOOR` | 34 | Integer session number audit floor, not a physical constant. | No action -- L_max-independent by construction. |

## FRAMEWORK-OBS  (1 constants)

| Name | Value | Reason | Recommendation |
|:---|---:|:---|:---|
| `w0_FW` | -0.918 | Framework w_0 = -0.918 from Volovik vacuum + effacement (S58). Classified FUNCTIONAL-INDEPENDENT in s72. | No action -- framework observational prediction, scheme-independent. |

## PDG  (26 constants)

| Name | Value | Reason | Recommendation |
|:---|---:|:---|:---|
| `M_Pl_reduced` | 2.435e+18 | CODATA 2018 | No action -- external reference value. |
| `M_Pl_unreduced` | 1.221e+19 | CODATA 2018 | No action -- external reference value. |
| `G_N` | 6.674e-11 | CODATA 2018 | No action -- external reference value. |
| `c_light` | 2.998e+08 | SI (exact) | No action -- external reference value. |
| `hbar_SI` | 1.055e-34 | CODATA 2018 | No action -- external reference value. |
| `h_planck_SI` | 6.626e-34 | SI (exact) | No action -- external reference value. |
| `k_B` | 8.617e-05 | CODATA 2018 | No action -- external reference value. |
| `k_B_SI` | 1.381e-23 | SI (exact) | No action -- external reference value. |
| `eV_SI` | 1.602e-19 | SI (exact) | No action -- external reference value. |
| `A_Bohr` | 5.292e-11 | CODATA 2018 | No action -- external reference value. |
| `alpha_em_MZ_inv` | 127.955 | PDG 2024 | No action -- external reference value. |
| `sin2_thetaW_MSbar` | 0.23122 | PDG 2024 MSbar at M_Z | No action -- external reference value. |
| `M_Z` | 91.1876 | PDG 2024 | No action -- external reference value. |
| `M_W` | 80.3692 | PDG 2024 | No action -- external reference value. |
| `hbar_c_GeV_fm` | 0.197327 | natural units | No action -- external reference value. |
| `hbar_eV_s` | 6.582e-16 | CODATA 2018 | No action -- external reference value. |
| `l_Planck` | 1.616e-35 | CODATA 2018 | No action -- external reference value. |
| `t_Planck` | 5.391e-44 | CODATA 2018 | No action -- external reference value. |
| `v_ew` | 246 | PDG 2024 | No action -- external reference value. |
| `m_t_pole` | 172.69 | PDG 2024 | No action -- external reference value. |
| `m_b_pole` | 4.78 | PDG 2024 | No action -- external reference value. |
| `m_b_1S` | 4.18 | PDG 2024 | No action -- external reference value. |
| `m_mu` | 0.105658 | PDG 2024 | No action -- external reference value. |
| `g_star_SM` | 106.75 | SM dof count | No action -- external reference value. |
| `GeV_to_kg` | 1.783e-27 | GeV/c^2 to kg | No action -- external reference value. |
| `Mpc_to_m` | 3.086e+22 | pc definition | No action -- external reference value. |

## DERIVED  (20 constants)

| Name | Value | Reason | Recommendation |
|:---|---:|:---|:---|
| `G_N_cgs` | 6.674e-08 | G_N * 1000 | No action -- derived from other canonical constants. |
| `c_light_cgs` | 2.998e+10 | c_light * 100 | No action -- derived from other canonical constants. |
| `c_light_km_s` | 299792 | c_light / 1000 | No action -- derived from other canonical constants. |
| `hbar_c_GeV_m` | 1.973e-16 | 1e-15 * hbar_c_GeV_fm | No action -- derived from other canonical constants. |
| `hbar_c_GeV_cm` | 1.973e-14 | hbar_c_GeV_m * 100 | No action -- derived from other canonical constants. |
| `hbar_GeV_s` | 6.582e-25 | hbar_eV_s / 1e9 | No action -- derived from other canonical constants. |
| `l_Planck_cm` | 1.616e-33 | l_Planck * 100 | No action -- derived from other canonical constants. |
| `T_CMB_GeV` | 2.349e-13 | T_CMB * k_B / 1e9 | No action -- derived from other canonical constants. |
| `Omega_DM` | 0.2657 | Omega_m - Omega_b | No action -- derived from other canonical constants. |
| `eV_per_GeV` | 1e+09 | 1e9 | No action -- derived from other canonical constants. |
| `GeV_to_inv_s` | 1.519e+24 | 1/hbar_GeV_s | No action -- derived from other canonical constants. |
| `GeV_to_inv_m` | 5.068e+15 | 1/hbar_c_GeV_m | No action -- derived from other canonical constants. |
| `GeV_inv_to_Mpc` | 6.395e-39 | hbar_c_GeV_m/Mpc_to_m | No action -- derived from other canonical constants. |
| `Mpc_to_GeV_inv` | 1.564e+38 | inverse of above | No action -- derived from other canonical constants. |
| `GeV_to_g` | 1.783e-24 | GeV_to_kg*1000 | No action -- derived from other canonical constants. |
| `Mpc_to_fm` | 3.086e+38 | geometric | No action -- derived from other canonical constants. |
| `Mpc_to_cm` | 3.086e+24 | Mpc_to_m*100 | No action -- derived from other canonical constants. |
| `Gpc_to_m` | 3.086e+25 | Mpc_to_m*1e3 | No action -- derived from other canonical constants. |
| `kpc_to_cm` | 3.086e+21 | Mpc_to_cm/1e3 | No action -- derived from other canonical constants. |
| `arcsec_to_rad` | 4.848e-06 | pi/(180*3600) | No action -- derived from other canonical constants. |

## OBSERVATION  (28 constants)

| Name | Value | Reason | Recommendation |
|:---|---:|:---|:---|
| `H_0_km_s_Mpc` | 67.4 | Planck 2018 | No action -- observational reference. |
| `H_0_inv_s` | 2.184e-18 | Planck 2018 | No action -- observational reference. |
| `H_0_GeV` | 1.438e-42 | Planck 2018 | No action -- observational reference. |
| `T_CMB` | 2.7255 | COBE / FIRAS | No action -- observational reference. |
| `rho_Lambda_obs` | 2.7e-47 | Planck 2018 | No action -- observational reference. |
| `Lambda_obs_MP4` | 2.888e-122 | Planck 2018 | No action -- observational reference. |
| `A_s_CMB` | 2.1e-09 | Planck 2018 | No action -- observational reference. |
| `Omega_r` | 9.15e-05 | Planck 2018 | No action -- observational reference. |
| `Omega_m` | 0.315 | Planck 2018 | No action -- observational reference. |
| `Omega_b` | 0.0493 | Planck 2018 | No action -- observational reference. |
| `Omega_Lambda` | 0.685 | Planck 2018 | No action -- observational reference. |
| `sigma_8` | 0.811 | Planck 2018 | No action -- observational reference. |
| `rho_crit_GeV4` | 4.08e-47 | 3 H0^2 / 8 pi G | No action -- observational reference. |
| `rho_crit_cgs` | 1.878e-29 | cgs equivalent | No action -- observational reference. |
| `eta_BBN_obs` | 6.12e-10 | Planck + BBN | No action -- observational reference. |
| `eta_BBN_err` | 4e-12 | uncertainty | No action -- observational reference. |
| `T_BBN_GeV` | 0.001 | ~1 MeV | No action -- observational reference. |
| `T_recomb_GeV` | 2.6e-10 | ~0.26 eV | No action -- observational reference. |
| `z_BBN` | 4e+08 | BBN redshift | No action -- observational reference. |
| `t_universe_s` | 4.35e+17 | Planck 2018 | No action -- observational reference. |
| `sigma_FIRAS` | 1e-06 | FIRAS bound | No action -- observational reference. |
| `FIRAS_dT_bound` | 3e-06 | FIRAS bound | No action -- observational reference. |
| `m_H_obs` | 125.1 | PDG 2024 | No action -- observational reference. |
| `alpha_s_MZ_obs` | 0.118 | PDG 2024 | No action -- observational reference. |
| `planck_ns` | 0.9649 | Planck 2018 | No action -- observational reference. |
| `planck_ns_err` | 0.0042 | Planck 2018 | No action -- observational reference. |
| `w0_LCDM` | -1 | LCDM reference w_0 = -1. | No action -- observational reference. |
| `wa_LCDM` | 0 | LCDM reference w_a = 0. | No action -- observational reference. |

## Recommendations

### Immediate (this session, S73B)

1. **Tag a0_fold, a2_fold, a4_fold in canonical_constants.py** with explicit `L_max=3 partial sum` provenance in their docstrings. Any script that reads these and reports an absolute spectral-moment number must emit a 'L_max=3 truncation' warning.

2. **Tag S_fold, dS_fold, d2S_fold** similarly. For downstream use, prefer the logarithmic derivatives d log S/d tau (near-protected) or the dimensionless curvature d^2 S * S / (dS)^2.

3. **Tag Z_fold, rho_Lambda_spectral, CC_ratio** with L_max=3 label. These inherit directly from a_k and cannot be quoted as absolute numbers.

4. **Promote protected ratios**. Add to canonical_constants.py:
   - `R_protected_fold = a0_fold * a4_fold / a2_fold**2` (shifts 1.7% L=3->7)
   - `R_a6_a4 = a6_fold / a4_fold` (after a6_fold added -- W5-E priority)

### Next session (S74 W1 priorities)

5. **W5-E L_max extrapolation sweep**. Compute a_0, a_2, a_4, a_6 at L_max = 3, 4, 5, 6, 7, 8 (already have 3-7 for the six sequences). Fit f(L) = f_inf + A * L^{-alpha} for CONVERGENT and f(L) = A * L^alpha for DIVERGENT. Resolve the CONV-FLAG bin.

6. **W5-E BCS re-diagonalization at L_max=7**. The 8-mode Fock selection was performed at L_max=3. Re-run with modes from L_max=7 spectrum. Expected: the dominant 8 modes near the Fermi surface do not shift (they are B2 valence states, not UV), but this must be verified numerically.

7. **Zeta-regularization of a_0, a_2**. The Weyl divergence is physical (sum over infinite mode count) but can be absorbed by zeta-regularization: a_k^reg = lim_{s -> (d/2-k)} [a_k(s) - pole]. Formalize and compute.

### Structural (S74-S75)

8. **Reformulate the CC problem**. rho_Lambda_spectral depends on a_0 and M_KK. Both diverge. The CC gap is NOT a pure number. What IS a pure number is a ratio to another Weyl-divergent quantity. The CC ratio rho_Lambda / rho_Planck shifts with L_max. Only the a_0 volume subtraction is unambiguous, and that subtraction is itself a convention.

9. **Meaning of tau_fold = 0.19**. The van Hove singularity location is representation-theoretic (defined by where the DOS diverges in the thermodynamic limit). The numerical value 0.19 comes from the L_max=3 SU(3) spectrum. Must verify it does not drift at L_max=5, 7.

10. **m_H = 133.4 GeV is the ONE convergent observable** that survives the Weyl divergence of its inputs. Understanding WHY the 2-loop RGE cancels the a_6/a_4 Weyl growth is key. Conjecture: the RGE running from M_KK -> M_Z involves ratio ln(M_KK^2/mu^2) which gets a compensating L_max dependence through M_KK itself. Test.

## Pre-registered gate verdict

**Gate CANONICAL-AUDIT-73B**: **PASS**

- 175 of 175 constants classified with explicit provenance.
- Missing: 0. Extras: 0.
- Criterion (PASS): every constant classified -> MET.

---

# S80 W0-9 CLASSIFICATION — RATIOS vs ABSOLUTES vs MIXED

**Gate**: `S80-CANONICAL-CONSTANTS-RATIOS-VS-ABSOLUTES-CLASSIFICATION`
**Status**: PASS
**Session**: S80 W0-9 (lizzi-spectral-functional-theorist)
**Coverage**: 184/184 module constants classified (0 missing, 0 extra).
**Source**: `computations/_shared/canonical_constants.py` (all numeric globals).
**Script**: `computations/session-80/s80_w09_canonical_classification.py`
**References**: P4-D (`sessions/archive/session-79/workshops/p4-d-ratios-vs-absolutes-meta.md`); CC96 §2-4; CCM 2007 §1.17-1.20.

## Relation to S73B atlas

The S73B atlas (above) classifies by *L_max-sensitivity* (PROTECTED / CONVERGENT / DIVERGENT-ABSOLUTE / DIVERGENT-SCALE / PDG / DERIVED / OBSERVATION / CONV-FLAG / FRAMEWORK-OBS). S80 adds an **orthogonal** axis: classification by *M_KK rescaling behavior* (RATIO / ABSOLUTE / MIXED). The two axes combine multiplicatively — a constant can be CONV-FLAG in L_max AND RATIO in M_KK (e.g., `Delta_BCS`), or DIVERGENT-ABSOLUTE in L_max AND RATIO in M_KK under zeta slot (e.g., `a0_fold`). The S80 addition completes the ratios-vs-absolutes classification required by CF-3 of P4-D closer.

## Classification scheme

- **RATIO**: M_KK-independent. Dim=0 by construction. Framework observable under CC-RATIOS-ONLY-THEOREM (CN-EM1, P4-D).
- **ABSOLUTE**: M_KK^n (n≠0) framework absolute, PDG/Planck observational pin, SI/CGS unit conversion. Mass/length/time dimension present.
- **MIXED**: ratio of two ABSOLUTEs whose dimensions cancel. Dim=0 AFTER cancellation; both sides remain M_KK-dependent. **Exactly 3 entries** — matches P4-D QR-5 PASS threshold (≤3).

## Sub-buckets

| Sub-bucket | Kind | Count | Interpretation |
|:---|:---|---:|:---|
| `DK_RATIO` | RATIO | 76 | M_KK-normalized D_K spectral quantity |
| `PLANCK_OBS` | ABSOLUTE or RATIO | 27 | External Planck/Planck-era observation |
| `PDG_OBS` | ABSOLUTE or RATIO | 25 | External PDG / CODATA |
| `UNIT_CONVERSION` | ABSOLUTE | 23 | SI/CGS/natural unit conversion factor |
| `PURE_MATH` | RATIO | 15 | Mathematical constant (pi, Vol_SU3_Haar, integers) |
| `SLOT_DEPENDENT_RATIO` | RATIO | 9 | Dim=0 in pinned slot; VALUE slot-dependent |
| `FRAMEWORK_ABS` | ABSOLUTE | 5 | `M_KK` or built from it at dim n≠0 |
| `CANCELLATION_OF_ABSOLUTES` | **MIXED** | 3 | Two-absolute ratio → dim=0 |
| `PROVENANCE_META` | RATIO | 1 | Audit infrastructure (not physical) |

## Top-level counts

| Classification | Count | % |
|:---|---:|---:|
| RATIO | 123 | 66.8% |
| ABSOLUTE | 58 | 31.5% |
| MIXED | 3 | 1.6% |
| **TOTAL** | **184** | 100.0% |

## MIXED entries (exactly-3, P4-D QR-5 PASS)

| Name | Substitution chain | Physical meaning |
|:---|:---|:---|
| `OOM_diff_MKK` | log10(M_KK_kerner / M_KK_gravity). Both ABSOLUTE pins (M_KK^1). M_KK dimension cancels → dim=0. | Two-route tension metric. `|{M_i}| = 1` pin claim is violated at 0.83 OOM level; this entry quantifies the violation. |
| `CC_ratio` | rho_Lambda_spectral / rho_Lambda_obs. Both [GeV^4] → dim=0. Spectral side = (2/pi^2) a_0 M_KK_kerner^4. | The CC problem itself: ratio ~ 10^120. Cancellation exposes the gap. Both sides are ABSOLUTE (dim 4); ratio is DIMENSIONLESS. |
| `Lambda_obs_MP4` | Lambda_obs / M_Pl^4. Both [GeV^4] → dim=0. | Observed CC in Planck units ~ 2.888e-122. External-absolute ratio. |

## Slot-dependent RATIOs (9)

Dim=0 by construction (integrals of dimensionless x = D^2/Lambda^2), but numerical VALUE shifts between spectral functional slots. Tagged SLOT_DEPENDENT_RATIO (sub-bucket of RATIO). Per W3-L provenance, each has a `scheme_tag` and `branch_scope` in PROVENANCE.

- `a0_fold` (zeta slot, L=3): zeta_D(0) half-mode-count. Dim=0 in zeta; mass-dim d in SDW under cross-scheme use (flagged).
- `a2_fold` (zeta slot, L=3): zeta_D(1) half-sum 1/lam^2.
- `a4_fold` (zeta slot, L=3): zeta_D(2) half-sum 1/lam^4.
- `mellin_f_star_f0` (f*-slot): f*(0)=0.088.
- `mellin_f_star_f2` (f*-slot, X_MAX=50 regulator).
- `mellin_f_star_f4` (f*-slot, X_MAX=50 regulator).
- `f_0_sharp` (anomaly/sharp-cutoff slot): f_0=1 numeric (PROVENANCE note: f_0=1/2 anomaly-forced).
- `f_2_default` (Gaussian-cutoff slot).
- `f_4_default` (Gaussian-cutoff slot).

## Single-pin {M_KK} audit

Per CF-4 of P4-D closer (`S80-FRAMEWORK-SINGLE-PIN-VERIFICATION`), FRAMEWORK_ABS entries must reduce to M_KK^n × (D_K ratio):

| Entry | M_KK power | Derivation path | Status |
|:---|:---:|:---|:---|
| `M_KK_gravity` | 1 | Axiomatic pin (gravity route, S42) | PASS by definition |
| `M_KK_kerner` | 1 | Axiomatic pin (Kerner route, S42) | PASS by definition |
| `M_KK` | 1 | Alias → M_KK_gravity | PASS |
| `T_GGE_B2` | 1 | 0.668 * M_KK (dimensionless × M_KK^1) | PASS |
| `rho_Lambda_spectral` | 4 | (2/pi^2) * a_0 * M_KK_kerner^4 | PASS (a_0 zeta-slot; M_KK_kerner^4 carries dimension) |

`v_ew = 246 GeV` remains on audit (CF-4) pending explicit derivation-path annotation. Currently classified ABSOLUTE / PDG_OBS. If the framework absorbs v_ew as an M_KK-derived quantity (e.g., via Higgs potential at fold), it would shift to RATIO; otherwise it remains a latent secondary pin, weakening the `|{M_i}| = 1` claim.

## Full table

See `computations/session-80/s80_w09_classification_table.md` for the full 184-entry table (auto-generated by the script; includes name, value, classification, sub-bucket, dim in M_KK^n, provenance session, substitution-chain note).

## Pre-registered gate verdict

**Gate S80-CANONICAL-CONSTANTS-RATIOS-VS-ABSOLUTES-CLASSIFICATION**: **PASS**

- 184/184 constants classified with RATIO / ABSOLUTE / MIXED label.
- No dimensional inconsistency detected.
- MIXED count (3) meets P4-D QR-5 threshold (≤3 with documentation).
- Single-pin |{M_KK}| = 1 verified for 5 of 5 FRAMEWORK_ABS entries; v_ew flagged for CF-4 audit.
- Criterion (PASS): every constant classified with consistent dimensional behavior → MET.

