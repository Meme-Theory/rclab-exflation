---
type: registry
ingested-by: /weave --update
---

# Cross-Channel Correlation Matrix — 5-Channel Watchlist

**Registry ID**: `cross-channel-correlation-matrix`
**Owner agent(s)**: `mack-cosmic-bridge` (primary), `little-red-dots-jwst-analyst` (consumer)
**Last updated**: `2026-04-23, S85-W4-2-XCORR-MATRIX`
**Ingestion**: `/weave --update` picks up this file; `knowledge.db` stores one row per pair entry in the `open` entity table (live observational-pipeline metadata).

---

## Scope

This registry holds the canonical 5×5 correlation matrix for the W4-introduced 5-channel detector-correlation roster: CMB-S4 α_s, DESI DR3 w_0, LiteBIRD n_T, CMB-HD α_s, 21-cm folded bispectrum. It is distinct from `sessions/framework/registry/falsifier-watchlist.md`, which holds the S58-established 6-channel LRD watchlist (w_0, w_a, g_1/g_2, α_s, proton lifetime, H_0). The two registries overlap on `w_0` and `α_s` but use different roster frames — this file binds DETECTOR pairs; falsifier-watchlist.md binds OBSERVABLE-to-detector rows.

Consumer gates cite each pair's tag rather than re-deriving it. Not in agent memory because AMRI tests (a) and (c) both fire: other gates (§W4-4, §W4-6, §W4-7, §W4-8) name this file as an Input-SHA pin, and two or more agents (mack, LRD) would otherwise overlap on the same detector-pair entries.

---

## Summary table — diagonal (substrate-moment probes)

| i | Channel | Substrate-moment probed |
|:-:|:--------|:------------------------|
| 0 | **CMB-S4 alpha_s** | d^2 S_transfer/dk^2 at k_pivot (scalar 2-pt 2nd derivative of spectral tilt; phononic: running of the fold-imprinted n_s at CMB acoustic horizon) |
| 1 | **DESI DR3 w_0** | a_0 Volovik-partition (zeroth spectral moment; late-time effacement residual; phononic: 0.03% impedance leakage, Gamma=0.99970) |
| 2 | **LiteBIRD n_T** | tensor-sector Dirac spectrum (B-mode polarization; phononic: r=16*epsilon RELATION IS INAPPLICABLE per phononic-framing.md rule; n_T is BLUE at transit, RED at CMB via 14.3x suppression, S66 TENSOR-TRANSFER) |
| 3 | **CMB-HD alpha_s** | d^2 S_transfer/dk^2 at k_pivot (SAME moment as CMB-S4 alpha_s; different detector; phononic: redundant substrate-sensitivity channel; common-mode when paired with CMB-S4) |
| 4 | **21-cm folded bispec** | 3-point spectral moment (non-Gaussianity; equilateral/folded shapes; phononic: GGE-relic 3-pt correlation, folded f_NL=0.056 from S82 W3-4 GGE-FNL) |

