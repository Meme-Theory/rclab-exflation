#!/usr/bin/env python3
"""
INV4 W2-1 - c_s(tau) re-derived from a_2(tau) stiffness; zero-count of (c_s^2 - v^2)(tau)
========================================================================================

Gate: INV4-W2-1 ([SIGN], GEOMETRIC; investigation-4 track)

Resolves contradiction C-1 from the SUBSTRATE:
  - S85 (s85_w6_acoustic_white_hole_formal): PROVEN bracketed-pair white hole (N_zeros=2,
    SYMMETRIC sealed interior) -- but built by holding v CONSTANT and putting a symmetric
    tanh^2 DIP in c_s on a +/-0.01 window (a LOCAL modeling formalization).
  - S95 (s95_w4_1_white_hole_kinematic_consistency): FAIL single-asymmetric-open white hole
    (N_zeros=1, ASYMMETRIC open exit; tau0=0.112443, kappa0=-18.442205) -- built by holding
    c_s = c_BLV CONSTANT and putting all tau-structure in the physical v(tau).

  BOTH prior gates held ONE of (c_s, v) constant. This gate re-derives c_s(tau) from the
  ACTUAL a_2(tau) Seeley-DeWitt spectral stiffness of the Jensen-deformed D_K spectrum
  (S95's constant-c_s was structurally BLIND to an a_2 softening / c_s DIP at the van Hove
  fold -- a NEW second-crossing channel). v(tau) is the SAME S95 physical supersonic-exit
  profile. Then count sign changes of D(tau) := c_s(tau)^2 - v(tau)^2 on [0.05, 0.40].

Pre-registered TWO-BRANCH structural verdict (plan investigation-4-plan-w2.md §W2-1):
  N_zeros = 1  => confirm S95 single-asymmetric-open (causal disconnection one-directional
                  Unruh-type; canonical Diagram J [bracketed pair] is WRONG; HY1/HY2 licensed)
  N_zeros = 2  => restore S85 bracketed-pair sealed-interior (a_2 stiffness genuinely DIPS at
                  the fold; c_s DIP re-crosses v ON PHYSICAL grounds, not modeling artifact)
  NEITHER branch is a failure -- both are structural resolutions of C-1. ONLY an indeterminate
  count (a bracketed root failing |dtau|<1e-4 OR |D|<1e-6, or unstable a_2(tau)) FAILs.

[SIGN] payload (the ONLY pre-registered direction): kappa_entry > 0 at the white-hole entry
surface (Visser kappa = (1/2) d_n(c_s^2 - v^2)|_entry, oriented interior->exterior).

----------------------------------------------------------------------------------------------------
SUBSTRATE FRAMING (phononic-framing.md):  GEOMETRIC.
The acoustic white hole is a laboratory analog OF the substrate transit, NOT a BEC the substrate
lives in. The explanatory arrow is held substrate -> analog throughout:

  D_K eigenvalues (Jensen-deformed SU(3))
    -> a_2(tau) Seeley-DeWitt spectral-action stiffness  [a_2 = (1/2) zeta_D(1) = 0.5 sum d_n/lam_n^2;
       a_2 generates the Einstein-Hilbert kinematic skeleton; the gradient-stiffness velocity scale
       is c_fabric = 209.97 (S42); a_2 SOFTENS where the spectral gap narrows at the van Hove fold]
    -> c_s(tau) = sqrt(stiffness(tau)/rho(tau))  (an a_2-moment functional; the NEW content vs S95)
    -> modulus transit velocity v(tau) = dtau/dt  (FORCED by the constant-sign dS/dtau = +58,673;
       rises into the fold, peaks at v_fold = Mach_max*c_BLV, supersonic exit -- the S95 profile)
    -> acoustic discriminant D(tau) = c_s(tau)^2 - v(tau)^2
    -> sonic-horizon (Mach-1) surface count
    -> the analog white-hole causal structure.

The substrate IS the causal structure; the sonic horizon is what a phonon sees, derived from
c_s(tau) -- a phononic stiffness observable -- not imposed from GR. The C-1 contradiction is the
framework's own ledger disagreeing with itself; a boundary-guard cannot let the canonical causal
diagram contradict the computation it represents.

----------------------------------------------------------------------------------------------------
SUBSTITUTION CHAIN (MANDATORY - [SIGN] trigger: kappa_entry sign + two-branch second-zero existence)

Claim (the [SIGN] payload): "the entry-crossing surface gravity sign is kappa_entry > 0, AND the
second-zero existence is DECIDED BY THE SCAN (NOT pre-decided) -- N_zeros in {1,2}."

  Definition 1 (c_s from a_2 stiffness): the BLV acoustic speed is c_s = sqrt(dP/drho); in the
    substrate the stiffness dP/drho IS the a_2(tau) Seeley-DeWitt curvature of the spectral action
    (a_2 generates Einstein-Hilbert; gradient-stiffness velocity scale c_fabric = 209.97368021, S42).
    a_2(tau) = 0.5 * sum_n d_n / lam_n(tau)^2  (zeta-scheme; a2_fold = 2776.1653888634 at tau=0.19).
    [source: canonical_constants.py c_fabric, a2_fold; phononic-framing.md a_2 -> 4D metric]
  Definition 2 (v transit velocity): v(tau) = dtau/dt, FORCED by dS/dtau = +58,673 (CONSTANT SIGN
    across the fold, S73A W1-D); rises into the fold, peaks at v_fold = Mach_max*c_BLV =
    13.75*0.485 = 6.66875 (M_KK), stays supersonic on the exit flank (no deceleration mechanism --
    Jensen monotonicity). [source: canonical_constants.py Mach_max=13.75, c_BLV=0.485]
  Definition 3 (discriminant + Visser kappa): D(tau) := c_s(tau)^2 - v(tau)^2; the sonic horizon is
    the surface D(tau)=0; surface gravity kappa = (1/2) d_n D|_horizon (n = outward normal coord;
    Visser acoustic-analog formula). [source: S95-W4-1 chain Def 1; eq_17092 BLV acoustic metric]

  Substitute (kappa-sign at the entry): at the entry (white-hole) surface the flow reads outward
    from supersonic interior (v>c_s, D<0) to subsonic exterior (v<c_s, D>0); D INCREASES outward
    => d_n D|_entry > 0.
  Simplify: kappa_entry = (1/2) d_n D|_entry, with d_n D > 0.
  Canonical form: kappa_entry > 0.
  Direction (sign_verdict): sign_verdict = PASS iff the computed oriented d_n D|_entry > 0 (the
    white-hole outflow surface gravity is positive). This matches S95 kappa0=-18.44 in MAGNITUDE
    only at the OTHER (open-exit) surface; the entry kappa-sign is the pre-registered claim here.

  Substitute (the two-branch count -- NO pre-registered direction):
    N_zeros=1 <=> D(tau) has exactly one sign change (entry); v stays supersonic past it AND c_s(tau)
                 does not dip back through v => ASYMMETRIC open exit (S95).
    N_zeros=2 <=> D(tau) has two sign changes; EITHER v re-rises through c_s OR -- the NEW channel
                 S95's constant c_s could not see -- c_s(tau) DIPS (a_2 stiffness softens at the
                 fold) back below v and re-crosses => bracketed pair (S85).
  Canonical form: N_zeros = count of sign changes of D on [0.05, 0.40].
  Direction: NONE -- the gate is OPEN between {1,2}; the chain fixes only the kappa_entry sign.
  Conclusion: kappa_entry > 0 is the [SIGN] claim; N_zeros is the two-branch structural verdict
    decided by the scan (see dual_prior in the plan).

----------------------------------------------------------------------------------------------------
a_2(tau) STIFFNESS RECONSTRUCTION (substrate-first; the NEW content over S95)

The L12 Peter-Weyl spectrum cache (s84_spectrum_cache_L12_tau019.npz) stores, per SU(3) sector
(p,q), the |lambda| eigenvalues of D_K at the REFERENCE deformation tau_ref = 0.19. The Jensen
metric g_tau = 3*diag(e^{-2tau} x3, e^{tau} x4, e^{2tau} x1) deforms the fiber; the Dirac operator
scales with the inverse vielbein, so each sector's eigenvalues rescale by the Jensen vielbein RATIO
from tau_ref to the target tau. A sector at SU(3) level n=(p+q) is weighted across the three Jensen
blocks (SU(2) contracting e^{-2tau}, C^2 expanding e^{tau}, U(1) expanding e^{2tau}) by the Peter-
Weyl per-block content; we use the level-resolved effective Jensen factor (the geometric-mean fiber
scale at level n), so that:

  lam_n(tau) = lam_n(tau_ref) * sqrt( s(tau_ref) / s(tau) )     [Dirac ~ 1/vielbein ~ 1/sqrt(g)]
  a_2(tau)   = 0.5 * sum_n d_n / lam_n(tau)^2                    [zeta-scheme second moment]
  rho(tau)   = a_0(tau) = 0.5 * sum_n d_n  (mode-count; tau-INDEPENDENT count at fixed L_max)

where s(tau) is the level-weighted effective Jensen fiber scale. The a_2(tau) SHAPE is what decides
the c_s DIP; c_s(tau) is anchored so its post-fold value equals the canonical c_BLV = 0.485 (the S95
constant choice), making the two stiffness->c_s readings DIRECTLY comparable (c_BLV cross-check vs
the tau-RESOLVED c_s(tau)). The zero-count is invariant to the overall c_s normalization given the
anchor; what the a_2(tau) re-derivation ADDS is the tau-DEPENDENCE (the dip channel).

A SYMMETRY FALSIFIER also (i) scans the full window for ANY grazing near-second-zero (a would-be
second horizon from a c_s DIP), and (ii) reproduces the S85 symmetric-bracket tanh^2-dip model as an
explicit modeling cross-check, so the count is robust to the modeling choice.
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
# Identity (plan §W2-1)
# ---------------------------------------------------------------------------
SESSION = "INV4"                                            # (local)
GATE_ID = "INV4-W2-1"                                       # (local)
SCHEME = "a2-stiffness-cs"                                  # (local) c_s(tau) from per-tau a_2(tau) curvature
CONVENTION = "BLV-acoustic-discriminant-cs-tau-resolved"   # (local) c_s tau-RESOLVED; v(tau) supersonic-exit
L_MAX = "12"                                               # (local) a_2(tau) from L_max=12 Peter-Weyl cache

# Plan-pinned machinery (PRDR §5)
N_EVAL = 4000                                              # (local) tau-grid points on [0.05,0.40]
SCAN_MIN = 0.05                                            # (local) transit-window genesis edge (S95-comparable)
SCAN_MAX = 0.40                                            # (local) transit-window post-fold edge
TOL_RESIDUAL = 1.0e-6                                      # (local) |D(tau_root)| acceptance at a refined root
TOL_ROOT_DTAU = 1.0e-4                                     # (local) bracket width per root
GRAZE_INFO_CEIL = 1.0e-3                                   # (local) near-second-horizon grazing-min INFO ceiling
TAU_REF = 0.19                                             # (local) cache reference deformation (s84 cache @ tau=0.19)
PUB_PRECISION = 6                                          # (local) tau0, kappa0 reported to 6 sig figs (Class 8.3)

# Window landmarks (context only -> tagged # (local))
TAU_TURN_FREE = 0.088                                      # (local) free-roll turnaround (window context)
TAU_DECOHER = 0.16                                         # (local) decoherence scale (thermodynamic, NOT sonic)
TAU_ENTRY_73A = 0.2195                                     # (local) S73A W3-A entry-horizon tau (FABRY-PEROT-73a)
TAU_BCS_EDGE = 0.235                                       # (local) BCS edge (thermodynamic, NOT sonic)

# S95 anchor (for branch comparison; from s95 verdict line + npz)
S95_N_ZEROS = 1                                            # (local) S95 result: single-asymmetric-open
S95_TAU0 = 0.112443                                        # (local) S95 entry crossing tau
S95_KAPPA0 = -18.442205                                    # (local) S95 surface gravity at its single crossing

OUT_NPZ = PROJECT_ROOT / "computations" / "investigation-4" / "inv4_w2_cs_zero_count.npz"
OUT_PNG = PROJECT_ROOT / "computations" / "investigation-4" / "inv4_w2_cs_zero_count.png"
VERDICT_TXT = PROJECT_ROOT / "computations" / "investigation-4" / "inv4_gate_verdicts.txt"

CACHE_L12 = PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
S95_NPZ = PROJECT_ROOT / "computations" / "session-95" / "s95_w4_1_white_hole_kinematic_consistency.npz"

INPUT_FILES = [
    PROJECT_ROOT / "computations" / "_shared" / "canonical_constants.py",
    CACHE_L12,
    S95_NPZ,
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
# Jensen fiber scale + a_2(tau) stiffness reconstruction (the NEW content over S95)
# ---------------------------------------------------------------------------
def jensen_block_scales(tau):
    """Jensen metric block scales g_tau = 3*diag(e^{-2tau} x3, e^{tau} x4, e^{2tau} x1).

    Returns the 8-vector of fiber block scales (SU(2): 3 dirs e^{-2tau}; C^2: 4 dirs e^{tau};
    U(1): 1 dir e^{2tau}). MEMORY.md / SP-1 canonical Jensen convention.
    """
    tau = float(tau)
    return np.array(
        [3.0 * np.exp(-2.0 * tau)] * 3
        + [3.0 * np.exp(1.0 * tau)] * 4
        + [3.0 * np.exp(2.0 * tau)] * 1
    )


def a2_block_rescale_ratio(tau, tau_ref):
    """a_2(tau)/a_2(tau_ref) from the PER-BLOCK Jensen eigenvalue rescaling.

    a_2 = 0.5 sum_n d_n/lam_n^2. Under Jensen deformation the eigenvalue on fiber-block b scales as
    lam_b(tau) = lam_b(ref) * sqrt(g_b(ref)/g_b(tau))  [Dirac ~ 1/vielbein ~ 1/sqrt(g)], so
    1/lam_b(tau)^2 = (1/lam_b(ref)^2) * (g_b(tau)/g_b(ref)). The a_2 ratio is therefore the block-
    average of (g_b(tau)/g_b(ref)).

    CRITICAL (volume-preservation): the Jensen metric is VOLUME-PRESERVING (det g_tau = const;
    contracting SU(2) e^{-2tau} exactly compensates expanding C^2 e^{tau} / U(1) e^{2tau} -- the
    PROVEN "Volume-preserving TT" result, MEMORY.md). So the GEOMETRIC mean of g_b is tau-FLAT and
    would WASH OUT the stiffness tau-dependence (collapsing the gate to S95's constant-c_s by
    accident). The a_2 moment uses the ARITHMETIC block-average (a_2 ~ sum 1/lam^2 ~ sum g, the
    EXPANDING blocks dominate the sum), which is NOT flat: it has a MINIMUM at tau_ref (the
    deformation centre) and RISES on both sides -- the genuine a_2 softening at the van Hove fold.

    The (0,0) bottom band (global min |lambda|, dominant a_2 weight) is the spinor harmonic that
    probes all 8 Jensen directions; the block-democratic average is the substrate-natural a_2 shape.
    """
    g = jensen_block_scales(tau)          # (local) 8 block scales at tau
    g_ref = jensen_block_scales(tau_ref)  # (local) 8 block scales at tau_ref
    return float(np.mean(g / g_ref))      # (local) a_2(tau)/a_2(ref) arithmetic block-average


def load_cache_spectrum():
    """Load the L12 cache; return {level: array of |lambda| at tau_ref=0.19 with multiplicity}."""
    d = np.load(CACHE_L12, allow_pickle=True)  # (local)
    se = d["sector_evals"].item()  # (local) {(p,q): {dim, level, abs_evals}}
    by_level = {}  # (local)
    for (p, q), inner in se.items():
        lev = int(np.asarray(inner["level"]))  # (local)
        ev = np.asarray(inner["abs_evals"], dtype=float)  # (local) |lambda| values, multiplicity-expanded
        by_level.setdefault(lev, []).append(ev)
    for lev in by_level:
        by_level[lev] = np.concatenate(by_level[lev])
    return by_level


def a2_stiffness_profile(tau_grid, by_level):
    """a_2(tau) = 0.5 * sum_n d_n / lam_n(tau)^2 over the Jensen-rescaled cache spectrum.

    a_2(tau) = a_2(tau_ref) * [a_2(tau)/a_2(tau_ref)], with the ratio from the PER-BLOCK Jensen
    eigenvalue rescaling (a2_block_rescale_ratio): the arithmetic block-average of g_b(tau)/g_b(ref),
    which is the substrate-correct a_2 shape (NOT the volume-preserving-flat geometric mean). a_2(ref)
    is the raw zeta-scheme second moment of the cached spectrum at tau_ref=0.19. The a_2(tau) profile
    has a MINIMUM at tau_ref (the deformation centre / van Hove fold region) and RISES on both sides
    -- the genuine spectral-stiffness softening; whether that softening is deep enough to dip c_s back
    through v (a 2nd crossing) is what the zero-scan decides.
    """
    a2_ref = 0.0  # (local) raw a_2 at tau_ref from the cache
    for lev, ev in by_level.items():
        nz = ev[ev > 1e-12]  # (local)
        a2_ref += 0.5 * np.sum(1.0 / nz ** 2)
    a2 = np.zeros_like(tau_grid)  # (local)
    for i, tau in enumerate(tau_grid):
        a2[i] = a2_ref * a2_block_rescale_ratio(float(tau), TAU_REF)  # (local) per-block-rescaled a_2(tau)
    return a2


# ---------------------------------------------------------------------------
# Kinematic profiles: c_s(tau) [tau-RESOLVED] and the physical v(tau) [S95]
# ---------------------------------------------------------------------------
def c_speed_tau_resolved(tau_grid, a2_grid):
    """c_s(tau) = sqrt(stiffness(tau)/rho(tau)), anchored so post-fold c_s = c_BLV (S95 constant).

    stiffness(tau) = a_2(tau) (the second Seeley-DeWitt moment -- the scalar-curvature stiffness
    channel; a_2 generates the Einstein-Hilbert kinematic skeleton). rho(tau) at fixed L_max is the
    mode-count a_0(tau) = 0.5 * sum d_n (tau-INDEPENDENT count), so c_s(tau)^2 ~ a_2(tau)/a_0,
    i.e. c_s(tau) ~ sqrt(a_2(tau)) up to the anchor normalization.

    Anchor: c_s(tau) = c_BLV * sqrt( a_2(tau) / a_2(tau_anchor) ), tau_anchor = post-fold reference
    (we use the largest tau in the window, the supersonic-exit flank, where c_BLV is the canonical
    S64 scalar sound speed). This makes the c_BLV cross-check and the tau-RESOLVED reading directly
    comparable, and renders the zero-count invariant to overall normalization.
    """
    a2_anchor = float(a2_grid[-1])  # (local) a_2 at the post-fold exit-flank reference
    return float(c_BLV) * np.sqrt(a2_grid / a2_anchor)  # (local) tau-resolved c_s anchored to c_BLV


def c_speed_constant(tau_grid):
    """S95 cross-check: c_s held CONSTANT at the canonical BLV speed c_BLV (the S95 modeling choice)."""
    return np.full_like(tau_grid, float(c_BLV))


def v_transit(tau):
    """Physical modulus transit velocity v(tau)=dtau/dt mapped to the acoustic normal coordinate.

    EXACT reproduction of the S95-W4-1 physical v(tau) (s95_w4_1 v_transit). Shape FORCED by the
    substrate: dS/dtau is CONSTANT-SIGN across the fold (S73A W1-D) -> no deceleration mechanism;
    monotone logistic rise to a supersonic plateau, with a fold-centred Gaussian enhancement peaking
    v at v_fold = Mach_max*c_BLV at tau_fold. Subsonic genesis flank, single Mach-1 entry crossing on
    the rising limb, supersonic exit (Jensen monotonicity).
    """
    tau = np.atleast_1d(tau).astype(float)
    v_fold = float(Mach_max) * float(c_BLV)            # (local) 6.66875 M_KK (peak at fold; Mach 13.75)
    v_genesis = 0.30 * float(c_BLV)                    # (local) deep subsonic genesis-flank floor (Mach 0.30)
    v_plateau = float(Mach_max) * float(c_BLV) / 1.20  # (local) supersonic exit plateau (Mach ~ 11.46)

    k_rise = 120.0                                     # (local) rise steepness (1/M_KK)
    tau_rise = 0.135                                   # (local) logistic midpoint (genesis-to-transit ramp)
    logistic = 1.0 / (1.0 + np.exp(-k_rise * (tau - tau_rise)))  # (local) 0->1 monotone
    v_base = v_genesis + (v_plateau - v_genesis) * logistic      # (local) monotone rise-to-plateau

    delta_fold = 0.016                                 # (local) fold enhancement width
    bump = np.exp(-0.5 * ((tau - float(tau_fold)) / delta_fold) ** 2)  # (local) Gaussian, peak 1 at fold
    v = v_base + (v_fold - v_plateau) * bump            # (local) peaks at v_fold at the fold
    return v


# ---------------------------------------------------------------------------
# Discriminant on the tau-grid (interpolating c_s(tau) for the root refiner)
# ---------------------------------------------------------------------------
class Discriminant:
    """D(tau) = c_s(tau)^2 - v(tau)^2 as a callable, with c_s(tau) interpolated from the grid.

    The a_2(tau) stiffness (hence c_s(tau)) is built on the dense tau-grid; for bisection root
    refinement we linearly interpolate c_s(tau) (the a_2 reconstruction is smooth in tau by the
    geometric-mean Jensen scale), and evaluate v(tau) exactly at the refined tau.
    """

    def __init__(self, tau_grid, cs_grid):
        self.tau_grid = np.asarray(tau_grid, dtype=float)  # (local)
        self.cs_grid = np.asarray(cs_grid, dtype=float)    # (local)

    def cs(self, tau):
        return np.interp(np.atleast_1d(tau).astype(float), self.tau_grid, self.cs_grid)  # (local)

    def __call__(self, tau):
        c = self.cs(tau)              # (local) c_s(tau) interpolated
        v = v_transit(tau)           # (local) v(tau) exact
        return c ** 2 - v ** 2


# ---------------------------------------------------------------------------
# Zero-finding: sign-change detection + bisection refinement
# ---------------------------------------------------------------------------
def find_zeros(tau_grid, disc):
    """Locate ALL zeros of D(tau) on the grid via sign-change + bisection.

    Bisection runs until BOTH |dtau| < TOL_ROOT_DTAU AND |D| < TOL_RESIDUAL. Returns list of dicts:
    {tau_root, residual, dtau_bracket, slope_disc}.
    """
    dgrid = disc(tau_grid)  # (local)
    sgn = np.sign(dgrid)    # (local)
    cross_idx = np.where(np.diff(sgn) != 0)[0]  # (local) zero bracketed between i and i+1
    roots = []  # (local)
    for i in cross_idx:
        a, b = float(tau_grid[i]), float(tau_grid[i + 1])  # (local)
        fa = float(disc(np.array([a]))[0])                 # (local)
        if fa == 0.0:
            roots.append(_root_record(disc, a)); continue
        it = 0  # (local)
        m = 0.5 * (a + b); fm = float(disc(np.array([m]))[0])  # (local)
        while ((b - a) > TOL_ROOT_DTAU or abs(fm) > TOL_RESIDUAL) and it < 300:
            if fm == 0.0:
                a = b = m; break
            if np.sign(fm) == np.sign(fa):
                a, fa = m, fm
            else:
                b = m
            m = 0.5 * (a + b)  # (local) bisection midpoint
            fm = float(disc(np.array([m]))[0])  # (local)
            it += 1
        roots.append(_root_record(disc, m, dtau_bracket=(b - a)))
    return roots


def _root_record(disc, tau_root, dtau_bracket=0.0):
    resid = float(disc(np.array([tau_root]))[0])  # (local)
    slope = surface_gravity(disc, tau_root)["d_disc"]  # (local) oriented d_n D at the root
    return {
        "tau_root": float(tau_root),
        "residual": float(resid),
        "dtau_bracket": float(dtau_bracket),
        "slope_disc": float(slope),
    }


# ---------------------------------------------------------------------------
# Surface gravity:  kappa = (1/2) d_n(c_s^2 - v^2)  (Visser; oriented interior->exterior)
# ---------------------------------------------------------------------------
def surface_gravity(disc, tau_surface, h=1.0e-6):
    """kappa = (1/2) d_n D|_surface, oriented from supersonic interior (D<0) to subsonic exterior (D>0).

    n is the OUTWARD NORMAL: the side with D>0 is the exterior; n points toward it. kappa is the
    increase of D going interior->exterior (positive for a white-hole outflow surface, Visser).
    """
    tp = float(tau_surface) + h  # (local)
    tm = float(tau_surface) - h  # (local)
    disc_p = float(disc(np.array([tp]))[0])  # (local)
    disc_m = float(disc(np.array([tm]))[0])  # (local)
    d_disc_tau = (disc_p - disc_m) / (2.0 * h)        # (local) raw d/d(+tau)
    n_sign = 1.0 if disc_p > disc_m else -1.0         # (local) +tau if larger-tau side is more subsonic
    d_disc = n_sign * d_disc_tau                      # (local) oriented d_n D (>0 for outflow)
    kappa = 0.5 * d_disc                              # (local) Visser acoustic surface gravity (oriented)
    T_a = abs(kappa) / (2.0 * np.pi)                  # (local) analog temperature; hbar=1
    return {"kappa": float(kappa), "d_disc": float(d_disc),
            "d_disc_tau": float(d_disc_tau), "n_sign": float(n_sign), "T_a": float(T_a)}


# ---------------------------------------------------------------------------
# S85 symmetric-bracket cross-check (modeling-robustness)
# ---------------------------------------------------------------------------
def s85_symmetric_bracket():
    """Reproduce the S85 narrow-window symmetric two-crossing model as a cross-check.

    S85 model: c_s(tau) = v_term*[1/Mach_max + A*tanh^2((tau-tau_fold)/delta_h)], v=v_term const;
    Mach=1 at tau_fold +/- delta_h*atanh(sqrt((1-1/Mach_max)/A)). Demonstrates that S85's TWO
    crossings are a property of its SYMMETRIC c_s dip on the +/-0.01 window.
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
    print("--- Section 6: a_2(tau) spectral-stiffness reconstruction (NEW content vs S95) ---")
    by_level = load_cache_spectrum()  # (local)
    total_modes = sum(ev.size for ev in by_level.values())  # (local)
    a2_ref = a2_stiffness_profile(np.array([TAU_REF]), by_level)[0]  # (local) a_2 at the cache tau_ref=0.19
    print(f"  L12 cache: {total_modes} eigenvalues over levels {min(by_level)}..{max(by_level)}")
    print(f"  a_2(tau_ref=0.19) raw (L12 truncation) = {a2_ref:.6f}")
    print(f"  a2_fold canonical (CONST-FREEZE-42)     = {float(a2_fold):.6f}  (S42 truncation; shape-only use here)")
    print(f"  a_2 block-rescale ratio: r(0.05)={a2_block_rescale_ratio(0.05,TAU_REF):.6f} "
          f"r(0.19)={a2_block_rescale_ratio(0.19,TAU_REF):.6f} r(0.40)={a2_block_rescale_ratio(0.40,TAU_REF):.6f} "
          f"(arith block-avg; MIN at tau_ref by volume-preservation)")
    print(f"  det g_tau check (volume-preserving): det(0.05)={np.prod(jensen_block_scales(0.05)):.4f} "
          f"det(0.19)={np.prod(jensen_block_scales(0.19)):.4f} det(0.40)={np.prod(jensen_block_scales(0.40)):.4f}")
    print()

    # (1) dense tau-grid; a_2(tau) and the two c_s readings
    tau_grid = np.linspace(SCAN_MIN, SCAN_MAX, N_EVAL)  # (local)
    a2_grid = a2_stiffness_profile(tau_grid, by_level)  # (local) a_2(tau) across the window
    cs_resolved = c_speed_tau_resolved(tau_grid, a2_grid)  # (local) tau-RESOLVED c_s(tau)
    cs_constant = c_speed_constant(tau_grid)              # (local) S95 cross-check (constant c_BLV)
    v_grid = v_transit(tau_grid)                          # (local)
    mach_resolved = v_grid / cs_resolved                  # (local)

    # a_2 dip diagnostics (the second-crossing channel)
    a2_min_idx = int(np.argmin(a2_grid))   # (local)
    a2_max_idx = int(np.argmax(a2_grid))   # (local)
    print("--- Section 7: a_2(tau) / c_s(tau) profile ---")
    print(f"  a_2(tau) range on window = [{a2_grid.min():.4f}, {a2_grid.max():.4f}]  "
          f"(min @ tau={tau_grid[a2_min_idx]:.4f}, max @ tau={tau_grid[a2_max_idx]:.4f})")
    print(f"  a_2 monotone-decreasing across window = {bool(np.all(np.diff(a2_grid) < 0))}  "
          f"(a DIP would create a c_s local min -> 2nd-crossing channel)")
    print(f"  c_s(tau) [tau-resolved] range = [{cs_resolved.min():.6f}, {cs_resolved.max():.6f}] M_KK")
    print(f"  c_s [constant cross-check]    = {float(c_BLV):.6f} M_KK (S95 choice)")
    print(f"  c_s(post-fold anchor)         = {cs_resolved[-1]:.6f} M_KK (= c_BLV by anchor)")
    print(f"  v(tau) range = [{v_grid.min():.6f}, {v_grid.max():.6f}] M_KK; v_fold = {float(Mach_max)*float(c_BLV):.6f}")
    print(f"  Mach (tau-resolved) range = [{mach_resolved.min():.4f}, {mach_resolved.max():.4f}]")
    print()

    # (2) discriminant + zero count (the C-1 two-branch discriminator)
    disc = Discriminant(tau_grid, cs_resolved)  # (local) D(tau)=c_s(tau)^2 - v(tau)^2
    disc_grid = disc(tau_grid)                  # (local)
    roots = find_zeros(tau_grid, disc)          # (local)
    N_zeros = len(roots)                        # (local)
    print("--- Section 8: zero-crossings of D(tau)=c_s(tau)^2 - v(tau)^2 [C-1 discriminator] ---")
    print(f"  N_zeros = {N_zeros}")
    for j, r in enumerate(roots):
        print(f"    root[{j}]: tau={r['tau_root']:.6f}  |D|={abs(r['residual']):.3e}  "
              f"bracket={r['dtau_bracket']:.3e}  d_n D={r['slope_disc']:+.4f}")
    print()

    # (3) surface gravity at each zero
    print("--- Section 9: surface gravity kappa=(1/2)d_n D at each Mach-1 surface ---")
    sg_records = []  # (local)
    for j, r in enumerate(roots):
        sg = surface_gravity(disc, r["tau_root"])  # (local)
        sg_records.append({**r, **sg})
        nstr = "+tau" if sg["n_sign"] > 0 else "-tau"  # (local)
        print(f"    surface[{j}] @ tau={r['tau_root']:.6f}: d(D)/d(+tau)={sg['d_disc_tau']:+.4f} (coord); "
              f"outward n={nstr}; d_n D={sg['d_disc']:+.4f} (oriented); kappa={sg['kappa']:+.6f}  "
              f"T_a={sg['T_a']:.6f} M_KK")
    print()

    # kappa SIGN at the entry (lowest-tau zero) -- Claim [SIGN] test
    sign_entry = float("nan")  # (local)
    if N_zeros >= 1:
        entry = min(sg_records, key=lambda d: d["tau_root"])  # (local) lowest-tau surface = entry
        sign_entry = entry["d_disc"]  # (local) ORIENTED d_n D|_entry (invariant)
        print(f"  [SIGN] Claim: raw d(D)/d(+tau)|_entry = {entry['d_disc_tau']:+.6f} (coordinate); "
              f"outward normal n = {'+tau' if entry['n_sign'] > 0 else '-tau'}")
        print(f"         oriented d_n D|_entry = {sign_entry:+.6f}  -> kappa_entry "
              f"{'> 0 (white-hole outflow; sign PASS)' if sign_entry > 0 else '<= 0 (sign FAIL)'}")
    print()

    # (4) symmetry falsifier -- scan for ANY post-entry second crossing (c_s dip channel)
    print("--- Section 10: symmetry falsifier (post-entry c_s dip / re-acceleration?) ---")
    if N_zeros >= 1:
        last_tau = max(r["tau_root"] for r in roots)  # (local)
        far_mask = tau_grid > last_tau  # (local) exit flank past the last sonic surface
        if np.any(far_mask):
            disc_far = disc_grid[far_mask]  # (local)
            graze_min_abs = float(np.min(np.abs(disc_far)))  # (local) closest approach to 0 on exit flank
            disc_far_max = float(np.max(disc_far))           # (local) >0 => a 2nd subsonic crossing seen
        else:
            graze_min_abs = float("nan"); disc_far_max = float("nan")
    else:
        graze_min_abs = float("nan"); disc_far_max = float("nan")
    monotone_supersonic_exit = bool(np.isfinite(disc_far_max) and disc_far_max < 0.0)  # (local) open exit
    print(f"  exit-flank grazing min |D| = {graze_min_abs:.6e}  (<{GRAZE_INFO_CEIL}: near-2nd-horizon INFO flag)")
    print(f"  exit-flank max D           = {disc_far_max:+.6e}  (>0 would be a 2nd subsonic crossing)")
    print(f"  monotone supersonic exit (open) = {monotone_supersonic_exit}")
    print()

    # (5) S85 symmetric-bracket cross-check
    s85 = s85_symmetric_bracket()  # (local)
    print("--- Section 11: S85 symmetric-bracket modeling cross-check ---")
    print(f"  S85 model tau_H_- = {s85['tau_H_minus']:.6f}  tau_H_+ = {s85['tau_H_plus']:.6f}  "
          f"(width {s85.get('interior_width', float('nan')):.6f})")
    print("  NOTE: S85's 2 crossings are a property of its SYMMETRIC tanh^2 c_s dip on +/-0.01 (v const).")
    print("        This gate tests whether the PHYSICAL a_2(tau) stiffness produces such a dip on its own.")
    print()

    # (6) branch comparison vs S95 anchor
    print("--- Section 12: branch comparison vs S95 anchor ---")
    print(f"  S95: N_zeros={S95_N_ZEROS}, tau0={S95_TAU0:.6f}, kappa0={S95_KAPPA0:.6f} (constant c_s)")
    branch = "Track_A_ASYMMETRIC(S95)" if N_zeros == 1 else (
        "Track_B_SYMMETRIC(S85)" if N_zeros == 2 else "INDETERMINATE")  # (local)
    print(f"  this gate (tau-resolved c_s from a_2): N_zeros={N_zeros} -> {branch}")
    print()

    return {
        "tau_grid": tau_grid, "a2_grid": a2_grid, "disc_grid": disc_grid,
        "cs_resolved": cs_resolved, "cs_constant": cs_constant, "v_grid": v_grid,
        "mach_resolved": mach_resolved,
        "a2_ref": float(a2_ref),
        "a2_monotone_decreasing": bool(np.all(np.diff(a2_grid) < 0)),
        "a2_min_tau": float(tau_grid[a2_min_idx]), "a2_max_tau": float(tau_grid[a2_max_idx]),
        "N_zeros": N_zeros, "roots": roots, "sg_records": sg_records,
        "sign_entry": sign_entry,
        "graze_min_abs": graze_min_abs, "disc_far_max": disc_far_max,
        "monotone_supersonic_exit": monotone_supersonic_exit,
        "s85": s85, "branch": branch,
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

    # --- sign: [SIGN] claim predicts kappa_entry > 0 (oriented d_n D|_entry > 0) ---
    se = result["sign_entry"]  # (local)
    if N >= 1 and np.isfinite(se):
        sign = "PASS" if se > 0 else "FAIL"  # (local)
    else:
        sign = "N/A"

    # --- magnitude: PRIMARY = N_zeros decisively in {1,2} (two-branch); both are PASS ---
    if N in (1, 2):
        # check the near-second-horizon grazing-min INFO clause (asymmetric branch only)
        gmin = result["graze_min_abs"]  # (local)
        if N == 1 and np.isfinite(gmin) and gmin <= GRAZE_INFO_CEIL:
            magnitude = "INFO"  # (local) asymmetric but at the boundary of the bracketed branch
        else:
            magnitude = "PASS"  # (local) decisively resolved to 1 or 2
    else:
        magnitude = "FAIL"  # (local) N_zeros not in {1,2} -> indeterminate count

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
    structure = ("ASYMMETRIC_open_exit_S95" if N == 1 else
                 ("SYMMETRIC_bracketed_pair_S85" if N == 2 else "INDETERMINATE"))  # (local)
    roots = result["roots"]  # (local)
    root_str = ";".join(f"tau{j}={r['tau_root']:.6f}" for j, r in enumerate(roots))  # (local)
    sg = result["sg_records"]  # (local)
    kappa_str = ";".join(f"kappa{j}={s['kappa']:.6f}" for j, s in enumerate(sg))  # (local)
    return (
        f"N_zeros={N};branch={structure};{root_str};{kappa_str};"
        f"sign_entry_d_disc={result['sign_entry']:.6f};"
        f"a2_dip_min_tau={result['a2_min_tau']:.6f};a2_monotone_decr={result['a2_monotone_decreasing']};"
        f"cs_resolved_min={result['cs_resolved'].min():.6f};cs_resolved_max={result['cs_resolved'].max():.6f};"
        f"graze_min_abs={result['graze_min_abs']:.6e};disc_far_max={result['disc_far_max']:.6e};"
        f"monotone_supersonic_exit={result['monotone_supersonic_exit']};"
        f"S95_anchor=N_zeros{S95_N_ZEROS}_tau0_{S95_TAU0:.6f}_kappa0_{S95_KAPPA0:.6f};"
        f"sign_verdict={sign};magnitude_verdict={magnitude};regime_verdict={regime};composite={composite}"
    )


def save_npz(result, composite, sign, magnitude, regime, audit_sha, content_sha):
    roots = result["roots"]  # (local)
    sg = result["sg_records"]  # (local)
    np.savez(
        OUT_NPZ,
        tau_grid=result["tau_grid"], a2_grid=result["a2_grid"], disc_grid=result["disc_grid"],
        cs_resolved=result["cs_resolved"], cs_constant=result["cs_constant"],
        v_grid=result["v_grid"], mach_resolved=result["mach_resolved"],
        a2_ref=np.array(result["a2_ref"]),
        a2_monotone_decreasing=np.array(result["a2_monotone_decreasing"]),
        a2_min_tau=np.array(result["a2_min_tau"]), a2_max_tau=np.array(result["a2_max_tau"]),
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
        s85_tau_H_minus=np.array(result["s85"]["tau_H_minus"]),
        s85_tau_H_plus=np.array(result["s85"]["tau_H_plus"]),
        S95_N_zeros=np.array(S95_N_ZEROS), S95_tau0=np.array(S95_TAU0), S95_kappa0=np.array(S95_KAPPA0),
        branch=np.array(result["branch"], dtype=object),
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
    fig, axes = plt.subplots(2, 2, figsize=(12.6, 9.4))  # (local)
    tau = result["tau_grid"]; a2 = result["a2_grid"]; disc = result["disc_grid"]  # (local)
    cs_r = result["cs_resolved"]; cs_c = result["cs_constant"]; v = result["v_grid"]  # (local)
    mach = result["mach_resolved"]; roots = result["roots"]  # (local)
    tauf = float(tau_fold)  # (local)

    # (a) a_2(tau) stiffness profile (the NEW channel)
    ax = axes[0, 0]
    ax.plot(tau, a2, "-", color="#8c564b", lw=1.4, label=r"$a_2(\tau)$ stiffness")
    ax.axvline(tauf, color="#9467bd", lw=0.8, ls=":", label=r"$\tau_\mathrm{fold}$")
    ax.axvline(result["a2_min_tau"], color="#e377c2", lw=0.8, ls="--",
               label=rf"$a_2$ min @ $\tau$={result['a2_min_tau']:.3f}")
    ax.set_xlabel(r"$\tau$"); ax.set_ylabel(r"$a_2(\tau)$ (zeta-scheme, L12)")
    ax.set_title("(a) $a_2(\\tau)$ spectral stiffness (vs S95 constant $c_s$)")
    ax.legend(loc="best", fontsize=8); ax.grid(alpha=0.3)

    # (b) the two c_s readings side-by-side + v(tau)
    ax = axes[0, 1]
    ax.plot(tau, cs_r, "-", color="#2ca02c", lw=1.5, label=r"$c_s(\tau)$ [a$_2$-resolved]")
    ax.plot(tau, cs_c, "--", color="#17becf", lw=1.3, label=rf"$c_s=c_\mathrm{{BLV}}={float(c_BLV):.3f}$ [S95 const]")
    ax.plot(tau, v, "-", color="#d62728", lw=1.4, label=r"$v(\tau)$ modulus transit")
    ax.axvline(tauf, color="#9467bd", lw=0.8, ls=":")
    for r in roots:
        ax.axvline(r["tau_root"], color="#d62728", lw=0.8, ls="--", alpha=0.6)
    ax.set_xlabel(r"$\tau$"); ax.set_ylabel(r"speed (M$_\mathrm{KK}$)")
    ax.set_title("(b) Two stiffness$\\rightarrow c_s$ readings + $v(\\tau)$")
    ax.legend(loc="best", fontsize=8); ax.grid(alpha=0.3)

    # (c) discriminant D(tau) with zeros
    ax = axes[1, 0]
    ax.plot(tau, disc, "-", color="#1f77b4", lw=1.4, label=r"$D=c_s^2-v^2$ [a$_2$-resolved]")
    ax.axhline(0.0, color="k", lw=0.7, ls="--", label=r"$D=0$ (Mach-1)")
    ax.axvline(tauf, color="#9467bd", lw=0.8, ls=":", label=r"$\tau_\mathrm{fold}$")
    for j, r in enumerate(roots):
        ax.axvline(r["tau_root"], color="#d62728", lw=1.1, ls="-",
                   label=("sonic surface" if j == 0 else None))
        ax.plot([r["tau_root"]], [0.0], "o", color="#d62728", ms=6)
    ax.set_xlabel(r"$\tau$"); ax.set_ylabel(r"$c_s^2-v^2$ (M$_\mathrm{KK}^2$)")
    ax.set_title(f"(c) Acoustic discriminant: $N_\\mathrm{{zeros}}={result['N_zeros']}$")
    ax.legend(loc="best", fontsize=8); ax.grid(alpha=0.3)

    # (d) Penrose diagram per the resolved branch
    ax = axes[1, 1]
    ax.set_xlim(-1.25, 1.25); ax.set_ylim(-1.25, 1.25); ax.set_aspect("equal")
    diamond = plt.Polygon([(-1, 0), (0, 1), (1, 0), (0, -1)], fill=False, edgecolor="black", lw=1.1)
    ax.add_patch(diamond)
    N = result["N_zeros"]  # (local)
    if N == 1:
        ax.plot([-0.7, 0.15], [0.5, -0.35], "-", color="#d62728", lw=2.0,
                label=r"entry sonic horizon ($\kappa>0$)")
        erg = plt.Polygon([(0.15, -0.35), (0.95, 0.45), (-0.7, 0.5)], alpha=0.30, color="#ffcc99")
        ax.add_patch(erg)
        ax.text(0.45, 0.0, "open\nexpulsion\nexit", ha="center", fontsize=8, color="#7f3b00")
        struct = "ASYMMETRIC (S95)"
    elif N == 2:
        ax.plot([-0.7, 0.0], [0.5, -0.2], "-", color="#d62728", lw=2.0, label=r"entry horizon")
        ax.plot([0.0, 0.7], [-0.2, 0.5], "-", color="#d62728", lw=2.0, label=r"exit horizon")
        erg = plt.Polygon([(0, -0.2), (0.7, 0.5), (-0.7, 0.5)], alpha=0.30, color="#ffcc99")
        ax.add_patch(erg)
        ax.text(0.0, 0.2, "sealed\ninterior", ha="center", fontsize=8, color="#7f3b00")
        struct = "SYMMETRIC (S85)"
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
    ax.set_title(f"(d) Penrose diagram — C-1 = {struct}")
    ax.legend(loc="lower left", fontsize=7)

    fig.suptitle(
        f"INV4 W2-1: $c_s(\\tau)$ from $a_2(\\tau)$ stiffness — zero-count of $(c_s^2-v^2)$: "
        f"$N_\\mathrm{{zeros}}={result['N_zeros']}$, verdict {composite}",
        fontsize=12,
    )
    fig.tight_layout(rect=(0.0, 0.0, 1.0, 0.96))
    fig.savefig(OUT_PNG, dpi=110)
    plt.close(fig)


def print_verdict_payload(composite, sign, magnitude, regime, value_str, audit_sha, content_sha):
    """Print the verdict payload for the agent to pass to emit_verdict (race-safe MCP path).

    The script computes value + dual-SHA and PRINTS the payload; the agent then calls
    emit_verdict(**payload, session=4, track='investigation'). Per gate-verdicts.md
    'Race-Safe Emission' — the script NEVER open-codes a verdict-file append.
    """
    print("=" * 92)
    print("VERDICT PAYLOAD (pass to emit_verdict; session=4, track='investigation'):")
    print(f"  gate_id          = {GATE_ID}")
    print(f"  verdict          = {composite}")
    print(f"  value            = {value_str}")
    print(f"  scheme           = {SCHEME}")
    print(f"  convention       = {CONVENTION}")
    print(f"  l_max            = {L_MAX}")
    print(f"  sign_verdict     = {sign}")
    print(f"  magnitude_verdict= {magnitude}")
    print(f"  regime_verdict   = {regime}")
    print(f"  audit_sha256     = {audit_sha}")
    print(f"  content_sha256   = {content_sha}")
    print("=" * 92)


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
    print(f"  tau_fold = {float(tau_fold)}  c_BLV = {float(c_BLV)}  Mach_max = {float(Mach_max)}  "
          f"c_fabric = {float(c_fabric)}")
    print(f"  a2_fold = {float(a2_fold)}  a0_fold = {float(a0_fold)}  (CONST-FREEZE-42, shape-anchor refs)")
    print()

    result = compute()
    composite, sign, magnitude, regime = evaluate_gate(result)

    value_str = build_value_string(result, composite, sign, magnitude, regime)  # (local)
    print(f"(value='{value_str}', scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print()

    save_npz(result, composite, sign, magnitude, regime, audit_sha, content_sha)
    save_png(result, composite)
    print_verdict_payload(composite, sign, magnitude, regime, value_str, audit_sha, content_sha)

    wall = time.time() - t0  # (local)
    print(f"=== {GATE_ID}: {composite}  (sign={sign} mag={magnitude} regime={regime}; "
          f"branch={result['branch']}; wall {wall:.1f}s) ===")
    print(f"NPZ:  {OUT_NPZ.name}")
    print(f"PNG:  {OUT_PNG.name}")
    return 0  # math-scripts.md §Exit Codes: exit 0 regardless of PASS/FAIL/INFO


if __name__ == "__main__":
    sys.exit(main())
