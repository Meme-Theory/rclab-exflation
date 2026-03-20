---
name: bogoliubov-imprint-50-result
description: S50 BOGOLIUBOV-IMPRINT-50 FAIL. Leggett mass NOT imprinted in Bogoliubov spectrum. Three arguments (ground state phi_0=0, B2 mod 1e-6, RG fraction 1.7e-4). Trans-Planckian erasure (Paper 27). Bogoliubov imprint channel CLOSED for n_s.
type: project
---

## BOGOLIUBOV-IMPRINT-50 Result (Session 50 W1-C)

### Gate: FAIL (2026-03-20)

### Key Numbers

| Quantity | Value |
|:---------|:------|
| omega_L1 / omega_transit | 7.86e-5 |
| epsilon_L | 0.00248 |
| delta(Delta)/Delta (ZP) | 1.52e-3 |
| P_LZ mod depth (B2, 93% of pairs) | 1.1e-6 |
| P_LZ mod depth (B3, 5% of pairs) | 0.042 (parametric, not realized) |
| Feature amplitude in P(K) | 1.7e-9 |
| Leggett fraction in RG integrals | 1.73e-4 |
| Erasure ratio | 6.2e-9 |

### Three Arguments for FAIL

1. **Ground state symmetry**: phi_0 = 0 everywhere. <cos(phi_0)> = 0. No spatial modulation.
2. **Dominant sector insensitivity**: B2 (93% of pairs) has mod depth 1.1e-6. Shielded by large rho and Delta.
3. **Information hierarchy**: omega_L encoded at 0.017% of RG integral range. Present but invisible.

### Physical Mechanism

Trans-Planckian erasure (Paper 27, Volovik 2013). When H >> omega (here 12,721x), all quasiparticles created with n ~ 1 regardless of pre-transit structure. The Leggett mode is the exact analog of the dipolar interaction in normal-state 3He: invisible when the condensate is destroyed.

### Consequences

- Bogoliubov imprint channel CLOSED for n_s
- Quasiparticle spectrum is uniform (n_s = 1 exactly from this mechanism)
- The S49 proposal "Bogoliubov coefficients carry frozen imprint" is DISPROVEN
- omega_L exists only in the BCS condensed phase; post-transit GGE has no collective modes

### What Survives

The RG integrals DO encode omega_L at the 0.017% level, but this is:
(a) Not spatially modulated (no K-dependence)
(b) Overwhelmed by BCS amplitude structure
(c) Not detectable in any observable power spectrum

**Why:** The sudden quench (dt_transit/T_L = 1.25e-5) erases the Leggett structure. This is a STRUCTURAL result: any mechanism that relies on pre-transit collective modes being preserved through a sudden quench faces the same erasure.

**How to apply:** Future n_s attempts must NOT use pre-transit collective mode imprinting. The only surviving channels are: (1) post-transit dynamics (if any collective modes re-emerge), (2) fabric-level texture (cell-to-cell variation from KZ defects), (3) non-equilibrium effects during transit itself (not frozen in Bogoliubov).

Files: s50_bogoliubov_imprint.py, s50_bogoliubov_imprint.npz, s50_bogoliubov_imprint.png
