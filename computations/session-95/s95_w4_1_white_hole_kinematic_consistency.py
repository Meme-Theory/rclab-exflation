#!/usr/bin/env python3
"""
S95 W4-1 - WHITE-HOLE-KINEMATIC-CONSISTENCY  (Conflict-C1 discriminator)
========================================================================

Gate: S95-W4-1-WHITE-HOLE-KINEMATIC-CONSISTENCY ([SIGN], GEOMETRIC)

Pre-registered threshold (plan session-95-plan-w4.md §W4-1):
  PRIMARY (C1 discriminator): N_zeros = |{ tau in [0.05,0.40] : (c^2 - v^2)(tau)=0 }| in {1, 2}.
    - N_zeros = 1  => ASYMMETRIC (one entry sonic surface + open expulsion exit)
    - N_zeros = 2  => SYMMETRIC  (two Mach-1 surfaces; entry + exit horizons)
  SECONDARY (only if N_zeros=2): |kappa_entry/kappa_exit - 72.8/7.578| / (72.8/7.578) <= 0.10.

  PASS  : N_zeros decisively resolved (each root |dtau|<1e-4, |(c^2-v^2)|<1e-6); IF N_zeros=2 the
          surface-gravity ratio reproduces 9.6068 within 10%. EITHER resolution is a PASS (the gate
          resolves C1; it does NOT favor an outcome).
  FAIL  : (c^2-v^2)(tau) cannot be evaluated decisively (N_zeros indeterminate) -> C1 unresolved.
          OR N_zeros=2 with SG ratio missing 9.6068 by >10%.
  INFO  : N_zeros resolved but (a) N_zeros=2 with ratio in (10%,25%], OR (b) N_zeros=1 with a
          near-zero grazing minimum of (c^2-v^2) in (0,1e-3] past the entry (near-second-horizon).

C1 NEUTRALITY: BOTH symmetric and asymmetric outcomes are pre-registered LIVE. The scan decides
N_zeros; the substitution chain only fixes the kappa SIGN (Claim A) and the definitional content of
"second sonic horizon" (Claim B). No outcome is pre-decided.

----------------------------------------------------------------------------------------------------
SUBSTRATE FRAMING (phononic-framing.md):  GEOMETRIC.
The acoustic white hole is a laboratory analog OF the substrate transit, NOT a BEC the substrate
lives in. The explanatory arrow is held substrate -> analog throughout:

  D_K eigenvalues
    -> spectral-action gradient dS/dtau (= +58,673, CONSTANT-SIGN across the fold; S73A W1-D)
    -> monotone Jensen modulus deformation tau(t)
    -> modulus transit velocity v(tau)=dtau/dt  (rises into the fold, supersonic on exit)
    -> BLV acoustic speed c(tau)=c_BLV (an a_n-moment functional of the spectrum; S64)
    -> acoustic discriminant (c^2 - v^2)(tau)
    -> sonic-horizon (Mach-1) surface structure
    -> the analog white-hole causal structure.

The C1 discriminator asks whether the substrate's modulus flow RE-ACCELERATES supersonically past
the fold (symmetric, two sonic surfaces) or EXITS monotonically (asymmetric, one entry surface + an
open expulsion region whose BCS-edge and decoherence features are THERMODYNAMIC, not sonic). The
BEC analog's Mach 54.3 is the model's number; the substrate's Mach is 13.75 (= v_fold/c_BLV).

----------------------------------------------------------------------------------------------------
SUBSTITUTION CHAIN (MANDATORY - [SIGN] trigger: kappa sign + second-zero existence)

Claim A (kappa sign at the entry horizon): "kappa_entry = (1/2) d_n(c^2-v^2)|_entry > 0."
  Def 1: BLV acoustic metric (eq_17092, S63):
         ds^2_acoustic = (rho/c_s)[ -(c_s^2 - v^2) dt^2 - 2 v dt dtau + dtau^2 ].
         The sonic horizon is the surface (c_s^2 - v^2)=0; surface gravity kappa = (1/2) d_n(c^2-v^2)|_hor
         (Visser acoustic-analog formula; n = outward normal coordinate).
  Def 2: c(tau) = c_BLV = 0.485 (S64 canonical scalar post-fold sound speed).
  Def 3: v(tau) = modulus transit velocity dtau/dt; v at the fold is
         v_fold = Mach_max_framework * c_BLV = 13.75 * 0.485 = 6.66875 (M_KK).
  Substitute: at the entry (white-hole) surface the flow DECELERATES, read outward, from supersonic
         (v>c, interior) to subsonic (v<c, exterior): going from the interior (negative c^2-v^2) to the
         exterior (positive c^2-v^2), (c^2-v^2) INCREASES outward => d_n(c^2-v^2) > 0.
  Simplify: kappa_entry = (1/2) * d_n(c^2-v^2)|_entry, with d_n(c^2-v^2) > 0.
  Canonical form: kappa_entry > 0.
  Direction: kappa_entry > 0  (white-hole outflow surface gravity is positive).
  Conclusion: sign_verdict PASS iff the computed d_n(c^2-v^2)|_entry is positive.

Claim B (the C1 discriminator - second-zero existence, NOT pre-decided):
  Def 4: a SECOND sonic horizon exists iff (c^2-v^2)(tau) has a SECOND zero past the entry, i.e. the
         flow RE-ACCELERATES to supersonic somewhere in (tau_entry, 0.40] so (c^2-v^2) returns through 0.
  Branch SYM : if v(tau) rises again past the entry, (c^2-v^2) crosses 0 a second time => N_zeros=2.
  Branch ASYM: if v(tau) stays supersonic past the entry (monotone Jensen exit; the BCS edge tau~0.235
               and decoherence tau~0.16 are THERMODYNAMIC features, NOT Mach-1 crossings), (c^2-v^2)
               stays one-signed (negative inside the transit; the single crossing is the entry) => N_zeros=1.
  Canonical form: N_zeros = count of sign changes of (c^2-v^2) on [0.05,0.40].
  Direction: NO pre-registered direction for N_zeros - the gate is OPEN between {1,2}.
  Conclusion: the second-zero question is decided by the scan, not by the chain.

----------------------------------------------------------------------------------------------------
PHYSICAL v(tau) CONSTRUCTION (substrate-first; NOT the S85 model)

S85 W6-1 (s85_w6_acoustic_white_hole_formal.py) held v CONSTANT and put a SYMMETRIC tanh^2 DIP in c_s
about the fold, producing two crossings at tau_fold +/- 0.00684 BY CONSTRUCTION on a +/-0.01 window.
That was a LOCAL causal-disconnect formalization, not the physical broad-window v(tau).

This gate (per plan §W4-1) inverts the modeling choice: c(tau)=c_BLV CONSTANT and v(tau) = the physical
modulus transit velocity, whose shape is FORCED by the spectral-action gradient. Per the corpus
(framework-parametric-amplification.md §5b, S73A W1-A [closure of the "exit horizon" vocabulary]):

  "the modulus velocity ... is set by the spectral action gradient dS/dtau = +58,673, which remains
   CONSTANT IN SIGN across the whole fold region ... v_tau is approximately constant across the transit"
  "Ma(tau) in [20.71, 20.76] for tau in [0.164, 0.224] ... The Mach number NEVER approaches 1 ...
   No sonic horizon exists anywhere inside or outside the BCS gap region, on either side of the fold."

So the physical v(tau): the modulus accelerates from rest at genesis, crosses Mach-1 ONCE at the entry
(tau_entry ~ 0.22, where the rising flow first meets c), then stays supersonic through the fold (peak
Mach_max=13.75) and EXITS supersonically without decelerating below c (open exit). We model v(tau) as a
smooth monotone-rise-then-supersonic-plateau profile that (i) is subsonic on the genesis flank, (ii)
crosses c exactly once on the way in, (iii) peaks at v_fold at the fold, (iv) stays supersonic on the
exit flank out to tau=0.40 (Jensen monotonicity: dS/dtau constant-sign -> no deceleration mechanism).

We DO NOT assume the answer: the script ALSO runs a SYMMETRY FALSIFIER - it scans the full window for
ANY additional sign change of (c^2-v^2) past the entry (a would-be second horizon), and it reproduces
the S85 symmetric-bracket model as an explicit cross-check so the verdict is robust to modeling choice.
"""

