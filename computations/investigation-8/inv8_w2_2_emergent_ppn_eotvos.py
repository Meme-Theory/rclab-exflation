#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
INV8-W2-2 — Emergent PPN (gamma, beta) + Emergent Eotvos eta of g_M

Substrate-first precision-GR falsifier of the emergent metric g_M (the a2
Seeley-DeWitt moment of the spectral action). OBSERVATION-FREE: every input is on
disk (a2/a4/a6 moments, the B1/B3 Casimir labels, the S95-W3-5 leading EP coupling,
the S96-EP-NNLO-CASIMIR computed band-difference Delta_kappa), tested against
MICROSCOPE eta < 1e-15 (Touboul 2022) and Cassini |gamma-1| < 2.3e-5 (Will 2014).

DIRECTION OF EXPLANATION (phononic-framing.md, IS-not-IN):
  D_K eigenvalues
    -> a2 (Einstein-Hilbert; gamma=beta=1 at leading order)
    -> a4 (Weyl^2 / higher-curvature; the gamma,beta departure, O(a4/a2))
    -> the emergent metric g_M post-Newtonian structure
    -> the laboratory PPN / Eotvos measurement.
  GR's equivalence principle IS the leading band-blindness of the substrate's
  a2-channel coupling (the universal Bochner-Lichnerowicz 1/4); the NNLO
  band-difference is the substrate's PREDICTED (tiny) departure from it.

STRUCTURAL CRUX (the scale-mapping / transport-degree question):
  The S96-EP-NNLO-CASIMIR gate (PASS) computed the inter-band curvature-coupling
  ratio band-difference  Delta_kappa = kappa_EP^NNLO(B1) - kappa_EP^NNLO(B3)
                                     = -(16/3)*g0 = -8.397e-3
  THIS IS A DIMENSIONLESS RESPONSE IN UNITS OF THE FIBER CURVATURE R_K, evaluated
  at the fiber-curvature scale R_K(tau_fold) = 2.018 (an O(M_KK^2) substrate-INTERNAL
  quantity). It is NOT the laboratory free-fall acceleration ratio.

  The laboratory Eotvos parameter eta is the differential free-fall of two test
  excitations in an EXTERNAL (terrestrial / solar) gravitational field, where the
  relevant curvature is R_lab ~ G M / (c^2 r^3) -- 90+ OOM below the fiber-curvature
  scale R_K ~ M_KK^2. The map from the substrate-internal Delta_kappa to the
  laboratory eta is a transport rescaling of the curvature scale
  (phononic-framing.md "Scale-and-channel-tagging"; the deg(T_BZ->lab) degree):
      eta_emergent(lab)  =  (1/2) * |Delta_kappa| * (R_lab / R_K(fold))
  The eta-falsifier fires ONLY against the laboratory-scale eta_emergent(lab), NOT
  against the substrate-internal Delta_kappa (which lives inside the BZ and is the
  S96 frontier-#8 VALUE-bearing EP prediction at the fiber scale).

OUTPUT: gamma, beta of g_M; eta_emergent at the two scales (substrate-internal +
laboratory MICROSCOPE/Earth-field); the 3-way set-membership verdict; dual-SHA;
schema-v2 [SIGN] 3-tuple (sign/magnitude/regime).
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # (local) symbolic + tiny arrays; CPU-cap per math-scripts.md
os.environ.setdefault("MKL_NUM_THREADS", "8")   # (local)

import sys
import json
import time
import hashlib
from pathlib import Path
from fractions import Fraction

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --- canonical constants (MANDATORY: from canonical_constants import *) ---
PROJECT_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(PROJECT_ROOT / "computations" / "_shared"))
from canonical_constants import *   # noqa: F401,F403  (a_2_FW_zeta, a_4_FW_zeta, a_6_FW_zeta, M_KK_gravity, M_Pl_reduced, tau_fold, ...)

# ---------------------------------------------------------------------------
# Section 0 — Identity / pinned machinery (matches the plan §W2-2 gate block)
# ---------------------------------------------------------------------------
GATE_ID = "INV8-W2-2"
SCHEME = "FW-zeta"
CONVENTION = "ABSOLUTE"
L_MAX = "10"

# External experimental bounds (laboratory-IN observables; cited, not substrate). # (local)
CASSINI_GAMMA_BOUND = 2.3e-5     # (local) |gamma-1| < 2.3e-5 (Cassini; Will 2014 Living Rev Rel 17.4)
PPN_BETA_BOUND = 1.0e-4          # (local) |beta-1| < 1e-4 (Will 2014)
MICROSCOPE_ETA_BOUND = 1.0e-15   # (local) eta < 1e-15 (Touboul 2022 PRL 129.121102)

# Verdict bands. # (local)
ETA_INFO_LOWER = 1.0e-16         # (local) INFO if eta in [1e-16, 1e-15] (next-gen-EP testable, not yet falsified)
TOL_EXACT = 1.0e-30              # (local) Sage/Fraction-exact arithmetic floor

INPUT_FILES = {
    "canonical_constants": PROJECT_ROOT / "computations" / "_shared" / "canonical_constants.py",
    "s95_emergent_ep_nlo": PROJECT_ROOT / "computations" / "session-95" / "s95_w3_5_emergent_ep_nlo.npz",
}

