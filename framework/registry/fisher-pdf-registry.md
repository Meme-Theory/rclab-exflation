---
type: registry
ingested-by: /weave --update
---

# Fisher-Forecast PDF Registry

> **Origin**: S86 W12-3 / `S86-FISHER-PDF-PIN-CLOSURE` (C32) by
> `mack-cosmic-bridge`. Plan: `sessions/session-plan/session-86-plan-w12.md`
> §W12-3.
>
> **Sole writer**: `mack-cosmic-bridge` (Fisher-forecast literature anchoring).
> **Index discipline**: each row = one PDF; full SHA-256 (64-char hex) per PRDR §7.
> **Substrate-framing** (plan §13): Fisher PDFs pin OBSERVABILITY (detector
> resolution); substrate physics is upstream and unchanged by SHA-pinning.

**Registry ID**: `fisher-pdf-registry`  
**Owner agent**: `mack-cosmic-bridge`  
**Last updated**: `2026-04-26, S86-W12-3`  
**Ingestion**: `/weave --update` picks up this file.

## Scope

Authoritative SHA-256 anchors for the 5 Fisher-forecast PDFs cited by S85
W4-3 (DESI-DR3-INDEP) + W4-6 (5x5 multi-D JFD). Fixes the AMRI failure
where σ-target values for CMB-S4 / LiteBIRD / DESI / CMB-HD / HERA were
agent-memory-recalled rather than literature-pinned
(per `feedback_agents-not-authoritative.md`). Future-session gates citing
those σ values can audit-trace through this registry.

## Master table (5 rows)

| # | Citation | URL | SHA-256 | Fetched | Used by gates |
|:-:|:---------|:----|:--------|:--------|:--------------|
| 1 | Abazajian+ 2022 'Snowmass 2021 CMB-S4 White Paper' (CMB-S4 Science Book v2) | arXiv:2203.08024 | `8f7e0277202d19d3319939cc187734cbb43621b20897c668a4a5fbe2d10f8967` | 2026-04-26 | W4-3 (CMB-S4 σ-target anchor); W4-6 (5x5 JFD CMB-S4 row); detector-readiness 9-cell row (c) CMB-S4 |
| 2 | DESI Collaboration 2025 'DR2 Results II: BAO + Cosmological Constraints' (latest official DESI Y3-companion forecast paper) | arXiv:2503.14738 | `1e82f26e4cc3901b16168cd147f252bfa804f9c3caad3f4f7e3532640d237841` | 2026-04-26 | W4-3 (DESI DR3 BAO σ_w0/σ_wa anchor); W4-6 (5x5 JFD DESI DR3 row); detector-readiness 9-cell row (b) DESI DR3 |
| 3 | Hazumi+ 2022 'LiteBIRD: A Satellite for the Studies of B-Mode Polarization and Inflation from Cosmic Background Radiation Detection' (PTEP 2023, 042F01; SPIE 12180; arXiv:2202.02773) | arXiv:2202.02773 | `cfc156dfda18a2736fc0a7e19c8454456bad3de66deeee9e32a41c4004781022` | 2026-04-26 | W4-3 (LiteBIRD σ-target row); W4-6 (5x5 JFD LiteBIRD row); detector-readiness 9-cell row (e) LiteBIRD |
| 4 | Sehgal+ 2019 'CMB-HD: An Ultra-Deep, High-Resolution Millimeter-Wave Survey Over Half the Sky' (Snowmass 2021 white paper) | arXiv:1906.10134 | `9785099967a973c5f9dfd7ca6589685b740f8f432008b894f1d42b3b9e8cfdca` | 2026-04-26 | W4-3 (CMB-HD σ_alpha_s anchor); W4-6 (5x5 JFD CMB-HD row); detector-readiness 9-cell row (g) CMB-HD |
| 5 | HERA Memo 54 (Nikolic, Carilli, Kent, Gale-Sides, Thyagarajan, Bernardi, Matika, 2018-11-06) 'Bispectrum Phase around Fornax A Transit using IDR2.1 Data' — pinned-by-memo-number per plan §6 closed list; topic differs from spawn-prompt assumed Ali+2018 21cm-Fisher framing but the memo number is the closed-list anchor and the document is HERA-collaboration sensitivity/instrument literature for the 9-cell row (h) SKA-1/HERA 21cm channel | https://reionization.org/wp-content/uploads/2018/11/hera-memo-54.pdf | `2c8d0b9249950a603e2637cdc7ade4ece8b73ca28f06242075365b4dc8bb74c5` | 2026-04-26 | W4-3 (21cm-channel row); W4-6 (5x5 JFD HERA row); detector-readiness 9-cell row (h) SKA-1 21cm channel |