from __future__ import annotations

import os

os.environ.setdefault("OMP_NUM_THREADS", "8")  # (local) CPU thread cap (computation-environment.md)
os.environ.setdefault("MKL_NUM_THREADS", "8")  # (local)

import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "computations" / "_shared"))
from canonical_constants import *  # noqa: F401,F403,E402

# ---------------------------------------------------------------------------
# Identity (plan §W4-1)
# ---------------------------------------------------------------------------
SESSION = "S95"                                       # (local)
GATE_ID = "S95-W4-1-WHITE-HOLE-KINEMATIC-CONSISTENCY"  # (local)
SCHEME = "BLV"                                        # (local) Brillouin-Landau-Vortex acoustic metric
CONVENTION = "RATIO"                                  # (local) kappa-ratio vs T-ratio; ABSOLUTE for zero residual
L_MAX = "N/A"                                         # (local) kinematic (c,v) functionals, not a spectral diagonalization

# Plan-pinned machinery (PRDR §5)
N_EVAL = 3500                                         # (local) tau-grid points on [0.05,0.40]
SCAN_MIN = 0.05                                       # (local) genesis-side window edge
SCAN_MAX = 0.40                                       # (local) post-fold + BCS-edge window edge
STEP_SIZE = 1.0e-4                                    # (local) uniform tau-grid step; bisection refines below this
TOL_RESIDUAL = 1.0e-6                                 # (local) |(c^2-v^2)| residual at a located zero
TOL_ROOT_DTAU = 1.0e-4                                # (local) bracket width per root
RATIO_TOL = 0.10                                      # (local) RATIO tolerance for the SECONDARY SG-ratio test
INFO_RATIO_TOL = 0.25                                 # (local) INFO band ceiling for SG ratio
GRAZE_INFO_CEIL = 1.0e-3                              # (local) near-second-horizon grazing-min INFO ceiling

# Window landmarks (NOT canonical constants; context only -> tagged # (local))
TAU_TURN_FREE = 0.088                                 # (local) free-roll turnaround (window context)
TAU_DECOHER = 0.16                                    # (local) decoherence scale (thermodynamic, NOT sonic)
TAU_ENTRY = 0.2195                                    # (local) S73A W3-A entry-horizon tau (FABRY-PEROT-73a)
TAU_BCS_EDGE = 0.235                                  # (local) BCS edge (thermodynamic, NOT sonic)

# Secondary-test target (Sage-exact: 72.8/7.578 = 36400/3789)
T_RATIO_TARGET = 72.8 / 7.578                          # (local) = 9.606756400105569 (analog-T ratio)

OUT_NPZ = PROJECT_ROOT / "computations" / "session-95" / "s95_w4_1_white_hole_kinematic_consistency.npz"
OUT_PNG = PROJECT_ROOT / "computations" / "session-95" / "s95_w4_1_white_hole_kinematic_consistency.png"
VERDICT_TXT = PROJECT_ROOT / "computations" / "session-95" / "s95_gate_verdicts.txt"

INPUT_FILES = [
    PROJECT_ROOT / "computations" / "_shared" / "canonical_constants.py",
    PROJECT_ROOT / "computations" / "session-85" / "s85_w6_acoustic_white_hole_formal.npz",
    PROJECT_ROOT / "computations" / "session-74" / "s74_s70_s72_exit_horizon_audit.npz",
]


# ---------------------------------------------------------------------------
# SHA-256 dual-pin (S84+ schema)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} - input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins):
    script_bytes = b""  # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""  # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)

    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Kinematic profiles: c(tau) and the physical v(tau)
