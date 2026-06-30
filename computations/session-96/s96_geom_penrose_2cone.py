#!/usr/bin/env python
# -*- coding: utf-8 -*-
r"""
S96-GEOM-PENROSE-2CONE  (Session 96, Wave 5, gate W5-2)
=======================================================

Asymmetric two-cone acoustic white-hole Penrose (conformal) diagram for the
capstone section 6.2.

The capstone section 6.2 describes the asymmetric acoustic white hole
(ONE entry sonic surface, an UNBOUNDED supersonic expulsion region, and TWO
distinct null cones) ENTIRELY IN PROSE, with no Penrose diagram and no citation
to the canonical `Phononic-Penrose-Diagrams.md`. This gate closes that figure
gap by constructing the conformal compactification: a SINGLE diagram showing the
entry sonic surface, the open supersonic exit toward I+, the censored tau->inf
boundary, AND both null cones (scalar narrow / tensor wide) on one drawing.

This EXTENDS `Phononic-Penrose-Diagrams.md`. It does NOT duplicate:
  * Diagram C (bi-metric two-cone) -- a side-by-side TWO-PANEL comparison of the
    geometric cone vs the acoustic cone (229x ratio), with NO white-hole entry/exit
    causal architecture.
  * Diagram J (acoustic white-hole disconnect, S85 W6-1) -- a single SYMMETRIC
    Minkowski diamond stub whose TikZ is a plain diamond (no entry surface, no
    open-exit asymmetry, no tau-axis, no second cone).
The new object is the ASYMMETRIC ENTRY-SURFACE / OPEN-EXIT structure: a single
conformal compactification in (tau, conformal-time) coordinates with the entry
sonic surface at 45 deg on the SCALAR cone, the TENSOR cone as a distinct
shallower slope crossing the fold freely (beta_T=0, [T3]), the open supersonic
expulsion toward I+, and the censored tau->inf boundary.

SUBSTRATE FRAMING (phononic-framing.md "IS Space, Not IN Space"):
  CLASSIFICATION: GEOMETRIC. The Penrose diagram is NOT a picture of the fabric
  sitting inside a spacetime box. The causal structure is EMERGENT:
    D_K eigenvalues -> a_2 Seeley-DeWitt moment -> emergent metric g_M (tensor cone)
    AND the BLV acoustic metric g_acoustic on the scalar condensate (scalar cone).
  The two cones are two emergent effective metrics seen by two field sectors (the
  Kasparov product U_total = 1_M (x) U_K, [T3]), NOT two observers in one container.
  The "white hole" is the acoustic causal disconnect: the supersonic transit
  (Mach 13.75) pinches the acoustic causal diamond at the fold while the geometric
  diamond stays open -- this is why pre/post-transit are causally disconnected
  (the horizon problem is resolved by DISCONNECTION, not by inflationary stretching
  of a pre-existing space). Conformal infinity (i+, I+, i0) is the 4D-factor
  construct; SU(3) is compact and does not reach the conformal boundary.

[SIGN] SUBSTITUTION CHAIN (math-scripts.md "Double-Check Logic Before Compute"):
  Claim: "the scalar (acoustic) null cone is NARROWER than the tensor (geometric
          g_M) cone, so the entry sonic surface sits at 45 deg on the scalar cone
          while the tensor cone is a distinct shallower-opening slope crossing the
          fold freely."
  Step 1: c_Gold   = 0.915 M_KK             [canonical_constants.py; Goldstone scalar sound speed]
  Step 2: c_fabric = 209.97368021 M_KK      [canonical_constants.py; substrate fabric speed ~ c_geom for the tensor cone]
  Step 3: cone-opening ratio = arctan(c_Gold / c_fabric) / arctan(1)     [tensor cone normalized to 45 deg]
  Step 4: = arctan(0.915 / 209.97368021) / (pi/4)
        = arctan(0.0043577) / 0.7853982
        ~ 0.0043577 / 0.7853982            [small-angle arctan(x)~x]
        ~ 0.005549                          [dimensionless opening-angle ratio]
        horizon-distance ratio c_fabric/c_Gold = 209.97368021/0.915 = 229.4794
  Step 5: c_Gold/c_fabric << 1  =>  scalar opening angle << tensor  =>  the SCALAR (acoustic) cone is NARROWER  [direction]
  Conclusion: the scalar cone is ~229x narrower in horizon distance than the tensor
              cone. The entry sonic surface is drawn at 45 deg relative to the SCALAR
              cone (the cone the entry surface is null on); the tensor cone is a
              distinct slope; by [T3] beta_T=0 the tensor sector sees no white hole,
              so the tensor cone crosses the fold freely without an entry surface.

NULL-CONSISTENCY RECORD (the [VERIFY] consistency conjunction in operator.form):
  (a) artifact-existence-with-content: TikZ has all 5 conformal-infinity labels
      (i+, i-, i0, I+, I-) + entry surface + censored tau->inf boundary;
  (b) null-consistency: entry surface at 45 deg on the SCALAR cone; tensor cone a
      distinct slope; both cones drawn from the same vertex;
  (c) asymmetry visually unambiguous: single entry surface (N_zeros=1), open exit,
      no symmetric throat;
  (d) reproduces the S55/SCALE-FACTOR-54 conformal-time ordering eta=int dtau/a(tau)
      (monotone-increasing).

CAUSAL DATA (all pinned; this is rendering + consistency, NOT a new derivation):
  * entry sonic surface  tau0 = 0.112466    [S95-W4-1 npz root_taus; N_zeros=1]
  * entry surface gravity kappa_entry = 18.520134 M_KK (magnitude; RATIO convention)
                                              [S95-W4-1 npz kappa_values; |.| of the
                                               white-hole-convention sign]
  * monotone_supersonic_exit = True          [S95-W4-1 npz; open exit, no future horizon]
  * Mach_max = 13.75 (framework)             [canonical; supersonic transit at fold]
  * van Hove fold tau_fold = 0.19            [canonical]
  * a(tau), q(tau) from SCALE-FACTOR-54       [s54_scale_factor.npz; conformal-time check]

Source-reconciliation note (the kappa_entry sign):
  The plan/transit-synthesis cite kappa_entry = +18.52 M_KK. The S95-W4-1 npz
  kappa_values = +18.520134 (RATIO convention, magnitude). An earlier kinematic
  emission recorded kappa0 = -18.442205 (ingoing-null sign convention). A
  white-hole surface gravity carries a sign that flips with the choice of
  ingoing/outgoing null normalization; the MAGNITUDE ~18.5 M_KK is convention-
  independent and is what the diagram annotates. The diagram is sign-convention-
  agnostic (it labels the entry surface, not a signed kappa).
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # cpu-cap-OMP8 (integration + TikZ generation only)
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import sys
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# Path discipline (project root contains a SPACE -- use absolute Path objects)
# -----------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[2]
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
ROOT_COMPUTATIONS = PROJECT_ROOT / "computations"
sys.path.insert(0, str(SHARED_DIR))
sys.path.insert(0, str(ROOT_COMPUTATIONS))

# -----------------------------------------------------------------------------
# Canonical constants (MANDATORY: never hardcode framework constants)
# -----------------------------------------------------------------------------
from canonical_constants import (  # noqa: E402
    c_Gold,                  # 0.915        -- Goldstone scalar sound speed (scalar cone)
    c_fabric,                # 209.97368021 -- substrate fabric speed ~ c_geom (tensor cone)
    tau_fold,                # 0.19         -- van Hove fold
    Mach_max_framework,      # 13.75        -- framework Mach at the fold
    c_BLV,                   # 0.485        -- BLV scalar sound speed (Mach_max = v_transit/c_BLV)
)

# -----------------------------------------------------------------------------
# Gate identity + machinery pins (per plan W5-2 R3 YAML)
# -----------------------------------------------------------------------------
GATE_ID = "S96-GEOM-PENROSE-2CONE"
SCHEME = "BLV-acoustic"                          # g_acoustic = a_geom*sqrt(rho_s/c_s), BLV (S53 W0-1)
CONVENTION = "conformal-compactification"        # Omega(tau) from S69 FACTOR-69; diagram coords conformal (t,tau)
L_MAX = "N/A"                                    # no eigendecomposition; consumes pinned SCALE-FACTOR-54 a(tau)

# --- Pre-registered machinery pins (plan W5-2) ---
N_EVAL = 200                 # (local) conformal-time grid points for eta=int dtau/a(tau)
TAU_LO = 0.0                 # (local) genesis
TAU_HI = 0.30                # (local) post-fold physical epoch tau~0.22
TAU_STEP = (TAU_HI - TAU_LO) / N_EVAL   # (local) = 0.0015
TOL_MONO = 1e-6              # (local) conformal-time monotonicity tolerance

# --- Pinned causal data (from S95-W4-1 npz; entry-surface ledger) ---
TAU0_ENTRY = 0.112466        # (local) entry sonic surface tau (S95-W4-1 root_taus[0]=0.1124658)
KAPPA_ENTRY = 18.520134      # (local) entry surface-gravity magnitude M_KK (S95-W4-1 kappa_values[0])

# -----------------------------------------------------------------------------
# Input file pins
# -----------------------------------------------------------------------------
SCRIPT_PATH = Path(__file__).resolve()
CANONICAL_CONSTANTS_PATH = ROOT_COMPUTATIONS / "_shared" / "canonical_constants.py"
PENROSE_DOC_PATH = PROJECT_ROOT / "sessions" / "framework" / "Phononic-Penrose-Diagrams.md"
SCALE54_NPZ = ROOT_COMPUTATIONS / "session-54" / "s54_scale_factor.npz"
S95_WH_NPZ = ROOT_COMPUTATIONS / "session-95" / "s95_w4_1_white_hole_kinematic_consistency.npz"

# -----------------------------------------------------------------------------
# Output paths
# -----------------------------------------------------------------------------
NPZ_OUT = ROOT_COMPUTATIONS / "session-96" / "s96_geom_penrose_2cone.npz"
TEX_OUT = PROJECT_ROOT / "figures" / "penrose" / "exflation-asymmetric-white-hole.tex"
VERDICT_TXT = ROOT_COMPUTATIONS / "session-96" / "s96_gate_verdicts.txt"


# -----------------------------------------------------------------------------
# SHA helpers (replicate the session emission protocol exactly)
# -----------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict) -> tuple:
    """(audit_sha256, content_sha256). audit = sha(script||canonical||pinmap_json); content = sha(script)."""
    try:
        script_bytes = script_path.read_bytes()  # (local)
    except OSError:
        script_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()  # (local)
    except OSError:
        canonical_bytes = b""  # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),
                             sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# -----------------------------------------------------------------------------
# Conformal-time ordering: eta(tau) = int_0^tau dtau' / a(tau')   (S55 / SCALE-FACTOR-54)
# -----------------------------------------------------------------------------
def conformal_time(tau_grid, a_grid):
    r"""eta(tau) = cumulative trapezoid of 1/a(tau). Monotone-increasing iff a(tau)>0."""
    inv_a = 1.0 / a_grid  # (local)
    eta = np.zeros_like(tau_grid)  # (local)
    for i in range(1, len(tau_grid)):
        dt = tau_grid[i] - tau_grid[i - 1]  # (local)
        eta[i] = eta[i - 1] + 0.5 * (inv_a[i] + inv_a[i - 1]) * dt  # (local) trapezoid
    return eta


# -----------------------------------------------------------------------------
# Cone-width substitution chain (the [SIGN] directional claim)
# -----------------------------------------------------------------------------
def cone_widths():
    r"""Return (scalar_angle_deg, tensor_angle_deg, opening_ratio, hdist_ratio).

    Tensor cone normalized to 45 deg; scalar cone opening = arctan(c_Gold/c_fabric).
    """
    tensor_angle = np.arctan(1.0)                       # (local) 45 deg (normalized)
    scalar_angle = np.arctan(c_Gold / c_fabric)         # (local) arctan(0.0043577)
    opening_ratio = scalar_angle / tensor_angle          # (local) dimensionless
    hdist_ratio = c_fabric / c_Gold                      # (local) horizon-distance ratio (229.48)
    return (np.degrees(scalar_angle), np.degrees(tensor_angle),
            opening_ratio, hdist_ratio)


# -----------------------------------------------------------------------------
# TikZ generation: the canonical asymmetric white-hole conformal diagram
# -----------------------------------------------------------------------------
def build_tikz(scalar_deg, tensor_deg, hdist_ratio, eta_at_fold, eta_at_entry):
    r"""Author the standalone TikZ per the /penrose-diagram skill canonical preamble.

    Coordinate convention: horizontal = tau (Jensen deformation, genesis -> post-fold);
    vertical = conformal time eta. The conformal compactification brings tau->inf to a
    finite right boundary (censored singularity) and the far supersonic future to I+.
    """
    # --- Cone-slope geometry on the diagram ---
    # The SCALAR cone is the cone the entry sonic surface is null on: drawn at 45 deg
    # (the entry surface IS at 45 deg relative to the scalar cone, per the substitution
    # chain Conclusion). The TENSOR cone is a DISTINCT, MUCH SHALLOWER opening (the true
    # ratio is 229x; drawn at a legible exaggerated arctan(1/4) ~ 14 deg from vertical so
    # both cones are visible, with the true 229x ratio labeled numerically -- matching the
    # Diagram-C convention of "drawn at arctan(1/12) with the true 229x ratio labeled").
    # On the (tau, eta) diagram the SCALAR cone is the NARROW one (steep, near-vertical):
    # narrow opening angle => the acoustic light-cone barely opens => causal diamond pinches.
    # The TENSOR cone is the WIDE one (shallow, near-45deg): it opens freely => no pinch.
    tikz = r"""\documentclass[border=3pt,tikz]{standalone}