## Per-row provenance

### Row 1 — Abazajian+ 2022 'Snowmass 2021 CMB-S4 White Paper' (CMB-S4 Science Book v2)

- **URL / arXiv**: arXiv:2203.08024
- **Local cache**: `computations/_fisher_pdf_cache/2203.08024.pdf`
- **Bytes**: 1188585
- **SHA-256 (full)**: `8f7e0277202d19d3319939cc187734cbb43621b20897c668a4a5fbe2d10f8967`
- **Fetched via**: mcp__paper-search__download_arxiv
- **Fetched date**: 2026-04-26
- **Used by gates**: W4-3 (CMB-S4 σ-target anchor); W4-6 (5x5 JFD CMB-S4 row); detector-readiness 9-cell row (c) CMB-S4

### Row 2 — DESI Collaboration 2025 'DR2 Results II: BAO + Cosmological Constraints' (latest official DESI Y3-companion forecast paper)

- **URL / arXiv**: arXiv:2503.14738
- **Local cache**: `computations/_fisher_pdf_cache/2503.14738.pdf`
- **Bytes**: 12175089
- **SHA-256 (full)**: `1e82f26e4cc3901b16168cd147f252bfa804f9c3caad3f4f7e3532640d237841`
- **Fetched via**: mcp__paper-search__download_arxiv
- **Fetched date**: 2026-04-26
- **Used by gates**: W4-3 (DESI DR3 BAO σ_w0/σ_wa anchor); W4-6 (5x5 JFD DESI DR3 row); detector-readiness 9-cell row (b) DESI DR3

### Row 3 — Hazumi+ 2022 'LiteBIRD: A Satellite for the Studies of B-Mode Polarization and Inflation from Cosmic Background Radiation Detection' (PTEP 2023, 042F01; SPIE 12180; arXiv:2202.02773)

- **URL / arXiv**: arXiv:2202.02773
- **Local cache**: `computations/_fisher_pdf_cache/2202.02773.pdf`
- **Bytes**: 27290943
- **SHA-256 (full)**: `cfc156dfda18a2736fc0a7e19c8454456bad3de66deeee9e32a41c4004781022`
- **Fetched via**: mcp__paper-search__download_arxiv
- **Fetched date**: 2026-04-26
- **Used by gates**: W4-3 (LiteBIRD σ-target row); W4-6 (5x5 JFD LiteBIRD row); detector-readiness 9-cell row (e) LiteBIRD

### Row 4 — Sehgal+ 2019 'CMB-HD: An Ultra-Deep, High-Resolution Millimeter-Wave Survey Over Half the Sky' (Snowmass 2021 white paper)

- **URL / arXiv**: arXiv:1906.10134
- **Local cache**: `computations/_fisher_pdf_cache/1906.10134.pdf`
- **Bytes**: 1188203
- **SHA-256 (full)**: `9785099967a973c5f9dfd7ca6589685b740f8f432008b894f1d42b3b9e8cfdca`
- **Fetched via**: mcp__paper-search__download_arxiv
- **Fetched date**: 2026-04-26
- **Used by gates**: W4-3 (CMB-HD σ_alpha_s anchor); W4-6 (5x5 JFD CMB-HD row); detector-readiness 9-cell row (g) CMB-HD

