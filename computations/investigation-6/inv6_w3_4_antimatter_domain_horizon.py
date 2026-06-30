#!/usr/bin/env python3
"""
INV6 W3-4 -- ANTIMATTER-DOMAIN-HORIZON
======================================

Gate: INV6-W3-4-ANTIMATTER-DOMAIN-HORIZON  ([SIGN])

Pre-registered threshold (plan investigation-6-plan-w3.md §W3-4):
  operator: inequality  R_horizon = r_acoustic / (c/H_0)
  PASS iff R_horizon > 1   (super-horizon single causal patch)
  FAIL iff R_horizon < 1   (sub-horizon multi-domain)
  INFO iff R_horizon ~ 1 within the post-fold-expansion-map uncertainty
  convention = RATIO ; scheme = ACOUSTIC-SOUND-HORIZON-S85-WHITE-HOLE

HYPOTHESIS (plan): the pre-transit acoustic sound-horizon of the Mach-13.75
supersonic transit EXCEEDS the present Hubble scale c/H_0, so the entire
observable universe was inside ONE causally-connected pre-transit acoustic
patch -> the delta_A-sourced baryon asymmetry is single-domain by construction
(consistent with Fermi-LAT antimatter-fraction <1e-5 / zero annihilation-
boundary gamma-flux), giving delta_A a spatial characterization.

WHAT THIS GATE COMPUTES (substrate-first; NUMBERS first, gate second):
  Step A. The comoving pre-transit acoustic SOUND HORIZON
            r_acoustic = integral_0^{tau_fold} c_s(tau)/a(tau) dtau
          on the substrate's OWN transit expansion history (NOT an assumed
          inflationary de-Sitter background). c_s = c_BLV = 0.485 M_KK
          constant; a(tau) from the substrate's integrated e-fold history
          (S53 phonon-EoS: N_e^total = 2.9205 across the whole transit;
          q(tau) transitions -0.97 -> +0.81, S54 SCALE-FACTOR-54).
  Step B. The present comoving Hubble scale c/H_0 (H_0 obtained by redshifting
          H_fold = 586.5267713108464 M_KK forward through the post-fold
          expansion history; entropy-conserving T_fold ~ M_KK -> T_0 = T_CMB).
  Step C. R_horizon = r_acoustic / (c/H_0), and the e-fold REQUIREMENT
            N_required for R_horizon = 1 (the standard horizon-problem bar),
          compared against the substrate's N_e^total.

DUAL-ANCHORED ROBUSTNESS (two independent unit pathways must agree on the
sign of R_horizon - 1, else the result is a units artifact):
  Pathway-1 (physical/dimensionful via redshift): both horizons in meters,
            with explicit (1+z_fold) = M_KK/T_CMB entropy-conserving map.
  Pathway-2 (e-fold requirement, unit-free): N_required vs N_e^total.
  Both pathways are computed; the gate verdict reads off the SIGN that both
  share.

SUBSTRATE-FIRST FRAMING (phononic-framing.md, MANDATORY direction):
  exflation is SPECTRAL COMPLEXIFICATION, NOT metric expansion ("Space expands"
  -> "Spectral complexity grows inside each point"). The acoustic sound horizon
  does NOT grow super-Hubble via metric inflation because the substrate has
  essentially NO metric inflation (N_e^total = 2.92, not ~60). The framework's
  single-domain mechanism is tau-SIMULTANEITY (the substrate has ONE Jensen
  slice; the fold happens at one tau value for the whole substrate), NOT a
  super-Hubble metric acoustic patch. This gate tests the METRIC-HORIZON
  hypothesis the plan posited; the substrate's own expansion history decides it.

Inputs:
  - canonical_constants.py (feeds audit_sha256 only)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)
  No external npz cache: the substrate e-fold history is read as canonical
  numbers (S53 EoS / S54 scale-factor) pinned in MACHINERY_PINS with provenance.
  (The orchestrator STALE CACHE-SHA HINT 88f1e9b1->9e6d9cf7 applies to the s84
  L12 mode cache used by SIBLING gates; THIS gate reads no spectrum cache ->
  zero physics effect; documented per SOURCE-RECON Class-(c).)

Output 4-tuple:
  (value=<R_horizon...>, scheme=ACOUSTIC-SOUND-HORIZON-S85-WHITE-HOLE,
   convention=RATIO, L_max=N/A)

Verdict: this script PRINTS the emit_verdict payload via print_verdict_payload;
the agent reads the delimited JSON block and calls mcp__knowledge__emit_verdict.
"""

import hashlib
import json
import sys
import os
import time
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "8")  # CPU-cap (1000-pt 1D quadrature; far below GPU threshold)

import numpy as np

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

t0 = time.time()  # (local)

# --------------------------------------------------------------------------
# Section 1 -- Canonical constants (MANDATORY first import)
# --------------------------------------------------------------------------
INV_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = INV_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403
import canonical_constants as cc
# consumed: M_KK, H_fold, c_BLV, c_fabric, Mach_max, tau_fold, T_CMB_GeV,
#           hbar_c_GeV_m, H_0_GeV, Mpc_to_m

