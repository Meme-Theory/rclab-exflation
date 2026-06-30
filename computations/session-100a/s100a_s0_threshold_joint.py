#!/usr/bin/env python3
"""
S100a W3-11 S100a-S0-THRESHOLD-JOINT — is S0 fixed by the KK-threshold machinery?
==================================================================================

Gate: S100a-S0-THRESHOLD-JOINT ([SIGN])
Classification: GEOMETRIC (KK-threshold fixing of the envelope magnitude)
Agent: phonon-first-cosmologist

Pre-registered three-band threshold (plan sessions/session-plan/session-100a-plan-w3.md
SectionW3-11 operator, RATIO convention):
    ratio_dev = |S0_threshold / S0_fit - 1|
    PASS iff ratio_dev <= 0.05          (S0 threshold-FIXED, no free normalization;
                                         envelope magnitude+slope close JOINTLY)
    INFO iff 0.05 < ratio_dev <= 0.5    (threshold-constrained to O(1) with a
                                         1-parameter residual knob)
    FAIL iff ratio_dev > 0.5            (S0 independent of threshold; scale stays an
                                         empirical anchor, the S99 W3-2 neutrino pattern)

Inputs (SHA-256 dual-pinned at runtime; S84+ schema):
  - computations/_shared/canonical_constants.py      (T_acoustic, m_H_FW_KK_threshold)
  - computations/session-100a/s100a_freezein_overconstrained.npz  (HARD: S0_fit, W3-9)
  - script bytes (feeds BOTH audit_sha256 and content_sha256)

Output 4-tuple:
  (value=<computed>, scheme=FW, convention=RATIO, L_max=N/A)

METHODOLOGY (plan SectionW3-11 method, executed exactly)
--------------------------------------------------------
  (1) eps_LX-split scale Delta_omega = 0.9 M_KK (plan pin, post shape-preserving-
      squaring halving) and horizon kappa_SONIC = 2*pi*T_acoustic computed from the
      CANONICAL T_acoustic = 0.112 M_KK (S63) — provenance-clean by construction,
      NOT a hardcoded literal. Sage-exact identity: T_acoustic = 14/125 exactly, so
      kappa_SONIC = 28/125*pi (cross-checked bit-identical in-script).
  (2) S0_threshold = Delta_omega / kappa_SONIC, assembled from KK-THRESHOLD-64
      machinery quantities ONLY (delta = 2.35, m_H = m_H_FW_KK_threshold = 131.8 GeV
      canonical import, promoted S100a W4-13; the threshold sets the eps_LX-split
      scale). NO free normalization enters the candidate.
  (3) Compare against S0_fit consumed from the W3-9 npz (HARD within-wave input;
      orchestrator-verified landed). Upstream honesty: W3-9 composite FAIL (Track B
      0.90 — the 12-slot over-constraint broke on the quark/CKM held-out set) BUT the
      charged-lepton SHAPE leg survived exactly (lepton fit resid 2.2e-16), so the
      threshold-fixing question on the FITTED S0 is well-posed per the orchestrator
      override + the plan's own W3-9-INFO branch language ("W3-10/W3-11 run on the
      partial S0 with their own bands").
  (4) Three-band verdict per the pre-registered operator above.

SUBSTITUTION CHAIN (plan SectionW3-11 item 7; substituted numbers + [SIGN] read-off)
------------------------------------------------------------------------------------
  Claim: "S0 is FIXED by the KK-threshold => magnitude and slope close JOINTLY".
  Step 1 — Definitions:
    S0_fit       = 1.6941531565757249            [W3-9 npz key S0_fit; consumed not hardcoded]
    Delta_omega  = 0.9 M_KK                      [plan pin; eps_LX one-fiber-gap split scale]
    kappa_SONIC  = 2*pi*T_acoustic = 28/125*pi   [canonical T_acoustic = 0.112 = 14/125 exact]
                 = 0.7037167544041136...         [float64; plan's 16-digit Sage rounding
                                                  0.7037167544041137 agrees to 1 ulp]
    S0_threshold = Delta_omega / kappa_SONIC     [threshold-derived candidate, NO free norm]
  Step 2 — Substitution (no simplification):
    S0_threshold = 0.9 / (28/125*pi) = 0.9 / 0.70371675440411...
  Step 3 — Simplify (one step per line):
    S0_threshold = 1.2789236498455876            [= (125/28)*0.9/pi*... = 4 sig figs 1.279]
    ratio        = S0_threshold / S0_fit = 1.2789236498/1.6941531566 = 0.7549043868
    ratio_dev    = |0.7549043868 - 1| = 0.2450956132
  Step 4 — Direction read-off (the JOINT-closure question):
    The envelope is exp(-S0*C2). MAGNITUDE is set by S0; SLOPE across sectors is set
    by the C2-grading (4/3, 3, 6) — fixed representation theory, threshold-independent.
    The [SIGN] directional leg of the threshold identification:
      sign_verdict = PASS iff (S0_threshold > 0: the candidate points in the
      SUPPRESSION direction of the envelope, inheriting the C2-ordered sign the W3-9
      chain Step 5 pre-registered and PASSed) AND (|log10(S0_threshold/S0_fit)| <= 0.5:
      OOM-commensurate, the plan's own "threshold-constrained to O(1)" / "no threshold
      relation" band vocabulary operationalized on the order axis).
    Computed: S0_threshold = +1.2789 > 0 (suppression direction holds) AND
      log10(ratio) = -0.1221, |.| <= 0.5 (same OOM)  =>  sign_verdict = PASS.
  Step 5 — Verdict direction (signed, three-band):
    ratio_dev = 0.2451:  0.05 < 0.2451 <= 0.5  =>  band_verdict = INFO
    => S0 is threshold-constrained to O(1) with a 1-parameter residual knob;
       NOT threshold-fixed at 5% (PASS refuted), NOT threshold-independent (FAIL refuted).
  Conclusion: magnitude does NOT close jointly with the slope at the 5% no-free-norm
    band; the residual normalization knob (= S0_fit/S0_threshold) is the carry-forward.

POST-HOC DIAGNOSTICS (reported, NOT gated; sharpen the INFO-band knob)
----------------------------------------------------------------------
  knob = S0_fit/S0_threshold = 1.324671 — two threshold-internal candidate
  identifications (both post-hoc, flagged as such):
    (a) knob vs C2(1,0) = 4/3: dev 0.65%  [one fundamental-Casimir quantum:
        S0_fit ~= C2(1,0) * Delta_omega / kappa_SONIC]
    (b) Delta_omega_req = S0_fit*kappa_SONIC = 1.192204 M_KK vs delta/2 = 1.175
        (KK-THRESHOLD-64 delta = 2.35 HALVED — the same halving operation the
        Delta_omega = 0.9 pin language cites): dev 1.46%; equivalently
        S0_alt = (delta/2)/kappa_SONIC = 1.669706, ratio_dev_alt = 0.0144 — a
        would-be PASS-band value had the split scale been pinned delta/2, but the
        PRE-REGISTERED pin is 0.9 and the verdict stands on it.
  Robustness: both W3-9 lepton diagonal legs give the SAME band (S0(mu/e) = 1.7772
  -> dev 0.2804; S0(tau/mu) = 1.6934 -> dev 0.2448; both INFO) — the band verdict is
  not an artifact of the joint-fit weighting.

DISCIPLINE
----------
- from canonical_constants import *  (T_acoustic, m_H_FW_KK_threshold — the latter
  promoted to canonical this session by W4-13; imported, NOT pinned as a literal)
- locals tagged # (local); scalar arithmetic, GPU not needed (plan GPU_path pin:
  numpy.linalg, CPU trivial; OMP capped at 8 BEFORE numpy import)
- SHA-256 of inputs logged in first 20 lines; S84+ dual-SHA
- verdict PRINTED as emit_verdict payload (race-safe MCP single-writer); NO
  open("a") append (S98 Windows lost-update race); exit 0 on script success
  regardless of scientific verdict (math-scripts.md exit-code semantics)
- publication precision 4 sig figs for S0_threshold (plan pin); full float64 to npz;
  downstream verifiers use rel_tol >= 1e-4 (Class-8.3)
"""

