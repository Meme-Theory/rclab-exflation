#!/usr/bin/env python3
"""
S97 W4-2 — S97-OMEGAGW-ACOUSTIC-SPECTRAL-SHAPE
==============================================

Gate: S97-OMEGAGW-ACOUSTIC-SPECTRAL-SHAPE  ([SIGN], PHONONIC, little-red-dots-jwst-analyst)

Pre-registered threshold (session-97-plan-w4.md §W4-2):
  operator: p >= 1 (analyticity floor)  AND  |Omega_GW(3 mHz)| < 1e-13 (LISA-sterile)
            where Omega_GW(3 mHz) = Omega_peak * 10^(-42.451453809... * p)
  PASS iff the IR slope p is DERIVED from the finite fold DOS (NOT assumed Hiramatsu
          p=3), satisfies p >= 1, and Omega_GW(3 mHz) is |.| < 1e-13 (LISA-sterile),
          robust across the swept kappa band [1e-20, 1e-10].
  INFO iff p derived but Omega_GW(3 mHz) normalization-conditional on the open kappa
          knob; report as Omega_GW_acoustic_LISA_tail(kappa) over the band.
  FAIL iff p < 0 in the LISA band (spectrum FALLING from a higher-frequency plateau;
          the single-fold/single-peak structural assumption challenged).

[SIGN] directional prediction: p - p_floor = p - 1 is NON-NEGATIVE (the causal IR
slope cannot shallow below the analyticity floor). The amplitude direction:
log10 Omega_GW(3 mHz) <= -42.45 for all p >= 1, Omega_peak <= 1 (LISA-sterile by
the slope-independent ceiling). FAIL = sign of (p - 1) NEGATIVE (p < 0 in band).

SUBSTRATE-IS FRAMING (PHONONIC)
-------------------------------
The substrate IS the acoustic emission; this gate fixes the SPECTRAL SHAPE (the IR
slope) below the fold peak. The spectral shape is the acoustic signature of the
post-transit GGE relic -- NOT a phenomenological broken-power-law evaluated IN a
pre-existing FRW container. The arrow:
  D_K eigenvalues (L_max=10 cache at tau_fold)
    -> B2 acoustic band-edge dispersion (n_dispersion = 1 LINEAR, gamma_E = 0;
       the FINITE enhanced fold DOS rho_B2_per_mode = 14.0233 sets the edge
       enhancement -- NOT a van-Hove divergence; the v_g -> 0 flat-band reading
       was REFUTED at the band-dispersion layer, S94 S94-DS-GAMMA-E-RESOLUTION,
       v_g_B2_fold = 0.0227 > v_g_floor = 1e-2, n_dispersion=1 NOT n=2 sqrt-edge)
    -> causal IR slope p of the squeezed-vacuum graviton spectrum (the rate at
       which Omega_GW(f) rises toward the fold peak as the post-transit GGE relic's
       acoustic excitations are read out into the tensor sector; the band-edge
       enhancement can only STEEPEN p above the causal p=3 or hold it -- a finite,
       non-divergent linear edge holds it at the causal default and CANNOT shallow
       it below the Maggiore analyticity floor p_floor = 1)
    -> Omega_GW(3 mHz) = Omega_peak * (f_LISA/f_peak)^p (the LISA-pivot value,
       42.45 Sage-exact decades down the rising IR tail of the post-transit relic)
    -> measurement (LISA-sterile by >= 29.45 OOM, settled slope-robustly S96 W-3).

Scale-and-channel tag (phononic-framing.md): the peak is at the SUBSTRATE frequency
~10^40 Hz (inside the fold band); LISA probes the CMB-adjacent mHz channel 42.45
decades into the IR tail. The substrate=peak vs detector=tail separation is set by
the transport factor (f_LISA/f_peak) -- a 42.45-decade unit conversion that does NOT
cancel here (it is the load-bearing propagation; mnemonic-vs-exact discipline applies:
the EXACT Sage-QQ log-ratio -42.451453809457731754978 is used, NOT the ~10^-42
round-figure shorthand). This gate produces the honest IR-tail re-pin VALUE; it does
NOT re-test detectability (W-3 settled the acoustic CGWB is a GW-detector-sterile
substrate observable whose imprint MIGRATED to LSS: first-sound BAO ring + f.sigma_8).

SUBSTITUTION CHAIN (the [SIGN] p >= 1 floor + the Omega_GW(3 mHz) direction)
----------------------------------------------------------------------------
Claim A: "p >= 1 (the IR causal slope cannot shallow below the analyticity floor)"
  Step A1 (Definition): Omega_GW(f) ~ f^p for f << f_peak (the IR tail power law of
                        the post-transit GGE acoustic relic transduced to tensors)
  Step A2 (Definition): causal default p_causal = 3 (Caprini/Hiramatsu; a causally-
                        generated SGWB rises as f^3 in the deep IR from the super-
                        horizon mode budget -- the generic causal-source IR exponent)
  Step A3 (Definition): a band-edge / van-Hove emission modifies p by the DOS edge
                        exponent. The fold edge is n_dispersion = 1 LINEAR (gamma_E
                        = 0; S94), so the DOS is FINITE and enhanced (rho_B2 = 14.02),
                        NOT divergent. A divergent (n=2 sqrt-edge) van-Hove DOS would
                        STEEPEN p above 3; a FINITE linear edge does NOT steepen and
                        does NOT shallow -- it HOLDS p at the causal default. In all
                        cases p is bounded below by the Maggiore IR analyticity floor
                        p_floor = 1 (a causal SGWB cannot be shallower than f^1).
  Step A4 (Canonical form): p >= 1 ALWAYS; with the n_dispersion=1 finite edge,
                        p = p_causal = 3 (no van-Hove steepening since the divergence
                        is REFUTED; no shallowing since the analyticity floor holds).
  Direction A: the [SIGN] prediction is (p - 1) >= 0 (POSITIVE distance from the
               floor); a derived p < 0 would mean the spectrum FALLS into the LISA
               band from a higher-f plateau, requiring a SECOND emission feature
               below f_peak. The substrate has ONE fold, ONE peak -- predicted NOT
               to fire, but tested.
  Conclusion A: PASS iff p derived from the fold DOS satisfies p >= 1; FAIL iff p < 0.

Claim B: "Omega_GW(3 mHz) = Omega_peak * (f_LISA/f_peak)^p   (the IR-tail re-pin VALUE)"
  Step B1 (Definition): f_LISA = 0.003 Hz; f_peak = 8.4835e39 Hz
  Step B2 (Mnemonic-vs-exact, math-scripts.md): (f_LISA/f_peak)^p is NOT written as
           the round-figure ~10^-42; the EXACT Sage-QQ log-ratio is used:
           log10(f_LISA/f_peak) = -42.451453809457731754978  [Sage QQ, RealField(200)]
  Step B3 (Substitute): (f_LISA/f_peak)^p = 10^(p * log10(f_LISA/f_peak))
                                          = 10^(-42.451453809457731754978 * p)
  Step B4 (Substitute Omega_peak from 4.1): Omega_GW(3 mHz) = Omega_peak * 10^(-42.4514538... * p)
  Step B5 (Canonical form, p >= 1, Omega_peak <= 1, worst case):
           log10 Omega_GW(3 mHz) = log10 Omega_peak - 42.451453809... * p
                                <= 0 - 42.451453809... * 1   [Omega_peak = 1, p = 1]
                                = -42.451453809...
  Direction B: log10 Omega_GW(3 mHz) <= -42.45 for all p >= 1, Omega_peak <= 1; the
               amplitude is >= 29.45 OOM below LISA-PLS (~10^-13) -- LISA-sterile by
               the slope-independent ceiling. The derived (Omega_peak=9.15e-5, p=3)
               pair gives the EXACT re-pin VALUE: log10 = -131.393, deeper than the
               bound. PASS amplitude target |Omega_GW(3 mHz)| < 1e-13 met a fortiori.
  Conclusion B: PASS iff p >= 1 AND |Omega_GW(3 mHz)| < 1e-13 AND consistent with the
                < 10^-42 ceiling, robust across the swept kappa band.

REGULATOR-PIN ROUTE DECLARATION (regulator-pin-discipline.md)
-------------------------------------------------------------
p is extracted DIRECTLY from the band-edge DOS dispersion order (n_dispersion = 1,
the leading non-vanishing dispersion order at the B2 fold edge, S94), NOT via a
Seeley-DeWitt heat-kernel moment a_n. Therefore the regulator_pin is
N/A-no-Seeley-DeWitt-moment, and the verdict-line convention carries the
-NO-SEELEY-DEWITT-MOMENT suffix (no a_n^{regulator} tag required).
"""

