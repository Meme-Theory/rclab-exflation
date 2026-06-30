#!/usr/bin/env python3
"""
INV6 W3-3 -- ETA-B-ACOUSTIC-SCHWINGER
=====================================

Gate: INV6-W3-3-ETA-B-ACOUSTIC-SCHWINGER ([SIGN])
Track: investigation (investigation-6)
Classification: PHONONIC

Pre-registered threshold (plan §W3-3):
  span operator -- eta_B_schwinger = CP_bias * (n_Schwinger / s),
                   n_Schwinger ~ exp(-pi*m_eff^2/(e*E_acoustic))
  PASS iff 3e-10 <= eta_B_schwinger <= 1.2e-9 (in-band; band center eta_BBN_obs=6.12e-10)
  FAIL iff eta_B_schwinger < 3e-10 (under) OR > 1.2e-9 (over-production)
  INFO iff the in-band value requires E_acoustic outside the Mach-13.75-implied range.

HYPOTHESIS (plan): recomputing eta_B as a CP-biased acoustic-Schwinger pair-production
rate in the supersonic transit's strong field gradient yields a field-strength-sensitive
eta_B; because exp(-pi m^2/eE) is exquisitely sensitive to E, the 1.1-OOM shortfall could
be a Mach-number (field-strength) effect that lands eta_B in [3e-10, 1.2e-9].

GOVERNING STRUCTURE (substrate-first; acoustic-Schwinger, NOT imported sphaleron physics)
----------------------------------------------------------------------------------------
The substrate IS the supersonic transit through the van Hove fold -- an acoustic white hole
at Mach 13.75 (v_transit = Mach*c_BLV = 6.66875 M_KK > c_s = c_BLV = 0.485 M_KK). Pair
creation at the fold is a Schwinger process in the strong, time-dependent ACOUSTIC
background. The substrate-native Schwinger exponent (S43 SCHWINGER-36 resolution; Volovik
3He-A PG-horizon pair creation, Papers 07/29) is:

    n_Schwinger ~ exp(-S),   S = pi * m_eff^2 / (e * E_acoustic)

with the substrate identifications (S43, machine-anchored):
  - m_eff   = quasiparticle gap = pair-creation threshold = Delta_0_GL = 0.770435... M_KK
              (S43 used Delta_0 = 0.770; the GL gap is the energy gap for QP creation).
  - e*E_eff = the acoustic white hole's SURFACE GRAVITY at the canonical fold = the modulus
              sweep rate |dtau/dt| = v_terminal = 26.5450 M_KK^2 (S43 TAU-DYN-36). S43 PROVED
              S_Schwinger = pi*Delta_0^2/|v_terminal| = 0.0702 (NOT the wrong PG-horizon
              formula that gave factor-36; the substrate-correct form has NO c_s denominator
              -- the system is effectively 0D, L/xi_GL = 0.031).

The plan's acoustic field strength E_acoustic = |d_tau v|/c_s scales LINEARLY with the
transit gradient, hence with v_transit ~ Mach. We anchor e*E_acoustic at the canonical
Mach=13.75 to the substrate field strength v_terminal, and scan Mach in [1, 13.75]:

    e*E_acoustic(Mach) = v_terminal * (Mach / Mach_max).

The CP-bias and entropy normalization are taken from the SAME S98 baryogenesis chain that
fixed eta_B_base = 4.517492e-11 (S98-W3-2-BARYOGEN-UNIQUENESS PASS, audit 3be22b8a):

    eta_B = eta_dkkms * sigma_supp * sin(phi_CP),
    sigma_supp = eps_nLI^2 * geom * fbar,  eps_nLI = eps_K7^2/n_pairs, geom=1/8, fbar=0.4892.

The Schwinger recompute replaces the PRODUCTION count by the Schwinger density; in ratio
form (relative to the canonical fold, holding the CP/entropy normalization fixed) this is:

    eta_B_schwinger(Mach) = eta_B_base * [ exp(-S(Mach)) / exp(-S(Mach_max)) ].

The bracket is the Schwinger production ENHANCEMENT relative to the canonical fold.

SUBSTITUTION CHAIN (SIGN; plan §W3-3 item 7) -- direction read-off
-----------------------------------------------------------------
  Step 1: n_Schwinger ~ exp(-pi m_eff^2/(e E_acoustic))            [Schwinger 1951; S43 substrate analog]
  Step 2: e E_acoustic = |d_tau v|/c_s -> linear in v_transit -> linear in Mach
  Step 3: d n / d E_acoustic ~ exp(-S)*(pi m^2/(eE)^2) > 0          => n MONOTONE INCREASING in E
  Step 4: d n / d Mach = (d n/d E)(d E/d Mach) > 0                  => n MONOTONE INCREASING in Mach
          exponent S = pi m^2/(eE) -> 0+ as E grows -> exp(-S) -> 1 (production UNSUPPRESSED ceiling)
  Step 5: eta_B_schwinger = CP_bias * n/s, CP_bias>0 (sin(phi_CP=pi/2)=1) -> eta_B MONOTONE
          INCREASING in Mach; at Mach 13.75 the field is near-maximal -> eta_B near its
          production CEILING. SIGN: eta_B > 0 (baryon excess) preserved by CP_bias sign.
  Conclusion: "supersonic transit maximizes eta_B" is established (sign). Whether the
              MAGNITUDE reaches the band is the gate's measured output.

THE DECISIVE ALGEBRA (follow it where it leads): exp(-S) <= 1 ALWAYS. At the canonical fold
the substrate ALREADY sits at exp(-S_canon) = exp(-0.0702) = 0.9322 -- 93% of the way to the
production ceiling. The MAXIMUM Schwinger boost (E->inf) is 1/exp(-S_canon) = 1.0728x. The
band-low requires a 6.64x boost; the band-low required exp(-S) = 6.19 > 1 is IMPOSSIBLE. So
the in-band value is UNREACHABLE at ANY Mach -- the shortfall is NOT a field-strength effect.
The substrate is in the strong-field (near-unsuppressed) regime where exp() sensitivity gives
no headroom; the 1.1-OOM shortfall lives in the CP-bias x fiber-volume suppression sigma_supp,
the SAME locus as the W3-1 GGE-rescattering null.

DISCIPLINE
----------
- `from canonical_constants import *` (Delta_0_GL, v_terminal, c_BLV, Mach_max, eta_BBN_obs,
  eta_BBN_err, epsilon_K7, n_pairs, phi_CP_K7_transit). Every intermediate tagged `# (local)`.
- numpy on a 200-pt 1D scan (cpu-cap-OMP8; far below the 100x100 GPU threshold).
- S84+ dual-SHA (audit = sha256(script||canonical||pinmap); content = sha256(script)).
- Verdict via emit_verdict MCP tool (race-safe); script PRINTS payload only.
- SOURCE-RECON Class-(c): the orchestrator STALE CACHE-SHA HINT (88f1e9b1->9e6d9cf7) targets
  the s84 L12 MODE cache used by SIBLING gates; THIS gate reads ONLY canonical_constants +
  s98_w3_2_baryogen_uniqueness.npz (plan <computed-at-runtime>; on-disk SHA runtime-pinned;
  s84 cache NOT read here) -> zero physics effect; documented in the verdict extra rows.
"""

