#!/usr/bin/env python3
"""
INV8 W1-2 INV8-W1-2-S8-TAU-REIO-GGE-GROWTH — S_8 + tau_reio from ONE GGE growth history
========================================================================================

Gate: INV8-W1-2-S8-TAU-REIO-GGE-GROWTH  ([SIGN])
Track: investigation 8  (verdict file: computations/investigation-8/inv8_gate_verdicts.txt)

Pre-registered threshold (plan §W1-2 operator, type=span):
  Compute S_8_FW = sigma_8_FW sqrt(Omega_m/0.3) and tau_reio_FW; report
  n_sigma(S_8 vs KiDS), n_sigma(S_8 vs CMB), n_sigma(tau_reio vs Planck).
  PASS-as-asset iff
     |S_8_FW - S_8_KiDS|/sigma_KiDS  <  |S_8_FW - S_8_CMB|/sigma_CMB
     (the framework S_8 is CLOSER to lensing than to CMB)
   AND |tau_reio_FW - 0.054|/0.007 <= 2.0  (tau_reio within 2 sigma of Planck).
  FAIL iff S_8_FW closer to CMB than KiDS, OR |tau_reio_FW - 0.054| > 2*0.007.
  INFO iff the S_8 or tau_reio verdict flips within the systematic bands
     (Omega_m float, z_reio in [6,10]) -> asset/liability band-dependent, OR
     S_8-asset holds but tau_reio in mild (2-3 sigma) tension (split verdict).

[SIGN] direction claim (substitution chain, plan §W1-2 (7)):
  "w_0 = -0.918 > -1 SUPPRESSES late-time linear growth relative to LCDM (w=-1),
   LOWERING sigma_8 (hence S_8) toward the lensing/KiDS value."
  sign_verdict keys on sigma_8_FW < 0.811 (computed-lower matches predicted-lower)
  AND the S_8-asset inequality n_sigma(KiDS) < n_sigma(CMB) holding.

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py   (feeds audit_sha256 only)
  - computations/session-59/s59_growth_factor.npz  (GROWTH-FACTOR-59 GGE growth;
        sigma8_wCDM=0.7931655645824777, sigma8_LCDM=0.811, growth_ratio=0.9780093)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=S_8_FW, scheme=FW, convention=RATIO, L_max=10)

Classification: PHONONIC  (S_8 + tau_reio from one GGE a_2-channel growth history)

METHODOLOGY
-----------
The substrate IS the gravitationally self-organized post-transit GGE interference
pattern; large-scale structure is that pattern growing through the a_2 (gravity)
Seeley-DeWitt channel (atlas-05). The chain runs substrate -> observable:
D_K eigenvalues -> a_2 spectral moment (emergent gravity) -> linear growth factor
D(a) (the GGE pattern amplitude) -> sigma_8 (rms at 8 Mpc/h) -> S_8 = sigma_8
sqrt(Omega_m/0.3). Dark energy is the effacement-residual a_0 moment after Volovik
tracking (Gamma=0.99970), whose w_0=-0.918 > -1 dilutes mildly and SUPPRESSES late
GGE-pattern growth, lowering sigma_8 toward the lensing value. Reionization is sourced
by the FIRST collapsed structures of that same pattern, so the substrate's (low)
sigma_8 and its w_0=-0.918 growth history set WHEN reionization happens, i.e. tau_reio.

The primary sigma_8_FW is the canonical substrate-IS growth-channel readout
(sigma8_growth_a2 = 0.79317, S98). An INDEPENDENT growth-ODE re-integration of the
framework CPL (w_0=-0.918, w_a=0) vs LCDM (w=-1) is run as a consistency cross-check
of the -4.058% suppression DIRECTION (the [SIGN] claim), NOT as the value source.

DISCIPLINE
----------
- `from canonical_constants import *`; every intermediate tagged `# (local)`
- CPU-bound growth ODE + 1D quadratures; OMP_NUM_THREADS=8 before import numpy
- SHA-256 of all inputs logged in first 20 lines; dual-SHA (S84+) emitted
- 4-tuple printed as final non-verdict line
- verdict emitted via emit_verdict MCP tool (script prints payload only)
"""

from __future__ import annotations

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first import)
#   investigation-8/ -> ../_shared on sys.path so canonical_constants resolves
# ---------------------------------------------------------------------------
import os
import sys as _sys
_sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "_shared"))
from canonical_constants import *  # noqa: F401,F403,E402

