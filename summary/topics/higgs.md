---
type: topic-page
ingested-by: /weave --update
class-id: Higgs
class-tier: 0
generated: 2026-06-28
---

# Topic — Higgs and EW cluster

> Auto-generated from `computations/_shared/canonical_classes.py` via `tools/build_topic_pages.py`. Edits to this file will be overwritten by the next `/weave --update`. To change the content, edit the class definition or its CLASS_EDGES entries in canonical_classes.py.

**Class ID**: `Higgs`  
**Tier**: 0 (root)  
**Parent class**: (root)  
**Seed session**: `S60`  
**Member count**: 4 (0 sub-classes)

## Scope

Constants of the Higgs sector: observed Higgs mass, EW VEV, and the third-generation Yukawa pole masses (top, bottom) that dominate Higgs-sector running. Framework prediction m_H = 131.8 GeV (KK threshold corrections to the |S|^2 mode of the fiber embedding). v_ew = 246 GeV is the EW symmetry-breaking scale.

## Members (4)

| Constant | Role | Value | Comment |
|:---------|:-----|:------|:--------|
| `m_H_obs` | PRIMARY | 125.1 | Observed Higgs mass (PDG 2024, 125.1 GeV) |
| `v_ew` | PRIMARY | 246 | Electroweak VEV (= 246 GeV) |
| `m_b_pole` | RELATED | 4.78 | Bottom pole mass (PDG 2024); secondary Yukawa contributor |
| `m_t_pole` | RELATED | 172.7 | Top pole mass (PDG 2024); dominates Higgs-sector running |

## By role

### PRIMARY (2)

_defining constants — the class cannot be described without them_

- **`m_H_obs`** = 125.1 — Observed Higgs mass (PDG 2024, 125.1 GeV)
- **`v_ew`** = 246 — Electroweak VEV (= 246 GeV)

### RELATED (2)

_kindred observables from sister classes, or boundary conditions; not native to this class_

- **`m_b_pole`** = 4.78 — Bottom pole mass (PDG 2024); secondary Yukawa contributor
- **`m_t_pole`** = 172.7 — Top pole mass (PDG 2024); dominates Higgs-sector running

## Consumer gates

_(no consumer gates yet — topic pages do not currently carry Input-SHA pins. When gates start citing topic pages as authoritative data, list them here.)_

## Change log

| Date | Session | Change | Author |
|:-----|:--------|:-------|:-------|
| 2026-06-28 | S86-W*-build_topic_pages | auto-generated from canonical_classes.py | build_topic_pages.py |

---

**Visualizer**: open `tools/viz/console/index.html` and select `Higgs` from the `▣ classes` dropdown in the Connections tab to see the radial member graph (color-coded by role).
