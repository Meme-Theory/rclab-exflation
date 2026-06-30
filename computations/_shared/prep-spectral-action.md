# Prep Block — T3-SPECTRAL-ACTION

**Gate ID**: T3-SPECTRAL-ACTION
**Script**: `computations/_shared/spectral_action.py` (72723 bytes, 1852 lines)
**Status**: PRODUCTION (live in `computations/_shared/`; also archived in `computations/_shared/`)
**Agent**: Spectral-Geometer
**Classification**: GEOMETRIC
**Domain**: Spectral action (Seeley-DeWitt a_0, a_2, a_4 on Jensen SU(3))
**Session**: S81 T3 re-run

## Hypothesis

The Chamseddine-Connes spectral action S = Tr(f(D^2/Lambda^2)) on Jensen-deformed
SU(3) yields Seeley-DeWitt coefficients a_0, a_2, a_4 encoding volume, scalar
curvature, and gauge-kinetic-plus-curvature-squared terms respectively, with
R(g_s) matching Baptista's analytical bracket [2*e^{2s}-1+8*e^{-s}-e^{-4s}]/8.

## Machinery Pins (PRDR)

| Parameter              | Value                          | Source                          |
|:-----------------------|:-------------------------------|:--------------------------------|
| `max_pq_sum`           | 3 (L_max proxy on (p,q) sum)   | Script default, line 1700       |
| `Lambda`               | 5.0 (energy cutoff)            | Script default, line 1700       |
| `t_range` (SD fit)     | (0.01, 0.5)                    | Script default, line 1693       |
| `n_points` (fit grid)  | 200                            | Script default, line 1693       |
| `s_values` sweep       | linspace(0.0, 2.0, 21)         | Script default, line 1698       |
| `f_type`               | heat (exp(-x))                 | Script default, line 934        |
| `OMP_NUM_THREADS`      | 8 (capped)                     | Script line 58                  |
| `MKL_NUM_THREADS`      | 8 (capped)                     | Script line 59                  |
| GPU path               | CPU-only (eigvalsh on small blocks) | All blocks dim(p,q)*16 <= 240 |
| Convention             | Chamseddine-Connes dim=8       | Gilkey 1995                     |
| Canonical imports      | tau_fold, Vol_SU3_Haar         | Lines 64-66                     |

## Input SHA-256 Pins (64-char hex)

| File                         | SHA-256                                                            |
|:-----------------------------|:-------------------------------------------------------------------|
| spectral_action.py           | ab38e01616ee15b50b17f1dd02a60b182269a561919fd70bdd8e558bf8971ccd   |
| dirac_spectrum.py            | eee1b6fdcbb86847385130b3b3467c76fe1b5b73573d7dac4baf428cf4ff163f   |
| canonical_constants.py       | 68b50cd325d2cc8c63b775da3b6b92f538da582bee44c5d906c81259f24dd12f   |

## Output Artifacts (post-run SHA-256)

| File                            | SHA-256                                                            |
|:--------------------------------|:-------------------------------------------------------------------|
| spectral_action_results.png     | 335039f0e91d0fb2bb436c8bbe7be65523ad5a5feac702c591a5b373af1522e4   |
| heat_kernel_analysis.png        | 2767ded9f63792712bac1631116b3b6b3c1d862726203b74d773752445e44e6c   |
| veff_stabilization.png          | 127645d5c0e1aa5de538c460d56d792a7f9f0beb42d144ed293756fde5baa0e8   |

## Closure SHA-256

**aaaa00322599e18c6539fe3fe87be49b7feaadc30e513e6e7c71202730e136b1**

## Expected Output 4-tuple

```
value=(a_0=4.658e-02, a_2=7.325e+00, a_4=-2.918e+02,
       S_heat(0)=11690.4, R_exact(0)=2.000, R_exact(2)=27.320,
       corr=0.9619, d_eff=8.58, kappa_cc0=0.4628)
scheme=heat_kernel_expansion
convention=Chamseddine-Connes_dim8
L_max=3 (max_pq_sum)
sha256=aaaa00322599e18c6539fe3fe87be49b7feaadc30e513e6e7c71202730e136b1
```

## Substitution Chain (Einstein-Hilbert from a_2)

**Step 1 Definition** (Gilkey 1995, heat kernel expansion on d=8 manifold):
```
K(t) = Tr(exp(-t D^2)) = sum_n a_n * t^{(n-d)/2}
     = a_0 * t^{-4} + a_2 * t^{-3} + a_4 * t^{-2} + a_6 * t^{-1} + a_8 + ...
```

**Step 2 Chamseddine-Connes identifications** (spin bundle, dim(S)=16 for d=8):
```
a_0 = 16 * Vol / (4pi)^4
a_2 = 16 * (R/6) * Vol / (4pi)^4
a_4 = 16 * (5R^2 - 2|Ric|^2 + 2|Riem|^2)/360 * Vol/(4pi)^4 + gauge + Higgs...
```

