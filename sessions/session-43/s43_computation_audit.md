# Computation Chain Audit: Cold Big Bang Timeline (W3-1)

**Auditor**: Dirac-Antimatter-Theorist
**Date**: 2026-03-14
**Scope**: Trace 12 key numbers from `s43_cbb_timeline.npz` / W3-1 back to their source `.npz` files.

## Audit Table

| # | Quantity | Source File | Source Value | Timeline/W3-1 Value | Verdict |
|---|---------|-------------|-------------|---------------------|---------|
| 1 | S_fold | `s36_sfull_tau_stabilization.npz` | 250,360.677 M_KK^4 | 250,361 | **MATCH** (integer rounding) |
| 2a | M_KK (gravity) | `s42_constants_snapshot.npz` | 7.4287e16 GeV | 7.4e16 GeV | **MATCH** |
| 2b | M_KK (gauge) | `s42_constants_snapshot.npz` | 5.0417e17 GeV | (used for rho_Lambda) | **MATCH** |
| 3a | E_exc | `s42_gge_energy.npz` | 50.945 M_KK | 50.9 M_KK | **MATCH** (3 sig fig) |
| 3b | n_pairs | `s42_gge_energy.npz` | 59.8 | 59.8 | **MATCH** (exact) |
| 4 | Z_fold | `s42_gradient_stiffness.npz` | 74,730.764 | 74,731 | **MATCH** (integer rounding) |
| 5 | dS/dtau (fold) | `s42_gradient_stiffness.npz` | 58,672.802 | 58,673 | **MATCH** (integer rounding) |
| 6a | d2S/dtau2 (fold) | `s42_gradient_stiffness.npz` | 317,862.849 | 317,863 | **MATCH** (integer rounding) |
| 6b | d2S/dtau2 (tau=0) | `s43_qfluc_tau0.npz` | 304,638.293 | 304,638 (W3-2) | **MATCH** |
| 6c | d2S (tau=0) cross-check | `s42_gradient_stiffness.npz` | 304,605.338 | -- | **NOTE** (0.011% vs qfluc, from FD step) |
| 7 | M_max | `s36_mmax_authoritative.npz` | 1.673955 | 1.674 | **MATCH** (3 dp rounding) |
| 8 | xi_BCS | `s37_instanton_action.npz` | 0.8083 M_KK^{-1} | 0.808 (W1-5) | **MATCH** |
| 8b | xi_BCS (chiral eta) | `s43_chiral_eta.npz` | 1.118 M_KK^{-1} | (wall profile) | **NOTE** (see below) |
| 9 | lambda_fs | `s43_gge_dm_abundance.npz` | 88.886 Mpc | 89 Mpc | **MATCH** |
| 10 | S_inst | `s37_instanton_action.npz` | 0.06860 | 0.069 | **MATCH** (2 sig fig) |
| 11 | epsilon_H | `s43_lifshitz_class.npz` | 0.01755 | 0.0176 | **MATCH** (3 sig fig) |
| 12a | E_exc (GeV) | `s42_gge_energy.npz` | 3.7845e18 GeV | -- | **MATCH** (E_exc * M_KK exact) |
| 12b | rho_Lambda | `s42_constants_snapshot.npz` | 8.432e73 GeV^4 | -- | **MATCH** ((2/pi^2)*a0*M_KK_kerner^4 exact) |
| 12c | T_RH (GeV) | `s42_gge_energy.npz` | 8.153e16 GeV | 1.098*M_KK | **MATCH** (T_RH/M_KK = 1.0975, rounds to 1.098) |

## Notes on Specific Items

### Item 6: d2S/dtau2 at tau=0

Two independent computations give slightly different values:
- `s42_gradient_stiffness.npz` (fd_step=0.0001): 304,605.3
- `s43_qfluc_tau0.npz`: 304,638.3

Difference = 33, or 0.011%. This is a finite-difference discretization artifact, not a physics error. Both are correct within their numerical precision. W3-2 uses the s43 value (304,638), which is consistent with that file.

### Item 8: xi_BCS = 0.808 vs 1.118

Two different coherence lengths appear in the computation chain:
- **xi_BCS = 0.808 M_KK^{-1}** (from `s37_instanton_action.npz`, `s43_pair_form_factor.npz`): BCS coherence length from the gap equation, v_F / (pi * Delta).
- **xi = 1.118 M_KK^{-1}** (hardcoded in `s43_chiral_eta.py` line 159, also in `s42_fabric_wz_v2.py`): A GL-type estimate using v_B2 / (pi * Delta_B3) = 0.618 / (pi * 0.176).

These are different physical quantities (different velocity and gap in the numerator/denominator). The authoritative BCS coherence length is 0.808. The 1.118 value was used for domain wall profile width in the chiral eta computation; while the qualitative results (all eta = 0, {gamma_9, D_K} = 0) are structurally robust and would not change with a different wall width, the naming `xi_BCS = 1.118` in that file is misleading. Impact on physics: **none** (the chiral eta result is a structural theorem, independent of wall width).

### Item on median_R in cbb_timeline.npz

The field `median_R` in `s43_cbb_timeline.npz` stores the value 6661.55, which is the **mean** (not median) of R_direct from `s43_adiabaticity.npz`. The actual median is 6345.3. Source: `s43_cbb_timeline.py` line 101 reads `mean_R_direct` and stores it in a variable named `median_R_direct`. The W3-1 epoch E1 text correctly reports "median R = 6,345" (from the actual median in the adiabaticity file). The summary line 1589 says "median R = 6662" which is the mean, not the median. This is a **labeling inconsistency** in the .npz and one line of the summary. Impact on physics: negligible (both values confirm 100% non-adiabatic transit; the qualitative conclusion is unchanged).

### Item on xi_KZ naming in cbb_timeline.npz

The field `xi_KZ` in `s43_cbb_timeline.npz` stores 0.808 (= xi_BCS from the pair form factor), while `xi_KZ` in `s43_gge_dm_abundance.npz` stores 0.152 (the Kibble-Zurek domain size). These are different physical quantities with the same field name. The lambda_fs computation in s43_gge_dm_abundance correctly uses xi_KZ = 0.152 for k_KZ = 1/xi_KZ. The cbb_timeline field is not used in any downstream computation within that file. Impact: **none** on computed results.

## Discrepancies Found

| Issue | Type | Magnitude | Impact |
|-------|------|-----------|--------|
| `median_R` field stores mean (6662) not median (6345) | Labeling | 5% | None (qualitative conclusion unchanged) |
| `xi_BCS = 1.118` in chiral_eta vs authoritative 0.808 | Input inconsistency | 38% | None (structural theorem) |
| `xi_KZ` name collision (0.808 vs 0.152) between files | Naming | Different quantities | None (not used downstream) |
| d2S(tau=0): 304,605 vs 304,638 between files | FD precision | 0.011% | None |

## Overall Assessment

**Chain verified.** All 12 audited quantities trace correctly from their source `.npz` files to the W3-1 timeline values. Every number matches to within the stated rounding precision. The four issues identified are labeling/naming inconsistencies, not computational errors. No discrepancy affects any physics conclusion or gate verdict.

The computation chain from S36/S37/S38/S42 source files through S43 synthesis to the Cold Big Bang timeline is internally consistent.
