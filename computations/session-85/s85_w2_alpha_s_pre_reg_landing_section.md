## §VII.M.2 — Event-driven alpha_s and beta_s pre-registrations (S82-S85 consolidated)

**Consolidation source**: S85 W2-8 (S85-W2-ALPHA-S-PRE-REG-REGISTRY-LANDING).

**Canonical central values** (from S50 + S84 W8-86 OZ-derivation):
  - alpha_s = -0.068968 (= n_s^2 - 1 at Planck n_s central)
  - beta_s  = -0.1331 (3rd Taylor coefficient)

**Per-pre-reg table**:

| Pre-reg ID | Observable | Detector | σ(1σ) | Pass-band | Prior |
|:-----------|:-----------|:---------|:------|:----------|:------|
| CMB-S4-ALPHA-FLAGSHIP | alpha_s | CMB-S4 | 0.002 | (-0.073, -0.065) | framework (zero-free-parameter) |
| CMB-HD-ALPHA-S-MACINNIS-EXPLICIT | alpha_s | CMB-HD | 0.0013 | (-0.0716, -0.0663) | framework (zero-free-parameter) |
| LITEBIRD-ALPHA-S-HAZUMI-VERIFIED | alpha_s | LiteBIRD | 0.006 | (-0.081, -0.057) | framework (zero-free-parameter) |
| ALPHA-S-JOINT-FISHER-CORRELATED | alpha_s | joint (S4 + SO + HD + LiteBIRD) | 0.00108 | (-0.0711, -0.0668) | framework (zero-free-parameter) |
| ALPHA-S-PRIOR-RANGE-LCDM | alpha_s | LCDM prior predictive | N/A | None | LCDM slow-roll model catalog (Martin+ 2014 Encyclopaedia Inflationaris) |
| ALPHA-S-TRANSIT-PS-67-SIMULTANEOUS | alpha_s | S84 registry (3 rows) | 0.0 | (-0.068968, -0.068968) | framework (resolves contradiction) |
| BETA-S-CMB-S4-PREREG | beta_s | CMB-S4 | 0.0022 | (-0.1375, -0.1287) | framework (3rd Taylor coefficient) |
| W1a-ALPHA-S-REGISTRY-UPGRADE | alpha_s (meta: registry-row upgrade) | registry-internal | 0.0 | (-0.068968, -0.068968) | framework (promotes numerical identity to zero-free-parameter theorem) |

**Scheme lockouts** (from W10-123 axiom closure chain):
  1. No post-data auxiliary couplings.
  2. No n_s redefinition.
  3. No derivation-chain change.
  4. No pivot migration.
  5. No axiom subtraction.
  6. No detector cherry-picking.
