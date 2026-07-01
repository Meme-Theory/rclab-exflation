---
name: Spectral-Geometer Key Results
description: Consolidated heat-kernel audit, R-protection theorem, CC-Ratios theorem, and conventions (S45-S82)
type: project
---

# Heat Kernel Validity Tiers (HEAT-KERNEL-AUDIT-45, updated S46)

The 992-level truncated Dirac spectrum has different analytic structure (entire zeta, convergent Taylor, d_s -> 0 as sigma -> 0) from the continuum (meromorphic zeta, asymptotic SD, d_s -> 8). Three tiers:

1. **Level 1 (exact on truncation)**: Spectral action S(Lambda), heat trace K(sigma), spectral zeta moments at any s. Spectral action monotonicity theorem (CUTOFF-SA-37) is here -- unaffected by truncation.
2. **Level 2 (different objects, NOT approximation)**: SD coefficients vs spectral zeta moments are STRUCTURALLY DIFFERENT. The "spectral a_2" = zeta_D(1) = 2776.17 is NOT the SD coefficient a_2^{SD} = 0.728 (factor 3812). zeta_D(s) has pole at s=1 for d=8; on the truncation it converges but is UV-dominated (~Lambda_max^6). M_KK extraction uses zeta_D(1) as the spectral moment correctly; calling it "a_2" is naming, not equality.
3. **Level 3 (artifact)**: Spectral dimension d_s in UV (-> 0 not 8), analytic torsion T (extensive in N, T ~ 10^{20301} unphysical), anything requiring zeta poles. CC routes via d_s and torsion: CLOSED.

Use Weyl counting d_Weyl = 6.81 instead of d_s for dimension. K(0) = 6440 (finite). Taylor converges at 20 terms. Moment ratio A_{2(n+1)}/A_{2n} -> lambda_max^2 = 4.25 (not curvature-related).

# R-Protection Theorem (S76 Workshop G2.1)

For compact simple Lie group G of dim d, rank r: spectral moment ratios R_n = a_0 * a_{2n} / a_n^2 are L_max-protected with sensitivity O(L^{-r}) in Weyl regime. Individual moments a_k are L_max-fragile with O(L^{d+r+k}). Weyl exponents alpha_k = d + r + k cancel exactly: alpha_0 + alpha_{2n} = 2*alpha_n. Holds for ANY compact simple Lie group.

**Application**: R-protection is structural, not SU(3)-specific. Pre-asymptotic at L=3-9 (effective 5.23 vs asymptotic 8 for a_0, S61 d_eff(PW)=5.83). Need L~210 for true Weyl regime.

# Intensive/Extensive Partition (S76)

Spectral observables partition by alpha_net = (d+r) * sum(n_k) + sum(k*n_k):
- **Intensive** (R-protected, alpha_net = 0, functional-independent): n_s, R_n
- **Extensive** (R-fragile, alpha_net != 0, functional-dependent): CC, A_s

CC * f_conv^2 ~ 1/a_0^3 (shared extensive parent). Spectral functional choice = ensemble (temperature t* = 0.088). chi_2 IS the CC prediction under f*.

Eigenvalue truncation gives a_0 >= angular-momentum-truncated a_0 -- f_conv SMALLER. A_s gap 0.12 OOM is a structural lower bound under any truncation including all L_max=3 modes.

# R-Protected-Fold Convention Split (S74 W1-M PASS / W2-O FAIL — STRUCTURAL)

R_protected_fold = a_0 * a_4 / a_2^2 has TWO inequivalent definitions; downstream usage MUST specify scheme:

- **R_protected_fold_partialsum = 1.128655** (S73B, L_max=3 partial-sum ratio, canonical). L_max=7 = 1.140699 (1.067% drift L=3-7; 2.890% L=3-9). Two zeta-sum conventions reconciled: S73B (a_k = 0.5 * zeta_D(k/2)) vs Wodzicki (a_k = zeta_D((d-k)/2)) -- structurally related via relabel. Vol(SU(3)) cancels to machine epsilon.
- **R_protected_fold_gilkey = 0.492288** (Gilkey heat-kernel curvature polynomial, L_max=infty). Closed form at fold:
  ```
  R_gilkey = (1/1000) * (500 - 32 * |Ric|^2/R^2 - 28 * K/R^2)
           = (1/1000) * (500 - 32*0.126169 - 28*0.131246)
           = 0.492288
  ```
  At tau=0 (bi-invariant): exactly 0.4925 = 492.5/1000.

Routes A and C (L_max -> infty zeta extrapolation = 1.152815) agree to 1.06%; both differ from Route B by factor ~2.33. STRUCTURAL: partial-sum ratio vs heat-kernel local-curvature polynomial are different mathematical objects; related via Mellin pole residues only.

# CC-Ratios-Only Theorem (S80, S82 SG validation)

CC96 eq 2.11 via heat-kernel / Mellin-Laplace duality:
```
Tr f(D^2/Lambda^2) ~ sum_k f_k * Lambda^k * a_{d-k}[D^2] / Gamma(k/2)
where f_k = integral_0^infty f(u) * u^{k/2-1} du   (Mellin moment at s=k/2)
```

**Theorem**: weight-balanced SDW ratios a_m/a_n with w(a_n) = d-n = k matched are f-INDEPENDENT under CC96. Cancellation is identity-level (f_k, Lambda^k, Gamma(k/2) factor identically). Unbalanced ratios RETAIN f.

