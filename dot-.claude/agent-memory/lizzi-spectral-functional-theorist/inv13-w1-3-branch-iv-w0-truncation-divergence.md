---
name: inv13-w1-3-branch-iv-w0-truncation-divergence
description: Zubarev late-time w0 functional DIVERGES under deep truncation on the branch-(iv) channel (spread_CAC FAIL at L{12..16}); offset-cancellation identity is FUNCTIONAL-INDEPENDENT, the divergence itself is SCHEME-DEPENDENT
metadata:
  type: project
---

INV13-W1-3-BRANCH-IV-W0-L1516-DR3 (investigation-13, 2026-06-17): FAIL. The branch-(iv) late-time w0 prediction is truncation-UNSTABLE on the L_max axis.

**Spectral functional used**: Zubarev (heat-kernel-Gaussian-weighted) late-time moment rho_B(L) = <|lambda|>_Z/lambda_max − 1, w_Z = exp(−|lambda|²/Λ_Z²), Λ_Z=1.0 M_KK; CAC binding form w0^CAC(L)=rho_B(L)+offset_B, offset_B := w0_FW − rho_B(L=10) (regulator-convention-lockdown.md; RDC FORBIDDEN).

**Result**: spread_CAC over L∈{12,13,14,15,16} = **0.0629703 > 0.05** → FAIL (band PASS≤0.025 / INFO(0.025,0.050] / FAIL>0.050). rho_B monotone-DECREASING: −0.633(12) → −0.657(13) → −0.678(14) → −0.696(15); decrements −0.0237/−0.0208/−0.0185 decelerating-but-NOT-closing. The S105 hope (Friedrich-Bär tail pulls spread <0.025) is FALSIFIED — adding L=15 GREW the spread +0.018456 (L=15 is the new minimum). Extends/supersedes the optimistic reading of S105-BRANCH-IV-DIRECT-L1314 (INFO 0.0443091 over {12,13,14}).

**PERMANENT FUNCTIONAL CLASSIFICATION (my directive)**:
- **FUNCTIONAL-INDEPENDENT**: the offset-cancellation identity spread_CAC = spread_rho = max_L rho_B(L) − min_L rho_B(L). offset_B is L-independent ⇒ cancels EXACTLY in any max−min difference, for ANY additive anchor (CAC or RDC). Verified machine-ε: |spread_CAC − spread_rho| = 1.11e-16. The CAC↔RDC choice changes per-L anchored VALUES but NOT the spread.
- **SCHEME-DEPENDENT**: the DIVERGENCE itself. spread_CAC>0.05 is a property of the **Zubarev late-time functional** on the branch-(iv) channel. A different late-time w0 moment-functional could in principle converge where Zubarev diverges — the late-time-functional choice is a regularization DOF. But CAC lockdown pins the functional for DR3-class gates, so within the pre-registered scheme the divergence IS the canonical result.

**Scope discipline**: truncation-stability axis ONLY. Does NOT retract branch-(iv) derivation-admissibility (separately closed S101-W0-BRANCH-IV-EVALUATOR INFO). Says only: the secondary R_842-window w0 prediction is not DR3-defensible on this branch (DESI DR3 ~2027). Closes optimistic Track_A; EVOI Q37 (DESI DR3 / branch-iv) updates to "deep-truncation DIVERGES".

**Data/feasibility lesson**: consumed S106 high-L cache (s106_w1_highl_cache_l1416.npz) — PRE-BUILT eigvals (GT (p,0)=Sym^p(C³) builder lifted the dense-3^p wall at S105; cuda:0 diag done at S106). L=16 Friedrich-Bär-SATURATED at operational L=15: the 17 level-16 sectors are FB-bounded (eta_FB_lower=0.3928, |lambda|_min ≥ eta_FB_lower·√(C₂+1) > bottom-K ceiling), absent from cache ⇒ rho_B(16)=rho_B(15) EXACTLY. L_max_plan={14,16}, L_max_operational=15.

**(4,4)-completeness gotcha (reusable)**: the s84 cache (s84_spectrum_cache_L12_tau019.npz) is MISSING the level-8 sector (4,4) (8/9 sectors at level 8 — an S84-era gap). S106 rebuilt it (dim=125). So rho_B(12) on the COMPLETE S106 dict (−0.633204) ≠ rho_B(12) on the s84-incomplete set (−0.634885, the S105/EXPECT_RHO basis) by 1.68e-3. This is a SECTOR-SET difference (both correct on their own set), NOT an evaluator failure. Apples-to-apples continuity uses the SAME incomplete s84 set. Future deep-truncation rho_B gates: use the COMPLETE per-level S106 union (p+q≤L literally), and do NOT spuriously guard against the s84-incomplete S105 record.

Links: [[permanent_theorems.md]] (three-layer regulator: zeta L1 / Zubarev L2 / observable L3 — this is the Zubarev L2 layer's DR3-truncation test), [[sessions_s78_s83_results.md]] (S83 Zubarev L2 minimizer). w0_FW=−0.918 (S58 four-fold-lock; canonical name w0_FW, NOT w_0_FW).