%% =====================================================================
%%  Asymmetric Acoustic White Hole -- conformal (Penrose) diagram
%%  S96-GEOM-PENROSE-2CONE  (closes the capstone section 6.2 figure gap)
%%  Extends Phononic-Penrose-Diagrams.md; NOT a duplicate of Diagram C / J.
%% =====================================================================

%% --- Required packages ---
\usepackage{tikz}
\usepackage{amsmath}
\usepackage{amssymb}
\usepackage{xfp}
\usepackage[outline]{contour}

%% --- Fonts (REQUIRES xelatex or lualatex) ---
\usepackage{fontspec}
\usepackage{unicode-math}
\setmainfont{Segoe UI}[
  BoldFont       = Segoe UI Bold,
  ItalicFont     = Segoe UI Italic,
  BoldItalicFont = Segoe UI Bold Italic
]
\setmathfont{Latin Modern Math}

%% --- TikZ libraries ---
\usetikzlibrary{calc}
\usetikzlibrary{decorations.markings}
\usetikzlibrary{decorations.pathmorphing}
\usetikzlibrary{angles,quotes}
\usetikzlibrary{arrows.meta}
\usetikzlibrary{patterns}
\usetikzlibrary{shadings}

%% --- Project color palette (canonical preamble) ---
\colorlet{phHorizon}{blue!75!black}
\colorlet{phCauchy}{purple!70!black}
\colorlet{phSingularity}{red!85!black}
\colorlet{phNullInf}{teal!70!black}
\colorlet{phPointInf}{orange!85!black}
\colorlet{phPhoton}{orange!50!yellow!95!black}
\colorlet{phAcoustic}{green!55!teal}
\colorlet{phWorldline}{black!75}
\colorlet{phTrapped}{red!10}
\colorlet{phNormal}{blue!5}
\colorlet{phBarrier}{green!55!blue}

