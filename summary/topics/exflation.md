---
type: topic-page
ingested-by: /weave --update
class-id: Exflation
class-tier: 0
generated: 2026-06-28
---

# Topic — Exflation — substrate cosmogenesis (acoustic white hole)

> Auto-generated from `computations/_shared/canonical_classes.py` via `tools/build_topic_pages.py`. Edits to this file will be overwritten by the next `/weave --update`. To change the content, edit the class definition or its CLASS_EDGES entries in canonical_classes.py.

**Class ID**: `Exflation`  
**Tier**: 0 (root)  
**Parent class**: (root)  
**Seed session**: `S38`  
**Member count**: 34 (0 sub-classes)

## Scope

The framework's cosmogenesis process end-to-end: the Jensen deformation parameter tau cascading from an unstable maximum at tau=0 through the van-Hove fold (tau_fold=0.19) into the post-fold GGE relic plateau. Replaces inflation with a first-order phase transition driven by dS/dtau=+58,672; replaces the Big Bang singularity with a supersonic transit (Mach=13.75). What cosmologists call 'particle creation' IS the eigenvalue spectrum reorganization at the fold — n_pairs=59.8 Bogoliubov pairs, P_exc_kz=1 exactly. Post-fold dynamics are an acoustic white hole with impedance Gamma_effacement=0.99970 transmitting structure and (1-Gamma)=3e-4 residual constituting dark-energy-like leakage. Headline predictions: w0_FW = -0.918, n_s_framework = 0.9561.

## Members (34)