from __future__ import annotations

# --- CPU thread cap BEFORE numpy import (math-scripts.md; scalar CPU path) ---
import os
os.environ.setdefault("OMP_NUM_THREADS", "8")
os.environ.setdefault("MKL_NUM_THREADS", "8")

import sys
from pathlib import Path

SESSION_DIR = Path(__file__).resolve().parent
COMPUTATIONS_DIR = SESSION_DIR.parent
SHARED_DIR = COMPUTATIONS_DIR / "_shared"
PROJECT_ROOT = COMPUTATIONS_DIR.parent
sys.path.insert(0, str(SHARED_DIR))

# ---------------------------------------------------------------------------
# Section 1 — Canonical constants (MANDATORY first project import)
# ---------------------------------------------------------------------------
from canonical_constants import *  # noqa: F401,F403

import hashlib
import json
import math
import time
from fractions import Fraction

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# ---------------------------------------------------------------------------
# Section 2 — Identity + pre-registered machinery pins (plan SectionW3-11)
# ---------------------------------------------------------------------------
SESSION = "100a"                                   # (local)
GATE_ID = "S100a-S0-THRESHOLD-JOINT"               # (local)
SCHEME = "FW"                                      # (local)
CONVENTION = "RATIO"                               # (local)
L_MAX = "N/A"                                      # (local) scalar threshold quantities; no D_K diagonalization