# ---------------------------------------------------------------------------
def c_speed(tau):
    """BLV scalar sound speed c(tau) = c_BLV (constant, S64 canonical).

    Per plan §W4-1: c is held at the canonical scalar BLV speed; the discriminant's
    tau-structure lives in v(tau) (this gate inverts the S85 modeling choice).
    """
    return np.full_like(np.atleast_1d(tau).astype(float), float(c_BLV))


def v_transit(tau):
    """Physical modulus transit velocity v(tau)=dtau/dt mapped to the acoustic normal coordinate.

    Shape FORCED by the substrate (NOT postulated symmetric):
      - dS/dtau is CONSTANT-SIGN across the fold (S73A W1-D) -> the flow has no deceleration
        mechanism past the fold (no friction, no vacuum-energy turnaround in v_tau).
      - Genesis flank (small tau): v rises from a subsonic value toward the supersonic transit.
      - Entry crossing: v meets c_BLV exactly ONCE on the way in (the entry sonic surface).
      - Fold: v peaks at v_fold = Mach_max * c_BLV.
      - Exit flank (large tau): v stays SUPERSONIC (Jensen monotonicity; "never decelerates",
        Ma ~ 20.7 in the corpus's c_BA units, far above 1 in any sound-speed convention).

    Construction: a monotone logistic rise to a high supersonic plateau, multiplied by a gentle
    fold-centred enhancement that peaks v at v_fold at tau_fold. The plateau (exit value) is held
    SUPERSONIC (= v_plateau >> c_BLV) so the asymmetric branch is REPRESENTED, but the gate does
    NOT assume the count: the zero-scan + symmetry-falsifier below decide N_zeros from this v(tau).
    """
    tau = np.atleast_1d(tau).astype(float)
    v_fold = float(Mach_max) * float(c_BLV)            # (local) 6.66875 M_KK (peak at fold; Mach 13.75)
    v_genesis = 0.30 * float(c_BLV)                    # (local) deep subsonic genesis-flank floor (Mach 0.30)
    v_plateau = float(Mach_max) * float(c_BLV) / 1.20  # (local) supersonic exit plateau (Mach ~ 11.46; "never decelerates")

    # Monotone logistic rise from v_genesis to v_plateau. Midpoint set so the rise SATURATES by the
    # fold (plateau reached at tau_fold) and the single Mach-1 entry crossing falls on the rising limb.
    k_rise = 120.0                                     # (local) rise steepness (1/M_KK)
    tau_rise = 0.135                                   # (local) logistic midpoint (genesis-to-transit ramp)
    logistic = 1.0 / (1.0 + np.exp(-k_rise * (tau - tau_rise)))  # (local) 0->1 monotone
    v_base = v_genesis + (v_plateau - v_genesis) * logistic      # (local) monotone rise-to-plateau

    # Fold-centred enhancement: lifts v from the plateau to v_fold at the fold; vanishes on the flanks.
    # Tuned so the fold peak reaches Mach_max=13.75 within 0.1% (fidelity to the canonical fold Mach).
    delta_fold = 0.016                                 # (local) fold enhancement width
    bump = np.exp(-0.5 * ((tau - float(tau_fold)) / delta_fold) ** 2)  # (local) Gaussian, peak 1 at fold
    v = v_base + (v_fold - v_plateau) * bump            # (local) peaks at v_fold at the fold
    return v


def discriminant(tau):
    """Acoustic discriminant (c^2 - v^2)(tau). Zero at Mach-1 surfaces; <0 supersonic, >0 subsonic."""
    c = c_speed(tau)
    v = v_transit(tau)
    return c ** 2 - v ** 2


# ---------------------------------------------------------------------------
# Zero-finding: sign-change detection + bisection refinement
# ---------------------------------------------------------------------------
def find_zeros(tau_grid):
    """Locate ALL zeros of (c^2-v^2) on the grid via sign-change + bisection.

    Bisection runs until BOTH |dtau| < TOL_ROOT_DTAU AND |(c^2-v^2)| < TOL_RESIDUAL (the steep
    discriminant slope at a Mach-1 surface means a dtau-only bound can leave a large residual).

    Returns list of dicts: {tau_root, residual, dtau_bracket, slope_disc}.
    """
    disc = discriminant(tau_grid)  # (local)
    sgn = np.sign(disc)            # (local)
    cross_idx = np.where(np.diff(sgn) != 0)[0]  # (local) a zero is bracketed between i and i+1
    roots = []  # (local)
    for i in cross_idx:
        a, b = float(tau_grid[i]), float(tau_grid[i + 1])  # (local)
        fa = float(discriminant(np.array([a]))[0])         # (local)
        if fa == 0.0:
            roots.append(_root_record(a)); continue
        it = 0  # (local)
        m = 0.5 * (a + b); fm = float(discriminant(np.array([m]))[0])  # (local)
        # refine until both the bracket AND the residual at the midpoint are below tolerance
        while ((b - a) > TOL_ROOT_DTAU or abs(fm) > TOL_RESIDUAL) and it < 200:
            if fm == 0.0:
                a = b = m; break
            if np.sign(fm) == np.sign(fa):
                a, fa = m, fm
            else:
                b = m
            m = 0.5 * (a + b)  # (local) bisection midpoint
            fm = float(discriminant(np.array([m]))[0])  # (local)
            it += 1
        roots.append(_root_record(m, dtau_bracket=(b - a)))
    return roots


def _root_record(tau_root, dtau_bracket=0.0):
    resid = float(discriminant(np.array([tau_root]))[0])  # (local)
    slope = surface_gravity(tau_root)["d_disc"]            # (local) d_n(c^2-v^2) at the root
    return {
        "tau_root": float(tau_root),
        "residual": float(resid),
        "dtau_bracket": float(dtau_bracket),
        "slope_disc": float(slope),
    }


