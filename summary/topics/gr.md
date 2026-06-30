---
type: topic-page
ingested-by: /weave --update
class-id: GR
class-tier: 0
generated: 2026-06-28
---

# Topic — Emergent General Relativity (a_2 channel)

> Auto-generated from `computations/_shared/canonical_classes.py` via `tools/build_topic_pages.py`. Edits to this file will be overwritten by the next `/weave --update`. To change the content, edit the class definition or its CLASS_EDGES entries in canonical_classes.py.

**Class ID**: `GR`  
**Tier**: 0 (root)  
**Parent class**: (root)  
**Seed session**: `S44`  
**Member count**: 29 (0 sub-classes)

## Scope

Constants of substrate-emergent General Relativity. GR is NOT fundamental in this framework: the Einstein-Hilbert action arises as the second Seeley-DeWitt coefficient a_2 of the spectral action on the Jensen-deformed SU(3) Dirac operator. Newton's constant satisfies 1/(16 pi G_N) = f_2 * a_2 * M_KK^2 (Sakharov / Chamseddine-Connes); the Planck mass and Planck units inherit. Members partition into (i) PRIMARY emergence machinery (a2_fold, M_KK, f_2, c_S_canon, Lambda_Planck, d_spec, R_protected_fold), (ii) EMERGENT_FROM observables (G_N, M_Pl_*, l_Planck, t_Planck, rho_crit_GeV4), (iii) DERIVED unit conversions and slow-roll proxies, and (iv) RELATED Friedmann boundary conditions. CC and KK are SISTER classes (different spectral moments — a_0 and M_KK extraction respectively).

## Members (29)

