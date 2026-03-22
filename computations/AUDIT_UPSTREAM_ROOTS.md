# Upstream Root Audit — Top 9 Most-Cited Data Files

**Auditor:** Claude Opus 4.6 (1M context)
**Date:** 2026-03-15
**Scope:** The 9 .npz files cited most frequently by downstream scripts

---

## 1. s42_gradient_stiffness.npz (18 downstream)

### Producer: s42_gradient_stiffness.py
- **Saved values**: `tau_grid`, `Z_spectral`, `dS_dtau`, `d2S_dtau2`, `S_total`, `G_DeWitt`, `Z_fold`, `dS_fold`, `d2S_fold`, `S_fold`, `c_fabric`, `M_ATDHFB`, `Vol_SU3_Haar`, `tau_fold_used`, `verdict`, per-sector Z values
- **Upstream inputs**: `s36_sfull_tau_stabilization.npz` (for Approach C cross-check), `tier1_dirac_spectrum.py` (imported functions)
- **Constants check**: FLAG
  - `M_ATDHFB = 1.695` hardcoded at line 1016. This matches `s40_collective_inertia.npz` value of `M_ATDHFB_TOTAL = 1.6947`. Acceptable rounding (0.2% error).
  - `Vol_SU3_Haar = 8 * sqrt(3) * pi^4 = 1349.74`. This formula comes from SU(n) Weyl integration: `sqrt(n) * (2*pi)^{(n^2-1)/2} / prod_{k=1}^{n-1} k!` for n=3 giving `sqrt(3) * (2*pi)^4 / 2`. This is the correct SU(3) Haar volume for coordinate-radius normalization. **However**, this DISAGREES with `s42_constants_snapshot.py` which uses `sqrt(3) * (4*pi^2)^3 / 12 = 8880.93` — see RED FLAG under file #2.
- **Units check**: PASS — Z_spectral is dimensionless (sum of (d lambda/d tau)^2 over eigenvalues), dS/dtau is dimensionless, all in spectral-action internal units.
- **Extreme values**: Z_fold ~ 74,731, d2S_fold ~ 317,863. These are large but justified: they represent sums over ~1000 KK eigenvalues with O(1) contributions each, times dim^2 Peter-Weyl multiplicities up to 225.
- **Provenance chain**: `tier1_dirac_spectrum.py` (base library) + `s36_sfull_tau_stabilization.npz` (cross-check only) -> **this** -> 18 downstream scripts
- **Verdict**: SUSPICIOUS
- **Risk if wrong**: Z_fold controls tau modulus mass (m_tau^2 = V''/Z), fabric sound speed (c_fabric = sqrt(Z/M)), and all stability analyses. If Z is wrong by a factor of N, m_tau changes by sqrt(N) and all stability verdicts could flip.

---

## 2. s42_constants_snapshot.npz (12 downstream)

