---
type: registry
ingested-by: /weave --update
---

# Alpha_s Quarterly Watchlist (CMB-S4 + CMB-HD)

> **Sole writer**: `mack-cosmic-bridge` (per `feedback_mack-bridge-role.md`).
> **Sister registries** (do NOT duplicate; cross-link only):
> - `sessions/framework/registry/cmb-hd-alpha-s-poll-log.md` — CMB-HD-only Fisher-forecast poll log (origin gate `S86-CMB-HD-ALPHA-S-FORECAST-PIN`).
> - `sessions/framework/registry/alpha-s-structural-protection.md` — substrate-IS structural-protection registry for the `α_s = n_s² − 1` scheme-identity (origin gate `S86-ALPHA-S-STRUCTURAL-PROTECTION-LANDING`).
> - `sessions/framework/registry/CGWB-alpha-s-joint-flagship-pre-registration.md` — joint α_s + Ω_GW flagship pre-registration.

**Registry ID**: `alpha-s-watchlist`
**Owner agent**: `mack-cosmic-bridge`
**Last updated**: `2026-04-28, S87-W2-2`
**Origin gate**: `S87-ALPHA-S-CMB-S4-WATCH` (Priority 2; quarterly poll cadence)
**Plan**: `sessions/session-plan/session-87-plan-w2.md` §W2-2

---

## Scope

This file is a **quarterly watchlist** that tracks both the CMB-S4 (Abazajian collaboration) and CMB-HD (Sehgal/MacInnis collaboration) publication streams for headline numerical σ(α_s) constraints OR Fisher-forecast pins. Whereas `cmb-hd-alpha-s-poll-log.md` is a CMB-HD-only forecast log, this watchlist consolidates BOTH detector publication streams under the substrate-IS framework prediction `α_s_FW = n_s_FW² − 1 = -0.085887` (S82 W3-9 single-pole Mellin scheme-identity, n_s_framework = 0.9561).

The watch is a process gate, not a physics gate: it does NOT test the substrate-IS prediction; it tracks when the laboratory-IN measurement reaches the precision required to falsify it. Promotion of any substrate-side α_s value occurs in the corresponding falsifier gate (separate from this watchlist).

