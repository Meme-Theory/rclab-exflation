---
type: topic-page
ingested-by: /weave --update
class-id: KK
class-tier: 0
generated: 2026-06-28
---

# Topic — Kaluza-Klein scale tower

> Auto-generated from `computations/_shared/canonical_classes.py` via `tools/build_topic_pages.py`. Edits to this file will be overwritten by the next `/weave --update`. To change the content, edit the class definition or its CLASS_EDGES entries in canonical_classes.py.

**Class ID**: `KK`  
**Tier**: 0 (root)  
**Parent class**: (root)  
**Seed session**: `S42`  
**Member count**: 4 (0 sub-classes)

## Scope

The internal-geometry mass scale M_KK extracted from the Dirac spectrum of the Jensen-deformed SU(3) fiber. Two routes — spectral zeta against Newton's constant (gravity route, ~7.4e16 GeV) and the Kerner gauge-metric route (~5.0e17 GeV) — bracket the value at 0.83 decades. CONST-FREEZE-42 (S42) pinned the convention; the gravity route is the canonical alias.

## Members (4)

| Constant | Role | Value | Comment |
|:---------|:-----|:------|:--------|
| `M_KK` | PRIMARY | 7.429e+16 | Canonical alias = M_KK_gravity (conservative route) |
| `M_KK_gravity` | PRIMARY | 7.429e+16 | Gravity route: spectral zeta / Newton's constant (S42) |
| `M_KK_kerner` | PRIMARY | 5.042e+17 | Kerner route: gauge-metric extraction (S42) |
| `OOM_diff_MKK` | DERIVED | 0.8317 | log10(M_KK_kerner / M_KK_gravity) = 0.83 decades |

## By role

### PRIMARY (3)

_defining constants — the class cannot be described without them_

- **`M_KK`** = 7.429e+16 — Canonical alias = M_KK_gravity (conservative route)
  - _Also in: [GR](./gr.md) (PRIMARY)_
- **`M_KK_gravity`** = 7.429e+16 — Gravity route: spectral zeta / Newton's constant (S42)
- **`M_KK_kerner`** = 5.042e+17 — Kerner route: gauge-metric extraction (S42)

### DERIVED (1)

_algebraic / definitional consequences — unit conversions, ratios of PRIMARY members_

- **`OOM_diff_MKK`** = 0.8317 — log10(M_KK_kerner / M_KK_gravity) = 0.83 decades

## Consumer gates

_(no consumer gates yet — topic pages do not currently carry Input-SHA pins. When gates start citing topic pages as authoritative data, list them here.)_

## Change log

| Date | Session | Change | Author |
|:-----|:--------|:-------|:-------|
| 2026-06-28 | S86-W*-build_topic_pages | auto-generated from canonical_classes.py | build_topic_pages.py |

---

**Visualizer**: open `tools/viz/console/index.html` and select `KK` from the `▣ classes` dropdown in the Connections tab to see the radial member graph (color-coded by role).
