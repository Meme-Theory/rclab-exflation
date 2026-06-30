#!/usr/bin/env python3
"""
INV2 W1-3 — Static spherically-symmetric tau(r) modulus-soliton:
reduced 12D Einstein-scalar ODE; does the compact-object sector open?
================================================================================

Gate: INV2-W1-3 ([VERIFY] — existence / set-membership)
  EXISTS tau_c such that tau(r) is a localized regular self-gravitating profile
  (tau(r)->tau_inf as r->inf, finite mass M = radial energy integral converges),
  AND the mass-radius curve M(R) is finite with a compactness ceiling
  sup(2GM/R) < C_max = 8/9 (the GR Buchdahl bound).

  PASS = the existence set is non-empty AND M(R) finite with sup(2GM/R) < 8/9.
  FAIL = no regular localized self-gravitating profile in the tau_c-scan.
  INFO = profiles exist but regime sub-verdict MARGINAL/BREAKDOWN
         (reduced-action truncation breaks before a clean M(R) ceiling).

Classification: GEOMETRIC.

METHODOLOGY
-----------
Reduce the 12D Einstein-Hilbert action S_{12D} = int_{M4 x SU(3)} R_P sqrt(g_P) d^{12}x
on the product M4 x SU(3) with the modulus tau promoted to a field tau(r) on a static
spherically-symmetric 4D base. The fiber Einstein-Hilbert term descends as the modulus
potential V(tau) = -R_K(tau) (the S32 domain-wall / Lambda_eff = -1/2 R_K lineage:
session-32-baptista-collab, session-54 RWP), with R_K the E3 closed-form internal scalar
curvature of the Jensen-deformed SU(3) fiber (recomputed in-script from the closed form,
the substrate-first source, NOT a hardcoded literal). The DeWitt supermetric supplies the
kinetic stiffness (1/2)*G_DeWitt = 5/2 (S42 s42_gradient_stiffness; the S32 flat-space
first integral (5/2)(dtau/dx)^2 = V(tau)-V_0 confirms the prefactor).

The reduced 4D action is the scalar-soliton functional
   E[tau(r)] = int d^3x [ (1/2)*G_DeWitt*(d_r tau)^2 + V_SA(tau) ]
coupled to ds^2 = -e^{2Phi}dt^2 + e^{2Lambda}dr^2 + r^2 dOmega^2. We solve the coupled
static Einstein-scalar (radion-TOV / scalar-star) system by RK45 adaptive shooting
(scipy.integrate.solve_ivp) from a regular center tau(0)=tau_c, tau'(0)=0, m(0)=0 for a
25-point tau_c-scan on [0.19, 2.0] (from the fold up into deep compactification), classify
each trajectory (localized / rolling / collapse), and where a localized profile exists,
extract the mass-radius relation M(R) and the compactness 2GM/R.

Because V_SA is PROVEN MONOTONE (dS/dtau = +58672.8 > 0 at the fold, S17a-S45, 9600/9600;
and V = -R_K is monotone DECREASING on [0.19, 2.0] with NO critical point — Sage-verified),
the soliton (if it exists) is NOT a double-well kink but a gradient-vs-gravity balance
(radion-boson-star analog). NUMBERS first, gate second, interpretation third.

DISCIPLINE
----------
- from canonical_constants import * (MANDATORY first import); G_DeWitt + tau_fold canonical
- R_K(tau) recomputed in-script from E3 closed form (substrate-first; NO 2.018144 literal)
- solve_ivp RK45 adaptive shooting from a regular center
- CPU-correct (1D radial ODE); OMP threads capped at 8 BEFORE numpy import
- dual-SHA (audit + content) emitted; print_verdict_payload (agent calls emit_verdict)
- every local/intermediate tagged # (local)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — CPU thread cap BEFORE numpy (1D radial ODE; GPU not warranted)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
#   investigation-2 is a sibling of _shared; inject _shared on sys.path so
#   `from canonical_constants import *` resolves the canonical module.
# ---------------------------------------------------------------------------
import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent              # computations/investigation-2
COMPUTATIONS_DIR = SESSION_DIR.parent                       # computations
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403  (G_DeWitt, tau_fold, ...)

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib
import json
import time

import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 3 — Identity + pre-registration pins (PRDR machinery_pin_map)
# ---------------------------------------------------------------------------
SESSION = "2"                                                       # (local) investigation number
GATE_ID = "INV2-W1-3"                                               # (local)
SCHEME = "reduced-12D-einstein-scalar-soliton-shooting-G-DeWitt-5-V-SA-monotone"  # (local)
CONVENTION = "static-spherically-symmetric-TOV-radion-analog"      # (local)
L_MAX = "N/A"                                                       # (local) closed-form R_K + V; no Peter-Weyl tower

N_EVAL = 25                                                         # (local) tau_c-scan points
SCAN_MIN = 0.19                                                     # (local) tau_c from the fold ...
SCAN_MAX = 2.0                                                      # (local) ... up into deep compactification
ODE_RTOL = 1.0e-8                                                   # (local) shooting integrator tol
ODE_ATOL = 1.0e-10                                                  # (local)
C_MAX = 8.0 / 9.0                                                   # (local) GR Buchdahl compactness ceiling = 0.8889
R_MAX_INTEGRATE = 5.0e3                                             # (local) outward radial cutoff (M_KK^-1 units)
DENSITY_FLOOR_FRAC = 1.0e-4                                         # (local) rho/rho_center floor defining the "edge"
MASS_ENCLOSE_FRAC = 0.99                                            # (local) radius R := where 99% of mass enclosed

OUT_NPZ = SESSION_DIR / "inv2_w1_tau_modulus_soliton.npz"
OUT_PNG = SESSION_DIR / "inv2_w1_tau_modulus_soliton.png"

INPUT_FILES = [SHARED_DIR / "canonical_constants.py"]


# ---------------------------------------------------------------------------
# Section 4 — substrate-first R_K(tau) (E3 closed form) + reduced potential V(tau)
# ---------------------------------------------------------------------------
def R_K_of_tau(tau):
    """E3 closed-form internal scalar curvature of Jensen-deformed SU(3).

    R_K(tau) = -1/4 e^{-4tau} + 2 e^{-tau} - 1/4 + 1/2 e^{2tau}.
    Source: baptista-operator-dk-tau.md (E3); R_K(0)=2, R_K(0.19)=2.018144.
    Recomputed here from the closed form — the substrate-first source —
    NOT a hardcoded literal (per substrate-first-canonical-sourcing.md).
    """
    return (-0.25 * np.exp(-4.0 * tau)
            + 2.0 * np.exp(-tau)
            - 0.25
            + 0.5 * np.exp(2.0 * tau))


def dR_K_dtau(tau):
    """d R_K / d tau (analytic derivative of the E3 closed form)."""
    return (1.0 * np.exp(-4.0 * tau)
            - 2.0 * np.exp(-tau)
            + 1.0 * np.exp(2.0 * tau))


def V_of_tau(tau):
    """Reduced-Einstein-Hilbert modulus potential V(tau) = -R_K(tau).

    The fiber Einstein-Hilbert term R_K descends into the dimensionally-reduced
    4D action as MINUS a scalar potential (S32 domain-wall V=-R_K;
    Lambda_eff=-1/2 R_K, session-54). Monotone DECREASING on [0.19,2.0],
    NO interior well (Sage-verified) -> the soliton, if any, is gradient-vs-gravity
    balance, NOT a double-well kink.
    """
    return -R_K_of_tau(tau)


def dV_dtau(tau):
    """d V / d tau = -d R_K / d tau."""
    return -dR_K_dtau(tau)


# Spectral-action monotonicity cross-check anchor (PROVEN, S42):
DS_DTAU_FOLD_PROVEN = 58672.8                                       # (local) dS/dtau at fold (S42; monotone)


# ---------------------------------------------------------------------------
# Section 5 — static Einstein-scalar (radion-TOV) RHS
#
# Metric: ds^2 = -e^{2Phi}dt^2 + e^{2Lambda}dr^2 + r^2 dOmega^2,  e^{-2Lambda}=1-2m/r.
# Geometrized units 8*pi*G = 1 (substrate-natural; compactness 2GM/R reported
# dimensionlessly so the unit choice does NOT affect the existence verdict).
# State y = [tau, psi, m, Phi], psi := dtau/dr.
#   dm/dr   = 4*pi*r^2 * rho
#   rho     = (1/2)*G_DeWitt*e^{-2Lambda}*psi^2 + V(tau)
#   p_r     = (1/2)*G_DeWitt*e^{-2Lambda}*psi^2 - V(tau)
#   dPhi/dr = (m + 4*pi*r^3*p_r) / (r*(r-2m))
#   dtau/dr = psi
#   dpsi/dr = -(2/r + dPhi/dr - dLambda/dr)*psi + (1/G_DeWitt)*e^{2Lambda}*dV/dtau
#   with dLambda/dr from differentiating e^{-2Lambda}=1-2m/r.
# ---------------------------------------------------------------------------
FOUR_PI = 4.0 * np.pi                                               # (local)


def rhs(r, y, G_dewitt):
    tau, psi, m, Phi = y                                           # (local)
    # metric function e^{-2Lambda} = 1 - 2m/r ; guard the center + horizon
    if r < 1.0e-12:
        emin2L = 1.0                                               # (local) regular center
    else:
        emin2L = 1.0 - 2.0 * m / r                                 # (local)
    # horizon / signature-flip guard: if 1-2m/r <= 0 the static ansatz breaks (collapse)
    if emin2L <= 1.0e-9:
        emin2L = 1.0e-9                                            # (local) clamp; event will fire
    e2L = 1.0 / emin2L                                            # (local) e^{2Lambda}

    Vt = V_of_tau(tau)                                            # (local)
    dVt = dV_dtau(tau)                                            # (local)

    rho = 0.5 * G_dewitt * emin2L * psi * psi + Vt                # (local) energy density
    p_r = 0.5 * G_dewitt * emin2L * psi * psi - Vt               # (local) radial pressure

    dm = FOUR_PI * r * r * rho                                    # (local)

    if r < 1.0e-12:
        dPhi = 0.0                                                # (local) regular center
        dLam = 0.0                                                # (local)
    else:
        denom = r * (r - 2.0 * m)                                # (local)
        if abs(denom) < 1.0e-30:
            denom = 1.0e-30 if denom >= 0 else -1.0e-30          # (local)
        dPhi = (m + FOUR_PI * r ** 3 * p_r) / denom              # (local)
        # dLambda/dr from e^{-2Lambda}=1-2m/r  =>  dLambda/dr = (dm/dr * r - m)/(r(r-2m))
        dLam = (dm * r - m) / denom                              # (local)

    dtau = psi                                                   # (local)
    dpsi = -(2.0 / max(r, 1.0e-12) + dPhi - dLam) * psi \
        + (1.0 / G_dewitt) * e2L * dVt                          # (local) scalar field eq

    return [dtau, dpsi, dm, dPhi]


# ----- termination events -----------------------------------------------------
def ev_horizon(r, y, G_dewitt):
    """1 - 2m/r -> 0 (apparent horizon / collapse): static ansatz breaks."""
    m = y[2]                                                     # (local)
    if r < 1.0e-9:
        return 1.0
    return (1.0 - 2.0 * m / r) - 1.0e-6
ev_horizon.terminal = True
ev_horizon.direction = -1


def ev_blowup(r, y, G_dewitt):
    """|tau| runs away to deep compactification (rolling, not localized)."""
    return 50.0 - abs(y[0])                                      # (local) |tau| reaches 50 -> rolling
ev_blowup.terminal = True
ev_blowup.direction = -1


# ---------------------------------------------------------------------------
# Section 6 — single shoot + classification
# ---------------------------------------------------------------------------
def shoot(tau_c, G_dewitt):
    """Integrate outward from a regular center; classify the trajectory.

    Returns dict with classification and, when localized, (M, R, compactness).
    """
    r0 = 1.0e-6                                                  # (local) tiny offset off the center
    y0 = [float(tau_c), 0.0, 0.0, 0.0]                          # (local) tau_c, psi=0, m=0, Phi=0
    sol = solve_ivp(
        rhs, (r0, R_MAX_INTEGRATE), y0,
        method="RK45", rtol=ODE_RTOL, atol=ODE_ATOL,
        args=(G_dewitt,), dense_output=False,
        events=(ev_horizon, ev_blowup), max_step=5.0,
    )                                                           # (local)

    r = sol.t                                                    # (local)
    tau = sol.y[0]                                               # (local)
    psi = sol.y[1]                                               # (local)
    m = sol.y[2]                                                 # (local)

    horizon_hit = sol.t_events[0].size > 0                       # (local) collapse
    blowup_hit = sol.t_events[1].size > 0                        # (local) rolling

    # local energy density along the ray (for edge / mass-fraction radius)
    emin2L = np.where(r > 1e-12, 1.0 - 2.0 * m / np.maximum(r, 1e-12), 1.0)  # (local)
    emin2L = np.clip(emin2L, 1e-9, None)                         # (local)
    rho = 0.5 * G_dewitt * emin2L * psi ** 2 + V_of_tau(tau)     # (local)

    out = {                                                      # (local)
        "tau_c": float(tau_c),
        "r": r, "tau": tau, "psi": psi, "m": m, "rho": rho,
        "horizon_hit": bool(horizon_hit),
        "blowup_hit": bool(blowup_hit),
        "r_end": float(r[-1]),
        "tau_end": float(tau[-1]),
        "psi_end": float(psi[-1]),
        "m_end": float(m[-1]),
        "localized": False,
        "M": np.nan, "R": np.nan, "compactness": np.nan,
        "classification": "",
    }

    # ---- classification ----
    # A localized self-gravitating profile requires:
    #   (i)  NO collapse (no horizon) and NO runaway (no blowup),
    #   (ii) the mass function m(r) settles to a finite ADM-like plateau,
    #   (iii) the density falls to a small fraction of its central value,
    #   (iv) the field settles (psi -> 0) toward an asymptotic tau_inf.
    if horizon_hit:
        out["classification"] = "collapse_horizon"
        return out
    if blowup_hit:
        out["classification"] = "rolling_runaway"
        return out

    # mass-settling test: does m(r) plateau? compare last-decade slope to plateau value
    rho_center = rho[0] if rho.size else np.nan                  # (local)
    # finite-mass requires the integrand 4 pi r^2 rho -> 0; with V=-R_K<0 the bulk
    # density is NEGATIVE and grows in magnitude as tau rolls, so m diverges negative.
    m_finite = np.isfinite(m[-1]) and abs(m[-1]) < 1.0e6         # (local)
    # density-decay test relative to centre
    if np.isfinite(rho_center) and abs(rho_center) > 0:
        decayed = abs(rho[-1]) < DENSITY_FLOOR_FRAC * abs(rho_center)  # (local)
    else:
        decayed = False                                         # (local)
    # field-settle test
    settled = abs(psi[-1]) < 1.0e-4                              # (local)

    if m_finite and decayed and settled:
        # localized: compute M (mass plateau) and R (99% mass-enclosure radius)
        M = float(m[-1])                                         # (local) ADM-like mass
        target = MASS_ENCLOSE_FRAC * m[-1]                       # (local)
        # first radius where |m(r)| >= 0.99 |m_end| (monotone-magnitude assumed)
        idx = np.searchsorted(np.abs(m), abs(target))           # (local)
        idx = min(idx, r.size - 1)                              # (local)
        R = float(r[idx])                                       # (local)
        compactness = abs(2.0 * M / R) if R > 0 else np.inf     # (local) 2GM/R (8piG=1 dimensionless)
        out.update(localized=True, M=M, R=R, compactness=compactness,
                   classification="localized")
        return out

    # neither collapsed nor runaway nor settled within R_MAX -> non-localizing roll
    out["classification"] = "non_localizing"
    return out


# ---------------------------------------------------------------------------
# Section 7 — SHA + verdict payload (S84+ dual-SHA; per script-template.py)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                        # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}                                                   # (local)
    for p in inputs:
        sha = sha256_of(p)                                     # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path, canonical_path, pins):
    sb = b""                                                    # (local)
    try:
        sb = script_path.read_bytes()
    except OSError:
        sb = b""
    cb = b""                                                    # (local)
    try:
        cb = canonical_path.read_bytes()
    except OSError:
        cb = b""
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"), sort_keys=True).encode("utf-8")  # (local)
    ha = hashlib.sha256(); ha.update(sb); ha.update(cb); ha.update(pinmap_json)
    hc = hashlib.sha256(); hc.update(sb)
    return ha.hexdigest(), hc.hexdigest()


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          companion_note="", extra_rows=None):
    """Print the delimited JSON payload for the agent to pass to emit_verdict.

    Investigation track: the agent calls
        emit_verdict(session=2, track="investigation", **payload)
    so we set session=2 and DO NOT add a session-track schema. [VERIFY] gate —
    NO sign/magnitude/regime 3-tuple (schema_v2_3tuple_required: false).
    """
    payload = {                                                 # (local)
        "session": 2,
        "track": "investigation",
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
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 8 — main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()                                            # (local)

    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()                      # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"      # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    # ----- substrate-first cross-checks (NUMBERS first) -----
    G_dewitt = float(G_DeWitt)                                  # (local) canonical 5.0
    print(f"G_DeWitt (canonical)            = {G_dewitt}")
    print(f"(1/2)*G_DeWitt                  = {0.5 * G_dewitt}   "
          f"<- S32 first integral (5/2)(dtau/dx)^2=V-V0 prefactor CHECK "
          f"({'OK' if abs(0.5*G_dewitt - 2.5) < 1e-12 else 'MISMATCH'})")
    print(f"tau_fold (canonical)           = {tau_fold}")
    print(f"R_K(0)   [E3, expect 2]        = {R_K_of_tau(0.0):.12f}")
    print(f"R_K(0.19)[E3, expect 2.018144] = {R_K_of_tau(0.19):.8f}")
    print(f"dR_K/dtau(0.19)[expect .27603] = {dR_K_dtau(0.19):.8f}")
    print(f"dS/dtau|fold (PROVEN monotone) = +{DS_DTAU_FOLD_PROVEN}  (V_SA=a0-a2+a4 well-less)")

    # monotonicity of V=-R_K across the scan (no interior well -> no double-well kink)
    tau_grid = np.linspace(SCAN_MIN, SCAN_MAX, 400)             # (local)
    dV_grid = dV_dtau(tau_grid)                                 # (local)
    V_monotone = bool(np.all(dV_grid < 0) or np.all(dV_grid > 0))  # (local)
    print(f"V(tau)=-R_K monotone on [{SCAN_MIN},{SCAN_MAX}]? {V_monotone}  "
          f"(dV/dtau sign-constant; NO interior well)")
    print()

    # ----- the tau_c-scan (25 points) -----
    tau_c_scan = np.linspace(SCAN_MIN, SCAN_MAX, N_EVAL)        # (local)
    results = []                                                # (local)
    print(f"=== tau_c-scan: {N_EVAL} points on [{SCAN_MIN}, {SCAN_MAX}] ===")
    for tc in tau_c_scan:
        res = shoot(tc, G_dewitt)                              # (local)
        results.append(res)
        print(f"  tau_c={tc:6.4f}  class={res['classification']:18s}  "
              f"r_end={res['r_end']:10.3g}  m_end={res['m_end']:+11.4g}  "
              f"localized={res['localized']}")

    n_localized = sum(1 for r in results if r["localized"])     # (local)
    n_collapse = sum(1 for r in results if r["classification"] == "collapse_horizon")  # (local)
    n_rolling = sum(1 for r in results if r["classification"] == "rolling_runaway")    # (local)
    n_nonloc = sum(1 for r in results if r["classification"] == "non_localizing")      # (local)

    # mass-radius + compactness over any localized profiles
    M_arr = np.array([r["M"] for r in results], dtype=float)    # (local)
    R_arr = np.array([r["R"] for r in results], dtype=float)    # (local)
    C_arr = np.array([r["compactness"] for r in results], dtype=float)  # (local)
    loc_mask = np.array([r["localized"] for r in results])      # (local)
    sup_compactness = (float(np.nanmax(C_arr[loc_mask]))        # (local)
                       if n_localized > 0 else np.nan)

    print()
    print(f"localized profiles found       : {n_localized} / {N_EVAL}")
    print(f"  collapse(horizon)            : {n_collapse}")
    print(f"  rolling(runaway)             : {n_rolling}")
    print(f"  non-localizing               : {n_nonloc}")
    if n_localized > 0:
        print(f"sup(2GM/R) over localized      : {sup_compactness:.6f}  "
              f"(C_max=8/9={C_MAX:.6f})")

    # ----- gate evaluation (set-membership existence) -----
    # PASS iff existence set non-empty AND M(R) finite AND sup(2GM/R) < C_max.
    if n_localized > 0 and np.isfinite(sup_compactness) and sup_compactness < C_MAX:
        verdict = "PASS"                                        # (local)
        value = (f"EXISTS_localized_n={n_localized}/{N_EVAL}_"
                 f"sup_compactness={sup_compactness:.4f}_lt_Cmax={C_MAX:.4f}")
    elif n_localized > 0:
        # localized but ceiling violated or M(R) ill-defined -> INFO (regime-marginal)
        verdict = "INFO"                                        # (local)
        value = (f"localized_n={n_localized}/{N_EVAL}_but_"
                 f"sup_compactness={sup_compactness:.4f}_ge_Cmax_or_illdef")
    else:
        # no localized profile anywhere in the scan -> FAIL (set empty)
        verdict = "FAIL"                                        # (local)
        # report the dominant non-existence channel
        chan = max(                                            # (local)
            (("collapse_horizon", n_collapse),
             ("rolling_runaway", n_rolling),
             ("non_localizing", n_nonloc)),
            key=lambda kv: kv[1])[0]
        value = (f"NO_localized_profile_set_empty_0/{N_EVAL}_"
                 f"dominant_channel={chan}_monotoneV_no_well")

    # ----- save data -----
    np.savez(
        OUT_NPZ,
        tau_c_scan=tau_c_scan,
        classification=np.array([r["classification"] for r in results]),
        localized=loc_mask,
        M=M_arr, R=R_arr, compactness=C_arr,
        r_end=np.array([r["r_end"] for r in results]),
        m_end=np.array([r["m_end"] for r in results]),
        tau_end=np.array([r["tau_end"] for r in results]),
        psi_end=np.array([r["psi_end"] for r in results]),
        n_localized=n_localized, n_collapse=n_collapse,
        n_rolling=n_rolling, n_nonloc=n_nonloc,
        sup_compactness=sup_compactness, C_max=C_MAX,
        G_DeWitt=G_dewitt, tau_fold=float(tau_fold),
        R_K_0=R_K_of_tau(0.0), R_K_fold=R_K_of_tau(0.19),
        dRK_dtau_fold=dR_K_dtau(0.19),
        half_G_DeWitt=0.5 * G_dewitt,
        V_monotone=V_monotone,
        dS_dtau_fold_proven=DS_DTAU_FOLD_PROVEN,
        verdict=verdict, value=value,
        audit_sha256=audit_sha, content_sha256=content_sha,
        # representative profiles for the plot (first 3 tau_c)
        prof0_r=results[0]["r"], prof0_tau=results[0]["tau"], prof0_m=results[0]["m"],
        prof_mid_r=results[N_EVAL // 2]["r"], prof_mid_tau=results[N_EVAL // 2]["tau"],
        prof_mid_m=results[N_EVAL // 2]["m"],
        prof_last_r=results[-1]["r"], prof_last_tau=results[-1]["tau"],
        prof_last_m=results[-1]["m"],
    )
    print(f"\nsaved: {OUT_NPZ.name}")

    # ----- plot -----
    _make_plot(results, tau_c_scan, tau_grid, dV_grid, n_localized,
               sup_compactness, verdict, G_dewitt)
    print(f"saved: {OUT_PNG.name}")

    # ----- 4-tuple + verdict payload -----
    print(f"(value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")
    print_verdict_payload(
        verdict, value, audit_sha, content_sha,
        companion_note=(f"existence set-membership; n_localized={n_localized}/{N_EVAL}; "
                        f"V=-R_K monotone(no well)={V_monotone}; "
                        f"(1/2)G_DeWitt=2.5 S32-check OK"),
        extra_rows=[
            f"# INV2-W1-3 channels: collapse={n_collapse} rolling={n_rolling} "
            f"nonloc={n_nonloc} localized={n_localized}",
        ],
    )

    wall = time.time() - t0                                     # (local)
    print(f"\n=== {GATE_ID}: {verdict} (wall {wall:.1f}s) ===")
    return 0


def _make_plot(results, tau_c_scan, tau_grid, dV_grid, n_localized,
               sup_compactness, verdict, G_dewitt):
    fig, ax = plt.subplots(2, 2, figsize=(13, 9))               # (local)

    # (a) representative tau(r) profiles
    a = ax[0, 0]                                                # (local)
    for i in [0, len(results) // 2, len(results) - 1]:
        r = results[i]                                          # (local)
        a.plot(r["r"], r["tau"], lw=1.6,
                label=f"tau_c={r['tau_c']:.2f} ({r['classification']})")
    a.axhline(float(tau_fold), color="k", ls=":", lw=1, label="tau_fold=0.19")
    a.set_xlabel("r  (M_KK^-1)"); a.set_ylabel("tau(r)")
    a.set_title("(a) radial modulus profiles tau(r)")
    a.set_xscale("symlog"); a.legend(fontsize=7); a.grid(alpha=0.3)

    # (b) mass function m(r)
    b = ax[0, 1]                                                # (local)
    for i in [0, len(results) // 2, len(results) - 1]:
        r = results[i]                                          # (local)
        b.plot(r["r"], r["m"], lw=1.6, label=f"tau_c={r['tau_c']:.2f}")
    b.set_xlabel("r  (M_KK^-1)"); b.set_ylabel("m(r)  (mass function)")
    b.set_title("(b) mass function m(r) — diverges if no localization")
    b.set_xscale("symlog"); b.legend(fontsize=7); b.grid(alpha=0.3)

    # (c) reduced potential V=-R_K and its monotone slope
    c = ax[1, 0]                                                # (local)
    c.plot(tau_grid, V_of_tau(tau_grid), "b-", lw=2, label="V(tau) = -R_K(tau)")
    c.plot(tau_grid, dV_grid, "r--", lw=1.4, label="dV/dtau (sign-constant)")
    c.axhline(0, color="k", lw=0.6)
    c.axvline(float(tau_fold), color="k", ls=":", lw=1, label="tau_fold")
    c.set_xlabel("tau"); c.set_ylabel("V, dV/dtau")
    c.set_title("(c) reduced potential V=-R_K: MONOTONE, NO interior well")
    c.legend(fontsize=8); c.grid(alpha=0.3)

    # (d) classification vs tau_c + verdict banner
    d = ax[1, 1]                                                # (local)
    classes = ["localized", "non_localizing", "rolling_runaway", "collapse_horizon"]  # (local)
    cmap = {cl: k for k, cl in enumerate(classes)}             # (local)
    yvals = [cmap.get(r["classification"], -1) for r in results]  # (local)
    d.scatter(tau_c_scan, yvals, c="purple", s=40)
    d.set_yticks(range(len(classes))); d.set_yticklabels(classes, fontsize=8)
    d.set_xlabel("tau_c (central modulus)")
    d.set_title(f"(d) trajectory class vs tau_c  —  VERDICT: {verdict}")
    d.grid(alpha=0.3)
    txt = (f"localized: {n_localized}/{len(results)}\n"
           f"sup(2GM/R): "
           f"{sup_compactness:.4f}\nC_max=8/9={8/9:.4f}\n"
           f"(1/2)G_DeWitt={0.5*G_dewitt:.1f} (=5/2 S32)")
    d.text(0.97, 0.05, txt, transform=d.transAxes, fontsize=8,
           ha="right", va="bottom",
           bbox=dict(boxstyle="round", fc="wheat", alpha=0.8))

    fig.suptitle("INV2-W1-3 — static spherically-symmetric tau(r) modulus-soliton "
                 "(reduced 12D Einstein-scalar; radion-TOV shooting)", fontsize=12)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


if __name__ == "__main__":
    sys.exit(main())
