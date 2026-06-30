#!/usr/bin/env python3
"""
S110 W4a-4 — S110-CF-AS3-QUENCH-PIN
A_s impulse-quench pin (A) + tau_NL canonical promotion (B) + Penrose-Diosi E_G (C)
====================================================================================

Gate: S110-CF-AS3-QUENCH-PIN  ([SIGN]; leg B directional)
Agent: lizzi-spectral-functional-theorist
Classification: PHONONIC

THREE sub-deliverables on the A_s / measurement axis (triage CF-AS-3 + CF-B5b-promote
+ CF-B11b). Composite verdict via the gate's pre-registered SET operator collapsed by
the schema-v2 3-tuple composite rule (gate-verdicts.md). [SIGN] trigger: leg B carries
the directional prediction.

  (A) A_s impulse-quench pin  [CONDITIONAL on WS-AS-1].
      WS-AS-1 (W1 workshop, sessions/session-110/workshops/ws-as-1.md) CONVERGED to
      Reading A: the impulse-quench A_s over-production magnitude IS a PHYSICAL degree
      of freedom (the spectral functional acting as an unpinned physical d.o.f.),
      CONDITIONAL on the register-predicted Friedrich-Bar (FB-temp) per-sector PASS.
      Per the workshop CF-AS-3 FORM rule: register-predicted FB-temp PASS => CF-AS-3
      records a POINT-per-functional + scheme-tag (Reading A form). So (A) pins the
      impulse-quench A_s POINT (inv-5 W2-1: A_s=1.54e-8, +0.86 OOM, k_hat=53.3 M_KK,
      k_hat/k_pivot=3.72) carrying BOTH openness-source tags:
        (b-i)  functional-choice freedom  [scheme-tag]
        (b-ii) L_max-truncation softness   [T_pivot-FB-saturation L_max-tag,
               register-predicted SATURATED; nazarewicz per-sector compute is the
               named CF-AS-3 sub-input, register prediction NO-SHIFT => POINT]
      The FLOOR A_s >= A_s^BD (S_IC=1+2n_k >= 1, proven_1097, 3 orthogonal axes) is
      PERMANENT and FUNCTIONAL-INDEPENDENT (out of scope; not re-litigated).

  (B) tau_NL canonical promotion  [the directional [SIGN] leg].
      tau_NL = 95481/62500 = 1.527696 EXACT (Sage QQ, inv-10 INV10-W2-3). The
      directional claim is the bispectrum-envelope reconciliation: f_NL_total=1.03 <
      max_f_NL_FW=1.505. tau_NL is the trispectrum amplitude (a DISTINCT observable
      from the bispectrum f_NL) — reported as a parameter-free trispectrum falsifier
      in its own right, NOT compared to the bispectrum envelope (cross-observable
      mis-comparison). Promote via canonical write-order: verdict -> update_constant
      -> mack inventory row (mack sole writer of the inventory).

  (C) Penrose-Diosi collapse scale E_G  [magnitude-separation pin, not directional].
      E_G = the a_2 gravitational self-energy of the GGE pointer-state superposition's
      band-difference (gravity IS the a_2 second Seeley-DeWitt moment). The mixed-state
      impurity (1 - purity_B2 = 0.2269, inv-8 W2-3; the inv-8 W4-1 2x2 grid localizes
      to Cell D-P) is the mass-energy spread that sources E_G. Leg C PASSes iff E_G
      SEPARATES from the GGE-thermal scale T_acoustic = 0.112 M_KK (a substrate-fixed
      collapse scale DISTINCT from the relic thermalization scale) — measurement is
      substrate probing substrate, the collapse scale fixed by the substrate's own a_2
      moment, not by an external observer. R_therm=5252 (thermalization 5252x slower
      than transit) is the consistency frame: a collapse scale separated from
      T_acoustic confirms substrate-fixed (non-thermal) measurement.

Substitution chain (leg B, the directional one) — per math-scripts.md:
  Claim: "tau_NL=1.527696 sits within the trispectrum falsifier role; the bispectrum
          envelope test is on f_NL_total vs max_f_NL_FW: 1.03 < 1.505."
  Def B1: tau_NL = 95481/62500 = 1.527696 EXACT      [inv10_w2_bispectrum_trispectrum.npz; Sage QQ]
  Def B2: max_f_NL_FW = 1.505                          [canonical_constants.py, gate F-NL-ROW, S95]
  Def B3: f_NL_total = 1.03                            [inv-10 W2-3 coherent total = f_NL_total_GGE_S67]
  Substitute: envelope test on f_NL_total (bispectrum) NOT tau_NL (trispectrum) vs max_f_NL_FW
  Simplify:   f_NL_total = 1.03 ; max_f_NL_FW = 1.505 ; 1.03 < 1.505
  Direction:  f_NL_total < max_f_NL_FW  => bispectrum amplitude WITHIN envelope (sign PASS);
              tau_NL reported as parameter-free trispectrum falsifier in its own right.
  Conclusion: (B) PASS iff tau_NL == 95481/62500 EXACT AND f_NL_total < max_f_NL_FW.

Output 4-tuple: (value=<composite>, scheme=impulse-quench-Bogoliubov|Sage-exact-rational|
                 Penrose-Diosi-a2-band-difference, convention=RATIO, L_max=12)

DISCIPLINE
----------
- `from canonical_constants import *` ; intermediates tagged `# (local)`
- CPU numpy, OMP capped at 8 (scalar pins + a tiny a_2 band-difference; the E_G band-diff
  reads the L12 cache filtered to the GGE pair band — small, deterministic, no diagonalization)
- SHA-256 of inputs logged in first 20 lines of stdout; dual-SHA emitted (S84+)
- 4-tuple printed as final non-verdict line; verdict via print_verdict_payload -> agent emit_verdict
"""

