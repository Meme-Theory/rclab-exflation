# Framework-Registry Rectification Diff Report

**Generated**: 2026-04-23T21:21:52.837545

The framework folder (`sessions/framework/*.md`) is the canonical destination for knowledge. This diff cross-checks session-level extractions against framework-registry entries. When the two disagree on the authoritative field, the **framework is wins** and the session file should be updated.

## Summary

| Bucket | Framework entries | Session entries | Overlap | Agree | **Disagree** | Framework-only | Session-only |
|:-------|------------------:|----------------:|--------:|------:|-------------:|--------------:|-------------:|
| theorems | 692 | 1056 | 14 | 9 | **5** | 678 | 1042 |
| closed_mechanisms | 44 | 456 | 2 | 1 | **1** | 42 | 454 |
| gates | 49 | 587 | 8 | 3 | **5** | 41 | 579 |
| open_channels | 135 | 436 | 5 | 5 | **0** | 130 | 431 |

**Total WARRANTs (disagreements)**: 11

## WARRANT entries

For each disagreement, the framework-registry value is authoritative. The session file should be updated to match, or the disagreement should be resolved through explicit session work (with a new framework-registry entry that supersedes).

### theorems

| Name | Framework value | Session value | Framework source | Session source |
|:-----|:----------------|:--------------|:-----------------|:---------------|
| a_2(fold) | Second Seeley-DeWitt coefficient | PROVEN | `sessions/framework/registry/baseline-findings-s66.md` | `sessions\session-75\session-75-results-workingpaper.md` |
| c_BLV | Fabric sound speed | PROVEN | `sessions/framework/registry/baseline-findings-s66.md` | `sessions\session-82\session-82-results-workingpaper.md` |
| Perturbative Exhaustion Theorem | Standard first-order phase transition thermodynamics with metastable branches. | PROVEN | `sessions/framework/Atlas/atlas-07-permanent-results.md` | `sessions\archive\session-23\session-23-sagan-verdict.md` |
| Volume-preserving TT-deformation | dirac_spectrum.py | PROVEN | `sessions/framework/Atlas/atlas-07-permanent-results.md` | `sessions\archive\session-22\session-22-master-synthesis.md` |
| WALL | PASS | PROVEN | `sessions/framework/Atlas/atlas-07-permanent-results.md` | `sessions\session-82\session-82-OOM.md` |

### closed_mechanisms

| Name | Framework value | Session value | Framework source | Session source |
|:-----|:----------------|:--------------|:-----------------|:---------------|
| Tesla g·N(0) ~ 8-10 | RETRACTED | corrected to 3.24 by block-diagonality | `sessions/framework/registry/constraint-mega-matrix.md` | `sessions\archive\session-22\session-22-master-synthesis.md` |

### gates

| Name | Framework value | Session value | Framework source | Session source |
|:-----|:----------------|:--------------|:-----------------|:---------------|
| BA-31 | FAIL | Diagnostic | `sessions/framework/registry/constraint-mega-matrix.md` | `sessions\archive\session-31\session-31Aa-synthesis.md` |
| BA-LIFETIME-FABRIC-67 | PASS | min(Gamma/H) = 8.83e52, 53 OOM margin, all 256 BA modes overdamped (Q<2) | `sessions/framework/registry/baseline-findings-s66.md` | `sessions\session-67\session-67-results-workingpaper.md` |
| BAYESIAN-FUNCTIONAL-67 | PASS | BMA n_s=0.969+/-0.022 (0.18 sigma). w_sqrt=0.813 (CMB), 1.000 (CMB+m_H). Omega_D | `sessions/framework/registry/baseline-findings-s66.md` | `sessions\session-67\session-67-results-workingpaper.md` |
| EFOLD-MAPPING-52 | FAIL | N_e=0.1734, K_pivot=0.841 | `sessions/framework/registry/constraint-mega-matrix.md` | `sessions\session-52\session-52-results-workingpaper.md` |
| TENSOR-BURST-64 | PASS | r_CMB = 0.033 < 0.036 (nonBD, no duty cycle) | `sessions/framework/registry/constraint-mega-matrix.md` | `sessions\session-64\session-64-results-workingpaper.md` |
