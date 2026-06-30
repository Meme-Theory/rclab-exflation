# OZ-Class Landau Falsifier Table (S85 W3-12)

**Generated**: from S85 W3-12 audit; observational face of the Landau structural block (W3-8). Each row is a spectral observable of D_K, sha256-pinned to a gate verdict.

| Observable | Predicted | Regulator spread | Landau exponent | Detector | Source gate | SHA |
|------------|-----------|------------------|-----------------|----------|-------------|-----|
| A_s | 3.2994349182266295e-09 | N/A (single regulator W3-7; W3-1 5-atlas pin) | −1 (mean-field power law absent for A_s; CW collapsed S58) | Planck 2018 + LiteBIRD + CMB-S4 | S85-W3-CF-1-BRANCH-A-A_S-CLOSURE-K2035 | b59acafa69463e16 |
| n_s | 0.9649 | 0.0042 (Planck 1-sigma; framework match within 0.5-sigma per S58 BCS-CW) | 0 (constant; mean-field n_s trivial across corridor) | Planck 2018 (canonical), CMB-S4 (≤ 0.001 forecast) | canonical_constants.planck_ns + S58 BCS-CW INFO | canonical-file-p |
| alpha_s | 0.12523524390551755 | cross-regulator: W1a SCHEME-DEP value 0.125 (FAIL); W1a registry=0.788 (FAIL) | −1 (alpha_s = n_s² − 1 per S50 atlas) | CMB-S4 alpha_s (1-sigma ~ 0.002) | S85-W1a-SCHEME-DEP | c9a2beaf9a0ce862 |
| beta_s | 60.49999999999999 | MS-bar canonical (single scheme; W0 sub-PASS) | N/A (third-derivative; mean-field ansatz subcritical) | CMB-S4 beta_s (1-sigma forecast ~ 0.005) | S85-BETA-S-CMB-S4-PREREG | 50a3ca8798488ee4 |
| r_TT | 588.7800000000001 | STRUCTURAL-FLOOR scheme; transfer-function-54-decade convention | r ≠ 16ε per VdD-Hawking workshop INAPPLICABLE (5 independent arguments) | LiteBIRD r ~ 0.001 / BICEP r ~ 0.01 sensitivity | S85-W1a-LITEBIRD-NT-REGISTRY-LANDING | f5a285d8548129b0 |
| mu_FIRAS | np.float64(8.694901226608571e-05) | 0 (W3-1 5-regulator atlas, gamma=1 lockout: machine precision) | N/A (gamma=1 fixed point; not a critical exponent) | PIXIE 1-sigma ~ 1e-8; mu_FW = 8.69e-5 (4 OOM separation from LCDM 2e-8) | S85-W3-CF-5-PIXIE-KMFIRAS-PREREG | a5fd4a36e2760911 |
| N_eff | 3.046 (framework matches LCDM; S35 N_EFF resolved) | N/A (zero-free-parameter prediction matches LCDM canonical) | 0 (no K-dependent shift on inflationary corridor) | Planck 2018 + ACT + CMB-S4 sigma(N_eff) ~ 0.03 | S35-N-EFF-CLOSURE (memory trace) | external-S35-tra |

**Pin status**: 7/7 rows pinned, 0 unpinned.