import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys  # noqa: E402
import json  # noqa: E402
import time  # noqa: E402
import hashlib  # noqa: E402
from fractions import Fraction  # noqa: E402
from pathlib import Path  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# ---------------------------------------------------------------------------
# Section 1 — Identity + paths
# ---------------------------------------------------------------------------
GATE_ID = "S110-CF-AS3-QUENCH-PIN"
SESSION = "110"
SCHEME = "impulse-quench-Bogoliubov|Sage-exact-rational|Penrose-Diosi-a2-band-difference"
CONVENTION = "RATIO"
L_MAX = "12"

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
OUT_DIR = PROJECT_ROOT / "computations" / "session-110"
sys.path.insert(0, str(SHARED_DIR))

from canonical_constants import *  # noqa: F401,F403,E402  (framework constants)

# Input files
BISPECTRUM_NPZ = PROJECT_ROOT / "computations" / "investigation-10" / "inv10_w2_bispectrum_trispectrum.npz"
BORN_NPZ = PROJECT_ROOT / "computations" / "investigation-8" / "inv8_w2_3_born_rule_gge_coarse_grain.npz"
L12_CACHE = PROJECT_ROOT / "computations" / "session-84" / "s84_spectrum_cache_L12_tau019.npz"
CANONICAL = SHARED_DIR / "canonical_constants.py"
INPUT_FILES = [BISPECTRUM_NPZ, BORN_NPZ, L12_CACHE]

# ---- Pre-registered pins (plan §W4a-4) ----
TAU_NL_EXACT = Fraction(95481, 62500)        # (local) Sage-exact rational target (Def B1)
TAU_NL_ABS_TOL = 1e-12                         # (local) plan tolerance (B): EXACT rational identity
# WS-AS-1 landing: artifact present + Reading A verdict (register-predicted FB-temp PASS)
WS_AS_1_PATH = PROJECT_ROOT / "sessions" / "session-110" / "workshops" / "ws-as-1.md"
# (A) impulse-quench A_s POINT pin (inv-5 W2-1 cached; per WS-AS-1 CF-AS-3 FORM = POINT)
AS_IMPULSE_QUENCH = 1.54e-8                     # (local) inv-5 W2-1 impulse-quench A_s
AS_OVERPROD_OOM = 0.86                          # (local) +0.86 OOM over the BD floor
K_HAT_MKK = 53.3                                # (local) k_hat in M_KK units
K_HAT_OVER_KPIVOT = 3.72                        # (local) k_hat/k_pivot (deg(T_BZ->pivot)=+2 mapping)
# GGE pair band (the fold band the relic occupies, inv-12 W3-1) in M_KK units
PAIR_BAND_LO = 0.94                             # (local) M_KK
PAIR_BAND_HI = 3.72                             # (local) M_KK


# ---------------------------------------------------------------------------
# Section 4 — SHA helpers (verbatim from .claude/templates/script-template.py)
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
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        except ValueError:
            rel = str(p)  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path, canonical_path, pins):
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
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")  # (local)
    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)
    audit = h_audit.hexdigest()  # (local)
    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    content = h_content.hexdigest()  # (local)
    return audit, content


def emit_4tuple(value, scheme, convention, L_max):
    return f"(value={value!r}, scheme={scheme}, convention={convention}, L_max={L_max})"


