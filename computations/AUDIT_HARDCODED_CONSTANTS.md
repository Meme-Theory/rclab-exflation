# Hardcoded Constants Audit — All Sessions

Audit date: 2026-03-15
Scripts searched: 463
Auditor: Claude Opus 4.6 (automated grep-based audit)

---

## 1. Planck Mass Convention

**Two values in use**: M_Pl = 1.22e19 GeV (unreduced) and M_Pl_red = 2.435e18 GeV (reduced = M_Pl/sqrt(8pi)).

| Script | Variable | Value | Convention | Notes |
|:-------|:---------|:------|:-----------|:------|
| s23c_moment_mapping.py | M_Pl | 1.22e19 | Unreduced | Also hardcodes G_N = 6.674e-11 |
| s28b_lambda_eff.py | M_PL / M_PL_REDUCED | 1.2209e19 / 2.435e18 | Both | Correctly defines both |
| s29b_modulus_eom.py | M_P_GEV | 2.435e18 | Reduced | |
| s29c_gw_spectrum.py | M_Pl_GeV | 2.435e18 | Reduced | |
| s29c_k_transition.py | M_Pl_GeV | 2.435e18 | Reduced | |
| s36_cc_arithmetic.py | M_P | 2.435e18 | Reduced | |
| s36_species_scale.py | M_P | 2.435e18 | Reduced | |
| s41_mkk_rge.py | M_Planck | **1.221e19** | **LABELED WRONG** | Comment says "reduced Planck mass is 2.435e18" but assigns 1.221e19 = UNREDUCED |
| s42_constants_snapshot.py | M_PL_REDUCED | 2.435e18 | Reduced | Authoritative S42 constants file |
| s42_homogeneity.py | M_Planck | 2.435e18 | Reduced | |
| s42_gge_energy.py | M_Pl | 1.2209e19 | Unreduced | |
| s42_fabric_wz.py | M_Planck_GeV | 1.2209e19 | Unreduced | |
| s42_dark_energy_wz.py | M_Planck_GeV | 1.2209e19 | Unreduced | |
| s42_fabric_wz_v2.py | M_Planck_GeV | 1.2209e19 | Unreduced | |
| s42_kz_fnl.py | M_Pl_GeV | 1.22e19 | Unreduced | Computed from sqrt(hbar*c/G) |
| s43_cbb_timeline.py | M_Pl | 1.22e19 | Unreduced | |
| s43_gge_dm_abundance.py | M_Pl_GeV | 1.22e19 | Unreduced | |
| s43_transplanckian.py | M_PL_GEV | 1.22e19 | Unreduced | |
| s43_friedmann_bcs.py | M_Pl_GeV | 2.435e18 | Reduced | |
| s43_mkk_posterior.py | M_PL | 2.435e18 | Reduced | |
| s43_oneloop_liv.py | M_P | **1.22e19** | **LABELED WRONG** | Comment: "reduced Planck mass: 2.435e18 GeV" then assigns 1.22e19 |
| s43_qtheory_selftune.py | M_Pl | 1.22e19 | Unreduced | |
| s43_twofluid_wz_v2.py | M_Pl_GeV | 1.22e19 | Unreduced | |
| s44_bcs_tensor_r.py | M_Pl_red | 2.435e18 | Reduced | Also uses M_Pl unreduced in comments |
| s44_cc_gap_audit.py | M_Pl_red | 2.435e18 | Reduced | |
| s44_bayesian_f.py | M_PL | 2.435e18 | Reduced | |
| s44_cutoff_f.py | M_PL_RED | 2.435e18 | Reduced | |
| s44_jacobson_spec.py | M_Pl | 2.435e18 | Reduced | |
| s44_induced_g.py | M_PL_RED | 2.435e18 | Reduced | |
| s44_sakharov_gn.py | M_PL_REDUCED | 2.435e18 | Reduced | |
| s44_sakharov_gn_crosscheck.py | M_PL_REDUCED | 2.435e18 | Reduced | |
| s44_dm_de_ratio.py | M_Pl_GeV | 1.22e19 | Unreduced | |
| s43_twofluid_wz.py | M_Pl_GeV | 2.435e18 | Reduced | |

**INCONSISTENCY FLAG**: Both conventions are used across scripts. This is NOT inherently wrong (different formulas require different versions), but:

