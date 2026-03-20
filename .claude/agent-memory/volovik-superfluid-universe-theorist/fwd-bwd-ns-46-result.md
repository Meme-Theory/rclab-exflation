---
name: fwd-bwd-ns-46-result
description: S46 FWD-BWD-NS-46 FAIL (244 sigma). Dense d_eff(tau_back) sweep confirms d_eff floor at 3 (K_7 topology). 5th n_s route closed. Planck requires d_eff=0.063.
type: project
---

## FWD-BWD-NS-46 Result (Session 46 W4-4)

### Gate: FAIL (2026-03-15, 244 sigma at closest approach)

Dense sweep of 72 tau_back values in [0.210, 0.600]. d_eff decreases monotonically from 6.52 to 1.89. S45 cross-validated at 5 points (delta ~ 0.07-0.20 from eigenvalue extrapolation differences).

### Key Numbers
- d_eff range: [1.893, 6.520]
- d_eff asymptotic (plateau): ~3.48 (fit) / 3.002 (S45 exact)
- d_eff structural floor: 3 (K_7 sector count, topological)
- d_eff required for Planck n_s = 0.965: 0.063
- n_s (per-mode, best): -0.061 at tau_back = 0.60
- n_s (per-mode, asymptotic): -0.617 at tau_back = 0.50 (S45: -0.682)
- Planck deviation: 244 sigma (best), 377 sigma (asymptotic)
- Exponential decoherence: gamma = 6.37 tau^{-1}, d_0 = 6.81, d_inf = 3.48
- Harmonic turnaround: tau_back = 0.229 (d_eff = 6.48)
- d_eff = 3 crossing at tau_back = 0.490

### Physical Selection Mechanisms Evaluated
1. Harmonic overshoot: tau_back = 0.229, d_eff = 6.48 (too high)
2. GGE beat decoherence: timescales 3-19 tau (far beyond sweep)
3. Backreaction: Q = 27, sets dissipation not turnaround
4. q-theory potential: chi_q = 300,338 (stiff), harmonic est. adequate

### Structural Theorem
d_eff = 3 floor from [iK_7, D_K] = 0 creating 3 independent channels. Direct analog of 3He-B J=0,1,2 gap branches. Planck d_eff = 0.063 requires < 1 sector (impossible). With-Weyl n_s always > 1 (blue). Neither n_s definition reaches Planck.

### n_s Route Closure (5 total)
1. Lifshitz eta (S44): FAIL
2. Bogoliubov KZ-NS-45 (S45): FAIL (370 sigma)
3. FWD-BWD-NS-45 (S45): FAIL (908 sigma)
4. epsilon_H (S44): FAIL by construction
5. FWD-BWD-NS-46 (S46): FAIL (244 sigma)

**Why:** BCS gap approximately constant across KK tower while eigenvalues span 2.5x. Forces |beta_k|^2 ~ (Delta/omega)^4 steep power law. No tau_back selection flattens it. K_7 topology fixes d_eff >= 3.

**How to apply:** Bogoliubov pair creation in KK tower permanently closed for n_s (5 routes). Future n_s must use non-Bogoliubov physics: topological defects, domain-wall correlations, or k-dependent Delta(k).

Files: s46_fwd_bwd_ns.py, s46_fwd_bwd_ns.npz, s46_fwd_bwd_ns.png