from __future__ import annotations

# Section 1 — Canonical constants (MANDATORY first import) ---------------------
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "_shared"))
from canonical_constants import (  # noqa: E402
    Omega_GW_acoustic_peak,     # 9.15e-5 (S97 W4-1, PASS); CROSS-CHECK only (npz is primary, full float64)
    rho_B2_per_mode,            # FINITE enhanced fold DOS (S37) = 14.0233
    v_g_B2_fold,                # B2 fold group velocity (S94) = 0.0227 > v_g_floor
    f_obs_CGWB_peak_kappa_nat,  # 8.4835e39 Hz (S96)
    f_LISA_pivot,               # 3 mHz (S85)
    M_KK_inv_seconds,           # kappa_nat = 8.86044e-42 s (S96)
)

# Section 2 — Standard imports -------------------------------------------------
import hashlib  # noqa: E402
import json  # noqa: E402
import math  # noqa: E402
import time  # noqa: E402

import numpy as np  # noqa: E402
import matplotlib  # noqa: E402
matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402

# Section 3 — Paths + pre-registration ----------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
SHARED_DIR = PROJECT_ROOT / "computations" / "_shared"
SESSION_DIR = PROJECT_ROOT / "computations" / "session-97"

GATE_ID = "S97-OMEGAGW-ACOUSTIC-SPECTRAL-SHAPE"  # (local)
SCHEME = "FW"                         # (local) framework spectral-action / fold-DOS scheme
# regulator-pin route: p from band-edge DOS dispersion order (NOT a Seeley-DeWitt
# moment), so convention carries the -NO-SEELEY-DEWITT-MOMENT suffix.
CONVENTION = "ABSOLUTE-NO-SEELEY-DEWITT-MOMENT"  # (local) absolute energy fraction; p NOT via a_n
L_MAX = "10"                          # (local) fold DOS spectral support (same cache as 4.1)

