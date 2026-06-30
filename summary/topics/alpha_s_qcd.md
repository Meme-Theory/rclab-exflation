---
type: topic-page
ingested-by: /weave --update
class-id: alpha_s_QCD
class-tier: 1
generated: 2026-06-28
---

# Topic — alpha_s — QCD strong coupling

> Auto-generated from `computations/_shared/canonical_classes.py` via `tools/build_topic_pages.py`. Edits to this file will be overwritten by the next `/weave --update`. To change the content, edit the class definition or its CLASS_EDGES entries in canonical_classes.py.

**Class ID**: `alpha_s_QCD`  
**Tier**: 1 (sub-class)  
**Parent class**: [alpha_s](./alpha_s.md) (alpha_s — running-coupling hierarchy (parent))  
**Seed session**: `S85`  
**Member count**: 1 (0 sub-classes)

## Scope

QCD running gauge coupling alpha_s(mu) at energy scale mu. The PDG-anchored value at M_Z is alpha_s(M_Z) = 0.1180. This is the gauge-theory observable, NOT the inflationary running of n_s. Tower extends to scales m_tau, m_b, M_Z, and (framework-side) M_KK via two-loop running.

## Members (1)

| Constant | Role | Value | Comment |
|:---------|:-----|:------|:--------|
| `alpha_s_MZ_obs` | PRIMARY | 0.118 | PDG 2024 anchor: alpha_s(M_Z) = 0.1180 |

## By role

### PRIMARY (1)

_defining constants — the class cannot be described without them_

- **`alpha_s_MZ_obs`** = 0.118 — PDG 2024 anchor: alpha_s(M_Z) = 0.1180

## Consumer gates

_(no consumer gates yet — topic pages do not currently carry Input-SHA pins. When gates start citing topic pages as authoritative data, list them here.)_

## Change log

| Date | Session | Change | Author |
|:-----|:--------|:-------|:-------|
| 2026-06-28 | S86-W*-build_topic_pages | auto-generated from canonical_classes.py | build_topic_pages.py |

---

**Visualizer**: open `tools/viz/console/index.html` and select `alpha_s_QCD` from the `▣ classes` dropdown in the Connections tab to see the radial member graph (color-coded by role).