### Producer: s42_constants_snapshot.py
- **Saved values**: `tau_values`, `tau_fold`, `g_U1/g_SU2/g_C2` arrays and fold values, `g0_diag`, spectral zeta sums (`a0_fold`, `a2_fold`, `a4_fold`), `sin2_thetaW_fold`, `alpha2_MKK_inv`, `alpha_EM_MKK_inv_kerner`, `M_KK_kerner`, `M_KK_from_GN`, `OOM_diff`, running rates, `rho_Lambda_spectral`, `CC_ratio`, gate verdict
- **Upstream inputs**: `s41_constants_vs_tau.npz` (tau_values, tau_fold, a0/a2/a4 zeta sums, clock_coeff), `s42_tau_dyn_reopening.npz` (shortfall_best), `tier1_dirac_spectrum.py` (jensen_metric)
- **Constants check**: RED FLAG
  - **SU(3) Volume**: Uses `Vol_SU3_unit = sqrt(3) * (4*pi^2)^3 / 12 = 8880.93` at line 622. This is the formula for `sqrt(3) * 64*pi^6 / 12`, which is NOT any standard formula for Vol(SU(3)). The CORRECT Haar volume is `8 * sqrt(3) * pi^4 = 1349.74` (as used in s42_gradient_stiffness.py, derived from the Weyl integration formula). The Marinov 1980 value cited in comments at line 148 is `sqrt(3)*(2*pi)^5/60 = 282.69`, yet another different number. The code at line 622 uses NEITHER of these. The factor-of-6.6 error in Vol_SU3 propagates to Vol_code = g0^4 * Vol_SU3_unit, which then enters M_* = (M_Pl^2 * M_KK^8 / Vol_code)^{1/10}. Since M_* enters as Vol_code^{-1/10}, the error in M_* from this alone is ~(6.6)^{1/10} ~ 1.21 (21% error). This is within 1 OOM but non-negligible.
  - PDG constants: `ALPHA_EM_MZ_INV = 127.955` (correct, PDG 2024), `M_PL_REDUCED = 2.435e18` GeV (correct), `M_Z = 91.1876` GeV (correct), `G_N_OBS = 6.67430e-11` (correct, CODATA 2018).
  - `alpha_GUT = 1/40`: approximate but standard.
  - `b2_SM = 19/6`: This is stated to be the SU(2) 1-loop beta coefficient. The standard SM value is `b_2 = 19/6` in the convention where `d(1/alpha_i)/d(ln mu) = b_i/(2*pi)`. PASS.
  - `b1_SM = -41/10`: Standard SM U(1) coefficient. PASS.
- **Units check**: FLAG — The script extensively discusses dimensional analysis (lines 163-543) with many self-corrections. The final Kerner formula `alpha_a = M_KK^2 / (M_Pl^2 * g_code)` is dimensionally consistent. However, the intermediate derivation contains multiple crossed-out/superseded attempts, making it hard to verify the final answer is the intended one. The self-consistency check works out (alpha_1/alpha_2 ratio matches e^{-4*tau}), which is encouraging.
- **Extreme values**: `M_KK_kerner ~ 5e17 GeV`, `M_KK_from_GN ~ 7.4e16 GeV`. Both physically reasonable (GUT-Planck scale). `CC_ratio ~ 10^{115}`: this is the standard cosmological constant problem, correctly reproduced.
- **Provenance chain**: `s41_constants_vs_tau.npz` + `s42_tau_dyn_reopening.npz` -> **this** -> 12 downstream (including s42_gge_energy, s42_fabric_wz, etc.)
- **Verdict**: RED FLAG
- **Risk if wrong**: M_KK values are used to set ALL physical energy scales. sin2_thetaW_fold enters Weinberg angle predictions. The SU(3) volume error propagates to M_* and V_phys, affecting gravity/gauge self-consistency. Any script converting M_KK-unit quantities to GeV inherits these values.

---

## 3. s36_sfull_tau_stabilization.npz (11 downstream)

### Producer: s36_sfull_tau_stabilization.py
- **Saved values**: `tau_combined` (16 points), `S_full`, `verdict`, `S_fold`, `dS_fold`, `d2S_fold`, `n_minima`, `is_monotonic`, `min_dS_dtau`, `tau_min_dS`, per-level S contributions, per-sector actions, eigenvalues at extra tau points
- **Upstream inputs**: `s27_multisector_bcs.npz` (eigenvalues at 9 tau values for 9 sectors)
- **Constants check**: PASS
  - `dim_pq(p,q) = (p+1)*(q+1)*(p+q+2)//2` — standard SU(3) dimension formula, correct.
  - `mult_pq(p,q) = dim_pq(p,q)^2` — correct Peter-Weyl multiplicity.
  - Sector list covers KK levels 0-3 (11 sectors): correct.
  - `(1,2)` spectrum set equal to `(2,1)` by conjugation: correct (complex conjugate reps have same |eigenvalues|).
- **Units check**: PASS — all quantities are dimensionless spectral sums in M_KK units.
- **Extreme values**: `S_full(0.190) ~ 250,000`. Reasonable for ~1000 eigenvalues with multiplicities up to 225.
- **Provenance chain**: `s27_multisector_bcs.npz` -> **this** -> 11 downstream (s42_gradient_stiffness, s42_fabric_dispersion, s42_fabric_wz, etc.)
- **Verdict**: CLEAN
- **Risk if wrong**: S_full(tau) and its derivatives control the spectral action potential V_eff(tau), all stabilization analyses, and gradient stiffness cross-checks. The monotonicity result (FAIL verdict) is the basis for closing spectral action stabilization. If the eigenvalues from s27 are wrong, the entire stabilization analysis is compromised.

