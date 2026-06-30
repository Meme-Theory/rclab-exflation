# atlas-08 Freshness Reconciliation — S98 closures (2026-06-01)

**Purpose**: backing audit for the `S98 freshness update` bullets appended to
`sessions/framework/Atlas/atlas-08-open-questions.md` at the S99 plan-freeze
(`/rclab-plan` Step 1c-REGISTERS.MAINTAIN). Originals are preserved verbatim per the
atlas-08 §V convention ("originals preserved; closures recorded as updates"); this file
records WHICH entries S98 advanced and the verdict provenance, so the bullets are
traceable to `computations/session-98/s98_gate_verdicts.txt` (11 gates) — no invented
closures.

**Source session**: S98 (6 compute waves; verdict file `s98_gate_verdicts.txt`; six
per-wave WPs `session-98-w{1..6}-workingpaper.md`; housekeeping `session-98-housekeeping.md`).

---

## Entries advanced by S98

| atlas-08 Q | S98 event | Verdict (audit short) | Net status |
|:-----------|:----------|:----------------------|:-----------|
| **Q13** (What maps τ-evolution to cosmic time?) | W1 `S98-W1-ROUTE-RECONCILIATION` FAIL (composite): AOFT covariant spectral-action route pinned as the **a₂-canonical acoustic frame** (Clause-1 PASS — VOL/GFT route-vs-AOFT residual 1.13e-18 M_KK², no independent a₂-content) + τ̇-shape uniquely pinned (sub-gate PASS); but the AOFT acoustic frame is conformally **STATIONARY** (a_eff rel-var 7.4e-7) so q_Ω is a genuine 0/0 (Clause-2 FAIL). | `75a45dd7` | **C1 stays ASSUMED.** Live residual moves from "route-invariance" to "non-ratio deceleration observable on the stationary frame" → CF-S99-W1-Q-OBSERVABLE-REDERIVE. |
| **Q18b** (Yukawa hierarchy beyond rank-1) | W3-1 `S98-W3-1-YUKAWA-EPS-LX-BETWEEN-GEN` PASS: an order-one-admissible (incremental=0 EXACT — the unique corridor per §VII.BL E1), non-gauge-removable (P_nLI>0) external non-LI ε_LX EXISTS on the multiplicity bundle and lifts the multiplicity-scalar degeneracy sign-locked; band reached 0.0 dex by a 2-eq closed-form FIT ⇒ hierarchy NUMBER HELD (NON-PROMOTION-BY-HELD-NUMBER). | `b8487bc8` | **STILL OPEN at the NUMBER**; corridor existence-PASS. Successor opening: derive ε_LX from a substrate principle (CF-W3-2 / ε_LX-SUBSTRATE-DERIVE, EVOI rank-9b standing gap). The **seesaw** route (Σm_ν vs DESI < 0.072 eV) — flagged at S97 as the live opening — is elevated to an **active S99 wave** (register-sourced, 1c-REGISTERS.CONSUME). |
| **Q29** (BBN-VOLOVIK-67 structural sharpening) | W2 `S98-MK3-1-C10-SUBLEADING-SIGN` PASS (TYPE-A from-below sub-leading sign PINNED) + `S98-MK3-2-BBN-VACUUM-FRACTION` FAIL: from-below relief DIRECTION confirmed but MAGNITUDE insufficient — (ρ_vac/ρ_rad)_BBN=0.474 > 0.227, ΔN_eff=2.087 > 1. | `0870e1a3` / `1ad846b2` | **STILL OPEN (BBN-arm tension)**; the −0.022 from-below shift relieves but does not rescue the n_eff<2 BBN over-contribution → CF-S99-W2-BBN-ADDITIONAL-RELIEF (quantify residual ~2.1×). C10 stays ASSUMED-PARTIALLY-PROVEN. |

## Companion advances (not atlas-08-numbered — recorded for provenance)

- **C10 Object C** (relaxation closure): W2 `S98-W2-2-RELAXATION-CLOSURE` PRE-REG-INC mechanical closure (`3c46b5ea`) — upstream-blocked by the W1 conformally-stationary frame; friction-ODE machinery correct, H(τ) input degenerate → CF-S99-W2-RELAXATION-NONSTATIONARY-H (Tier-1). Atlas-04 C10 unchanged.
- **Baryogenesis #9** (atlas-04 C6): W3-2 `S98-W3-2-BARYOGEN-UNIQUENESS` PASS (`3be22b8a`) — existence→uniqueness: substrate-FIXED (ε_nLI=ε_K7²/n_pairs, φ_CP=π/2) → UNIQUE η_B=4.52e-11; φ_88-Cartan the UNIQUE non-leptophilic CP-source. Atlas-04 C6 stays CONDITIONAL (η_B still under-produced vs 6.12e-10 obs by ~1.1 OOM; the sourced prediction is sharpened, not the observation matched).
- **OQ3 / BF-spine** (mack §7 falsifier surface): W4-4 `S98-W4-4-OQ3-COVARIANCE` PASS (`0814c57f`) — 4 spine factors pipeline-INDEPENDENT (max|Corr|=0); rank-2 dagger LICENSED; BF_spine → DECISIVE (2000); `oq3_orthogonal_established=True`. Landed to `falsifier-master-inventory.md` + capstone §7 by mack in-session (dispatch `ada676fd`, housekeeping §A7) — NOT re-edited here.
- **κ-determinacy** (mack §7): W4 `S98-KAPPA-INDEP-FROM-CGWB-FREQ` FAIL (`10d31d0e`) — CGWB-frequency axis detector-sterile; κ stays CONSISTENCY-PINNED (no §7 status change; mack-landed). → CF-S99-KAPPA-ALT-OBSERVABLE-SCAN.
- **§8.5 a₀/a₂ tier-2** robustness: W5 `S98-A0A2-TIER2-PV-INVARIANCE` INFO (`4522ea7e`) — survival LABEL regulator-INVARIANT; residual RD localized to the L_max axis (d_PV=0.0570) → CF-S99-W5-A0A2-LMAX13.

---

*A full atlas-08 re-stamp to "Through S98" awaits the next `/weave --update`. This file is the
interim S98 freshness record per the same pattern as `atlas-08-freshness-S97.md`.*
