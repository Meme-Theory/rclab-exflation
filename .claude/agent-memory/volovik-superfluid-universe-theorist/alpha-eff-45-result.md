---
name: alpha-eff-45-result
description: S45 ALPHA-EFF-45 INFO (downgraded from PASS). Method 7c entropy deficit gives alpha=0.410 (1.06x obs). Formula alpha=S/(S_max-S). S_GGE/S_max=0.291. 10/11 methods give alpha=0.8-7.6 (outside PASS). Zubarev formula model-dependent.
type: project
---

## ALPHA-EFF-45: Non-Equilibrium Specific Heat for DM/DE

### Gate Result: INFO (2026-03-15, S45 W2-R1)

Downgraded from PASS to INFO. One method (7c) hits the PASS window [0.3, 0.5], but it uses a specific non-equilibrium formalism (Zubarev). The other 10 methods give alpha = 0.78-7.6.

### Key Numbers

- alpha_eff (Method 7c, entropy deficit): **0.4099** (1.06x observed 0.388)
- alpha_eff (Method 1a, harmonic mean): 1.060 (2.73x, reproduces S44)
- alpha_eff (Method 2a, C_kl trace): 0.782 (2.02x)
- alpha_eff range (all methods): [0.114, 7.56] (Method 3 unreliable, excluded)
- S_GGE = 1.612 nats, S_max = 5.545 nats
- S_GGE / S_max = 0.291 (non-thermality = 0.709)
- C_kl: 3/8 negative eigenvalues, |C_neg|/C_pos = 0.262

### Method 7c Formula

alpha_eff = S_GGE / (S_max - S_GGE) = S / delta_S

Derivation: Zubarev non-equilibrium thermodynamic potential gives rho_vac = -T_eff * delta_S, where:
- T_eff = E_GGE / S_GGE = 1.047 M_KK (effective temperature)
- delta_S = S_max - S_GGE = 3.933 nats (entropy deficit)
- rho_vac = -4.119 M_KK

Then alpha = E / |rho_vac| = S / (S_max - S) = 0.291 / 0.709 = 0.410.

No free parameters. S_GGE from exact 256-state ED. S_max = 8*ln(2) from mode count.

### Structural Finding

- alpha >= 1 is a structural bound for EQUILIBRIUM quantum liquids (Volovik + 3rd law)
- The NON-EQUILIBRIUM GGE can access alpha < 1 through the entropy deficit
- The DM/DE ratio becomes a function of a SINGLE dimensionless number: S/S_max
- S/S_max = 0.291 maps to alpha = 0.410, matching observation to 6%

### What Opens

- Zubarev formula cross-check needed (is it unique or one of several non-eq extensions?)
- S_GGE/S_max = 0.291 is the key number. Anything that changes it changes DM/DE.
- Epoch evolution: does S_GGE/S_max change as the GGE evolves?
- Connection to q-theory: does q-theory self-tuning produce the same formula?

### What is Excluded

- Method 3 (cross-temperature correction): UNRELIABLE (mixes C_kl susceptibility with vacuum formula)
- Methods 7a, 7b (free energy partition): E/F and TS/F are not physical vacuum energy

### Files

- Script: tier0-archive/s45_alpha_eff.py
- Data: tier0-archive/s45_alpha_eff.npz
- Plot: tier0-archive/s45_alpha_eff.png

**Why:** The DM/DE ratio may be determined by the non-thermality of the GGE, not the equilibrium specific heat exponent. The entropy deficit formula gives a parameter-free prediction.

**How to apply:** The key quantity is S_GGE/S_max = 0.291. This should be checked against the 59.8-pair GGE (not just 1-pair). The Zubarev formula needs independent derivation from the superfluid vacuum framework before the result can be promoted from INFO to PASS.
