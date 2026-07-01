---
name: s96-w3-cgwb-flagship-retirement
description: S96 W-3 workshop closure — the §7.2 acoustic-CGWB GW-detector flagship is RETIRED (GW→LSS migration); Omega_GW_Lambda_A_LISA=1e-10 is PENDING-SUBSTRATE-RECOMPUTE; slope-independent LISA bound <1e-42
metadata:
  type: project
---

# S96 W-3 — Acoustic Ω_GW GW-detector flagship RETIRED (GW→LSS migration)

**Workshop**: `sessions/archive/session-96/workshops/w3-omega-gw-acoustic-spectral-shape.md` (little-red-dots ∧ mack, 2026-05-30). Topics 1-3 Converged, Topic 4 Emerged (GW→LSS migration).

**Why**: The §7.2 LISA-CGWB "flagship" (`Ω_GW^(A) ~ 1e-10` at 3 mHz, "SNR ~10¹³") was a number-vs-prose drift W8-2 left open. W6-3 (`S96-OBS-CGWB-PEAK-FREQ`, audit `646e6ad0…`) derived the peak at `f_peak = 8.4835e39 Hz` (redshift-chain, GHz+ across the whole swept κ band) — 42.45 decades above the LISA pivot. The `1e-10` was a Case-A provenance-less pivot placeholder under an assumed peak-at-3-mHz (no PROVENANCE entry; fires Class-(f) PIN-PLACEHOLDER + Class-(c) PIN-DRIFT-FROM-STALE-SOURCE, W6-3 the supersession event).

**How to apply** (permanent dispositions, all Sage-verified):
- **GW-detector-STERILE, slope-independent + UNCONDITIONAL**: for ALL causal `p ≥ 1` with `Ω_peak ≤ O(1)`, `Ω(LISA) ≤ 10^(−42.451454) < 10⁻⁴²`, ≥ 29.45 OOM below LISA-PLS. No causal `p` revives the flagship. Peak is 28.93 decades above the HF ceiling (≲10¹¹ Hz) → above LISA(mHz) AND PTA(nHz) AND HF. Publish the bound as the INEQUALITY `< 10⁻⁴²`, NEVER `≈` (would understate by 0.45 OOM).
- **The acoustic falsifier MIGRATES GW→LSS**: live = first-sound BAO ring (Row #72, `S96-OBS-FIRST-SOUND-RING`, PASS, `A_FS=0.204`, k₁=0.0193 Mpc⁻¹, r₁=325.30 Mpc, **SNR 8.6341 DESI-5yr** / 5.0789 DR1, audit `b74ccd56…`, no ΛCDM counterpart) + f·σ₈ (Row #71, INFO, −4.06% S₈-relieving).
- **`Omega_GW_Lambda_A_LISA = 1.0e-10` → `PENDING-SUBSTRATE-RECOMPUTE`** in BOTH inventory (Row #7.audit-3) AND `canonical_constants.py` PROVENANCE (lines ~2490 + 2504 + aliases 2510-2512). VALUE HELD (no derived Ω_peak yet; import must not break), NOT deleted (IR-tail amplitude is a real observable). 3 aliased pins inherit the flag.
- **Two SURVIVING structural companions** (STRUCTURAL-ORTHOGONAL-COMPANION, never co-primary), each guard-tagged `[STRUCTURAL — NOT detector-testable]`: wall=0 (`Ω_GW^{walls}=0` EXACTLY, π₀(U(1))=0, W6-4) + (A)/(C) split `47.081` (Sage `47.080974235`; `Ω_GW^(C)=8.299e-58`, `log10 Ω^(C)=−57.081` — note R3 prose said −58.08, a one-decade slip; the split 47.081 is unaffected).

**Landed (mack sole-writer)**:
- capstone §7.2: `phonic-exflation-equation.md` line 542 (lead note), line 550 (Row #7 retired), line 551 (NEW Row #8 BAO ring). Did NOT touch §7.3 (~558), §6.3, §5.3, §7.1.
- `falsifier-master-inventory.md` line 1574: NEW Row #7.audit-3 (supersedes Row #7.audit-2 (a) "UNCHANGED LIVE 1e-10").
- `canonical_constants.py` PROVENANCE annotation (value held; import verified `IMPORT OK`).

**S97 carry-forward (two-gate, reframed purpose = produce honest re-pin VALUE, NOT test survival)**: `S97-OMEGAGW-PEAK-HEIGHT` (mack: derive Ω_peak from fold DOS at f_peak — CANNOT come from placeholder pivot, back-out = 10^117 unphysical) FEEDS `S97-OMEGAGW-ACOUSTIC-SPECTRAL-SHAPE` (little-red-dots: derive IR slope p, propagate to LISA, re-pin). The L4 `Omega_peak_source: ADJUDICATED_IN_W3` pin was RETRACTED → `S97-OMEGAGW-PEAK-HEIGHT`.

**Open cross-section CF (NOT mine — §7.3 scope)**: capstone §7.3-region "Headline test: LISA's CGWB … SNR ~10¹³" callout (~line 559) still narrates the GW flagship at full confidence; routed to §7.3 designated writer.

Links: [[key-constraints]], [[project_s96_3register_section7_surface]], [[project_omega-gw-roundfigure-fidelity]] (the DISTINCT 1.205×/0.081-OOM (C)-class fidelity item, NOT the 127-OOM (A)-class defect), [[project_bao-substrate-emergent-transport]] (the first-sound ring channel).
