---
name: S85 W0-3 CC-5 2:1 Identity Theorem (W3-31 closure)
description: b_pow(span_2)/b_pow(span_3) = 2.000 is a spectral-triple identity derived from A_s-linear/f_NL-sqrt power-counting in 1/M_0, machine-precision verified at L in {3..12}
type: project
---

**S85-CC-5-LMAX-ASYMPTOTIC-REFIT (W0-3): PASS** — theorem-grade closure of W3-31.

**Gate value**: |b_pow(span_2)/b_pow(span_3) − 2.000| = 2.22 × 10⁻¹⁵ (12 orders under 1e-3 PASS tol).

**Theorem (W3-31 closure, S85 W0-3)**: For the CC-5 cluster-span observables span_2(L) = span_R(A_s/μ) and span_3(L) = span_R(f_NL/r) over the 5-regulator set {zeta, Zubarev, SDW, dim-reg, lattice-BR} at τ_fold on L_max ∈ {3..12}, the log-log OLS slope ratio b_pow(span_2)/b_pow(span_3) equals 2 exactly. Proof: A_s ∝ f_conv ∝ 1/M_0², μ ∝ 1/M_0 ⇒ A_s/μ ∝ 1/M_0 (p=1); f_NL ∝ 1/√(2 M_0), r = r_FW invariant ⇒ f_NL/r ∝ 1/√M_0 (p=1/2). span(Y^p) = σ^p with σ = span(1/M_0) ⇒ ln span_2 = 2 · ln span_3 + const ⇒ b_pow(span_2) = 2 · b_pow(span_3). The identity is L-INDEPENDENT; holds at any L_max where both spans are positive.

**Why**: the 2:1 ratio is a pure power-counting signature of how CC-5 observables are constructed from M_0^R = 0.5 · Σ d_j · w_R(λ_j). NOT an empirical finding; a direct corollary of the S80 W1-4 CC-RATIOS-ONLY theorem.

**How to apply**: Any downstream mechanism using b_pow as an anchor must specify L_max or re-compute at its native scale — individual b_pow values are L-DEPENDENT (growing Weyl-growth signature). The RATIO is the invariant. The identity is a canonical input to W5 (HP^0 comparison) and W11 (van-den-dungen structural audit) — if they do not reproduce it, there is a machinery error.

**Key quantitative results (L ∈ {8..12})**:
- b_pow(span_1) = 1.5944 (R²=0.9998)
- b_pow(span_2) = 6.5637 (R²=0.99998)
- b_pow(span_3) = 3.2819 (R²=0.99998)
- ratio 2/3 = 2.000 to machine precision
- All monotone-convergent (drift s1=4.27%, s2=1.44%, s3=1.44%, all < 5%)

**Negative result (CF-1)**: The S83 G4 anchor b_pow(span_3)/b_pow(span_1) = 3/2 is NOT an asymptotic identity. At L ∈ {8..12} the observed ratio is 2.058, a 37% deviation from 1.500. Flags: low-L coincidence, not structural. Permanent-registry correction recommended.

**Artifacts**:
- Script: `computations/s85_w0_cc5_lmax_asymptotic_refit.py` (SHA 8f7c418f...)
- NPZ: `computations/s85_w0_cc5_lmax_asymptotic_refit.npz` (content_sha fe2d058d...)
- audit_sha = 331d6529...
- WP: `sessions/archive/session-85/session-85-w0-workingpaper.md` §W0-3
- Spectrum cache: `s84_spectrum_cache_L12_tau019.npz` (SHA 9e6d9cf7..., L≤12 at τ=0.190)