from __future__ import annotations

import hashlib
import json
import os
import sys
import time
from pathlib import Path

os.environ.setdefault("OMP_NUM_THREADS", "8")  # CPU-cap (200-pt 1D scan; below GPU threshold)

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
# consumed: Delta_0_GL, Delta_0_OES, v_terminal, c_BLV, Mach_max, eta_BBN_obs,
#           eta_BBN_err, epsilon_K7, n_pairs, phi_CP_K7_transit

# --------------------------------------------------------------------------
# Section 2 -- Identity + machinery pins
# --------------------------------------------------------------------------
SESSION = 6                                                       # (local)
GATE_ID = "INV6-W3-3-ETA-B-ACOUSTIC-SCHWINGER"                    # (local)
SCHEME = "ACOUSTIC-SCHWINGER-dS-BACKREACTION"                     # (local)
CONVENTION = "ABSOLUTE"                                           # (local)
L_MAX = "N/A"                                                     # (local)

OUT_NPZ = INV_DIR / "inv6_w3_3_eta_b_acoustic_schwinger.npz"      # (local)
OUT_PNG = INV_DIR / "inv6_w3_3_eta_b_acoustic_schwinger.png"      # (local)

S98_NPZ = COMPUTATIONS_DIR / "session-98" / "s98_w3_2_baryogen_uniqueness.npz"  # (local)

# PASS band (plan strict_PASS_boundary)
BAND_LO = 3.0e-10                                                 # (local)
BAND_HI = 1.2e-9                                                  # (local)
ETA_TOL = 1e-12                                                   # (local) float compare
N_EVAL = 200                                                      # (local) E_acoustic scan resolution
MACH_LO = 1.0                                                     # (local) sonic point
MACH_HI = float(Mach_max)                                         # (local) 13.75 supersonic transit

