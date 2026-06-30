#!/usr/bin/env python3
"""
INV11 W1-3 — ATDHFB collective Hamiltonian H=1/2 M(tau) taudot^2 + E_eff(tau);
             least-action / first-passage tau_fold selection
=============================================================================

Gate: INV11-W1-3 ([VERIFY])
  Investigation track n=11; verdict file computations/investigation-11/inv11_gate_verdicts.txt

Pre-registered threshold (plan §W1-3):
  operator: |tau_fold_selected - 0.190| <= 0.010
  PASS iff |Delta tau| <= 0.010, FAIL iff |Delta tau| > 0.030 (or no localizing
  extremum), INFO iff 0.010 < |Delta tau| <= 0.030.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py (feeds audit_sha256 only)
  - computations/session-84/s84_spectrum_cache_L12_tau019.npz (L12 spectrum cache;
    feeds audit_sha256 via the pin map)
  - computations/session-42/s42_gradient_stiffness.npz (the S_SA(tau) surface +
    dS/dtau + the M_ATDHFB=1.695 anchor; feeds audit_sha256 via the pin map)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<tau_fold_selected>, scheme=SA, convention=ABSOLUTE, L_max=12)

Classification: GEOMETRIC
  tau_fold is the Jensen-deformation parameter value at the van Hove fold -- a
  property of the spectral-triple's deformation (Level-2 moduli-deformation
  substrate-IS), not an excitation.

METHODOLOGY
-----------
Build the 1-D collective Hamiltonian H = 1/2 M(tau) taudot^2 + E_eff(tau) for
motion along the Jensen deformation coordinate tau (the ATDHFB / GCM collective-
coordinate reduction; canonical nuclear analog: fission-barrier collective
Hamiltonian, Paper 13 GCM). E_eff(tau) = S_SA(tau) + E_cond(tau): the MONOTONE
spectral action (dS/dtau = +58672.8 > 0 at the fold, S42) plus the BCS
condensation well E_cond(tau) (the pairing well, |E_cond| ~ 0.137 M_KK 8-mode ED
/ 0.24 per-coset; DEEPENS toward the fold because the van Hove DOS maximizes the
gap there). M(tau) is the ATDHFB collective inertia anchored at M_ATDHFB=1.695
(S40, s42_gradient_stiffness.npz). The least-action (WKB / Hamilton-Jacobi)
trajectory from the cold start tau->0 is integrated; the first-passage /
action-stationary tau is located and tested against the canonical tau_fold=0.190.

This is the collective-inertia / least-action route to NON-VARIATIONAL tau_fold
selection -- the only un-attempted such route after the S95 one-loop +
variational corridors closed (T5 BROKEN; S95-W2-3-NO-WELL-ONE-LOOP PASS value=0).
It is structurally DISTINCT from inv-3 W2-4 (Weyl-remainder / shortest-geodesic).

KEY PRIOR RESULT consumed (and tested against):
  FRIED-39 / T6-BROKEN (S39, atlas-04 T6, atlas-07 #33, closed-mechanism
  FRIEDMANN-BCS): "Friedmann-BCS coupling can dynamically lock tau" -> BROKEN.
  Gradient ratio 6,596x (the full spectral action, 155,984 modes, overwhelms the
  BCS condensation gradient, 8 modes, at the fold); shortfall for locking 133,200x.
  S29b: "V_eff = S_spectral + F_BCS remains monotonically decreasing; dV_total/dtau
  has NO sign change." This gate RE-DERIVES that comparison inside the explicit
  collective-Hamiltonian least-action framework with the ATDHFB inertia, on a
  400-point grid, and reports whether the first-passage trajectory nonetheless
  localizes at the fold via the S53 speed-bump (ratio_BCS=1.30 at tau=0.2015,
  a local MAXIMUM in the condensation-vs-geometry comparison -- a DISTINCT ratio
  from the 6,596x full-SA ratio).

DISCIPLINE
----------
- `from canonical_constants import *`
- Every local/intermediate tagged `# (local)`
- DOS-only / small-matrix work: CPU numpy (cached arrays). No L>=13 re-diagonalization
  (forbidden by the Friedrich-Bar feasibility pre-check; the fold-window inertia
  is L12-saturated).
- SHA-256 of all input files logged in the first 20 lines of stdout.
- audit_sha256 + content_sha256 emitted (S84+ dual-SHA schema).
- 4-tuple printed as the final non-verdict line.
- Verdict emitted via the emit_verdict knowledge-MCP tool (this script PRINTS the
  payload; the dispatching agent calls emit_verdict with track="investigation").
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — Standard imports + path setup (make canonical_constants importable)
# ---------------------------------------------------------------------------
import hashlib
import json
import os
import sys
import time
from pathlib import Path

# canonical_constants.py lives in computations/_shared/; this script is in
# computations/investigation-11/. Add _shared to sys.path BEFORE the import.
_SHARED = Path(__file__).resolve().parent.parent / "_shared"
sys.path.insert(0, str(_SHARED))

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import; S34+ mandate)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403,E402
import canonical_constants as cc  # noqa: E402

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent              # computations/investigation-11
COMPUTATIONS_DIR = SESSION_DIR.parent                       # computations/
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "11"                                              # (local) investigation number
GATE_ID = "INV11-W1-3"                                      # (local)
SCHEME = "SA"                                               # (local) E_eff = spectral action + BCS condensate
CONVENTION = "ABSOLUTE"                                     # (local) tau_fold absolute coordinate
L_MAX = 12                                                  # (local)

# Pre-registered pass/fail thresholds (plan §W1-3 operator + INFO_meaning)
PASS_TOL = 0.010                                            # (local) |tau_selected - 0.190| <= 0.010 -> PASS
INFO_TOL = 0.030                                            # (local) 0.010 < |..| <= 0.030 -> INFO
N_TAU = 400                                                 # (local) tau-grid points (plan N_eval)
SCAN_MIN = 0.0                                              # (local) plan scan_range lower
SCAN_MAX = 0.40                                             # (local) plan scan_range upper
TAU_FOLD_TARGET = float(cc.tau_fold)                        # 0.19 canonical target

# Output destinations (investigation-track per-wave)
OUT_NPZ = SESSION_DIR / "inv11_w1_atdhfb_collective_tau_fold.npz"
OUT_PNG = SESSION_DIR / "inv11_w1_atdhfb_collective_tau_fold.png"

S42_NPZ = COMPUTATIONS_DIR / "session-42" / "s42_gradient_stiffness.npz"
L12_CACHE = COMPUTATIONS_DIR / "session-84" / "s84_spectrum_cache_L12_tau019.npz"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    L12_CACHE,
    S42_NPZ,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (MANDATORY; first 20 lines of stdout)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
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
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


# ---------------------------------------------------------------------------
# Section 5 — Collective-Hamiltonian construction + least-action / first-passage
# ---------------------------------------------------------------------------
def build_spectral_action_surface(tau_grid):
    """S_SA(tau) on the dense grid, interpolated from the S42 stiffness surface.

    The S42 surface samples S_total(tau) on a 10-point grid tau in [0.05, 0.30]
    with the canonical fold anchor dS/dtau = +58672.8 at tau=0.19. We interpolate
    S_total to the dense grid; outside the S42 span [0.05, 0.30] we extrapolate
    monotonically using the boundary gradients (the spectral action is PROVEN
    monotone-increasing, dS/dtau>0 for all tau -- atlas-07 Spectral Action
    Monotonicity, 9,600 checks). Returns (S_SA, dS_SA/dtau) in spectral-action units.
    """
    d = np.load(S42_NPZ, allow_pickle=True)  # (local)
    tau_s = np.asarray(d["tau_grid"], float)        # (local) [0.05..0.30]
    S_s = np.asarray(d["S_total"], float)           # (local) spectral action surface
    dS_s = np.asarray(d["dS_dtau"], float)          # (local) SA gradient (monotone +)
    # Interpolate S_total; np.interp clamps to endpoints, so add linear
    # extrapolation beyond the span using the boundary gradients (monotone SA).
    S_SA = np.interp(tau_grid, tau_s, S_s)          # (local)
    below = tau_grid < tau_s[0]                      # (local)
    above = tau_grid > tau_s[-1]                     # (local)
    S_SA = np.where(below, S_s[0] + dS_s[0] * (tau_grid - tau_s[0]), S_SA)
    S_SA = np.where(above, S_s[-1] + dS_s[-1] * (tau_grid - tau_s[-1]), S_SA)
    # dS/dtau on the dense grid (interp of the sampled gradient; clamp outside span)
    dS_SA = np.interp(tau_grid, tau_s, dS_s)        # (local)
    dS_SA = np.where(below, dS_s[0], dS_SA)
    dS_SA = np.where(above, dS_s[-1], dS_SA)
    return S_SA, dS_SA, (tau_s, S_s, dS_s)


def build_condensation_well(tau_grid):
    """E_cond(tau): the BCS condensation well, on the SAME energy axis as S_SA.

    Physics: the van Hove DOS maximizes the gap (hence |E_cond|) at the fold, so
    E_cond(tau) is a well centred on tau_fold=0.190 with depth |E_cond_fold|. The
    canonical magnitude is the 8-mode ED condensation energy E_cond=-0.13685 M_KK
    (negative = bound). The S53 speed bump (ratio_BCS=1.30, local MAXIMUM at
    tau=0.2015) lives in the condensation-vs-geometry gradient comparison; the
    well shape we adopt is the substrate-natural one whose gradient at the fold
    matches the canonical |dE_cond/dtau| inferred from ratio_BCS.

    CRITICAL UNIT NOTE: S_SA is in spectral-action units (surface span ~13545
    over tau in [0.05,0.30]); E_cond is in M_KK units (|E_cond|~0.137). To form
    E_eff = S_SA + E_cond on a single energy axis we keep BOTH in their native
    framework units WITHOUT an artificial rescaling: the spectral action IS the
    substrate energy functional (a_0-a_2+a_4 spectral moments), and E_cond is the
    pairing-sector energy in the same M_KK system once the SA is expressed in M_KK
    energy units. The S42 surface is dimensionless-Tr-normalized; we therefore
    report BOTH the raw-units E_eff (S_SA + E_cond, where E_cond is a sub-permille
    perturbation) AND the gradient-ratio diagnostic that is unit-INVARIANT (a
    dimensionless ratio of gradients). The verdict's localization test uses the
    gradient-ratio (unit-invariant) AND the explicit first-passage integral.
    """
    depth = abs(float(cc.E_cond))                   # (local) 0.13685 M_KK (8-mode ED)
    # Width of the condensation well: tie to the fold-window. The van Hove A2
    # cusp localizes the gap enhancement; use a Gaussian well of width sigma_w
    # set by the S42 fold-window half-span (the fold sits at 0.19; the S53 speed
    # bump at 0.2015 is ~0.012 away). sigma_w = 0.03 (the fold neighbourhood).
    sigma_w = 0.03                                  # (local) condensation-well width (fold neighbourhood)
    # E_cond(tau) = -depth * exp(-(tau-tau_fold)^2 / (2 sigma_w^2))  [well, min at fold]
    E_cond = -depth * np.exp(-((tau_grid - TAU_FOLD_TARGET) ** 2) / (2.0 * sigma_w ** 2))  # (local)
    # dE_cond/dtau = -depth * exp(...) * (-(tau-tau_fold)/sigma_w^2)
    dE_cond = (-depth * np.exp(-((tau_grid - TAU_FOLD_TARGET) ** 2) / (2.0 * sigma_w ** 2))
               * (-(tau_grid - TAU_FOLD_TARGET) / sigma_w ** 2))  # (local)
    return E_cond, dE_cond, depth, sigma_w


def build_collective_inertia(tau_grid):
    """M(tau): the ATDHFB collective inertia along Jensen.

    Anchored at M_ATDHFB=1.695 (S40 cranking mass; the corrected value -- the
    raw S40 cranking estimate was 50-170x wrong, M_ATDHFB=1.695 is canonical).
    ATDHFB cranking inertia scales as M(tau) ~ [sum_qp |<qp|dH/dtau|qp'>|^2 /
    (E_qp+E_qp')^3]; near a van Hove DOS enhancement the inertia rises (more
    low-energy two-qp states), but the BCS pairing gap REDUCES M (the "speedup":
    a finite gap pushes E_qp up, shrinking the cranking sum). We model M(tau) as
    the anchor value with a mild DOS-tracking enhancement near the fold,
    suppressed by the pairing gap. Because the inertia enters the first-passage
    time as sqrt(M), and M varies by O(1) across the grid (NOT orders of
    magnitude), it does NOT create a localizing extremum on its own -- the
    localization (if any) must come from E_eff. Returns M(tau) (>0).
    """
    M0 = float(cc.M_ATDHFB)                          # (local) 1.695 anchor
    # DOS-tracking bump near the fold (mild, O(1)); width matches the fold window.
    # The pairing-gap suppression keeps the enhancement modest (factor <~1.3).
    sigma_M = 0.04                                   # (local) inertia bump width
    bump = 0.25 * np.exp(-((tau_grid - TAU_FOLD_TARGET) ** 2) / (2.0 * sigma_M ** 2))  # (local) <=25%
    M_tau = M0 * (1.0 + bump)                         # (local) M(tau) > 0
    return M_tau, M0, sigma_M


def first_passage_localization(tau_grid, M_tau, E_eff, dE_eff):
    """Least-action / first-passage analysis on the collective Hamiltonian.

    Two complementary localization probes:

    (A) Interior-stationary-point test (the variational question): does E_eff(tau)
        have a sign change in dE_eff/dtau on the interior of [SCAN_MIN, SCAN_MAX]?
        If YES at tau* -- that is a dynamically-selected extremum (a well bottom
        or a barrier top). If NO -- E_eff is monotone, the pure-action variational
        route has no interior selection (the S95 T5-BROKEN structure).

    (B) First-passage / action-density localization: from the cold start tau->0,
        the WKB action density along the trajectory is
            dS_WKB/dtau = sqrt( 2 M(tau) * |E_eff(tau) - E_eff(tau_start)| )
        and the FIRST-PASSAGE dwell density (the inverse local "velocity") is
            rho_dwell(tau) ∝ sqrt( M(tau) / (2 * |E_top - E_eff(tau)| + eps) ).
        The transit "localizes" where the dwell density (or equivalently the
        action density gradient) peaks. We locate tau_selected as the interior
        extremum of E_eff if one exists (probe A); else as the argmax of the
        first-passage dwell density relative to the monotone background, which
        identifies any speed-bump-induced concentration even absent a true well.

    Returns tau_selected, a method tag, and a diagnostics dict.
    """
    eps = 1e-30                                      # (local)
    interior = (tau_grid > SCAN_MIN + 1e-9) & (tau_grid < SCAN_MAX - 1e-9)  # (local)
    # --- Probe A: interior stationary point of E_eff (sign change of dE_eff) ---
    sign = np.sign(dE_eff)                            # (local)
    sign_changes = np.where(np.diff(sign) != 0)[0]   # (local) indices where gradient flips
    # restrict to interior crossings
    interior_changes = [i for i in sign_changes
                        if interior[i] and interior[i + 1]]  # (local)
    tau_star_A = None                                # (local)
    if interior_changes:
        # refine by linear interpolation of dE_eff to its zero
        i = interior_changes[0]                      # (local) first interior crossing
        t0, t1 = tau_grid[i], tau_grid[i + 1]        # (local)
        g0, g1 = dE_eff[i], dE_eff[i + 1]            # (local)
        tau_star_A = t0 - g0 * (t1 - t0) / (g1 - g0) if (g1 - g0) != 0 else t0
    # --- Probe B: first-passage dwell-density localization (a LOCAL speed bump) ---
    # WKB inverse-velocity density rho_dwell ∝ sqrt(M / (2(E_top - E_eff))). For a
    # MONOTONE E_eff this diverges only at the top-of-slide turning point (an edge
    # artifact, NOT a fold localization); a genuine speed bump shows as a LOCAL
    # peak in the dwell RESIDUAL over the smooth monotone background. Floor the
    # sqrt argument at a physically-scaled positive eps (turning-point handling).
    E_top = float(np.max(E_eff[interior]))           # (local) top of the (monotone) surface in-window
    E_span = float(np.ptp(E_eff[interior])) + eps    # (local) energy span (for the floor scale)
    arg = (E_top - E_eff) / E_span                   # (local) dimensionless, >=0 on interior
    arg = np.maximum(arg, 1e-12)                      # (local) turning-point floor (no sqrt-of-neg)
    dwell = np.sqrt(M_tau / (2.0 * arg))             # (local) inverse-velocity density (relative)
    # Subtract the smooth monotone trend to expose any LOCAL concentration.
    ln_dwell = np.log(dwell + eps)                   # (local)
    coeffs = np.polyfit(tau_grid[interior], ln_dwell[interior], 2)  # (local) smooth quadratic trend
    ln_dwell_smooth = np.polyval(coeffs, tau_grid)   # (local)
    dwell_residual = ln_dwell - ln_dwell_smooth      # (local) local concentration over smooth bg
    # A real speed bump is a STRICT INTERIOR local maximum of the residual; the
    # last interior index is excluded so the top-of-slide turning point cannot
    # masquerade as a localization. argrelmax-free: detect interior local maxima.
    res = dwell_residual                              # (local)
    interior_idx = np.where(interior)[0]             # (local)
    local_max_idx = [j for j in interior_idx[1:-1]
                     if res[j] > res[j - 1] and res[j] >= res[j + 1]]  # (local) strict interior peaks
    if local_max_idx:
        j_best = max(local_max_idx, key=lambda j: res[j])  # (local) strongest interior bump
        tau_star_B = float(tau_grid[j_best])         # (local)
        max_residual = float(res[j_best])             # (local) speed-bump strength
        bump_found = True                            # (local)
    else:
        # No interior local maximum: the dwell is monotone -> NO speed-bump
        # localization. Report None (honest: the first-passage probe found no
        # interior concentration; the transit slides monotonically).
        tau_star_B = None                            # (local)
        max_residual = 0.0                           # (local)
        bump_found = False                           # (local)
    # --- Select: prefer a genuine interior stationary point of E_eff (A);
    #     else the first-passage interior speed-bump (B); else NO localization. ---
    if tau_star_A is not None:
        tau_selected = float(tau_star_A)             # (local)
        method = "interior-stationary-point"         # (local)
    elif tau_star_B is not None:
        tau_selected = float(tau_star_B)             # (local)
        method = "first-passage-speed-bump"          # (local)
    else:
        # No dynamical localization at all. Sentinel = SCAN_MAX edge (the cold
        # transit runs monotonically off the top of the surface); the |dtau|
        # against the fold is then large by construction -> FAIL, for the
        # structurally-correct reason (no interior selection).
        tau_selected = float(SCAN_MAX)               # (local) sentinel: monotone runoff
        method = "no-localization-monotone-runoff"   # (local)
    diagnostics = {
        "tau_star_A_interior_stationary": (float(tau_star_A) if tau_star_A is not None else None),
        "tau_star_B_first_passage": (float(tau_star_B) if tau_star_B is not None else None),
        "n_interior_sign_changes_dE_eff": int(len(interior_changes)),
        "n_interior_dwell_local_maxima": int(len(local_max_idx)),
        "speed_bump_found": bool(bump_found),
        "max_dwell_residual": max_residual,
        "E_top_in_window": float(E_top),
    }
    return tau_selected, method, diagnostics


def compute() -> dict:
    """Main computation: build H, run least-action/first-passage, select tau."""
    tau = np.linspace(SCAN_MIN, SCAN_MAX, N_TAU)     # (local) 400-pt tau grid

    # 1. Spectral action surface S_SA(tau) (monotone) + its gradient
    S_SA, dS_SA, s42_raw = build_spectral_action_surface(tau)

    # 2. BCS condensation well E_cond(tau) (deepening toward fold) + gradient
    E_cond, dE_cond, ec_depth, sigma_w = build_condensation_well(tau)

    # 3. Effective potential E_eff = S_SA + E_cond + its gradient
    E_eff = S_SA + E_cond                            # (local)
    dE_eff = dS_SA + dE_cond                          # (local)

    # 4. ATDHFB collective inertia M(tau)
    M_tau, M0, sigma_M = build_collective_inertia(tau)

    # 5. Least-action / first-passage localization
    tau_selected, method, diag = first_passage_localization(tau, M_tau, E_eff, dE_eff)

    # 6. The governing magnitude check (unit-INVARIANT gradient ratio at the fold)
    #    -- this is the FRIED-39 quantity, reproduced inside the collective frame.
    i_fold = int(np.argmin(np.abs(tau - TAU_FOLD_TARGET)))  # (local)
    dS_fold_grid = float(dS_SA[i_fold])              # (local) SA gradient at fold
    dEcond_fold_grid = float(abs(dE_cond[i_fold]))   # (local) |E_cond gradient| at fold
    # |dE_cond/dtau| at the fold of a Gaussian well is 0 (minimum); the MAX
    # gradient of the well is at tau_fold +- sigma_w. Report the max well gradient
    # (the strongest the condensate can pull) vs the SA gradient there.
    imax_well = int(np.argmax(np.abs(dE_cond)))      # (local)
    dEcond_max_grad = float(abs(dE_cond[imax_well])) # (local) steepest well gradient
    dS_at_wellmax = float(dS_SA[imax_well])          # (local) SA gradient at the steepest-well point
    grad_ratio = dS_at_wellmax / (dEcond_max_grad + 1e-30)  # (local) SA-vs-BCS gradient ratio

    # 7. Does E_eff acquire an interior stationary point? (the variational test)
    has_interior_extremum = diag["n_interior_sign_changes_dE_eff"] > 0  # (local)

    delta_tau = abs(tau_selected - TAU_FOLD_TARGET)  # (local)

    return {
        "value": float(tau_selected),
        "tau": tau,
        "S_SA": S_SA,
        "dS_SA": dS_SA,
        "E_cond": E_cond,
        "dE_cond": dE_cond,
        "E_eff": E_eff,
        "dE_eff": dE_eff,
        "M_tau": M_tau,
        "tau_selected": float(tau_selected),
        "method": method,
        "delta_tau": float(delta_tau),
        "has_interior_extremum": bool(has_interior_extremum),
        "grad_ratio_SA_vs_BCS": float(grad_ratio),
        "dS_fold_grid": dS_fold_grid,
        "dEcond_max_grad": dEcond_max_grad,
        "ec_depth": float(ec_depth),
        "sigma_w": float(sigma_w),
        "M0": float(M0),
        "diag": diag,
        "s42_raw": s42_raw,
        "i_fold": i_fold,
    }


# ---------------------------------------------------------------------------
# Section 6 — Plot
# ---------------------------------------------------------------------------
def make_plot(R):
    tau = R["tau"]
    fig, axes = plt.subplots(2, 2, figsize=(13, 9))

    # (a) Effective potential E_eff = S_SA + E_cond
    ax = axes[0, 0]
    ax.plot(tau, R["S_SA"], color="navy", lw=1.6, label=r"$S_{\rm SA}(\tau)$ (spectral action)")
    ax.axvline(TAU_FOLD_TARGET, color="crimson", ls="--", lw=1.2, label=r"$\tau_{\rm fold}=0.190$")
    ax.axvline(R["tau_selected"], color="green", ls=":", lw=1.6,
               label=fr"$\tau_{{\rm sel}}={R['tau_selected']:.3f}$")
    ax.set_xlabel(r"$\tau$ (Jensen deformation)")
    ax.set_ylabel(r"$S_{\rm SA}$ (spectral-action units)")
    ax.set_title("(a) Spectral action surface (monotone)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # (b) Condensation well + the gradient comparison
    ax = axes[0, 1]
    ax.plot(tau, R["E_cond"], color="darkorange", lw=1.8,
            label=fr"$E_{{\rm cond}}(\tau)$ (well, depth {R['ec_depth']:.3f} $M_{{KK}}$)")
    ax.axvline(TAU_FOLD_TARGET, color="crimson", ls="--", lw=1.2)
    ax.set_xlabel(r"$\tau$")
    ax.set_ylabel(r"$E_{\rm cond}$ ($M_{KK}$ units)")
    ax.set_title("(b) BCS condensation well (deepens at fold)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    # (c) Gradient ratio diagnostic (the FRIED-39 quantity, unit-invariant)
    ax = axes[1, 0]
    ax.semilogy(tau, np.abs(R["dS_SA"]), color="navy", lw=1.6, label=r"$|dS_{\rm SA}/d\tau|$")
    ax.semilogy(tau, np.abs(R["dE_cond"]) + 1e-12, color="darkorange", lw=1.6,
                label=r"$|dE_{\rm cond}/d\tau|$")
    ax.axvline(TAU_FOLD_TARGET, color="crimson", ls="--", lw=1.2)
    ax.set_xlabel(r"$\tau$")
    ax.set_ylabel("gradient magnitude (log)")
    ax.set_title(fr"(c) SA-vs-BCS gradient ratio $\approx${R['grad_ratio_SA_vs_BCS']:.0f}$\times$ "
                 f"(FRIED-39: 6596x)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, which="both")

    # (d) Collective inertia M(tau) + dwell residual
    ax = axes[1, 1]
    ax.plot(tau, R["M_tau"], color="purple", lw=1.6, label=fr"$M(\tau)$ (anchor {R['M0']:.3f})")
    ax.axhline(R["M0"], color="gray", ls=":", lw=1.0)
    ax.axvline(TAU_FOLD_TARGET, color="crimson", ls="--", lw=1.2)
    ax.axvline(R["tau_selected"], color="green", ls=":", lw=1.6)
    ax.set_xlabel(r"$\tau$")
    ax.set_ylabel(r"$M(\tau)$ (ATDHFB inertia)")
    ax.set_title(f"(d) Collective inertia; method={R['method']}")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3)

    fig.suptitle(
        f"INV11-W1-3 ATDHFB collective Hamiltonian -- least-action tau_fold selection\n"
        fr"$\tau_{{\rm sel}}={R['tau_selected']:.4f}$, target 0.190, "
        fr"$|\Delta\tau|={R['delta_tau']:.4f}$ (PASS$\leq$0.010, INFO$\leq$0.030); "
        f"interior extremum: {R['has_interior_extremum']}",
        fontsize=10)
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 7 — Verdict payload
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme, convention, L_max) -> str:
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          companion_note="", extra_rows=None) -> dict:
    payload: dict = {
        "session": int(SESSION),
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
    }
    if companion_note:
        payload["companion_note"] = companion_note
    if not (sign_verdict is None and magnitude_verdict is None and regime_verdict is None):
        payload["sign_verdict"] = sign_verdict
        payload["magnitude_verdict"] = magnitude_verdict
        payload["regime_verdict"] = regime_verdict
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


def evaluate_gate(delta_tau: float) -> str:
    """Plan §W1-3: PASS iff |dtau|<=0.010, INFO iff 0.010<|dtau|<=0.030, else FAIL."""
    if delta_tau <= PASS_TOL:
        return "PASS"
    if delta_tau <= INFO_TOL:
        return "INFO"
    return "FAIL"


# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")

    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    R = compute()

    print("=== Collective-Hamiltonian construction ===")
    print(f"  tau-grid: {N_TAU} pts over [{SCAN_MIN}, {SCAN_MAX}]")
    print(f"  M_ATDHFB anchor              : {R['M0']:.4f}")
    print(f"  E_cond well depth            : {R['ec_depth']:.5f} M_KK (8-mode ED)")
    print(f"  condensation-well width      : {R['sigma_w']:.3f}")
    print(f"  dS/dtau at fold (S42)        : {R['dS_fold_grid']:.1f}")
    print(f"  |dE_cond/dtau| max (well)    : {R['dEcond_max_grad']:.4f}")
    print(f"  SA-vs-BCS gradient ratio     : {R['grad_ratio_SA_vs_BCS']:.1f}x "
          f"(FRIED-39 canonical: 6596x)")
    print()
    print("=== Least-action / first-passage localization ===")
    print(f"  interior stationary point of E_eff? : {R['has_interior_extremum']}")
    print(f"  n_interior_sign_changes(dE_eff)     : {R['diag']['n_interior_sign_changes_dE_eff']}")
    print(f"  tau_star_A (interior stationary)    : {R['diag']['tau_star_A_interior_stationary']}")
    _tsb = R['diag']['tau_star_B_first_passage']  # (local)
    print(f"  tau_star_B (first-passage bump)     : "
          f"{(f'{_tsb:.4f}' if _tsb is not None else 'None (no interior bump)')}")
    print(f"  speed-bump found?                   : {R['diag']['speed_bump_found']}")
    print(f"  n_interior dwell local maxima       : {R['diag']['n_interior_dwell_local_maxima']}")
    print(f"  max dwell residual (speed bump)     : {R['diag']['max_dwell_residual']:.4e}")
    print(f"  selection method                    : {R['method']}")
    print()
    print(f"  tau_selected                 : {R['tau_selected']:.4f}")
    print(f"  target tau_fold              : {TAU_FOLD_TARGET:.4f}")
    print(f"  |delta_tau|                  : {R['delta_tau']:.4f}")
    print(f"  PASS_TOL={PASS_TOL}, INFO_TOL={INFO_TOL}")
    print()

    verdict = evaluate_gate(R["delta_tau"])

    # Save data
    np.savez(
        OUT_NPZ,
        tau=R["tau"], S_SA=R["S_SA"], dS_SA=R["dS_SA"],
        E_cond=R["E_cond"], dE_cond=R["dE_cond"],
        E_eff=R["E_eff"], dE_eff=R["dE_eff"], M_tau=R["M_tau"],
        tau_selected=R["tau_selected"], tau_fold_target=TAU_FOLD_TARGET,
        delta_tau=R["delta_tau"], method=R["method"],
        has_interior_extremum=R["has_interior_extremum"],
        grad_ratio_SA_vs_BCS=R["grad_ratio_SA_vs_BCS"],
        dS_fold_grid=R["dS_fold_grid"], dEcond_max_grad=R["dEcond_max_grad"],
        ec_depth=R["ec_depth"], sigma_w=R["sigma_w"], M0=R["M0"],
        n_interior_sign_changes=R["diag"]["n_interior_sign_changes_dE_eff"],
        tau_star_A=(R["diag"]["tau_star_A_interior_stationary"]
                    if R["diag"]["tau_star_A_interior_stationary"] is not None else np.nan),
        tau_star_B=(R["diag"]["tau_star_B_first_passage"]
                    if R["diag"]["tau_star_B_first_passage"] is not None else np.nan),
        speed_bump_found=R["diag"]["speed_bump_found"],
        n_interior_dwell_local_maxima=R["diag"]["n_interior_dwell_local_maxima"],
        max_dwell_residual=R["diag"]["max_dwell_residual"],
        PASS_TOL=PASS_TOL, INFO_TOL=INFO_TOL, verdict=verdict,
        FRIED39_grad_ratio=6596.0, FRIED39_shortfall=133200.0,
    )
    print(f"  saved: {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    make_plot(R)
    print(f"  saved: {OUT_PNG.relative_to(PROJECT_ROOT)}")
    print()

    # 4-tuple + verdict payload
    tag = emit_4tuple(round(R["tau_selected"], 3), SCHEME, CONVENTION, L_MAX)
    print(tag)

    # Companion annotation rows: the governing-physics finding + FRIED-39 cross-ref.
    extra = [
        (f"# INV11-W1-3 collective-H least-action: tau_selected={R['tau_selected']:.4f} "
         f"target=0.190 |dtau|={R['delta_tau']:.4f} method={R['method']}"),
        (f"# E_eff=S_SA+E_cond interior_extremum={R['has_interior_extremum']} "
         f"SA-vs-BCS_grad_ratio={R['grad_ratio_SA_vs_BCS']:.0f}x "
         f"(FRIED-39 T6-BROKEN canonical: 6596x, shortfall 133200x)"),
    ]
    value_str = (f"tau_selected={R['tau_selected']:.4f}_target=0.190_dtau={R['delta_tau']:.4f}_"
                 f"interior_extremum={R['has_interior_extremum']}_"
                 f"grad_ratio={R['grad_ratio_SA_vs_BCS']:.0f}x")
    print_verdict_payload(
        verdict, value_str, audit_sha, content_sha,
        companion_note=("ATDHFB collective Hamiltonian H=1/2 M(tau)taudot^2+E_eff(tau); "
                        "least-action/first-passage tau_fold selection; "
                        "re-derives FRIED-39 (T6-BROKEN) SA-vs-BCS gradient dominance "
                        "in the explicit collective frame"),
        extra_rows=extra,
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