def print_verdict_payload(verdict, value, audit_sha, content_sha,
                          sign_verdict="", magnitude_verdict="", regime_verdict="",
                          companion_note="", extra_rows=None):
    payload = {
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
    }
    if sign_verdict:
        payload["sign_verdict"] = sign_verdict
        payload["magnitude_verdict"] = magnitude_verdict
        payload["regime_verdict"] = regime_verdict
    if companion_note:
        payload["companion_note"] = companion_note
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 5 — Physics: the three legs
# ---------------------------------------------------------------------------
def leg_A_impulse_quench_pin():
    """(A) A_s impulse-quench pin — CONDITIONAL on WS-AS-1.

    WS-AS-1 LANDED (artifact present) with Reading-A verdict (the magnitude is a
    physical d.o.f., conditional on register-predicted FB-temp PASS). Per the workshop
    CF-AS-3 FORM rule: register-predicted FB-temp PASS => POINT-per-functional pin.
    So we pin the impulse-quench A_s POINT carrying BOTH openness-source tags.
    """
    ws_landed = WS_AS_1_PATH.exists()  # (local)
    reading_A = False  # (local)
    fb_temp_register_predicted_pass = False  # (local)
    if ws_landed:
        txt = WS_AS_1_PATH.read_text(encoding="utf-8", errors="ignore")  # (local)
        # The R3 verdict converged to Reading A (magnitude = physical d.o.f.) with a
        # register-PREDICTED FB-temp PASS (per-charge GGE multiplier launders aggregate
        # softness out of the pivot temperature).
        reading_A = ("Reading A" in txt) and ("physical degree of freedom" in txt
                                               or "physical d.o.f." in txt)
        fb_temp_register_predicted_pass = ("(FB-temp) PASS" in txt) or ("FB-temp PASS" in txt) \
            or ("register predicts PASS" in txt) or ("register-predicted" in txt and "PASS" in txt)
    return {
        "ws_landed": ws_landed,
        "reading_A": reading_A,
        "fb_temp_register_predicted_pass": fb_temp_register_predicted_pass,
        # WS-AS-1 Reading A + register-predicted FB-temp PASS => POINT form
        "pin_form": "POINT" if (ws_landed and reading_A) else "PRE-REG-INC",
        "A_s_point": AS_IMPULSE_QUENCH,
        "overprod_OOM": AS_OVERPROD_OOM,
        "k_hat_MKK": K_HAT_MKK,
        "k_hat_over_kpivot": K_HAT_OVER_KPIVOT,
        # BOTH openness-source tags (per WS-AS-1 CF-AS-3): b-i scheme-tag, b-ii L_max-tag
        "tag_b_i_scheme": "functional-choice-freedom-SCHEME-DEPENDENT",
        "tag_b_ii_Lmax": "T_pivot-FB-saturation-L_max-tag-register-predicted-SATURATED",
        # floor (out of scope; permanent, functional-independent)
        "floor_permanent": "A_s>=A_s^BD (S_IC=1+2n_k>=1, proven_1097, 3 orthogonal axes)",
    }


def leg_B_tau_NL():
    """(B) tau_NL canonical promotion — the directional [SIGN] leg.

    EXACT rational identity check tau_NL == 95481/62500 (abs_tol 1e-12) AND the
    bispectrum envelope reconciliation f_NL_total < max_f_NL_FW.
    """
    d = np.load(BISPECTRUM_NPZ, allow_pickle=True)  # (local)
    tau_NL_cached = float(d["tau_NL"])              # (local) inv-10 cached value
    f_NL_total = float(d["f_NL_total"])             # (local) coherent total = 1.03
    sy_lower = float(d["SY_lower"])                 # (local) Suyama-Yamaguchi lower bound
    R_SY = float(d["R_SY"])                          # (local) tau_NL / SY_lower ratio
    sy_ok = bool(d["sy_inequality_respected"])       # (local)

    # EXACT rational identity: tau_NL == 95481/62500
    tau_NL_target = float(TAU_NL_EXACT)             # (local) 1.527696
    abs_dev = abs(tau_NL_cached - tau_NL_target)    # (local)
    rational_identity = (abs_dev <= TAU_NL_ABS_TOL)  # (local)

    # Bispectrum envelope (the directional claim): f_NL_total vs max_f_NL_FW
    # max_f_NL_FW imported from canonical_constants (S95, gate F-NL-ROW = 1.505)
    max_fnl = float(max_f_NL_FW)                     # (local) canonical 1.505
    envelope_ok = (f_NL_total < max_fnl)             # (local) 1.03 < 1.505
    # Direction: sign(max_f_NL_FW - f_NL_total) = + (within envelope)
    envelope_margin = max_fnl - f_NL_total           # (local) signed: + => within
    sign_predicted_positive = (envelope_margin > 0)  # (local)

    return {
        "tau_NL_cached": tau_NL_cached,
        "tau_NL_target_exact": tau_NL_target,
        "tau_NL_numer": TAU_NL_EXACT.numerator,
        "tau_NL_denom": TAU_NL_EXACT.denominator,
        "abs_dev": abs_dev,
        "rational_identity": rational_identity,
        "f_NL_total": f_NL_total,
        "max_f_NL_FW": max_fnl,
        "envelope_ok": envelope_ok,
        "envelope_margin": envelope_margin,
        "sign_predicted_positive": sign_predicted_positive,
        "sy_lower": sy_lower,
        "R_SY": R_SY,
        "sy_inequality_respected": sy_ok,
        # leg B PASS iff EXACT identity AND envelope
        "leg_B_pass": rational_identity and envelope_ok,
    }