| Constant | Role | Value | Comment |
|:---------|:-----|:------|:--------|
| `Gamma_effacement` | PRIMARY | 0.9997 | Acoustic-white-hole impedance = 0.99970; (1-Gamma)=3e-4 = effacement residual |
| `H_fold` | PRIMARY | 586.5 | Hubble parameter at fold = 586.5 (M_KK units); expansion rate during transit |
| `Mach_max_framework` | PRIMARY | 13.75 | Mach number at fold = 13.75; defining property — supersonic transit IS the acous |
| `P_exc_kz` | PRIMARY | 1 | Kibble-Zurek excitation probability = 1.0 exactly; saturation (no Landau-Zener a |
| `S_fold` | PRIMARY | 2.504e+05 | Spectral action at fold = 250,360.7; absolute energy scale of cascade event |
| `T_acoustic` | PRIMARY | 0.112 | GGE acoustic temperature = 0.112 M_KK; relic's effective acoustic temperature on |
| `c_BLV` | PRIMARY | 0.485 | BLV post-fold scalar sound speed = 0.485 (S64); GGE-relic phonon sector |
| `c_fabric` | PRIMARY | 210 | Substrate sound speed = 209.97; Mach denominator (Mach=v_terminal/c_fabric) |
| `dS_fold` | PRIMARY | 5.867e+04 | Spectral action gradient at fold = +58,672; substrate-driver of cascade (the 'in |
| `dt_transit` | PRIMARY | 0.00113 | Transit duration = 1.13e-3 M_KK^-1; impulsiveness defines KZ freezing window |
| `n_Bog` | PRIMARY | 0.9986 | Bogoliubov fraction per mode = 0.9986; pins per-mode GGE distribution shape |
| `v_terminal` | PRIMARY | 26.54 | Terminal velocity of modulus = 26.545 (M_KK units); kinematic state at fold |
| `n_pairs` | CONSEQUENCE | 59.8 | Bogoliubov pairs from transit = 59.8; produced BY cascade, becomes PRIMARY in an |
| `n_s_framework` | OBSERVABLE_OUTPUT | 0.9561 | Framework scalar spectral index at CMB pivot = 0.9561 (S84 T6); Planck/CMB-S4 te |
| `w0_FW` | OBSERVABLE_OUTPUT | -0.918 | Framework dark-energy EOS w_0 = -0.918 (Volovik vacuum + effacement); DESI/Eucli |
| `E_exc` | DERIVED | 60.62 | Total excitation energy from BCS transit quench (= E_exc_ratio * /E_cond/) |
| `E_exc_ratio` | DERIVED | 443 | Excitation/condensation ratio = 443.0; Schwinger-instanton-duality measure |
| `N_pivot` | DERIVED | 64.08 | CMB pivot e-fold count = 64.08 = 55 + ln(c/c_s); substrate-c_s correction to LCD |
| `T_compound` | DERIVED | 7.578 | Microcanonical post-fold compound temperature (= E_exc / 8 across BCS Fock modes |
| `Z_fold` | DERIVED | 7.473e+04 | Gradient stiffness at fold; G_DeWitt-weighted moduli-space stiffness |
| `d2S_fold` | DERIVED | 3.179e+05 | Curvature of spectral action at fold; characterizes width of fold transit |
| `omega_att` | DERIVED | 1.43 | Post-fold attractor frequency = 1.430; geometric from spectral action curvature  |
| `omega_tau` | DERIVED | 8.27 | Transit frequency d(tau)/dt; algebraic from v_terminal + modulus mass |
| `Q_Leggett` | RELATED | 6.7e+05 | Leggett mode quality factor 6.7e5 (S50); cascade-survivor DM candidate |
| `T_BCS` | RELATED | 0.64 | BCS canonical temperature 0.640; substrate-pairing scale partially surviving tra |
| `T_c_BCS` | RELATED | 0.083 | BCS critical temperature 0.083; post-fold residual-pairing scale |
| `eps_H_W6` | RELATED | 0.02163 | Slow-roll bound from S80 dS/dtau at fold; interface between substrate and slow-r |
| `kappa_BCS` | RELATED | 4.019 | BCS surface-gravity analog 4.019 (S69); white-hole side characterization |
| `m_tau` | RELATED | 2.062 | Modulus mass at fold = 2.062; inertial response to dS_fold gradient |
| `phi_paasch` | RELATED | 1.532 | Paasch spectral ratio (PROVEN, S12); substrate-static identity pre-dating cascad |
| `tau_fold` | RELATED | 0.19 | Cascade transits THROUGH this tau locus; PRIMARY in fold, RELATED here (per user |
| `tau_overshoot` | RELATED | 1.614 | Overshoot turnaround at K=53.35 (S77); post-fold modulus dynamics first turnarou |
| `tau_phase_trans` | RELATED | 0.5372 | C^2 sectional K=0 phase transition (S48); second tau-landmark beyond tau_fold |
| `v_crit` | RELATED | 219.3 | Censorship critical velocity = 219.3; transit just barely satisfies v_terminal < |

## By role

### PRIMARY (12)

_defining constants — the class cannot be described without them_

- **`Gamma_effacement`** = 0.9997 — Acoustic-white-hole impedance = 0.99970; (1-Gamma)=3e-4 = effacement residual
  - _Also in: [CC](./cc.md) (RELATED)_
- **`H_fold`** = 586.5 — Hubble parameter at fold = 586.5 (M_KK units); expansion rate during transit
  - _Also in: [fold](./fold.md) (DERIVED)_
- **`Mach_max_framework`** = 13.75 — Mach number at fold = 13.75; defining property — supersonic transit IS the acoustic white hole
- **`P_exc_kz`** = 1 — Kibble-Zurek excitation probability = 1.0 exactly; saturation (no Landau-Zener adiabaticity)
  - _Also in: [fold](./fold.md) (DERIVED)_
- **`S_fold`** = 2.504e+05 — Spectral action at fold = 250,360.7; absolute energy scale of cascade event
  - _Also in: [fold](./fold.md) (PRIMARY)_
- **`T_acoustic`** = 0.112 — GGE acoustic temperature = 0.112 M_KK; relic's effective acoustic temperature on substrate (algebraic GGE permanence)
- **`c_BLV`** = 0.485 — BLV post-fold scalar sound speed = 0.485 (S64); GGE-relic phonon sector
- **`c_fabric`** = 210 — Substrate sound speed = 209.97; Mach denominator (Mach=v_terminal/c_fabric)
  - _Also in: [fold](./fold.md) (RELATED)_
- **`dS_fold`** = 5.867e+04 — Spectral action gradient at fold = +58,672; substrate-driver of cascade (the 'inflaton field' in container language)
  - _Also in: [fold](./fold.md) (PRIMARY)_
- **`dt_transit`** = 0.00113 — Transit duration = 1.13e-3 M_KK^-1; impulsiveness defines KZ freezing window
  - _Also in: [fold](./fold.md) (DERIVED)_
- **`n_Bog`** = 0.9986 — Bogoliubov fraction per mode = 0.9986; pins per-mode GGE distribution shape
  - _Also in: [fold](./fold.md) (DERIVED)_
- **`v_terminal`** = 26.54 — Terminal velocity of modulus = 26.545 (M_KK units); kinematic state at fold
  - _Also in: [fold](./fold.md) (DERIVED)_

### CONSEQUENCE (1)

_produced by the class's process; becomes a downstream-class PRIMARY_

- **`n_pairs`** = 59.8 — Bogoliubov pairs from transit = 59.8; produced BY cascade, becomes PRIMARY in any future GGE-relic class
  - _Also in: [fold](./fold.md) (DERIVED)_

### OBSERVABLE_OUTPUT (2)

_external-cosmology testable predictions — the class's headline observables_

- **`n_s_framework`** = 0.9561 — Framework scalar spectral index at CMB pivot = 0.9561 (S84 T6); Planck/CMB-S4 testable
- **`w0_FW`** = -0.918 — Framework dark-energy EOS w_0 = -0.918 (Volovik vacuum + effacement); DESI/Euclid testable

### DERIVED (8)

_algebraic / definitional consequences — unit conversions, ratios of PRIMARY members_

- **`E_exc`** = 60.62 — Total excitation energy from BCS transit quench (= E_exc_ratio * |E_cond|)
- **`E_exc_ratio`** = 443 — Excitation/condensation ratio = 443.0; Schwinger-instanton-duality measure
- **`N_pivot`** = 64.08 — CMB pivot e-fold count = 64.08 = 55 + ln(c/c_s); substrate-c_s correction to LCDM
- **`T_compound`** = 7.578 — Microcanonical post-fold compound temperature (= E_exc / 8 across BCS Fock modes)
- **`Z_fold`** = 7.473e+04 — Gradient stiffness at fold; G_DeWitt-weighted moduli-space stiffness
  - _Also in: [fold](./fold.md) (DERIVED)_
- **`d2S_fold`** = 3.179e+05 — Curvature of spectral action at fold; characterizes width of fold transit
  - _Also in: [fold](./fold.md) (PRIMARY)_
- **`omega_att`** = 1.43 — Post-fold attractor frequency = 1.430; geometric from spectral action curvature at attractor
- **`omega_tau`** = 8.27 — Transit frequency d(tau)/dt; algebraic from v_terminal + modulus mass
  - _Also in: [fold](./fold.md) (RELATED)_

### RELATED (11)

_kindred observables from sister classes, or boundary conditions; not native to this class_

- **`Q_Leggett`** = 6.7e+05 — Leggett mode quality factor 6.7e5 (S50); cascade-survivor DM candidate
- **`T_BCS`** = 0.64 — BCS canonical temperature 0.640; substrate-pairing scale partially surviving transit
- **`T_c_BCS`** = 0.083 — BCS critical temperature 0.083; post-fold residual-pairing scale
- **`eps_H_W6`** = 0.02163 — Slow-roll bound from S80 dS/dtau at fold; interface between substrate and slow-roll-equivalent observables
- **`kappa_BCS`** = 4.019 — BCS surface-gravity analog 4.019 (S69); white-hole side characterization
- **`m_tau`** = 2.062 — Modulus mass at fold = 2.062; inertial response to dS_fold gradient
  - _Also in: [fold](./fold.md) (RELATED)_
- **`phi_paasch`** = 1.532 — Paasch spectral ratio (PROVEN, S12); substrate-static identity pre-dating cascade
  - _Also in: [fold](./fold.md) (RELATED)_
- **`tau_fold`** = 0.19 — Cascade transits THROUGH this tau locus; PRIMARY in fold, RELATED here (per user-confirmed taxonomy)
  - _Also in: [GR](./gr.md) (RELATED), [fold](./fold.md) (PRIMARY)_
- **`tau_overshoot`** = 1.614 — Overshoot turnaround at K=53.35 (S77); post-fold modulus dynamics first turnaround
- **`tau_phase_trans`** = 0.5372 — C^2 sectional K=0 phase transition (S48); second tau-landmark beyond tau_fold
- **`v_crit`** = 219.3 — Censorship critical velocity = 219.3; transit just barely satisfies v_terminal < v_crit

## Consumer gates

_(no consumer gates yet — topic pages do not currently carry Input-SHA pins. When gates start citing topic pages as authoritative data, list them here.)_

## Change log

| Date | Session | Change | Author |
|:-----|:--------|:-------|:-------|
| 2026-06-28 | S86-W*-build_topic_pages | auto-generated from canonical_classes.py | build_topic_pages.py |

---

**Visualizer**: open `tools/viz/console/index.html` and select `Exflation` from the `▣ classes` dropdown in the Connections tab to see the radial member graph (color-coded by role).