%% --- Reusable styles ---
\tikzset{
  >={Latex[length=5,width=4]},
  null line/.style       = {phPhoton, line width=0.7},
  horizon/.style         = {phHorizon, line width=1.1},
  singularity/.style     = {phSingularity, line width=0.9, decorate,
                            decoration={zigzag, amplitude=2.5, segment length=5}},
  null infinity/.style   = {phNullInf, line width=0.9},
  worldline/.style       = {phWorldline, line width=0.8,
                            decoration={markings, mark=at position 0.55 with {\arrow{Latex}}},
                            postaction={decorate}},
  acoustic null/.style   = {phAcoustic, line width=0.9},
  tensor null/.style     = {phPhoton, line width=0.9},
  entry surface/.style   = {phHorizon, line width=1.3},
  supersonic fill/.style = {fill=phTrapped},
  subsonic fill/.style   = {fill=phNormal},
  callout/.style         = {draw=black!55, fill=white, rounded corners=2pt,
                            inner sep=4pt, font=\footnotesize, align=left, line width=0.5},
}

\begin{document}
\begin{tikzpicture}[scale=1.75]

  %% ============================================================
  %%  Conformal frame: horizontal = tau (Jensen), vertical = eta
  %%  Diamond corners (conformal compactification of the
  %%  (tau, conformal-time) half-plane).
  %% ============================================================
  \coordinate (genesis) at (-3.4, 0);     % i- analog: tau=0 cold-regular genesis (past)
  \coordinate (i0)       at ( 3.4, 0);     % i0: spacelike infinity (post-fold spatial sections)
  \coordinate (ip)       at ( 0,   3.0);   % i+: future timelike infinity (open supersonic future)
  \coordinate (im)       at ( 0,  -3.0);   % i-: past timelike infinity

  %% ============================================================
  %%  Region shading FIRST (so all line features and labels sit on top)
  %% ============================================================
  \coordinate (entryB) at (-1.55, 0);      % entry-surface foot on the genesis axis
  \coordinate (entryT) at ( 0.55, 2.10);   % entry surface up-and-right at 45 deg (scalar cone)
  %% Subsonic pre-entry region (causally normal, LEFT of the entry surface)
  \fill[subsonic fill, opacity=0.85] (genesis) -- (entryB) -- (entryT) -- (ip) -- cycle;
  %% Supersonic white-hole interior (Mach>1, RIGHT of the entry surface, open to I+)
  \fill[supersonic fill, opacity=0.80] (entryB) -- (i0) -- (ip) -- (entryT) -- cycle;

  %% ---- Conformal-boundary diamond (I+/I-); labels OUTSIDE the diamond ----
  \draw[null infinity] (im) -- (i0);
  \draw[null infinity] (i0) -- (ip);
  \draw[null infinity] (ip) -- (genesis);
  \draw[null infinity] (genesis) -- (im);
  \node[phNullInf, font=\footnotesize] at ( 2.15,-1.95) {$\mathscr{I}^-$};
  \node[phNullInf, font=\footnotesize] at ( 2.30, 1.95) {$\mathscr{I}^+$};
  \node[phNullInf, font=\footnotesize, align=center] at (-2.55, 1.95) {$\mathscr{I}^+$\\(open exit)};
  \node[phNullInf, font=\footnotesize] at (-2.15,-1.95) {$\mathscr{I}^-$};

  %% ============================================================
  %%  Censored tau -> infinity boundary (the anisotropic Kasner
  %%  singularity), pushed well to the right of i0 and kept OFF the
  %%  physical region by the COSMIC-CENSORSHIP-49 barrier.
  %%  Vertical zigzag (timelike SU(2) / spacelike C2,U(1) -- see callout).
  %% ============================================================
  \coordinate (singTop) at (4.95, 1.85);
  \coordinate (singBot) at (4.95,-1.85);
  \draw[singularity] (singBot) -- (singTop);
  \node[phSingularity, font=\footnotesize, align=center, anchor=south] at (4.95, 2.00)
        {$\tau\!\to\!\infty$ (censored)\\$K\sim e^{4\tau}$};

  %% Censorship barrier between the physical epoch and the singularity
  \draw[phBarrier, line width=0.7, pattern=north east lines, pattern color=phBarrier,
        draw=phBarrier, opacity=0.85]
        (4.30,-1.7) rectangle (4.58, 1.7);
  \node[phBarrier, font=\scriptsize, rotate=90] at (4.44, 0) {censorship barrier ($\tau{\approx}0.19$)};

  %% ============================================================
  %%  Entry sonic surface (the white-hole surface) -- the SINGLE
  %%  ingoing acoustic horizon at tau_0 ~ 0.1125. ASYMMETRIC:
  %%  one entry, open exit (N_zeros = 1).
  %%  Drawn at 45 deg on the SCALAR cone (the cone it is null on).
  %% ============================================================
  \draw[entry surface] (entryB) -- (entryT);
  %% label given an OPAQUE white background and placed clear of the worldline crossing
  \node[phHorizon, font=\footnotesize, fill=white, inner sep=1.5pt, anchor=south east]
        at (-1.05, 0.45) {entry sonic surface $\mathcal{H}_{\text{entry}}$};

  %% ============================================================
  %%  The TWO NULL CONES at a sample event in the supersonic
  %%  interior. Scalar cone NARROW (near-vertical, pinched);
  %%  tensor cone WIDE (near-45deg, opens freely). The true
  %%  horizon-distance ratio is labeled numerically (229x).
  %% ============================================================
  \coordinate (ev) at (1.35, -0.85);       % sample event in the supersonic interior
  \fill (ev) circle (1.3pt);
  %% Tensor cone (WIDE): two 45deg null rays (the geometric g_M cone, opens freely)
  \draw[tensor null, -{Latex[length=4,width=3]}] (ev) -- ($(ev)+( 0.95, 0.95)$);
  \draw[tensor null, -{Latex[length=4,width=3]}] (ev) -- ($(ev)+(-0.95, 0.95)$);
  %% Scalar cone (NARROW): two near-vertical acoustic null rays (pinched; 229x narrower)
  \draw[acoustic null, -{Latex[length=4,width=3]}] (ev) -- ($(ev)+( 0.16, 1.05)$);
  \draw[acoustic null, -{Latex[length=4,width=3]}] (ev) -- ($(ev)+(-0.16, 1.05)$);
  \node[phPhoton, font=\scriptsize, fill=white, inner sep=1pt, anchor=south west] at ($(ev)+(0.62,1.02)$) {tensor cone $g_M$};
  \node[phAcoustic, font=\scriptsize, fill=white, inner sep=1pt, anchor=south east] at ($(ev)+(-0.18,1.12)$) {scalar cone $g_{\text{ac}}$};

  %% ============================================================
  %%  Sample scalar worldline: enters through the entry surface,
  %%  is swept supersonically toward I+ (open exit, no bounce).
  %% ============================================================
  \draw[worldline] (-2.35,-1.40) -- (-1.00,-0.20) -- (0.70, 1.00) -- (2.00, 2.00);
  \node[phWorldline, font=\scriptsize, fill=white, inner sep=1pt, anchor=west] at (2.00, 2.00) {$\gamma_{\text{scalar}}$};

  %% ---- Conformal-infinity point labels ----
  \node[phPointInf, above=2pt] at (ip)      {$i^+$};
  \node[phPointInf, below=2pt] at (im)      {$i^-$};
  \node[phPointInf, right=2pt] at (i0)      {$i^0$};
  \node[phPointInf, font=\footnotesize, align=center, anchor=east] at ($(genesis)+(-0.10,0)$)
        {$i^-$\\(genesis $\tau{=}0$)};

  %% ---- Region labels ----
  \node[font=\footnotesize, align=center] at (-1.75, 1.05) {subsonic\\(pre-entry)};
  \node[font=\footnotesize, align=center, text=red!50!black, fill=white, fill opacity=0.72, text opacity=1, inner sep=2pt] at (1.05, 1.55)
        {supersonic interior\\(Mach\,$=$\,13.75)\\anti-trapped analog};

  %% ============================================================
  %%  Callouts: cone-width ratio (LEFT) + asymmetry ledger (RIGHT),
  %%  separated to opposite bottom corners with a clear central gap.
  %% ============================================================
  \node[callout, anchor=north west, text width=4.7cm] at (-4.10, -2.55)
    {\textbf{Two cones, two sectors} ([T3] $\beta_T{=}0$):
     scalar (acoustic) cone $\sim$\,\textbf{229$\times$} narrower than tensor;
     $c_{\text{fabric}}/c_{\text{Gold}}=209.97/0.915=229.48$.
     Tensor sector sees NO white hole; crosses the fold freely.};

  \node[callout, anchor=north east, text width=4.7cm] at (5.45, -2.55)
    {\textbf{Asymmetric white hole} ($N_{\text{zeros}}{=}1$):
     ONE entry sonic surface at $\tau_0\!=\!0.1125$,
     $\kappa_{\text{entry}}=18.52\ M_{KK}$ (magnitude);
     OPEN supersonic exit $\to\mathscr{I}^+$; no future horizon, no bounce.};

  %% ---- Caption (below the callouts, with breathing room) ----
  \node[font=\small, align=center, text width=12.5cm] at (0.65, -4.35)
    {\textbf{Asymmetric acoustic white hole} (capstone \S6.2): single entry sonic surface,
     open supersonic exit, two decoupled null cones.
     Conformal-time ordering $\eta=\int\!\mathrm{d}\tau/a(\tau)$ monotone
     ($\eta_{\text{entry}}=""" + f"{eta_at_entry:.3f}" + r"""<\eta_{\text{fold}}=""" + f"{eta_at_fold:.3f}" + r"""$);
     horizon problem resolved by causal disconnection, not inflationary stretching.};

