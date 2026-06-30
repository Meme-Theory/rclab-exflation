# Registry patch -- S85 W1a-2 alpha_s partition-invariance audit

**Gate**: S85-W1a-ALPHA-S-REGISTRY-UPGRADE
**Verdict**: FAIL
**Target row** (pre-gate): `alpha_s` identity (S50-51 atlas) "alpha_s = n_s^2 - 1".

## Audit result

Scheme A (topological): alpha_s^(A) = n_s_framework^2 - 1 = -0.079360
Scheme B (spectral, CV^2 norm): alpha_s^(B) = +0.013582
Scheme B (raw Var, dimensional): alpha_s^(B) = +1.263924

Cross-scheme residual (CV^2 variant): |A - B| / alpha_s_obs = 0.7876
Cross-scheme residual (raw variant):  |A - B| / alpha_s_obs = 11.3838

PDG agreement pulls (alpha_s(M_Z) = 0.1180 +/- 0.0010):
- pull_A        = 197.4 sigma
- pull_B_CV^2   = 104.4 sigma
- pull_B_raw    = 1145.9 sigma

## Registry action

**FAIL** - registry row STAYS single-scheme; partition-invariance claim RETRACTED from S84 permanent-results row for alpha_s.

## Provenance

- audit_sha256:   3cf7dd462069c16f68e0947cd8d3d2e66b931d927cad676faede39026f0c88b4
- content_sha256: ad873f62e3fd40d91869a04b86b4da49b1034a48cb5d5e0530290c9080f15381
- schema_version: S84+
- L_max truncation for SU(3) Casimir spectrum: 10
- Peter-Weyl multiplicity convention: dim^2
- N_irreps (L_max=10, p+q <= L_max, excluding trivial): 65
- <D_K^0> (total weighted count): 611610