---

## 4. s42_fabric_dispersion.npz (7 downstream)

### Producer: s42_fabric_dispersion.py
- **Saved values**: verdict, `c_fabric_value` (=1.0), `m_tau`, `m_tau_sq`, quasiparticle energies (`E_fold`, `eps_fold`, `Delta_fold`), effective masses (`M_star_B2/B1/B3/avg`), DM quantities (`v_th_B2`, `v_th_avg`, `lambda_C_Mpc_A/C`, `sigma_over_m`, profile/DM type predictions), dispersion curve data, input parameters
- **Upstream inputs**: `s42_gradient_stiffness.npz` (Z, dS, d2S, S, c_fabric, M_ATDHFB, tau_fold), `s36_sfull_tau_stabilization.npz` (S_full, tau_combined), `s40_collective_inertia.npz` (M_ATDHFB, eps_fold, Delta_fold, E_fold, u/v_fold, omega frequencies)
- **Constants check**: FLAG
  - `E_exc_total = 50.9` and `n_pairs = 59.8` hardcoded at lines 280-281. These come from S38 but use E_cond = 0.115 (see E_cond inconsistency under file #6). If E_cond = 0.137 (from s37), E_exc = 60.7, not 50.9.
  - `f_B2 = 0.891` hardcoded at line 310. From B2-DECAY-40 (retained fraction after dephasing). Reasonable.
  - `hbar_c = 1.97e-16 m*GeV` at line 495: correct.
  - `hbar_c_cm = 1.97e-14 cm*GeV` at line 589: correct.
  - `z_formation = 1e22` at line 390: extremely rough, acknowledged in script.
- **Units check**: FLAG — `m_tau^2 = V_eff''/Z = d2S_fold / Z_fold`. Both are dimensionless, so m_tau is dimensionless in M_KK units. But V_eff'' is identified with d2S/dtau2 (spectral action second derivative), and Z is the gradient stiffness. These have DIFFERENT normalizations — V_eff'' has a factor of Vol_K * Lambda^{d-2} that Z also has, so the ratio is indeed dimensionless. PASS on dimensional grounds, but the interpretation assumes V_eff = S_full, which is a choice.
- **Extreme values**: `sigma_over_m ~ 10^{-50} cm^2/g`: extreme but physical (gravitational-strength interactions between KK-scale particles).
- **Provenance chain**: `s42_gradient_stiffness` + `s36_sfull` + `s40_collective_inertia` -> **this** -> 7 downstream
- **Verdict**: SUSPICIOUS (inherits Z from gradient_stiffness, E_cond inconsistency)
- **Risk if wrong**: DM prediction (CDM-like vs WDM), tau modulus mass, Compton wavelength, and self-interaction cross-section. If m_tau is wrong (from Z error), stability verdicts could change.

---

## 5. s37_pair_susceptibility.npz (7 downstream)

### Producer: s37_pair_susceptibility.py
- **Saved values**: Full BCS spectrum (`E_all`, `E_gs`, `E_cond`, `omega_n`), pair creation matrix elements (`B_n_plus`, `B_n_minus`), mode-resolved amplitudes, number-sector info, chi_pair at multiple eta values, pair gap estimates (`Delta_pair`, `Delta_OES`), pole/continuum ratio, E_vac, sum rules
- **Upstream inputs**: `s36_multisector_ed.npz` (V_8x8, E_8, branch_labels, E_cond), `s35a_vh_impedance_arbiter.npz` (rho_at_physical = 14.023)
- **Constants check**: PASS
  - `n_modes = 8`, `n_states = 256 = 2^8`: correct for 8-mode pair Fock space.
  - `mu = 0.0`: forced by S34 (PH symmetry).
  - `rho = [14.023]*4 + [1.0]*4`: B2 modes at van Hove DOS, B1/B3 at smooth DOS. Consistent with arbiter.
  - Pair Hamiltonian construction (lines 88-108): diagonal is `2*xi[m]` per occupied pair, off-diagonal is `-V_8x8[n,m] * sqrt(rho[n]*rho[m])`. This is the standard DOS-weighted reduced BCS Hamiltonian. PASS.
- **Units check**: PASS — all in dimensionless M_KK units.
- **Extreme values**: None problematic. E_gs ~ -0.137, typical excitation energies O(0.1-1.0).
- **Provenance chain**: `s36_multisector_ed` + `s35a_vh_impedance_arbiter` -> **this** -> 7 downstream (s38_cc_instanton, s39_richardson_gaudin, s42_gge_energy, etc.)
- **Verdict**: CLEAN
- **Risk if wrong**: E_cond, pair gap, and pole structure feed into all instanton, GGE, and BBN analyses. E_cond = -0.137 (stored as `config_4_E_cond`) is the single most important BCS number. Cross-checked against full 256-state ED to machine epsilon (line 118: `assert abs(E_gs - E_cond_stored) < 1e-10`).

---

## 6. s42_hauser_feshbach.npz (6 downstream)

### Producer: s42_hauser_feshbach.py
- **Saved values**: Input parameters (T_acoustic, T_Gibbs, T_compound, E_exc, Delta_pair, omega_att), mass spectrum, transmission coefficients, sector branching ratios, doorway parameters (BR_B2/B1/B3, V_rms values, level densities), gate verdict, eta estimates, sensitivity scan
- **Upstream inputs**: `s27_multisector_bcs.npz` (D_K eigenvalues), `s40_acoustic_temperature.npz` (T_acoustic, T_Gibbs, Delta_pair), `s40_nohair_sensitivity.npz` (T_variation, Delta_k, branch_labels), `s40_b2_integrability.npz` (PR_B2, r_B2, V_B2B2, V_B2_B1, V_B2_B3), `s23a_kosmann_singlet.npz` (for doorway overlap)
- **Constants check**: RED FLAG
  - **E_cond = -0.115 hardcoded at line 145**. The s37_pair_susceptibility stores E_cond = -0.137 (from `config_4_E_cond`). This is a 16% discrepancy. The value 0.115 appears to be from an older computation or a different convention. E_exc = 443 * 0.115 = 50.945, whereas 443 * 0.137 = 60.691 — a 19% error. This propagates to T_compound = E_exc/8, eta estimates, and all cascade analyses.
  - `N_pairs = 59.8` at line 146: consistent with S38 sudden quench. PASS.
  - `omega_att = 1.430` at line 214: from S38, the attractor frequency. PASS.
  - `PR_B2 = 3.17` hardcoded at line 79 — should match `s40_b2_integrability.npz`. PASS (referenced as "from memory, confirmed in data").
  - `BR_BCS` at lines 347-350: `B2: 0.855, B1: 0.133, B3: 0.0045`. These are from S38. However, sum = 0.855 + 0.133 + 0.0045 = 0.9925 (not 1.0). The 0.75% deficit is unaccounted but minor.
  - `idx_fold = 3` uses `tau=0.20`, not `0.190`. The fold is at 0.190 but only 0.20 is on the grid. Acknowledged in script but introduces small systematic error in mass table.
- **Units check**: PASS — all internal computations in M_KK units. Boltzmann factors exp(-m/T) dimensionally consistent.
- **Extreme values**: `eta_HF_acoustic ~ 10^{-5}`: reasonable. `DR_acoustic ~ 10^{4.9}` (eigenvalue level): reasonable. `rho_B3 ~ 1008/M_KK`: seems large but consistent with many high-rep eigenvalues.
- **Provenance chain**: `s27_multisector_bcs` + `s40_*` (3 files) + `s23a_kosmann` -> **this** -> 6 downstream
- **Verdict**: RED FLAG (E_cond = 0.115 vs 0.137)
- **Risk if wrong**: E_exc = 50.9 vs 60.7 M_KK (19% error). T_compound = 6.37 vs 7.59 M_KK. All Boltzmann branching ratios change. eta_best shifts by ~1 OOM via the pair-breaking chain. This cascades to s42_gge_energy and all BBN analyses.

---

## 7. s42_gge_energy.npz (6 downstream)

### Producer: s42_gge_energy.py
- **Saved values**: M_KK values (gravity/gauge), framework quantities in M_KK units, physical quantities in GeV (both routes), eta estimates, cascade parameters, HF branching, gate verdict
- **Upstream inputs**: `s42_constants_snapshot.npz` (M_KK values), `s42_hauser_feshbach.npz` (E_exc, Delta_pair, T_acoustic, T_compound, eta, sector BRs, pair_breaking_factor), `s37_pair_susceptibility.npz` (E_cond)
- **Constants check**: FLAG
  - `M_Pl = 1.2209e19 GeV` (line 51): this is the FULL Planck mass, but s42_constants_snapshot uses `M_PL_REDUCED = 2.435e18 GeV`. The script doesn't actually use M_Pl in computation (uses M_KK from upstream), so this is benign but confusing.
  - `G_N = 6.7088e-39 GeV^{-2}` (line 52): correct in natural units.
  - `g_star_RH = 106.75`, `g_star_BBN = 10.75`: standard SM values. PASS.
  - `eta_observed = 6.12e-10`: Planck 2018. PASS.
  - `hbar = 6.582e-25 GeV*s` at line 462: correct.
  - Script reads `E_cond_MKK = abs(float(pair['E_cond']))` from s37 (= 0.137) but also uses `E_exc` from s42_hauser_feshbach (which was computed with E_cond = 0.115). **Inconsistent**: E_cond_MKK = 0.137 from s37, but E_exc_MKK = 50.945 from HF (which used 0.115). The cross-check at lines 100-108 catches this: `443 * 0.115 = 50.945` matches stored E_exc but `443 * 0.137 = 60.691` would not.
  - `n_pairs = 59.8` hardcoded at line 83 (matching HF). PASS.
  - File path issue: loads from `'tier0-computation/s42_constants_snapshot.npz'` (relative path from project root, not from script directory). This means the script must be run from the project root, unlike most other scripts which use `SCRIPT_DIR`. Not a data error but a fragility.
- **Units check**: PASS — conversions from M_KK units to GeV are straightforward multiplications by M_KK. T_RH formula (line 278) dimensionally correct.
- **Extreme values**: `T_RH ~ 10^{16-17} GeV`: physically meaningful (GUT-scale reheating). `t_decay ~ 10^{-40} s`: physically meaningful (inverse GUT-scale mass).
- **Provenance chain**: `s42_constants_snapshot` + `s42_hauser_feshbach` + `s37_pair_susceptibility` -> **this** -> 6 downstream
- **Verdict**: SUSPICIOUS (inherits E_cond inconsistency from HF, plus Vol(SU3) from constants_snapshot)
- **Risk if wrong**: T_RH and eta are the key BBN predictions. T_RH scales as M_KK so any error in M_KK propagates directly. The E_cond inconsistency means E_exc_MKK is internally contradictory (HF used 0.115, s37 has 0.137).

---

## 8. s39_richardson_gaudin.npz (6 downstream)

### Producer: s39_richardson_gaudin.py
- **Saved values**: Gate result, exact energies at tau=0.20, Richardson effective G, tau sweep (9 points: e1, psi_pair, E_8, V_8x8, V_phys, rho, G_eff, all eigenvalues), fold interpolation (e1_fold, psi_fold, de1/dtau, d2e1/dtau2), Bogoliubov coefficients (v_k, u_k, n_k, Delta_k), adiabatic overlaps, metadata
- **Upstream inputs**: `s37_pair_susceptibility.npz` (E_8, V_8x8, rho, branch_labels, E_gs), `s38_otoc_bcs.npz` (evals_BCS for cross-check), `s23a_kosmann_singlet.npz` (eigenvalues and K_a matrices at all tau), `s35a_vh_impedance_arbiter.npz` (rho_at_physical, tau_fold, v_min_physical)
- **Constants check**: PASS
  - `mu = 0.0`: forced (S34). PASS.
  - DOS weighting: `V_phys = V_8x8 * sqrt(outer(rho, rho))`. Standard. PASS.
  - Hamiltonian: `H_1 = diag(2*xi) - V_phys`. Correct N_pair=1 reduced BCS Hamiltonian. PASS.
  - Richardson equation: `1 = G * sum_k 1/(2*eps_k - e)`. Standard. PASS.
  - Gate: `|E_gs(8x8) - E_gs(ED 256)| < 1e-10`. Machine-precision cross-check. PASS.
  - Tau-dependent DOS: `rho_B2(tau) = 1/(pi * max(|v(tau)|, v_min))` from B2 band dispersion. Physically motivated approximation. Acceptable.
- **Units check**: PASS — all dimensionless in M_KK units.
- **Extreme values**: None. All quantities O(0.01-10).
- **Provenance chain**: `s37_pair_susceptibility` + `s38_otoc_bcs` + `s23a_kosmann` + `s35a_vh_impedance_arbiter` -> **this** -> 6 downstream
- **Verdict**: CLEAN
- **Risk if wrong**: Pair wavefunction, Bogoliubov coefficients, and Richardson G_eff feed into transit dynamics and adiabaticity analyses. The machine-precision gate cross-check (< 1e-10) gives high confidence.

---

## 9. s38_cc_instanton.npz (6 downstream)

### Producer: s38_cc_instanton.py
- **Saved values**: GL parameters (a, b, Delta_0, barrier, xi_GL, xi_BCS, L), 0D thermal averages at target temperatures (phi2/D02, phi4/D04, frac_near_0, abs_phi/D0), extended T scan, min phi2/D02, instanton-averaged BdG shift, multi-tau instanton shift, gradient comparison, branch energies at fold, distribution data for plotting
- **Upstream inputs**: `s37_instanton_action.npz` (a_GL, b_GL, xi_BCS, S_inst, B2_bw), `s37_oneloop_sa.npz` (tau_kosmann, E_branches, delta_S_BdG, Delta_sc, E_cond_ED/MF, dS_dtau), `s37_instanton_mc.npz` (MC data for cross-check)
- **Constants check**: PASS
  - `L = 0.030` hardcoded at line 69. This is the B2 pairing window from S37. PASS.
  - `Delta_0 = sqrt(-a_GL/(2*b_GL))`: standard GL minimum. PASS.
  - `barrier_1d = a_GL^2 / (4*b_GL)`: standard GL barrier. PASS.
  - `barrier_0d = L * barrier_1d`: correct 0D reduction. PASS.
  - `xi_GL = 1/sqrt(2*|a_GL|)`: standard GL coherence length. PASS.
  - BdG shift formula (lines 251-262): `delta_S = sum mult_k * [2*xi_k^2*Delta^2 + Delta^4]`. This is the quartic expansion of `sqrt(xi^2 + Delta^2) - |xi|` summed over modes, which is NOT exactly polynomial. The correct BdG quasiparticle energy is `E_k = sqrt(xi_k^2 + Delta^2)`, and `sum |E_k| - sum |xi_k|` is NOT `sum [2*xi^2*Delta^2 + Delta^4]`. The formula at line 254 corresponds to `(xi^2 + Delta^2)^2 - xi^4 = 2*xi^2*Delta^2 + Delta^4`, which is the QUARTIC spectral action `sum lambda^4`, not the LINEAR spectral action `sum |lambda|`. **This conflation of spectral action orders (S_4 vs S_1) may matter for quantitative accuracy** but the qualitative result (ratio > 0.5 at all T) is robust because min(phi2/D02) = 0.831.
  - `FOLD_IDX = 3`: uses tau=0.20 as fold proxy. Same grid-proximity issue as HF.
  - `mult_k = [1, 4, 3]` at line 267: B1(1), B2(4), B3(3). PASS.
- **Units check**: PASS — GL potential is dimensionless, thermal averages are dimensionless ratios.
- **Extreme values**: None. min(phi2/D02) = 0.831, well above 0.011 threshold.
- **Provenance chain**: `s37_instanton_action` + `s37_oneloop_sa` + `s37_instanton_mc` -> **this** -> 6 downstream
- **Verdict**: SUSPICIOUS (BdG shift formula uses quartic spectral action, not linear)
- **Risk if wrong**: The CC-INST-38 gate closure depends on min(phi2/D02) = 0.831 >> 0.011. Even if the BdG shift formula is wrong by a factor of 2-3x, the 76x margin (0.831/0.011) ensures the qualitative conclusion survives. But the NUMERICAL value of the instanton-averaged BdG shift (and its ratio to the static shift) could be quantitatively wrong.

---

## Dependency Graph

```
                    tier1_dirac_spectrum.py (library)
                           |
                    s27_multisector_bcs.npz
                     /         |         \
                    /          |          \
   s36_sfull_tau_stabilization  |   s42_hauser_feshbach
          |            \       |       /        |
          |             \      |      /         |
   s42_gradient_stiffness \    |     /   s42_gge_energy
          |         \      \   |    /          |
          |          \      \  |   /           |
   s42_fabric_dispersion   s42_constants_snapshot
                                |
                           12 downstream

   s23a_kosmann + s35a_arbiter + s36_ed + s37_instanton_* + s38_otoc
          |                |
   s37_pair_susceptibility  |
     /       |       \      |
    /        |        \     |
 s38_cc_instanton  s39_richardson_gaudin  (+ s42_gge_energy)
```

---

## Summary

- **Files audited**: 9
- **Red flags**: 2
  1. **s42_constants_snapshot.py**: SU(3) volume formula `sqrt(3)*(4*pi^2)^3/12 = 8881` disagrees with correct Haar volume `8*sqrt(3)*pi^4 = 1350` used in s42_gradient_stiffness.py and with the Marinov reference cited in the comments (`sqrt(3)*(2pi)^5/60 = 283`). Three different formulas for the same quantity across two scripts.
  2. **s42_hauser_feshbach.py**: `E_cond = -0.115` hardcoded, but s37_pair_susceptibility stores `E_cond = -0.137` (verified to 1e-10 against 256-state ED). This 16% discrepancy propagates to E_exc (19% error), T_compound, and all eta/BBN predictions in the 6 downstream scripts.

- **Suspicious**: 3 (s42_gradient_stiffness: M_ATDHFB hardcoded; s42_fabric_dispersion: inherits both issues; s38_cc_instanton: BdG shift uses quartic vs linear spectral action)

- **Clean**: 4 (s36_sfull_tau_stabilization, s37_pair_susceptibility, s39_richardson_gaudin — all have strong internal cross-checks; s42_gge_energy is structurally sound but inherits upstream issues)

- **Highest-risk chain**: `s42_hauser_feshbach (E_cond=0.115)` -> `s42_gge_energy` -> all BBN/eta predictions. The 19% error in E_exc means T_compound, Boltzmann branching ratios, and eta estimates are quantitatively unreliable. Combined with the SU(3) volume inconsistency in `s42_constants_snapshot` affecting M_KK, the physical-unit predictions (T_RH in GeV, eta) have uncontrolled systematic errors at the ~20-50% level.

### Recommended Actions

1. **Resolve SU(3) volume formula**: Pick ONE correct formula for Vol(SU(3)) and use it consistently. The Weyl integration formula `sqrt(3) * (2*pi)^4 / 2 = 8*sqrt(3)*pi^4` (for Haar measure with coordinate-radius normalization) is the most standard. Document which normalization convention is being used and verify against a reference (e.g., Brocker & tom Dieck, Table VI.5.7).

2. **Fix E_cond in s42_hauser_feshbach.py**: Replace hardcoded `E_cond = -0.115` with the value loaded from s37_pair_susceptibility (`E_cond = -0.137`), or load it dynamically. Rerun all downstream scripts.

3. **Audit BdG shift formula in s38_cc_instanton.py**: Determine whether the correct quantity is `sum (xi^2+Delta^2)^2 - xi^4` (quartic spectral action) or `sum sqrt(xi^2+Delta^2) - |xi|` (linear spectral action). The 76x safety margin likely protects the qualitative conclusion, but the quantitative shift values should be corrected.