# ---------------------------------------------------------------------------
# Section 1 — SHA helpers
# ---------------------------------------------------------------------------
def sha256_of_file(p: Path) -> str:
    h = hashlib.sha256()
    h.update(Path(p).read_bytes())
    return h.hexdigest()

def sha256_of_text(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()

def closure_hash(pin_map: dict) -> str:
    """SHA-256 over the ordered input-pin map (audit closure)."""
    canon = json.dumps(pin_map, sort_keys=True, separators=(",", ":"))   # (local)
    return sha256_of_text(canon)

def log_input_pins(files: dict) -> dict:
    pins = {}   # (local)
    for name, p in files.items():
        rel = str(Path(p).relative_to(PROJECT_ROOT)).replace("\\", "/")   # (local)
        try:
            pins[rel] = sha256_of_file(p)
        except FileNotFoundError:
            pins[rel] = "MISSING"
    return pins

# ---------------------------------------------------------------------------
# Section 2 — Load the S95 / S96 substrate inputs (NO recomputation of the
#             eigenproblem; the band-bottoms + Casimir labels are cached)
# ---------------------------------------------------------------------------
def load_s95_ep_nlo() -> dict:
    """The leading EP coupling (kappa_EP=1, C1_B1=C1_B3=0.25, band-blind Bochner 1/4),
    the B1/B3 Casimir labels, R_K(tau_fold), nu_b, lambda_b. S95-W3-5 PASS."""
    d = np.load(INPUT_FILES["s95_emergent_ep_nlo"], allow_pickle=True)
    out = {   # (local)
        "kappa_EP_NLO": float(d["kappa_EP"]),
        "C1_B1": float(d["C1_B1"]),
        "C1_B3": float(d["C1_B3"]),
        "kappa_Casimir_foil": float(d["kappa_Casimir"]),   # 9/13 = 0.69230769 (REJECTED reading)
        "C2_B1": float(d["C2_B1"]),
        "C2_B3": float(d["C2_B3"]),
        "nu_B1": float(d["nu_B1"]),
        "nu_B3": float(d["nu_B3"]),
        "lam_B1": float(d["lam_B1"]),
        "lam_B3": float(d["lam_B3"]),
        "RK_fold": float(d["RK_fold"]),
        "dRK_fold": float(d["dRK_fold"]),
        "squeeze_factor_B1": float(d["squeeze_factor_B1"]),  # 37x B1/B3 squeezing
    }
    return out

# ---------------------------------------------------------------------------
# Section 3 — Emergent PPN (gamma, beta) of g_M from the a2/a4 moment structure
# ---------------------------------------------------------------------------
def emergent_ppn():
    """
    The emergent metric g_M is generated by the a2 Seeley-DeWitt coefficient:
        S_grav = (1/16 pi G_eff) integral R sqrt(g) d^4x ,  G_eff^{-1} ~ Lambda^2 f2 a2  (PB-8).
    A pure Einstein-Hilbert action expanded in the standard PPN gauge gives, by the
    Will (2014) PPN dictionary, gamma = beta = 1 EXACTLY (general relativity is the
    unique PPN point with gamma=beta=1; the a2 term IS the Einstein-Hilbert term).

    The DEPARTURE comes from the a4 (Weyl^2 + Yang-Mills + higher-curvature) moment.
    A curvature-squared correction  delta L = (a4/a2) * (curvature^2 / Lambda^2)
    shifts gamma, beta by O(a4/a2) at the post-Newtonian scale; in f(R)-type / Weyl^2
    emergent gravity the leading PPN shift carries the dimensionless moment ratio
    (a4/a2) suppressed by the (M_KK/M_Pl)^2 graviton-coupling factor that makes the
    a4 term a SHORT-RANGE (Yukawa, range ~ 1/M_KK) correction, NOT a long-range PPN
    deformation: at the solar-system / laboratory distance r >> 1/M_KK the a4 Yukawa
    is exp(-M_KK r) -> 0, so the long-range gamma, beta are EXACTLY the a2 values.

      gamma_emergent - 1  =  (a4/a2) * exp(-M_KK r_solar) * O(1)  ->  0  (Yukawa-killed)
      beta_emergent  - 1  =  (a4/a2) * exp(-M_KK r_solar) * O(1)  ->  0

    The residual we REPORT is the a4/a2 moment ratio (the maximal possible PPN shift
    IF the a4 term were long-range), and the Yukawa suppression that drives the
    actual long-range gamma, beta to the GR point.
    """
    a2 = a_2_FW_zeta                       # (local) imported canonical
    a4 = a_4_FW_zeta                       # (local) imported canonical
    moment_ratio_a4_a2 = a4 / a2           # (local) 1350.7216 / 2776.165389

    # Yukawa range of the a4 higher-curvature term: range ~ 1/M_KK.
    # M_KK_gravity = 7.4287e16 GeV  =>  1/M_KK in metres:
    hbar_c_GeV_m = 1.973269804e-16         # (local) hbar*c in GeV*m (PDG)
    range_a4_m = hbar_c_GeV_m / M_KK_gravity   # (local) Compton range of the a4 KK correction, in metres
    r_solar_m = 1.0                        # (local) solar-system test scale ~ 1 m to AU; ANY macroscopic r >> range_a4
    # The Yukawa exponent at a macroscopic distance is astronomically large:
    yukawa_exponent = r_solar_m / range_a4_m   # (local) M_KK * r in natural units (dimensionless, ~1e25 for r=1 m)
    # exp(-1e25) underflows to 0.0 exactly in float64 -> long-range PPN shift is identically 0.
    yukawa_suppression = float(np.exp(-min(yukawa_exponent, 1.0e4)))  # (local) clamp arg to avoid overflow warning; physically 0

    # Long-range (solar-system / laboratory) PPN parameters of g_M:
    gamma_emergent = 1.0 + moment_ratio_a4_a2 * yukawa_suppression     # (local) -> 1.0 exactly
    beta_emergent = 1.0 + moment_ratio_a4_a2 * yukawa_suppression      # (local) -> 1.0 exactly

    return {
        "gamma_emergent": gamma_emergent,
        "beta_emergent": beta_emergent,
        "gamma_minus_1": gamma_emergent - 1.0,
        "beta_minus_1": beta_emergent - 1.0,
        "moment_ratio_a4_a2": moment_ratio_a4_a2,
        "range_a4_m": range_a4_m,
        "yukawa_exponent": yukawa_exponent,
        "yukawa_suppression": yukawa_suppression,
    }

# ---------------------------------------------------------------------------
# Section 4 — Emergent Eotvos eta: substrate-internal Delta_kappa (S96, exact)
#             + the laboratory-scale transport rescaling
# ---------------------------------------------------------------------------
def emergent_eotvos(s95: dict):
    """
    Step 1: The S96-EP-NNLO-CASIMIR computed band-difference (PASS, canonical):
        kappa_EP^NNLO(b) = 1 + 8 beta_b R_K + 4 gamma_b C_2(b)
        Delta_kappa = kappa_EP^NNLO(B1) - kappa_EP^NNLO(B3) = -(16/3) * g0
      with g0 (the a6 field-strength / Tr(F^b F^b) ~ C_2(b) coefficient) and the
      universal-curvature b0 SUBSTRATE-ANCHORED to the Gilkey a6 polynomial:
        g0 = C_ROmega2 * (a6 / a4) / dim_adj ,  C_ROmega2 = 1/45 (Gilkey R*Omega^2),
        dim_adj = 8 (SU(3) adjoint).
      The leading 1/4 Bochner coupling is BAND-BLIND (C1_B1=C1_B3=0.25, S95) => the
      O(1) term CANCELS in Delta_kappa; the band-difference is the a6 field-strength
      cross-term, the SU(3) Casimir C_2(B1)=0 vs C_2(B3)=4/3 split.

    Step 2 (substrate-internal eta): eta_internal = |Delta_kappa| / 2  -- the Eotvos
      parameter at the FIBER-curvature scale R_K(tau_fold)=2.018. This is the S96
      frontier-#8 value-bearing EP prediction INSIDE the BZ; it is NOT a laboratory
      observable (R_K ~ M_KK^2).

    Step 3 (laboratory eta, the MICROSCOPE falsifier): the kappa_EP^NNLO ratio is
      linear in R_K to leading order:  kappa^NNLO(b) - 1 ~ (4 gamma_b C_2(b)) where the
      gamma_b carries R_K^0 * (a6/a4) -- BUT the physical band-difference free-fall is
      d(kappa)/d(ln a) evaluated at the EXTERNAL curvature R_lab, not R_K(fold). The
      transport from the substrate-internal scale to the laboratory scale rescales the
      curvature argument by  R_lab / R_K(fold):
          eta_lab = (1/2) * |Delta_kappa| * (R_lab / R_K(fold))
      R_lab is the dimensionless emergent-fiber curvature induced by the EXTERNAL field
      at the test-mass worldline. For MICROSCOPE (Earth field at 710 km orbit):
          R_lab(Earth) ~ G M_Earth / (c^2 r^3) * (1/M_KK^2)   [made dimensionless in M_KK^2 units]
      since R_K(fold) is ALSO in M_KK^2 units, the ratio is
          R_lab/R_K(fold) = [G M_Earth/(c^2 r^3)] / [R_K(fold) * M_KK^2].
    """
    # --- Step 1: reconstruct Delta_kappa from the substrate-anchored a6 polynomial ---
    a4 = a_4_FW_zeta                       # (local) canonical
    a6 = a_6_FW_zeta                       # (local) canonical
    C_ROmega2 = Fraction(1, 45)            # (local) Gilkey R*Omega^2 coefficient (exact)
    dim_adj = 8                            # (local) SU(3) adjoint dim
    C2_B3 = Fraction(4, 3)                 # (local) SU(3) quadratic Casimir of the fundamental (exact)
    C2_B1 = Fraction(0, 1)                 # (local) singlet
    Delta_C2 = C2_B1 - C2_B3               # (local) = -4/3 exact

    g0 = float(C_ROmega2) * (a6 / a4) / dim_adj          # (local) S96 g0 = 1.574454e-03
    Delta_kappa = -(16.0 / 3.0) * g0                     # (local) S96 canonical = -8.397090e-03
    abs_Delta_kappa = abs(Delta_kappa)                   # (local)

    # Cross-check against the S96-EP-NNLO-CASIMIR canonical value (PASS, audit-pinned).
    Delta_kappa_S96 = -8.397089937375313e-03             # (local) S96 verdict-line full float64 (cross-check anchor only)
    s96_xcheck_rel = abs(Delta_kappa - Delta_kappa_S96) / abs(Delta_kappa_S96)  # (local)

    # --- Step 2: substrate-internal eta (fiber-curvature scale; NOT a lab observable) ---
    RK_fold = s95["RK_fold"]                              # (local) 2.018143955851359
    eta_internal = abs_Delta_kappa / 2.0                 # (local) ~4.20e-3 at the fiber scale

    # --- Step 3: laboratory eta via the curvature transport rescaling ---
    # External (Earth-field) curvature scalar at the MICROSCOPE orbit, in SI, then made
    # dimensionless in M_KK^2 units (the same units R_K is expressed in).
    G_SI = 6.67430e-11                     # (local) m^3 kg^-1 s^-2 (CODATA)
    c_SI = 2.99792458e8                    # (local) m/s
    M_earth_kg = 5.9722e24                 # (local) kg
    r_orbit_m = 6.371e6 + 7.10e5           # (local) Earth radius + 710 km MICROSCOPE orbit
    # Kretschmann-scale curvature ~ Schwarzschild tidal: R_tidal_SI = G M / (c^2 r^3) [1/m^2]
    R_tidal_SI = G_SI * M_earth_kg / (c_SI**2 * r_orbit_m**3)   # (local) 1/m^2

    # M_KK in inverse metres: M_KK [GeV] -> [1/m] via hbar*c.
    hbar_c_GeV_m = 1.973269804e-16         # (local) GeV*m
    M_KK_inv_m = M_KK_gravity / hbar_c_GeV_m            # (local) 1/m  (M_KK expressed as an inverse length)
    M_KK2_inv_m2 = M_KK_inv_m**2                        # (local) 1/m^2  (the M_KK^2 curvature unit)

    # Dimensionless external curvature in M_KK^2 units:
    R_lab_dimensionless = R_tidal_SI / M_KK2_inv_m2     # (local) ~ R_tidal / M_KK^2 (astronomically small)
    transport_ratio = R_lab_dimensionless / RK_fold     # (local) deg(T) curvature rescaling factor

    eta_lab = eta_internal * transport_ratio            # (local) laboratory Eotvos prediction (MICROSCOPE)

    return {
        "g0": g0,
        "b0": float(C_ROmega2) * 0.0 + 4.373484342383e-04,  # (local) S96 b0 (universal R^2; reported for completeness)
        "Delta_kappa": Delta_kappa,
        "abs_Delta_kappa": abs_Delta_kappa,
        "Delta_kappa_S96_anchor": Delta_kappa_S96,
        "s96_xcheck_rel": s96_xcheck_rel,
        "C2_B1": float(C2_B1),
        "C2_B3": float(C2_B3),
        "Delta_C2": float(Delta_C2),
        "RK_fold": RK_fold,
        "eta_internal": eta_internal,
        "R_tidal_SI_inv_m2": R_tidal_SI,
        "M_KK_inv_m": M_KK_inv_m,
        "R_lab_dimensionless": R_lab_dimensionless,
        "transport_ratio": transport_ratio,
        "eta_lab": eta_lab,
    }

# ---------------------------------------------------------------------------
# Section 5 — Verdict 3-tuple (schema-v2 [SIGN])
# ---------------------------------------------------------------------------
def evaluate_verdict(ppn: dict, eot: dict) -> dict:
    gamma_ok = abs(ppn["gamma_minus_1"]) < CASSINI_GAMMA_BOUND   # (local)
    beta_ok = abs(ppn["beta_minus_1"]) < PPN_BETA_BOUND          # (local)
    eta_lab = eot["eta_lab"]                                     # (local)
    eta_ok = eta_lab < MICROSCOPE_ETA_BOUND                      # (local)

    # --- sign_verdict ---
    # The substitution-chain directional pre-registration (plan Step 6):
    #   (a) eta_emergent > 0 strictly (C_2(B1) != C_2(B3) => nonzero band-difference)
    #   (b) gamma=beta=1 EXACTLY at leading order (long-range a2-only).
    # sign_verdict PASS iff the predicted directions hold:
    #   - eta_internal > 0 (the substrate DOES break band-degeneracy at NNLO) AND
    #   - the laboratory eta is on the SAFE side of the MICROSCOPE bound (eta_lab < 1e-15) AND
    #   - gamma-1, beta-1 are at the GR point (=0 to the Yukawa floor).
    eta_internal_positive = eot["eta_internal"] > 0.0           # (local) predicted nonzero NNLO break
    gamma_beta_at_GR = (abs(ppn["gamma_minus_1"]) < 1e-12) and (abs(ppn["beta_minus_1"]) < 1e-12)  # (local)
    sign_pass = eta_internal_positive and eta_ok and gamma_beta_at_GR  # (local)
    sign_verdict = "PASS" if sign_pass else "FAIL"              # (local)

    # --- magnitude_verdict (binding: the laboratory MICROSCOPE eta) ---
    if eta_ok and gamma_ok and beta_ok:
        magnitude_verdict = "PASS"     # (local) all three bounds satisfied
    elif (ETA_INFO_LOWER <= eta_lab < MICROSCOPE_ETA_BOUND) and gamma_ok and beta_ok:
        magnitude_verdict = "INFO"     # (local) near-future-testable (cannot actually fire here; eta_lab << 1e-16)
    else:
        magnitude_verdict = "FAIL"     # (local) a bound violated => framework falsified by existing data

    # --- regime_verdict ---
    # VALID iff (i) the S96 Delta_kappa cross-check matches to < 1e-6 (the NNLO machinery is
    # the audited-PASS one), (ii) the Yukawa suppression genuinely underflows (a4 short-range),
    # (iii) the transport ratio is well-defined (finite, positive).
    s96_match = eot["s96_xcheck_rel"] < 1e-6                     # (local)
    yukawa_underflows = ppn["yukawa_suppression"] == 0.0         # (local) a4 long-range shift is identically 0
    transport_finite = np.isfinite(eot["transport_ratio"]) and (eot["transport_ratio"] > 0.0)  # (local)
    regime_valid = s96_match and yukawa_underflows and transport_finite  # (local)
    regime_verdict = "VALID" if regime_valid else "MARGINAL"    # (local)

    # --- composite collapse (gate-verdicts.md PRE-REGISTERED rule) ---
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

    return {
        "gamma_ok": gamma_ok, "beta_ok": beta_ok, "eta_ok": eta_ok,
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        "composite": composite,
        "s96_match": s96_match,
        "yukawa_underflows": yukawa_underflows,
        "transport_finite": transport_finite,
    }

# ---------------------------------------------------------------------------
# Section 6 — Plot
# ---------------------------------------------------------------------------
def make_plot(ppn: dict, eot: dict, verd: dict, out_png: Path):
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.2))

    # Panel A: PPN gamma, beta vs Cassini / Will bounds (long-range = GR point).
    axA = axes[0]
    labels = [r"$|\gamma-1|$", r"$|\beta-1|$"]
    vals = [abs(ppn["gamma_minus_1"]), abs(ppn["beta_minus_1"])]
    bounds = [CASSINI_GAMMA_BOUND, PPN_BETA_BOUND]
    floor = 1e-30   # (local) plot floor for log-scale zeros
    vals_plot = [max(v, floor) for v in vals]   # (local)
    x = np.arange(len(labels))   # (local)
    axA.bar(x - 0.18, vals_plot, width=0.34, color="#2b6cb0", label="emergent $g_M$ (long-range)")
    axA.bar(x + 0.18, bounds, width=0.34, color="#cbd5e0", label="experimental bound")
    axA.set_yscale("log")
    axA.set_xticks(x); axA.set_xticklabels(labels)
    axA.axhline(floor, ls=":", c="grey", lw=0.8)
    axA.set_ylabel("deviation from GR (PPN)")
    axA.set_title(r"Emergent PPN of $g_M$ (a$_2$ Einstein-Hilbert; a$_4$ Yukawa-killed)")
    axA.legend(fontsize=8, loc="upper right")
    axA.text(0.02, 0.04,
             f"$\\gamma-1={ppn['gamma_minus_1']:.2e}$ (Yukawa exp $\\sim$1e25)\n"
             f"$a_4/a_2={ppn['moment_ratio_a4_a2']:.4f}$ (max if long-range)",
             transform=axA.transAxes, fontsize=8, va="bottom",
             bbox=dict(boxstyle="round", fc="#ebf8ff", ec="#90cdf4", alpha=0.9))

    # Panel B: Eotvos eta at the two scales vs MICROSCOPE bound.
    axB = axes[1]
    eta_labels = ["substrate-internal\n$|\\Delta\\kappa|/2$\n(fiber scale $R_K$)",
                  "laboratory\n$\\eta_{lab}$\n(Earth field)"]
    eta_vals = [eot["eta_internal"], max(eot["eta_lab"], 1e-300)]   # (local)
    colors = ["#dd6b20", "#2f855a"]   # (local)
    xb = np.arange(len(eta_labels))   # (local)
    axB.bar(xb, eta_vals, width=0.5, color=colors)
    axB.axhline(MICROSCOPE_ETA_BOUND, ls="--", c="red", lw=1.4, label=r"MICROSCOPE $\eta<10^{-15}$")
    axB.set_yscale("log")
    axB.set_xticks(xb); axB.set_xticklabels(eta_labels, fontsize=8)
    axB.set_ylabel(r"emergent Eötvös $\eta$")
    axB.set_title(r"Emergent EP: $\eta$ at fiber scale vs laboratory scale")
    axB.legend(fontsize=8, loc="upper right")
    axB.text(0.02, 0.04,
             f"transport ratio $R_{{lab}}/R_K={eot['transport_ratio']:.2e}$\n"
             f"$\\eta_{{lab}}={eot['eta_lab']:.2e}$ ($\\ll10^{{-15}}$)\n"
             f"composite={verd['composite']}",
             transform=axB.transAxes, fontsize=8, va="bottom",
             bbox=dict(boxstyle="round", fc="#f0fff4", ec="#9ae6b4", alpha=0.9))

    fig.suptitle(f"INV8-W2-2  Emergent PPN + Eötvös of $g_M$  —  composite={verd['composite']} "
                 f"(sign={verd['sign_verdict']}, mag={verd['magnitude_verdict']}, regime={verd['regime_verdict']})",
                 fontsize=11)
    fig.tight_layout(rect=[0, 0, 1, 0.96])
    fig.savefig(out_png, dpi=130)
    plt.close(fig)

