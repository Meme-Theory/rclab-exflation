---
name: s115-w3-3-b5a-tfd-qes-overshoots-2a4
description: S115 W3-3 — two-sided TFD island QES OVERSHOOTS to 2A/4 (R_QES=2.0001), not A/4; closes the two-sided-island corridor; the B5A microstate gap is structural across ALL island mechanisms
metadata:
  type: project
---

S115 W3-3 (S115-B5A-TFD-QES, OPTIONAL Tier-3 NON-BLOCKING) replaced the closed-form linear bracket interpolant (which FAILed at every causal-patch route, S112/S114) with a GENUINE two-sided (TFD/eternal-island) quantum-extremal-surface extremization of S_gen^TFD = [Area(∂I_L)+Area(∂I_R)]/4 + S_bulk-EE(I_{L∪R}). Verdict: composite **INFO** (sign=PASS / magnitude=FAIL / regime=MARGINAL). audit_sha256=144fcde21b5d17838e4039c353f04cc6c8273393d92ff4b7159ca40a78f20078.

**The decisive result: R_QES = 2.000001 — the two-sided QES OVERSHOOTS to 2A/4, not A/4.** This is the eternal-black-hole result, not a numerical accident: the TFD/eternal geometry has TWO bifurcate horizons (L and R), total area 2A, so the doubled-island microstate count is 2A/4. |R_QES−1|=1.000 ≫ 0.25 → magnitude FAIL.

**Why (the monotonicity obstruction + TFD purification — load-bearing for any future B5A-island gate):**
- Single-sided S_gen(λ) = Area(∂I)/4 + S_bulk(I) is STRICTLY MONOTONE INCREASING (both are cumulative sums of non-negative spectral weights), so dS_gen/dλ=0 has NO interior solution. The S111 "QES" at R=0.987 was the TAUTOLOGICAL S_gen=A/4 crossing (DIAGNOSTIC-ONLY, NOT a stationary point). A genuine interior QES needs a SUBTRACTIVE λ-dependent term.
- Two-sided supplies it via cross-copy mutual info: S_bulk-EE(I_{L∪R}) = 2·S_bulk(I) − I(I_L:I_R). For a TFD, each island mode (k_L,k_R) is a 2-mode-squeezed pair → I_mode(n)=2·s(n) EXACTLY (L-R pair globally pure: S_L=S_R=s(n), S_LR=0).
- Substrate relic is a MAXIMALLY-SQUEEZED GGE (P_exc=1.000) → χ→1 (perfect TFD purification) → joint island bulk-EE VANISHES → S_gen^TFD = 2·Area/4, STILL monotone → QES at the BOUNDARY (maximal island = full slice) → saturates at 2·(A/4). The cross-copy entanglement PURIFIES AWAY the bulk-EE term that gave single-sided R_island=1.382.
- regime=MARGINAL (NOT VALID) is forced: no interior stationary point exists; the extremum is a degenerate boundary clamp at λ_max=5.419. A float-noise sign-flip at grid idx 294 (dS=−2.3e-10) was excluded by a physical NEG_FLOOR=1e-6·max|dS|=2.7e-2 discriminator. (Caught + fixed in-session: first run mis-tagged VALID via the raw sign-change, which would have made composite FAIL; the correct MARGINAL gives composite INFO per the gate-verdicts.md collapse mag=FAIL∧regime=MARGINAL⇒INFO.)

**B5A microstate-gap is STRUCTURAL — corridor CLOSED on all island mechanisms.** A/4 is NOT reachable by ANY island-QES mechanism tried:
- S110 edge-only: R_edge = 0.526 (~½ undershoot)
- S111 single-sided full bulk-EE: R_island = 1.382 (OVERSHOOT)
- S112/S113/S114 causal-patch linear interpolant: R_TFD = 0.535 (undershoot, f_bulk≈0.0098)
- S115 two-sided perfect-TFD QES: R_QES = 2.000 (OVERSHOOT by the second horizon)
Substrate-first reading: A/4 is the FULL emergent horizon area count; the GGE-relic island entropy is a DIFFERENT spectral functional (relic-occupation EE on the L12 D_K spectrum). They coincide only at the tautological crossing, not structurally. This completes the B5A bracket quartet S110/S111/S112-114/S115. Tier-3 NON-BLOCKING (atlas-08 internal-consistency only; no falsifier-row update).

**Reading ladder (χ-bracket, honest disclosure):** (L1) independent copies χ=0: R_full=22.30 (massive overshoot); (L2) perfect TFD χ=1 CANONICAL: R_full=2.0000 (gate operator); (L3) radiation-island complement-EE min-QES: R=2.0000 (Page-curve construction also saturates at 2A/4 once complement EE exhausted). Constructed on s111_b5a_island.npz + s84_spectrum_cache_L12_tau019.npz; c_conical=0.25=a_2^{Pauli-Villars}; A/4=17806.5658.

Relates to: [[s114-w4-2-b5a-tfd-two-sided-closes]] (the PRIOR linear-interpolant FAIL this gate replaces — that was the causal-patch f_bulk^TFD route; THIS gate is the genuine-QES route, and it OVERSHOOTS where the interpolant undershot), [[s112-w3-1-b5a-bracketed-causal-patch-closes]], [[s111-w4-1-island-overshoots-a4]], [[s110-w4a1-microstate-boundary-vs-bulk]].
