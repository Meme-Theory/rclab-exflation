# alpha_s recalibration: Planck 2018 → ACT DR4 (post-2018 real data)

**Gate**: S85-W1b-PLANCK-DESI-2025-ALPHA-S-RECALIBRATION

## Audit: plan-named sources do NOT tabulate alpha_s

| Source | Status | Pages | alpha_s hits | Has tabulation |
|:-------|:-------|:------|:-------------|:---------------|
| Tristram et al. 2023 PR4 (arXiv:2309.10034) | scanned | 21 | 0 | NO |
| DESI 2024 III BAO (arXiv:2404.03000) | scanned | 71 | 0 | NO |
| DESI 2024 VI Cosmology (arXiv:2404.03002) | scanned | 71 | 0 | NO |

Planck PR4 runs baseline-LCDM only; DESI is a BAO/late-universe experiment and doesn't measure inflationary α_s.

## Real post-2018 source: ACT DR4 (Aiola 2020, arXiv:2007.07288 Table 5)

| Combination | α_s = dns/dlnk | σ |
|:-----------|:---------------|:--|
| ACT alone            | +0.0690  | 0.0290 |
| ACT+WMAP (P-indep)   | +0.0128  | 0.0081 |
| **ACT+Planck**       | **+0.0023**  | **0.0063** ← primary post-2018 best-combined |
| Planck-alone (ACT's τ prior) | -0.0067  | 0.0067 |

## Primary analysis: ACT+Planck (post-2018 best) vs Planck 2018 canonical

| Quantity | Value |
|:---------|:------|
| α_2018 (canonical) | -0.0045 ± 0.0067 (Planck 2018 VI) |
| α_2020 (ACT+Planck) | +0.0023 ± 0.0063 (Aiola 2020 Table 5 col 3) |
| Δα = α_2020 − α_2018 | **+0.006800** |
| \|Δα\| / σ_2018 | **1.0149** |

Thresholds (plan §W1b-8): PASS iff |Δα| < σ/3 = 0.002233; FAIL iff > σ = 0.006700.

## Audit-robustness: alternative combinations

| Combination | α_combined | σ_combined | Δα | Ratio Δα/σ_2018 |
|:-----------|:-----------|:-----------|:---|:----------------|
| Planck 2018 + ACT+WMAP (altA, inverse-var, Planck-independent) | +0.002528 | 0.005163 | +0.007028 | 1.049 |
| Planck 2018 + ACT-alone (altB, inverse-var) | -0.000776 | 0.006528 | +0.003724 | 0.556 |

## What this result means

The framework's canonical `alpha_s = -0.0045 ± 0.0067` (Planck 2018) has
drifted by |Δα| = 0.0068 when post-2018 ACT DR4
data is incorporated. All three treatments (ACT+Planck primary, ACT+WMAP
alt, ACT-alone alt) show |Δα| > σ_2018/3, meaning the canonical pin is
no longer within the PASS band.

Under plan §Cross-wave rule 6, FAIL (|Δα| > σ_2018) triggers a
canonical-constants update. Recommended new pin:
```
alpha_s_canon_2020 = +0.0023 ± 0.0063  (ACT+Planck, Aiola 2020 Table 5)
```
All pre-update S85 verdicts remain permanent per `.claude/rules/gate-verdicts.md`,
but future gates consuming `alpha_s_canon` should use the 2020 value.

## Provenance

- audit_sha256:   594929470c94342a9e23d381f5a1c21cbd87a28c0827a2a55197e81e67b4b946
- content_sha256: 6b2f30855cf48f8c12d7d8858dc639ba80d356e3554c9f7ab818780a6fae11f4
- schema_version: S84+
- Source SHAs pinned at runtime (Planck 2018 VI, Tristram PR4, DESI III, DESI VI, ACT DR4)