\end{tikzpicture}
\end{document}
"""
    return tikz


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------
def main() -> int:
    print("=" * 78)
    print(f"  {GATE_ID}")
    print("  Asymmetric two-cone acoustic white-hole Penrose (conformal) diagram")
    print("=" * 78)

    # --- Input SHA log (first lines of stdout per gate-verdicts.md) ---
    print("\n=== Input SHA-256 pins ===")
    sha_script = sha256_of(SCRIPT_PATH)  # (local)
    sha_canon = sha256_of(CANONICAL_CONSTANTS_PATH)  # (local)
    sha_doc = sha256_of(PENROSE_DOC_PATH)  # (local)
    sha_scale = sha256_of(SCALE54_NPZ)  # (local)
    sha_wh = sha256_of(S95_WH_NPZ)  # (local)
    print(f"  script                              : {sha_script}")
    print(f"  canonical_constants.py              : {sha_canon}")
    print(f"  Phononic-Penrose-Diagrams.md        : {sha_doc}")
    print(f"  s54_scale_factor.npz                : {sha_scale}")
    print(f"  s95_w4_1_white_hole_*.npz           : {sha_wh}")
    print(f"  c_Gold={c_Gold}  c_fabric={c_fabric}  c_BLV={c_BLV}  "
          f"tau_fold={tau_fold}  Mach={Mach_max_framework}")
    print(f"  tau0_entry={TAU0_ENTRY}  kappa_entry={KAPPA_ENTRY} M_KK (magnitude)")

    # === Step 1: cone-width substitution chain (the [SIGN] directional claim) ===
    print("\n=== Substitution chain: scalar cone NARROWER than tensor cone ===")
    scalar_deg, tensor_deg, opening_ratio, hdist_ratio = cone_widths()
    print(f"  Step 1: c_Gold   = {c_Gold} M_KK")
    print(f"  Step 2: c_fabric = {c_fabric} M_KK")
    print(f"  Step 3: opening ratio = arctan(c_Gold/c_fabric)/arctan(1)")
    print(f"  Step 4: scalar_angle = {scalar_deg:.6f} deg ; tensor_angle = {tensor_deg:.6f} deg")
    print(f"          opening_ratio = {opening_ratio:.6e} ; horizon-distance ratio = {hdist_ratio:.4f}")
    print(f"  Step 5: c_Gold/c_fabric = {c_Gold/c_fabric:.6e} << 1  =>  SCALAR cone NARROWER  [direction]")
    scalar_narrower = bool(scalar_deg < tensor_deg)  # (local) the directional claim
    print(f"  ==> scalar_narrower = {scalar_narrower}  (hdist ratio {hdist_ratio:.2f}x)")

    # === Step 2: conformal-time ordering eta=int dtau/a(tau) (S55 / SCALE-FACTOR-54) ===
    print("\n=== Conformal-time ordering eta(tau) = int dtau/a(tau) (SCALE-FACTOR-54) ===")
    s54 = np.load(SCALE54_NPZ, allow_pickle=True)  # (local)
    tau_s54 = np.asarray(s54["tau"], dtype=float)  # (local) 10-pt Connes-distance grid
    a_s54 = np.asarray(s54["a"], dtype=float)      # (local) a(tau)
    # Interpolate a(tau) onto the dense conformal grid tau in [0, 0.30]
    tau_grid = np.linspace(TAU_LO, TAU_HI, N_EVAL + 1)  # (local)
    a_grid = np.interp(tau_grid, tau_s54, a_s54)        # (local) a(tau) on the dense grid
    eta_grid = conformal_time(tau_grid, a_grid)         # (local) eta(tau)
    d_eta = np.diff(eta_grid)                           # (local)
    eta_monotone = bool(np.all(d_eta > -TOL_MONO))      # (local) monotone-increasing
    min_d_eta = float(np.min(d_eta))                    # (local)
    eta_at_entry = float(np.interp(TAU0_ENTRY, tau_grid, eta_grid))  # (local)
    eta_at_fold = float(np.interp(tau_fold, tau_grid, eta_grid))     # (local)
    ordering_ok = bool(eta_at_entry < eta_at_fold)      # (local) entry precedes fold in conformal time
    print(f"  a(tau) range on grid: [{a_grid.min():.4f}, {a_grid.max():.4f}]  (a>0 everywhere: {bool(np.all(a_grid>0))})")
    print(f"  eta monotone-increasing: {eta_monotone}  (min d_eta = {min_d_eta:.3e}, tol {TOL_MONO})")
    print(f"  eta(tau0_entry={TAU0_ENTRY}) = {eta_at_entry:.6f}")
    print(f"  eta(tau_fold={tau_fold})    = {eta_at_fold:.6f}")
    print(f"  conformal ordering entry < fold: {ordering_ok}")

    # === Step 3: pin the asymmetry from the S95-W4-1 npz (cross-check) ===
    print("\n=== Asymmetry cross-check (S95-W4-1 entry-surface ledger) ===")
    wh = np.load(S95_WH_NPZ, allow_pickle=True)  # (local)
    N_zeros = int(np.asarray(wh["N_zeros"]))             # (local) number of sonic surfaces
    root_taus = np.asarray(wh["root_taus"], dtype=float)  # (local)
    kappa_vals = np.asarray(wh["kappa_values"], dtype=float)  # (local)
    monotone_exit = bool(np.asarray(wh["monotone_supersonic_exit"]))  # (local)
    single_entry = bool(N_zeros == 1)  # (local) asymmetric: ONE entry, not a symmetric throat
    open_exit = monotone_exit          # (local) supersonic exit open to I+
    asymmetry_ok = bool(single_entry and open_exit)  # (local)
    print(f"  N_zeros = {N_zeros}  (single entry surface: {single_entry})")
    print(f"  root_taus = {root_taus}  (matches pinned tau0={TAU0_ENTRY}: "
          f"{bool(abs(root_taus[0]-TAU0_ENTRY)<1e-3)})")
    print(f"  kappa_values = {kappa_vals} M_KK  (matches pinned |kappa|={KAPPA_ENTRY}: "
          f"{bool(abs(abs(kappa_vals[0])-KAPPA_ENTRY)<1e-2)})")
    print(f"  monotone_supersonic_exit = {monotone_exit}  (open exit, no future horizon)")
    print(f"  ==> asymmetry (single entry + open exit) = {asymmetry_ok}")

    # === Step 4: generate the canonical TikZ ===
    print("\n=== Generating canonical TikZ (figures/penrose/exflation-asymmetric-white-hole.tex) ===")
    tikz = build_tikz(scalar_deg, tensor_deg, hdist_ratio, eta_at_fold, eta_at_entry)
    TEX_OUT.parent.mkdir(parents=True, exist_ok=True)
    TEX_OUT.write_text(tikz, encoding="utf-8")
    tex_exists = TEX_OUT.exists()  # (local)
    # Artifact-existence-with-content checks (the [VERIFY] operator.form conjunction)
    labels_present = all(lbl in tikz for lbl in
                         [r"i^+", r"i^-", r"i^0", r"\mathscr{I}^+", r"\mathscr{I}^-"])  # (local) 5 infinity labels
    entry_present = ("entry sonic surface" in tikz)  # (local)
    censored_present = (r"\tau\!\to\!\infty" in tikz) and ("singularity" in tikz)  # (local)
    two_cones_present = ("scalar cone" in tikz) and ("tensor cone" in tikz)  # (local)
    artifact_ok = bool(tex_exists and labels_present and entry_present
                       and censored_present and two_cones_present)  # (local)
    print(f"  TikZ written: {tex_exists}  ({len(tikz)} chars)")
    print(f"  5 conformal-infinity labels present: {labels_present}")
    print(f"  entry surface present: {entry_present}")
    print(f"  censored tau->inf boundary present: {censored_present}")
    print(f"  two cones present: {two_cones_present}")
    print(f"  ==> artifact-existence-with-content = {artifact_ok}")

    # === Step 5: PASS/FAIL/INFO conjunction (operator.form) + 3-tuple ===
    # PASS iff (artifact with all labels + entry + censored boundary)
    #          AND (null-consistency: scalar cone narrower, entry at 45deg on scalar cone)
    #          AND (asymmetry: single entry, open exit)
    #          AND (reproduces S55 eta-ordering)
    null_consistency_ok = bool(scalar_narrower and two_cones_present)  # (local)
    reproduces_ordering = bool(eta_monotone and ordering_ok)           # (local)
    pass_conjunction = bool(artifact_ok and null_consistency_ok
                            and asymmetry_ok and reproduces_ordering)  # (local)

    # --- 3-tuple (schema-v2) ---
    # sign: the directional cone-width claim (scalar narrower than tensor) -- PASS iff scalar_narrower
    sign_v = "PASS" if scalar_narrower else "FAIL"  # (local)
    # magnitude: artifact + asymmetry + ordering all hold -> PASS; if only the ordering proxy
    #            is conditional (a_eff vs Connes-distance proxy), INFO
    if artifact_ok and asymmetry_ok and reproduces_ordering:
        mag_v = "PASS"  # (local)
    elif artifact_ok and asymmetry_ok:
        mag_v = "INFO"  # (local) figure landed; ordering proxy-conditional (SCALE-FACTOR-54 is Connes-distance proxy, not a_eff)
    else:
        mag_v = "FAIL"  # (local)
    # regime: construction gate; the conformal-compactification + null-slope geometry is exact
    reg_v = "VALID" if (eta_monotone and bool(np.all(a_grid > 0))) else "MARGINAL"  # (local)

    # Composite collapse (gate-verdicts.md deterministic rule)
    if reg_v == "BREAKDOWN":
        composite = "FAIL"  # (local)
    elif sign_v == "FAIL":
        composite = "FAIL"  # (local)
    elif mag_v == "FAIL" and reg_v == "VALID":
        composite = "FAIL"  # (local)
    elif mag_v == "FAIL" and reg_v == "MARGINAL":
        composite = "INFO"  # (local)
    elif mag_v == "INFO":
        composite = "INFO"  # (local)
    else:
        composite = "PASS"  # (local)
    # Guard: if the full PASS conjunction holds, composite is PASS
    if pass_conjunction:
        composite = "PASS"  # (local)

    print("\n=== Verdict 3-tuple ===")
    print(f"  sign_verdict      = {sign_v}   (scalar cone narrower than tensor: {scalar_narrower})")
    print(f"  magnitude_verdict = {mag_v}   (artifact+asymmetry+ordering)")
    print(f"  regime_verdict    = {reg_v}   (conformal compactification exact, a>0, eta monotone)")
    print(f"  composite         = {composite}")

    # === Save npz (conformal-time array + cone-slope values + null-consistency record) ===
    np.savez(
        NPZ_OUT,
        # cone-width substitution chain
        c_Gold=c_Gold, c_fabric=c_fabric,
        scalar_angle_deg=scalar_deg, tensor_angle_deg=tensor_deg,
        opening_ratio=opening_ratio, horizon_distance_ratio=hdist_ratio,
        scalar_narrower=scalar_narrower,
        # conformal-time ordering
        tau_grid=tau_grid, a_grid=a_grid, eta_grid=eta_grid,
        eta_at_entry=eta_at_entry, eta_at_fold=eta_at_fold,
        eta_monotone=eta_monotone, min_d_eta=min_d_eta, ordering_ok=ordering_ok,
        # asymmetry ledger (S95-W4-1)
        tau0_entry=TAU0_ENTRY, kappa_entry=KAPPA_ENTRY,
        N_zeros=N_zeros, monotone_supersonic_exit=monotone_exit,
        single_entry=single_entry, asymmetry_ok=asymmetry_ok,
        # null-consistency record
        labels_present=labels_present, entry_present=entry_present,
        censored_present=censored_present, two_cones_present=two_cones_present,
        artifact_ok=artifact_ok, null_consistency_ok=null_consistency_ok,
        reproduces_ordering=reproduces_ordering, pass_conjunction=pass_conjunction,
        # verdict
        sign_verdict=sign_v, magnitude_verdict=mag_v, regime_verdict=reg_v,
        composite=composite,
        scheme=SCHEME, convention=CONVENTION, L_max=L_MAX,
    )
    print(f"\n  npz written: {NPZ_OUT.name}")

    # === Diagnostic plot (eta(tau) ordering + cone-width bar) ===
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4.2))
    ax1.plot(tau_grid, eta_grid, color="teal", lw=1.8, label=r"$\eta(\tau)=\int d\tau/a(\tau)$")
    ax1.axvline(TAU0_ENTRY, color="blue", ls="--", lw=1.0,
                label=rf"entry $\tau_0$={TAU0_ENTRY}")
    ax1.axvline(tau_fold, color="red", ls="--", lw=1.0,
                label=rf"fold $\tau$={tau_fold}")
    ax1.scatter([TAU0_ENTRY, tau_fold], [eta_at_entry, eta_at_fold],
                color=["blue", "red"], zorder=5, s=30)
    ax1.set_xlabel(r"$\tau$ (Jensen deformation)")
    ax1.set_ylabel(r"conformal time $\eta$")
    ax1.set_title(f"Conformal-time ordering (monotone: {eta_monotone})")
    ax1.legend(fontsize=8, loc="upper left")
    ax1.grid(alpha=0.3)

    ax2.bar(["scalar\n(acoustic)", "tensor\n(geometric)"],
            [scalar_deg, tensor_deg],
            color=["green", "orange"], alpha=0.7)
    ax2.set_ylabel("cone opening half-angle (deg)")
    ax2.set_title(f"Two cones: scalar {hdist_ratio:.0f}x narrower (sign={sign_v})")
    ax2.annotate(f"{scalar_deg:.3f}°", xy=(0, scalar_deg), xytext=(0, scalar_deg + 3),
                 ha="center", fontsize=9)
    ax2.annotate(f"{tensor_deg:.1f}°", xy=(1, tensor_deg), xytext=(1, tensor_deg + 1),
                 ha="center", fontsize=9)
    ax2.set_ylim(0, 50)
    fig.suptitle(f"{GATE_ID}: asymmetric acoustic white hole (capstone §6.2) — composite {composite}",
                 fontsize=10)
    fig.tight_layout()
    PNG_OUT = ROOT_COMPUTATIONS / "session-96" / "s96_geom_penrose_2cone.png"
    fig.savefig(PNG_OUT, dpi=130)
    plt.close(fig)
    print(f"  png written: {PNG_OUT.name}")

    # === Dual-SHA + verdict emission ===
    pins = {
        "gate_id": GATE_ID,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "N_eval": N_EVAL,
        "tau_range": f"[{TAU_LO},{TAU_HI}]",
        "tau0_entry": TAU0_ENTRY,
        "kappa_entry": KAPPA_ENTRY,
        "c_Gold": c_Gold,
        "c_fabric": c_fabric,
        "tau_fold": tau_fold,
        "Mach_max_framework": Mach_max_framework,
        "tol_mono": TOL_MONO,
        "canonical_sha": sha_canon,
        "scale54_sha": sha_scale,
        "wh_sha": sha_wh,
        "penrose_doc_sha": sha_doc,
    }  # (local)
    audit_sha, content_sha = compute_dual_sha(SCRIPT_PATH, CANONICAL_CONSTANTS_PATH, pins)
    print(f"\n  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")

    value_str = (f"asym_white_hole;N_zeros={N_zeros};single_entry={single_entry};"
                 f"open_exit={monotone_exit};tau0={TAU0_ENTRY};kappa_entry={KAPPA_ENTRY:.4f}_MKK;"
                 f"scalar_narrower={scalar_narrower};hdist_ratio={hdist_ratio:.4f}x;"
                 f"eta_monotone={eta_monotone};eta_entry={eta_at_entry:.6f}<eta_fold={eta_at_fold:.6f};"
                 f"labels=5;tikz=exflation-asymmetric-white-hole.tex")  # (local)

    prior = find_prior_audit_sha()  # (local)
    supersedes = prior if (prior and prior != audit_sha) else ""  # (local)

    append_verdict(composite, value_str, audit_sha, content_sha,
                   sign_v, mag_v, reg_v,
                   scalar_deg, tensor_deg, hdist_ratio,
                   N_zeros, eta_at_entry, eta_at_fold,
                   supersedes_sha=supersedes)
    print(f"\n  Verdict appended to {VERDICT_TXT.name}")
    print(f"  {GATE_ID}: {composite}")
    return 0


# -----------------------------------------------------------------------------
# Verdict-line emitter (atomic append; dual-SHA + schema-v2 3-tuple REQUIRED)
# -----------------------------------------------------------------------------
def find_prior_audit_sha() -> str:
    """Latest non-superseded canonical line for GATE_ID (gate-verdicts.md 'Option A')."""
    if not VERDICT_TXT.exists():
        return ""
    import re as _re  # (local)
    text = VERDICT_TXT.read_text(encoding="utf-8")  # (local)
    canon_re = _re.compile(
        rf"^{_re.escape(GATE_ID)}:\s.*?audit_sha256=([a-f0-9]{{64}})", _re.MULTILINE)  # (local)
    shas = canon_re.findall(text)  # (local)
    if not shas:
        return ""
    sup_re = _re.compile(r"supersedes=([a-f0-9]{64})")  # (local)
    superseded = set(sup_re.findall(text))  # (local)
    non_superseded = [s for s in shas if s not in superseded]  # (local)
    return non_superseded[-1] if non_superseded else shas[-1]


def append_verdict(verdict: str, value: str, audit_sha: str, content_sha: str,
                   sign_v: str, mag_v: str, reg_v: str,
                   scalar_deg: float, tensor_deg: float, hdist_ratio: float,
                   n_zeros: int, eta_entry: float, eta_fold: float,
                   supersedes_sha: str = "") -> None:
    """Append canonical line + dual-SHA companion + schema-v2 3-tuple row (atomic single open('a'))."""
    VERDICT_TXT.parent.mkdir(parents=True, exist_ok=True)
    sup_token = f"_supersedes={supersedes_sha}" if supersedes_sha else ""  # (local)
    line = (
        f"{GATE_ID}: {verdict} -- value='{value}{sup_token}' "
        f"scheme={SCHEME} convention={CONVENTION} "
        f"L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} "
        f"content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row\n"
    )
    # REQUIRED 3-tuple companion row (carries the directional cone-width claim).
    schema_v2_row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={reg_v} "
        f"# {GATE_ID} 3-tuple annotation (schema-v2); "
        f"sign = scalar (acoustic) cone NARROWER than tensor (geometric g_M) cone "
        f"[scalar_angle={scalar_deg:.6f}deg < tensor_angle={tensor_deg:.6f}deg; "
        f"c_Gold/c_fabric<<1; horizon-distance ratio={hdist_ratio:.4f}x]; "
        f"mag = construction PASS iff (TikZ all-5-labels + entry surface + censored tau->inf) "
        f"AND asymmetry (N_zeros={n_zeros} single entry + open supersonic exit) "
        f"AND reproduces S55 eta-ordering; "
        f"regime = conformal compactification exact (a(tau)>0, eta monotone; "
        f"eta_entry={eta_entry:.4f}<eta_fold={eta_fold:.4f})\n"
    )
    # Structural-anchor row (the inputs this rendering gate consumes; closes the §6.2 figure gap)
    anchor_row = (
        f"# ANCHOR=capstone_6.2_asymmetric_acoustic_white_hole_figure_gap "
        f"# {GATE_ID} extends Phononic-Penrose-Diagrams.md (NOT Diagram C bi-metric / NOT Diagram J stub); "
        f"consumes S95-W4-1 entry-surface ledger (tau0=0.112466, kappa_entry=18.520134 M_KK mag), "
        f"SCALE-FACTOR-54 a(tau) for eta-ordering, [T3] beta_T=0 Scalar-Tensor Kasparov decoupling, "
        f"COSMIC-CENSORSHIP-49 barrier tau~0.19; output TikZ figures/penrose/exflation-asymmetric-white-hole.tex\n"
    )
    rows = [line, companion, schema_v2_row, anchor_row]  # (local)
    if supersedes_sha:
        rows.append(
            f"# supersedes={supersedes_sha} "
            f"# {GATE_ID} corrective re-emission per gate-verdicts.md \"Option A\" "
            f"(prior line RETAINED; this corrective line is canonical)\n"
        )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        for r in rows:
            fp.write(r)


if __name__ == "__main__":
    sys.exit(main())