PASS_BAND = 0.05    # (local) plan SectionW3-11 strict_PASS_boundary (pre-registered gate band, RATIO convention)
INFO_BAND = 0.50    # (local) plan SectionW3-11 operator: INFO in (0.05, 0.5]; FAIL > 0.5 (pre-registered)
OOM_SIGN_BAND = 0.5 # (local) plan band vocabulary "O(1)/no relation" operationalized: |log10 ratio| <= 0.5 same-OOM (sign leg)

DELTA_OMEGA_PIN = 0.9        # (local) M_KK; eps_LX-split scale plan pin (post shape-preserving-squaring halving)
KK_THRESHOLD_DELTA = 2.35    # (local) KK-THRESHOLD-64 delta (S64 W4-B gate record; outside its own PASS band [0.73,1.48]); context + diagnostic
C2_FUND = 4.0 / 3.0          # (local) SU(3) quadratic Casimir C2(1,0); diagnostic comparator for the residual knob
C2_VEC = (4.0 / 3.0, 3.0, 6.0)  # (local) C2 for (1,0)/(1,1)/(3,0); the SLOPE leg (representation-fixed, threshold-independent)
PUB_SIGFIGS = 4              # (local) plan publication_precision pin (S0_threshold at 4 sig figs)

OUT_NPZ = SESSION_DIR / "s100a_s0_threshold_joint.npz"
OUT_PNG = SESSION_DIR / "s100a_s0_threshold_joint.png"
FREEZEIN_NPZ = SESSION_DIR / "s100a_freezein_overconstrained.npz"

INPUT_FILES = [
    SHARED_DIR / "canonical_constants.py",
    FREEZEIN_NPZ,
]


# ---------------------------------------------------------------------------
# Section 3 — SHA-256 input-pin block (S84+ dual-SHA; template-canonical)
# ---------------------------------------------------------------------------

def sha256_of(path: Path) -> str:
    """SHA-256 of a file's bytes; empty string on missing/unreadable."""
    h = hashlib.sha256()  # (local)
    try:
        h.update(path.read_bytes())
    except OSError:
        return ""
    return h.hexdigest()


def log_input_pins(inputs: list[Path]) -> dict[str, str]:
    """Print SHA-256 of each input; return {relpath: sha} for the closure hash."""
    print(f"=== {GATE_ID} — input SHA-256 pins ===")
    pins: dict[str, str] = {}
    for p in inputs:
        sha = sha256_of(p)  # (local)
        rel = str(p.relative_to(PROJECT_ROOT)).replace("\\", "/")  # (local)
        print(f"  {rel}: {sha[:16]}...")
        pins[rel] = sha
    return pins


def compute_dual_sha(script_path: Path, canonical_path: Path,
                     pins: dict[str, str]) -> tuple[str, str]:
    """(audit_sha256, content_sha256) per S84+ dual-SHA schema.

    audit_sha256   = sha256( bytes(script) || bytes(canonical) || pinmap_json )
    content_sha256 = sha256( bytes(script) )
    """
    script_bytes = script_path.read_bytes()        # (local)
    canonical_bytes = canonical_path.read_bytes()  # (local)
    pinmap_json = json.dumps(
        dict(sorted(pins.items())), separators=(",", ":"), sort_keys=True
    ).encode("utf-8")  # (local)

    h_audit = hashlib.sha256()  # (local)
    h_audit.update(script_bytes)
    h_audit.update(canonical_bytes)
    h_audit.update(pinmap_json)

    h_content = hashlib.sha256()  # (local)
    h_content.update(script_bytes)
    return h_audit.hexdigest(), h_content.hexdigest()


def round_sigfigs(x: float, n: int) -> float:
    """Round x to n significant figures (publication-precision helper)."""
    if x == 0.0:
        return 0.0
    return round(x, -int(math.floor(math.log10(abs(x)))) + (n - 1))