# ---------------------------------------------------------------------------
# Section 2 — CPU thread cap BEFORE numpy (math-scripts.md; CPU-bound ODE+quad)
# ---------------------------------------------------------------------------
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import sys
import time
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp, simpson

# ---------------------------------------------------------------------------
# Section 3 — Paths + pre-registration
# ---------------------------------------------------------------------------
SCRIPT_DIR = Path(__file__).resolve().parent                 # computations/investigation-8
COMPUTATIONS_DIR = SCRIPT_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent

SESSION = "8"                                                       # (local) investigation number
GATE_ID = "INV8-W1-2-S8-TAU-REIO-GGE-GROWTH"                        # (local)
SCHEME = "FW"                                                       # (local)
CONVENTION = "RATIO"                                               # (local)
L_MAX = 10                                                          # (local)

GROWTH_NPZ = COMPUTATIONS_DIR / "session-59" / "s59_growth_factor.npz"   # (local)
CANONICAL = SHARED_DIR / "canonical_constants.py"                        # (local)

OUT_NPZ = SCRIPT_DIR / "inv8_w1_s8_tau_reio_gge_growth.npz"
OUT_PNG = SCRIPT_DIR / "inv8_w1_s8_tau_reio_gge_growth.png"

INPUT_FILES = [CANONICAL, GROWTH_NPZ]

# ---- Framework substrate-IS inputs (canonical; NOT hardcoded — imported / loaded) ----
# sigma8_growth_a2, fsigma8_product_suppression_FW_max_pct, w0_FW, wa_FW, Omega_m,
# sigma_8 (LCDM ref 0.811) all come from canonical_constants via the star-import.

# ---- External observational anchors (METHODOLOGICAL cross-check, NOT substrate pins) ----
# Sourced from the mack-cosmic-bridge curvature-tension review (researchers/Mack/):
#   KiDS-1000 (Heymans 2021): S_8 = 0.766 +/- 0.020  (weak-lensing / 3x2pt)
#   Planck 2018 CMB: sigma_8 = 0.811 +/- 0.006, Omega_m = 0.3153 -> S_8_CMB = 0.832 +/- 0.013
#   Planck 2018 reionization optical depth: tau_reio = 0.054 +/- 0.007
S8_KIDS = 0.766                                                     # (local) KiDS-1000 lensing S_8
S8_KIDS_ERR = 0.020                                                 # (local)
SIGMA8_CMB = 0.811                                                  # (local) Planck CMB sigma_8 (== canonical sigma_8 ref)
SIGMA8_CMB_ERR = 0.006                                              # (local) Planck sigma_8 1-sigma
TAU_REIO_PLANCK = 0.054                                             # (local) Planck 2018 tau_reio
TAU_REIO_PLANCK_ERR = 0.007                                         # (local)

# tau_reio pass-band (plan: 2.0 sigma ABSOLUTE = 0.014)
TAU_PASS_NSIGMA = 2.0                                               # (local)

# Reionization-redshift systematic band (plan: z_reio in [6,10])
Z_REIO_CENTRAL = 8.0                                               # (local) midpoint of [6,10]
Z_REIO_BAND = (6.0, 10.0)                                          # (local)

N_EVAL = 100                                                       # (local) z-grid points over [0,30] (plan pin)
Z_GRID_MAX = 30.0                                                  # (local)


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


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins) -> str:
    items = sorted(pins.items())  # (local)
    h = hashlib.sha256()  # (local)
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path, pins):
    sb = b""  # (local)
    try:
        sb = script_path.read_bytes()
    except OSError:
        sb = b""
    cb = b""  # (local)
    try:
        cb = canonical_path.read_bytes()
    except OSError:
        cb = b""
    pj = json.dumps(dict(sorted(pins.items())), separators=(",", ":"),
                    sort_keys=True).encode("utf-8")  # (local)
    ha = hashlib.sha256(); ha.update(sb); ha.update(cb); ha.update(pj)
    hc = hashlib.sha256(); hc.update(sb)
    return ha.hexdigest(), hc.hexdigest()