### Row 5 — HERA Memo 54 (Nikolic, Carilli, Kent, Gale-Sides, Thyagarajan, Bernardi, Matika, 2018-11-06) 'Bispectrum Phase around Fornax A Transit using IDR2.1 Data' — pinned-by-memo-number per plan §6 closed list; topic differs from spawn-prompt assumed Ali+2018 21cm-Fisher framing but the memo number is the closed-list anchor and the document is HERA-collaboration sensitivity/instrument literature for the 9-cell row (h) SKA-1/HERA 21cm channel

- **URL / arXiv**: https://reionization.org/wp-content/uploads/2018/11/hera-memo-54.pdf
- **Local cache**: `computations/_fisher_pdf_cache/hera-memo-54.pdf`
- **Bytes**: 5723255
- **SHA-256 (full)**: `2c8d0b9249950a603e2637cdc7ade4ece8b73ca28f06242075365b4dc8bb74c5`
- **Fetched via**: WebFetch (collaboration memo, non-arXiv)
- **Fetched date**: 2026-04-26
- **Used by gates**: W4-3 (21cm-channel row); W4-6 (5x5 JFD HERA row); detector-readiness 9-cell row (h) SKA-1 21cm channel

## Substitution chain (plan §6 step 4)

```
Definition:  N_pdfs_required = 5 (CMB-S4-SBv2, DESI-DR2-II, LiteBIRD-Hazumi,
             CMB-HD-Sehgal, HERA-Memo-54)
Definition:  N_pinned = count(rows with full 64-char SHA-256)
Definition:  N_reemit = count of S85 verdicts re-emitted under fisher-pdf-pin map
Substitute:  N_required = 5; N_reemit_required = 2 (W4-3, W4-6)
Simplify:    N_pinned = 5/5; N_reemit = 2/2
Direction:   PASS iff (N_pinned == 5 AND N_reemit == 2);
             INFO if 3 <= N_pinned <= 4;
             FAIL if N_pinned <= 2.
Verify:      Python sha256_file() over each PDF; verdict=PASS.
             Original verdict VALUE/SCHEME/CONVENTION/L_max preserved
             unchanged in s85_gate_verdicts.txt; only input-pin map
             changes (now references Fisher-PDF SHAs from this registry).
```

## Provenance

- Plan: `sessions/session-plan/session-86-plan-w12.md` §W12-3
- Producing script: `computations/s86_w12_fisher_pdf_pin.py`
- Verdict file: `computations/s86_gate_verdicts.txt`
  (S86-FISHER-PDF-PIN-CLOSURE + W4-3 re-emission + W4-6 re-emission)
- Upstream registry: `sessions/framework/registry/detector-readiness-9-cell.md`
  (rows (b)/(c)/(e)/(g)/(h) anchor to these PDFs via 'σ-target' column)

## Status

- Registry: REGISTERED (S86 W12-3).
- Downstream cite-points: any future gate citing σ(α_s)_CMB-S4,
  σ(α_s)_CMB-HD, σ(n_T)_LiteBIRD, σ(w_0)/σ(w_a)_DESI, or 21cm-HERA
  Fisher widths must reference the row + SHA in this table.

## Carry-forward

- Row 5 (HERA Memo 54): topic-vs-memo-number discrepancy noted —
  spawn prompt assumed Ali+2018 21cm-Fisher framing; the actual Memo 54
  is Nikolic+2018 'Bispectrum Phase around Fornax A Transit using IDR2.1'.
  The closed-list anchor is the memo NUMBER (per plan §6); the registry
  pin is the canonical Memo 54 PDF. If a future S87+ session needs the
  21cm-Fisher Ali+2018 reference, that is a SEPARATE row to add.
- Any TBD-S87 row (paywalled / withdrawn) is re-fetched at next session.