# ---------------------------------------------------------------------------
# Section 4 — Compute
# ---------------------------------------------------------------------------

def compute() -> dict:
    # (3a) HARD within-wave prereq: W3-9 npz must carry S0_fit (orchestrator-verified
    # landed; the mechanical-closure branch below is the plan's if-absent contract).
    if not FREEZEIN_NPZ.exists():
        raise FileNotFoundError(
            "PRE-REG-INC_blocked_by_S100a-FREEZEIN-OVERCONSTRAINED_unlanded: "
            f"{FREEZEIN_NPZ} absent — honest closure per mechanical-closure-discipline.md"
        )
    d = np.load(FREEZEIN_NPZ, allow_pickle=True)  # (local)
    S0_fit = float(d["S0_fit"])                   # (local) consumed from npz, never hardcoded
    S0_leg_mue = float(d["S0_leg_mue"])           # (local) W3-9 lepton diagonal leg mu/e
    S0_leg_taumu = float(d["S0_leg_taumu"])       # (local) W3-9 lepton diagonal leg tau/mu
    upstream_verdict = str(d["verdict"])          # (local) W3-9 composite (FAIL, Track B 0.90)
    upstream_resid = float(d["lepton_fit_resid_max"])  # (local) SHAPE-leg survival witness

    # (1) kappa_SONIC from the CANONICAL T_acoustic (substrate-first; provenance-clean)
    kappa_SONIC = 2.0 * math.pi * T_acoustic      # (local) M_KK; T_acoustic = 0.112 canonical S63

    # Sage-exactness cross-checks: T_acoustic = 0.112 = 14/125 exactly => kappa = 28/125*pi
    t_ac_frac_dev = abs(T_acoustic - 14.0 / 125.0)              # (local) expect 0.0 bit-exact
    kappa_frac_float = float(Fraction(28, 125)) * math.pi       # (local) 28/125*pi float64 image
    kappa_bit_identical = bool(kappa_SONIC == kappa_frac_float)  # (local) expect True
    PLAN_KAPPA_LITERAL = 0.7037167544041137                     # (local) plan's 16-digit Sage rounding (cross-check ONLY, not consumed)
    kappa_vs_plan_literal = abs(kappa_SONIC - PLAN_KAPPA_LITERAL)  # (local) expect <= 1 ulp ~ 1.1e-16

    # (2) Threshold-derived candidate — KK-THRESHOLD-64 quantities only, NO free norm
    S0_threshold = DELTA_OMEGA_PIN / kappa_SONIC  # (local) the candidate

    # (3) Ratio comparison against the fitted S0
    ratio = S0_threshold / S0_fit                 # (local)
    ratio_dev = abs(ratio - 1.0)                  # (local) the gate observable
    log10_ratio = math.log10(ratio)               # (local) OOM-commensurability (sign leg)

    # Per-leg robustness (diagnostic, NOT gated)
    ratio_dev_leg_mue = abs(S0_threshold / S0_leg_mue - 1.0)      # (local)
    ratio_dev_leg_taumu = abs(S0_threshold / S0_leg_taumu - 1.0)  # (local)

    # POST-HOC diagnostics sharpening the INFO-band residual knob (NOT gated)
    knob = S0_fit / S0_threshold                                  # (local) residual normalization knob
    knob_vs_C2fund_dev = abs(knob / C2_FUND - 1.0)                # (local) candidate (a): one C2(1,0) quantum
    Dw_req = S0_fit * kappa_SONIC                                 # (local) split scale that WOULD close exactly
    half_delta = KK_THRESHOLD_DELTA / 2.0                         # (local) KK-THRESHOLD-64 delta halved
    Dw_req_vs_half_delta_dev = abs(Dw_req / half_delta - 1.0)     # (local) candidate (b)
    S0_alt_halfdelta = half_delta / kappa_SONIC                   # (local) would-be candidate at Dw = delta/2
    ratio_dev_alt_halfdelta = abs(S0_alt_halfdelta / S0_fit - 1.0)  # (local) would-be band position (post-hoc)

    # ---- [SIGN] 3-tuple legs (gate-verdicts.md schema-v2) ----
    suppression_direction_ok = bool(S0_threshold > 0.0)           # (local) envelope exp(-S0*C2) suppression sign
    same_oom_ok = bool(abs(log10_ratio) <= OOM_SIGN_BAND)         # (local) O(1)-commensurability
    sign_verdict = "PASS" if (suppression_direction_ok and same_oom_ok) else "FAIL"  # (local)

    if ratio_dev <= PASS_BAND:
        magnitude_verdict = "PASS"   # (local)
        band_verdict = "PASS"        # (local)
    elif ratio_dev <= INFO_BAND:
        magnitude_verdict = "INFO"   # (local)
        band_verdict = "INFO"        # (local)
    else:
        magnitude_verdict = "FAIL"   # (local)
        band_verdict = "FAIL"        # (local)

    # Regime: exact scalar arithmetic on canonical/exact inputs; no expansion window,
    # no scan, no truncation — the RATIO convention is well-defined throughout.
    regime_verdict = "VALID"  # (local)

    # Composite collapse rule (gate-verdicts.md schema-v2; pre-registered)
    if regime_verdict == "BREAKDOWN":
        composite = "FAIL"           # (local)
    elif sign_verdict == "FAIL":
        composite = "FAIL"           # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "VALID":
        composite = "FAIL"           # (local)
    elif magnitude_verdict == "FAIL" and regime_verdict == "MARGINAL":
        composite = "INFO"           # (local)
    elif magnitude_verdict == "INFO":
        composite = "INFO"           # (local)
    else:
        composite = "PASS"           # (local)

    return dict(
        S0_fit=S0_fit, S0_leg_mue=S0_leg_mue, S0_leg_taumu=S0_leg_taumu,
        upstream_verdict=upstream_verdict, upstream_resid=upstream_resid,
        kappa_SONIC=kappa_SONIC, t_ac_frac_dev=t_ac_frac_dev,
        kappa_bit_identical=kappa_bit_identical,
        kappa_vs_plan_literal=kappa_vs_plan_literal,
        S0_threshold=S0_threshold, ratio=ratio, ratio_dev=ratio_dev,
        log10_ratio=log10_ratio,
        ratio_dev_leg_mue=ratio_dev_leg_mue, ratio_dev_leg_taumu=ratio_dev_leg_taumu,
        knob=knob, knob_vs_C2fund_dev=knob_vs_C2fund_dev,
        Dw_req=Dw_req, half_delta=half_delta,
        Dw_req_vs_half_delta_dev=Dw_req_vs_half_delta_dev,
        S0_alt_halfdelta=S0_alt_halfdelta,
        ratio_dev_alt_halfdelta=ratio_dev_alt_halfdelta,
        sign_verdict=sign_verdict, magnitude_verdict=magnitude_verdict,
        regime_verdict=regime_verdict, band_verdict=band_verdict,
        composite=composite,
    )