**Substitution chain (balanced pair)**:
1. Definition: R^{(f)}_{m,n} = S_m^{(f)} / S_n^{(f)}
2. Substitute: = [f_k * Lambda^k * a_m / Gamma(k/2)] / [f_k * Lambda^k * a_n / Gamma(k/2)]  (m=n weight => same k)
3. Simplify: f_k, Lambda^k, Gamma(k/2) cancel arithmetically
4. Direction: balanced => f CANCELS

**Subtlety (multiset vs sum)**: Monomial balance requires MULTISET equality of weight labels, NOT sum equality. (a_4)^2 (weights {4,4}) and a_2*a_6 (weights {6,2}) have equal sum (8) but different multisets — ratio of full SA contributions does NOT cancel f. P4-D CN-EM1 sum-form is sufficient ONLY in the binary case.

**S82 SG validation**: Closure SHA `8a5678ba2a411ceebf2952b4b25634fd88acae4bc174d131f021d49ae9464211`. Part C balanced cancellation max dev 2.22e-16 across 3 regulators (e^{-u}, (1+u)^{-2}, e^{-u^{0.7}}). Part D unbalanced rel spread 198.38% (sign flips). Verdict PASS value=0.

**Implication**: S74 W2-O 134% R_1 drift is now formally EXPLAINED -- R_1 multiset {8,4} vs {6,6} are NOT multiset-equal => not f-free => scheme-pin is structural necessity.

# f_conv Identity (S76 MPL-SPEC-CONVERGENCE INFO)

f_conv = pi^4 / (9216 * a_0^2) EXACT. a_2 cancellation is structural (algebraic, from G_N matching). R_1 IS protected (2.89% drift L=3-9). f_conv NOT R-protected (5.0 OOM total span L=3-9). Planck-implied L_max* = 2.92 (physical L_max=3 first integer above; A_s gap 0.12 OOM = 2.7% L_max overshoot).

S77 f*-weighted: f_conv(f*)/f_conv(SDW) = 1.784. M_0(f*)/a_0 = 0.749 at L_max=3. delta_log10 = +0.251 OOM (closes 0.12 OOM S75 residual; does NOT close full 3.36 OOM W1-B gap).

# R_1 Tau Trajectory (S77 INFO)

R_1(tau) strictly monotone increasing across [0, 0.5]: 1.109 (tau=0) -> 1.129 (fold) -> 1.237 (tau=0.5). NOT stationary at fold (dR_1/dtau = +0.203, d^2 = +1.03). Total variation 11.13%. a_0 = const (6440) at fixed L_max (mode count topological). a_2 varies 19.86%, a_4 varies 28.65%. **L_max protection != tau protection**: structurally different phenomena (Weyl exponent cancellation vs curvature redistribution).

# W9b-105 Spectral Dimension at Fiber-Transition Scale (S84 FAIL)

Plan-literal extractor s* = argmin |d^2 zeta_D / ds^2| on [0.5, 6.0] is BOUNDARY-DOMINATED: d^2 zeta/ds^2 = sum d_rho (ln lambda)^2 lambda^{-s} > 0 with derivative ~ -<(ln lambda)^3>_s < 0 (most lambda > 1) hence monotone-decreasing on scan range. argmin at s* = 5.999 (upper boundary). d_spec = s* + 1/(d ln zeta/ds) = 5.999 + 1/(-0.9057) = 4.895. OUTSIDE [2.0, 4.0] => FAIL. L_max drift L=6 -> L=12 GROWS d_spec (4.28 -> 5.04), away from cube-3 target. Cube-3 "12 = 4 * d_spec" override NOT supported. Closure SHA `a192e39a7d187448798282de8e241ad399561445d40171a336539a9511617cac`.

# Normalization Conventions

- **Spin rep of Lie algebras via adjoint**: rho_spin(e_a) = (1/4) sum_{bc} ad(e_a)_{bc} gamma_b gamma_c where ad(e_a)_{bc} = f_{a,c,b} = -f_{a,b,c}. Sign matters: ad(e_a)_{cb} = f_{abc} but ad(e_a)_{bc} = -f_{abc}. Use matrix entries directly, not f with index-matched gammas.
- Seeley-DeWitt: a_k with (4*pi)^{-d/2} prefactor, d=8 for SU(3).
- Spinor rank: 2^4 = 16 for 8-dim SU(3).
- Volume-preserving Jensen deformation (TT constraint).
- Kosmann pairing kernel: V_nm = sum_{a=0..7} |<n|K_a|m>|^2 (SPINOR basis, not frame).
- K_a = (1/8) sum_{rs} A^a_{rs} gamma_r gamma_s (Kosmann from frame structure constants).
- Connes 15/16: finite-density spectral action exists (van Suijlekom, JNCG 2022).
- Pre-S86+: tag a_n citations as a_n^{regulator} (zeta, Pauli-Villars, Mellin, lattice, cutoff) per .claude/rules/regulator-pin-discipline.md.

# Key Eigenvalue Data (SU(3) Jensen-deformed)

- B1: lambda = 0.819. B2: lambda = 0.845 (min at tau = 0.190). B3: lambda = 0.978 (at tau = 0.20).
- phi_paasch = 1.531580 at tau = 0.15 (canonical -- check canonical_constants.py before re-citing).
- Kirchberg(K') bound 5R/16 = 0.631 at fold (tightest). lambda_1^2/Kirchberg = 1.065 (6.5% gap). All Lichnerowicz/FK bounds SATISFIED.
- R(tau=0.19) = 2.018 (machine epsilon).
- a_2^{SD}(fold) = 0.728235 (Gilkey, exact). Vol(SU(3))(fold) = 1349.74. C_8 = 1/(384*pi^4) Weyl constant.