MACHINERY_PINS = {                                                # (local)
    "N_eval": "200",                # E_acoustic scan resolution across Mach in [1,13.75]
    "L_max": "N/A",                 # field-theory rate in the acoustic background; no D_K irrep
    "scan_range": "E_acoustic = v_terminal*(Mach/Mach_max), Mach in [1,13.75]",
    "step_size": "uniform-200pt-linspace",
    "tolerance": "1e-12",
    "scheme": SCHEME,
    "convention": CONVENTION,
    "random_seed": "N/A-deterministic",
    "GPU_path": "numpy-cpu-cap-OMP8 (200-pt 1D scan; below 100x100 GPU threshold)",
    "publication_precision": "6",
    "m_eff_pin": "Delta_0_GL=0.7704350982797368 (QP gap = pair-creation threshold; S43)",
    "eE_anchor_pin": "v_terminal=26.54496622300285 (S43 surface-gravity at canonical fold; eE(Mach_max))",
    "cp_entropy_norm_pin": "S98 eta_dkkms*sigma_supp*sin(phi_CP); eta_B_base=4.517492e-11 (S98-W3-2 PASS 3be22b8a)",
    "s84_sibling_pin_drift": "Class-(c) PIN-DRIFT 88f1e9b1(inv-6-plan-stale)->9e6d9cf7(S100-canonical); "
                             "s84 cache NOT read by THIS gate (W3-3 reads s98 + canonical only)",
}


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
    """Print the emit_verdict PAYLOAD for the dispatching agent (race-safe MCP path)."""
    payload: dict = {
        "session": SESSION,
        "gate_id": GATE_ID,
        "verdict": verdict,
        "value": str(value),
        "scheme": SCHEME,
        "convention": CONVENTION,
        "l_max": str(L_MAX),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "schema_version": "S84+",
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


# --------------------------------------------------------------------------
# Section 3 -- Load S98 baryogenesis chain (CP/entropy normalization)
# --------------------------------------------------------------------------
def load_s98() -> dict:
    """Pull the S98 entropy/CP normalization that fixed eta_B_base. The acoustic-Schwinger
    recompute holds these FIXED and varies only the production count (Schwinger density)."""
    d = np.load(S98_NPZ, allow_pickle=True)                       # (local)
    out = {                                                       # (local)
        "eta_B_base": float(d["eta_B"]),          # 4.517492e-11 (S98-W3-2 PASS)
        "eta_dkkms": float(d["eta_dkkms"]),       # 69832.54 DKKMS entropy baseline
        "geom": float(d["geom"]),                 # 1/8 fiber ratio
        "fbar": float(d["fbar"]),                 # 0.4892 tau-support fraction
        "eps_nLI": float(d["eps_nLI"]),           # eps_K7^2/n_pairs
        "phi_CP": float(d["phi_CP"]),             # pi/2
        "sigma_supp": float(d["sigma_supp"]),     # eps_nLI^2*geom*fbar
        "eta_obs": float(d["eta_obs"]),           # 6.12e-10
    }
    return out


# --------------------------------------------------------------------------
# Section 4 -- Compute (acoustic-Schwinger eta_B + Mach scan)
# --------------------------------------------------------------------------
def schwinger_exponent(m_eff: float, eE: float) -> float:
    """Substrate Schwinger action S = pi*m_eff^2/(e*E)  (S43; 3He-A PG-horizon analog)."""
    return float(np.pi * m_eff ** 2 / eE)                         # (local)


def compute() -> dict:
    PI = np.pi                                                    # (local)
    a = load_s98()                                                # (local)
    eta_base = a["eta_B_base"]                                    # (local)
    eta_obs = a["eta_obs"]                                        # (local)

    # --- substrate Schwinger inputs (S43 machine-anchored) ---
    m_eff = float(Delta_0_GL)         # (local) QP gap = pair-creation threshold = 0.770435
    m_eff_OES = float(Delta_0_OES)    # (local) alternative (OES) gap = 0.464255 (robustness x-check)
    eE_canon = float(v_terminal)      # (local) e*E at canonical fold = surface gravity = 26.5450
    c_s = float(c_BLV)                # (local) sound speed 0.485
    Mach_c = float(Mach_max)          # (local) 13.75
    v_transit = Mach_c * c_s          # (local) 6.66875 M_KK

    # --- canonical-fold Schwinger suppression ---
    S_canon = schwinger_exponent(m_eff, eE_canon)                 # (local) 0.0702 (GL)
    exp_canon = float(np.exp(-S_canon))                           # (local) 0.9322 (production at fold)
    S_canon_OES = schwinger_exponent(m_eff_OES, eE_canon)         # (local)
    exp_canon_OES = float(np.exp(-S_canon_OES))                   # (local)

    # --- reconstruct eta_B_base from the S98 CP/entropy chain (bit-for-bit cross-check) ---
    sigma_supp_check = a["eps_nLI"] ** 2 * a["geom"] * a["fbar"]  # (local)
    eta_base_recon = float(a["eta_dkkms"] * sigma_supp_check * np.sin(a["phi_CP"]))  # (local)
    recon_match = bool(abs(eta_base_recon - eta_base) < 1e-18)    # (local)

    # --- Mach scan: eE(Mach) = eE_canon*(Mach/Mach_max); eta_B(Mach) = base*[exp(-S(Mach))/exp(-S_canon)] ---
    Mach_grid = np.linspace(MACH_LO, MACH_HI, N_EVAL)            # (local)
    eE_grid = eE_canon * (Mach_grid / Mach_c)                     # (local) e*E_acoustic(Mach)
    S_grid = PI * m_eff ** 2 / eE_grid                            # (local) Schwinger action
    n_grid = np.exp(-S_grid)                                      # (local) production density (rel)
    boost_grid = n_grid / exp_canon                              # (local) production boost vs canonical fold
    eta_grid = eta_base * boost_grid                              # (local) eta_B(Mach)

    # eta_B at the canonical Mach=13.75 transit
    eta_canonical = eta_base * (np.exp(-schwinger_exponent(m_eff, eE_canon)) / exp_canon)  # (local) == eta_base
    eta_canonical = float(eta_canonical)

    # --- Schwinger production CEILING (E->inf, exp(-S)->1): the max eta_B the channel can give ---
    boost_ceiling = 1.0 / exp_canon                              # (local) 1.0728 (GL)
    eta_ceiling = float(eta_base * boost_ceiling)                # (local) 4.846e-11 -- the absolute max
    boost_ceiling_OES = 1.0 / exp_canon_OES                      # (local)
    eta_ceiling_OES = float(eta_base * boost_ceiling_OES)        # (local)

    # --- required boost for the PASS band ---
    R_required = eta_obs / eta_base                              # (local) 13.55 (vs band center)
    boost_band_lo = BAND_LO / eta_base                           # (local) 6.64
    boost_band_hi = BAND_HI / eta_base                           # (local) 26.56
    # required exp(-S) to hit band-low (relative to fixed CP/entropy norm): boost_band_lo*exp_canon
    req_expS_band_lo = boost_band_lo * exp_canon                 # (local) 6.19 -> IMPOSSIBLE (>1)
    band_reachable = bool(req_expS_band_lo <= 1.0)              # (local) False: exp(-S)<=1 always

    # --- direction (SIGN) check: monotone increasing in Mach ---
    dn = np.diff(n_grid)                                         # (local)
    monotone_up = bool(np.all(dn > 0))                          # (local) True
    sign_eta_pos = bool(np.sin(a["phi_CP"]) > 0)               # (local) True (baryon excess)

    # --- gate magnitude reading at the canonical Mach (and at ceiling) ---
    in_band_canonical = bool((BAND_LO - ETA_TOL) <= eta_canonical <= (BAND_HI + ETA_TOL))  # (local)
    in_band_ceiling = bool((BAND_LO - ETA_TOL) <= eta_ceiling <= (BAND_HI + ETA_TOL))      # (local)
    underproduction = bool(eta_ceiling < BAND_LO)               # (local) True: even ceiling < band-low
    overproduction = bool(eta_canonical > BAND_HI)              # (local) False
    underprod_oom_ceiling = float(np.log10(eta_obs / eta_ceiling))  # (local) 1.10 OOM short at ceiling
    underprod_oom_canonical = float(np.log10(eta_obs / eta_canonical))  # (local) 1.13 OOM at fold

    return {
        # headline
        "eta_canonical": eta_canonical,         # eta_B at Mach=13.75 (== base; the substrate sits at the fold)
        "eta_ceiling": eta_ceiling,             # max eta_B the Schwinger channel can give (E->inf)
        "eta_base": eta_base,
        "eta_obs": eta_obs,
        "in_band_canonical": in_band_canonical,
        "in_band_ceiling": in_band_ceiling,
        "band_reachable": band_reachable,       # is in-band reachable at ANY Mach? (False)
        "underproduction": underproduction,
        "overproduction": overproduction,
        "underprod_oom_ceiling": underprod_oom_ceiling,
        "underprod_oom_canonical": underprod_oom_canonical,
        # Schwinger structure
        "m_eff_GL": m_eff, "m_eff_OES": m_eff_OES,
        "eE_canon": eE_canon, "c_s": c_s, "Mach_c": Mach_c, "v_transit": v_transit,
        "S_canon": S_canon, "exp_canon": exp_canon,
        "S_canon_OES": S_canon_OES, "exp_canon_OES": exp_canon_OES,
        "boost_ceiling": boost_ceiling, "boost_ceiling_OES": boost_ceiling_OES,
        "eta_ceiling_OES": eta_ceiling_OES,
        # band requirements
        "R_required": float(R_required),
        "boost_band_lo": float(boost_band_lo), "boost_band_hi": float(boost_band_hi),
        "req_expS_band_lo": float(req_expS_band_lo),
        # direction
        "monotone_up": monotone_up, "sign_eta_pos": sign_eta_pos,
        # scan arrays
        "Mach_grid": Mach_grid, "eE_grid": eE_grid, "S_grid": S_grid,
        "n_grid": n_grid, "boost_grid": boost_grid, "eta_grid": eta_grid,
        # cross-checks
        "eta_base_recon": eta_base_recon, "recon_match": recon_match,
        "sigma_supp": a["sigma_supp"], "eta_dkkms": a["eta_dkkms"],
        "geom": a["geom"], "fbar": a["fbar"], "eps_nLI": a["eps_nLI"], "phi_CP": a["phi_CP"],
        "BAND_LO": BAND_LO, "BAND_HI": BAND_HI,
    }


# --------------------------------------------------------------------------
# Section 5 -- Gate evaluation ([SIGN] 3-tuple + collapse rule)
# --------------------------------------------------------------------------
def evaluate_gate(r: dict):
    # SIGN: chain Step 3-5 predicts eta_B MONOTONE INCREASING in Mach (production rises toward
    # the ceiling) AND eta_B > 0 (baryon excess). sign PASS iff both hold.
    sign_ok = bool(r["monotone_up"] and r["sign_eta_pos"])       # (local)
    sign_v = "PASS" if sign_ok else "FAIL"                       # (local)

    # MAGNITUDE: gate value = eta_B at the canonical Mach=13.75. The decisive structural reading
    # uses the production CEILING (E->inf): if even the ceiling stays below the band, the
    # field-strength corridor is closed regardless of Mach.
    eta_val = r["eta_ceiling"]   # (local) most generous: max the Schwinger channel can supply
    if (r["BAND_LO"] - ETA_TOL) <= eta_val <= (r["BAND_HI"] + ETA_TOL):
        mag_v = "PASS"                                           # (local)
    elif abs(eta_val - r["eta_obs"]) <= abs(r["eta_obs"] - r["BAND_LO"]):
        # within ~factor-2 of obs but outside band -> INFO
        mag_v = "INFO"                                           # (local)
    else:
        mag_v = "FAIL"                                           # (local)

    # REGIME: full deterministic 200-pt scan, no auto-shortening; the Schwinger rate is well
    # defined throughout (exp(-S) in (0,1], no breakdown) -> VALID.
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

    detail = (f"sign={sign_v}(monotone_up={r['monotone_up']},eta>0={r['sign_eta_pos']}); "
              f"mag={mag_v}(eta_ceiling={eta_val:.6e} vs band[{r['BAND_LO']:.1e},{r['BAND_HI']:.1e}]); "
              f"regime={regime_v}")                              # (local)
    return comp, sign_v, mag_v, regime_v, detail


# --------------------------------------------------------------------------
# Section 6 -- Plot
# --------------------------------------------------------------------------
def make_plot(r: dict):
    fig, ax = plt.subplots(2, 2, figsize=(13, 9))               # (local)

    # Panel 1: Schwinger suppression exp(-S) vs Mach
    ax0 = ax[0, 0]
    ax0.plot(r["Mach_grid"], r["n_grid"], "b-", lw=2, label=r"$e^{-S}=e^{-\pi m^2/eE}$")
    ax0.axhline(1.0, color="k", ls=":", lw=1, label="ceiling $e^{-S}\\to1$")
    ax0.axvline(r["Mach_c"], color="r", ls="--", lw=1.2, label=f"Mach={r['Mach_c']:.2f} (transit)")
    ax0.scatter([r["Mach_c"]], [r["exp_canon"]], c="r", zorder=5,
                label=f"$e^{{-S_{{canon}}}}$={r['exp_canon']:.4f}")
    ax0.set_xlabel("Mach number"); ax0.set_ylabel(r"production $e^{-S}$")
    ax0.set_title("Schwinger production vs Mach (substrate at strong-field ceiling)")
    ax0.legend(fontsize=8); ax0.grid(alpha=0.3)

    # Panel 2: eta_B(Mach) vs the PASS band
    ax1 = ax[0, 1]
    ax1.plot(r["Mach_grid"], r["eta_grid"], "b-", lw=2, label=r"$\eta_B(\mathrm{Mach})$")
    ax1.axhspan(r["BAND_LO"], r["BAND_HI"], color="g", alpha=0.18, label="PASS band [3e-10,1.2e-9]")
    ax1.axhline(r["eta_obs"], color="g", ls="-", lw=1.2, label=f"$\\eta_{{obs}}$={r['eta_obs']:.2e}")
    ax1.axhline(r["eta_ceiling"], color="m", ls="--", lw=1.4,
                label=f"Schwinger ceiling={r['eta_ceiling']:.3e}")
    ax1.axhline(r["eta_base"], color="b", ls=":", lw=1, label=f"base={r['eta_base']:.3e}")
    ax1.set_xlabel("Mach number"); ax1.set_ylabel(r"$\eta_B$")
    ax1.set_yscale("log"); ax1.set_title("eta_B(Mach): even the E->inf ceiling stays below band")
    ax1.legend(fontsize=8); ax1.grid(alpha=0.3)

    # Panel 3: required boost vs achievable boost
    ax2 = ax[1, 0]
    bars = ["ceiling\n(E->inf)", "band-low\nneeded", "band-hi\nneeded", "R_required\n(vs obs)"]
    vals = [r["boost_ceiling"], r["boost_band_lo"], r["boost_band_hi"], r["R_required"]]
    cols = ["m", "orange", "red", "darkred"]
    ax2.bar(bars, vals, color=cols, alpha=0.75)
    ax2.axhline(r["boost_ceiling"], color="m", ls="--", lw=1.2)
    ax2.set_ylabel("boost factor (x base)"); ax2.set_yscale("log")
    ax2.set_title(f"Schwinger ceiling {r['boost_ceiling']:.3f}x << band-low {r['boost_band_lo']:.2f}x needed")
    for i, v in enumerate(vals):
        ax2.text(i, v * 1.05, f"{v:.2f}", ha="center", fontsize=8)
    ax2.grid(alpha=0.3, axis="y")

    # Panel 4: Schwinger action S vs Mach (shows S->0, no exponential headroom at high Mach)
    ax3 = ax[1, 1]
    ax3.plot(r["Mach_grid"], r["S_grid"], "b-", lw=2, label=r"$S=\pi m^2/eE$ (GL gap)")
    ax3.axvline(r["Mach_c"], color="r", ls="--", lw=1.2)
    ax3.scatter([r["Mach_c"]], [r["S_canon"]], c="r", zorder=5,
                label=f"$S_{{canon}}$={r['S_canon']:.4f}")
    ax3.set_xlabel("Mach number"); ax3.set_ylabel(r"Schwinger action $S$")
    ax3.set_title("S->0 at high Mach: no exponential headroom (already unsuppressed)")
    ax3.legend(fontsize=8); ax3.grid(alpha=0.3)

    fig.suptitle(f"INV6-W3-3 ETA-B-ACOUSTIC-SCHWINGER -- field-strength corridor: "
                 f"ceiling eta_max={r['eta_ceiling']:.3e} < band-low 3e-10 (FAIL, "
                 f"{r['underprod_oom_ceiling']:.2f} OOM short)", fontsize=11)
    fig.tight_layout(rect=[0, 0, 1, 0.97])
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)