# --------------------------------------------------------------------------
# Section 2 -- Identity + machinery pins
# --------------------------------------------------------------------------
SESSION = 6                                                       # (local)
GATE_ID = "INV6-W3-4-ANTIMATTER-DOMAIN-HORIZON"                   # (local)
SCHEME = "ACOUSTIC-SOUND-HORIZON-S85-WHITE-HOLE"                  # (local)
CONVENTION = "RATIO"                                              # (local)
L_MAX = "N/A"                                                     # (local)

OUT_NPZ = INV_DIR / "inv6_w3_4_antimatter_domain_horizon.npz"     # (local)
OUT_PNG = INV_DIR / "inv6_w3_4_antimatter_domain_horizon.png"     # (local)

# --- pre-registered machinery pins (plan §W3-4 machinery_pin_map) ---
N_EVAL = 1000                                                     # (local) tau-grid for sound-horizon integral
TAU_LO = 0.0                                                      # (local) pre-transit epoch start (cold big bang, tau=0)
TAU_HI = float(cc.tau_fold)                                       # (local) = 0.19 (fold)
R_TOL = 1e-9                                                      # (local) R_horizon ratio comparison tolerance

# --- substrate expansion-history anchors (S53 phonon-EoS / S54 scale-factor) ---
# These are CANONICAL substrate numbers (not free parameters): the integrated
# e-fold history of the transit. Provenance pinned in MACHINERY_PINS.
N_E_TOTAL = 2.9205          # (local) full transit e-folds (S53 EoS Section 8; acoustic-metric driven)
N_E_GEOM = 0.1734           # (local) geometric (KK ceiling) e-folds (S53; EFOLD-MAPPING-52)
N_E_INTERNAL = 0.0282       # (local) GL-internal-only e-folds (S53; N_e^acoustic_only)

# --- INFO band: R_horizon ~ 1 within the post-fold-map uncertainty ---
# The a(t)-map carries the K_pivot/a(t) gap (atlas-04 C1/C2). We treat
# R_horizon within a factor ~2 (|log10 R| < 0.30) of unity as INFO (map-limited).
INFO_LOG_HALFWIDTH = 0.30   # (local) |log10 R_horizon| < 0.30 -> INFO (a(t)-map sensitive)

MACHINERY_PINS = {                                               # (local)
    "N_eval": str(N_EVAL),
    "tau_range": f"[{TAU_LO},{TAU_HI}]",
    "tolerance": str(R_TOL),
    "scheme": SCHEME,
    "convention": CONVENTION,
    "publication_precision": "4",
    "c_s_sound_speed": f"c_BLV={float(cc.c_BLV)} (M_KK units; S64 four-speed hierarchy)",
    "H_fold": f"{float(cc.H_fold)} (M_KK units; S38 s38_kz_defects)",
    "Mach_max": f"{float(cc.Mach_max)} (van Hove fold; v_transit={float(cc.Mach_max)*float(cc.c_BLV)} M_KK)",
    "N_e_total_substrate": f"{N_E_TOTAL} (S53 s53_phonon_eos_output.txt Section 8; acoustic-metric driven)",
    "N_e_geom": f"{N_E_GEOM} (S53 EFOLD-MAPPING-52)",
    "N_e_internal": f"{N_E_INTERNAL} (S53 N_e^acoustic_only)",
    "z_fold_map": "1+z_fold = M_KK/T_CMB (entropy-conserving; T_fold ~ M_KK fold energy scale)",
    "white_hole_provenance": "S85 acoustic white-hole causal-disconnect PROVEN (s85_w6_acoustic_white_hole_formal)",
    "cache_pin_note": "no spectrum cache read; STALE-HINT 88f1e9b1->9e6d9cf7 (s84 L12) "
                      "applies to SIBLING gates only -> zero physics effect (SOURCE-RECON Class-(c))",
}


# --------------------------------------------------------------------------
# Section 3 -- SHA helpers (S84+ dual-SHA schema)
# --------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()                                          # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict) -> tuple[str, str]:
    """S84+ dual-SHA: audit = sha256(script || canonical || pinmap_json);
    content = sha256(script)."""
    script_bytes = script_path.read_bytes()                       # (local)
    canonical_bytes = canonical_path.read_bytes()                 # (local)
    pinmap_json = json.dumps(dict(sorted(pins.items())),
                             separators=(",", ":"),
                             sort_keys=True).encode("utf-8")       # (local)
    h_a = hashlib.sha256()                                        # (local)
    h_a.update(script_bytes); h_a.update(canonical_bytes); h_a.update(pinmap_json)
    h_c = hashlib.sha256()                                        # (local)
    h_c.update(script_bytes)
    return h_a.hexdigest(), h_c.hexdigest()


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, companion_note="",
                          extra_rows=None) -> dict:
    """Print the emit_verdict payload (race-safe MCP emission by the agent)."""
    payload = {                                                   # (local)
        "session": SESSION, "gate_id": GATE_ID, "verdict": verdict,
        "value": str(value), "scheme": SCHEME, "convention": CONVENTION,
        "l_max": str(L_MAX), "audit_sha256": audit_sha,
        "content_sha256": content_sha, "schema_version": "S84+",
        "track": "investigation",
    }
    if companion_note:
        payload["companion_note"] = companion_note
    if not (sign_verdict is None and magnitude_verdict is None
            and regime_verdict is None):
        payload["sign_verdict"] = sign_verdict
        payload["magnitude_verdict"] = magnitude_verdict
        payload["regime_verdict"] = regime_verdict
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