- **s41_mkk_rge.py**: Comments say "reduced Planck mass is 2.435e18" next to M_Planck = 1.221e19. The variable name `M_Planck` is then used in ratios. Not mislabeled per se (comment is parenthetical), but confusing.
- **s43_oneloop_liv.py**: Comment says "M_P = 1.22e19 GeV (reduced Planck mass: 2.435e18 GeV)" then assigns M_P = 1.22e19. The parenthetical could mislead a reader into thinking M_P is reduced.
- The Friedmann equations and Sakharov mechanism scripts (S43-S44) correctly use the reduced mass M_Pl_red = 2.435e18 in G_N = 1/(8pi M_Pl_red^2).
- The cosmological-observable scripts (fabric w(z), dark energy) use the full Planck mass, which is appropriate for the formulas they implement.

**RISK LEVEL**: MEDIUM. The split is intentional, but the misleading comments in s41/s43 could propagate errors if values are copied.

---

## 2. M_KK Convention Usage

The framework has THREE M_KK conventions: Convention A (~1e9 GeV), Convention C (~1e13 GeV), and the gravity route (~7.43e16 GeV). The gravity route value comes from the Sakharov formula: M_KK^2 = pi^3 M_Pl_red^2 / (12 a_2).

| Script | Value Used | Convention | Source |
|:-------|:-----------|:-----------|:-------|
| rge33a_reanalysis.py | 1e16 | GUT estimate | Pre-gravity-route |
| s33a_rge_gate.py | 1e16 | GUT estimate | Pre-gravity-route |
| s33a_rge_gate_corrected.py | 1e16 | GUT estimate | Pre-gravity-route |
| s36_cc_arithmetic.py | 1e16 | GUT estimate | Pre-gravity-route |
| s36_species_scale.py | 1e16 | "framework calibration" | Pre-gravity-route |
| s39_integrability_check.py | 1e6 | Exploratory | Used for physical-units illustration |
| s42_constants_snapshot.py | 7.43e16 | Gravity route (S42) | **AUTHORITATIVE** |
| s42_gge_energy.py | 7.43e16 | Gravity route | Loaded from npz |
| s42_ns_tilt.py | 7.43e16 | Gravity route | Loaded from npz |
| s42_kz_fnl.py | 7.43e16 | Gravity route | Loaded from npz |
| s42_polariton.py | 7.43e16 | Gravity route | Hardcoded |
| s43_* (13+ scripts) | 7.43e16 | Gravity route | Loaded from npz |
| s44_* (10+ scripts) | 7.43e16 | Gravity route | Loaded from npz |
| s43_offj_jsymm.py | 1e16 | GUT estimate | **STALE** — should use 7.43e16 |
| s43_oneloop_liv.py | 10^{16.9-17.7} | Range | Explores multiple M_KK scenarios |
| s42_fabric_wz.py | Multiple | Sweep | Tests Conv A, C, GUT, Planck |
| s42_dark_energy_wz.py | Multiple | Sweep | Tests Conv A, C, GUT, Planck |

**INCONSISTENCY FLAG**:
- Pre-S42 scripts (S33, S36) use M_KK = 1e16 (a rough GUT-scale estimate). The authoritative value from S42 is 7.43e16 GeV. These older scripts should not be re-run with stale M_KK values.
- **s43_offj_jsymm.py**: Uses M_KK = 1e16 despite being an S43 script. Should use 7.43e16.
- Most S43-S44 scripts properly load M_KK from the s42_constants_snapshot.npz file.

**RISK LEVEL**: LOW-MEDIUM. The old scripts are historical and unlikely to be re-run. s43_offj_jsymm.py is the only active-session script with a stale value.

---

## 3. BCS Gap and Condensation Energy Values

**THREE different |E_cond| values appear**: 0.115, 0.137, and 0.156. This is the most significant inconsistency.