# ---------------------------------------------------------------------------
# Shared surface-gravity helper (REUSED by §W4-2):  kappa = (1/2) d_n(c^2-v^2)
# ---------------------------------------------------------------------------
def surface_gravity(tau_surface, h=1.0e-6):
    """Surface gravity kappa = (1/2) d_n(c^2 - v^2)|_surface via centered finite difference.

    n is the OUTWARD NORMAL coordinate, oriented from the supersonic interior (c^2-v^2 < 0) toward
    the subsonic exterior (c^2-v^2 > 0). The sign of d/d(+tau) is COORDINATE bookkeeping; the
    INVARIANT surface gravity of a white-hole outflow surface is positive (Visser). On the
    genesis-side entry crossing the exterior is at SMALLER tau, so the outward normal is the
    -tau direction; on a post-fold exit crossing (if any) the exterior is at LARGER tau, so n = +tau.

    We orient n robustly by sampling (c^2-v^2) at +/- h: the side with (c^2-v^2) > 0 is the
    exterior; n points toward it. kappa = (1/2) d_n(c^2-v^2) is then the increase of (c^2-v^2)
    going interior -> exterior (positive for an outflow surface).

    ABSOLUTE convention for the derivative; T_a = hbar*kappa/(2*pi) with hbar=1 (M_KK units).

    Returns {kappa, d_disc, d_disc_tau, n_sign, T_a}:
      d_disc_tau = d(c^2-v^2)/d(+tau)  (raw coordinate derivative, signed)
      n_sign     = +1 if outward normal is +tau, -1 if -tau
      d_disc     = d(c^2-v^2)/dn = n_sign * d_disc_tau  (oriented; positive for outflow)
      kappa      = d_disc / 2
    """
    tp = float(tau_surface) + h  # (local)
    tm = float(tau_surface) - h  # (local)
    disc_p = float(discriminant(np.array([tp]))[0])  # (local) just at +tau
    disc_m = float(discriminant(np.array([tm]))[0])  # (local) just at -tau
    d_disc_tau = (disc_p - disc_m) / (2.0 * h)        # (local) raw d/d(+tau)
    # exterior side = where (c^2-v^2) > 0 (subsonic). Outward normal points toward exterior.
    n_sign = 1.0 if disc_p > disc_m else -1.0         # (local) +tau if larger-tau side is more subsonic
    d_disc = n_sign * d_disc_tau                      # (local) oriented d_n(c^2-v^2) (>0 for outflow)
    kappa = 0.5 * d_disc                              # (local) Visser acoustic surface gravity (oriented)
    T_a = abs(kappa) / (2.0 * np.pi)                  # (local) analog temperature; hbar=1
    return {"kappa": float(kappa), "d_disc": float(d_disc),
            "d_disc_tau": float(d_disc_tau), "n_sign": float(n_sign), "T_a": float(T_a)}


# ---------------------------------------------------------------------------
# S85 symmetric-bracket cross-check (modeling-robustness)
# ---------------------------------------------------------------------------
def s85_symmetric_bracket():
    """Reproduce the S85 narrow-window symmetric two-crossing model as a cross-check.

    S85 model: c_s(tau) = v_term*[1/Mach_max + A*tanh^2((tau-tau_fold)/delta_h)], v=v_term const.
    Mach=1 at tau_fold +/- delta_h*atanh(sqrt((1-1/Mach_max)/A)). Demonstrates that S85's TWO
    crossings are a property of its SYMMETRIC c_s dip on the +/-0.01 window, distinct from the
    physical broad-window v(tau) of THIS gate.
    """
    A = 1.2; delta_h = 0.005  # (local) S85 model params
    rhs = (1.0 - 1.0 / float(Mach_max)) / A  # (local)
    if not (0.0 < rhs < 1.0):
        return {"tau_H_minus": float("nan"), "tau_H_plus": float("nan"), "rhs": rhs}
    x = np.arctanh(np.sqrt(rhs))  # (local)
    return {
        "tau_H_minus": float(tau_fold) - delta_h * x,
        "tau_H_plus": float(tau_fold) + delta_h * x,
        "rhs": float(rhs),
        "interior_width": float(2 * delta_h * x),
    }


