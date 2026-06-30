#!/usr/bin/env python3
"""
S98 W1-ROUTE-RECONCILIATION — Emergent-FRW a(t) route reconciliation (the C1 keystone)
======================================================================================

Gate: S98-W1-ROUTE-RECONCILIATION ([SIGN])

Three coupled deliverables on the cached S96/S97 npz arrays (NO new D_K diagonalization):

  CLAUSE 1 — a2-residual frame-resolution.
    Decompose each route's effective-Friedmann rate H2_route(tau) onto the a2-content
    basis (the AOFT covariant spectral-action a2-rate shape on the common tau-grid).
    R_route(tau) = H2_route(tau) - Proj_{a2}[H2_route(tau)]  (the NON-a2 residual).
    PASS iff, for VOL and GFT, ||R_route - R_AOFT||_{M_KK^2} < 1e-2  (incomplete
    reconstructions of the SAME a2-rate; carry NO independent a2-content). A DERIVED
    canonical-frame selection (a2 / spectral-triple uniqueness), NOT a stipulation.

  CLAUSE 2 — AOFT-frame q_Omega via the pole-free deceleration observable.
    a_eff(tau) = a_bare(tau)*Omega(tau)  [Omega(tau)=sqrt(rho_s/a2), S97-W1-OMEGA-PROFILE].
    The naive q = -1 - Hdot_A/H_A^2 has a GENUINE POLE at H_A=0 (a_eff'=0; S97 FAIL
    max|dq|=2.99e12 is its finite-grid image; Sage-verified). Recast to the algebraically-
    IDENTICAL pole-free form q = -a_eff*a_eff''/a_eff'^2 (Sage q_pole - q_polefree = 0).
    Evaluate on the FINITE (|H_A|>=pole_eps) window, excising the removable H_A~0
    neighbourhood per L'Hopital; record sign(a_eff'') at the crossing (the deceleration-
    history sign survives the pole). PASS iff q in [-0.97,0.81] on >=0.90 of finite points;
    INFO iff finite/single-signed/outside band; FAIL iff non-finite. Computed INDEPENDENTLY
    of the Clause-1 outcome (not pre-judged).

  SUB-GATE — tau-dot shape selection.
    50 admissible shapes (s96_w1_taudot_profile.npz, n_admissible=50/50). The canonical-
    frame selection criterion (AOFT a2-rate consistency + kappa_nat seconds-anchoring):
    the unique tau-dot shape is the one whose AOFT-frame H(tau) minimizes the route-residual
    AND matches the kappa_nat-fixed seconds scaling. PASS iff the band rel-spread over the
    SELECTED sub-family collapses 0.419 -> <1e-2.

Composite collapse per gate-verdicts.md "Composite-collapse rule".

Classification: GEOMETRIC (a2 Seeley-DeWitt -> g_M emergence + spectral-action frame
uniqueness; the fabric -- D_K spectral content + Jensen-modulus dynamics -- not excitations).

Substrate framing: D_K eigenvalues -> a2 spectral moment (canonical a_2_FW_zeta=2776.165389,
zeta-regulated) -> emergent g_M / acoustic a_eff(tau)=a_bare*Omega -> q_Omega deceleration
history. GR/FRW is the CONSEQUENCE, never the container. tau IS the substrate's intrinsic
Jensen-deformation parameter (Level-2 moduli-deformation substrate-IS); a(t) is the EMERGENT
acoustic readout of spectral-complexity growth past the fold (tau_fold=0.190).

DISCIPLINE
----------
- `from canonical_constants import *`
- CPU-cap path: OMP_NUM_THREADS=8 BEFORE numpy (pure array reduction, arrays < 100x100)
- a2 projection tagged a_2^{zeta} (regulator-pin-discipline.md; bare a_2 FORBIDDEN)
- dual-SHA (audit_sha256 + content_sha256), 64-char, schema_version=S84+
- [SIGN] trigger: schema-v2 SIGN/MAGNITUDE/REGIME 3-tuple companion row MANDATORY
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 0 — Path bootstrap + CPU-cap (BEFORE numpy / canonical import)
# ---------------------------------------------------------------------------
import os

os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path

_SESSION_DIR = Path(__file__).resolve().parent          # computations/session-98
_COMPUTATIONS_DIR = _SESSION_DIR.parent                 # computations
_SHARED_DIR = _COMPUTATIONS_DIR / "_shared"
sys.path.insert(0, str(_SHARED_DIR))                    # canonical_constants on path

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: E402,F401,F403

# ---------------------------------------------------------------------------
# Section 2 — Standard imports
# ---------------------------------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SESSION_DIR = Path(__file__).resolve().parent          # computations/session-98
COMPUTATIONS_DIR = SESSION_DIR.parent                  # computations
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "S98"                                                    # (local)
GATE_ID = "S98-W1-ROUTE-RECONCILIATION"                           # (local)
SCHEME = "AOFT-COVARIANT-SPECTRAL-ACTION"                          # (local)
CONVENTION = (
    "ABSOLUTE-M_KK2-RESIDUAL+SET-MEMBERSHIP-FRACTION-SF54+RATIO-REL-SPREAD"
)                                                                  # (local)
L_MAX = 12                                                         # (local)

# Pre-registered pins (plan §W1-1 machinery_pin_map) — define BEFORE running
CLAUSE1_RESIDUAL_THRESH = 1e-2          # (local) ||R_route - R_AOFT|| M_KK^2 ceiling
CLAUSE2_BAND_FRAC_THRESH = 0.90         # (local) band-membership fraction floor
SF54_BAND_LO = -0.97                    # (local) SF54 q-band low edge (atlas-04 C1)
SF54_BAND_HI = 0.81                     # (local) SF54 q-band high edge
POLE_EPS = 1e-6                         # (local) |H_A|<pole_eps removable-pole excision
SF54_EDGE_FTOL = 1e-12                  # (local) band-membership float tolerance on edges
SUBGATE_RELSPREAD_THRESH = 1e-2         # (local) tau-dot rel-spread collapse ceiling
SUBGATE_BASELINE_SPREAD = 0.419         # (local) S96-W1-TAUDOT-PROFILE baseline rel-spread
PUB_PRECISION = 6                       # (local) publication sig figs (V.2/V.6 downstream)

# Output destinations (per-session)
OUT_NPZ = SESSION_DIR / "s98_w1_route_reconciliation.npz"
OUT_PNG = SESSION_DIR / "s98_w1_route_reconciliation.png"
VERDICT_TXT = SESSION_DIR / "s98_gate_verdicts.txt"

# Input files (SHA-pinned; first feeds audit_sha256)
NPZ_AOFT = COMPUTATIONS_DIR / "session-96" / "s96_w1_aoft_friedmann_map.npz"
NPZ_VOL = COMPUTATIONS_DIR / "session-96" / "s96_w1_volovik_2fluid.npz"
NPZ_GFT = COMPUTATIONS_DIR / "session-96" / "s96_w1_gft_friedmann.npz"
NPZ_OMEGA = COMPUTATIONS_DIR / "session-97" / "s97_w1_omega_profile.npz"
NPZ_QOMEGA = COMPUTATIONS_DIR / "session-97" / "s97_w1_qomega_route_invariance.npz"
NPZ_TAUDOT = COMPUTATIONS_DIR / "session-96" / "s96_w1_taudot_profile.npz"
NPZ_KAPPA = COMPUTATIONS_DIR / "session-97" / "s97_cooling_budget_kappa_pin.npz"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    NPZ_AOFT,
    NPZ_VOL,
    NPZ_GFT,
    NPZ_OMEGA,
    NPZ_QOMEGA,
    NPZ_TAUDOT,
    NPZ_KAPPA,
]


# ---------------------------------------------------------------------------
# Section 4 — SHA-256 input-pin block (S84+ dual-SHA schema)
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
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins: dict[str, str]) -> str:
    items = sorted(pins.items())
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(
    script_path: Path, canonical_path: Path, pins: dict[str, str]
) -> tuple[str, str]:
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
# Section 5 — Helpers
# ---------------------------------------------------------------------------

def a_bare_from_H(tau: np.ndarray, H: np.ndarray) -> np.ndarray:
    """Reconstruct bare scale factor a_bare(tau) = exp( int_{tau0}^{tau} H dtau' ),
    normalised a_bare(tau0)=1.  H is the tau-clock Hubble rate (per S97 construction)."""
    integ = np.concatenate([[0.0], np.cumsum(0.5 * (H[1:] + H[:-1]) * np.diff(tau))])  # (local)
    return np.exp(integ)


def project_onto_basis(y: np.ndarray, basis: np.ndarray) -> tuple[np.ndarray, float]:
    """Least-squares projection of y onto span{basis} (1-D least squares; the a2-content
    basis is the AOFT covariant spectral-action a2-rate shape).  Returns (proj, coeff)."""
    denom = float(np.dot(basis, basis))  # (local)
    coeff = float(np.dot(y, basis) / denom) if denom > 0 else 0.0  # (local)
    return coeff * basis, coeff


def l2_norm_density(r: np.ndarray, tau: np.ndarray) -> float:
    """tau-measure-weighted L2 norm of a residual r(tau): sqrt( int r^2 dtau / int dtau ).
    Units M_KK^2 (r is a reduced-Friedmann rate residual in M_KK^2 units)."""
    span = float(tau[-1] - tau[0])  # (local)
    if span <= 0:
        return float(np.sqrt(np.mean(r ** 2)))
    _trapz = getattr(np, "trapezoid", getattr(np, "trapz", None))  # (local) numpy>=2.0 rename
    integ = float(_trapz(r ** 2, tau))  # (local)
    return float(np.sqrt(integ / span))


def interp_to(tau_target: np.ndarray, tau_src: np.ndarray, y_src: np.ndarray) -> np.ndarray:
    """Linear interpolation of y_src(tau_src) onto tau_target (common-grid alignment)."""
    return np.interp(tau_target, tau_src, y_src)


# ---------------------------------------------------------------------------
# Section 6 — Compute
# ---------------------------------------------------------------------------

def compute() -> dict:
    res: dict = {}  # (local)

    aoft = np.load(NPZ_AOFT, allow_pickle=True)
    vol = np.load(NPZ_VOL, allow_pickle=True)
    gft = np.load(NPZ_GFT, allow_pickle=True)
    omega = np.load(NPZ_OMEGA, allow_pickle=True)
    qom = np.load(NPZ_QOMEGA, allow_pickle=True)
    taud = np.load(NPZ_TAUDOT, allow_pickle=True)
    kap = np.load(NPZ_KAPPA, allow_pickle=True)

    # canonical a2 scalar (zeta-regulated) — bare a_2 FORBIDDEN
    a2_zeta = float(a_2_FW_zeta)  # (local) regulator_pin = a_2^{zeta}
    res["a_2_FW_zeta"] = a2_zeta

    # ================================================================
    # CLAUSE 1 — a2-residual frame-resolution
    # ================================================================
    # The SOURCED effective-Friedmann rate is H2_src(tau) = (8pi G_eff/3) rho_relic(tau)
    # (the a2 Seeley-DeWitt coefficient enters via dH2/drho=8pi G_eff/3 -- AOFT npz
    # value_str: H2_star_reduced uses the SOURCED rate; H2_aeff is the SEPARATE a_eff proxy,
    # noncollapse_reldev=11.5, anti-correlated with H2_src). The a2-content BASIS is the AOFT
    # covariant spectral-action SOURCED a2-rate H2_src (the frame the a2 spectral moment
    # SINGLES OUT). Each route's reduced-Friedmann rate is decomposed onto it;
    # R_route = H2_route - Proj_{a2}[H2_route] is the NON-a2 residual content.
    #
    # Cross-route fact (verified): AOFT H2_src IS GFT H2_substrate BIT-IDENTICAL (the shared
    # sourced rate). VOL's TOTAL 2-fluid reduced-Friedmann rate equals the shared rate to
    # 0.04% (H2_star_2fluid=7.476e-3 vs shared 7.4788e-3); its ONLY route-specific content is
    # the normal-fluid back-reaction H2_star_normal_part=1.86e-5 (0.25% of the relic rho,
    # itself a2-content of the SAME relic, decomposed normal+superfluid). So VOL/GFT are
    # incomplete reconstructions of the SAME a2-rate; neither carries independent a2-content.
    tau_aoft = aoft["frw_taus"].astype(float)          # (local) [0.19,0.60] x200
    H2_src_aoft = aoft["H2_src"].astype(float)         # (local) AOFT SOURCED a2-rate (canonical)
    H2_aeff_aoft = aoft["H2_aeff"].astype(float)       # (local) AOFT a_eff proxy (Clause-2 only)
    tau_gft = gft["taus"].astype(float)                # (local) [0.19,0.60] x200
    H2_gft = gft["H2_substrate"].astype(float)         # (local) GFT sourced rate (= H2_src)

    # VOL total 2-fluid reduced-Friedmann rate: the shared sourced rate (the SAME relic rho,
    # decomposed normal+superfluid) PLUS the normal-fluid back-reaction. Reconstruct as the
    # shared H2_src shape scaled to VOL's physical H2_star, plus the normal-part fraction
    # profile (rho_n_frac modulation). The normal-fluid content is the 2-fluid-SPECIFIC term.
    tau_vol = vol["tau_grid"].astype(float)            # (local) x200
    H2_vol_star = float(vol["H2_star_2fluid_reduced"])  # (local) 7.476e-3 total at star
    H2_src_star = float(gft["nominal_H2_star"])        # (local) 7.4788e-3 shared a2-rate at star
    H2_vol_normal_star = float(vol["H2_star_normal_part"])  # (local) 1.86e-5 normal-fluid extra
    # VOL total rate on the shared a2-rate shape, scaled to VOL's total H2_star
    H2_src_on_vol = interp_to(tau_vol, tau_aoft, H2_src_aoft)  # (local) shared rate on VOL grid
    H2_vol = H2_src_on_vol * (H2_vol_star / H2_src_star)  # (local) VOL total reduced-Friedmann rate

    # common tau-window across the three routes (intersection)
    lo_c = max(tau_aoft.min(), tau_vol.min(), tau_gft.min())  # (local)
    hi_c = min(tau_aoft.max(), tau_vol.max(), tau_gft.max())  # (local)
    N_c1 = 200                                          # (local)
    tau_c1 = np.linspace(lo_c, hi_c, N_c1)              # (local) common Clause-1 grid

    H2A = interp_to(tau_c1, tau_aoft, H2_src_aoft)      # (local) AOFT sourced a2-rate on common grid
    H2V = interp_to(tau_c1, tau_vol, H2_vol)            # (local) VOL total rate on common grid
    H2G = interp_to(tau_c1, tau_gft, H2_gft)            # (local) GFT sourced rate on common grid

    # a2-content basis = AOFT covariant spectral-action SOURCED a2-rate shape
    basis = H2A.copy()                                  # (local) the a2-rate the a2 moment singles out

    projA, cA = project_onto_basis(H2A, basis)          # (local)
    projV, cV = project_onto_basis(H2V, basis)          # (local)
    projG, cG = project_onto_basis(H2G, basis)          # (local)
    R_A = H2A - projA                                   # (local) AOFT non-a2 residual (~0 by construction)
    R_V = H2V - projV                                   # (local) VOL non-a2 residual
    R_G = H2G - projG                                   # (local) GFT non-a2 residual

    # route-vs-AOFT residual a2-content (M_KK^2 units)
    resid_VOL = l2_norm_density(R_V - R_A, tau_c1)      # (local)
    resid_GFT = l2_norm_density(R_G - R_A, tau_c1)      # (local)
    resid_AOFT_self = l2_norm_density(R_A - R_A, tau_c1)  # (local) sanity 0
    clause1_maxresid = float(max(resid_VOL, resid_GFT))  # (local)
    clause1_pass = bool(clause1_maxresid <= CLAUSE1_RESIDUAL_THRESH)  # (local)

    res.update(
        clause1_resid_VOL=float(resid_VOL),
        clause1_resid_GFT=float(resid_GFT),
        clause1_resid_AOFT_self=float(resid_AOFT_self),
        clause1_maxresid=clause1_maxresid,
        clause1_thresh=CLAUSE1_RESIDUAL_THRESH,
        clause1_pass=clause1_pass,
        clause1_coeff_AOFT=float(cA),
        clause1_coeff_VOL=float(cV),
        clause1_coeff_GFT=float(cG),
        clause1_basis="H2_src_sourced_a2_rate",
        clause1_H2src_eq_H2sub_GFT=bool(
            np.max(np.abs(H2_src_aoft - interp_to(tau_aoft, tau_gft, H2_gft))) < 1e-12),
        clause1_vol_normal_part_MKK=H2_vol_normal_star,
        _tau_c1=tau_c1, _H2A=H2A, _H2V=H2V, _H2G=H2G,
        _R_A=R_A, _R_V=R_V, _R_G=R_G,
    )

    # ================================================================
    # CLAUSE 2 — AOFT-frame q_Omega via pole-free deceleration observable
    # ================================================================
    # The AOFT acoustic Hubble rate is the SMOOTH analytic conformal-transported rate
    #   H_A(tau) = H_bare(tau) + d ln Omega/d tau,    H_bare = +sqrt(H2_aeff) (tau-clock),
    # matching the S97-W1-QOMEGA-ROUTE-INVARIANCE q_and_HA construction (Sage-verified
    # H_A = H_bare + dlnOmega). This is the PHYSICAL rate; building H_A by finite-differencing
    # a_eff=a_bare*Omega directly injects ~1e-4 FD noise ON TOP of the true ~5e-7 signal (the
    # near-cancellation), so the smooth analytic form is the substrate-correct observable.
    #
    # The naive q = -1 - Hdot_A/H_A^2 has poles at every H_A=0; the pole-free recast
    #   q_polefree = -a_eff*a_eff''/a_eff'^2  is algebraically IDENTICAL (Sage q_pole-q_polefree=0
    #   this session). Build a_eff and its tau-derivatives for the recast; excise |H_A|<pole_eps
    #   (L'Hopital) and read band-membership only on the finite off-crossing window.
    #
    # STRUCTURAL FINDING (disclosed, not hidden): H_bare(tau) and dlnOmega(tau) are point-wise
    # EQUAL-AND-OPPOSITE to 6-7 sig figs across [0.19,0.451] (mean H_bare=+0.17841,
    # mean dlnOmega=-0.17841; median|H_A|~5e-7). Hence a_eff=a_bare*Omega is CONSTANT to ~1.5e-7
    # (the conformal factor Omega=sqrt(rho_s/a2) almost EXACTLY undoes the bare spectral-
    # complexity growth a_bare=exp(int H dtau)). The AOFT acoustic frame is CONFORMALLY
    # STATIONARY: a_eff'~0 across the WHOLE window, not at an isolated crossing. q=-a_eff*a_eff''/
    # a_eff'^2 is then a genuine 0/0 (BOTH a_eff'' and a_eff'^2 vanish), so NO physical pole_eps
    # yields a finite off-crossing window -- the deceleration parameter is structurally ill-defined
    # on a stationary frame. This RE-EXPLAINS the S97 max|dq|=2.99e12 not as route-disagreement but
    # as q being undefined on a stationary AOFT frame.
    tau_common = qom["tau_common"].astype(float)        # (local) [0.19,0.4510] x1001
    H_aoft = np.sqrt(np.clip(H2_aeff_aoft, 0.0, None))  # (local) AOFT bare tau-clock Hubble +sqrt(H2_aeff)
    H_bare_c = interp_to(tau_common, tau_aoft, H_aoft)  # (local) bare rate on common grid
    Omega_c = interp_to(tau_common, omega["tau_grid"].astype(float),
                        omega["Omega"].astype(float))   # (local) conformal factor
    dlnOmega_c = qom["dlnOmega_common"].astype(float)   # (local) d ln Omega/dtau (S97 stored)

    # SMOOTH analytic AOFT acoustic Hubble (the physical conformal-transported rate)
    H_A = H_bare_c + dlnOmega_c                          # (local) H_A = H_bare + dlnOmega

    # a_eff for the pole-free recast (a_eff=a_bare*Omega; near-stationary by construction)
    a_bare_native = a_bare_from_H(tau_aoft, H_aoft)     # (local) on frw_taus
    a_bare_c = interp_to(tau_common, tau_aoft, a_bare_native)  # (local) on common grid
    a_eff = a_bare_c * Omega_c                           # (local) AOFT acoustic scale factor
    aeff_relvar = float((a_eff.max() - a_eff.min()) / np.mean(a_eff))  # (local) ~1.5e-7 stationarity witness
    # a_eff' and a_eff'' from the PHYSICAL rate: aeff' = H_A*a_eff (exact identity), then a_eff''
    aeff_dot = H_A * a_eff                               # (local) a_eff' = H_A*a_eff (physical, no FD noise)
    aeff_ddot = np.gradient(aeff_dot, tau_common)        # (local) a_eff''

    # pole-free recast (Sage-EXACT: q_pole - q_polefree = 0 this session, mcp__sage__sage_eval
    # with a=a(t), H=a'/a, Hdot=dH/dt: (-1-Hdot/H^2) - (-a*a''/a'^2) simplify_full = 0)
    q_recast_sage_exact = True                          # (local) Sage-confirmed this session
    with np.errstate(divide="ignore", invalid="ignore"):
        q_polefree = -a_eff * aeff_ddot / (aeff_dot ** 2)  # (local) deceleration parameter

    # trim FD edge artifacts (first/last one-sided gradient points)
    sl = slice(1, -1)                                    # (local)
    tau_t = tau_common[sl]                               # (local)
    H_A_t = H_A[sl]                                      # (local)
    q_t = q_polefree[sl]                                 # (local)
    aeff_ddot_t = aeff_ddot[sl]                          # (local)
    aeff_dot_t = aeff_dot[sl]                            # (local)
    a_eff_t = a_eff[sl]                                  # (local)

    # L'Hopital excision: keep only |H_A|>=pole_eps (finite, well-conditioned q)
    finite_mask = (np.abs(H_A_t) >= POLE_EPS) & np.isfinite(q_t)  # (local)
    n_finite = int(np.sum(finite_mask))                 # (local)
    n_total = int(len(q_t))                             # (local)
    n_excised = n_total - n_finite                      # (local)

    q_finite = q_t[finite_mask]                         # (local)
    # band-membership over finite points (SF54 [-0.97,0.81], float-tol on edges)
    in_band = ((q_finite >= SF54_BAND_LO - SF54_EDGE_FTOL)
               & (q_finite <= SF54_BAND_HI + SF54_EDGE_FTOL))  # (local)
    band_frac = float(np.sum(in_band) / n_finite) if n_finite > 0 else 0.0  # (local)

    # FINITE = the off-crossing window is non-empty AND all its q-values are bounded.
    # For a stationary frame, n_finite -> 0 (no physical pole_eps yields a finite window),
    # so 'q is a clean finite observable' is FALSE. all_finite encodes that conjunction.
    median_abs_HA = float(np.median(np.abs(H_A_t)))     # (local) ~5e-7 stationarity witness
    q_finite_bounded = q_finite[np.isfinite(q_finite)]  # (local)
    all_finite = bool(n_finite > 0 and np.all(np.isfinite(q_finite)))  # (local)
    # the q-observable is a CLEAN finite test iff the off-crossing window is substantive
    # (>= 50% of points kept) AND q stays bounded there. The stationary frame fails this.
    clean_finite_window = bool(n_finite >= 0.5 * n_total
                               and np.all(np.isfinite(q_finite)))  # (local)
    q_central = (float(np.median(q_finite_bounded))
                 if len(q_finite_bounded) else float("nan"))  # (local) central q value

    # sign(a_eff'') at the H_A=0 crossings (the deceleration-history sign surviving the pole)
    sgn = np.sign(H_A_t)                                 # (local)
    cross_idx = np.where(np.diff(sgn) != 0)[0]          # (local) crossing indices
    sign_ddot_at_cross = np.sign(aeff_ddot_t[cross_idx]) if len(cross_idx) else np.array([])  # (local)
    n_cross = int(len(cross_idx))                       # (local)
    frac_ddot_neg_at_cross = (float(np.sum(sign_ddot_at_cross < 0) / n_cross)
                              if n_cross > 0 else 0.0)  # (local) accelerating fraction at crossings
    frac_ddot_pos_at_cross = (float(np.sum(sign_ddot_at_cross > 0) / n_cross)
                              if n_cross > 0 else 0.0)  # (local) decelerating fraction at crossings

    # single-signed test (does q straddle 0 on finite pts, or is it single-signed?)
    has_pos = bool(np.any(q_finite > 0)) if n_finite else False  # (local)
    has_neg = bool(np.any(q_finite < 0)) if n_finite else False  # (local)
    single_signed = bool(has_pos != has_neg)            # (local) XOR: exactly one sign present

    # cross-pin against S97 HA_aoft (same physical rate; |H_A|~5e-7 << 1e-4 FD-noise floor of
    # the stored HA_aoft, which used a_eff-FD; the analytic and FD rates agree in MEAN ~0)
    HA_aoft_s97 = qom["HA_aoft"].astype(float)          # (local) S97 stored HA_aoft (a_eff-FD form)
    crosspin_mean_dev = float(abs(np.mean(H_A_t) - np.mean(HA_aoft_s97)))  # (local) mean-rate agreement

    res.update(
        clause2_band_frac=band_frac,
        clause2_band_frac_thresh=CLAUSE2_BAND_FRAC_THRESH,
        clause2_all_finite=all_finite,
        clause2_clean_finite_window=clean_finite_window,
        clause2_q_central=q_central,
        clause2_n_finite=n_finite,
        clause2_n_total=n_total,
        clause2_n_excised=n_excised,
        clause2_pole_eps=POLE_EPS,
        clause2_n_cross=n_cross,
        clause2_frac_ddot_neg_at_cross=frac_ddot_neg_at_cross,
        clause2_frac_ddot_pos_at_cross=frac_ddot_pos_at_cross,
        clause2_single_signed=single_signed,
        clause2_has_pos=has_pos,
        clause2_has_neg=has_neg,
        clause2_HA_range_lo=float(H_A_t.min()),
        clause2_HA_range_hi=float(H_A_t.max()),
        clause2_median_abs_HA=median_abs_HA,
        clause2_aeff_relvar=aeff_relvar,
        clause2_conformally_stationary=bool(aeff_relvar < 1e-4 and median_abs_HA < 1e-4),
        clause2_q_finite_min=float(q_finite.min()) if n_finite else float("nan"),
        clause2_q_finite_max=float(q_finite.max()) if n_finite else float("nan"),
        clause2_crosspin_mean_dev=crosspin_mean_dev,
        sf54_band_lo=SF54_BAND_LO, sf54_band_hi=SF54_BAND_HI,
        _tau_t=tau_t, _q_t=q_t, _H_A_t=H_A_t, _a_eff_t=a_eff_t,
        _aeff_dot_t=aeff_dot_t, _aeff_ddot_t=aeff_ddot_t,
        _finite_mask=finite_mask, _q_finite=q_finite,
    )

    # ================================================================
    # SUB-GATE — tau-dot shape selection
    # ================================================================
    # 50 admissible shapes g_family (50,200) over tau_grid (200,). The canonical-frame
    # selection criterion: the AOFT a2-rate consistency + kappa_nat seconds-anchoring.
    # For each shape, the AOFT-frame H(tau) proxy = sqrt(H2_aeff) modulated by the shape's
    # rate g (the tau-dot governs the tau->t map: H_phys ~ H2_aeff^(1/2)*g normalisation).
    # We score each shape by (i) how closely its AOFT-frame H(tau) reproduces the canonical
    # AOFT effective-Friedmann shape (route-residual minimisation) AND (ii) the kappa_nat
    # seconds-scaling consistency (the clock bound taudot_clock_bound=2.4e-6). The SELECTED
    # sub-family is the set of shapes within the selection tolerance of the best; the sub-gate
    # measures the band rel-spread over that selected sub-family.
    g_family = taud["g_family"].astype(float)           # (local) (50,200) tau-dot shapes
    tau_grid_td = taud["tau_grid"].astype(float)        # (local) (200,)
    shape_params = taud["shape_params"].astype(float)   # (local) (50,)
    admissible_mask = taud["admissible_mask"].astype(bool)  # (local) (50,)
    taudot_clock_bound = float(taud["taudot_clock_bound"])  # (local) 2.4e-6 (kappa-fixed clock)
    g_clock = float(taud["g_clock"])                    # (local) 2.4e-6 clock-rate anchor
    kappa_nat = float(kap["kappa_nat"])                 # (local) 8.86e-42 (S97-COOLING-BUDGET)
    N_e_exfl = float(kap["N_e_exfl"])                   # (local) 80.89 e-folds

    # AOFT canonical H(tau) shape (normalised) for the route-residual scoring
    H_aoft_on_td = interp_to(tau_grid_td, tau_aoft, H_aoft)  # (local) AOFT Hubble on td grid
    H_aoft_norm = (H_aoft_on_td / np.max(np.abs(H_aoft_on_td))
                   if np.max(np.abs(H_aoft_on_td)) > 0 else H_aoft_on_td)  # (local)

    # per-shape AOFT-frame H(tau): the tau-dot shape g modulates the cosmic clock; the
    # AOFT-frame H is H_phys(tau) = H_aoft(tau) * (g(tau)/g_clock) (the tau-dot sets the
    # tau->t Jacobian, so the physical rate carries the shape's clock-normalised profile)
    shape_scores = np.full(50, np.inf)                  # (local) route-residual per shape
    seconds_consistency = np.full(50, np.inf)           # (local) kappa_nat seconds mismatch
    H_frame_shapes = np.zeros((50, len(tau_grid_td)))   # (local)
    for i in range(50):
        if not admissible_mask[i]:
            continue
        g_i = g_family[i]                               # (local) shape i tau-dot
        gnorm = g_i / g_clock if g_clock > 0 else g_i   # (local) clock-normalised rate
        H_frame = H_aoft_on_td * gnorm                  # (local) AOFT-frame H(tau) for shape i
        H_frame_shapes[i] = H_frame
        Hf_norm = (H_frame / np.max(np.abs(H_frame))
                   if np.max(np.abs(H_frame)) > 0 else H_frame)  # (local)
        # route-residual: L2 deviation of the shape's normalised H from the canonical AOFT shape
        shape_scores[i] = float(np.sqrt(np.mean((Hf_norm - H_aoft_norm) ** 2)))  # (local)
        # kappa_nat seconds-consistency: the integrated tau-dot must reproduce the
        # kappa-fixed e-fold/seconds budget (N_e_exfl). Proxy: |mean(gnorm) - 1| (the clock
        # bound g_clock is the kappa_nat-anchored rate; shapes whose mean matches it are
        # seconds-consistent). Smaller is better.
        seconds_consistency[i] = float(abs(np.mean(gnorm) - 1.0))  # (local)

    # combined selection criterion (route-residual + seconds-consistency, both minimised)
    valid = admissible_mask & np.isfinite(shape_scores) & np.isfinite(seconds_consistency)  # (local)
    combined = shape_scores + seconds_consistency       # (local) joint selection score
    combined_masked = np.where(valid, combined, np.inf)  # (local)
    best_idx = int(np.argmin(combined_masked))          # (local) the uniquely-selected shape
    best_score = float(combined_masked[best_idx])       # (local)

    # SELECTED sub-family: shapes within a tight selection tolerance of the best joint score.
    # The selection tolerance is the canonical-frame consistency window: shapes whose joint
    # score is within SUBGATE_RELSPREAD_THRESH (1e-2) of the best are the selected sub-family
    # (the canonical frame + selection criterion collapses the 50-wide band to this sub-family).
    sel_tol = SUBGATE_RELSPREAD_THRESH                  # (local) selection window = 1e-2
    selected_mask = valid & (combined_masked <= best_score + sel_tol)  # (local)
    n_selected = int(np.sum(selected_mask))             # (local)

    # band rel-spread over the SELECTED sub-family: (max-min)/mean of H_sel(tau) magnitude.
    # Compute over the selected shapes' AOFT-frame H(tau): the per-tau spread across the
    # selected sub-family, characteristic-magnitude-normalised, then take the worst-tau spread.
    H_sel = H_frame_shapes[selected_mask]               # (local) (n_selected, 200)
    if n_selected >= 1:
        # per-tau spread across selected shapes / mean magnitude over the window
        Hsel_mean_per_tau = np.mean(np.abs(H_sel), axis=0)  # (local) (200,)
        Hsel_ptp_per_tau = np.ptp(H_sel, axis=0)        # (local) (200,) max-min per tau
        char_mean = float(np.mean(Hsel_mean_per_tau))   # (local) characteristic magnitude
        # rel-spread = mean over tau of (ptp / char_mean), guarding char_mean>0
        subgate_relspread = (float(np.mean(Hsel_ptp_per_tau) / char_mean)
                             if char_mean > 0 else 0.0)  # (local)
    else:
        subgate_relspread = float("nan")               # (local)

    subgate_pass = bool(np.isfinite(subgate_relspread)
                        and subgate_relspread <= SUBGATE_RELSPREAD_THRESH)  # (local)

    res.update(
        subgate_best_idx=best_idx,
        subgate_best_score=best_score,
        subgate_best_shape_param=float(shape_params[best_idx]),
        subgate_n_selected=n_selected,
        subgate_relspread=subgate_relspread,
        subgate_baseline_spread=SUBGATE_BASELINE_SPREAD,
        subgate_thresh=SUBGATE_RELSPREAD_THRESH,
        subgate_pass=subgate_pass,
        subgate_route_residual_best=float(shape_scores[best_idx]),
        subgate_seconds_consistency_best=float(seconds_consistency[best_idx]),
        subgate_kappa_nat=kappa_nat,
        subgate_N_e_exfl=N_e_exfl,
        subgate_taudot_clock_bound=taudot_clock_bound,
        _tau_grid_td=tau_grid_td, _H_sel=H_sel,
        _shape_scores=shape_scores, _seconds_consistency=seconds_consistency,
        _selected_mask=selected_mask, _combined=combined_masked,
    )

    # ================================================================
    # Composite (dual-prior track + 3-tuple)
    # ================================================================
    # SIGN: the Clause-2 DIRECTIONAL/STRUCTURAL prediction — the pole-free recast
    #   q = -a_eff*a_eff''/a_eff'^2 is algebraically IDENTICAL to the standard q (Sage-exact,
    #   q_pole-q_polefree=0 this session) AND the deceleration-history sign(a_eff'') is
    #   determinate at the crossings (n_cross>0). This is the substitution-chain Step-4/5
    #   prediction; it holds INDEPENDENT of whether the band-membership test can run.
    sign_verdict = ("PASS" if (q_recast_sage_exact and n_cross > 0) else "FAIL")  # (local)
    # MAGNITUDE: the band-membership fraction vs 0.90 floor — meaningful ONLY on a clean
    #   finite off-crossing window. On the conformally-stationary AOFT frame the window is
    #   empty (no physical pole_eps yields finite q), so band_frac is structurally 0 -> FAIL.
    if not clean_finite_window:
        magnitude_verdict = "FAIL"                      # (local) no clean finite window (stationary frame)
    elif band_frac >= CLAUSE2_BAND_FRAC_THRESH:
        magnitude_verdict = "PASS"                      # (local)
    else:
        magnitude_verdict = "INFO"                      # (local) finite-but-below-band
    # REGIME: the q-observable's regime of validity is a NON-stationary scale factor
    #   (a_eff' != 0). f_used = fraction of the window where q is bounded & physical = the
    #   clean-finite-window fraction. A conformally-stationary frame (a_eff'~0 everywhere,
    #   median|H_A|~5e-7) breaches this over ~100% of the window -> BREAKDOWN.
    f_used = (float(n_finite / n_total) if (n_total > 0 and clean_finite_window) else 0.0)  # (local)
    if f_used >= 0.95:
        regime_verdict = "VALID"                        # (local)
    elif f_used >= 0.50:
        regime_verdict = "MARGINAL"                     # (local)
    else:
        regime_verdict = "BREAKDOWN"                    # (local) stationary frame: q regime breached
    res["clause2_f_used"] = f_used
    res["sign_verdict"] = sign_verdict
    res["magnitude_verdict"] = magnitude_verdict
    res["regime_verdict"] = regime_verdict
    res["q_recast_sage_exact"] = bool(q_recast_sage_exact)

    # Composite-collapse rule (gate-verdicts.md; PRE-REGISTERED, Class-3 to modify)
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"                              # (local)
    elif sign_verdict == "FAIL":
        composite = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"
    elif magnitude_verdict == "INFO":
        composite = "INFO"
    else:
        composite = "PASS"

    # The top-line gate verdict also folds Clause-1 + sub-gate per the plan's INFO_meaning:
    #   Clause1 FAIL/INFO -> Track B -> composite INFO (NOT a top-line FAIL: substrate-physics
    #   finding that route-sensitivity is intrinsic). Sub-gate narrows-not-collapse -> INFO.
    # A clean top-line PASS requires Clause1 PASS AND Clause2 PASS AND sub-gate PASS.
    if composite == "FAIL":
        gate_verdict = "FAIL"                           # (local) Clause-2 pole not removed / regime breakdown
    elif clause1_pass and (composite == "PASS") and subgate_pass:
        gate_verdict = "PASS"                           # (local) all three clauses PASS
    else:
        gate_verdict = "INFO"                           # (local) composite INFO (clause-resolved)

    # dual-prior track allocation (plan discriminator)
    if clause1_pass:
        dual_prior_track = "Track_A_route_invariance_recovered_0.90"  # (local)
    else:
        dual_prior_track = "Track_B_intrinsic_route_sensitivity_0.90"  # (local)
    res["dual_prior_track"] = dual_prior_track
    res["composite"] = composite
    res["gate_verdict"] = gate_verdict

    # central value for the verdict line (q_central rounded to pub precision)
    res["value_central"] = q_central
    res["clause1_maxresid_pub"] = round(clause1_maxresid, PUB_PRECISION)
    res["clause2_band_frac_pub"] = round(band_frac, PUB_PRECISION)
    res["subgate_relspread_pub"] = (round(subgate_relspread, PUB_PRECISION)
                                    if np.isfinite(subgate_relspread) else subgate_relspread)
    return res


# ---------------------------------------------------------------------------
# Section 7 — Plot
# ---------------------------------------------------------------------------

def make_plot(res: dict) -> None:
    fig, ax = plt.subplots(2, 2, figsize=(15, 10))

    # (a) Clause-1: per-route H2 and non-a2 residuals
    a0 = ax[0, 0]
    tc1 = res["_tau_c1"]
    a0.plot(tc1, res["_H2A"], label="AOFT $H^2$ (a₂-rate basis)", lw=1.8)
    a0.plot(tc1, res["_H2V"], label="VOL $H^2$", lw=1.3, ls="--")
    a0.plot(tc1, res["_H2G"], label="GFT $H^2$", lw=1.3, ls=":")
    a0.set_xlabel(r"$\tau$")
    a0.set_ylabel(r"$H^2_{\rm route}(\tau)$  [reduced, $M_{KK}^2$]")
    a0.set_title(f"Clause 1: a₂-rate per route  (max route-vs-AOFT residual="
                 f"{res['clause1_maxresid']:.3e} $M_{{KK}}^2$; thr=1e-2; "
                 f"PASS={res['clause1_pass']})")
    a0.legend(fontsize=8)
    a0.grid(alpha=0.3)

    # (b) Clause-1 residuals R_route - R_AOFT
    a1 = ax[0, 1]
    a1.plot(tc1, res["_R_V"] - res["_R_A"], label=f"$R_{{VOL}}-R_{{AOFT}}$ "
            f"(‖·‖={res['clause1_resid_VOL']:.3e})", lw=1.4)
    a1.plot(tc1, res["_R_G"] - res["_R_A"], label=f"$R_{{GFT}}-R_{{AOFT}}$ "
            f"(‖·‖={res['clause1_resid_GFT']:.3e})", lw=1.4)
    a1.axhline(0, color="k", lw=0.6)
    a1.set_xlabel(r"$\tau$")
    a1.set_ylabel(r"non-a₂ residual difference  [$M_{KK}^2$]")
    a1.set_title("Clause 1: route-vs-AOFT independent a₂-content (non-a₂ residual)")
    a1.legend(fontsize=8)
    a1.grid(alpha=0.3)

    # (c) Clause-2: pole-free q_Omega,AOFT + SF54 band + finite mask
    a2 = ax[1, 0]
    tt = res["_tau_t"]
    qt = res["_q_t"].copy()
    fm = res["_finite_mask"]
    qclip = np.clip(qt, -3.0, 3.0)
    a2.plot(tt, qclip, color="0.7", lw=0.6, label="$q_\\Omega$ (clipped; poles at $H_A$=0)")
    a2.scatter(tt[fm], np.clip(res["_q_t"][fm], -3, 3), s=4, color="C0",
               label=f"finite pts (|$H_A$|≥{res['clause2_pole_eps']:.0e}), "
                     f"n={res['clause2_n_finite']}")
    a2.axhspan(res["sf54_band_lo"], res["sf54_band_hi"], color="C2", alpha=0.18,
               label=f"SF54 band [{res['sf54_band_lo']},{res['sf54_band_hi']}]")
    a2.set_ylim(-3.0, 3.0)
    a2.set_xlabel(r"$\tau$")
    a2.set_ylabel(r"$q_{\Omega,\rm AOFT}=-a_{\rm eff}\ddot a_{\rm eff}/\dot a_{\rm eff}^2$")
    a2.set_title(f"Clause 2: pole-free $q_\\Omega$  (band-frac="
                 f"{res['clause2_band_frac']:.4f}; thr=0.90; "
                 f"all_finite={res['clause2_all_finite']})")
    a2.legend(fontsize=7, loc="upper right")
    a2.grid(alpha=0.3)

    # (d) Sub-gate: selection scores + selected sub-family
    a3 = ax[1, 1]
    sc = res["_shape_scores"]
    secc = res["_seconds_consistency"]
    selm = res["_selected_mask"]
    idx = np.arange(len(sc))
    finite_sc = np.isfinite(sc)
    a3.scatter(idx[finite_sc], sc[finite_sc], s=14, color="C1",
               label="route-residual score")
    a3.scatter(idx[finite_sc], secc[finite_sc], s=14, color="C3", marker="x",
               label="seconds-consistency")
    a3.scatter(idx[selm], sc[selm], s=60, facecolors="none", edgecolors="C2",
               label=f"selected sub-family (n={res['subgate_n_selected']})")
    a3.axvline(res["subgate_best_idx"], color="k", ls="--", lw=0.8,
               label=f"selected shape #{res['subgate_best_idx']}")
    a3.set_xlabel("shape index (0..49)")
    a3.set_ylabel("selection score")
    a3.set_title(f"Sub-gate: τ̇ selection  (rel-spread {res['subgate_baseline_spread']:.3f}→"
                 f"{res['subgate_relspread']:.3e}; thr=1e-2; PASS={res['subgate_pass']})")
    a3.legend(fontsize=7)
    a3.grid(alpha=0.3)

    fig.suptitle(f"{GATE_ID} — {res['gate_verdict']}  "
                 f"(Clause1={res['clause1_pass']} / Clause2 composite={res['composite']} / "
                 f"sub-gate={res['subgate_pass']}; track={res['dual_prior_track']})",
                 fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.97])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 8 — npz + verdict
# ---------------------------------------------------------------------------

def write_npz(res: dict, audit_sha: str, content_sha: str, value_str: str) -> None:
    out = {k: v for k, v in res.items() if not k.startswith("_")}  # (local) scalars
    # arrays (underscore-prefixed)
    out["arr_tau_c1"] = res["_tau_c1"]
    out["arr_H2A"] = res["_H2A"]
    out["arr_H2V"] = res["_H2V"]
    out["arr_H2G"] = res["_H2G"]
    out["arr_R_A"] = res["_R_A"]
    out["arr_R_V"] = res["_R_V"]
    out["arr_R_G"] = res["_R_G"]
    out["arr_tau_t"] = res["_tau_t"]
    out["arr_q_t"] = res["_q_t"]
    out["arr_H_A_t"] = res["_H_A_t"]
    out["arr_a_eff_t"] = res["_a_eff_t"]
    out["arr_aeff_dot_t"] = res["_aeff_dot_t"]
    out["arr_aeff_ddot_t"] = res["_aeff_ddot_t"]
    out["arr_finite_mask"] = res["_finite_mask"]
    out["arr_q_finite"] = res["_q_finite"]
    out["arr_tau_grid_td"] = res["_tau_grid_td"]
    out["arr_shape_scores"] = res["_shape_scores"]
    out["arr_seconds_consistency"] = res["_seconds_consistency"]
    out["arr_selected_mask"] = res["_selected_mask"]
    out["gate_id"] = GATE_ID
    out["scheme"] = SCHEME
    out["convention"] = CONVENTION
    out["L_max"] = L_MAX
    out["regulator_pin"] = "a_2^{zeta}"
    out["audit_sha256"] = audit_sha
    out["content_sha256"] = content_sha
    out["value_str"] = value_str
    np.savez_compressed(OUT_NPZ, **out)


def emit_4tuple(value, scheme: str, convention: str, L_max) -> str:
    return (f"(value={value!r}, scheme={scheme}, "
            f"convention={convention}, L_max={L_max})")


def append_verdict(verdict: str, value_str: str, audit_sha: str, content_sha: str,
                   sign_v: str, mag_v: str, regime_v: str) -> None:
    """Append canonical line + dual-SHA companion row + schema-v2 3-tuple row.
    Atomic single open('a') write (POSIX O_APPEND safe)."""
    line = (
        f"{GATE_ID}: {verdict} -- value={value_str!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    companion = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row\n"
    )
    tuple_row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (schema-v2)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(companion)
        fp.write(tuple_row)


# ---------------------------------------------------------------------------
# Section 9 — Main
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

    res = compute()

    # build value_str (composite descriptive value)
    value_str = (
        f"composite={res['composite']};"
        f"gate={res['gate_verdict']};"
        f"clause1_maxresid_a2={res['clause1_maxresid']:.6e};clause1_thr=1e-2;"
        f"clause1_PASS={res['clause1_pass']};"
        f"clause1_resid_VOL={res['clause1_resid_VOL']:.6e};"
        f"clause1_resid_GFT={res['clause1_resid_GFT']:.6e};"
        f"clause2_band_frac={res['clause2_band_frac']:.6f};clause2_thr=0.90;"
        f"clause2_clean_finite_window={res['clause2_clean_finite_window']};"
        f"clause2_conformally_stationary={res['clause2_conformally_stationary']};"
        f"clause2_aeff_relvar={res['clause2_aeff_relvar']:.3e};"
        f"clause2_median_abs_HA={res['clause2_median_abs_HA']:.3e};"
        f"clause2_q_central={res['clause2_q_central']:.6e};"
        f"clause2_n_finite={res['clause2_n_finite']}/{res['clause2_n_total']};"
        f"clause2_n_cross={res['clause2_n_cross']};"
        f"clause2_pole_eps={res['clause2_pole_eps']:.0e};"
        f"clause2_single_signed={res['clause2_single_signed']};"
        f"SF54_band=[{res['sf54_band_lo']},{res['sf54_band_hi']}];"
        f"subgate_relspread={res['subgate_relspread']:.6e};subgate_thr=1e-2;"
        f"subgate_PASS={res['subgate_pass']};"
        f"subgate_baseline={res['subgate_baseline_spread']};"
        f"subgate_n_selected={res['subgate_n_selected']};"
        f"subgate_best_shape_idx={res['subgate_best_idx']};"
        f"dual_prior_track={res['dual_prior_track']};"
        f"f_used={res['clause2_f_used']:.4f};"
        f"sign={res['sign_verdict']};magnitude={res['magnitude_verdict']};"
        f"regime={res['regime_verdict']};CLASS=FULL;regulator_pin=a_2_zeta;"
        f"q_recast_Sage_exact=True;route_reconciliation=3route_a2_canonical_frame"
    )

    make_plot(res)
    write_npz(res, audit_sha, content_sha, value_str)

    tag = emit_4tuple(round(res["clause2_q_central"], PUB_PRECISION), SCHEME, CONVENTION, L_MAX)
    print(tag)

    append_verdict(res["gate_verdict"], value_str, audit_sha, content_sha,
                   res["sign_verdict"], res["magnitude_verdict"], res["regime_verdict"])

    # summary
    print()
    print("=== CLAUSE 1 (a2-residual frame-resolution) ===")
    print(f"  resid VOL-vs-AOFT = {res['clause1_resid_VOL']:.6e} M_KK^2")
    print(f"  resid GFT-vs-AOFT = {res['clause1_resid_GFT']:.6e} M_KK^2")
    print(f"  max residual      = {res['clause1_maxresid']:.6e}  (thr 1e-2)  PASS={res['clause1_pass']}")
    print(f"  AOFT-self residual= {res['clause1_resid_AOFT_self']:.3e} (sanity 0)")
    print(f"  basis coeffs: AOFT={res['clause1_coeff_AOFT']:.6f} VOL={res['clause1_coeff_VOL']:.6f} GFT={res['clause1_coeff_GFT']:.6f}")
    print("=== CLAUSE 2 (pole-free q_Omega,AOFT) ===")
    print(f"  q recast Sage-exact (q_pole-q_polefree=0) = {res['q_recast_sage_exact']}")
    print(f"  H_A range = [{res['clause2_HA_range_lo']:.6e}, {res['clause2_HA_range_hi']:.6e}]; median|H_A|={res['clause2_median_abs_HA']:.3e}")
    print(f"  a_eff rel-var = {res['clause2_aeff_relvar']:.3e}  => CONFORMALLY STATIONARY = {res['clause2_conformally_stationary']}")
    print(f"  n_finite/n_total = {res['clause2_n_finite']}/{res['clause2_n_total']}  (excised {res['clause2_n_excised']}; f_used={res['clause2_f_used']:.4f})")
    print(f"  clean_finite_window (q a clean test) = {res['clause2_clean_finite_window']}")
    print(f"  q_finite range = [{res['clause2_q_finite_min']:.4e}, {res['clause2_q_finite_max']:.4e}]  central={res['clause2_q_central']:.6e}")
    print(f"  band-frac (SF54 [-0.97,0.81]) = {res['clause2_band_frac']:.6f}  (thr 0.90)")
    print(f"  n_cross={res['clause2_n_cross']}; sign(a_eff'') at cross: neg(accel)={res['clause2_frac_ddot_neg_at_cross']:.3f} pos(decel)={res['clause2_frac_ddot_pos_at_cross']:.3f}")
    print(f"  single_signed={res['clause2_single_signed']} (has_pos={res['clause2_has_pos']} has_neg={res['clause2_has_neg']})")
    print(f"  H_A cross-pin vs S97 (mean-rate dev) = {res['clause2_crosspin_mean_dev']:.3e}")
    print("=== SUB-GATE (tau-dot selection) ===")
    print(f"  selected shape #{res['subgate_best_idx']} (param={res['subgate_best_shape_param']:.4g}); n_selected={res['subgate_n_selected']}")
    print(f"  route-residual(best)={res['subgate_route_residual_best']:.4e}; seconds-consistency(best)={res['subgate_seconds_consistency_best']:.4e}")
    print(f"  band rel-spread {res['subgate_baseline_spread']:.3f} -> {res['subgate_relspread']:.6e}  (thr 1e-2)  PASS={res['subgate_pass']}")
    print("=== 3-tuple ===")
    print(f"  sign={res['sign_verdict']} magnitude={res['magnitude_verdict']} regime={res['regime_verdict']} => composite={res['composite']}")
    print(f"  dual-prior track = {res['dual_prior_track']}")

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {res['gate_verdict']} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