# ---------------------------------------------------------------------------
# Section 5 — Plot
# ---------------------------------------------------------------------------

def make_plot(r: dict) -> None:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12.5, 5.2))  # (local)

    # Panel 1 — S0 values: fitted vs threshold-derived (+ diagnostics)
    names = ["S0_fit\n(W3-9 joint)", "S0_threshold\n(Dw=0.9 pin)",
             "S0_alt\n(Dw=delta/2, diag)"]                       # (local)
    vals = [r["S0_fit"], r["S0_threshold"], r["S0_alt_halfdelta"]]  # (local)
    cols = ["#2c5f8a", "#c0392b", "#e6a23c"]                     # (local)
    bars = ax1.bar(names, vals, color=cols, alpha=0.85, width=0.6)  # (local)
    ax1.axhline(r["S0_fit"], color="#2c5f8a", ls="--", lw=1.0, alpha=0.7)
    ax1.scatter([0, 0], [r["S0_leg_mue"], r["S0_leg_taumu"]], marker="_",
                s=600, color="k", zorder=5,
                label="W3-9 lepton legs (mu/e, tau/mu)")
    ax1.scatter([1], [C2_FUND * r["S0_threshold"]], marker="D", s=55,
                color="#7d3c98", zorder=5,
                label="(4/3)*S0_threshold (knob diag)")
    for b, v in zip(bars, vals):
        ax1.text(b.get_x() + b.get_width() / 2, v + 0.02, f"{v:.4f}",
                 ha="center", fontsize=9)
    ax1.set_ylabel("S0  (envelope exponent scale)")
    ax1.set_title("Threshold candidate vs fitted S0")
    ax1.legend(fontsize=8, loc="lower right")
    ax1.grid(axis="y", alpha=0.3)

    # Panel 2 — ratio_dev on the pre-registered three-band axis
    ax2.axvspan(0.0, PASS_BAND, color="#2ecc71", alpha=0.30,
                label=f"PASS <= {PASS_BAND}")
    ax2.axvspan(PASS_BAND, INFO_BAND, color="#f1c40f", alpha=0.30,
                label=f"INFO ({PASS_BAND}, {INFO_BAND}]")
    ax2.axvspan(INFO_BAND, 0.72, color="#e74c3c", alpha=0.25,
                label=f"FAIL > {INFO_BAND}")
    ax2.scatter([r["ratio_dev"]], [0.55], s=190, color="k", zorder=6,
                label=f"ratio_dev = {r['ratio_dev']:.4f} (GATE)")
    ax2.scatter([r["ratio_dev_leg_mue"], r["ratio_dev_leg_taumu"]],
                [0.40, 0.40], s=70, color="#34495e", marker="s", zorder=5,
                label="per-leg devs (mu/e, tau/mu)")
    ax2.scatter([r["ratio_dev_alt_halfdelta"]], [0.25], s=80, color="#e6a23c",
                marker="^", zorder=5,
                label=f"diag Dw=delta/2: {r['ratio_dev_alt_halfdelta']:.4f}")
    ax2.scatter([r["knob_vs_C2fund_dev"]], [0.12], s=80, color="#7d3c98",
                marker="D", zorder=5,
                label=f"diag knob vs 4/3: {r['knob_vs_C2fund_dev']:.4f}")
    ax2.set_xlim(0, 0.72)
    ax2.set_ylim(0, 0.75)
    ax2.set_yticks([])
    ax2.set_xlabel("ratio_dev = |S0_threshold/S0_fit - 1|")
    ax2.set_title(f"Three-band verdict: {r['band_verdict']}  "
                  f"(sign={r['sign_verdict']}, mag={r['magnitude_verdict']}, "
                  f"regime={r['regime_verdict']})")
    ax2.legend(fontsize=8, loc="upper right")

    fig.suptitle(f"{GATE_ID} — is S0 fixed by the KK-threshold machinery?  "
                 f"composite = {r['composite']}", fontsize=12)
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    fig.savefig(OUT_PNG, dpi=130)
    plt.close(fig)
    print(f"  plot -> {OUT_PNG.name}")


