## W6-5 Results: MULTI-T-JACOBSON-44

##### 1. Gate Verdict

**MULTI-T-JACOBSON-44 = INFO** (8-fluid EOS computed; structural results on multi-temperature thermodynamics)

##### 2. Key Numbers

| Quantity | Value | Unit | Note |
|:---------|:------|:-----|:-----|
| E_GGE | 1.688 | M_KK | Total GGE energy (verified) |
| T_B2 / T_B1 / T_B3 | 0.668 / 0.435 / 0.178 | M_KK | Branch temperatures |
| T(B2,B1) | -0.066 | M_KK | NEGATIVE cross-temperature |
| T(B2,B3) / T(B1,B3) | +0.065 / +0.096 | M_KK | Positive cross-temperatures |
| w_eff (GGE grand potential) | 0.132 | -- | From single-mode Omega_k |
| w_eff (Juttner) | 0.334 | -- | Relativistic kinetic theory |
| w_eff (W5-1, T_k/2E_k) | 0.387 | -- | Prior estimate |
| w_4D | 0 | -- | CDM by construction (T^{0i}=0) |
| C_off/C_diag | 5.40 | -- | Off-diagonal heat capacity dominates |
| Negative C eigenvalues | 3/8 | -- | Thermodynamic instability |
| Euler deficit | 6.8% | -- | sum T_k S_k / E_GGE = 0.932 |
| T_cross eigenvalues | (0.133, 0.459, 0.688) | M_KK | All positive |
| Pi/T_trace | 0.308 | -- | Internal anisotropic stress |

##### 3. Method

1. **Per-mode decomposition.** rho_k = 2 E_k n_k, S_k = -n_k ln n_k - (1-n_k)ln(1-n_k), F_k = rho_k - T_k S_k for all 8 modes. Verified E_total = E_GGE = 1.688 M_KK.

2. **Three EOS prescriptions.** (a) Juttner: w_eff = 0.334. (b) GGE grand potential: w_eff = 0.132. (c) W5-1 (T_k/2E_k): w_eff = 0.387. The spread (0.13--0.39) reflects non-equilibrium nature of GGE.

3. **Cross-temperature analysis.** G_kl susceptibility matrix has off-diagonal elements >> n_k(1-n_k). Intra-B2 correlations dominate (G(B2[0],B2[1]) = 0.80). Cross-correlation energy E_cross = 18.06 M_KK exceeds E_GGE by 10.7x.

4. **Branch cross-temperature matrix.** 3x3 matrix with eigenvalues (0.133, 0.459, 0.688) -- all positive despite T(B2,B1) < 0. Internal anisotropic stress 31%.

5. **Heat capacity.** 3/8 eigenvalues negative: (-4.51, -1.60, -0.68). GGE is thermodynamically unstable in 3 collective directions, stabilized only by integrability.

6. **Euler relation.** sum T_k S_k = 1.573 vs E_GGE = 1.688. Deficit = |E_cond| = 0.115 M_KK exactly. T_therm * S_GGE = E_GGE (Gibbs Euler holds).

7. **8-fluid Friedmann.** w_eff(a) decreases from 0.132 to 0.072 over 4 decades. B2 drops 89%->46%, B3 grows 1.3%->22%. All approach w=0 asymptotically.

##### 4. Cross-checks

- E_GGE = 1.688189 matches stored value exactly.
- T_therm * S_GGE = E_GGE to machine epsilon (Gibbs Euler).
- w_eff(a -> inf) -> 0 consistent with CDM-CONSTRUCT-43.
- Branch T_cross matrix positive definite despite negative T(B2,B1).

##### 5. Physical Interpretation

The multi-temperature Jacobson first law delta Q = sum_k T_k dS_k describes heat flow through a Rindler horizon sourced by a GGE. The 8 modes define 8 separately conserved cosmological fluids (integrability-protected). T(B2,B1) = -0.066 < 0 encodes B2-B1 anti-correlation -- a competing-order effect from shared BCS spectral weight, not time-crystalline.

Critical distinction: w_internal (0.13--0.39) vs w_4D = 0 (dust by CDM-CONSTRUCT-43). Multi-temperature structure describes INTERNAL thermodynamics (second sound, heat capacity, perturbation response) but NOT the 4D Friedmann equation.

Three negative C eigenvalues = GGE thermodynamically unstable in 3 collective directions, stabilized by 8 Richardson-Gaudin conserved charges. The Euler deficit sum T_k S_k / E_GGE = 0.932 with gap = |E_cond| is a new structural identity linking GGE non-thermality to BCS condensation energy.

##### 6. Data Files

- `tier0-computation/s44_multi_t_jacobson.py` (script)
- `tier0-computation/s44_multi_t_jacobson.npz` (39 KB)
- `tier0-computation/s44_multi_t_jacobson.png` (283 KB)

##### 7. Assessment

Three structural results: (1) w_eff is prescription-dependent (0.13--0.39), physical w_4D = 0 by CDM-CONSTRUCT-43 independently. (2) Euler deficit = condensation energy (6.8%), new identity. (3) 3/8 negative heat capacity eigenvalues, stabilized by integrability. Negative T(B2,B1) does not destabilize the branch matrix (all eigenvalues positive). 8-fluid Friedmann evolution: all fluids converge to dust asymptotically, CDM approximation excellent at all cosmological epochs.