**Step 3 Scalar curvature from ratio** (dim(S) and Vol cancel):
```
6 * a_2 / a_0 = R
```

**Step 4 Baptista bracket** (eq 3.80 of Paper 15):
```
R(s) / R(0) = [2*e^{2s} - 1 + 8*e^{-s} - e^{-4s}] / 8
At s=0: bracket = 2 - 1 + 8 - 1 = 8  =>  R(0)/R(0) = 1  [consistent]
```

**Step 5 Direction (verified numerically)**:
```
s=0.000  bracket=8.000000  R/R0=1.000000
s=0.050  bracket=8.001446  R/R0=1.000181
s=0.100  bracket=8.011185  R/R0=1.001398
s=0.150  bracket=8.036570  R/R0=1.004571
s=0.190  bracket=8.072576  R/R0=1.009072  <-- tau_fold
s=0.200  bracket=8.084166  R/R0=1.010521
```

**Conclusion**: R(s) INCREASES monotonically for s > 0. Therefore a_2(s) INCREASES
(since Vol is preserved and R is the only s-dependent factor in a_2/dim(S)).
Einstein-Hilbert action (gravity = second spectral moment) therefore INCREASES
under Jensen deformation.

## Simultaneous Direction of Total S (independent)

Total spectral action S_heat(Lambda=5.0) = Tr(exp(-D^2/25)):
```
S(0.0) = 11690.4
S(0.5) = 11269.8  (-3.6%)
S(1.0) = 9701.4   (-17.0%)
S(2.0) = 2974.9   (-74.6%)
```

S_heat DECREASES in s. This is NOT a contradiction with a_2 INCREASING, because
S_heat at finite Lambda probes a_4, a_6, a_8, ... as well (f(x)=exp(-x) has
an infinite-order expansion in 1/Lambda^2), and the negative a_4 term (computed
-2.918e+02 at s=0, even with large uncertainty) dominates the UV contribution
at Lambda=5.0. The geometric and gravitational moments tell a structurally
consistent story: gravity grows while the full spectral action decays.

## What PASSES means

The machinery validates: exact R(g_s) matches Baptista analytical to 5e-15,
volume preserved to 1e-16, correlation S vs V_Baptista = 0.9619, Weyl d_eff
within 7.2% of 8.0 at truncation 3, SU(2) Dirac benchmark passes.

## What FAILS means

Would require: volume NOT preserved, R_exact NOT matching Baptista bracket,
Weyl dimension strongly deviant (>30%), SU(2) benchmark failure, or complete
loss of correlation between spectral action and Baptista potential.

## What INFO means (applied here)

The gate is a diagnostic / machinery validation, not a pass/fail physics claim.
The script's reliable outputs cross-check; its unreliable outputs (individual
a_0, a_2, a_4) are structurally limited by truncation. INFO is the appropriate
verdict because no pre-registered binary threshold applies.

## Solution-space boundary this gate maps

The spectral-action machinery on Jensen SU(3) at max_pq_sum=3 truncation:
  - correctly produces total S(s), its monotonicity, and Baptista correlation
  - correctly reproduces exact R(g_s) via Levi-Civita (NOT via heat kernel)
  - CANNOT produce reliable individual Seeley-DeWitt coefficients at this L_max
  - produces a Coleman-Weinberg Lambda_cc=0 crossing at kappa ~ 0.4628

Any downstream mechanism that depends on individual a_0/a_2/a_4 numerics at
this truncation is UNDER-CONSTRAINED; must push L_max higher or use exact
connection results. Mechanisms that depend only on ratios, totals, or exact
R(s) remain viable.

## Flags

- Script IS in PRODUCTION (`computations/_shared/`). Changes audited.
- Script has a one-shot twin in `computations/_shared/` that differs only in the S81
  T3 compliance header (canonical imports + OMP caps). The archived twin is
  the earlier S14 one-shot; the live production version is the current one.
- The script's own stdout explicitly warns "individual coefficients have >100%
  uncertainty at max_pq_sum=3" -- we carry that caveat into the verdict.
- `tau_fold` in `canonical_constants.py` is `0.19` (legacy), consistent with
  S42 constants_snapshot; the newer canonical `tau_fold_v2 = 0.190` in some
  plans is equivalent at the precision tested here.

## Notes

- 3 PNG artifacts regenerated under closure SHA.
- Full stdout log: `/tmp/t3_spectral_action.log` (transient).
- Runtime: roughly 90-120 s on CPU (capped OMP=8); no GPU path used since all
  eigvalsh blocks are <= 240x240 (dim(p,q)*16 for max p+q=3).
- The S81 T3 canonical header (`from canonical_constants import tau_fold,
  Vol_SU3_Haar`) was already present; no script modifications were required.