# --------------------------------------------------------------------------
# Section 7 -- Main
# --------------------------------------------------------------------------
def main() -> int:
    # input pins
    input_files = [SHARED_DIR / "canonical_constants.py", S98_NPZ]  # (local)
    print(f"=== {GATE_ID} -- input SHA-256 pins ===")
    pins = {}                                                     # (local)
    for p in input_files:
        sha = sha256_of(p)                                       # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    for k, v in MACHINERY_PINS.items():
        pins[f"pin::{k}"] = v

    script_path = Path(__file__).resolve()                        # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"        # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    r = compute()                                                # (local)

    # report
    print(f"[{GATE_ID}] === acoustic-Schwinger eta_B (substrate-first) ===")
    print(f"  m_eff (GL gap)        = {r['m_eff_GL']:.10f} M_KK  (pair-creation threshold)")
    print(f"  eE_canon (v_terminal) = {r['eE_canon']:.6f} M_KK^2  (acoustic surface gravity at fold)")
    print(f"  c_s=c_BLV={r['c_s']}, Mach={r['Mach_c']}, v_transit={r['v_transit']:.5f} M_KK")
    print(f"  S_canon = pi*m^2/eE   = {r['S_canon']:.6f}  -> exp(-S)={r['exp_canon']:.6f} (production at fold)")
    print(f"  eta_base recon match (S98 chain bit-for-bit): {r['recon_match']} "
          f"(recon={r['eta_base_recon']:.6e}, base={r['eta_base']:.6e})")
    print(f"  eta_B(Mach=13.75)     = {r['eta_canonical']:.6e}")
    print(f"  eta_B CEILING (E->inf)= {r['eta_ceiling']:.6e}  (boost {r['boost_ceiling']:.6f}x; max possible)")
    print(f"  eta_obs (BBN)         = {r['eta_obs']:.6e}")
    print(f"  band [{r['BAND_LO']:.1e},{r['BAND_HI']:.1e}]; boost needed band-low={r['boost_band_lo']:.4f}x, "
          f"R_required={r['R_required']:.4f}x")
    print(f"  required exp(-S) for band-low = {r['req_expS_band_lo']:.4f}  "
          f"(>1 IMPOSSIBLE; band_reachable={r['band_reachable']})")
    print(f"  underproduction (ceiling<band-low)={r['underproduction']}; "
          f"underprod OOM at ceiling={r['underprod_oom_ceiling']:.4f}")
    print(f"  direction: monotone_up={r['monotone_up']}, eta>0={r['sign_eta_pos']}")
    print(f"  OES x-check: ceiling={r['eta_ceiling_OES']:.4e} (boost {r['boost_ceiling_OES']:.4f}x) still < band-low")

    # save npz (full float64)
    np.savez(
        OUT_NPZ,
        gate_id=GATE_ID, scheme=SCHEME, convention=CONVENTION,
        eta_canonical=r["eta_canonical"], eta_ceiling=r["eta_ceiling"],
        eta_base=r["eta_base"], eta_obs=r["eta_obs"],
        in_band_canonical=r["in_band_canonical"], in_band_ceiling=r["in_band_ceiling"],
        band_reachable=r["band_reachable"], underproduction=r["underproduction"],
        overproduction=r["overproduction"],
        underprod_oom_ceiling=r["underprod_oom_ceiling"],
        underprod_oom_canonical=r["underprod_oom_canonical"],
        m_eff_GL=r["m_eff_GL"], m_eff_OES=r["m_eff_OES"],
        eE_canon=r["eE_canon"], c_s=r["c_s"], Mach_c=r["Mach_c"], v_transit=r["v_transit"],
        S_canon=r["S_canon"], exp_canon=r["exp_canon"],
        S_canon_OES=r["S_canon_OES"], exp_canon_OES=r["exp_canon_OES"],
        boost_ceiling=r["boost_ceiling"], boost_ceiling_OES=r["boost_ceiling_OES"],
        eta_ceiling_OES=r["eta_ceiling_OES"],
        R_required=r["R_required"], boost_band_lo=r["boost_band_lo"],
        boost_band_hi=r["boost_band_hi"], req_expS_band_lo=r["req_expS_band_lo"],
        monotone_up=r["monotone_up"], sign_eta_pos=r["sign_eta_pos"],
        Mach_grid=r["Mach_grid"], eE_grid=r["eE_grid"], S_grid=r["S_grid"],
        n_grid=r["n_grid"], boost_grid=r["boost_grid"], eta_grid=r["eta_grid"],
        eta_base_recon=r["eta_base_recon"], recon_match=r["recon_match"],
        sigma_supp=r["sigma_supp"], eta_dkkms=r["eta_dkkms"],
        geom=r["geom"], fbar=r["fbar"], eps_nLI=r["eps_nLI"], phi_CP=r["phi_CP"],
        BAND_LO=r["BAND_LO"], BAND_HI=r["BAND_HI"],
        audit_sha256=audit_sha, content_sha256=content_sha,
    )
    print(f"\nSaved data: {OUT_NPZ}")

    make_plot(r)
    print(f"Saved plot: {OUT_PNG}")

    comp, sign_v, mag_v, regime_v, detail = evaluate_gate(r)      # (local)

    val = (f"eta_B_schwinger={r['eta_canonical']:.6e};eta_ceiling={r['eta_ceiling']:.6e};"
           f"boost_ceiling={r['boost_ceiling']:.6f};R_required={r['R_required']:.4f};"
           f"boost_band_lo={r['boost_band_lo']:.4f};band_reachable={r['band_reachable']};"
           f"underprod_oom_ceiling={r['underprod_oom_ceiling']:.4f};"
           f"eta_base={r['eta_base']:.6e};in_band={r['in_band_ceiling']}")  # (local)
    print(f"\n(value={val!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")

    note = (f"Acoustic-Schwinger eta_B in the Mach-13.75 transit. m_eff=Delta_0_GL=0.7704 "
            f"(QP gap); eE=v_terminal=26.545 (acoustic surface gravity, S43). "
            f"S_canon=pi m^2/eE={r['S_canon']:.4f} -> exp(-S)={r['exp_canon']:.4f}: the substrate "
            f"ALREADY sits at the strong-field production ceiling. Schwinger CEILING boost "
            f"(E->inf)={r['boost_ceiling']:.4f}x -> eta_max={r['eta_ceiling']:.3e} < band-low 3e-10; "
            f"band-low needs {r['boost_band_lo']:.2f}x (required exp(-S)={r['req_expS_band_lo']:.2f}>1 "
            f"IMPOSSIBLE). The 1.1-OOM shortfall is NOT a Mach/field-strength effect; field-strength "
            f"corridor CLOSED. Track-B (independent-mechanism-insufficient).")  # (local)

    rows = [                                                      # (local)
        f"# DECISIVE ALGEBRA: exp(-S)<=1 ALWAYS. Substrate at canonical fold sits at "
        f"exp(-S_canon)={r['exp_canon']:.4f} (93% to ceiling). Max Schwinger boost (E->inf)="
        f"{r['boost_ceiling']:.4f}x; band-low needs {r['boost_band_lo']:.2f}x -> required "
        f"exp(-S)={r['req_expS_band_lo']:.2f}>1 IMPOSSIBLE: in-band UNREACHABLE at ANY Mach. # {GATE_ID}",
        f"# Schwinger exponent monotone: S=pi m^2/eE -> 0+ as E(Mach) grows -> exp(-S) -> 1 "
        f"(production UNSUPPRESSED). sign PASS (eta_B monotone INCREASING in Mach, "
        f"chain Step3-4); but the substrate is ALREADY near-unsuppressed -> no exponential headroom. # {GATE_ID}",
        f"# m_eff=Delta_0_GL=0.770435 (QP gap=pair-creation threshold); eE_canon=v_terminal=26.545 "
        f"(S43 acoustic-white-hole surface gravity; S_Schwinger=pi Delta_0^2/v_terminal=0.0702 PROVEN S43, "
        f"NOT the wrong PG-horizon formula that gave factor-36). # {GATE_ID}",
        f"# CP/entropy normalization held FIXED from S98-W3-2 (eta_dkkms*sigma_supp*sin(phi_CP); "
        f"sigma_supp=eps_nLI^2*geom*fbar; recon of eta_B_base={r['eta_base_recon']:.6e} matches "
        f"S98 base {r['eta_base']:.6e} bit-for-bit: recon_match={r['recon_match']}). # {GATE_ID}",
        f"# OES-gap robustness x-check: ceiling(OES)={r['eta_ceiling_OES']:.4e} "
        f"(boost {r['boost_ceiling_OES']:.4f}x) STILL < band-low -> verdict anchor-robust. # {GATE_ID}",
        f"# SHORTFALL LOCUS: not the production exponential (ceiling-limited) but the CP-bias x "
        f"fiber-volume suppression sigma_supp -- the SAME locus as the W3-1 GGE-rescattering null "
        f"(R_enh<=1). Both substrate eta_B-enhancement corridors (W3-1, W3-3) CLOSED. # {GATE_ID}",
        f"# Track-B (independent-mechanism-insufficient, dual-prior 0.65->0.9): the Schwinger channel "
        f"does NOT close the gap at the substrate field strength; the delta_A magnitude posit (LBA-1) "
        f"remains the open failure locus. INFO-attribution: in-band would need exp(-S)>1 (unphysical), "
        f"NOT a finite Mach/E -> the residual is NOT a wrong-M_KK (G-4) field-strength artifact. # {GATE_ID}",
        f"# regulator_pin=N/A -- no Seeley-DeWitt a_n; no SCHEMATIC helper "
        f"(canonical_constants + s98 npz only). # {GATE_ID}",
        f"# cache-pin SOURCE-RECON Class-(c): orchestrator STALE-HINT 88f1e9b1->9e6d9cf7 targets "
        f"the s84 L12 MODE cache used by SIBLING gates; THIS gate reads canonical_constants + "
        f"s98_w3_2 (on-disk SHA runtime-pinned; s84 NOT read here) -> zero physics effect. # {GATE_ID}",
    ]

    print_verdict_payload(comp, val, audit_sha, content_sha,
                          sign_verdict=sign_v, magnitude_verdict=mag_v,
                          regime_verdict=regime_v, companion_note=note,
                          extra_rows=rows)

    print(f"\n=== {GATE_ID}: {comp} (sign={sign_v} mag={mag_v} regime={regime_v}; "
          f"wall {time.time()-t0:.1f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
