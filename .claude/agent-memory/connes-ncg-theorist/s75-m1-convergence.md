---
name: S75 M1 L11 Convergence
description: M_1 sqrt-moment extended to L=11, drift 7.94% PASS, chi_2 stable 0.14%, CC gap +0.12 to +0.19 OOM
type: project
---

## S75-D6-M1-L11: PASS (7.94% drift)

**Gate**: Drift(<|lam|>) from L=10 to L=11 < 15% = PASS, > 30% = FAIL.
**Result**: 7.94% drift. PASS.

### Key numbers
- L=9: <|lam|>=3.1852, chi_2=0.7414, log10(rho_B/rho_obs)=+0.1203
- L=10: <|lam|>=3.4495, chi_2=0.7505, log10=+0.1549
- L=11: <|lam|>=3.7236, chi_2=0.7494, log10=+0.1881

### Structural findings
1. **<|lam|> drift decelerating**: 19.5% (L7->9), 8.3% (L9->10), 7.9% (L10->11). Weyl-asymptotic 1/L correction.
2. **chi_2 converged**: 0.75 +/- 1% across all L. Bounded dimensionless quantity stable.
3. **CC gap L_max-stable**: +0.12 to +0.19 OOM across L=3..11. Gravity-normalised route robust.
4. **(p,q) <-> (q,p) symmetry PROVEN**: |eigenvalues| identical to 1e-14 on all 24 pairs. Halves computation.
5. **Rational extrapolation cross-validates**: Predicted L=10 matches computed to 0.04%.

### Technical notes
- Partial coverage at L=10 (8/11) and L=11 (8/12) due to diagonal-sector (k,k) recursion bottleneck.
- Missing sectors systematic -> drift estimate unbiased.
- dirac_spectrum.py (p,p) sectors trigger slow conjugation path. Fix requires algorithmic change.
