"""penrose-glow reference render — Schwarzschild collapse cartoon.

Regenerates `.claude/skills/penrose-glow/example-schwarzschild.png`, the
canonical look-target for the /penrose-glow skill (PBS-Space-Time-style
dark-mode conformal diagram). Pure style demo: textbook Schwarzschild
geometry, no framework physics, no verdicts.

Run from the project root:
    "phonon-exflation-sim/.venv312/Scripts/python.exe" \
        ".claude/skills/penrose-glow/demo_schwarzschild.py"
"""

import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "computations" / "_shared"))

import _penrose_style as ps  # noqa: E402

OUT = Path(__file__).resolve().parent / "example-schwarzschild.png"

# --- geometry (unit wedge; all null segments exactly 45 deg) ----------------
I_MINUS = (0.0, -1.0)      # past timelike infinity
I_ZERO = (1.0, 0.0)        # spatial infinity
I_PLUS = (0.45, 0.55)      # future timelike infinity = right end of singularity
H_FOOT = (0.0, 0.10)       # horizon foot on the r=0 axis
SING_Y = 0.55              # singularity height (a moment, not a place)
AXIS_TOP = (0.0, SING_Y)   # r=0 axis meets the singularity

fig, ax = ps.penrose_figure(figsize=(9.0, 12.0), dpi=220)
ps.backdrop(ax, xlim=(-0.16, 1.18), ylim=(-1.16, 0.80), center=(0.42, -0.05))

# --- faint hyperbola grid, clipped to the EXTERIOR region -------------------
exterior = ps.make_clip(ax, [I_MINUS, I_ZERO, I_PLUS, H_FOOT])
ps.conformal_grid(ax, mode="wedge", clip=exterior)

# --- black-hole interior shading --------------------------------------------
ps.shade(ax, [H_FOOT, I_PLUS, AXIS_TOP], ps.PALETTE["horizon"], alpha=0.10)

# --- conformal boundary ------------------------------------------------------
ps.boundary_edge(ax, I_MINUS, I_ZERO)                    # scri-minus (null)
ps.boundary_edge(ax, I_ZERO, I_PLUS)                     # scri-plus (null)
ps.boundary_edge(ax, I_MINUS, AXIS_TOP, kind="timelike")  # r=0 axis

# --- black-hole furniture ----------------------------------------------------
ps.horizon(ax, H_FOOT, I_PLUS)                            # r=2M, validated null
ps.singularity_zigzag(ax, 0.0, I_PLUS[0], SING_Y,
                      label_text=r"singularity   $r=0$")

# --- singularity tooth-bottom snap points (clean line terminations) ----------
tooth = ps.zigzag_tooth_bottoms(0.0, I_PLUS[0], SING_Y)               # (local)
amber_end = tuple(tooth[np.argmin(np.abs(tooth[:, 0] - 0.216))])      # (local)
ray_end = tuple(tooth[np.argmin(np.abs(tooth[:, 0] - 0.291))])        # (local)
rx = 0.5 * (ray_end[0] + ray_end[1] + 1.0)                            # (local)
ray_start = (rx, rx - 1.0)   # on scri-minus (y = x - 1), null to ray_end

# --- massive worldlines (timelike-validated; all begin at i-minus) -----------
# Infaller control points rotate their direction MONOTONICALLY (+27deg ->
# -39deg off vertical) so curvature is distributed along the whole arc —
# no straight-climb-then-hook geometry for the smoother to preserve. The
# final point is snapped to a singularity DOWN-tooth tip.
infaller = [(0.0, -1.0), (0.14, -0.72), (0.25, -0.44), (0.32, -0.15),
            (0.35, 0.12), (0.34, 0.30), (0.30, 0.42), (0.26, 0.48),
            amber_end]
ps.worldline(ax, infaller, color=ps.PALETTE["worldline"])

observer = [(0.0, -1.0), (0.30, -0.62), (0.50, -0.28), (0.60, 0.00),
            (0.52, 0.30), (0.451, 0.547)]   # terminates flush at i-plus
ps.worldline(ax, observer, color=ps.PALETTE["worldline_alt"], lw=2.0)

# --- photons (45-degree-locked) ----------------------------------------------
ps.light_ray(ax, (0.32, -0.15), (0.735, 0.265))           # escapes to scri-plus
ps.light_ray(ax, ray_start, ray_end,
             color=ps.PALETTE["light_alt"])   # scri-minus -> a DOWN-tooth tip

# --- light-cone stamps (exterior one pinned to an infaller control point) ----
ps.light_cone(ax, (0.32, -0.15), size=0.045,
              label_text="light cone")                    # exterior event
ps.light_cone(ax, (0.24, 0.44), size=0.038)               # interior event

# --- labels -------------------------------------------------------------------
ps.infinity_label(ax, I_PLUS, ps.I_PLUS, dx=0.045, dy=0.045)
ps.infinity_label(ax, I_MINUS, ps.I_MINUS, dy=-0.065)
ps.infinity_label(ax, I_ZERO, ps.I_ZERO, dx=0.075)
ps.infinity_label(ax, (0.725, 0.275), ps.SCRI_PLUS, dx=0.075, dy=0.075)
ps.infinity_label(ax, (0.5, -0.5), ps.SCRI_MINUS, dx=0.08, dy=-0.08)
ps.label(ax, -0.04, -0.25, r"$r=0$", rotation=90, size=12,
         color=ps.PALETTE["subtext"])
ps.label(ax, 0.115, 0.44, "interior", size=10.5,
         color=ps.PALETTE["horizon"], alpha=0.85)

ps.title(fig, "Schwarzschild black hole",
         sub="conformal (Penrose) diagram — /penrose-glow reference render")

ps.save(fig, OUT)
print(f"[penrose-glow demo] wrote {OUT}")
print("[penrose-glow demo] null-ray 45-degree validation: PASS "
      "(horizon, scri edges, 2 photons)")
print("[penrose-glow demo] worldline timelike validation: PASS (2 worldlines)")
sys.exit(0)