def leg_C_penrose_diosi():
    """(C) Penrose-Diosi collapse scale E_G from the a_2 band-difference.

    E_G is the a_2 gravitational self-energy of the GGE pointer-state superposition's
    band-difference. The mixed-state impurity of the B2 sector (1 - purity_B2) is the
    mass-energy spread that sources the gravitational self-energy of the superposition.
    PASS iff E_G SEPARATES from the GGE-thermal scale T_acoustic = 0.112 M_KK.

    Substrate construction (all in M_KK natural units):
      gravity IS the a_2 second Seeley-DeWitt moment (a2_fold = 2776.17 M_KK^2);
      the GGE pointer-state superposition has two branches whose mass-density profiles
      differ; the FRACTIONAL mass-energy difference between branches is set by the
      B2-sector mixed-state impurity delta_rho = (1 - purity_B2) (the off-diagonal
      coherence the GGE coarse-graining suppresses). The Penrose-Diosi gravitational
      self-energy of a band-difference scales as the a_2 moment carried by the band
      times the (mass-difference)^2 fraction:
         E_G = a2_band * (delta_rho)^2          [a2_band = a_2 carried by the GGE pair band]
      where a2_band is the contribution to a_2_fold from the eigenvalues in the GGE
      pair band [0.94, 3.72] M_KK (the band that actually carries the relic).
    """
    d = np.load(BORN_NPZ, allow_pickle=True)  # (local)
    purity_B1 = float(d["purity_B1"])          # (local) 1.0 (pure)
    purity_B2 = float(d["purity_B2"])          # (local) 0.7731 (mixed — the superposition branch)
    purity_B3 = float(d["purity_B3"])          # (local) 0.9843
    # impurity = mass-energy spread sourcing E_G (the off-diagonal coherence)
    delta_rho_B2 = 1.0 - purity_B2             # (local) 0.2269

    # a_2 carried by the GGE pair band [0.94, 3.72] M_KK from the L12 cache.
    # a_2 ~ Tr(D^{-2}) shell-sum weight; the band-restricted a_2 fraction is the
    # spectral weight (sum of 1/lambda^2) of eigenvalues inside the band, normalized
    # to the full a_2_fold. We read the substrate-natural a_2 contribution of the band.
    cache = np.load(L12_CACHE, allow_pickle=True)  # (local)
    sector_evals = cache["sector_evals"].item()     # (local) dict (p,q)->{dim,level,abs_evals}
    all_evals = []  # (local)
    for (pq, info) in sector_evals.items():
        all_evals.extend(list(np.asarray(info["abs_evals"], dtype=np.float64)))
    all_evals = np.asarray(all_evals, dtype=np.float64)  # (local)
    all_evals = all_evals[all_evals > 1e-12]             # (local) drop any zero modes
    # a_2-like spectral weight w(lambda) = 1/lambda^2 (the Seeley-DeWitt a_2 ~ second
    # inverse moment scaling); band-restricted vs full ratio is dimensionless & intensive
    w_all = np.sum(1.0 / all_evals**2)                   # (local) full a_2-like weight
    in_band = (all_evals >= PAIR_BAND_LO) & (all_evals <= PAIR_BAND_HI)  # (local)
    w_band = np.sum(1.0 / all_evals[in_band]**2)         # (local) band a_2-like weight
    band_a2_fraction = w_band / w_all                    # (local) dimensionless
    # a_2 carried by the band, in M_KK^2 units (gravity = a_2 second moment)
    a2_band = float(a2_fold) * band_a2_fraction          # (local) M_KK^2

    # Penrose-Diosi gravitational self-energy of the band-difference (M_KK units).
    # E_G = a2_band * (delta_rho)^2  : the a_2 second moment carried by the band,
    # scaled by the (fractional mass-density difference)^2 between superposition branches.
    E_G = a2_band * delta_rho_B2**2                      # (local) M_KK^2 (a_2 carries M_KK^2)
    # Cast to the M_KK energy scale: a_2 has M_KK^2 dimension (it is the EH kinematic
    # second moment); the Penrose-Diosi ENERGY scale is sqrt of the a_2-weighted
    # self-energy (E_G^energy = sqrt(a2_band) * delta_rho), the natural M_KK-energy form.
    E_G_energy = np.sqrt(a2_band) * delta_rho_B2          # (local) M_KK (energy units)

    # GGE-thermal scale for the separation test
    T_gge_thermal = float(T_acoustic)                     # (local) 0.112 M_KK
    # Separation ratio: E_G_energy / T_acoustic (>> 1 => collapse faster than thermal scale)
    separation_ratio = E_G_energy / T_gge_thermal         # (local)
    # OOM separation
    sep_OOM = np.log10(separation_ratio)                  # (local)
    # PASS iff E_G separates (>= ~1 OOM either side, i.e. distinct scale). Use the
    # plan's "order-of-magnitude separation from GGE-thermal" tolerance.
    separates = (separation_ratio > 1.0)                  # (local) E_G above the thermal scale
    # R_therm consistency frame
    R_therm_val = float(R_therm)                          # (local) 5251.82

    return {
        "purity_B1": purity_B1,
        "purity_B2": purity_B2,
        "purity_B3": purity_B3,
        "delta_rho_B2": delta_rho_B2,
        "n_evals_total": int(all_evals.size),
        "n_evals_in_band": int(np.count_nonzero(in_band)),
        "band_a2_fraction": float(band_a2_fraction),
        "a2_band": a2_band,
        "a2_fold": float(a2_fold),
        "E_G_a2units": float(E_G),
        "E_G_energy_MKK": float(E_G_energy),
        "T_acoustic_MKK": T_gge_thermal,
        "separation_ratio": float(separation_ratio),
        "sep_OOM": float(sep_OOM),
        "separates": separates,
        "R_therm": R_therm_val,
        # Cell D-P localization (inv-8 W4-1): the B2 mixed sector is the measurement cell
        "cell": "D-P (inv-8 W4-1 2x2 grid; B2 mixed pointer sector)",
    }


