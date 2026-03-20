# Session 26: Multi-Mode BCS

- Script: `s26_multimode_bcs.py`. Data: `.npz` (100.7 KB). Plot: `.png`

## Key Numbers
- mu=0: M_max=0.077-0.154 (BCS-1 confirmed)
- mu=lmin: M_max=6.3-9.7, |Delta|=0.17-0.28, F_cond<0
- mu_critical = 0.875-0.925 * lambda_min
- 39 non-trivial solutions across (tau, mu) space

## [V,J] != 0 -- PERMANENT structural result
- ||[V,J]||/||V|| = 0.14-0.30. Kosmann coupling breaks J symmetry.
- V(same-sign)/V(opp-sign) = 68-500. Delta(+lmin)=0.24, Delta(-lmin)=0.004.

## Failures
- No tau lock: F_cond local MAX near tau=0.20 (pushes AWAY from tau=0.15)
- Below confinement: g*Delta^2=0.008-0.010 (needs >0.109 for bound state, >50 for cosmo lifetime)
- Delta^4 coeff b=+0.41: second-order, not first-order

## Verdict: CONDITIONAL PASS WITH STRUCTURAL FAILURE
BCS works at finite mu but fails to lock tau, fails confinement, second-order transition.
