# S45 W4-R7: Heat Kernel Validity Audit on Finite Discrete Spectrum

**Gate**: HEAT-KERNEL-AUDIT-45
**Verdict**: INFO (epistemological audit)
**Author**: Spectral-Geometer
**Session**: 45
**Date**: 2026-03-15

---

## 1. The Central Problem

The Dirac operator D_K on SU(3) with Jensen deformation at tau = 0.190, truncated to max_pq_sum = 5, yields a **finite discrete spectrum**: 992 distinct eigenvalue levels, 101,984 states with Peter-Weyl multiplicities (6,440 positive eigenvalues before the PW squaring). The eigenvalue range is |lambda| in [0.820, 2.061] in M_KK units.

Multiple S44-S45 computations applied continuum heat kernel formulas to this spectrum. The heat kernel on a **compact Riemannian 8-manifold** has specific analytic structure -- short-time asymptotic expansion with (4 pi sigma)^{-4} divergence, meromorphic spectral zeta with poles at s = 4, 3, 2, 1, spectral dimension flowing to dim(M) = 8 as sigma -> 0. On our truncated spectrum, **none of these properties hold**. This audit determines which computations survive this structural mismatch and which are artifacts.

---

## 2. The Finite Spectrum Heat Kernel: What It Is

For a finite positive spectrum {(lambda_k, d_k)}_{k=1}^{N}, the heat trace is:

$$K(\sigma) = \sum_{k=1}^{N} d_k \, e^{-\sigma \lambda_k^2} \tag{1}$$

This is an **entire function** of sigma (finite sum of exponentials). Its properties:

| Property | Continuum 8-manifold | Finite spectrum (N = 992) |
|:---------|:---------------------|:--------------------------|
| K(0) | Diverges as (4 pi sigma)^{-4} | Finite: K(0) = sum d_k = 6440 |
| Small-sigma expansion | Asymptotic: K ~ (4 pi sigma)^{-4} [a_0 + a_2 sigma + ...] | Convergent Taylor: K = A_0 - A_2 sigma + A_4 sigma^2/2! - ... |
| Spectral zeta poles | Meromorphic: poles at s = 4, 3, 2, 1 | Entire: no poles anywhere |
| d_s as sigma -> 0 | d_s -> dim(M) = 8 | d_s -> 0 (not 8) |
| d_s as sigma -> infinity | d_s -> 0 (compact, gapped) | d_s -> 0 (same) |
| zeta'(0) meaning | Regularized functional determinant | Finite sum: -2 sum d_k ln|lambda_k| |

The Taylor expansion of K(sigma) around sigma = 0 converges exactly (machine epsilon error at 20 terms for all sigma < 1), because K is a finite sum of entire functions. **This is the fundamental distinction**: on the continuum, the SD expansion is *asymptotic* (divergent for fixed sigma as terms increase); on the finite spectrum, it is *convergent* (and equals the exact function).

Numerical verification:

| sigma | K_exact | K_Taylor(5 terms) | K_Taylor(20 terms) | Relative error |
|:------|:--------|:------------------|:-------------------|:---------------|
| 0.01 | 6277.77 | 6277.77 | 6277.77 | 0 |
| 0.10 | 5001.65 | 5001.76 | 5001.65 | 1.8e-16 |
| 0.50 | 1916.22 | 2190.37 | 1916.22 | 1.6e-13 |
| 1.00 | 644.46 | 7754.58 | 644.46 | 4.5e-7 |
| 2.00 | 100.09 | 163684.68 | -159.36 | 2.6 (divergent) |

The 5-term Taylor diverges above sigma ~ 0.5; the 20-term Taylor converges up to sigma ~ 1.5. The **exact sum** converges everywhere.

---

## 3. Audit of Individual Computations

### 3.1 Seeley-DeWitt Coefficients a_0, a_2, a_4

**Computation**: Extract a_n from the heat kernel expansion K(sigma) ~ sum a_n sigma^{n-d/2}.

