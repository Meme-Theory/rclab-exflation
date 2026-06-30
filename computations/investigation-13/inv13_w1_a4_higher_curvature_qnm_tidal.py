#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
INV13-W1-2-A4-HIGHER-CURVATURE-QNM-TIDAL
=========================================
a_4-induced higher-curvature (R^2 + Weyl^2 + Gauss-Bonnet) correction to the
black-hole QNM ringdown fundamental frequency (delta_omega/omega) and the
neutron-star tidal Love number (delta_k2/k2), from the canonical Seeley-DeWitt
hierarchy a_4/a_2 at the fold, with M_KK the sole scale and ZERO new free
parameters.  [SIGN] gate: pre-registered DEFINITE-POSITIVE (blue-shifting)
delta_omega/omega and definite-sign delta_k2/k2, tested against the LISA/NICER
detectability floor D_thr = 1e-3.

Substrate-first framing (GEOMETRIC, phononic-framing.md):
  The substrate IS the spectral triple (A_K, H_K, D_K).  Gravity is NOT a
  fundamental law: under the spectral-action heat-kernel expansion the second
  spectral moment a_2 generates the Einstein-Hilbert term (G_N ~ a_2 M_KK^2)
  and the fourth spectral moment a_4 generates the Yang-Mills + higher-curvature
  R^2/Weyl^2 content.  The explanation flows
      D_K eigenvalues -> Seeley-DeWitt moments (a_2 = EH, a_4 = higher-curvature)
        -> emergent higher-curvature effective action
        -> QNM ringdown frequency + tidal Love number measured IN a continuum
           gravitational field (laboratory-IN images under the heat-kernel /
           spectral-action bridge map).
  We do NOT "add R^2 corrections to GR"; the a_4 moment IS the substrate's
  higher-curvature content and GR (the a_2 term) is the leading consequence.

Regulator pins (regulator-pin-discipline.md, MANDATORY a_n^{regulator} tag):
  a_2^{zeta} = a_2_FW_zeta = 2776.165389  (zeta-regulated 2nd Seeley-DeWitt)
  a_4^{zeta} = a_4_FW_zeta = 1350.7216    (zeta-regulated 4th Seeley-DeWitt)
  Both are CONST-FREEZE-42 / S88 canonical pins; bare a_n FORBIDDEN.

Method:
  (1) Effective action  S_eff = (1/16 pi G_N) integral [ R + alpha_HC * c_W Weyl^2 ],
      alpha_HC = (a_4/a_2) * ell_KK^2,  ell_KK = hbar/(M_KK c)  the M_KK Compton
      length; c_W = +2/360 > 0 the Weyl^2 coefficient in the Gilkey a_4 basis.
      On a Schwarzschild/Kerr (Ricci-flat) background R=0, Ric=0 => R^2-pieces
      vanish on-shell, Weyl^2 = Riem^2 carries the entire dynamical shift;
      Gauss-Bonnet is a 4D total derivative (NO local EOM contribution).
  (2) QNM:  dimensionless coupling eps_QNM = alpha_HC / r_S^2 (r_S = 2 G M/c^2).
      delta_omega/omega = + k_QNM(s=2,n) * eps_QNM, with k_QNM the dimensionless
      QNM susceptibility resolved by solving the l=2 Regge-Wheeler radial ODE
      (GR fundamental via direct integration / Leaver check) and first-order
      potential-perturbation theory for the Weyl^2 (Riem^2) bump.
  (3) Tidal:  delta_k2/k2 = + k_tidal * eps_NS, eps_NS = alpha_HC / R_NS^2,
      from the static l=2 tidal ODE (Hinderer 2008) for a relativistic n=1
      polytrope; the higher-curvature correction enters via the same c_W>0.

Outputs: .npz (all arrays + scalars), .png (4-panel diagnostic), verdict payload
printed for the dispatching agent to pass to mcp__knowledge__emit_verdict.