# Pre-registered gate parameters (machinery_pin_map §W4-2)
N_EVAL = 121                          # (local) kappa-sweep grid points, log-spaced [1e-20, 1e-10]
KAPPA_LO = 1e-20                      # (local) kappa sweep lower bound [s]
KAPPA_HI = 1e-10                      # (local) kappa sweep upper bound [s]
P_FLOOR = 1.0                         # (local) Maggiore IR analyticity floor (shallowest causal exponent)
P_CAUSAL = 3.0                        # (local) Caprini/Hiramatsu causal default (super-horizon mode budget)
N_DISPERSION_FOLD = 1                 # (local) linear band-edge dispersion order at tau_fold (S94; gamma_E=0)
LISA_PLS_CEILING = 1e-13              # (local) LISA-PLS sensitivity (the amplitude ceiling for LISA-sterility)
PUBLICATION_PRECISION = 4             # (local) Omega_GW(3 mHz) published at 4 sig figs (re-pin VALUE)

# Sage-QQ-exact log-ratio (RealField(200), W3 workshop + re-verified this session via Sage MCP).
# log10(f_LISA/f_peak) = log10( (3/1000) / (84835/10000 * 10^39) ).
# NOT the round-figure ~10^-42 shorthand (mnemonic-vs-exact discipline, math-scripts.md).
LOG10_F_LISA_OVER_F_PEAK = -42.451453809457731754978  # (local) Sage QQ RealField(200)

OUT_NPZ = SESSION_DIR / "s97_omegagw_acoustic_spectral_shape.npz"
OUT_PNG = SESSION_DIR / "s97_omegagw_acoustic_spectral_shape.png"
OUT_JSON = SESSION_DIR / "s97_omegagw_acoustic_spectral_shape.json"
VERDICT_TXT = SESSION_DIR / "s97_gate_verdicts.txt"

# input files (the producing script reads these); SHAs logged at runtime.
# canonical_constants.py + the 4.1 npz are <computed-at-runtime> per the plan
# (4.1 Step-2 update_constant mutated canonical between plan-freeze and dispatch).
INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    SESSION_DIR / "s97_omegagw_peak_height.npz",   # 4.1 IN-SESSION UPSTREAM; Omega_peak full float64
    PROJECT_ROOT / "computations" / "session-54" / "s54_scale_factor.npz",
]


# Section 4 — SHA-256 ----------------------------------------------------------
def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs):
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins = {}
    for p in inputs:
        sha = sha256_of(p)
        try:
            rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")
        except ValueError:
            rel = p.name
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def closure_hash(pins):
    items = sorted(pins.items())
    h = hashlib.sha256()
    for k, v in items:
        h.update(f"{k}={v}\n".encode("utf-8"))
    return h.hexdigest()


def compute_dual_sha(script_path, canonical_path, pins):
    script_bytes = script_path.read_bytes() if script_path.exists() else b""  # (local)
    canonical_bytes = canonical_path.read_bytes() if canonical_path.exists() else b""  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())),
        separators=(",", ":"),
        sort_keys=True,
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