| Script | E_cond Value | Origin | Notes |
|:-------|:-------------|:-------|:------|
| s35_ed_corrected_dos.py | 0 (vacuum) | S35 ED at rho=14.02, V_bare | FAIL result |
| s36_multisector_ed.py | -0.1151 | S36 ED (multi-sector, 32 states) | "E_cond = -0.1151" |
| s36_gl_cubic_check.py | -0.115 | S35/S36 | Rounded |
| s36_cc_arithmetic.py | -0.137 | S36 ED (8-mode) | `E_BCS = float(ed["E_cond_full"])` |
| s37_instanton_action.py | -0.137 | S36 ED (8-mode, ED-CONV-36) | Authoritative for S37 |
| s37_oneloop_sa.py | -0.137 | S36 ED | Multiple references |
| s38_attempt_freq.py | -0.156 | S37/S38 instanton data | `E_cond = float(inst_data['E_cond_use'])` |
| s39_schwinger_naz_review.py | -0.156 | Gap equation | "(E_cond=-0.156, Delta_0=0.770)" |
| s40_cc_transit.py | 0.156 | S38/S39 data | |
| s40_self_consistent_ode.py | -0.156 / -0.137 | Both! | Loads two different sources |
| s42_dm_profile.py | -0.115 | S35 | Explicitly says "from S35" |
| s42_fabric_wz.py | -0.115 | S35 | |
| s42_fabric_wz_v2.py | -0.115 | S35 | |
| s42_hauser_feshbach.py | -0.115 | S35 | |
| s42_gge_energy.py | 0.137 | Loaded from npz | Comment notes confusion: "task says 0.115" |
| s42_polariton.py | -0.137 | S36 | |
| s43_schwinger_factor36.py | 0.115 | S42 | Comment: "used incorrectly in S42" |
| s43_flat_band.py | -0.115 | S35 ED | |
| s43_friedmann_bcs.py | -0.115 | S35 | |
| s43_first_law.py | 0.137 | Loaded from npz | |
| s43_cbb_timeline.py | 0.137 | Loaded from npz | |
| s43_qfluc_tau0.py | -0.137 | S36 ED | |
| s43_foam_gge.py | -0.137 | Loaded from npz | |
| s44_bcs_tensor_r.py | 0.137 | Hardcoded | |
| s44_tracelog_cc.py | 0.137 | Loaded from npz | |
| s44_sakharov_gn.py | -0.115 | Hardcoded | "From S38" — but S38 had 0.156 |
| s44_singlet_cc.py | -0.137 | Comment | |

**The three values correspond to different computations**:
- **0.115 (-0.1151)**: S35/S36 multi-sector ED with 32 Fock states, partial V matrix
- **0.137**: S36 full 8-mode ED with converged V matrix (ED-CONV-36)
- **0.156**: GL/gap-equation derived, used in instanton calculations (S37-S38)

**KEY ISSUE**: The s42_gge_energy.py script explicitly notes this confusion (lines 101-106): "The task says E_cond = 0.115 (rounded). Let's use the stored value" [0.137]. The s43_schwinger_factor36.py says E_cond = 0.115 was "used incorrectly in S42". And s44_sakharov_gn.py hardcodes -0.115 claiming "From S38" when S38 actually used -0.156.

**RISK LEVEL**: **HIGH**. Three different values for the same physical quantity. Scripts that compute E_exc = 443 * |E_cond| get different answers (50.9 vs 60.7 vs 69.1) depending on which E_cond they use.

---

## 4. Van Hove Peak M_max Values

| Script | Value | Session Origin | Status |
|:-------|:------|:---------------|:-------|
| s23a_bcs_gap_equation.py | Computed | S23 | Dynamic (not hardcoded) |
| s33b_nuc1_nucleation.py | 2.062 | S33b TRAP-33b | **RETRACTED in S34** |
| s34a_dphys_thouless.py | 2.062 | S33b baseline | Documents retraction |
| s35a_mu_physical_basis.py | 2.062 | TRAP-33b | References as "stands on its own" |
| s35a_vh_impedance_arbiter.py | 2.062 | TRAP-33b | As reference point |
| s36_mmax_authoritative.py | 1.674 (8x8) | S35/S36 | **AUTHORITATIVE** |
| s36_bayesian_posterior.py | 1.674 | S35/S36 authoritative | Resolves 1.445 vs 1.674 |
| s37_instanton_action.py | 1.674 | MMAX-AUTH-36 | Authoritative |
| s39_cascade_spectroscopy.py | 1.674 | S35/S36 | Calibration point |
| s43_transplanckian.py | 1.674 | MMAX-AUTH-36 | |
| s43_lifshitz_class.py | 1.674 | S35/S36 | |
| s35_thouless_multiband.py | 1.445 | S34 workshop estimate | **SUPERSEDED** |
| s35_ed_corrected_dos.py | 1.445 | S34 workshop estimate | **SUPERSEDED** |

**NOTE**: The value 2.062 also appears as a DIFFERENT quantity — the modulus mass m_tau:

