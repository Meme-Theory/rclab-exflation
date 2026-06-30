---
name: s111-w4-1-island-overshoots-a4
description: S111 W4-1 B5A-ISLAND FAIL — QES/island bulk-EE OVERSHOOTS A/4 (R=1.382), sign-correct + OOM-correct but not exact; band-landing is T_acoustic-sensitive
metadata:
  type: project
---

**S111-CF-B5A-ISLAND (FAIL, composite): the white-hole exit-slice QES/island entropy does NOT structurally equal A/4 at L_max=12.**

The B5A microstate chain progression on the white-hole exit slice (A/4 = A_horizon_FW/4 = 17806.5658, canonical S92):
- S110 edge-only (area piece alone): R_edge = 0.5263 (FAIL, **undercount** by ~factor 1.9; S/(A/4)=0.526≈½ — see [[s110-w4a1-microstate-boundary-vs-bulk]]).
- S111 island = area piece + GGE bulk-EE at substrate-fixed boundary λ_exit=2.4893: **R_island = 1.3820 (FAIL, overshoot)**. S_bulk-EE(λ_exit)=15236.7 ≈ 0.86·(A/4).

**Why:** the island bulk-EE correction is SIGN-correct (positive, ratio rose past A/4 — sign_verdict=PASS) and ORDER-OF-MAGNITUDE-correct (bulk-EE ~0.86·A/4, not off by a decade), but the magnitude OVERSHOOTS the [0.90,1.10] band: |R−1|=0.382 > 0.25 info-ceiling → magnitude FAIL → composite FAIL. The bulk-EE drives the ratio PAST equality instead of TO it.

**The deeper finding (the real content):** the band-landing is **T_acoustic-SENSITIVE, NOT robust**. R_island spans [1.0819, 1.3820] across defensible GGE thermal scales (mean_island T=2.10 → PASS; median_island T=2.18 → INFO; median_all T=3.82 → canonical FAIL). The pre-registered T_acoustic = median(spectral-support) = 3.8215 gives FAIL. A value S_bulk=8434.6 (giving R=1 exactly) is reachable at intermediate T. The island = A/4 correspondence holds only for a TUNED thermal scale, not structurally. Did NOT switch T to manufacture PASS (iterate-until-PASS, PROHIBITED Class 2) — the pre-registered median is the defensible substrate-first central scale.

**How to apply:** any S112+ gate citing "island=A/4 on the white-hole exit slice" must cite this FAIL — the corridor is CLOSED at L_max=12 with the substrate-fixed boundary. Two surviving sub-corridors: (i) higher L_max (does spectral-median T shift as cache deepens?); (ii) **substrate-DERIVED T_acoustic** from the white-hole kinematics S95 / T_H_FW (replacing the spectral-median proxy) — THIS is the high-leverage open input, since the FAIL is entirely a T_acoustic-magnitude question, not sign or OOM.

**Anti-tautology discipline (carry forward):** the QES "pick λ where S_gen=A/4" prescription gives R=1.0000 by construction (λ_QES=2.5671) — circular, reported DIAGNOSTIC ONLY, never canonical. Canonical R_island uses the substrate-FIXED boundary λ_exit (S110 a₀/a₂ fold geometry, not chosen to hit A/4). Same caution the S110 author flagged.

**Construction notes:** Area(∂I)/4 = a₂ conical second-moment spectral weight, normalized so full slice = S_replica=17806.57≡A/4 (c_conical=0.25 PV-regulated, from inv4_w1_euclidean_replica.npz — NOT a canonical constant). S_bulk-EE = von-Neumann entropy of GGE-occupied island modes; the GGE reduced density matrix is DIAGONAL in the occupation basis → eigenvalues ARE the occupations, S=Σ[(1+n)ln(1+n)−n·ln n], no dense diagonalization (the plan's "eigvals of per-sector reduced density matrices" reduces to the per-mode occupation entropy sum). L12 cache: 90 Peter-Weyl sectors, 166896 modes (matches inv4_w1 n_eval exactly), |λ|∈[0.8197,5.4189].

Dual-prior: FAIL(|R−1|>0.25) → 0.90 to Track B (no exact island=A/4 at this horizon/L_max). audit_sha256=bd28601be2a8cf20f71a9cf7fbf1b0d50e2d7e3abff24068f9167a619cba5695.