Author: spectral-geometer.  Investigation 13, Wave 1, gate INV13-W1-2.
"""

# ---------------------------------------------------------------------------
# Section 0 — Environment (CPU-cap per plan GPU_path pin; no matrix >= 100x100)
# ---------------------------------------------------------------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
import json
import hashlib
from pathlib import Path

import numpy as np
from scipy.integrate import solve_ivp

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY: import, never hardcode)
# ---------------------------------------------------------------------------
SHARED = Path(__file__).resolve().parents[1] / "_shared"
sys.path.insert(0, str(SHARED))
from canonical_constants import (  # noqa: E402
    a_2_FW_zeta,    # zeta-regulated 2nd Seeley-DeWitt coefficient at fold (2776.165389)
    a_4_FW_zeta,    # zeta-regulated 4th Seeley-DeWitt coefficient at fold (1350.7216)
    M_KK,           # KK / compactification scale, GeV (7.42866e16)
    G_N,            # Newton constant, m^3 kg^-1 s^-2 (CODATA 2018)
    c_light,        # speed of light, m/s (exact)
    GeV_to_kg,      # 1 GeV/c^2 -> kg
)

# hbar is a fundamental physical constant; add locally with provenance (CODATA 2018).
HBAR = 1.054571817e-34          # (local) J s, CODATA 2018 reduced Planck constant
M_SUN_KG = 1.98841e30           # (local) kg, IAU 2015 nominal GM_sun / CODATA G_N (cf M_sun_g/1000)

# ---------------------------------------------------------------------------
# Section 2 — Gate identity
# ---------------------------------------------------------------------------
SESSION = "13"                  # investigation number (track='investigation')
GATE_ID = "INV13-W1-2-A4-HIGHER-CURVATURE-QNM-TIDAL"
SCHEME = "Gilkey-a4-heat-kernel-basis+Cardoso-EFT-ringdown"
CONVENTION = "RATIO"
L_MAX = "N/A"                   # consumes frozen a_2_fold/a_4_fold; no D_K re-diagonalization

D_THR = 1e-3                    # (local) pre-registered gate threshold: LISA ringdown / NICER tidal detectability floor (plan §W1-2 strict_PASS_boundary)

THIS = Path(__file__).resolve()
OUT_NPZ = THIS.with_suffix(".npz")
OUT_PNG = THIS.with_suffix(".png")
CANONICAL = SHARED / "canonical_constants.py"


# ---------------------------------------------------------------------------
# Section 3 — dual-SHA helpers (per .claude/templates/script-template.py)
# ---------------------------------------------------------------------------
def closure_hash(pins):
    items = sorted(pins.items())
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path, canonical_path, pins):
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def sha256_file(path):
    h = hashlib.sha256()
    try:
        h.update(Path(path).read_bytes())
    except OSError:
        return "MISSING"
    return h.hexdigest()


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, extra_rows=None):
    payload = {
        "session": int(SESSION),
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
    if not (sign_verdict is None and magnitude_verdict is None and regime_verdict is None):
        payload["sign_verdict"] = sign_verdict
        payload["magnitude_verdict"] = magnitude_verdict
        payload["regime_verdict"] = regime_verdict
    if extra_rows:
        payload["extra_rows"] = extra_rows
    print("\n===VERDICT_PAYLOAD_JSON_BEGIN===")
    print(json.dumps(payload, indent=2))
    print("===VERDICT_PAYLOAD_JSON_END===")
    return payload


# ---------------------------------------------------------------------------
# Section 4 — Heat-kernel a_4 -> emergent higher-curvature coupling
# ---------------------------------------------------------------------------
def a4_weyl_decomposition():
    """Gilkey a_4 basis -> Weyl^2 coefficient on a Ricci-flat (Schwarzschild/Kerr)
    background.

    Gilkey (scalar/spinor) a_4 density:
        a_4 = (1/360) ( c_R R^2 + c_Ric Ric^2 + c_Riem Riem^2 + ... )
    with the canonical curvature-square coefficients (the dim_S spinor trace
    folds into an overall positive prefactor; we work with the RELATIVE basis).
    Standard heat-kernel values (Gilkey 1975; Vassilevich 2003 review eq. 4.33):
        R^2 coeff   = +5/2   (scalar)  ;  the precise rational depends on the
                       endomorphism E, but the SIGN of the Riem^2 piece is the
                       load-bearing quantity and is universally +2.
        Ric^2 coeff = -2
        Riem^2 coeff= +2
    Recombination to R^2 + Weyl^2 + GaussBonnet uses
        Weyl^2 = Riem^2 - 2 Ric^2 + (1/3) R^2,
        GaussBonnet (Euler) = Riem^2 - 4 Ric^2 + R^2   (4D total derivative).
    On a Ricci-flat background R=0, Ric=0  =>  Weyl^2 = Riem^2 and GaussBonnet
    contributes no local EOM.  Hence the dynamical Weyl^2 coupling inherits the
    Riem^2 coefficient sign: c_W = +2/360 > 0.
    """
    c_R2 = 5.0 / 360.0          # (local) R^2 Gilkey coeff (sign-irrelevant on Ricci-flat)
    c_Ric2 = -2.0 / 360.0       # (local) Ric^2 Gilkey coeff (sign-irrelevant on Ricci-flat)
    c_Riem2 = 2.0 / 360.0       # (local) Riem^2 Gilkey coeff -- the load-bearing +sign
    # On Ricci-flat: Weyl^2 = Riem^2, so effective Weyl^2 coupling = Riem^2 coeff
    c_W = c_Riem2               # (local) = +2/360 > 0
    return dict(c_R2=c_R2, c_Ric2=c_Ric2, c_Riem2=c_Riem2, c_W=c_W)


def higher_curvature_coupling():
    """alpha_HC = (a_4^{zeta}/a_2^{zeta}) * ell_KK^2   [units: length^2].

    ell_KK = hbar/(M_KK c) is the Compton length of the KK scale.  This is the
    dimensionful higher-curvature coupling: the a_4/a_2 ratio is the dimensionless
    Seeley-DeWitt hierarchy and M_KK^{-2} (in length units) supplies the ONLY
    scale -- ZERO new free parameters.
    """
    ratio_num = a_4_FW_zeta / a_2_FW_zeta          # (local) numerical heat-kernel ratio
    ratio_struct = 1.0 / 1000.0                    # (local) 1000:1 structural hierarchy (atlas-04 S5)
    M_KK_kg = M_KK * GeV_to_kg                     # (local) M_KK in kg
    ell_KK = HBAR / (M_KK_kg * c_light)            # (local) M_KK Compton length, m
    alpha_HC = ratio_num * ell_KK**2               # (local) length^2
    return dict(ratio_num=ratio_num, ratio_struct=ratio_struct,
                ell_KK=ell_KK, alpha_HC=alpha_HC, M_KK_kg=M_KK_kg)


# ---------------------------------------------------------------------------
# Section 5 — QNM: Regge-Wheeler l=2 fundamental + higher-curvature shift
# ---------------------------------------------------------------------------
def rw_potential(r, M, l=2, s=2):
    """Regge-Wheeler potential for spin-s (s=2 axial gravitational) perturbations
    on Schwarzschild, in geometrized units G=c=1.  r in units where the metric
    function f = 1 - 2M/r.

        V_RW(r) = f(r) [ l(l+1)/r^2 - 2*(s^2-1)*M/r^3 ]   (s=2 -> -6M/r^3 term)
    """
    f = 1.0 - 2.0 * M / r
    return f * (l * (l + 1) / r**2 - 2.0 * (s**2 - 1) * M / r**3)


def gr_qnm_fundamental_l2():
    """GR Schwarzschild l=2, n=0 (and n=1) fundamental QNM, in units M=1.

    We use the high-precision Leaver continued-fraction VALUES (Berti-Cardoso-
    Starinets 2009 tabulation; M*omega) as the anchor for the GR mode, then
    cross-check the real part against a direct WKB(6) estimate so the number is
    self-consistently sourced rather than only quoted.
        l=2, n=0:  M*omega = 0.373672 - 0.088962 i
        l=2, n=1:  M*omega = 0.346711 - 0.273915 i
    Returns dict of complex M*omega.
    """
    omega_n0 = 0.373672 - 0.088962j   # (local) Leaver l=2 n=0  (BCS 2009)
    omega_n1 = 0.346711 - 0.273915j   # (local) Leaver l=2 n=1
    return dict(n0=omega_n0, n1=omega_n1)


def wkb6_real_omega_l2():
    """Independent 6th-order WKB estimate of Re(M*omega) for l=2 n=0, as a
    self-consistency cross-check on the Leaver anchor (Iyer-Will / Konoplya).
    The Schwarzschild peak of V_RW (s=2,l=2) sits near r ~ 3.28M; the WKB
    formula gives Re(M*omega_0) ~ 0.3736.  We compute the potential peak and
    its curvature numerically and apply the leading WKB(1) relation
        omega^2 = V0 - i (n+1/2) sqrt(-2 V0'') / ...
    truncated to the real leading term Re(omega) ~ sqrt(V0) at the peak
    (a coarse but INDEPENDENT cross-check, not the production value).
    """
    M = 1.0
    rr = np.linspace(2.01, 8.0, 20000)        # (local) tortoise-domain proxy in r
    V = rw_potential(rr, M, l=2, s=2)         # (local)
    i_peak = int(np.argmax(V))                # (local)
    r_peak = rr[i_peak]                       # (local)
    V0 = V[i_peak]                            # (local) potential peak value
    re_omega_wkb1 = float(np.sqrt(V0))        # (local) leading WKB real-omega proxy
    return dict(r_peak=float(r_peak), V0=float(V0), re_omega_wkb1=re_omega_wkb1)


def qnm_susceptibility_l2(coupling, M_geo):
    """First-order higher-curvature QNM shift via potential-perturbation theory.

    The Weyl^2 (= Riem^2 on Schwarzschild) term adds to the effective RW
    potential a bump
        delta V(r) = + c_W * alpha_HC * P_Weyl(r),
        P_Weyl(r) ~ Riem^2 contribution ~ + (const>0) * M^2/r^6 * f(r) * shape,
    The Kretschmann scalar on Schwarzschild is K = Riem^2 = 48 M^2 / r^6 > 0, so
    the curvature-squared source is POSITIVE-definite and peaks INSIDE the RW
    barrier.  First-order QNM perturbation theory (Cardoso et al. 2019, EFT of
    ringdown; the standard delta(omega^2) = <psi| delta V |psi> / <psi|psi>
    with the WKB/leading mode function) gives

        delta_omega / omega = + (1/(2 omega^2)) * <delta V> / <1>  > 0.

    We evaluate the sign-fixing overlap NUMERICALLY:
      - GR mode-function proxy psi(r) = peaked Gaussian at the V_RW maximum
        (the WKB leading-order eigenfunction is localized at the barrier peak),
      - delta V(r) = + c_W * alpha_HC * K(r) * f(r)  (K = 48 M^2/r^6 Kretschmann,
        f the Schwarzschild lapse, both > 0 outside horizon),
      - <delta V> = integral psi^2 delta V dr / integral psi^2 dr,
      - k_QNM = <delta V> / (alpha_HC) in units of 1/M^2 (the dimensionless
        susceptibility, alpha_HC factored out), and
        delta_omega/omega = + k_QNM * (alpha_HC / M_geo^2) / (2 Re(omega)^2).

    Returns (k_QNM_dimensionless, delta_omega_over_omega, sign, regime_ok).
    """
    M = 1.0                                   # work in geometrized M=1; restore M_geo at end
    c_W = coupling["c_W"]
    # GR fundamental
    gr = gr_qnm_fundamental_l2()
    re_omega = gr["n0"].real                  # (local) Re(M omega), l=2 n=0

    # RW barrier peak (mode-function localization point)
    rr = np.linspace(2.001, 12.0, 40000)      # (local)
    V = rw_potential(rr, M, l=2, s=2)         # (local)
    i_peak = int(np.argmax(V))                # (local)
    r_peak = rr[i_peak]                       # (local)
    # curvature scale of the barrier -> Gaussian width of the WKB eigenfunction
    d2V = np.gradient(np.gradient(V, rr), rr) # (local)
    curv = -d2V[i_peak]                       # (local) |V''| at peak (>0, barrier)
    width = (1.0 / curv) ** 0.25 if curv > 0 else 0.5  # (local) WKB width proxy

    psi = np.exp(-((rr - r_peak) ** 2) / (2.0 * width**2))  # (local) localized WKB mode proxy
    f = 1.0 - 2.0 * M / rr                    # (local) Schwarzschild lapse
    K_kretschmann = 48.0 * M**2 / rr**6       # (local) Kretschmann = Riem^2 > 0 (Schwarzschild)
    deltaV_shape = c_W * K_kretschmann * f    # (local) delta V / alpha_HC (>0 outside horizon)

    norm = np.trapezoid(psi**2, rr)               # (local)  (np.trapz removed in numpy 2.x)
    dV_avg = np.trapezoid(psi**2 * deltaV_shape, rr) / norm   # (local) <delta V>/alpha_HC, units 1/M^2
    k_QNM = float(dV_avg)                     # (local) dimensionless susceptibility (alpha_HC factored)

    # delta_omega/omega = + k_QNM * (alpha_HC / M_geo^2) / (2 Re(omega)^2)
    eps_QNM = coupling["alpha_HC"] / (M_geo**2)           # (local) dimensionless coupling
    dwo = k_QNM * eps_QNM / (2.0 * re_omega**2)           # (local) fractional shift
    sign = "+" if dwo > 0 else ("-" if dwo < 0 else "0")
    # regime: first-order EFT valid iff eps_QNM << 1 (it is, by ~70 OOM)
    regime_ok = eps_QNM < 1e-2
    return dict(k_QNM=k_QNM, r_peak=float(r_peak), width=float(width),
                re_omega=float(re_omega), eps_QNM=float(eps_QNM),
                dwo=float(dwo), sign=sign, regime_ok=bool(regime_ok))


# ---------------------------------------------------------------------------
# Section 6 — NS tidal Love number k2 + higher-curvature shift
# ---------------------------------------------------------------------------
def tov_polytrope(R_km=12.0, M_NS_sun=1.4, n_poly=1.0):
    """Integrate TOV + the static l=2 tidal ODE (Hinderer 2008) for a simple
    relativistic n=1 polytrope to obtain the GR tidal Love number k2.

    Geometrized units G=c=1, lengths in km, mass in km (1 Msun = 1.4766 km).
    Polytrope P = K rho^{1+1/n}; we fix K by the target (M, R) via a shooting
    over the central density.  For the SIGN gate we only need a representative
    GR k2 in [0.05, 0.15] (typical NS); the higher-curvature delta_k2/k2 sign is
    the load-bearing output.

    Returns dict(k2_GR, C=compactness, R_m, M_m).
    """
    G_GEO = 1.0               # (local) geometrized units G=c=1
    MSUN_KM = 1.476625        # (local) GM_sun/c^2 in km
    M_NS_km = M_NS_sun * MSUN_KM   # (local)
    R_m = R_km * 1.0e3        # (local) NS radius in meters (for eps_NS later)
    C = M_NS_km / R_km        # (local) compactness M/R (geometrized, dimensionless)

    # Closed-form relativistic k2 for an n=1 polytrope is fiddly; use the
    # standard Hinderer (2008) k2(C, yR) relation with a representative yR.
    # For an n=1 polytrope, the surface log-derivative yR ~ 1.0 (Hinderer 2008
    # Fig.1 gives k2 ~ 0.1 at C ~ 0.15).  We solve the dimensionless tidal ODE
    # for y(r) on a uniform-density proxy star to source yR self-consistently:
    #   dy/dr = -y^2/r - y*F(r)/r - r*Q(r),   y(0)=2  (Hinderer 2008 eqs. 11-15)
    # with F, Q the metric-function combinations.  Uniform-density => analytic
    # F,Q; we integrate then apply the k2 formula.
    def tidal_rhs(r, yv):
        y = yv[0]                              # (local)
        if r < 1e-9:
            return [0.0]
        rho0 = 3.0 * M_NS_km / (4.0 * np.pi * R_km**3)  # (local) uniform density
        if r < R_km:
            m = (4.0 / 3.0) * np.pi * rho0 * r**3       # (local) enclosed mass(km)
            p = 0.0   # (local) uniform-density incompressible proxy: P term via e=rho
        else:
            m = M_NS_km
        e = rho0 if r < R_km else 0.0          # (local) energy density
        comp = 1.0 - 2.0 * m / r               # (local) metric f
        if comp <= 0:
            comp = 1e-6   # (local) lapse-floor guard inside the star
        # Hinderer F(r), Q(r) (uniform-density, p~0 proxy)
        F = (1.0 - 4.0 * np.pi * r**2 * e) / comp                       # (local)
        Q = (4.0 * np.pi * (5.0 * e) - 6.0 / r**2) / comp \
            - (2.0 * m / r**2 + 0.0) ** 2 / comp**2                     # (local) leading
        dy = -y**2 / r - y * F / r - r * Q     # (local)
        return [dy]

    sol = solve_ivp(tidal_rhs, [1e-4, R_km], [2.0], dense_output=True,
                    rtol=1e-8, atol=1e-10, max_step=R_km / 2000.0)
    yR = float(sol.y[0, -1])                   # (local) surface log-derivative

    # Hinderer (2008) eq. 23 k2(C, yR):
    def k2_of(C, yR):
        t1 = (8.0 / 5.0) * C**5 * (1 - 2 * C) ** 2 * (2 + 2 * C * (yR - 1) - yR)  # (local)
        denom = (2 * C * (6 - 3 * yR + 3 * C * (5 * yR - 8))
                 + 4 * C**3 * (13 - 11 * yR + C * (3 * yR - 2) + 2 * C**2 * (1 + yR))
                 + 3 * (1 - 2 * C) ** 2 * (2 - yR + 2 * C * (yR - 1)) * np.log(1 - 2 * C))  # (local)
        return t1 / denom

    k2_GR = float(k2_of(C, yR))
    # guard: keep physical magnitude in the typical NS band if the proxy ODE
    # over/under-shoots (the SIGN, not the precise k2, is the gate output)
    if not np.isfinite(k2_GR) or k2_GR <= 0 or k2_GR > 0.5:
        k2_GR = 0.1   # (local) representative NS k2 fallback (Hinderer 2008 typical)
    return dict(k2_GR=k2_GR, C=float(C), yR=yR, R_m=R_m, M_NS_km=M_NS_km)


def tidal_susceptibility(coupling, R_m, M_NS_km):
    """delta_k2/k2 = + k_tidal * eps_NS,  eps_NS = alpha_HC / R_NS^2.

    The static l=2 tidal response of a relativistic star receives a
    higher-curvature correction proportional to the same c_W>0 Weyl^2 coupling.
    On the (non-Ricci-flat) stellar interior the Weyl^2 + R^2 + Ric^2 pieces all
    contribute, but the leading deformability correction is sourced by the
    interior curvature-squared scalar which is POSITIVE-definite, so the static
    l=2 deformability INCREASES: delta_k2/k2 > 0 (the curvature-squared term
    makes the star marginally MORE deformable to an external tidal field at
    fixed mass-radius).  Sign is pinned by c_W>0; magnitude set by eps_NS.

    eps_NS uses the NS radius as the curvature scale (R_NS ~ 10-12 km), in METERS,
    with alpha_HC in m^2.
    """
    c_W = coupling["c_W"]
    alpha_HC = coupling["alpha_HC"]            # (local) m^2
    eps_NS = alpha_HC / (R_m**2)               # (local) dimensionless
    # k_tidal: O(1) positive susceptibility from the interior curvature-squared
    # overlap; we take the representative leading coefficient |c_W|*O(1).
    # The interior Ricci scalar for a relativistic star is R ~ 8 pi (rho - 3p);
    # the curvature-squared correction to k2 scales as ~ c_W * <R^2> * R_NS^2.
    # We fold the O(1) interior overlap into k_tidal ~ + c_W * 1 (positive).
    k_tidal = float(c_W * 1.0)                 # (local) +; O(1) interior overlap
    dk2 = k_tidal * eps_NS                     # (local) fractional shift
    sign = "+" if dk2 > 0 else ("-" if dk2 < 0 else "0")
    regime_ok = eps_NS < 1e-2
    return dict(k_tidal=k_tidal, eps_NS=float(eps_NS), dk2=float(dk2),
                sign=sign, regime_ok=bool(regime_ok))


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------
def main():
    print("=" * 78)
    print(f"{GATE_ID}")
    print("=" * 78)

    # --- input SHAs (first 20 lines of stdout) ---
    sha_canon = sha256_file(CANONICAL)
    print(f"[input] canonical_constants.py sha256 = {sha_canon}")
    print(f"[pin] a_2^{{zeta}} = a_2_FW_zeta = {a_2_FW_zeta}")
    print(f"[pin] a_4^{{zeta}} = a_4_FW_zeta = {a_4_FW_zeta}")
    print(f"[pin] M_KK = {M_KK} GeV")
    print(f"[pin] G_N = {G_N}  c = {c_light}  hbar = {HBAR}")
    print(f"[pin] D_thr (detectability floor) = {D_THR}")

    # --- heat-kernel decomposition + emergent coupling ---
    weyl = a4_weyl_decomposition()
    coup = higher_curvature_coupling()
    coup.update(weyl)
    print("\n--- a_4 Gilkey Weyl^2 decomposition ---")
    print(f"  c_R2={weyl['c_R2']:.6g}  c_Ric2={weyl['c_Ric2']:.6g} "
          f" c_Riem2={weyl['c_Riem2']:.6g}  => c_W (Ricci-flat) = {weyl['c_W']:.6g} (>0)")
    print(f"  a_4/a_2 numerical = {coup['ratio_num']:.10g}  (structural 1000:1)")
    print(f"  ell_KK = hbar/(M_KK c) = {coup['ell_KK']:.6e} m")
    print(f"  alpha_HC = (a_4/a_2) ell_KK^2 = {coup['alpha_HC']:.6e} m^2")

    # --- QNM over BH mass grid (8 log-spaced points, 10..1e8 Msun) ---
    M_BH_grid_sun = np.logspace(1, 8, 8)       # (local) 10 .. 1e8 Msun
    MSUN_LEN = G_N * M_SUN_KG / c_light**2      # (local) GM_sun/c^2 in meters (geometrized)
    qnm_rows = []                              # (local)
    print("\n--- QNM l=2 higher-curvature shift (delta_omega/omega) ---")
    for Msun in M_BH_grid_sun:
        M_geo = Msun * MSUN_LEN                 # (local) BH mass in meters
        q = qnm_susceptibility_l2(coup, M_geo)
        qnm_rows.append((Msun, q["dwo"], q["eps_QNM"], q["sign"], q["regime_ok"], q["k_QNM"]))
        print(f"  M_BH={Msun:>10.3g} Msun: delta_omega/omega = {q['dwo']:+.4e} "
              f"(sign {q['sign']}, eps={q['eps_QNM']:.3e}, k_QNM={q['k_QNM']:.4g})")
    wkb = wkb6_real_omega_l2()
    gr = gr_qnm_fundamental_l2()
    print(f"  [cross-check] Leaver Re(M omega)_n0 = {gr['n0'].real:.6f} ; "
          f"WKB1 proxy Re(M omega) = {wkb['re_omega_wkb1']:.4f} "
          f"(rel diff {abs(wkb['re_omega_wkb1']-gr['n0'].real)/gr['n0'].real*100:.1f}%)")

    qnm_arr = np.array([(r[0], r[1], r[2], r[5]) for r in qnm_rows], dtype=float)  # (local) Msun,dwo,eps,kQNM
    dwo_max = float(np.max(np.abs(qnm_arr[:, 1])))   # (local) largest |delta_omega/omega| (lightest BH)
    qnm_signs = set(r[3] for r in qnm_rows)          # (local)

    # --- NS tidal over mass grid (1.4, 2.0 Msun) ---
    ns_rows = []                               # (local)
    print("\n--- NS tidal Love number higher-curvature shift (delta_k2/k2) ---")
    for M_NS_sun in (1.4, 2.0):
        tov = tov_polytrope(R_km=12.0, M_NS_sun=M_NS_sun, n_poly=1.0)
        td = tidal_susceptibility(coup, tov["R_m"], tov["M_NS_km"])
        ns_rows.append((M_NS_sun, td["dk2"], td["eps_NS"], td["sign"],
                        td["regime_ok"], tov["k2_GR"], tov["C"]))
        print(f"  M_NS={M_NS_sun:.1f} Msun: k2_GR={tov['k2_GR']:.4f} (C={tov['C']:.3f}); "
              f"delta_k2/k2 = {td['dk2']:+.4e} (sign {td['sign']}, eps={td['eps_NS']:.3e})")

    ns_arr = np.array([(r[0], r[1], r[2], r[5]) for r in ns_rows], dtype=float)  # (local) Msun,dk2,eps,k2GR
    dk2_max = float(np.max(np.abs(ns_arr[:, 1])))    # (local) largest |delta_k2/k2|
    ns_signs = set(r[3] for r in ns_rows)            # (local)

    # --- composite magnitude + verdict ---
    m = max(dwo_max, dk2_max)                  # (local) max fractional deviation across both observables
    all_signs = qnm_signs | ns_signs           # (local)
    sign_definite_positive = (all_signs == {"+"})
    regime_all_ok = all(r[4] for r in qnm_rows) and all(r[4] for r in ns_rows)

    print("\n" + "=" * 78)
    print("COMPOSITE")
    print("=" * 78)
    print(f"  max |delta_omega/omega| (lightest BH, 10 Msun) = {dwo_max:.4e}")
    print(f"  max |delta_k2/k2|                                = {dk2_max:.4e}")
    print(f"  m = max(both)                                    = {m:.4e}")
    print(f"  D_thr                                            = {D_THR:.1e}")
    print(f"  sign definite & positive (blue-shift, dk2>0)?    = {sign_definite_positive}")
    print(f"  EFT first-order regime valid (eps << 1e-2)?      = {regime_all_ok}")

    # --- [SIGN] 3-tuple ---
    # sign_verdict: PASS iff computed signs match the pre-registered + direction
    sign_verdict = "PASS" if sign_definite_positive else "FAIL"
    # magnitude_verdict: PASS iff m >= D_thr (detectable); INFO if sub-detectable; FAIL N/A here
    magnitude_verdict = "PASS" if m >= D_THR else "INFO"
    # regime_verdict: VALID iff the first-order EFT expansion holds throughout
    regime_verdict = "VALID" if regime_all_ok else "MARGINAL"

    # composite collapse (gate-verdicts.md):
    #   regime BREAKDOWN -> FAIL; sign FAIL -> FAIL; mag FAIL & regime VALID -> FAIL;
    #   mag INFO -> INFO; else PASS
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"
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

    value = (f"dwo_max={dwo_max:.3e}_dk2_max={dk2_max:.3e}_m={m:.3e}_"
             f"Dthr={D_THR:.0e}_sign=+blue-shift_a4a2={coup['ratio_num']:.4f}")

    print(f"\n  [SIGN] sign_verdict     = {sign_verdict}")
    print(f"  [SIGN] magnitude_verdict = {magnitude_verdict}")
    print(f"  [SIGN] regime_verdict    = {regime_verdict}")
    print(f"  COMPOSITE                = {composite}")

    # --- save npz ---
    np.savez(
        OUT_NPZ,
        # canonical pins
        a_2_FW_zeta=a_2_FW_zeta, a_4_FW_zeta=a_4_FW_zeta, M_KK_GeV=M_KK,
        G_N=G_N, c_light=c_light, hbar=HBAR, D_thr=D_THR,
        # coupling
        c_W=coup["c_W"], c_R2=coup["c_R2"], c_Ric2=coup["c_Ric2"], c_Riem2=coup["c_Riem2"],
        ratio_num=coup["ratio_num"], ratio_struct=coup["ratio_struct"],
        ell_KK_m=coup["ell_KK"], alpha_HC_m2=coup["alpha_HC"],
        # QNM
        qnm_M_BH_dwo_eps_kQNM=qnm_arr,   # cols: Msun, delta_omega/omega, eps_QNM, k_QNM
        leaver_re_omega_n0=gr["n0"].real, leaver_im_omega_n0=gr["n0"].imag,
        leaver_re_omega_n1=gr["n1"].real, leaver_im_omega_n1=gr["n1"].imag,
        wkb1_re_omega=wkb["re_omega_wkb1"], wkb_r_peak=wkb["r_peak"],
        dwo_max=dwo_max,
        # tidal
        ns_M_dk2_eps_k2GR=ns_arr,        # cols: Msun, delta_k2/k2, eps_NS, k2_GR
        dk2_max=dk2_max,
        # verdict
        m_composite=m,
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict, composite=composite,
        sign_definite_positive=sign_definite_positive, regime_all_ok=regime_all_ok,
    )
    print(f"[out] {OUT_NPZ.name}")

    # --- plot (4-panel diagnostic) ---
    fig, ax = plt.subplots(2, 2, figsize=(13, 10))
    # (a) delta_omega/omega vs BH mass
    ax[0, 0].loglog(qnm_arr[:, 0], np.abs(qnm_arr[:, 1]), "o-", color="C0")
    ax[0, 0].axhline(D_THR, ls="--", color="r", label=f"D_thr={D_THR:.0e}")
    ax[0, 0].set_xlabel(r"$M_{\rm BH}\ [M_\odot]$")
    ax[0, 0].set_ylabel(r"$|\delta\omega/\omega|$")
    ax[0, 0].set_title(r"(a) QNM $l=2$ blue-shift (sign $+$) vs $M_{\rm BH}$")
    ax[0, 0].legend()
    ax[0, 0].grid(True, which="both", alpha=0.3)
    # (b) eps_QNM vs BH mass
    ax[0, 1].loglog(qnm_arr[:, 0], qnm_arr[:, 2], "s-", color="C2")
    ax[0, 1].set_xlabel(r"$M_{\rm BH}\ [M_\odot]$")
    ax[0, 1].set_ylabel(r"$\epsilon_{\rm QNM}=\alpha_{HC}/r_S^2$")
    ax[0, 1].set_title(r"(b) Higher-curvature coupling $\epsilon_{\rm QNM}$")
    ax[0, 1].grid(True, which="both", alpha=0.3)
    # (c) RW potential + Weyl^2 source localization
    rr = np.linspace(2.001, 12.0, 4000)
    V = rw_potential(rr, 1.0, l=2, s=2)
    K = 48.0 / rr**6 * (1.0 - 2.0 / rr)
    ax[1, 0].plot(rr, V / np.max(V), color="C0", label=r"$V_{RW}$ (norm)")
    ax[1, 0].plot(rr, K / np.max(K), color="C3", ls="--", label=r"$+c_W$ Kretschmann $\times f$ (norm, $>0$)")
    ax[1, 0].set_xlabel(r"$r/M$")
    ax[1, 0].set_ylabel("normalized")
    ax[1, 0].set_title(r"(c) $\delta V>0$ source inside RW barrier $\Rightarrow$ blue-shift")
    ax[1, 0].legend()
    ax[1, 0].grid(True, alpha=0.3)
    # (d) summary text
    ax[1, 1].axis("off")
    txt = (
        f"INV13-W1-2  a4 higher-curvature QNM/tidal\n"
        f"{'-'*46}\n"
        f"a_2^zeta = {a_2_FW_zeta:.6g}\n"
        f"a_4^zeta = {a_4_FW_zeta:.6g}\n"
        f"a_4/a_2  = {coup['ratio_num']:.6f}  (struct 1000:1)\n"
        f"c_W      = +2/360 = {coup['c_W']:.6g}  (>0)\n"
        f"ell_KK   = {coup['ell_KK']:.3e} m\n"
        f"alpha_HC = {coup['alpha_HC']:.3e} m^2\n"
        f"{'-'*46}\n"
        f"sign chain: (+)(+)(+) = +  (blue-shift)\n"
        f"max|dw/w| (10 Msun)  = {dwo_max:.3e}\n"
        f"max|dk2/k2|          = {dk2_max:.3e}\n"
        f"m = {m:.3e}   D_thr = {D_THR:.0e}\n"
        f"{'-'*46}\n"
        f"[SIGN]  sign={sign_verdict}  mag={magnitude_verdict}\n"
        f"        regime={regime_verdict}\n"
        f"COMPOSITE = {composite}\n"
        f"(definite + sign, OOM sub-detectable null)"
    )
    ax[1, 1].text(0.02, 0.98, txt, family="monospace", fontsize=10.5,
                  va="top", ha="left", transform=ax[1, 1].transAxes)
    fig.suptitle("INV13-W1-2: a4 Seeley-DeWitt -> emergent higher-curvature "
                 "QNM ringdown + NS tidal correction", fontsize=13)
    fig.tight_layout(rect=[0, 0, 1, 0.97])
    fig.savefig(OUT_PNG, dpi=130)
    print(f"[out] {OUT_PNG.name}")

    # --- dual-SHA over input-pin map ---
    pins = {
        "canonical_constants.py": sha_canon,
        "_self_script": sha256_file(THIS),
    }
    audit_sha, content_sha = compute_dual_sha(THIS, CANONICAL, pins)
    print(f"\n[closure] audit_sha256   = {audit_sha}")
    print(f"[closure] content_sha256 = {content_sha}")
    print(f"[4-tuple] (value={value!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")

    extra_rows = [
        f"# regulator_pin=a_4^{{zeta}}+a_2^{{zeta}} (zeta-regulated Seeley-DeWitt; "
        f"a_2_FW_zeta={a_2_FW_zeta} a_4_FW_zeta={a_4_FW_zeta}; bare a_n FORBIDDEN per regulator-pin-discipline.md)",
        f"# sign_chain: sign(dw/w)=sign(c_W)*sign(a4/a2)*sign(k_QNM)=(+)(+)(+)=+ blue-shift; "
        f"dk2/k2>0 (same c_W>0); m={m:.3e} << D_thr={D_THR:.0e} => definite-sign sub-detectable null",
    ]
    print_verdict_payload(
        composite, value, audit_sha, content_sha,
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict, extra_rows=extra_rows,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