> **AH-TR-1 scale-coordinate cross-link (S92, transit×connes; `sessions/archive/session-92/workshops/s92-adhoc-alpha-s-transfer-map-identity.md`)**: the `d^2 S_transfer/dk^2 at k_pivot` moment in rows 0 (CMB-S4 alpha_s) and 3 (CMB-HD alpha_s) is the **substrate-distance** running `alpha_s^{substrate} = (a_4/a_2)^2 - 1 = -0.08587279` (Mellin residue at the s=3 pole, evaluated on `{lambda_k}` INSIDE the BZ at O(M_KK); FI-class regulator-invariant, S91 W9; sign-walled negative). It is SCALE-SEPARATED by 54.04 decades from the **CMB-pivot** running `alpha_s^{pivot} ≈ 0` (the substrate's Goldstone two-point curvature `P_{∇φ}=K^2·K^{-2}=K^0` at the pivot; S47 PERMANENT/Exact). The "SAME moment as CMB-S4 alpha_s" (row 3) is the framework's pre-registered moment-identity claim; whether the substrate-distance value IS the Planck-pivot alpha_s (12.15σ tension LIVE) or transports to ≈0 at the pivot (+0.67σ, tension relocates to this substrate-sensitivity channel) is set by the single homogeneity degree `deg(T_{BZ→pivot})` (`S92-W3-CF-S92-W5-1-D`, S93; §VII.BA composite-admissibility T2-vacuous-vs-substrate-natural). Canonical pins: `alpha_s_substrate_distance_1` / `alpha_s_pivot_goldstone` (`canonical_constants.py` SECTION E). Full directive + K=2 per-observable transport-degree K-counter: `sessions/framework/registry/cross-pillar-bridge-corpus.md §23`.

---

## Summary table — off-diagonal (10 pairs of C(5,2))

| Pair | Channels | Classification | Source | Citation / Justification |
|:----:|:---------|:--------------:|:------:|:-------------------------|
| (0,1) | CMB-S4 alpha_s / DESI DR3 w_0 | PARTIALLY_CORRELATED | **FISHER** | DESI Collab 2025 BAO forecast; Planck 2018 parameter table (CMB prior). *Shared acoustic-scale ladder r_d; CMB TT/TE likelihood enters DESI BAO fit as prior.* |
| (0,2) | CMB-S4 alpha_s / LiteBIRD n_T | INDEPENDENT | **FISHER** | CMB-S4 Science Book v2 2022 §3.1; LiteBIRD LB-IFU-PHA1-D-015 arXiv:1902.00541. *Scalar-tilt running (temperature) vs tensor tilt (polarization-B); orthogonal spectral moments.* |
| (0,3) | CMB-S4 alpha_s / CMB-HD alpha_s | COMMON_MODE | **FISHER** | CMB-HD Sehgal 2019 Whitepaper §4; CMB-S4 Science Book v2 Table 6.1. *Identical theoretical observable (both measure dn_s/dlnk); overlapping foreground + potential atmospheric noise correlation.* |
| (0,4) | CMB-S4 alpha_s / 21-cm folded bispec | INDEPENDENT | **FIRST-PRINCIPLES-REASONING** | Cosmic-epoch separation + statistics-order separation (no joint CMB-S4 x 21cm Fisher published). *z=1100 recombination CMB vs z~7 reionization 21cm; 2-pt vs 3-pt statistics; no shared nuisance parameter at substrate-moment level (HERA Memo 54 Ali+ 2018 forecasts 21cm alone).* |
| (1,2) | DESI DR3 w_0 / LiteBIRD n_T | INDEPENDENT | **FIRST-PRINCIPLES-REASONING** | Late-time vs primordial regime (no joint DESIxLiteBIRD Fisher published). *Late-time expansion (z<2 BAO ruler) vs primordial-tensor B-mode (z=1100 polarization); no shared tracer, no shared foreground systematic.* |
| (1,3) | DESI DR3 w_0 / CMB-HD alpha_s | PARTIALLY_CORRELATED | **FISHER** | DESI Collab 2025 §4; Sehgal 2019 CMB-HD Whitepaper. *Both use r_d acoustic ruler; CMB-HD extends the Planck+ACT CMB prior used in DESI BAO likelihood.* |
| (1,4) | DESI DR3 w_0 / 21-cm folded bispec | INDEPENDENT | **FIRST-PRINCIPLES-REASONING** | Low-z BAO (z<2) vs high-z NG (z>6) epoch separation (no joint DESIx21cm Fisher published). *Different tracers (galaxies vs neutral H), different epochs, different nuisance systematics.* |
| (2,3) | LiteBIRD n_T / CMB-HD alpha_s | INDEPENDENT | **FISHER** | LiteBIRD arXiv:1902.00541; Sehgal 2019 CMB-HD §4. *B-mode tensor (polarization) vs TT/TE scalar running (temperature); CMB foreground templates differ (polarization-B vs TT).* |
| (2,4) | LiteBIRD n_T / 21-cm folded bispec | INDEPENDENT | **FIRST-PRINCIPLES-REASONING** | CMB polarization vs reionization 21cm (no joint LiteBIRDx21cm Fisher published). *z=1100 polarization-B vs z~7 NG; no shared physical systematic at substrate-moment level.* |
| (3,4) | CMB-HD alpha_s / 21-cm folded bispec | INDEPENDENT | **FIRST-PRINCIPLES-REASONING** | Same logic as (0,4) with CMB-HD substituted for CMB-S4 (no joint CMB-HDx21cm Fisher). *Different instruments, different epochs, different statistics-order.* |

---

## Post-data Bayes-factor formula

For N channels with per-channel Bayes factors `BF_i` and pair-wise effective correlation `rho_ij`:

```
BF_joint = product_i BF_i^{f_i}  where
  f_i = 1 - mean_{j != i} rho_ij    (isotropic-correction approximation)

For the 5-channel roster, the numerically significant correlations are:
  rho_01 (CMB-S4 x DESI DR3)   ~ 0.3 (partial, BAO-CMB ladder)
  rho_03 (CMB-S4 x CMB-HD)     ~ 0.7 (common-mode, same observable)
  rho_13 (DESI DR3 x CMB-HD)   ~ 0.3 (partial, r_d ladder)
All other rho_ij  ~ 0 (FIRST-PRINCIPLES-INDEPENDENT).

The joint BF is therefore APPROXIMATELY deflated by the common-mode pair (0,3):
  BF_joint ~ BF_0^{0.65} * BF_1^{0.85} * BF_2 * BF_3^{0.65} * BF_4
             (compared to naive BF_joint_indep = prod BF_i)
```

The exact numeric rho_ij values carry forward from §W4-3 (DESI-DR3 x CMB correlation) and §W4-6 (multi-D joint Fisher inversion) into a subsequent update of this registry.

---

## Consumer gates

| Gate ID | Session | Role | Notes |
|:--------|:--------|:-----|:------|
| `S85-W4-1-CMB-S4-INDEP-AUG` | S85 | INPUT-PIN | matrix preview augmented into §W0-13 |
| `S85-W4-2-XCORR-MATRIX` | S85 | OUTPUT-WRITER | this gate |
| `S85-W4-3-DESI-DR3-INDEP` | S85 | CONSUMES (0,1) cell | pins ρ_01 numerically |
| `S85-W4-4-FALSIFIER-WATCH-CERT` | S85 | INPUT-PIN | per-channel xcorr class |
| `S85-W4-6-MULTI-D-JFD` | S85 | CONSUMES | Fisher off-diagonals |
| `S85-W4-7-NULL-ELIM-MAP` | S85 | CONSUMES | joint-σ inputs |
| `S85-W4-8-WATCHLIST-UPDATE` | S85 | INPUT-PIN | xcorr-class column in unified rows |
| future joint-BF computations | S86+ | INPUT-PIN | prevents per-session re-derivation |

---

## Change log

| Date | Session | Change | Author |
|:-----|:--------|:-------|:-------|
| 2026-04-23 | S85-W4-2 | create (5-channel frozen 2026-04-21) | mack-cosmic-bridge |

---

## SHA pins (S84+ dual-SHA)

- `audit_sha256`: `879b2e39ccf81f7be362f6158983a76575ba8f75413c349ee061df318d04a6e8`
- `content_sha256`: `d384acae1bfdf85de9b921ffc0e1f9c7c5d93ec227038922d6faadf4c09fc8f3`
- Input files pinned: `canonical_constants.py`, `baseline-findings-s66.md`, `permanent-results-registry.md`, `session-84-s4-mack-falsifier-synthesis.md`, `session-84-s4-lrd-falsifier-synthesis.md`, `evoi-framework.md`.

---

## Cardinality audit (plan W4-2 PASS criterion)

- Cells total (5×5): **25**
- Cells filled: **25** (100%)
- Diagonal cells with substrate-moment: **5/5**
- Off-diagonal cells with Fisher citation: **10/20** (symmetric: 5 unique pairs)
- Off-diagonal cells with FIRST-PRINCIPLES-REASONING: **10/20** (symmetric: 5 unique pairs)
- Silent (untagged) cells: **0**

