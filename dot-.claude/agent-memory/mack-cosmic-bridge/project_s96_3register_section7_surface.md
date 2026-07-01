---
name: s96-3register-section7-surface
description: S96 W8-2 — the §7 "now" observable surface is split into 3 epistemic registers (robust/conditional/falsified); dual-status straddle disclosure rule; W6/W7 falsifier-row consolidation
metadata:
  type: project
---

# §7 observable surface — 3-register epistemic stratification (S96 W8-2)

**Decision**: the capstone §7.1 "now" table is now split into **3 epistemic registers** (the external review flagged the flat table for "visually flattening conditional and unconditional claims into a common rhetorical register"). The 3-register split is the PRIMARY §7.1 view; the flat 14-row table is retained below as a "flat reference."

**Why**: a referee must read each framework claim at its TRUE epistemic register — the zero-parameter robust spine must be visually separated from conditional forecasts and live wagers. Gate `S96-CONSOL-3REGISTER-TABLE` (INFO, audit_sha256 `014aea22…`; supersedes `ba39384d…` per Option A, a script-bug pipe-escape fix).

**How to apply**: when a NEW §7 observable lands, assign its register by the **categorical function of its W8-1-reconciled status tag** (NOT by eye):
- **Register A — ROBUST-STRUCTURAL**: status ∈ {PROVEN, PASS-structural, DISSOLVED-favorably, BOUND-Gaussian-by-Wick}. The no-borrowed-H joint-BF spine. Current members (7): CC closure, r, f_NL (Gaussian-by-Wick BOUND), σ/m=0, f·σ₈, ν mass ordering, c_s²=0.
- **Register B — CONDITIONAL**: status ∈ {CONDITIONAL, SCHEME-DEPENDENT, route-dependent, doubly-conditional, VIABLE}. Current members (6): w₀, n_s, α_s, m_H (dual-status), Ω_DM h², σ₈.
- **Register C — CURRENTLY-FALSIFIED**: status ∈ {BROKEN, advancing-tension, INVERSION-falsified}. Current member (1): w_a=0 (C5 BROKEN, 3.43σ — the live wager).

**SUM-check (no-flattening predicate)**: |A|+|B|+|C| == |§7.1 rows| (exact; no omission, no double-count); ZERO BROKEN/CONDITIONAL rows in Register A. Each row keeps its substrate-moment-layer tag (a₀/a₂/a₄). Producing script: `computations/_shared/s96_consol_3register_table.py` (the 14-row ROWS list + `is_non_robust_status` predicate is the canonical source — extend it when the table grows).

## Dual-status straddle disclosure rule (the honest INFO)

When a row legitimately straddles TWO registers (robust on one axis, conditional on another), place it in **CONDITIONAL with an explicit dual-status annotation** — NEVER flatten it into robust. This is the gate's INFO_meaning, NOT a flattening.

- **Inaugural instance: m_H** — robust-on-MAGNITUDE (~2% theory budget PASS vs PDG) but conditional-on-ROUTE (zeta 138.5 GeV excluded; μ_BC 188 GeV is an ACCOMMODATION, not a prediction). → CONDITIONAL, disclosed. This is why W8-2 closed INFO not PASS.

## W6/W7 falsifier-inventory rows landed (canonical write-order Step 3; mack sole writer)

`falsifier-master-inventory.md` (sole-writer surface):
- **Row #71** — f·σ₈(z) RSD: −4.058% f·σ₈ PRODUCT suppression (bare-f −0.311%, **C5 conflation guard**), S₈-relieving sign; DESI-5yr→Euclid (σ-dist 1.013/1.534). W6-1 PASS.
- **Row #72** — first-sound BAO ring A_FS=0.204=c₂²/c₁², NO ΛCDM counterpart; SNR 8.6 (DESI-5yr) / 5.1 (DR1). W6-2 PASS. Contrast: per-branch sub-feature A_obs_B1=1.445e-3 is OUTSIDE rulers BY DESIGN (0.60× DESI-DR2) — scope "far below rulers" to the SUB-FEATURE, not the ring (141× it).
- **Row #73** — ν normal ordering B1<B2<B3, zero-param, dynamical τ=0.107 (1,1,0)-crossing; JUNO/DUNE. W7-5. (The neutrino sector was ABSENT from the inventory before this.)
- **Row #7.audit-2** — CGWB peak-FREQUENCY scope-correction (W6-3 FAIL, D4 resolved AGAINST mHz): LISA samples the Ω_GW IR-tail AMPLITUDE (Ω_GW^(A)~1e-10, live), NOT the spectral PEAK (f_obs=8.48e39 Hz, GHz+, 43.9 decades above LISA). Read Row #7 as the AMPLITUDE discriminator. Peak-freq tag: NORMALIZATION-CONDITIONAL-AND-CURRENTLY-AGAINST-mHz.

## Key fidelity corrections ratified at W8-2

- **W6-4 Ω_GW round-figure**: the round figure `1e-57` vs Sage-exact `8.299e-58` is `1.205× = 0.081 OOM` (**SAME-decade**), NOT the "~10×/~2 OOM" the rule/plan prose (`regulator-pin-discipline.md §"Sage-Exact Rationals"`) claimed. The DISCIPLINE (use 8.299e-58, never 1e-57) is correct and binding — but the binding REASON is publication-precision hygiene (**Class-8.3**), NOT an OOM blunder. The rule-prose "~10×/~1 OOM" is itself an overstatement; flagged for W8-6/W8-7 rule-prose fix. See [[omega-gw-roundfigure-fidelity]].
- **W6-7 σ₈/S₈ labeling**: `canonical_constants.py:sigma_8 = 0.811` is the Planck **σ₈**; the capstone "Planck 0.829" was the **S₈** value mis-labeled. The §7.1 σ₈ comparison anchor now cites `Planck σ₈ 0.811 (S₈ 0.829)`. Prose/citation fix also routes to W8-6.
- **§VII.BH (c_s²=0)**: mack-review verdict — NO §7-falsifier-surface retrofit needed. It is a §VII permanent-results CROSS-PILLAR BRIDGE (substrate-IS → Kasparov → lab-IN bound), NOT a falsifier-SURFACE row. The §7.1 c_s² row stays as a robust-spine SCORECARD POINTER; no inventory row created (a registry bridge is not a falsifier).

## Atomic-write discipline (curated-doc sole writer)
All 3 sole-writer surfaces written via atomic section-scoped helpers (read → splice ONLY the target region → fsync+os.replace, or O_APPEND single `open('a')`): capstone §7.1 (`s96_consol_3register_capstone_patch.py`, ASSERTS all 5 W7 guard markers survive), inventory (`s96_consol_inventory_append.py`), WP §W8-2 (`s96_consol_3register_wp.py`). NEVER bulk-append to the curated capstone.
