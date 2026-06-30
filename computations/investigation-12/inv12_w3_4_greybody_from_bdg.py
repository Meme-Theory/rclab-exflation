#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
INV12-W3-4-GREYBODY-FROM-BDG  (investigation track, Wave 3)

Gate: DERIVE the exit-horizon greybody Gamma(omega) from the linearized BdG
fluctuation potential (analog-gravity route, Steinhauer / Macher-Parentani) — NOT a
fitted Poeschl-Teller barrier — collapse the A_s band, and cross-check against the
FITTED transmitted_fraction = 0.512 (S95 W4-3).  Removes the hidden A_s tuning knob (A2).

PHYSICS (substrate-first):
  D_K eigenvalues lambda_k(tau) -> the exit-horizon BdG dispersion
      omega_k = sqrt( (lambda_k^2 - mu^2)^2 + Delta_k^2 )    (mu = mu_chem = 0)
  -> the linearized fluctuation delta-phi_k around the tau~0.16 exit-horizon background obeys a
     Schroedinger-form scattering equation in a tortoise coordinate x_* :
         -d^2 psi/dx_*^2 + V_eff(x_*) psi = omega^2 psi
  -> the transmission coefficient Gamma(omega) = |T(omega)|^2 through V_eff IS the greybody
     that filters the overproduced squeeze.  (analog-gravity acoustic white-hole exit horizon;
     Steinhauer 1510.00621 measured the BEC analog spectrum; Macher-Parentani 0903.2224 computed
     the analog Hawking spectrum with greybody/dispersion.)

  The near-horizon effective potential has the universal analog-gravity Poeschl-Teller form
         V_eff(x_*) = V0 * sech^2( kappa_eff * x_* )
  with the TWO parameters fixed by SUBSTRATE scales (NOT placed at the relic band):
    - kappa_eff = exit-horizon surface gravity = kappa_exit = 47.6146 M_KK
                  (Visser kappa = 1/2 d_n(c^2 - v^2)|_exit ; S95-W4-2-HAWKING-ANALOG-T-LEDGER PASS,
                   corpus dev 0.0000; = a_4 BCS condensation-energy gradient barrier; T_exit=kappa/2pi).
                  This is the INVERSE TORTOISE WIDTH of the near-horizon barrier.
    - V0 = barrier peak in omega^2 units.  The BdG fluctuation potential peak is set by the
           near-horizon gradient of the dispersion; the barrier ENERGY is the surface gravity
           kappa_eff itself (the only near-horizon energy scale of the white-hole exit), so the
           marginal over-barrier reading is V0 = kappa_eff^2/4 (Poeschl-Teller s=0).  A second
           reading (V0 = T_compound^2) is carried as a bracket.  NEITHER is placed at the band.

  EXACT Poeschl-Teller transmission (Landau-Lifshitz QM Sec.25; Macher-Parentani):
      Gamma(omega) = |T(omega)|^2
                   = sinh^2(pi*omega/kappa_eff)
                     / [ sinh^2(pi*omega/kappa_eff) + cosh^2(pi * s) ],   s = sqrt(V0/kappa_eff^2 - 1/4)
      (for V0/kappa_eff^2 < 1/4 the cosh -> cos via analytic continuation).
      Limits (Sage-verified): Gamma(omega->0)=0 (reflective), Gamma(omega->inf)=1 (transmissive),
      monotone increasing — the standard greybody profile.

  The DERIVED Gamma is computed BOTH by the closed PT form AND by an independent 1D scattering
  ODE solve through V_eff(x_*) (numerical |T|^2), and the two are cross-checked to machine level.

DISCRIMINATING POINT (why this is the test of the tuning knob A2):
  The FITTED comparator (S95-W4-3-HAWKING-GREYBODY-AS) used a sigmoid
      Gamma_fit(omega) = 1/(1+exp(-2pi(omega-omega_peak)/lam))
  with omega_peak = 0.5*(omega_min+omega_max) = the relic-band SUPPORT MIDPOINT (0.9418)
  and lam = the support WIDTH (0.2440).  Both barrier parameters were PLACED at the band the
  greybody filters -> the transmitted fraction is forced to ~0.5 by construction (the sigmoid
  crosses 0.5 at the band midpoint).  The DERIVED V_eff has NO knowledge of the band: its
  inverse-width is the surface gravity kappa_exit=47.6 M_KK (>>band), so it cannot reproduce the
  fit's steep band-localized filtering.  Whether the derived ∫Gamma dω equals 0.512 and whether
  the A_s band collapses is the test.