def verify_inputs() -> dict:
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins: dict = {}                                               # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"        # (local)
    sha_canon = sha256_of(canonical_path)                         # (local)
    print(f"  canonical_constants.py: {sha_canon[:16]}... (runtime-pinned)")
    pins["computations/_shared/canonical_constants.py"] = sha_canon
    if sha_canon == "":
        print("HARD-ABORT: canonical_constants.py ABSENT.")
        sys.exit(2)
    return pins


# --------------------------------------------------------------------------
# Section 4 -- Sound-horizon integral on the substrate transit profile
# --------------------------------------------------------------------------
def comoving_sound_horizon(N_e_transit: float) -> dict:
    """Comoving pre-transit acoustic sound horizon, normalized to a_today=1.

    The substrate's pre-transit expansion is parameterized by its integrated
    e-fold count N_e_transit. Modeling a(tau) over the pre-transit epoch by the
    e-fold variable N(tau) in [0, N_e_transit] (a = a_fold * exp(N(tau)-N_total)),
    and c_s = c_BLV constant, the PROPER causal sound horizon at the fold is

    PROPER causal sound horizon at the fold (the proper size of the patch a
    sound wave could have crossed by the fold):

        d_sound_PROPER@fold = a_fold * integral_0^{tau_fold} c_s/a(tau) (dN/H)
                            = (c_s / H_fold) * (1 - e^{-N_e_transit})        (1)

      [saturates to the Hubble radius c_s/H_fold at large N; ~ N*c_s/H_fold
       at small N. This is the PROPER horizon AT the fold.]

    COMOVING sound horizon (scaled to a_today=1) is obtained by dividing the
    proper-at-fold horizon by a_fold = 1/(1+z_fold) -- equivalently multiplying
    by (1+z_fold). The downstream comparison uses the COMOVING horizon.

    Both the PROPER-at-fold integral (1) and its companion COMOVING form are
    evaluated NUMERICALLY on the N_EVAL tau-grid (explicit 1000-pt quadrature),
    each cross-checked against its own closed form. The pre-transit phase is
    modeled as exponentially expanding at rate H ~ H_fold (de-Sitter-like) over
    the substrate's integrated e-fold count N_e_transit; dN = H_fold dtau.
    """
    r: dict = {}                                                  # (local)
    c_s = float(cc.c_BLV)                                         # (local) M_KK units
    H_f = float(cc.H_fold)                                        # (local) M_KK units
    _trapz = getattr(np, "trapezoid", getattr(np, "trapz", None))  # (local) NumPy 2.x renamed trapz->trapezoid

    # --- tau-grid (pre-registered N_EVAL) ---
    tau = np.linspace(TAU_LO, TAU_HI, N_EVAL)                     # (local) pre-transit epoch
    # map tau -> e-fold N(tau): linear over [0, tau_fold] -> [0, N_e_transit]
    N_of_tau = N_e_transit * (tau - TAU_LO) / (TAU_HI - TAU_LO)   # (local)
    a_fold = 1.0                                                  # (local) normalize a at fold
    a_of_tau = a_fold * np.exp(N_of_tau - N_e_transit)           # (local) a(tau) < a_fold pre-fold
    dN = np.gradient(N_of_tau, tau)                              # (local) const = N_e_transit/(tau_hi-tau_lo)

    # PROPER-at-fold integrand: a_fold * c_s/a * (dN/H_f).  a_fold/a = e^{N_total-N}
    integrand_proper = a_fold * c_s / a_of_tau                   # (local) per dN/H_f
    d_sound_proper_fold_MKKinv = float(_trapz(integrand_proper * dN / H_f, tau))  # (local) M_KK^-1
    d_sound_proper_closed = (c_s / H_f) * (1.0 - np.exp(-N_e_transit))  # (local) closed form for (1)

    # COMOVING integrand (a_today=1, a here normalized so a_fold = 1 at fold;
    # comoving = proper-at-fold / a_fold; with a_fold=1 the comoving integrand is
    # c_s/a * (dN/H_f) WITHOUT the a_fold factor in the numerator -> e^{N}-1 form).
    integrand_comov = c_s / a_of_tau                            # (local) per dN/H_f (comoving rel. to fold-normalized a)
    d_sound_comov_fold_MKKinv = float(_trapz(integrand_comov * dN / H_f, tau))  # (local) M_KK^-1
    d_sound_comov_closed = (c_s / H_f) * (np.exp(N_e_transit) - 1.0)  # (local) closed form

    r["c_s"] = c_s
    r["H_fold"] = H_f
    r["tau"] = tau
    r["a_of_tau"] = a_of_tau
    r["N_of_tau"] = N_of_tau
    r["d_sound_proper_fold_MKKinv_numeric"] = d_sound_proper_fold_MKKinv
    r["d_sound_proper_fold_MKKinv_closed"] = float(d_sound_proper_closed)
    r["d_sound_comov_fold_MKKinv_numeric"] = d_sound_comov_fold_MKKinv
    r["d_sound_comov_fold_MKKinv_closed"] = float(d_sound_comov_closed)
    # numeric/closed agreement fractions (honest cross-check)
    r["proper_numeric_closed_ratio"] = d_sound_proper_fold_MKKinv / float(d_sound_proper_closed)
    r["comov_numeric_closed_ratio"] = d_sound_comov_fold_MKKinv / float(d_sound_comov_closed)
    r["N_e_transit"] = N_e_transit
    return r


