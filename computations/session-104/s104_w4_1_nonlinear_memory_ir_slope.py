#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""S104-W4-1-NONLINEAR-MEMORY-IR-SLOPE  (Wave 4, gem-sourced transit-shape)

GATE: Ünal-Veske (2511.08514) universal nonlinear-memory background deep-IR slope
      p(w) = 3 - 2*|(3w-1)/(3w+1)|  evaluated on the framework's PINNED stiff transit
      EOS w_stiff = 1 (Zel'dovich), classifies memory-tail vs causality-tail, and
      cross-checks INTERNAL CONSISTENCY against the independently-pinned blue tensor
      tilt n_T(transit) = +0.4676036871525688 (NT-BLUE-65) at the MATCHED transit scale.

CLASSIFICATION: PHONONIC. The GW memory tail is a substrate acoustic-relic SHAPE
      observable: the post-transit acoustic excitations' interference, whose deep-IR
      power-law is fixed by the substrate's own stiff EOS through the GR-universal
      nonlinear-memory relation. The arrow is substrate-first:
          D_K eigenvalues -> stiff transit EOS (w=1, modulus-kinetic domination
          through the van-Hove fold) -> emergent-metric a_2 self-coupling channel ->
          the nonlinear-memory GW background whose deep-IR slope IS the EOS.
      This is NOT "GW produced IN an expanding container" — the memory tail is a
      relic SHAPE of the substrate's own transit.

LOAD-BEARING SLOT-DISTINCTION (Class-8.7-adjacent degenerate-observable hazard,
      avoided by construction):
        memory driver  = w_stiff = 1 (Zel'dovich, s53_exflation_flatness_output.txt
                         "w = 1.000004 at fold"; a(t)~t^{1/3}).  <-- THE GEM PIN
        DISTINCT slot  = w_phonon = 0.202392 (s53_phonon_eos.npz; the post-fold GGE
                         relic-gas EOS at T_acoustic=0.112).  <-- loaded ONLY to PIN
                         the distinction; NEVER substituted as the memory-tail driver.

SCALE-CHANNEL (MANDATORY per phononic-framing.md "Scale-and-channel-tagging"):
      The comparator is n_T(transit) = +0.4676 at the PRODUCTION/transit scale
      (k ~ k_transit = 5.532e52 Mpc^-1, M_KK scale; NT-BLUE-65). The CMB-pivot images
      n_T(k_CMB) = -0.003, n_T_PathH = -0.0009338, n_T_PathC = -0.0014664 are DISTINCT,
      red, and FORBIDDEN as comparators (54.04-decade scale separation). The memory tail
      is sourced AT the stiff transit epoch, so the matched scale is the transit scale.

RETIREMENT (MANDATORY): the Omega_GW amplitude flagship is RETIRED (falsifier-master-
      inventory Row #7.audit-3/-4; LISA-STERILE; Omega_GW_acoustic_LISA_tail=4.046e-132).
      THIS GATE COMPUTES NO AMPLITUDE / DETECTABILITY CRITERION. It is a SHAPE /
      internal-consistency gate. A consistency FAIL is an INTERNAL inconsistency
      (the emergent metric failing a model-independent GR result), NEVER a dead-
      detector readout.

TRANSFER ASSUMPTION (pre-registered, named): SLOW-ROLL-CONSISTENCY-AT-TRANSIT-SCALE.
      n_T(transit) is read as the tensor spectral index of the GW background AT the
      transit/production scale and converted to an effective-w via the standard GR
      relation between a power-law-background GW spectral index and its EOS, evaluated
      at the SAME scale (transit), NOT transported to the CMB pivot. The exact map is:
          n_T(w)  =  2 * (3w - 1)/(3w + 1)
      validated at both EOS anchors (n_T(w=1) = +1 maximally blue; n_T(w=1/3) = 0
      radiation/flat). Its inverse (used for w_nT) is:
          inner_nT = n_T/2 ;  w_nT = (1 + inner_nT)/(3*(1 - inner_nT)).
      The 20% band absorbs the transfer-map ambiguity.

Trigger:  [CHAIN]  (directional pre-registration -> schema-v2 3-tuple required)
Verdict via the race-safe knowledge-MCP `emit_verdict` tool (this script PRINTS the
payload via print_verdict_payload; the agent calls emit_verdict). No open-coded append.
"""
from __future__ import annotations

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")   # CPU-scale scalar; cap before numpy
os.environ.setdefault("MKL_NUM_THREADS", "8")

import hashlib
import json
import sys
from fractions import Fraction
from pathlib import Path

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# --- canonical constants import (MANDATORY; S34+) ---------------------------
SHARED = Path(__file__).resolve().parents[1] / "_shared"
sys.path.insert(0, str(SHARED))
from canonical_constants import *  # noqa: F401,F403  (framework constants/provenance)

PROJECT_ROOT = Path(__file__).resolve().parents[2]

# ---------------------------------------------------------------------------
# Identity
# ---------------------------------------------------------------------------
GATE_ID = "S104-W4-1-NONLINEAR-MEMORY-IR-SLOPE"
SESSION = "S104"
SCHEME = "UNAL-VESKE-2511.08514-memory-tail"
# convention carries the RATIO+set-membership form AND the named transfer assumption
CONVENTION = "RATIO+set-membership_transfer=SLOW-ROLL-CONSISTENCY-AT-TRANSIT-SCALE"
L_MAX = "N/A"   # no spectral-triple truncation enters (EOS scalar + tilt scalar)

# ---------------------------------------------------------------------------
# Pre-registered thresholds (frozen at plan-freeze; anti-tolerance-shopping)
# ---------------------------------------------------------------------------
# pre-registered gate thresholds (frozen at plan-freeze; NOT local intermediates,
# NOT framework constants — gate-specific pre-registered criteria per
# session-104-plan-w4.md §W4-1 strict_PASS_boundary; anti-tolerance-shopping)
TAU_CONSISTENCY = 0.20          # (plan-frozen threshold) gate-(ii) consistency band
W_RAD_BOUNDARY = Fraction(1, 3) # (plan-frozen threshold) memory-tail iff w > 1/3 strict

OUTDIR = PROJECT_ROOT / "computations" / "session-104"
NPZ_PATH = OUTDIR / "s104_w4_1_nonlinear_memory_ir_slope.npz"
PNG_PATH = OUTDIR / "s104_w4_1_nonlinear_memory_ir_slope.png"
THIS_SCRIPT = Path(__file__).resolve()
CANONICAL_PATH = SHARED / "canonical_constants.py"

# input files (every file the script reads / pins)
IN_CANONICAL = CANONICAL_PATH
IN_S53_PHONON = PROJECT_ROOT / "computations" / "session-53" / "s53_phonon_eos.npz"
IN_S53_FLATNESS = (PROJECT_ROOT / "computations" / "session-53"
                   / "s53_exflation_flatness_output.txt")
IN_S65_BLUE = (PROJECT_ROOT / "computations" / "session-65"
               / "s65_blue_tensor_tilt.npz")
IN_S66_TRANSFER = (PROJECT_ROOT / "computations" / "session-66"
                   / "s66_tensor_transfer.npz")


# ---------------------------------------------------------------------------
# Dual-SHA helpers (canonical, per .claude/templates/script-template.py §4)
# ---------------------------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict:
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}  # (local)
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path, pins: dict):
    script_bytes = b""        # (local)
    try:
        script_bytes = script_path.read_bytes()
    except OSError:
        script_bytes = b""
    canonical_bytes = b""     # (local)
    try:
        canonical_bytes = canonical_path.read_bytes()
    except OSError:
        canonical_bytes = b""
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")          # (local)
    h_audit = hashlib.sha256()
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()      # (local)
    h_content = hashlib.sha256()
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict=None, magnitude_verdict=None,
                          regime_verdict=None, companion_note="", extra_rows=None):
    payload = {
        "session": int(SESSION.lstrip("Ss")),
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


# ---------------------------------------------------------------------------
# Closed-form maps (EXACT rationals via Fraction; float64 echoes for plot/npz)
# ---------------------------------------------------------------------------
def unal_veske_p(w: Fraction) -> Fraction:
    """Ünal-Veske universal nonlinear-memory deep-IR exponent.

    p(w) = 3 - 2*|(3w-1)/(3w+1)| ;  Omega_GW,mem ∝ f^{p(w)}.
    Memory-tail iff w > 1/3 ; causality-tail iff w < 1/3.
    """
    inner = (3 * w - 1) / (3 * w + 1)            # (local)
    return 3 - 2 * abs(inner)


def w_from_p_memory_branch(p: Fraction) -> Fraction:
    """Inverse of p(w) on the MEMORY branch (inner >= 0, w > 1/3).

    p = 3 - 2*inner  =>  inner = (3 - p)/2 ;
    inner = (3w-1)/(3w+1)  =>  w = (1 + inner)/(3*(1 - inner)).
    """
    inner = (3 - p) / 2                           # (local)
    return (1 + inner) / (3 * (1 - inner))


def nT_from_w(w: Fraction) -> Fraction:
    """SLOW-ROLL-CONSISTENCY-AT-TRANSIT-SCALE transfer map (forward).

    n_T(w) = 2*(3w-1)/(3w+1) = 2*inner. Standard GR relation between the tensor
    spectral index of a power-law-background GW spectrum and its EOS, evaluated at
    the production (transit) scale. Anchors: n_T(1)=+1, n_T(1/3)=0.
    """
    inner = (3 * w - 1) / (3 * w + 1)            # (local)
    return 2 * inner


def w_from_nT(nT: Fraction) -> Fraction:
    """SLOW-ROLL-CONSISTENCY-AT-TRANSIT-SCALE transfer map (inverse).

    inner_nT = n_T/2 ;  w_nT = (1 + inner_nT)/(3*(1 - inner_nT)).
    """
    inner_nT = nT / 2                             # (local)
    return (1 + inner_nT) / (3 * (1 - inner_nT))


# ---------------------------------------------------------------------------
# Compute
# ---------------------------------------------------------------------------
def compute() -> dict:
    # --- (1) load the DISTINCT relic-gas slot to PIN the slot-distinction -----
    #     w_phonon is the post-fold GGE relic-gas EOS; it is NOT the memory driver.
    d53 = np.load(IN_S53_PHONON, allow_pickle=True)
    w_phonon = float(d53["w_phonon"])            # (local) DISTINCT slot, NOT driver

    # --- the memory DRIVER: stiff Zel'dovich w_stiff = 1 EXACT ----------------
    #     Pinned EXACT from the Zel'dovich definition (modulus-kinetic domination,
    #     a(t)~t^{1/3}); s53_exflation_flatness_output.txt is the documentary anchor
    #     ("w = 1.000004 at fold" -> idealized stiff limit w=1).
    w_stiff = Fraction(1)                         # EXACT memory-tail driver

    assert w_phonon != float(w_stiff), (
        "SLOT-DISTINCTION GUARD: w_phonon (relic gas) must differ from w_stiff "
        "(memory driver). Refusing to mis-substitute the relic-gas EOS."
    )

    # --- (2) Ünal-Veske deep-IR exponent at w_stiff (Sage-QQ exact: p(1)=2) ----
    inner_stiff = (3 * w_stiff - 1) / (3 * w_stiff + 1)  # (local) = 1/2 exact
    p_stiff = unal_veske_p(w_stiff)              # = 2 exact

    # --- (3) branch classification: memory-tail iff w_stiff > 1/3 -------------
    is_memory_tail = w_stiff > W_RAD_BOUNDARY    # True (1 > 1/3)
    branch = "memory-tail" if is_memory_tail else "causality-tail"  # (local)

    # --- (4) INTERNAL-CONSISTENCY cross-check ---------------------------------
    # (4a) w_slope = inverse of p on memory branch at p_framework = p(1) = 2
    p_framework = p_stiff                        # the framework's memory-tail slope
    w_slope = w_from_p_memory_branch(p_framework)  # = 1 exact (round-trip)

    # (4b) load n_T(transit) — NT-BLUE-65, PRODUCTION/transit scale -------------
    d65 = np.load(IN_S65_BLUE, allow_pickle=True)
    nT_transit_f = float(d65["n_T"])             # 0.4676036871525688 (PASS, BLUE)
    # exact rational image of the published float64 (bit-faithful via Fraction)
    nT_transit_Q = Fraction(nT_transit_f)        # (local) exact-from-float64

    # documentary scale-channel pins (CONFIRM the comparator is transit, not CMB)
    d66 = np.load(IN_S66_TRANSFER, allow_pickle=True)
    nT_CMB_A = float(d66["n_T_CMB_scenario_A"])  # (local) -0.00302 (FORBIDDEN comparator)
    k_transit_Mpc = float(d66["k_transit_Mpc"])  # (local) 5.532e52
    k_CMB_pivot = float(d66["k_CMB_pivot"])      # (local) 0.05
    decades_sep = float(d66["decades_separation"])  # (local) 54.04
    # CMB-pivot single-field-consistency images (FORBIDDEN comparators; canonical)
    try:
        nT_PathH = float(n_T_PathH_canonical)    # (local) -0.000933812
    except Exception:
        nT_PathH = -0.000933812                  # (local) fallback literal (documentary)
    try:
        nT_PathC = float(n_T_PathC_canonical)    # (local) -0.00146644
    except Exception:
        nT_PathC = -0.00146644                   # (local) fallback literal (documentary)

    # (4c) w_nT via the SAME transfer map, at the SAME (transit) scale ----------
    w_nT = w_from_nT(nT_transit_Q)               # = 0.536764... exact rational

    # (4d) relative-deviation consistency (RATIO convention) -------------------
    dev_Q = abs(w_slope - w_nT) / w_slope        # exact rational deviation
    dev_f = float(dev_Q)                         # (local) 0.463236...

    # cross-handle diagnostics (narrative-only; NOT gates):
    nT_implied_by_slope = nT_from_w(w_slope)     # = +1 (what w_slope alone implies)
    p_implied_by_nT = unal_veske_p(w_nT)         # = 2.5324 (what n_T alone implies)

    # --- directional substitution-chain readout (for the 3-tuple) -------------
    # sign: branch-direction prediction (w_stiff > 1/3 -> memory-tail) is the gate's
    #       primary SHAPE/direction claim; verify it holds.
    sign_ok = is_memory_tail                     # True -> sign_verdict PASS
    # magnitude: the consistency band (single pass_band 0.20; no info_band)
    mag_pass = dev_f <= TAU_CONSISTENCY          # 0.4632 <= 0.20 -> False
    # regime: closed-form exact maps, evaluated at the MATCHED transit scale; valid.
    regime_valid = True

    return dict(
        w_phonon=w_phonon,
        w_stiff=float(w_stiff),
        inner_stiff=float(inner_stiff),
        p_stiff=float(p_stiff),
        p_stiff_exact_num=int(p_stiff.numerator),
        p_stiff_exact_den=int(p_stiff.denominator),
        is_memory_tail=bool(is_memory_tail),
        branch=branch,
        w_slope=float(w_slope),
        w_slope_exact_num=int(w_slope.numerator),
        w_slope_exact_den=int(w_slope.denominator),
        nT_transit=nT_transit_f,
        nT_transit_exact_num=int(nT_transit_Q.numerator),
        nT_transit_exact_den=int(nT_transit_Q.denominator),
        w_nT=float(w_nT),
        w_nT_exact_num=int(w_nT.numerator),
        w_nT_exact_den=int(w_nT.denominator),
        dev=dev_f,
        dev_exact_num=int(dev_Q.numerator),
        dev_exact_den=int(dev_Q.denominator),
        tau_consistency=TAU_CONSISTENCY,
        nT_implied_by_slope=float(nT_implied_by_slope),
        p_implied_by_nT=float(p_implied_by_nT),
        # documentary scale-channel (FORBIDDEN comparators recorded, not used in gate)
        nT_CMB_A=nT_CMB_A,
        nT_PathH=nT_PathH,
        nT_PathC=nT_PathC,
        k_transit_Mpc=k_transit_Mpc,
        k_CMB_pivot=k_CMB_pivot,
        decades_separation=decades_sep,
        # 3-tuple inputs
        sign_ok=bool(sign_ok),
        mag_pass=bool(mag_pass),
        regime_valid=bool(regime_valid),
    )


# ---------------------------------------------------------------------------
# Gate verdict (composite-collapse per gate-verdicts.md schema-v2)
# ---------------------------------------------------------------------------
def collapse(sign_v: str, mag_v: str, regime_v: str) -> str:
    """Deterministic composite collapse (PRE-REGISTERED; gate-verdicts.md)."""
    if regime_v == "BREAKDOWN":
        return "FAIL"
    if sign_v == "FAIL":
        return "FAIL"
    if mag_v == "FAIL" and regime_v == "VALID":
        return "FAIL"
    if mag_v == "FAIL" and regime_v == "MARGINAL":
        return "INFO"
    if mag_v == "INFO":
        return "INFO"
    return "PASS"


def make_plot(res: dict) -> None:
    w = np.linspace(0.0, 1.0, 2001)              # (local)
    inner = (3.0 * w - 1.0) / (3.0 * w + 1.0)    # (local)
    p = 3.0 - 2.0 * np.abs(inner)                # (local) p(w) over w in [0,1]

    fig, ax = plt.subplots(figsize=(8.2, 5.6))
    ax.plot(w, p, "-", lw=2.2, color="#1b4f9c",
            label=r"$p(w)=3-2\,|(3w-1)/(3w+1)|$ (Ünal-Veske memory)")

    # w = 1/3 branch boundary (memory-tail | causality-tail)
    ax.axvline(1.0 / 3.0, color="#888888", ls="--", lw=1.3)
    ax.text(1.0 / 3.0 + 0.006, 0.35, r"$w=1/3$ branch boundary"
            "\n(memory-tail $w>1/3$ | causality-tail $w<1/3$)",
            fontsize=8.5, color="#555555", va="bottom")

    # w_stiff = 1 memory-tail point: p = 2 EXACT
    ax.plot([res["w_stiff"]], [res["p_stiff"]], "o", ms=11, color="#c0392b",
            zorder=5, label=r"$w_{\rm stiff}=1\ \Rightarrow\ p=2$ (memory-tail, framework driver)")
    ax.annotate(r"$p(w{=}1)=2$ EXACT", xy=(1.0, 2.0), xytext=(0.66, 2.35),
                fontsize=9.5, color="#c0392b",
                arrowprops=dict(arrowstyle="->", color="#c0392b", lw=1.2))

    # n_T(transit)-implied effective-w overlay: w_nT, and the p it would imply
    w_nT = res["w_nT"]                            # (local)
    p_at_wnT = res["p_implied_by_nT"]             # (local)
    ax.plot([w_nT], [p_at_wnT], "s", ms=10, color="#2e8b57", zorder=5,
            label=(r"$n_T(\mathrm{transit}){=}{+}0.4676\Rightarrow w_{nT}{=}%.4f$"
                   r" ($p{=}%.3f$)" % (w_nT, p_at_wnT)))
    ax.axvline(w_nT, color="#2e8b57", ls=":", lw=1.3)
    ax.axvline(res["w_slope"], color="#c0392b", ls=":", lw=1.0, alpha=0.7)

    # consistency annotation
    dev = res["dev"]                              # (local)
    verdict_txt = "FAIL" if dev > res["tau_consistency"] else "PASS"  # (local)
    ax.text(0.02, 2.78,
            (r"consistency: $|w_{\rm slope}-w_{nT}|/w_{\rm slope}=%.4f$"
             "\n"
             r"threshold $\tau=%.2f$  $\Rightarrow$  %s (INTERNAL)"
             % (dev, res["tau_consistency"], verdict_txt)),
            fontsize=9, color="#333333",
            bbox=dict(boxstyle="round", fc="#fff4e6", ec="#d68910"))

    ax.set_xlabel(r"EOS  $w$")
    ax.set_ylabel(r"deep-IR memory exponent  $p(w)$   ($\Omega_{\rm GW,mem}\propto f^{p}$)")
    ax.set_title("S104-W4-1  Ünal-Veske nonlinear-memory deep-IR slope on the stiff "
                 "transit EOS\n(SHAPE / internal-consistency — NO amplitude/detectability; "
                 "amplitude RETIRED LISA-STERILE)", fontsize=9.5)
    ax.set_xlim(0.0, 1.0)
    ax.set_ylim(0.0, 3.15)
    ax.grid(alpha=0.25)
    ax.legend(loc="lower right", fontsize=8.0, framealpha=0.92)
    fig.tight_layout()
    fig.savefig(PNG_PATH, dpi=140)
    plt.close(fig)


def main() -> int:
    OUTDIR.mkdir(parents=True, exist_ok=True)
    inputs = [IN_CANONICAL, IN_S53_PHONON, IN_S53_FLATNESS, IN_S65_BLUE, IN_S66_TRANSFER]
    pins = log_input_pins(inputs)

    res = compute()

    # --- echo numbers (numbers-first; verdict second) -------------------------
    print(f"\n=== {GATE_ID} — results ===")
    print(f"  EOS slot-distinction:")
    print(f"    w_stiff (MEMORY DRIVER, Zel'dovich)     = {res['w_stiff']:.6f}  (pinned EXACT = 1)")
    print(f"    w_phonon (DISTINCT relic-gas slot)      = {res['w_phonon']:.6f}  (NOT substituted)")
    print(f"  Ünal-Veske deep-IR exponent:")
    print(f"    inner(w=1) = (3-1)/(3+1)                = {res['inner_stiff']:.6f}  (= 1/2 exact)")
    print(f"    p(w_stiff=1) = 3 - 2*(1/2)              = {res['p_stiff']:.6f}  "
          f"(= {res['p_stiff_exact_num']}/{res['p_stiff_exact_den']} EXACT)")
    print(f"    branch (w_stiff > 1/3 ?)                = {res['branch']}  "
          f"(memory_tail={res['is_memory_tail']})")
    print(f"  Internal-consistency cross-check (TRANSIT scale; transfer="
          f"SLOW-ROLL-CONSISTENCY-AT-TRANSIT-SCALE):")
    print(f"    w_slope = inv_p(p=2, memory branch)     = {res['w_slope']:.6f}  "
          f"(= {res['w_slope_exact_num']}/{res['w_slope_exact_den']}, round-trip)")
    print(f"    n_T(transit) [NT-BLUE-65, PASS]         = {res['nT_transit']:.10f}  (PRODUCTION scale)")
    print(f"    w_nT = inv_transfer(n_T(transit))       = {res['w_nT']:.6f}  "
          f"(= {res['w_nT_exact_num']}/{res['w_nT_exact_den']})")
    print(f"    |w_slope - w_nT|/w_slope                = {res['dev']:.6f}  "
          f"(threshold tau = {res['tau_consistency']:.2f})")
    print(f"  cross-handle diagnostics (narrative; NOT gates):")
    print(f"    n_T implied by w_slope=1                = {res['nT_implied_by_slope']:.6f}  (maximally blue)")
    print(f"    p implied by n_T(transit) via w_nT      = {res['p_implied_by_nT']:.6f}")
    print(f"  FORBIDDEN comparators (recorded, NOT used): n_T(k_CMB,A)={res['nT_CMB_A']:.6f}, "
          f"PathH={res['nT_PathH']:.7f}, PathC={res['nT_PathC']:.7f}; "
          f"scale separation = {res['decades_separation']:.2f} decades")

    # --- 3-tuple (directional pre-registration; [CHAIN]) ----------------------
    sign_verdict = "PASS" if res["sign_ok"] else "FAIL"     # branch direction correct
    if res["mag_pass"]:
        magnitude_verdict = "PASS"
    else:
        # single pass_band only (0.20); no info_band -> deviation > band is FAIL
        magnitude_verdict = "FAIL"
    regime_verdict = "VALID" if res["regime_valid"] else "BREAKDOWN"
    composite = collapse(sign_verdict, magnitude_verdict, regime_verdict)

    print(f"\n  3-tuple: sign={sign_verdict} magnitude={magnitude_verdict} "
          f"regime={regime_verdict}  =>  composite={composite}")

    # --- save npz (full float64 + exact-rational num/den + transfer formula) --
    np.savez(
        NPZ_PATH,
        gate_id=GATE_ID,
        verdict=composite,
        # core numbers
        w_stiff=res["w_stiff"],
        w_phonon_distinct_slot=res["w_phonon"],
        p_stiff=res["p_stiff"],
        p_stiff_exact_num=res["p_stiff_exact_num"],
        p_stiff_exact_den=res["p_stiff_exact_den"],
        inner_stiff=res["inner_stiff"],
        is_memory_tail=res["is_memory_tail"],
        branch=res["branch"],
        w_slope=res["w_slope"],
        w_slope_exact_num=res["w_slope_exact_num"],
        w_slope_exact_den=res["w_slope_exact_den"],
        nT_transit=res["nT_transit"],
        nT_transit_exact_num=res["nT_transit_exact_num"],
        nT_transit_exact_den=res["nT_transit_exact_den"],
        w_nT=res["w_nT"],
        w_nT_exact_num=res["w_nT_exact_num"],
        w_nT_exact_den=res["w_nT_exact_den"],
        dev=res["dev"],
        dev_exact_num=res["dev_exact_num"],
        dev_exact_den=res["dev_exact_den"],
        tau_consistency=res["tau_consistency"],
        nT_implied_by_slope=res["nT_implied_by_slope"],
        p_implied_by_nT=res["p_implied_by_nT"],
        # the EXACT transfer formula used (emitted per HARD CONSTRAINT)
        transfer_assumption="SLOW-ROLL-CONSISTENCY-AT-TRANSIT-SCALE",
        transfer_formula_forward="n_T(w) = 2*(3w-1)/(3w+1)",
        transfer_formula_inverse="w_nT = (1 + n_T/2)/(3*(1 - n_T/2))",
        unal_veske_formula="p(w) = 3 - 2*|(3w-1)/(3w+1)|",
        unal_veske_inverse_memory="w = (1 + (3-p)/2)/(3*(1 - (3-p)/2))",
        scale_channel="TRANSIT-SCALE",
        # FORBIDDEN comparators (documentary)
        nT_CMB_scenario_A_FORBIDDEN=res["nT_CMB_A"],
        nT_PathH_FORBIDDEN=res["nT_PathH"],
        nT_PathC_FORBIDDEN=res["nT_PathC"],
        k_transit_Mpc=res["k_transit_Mpc"],
        k_CMB_pivot=res["k_CMB_pivot"],
        decades_separation=res["decades_separation"],
        # 3-tuple
        sign_verdict=sign_verdict,
        magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
        composite_verdict=composite,
        scheme=SCHEME,
        convention=CONVENTION,
        retirement_note=("Omega_GW amplitude RETIRED (Row #7.audit-3/-4, LISA-STERILE); "
                         "SHAPE/internal-consistency gate; NO amplitude/detectability "
                         "criterion; a FAIL is an INTERNAL inconsistency, not a dead detector"),
    )
    print(f"\n  npz  -> {NPZ_PATH}")

    make_plot(res)
    print(f"  plot -> {PNG_PATH}")

    # --- dual SHA + payload ---------------------------------------------------
    audit_sha, content_sha = compute_dual_sha(THIS_SCRIPT, CANONICAL_PATH, pins)
    print(f"\n  audit_sha256   = {audit_sha}")
    print(f"  content_sha256 = {content_sha}")

    # value payload: report the consistency deviation (the gate's decision metric)
    # plus the branch/exponent. No single-quote chars (tool wraps value='...').
    value = (f"dev={res['dev']:.6f}_vs_tau={res['tau_consistency']:.2f}_"
             f"INTERNAL-INCONSISTENT;p={res['p_stiff_exact_num']}_EXACT_memory-tail;"
             f"w_slope={res['w_slope']:.6f};w_nT={res['w_nT']:.6f};"
             f"transfer=SLOW-ROLL-CONSISTENCY-AT-TRANSIT-SCALE;SHAPE-not-amplitude")

    extra = [
        ("# transfer=SLOW-ROLL-CONSISTENCY-AT-TRANSIT-SCALE "
         "n_T(w)=2*(3w-1)/(3w+1); scale_channel=TRANSIT (k_transit=5.532e52 Mpc^-1); "
         "# S104-W4-1 transfer-map row"),
        ("# RETIREMENT: Omega_GW amplitude RETIRED Row#7.audit-3/-4 LISA-STERILE; "
         "SHAPE/internal-consistency only; FAIL is INTERNAL inconsistency not dead-detector; "
         "# S104-W4-1 retirement row"),
        ("# slot-distinction: w_stiff=1 MEMORY DRIVER vs w_phonon=0.202392 relic-gas DISTINCT "
         "(NOT substituted); # S104-W4-1 slot-distinction row"),
    ]

    print_verdict_payload(
        composite, value, audit_sha, content_sha,
        sign_verdict=sign_verdict,
        magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict,
        extra_rows=extra,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