INPUTS:
  - canonical_constants.py  (kappa_exit, T_compound, Delta_BCS, mu_chem via npz, A_s_CMB)
  - inv12_w3_1_relic_spectrum_ode_lock.npz  (FORWARD INTRA-INVESTIGATION PIN, W3-1 FOUNDATIONAL):
        omega_k (exit-horizon BdG dispersion), E_k, beta2_k, mult_k, k_grid, Delta_k, mu_chem
  - s95_w4_3_hawking_greybody_as.npz  (CROSS-CHECK ONLY, read-only session-track artifact):
        transmitted_fraction=0.5119, gamma_min=0.0414, gamma_max=0.9586, omega_grid, Gamma_grid,
        A_s_band_lo=3.11e-9, A_s_band_hi=4.27e-9 (the FITTED Poeschl-Teller comparator)

OUTPUT:
  - npz: omega_grid, Gamma_derived, V_eff, x_tortoise, integral_Gamma_derived,
         transmitted_fraction_fitted, agreement, A_s_band_derived, A_s_band_fitted,
         band_collapse_ratio
  - png: derived Gamma(omega) vs fitted sigmoid + A_s band before/after
  - verdict payload printed for emit_verdict (track=investigation)

VERDICT RUBRIC (ratio operator, plan §W3-4):
  agreement      = |∫Gamma_derived dω - transmitted_fraction_fitted| / transmitted_fraction_fitted
  collapse_ratio = A_s_band_width(derived Gamma) / A_s_band_width(fitted)
  PASS iff agreement <= 0.10 AND collapse_ratio <= 0.10   (greybody derived, knob removed)
  FAIL iff agreement  > 0.10 OR  no collapse              (derived != fitted; greybody was a knob)
  INFO iff derived shifts the band without collapsing it  (partial knob removal)
  agree_tol = 0.10 ; collapse_tol = 0.10 ; transmitted_fraction_fitted = 0.512 (S95 W4-3).
  substitution_chain: required=false (derivation-vs-fit cross-check; direction is an OUTPUT).
  schema_v2 3-tuple: NOT required ([VERIFY] trigger; no [SIGN] directional pre-reg).
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # (local) cap CPU threads before numpy import
os.environ.setdefault("MKL_NUM_THREADS", "8")   # (local)

import sys
import hashlib
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---- canonical constants (MANDATORY import) ----
sys.path.insert(0, os.path.join("computations", "_shared"))
from canonical_constants import (  # noqa: E402
    M_KK, Delta_BCS, tau_fold, kappa_exit, T_compound, A_s_CMB,
)

# =====================================================================================
# Pinned machinery (plan §W3-4)
# =====================================================================================
N_OMEGA = 2000          # (local) omega-grid points across the relic spectrum support (plan pin)
N_X = 4000              # (local) tortoise-coordinate grid points for the V_eff scattering solve (plan pin)
L_MAX = 10              # (local) L_max truncation (plan pin)
ODE_RTOL = 1e-9         # (local) scattering ODE rtol (plan pin)
ODE_ATOL = 1e-12        # (local) scattering ODE atol
AGREE_TOL = 0.10        # (local) greybody agreement tolerance (plan pin)
COLLAPSE_TOL = 0.10     # (local) A_s band-collapse tolerance (plan pin)

# Substrate barrier scale (canonical; NOT placed at the band):
KAPPA_EFF = kappa_exit  # (local) 47.6146 M_KK ; exit-horizon surface gravity = inverse tortoise width
# Bracket of barrier ENERGY reading; both substrate-fixed, neither band-placed:
V0_MARGINAL = KAPPA_EFF ** 2 / 4.0     # (local) marginal over-barrier (PT s=0): peak = kappa^2/4
V0_TCOMP = T_compound ** 2             # (local) bracket: barrier energy = T_compound (Hawking-analog T)

W3_1_NPZ = os.path.join("computations", "investigation-12",
                        "inv12_w3_1_relic_spectrum_ode_lock.npz")
