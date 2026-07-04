---
name: penrose-glow
description: Restyle or author Penrose/conformal diagrams as PBS-Space-Time-grade dark-mode artifacts — glowing 45°-locked null rays, neon horizons, jagged singularities, hyperbola coordinate grids, haloed sans-serif labels. Use when the user wants a Penrose diagram upgraded/beautified ("make it look like PBS Space Time"), or wants a new conformal diagram rendered at presentation quality.
---

# /penrose-glow — high-production conformal diagrams

Turn a boring Penrose diagram into a presentation-grade artifact, or author a
new one at that grade directly. The look: deep midnight background, glowing
neon vector lines, exact 45° null geometry, clean sans-serif typography.

**Reference render**: `.claude/skills/penrose-glow/example-schwarzschild.png`
— match this look. Regenerate it any time with:

```bash
"phonon-exflation-sim/.venv312/Scripts/python.exe" ".claude/skills/penrose-glow/demo_schwarzschild.py"
```

`demo_schwarzschild.py` is also the canonical worked example of the API.

## The engine

All styling lives in **`computations/_shared/_penrose_style.py`** (style only —
no physics, no framework constants; framework numbers belong in the CALLING
script). Import pattern from any script:

```python
import sys; sys.path.insert(0, r"computations/_shared")   # abs path in practice
import _penrose_style as ps
fig, ax = ps.penrose_figure()
ps.backdrop(ax, xlim=(...), ylim=(...))
```

| Primitive | Renders | Enforces |
|:----------|:--------|:---------|
| `penrose_figure`, `backdrop` | midnight canvas + radial lift | — |
| `boundary_edge`, `minkowski_diamond`, `minkowski_wedge` | conformal frame + `i±`, `i⁰`, scri labels | null edges validated 45° |
| `light_ray` | glowing cyan/yellow photon + arrowhead | **refuses non-45° lines** (`assert_null`) |
| `light_cone` | tiny 45° V-stamps at events | — |
| `worldline` | glowing amber/white massive path (C2 cubic-spline through control points; chord-clamped ends; Chaikin fallback) | **refuses null/spacelike segments** (`assert_timelike` on the final sampled curve) |
| `conformal_grid` | faint dashed constant-r arcs + constant-t fans (`mode='wedge'|'diamond'`, `clip=`) | true compactified hyperbolae |
| `horizon` | bold neon-red 45° line, `r=2M` label | validated null |
| `singularity_zigzag` | jagged red horizontal singularity | — |
| `shade`, `make_clip` | translucent region fills; grid clipping | — |
| `censored_region` | hatched violet region (framework: dynamically-censored zones) | — |
| `event_point` | radiant event marker (framework: poised hinge instants) | — |
| `label`, `infinity_label`, `title`, `save` | haloed text, STIX script scri (`ps.SCRI_PLUS` etc.), tight save | — |

Palette/typography are locked in `ps.PALETTE` + `ps.apply_style()` — do not
ad-hoc recolor; pick from the palette roles (light/worldline/horizon/…).

## The aesthetic contract (owner's design spec, 2026-07-02)

1. **Boundaries**: diamond or radial wedge; label every corner — `i⁺` top,
   `i⁻` bottom, `i⁰` spatial; scri edges `ℐ⁺`/`ℐ⁻`; `r=0` on the left axis.
2. **45° rule is absolute**: every photon/null structure is exactly 45°. The
   engine hard-errors on violations — that is a feature, never work around it.
3. **Massive objects**: worldlines steeper than 45° everywhere, running i⁻ →
   (i⁺ | singularity); faint dashed hyperbola grid behind them.
4. **Black-hole furniture**: horizon = bold neon 45° line labeled `r=2M`;
   singularity = jagged horizontal zigzag (a moment, not a place); infalling
   worldlines bend into it.
5. **Palette/typography**: midnight (not black) background; neon cyan/yellow
   light; red/amber horizons+singularities; desaturated blue grid; clean
   sans-serif labels, small elegant math.

## Workflow A — restyle an existing diagram

1. **Find the producing script** (e.g. `computations/session-N/*.py`), not the
   PNG. Extract the geometry from code/data. NEVER eyeball-trace physics off a
   raster image; if only a raster exists, reconstruct from the documents that
   defined the diagram and say so.
2. **Port geometry into the primitives, preserving causal content EXACTLY** —
   restyle is a style-only transform. If a source "null" line fails
   `assert_null` or a worldline goes spacelike, that is a *finding about the
   source*: surface it to the user/orchestrator; do not silently bend physics
   to make the render pass.
3. Write the restyled script alongside the original as `<stem>_glow.py`,
   render `<stem>_glow.png` (≥220 dpi) in the same directory. Leave the
   original artifacts untouched.
4. Visually inspect the PNG (Read it) before declaring done — check label
   collisions, curves escaping the frame, glow legibility. If a smoothed curve
   still looks wrong (flat stretches, sudden hooks), the defect is in the
   CONTROL-POINT DATA, not the smoother — the spline faithfully preserves
   uneven turning. Fix by redistributing the control points so direction
   rotates gradually along the arc; pin event stamps to control points so
   they sit exactly on the curve.
5. `SendUserFile` the render.

## Workflow B — author from a spec

Same as A from step 2, geometry authored from the spec/receipts. Session work
goes in `computations/session-N/s{N}_*.py` (canonical-constants import rules
apply to the CALLING script: `from canonical_constants import *`, `# (local)`
tags on drawing-geometry literals). Ad-hoc/non-session renders go to the
scratchpad.

## Framework conventions (this project)

- Substrate-first annotations: the framework's diagrams depict the substrate's
  OWN causal structure; GR objects (gravastar, Schwarzschild) are laboratory-IN
  references — label comparisons "predicate correspondence only; no
  object-level map" where SP-E1 applies.
- `censored_region` for dynamically-censored singularities (censorship ≠
  regularity — keep the zigzag inside it, hatched, labeled).
- `event_point` for measure-zero instants (e.g. the τ=0 poised hinge).
- Anchor new diagrams to the letters in
  `sessions/framework/Phononic-Penrose-Diagrams.md` (A/B/C/G…) when they
  extend existing ones.

## Environment

- Python: `"phonon-exflation-sim/.venv312/Scripts/python.exe"` (quote — the
  project root contains a space). Engine forces the Agg backend; CPU is fine.
- Multi-panel: one figure per panel beats subplot cramming; a combined atlas
  sheet is optional extra.