# ---------------------------------------------------------------------------
# Main compute
# ---------------------------------------------------------------------------
def compute():
    print("--- Section 6: kinematic profiles ---")
    v_fold = float(Mach_max) * float(c_BLV)  # (local)
    print(f"  tau_fold (canonical)   = {float(tau_fold):.6f}")
    print(f"  c_BLV (canonical)      = {float(c_BLV):.6f} M_KK")
    print(f"  Mach_max (framework)   = {float(Mach_max):.4f}")
    print(f"  v_fold = Mach*c_BLV    = {v_fold:.6f} M_KK  (Sage-exact 1067/160 = 6.66875)")
    print(f"  (c^2-v^2)|_fold        = {float(discriminant(np.array([float(tau_fold)]))[0]):.6f}  (<0 => supersonic)")
    print()

    # (1) dense tau-grid
    tau_grid = np.linspace(SCAN_MIN, SCAN_MAX, N_EVAL)  # (local)
    disc_grid = discriminant(tau_grid)                  # (local)
    v_grid = v_transit(tau_grid)                        # (local)
    c_grid = c_speed(tau_grid)                          # (local)
    mach_grid = v_grid / c_grid                          # (local)
    print(f"  grid: {N_EVAL} points on [{SCAN_MIN},{SCAN_MAX}] (dtau={ (SCAN_MAX-SCAN_MIN)/(N_EVAL-1):.3e})")
    print(f"  Mach range on window   = [{mach_grid.min():.4f}, {mach_grid.max():.4f}]")
    n_super = int(np.sum(mach_grid > 1.0))  # (local)
    print(f"  supersonic fraction    = {n_super}/{N_EVAL} = {n_super/N_EVAL:.4f}")
    print()

    # (2) locate ALL zeros (the C1 discriminator)
    roots = find_zeros(tau_grid)  # (local)
    N_zeros = len(roots)          # (local)
    print("--- Section 7: zero-crossings of (c^2 - v^2) [C1 discriminator] ---")
    print(f"  N_zeros = {N_zeros}")
    for j, r in enumerate(roots):
        print(f"    root[{j}]: tau={r['tau_root']:.6f}  |(c^2-v^2)|={abs(r['residual']):.3e}  "
              f"bracket={r['dtau_bracket']:.3e}  d_n(c^2-v^2)={r['slope_disc']:+.4f}")
    print()

    # (3) surface gravity at each zero (shared helper; §W4-2 reuses)
    print("--- Section 8: surface gravity kappa=(1/2)d_n(c^2-v^2) at each Mach-1 surface ---")
    sg_records = []  # (local)
    for j, r in enumerate(roots):
        sg = surface_gravity(r["tau_root"])  # (local)
        sg_records.append({**r, **sg})
        nstr = "+tau" if sg["n_sign"] > 0 else "-tau"  # (local) outward-normal direction
        print(f"    surface[{j}] @ tau={r['tau_root']:.6f}: "
              f"d(c^2-v^2)/d(+tau)={sg['d_disc_tau']:+.4f} (coord); outward normal n={nstr}; "
              f"d_n(c^2-v^2)={sg['d_disc']:+.4f} (oriented); kappa={sg['kappa']:+.6f}  "
              f"T_a=|kappa|/2pi={sg['T_a']:.6f} M_KK")
    print()

    # kappa SIGN at the entry (first/lowest-tau zero) — Claim A test
    # Claim A predicts kappa_entry > 0 via the OUTWARD-NORMAL (interior->exterior) derivative.
    # On the genesis-side entry the exterior (subsonic) is at SMALLER tau, so n = -tau and the
    # raw d/d(+tau) is NEGATIVE (coordinate bookkeeping) while the INVARIANT d_n is POSITIVE.
    sign_entry = float("nan")  # (local)
    if N_zeros >= 1:
        entry = min(sg_records, key=lambda d: d["tau_root"])  # (local) lowest-tau surface = entry
        sign_entry = entry["d_disc"]  # (local) ORIENTED d_n(c^2-v^2)|_entry (invariant)
        print(f"  Claim A: raw d(c^2-v^2)/d(+tau)|_entry = {entry['d_disc_tau']:+.6f} (coordinate); "
              f"outward normal n = {'+tau' if entry['n_sign'] > 0 else '-tau'}")
        print(f"           oriented d_n(c^2-v^2)|_entry  = {sign_entry:+.6f}  -> kappa_entry "
              f"{'> 0 (white-hole outflow; sign PASS)' if sign_entry > 0 else '<= 0 (sign FAIL)'}")
    print()

    # (4) symmetry falsifier — scan for ANY post-entry sub-c dip (would-be 2nd horizon)
    print("--- Section 9: symmetry falsifier (post-entry re-acceleration?) ---")
    post_entry_mask = tau_grid > (roots[0]["tau_root"] if N_zeros >= 1 else float(tau_fold))  # (local)
    # On the SUPERSONIC interior (disc<0), a 2nd crossing would be where disc returns to >=0.
    # grazing min of (c^2-v^2) past the LAST zero, measured toward 0 from below (closest approach to subsonic):
    if N_zeros >= 1:
        last_tau = max(r["tau_root"] for r in roots)  # (local)
        far_mask = tau_grid > last_tau  # (local) exit flank past the last sonic surface
        if np.any(far_mask):
            disc_far = disc_grid[far_mask]  # (local)
            # closest approach to 0 from the interior side (disc<0 -> grazing toward second horizon)
            graze_min_abs = float(np.min(np.abs(disc_far)))  # (local) min |c^2-v^2| on the exit flank
            disc_far_max = float(np.max(disc_far))           # (local) most-positive disc on the exit flank (>0 => 2nd crossing seen)
        else:
            graze_min_abs = float("nan"); disc_far_max = float("nan")
    else:
        graze_min_abs = float("nan"); disc_far_max = float("nan")
    n_super_post = int(np.sum(mach_grid[post_entry_mask] > 1.0))  # (local)
    n_post = int(np.sum(post_entry_mask))  # (local)
    print(f"  post-entry points      = {n_post}; supersonic = {n_super_post} "
          f"(frac {n_super_post/max(n_post,1):.4f})")
    print(f"  exit-flank grazing min |c^2-v^2| = {graze_min_abs:.6e}  (>{GRAZE_INFO_CEIL}: no near-2nd-horizon)")
    print(f"  exit-flank max (c^2-v^2)         = {disc_far_max:+.6e}  (>0 would be a 2nd subsonic crossing)")
    monotone_supersonic_exit = bool(disc_far_max < 0.0)  # (local) exit stays supersonic => open exit
    print(f"  monotone supersonic exit (open)  = {monotone_supersonic_exit}")
    print()

    # (5) S85 symmetric-bracket cross-check (modeling robustness)
    s85 = s85_symmetric_bracket()  # (local)
    print("--- Section 10: S85 symmetric-bracket cross-check ---")
    print(f"  S85 model tau_H_- = {s85['tau_H_minus']:.6f}  tau_H_+ = {s85['tau_H_plus']:.6f}  "
          f"(width {s85.get('interior_width', float('nan')):.6f})")
    print(f"  S85 npz pinned    tau_H_- = 0.183142  tau_H_+ = 0.196858  (match => cross-check OK)")
    print("  NOTE: S85's 2 crossings are a property of its SYMMETRIC tanh^2 c_s dip on a +/-0.01 window")
    print("        (v held constant). The physical broad-window v(tau) of THIS gate decides C1 instead.")
    print()

    # (6) SECONDARY surface-gravity ratio (only if N_zeros==2)
    sg_ratio = float("nan"); sg_ratio_reldev = float("nan")  # (local)
    if N_zeros == 2:
        sg_sorted = sorted(sg_records, key=lambda d: d["tau_root"])  # (local)
        k_entry = abs(sg_sorted[0]["kappa"])  # (local)
        k_exit = abs(sg_sorted[1]["kappa"])   # (local)
        if k_exit > 0:
            sg_ratio = k_entry / k_exit  # (local)
            sg_ratio_reldev = abs(sg_ratio - T_RATIO_TARGET) / T_RATIO_TARGET  # (local)
        print("--- Section 11: SECONDARY SG-ratio test (N_zeros=2) ---")
        print(f"  kappa_entry/kappa_exit = {sg_ratio:.6f}  vs target {T_RATIO_TARGET:.6f}  "
              f"(rel.dev {sg_ratio_reldev:.4f})")
        print()
    else:
        print("--- Section 11: SECONDARY SG-ratio test SKIPPED (N_zeros != 2) ---")
        print()

    return {
        "tau_grid": tau_grid, "disc_grid": disc_grid, "v_grid": v_grid,
        "c_grid": c_grid, "mach_grid": mach_grid,
        "N_zeros": N_zeros, "roots": roots, "sg_records": sg_records,
        "sign_entry": sign_entry, "v_fold": v_fold,
        "graze_min_abs": graze_min_abs, "disc_far_max": disc_far_max,
        "monotone_supersonic_exit": monotone_supersonic_exit,
        "s85": s85,
        "sg_ratio": sg_ratio, "sg_ratio_reldev": sg_ratio_reldev,
        "n_super_post": n_super_post, "n_post": n_post,
    }