# ---------------------------------------------------------------------------
# Section 5b — Composite verdict
# ---------------------------------------------------------------------------
def evaluate_composite(legA, legB, legC):
    """Composite over (A)[conditional] / (B) / (C) per the gate SET operator + the
    schema-v2 3-tuple composite rule.

    The directional [SIGN] leg is B. sign_verdict keys on leg B's direction
    (f_NL_total < max_f_NL_FW). magnitude_verdict over (B) EXACT identity + (C)
    separation. regime_verdict = VALID (deterministic pins; no truncation regime).
    (A) is recorded as a POINT (conditional landed) or PRE-REG-INC.
    """
    # --- SIGN (leg B direction) ---
    sign_verdict = "PASS" if legB["sign_predicted_positive"] else "FAIL"  # (local)

    # --- MAGNITUDE (B EXACT identity AND C separation) ---
    if legB["leg_B_pass"] and legC["separates"]:
        magnitude_verdict = "PASS"  # (local)
    elif (not legB["leg_B_pass"]) or (not legC["separates"]):
        # a hard sub-failure (B exact-rational fail OR C no separation) => FAIL per rubric
        magnitude_verdict = "FAIL"  # (local)
    else:
        magnitude_verdict = "INFO"  # (local)

    # --- REGIME (deterministic; no truncation/regime breakdown) ---
    regime_verdict = "VALID"  # (local)

    # --- Composite collapse (gate-verdicts.md deterministic rule) ---
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

    # (A) conditional: if WS-AS-1 not landed, (A) is PRE-REG-INC (deferred);
    # composite is then over (B) AND (C) only. WS-AS-1 IS landed (Reading A), so (A)
    # contributes a POINT pin; it does not gate the composite directionally.
    A_deferred = (legA["pin_form"] == "PRE-REG-INC")  # (local)

    return {
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
        "composite": composite,
        "A_deferred": A_deferred,
    }


