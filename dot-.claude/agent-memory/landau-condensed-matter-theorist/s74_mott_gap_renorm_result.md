---
name: S74 W4-P MOTT-GAP-RENORMALIZATION-74 Result
description: Mott charging gap redshift from fold to today, canonical a^-1 scaling gives 1.04e-32 eV (ultralight); closes Mott-as-DM channel under both a^-1 and a^0 readings
type: project
---

# S74 W4-P MOTT-GAP-RENORMALIZATION-74 Result

**Gate**: PASS. E_C_today identified in all four units {GeV, eV, M_Pl_reduced, M_Pl_unreduced}.

## Key numbers

- E_C_fold = 0.46425474 M_KK = 3.4488e+16 GeV (S66 ROUTE2-OES, Delta_0_OES canonical)
- N_total = 132.4488 e-folds (EFOLD-MAPPING-73B canonical, from s73b_efold_mapping.npz)
- a_fold/a_today = 3.0076e-58, a_today/a_fold = 3.3249e+57

### Three redshift assumptions

| scaling | E_C_today [GeV] | [eV] | Detector band |
|---|---:|---:|---|
| a^-1 frequency (CANONICAL) | 1.0373e-41 | 1.0373e-32 | ultralight |
| a^-2 kinetic | 3.1197e-99 | 3.1197e-90 | below floor |
| a^0 pinned | 3.4488e+16 | 3.4488e+25 | above ceiling |

## Permanent structural results

1. **Horizon-scale alignment**: lambda_mode_today / (c/H_0) = 0.139. Follows from E_C_fold / H_fold = 1.17 via common a^-1 redshift. PERMANENT structural identity -- any Josephson network built on the same fabric whose emergent curvature sets H_fold will redshift to a horizon-fraction wavelength today. Not tuning.
2. E_C_today / H_0 = 7.21 (mode still underdamped by Hubble friction)
3. Period 2*pi/f_C_today = 12.6 Gyr (within factor ~3 of age of universe)

## Constraint map tightening

- Mott gap == DM candidate under a^-1: CLOSED (11 OOM below Lyman-alpha fuzzy-DM bound m > 1e-21 eV)
- Mott gap == DM candidate under a^0 pinned: CLOSED (GUT-scale UV quasiparticle decouples from Hubble dynamics)
- **Mott gap is the DM channel: CLOSED by both readings** -- permanent constraint-map tightening
- DM channel remains the Leggett-1 mode (S66 LEGGETT-SPECTRAL PASS, Q=18.6, omega_L1=0.138 M_KK)
- Under a^-1, omega_L1_today = 3.08e-33 eV (3.4x below Mott gap, same ultralight band); fold ratio omega_L1/E_C = 0.297 preserved by common scaling

## Two-layer architecture confirmed

- Spectral (all-sector): governs gravity and H_0
- BCS-sector: governs DM and pairing
- Mott gap belongs to BCS sector as a PHASE-DIFFUSION DECOHERENCE scale (enters A_s via W2-F delta_OOM_Mott=0.141), NOT as a DM mass

## Files

- Script: computations/s74_mott_gap_renormalization.py
- Data: computations/s74_mott_gap_renormalization.npz (34 keys)
- Plot: computations/s74_mott_gap_renormalization.png