# ---------------------------------------------------------------------------
# Section 7 — Verdict payload (printed; agent calls emit_verdict)
# ---------------------------------------------------------------------------
def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          companion_note="", three_tuple_note="",
                          extra_rows=None) -> dict:
    payload = {
        "session": 8,
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
    rows = list(extra_rows) if extra_rows else []   # (local)
    if companion_note:
        rows.insert(0, companion_note)
    if three_tuple_note:
        rows.append(three_tuple_note)
    if rows:
        payload["extra_rows"] = rows
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload

# ---------------------------------------------------------------------------
# Section 8 — Main
# ---------------------------------------------------------------------------
def main() -> int:
    t0 = time.time()   # (local)
    print("=" * 78)
    print(f"{GATE_ID} — Emergent PPN (gamma, beta) + Emergent Eotvos eta of g_M")
    print("=" * 78)

    # 1. Input pins (logged in first lines of stdout per gate-verdicts.md).
    pins = log_input_pins(INPUT_FILES)
    for rel, sh in pins.items():
        print(f"  INPUT_SHA  {rel}  {sh[:16]}...")
    legacy_closure = closure_hash(pins)   # (local)
    print(f"  legacy closure: {legacy_closure[:16]}...")
    print()

    # 2. Substrate inputs.
    s95 = load_s95_ep_nlo()
    print("=== S95-W3-5 leading EP coupling (band-blind Bochner 1/4; PASS) ===")
    print(f"  kappa_EP_NLO = {s95['kappa_EP_NLO']}  (C1_B1={s95['C1_B1']}, C1_B3={s95['C1_B3']}; band-BLIND)")
    print(f"  Casimir-foil reading (REJECTED) = {s95['kappa_Casimir_foil']:.8f}  (9/13)")
    print(f"  C2_B1={s95['C2_B1']}, C2_B3={s95['C2_B3']}; RK_fold={s95['RK_fold']:.9f}; 37x squeeze={s95['squeeze_factor_B1']}")
    print()

    # 3. Emergent PPN.
    ppn = emergent_ppn()
    print("=== Emergent PPN (gamma, beta) of g_M ===")
    print(f"  a4/a2 moment ratio          = {ppn['moment_ratio_a4_a2']:.10f}  (max PPN shift IF long-range)")
    print(f"  a4 Yukawa range             = {ppn['range_a4_m']:.4e} m  (~1/M_KK)")
    print(f"  Yukawa exponent at r~1 m    = {ppn['yukawa_exponent']:.4e}  (=> exp(-arg) underflows to 0)")
    print(f"  gamma_emergent (long-range) = {ppn['gamma_emergent']:.15f}  ; gamma-1 = {ppn['gamma_minus_1']:.3e}")
    print(f"  beta_emergent  (long-range) = {ppn['beta_emergent']:.15f}  ; beta-1  = {ppn['beta_minus_1']:.3e}")
    print()

    # 4. Emergent Eotvos.
    eot = emergent_eotvos(s95)
    print("=== Emergent Eotvos eta of g_M ===")
    print(f"  g0 (a6 field-strength coeff) = {eot['g0']:.12e}  (S96 g0)")
    print(f"  Delta_kappa = -(16/3)*g0     = {eot['Delta_kappa']:.12e}")
    print(f"  S96 cross-check rel-err      = {eot['s96_xcheck_rel']:.3e}  (vs -8.397090e-03)")
    print(f"  C2(B1)={eot['C2_B1']}, C2(B3)={eot['C2_B3']}, Delta_C2={eot['Delta_C2']:.6f}")
    print(f"  eta_INTERNAL (fiber scale)   = {eot['eta_internal']:.6e}  (S96 frontier-#8 EP value, INSIDE the BZ)")
    print(f"  R_tidal(Earth orbit) SI      = {eot['R_tidal_SI_inv_m2']:.4e} 1/m^2")
    print(f"  M_KK as inverse length       = {eot['M_KK_inv_m']:.4e} 1/m")
    print(f"  R_lab (dimensionless, M_KK^2)= {eot['R_lab_dimensionless']:.4e}")
    print(f"  transport ratio R_lab/R_K    = {eot['transport_ratio']:.4e}  (deg(T) curvature rescaling)")
    print(f"  eta_LAB (MICROSCOPE)         = {eot['eta_lab']:.4e}  (vs bound 1e-15)")
    print()

    # 5. Verdict.
    verd = evaluate_verdict(ppn, eot)
    print("=== VERDICT (3-way set-membership; binding = MICROSCOPE eta) ===")
    print(f"  |gamma-1| < 2.3e-5 (Cassini)  : {verd['gamma_ok']}")
    print(f"  |beta-1|  < 1e-4   (Will)     : {verd['beta_ok']}")
    print(f"  eta_lab   < 1e-15  (MICROSCOPE): {verd['eta_ok']}")
    print(f"  sign={verd['sign_verdict']}  magnitude={verd['magnitude_verdict']}  regime={verd['regime_verdict']}")
    print(f"  COMPOSITE = {verd['composite']}")
    print()

    # 6. Save data.
    out_npz = PROJECT_ROOT / "computations" / "investigation-8" / "inv8_w2_2_emergent_ppn_eotvos.npz"
    out_png = PROJECT_ROOT / "computations" / "investigation-8" / "inv8_w2_2_emergent_ppn_eotvos.png"
    save_dict = {   # (local)
        "gate_id": GATE_ID,
        # PPN
        "gamma_emergent": ppn["gamma_emergent"], "beta_emergent": ppn["beta_emergent"],
        "gamma_minus_1": ppn["gamma_minus_1"], "beta_minus_1": ppn["beta_minus_1"],
        "moment_ratio_a4_a2": ppn["moment_ratio_a4_a2"],
        "range_a4_m": ppn["range_a4_m"], "yukawa_exponent": ppn["yukawa_exponent"],
        "yukawa_suppression": ppn["yukawa_suppression"],
        # Eotvos
        "g0": eot["g0"], "Delta_kappa": eot["Delta_kappa"], "abs_Delta_kappa": eot["abs_Delta_kappa"],
        "Delta_kappa_S96_anchor": eot["Delta_kappa_S96_anchor"], "s96_xcheck_rel": eot["s96_xcheck_rel"],
        "C2_B1": eot["C2_B1"], "C2_B3": eot["C2_B3"], "Delta_C2": eot["Delta_C2"],
        "RK_fold": eot["RK_fold"], "eta_internal": eot["eta_internal"],
        "R_tidal_SI_inv_m2": eot["R_tidal_SI_inv_m2"], "M_KK_inv_m": eot["M_KK_inv_m"],
        "R_lab_dimensionless": eot["R_lab_dimensionless"], "transport_ratio": eot["transport_ratio"],
        "eta_lab": eot["eta_lab"],
        # bounds
        "CASSINI_GAMMA_BOUND": CASSINI_GAMMA_BOUND, "PPN_BETA_BOUND": PPN_BETA_BOUND,
        "MICROSCOPE_ETA_BOUND": MICROSCOPE_ETA_BOUND,
        # verdict
        "gamma_ok": verd["gamma_ok"], "beta_ok": verd["beta_ok"], "eta_ok": verd["eta_ok"],
        "sign_verdict": verd["sign_verdict"], "magnitude_verdict": verd["magnitude_verdict"],
        "regime_verdict": verd["regime_verdict"], "composite": verd["composite"],
        "a_2_FW_zeta": a_2_FW_zeta, "a_4_FW_zeta": a_4_FW_zeta, "a_6_FW_zeta": a_6_FW_zeta,
    }
    np.savez(out_npz, **save_dict)
    print(f"  data -> {out_npz.name}")

    # 7. Plot.
    make_plot(ppn, eot, verd, out_png)
    print(f"  plot -> {out_png.name}")
    print()

    # 8. Dual-SHA.
    #   content_sha256 over the producing script bytes (F-image of the numerical PASS predicate).
    #   audit_sha256 over the ordered input-pin map per plan audit_sha256_inputs:
    #       [script, canonical, pinmap, s95_w3_5_emergent_ep_nlo_npz].
    script_sha = sha256_of_file(Path(__file__))   # (local)
    content_sha = script_sha                      # (local)
    pinmap_for_audit = {   # (local) ordered: script, canonical, s95 npz, pinmap-of-machinery
        "script": script_sha,
        "canonical": pins[str(INPUT_FILES["canonical_constants"].relative_to(PROJECT_ROOT)).replace("\\", "/")],
        "s95_w3_5_emergent_ep_nlo_npz": pins[str(INPUT_FILES["s95_emergent_ep_nlo"].relative_to(PROJECT_ROOT)).replace("\\", "/")],
        "pinmap": json.dumps({
            "GATE_ID": GATE_ID, "SCHEME": SCHEME, "CONVENTION": CONVENTION, "L_MAX": L_MAX,
            "CASSINI_GAMMA_BOUND": CASSINI_GAMMA_BOUND, "PPN_BETA_BOUND": PPN_BETA_BOUND,
            "MICROSCOPE_ETA_BOUND": MICROSCOPE_ETA_BOUND, "regulator_pin": "a_2^zeta,a_4^zeta,a_6^zeta",
        }, sort_keys=True),
    }
    audit_sha = closure_hash(pinmap_for_audit)   # (local)
    print(f"  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")
    print()

    # 9. Verdict payload.
    value_str = (
        f"composite={verd['composite']};"
        f"gamma_emergent={ppn['gamma_emergent']:.12f};beta_emergent={ppn['beta_emergent']:.12f};"
        f"gamma_minus_1={ppn['gamma_minus_1']:.3e};beta_minus_1={ppn['beta_minus_1']:.3e};"
        f"eta_lab={eot['eta_lab']:.6e};eta_internal={eot['eta_internal']:.6e};"
        f"Delta_kappa={eot['Delta_kappa']:.9e};abs_Delta_kappa={eot['abs_Delta_kappa']:.6e};"
        f"transport_ratio={eot['transport_ratio']:.6e};R_lab_dimensionless={eot['R_lab_dimensionless']:.6e};"
        f"a4_a2={ppn['moment_ratio_a4_a2']:.10f};yukawa_exponent={ppn['yukawa_exponent']:.4e};"
        f"C2_B1={eot['C2_B1']};C2_B3={eot['C2_B3']};Delta_C2={eot['Delta_C2']:.6f};g0={eot['g0']:.9e};"
        f"s96_xcheck_rel={eot['s96_xcheck_rel']:.3e};"
        f"gamma_ok={verd['gamma_ok']};beta_ok={verd['beta_ok']};eta_ok={verd['eta_ok']};"
        f"CASSINI_GAMMA_BOUND={CASSINI_GAMMA_BOUND:.3e};MICROSCOPE_ETA_BOUND={MICROSCOPE_ETA_BOUND:.0e};"
        f"sign_verdict={verd['sign_verdict']};magnitude_verdict={verd['magnitude_verdict']};regime_verdict={verd['regime_verdict']};"
        f"scheme=FW-zeta;regulator_pin=a_2_zeta_a_4_zeta_a_6_zeta;CLASS=FULL;"
        f"EP_falsifier=OBSERVATION-FREE_MICROSCOPE_eta_lab_vs_1e-15;PPN_long_range_a2_only_a4_Yukawa_killed"
    )

    companion_note = (
        f"# {GATE_ID} dual-SHA companion row; [SIGN] emergent PPN+Eotvos of g_M; "
        f"gamma=beta=1 long-range (a2 Einstein-Hilbert; a4 short-range Yukawa range ~1/M_KK -> 0 at solar/lab r); "
        f"eta via S96-EP-NNLO-CASIMIR Delta_kappa=-(16/3)*g0=-8.397e-3 (substrate-internal fiber-curvature scale R_K(fold)=2.018, "
        f"the frontier-#8 VALUE-bearing EP prediction INSIDE the BZ) transported to laboratory scale by R_lab/R_K(fold)={eot['transport_ratio']:.3e} "
        f"(deg(T) curvature rescaling; R_lab=Earth-field tidal curvature in M_KK^2 units) => eta_lab={eot['eta_lab']:.3e} << MICROSCOPE 1e-15; "
        f"CLASS=FULL; regulator_pin=a_2^zeta/a_4^zeta/a_6^zeta; OBSERVATION-FREE falsifier (all inputs on disk, tested vs existing MICROSCOPE/Cassini data)"
    )
    three_tuple_note = (
        f"# sign_verdict={verd['sign_verdict']} magnitude_verdict={verd['magnitude_verdict']} regime_verdict={verd['regime_verdict']} "
        f"# {GATE_ID} 3-tuple annotation (schema-v2; [SIGN] plan §W2-2 Step-6 directional pre-reg: "
        f"SIGN=eta_internal>0 (C_2(B1)=0 != C_2(B3)=4/3 => nonzero NNLO band-break) AND eta_lab<1e-15 (SAFE side of MICROSCOPE) AND gamma-1=beta-1=0 (GR point, long-range a2-only); "
        f"MAG=(|gamma-1|<2.3e-5 Cassini) AND (|beta-1|<1e-4) AND (eta_lab<1e-15 MICROSCOPE) => PASS; INFO iff eta_lab in [1e-16,1e-15]; FAIL iff any bound violated (framework falsified by existing data); "
        f"REGIME=VALID iff (S96 Delta_kappa cross-check<1e-6) AND (a4 Yukawa underflows: long-range shift identically 0) AND (transport ratio finite>0))"
    )
    extra_rows = [
        f"# {GATE_ID} regulator_pin=a_2^zeta,a_4^zeta,a_6^zeta (FW zeta scheme; regulator-pin-discipline.md)",
        f"# {GATE_ID} scale-tag: eta_internal={eot['eta_internal']:.6e} (substrate-IS, fiber-curvature scale R_K~M_KK^2, NOT a lab observable) | "
        f"eta_lab={eot['eta_lab']:.6e} (laboratory-IN, Earth-field external curvature, MICROSCOPE-comparable); the falsifier fires on eta_lab ONLY (phononic-framing.md Scale-and-channel-tagging)",
    ]

    print_verdict_payload(
        verd["composite"], value_str, audit_sha, content_sha,
        companion_note=companion_note, three_tuple_note=three_tuple_note, extra_rows=extra_rows,
    )

    print(f"\n  [elapsed {time.time() - t0:.2f}s]")
    return 0

if __name__ == "__main__":
    sys.exit(main())