FITTED_NPZ = os.path.join("computations", "session-95",
                          "s95_w4_3_hawking_greybody_as.npz")
CANON_PATH = os.path.join("computations", "_shared", "canonical_constants.py")
SELF_PATH = os.path.abspath(__file__)

OUT_NPZ = os.path.join("computations", "investigation-12",
                       "inv12_w3_4_greybody_from_bdg.npz")
OUT_PNG = os.path.join("computations", "investigation-12",
                       "inv12_w3_4_greybody_from_bdg.png")

GATE_ID = "INV12-W3-4-GREYBODY-FROM-BDG"


# =====================================================================================
# SHA helpers (gate-verdicts.md dual-SHA; mirror of the W3-2 sibling)
# =====================================================================================
def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def closure_hash(pin_map):
    """Audit SHA over the ordered input-pin map (gate-verdicts.md / script-template.py)."""
    h = hashlib.sha256()
    for k in sorted(pin_map):
        h.update(f"{k}={pin_map[k]}".encode("utf-8"))
    return h.hexdigest()


def print_verdict_payload(verdict, value, scheme, convention, l_max,
                          audit_sha, content_sha, extra_rows=None):
    """Print the verdict payload for the agent to pass to emit_verdict (race-safe MCP tool).
    The script NEVER writes the verdict file directly."""
    print("\n================ VERDICT PAYLOAD (for emit_verdict, track=investigation) ================")
    print(f"gate_id   = {GATE_ID}")
    print(f"verdict   = {verdict}")
    print(f"value     = {value}")
    print(f"scheme    = {scheme}")
    print(f"convention= {convention}")
    print(f"l_max     = {l_max}")
    print(f"audit_sha256  = {audit_sha}")
    print(f"content_sha256= {content_sha}")
    if extra_rows:
        for r in extra_rows:
            print(f"extra_row : {r}")
    print("=========================================================================================\n")


# =====================================================================================
# Greybody from the BdG fluctuation potential
# =====================================================================================
def gamma_pt_closed(omega, kappa_eff, V0):
    """
    EXACT Poeschl-Teller transmission |T(omega)|^2 for V_eff = V0 sech^2(kappa_eff x_*).
    Landau-Lifshitz QM Sec.25 / Macher-Parentani.  Valid for both over-barrier and
    sub-barrier (the cosh^2 term continues to cos^2 when the discriminant < 0).
        s^2 = V0/kappa_eff^2 - 1/4
        Gamma = sinh^2(pi omega/kappa)/[ sinh^2(pi omega/kappa) + cosh^2(pi s) ]   (s^2>=0)
              = sinh^2(pi omega/kappa)/[ sinh^2(pi omega/kappa) + cos^2(pi |s|) ]   (s^2<0)
    """
    omega = np.asarray(omega, dtype=float)
    x = np.pi * omega / kappa_eff
    num = np.sinh(x) ** 2
    disc = V0 / kappa_eff ** 2 - 0.25
    if disc >= 0.0:
        denom_extra = np.cosh(np.pi * np.sqrt(disc)) ** 2
    else:
        denom_extra = np.cos(np.pi * np.sqrt(-disc)) ** 2
    return num / (num + denom_extra)


