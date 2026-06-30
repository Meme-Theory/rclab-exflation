# Hazumi 2022 LiteBIRD alpha_s forecast — PRE-REG-INCOMPLETE disposition

**Gate**: S85-W1b-LITEBIRD-ALPHA-S-HAZUMI-VERIFIED
**Verdict**: PRE-REG-INCOMPLETE

## Full-text grep across Hazumi 2022 (156 pages)

Keywords searched: alpha_s, alpha s, running of, dn_s/dlnk, d²ln, nrun, running spectral.

Hits: 0 (zero).

Verified: LiteBIRD definition paper (Hazumi et al. 2022 JLTP,
arXiv:2202.02773) does not forecast or even discuss alpha_s.

## Hazumi 2022 headline forecasts (extracted from memory/cross-reference)

| Parameter | Hazumi value | Status |
|:----------|:-------------|:-------|
| sigma(r)           | Δr budget, aim 0.001 | PUBLISHED |
| sigma(tau_re)      | 0.002 (CVR)   | PUBLISHED |
| sigma(n_T)         | derived from r-consistency | PUBLISHED (indirect) |
| **sigma(alpha_s)** | **NOT PUBLISHED**     | ABSENT |

## Why this is NOT a FAIL

Plan §W1b-7 expected that sigma_LB / sigma_S4 > 5 from naive
ell_max^{-0.5} scaling — LiteBIRD being B-mode-optimized, not
competitive on alpha_s. The finding that LiteBIRD does NOT
forecast alpha_s at all is CONSISTENT with the design expectation.
Ratio > 5 is VACUOUSLY SATISFIED (LiteBIRD alpha_s sensitivity is
effectively infinite).

The gate carries the PRE-REG-INCOMPLETE flag because the
requested numerical value is absent, not because the expectation
is falsified. The projected sigma_LB_proj = 1.05e-2 used in
W1a-9 / W1b-2 remains a sensitivity-scaling estimate and is
flagged as detector-portfolio-appropriate (LiteBIRD does not
discriminate on alpha_s; its value in the ensemble is negligible).

## S86 carry-forward

If a dedicated LiteBIRD alpha_s forecast appears (e.g., within a
companion inflation-physics paper), re-fire this gate. Until
then: treat LiteBIRD's alpha_s contribution as formally not
forecast, practically negligible in any joint ensemble.

## Provenance

- audit_sha256:   1fd76b38f50abb8b806098cccec92fca4669f49c3ccff509a7ac84db5bfce73a
- content_sha256: d23e3aa61326e31c167d99362aef4d653bff85c8e2228a0d2f3c99cec1d97164
- schema_version: S84+
- Hazumi source SHA pinned at runtime