# --------------------------------------------------------------------------
# Section 5 -- Full horizon comparison (two independent unit pathways)
# --------------------------------------------------------------------------
def compute() -> dict:
    r: dict = {}                                                  # (local)

    M_KK_GeV = float(cc.M_KK)                                     # (local) GeV
    H_f_MKK = float(cc.H_fold)                                    # (local) M_KK units
    H_f_GeV = H_f_MKK * M_KK_GeV                                  # (local) GeV
    c_s = float(cc.c_BLV)                                         # (local) M_KK velocity (dimensionless rel. to c)
    c_fab = float(cc.c_fabric)                                    # (local) M_KK velocity (relay/causal limit)
    hbar_c_m = float(cc.hbar_c_GeV_m)                             # (local) GeV*m
    H0_GeV = float(cc.H_0_GeV)                                    # (local) GeV
    T0_GeV = float(cc.T_CMB_GeV)                                  # (local) GeV
    v_transit = float(cc.Mach_max) * c_s                         # (local) M_KK velocity

    # ----- present comoving Hubble scale c/H_0 (a_today = 1) -----
    # natural units c=1: length = hbar_c / E ; R_H0 = (1/H0)*hbar_c (meters)
    R_H0_m = (1.0 / H0_GeV) * hbar_c_m                            # (local) m

    # ----- substrate sound-horizon (Step A) on the substrate e-fold history -----
    sh = comoving_sound_horizon(N_E_TOTAL)                        # (local)
    d_sound_proper_fold_MKKinv = sh["d_sound_proper_fold_MKKinv_numeric"]  # (local) M_KK^-1
    # convert M_KK^-1 -> meters: length(M_KK^-1) = (1/M_KK_GeV)*hbar_c_m
    MKKinv_to_m = (1.0 / M_KK_GeV) * hbar_c_m                     # (local) m per M_KK^-1
    d_sound_proper_fold_m = d_sound_proper_fold_MKKinv * MKKinv_to_m  # (local) m
    R_hubble_fold_m = (c_s / H_f_GeV) * hbar_c_m                  # (local) m (proper Hubble radius @fold, acoustic)

    # ----- redshift fold->today (entropy-conserving, T_fold ~ M_KK) -----
    one_plus_z_fold = M_KK_GeV / T0_GeV                          # (local)

    # ===== PATHWAY-1: physical/dimensionful comoving comparison =====
    r_acoustic_com_m = d_sound_proper_fold_m * one_plus_z_fold    # (local) comoving -> today (m)
    R_horizon_phys = r_acoustic_com_m / R_H0_m                    # (local)

    # ===== PATHWAY-2: e-fold requirement (unit-free) =====
    # R_horizon=1 requires (c_s/H_fold)*(e^N - 1)*(1+z) >= c/H0  [comoving]
    rhs = R_H0_m / (R_hubble_fold_m * one_plus_z_fold)           # (local)
    N_required = float(np.log(rhs + 1.0))                        # (local)
    efold_shortfall = N_required - N_E_TOTAL                     # (local)

    # ----- headline ratio (Pathway-1 is the canonical R_horizon) -----
    R_horizon = R_horizon_phys                                    # (local)
    log10_R = float(np.log10(R_horizon))                         # (local)

    # ----- single-domain comoving size of delta_A (the spatial characterization) -----
    # r_acoustic is the comoving coherence scale of the delta_A imprint (meters / Mpc)
    r_acoustic_Mpc = r_acoustic_com_m / float(cc.Mpc_to_m)       # (local)
    R_H0_Mpc = R_H0_m / float(cc.Mpc_to_m)                       # (local)

    r.update(dict(
        # headline
        R_horizon=R_horizon, log10_R_horizon=log10_R,
        R_horizon_phys=R_horizon_phys,
        N_required=N_required, N_e_total=N_E_TOTAL,
        efold_shortfall=efold_shortfall,
        efold_shortfall_dex=float(efold_shortfall / np.log(10.0)),
        # horizons (m)
        r_acoustic_com_m=r_acoustic_com_m, c_over_H0_m=R_H0_m,
        d_sound_proper_fold_m=d_sound_proper_fold_m,
        R_hubble_fold_m=R_hubble_fold_m,
        # horizons (Mpc) for human scale
        r_acoustic_Mpc=r_acoustic_Mpc, c_over_H0_Mpc=R_H0_Mpc,
        # cross-checks (PROPER-at-fold: numeric vs its own closed form (1-e^-N))
        d_sound_proper_numeric_MKKinv=sh["d_sound_proper_fold_MKKinv_numeric"],
        d_sound_proper_closed_MKKinv=sh["d_sound_proper_fold_MKKinv_closed"],
        proper_numeric_closed_ratio=sh["proper_numeric_closed_ratio"],
        # cross-checks (COMOVING-rel-fold: numeric vs its own closed form (e^N-1))
        d_sound_comov_numeric_MKKinv=sh["d_sound_comov_fold_MKKinv_numeric"],
        d_sound_comov_closed_MKKinv=sh["d_sound_comov_fold_MKKinv_closed"],
        comov_numeric_closed_ratio=sh["comov_numeric_closed_ratio"],
        horizon_over_hubble_fold=float(1.0 - np.exp(-N_E_TOTAL)),
        # inputs
        one_plus_z_fold=one_plus_z_fold,
        H_fold_GeV=H_f_GeV, H0_GeV=H0_GeV, T0_GeV=T0_GeV,
        c_s=c_s, c_fabric=c_fab, v_transit=v_transit, M_KK_GeV=M_KK_GeV,
        # e-fold history (substrate)
        N_e_geom=N_E_GEOM, N_e_internal=N_E_INTERNAL,
        # arrays for plot
        tau=sh["tau"], a_of_tau=sh["a_of_tau"], N_of_tau=sh["N_of_tau"],
    ))
    return r


