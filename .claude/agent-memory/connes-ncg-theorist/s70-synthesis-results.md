---
name: S70 NCG synthesis results
description: S70 46-computation session NCG-relevant results: HK convergence, c_s^2=0 proof, 35D Hessian, alpha_s tension, L=7 sign reversal, FI map
type: project
---

## S70 NCG-Critical Results

### Spectral Action Convergence (NON-PERT-SA-70 PASS)
- 5-term HK expansion converges to 0.08% at Lambda=2.048 for exp(-x)
- 3-term fails everywhere (wrong sign)
- SDW from spectral zeta sums: a_0=219,744, a_2=42,862, a_4=9,523, a_6=2,590
- Three functionals (sqrt, exp, zeta) span 53x range at same Lambda: maximal scheme dependence
- Spectral zeta sums = canonical extraction method for finite spectral triples

### Product Geometry c_s^2=0 (Q-SOUND-70 PASS, PERMANENT)
- c_s^2=0 at tree level from product spectral triple factorization
- D_K eigenvalues depend on g_K(x), NOT d_mu g_K(x)
- One-loop correction: 3.36e-4, physically suppressed by exp(-M_KK/H_0)~0
- Converts S68 ISW tracking from assumption to structural NCG prediction
- ISW auto-power: 6.7% FW/Quint difference (CLASS-ISW-70 PASS, Boltzmann via CAMB)

### Jensen Fold = True Minimum (OFF-JENSEN-HESS-70 PERMANENT)
- All 35 volume-preserving eigenvalues positive (BCS: [29.81, 240.13])
- Eigenvalue cluster {1,4,3,6,3,1,4,8,5} matches Ad(U(2)) irrep decomposition
- Softest mode: u(1) breathing mode (eigenvalue 29.81), Jensen overlap 0.478
- BCS uniformly softens by 11-12% across all directions
- Condition number kappa=8.06 (well-conditioned)

### Alpha_s Tension (F0-ALPHA-S-70 FAIL, STRUCTURAL)
- alpha_s=0.118 at f_0=6.33 where m_H=190 GeV
- m_H=125 at f_0=1.33 where alpha_s=0.020
- Anti-correlation from CCM: lambda_CCM=(4/3)*g_3^2*ratio_gilkey shares g_3^2 with alpha_s
- Escape routes: a_6 corrections, off-Jensen, Pati-Salam

### L=7 Sign Reversal (LMAX7-PW-70 PERMANENT)
- All L=7 sectors have omega_min > Lambda=2.048
- Gaussian threshold sum oscillates, not monotone converges
- Aitken extrapolation assumptions break; m_H range widens [127,135] GeV
- Spectral zeta route bypasses oscillation entirely

### Functional Independence Map (CONSISTENCY-FI-MAP-70 PERMANENT)
- alpha_s=0: FUNCTIONAL-INDEPENDENT (Bogoliubov saturation, k_CMB/k_tach~10^{-60})
- f_NL^equil=0.853: FI (c_BLV from fermionic sector)
- n_s: SCHEME-DEPENDENT (d(ln eps_H)/d(alpha)=1.076, Planck window alpha in [0.67,1.10])
- r: SD (sign flip in zeta vs cutoff)

### Convention Resolution (RATIO-GILKEY-70)
- a_4/a_2(zeta)=0.4866 != ratio_gilkey=0.4140 (14.9% mismatch)
- Different objects: zeta value vs pure curvature ratio
- CCM uses ratio_gilkey (Gilkey heat kernel), not spectral zeta ratio
- ratio_gilkey=0.4140 propagates identically through S61-S69 chain

### BCS Shell Exactness (BCS-PROXIMITY-70 PERMANENT)
- Delta_ind=0 exactly: SU(3) singlet selection rule
- BCS shell {(0,1),(1,0),(0,0),(1,1),(0,2),(2,0),(1,2),(2,1)} is self-conjugate
- None of 8 proximity sectors have conjugate partners in BCS shell
- 8/992 truncation EXACT by representation theory

### Other NCG-Relevant Results
- Geodesic distance: d(round,fold)=0.4249, sub-Planckian by 2.35x (DeWitt metric G=5.0)
- WKB inapplicable: Mach 54.73, gamma>1 for 93.4% modes, sudden approximation required
- BCS backreaction: Ricci-only, Weyl invariant (K_BCS/K_bare=2.96, all from Ricci sector)
- Spectral dim d_s=4 at sigma=0.922 M_KK^{-2}: mode-counting, not topological
- Leggett moment: a_4 structural, a_0 numerically dominant (2.907), a_6 subleading (0.031)

**Why:** S70 is the most comprehensive single-session validation of the spectral action at the fold.
**How to apply:** Use SDW values {219744, 42862, 9523, 2590} as canonical. Use ratio_gilkey=0.4140 for CCM matching. Alpha_s tension is structural — do not resolve by f_0 adjustment. L=7 sign reversal motivates spectral zeta threshold computation.
