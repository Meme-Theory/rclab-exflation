---
name: Dirac Spectrum PW Scaling Law
description: Exact scaling law for Dirac eigenvalues on (SU(3), g_Jensen) vs Peter-Weyl truncation. Key for any future spectral action computation.
type: project
---

S51 HIGH-PW-51 established the eigenvalue scaling law at the fold tau=0.19:

**max|lambda| = 0.633 * sqrt(C2(p,q)) + 0.555 M_KK** (RMS = 0.046)

Where C2(p,q) = (p^2+q^2+pq+3p+3q)/3 is the quadratic Casimir.

Key numbers:
- max_pq_sum=6: R=3.175 M_KK, 791 distinct eigenvalues, 28/28 sectors, 4.5s
- max_pq_sum=8: R=3.922 M_KK, 1785 distinct eigenvalues, 42/45 sectors, 86s
- k(tau=0.19) = 0.790 +/- 0.039 (ratio max|lam|/sqrt(C2) for C2>5)
- Reaching R=12 M_KK requires max_pq_sum ~ 30

**Why:** The spectral action at Lambda ~ 12 M_KK needs eigenvalues at that scale. The sqrt(C2) growth means N=30 is needed, not N=12 as one might naively expect.

**How to apply:** Any future spectral action computation at large cutoff Lambda should either:
1. Implement weight-space irrep construction (O(dim^2), not O(3^p)) to reach N=30
2. Use the asymptotic eigenvalue distribution model from s51_high_pw.py

Structural result: n_s(Lambda) > 1 at ALL finite Lambda for the bare Dirac spectrum on compact 8-manifold. The Planck value n_s=0.965 is unreachable from heat kernel of the internal space alone.

The 3 failed sectors at N=8 ((3,4), (4,4), (3,5)) are from _build_irrep_no_cache not supporting mixed conjugated reps where the recursion hits (q,p) with q>p>0 and needs building (p-1,q). Fix: extend _build_irrep_no_cache to handle general (p,q) with p>=q via same recursion as get_irrep.