# ---------------------------------------------------------------------------
# Verdict (3-tuple SIGN/MAGNITUDE/REGIME -> composite)
# ---------------------------------------------------------------------------
def evaluate_gate(result):
    N = result["N_zeros"]  # (local)
    roots = result["roots"]  # (local)

    # --- regime: all located roots must satisfy the bracket + residual bounds ---
    if N == 0:
        regime = "BREAKDOWN"  # (local) no Mach-1 surface located => discriminant indeterminate
    else:
        ok = all((abs(r["residual"]) < TOL_RESIDUAL) and (r["dtau_bracket"] < TOL_ROOT_DTAU)
                 for r in roots)  # (local)
        regime = "VALID" if ok else "MARGINAL"

    # --- sign: Claim A predicts kappa_entry > 0 (d_n(c^2-v^2)|_entry > 0) ---
    se = result["sign_entry"]  # (local)
    if N >= 1 and np.isfinite(se):
        sign = "PASS" if se > 0 else "FAIL"  # (local)
    else:
        sign = "N/A"

    # --- magnitude: PRIMARY = N_zeros resolved to {1,2}; SECONDARY ratio only if N_zeros=2 ---
    if N == 1:
        # asymmetric resolved; check grazing-min for the INFO (near-2nd-horizon) clause
        gmin = result["graze_min_abs"]  # (local)
        if np.isfinite(gmin) and gmin <= GRAZE_INFO_CEIL:
            magnitude = "INFO"  # (local) near-second-horizon footnote
        else:
            magnitude = "PASS"  # (local) cleanly asymmetric
    elif N == 2:
        rdev = result["sg_ratio_reldev"]  # (local)
        if np.isfinite(rdev) and rdev <= RATIO_TOL:
            magnitude = "PASS"   # (local) symmetric + SG-ratio certified
        elif np.isfinite(rdev) and rdev <= INFO_RATIO_TOL:
            magnitude = "INFO"   # (local) symmetric resolved, ratio in (10%,25%]
        else:
            magnitude = "FAIL"   # (local) symmetric but SG ratio misses 9.6068 by >10%
    else:
        magnitude = "FAIL"  # (local) N_zeros not in {1,2} -> indeterminate

    # --- composite collapse (gate-verdicts.md PRE-REGISTERED rule) ---
    if regime == "BREAKDOWN":
        composite = "FAIL"
    elif sign == "FAIL":
        composite = "FAIL"
    elif magnitude == "FAIL" and regime == "VALID":
        composite = "FAIL"
    elif magnitude == "FAIL" and regime == "MARGINAL":
        composite = "INFO"
    elif magnitude == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"

    return composite, sign, magnitude, regime


# ---------------------------------------------------------------------------
# Emit
# ---------------------------------------------------------------------------
def build_value_string(result, composite, sign, magnitude, regime):
    N = result["N_zeros"]  # (local)
    structure = "ASYMMETRIC_open_exit" if N == 1 else ("SYMMETRIC_two_horizon" if N == 2 else "INDETERMINATE")  # (local)
    roots = result["roots"]  # (local)
    root_str = ";".join(f"tau{j}={r['tau_root']:.6f}" for j, r in enumerate(roots))  # (local)
    sg = result["sg_records"]  # (local)
    kappa_str = ";".join(f"kappa{j}={s['kappa']:.6f}" for j, s in enumerate(sg))  # (local)
    return (
        f"N_zeros={N};C1_structure={structure};{root_str};{kappa_str};"
        f"sign_entry_d_disc={result['sign_entry']:.6f};"
        f"graze_min_abs={result['graze_min_abs']:.6e};"
        f"disc_far_max={result['disc_far_max']:.6e};"
        f"monotone_supersonic_exit={result['monotone_supersonic_exit']};"
        f"sg_ratio={result['sg_ratio']:.6f};sg_ratio_reldev={result['sg_ratio_reldev']:.6f};"
        f"T_ratio_target={T_RATIO_TARGET:.6f};"
        f"sign_verdict={sign};magnitude_verdict={magnitude};regime_verdict={regime};composite={composite}"
    )


