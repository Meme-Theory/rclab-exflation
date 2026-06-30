# MacInnis 2022 CMB-HD alpha_s forecast — PRE-REG-INCOMPLETE disposition

**Gate**: S85-W1b-CMB-HD-ALPHA-S-MACINNIS-EXPLICIT
**Verdict**: PRE-REG-INCOMPLETE
**Reason**: Source paper (arXiv:2203.05728, MacInnis et al. 2022 Snowmass
CMB-HD White Paper) is available in the project cache, but does NOT
publish an explicit sigma(alpha_s) forecast.

## MacInnis 2022 headline forecasts (read from pages 11-30)

| Parameter | MacInnis value | Section |
|:----------|:--------------|:--------|
| sigma(N_eff)           | 0.014 | 4.1 |
| sigma(f_NL^local)      | 0.26 | 5.2 |
| sigma(r) (tensor-to-scalar) | 0.005 | 9.1 |
| sigma(w_0)             | 0.005 | 6 |
| sigma(sum m_nu)        | 13 meV | 6 |
| sigma(B_SI, nG)        | 0.036 | 5.1 |
| **sigma(alpha_s)**     | **NOT PUBLISHED** | — |

## Why this is NOT a FAIL

Per plan §W1b-6 fallback clause, PRE-REG-INCOMPLETE is treated
per `.claude/rules/epistemic-discipline.md` §Pre-Registration
Completeness: a gate that cannot be evaluated because its machinery
is unpinned is NOT a FAIL — it is PRE-REG-INCOMPLETE. The projected
value sigma(alpha_s)_CMB-HD = 1.5e-3 used in W1a-9 and W1b-2 remains
a sensitivity-scaling estimate (derived from CMB-S4 scaling, not
from a published CMB-HD forecast pipeline).

## S86 carry-forward

Track publications of an explicit CMB-HD alpha_s forecast. Most
likely sources:
- Abazajian et al. CMB-HD companion papers
- CMB-HD SciBook forecast code release
- Updated CMB-HD paper incorporating alpha_s into Table

When published, re-fire this gate with the verified sigma value
and perform the ratio test.

## Downstream impact

Plan §Cross-wave rule 5: W1a-9 MULTID-FISHER ensemble flagged
PRE-REG-INCOMPLETE-ADJACENT on the alpha_s detector portfolio
(CMB-HD component uses a projection, not a published forecast).
This flag attaches as an annotation, NOT a retraction.

## Provenance

- audit_sha256:   48eccb17f5f07edf3acdfc4e89476655b6ca549e4aab77873f9b1bca6e209e16
- content_sha256: 5a30def173ea4001ddfbd14d68ec94ed8df99ee67ae98313b3e54db286457b99
- schema_version: S84+
- MacInnis source SHA pinned at runtime