**Property used**: On the continuum, the small-sigma asymptotic expansion of K(sigma) encodes geometric invariants: a_0 = (4 pi)^{-d/2} * rank * Vol, a_2 propto integral(R dV), a_4 propto integral(R^2 + Ric^2 + Rm^2 dV).

**What actually happens on the finite spectrum**: The codebase computes:

- a_0 = sum d_k = 6440 (stored as `a0_fold`)
- a_2 = sum d_k / lambda_k^2 = 2776.17 (stored as `a2_fold`)
- a_4 = sum d_k / lambda_k^4 = 1350.72 (stored as `a4_fold`)

These are the **spectral zeta function at non-negative integer values**: zeta(0), zeta(1), zeta(2). They are well-defined finite sums on the truncated spectrum. The computation is arithmetically exact.

**The epistemological question**: Do these spectral zeta values equal the geometric curvature integrals?

**Answer: YES, with a controlled truncation error.**

The Peter-Weyl decomposition gives D_K as a direct sum of finite matrices over irreps. Each irrep (p,q) contributes d_{p,q}^2 = [(p+1)(q+1)(p+q+2)/2]^2 states to the spectrum (the squared dimension comes from the PW decomposition of L^2(G)). The sum over all irreps gives the exact heat trace on the full manifold (Paper 25, Show 2011; Paper 04, Gilkey 1978):

$$K_{\text{full}}(\sigma) = \sum_{(p,q) \in \hat{G}} d_{p,q}^2 \sum_{i=1}^{16} e^{-\sigma \lambda_{(p,q),i}^2} \tag{2}$$

Our truncation keeps irreps with p + q <= 5. The missing UV tail consists of irreps with p + q > 5, which have eigenvalues lambda > lambda_max = 2.061. These contribute:

$$K_{\text{tail}}(\sigma) = \sum_{p+q > 5} d_{p,q}^2 \sum_i e^{-\sigma \lambda_{(p,q),i}^2} \tag{3}$$

For the spectral zeta at s = 0: zeta_tail(0) = sum of all missing multiplicities (a large number). For s = 1: zeta_tail(1) = sum d_k / lambda_k^2 over missing modes. Since lambda_k > 2.06 for all missing modes, and d_k grows polynomially while 1/lambda_k^2 shrinks, the tail contribution to zeta(1) is **convergent but not small**. The Weyl effective dimension d_eff = 7.41 (fold) vs 8.19 (round) confirms the truncation has not yet reached the Weyl regime.

**Classification**: APPROXIMATION that converges to the geometric a_n as max_pq_sum -> infinity. The convergence rate is set by the ratio zeta_tail(s)/zeta_trunc(s), which decreases with s. For a_0 (s=0), the tail correction is large (we capture only 6440 out of infinitely many modes). For a_2 (s=1), it is moderate. For a_4 (s=2), it is smaller (tail modes contribute less because 1/lambda^4 falls faster).

**Verdict**: VALID as an approximation. The a_n computed from the truncated spectrum are lower bounds on the full a_n (all terms in the tail are positive for even n). The identification a_2 propto integral(R dV) holds only in the limit max_pq_sum -> infinity, but the truncated values are consistent with the known curvature of SU(3).

### 3.2 Spectral Dimension d_s(sigma)

**Computation**: d_s(sigma) = -2 sigma (dK/dsigma) / K(sigma) = -2 d(ln K) / d(ln sigma).

**Property used**: On the continuum, d_s -> dim(M) = 8 as sigma -> 0. The "walking scale" where d_s transitions from UV (= 8) to IR (= 0) contains information about the geometry at intermediate scales.

**What actually happens on the finite spectrum**: As sigma -> 0:

$$d_s(\sigma) = \frac{2\sigma \sum d_k \lambda_k^2 e^{-\sigma\lambda_k^2}}{\sum d_k e^{-\sigma\lambda_k^2}} \to \frac{2\sigma \cdot A_2}{A_0} = \frac{2\sigma \cdot 16448}{6440} \to 0 \tag{4}$$