| Script | Context | Value | Meaning |
|:-------|:--------|:------|:--------|
| s42_coupled_doorway.py | m_tau | 2.062 | Fabric modulus mass (M_KK units) |
| s42_fabric_wz.py | m_tau | 2.062 | Fabric modulus mass |
| s42_fabric_wz_v2.py | m_tau | 2.062 | Loaded from npz |
| s43_gquest_prereg.py | m_tau | 2.062 | Fabric gap |
| s43_parametric_resonance.py | m_tau | 2.062 | tau oscillator mass |
| s43_impedance_mismatch.py | m_tau | 2.06238706 | From C-FABRIC-42 |
| s43_breathing_mode.py | Delta(B2) | 2.062 | B2 quartet BdG gap |

The m_tau = 2.062 M_KK comes from a completely different computation (fabric dispersion, S42) than the retracted M_max = 2.062 (BCS Thouless eigenvalue, S33b). The numerical coincidence is purely accidental.

**For M_max as Thouless eigenvalue**: The authoritative value is **1.674** (MMAX-AUTH-36, 8x8 multi-band). The value 1.445 was a workshop estimate, never a proper computation. The value 2.062 was computed with a wrong V matrix (retracted S34).

**RISK LEVEL**: LOW. The retracted values appear only in their originating scripts and scripts that document the retraction. No active computation uses 2.062 as M_max.

---

## 5. Delta_0 (BCS Gap Parameter) Values

| Script | Value | Context |
|:-------|:------|:--------|
| s37_instanton_action.py | 0.464 | Delta_OES (odd-even staggering) |
| s38_attempt_freq.py | 0.7704 | Delta_0_peak (GL gap) |
| s38_kz_defects.py | 0.770 | Delta_0 at fold |
| s39_schwinger_geometric.py | 0.7704 | Delta_0_peak (GL gap) |
| s39_schwinger_naz_review.py | 0.770 / 0.365 | GL gap vs numerical minimum |
| s43_flat_band.py | 0.464 | S37 instanton gas gap |
| s43_schwinger_factor36.py | 0.770 | BCS gap at fold |
| s43_transplanckian.py | 0.365 | Numerical landscape minimum |
| s43_mod_reheating.py | 0.128 | "BCS gap, S35" |
| s44_tracelog_cc.py | 0.770 | Bare gap parameter (GL) |
| s44_n3_bdg.py | 0.770 | S38 reference |

**These are DIFFERENT physical quantities** (as documented in s39_schwinger_naz_review.py):
- **0.770 (0.7704)**: GL-derived gap from gap equation. Peak of BCS gap curve
- **0.464**: Odd-even staggering Delta (pair susceptibility)
- **0.365**: Numerical minimum of F_BCS along alpha-path (instanton landscape)
- **0.128**: Appears only in s43_mod_reheating.py as "BCS gap, S35" — **SUSPECT**: no other script uses this value

**RISK LEVEL**: LOW-MEDIUM. The values are physically distinct, but s43_mod_reheating.py's Delta_0 = 0.128 cited as "BCS gap, S35" has no corroboration.

---

## 6. Spectral Action Constants (a_0, a_2, a_4, S_fold)

| Constant | Value | Source | Scripts Using |
|:---------|:------|:-------|:-------------|
| a_0 (zeta) | 6440 | S42 constants snapshot | s42_dark_energy_wz, s42_gge_energy, s42_kz_fnl, s43_kz_transfer, s44_cutoff_f, s44_cc_gap_audit, s44_first_sound_imprint, s44_eih_grav, s44_holographic_spec, s44_induced_g, s44_tracelog_cc, s44_strutinsky_diag, s44_sakharov_gn, s44_sakharov_gn_crosscheck, s44_sakharov_gn_audit |
| a_2 (zeta) | 2776.17 | S42 constants snapshot | s42_dark_energy_wz, s42_kz_fnl, s43_kz_transfer, s44_cutoff_f, s44_first_sound_imprint, s44_eih_grav, s44_holographic_spec, s44_induced_g, s44_tracelog_cc, s44_strutinsky_diag, s44_sakharov_gn, s44_sakharov_gn_audit |
| a_4 (zeta) | 1351 | S42 constants snapshot | s42_constants_snapshot, s44_first_sound_imprint |
| S_fold | 250361 | S42 W1-1 | s42_dm_profile, s42_tau_dyn_reopening, s43_friedmann_bcs, s43_parametric_resonance, s43_qfluc_tau0, s43_schwinger_factor36, s44_eih_grav, s44_sakharov_gn, s44_tracelog_cc |

