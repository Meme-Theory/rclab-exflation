---
name: S83 W2-G13 JENSEN-FLOW-TRAJECTORY
description: Substrate-native Mukhanov z(tau) derivation; closed-form PASS but numerical ratio FAIL (0.0263); unit-consistency correction required over W1-G4
type: project
---

## S83 W2-G13: JENSEN-FLOW-TRAJECTORY (substrate-native z(tau))

**Verdict**: FAIL (structural PASS, numerical FAIL).
**4-tuple**: `(ratio=0.026257_substrate-derivable=True_F_traj_z=1.3569, scheme=zeta+Zubarev+SDW-jointly, convention=substrate-a2-Jensen-flow, L_max=5)`
**Closure SHA**: `c81b6da256e77e6ea8c96ad02255873e85a263897061ec659ef63840dd254ea5`

### Why FAIL (two-axis verdict):
- Axis 1 (structural): substrate-derivable = True. z(tau) admits closed symbolic form `z = (2 Lambda^2 a_2 a_fold f_2 / pi^2) * exp(N) * |V'(tau)|/sqrt(Z_fold V(tau)^2)`. All symbols canonical constants + dynamical tau. No inflaton imported.
- Axis 2 (numerical): z_sub(N_pivot=64.08, zeta) = 8.99e43 GeV vs z_canonical(Planck A_s) = 3.42e45 GeV. Ratio = 0.0263, below INFO floor 0.1. Shortfall decomposition: M_Pl_eff/M_Pl_red = 0.51 (0.29 OOM) + sqrt(eps_H_sub/eps_H_can) = 0.051 (1.29 OOM); total 1.58 OOM. **Dominant driver: eps_H_sub = 380x smaller than eps_H_canonical.**

### Unit-consistency correction (critical)
W1-G4 eps_H derivation uses `M_Pl_eff^2/Z_fold * (V'/V)^2` treating M_Pl_eff^2 in GeV^2 and Z_fold as dimensionless — this is dimensionally inconsistent. Produces tau runaway tau ~ -4e28 after 64 e-folds (observed in W1-G4 .npz data).

Correct reduction: Z_fold_phys [GeV^2] = Z_fold_dimless * M_KK^2. Then:
- `(M_Pl^2/Z_phys)_dimless = (f_2/pi^2) * a_2 / Z_fold_dimless`
- For zeta: `(1/pi^2) * 2776 / 74730 = 3.764e-3` (physical slow-roll rate).
- `dtau/dN_fold = -3.76e-3 * 0.234 = -8.82e-4` (reasonable).

W1-G4 F_traj=1.5 INFO-verdict preserved by ratio cancellation (max_R/min_R kills absolute scale). Flag for W1-G4 absolute-tau re-audit in S84.

### Regulator spread F_traj_z = 1.357
Narrower than W1-G4's F_traj_epsH = 1.5 because z combines M_Pl_eff (sqrt(f_2)) with sqrt(eps_H) (sqrt(f_2)) — tau-trajectory back-reaction partially compensates regulator differences.

### Cross-checks
- H_sub^zeta = 1.27e18 GeV, H_obs = 1.46e14 GeV; ratio +3.94 OOM (substrate-native H at Jensen scale, not Planck A_s scale).
- A_s_substrate / A_s_Planck = +11.04 OOM (restates TD-branch overproduction).
- tau drift -0.049 over 64 efolds (slow-roll reasonable, not singular).

### Connection to prior findings
- Restates S77 9.5-OOM A_s gap (backreaction-reduced to ~7.35 OOM per S78 W1-C).
- Consistent with S82 W1-1 DIVERGED (branch-conditional H_tilde).
- z(tau) structural PASS is the POSITIVE half of the result — framework does NOT require inflaton field theory, only spectral action + Jensen axis.

### Carry-forward (S84)
- CF-G13-A: Source of eps_H shortfall: steep S_fold curvature OR observational eps_H is not reachable by single-field substrate.
- CF-G13-B: Locate N_match at which z_sub = z_canon (candidate alternate pivot epoch).
- CF-G13-C: Higher-order Jensen potential expansion beyond quadratic.
- CF-G13-D: W1-G4 absolute-tau re-audit with unit-consistent KG.