# ---------------------------------------------------------------------------
# Section 6 — emit_verdict payload printer (race-safe MCP single-writer path)
# ---------------------------------------------------------------------------

def print_verdict_payload(verdict: str, value, audit_sha: str, content_sha: str,
                          sign_verdict: str, magnitude_verdict: str,
                          regime_verdict: str, companion_note: str = "",
                          extra_rows: list[str] | None = None) -> dict:
    """PRINT the verdict payload for the dispatching agent -> mcp emit_verdict.

    The script does NOT write the verdict file (S98 Windows open("a") race);
    the lock-serialized write is owned by the emit_verdict knowledge-MCP tool.
    [SIGN] gate: all three of sign/magnitude/regime are carried (schema-v2).
    """
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
        "sign_verdict": sign_verdict,
        "magnitude_verdict": magnitude_verdict,
        "regime_verdict": regime_verdict,
    }
    if companion_note:
        payload["companion_note"] = companion_note
    if extra_rows:
        payload["extra_rows"] = list(extra_rows)
    print("<<<EMIT_VERDICT_PAYLOAD>>>")
    print(json.dumps(payload, separators=(",", ":"), sort_keys=True))
    print("<<<END_EMIT_VERDICT_PAYLOAD>>>")
    return payload


# ---------------------------------------------------------------------------
# Section 7 — Main
# ---------------------------------------------------------------------------