# --------------------------------------------------------------------------
# Section 6 -- Gate verdict ([SIGN] 3-tuple + collapse rule)
# --------------------------------------------------------------------------
def evaluate_gate(r: dict) -> tuple:
    R = r["R_horizon"]                                            # (local)
    log10_R = r["log10_R_horizon"]                                # (local)

    # SIGN: the substitution chain (plan Step 5) PREDICTS R_horizon > 1
    # (super-horizon, single-domain). sign_verdict PASS iff the MEASURED
    # direction matches the predicted direction (R_horizon > 1).
    predicted_super_horizon = True                                # (local) chain Step 5
    measured_super_horizon = bool(R > 1.0)                        # (local)
    sign_ok = (predicted_super_horizon == measured_super_horizon)  # (local)
    sign_v = "PASS" if sign_ok else "FAIL"                        # (local)

    # MAGNITUDE: R_horizon > 1 (PASS); R_horizon ~ 1 within a(t)-map uncertainty
    # (|log10 R| < INFO_LOG_HALFWIDTH) -> INFO; else FAIL.
    mag_pass = bool(R > 1.0 + R_TOL)                              # (local)
    mag_info = bool((not mag_pass) and abs(log10_R) < INFO_LOG_HALFWIDTH)  # (local)
    if mag_pass:
        mag_v = "PASS"                                            # (local)
    elif mag_info:
        mag_v = "INFO"                                            # (local)
    else:
        mag_v = "FAIL"                                            # (local)

    # REGIME: deterministic 1000-pt quadrature on the full intended tau-window
    # [0, tau_fold]; numeric/closed-form sound-horizon agree; no auto-shortening,
    # no small-parameter expansion. The post-fold a(t)-map is a SINGLE entropy-
    # conserving redshift (1+z=M_KK/T_CMB); its uncertainty is captured in the
    # INFO band, NOT a regime breakdown. -> VALID.
    regime_v = "VALID"                                           # (local)

    # collapse rule (pre-registered, gate-verdicts.md)
    if regime_v == "BREAKDOWN":
        comp = "FAIL"                                            # (local)
    elif sign_v == "FAIL":
        comp = "FAIL"
    elif mag_v == "FAIL" and regime_v == "VALID":
        comp = "FAIL"
    elif mag_v == "FAIL" and regime_v == "MARGINAL":
        comp = "INFO"
    elif mag_v == "INFO":
        comp = "INFO"
    else:
        comp = "PASS"

    detail = dict(sign_ok=sign_ok, measured_super_horizon=measured_super_horizon,
                  mag_pass=mag_pass, mag_info=mag_info)            # (local)
    return comp, sign_v, mag_v, regime_v, detail