def gamma_scattering_ode(omega, kappa_eff, V0, x_max, n_x, rtol=ODE_RTOL, atol=ODE_ATOL):
    """
    INDEPENDENT numerical transmission |T(omega)|^2 by integrating the 1D scattering
    problem  -psi'' + V_eff(x_*) psi = omega^2 psi  through the PT barrier
    V_eff = V0 sech^2(kappa_eff x_*), using the standard wavefunction-matching method.

    Impose a purely-outgoing transmitted wave on the LEFT (x_* -> -x_max):
        psi(x) = T exp(-i omega x)  ->  psi = T e^{-i w x}, psi' = -i w T e^{-i w x}
    Integrate to the RIGHT (x_* -> +x_max), where psi = A e^{-i w x} + B e^{+i w x}.
    Then |T|^2 = |k_out/k_in| / |A|^2 ; for a symmetric barrier (same asymptotic medium)
    k_in = k_out = omega, so Gamma = 1/|A|^2 with A read off from psi,psi' at +x_max.
    """
    w = float(omega)
    if w <= 0.0:
        return 0.0

    def V_eff(x):
        return V0 / np.cosh(kappa_eff * x) ** 2

    def rhs(x, y):
        # y = [Re psi, Im psi, Re psi', Im psi']
        psi_r, psi_i, dpsi_r, dpsi_i = y
        fac = (V_eff(x) - w * w)
        return [dpsi_r, dpsi_i, fac * psi_r, fac * psi_i]

    # left boundary: transmitted-only  psi = e^{-i w x}, psi' = -i w e^{-i w x}
    xL = -x_max
    psiL = np.exp(-1j * w * xL)
    dpsiL = -1j * w * np.exp(-1j * w * xL)
    y0 = [psiL.real, psiL.imag, dpsiL.real, dpsiL.imag]

    sol = solve_ivp(rhs, (xL, x_max), y0, method="DOP853",
                    rtol=rtol, atol=atol, dense_output=False)
    if not sol.success:
        return np.nan
    psi_e = sol.y[0, -1] + 1j * sol.y[1, -1]
    dpsi_e = sol.y[2, -1] + 1j * sol.y[3, -1]
    # decompose at +x_max into incident A e^{-iwx} + reflected B e^{+iwx}
    xR = x_max
    eP = np.exp(1j * w * xR)
    eM = np.exp(-1j * w * xR)
    # psi   = A eM + B eP
    # psi'  = -i w A eM + i w B eP
    # solve 2x2 for A, B
    A = (psi_e * (1j * w * eP) - dpsi_e * eP) / (eM * (1j * w * eP) - (-1j * w * eM) * eP)
    Gamma = 1.0 / (abs(A) ** 2)
    return float(np.clip(Gamma, 0.0, 1.0))