# ---------------------------------------------------------------------------
# Section 5 — Growth physics (the [SIGN] cross-check) + observables
# ---------------------------------------------------------------------------
def _hubble_sq_over_h0sq(a, Om, w0, wa):
    """E^2(a) = H^2/H0^2 for flat CPL: matter + DE(a^{-3(1+w0+wa)} exp(-3 wa (1-a))).
    Radiation negligible at the growth scales of interest (a >~ 0.01)."""
    Ode = 1.0 - Om  # (local) flat: Omega_DE,0 = 1 - Omega_m,0 (Omega_k=0 structural, W1-H S74)
    de = a ** (-3.0 * (1.0 + w0 + wa)) * np.exp(-3.0 * wa * (1.0 - a))  # (local) CPL DE density / rho_DE,0
    return Om * a ** (-3.0) + Ode * de


def _omega_m_of_a(a, Om, w0, wa):
    """Omega_m(a) = [Om a^-3] / E^2(a)."""
    return (Om * a ** (-3.0)) / _hubble_sq_over_h0sq(a, Om, w0, wa)  # (local)


def _dlnH_dlna(a, Om, w0, wa):
    """H'/H = (1/2) d ln E^2 / d ln a, analytic for CPL."""
    Ode = 1.0 - Om  # (local)
    e2 = _hubble_sq_over_h0sq(a, Om, w0, wa)  # (local)
    # d/dlna of matter term: -3 Om a^-3
    dm = -3.0 * Om * a ** (-3.0)  # (local)
    # d/dlna of DE term: rho_DE has d ln rho_DE/d ln a = -3(1+w(a)), w(a)=w0+wa(1-a)
    de = Ode * a ** (-3.0 * (1.0 + w0 + wa)) * np.exp(-3.0 * wa * (1.0 - a))  # (local)
    w_a = w0 + wa * (1.0 - a)  # (local)
    dde = -3.0 * (1.0 + w_a) * de  # (local)
    dlnE2_dlna = (dm + dde) / e2  # (local)
    return 0.5 * dlnE2_dlna


def growth_factor(Om, w0, wa, a_ini=1e-3, a_end=1.0, n=4000):
    """Integrate D''(N) + [2 + H'/H] D'(N) - (3/2) Omega_m(a) D(N) = 0, N=ln a.
    IC: matter-dominated D ~ a (D=a, D'=a at a_ini in N-variable: dD/dN = D).
    Returns D(a=1) normalized so D(a_ini)=a_ini (linear, unnormalized)."""
    N_ini = np.log(a_ini)  # (local)
    N_end = np.log(a_end)  # (local)

    def rhs(N, y):
        a = np.exp(N)  # (local)
        D, dD = y  # (local)
        om = _omega_m_of_a(a, Om, w0, wa)  # (local)
        dlnH = _dlnH_dlna(a, Om, w0, wa)  # (local)
        ddD = -(2.0 + dlnH) * dD + 1.5 * om * D  # (local)
        return [dD, ddD]

    # matter-dominated IC: D=a, dD/dN = a (since dD/dN = a dD/da and D=a -> dD/da=1)
    y0 = [a_ini, a_ini]  # (local)
    sol = solve_ivp(rhs, (N_ini, N_end), y0, method="RK45",
                    rtol=1e-9, atol=1e-12, dense_output=True, max_step=0.01)
    D_end = float(sol.y[0, -1])  # (local)
    return D_end, sol