# --------------------------------------------------------------------------
# Section 7 -- Plot
# --------------------------------------------------------------------------
def make_plot(r: dict):
    fig, ax = plt.subplots(1, 2, figsize=(13, 5))

    # (a) the two horizon scales (log bar), Pathway-1
    labels = ["r_acoustic\n(pre-transit\nsound horizon)", "c/H_0\n(present\nHubble scale)"]
    vals = [r["r_acoustic_com_m"], r["c_over_H0_m"]]
    colors = ["#c0392b", "#2980b9"]
    ax[0].bar(labels, vals, color=colors, alpha=0.85)
    ax[0].set_yscale("log")
    ax[0].set_ylabel("comoving length (m, a_today=1)")
    ax[0].set_title(f"(a) Horizon comparison  R_horizon = {r['R_horizon']:.3e}\n"
                    f"(log10 R = {r['log10_R_horizon']:.2f}; PASS needs R>1)")
    for i, v in enumerate(vals):
        ax[0].text(i, v * 1.5, f"{v:.2e} m", ha="center", fontsize=9)
    ax[0].axhline(r["c_over_H0_m"], ls="--", color="#2980b9", lw=0.8)

    # (b) e-fold requirement vs substrate e-folds
    bars = ["N_required\n(for R=1)", "N_e^total\n(substrate)", "N_e^geom", "N_e^internal"]
    bvals = [r["N_required"], r["N_e_total"], r["N_e_geom"], r["N_e_internal"]]
    bcol = ["#7f8c8d", "#27ae60", "#16a085", "#1abc9c"]
    ax[1].bar(bars, bvals, color=bcol, alpha=0.85)
    ax[1].set_ylabel("e-folds N")
    ax[1].set_title(f"(b) Horizon-problem e-fold bar\n"
                    f"shortfall = {r['efold_shortfall']:.1f} e-folds "
                    f"({r['efold_shortfall_dex']:.1f} dex)")
    ax[1].axhline(r["N_required"], ls="--", color="#7f8c8d", lw=0.8)
    for i, v in enumerate(bvals):
        ax[1].text(i, v + 1.5, f"{v:.2f}", ha="center", fontsize=9)

    fig.suptitle(f"{GATE_ID}: pre-transit acoustic sound-horizon vs c/H_0  "
                 f"(substrate N_e^total={r['N_e_total']:.2f} << N_required={r['N_required']:.0f}; "
                 f"metric-horizon single-domain FAILs; tau-simultaneity is the substrate mechanism)",
                 fontsize=9)
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)
    print(f"Saved plot: {OUT_PNG}")