def main() -> int:
    t0 = time.time()  # (local)

    pins = log_input_pins(INPUT_FILES)  # (local)
    script_path = Path(__file__).resolve()                 # (local)
    canonical_path = SHARED_DIR / "canonical_constants.py"  # (local)
    audit_sha, content_sha = compute_dual_sha(script_path, canonical_path, pins)  # (local)
    print(f"  audit_sha256:   {audit_sha[:16]}... (script+canonical+pinmap)")
    print(f"  content_sha256: {content_sha[:16]}... (script only)")
    print()

    r = compute()  # (local)

    # ---- NUMBERS first ----
    print("=== NUMBERS (substituted chain) ===")
    print(f"  T_acoustic (canonical S63)        = {T_acoustic!r}  "
          f"[= 14/125 exact: dev {r['t_ac_frac_dev']:.3e}]")
    print(f"  kappa_SONIC = 2*pi*T_acoustic     = {r['kappa_SONIC']!r}  M_KK")
    print(f"    28/125*pi bit-identical:          {r['kappa_bit_identical']}")
    print(f"    vs plan 16-digit Sage rounding:   dev {r['kappa_vs_plan_literal']:.3e} (<= 1 ulp)")
    print(f"  Delta_omega (plan pin)            = {DELTA_OMEGA_PIN}  M_KK")
    print(f"  KK-THRESHOLD-64: delta = {KK_THRESHOLD_DELTA}, m_H = {m_H_FW_KK_threshold} GeV (canonical import)")
    print(f"  S0_threshold = Dw/kappa           = {r['S0_threshold']!r}  "
          f"[4 sig figs: {round_sigfigs(r['S0_threshold'], PUB_SIGFIGS)}]")
    print(f"  S0_fit (W3-9 npz, consumed)       = {r['S0_fit']!r}")
    print(f"  ratio = S0_threshold/S0_fit       = {r['ratio']!r}")
    print(f"  ratio_dev = |ratio - 1|           = {r['ratio_dev']!r}")
    print(f"  log10(ratio)                      = {r['log10_ratio']:.6f}  (same-OOM leg)")
    print(f"  per-leg devs (mu/e, tau/mu)       = ({r['ratio_dev_leg_mue']:.4f}, {r['ratio_dev_leg_taumu']:.4f})")
    print()
    print("=== GATE (pre-registered three-band, RATIO) ===")
    print(f"  PASS <= {PASS_BAND} | INFO ({PASS_BAND}, {INFO_BAND}] | FAIL > {INFO_BAND}")
    print(f"  band_verdict      = {r['band_verdict']}")
    print(f"  sign_verdict      = {r['sign_verdict']}  (S0_threshold > 0 suppression dir AND |log10 ratio| <= {OOM_SIGN_BAND})")
    print(f"  magnitude_verdict = {r['magnitude_verdict']}")
    print(f"  regime_verdict    = {r['regime_verdict']}")
    print(f"  composite         = {r['composite']}")
    print()
    print("=== DIAGNOSTICS (post-hoc, NOT gated) ===")
    print(f"  knob = S0_fit/S0_threshold        = {r['knob']!r}")
    print(f"    vs C2(1,0) = 4/3:                 dev {r['knob_vs_C2fund_dev']:.4%}")
    print(f"  Dw_req = S0_fit*kappa             = {r['Dw_req']!r}  M_KK")
    print(f"    vs delta/2 = {r['half_delta']}:               dev {r['Dw_req_vs_half_delta_dev']:.4%}")
    print(f"  S0_alt(delta/2) = {r['S0_alt_halfdelta']:.6f}; ratio_dev_alt = {r['ratio_dev_alt_halfdelta']:.4f} (would-be PASS-band; post-hoc)")
    print(f"  upstream W3-9: {r['upstream_verdict']} (lepton SHAPE-leg resid {r['upstream_resid']:.2e} — S0_fit well-posed)")
    print()

    # ---- npz (required keys + diagnostics; full float64) ----
    np.savez(
        OUT_NPZ,
        # required keys (plan output_artifacts data block)
        S0_threshold=r["S0_threshold"],
        S0_fit_consumed=r["S0_fit"],
        ratio_dev=r["ratio_dev"],
        Delta_omega=DELTA_OMEGA_PIN,
        kappa_SONIC=r["kappa_SONIC"],
        band_verdict=r["band_verdict"],
        # chain + cross-checks
        ratio=r["ratio"], log10_ratio=r["log10_ratio"],
        T_acoustic_used=T_acoustic,
        kappa_frac_num=28, kappa_frac_den=125,
        kappa_bit_identical=r["kappa_bit_identical"],
        kappa_vs_plan_literal_dev=r["kappa_vs_plan_literal"],
        t_ac_frac_dev=r["t_ac_frac_dev"],
        KK_threshold_delta=KK_THRESHOLD_DELTA,
        m_H_FW_KK_threshold_used=m_H_FW_KK_threshold,
        C2_vec=np.array(C2_VEC),
        # per-leg robustness
        S0_leg_mue=r["S0_leg_mue"], S0_leg_taumu=r["S0_leg_taumu"],
        ratio_dev_leg_mue=r["ratio_dev_leg_mue"],
        ratio_dev_leg_taumu=r["ratio_dev_leg_taumu"],
        # post-hoc knob diagnostics
        knob=r["knob"], knob_vs_C2fund_dev=r["knob_vs_C2fund_dev"],
        Dw_req=r["Dw_req"], half_delta=r["half_delta"],
        Dw_req_vs_half_delta_dev=r["Dw_req_vs_half_delta_dev"],
        S0_alt_halfdelta=r["S0_alt_halfdelta"],
        ratio_dev_alt_halfdelta=r["ratio_dev_alt_halfdelta"],
        # upstream + identity + verdict block
        upstream_w3_9_verdict=r["upstream_verdict"],
        upstream_lepton_resid_max=r["upstream_resid"],
        gate_id=GATE_ID, scheme=SCHEME, convention=CONVENTION, l_max=L_MAX,
        sign_verdict=r["sign_verdict"], magnitude_verdict=r["magnitude_verdict"],
        regime_verdict=r["regime_verdict"], verdict=r["composite"],
        pass_band=PASS_BAND, info_band=INFO_BAND,
        publication_sigfigs=PUB_SIGFIGS,
        audit_sha256=audit_sha, content_sha256=content_sha,
        schema_version="S84+",
    )
    print(f"  npz  -> {OUT_NPZ.name}")

    make_plot(r)
    print()

    # ---- 4-tuple (final non-verdict line) + emit_verdict payload ----
    s0t_pub = round_sigfigs(r["S0_threshold"], PUB_SIGFIGS)   # (local) 4-sig-fig publication form
    value_payload = (
        f"S0_thr={s0t_pub};S0_fit={r['S0_fit']:.4f};ratio={r['ratio']:.4f};"
        f"ratio_dev={r['ratio_dev']:.4f}_band({PASS_BAND},{INFO_BAND}]=INFO;"
        f"Dw={DELTA_OMEGA_PIN};kappa=28/125pi={r['kappa_SONIC']:.5f};"
        f"knob={r['knob']:.4f}_vs_4/3_dev{r['knob_vs_C2fund_dev']:.2%};"
        f"Dw_req={r['Dw_req']:.4f}_vs_delta/2={r['half_delta']}_dev{r['Dw_req_vs_half_delta_dev']:.2%};"
        f"legs_dev=({r['ratio_dev_leg_mue']:.4f},{r['ratio_dev_leg_taumu']:.4f});"
        f"upstream_W3-9={r['upstream_verdict']}_shape-leg-survived"
    )  # (local)
    print(f"(value={value_payload!r}, scheme={SCHEME}, convention={CONVENTION}, L_max={L_MAX})")

    companion = (
        "S0 threshold-CONSTRAINED to O(1), NOT threshold-fixed at 5%: residual knob "
        f"{r['knob']:.4f} (1-param carry-forward); magnitude does NOT close jointly with "
        "the representation-fixed C2 slope at the no-free-norm band"
    )  # (local)
    extra = [
        f"# regulator_pin=N/A (KK-THRESHOLD-64 supplies delta={KK_THRESHOLD_DELTA} / m_H={m_H_FW_KK_threshold} GeV canonical import; no Seeley-DeWitt a_n consumed) # {GATE_ID}",
        (f"# diagnostics(non-verdict): knob=S0_fit/S0_thr={r['knob']:.6f} vs C2(1,0)=4/3 dev={r['knob_vs_C2fund_dev']:.4%}; "
         f"Dw_req=S0_fit*kappa={r['Dw_req']:.6f} vs delta/2={r['half_delta']} dev={r['Dw_req_vs_half_delta_dev']:.4%}; "
         f"S0_alt(delta/2)={r['S0_alt_halfdelta']:.6f} ratio_dev_alt={r['ratio_dev_alt_halfdelta']:.4f} (would-be PASS-band; post-hoc NOT gated) # {GATE_ID}"),
        (f"# upstream: W3-9 {r['upstream_verdict']} (Track B 0.90, over-constraint broke) BUT charged-lepton SHAPE leg exact "
         f"(resid {r['upstream_resid']:.2e}); S0_fit well-posed; legs S0(mue)={r['S0_leg_mue']:.4f} S0(taumu)={r['S0_leg_taumu']:.4f} "
         f"band-robust INFO (dev {r['ratio_dev_leg_mue']:.4f}/{r['ratio_dev_leg_taumu']:.4f}) # {GATE_ID}"),
    ]  # (local)
    print_verdict_payload(r["composite"], value_payload, audit_sha, content_sha,
                          r["sign_verdict"], r["magnitude_verdict"],
                          r["regime_verdict"], companion_note=companion,
                          extra_rows=extra)

    wall = time.time() - t0  # (local)
    print(f"\n=== {GATE_ID}: {r['composite']} (wall {wall:.1f}s) ===")
    return 0  # script success regardless of scientific verdict (math-scripts.md)


if __name__ == "__main__":
    sys.exit(main())
