# Sessions 28-29 Computation Results

## Session 28a

### KC-1 Bogoliubov Coefficients -- PASS
- Script: `s28a_bogoliubov_coefficients.py`. Data: `.npz`, `.png`
- B_k = (1/(4*omega_k^2)) * (d(omega_k)/d(tau))^2, 3-point central diff on s19a data
- Max B_k in [0.10, 0.40]: 0.225 (sector (3,3)), gap edge: 0.023 (>0.01 threshold)
- Adiabaticity ratio min ~1.07-1.14; no mode has ratio < 1
- Total injection 6,228-29,643 (mult-weighted), grows monotonically with tau

### L-1 Thermal Spectral Action -- CLOSED
- Script: `s28a_thermal_spectral_action.py`
- F_ferm, F_bos, F_total ALL monotonically increasing at ALL 10 temperatures (T/lmin = 0.1 to 10)
- ALL 9 sectors have F min at tau=0 (boundary). Thermal does NOT break monotonicity wall (W1).

## Session 28b

### L-7 Self-Consistent (tau, T) -- WEAK PASS
- Script: `s28b_self_consistent_tau_T.py`
- Interior minima: tau=0.35/mu=1.50 (F=-43.55), tau=0.35/mu=1.20 (F=-18.56), tau=0.20/mu=1.20 (F=-3.69)
- Global min at BOUNDARY: tau=0.00/mu=1.50 (F=-127.10). BCS has LOCAL interior, NOT global.
- Dominant sectors at interior: (3,0)+(0,3) = 93%.

### E-5 CC from Condensation -- DIAGNOSTIC
- rho_BCS = F_total * M_KK^4. At M_GUT: 113 orders too large.
- BCS inherits standard CC problem. Needed M_KK ~ 10^{-12} GeV (unphysical).

### L-3 Relaxation Times -- PASS
- Script: `s28b_relaxation_times.py`
- (0,0),(1,0),(0,1),(3,0),(0,3): ALWAYS supercritical at mu=lmin
- (2,0),(0,2): RE-ENTRANT [tau=0.069, 0.499]
- (1,1): transition at tau=0.095. (2,1): transition at tau=0.303.
- D_can: ALL sectors always supercritical (torsion enhancement 2-13x).

### L-9 Cubic Invariant -- PASS
- Script: `s28b_cubic_invariant.py`
- (3,0): c=0.0055, (0,3): c=0.0072 (1st-order character)
- (1,0): c=0.00013, (0,1): c=0.00026 (2nd-order)
- 5 cusps in d3F/dtau3.

### S-3 Hessian -- PASS
- 3 genuine minima (both eigenvalues > 0):
  - tau=0.15/mu=1.10: F=-1.03, eigs=(254, 917)
  - tau=0.35/mu=1.50: F=-43.55, eigs=(426, 31996)
  - tau=0.35/mu=1.20: F=-18.56, eigs=(438, 6842)
- 7 saddle points. Global min at boundary.

## Session 29

### 29Aa
- K-29a PASS: T-matrix to tau=0.50. W/Gamma=0.148 (>0.1). Script: `s29a_tmatrix_extension.py`
- G-29a PASS: E_crit/V(0)=1.52 for n_gap=20. Script: `s29a_derived_drive_rate.py`
- G-29b: J_perp=1/3 EXACTLY (Schur orthogonality). Script: `s29a_inter_sector_coupling.py`

### 29Ab
- K-29c PASS: F_BCS < 0. Trapping requires L-9 1st-order. Script: `s29b_free_energy_comparison.py`
- G-29c PASS: t_BCS=1.3e-41s at M_KK=1e16. Script: `s29b_modulus_eom.py`
- K-29d PASS: Gi=0.354-0.361, mean-field reliable. Script: `s29b_gaussian_correction.py`

### 29Ba
- B-29a PASS: F_3sect=-17.22 at (tau=0.35, mu/lmin=1.20). Script: `s29b_3sector_fbcs.py`
- PMNS: theta_13=0.027 (CONDITIONAL), R=0.29-0.63 vs PDG 32.6 (mass hierarchy wrong)

### 29Bb
- B-29d FIRES: 2/4 negative Jensen Hessian eigenvalues
- P-29c FIRES: Bogoliubov BCS gap passes all 3 load-bearing sectors
- P-29e FIRES: Josephson J_perp=1.17 at tau=0.35
- Weinberg: sin^2(theta_W)=0.231 at eps_T2=0.049 (NOT prediction, no minimum)