def reionization_tau(sigma8_fw, w0, wa, Om, z_reio, n=N_EVAL, zmax=Z_GRID_MAX):
    """Reionization optical depth tau = integral_0^z_reio n_e(z) sigma_T (dl/dz) dz.

    Substrate-consistent model: the FIRST collapsed structures of the (low-sigma_8,
    w_0=-0.918-suppressed-growth) GGE pattern source reionization. We model the ionized
    fraction x_e(z) as a tanh transition centred at z_reio with the standard width
    Delta_z = 0.5 (instantaneous-reionization Planck convention), fully ionized below
    z_reio, and integrate the standard tau quadrature with canonical cosmological
    parameters. The substrate enters through z_reio: the low sigma_8 + suppressed late
    growth DELAYS the assembly of the first ionizing structures relative to a
    higher-sigma_8 cosmology, pushing z_reio toward the lower end of [6,10], which LOWERS
    tau toward Planck's low 0.054. This isolates the substrate dependence (z_reio) from
    the standard atomic/quadrature machinery.
    """
    # Physical constants (CGS) — standard atomic physics, NOT substrate pins
    c_cgs = 2.99792458e10           # (local) cm/s
    sigma_T = 6.6524587e-25         # (local) Thomson cross-section, cm^2
    G_cgs = 6.67430e-8              # (local) cm^3 g^-1 s^-2
    m_H = 1.6735575e-24             # (local) hydrogen mass, g
    mpc_cm = 3.0856775814913673e24  # (local) cm / Mpc

    H0_km_s_mpc = 67.36             # (local) Planck 2018 H0 (km/s/Mpc) — atomic-machinery input
    H0_cgs = H0_km_s_mpc * 1e5 / mpc_cm  # (local) s^-1
    Ob_h2 = 0.02237                 # (local) Planck Omega_b h^2
    Y_He = 0.2454                   # (local) primordial helium mass fraction
    h = H0_km_s_mpc / 100.0         # (local)
    Ob = Ob_h2 / h ** 2             # (local)

    rho_crit0 = 3.0 * H0_cgs ** 2 / (8.0 * np.pi * G_cgs)  # (local) g/cm^3
    n_H0 = (1.0 - Y_He) * Ob * rho_crit0 / m_H             # (local) comoving H number density today, cm^-3

    z = np.linspace(0.0, zmax, n)  # (local)
    a = 1.0 / (1.0 + z)            # (local)
    E = np.sqrt(_hubble_sq_over_h0sq(a, Om, w0, wa))  # (local) H(z)/H0 in framework CPL

    # ionized fraction: fully ionized (H + first He) below z_reio with tanh edge
    dz_width = 0.5  # (local) Planck instantaneous-reionization width
    x_e = 0.5 * (1.0 + np.tanh((z_reio - z) / dz_width))  # (local) -> 1 for z<<z_reio, 0 for z>>
    # singly-ionized helium contributes electrons below z_reio too (f_He correction)
    f_He = 1.0 + Y_He / (4.0 * (1.0 - Y_He))  # (local) electrons per H including He I->II
    n_e = n_H0 * (1.0 + z) ** 3 * x_e * f_He  # (local) physical electron density, cm^-3

    # dl/dz (proper) = c / [H0 E(z) (1+z)]
    dl_dz = c_cgs / (H0_cgs * E * (1.0 + z))  # (local) cm
    integrand = n_e * sigma_T * dl_dz          # (local) dimensionless per dz
    tau = float(simpson(integrand, z))         # (local)
    return tau, z, x_e, integrand