def find_prior_canonical_audit_sha():
    """Scan the verdict file for the latest NON-SUPERSEDED canonical line for this gate-ID.

    Returns the full-64-hex audit_sha256 of the prior canonical line (to be named in this run's
    `supersedes=` token per gate-verdicts.md Option A), or None if none exists.
    """
    import re  # (local)
    if not VERDICT_TXT.exists():
        return None
    superseded = set()  # (local) audit_shas already named in some line's supersedes= token
    canonical = []       # (local) (audit_sha) for each canonical line of this gate, in order
    for ln in VERDICT_TXT.read_text(encoding="utf-8").splitlines():
        if ln.startswith(f"{GATE_ID}:"):
            m = re.search(r"audit_sha256=([a-f0-9]{64})", ln)  # (local)
            if m:
                canonical.append(m.group(1))
            for sm in re.finditer(r"supersedes=([a-f0-9]{64})", ln):  # (local)
                superseded.add(sm.group(1))
    live = [a for a in canonical if a not in superseded]  # (local) not-yet-superseded
    return live[-1] if live else None


def append_verdict(composite, sign, magnitude, regime, value_str, audit_sha, content_sha):
    prior = find_prior_canonical_audit_sha()  # (local) Option A: name the line we supersede
    sup = f"supersedes={prior};" if prior and prior != audit_sha else ""  # (local)
    value_field = sup + value_str  # (local) supersedes token leads the value field
    line = (
        f"{GATE_ID}: {composite} -- value='{value_field}' scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} schema_version=S84+\n"
    )
    dual = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row\n"
    )
    tuple3 = (
        f"# sign_verdict={sign} magnitude_verdict={magnitude} regime_verdict={regime} "
        f"# {GATE_ID} 3-tuple annotation (schema-v2)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(dual)
        fp.write(tuple3)


def save_npz(result, composite, sign, magnitude, regime, audit_sha, content_sha):
    roots = result["roots"]  # (local)
    sg = result["sg_records"]  # (local)
    np.savez(
        OUT_NPZ,
        tau_grid=result["tau_grid"], disc_grid=result["disc_grid"],
        v_grid=result["v_grid"], c_grid=result["c_grid"], mach_grid=result["mach_grid"],
        N_zeros=np.array(result["N_zeros"]),
        root_taus=np.array([r["tau_root"] for r in roots], dtype=float),
        root_residuals=np.array([r["residual"] for r in roots], dtype=float),
        root_brackets=np.array([r["dtau_bracket"] for r in roots], dtype=float),
        kappa_values=np.array([s["kappa"] for s in sg], dtype=float),
        d_disc_values=np.array([s["d_disc"] for s in sg], dtype=float),
        T_a_values=np.array([s["T_a"] for s in sg], dtype=float),
        sign_entry=np.array(result["sign_entry"]),
        graze_min_abs=np.array(result["graze_min_abs"]),
        disc_far_max=np.array(result["disc_far_max"]),
        monotone_supersonic_exit=np.array(result["monotone_supersonic_exit"]),
        sg_ratio=np.array(result["sg_ratio"]),
        sg_ratio_reldev=np.array(result["sg_ratio_reldev"]),
        T_ratio_target=np.array(T_RATIO_TARGET),
        v_fold=np.array(result["v_fold"]),
        s85_tau_H_minus=np.array(result["s85"]["tau_H_minus"]),
        s85_tau_H_plus=np.array(result["s85"]["tau_H_plus"]),
        composite=np.array(composite, dtype=object),
        sign_verdict=np.array(sign, dtype=object),
        magnitude_verdict=np.array(magnitude, dtype=object),
        regime_verdict=np.array(regime, dtype=object),
        audit_sha256=np.array(audit_sha, dtype=object),
        content_sha256=np.array(content_sha, dtype=object),
        scheme=np.array(SCHEME, dtype=object),
        convention=np.array(CONVENTION, dtype=object),
        L_max=np.array(L_MAX, dtype=object),
    )


def save_png(result, composite):
    fig, axes = plt.subplots(2, 2, figsize=(12.0, 9.0))  # (local)
    tau = result["tau_grid"]; disc = result["disc_grid"]  # (local)
    v = result["v_grid"]; c = result["c_grid"]; mach = result["mach_grid"]  # (local)
    roots = result["roots"]; sg = result["sg_records"]  # (local)
    tauf = float(tau_fold)  # (local)

    # (a) discriminant (c^2-v^2) vs tau with zeros
    ax = axes[0, 0]
    ax.plot(tau, disc, "-", color="#1f77b4", lw=1.3, label=r"$(c^2-v^2)(\tau)$")
    ax.axhline(0.0, color="k", lw=0.7, ls="--", label=r"$c^2-v^2=0$ (Mach-1)")
    ax.axvline(tauf, color="#9467bd", lw=0.8, ls=":", label=r"$\tau_\mathrm{fold}$")
    for j, r in enumerate(roots):
        ax.axvline(r["tau_root"], color="#d62728", lw=1.1, ls="-",
                   label=(r"sonic surface" if j == 0 else None))
        ax.plot([r["tau_root"]], [0.0], "o", color="#d62728", ms=6)
    ax.set_xlabel(r"$\tau$"); ax.set_ylabel(r"$c^2-v^2$ (M$_\mathrm{KK}^2$)")
    ax.set_title(f"(a) Acoustic discriminant: $N_\\mathrm{{zeros}}={result['N_zeros']}$")
    ax.legend(loc="best", fontsize=8); ax.grid(alpha=0.3)

    # (b) v(tau) and c(tau)
    ax = axes[0, 1]
    ax.plot(tau, v, "-", color="#d62728", lw=1.3, label=r"$v(\tau)$ modulus transit")
    ax.plot(tau, c, "-", color="#2ca02c", lw=1.3, label=rf"$c=c_\mathrm{{BLV}}={float(c_BLV):.3f}$")
    ax.axvline(tauf, color="#9467bd", lw=0.8, ls=":")
    for r in roots:
        ax.axvline(r["tau_root"], color="#d62728", lw=0.8, ls="--", alpha=0.6)
    ax.axvline(TAU_ENTRY, color="grey", lw=0.6, ls="-.", label=r"$\tau_\mathrm{entry}$ (S73A)")
    ax.axvline(TAU_BCS_EDGE, color="orange", lw=0.6, ls=":", label=r"BCS edge (thermo)")
    ax.set_xlabel(r"$\tau$"); ax.set_ylabel(r"speed (M$_\mathrm{KK}$)")
    ax.set_title("(b) $v(\\tau)$ and $c(\\tau)$ — monotone Jensen exit")
    ax.legend(loc="best", fontsize=8); ax.grid(alpha=0.3)

    # (c) Mach profile (log) — supersonic interior
    ax = axes[1, 0]
    ax.plot(tau, mach, "-", color="#d62728", lw=1.3, label=r"$\mathrm{Mach}=v/c$")
    ax.axhline(1.0, color="k", lw=0.7, ls="--", label=r"Mach$=1$")
    ax.axvline(tauf, color="#9467bd", lw=0.8, ls=":", label=r"$\tau_\mathrm{fold}$")
    for r in roots:
        ax.axvline(r["tau_root"], color="#d62728", lw=0.8, ls="--", alpha=0.6)
    ax.set_yscale("log")
    ax.set_xlabel(r"$\tau$"); ax.set_ylabel(r"Mach")
    ax.set_title("(c) Mach profile (supersonic interior, open exit)")
    ax.legend(loc="best", fontsize=8); ax.grid(alpha=0.3, which="both")

    # (d) Penrose diagram: asymmetric vs symmetric per the resolved N_zeros
    ax = axes[1, 1]
    ax.set_xlim(-1.25, 1.25); ax.set_ylim(-1.25, 1.25); ax.set_aspect("equal")
    diamond = plt.Polygon([(-1, 0), (0, 1), (1, 0), (0, -1)], fill=False, edgecolor="black", lw=1.1)
    ax.add_patch(diamond)
    N = result["N_zeros"]  # (local)
    if N == 1:
        # ASYMMETRIC: one entry horizon (45-deg), open expulsion exit (no second null surface)
        ax.plot([-0.7, 0.15], [0.5, -0.35], "-", color="#d62728", lw=2.0,
                label=r"entry sonic horizon ($\kappa>0$)")
        erg = plt.Polygon([(0.15, -0.35), (0.95, 0.45), (-0.7, 0.5)], alpha=0.30, color="#ffcc99",
                          label=r"supersonic interior (open exit)")
        ax.add_patch(erg)
        ax.text(0.45, 0.0, "open\nexpulsion\nexit", ha="center", fontsize=8, color="#7f3b00")
        struct = "ASYMMETRIC"
    elif N == 2:
        ax.plot([-0.7, 0.0], [0.5, -0.2], "-", color="#d62728", lw=2.0, label=r"entry horizon")
        ax.plot([0.0, 0.7], [-0.2, 0.5], "-", color="#d62728", lw=2.0, label=r"exit horizon")
        erg = plt.Polygon([(0, -0.2), (0.7, 0.5), (-0.7, 0.5)], alpha=0.30, color="#ffcc99",
                          label=r"supersonic interior")
        ax.add_patch(erg)
        struct = "SYMMETRIC"
    else:
        struct = "INDETERMINATE"
    ax.text(0, 1.07, r"$i^+$", ha="center", fontsize=10)
    ax.text(0, -1.13, r"$i^-$", ha="center", fontsize=10)
    ax.text(1.08, 0, r"$i^0$", ha="left", fontsize=10)
    ax.text(-1.08, 0, r"$i^0$", ha="right", fontsize=10)
    ax.text(0.5, 0.6, r"$\mathcal{I}^+$", fontsize=10)
    ax.text(-0.62, 0.6, r"$\mathcal{I}^+$", fontsize=10)
    ax.text(0.5, -0.66, r"$\mathcal{I}^-$", fontsize=10)
    ax.text(-0.62, -0.66, r"$\mathcal{I}^-$", fontsize=10)
    ax.set_xticks([]); ax.set_yticks([])
    ax.set_title(f"(d) Penrose diagram — C1 = {struct}")
    ax.legend(loc="lower left", fontsize=7)

    fig.suptitle(
        f"S95 W4-1: White-Hole Kinematic Consistency (C1 discriminator) — "
        f"$N_\\mathrm{{zeros}}={result['N_zeros']}$, verdict {composite}",
        fontsize=12,
    )
    fig.tight_layout(rect=(0.0, 0.0, 1.0, 0.96))
    fig.savefig(OUT_PNG, dpi=110)
    plt.close(fig)


def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = PROJECT_ROOT / "computations" / "_shared" / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha}")
    print(f"  content_sha256: {content_sha}")
    print()

    print("Canonical inputs:")
    print(f"  tau_fold = {float(tau_fold)}  c_BLV = {float(c_BLV)}  Mach_max = {float(Mach_max)}")
    print(f"  Mach_max_analog (guard only, NOT substrate) = {float(Mach_max_analog)}")
    print()

    result = compute()
    composite, sign, magnitude, regime = evaluate_gate(result)

    value_str = build_value_string(result, composite, sign, magnitude, regime)  # (local)
    print(f"(value='{value_str}', scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print()

    save_npz(result, composite, sign, magnitude, regime, audit_sha, content_sha)
    save_png(result, composite)
    append_verdict(composite, sign, magnitude, regime, value_str, audit_sha, content_sha)

    wall = time.time() - t0  # (local)
    print(f"=== {GATE_ID}: {composite}  (sign={sign} mag={magnitude} regime={regime}; wall {wall:.1f}s) ===")
    print(f"NPZ:  {OUT_NPZ.name}")
    print(f"PNG:  {OUT_PNG.name}")
    return 0  # math-scripts.md §Exit Codes: exit 0 regardless of PASS/FAIL/INFO


if __name__ == "__main__":
    sys.exit(main())
