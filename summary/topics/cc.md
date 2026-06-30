---
type: topic-page
ingested-by: /weave --update
class-id: CC
class-tier: 0
generated: 2026-06-28
---

# Topic — Cosmological constant family

> Auto-generated from `computations/_shared/canonical_classes.py` via `tools/build_topic_pages.py`. Edits to this file will be overwritten by the next `/weave --update`. To change the content, edit the class definition or its CLASS_EDGES entries in canonical_classes.py.

**Class ID**: `CC`  
**Tier**: 0 (root)  
**Parent class**: (root)  
**Seed session**: `S44`  
**Member count**: 7 (0 sub-classes)

## Scope

The cosmological-constant problem: the spectral-action zeroth moment a_0 evaluated against the observed dark-energy density rho_Lambda. The ratio is ~10^120 in the canonical sign convention. Class members include the ratio itself, the Planck-2018 anchor, the dimensionless Lambda/M_Pl^4 form, the spectral-density estimate, and the effacement-residual coefficient.

## Members (7)

| Constant | Role | Value | Comment |
|:---------|:-----|:------|:--------|
| `CC_ratio` | PRIMARY | 3.123e+120 | Headline ratio rho_Lambda_spectral / rho_Lambda_obs (~10^120) |
| `R_protected_fold` | PRIMARY | 1.129 | L_max-invariant ratio a_0*a_4/a_2^2; SOLE Chamseddine-Connes observable tying CC |
| `rho_Lambda_obs` | PRIMARY | 2.7e-47 | Observed CC density (Planck 2018, GeV^4) |
| `Lambda_obs_MP4` | DERIVED | 2.888e-122 | Dimensionless Lambda/M_Pl^4 form (= rho_Lambda_obs scaled) |
| `Gamma_effacement` | RELATED | 0.9997 | Acoustic-white-hole impedance; (1-Gamma) = effacement residual |
| `Omega_DE_obs` | RELATED | 0.685 | Planck 2020 DR2 update of Omega_Lambda |
| `Omega_Lambda` | RELATED | 0.685 | Dark-energy density parameter (Planck 2018) |

## By role

### PRIMARY (3)

_defining constants — the class cannot be described without them_

- **`CC_ratio`** = 3.123e+120 — Headline ratio rho_Lambda_spectral / rho_Lambda_obs (~10^120)
- **`R_protected_fold`** = 1.129 — L_max-invariant ratio a_0*a_4/a_2^2; SOLE Chamseddine-Connes observable tying CC (a_0) to GR (a_2) and YM (a_4); Vol(SU(3)) cancels (Baptista B2). S73B/S74.
  - _Also in: [GR](./gr.md) (PRIMARY)_
- **`rho_Lambda_obs`** = 2.7e-47 — Observed CC density (Planck 2018, GeV^4)

### DERIVED (1)

_algebraic / definitional consequences — unit conversions, ratios of PRIMARY members_

- **`Lambda_obs_MP4`** = 2.888e-122 — Dimensionless Lambda/M_Pl^4 form (= rho_Lambda_obs scaled)

### RELATED (3)

_kindred observables from sister classes, or boundary conditions; not native to this class_

- **`Gamma_effacement`** = 0.9997 — Acoustic-white-hole impedance; (1-Gamma) = effacement residual
  - _Also in: [Exflation](./exflation.md) (PRIMARY)_
- **`Omega_DE_obs`** = 0.685 — Planck 2020 DR2 update of Omega_Lambda
- **`Omega_Lambda`** = 0.685 — Dark-energy density parameter (Planck 2018)
  - _Also in: [GR](./gr.md) (RELATED)_

## Consumer gates

_(no consumer gates yet — topic pages do not currently carry Input-SHA pins. When gates start citing topic pages as authoritative data, list them here.)_

## Change log

| Date | Session | Change | Author |
|:-----|:--------|:-------|:-------|
| 2026-06-28 | S86-W*-build_topic_pages | auto-generated from canonical_classes.py | build_topic_pages.py |

---

**Visualizer**: open `tools/viz/console/index.html` and select `CC` from the `▣ classes` dropdown in the Connections tab to see the radial member graph (color-coded by role).