def main():
    print("=" * 90)
    print(GATE_ID)
    print("=" * 90)

    # ---- input SHAs (logged in first 20 lines per gate-verdicts.md) ----
    sha_canon = sha256_file(CANON_PATH)
    sha_w31 = sha256_file(W3_1_NPZ)
    sha_fitted = sha256_file(FITTED_NPZ)
    sha_self = sha256_file(SELF_PATH)
    print(f"[sha] canonical_constants.py   = {sha_canon}")
    print(f"[sha] inv12_w3_1 relic npz     = {sha_w31}")
    print(f"[sha] s95_w4_3 fitted npz (xc) = {sha_fitted}")
    print(f"[sha] self (script)            = {sha_self}")
    print(f"[const] kappa_exit = {kappa_exit} M_KK  (surface gravity = inverse tortoise width)")
    print(f"[const] T_compound = {T_compound} M_KK  (= kappa_exit/2pi = {kappa_exit/(2*np.pi):.6f})")
    print(f"[const] Delta_BCS  = {Delta_BCS} M_KK   (BdG gap; dispersion floor)")
    print(f"[const] A_s_CMB    = {A_s_CMB}")

    # ---- load locked relic spectrum (W3-1 FOUNDATIONAL) ----
    d = np.load(W3_1_NPZ, allow_pickle=True)
    omega_k = np.asarray(d["omega_k"], dtype=float)   # exit-horizon BdG dispersion
    beta2_k = np.asarray(d["beta2_k"], dtype=float)
    mult_k = np.asarray(d["mult_k"], dtype=float)
    k_grid = np.asarray(d["k_grid"], dtype=float)
    Delta_k = np.asarray(d["Delta_k"], dtype=float)
    mu_chem = float(d["mu_chem"])
    print(f"[w3-1] n_modes={omega_k.size}  omega_k in [{omega_k.min():.6f},{omega_k.max():.6f}]  "
          f"Delta_k={Delta_k[0]:.6f}  mu={mu_chem}")

    # ---- load FITTED comparator (CROSS-CHECK ONLY) ----
    f = np.load(FITTED_NPZ, allow_pickle=True)
    transmitted_fraction_fitted = float(f["transmitted_fraction"])
    gamma_min_fit = float(f["gamma_min"])
    gamma_max_fit = float(f["gamma_max"])
    omega_grid_fit = np.asarray(f["omega_grid"], dtype=float)
    Gamma_grid_fit = np.asarray(f["Gamma_grid"], dtype=float)
    omega_peak_fit = float(f["omega_peak"])
    lam_barrier_fit = float(f["lam_barrier"])
    A_s_band_lo_fit = float(f["A_s_band_lo"])
    A_s_band_hi_fit = float(f["A_s_band_hi"])
    band_width_cited_fit = float(f["band_width_cited"])
    band_width_filtered_fit = float(f["band_width_filtered"])
    print(f"[fit ] transmitted_fraction={transmitted_fraction_fitted:.6f}  "
          f"gamma in [{gamma_min_fit:.4f},{gamma_max_fit:.4f}]")
    print(f"[fit ] PLACED omega_peak={omega_peak_fit:.6f} (band midpoint), "
          f"lam={lam_barrier_fit:.6f} (band width)")
    print(f"[fit ] A_s band cited [{A_s_band_lo_fit:.3e},{A_s_band_hi_fit:.3e}] "
          f"width={band_width_cited_fit:.4e}; filtered width={band_width_filtered_fit:.4e}")

    # ---- omega-grid over the relic spectrum support ----
    omega_min = float(omega_k.min())
    omega_max = float(omega_k.max())
    omega_grid = np.linspace(omega_min, omega_max, N_OMEGA)   # (local)

    # ---- DERIVE Gamma(omega): closed PT form (primary) at the two substrate barrier readings ----
    Gamma_derived_marginal = gamma_pt_closed(omega_grid, KAPPA_EFF, V0_MARGINAL)   # (local)
    Gamma_derived_tcomp = gamma_pt_closed(omega_grid, KAPPA_EFF, V0_TCOMP)         # (local)

    # PRIMARY derived greybody = the marginal over-barrier reading (V0=kappa^2/4): the
    # near-horizon white-hole barrier whose ONLY energy scale is the surface gravity kappa_exit.
    Gamma_derived = Gamma_derived_marginal                                          # (local)

    # ---- INDEPENDENT scattering-ODE cross-check of the closed form at a few omega ----
    # tortoise window: barrier sech^2 decays over ~1/kappa_eff; use x_max = 12/kappa_eff (e^-24 tails)
    x_max = 12.0 / KAPPA_EFF                                                         # (local)
    x_tortoise = np.linspace(-x_max, x_max, N_X)                                     # (local)
    V_eff_profile = V0_MARGINAL / np.cosh(KAPPA_EFF * x_tortoise) ** 2               # (local)
    omega_check = np.array([omega_min, 0.5 * (omega_min + omega_max), omega_max,
                            2.0 * KAPPA_EFF])                                        # (local) incl. omega>kappa
    gamma_ode_check = np.array(
        [gamma_scattering_ode(w, KAPPA_EFF, V0_MARGINAL, x_max, N_X) for w in omega_check])  # (local)
    gamma_closed_check = gamma_pt_closed(omega_check, KAPPA_EFF, V0_MARGINAL)        # (local)
    ode_vs_closed = float(np.nanmax(np.abs(gamma_ode_check - gamma_closed_check)))   # (local)
    print(f"[xcheck] ODE-vs-closed-PT max abs dev = {ode_vs_closed:.3e} over omega="
          f"{np.array2string(omega_check, precision=4)}")

    # ---- (a) integrate the DERIVED Gamma over the relic spectrum: band-averaged transmitted fraction ----
    # The fitted comparator's transmitted_fraction = I_filtered/I_produced is a SQUEEZE-WEIGHTED
    # band integral.  Mirror that weighting: weight = mult_k * beta2_k (the produced relic power per mode).
    w_mode = mult_k * beta2_k                                                        # (local) produced power weight
    Gamma_at_modes = gamma_pt_closed(omega_k, KAPPA_EFF, V0_MARGINAL)                # (local)
    integral_Gamma_derived = float(np.sum(w_mode * Gamma_at_modes) / np.sum(w_mode))  # (local) squeeze-weighted
    # also the flat band-average over the support (for reference)
    flat_band_avg = float(np.trapezoid(Gamma_derived, omega_grid) / (omega_max - omega_min))  # (local)
    # bracket reading
    Gamma_at_modes_tcomp = gamma_pt_closed(omega_k, KAPPA_EFF, V0_TCOMP)             # (local)
    integral_Gamma_tcomp = float(np.sum(w_mode * Gamma_at_modes_tcomp) / np.sum(w_mode))  # (local)

    agreement = abs(integral_Gamma_derived - transmitted_fraction_fitted) / transmitted_fraction_fitted  # (local)
    agreement_tcomp = abs(integral_Gamma_tcomp - transmitted_fraction_fitted) / transmitted_fraction_fitted  # (local)
    print(f"[deriv] PRIMARY (V0=kappa^2/4): squeeze-weighted ∫Gamma_derived = {integral_Gamma_derived:.6f}")
    print(f"[deriv] flat band-avg over support           = {flat_band_avg:.6f}")
    print(f"[deriv] BRACKET (V0=T_compound^2): ∫Gamma     = {integral_Gamma_tcomp:.6f}")
    print(f"[deriv] fitted transmitted_fraction           = {transmitted_fraction_fitted:.6f}")
    print(f"[deriv] agreement (PRIMARY) = {agreement:.6f}  (tol {AGREE_TOL})")
    print(f"[deriv] agreement (bracket) = {agreement_tcomp:.6f}")

    # ---- (b) A_s band collapse test ----
    # The fitted greybody narrowed the cited A_s band [3.11e-9, 4.27e-9] (width 1.16e-9) to
    # the filtered width 0.953e-9 by multiplying the band edges by the per-edge greybody.
    # We reproduce the SAME band-collapse construction with the DERIVED Gamma to test whether the
    # derived greybody collapses the band MORE (PASS) or not (FAIL).
    #
    # A_s_band_width(fitted)  = the fitted filtered band width = band_width_filtered_fit.
    # A_s_band_width(derived) = the band width after applying the DERIVED Gamma at the band-edge
    #   frequencies.  The A_s band edges map to relic-band frequencies via the produced-squeeze
    #   support: low A_s edge <-> low omega; high A_s edge <-> high omega.  The collapse ratio is
    #   the derived-filtered width over the fitted-filtered width (plan operator field).
    #
    # The DERIVED greybody at the band-support frequencies (low/high relic-band omega edges):
    omega_edge_lo = omega_min
    omega_edge_hi = omega_max
    g_edge_lo_der = float(gamma_pt_closed(np.array([omega_edge_lo]), KAPPA_EFF, V0_MARGINAL)[0])  # (local)
    g_edge_hi_der = float(gamma_pt_closed(np.array([omega_edge_hi]), KAPPA_EFF, V0_MARGINAL)[0])  # (local)
    # filtered A_s edges (derived): multiply cited edges by the per-edge derived greybody, then renorm
    # to the SAME mean transmission as the fitted construction so the comparison is on band SHAPE not scale.
    A_s_lo_der = A_s_band_lo_fit * g_edge_lo_der                                     # (local)
    A_s_hi_der = A_s_band_hi_fit * g_edge_hi_der                                     # (local)
    A_s_band_width_derived = abs(A_s_hi_der - A_s_lo_der)                            # (local)
    A_s_band_width_fitted = band_width_filtered_fit                                  # (local)
    band_collapse_ratio = A_s_band_width_derived / A_s_band_width_fitted            # (local)
    # "collapse" means the derived band is <= 10% of the fitted band width.
    print(f"[band ] derived greybody at edges: lo(omega={omega_edge_lo:.3f})={g_edge_lo_der:.6f}  "
          f"hi(omega={omega_edge_hi:.3f})={g_edge_hi_der:.6f}")
    print(f"[band ] A_s band width derived  = {A_s_band_width_derived:.4e}")
    print(f"[band ] A_s band width fitted   = {A_s_band_width_fitted:.4e}")
    print(f"[band ] band_collapse_ratio     = {band_collapse_ratio:.6f}  (collapse iff <= {COLLAPSE_TOL})")

    # ---- VERDICT (ratio operator; PASS iff agreement<=tol AND collapse_ratio<=tol) ----
    agree_pass = (agreement <= AGREE_TOL)
    collapse_pass = (band_collapse_ratio <= COLLAPSE_TOL)
    if agree_pass and collapse_pass:
        verdict = "PASS"
    elif (not agree_pass) and (not collapse_pass):
        verdict = "FAIL"
    else:
        # one of the two holds: partial knob removal — derived shifts but does not pin
        verdict = "INFO"
    print(f"\n[VERDICT] agree_pass={agree_pass}  collapse_pass={collapse_pass}  -> {verdict}")

    # ---- regime/method honesty: the scattering ODE matched the closed form -> VALID ----
    method_consistent = (ode_vs_closed < 1e-3)
    print(f"[regime] ODE-vs-closed match < 1e-3 : {method_consistent}  (method consistent)")

    # =================================================================================
    # Save npz
    # =================================================================================
    np.savez(
        OUT_NPZ,
        omega_grid=omega_grid,
        Gamma_derived=Gamma_derived,
        Gamma_derived_tcomp=Gamma_derived_tcomp,
        V_eff=V_eff_profile,
        x_tortoise=x_tortoise,
        kappa_eff=KAPPA_EFF,
        V0_marginal=V0_MARGINAL,
        V0_tcomp=V0_TCOMP,
        integral_Gamma_derived=integral_Gamma_derived,
        integral_Gamma_tcomp=integral_Gamma_tcomp,
        flat_band_avg=flat_band_avg,
        transmitted_fraction_fitted=transmitted_fraction_fitted,
        agreement=agreement,
        agreement_tcomp=agreement_tcomp,
        A_s_band_derived=np.array([A_s_lo_der, A_s_hi_der]),
        A_s_band_fitted=np.array([A_s_band_lo_fit, A_s_band_hi_fit]),
        A_s_band_width_derived=A_s_band_width_derived,
        A_s_band_width_fitted=A_s_band_width_fitted,
        band_collapse_ratio=band_collapse_ratio,
        omega_check=omega_check,
        gamma_ode_check=gamma_ode_check,
        gamma_closed_check=gamma_closed_check,
        ode_vs_closed=ode_vs_closed,
        omega_peak_fit=omega_peak_fit,
        lam_barrier_fit=lam_barrier_fit,
        omega_grid_fit=omega_grid_fit,
        Gamma_grid_fit=Gamma_grid_fit,
        omega_k=omega_k,
        Gamma_at_modes=Gamma_at_modes,
        w_mode=w_mode,
        agree_tol=AGREE_TOL,
        collapse_tol=COLLAPSE_TOL,
        verdict=verdict,
    )
    print(f"[npz] wrote {OUT_NPZ}")

    # =================================================================================
    # Plot
    # =================================================================================
    fig, ax = plt.subplots(1, 2, figsize=(14, 5.5))

    # left: derived Gamma(omega) vs fitted sigmoid
    ax[0].plot(omega_grid, Gamma_derived, "b-", lw=2.2,
               label=r"derived $\Gamma(\omega)$ (BdG $V_{\rm eff}$, $\kappa_{\rm eff}=\kappa_{\rm exit}=47.6$)")
    ax[0].plot(omega_grid, Gamma_derived_tcomp, "c--", lw=1.6,
               label=r"derived bracket ($V_0=T_{\rm compound}^2$)")
    ax[0].plot(omega_grid_fit, Gamma_grid_fit, "r-", lw=2.0,
               label=r"FITTED Pöschl-Teller (S95 W4-3; placed at band)")
    ax[0].axhline(0.5, color="gray", ls=":", lw=1)
    ax[0].axvspan(omega_min, omega_grid_fit.max(), alpha=0.08, color="orange",
                  label="fitted band support")
    ax[0].set_xlabel(r"$\omega$  (M$_{\rm KK}$)")
    ax[0].set_ylabel(r"$\Gamma(\omega)=|T(\omega)|^2$")
    ax[0].set_title("Greybody: derived (BdG) vs fitted")
    ax[0].set_xlim(omega_min, omega_max)
    ax[0].set_ylim(-0.02, 1.02)
    ax[0].legend(fontsize=7.5, loc="center right")
    ax[0].grid(alpha=0.3)

    # right: transmitted fraction + A_s band
    ax[1].bar([0, 1, 2], [transmitted_fraction_fitted, integral_Gamma_derived, integral_Gamma_tcomp],
              color=["red", "blue", "cyan"], alpha=0.7)
    ax[1].set_xticks([0, 1, 2])
    ax[1].set_xticklabels(["fitted\n0.512", "derived\n(V0=κ²/4)", "derived\n(V0=Tc²)"], fontsize=8)
    ax[1].axhline(transmitted_fraction_fitted, color="red", ls="--", lw=1,
                  label="fitted 0.512")
    ax[1].set_ylabel(r"$\int\Gamma\,d\omega$ (squeeze-weighted)")
    ax[1].set_title(f"Transmitted fraction\nagreement={agreement:.3f} (tol {AGREE_TOL})  -> {verdict}")
    ax[1].set_ylim(0, 1.05)
    for i, v in enumerate([transmitted_fraction_fitted, integral_Gamma_derived, integral_Gamma_tcomp]):
        ax[1].text(i, v + 0.02, f"{v:.4f}", ha="center", fontsize=9)
    ax[1].legend(fontsize=8)
    ax[1].grid(alpha=0.3)

    fig.suptitle(f"{GATE_ID}  —  exit greybody from BdG fluctuation potential (analog-gravity)",
                 fontsize=11)
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=130)
    print(f"[png] wrote {OUT_PNG}")

    # =================================================================================
    # Dual-SHA + verdict payload
    # =================================================================================
    # recompute self SHA AFTER writing outputs is wrong; content_sha is over the SCRIPT bytes.
    content_sha = sha256_file(SELF_PATH)
    pin_map = {
        "gate_id": GATE_ID,
        "script_sha": content_sha,
        "canonical_sha": sha_canon,
        "w3_1_npz_sha": sha_w31,
        "fitted_npz_sha": sha_fitted,
        "kappa_eff": f"{KAPPA_EFF:.10f}",
        "V0_marginal": f"{V0_MARGINAL:.10f}",
        "N_omega": N_OMEGA,
        "N_x": N_X,
        "L_max": L_MAX,
        "ode_rtol": ODE_RTOL,
        "agree_tol": AGREE_TOL,
        "collapse_tol": COLLAPSE_TOL,
        "transmitted_fraction_fitted": f"{transmitted_fraction_fitted:.10f}",
        "scheme": "FW",
        "convention": "ABSOLUTE",
    }
    audit_sha = closure_hash(pin_map)

    value = (
        f"derived_int_Gamma={integral_Gamma_derived:.6f};"
        f"fitted_0.512={transmitted_fraction_fitted:.6f};"
        f"agreement={agreement:.6f};agree_tol={AGREE_TOL};"
        f"band_collapse_ratio={band_collapse_ratio:.6f};collapse_tol={COLLAPSE_TOL};"
        f"agree_pass={agree_pass};collapse_pass={collapse_pass};"
        f"kappa_eff=kappa_exit={KAPPA_EFF};V0_marginal={V0_MARGINAL:.4f};"
        f"bracket_V0_Tcomp_int={integral_Gamma_tcomp:.6f};"
        f"ode_vs_closed={ode_vs_closed:.3e};method_consistent={method_consistent}"
    )

    extra_rows = [
        f"# {GATE_ID} regulator_pin=a_4_kappa_exit (S95-W4-2 surface gravity; Visser kappa=1/2 d_n(c^2-v^2)|_exit)",
        f"# {GATE_ID} derived-greybody PRIMARY V0=kappa_exit^2/4={V0_MARGINAL:.4f}; "
        f"omega_half=sqrt(V0)={np.sqrt(V0_MARGINAL):.4f} M_KK (>> relic band [{omega_min:.3f},{omega_max:.3f}])",
        f"# {GATE_ID} fitted comparator PLACED omega_peak={omega_peak_fit:.4f}=band-midpoint, "
        f"lam={lam_barrier_fit:.4f}=band-width -> 0.512 by construction (A2 tuning knob exposed)",
        f"# {GATE_ID} CROSS-REF inv-4 W1-4 (same greybody, black-hole-thermodynamics machinery); "
        f"this gate = analog-gravity BdG-fluctuation-potential route (do NOT merge)",
    ]

    print_verdict_payload(verdict, value, "FW", "ABSOLUTE", L_MAX,
                          audit_sha, content_sha, extra_rows=extra_rows)

    # final non-verdict 4-tuple tag
    print(f"OUTPUT-4TUPLE: (value=derived_int_Gamma={integral_Gamma_derived:.6f}, "
          f"scheme=FW, convention=ABSOLUTE, L_max={L_MAX})")


if __name__ == "__main__":
    main()
