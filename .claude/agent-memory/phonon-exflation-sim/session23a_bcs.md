# Session 23a: BCS Gap Equation -- K-1 DECISIVE CLOSURE

## Scripts/Data
- `s23a_kosmann_singlet.py` / `.npz` -- K_a extraction (antisymmetric formula)
- `s23a_bcs_gap_equation.py` / `s23a_gap_equation.npz` / `.png` / `.txt`

## Formulas
- V_nm = -sum_{a=3..6} |<n|K_a|m>|^2 (V<0 = attractive)
- Gap eq: Delta_n = -sum_m V_nm*Delta_m / (2*sqrt(xi_m^2+Delta_m^2))
- Linearized: M_nm = -V_nm/(2|xi_m|), gate = max eigenvalue > 1

## Critical Structural Findings
- **V(gap,gap) = 0 EXACTLY** at all tau>0 (order 1e-29). Selection rule: V couples BETWEEN levels, not within.
- 2-mode truncation has ZERO pairing; minimum viable basis is 10 modes.

## BCS by mu (tau=0.30)
- mu=0: M_max=0.118 FAIL | mu=+lmin: M_max=11.35 PASS (regulator-dep) | BdG: M_max=0.115 FAIL
- mu=0 correct (Landau): spectral action = trace over ALL eigenvalues, no Fermi surface. mu=lmin not physical.

## Kosmann Implementation (CORRECT formula, Baptista Paper 17 eq 4.1)
- K_a = (1/8) sum_{r,s} [Gamma[s,r,a] - Gamma[r,s,a]] * gamma_r * gamma_s
- Uses ANTISYMMETRIC part. SYMMETRIC part (s22b code) gives identically zero.

## Technical Lessons
- eigh requires finite inputs; add floor: eta = max(eta_frac*lmin, 1e-15)
- tau=0 fully degenerate (16 identical eigenvalues): special handling in basis selection
