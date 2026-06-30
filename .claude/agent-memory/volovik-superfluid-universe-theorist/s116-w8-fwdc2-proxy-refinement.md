---
name: s116-w8-fwdc2-proxy-refinement
description: S116 W8-2 FWD-C2 PROXY-REFINEMENT DISCHARGED (PASS) — FULL-PV s=4 spectral moment reproduces the Casimir-bound proxy -7.046336 via multiplicative-normalization-cancellation; the layer pin resolves Reading A vs Reading B
metadata:
  type: reference
---

S116 W8-2 `S116-W8-FWDC2-LANDING` PASS (sign/mag/regime = PASS/PASS/VALID). Discharged the FWD-C2 `REGISTRY-INCOMPLETE-PENDING-PROXY-REFINEMENT` sub-class (CF-49). audit_sha256=`c79ee0dbdcef3612e2102226e6d151a7d2f891b23174967fc75990bb49b0a9b7`.

**The load-bearing methodology (re-use for any FWD-C2 / §VII.AV-adjacent gate)**: the substrate-IS observable `L_emp = d²ln Var_a(|v_a(K)|²)/d(ln K)²` at s=4 is single-pinned at `(M_2(C), P_BdG, s=4)`, but FULL-PV has TWO inequivalent F-images settled at the S91 W4 layer-orthogonality workshop (I was Reading-A defender) + my S93 W3-2 K=3 theorem:
- **Reading A = the PINNED layer** (`a_4^{Pauli-Villars}`, s=4 SPECTRAL MOMENT, poleconv-A-double n=0). PV regularizes the K-INDEPENDENT s=4 Mellin moment `M_PV(s=4)`, which enters as a multiplicative spectral-support weight. By [[multiplicative-normalization-cancellation]] (S93 W3-2; `math-scripts.md` MANDATORY K=3) `d²/d(lnK)²` annihilates it ⇒ `L_emp_FULL = kernel = proxy = -7.046336` EXACTLY (rel 7.33e-11). The Casimir BOUND bounded the WEIGHT; the FULL-PV moment refines the WEIGHT; the weight cancels ⇒ proxy is FAITHFUL at the observable level. Verified on L12 (M_PV=1321.56) AND L14 (M_PV=1333.26): weights DIFFER (ratio 1.0088) but L_emp_FULL identical (L_max-invariance residual 3e-10) — the binding evidence.
- **Reading B = orthogonal per-mode-dispersion layer** (S91 W5-1; PV mass-shifts `E_a^{(M_j)}=√(ξ²+Δ²+M_j²)`). Reproduced as cross-ref: **L_emp_permode = -527.966919** (75× the proxy; matches S91 W5-1 to 5.5e-8). Recovers proxy only as m_PV→0 (S93 W3-2 m_PV-axis flow). NOT the gate value — reporting it makes the PASS non-convention-shopping.

**Do NOT** conflate the two: the gate pins the SPECTRAL-MOMENT layer (`a_4^{Pauli-Villars}`), so Reading A is correct; the S91 −527.97 is the SEPARATE per-mode question, already classified orthogonal. The plan's track-B FAIL hypothesis ("M_3(C) Cartan-zone weight non-negligible, W11-5 ~21× pattern") is predicated on a NON-multiplicative weight — inapplicable, since the s=4 moment magnitude (however large) cancels.

**In-session fix**: promoted the proxy literal `-7.046336474406761` (used in s89/s91/s93) to `canonical_constants.py` as `L_emp_VII_AV_STATE_PROJ` + PROVENANCE (per `math-scripts.md §"Canonical Write-Order"`). Gap-IR kernel: the gap |Δ_a|=0.464 M_KK supplies the intrinsic IR scale so the curvature converges WITHOUT a UV cutoff — the gap DEFINES, the PV DRESSES.

Canonical homes (NOT this memory): verdict `computations/session-116/s116_gate_verdicts.txt`; the §VII.U.2 Corner-II Var_a `PROXY-REFINEMENT → binding` re-tag is `mack-cosmic-bridge`'s registry write. Origin -7.046336 is S87 W2-3, STAGE-3-PERMANENT §VII.AV.STATE-PROJ (S93 W3). See [[feedback-read-session-history]].
