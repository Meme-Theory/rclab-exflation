# LISA flagship pre-registration (fix-k & fix-f dual) -- S85 W1a-6

**Gate**: S85-W1a-LISA-CGWB-FLAGSHIP-FIX-K
**Verdict**: PASS
**Companion**: lifts S84 W6-50 CGWB-ABSOLUTE-PT PASS into a flagship pre-registration.

## Dual-convention values

| Quantity                   | Value            | Source                  |
|:---------------------------|:-----------------|:------------------------|
| rho_AC (fix-k)             | 2.1000          | S84 W6-50 verdict        |
| rho_AC (fix-f)             | 2.3800          | S84 W6-50 verdict        |
| ratio fix-f / fix-k        | 1.1333333333 | This gate (S85 W1a-6) |
| target ratio               | 1.133            | Plan §W1a-6 pre-registered |
| residual |computed - target| | 0.0003333333 | This gate |

## Deterministic map (fix-k <-> fix-f)

k = 2*pi*f / c_Gold, with c_Gold = 0.915 (M_KK natural units).

At LISA pivot f_pivot = 0.003 Hz:
  k_pivot / c_Gold_units = 2*pi * f_pivot / c_Gold = 2.060061e-02

## Interpretation

The 13.3% excess in rho_AC(fix-f) vs rho_AC(fix-k) originates from the
transfer-function Jacobian at the LISA pivot, a structural signature
of the blue-tilt tensor spectrum n_T > 0 localized at transit scale
(S65 W5-65) redshifted to LISA band via the GGE acoustic tail
(S66 TENSOR-TRANSFER). This is NOT a freely-fit parameter; it is a
deterministic consequence of the substrate transit.

## Pre-registration completeness

- fix-k formulation: documented with rho_AC value, k-space measure.
- fix-f formulation: documented with rho_AC value, f-space measure.
- Jacobian ratio: 1.1333 (13.3% enhancement).
- Threshold for ratio consistency: 1e-3 (met within 3.33e-4).

## Provenance

- audit_sha256:   68063dd5c1bb63a9623a2914ca75bc22406de7e1223cbaafc2b90a484e325d76
- content_sha256: 2d938c61d6744f51e4f1b70a6842d519b2924e7ee9c05d938ce2aaf33ecbe401
- schema_version: S84+