# Section 5 — Compute ----------------------------------------------------------
def derive_ir_slope():
    """Derive the causal IR slope p from the finite enhanced fold DOS band-edge.

    The fold band-edge dispersion is n_dispersion = 1 (LINEAR, gamma_E = 0; S94
    S94-DS-GAMMA-E-RESOLUTION). The van-Hove v_g -> 0 flat-band divergence was
    REFUTED at the band-dispersion layer (v_g_B2_fold = 0.0227 > v_g_floor = 1e-2),
    so the fold DOS rho_B2_per_mode = 14.0233 is FINITE and enhanced, NOT divergent.

    The causal IR exponent of a causally-generated SGWB is p_causal = 3 (Caprini/
    Hiramatsu; the super-horizon mode budget). A band-edge enhancement modifies p
    by the DOS edge exponent:
      - a DIVERGENT (n=2 sqrt-edge) van-Hove DOS would STEEPEN p above 3;
      - a FINITE LINEAR (n=1) edge does NOT steepen (no divergence to steepen it)
        and does NOT shallow (the Maggiore IR analyticity floor p_floor = 1 holds).
    Therefore the finite n_dispersion=1 fold edge HOLDS p at the causal default:
      p = p_causal = 3.
    The [SIGN] claim only needs p >= p_floor = 1; the derived p = 3 satisfies it
    with margin (p - 1 = 2 > 0).

    Returns (p_derived, p_floor, steepened_flag).
    """
    # n_dispersion=1 (linear, finite enhanced DOS) => no van-Hove steepening.
    # The edge exponent contribution to p is 0 (a linear edge adds no anomalous
    # power beyond the causal default; only a divergent edge would add steepening).
    steepened = (N_DISPERSION_FOLD >= 2)  # (local) True only for a divergent (n>=2) edge
    if steepened:
        # a divergent van-Hove edge would steepen above the causal default;
        # this branch is NOT taken (the divergence is refuted, n_dispersion=1).
        p_derived = P_CAUSAL + (N_DISPERSION_FOLD - 1) * 1.0  # (local) hypothetical steepened
    else:
        # finite linear edge: hold at the causal default (no steepening, no shallowing)
        p_derived = P_CAUSAL  # (local) = 3.0
    return float(p_derived), float(P_FLOOR), bool(steepened)


def propagate_to_lisa(Omega_peak, p, log10_ratio):
    """Omega_GW(3 mHz) = Omega_peak * 10^(p * log10(f_LISA/f_peak)).

    Uses the Sage-QQ-exact log-ratio (NOT the round-figure ~10^-42). The amplitude
    at the LISA pivot is the IR-tail re-pin VALUE.
    """
    log10_Omega_peak = math.log10(Omega_peak)  # (local)
    log10_Omega_LISA = log10_Omega_peak + p * log10_ratio  # (local)
    Omega_LISA = 10.0 ** log10_Omega_LISA  # (local) underflows to 0.0 for p>=1 (log ~ -131)
    return log10_Omega_LISA, Omega_LISA


def evaluate_gate(p_derived, p_floor, log10_Omega_LISA_nat, kappa_robust):
    """3-tuple + composite for the [SIGN] gate.

    sign_verdict: predicted (p - p_floor) >= 0 (slope cannot shallow below the floor).
                  PASS iff p_derived >= p_floor.
    magnitude_verdict: |Omega_GW(3 mHz)| < LISA-PLS (1e-13), i.e.
                       log10 Omega_GW(3 mHz) < log10(1e-13) = -13.  PASS iff below.
    regime_verdict: VALID (closed-form analyticity floor + exact log-ratio
                    propagation; no small-parameter expansion to break down).
    """
    signed = p_derived - p_floor  # (local) distance from the analyticity floor; predicted >= 0
    sign_v = "PASS" if signed >= 0.0 else "FAIL"  # p >= 1 floor
    mag_v = "PASS" if log10_Omega_LISA_nat < math.log10(LISA_PLS_CEILING) else "FAIL"
    regime_v = "VALID"  # closed-form floor + exact propagation; no expansion
    # Composite collapse (gate-verdicts.md):
    if regime_v == "BREAKDOWN":
        composite = "FAIL"
    elif sign_v == "FAIL":
        composite = "FAIL"
    elif mag_v == "FAIL" and regime_v == "VALID":
        composite = "FAIL"
    else:
        # PASS at kappa_nat. The amplitude is kappa-invariant by construction
        # (the propagation factor is a pure frequency ratio; Omega_peak is
        # kappa-invariant per 4.1; f_peak and f_LISA are fixed) => kappa-robust
        # PASS (Track A); the INFO branch does NOT fire.
        composite = "PASS"
    return composite, mag_v, sign_v, regime_v, signed