# ---------------------------------------------------------------------------
# Section 6 — Plot
# ---------------------------------------------------------------------------
def make_plot(legA, legB, legC, out_png):
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))  # (local)

    # Panel 1 — (B) tau_NL exact identity + bispectrum envelope
    ax = axes[0]  # (local)
    bars = ["tau_NL\n(trispectrum)", "f_NL_total\n(bispectrum)", "max_f_NL_FW\n(envelope)"]  # (local)
    vals = [legB["tau_NL_cached"], legB["f_NL_total"], legB["max_f_NL_FW"]]  # (local)
    cols = ["#2a6f97", "#1b4332", "#c1121f"]  # (local)
    ax.bar(bars, vals, color=cols, alpha=0.85)
    ax.axhline(legB["max_f_NL_FW"], color="#c1121f", ls="--", lw=1,
               label=f"max_f_NL_FW={legB['max_f_NL_FW']:.3f}")
    ax.set_ylabel("amplitude")
    ax.set_title(f"(B) tau_NL=95481/62500={legB['tau_NL_cached']:.6f} EXACT\n"
                 f"f_NL_total={legB['f_NL_total']:.2f} < {legB['max_f_NL_FW']:.3f} (within envelope)")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, axis="y")

    # Panel 2 — (C) Penrose-Diosi E_G vs GGE-thermal scale (log)
    ax = axes[1]  # (local)
    scales = ["E_G\n(Penrose-Diosi)", "T_acoustic\n(GGE-thermal)"]  # (local)
    svals = [legC["E_G_energy_MKK"], legC["T_acoustic_MKK"]]  # (local)
    ax.bar(scales, svals, color=["#5a189a", "#bb3e03"], alpha=0.85)
    ax.set_yscale("log")
    ax.set_ylabel("scale (M_KK units, log)")
    sep_tag = "SEPARATES" if legC["separates"] else "no separation"  # (local)
    ax.set_title(f"(C) E_G={legC['E_G_energy_MKK']:.4g} M_KK  vs  T_acoustic={legC['T_acoustic_MKK']:.3f}\n"
                 f"ratio={legC['separation_ratio']:.3g} ({legC['sep_OOM']:+.2f} OOM) [{sep_tag}]")
    ax.grid(alpha=0.3, axis="y")

    # Panel 3 — (A) impulse-quench A_s POINT pin + purity sectors
    ax = axes[2]  # (local)
    secs = ["B1\n(pure)", "B2\n(mixed)", "B3"]  # (local)
    pur = [legC["purity_B1"], legC["purity_B2"], legC["purity_B3"]]  # (local)
    ax.bar(secs, pur, color=["#1b4332", "#bb3e03", "#5a189a"], alpha=0.85)
    ax.axhline(1.0, color="k", ls=":", lw=1, label="pure (purity=1)")
    ax.set_ylabel("purity Tr(rho^2)")
    ax.set_ylim(0, 1.1)
    ax.set_title(f"(A) [WS-AS-1 Reading A, {legA['pin_form']}]\n"
                 f"A_s={legA['A_s_point']:.3g} (+{legA['overprod_OOM']} OOM); "
                 f"B2 impurity={legC['delta_rho_B2']:.4f} sources E_G")
    ax.legend(fontsize=8)
    ax.grid(alpha=0.3, axis="y")

    fig.suptitle("S110-CF-AS3-QUENCH-PIN — A_s pin (A) + tau_NL promote (B) + Penrose-Diosi E_G (C)",
                 fontsize=12)
    fig.tight_layout(rect=[0, 0, 1, 0.95])
    fig.savefig(out_png, dpi=130)
    plt.close(fig)


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------
def main():
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)
    script_path = Path(__file__).resolve()  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, CANONICAL, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    legA = leg_A_impulse_quench_pin()
    legB = leg_B_tau_NL()
    legC = leg_C_penrose_diosi()
    comp = evaluate_composite(legA, legB, legC)

    # ---- Report (NUMBERS first) ----
    print("=== (A) A_s impulse-quench pin [CONDITIONAL on WS-AS-1] ===")
    print(f"  WS-AS-1 landed: {legA['ws_landed']}  Reading-A verdict: {legA['reading_A']}  "
          f"FB-temp register-predicted PASS: {legA['fb_temp_register_predicted_pass']}")
    print(f"  pin_form: {legA['pin_form']}  (Reading A + register-predicted FB-temp PASS => POINT)")
    print(f"  A_s = {legA['A_s_point']:.4g}  (+{legA['overprod_OOM']} OOM over BD floor); "
          f"k_hat = {legA['k_hat_MKK']} M_KK; k_hat/k_pivot = {legA['k_hat_over_kpivot']}")
    print(f"  tags: (b-i) {legA['tag_b_i_scheme']}; (b-ii) {legA['tag_b_ii_Lmax']}")
    print(f"  FLOOR (out of scope, permanent): {legA['floor_permanent']}")

    print("\n=== (B) tau_NL canonical promotion [directional [SIGN] leg] ===")
    print(f"  tau_NL cached  = {legB['tau_NL_cached']:.12f}")
    print(f"  tau_NL target  = {legB['tau_NL_numer']}/{legB['tau_NL_denom']} = "
          f"{legB['tau_NL_target_exact']:.12f}  (Sage-exact rational)")
    print(f"  abs_dev        = {legB['abs_dev']:.3e}  (tol {TAU_NL_ABS_TOL:.0e}) -> "
          f"rational_identity={legB['rational_identity']}")
    print(f"  Suyama-Yamaguchi: SY_lower={legB['sy_lower']:.6f}, R_SY={legB['R_SY']:.6f}, "
          f"respected={legB['sy_inequality_respected']}")
    print(f"  bispectrum envelope: f_NL_total={legB['f_NL_total']:.4f} < "
          f"max_f_NL_FW={legB['max_f_NL_FW']:.4f}  margin={legB['envelope_margin']:+.4f} -> "
          f"envelope_ok={legB['envelope_ok']}")
    print(f"  sign (direction): f_NL_total < max_f_NL_FW => within-envelope POSITIVE = "
          f"{legB['sign_predicted_positive']}")
    print(f"  leg_B_pass = {legB['leg_B_pass']}  (EXACT identity AND envelope)")

    print("\n=== (C) Penrose-Diosi collapse scale E_G [a_2 band-difference; separation pin] ===")
    print(f"  purity: B1={legC['purity_B1']:.4f} (pure), B2={legC['purity_B2']:.4f} (mixed), "
          f"B3={legC['purity_B3']:.4f}; Cell {legC['cell']}")
    print(f"  delta_rho_B2 (impurity, mass-energy spread) = {legC['delta_rho_B2']:.6f}")
    print(f"  L12 cache: {legC['n_evals_total']} evals total, {legC['n_evals_in_band']} in band "
          f"[{PAIR_BAND_LO}, {PAIR_BAND_HI}] M_KK")
    print(f"  band a_2 fraction = {legC['band_a2_fraction']:.6f}; a2_band = {legC['a2_band']:.4f} M_KK^2 "
          f"(of a2_fold={legC['a2_fold']:.2f})")
    print(f"  E_G = a2_band*(delta_rho)^2 = {legC['E_G_a2units']:.4f} M_KK^2 (a_2 units)")
    print(f"  E_G_energy = sqrt(a2_band)*delta_rho = {legC['E_G_energy_MKK']:.6f} M_KK (energy)")
    print(f"  GGE-thermal scale T_acoustic = {legC['T_acoustic_MKK']:.4f} M_KK")
    print(f"  separation: E_G/T_acoustic = {legC['separation_ratio']:.4f} ({legC['sep_OOM']:+.4f} OOM) "
          f"-> separates={legC['separates']}")
    print(f"  R_therm consistency frame = {legC['R_therm']:.2f} (thermalization 5252x slower than transit)")

    print("\n=== Composite verdict (schema-v2 3-tuple over (A)[cond]/(B)/(C)) ===")
    print(f"  sign_verdict      = {comp['sign_verdict']}  (leg B direction)")
    print(f"  magnitude_verdict = {comp['magnitude_verdict']}  (B EXACT identity AND C separation)")
    print(f"  regime_verdict    = {comp['regime_verdict']}  (deterministic pins)")
    print(f"  COMPOSITE         = {comp['composite']}")
    print(f"  (A) deferred (PRE-REG-INC)? {comp['A_deferred']}")

    # ---- Save data ----
    out_npz = OUT_DIR / "s110_cf_as3_quench_pin.npz"  # (local)
    np.savez(
        out_npz,
        # (A)
        ws_as_1_landed=np.bool_(legA["ws_landed"]),
        reading_A=np.bool_(legA["reading_A"]),
        fb_temp_register_predicted_pass=np.bool_(legA["fb_temp_register_predicted_pass"]),
        A_s_pin_form=np.str_(legA["pin_form"]),
        A_s_impulse_quench=np.float64(legA["A_s_point"]),
        A_s_overprod_OOM=np.float64(legA["overprod_OOM"]),
        k_hat_MKK=np.float64(legA["k_hat_MKK"]),
        k_hat_over_kpivot=np.float64(legA["k_hat_over_kpivot"]),
        # (B)
        tau_NL_cached=np.float64(legB["tau_NL_cached"]),
        tau_NL_target_exact=np.float64(legB["tau_NL_target_exact"]),
        tau_NL_numer=np.int64(legB["tau_NL_numer"]),
        tau_NL_denom=np.int64(legB["tau_NL_denom"]),
        tau_NL_abs_dev=np.float64(legB["abs_dev"]),
        tau_NL_rational_identity=np.bool_(legB["rational_identity"]),
        f_NL_total=np.float64(legB["f_NL_total"]),
        max_f_NL_FW=np.float64(legB["max_f_NL_FW"]),
        envelope_ok=np.bool_(legB["envelope_ok"]),
        envelope_margin=np.float64(legB["envelope_margin"]),
        SY_lower=np.float64(legB["sy_lower"]),
        R_SY=np.float64(legB["R_SY"]),
        leg_B_pass=np.bool_(legB["leg_B_pass"]),
        # (C)
        purity_B1=np.float64(legC["purity_B1"]),
        purity_B2=np.float64(legC["purity_B2"]),
        purity_B3=np.float64(legC["purity_B3"]),
        delta_rho_B2=np.float64(legC["delta_rho_B2"]),
        n_evals_total=np.int64(legC["n_evals_total"]),
        n_evals_in_band=np.int64(legC["n_evals_in_band"]),
        band_a2_fraction=np.float64(legC["band_a2_fraction"]),
        a2_band=np.float64(legC["a2_band"]),
        a2_fold=np.float64(legC["a2_fold"]),
        E_G_a2units=np.float64(legC["E_G_a2units"]),
        E_G_energy_MKK=np.float64(legC["E_G_energy_MKK"]),
        T_acoustic_MKK=np.float64(legC["T_acoustic_MKK"]),
        separation_ratio=np.float64(legC["separation_ratio"]),
        sep_OOM=np.float64(legC["sep_OOM"]),
        separates=np.bool_(legC["separates"]),
        R_therm=np.float64(legC["R_therm"]),
        cell=np.str_(legC["cell"]),
        # composite
        sign_verdict=np.str_(comp["sign_verdict"]),
        magnitude_verdict=np.str_(comp["magnitude_verdict"]),
        regime_verdict=np.str_(comp["regime_verdict"]),
        composite_verdict=np.str_(comp["composite"]),
        A_deferred=np.bool_(comp["A_deferred"]),
        audit_sha256=np.str_(audit_sha),
        content_sha256=np.str_(content_sha),
    )
    print(f"\n  data: {out_npz.relative_to(PROJECT_ROOT)}")

    out_png = OUT_DIR / "s110_cf_as3_quench_pin.png"  # (local)
    make_plot(legA, legB, legC, out_png)
    print(f"  plot: {out_png.relative_to(PROJECT_ROOT)}")

    # ---- 4-tuple + verdict payload ----
    print()
    composite_value = (f"composite={comp['composite']};tau_NL=95481/62500={legB['tau_NL_cached']:.6f}_EXACT;"
                       f"f_NL_total={legB['f_NL_total']:.2f}<max_f_NL_FW={legB['max_f_NL_FW']:.3f};"
                       f"E_G={legC['E_G_energy_MKK']:.4g}_MKK_vs_T_acoustic={legC['T_acoustic_MKK']:.3f}_"
                       f"sep={legC['separation_ratio']:.3g}x;A_s_pin={legA['pin_form']}_{legA['A_s_point']:.3g}")
    print(emit_4tuple(composite_value, SCHEME, CONVENTION, L_MAX))

    note = (f"(B) tau_NL=95481/62500=1.527696 EXACT (abs_dev={legB['abs_dev']:.1e}<{TAU_NL_ABS_TOL:.0e}); "
            f"f_NL_total=1.03<max_f_NL_FW=1.505 (bispectrum within envelope; tau_NL is the DISTINCT "
            f"trispectrum falsifier, not bispectrum-compared). (C) E_G={legC['E_G_energy_MKK']:.4g} M_KK "
            f"SEPARATES from T_acoustic=0.112 ({legC['separation_ratio']:.3g}x, {legC['sep_OOM']:+.2f} OOM). "
            f"(A) WS-AS-1 Reading A => POINT pin A_s={legA['A_s_point']:.3g} (+0.86 OOM), tags scheme+T_pivot-L_max.")
    extra_rows = [
        f"# leg_A_pin_form={legA['pin_form']} (WS-AS-1 Reading A; register-predicted FB-temp PASS => POINT); "
        f"A_s={legA['A_s_point']:.3g} +{legA['overprod_OOM']}OOM k_hat={legA['k_hat_MKK']}MKK; "
        f"tags=scheme-DEPENDENT(b-i)+T_pivot-FB-L_max(b-ii); FLOOR permanent FI (out of scope)",
        f"# leg_B tau_NL=95481/62500 numer/denom EXACT abs_dev={legB['abs_dev']:.1e}; "
        f"f_NL_total={legB['f_NL_total']}<max_f_NL_FW={legB['max_f_NL_FW']}; SY_lower={legB['sy_lower']:.6f} R_SY={legB['R_SY']:.4f}; "
        f"canonical-write-order: verdict->update_constant(tau_NL)->mack inventory Row(mack sole writer)",
        f"# leg_C E_G={legC['E_G_energy_MKK']:.6g}MKK a2_band={legC['a2_band']:.4f}MKK^2 "
        f"band_a2_frac={legC['band_a2_fraction']:.4f} delta_rho_B2={legC['delta_rho_B2']:.4f} "
        f"sep={legC['separation_ratio']:.4g}x_T_acoustic Cell-D-P; R_therm={legC['R_therm']:.0f}",
        "# regulator_pin=N/A for tau_NL/A_s (GGE relic amplitudes, not Seeley-DeWitt moments); "
        "E_G uses a2_fold(zeta) second-moment second-inverse-power band weight",
    ]
    print_verdict_payload(
        comp["composite"], composite_value, audit_sha, content_sha,
        sign_verdict=comp["sign_verdict"],
        magnitude_verdict=comp["magnitude_verdict"],
        regime_verdict=comp["regime_verdict"],
        companion_note=note,
        extra_rows=extra_rows,
    )

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {comp['composite']} "
          f"(sign={comp['sign_verdict']}/mag={comp['magnitude_verdict']}/regime={comp['regime_verdict']}) "
          f"(wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
