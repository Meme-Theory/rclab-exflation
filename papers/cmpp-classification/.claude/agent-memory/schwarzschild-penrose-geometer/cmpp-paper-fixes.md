---
name: CMPP paper peer review fixes
description: Eight corrections applied to main.tex from peer review, including critical eigenvalue and table fixes
type: project
---

Applied 8 fixes to `papers/cmpp-classification/main.tex` on 2026-03-20:

1. **Weyl eigenvalues at tau=0**: Corrected from {-1/8 (mult 8), 0 (mult 20)} to {-5/28 (mult 8), +1/14 (mult 20)}. Old values violated trace-free condition. Derived from Lambda^2(8) = 8 + 10 + 10bar decomposition via Schur's lemma.

2. **Table 1 values**: Recomputed from closed-form expressions. Key corrections: R(0.5) = 2.2884 (was 3.6497), K(1.0) = 4.777 (was 47.17). Removed tau=1.5 and 2.0 rows. Verified at tau=0: R=2, Ric2=0.5, K=0.5, C2=5/14.

3. **Table 2 eigenvalues**: All tau>0 rows violated trace-free. Replaced with tau=0 exact values only + note that tau>0 requires numerical diagonalization of 28x28 Weyl operator with trace-free and norm constraints.

4. **Type D proof Kulkarni-Nomizu gap**: Added explicit treatment of KN subtraction terms. Block-diagonal Ric (Ric_{mu a}=0) ensures mixed Weyl components from KN product have bw=0 only.

5. **WAND location**: Changed from "lies in flat external factor" to "spans null 2-plane with components in both external and internal factors" (consistent with alpha=pi/2 in eq 14). Fixed in abstract, Section 4.1, Section 6 discussion, and conclusion.

6. **Weyl dimension**: Corrected 301 to 300. Formula: n^2(n^2-1)/12 - n(n+1)/2 = 336-36 = 300.

7. **NEC statement**: Changed from "NEC violation on internal manifold" (Riemannian, meaningless) to NEC violation on full 12D Lorentzian product for null vectors with internal spatial projection.

8. **Theorem 5 to Proposition**: Sign-change hierarchy critical tau values found by numerical bisection, not proven analytically. Added "determined by numerical bisection to precision 10^{-14}."

**Why:** Peer review identified internal inconsistencies (trace violations, formula/table disagreements) and logical gaps.
**How to apply:** If returning to this paper, verify tau>0 eigenvalues with actual 28x28 diagonalization before adding them back to Table 2.
