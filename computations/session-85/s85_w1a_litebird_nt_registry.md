# Registry patch -- S85 W1a-8 LiteBIRD n_T STRUCTURAL-FLOOR landing

**Gate**: S85-W1a-LITEBIRD-NT-REGISTRY-LANDING
**Verdict**: PASS
**Target row**: new row in permanent-results-registry for LiteBIRD n_T blue-tilt localization.

## Audit result

- n_T at transit scale: +0.4680 (S65 W5-65)
- n_T at CMB scale:     -0.003024 (S66 TENSOR-TRANSFER)
- separation |transit - CMB|: 0.471024
- Decade separation: 54 (transit k vs CMB k)

## Normalized by LiteBIRD sigma_nT

| Scenario       | sigma_nT    | normalized | S84 W4-41 bracket |
|:---------------|:------------|:-----------|:-------------------|
| Canonical (S84) | 8e-04 | 588.78  | [540, 654]: YES |
| Optimistic      | 1e-04 | 4710.24 | (strawman floor) |
| Pessimistic     | 8e-03 | 58.88  | (delensing degraded) |

## Registry action

**PASS** => row LANDS as STRUCTURAL-FLOOR. Provenance: "S65 NT-BLUE-65 + S66 TENSOR-TRANSFER + S84 W4-41 EVOI=0".

## What STRUCTURAL-FLOOR means

The n_T separation between transit scale (blue tilt +0.468, dominated
by acoustic pile-up at van Hove fold) and CMB scale (slow-roll
consistency n_T ~ -r/8) is a GEOMETRIC property of the substrate
transit-to-CMB transfer function over 54 decades of k-space
(S66 TENSOR-TRANSFER). LiteBIRD cannot see the transit-scale blue
tilt -- NOT because the framework prediction is wrong, but because
the tilt is LOCALIZED at a scale 54 decades above what LiteBIRD
probes. This is GEOMETRY, not detector limitation.

EVOI for LiteBIRD 2030-2040 on this prediction is ZERO (no Bayesian
update possible from a detector that cannot access the relevant k-mode).
The framework's flagship tensor-channel detector is the fabric-transit
CGWB at LISA (see W1a-6, W1a-7) and NOT LiteBIRD.

## Provenance

- audit_sha256:   f5a285d8548129b053b0c34d54043f7fd00487ee4549d43cf367fff015f6c8b7
- content_sha256: 0c1ab0e9ab063c59e8d8d3c10ddc6aeab667cb414200a0f92d2a7dbcf1b203ba
- schema_version: S84+