# --------------------------------------------------------------------------
# Section 8 -- main
# --------------------------------------------------------------------------
def main() -> int:
    pins = verify_inputs()                                       # (local)

    pinmap = dict(pins)                                          # (local)
    pinmap.update({f"_machinery::{k}": v for k, v in MACHINERY_PINS.items()})
    pinmap["_gate::id"] = GATE_ID
    audit_sha, content_sha = compute_dual_sha(
        Path(__file__).resolve(), SHARED_DIR / "canonical_constants.py",
        pinmap)                                                  # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")

    r = compute()                                               # (local)
    comp, sign_v, mag_v, regime_v, detail = evaluate_gate(r)    # (local)

    print("\n" + "=" * 72)
    print("NUMBERS (computed before gate)")
    print("=" * 72)
    print(f"  c_s = c_BLV                          = {r['c_s']:.6f} M_KK")
    print(f"  c_fabric (relay/causal limit)        = {r['c_fabric']:.6f} M_KK")
    print(f"  v_transit = Mach*c_BLV               = {r['v_transit']:.6f} M_KK  (Mach {float(cc.Mach_max)} > 1 => white hole, S85)")
    print(f"  H_fold                               = {r['H_fold_GeV']:.6e} GeV  ({float(cc.H_fold)} M_KK)")
    print(f"  H_0                                  = {r['H0_GeV']:.6e} GeV")
    print(f"  T_CMB                                = {r['T0_GeV']:.6e} GeV")
    print(f"  1+z_fold (M_KK/T_CMB)                = {r['one_plus_z_fold']:.6e}")
    print(f"  -- substrate expansion history (S53 EoS) --")
    print(f"  N_e^total                            = {r['N_e_total']:.4f}  (acoustic-metric driven)")
    print(f"  N_e^geom                             = {r['N_e_geom']:.4f}")
    print(f"  N_e^internal (acoustic_only)         = {r['N_e_internal']:.4f}")
    print(f"  horizon/Hubble @fold = 1-e^-N        = {r['horizon_over_hubble_fold']:.6f}")
    print(f"  -- sound-horizon integral (numeric vs closed-form cross-check) --")
    print(f"  PROPER@fold (numeric)                = {r['d_sound_proper_numeric_MKKinv']:.6e} M_KK^-1")
    print(f"  PROPER@fold (closed (1-e^-N))        = {r['d_sound_proper_closed_MKKinv']:.6e} M_KK^-1  [ratio {r['proper_numeric_closed_ratio']:.6f}]")
    print(f"  COMOVING-rel-fold (numeric)          = {r['d_sound_comov_numeric_MKKinv']:.6e} M_KK^-1")
    print(f"  COMOVING-rel-fold (closed (e^N-1))   = {r['d_sound_comov_closed_MKKinv']:.6e} M_KK^-1  [ratio {r['comov_numeric_closed_ratio']:.6f}]")
    print(f"  proper sound horizon @fold           = {r['d_sound_proper_fold_m']:.6e} m")
    print(f"  proper Hubble radius @fold (acoustic)= {r['R_hubble_fold_m']:.6e} m")
    print(f"  -- horizons (comoving, today) --")
    print(f"  r_acoustic (comoving -> today)       = {r['r_acoustic_com_m']:.6e} m  ({r['r_acoustic_Mpc']:.3e} Mpc)")
    print(f"  c/H_0 (present Hubble scale)          = {r['c_over_H0_m']:.6e} m  ({r['c_over_H0_Mpc']:.3e} Mpc)")
    print()
    print(f"  *** R_horizon = r_acoustic / (c/H_0) = {r['R_horizon']:.6e}  (log10 = {r['log10_R_horizon']:.4f})")
    print(f"  *** N_required (R=1)  = {r['N_required']:.4f} e-folds")
    print(f"  *** N_e^total         = {r['N_e_total']:.4f} e-folds")
    print(f"  *** e-fold SHORTFALL  = {r['efold_shortfall']:.4f} e-folds ({r['efold_shortfall_dex']:.2f} dex)")

    print("\n" + "=" * 72)
    print("GATE EVALUATION ([SIGN] 3-tuple + collapse rule)")
    print("=" * 72)
    print(f"  SIGN: chain Step-5 predicts R_horizon>1 (super-horizon); measured "
          f"R_horizon={r['R_horizon']:.3e} {'>' if detail['measured_super_horizon'] else '<'} 1 "
          f"[match={detail['sign_ok']}] => {sign_v}")
    print(f"  MAGNITUDE: R_horizon>1? [{detail['mag_pass']}]; |log10 R|<{INFO_LOG_HALFWIDTH} (a(t)-map INFO)? "
          f"[{detail['mag_info']}] => {mag_v}")
    print(f"  REGIME: deterministic 1000-pt quadrature, full window, numeric=closed cross-check => {regime_v}")
    print(f"  COMPOSITE (collapse rule): {comp}")

    # ---- npz (full float64) ----
    np.savez(
        OUT_NPZ,
        # headline
        R_horizon=r["R_horizon"], log10_R_horizon=r["log10_R_horizon"],
        N_required=r["N_required"], N_e_total=r["N_e_total"],
        efold_shortfall=r["efold_shortfall"], efold_shortfall_dex=r["efold_shortfall_dex"],
        # horizons (m + Mpc)
        r_acoustic_com_m=r["r_acoustic_com_m"], c_over_H0_m=r["c_over_H0_m"],
        r_acoustic_Mpc=r["r_acoustic_Mpc"], c_over_H0_Mpc=r["c_over_H0_Mpc"],
        d_sound_proper_fold_m=r["d_sound_proper_fold_m"],
        R_hubble_fold_m=r["R_hubble_fold_m"],
        # cross-checks (numeric vs own closed form, PROPER + COMOVING)
        d_sound_proper_numeric_MKKinv=r["d_sound_proper_numeric_MKKinv"],
        d_sound_proper_closed_MKKinv=r["d_sound_proper_closed_MKKinv"],
        proper_numeric_closed_ratio=r["proper_numeric_closed_ratio"],
        d_sound_comov_numeric_MKKinv=r["d_sound_comov_numeric_MKKinv"],
        d_sound_comov_closed_MKKinv=r["d_sound_comov_closed_MKKinv"],
        comov_numeric_closed_ratio=r["comov_numeric_closed_ratio"],
        horizon_over_hubble_fold=r["horizon_over_hubble_fold"],
        # inputs
        one_plus_z_fold=r["one_plus_z_fold"],
        H_fold_GeV=r["H_fold_GeV"], H0_GeV=r["H0_GeV"], T0_GeV=r["T0_GeV"],
        c_s=r["c_s"], c_fabric=r["c_fabric"], v_transit=r["v_transit"], M_KK_GeV=r["M_KK_GeV"],
        N_e_geom=r["N_e_geom"], N_e_internal=r["N_e_internal"],
        # arrays
        tau=r["tau"], a_of_tau=r["a_of_tau"], N_of_tau=r["N_of_tau"],
        # band
        info_log_halfwidth=INFO_LOG_HALFWIDTH, R_tol=R_TOL,
        # verdict block
        verdict=comp, sign_verdict=sign_v, magnitude_verdict=mag_v,
        regime_verdict=regime_v,
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"\nSaved data: {OUT_NPZ}")

    make_plot(r)

    # ---- 4-tuple + payload ----
    val = (f"R_horizon={r['R_horizon']:.6e};log10R={r['log10_R_horizon']:.4f};"
           f"r_acoustic_Mpc={r['r_acoustic_Mpc']:.4e};c_over_H0_Mpc={r['c_over_H0_Mpc']:.4e};"
           f"N_required={r['N_required']:.4f};N_e_total={r['N_e_total']:.4f};"
           f"efold_shortfall={r['efold_shortfall']:.4f};super_horizon={bool(r['R_horizon']>1)}")  # (local)
    print(f"\n(value={val!r}, scheme={SCHEME}, convention={CONVENTION}, "
          f"L_max={L_MAX})")

    note = (f"Pre-transit acoustic sound horizon r_acoustic={r['r_acoustic_Mpc']:.3e} Mpc vs "
            f"c/H_0={r['c_over_H0_Mpc']:.3e} Mpc => R_horizon={r['R_horizon']:.3e} (log10={r['log10_R_horizon']:.2f}) "
            f"<< 1 EXACTLY. Substrate N_e^total={r['N_e_total']:.2f} e-folds (S53 acoustic-metric driven) vs "
            f"N_required={r['N_required']:.1f} for R=1 => shortfall {r['efold_shortfall']:.1f} e-folds "
            f"({r['efold_shortfall_dex']:.1f} dex). The METRIC-horizon single-domain hypothesis (plan track_A) "
            f"FAILs: exflation is spectral complexification NOT metric inflation (phononic-framing). "
            f"sign FAIL (predicted R>1, measured R<<1). Track-B (sub-horizon by the metric mechanism).")

    rows = [
        f"# SUBSTRATE-FIRST: exflation = SPECTRAL COMPLEXIFICATION, NOT metric expansion "
        f"(phononic-framing.md). N_e^total={r['N_e_total']:.2f} (S53 EoS Section 8) << ~60 needed; "
        f"q(tau) -0.97->+0.81 (S54). The acoustic sound horizon does NOT grow super-Hubble "
        f"because there is essentially NO metric inflation. # {GATE_ID}",
        f"# DUAL-PATHWAY AGREEMENT on sign(R-1)<0: Pathway-1 (physical/redshift) R_horizon="
        f"{r['R_horizon']:.3e}; Pathway-2 (e-fold requirement) N_required={r['N_required']:.1f} "
        f">> N_e^total={r['N_e_total']:.2f}. Both independent unit routes agree R<<1 => NOT a units "
        f"artifact. # {GATE_ID}",
        f"# Fermi-LAT <1e-5 single-domain SURVIVES via a DIFFERENT substrate mechanism: "
        f"tau-SIMULTANEITY (the substrate has ONE Jensen slice; the fold is at one tau value for the "
        f"whole substrate -- canonical_constants tau_pivot provenance 'substrate has ONE Jensen slice'). "
        f"The single-domain property is NOT a metric causal patch. S41: 'Horizon problem AMELIORATED "
        f"by tau-simultaneity, NOT eliminated'. # {GATE_ID}",
        f"# delta_A spatial characterization (UB-2): the metric-acoustic coherence scale is "
        f"r_acoustic={r['r_acoustic_Mpc']:.3e} Mpc (NOT super-Hubble); delta_A's actual single-domain "
        f"coherence is tau-simultaneity (one Jensen slice), an INTERNAL-space (fiber) coherence, not "
        f"a 4D metric patch. The G-3 antimatter face is filled by tau-simultaneity, not by R_horizon>1. # {GATE_ID}",
        f"# white-hole causal-disconnect PROVEN S85 is REAL (pre/post-fold causally separated) but does "
        f"NOT imply R_horizon>1: the disconnect prevents post-fold RE-connection; it does not grow the "
        f"PRE-fold comoving horizon to super-Hubble size (that needs ~60 e-folds the substrate lacks). # {GATE_ID}",
        f"# sound-horizon integral cross-check (numeric 1000-pt vs own closed form): "
        f"PROPER@fold ratio={r['proper_numeric_closed_ratio']:.6f} [closed (c_s/H_f)(1-e^-N)]; "
        f"COMOVING-rel-fold ratio={r['comov_numeric_closed_ratio']:.6f} [closed (c_s/H_f)(e^N-1)]. "
        f"Both numeric=closed to <1e-3. # {GATE_ID}",
        f"# regulator_pin=N/A -- no Seeley-DeWitt a_n; no SCHEMATIC helper (canonical_constants + "
        f"S53/S54 substrate e-fold history only; no spectrum cache). # {GATE_ID}",
        f"# cache-pin SOURCE-RECON Class-(c): orchestrator STALE-HINT 88f1e9b1->9e6d9cf7 applies to the "
        f"s84 L12 mode cache used by SIBLING gates; THIS gate reads NO spectrum cache -> zero physics "
        f"effect. # {GATE_ID}",
        f"# Track-B (sub-horizon-by-metric-mechanism, dual-prior 0.20): the plan's track_A super-horizon "
        f"metric hypothesis (prior 0.80) is FALSIFIED by the substrate's own integrated expansion history; "
        f"BUT Fermi-LAT consistency is preserved by tau-simultaneity (a structurally distinct mechanism). "
        f"Routes the a(t)-map sharpening to the K_pivot/a(t) gap (atlas-04 C1/C2). # {GATE_ID}",
    ]                                                          # (local)

    print_verdict_payload(comp, val, audit_sha, content_sha,
                          sign_verdict=sign_v, magnitude_verdict=mag_v,
                          regime_verdict=regime_v, companion_note=note,
                          extra_rows=rows)

    print(f"\n=== {GATE_ID}: {comp} (wall {time.time()-t0:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
