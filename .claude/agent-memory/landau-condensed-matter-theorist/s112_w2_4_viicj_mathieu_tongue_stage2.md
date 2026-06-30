---
name: s112-w2-4-viicj-mathieu-tongue-stage2
description: Stage-2 Axis-B (Mathieu-tongue/monodromy band-stability) NON-AUTHOR verify of §VII.CJ — both clauses PASS; convention-independence of tongue exponent proven symbolically
metadata:
  type: project
---

S112 W2-4 (CF-S112-VIICJ-STAGE2): Axis-B cross-axis independent-verify of STAGE-1-CANDIDATE §VII.CJ (McLachlan tongue-half-width cutoff-robustness EXPONENT theorem confirming §VII.BP DEAD at any L_max>=12). My axis = Mathieu-tongue / monodromy band-stability. **Both clauses PASS.**

**Why (the physics, for future reuse):**
- The n-th Mathieu instability tongue (`y'' + (a - 2q cos2x)y = 0`) sits about `a=n^2`; its half-width vanishes as `q->0` with order EXACTLY n. From DLMF-28.6 exact-rational series: n=1 full width `2q - q^3/32`; n=2 `q^2/2 - q^4/18`; n=3 `q^3/32`. So `degree_q == n` for n=1,2,3 (Sage-verified). Half-width leading coeffs `[1, 1/4, 1/64]` = registered DIAGNOSTIC `q, q^2/4, q^3/64`.
- **Convention-independence (the load-bearing structural point):** the exponent IS the order of vanishing at q=0. Under any reparametrization `q->lam*q` (cos2x vs 2cos2x; q vs 2q), `Delta(lam q) = (c_n lam^n) q^n + ...` — power n INVARIANT, coefficient rescaled by lam^n. Hence `degree_q==n` is conventionless; the x16 / q^3/64 / q^2/4 coefficients are convention-DEPENDENT => correctly DIAGNOSTIC-ONLY, NOT registered.
- **Band-stability = no-overlap:** a Hill/Mathieu mode at parameter A is in a stability band (`|Tr M|<2`, `Re mu=0`) iff detuning `|A-n^2| > half-width`. Independently recomputing half-width as `c_n q^n` from MY OWN coefficients (not the stored npz field) and comparing to `dist_to_zone_A`: **0/1248 overlaps**. Worst-case `i_closest=1168` (A=9.000371, zone n=3): my half-width 8.14e-10 vs detuning 3.71e-04, margin **5.66 decades**. Direct monodromy: `max|Tr M|_relic = 1.99999996 < 2`.

**INFO note:** npz `tongue_halfwidth_relic` stores `q^3/32` (FULL width) at the worst-case mode = 2x my prefactor-correct half-width `q^3/64`. Labeling matter, not a defect — certificate holds either way; my (tighter) value gives the LARGER margin (5.66 vs registry's ~5.4 decades). Mnemonic-vs-exact confirmed: bare `(q_M)^3=1.445e-07>1e-7` (plan mnemonic fails literal bound at broad-band-max q_M=5.248e-3, mode 1247 in zone n=4); prefactor `(q_M)^3/64=2.26e-09<<1e-7` load-bearing. Registry discloses correctly.

**Structural reading:** the no-re-pumping fact is L_max-extension-ROBUST by construction — higher Casimir => higher A => higher-n zone => more-suppressed (`q^n`) tongue. Finer truncation STRENGTHENS the protection, never weakens it. This is a substrate-IS spectral-geometry fact (D_K Casimir ladder -> A placement -> tongue exponent -> |Tr M|<2), Level-1 single-tau-slice, intra-pillar PHONONIC. Related: [[framework-constants]] (Ordered Veil S_ent=0, GGE relic).

Deliverable: `computations/session-112/s112_viicj_stage2_axisB_landau.json` (overall_axis_verdict=PASS). Scripts: `_landau_nooverlap_check.py`, `_landau_inspect_npz.py`.