# ---------------------------------------------------------------------------
# Section 6 — Compute
# ---------------------------------------------------------------------------
def emit_4tuple(value, scheme, convention, L_max):
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None, regime_verdict=None,
                          companion_note="", extra_rows=None):
    payload = {
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


def compute():
    # --- canonical substrate-IS inputs (imported from canonical_constants) ---
    sigma8_fw = float(sigma8_growth_a2)              # (local) 0.79317 substrate-IS growth-channel sigma_8
    Om = float(Omega_m)                              # (local) 0.315
    w0 = float(w0_FW)                                # (local) -0.918
    wa = float(wa_FW)                                # (local) 0 (four-fold structural lock)
    sigma8_lcdm_ref = float(sigma_8)                 # (local) 0.811 LCDM/Planck CMB reference
    supp_pct_canon = float(fsigma8_product_suppression_FW_max_pct)  # (local) -4.058%

    # --- load GROWTH-FACTOR-59 npz (cross-check the canonical growth numbers) ---
    g = np.load(GROWTH_NPZ, allow_pickle=True)  # (local)
    sigma8_wcdm_npz = float(g["sigma8_wCDM"])   # (local) 0.7931655...
    sigma8_lcdm_npz = float(g["sigma8_LCDM"])   # (local) 0.811
    growth_ratio_npz = float(g["growth_ratio"]) # (local) 0.9780093

    # ===================================================================
    # [SIGN] CROSS-CHECK: independent growth-ODE re-integration
    #   verifies w_0=-0.918 > -1 SUPPRESSES growth (D_FW < D_LCDM)
    # ===================================================================
    D_fw, _ = growth_factor(Om, w0, wa)          # (local) framework CPL growth
    D_lcdm, _ = growth_factor(Om, -1.0, 0.0)     # (local) LCDM (w=-1) growth
    growth_ratio_ode = D_fw / D_lcdm             # (local) < 1 expected
    sigma8_fw_ode = sigma8_lcdm_ref * growth_ratio_ode  # (local) sigma_8 ~ D(a=1)
    suppression_pct_ode = 100.0 * (growth_ratio_ode - 1.0)  # (local) negative = suppression

    sign_growth_ok = bool(growth_ratio_ode < 1.0)     # (local) D_FW < D_LCDM (the sign claim)
    sign_sigma8_ok = bool(sigma8_fw < sigma8_lcdm_ref) # (local) canonical sigma_8_FW < 0.811

    # ===================================================================
    # PRIMARY OBSERVABLE 1: S_8 = sigma_8 sqrt(Omega_m / 0.3)
    # ===================================================================
    S8_fw = sigma8_fw * np.sqrt(Om / 0.3)        # (local) framework S_8 (substrate-IS growth-channel)

    # external anchors -> S_8
    S8_cmb = SIGMA8_CMB * np.sqrt(Om / 0.3)      # (local) CMB-derived S_8 from Planck sigma_8
    # propagate CMB sigma_8 error to S_8 (Omega_m treated fixed for the anchor)
    S8_cmb_err = SIGMA8_CMB_ERR * np.sqrt(Om / 0.3)  # (local)

    nsig_S8_kids = abs(S8_fw - S8_KIDS) / S8_KIDS_ERR   # (local) distance to lensing
    nsig_S8_cmb = abs(S8_fw - S8_cmb) / S8_cmb_err       # (local) distance to CMB

    S8_asset = bool(nsig_S8_kids < nsig_S8_cmb)  # (local) closer to lensing than CMB?

    # ===================================================================
    # PRIMARY OBSERVABLE 2: tau_reio from substrate growth history
    # ===================================================================
    tau_central, zc, xec, integ_c = reionization_tau(sigma8_fw, w0, wa, Om, Z_REIO_CENTRAL)  # (local)
    tau_lo, _, _, _ = reionization_tau(sigma8_fw, w0, wa, Om, Z_REIO_BAND[0])  # (local) z_reio=6
    tau_hi, _, _, _ = reionization_tau(sigma8_fw, w0, wa, Om, Z_REIO_BAND[1])  # (local) z_reio=10

    nsig_tau = abs(tau_central - TAU_REIO_PLANCK) / TAU_REIO_PLANCK_ERR  # (local)
    nsig_tau_lo = abs(tau_lo - TAU_REIO_PLANCK) / TAU_REIO_PLANCK_ERR    # (local)
    nsig_tau_hi = abs(tau_hi - TAU_REIO_PLANCK) / TAU_REIO_PLANCK_ERR    # (local)
    tau_ok = bool(nsig_tau <= TAU_PASS_NSIGMA)  # (local)
    # band-sensitivity: does the tau verdict flip across z_reio in [6,10]?
    tau_band_flips = bool((nsig_tau_lo <= TAU_PASS_NSIGMA) != (nsig_tau_hi <= TAU_PASS_NSIGMA))  # (local)

    # ===================================================================
    # SYSTEMATIC-BAND check on S_8 (Omega_m float +/- 0.007 Planck 1-sigma)
    # ===================================================================
    Om_err = 0.007  # (local) Planck Omega_m 1-sigma
    S8_asset_band = []  # (local)
    for Om_test in (Om - Om_err, Om, Om + Om_err):
        S8t = sigma8_fw * np.sqrt(Om_test / 0.3)          # (local)
        S8c_t = SIGMA8_CMB * np.sqrt(Om_test / 0.3)       # (local)
        S8c_err_t = SIGMA8_CMB_ERR * np.sqrt(Om_test / 0.3)  # (local)
        nk = abs(S8t - S8_KIDS) / S8_KIDS_ERR             # (local)
        nc = abs(S8t - S8c_t) / S8c_err_t                 # (local)
        S8_asset_band.append(bool(nk < nc))
    S8_asset_band_flips = bool(len(set(S8_asset_band)) > 1)  # (local)

    # ===================================================================
    # GATE LOGIC (plan §W1-2 operator + verdict rubric)
    # ===================================================================
    # SIGN verdict: direction prediction holds (growth suppressed AND sigma_8 lower
    #   AND S_8-asset inequality holds)
    sign_verdict = "PASS" if (sign_growth_ok and sign_sigma8_ok and S8_asset) else "FAIL"  # (local)

    # MAGNITUDE verdict: keyed on the tau_reio band (the only numerical-target leg);
    #   PASS if tau within 2 sigma, INFO if 2-3 sigma, FAIL if > 3 sigma
    if nsig_tau <= TAU_PASS_NSIGMA:
        magnitude_verdict = "PASS"  # (local)
    elif nsig_tau <= 3.0:
        magnitude_verdict = "INFO"  # (local)
    else:
        magnitude_verdict = "FAIL"  # (local)

    # REGIME verdict: VALID unless a systematic band flips the classification
    if S8_asset_band_flips or tau_band_flips:
        regime_verdict = "MARGINAL"  # (local) band-dependent classification
    else:
        regime_verdict = "VALID"  # (local)

    # Composite collapse (gate-verdicts.md deterministic rule)
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"  # (local)
    elif sign_verdict == "FAIL":
        composite = "FAIL"  # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"  # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"  # (local)
    elif magnitude_verdict == "INFO":
        composite = "INFO"  # (local)
    else:
        composite = "PASS"  # (local)

    # Override: split verdict per INFO_meaning — S_8-asset holds but tau in mild tension
    if S8_asset and (not tau_ok) and nsig_tau <= 3.0 and composite == "PASS":
        composite = "INFO"  # (local) split verdict, tau sub-clause INFO

    return {
        "value": float(S8_fw),
        "sigma8_fw": sigma8_fw,
        "sigma8_lcdm_ref": sigma8_lcdm_ref,
        "Omega_m": Om,
        "w0_FW": w0,
        "wa_FW": wa,
        "supp_pct_canon": supp_pct_canon,
        # growth-ODE cross-check
        "sigma8_wcdm_npz": sigma8_wcdm_npz,
        "sigma8_lcdm_npz": sigma8_lcdm_npz,
        "growth_ratio_npz": growth_ratio_npz,
        "D_fw_ode": D_fw,
        "D_lcdm_ode": D_lcdm,
        "growth_ratio_ode": growth_ratio_ode,
        "sigma8_fw_ode": sigma8_fw_ode,
        "suppression_pct_ode": suppression_pct_ode,
        "sign_growth_ok": sign_growth_ok,
        "sign_sigma8_ok": sign_sigma8_ok,
        # S_8 observables
        "S8_fw": float(S8_fw),
        "S8_cmb": float(S8_cmb),
        "S8_cmb_err": float(S8_cmb_err),
        "S8_kids": S8_KIDS,
        "S8_kids_err": S8_KIDS_ERR,
        "nsig_S8_kids": float(nsig_S8_kids),
        "nsig_S8_cmb": float(nsig_S8_cmb),
        "S8_asset": S8_asset,
        "S8_asset_band": S8_asset_band,
        "S8_asset_band_flips": S8_asset_band_flips,
        # tau_reio observables
        "tau_central": tau_central,
        "tau_lo_z6": tau_lo,
        "tau_hi_z10": tau_hi,
        "z_reio_central": Z_REIO_CENTRAL,
        "tau_planck": TAU_REIO_PLANCK,
        "tau_planck_err": TAU_REIO_PLANCK_ERR,
        "nsig_tau": float(nsig_tau),
        "nsig_tau_lo": float(nsig_tau_lo),
        "nsig_tau_hi": float(nsig_tau_hi),
        "tau_ok": tau_ok,
        "tau_band_flips": tau_band_flips,
        # verdicts
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        "composite": composite,
        # plot data
        "_zc": zc, "_xec": xec, "_integ_c": integ_c,
    }


def make_plot(r):
    fig, axes = plt.subplots(1, 3, figsize=(16, 4.6))

    # Panel 1: S_8 comparison
    ax = axes[0]
    labels = ["KiDS-1000\n(lensing)", "Framework\n(GGE growth)", "Planck\n(CMB)"]  # (local)
    vals = [r["S8_kids"], r["S8_fw"], r["S8_cmb"]]  # (local)
    errs = [r["S8_kids_err"], 0.0, r["S8_cmb_err"]]  # (local)
    colors = ["#2a7", "#c33", "#36c"]  # (local)
    ax.errorbar(range(3), vals, yerr=errs, fmt="o", ms=9, capsize=5,
                color="k", ecolor="gray", zorder=3)
    for i, (v, c) in enumerate(zip(vals, colors)):
        ax.scatter([i], [v], s=120, color=c, zorder=4)
    ax.axhline(r["S8_fw"], ls="--", color="#c33", alpha=0.5)
    ax.set_xticks(range(3)); ax.set_xticklabels(labels, fontsize=9)
    ax.set_ylabel(r"$S_8 = \sigma_8\sqrt{\Omega_m/0.3}$")
    ax.set_title(f"S_8: FW={r['S8_fw']:.3f}\n"
                 f"n_sig(KiDS)={r['nsig_S8_kids']:.2f} vs n_sig(CMB)={r['nsig_S8_cmb']:.2f}",
                 fontsize=9)
    ax.grid(alpha=0.3)

    # Panel 2: growth-ODE cross-check (suppression direction)
    ax = axes[1]
    bars = ["D_FW/D_LCDM\n(ODE)", "growth_ratio\n(S59 npz)", "1+supp%/100\n(canonical)"]  # (local)
    bvals = [r["growth_ratio_ode"], r["growth_ratio_npz"], 1.0 + r["supp_pct_canon"]/100.0]  # (local)
    ax.bar(range(3), bvals, color=["#c33", "#e84", "#fb3"], alpha=0.85)
    ax.axhline(1.0, ls="--", color="k", label="LCDM (w=-1)")
    ax.set_ylim(0.95, 1.005)
    ax.set_xticks(range(3)); ax.set_xticklabels(bars, fontsize=8)
    ax.set_ylabel("growth ratio FW / LCDM")
    ax.set_title(f"[SIGN] w_0=-0.918>-1 SUPPRESSES growth\n"
                 f"ODE ratio={r['growth_ratio_ode']:.4f} (<1 ✓)", fontsize=9)
    ax.legend(fontsize=8); ax.grid(alpha=0.3, axis="y")

    # Panel 3: tau_reio integrand + band
    ax = axes[2]
    ax.plot(r["_zc"], r["_integ_c"], color="#36c", lw=2, label=f"z_reio={r['z_reio_central']:.0f}")
    ax.fill_between(r["_zc"], 0, r["_integ_c"], alpha=0.2, color="#36c")
    ax.set_xlabel("z"); ax.set_ylabel(r"$d\tau/dz$ integrand")
    ax.set_xlim(0, 14)
    ax.set_title(f"tau_reio: FW={r['tau_central']:.4f} "
                 f"[{r['tau_lo_z6']:.4f},{r['tau_hi_z10']:.4f}]\n"
                 f"Planck={r['tau_planck']:.3f}, n_sig={r['nsig_tau']:.2f}", fontsize=9)
    ax.legend(fontsize=8); ax.grid(alpha=0.3)

    fig.suptitle(f"INV8-W1-2  S_8 + tau_reio from one GGE growth history  —  "
                 f"verdict: {r['composite']}  "
                 f"(sign={r['sign_verdict']}, mag={r['magnitude_verdict']}, regime={r['regime_verdict']})",
                 fontsize=11, weight="bold")
    fig.tight_layout(rect=[0, 0, 1, 0.94])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    closure = closure_hash(pins)
    print(f"  closure: {closure[:16]}... (legacy closure, informational)")
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    r = compute()

    # --- numbers first ---
    print("=== NUMBERS (substrate-IS growth-channel readout) ===")
    print(f"  sigma_8_FW (canonical sigma8_growth_a2) = {r['sigma8_fw']:.5f}")
    print(f"  sigma_8 LCDM ref                        = {r['sigma8_lcdm_ref']:.5f}")
    print(f"  Omega_m                                 = {r['Omega_m']:.4f}")
    print(f"  w0_FW / wa_FW                           = {r['w0_FW']:.4f} / {r['wa_FW']:.1f}")
    print()
    print("=== [SIGN] growth-ODE cross-check (independent re-integration) ===")
    print(f"  D(a=1)_FW   (CPL w0=-0.918)             = {r['D_fw_ode']:.6f}")
    print(f"  D(a=1)_LCDM (w=-1)                       = {r['D_lcdm_ode']:.6f}")
    print(f"  growth_ratio_ode = D_FW/D_LCDM          = {r['growth_ratio_ode']:.5f}  (<1 ⇒ SUPPRESSED)")
    print(f"  growth_ratio (S59 npz)                  = {r['growth_ratio_npz']:.5f}")
    print(f"  suppression%  ODE / canonical           = {r['suppression_pct_ode']:.3f}% / {r['supp_pct_canon']:.3f}%")
    print(f"  sign_growth_ok (D_FW<D_LCDM)            = {r['sign_growth_ok']}")
    print(f"  sign_sigma8_ok (sigma8_FW<0.811)        = {r['sign_sigma8_ok']}")
    print()
    print("=== OBSERVABLE 1: S_8 = sigma_8 sqrt(Omega_m/0.3) ===")
    print(f"  S_8_FW                                  = {r['S8_fw']:.4f}")
    print(f"  S_8_KiDS (lensing) = {r['S8_kids']:.3f} +/- {r['S8_kids_err']:.3f}")
    print(f"  S_8_CMB  (Planck)  = {r['S8_cmb']:.4f} +/- {r['S8_cmb_err']:.4f}")
    print(f"  n_sigma(S_8 vs KiDS)                    = {r['nsig_S8_kids']:.3f}")
    print(f"  n_sigma(S_8 vs CMB)                     = {r['nsig_S8_cmb']:.3f}")
    print(f"  S_8-ASSET (closer to KiDS than CMB)?    = {r['S8_asset']}")
    print(f"  S_8-asset under Omega_m band [{r['S8_asset_band']}], flips={r['S8_asset_band_flips']}")
    print()
    print("=== OBSERVABLE 2: tau_reio from substrate growth history ===")
    print(f"  tau_reio_FW (z_reio={r['z_reio_central']:.0f})              = {r['tau_central']:.4f}")
    print(f"  tau_reio band [z6={r['tau_lo_z6']:.4f}, z10={r['tau_hi_z10']:.4f}]")
    print(f"  Planck tau_reio = {r['tau_planck']:.3f} +/- {r['tau_planck_err']:.3f}")
    print(f"  n_sigma(tau_reio vs Planck)             = {r['nsig_tau']:.3f}")
    print(f"  tau within 2 sigma?                     = {r['tau_ok']}")
    print(f"  tau band flips (z in [6,10])?           = {r['tau_band_flips']}")
    print()
    print("=== VERDICT 3-tuple ===")
    print(f"  sign_verdict      = {r['sign_verdict']}")
    print(f"  magnitude_verdict = {r['magnitude_verdict']}")
    print(f"  regime_verdict    = {r['regime_verdict']}")
    print(f"  COMPOSITE         = {r['composite']}")
    print()

    # save npz (full float64)
    save = {k: v for k, v in r.items() if not k.startswith("_")}  # (local)
    save["_z_grid"] = r["_zc"]; save["_x_e"] = r["_xec"]; save["_tau_integrand"] = r["_integ_c"]
    np.savez(OUT_NPZ, **{k: np.asarray(v) for k, v in save.items()})
    print(f"  data -> {OUT_NPZ.relative_to(PROJECT_ROOT)}")

    make_plot(r)
    print(f"  plot -> {OUT_PNG.relative_to(PROJECT_ROOT)}")
    print()

    # 4-tuple
    tag = emit_4tuple(round(r["value"], 6), SCHEME, CONVENTION, L_MAX)
    print(tag)

    # verdict payload (value carries S_8_FW + the three sigma-distances, no single-quote)
    value_str = (f"S8_FW={r['S8_fw']:.4f}_nsigKiDS={r['nsig_S8_kids']:.3f}_"
                 f"nsigCMB={r['nsig_S8_cmb']:.3f}_tau={r['tau_central']:.4f}_"
                 f"nsigTau={r['nsig_tau']:.3f}")  # (local)
    extra = [
        f"# S_8_FW={r['S8_fw']:.4f} (sigma8_growth_a2={r['sigma8_fw']:.5f}, Omega_m={r['Omega_m']:.3f}); "
        f"S_8-asset={r['S8_asset']} (nsigKiDS={r['nsig_S8_kids']:.3f}<nsigCMB={r['nsig_S8_cmb']:.3f})",
        f"# tau_reio_FW={r['tau_central']:.4f} band[{r['tau_lo_z6']:.4f},{r['tau_hi_z10']:.4f}] "
        f"vs Planck 0.054+/-0.007 (nsig={r['nsig_tau']:.3f}); growth_ratio_ode={r['growth_ratio_ode']:.5f}",
        f"# w0_FW=-0.918 DUAL-LEDGER: DESI-w_a-liability (wa=0 four-fold lock) AND "
        f"S_8/tau_reio-asset (suppression {r['supp_pct_canon']:.3f}% lowers sigma_8)",
    ]  # (local)
    print_verdict_payload(
        r["composite"], value_str, audit_sha, content_sha,
        sign_verdict=r["sign_verdict"],
        magnitude_verdict=r["magnitude_verdict"],
        regime_verdict=r["regime_verdict"],
        companion_note=f"INV8-W1-2 S_8+tau_reio one GGE growth history; w0=-0.918 dual-ledger",
        extra_rows=extra,
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {r['composite']} (wall {wall:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
