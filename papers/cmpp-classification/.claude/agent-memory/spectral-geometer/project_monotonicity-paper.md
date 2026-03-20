---
name: Monotonicity paper revision
description: Key structural decisions and fixes applied to papers/monotonicity/main.tex during peer review revision
type: project
---

Paper: `papers/monotonicity/main.tex`

**Central revision (2026-03-20)**: Theorem 2 (Structural Monotonicity) weakened from "all monotone f" to:
- Part (i): mean eigenvalue squared increasing (PROVEN by computation)
- Part (ii): S_f monotone for COMPLETELY MONOTONE f (proven via Bernstein's theorem + heat kernel monotonicity)
- Part (iii): 10 representative cutoffs verified computationally (9,600 checks)
- Part (iv): No minimum for any of the above

**Why:** 288/1232 eigenvalues (23.4%) decrease individually. The old proof claimed universality for all monotone f but only verified finitely many. Bernstein's theorem (completely monotone = Laplace transform of positive measure) provides the correct proof pathway since heat kernel inherits monotonicity from the dominant increasing eigenvalues.

**How to apply:** Any future claims about spectral action monotonicity must distinguish completely monotone cutoffs (proven) from general monotone cutoffs (conjectured, Remark rem:general-monotone-conjecture).

Other fixes applied:
- a_4 monotonicity: "verified analytically" changed to "evaluated at 100 tau-values"
- Jensen's inequality: sqrt(x^2+y^2) is CONVEX (a norm), not concave. Argument restructured.
- a_2 convention footnote added (Gilkey vs Vassilevich, monotonicity independent of normalization)
- Higher sectors "reinforcing": weakened to "expected but not proven in general"
- Connes 2019: "address the open problem" -> "provide partial results toward the open problem, for one specific deformation family on one manifold"
- Bar1996 -> Bar1992 (bibtex key/year mismatch)
- Abstract rewrites separating geometric a_2 (increasing) from effective hat{a}_2 (decreasing)
