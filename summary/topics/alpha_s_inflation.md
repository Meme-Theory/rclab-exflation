---
type: topic-page
ingested-by: /weave --update
class-id: alpha_s_inflation
class-tier: 1
generated: 2026-06-28
---

# Topic — alpha_s — inflationary running of n_s

> Auto-generated from `computations/_shared/canonical_classes.py` via `tools/build_topic_pages.py`. Edits to this file will be overwritten by the next `/weave --update`. To change the content, edit the class definition or its CLASS_EDGES entries in canonical_classes.py.

**Class ID**: `alpha_s_inflation`  
**Tier**: 1 (sub-class)  
**Parent class**: [alpha_s](./alpha_s.md) (alpha_s — running-coupling hierarchy (parent))  
**Seed session**: `S50`  
**Member count**: 8 (0 sub-classes)

## Scope

Inflationary alpha_s = d(n_s)/d(ln k), the running of the scalar spectral index. Planck-2018 reports -0.0045 ± 0.0067; ACT DR4 + Planck combined (Aiola+ 2020) reports +0.0023 ± 0.0063 (post-2018 canonical pin per S86 W13 P12). The framework prediction is alpha_s_inflation = n_s^2 - 1 (S50 constant-mass identity). NOT the QCD coupling.

## Members (8)

| Constant | Role | Value | Comment |
|:---------|:-----|:------|:--------|
| `alpha_s_canon_2020` | PRIMARY | 0.0023 | ACT DR4 + Planck combined (Aiola+ 2020); post-2018 canonical pin |
| `alpha_s_inflation_framework` | PRIMARY | -0.06897 | Framework prediction: n_s^2 - 1 (S50 identity) |
| `planck_alpha_s` | PRIMARY | -0.0045 | Planck 2018 central value (legacy, superseded by alpha_s_canon_2020) |
| `alpha_s_canon_2020_err` | DERIVED | 0.0063 | Aiola+ 2020 1-sigma on alpha_s |
| `alpha_s_framework_central` | DERIVED | -0.06897 | Canonical handle alias for alpha_s_inflation_framework (S85 W1c-1) |
| `planck_alpha_s_err` | DERIVED | 0.0067 | Planck 2018 1-sigma on alpha_s |
| `alpha_s_cmb_central` | RELATED | -0.06897 | CMB-pivot identity using planck_ns=0.9649 (S50/S85 W13-2) |
| `planck_ns` | RELATED | 0.9649 | n_s anchor that the framework's alpha_s prediction depends on |

## By role

### PRIMARY (3)

_defining constants — the class cannot be described without them_

- **`alpha_s_canon_2020`** = 0.0023 — ACT DR4 + Planck combined (Aiola+ 2020); post-2018 canonical pin
- **`alpha_s_inflation_framework`** = -0.06897 — Framework prediction: n_s^2 - 1 (S50 identity)
- **`planck_alpha_s`** = -0.0045 — Planck 2018 central value (legacy, superseded by alpha_s_canon_2020)

### DERIVED (3)

_algebraic / definitional consequences — unit conversions, ratios of PRIMARY members_

- **`alpha_s_canon_2020_err`** = 0.0063 — Aiola+ 2020 1-sigma on alpha_s
- **`alpha_s_framework_central`** = -0.06897 — Canonical handle alias for alpha_s_inflation_framework (S85 W1c-1)
- **`planck_alpha_s_err`** = 0.0067 — Planck 2018 1-sigma on alpha_s

### RELATED (2)

_kindred observables from sister classes, or boundary conditions; not native to this class_

- **`alpha_s_cmb_central`** = -0.06897 — CMB-pivot identity using planck_ns=0.9649 (S50/S85 W13-2)
- **`planck_ns`** = 0.9649 — n_s anchor that the framework's alpha_s prediction depends on

## Consumer gates

_(no consumer gates yet — topic pages do not currently carry Input-SHA pins. When gates start citing topic pages as authoritative data, list them here.)_

## Change log

| Date | Session | Change | Author |
|:-----|:--------|:-------|:-------|
| 2026-06-28 | S86-W*-build_topic_pages | auto-generated from canonical_classes.py | build_topic_pages.py |

---

**Visualizer**: open `tools/viz/console/index.html` and select `alpha_s_inflation` from the `▣ classes` dropdown in the Connections tab to see the radial member graph (color-coded by role).
