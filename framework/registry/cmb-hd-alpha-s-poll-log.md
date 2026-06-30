# CMB-HD σ(α_s) Forecast Quarterly Poll Log

**Origin gate**: `S86-CMB-HD-ALPHA-S-FORECAST-PIN` (C36)
**Plan**: `sessions/session-plan/session-86-plan-w12.md` §W12-5
**Producing script**: `computations/s86_w12_cmb_hd_alpha_s_poll.py`
**Cadence**: quarterly (every 3 months) through 2026-2030
**Source streams (3, closed at plan freeze)**:
  1. **Abazajian + CMB-HD-companion publication stream** — arXiv astro-ph queries for new CMB-HD-tagged papers since last poll.
  2. **CMB-HD SciBook code release tracker** — `https://cmb-hd.org/`, `https://github.com/CMB-HD/hdPk`, `https://github.com/CMB-HD/hdlike`, and any successor repos for an explicit σ(α_s) forecast file.
  3. **CMB-S4 / CMB-HD joint forecast literature** — Google Scholar / arXiv queries for "CMB-S4 CMB-HD joint" or "CMB-HD α_s forecast" hits.

**Detection criterion**: a publication that contains an explicit numeric σ(α_s) forecast (Fisher 1-σ on dn_s/dlnk) for the CMB-HD detector specification (ℓ ≤ 20000, 0.5 µK·arcmin, 15", half-sky).

**Verdict semantics**:
  - **PASS** iff publication detected AND PDF SHA-pinned in `sessions/framework/registry/fisher-pdf-registry.md` AND S85 W1b-6 verdict re-fired with dual-SHA companion row in `computations/s86_gate_verdicts.txt`.
  - **INFO** iff poll completed AND no publication available (this is the expected outcome at S86-Q2 and likely through several subsequent quarters).
  - **FAIL** iff quarterly poll cadence missed (>3 months since prior poll).

**Substrate-framing note**: CMB-HD σ(α_s) is a Fisher-forecast observability bound — detector specification, NOT substrate physics. The framework's α_s prediction (S85 W1b-6 = +0.0023 = n_s_canon² − 1, S50–51 identity) is the substrate-side quantity being monitored. The poll-and-pin discipline ensures substrate-prediction re-test occurs immediately on detector publication, eliminating iterate-until-PASS post-hoc adjustment risk.

---

## Poll Entry — 2026-Q2 (S86)

**Poll date**: 2026-04-26
**Polled-by-agent**: `mack-cosmic-bridge`
**Producing script run**: `computations/s86_w12_cmb_hd_alpha_s_poll.py`
**Status**: NO-PUBLICATION-YET

### Stream 1 — Abazajian + CMB-HD-companion arXiv

**Query**: `mcp__paper-search__search_arxiv("CMB-HD alpha_s forecast running spectral index", max_results=8)` and `mcp__paper-search__search_arxiv("Abazajian CMB-HD companion paper forecast", max_results=8)`.

**Hits returned**:
| arXiv ID | Title | Headline σ(α_s) published? |
|:---------|:------|:----------------------------|
| 2203.05728 | Snowmass2021 CMB-HD White Paper (Aiola+ 2022) | NO — headlines: σ(N_eff)=0.014, σ(f_NL)=0.26, σ(r)=0.005, σ(w_0)=0.005, σ(Σm_ν)=13 meV, σ(B_SI)=0.036 nG. α_s NOT in headline. (Re-confirms S85 W1b-6 PRE-REG-INCOMPLETE finding.) |
| 2309.03021 | Cosmological Parameter Forecasts for a CMB-HD Survey (MacInnis, Sehgal, Rothermel 2023, v3 2024-02-05) | NO — headlines σ(n_s)=0.0013, σ(N_eff)=0.014 for ΛCDM+N_eff+Σm_ν model. α_s NOT a marginalized parameter. |
| 2405.12220 | CMB-HD as a Probe of Dark Matter on Sub-Galactic Scales (MacInnis, Sehgal 2024) | NO — focus is k≤55 h/Mpc lensing, WDM/FDM constraints; α_s not forecast. |
| 2002.12714 | CMB-HD Astro2020 RFI Response (Sehgal+ 2020) | NO — predates Snowmass2021 White Paper. |
| 2112.02109 | Foreground Mitigation CMB-HD Lensing (Han, Sehgal 2021) | NO — foreground systematics paper, not parameter forecast. |

**Stream 1 classification**: NO publication of explicit σ(α_s)_CMB-HD detected at 2026-Q2.

### Stream 2 — CMB-HD SciBook / code release tracker

**Queries**:
- `WebSearch("CMB-HD SciBook hdPk GitHub release alpha_s running spectral index 2026")`
- `WebSearch("CMB-HD alpha_s forecast 2026 SciBook running spectral index sigma")`

**Hits returned**:
| Resource | Status |
|:---------|:-------|
| `https://cmb-hd.org/` | Project landing page; no SciBook PDF release with explicit α_s table at 2026-Q2 search. |
| `https://github.com/CMB-HD/hdPk` | Matter Power Spectrum and Non-CDM Forecast Code — Jupyter notebooks reproduce MacInnis & Sehgal (2024) DM forecasts; α_s not a tracked Fisher parameter in the public examples. |
| `https://github.com/CMB-HD/hdlike` | CMB-HD Likelihood (Cobaya-integrated) — likelihood module; no explicit σ(α_s) Fisher number in repository documentation at 2026-Q2. |

**Stream 2 classification**: NO explicit σ(α_s)_CMB-HD code-release artifact detected at 2026-Q2.

### Stream 3 — CMB-S4 / CMB-HD joint forecast literature

**Queries**:
- `mcp__paper-search__search_google_scholar('"CMB-HD" "alpha_s" sigma forecast running spectral index', max_results=8)`
- `mcp__paper-search__search_google_scholar("CMB-S4 CMB-HD joint forecast alpha_s running 2025 2026", max_results=6)`
- `mcp__paper-search__search_arxiv("CMB-HD running scalar spectral index inflation 2025", max_results=6)`

**Hits returned (filtered to CMB-HD-relevant)**:
| Reference | Year | σ(α_s)_CMB-HD published? |
|:----------|:-----|:--------------------------|
| Fairbairn, Heurtier, Olea-Romacho, "Is ΛCDM on the run?" (2511.01612) | 2025 | NO — combines Planck + ACT DR6 + SPT-3G + eBOSS Lyα; presents joint α_s & β_s constraints but NOT a CMB-HD Fisher forecast. (Relevant: confirms current α_s 2σ tensions in non-CMB-HD data; does NOT replace the CMB-HD σ(α_s) gap.) |
| Li, Guo, Zu, "FAST/SKA scalar-induced GW" (2507.09552) | 2025 | NO — SKA forecast, not CMB-HD; reports n_s = 0.9589 ± 0.0021 from CMB+BAO+SKA; α_s sensitivity discussed for SKA, not CMB-HD. |
| Google Scholar query for "CMB-S4 CMB-HD joint forecast alpha_s" 2025–2026 | 2025–2026 | NO — empty result set. |

**Stream 3 classification**: NO joint CMB-S4/CMB-HD α_s forecast detected at 2026-Q2.

### Poll outcome

**Aggregate**: 0 of 3 streams returned a publication carrying an explicit numeric σ(α_s)_CMB-HD forecast at 2026-Q2.

**Verdict**: `INFO` — `value=NO-PUBLICATION-YET`.

**Action taken**: NO update to `sessions/framework/registry/fisher-pdf-registry.md`; NO addition of `sigma_alpha_s_CMB_HD` to `computations/canonical_constants.py`; NO re-emission of S85 W1b-6 verdict. Cadence preserved.

**Next poll target**: S87-Q3 (within 3 months of 2026-04-26, i.e., by 2026-07-26). Failure to fire by 2026-07-26 → cadence FAIL on the S86-CMB-HD-ALPHA-S-FORECAST-PIN gate at S87.

---
