---
type: topic-page
ingested-by: /weave --update
class-id: fold
class-tier: 0
generated: 2026-06-28
---

# Topic — Jensen-deformation transit complex

> Auto-generated from `computations/_shared/canonical_classes.py` via `tools/build_topic_pages.py`. Edits to this file will be overwritten by the next `/weave --update`. To change the content, edit the class definition or its CLASS_EDGES entries in canonical_classes.py.

**Class ID**: `fold`  
**Tier**: 0 (root)  
**Parent class**: (root)  
**Seed session**: `S38`  
**Member count**: 15 (0 sub-classes)

## Scope

Constants describing the fold transit at tau_fold = 0.19 — the framework's first-order phase transition that replaces the Big Bang singularity. Includes the spectral action S_fold and its first/second derivatives, transit timescale, terminal velocity, and Kibble-Zurek excitation parameters. The substrate sound speed c_fabric (NOT a propagation cutoff) sets the Mach number for the supersonic phase.

## Members (15)

| Constant | Role | Value | Comment |
|:---------|:-----|:------|:--------|
| `S_fold` | PRIMARY | 2.504e+05 | Spectral action at the fold (S42) |
| `d2S_fold` | PRIMARY | 3.179e+05 | d^2 S/dtau^2 at the fold (curvature of action) |
| `dS_fold` | PRIMARY | 5.867e+04 | dS/dtau at the fold = +58,672 (drives transit) |
| `tau_fold` | PRIMARY | 0.19 | Jensen deformation parameter at the fold (= 0.19) |
| `H_fold` | DERIVED | 586.5 | Hubble parameter at fold (M_KK units) |
| `P_exc_kz` | DERIVED | 1 | Kibble-Zurek excitation probability (= 1 exactly) |
| `Z_fold` | DERIVED | 7.473e+04 | Gradient stiffness at fold (= G_DeWitt-weighted) |
| `dt_transit` | DERIVED | 0.00113 | Transit duration (M_KK^-1 units) |
| `n_Bog` | DERIVED | 0.9986 | Bogoliubov fraction per mode |
| `n_pairs` | DERIVED | 59.8 | Bogoliubov quasiparticle pairs from transit (= 59.8) |
| `v_terminal` | DERIVED | 26.54 | Terminal velocity of modulus during transit |
| `c_fabric` | RELATED | 210 | Substrate sound speed (sets Mach number for transit) |
| `m_tau` | RELATED | 2.062 | Modulus mass at the fold (M_KK units) |
| `omega_tau` | RELATED | 8.27 | Transit frequency d(tau)/dt |
| `phi_paasch` | RELATED | 1.532 | Paasch spectral ratio at s=0.15 (PROVEN, related to fold geometry) |

## By role

### PRIMARY (4)

_defining constants — the class cannot be described without them_

- **`S_fold`** = 2.504e+05 — Spectral action at the fold (S42)
  - _Also in: [Exflation](./exflation.md) (PRIMARY)_
- **`d2S_fold`** = 3.179e+05 — d^2 S/dtau^2 at the fold (curvature of action)
  - _Also in: [Exflation](./exflation.md) (DERIVED)_
- **`dS_fold`** = 5.867e+04 — dS/dtau at the fold = +58,672 (drives transit)
  - _Also in: [Exflation](./exflation.md) (PRIMARY)_
- **`tau_fold`** = 0.19 — Jensen deformation parameter at the fold (= 0.19)
  - _Also in: [Exflation](./exflation.md) (RELATED), [GR](./gr.md) (RELATED)_

### DERIVED (7)

_algebraic / definitional consequences — unit conversions, ratios of PRIMARY members_

- **`H_fold`** = 586.5 — Hubble parameter at fold (M_KK units)
  - _Also in: [Exflation](./exflation.md) (PRIMARY)_
- **`P_exc_kz`** = 1 — Kibble-Zurek excitation probability (= 1 exactly)
  - _Also in: [Exflation](./exflation.md) (PRIMARY)_
- **`Z_fold`** = 7.473e+04 — Gradient stiffness at fold (= G_DeWitt-weighted)
  - _Also in: [Exflation](./exflation.md) (DERIVED)_
- **`dt_transit`** = 0.00113 — Transit duration (M_KK^-1 units)
  - _Also in: [Exflation](./exflation.md) (PRIMARY)_
- **`n_Bog`** = 0.9986 — Bogoliubov fraction per mode
  - _Also in: [Exflation](./exflation.md) (PRIMARY)_
- **`n_pairs`** = 59.8 — Bogoliubov quasiparticle pairs from transit (= 59.8)
  - _Also in: [Exflation](./exflation.md) (CONSEQUENCE)_
- **`v_terminal`** = 26.54 — Terminal velocity of modulus during transit
  - _Also in: [Exflation](./exflation.md) (PRIMARY)_

### RELATED (4)

_kindred observables from sister classes, or boundary conditions; not native to this class_

- **`c_fabric`** = 210 — Substrate sound speed (sets Mach number for transit)
  - _Also in: [Exflation](./exflation.md) (PRIMARY)_
- **`m_tau`** = 2.062 — Modulus mass at the fold (M_KK units)
  - _Also in: [Exflation](./exflation.md) (RELATED)_
- **`omega_tau`** = 8.27 — Transit frequency d(tau)/dt
  - _Also in: [Exflation](./exflation.md) (DERIVED)_
- **`phi_paasch`** = 1.532 — Paasch spectral ratio at s=0.15 (PROVEN, related to fold geometry)
  - _Also in: [Exflation](./exflation.md) (RELATED)_

## Consumer gates

_(no consumer gates yet — topic pages do not currently carry Input-SHA pins. When gates start citing topic pages as authoritative data, list them here.)_

## Change log

| Date | Session | Change | Author |
|:-----|:--------|:-------|:-------|
| 2026-06-28 | S86-W*-build_topic_pages | auto-generated from canonical_classes.py | build_topic_pages.py |

---

**Visualizer**: open `tools/viz/console/index.html` and select `fold` from the `▣ classes` dropdown in the Connections tab to see the radial member graph (color-coded by role).