| Constant | Role | Value | Comment |
|:---------|:-----|:------|:--------|
| `Lambda_Planck` | PRIMARY | 1 | Planck-scale regulator in M_KK units (= 1.0 default, S85 W6-3) |
| `M_KK` | PRIMARY | 7.429e+16 | KK scale fixes dimensional anchor of a_2 channel; KK class owns extraction, GR u |
| `R_protected_fold` | PRIMARY | 1.129 | L_max-invariant ratio a_0*a_4/a_2^2; ties GR (a_2) to CC (a_0) and YM (a_4) chan |
| `a2_fold` | PRIMARY | 2776 | Second Seeley-DeWitt coefficient at fold; sole source of EH action 1/(16 pi G_N) |
| `c_S_canon` | PRIMARY | 1 | Canonical spectral-action scale normalization (Chamseddine-Connes 1997) |
| `d_spec` | PRIMARY | 3 | Classical spectral dimension of D_K = 3 (Connes-Moscovici); gates which SDW term |
| `f_2_default` | PRIMARY | 2.34 | f_2 spectral cutoff moment (S62 W1 Gaussian-cutoff = 2.34); regulator-pinned pre |
| `G_N` | EMERGENT_FROM | 6.674e-11 | Newton's constant from 1/(16 pi G_N) = f_2 a_2 M_KK^2; substrate-level emergence |
| `M_Pl_reduced` | EMERGENT_FROM | 2.435e+18 | Reduced Planck mass = 1/sqrt(8 pi G_N); inherits substrate-emergence from G_N |
| `M_Pl_unreduced` | EMERGENT_FROM | 1.221e+19 | Unreduced Planck mass = sqrt(hbar c / G_N); inherits substrate-emergence |
| `l_Planck` | EMERGENT_FROM | 1.616e-35 | Planck length sqrt(hbar G_N / c^3); inherits substrate-emergence |
| `rho_crit_GeV4` | EMERGENT_FROM | 4.08e-47 | Critical density 3 H_0^2 / (8 pi G); equation-of-motion of emergent EH action |
| `t_Planck` | EMERGENT_FROM | 5.391e-44 | Planck time sqrt(hbar G_N / c^5); inherits substrate-emergence |
| `G_N_cgs` | DERIVED | 6.674e-08 | G_N in CGS units (= G_N * 1000); pure unit conversion |
| `eps_baseline` | DERIVED | 0.01755 | Substrate slow-roll-equivalent = (1 - planck_ns)/2; algebraic from Planck n_s |
| `l_Planck_cm` | DERIVED | 1.616e-33 | Planck length in cm (= l_Planck * 100); pure unit conversion |
| `rho_crit_cgs` | DERIVED | 1.878e-29 | Critical density in CGS (= rho_crit_GeV4 in g/cm^3); pure unit conversion |
| `H_0_GeV` | RELATED | 1.438e-42 | H_0 in GeV; unit conversion of H_0_km_s_Mpc |
| `H_0_inv_s` | RELATED | 2.184e-18 | H_0 in s^-1; unit conversion |
| `H_0_km_s_Mpc` | RELATED | 67.4 | Hubble constant 67.4 km/s/Mpc (Planck 2018); Friedmann observational anchor |
| `Omega_DM` | RELATED | 0.2657 | Dark matter density 0.266; BC (S44 CDM-CONSTRUCT-44 gives DM by construction) |
| `Omega_Lambda` | RELATED | 0.685 | Dark-energy density 0.685; value lives in CC class (a_0), Friedmann observable h |
| `Omega_b` | RELATED | 0.0493 | Baryon density 0.0493 (Planck 2018); matter-sector BC |
| `Omega_m` | RELATED | 0.315 | Matter density 0.315 (Planck 2018); Friedmann boundary condition |
| `Omega_r` | RELATED | 9.15e-05 | Radiation density 9.15e-5; cosmological boundary condition |
| `T_CMB` | RELATED | 2.725 | CMB temperature 2.7255 K (COBE/FIRAS); BC for Friedmann-radiation era |
| `clock_coeff` | RELATED | -3.08 | Atomic-clock variation coefficient -3.08 (S22d); tests emergent equivalence-prin |
| `t_universe_s` | RELATED | 4.35e+17 | Age of universe 4.35e17 s (Planck 2018); Friedmann observable |
| `tau_fold` | RELATED | 0.19 | Jensen evaluation point of a_2; PRIMARY in fold class, RELATED here (per user-co |

## By role

### PRIMARY (7)

_defining constants — the class cannot be described without them_

- **`Lambda_Planck`** = 1 — Planck-scale regulator in M_KK units (= 1.0 default, S85 W6-3)
- **`M_KK`** = 7.429e+16 — KK scale fixes dimensional anchor of a_2 channel; KK class owns extraction, GR uses as input
  - _Also in: [KK](./kk.md) (PRIMARY)_
- **`R_protected_fold`** = 1.129 — L_max-invariant ratio a_0*a_4/a_2^2; ties GR (a_2) to CC (a_0) and YM (a_4) channels
  - _Also in: [CC](./cc.md) (PRIMARY)_
- **`a2_fold`** = 2776 — Second Seeley-DeWitt coefficient at fold; sole source of EH action 1/(16 pi G_N) = f_2 a_2 M_KK^2 (S44 SAKHAROV-GN-44)
- **`c_S_canon`** = 1 — Canonical spectral-action scale normalization (Chamseddine-Connes 1997)
- **`d_spec`** = 3 — Classical spectral dimension of D_K = 3 (Connes-Moscovici); gates which SDW term carries EH content
- **`f_2_default`** = 2.34 — f_2 spectral cutoff moment (S62 W1 Gaussian-cutoff = 2.34); regulator-pinned prefactor in EH dictionary

### EMERGENT_FROM (6)

_constants that emerge from PRIMARY members via substrate-level computation (regulators, schemes, multi-route consistency) — NOT algebraic one-liners_

- **`G_N`** = 6.674e-11 — Newton's constant from 1/(16 pi G_N) = f_2 a_2 M_KK^2; substrate-level emergence (S44 SAKHAROV-GN-44 PASS, 3-route check)
- **`M_Pl_reduced`** = 2.435e+18 — Reduced Planck mass = 1/sqrt(8 pi G_N); inherits substrate-emergence from G_N
- **`M_Pl_unreduced`** = 1.221e+19 — Unreduced Planck mass = sqrt(hbar c / G_N); inherits substrate-emergence
- **`l_Planck`** = 1.616e-35 — Planck length sqrt(hbar G_N / c^3); inherits substrate-emergence
- **`rho_crit_GeV4`** = 4.08e-47 — Critical density 3 H_0^2 / (8 pi G); equation-of-motion of emergent EH action
- **`t_Planck`** = 5.391e-44 — Planck time sqrt(hbar G_N / c^5); inherits substrate-emergence

### DERIVED (4)

_algebraic / definitional consequences — unit conversions, ratios of PRIMARY members_

- **`G_N_cgs`** = 6.674e-08 — G_N in CGS units (= G_N * 1000); pure unit conversion
- **`eps_baseline`** = 0.01755 — Substrate slow-roll-equivalent = (1 - planck_ns)/2; algebraic from Planck n_s
- **`l_Planck_cm`** = 1.616e-33 — Planck length in cm (= l_Planck * 100); pure unit conversion
- **`rho_crit_cgs`** = 1.878e-29 — Critical density in CGS (= rho_crit_GeV4 in g/cm^3); pure unit conversion

### RELATED (12)

_kindred observables from sister classes, or boundary conditions; not native to this class_

- **`H_0_GeV`** = 1.438e-42 — H_0 in GeV; unit conversion of H_0_km_s_Mpc
- **`H_0_inv_s`** = 2.184e-18 — H_0 in s^-1; unit conversion
- **`H_0_km_s_Mpc`** = 67.4 — Hubble constant 67.4 km/s/Mpc (Planck 2018); Friedmann observational anchor
- **`Omega_DM`** = 0.2657 — Dark matter density 0.266; BC (S44 CDM-CONSTRUCT-44 gives DM by construction)
- **`Omega_Lambda`** = 0.685 — Dark-energy density 0.685; value lives in CC class (a_0), Friedmann observable here
  - _Also in: [CC](./cc.md) (RELATED)_
- **`Omega_b`** = 0.0493 — Baryon density 0.0493 (Planck 2018); matter-sector BC
- **`Omega_m`** = 0.315 — Matter density 0.315 (Planck 2018); Friedmann boundary condition
- **`Omega_r`** = 9.15e-05 — Radiation density 9.15e-5; cosmological boundary condition
- **`T_CMB`** = 2.725 — CMB temperature 2.7255 K (COBE/FIRAS); BC for Friedmann-radiation era
- **`clock_coeff`** = -3.08 — Atomic-clock variation coefficient -3.08 (S22d); tests emergent equivalence-principle behavior
- **`t_universe_s`** = 4.35e+17 — Age of universe 4.35e17 s (Planck 2018); Friedmann observable
- **`tau_fold`** = 0.19 — Jensen evaluation point of a_2; PRIMARY in fold class, RELATED here (per user-confirmed taxonomy)
  - _Also in: [Exflation](./exflation.md) (RELATED), [fold](./fold.md) (PRIMARY)_

## Consumer gates

_(no consumer gates yet — topic pages do not currently carry Input-SHA pins. When gates start citing topic pages as authoritative data, list them here.)_

## Change log

| Date | Session | Change | Author |
|:-----|:--------|:-------|:-------|
| 2026-06-28 | S86-W*-build_topic_pages | auto-generated from canonical_classes.py | build_topic_pages.py |

---

**Visualizer**: open `tools/viz/console/index.html` and select `GR` from the `▣ classes` dropdown in the Connections tab to see the radial member graph (color-coded by role).