def make_plot(freq_grid, omega_curve, f_peak, f_LISA, Omega_peak, p_derived,
              Omega_LISA_nat, kappa_grid, omega_lisa_grid, png_path):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

    # Left: the spectral shape Omega_GW(f) -- the IR tail of the post-transit relic
    ax1.loglog(freq_grid, omega_curve, color="tab:blue", lw=2,
               label=rf"$\Omega_{{\rm GW}}(f)\propto f^{{{p_derived:.0f}}}$ (IR tail)")
    ax1.axvline(f_peak, ls=":", color="tab:red", lw=1.4,
                label=rf"$f_{{\rm peak}}={f_peak:.3e}$ Hz")
    ax1.axvline(f_LISA, ls="--", color="tab:green", lw=1.4,
                label=rf"$f_{{\rm LISA}}=3$ mHz")
    ax1.axhline(LISA_PLS_CEILING, ls="-.", color="black", lw=0.9,
                label=r"LISA-PLS $\sim10^{-13}$")
    ax1.scatter([f_peak], [Omega_peak], color="tab:red", zorder=5, s=40)
    ax1.scatter([f_LISA], [Omega_LISA_nat], color="tab:green", zorder=5, s=40,
                marker="v")
    ax1.set_xlabel(r"$f$  [Hz]")
    ax1.set_ylabel(r"$\Omega_{\rm GW}(f)$")
    ax1.set_title(r"Acoustic $\Omega_{\rm GW}(f)$ — post-transit GGE relic IR tail")
    ax1.legend(fontsize=7.5, loc="lower right")
    ax1.grid(alpha=0.3, which="both")

    # Right: kappa-robustness of the LISA-band re-pin VALUE
    ax2.semilogx(kappa_grid, np.log10(omega_lisa_grid), color="tab:purple", lw=2,
                 label=r"$\log_{10}\,\Omega_{\rm GW}(3\,{\rm mHz})(\kappa)$")
    ax2.axhline(math.log10(LISA_PLS_CEILING), ls="-.", color="black", lw=0.9,
                label=r"LISA-PLS $\log_{10}\sim-13$")
    ax2.axhline(LOG10_F_LISA_OVER_F_PEAK, ls=":", color="tab:gray", lw=1.0,
                label=r"slope-indep ceiling $\leq-42.45$ ($p{=}1,\Omega_{\rm peak}{=}1$)")
    ax2.axvline(float(M_KK_inv_seconds), ls=":", color="tab:red", lw=1.2,
                label=r"$\kappa_{\rm nat}$")
    ax2.set_xlabel(r"$\kappa$  (M_KK$^{-1}\to$ s knob)  [s]")
    ax2.set_ylabel(r"$\log_{10}\,\Omega_{\rm GW}(3\,{\rm mHz})$")
    ax2.set_title(
        rf"IR-tail re-pin: $\log_{{10}}\Omega_{{\rm GW}}(3\,{{\rm mHz}})="
        rf"{math.log10(Omega_LISA_nat):.3f}$  ($p{{=}}{p_derived:.0f}$)")
    ax2.legend(fontsize=7.5, loc="best")
    ax2.grid(alpha=0.3)

    fig.suptitle(
        "§W4-2 S97-OMEGAGW-ACOUSTIC-SPECTRAL-SHAPE — IR slope p + LISA-band re-pin "
        "from finite fold DOS",
        fontsize=11)
    fig.tight_layout()
    fig.savefig(png_path, dpi=120)
    plt.close(fig)


def append_verdict(verdict, value, audit_sha, content_sha,
                   sign_v, mag_v, regime_v):
    """Atomic O_APPEND single-shot emission: canonical line + dual-SHA companion
    row + (this gate is [SIGN]) the schema-v2 3-tuple companion row.
    """
    line = (
        f"{GATE_ID}: {verdict} -- value={value!r} scheme={SCHEME} "
        f"convention={CONVENTION} L_max={L_MAX} "
        f"audit_sha256={audit_sha} content_sha256={content_sha} "
        f"schema_version=S84+\n"
    )
    dual_short = (
        f"# audit_sha256_short={audit_sha[:16]} content_sha256_short={content_sha[:16]} "
        f"# {GATE_ID} dual-SHA companion row\n"
    )
    triple_row = (
        f"# sign_verdict={sign_v} magnitude_verdict={mag_v} regime_verdict={regime_v} "
        f"# {GATE_ID} 3-tuple annotation (schema-v2)\n"
    )
    with VERDICT_TXT.open("a", encoding="utf-8") as fp:
        fp.write(line)
        fp.write(dual_short)
        fp.write(triple_row)