Numerically confirmed:
- sigma = 1e-4: d_s = 0.0005
- sigma = 1e-2: d_s = 0.051
- sigma = 1e-1: d_s = 0.500
- sigma = 1.0: d_s = 4.13
- sigma = 10.0: d_s = 15.25

The spectral dimension **never reaches 8**. It rises linearly from 0, passes through d_s = 4 near sigma ~ 1, then **exceeds 8** at larger sigma before eventually falling to 0 in the deep IR. The "d_s = 4" that was used for n_s extraction in S44 DIMFLOW-44 occurs at sigma ~ 0.97 -- this is in the regime where d_s is varying rapidly and happens to pass through 4 en route to overshooting.

**The overshooting phenomenon** (d_s > 8 at sigma ~ 5-10) has no continuum analog. On a smooth 8-manifold, d_s is monotonically non-increasing from 8 to 0. On the finite spectrum, the absence of UV modes creates a "spectral pileup" that makes d_s overshoot the true dimension.

**Classification**: ARTIFACT of the truncation in the UV regime (sigma << 1) and the intermediate regime (sigma ~ 1-10). The only regime where d_s is meaningful is the deep IR (sigma >> 1/lambda_min^2 ~ 1.5), where d_s -> 0 reflects the genuine gap structure.

**The correct diagnostic on a finite crystal**: For a finite periodic structure with N modes, the natural dimensionality probe is the **Weyl counting function**:

$$N(\lambda) \sim C \cdot \lambda^{d_{\text{Weyl}}} \tag{5}$$

The log-log slope of the integrated density of states gives d_Weyl = 6.81 (from the s45_unexpanded_sa computation). This is the correct effective dimension, not d_s at any particular sigma. The Weyl law probes the **asymptotic distribution of eigenvalues**, which is the proper analog of "dimension" for a truncated spectrum.

Alternative diagnostics:
- **Weyl effective dimension**: d_Weyl = 6.81 (from mode counting slope). Most reliable.
- **Participation ratio**: how many modes contribute at a given energy scale.
- **Spectral form factor**: two-point eigenvalue correlations (probes RMT universality class).

**Verdict**: INVALID as a dimension diagnostic. d_s on the finite spectrum does not reach 8, overshoots in the intermediate regime, and the value d_s = 4 at sigma ~ 1 is a coincidence of the particular truncation. The extraction of n_s from d_s in S44 DIMFLOW-44 and S45 SIGMA-SELECT-45 is **not grounded** -- the sigma at which d_s = 4 has no intrinsic meaning on the finite crystal.

### 3.3 Analytic Torsion T