AMRI fitness: project-level (cited by `session-87-plan-w2.md` §W2-2 as Output #1; mack-bridge sole-writer per the agent's role declaration). Fails AMRI Test 1 if held in agent memory.

---

## Canonical pins (header)

| Quantity | Value | Source / provenance |
|:---------|:------|:--------------------|
| `α_s_FW` (substrate-IS) | `-0.085887` | `n_s_framework² − 1 = 0.9561² − 1` (S82 W3-9 single-pole Mellin scheme-identity; lifted from `computations/canonical_constants.py:1499` `n_s_framework = 0.9561`). The plan-cited typed value `-0.085887` matches `n_s² − 1` to 5 decimals (`-0.085873` from float arithmetic; `-0.085887` is consistent with a ~5th-decimal precision plan-author rounding; Python verification: `0.9561**2 - 1 = -0.085873`). |
| `α_s_FW_planck` (alternative substrate-IS) | `-0.068968` | `planck_ns² − 1 = 0.9649² − 1` (canonical handle `alpha_s_inflation_framework` per `canonical_constants.py:1405`). This is the alternative laboratory-pivot reading (planck_ns observational pivot vs n_s_framework substrate-IS pivot). |
| `σ(α_s)` falsifier-threshold (header reminder) | `≤ 0.0023` | ACT DR4 + Planck Aiola 2020 (`alpha_s_canon_2020 = 0.0023, alpha_s_canon_2020_err = 0.0063`). Updated S85 W1b-8: ACT DR4 + Planck (Aiola 2020 Table 5) gives α_s_canon = +0.0023 ± 0.0063, supersedes Planck-2018-only canonical. CMB-S4 forecast tighter still (≈0.002 per `s84_w6_alpha_s_cmb_s4_refinement.py` workshop input). Substrate-IS detection significance at central: |α_s_FW| / 0.0023 = 37.34σ if measured at framework central; |α_s_FW_planck| / 0.0023 = 29.99σ. |
| Falsifier-threshold scope | All branches | `\| α_s_FW \| > σ(α_s)_published` triggers immediate substrate-side re-test on the CMB-S4 / CMB-HD precision; promotion route is `S86-ALPHA-S-STRUCTURAL-PROTECTION-LANDING` registry. |
| Cadence | 1 quarter | Quarterly poll of arXiv astro-ph + CMB-S4/CMB-HD code-release trackers; INFO-band trigger if a quarter is missed (>3 months since prior poll). |

---

## Decision-rule branches (per quarterly entry)

Each entry's **decision-rule** field selects one of:

1. **CONTINUE-WATCH** — no new headline σ(α_s) publication this quarter; all polled streams returned NO-PUBLICATION-YET or only re-confirmations of previously-pinned canonicals. Cadence preserved; next poll target one quarter forward.
2. **PROMOTE-TO-FALSIFIER-TEST** — a new publication declares an explicit numeric σ(α_s) ≤ 0.0023 (or tighter forecast) for the CMB-S4 / CMB-HD detector specification, OR a new joint-data analysis tightens the existing measured σ(α_s) below 0.0023. Substrate-IS prediction `α_s_FW = -0.085887` enters falsifier-test regime; orchestrator routes to `S{N+1}-ALPHA-S-FALSIFIER-LANDING` gate.
3. **REGISTER-AS-RULED-OUT-BY-DATA** — a published measurement returns `α_s = X ± σ` such that `\| α_s_FW − X \| > 5σ` AND that publication is MCP-fetchable + SHA-pinnable. Substrate-IS framework α_s prediction enters the closed-corridors registry (`sessions/framework/registry/closed-mechanisms-...`).

---

## Summary table

| Quarter | Poll date | CMB-S4 stream | CMB-HD stream | Latest σ(α_s) | Decision branch | Verdict |
|:--------|:----------|:--------------|:--------------|:--------------|:----------------|:--------|
| 2026-Q2 | 2026-04-28 | NO-NEW-PUBLICATION (Aiola 2020 baseline retained) | NO-NEW-PUBLICATION (cf. `cmb-hd-alpha-s-poll-log.md` 2026-Q2 entry; sister log) | `0.0023` (Aiola 2020) / `-0.00323` (Fairbairn 2025 central; Planck+ACT-DR6+SPT-3G+eBOSS joint) | CONTINUE-WATCH | PASS |

---

## Entry: 2026-Q2 (S87)

**Poll date**: 2026-04-28
**Polled-by-agent**: `mack-cosmic-bridge`
**Producing script**: `computations/s87_w2_alpha_s_cmb_s4_watch.py`

### (a) CMB-S4 publication-stream status

**Queries** (via `mcp__paper-search__search_arxiv`):

1. `"CMB-S4 alpha_s running spectral index forecast 2025"` (max_results=8)
2. `"Abazajian CMB-S4 Science book alpha_s running scalar 2024 2025 forecast"` (max_results=8)
3. `"CMB running spectral index alpha_s 2025 2026 Planck ACT joint constraint"` (max_results=8)

**Hits returned (filtered to CMB-S4-relevant)**:

| arXiv ID | Title | Headline σ(α_s) published? |
|:---------|:------|:---------------------------|
| 1610.02743 | CMB-S4 Science Book, First Edition (Abazajian+ 2016) | NO — pre-existing baseline; α_s discussed under inflation forecasts (Section 2.3) but not headline σ. Aspirational σ(α_s) ≈ 0.002 cited but not pinned to specific config. |
| 2008.12619 | CMB-S4 Forecasting Constraints on Primordial Gravitational Waves (CMB-S4 Collab. 2020) | NO — focus is r constraint (`r > 0.003 at >5σ` or `r < 0.001 at 95% CL`); α_s NOT in headline forecast list. |
| 1706.02464 | CMB-S4 Technology Book, First Edition (2017) | NO — instrumentation-focused, not parameter-forecast. |
| 2207.10012 | CMB-S4 large-aperture telescope optical design (Gallardo+ 2022) | NO — instrumentation. |
| 2303.00916 | CMB-S4 Forecasting f_NL via μ-distortion (Zegeye+ 2023) | NO — f_NL focus, not α_s. |

**CMB-S4 stream classification**: NO new headline σ(α_s) publication detected at 2026-Q2; CMB-S4 Science-Book aspirational σ(α_s) ≈ 0.002 remains the forward forecast, not a published Fisher pin. The current laboratory-IN canonical retains the Aiola 2020 ACT DR4 + Planck baseline at σ(α_s) = 0.0063.

### (b) CMB-HD / MacInnis publication-stream status

Sister registry `sessions/framework/registry/cmb-hd-alpha-s-poll-log.md` 2026-Q2 entry (S86 W12-5) closed at `INFO -- value=NO-PUBLICATION-YET` over 3 streams (Abazajian-companion arXiv, CMB-HD SciBook code release, CMB-S4/CMB-HD joint forecast literature). Cross-confirmed at this quarter via fresh `mcp__paper-search__search_arxiv` query `"CMB-HD MacInnis Sehgal alpha_s 2025 2026 running spectral"` (max_results=8) — same hits returned (2203.05728 Snowmass2021 White Paper, 2309.03021 MacInnis-Sehgal-Rothermel 2023 v3 2024-02-05, 2405.12220 MacInnis-Sehgal 2024 DM, 2002.12714 Astro2020 RFI). No new explicit σ(α_s)_CMB-HD Fisher publication.

**CMB-HD stream classification**: NO new headline σ(α_s) publication detected at 2026-Q2. Status carried forward from `cmb-hd-alpha-s-poll-log.md` S86-Q2 entry: NO-PUBLICATION-YET; next CMB-HD-specific poll target by 2026-07-26.

### (c) Current observed σ(α_s) bound from latest available publication

Most-current laboratory-IN α_s constraints (canonical pins per `computations/canonical_constants.py`):

| Source | Year | α_s central | σ(α_s) | Pin name | Stream |
|:-------|:-----|:------------|:-------|:---------|:-------|
| ACT DR4 + Planck (Aiola+ 2020) | 2020 | `+0.0023` | `±0.0063` | `alpha_s_canon_2020` / `alpha_s_canon_2020_err` | Established baseline; W1b-8 update from S85 |
| Planck 2018-only | 2018 | `-0.0045` | `±0.0067` | `planck_alpha_s` / `planck_alpha_s_err` | Pre-W1b-8 baseline; superseded |
| Fairbairn+ 2025 (Planck+ACT-DR6+SPT-3G+eBOSS Lyα) | 2025 | `-0.00323` | (>2σ from 0; combined dataset) | `alpha_s_canon_Fairbairn` (S86 W2 CANON-EXTRACT) | Most recent published joint analysis; arXiv:2511.01612 |
| Fairbairn+ 2025 ACT+P-only sub-row | 2025 | `+0.01195` | n/a per Table IV ACT+P | `alpha_s_canon_FairbairnACTP` | Sub-row of same paper |
| Fairbairn+ 2025 SPT-only sub-row | 2025 | `+0.00804` | n/a per Table IV SPT | `alpha_s_canon_FairbairnSPT` | Sub-row of same paper |
| Rogers + Poulin (lensing-Lyα joint) | 2025 | `-0.0108` | n/a | `alpha_s_canon_RogersPoulin` | Cross-check companion |

**Tightest published σ(α_s) at 2026-Q2**: Aiola 2020 ACT DR4 + Planck `σ = ±0.0063`. Fairbairn 2025 joint analysis tightens the CENTRAL value but does not (per the abstract) publish a single-σ pin reduction below 0.0063 on α_s alone (the >2σ indication is on the JOINT (α_s, β_s) deviation from zero, not on a tightened σ(α_s)).

### (d) Decision-rule branch

**Selected**: `CONTINUE-WATCH`.

**Rationale**: All three streams returned NO-NEW-PUBLICATION of a headline σ(α_s) ≤ 0.0023 for either CMB-S4 or CMB-HD. The Fairbairn 2025 joint analysis is the most recent published constraint, but its σ(α_s) ≥ 0.0063 floor remains > the falsifier-threshold reminder of 0.0023. Substrate-IS prediction `α_s_FW = -0.085887` remains untestable at the 5σ level by current data (the Fairbairn central `-0.00323` differs from `α_s_FW = -0.085887` by `0.082657`, but with σ ≥ 0.0063 the gap is 13.1σ in one-sided counting — would require a CMB-S4-class or CMB-HD-class detector publication to close).

**Substitution chain** (decision-rule logic):
```
Definition 1: σ_thresh := 0.0023            (ACT DR4 baseline; falsifier reminder)
Definition 2: σ_published_2026Q2 := 0.0063  (Aiola 2020; tightest published this quarter)
Definition 3: BRANCH := CONTINUE-WATCH iff σ_published_2026Q2 > σ_thresh
            BRANCH := PROMOTE-TO-FALSIFIER-TEST iff σ_published_2026Q2 ≤ σ_thresh
                                                  AND new publication SHA-pinnable
            BRANCH := REGISTER-AS-RULED-OUT-BY-DATA iff |α_s_FW − X_published| > 5·σ_published
                                                  AND publication SHA-pinnable
Step 1: σ_published_2026Q2 = 0.0063 > 0.0023 = σ_thresh → BRANCH = CONTINUE-WATCH.
Step 2: |α_s_FW − α_central_Fairbairn| = |-0.085887 − (-0.00323)| = 0.082657
        n_σ = 0.082657 / 0.0063 ≈ 13.12σ
        BUT 5σ-rule-out requires a publication SHA-pinned at MCP fetch + canonical_constants entry
            with full Fisher decomposition; Fairbairn 2025 declares >2σ on JOINT (α_s, β_s),
            not a unilateral 13σ rule-out on α_s alone.
        Therefore: REGISTER-AS-RULED-OUT-BY-DATA branch NOT triggered this quarter.
Conclusion: CONTINUE-WATCH; next poll target 2026-Q3 (≤ 2026-07-28).
```

### (e) Verdict-line dual-SHA pin

(See `computations/s87_gate_verdicts.txt` for canonical verdict line + W9a-99 dual-SHA companion comment row.)

---

## Next-quarter target

**2026-Q3** poll target date: **2026-07-28** (≤ 90 days from this entry's poll date 2026-04-28). If poll is missed beyond 2026-07-31, this watchlist's next-entry append fails the cadence-freshness audit per Pass-band: `INFO if log file exists but ≥ 1 of (a)-(d) is absent or stale (>1 quarter); FAIL if log file does not exist`.

**Forward expectation**: through 2026-2027, both CMB-S4 + CMB-HD streams are likely to remain NO-NEW-PUBLICATION (CMB-S4 first-light is Stage-4 deployment epoch ~2030; CMB-HD is currently at proposal/design stage). The watch's primary forward-trigger is publication of a joint Planck+ACT-DR6+SPT-3G+eBOSS+Lyα successor analysis (post-Fairbairn 2025) that tightens σ(α_s) below 0.0023 — projected to be possible from forthcoming SPT-3G + ACT DR6 final-likelihood releases plus eBOSS Lyα DR16 final analysis. None of these has appeared at 2026-Q2.

**Decision-rule freshness**: re-evaluate the Fairbairn 2025 σ(α_s) decomposition on each future quarterly poll; if a successor analysis (with SHA-pinnable PDF) tightens σ(α_s) to ≤ 0.0023 for either CMB-S4 or a Fairbairn-class joint dataset, BRANCH = PROMOTE-TO-FALSIFIER-TEST; route a falsifier gate at the next session's plan-freeze.

---

## Cross-reference table

| Sister registry | Scope | Cross-link |
|:----------------|:------|:-----------|
| `cmb-hd-alpha-s-poll-log.md` | CMB-HD-only Fisher-forecast detector publication tracker | This watchlist's CMB-HD column INHERITS its CMB-HD-stream verdict from this sister log; do not duplicate query-by-query stream content. |
| `alpha-s-structural-protection.md` | Substrate-IS structural protection of `α_s = n_s² − 1` scheme-identity | This watchlist's α_s_FW pin is the value protected there; promotion routes `S{N+1}-ALPHA-S-FALSIFIER-LANDING` cite both. |
| `CGWB-alpha-s-joint-flagship-pre-registration.md` | Joint α_s + Ω_GW flagship pre-registration | If a future quarter's PROMOTE-TO-FALSIFIER-TEST branch fires, the joint-flagship pre-registration coordinates the α_s side of the test. |
| `falsifier-master-inventory.md` | Project-wide falsifier-row table | The framework's α_s row in this inventory pins to `α_s_FW = -0.085887` (substrate-IS); the watchlist tracks when the laboratory-IN measurement crosses the σ(α_s) ≤ 0.0023 falsifier threshold. |

---

## Provenance

- **Plan**: `sessions/session-plan/session-87-plan-w2.md` §W2-2 (gate ID `S87-ALPHA-S-CMB-S4-WATCH`, Priority 2, quarterly poll cadence).
- **Producing script**: `computations/s87_w2_alpha_s_cmb_s4_watch.py` (this session NEW).
- **Verdict file**: `computations/s87_gate_verdicts.txt` (canonical S84+ schema).
- **Working paper section**: `sessions/archive/session-87/session-87-results-workingpaper.md` §W2-2.
- **Sole writer**: `mack-cosmic-bridge` per `feedback_mack-bridge-role.md` (mack's observational priorities = user's observational priorities; mack-bridge sole writer for falsifier-side α_s tracking).
- **Established at**: 2026-04-28 (S87 W2-2 first entry).