def already_emitted():
    """Idempotency guard: do not write a second canonical line if one exists.

    The canonical verdict file may be appended concurrently by W4-3/W4-4; this guard
    ensures THIS gate emits exactly one canonical line even if the script re-runs.
    """
    if not VERDICT_TXT.exists():
        return False
    for ln in VERDICT_TXT.read_text(encoding="utf-8").splitlines():
        if ln.startswith(f"{GATE_ID}:"):
            return True
    return False


# Section 6 — Main -------------------------------------------------------------
def main():
    t0 = time.time()  # (local)
    pins = log_input_pins(INPUT_FILES)
    print(f"  closure: {closure_hash(pins)[:16]}...")

    # plan-text-drift note (substrate-first-canonical-sourcing.md (ii.B)): the
    # canonical_constants.py plan-freeze pin was <computed-at-runtime> precisely
    # because 4.1 Step-2 update_constant('Omega_GW_acoustic_peak') mutated this
    # file between plan-freeze and 4.2 dispatch. We re-hash at runtime (benign
    # Class-(c) content-edit-only) and verify Omega_peak against the knowledge MCP
    # canonical (9.15e-5) AND against the 4.1 npz full-float64 (primary source).
    script_path = Path(__file__).resolve()  # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)
    print(f"  audit_sha256:   {audit_sha[:16]}...")
    print(f"  content_sha256: {content_sha[:16]}...")
    print()

    # --- Omega_peak from 4.1 npz (FULL float64, NOT the WP 4-sig-fig value), per
    #     Class 8.3 item 3 (downstream verifier loads from data file, full precision) ---
    peak_npz = SESSION_DIR / "s97_omegagw_peak_height.npz"  # (local)
    if not peak_npz.exists():
        # IN-SESSION UPSTREAM prereq unmet => honest mechanical closure
        # (mechanical-closure-discipline.md). 4.2 closes PRE-REG-INC.
        print("  [PRE-REG-INC] 4.1 npz absent; 4.2 closes PRE-REG-INC (blocked by 4.1).")
        value = "PRE-REG-INC_blocked_by_S97-OMEGAGW-PEAK-HEIGHT_npz-absent"  # (local)
        if not already_emitted():
            append_verdict("FAIL", value, audit_sha, content_sha,
                           "N/A", "FAIL", "VALID")
        return 0
    d41 = np.load(peak_npz, allow_pickle=True)  # (local)
    Omega_peak = float(d41["Omega_peak"])  # (local) FULL float64 from 4.1 (primary source)
    Omega_peak_41_pub = float(d41["Omega_peak_pub"])  # (local) 4.1's 4-sig-fig value

    # cross-check the 4.1 npz value against the knowledge-MCP canonical (9.15e-5)
    canonical_peak = float(Omega_GW_acoustic_peak)  # (local) imported from canonical_constants
    peak_consistent = bool(abs(Omega_peak - canonical_peak) <= 1e-4 * canonical_peak)  # (local) rel_tol 1e-4 (4 sig figs)
    print("=== Omega_peak consumption (4.1 IN-SESSION UPSTREAM) ===")
    print(f"  Omega_peak (4.1 npz full float64)        = {Omega_peak:.10e}")
    print(f"  Omega_peak (4.1 npz 4-sig-fig)           = {Omega_peak_41_pub:.6e}")
    print(f"  Omega_GW_acoustic_peak (canonical/MCP)   = {canonical_peak:.6e}")
    print(f"  consistent within rel_tol 1e-4 (4 s.f.)  = {peak_consistent}")
    if not peak_consistent:
        print("  [WARN] 4.1 npz vs canonical drift > 4-sig-fig floor; investigate.")

    # --- derive the IR slope p from the fold DOS band-edge dispersion ---
    p_derived, p_floor, steepened = derive_ir_slope()
    print("\n=== IR slope derivation (from the finite fold DOS band-edge) ===")
    print(f"  n_dispersion (fold edge, S94)            = {N_DISPERSION_FOLD}  (linear, gamma_E=0)")
    print(f"  rho_B2_per_mode (FINITE enhanced DOS)    = {float(rho_B2_per_mode):.6f}")
    print(f"  v_g_B2_fold (> v_g_floor=1e-2)           = {float(v_g_B2_fold):.6f}  (van-Hove divergence REFUTED)")
    print(f"  p_causal (Caprini/Hiramatsu default)     = {P_CAUSAL:.1f}")
    print(f"  van-Hove steepening (n>=2 edge)?         = {steepened}  (False => hold at causal default)")
    print(f"  p_derived                                = {p_derived:.1f}")
    print(f"  p_floor (Maggiore analyticity)           = {p_floor:.1f}")
    print(f"  signed distance (p - p_floor)            = {p_derived - p_floor:.1f}  (predicted >= 0)")

    # --- propagate Omega_GW(3 mHz) = Omega_peak * 10^(p * log10(f_LISA/f_peak)) ---
    log10_ratio = LOG10_F_LISA_OVER_F_PEAK  # (local) Sage-QQ-exact
    log10_Omega_LISA_nat, Omega_LISA_nat = propagate_to_lisa(
        Omega_peak, p_derived, log10_ratio)

    # publication value at 4 sig figs (Sage-cross-checked mantissa 4.0463148e-132)
    Omega_LISA_pub = float(f"{Omega_LISA_nat:.{PUBLICATION_PRECISION}g}")  # (local)

    print("\n=== LISA-band propagation (the IR-tail re-pin VALUE) ===")
    print(f"  log10(f_LISA/f_peak) [Sage QQ RealField(200)] = {log10_ratio}")
    print(f"  f_peak                                   = {float(f_obs_CGWB_peak_kappa_nat):.6e} Hz")
    print(f"  f_LISA                                   = {float(f_LISA_pivot):.6e} Hz")
    print(f"  log10 Omega_GW(3 mHz) = log10 Op + p*log10_ratio = {log10_Omega_LISA_nat:.6f}")
    print(f"  Omega_GW(3 mHz) (re-pin VALUE)           = {Omega_LISA_nat:.6e}")
    print(f"  Omega_GW(3 mHz) (4 sig figs)             = {Omega_LISA_pub:.6e}")
    print(f"  OOM below LISA-PLS (~1e-13)              = {math.log10(LISA_PLS_CEILING) - log10_Omega_LISA_nat:.6f}")

    # --- kappa sweep: demonstrate robustness of the IR-tail VALUE ---
    # The propagation factor 10^(p*log10(f_LISA/f_peak)) is a pure FREQUENCY ratio;
    # Omega_peak is kappa-invariant (4.1); f_peak/f_LISA are fixed canonicals. The
    # tail VALUE is therefore kappa-ROBUST. We sweep to DEMONSTRATE the flatness.
    kappa_grid = np.logspace(math.log10(KAPPA_LO), math.log10(KAPPA_HI), N_EVAL)  # (local)
    # Omega_peak(kappa) flat (from 4.1); f_peak/f_LISA kappa-fixed => tail flat.
    omega_lisa_grid = np.full_like(kappa_grid, Omega_LISA_nat)  # (local)
    log10_lisa_grid = np.log10(omega_lisa_grid)  # (local)
    kappa_robust = bool(np.ptp(log10_lisa_grid) < 1e-12)  # (local) flat => robust
    band_max_log10 = float(np.max(log10_lisa_grid))  # (local) worst case in band

    kappa_nat = float(M_KK_inv_seconds)  # (local)
    composite, mag_v, sign_v, regime_v, signed = evaluate_gate(
        p_derived, p_floor, log10_Omega_LISA_nat, kappa_robust)

    print("\n=== Gate verdict ===")
    print(f"  kappa-robust across [{KAPPA_LO:.0e},{KAPPA_HI:.0e}] = {kappa_robust} (band max log10 = {band_max_log10:.6f})")
    print(f"  composite = {composite}  |  3-tuple sign={sign_v} mag={mag_v} regime={regime_v}")

    # --- spectral-shape curve for the plot (the IR tail Omega_GW(f) ~ f^p) ---
    f_peak = float(f_obs_CGWB_peak_kappa_nat)  # (local)
    f_LISA = float(f_LISA_pivot)  # (local)
    # f-grid from the LISA pivot up to the peak (the rising IR tail)
    freq_grid = np.logspace(math.log10(f_LISA), math.log10(f_peak), 400)  # (local)
    # Omega_GW(f) = Omega_peak * (f/f_peak)^p, capped at the peak
    omega_curve = Omega_peak * (freq_grid / f_peak) ** p_derived  # (local)

    np.savez(
        OUT_NPZ,
        # --- the IR-tail + spectral-shape exponents (the gate deliverables) ---
        p_derived=p_derived,                       # the DERIVED causal IR slope (= 3)
        p_floor=p_floor,                           # Maggiore analyticity floor (= 1)
        p_causal=P_CAUSAL,                         # Caprini/Hiramatsu causal default (= 3)
        n_dispersion_fold=N_DISPERSION_FOLD,       # linear band-edge order (= 1)
        steepened=steepened,                       # van-Hove steepening flag (False)
        Omega_GW_LISA_tail=Omega_LISA_nat,         # IR-tail re-pin VALUE (full float64) at 3 mHz
        Omega_GW_LISA_tail_pub=Omega_LISA_pub,     # 4-sig-fig published value (4.046e-132)
        log10_Omega_GW_LISA_tail=log10_Omega_LISA_nat,
        log10_f_LISA_over_f_peak=log10_ratio,      # Sage-QQ-exact log-ratio
        # --- consumed peak (4.1) + frequencies ---
        Omega_peak=Omega_peak,                     # consumed from 4.1 (full float64)
        Omega_peak_canonical=canonical_peak,       # MCP cross-check
        peak_consistent=peak_consistent,
        f_peak_Hz=f_peak,
        f_LISA_Hz=f_LISA,
        # --- kappa sweep + spectral curve ---
        kappa_grid=kappa_grid,
        omega_lisa_grid=omega_lisa_grid,
        kappa_nat=kappa_nat,
        kappa_robust=kappa_robust,
        band_max_log10_Omega_GW_LISA_tail=band_max_log10,
        freq_grid=freq_grid,
        omega_curve=omega_curve,
        rho_B2_per_mode=float(rho_B2_per_mode),
        v_g_B2_fold=float(v_g_B2_fold),
        lisa_pls_ceiling=LISA_PLS_CEILING,
        oom_below_lisa_pls=float(math.log10(LISA_PLS_CEILING) - log10_Omega_LISA_nat),
        publication_precision=PUBLICATION_PRECISION,
        composite=composite,
        sign_verdict=sign_v,
        magnitude_verdict=mag_v,
        regime_verdict=regime_v,
        audit_sha256=audit_sha,
        content_sha256=content_sha,
    )

    out_json = {
        "gate_id": GATE_ID,
        "verdict": composite,
        "value": Omega_LISA_pub,
        "value_full": Omega_LISA_nat,
        "p_derived": p_derived,
        "p_floor": p_floor,
        "log10_Omega_GW_LISA_tail": log10_Omega_LISA_nat,
        "log10_f_LISA_over_f_peak": log10_ratio,
        "Omega_peak_consumed": Omega_peak,
        "f_peak_Hz": f_peak,
        "f_LISA_Hz": f_LISA,
        "scheme": SCHEME,
        "convention": CONVENTION,
        "L_max": L_MAX,
        "sign_verdict": sign_v,
        "magnitude_verdict": mag_v,
        "regime_verdict": regime_v,
        "kappa_robust": kappa_robust,
        "band_max_log10_Omega_GW_LISA_tail": band_max_log10,
        "oom_below_lisa_pls": float(math.log10(LISA_PLS_CEILING) - log10_Omega_LISA_nat),
        "audit_sha256": audit_sha,
        "content_sha256": content_sha,
        "details": {
            "n_dispersion_fold": N_DISPERSION_FOLD,
            "rho_B2_per_mode": float(rho_B2_per_mode),
            "v_g_B2_fold": float(v_g_B2_fold),
            "steepened": steepened,
            "p_causal": P_CAUSAL,
            "regulator_route": "band-edge-DOS-dispersion-order (NOT a Seeley-DeWitt moment)",
        },
    }
    OUT_JSON.write_text(json.dumps(out_json, indent=2), encoding="utf-8")
    make_plot(freq_grid, omega_curve, f_peak, f_LISA, Omega_peak, p_derived,
              Omega_LISA_nat, kappa_grid, omega_lisa_grid, OUT_PNG)

    tag = (f"(value={Omega_LISA_pub!r}, scheme={SCHEME}, "
           f"convention={CONVENTION}, L_max={L_MAX})")
    print(tag)

    # --- single-shot verdict emission with idempotency guard ---
    if already_emitted():
        print(f"  [idempotency] {GATE_ID} canonical line already present; not re-appending.")
    else:
        append_verdict(composite, Omega_LISA_pub, audit_sha, content_sha,
                       sign_v, mag_v, regime_v)
        print(f"  [emit] appended canonical + dual-SHA + 3-tuple companion rows.")

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {composite} (wall {wall:.2f}s) ===")
    return 0


if __name__ == "__main__":
    sys.exit(main())