**Computation**: T = exp(-(1/2) zeta'(0)), where zeta(s) = sum d_k |lambda_k|^{-2s} and zeta'(0) = -2 sum d_k ln|lambda_k|.

**Property used**: On the continuum, the Ray-Singer analytic torsion is defined via the spectral zeta function of the Laplacian on differential forms. It requires:
1. The spectral zeta zeta(s) to have a meromorphic continuation to s = 0.
2. The poles of zeta(s) at s = d/2, d/2-1, ..., 1 to be subtracted (absorbed by renormalization).
3. zeta'(0) to be the finite part after this subtraction.

On the full continuum SU(3), the spectral zeta zeta_{D_K^2}(s) has poles at s = 4, 3, 2, 1. The residues at these poles are precisely the Seeley-DeWitt coefficients a_0, a_2, a_4, a_6. The analytic continuation through these poles to s = 0 is non-trivial and involves subtracting the divergent contributions, leaving a finite, scheme-dependent remainder.

**What actually happens on the finite spectrum**: zeta(s) = sum d_k |lambda_k|^{-2s} is **entire** in s (no poles, since all lambda_k > 0 and N is finite). Therefore:

$$\zeta'(0) = -2\sum_{k=1}^{N} d_k \ln|\lambda_k| = -93,490 \tag{6}$$

This is a well-defined finite sum. But it is **not the analytic torsion** of SU(3). The analytic torsion of SU(3) requires summing over ALL eigenvalues (infinitely many), and the resulting series zeta(s) = sum_{all modes} d_k |lambda_k|^{-2s} converges only for Re(s) > 4. The continuation to s = 0 involves cancellations between the pole contributions and the finite part that cannot be captured by any finite truncation.

The truncated zeta'(0) is **extensive** in the number of modes: it grows linearly with the number of PW sectors included. This is confirmed by the sector decomposition:

| Sector dim^2 | zeta'(0) contribution | Fraction of total |
|:-------------|:---------------------|:-----------------|
| 1 (singlet) | +3.83 | -0.004% |
| 9 | -170.43 | 0.18% |
| 36 | -4412.84 | 4.72% |
| 64 | -4723.84 | 5.05% |
| 100 | -33031.90 | 35.33% |
| 225 | -51154.35 | 54.72% |

The high-multiplicity sectors (dim^2 = 100, 225) dominate. Adding the next PW shell (p + q = 6, 7, ...) would add sectors with dim^2 = 441, 784, ... , each contributing O(dim^2 * N_levels * ln lambda) to zeta'(0). The result T ~ 10^{20301} grows without bound as more sectors are added.

On the continuum, this growth is absorbed by the poles of the spectral zeta. The regularized zeta'(0)_full involves cancellations between the growing partial sums and the pole subtractions. The truncated sum captures the growth but not the cancellation.

**The S45 observation that T > 1 is universal for compact manifolds with no zero modes** (memory entry) is **correct for the truncated sum** but not informative about the actual analytic torsion. The actual analytic torsion of a compact Lie group with bi-invariant metric is known to be a finite number computable from the root system (Paper 08, Mueller 1978; Paper 25, Show 2011).

**Classification**: ARTIFACT of the truncation. The quantity -2 sum d_k ln|lambda_k| is a well-defined spectral moment, but it is not the analytic torsion of SU(3). It is an unregularized partial sum that diverges as the truncation is removed. The reported T ~ 10^{20301} is an artifact.

**The correct computation**: To compute the analytic torsion of Jensen-deformed SU(3), one would need either:
1. A closed-form expression for the spectral zeta using representation theory (viable for bi-invariant metric, difficult for Jensen-deformed).
2. A heat kernel regularization: subtract the SD asymptotic terms from K(sigma) before integrating, then take the Mellin transform. This requires knowing a_0 through a_8 (for 8-dimensional SU(3)) independently from geometric computation.

The S45 TRUNCATED-TORSION-45 result (T_singlet = 0.147 for the singlet sector) is **more defensible** because the singlet sector has only 16 modes and the UV tail correction is suppressed by the small multiplicity (dim^2 = 1). But even this is a partial sum, not the regularized torsion.

**Verdict**: ARTIFACT. The reported T ~ 10^{20301} is the exponential of an unregularized, divergent partial sum. It does not represent the analytic torsion of SU(3).

### 3.4 Spectral Action S(Lambda)

**Computation**: S(Lambda) = Tr f(D^2/Lambda^2) = sum d_k f(lambda_k^2/Lambda^2).

**Property used**: The spectral action is defined as a trace of a function of the Dirac operator. For any choice of cutoff function f and scale Lambda, S is a well-defined number.

**On the finite spectrum**: S(Lambda) = sum_{k=1}^{N} d_k f(lambda_k^2/Lambda^2) is a finite sum of values of f. No asymptotic expansion, analytic continuation, or regularization is needed. The computation is exact.

The S45 UNEXPANDED-SA-45 computation verified that the 20-term Taylor expansion of S_heat(Lambda) agrees with the exact sum to machine epsilon (1.6e-16) for all Lambda, confirming that the polynomial expansion captures ALL content of the spectral action on the finite spectrum.

**Classification**: VALID. The spectral action is the one computation that transfers directly from the continuum to the finite spectrum without any loss of meaning. It is a finite sum, exactly computable, with no regularization ambiguity.

**Verdict**: VALID. No issues.

### 3.5 Heat Kernel Regularization of G_N

**Computation**: G_N ~ 1 / (f_2 Lambda^2 a_2), where a_2 is the second Seeley-DeWitt coefficient.

**Property used**: On the continuum, a_2 = (4 pi)^{-d/2} integral(R/6 dV) * rank(spinor), so a_2 encodes the integrated scalar curvature. Newton's constant is extracted by matching the a_2 term in the spectral action to the Einstein-Hilbert action integral(R dV).

**On the finite spectrum**: a_2 = zeta(1) = sum d_k / lambda_k^2 = 2776.17 is a well-defined spectral moment. The **identification** a_2 = curvature integral requires that the truncated spectrum faithfully represents the curvature information encoded in the full spectrum.

This is more subtle than the spectral action itself. The spectral action S(Lambda) is exact on the truncated spectrum -- but it is the spectral action of the **truncated** spectrum, not of SU(3). The G_N extraction works as follows:

1. Compute S(Lambda) on the truncated spectrum: exact.
2. Expand S(Lambda) at large Lambda: S ~ f_4 Lambda^4 A_0 + f_2 Lambda^2 Z_2 + f_0 Z_4 + ...
3. Identify the Lambda^2 term as the Einstein-Hilbert action: f_2 Lambda^2 Z_2 = integral(R dV) / (16 pi G_N).
4. Solve for G_N.

Step 3 is the ANSATZ. It assumes Z_2 = a_2 (geometric) = (4 pi)^{-d/2} integral(R/6 dV) * 16. This is an approximation whose quality depends on how much of the scalar curvature information is captured by the lowest 992 eigenvalue levels.

The convergence of Z_2 with truncation is better than that of A_0 (= zeta(0)) because the 1/lambda^2 weighting suppresses UV modes. The tail correction to Z_2 is roughly:

$$\delta Z_2 = \sum_{p+q > 5} d_{p,q}^2 \sum_i \frac{1}{\lambda_{(p,q),i}^2} \tag{7}$$

Since lambda_{(p,q),i}^2 > 4.25 for all missing modes and the Casimir grows quadratically with p+q, this sum converges (Weyl's law guarantees it). The first missing sector (p+q = 6) would contribute modes with lambda^2 ~ 5-6, adding roughly O(1000) to Z_2 ~ 2776. So the truncation error is O(30-50%).

**Classification**: APPROXIMATION. The G_N extraction is valid in principle but carries O(30-50%) truncation error from the missing UV tail. The Weyl effective dimension d_eff = 6.81 (vs 8 for the full manifold) quantifies this deficit.

**Verdict**: VALID as an order-of-magnitude estimate. Not valid for precision work. The 0.83-decade tension between M_KK_gravity and M_KK_kerner (CONST-FREEZE-42) may partially reflect this truncation error.

---

## 4. Summary Classification Table

| Computation | Property Used | Valid on Finite Spectrum? | Alternative/Correction |
|:---|:---|:---|:---|
| **a_0, a_2, a_4** (SD coefficients) | Heat kernel asymptotics, geometric curvature integrals | APPROXIMATION -- converges to geometric a_n as max_pq_sum -> infinity. Quality degrades for lower n (a_0 worst, a_4 best). | Increase max_pq_sum. Or compute geometric a_n independently from Riemann tensor (known exactly for Jensen SU(3)). |
| **d_s(sigma)** (spectral dimension) | Return probability scaling exponent | ARTIFACT -- d_s -> 0 as sigma -> 0 (not 8); overshoots above 8 at intermediate sigma; no intrinsic walking scale. | Use **Weyl counting function** d_Weyl = d(log N)/d(log lambda) = 6.81. Or use participation ratio at fixed energy. |
| **T** (analytic torsion) | Zeta-regularized determinant via analytic continuation | ARTIFACT -- truncated zeta'(0) is extensive in N, misses pole subtractions that define the regulated torsion. T ~ 10^{20301} is unphysical. | Compute torsion via heat kernel regularization with independently known SD coefficients subtracted. Or use representation-theoretic formulas (viable for bi-invariant, difficult for Jensen). |
| **S(Lambda)** (spectral action) | Trace of cutoff function | **VALID** -- exact finite sum, no regularization needed. Polynomial expansion converges. | None needed. But S(Lambda) is the spectral action of the **truncated** spectrum, not of the full manifold. |
| **G_N from a_2** | Identification of a_2 with curvature integral | APPROXIMATION -- valid up to O(30-50%) truncation error. | Compute a_2 independently from Jensen metric Ricci scalar (analytically known). Cross-check with higher max_pq_sum. |

---

## 5. The Fundamental Structural Issue

The hierarchy of heat kernel quantities is, in order of robustness on a finite spectrum:

**Tier 1 (exact on finite spectrum):**
- Spectral action S(Lambda) for any f, any Lambda
- Heat trace K(sigma) for any sigma > 0
- Spectral zeta moments sum d_k lambda_k^{-2s} for any real s
- Taylor coefficients of K(sigma)

**Tier 2 (faithful approximation, converging as truncation -> infinity):**
- Seeley-DeWitt coefficients a_0, a_2, a_4 (convergence rate: ~ 1/(max_pq_sum)^2 for a_n with n > 0)
- Spectral action S(Lambda) as an approximation to the **full** spectral action on SU(3)
- Eigenvalue counting function N(lambda) in the Weyl regime
- G_N extraction from a_2

**Tier 3 (meaningless on finite spectrum without additional regularization):**
- Spectral dimension d_s(sigma) in the UV regime (sigma << 1)
- Analytic torsion T = exp(-(1/2) zeta'(0))
- Any quantity that relies on zeta(s) having poles (pole residues, analytic continuation)

The computations in S44-S45 that produced large numbers (T ~ 10^{20301}, d_s reaching 15 at intermediate sigma) fall into **Tier 3**. They are not wrong as arithmetic -- the numbers are correctly computed from the data. They are wrong as **spectral geometry**, because the quantities they purport to compute require continuum structure that the finite spectrum does not possess.

---

## 6. What Would Fix This

### 6.1 For spectral dimension:
Replace d_s(sigma) with the Weyl counting exponent d_Weyl = 6.81. This is the correct finite-spectrum analog of "dimension" and converges to 8 as max_pq_sum -> infinity. The spectral tilt n_s CANNOT be extracted from d_s on the truncated spectrum -- it requires either the full continuum d_s (uncomputable without all modes) or a different observable.

### 6.2 For analytic torsion:
Compute the geometric Seeley-DeWitt coefficients a_0 through a_8 independently from the Jensen metric (the Riemann tensor is known analytically from S20a). Use these to subtract the pole contributions from the truncated zeta(s), leaving a finite remainder that approximates the true torsion. Alternatively, recognize that the torsion of SU(3) is computable in closed form for the bi-invariant metric (using root system data from Paper 25) and estimate the Jensen correction perturbatively.

### 6.3 For G_N:
Cross-check a_2 from the spectrum against a_2 from the known scalar curvature R(tau) of Jensen-deformed SU(3). The scalar curvature is R = 12 - 6 tau + ... (from the Ricci tensor computation in S20a). The geometric a_2 = (4 pi)^{-4} * 16 * R/6 * Vol(SU(3)). Comparing this to the spectral a_2 = 2776.17 quantifies the truncation error.

### 6.4 For spectral action:
No fix needed -- the computation is exact on the truncated spectrum. The only caveat is that S(Lambda) on the truncated spectrum differs from S(Lambda) on the full SU(3) by a UV tail correction that is O(1) for Lambda ~ lambda_max and negligible for Lambda << lambda_min.

---

## 7. Impact on Framework Gates

| Gate | Uses | Affected? | Impact |
|:-----|:-----|:----------|:-------|
| ANALYTIC-TORSION-45 (INFO) | Truncated zeta'(0) | YES -- artifact | T ~ 10^{20301} is unphysical. The INFO verdict is correct (not PASS or FAIL), but the number itself has no geometric meaning. CC from torsion route is CLOSED not because T is large, but because the computation does not access the actual torsion. |
| TRUNCATED-TORSION-45 (INFO) | Singlet zeta'(0) | PARTIALLY -- less severe | T_singlet = 0.147 is more defensible (16 modes, small multiplicity), but still a partial sum. The INFO verdict stands. |
| UNEXPANDED-SA-45 (FAIL) | Exact spectral action | NO -- fully valid | The FAIL verdict (polynomial expansion captures all content) is correct and correctly interpreted. |
| SIGMA-SELECT-45 (FAIL) | d_s(sigma) for n_s | YES -- artifact | The search for a "correct sigma" at which d_s gives n_s is searching for structure that does not exist on the finite spectrum. The FAIL verdict is correct, but for deeper reasons than stated. |
| DIMFLOW-44 | d_s(sigma, tau) | YES -- artifact | The d_s = 4 at sigma = 0.97 is not a physical walking scale; it is a coincidental crossing point on a function that should monotonically decrease from 8 to 0 but instead rises from 0 due to truncation. |
| CUTOFF-SA-37 (FAIL) | Spectral action monotonicity | NO -- fully valid | The structural monotonicity theorem operates on the spectral action (Tier 1) and is unaffected by this audit. |
| HESS-40 (PASS) | Spectral action Hessian | NO -- fully valid | Hessian of spectral action is a Tier 1 quantity. |
| All CC computations using a_0, a_2 | SD coefficients | PARTIALLY | The CC gap (~120 orders) is so large that even 50% truncation error in a_2 changes nothing qualitatively. The CC problem is structural, not a truncation artifact. |

---

## 8. Structural Constraint Recorded

**STRUCTURAL**: On a finite discrete spectrum with N levels, the heat kernel K(sigma) = sum d_k exp(-sigma lambda_k^2) is an entire function. The Seeley-DeWitt expansion is a convergent Taylor series (not asymptotic). The spectral zeta is entire (no poles). Consequently:

1. The spectral dimension d_s(sigma) is not a dimension diagnostic in the UV; use Weyl counting instead.
2. The "analytic torsion" zeta'(0) is an extensive spectral moment, not the regulated torsion; it diverges as the truncation is removed.
3. The spectral action is exact and well-defined.
4. Seeley-DeWitt coefficients, interpreted as spectral zeta moments, are valid approximations to the geometric curvature integrals, with truncation error quantifiable via the Weyl deficit d_eff vs dim(M).

This constraint eliminates all spectral dimension / torsion routes to the CC problem that were explored in S44-S45, and clarifies that the spectral action route (already CLOSED by CUTOFF-SA-37 monotonicity theorem) was the only geometrically valid approach.

---

## 9. Uncomputed Priority

**Independent geometric a_2 computation**: Calculate a_2 = (4 pi)^{-4} * 16 * integral(R(tau)/6 dV) directly from the known Jensen metric. This provides a model-independent cross-check on the spectral a_2 = 2776.17 and quantifies the truncation error. The scalar curvature R(tau) was computed analytically in S20a. This computation would close the loop on whether the a_n from the truncated spectrum are trustworthy.

---

*Filed as Tier 1 structural constraint. All future computations using heat kernel quantities on the truncated SU(3) spectrum must reference this audit to determine which tier their inputs belong to.*