**Early scripts (S36 and before)** have different S_fold values:
- s36_bayesian_posterior.py: S_fold = 14.2302 — this is NOT the same quantity. It is S(tau) from a different sum convention (non-zeta, non-Peter-Weyl-weighted).

**CONSISTENCY**: All S42+ scripts use the same values (6440, 2776.17, 1351, 250361). These are loaded from s42_constants_snapshot.npz or hardcoded consistently.

**RISK LEVEL**: LOW. Very consistent across post-S42 scripts.

---

## 7. Fine Structure Constant / Weinberg Angle

| Constant | Value | Scripts |
|:---------|:------|:--------|
| alpha_em^{-1}(M_Z) | 127.951 | b5_gauge_convergence, feynman_predictions_compute, rge33a_reanalysis, s33a_rge_gate, s33a_rge_gate_corrected, s41_mkk_rge |
| alpha_em^{-1}(M_Z) | **127.9** | s31Aa_nck_tau021, s31Ba_nck_tau021 |
| alpha_em^{-1}(M_Z) | **127.955** | s42_constants_snapshot, s43_mkk_posterior, s44_bayesian_f |
| sin^2(theta_W) | 0.23121 | b5_gauge_convergence, feynman_actual_predictions, feynman_predictions_compute, h5_full_veff, h5_standalone_verify |
| sin^2(theta_W) | **0.23122** | rge33a_reanalysis, s30b_rge_running, s31Aa_nck_tau021, s31Ba_nck_tau021, s33a_rge_gate, s33a_rge_gate_corrected, s41_mkk_rge, s42_constants_snapshot |
| sin^2(theta_W) | 0.2312 | gauge_coupling_derivation, h4_entropy_counting (3-digit rounded) |
| sin^2(theta_W) | 0.231 | s31Ce_gcm_moduli (2-digit rounded) |

**INCONSISTENCY FLAG**:
- **alpha_em^{-1}**: Three values (127.9, 127.951, 127.955). The 127.9 in S31 scripts is a 2-digit rounding. The shift from 127.951 to 127.955 reflects PDG 2022->2024 update. S42+ uses 127.955.
- **sin^2(theta_W)**: 0.23121 vs 0.23122. The difference is within PDG uncertainty (0.00003). The S42+ value of 0.23122 matches the latest PDG MSbar value.

**RISK LEVEL**: LOW. The differences are at the last significant digit and within experimental uncertainty.

---

## 8. Cosmological Constant (Observed)

| Script | Variable | Value (GeV^4) | Notes |
|:-------|:---------|:--------------|:------|
| s28b_lambda_eff.py | RHO_LAMBDA_OBS | 5.35e-47 | "Planck 2018" |
| s36_cc_arithmetic.py | rho_obs_MP4 | 2.888e-122 M_P^4 | Planck units |
| s43_qtheory_selftune.py | rho_obs | 2.9e-47 | Rounded |
| s43_twofluid_wz_v2.py | rho_Lambda_obs | 2.9e-47 | Rounded |
| s43_gge_dm_abundance.py | rho_Lambda_obs | Computed | From Omega_Lambda * rho_crit |
| s44_cc_gap_audit.py | rho_Lambda_obs | Computed | From Omega_Lambda * rho_crit |
| s44_jacobson_spec.py | rho_Lambda_obs | 2.888e-47 | |
| s44_sakharov_gn.py | rho_Lambda_obs | 2.888e-47 | "Planck 2018" |
| s44_holographic_spec.py | rho_obs | 2.888e-47 | |
| s44_cutoff_f.py | rho_obs | 2.70e-47 | **Different** |
| s44_eih_grav.py | rho_obs | **3.8e-47** | **OUTLIER** |
| s44_tracelog_cc.py | rho_obs_GeV4 | **2.3e-47** | **Different** |
| s44_dm_de_ratio.py | rho_obs_GeV4 | 2.9e-47 | |
| s43_carlip_cc.py | Comment | 2.888e-47 | |

**INCONSISTENCY FLAG**: Four different values for the observed dark energy density:
- **5.35e-47** (s28b): This is Lambda/(8piG), which equals rho_Lambda. May use older Planck parameters
- **2.888e-47** (S44 Sakharov/Jacobson/holographic): Standard value
- **2.70e-47** (s44_cutoff_f): 7% lower than 2.888e-47
- **3.8e-47** (s44_eih_grav): 32% higher than 2.888e-47
- **2.3e-47** (s44_tracelog_cc): 20% lower than 2.888e-47
- **2.9e-47** (several S43-S44): Rounded

The 5.35e-47 in s28b is rho_Lambda = Lambda/(8piG) = 3*H_0^2*Omega_Lambda/(8piG). The difference from 2.888e-47 comes from the 2018 vs later Planck parameter values and whether Omega_Lambda = 0.685 or 0.692 is used.

**RISK LEVEL**: MEDIUM. The CC is used for order-of-magnitude comparisons (ratio = rho_spectral/rho_obs), so the ~30% scatter between 2.3e-47 and 3.8e-47 shifts log10 ratios by ~0.2. Not catastrophic for 120-order comparisons but sloppy.

---

## 9. Newton's Constant

| Script | Value | Units |
|:-------|:------|:------|
| s23c_moment_mapping.py | 6.674e-11 | m^3/(kg*s^2) |
| s29c_k_transition.py | 6.674e-11 | m^3/(kg*s^2) |
| s43_carlip_cc.py | 6.674e-11 | m^3/(kg*s^2) |

**Consistent** across all scripts that use SI units. Most scripts work in natural units where G = 1/(8pi M_Pl_red^2).

**RISK LEVEL**: LOW.

---

## 10. tau_fold Value

| Script | Value | Precision |
|:-------|:------|:----------|
| Most S36-S44 scripts | 0.190 | 3 digits |
| s36_bdi_winding.py | 0.190158 | 6 digits |
| s39_schwinger_proof.py | 0.19015818 | 8 digits |
| s39_schwinger_geometric.py | 0.19016 | 5 digits |

**Consistent** to the precision used. All scripts agree on tau_fold = 0.190 to 3 significant figures.

**RISK LEVEL**: LOW.

---

## 11. Modulus Mass m_tau

| Script | Value | Source |
|:-------|:------|:-------|
| s31Cg_selfconsistent_cranking.py | **5.0** | Baptista Paper 15 eq 3.79 | **SUPERSEDED** |
| s42_fabric_dispersion.py | 2.062 | Computed (fabric dispersion) |
| s42+ scripts | 2.062 | Loaded from npz |
| s43_impedance_mismatch.py | 2.06238706 | Full precision from C-FABRIC-42 |

The S31 value m_tau = 5.0 was from the Baptista kinetic energy coefficient. The S42 value 2.062 is from the computed fabric dispersion relation. These may be different quantities (kinetic coefficient vs effective mass), but if any script after S42 uses m_tau = 5.0, it would be stale.

**RISK LEVEL**: LOW. Only one pre-S42 script uses the old value.

---

## 12. S_inst (Instanton Action)

All scripts consistently use **S_inst = 0.069** (dense instanton gas, from S37). Confirmed by S43 audit to be 0.0686.

**RISK LEVEL**: LOW. Fully consistent.

---

## Inconsistencies Found

1. **E_cond: 0.115 vs 0.137 vs 0.156** — THREE values for the same quantity used in active scripts. Most critical: S42 fabric scripts use 0.115 while S42-S44 GGE/pair scripts use 0.137. The s43_schwinger_factor36.py explicitly notes "used incorrectly in S42".

2. **Planck mass mislabeling** — s41_mkk_rge.py and s43_oneloop_liv.py have comments that could be read as identifying 1.22e19 as the reduced Planck mass (it is the full Planck mass).

3. **rho_obs scatter** — The observed CC density varies from 2.3e-47 to 5.35e-47 GeV^4 across scripts. The s44_eih_grav.py value of 3.8e-47 is an outlier.

4. **M_KK in s43_offj_jsymm.py** — Uses 1e16 instead of the post-S42 authoritative 7.43e16 GeV.

5. **alpha_em^{-1} version drift** — 127.951 (PDG 2022) vs 127.955 (PDG 2024) used in different scripts.

6. **Delta_0 = 0.128 in s43_mod_reheating.py** — Cited as "BCS gap, S35" but no other script uses this value. Possible transcription error.

---

## Summary

- **Scripts searched**: 463
- **Constants checked**: 12 categories
- **Inconsistencies found**: 6
- **Highest risk**: **E_cond values (0.115 / 0.137 / 0.156)** — Three different values for the BCS condensation energy used interchangeably across active S42-S44 scripts. This directly affects E_exc = 443 * |E_cond| (the post-transit excitation energy), which feeds into dark matter abundance, cosmological constant, and Friedmann equation computations. The correct value depends on which ED computation is considered authoritative: S35 multi-sector (0.115), S36 8-mode (0.137), or gap-equation/GL (0.156).
